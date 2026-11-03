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
            k0 = self.key(r)                 # a runner can appear twice in one market at
            occ[k0] = occ.get(k0, -1) + 1    # different handicaps: key by occurrence too
            k, v = (k0, occ[k0]), self.val(r)
            cur[k] = v
            if keyframe or self.last.get(k) != v: out.append(r)
        if keyframe: self.last = cur
        else: self.last.update(cur)
        if not out: return 0, 0
        fn = f"{ts}-k.jsonl.gz" if keyframe else f"{ts}.jsonl.gz"
        txt = "".join(json.dumps(r, separators=(",", ":")) + "\n" for r in out)
        return len(out), write_gz(P(self.name, day, fn), txt)


def skip_mt(mt):
    mt = mt or ""
    return any(x in mt for x in ("ALTERNATE", "_ALT_", "SGP", "OUTRIGHT", "FUTURE",
                                 "REGULAR_SEASON", "CHAMPION", "TOURNAMENT", "CONFERENCE_WINNER",
                                 "EXACT", "ODD/EVEN", "3-WAY", "HIGHEST_SCORING",
                                 "MARGIN", "RACE_TO", "FIRST_TO", "WINNING_MARGIN"))


def od_of(r):
    try: return r["winRunnerOdds"]["americanDisplayOdds"]["americanOdds"]
    except Exception: return None


# ---------------------------------------------------------------- discovery
def discover(day_et):
    """Try endpoint variants; keep whichever returns the most usable data."""
    probe = {"run_utc": now_utc().strftime("%Y-%m-%dT%H:%M:%SZ"), "tried": []}

    def attempt(kind, url, extra=None, score=None):
        rec = {"kind": kind, "url": url.replace(AK, "<ak>")}
        try:
            txt = get(url, extra); rec["bytes"] = len(txt)
            rec["score"] = score(txt) if score else len(txt)
        except Exception as e:
            rec["error"] = f"{type(e).__name__}: {str(e)[:120]}"; rec["score"] = -1
        probe["tried"].append(rec)
        return rec["score"], url

    def best(results):          # highest score; ties go to the FIRST (plainest) variant
        i = max(range(len(results)), key=lambda k: (results[k][0], -k))
        return results[i]

    def fd_score(t):
        ev = json.loads(t).get("attachments", {}).get("events", {})
        return sum(1 for v in ev.values() if "@" in str(v.get("name", "")))

    def an_score(t):
        return sum(1 for g in json.loads(t).get("games", []) if g.get("markets"))

    fd = best([attempt("fd_lobby", f"{FD}/content-managed-page?page=CUSTOM&customPageId={pid}&_ak={AK}",
                       score=fd_score)
               for pid in ("ncaab", "ncaa-basketball", "college-basketball", "ncaa-basketball-men")])
    an = best([attempt("actionnet", u, score=an_score) for u in (
        f"{AN}?period=game&date={day_et}",
        f"{AN}?period=game&division=D1&date={day_et}")])

    pin_league, pin_name = None, None
    try:
        lg = json.loads(get(f"{PINB}/sports/4/leagues?all=false", PIN))
        cands = [l for l in lg if "NCAA" in str(l.get("name", "")).upper()
                 and "WOMEN" not in str(l.get("name", "")).upper()]
        cands.sort(key=lambda l: (str(l.get("name")).strip().upper() != "NCAA",
                                  -(l.get("matchupCount") or 0)))
        if cands: pin_league, pin_name = cands[0]["id"], cands[0].get("name")
        probe["pin_leagues"] = [{"id": l.get("id"), "name": l.get("name"),
                                 "n": l.get("matchupCount")} for l in cands[:6]]
    except Exception as e:
        probe["pin_leagues_error"] = f"{type(e).__name__}: {str(e)[:120]}"
    if pin_league is None: pin_league, pin_name = 493, "fallback-493"

    vs = best([attempt("vsin", f"https://data.vsin.com/betting-splits/?sport={s}") for s in ("CBB", "NCAAB")])

    cfg = {"fd_lobby": fd[1] if fd[0] > 0 else None,
           "an_div": "&division=D1" if "division=D1" in an[1] else "", "an_ok": an[0] > 0,
           "pin_league": pin_league, "pin_name": pin_name,
           "vsin": vs[1] if vs[0] > 0 else None}
    probe["chosen"] = {k: (v.replace(AK, "<ak>") if isinstance(v, str) else v) for k, v in cfg.items()}
    jsave(P("data", "_probe.json"), probe, pretty=True)
    return cfg


