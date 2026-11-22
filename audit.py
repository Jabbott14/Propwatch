#!/usr/bin/env python3
"""audit.py -- produces the research question nobody asked for.

The brain doc only works if a session opens it. The guards in the graders only fire when
a measurement is already wrong. Neither of those makes anyone NOTICE that something needs
investigating. That is what this does, and it runs on a schedule rather than on demand,
because the whole failure mode is nobody asking.

Four sections, in the order they matter:

  1. STALE        register items sitting in RECORDED with nothing consuming them, aged in
                  days. Recorded-and-forgotten is this repo's characteristic failure --
                  path features, key numbers and limit cuts are all computed right now and
                  graded by nothing.
  2. ANOMALIES    every graded cell with >=30 decisions, ranked by |z|, printed ALONGSIDE
                  how many cells chance alone produces at that z. The second number is the
                  point. A 2.3-sigma cell read in isolation looks like a finding; read next
                  to "18 cells at this level are expected from 806 by chance" it looks like
                  what it is. The project has quantified this and then quoted single cells
                  anyway, which is why the two numbers now print together or not at all.
  3. QUESTIONS    the open-question queue, aged. A question nobody has touched in three
                  weeks is either answered somewhere or not worth asking.
  4. DRIFT        holdout age, forward sample size, and whether the forward record has
                  reached the size where it can say anything.

Writes AUDIT.md and prints the same thing to the Actions log. Exits 0 always -- this is a
prompt, not a gate. A gate that fails a run gets disabled; a prompt that shows up in the
log and in a file gets read.
"""
import json, math, os, sys, datetime, collections

ROOT = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.date.today()
BREAKEVEN = 110 / 210          # -110 both sides
MIN_DEC = 30                   # below this a z-score is theatre
STALE_RECORDED = 14            # days a RECORDED item may sit before it is called out
STALE_QUESTION = 21

L = []
def say(s=""):
    L.append(s)
    print(s, flush=True)


def days(d):
    try:
        return (TODAY - datetime.date.fromisoformat(d)).days
    except Exception:
        return None


def load(p):
    try:
        return json.load(open(os.path.join(ROOT, p)))
    except Exception as e:
        say(f"  (could not read {p}: {e})")
        return None


# ---------------------------------------------------------------- 1. stale register
def stale(reg):
    say("## 1. RECORDED AND CONSUMED BY NOTHING")
    say()
    ideas = reg.get("ideas", [])
    rec = [i for i in ideas if i.get("state") == "RECORDED"]
    opn = [i for i in ideas if i.get("state") == "OPEN"]
    if not rec and not opn:
        say("  nothing recorded-but-unused. That has never been true before; check the file.")
        return
    say(f"  {len(rec)} RECORDED (computed, graded by nothing) | {len(opn)} OPEN (not built)")
    say()
    for grp, items in (("RECORDED", rec), ("OPEN", opn)):
        for i in sorted(items, key=lambda x: -(days(x.get("recorded", "")) or 0)):
            d = days(i.get("recorded", ""))
            age = f"{d}d" if d is not None else "undated"
            flag = ""
            if d is not None and d >= STALE_RECORDED:
                flag = "  <-- STALE" if grp == "RECORDED" else "  <-- stale"
            say(f"  [{grp:8}] {age:>8}  {i['idea']}{flag}")
            say(f"             {i.get('where','')}")
            if i.get("note"):
                say(f"             note: {i['note']}")
            say()
    nstale = sum(1 for i in rec if (days(i.get('recorded','')) or 0) >= STALE_RECORDED)
    if nstale:
        say(f"  {nstale} recorded item(s) past {STALE_RECORDED} days. Each is a feature being")
        say("  computed on every run and read by no grading code. Either grade it (which moves")
        say("  the holdout -- that cost is deliberate) or move it to TESTED with a result.")
        say()


