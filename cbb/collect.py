#!/usr/bin/env python3
"""Propwatch CBB collector. Long-running snapshot loop for a GitHub Actions runner.

What differs from the NFL collector, and why:

* OPENERS ARE CAUGHT CONTINUOUSLY. There is no weekly reset in college basketball.
  The FanDuel lobby carries main lines for every listed game in one request, so it is
  swept every cycle and each game's first posted number is recorded the cycle it
  appears (cbb/state/collector.json -> openers). caught=false means the game was
  already posted when the collector looked -- that is the first number WE saw, not
  the opener, and it must not be treated as one.

* GAME MARKETS FIRST. Full game, halves, totals, team totals are the focus: the CBB
  edge is early lines and early movement. Player props are kept only if FanDuel
  happens to post them (rare in CBB) -- collected, never prioritised.

* ACTION NETWORK BOOK 30 IS THE OPENING LINE. Across 103 NFL snapshots its number
  never moved while every other book moved in 12-23 of 29 games. It is recorded
  for every game as openers.an[gid].open, so a game posted before the collector
  looked still has its true opener.

* VOLUME IS FILTERED BY MEASURED DEPTH, NOT A CONFERENCE LIST. Every game gets its
  main lines every cycle. Per-event half/team-total pulls are tiered by tip time.
  Two depth measures are stored on every row so the grader can bucket by them:
    - Action Network num_bets (ticket count) on split rows
    - Pinnacle maxRiskStake (the sharp book's own limit) on Pinnacle rows

* ROWS ARE DELTA-ENCODED. A December Tuesday is ~10x an NFL slate. Each cycle writes
  only rows whose line/price/status changed; every KF_N cycles (and the first cycle
  of every job) writes a full keyframe, named <ts>-k.jsonl.gz. Readers build sparse
  series: a value holds until the next row for that key. Count SNAPSHOTS by
  keyframes or by elapsed time, never by rows per key.

* ENDPOINTS ARE DISCOVERED, NOT ASSUMED. The CBB page IDs, Pinnacle league ID and
  VSIN sport code have not been verified (sportsbook domains are blocked from the
  analysis container). Each job start tries the variants and writes what worked to
  cbb/data/_probe.json.

Barttorvik is not collected: it answers HTTP 403 to GitHub runners (hoopR-mbb-data
build log, 2026-11-03). Scheme data comes from hoopR-mbb-data instead.
"""
import gzip, json, os, re, subprocess, sys, time
from datetime import datetime, timezone, timedelta
from urllib.request import Request, urlopen

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
P = lambda *a: os.path.join(ROOT, "cbb", *a)

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36",
      "Accept": "application/json,text/html,*/*", "Accept-Language": "en-US,en;q=0.9"}
PIN = {"X-API-Key": "CmX2KcMrXuFmNg6YFbmTxE0y9CIrOi0R"}
AK = "FhMFpcPWXMeyZxOx"
FD = "https://sbapi.nj.sportsbook.fanduel.com/api"
AN = "https://api.actionnetwork.com/web/v2/scoreboard/ncaab"
PINB = "https://guest.api.arcadia.pinnacle.com/0.1"
ESPN = ("https://site.api.espn.com/apis/site/v2/sports/basketball/"
        "mens-college-basketball/scoreboard?groups=50&limit=500&dates=")
REFBOOK = "69"                     # FanDuel on Action Network (verified on NFL)
OPENBOOK = "30"                    # Action Network's opening line: never moves, no splits

CYCLE    = int(os.environ.get("CYCLE", 600))       # 10 min
RUNFOR   = int(os.environ.get("RUNFOR", 320 * 60))  # under the 6h job ceiling
KF_N     = 6       # keyframe every 6th cycle (hourly); deltas in between
ALLBOOK_N= 6       # every-book Action Network lines hourly; ref book every cycle
ESPN_N   = 6       # finals hourly
RAW_HOUR = 15      # full raw JSON once a day (first cycle at/after 15:00 UTC), on the
                   # very first run, and on the cycle after any parse error
PUSH_N   = 3       # commit every 30 min
REQ_BUDGET = 150   # FanDuel event-page requests per cycle (NFL used 112)
CYCLE_TIME_GUARD = 0.75
LINES_H  = 7 * 24  # lobby rows for games tipping within 7 days
DEEP_A_H = 12      # events with props tipping within 12h: all prop tabs every cycle
DEEP_B_H = 30      # within 30h: every 3rd cycle
OFFLINE  = os.environ.get("PW_OFFLINE")             # test hook: skip git

PROP_TAB = re.compile(r"(half|team|player|point|rebound|assist|three)", re.I)
SKIP_TAB = re.compile(r"(same game|parlay|quarter|popular|live)", re.I)
HALF_TABS = ["1st-half", "2nd-half"]
MAIN_MT = ("MATCH_HANDICAP_(2-WAY)", "TOTAL_POINTS_(OVER/UNDER)", "MONEY_LINE")


def now_utc(): return datetime.now(timezone.utc)
def tsfmt(t): return t.strftime("%Y-%m-%dT%H%MZ")
def parse_ts(s): return datetime.strptime(s, "%Y-%m-%dT%H%MZ").replace(tzinfo=timezone.utc)
def et_date(t, add=0): return (t - timedelta(hours=5) + timedelta(days=add)).strftime("%Y%m%d")
def slug(title): return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def get(url, extra=None, timeout=25):
    h = dict(UA); h.update(extra or {})
    with urlopen(Request(url, headers=h), timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def jload(path, default):
    try: return json.load(open(path))
    except Exception: return default


def jsave(path, obj, pretty=False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    json.dump(obj, open(tmp, "w"), sort_keys=True,
              **({"indent": 1} if pretty else {"separators": (",", ":")}))
    os.replace(tmp, path)


def write_gz(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8", compresslevel=9) as f: f.write(text)
    return os.path.getsize(path)


class Delta:
    """Write only rows whose value changed since the last cycle; full keyframe on demand."""
    def __init__(self, name, key, val):
        self.name, self.key, self.val, self.last = name, key, val, {}

    def write(self, rows, ts, day, keyframe):
        cur, out, occ = {}, [], {}
        for r in rows:
            k0 = self.key(r)                 # a runner can appear twice in
