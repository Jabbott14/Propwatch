# Propwatch audit

Generated 2026-11-22 by `audit.py`. Nobody asked for it; that is the point.

```
==============================================================================
PROPWATCH AUDIT   2026-11-22
==============================================================================

Nobody asked for this. That is the point -- the knowledge base only gets read when
a session opens it, and the guards only fire once a measurement is already wrong.

## 1. RECORDED AND CONSUMED BY NOTHING

  5 RECORDED (computed, graded by nothing) | 6 OPEN (not built)

  [RECORDED]       0d  key numbers 3 and 7 in football; CBB verified to have none
             key_crossed, key_dist -- computed, graded by nothing

  [RECORDED]       0d  a Pinnacle limit cut mid-week is unpriced news
             lim_slashed, lim_drop_frac -- computed, graded by nothing

  [RECORDED]       0d  the PATH money takes across the week, not its endpoint -- switches, retracements, give-backs
             path_features(): line_eff, line_revs, mny_crossings, mny_gave_back, sync, against_money_pts
             note: the two-photograph problem: every signal reads 2 observations from a series of 200-470. Median 232 money observations per NFL spread; the money majority flips in 28% of games. Recorded deliberately so grading it does not reset the holdout -- but recorded is not tested.

  [RECORDED]       0d  signals that are strict SUBSETS of other signals are graded against the wrong thing
             audit.py section 5 computes lift vs parent; the scorecard still grades vs base rate
             note: Found while re-testing volume properly. rlm_quiet fires 523/523 times where follow_move also fires -- 100%, by construction, since both require the line to have moved toward their side. rlm_ratio 477/477. pin_rlm 87.2% inside pin_move. They are FILTERS, not signals, and the comparison that matters is against the parent on the same games. Scored that way rlm_ratio lifts follow_move on CBB totals from 45.5% to 53.6%, ROI -13.1 to +2.6, n=252, z=+2.03 -- a row the base-rate scorecard reports as unremarkable. Also means the project does not have 12 independent signals: 8 pairs agree on side 100% of the time when both fire, so every 'two signals confirm' reading is in many cases one signal counted twice.

  [RECORDED]       0d  retracement off the Pinnacle extreme -- a number that bottomed and climbed back is not the same as one still falling
             pin_bounce, retraced -- display only
             note: built after quoting a stale 136.5 -> 132 Pinnacle move on UTEP that had actually bottomed at 131 and been climbing 4.5h

  [OPEN    ]       0d  most-bet / most-watched games are where to fade the public -- NOT standalone, but combined with other signals
             volume slice runs on all 12 signals; audit.py section 5 now reports it per filter
             note: HIS CORRECTION, 2026-11-22, and it was right. The standalone form is measured and dead: fading the public INVERTS with volume, 52.1% under 1k bets -> 47.4% at 4k+, spreads 4k+ 43.0% / -17.9% on n=114. But I then closed the whole idea on 3 of 12 signals, which is not a test of it. His words: 'maybe it isn't that easy of just fading public but looking at most bet games and fading public w other signals involved as well -- we have many other different signals too.' Re-run across all 12: n-weighted aggregate is FLAT in every market (|z| all under 1.5), so volume is not a blanket conditioner. Per-cell, 9 of 26 signal x market cells rise monotonically with volume against 4.3 expected by chance, 4 fall -- a mild excess on correlated cells. Spread and total disagree in direction for the same signal (rlm_quiet spread lift +1.3 -> +11.8 with volume; total lift -9.0 -> -22.0). STAYS OPEN: the aggregate says no, the per-cell picture is not flat, NFL cannot check it (0 forward cells at n>=30), and everything above is FIT.

  [OPEN    ]       0d  CFB limits scale differently than NFL, so raw limit comparison is wrong across sports
             raw limits still compared

  [OPEN    ]       0d  steam = many books moving at once
             breadth (books-per-interval) only -- ordering is PERMANENTLY unmeasurable, all 7 books share our snapshot timestamp
             note: data is in hand; the breadth measurement has not been built

  [OPEN    ]       0d  our own closing-line model, to price independently of the books
             needs hoopR

  [OPEN    ]       0d  Circa as a second sharp reference alongside Pinnacle
             raw/vsin_circa collected, never parsed

  [OPEN    ]       0d  record each book's OWN observed change time, not our snapshot time
             collector change, not made -- this is the only thing that would make lead-lag measurable going forward

## 2. ANOMALY SCAN, WITH THE MULTIPLE-COMPARISONS DENOMINATOR

  excluded as non-independent or unscoreable:
      1409  period=all (fit+fwd re-counted)
       640  market=both (pools base rates)
       595  signal pair (derived from singles)

  independent-ish cells with >=30 decisions: 299
  z is hit rate against each cell's OWN base rate, not against break-even.
    |z| >= 1.65  observed 36    expected-by-chance   29.6   marginally above chance
    |z| >= 2.0   observed 15    expected-by-chance   13.6   nothing here
    |z| >= 2.5   observed 5     expected-by-chance    3.7   marginally above chance
    |z| >= 3.0   observed 3     expected-by-chance    0.8   ABOVE CHANCE -- worth a look

  The expected column is not a caveat. It is the comparison. A cell is only
  evidence if the observed count at its z exceeds the expected count, and then
  only the excess is evidence -- not that cell in particular.

  ### SIGN ASYMMETRY (direction, which the count test cannot see)

  FWD    44 cells   15 positive / 29 negative   mean z -0.40   sign test p=0.049
         rlm_quiet          n=  2  mean z -1.30
         follow_move        n= 13  mean z -0.76
         sharp_gap          n=  6  mean z -0.69
         consensus_gap      n=  1  mean z +0.66
         pin_value          n=  3  mean z +0.75
         money_delta        n=  1  mean z +0.97

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

  ### FORWARD (out of sample -- evidence)  (44 cells)

  sport signal                 cp     mkt       slice             W-L   hit%  base%   edge    ROI%      z
  cbb   pin_value              close  spread    all             24-11   68.6   49.5   19.1    28.0   2.26
  cbb   pin_move               close  total     all             18-33   35.3   47.9  -12.6   -32.1  -1.80
  cbb   follow_move            close  spread    1-3k bets       15-24   38.5   52.5  -14.1   -26.4  -1.76
  cbb   follow_move            close  total     1-3k bets       21-36   36.8   48.4  -11.6   -29.3  -1.75
  cbb   follow_move            close  total     all             31-50   38.3   47.7   -9.4   -26.5  -1.70
  cbb   rlm_quiet              close  total     all             12-29   29.3   42.3  -13.0   -43.5  -1.69
  cbb   pin_move               close  total     1-3k bets       13-24   35.1   48.5  -13.3   -32.6  -1.63
  cbb   follow_move            early  spread    all             12-20   37.5   51.5  -14.0   -28.1  -1.58
  cbb   follow_move            close  spread    all             22-31   41.5   51.9  -10.4   -20.5  -1.51
  cbb   sharp_gap              close  moneyline 1-3k bets       16-31   34.0   44.9  -10.9   -41.9  -1.50
  cbb   follow_move            early  spread    <1k bets        12-18   40.0   51.2  -11.2   -23.3  -1.23
  cbb   money_delta            close  total     all             21-21   50.0   42.6    7.4    -4.0   0.97

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

  [    0d] Is the low-limit CBB totals cell real or is it where this dataset's noise concentrates?
           why: pin_value reads 60.4% there vs 47.7% at high limits (totals only, spreads flat), and pin_rlm and rlm_ratio are ALSO better under $1k. The same corner keeps reappearing across unrelated signals. Either thin markets where Pinnacle has not done the work and FanDuel copies a lazy number, or noise. They look identical and it has never survived forward.
           next: forward-only test; the plausibility guard already flags it  (owner: unassigned)

  [    0d] Does cross-book BREADTH (how many books move within an interval) predict anything, given ordering is unmeasurable?
           why: the only survivable form of the steam idea. Data is in hand.
           next: build the breadth measurement  (owner: unassigned)

  [    0d] Does the volume/attention thesis hold in NFL, where public bias is stronger?
           why: it inverted in CBB, but NFL's n=43 cannot answer it either way. If the thesis is right anywhere it is probably NFL.
           next: most of a season of forward data  (owner: unassigned)

  [    0d] Why do ~200 CBB finals never join to a graded game?
           why: unknown selection bias in everything measured off the graded set
           next: inspect the unmatched list  (owner: unassigned)

  [    0d] Does rlm_ratio's lift over follow_move on totals (+8.1 pts, ROI -13.1 to +2.6, n=252, z=+2.03) survive forward?
           why: the best-posed result the project has produced, because it is measured against the right denominator -- the parent signal on the same games, not a market base rate. It is also entirely FIT. pin_rlm shows the same direction on totals (+5.3 pts, ROI -9.2 to +1.3) which is weak independent support, except pin_rlm is not independent of it.
           next: forward only. Do not re-cut it in-sample.  (owner: unassigned)

  [    0d] Should the scorecard's signal-PAIR rows be dropped for pairs that agree 100% of the time?
           why: the pair rows exist on the theory that evidence combines. For follow_move+rlm_quiet, which agree 523/523, nothing combines -- the pair row is the child row with a different name, and both appeared in the forward anomaly list as separate cells with identical 24-61 records.
           next: decide whether to drop them or label them nested; either way the anomaly scan already excludes pairs  (owner: unassigned)

  [    0d] For each of the 4 live signals: what mechanism does it trade against, documented OUTSIDE our archive?
           why: a correlation with no mechanism is a hypothesis. The Pinnacle limit/news research was 5 minutes of outside reading and produced two register items. Nothing has been read that way about the other signals.
           next: one signal per week of outside reading  (owner: unassigned)

## 5. FILTER LIFT -- signals that are subsets of other signals

  rlm_quiet and rlm_ratio fire only where follow_move also fires, 100% of the
  time, by construction. pin_rlm sits 87% inside pin_move. They are filters, so
  the comparison that matters is against the PARENT on the same games, not
  against a market base rate. Scored against a base rate they look unremarkable.

  ### CBB

  does rlm_quiet improve on its parent follow_move?
    spread    all    with  49.0% n=100 ROI   -5.6   without  47.7% n=461 ROI   -9.1   lift   +1.3pt /   +3.5ROI  z +0.23
    spread    1-3k   with  50.8% n= 65 ROI   -2.2   without  48.1% n=308 ROI   -8.4   lift   +2.7pt /   +6.2ROI  z +0.40
    spread    3k+    with  56.0% n= 25 ROI   +8.2   without  44.2% n= 86 ROI  -16.3   lift  +11.8pt /  +24.5ROI  z +1.04
    total     all    with  42.5% n=228 ROI  -18.4   without  51.6% n=446 ROI   -1.5   lift   -9.0pt /  -16.9ROI  z -2.22
    total     <1k    with  51.6% n= 31 ROI   -0.9   without  41.0% n= 61 ROI  -21.4   lift  +10.6pt /  +20.5ROI  z +0.97
    total     1-3k   with  42.7% n=150 ROI  -18.3   without  51.6% n=287 ROI   -1.5   lift   -8.9pt /  -16.8ROI  z -1.77
    total     3k+    with  36.2% n= 47 ROI  -30.4   without  58.2% n= 98 ROI  +10.9   lift  -22.0pt /  -41.3ROI  z -2.48
    moneyline all    with  30.8% n=195 ROI   -5.9   without  72.2% n=396 ROI   -5.0   lift  -41.5pt /   -0.9ROI  z -9.62   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline <1k    with  24.0% n= 25 ROI  -34.8   without  70.3% n= 74 ROI  -10.9   lift  -46.3pt /  -23.9ROI  z -4.06   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k   with  29.2% n=130 ROI   -3.8   without  76.1% n=230 ROI   -2.3   lift  -46.9pt /   -1.4ROI  z -8.69   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 3k+    with  40.0% n= 40 ROI   +5.1   without  64.1% n= 92 ROI   -7.0   lift  -24.1pt /  +12.1ROI  z -2.57   [ML: read ROI only, hit lift is a dog/fav artifact]

  does rlm_ratio improve on its parent follow_move?
    spread    all    with  47.7% n= 86 ROI   -9.0   without  48.0% n=475 ROI   -8.4   lift   -0.3pt /   -0.6ROI  z -0.06
    spread    1-3k   with  46.3% n= 54 ROI  -11.7   without  48.9% n=319 ROI   -6.6   lift   -2.6pt /   -5.2ROI  z -0.35
    total     all    with  53.6% n=252 ROI   +2.6   without  45.5% n=422 ROI  -13.1   lift   +8.1pt /  +15.7ROI  z +2.03
    total     <1k    with  57.1% n= 35 ROI  +10.0   without  36.8% n= 57 ROI  -29.5   lift  +20.3pt /  +39.5ROI  z +1.90
    total     1-3k   with  52.1% n=169 ROI   -0.3   without  46.3% n=268 ROI  -11.6   lift   +5.8pt /  +11.3ROI  z +1.18
    total     3k+    with  56.2% n= 48 ROI   +7.7   without  48.5% n= 97 ROI   -7.5   lift   +7.8pt /  +15.1ROI  z +0.88
    moneyline all    with  29.5% n=139 ROI  -11.9   without  67.5% n=452 ROI   -3.3   lift  -38.0pt /   -8.6ROI  z -7.95   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k   with  25.3% n= 95 ROI  -19.9   without  71.3% n=265 ROI   +3.3   lift  -46.1pt /  -23.2ROI  z -7.84   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 3k+    with  46.2% n= 26 ROI  +32.3   without  59.4% n=106 ROI  -12.1   lift  -13.3pt /  +44.4ROI  z -1.23   [ML: read ROI only, hit lift is a dog/fav artifact]

  does pin_rlm improve on its parent pin_move?
    spread    all    with  52.1% n= 48 ROI   -0.4   without  48.4% n=395 ROI   -7.6   lift   +3.7pt /   +7.1ROI  z +0.49
    spread    1-3k   with  51.6% n= 31 ROI   -1.5   without  49.6% n=258 ROI   -5.3   lift   +2.0pt /   +3.8ROI  z +0.21
    total     all    with  52.9% n=157 ROI   +1.3   without  47.5% n=282 ROI   -9.2   lift   +5.3pt /  +10.5ROI  z +1.07
    total     <1k    with  59.3% n= 27 ROI  +13.9   without  48.5% n= 33 ROI   -6.8   lift  +10.8pt /  +20.6ROI  z +0.83
    total     1-3k   with  53.7% n= 95 ROI   +2.8   without  46.8% n=190 ROI  -10.5   lift   +6.8pt /  +13.3ROI  z +1.09
    total     3k+    with  45.7% n= 35 ROI  -12.2   without  49.2% n= 59 ROI   -6.0   lift   -3.4pt /   -6.2ROI  z -0.32
    moneyline all    with  35.8% n= 81 ROI  +15.1   without  57.8% n=154 ROI   -4.1   lift  -22.0pt /  +19.2ROI  z -3.20   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k   with  38.3% n= 47 ROI  +27.3   without  59.0% n= 83 ROI   -2.3   lift  -20.7pt /  +29.6ROI  z -2.27   [ML: read ROI only, hit lift is a dog/fav artifact]

  ### NFL

## 4. HOLDOUT AND FORWARD SAMPLE

  cbb: holdout from 2026-11-21 (1d ago)
         684 fit games, 86 forward games
         the holdout moved in the last 2 days -- a threshold changed, so the
         forward test restarted. Every forward record below is new.

  nfl: holdout from 2026-11-21 (1d ago)
         43 fit games, 0 forward games
         forward sample is 0 games. Nothing measured forward can
         distinguish a 55% signal from a 50% one yet. Do not promote on it.
         the holdout moved in the last 2 days -- a threshold changed, so the
         forward test restarted. Every forward record below is new.

------------------------------------------------------------------------------
The standing rule: search the project docs before investigating anything here.
An hour went on a question already answered 0-for-17 in propwatch-line-value-state.
------------------------------------------------------------------------------
```
