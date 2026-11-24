# Propwatch audit

Generated 2026-11-24 by `audit.py`. Nobody asked for it; that is the point.

```
==============================================================================
PROPWATCH AUDIT   2026-11-24
==============================================================================

Nobody asked for this. That is the point -- the knowledge base only gets read when
a session opens it, and the guards only fire once a measurement is already wrong.

## 0. IS THE DATA STILL ARRIVING?

  NFL collector    last    0.1h ago  (2026-11-24T00:40:19Z)
  CBB collector    NO COMMITS FOUND  <-- never ran, or the message changed
  NCAAF collector  NO COMMITS FOUND  <-- never ran, or the message changed
  NFL grader       NO COMMITS FOUND  <-- never ran, or the message changed
  CBB grader       NO COMMITS FOUND  <-- never ran, or the message changed

  4 feed(s) stale. EVERY NUMBER BELOW THAT DEPENDS ON THEM IS SUSPECT --
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
      1504  period=all (fit+fwd re-counted)
       707  market=both (pools base rates)
       635  signal pair (derived from singles)

  independent-ish cells with >=30 decisions: 328
  z is hit rate against each cell's OWN base rate, not against break-even.
    |z| >= 1.65  observed 33    expected-by-chance   32.5   nothing here
    |z| >= 2.0   observed 15    expected-by-chance   14.9   nothing here
    |z| >= 2.5   observed 5     expected-by-chance    4.1   marginally above chance
    |z| >= 3.0   observed 3     expected-by-chance    0.9   ABOVE CHANCE -- worth a look

  The expected column is not a caveat. It is the comparison. A cell is only
  evidence if the observed count at its z exceeds the expected count, and then
  only the excess is evidence -- not that cell in particular.

  ### SIGN ASYMMETRY (direction, which the count test cannot see)

  FWD    73 cells   28 positive / 45 negative   mean z -0.16   sign test p=0.060
         follow_move        n= 16  mean z -0.67
         rlm_quiet          n=  4  mean z -0.67
         rlm_ratio          n=  2  mean z -0.64
         consensus_gap      n=  5  mean z +0.66
         money_delta        n=  3  mean z +0.75
         pin_value          n=  5  mean z +0.80

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

  ### FORWARD (out of sample -- evidence)  (73 cells)

  sport signal                 cp     mkt       slice             W-L   hit%  base%   edge    ROI%      z
  cbb   pin_value              close  spread    1-3k bets       27-14   65.9   50.2   15.6    22.9   2.00
  cbb   follow_move            close  total     pin limit <$    12-23   34.3   48.7  -14.4   -34.5  -1.71
  cbb   follow_move            early  spread    all             21-31   40.4   52.1  -11.7   -22.1  -1.69
  cbb   pin_move               close  total     1-3k bets       20-33   37.7   48.5  -10.7   -27.8  -1.57
  cbb   follow_move            early  spread    <1k bets        20-29   40.8   51.7  -10.8   -21.2  -1.52
  cbb   follow_move            close  spread    1-3k bets       25-32   43.9   53.3   -9.5   -16.0  -1.43
  cbb   money_level            close  moneyline pin $2k+        22-21   51.2   61.7  -10.6   -26.5  -1.42
  cbb   sharp_gap              close  total     pin limit <$    12-22   35.3   47.3  -12.1   -32.7  -1.40
  cbb   pin_move               close  total     all             29-43   40.3   48.5   -8.2   -23.0  -1.40
  cbb   rlm_ratio              close  moneyline all              9-26   25.7   37.1  -11.4   -42.3  -1.39
  cbb   money_moving           close  total     pin limit <$    14-24   36.8   48.1  -11.3   -29.8  -1.39
  cbb   consensus_gap          early  total     all             19-12   61.3   49.1   12.2    16.5   1.36

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
    spread    all         with  49.1% n=108 ROI   -5.4   without  48.0% n=479 ROI   -8.5   lift   +1.1pt /   +3.2ROI  z +0.20
    spread    1-3k        with  51.4% n= 70 ROI   -0.9   without  48.3% n=321 ROI   -7.9   lift   +3.1pt /   +7.1ROI  z +0.48
    spread    3k+         with  53.8% n= 26 ROI   +4.1   without  44.2% n= 86 ROI  -16.3   lift   +9.7pt /  +20.3ROI  z +0.87
    total     all         with  43.0% n=242 ROI  -17.6   without  51.5% n=464 ROI   -1.6   lift   -8.5pt /  -16.0ROI  z -2.15
    total     all    FWD  with  34.5% n= 55 ROI  -33.4   without  48.3% n= 58 ROI   -7.9   lift  -13.7pt /  -25.5ROI  z -1.48
    total     <1k         with  53.1% n= 32 ROI   +2.0   without  39.7% n= 63 ROI  -23.9   lift  +13.4pt /  +25.8ROI  z +1.25
    total     1-3k        with  43.2% n=162 ROI  -17.2   without  51.7% n=302 ROI   -1.3   lift   -8.4pt /  -15.9ROI  z -1.74
    total     1-3k   FWD  with  36.6% n= 41 ROI  -29.4   without  46.5% n= 43 ROI  -11.4   lift   -9.9pt /  -18.0ROI  z -0.92
    total     3k+         with  35.4% n= 48 ROI  -31.8   without  58.6% n= 99 ROI  +11.7   lift  -23.2pt /  -43.6ROI  z -2.64
    moneyline all         with  31.6% n=212 ROI   -5.9   without  71.9% n=409 ROI   -4.9   lift  -40.3pt /   -1.0ROI  z -9.65   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline all    FWD  with  30.0% n= 50 ROI   -9.9   without  62.3% n= 53 ROI   -3.1   lift  -32.3pt /   -6.8ROI  z -3.28   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline <1k         with  22.2% n= 27 ROI  -39.6   without  72.4% n= 76 ROI   -8.3   lift  -50.1pt /  -31.3ROI  z -4.55   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k        with  31.2% n=144 ROI   -1.9   without  75.0% n=240 ROI   -2.6   lift  -43.8pt /   +0.7ROI  z -8.43   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k   FWD  with  36.8% n= 38 ROI  +12.1   without  61.1% n= 36 ROI   -1.8   lift  -24.3pt /  +13.9ROI  z -2.09   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 3k+         with  39.0% n= 41 ROI   +2.5   without  63.4% n= 93 ROI   -8.0   lift  -24.4pt /  +10.5ROI  z -2.62   [ML: read ROI only, hit lift is a dog/fav artifact]

  does rlm_ratio improve on its parent follow_move?
    spread    all         with  48.3% n= 87 ROI   -7.9   without  48.2% n=500 ROI   -7.9   lift   +0.1pt /   -0.0ROI  z +0.01
    spread    1-3k        with  47.3% n= 55 ROI  -10.0   without  49.1% n=336 ROI   -6.1   lift   -1.8pt /   -3.9ROI  z -0.25
    total     all         with  53.1% n=260 ROI   +1.7   without  46.0% n=446 ROI  -12.2   lift   +7.1pt /  +13.9ROI  z +1.82
    total     all    FWD  with  44.4% n= 36 ROI  -14.7   without  40.3% n= 77 ROI  -23.0   lift   +4.2pt /   +8.3ROI  z +0.42
    total     <1k         with  57.1% n= 35 ROI  +10.0   without  36.7% n= 60 ROI  -29.8   lift  +20.5pt /  +39.8ROI  z +1.94
    total     1-3k        with  51.4% n=177 ROI   -1.6   without  47.0% n=287 ROI  -10.1   lift   +4.4pt /   +8.6ROI  z +0.92
    total     1-3k   FWD  with  42.3% n= 26 ROI  -18.7   without  41.4% n= 58 ROI  -20.8   lift   +0.9pt /   +2.1ROI  z +0.08
    total     3k+         with  56.2% n= 48 ROI   +7.7   without  48.5% n= 99 ROI   -7.4   lift   +7.8pt /  +15.1ROI  z +0.88
    moneyline all         with  30.3% n=152 ROI  -11.6   without  67.2% n=469 ROI   -3.2   lift  -36.9pt /   -8.4ROI  z -8.01   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline all    FWD  with  25.7% n= 35 ROI  -42.3   without  57.4% n= 68 ROI  +12.0   lift  -31.6pt /  -54.3ROI  z -3.05   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k        with  27.1% n=107 ROI  -17.7   without  70.8% n=277 ROI   +3.6   lift  -43.7pt /  -21.3ROI  z -7.79   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k   FWD  with  27.6% n= 29 ROI  -38.4   without  62.2% n= 45 ROI  +33.5   lift  -34.6pt /  -71.9ROI  z -2.91   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 3k+         with  44.4% n= 27 ROI  +27.4   without  58.9% n=107 ROI  -12.9   lift  -14.4pt /  +40.3ROI  z -1.35   [ML: read ROI only, hit lift is a dog/fav artifact]

  does pin_rlm improve on its parent pin_move?
    spread    all         with  53.1% n= 49 ROI   +1.4   without  48.2% n=409 ROI   -8.0   lift   +4.9pt /   +9.4ROI  z +0.65
    spread    1-3k        with  53.1% n= 32 ROI   +1.4   without  49.4% n=269 ROI   -5.6   lift   +3.7pt /   +7.0ROI  z +0.39
    total     all         with  52.8% n=161 ROI   +1.2   without  47.8% n=299 ROI   -8.6   lift   +5.0pt /   +9.9ROI  z +1.02
    total     <1k         with  59.3% n= 27 ROI  +13.9   without  51.4% n= 37 ROI   -1.5   lift   +7.9pt /  +15.3ROI  z +0.63
    total     1-3k        with  53.5% n= 99 ROI   +2.5   without  46.5% n=202 ROI  -11.2   lift   +7.0pt /  +13.7ROI  z +1.14
    total     3k+         with  45.7% n= 35 ROI  -12.2   without  50.0% n= 60 ROI   -4.4   lift   -4.3pt /   -7.8ROI  z -0.40
    moneyline all         with  37.6% n= 85 ROI  +18.8   without  57.4% n=162 ROI   -4.2   lift  -19.8pt /  +23.1ROI  z -2.95   [ML: read ROI only, hit lift is a dog/fav artifact]
    moneyline 1-3k        with  41.2% n= 51 ROI  +32.6   without  57.8% n= 90 ROI   -3.9   lift  -16.6pt /  +36.5ROI  z -1.90   [ML: read ROI only, hit lift is a dog/fav artifact]

  ### NFL

## 4. HOLDOUT AND FORWARD SAMPLE

  cbb: holdout from 2026-11-21 (3d ago)
         684 fit games, 122 forward games

  nfl: holdout from 2026-11-21 (3d ago)
         43 fit games, 11 forward games
         forward sample is 11 games. Nothing measured forward can
         distinguish a 55% signal from a 50% one yet. Do not promote on it.

------------------------------------------------------------------------------
The standing rule: search the project docs before investigating anything here.
An hour went on a question already answered 0-for-17 in propwatch-line-value-state.
------------------------------------------------------------------------------
```
