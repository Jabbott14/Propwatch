# Propwatch audit

Generated 2026-11-27 by `audit.py`. Nobody asked for it; that is the point.

```
==============================================================================
PROPWATCH AUDIT   2026-11-27
==============================================================================

Nobody asked for this. That is the point -- the knowledge base only gets read when
a session opens it, and the guards only fire once a measurement is already wrong.

## 0. IS THE DATA STILL ARRIVING?

  NFL collector    last    0.0h ago  (2026-11-27T12:41:58+00:00)
  CBB collector    last    0.1h ago  (2026-11-27T12:35:39+00:00)
  NCAAF collector  last    0.3h ago  (2026-11-27T12:24:57+00:00)
  NFL grader       last    4.0h ago  (2026-11-27T08:46:11+00:00)
  CBB grader       last    3.6h ago  (2026-11-27T09:08:20+00:00)

  data             all sources OK as of 2026-11-27T12:41:44Z
  cbb              all sources OK as of 2026-11-27T12:35:33Z
  ncaaf            all sources OK as of 2026-11-27T12:24:50Z

  all feeds current.

## 1. RECORDED AND CONSUMED BY NOTHING

  3 RECORDED (computed, graded by nothing) | 9 OPEN (not built)

  [RECORDED]       5d  signals that are strict SUBSETS of other signals are graded against the wrong thing
             audit.py section 5 computes lift vs parent; the scorecard still grades vs base rate
             note: audit.py section 5 computes filter lift vs parent. Still RECORDED because the live SCORECARD continues to grade rlm_quiet/rlm_ratio/rlm/pin_rlm against a market base rate rather than their parent, so the board a person reads still shows the wrong comparison.

  [RECORDED]       5d  retracement off the Pinnacle extreme -- a number that bottomed and climbed back is not the same as one still falling
             pin_bounce, retraced -- display only
             note: pin_bounce and pin_extreme are stored on every close row but are not yet in the audit's feature list -- the path-layer features were graded first. Next one to wire in.

  [RECORDED]       4d  the NFL collector dies silently and nothing notices
             audit.py section 0 (heartbeat) now checks it; the workflow itself is NOT fixed
             note: DEFECT. `snap` ran every ~10 min then STOPPED 2026-11-23T01:12Z -- fifteen minutes before the MIN@SF kickoff -- so that game has no closing data. Came back 10:56Z, 9.7h gap. Died again, 3h gap. Last run 14:46Z and was 7.6h cold when Monday's card was being built. CBB and NCAAF ran clean every 30 min through all of it, which is exactly why nothing looked wrong. collect.yml is cron '7 * * * *' with timeout-minutes 350, so ~6 runs overlap by design, and `continue-on-error: true` means a failing step never surfaces. Suspected cause is Actions concurrency/queue pressure on NFL Sunday (6 overlapping 5h50m snap jobs plus cbb, ncaaf and the graders), but THIS IS UNVERIFIED -- the Actions API was not reachable from the session that found it. Justin needs to read the Actions tab. A stale feed is the worst failure this project has because downstream it does not look like an error, it looks like a quiet market.

  [OPEN    ]       5d  most-bet / most-watched games are where to fade the public -- NOT standalone, but combined with other signals
             volume slice runs on all 12 signals; audit.py section 5 now reports it per filter
             note: HIS CORRECTION, 2026-11-22, and it was right. The standalone form is measured and dead: fading the public INVERTS with volume, 52.1% under 1k bets -> 47.4% at 4k+, spreads 4k+ 43.0% / -17.9% on n=114. But I then closed the whole idea on 3 of 12 signals, which is not a test of it. His words: 'maybe it isn't that easy of just fading public but looking at most bet games and fading public w other signals involved as well -- we have many other different signals too.' Re-run across all 12: n-weighted aggregate is FLAT in every market (|z| all under 1.5), so volume is not a blanket conditioner. Per-cell, 9 of 26 signal x market cells rise monotonically with volume against 4.3 expected by chance, 4 fall -- a mild excess on correlated cells. Spread and total disagree in direction for the same signal (rlm_quiet spread lift +1.3 -> +11.8 with volume; total lift -9.0 -> -22.0). STAYS OPEN: the aggregate says no, the per-cell picture is not flat, NFL cannot check it (0 forward cells at n>=30), and everything above is FIT.

  [OPEN    ]       5d  CFB limits scale differently than NFL, so raw limit comparison is wrong across sports
             raw limits still compared

  [OPEN    ]       5d  steam = many books moving at once
             breadth (books-per-interval) only -- ordering is PERMANENTLY unmeasurable, all 7 books share our snapshot timestamp
             note: data is in hand; the breadth measurement has not been built

  [OPEN    ]       5d  our own closing-line model, to price independently of the books
             needs hoopR

  [OPEN    ]       5d  Circa as a second sharp reference alongside Pinnacle
             raw/vsin_circa collected, never parsed

  [OPEN    ]       5d  record each book's OWN observed change time, not our snapshot time
             collector change, not made -- this is the only thing that would make lead-lag measurable going forward

  [OPEN    ]       5d  the BOOK'S OWN EXPOSURE -- which side the house needs. Upstream of why a number moves.
             not collected anywhere
             note: Justin shared a Patrick Everson / Prime Sportsbook post 2026-11-22 listing 'Biggest House Needs' (Lions -3.5, Panthers -2.5, Bills -16.5, Raiders +10.5, Giants +5.5) alongside sharp action and public plays. We collect tickets and money -- what BETTORS did. We have never had what the BOOK is holding. A book moves a number to balance its own book, so its liability is upstream of the move we measure; every signal in this system reads the move and infers backwards. HONEST LIMIT: this is not published as a feed. It appears in weekly columns written by people (Everson/Prime, VSIN liability reports, SuperBook). Treat it as a manual cross-check when Justin shares one, not a signal input, unless a structured source turns up. Also unresolved: Everson listed Lions -3.5 under BOTH 'Top Public Plays' and 'Biggest House Needs', which is not consistent under either reading of the term -- do not build on it until the convention is confirmed.

  [OPEN    ]       5d  'the public' is one book's clientele, not a fact about the world
             every public/fade signal reads Action Network book 69 only
             note: MATERIAL LIMIT ON THE WHOLE FADE-THE-PUBLIC THESIS, found 2026-11-22 by cross-checking Justin's Everson post. Prime listed 'Dolphins +16.5' as a top public play while our Action Network data read 60% of tickets on BUFFALO -- the opposite side. Prime listed public on Ravens +2.5 where we read 49/50, no lean at all. rlm, rlm_quiet, rlm_ratio, sharp_gap and the volume slices all define 'the public' as FanDuel's ticket split via Action Network. If two books disagree about which side the public is on, then a fade signal is fading one book's customers, and its record is a statement about that book, not about public money. Nothing in the archive can currently test this because we have only ever had one source of splits.

  [OPEN    ]       3d  name Action Network books 15, 49, 68, 71, 75
             nowhere -- only 69 (FanDuel) and 30 (opener) are identified in the codebase
             note: BLOCKING. xbook.py found that book 75 leads the market at z=+3.67 and nobody knows what book 75 is. The AN payload carries no book metadata -- no names, no books array. Identify by cross-referencing a known line at a known time against a named sportsbook, or by finding AN's book-list endpoint. Until then the strongest cross-book result in the project points at an anonymous book.

## 2. ANOMALY SCAN, WITH THE MULTIPLE-COMPARISONS DENOMINATOR

  excluded as non-independent or unscoreable:
      1649  period=all (fit+fwd re-counted)
       894  market=both (pools base rates)
       853  signal pair (derived from singles)

  independent-ish cells with >=30 decisions: 412
  z is hit rate against each cell's OWN base rate, not against break-even.
    |z| >= 1.65  observed 37    expected-by-chance   40.8   nothing here
    |z| >= 2.0   observed 16    expected-by-chance   18.7   nothing here
    |z| >= 2.5   observed 5     expected-by-chance    5.1   nothing here
    |z| >= 3.0   observed 3     expected-by-chance    1.1   ABOVE CHANCE -- worth a look

  The expected column is not a caveat. It is the comparison. A cell is only
  evidence if the observed count at its z exceeds the expected count, and then
  only the excess is evidence -- not that cell in particular.

  ### SIGN ASYMMETRY (direction, which the count test cannot see)

  FWD   157 cells   66 positive / 91 negative   mean z -0.15   sign test p=0.055
         rlm_ratio          n=  7  mean z -0.58
         pin_move           n= 15  mean z -0.43
         sharp_gap          n= 21  mean z -0.40
         money_level        n= 21  mean z +0.08
         money_delta        n=  9  mean z +0.22
         consensus_gap      n= 14  mean z +0.23

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

  ### FORWARD (out of sample -- evidence)  (157 cells)

  sport signal                 cp     mkt       slice             W-L   hit%  base%   edge    ROI%      z
  cbb   pin_value              close  spread    1-3k bets       55-35   61.1   49.1   12.0    14.0   2.28
  cbb   money_level            close  moneyline <1k bets         26-7   78.8   61.0   17.7     5.4   2.09
  cbb   consensus_gap          early  spread    all             31-20   60.8   47.4   13.4    13.6   1.91
  cbb   pin_value              close  spread    3k+ bets        16-26   38.1   52.0  -13.9   -28.5  -1.80
  cbb   follow_move            early  moneyline all            109-94   53.7   47.4    6.3     1.1   1.80
  cbb   rlm_quiet              close  moneyline pin $2k+        27-33   45.0   34.7   10.3    23.2   1.68
  cbb   follow_move            early  spread    all             55-72   43.3   50.7   -7.4   -16.4  -1.67
  cbb   consensus_gap          early  spread    <1k bets        24-16   60.0   47.2   12.8    12.5   1.62
  cbb   pin_move               close  moneyline 1-3k bets       40-33   54.8   45.4    9.4    21.4   1.61
  cbb   sharp_gap              close  moneyline pin $2k+        41-68   37.6   45.2   -7.6   -20.9  -1.59
  cbb   rlm_quiet              close  total     1-3k bets       30-47   39.0   47.9   -8.9   -24.8  -1.57
  cbb   pin_move               close  total     pin $1-2k       42-58   42.0   49.7   -7.7   -19.4  -1.54

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

  [    5d] Is the low-limit CBB totals cell real or is it where this dataset's noise concentrates?
           why: pin_value reads 60.4% there vs 47.7% at high limits (totals only, spreads flat), and pin_rlm and rlm_ratio are ALSO better under $1k. The same corner keeps reappearing across unrelated signals. Either thin markets where Pinnacle has not done the work and FanDuel copies a lazy number, or noise. They look identical and it has never survived forward.
           next: forward-only test; the plausibility guard already flags it  (owner: unassigned)

  [    5d] Does cross-book BREADTH (how many books move within an interval) predict anything, given ordering is unmeasurable?
           why: the only survivable form of the steam idea. Data is in hand.
           next: build the breadth measurement  (owner: unassigned)

  [    5d] Does the volume/attention thesis hold in NFL, where public bias is stronger?
           why: it inverted in CBB, but NFL's n=43 cannot answer it either way. If the thesis is right anywhere it is probably NFL.
           next: most of a season of forward data  (owner: unassigned)

  [    5d] Does rlm_ratio's lift over follow_move on totals (+8.1 pts, ROI -13.1 to +2.6, n=252, z=+2.03) survive forward?
           why: the best-posed result the project has produced, because it is measured against the right denominator -- the parent signal on the same games, not a market base rate. pin_rlm shows the same direction on totals (+5.3 pts, ROI -9.2 to +1.3), which is weak support and not independent of it. FORWARD, 2026-11-22, once the date-field bug was fixed: lift +12.5 pts, ROI -34.8 to -11.0, n=28, z=+1.10. Direction reproduces out of sample. n=28 and z=1.10 are not evidence, but this is the FIRST thing in this project whose direction has held fit-to-forward at all, and note the parent is badly negative forward (34.0%) so part of the lift is the parent being bad.
           next: forward only, let n grow. Do not re-cut it in-sample. Watch whether the lift survives the parent improving.  (owner: unassigned)

  [    5d] Why does rlm_ratio hold forward while rlm_quiet gets worse, when both are Justin's same reverse-movement idea?
           why: they are both filters on follow_move and they split cleanly. rlm_ratio (minority tickets + money share at >=1.2x the ticket share + line confirms) forward lift +12.5 on totals. rlm_quiet (minority tickets AND minority money + line confirms) forward lift -18.2 on the same market. The difference between them is the money ratio: rlm_ratio requires the money to be disproportionately heavy on that side, rlm_quiet requires it to be light. Same line confirmation, opposite money condition, opposite result.
           next: this is a mechanism question, not a data-cut question. What kind of account moves a number while leaving a light money share behind?  (owner: unassigned)

  [    5d] Should the scorecard's signal-PAIR rows be dropped for pairs that agree 100% of the time?
           why: the pair rows exist on the theory that evidence combines. For follow_move+rlm_quiet, which agree 523/523, nothing combines -- the pair row is the child row with a different name, and both appeared in the forward anomaly list as separate cells with identical 24-61 records.
           next: decide whether to drop them or label them nested; either way the anomaly scan already excludes pairs  (owner: unassigned)

  [    5d] For each of the 4 live signals: what mechanism does it trade against, documented OUTSIDE our archive?
           why: a correlation with no mechanism is a hypothesis. The Pinnacle limit/news research was 5 minutes of outside reading and produced two register items. Nothing has been read that way about the other signals.
           next: one signal per week of outside reading  (owner: unassigned)

  [    5d] Does an independent sharp source systematically disagree with follow_move after a number has already travelled?
           why: 2026-11-22, Everson/Prime named sharp action on Saints +11.5 and Raiders +10 -- both the OPPOSITE side from our lean, and in both cases our lean came from follow_move chasing a 1-2 point move that had already happened. follow_move is our worst forward signal, mean z -0.76, +0.22 fit to negative forward. The same source CONFIRMED us where the move was still live: sharps took Bucs at +6.5/+5.5 (Pinnacle has since gone to 3.5) and Eagles at +4.5 (now 3.5). Two confirmations where we were early, two contradictions where we were late. That is a mechanism for the follow_move forward number, not a coincidence.
           next: log Everson's weekly post against our follow_move calls for the rest of the season. n will be tiny; it is a mechanism check, not a signal test.  (owner: unassigned)

  [    4d] Why did price gating come back after being closed with evidence, and what stops the next recurrence?
           why: On 2026-11-22 the whole NFL card was ranked by FanDuel-vs-Pinnacle edge, two artifacts were built around it, and it was described as 'the only column that does not depend on a signal record'. Price gating is in the brain doc's CLOSED list -- the gap is non-monotonic, being a point WORSE than Pinnacle was the best bucket, and it had already been removed once for cutting plays with no support. Justin caught it the second time too, in nearly the same words. CLAUDE.md lists the closed items but a closed item is a fact to recall, not a check that fires. Day-one evidence was mixed: the four signal-only plays that price gating had excluded went 2-2, and the biggest price play (ARI +15.5, $100k limit) lost.
           next: consider making audit.py assert that the current ranking rule is not one of the closed ones -- a closed item that only lives in prose gets re-derived  (owner: unassigned)

  [    3d] Does line_reversed hold forward as n grows? It is the only path feature on both sides of the holdout in both sports.
           why: CBB fit totals 58.2% n=402 ROI +11.3 (z=+3.43); CBB FORWARD moneylines 55.2% n=192 ROI +17.0 (z=+1.85); NFL fit moneylines z=+2.05. A number that reverses at least once behaving differently from one that travels straight is also mechanically plausible -- a reversal means two opposing flows rather than one, so the close is a contested number rather than a settled one. 44 comparisons were made and ~2.2 were expected at |z|>=2, and the cells are not independent.
           next: forward only, let n grow. Do not promote to a SIGNAL yet -- that moves the holdout.  (owner: unassigned)

## 5. FILTER LIFT -- signals that are subsets of other signals

  rlm_quiet and rlm_ratio fire only where follow_move also fires, 100% of the
  time, by construction. pin_rlm sits 87% inside pin_move. They are filters, so
  the comparison that matters is against the PARENT on the same games, not
  against a market base rate. Scored against a base rate they look unremarkable.

  ### CBB

  does rlm_quiet improve on its parent follow_move?
    spread    all         with  49.0% n=145 ROI   -5.6   without  48.2% n=570 ROI   -8.1   lift   +0.7pt /   +2.5ROI  z +0.15
    spread    all    FWD  with  46.4% n= 56 ROI  -10.2   without  48.3% n=151 ROI   -7.8   lift   -1.9pt /   -2.5ROI  z -0.25
    spread    1-3k        with  50.0% n= 86 ROI   -3.4   without  48.2% n=371 ROI   -8.0   lift   +1.8pt /   +4.6ROI  z +0.29
    spread    1-3k   FWD  with  44.8% n= 29 ROI  -12.6   without  45.7% n= 94 ROI  -12.8   lift   -0.9pt /   +0.2ROI  z -0.09
    spread    3k+         with  53.2% n= 47 ROI   +2.3   without  47.4% n=114 ROI  -10.1   lift   +5.8pt /  +12.5ROI  z +0.67
    total     all         with  44.3% n=318 ROI  -14.9   without  51.9% n=553 ROI   -0.9   lift   -7.6pt /  -14.0ROI  z -2.15
    total     all    FWD  with  42.7% n=131 ROI  -17.6   without  51.7% n=147 ROI   -1.3   lift   -9.0pt /  -16.3ROI  z -1.49
    total     <1k         with  57.9% n= 38 ROI  +11.1   without  43.8% n= 73 ROI  -16.0   lift  +14.1pt /  +27.1ROI  z +1.41
    total     1-3k        with  42.9% n=198 ROI  -17.6   without  52.7% n=349 ROI   +0.7   lift   -9.8pt /  -18.3ROI  z -2.20
    total     1-3k   FWD  with  39.0% n= 77 ROI  -24.8   without  53.3% n= 90 ROI   +1.7   lift  -14.4pt /  -26.5ROI  z -1.86
    total     3k+         with  41.5% n= 82 ROI  -20.2   without  54.2% n=131 ROI   +3.5   lift  -12.7pt /  -23.6ROI  z -1.81
    total     3k+    FWD  with  46.2% n= 39 ROI  -11.0   without  47.4% n= 38 ROI   -9.2   lift   -1.2pt /   -1.8ROI  z -0.11
    moneyline all         with  33.6% n=292 ROI   -4.9   without  70.0% n=490 ROI   -6.6   lift  -36.4pt /   +1.7ROI  z -9.94   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline all    FWD  with  35.4% n=130 ROI   -5.3   without  61.2% n=134 ROI  -10.5   lift  -25.8pt /   +5.3ROI  z -4.19   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline <1k         with  24.1% n= 29 ROI  -36.7   without  69.0% n= 84 ROI  -13.3   lift  -44.9pt /  -23.3ROI  z -4.22   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k        with  33.0% n=185 ROI   +0.0   without  71.8% n=280 ROI   -6.2   lift  -38.8pt /   +6.3ROI  z -8.26   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k   FWD  with  38.0% n= 79 ROI   +9.4   without  56.6% n= 76 ROI  -15.5   lift  -18.6pt /  +25.0ROI  z -2.32   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 3k+         with  38.5% n= 78 ROI   -4.8   without  66.7% n=126 ROI   -3.1   lift  -28.2pt /   -1.7ROI  z -3.94   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 3k+    FWD  with  37.5% n= 40 ROI  -13.4   without  70.7% n= 41 ROI   +4.6   lift  -33.2pt /  -18.0ROI  z -3.00   [ML: read ROI only, hit lift is a dog/fav artifact]

  does rlm_ratio improve on its parent follow_move?
    spread    all         with  50.0% n=110 ROI   -4.8   without  48.1% n=605 ROI   -8.1   lift   +1.9pt /   +3.3ROI  z +0.37
    spread    all    FWD  with  53.8% n= 26 ROI   +2.0   without  47.0% n=181 ROI   -9.9   lift   +6.9pt /  +11.9ROI  z +0.66
    spread    1-3k        with  50.0% n= 66 ROI   -4.8   without  48.3% n=391 ROI   -7.5   lift   +1.7pt /   +2.8ROI  z +0.25
    spread    3k+         with  50.0% n= 32 ROI   -4.5   without  48.8% n=129 ROI   -7.0   lift   +1.2pt /   +2.5ROI  z +0.12
    total     all         with  51.4% n=321 ROI   -1.5   without  47.8% n=550 ROI   -8.6   lift   +3.6pt /   +7.0ROI  z +1.02
    total     all    FWD  with  44.3% n= 97 ROI  -15.0   without  49.2% n=181 ROI   -5.8   lift   -4.8pt /   -9.3ROI  z -0.77
    total     <1k         with  58.5% n= 41 ROI  +12.5   without  42.9% n= 70 ROI  -18.0   lift  +15.7pt /  +30.5ROI  z +1.60
    total     1-3k        with  49.3% n=205 ROI   -5.7   without  49.1% n=342 ROI   -6.1   lift   +0.1pt /   +0.4ROI  z +0.03
    total     1-3k   FWD  with  38.9% n= 54 ROI  -25.4   without  50.4% n=113 ROI   -3.5   lift  -11.6pt /  -22.0ROI  z -1.40
    total     3k+         with  53.3% n= 75 ROI   +2.2   without  47.1% n=138 ROI   -9.9   lift   +6.2pt /  +12.0ROI  z +0.87
    total     3k+    FWD  with  50.0% n= 30 ROI   -4.0   without  44.7% n= 47 ROI  -14.1   lift   +5.3pt /  +10.1ROI  z +0.46
    moneyline all         with  30.9% n=204 ROI  -12.0   without  65.4% n=578 ROI   -3.9   lift  -34.5pt /   -8.1ROI  z -8.55   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline all    FWD  with  29.9% n= 87 ROI  -24.8   without  57.6% n=177 ROI   +0.4   lift  -27.7pt /  -25.2ROI  z -4.24   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k        with  29.6% n=135 ROI  -11.5   without  67.3% n=330 ROI   -0.6   lift  -37.6pt /  -10.9ROI  z -7.43   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k   FWD  with  33.3% n= 57 ROI  -13.4   without  55.1% n= 98 ROI   +3.3   lift  -21.8pt /  -16.7ROI  z -2.62   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 3k+         with  35.4% n= 48 ROI   -4.1   without  62.2% n=156 ROI   -3.6   lift  -26.8pt /   -0.5ROI  z -3.27   [ML: read ROI only, hit lift is a dog/fav artifact]

  does pin_rlm improve on its parent pin_move?
    spread    all         with  51.7% n= 60 ROI   -1.3   without  47.2% n=494 ROI   -9.9   lift   +4.5pt /   +8.6ROI  z +0.66
    spread    1-3k        with  55.6% n= 36 ROI   +6.1   without  48.2% n=313 ROI   -7.9   lift   +7.3pt /  +14.0ROI  z +0.83
    total     all         with  52.8% n=195 ROI   +1.2   without  48.1% n=370 ROI   -8.0   lift   +4.7pt /   +9.2ROI  z +1.07
    total     all    FWD  with  48.1% n= 54 ROI   -7.8   without  45.5% n=123 ROI  -12.8   lift   +2.6pt /   +5.0ROI  z +0.32
    total     <1k         with  62.5% n= 32 ROI  +19.8   without  52.4% n= 42 ROI   +0.4   lift  +10.1pt /  +19.4ROI  z +0.87
    total     1-3k        with  50.9% n=114 ROI   -2.6   without  48.3% n=240 ROI   -7.6   lift   +2.5pt /   +5.0ROI  z +0.45
    total     1-3k   FWD  with  37.9% n= 29 ROI  -27.1   without  46.8% n= 77 ROI  -10.4   lift   -8.8pt /  -16.7ROI  z -0.82
    total     3k+         with  51.0% n= 49 ROI   -2.2   without  45.5% n= 88 ROI  -13.1   lift   +5.6pt /  +10.9ROI  z +0.63
    moneyline all         with  35.7% n=112 ROI   +8.0   without  57.9% n=216 ROI   +1.5   lift  -22.2pt /   +6.6ROI  z -3.81   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline all    FWD  with  34.2% n= 38 ROI  -16.3   without  58.3% n= 84 ROI  +15.9   lift  -24.1pt /  -32.2ROI  z -2.47   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k        with  39.7% n= 68 ROI  +22.2   without  59.6% n=114 ROI   +7.1   lift  -19.9pt /  +15.1ROI  z -2.61   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k   FWD  with  40.7% n= 27 ROI   +1.2   without  63.0% n= 46 ROI  +33.3   lift  -22.3pt /  -32.1ROI  z -1.85   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 3k+         with  30.3% n= 33 ROI  -14.3   without  57.1% n= 77 ROI   -1.4   lift  -26.8pt /  -12.9ROI  z -2.58   [ML: read ROI only, hit lift is a dog/fav artifact]

  ### NFL

## 6. RECORDED FEATURES, SCORED AS CONDITIONERS

  Splitting calls already made. No call changes, so the holdout does NOT move.
  This is what 'RECORDED and consumed by nothing' was costing.

  47 comparisons made. Chance alone gives ~2.4 at |z|>=2.0 and
  ~4.7 at |z|>=1.65. Read every row below against those two numbers.

  sport per  feature        mkt                         WITH                WITHOUT      z
  nfl   fit  deep_series    spread         36.9% n=179 -30.0       73.5% n=34 +36.8  -3.96
  cbb   fit  line_reversed  total          58.2% n=402 +11.3      49.1% n=3098 -6.2   3.43
  cbb   fwd  mny_gave_back  moneyline      42.6% n=564 -17.7       52.1% n=630 +6.9  -3.29
  cbb   fit  lim_slashed    spread          72.9% n=48 +41.5      49.5% n=2990 -6.1   3.22
  nfl   fit  mny_crossed    moneyline       21.1% n=38 -55.8      48.4% n=223 -15.8  -3.14
  cbb   fit  line_ineff     moneyline      43.0% n=1022 -1.7      48.7% n=1192 +0.4  -2.68
  cbb   fit  lim_slashed    total           65.7% n=67 +25.6      49.9% n=3433 -4.7   2.56
  nfl   fit  line_ineff     moneyline      40.7% n=209 -30.9       59.6% n=52 +15.6  -2.46
  nfl   fit  mny_crossed    total           59.6% n=89 +13.4      43.4% n=113 -16.9   2.28
  cbb   fit  mny_crossed    total          49.3% n=2821 -5.9       53.9% n=679 +3.1  -2.17
  nfl   fit  line_reversed  moneyline       50.4% n=139 -8.2      37.7% n=122 -37.0   2.05
  nfl   fwd  mny_crossed    spread          46.7% n=60 -10.1       24.1% n=29 -52.5   2.04
  cbb   fit  mny_gave_back  spread         51.9% n=1157 -1.1      48.5% n=1881 -8.0   1.82
  nfl   fit  key_crossed    spread          31.7% n=41 -38.9      45.3% n=172 -14.7  -1.59
  nfl   fit  mny_gave_back  moneyline        51.1% n=90 +7.8      40.9% n=171 -37.1   1.57
  cbb   fit  line_ineff     total           52.9% n=681 +1.1      49.5% n=2819 -5.4   1.57
  cbb   fit  line_reversed  moneyline       47.9% n=941 +9.4      44.6% n=1273 -7.9   1.54
  nfl   fit  mny_gave_back  total           41.8% n=55 -20.1       53.7% n=147 +2.6  -1.51
  nfl   fwd  line_ineff     total           75.9% n=29 +44.7       60.6% n=71 +15.7   1.46
  nfl   fwd  mny_gave_back  spread          44.8% n=58 -12.7       29.0% n=31 -44.8   1.45
  cbb   fwd  line_ineff     total           51.5% n=452 -1.6      47.6% n=1089 -9.1   1.42
  nfl   fwd  mny_gave_back  total            55.9% n=34 +8.1       69.7% n=66 +32.4  -1.37
  cbb   fit  mny_gave_back  moneyline       44.3% n=902 -3.4      47.2% n=1312 +1.5  -1.31
  cbb   fit  mny_gave_back  total          49.3% n=1954 -5.8      51.3% n=1546 -2.1  -1.18
  cbb   fwd  mny_crossed    spread         46.6% n=696 -11.8       50.1% n=417 -4.4  -1.15
  nfl   fwd  deep_series    moneyline       44.0% n=50 +11.7       33.9% n=59 -41.5   1.08
  nfl   fit  mny_crossed    spread          33.3% n=27 -37.2      44.1% n=186 -16.8  -1.06
  cbb   fwd  mny_gave_back  spread         44.7% n=217 -15.6       48.7% n=896 -7.4  -1.05
  cbb   fwd  line_ineff     spread          50.3% n=316 -4.1      46.9% n=797 -11.0   1.02
  cbb   fit  mny_crossed    spread         49.3% n=2111 -6.6       51.1% n=927 -2.5  -0.95
  nfl   fwd  deep_series    total           60.8% n=51 +16.2       69.4% n=49 +32.4  -0.90
  cbb   fit  line_ineff     spread          48.5% n=715 -8.0      50.2% n=2323 -4.6  -0.80
  cbb   fwd  mny_crossed    moneyline       48.3% n=745 -4.8       46.3% n=449 -4.6   0.67
  cbb   fwd  mny_crossed    total          49.1% n=1308 -6.2      46.8% n=233 -10.7   0.65
  cbb   fwd  line_reversed  spread         45.0% n=109 -14.0      48.2% n=1004 -8.5  -0.65
  nfl   fit  deep_series    moneyline      43.6% n=218 -23.0       48.8% n=43 -14.7  -0.63
  cbb   fit  lim_slashed    moneyline        41.5% n=41 -8.5      46.1% n=2173 -0.4  -0.59
  nfl   fit  line_ineff     total            53.4% n=58 +1.6       49.3% n=144 -5.7   0.53
  cbb   fwd  line_ineff     moneyline       46.8% n=500 -4.1       48.1% n=694 -5.2  -0.45
  cbb   fwd  line_reversed  total           50.0% n=204 -5.0      48.5% n=1337 -7.2   0.39
  nfl   fit  mny_gave_back  spread          44.4% n=72 -15.4      41.8% n=141 -21.4   0.36
  nfl   fit  deep_series    total           50.8% n=177 -2.8        48.0% n=25 -8.8   0.27
  cbb   fit  mny_crossed    moneyline      46.2% n=1458 -0.9       45.6% n=756 +0.2   0.27
  cbb   fit  line_reversed  spread          50.2% n=233 -5.4      49.8% n=2805 -5.4   0.12
  nfl   fwd  deep_series    spread          40.0% n=40 -21.8       38.8% n=49 -25.6   0.12
  cbb   fwd  line_reversed  moneyline       47.5% n=451 -3.3       47.6% n=743 -5.6  -0.07
  cbb   fwd  mny_gave_back  total           48.7% n=823 -6.9       48.7% n=718 -6.9  -0.01

  FIT is a hypothesis, FORWARD is evidence. A feature that only appears in FIT
  rows has not been tested; one that holds in both, and across sports, is the
  project's own standard for believing anything.

  12 at |z|>=2.0 against ~2.4 expected. Above chance — worth a look.
  ROI is the currency, not hit rate: money_level hit 73.4% and lost 14.87 units.

## 4. HOLDOUT AND FORWARD SAMPLE

  cbb: holdout from 2026-11-21 (6d ago)
         684 fit games, 307 forward games

  nfl: holdout from 2026-11-21 (6d ago)
         43 fit games, 16 forward games
         forward sample is 16 games. Nothing measured forward can
         distinguish a 55% signal from a 50% one yet. Do not promote on it.

------------------------------------------------------------------------------
The standing rule: search the project docs before investigating anything here.
An hour went on a question already answered 0-for-17 in propwatch-line-value-state.
------------------------------------------------------------------------------
```