# ---------------------------------------------------------------- extraction
def an_rows(txt, ts, allbooks, teams):
    """Splits are consensus (identical across book rows, verified on NFL), so only the
    ref book carries tix/mny. Other books carry line and juice only, hourly."""
    out = []
    for g in json.loads(txt).get("games", []):
        tm = {t["id"]: t for t in g.get("teams", [])}
        for tid, t in tm.items():
            if str(tid) not in teams:
                teams[str(tid)] = {"abbr": t.get("abbr"), "name": t.get("full_name"),
                                   "conf": t.get("conference_type"), "div": t.get("division_type")}
        a, h = tm.get(g.get("away_team_id"), {}), tm.get(g.get("home_team_id"), {})
        if not a or not h: continue
        base = {"t": ts, "gid": g.get("id"), "g": f"{a.get('abbr')}@{h.get('abbr')}",
                "st": g.get("start_time"), "ss": g.get("status"), "nb": g.get("num_bets"),
                "ac": a.get("conference_type"), "hc": h.get("conference_type")}
        for bid, blk in (g.get("markets") or {}).items():
            if bid not in (REFBOOK, OPENBOOK) and not allbooks: continue
            ev = (blk or {}).get("event") or {}
            for mkt in ("spread", "total", "moneyline"):
                for o in ev.get(mkt, []) or []:
                    r = dict(base); r.update({"b": bid, "m": mkt, "sd": o.get("side"),
                                              "tid": o.get("team_id"), "v": o.get("value"),
                                              "o": o.get("odds")})
                    if bid == REFBOOK:
                        bi = o.get("bet_info") or {}
                        r["tx"] = (bi.get("tickets") or {}).get("percent")
                        r["mn"] = (bi.get("money") or {}).get("percent")
                    out.append(r)
    return out


def fd_market_rows(markets, ts, evmeta, seen):
    out = []
    for m in markets.values():
        mt = m.get("marketType")
        if skip_mt(mt): continue
        eid = str(m.get("eventId"))
        if eid not in evmeta: continue
        nm, kick = evmeta[eid]
        for r in m.get("runners", []) or []:
            key = (eid, mt, m.get("marketName"), r.get("runnerName"), r.get("handicap"))
            if key in seen: continue
            seen.add(key)
            out.append({"t": ts, "e": eid, "g": nm, "k": kick, "mt": mt, "mn": m.get("marketName"),
                        "r": r.get("runnerName"), "h": r.get("handicap"), "o": od_of(r),
                        "s": r.get("runnerStatus")})
    return out


def pin_rows(mtxt, ptxt, ts):
    """Pinnacle primary (non-alternate) markets with the book's own stake limit.
    maxRiskStake is the sharpest liquidity measure available: Pinnacle raises limits
    as its confidence in a number grows, so it buckets market depth directly."""
    meta = {}
    for x in json.loads(mtxt):
        if x.get("type") != "matchup" or x.get("parentId") or x.get("isLive"): continue
        if str(x.get("units") or "Regular") != "Regular": continue
        pp = {p.get("alignment"): p.get("name") for p in x.get("participants", [])}
        if "home" in pp and "away" in pp:
            meta[x["id"]] = (f"{pp['away']} @ {pp['home']}", x.get("startTime"))
    out = []
    for m in json.loads(ptxt):
        if m.get("isAlternate") or m.get("matchupId") not in meta: continue
        g, k = meta[m["matchupId"]]
        lim = next((l.get("amount") for l in m.get("limits") or [] if l.get("type") == "maxRiskStake"), None)
        for pr in m.get("prices") or []:
            out.append({"t": ts, "mid": m["matchupId"], "g": g, "k": k, "ty": m.get("type"),
                        "per": m.get("period"), "side": m.get("side"), "d": pr.get("designation"),
                        "pts": pr.get("points"), "pr": pr.get("price"), "lim": lim,
                        "st": m.get("status")})
    return out


def espn_finals(txt):
    out = {}
    for e in json.loads(txt).get("events", []):
        try:
            c = e["competitions"][0]
            if not c["status"]["type"].get("completed"): continue
            d = {t["homeAway"]: t for t in c["competitors"]}
            ls = lambda t: [int(float(q.get("value", 0))) for q in (t.get("linescores") or [])]
            la, lh = ls(d["away"]), ls(d["home"])
            out[str(e["id"])] = {
                "date": e.get("date"), "neutral": c.get("neutralSite"),
                "away": d["away"]["team"].get("displayName"), "home": d["home"]["team"].get("displayName"),
                "away_abbr": d["away"]["team"].get("abbreviation"),
                "home_abbr": d["home"]["team"].get("abbreviation"),
                "as": int(d["away"]["score"]), "hs": int(d["home"]["score"]),
                "h1a": la[0] if la else None, "h1h": lh[0] if lh else None,
                "ot": max(len(la), len(lh)) > 2}
        except Exception:
            continue
    return out