# ---------------------------------------------------------------- 2. anomaly scan
def anomalies(sources):
    say("## 2. ANOMALY SCAN, WITH THE MULTIPLE-COMPARISONS DENOMINATOR")
    say()
    # z must be against the cell's OWN base rate, not against break-even. The first
    # version of this function used z_vs_breakeven and read "377 cells at z>=3 against 7.9
    # expected", which is rule 3 all over again: a signal that systematically takes
    # favourites in a market where favourites cover 70% scores enormously against
    # break-even while carrying no edge at all. expected_pct is the base-rate-corrected
    # expectation the grader already computes; edge is hit minus that.
    #
    # And the cells are not independent, so they cannot all go in the denominator:
    #   period "all"     is fit+fwd re-counted
    #   market "both"    pools markets that have different base rates
    #   signal with "+"  is a pair derived from two singles already counted
    # Each of those is dropped from the test and counted separately, so the denominator is
    # cells that could plausibly vary on their own rather than every row in the file.
    rows, dropped = [], collections.Counter()
    for sport, s in sources.items():
        for r in (s.get("signals") or []):
            dec = (r.get("W") or 0) + (r.get("L") or 0)
            if dec < MIN_DEC:
                continue
            if r.get("period") == "all":
                dropped["period=all (fit+fwd re-counted)"] += 1; continue
            if r.get("market") == "both":
                dropped["market=both (pools base rates)"] += 1; continue
            if "+" in str(r.get("signal", "")):
                dropped["signal pair (derived from singles)"] += 1; continue
            p = r.get("expected_pct")
            if p is None:
                dropped["no base rate (no fav/dog decision)"] += 1; continue
            p = p / 100.0
            if not (0 < p < 1):
                dropped["degenerate base rate"] += 1; continue
            z = (r["W"] - dec * p) / math.sqrt(dec * p * (1 - p))
            rows.append((sport, r, dec, z))

    if not rows:
        say("  no cell has reached 30 decisions. Nothing to scan, which is itself the finding.")
        return

    total = len(rows)
    if dropped:
        say("  excluded as non-independent or unscoreable:")
        for k, v in dropped.most_common():
            say(f"    {v:>6}  {k}")
        say()
    # Two-sided, because a cell that loses badly is as interesting as one that wins and the
    # project has only ever looked at the winning tail.
    def expected(thr):
        # P(|Z| > thr) under the null, normal approximation
        p = math.erfc(thr / math.sqrt(2))
        return total * p

    say(f"  independent-ish cells with >={MIN_DEC} decisions: {total}")
    say("  z is hit rate against each cell's OWN base rate, not against break-even.")
    for thr in (1.65, 2.0, 2.5, 3.0):
        got = sum(1 for _, _, _, z in rows if abs(z) >= thr)
        exp = expected(thr)
        verdict = ("nothing here" if got <= exp * 1.2 else
                   "marginally above chance" if got <= exp * 2 else
                   "ABOVE CHANCE -- worth a look")
        say(f"    |z| >= {thr:<4}  observed {got:<5} expected-by-chance {exp:>6.1f}   {verdict}")
    say()
    say("  The expected column is not a caveat. It is the comparison. A cell is only")
    say("  evidence if the observed count at its z exceeds the expected count, and then")
    say("  only the excess is evidence -- not that cell in particular.")
    say()

    # --- sign asymmetry. The count-vs-expected test above asks whether there are MORE
    #     extreme cells than chance allows. It cannot see direction, and direction turned
    #     out to be where the information was: on the first run of this script the forward
    #     tail was 29 negative to 15 positive with a mean z of -0.40, while the fit tail
    #     sat at +0.06. Pure noise gives mean 0 in both. A fitted-then-failed signal gives
    #     positive fit and ZERO forward. Negative forward means the signals are landing on
    #     the losing side more often than chance -- which is a different claim, and a
    #     testable one, so it prints every run rather than being found once.
    say("  ### SIGN ASYMMETRY (direction, which the count test cannot see)")
    say()
    for per in ("fwd", "fit"):
        sub = [(r, z) for _, r, _, z in rows if r.get("period") == per]
        if len(sub) < 10:
            continue
        n = len(sub)
        neg = sum(1 for _, z in sub if z < 0)
        pos = n - neg
        k = min(neg, pos)
        p = min(1.0, sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n * 2)
        mz = sum(z for _, z in sub) / n
        say(f"  {per.upper():4} {n:>4} cells   {pos} positive / {neg} negative   "
            f"mean z {mz:+.2f}   sign test p={p:.3f}")
        bysig = collections.defaultdict(list)
        for r, z in sub:
            bysig[r["signal"]].append(z)
        worst = sorted(bysig.items(), key=lambda x: sum(x[1]) / len(x[1]))
        for sig, zs in worst[:3] + worst[-3:]:
            say(f"         {sig:18} n={len(zs):>3}  mean z {sum(zs)/len(zs):+.2f}")
        say()
    say("  Read the two mean-z lines together. Noise is 0 and 0. Overfit-then-failed is")
    say("  positive fit and 0 forward. Positive fit and NEGATIVE forward is a third thing,")
    say("  and the cells are not independent of each other (same games, nested slices), so")
    say("  the p-value above is optimistic. Treat it as a question, not a result.")
    say()

    # Rank, but show FORWARD separately: a fit cell at 3 sigma is a hypothesis by
    # construction, and mixing them is how in-sample records got quoted as reasons to bet.
    for per, label in (("fwd", "FORWARD (out of sample -- evidence)"),
                       ("fit", "FIT (in sample -- hypotheses only)")):
        sub = [x for x in rows if x[1].get("period") == per]
        if not sub:
            continue
        sub.sort(key=lambda x: -abs(x[3]))
        say(f"  ### {label}  ({len(sub)} cells)")
        say()
        say(f"  {'sport':5} {'signal':22} {'cp':6} {'mkt':9} {'slice':12} "
            f"{'W-L':>8} {'hit%':>6} {'base%':>6} {'edge':>6} {'ROI%':>7} {'z':>6}")
        for sport, r, dec, z in sub[:12]:
            mix = r.get("market_mix")
            warn = ""
            if mix and max(mix.values()) >= 85 and r.get("slice") != "all":
                warn = f"  !mix {max(mix, key=mix.get)} {max(mix.values())}%"
            say(f"  {sport:5} {str(r['signal'])[:22]:22} {str(r['checkpoint'])[:6]:6} "
                f"{str(r['market'])[:9]:9} {str(r['slice'])[:12]:12} "
                f"{str(r['W'])+'-'+str(r['L']):>8} {str(r.get('hit_pct')):>6} "
                f"{str(r.get('expected_pct')):>6} {str(r.get('edge_pts')):>6} "
                f"{str(r.get('roi_pct')):>7} {z:>6.2f}{warn}")
        say()


