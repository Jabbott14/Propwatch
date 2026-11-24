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


# ---------------------------------------------------------------- 0. collector heartbeat
def heartbeat():
    """Is the data still arriving? Nothing in this system asked that until two outages
    were found by hand on consecutive days:

      * VSIN stopped 2026-11-12 and nobody noticed for TEN DAYS -- and what it had been
        archiving was the page shell with no numbers in it anyway.
      * The NFL collector (`snap`) died 2026-11-23T01:12Z, fifteen minutes before the
        MIN@SF kickoff, so that game has no closing data at all. It came back, died
        again, and was 7h cold when the Monday card was being built. CBB and NCAAF ran
        clean through all of it, which is why nothing looked wrong.

    Every other check in this file reasons about data that is present. A measurement
    computed from a feed that stopped is not wrong, it is stale, and stale looks exactly
    like a quiet market. That is the worst failure mode this project has, because it is
    invisible in every downstream number.

    Thresholds are per-feed because the cadences differ: snap targets 3-10 min near a
    kickoff, cbb and ncaaf 30 min.
    """
    import subprocess, datetime as dt
    say("## 0. IS THE DATA STILL ARRIVING?")
    say()
    FEEDS = [("snap", 90, "NFL collector"), ("cbb", 90, "CBB collector"),
             ("ncaaf", 120, "NCAAF collector"), ("nfl grade", 1440, "NFL grader"),
             ("grade-cbb", 1440, "CBB grader")]
    now = dt.datetime.now(dt.timezone.utc)
    bad = 0
    for prefix, max_min, label in FEEDS:
        try:
            out = subprocess.run(["git", "log", "-1", "--format=%cI", f"--grep=^{prefix}"],
                                 cwd=ROOT, capture_output=True, text=True, timeout=30).stdout.strip()
            if not out:
                # A shallow clone holds only the most recent commits, so a feed that
                # commits less often than the others legitimately has none in range.
                # Saying "never ran" there is a false alarm, and a guard that cries wolf
                # trains people to scroll past it -- the check_rate lesson, which fired
                # 95 times on its first calibration.
                depth = subprocess.run(["git", "rev-list", "--count", "HEAD"],
                                       cwd=ROOT, capture_output=True, text=True).stdout.strip()
                shallow = subprocess.run(["git", "rev-parse", "--is-shallow-repository"],
                                         cwd=ROOT, capture_output=True, text=True).stdout.strip()
                if shallow == "true":
                    say(f"  {label:16} not in the last {depth} commits (shallow clone — not a failure)")
                else:
                    say(f"  {label:16} NO COMMITS FOUND  <-- never ran, or the message changed")
                    bad += 1
                continue
            age = (now - dt.datetime.fromisoformat(out)).total_seconds() / 60
            flag = ""
            if age > max_min:
                flag = f"  <-- STALE, expected every ~{max_min}m"; bad += 1
            say(f"  {label:16} last {age/60:6.1f}h ago  ({out}){flag}")
        except Exception as e:
            say(f"  {label:16} check failed: {e}")
    say()
    bad_feeds = 0

    # --- did any SOURCE fail? The feed check above only sees whether commits arrive.
    #     A collector can run perfectly, commit on schedule, and be silently failing to
    #     fetch one of its sources -- which is exactly what happened: VSIN has returned
    #     HTTP 403 on EVERY cycle since 2026-11-12 and data/_diag.json recorded it every
    #     time. Nobody read it for twelve days.
    #
    #     Worse, the diag's own health line says `pulls_fail: 0` while two pulls fail,
    #     because ok/fail count only the per-game FanDuel prop requests. archive()
    #     failures land in attempts[].error and are counted nowhere. The one number a
    #     person would check was structurally incapable of showing the problem.
    for diagp in ("data/_diag.json", "cbb/data/_diag.json", "ncaaf/data/_diag.json"):
        fp = os.path.join(ROOT, diagp)
        if not os.path.exists(fp):
            continue
        try:
            dg = json.load(open(fp))
        except Exception:
            continue
        badsrc = [a for a in (dg.get("attempts") or []) if a.get("error")]
        tag = diagp.split("/")[0] if "/" in diagp else "nfl"
        if badsrc:
            say(f"  {tag:16} SOURCES FAILING as of {dg.get('run_utc','?')}:")
            for a in badsrc:
                say(f"      {a.get('name','?'):14} {a.get('error','?')}")
            say(f"      (that run reported pulls_fail={dg.get('pulls_fail')} — the counter")
            say("       covers prop requests only, not these)")
            bad_feeds += 1
        else:
            say(f"  {tag:16} all sources OK as of {dg.get('run_utc','?')}")
    say()
    bad += bad_feeds
    if bad:
        say(f"  {bad} feed/source problem(s). EVERY NUMBER BELOW THAT DEPENDS ON THEM IS SUSPECT --")
        say("  a dead feed does not look like an error downstream, it looks like a quiet")
        say("  market. Check the Actions tab before trusting anything in sections 2-5.")
    else:
        say("  all feeds current.")
    say()


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
# pre_move is deliberately NOT here: it fires 11 times in NFL and follow_move fires on
# ZERO of them, because pre_move claims the move has not happened yet. It is the
# COMPLEMENT of follow_move, not a subset -- genuinely independent, and the only signal in
# the set that is.
PARENT = {"rlm_quiet": "follow_move", "rlm_ratio": "follow_move",
          "rlm": "follow_move",          # NFL only: 41/41 inside follow_move, same side
          "pin_rlm": "pin_move"}


