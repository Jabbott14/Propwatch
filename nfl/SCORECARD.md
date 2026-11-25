# NFL scorecard

Generated 2026-11-25 09:02 UTC. 55 graded games (0 finished games had no final score and are not graded).

## Read this first: fit vs forward

**43 games before 2026-11-21 (fit) · 12 on or after it (forward).**

Every signal here, every threshold, and every PROMOTE/DROP label this scorecard
has printed was chosen while looking at the games before 2026-11-21.
Scoring those choices on those same games is grading the exam you studied from.
`pin_value` was 108-68 in CBB first halves and 10-1 on NFL spreads; both numbers
were fitted and scored on one sample, and neither has ever been tested on a game
it did not help choose. So every record below appears twice:

- **FIT** — in-sample. A label here is a **hypothesis**. It is what we guessed.
- **FORWARD** — out-of-sample. A label here is **evidence**. It is what happened.

Base rates are measured separately in each period. Scoring the forward test
against the fit window's chalk rate would re-import the bias the split exists to
remove — the fit window ran
65.1% favourites, and a signal that is
structurally long favourites would look like a discovery the week dogs cover.

The board follows the same rule: a signal is weighted by its FIT edge until it
has 30 decided forward outcomes, and by its FORWARD edge from then on. It
migrates onto out-of-sample evidence on its own, with no hand-tuning.

**Changing any threshold moves the holdout date to the day of the change and
restarts the forward test.** That is the real cost of fiddling with the engine,
and it is deliberately expensive.

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before kickoff. Break-even at -110 is 52.4%. CLV = points of
closing-line value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured on
this sample. `edge` is hit% minus that. A signal that is structurally long dogs or
unders will beat 50% in any week dogs or unders run, which is not an edge --
this sample ran **61.8% favourites** (n=55)
**52.7% overs** (n=55) and **76.4% moneyline favourites** (n=55) and **50.0% team-total overs** (n=110).

Moneyline has no handicap, so its `follow_move` reads price, its CLV is
percentage points of implied probability, and `pin_value` is a pure price
comparison against Pinnacle's no-vig fair -- no half-points involved.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

**Gate B is these signals. Gate A is the Pinnacle columns on the board — a price
floor, never a veto.** EV against Pinnacle can essentially never be positive,
because Pinnacle is the fair-value definition. Using it as a veto rejects every
signal this system exists to find. See fault 4 in propwatch-news-vs-coherence.md.

# FORWARD (out-of-sample — this is the evidence)

