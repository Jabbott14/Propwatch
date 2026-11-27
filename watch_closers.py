#!/usr/bin/env python3
"""Capture CLOSING lines for NFL games that have kicked off -- defect 19.

The watch has declined thirteen boards and never stored a closer, so none of its
declines were ever measurable. This writes `watch_closers.json`, one record per
(game, market), built from the LAST committed snapshot before `start_time`:
Pinnacle's main close with its limit, every book's close, the public split at the
close, and the final score once the game completes.

Primary source only (rule 1): raw JSON named fields, never a stored series tuple --
the NFL/CBB pin row field order is swapped between graders and index 4 has been read
as a limit before. Alternates and non-period-0 rows are excluded, sides are matched
by TEAM name, never by the home/away label.

Idempotent: re-running updates records in place (a result can arrive after the
close), so it is safe to call every watch run.
"""
import gzip, json, glob, os, datetime as dt

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "watch_closers.json")


def lg(p):
    try:
        return json.load(gzip.open(p, "rt"))
    except Exception:
        return None


def snaps(kind):
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, f"raw/{kind}/*/*.json.gz"))):
        b = os.path.basename(f).replace(".json.gz", "")
        try:
            t = dt.datetime.strptime(b, "%Y-%m-%dT%H%MZ").replace(tzinfo=dt.timezone.utc)
        except Exception:
            continue
        out.append((t, f))
    return out


def pin_board(price_path, matchup_paths):
    """Pinnacle period-0 MAIN lines from one snapshot -> {(away,home,type,side): rec}."""
    mf = None
    for f in matchup_paths:
        if os.path.basename(f) <= os.path.basename(price_path):
            mf = f
    if mf is None and matchup_paths:
        mf = matchup_paths[0]
    mm = {}
    for m in (lg(mf) or []):
        if m.get("parentId") is not None:
            continue
        p = m.get("participants") or []
        if len(p) != 2:
            continue
        d = {x.get("alignment"): x.get("name") for x in p}
        if len(d) == 2:
            mm[m["id"]] = {"away": d.get("away"), "home": d.get("home"), "st": m.get("startTime")}
    out = {}
    for r in (lg(price_path) or []):
        mid = r.get("matchupId")
        if mid not in mm or r.get("isAlternate") or r.get("period") != 0:
            continue
        if r.get("type") not in ("total", "spread"):
            continue
        g = mm[mid]
        lim = max([x.get("amount", 0) for x in (r.get("limits") or [])], default=0)
        for p in (r.get("prices") or []):
            des = p.get("designation")
            k2 = des if r["type"] == "total" else g.get(des)
            if k2 is None:
                continue
            out[(g["away"], g["home"], r["type"], k2)] = {
                "pts": p.get("points"), "price": p.get("price"), "limit": lim, "start": g["st"]}
    return out


