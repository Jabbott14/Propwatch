#!/usr/bin/env python3
"""Propwatch NCAAF collector. Long-running snapshot loop for a GitHub Actions runner.

Ported from cbb/collect.py 2026-11-21. Read claude/propwatch-ncaaf.md for why this
exists now, at the end of a season: ~120 capturable games (rivalry week, conference
championships, 46 bowls) and then nothing until late August 2027. The point of
building in November is a pipeline that has met real games before Week 0 of 2027.
Every collector in this project shipped with defects only live data exposed -- dark
windows, moneyline openers reading index 0, `gid` typed differently in two files,
late games filing under the next UTC date. Finding those on 120 throwaway games is
far cheaper than finding them next September.

What differs from the CBB collector, and why:

* FOOTBALL HAS QUARTERS. CBB's tab filter actively SKIPS anything matching "quarter"
  because college basketball has none. Here quarters are a wanted market, so the skip
  list drops that term and the tab matcher adds it. Getting this backwards would
  silently discard a whole market class -- the same shape as engine defect 6, where a
  `designation` filter matched nothing and prop prices looked uncollected all season.

* A WEEK OF LOOKAHEAD, NOT A DAY. CBB tips nightly, so the collector sweeps today and
  tomorrow. NCAAF is weekly: books post next Saturday's numbers days early, and the
  early number is the one worth having. Today and tomorrow are swept every cycle;
  the full 8-day horizon is swept on keyframe cycles (hourly).

* PHASE IS RECORDED ON EVERY GAME. regular / champ / bowl / cfp. Bowls are a
  different population from September football -- opt-outs, portal departures,
  interim coaches, 30+ day layoffs, and every one of them on a neutral floor. Pooling
  them is the same error as pooling markets, which this project has now made twice.

* EVERY BOWL IS A NEUTRAL SITE. The CBB matcher fix for neutral-site orientation
  (2026-11-19) is load-bearing here from day one, not an edge case: 46 of the ~120
  capturable games have no home team.

* FBS ONLY (ESPN groups=80), but FCS opponents appear in non-conference games and
  distort totals and blowout rates, so the opponent's group is recorded when ESPN
  gives it.

* ENDPOINTS ARE DISCOVERED, NOT ASSUMED. Same as CBB, and more so: the FanDuel page
  id, the Pinnacle football sport id and its NCAA league id are all unverified --
  sportsbook domains answer a proxy 403 from the analysis container, so none of this
  could be probed before shipping. Each job start tries the variants and writes what
  worked to ncaaf/data/_probe.json. READ THAT FILE AFTER THE FIRST RUN before
  trusting anything downstream.
"""
import gzip, json, os, re, subprocess, sys, time
from datetime import datetime, timezone, timedelta
from urllib.request import Request, urlopen

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
P = lambda *a: os.path.join(ROOT, "ncaaf", *a)

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36",
      "Accept": "application/json,text/html,*/*", "Accept-Language": "en-US,en;q=0.9"}
PIN = {"X-API-Key": "CmX2KcMrXuFmNg6YFbmTxE0y9CIrOi0R"}
AK = "FhMFpcPWXMeyZxOx"
FD = "https://sbapi.nj.sportsbook.fanduel.com/api"
AN = "https://api.actionnetwork.com/web/v2/scoreboard/ncaaf"
PINB = "https://guest.api.arcadia.pinnacle.com/0.1"
ESPN = ("https://site.api.espn.com/apis/site/v2/sports/football/"
        "college-football/scoreboard?groups=80&limit=500&dates=")
REFBOOK = "69"                     # FanDuel on Action Network (verified on NFL)
OPENBOOK = "30"                    # Action Network's opening line: never moves, no splits

CYCLE    = int(os.environ.get("CYCLE", 600))        # 10 min
RUNFOR   = int(os.environ.get("RUNFOR", 320 * 60))  # under the 6h job ceiling
KF_N     = 6       # keyframe every 6th cycle (hourly); deltas in between
ALLBOOK_N= 1       # every book every cycle -- costs nothing, the AN response already
                   # carries them all, and sampling parity is what makes the
                   # cross-book signals measurable at all (see cbb/collect.py)