# ---------------------------------------------------------------- state
def prune_and_spill(state, now):
    """Openers and depth for games tipped more than 2 days ago move to per-day files
    written once, so the live state stays small and git history does not balloon."""
    cut = (now - timedelta(days=2)).strftime("%Y-%m-%d")
    spill = {}
    for src in ("fd", "an"):
        keep = {}
        for k, v in state["openers"].get(src, {}).items():
            day = str(v.get("k") or "")[:10]
            if day and day < cut: spill.setdefault(day, {}).setdefault(src, {})[k] = v
            else: keep[k] = v
        state["openers"][src] = keep
    for day, blob in spill.items():
        path = P("openers", f"{day}.json")
        old = jload(path, {})
        for src, d in blob.items(): old.setdefault(src, {}).update(d)
        jsave(path, old)
    state["depth"] = {k: v for k, v in state["depth"].items() if str(v.get("k") or "9")[:10] >= cut}


def fresh(prev, now, minutes=25):
    try: return (now - parse_ts(prev)) <= timedelta(minutes=minutes)
    except Exception: return False


def commit():
    if OFFLINE: return
    try:
        subprocess.run(["git", "add", "-A", "cbb/"], check=False, cwd=ROOT)
        if subprocess.run(["git", "diff", "--staged", "--quiet"], cwd=ROOT).returncode != 0:
            subprocess.run(["git", "commit", "-q", "-m", f"cbb {now_utc().strftime('%FT%TZ')}"],
                           check=False, cwd=ROOT)
        for _ in range(3):                  # another job may push to the same repo
            subprocess.run(["git", "pull", "-q", "--rebase", "--autostash"], check=False, cwd=ROOT)
            if subprocess.run(["git", "push", "-q"], cwd=ROOT).returncode == 0: break
            time.sleep(7)
    except Exception as e:
        print("commit err", e)