def main():
    pins, ans = snaps("pin_prices"), snaps("actionnet")
    mps = sorted(glob.glob(os.path.join(ROOT, "raw/pin_matchups/*/*.json.gz")))
    if not pins or not ans:
        print("no snapshots; nothing to do")
        return
    now = dt.datetime.now(dt.timezone.utc)

    # every game we hold, from the newest Action Network snapshot
    newest = lg(ans[-1][1]) or {}
    games = {}
    for g in newest.get("games", []):
        ts = [t.get("abbr") for t in (g.get("teams") or [])]
        st = g.get("start_time")
        if len(ts) != 2 or not st:
            continue
        k = dt.datetime.fromisoformat(st.replace("Z", "+00:00"))
        if k >= now:
            continue  # not kicked off
        ids = {t.get("id"): t.get("abbr") for t in (g.get("teams") or [])}
        away = ids.get(g.get("away_team_id")) or ts[0]
        home = ids.get(g.get("home_team_id")) or ts[1]
        games[f"{away}@{home}"] = {"ko": k, "abbrs": set(ts), "g": g}

    recs = {}
    if os.path.exists(OUT):
        for r in json.load(open(OUT)):
            recs[r["key"]] = r

    wrote = 0
    for label, info in sorted(games.items()):
        k, abbrs = info["ko"], info["abbrs"]
        lp = [f for t, f in pins if t <= k]
        la = [f for t, f in ans if t <= k]
        if not lp or not la:
            continue
        pin = pin_board(lp[-1], mps)
        A = lg(la[-1]) or {}
        ag = None
        for g in A.get("games", []):
            if {t.get("abbr") for t in (g.get("teams") or [])} == abbrs:
                ag = g
                break
        if ag is None:
            continue

        # final score, from the newest snapshot (result can post long after close)
        gg = info["g"]
        bs = gg.get("boxscore") or {}
        ids = {t.get("id"): t.get("abbr") for t in (gg.get("teams") or [])}
        aw, hm = ids.get(gg.get("away_team_id")), ids.get(gg.get("home_team_id"))
        ap, hp = bs.get("total_away_points"), bs.get("total_home_points")
        complete = gg.get("status") == "complete"
        total_pts = (ap + hp) if (complete and ap is not None and hp is not None) else None

        # Select this game's Pinnacle rows BY TEAM NAME, never by start time.
        #
        # This join was an exact start-time equality until 2026-11-27 and it was wrong
        # twice over. (a) The two feeds disagree on kickoff: Action Network had KC@BUF at
        # 01:20Z and Pinnacle at 01:15:00Z, so the match returned nothing and the record
        # stored `pinnacle_close: {}`, which prints as "pin total None" and reads as
        # "Pinnacle had no close" rather than as a failed filter -- engine defect 4's rule
        # that an empty filter is evidence about the filter first. (b) Worse, start time
        # does not identify a game at all: nine games kick off at 18:00Z every Sunday, so
        # every one of them wrote to the same `total|over` key and the last one won. The
        # three Thanksgiving records survived only because each had a unique kickoff.
        #
        # Action Network's `full_name` and Pinnacle's participant names agree exactly
        # ("Kansas City Chiefs", "Buffalo Bills"), so the pair of names is the key. Matched
        # as an unordered pair, because Pinnacle lists some games in the opposite
        # orientation to Action Network.
        names = {t.get("full_name") for t in (gg.get("teams") or []) if t.get("full_name")}
        mine = {}
        if len(names) == 2:
            for kk, v in pin.items():
                if {kk[0], kk[1]} == names:
                    mine[f"{kk[2]}|{kk[3]}"] = {"pts": v["pts"], "price": v["price"],
                                                "limit": v["limit"]}
        if not mine:
            print(f"  WARN {label}: no Pinnacle main rows matched {sorted(names)} "
                  f"in {os.path.basename(lp[-1])} -- filter, not a quiet market")

        books = {}
        for bid, bm in (ag.get("markets") or {}).items():
            ev = (bm or {}).get("event") or {}
            for mk in ("total", "spread"):
                for o in (ev.get(mk) or []):
                    if o.get("period") != "event" or o.get("is_live"):
                        continue
                    bi = o.get("bet_info") or {}
                    books.setdefault(bid, {})[f"{mk}|{o.get('side')}"] = {
                        "value": o.get("value"), "odds": o.get("odds"),
                        "tickets_pct": ((bi.get("tickets") or {}).get("percent")),
                        "money_pct": ((bi.get("money") or {}).get("percent"))}

        rec = {
            "key": f"{label}|{k:%Y-%m-%dT%H%MZ}",
            "game": label, "kickoff": f"{k:%Y-%m-%dT%H%MZ}",
            "close_snap": os.path.basename(lp[-1]).replace(".json.gz", ""),
            "pinnacle_close": mine,
            "book_closes": books,
            "num_bets_at_close": ag.get("num_bets"),
            "status": gg.get("status"),
            "final": ({"away": aw, "away_pts": ap, "home": hm, "home_pts": hp,
                       "total": total_pts} if complete else None),
            "captured_at": f"{now:%Y-%m-%dT%H%MZ}",
        }
        prev = recs.get(rec["key"])
        if prev != rec:
            recs[rec["key"]] = rec
            wrote += 1

    allr = sorted(recs.values(), key=lambda r: r["kickoff"])
    json.dump(allr, open(OUT, "w"), indent=1, sort_keys=True)
    print(f"watch_closers.json: {len(allr)} records, {wrote} written/updated this run")
    for r in allr[-6:]:
        f = r["final"]
        res = (f"FINAL {f['away']} {f['away_pts']} - {f['home']} {f['home_pts']}"
               f"  total {f['total']}") if f else f"({r['status']})"
        pt = r["pinnacle_close"].get("total|over", {})
        print(f"  {r['game']:9} {r['kickoff']}  pin total {pt.get('pts')} "
              f"@ {pt.get('price')} lim ${pt.get('limit') or 0:,}  {res}")


if __name__ == "__main__":
    main()
