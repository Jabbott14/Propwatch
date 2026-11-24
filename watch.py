#!/usr/bin/env python3
"""watch.py -- find the setups while they are still live, not after.

The engine's primary input is MOVEMENT, and movement is a thing that happens between
two moments. Every read this project produced by hand has been built from whatever
snapshot happened to be sitting there when someone asked, which is how a Pinnacle total
that had bottomed at 131 and climbed for four hours got quoted as "136.5 -> 132", and
how a board scalar one move stale got quoted on 2026-11-22 after Pinnacle had already
moved again.

So this reads the SERIES, never a scalar, and prints three things:

  LOADED      heavy one-way public money with the number still sitting on its opener.
              Nothing has happened yet -- this is where to look, not what to bet. On
              2026-11-24 the whole Week 12 board was in this state: 52 of 52 markets
              unmoved with 92-93% of money stacked on one side of two of them.
  BROKEN      a LOADED market where the number has since moved AGAINST the public.
              This is the setup, and it is only visible if you knew the prior state.
  FOLLOWED    a LOADED market where the number moved WITH the public. Not a fade. Worth
              printing because the project keeps mistaking these for fades after the
              fact -- Tampa on 2026-11-22 had 81% against it, three points of Pinnacle
              movement and a $100k limit, and lost by ten.

Two rules this file enforces mechanically, because prose has not held:

  * Pinnacle main lines only, `isAlternate: false`. Alternates carry the SAME limit as
    the main line, so "take the row with the biggest limit" silently returns a 44.5
    total at +220 on a game whose real number is 37.5.
  * Pinnacle sides matched by TEAM, never by home/away label. Pinnacle lists some games
    in the opposite orientation to Action Network (NYG @ JAC where AN has JAC @ NYG), so
    a lookup keyed on the label reads the wrong side without erroring.

Prints to stdout and writes WATCH.md. Exits 0 always -- a prompt, not a gate.
"""
import gzip, json, glob, os, sys, collections, datetime as dt

ROOT = os.path.dirname(os.path.abspath(__file__))
PUBLIC_TIX = 65        # tickets % that counts as one-way
PUBLIC_MNY = 65
MOVE_EPS   = 1e-9

L = []
def say(s=""):
    L.append(s); print(s, flush=True)


def newest(pattern, n=1):
    fs = sorted(glob.glob(os.path.join(ROOT, pattern)))
    return fs[-n:] if fs else []


def load_gz(p):
    try:
        return json.load(gzip.open(p, "rt"))
    except Exception:
        return None


def pin_now():
    """Current Pinnacle main lines, keyed by (teams, market, team-or-side)."""
    mf = newest("raw/pin_matchups/*/*.json.gz")
    pf = newest("raw/pin_prices/*/*.json.gz")
    if not mf or not pf:
        return {}, None
    mm = {}
    for m in (load_gz(mf[0]) or []):
        if m.get("parentId") is not None:
            continue
        p = m.get("participants") or []
        if len(p) != 2:
            continue
        d = {x.get("alignment"): x.get("name") for x in p}
        if len(d) == 2:
            mm[m["id"]] = {"away": d.get("away"), "home": d.get("home"), "st": m.get("startTime")}
    out = {}
    for r in (load_gz(pf[0]) or []):
        mid = r.get("matchupId")
        if mid not in mm or r.get("isAlternate") or r.get("period") != 0:
            continue
        if r.get("type") not in ("total", "spread"):
            continue
        g = mm[mid]
        lim = max([x.get("amount", 0) for x in (r.get("limits") or [])], default=0)
        for p in (r.get("prices") or []):
            des = p.get("designation")
            # total -> over/under; side markets -> the TEAM NAME, never the label
            k2 = des if r["type"] == "total" else g.get(des)
            if k2 is None:
                continue
            out[(g["away"], g["home"], r["type"], k2)] = {
                "pts": p.get("points"), "pr": p.get("price"), "lim": lim, "st": g["st"]}
    return out, os.path.basename(pf[0]).replace(".json.gz", "")


def fd_series(days=3):
    """FanDuel across every snapshot we hold: opener, current, and the splits.

    The live set comes from the NEWEST snapshot only, then history is filled in from
    older ones. Reading the union of three days instead put eight finished Week 11 games
    in the first run of this file -- they were `scheduled` in Sunday morning's snapshots
    and the status filter was reading those old copies, so TB@DET showed up as a live
    setup two days after Detroit won it.
    """
    fs = []
    for d in sorted(glob.glob(os.path.join(ROOT, "raw/actionnet/*")))[-days:]:
        fs += sorted(glob.glob(os.path.join(d, "*.json.gz")))
    if not fs:
        return {}, {}
    now = dt.datetime.now(dt.timezone.utc)
    live = set()
    j = load_gz(fs[-1]) or {}
    tmn = {}
    for g in j.get("games", []):
        for t in (g.get("teams") or []):
            tmn[t.get("id")] = t.get("abbr")
    for g in j.get("games", []):
        st = g.get("start_time") or ""
        if (g.get("status") or "") == "complete":
            continue
        try:
            if dt.datetime.fromisoformat(st.replace("Z", "+00:00")) <= now:
                continue            # kicked off already
        except Exception:
            continue
        a, h = tmn.get(g.get("away_team_id")), tmn.get(g.get("home_team_id"))
        if a and h:
            live.add((a, h))
    hist = collections.defaultdict(dict)
    names = {}
    for f in fs:
        ts = os.path.basename(f).replace(".json.gz", "")
        j = load_gz(f)
        if not j:
            continue
        tm = {}
        for g in j.get("games", []):
            for t in (g.get("teams") or []):
                tm[t.get("id")] = t.get("abbr")
                if t.get("full_name"): names[t.get("abbr")] = t["full_name"]
                elif t.get("display_name"): names[t.get("abbr")] = t["display_name"]
        for g in j.get("games", []):
            a, h = tm.get(g.get("away_team_id")), tm.get(g.get("home_team_id"))
            if (a, h) not in live:
                continue
            fd = (g.get("markets") or {}).get("69", {}).get("event", {})
            bi = lambda x, k: (x.get("bet_info", {}).get(k, {}) or {}).get("percent")
            for mk in ("spread", "total"):
                for x in (fd.get(mk) or []):
                    if x.get("value") is None:
                        continue
                    sd = x.get("side")
                    k2 = sd if mk == "total" else (h if sd == "home" else a)
                    hist[(a, h, mk, k2)][ts] = {
                        "v": x["value"], "odds": x.get("odds"), "tix": bi(x, "tickets"),
                        "mny": bi(x, "money"), "nb": g.get("num_bets"), "st": g.get("start_time")}
    return hist, names


