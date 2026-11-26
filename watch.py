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
PP_PER_PT  = 2.75      # probability points per point of NFL spread/total
MIN_PP     = 1.0       # a move must be worth at least this much to count

# A LINE MOVE WITH A PRICE MOVE AGAINST IT IS NOT A MOVE.
# First run, 2026-11-24: NO@CIN showed FanDuel -10.5 -> -9.5 with 89% of tickets and 86%
# of money on Cincinnati, and the detector called it the strongest setup on the board.
# Verification killed it. The price went -100 -> -120 at the same instant, and all six
# other books sat at -10. Half a point of spread is worth ~1.4 probability points; 20
# cents of juice is worth ~4.5. The "move" was the same number repackaged, and what
# little it was worth ran AGAINST the bettor.
#
# So movement is measured in probability points with the price included, never in line
# points alone. The other books' consensus prints alongside, because a book that is
# alone at its number is an outlier, not a market -- and xbook.py has already measured
# that FanDuel is the one that lags (z = -3.49 over 1110 multi-book move events).


def _imp(odds):
    o = float(odds)
    return 100.0 / (o + 100.0) if o > 0 else (-o) / ((-o) + 100.0)


def eff_move(mk, side, o_v, o_odds, n_v, n_odds):
    """Movement toward this side, in probability points, line and price together."""
    if mk == "total":
        line_pp = ((n_v - o_v) if side == "over" else (o_v - n_v)) * PP_PER_PT
    else:
        line_pp = (o_v - n_v) * PP_PER_PT      # this side's own handicap shrinking
    price_pp = 0.0
    try:
        if o_odds is not None and n_odds is not None:
            # a shorter price means the market likes this side more
            price_pp = (_imp(n_odds) - _imp(o_odds)) * 100.0
    except Exception:
        pass
    return round(line_pp + price_pp, 2), round(line_pp, 2), round(price_pp, 2)

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
    books_now = {}
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
            for bid, bm in (g.get("markets") or {}).items():
                for mk2 in ("spread", "total"):
                    for x in ((bm.get("event") or {}).get(mk2) or []):
                        if x.get("is_alt_market") or x.get("is_live") or x.get("value") is None:
                            continue
                        sd2 = x.get("side")
                        kk = sd2 if mk2 == "total" else (h if sd2 == "home" else a)
                        books_now.setdefault((a, h, mk2, kk), {})[bid] = x["value"]
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
    return hist, names, books_now