# ---------------------------------------------------------------- 3. open questions
def questions(reg):
    say("## 3. OPEN QUESTIONS, AGED")
    say()
    qs = reg.get("questions", [])
    if not qs:
        say("  the queue is empty. That means nobody has written down what they don't know.")
        return
    for q in sorted(qs, key=lambda x: -(days(x.get("asked", "")) or 0)):
        d = days(q.get("asked", ""))
        age = f"{d}d" if d is not None else "undated"
        flag = "  <-- UNTOUCHED" if d is not None and d >= STALE_QUESTION else ""
        say(f"  [{age:>6}] {q['q']}{flag}")
        say(f"           why: {q.get('why','')}")
        say(f"           next: {q.get('next','')}  (owner: {q.get('owner','unassigned')})")
        say()


# ---------------------------------------------------------------- 4. drift
def drift(sources):
    say("## 4. HOLDOUT AND FORWARD SAMPLE")
    say()
    for sport, s in sources.items():
        hf = s.get("holdout_from")
        fwd, fit = s.get("forward_games"), s.get("fit_games")
        d = days(hf) if hf else None
        say(f"  {sport}: holdout from {hf}" + (f" ({d}d ago)" if d is not None else ""))
        say(f"         {fit} fit games, {fwd} forward games")
        if fwd is not None and fwd < 60:
            say(f"         forward sample is {fwd} games. Nothing measured forward can")
            say("         distinguish a 55% signal from a 50% one yet. Do not promote on it.")
        if d is not None and d <= 2:
            say("         the holdout moved in the last 2 days -- a threshold changed, so the")
            say("         forward test restarted. Every forward record below is new.")
        say()


# ---------------------------------------------------------------- 5. filter lift
# Several "signals" are not signals. Measured 2026-11-22 on 332 CBB games: when rlm_quiet
# fires, follow_move fires on the SAME side 523 out of 523 times. rlm_ratio, 477 of 477.
# This is by construction -- both require the line to have moved toward their side, which
# IS follow_move's call -- so they are FILTERS on follow_move, not independent opinions.
# pin_rlm sits at 87.2% inside pin_move for the same reason.
#
# Two consequences, and the second is a defect:
#
# 1. The project does not have twelve signals. Eight pairs agree on side 100% of the time
#    when both fire. Multiple comparisons are therefore less inflated than the 806-cell
#    count implies -- but so is every "two signals confirm" reading, because in many cases
#    it is one signal counted twice. The pair rows in the scorecard were built on "evidence
#    combines"; for a pair that agrees 100% of the time, nothing combines.
#
# 2. THE WRONG DENOMINATOR. The scorecard grades every signal against a market base rate.
#    For a strict subset of another signal, the base rate is not the comparison anyone
#    cares about: the question is whether the filter beats its PARENT on the same games.
#    Scored that way, rlm_ratio on CBB totals lifts follow_move from 45.5% to 53.6% --
#    ROI -13.1 to +2.6, n=252, z=+2.03 -- which the base-rate scorecard reports as an
#    unremarkable row. Three signals have been graded against the wrong thing all along.
#
# Computing a lift changes no call, so the holdout does not reset.
PARENT = {"rlm_quiet": "follow_move", "rlm_ratio": "follow_move", "pin_rlm": "pin_move"}


def _vol(nb):
    nb = nb or 0
    return "<1k" if nb < 1000 else ("1-3k" if nb < 3000 else "3k+")