ESPN_N   = 6
RAW_HOUR = 15
PUSH_N   = 3
REQ_BUDGET = 150
CYCLE_TIME_GUARD = 0.75
LINES_H  = 8 * 24  # lobby rows for games kicking within 8 days (lookahead lines)
DEEP_A_H = 12      # within 12h: all prop/period tabs every cycle
DEEP_B_H = 48      # within 48h: every 3rd cycle (football is weekly, CBB used 30h)
OFFLINE  = os.environ.get("PW_OFFLINE")

# Quarters are WANTED here. CBB's SKIP_TAB dropped them because college basketball has
# none; leaving that in would silently discard a market class.
PROP_TAB = re.compile(r"(half|quarter|team|player|passing|rushing|receiving|touchdown)", re.I)
SKIP_TAB = re.compile(r"(same game|parlay|popular|live)", re.I)
PERIOD_TABS = ["1st-half", "2nd-half", "1st-quarter"]
MAIN_MT = ("MATCH_HANDICAP_(2-WAY)", "TOTAL_POINTS_(OVER/UNDER)", "MONEY_LINE")

# Phase boundaries for the 2026-27 cycle. Regular season ends after rivalry week;
# conference championships are Dec 4-5; bowl season runs Dec 12 - Jan 25 (46 games,
# 35 bowls + 11 CFP). Dates are ET calendar days.
PHASE_BOUNDS = (("2026-11-30", "regular"), ("2026-12-08", "champ"),
                ("2026-12-28", "bowl"), ("2027-02-01", "cfp"))


def now_utc(): return datetime.now(timezone.utc)
def tsfmt(t): return t.strftime("%Y-%m-%dT%H%MZ")
def parse_ts(s): return datetime.strptime(s, "%Y-%m-%dT%H%MZ").replace(tzinfo=timezone.utc)
def et(t, add=0): return t - timedelta(hours=5) + timedelta(days=add)
def et_date(t, add=0): return et(t, add).strftime("%Y%m%d")
def slug(title): return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def phase_of(iso):
    """regular / champ / bowl / cfp from a kickoff timestamp. Never pool these."""
    try:
        d = datetime.fromisoformat(str(iso).replace("Z", "+00:00"))
    except Exception:
        return None
    day = (d - timedelta(hours=5)).strftime("%Y-%m-%d")
    for cut, name in PHASE_BOUNDS:
        if day < cut: return name
    return "cfp"


def kick_window(iso):
    """noon / afternoon / primetime -- different betting populations watch each."""
    try:
        h = (datetime.fromisoformat(str(iso).replace("Z", "+00:00")) - timedelta(hours=5)).hour
    except Exception:
        return None
    return "early" if h < 15 else ("afternoon" if h < 18 else "primetime")


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
            k0 = self.key(r)
            occ[k0] = occ.get(k0, -1) + 1
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
                                 "REGULAR_SEASON", "CHAMPION", "CONFERENCE_WINNER",
                                 "HEISMAN", "TO_MAKE_PLAYOFF", "WIN_TOTAL",
                                 "EXACT", "ODD/EVEN", "3-WAY", "HIGHEST_SCORING",
                                 "MARGIN", "RACE_TO", "FIRST_TO", "WINNING_MARGIN"))


def od_of(r):
    try: return r["winRunnerOdds"]["americanDisplayOdds"]["americanOdds"]
    except Exception: return None


