# Propwatch audit

Generated 2026-11-25 by `audit.py`. Nobody asked for it; that is the point.

```
==============================================================================
PROPWATCH AUDIT   2026-11-25
==============================================================================

Nobody asked for this. That is the point -- the knowledge base only gets read when
a session opens it, and the guards only fire once a measurement is already wrong.

## 0. IS THE DATA STILL ARRIVING?

  NFL collector    not in the last 1 commits (shallow clone — not a failure)
  CBB collector    last    0.2h ago  (2026-11-25T22:12:42Z)
  NCAAF collector  not in the last 1 commits (shallow clone — not a failure)
  NFL grader       not in the last 1 commits (shallow clone — not a failure)
  CBB grader       not in the last 1 commits (shallow clone — not a failure)

  data             all sources OK as of 2026-11-25T22:00:39Z
  cbb              all sources OK as of 2026-11-25T22:12:33Z
  ncaaf            all sources OK as of 2026-11-25T22:02:01Z

  all feeds current.

## 1. RECORDED AND CONSUMED BY NOTHING

  3 RECORDED (computed, graded by nothing) | 9 OPEN (not built)

  [RECORDED]       3d  signals that are strict SUBSETS of other signals are graded against the wrong thing
             audit.py section 5 computes lift vs parent; the scorecard still grades vs base rate
             note: audit.py section 5 computes filter lift vs parent. Still RECORDED because the live SCORECARD continues to grade rlm_quiet/rlm_ratio/rlm/pin_rlm against a market base rate rather than their parent, so the board a person reads still shows the wrong comparison.

  [RECORDED]       3d  retracement off the Pinnacle extreme -- a number that bottomed and climbed back is not the same as one still falling
             pin_bounce, retraced -- display only
             note: pin_bounce and pin_extreme are stored on every close row but are not yet in the audit's feature list -- the path-layer features were graded first. Next one to wire in.

  [RECORDED]       2d  the NFL collector dies silently and nothing notices
             audit.py section 0 (heartbeat) now checks it; the workflow itself is NOT fixed
             note: DEFECT. `snap` ran every ~10 min then STOPPED 2026-11-23T01:12Z -- fifteen minutes before the MIN@SF kickoff -- so that game has no closing data. Came back 10:56Z, 9.7h gap. Died again, 3h gap. Last run 14:46Z and was 7.6h cold when Monday's card was being built. CBB and NCAAF ran clean every 30 min through all of it, which is exactly why nothing looked wrong. collect.yml is cron '7 * * * *' with timeout-minutes 350, so ~6 runs overlap by design, and `continue-on-error: true` means a failing step never surfaces. Suspected cause is Actions concurrency/queue pressure on NFL Sunday (6 overlapping 5h50m snap jobs plus cbb, ncaaf and the graders), but THIS IS UNVERIFIED -- the Actions API was not reachable from the session that found it. Justin needs to read the Actions tab. A stale feed is the worst failure this project has because downstream it does not look like an error, it looks like a quiet market.

  [OPEN    ]       3d  most-bet / most-watched games are where to fade the public -- NOT standalone, but combined with other signals
             volume slice runs on all 12 signals; audit.py section 5 now reports it per filter
             note: HIS CORRECTION, 2026-11-22, and it was right. The standalone form is measured and dead: fading the public INVERTS with volume, 52.1% under 1k bets -> 47.4% at 4k+, spreads 4k+ 43.0% / -17.9% on n=114. But I then closed the whole idea on 3 of 12 signals, which is not a test of it. His words: 'maybe it isn't that easy of just fading public but looking at most bet games and fading public w other signals involved as well -- we have many other different signals too.' Re-run across all 12: n-weighted aggregate is FLAT in every market (|z| all under 1.5), so volume is not a blanket conditioner. Per-cell, 9 of 26 signal x market cells rise monotonically with volume against 4.3 expected by chance, 4 fall -- a mild excess on correlated cells. Spread and total disagree in direction for the same signal (rlm_quiet spread lift +1.3 -> +11.8 with volume; total lift -9.0 -> -22.0). STAYS OPEN: the aggregate says no, the per-cell picture is not flat, NFL cannot check it (0 forward cells at n>=30), and everything above is FIT.

  [OPEN    ]       3d  CFB limits scale differently than NFL, so raw limit comparison is wrong across sports
             raw limits still compared

  [OPEN    ]       3d  steam = many books moving at once
             breadth (books-per-interval) only -- ordering is PERMANENTLY unmeasurable, all 7 books share our snapshot timestamp
             note: data is in hand; the breadth measurement has not been built

  [OPEN    ]       3d  our own closing-line model, to price independently of the books
             needs hoopR

  [OPEN    ]       3d  Circa as a second sharp reference alongside Pinnacle
             raw/vsin_circa collected, never parsed

  [OPEN    ]       3d  record each book's OWN observed change time, not our snapshot time
             collector change, not made -- this is the only thing that would make lead-lag measurable going forward

  [OPEN    ]       3d  the BOOK'S OWN EXPOSURE -- which side the house needs. Upstream of why a number moves.
             not collected anywhere
             note: Justin shared a Patrick Everson / Prime Sportsbook post 2026-11-22 listing 'Biggest House Needs' (Lions -3.5, Panthers -2.5, Bills -16.5, Raiders +10.5, Giants +5.5) alongside sharp action and public plays. We collect tickets and money -- what BETTORS did. We have never had what the BOOK is holding. A book moves a number to balance its own book, so its liability is upstream of the move we measure; every signal in this system reads the move and infers backwards. HONEST LIMIT: this is not published as a feed. It appears in weekly columns written by people (Everson/Prime, VSIN liability reports, SuperBook). Treat it as a manual cross-check when Justin shares one, not a signal input, unless a structured source turns up. Also unresolved: Everson listed Lions -3.5 under BOTH 'Top Public Plays' and 'Biggest House Needs', which is not consistent under either reading of the term -- do not build on it until the convention is confirmed.

  [OPEN    ]       3d  'the public' is one book's clientele, not a fact about the world
             every public/fade signal reads Action Network book 69 only
             note: MATERIAL LIMIT ON THE WHOLE FADE-THE-PUBLIC THESIS, found 2026-11-22 by cross-checking Justin's Everson post. Prime listed 'Dolphins +16.5' as a top public play while our Action Network data read 60% of tickets on BUFFALO -- the opposite side. Prime listed public on Ravens +2.5 where we read 49/50, no lean at all. rlm, rlm_quiet, rlm_ratio, sharp_gap and the volume slices all define 'the public' as FanDuel's ticket split via Action Network. If two books disagree about which side the public is on, then a fade signal is fading one book's customers, and its record is a statement about that book, not about public money. Nothing in the archive can currently test this because we have only ever had one source of splits.

  [OPEN    ]       1d  name Action Network books 15, 49, 68, 71, 75
             nowhere -- only 69 (FanDuel) and 30 (opener) are identified in the codebase
             note: BLOCKING. xbook.py found that book 75 leads the market at z=+3.67 and nobody knows what book 75 is. The AN payload carries no book metadata -- no names, no books array. Identify by cross-referencing a known line at a known time against a named sportsbook, or by finding AN's book-list endpoint. Until then the strongest cross-book result in the project points at an anonymous book.

## 2. ANOMALY SCAN, WITH THE MULTIPLE-COMPARISONS DENOMINATOR

  excluded as non-independent or unscoreable:
      1584  period=all (fit+fwd re-counted)
       822  market=both (pools base rates)
       755  signal pair (derived from singles)

  independent-ish cells with >=30 decisions: 389
  z is hit rate against each cell's OWN base rate, not against break-even.
    |z| >= 1.65  observed 47    expected-by-chance   38.5   marginally above chance
    |z| >= 2.0   observed 20    expected-by-chance   17.7   nothing here
    |z| >= 2.5   observed 5     expected-by-chance    4.8   nothing here
    |z| >= 3.0   observed 3     expected-by-chance    1.1   ABOVE CHANCE -- worth a look

  The expected column is not a caveat. It is the comparison. A cell is only
  evidence if the observed count at its z exceeds the expected count, and then
  only the excess is evidence -- not that cell in particular.

  ### SIGN ASYMMETRY (direction, which the count test cannot see)

  FWD   134 cells   48 positive / 86 negative   mean z -0.38   sign test p=0.001
         pin_rlm            n=  2  mean z -1.14
         rlm_ratio          n=  4  mean z -1.02
         pin_move           n= 13  mean z -0.86
         money_delta        n=  5  mean z +0.28
         pin_value          n=  8  mean z +0.34
         consensus_gap      n= 13  mean z +0.53

  FIT   255 cells   151 positive / 104 negative   mean z +0.07   sign test p=0.004
         consensus_gap      n= 27  mean z -0.43
         money_moving       n= 30  mean z -0.42
         money_delta        n= 17  mean z -0.12
         money_level        n= 38  mean z +0.45
         rlm_ratio          n= 12  mean z +0.48
         pin_rlm            n= 12  mean z +0.68

  Read the two mean-z lines together. Noise is 0 and 0. Overfit-then-failed is
  positive fit and 0 forward. Positive fit and NEGATIVE forward is a third thing,
  and the cells are not independent of each other (same games, nested slices), so
  the p-value above is optimistic. Treat it as a question, not a result.

  ### FORWARD (out of sample -- evidence)  (134 cells)

  sport signal                 cp     mkt       slice             W-L   hit%  base%   edge    ROI%      z
  cbb   pin_move               close  total     pin $1-2k       31-54   36.5   49.6  -13.1   -29.9  -2.42
  cbb   pin_move               close  total     3k+ bets        10-24   29.4   50.0  -20.6   -43.4  -2.40
  cbb   money_level            close  moneyline <1k bets         25-5   83.3   62.7   20.7    12.5   2.34
  cbb   pin_move               close  total     all             55-83   39.9   49.6   -9.7   -23.6  -2.29
  cbb   money_level            close  total     3k+ bets        18-32   36.0   51.6  -15.6   -31.2  -2.21
  cbb   pin_value              close  spread    1-3k bets       46-28   62.2   49.4   12.7    15.7   2.20
  cbb   sharp_gap              close  total     pin limit <$    23-38   37.7   50.3  -12.6   -28.0  -1.97
  cbb   sharp_gap              close  moneyline pin $2k+        30-53   36.1   46.5  -10.3   -26.1  -1.89
  cbb   money_moving           close  total     pin limit <$    26-40   39.4   50.3  -10.9   -24.8  -1.77
  cbb   sharp_gap              close  total     all            95-119   44.4   50.4   -6.0   -15.1  -1.76
  cbb   follow_move            early  spread    all             39-54   41.9   50.8   -8.8   -19.1  -1.71
  cbb   money_moving           close  total     all            98-122   44.5   50.3   -5.8   -14.9  -1.71

  ### FIT (in sample -- hypotheses only)  (255 cells)

  sport signal                 cp     mkt       slice             W-L   hit%  base%   edge    ROI%      z
  cbb   consensus_gap          close  moneyline all           140-272   34.0   44.9  -10.9   -18.8  -4.46
  cbb   consensus_gap          close  moneyline 1-3k bets      88-162   35.2   46.3  -11.1   -21.3  -3.52
  cbb   consensus_gap          early  moneyline all            89-164   35.2   44.7   -9.6   -20.0  -3.05
  cbb   consensus_gap          early  moneyline <1k bets       75-138   35.2   45.3  -10.1   -24.2  -2.96
  cbb   money_level            close  moneyline 1-3k bets      263-80   76.7   70.4    6.3     0.3   2.55
  cbb   rlm_quiet              close  total     pin $1-2k       24-44   35.3   50.1  -14.8   -32.4  -2.44
  cbb   pin_value              close  total     pin limit <$    85-58   59.4   49.9    9.5    12.9   2.28
  cbb   consensus_gap          close  moneyline pin $2k+        52-80   39.4   48.9   -9.5   -10.2  -2.18
  cbb   consensus_gap          close  moneyline <1k bets        21-54   28.0   40.3  -12.3   -38.4  -2.17
  cbb   money_level            close  moneyline pin $1-2k       80-52   60.6   69.1   -8.5   -14.4  -2.11
  cbb   pin_value              close  total     <1k bets        26-13   66.7   49.9   16.8    26.9   2.09
  cbb   sharp_gap              close  moneyline 1-3k bets     110-201   35.4   41.1   -5.7   -16.0  -2.05

## 3. OPEN QUESTIONS, AGED

  [    3d] Is the low-limit CBB totals cell real or is it where this dataset's noise concentrates?
           why: pin_value reads 60.4% there vs 47.7% at high limits (totals only, spreads flat), and pin_rlm and rlm_ratio are ALSO better under $1k. The same corner keeps reappearing across unrelated signals. Either thin markets where Pinnacle has not done the work and FanDuel copies a lazy number, or noise. They look identical and it has never survived forward.
           next: forward-only test; the plausibility guard already flags it  (owner: unassigned)

  [    3d] Does cross-book BREADTH (how many books move within an interval) predict anything, given ordering is unmeasurable?
           why: the only survivable form of the steam idea. Data is in hand.
           next: build the breadth measurement  (owner: unassigned)

  [    3d] Does the volume/attention thesis hold in NFL, where public bias is stronger?
           why: it inverted in CBB, but NFL's n=43 cannot answer it either way. If the thesis is right anywhere it is probably NFL.
           next: most of a season of forward data  (owner: unassigned)

  [    3d] Does rlm_ratio's lift over follow_move on totals (+8.1 pts, ROI -13.1 to +2.6, n=252, z=+2.03) survive forward?
           why: the best-posed result the project has produced, because it is measured against the right denominator -- the parent signal on the same games, not a market base rate. pin_rlm shows the same direction on totals (+5.3 pts, ROI -9.2 to +1.3), which is weak support and not independent of it. FORWARD, 2026-11-22, once the date-field bug was fixed: lift +12.5 pts, ROI -34.8 to -11.0, n=28, z=+1.10. Direction reproduces out of sample. n=28 and z=1.10 are not evidence, but this is the FIRST thing in this project whose direction has held fit-to-forward at all, and note the parent is badly negative forward (34.0%) so part of the lift is the parent being bad.
           next: forward only, let n grow. Do not re-cut it in-sample. Watch whether the lift survives the parent improving.  (owner: unassigned)

  [    3d] Why does rlm_ratio hold forward while rlm_quiet gets worse, when both are Justin's same reverse-movement idea?
           why: they are both filters on follow_move and they split cleanly. rlm_ratio (minority tickets + money share at >=1.2x the ticket share + line confirms) forward lift +12.5 on totals. rlm_quiet (minority tickets AND minority money + line confirms) forward lift -18.2 on the same market. The difference between them is the money ratio: rlm_ratio requires the money to be disproportionately heavy on that side, rlm_quiet requires it to be light. Same line confirmation, opposite money condition, opposite result.
           next: this is a mechanism question, not a data-cut question. What kind of account moves a number while leaving a light money share behind?  (owner: unassigned)

  [    3d] Should the scorecard's signal-PAIR rows be dropped for pairs that agree 100% of the time?
           why: the pair rows exist on the theory that evidence combines. For follow_move+rlm_quiet, which agree 523/523, nothing combines -- the pair row is the child row with a different name, and both appeared in the forward anomaly list as separate cells with identical 24-61 records.
           next: decide whether to drop them or label them nested; either way the anomaly scan already excludes pairs  (owner: unassigned)

  [    3d] For each of the 4 live signals: what mechanism does it trade against, documented OUTSIDE our archive?
           why: a correlation with no mechanism is a hypothesis. The Pinnacle limit/news research was 5 minutes of outside reading and produced two register items. Nothing has been read that way about the other signals.
           next: one signal per week of outside reading  (owner: unassigned)

  [    3d] Does an independent sharp source systematically disagree with follow_move after a number has already travelled?
           why: 2026-11-22, Everson/Prime named sharp action on Saints +11.5 and Raiders +10 -- both the OPPOSITE side from our lean, and in both cases our lean came from follow_move chasing a 1-2 point move that had already happened. follow_move is our worst forward signal, mean z -0.76, +0.22 fit to negative forward. The same source CONFIRMED us where the move was still live: sharps took Bucs at +6.5/+5.5 (Pinnacle has since gone to 3.5) and Eagles at +4.5 (now 3.5). Two confirmations where we were early, two contradictions where we were late. That is a mechanism for the follow_move forward number, not a coincidence.
           next: log Everson's weekly post against our follow_move calls for the rest of the season. n will be tiny; it is a mechanism check, not a signal test.  (owner: unassigned)

  [    2d] Why did price gating come back after being closed with evidence, and what stops the next recurrence?
           why: On 2026-11-22 the whole NFL card was ranked by FanDuel-vs-Pinnacle edge, two artifacts were built around it, and it was described as 'the only column that does not depend on a signal record'. Price gating is in the brain doc's CLOSED list -- the gap is non-monotonic, being a point WORSE than Pinnacle was the best bucket, and it had already been removed once for cutting plays with no support. Justin caught it the second time too, in nearly the same words. CLAUDE.md lists the closed items but a closed item is a fact to recall, not a check that fires. Day-one evidence was mixed: the four signal-only plays that price gating had excluded went 2-2, and the biggest price play (ARI +15.5, $100k limit) lost.
           next: consider making audit.py assert that the current ranking rule is not one of the closed ones -- a closed item that only lives in prose gets re-derived  (owner: unassigned)

  [    1d] Does line_reversed hold forward as n grows? It is the only path feature on both sides of the holdout in both sports.
           why: CBB fit totals 58.2% n=402 ROI +11.3 (z=+3.43); CBB FORWARD moneylines 55.2% n=192 ROI +17.0 (z=+1.85); NFL fit moneylines z=+2.05. A number that reverses at least once behaving differently from one that travels straight is also mechanically plausible -- a reversal means two opposing flows rather than one, so the close is a contested number rather than a settled one. 44 comparisons were made and ~2.2 were expected at |z|>=2, and the cells are not independent.
           next: forward only, let n grow. Do not promote to a SIGNAL yet -- that moves the holdout.  (owner: unassigned)

## 5. FILTER LIFT -- signals that are subsets of other signals

  rlm_quiet and rlm_ratio fire only where follow_move also fires, 100% of the
  time, by construction. pin_rlm sits 87% inside pin_move. They are filters, so
  the comparison that matters is against the PARENT on the same games, not
  against a market base rate. Scored against a base rate they look unremarkable.

  ### CBB

  does rlm_quiet improve on its parent follow_move?
    spread    all         with  48.8% n=129 ROI   -5.8   without  47.9% n=536 ROI   -8.6   lift   +0.9pt /   +2.8ROI  z +0.18
    spread    all    FWD  with  45.0% n= 40 ROI  -12.7   without  47.0% n=117 ROI  -10.0   lift   -2.0pt /   -2.8ROI  z -0.22
    spread    1-3k        with  50.0% n= 80 ROI   -3.4   without  47.9% n=353 ROI   -8.7   lift   +2.1pt /   +5.3ROI  z +0.34
    spread    3k+         with  54.1% n= 37 ROI   +4.1   without  46.5% n=101 ROI  -11.6   lift   +7.5pt /  +15.7ROI  z +0.78
    total     all         with  44.1% n=281 ROI  -15.2   without  50.7% n=523 ROI   -3.2   lift   -6.5pt /  -12.0ROI  z -1.77
    total     all    FWD  with  41.5% n= 94 ROI  -19.8   without  46.2% n=117 ROI  -12.0   lift   -4.7pt /   -7.8ROI  z -0.68
    total     <1k         with  56.8% n= 37 ROI   +9.0   without  43.5% n= 69 ROI  -16.7   lift  +13.3pt /  +25.6ROI  z +1.30
    total     1-3k        with  42.9% n=182 ROI  -17.7   without  51.9% n=335 ROI   -0.8   lift   -9.1pt /  -16.9ROI  z -1.97
    total     1-3k   FWD  with  37.7% n= 61 ROI  -27.0   without  50.0% n= 76 ROI   -4.8   lift  -12.3pt /  -22.2ROI  z -1.44
    total     3k+         with  40.3% n= 62 ROI  -22.2   without  51.3% n=119 ROI   -2.2   lift  -10.9pt /  -20.0ROI  z -1.40
    moneyline all         with  32.0% n=259 ROI   -7.5   without  71.0% n=458 ROI   -5.4   lift  -38.9pt /   -2.1ROI  z -10.11   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline all    FWD  with  32.0% n= 97 ROI  -12.5   without  62.7% n=102 ROI   -6.4   lift  -30.8pt /   -6.1ROI  z -4.35   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline <1k         with  21.4% n= 28 ROI  -41.8   without  70.4% n= 81 ROI  -11.4   lift  -48.9pt /  -30.3ROI  z -4.52   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k        with  32.4% n=170 ROI   -2.0   without  72.7% n=267 ROI   -5.0   lift  -40.3pt /   +3.0ROI  z -8.30   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k   FWD  with  37.5% n= 64 ROI   +6.2   without  57.1% n= 63 ROI  -12.1   lift  -19.6pt /  +18.3ROI  z -2.22   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 3k+         with  36.1% n= 61 ROI   -7.3   without  67.3% n=110 ROI   -2.2   lift  -31.2pt /   -5.1ROI  z -3.94   [ML: read ROI only, hit lift is a dog/fav artifact]

  does rlm_ratio improve on its parent follow_move?
    spread    all         with  50.0% n= 96 ROI   -4.7   without  47.8% n=569 ROI   -8.6   lift   +2.2pt /   +3.9ROI  z +0.40
    spread    1-3k        with  47.5% n= 59 ROI   -9.5   without  48.4% n=374 ROI   -7.4   lift   -0.9pt /   -2.1ROI  z -0.13
    spread    3k+         with  53.8% n= 26 ROI   +2.9   without  47.3% n=112 ROI   -9.8   lift   +6.5pt /  +12.7ROI  z +0.60
    total     all         with  51.2% n=291 ROI   -1.9   without  46.8% n=513 ROI  -10.6   lift   +4.4pt /   +8.7ROI  z +1.20
    total     all    FWD  with  40.3% n= 67 ROI  -22.6   without  45.8% n=144 ROI  -12.1   lift   -5.5pt /  -10.5ROI  z -0.75
    total     <1k         with  58.5% n= 41 ROI  +12.5   without  41.5% n= 65 ROI  -20.5   lift  +17.0pt /  +33.0ROI  z +1.71
    total     1-3k        with  49.2% n=191 ROI   -5.8   without  48.5% n=326 ROI   -7.4   lift   +0.7pt /   +1.6ROI  z +0.16
    total     1-3k   FWD  with  35.0% n= 40 ROI  -32.8   without  48.5% n= 97 ROI   -7.2   lift  -13.5pt /  -25.6ROI  z -1.44
    total     3k+         with  52.5% n= 59 ROI   +0.8   without  45.1% n=122 ROI  -13.8   lift   +7.5pt /  +14.5ROI  z +0.94
    moneyline all         with  30.7% n=179 ROI  -11.5   without  65.6% n=538 ROI   -4.4   lift  -34.9pt /   -7.1ROI  z -8.16   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline all    FWD  with  29.0% n= 62 ROI  -28.8   without  56.2% n=137 ROI   -0.5   lift  -27.2pt /  -28.2ROI  z -3.55   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k        with  28.7% n=122 ROI  -14.2   without  67.9% n=315 ROI   +0.2   lift  -39.2pt /  -14.4ROI  z -7.43   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k   FWD  with  31.8% n= 44 ROI  -21.4   without  55.4% n= 83 ROI   +7.0   lift  -23.6pt /  -28.4ROI  z -2.54   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 3k+         with  39.5% n= 38 ROI   +9.6   without  60.9% n=133 ROI   -7.9   lift  -21.4pt /  +17.5ROI  z -2.35   [ML: read ROI only, hit lift is a dog/fav artifact]

  does pin_rlm improve on its parent pin_move?
    spread    all         with  52.8% n= 53 ROI   +0.9   without  47.2% n=462 ROI   -9.9   lift   +5.6pt /  +10.8ROI  z +0.78
    spread    1-3k        with  54.5% n= 33 ROI   +4.1   without  47.6% n=296 ROI   -9.0   lift   +6.9pt /  +13.2ROI  z +0.75
    total     all         with  50.6% n=180 ROI   -3.1   without  47.1% n=346 ROI   -9.9   lift   +3.4pt /   +6.8ROI  z +0.75
    total     all    FWD  with  35.9% n= 39 ROI  -31.1   without  41.4% n= 99 ROI  -20.6   lift   -5.5pt /  -10.5ROI  z -0.60
    total     <1k         with  61.3% n= 31 ROI  +17.5   without  51.3% n= 39 ROI   -1.6   lift  +10.0pt /  +19.2ROI  z +0.84
    total     1-3k        with  50.0% n=108 ROI   -4.3   without  47.6% n=227 ROI   -9.1   lift   +2.4pt /   +4.8ROI  z +0.41
    total     3k+         with  43.9% n= 41 ROI  -15.6   without  43.8% n= 80 ROI  -16.3   lift   +0.2pt /   +0.7ROI  z +0.02
    moneyline all         with  34.7% n=101 ROI   +8.4   without  58.5% n=195 ROI   +0.6   lift  -23.8pt /   +7.8ROI  z -3.88   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline all    FWD  with  29.6% n= 27 ROI  -25.0   without  60.3% n= 63 ROI  +18.0   lift  -30.7pt /  -42.9ROI  z -2.67   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k        with  38.3% n= 60 ROI  +23.3   without  59.0% n=105 ROI   +3.6   lift  -20.7pt /  +19.7ROI  z -2.56   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 3k+         with  29.0% n= 31 ROI  -16.4   without  59.1% n= 66 ROI   +0.3   lift  -30.1pt /  -16.7ROI  z -2.76   [ML: read ROI only, hit lift is a dog/fav artifact]

  ### NFL

## 6. RECORDED FEATURES, SCORED AS CONDITIONERS

  Splitting calls already made. No call changes, so the holdout does NOT move.
  This is what 'RECORDED and consumed by nothing' was costing.

  45 comparisons made. Chance alone gives ~2.2 at |z|>=2.0 and
  ~4.5 at |z|>=1.65. Read every row below against those two numbers.

  sport per  feature        mkt                         WITH                WITHOUT      z
  nfl   fit  deep_series    spread         36.9% n=179 -30.0       73.5% n=34 +36.8  -3.96
  cbb   fit  line_reversed  total          58.2% n=402 +11.3      49.1% n=3098 -6.2   3.43
  cbb   fit  lim_slashed    spread          72.9% n=48 +41.5      49.5% n=2990 -6.1   3.22
  nfl   fit  mny_crossed    moneyline       21.1% n=38 -55.8      48.4% n=223 -15.8  -3.14
  cbb   fwd  mny_gave_back  moneyline      42.3% n=421 -20.9       52.2% n=464 +9.2  -2.94
  cbb   fit  line_ineff     moneyline      43.0% n=1022 -1.7      48.7% n=1192 +0.4  -2.68
  cbb   fit  lim_slashed    total           65.7% n=67 +25.6      49.9% n=3433 -4.7   2.56
  nfl   fit  line_ineff     moneyline      40.7% n=209 -30.9       59.6% n=52 +15.6  -2.46
  nfl   fit  mny_crossed    total           59.6% n=89 +13.4      43.4% n=113 -16.9   2.28
  cbb   fit  mny_crossed    total          49.3% n=2821 -5.9       53.9% n=679 +3.1  -2.17
  nfl   fit  line_reversed  moneyline       50.4% n=139 -8.2      37.7% n=122 -37.0   2.05
  cbb   fit  mny_gave_back  spread         51.9% n=1157 -1.1      48.5% n=1881 -8.0   1.82
  nfl   fwd  line_ineff     total           76.0% n=25 +45.4        56.6% n=53 +8.1   1.65
  nfl   fit  key_crossed    spread          31.7% n=41 -38.9      45.3% n=172 -14.7  -1.59
  nfl   fit  mny_gave_back  moneyline        51.1% n=90 +7.8      40.9% n=171 -37.1   1.57
  cbb   fwd  line_ineff     moneyline       44.4% n=374 -9.6       49.7% n=511 -1.8  -1.57
  cbb   fit  line_ineff     total           52.9% n=681 +1.1      49.5% n=2819 -5.4   1.57
  cbb   fit  line_reversed  moneyline       47.9% n=941 +9.4      44.6% n=1273 -7.9   1.54
  nfl   fit  mny_gave_back  total           41.8% n=55 -20.1       53.7% n=147 +2.6  -1.51
  cbb   fwd  mny_crossed    moneyline       49.3% n=566 -3.6       44.2% n=319 -7.7   1.46
  cbb   fit  mny_gave_back  moneyline       44.3% n=902 -3.4      47.2% n=1312 +1.5  -1.31
  cbb   fit  mny_gave_back  total          49.3% n=1954 -5.8      51.3% n=1546 -2.1  -1.18
  nfl   fwd  mny_gave_back  total            55.9% n=34 +8.1       68.2% n=44 +29.3  -1.11
  nfl   fit  mny_crossed    spread          33.3% n=27 -37.2      44.1% n=186 -16.8  -1.06
  nfl   fwd  deep_series    moneyline        46.9% n=32 +9.7       35.3% n=51 -38.9   1.05
  cbb   fit  mny_crossed    spread         49.3% n=2111 -6.6       51.1% n=927 -2.5  -0.95
  cbb   fit  line_ineff     spread          48.5% n=715 -8.0      50.2% n=2323 -4.6  -0.80
  cbb   fwd  line_reversed  spread          44.2% n=95 -15.7       48.2% n=710 -8.7  -0.73
  nfl   fwd  deep_series    total           58.8% n=34 +12.1       65.9% n=44 +26.2  -0.64
  nfl   fit  deep_series    moneyline      43.6% n=218 -23.0       48.8% n=43 -14.7  -0.63
  cbb   fit  lim_slashed    moneyline        41.5% n=41 -8.5      46.1% n=2173 -0.4  -0.59
  nfl   fit  line_ineff     total            53.4% n=58 +1.6       49.3% n=144 -5.7   0.53
  cbb   fwd  line_reversed  total          43.1% n=160 -18.2     45.2% n=1021 -13.6  -0.48
  cbb   fwd  mny_gave_back  spread         45.8% n=131 -13.3       48.1% n=674 -8.8  -0.48
  cbb   fwd  line_ineff     spread          48.9% n=237 -6.9      47.2% n=568 -10.6   0.46
  cbb   fwd  mny_gave_back  total          44.3% n=652 -15.3      45.6% n=529 -12.8  -0.42
  nfl   fit  mny_gave_back  spread          44.4% n=72 -15.4      41.8% n=141 -21.4   0.36
  cbb   fwd  line_ineff     total          44.1% n=347 -15.8      45.2% n=834 -13.5  -0.35
  nfl   fwd  deep_series    spread           46.7% n=30 -8.6       43.2% n=44 -17.1   0.30
  nfl   fit  deep_series    total           50.8% n=177 -2.8        48.0% n=25 -8.8   0.27
  cbb   fit  mny_crossed    moneyline      46.2% n=1458 -0.9       45.6% n=756 +0.2   0.27
  cbb   fwd  mny_crossed    total         44.8% n=1025 -14.4      45.5% n=156 -13.0  -0.17
  cbb   fit  line_reversed  spread          50.2% n=233 -5.4      49.8% n=2805 -5.4   0.12
  cbb   fwd  line_reversed  moneyline       47.6% n=334 -4.6       47.4% n=551 -5.4   0.07
  cbb   fwd  mny_crossed    spread          47.7% n=484 -9.6       47.7% n=321 -9.4   0.02

  FIT is a hypothesis, FORWARD is evidence. A feature that only appears in FIT
  rows has not been tested; one that holds in both, and across sports, is the
  project's own standard for believing anything.

  11 at |z|>=2.0 against ~2.2 expected. Above chance — worth a look.
  ROI is the currency, not hit rate: money_level hit 73.4% and lost 14.87 units.

## 4. HOLDOUT AND FORWARD SAMPLE

  cbb: holdout from 2026-11-21 (4d ago)
         684 fit games, 234 forward games

  nfl: holdout from 2026-11-21 (4d ago)
         43 fit games, 12 forward games
         forward sample is 12 games. Nothing measured forward can
         distinguish a 55% signal from a 50% one yet. Do not promote on it.

------------------------------------------------------------------------------
The standing rule: search the project docs before investigating anything here.
An hour went on a question already answered 0-for-17 in propwatch-line-value-state.
------------------------------------------------------------------------------
```