def main():
    now = dt.datetime.now(dt.timezone.utc)
    say("=" * 84)
    say(f"PROPWATCH WATCH   {now.strftime('%Y-%m-%dT%H:%MZ')}")
    say("=" * 84)
    say()

    pin, pints = pin_now()
    hist, names = fd_series()
    if not hist:
        say("  no Action Network snapshots. Collector may be down -- check audit.py section 0.")
        return 0
    rev = {v: k for k, v in names.items()}

    loaded, broken, followed = [], [], []
    for (a, h, mk, k2), series in hist.items():
        tss = sorted(series)
        if len(tss) < 2:
            continue
        first, cur = series[tss[0]], series[tss[-1]]
        if cur["tix"] is None:
            continue
        # Pinnacle: side markets are keyed by FULL team name on Pinnacle's side
        pk = None
        if mk == "total":
            cand = [k for k in pin if k[2] == "total" and k[3] == k2
                    and {names.get(a, a), names.get(h, h)} == {k[0], k[1]}]
        else:
            cand = [k for k in pin if k[2] == "spread" and k[3] == names.get(k2, k2)
                    and {names.get(a, a), names.get(h, h)} == {k[0], k[1]}]
        p = pin.get(cand[0]) if cand else None

        mv = round(cur["v"] - first["v"], 2)
        public_here = cur["tix"] >= PUBLIC_TIX and (cur["mny"] or 0) >= PUBLIC_MNY
        if not public_here:
            continue
        # did the number move toward this (public) side?
        if mk == "total":
            toward = (mv > 0) if k2 == "over" else (mv < 0)
        else:
            toward = mv < 0          # this side's own handicap shrinking = market likes it
        rec = {"g": f"{a}@{h}", "mk": mk, "side": k2, "open": first["v"], "now": cur["v"],
               "mv": mv, "odds": cur["odds"], "tix": cur["tix"], "mny": cur["mny"],
               "nb": cur["nb"], "st": cur["st"], "snaps": len(tss),
               "pin": (p or {}).get("pts"), "lim": (p or {}).get("lim")}
        if abs(mv) < MOVE_EPS:
            loaded.append(rec)
        elif toward:
            followed.append(rec)
        else:
            broken.append(rec)

    def show(rows, title, note):
        say(f"## {title}  ({len(rows)})")
        say(f"   {note}")
        say()
        if not rows:
            say("   none"); say(); return
        for r in sorted(rows, key=lambda x: -(x["tix"] or 0)):
            pin_s = f"Pin {r['pin']:g}" + (f" ${r['lim']:,}" if r['lim'] else "") if r['pin'] is not None else "Pin ?"
            say(f"   {r['g']:10} {r['mk']:7} {str(r['side'])[:5]:5}  "
                f"public {r['tix']:>3}%/{r['mny']:>3}%  "
                f"open {r['open']:>6g} -> {r['now']:>6g} ({r['mv']:+g})  "
                f"{pin_s:>18}  {r['nb'] or 0:>7,} bets  {r['st'][:16].replace('T',' ')}Z")
        say()

    show(broken, "BROKEN — the number moved AGAINST heavy public money",
         "the setup. Only visible because the prior state was recorded.")
    show(loaded, "LOADED — one-way money, number still on its opener",
         "nothing has happened yet. Where to look, not what to bet.")
    show(followed, "FOLLOWED — the number moved WITH the public",
         "not a fade. Printed because these get mistaken for fades afterwards.")

    say("-" * 84)
    say("Public = >=65% of BOTH tickets and money. Pinnacle read from the current")
    say("snapshot, main lines only (isAlternate false), sides matched by team not by")
    say("home/away label. Movement measured from the earliest snapshot held, so a number")
    say("that opened before our first snapshot shows less movement than it really had.")
    say("-" * 84)

    with open(os.path.join(ROOT, "WATCH.md"), "w") as f:
        f.write("# Propwatch watch\n\nGenerated " + now.strftime("%Y-%m-%dT%H:%MZ") +
                " by `watch.py`.\n\n```\n" + "\n".join(L) + "\n```\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