Games kicking off on or after 2026-11-21. Nothing in the engine was chosen using these. n=12 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 1-2 | 33.3 | 50.0 | -16.7 | -1.0 | -33.3 | 0.0 | 0.0 | keep collecting (3/30) |
| pin_move | both | 7-4 | 63.6 | 56.1 | 7.6 | +0.44 | 4.0 | -0.02 | 54.5 | keep collecting (11/30) |
| pin_rlm | both | 1-2 | 33.3 | 38.9 | -5.6 | -1.05 | -34.9 | -1.23 | 33.3 | keep collecting (3/30) |
| pre_move | both | 5-11 | 31.2 | 39.6 | -8.3 | -4.97 | -31.0 | -0.59 | 31.2 | keep collecting (16/30) |
| follow_move | both | 4-6 | 40.0 | 50.0 | -10.0 | -2.21 | -22.1 | -0.5 | 10.0 | keep collecting (10/30) |
| rlm | both | 1-2 | 33.3 | 50.0 | -16.7 | -1.0 | -33.3 | 0.0 | 0.0 | keep collecting (3/30) |
| rlm_ratio | both | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level | both | 22-14 | 61.1 | 55.6 | 5.6 | +1.03 | 2.9 | 0.34 | 44.4 | no edge shown yet |
| sharp_gap | both | 14-18 | 43.8 | 45.3 | -1.6 | -3.92 | -12.2 | -0.15 | 40.6 | no edge shown yet |
| pin_value | both | 7-12 | 36.8 | 46.9 | -10.1 | -5.88 | -31.0 | 0.23 | 31.6 | keep collecting (19/30) |
| book_lag | both | 3-0 | 100.0 | 50.0 | 50.0 | +2.6 | 86.5 | -1.63 | 33.3 | keep collecting (3/30) |
| consensus_gap | both | 8-10 | 44.4 | 38.9 | 5.6 | +0.82 | 4.6 | -0.41 | 33.3 | keep collecting (18/30) |
| consensus_gap+money_level | both | 4-2 | 66.7 | 50.0 | 16.7 | +1.37 | 22.8 | 0.58 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | both | 2-5 | 28.6 | 42.9 | -14.3 | -3.3 | -47.1 | 0.47 | 28.6 | keep collecting (7/30) |
| consensus_gap+sharp_gap | both | 5-9 | 35.7 | 38.1 | -2.4 | -3.12 | -22.3 | -0.49 | 35.7 | keep collecting (14/30) |
| follow_move+rlm | both | 1-2 | 33.3 | 50.0 | -16.7 | -1.0 | -33.3 | 0.0 | 0.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | both | 1-2 | 33.3 | 50.0 | -16.7 | -1.0 | -33.3 | 0.0 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+pin_value | both | 4-3 | 57.1 | 50.0 | 7.1 | +0.48 | 6.9 | 0.57 | 42.9 | keep collecting (7/30) |
| money_level+sharp_gap | both | 7-4 | 63.6 | 51.5 | 12.1 | +2.23 | 20.3 | 0.42 | 63.6 | keep collecting (11/30) |
| pin_value+sharp_gap | both | 3-6 | 33.3 | 44.4 | -11.1 | -3.43 | -38.1 | 0.7 | 55.6 | keep collecting (9/30) |
| rlm+rlm_quiet | both | 1-2 | 33.3 | 50.0 | -16.7 | -1.0 | -33.3 | 0.0 | 0.0 | redundant -- identical record to rlm alone, not independent confirmation |
| money_level+pin_move | both | 6-3 | 66.7 | 57.4 | 9.3 | +0.49 | 5.4 | -0.02 | 55.6 | keep collecting (9/30) |
| pre_move+sharp_gap | both | 5-11 | 31.2 | 39.6 | -8.3 | -4.97 | -31.0 | -0.59 | 31.2 | redundant -- identical record to pre_move alone, not independent confirmation |
| consensus_gap+pre_move | both | 2-8 | 20.0 | 33.3 | -13.3 | -4.66 | -46.6 | -1.04 | 20.0 | keep collecting (10/30) |
| pin_value+pre_move | both | 1-3 | 25.0 | 37.5 | -12.5 | -2.17 | -54.2 | 0.82 | 50.0 | keep collecting (4/30) |
| follow_move+money_level | both | 3-2 | 60.0 | 50.0 | 10.0 | +0.78 | 15.7 | -0.5 | 20.0 | keep collecting (5/30) |
| follow_move+pin_move | both | 1-2 | 33.3 | 50.0 | -16.7 | -1.05 | -34.9 | -0.67 | 33.3 | keep collecting (3/30) |
| follow_move+sharp_gap | both | 2-2 | 50.0 | 50.0 | 0.0 | -0.05 | -1.2 | -0.62 | 25.0 | keep collecting (4/30) |
| pin_move+sharp_gap | both | 3-2 | 60.0 | 53.3 | 6.7 | +0.77 | 15.5 | 0.32 | 80.0 | keep collecting (5/30) |
| book_lag+money_level | both | 2-0 | 100.0 | 58.3 | 41.7 | +1.25 | 62.7 | -1.25 | 50.0 | keep collecting (2/30) |
| book_lag+pin_move | both | 2-0 | 100.0 | 58.3 | 41.7 | +1.25 | 62.7 | -1.25 | 50.0 | keep collecting (2/30) |
| consensus_gap+follow_move | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_value | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+rlm_ratio | both | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+rlm_ratio | both | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| rlm_quiet+rlm_ratio | both | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| rlm_ratio+sharp_gap | both | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+pre_move | both | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_rlm+pre_move | both | 1-2 | 33.3 | 38.9 | -5.6 | -1.05 | -34.9 | -1.23 | 33.3 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 1-2 | 33.3 | 38.9 | -5.6 | -1.05 | -34.9 | -1.23 | 33.3 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_rlm | both | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 | -2.35 | 0.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| book_lag+consensus_gap | both | 1-0 | 100.0 | 33.3 | 66.7 | +1.34 | 134.0 | -2.4 | 0.0 | keep collecting (1/30) |
| book_lag+pre_move | both | 1-0 | 100.0 | 33.3 | 66.7 | +1.34 | 134.0 | -2.4 | 0.0 | keep collecting (1/30) |
| book_lag+sharp_gap | both | 2-0 | 100.0 | 41.7 | 58.3 | +2.21 | 110.5 | -0.2 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 1-0 | 100.0 | 50.0 | 50.0 | +0.87 | 87.0 | 2.0 | 100.0 | keep collecting (1/30) |
| pin_move+pin_value | both | 1-2 | 33.3 | 50.0 | -16.7 | -1.13 | -37.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+pin_move | both | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| rlm_quiet | spread | 1-2 | 33.3 | 50.0 | -16.7 | -1.0 | -33.3 | 0.0 | 0.0 | keep collecting (3/30) |
| pin_move | moneyline | 3-1 | 75.0 | 66.7 | 8.3 | -0.28 | -7.1 | -0.05 | 75.0 | keep collecting (4/30) |
| pin_move | spread | 2-2 | 50.0 | 50.0 | 0.0 | -0.18 | -4.5 | 0.0 | 50.0 | keep collecting (4/30) |
| pin_move | total | 2-1 | 66.7 | 50.0 | 16.7 | +0.9 | 30.1 | 0.0 | 33.3 | keep collecting (3/30) |
| pin_rlm | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 | -2.35 | 0.0 | keep collecting (2/30) |
| pin_rlm | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 | 1.0 | 100.0 | keep collecting (1/30) |
| pre_move | moneyline | 2-8 | 20.0 | 33.3 | -13.3 | -4.66 | -46.6 | -1.04 | 20.0 | keep collecting (10/30) |
| pre_move | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.31 | -5.1 | 0.17 | 50.0 | keep collecting (6/30) |
| follow_move | spread | 4-6 | 40.0 | 50.0 | -10.0 | -2.21 | -22.1 | -0.5 | 10.0 | keep collecting (10/30) |
| rlm | spread | 1-2 | 33.3 | 50.0 | -16.7 | -1.0 | -33.3 | 0.0 | 0.0 | keep collecting (3/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level | moneyline | 8-4 | 66.7 | 66.7 | 0.0 | -1.57 | -13.1 | 0.77 | 58.3 | keep collecting (12/30) |
| money_level | spread | 8-4 | 66.7 | 50.0 | 16.7 | +3.1 | 25.8 | 0.08 | 33.3 | keep collecting (12/30) |
| money_level | total | 6-6 | 50.0 | 50.0 | 0.0 | -0.5 | -4.2 | 0.17 | 41.7 | keep collecting (12/30) |
| sharp_gap | moneyline | 2-9 | 18.2 | 36.4 | -18.2 | -5.66 | -51.5 | -0.89 | 27.3 | keep collecting (11/30) |
| sharp_gap | spread | 8-3 | 72.7 | 50.0 | 22.7 | +4.18 | 38.0 | 0.27 | 45.5 | keep collecting (11/30) |
| sharp_gap | total | 4-6 | 40.0 | 50.0 | -10.0 | -2.44 | -24.4 | 0.2 | 50.0 | keep collecting (10/30) |
| pin_value | moneyline | 0-3 | 0.0 | 33.3 | -33.3 | -3.0 | -100.0 | 0.77 | 33.3 | keep collecting (3/30) |
| pin_value | spread | 4-2 | 66.7 | 50.0 | 16.7 | +1.48 | 24.7 | 0.5 | 33.3 | keep collecting (6/30) |
| pin_value | total | 1-3 | 25.0 | 50.0 | -25.0 | -2.17 | -54.2 | 0.0 | 50.0 | keep collecting (4/30) |
| pin_value | tt_away | 1-1 | 50.0 | 50.0 | 0.0 | -0.2 | -10.0 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_value | tt_home | 1-3 | 25.0 | 47.9 | -22.9 | -2.0 | -50.0 | 0.0 | 25.0 | keep collecting (4/30) |
| book_lag | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.73 | 86.2 | -3.45 | 0.0 | keep collecting (2/30) |
| book_lag | spread | 1-0 | 100.0 | 50.0 | 50.0 | +0.87 | 87.0 | 2.0 | 100.0 | keep collecting (1/30) |
| consensus_gap | moneyline | 4-8 | 33.3 | 33.3 | -0.0 | -0.55 | -4.6 | -0.9 | 25.0 | keep collecting (12/30) |
| consensus_gap | spread | 4-2 | 66.7 | 50.0 | 16.7 | +1.37 | 22.8 | 0.58 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | moneyline | 0-3 | 0.0 | 33.3 | -33.3 | -3.0 | -100.0 | 0.77 | 33.3 | redundant -- identical record to pin_value alone, not independent confirmation |
| consensus_gap+pre_move | moneyline | 2-8 | 20.0 | 33.3 | -13.3 | -4.66 | -46.6 | -1.04 | 20.0 | redundant -- identical record to pre_move alone, not independent confirmation |
| consensus_gap+sharp_gap | moneyline | 2-8 | 20.0 | 33.3 | -13.3 | -4.66 | -46.6 | -1.04 | 20.0 | keep collecting (10/30) |
| pin_value+pre_move | moneyline | 0-3 | 0.0 | 33.3 | -33.3 | -3.0 | -100.0 | 0.77 | 33.3 | redundant -- identical record to pin_value alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-3 | 0.0 | 33.3 | -33.3 | -3.0 | -100.0 | 0.77 | 33.3 | redundant -- identical record to pin_value alone, not independent confirmation |
| pre_move+sharp_gap | moneyline | 2-8 | 20.0 | 33.3 | -13.3 | -4.66 | -46.6 | -1.04 | 20.0 | redundant -- identical record to pre_move alone, not independent confirmation |
| book_lag+money_level | moneyline | 1-0 | 100.0 | 66.7 | 33.3 | +0.39 | 38.5 | -4.5 | 0.0 | keep collecting (1/30) |
| book_lag+pin_move | moneyline | 1-0 | 100.0 | 66.7 | 33.3 | +0.39 | 38.5 | -4.5 | 0.0 | keep collecting (1/30) |
| money_level+pin_move | moneyline | 3-1 | 75.0 | 66.7 | 8.3 | -0.28 | -7.1 | -0.05 | 75.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| consensus_gap+pin_rlm | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 | -2.35 | 0.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_rlm+pre_move | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 | -2.35 | 0.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 | -2.35 | 0.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | moneyline | 1-0 | 100.0 | 33.3 | 66.7 | +1.34 | 134.0 | -2.4 | 0.0 | keep collecting (1/30) |
| book_lag+pre_move | moneyline | 1-0 | 100.0 | 33.3 | 66.7 | +1.34 | 134.0 | -2.4 | 0.0 | keep collecting (1/30) |
| book_lag+sharp_gap | moneyline | 1-0 | 100.0 | 33.3 | 66.7 | +1.34 | 134.0 | -2.4 | 0.0 | keep collecting (1/30) |
| money_level+sharp_gap | moneyline | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 | 0.6 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | moneyline | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 | 0.6 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 4-2 | 66.7 | 50.0 | 16.7 | +1.37 | 22.8 | 0.58 | 50.0 | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+pin_value | spread | 2-2 | 50.0 | 50.0 | 0.0 | -0.3 | -7.4 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+sharp_gap | spread | 3-1 | 75.0 | 50.0 | 25.0 | +1.54 | 38.4 | 0.88 | 75.0 | keep collecting (4/30) |
| follow_move+rlm | spread | 1-2 | 33.3 | 50.0 | -16.7 | -1.0 | -33.3 | 0.0 | 0.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 1-2 | 33.3 | 50.0 | -16.7 | -1.0 | -33.3 | 0.0 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+pin_value | spread | 4-2 | 66.7 | 50.0 | 16.7 | +1.48 | 24.7 | 0.5 | 33.3 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_level+sharp_gap | spread | 6-1 | 85.7 | 50.0 | 35.7 | +4.36 | 62.3 | 0.29 | 57.1 | keep collecting (7/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 50.0 | 16.7 | +0.74 | 24.7 | 1.0 | 66.7 | keep collecting (3/30) |
| rlm+rlm_quiet | spread | 1-2 | 33.3 | 50.0 | -16.7 | -1.0 | -33.3 | 0.0 | 0.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+money_level | spread | 3-2 | 60.0 | 50.0 | 10.0 | +0.78 | 15.7 | -0.5 | 20.0 | keep collecting (5/30) |
| follow_move+pin_move | spread | 1-2 | 33.3 | 50.0 | -16.7 | -1.05 | -34.9 | -0.67 | 33.3 | keep collecting (3/30) |
| follow_move+sharp_gap | spread | 2-2 | 50.0 | 50.0 | 0.0 | -0.05 | -1.2 | -0.62 | 25.0 | keep collecting (4/30) |
| money_level+pin_move | spread | 2-2 | 50.0 | 50.0 | 0.0 | -0.18 | -4.5 | 0.0 | 50.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| pin_move+sharp_gap | spread | 2-1 | 66.7 | 50.0 | 16.7 | +0.82 | 27.4 | 0.0 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+rlm_ratio | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| rlm_quiet+rlm_ratio | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| book_lag+money_level | spread | 1-0 | 100.0 | 50.0 | 50.0 | +0.87 | 87.0 | 2.0 | 100.0 | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | spread | 1-0 | 100.0 | 50.0 | 50.0 | +0.87 | 87.0 | 2.0 | 100.0 | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_value | spread | 1-0 | 100.0 | 50.0 | 50.0 | +0.87 | 87.0 | 2.0 | 100.0 | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | spread | 1-0 | 100.0 | 50.0 | 50.0 | +0.87 | 87.0 | 2.0 | 100.0 | redundant -- identical record to book_lag alone, not independent confirmation |
| pin_move+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.13 | -6.5 | 1.5 | 100.0 | keep collecting (2/30) |
| consensus_gap+pin_move | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_move | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 | 0.0 | 0.0 | keep collecting (1/30) |
| pre_move+sharp_gap | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.31 | -5.1 | 0.17 | 50.0 | redundant -- identical record to pre_move alone, not independent confirmation |
| money_level+sharp_gap | total | 1-2 | 33.3 | 50.0 | -16.7 | -1.13 | -37.7 | 0.67 | 66.7 | keep collecting (3/30) |
| pin_value+pre_move | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.83 | 83.3 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | total | 1-2 | 33.3 | 50.0 | -16.7 | -1.17 | -38.9 | 0.33 | 66.7 | keep collecting (3/30) |
| pin_move+pin_rlm | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 | 1.0 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pre_move | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_rlm+pre_move | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 | 1.0 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 | 1.0 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | total | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 8-5 | 61.5 | 46.2 | 15.4 | +3.34 | 25.7 |  |  | keep collecting (13/30) |
| pin_move | both | 17-11 | 60.7 | 50.6 | 10.1 | +3.37 | 12.0 |  |  | keep collecting (28/30) |
| money_delta | both | 4-4 | 50.0 | 45.8 | 4.2 | +1.27 | 15.9 |  |  | keep collecting (8/30) |
| pin_rlm | both | 0-3 | 0.0 | 38.9 | -38.9 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pre_move | both | 1-2 | 33.3 | 38.9 | -5.6 | -1.04 | -34.6 |  |  | keep collecting (3/30) |
| follow_move | both | 26-16 | 61.9 | 51.5 | 10.4 | +6.38 | 15.2 |  |  | no edge shown yet |
| rlm | both | 8-5 | 61.5 | 46.2 | 15.4 | +3.34 | 25.7 |  |  | keep collecting (13/30) |
| rlm_ratio | both | 0-2 | 0.0 | 41.7 | -41.7 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level | both | 17-18 | 48.6 | 55.7 | -7.1 | -7.63 | -21.8 |  |  | no edge shown yet |
| sharp_gap | both | 15-20 | 42.9 | 47.1 | -4.3 | -4.49 | -12.8 |  |  | no edge shown yet |
| money_moving | both | 16-19 | 45.7 | 51.4 | -5.7 | -4.49 | -12.8 |  |  | no edge shown yet |
| pin_value | both | 11-18 | 37.9 | 47.4 | -9.5 | -6.65 | -22.9 |  |  | keep collecting (29/30) |
| consensus_gap | both | 4-10 | 28.6 | 35.7 | -7.1 | -1.9 | -13.6 |  |  | keep collecting (14/30) |
| follow_move+money_level | both | 9-8 | 52.9 | 56.9 | -3.9 | -2.04 | -12.0 |  |  | keep collecting (17/30) |
| follow_move+money_moving | both | 6-5 | 54.5 | 56.1 | -1.5 | -0.1 | -0.9 |  |  | keep collecting (11/30) |
| money_level+money_moving | both | 9-11 | 45.0 | 55.8 | -10.8 | -4.55 | -22.8 |  |  | keep collecting (20/30) |
| pin_value+sharp_gap | both | 3-5 | 37.5 | 43.8 | -6.3 | -2.31 | -28.8 |  |  | keep collecting (8/30) |
| money_moving+pin_move | both | 6-4 | 60.0 | 51.7 | 8.3 | +1.09 | 10.9 |  |  | keep collecting (10/30) |
| money_moving+sharp_gap | both | 9-12 | 42.9 | 49.2 | -6.3 | -2.65 | -12.6 |  |  | keep collecting (21/30) |
| pin_move+sharp_gap | both | 7-6 | 53.8 | 47.4 | 6.4 | +0.41 | 3.2 |  |  | keep collecting (13/30) |
| consensus_gap+follow_move | both | 1-2 | 33.3 | 33.3 | 0.0 | -0.28 | -9.3 |  |  | keep collecting (3/30) |
| consensus_gap+rlm | both | 1-2 | 33.3 | 33.3 | 0.0 | -0.28 | -9.3 |  |  | keep collecting (3/30) |
| consensus_gap+rlm_quiet | both | 1-2 | 33.3 | 33.3 | 0.0 | -0.28 | -9.3 |  |  | keep collecting (3/30) |
| consensus_gap+rlm_ratio | both | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+sharp_gap | both | 2-8 | 20.0 | 35.0 | -15.0 | -4.07 | -40.7 |  |  | keep collecting (10/30) |
| follow_move+rlm | both | 8-5 | 61.5 | 46.2 | 15.4 | +3.34 | 25.7 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | both | 8-5 | 61.5 | 46.2 | 15.4 | +3.34 | 25.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 0-2 | 0.0 | 41.7 | -41.7 | -2.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 6-7 | 46.2 | 50.0 | -3.8 | -1.46 | -11.2 |  |  | keep collecting (13/30) |
| rlm+rlm_quiet | both | 8-5 | 61.5 | 46.2 | 15.4 | +3.34 | 25.7 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+rlm_ratio | both | 0-2 | 0.0 | 41.7 | -41.7 | -2.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 3-3 | 50.0 | 47.2 | 2.8 | -0.19 | -3.1 |  |  | keep collecting (6/30) |
| rlm_quiet+rlm_ratio | both | 0-2 | 0.0 | 41.7 | -41.7 | -2.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 3-3 | 50.0 | 47.2 | 2.8 | -0.19 | -3.1 |  |  | keep collecting (6/30) |
| rlm_ratio+sharp_gap | both | 0-2 | 0.0 | 41.7 | -41.7 | -2.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_move | both | 15-8 | 65.2 | 52.2 | 13.0 | +4.59 | 20.0 |  |  | keep collecting (23/30) |
| follow_move+pin_rlm | both | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_rlm | both | 0-2 | 0.0 | 41.7 | -41.7 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_moving+rlm | both | 2-1 | 66.7 | 50.0 | 16.7 | +0.86 | 28.7 |  |  | keep collecting (3/30) |
| money_moving+rlm_quiet | both | 2-1 | 66.7 | 50.0 | 16.7 | +0.86 | 28.7 |  |  | keep collecting (3/30) |
| money_moving+rlm_ratio | both | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_move+pin_rlm | both | 0-3 | 0.0 | 38.9 | -38.9 | -3.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm | both | 7-3 | 70.0 | 46.7 | 23.3 | +4.3 | 43.0 |  |  | keep collecting (10/30) |
| pin_move+rlm_quiet | both | 7-3 | 70.0 | 46.7 | 23.3 | +4.3 | 43.0 |  |  | keep collecting (10/30) |
| pin_move+rlm_ratio | both | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+rlm | both | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+sharp_gap | both | 0-3 | 0.0 | 38.9 | -38.9 | -3.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_move | both | 8-5 | 61.5 | 56.4 | 5.1 | +0.24 | 1.9 |  |  | keep collecting (13/30) |
| money_level+sharp_gap | both | 5-8 | 38.5 | 53.8 | -15.4 | -3.97 | -30.5 |  |  | keep collecting (13/30) |
| consensus_gap+pin_move | both | 1-3 | 25.0 | 33.3 | -8.3 | -1.28 | -32.0 |  |  | keep collecting (4/30) |
| pin_move+pin_value | both | 4-4 | 50.0 | 45.8 | 4.2 | -0.52 | -6.5 |  |  | keep collecting (8/30) |
| follow_move+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 1-2 | 33.3 | 44.4 | -11.1 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| money_delta+rlm | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_delta+rlm_quiet | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_delta+sharp_gap | both | 3-4 | 42.9 | 45.2 | -2.4 | +0.36 | 5.1 |  |  | keep collecting (7/30) |
| consensus_gap+money_delta | both | 1-1 | 50.0 | 33.3 | 16.7 | +1.45 | 72.5 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | both | 1-5 | 16.7 | 38.9 | -22.2 | -2.55 | -42.5 |  |  | keep collecting (6/30) |
| consensus_gap+pin_rlm | both | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+pin_value | both | 1-4 | 20.0 | 36.7 | -16.7 | -1.55 | -31.0 |  |  | keep collecting (5/30) |
| consensus_gap+pre_move | both | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_delta+money_moving | both | 3-2 | 60.0 | 43.3 | 16.7 | +2.36 | 47.2 |  |  | keep collecting (5/30) |
| money_delta+pin_rlm | both | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta+pin_value | both | 0-2 | 0.0 | 41.7 | -41.7 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_delta+pre_move | both | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_value | both | 2-4 | 33.3 | 44.4 | -11.1 | -2.26 | -37.7 |  |  | keep collecting (6/30) |
| money_moving+pre_move | both | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_move+pre_move | both | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+pin_value | both | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm+pre_move | both | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_value+pre_move | both | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pre_move+sharp_gap | both | 1-2 | 33.3 | 38.9 | -5.6 | -1.04 | -34.6 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| money_level+pin_value | both | 4-3 | 57.1 | 50.0 | 7.1 | +0.47 | 6.7 |  |  | keep collecting (7/30) |
| consensus_gap+money_level | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| follow_move+pin_value | both | 3-1 | 75.0 | 50.0 | 25.0 | +1.61 | 40.2 |  |  | keep collecting (4/30) |
| pin_value+rlm | both | 1-0 | 100.0 | 50.0 | 50.0 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_value+rlm_quiet | both | 1-0 | 100.0 | 50.0 | 50.0 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 1-2 | 33.3 | 33.3 | 0.0 | -0.28 | -9.3 |  |  | keep collecting (3/30) |
| rlm_quiet | spread | 3-2 | 60.0 | 50.0 | 10.0 | +0.94 | 18.9 |  |  | keep collecting (5/30) |
| rlm_quiet | total | 4-1 | 80.0 | 50.0 | 30.0 | +2.68 | 53.6 |  |  | keep collecting (5/30) |
| pin_move | moneyline | 4-5 | 44.4 | 51.9 | -7.4 | -2.5 | -27.8 |  |  | keep collecting (9/30) |
| pin_move | spread | 3-4 | 42.9 | 50.0 | -7.1 | -1.19 | -17.0 |  |  | keep collecting (7/30) |
| pin_move | total | 10-2 | 83.3 | 50.0 | 33.3 | +7.05 | 58.8 |  |  | keep collecting (12/30) |
| money_delta | moneyline | 1-1 | 50.0 | 33.3 | 16.7 | +1.45 | 72.5 |  |  | keep collecting (2/30) |
| money_delta | spread | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta | total | 2-3 | 40.0 | 50.0 | -10.0 | -1.09 | -21.8 |  |  | keep collecting (5/30) |
| pin_rlm | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pre_move | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pre_move | spread | 1-0 | 100.0 | 50.0 | 50.0 | +0.96 | 96.2 |  |  | keep collecting (1/30) |
| follow_move | moneyline | 5-5 | 50.0 | 56.7 | -6.7 | -1.82 | -18.2 |  |  | keep collecting (10/30) |
| follow_move | spread | 5-6 | 45.5 | 50.0 | -4.5 | -1.24 | -11.3 |  |  | keep collecting (11/30) |
| follow_move | total | 8-2 | 80.0 | 50.0 | 30.0 | +5.27 | 52.7 |  |  | keep collecting (10/30) |
| follow_move | tt_away | 5-1 | 83.3 | 48.6 | 34.7 | +3.44 | 57.3 |  |  | keep collecting (6/30) |
| follow_move | tt_home | 3-2 | 60.0 | 50.8 | 9.2 | +0.72 | 14.5 |  |  | keep collecting (5/30) |
| rlm | moneyline | 1-2 | 33.3 | 33.3 | 0.0 | -0.28 | -9.3 |  |  | keep collecting (3/30) |
| rlm | spread | 3-2 | 60.0 | 50.0 | 10.0 | +0.94 | 18.9 |  |  | keep collecting (5/30) |
| rlm | total | 4-1 | 80.0 | 50.0 | 30.0 | +2.68 | 53.6 |  |  | keep collecting (5/30) |
| rlm_ratio | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level | moneyline | 8-4 | 66.7 | 66.7 | 0.0 | -1.67 | -13.9 |  |  | keep collecting (12/30) |
| money_level | spread | 3-8 | 27.3 | 50.0 | -22.7 | -5.35 | -48.6 |  |  | keep collecting (11/30) |
| money_level | total | 6-6 | 50.0 | 50.0 | 0.0 | -0.61 | -5.1 |  |  | keep collecting (12/30) |
| sharp_gap | moneyline | 3-9 | 25.0 | 41.7 | -16.7 | -4.59 | -38.3 |  |  | keep collecting (12/30) |
| sharp_gap | spread | 7-5 | 58.3 | 50.0 | 8.3 | +1.51 | 12.5 |  |  | keep collecting (12/30) |
| sharp_gap | total | 5-6 | 45.5 | 50.0 | -4.5 | -1.4 | -12.8 |  |  | keep collecting (11/30) |
| money_moving | moneyline | 5-6 | 45.5 | 54.5 | -9.1 | -1.63 | -14.8 |  |  | keep collecting (11/30) |
| money_moving | spread | 5-7 | 41.7 | 50.0 | -8.3 | -2.42 | -20.2 |  |  | keep collecting (12/30) |
| money_moving | total | 6-6 | 50.0 | 50.0 | 0.0 | -0.43 | -3.6 |  |  | keep collecting (12/30) |
| pin_value | moneyline | 1-3 | 25.0 | 33.3 | -8.3 | -0.55 | -13.7 |  |  | keep collecting (4/30) |
| pin_value | spread | 2-3 | 40.0 | 50.0 | -10.0 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| pin_value | total | 4-2 | 66.7 | 50.0 | 16.7 | +1.48 | 24.7 |  |  | keep collecting (6/30) |
| pin_value | tt_away | 2-6 | 25.0 | 50.0 | -25.0 | -4.15 | -51.9 |  |  | keep collecting (8/30) |
| pin_value | tt_home | 2-4 | 33.3 | 48.6 | -15.3 | -2.25 | -37.6 |  |  | keep collecting (6/30) |
| consensus_gap | moneyline | 4-8 | 33.3 | 33.3 | -0.0 | +0.1 | 0.8 |  |  | keep collecting (12/30) |
| consensus_gap | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+follow_move | moneyline | 1-2 | 33.3 | 33.3 | 0.0 | -0.28 | -9.3 |  |  | keep collecting (3/30) |
| consensus_gap+rlm | moneyline | 1-2 | 33.3 | 33.3 | 0.0 | -0.28 | -9.3 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| consensus_gap+rlm_quiet | moneyline | 1-2 | 33.3 | 33.3 | 0.0 | -0.28 | -9.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+sharp_gap | moneyline | 2-7 | 22.2 | 33.3 | -11.1 | -3.07 | -34.1 |  |  | keep collecting (9/30) |
| follow_move+rlm | moneyline | 1-2 | 33.3 | 33.3 | 0.0 | -0.28 | -9.3 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | moneyline | 1-2 | 33.3 | 33.3 | 0.0 | -0.28 | -9.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+money_moving | moneyline | 4-3 | 57.1 | 66.7 | -9.5 | -1.08 | -15.4 |  |  | keep collecting (7/30) |
| rlm+rlm_quiet | moneyline | 1-2 | 33.3 | 33.3 | 0.0 | -0.28 | -9.3 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+rlm_ratio | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_quiet+rlm_ratio | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_ratio+sharp_gap | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+pin_move | moneyline | 1-3 | 25.0 | 33.3 | -8.3 | -1.28 | -32.0 |  |  | keep collecting (4/30) |
| follow_move+pin_move | moneyline | 4-3 | 57.1 | 57.1 | 0.0 | -0.5 | -7.1 |  |  | keep collecting (7/30) |
| money_level+sharp_gap | moneyline | 1-2 | 33.3 | 66.7 | -33.3 | -1.52 | -50.8 |  |  | keep collecting (3/30) |
| money_moving+sharp_gap | moneyline | 2-5 | 28.6 | 47.6 | -19.0 | -2.07 | -29.6 |  |  | keep collecting (7/30) |
| pin_move+rlm | moneyline | 1-1 | 50.0 | 33.3 | 16.7 | +0.72 | 36.0 |  |  | keep collecting (2/30) |
| pin_move+rlm_quiet | moneyline | 1-1 | 50.0 | 33.3 | 16.7 | +0.72 | 36.0 |  |  | keep collecting (2/30) |
| consensus_gap+money_delta | moneyline | 1-1 | 50.0 | 33.3 | 16.7 | +1.45 | 72.5 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 1-3 | 25.0 | 33.3 | -8.3 | -0.55 | -13.7 |  |  | keep collecting (4/30) |
| consensus_gap+pin_rlm | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 1-3 | 25.0 | 33.3 | -8.3 | -0.55 | -13.7 |  |  | redundant -- identical record to pin_value alone, not independent confirmation |
| consensus_gap+pre_move | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| money_delta+money_moving | moneyline | 1-1 | 50.0 | 33.3 | 16.7 | +1.45 | 72.5 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_move | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta+pin_rlm | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta+pin_value | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta+pre_move | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta+sharp_gap | moneyline | 1-1 | 50.0 | 33.3 | 16.7 | +1.45 | 72.5 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| money_moving+pin_move | moneyline | 1-2 | 33.3 | 55.6 | -22.2 | -1.5 | -50.0 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_moving+pre_move | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| pin_move+pin_rlm | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_move+pre_move | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_move+sharp_gap | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pre_move | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+sharp_gap | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+pre_move | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-3 | 0.0 | 33.3 | -33.3 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pre_move+sharp_gap | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+money_level | moneyline | 4-3 | 57.1 | 66.7 | -9.5 | -1.54 | -22.0 |  |  | keep collecting (7/30) |
| follow_move+money_moving | moneyline | 2-2 | 50.0 | 66.7 | -16.7 | -0.82 | -20.6 |  |  | keep collecting (4/30) |
| money_level+pin_move | moneyline | 3-2 | 60.0 | 66.7 | -6.7 | -1.22 | -24.4 |  |  | keep collecting (5/30) |
| follow_move+money_level | spread | 1-4 | 20.0 | 50.0 | -30.0 | -3.09 | -61.8 |  |  | keep collecting (5/30) |
| follow_move+money_moving | spread | 2-3 | 40.0 | 50.0 | -10.0 | -1.14 | -22.8 |  |  | keep collecting (5/30) |
| money_level+money_moving | spread | 2-5 | 28.6 | 50.0 | -21.4 | -3.22 | -46.0 |  |  | keep collecting (7/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 50.0 | 16.7 | +0.82 | 27.4 |  |  | keep collecting (3/30) |
| follow_move+pin_move | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.19 | -3.1 |  |  | keep collecting (6/30) |
| follow_move+pin_rlm | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+rlm | spread | 3-2 | 60.0 | 50.0 | 10.0 | +0.94 | 18.9 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 50.0 | 10.0 | +0.94 | 18.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 4-4 | 50.0 | 50.0 | 0.0 | -0.28 | -3.5 |  |  | keep collecting (8/30) |
| money_moving+pin_move | spread | 1-2 | 33.3 | 50.0 | -16.7 | -1.05 | -34.9 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| money_moving+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+sharp_gap | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.27 | -4.5 |  |  | keep collecting (6/30) |
| pin_move+pin_rlm | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm | spread | 2-1 | 66.7 | 50.0 | 16.7 | +0.9 | 30.1 |  |  | keep collecting (3/30) |
| pin_move+rlm_quiet | spread | 2-1 | 66.7 | 50.0 | 16.7 | +0.9 | 30.1 |  |  | keep collecting (3/30) |
| pin_move+rlm_ratio | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_move+sharp_gap | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.19 | -3.1 |  |  | keep collecting (6/30) |
| pin_rlm+rlm | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm+rlm_quiet | spread | 3-2 | 60.0 | 50.0 | 10.0 | +0.94 | 18.9 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+rlm_ratio | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 2-1 | 66.7 | 50.0 | 16.7 | +0.9 | 30.1 |  |  | keep collecting (3/30) |
| rlm_quiet+rlm_ratio | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | spread | 2-1 | 66.7 | 50.0 | 16.7 | +0.9 | 30.1 |  |  | keep collecting (3/30) |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.22 | -37.0 |  |  | keep collecting (6/30) |
| pin_move+pin_value | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+pin_value | spread | 1-2 | 33.3 | 50.0 | -16.7 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| money_moving+pin_value | spread | 1-2 | 33.3 | 50.0 | -16.7 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| money_level+pin_move | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+money_level | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+money_moving | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| pre_move+sharp_gap | spread | 1-0 | 100.0 | 50.0 | 50.0 | +0.96 | 96.2 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| consensus_gap+pin_value | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+sharp_gap | spread | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_move | total | 4-0 | 100.0 | 50.0 | 50.0 | +3.64 | 91.0 |  |  | keep collecting (4/30) |
| money_moving+sharp_gap | total | 4-4 | 50.0 | 50.0 | 0.0 | -0.31 | -3.9 |  |  | keep collecting (8/30) |
| pin_move+sharp_gap | total | 4-1 | 80.0 | 50.0 | 30.0 | +2.6 | 51.9 |  |  | keep collecting (5/30) |
| follow_move+money_level | total | 4-1 | 80.0 | 50.0 | 30.0 | +2.59 | 51.9 |  |  | keep collecting (5/30) |
| follow_move+pin_move | total | 8-2 | 80.0 | 50.0 | 30.0 | +5.27 | 52.7 |  |  | redundant -- identical record to follow_move alone, not independent confirmation |
| follow_move+sharp_gap | total | 2-1 | 66.7 | 50.0 | 16.7 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| money_level+pin_move | total | 5-1 | 83.3 | 50.0 | 33.3 | +3.46 | 57.7 |  |  | keep collecting (6/30) |
| money_level+sharp_gap | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.22 | -5.5 |  |  | keep collecting (4/30) |
| follow_move+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| follow_move+rlm | total | 4-1 | 80.0 | 50.0 | 30.0 | +2.68 | 53.6 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | total | 4-1 | 80.0 | 50.0 | 30.0 | +2.68 | 53.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_delta+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_delta+rlm | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_delta+rlm_quiet | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_delta+sharp_gap | total | 2-3 | 40.0 | 50.0 | -10.0 | -1.09 | -21.8 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+money_moving | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.25 | -4.2 |  |  | keep collecting (6/30) |
| pin_move+rlm | total | 4-1 | 80.0 | 50.0 | 30.0 | +2.68 | 53.6 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| pin_move+rlm_quiet | total | 4-1 | 80.0 | 50.0 | 30.0 | +2.68 | 53.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm+rlm_quiet | total | 4-1 | 80.0 | 50.0 | 30.0 | +2.68 | 53.6 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| rlm_quiet+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_level+pin_value | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.6 | 40.0 |  |  | keep collecting (4/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.87 | 87.0 |  |  | keep collecting (1/30) |
| pin_move+pin_value | total | 4-1 | 80.0 | 50.0 | 30.0 | +2.48 | 49.6 |  |  | keep collecting (5/30) |
| pin_value+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| follow_move+money_moving | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 |  |  | keep collecting (2/30) |
| money_delta+money_moving | total | 2-1 | 66.7 | 50.0 | 16.7 | +0.91 | 30.3 |  |  | keep collecting (3/30) |
| money_moving+rlm | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_moving+rlm_quiet | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| follow_move+pin_value | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.61 | 40.2 |  |  | keep collecting (4/30) |
| pin_value+rlm | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_value+rlm_quiet | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| money_delta+pin_value | total | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |

# FIT (in-sample — this is the hypothesis)

Games before 2026-11-21. The signals and thresholds were chosen by looking at these, so a strong record here is expected and proves nothing. n=43 games.

## EARLY  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 2-6 | 25.0 | 48.3 | -23.3 | -4.33 | -54.2 | 0.06 | 25.0 | keep collecting (8/30) |
| pin_move | both | 14-15 | 48.3 | 61.5 | -13.2 | -5.57 | -19.2 | 1.04 | 55.2 | keep collecting (29/30) |
| pin_rlm | both | 1-4 | 20.0 | 20.9 | -0.9 | -2.92 | -58.4 | -0.8 | 80.0 | keep collecting (5/30) |
| pre_move | both | 8-16 | 33.3 | 31.7 | 1.6 | -6.6 | -27.5 | -0.28 | 45.8 | keep collecting (24/30) |
| follow_move | both | 13-13 | 50.0 | 55.4 | -5.4 | -1.55 | -6.0 | -0.06 | 23.1 | keep collecting (26/30) |
| rlm | both | 1-6 | 14.3 | 45.8 | -31.6 | -5.17 | -73.8 | 0.07 | 28.6 | keep collecting (7/30) |
| rlm_ratio | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level | both | 70-33 | 68.0 | 60.6 | 7.4 | +17.51 | 17.0 | -0.33 | 26.2 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| sharp_gap | both | 60-41 | 59.4 | 49.9 | 9.5 | +10.98 | 10.9 | 0.04 | 34.7 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | both | 15-9 | 62.5 | 52.3 | 10.2 | +3.38 | 14.1 | -0.03 | 33.3 | keep collecting (24/30) |
| pin_value | both | 34-25 | 57.6 | 48.4 | 9.3 | +4.52 | 7.7 | 0.18 | 30.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | both | 2-3 | 40.0 | 41.4 | -1.4 | -1.05 | -21.0 | 0.76 | 80.0 | keep collecting (5/30) |
| consensus_gap | both | 17-31 | 35.4 | 30.9 | 4.5 | -12.59 | -26.2 | 0.12 | 52.1 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm | both | 1-6 | 14.3 | 45.8 | -31.6 | -5.17 | -73.8 | 0.07 | 28.6 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | both | 2-6 | 25.0 | 48.3 | -23.3 | -4.33 | -54.2 | 0.06 | 25.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 11-6 | 64.7 | 56.2 | 8.5 | +4.05 | 23.8 | 0.24 | 23.5 | keep collecting (17/30) |
| rlm+rlm_quiet | both | 1-6 | 14.3 | 45.8 | -31.6 | -5.17 | -73.8 | 0.07 | 28.6 | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+rlm_ratio | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_value | both | 11-3 | 78.6 | 56.1 | 22.4 | +6.82 | 48.7 | -0.04 | 21.4 | keep collecting (14/30) |
| money_level+sharp_gap | both | 46-20 | 69.7 | 58.1 | 11.6 | +16.39 | 24.8 | -0.22 | 25.8 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| pin_value+sharp_gap | both | 14-5 | 73.7 | 48.0 | 25.7 | +7.43 | 39.1 | 0.56 | 36.8 | keep collecting (19/30) |
| consensus_gap+pin_value | both | 4-7 | 36.4 | 36.8 | -0.4 | -3.66 | -33.3 | 1.02 | 63.6 | keep collecting (11/30) |
| money_level+pre_move | both | 2-4 | 33.3 | 39.5 | -6.2 | -2.22 | -37.0 | -1.6 | 16.7 | keep collecting (6/30) |
| pre_move+sharp_gap | both | 8-16 | 33.3 | 31.7 | 1.6 | -6.6 | -27.5 | -0.28 | 45.8 | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+pin_value | both | 5-1 | 83.3 | 60.1 | 23.3 | +3.38 | 56.2 | 0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+follow_move | both | 1-1 | 50.0 | 43.0 | 7.0 | -0.18 | -9.0 | 0.25 | 50.0 | keep collecting (2/30) |
| consensus_gap+money_level | both | 7-1 | 87.5 | 53.8 | 33.7 | +4.33 | 54.1 | -1.05 | 50.0 | keep collecting (8/30) |
| consensus_gap+sharp_gap | both | 12-15 | 44.4 | 32.3 | 12.1 | -2.07 | -7.7 | 0.34 | 63.0 | keep collecting (27/30) |
| follow_move+money_level | both | 10-6 | 62.5 | 61.5 | 1.0 | +2.95 | 18.4 | -0.13 | 25.0 | keep collecting (16/30) |
| consensus_gap+pre_move | both | 4-10 | 28.6 | 20.9 | 7.6 | -4.24 | -30.3 | -0.3 | 64.3 | keep collecting (14/30) |
| follow_move+money_moving | both | 3-2 | 60.0 | 61.9 | -1.9 | +0.38 | 7.5 | -0.62 | 0.0 | keep collecting (5/30) |
| money_level+money_moving | both | 10-3 | 76.9 | 60.6 | 16.3 | +4.57 | 35.1 | -0.47 | 30.8 | keep collecting (13/30) |
| money_moving+pin_value | both | 5-2 | 71.4 | 47.5 | 23.9 | +2.56 | 36.6 | 1.0 | 42.9 | keep collecting (7/30) |
| money_moving+sharp_gap | both | 7-3 | 70.0 | 49.8 | 20.2 | +3.15 | 31.5 | 0.03 | 30.0 | keep collecting (10/30) |
| consensus_gap+rlm | both | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | both | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_value | both | 3-3 | 50.0 | 58.1 | -8.1 | -0.35 | -5.8 | 0.83 | 66.7 | keep collecting (6/30) |
| consensus_gap+pin_move | both | 1-2 | 33.3 | 35.7 | -2.3 | -1.13 | -37.7 | -0.13 | 66.7 | keep collecting (3/30) |
| pin_move+sharp_gap | both | 9-3 | 75.0 | 58.9 | 16.1 | +4.21 | 35.0 | 0.83 | 58.3 | keep collecting (12/30) |
| book_lag+consensus_gap | both | 2-2 | 50.0 | 35.5 | 14.5 | -0.05 | -1.2 | 1.45 | 100.0 | keep collecting (4/30) |
| money_level+pin_move | both | 13-3 | 81.2 | 69.6 | 11.6 | +5.56 | 34.8 | 1.4 | 56.2 | keep collecting (16/30) |
| money_moving+pin_move | both | 1-0 | 100.0 | 34.9 | 65.1 | +0.95 | 95.2 | -2.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+pin_rlm | both | 1-4 | 20.0 | 20.9 | -0.9 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+pre_move | both | 1-4 | 20.0 | 20.9 | -0.9 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 1-4 | 20.0 | 20.9 | -0.9 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+money_level | both | 1-1 | 50.0 | 65.1 | -15.1 | -0.13 | -6.5 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 43.0 | 7.0 | +0.08 | 4.0 | -0.05 | 50.0 | keep collecting (2/30) |
| book_lag+sharp_gap | both | 2-1 | 66.7 | 50.4 | 16.3 | +0.95 | 31.7 | 0.3 | 66.7 | keep collecting (3/30) |
| money_moving+rlm_quiet | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | both | 1-0 | 100.0 | 65.1 | 34.9 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_value+pre_move | both | 1-3 | 25.0 | 27.3 | -2.3 | -2.09 | -52.3 | 2.27 | 75.0 | keep collecting (4/30) |
| consensus_gap+money_moving | both | 2-1 | 66.7 | 25.6 | 41.1 | +0.95 | 31.7 | 2.63 | 100.0 | keep collecting (3/30) |
| money_moving+pre_move | both | 2-1 | 66.7 | 29.5 | 37.2 | +1.03 | 34.4 | 1.63 | 66.7 | keep collecting (3/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | 1.8 | 100.0 | keep collecting (1/30) |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 20.9 | 79.1 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+pre_move | both | 1-0 | 100.0 | 20.9 | 79.1 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| money_moving+pin_rlm | both | 1-0 | 100.0 | 20.9 | 79.1 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| follow_move+pin_move | both | 2-3 | 40.0 | 65.1 | -25.1 | -1.14 | -22.8 | 0.0 | 20.0 | keep collecting (5/30) |
| money_moving+rlm | both | 0-1 | 0.0 | 34.9 | -34.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+rlm | both | 0-2 | 0.0 | 65.1 | -65.1 | -2.0 | -100.0 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_move+rlm_quiet | both | 0-2 | 0.0 | 65.1 | -65.1 | -2.0 | -100.0 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_move+pin_rlm | both | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+pre_move | both | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_move | both | 1-0 | 100.0 | 65.1 | 34.9 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | both | 1-0 | 100.0 | 65.1 | 34.9 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| rlm_quiet | spread | 2-5 | 28.6 | 52.2 | -23.6 | -3.33 | -47.6 | 0.0 | 14.3 | keep collecting (7/30) |
| pin_move | moneyline | 7-6 | 53.8 | 70.1 | -16.3 | -2.94 | -22.6 | 1.72 | 61.5 | keep collecting (13/30) |
| pin_move | spread | 4-3 | 57.1 | 60.8 | -3.7 | +0.68 | 9.8 | -0.14 | 28.6 | keep collecting (7/30) |
| pin_move | total | 3-6 | 33.3 | 49.6 | -16.3 | -3.31 | -36.8 | 1.0 | 66.7 | keep collecting (9/30) |
| pin_rlm | moneyline | 1-4 | 20.0 | 20.9 | -0.9 | -2.92 | -58.4 | -0.8 | 80.0 | keep collecting (5/30) |
| pre_move | moneyline | 4-10 | 28.6 | 20.9 | 7.6 | -4.24 | -30.3 | -0.3 | 64.3 | keep collecting (14/30) |
| pre_move | spread | 1-2 | 33.3 | 45.0 | -11.6 | -1.09 | -36.4 | -0.5 | 33.3 | keep collecting (3/30) |
| pre_move | total | 3-4 | 42.9 | 47.5 | -4.7 | -1.27 | -18.1 | -0.14 | 14.3 | keep collecting (7/30) |
| follow_move | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.44 | -21.9 | -1.3 | 50.0 | keep collecting (2/30) |
| follow_move | spread | 12-11 | 52.2 | 55.9 | -3.7 | -0.11 | -0.5 | 0.17 | 21.7 | keep collecting (23/30) |
| follow_move | total | 0-1 | 0.0 | 53.5 | -53.5 | -1.0 | -100.0 | -3.0 | 0.0 | keep collecting (1/30) |
| rlm | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| rlm | spread | 1-5 | 16.7 | 50.0 | -33.3 | -4.17 | -69.5 | 0.0 | 16.7 | keep collecting (6/30) |
| rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level | moneyline | 27-7 | 79.4 | 75.6 | 3.8 | +4.19 | 12.3 | -0.68 | 35.3 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 24-10 | 70.6 | 54.4 | 16.1 | +12.14 | 35.7 | -0.1 | 17.6 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level | total | 19-16 | 54.3 | 51.9 | 2.4 | +1.17 | 3.4 | -0.23 | 25.7 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 17-16 | 51.5 | 43.8 | 7.7 | -3.06 | -9.3 | 0.27 | 51.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | spread | 22-13 | 62.9 | 54.8 | 8.1 | +7.05 | 20.1 | 0.07 | 25.7 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 21-12 | 63.6 | 51.0 | 12.7 | +6.99 | 21.2 | -0.21 | 27.3 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | moneyline | 5-2 | 71.4 | 54.2 | 17.3 | +1.1 | 15.6 | 0.33 | 57.1 | keep collecting (7/30) |
| money_moving | spread | 5-5 | 50.0 | 53.0 | -3.0 | -0.41 | -4.1 | 0.0 | 30.0 | keep collecting (10/30) |
| money_moving | total | 5-2 | 71.4 | 49.5 | 21.9 | +2.7 | 38.6 | -0.43 | 14.3 | keep collecting (7/30) |
| pin_value | moneyline | 0-6 | 0.0 | 20.9 | -20.9 | -6.0 | -100.0 | 1.68 | 83.3 | keep collecting (6/30) |
| pin_value | spread | 13-4 | 76.5 | 54.4 | 22.0 | +7.42 | 43.6 | 0.09 | 29.4 | keep collecting (17/30) |
| pin_value | total | 6-6 | 50.0 | 50.0 | 0.0 | -0.61 | -5.1 | 0.0 | 16.7 | keep collecting (12/30) |
| pin_value | tt_away | 8-4 | 66.7 | 50.0 | 16.7 | +2.88 | 24.0 | 0.0 | 25.0 | keep collecting (12/30) |
| pin_value | tt_home | 7-5 | 58.3 | 50.2 | 8.1 | +0.83 | 6.9 | -0.08 | 25.0 | keep collecting (12/30) |
| book_lag | moneyline | 1-1 | 50.0 | 20.9 | 29.1 | +0.08 | 4.0 | 2.15 | 100.0 | keep collecting (2/30) |
| book_lag | spread | 1-2 | 33.3 | 55.0 | -21.7 | -1.13 | -37.7 | -0.17 | 66.7 | keep collecting (3/30) |
| consensus_gap | moneyline | 10-25 | 28.6 | 24.3 | 4.3 | -12.6 | -36.0 | 0.05 | 57.1 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 7-6 | 53.8 | 48.8 | 5.0 | +0.01 | 0.1 | 0.31 | 38.5 | keep collecting (13/30) |
| money_level+sharp_gap | moneyline | 12-3 | 80.0 | 71.3 | 8.7 | +2.34 | 15.6 | -0.53 | 33.3 | keep collecting (15/30) |
| consensus_gap+pre_move | moneyline | 4-10 | 28.6 | 20.9 | 7.6 | -4.24 | -30.3 | -0.3 | 64.3 | redundant -- identical record to pre_move alone, not independent confirmation |
| consensus_gap+sharp_gap | moneyline | 8-14 | 36.4 | 26.2 | 10.1 | -4.5 | -20.5 | 0.3 | 63.6 | keep collecting (22/30) |
| pre_move+sharp_gap | moneyline | 4-10 | 28.6 | 20.9 | 7.6 | -4.24 | -30.3 | -0.3 | 64.3 | redundant -- identical record to pre_move alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm alone, not independent confirmation |
| consensus_gap+rlm_quiet | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm alone, not independent confirmation |
| consensus_gap+pin_move | moneyline | 0-2 | 0.0 | 20.9 | -20.9 | -2.0 | -100.0 | -0.7 | 50.0 | keep collecting (2/30) |
| money_level+money_moving | moneyline | 4-0 | 100.0 | 79.1 | 20.9 | +2.02 | 50.4 | -0.78 | 50.0 | keep collecting (4/30) |
| pin_move+sharp_gap | moneyline | 3-3 | 50.0 | 59.7 | -9.7 | -1.21 | -20.2 | 0.83 | 50.0 | keep collecting (6/30) |
| follow_move+money_level | moneyline | 1-0 | 100.0 | 79.1 | 20.9 | +0.56 | 56.2 | -3.1 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | moneyline | 1-0 | 100.0 | 79.1 | 20.9 | +0.56 | 56.2 | -3.1 | 0.0 | keep collecting (1/30) |
| consensus_gap+money_level | moneyline | 3-1 | 75.0 | 50.0 | 25.0 | +0.9 | 22.4 | -2.6 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_value | moneyline | 0-5 | 0.0 | 20.9 | -20.9 | -5.0 | -100.0 | 1.64 | 80.0 | keep collecting (5/30) |
| consensus_gap+pin_rlm | moneyline | 1-4 | 20.0 | 20.9 | -0.9 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| money_level+pre_move | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+pre_move | moneyline | 1-4 | 20.0 | 20.9 | -0.9 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 1-4 | 20.0 | 20.9 | -0.9 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | moneyline | 2-1 | 66.7 | 40.3 | 26.4 | +0.47 | 15.7 | 1.1 | 66.7 | keep collecting (3/30) |
| pin_value+pre_move | moneyline | 0-3 | 0.0 | 20.9 | -20.9 | -3.0 | -100.0 | 3.03 | 100.0 | keep collecting (3/30) |
| pin_value+sharp_gap | moneyline | 0-3 | 0.0 | 20.9 | -20.9 | -3.0 | -100.0 | 3.03 | 100.0 | keep collecting (3/30) |
| consensus_gap+money_moving | moneyline | 1-1 | 50.0 | 20.9 | 29.1 | +0.08 | 4.0 | 3.45 | 100.0 | keep collecting (2/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving+pre_move | moneyline | 1-1 | 50.0 | 20.9 | 29.1 | +0.08 | 4.0 | 3.45 | 100.0 | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | 1.8 | 100.0 | keep collecting (1/30) |
| money_level+pin_move | moneyline | 7-2 | 77.8 | 79.1 | -1.3 | +1.06 | 11.8 | 2.38 | 66.7 | keep collecting (9/30) |
| book_lag+consensus_gap | moneyline | 1-1 | 50.0 | 20.9 | 29.1 | +0.08 | 4.0 | 2.15 | 100.0 | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | moneyline | 1-0 | 100.0 | 20.9 | 79.1 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+pin_rlm | moneyline | 1-0 | 100.0 | 20.9 | 79.1 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+pre_move | moneyline | 1-0 | 100.0 | 20.9 | 79.1 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+sharp_gap | moneyline | 1-0 | 100.0 | 20.9 | 79.1 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 1-0 | 100.0 | 20.9 | 79.1 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+pre_move | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| follow_move+rlm | spread | 1-5 | 16.7 | 50.0 | -33.3 | -4.17 | -69.5 | 0.0 | 16.7 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 2-5 | 28.6 | 52.2 | -23.6 | -3.33 | -47.6 | 0.0 | 14.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 11-6 | 64.7 | 56.2 | 8.5 | +4.05 | 23.8 | 0.24 | 23.5 | keep collecting (17/30) |
| rlm+rlm_quiet | spread | 1-5 | 16.7 | 50.0 | -33.3 | -4.17 | -69.5 | 0.0 | 16.7 | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+pin_value | spread | 4-2 | 66.7 | 50.0 | 16.7 | +1.34 | 22.4 | 0.5 | 50.0 | keep collecting (6/30) |
| money_level+sharp_gap | spread | 19-8 | 70.4 | 56.2 | 14.2 | +9.43 | 34.9 | -0.02 | 22.2 | keep collecting (27/30) |
| follow_move+pin_value | spread | 5-1 | 83.3 | 60.1 | 23.3 | +3.38 | 56.2 | 0.17 | 16.7 | keep collecting (6/30) |
| pin_value+sharp_gap | spread | 9-0 | 100.0 | 55.0 | 45.0 | +7.94 | 88.3 | 0.17 | 33.3 | keep collecting (9/30) |
| consensus_gap+follow_move | spread | 1-0 | 100.0 | 65.1 | 34.9 | +0.82 | 82.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 4-0 | 100.0 | 57.6 | 42.4 | +3.43 | 85.8 | 0.5 | 50.0 | keep collecting (4/30) |
| consensus_gap+sharp_gap | spread | 4-1 | 80.0 | 59.1 | 20.9 | +2.43 | 48.6 | 0.5 | 60.0 | keep collecting (5/30) |
| follow_move+money_level | spread | 9-5 | 64.3 | 60.8 | 3.5 | +3.39 | 24.2 | 0.29 | 28.6 | keep collecting (14/30) |
| money_level+pin_value | spread | 8-1 | 88.9 | 58.4 | 30.5 | +6.11 | 67.9 | 0.17 | 33.3 | keep collecting (9/30) |
| follow_move+money_moving | spread | 2-2 | 50.0 | 57.6 | -7.6 | -0.19 | -4.7 | 0.0 | 0.0 | keep collecting (4/30) |
| money_level+money_moving | spread | 3-2 | 60.0 | 53.0 | 7.0 | +0.8 | 16.0 | -0.6 | 20.0 | keep collecting (5/30) |
| money_moving+pin_value | spread | 4-1 | 80.0 | 53.0 | 27.0 | +2.63 | 52.7 | 0.4 | 40.0 | keep collecting (5/30) |
| money_moving+sharp_gap | spread | 2-2 | 50.0 | 57.6 | -7.6 | -0.15 | -3.8 | -0.25 | 25.0 | keep collecting (4/30) |
| book_lag+consensus_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.13 | -6.5 | 0.75 | 100.0 | keep collecting (2/30) |
| money_level+pre_move | spread | 1-1 | 50.0 | 34.9 | 15.1 | -0.09 | -4.5 | -1.0 | 0.0 | keep collecting (2/30) |
| pre_move+sharp_gap | spread | 1-2 | 33.3 | 45.0 | -11.6 | -1.09 | -36.4 | -0.5 | 33.3 | redundant -- identical record to pre_move alone, not independent confirmation |
| money_level+pin_move | spread | 4-1 | 80.0 | 59.1 | 20.9 | +2.68 | 53.7 | 0.0 | 40.0 | keep collecting (5/30) |
| money_moving+pin_move | spread | 1-0 | 100.0 | 34.9 | 65.1 | +0.95 | 95.2 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+money_level | spread | 1-1 | 50.0 | 65.1 | -15.1 | -0.13 | -6.5 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+money_moving | spread | 0-1 | 0.0 | 65.1 | -65.1 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+sharp_gap | spread | 1-1 | 50.0 | 65.1 | -15.1 | -0.13 | -6.5 | -0.5 | 50.0 | keep collecting (2/30) |
| money_moving+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-0 | 100.0 | 65.1 | 34.9 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+pin_move | spread | 2-3 | 40.0 | 65.1 | -25.1 | -1.14 | -22.8 | 0.0 | 20.0 | keep collecting (5/30) |
| pin_move+pin_value | spread | 2-1 | 66.7 | 65.1 | 1.6 | +0.78 | 26.0 | 0.67 | 66.7 | keep collecting (3/30) |
| pin_move+sharp_gap | spread | 3-0 | 100.0 | 65.1 | 34.9 | +2.73 | 91.0 | 0.67 | 66.7 | keep collecting (3/30) |
| money_moving+rlm | spread | 0-1 | 0.0 | 34.9 | -34.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+rlm | spread | 0-2 | 0.0 | 65.1 | -65.1 | -2.0 | -100.0 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_move+rlm_quiet | spread | 0-2 | 0.0 | 65.1 | -65.1 | -2.0 | -100.0 | -0.5 | 0.0 | keep collecting (2/30) |
| book_lag+pin_move | spread | 1-0 | 100.0 | 65.1 | 34.9 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | spread | 1-0 | 100.0 | 65.1 | 34.9 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+pin_move | spread | 1-0 | 100.0 | 65.1 | 34.9 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_moving | spread | 1-0 | 100.0 | 34.9 | 65.1 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_value | total | 3-2 | 60.0 | 52.1 | 7.9 | +0.71 | 14.1 | -0.4 | 0.0 | keep collecting (5/30) |
| money_level+sharp_gap | total | 15-9 | 62.5 | 52.0 | 10.5 | +4.61 | 19.2 | -0.25 | 25.0 | keep collecting (24/30) |
| pin_value+sharp_gap | total | 5-2 | 71.4 | 50.5 | 20.9 | +2.48 | 35.5 | 0.0 | 14.3 | keep collecting (7/30) |
| money_level+pre_move | total | 1-2 | 33.3 | 48.8 | -15.5 | -1.13 | -37.7 | 1.0 | 33.3 | keep collecting (3/30) |
| pre_move+sharp_gap | total | 3-4 | 42.9 | 47.5 | -4.7 | -1.27 | -18.1 | -0.14 | 14.3 | redundant -- identical record to pre_move alone, not independent confirmation |
| pin_move+pin_value | total | 1-2 | 33.3 | 51.2 | -17.8 | -1.13 | -37.7 | 1.0 | 66.7 | keep collecting (3/30) |
| follow_move+money_level | total | 0-1 | 0.0 | 53.5 | -53.5 | -1.0 | -100.0 | -3.0 | 0.0 | redundant -- identical record to follow_move alone, not independent confirmation |
| money_level+money_moving | total | 3-1 | 75.0 | 51.7 | 23.3 | +1.75 | 43.7 | 0.0 | 25.0 | keep collecting (4/30) |
| money_moving+sharp_gap | total | 3-0 | 100.0 | 48.8 | 51.2 | +2.83 | 94.3 | -0.67 | 0.0 | keep collecting (3/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 46.5 | 53.5 | +0.93 | 92.6 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_move | total | 2-0 | 100.0 | 53.5 | 46.5 | +1.82 | 90.9 | 0.5 | 50.0 | keep collecting (2/30) |
| pin_move+sharp_gap | total | 3-0 | 100.0 | 51.2 | 48.8 | +2.69 | 89.6 | 1.0 | 66.7 | keep collecting (3/30) |
| money_moving+pre_move | total | 1-0 | 100.0 | 46.5 | 53.5 | +0.95 | 95.2 | -2.0 | 0.0 | keep collecting (1/30) |
| pin_value+pre_move | total | 1-0 | 100.0 | 46.5 | 53.5 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |

## CLOSE  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 6-28 | 17.6 | 35.0 | -17.3 | -21.58 | -63.5 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| pin_move | both | 39-34 | 53.4 | 51.5 | 1.9 | -3.41 | -4.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | both | 11-26 | 29.7 | 36.1 | -6.4 | -14.02 | -37.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm | both | 5-10 | 33.3 | 31.6 | 1.7 | -5.07 | -33.8 |  |  | keep collecting (15/30) |
| pre_move | both | 3-8 | 27.3 | 38.3 | -11.0 | -3.38 | -30.8 |  |  | keep collecting (11/30) |
| follow_move | both | 61-65 | 48.4 | 50.5 | -2.1 | -14.38 | -11.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm | both | 9-32 | 22.0 | 34.5 | -12.5 | -21.77 | -53.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio | both | 6-14 | 30.0 | 33.3 | -3.3 | -7.17 | -35.9 |  |  | keep collecting (20/30) |
| money_level | both | 83-43 | 65.9 | 61.5 | 4.4 | +17.15 | 13.6 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 59-66 | 47.2 | 48.5 | -1.3 | -15.68 | -12.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | both | 39-58 | 40.2 | 44.2 | -4.0 | -24.61 | -25.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | both | 61-45 | 57.5 | 49.1 | 8.4 | +7.48 | 7.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | both | 5-1 | 83.3 | 64.7 | 18.6 | +2.86 | 47.7 |  |  | keep collecting (6/30) |
| consensus_gap | both | 18-33 | 35.3 | 30.1 | 5.2 | -12.67 | -24.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm | both | 9-32 | 22.0 | 34.5 | -12.5 | -21.77 | -53.1 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | both | 6-28 | 17.6 | 35.0 | -17.3 | -21.58 | -63.5 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 6-14 | 30.0 | 33.3 | -3.3 | -7.17 | -35.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 25-29 | 46.3 | 48.5 | -2.2 | -7.35 | -13.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | both | 16-6 | 72.7 | 57.7 | 15.0 | +7.86 | 35.7 |  |  | keep collecting (22/30) |
| rlm+rlm_quiet | both | 6-27 | 18.2 | 34.0 | -15.9 | -20.58 | -62.4 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| rlm+rlm_ratio | both | 6-14 | 30.0 | 33.3 | -3.3 | -7.17 | -35.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 7-19 | 26.9 | 35.0 | -8.1 | -11.3 | -43.5 |  |  | keep collecting (26/30) |
| rlm_quiet+rlm_ratio | both | 3-10 | 23.1 | 32.4 | -9.3 | -6.98 | -53.7 |  |  | keep collecting (13/30) |
| rlm_quiet+sharp_gap | both | 4-14 | 22.2 | 34.4 | -12.1 | -10.11 | -56.2 |  |  | keep collecting (18/30) |
| rlm_ratio+sharp_gap | both | 6-14 | 30.0 | 33.3 | -3.3 | -7.17 | -35.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 42-26 | 61.8 | 59.1 | 2.7 | +5.68 | 8.4 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_level | both | 7-1 | 87.5 | 55.5 | 32.0 | +4.86 | 60.7 |  |  | keep collecting (8/30) |
| pre_move+sharp_gap | both | 3-8 | 27.3 | 38.3 | -11.0 | -3.38 | -30.8 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+money_level | both | 31-15 | 67.4 | 64.2 | 3.2 | +6.66 | 14.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| book_lag+money_level | both | 2-1 | 66.7 | 74.4 | -7.8 | +0.4 | 13.4 |  |  | keep collecting (3/30) |
| consensus_gap+pre_move | both | 1-2 | 33.3 | 20.9 | 12.4 | +0.9 | 30.0 |  |  | keep collecting (3/30) |
| consensus_gap+sharp_gap | both | 9-15 | 37.5 | 29.4 | 8.1 | -3.85 | -16.0 |  |  | keep collecting (24/30) |
| follow_move+pin_value | both | 12-7 | 63.2 | 51.7 | 11.5 | +3.27 | 17.2 |  |  | keep collecting (19/30) |
| pin_value+rlm | both | 2-6 | 25.0 | 40.1 | -15.1 | -4.26 | -53.2 |  |  | keep collecting (8/30) |
| pin_value+rlm_quiet | both | 2-6 | 25.0 | 40.1 | -15.1 | -4.26 | -53.2 |  |  | keep collecting (8/30) |
| pin_value+pre_move | both | 1-1 | 50.0 | 33.7 | 16.3 | -0.15 | -7.7 |  |  | keep collecting (2/30) |
| pin_value+sharp_gap | both | 17-12 | 58.6 | 47.0 | 11.6 | +2.36 | 8.1 |  |  | keep collecting (29/30) |
| consensus_gap+follow_move | both | 6-15 | 28.6 | 28.6 | -0.0 | -7.66 | -36.5 |  |  | keep collecting (21/30) |
| consensus_gap+rlm | both | 4-15 | 21.1 | 23.3 | -2.2 | -9.2 | -48.4 |  |  | keep collecting (19/30) |
| consensus_gap+rlm_quiet | both | 2-14 | 12.5 | 23.7 | -11.2 | -11.1 | -69.4 |  |  | keep collecting (16/30) |
| consensus_gap+pin_value | both | 3-7 | 30.0 | 23.7 | 6.3 | -4.42 | -44.2 |  |  | keep collecting (10/30) |
| book_lag+consensus_gap | both | 3-0 | 100.0 | 55.0 | 45.0 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| book_lag+money_moving | both | 1-0 | 100.0 | 34.9 | 65.1 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | both | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | both | 7-15 | 31.8 | 24.2 | 7.6 | -6.73 | -30.6 |  |  | keep collecting (22/30) |
| money_moving+pin_value | both | 11-10 | 52.4 | 45.5 | 6.9 | -0.75 | -3.6 |  |  | keep collecting (21/30) |
| money_moving+pre_move | both | 1-3 | 25.0 | 37.8 | -12.8 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| money_moving+sharp_gap | both | 27-39 | 40.9 | 43.8 | -2.9 | -14.57 | -22.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_moving | both | 17-29 | 37.0 | 45.2 | -8.2 | -13.97 | -30.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm | both | 6-22 | 21.4 | 33.2 | -11.8 | -15.17 | -54.2 |  |  | keep collecting (28/30) |
| money_moving+rlm_quiet | both | 3-17 | 15.0 | 32.0 | -17.0 | -13.98 | -69.9 |  |  | keep collecting (20/30) |
| money_level+money_moving | both | 26-15 | 63.4 | 58.1 | 5.3 | +5.25 | 12.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | both | 26-10 | 72.2 | 64.4 | 7.8 | +7.74 | 21.5 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+pin_move | both | 20-23 | 46.5 | 46.8 | -0.3 | -6.36 | -14.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_value | both | 12-10 | 54.5 | 47.8 | 6.8 | +0.27 | 1.2 |  |  | keep collecting (22/30) |
| pin_move+sharp_gap | both | 21-21 | 50.0 | 48.2 | 1.8 | -3.25 | -7.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_move | both | 5-8 | 38.5 | 28.8 | 9.7 | -2.53 | -19.4 |  |  | keep collecting (13/30) |
| consensus_gap+money_delta | both | 4-5 | 44.4 | 20.9 | 23.5 | +0.6 | 6.7 |  |  | keep collecting (9/30) |
| consensus_gap+pin_rlm | both | 2-6 | 25.0 | 20.9 | 4.1 | -3.76 | -47.0 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_ratio | both | 3-6 | 33.3 | 20.9 | 12.4 | -1.86 | -20.7 |  |  | keep collecting (9/30) |
| follow_move+money_delta | both | 6-13 | 31.6 | 33.7 | -2.1 | -6.04 | -31.8 |  |  | keep collecting (19/30) |
| follow_move+pin_rlm | both | 5-10 | 33.3 | 31.6 | 1.7 | -5.07 | -33.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+money_level | both | 3-5 | 37.5 | 37.5 | 0.0 | -1.76 | -22.0 |  |  | keep collecting (8/30) |
| money_delta+money_moving | both | 11-23 | 32.4 | 35.9 | -3.6 | -11.02 | -32.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_rlm | both | 4-8 | 33.3 | 32.2 | 1.2 | -3.94 | -32.9 |  |  | keep collecting (12/30) |
| money_delta+rlm | both | 5-11 | 31.2 | 32.7 | -1.5 | -5.04 | -31.5 |  |  | keep collecting (16/30) |
| money_delta+rlm_ratio | both | 5-9 | 35.7 | 31.6 | 4.2 | -3.04 | -21.7 |  |  | keep collecting (14/30) |
| money_delta+sharp_gap | both | 10-22 | 31.2 | 35.2 | -4.0 | -10.97 | -34.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_rlm | both | 0-3 | 0.0 | 40.3 | -40.3 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_level+rlm | both | 0-3 | 0.0 | 40.3 | -40.3 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_level+rlm_ratio | both | 0-3 | 0.0 | 40.3 | -40.3 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | both | 5-10 | 33.3 | 31.6 | 1.7 | -5.07 | -33.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | both | 6-12 | 33.3 | 31.4 | 1.9 | -5.17 | -28.7 |  |  | keep collecting (18/30) |
| pin_rlm+rlm | both | 5-10 | 33.3 | 31.6 | 1.7 | -5.07 | -33.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | both | 5-10 | 33.3 | 31.6 | 1.7 | -5.07 | -33.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 5-10 | 33.3 | 31.6 | 1.7 | -5.07 | -33.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+pin_move | both | 32-28 | 53.3 | 52.1 | 1.2 | -3.65 | -6.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_quiet | both | 5-18 | 21.7 | 36.6 | -14.9 | -12.45 | -54.1 |  |  | keep collecting (23/30) |
| money_delta+pin_move | both | 6-11 | 35.3 | 37.8 | -2.5 | -5.11 | -30.1 |  |  | keep collecting (17/30) |
| money_delta+pin_value | both | 1-5 | 16.7 | 37.2 | -20.5 | -4.17 | -69.5 |  |  | keep collecting (6/30) |
| money_delta+rlm_quiet | both | 2-6 | 25.0 | 29.1 | -4.1 | -3.85 | -48.1 |  |  | keep collecting (8/30) |
| pin_move+pin_rlm | both | 5-8 | 38.5 | 33.3 | 5.2 | -3.07 | -23.6 |  |  | keep collecting (13/30) |
| pin_move+rlm | both | 7-20 | 25.9 | 36.7 | -10.8 | -12.54 | -46.5 |  |  | keep collecting (27/30) |
| pin_move+rlm_ratio | both | 5-8 | 38.5 | 33.3 | 5.2 | -3.07 | -23.6 |  |  | keep collecting (13/30) |
| pin_rlm+pin_value | both | 1-3 | 25.0 | 33.7 | -8.7 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| pin_rlm+rlm_quiet | both | 3-7 | 30.0 | 28.6 | 1.4 | -3.98 | -39.8 |  |  | keep collecting (10/30) |
| pin_value+rlm_ratio | both | 1-3 | 25.0 | 33.7 | -8.7 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| money_delta+pre_move | both | 1-2 | 33.3 | 34.9 | -1.6 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| money_level+pre_move | both | 1-1 | 50.0 | 34.9 | 15.1 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| rlm_quiet | moneyline | 2-15 | 11.8 | 20.9 | -9.2 | -12.1 | -71.2 |  |  | keep collecting (17/30) |
| rlm_quiet | spread | 1-9 | 10.0 | 50.0 | -40.0 | -8.13 | -81.3 |  |  | keep collecting (10/30) |
| rlm_quiet | total | 3-4 | 42.9 | 47.5 | -4.7 | -1.35 | -19.3 |  |  | keep collecting (7/30) |
| pin_move | moneyline | 15-11 | 57.7 | 50.0 | 7.7 | -2.08 | -8.0 |  |  | keep collecting (26/30) |
| pin_move | spread | 8-10 | 44.4 | 55.0 | -10.6 | -2.75 | -15.3 |  |  | keep collecting (18/30) |
| pin_move | total | 14-13 | 51.9 | 50.6 | 1.2 | -0.31 | -1.1 |  |  | keep collecting (27/30) |
| pin_move | tt_away | 1-0 | 100.0 | 51.2 | 48.8 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| pin_move | tt_home | 1-0 | 100.0 | 51.2 | 48.8 | +0.89 | 88.5 |  |  | keep collecting (1/30) |
| money_delta | moneyline | 4-5 | 44.4 | 20.9 | 23.5 | +0.6 | 6.7 |  |  | keep collecting (9/30) |
| money_delta | spread | 3-14 | 17.6 | 36.7 | -19.0 | -11.3 | -66.5 |  |  | keep collecting (17/30) |
| money_delta | total | 4-7 | 36.4 | 47.8 | -11.4 | -3.32 | -30.2 |  |  | keep collecting (11/30) |
| pin_rlm | moneyline | 2-7 | 22.2 | 20.9 | 1.3 | -4.76 | -52.9 |  |  | keep collecting (9/30) |
| pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm | total | 3-1 | 75.0 | 46.5 | 28.5 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| pre_move | moneyline | 1-3 | 25.0 | 35.5 | -10.5 | -0.1 | -2.5 |  |  | keep collecting (4/30) |
| pre_move | spread | 1-3 | 25.0 | 34.9 | -9.9 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| pre_move | total | 1-2 | 33.3 | 46.5 | -13.2 | -1.15 | -38.4 |  |  | keep collecting (3/30) |
| follow_move | moneyline | 17-18 | 48.6 | 45.8 | 2.7 | -7.12 | -20.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | spread | 16-21 | 43.2 | 55.3 | -12.1 | -6.32 | -17.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | total | 10-9 | 52.6 | 50.2 | 2.4 | +0.15 | 0.8 |  |  | keep collecting (19/30) |
| follow_move | tt_away | 9-7 | 56.2 | 50.3 | 6.0 | +0.96 | 6.0 |  |  | keep collecting (16/30) |
| follow_move | tt_home | 9-10 | 47.4 | 50.3 | -2.9 | -2.04 | -10.7 |  |  | keep collecting (19/30) |
| rlm | moneyline | 4-16 | 20.0 | 20.9 | -0.9 | -10.2 | -51.0 |  |  | keep collecting (20/30) |
| rlm | spread | 1-11 | 8.3 | 47.5 | -39.1 | -10.13 | -84.4 |  |  | keep collecting (12/30) |
| rlm | total | 4-5 | 44.4 | 47.3 | -2.8 | -1.44 | -16.0 |  |  | keep collecting (9/30) |
| rlm_ratio | moneyline | 3-7 | 30.0 | 20.9 | 9.1 | -2.86 | -28.6 |  |  | keep collecting (10/30) |
| rlm_ratio | spread | 0-6 | 0.0 | 45.0 | -45.0 | -6.0 | -100.0 |  |  | keep collecting (6/30) |
| rlm_ratio | total | 3-1 | 75.0 | 46.5 | 28.5 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| money_level | moneyline | 35-7 | 83.3 | 74.9 | 8.4 | +9.37 | 22.3 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level | spread | 25-17 | 59.5 | 56.5 | 3.0 | +5.63 | 13.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | total | 23-19 | 54.8 | 53.0 | 1.8 | +2.16 | 5.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 21-19 | 52.5 | 50.0 | 2.5 | -2.79 | -7.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | spread | 17-25 | 40.5 | 45.0 | -4.5 | -9.91 | -23.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| sharp_gap | total | 21-22 | 48.8 | 50.6 | -1.7 | -2.97 | -6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | moneyline | 14-19 | 42.4 | 38.5 | 3.9 | -8.21 | -24.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | spread | 10-21 | 32.3 | 43.7 | -11.4 | -12.09 | -39.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | total | 15-18 | 45.5 | 50.3 | -4.9 | -4.32 | -13.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | moneyline | 2-7 | 22.2 | 27.4 | -5.2 | -5.59 | -62.2 |  |  | keep collecting (9/30) |
| pin_value | spread | 16-3 | 84.2 | 55.6 | 28.6 | +10.95 | 57.6 |  |  | keep collecting (19/30) |
| pin_value | total | 12-11 | 52.2 | 50.2 | 2.0 | -0.51 | -2.2 |  |  | keep collecting (23/30) |
| pin_value | tt_away | 14-12 | 53.8 | 49.9 | 3.9 | +0.14 | 0.6 |  |  | keep collecting (26/30) |
| pin_value | tt_home | 17-12 | 58.6 | 50.2 | 8.4 | +2.5 | 8.6 |  |  | keep collecting (29/30) |
| book_lag | moneyline | 1-1 | 50.0 | 79.1 | -29.1 | -0.43 | -21.6 |  |  | keep collecting (2/30) |
| book_lag | spread | 4-0 | 100.0 | 57.6 | 42.4 | +3.29 | 82.4 |  |  | keep collecting (4/30) |
| consensus_gap | moneyline | 13-30 | 30.2 | 26.3 | 3.9 | -13.79 | -32.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 5-3 | 62.5 | 50.0 | 12.5 | +1.13 | 14.1 |  |  | keep collecting (8/30) |
| consensus_gap+money_level | moneyline | 6-1 | 85.7 | 54.2 | 31.6 | +4.02 | 57.5 |  |  | keep collecting (7/30) |
| pre_move+sharp_gap | moneyline | 1-3 | 25.0 | 35.5 | -10.5 | -0.1 | -2.5 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| book_lag+money_level | moneyline | 1-1 | 50.0 | 79.1 | -29.1 | -0.43 | -21.6 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pre_move | moneyline | 1-2 | 33.3 | 20.9 | 12.4 | +0.9 | 30.0 |  |  | keep collecting (3/30) |
| consensus_gap+sharp_gap | moneyline | 8-14 | 36.4 | 28.9 | 7.5 | -3.68 | -16.7 |  |  | keep collecting (22/30) |
| money_level+sharp_gap | moneyline | 17-4 | 81.0 | 73.5 | 7.4 | +5.17 | 24.6 |  |  | keep collecting (21/30) |
| consensus_gap+follow_move | moneyline | 6-14 | 30.0 | 26.7 | 3.3 | -6.66 | -33.3 |  |  | keep collecting (20/30) |
| consensus_gap+rlm | moneyline | 4-14 | 22.2 | 20.9 | 1.3 | -8.2 | -45.6 |  |  | keep collecting (18/30) |
| consensus_gap+rlm_quiet | moneyline | 2-13 | 13.3 | 20.9 | -7.6 | -10.1 | -67.3 |  |  | keep collecting (15/30) |
| follow_move+rlm | moneyline | 4-16 | 20.0 | 20.9 | -0.9 | -10.2 | -51.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | moneyline | 2-15 | 11.8 | 20.9 | -9.2 | -12.1 | -71.2 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm+rlm_quiet | moneyline | 2-15 | 11.8 | 20.9 | -9.2 | -12.1 | -71.2 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 1-7 | 12.5 | 20.9 | -8.4 | -6.04 | -75.5 |  |  | keep collecting (8/30) |
| pin_value+pre_move | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 1-5 | 16.7 | 30.6 | -14.0 | -4.56 | -75.9 |  |  | keep collecting (6/30) |
| follow_move+money_level | moneyline | 13-2 | 86.7 | 75.2 | 11.5 | +3.08 | 20.5 |  |  | keep collecting (15/30) |
| follow_move+sharp_gap | moneyline | 9-8 | 52.9 | 44.9 | 8.1 | -0.89 | -5.3 |  |  | keep collecting (17/30) |
| follow_move+money_moving | moneyline | 8-12 | 40.0 | 38.4 | 1.6 | -5.33 | -26.7 |  |  | keep collecting (20/30) |
| money_moving+rlm | moneyline | 3-11 | 21.4 | 20.9 | 0.5 | -6.86 | -49.0 |  |  | keep collecting (14/30) |
| money_moving+rlm_quiet | moneyline | 1-10 | 9.1 | 20.9 | -11.8 | -8.76 | -79.6 |  |  | keep collecting (11/30) |
| consensus_gap+money_moving | moneyline | 6-15 | 28.6 | 23.7 | 4.9 | -7.51 | -35.8 |  |  | keep collecting (21/30) |
| consensus_gap+pin_move | moneyline | 5-7 | 41.7 | 25.8 | 15.9 | -1.53 | -12.7 |  |  | keep collecting (12/30) |
| money_moving+pin_move | moneyline | 7-6 | 53.8 | 38.8 | 15.0 | -1.2 | -9.2 |  |  | keep collecting (13/30) |
| money_moving+pin_value | moneyline | 2-4 | 33.3 | 30.6 | 2.7 | -2.59 | -43.2 |  |  | keep collecting (6/30) |
| pin_move+pin_value | moneyline | 2-3 | 40.0 | 32.6 | 7.4 | -1.59 | -31.9 |  |  | keep collecting (5/30) |
| consensus_gap+money_delta | moneyline | 4-5 | 44.4 | 20.9 | 23.5 | +0.6 | 6.7 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| consensus_gap+pin_rlm | moneyline | 2-6 | 25.0 | 20.9 | 4.1 | -3.76 | -47.0 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_ratio | moneyline | 3-6 | 33.3 | 20.9 | 12.4 | -1.86 | -20.7 |  |  | keep collecting (9/30) |
| follow_move+money_delta | moneyline | 3-5 | 37.5 | 20.9 | 16.6 | -0.86 | -10.7 |  |  | keep collecting (8/30) |
| follow_move+pin_rlm | moneyline | 2-7 | 22.2 | 20.9 | 1.3 | -4.76 | -52.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 3-7 | 30.0 | 20.9 | 9.1 | -2.86 | -28.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | moneyline | 1-1 | 50.0 | 20.9 | 29.1 | +0.46 | 23.0 |  |  | keep collecting (2/30) |
| money_delta+money_moving | moneyline | 4-5 | 44.4 | 20.9 | 23.5 | +0.6 | 6.7 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_rlm | moneyline | 2-5 | 28.6 | 20.9 | 7.6 | -2.76 | -39.4 |  |  | keep collecting (7/30) |
| money_delta+rlm | moneyline | 3-5 | 37.5 | 20.9 | 16.6 | -0.86 | -10.7 |  |  | keep collecting (8/30) |
| money_delta+rlm_ratio | moneyline | 3-5 | 37.5 | 20.9 | 16.6 | -0.86 | -10.7 |  |  | keep collecting (8/30) |
| money_delta+sharp_gap | moneyline | 4-5 | 44.4 | 20.9 | 23.5 | +0.6 | 6.7 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+money_moving | moneyline | 10-2 | 83.3 | 69.4 | 14.0 | +3.69 | 30.8 |  |  | keep collecting (12/30) |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+rlm | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+rlm_ratio | moneyline | 0-1 | 0.0 | 20.9 | -20.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 2-7 | 22.2 | 20.9 | 1.3 | -4.76 | -52.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | moneyline | 3-7 | 30.0 | 20.9 | 9.1 | -2.86 | -28.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+sharp_gap | moneyline | 10-12 | 45.5 | 39.4 | 6.0 | -2.97 | -13.5 |  |  | keep collecting (22/30) |
| pin_rlm+rlm | moneyline | 2-7 | 22.2 | 20.9 | 1.3 | -4.76 | -52.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | moneyline | 2-7 | 22.2 | 20.9 | 1.3 | -4.76 | -52.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 2-7 | 22.2 | 20.9 | 1.3 | -4.76 | -52.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm+rlm_ratio | moneyline | 3-7 | 30.0 | 20.9 | 9.1 | -2.86 | -28.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | moneyline | 3-7 | 30.0 | 20.9 | 9.1 | -2.86 | -28.6 |  |  | keep collecting (10/30) |
| rlm_ratio+sharp_gap | moneyline | 3-7 | 30.0 | 20.9 | 9.1 | -2.86 | -28.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_move | moneyline | 14-9 | 60.9 | 51.3 | 9.6 | -1.04 | -4.5 |  |  | keep collecting (23/30) |
| follow_move+pin_value | moneyline | 1-3 | 25.0 | 35.5 | -10.5 | -2.56 | -63.9 |  |  | keep collecting (4/30) |
| money_delta+pin_move | moneyline | 2-3 | 40.0 | 20.9 | 19.1 | -0.76 | -15.2 |  |  | keep collecting (5/30) |
| money_delta+pin_value | moneyline | 0-2 | 0.0 | 20.9 | -20.9 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_delta+rlm_quiet | moneyline | 1-4 | 20.0 | 20.9 | -0.9 | -2.76 | -55.2 |  |  | keep collecting (5/30) |
| pin_move+pin_rlm | moneyline | 2-5 | 28.6 | 20.9 | 7.6 | -2.76 | -39.4 |  |  | keep collecting (7/30) |
| pin_move+rlm | moneyline | 3-8 | 27.3 | 20.9 | 6.3 | -4.1 | -37.3 |  |  | keep collecting (11/30) |
| pin_move+rlm_quiet | moneyline | 2-8 | 20.0 | 20.9 | -0.9 | -5.1 | -51.0 |  |  | keep collecting (10/30) |
| pin_move+rlm_ratio | moneyline | 2-5 | 28.6 | 20.9 | 7.6 | -2.76 | -39.4 |  |  | keep collecting (7/30) |
| pin_move+sharp_gap | moneyline | 6-5 | 54.5 | 42.1 | 12.5 | -0.81 | -7.4 |  |  | keep collecting (11/30) |
| pin_rlm+pin_value | moneyline | 0-2 | 0.0 | 20.9 | -20.9 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm+rlm_quiet | moneyline | 1-6 | 14.3 | 20.9 | -6.6 | -4.76 | -68.0 |  |  | keep collecting (7/30) |
| pin_value+rlm | moneyline | 0-3 | 0.0 | 20.9 | -20.9 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_value+rlm_quiet | moneyline | 0-3 | 0.0 | 20.9 | -20.9 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_value+rlm_ratio | moneyline | 0-2 | 0.0 | 20.9 | -20.9 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | moneyline | 1-6 | 14.3 | 20.9 | -6.6 | -4.76 | -68.0 |  |  | keep collecting (7/30) |
| rlm_quiet+sharp_gap | moneyline | 1-6 | 14.3 | 20.9 | -6.6 | -4.76 | -68.0 |  |  | keep collecting (7/30) |
| money_level+pin_move | moneyline | 11-1 | 91.7 | 79.1 | 12.6 | +3.06 | 25.5 |  |  | keep collecting (12/30) |
| money_level+pin_value | moneyline | 1-0 | 100.0 | 79.1 | 20.9 | +0.44 | 44.4 |  |  | keep collecting (1/30) |
| follow_move+rlm | spread | 1-11 | 8.3 | 47.5 | -39.1 | -10.13 | -84.4 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 1-9 | 10.0 | 50.0 | -40.0 | -8.13 | -81.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-6 | 0.0 | 45.0 | -45.0 | -6.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 9-14 | 39.1 | 50.7 | -11.5 | -5.83 | -25.3 |  |  | keep collecting (23/30) |
| money_level+pin_value | spread | 9-2 | 81.8 | 59.6 | 22.2 | +6.09 | 55.4 |  |  | keep collecting (11/30) |
| rlm+rlm_quiet | spread | 1-8 | 11.1 | 48.3 | -37.2 | -7.13 | -79.2 |  |  | keep collecting (9/30) |
| rlm+rlm_ratio | spread | 0-6 | 0.0 | 45.0 | -45.0 | -6.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 0-9 | 0.0 | 41.6 | -41.6 | -9.0 | -100.0 |  |  | keep collecting (9/30) |
| rlm_quiet+rlm_ratio | spread | 0-3 | 0.0 | 45.0 | -45.0 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| rlm_quiet+sharp_gap | spread | 0-6 | 0.0 | 39.9 | -39.9 | -6.0 | -100.0 |  |  | keep collecting (6/30) |
| rlm_ratio+sharp_gap | spread | 0-6 | 0.0 | 45.0 | -45.0 | -6.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 12-10 | 54.5 | 61.0 | -6.4 | +1.0 | 4.5 |  |  | keep collecting (22/30) |
| follow_move+pin_value | spread | 7-1 | 87.5 | 61.3 | 26.2 | +5.19 | 64.9 |  |  | keep collecting (8/30) |
| pin_value+rlm | spread | 1-0 | 100.0 | 65.1 | 34.9 | +0.87 | 87.0 |  |  | keep collecting (1/30) |
| pin_value+rlm_quiet | spread | 1-0 | 100.0 | 65.1 | 34.9 | +0.87 | 87.0 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | spread | 11-10 | 52.4 | 52.2 | 0.2 | -0.23 | -1.1 |  |  | keep collecting (21/30) |
| consensus_gap+sharp_gap | spread | 1-1 | 50.0 | 34.9 | 15.1 | -0.17 | -8.4 |  |  | keep collecting (2/30) |
| book_lag+consensus_gap | spread | 3-0 | 100.0 | 55.0 | 45.0 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| pin_value+sharp_gap | spread | 8-1 | 88.9 | 51.7 | 37.2 | +5.91 | 65.7 |  |  | keep collecting (9/30) |
| book_lag+money_moving | spread | 1-0 | 100.0 | 34.9 | 65.1 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | spread | 1-0 | 100.0 | 34.9 | 65.1 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| consensus_gap+pin_value | spread | 2-0 | 100.0 | 34.9 | 65.1 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| money_moving+pin_value | spread | 5-0 | 100.0 | 53.0 | 47.0 | +4.34 | 86.8 |  |  | keep collecting (5/30) |
| follow_move+pin_move | spread | 6-10 | 37.5 | 55.7 | -18.2 | -4.49 | -28.1 |  |  | keep collecting (16/30) |
| money_level+money_moving | spread | 7-6 | 53.8 | 53.5 | 0.4 | +0.3 | 2.3 |  |  | keep collecting (13/30) |
| money_moving+sharp_gap | spread | 7-15 | 31.8 | 41.8 | -9.9 | -8.65 | -39.3 |  |  | keep collecting (22/30) |
| pin_move+rlm_quiet | spread | 0-6 | 0.0 | 50.0 | -50.0 | -6.0 | -100.0 |  |  | keep collecting (6/30) |
| money_delta+money_moving | spread | 3-12 | 20.0 | 36.9 | -16.9 | -9.3 | -62.0 |  |  | keep collecting (15/30) |
| money_delta+sharp_gap | spread | 3-12 | 20.0 | 36.9 | -16.9 | -9.3 | -62.0 |  |  | keep collecting (15/30) |
| money_delta+money_level | spread | 1-4 | 20.0 | 40.9 | -20.9 | -3.13 | -62.6 |  |  | keep collecting (5/30) |
| money_delta+pre_move | spread | 1-2 | 33.3 | 34.9 | -1.6 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| money_level+pre_move | spread | 1-1 | 50.0 | 34.9 | 15.1 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| money_moving+pre_move | spread | 1-2 | 33.3 | 34.9 | -1.6 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| pre_move+sharp_gap | spread | 1-3 | 25.0 | 34.9 | -9.9 | -2.13 | -53.2 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+money_moving | spread | 3-10 | 23.1 | 51.2 | -28.1 | -7.18 | -55.2 |  |  | keep collecting (13/30) |
| money_moving+pin_move | spread | 3-7 | 30.0 | 50.0 | -20.0 | -4.26 | -42.6 |  |  | keep collecting (10/30) |
| money_moving+rlm | spread | 0-7 | 0.0 | 43.5 | -43.5 | -7.0 | -100.0 |  |  | keep collecting (7/30) |
| money_moving+rlm_quiet | spread | 0-4 | 0.0 | 42.4 | -42.4 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| pin_move+rlm | spread | 0-7 | 0.0 | 47.8 | -47.8 | -7.0 | -100.0 |  |  | keep collecting (7/30) |
| pin_move+sharp_gap | spread | 5-7 | 41.7 | 50.0 | -8.3 | -2.48 | -20.7 |  |  | keep collecting (12/30) |
| follow_move+money_delta | spread | 1-5 | 16.7 | 39.9 | -23.3 | -4.0 | -66.7 |  |  | keep collecting (6/30) |
| follow_move+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+pin_move | spread | 2-3 | 40.0 | 40.9 | -0.9 | -1.17 | -23.3 |  |  | keep collecting (5/30) |
| money_delta+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+rlm | spread | 0-4 | 0.0 | 42.4 | -42.4 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| money_delta+rlm_ratio | spread | 0-3 | 0.0 | 45.0 | -45.0 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_level+pin_move | spread | 6-4 | 60.0 | 62.1 | -2.1 | +1.42 | 14.2 |  |  | keep collecting (10/30) |
| money_level+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_moving+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-4 | 0.0 | 42.4 | -42.4 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| pin_move+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm+rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+rlm_quiet | spread | 0-1 | 0.0 | 34.9 | -34.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+follow_move | spread | 0-1 | 0.0 | 65.1 | -65.1 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+pin_move | spread | 0-1 | 0.0 | 65.1 | -65.1 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+rlm | spread | 0-1 | 0.0 | 65.1 | -65.1 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 0-1 | 0.0 | 65.1 | -65.1 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta+pin_value | spread | 1-0 | 100.0 | 34.9 | 65.1 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| pin_move+pin_value | spread | 4-0 | 100.0 | 57.6 | 42.4 | +3.52 | 88.0 |  |  | keep collecting (4/30) |
| book_lag+money_level | spread | 1-0 | 100.0 | 65.1 | 34.9 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| consensus_gap+money_level | spread | 1-0 | 100.0 | 65.1 | 34.9 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | total | 14-12 | 53.8 | 53.0 | 0.9 | +0.75 | 2.9 |  |  | keep collecting (26/30) |
| pin_value+pre_move | total | 1-0 | 100.0 | 46.5 | 53.5 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| pin_value+sharp_gap | total | 8-6 | 57.1 | 51.0 | 6.1 | +1.0 | 7.2 |  |  | keep collecting (14/30) |
| pre_move+sharp_gap | total | 1-2 | 33.3 | 46.5 | -13.2 | -1.15 | -38.4 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| money_level+pin_value | total | 6-4 | 60.0 | 53.5 | 6.5 | +1.33 | 13.3 |  |  | keep collecting (10/30) |
| money_moving+pre_move | total | 0-1 | 0.0 | 46.5 | -46.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+sharp_gap | total | 10-12 | 45.5 | 50.3 | -4.9 | -2.96 | -13.5 |  |  | keep collecting (22/30) |
| money_level+money_moving | total | 9-7 | 56.2 | 53.5 | 2.8 | +1.26 | 7.9 |  |  | keep collecting (16/30) |
| money_level+pin_move | total | 9-5 | 64.3 | 53.5 | 10.8 | +3.26 | 23.3 |  |  | keep collecting (14/30) |
| money_moving+pin_move | total | 10-10 | 50.0 | 50.3 | -0.3 | -0.91 | -4.5 |  |  | keep collecting (20/30) |
| money_moving+pin_value | total | 4-6 | 40.0 | 50.7 | -10.7 | -2.5 | -25.0 |  |  | keep collecting (10/30) |
| pin_move+pin_value | total | 5-7 | 41.7 | 50.6 | -8.9 | -2.54 | -21.2 |  |  | keep collecting (12/30) |
| pin_move+sharp_gap | total | 10-9 | 52.6 | 50.6 | 2.1 | +0.04 | 0.2 |  |  | keep collecting (19/30) |
| money_delta+money_level | total | 1-0 | 100.0 | 53.5 | 46.5 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+money_moving | total | 4-6 | 40.0 | 47.9 | -7.9 | -2.32 | -23.2 |  |  | keep collecting (10/30) |
| money_delta+sharp_gap | total | 3-5 | 37.5 | 48.3 | -10.8 | -2.27 | -28.4 |  |  | keep collecting (8/30) |
| follow_move+money_delta | total | 2-3 | 40.0 | 46.5 | -6.5 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| follow_move+money_moving | total | 6-7 | 46.2 | 49.7 | -3.6 | -1.45 | -11.2 |  |  | keep collecting (13/30) |
| follow_move+pin_move | total | 10-9 | 52.6 | 50.2 | 2.4 | +0.15 | 0.8 |  |  | redundant -- identical record to follow_move alone, not independent confirmation |
| follow_move+pin_rlm | total | 3-1 | 75.0 | 46.5 | 28.5 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+pin_value | total | 2-3 | 40.0 | 49.3 | -9.3 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| follow_move+rlm | total | 4-5 | 44.4 | 47.3 | -2.8 | -1.44 | -16.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | total | 3-4 | 42.9 | 47.5 | -4.7 | -1.35 | -19.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 3-1 | 75.0 | 46.5 | 28.5 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 7-7 | 50.0 | 49.5 | 0.5 | -0.63 | -4.5 |  |  | keep collecting (14/30) |
| money_delta+pin_move | total | 2-5 | 28.6 | 47.5 | -18.9 | -3.18 | -45.5 |  |  | keep collecting (7/30) |
| money_delta+pin_rlm | total | 2-1 | 66.7 | 46.5 | 20.2 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| money_delta+pin_value | total | 0-3 | 0.0 | 48.8 | -48.8 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_delta+rlm | total | 2-2 | 50.0 | 46.5 | 3.5 | -0.18 | -4.5 |  |  | keep collecting (4/30) |
| money_delta+rlm_quiet | total | 1-1 | 50.0 | 46.5 | 3.5 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_delta+rlm_ratio | total | 2-1 | 66.7 | 46.5 | 20.2 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | total | 3-1 | 75.0 | 46.5 | 28.5 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm | total | 3-4 | 42.9 | 47.5 | -4.7 | -1.31 | -18.7 |  |  | keep collecting (7/30) |
| money_moving+rlm_quiet | total | 2-3 | 40.0 | 47.9 | -7.9 | -1.22 | -24.4 |  |  | keep collecting (5/30) |
| money_moving+rlm_ratio | total | 3-1 | 75.0 | 46.5 | 28.5 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_move+pin_rlm | total | 3-1 | 75.0 | 46.5 | 28.5 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm | total | 4-5 | 44.4 | 47.3 | -2.8 | -1.44 | -16.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| pin_move+rlm_quiet | total | 3-4 | 42.9 | 47.5 | -4.7 | -1.35 | -19.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_ratio | total | 3-1 | 75.0 | 46.5 | 28.5 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+pin_value | total | 1-1 | 50.0 | 46.5 | 3.5 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| pin_rlm+rlm | total | 3-1 | 75.0 | 46.5 | 28.5 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | total | 2-1 | 66.7 | 46.5 | 20.2 | +0.78 | 26.0 |  |  | keep collecting (3/30) |
| pin_rlm+rlm_ratio | total | 3-1 | 75.0 | 46.5 | 28.5 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | total | 3-1 | 75.0 | 46.5 | 28.5 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm | total | 1-3 | 25.0 | 48.3 | -23.3 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| pin_value+rlm_quiet | total | 1-3 | 25.0 | 48.3 | -23.3 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| pin_value+rlm_ratio | total | 1-1 | 50.0 | 46.5 | 3.5 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| rlm+rlm_quiet | total | 3-4 | 42.9 | 47.5 | -4.7 | -1.35 | -19.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm+rlm_ratio | total | 3-1 | 75.0 | 46.5 | 28.5 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | total | 4-3 | 57.1 | 46.5 | 10.6 | +0.56 | 8.0 |  |  | keep collecting (7/30) |
| rlm_quiet+rlm_ratio | total | 2-1 | 66.7 | 46.5 | 20.2 | +0.78 | 26.0 |  |  | keep collecting (3/30) |
| rlm_quiet+sharp_gap | total | 3-2 | 60.0 | 46.5 | 13.5 | +0.65 | 13.0 |  |  | keep collecting (5/30) |
| rlm_ratio+sharp_gap | total | 3-1 | 75.0 | 46.5 | 28.5 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | total | 6-3 | 66.7 | 53.5 | 13.2 | +2.59 | 28.8 |  |  | keep collecting (9/30) |
| follow_move+pin_move | tt_away | 1-0 | 100.0 | 51.2 | 48.8 | +0.85 | 84.7 |  |  | redundant -- identical record to pin_move alone, not independent confirmation |
| follow_move+pin_move | tt_home | 1-0 | 100.0 | 51.2 | 48.8 | +0.89 | 88.5 |  |  | redundant -- identical record to pin_move alone, not independent confirmation |
| follow_move+pin_value | tt_home | 2-0 | 100.0 | 51.2 | 48.8 | +1.81 | 90.5 |  |  | keep collecting (2/30) |
| pin_move+pin_value | tt_home | 1-0 | 100.0 | 51.2 | 48.8 | +0.89 | 88.5 |  |  | redundant -- identical record to pin_move alone, not independent confirmation |

# Pooled (fit + forward together)

Kept for continuity with earlier runs. **This table is contaminated** — it
mixes the games the engine was built on with the games testing it. Use the
forward table for any decision.

## EARLY  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 3-8 | 27.3 | 45.5 | -18.2 | -5.33 | -48.5 | 0.05 | 18.2 | keep collecting (11/30) |
| pin_move | both | 21-19 | 52.5 | 61.2 | -8.7 | -5.13 | -12.8 | 0.75 | 55.0 | no edge shown yet |
| pin_rlm | both | 2-6 | 25.0 | 26.6 | -1.6 | -3.97 | -49.6 | -0.96 | 62.5 | keep collecting (8/30) |
| pre_move | both | 13-27 | 32.5 | 33.1 | -0.6 | -11.57 | -28.9 | -0.4 | 40.0 | DROP: below break-even |
| follow_move | both | 17-19 | 47.2 | 52.4 | -5.2 | -3.77 | -10.5 | -0.18 | 19.4 | no edge shown yet |
| rlm | both | 2-8 | 20.0 | 43.8 | -23.8 | -6.17 | -61.7 | 0.05 | 20.0 | keep collecting (10/30) |
| rlm_ratio | both | 1-2 | 33.3 | 46.1 | -12.7 | -1.17 | -38.9 | 0.0 | 0.0 | keep collecting (3/30) |
| money_level | both | 92-47 | 66.2 | 60.2 | 6.0 | +18.54 | 13.3 | -0.16 | 30.9 | PROMOTE: beats break-even and its own base rate |
| sharp_gap | both | 74-59 | 55.6 | 48.0 | 7.6 | +7.06 | 5.3 | -0.0 | 36.1 | no edge shown yet |
| money_moving | both | 15-9 | 62.5 | 52.0 | 10.5 | +3.38 | 14.1 | -0.03 | 33.3 | keep collecting (24/30) |
| pin_value | both | 41-37 | 52.6 | 48.6 | 3.9 | -1.36 | -1.7 | 0.19 | 30.8 | no edge shown yet |
| book_lag | both | 5-3 | 62.5 | 46.4 | 16.1 | +1.55 | 19.3 | -0.14 | 62.5 | keep collecting (8/30) |
| consensus_gap | both | 25-41 | 37.9 | 33.7 | 4.2 | -11.77 | -17.8 | -0.02 | 47.0 | DROP: below break-even |
| follow_move+rlm | both | 2-8 | 20.0 | 43.8 | -23.8 | -6.17 | -61.7 | 0.05 | 20.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | both | 3-8 | 27.3 | 45.5 | -18.2 | -5.33 | -48.5 | 0.05 | 18.2 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 1-2 | 33.3 | 46.1 | -12.7 | -1.17 | -38.9 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 13-8 | 61.9 | 53.9 | 8.0 | +4.01 | 19.1 | 0.07 | 23.8 | keep collecting (21/30) |
| rlm+rlm_quiet | both | 2-8 | 20.0 | 43.8 | -23.8 | -6.17 | -61.7 | 0.05 | 20.0 | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+rlm_ratio | both | 1-2 | 33.3 | 46.1 | -12.7 | -1.17 | -38.9 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 1-2 | 33.3 | 46.1 | -12.7 | -1.17 | -38.9 | 0.0 | 0.0 | keep collecting (3/30) |
| rlm_quiet+rlm_ratio | both | 1-2 | 33.3 | 46.1 | -12.7 | -1.17 | -38.9 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 1-2 | 33.3 | 46.1 | -12.7 | -1.17 | -38.9 | 0.0 | 0.0 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | both | 1-2 | 33.3 | 46.1 | -12.7 | -1.17 | -38.9 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_value | both | 15-6 | 71.4 | 56.7 | 14.7 | +7.3 | 34.8 | 0.17 | 28.6 | keep collecting (21/30) |
| money_level+sharp_gap | both | 53-24 | 68.8 | 57.2 | 11.7 | +18.61 | 24.2 | -0.13 | 31.2 | PROMOTE: beats break-even and its own base rate |
| pin_value+sharp_gap | both | 17-11 | 60.7 | 46.9 | 13.8 | +4.0 | 14.3 | 0.6 | 42.9 | keep collecting (28/30) |
| consensus_gap+pin_value | both | 6-12 | 33.3 | 40.9 | -7.6 | -6.96 | -38.6 | 0.81 | 50.0 | keep collecting (18/30) |
| money_level+pre_move | both | 2-4 | 33.3 | 41.2 | -7.9 | -2.22 | -37.0 | -1.6 | 16.7 | keep collecting (6/30) |
| pre_move+sharp_gap | both | 13-27 | 32.5 | 33.1 | -0.6 | -11.57 | -28.9 | -0.4 | 40.0 | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+pin_value | both | 6-2 | 75.0 | 58.9 | 16.1 | +3.21 | 40.1 | 0.25 | 25.0 | keep collecting (8/30) |
| consensus_gap+follow_move | both | 2-2 | 50.0 | 52.3 | -2.3 | -0.35 | -8.7 | 0.38 | 50.0 | keep collecting (4/30) |
| consensus_gap+money_level | both | 11-3 | 78.6 | 56.8 | 21.8 | +5.7 | 40.7 | -0.35 | 50.0 | keep collecting (14/30) |
| consensus_gap+sharp_gap | both | 17-24 | 41.5 | 34.0 | 7.5 | -5.2 | -12.7 | 0.05 | 53.7 | no edge shown yet |
| follow_move+money_level | both | 13-8 | 61.9 | 58.7 | 3.2 | +3.74 | 17.8 | -0.22 | 23.8 | keep collecting (21/30) |
| consensus_gap+pre_move | both | 6-18 | 25.0 | 23.6 | 1.4 | -8.9 | -37.1 | -0.61 | 45.8 | keep collecting (24/30) |
| follow_move+money_moving | both | 3-2 | 60.0 | 60.0 | 0.0 | +0.38 | 7.5 | -0.62 | 0.0 | keep collecting (5/30) |
| money_level+money_moving | both | 10-3 | 76.9 | 59.4 | 17.5 | +4.57 | 35.1 | -0.47 | 30.8 | keep collecting (13/30) |
| money_moving+pin_value | both | 5-2 | 71.4 | 47.5 | 23.9 | +2.56 | 36.6 | 1.0 | 42.9 | keep collecting (7/30) |
| money_moving+sharp_gap | both | 7-3 | 70.0 | 49.5 | 20.5 | +3.15 | 31.5 | 0.03 | 30.0 | keep collecting (10/30) |
| consensus_gap+rlm | both | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | both | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_value | both | 4-5 | 44.4 | 57.2 | -12.7 | -1.48 | -16.5 | 0.78 | 66.7 | keep collecting (9/30) |
| consensus_gap+pin_move | both | 1-3 | 25.0 | 42.7 | -17.7 | -2.13 | -53.2 | 0.15 | 75.0 | keep collecting (4/30) |
| pin_move+sharp_gap | both | 12-5 | 70.6 | 58.8 | 11.8 | +4.98 | 29.3 | 0.68 | 64.7 | keep collecting (17/30) |
| book_lag+consensus_gap | both | 3-2 | 60.0 | 34.2 | 25.8 | +1.29 | 25.8 | 0.68 | 80.0 | keep collecting (5/30) |
| money_level+pin_move | both | 19-6 | 76.0 | 67.3 | 8.7 | +6.05 | 24.2 | 0.89 | 56.0 | keep collecting (25/30) |
| money_moving+pin_move | both | 1-0 | 100.0 | 38.2 | 61.8 | +0.95 | 95.2 | -2.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+pin_rlm | both | 1-6 | 14.3 | 23.6 | -9.4 | -4.92 | -70.3 | -1.24 | 57.1 | keep collecting (7/30) |
| money_level+pin_rlm | both | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+pre_move | both | 2-6 | 25.0 | 26.6 | -1.6 | -3.97 | -49.6 | -0.96 | 62.5 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 2-6 | 25.0 | 26.6 | -1.6 | -3.97 | -49.6 | -0.96 | 62.5 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+money_level | both | 3-1 | 75.0 | 65.5 | 9.5 | +1.12 | 28.1 | -0.88 | 50.0 | keep collecting (4/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 42.7 | 7.3 | +0.08 | 4.0 | -0.05 | 50.0 | keep collecting (2/30) |
| book_lag+sharp_gap | both | 4-1 | 80.0 | 46.5 | 33.5 | +3.16 | 63.2 | 0.1 | 60.0 | keep collecting (5/30) |
| money_moving+rlm_quiet | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | both | 1-0 | 100.0 | 61.8 | 38.2 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_value+pre_move | both | 2-6 | 25.0 | 29.5 | -4.5 | -4.26 | -53.2 | 1.55 | 62.5 | keep collecting (8/30) |
| consensus_gap+money_moving | both | 2-1 | 66.7 | 28.5 | 38.2 | +0.95 | 31.7 | 2.63 | 100.0 | keep collecting (3/30) |
| money_moving+pre_move | both | 2-1 | 66.7 | 31.5 | 35.2 | +1.03 | 34.4 | 1.63 | 66.7 | keep collecting (3/30) |
| pin_rlm+pin_value | both | 0-2 | 0.0 | 23.6 | -23.6 | -2.0 | -100.0 | 0.9 | 50.0 | keep collecting (2/30) |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 23.6 | 76.4 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+pre_move | both | 2-0 | 100.0 | 23.6 | 76.4 | +2.42 | 121.0 | -0.25 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | both | 1-0 | 100.0 | 23.6 | 76.4 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| follow_move+pin_move | both | 3-5 | 37.5 | 61.8 | -24.3 | -2.19 | -27.3 | -0.25 | 25.0 | keep collecting (8/30) |
| money_moving+rlm | both | 0-1 | 0.0 | 38.2 | -38.2 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+rlm | both | 0-2 | 0.0 | 61.8 | -61.8 | -2.0 | -100.0 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_move+rlm_quiet | both | 0-2 | 0.0 | 61.8 | -61.8 | -2.0 | -100.0 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_move+pin_rlm | both | 1-1 | 50.0 | 35.5 | 14.5 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+pre_move | both | 1-1 | 50.0 | 35.5 | 14.5 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |
| book_lag+pin_move | both | 3-0 | 100.0 | 66.7 | 33.3 | +2.12 | 70.8 | -0.5 | 66.7 | keep collecting (3/30) |
| book_lag+pin_value | both | 2-0 | 100.0 | 61.8 | 38.2 | +1.74 | 87.0 | 1.5 | 100.0 | keep collecting (2/30) |
| rlm_quiet | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| rlm_quiet | spread | 3-7 | 30.0 | 47.6 | -17.6 | -4.33 | -43.3 | 0.0 | 10.0 | keep collecting (10/30) |
| pin_move | moneyline | 10-7 | 58.8 | 70.2 | -11.3 | -3.22 | -19.0 | 1.3 | 64.7 | keep collecting (17/30) |
| pin_move | spread | 6-5 | 54.5 | 59.7 | -5.1 | +0.5 | 4.6 | -0.09 | 36.4 | keep collecting (11/30) |
| pin_move | total | 5-7 | 41.7 | 50.0 | -8.3 | -2.41 | -20.1 | 0.75 | 58.3 | keep collecting (12/30) |
| pin_rlm | moneyline | 1-6 | 14.3 | 23.6 | -9.4 | -4.92 | -70.3 | -1.24 | 57.1 | keep collecting (7/30) |
| pin_rlm | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.95 | 95.2 | 1.0 | 100.0 | keep collecting (1/30) |
| pre_move | moneyline | 6-18 | 25.0 | 23.6 | 1.4 | -8.9 | -37.1 | -0.61 | 45.8 | keep collecting (24/30) |
| pre_move | spread | 1-2 | 33.3 | 46.1 | -12.7 | -1.09 | -36.4 | -0.5 | 33.3 | keep collecting (3/30) |
| pre_move | total | 6-7 | 46.2 | 47.7 | -1.5 | -1.57 | -12.1 | 0.0 | 30.8 | keep collecting (13/30) |
| follow_move | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.44 | -21.9 | -1.3 | 50.0 | keep collecting (2/30) |
| follow_move | spread | 16-17 | 48.5 | 52.5 | -4.0 | -2.33 | -7.1 | -0.03 | 18.2 | no edge shown yet |
| follow_move | total | 0-1 | 0.0 | 52.7 | -52.7 | -1.0 | -100.0 | -3.0 | 0.0 | keep collecting (1/30) |
| rlm | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| rlm | spread | 2-7 | 22.2 | 46.1 | -23.8 | -5.17 | -57.4 | 0.0 | 11.1 | keep collecting (9/30) |
| rlm_ratio | spread | 1-2 | 33.3 | 46.1 | -12.7 | -1.17 | -38.9 | 0.0 | 0.0 | keep collecting (3/30) |
| money_level | moneyline | 35-11 | 76.1 | 74.1 | 2.0 | +2.62 | 5.7 | -0.3 | 41.3 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 32-14 | 69.6 | 55.1 | 14.4 | +15.24 | 33.1 | -0.05 | 21.7 | PROMOTE: beats break-even and its own base rate |
| money_level | total | 25-22 | 53.2 | 51.7 | 1.5 | +0.68 | 1.4 | -0.13 | 29.8 | no edge shown yet |
| sharp_gap | moneyline | 19-25 | 43.2 | 40.4 | 2.8 | -8.72 | -19.8 | -0.02 | 45.5 | no edge shown yet |
| sharp_gap | spread | 30-16 | 65.2 | 53.1 | 12.1 | +11.22 | 24.4 | 0.12 | 30.4 | PROMOTE: beats break-even and its own base rate |
| sharp_gap | total | 25-18 | 58.1 | 50.3 | 7.8 | +4.56 | 10.6 | -0.12 | 32.6 | no edge shown yet |
| money_moving | moneyline | 5-2 | 71.4 | 53.8 | 17.7 | +1.1 | 15.6 | 0.33 | 57.1 | keep collecting (7/30) |
| money_moving | spread | 5-5 | 50.0 | 52.4 | -2.4 | -0.41 | -4.1 | 0.0 | 30.0 | keep collecting (10/30) |
| money_moving | total | 5-2 | 71.4 | 49.6 | 21.8 | +2.7 | 38.6 | -0.43 | 14.3 | keep collecting (7/30) |
| pin_value | moneyline | 0-9 | 0.0 | 23.6 | -23.6 | -9.0 | -100.0 | 1.38 | 66.7 | keep collecting (9/30) |
| pin_value | spread | 17-6 | 73.9 | 55.7 | 18.3 | +8.9 | 38.7 | 0.2 | 30.4 | keep collecting (23/30) |
| pin_value | total | 7-9 | 43.8 | 50.0 | -6.2 | -2.77 | -17.3 | 0.0 | 25.0 | keep collecting (16/30) |
| pin_value | tt_away | 9-5 | 64.3 | 50.0 | 14.3 | +2.68 | 19.1 | -0.07 | 21.4 | keep collecting (14/30) |
| pin_value | tt_home | 8-8 | 50.0 | 50.0 | 0.0 | -1.17 | -7.3 | -0.06 | 25.0 | keep collecting (16/30) |
| book_lag | moneyline | 3-1 | 75.0 | 36.8 | 38.2 | +1.81 | 45.1 | -0.65 | 50.0 | keep collecting (4/30) |
| book_lag | spread | 2-2 | 50.0 | 55.9 | -5.9 | -0.26 | -6.5 | 0.38 | 75.0 | keep collecting (4/30) |
| consensus_gap | moneyline | 14-33 | 29.8 | 25.9 | 3.9 | -13.15 | -28.0 | -0.19 | 48.9 | DROP: below break-even |
| consensus_gap | spread | 11-8 | 57.9 | 53.1 | 4.8 | +1.38 | 7.3 | 0.39 | 42.1 | keep collecting (19/30) |
| money_level+sharp_gap | moneyline | 12-4 | 75.0 | 69.8 | 5.2 | +1.34 | 8.4 | -0.46 | 37.5 | keep collecting (16/30) |
| consensus_gap+pre_move | moneyline | 6-18 | 25.0 | 23.6 | 1.4 | -8.9 | -37.1 | -0.61 | 45.8 | redundant -- identical record to pre_move alone, not independent confirmation |
| consensus_gap+sharp_gap | moneyline | 10-22 | 31.2 | 26.9 | 4.3 | -9.16 | -28.6 | -0.12 | 50.0 | DROP: below break-even |
| pre_move+sharp_gap | moneyline | 6-18 | 25.0 | 23.6 | 1.4 | -8.9 | -37.1 | -0.61 | 45.8 | redundant -- identical record to pre_move alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm alone, not independent confirmation |
| consensus_gap+rlm_quiet | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm alone, not independent confirmation |
| consensus_gap+pin_move | moneyline | 0-2 | 0.0 | 23.6 | -23.6 | -2.0 | -100.0 | -0.7 | 50.0 | keep collecting (2/30) |
| money_level+money_moving | moneyline | 4-0 | 100.0 | 76.4 | 23.6 | +2.02 | 50.4 | -0.78 | 50.0 | keep collecting (4/30) |
| pin_move+sharp_gap | moneyline | 3-4 | 42.9 | 61.3 | -18.4 | -2.21 | -31.6 | 0.8 | 57.1 | keep collecting (7/30) |
| follow_move+money_level | moneyline | 1-0 | 100.0 | 76.4 | 23.6 | +0.56 | 56.2 | -3.1 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | moneyline | 1-0 | 100.0 | 76.4 | 23.6 | +0.56 | 56.2 | -3.1 | 0.0 | keep collecting (1/30) |
| consensus_gap+money_level | moneyline | 3-1 | 75.0 | 50.0 | 25.0 | +0.9 | 22.4 | -2.6 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_value | moneyline | 0-8 | 0.0 | 23.6 | -23.6 | -8.0 | -100.0 | 1.31 | 62.5 | keep collecting (8/30) |
| consensus_gap+pin_rlm | moneyline | 1-6 | 14.3 | 23.6 | -9.4 | -4.92 | -70.3 | -1.24 | 57.1 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| money_level+pre_move | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+pre_move | moneyline | 1-6 | 14.3 | 23.6 | -9.4 | -4.92 | -70.3 | -1.24 | 57.1 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 1-6 | 14.3 | 23.6 | -9.4 | -4.92 | -70.3 | -1.24 | 57.1 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | moneyline | 2-1 | 66.7 | 41.2 | 25.5 | +0.47 | 15.7 | 1.1 | 66.7 | keep collecting (3/30) |
| pin_value+pre_move | moneyline | 0-6 | 0.0 | 23.6 | -23.6 | -6.0 | -100.0 | 1.9 | 66.7 | keep collecting (6/30) |
| pin_value+sharp_gap | moneyline | 0-6 | 0.0 | 23.6 | -23.6 | -6.0 | -100.0 | 1.9 | 66.7 | keep collecting (6/30) |
| consensus_gap+money_moving | moneyline | 1-1 | 50.0 | 23.6 | 26.4 | +0.08 | 4.0 | 3.45 | 100.0 | keep collecting (2/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving+pre_move | moneyline | 1-1 | 50.0 | 23.6 | 26.4 | +0.08 | 4.0 | 3.45 | 100.0 | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-2 | 0.0 | 23.6 | -23.6 | -2.0 | -100.0 | 0.9 | 50.0 | keep collecting (2/30) |
| money_level+pin_move | moneyline | 10-3 | 76.9 | 76.4 | 0.6 | +0.78 | 6.0 | 1.63 | 69.2 | keep collecting (13/30) |
| book_lag+consensus_gap | moneyline | 2-1 | 66.7 | 23.6 | 43.0 | +1.42 | 47.3 | 0.63 | 66.7 | keep collecting (3/30) |
| book_lag+money_moving | moneyline | 1-0 | 100.0 | 23.6 | 76.4 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+pin_rlm | moneyline | 1-0 | 100.0 | 23.6 | 76.4 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+pre_move | moneyline | 2-0 | 100.0 | 23.6 | 76.4 | +2.42 | 121.0 | -0.25 | 50.0 | keep collecting (2/30) |
| book_lag+sharp_gap | moneyline | 2-0 | 100.0 | 23.6 | 76.4 | +2.42 | 121.0 | -0.25 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 1-0 | 100.0 | 23.6 | 76.4 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+pre_move | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+money_level | moneyline | 1-0 | 100.0 | 76.4 | 23.6 | +0.39 | 38.5 | -4.5 | 0.0 | keep collecting (1/30) |
| book_lag+pin_move | moneyline | 1-0 | 100.0 | 76.4 | 23.6 | +0.39 | 38.5 | -4.5 | 0.0 | keep collecting (1/30) |
| follow_move+rlm | spread | 2-7 | 22.2 | 46.1 | -23.8 | -5.17 | -57.4 | 0.0 | 11.1 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 3-7 | 30.0 | 47.6 | -17.6 | -4.33 | -43.3 | 0.0 | 10.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 1-2 | 33.3 | 46.1 | -12.7 | -1.17 | -38.9 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 13-8 | 61.9 | 53.9 | 8.0 | +4.01 | 19.1 | 0.07 | 23.8 | keep collecting (21/30) |
| rlm+rlm_quiet | spread | 2-7 | 22.2 | 46.1 | -23.8 | -5.17 | -57.4 | 0.0 | 11.1 | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+rlm_ratio | spread | 1-2 | 33.3 | 46.1 | -12.7 | -1.17 | -38.9 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 1-2 | 33.3 | 46.1 | -12.7 | -1.17 | -38.9 | 0.0 | 0.0 | keep collecting (3/30) |
| rlm_quiet+rlm_ratio | spread | 1-2 | 33.3 | 46.1 | -12.7 | -1.17 | -38.9 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | spread | 1-2 | 33.3 | 46.1 | -12.7 | -1.17 | -38.9 | 0.0 | 0.0 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | spread | 1-2 | 33.3 | 46.1 | -12.7 | -1.17 | -38.9 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+pin_value | spread | 6-4 | 60.0 | 54.7 | 5.3 | +1.04 | 10.4 | 0.4 | 40.0 | keep collecting (10/30) |
| money_level+sharp_gap | spread | 25-9 | 73.5 | 55.6 | 18.0 | +13.79 | 40.6 | 0.04 | 29.4 | PROMOTE: beats break-even and its own base rate |
| follow_move+pin_value | spread | 6-2 | 75.0 | 58.9 | 16.1 | +3.21 | 40.1 | 0.25 | 25.0 | keep collecting (8/30) |
| pin_value+sharp_gap | spread | 11-1 | 91.7 | 55.9 | 35.8 | +8.68 | 72.4 | 0.38 | 41.7 | keep collecting (12/30) |
| consensus_gap+follow_move | spread | 2-1 | 66.7 | 61.8 | 4.8 | +0.65 | 21.8 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+money_level | spread | 8-2 | 80.0 | 59.5 | 20.5 | +4.8 | 48.0 | 0.55 | 50.0 | keep collecting (10/30) |
| consensus_gap+sharp_gap | spread | 7-2 | 77.8 | 59.2 | 18.6 | +3.97 | 44.1 | 0.67 | 66.7 | keep collecting (9/30) |
| follow_move+money_level | spread | 12-7 | 63.2 | 58.1 | 5.1 | +4.17 | 22.0 | 0.08 | 26.3 | keep collecting (19/30) |
| money_level+pin_value | spread | 12-3 | 80.0 | 58.7 | 21.3 | +7.59 | 50.6 | 0.3 | 33.3 | keep collecting (15/30) |
| follow_move+money_moving | spread | 2-2 | 50.0 | 55.9 | -5.9 | -0.19 | -4.7 | 0.0 | 0.0 | keep collecting (4/30) |
| money_level+money_moving | spread | 3-2 | 60.0 | 52.4 | 7.6 | +0.8 | 16.0 | -0.6 | 20.0 | keep collecting (5/30) |
| money_moving+pin_value | spread | 4-1 | 80.0 | 52.4 | 27.6 | +2.63 | 52.7 | 0.4 | 40.0 | keep collecting (5/30) |
| money_moving+sharp_gap | spread | 2-2 | 50.0 | 55.9 | -5.9 | -0.15 | -3.8 | -0.25 | 25.0 | keep collecting (4/30) |
| book_lag+consensus_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.13 | -6.5 | 0.75 | 100.0 | keep collecting (2/30) |
| money_level+pre_move | spread | 1-1 | 50.0 | 38.2 | 11.8 | -0.09 | -4.5 | -1.0 | 0.0 | keep collecting (2/30) |
| pre_move+sharp_gap | spread | 1-2 | 33.3 | 46.1 | -12.7 | -1.09 | -36.4 | -0.5 | 33.3 | redundant -- identical record to pre_move alone, not independent confirmation |
| money_level+pin_move | spread | 6-3 | 66.7 | 59.2 | 7.5 | +2.5 | 27.8 | 0.0 | 44.4 | keep collecting (9/30) |
| money_moving+pin_move | spread | 1-0 | 100.0 | 38.2 | 61.8 | +0.95 | 95.2 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+money_level | spread | 2-1 | 66.7 | 61.8 | 4.8 | +0.74 | 24.7 | 0.33 | 66.7 | keep collecting (3/30) |
| book_lag+money_moving | spread | 0-1 | 0.0 | 61.8 | -61.8 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+sharp_gap | spread | 2-1 | 66.7 | 61.8 | 4.8 | +0.74 | 24.7 | 0.33 | 66.7 | keep collecting (3/30) |
| money_moving+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-0 | 100.0 | 61.8 | 38.2 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+pin_move | spread | 3-5 | 37.5 | 61.8 | -24.3 | -2.19 | -27.3 | -0.25 | 25.0 | keep collecting (8/30) |
| pin_move+pin_value | spread | 3-2 | 60.0 | 61.8 | -1.8 | +0.65 | 13.0 | 1.0 | 80.0 | keep collecting (5/30) |
| pin_move+sharp_gap | spread | 5-1 | 83.3 | 61.8 | 21.5 | +3.55 | 59.2 | 0.33 | 66.7 | keep collecting (6/30) |
| money_moving+rlm | spread | 0-1 | 0.0 | 38.2 | -38.2 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+rlm | spread | 0-2 | 0.0 | 61.8 | -61.8 | -2.0 | -100.0 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_move+rlm_quiet | spread | 0-2 | 0.0 | 61.8 | -61.8 | -2.0 | -100.0 | -0.5 | 0.0 | keep collecting (2/30) |
| book_lag+pin_move | spread | 2-0 | 100.0 | 61.8 | 38.2 | +1.74 | 87.0 | 1.5 | 100.0 | keep collecting (2/30) |
| book_lag+pin_value | spread | 2-0 | 100.0 | 61.8 | 38.2 | +1.74 | 87.0 | 1.5 | 100.0 | keep collecting (2/30) |
| consensus_gap+pin_move | spread | 1-1 | 50.0 | 61.8 | -11.8 | -0.13 | -6.5 | 1.0 | 100.0 | keep collecting (2/30) |
| consensus_gap+money_moving | spread | 1-0 | 100.0 | 38.2 | 61.8 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_value | total | 3-3 | 50.0 | 51.8 | -1.8 | -0.29 | -4.9 | -0.17 | 16.7 | keep collecting (6/30) |
| money_level+sharp_gap | total | 16-11 | 59.3 | 51.7 | 7.5 | +3.48 | 12.9 | -0.15 | 29.6 | keep collecting (27/30) |
| pin_value+sharp_gap | total | 6-4 | 60.0 | 50.0 | 10.0 | +1.32 | 13.2 | 0.1 | 30.0 | keep collecting (10/30) |
| money_level+pre_move | total | 1-2 | 33.3 | 49.1 | -15.8 | -1.13 | -37.7 | 1.0 | 33.3 | keep collecting (3/30) |
| pre_move+sharp_gap | total | 6-7 | 46.2 | 47.7 | -1.5 | -1.57 | -12.1 | 0.0 | 30.8 | redundant -- identical record to pre_move alone, not independent confirmation |
| pin_move+pin_value | total | 1-3 | 25.0 | 51.4 | -26.4 | -2.13 | -53.2 | 0.5 | 50.0 | keep collecting (4/30) |
| follow_move+money_level | total | 0-1 | 0.0 | 52.7 | -52.7 | -1.0 | -100.0 | -3.0 | 0.0 | redundant -- identical record to follow_move alone, not independent confirmation |
| money_level+money_moving | total | 3-1 | 75.0 | 51.4 | 23.6 | +1.75 | 43.7 | 0.0 | 25.0 | keep collecting (4/30) |
| money_moving+sharp_gap | total | 3-0 | 100.0 | 49.1 | 50.9 | +2.83 | 94.3 | -0.67 | 0.0 | keep collecting (3/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.93 | 92.6 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_move | total | 3-0 | 100.0 | 52.7 | 47.3 | +2.77 | 92.3 | 0.33 | 33.3 | keep collecting (3/30) |
| pin_move+sharp_gap | total | 4-0 | 100.0 | 50.0 | 50.0 | +3.64 | 91.0 | 1.0 | 75.0 | keep collecting (4/30) |
| money_moving+pre_move | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.95 | 95.2 | -2.0 | 0.0 | keep collecting (1/30) |
| pin_value+pre_move | total | 2-0 | 100.0 | 47.3 | 52.7 | +1.74 | 87.1 | 0.5 | 50.0 | keep collecting (2/30) |
| pin_move+pin_rlm | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.95 | 95.2 | 1.0 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pre_move | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.95 | 95.2 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_rlm+pre_move | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.95 | 95.2 | 1.0 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.95 | 95.2 | 1.0 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 14-33 | 29.8 | 37.4 | -7.7 | -18.24 | -38.8 |  |  | DROP: below break-even |
| pin_move | both | 56-45 | 55.4 | 51.2 | 4.2 | -0.04 | -0.0 |  |  | no edge shown yet |
| money_delta | both | 15-30 | 33.3 | 38.7 | -5.4 | -12.75 | -28.3 |  |  | DROP: below break-even |
| pin_rlm | both | 5-13 | 27.8 | 32.6 | -4.8 | -8.07 | -44.8 |  |  | keep collecting (18/30) |
| pre_move | both | 4-10 | 28.6 | 37.7 | -9.1 | -4.42 | -31.6 |  |  | keep collecting (14/30) |
| follow_move | both | 87-81 | 51.8 | 50.8 | 1.0 | -8.0 | -4.8 |  |  | no edge shown yet |
| rlm | both | 17-37 | 31.5 | 37.1 | -5.6 | -18.43 | -34.1 |  |  | DROP: below break-even |
| rlm_ratio | both | 6-16 | 27.3 | 34.7 | -7.4 | -9.17 | -41.7 |  |  | keep collecting (22/30) |
| money_level | both | 100-61 | 62.1 | 60.4 | 1.7 | +9.52 | 5.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 74-86 | 46.2 | 48.6 | -2.3 | -20.17 | -12.6 |  |  | DROP: below break-even |
| money_moving | both | 55-77 | 41.7 | 46.8 | -5.1 | -29.1 | -22.0 |  |  | DROP: below break-even |
| pin_value | both | 72-63 | 53.3 | 48.6 | 4.8 | +0.83 | 0.6 |  |  | no edge shown yet |
| book_lag | both | 5-1 | 83.3 | 62.7 | 20.6 | +2.86 | 47.7 |  |  | keep collecting (6/30) |
| consensus_gap | both | 22-43 | 33.8 | 31.3 | 2.5 | -14.57 | -22.4 |  |  | DROP: below break-even |
| follow_move+rlm | both | 17-37 | 31.5 | 37.1 | -5.6 | -18.43 | -34.1 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | both | 14-33 | 29.8 | 37.4 | -7.7 | -18.24 | -38.8 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 6-16 | 27.3 | 34.7 | -7.4 | -9.17 | -41.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 31-36 | 46.3 | 49.6 | -3.3 | -8.81 | -13.1 |  |  | no edge shown yet |
| money_level+pin_value | both | 20-9 | 69.0 | 55.3 | 13.7 | +8.34 | 28.7 |  |  | keep collecting (29/30) |
| rlm+rlm_quiet | both | 14-32 | 30.4 | 36.9 | -6.5 | -17.24 | -37.5 |  |  | DROP: below break-even |
| rlm+rlm_ratio | both | 6-16 | 27.3 | 34.7 | -7.4 | -9.17 | -41.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 10-22 | 31.2 | 38.0 | -6.7 | -11.49 | -35.9 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 3-12 | 20.0 | 33.8 | -13.8 | -8.98 | -59.9 |  |  | keep collecting (15/30) |
| rlm_quiet+sharp_gap | both | 7-17 | 29.2 | 38.0 | -8.8 | -10.3 | -42.9 |  |  | keep collecting (24/30) |
| rlm_ratio+sharp_gap | both | 6-16 | 27.3 | 34.7 | -7.4 | -9.17 | -41.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 47-34 | 58.0 | 58.7 | -0.7 | +1.72 | 2.1 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 7-3 | 70.0 | 56.2 | 13.8 | +2.86 | 28.6 |  |  | keep collecting (10/30) |
| pre_move+sharp_gap | both | 4-10 | 28.6 | 37.7 | -9.1 | -4.42 | -31.6 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+money_level | both | 40-23 | 63.5 | 62.5 | 1.0 | +4.62 | 7.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| book_lag+money_level | both | 2-1 | 66.7 | 71.5 | -4.8 | +0.4 | 13.4 |  |  | keep collecting (3/30) |
| consensus_gap+pre_move | both | 1-4 | 20.0 | 23.6 | -3.6 | -1.1 | -22.0 |  |  | keep collecting (5/30) |
| consensus_gap+sharp_gap | both | 11-23 | 32.4 | 30.3 | 2.1 | -7.92 | -23.3 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 15-8 | 65.2 | 50.7 | 14.5 | +4.88 | 21.2 |  |  | keep collecting (23/30) |
| pin_value+rlm | both | 3-6 | 33.3 | 41.6 | -8.3 | -3.38 | -37.6 |  |  | keep collecting (9/30) |
| pin_value+rlm_quiet | both | 3-6 | 33.3 | 41.6 | -8.3 | -3.38 | -37.6 |  |  | keep collecting (9/30) |
| pin_value+pre_move | both | 1-2 | 33.3 | 31.5 | 1.8 | -1.15 | -38.4 |  |  | keep collecting (3/30) |
| pin_value+sharp_gap | both | 20-17 | 54.1 | 46.6 | 7.5 | +0.05 | 0.1 |  |  | no edge shown yet |
| consensus_gap+follow_move | both | 7-17 | 29.2 | 29.6 | -0.5 | -7.94 | -33.1 |  |  | keep collecting (24/30) |
| consensus_gap+rlm | both | 5-17 | 22.7 | 25.4 | -2.6 | -9.48 | -43.1 |  |  | keep collecting (22/30) |
| consensus_gap+rlm_quiet | both | 3-16 | 15.8 | 25.6 | -9.9 | -11.38 | -59.9 |  |  | keep collecting (19/30) |
| consensus_gap+pin_value | both | 4-11 | 26.7 | 28.1 | -1.5 | -5.97 | -39.8 |  |  | keep collecting (15/30) |
| book_lag+consensus_gap | both | 3-0 | 100.0 | 53.9 | 46.1 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| book_lag+money_moving | both | 1-0 | 100.0 | 38.2 | 61.8 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | both | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | both | 8-20 | 28.6 | 28.8 | -0.2 | -9.28 | -33.1 |  |  | keep collecting (28/30) |
| money_moving+pin_value | both | 13-14 | 48.1 | 45.3 | 2.8 | -3.01 | -11.1 |  |  | keep collecting (27/30) |
| money_moving+pre_move | both | 1-5 | 16.7 | 34.8 | -18.2 | -4.13 | -68.8 |  |  | keep collecting (6/30) |
| money_moving+sharp_gap | both | 36-51 | 41.4 | 46.0 | -4.7 | -17.23 | -19.8 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 23-34 | 40.4 | 48.1 | -7.8 | -14.07 | -24.7 |  |  | DROP: below break-even |
| money_moving+rlm | both | 8-23 | 25.8 | 35.7 | -9.9 | -14.31 | -46.2 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | both | 5-18 | 21.7 | 34.9 | -13.1 | -13.12 | -57.0 |  |  | keep collecting (23/30) |
| money_level+money_moving | both | 35-26 | 57.4 | 58.6 | -1.3 | +0.7 | 1.1 |  |  | no edge shown yet |
| money_level+pin_move | both | 34-15 | 69.4 | 62.6 | 6.8 | +7.98 | 16.3 |  |  | PROMOTE: beats break-even and its own base rate |
| money_moving+pin_move | both | 26-27 | 49.1 | 48.0 | 1.1 | -5.27 | -9.9 |  |  | no edge shown yet |
| pin_move+pin_value | both | 16-14 | 53.3 | 46.3 | 7.1 | -0.25 | -0.8 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 28-27 | 50.9 | 48.2 | 2.7 | -2.84 | -5.2 |  |  | no edge shown yet |
| consensus_gap+pin_move | both | 6-11 | 35.3 | 29.0 | 6.3 | -3.81 | -22.4 |  |  | keep collecting (17/30) |
| consensus_gap+money_delta | both | 5-6 | 45.5 | 23.6 | 21.8 | +2.05 | 18.6 |  |  | keep collecting (11/30) |
| consensus_gap+pin_rlm | both | 2-8 | 20.0 | 23.6 | -3.6 | -5.76 | -57.6 |  |  | keep collecting (10/30) |
| consensus_gap+rlm_ratio | both | 3-7 | 30.0 | 23.6 | 6.4 | -2.86 | -28.6 |  |  | keep collecting (10/30) |
| follow_move+money_delta | both | 7-14 | 33.3 | 36.8 | -3.5 | -6.13 | -29.2 |  |  | keep collecting (21/30) |
| follow_move+pin_rlm | both | 5-11 | 31.2 | 33.8 | -2.5 | -6.07 | -38.0 |  |  | keep collecting (16/30) |
| money_delta+money_level | both | 3-5 | 37.5 | 39.3 | -1.8 | -1.76 | -22.0 |  |  | keep collecting (8/30) |
| money_delta+money_moving | both | 14-25 | 35.9 | 38.1 | -2.2 | -8.66 | -22.2 |  |  | DROP: below break-even |
| money_delta+pin_rlm | both | 4-9 | 30.8 | 33.1 | -2.4 | -4.94 | -38.0 |  |  | keep collecting (13/30) |
| money_delta+rlm | both | 6-12 | 33.3 | 36.1 | -2.7 | -5.13 | -28.5 |  |  | keep collecting (18/30) |
| money_delta+rlm_ratio | both | 5-9 | 35.7 | 33.5 | 2.2 | -3.04 | -21.7 |  |  | keep collecting (14/30) |
| money_delta+sharp_gap | both | 13-26 | 33.3 | 38.1 | -4.8 | -10.61 | -27.2 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 0-3 | 0.0 | 41.2 | -41.2 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_level+rlm | both | 0-3 | 0.0 | 41.2 | -41.2 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_level+rlm_ratio | both | 0-3 | 0.0 | 41.2 | -41.2 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | both | 5-12 | 29.4 | 33.2 | -3.7 | -7.07 | -41.6 |  |  | keep collecting (17/30) |
| money_moving+rlm_ratio | both | 6-13 | 31.6 | 33.7 | -2.1 | -6.17 | -32.5 |  |  | keep collecting (19/30) |
| pin_rlm+rlm | both | 5-11 | 31.2 | 33.8 | -2.5 | -6.07 | -38.0 |  |  | keep collecting (16/30) |
| pin_rlm+rlm_ratio | both | 5-11 | 31.2 | 33.8 | -2.5 | -6.07 | -38.0 |  |  | keep collecting (16/30) |
| pin_rlm+sharp_gap | both | 5-13 | 27.8 | 32.6 | -4.8 | -8.07 | -44.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+pin_move | both | 47-36 | 56.6 | 52.4 | 4.2 | +0.94 | 1.1 |  |  | no edge shown yet |
| pin_move+rlm_quiet | both | 12-21 | 36.4 | 39.2 | -2.9 | -8.15 | -24.7 |  |  | DROP: below break-even |
| money_delta+pin_move | both | 7-13 | 35.0 | 39.4 | -4.4 | -6.2 | -31.0 |  |  | keep collecting (20/30) |
| money_delta+pin_value | both | 1-7 | 12.5 | 38.0 | -25.5 | -6.17 | -77.1 |  |  | keep collecting (8/30) |
| money_delta+rlm_quiet | both | 3-7 | 30.0 | 34.5 | -4.5 | -3.94 | -39.4 |  |  | keep collecting (10/30) |
| pin_move+pin_rlm | both | 5-11 | 31.2 | 33.8 | -2.5 | -6.07 | -38.0 |  |  | keep collecting (16/30) |
| pin_move+rlm | both | 14-23 | 37.8 | 39.2 | -1.4 | -8.24 | -22.3 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | both | 5-9 | 35.7 | 35.2 | 0.5 | -4.07 | -29.1 |  |  | keep collecting (14/30) |
| pin_rlm+pin_value | both | 1-5 | 16.7 | 31.5 | -14.8 | -4.13 | -68.8 |  |  | keep collecting (6/30) |
| pin_rlm+rlm_quiet | both | 3-8 | 27.3 | 31.4 | -4.1 | -4.98 | -45.3 |  |  | keep collecting (11/30) |
| pin_value+rlm_ratio | both | 1-3 | 25.0 | 35.5 | -10.5 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| money_delta+pre_move | both | 1-3 | 25.0 | 34.5 | -9.5 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| money_level+pre_move | both | 1-1 | 50.0 | 38.2 | 11.8 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| pin_move+pre_move | both | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+pre_move | both | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 3-17 | 15.0 | 23.6 | -8.6 | -12.38 | -61.9 |  |  | keep collecting (20/30) |
| rlm_quiet | spread | 4-11 | 26.7 | 47.6 | -21.0 | -7.19 | -47.9 |  |  | keep collecting (15/30) |
| rlm_quiet | total | 7-5 | 58.3 | 47.7 | 10.6 | +1.33 | 11.1 |  |  | keep collecting (12/30) |
| pin_move | moneyline | 19-16 | 54.3 | 50.8 | 3.5 | -4.58 | -13.1 |  |  | no edge shown yet |
| pin_move | spread | 11-14 | 44.0 | 53.3 | -9.3 | -3.94 | -15.8 |  |  | keep collecting (25/30) |
| pin_move | total | 24-15 | 61.5 | 50.3 | 11.2 | +6.75 | 17.3 |  |  | no edge shown yet |
| pin_move | tt_away | 1-0 | 100.0 | 50.0 | 50.0 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| pin_move | tt_home | 1-0 | 100.0 | 50.0 | 50.0 | +0.89 | 88.5 |  |  | keep collecting (1/30) |
| money_delta | moneyline | 5-6 | 45.5 | 23.6 | 21.8 | +2.05 | 18.6 |  |  | keep collecting (11/30) |
| money_delta | spread | 4-14 | 22.2 | 39.5 | -17.3 | -10.39 | -57.7 |  |  | keep collecting (18/30) |
| money_delta | total | 6-10 | 37.5 | 48.3 | -10.8 | -4.41 | -27.6 |  |  | keep collecting (16/30) |
| pin_rlm | moneyline | 2-9 | 18.2 | 23.6 | -5.5 | -6.76 | -61.5 |  |  | keep collecting (11/30) |
| pin_rlm | spread | 0-3 | 0.0 | 46.1 | -46.1 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_rlm | total | 3-1 | 75.0 | 47.3 | 27.7 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| pre_move | moneyline | 1-5 | 16.7 | 32.4 | -15.8 | -2.1 | -35.0 |  |  | keep collecting (6/30) |
| pre_move | spread | 2-3 | 40.0 | 38.2 | 1.8 | -1.17 | -23.4 |  |  | keep collecting (5/30) |
| pre_move | total | 1-2 | 33.3 | 47.3 | -13.9 | -1.15 | -38.4 |  |  | keep collecting (3/30) |
| follow_move | moneyline | 22-23 | 48.9 | 49.4 | -0.5 | -8.95 | -19.9 |  |  | no edge shown yet |
| follow_move | spread | 21-27 | 43.8 | 53.4 | -9.7 | -7.56 | -15.7 |  |  | no edge shown yet |
| follow_move | total | 18-11 | 62.1 | 49.9 | 12.2 | +5.42 | 18.7 |  |  | keep collecting (29/30) |
| follow_move | tt_away | 14-8 | 63.6 | 50.0 | 13.6 | +4.39 | 20.0 |  |  | keep collecting (22/30) |
| follow_move | tt_home | 12-12 | 50.0 | 50.0 | 0.0 | -1.32 | -5.5 |  |  | keep collecting (24/30) |
| rlm | moneyline | 5-18 | 21.7 | 23.6 | -1.9 | -10.48 | -45.6 |  |  | keep collecting (23/30) |
| rlm | spread | 4-13 | 23.5 | 46.5 | -23.0 | -9.19 | -54.0 |  |  | keep collecting (17/30) |
| rlm | total | 8-6 | 57.1 | 47.7 | 9.5 | +1.24 | 8.9 |  |  | keep collecting (14/30) |
| rlm_ratio | moneyline | 3-8 | 27.3 | 23.6 | 3.6 | -3.86 | -35.1 |  |  | keep collecting (11/30) |
| rlm_ratio | spread | 0-7 | 0.0 | 44.9 | -44.9 | -7.0 | -100.0 |  |  | keep collecting (7/30) |
| rlm_ratio | total | 3-1 | 75.0 | 47.3 | 27.7 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| money_level | moneyline | 43-11 | 79.6 | 73.4 | 6.2 | +7.69 | 14.2 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level | spread | 28-25 | 52.8 | 55.6 | -2.7 | +0.28 | 0.5 |  |  | no edge shown yet |
| money_level | total | 29-25 | 53.7 | 52.2 | 1.5 | +1.55 | 2.9 |  |  | no edge shown yet |
| sharp_gap | moneyline | 24-28 | 46.2 | 47.0 | -0.8 | -7.39 | -14.2 |  |  | no edge shown yet |
| sharp_gap | spread | 24-30 | 44.4 | 48.2 | -3.8 | -8.4 | -15.6 |  |  | no edge shown yet |
| sharp_gap | total | 26-28 | 48.1 | 50.4 | -2.3 | -4.38 | -8.1 |  |  | no edge shown yet |
| money_moving | moneyline | 19-25 | 43.2 | 44.0 | -0.8 | -9.83 | -22.3 |  |  | no edge shown yet |
| money_moving | spread | 15-28 | 34.9 | 45.9 | -11.0 | -14.51 | -33.7 |  |  | DROP: below break-even |
| money_moving | total | 21-24 | 46.7 | 50.4 | -3.8 | -4.75 | -10.6 |  |  | no edge shown yet |
| pin_value | moneyline | 3-10 | 23.1 | 27.7 | -4.6 | -6.14 | -47.3 |  |  | keep collecting (13/30) |
| pin_value | spread | 18-6 | 75.0 | 53.9 | 21.1 | +9.77 | 40.7 |  |  | keep collecting (24/30) |
| pin_value | total | 16-13 | 55.2 | 50.1 | 5.1 | +0.97 | 3.3 |  |  | keep collecting (29/30) |
| pin_value | tt_away | 16-18 | 47.1 | 50.0 | -2.9 | -4.01 | -11.8 |  |  | no edge shown yet |
| pin_value | tt_home | 19-16 | 54.3 | 50.0 | 4.3 | +0.24 | 0.7 |  |  | no edge shown yet |
| book_lag | moneyline | 1-1 | 50.0 | 76.4 | -26.4 | -0.43 | -21.6 |  |  | keep collecting (2/30) |
| book_lag | spread | 4-0 | 100.0 | 55.9 | 44.1 | +3.29 | 82.4 |  |  | keep collecting (4/30) |
| consensus_gap | moneyline | 17-38 | 30.9 | 27.5 | 3.4 | -13.7 | -24.9 |  |  | DROP: below break-even |
| consensus_gap | spread | 5-5 | 50.0 | 52.4 | -2.4 | -0.87 | -8.7 |  |  | keep collecting (10/30) |
| consensus_gap+money_level | moneyline | 6-1 | 85.7 | 53.8 | 31.9 | +4.02 | 57.5 |  |  | keep collecting (7/30) |
| pre_move+sharp_gap | moneyline | 1-5 | 16.7 | 32.4 | -15.8 | -2.1 | -35.0 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| book_lag+money_level | moneyline | 1-1 | 50.0 | 76.4 | -26.4 | -0.43 | -21.6 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pre_move | moneyline | 1-4 | 20.0 | 23.6 | -3.6 | -1.1 | -22.0 |  |  | keep collecting (5/30) |
| consensus_gap+sharp_gap | moneyline | 10-21 | 32.3 | 28.7 | 3.5 | -6.75 | -21.8 |  |  | DROP: below break-even |
| money_level+sharp_gap | moneyline | 18-6 | 75.0 | 72.0 | 3.0 | +3.64 | 15.2 |  |  | keep collecting (24/30) |
| consensus_gap+follow_move | moneyline | 7-16 | 30.4 | 28.2 | 2.2 | -6.94 | -30.2 |  |  | keep collecting (23/30) |
| consensus_gap+rlm | moneyline | 5-16 | 23.8 | 23.6 | 0.2 | -8.48 | -40.4 |  |  | keep collecting (21/30) |
| consensus_gap+rlm_quiet | moneyline | 3-15 | 16.7 | 23.6 | -7.0 | -10.38 | -57.7 |  |  | keep collecting (18/30) |
| follow_move+rlm | moneyline | 5-18 | 21.7 | 23.6 | -1.9 | -10.48 | -45.6 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | moneyline | 3-17 | 15.0 | 23.6 | -8.6 | -12.38 | -61.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm+rlm_quiet | moneyline | 3-17 | 15.0 | 23.6 | -8.6 | -12.38 | -61.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 2-10 | 16.7 | 23.6 | -7.0 | -6.59 | -54.9 |  |  | keep collecting (12/30) |
| pin_value+pre_move | moneyline | 0-2 | 0.0 | 23.6 | -23.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_value+sharp_gap | moneyline | 1-8 | 11.1 | 29.5 | -18.4 | -7.56 | -84.0 |  |  | keep collecting (9/30) |
| follow_move+money_level | moneyline | 17-5 | 77.3 | 74.0 | 3.3 | +1.53 | 7.0 |  |  | keep collecting (22/30) |
| follow_move+sharp_gap | moneyline | 9-10 | 47.4 | 45.8 | 1.5 | -2.89 | -15.2 |  |  | keep collecting (19/30) |
| follow_move+money_moving | moneyline | 10-14 | 41.7 | 45.6 | -3.9 | -6.16 | -25.7 |  |  | keep collecting (24/30) |
| money_moving+rlm | moneyline | 3-11 | 21.4 | 23.6 | -2.2 | -6.86 | -49.0 |  |  | keep collecting (14/30) |
| money_moving+rlm_quiet | moneyline | 1-10 | 9.1 | 23.6 | -14.5 | -8.76 | -79.6 |  |  | keep collecting (11/30) |
| consensus_gap+money_moving | moneyline | 7-18 | 28.0 | 25.7 | 2.3 | -8.06 | -32.2 |  |  | keep collecting (25/30) |
| consensus_gap+pin_move | moneyline | 6-10 | 37.5 | 26.9 | 10.6 | -2.81 | -17.6 |  |  | keep collecting (16/30) |
| money_moving+pin_move | moneyline | 8-8 | 50.0 | 43.4 | 6.6 | -2.7 | -16.9 |  |  | keep collecting (16/30) |
| money_moving+pin_value | moneyline | 2-6 | 25.0 | 30.2 | -5.2 | -4.59 | -57.4 |  |  | keep collecting (8/30) |
| pin_move+pin_value | moneyline | 2-5 | 28.6 | 31.2 | -2.6 | -3.59 | -51.3 |  |  | keep collecting (7/30) |
| consensus_gap+money_delta | moneyline | 5-6 | 45.5 | 23.6 | 21.8 | +2.05 | 18.6 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| consensus_gap+pin_rlm | moneyline | 2-8 | 20.0 | 23.6 | -3.6 | -5.76 | -57.6 |  |  | keep collecting (10/30) |
| consensus_gap+rlm_ratio | moneyline | 3-7 | 30.0 | 23.6 | 6.4 | -2.86 | -28.6 |  |  | keep collecting (10/30) |
| follow_move+money_delta | moneyline | 3-5 | 37.5 | 23.6 | 13.9 | -0.86 | -10.7 |  |  | keep collecting (8/30) |
| follow_move+pin_rlm | moneyline | 2-7 | 22.2 | 23.6 | -1.4 | -4.76 | -52.9 |  |  | keep collecting (9/30) |
| follow_move+rlm_ratio | moneyline | 3-8 | 27.3 | 23.6 | 3.6 | -3.86 | -35.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | moneyline | 1-1 | 50.0 | 23.6 | 26.4 | +0.46 | 23.0 |  |  | keep collecting (2/30) |
| money_delta+money_moving | moneyline | 5-6 | 45.5 | 23.6 | 21.8 | +2.05 | 18.6 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_rlm | moneyline | 2-6 | 25.0 | 23.6 | 1.4 | -3.76 | -47.0 |  |  | keep collecting (8/30) |
| money_delta+rlm | moneyline | 3-5 | 37.5 | 23.6 | 13.9 | -0.86 | -10.7 |  |  | keep collecting (8/30) |
| money_delta+rlm_ratio | moneyline | 3-5 | 37.5 | 23.6 | 13.9 | -0.86 | -10.7 |  |  | keep collecting (8/30) |
| money_delta+sharp_gap | moneyline | 5-6 | 45.5 | 23.6 | 21.8 | +2.05 | 18.6 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+money_moving | moneyline | 14-5 | 73.7 | 70.8 | 2.9 | +2.61 | 13.8 |  |  | keep collecting (19/30) |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+rlm | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+rlm_ratio | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 2-8 | 20.0 | 23.6 | -3.6 | -5.76 | -57.6 |  |  | keep collecting (10/30) |
| money_moving+rlm_ratio | moneyline | 3-7 | 30.0 | 23.6 | 6.4 | -2.86 | -28.6 |  |  | keep collecting (10/30) |
| money_moving+sharp_gap | moneyline | 12-17 | 41.4 | 41.8 | -0.4 | -5.04 | -17.4 |  |  | keep collecting (29/30) |
| pin_rlm+rlm | moneyline | 2-7 | 22.2 | 23.6 | -1.4 | -4.76 | -52.9 |  |  | keep collecting (9/30) |
| pin_rlm+rlm_ratio | moneyline | 2-7 | 22.2 | 23.6 | -1.4 | -4.76 | -52.9 |  |  | keep collecting (9/30) |
| pin_rlm+sharp_gap | moneyline | 2-9 | 18.2 | 23.6 | -5.5 | -6.76 | -61.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm+rlm_ratio | moneyline | 3-8 | 27.3 | 23.6 | 3.6 | -3.86 | -35.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | moneyline | 3-8 | 27.3 | 23.6 | 3.6 | -3.86 | -35.1 |  |  | keep collecting (11/30) |
| rlm_ratio+sharp_gap | moneyline | 3-8 | 27.3 | 23.6 | 3.6 | -3.86 | -35.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_move | moneyline | 18-12 | 60.0 | 53.5 | 6.5 | -1.54 | -5.1 |  |  | no edge shown yet |
| follow_move+pin_value | moneyline | 1-3 | 25.0 | 36.8 | -11.8 | -2.56 | -63.9 |  |  | keep collecting (4/30) |
| money_delta+pin_move | moneyline | 2-4 | 33.3 | 23.6 | 9.7 | -1.76 | -29.3 |  |  | keep collecting (6/30) |
| money_delta+pin_value | moneyline | 0-3 | 0.0 | 23.6 | -23.6 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 1-4 | 20.0 | 23.6 | -3.6 | -2.76 | -55.2 |  |  | keep collecting (5/30) |
| pin_move+pin_rlm | moneyline | 2-7 | 22.2 | 23.6 | -1.4 | -4.76 | -52.9 |  |  | keep collecting (9/30) |
| pin_move+rlm | moneyline | 4-9 | 30.8 | 23.6 | 7.1 | -3.38 | -26.0 |  |  | keep collecting (13/30) |
| pin_move+rlm_quiet | moneyline | 3-9 | 25.0 | 23.6 | 1.4 | -4.38 | -36.5 |  |  | keep collecting (12/30) |
| pin_move+rlm_ratio | moneyline | 2-5 | 28.6 | 23.6 | 4.9 | -2.76 | -39.4 |  |  | keep collecting (7/30) |
| pin_move+sharp_gap | moneyline | 6-7 | 46.2 | 39.9 | 6.3 | -2.81 | -21.6 |  |  | keep collecting (13/30) |
| pin_rlm+pin_value | moneyline | 0-4 | 0.0 | 23.6 | -23.6 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| pin_rlm+rlm_quiet | moneyline | 1-6 | 14.3 | 23.6 | -9.4 | -4.76 | -68.0 |  |  | keep collecting (7/30) |
| pin_value+rlm | moneyline | 0-3 | 0.0 | 23.6 | -23.6 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_value+rlm_quiet | moneyline | 0-3 | 0.0 | 23.6 | -23.6 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_value+rlm_ratio | moneyline | 0-2 | 0.0 | 23.6 | -23.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | moneyline | 1-7 | 12.5 | 23.6 | -11.1 | -5.76 | -72.0 |  |  | keep collecting (8/30) |
| rlm_quiet+sharp_gap | moneyline | 1-7 | 12.5 | 23.6 | -11.1 | -5.76 | -72.0 |  |  | keep collecting (8/30) |
| money_level+pin_move | moneyline | 14-3 | 82.4 | 76.4 | 6.0 | +1.84 | 10.8 |  |  | keep collecting (17/30) |
| money_level+pin_value | moneyline | 1-0 | 100.0 | 76.4 | 23.6 | +0.44 | 44.4 |  |  | keep collecting (1/30) |
| money_delta+pre_move | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pre_move | moneyline | 0-2 | 0.0 | 23.6 | -23.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_move+pre_move | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+pre_move | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| follow_move+rlm | spread | 4-13 | 23.5 | 46.5 | -23.0 | -9.19 | -54.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 4-11 | 26.7 | 47.6 | -21.0 | -7.19 | -47.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-7 | 0.0 | 44.9 | -44.9 | -7.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 13-18 | 41.9 | 51.9 | -10.0 | -6.11 | -19.7 |  |  | no edge shown yet |
| money_level+pin_value | spread | 10-4 | 71.4 | 56.8 | 14.7 | +4.96 | 35.5 |  |  | keep collecting (14/30) |
| rlm+rlm_quiet | spread | 4-10 | 28.6 | 46.6 | -18.1 | -6.19 | -44.2 |  |  | keep collecting (14/30) |
| rlm+rlm_ratio | spread | 0-7 | 0.0 | 44.9 | -44.9 | -7.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 2-10 | 16.7 | 44.1 | -27.4 | -8.1 | -67.5 |  |  | keep collecting (12/30) |
| rlm_quiet+rlm_ratio | spread | 0-4 | 0.0 | 44.1 | -44.1 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| rlm_quiet+sharp_gap | spread | 2-7 | 22.2 | 43.4 | -21.2 | -5.1 | -56.6 |  |  | keep collecting (9/30) |
| rlm_ratio+sharp_gap | spread | 0-7 | 0.0 | 44.9 | -44.9 | -7.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 13-14 | 48.1 | 58.3 | -10.2 | -2.09 | -7.8 |  |  | keep collecting (27/30) |
| follow_move+pin_value | spread | 7-1 | 87.5 | 58.9 | 28.6 | +5.19 | 64.9 |  |  | keep collecting (8/30) |
| pin_value+rlm | spread | 1-0 | 100.0 | 61.8 | 38.2 | +0.87 | 87.0 |  |  | keep collecting (1/30) |
| pin_value+rlm_quiet | spread | 1-0 | 100.0 | 61.8 | 38.2 | +0.87 | 87.0 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | spread | 13-14 | 48.1 | 53.9 | -5.8 | -2.45 | -9.1 |  |  | keep collecting (27/30) |
| consensus_gap+sharp_gap | spread | 1-2 | 33.3 | 46.1 | -12.7 | -1.17 | -38.9 |  |  | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 3-0 | 100.0 | 53.9 | 46.1 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| pin_value+sharp_gap | spread | 10-2 | 83.3 | 53.9 | 29.4 | +6.74 | 56.1 |  |  | keep collecting (12/30) |
| book_lag+money_moving | spread | 1-0 | 100.0 | 38.2 | 61.8 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | spread | 1-2 | 33.3 | 53.9 | -20.6 | -1.22 | -40.6 |  |  | keep collecting (3/30) |
| consensus_gap+pin_value | spread | 2-1 | 66.7 | 46.1 | 20.6 | +0.61 | 20.5 |  |  | keep collecting (3/30) |
| money_moving+pin_value | spread | 6-2 | 75.0 | 53.0 | 22.0 | +3.21 | 40.1 |  |  | keep collecting (8/30) |
| follow_move+pin_move | spread | 9-13 | 40.9 | 54.3 | -13.4 | -4.68 | -21.3 |  |  | keep collecting (22/30) |
| money_level+money_moving | spread | 9-11 | 45.0 | 53.5 | -8.5 | -2.92 | -14.6 |  |  | keep collecting (20/30) |
| money_moving+sharp_gap | spread | 10-18 | 35.7 | 45.8 | -10.1 | -8.91 | -31.8 |  |  | keep collecting (28/30) |
| pin_move+rlm_quiet | spread | 2-7 | 22.2 | 48.7 | -26.5 | -5.1 | -56.6 |  |  | keep collecting (9/30) |
| money_delta+money_moving | spread | 3-12 | 20.0 | 39.8 | -19.8 | -9.3 | -62.0 |  |  | keep collecting (15/30) |
| money_delta+sharp_gap | spread | 3-12 | 20.0 | 39.8 | -19.8 | -9.3 | -62.0 |  |  | keep collecting (15/30) |
| money_delta+money_level | spread | 1-4 | 20.0 | 42.9 | -22.9 | -3.13 | -62.6 |  |  | keep collecting (5/30) |
| money_delta+pre_move | spread | 1-2 | 33.3 | 38.2 | -4.8 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| money_level+pre_move | spread | 1-1 | 50.0 | 38.2 | 11.8 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| money_moving+pre_move | spread | 1-2 | 33.3 | 38.2 | -4.8 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| pre_move+sharp_gap | spread | 2-3 | 40.0 | 38.2 | 1.8 | -1.17 | -23.4 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+money_moving | spread | 5-13 | 27.8 | 50.0 | -22.2 | -8.32 | -46.2 |  |  | keep collecting (18/30) |
| money_moving+pin_move | spread | 4-9 | 30.8 | 49.1 | -18.3 | -5.31 | -40.8 |  |  | keep collecting (13/30) |
| money_moving+rlm | spread | 1-8 | 11.1 | 43.4 | -32.3 | -7.05 | -78.3 |  |  | keep collecting (9/30) |
| money_moving+rlm_quiet | spread | 1-5 | 16.7 | 42.1 | -25.5 | -4.05 | -67.5 |  |  | keep collecting (6/30) |
| pin_move+rlm | spread | 2-8 | 20.0 | 47.6 | -27.6 | -6.1 | -61.0 |  |  | keep collecting (10/30) |
| pin_move+sharp_gap | spread | 8-10 | 44.4 | 51.3 | -6.9 | -2.67 | -14.8 |  |  | keep collecting (18/30) |
| follow_move+money_delta | spread | 1-5 | 16.7 | 42.1 | -25.5 | -4.0 | -66.7 |  |  | keep collecting (6/30) |
| follow_move+pin_rlm | spread | 0-3 | 0.0 | 46.1 | -46.1 | -3.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+pin_move | spread | 2-3 | 40.0 | 42.9 | -2.9 | -1.17 | -23.3 |  |  | keep collecting (5/30) |
| money_delta+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_delta+rlm | spread | 0-4 | 0.0 | 44.1 | -44.1 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| money_delta+rlm_ratio | spread | 0-3 | 0.0 | 46.1 | -46.1 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_level+pin_move | spread | 6-6 | 50.0 | 59.8 | -9.8 | -0.58 | -4.9 |  |  | keep collecting (12/30) |
| money_level+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_moving+pin_rlm | spread | 0-3 | 0.0 | 46.1 | -46.1 | -3.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-5 | 0.0 | 42.9 | -42.9 | -5.0 | -100.0 |  |  | keep collecting (5/30) |
| pin_move+pin_rlm | spread | 0-3 | 0.0 | 46.1 | -46.1 | -3.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | spread | 0-3 | 0.0 | 46.1 | -46.1 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_rlm+rlm | spread | 0-3 | 0.0 | 46.1 | -46.1 | -3.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | spread | 0-3 | 0.0 | 46.1 | -46.1 | -3.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 0-3 | 0.0 | 46.1 | -46.1 | -3.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+rlm_quiet | spread | 0-1 | 0.0 | 38.2 | -38.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+follow_move | spread | 0-1 | 0.0 | 61.8 | -61.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+pin_move | spread | 0-1 | 0.0 | 61.8 | -61.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+rlm | spread | 0-1 | 0.0 | 61.8 | -61.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 0-1 | 0.0 | 61.8 | -61.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta+pin_value | spread | 1-0 | 100.0 | 38.2 | 61.8 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| pin_move+pin_value | spread | 4-1 | 80.0 | 52.4 | 27.6 | +2.52 | 50.4 |  |  | keep collecting (5/30) |
| book_lag+money_level | spread | 1-0 | 100.0 | 61.8 | 38.2 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| consensus_gap+money_level | spread | 1-2 | 33.3 | 61.8 | -28.5 | -1.17 | -38.9 |  |  | keep collecting (3/30) |
| pin_rlm+rlm_quiet | spread | 0-1 | 0.0 | 38.2 | -38.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | total | 16-14 | 53.3 | 52.4 | 1.0 | +0.53 | 1.8 |  |  | no edge shown yet |
| pin_value+pre_move | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| pin_value+sharp_gap | total | 9-7 | 56.2 | 50.7 | 5.6 | +0.88 | 5.5 |  |  | keep collecting (16/30) |
| pre_move+sharp_gap | total | 1-2 | 33.3 | 47.3 | -13.9 | -1.15 | -38.4 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| money_level+pin_value | total | 9-5 | 64.3 | 52.3 | 11.9 | +2.93 | 20.9 |  |  | keep collecting (14/30) |
| money_moving+pre_move | total | 0-1 | 0.0 | 47.3 | -47.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+sharp_gap | total | 14-16 | 46.7 | 50.4 | -3.7 | -3.27 | -10.9 |  |  | no edge shown yet |
| money_level+money_moving | total | 12-10 | 54.5 | 52.7 | 1.8 | +1.01 | 4.6 |  |  | keep collecting (22/30) |
| money_level+pin_move | total | 14-6 | 70.0 | 52.5 | 17.5 | +6.73 | 33.6 |  |  | keep collecting (20/30) |
| money_moving+pin_move | total | 14-10 | 58.3 | 50.5 | 7.9 | +2.73 | 11.4 |  |  | keep collecting (24/30) |
| money_moving+pin_value | total | 5-6 | 45.5 | 50.7 | -5.3 | -1.63 | -14.8 |  |  | keep collecting (11/30) |
| pin_move+pin_value | total | 9-8 | 52.9 | 50.5 | 2.5 | -0.07 | -0.4 |  |  | keep collecting (17/30) |
| pin_move+sharp_gap | total | 14-10 | 58.3 | 50.5 | 7.9 | +2.64 | 11.0 |  |  | keep collecting (24/30) |
| money_delta+money_level | total | 1-0 | 100.0 | 52.7 | 47.3 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+money_moving | total | 6-7 | 46.2 | 48.5 | -2.4 | -1.41 | -10.9 |  |  | keep collecting (13/30) |
| money_delta+sharp_gap | total | 5-8 | 38.5 | 48.5 | -10.1 | -3.36 | -25.9 |  |  | keep collecting (13/30) |
| follow_move+money_delta | total | 3-4 | 42.9 | 47.3 | -4.4 | -1.27 | -18.2 |  |  | keep collecting (7/30) |
| follow_move+money_moving | total | 8-7 | 53.3 | 49.8 | 3.5 | +0.41 | 2.7 |  |  | keep collecting (15/30) |
| follow_move+pin_move | total | 18-11 | 62.1 | 49.9 | 12.2 | +5.42 | 18.7 |  |  | redundant -- identical record to follow_move alone, not independent confirmation |
| follow_move+pin_rlm | total | 3-1 | 75.0 | 47.3 | 27.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+pin_value | total | 5-4 | 55.6 | 49.7 | 5.9 | +0.43 | 4.8 |  |  | keep collecting (9/30) |
| follow_move+rlm | total | 8-6 | 57.1 | 47.7 | 9.5 | +1.24 | 8.9 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | total | 7-5 | 58.3 | 47.7 | 10.6 | +1.33 | 11.1 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 3-1 | 75.0 | 47.3 | 27.7 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 9-8 | 52.9 | 49.5 | 3.4 | +0.19 | 1.1 |  |  | keep collecting (17/30) |
| money_delta+pin_move | total | 3-6 | 33.3 | 47.9 | -14.5 | -3.27 | -36.4 |  |  | keep collecting (9/30) |
| money_delta+pin_rlm | total | 2-1 | 66.7 | 47.3 | 19.4 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| money_delta+pin_value | total | 0-4 | 0.0 | 48.6 | -48.6 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| money_delta+rlm | total | 3-3 | 50.0 | 47.3 | 2.7 | -0.27 | -4.5 |  |  | keep collecting (6/30) |
| money_delta+rlm_quiet | total | 2-2 | 50.0 | 47.3 | 2.7 | -0.18 | -4.5 |  |  | keep collecting (4/30) |
| money_delta+rlm_ratio | total | 2-1 | 66.7 | 47.3 | 19.4 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | total | 3-1 | 75.0 | 47.3 | 27.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm | total | 4-4 | 50.0 | 48.0 | 2.0 | -0.4 | -5.0 |  |  | keep collecting (8/30) |
| money_moving+rlm_quiet | total | 3-3 | 50.0 | 48.2 | 1.8 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| money_moving+rlm_ratio | total | 3-1 | 75.0 | 47.3 | 27.7 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_move+pin_rlm | total | 3-1 | 75.0 | 47.3 | 27.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm | total | 8-6 | 57.1 | 47.7 | 9.5 | +1.24 | 8.9 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| pin_move+rlm_quiet | total | 7-5 | 58.3 | 47.7 | 10.6 | +1.33 | 11.1 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_ratio | total | 3-1 | 75.0 | 47.3 | 27.7 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+pin_value | total | 1-1 | 50.0 | 47.3 | 2.7 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| pin_rlm+rlm | total | 3-1 | 75.0 | 47.3 | 27.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | total | 2-1 | 66.7 | 47.3 | 19.4 | +0.78 | 26.0 |  |  | keep collecting (3/30) |
| pin_rlm+rlm_ratio | total | 3-1 | 75.0 | 47.3 | 27.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | total | 3-1 | 75.0 | 47.3 | 27.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm | total | 2-3 | 40.0 | 48.4 | -8.4 | -1.25 | -25.1 |  |  | keep collecting (5/30) |
| pin_value+rlm_quiet | total | 2-3 | 40.0 | 48.4 | -8.4 | -1.25 | -25.1 |  |  | keep collecting (5/30) |
| pin_value+rlm_ratio | total | 1-1 | 50.0 | 47.3 | 2.7 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| rlm+rlm_quiet | total | 7-5 | 58.3 | 47.7 | 10.6 | +1.33 | 11.1 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm+rlm_ratio | total | 3-1 | 75.0 | 47.3 | 27.7 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | total | 5-4 | 55.6 | 47.3 | 8.3 | +0.47 | 5.2 |  |  | keep collecting (9/30) |
| rlm_quiet+rlm_ratio | total | 2-1 | 66.7 | 47.3 | 19.4 | +0.78 | 26.0 |  |  | keep collecting (3/30) |
| rlm_quiet+sharp_gap | total | 4-3 | 57.1 | 47.3 | 9.9 | +0.56 | 8.0 |  |  | keep collecting (7/30) |
| rlm_ratio+sharp_gap | total | 3-1 | 75.0 | 47.3 | 27.7 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | total | 10-4 | 71.4 | 52.3 | 19.1 | +5.18 | 37.0 |  |  | keep collecting (14/30) |
| follow_move+pin_move | tt_away | 1-0 | 100.0 | 50.0 | 50.0 | +0.85 | 84.7 |  |  | redundant -- identical record to pin_move alone, not independent confirmation |
| follow_move+pin_move | tt_home | 1-0 | 100.0 | 50.0 | 50.0 | +0.89 | 88.5 |  |  | redundant -- identical record to pin_move alone, not independent confirmation |
| follow_move+pin_value | tt_home | 2-0 | 100.0 | 50.0 | 50.0 | +1.81 | 90.5 |  |  | keep collecting (2/30) |
| pin_move+pin_value | tt_home | 1-0 | 100.0 | 50.0 | 50.0 | +0.89 | 88.5 |  |  | redundant -- identical record to pin_move alone, not independent confirmation |

## By ticket volume and Pinnacle limit (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| rlm_quiet | close | 40k+ bets | 14-33 | 29.8 | -7.7 | -38.8 |  |
| rlm_quiet | close | pin $10-50k | 7-8 | 46.7 | 3.8 | -11.1 |  |
| rlm_quiet | close | pin $50k+ | 7-25 | 21.9 | -13.0 | -51.8 |  |
| pin_move | close | 40k+ bets | 56-45 | 55.4 | 4.2 | -0.0 |  |
| pin_move | close | pin $10-50k | 25-15 | 62.5 | 11.0 | 14.6 |  |
| pin_move | close | pin $50k+ | 29-30 | 49.2 | -1.9 | -12.9 |  |
| pin_move | close | pin limit <$10k | 2-0 | 100.0 | 50.0 | 86.6 |  |
| money_delta | close | 40k+ bets | 15-30 | 33.3 | -5.4 | -28.3 |  |
| money_delta | close | pin $10-50k | 5-10 | 33.3 | -13.5 | -36.1 |  |
| money_delta | close | pin $50k+ | 10-20 | 33.3 | -1.4 | -24.5 |  |
| pin_rlm | close | 40k+ bets | 5-13 | 27.8 | -4.8 | -44.8 |  |
| pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| pin_rlm | close | pin $50k+ | 2-11 | 15.4 | -13.4 | -67.4 |  |
| pre_move | close | 40k+ bets | 4-10 | 28.6 | -9.1 | -31.6 |  |
| pre_move | close | pin $10-50k | 1-3 | 25.0 | -16.4 | -53.8 |  |
| pre_move | close | pin $50k+ | 3-7 | 30.0 | -6.2 | -22.7 |  |
| follow_move | close | 40k+ bets | 87-81 | 51.8 | 1.0 | -4.8 |  |
| follow_move | close | pin $10-50k | 21-13 | 61.8 | 11.2 | 10.3 |  |
| follow_move | close | pin $50k+ | 40-48 | 45.5 | -5.9 | -16.6 |  |
| follow_move | close | pin limit <$10k | 26-20 | 56.5 | 6.5 | 6.7 |  |
| rlm | close | 40k+ bets | 17-37 | 31.5 | -5.6 | -34.1 |  |
| rlm | close | pin $10-50k | 8-9 | 47.1 | 3.6 | -10.4 |  |
| rlm | close | pin $50k+ | 9-28 | 24.3 | -9.8 | -45.0 |  |
| rlm_ratio | close | 40k+ bets | 6-16 | 27.3 | -7.4 | -41.7 |  |
| rlm_ratio | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| rlm_ratio | close | pin $50k+ | 3-14 | 17.6 | -14.8 | -58.0 |  |
| money_level | close | 40k+ bets | 100-61 | 62.1 | 1.7 | 5.9 |  |
| money_level | close | pin $10-50k | 35-24 | 59.3 | 3.9 | 4.2 |  |
| money_level | close | pin $50k+ | 65-37 | 63.7 | 0.4 | 6.9 |  |
| sharp_gap | close | 40k+ bets | 74-86 | 46.2 | -2.3 | -12.6 |  |
| sharp_gap | close | pin $10-50k | 26-31 | 45.6 | -4.7 | -16.2 |  |
| sharp_gap | close | pin $50k+ | 48-55 | 46.6 | -1.0 | -10.6 |  |
| money_moving | close | 40k+ bets | 55-77 | 41.7 | -5.1 | -22.0 |  |
| money_moving | close | pin $10-50k | 21-28 | 42.9 | -6.9 | -21.8 |  |
| money_moving | close | pin $50k+ | 34-49 | 41.0 | -4.1 | -22.2 |  |
| pin_value | close | 40k+ bets | 72-63 | 53.3 | 4.8 | 0.6 |  |
| pin_value | close | pin $10-50k | 16-15 | 51.6 | 4.2 | -3.3 |  |
| pin_value | close | pin $50k+ | 21-14 | 60.0 | 13.2 | 16.1 |  |
| pin_value | close | pin limit <$10k | 35-34 | 50.7 | 0.7 | -5.5 |  |
| book_lag | close | 40k+ bets | 5-1 | 83.3 | 20.6 | 47.7 |  |
| book_lag | close | pin $50k+ | 5-1 | 83.3 | 20.6 | 47.7 |  |
| consensus_gap | close | 40k+ bets | 22-43 | 33.8 | 2.5 | -22.4 |  |
| consensus_gap | close | pin $10-50k | 1-7 | 12.5 | -17.7 | -83.9 |  |
| consensus_gap | close | pin $50k+ | 21-36 | 36.8 | 5.4 | -13.8 |  |
| follow_move+rlm | close | 40k+ bets | 17-37 | 31.5 | -5.6 | -34.1 |  |
| follow_move+rlm_quiet | close | 40k+ bets | 14-33 | 29.8 | -7.7 | -38.8 |  |
| follow_move+rlm_ratio | close | 40k+ bets | 6-16 | 27.3 | -7.4 | -41.7 |  |
| follow_move+sharp_gap | close | 40k+ bets | 31-36 | 46.3 | -3.3 | -13.1 |  |
| money_level+pin_value | close | 40k+ bets | 20-9 | 69.0 | 13.7 | 28.7 |  |
| rlm+rlm_quiet | close | 40k+ bets | 14-32 | 30.4 | -6.5 | -37.5 |  |
| rlm+rlm_ratio | close | 40k+ bets | 6-16 | 27.3 | -7.4 | -41.7 |  |
| rlm+sharp_gap | close | 40k+ bets | 10-22 | 31.2 | -6.7 | -35.9 |  |
| rlm_quiet+rlm_ratio | close | 40k+ bets | 3-12 | 20.0 | -13.8 | -59.9 |  |
| rlm_quiet+sharp_gap | close | 40k+ bets | 7-17 | 29.2 | -8.8 | -42.9 |  |
| rlm_ratio+sharp_gap | close | 40k+ bets | 6-16 | 27.3 | -7.4 | -41.7 |  |
| money_level+sharp_gap | close | 40k+ bets | 47-34 | 58.0 | -0.7 | 2.1 |  |
| consensus_gap+money_level | close | 40k+ bets | 7-3 | 70.0 | 13.8 | 28.6 |  |
| pre_move+sharp_gap | close | 40k+ bets | 4-10 | 28.6 | -9.1 | -31.6 |  |
| follow_move+money_level | close | 40k+ bets | 40-23 | 63.5 | 1.0 | 7.3 |  |
| book_lag+money_level | close | 40k+ bets | 2-1 | 66.7 | -4.8 | 13.4 |  |
| consensus_gap+pre_move | close | 40k+ bets | 1-4 | 20.0 | -3.6 | -22.0 |  |
| consensus_gap+sharp_gap | close | 40k+ bets | 11-23 | 32.4 | 2.1 | -23.3 |  |
| follow_move+pin_value | close | 40k+ bets | 15-8 | 65.2 | 14.5 | 21.2 |  |
| pin_value+rlm | close | 40k+ bets | 3-6 | 33.3 | -8.3 | -37.6 |  |
| pin_value+rlm_quiet | close | 40k+ bets | 3-6 | 33.3 | -8.3 | -37.6 |  |
| pin_value+pre_move | close | 40k+ bets | 1-2 | 33.3 | 1.8 | -38.4 |  |
| pin_value+sharp_gap | close | 40k+ bets | 20-17 | 54.1 | 7.5 | 0.1 |  |
| consensus_gap+follow_move | close | 40k+ bets | 7-17 | 29.2 | -0.5 | -33.1 |  |
| consensus_gap+rlm | close | 40k+ bets | 5-17 | 22.7 | -2.6 | -43.1 |  |
| consensus_gap+rlm_quiet | close | 40k+ bets | 3-16 | 15.8 | -9.9 | -59.9 |  |
| consensus_gap+pin_value | close | 40k+ bets | 4-11 | 26.7 | -1.5 | -39.8 |  |
| book_lag+consensus_gap | close | 40k+ bets | 3-0 | 100.0 | 46.1 | 82.0 |  |
| book_lag+money_moving | close | 40k+ bets | 1-0 | 100.0 | 61.8 | 78.1 |  |
| book_lag+pin_value | close | 40k+ bets | 2-0 | 100.0 | 50.0 | 80.7 |  |
| consensus_gap+money_moving | close | 40k+ bets | 8-20 | 28.6 | -0.2 | -33.1 |  |
| money_moving+pin_value | close | 40k+ bets | 13-14 | 48.1 | 2.8 | -11.1 |  |
| money_moving+pre_move | close | 40k+ bets | 1-5 | 16.7 | -18.2 | -68.8 |  |
| money_moving+sharp_gap | close | 40k+ bets | 36-51 | 41.4 | -4.7 | -19.8 |  |
| follow_move+money_moving | close | 40k+ bets | 23-34 | 40.4 | -7.8 | -24.7 |  |
| money_moving+rlm | close | 40k+ bets | 8-23 | 25.8 | -9.9 | -46.2 |  |
| money_moving+rlm_quiet | close | 40k+ bets | 5-18 | 21.7 | -13.1 | -57.0 |  |
| money_level+money_moving | close | 40k+ bets | 35-26 | 57.4 | -1.3 | 1.1 |  |
| money_level+pin_move | close | 40k+ bets | 34-15 | 69.4 | 6.8 | 16.3 |  |
| money_moving+pin_move | close | 40k+ bets | 26-27 | 49.1 | 1.1 | -9.9 |  |
| pin_move+pin_value | close | 40k+ bets | 16-14 | 53.3 | 7.1 | -0.8 |  |
| pin_move+sharp_gap | close | 40k+ bets | 28-27 | 50.9 | 2.7 | -5.2 |  |
| consensus_gap+pin_move | close | 40k+ bets | 6-11 | 35.3 | 6.3 | -22.4 |  |
| consensus_gap+money_delta | close | 40k+ bets | 5-6 | 45.5 | 21.8 | 18.6 |  |
| consensus_gap+pin_rlm | close | 40k+ bets | 2-8 | 20.0 | -3.6 | -57.6 |  |
| consensus_gap+rlm_ratio | close | 40k+ bets | 3-7 | 30.0 | 6.4 | -28.6 |  |
| follow_move+money_delta | close | 40k+ bets | 7-14 | 33.3 | -3.5 | -29.2 |  |
| follow_move+pin_rlm | close | 40k+ bets | 5-11 | 31.2 | -2.5 | -38.0 |  |
| money_delta+money_level | close | 40k+ bets | 3-5 | 37.5 | -1.8 | -22.0 |  |
| money_delta+money_moving | close | 40k+ bets | 14-25 | 35.9 | -2.2 | -22.2 |  |
| money_delta+pin_rlm | close | 40k+ bets | 4-9 | 30.8 | -2.4 | -38.0 |  |
| money_delta+rlm | close | 40k+ bets | 6-12 | 33.3 | -2.7 | -28.5 |  |
| money_delta+rlm_ratio | close | 40k+ bets | 5-9 | 35.7 | 2.2 | -21.7 |  |
| money_delta+sharp_gap | close | 40k+ bets | 13-26 | 33.3 | -4.8 | -27.2 |  |
| money_level+pin_rlm | close | 40k+ bets | 0-3 | 0.0 | -41.2 | -100.0 |  |
| money_level+rlm | close | 40k+ bets | 0-3 | 0.0 | -41.2 | -100.0 |  |
| money_level+rlm_ratio | close | 40k+ bets | 0-3 | 0.0 | -41.2 | -100.0 |  |
| money_moving+pin_rlm | close | 40k+ bets | 5-12 | 29.4 | -3.7 | -41.6 |  |
| money_moving+rlm_ratio | close | 40k+ bets | 6-13 | 31.6 | -2.1 | -32.5 |  |
| pin_rlm+rlm | close | 40k+ bets | 5-11 | 31.2 | -2.5 | -38.0 |  |
| pin_rlm+rlm_ratio | close | 40k+ bets | 5-11 | 31.2 | -2.5 | -38.0 |  |
| pin_rlm+sharp_gap | close | 40k+ bets | 5-13 | 27.8 | -4.8 | -44.8 |  |
| follow_move+pin_move | close | 40k+ bets | 47-36 | 56.6 | 4.2 | 1.1 |  |
| pin_move+rlm_quiet | close | 40k+ bets | 12-21 | 36.4 | -2.9 | -24.7 |  |
| money_delta+pin_move | close | 40k+ bets | 7-13 | 35.0 | -4.4 | -31.0 |  |
| money_delta+pin_value | close | 40k+ bets | 1-7 | 12.5 | -25.5 | -77.1 |  |
| money_delta+rlm_quiet | close | 40k+ bets | 3-7 | 30.0 | -4.5 | -39.4 |  |
| pin_move+pin_rlm | close | 40k+ bets | 5-11 | 31.2 | -2.5 | -38.0 |  |
| pin_move+rlm | close | 40k+ bets | 14-23 | 37.8 | -1.4 | -22.3 |  |
| pin_move+rlm_ratio | close | 40k+ bets | 5-9 | 35.7 | 0.5 | -29.1 |  |
| pin_rlm+pin_value | close | 40k+ bets | 1-5 | 16.7 | -14.8 | -68.8 |  |
| pin_rlm+rlm_quiet | close | 40k+ bets | 3-8 | 27.3 | -4.1 | -45.3 |  |
| pin_value+rlm_ratio | close | 40k+ bets | 1-3 | 25.0 | -10.5 | -53.2 |  |
| money_delta+pre_move | close | 40k+ bets | 1-3 | 25.0 | -9.5 | -53.2 |  |
| money_level+pre_move | close | 40k+ bets | 1-1 | 50.0 | 11.8 | -6.5 |  |
| pin_move+pre_move | close | 40k+ bets | 0-1 | 0.0 | -23.6 | -100.0 |  |
| pin_rlm+pre_move | close | 40k+ bets | 0-1 | 0.0 | -23.6 | -100.0 |  |
| money_level+sharp_gap | close | pin $10-50k | 17-14 | 54.8 | 0.2 | -1.1 |  |
| pin_value+pre_move | close | pin $10-50k | 1-0 | 100.0 | 52.7 | 84.7 |  |
| pin_value+sharp_gap | close | pin $10-50k | 9-9 | 50.0 | 2.3 | -6.3 |  |
| pre_move+sharp_gap | close | pin $10-50k | 1-3 | 25.0 | -16.4 | -53.8 |  |
| money_level+pin_value | close | pin $10-50k | 9-4 | 69.2 | 16.9 | 30.2 |  |
| consensus_gap+pin_value | close | pin $10-50k | 0-3 | 0.0 | -23.6 | -100.0 |  |
| follow_move+money_level | close | pin $10-50k | 13-3 | 81.2 | 23.0 | 39.1 |  |
| follow_move+sharp_gap | close | pin $10-50k | 10-9 | 52.6 | 1.8 | -5.6 |  |
| money_moving+pre_move | close | pin $10-50k | 0-2 | 0.0 | -35.5 | -100.0 |  |
| money_moving+sharp_gap | close | pin $10-50k | 12-18 | 40.0 | -9.4 | -25.1 |  |
| consensus_gap+money_level | close | pin $10-50k | 1-0 | 100.0 | 23.6 | 28.6 |  |
| consensus_gap+sharp_gap | close | pin $10-50k | 1-3 | 25.0 | -11.8 | -67.8 |  |
| follow_move+money_moving | close | pin $10-50k | 9-9 | 50.0 | 0.3 | -10.1 |  |
| follow_move+rlm | close | pin $10-50k | 8-9 | 47.1 | 3.6 | -10.4 |  |
| follow_move+rlm_quiet | close | pin $10-50k | 7-8 | 46.7 | 3.8 | -11.1 |  |
| money_moving+rlm | close | pin $10-50k | 4-6 | 40.0 | -3.1 | -24.0 |  |
| money_moving+rlm_quiet | close | pin $10-50k | 3-5 | 37.5 | -4.5 | -28.9 |  |
| rlm+rlm_quiet | close | pin $10-50k | 7-8 | 46.7 | 3.8 | -11.1 |  |
| money_level+money_moving | close | pin $10-50k | 13-10 | 56.5 | 0.7 | 0.3 |  |
| money_level+pin_move | close | pin $10-50k | 15-5 | 75.0 | 19.0 | 34.0 |  |
| money_moving+pin_move | close | pin $10-50k | 14-11 | 56.0 | 4.7 | 2.4 |  |
| money_moving+pin_value | close | pin $10-50k | 5-7 | 41.7 | -6.8 | -21.9 |  |
| pin_move+pin_value | close | pin $10-50k | 9-8 | 52.9 | 4.2 | -0.4 |  |
| pin_move+sharp_gap | close | pin $10-50k | 13-11 | 54.2 | 3.9 | 1.6 |  |
| money_delta+money_level | close | pin $10-50k | 1-0 | 100.0 | 47.3 | 90.9 |  |
| money_delta+money_moving | close | pin $10-50k | 5-8 | 38.5 | -8.3 | -26.2 |  |
| money_delta+sharp_gap | close | pin $10-50k | 4-9 | 30.8 | -15.9 | -41.3 |  |
| follow_move+money_delta | close | pin $10-50k | 3-5 | 37.5 | -6.8 | -28.4 |  |
| follow_move+pin_move | close | pin $10-50k | 20-11 | 64.5 | 13.1 | 17.5 |  |
| follow_move+pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| follow_move+pin_value | close | pin $10-50k | 5-4 | 55.6 | 9.1 | 4.8 |  |
| follow_move+rlm_ratio | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| money_delta+pin_move | close | pin $10-50k | 3-7 | 30.0 | -15.5 | -42.7 |  |
| money_delta+pin_rlm | close | pin $10-50k | 2-2 | 50.0 | 8.6 | -4.5 |  |
| money_delta+pin_value | close | pin $10-50k | 0-5 | 0.0 | -43.6 | -100.0 |  |
| money_delta+rlm | close | pin $10-50k | 3-4 | 42.9 | -1.0 | -18.2 |  |
| money_delta+rlm_quiet | close | pin $10-50k | 2-3 | 40.0 | -2.5 | -23.6 |  |
| money_delta+rlm_ratio | close | pin $10-50k | 2-2 | 50.0 | 8.6 | -4.5 |  |
| money_moving+pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| money_moving+rlm_ratio | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| pin_move+pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| pin_move+rlm | close | pin $10-50k | 8-7 | 53.3 | 7.3 | 1.6 |  |
| pin_move+rlm_quiet | close | pin $10-50k | 7-6 | 53.8 | 8.0 | 2.5 |  |
| pin_move+rlm_ratio | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| pin_rlm+pin_value | close | pin $10-50k | 1-2 | 33.3 | -6.1 | -37.7 |  |
| pin_rlm+rlm | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| pin_rlm+rlm_quiet | close | pin $10-50k | 2-2 | 50.0 | 8.6 | -5.5 |  |
| pin_rlm+rlm_ratio | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| pin_rlm+sharp_gap | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| pin_value+rlm | close | pin $10-50k | 2-4 | 33.3 | -10.9 | -37.6 |  |
| pin_value+rlm_quiet | close | pin $10-50k | 2-4 | 33.3 | -10.9 | -37.6 |  |
| pin_value+rlm_ratio | close | pin $10-50k | 1-2 | 33.3 | -6.1 | -37.7 |  |
| rlm+rlm_ratio | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| rlm+sharp_gap | close | pin $10-50k | 5-5 | 50.0 | 5.1 | -5.3 |  |
| rlm_quiet+rlm_ratio | close | pin $10-50k | 2-2 | 50.0 | 8.6 | -5.5 |  |
| rlm_quiet+sharp_gap | close | pin $10-50k | 4-4 | 50.0 | 5.7 | -5.5 |  |
| rlm_ratio+sharp_gap | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| consensus_gap+follow_move | close | pin $10-50k | 0-2 | 0.0 | -23.6 | -100.0 |  |
| consensus_gap+rlm | close | pin $10-50k | 0-2 | 0.0 | -23.6 | -100.0 |  |
| consensus_gap+rlm_quiet | close | pin $10-50k | 0-2 | 0.0 | -23.6 | -100.0 |  |
| consensus_gap+money_delta | close | pin $10-50k | 0-1 | 0.0 | -23.6 | -100.0 |  |
| consensus_gap+money_moving | close | pin $10-50k | 0-3 | 0.0 | -23.6 | -100.0 |  |
| consensus_gap+pin_move | close | pin $10-50k | 0-1 | 0.0 | -23.6 | -100.0 |  |
| consensus_gap+pin_rlm | close | pin $10-50k | 0-1 | 0.0 | -23.6 | -100.0 |  |
| consensus_gap+rlm_ratio | close | pin $10-50k | 0-1 | 0.0 | -23.6 | -100.0 |  |
| consensus_gap+pre_move | close | pin $10-50k | 0-1 | 0.0 | -23.6 | -100.0 |  |
| follow_move+rlm | close | pin $50k+ | 9-28 | 24.3 | -9.8 | -45.0 |  |
| follow_move+rlm_quiet | close | pin $50k+ | 7-25 | 21.9 | -13.0 | -51.8 |  |
| follow_move+rlm_ratio | close | pin $50k+ | 3-14 | 17.6 | -14.8 | -58.0 |  |
| follow_move+sharp_gap | close | pin $50k+ | 21-27 | 43.8 | -5.3 | -16.1 |  |
| money_level+pin_value | close | pin $50k+ | 11-5 | 68.8 | 11.0 | 27.5 |  |
| rlm+rlm_quiet | close | pin $50k+ | 7-24 | 22.6 | -11.4 | -50.2 |  |
| rlm+rlm_ratio | close | pin $50k+ | 3-14 | 17.6 | -14.8 | -58.0 |  |
| rlm+sharp_gap | close | pin $50k+ | 5-17 | 22.7 | -12.1 | -49.8 |  |
| rlm_quiet+rlm_ratio | close | pin $50k+ | 1-10 | 9.1 | -22.0 | -79.6 |  |
| rlm_quiet+sharp_gap | close | pin $50k+ | 3-13 | 18.8 | -16.0 | -61.6 |  |
| rlm_ratio+sharp_gap | close | pin $50k+ | 3-14 | 17.6 | -14.8 | -58.0 |  |
| consensus_gap+money_level | close | pin $50k+ | 6-3 | 66.7 | 12.7 | 28.6 |  |
| pre_move+sharp_gap | close | pin $50k+ | 3-7 | 30.0 | -6.2 | -22.7 |  |
| follow_move+money_level | close | pin $50k+ | 27-20 | 57.4 | -6.4 | -3.5 |  |
| book_lag+money_level | close | pin $50k+ | 2-1 | 66.7 | -4.8 | 13.4 |  |
| consensus_gap+pre_move | close | pin $50k+ | 1-3 | 25.0 | 1.4 | -2.5 |  |
| consensus_gap+sharp_gap | close | pin $50k+ | 10-20 | 33.3 | 3.9 | -17.3 |  |
| follow_move+pin_value | close | pin $50k+ | 8-4 | 66.7 | 12.7 | 22.0 |  |
| pin_value+rlm | close | pin $50k+ | 1-2 | 33.3 | -3.0 | -37.7 |  |
| pin_value+rlm_quiet | close | pin $50k+ | 1-2 | 33.3 | -3.0 | -37.7 |  |
| money_level+sharp_gap | close | pin $50k+ | 30-20 | 60.0 | -1.2 | 4.1 |  |
| consensus_gap+follow_move | close | pin $50k+ | 7-15 | 31.8 | 1.7 | -27.0 |  |
| consensus_gap+rlm | close | pin $50k+ | 5-15 | 25.0 | -0.5 | -37.4 |  |
| consensus_gap+rlm_quiet | close | pin $50k+ | 3-14 | 17.6 | -8.2 | -55.2 |  |
| consensus_gap+pin_value | close | pin $50k+ | 4-8 | 33.3 | 4.1 | -24.8 |  |
| pin_value+pre_move | close | pin $50k+ | 0-2 | 0.0 | -23.6 | -100.0 |  |
| pin_value+sharp_gap | close | pin $50k+ | 11-8 | 57.9 | 12.3 | 6.2 |  |
| book_lag+consensus_gap | close | pin $50k+ | 3-0 | 100.0 | 46.1 | 82.0 |  |
| book_lag+money_moving | close | pin $50k+ | 1-0 | 100.0 | 61.8 | 78.1 |  |
| book_lag+pin_value | close | pin $50k+ | 2-0 | 100.0 | 50.0 | 80.7 |  |
| consensus_gap+money_moving | close | pin $50k+ | 8-17 | 32.0 | 2.6 | -25.1 |  |
| money_moving+pin_value | close | pin $50k+ | 8-7 | 53.3 | 10.5 | -2.6 |  |
| consensus_gap+pin_move | close | pin $50k+ | 6-10 | 37.5 | 8.2 | -17.6 |  |
| money_moving+pin_move | close | pin $50k+ | 12-16 | 42.9 | -2.2 | -20.9 |  |
| pin_move+pin_value | close | pin $50k+ | 6-6 | 50.0 | 7.6 | -8.9 |  |
| consensus_gap+money_delta | close | pin $50k+ | 5-5 | 50.0 | 26.4 | 30.5 |  |
| consensus_gap+pin_rlm | close | pin $50k+ | 2-7 | 22.2 | -1.4 | -52.9 |  |
| consensus_gap+rlm_ratio | close | pin $50k+ | 3-6 | 33.3 | 9.7 | -20.7 |  |
| follow_move+money_delta | close | pin $50k+ | 4-9 | 30.8 | -1.4 | -29.7 |  |
| follow_move+money_moving | close | pin $50k+ | 14-25 | 35.9 | -11.5 | -31.4 |  |
| follow_move+pin_rlm | close | pin $50k+ | 2-9 | 18.2 | -11.6 | -61.5 |  |
| money_delta+money_level | close | pin $50k+ | 2-5 | 28.6 | -8.8 | -38.1 |  |
| money_delta+money_moving | close | pin $50k+ | 9-17 | 34.6 | 0.8 | -20.2 |  |
| money_delta+pin_rlm | close | pin $50k+ | 2-7 | 22.2 | -7.3 | -52.9 |  |
| money_delta+rlm | close | pin $50k+ | 3-8 | 27.3 | -3.8 | -35.1 |  |
| money_delta+rlm_ratio | close | pin $50k+ | 3-7 | 30.0 | -0.4 | -28.6 |  |
| money_delta+sharp_gap | close | pin $50k+ | 9-17 | 34.6 | 0.8 | -20.2 |  |
| money_level+money_moving | close | pin $50k+ | 22-16 | 57.9 | -2.4 | 1.6 |  |
| money_level+pin_rlm | close | pin $50k+ | 0-3 | 0.0 | -41.2 | -100.0 |  |
| money_level+rlm | close | pin $50k+ | 0-3 | 0.0 | -41.2 | -100.0 |  |
| money_level+rlm_ratio | close | pin $50k+ | 0-3 | 0.0 | -41.2 | -100.0 |  |
| money_moving+pin_rlm | close | pin $50k+ | 2-10 | 16.7 | -12.6 | -64.7 |  |
| money_moving+rlm | close | pin $50k+ | 4-17 | 19.0 | -13.1 | -56.7 |  |
| money_moving+rlm_ratio | close | pin $50k+ | 3-11 | 21.4 | -9.1 | -49.0 |  |
| money_moving+sharp_gap | close | pin $50k+ | 24-33 | 42.1 | -2.2 | -17.0 |  |
| pin_rlm+rlm | close | pin $50k+ | 2-9 | 18.2 | -11.6 | -61.5 |  |
| pin_rlm+rlm_ratio | close | pin $50k+ | 2-9 | 18.2 | -11.6 | -61.5 |  |
| pin_rlm+sharp_gap | close | pin $50k+ | 2-11 | 15.4 | -13.4 | -67.4 |  |
| follow_move+pin_move | close | pin $50k+ | 25-25 | 50.0 | -3.1 | -12.4 |  |
| pin_move+rlm_quiet | close | pin $50k+ | 5-15 | 25.0 | -9.9 | -42.4 |  |
| money_delta+pin_move | close | pin $50k+ | 4-6 | 40.0 | 6.7 | -19.3 |  |
| money_delta+pin_value | close | pin $50k+ | 1-2 | 33.3 | 4.8 | -38.9 |  |
| money_delta+rlm_quiet | close | pin $50k+ | 1-4 | 20.0 | -6.5 | -55.2 |  |
| money_moving+rlm_quiet | close | pin $50k+ | 2-13 | 13.3 | -17.7 | -72.1 |  |
| pin_move+pin_rlm | close | pin $50k+ | 2-9 | 18.2 | -11.6 | -61.5 |  |
| pin_move+rlm | close | pin $50k+ | 6-16 | 27.3 | -7.3 | -38.5 |  |
| pin_move+rlm_ratio | close | pin $50k+ | 2-7 | 22.2 | -8.9 | -52.9 |  |
| pin_move+sharp_gap | close | pin $50k+ | 15-16 | 48.4 | 1.7 | -10.4 |  |
| pin_rlm+pin_value | close | pin $50k+ | 0-3 | 0.0 | -23.6 | -100.0 |  |
| pin_rlm+rlm_quiet | close | pin $50k+ | 1-6 | 14.3 | -11.4 | -68.0 |  |
| pin_value+rlm_ratio | close | pin $50k+ | 0-1 | 0.0 | -23.6 | -100.0 |  |
| money_delta+pre_move | close | pin $50k+ | 1-3 | 25.0 | -9.5 | -53.2 |  |
| money_level+pre_move | close | pin $50k+ | 1-1 | 50.0 | 11.8 | -6.5 |  |
| money_moving+pre_move | close | pin $50k+ | 1-3 | 25.0 | -9.5 | -53.2 |  |
| money_level+pin_move | close | pin $50k+ | 19-10 | 65.5 | -1.6 | 4.1 |  |
| pin_move+pre_move | close | pin $50k+ | 0-1 | 0.0 | -23.6 | -100.0 |  |
| pin_rlm+pre_move | close | pin $50k+ | 0-1 | 0.0 | -23.6 | -100.0 |  |
| follow_move+pin_move | close | pin limit <$10k | 2-0 | 100.0 | 50.0 | 86.6 |  |
| follow_move+pin_value | close | pin limit <$10k | 2-0 | 100.0 | 50.0 | 90.5 |  |
| pin_move+pin_value | close | pin limit <$10k | 1-0 | 100.0 | 50.0 | 88.5 |  |
| rlm_quiet | early | 40k+ bets | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| rlm_quiet | early | <10k bets | 3-7 | 30.0 | -16.2 | -43.3 | 0.05 |
| rlm_quiet | early | pin $10-50k | 3-3 | 50.0 | 3.9 | -5.6 | 0.17 |
| rlm_quiet | early | pin $50k+ | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| rlm_quiet | early | pin limit <$10k | 0-3 | 0.0 | -49.1 | -100.0 | -0.17 |
| pin_move | early | <10k bets | 21-19 | 52.5 | -8.7 | -12.8 | 0.75 |
| pin_move | early | pin $10-50k | 3-1 | 75.0 | 19.1 | 43.3 | 0.25 |
| pin_move | early | pin limit <$10k | 18-18 | 50.0 | -11.8 | -19.0 | 0.81 |
| pin_rlm | early | <10k bets | 2-6 | 25.0 | -1.6 | -49.6 | -0.96 |
| pin_rlm | early | pin $10-50k | 1-1 | 50.0 | 26.4 | 4.0 | -1.4 |
| pin_rlm | early | pin limit <$10k | 1-5 | 16.7 | -10.9 | -67.5 | -0.82 |
| pre_move | early | 10-40k bets | 1-1 | 50.0 | 26.4 | 23.0 | 0.55 |
| pre_move | early | 40k+ bets | 0-1 | 0.0 | -47.3 | -100.0 | 0.0 |
| pre_move | early | <10k bets | 12-25 | 32.4 | -0.8 | -29.8 | -0.46 |
| pre_move | early | pin $10-50k | 2-4 | 33.3 | -3.0 | -24.3 | -0.55 |
| pre_move | early | pin $50k+ | 0-1 | 0.0 | -23.6 | -100.0 | 2.1 |
| pre_move | early | pin limit <$10k | 9-19 | 32.1 | 0.2 | -30.0 | -0.2 |
| follow_move | early | 10-40k bets | 1-0 | 100.0 | 38.2 | 82.0 | 0.0 |
| follow_move | early | 40k+ bets | 1-1 | 50.0 | 11.8 | -8.4 | 0.0 |
| follow_move | early | <10k bets | 15-18 | 45.5 | -7.5 | -13.4 | -0.2 |
| follow_move | early | pin $10-50k | 9-7 | 56.2 | 4.8 | 7.3 | 0.16 |
| follow_move | early | pin $50k+ | 2-1 | 66.7 | 20.6 | 21.8 | 0.0 |
| follow_move | early | pin limit <$10k | 5-8 | 38.5 | -19.0 | -27.6 | -0.43 |
| rlm | early | 40k+ bets | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| rlm | early | <10k bets | 2-7 | 22.2 | -22.2 | -57.4 | 0.06 |
| rlm | early | pin $10-50k | 2-3 | 40.0 | -2.9 | -23.3 | 0.2 |
| rlm | early | pin $50k+ | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| rlm | early | pin limit <$10k | 0-3 | 0.0 | -49.1 | -100.0 | -0.17 |
| rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| rlm_ratio | early | <10k bets | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm_ratio | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| money_level | early | 10-40k bets | 3-3 | 50.0 | -8.8 | -13.8 | -0.28 |
| money_level | early | 40k+ bets | 4-4 | 50.0 | -13.2 | -19.9 | -0.06 |
| money_level | early | <10k bets | 85-40 | 68.0 | 7.9 | 16.8 | -0.16 |
| money_level | early | pin $10-50k | 19-15 | 55.9 | -1.3 | 3.8 | 0.06 |
| money_level | early | pin $50k+ | 5-2 | 71.4 | 6.8 | 20.1 | -0.36 |
| money_level | early | pin limit <$10k | 61-25 | 70.9 | 10.0 | 17.7 | -0.25 |
| sharp_gap | early | 10-40k bets | 3-3 | 50.0 | 3.9 | 3.1 | 0.27 |
| sharp_gap | early | 40k+ bets | 4-5 | 44.4 | -13.3 | -29.5 | -0.06 |
| sharp_gap | early | <10k bets | 67-51 | 56.8 | 9.4 | 8.1 | -0.01 |
| sharp_gap | early | pin $10-50k | 19-13 | 59.4 | 8.6 | 13.1 | 0.07 |
| sharp_gap | early | pin $50k+ | 3-5 | 37.5 | -17.3 | -37.5 | 0.33 |
| sharp_gap | early | pin limit <$10k | 45-36 | 55.6 | 9.2 | 4.6 | -0.06 |
| money_moving | early | <10k bets | 15-9 | 62.5 | 10.5 | 14.1 | -0.03 |
| money_moving | early | pin $10-50k | 5-2 | 71.4 | 21.8 | 40.0 | -0.16 |
| money_moving | early | pin limit <$10k | 9-6 | 60.0 | 5.7 | 4.2 | 0.16 |
| pin_value | early | 10-40k bets | 1-2 | 33.3 | -20.6 | -39.3 | 0.0 |
| pin_value | early | 40k+ bets | 4-2 | 66.7 | 20.2 | 22.5 | 0.0 |
| pin_value | early | <10k bets | 36-33 | 52.2 | 3.6 | -2.2 | 0.22 |
| pin_value | early | pin $10-50k | 11-4 | 73.3 | 13.7 | 39.3 | 0.03 |
| pin_value | early | pin $50k+ | 3-0 | 100.0 | 53.9 | 81.1 | 0.0 |
| pin_value | early | pin limit <$10k | 27-33 | 45.0 | -1.0 | -16.1 | 0.24 |
| book_lag | early | <10k bets | 5-3 | 62.5 | 16.1 | 19.3 | -0.14 |
| book_lag | early | pin $10-50k | 2-2 | 50.0 | 3.6 | -1.2 | 0.6 |
| book_lag | early | pin limit <$10k | 2-1 | 66.7 | 12.7 | 8.5 | -0.37 |
| consensus_gap | early | 10-40k bets | 2-2 | 50.0 | 7.3 | 7.0 | 0.4 |
| consensus_gap | early | 40k+ bets | 2-2 | 50.0 | 22.7 | -6.4 | 0.17 |
| consensus_gap | early | <10k bets | 21-37 | 36.2 | 2.7 | -20.3 | -0.07 |
| consensus_gap | early | pin $10-50k | 8-7 | 53.3 | 9.0 | 10.8 | -0.04 |
| consensus_gap | early | pin $50k+ | 3-3 | 50.0 | 11.2 | -7.3 | 0.43 |
| consensus_gap | early | pin limit <$10k | 11-29 | 27.5 | -1.8 | -37.4 | -0.19 |
| consensus_gap+follow_move | early | 10-40k bets | 1-0 | 100.0 | 38.2 | 82.0 | 0.0 |
| consensus_gap+money_level | early | 10-40k bets | 1-0 | 100.0 | 38.2 | 82.0 | 0.0 |
| consensus_gap+pin_value | early | 10-40k bets | 1-0 | 100.0 | 38.2 | 82.0 | 0.0 |
| consensus_gap+sharp_gap | early | 10-40k bets | 2-2 | 50.0 | 7.3 | 7.0 | 0.4 |
| follow_move+money_level | early | 10-40k bets | 1-0 | 100.0 | 38.2 | 82.0 | 0.0 |
| follow_move+pin_value | early | 10-40k bets | 1-0 | 100.0 | 38.2 | 82.0 | 0.0 |
| follow_move+sharp_gap | early | 10-40k bets | 1-0 | 100.0 | 38.2 | 82.0 | 0.0 |
| money_level+pin_value | early | 10-40k bets | 1-0 | 100.0 | 38.2 | 82.0 | 0.0 |
| money_level+sharp_gap | early | 10-40k bets | 1-1 | 50.0 | -7.3 | -9.0 | 0.0 |
| pin_value+sharp_gap | early | 10-40k bets | 1-0 | 100.0 | 38.2 | 82.0 | 0.0 |
| consensus_gap+pre_move | early | 10-40k bets | 1-1 | 50.0 | 26.4 | 23.0 | 0.55 |
| pre_move+sharp_gap | early | 10-40k bets | 1-1 | 50.0 | 26.4 | 23.0 | 0.55 |
| follow_move+rlm | early | 40k+ bets | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| follow_move+rlm_quiet | early | 40k+ bets | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | 40k+ bets | 1-1 | 50.0 | 11.8 | -8.4 | 0.0 |
| rlm+rlm_quiet | early | 40k+ bets | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| rlm+rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| rlm+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| rlm_quiet+rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| rlm_quiet+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| rlm_ratio+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| money_level+pin_value | early | 40k+ bets | 0-1 | 0.0 | -52.7 | -100.0 | 0.0 |
| money_level+sharp_gap | early | 40k+ bets | 3-4 | 42.9 | -20.5 | -35.5 | -0.07 |
| pin_value+sharp_gap | early | 40k+ bets | 1-1 | 50.0 | 4.5 | -8.4 | 0.0 |
| consensus_gap+pin_value | early | 40k+ bets | 1-0 | 100.0 | 61.8 | 78.1 | 0.0 |
| money_level+pre_move | early | 40k+ bets | 0-1 | 0.0 | -47.3 | -100.0 | 0.0 |
| pre_move+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -47.3 | -100.0 | 0.0 |
| follow_move+pin_value | early | 40k+ bets | 1-0 | 100.0 | 61.8 | 83.3 | 0.0 |
| follow_move+money_level | early | <10k bets | 12-8 | 60.0 | 1.5 | 14.6 | -0.23 |
| follow_move+money_moving | early | <10k bets | 3-2 | 60.0 | 0.0 | 7.5 | -0.62 |
| follow_move+pin_value | early | <10k bets | 4-2 | 66.7 | 4.8 | 25.9 | 0.33 |
| follow_move+sharp_gap | early | <10k bets | 11-7 | 61.1 | 5.9 | 18.6 | 0.08 |
| money_level+money_moving | early | <10k bets | 10-3 | 76.9 | 17.5 | 35.1 | -0.47 |
| money_level+pin_value | early | <10k bets | 14-5 | 73.7 | 17.0 | 39.4 | 0.18 |
| money_level+sharp_gap | early | <10k bets | 49-19 | 72.1 | 15.5 | 31.3 | -0.14 |
| money_moving+pin_value | early | <10k bets | 5-2 | 71.4 | 23.9 | 36.6 | 1.0 |
| money_moving+sharp_gap | early | <10k bets | 7-3 | 70.0 | 20.5 | 31.5 | 0.03 |
| pin_value+sharp_gap | early | <10k bets | 15-10 | 60.0 | 13.6 | 13.4 | 0.68 |
| consensus_gap+follow_move | early | <10k bets | 1-2 | 33.3 | -15.8 | -38.9 | 0.5 |
| consensus_gap+rlm | early | <10k bets | 0-1 | 0.0 | -23.6 | -100.0 | 0.5 |
| consensus_gap+rlm_quiet | early | <10k bets | 0-1 | 0.0 | -23.6 | -100.0 | 0.5 |
| follow_move+rlm | early | <10k bets | 2-7 | 22.2 | -22.2 | -57.4 | 0.06 |
| follow_move+rlm_quiet | early | <10k bets | 3-7 | 30.0 | -16.2 | -43.3 | 0.05 |
| rlm+rlm_quiet | early | <10k bets | 2-7 | 22.2 | -22.2 | -57.4 | 0.06 |
| pin_move+pin_value | early | <10k bets | 4-5 | 44.4 | -12.7 | -16.5 | 0.78 |
| consensus_gap+pin_move | early | <10k bets | 1-3 | 25.0 | -17.7 | -53.2 | 0.15 |
| consensus_gap+sharp_gap | early | <10k bets | 15-22 | 40.5 | 7.5 | -14.8 | 0.02 |
| pin_move+sharp_gap | early | <10k bets | 12-5 | 70.6 | 11.8 | 29.3 | 0.68 |
| consensus_gap+money_level | early | <10k bets | 10-3 | 76.9 | 20.6 | 37.5 | -0.38 |
| book_lag+consensus_gap | early | <10k bets | 3-2 | 60.0 | 25.8 | 25.8 | 0.68 |
| money_level+pre_move | early | <10k bets | 2-3 | 40.0 | 0.0 | -24.4 | -1.92 |
| pre_move+sharp_gap | early | <10k bets | 12-25 | 32.4 | -0.8 | -29.8 | -0.46 |
| consensus_gap+pin_value | early | <10k bets | 4-12 | 25.0 | -14.8 | -53.5 | 0.91 |
| money_level+pin_move | early | <10k bets | 19-6 | 76.0 | 8.7 | 24.2 | 0.89 |
| money_moving+pin_move | early | <10k bets | 1-0 | 100.0 | 61.8 | 95.2 | -2.0 |
| consensus_gap+pin_rlm | early | <10k bets | 1-6 | 14.3 | -9.4 | -70.3 | -1.24 |
| consensus_gap+pre_move | early | <10k bets | 5-17 | 22.7 | -0.9 | -42.5 | -0.71 |
| money_level+pin_rlm | early | <10k bets | 0-1 | 0.0 | -23.6 | -100.0 | -10.6 |
| pin_rlm+pre_move | early | <10k bets | 2-6 | 25.0 | -1.6 | -49.6 | -0.96 |
| pin_rlm+sharp_gap | early | <10k bets | 2-6 | 25.0 | -1.6 | -49.6 | -0.96 |
| book_lag+money_level | early | <10k bets | 3-1 | 75.0 | 9.5 | 28.1 | -0.88 |
| book_lag+money_moving | early | <10k bets | 1-1 | 50.0 | 7.3 | 4.0 | -0.05 |
| book_lag+sharp_gap | early | <10k bets | 4-1 | 80.0 | 33.5 | 63.2 | 0.1 |
| money_moving+rlm_quiet | early | <10k bets | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| pin_value+rlm_quiet | early | <10k bets | 1-0 | 100.0 | 38.2 | 83.3 | 0.0 |
| pin_value+pre_move | early | <10k bets | 2-6 | 25.0 | -4.5 | -53.2 | 1.55 |
| consensus_gap+money_moving | early | <10k bets | 2-1 | 66.7 | 38.2 | 31.7 | 2.63 |
| money_moving+pre_move | early | <10k bets | 2-1 | 66.7 | 35.2 | 34.4 | 1.63 |
| pin_rlm+pin_value | early | <10k bets | 0-2 | 0.0 | -23.6 | -100.0 | 0.9 |
| book_lag+pin_rlm | early | <10k bets | 1-0 | 100.0 | 76.4 | 108.0 | 1.9 |
| book_lag+pre_move | early | <10k bets | 2-0 | 100.0 | 76.4 | 121.0 | -0.25 |
| money_moving+pin_rlm | early | <10k bets | 1-0 | 100.0 | 76.4 | 108.0 | 1.9 |
| follow_move+rlm_ratio | early | <10k bets | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm+rlm_ratio | early | <10k bets | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm+sharp_gap | early | <10k bets | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm_quiet+rlm_ratio | early | <10k bets | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm_quiet+sharp_gap | early | <10k bets | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm_ratio+sharp_gap | early | <10k bets | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| follow_move+pin_move | early | <10k bets | 3-5 | 37.5 | -24.3 | -27.3 | -0.25 |
| money_moving+rlm | early | <10k bets | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| pin_move+rlm | early | <10k bets | 0-2 | 0.0 | -61.8 | -100.0 | -0.5 |
| pin_move+rlm_quiet | early | <10k bets | 0-2 | 0.0 | -61.8 | -100.0 | -0.5 |
| pin_move+pin_rlm | early | <10k bets | 1-1 | 50.0 | 14.5 | -2.4 | 1.0 |
| pin_move+pre_move | early | <10k bets | 1-1 | 50.0 | 14.5 | -2.4 | 1.0 |
| book_lag+pin_move | early | <10k bets | 3-0 | 100.0 | 33.3 | 70.8 | -0.5 |
| book_lag+pin_value | early | <10k bets | 2-0 | 100.0 | 38.2 | 87.0 | 1.5 |
| money_level+pin_value | early | pin $10-50k | 8-2 | 80.0 | 19.1 | 52.0 | 0.15 |
| money_level+sharp_gap | early | pin $10-50k | 14-8 | 63.6 | 8.4 | 18.3 | 0.11 |
| pin_value+sharp_gap | early | pin $10-50k | 6-1 | 85.7 | 25.2 | 63.7 | 0.21 |
| money_level+pre_move | early | pin $10-50k | 0-2 | 0.0 | -42.7 | -100.0 | 0.0 |
| pre_move+sharp_gap | early | pin $10-50k | 2-4 | 33.3 | -3.0 | -24.3 | -0.55 |
| consensus_gap+pre_move | early | pin $10-50k | 2-1 | 66.7 | 43.0 | 51.3 | -1.27 |
| consensus_gap+sharp_gap | early | pin $10-50k | 5-1 | 83.3 | 40.6 | 68.6 | -0.38 |
| follow_move+money_level | early | pin $10-50k | 6-3 | 66.7 | 10.1 | 27.7 | 0.33 |
| follow_move+money_moving | early | pin $10-50k | 2-0 | 100.0 | 38.2 | 90.6 | 0.0 |
| follow_move+pin_value | early | pin $10-50k | 4-0 | 100.0 | 38.2 | 88.9 | 0.25 |
| follow_move+sharp_gap | early | pin $10-50k | 6-3 | 66.7 | 12.7 | 27.7 | 0.33 |
| money_level+money_moving | early | pin $10-50k | 2-1 | 66.7 | 12.7 | 31.1 | -1.33 |
| money_moving+pin_value | early | pin $10-50k | 3-1 | 75.0 | 19.1 | 44.1 | 0.25 |
| money_moving+sharp_gap | early | pin $10-50k | 2-1 | 66.7 | 17.6 | 35.3 | -0.03 |
| book_lag+consensus_gap | early | pin $10-50k | 1-1 | 50.0 | 19.1 | 4.0 | 1.2 |
| money_level+pin_move | early | pin $10-50k | 3-1 | 75.0 | 19.1 | 43.3 | 0.25 |
| money_moving+pin_move | early | pin $10-50k | 1-0 | 100.0 | 61.8 | 95.2 | -2.0 |
| follow_move+rlm | early | pin $10-50k | 2-3 | 40.0 | -2.9 | -23.3 | 0.2 |
| follow_move+rlm_quiet | early | pin $10-50k | 3-3 | 50.0 | 3.9 | -5.6 | 0.17 |
| rlm+rlm_quiet | early | pin $10-50k | 2-3 | 40.0 | -2.9 | -23.3 | 0.2 |
| book_lag+money_level | early | pin $10-50k | 1-1 | 50.0 | -11.8 | -6.5 | 0.0 |
| book_lag+money_moving | early | pin $10-50k | 1-1 | 50.0 | 7.3 | 4.0 | -0.05 |
| book_lag+sharp_gap | early | pin $10-50k | 2-1 | 66.7 | 17.6 | 31.7 | 0.63 |
| money_moving+rlm_quiet | early | pin $10-50k | 1-0 | 100.0 | 38.2 | 83.3 | 0.0 |
| pin_value+rlm_quiet | early | pin $10-50k | 1-0 | 100.0 | 38.2 | 83.3 | 0.0 |
| consensus_gap+money_level | early | pin $10-50k | 4-1 | 80.0 | 18.2 | 48.1 | 0.3 |
| consensus_gap+pin_value | early | pin $10-50k | 2-2 | 50.0 | -11.8 | -7.4 | 0.0 |
| book_lag+pin_rlm | early | pin $10-50k | 1-0 | 100.0 | 76.4 | 108.0 | 1.9 |
| book_lag+pre_move | early | pin $10-50k | 1-0 | 100.0 | 76.4 | 108.0 | 1.9 |
| consensus_gap+money_moving | early | pin $10-50k | 1-0 | 100.0 | 76.4 | 108.0 | 1.9 |
| consensus_gap+pin_rlm | early | pin $10-50k | 1-1 | 50.0 | 26.4 | 4.0 | -1.4 |
| money_moving+pin_rlm | early | pin $10-50k | 1-0 | 100.0 | 76.4 | 108.0 | 1.9 |
| money_moving+pre_move | early | pin $10-50k | 1-0 | 100.0 | 76.4 | 108.0 | 1.9 |
| pin_rlm+pre_move | early | pin $10-50k | 1-1 | 50.0 | 26.4 | 4.0 | -1.4 |
| pin_rlm+sharp_gap | early | pin $10-50k | 1-1 | 50.0 | 26.4 | 4.0 | -1.4 |
| follow_move+rlm_ratio | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm+rlm_ratio | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm+sharp_gap | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm_quiet+rlm_ratio | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm_quiet+sharp_gap | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| follow_move+pin_move | early | pin $10-50k | 1-1 | 50.0 | -11.8 | -4.5 | 0.5 |
| pin_move+pin_value | early | pin $10-50k | 2-0 | 100.0 | 38.2 | 88.9 | 1.5 |
| pin_move+sharp_gap | early | pin $10-50k | 2-0 | 100.0 | 38.2 | 88.9 | 1.5 |
| consensus_gap+follow_move | early | pin $10-50k | 1-0 | 100.0 | 38.2 | 83.3 | 0.0 |
| book_lag+pin_move | early | pin $10-50k | 1-0 | 100.0 | 38.2 | 87.0 | 2.0 |
| book_lag+pin_value | early | pin $10-50k | 1-0 | 100.0 | 38.2 | 87.0 | 2.0 |
| follow_move+rlm | early | pin $50k+ | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| follow_move+rlm_quiet | early | pin $50k+ | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | pin $50k+ | 2-1 | 66.7 | 20.6 | 21.8 | 0.0 |
| rlm+rlm_quiet | early | pin $50k+ | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| rlm+rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| rlm+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| rlm_quiet+rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| rlm_quiet+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -38.2 | -100.0 | 0.0 |
| money_level+sharp_gap | early | pin $50k+ | 2-2 | 50.0 | -19.1 | -20.9 | 0.0 |
| consensus_gap+pin_value | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 80.0 | 0.0 |
| follow_move+pin_value | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 82.7 | 0.0 |
| pin_value+sharp_gap | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 82.7 | 0.0 |
| consensus_gap+follow_move | early | pin $50k+ | 1-0 | 100.0 | 38.2 | 82.0 | 0.0 |
| consensus_gap+money_level | early | pin $50k+ | 1-0 | 100.0 | 38.2 | 82.0 | 0.0 |
| consensus_gap+sharp_gap | early | pin $50k+ | 1-2 | 33.3 | -15.8 | -39.3 | 0.87 |
| follow_move+money_level | early | pin $50k+ | 1-0 | 100.0 | 38.2 | 82.0 | 0.0 |
| money_level+pin_value | early | pin $50k+ | 1-0 | 100.0 | 38.2 | 82.0 | 0.0 |
| consensus_gap+pre_move | early | pin $50k+ | 0-1 | 0.0 | -23.6 | -100.0 | 2.1 |
| pre_move+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -23.6 | -100.0 | 2.1 |
| money_level+pin_value | early | pin limit <$10k | 6-4 | 60.0 | 8.0 | 12.8 | 0.2 |
| money_level+sharp_gap | early | pin limit <$10k | 33-12 | 73.3 | 16.5 | 32.0 | -0.26 |
| pin_value+sharp_gap | early | pin limit <$10k | 9-10 | 47.4 | 5.8 | -11.1 | 0.81 |
| consensus_gap+follow_move | early | pin limit <$10k | 0-2 | 0.0 | -42.7 | -100.0 | 0.75 |
| consensus_gap+rlm | early | pin limit <$10k | 0-1 | 0.0 | -23.6 | -100.0 | 0.5 |
| consensus_gap+rlm_quiet | early | pin limit <$10k | 0-1 | 0.0 | -23.6 | -100.0 | 0.5 |
| follow_move+rlm | early | pin limit <$10k | 0-3 | 0.0 | -49.1 | -100.0 | -0.17 |
| follow_move+rlm_quiet | early | pin limit <$10k | 0-3 | 0.0 | -49.1 | -100.0 | -0.17 |
| rlm+rlm_quiet | early | pin limit <$10k | 0-3 | 0.0 | -49.1 | -100.0 | -0.17 |
| pin_move+pin_value | early | pin limit <$10k | 2-5 | 28.6 | -27.3 | -46.6 | 0.57 |
| consensus_gap+pin_move | early | pin limit <$10k | 1-3 | 25.0 | -17.7 | -53.2 | 0.15 |
| consensus_gap+sharp_gap | early | pin limit <$10k | 8-20 | 28.6 | -2.1 | -39.8 | -0.11 |
| money_level+money_moving | early | pin limit <$10k | 8-2 | 80.0 | 18.9 | 36.3 | -0.21 |
| pin_move+sharp_gap | early | pin limit <$10k | 10-5 | 66.7 | 8.2 | 21.3 | 0.57 |
| follow_move+money_level | early | pin limit <$10k | 5-4 | 55.6 | -6.9 | 4.6 | -0.57 |
| follow_move+money_moving | early | pin limit <$10k | 1-1 | 50.0 | -19.1 | -21.9 | -1.55 |
| consensus_gap+money_level | early | pin limit <$10k | 5-2 | 71.4 | 19.7 | 23.4 | -1.06 |
| money_level+pre_move | early | pin limit <$10k | 2-2 | 50.0 | 9.5 | -5.5 | -2.4 |
| pre_move+sharp_gap | early | pin limit <$10k | 9-19 | 32.1 | 0.2 | -30.0 | -0.2 |
| consensus_gap+pin_value | early | pin limit <$10k | 2-10 | 16.7 | -15.8 | -68.8 | 1.21 |
| money_moving+sharp_gap | early | pin limit <$10k | 4-2 | 66.7 | 16.7 | 19.0 | 0.4 |
| consensus_gap+pin_rlm | early | pin limit <$10k | 0-5 | 0.0 | -23.6 | -100.0 | -1.18 |
| consensus_gap+pre_move | early | pin limit <$10k | 3-15 | 16.7 | -7.0 | -54.3 | -0.42 |
| money_level+pin_rlm | early | pin limit <$10k | 0-1 | 0.0 | -23.6 | -100.0 | -10.6 |
| pin_rlm+pre_move | early | pin limit <$10k | 1-5 | 16.7 | -10.9 | -67.5 | -0.82 |
| pin_rlm+sharp_gap | early | pin limit <$10k | 1-5 | 16.7 | -10.9 | -67.5 | -0.82 |
| money_moving+pin_value | early | pin limit <$10k | 2-1 | 66.7 | 30.3 | 26.5 | 2.0 |
| pin_value+pre_move | early | pin limit <$10k | 2-6 | 25.0 | -4.5 | -53.2 | 1.55 |
| consensus_gap+money_moving | early | pin limit <$10k | 1-1 | 50.0 | 19.1 | -6.5 | 3.0 |
| money_moving+pre_move | early | pin limit <$10k | 0-1 | 0.0 | -23.6 | -100.0 | 5.0 |
| follow_move+sharp_gap | early | pin limit <$10k | 4-3 | 57.1 | -1.3 | 12.2 | 0.14 |
| pin_rlm+pin_value | early | pin limit <$10k | 0-2 | 0.0 | -23.6 | -100.0 | 0.9 |
| money_level+pin_move | early | pin limit <$10k | 16-5 | 76.2 | 6.7 | 20.6 | 1.01 |
| book_lag+consensus_gap | early | pin limit <$10k | 1-1 | 50.0 | 7.3 | -6.5 | 1.7 |
| follow_move+pin_move | early | pin limit <$10k | 2-4 | 33.3 | -28.5 | -34.9 | -0.5 |
| follow_move+pin_value | early | pin limit <$10k | 0-2 | 0.0 | -61.8 | -100.0 | 0.5 |
| pin_move+rlm | early | pin limit <$10k | 0-2 | 0.0 | -61.8 | -100.0 | -0.5 |
| pin_move+rlm_quiet | early | pin limit <$10k | 0-2 | 0.0 | -61.8 | -100.0 | -0.5 |
| pin_move+pin_rlm | early | pin limit <$10k | 1-1 | 50.0 | 14.5 | -2.4 | 1.0 |
| pin_move+pre_move | early | pin limit <$10k | 1-1 | 50.0 | 14.5 | -2.4 | 1.0 |
| book_lag+money_level | early | pin limit <$10k | 2-0 | 100.0 | 30.9 | 62.7 | -1.75 |
| book_lag+pin_move | early | pin limit <$10k | 2-0 | 100.0 | 30.9 | 62.7 | -1.75 |
| book_lag+pin_value | early | pin limit <$10k | 1-0 | 100.0 | 38.2 | 87.0 | 1.0 |
| book_lag+sharp_gap | early | pin limit <$10k | 1-0 | 100.0 | 38.2 | 87.0 | 1.0 |