# ---------------------------------------------------------------- discovery
def discover(day_et):
    """Try endpoint variants; keep whichever returns the most usable data.

    Nothing here was verifiable before shipping -- every sportsbook host answers a
    proxy 403 from the analysis container -- so the FanDuel page id, the Pinnacle
    football sport id and its NCAA league are all found at runtime and written to
    ncaaf/data/_probe.json. Read it after the first run."""
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

    def best(results):
        i = max(range(len(results)), key=lambda k: (results[k][0], -k))
        return results[i]

    def fd_score(t):
        ev = json.loads(t).get("attachments", {}).get("events", {})
        return sum(1 for v in ev.values() if "@" in str(v.get("name", "")))

    def an_score(t):
        return sum(1 for g in json.loads(t).get("games", []) if g.get("markets"))

    fd = best([attempt("fd_lobby", f"{FD}/content-managed-page?page=CUSTOM&customPageId={pid}&_ak={AK}",
                       score=fd_score)
               for pid in ("ncaaf", "college-football", "ncaa-football", "cfb")])
    # Plain ?period=game returns the current week on the NFL board; the dated form is
    # what CBB needs. Score both and keep whichever actually carries markets.
    an = best([attempt("actionnet", u, score=an_score) for u in (
        f"{AN}?period=game",
        f"{AN}?period=game&date={day_et}",
        f"{AN}?period=game&division=FBS&date={day_et}")])

    # Pinnacle: find the football sport, then its NCAA league. CBB hardcoded sport 4
    # with a 493 fallback; here the sport id itself is unknown, so enumerate.
    pin_league, pin_name, pin_sport = None, None, None
    try:
        sports = json.loads(get(f"{PINB}/sports", PIN))
        fb = [s for s in sports if "FOOTBALL" in str(s.get("name", "")).upper()
              and "AUSTRALIAN" not in str(s.get("name", "")).upper()]
        probe["pin_sports"] = [{"id": s.get("id"), "name": s.get("name")} for s in fb[:8]]
        for s in fb:
            try:
                lg = json.loads(get(f"{PINB}/sports/{s['id']}/leagues?all=false", PIN))
            except Exception:
                continue
            cands = [l for l in lg
                     if any(w in str(l.get("name", "")).upper() for w in ("NCAA", "COLLEGE"))
                     and "WOMEN" not in str(l.get("name", "")).upper()]
            cands.sort(key=lambda l: -(l.get("matchupCount") or 0))
            if cands:
                pin_sport, pin_league, pin_name = s["id"], cands[0]["id"], cands[0].get("name")
                probe["pin_leagues"] = [{"id": l.get("id"), "name": l.get("name"),
                                         "n": l.get("matchupCount")} for l in cands[:6]]
                break
    except Exception as e:
        probe["pin_leagues_error"] = f"{type(e).__name__}: {str(e)[:120]}"

    vs = best([attempt("vsin", f"https://data.vsin.com/betting-splits/?sport={s}")
               for s in ("NCAAF", "CFB", "college-football")])

    an_q = an[1].split("?", 1)[1] if "?" in an[1] else "period=game"
    cfg = {"fd_lobby": fd[1] if fd[0] > 0 else None,
           "an_dated": "date=" in an_q, "an_div": "&division=FBS" if "division=FBS" in an_q else "",
           "an_ok": an[0] > 0,
           "pin_sport": pin_sport, "pin_league": pin_league, "pin_name": pin_name,
           "vsin": vs[1] if vs[0] > 0 else None}
    probe["chosen"] = {k: (v.replace(AK, "<ak>") if isinstance(v, str) else v) for k, v in cfg.items()}
    jsave(P("data", "_probe.json"), probe, pretty=True)
    return cfg