def _gdate(gm):
    """The graders do not agree on this field name and neither carries "date": CBB writes
    `tip`, NFL writes `kickoff`. Reading `date` returned None for every game in both, so
    "" < holdout classified the entire archive as FIT and the forward split was dead while
    looking like it worked. Only the period="all" rows were being printed, so nothing
    reported was wrong -- which is exactly why it survived."""
    return ((gm.get("date") or gm.get("tip") or gm.get("kickoff") or "")[:10])


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
            per = "fit" if _gdate(gm) < holdout else "fwd"
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
              for pr in ("all", "fwd"):
                d = acc.get((mkt, sl, pr))
                if not d:
                    continue
                w, wo = d.get("with"), d.get("without")
                if not w or not wo or w[1] < 25 or wo[1] < 25:
                    continue
                if not printed:
                    say(f"  does {child} improve on its parent {parent}?")
                    printed = True
                lbl = f"{mkt:9} {sl:5}" + ("  FWD" if pr == "fwd" else "     ")
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
                say(f"    {lbl}  with {hw:5.1f}% n={w[1]:>3} ROI {rw:+6.1f}   "
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



# ---------------------------------------------------------------- 6. recorded features
# Five register items have sat RECORDED for days: key numbers, Pinnacle limit cuts, the
# path layer, retracement, and filter-lift. Every one is computed on every run and read
# by nothing. That is this repo's characteristic failure, and audit.py has been flagging
# it as stale without doing anything about it.
#
# The reason they were never graded is real: promoting a feature to a SIGNAL changes
# which plays the board emits, which moves HOLDOUT_FROM and restarts the forward test.
# That cost is deliberate and should not be paid on a hunch.
#
# But scoring a feature as a CONDITIONER on calls that were already made changes no call
# at all. The holdout does not move. So there is no reason these have gone unmeasured,
# and this section measures them: split every graded call by the feature, compare the
# two halves, and print the number of tests alongside, because 8 features x 3 markets is
# 24 comparisons and roughly one will clear |z|>=2 on noise alone.
FEATURES = [
    ("lim_slashed",   lambda p: bool(p.get("lim_slashed")),                 "Pinnacle cut its limit"),
    ("line_reversed", lambda p: (p.get("line_revs") or 0) >= 1,             "the number reversed at least once"),
    ("mny_crossed",   lambda p: (p.get("mny_crossings") or 0) >= 1,         "money majority changed sides"),
    ("mny_gave_back", lambda p: (p.get("mny_gave_back") or 0) >= 10,        "money peaked then retreated >=10pts"),
    ("line_ineff",    lambda p: (p.get("line_eff") is not None and p["line_eff"] < 0.5),
                                                                            "the number wandered (efficiency <0.5)"),
    ("key_crossed",   lambda p: bool(p.get("key_crossed")),                 "crossed a key number (3/7)"),
    ("deep_series",   lambda p: (p.get("n_obs") or 0) >= 200,               "200+ observations in the series"),
]


def _gper(gm, holdout):
    d = (gm.get("date") or gm.get("tip") or gm.get("kickoff") or "")[:10]
    return "fit" if d < holdout else "fwd"


def features(sports, holdouts):
    say("## 6. RECORDED FEATURES, SCORED AS CONDITIONERS")
    say()
    say("  Splitting calls already made. No call changes, so the holdout does NOT move.")
    say("  This is what 'RECORDED and consumed by nothing' was costing.")
    say()
    tests = 0
    out = []
    for sport in sports:
        path = os.path.join(ROOT, sport, "graded", "games.json")
        if not os.path.exists(path):
            continue
        try:
            games = json.load(open(path))
        except Exception:
            continue
        for fname, fn, desc in FEATURES:
            acc = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0, 0.0]))
            ho = holdouts.get(sport) or "9999-01-01"
            for gm in games:
                per = _gper(gm, ho)
                for mkt, m in (gm.get("markets") or {}).items():
                    c = m.get("close") or {}
                    p = c.get("path")
                    if not p:
                        continue
                    try:
                        flag = fn(p)
                    except Exception:
                        continue
                    for sig, r in (m.get("close_graded") or {}).items():
                        if r.get("res") == "P":
                            continue
                        a = acc[(mkt, per)]["yes" if flag else "no"]
                        a[0] += r["res"] == "W"; a[1] += 1; a[2] += r.get("units", 0)
            for (mkt, per), d in acc.items():
                y, n = d.get("yes"), d.get("no")
                if not y or not n or y[1] < 25 or n[1] < 25:
                    continue
                tests += 1
                hy, hn = 100 * y[0] / y[1], 100 * n[0] / n[1]
                ry, rn = 100 * y[2] / y[1], 100 * n[2] / n[1]
                pp = (y[0] + n[0]) / (y[1] + n[1])
                se = math.sqrt(pp * (1 - pp) * (1 / y[1] + 1 / n[1]))
                z = ((y[0] / y[1]) - (n[0] / n[1])) / se if se else 0.0
                out.append((abs(z), sport, per, fname, mkt, hy, y[1], ry, hn, n[1], rn, z, desc))
    if not out:
        say("  no feature reached 40 decisions on both sides of a split.")
        say()
        return
    out.sort(reverse=True)
    say(f"  {tests} comparisons made. Chance alone gives ~{tests*0.05:.1f} at |z|>=2.0 and")
    say(f"  ~{tests*0.10:.1f} at |z|>=1.65. Read every row below against those two numbers.")
    say()
    say(f"  {'sport':5} {'per':4} {'feature':14} {'mkt':9} {'WITH':>22} {'WITHOUT':>22} {'z':>6}")
    for _, sport, per, fname, mkt, hy, ny, ry, hn, nn, rn, z, desc in out:
        say(f"  {sport:5} {per:4} {fname:14} {mkt:9} "
            f"{f'{hy:.1f}% n={ny} {ry:+.1f}':>22} {f'{hn:.1f}% n={nn} {rn:+.1f}':>22} {z:>6.2f}")
    say()
    say("  FIT is a hypothesis, FORWARD is evidence. A feature that only appears in FIT")
    say("  rows has not been tested; one that holds in both, and across sports, is the")
    say("  project's own standard for believing anything.")
    say()
    hits = [o for o in out if abs(o[11]) >= 2.0]
    say(f"  {len(hits)} at |z|>=2.0 against ~{tests*0.05:.1f} expected. " +
        ("Nothing here." if len(hits) <= tests * 0.05 * 1.5 else "Above chance — worth a look."))
    say("  ROI is the currency, not hit rate: money_level hit 73.4% and lost 14.87 units.")
    say()


def main():
    say("=" * 78)
    say(f"PROPWATCH AUDIT   {TODAY.isoformat()}")
    say("=" * 78)
    say()
    say("Nobody asked for this. That is the point -- the knowledge base only gets read when")
    say("a session opens it, and the guards only fire once a measurement is already wrong.")
    say()

    heartbeat()

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
        features(list(sources), {k: (v.get('holdout_from') or '9999-01-01') for k, v in sources.items()})
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