def filter_lift(sport, holdout):
    path = os.path.join(ROOT, sport, "graded", "games.json")
    if not os.path.exists(path):
        return
    try:
        games = json.load(open(path))
    except Exception as e:
        say(f"  (could not read {sport} games.json: {e})")
        return
    say(f"  ### {sport.upper()}")
    say()
    for child, parent in PARENT.items():
        acc = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0, 0.0]))
        for gm in games:
            per = "fit" if (gm.get("date") or "")[:10] < holdout else "fwd"
            for mkt, m in (gm.get("markets") or {}).items():
                gr = m.get("close_graded") or {}
                r = m.get("close") or {}
                if parent not in gr:
                    continue
                x = gr[parent]
                if x.get("res") == "P":
                    continue
                grp = "with" if child in gr else "without"
                for sl in ("all", _vol(r.get("nb"))):
                    for pr in ("all", per):
                        a = acc[(mkt, sl, pr)][grp]
                        a[0] += x["res"] == "W"; a[1] += 1; a[2] += x.get("units", 0)
        printed = False
        for mkt in ("spread", "total", "moneyline"):
            for sl in ("all", "<1k", "1-3k", "3k+"):
                d = acc.get((mkt, sl, "all"))
                if not d:
                    continue
                w, wo = d.get("with"), d.get("without")
                if not w or not wo or w[1] < 25 or wo[1] < 25:
                    continue
                if not printed:
                    say(f"  does {child} improve on its parent {parent}?")
                    printed = True
                hw, hwo = 100 * w[0] / w[1], 100 * wo[0] / wo[1]
                rw, rwo = 100 * w[2] / w[1], 100 * wo[2] / wo[1]
                p = (w[0] + wo[0]) / (w[1] + wo[1])
                se = math.sqrt(p * (1 - p) * (1 / w[1] + 1 / wo[1]))
                z = ((w[0] / w[1]) - (wo[0] / wo[1])) / se if se else 0.0
                # On a moneyline the hit-rate lift is an artifact and must not be read:
                # these filters take the minority-MONEY side, which on a moneyline is the
                # dog, so they trade a ~70% base for a ~35% one by construction. The ROI
                # columns are the only meaningful ones there, and they disagree with the
                # hit rate -- pin_rlm reads -22.0 points of hit and +19.2 of ROI. This is
                # the hit-rate trap the project already closed once, in a new place.
                note = "   [ML: read ROI only, hit lift is a dog/fav artifact]" if mkt == "moneyline" else ""
                say(f"    {mkt:9} {sl:5}  with {hw:5.1f}% n={w[1]:>3} ROI {rw:+6.1f}   "
                    f"without {hwo:5.1f}% n={wo[1]:>3} ROI {rwo:+6.1f}   "
                    f"lift {hw-hwo:+6.1f}pt / {rw-rwo:+6.1f}ROI  z {z:+5.2f}{note}")
        if printed:
            say()


def filters(sources):
    say("## 5. FILTER LIFT -- signals that are subsets of other signals")
    say()
    say("  rlm_quiet and rlm_ratio fire only where follow_move also fires, 100% of the")
    say("  time, by construction. pin_rlm sits 87% inside pin_move. They are filters, so")
    say("  the comparison that matters is against the PARENT on the same games, not")
    say("  against a market base rate. Scored against a base rate they look unremarkable.")
    say()
    for sport, s in sources.items():
        filter_lift(sport, s.get("holdout_from") or "9999-01-01")


def main():
    say("=" * 78)
    say(f"PROPWATCH AUDIT   {TODAY.isoformat()}")
    say("=" * 78)
    say()
    say("Nobody asked for this. That is the point -- the knowledge base only gets read when")
    say("a session opens it, and the guards only fire once a measurement is already wrong.")
    say()

    reg = load("register.json") or {}
    sources = {}
    for sport, path in (("cbb", "cbb/graded/summary.json"), ("nfl", "nfl/graded/summary.json"),
                        ("ncaaf", "ncaaf/graded/summary.json")):
        s = None
        if os.path.exists(os.path.join(ROOT, path)):
            s = load(path)
        if s:
            sources[sport] = s
    if not sources:
        say("  no grader summary found. Run the graders first; sections 2 and 4 need them.")
        say()

    if reg:
        stale(reg)
    if sources:
        anomalies(sources)
    if reg:
        questions(reg)
    if sources:
        filters(sources)
        drift(sources)

    say("-" * 78)
    say("The standing rule: search the project docs before investigating anything here.")
    say("An hour went on a question already answered 0-for-17 in propwatch-line-value-state.")
    say("-" * 78)

    with open(os.path.join(ROOT, "AUDIT.md"), "w") as f:
        f.write("# Propwatch audit\n\nGenerated " + TODAY.isoformat() +
                " by `audit.py`. Nobody asked for it; that is the point.\n\n```\n" +
                "\n".join(L) + "\n```\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