# ---------------------------------------------------------------- extraction
def an_rows(txt, ts, allbooks, teams):
    """Splits are consensus (identical across book rows, verified on NFL), so only the
    ref book carries tix/mny. Other books carry line and juice only."""
    out = []
    for g in json.loads(txt).get("games", []):
        tm = {t["id"]: t for t in g.get("teams", [])}
        for tid, t in tm.items():
            if str(tid) not in teams:
                teams[str(tid)] = {"abbr": t.get("abbr"), "name": t.get("full_name"),
                                   "conf": t.get("conference_type"), "div": t.get("division_type")}
        a, h = tm.get(g.get("away_team_id"), {}), tm.get(g.get("home_team_id"), {})
        if not a or not h: continue
        st = g.get("start_time")
        base = {"t": ts, "gid": g.get("id"), "g": f"{a.get('abbr')}@{h.get('abbr')}",
                "st": st, "ss": g.get("status"), "nb": g.get("num_bets"),
                "ac": a.get("conference_type"), "hc": h.get("conference_type"),
                "ad": a.get("division_type"), "hd": h.get("division_type"),
                "ph": phase_of(st), "kw": kick_window(st), "neu": g.get("neutral_site"),
                "rot": [g.get("away_rotation_number"), g.get("home_rotation_number")],
                "tv": (g.get("broadcast") or {}).get("network"),
                "trend": g.get("trending"), "gtype": g.get("type")}
        for bid, blk in (g.get("markets") or {}).items():
            if bid not in (REFBOOK, OPENBOOK) and not allbooks: continue
            ev = (blk or {}).get("event") or {}
            for mkt in ("spread", "total", "moneyline"):
                for o in ev.get(mkt, []) or []:
                    r = dict(base); r.update({"b": bid, "m": mkt, "sd": o.get("side"),
                                              "tid": o.get("team_id"), "v": o.get("value"),
                                              "o": o.get("odds"),
                                              # is_live and is_alt_market are how AN labels
                                              # the live in-game quote and alternate lines.
                                              # Dropping them let both leak into the main
                                              # series: measured 2026-11-21, the graded
                                              # CLOSE landed on the wrong quote in ~10% of
                                              # CBB markets, median 5 points out. The
                                              # grader had to guess with a heuristic at
                                              # what these two booleans state outright.
                                              "lv": o.get("is_live"),
                                              "alt": o.get("is_alt_market"),
                                              "per": o.get("period"),
                                              "ls": o.get("line_status")})
                    if bid == REFBOOK:
                        bi = o.get("bet_info") or {}
                        r["tx"] = (bi.get("tickets") or {}).get("percent")
                        r["mn"] = (bi.get("money") or {}).get("percent")
                        # raw counts, not just shares -- a 60% money share on 200 bets
                        # and on 20,000 bets are not the same event
                        r["txv"] = (bi.get("tickets") or {}).get("value")
                        r["mnv"] = (bi.get("money") or {}).get("value")
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
    """Football linescores are four quarters (plus OT), not two halves. Halves are
    derived so the period grader can read them without re-deriving."""
    out = {}
    for e in json.loads(txt).get("events", []):
        try:
            c = e["competitions"][0]
            if not c["status"]["type"].get("completed"): continue
            d = {t["homeAway"]: t for t in c["competitors"]}
            ls = lambda t: [int(float(q.get("value", 0))) for q in (t.get("linescores") or [])]
            la, lh = ls(d["away"]), ls(d["home"])
            half = lambda l: (sum(l[:2]) if len(l) >= 2 else None,
                              sum(l[2:4]) if len(l) >= 4 else None)
            h1a, h2a = half(la); h1h, h2h = half(lh)
            grp = lambda t: ((t["team"].get("groups") or {}) or {}).get("parent", {}).get("id") \
                if isinstance(t["team"].get("groups"), dict) else None
            out[str(e["id"])] = {
                "date": e.get("date"), "neutral": c.get("neutralSite"),
                "phase": phase_of(e.get("date")),
                "away": d["away"]["team"].get("displayName"), "home": d["home"]["team"].get("displayName"),
                "away_abbr": d["away"]["team"].get("abbreviation"),
                "home_abbr": d["home"]["team"].get("abbreviation"),
                "as": int(d["away"]["score"]), "hs": int(d["home"]["score"]),
                "qa": la, "qh": lh, "h1a": h1a, "h1h": h1h, "h2a": h2a, "h2h": h2h,
                "ot": max(len(la), len(lh)) > 4,
                "away_grp": grp(d["away"]), "home_grp": grp(d["home"])}
        except Exception:
            continue
    return out


