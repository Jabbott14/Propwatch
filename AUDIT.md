# Propwatch audit

Generated 2026-11-24 by `audit.py`. Nobody asked for it; that is the point.

```
==============================================================================
PROPWATCH AUDIT   2026-11-24
==============================================================================

Nobody asked for this. That is the point -- the knowledge base only gets read when
a session opens it, and the guards only fire once a measurement is already wrong.

## 0. IS THE DATA STILL ARRIVING?

  NFL collector    last    0.1h ago  (2026-11-24T08:03:53-05:00)
  CBB collector    NO COMMITS FOUND  <-- never ran, or the message changed
  NCAAF collector  last    0.1h ago  (2026-11-24T13:00:04+00:00)
  NFL grader       NO COMMITS FOUND  <-- never ran, or the message changed
  CBB grader       NO COMMITS FOUND  <-- never ran, or the message changed

  3 feed(s) stale. EVERY NUMBER BELOW THAT DEPENDS ON THEM IS SUSPECT --
  a dead feed does not look like an error downstream, it looks like a quiet
  market. Check the Actions tab before trusting anything in sections 2-5.

## 1. RECORDED AND CONSUMED BY NOTHING

  6 RECORDED (computed, graded by nothing) | 9 OPEN (not built)

  [RECORDED]       2d  key numbers 3 and 7 in football; CBB verified to have none
             key_crossed, key_dist -- computed, graded by nothing

  [RECORDED]       2d  a Pinnacle limit cut mid-week is unpriced news
             lim_slashed, lim_drop_frac -- computed, graded by nothing

  [RECORDED]       2d  the PATH money takes across the week, not its endpoint -- switches, retracements, give-backs
             path_features(): line_eff, line_revs, mny_crossings, mny_gave_back, sync, against_money_pts
             note: the two-photograph problem: every signal reads 2 observations from a series of 200-470. Median 232 money observations per NFL spread; the money majority flips in 28% of games. Recorded deliberately so grading it does not reset the holdout -- but recorded is not tested.

  [RECORDED]       2d  signals that are strict SUBSETS of other signals are graded against the wrong thing
             audit.py section 5 computes lift vs parent; the scorecard still grades vs base rate
             note: Found while re-testing volume properly. rlm_quiet fires 523/523 times where follow_move also fires -- 100%, by construction, since both require the line to have moved toward their side. rlm_ratio 477/477. pin_rlm 87.2% inside pin_move. They are FILTERS, not signals, and the comparison that matters is against the parent on the same games. Scored that way rlm_ratio lifts follow_move on CBB totals from 45.5% to 53.6%, ROI -13.1 to +2.6, n=252, z=+2.03 -- a row the base-rate scorecard reports as unremarkable. Also means the project does not have 12 independent signals: 8 pairs agree on side 100% of the time when both fire, so every 'two signals confirm' reading is in many cases one signal counted twice.

  [RECORDED]       2d  retracement off the Pinnacle extreme -- a number that bottomed and climbed back is not the same as one still falling
             pin_bounce, retraced -- display only
             note: built after quoting a stale 136.5 -> 132 Pinnacle move on UTEP that had actually bottomed at 131 and been climbing 4.5h

  [RECORDED]       1d  the NFL collector dies silently and nothing notices
             audit.py section 0 (heartbeat) now checks it; the workflow itself is NOT fixed
             note: DEFECT. `snap` ran every ~10 min then STOPPED 2026-11-23T01:12Z -- fifteen minutes before the MIN@SF kickoff -- so that game has no closing data. Came back 10:56Z, 9.7h gap. Died again, 3h gap. Last run 14:46Z and was 7.6h cold when Monday's card was being built. CBB and NCAAF ran clean every 30 min through all of it, which is exactly why nothing looked wrong. collect.yml is cron '7 * * * *' with timeout-minutes 350, so ~6 runs overlap by design, and `continue-on-error: true` means a failing step never surfaces. Suspected cause is Actions concurrency/queue pressure on NFL Sunday (6 overlapping 5h50m snap jobs plus cbb, ncaaf and the graders), but THIS IS UNVERIFIED -- the Actions API was not reachable from the session that found it. Justin needs to read the Actions tab. A stale feed is the worst failure this project has because downstream it does not look like an error, it looks like a quiet market.

  [OPEN    ]       2d  most-bet / most-watched games are where to fade the public -- NOT standalone, but combined with other signals
             volume slice runs on all 12 signals; audit.py section 5 now reports it per filter
             note: HIS CORRECTION, 2026-11-22, and it was right. The standalone form is measured and dead: fading the public INVERTS with volume, 52.1% under 1k bets -> 47.4% at 4k+, spreads 4k+ 43.0% / -17.9% on n=114. But I then closed the whole idea on 3 of 12 signals, which is not a test of it. His words: 'maybe it isn't that easy of just fading public but looking at most bet games and fading public w other signals involved as well -- we have many other different signals too.' Re-run across all 12: n-weighted aggregate is FLAT in every market (|z| all under 1.5), so volume is not a blanket conditioner. Per-cell, 9 of 26 signal x market cells rise monotonically with volume against 4.3 expected by chance, 4 fall -- a mild excess on correlated cells. Spread and total disagree in direction for the same signal (rlm_quiet spread lift +1.3 -> +11.8 with volume; total lift -9.0 -> -22.0). STAYS OPEN: the aggregate says no, the per-cell picture is not flat, NFL cannot check it (0 forward cells at n>=30), and everything above is FIT.

  [OPEN    ]       2d  CFB limits scale differently than NFL, so raw limit comparison is wrong across sports
             raw limits still compared

  [OPEN    ]       2d  steam = many books moving at once
             breadth (books-per-interval) only -- ordering is PERMANENTLY unmeasurable, all 7 books share our snapshot timestamp
             note: data is in hand; the breadth measurement has not been built

  [OPEN    ]       2d  our own closing-line model, to price independently of the books
             needs hoopR

  [OPEN    ]       2d  Circa as a second sharp reference alongside Pinnacle
             raw/vsin_circa collected, never parsed

  [OPEN    ]       2d  record each book's OWN observed change time, not our snapshot time
             collector change, not made -- this is the only thing that would make lead-lag measurable going forward

  [OPEN    ]       2d  the BOOK'S OWN EXPOSURE -- which side the house needs. Upstream of why a number moves.
             not collected anywhere
             note: Justin shared a Patrick Everson / Prime Sportsbook post 2026-11-22 listing 'Biggest House Needs' (Lions -3.5, Panthers -2.5, Bills -16.5, Raiders +10.5, Giants +5.5) alongside sharp action and public plays. We collect tickets and money -- what BETTORS did. We have never had what the BOOK is holding. A book moves a number to balance its own book, so its liability is upstream of the move we measure; every signal in this system reads the move and infers backwards. HONEST LIMIT: this is not published as a feed. It appears in weekly columns written by people (Everson/Prime, VSIN liability reports, SuperBook). Treat it as a manual cross-check when Justin shares one, not a signal input, unless a structured source turns up. Also unresolved: Everson listed Lions -3.5 under BOTH 'Top Public Plays' and 'Biggest House Needs', which is not consistent under either reading of the term -- do not build on it until the convention is confirmed.

  [OPEN    ]       2d  'the public' is one book's clientele, not a fact about the world
             every public/fade signal reads Action Network book 69 only
             note: MATERIAL LIMIT ON THE WHOLE FADE-THE-PUBLIC THESIS, found 2026-11-22 by cross-checking Justin's Everson post. Prime listed 'Dolphins +16.5' as a top public play while our Action Network data read 60% of tickets on BUFFALO -- the opposite side. Prime listed public on Ravens +2.5 where we read 49/50, no lean at all. rlm, rlm_quiet, rlm_ratio, sharp_gap and the volume slices all define 'the public' as FanDuel's ticket split via Action Network. If two books disagree about which side the public is on, then a fade signal is fading one book's customers, and its record is a statement about that book, not about public money. Nothing in the archive can currently test this because we have only ever had one source of splits.

  [OPEN    ]       2d  splits from a book that is NOT FanDuel -- Circa, DK, South Point via VSIN
             raw/vsin and raw/vsin_circa: BROKEN, see note
             note: DEFECT, found 2026-11-22. Two problems. (1) What we archived is the VSIN page SHELL, not data -- the splits load from query params (?source=DK&view=topspreadhandle) and the fetched HTML contains the filter chips and zero numbers. 'Handle' appears 3 times, all in button labels; 'Tickets' appears 0 times. So the parse that was never written would have found nothing anyway. (2) Collection STOPPED on 2026-11-12 and nothing noticed for ten days. This is the fourth collected-but-never-parsed item after Circa, is_live/is_alt_market, and the rotation numbers. It is also the blocker on public_is_book_specific: a second book's splits is the only way to test whether 'the public' means anything beyond FanDuel.

## 2. ANOMALY SCAN, WITH THE MULTIPLE-COMPARISONS DENOMINATOR

  excluded as non-independent or unscoreable:
      1514  period=all (fit+fwd re-counted)
       720  market=both (pools base rates)
       649  signal pair (derived from singles)

  independent-ish cells with >=30 decisions: 336
  z is hit rate against each cell's OWN base rate, not against break-even.
    |z| >= 1.65  observed 35    expected-by-chance   33.2   nothing here
    |z| >= 2.0   observed 16    expected-by-chance   15.3   nothing here
    |z| >= 2.5   observed 5     expected-by-chance    4.2   nothing here
    |z| >= 3.0   observed 3     expected-by-chance    0.9   ABOVE CHANCE -- worth a look

  The expected column is not a caveat. It is the comparison. A cell is only
  evidence if the observed count at its z exceeds the expected count, and then
  only the excess is evidence -- not that cell in particular.

  ### SIGN ASYMMETRY (direction, which the count test cannot see)

  FWD    81 cells   32 positive / 49 negative   mean z -0.18   sign test p=0.075
         rlm_quiet          n=  4  mean z -0.78
         rlm_ratio          n=  3  mean z -0.75
         follow_move        n= 16  mean z -0.62
         pin_value          n=  6  mean z +0.51
         money_delta        n=  3  mean z +0.53
         consensus_gap      n=  7  mean z +0.80

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

  ### FORWARD (out of sample -- evidence)  (81 cells)

  sport signal                 cp     mkt       slice             W-L   hit%  base%   edge    ROI%      z
  cbb   follow_move            early  spread    all             22-36   37.9   51.4  -13.4   -26.7  -2.05
  cbb   pin_move               close  total     all             31-50   38.3   49.6  -11.3   -26.8  -2.04
  cbb   follow_move            early  spread    <1k bets        21-34   38.2   51.0  -12.8   -26.2  -1.90
  cbb   follow_move            close  total     pin limit <$    12-23   34.3   49.1  -14.8   -34.5  -1.75
  cbb   pin_value              close  spread    1-3k bets       27-16   62.8   49.8   13.0    17.1   1.70
  cbb   consensus_gap          close  moneyline pin $2k+         24-9   72.7   59.1   13.6    26.2   1.59
  cbb   follow_move            close  total     all             54-75   41.9   48.7   -6.9   -19.8  -1.55
  cbb   pin_move               close  moneyline 1-3k bets       21-15   58.3   45.6   12.7    19.9   1.53
  cbb   pin_move               close  total     pin $1-2k       19-30   38.8   49.6  -10.8   -25.7  -1.52
  cbb   sharp_gap              close  total     pin limit <$    12-22   35.3   48.1  -12.8   -32.7  -1.49
  cbb   pin_move               close  total     1-3k bets       22-34   39.3   49.1   -9.8   -25.0  -1.47
  cbb   money_moving           close  total     pin limit <$    14-24   36.8   48.6  -11.8   -29.8  -1.45

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

  [    2d] Is the low-limit CBB totals cell real or is it where this dataset's noise concentrates?
           why: pin_value reads 60.4% there vs 47.7% at high limits (totals only, spreads flat), and pin_rlm and rlm_ratio are ALSO better under $1k. The same corner keeps reappearing across unrelated signals. Either thin markets where Pinnacle has not done the work and FanDuel copies a lazy number, or noise. They look identical and it has never survived forward.
           next: forward-only test; the plausibility guard already flags it  (owner: unassigned)

  [    2d] Does cross-book BREADTH (how many books move within an interval) predict anything, given ordering is unmeasurable?
           why: the only survivable form of the steam idea. Data is in hand.
           next: build the breadth measurement  (owner: unassigned)

  [    2d] Does the volume/attention thesis hold in NFL, where public bias is stronger?
           why: it inverted in CBB, but NFL's n=43 cannot answer it either way. If the thesis is right anywhere it is probably NFL.
           next: most of a season of forward data  (owner: unassigned)

  [    2d] Why do ~200 CBB finals never join to a graded game?
           why: unknown selection bias in everything measured off the graded set
           next: inspect the unmatched list  (owner: unassigned)

  [    2d] Does rlm_ratio's lift over follow_move on totals (+8.1 pts, ROI -13.1 to +2.6, n=252, z=+2.03) survive forward?
           why: the best-posed result the project has produced, because it is measured against the right denominator -- the parent signal on the same games, not a market base rate. pin_rlm shows the same direction on totals (+5.3 pts, ROI -9.2 to +1.3), which is weak support and not independent of it. FORWARD, 2026-11-22, once the date-field bug was fixed: lift +12.5 pts, ROI -34.8 to -11.0, n=28, z=+1.10. Direction reproduces out of sample. n=28 and z=1.10 are not evidence, but this is the FIRST thing in this project whose direction has held fit-to-forward at all, and note the parent is badly negative forward (34.0%) so part of the lift is the parent being bad.
           next: forward only, let n grow. Do not re-cut it in-sample. Watch whether the lift survives the parent improving.  (owner: unassigned)

  [    2d] Why does rlm_ratio hold forward while rlm_quiet gets worse, when both are Justin's same reverse-movement idea?
           why: they are both filters on follow_move and they split cleanly. rlm_ratio (minority tickets + money share at >=1.2x the ticket share + line confirms) forward lift +12.5 on totals. rlm_quiet (minority tickets AND minority money + line confirms) forward lift -18.2 on the same market. The difference between them is the money ratio: rlm_ratio requires the money to be disproportionately heavy on that side, rlm_quiet requires it to be light. Same line confirmation, opposite money condition, opposite result.
           next: this is a mechanism question, not a data-cut question. What kind of account moves a number while leaving a light money share behind?  (owner: unassigned)

  [    2d] Should the scorecard's signal-PAIR rows be dropped for pairs that agree 100% of the time?
           why: the pair rows exist on the theory that evidence combines. For follow_move+rlm_quiet, which agree 523/523, nothing combines -- the pair row is the child row with a different name, and both appeared in the forward anomaly list as separate cells with identical 24-61 records.
           next: decide whether to drop them or label them nested; either way the anomaly scan already excludes pairs  (owner: unassigned)

  [    2d] For each of the 4 live signals: what mechanism does it trade against, documented OUTSIDE our archive?
           why: a correlation with no mechanism is a hypothesis. The Pinnacle limit/news research was 5 minutes of outside reading and produced two register items. Nothing has been read that way about the other signals.
           next: one signal per week of outside reading  (owner: unassigned)

  [    2d] Does an independent sharp source systematically disagree with follow_move after a number has already travelled?
           why: 2026-11-22, Everson/Prime named sharp action on Saints +11.5 and Raiders +10 -- both the OPPOSITE side from our lean, and in both cases our lean came from follow_move chasing a 1-2 point move that had already happened. follow_move is our worst forward signal, mean z -0.76, +0.22 fit to negative forward. The same source CONFIRMED us where the move was still live: sharps took Bucs at +6.5/+5.5 (Pinnacle has since gone to 3.5) and Eagles at +4.5 (now 3.5). Two confirmations where we were early, two contradictions where we were late. That is a mechanism for the follow_move forward number, not a coincidence.
           next: log Everson's weekly post against our follow_move calls for the rest of the season. n will be tiny; it is a mechanism check, not a signal test.  (owner: unassigned)

  [    1d] Why did price gating come back after being closed with evidence, and what stops the next recurrence?
           why: On 2026-11-22 the whole NFL card was ranked by FanDuel-vs-Pinnacle edge, two artifacts were built around it, and it was described as 'the only column that does not depend on a signal record'. Price gating is in the brain doc's CLOSED list -- the gap is non-monotonic, being a point WORSE than Pinnacle was the best bucket, and it had already been removed once for cutting plays with no support. Justin caught it the second time too, in nearly the same words. CLAUDE.md lists the closed items but a closed item is a fact to recall, not a check that fires. Day-one evidence was mixed: the four signal-only plays that price gating had excluded went 2-2, and the biggest price play (ARI +15.5, $100k limit) lost.
           next: consider making audit.py assert that the current ranking rule is not one of the closed ones -- a closed item that only lives in prose gets re-derived  (owner: unassigned)

## 5. FILTER LIFT -- signals that are subsets of other signals

  rlm_quiet and rlm_ratio fire only where follow_move also fires, 100% of the
  time, by construction. pin_rlm sits 87% inside pin_move. They are filters, so
  the comparison that matters is against the PARENT on the same games, not
  against a market base rate. Scored against a base rate they look unremarkable.

  ### CBB

  does rlm_quiet improve on its parent follow_move?
    spread    all         with  49.1% n=110 ROI   -5.3   without  48.3% n=487 ROI   -8.0   lift   +0.8pt /   +2.8ROI  z +0.16
    spread    1-3k        with  52.1% n= 71 ROI   +0.5   without  48.5% n=326 ROI   -7.5   lift   +3.6pt /   +8.1ROI  z +0.56
    spread    3k+         with  51.9% n= 27 ROI   +0.2   without  44.9% n= 89 ROI  -14.8   lift   +6.9pt /  +15.0ROI  z +0.63
    total     all         with  43.1% n=248 ROI  -17.2   without  51.3% n=474 ROI   -2.1   lift   -8.1pt /  -15.1ROI  z -2.07
    total     all    FWD  with  36.1% n= 61 ROI  -30.4   without  47.1% n= 68 ROI  -10.3   lift  -11.0pt /  -20.1ROI  z -1.26
    total     <1k         with  53.1% n= 32 ROI   +2.0   without  39.7% n= 63 ROI  -23.9   lift  +13.4pt /  +25.8ROI  z +1.25
    total     1-3k        with  43.0% n=165 ROI  -17.5   without  52.0% n=306 ROI   -0.8   lift   -8.9pt /  -16.7ROI  z -1.85
    total     1-3k   FWD  with  36.4% n= 44 ROI  -29.8   without  48.9% n= 47 ROI   -6.9   lift  -12.6pt /  -22.9ROI  z -1.21
    total     3k+         with  37.3% n= 51 ROI  -28.2   without  56.2% n=105 ROI   +7.2   lift  -18.9pt /  -35.4ROI  z -2.22
    moneyline all         with  30.9% n=220 ROI   -8.3   without  71.9% n=417 ROI   -4.5   lift  -41.0pt /   -3.8ROI  z -9.97   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline all    FWD  with  27.6% n= 58 ROI  -18.7   without  63.9% n= 61 ROI   -0.8   lift  -36.3pt /  -17.9ROI  z -3.98   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline <1k         with  22.2% n= 27 ROI  -39.6   without  72.4% n= 76 ROI   -8.3   lift  -50.1pt /  -31.3ROI  z -4.55   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k        with  31.3% n=147 ROI   -2.5   without  74.6% n=244 ROI   -2.8   lift  -43.3pt /   +0.3ROI  z -8.41   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k   FWD  with  36.6% n= 41 ROI   +9.1   without  60.0% n= 40 ROI   -2.9   lift  -23.4pt /  +12.0ROI  z -2.11   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 3k+         with  34.8% n= 46 ROI   -8.6   without  64.9% n= 97 ROI   -6.0   lift  -30.2pt /   -2.7ROI  z -3.39   [ML: read ROI only, hit lift is a dog/fav artifact]

  does rlm_ratio improve on its parent follow_move?
    spread    all         with  48.3% n= 87 ROI   -7.9   without  48.4% n=510 ROI   -7.5   lift   -0.2pt /   -0.5ROI  z -0.03
    spread    1-3k        with  47.3% n= 55 ROI  -10.0   without  49.4% n=342 ROI   -5.5   lift   -2.1pt /   -4.5ROI  z -0.29
    total     all         with  53.0% n=266 ROI   +1.6   without  45.8% n=456 ROI  -12.4   lift   +7.2pt /  +14.0ROI  z +1.86
    total     all    FWD  with  45.2% n= 42 ROI  -13.1   without  40.2% n= 87 ROI  -23.0   lift   +5.0pt /   +9.8ROI  z +0.54
    total     <1k         with  57.1% n= 35 ROI  +10.0   without  36.7% n= 60 ROI  -29.8   lift  +20.5pt /  +39.8ROI  z +1.94
    total     1-3k        with  51.4% n=179 ROI   -1.6   without  47.3% n=292 ROI   -9.7   lift   +4.1pt /   +8.1ROI  z +0.87
    total     1-3k   FWD  with  42.9% n= 28 ROI  -17.9   without  42.9% n= 63 ROI  -18.0   lift   +0.0pt /   +0.2ROI  z +0.00
    total     3k+         with  55.8% n= 52 ROI   +6.9   without  47.1% n=104 ROI  -10.0   lift   +8.7pt /  +16.9ROI  z +1.02
    moneyline all         with  29.9% n=157 ROI  -13.0   without  66.9% n=480 ROI   -3.5   lift  -36.9pt /   -9.5ROI  z -8.13   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline all    FWD  with  25.0% n= 40 ROI  -44.1   without  57.0% n= 79 ROI   +8.0   lift  -32.0pt /  -52.1ROI  z -3.30   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k        with  27.3% n=110 ROI  -18.0   without  70.5% n=281 ROI   +3.3   lift  -43.2pt /  -21.4ROI  z -7.79   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k   FWD  with  28.1% n= 32 ROI  -37.5   without  61.2% n= 49 ROI  +29.7   lift  -33.1pt /  -67.2ROI  z -2.91   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 3k+         with  41.4% n= 29 ROI  +18.6   without  58.8% n=114 ROI  -13.3   lift  -17.4pt /  +31.9ROI  z -1.68   [ML: read ROI only, hit lift is a dog/fav artifact]

  does pin_rlm improve on its parent pin_move?
    spread    all         with  53.1% n= 49 ROI   +1.4   without  48.3% n=418 ROI   -7.7   lift   +4.7pt /   +9.1ROI  z +0.63
    spread    1-3k        with  53.1% n= 32 ROI   +1.4   without  49.6% n=272 ROI   -5.2   lift   +3.5pt /   +6.7ROI  z +0.37
    total     all         with  52.4% n=164 ROI   +0.5   without  47.2% n=305 ROI   -9.8   lift   +5.2pt /  +10.3ROI  z +1.08
    total     <1k         with  59.3% n= 27 ROI  +13.9   without  51.4% n= 37 ROI   -1.5   lift   +7.9pt /  +15.3ROI  z +0.63
    total     1-3k        with  53.5% n=101 ROI   +2.3   without  46.8% n=203 ROI  -10.7   lift   +6.7pt /  +13.0ROI  z +1.10
    total     3k+         with  44.4% n= 36 ROI  -14.6   without  46.2% n= 65 ROI  -11.8   lift   -1.7pt /   -2.8ROI  z -0.17
    moneyline all         with  37.5% n= 88 ROI  +17.2   without  57.4% n=169 ROI   -4.3   lift  -19.9pt /  +21.5ROI  z -3.03   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k        with  41.5% n= 53 ROI  +31.6   without  58.7% n= 92 ROI   -2.2   lift  -17.2pt /  +33.8ROI  z -2.00   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 3k+         with  32.0% n= 25 ROI   -4.8   without  56.6% n= 53 ROI   -4.4   lift  -24.6pt /   -0.4ROI  z -2.03   [ML: read ROI only, hit lift is a dog/fav artifact]

  ### NFL

## 4. HOLDOUT AND FORWARD SAMPLE

  cbb: holdout from 2026-11-21 (3d ago)
         684 fit games, 138 forward games

  nfl: holdout from 2026-11-21 (3d ago)
         43 fit games, 11 forward games
         forward sample is 11 games. Nothing measured forward can
         distinguish a 55% signal from a 50% one yet. Do not promote on it.

------------------------------------------------------------------------------
The standing rule: search the project docs before investigating anything here.
An hour went on a question already answered 0-for-17 in propwatch-line-value-state.
------------------------------------------------------------------------------
```