# ---------------------------------------------------------------- main loop
def main():
    if not OFFLINE:
        for k, v in (("user.name", "propwatch"), ("user.email", "propwatch@users.noreply.github.com")):
            subprocess.run(["git", "config", k, v], check=False, cwd=ROOT)
    state = jload(P("state", "collector.json"), {})
    state.setdefault("openers", {"fd": {}, "an": {}})
    state.setdefault("depth", {})
    teams = jload(P("state", "teams.json"), {}); nteams = len(teams)

    cfg = discover(et_date(now_utc()))
    print("discovered:", json.dumps(jload(P("data", "_probe.json"), {}).get("chosen")), flush=True)

    D_lines = Delta("props", lambda r: (r["e"], r["mt"], r["mn"], r["r"]),
                    lambda r: (r["h"], r["o"], r["s"]))
    D_split = Delta("splits", lambda r: (r["gid"], r["b"], r["m"], r["sd"]),
                    lambda r: (r["v"], r["o"], r.get("tx"), r.get("mn"), r["ss"]))
    D_pin = Delta("pin", lambda r: (r["mid"], r["ty"], r["per"], r["side"], r["d"]),
                  lambda r: (r["pts"], r["pr"], r["lim"], r["st"]))

    t0 = time.time(); cyc = 0
    while time.time() - t0 < RUNFOR:
        cyc += 1; tc = time.time()
        now = now_utc(); ts = tsfmt(now); day = now.strftime("%Y-%m-%d")
        kf = (cyc % KF_N == 1); allbooks = (cyc % ALLBOOK_N == 1)
        raw = (state.get("raw_day") is None or state.get("force_raw")
               or (state.get("raw_day") != day and now.hour >= RAW_HOUR))
        if raw: state["raw_day"] = day; state["force_raw"] = False
        diag = {"run_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "cycle": cyc, "keyframe": kf,
                "raw": raw, "errors": [], "gz": {}, "rows_written": {}}

        def fetch(name, url, extra=None, keep_raw=False):
            try: txt = get(url, extra)
            except Exception as e:
                diag["errors"].append(f"{name}: {type(e).__name__}: {str(e)[:100]}"); return None
            if keep_raw and len(txt) > 500:
                diag["gz"][f"raw_{name}"] = write_gz(P("raw", name, day, f"{ts}.json.gz"), txt)
            return txt

        def put(D, rows):
            n, sz = D.write(rows, ts, day, kf)
            diag["rows_written"][D.name] = n; diag["gz"][D.name] = sz

        # ---- Action Network: today AND tomorrow every cycle (early lines move overnight)
        arows = []
        if cfg["an_ok"]:
            dates = [et_date(now), et_date(now, 1)]
            for i, d in enumerate(dates):
                txt = fetch(f"actionnet_d{i}", f"{AN}?period=game{cfg['an_div']}&date={d}", keep_raw=raw)
                if txt:
                    try: arows += an_rows(txt, ts, allbooks, teams)
                    except Exception as e: diag["errors"].append(f"an parse: {str(e)[:100]}")
        for r in arows:                      # book 30 = Action Network's opening line
            if r["b"] == OPENBOOK:
                o = state["openers"]["an"].setdefault(str(r["gid"]), {"g": r["g"], "k": r["st"]})
                o.setdefault("open", {}).setdefault(f"{r['m']}|{r['sd']}", [r["v"], r["o"]])
        if not allbooks:                     # every book hourly; ref + opener every cycle
            arows = [r for r in arows if r["b"] in (REFBOOK, OPENBOOK)]
        put(D_split, arows)
        caught = fresh(state.get("an_last_ok"), now)
        for r in arows:
            if r["b"] != REFBOOK or r.get("tx") is None: continue
            gid = str(r["gid"])
            o = state["openers"]["an"].setdefault(gid, {"g": r["g"], "k": r["st"]})
            if "first" not in o:
                o.update({"first": ts, "nb0": r["nb"], "caught": caught})
        if arows: state["an_last_ok"] = ts
        diag["an_rows"] = len(arows)

        # ---- FanDuel lobby: main lines for every listed game, every cycle
        lrows, evmeta, seen = [], {}, set()
        lob = fetch("fanduel", cfg["fd_lobby"], keep_raw=raw) if cfg["fd_lobby"] else None
        if lob:
            try:
                att = json.loads(lob).get("attachments", {})
                horizon = now + timedelta(hours=LINES_H)
                for k, v in (att.get("events") or {}).items():
                    nm, od = str(v.get("name", "")), str(v.get("openDate", ""))
                    if "@" not in nm or not od: continue
                    try: kt = datetime.fromisoformat(od.replace("Z", "+00:00"))
                    except Exception: continue
                    if kt <= horizon: evmeta[str(v.get("eventId") or k)] = (nm, od)
                lrows = fd_market_rows(att.get("markets") or {}, ts, evmeta, seen)
            except Exception as e:
                diag["errors"].append(f"lobby parse: {str(e)[:100]}")
        caught = fresh(state.get("fd_last_ok"), now)
        firsts = {}
        for r in lrows:
            if r["mt"] in MAIN_MT:
                firsts.setdefault(r["e"], {})[f"{r['mt']}|{r['r']}"] = [r["h"], r["o"]]
        new_caught = 0
        for eid, lines in firsts.items():
            if eid not in state["openers"]["fd"]:
                nm, od = evmeta[eid]
                state["openers"]["fd"][eid] = {"first": ts, "g": nm, "k": od, "lines": lines,
                                               "caught": caught}
                new_caught += caught
        if lrows: state["fd_last_ok"] = ts
        diag["lobby_events"] = len(evmeta); diag["new_openers_caught"] = new_caught

        # ---- FanDuel event pages, tiered by measured depth
        plan = []
        for eid, (nm, od) in evmeta.items():
            hrs = (datetime.fromisoformat(od.replace("Z", "+00:00")) - now).total_seconds() / 3600
            if not (0 < hrs <= DEEP_B_H): continue
            dp = state["depth"].get(eid)
            if dp is None:
                plan.append((0, hrs, eid, nm, od, None, "U"))          # depth unknown: look once
            elif dp["tabs"]:
                if hrs <= DEEP_A_H: plan.append((1, hrs, eid, nm, od, dp["tabs"], "A"))
                elif cyc % 3 == 1:  plan.append((2, hrs, eid, nm, od, dp["tabs"], "B"))
            elif cyc % 3 == 1:
                plan.append((3, hrs, eid, nm, od, HALF_TABS, "C"))
        plan.sort()
        prow, ok, fail, deferred = [], 0, 0, 0
        tiers = {"U": 0, "A": 0, "B": 0, "C": 0}
        for _, hrs, eid, nm, od, tabs, tier in plan:
            if ok + fail >= REQ_BUDGET or (time.time() - tc) > CYCLE * CYCLE_TIME_GUARD:
                deferred += 1; continue
            tiers[tier] += 1
            queries = [""] + [f"&tab={t}" for t in (tabs or [])]
            for q in queries:                       # list may grow on a first look
                if ok + fail >= REQ_BUDGET: break
                try:
                    j = json.loads(get(f"{FD}/event-page?eventId={eid}{q}&_ak={AK}")); ok += 1
                except Exception:
                    fail += 1
                    if q == "" and eid not in state["depth"]:
                        state["depth"][eid] = {"k": od, "tabs": [], "n_mk": 0, "last": ts, "fail": 1}
                    continue
                mk = (j.get("attachments") or {}).get("markets") or {}
                if q == "":
                    tabd = (j.get("layout") or {}).get("tabs") or {}
                    found = [slug(v.get("title", "")) for v in tabd.values()
                             if isinstance(v, dict) and PROP_TAB.search(v.get("title", ""))
                             and not SKIP_TAB.search(v.get("title", ""))]
                    state["depth"][eid] = {"k": od, "tabs": found, "n_mk": len(mk), "last": ts}
                    if tabs is None: queries += [f"&tab={t}" for t in found]
                prow += fd_market_rows(mk, ts, {eid: (nm, od)}, seen)
        put(D_lines, lrows + prow)
        diag.update({"lobby_rows": len(lrows), "event_rows": len(prow), "pulls_ok": ok,
                     "pulls_fail": fail, "deferred_events": deferred, "tiers": tiers,
                     "events_with_props": sum(1 for v in state["depth"].values() if v["tabs"])})

        # ---- Pinnacle: every cycle, compact + delta (the sharp reference and its limits)
        if cfg["pin_league"]:
            base = f"{PINB}/leagues/{cfg['pin_league']}"
            mt_ = fetch("pin_matchups", f"{base}/matchups", PIN, keep_raw=raw)
            pt_ = fetch("pin_prices", f"{base}/markets/straight", PIN, keep_raw=raw) if mt_ else None
            if mt_ and pt_:
                try:
                    pr = pin_rows(mt_, pt_, ts); put(D_pin, pr); diag["pin_rows"] = len(pr)
                except Exception as e: diag["errors"].append(f"pin parse: {str(e)[:100]}")

        # ---- finals (grader) and VSIN (second splits source, DraftKings handle)
        if cyc % ESPN_N == 1:
            for i in (0, -1):
                d = et_date(now, i)
                txt = fetch(f"espn_{d}", ESPN + d, keep_raw=raw)
                if txt:
                    try:
                        f = espn_finals(txt); path = P("finals", f"{d}.json")
                        old = jload(path, {})
                        if f and any(old.get(k) != v for k, v in f.items()):
                            old.update(f); jsave(path, old, pretty=True)
                    except Exception as e: diag["errors"].append(f"espn parse: {str(e)[:100]}")
        if raw and cfg["vsin"]: fetch("vsin", cfg["vsin"], keep_raw=True)

        if any("parse" in e for e in diag["errors"]): state["force_raw"] = True
        prune_and_spill(state, now)
        jsave(P("state", "collector.json"), state)
        if len(teams) != nteams: jsave(P("state", "teams.json"), teams, pretty=True); nteams = len(teams)
        diag["elapsed_min"] = round((time.time() - t0) / 60, 1)
        diag["cycle_sec"] = round(time.time() - tc, 1)
        diag["gz_kb_total"] = round(sum(diag["gz"].values()) / 1024, 1)
        jsave(P("data", "_diag.json"), diag, pretty=True)
        print(f"cyc {cyc:3} {ts} kf={int(kf)} an={len(arows)} lobby_ev={len(evmeta)} "
              f"lines={len(lrows)} props={len(prow)} pin={diag.get('pin_rows', 0)} ok={ok} "
              f"fail={fail} def={deferred} tiers={tiers} written={diag['rows_written']} "
              f"gz={diag['gz_kb_total']}KB {diag['cycle_sec']}s err={len(diag['errors'])}", flush=True)

        if cyc % PUSH_N == 0: commit()
        left = RUNFOR - (time.time() - t0)
        if left <= 0: break
        time.sleep(min(max(5, CYCLE - (time.time() - tc)), max(5, left)))

    commit()
    print("DONE cycles:", cyc)


if __name__ == "__main__":
    main()