# ---------------------------------------------------------------- state
def prune_and_spill(state, now):
    cut = (now - timedelta(days=3)).strftime("%Y-%m-%d")
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
        subprocess.run(["git", "add", "-A", "ncaaf/"], check=False, cwd=ROOT)
        if subprocess.run(["git", "diff", "--staged", "--quiet"], cwd=ROOT).returncode != 0:
            subprocess.run(["git", "commit", "-q", "-m", f"ncaaf {now_utc().strftime('%FT%TZ')}"],
                           check=False, cwd=ROOT)
        for _ in range(3):
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
        kf = (cyc % KF_N == 1)
        allbooks = (ALLBOOK_N <= 1) or (cyc % ALLBOOK_N == 1)
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

        # ---- Action Network. Today+tomorrow every cycle; the full 8-day lookahead
        #      hourly, because next Saturday's number is posted days early and the
        #      early number is the one worth having.
        arows = []
        if cfg["an_ok"]:
            if not cfg["an_dated"]:
                urls = [("wk", f"{AN}?period=game{cfg['an_div']}")]
            else:
                span = range(0, 8) if kf else range(0, 2)
                urls = [(f"d{i}", f"{AN}?period=game{cfg['an_div']}&date={et_date(now, i)}")
                        for i in span]
            for tag, u in urls:
                txt = fetch(f"actionnet_{tag}", u, keep_raw=(raw and tag in ("wk", "d0")))
                if txt:
                    try: arows += an_rows(txt, ts, allbooks, teams)
                    except Exception as e: diag["errors"].append(f"an parse: {str(e)[:100]}")
        for r in arows:
            if r["b"] == OPENBOOK:
                o = state["openers"]["an"].setdefault(str(r["gid"]),
                                                      {"g": r["g"], "k": r["st"], "ph": r.get("ph")})
                o.setdefault("open", {}).setdefault(f"{r['m']}|{r['sd']}", [r["v"], r["o"]])
        if not allbooks:
            arows = [r for r in arows if r["b"] in (REFBOOK, OPENBOOK)]
        put(D_split, arows)
        caught = fresh(state.get("an_last_ok"), now)
        for r in arows:
            if r["b"] != REFBOOK or r.get("tx") is None: continue
            gid = str(r["gid"])
            o = state["openers"]["an"].setdefault(gid, {"g": r["g"], "k": r["st"], "ph": r.get("ph")})
            if "first" not in o:
                o.update({"first": ts, "nb0": r["nb"], "caught": caught})
        if arows: state["an_last_ok"] = ts
        diag["an_rows"] = len(arows)
        diag["an_phases"] = {p: sum(1 for r in arows if r.get("ph") == p)
                             for p in ("regular", "champ", "bowl", "cfp")}

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
                                               "caught": caught, "ph": phase_of(od)}
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
                plan.append((0, hrs, eid, nm, od, None, "U"))
            elif dp["tabs"]:
                if hrs <= DEEP_A_H: plan.append((1, hrs, eid, nm, od, dp["tabs"], "A"))
                elif cyc % 3 == 1:  plan.append((2, hrs, eid, nm, od, dp["tabs"], "B"))
            elif cyc % 3 == 1:
                plan.append((3, hrs, eid, nm, od, PERIOD_TABS, "C"))
        plan.sort()
        prow, ok, fail, deferred = [], 0, 0, 0
        tiers = {"U": 0, "A": 0, "B": 0, "C": 0}
        for _, hrs, eid, nm, od, tabs, tier in plan:
            if ok + fail >= REQ_BUDGET or (time.time() - tc) > CYCLE * CYCLE_TIME_GUARD:
                deferred += 1; continue
            tiers[tier] += 1
            queries = [""] + [f"&tab={t}" for t in (tabs or [])]
            for q in queries:
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
                     "events_with_tabs": sum(1 for v in state["depth"].values() if v["tabs"])})

        # ---- Pinnacle: the sharp reference and its limits
        if cfg["pin_league"]:
            base = f"{PINB}/leagues/{cfg['pin_league']}"
            mt_ = fetch("pin_matchups", f"{base}/matchups", PIN, keep_raw=raw)
            pt_ = fetch("pin_prices", f"{base}/markets/straight", PIN, keep_raw=raw) if mt_ else None
            if mt_ and pt_:
                try:
                    pr = pin_rows(mt_, pt_, ts); put(D_pin, pr); diag["pin_rows"] = len(pr)
                except Exception as e: diag["errors"].append(f"pin parse: {str(e)[:100]}")

        # ---- finals and VSiN
        if cyc % ESPN_N == 1:
            for i in (0, -1, -2):       # Saturday games settle late; look back two days
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
        print(f"cyc {cyc:3} {ts} kf={int(kf)} an={len(arows)} ph={diag['an_phases']} "
              f"lobby_ev={len(evmeta)} lines={len(lrows)} periods={len(prow)} "
              f"pin={diag.get('pin_rows', 0)} ok={ok} fail={fail} def={deferred} "
              f"written={diag['rows_written']} gz={diag['gz_kb_total']}KB "
              f"{diag['cycle_sec']}s err={len(diag['errors'])}", flush=True)

        if cyc % PUSH_N == 0: commit()
        left = RUNFOR - (time.time() - t0)
        if left <= 0: break
        time.sleep(min(max(5, CYCLE - (time.time() - tc)), max(5, left)))

    commit()
    print("DONE cycles:", cyc)


if __name__ == "__main__":
    main()