def main():
    now = dt.datetime.now(dt.timezone.utc)
    say("=" * 84)
    say(f"PROPWATCH WATCH   {now.strftime('%Y-%m-%dT%H:%MZ')}")
    say("=" * 84)
    say()

    pin, pints = pin_now()
    hist, names, books_now = fd_series()
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
        pp, lpp, ppp = eff_move(mk, k2, first["v"], first.get("odds"),
                                cur["v"], cur.get("odds"))
        # QUALIFY ON THE ENTRY SNAPSHOT'S SPLIT, NOT THE CURRENT ONE.
        # Runs 4 and 5 of the scheduled watch each lost a run to this, in opposite
        # directions. Run 4: DEN@PIT's over money fell 70% -> 64%, dropped below
        # PUBLIC_MNY, and the market vanished from the board entirely -- with the
        # two-point move still sitting there. The public being wrong and the money
        # leaving is the thing the setup is WAITING for, so a market that did what
        # the thesis wants deleted itself while one where the public never budges
        # stays visible forever. Run 5: the same market re-entered BROKEN on a
        # four-point money tick back to 68%, manufacturing a crossing out of a
        # spent move. So the test is whether this market was ever one-way, and the
        # current split prints alongside so the decay is visible instead of fatal.
        # how many of the trailing snapshots the CURRENT FanDuel (number, price) has
        # held. Every market shares the same total snapshot count, so printing that
        # alone was uninformative; the hold length is the figure every run's
        # verification reaches for by hand.
        held = 0
        for t in reversed(tss):
            r0 = series[t]
            if (r0.get("v"), r0.get("odds")) == (cur.get("v"), cur.get("odds")):
                held += 1
            else:
                break
        # HOW OLD IS THE LINE LEG ON ITS OWN, ignoring the price?
        # Runs 7 and 8 each lost their only "new crossing" to the same artifact in a
        # different leg. Run 7: WAS@ARI crossed because FanDuel's juice went -115 back
        # to -105, netting the price leg to zero and leaving a 30-hour-old half point
        # as the whole move. Run 8: ATL@MIN crossed because the public MONEY rose
        # through 65%, 31 hours after FanDuel's only line move, with Pinnacle's number
        # unchanged for 63.6 hours. In both the pp figure was real and the line leg
        # behind it was a day and a half stale, and in both the detector presented it
        # as today's event. So print the line leg's own age next to pp: `line L/Ms` is
        # how many trailing snapshots the current NUMBER has survived with the price
        # ignored. L close to M with a non-zero line leg means the move is old and the
        # crossing came from somewhere else. Classification is untouched -- this is a
        # print, and consecutive boards stay comparable.
        lheld = 0
        for t in reversed(tss):
            if series[t].get("v") == cur.get("v"):
                lheld += 1
            else:
                break
        entry = None
        for t in tss:
            r0 = series[t]
            if r0.get("tix") is not None and r0["tix"] >= PUBLIC_TIX \
                    and (r0.get("mny") or 0) >= PUBLIC_MNY:
                entry = (t, r0["tix"], r0["mny"])
                break
        if entry is None:
            continue
        # did the number move toward this (public) side?
        toward = pp > 0
        rec = {"g": f"{a}@{h}", "mk": mk, "side": k2, "open": first["v"], "now": cur["v"],
               "mv": mv, "pp": pp, "lpp": lpp, "ppp": ppp,
               "o_odds": first.get("odds"), "odds": cur["odds"],
               "tix": cur["tix"], "mny": cur["mny"],
               "e_ts": entry[0], "e_tix": entry[1], "e_mny": entry[2],
               "nb": cur["nb"], "st": cur["st"], "snaps": len(tss), "held": held,
               "lheld": lheld,
               "pin": (p or {}).get("pts"), "lim": (p or {}).get("lim"),
               "books": books_now.get((a, h, mk, k2), {})}
        if abs(pp) < MIN_PP:
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
            bs = r.get("books") or {}
            others = sorted({v for b, v in bs.items() if b not in ("69", "30")})
            ostr = ("books " + "/".join(f"{v:g}" for v in others)) if others else ""
            alone = len(others) == 1 and abs(others[0] - r["now"]) > 1e-9
            dec = "" if (r["e_tix"], r["e_mny"]) == (r["tix"], r["mny"]) else \
                  f" (entry {r['e_tix']}%/{r['e_mny']}%)"
            say(f"   {r['g']:10} {r['mk']:7} {str(r['side'])[:5]:5}  "
                f"public {r['tix']:>3}%/{r['mny']:>3}%{dec}  "
                f"{r['open']:g} ({r['o_odds']:+d}) -> {r['now']:g} ({r['odds']:+d}) "
                f"[held {r['held']}/{r['snaps']}s, line {r['lheld']}/{r['snaps']}s]  "
                f"= {r['pp']:+5.1f}pp (line {r['lpp']:+.1f} price {r['ppp']:+.1f})  "
                f"{pin_s}  {ostr}  {r['nb'] or 0:,} bets  {r['st'][:16].replace('T',' ')}Z"
                + ("   <-- FanDuel alone at its number" if alone else ""))
        say()

    show(broken, "BROKEN — the number moved AGAINST heavy public money",
         "the setup. Only visible because the prior state was recorded.")
    show(loaded, "LOADED — one-way money, number still on its opener",
         "nothing has happened yet. Where to look, not what to bet.")
    show(followed, "FOLLOWED — the number moved WITH the public",
         "not a fade. Printed because these get mistaken for fades afterwards.")

    say("-" * 84)
    say("Movement is in PROBABILITY POINTS with the price included, not line points: a")
    say("half point of spread is ~1.4pp and 20 cents of juice is ~4.5pp, so a line move")
    say("paired with worse juice can be a move against you. Threshold |pp| >= 1.0.")
    say("Public = >=65% of BOTH tickets and money AT THE ENTRY SNAPSHOT, carried")
    say("forward; the current split prints first and the entry split in brackets when")
    say("they differ, so a market whose money has left stays on the board instead of")
    say("deleting itself. [held N/Ms, line L/Ms] is how many of the M snapshots we hold")
    say("for this market the current FanDuel number AND price (N), and the number ALONE")
    say("with the price ignored (L), have survived -- counts, NOT a")
    say("duration: the collector ran at ~60 min up to 2026-11-25T1300Z and ~10 min")
    say("after it, so 6 prints before that change is an hour and 6 after it is ten")
    say("minutes. M is also the same for every market in a week that entered the feed")
    say("together, so \"open\" is the earliest value we hold, never a week opener.")
    say("L at or near M with a non-zero line leg means the HANDICAP has not moved in the")
    say("whole window and whatever put this market on the board today is the price leg or")
    say("the public split crossing the threshold, not a market event. Runs 7 and 8 each")
    say("lost their only new crossing to exactly that, in opposite legs.")
    say("Pinnacle read from the current")
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
