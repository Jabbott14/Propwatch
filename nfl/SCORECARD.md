# NFL scorecard

Generated 2026-11-26 22:26 UTC. 57 graded games (1 finished games had no final score and are not graded).

## Read this first: fit vs forward

**43 games before 2026-11-21 (fit) · 14 on or after it (forward).**

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
this sample ran **63.2% favourites** (n=57)
**52.6% overs** (n=57) and **77.2% moneyline favourites** (n=57) and **50.9% team-total overs** (n=114).

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

Games kicking off on or after 2026-11-21. Nothing in the engine was chosen using these. n=14 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 1-2 | 33.3 | 42.9 | -9.5 | -1.0 | -33.3 | 0.0 | 0.0 | keep collecting (3/30) |
| pin_move | both | 8-6 | 57.1 | 56.1 | 1.0 | -0.73 | -5.2 | 0.06 | 50.0 | keep collecting (14/30) |
| pin_rlm | both | 1-3 | 25.0 | 33.9 | -8.9 | -2.05 | -51.2 | -0.93 | 25.0 | keep collecting (4/30) |
| pre_move | both | 5-12 | 29.4 | 36.1 | -6.7 | -5.97 | -35.1 | -0.55 | 29.4 | keep collecting (17/30) |
| follow_move | both | 5-7 | 41.7 | 48.8 | -7.1 | -2.34 | -19.5 | -0.5 | 8.3 | keep collecting (12/30) |
| rlm | both | 1-2 | 33.3 | 42.9 | -9.5 | -1.0 | -33.3 | 0.0 | 0.0 | keep collecting (3/30) |
| rlm_ratio | both | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level | both | 25-17 | 59.5 | 58.5 | 1.0 | +0.25 | 0.6 | 0.21 | 42.9 | no edge shown yet |
| sharp_gap | both | 17-21 | 44.7 | 45.1 | -0.4 | -4.51 | -11.9 | -0.22 | 39.5 | no edge shown yet |
| pin_value | both | 9-13 | 40.9 | 49.4 | -8.4 | -5.1 | -23.2 | 0.2 | 31.8 | keep collecting (22/30) |
| book_lag | both | 3-0 | 100.0 | 52.4 | 47.6 | +2.6 | 86.5 | -1.63 | 33.3 | keep collecting (3/30) |
| consensus_gap | both | 8-12 | 40.0 | 37.1 | 2.9 | -1.18 | -5.9 | -0.14 | 35.0 | keep collecting (20/30) |
| consensus_gap+money_level | both | 4-2 | 66.7 | 57.1 | 9.5 | +1.37 | 22.8 | 0.58 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | both | 2-5 | 28.6 | 44.9 | -16.3 | -3.3 | -47.1 | 0.47 | 28.6 | keep collecting (7/30) |
| consensus_gap+sharp_gap | both | 5-10 | 33.3 | 36.2 | -2.9 | -4.12 | -27.5 | -0.46 | 33.3 | keep collecting (15/30) |
| follow_move+rlm | both | 1-2 | 33.3 | 42.9 | -9.5 | -1.0 | -33.3 | 0.0 | 0.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | both | 1-2 | 33.3 | 42.9 | -9.5 | -1.0 | -33.3 | 0.0 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+pin_value | both | 4-3 | 57.1 | 56.1 | 1.0 | +0.48 | 6.9 | 0.57 | 42.9 | keep collecting (7/30) |
| money_level+sharp_gap | both | 9-6 | 60.0 | 54.8 | 5.2 | +1.75 | 11.6 | 0.08 | 60.0 | keep collecting (15/30) |
| pin_value+sharp_gap | both | 3-6 | 33.3 | 45.2 | -11.9 | -3.43 | -38.1 | 0.7 | 55.6 | keep collecting (9/30) |
| rlm+rlm_quiet | both | 1-2 | 33.3 | 42.9 | -9.5 | -1.0 | -33.3 | 0.0 | 0.0 | redundant -- identical record to rlm alone, not independent confirmation |
| money_level+pin_move | both | 7-4 | 63.6 | 59.7 | 3.9 | +0.32 | 2.9 | 0.07 | 54.5 | keep collecting (11/30) |
| pre_move+sharp_gap | both | 5-12 | 29.4 | 36.1 | -6.7 | -5.97 | -35.1 | -0.55 | 29.4 | redundant -- identical record to pre_move alone, not independent confirmation |
| consensus_gap+pre_move | both | 2-9 | 18.2 | 28.6 | -10.4 | -5.66 | -51.5 | -0.95 | 18.2 | keep collecting (11/30) |
| pin_value+pre_move | both | 1-3 | 25.0 | 33.9 | -8.9 | -2.17 | -54.2 | 0.82 | 50.0 | keep collecting (4/30) |
| follow_move+money_level | both | 3-3 | 50.0 | 52.4 | -2.4 | -0.22 | -3.6 | -0.42 | 16.7 | keep collecting (6/30) |
| follow_move+pin_move | both | 1-3 | 25.0 | 53.6 | -28.6 | -2.05 | -51.2 | -0.5 | 25.0 | keep collecting (4/30) |
| follow_move+sharp_gap | both | 2-2 | 50.0 | 50.0 | 0.0 | -0.05 | -1.2 | -0.62 | 25.0 | keep collecting (4/30) |
| pin_move+sharp_gap | both | 4-3 | 57.1 | 53.1 | 4.1 | +0.61 | 8.7 | 0.37 | 71.4 | keep collecting (7/30) |
| book_lag+money_level | both | 2-0 | 100.0 | 64.3 | 35.7 | +1.25 | 62.7 | -1.25 | 50.0 | keep collecting (2/30) |
| book_lag+pin_move | both | 2-0 | 100.0 | 64.3 | 35.7 | +1.25 | 62.7 | -1.25 | 50.0 | keep collecting (2/30) |
| consensus_gap+follow_move | both | 1-1 | 50.0 | 57.1 | -7.1 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_value | both | 1-1 | 50.0 | 57.1 | -7.1 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+rlm_ratio | both | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+rlm_ratio | both | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| rlm_quiet+rlm_ratio | both | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| rlm_ratio+sharp_gap | both | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_move+pin_rlm | both | 1-1 | 50.0 | 39.3 | 10.7 | -0.05 | -2.4 | 0.5 | 50.0 | keep collecting (2/30) |
| pin_move+pre_move | both | 1-1 | 50.0 | 39.3 | 10.7 | -0.05 | -2.4 | 0.5 | 50.0 | keep collecting (2/30) |
| pin_rlm+pre_move | both | 1-3 | 25.0 | 33.9 | -8.9 | -2.05 | -51.2 | -0.93 | 25.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 1-3 | 25.0 | 33.9 | -8.9 | -2.05 | -51.2 | -0.93 | 25.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_rlm | both | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 | -1.57 | 0.0 | keep collecting (3/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| book_lag+consensus_gap | both | 1-0 | 100.0 | 28.6 | 71.4 | +1.34 | 134.0 | -2.4 | 0.0 | keep collecting (1/30) |
| book_lag+pre_move | both | 1-0 | 100.0 | 28.6 | 71.4 | +1.34 | 134.0 | -2.4 | 0.0 | keep collecting (1/30) |
| book_lag+sharp_gap | both | 2-0 | 100.0 | 42.9 | 57.1 | +2.21 | 110.5 | -0.2 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 1-0 | 100.0 | 57.1 | 42.9 | +0.87 | 87.0 | 2.0 | 100.0 | keep collecting (1/30) |
| pin_move+pin_value | both | 1-2 | 33.3 | 54.8 | -21.4 | -1.13 | -37.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+pin_move | both | 0-2 | 0.0 | 42.9 | -42.9 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| rlm_quiet | spread | 1-2 | 33.3 | 42.9 | -9.5 | -1.0 | -33.3 | 0.0 | 0.0 | keep collecting (3/30) |
| pin_move | moneyline | 3-2 | 60.0 | 62.9 | -2.9 | -1.28 | -25.7 | -0.04 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 2-3 | 40.0 | 54.3 | -14.3 | -1.18 | -23.6 | 0.0 | 40.0 | keep collecting (5/30) |
| pin_move | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.74 | 43.4 | 0.25 | 50.0 | keep collecting (4/30) |
| pin_rlm | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 | -1.57 | 0.0 | keep collecting (3/30) |
| pin_rlm | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 | 1.0 | 100.0 | keep collecting (1/30) |
| pre_move | moneyline | 2-9 | 18.2 | 28.6 | -10.4 | -5.66 | -51.5 | -0.95 | 18.2 | keep collecting (11/30) |
| pre_move | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.31 | -5.1 | 0.17 | 50.0 | keep collecting (6/30) |
| follow_move | spread | 5-7 | 41.7 | 48.8 | -7.1 | -2.34 | -19.5 | -0.5 | 8.3 | keep collecting (12/30) |
| rlm | spread | 1-2 | 33.3 | 42.9 | -9.5 | -1.0 | -33.3 | 0.0 | 0.0 | keep collecting (3/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level | moneyline | 10-4 | 71.4 | 71.4 | 0.0 | -0.18 | -1.3 | 0.35 | 50.0 | keep collecting (14/30) |
| money_level | spread | 8-6 | 57.1 | 54.1 | 3.1 | +1.1 | 7.9 | 0.14 | 35.7 | keep collecting (14/30) |
| money_level | total | 7-7 | 50.0 | 50.0 | 0.0 | -0.67 | -4.8 | 0.14 | 42.9 | keep collecting (14/30) |
| sharp_gap | moneyline | 3-10 | 23.1 | 35.2 | -12.1 | -5.97 | -46.0 | -1.09 | 23.1 | keep collecting (13/30) |
| sharp_gap | spread | 9-4 | 69.2 | 50.5 | 18.7 | +4.07 | 31.3 | 0.31 | 46.2 | keep collecting (13/30) |
| sharp_gap | total | 5-7 | 41.7 | 50.0 | -8.3 | -2.6 | -21.7 | 0.17 | 50.0 | keep collecting (12/30) |
| pin_value | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 | 0.77 | 33.3 | keep collecting (3/30) |
| pin_value | spread | 4-2 | 66.7 | 57.1 | 9.5 | +1.48 | 24.7 | 0.5 | 33.3 | keep collecting (6/30) |
| pin_value | total | 1-3 | 25.0 | 50.0 | -25.0 | -2.17 | -54.2 | 0.0 | 50.0 | keep collecting (4/30) |
| pin_value | tt_away | 1-2 | 33.3 | 52.4 | -19.0 | -1.2 | -40.0 | -0.33 | 0.0 | keep collecting (3/30) |
| pin_value | tt_home | 3-3 | 50.0 | 50.0 | 0.0 | -0.22 | -3.6 | 0.0 | 33.3 | keep collecting (6/30) |
| book_lag | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.73 | 86.2 | -3.45 | 0.0 | keep collecting (2/30) |
| book_lag | spread | 1-0 | 100.0 | 57.1 | 42.9 | +0.87 | 87.0 | 2.0 | 100.0 | keep collecting (1/30) |
| consensus_gap | moneyline | 4-10 | 28.6 | 28.6 | 0.0 | -2.55 | -18.2 | -0.46 | 28.6 | keep collecting (14/30) |
| consensus_gap | spread | 4-2 | 66.7 | 57.1 | 9.5 | +1.37 | 22.8 | 0.58 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 | 0.77 | 33.3 | redundant -- identical record to pin_value alone, not independent confirmation |
| consensus_gap+pre_move | moneyline | 2-9 | 18.2 | 28.6 | -10.4 | -5.66 | -51.5 | -0.95 | 18.2 | redundant -- identical record to pre_move alone, not independent confirmation |
| consensus_gap+sharp_gap | moneyline | 2-9 | 18.2 | 28.6 | -10.4 | -5.66 | -51.5 | -0.95 | 18.2 | keep collecting (11/30) |
| pin_value+pre_move | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 | 0.77 | 33.3 | redundant -- identical record to pin_value alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 | 0.77 | 33.3 | redundant -- identical record to pin_value alone, not independent confirmation |
| pre_move+sharp_gap | moneyline | 2-9 | 18.2 | 28.6 | -10.4 | -5.66 | -51.5 | -0.95 | 18.2 | redundant -- identical record to pre_move alone, not independent confirmation |
| book_lag+money_level | moneyline | 1-0 | 100.0 | 71.4 | 28.6 | +0.39 | 38.5 | -4.5 | 0.0 | keep collecting (1/30) |
| book_lag+pin_move | moneyline | 1-0 | 100.0 | 71.4 | 28.6 | +0.39 | 38.5 | -4.5 | 0.0 | keep collecting (1/30) |
| money_level+pin_move | moneyline | 3-1 | 75.0 | 71.4 | 3.6 | -0.28 | -7.1 | -0.05 | 75.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 | -1.57 | 0.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_rlm+pre_move | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 | -1.57 | 0.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 | -1.57 | 0.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | moneyline | 1-0 | 100.0 | 28.6 | 71.4 | +1.34 | 134.0 | -2.4 | 0.0 | keep collecting (1/30) |
| book_lag+pre_move | moneyline | 1-0 | 100.0 | 28.6 | 71.4 | +1.34 | 134.0 | -2.4 | 0.0 | keep collecting (1/30) |
| book_lag+sharp_gap | moneyline | 1-0 | 100.0 | 28.6 | 71.4 | +1.34 | 134.0 | -2.4 | 0.0 | keep collecting (1/30) |
| money_level+sharp_gap | moneyline | 1-1 | 50.0 | 71.4 | -21.4 | -0.31 | -15.7 | -1.9 | 50.0 | keep collecting (2/30) |
| pin_move+sharp_gap | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.3 | 50.0 | keep collecting (2/30) |
| consensus_gap+pin_move | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pre_move | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 4-2 | 66.7 | 57.1 | 9.5 | +1.37 | 22.8 | 0.58 | 50.0 | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+pin_value | spread | 2-2 | 50.0 | 57.1 | -7.1 | -0.3 | -7.4 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+sharp_gap | spread | 3-1 | 75.0 | 57.1 | 17.9 | +1.54 | 38.4 | 0.88 | 75.0 | keep collecting (4/30) |
| follow_move+rlm | spread | 1-2 | 33.3 | 42.9 | -9.5 | -1.0 | -33.3 | 0.0 | 0.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 1-2 | 33.3 | 42.9 | -9.5 | -1.0 | -33.3 | 0.0 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+pin_value | spread | 4-2 | 66.7 | 57.1 | 9.5 | +1.48 | 24.7 | 0.5 | 33.3 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_level+sharp_gap | spread | 6-2 | 75.0 | 53.6 | 21.4 | +3.36 | 42.0 | 0.38 | 62.5 | keep collecting (8/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 57.1 | 9.5 | +0.74 | 24.7 | 1.0 | 66.7 | keep collecting (3/30) |
| rlm+rlm_quiet | spread | 1-2 | 33.3 | 42.9 | -9.5 | -1.0 | -33.3 | 0.0 | 0.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+money_level | spread | 3-3 | 50.0 | 52.4 | -2.4 | -0.22 | -3.6 | -0.42 | 16.7 | keep collecting (6/30) |
| follow_move+pin_move | spread | 1-3 | 25.0 | 53.6 | -28.6 | -2.05 | -51.2 | -0.5 | 25.0 | keep collecting (4/30) |
| follow_move+sharp_gap | spread | 2-2 | 50.0 | 50.0 | 0.0 | -0.05 | -1.2 | -0.62 | 25.0 | keep collecting (4/30) |
| money_level+pin_move | spread | 2-3 | 40.0 | 54.3 | -14.3 | -1.18 | -23.6 | 0.0 | 40.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| pin_move+sharp_gap | spread | 2-1 | 66.7 | 57.1 | 9.5 | +0.82 | 27.4 | 0.0 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 1-1 | 50.0 | 57.1 | -7.1 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_value | spread | 1-1 | 50.0 | 57.1 | -7.1 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+rlm_ratio | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| rlm_quiet+rlm_ratio | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| book_lag+money_level | spread | 1-0 | 100.0 | 57.1 | 42.9 | +0.87 | 87.0 | 2.0 | 100.0 | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | spread | 1-0 | 100.0 | 57.1 | 42.9 | +0.87 | 87.0 | 2.0 | 100.0 | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_value | spread | 1-0 | 100.0 | 57.1 | 42.9 | +0.87 | 87.0 | 2.0 | 100.0 | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | spread | 1-0 | 100.0 | 57.1 | 42.9 | +0.87 | 87.0 | 2.0 | 100.0 | redundant -- identical record to book_lag alone, not independent confirmation |
| pin_move+pin_value | spread | 1-1 | 50.0 | 57.1 | -7.1 | -0.13 | -6.5 | 1.5 | 100.0 | keep collecting (2/30) |
| consensus_gap+pin_move | spread | 0-1 | 0.0 | 57.1 | -57.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_move | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 89.2 | 0.5 | 50.0 | keep collecting (2/30) |
| pre_move+sharp_gap | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.31 | -5.1 | 0.17 | 50.0 | redundant -- identical record to pre_move alone, not independent confirmation |
| money_level+sharp_gap | total | 2-3 | 40.0 | 50.0 | -10.0 | -1.3 | -25.9 | 0.4 | 60.0 | keep collecting (5/30) |
| pin_value+pre_move | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.83 | 83.3 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | total | 1-2 | 33.3 | 50.0 | -16.7 | -1.17 | -38.9 | 0.33 | 66.7 | keep collecting (3/30) |
| pin_move+pin_rlm | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 | 1.0 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pre_move | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 89.2 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_rlm+pre_move | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 | 1.0 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 | 1.0 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | total | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 9-5 | 64.3 | 43.9 | 20.4 | +4.27 | 30.5 |  |  | keep collecting (14/30) |
| pin_move | both | 19-15 | 55.9 | 49.2 | 6.7 | +1.16 | 3.4 |  |  | no edge shown yet |
| money_delta | both | 4-5 | 44.4 | 42.1 | 2.4 | +0.27 | 3.0 |  |  | keep collecting (9/30) |
| pin_rlm | both | 0-4 | 0.0 | 32.1 | -32.1 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| pre_move | both | 1-3 | 25.0 | 32.1 | -7.1 | -2.04 | -51.0 |  |  | keep collecting (4/30) |
| follow_move | both | 30-19 | 61.2 | 51.3 | 9.9 | +6.95 | 14.2 |  |  | no edge shown yet |
| rlm | both | 9-5 | 64.3 | 43.9 | 20.4 | +4.27 | 30.5 |  |  | keep collecting (14/30) |
| rlm_ratio | both | 0-2 | 0.0 | 35.7 | -35.7 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level | both | 19-22 | 46.3 | 57.1 | -10.8 | -10.06 | -24.5 |  |  | no edge shown yet |
| sharp_gap | both | 16-25 | 39.0 | 46.5 | -7.5 | -8.62 | -21.0 |  |  | DROP: below break-even |
| money_moving | both | 19-21 | 47.5 | 51.2 | -3.7 | -3.99 | -10.0 |  |  | no edge shown yet |
| pin_value | both | 12-21 | 36.4 | 46.8 | -10.4 | -8.85 | -26.8 |  |  | DROP: below break-even |
| consensus_gap | both | 4-12 | 25.0 | 32.1 | -7.1 | -3.9 | -24.4 |  |  | keep collecting (16/30) |
| follow_move+money_level | both | 10-10 | 50.0 | 57.1 | -7.1 | -3.17 | -15.8 |  |  | keep collecting (20/30) |
| follow_move+money_moving | both | 8-7 | 53.3 | 53.8 | -0.5 | -0.31 | -2.0 |  |  | keep collecting (15/30) |
| money_level+money_moving | both | 11-13 | 45.8 | 56.8 | -11.0 | -4.98 | -20.7 |  |  | keep collecting (24/30) |
| pin_value+sharp_gap | both | 3-7 | 30.0 | 42.9 | -12.9 | -4.31 | -43.1 |  |  | keep collecting (10/30) |
| money_moving+pin_move | both | 7-6 | 53.8 | 48.9 | 4.9 | -0.04 | -0.3 |  |  | keep collecting (13/30) |
| money_moving+sharp_gap | both | 10-14 | 41.7 | 48.5 | -6.8 | -3.78 | -15.8 |  |  | keep collecting (24/30) |
| pin_move+sharp_gap | both | 8-10 | 44.4 | 45.2 | -0.8 | -2.72 | -15.1 |  |  | keep collecting (18/30) |
| consensus_gap+follow_move | both | 1-3 | 25.0 | 28.6 | -3.6 | -1.28 | -32.0 |  |  | keep collecting (4/30) |
| consensus_gap+rlm | both | 1-2 | 33.3 | 28.6 | 4.8 | -0.28 | -9.3 |  |  | keep collecting (3/30) |
| consensus_gap+rlm_quiet | both | 1-2 | 33.3 | 28.6 | 4.8 | -0.28 | -9.3 |  |  | keep collecting (3/30) |
| consensus_gap+rlm_ratio | both | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+sharp_gap | both | 2-10 | 16.7 | 31.0 | -14.3 | -6.07 | -50.6 |  |  | keep collecting (12/30) |
| follow_move+rlm | both | 9-5 | 64.3 | 43.9 | 20.4 | +4.27 | 30.5 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | both | 9-5 | 64.3 | 43.9 | 20.4 | +4.27 | 30.5 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 0-2 | 0.0 | 35.7 | -35.7 | -2.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 7-9 | 43.8 | 50.0 | -6.2 | -2.59 | -16.2 |  |  | keep collecting (16/30) |
| rlm+rlm_quiet | both | 9-5 | 64.3 | 43.9 | 20.4 | +4.27 | 30.5 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+rlm_ratio | both | 0-2 | 0.0 | 35.7 | -35.7 | -2.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 3-3 | 50.0 | 45.2 | 4.8 | -0.19 | -3.1 |  |  | keep collecting (6/30) |
| rlm_quiet+rlm_ratio | both | 0-2 | 0.0 | 35.7 | -35.7 | -2.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 3-3 | 50.0 | 45.2 | 4.8 | -0.19 | -3.1 |  |  | keep collecting (6/30) |
| rlm_ratio+sharp_gap | both | 0-2 | 0.0 | 35.7 | -35.7 | -2.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_move | both | 17-10 | 63.0 | 51.9 | 11.1 | +4.38 | 16.2 |  |  | keep collecting (27/30) |
| follow_move+pin_rlm | both | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_rlm | both | 0-2 | 0.0 | 35.7 | -35.7 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_moving+rlm | both | 2-1 | 66.7 | 45.2 | 21.4 | +0.86 | 28.7 |  |  | keep collecting (3/30) |
| money_moving+rlm_quiet | both | 2-1 | 66.7 | 45.2 | 21.4 | +0.86 | 28.7 |  |  | keep collecting (3/30) |
| money_moving+rlm_ratio | both | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_move+pin_rlm | both | 0-4 | 0.0 | 32.1 | -32.1 | -4.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm | both | 8-3 | 72.7 | 45.5 | 27.3 | +5.23 | 47.6 |  |  | keep collecting (11/30) |
| pin_move+rlm_quiet | both | 8-3 | 72.7 | 45.5 | 27.3 | +5.23 | 47.6 |  |  | keep collecting (11/30) |
| pin_move+rlm_ratio | both | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+rlm | both | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+sharp_gap | both | 0-4 | 0.0 | 32.1 | -32.1 | -4.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_move | both | 9-8 | 52.9 | 55.0 | -2.1 | -1.89 | -11.1 |  |  | keep collecting (17/30) |
| money_level+sharp_gap | both | 6-12 | 33.3 | 54.0 | -20.6 | -7.1 | -39.4 |  |  | keep collecting (18/30) |
| consensus_gap+pin_move | both | 1-5 | 16.7 | 28.6 | -11.9 | -3.28 | -54.7 |  |  | keep collecting (6/30) |
| pin_move+pin_value | both | 4-6 | 40.0 | 42.1 | -2.1 | -2.52 | -25.2 |  |  | keep collecting (10/30) |
| follow_move+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 1-3 | 25.0 | 39.3 | -14.3 | -2.09 | -52.3 |  |  | keep collecting (4/30) |
| money_delta+rlm | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_delta+rlm_quiet | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_delta+sharp_gap | both | 3-5 | 37.5 | 42.0 | -4.5 | -0.64 | -8.0 |  |  | keep collecting (8/30) |
| consensus_gap+money_delta | both | 1-2 | 33.3 | 28.6 | 4.8 | +0.45 | 15.0 |  |  | keep collecting (3/30) |
| consensus_gap+money_moving | both | 1-6 | 14.3 | 36.7 | -22.4 | -3.55 | -50.7 |  |  | keep collecting (7/30) |
| consensus_gap+pin_rlm | both | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| consensus_gap+pin_value | both | 1-5 | 16.7 | 33.3 | -16.7 | -2.55 | -42.5 |  |  | keep collecting (6/30) |
| consensus_gap+pre_move | both | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_delta+money_moving | both | 3-2 | 60.0 | 41.4 | 18.6 | +2.36 | 47.2 |  |  | keep collecting (5/30) |
| money_delta+pin_rlm | both | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_delta+pin_value | both | 0-2 | 0.0 | 39.3 | -39.3 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_delta+pre_move | both | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_moving+pin_value | both | 2-5 | 28.6 | 41.8 | -13.3 | -3.26 | -46.6 |  |  | keep collecting (7/30) |
| money_moving+pre_move | both | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_move+pre_move | both | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm+pre_move | both | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_value+pre_move | both | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pre_move+sharp_gap | both | 1-3 | 25.0 | 32.1 | -7.1 | -2.04 | -51.0 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| money_level+pin_value | both | 4-5 | 44.4 | 47.6 | -3.2 | -1.53 | -17.0 |  |  | keep collecting (9/30) |
| consensus_gap+money_level | both | 0-3 | 0.0 | 47.6 | -47.6 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| follow_move+pin_value | both | 3-2 | 60.0 | 45.7 | 14.3 | +0.61 | 12.2 |  |  | keep collecting (5/30) |
| pin_value+rlm | both | 1-0 | 100.0 | 50.0 | 50.0 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_value+rlm_quiet | both | 1-0 | 100.0 | 50.0 | 50.0 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 1-2 | 33.3 | 28.6 | 4.8 | -0.28 | -9.3 |  |  | keep collecting (3/30) |
| rlm_quiet | spread | 3-2 | 60.0 | 45.7 | 14.3 | +0.94 | 18.9 |  |  | keep collecting (5/30) |
| rlm_quiet | total | 5-1 | 83.3 | 50.0 | 33.3 | +3.61 | 60.1 |  |  | keep collecting (6/30) |
| pin_move | moneyline | 4-7 | 36.4 | 48.1 | -11.7 | -4.5 | -40.9 |  |  | keep collecting (11/30) |
| pin_move | spread | 3-6 | 33.3 | 49.2 | -15.9 | -3.19 | -35.4 |  |  | keep collecting (9/30) |
| pin_move | total | 12-2 | 85.7 | 50.0 | 35.7 | +8.85 | 63.2 |  |  | keep collecting (14/30) |
| money_delta | moneyline | 1-2 | 33.3 | 28.6 | 4.8 | +0.45 | 15.0 |  |  | keep collecting (3/30) |
| money_delta | spread | 1-0 | 100.0 | 42.9 | 57.1 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta | total | 2-3 | 40.0 | 50.0 | -10.0 | -1.09 | -21.8 |  |  | keep collecting (5/30) |
| pin_rlm | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_rlm | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pre_move | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pre_move | spread | 1-0 | 100.0 | 42.9 | 57.1 | +0.96 | 96.2 |  |  | keep collecting (1/30) |
| follow_move | moneyline | 5-6 | 45.5 | 55.8 | -10.4 | -2.82 | -25.7 |  |  | keep collecting (11/30) |
| follow_move | spread | 6-7 | 46.2 | 50.5 | -4.4 | -1.31 | -10.1 |  |  | keep collecting (13/30) |
| follow_move | total | 10-2 | 83.3 | 50.0 | 33.3 | +7.07 | 58.9 |  |  | keep collecting (12/30) |
| follow_move | tt_away | 5-1 | 83.3 | 47.6 | 35.7 | +3.44 | 57.3 |  |  | keep collecting (6/30) |
| follow_move | tt_home | 4-3 | 57.1 | 51.0 | 6.1 | +0.57 | 8.2 |  |  | keep collecting (7/30) |
| rlm | moneyline | 1-2 | 33.3 | 28.6 | 4.8 | -0.28 | -9.3 |  |  | keep collecting (3/30) |
| rlm | spread | 3-2 | 60.0 | 45.7 | 14.3 | +0.94 | 18.9 |  |  | keep collecting (5/30) |
| rlm | total | 5-1 | 83.3 | 50.0 | 33.3 | +3.61 | 60.1 |  |  | keep collecting (6/30) |
| rlm_ratio | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level | moneyline | 9-5 | 64.3 | 68.4 | -4.1 | -1.97 | -14.1 |  |  | keep collecting (14/30) |
| money_level | spread | 3-10 | 23.1 | 52.7 | -29.7 | -7.35 | -56.5 |  |  | keep collecting (13/30) |
| money_level | total | 7-7 | 50.0 | 50.0 | 0.0 | -0.74 | -5.3 |  |  | keep collecting (14/30) |
| sharp_gap | moneyline | 3-11 | 21.4 | 37.8 | -16.3 | -6.59 | -47.1 |  |  | keep collecting (14/30) |
| sharp_gap | spread | 7-7 | 50.0 | 52.0 | -2.0 | -0.49 | -3.5 |  |  | keep collecting (14/30) |
| sharp_gap | total | 6-7 | 46.2 | 50.0 | -3.8 | -1.53 | -11.8 |  |  | keep collecting (13/30) |
| money_moving | moneyline | 6-7 | 46.2 | 54.9 | -8.8 | -1.92 | -14.8 |  |  | keep collecting (13/30) |
| money_moving | spread | 6-8 | 42.9 | 49.0 | -6.1 | -2.5 | -17.8 |  |  | keep collecting (14/30) |
| money_moving | total | 7-6 | 53.8 | 50.0 | 3.8 | +0.44 | 3.4 |  |  | keep collecting (13/30) |
| pin_value | moneyline | 1-4 | 20.0 | 28.6 | -8.6 | -1.55 | -31.0 |  |  | keep collecting (5/30) |
| pin_value | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.18 | -36.3 |  |  | keep collecting (6/30) |
| pin_value | total | 4-2 | 66.7 | 50.0 | 16.7 | +1.48 | 24.7 |  |  | keep collecting (6/30) |
| pin_value | tt_away | 2-7 | 22.2 | 50.8 | -28.6 | -5.15 | -57.2 |  |  | keep collecting (9/30) |
| pin_value | tt_home | 3-4 | 42.9 | 49.0 | -6.1 | -1.45 | -20.8 |  |  | keep collecting (7/30) |
| consensus_gap | moneyline | 4-10 | 28.6 | 28.6 | 0.0 | -1.9 | -13.6 |  |  | keep collecting (14/30) |
| consensus_gap | spread | 0-2 | 0.0 | 57.1 | -57.1 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+follow_move | moneyline | 1-3 | 25.0 | 28.6 | -3.6 | -1.28 | -32.0 |  |  | keep collecting (4/30) |
| consensus_gap+rlm | moneyline | 1-2 | 33.3 | 28.6 | 4.8 | -0.28 | -9.3 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| consensus_gap+rlm_quiet | moneyline | 1-2 | 33.3 | 28.6 | 4.8 | -0.28 | -9.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+sharp_gap | moneyline | 2-9 | 18.2 | 28.6 | -10.4 | -5.07 | -46.1 |  |  | keep collecting (11/30) |
| follow_move+rlm | moneyline | 1-2 | 33.3 | 28.6 | 4.8 | -0.28 | -9.3 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | moneyline | 1-2 | 33.3 | 28.6 | 4.8 | -0.28 | -9.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 0-3 | 0.0 | 42.9 | -42.9 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_level+money_moving | moneyline | 5-4 | 55.6 | 66.7 | -11.1 | -1.37 | -15.3 |  |  | keep collecting (9/30) |
| rlm+rlm_quiet | moneyline | 1-2 | 33.3 | 28.6 | 4.8 | -0.28 | -9.3 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+rlm_ratio | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_quiet+rlm_ratio | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_ratio+sharp_gap | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+pin_move | moneyline | 1-5 | 16.7 | 28.6 | -11.9 | -3.28 | -54.7 |  |  | keep collecting (6/30) |
| follow_move+pin_move | moneyline | 4-4 | 50.0 | 55.4 | -5.4 | -1.5 | -18.7 |  |  | keep collecting (8/30) |
| money_level+sharp_gap | moneyline | 1-3 | 25.0 | 60.7 | -35.7 | -2.52 | -63.1 |  |  | keep collecting (4/30) |
| money_moving+sharp_gap | moneyline | 2-6 | 25.0 | 44.6 | -19.6 | -3.07 | -38.4 |  |  | keep collecting (8/30) |
| pin_move+rlm | moneyline | 1-1 | 50.0 | 28.6 | 21.4 | +0.72 | 36.0 |  |  | keep collecting (2/30) |
| pin_move+rlm_quiet | moneyline | 1-1 | 50.0 | 28.6 | 21.4 | +0.72 | 36.0 |  |  | keep collecting (2/30) |
| consensus_gap+money_delta | moneyline | 1-2 | 33.3 | 28.6 | 4.8 | +0.45 | 15.0 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 1-4 | 20.0 | 28.6 | -8.6 | -1.55 | -31.0 |  |  | keep collecting (5/30) |
| consensus_gap+pin_rlm | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 1-4 | 20.0 | 28.6 | -8.6 | -1.55 | -31.0 |  |  | redundant -- identical record to pin_value alone, not independent confirmation |
| consensus_gap+pre_move | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| money_delta+money_moving | moneyline | 1-1 | 50.0 | 28.6 | 21.4 | +1.45 | 72.5 |  |  | keep collecting (2/30) |
| money_delta+pin_move | moneyline | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_delta+pin_rlm | moneyline | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_delta+pin_value | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta+pre_move | moneyline | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_delta+sharp_gap | moneyline | 1-2 | 33.3 | 28.6 | 4.8 | +0.45 | 15.0 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| money_moving+pin_move | moneyline | 1-3 | 25.0 | 50.0 | -25.0 | -2.5 | -62.5 |  |  | keep collecting (4/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_moving+pre_move | moneyline | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_move+pin_rlm | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_move+pre_move | moneyline | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_move+sharp_gap | moneyline | 0-4 | 0.0 | 28.6 | -28.6 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| pin_rlm+pin_value | moneyline | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm+pre_move | moneyline | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm+sharp_gap | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+pre_move | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-4 | 0.0 | 28.6 | -28.6 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| pre_move+sharp_gap | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+money_level | moneyline | 4-4 | 50.0 | 66.1 | -16.1 | -2.54 | -31.8 |  |  | keep collecting (8/30) |
| follow_move+money_moving | moneyline | 2-3 | 40.0 | 62.9 | -22.9 | -1.82 | -36.5 |  |  | keep collecting (5/30) |
| money_level+pin_move | moneyline | 3-3 | 50.0 | 64.3 | -14.3 | -2.22 | -37.0 |  |  | keep collecting (6/30) |
| consensus_gap+money_level | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| follow_move+pin_value | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| follow_move+money_level | spread | 1-5 | 16.7 | 52.4 | -35.7 | -4.09 | -68.2 |  |  | keep collecting (6/30) |
| follow_move+money_moving | spread | 3-4 | 42.9 | 49.0 | -6.1 | -1.21 | -17.3 |  |  | keep collecting (7/30) |
| money_level+money_moving | spread | 2-6 | 25.0 | 51.8 | -26.8 | -4.22 | -52.8 |  |  | keep collecting (8/30) |
| pin_value+sharp_gap | spread | 2-2 | 50.0 | 53.6 | -3.6 | -0.18 | -4.4 |  |  | keep collecting (4/30) |
| follow_move+pin_move | spread | 3-4 | 42.9 | 51.0 | -8.2 | -1.19 | -17.0 |  |  | keep collecting (7/30) |
| follow_move+pin_rlm | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+rlm | spread | 3-2 | 60.0 | 45.7 | 14.3 | +0.94 | 18.9 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 45.7 | 14.3 | +0.94 | 18.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 4-5 | 44.4 | 52.4 | -7.9 | -1.28 | -14.2 |  |  | keep collecting (9/30) |
| money_moving+pin_move | spread | 1-3 | 25.0 | 46.4 | -21.4 | -2.05 | -51.2 |  |  | keep collecting (4/30) |
| money_moving+pin_rlm | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm | spread | 1-1 | 50.0 | 42.9 | 7.1 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| money_moving+rlm_quiet | spread | 1-1 | 50.0 | 42.9 | 7.1 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+sharp_gap | spread | 3-4 | 42.9 | 51.0 | -8.2 | -1.27 | -18.1 |  |  | keep collecting (7/30) |
| pin_move+pin_rlm | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm | spread | 2-1 | 66.7 | 47.6 | 19.0 | +0.9 | 30.1 |  |  | keep collecting (3/30) |
| pin_move+rlm_quiet | spread | 2-1 | 66.7 | 47.6 | 19.0 | +0.9 | 30.1 |  |  | keep collecting (3/30) |
| pin_move+rlm_ratio | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_move+sharp_gap | spread | 3-5 | 37.5 | 50.0 | -12.5 | -2.19 | -27.3 |  |  | keep collecting (8/30) |
| pin_rlm+rlm | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm+rlm_quiet | spread | 3-2 | 60.0 | 45.7 | 14.3 | +0.94 | 18.9 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+rlm_ratio | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 2-1 | 66.7 | 47.6 | 19.0 | +0.9 | 30.1 |  |  | keep collecting (3/30) |
| rlm_quiet+rlm_ratio | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | spread | 2-1 | 66.7 | 47.6 | 19.0 | +0.9 | 30.1 |  |  | keep collecting (3/30) |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 42.9 | -42.9 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 2-6 | 25.0 | 53.6 | -28.6 | -4.22 | -52.8 |  |  | keep collecting (8/30) |
| pin_move+pin_value | spread | 0-2 | 0.0 | 42.9 | -42.9 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+pin_value | spread | 1-3 | 25.0 | 50.0 | -25.0 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| money_moving+pin_value | spread | 1-2 | 33.3 | 52.4 | -19.0 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| money_level+pin_move | spread | 0-4 | 0.0 | 50.0 | -50.0 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| consensus_gap+money_level | spread | 0-2 | 0.0 | 57.1 | -57.1 | -2.0 | -100.0 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+money_moving | spread | 0-2 | 0.0 | 57.1 | -57.1 | -2.0 | -100.0 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| pre_move+sharp_gap | spread | 1-0 | 100.0 | 42.9 | 57.1 | +0.96 | 96.2 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| consensus_gap+pin_value | spread | 0-1 | 0.0 | 57.1 | -57.1 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+sharp_gap | spread | 0-1 | 0.0 | 57.1 | -57.1 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_move | total | 5-0 | 100.0 | 50.0 | 50.0 | +4.51 | 90.2 |  |  | keep collecting (5/30) |
| money_moving+sharp_gap | total | 5-4 | 55.6 | 50.0 | 5.6 | +0.56 | 6.2 |  |  | keep collecting (9/30) |
| pin_move+sharp_gap | total | 5-1 | 83.3 | 50.0 | 33.3 | +3.47 | 57.8 |  |  | keep collecting (6/30) |
| follow_move+money_level | total | 5-1 | 83.3 | 50.0 | 33.3 | +3.46 | 57.7 |  |  | keep collecting (6/30) |
| follow_move+pin_move | total | 10-2 | 83.3 | 50.0 | 33.3 | +7.07 | 58.9 |  |  | redundant -- identical record to follow_move alone, not independent confirmation |
| follow_move+sharp_gap | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| money_level+pin_move | total | 6-1 | 85.7 | 50.0 | 35.7 | +4.33 | 61.9 |  |  | keep collecting (7/30) |
| money_level+sharp_gap | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.35 | -5.8 |  |  | keep collecting (6/30) |
| follow_move+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| follow_move+rlm | total | 5-1 | 83.3 | 50.0 | 33.3 | +3.61 | 60.1 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | total | 5-1 | 83.3 | 50.0 | 33.3 | +3.61 | 60.1 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_delta+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_delta+rlm | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_delta+rlm_quiet | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_delta+sharp_gap | total | 2-3 | 40.0 | 50.0 | -10.0 | -1.09 | -21.8 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+money_moving | total | 4-3 | 57.1 | 50.0 | 7.1 | +0.62 | 8.8 |  |  | keep collecting (7/30) |
| pin_move+rlm | total | 5-1 | 83.3 | 50.0 | 33.3 | +3.61 | 60.1 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| pin_move+rlm_quiet | total | 5-1 | 83.3 | 50.0 | 33.3 | +3.61 | 60.1 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm+rlm_quiet | total | 5-1 | 83.3 | 50.0 | 33.3 | +3.61 | 60.1 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| rlm_quiet+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_level+pin_value | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.6 | 40.0 |  |  | keep collecting (4/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.87 | 87.0 |  |  | keep collecting (1/30) |
| pin_move+pin_value | total | 4-1 | 80.0 | 50.0 | 30.0 | +2.48 | 49.6 |  |  | keep collecting (5/30) |
| pin_value+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| follow_move+money_moving | total | 3-0 | 100.0 | 50.0 | 50.0 | +2.73 | 91.0 |  |  | keep collecting (3/30) |
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
| rlm_quiet | both | 3-8 | 27.3 | 45.1 | -17.9 | -5.33 | -48.5 | 0.05 | 18.2 | keep collecting (11/30) |
| pin_move | both | 22-21 | 51.2 | 60.0 | -8.8 | -6.29 | -14.6 | 0.72 | 53.5 | no edge shown yet |
| pin_rlm | both | 2-7 | 22.2 | 25.5 | -3.3 | -4.97 | -55.2 | -0.86 | 55.6 | keep collecting (9/30) |
| pre_move | both | 13-28 | 31.7 | 32.4 | -0.7 | -12.57 | -30.6 | -0.39 | 39.0 | DROP: below break-even |
| follow_move | both | 18-20 | 47.4 | 52.5 | -5.1 | -3.9 | -10.3 | -0.2 | 18.4 | no edge shown yet |
| rlm | both | 2-8 | 20.0 | 43.3 | -23.3 | -6.17 | -61.7 | 0.05 | 20.0 | keep collecting (10/30) |
| rlm_ratio | both | 1-2 | 33.3 | 45.6 | -12.3 | -1.17 | -38.9 | 0.0 | 0.0 | keep collecting (3/30) |
| money_level | both | 95-50 | 65.5 | 60.4 | 5.1 | +17.76 | 12.3 | -0.18 | 31.0 | PROMOTE: beats break-even and its own base rate |
| sharp_gap | both | 77-62 | 55.4 | 48.1 | 7.3 | +6.48 | 4.7 | -0.03 | 36.0 | no edge shown yet |
| money_moving | both | 15-9 | 62.5 | 52.1 | 10.4 | +3.38 | 14.1 | -0.03 | 33.3 | keep collecting (24/30) |
| pin_value | both | 43-38 | 53.1 | 48.8 | 4.3 | -0.58 | -0.7 | 0.18 | 30.9 | no edge shown yet |
| book_lag | both | 5-3 | 62.5 | 46.5 | 16.0 | +1.55 | 19.3 | -0.14 | 62.5 | keep collecting (8/30) |
| consensus_gap | both | 25-43 | 36.8 | 33.0 | 3.8 | -13.77 | -20.2 | 0.04 | 47.1 | DROP: below break-even |
| follow_move+rlm | both | 2-8 | 20.0 | 43.3 | -23.3 | -6.17 | -61.7 | 0.05 | 20.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | both | 3-8 | 27.3 | 45.1 | -17.9 | -5.33 | -48.5 | 0.05 | 18.2 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 1-2 | 33.3 | 45.6 | -12.3 | -1.17 | -38.9 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 13-8 | 61.9 | 54.4 | 7.5 | +4.01 | 19.1 | 0.07 | 23.8 | keep collecting (21/30) |
| rlm+rlm_quiet | both | 2-8 | 20.0 | 43.3 | -23.3 | -6.17 | -61.7 | 0.05 | 20.0 | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+rlm_ratio | both | 1-2 | 33.3 | 45.6 | -12.3 | -1.17 | -38.9 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 1-2 | 33.3 | 45.6 | -12.3 | -1.17 | -38.9 | 0.0 | 0.0 | keep collecting (3/30) |
| rlm_quiet+rlm_ratio | both | 1-2 | 33.3 | 45.6 | -12.3 | -1.17 | -38.9 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 1-2 | 33.3 | 45.6 | -12.3 | -1.17 | -38.9 | 0.0 | 0.0 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | both | 1-2 | 33.3 | 45.6 | -12.3 | -1.17 | -38.9 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_value | both | 15-6 | 71.4 | 57.4 | 14.0 | +7.3 | 34.8 | 0.17 | 28.6 | keep collecting (21/30) |
| money_level+sharp_gap | both | 55-26 | 67.9 | 57.3 | 10.6 | +18.13 | 22.4 | -0.16 | 32.1 | PROMOTE: beats break-even and its own base rate |
| pin_value+sharp_gap | both | 17-11 | 60.7 | 47.0 | 13.7 | +4.0 | 14.3 | 0.6 | 42.9 | keep collecting (28/30) |
| consensus_gap+pin_value | both | 6-12 | 33.3 | 40.8 | -7.5 | -6.96 | -38.6 | 0.81 | 50.0 | keep collecting (18/30) |
| money_level+pre_move | both | 2-4 | 33.3 | 40.6 | -7.3 | -2.22 | -37.0 | -1.6 | 16.7 | keep collecting (6/30) |
| pre_move+sharp_gap | both | 13-28 | 31.7 | 32.4 | -0.7 | -12.57 | -30.6 | -0.39 | 39.0 | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+pin_value | both | 6-2 | 75.0 | 59.9 | 15.1 | +3.21 | 40.1 | 0.25 | 25.0 | keep collecting (8/30) |
| consensus_gap+follow_move | both | 2-2 | 50.0 | 53.1 | -3.1 | -0.35 | -8.7 | 0.38 | 50.0 | keep collecting (4/30) |
| consensus_gap+money_level | both | 11-3 | 78.6 | 57.5 | 21.1 | +5.7 | 40.7 | -0.35 | 50.0 | keep collecting (14/30) |
| consensus_gap+sharp_gap | both | 17-25 | 40.5 | 33.4 | 7.1 | -6.2 | -14.8 | 0.05 | 52.4 | DROP: below break-even |
| follow_move+money_level | both | 13-9 | 59.1 | 58.5 | 0.6 | +2.74 | 12.4 | -0.21 | 22.7 | keep collecting (22/30) |
| consensus_gap+pre_move | both | 6-19 | 24.0 | 22.8 | 1.2 | -9.9 | -39.6 | -0.58 | 44.0 | keep collecting (25/30) |
| follow_move+money_moving | both | 3-2 | 60.0 | 60.7 | -0.7 | +0.38 | 7.5 | -0.62 | 0.0 | keep collecting (5/30) |
| money_level+money_moving | both | 10-3 | 76.9 | 59.8 | 17.1 | +4.57 | 35.1 | -0.47 | 30.8 | keep collecting (13/30) |
| money_moving+pin_value | both | 5-2 | 71.4 | 47.6 | 23.8 | +2.56 | 36.6 | 1.0 | 42.9 | keep collecting (7/30) |
| money_moving+sharp_gap | both | 7-3 | 70.0 | 49.6 | 20.4 | +3.15 | 31.5 | 0.03 | 30.0 | keep collecting (10/30) |
| consensus_gap+rlm | both | 0-1 | 0.0 | 22.8 | -22.8 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | both | 0-1 | 0.0 | 22.8 | -22.8 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_value | both | 4-5 | 44.4 | 57.9 | -13.5 | -1.48 | -16.5 | 0.78 | 66.7 | keep collecting (9/30) |
| consensus_gap+pin_move | both | 1-4 | 20.0 | 38.9 | -18.9 | -3.13 | -62.6 | 0.12 | 60.0 | keep collecting (5/30) |
| pin_move+sharp_gap | both | 13-6 | 68.4 | 56.9 | 11.5 | +4.81 | 25.3 | 0.66 | 63.2 | keep collecting (19/30) |
| book_lag+consensus_gap | both | 3-2 | 60.0 | 33.7 | 26.3 | +1.29 | 25.8 | 0.68 | 80.0 | keep collecting (5/30) |
| money_level+pin_move | both | 20-7 | 74.1 | 66.2 | 7.9 | +5.89 | 21.8 | 0.86 | 55.6 | keep collecting (27/30) |
| money_moving+pin_move | both | 1-0 | 100.0 | 36.8 | 63.2 | +0.95 | 95.2 | -2.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+pin_rlm | both | 1-7 | 12.5 | 22.8 | -10.3 | -5.92 | -74.0 | -1.09 | 50.0 | keep collecting (8/30) |
| money_level+pin_rlm | both | 0-1 | 0.0 | 22.8 | -22.8 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+pre_move | both | 2-7 | 22.2 | 25.5 | -3.3 | -4.97 | -55.2 | -0.86 | 55.6 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 2-7 | 22.2 | 25.5 | -3.3 | -4.97 | -55.2 | -0.86 | 55.6 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+money_level | both | 3-1 | 75.0 | 66.7 | 8.3 | +1.12 | 28.1 | -0.88 | 50.0 | keep collecting (4/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 43.0 | 7.0 | +0.08 | 4.0 | -0.05 | 50.0 | keep collecting (2/30) |
| book_lag+sharp_gap | both | 4-1 | 80.0 | 47.0 | 33.0 | +3.16 | 63.2 | 0.1 | 60.0 | keep collecting (5/30) |
| money_moving+rlm_quiet | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | both | 1-0 | 100.0 | 63.2 | 36.8 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_value+pre_move | both | 2-6 | 25.0 | 28.9 | -3.9 | -4.26 | -53.2 | 1.55 | 62.5 | keep collecting (8/30) |
| consensus_gap+money_moving | both | 2-1 | 66.7 | 27.5 | 39.2 | +0.95 | 31.7 | 2.63 | 100.0 | keep collecting (3/30) |
| money_moving+pre_move | both | 2-1 | 66.7 | 31.0 | 35.7 | +1.03 | 34.4 | 1.63 | 66.7 | keep collecting (3/30) |
| pin_rlm+pin_value | both | 0-2 | 0.0 | 22.8 | -22.8 | -2.0 | -100.0 | 0.9 | 50.0 | keep collecting (2/30) |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 22.8 | 77.2 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+pre_move | both | 2-0 | 100.0 | 22.8 | 77.2 | +2.42 | 121.0 | -0.25 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | both | 1-0 | 100.0 | 22.8 | 77.2 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| follow_move+pin_move | both | 3-6 | 33.3 | 60.2 | -26.9 | -3.19 | -35.4 | -0.22 | 22.2 | keep collecting (9/30) |
| money_moving+rlm | both | 0-1 | 0.0 | 36.8 | -36.8 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+rlm | both | 0-2 | 0.0 | 63.2 | -63.2 | -2.0 | -100.0 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_move+rlm_quiet | both | 0-2 | 0.0 | 63.2 | -63.2 | -2.0 | -100.0 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_move+pin_rlm | both | 1-2 | 33.3 | 31.0 | 2.3 | -1.05 | -34.9 | 0.67 | 66.7 | keep collecting (3/30) |
| pin_move+pre_move | both | 1-2 | 33.3 | 31.0 | 2.3 | -1.05 | -34.9 | 0.67 | 66.7 | keep collecting (3/30) |
| book_lag+pin_move | both | 3-0 | 100.0 | 67.8 | 32.2 | +2.12 | 70.8 | -0.5 | 66.7 | keep collecting (3/30) |
| book_lag+pin_value | both | 2-0 | 100.0 | 63.2 | 36.8 | +1.74 | 87.0 | 1.5 | 100.0 | keep collecting (2/30) |
| rlm_quiet | moneyline | 0-1 | 0.0 | 22.8 | -22.8 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| rlm_quiet | spread | 3-7 | 30.0 | 47.4 | -17.4 | -4.33 | -43.3 | 0.0 | 10.0 | keep collecting (10/30) |
| pin_move | moneyline | 10-8 | 55.6 | 68.1 | -12.6 | -4.22 | -23.5 | 1.23 | 61.1 | keep collecting (18/30) |
| pin_move | spread | 6-6 | 50.0 | 58.8 | -8.8 | -0.5 | -4.1 | -0.08 | 33.3 | keep collecting (12/30) |
| pin_move | total | 6-7 | 46.2 | 49.8 | -3.6 | -1.58 | -12.1 | 0.77 | 61.5 | keep collecting (13/30) |
| pin_rlm | moneyline | 1-7 | 12.5 | 22.8 | -10.3 | -5.92 | -74.0 | -1.09 | 50.0 | keep collecting (8/30) |
| pin_rlm | total | 1-0 | 100.0 | 47.4 | 52.6 | +0.95 | 95.2 | 1.0 | 100.0 | keep collecting (1/30) |
| pre_move | moneyline | 6-19 | 24.0 | 22.8 | 1.2 | -9.9 | -39.6 | -0.58 | 44.0 | keep collecting (25/30) |
| pre_move | spread | 1-2 | 33.3 | 45.6 | -12.3 | -1.09 | -36.4 | -0.5 | 33.3 | keep collecting (3/30) |
| pre_move | total | 6-7 | 46.2 | 47.8 | -1.6 | -1.57 | -12.1 | 0.0 | 30.8 | keep collecting (13/30) |
| follow_move | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.44 | -21.9 | -1.3 | 50.0 | keep collecting (2/30) |
| follow_move | spread | 17-18 | 48.6 | 52.6 | -4.1 | -2.46 | -7.0 | -0.06 | 17.1 | no edge shown yet |
| follow_move | total | 0-1 | 0.0 | 52.6 | -52.6 | -1.0 | -100.0 | -3.0 | 0.0 | keep collecting (1/30) |
| rlm | moneyline | 0-1 | 0.0 | 22.8 | -22.8 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| rlm | spread | 2-7 | 22.2 | 45.6 | -23.4 | -5.17 | -57.4 | 0.0 | 11.1 | keep collecting (9/30) |
| rlm_ratio | spread | 1-2 | 33.3 | 45.6 | -12.3 | -1.17 | -38.9 | 0.0 | 0.0 | keep collecting (3/30) |
| money_level | moneyline | 37-11 | 77.1 | 74.9 | 2.2 | +4.01 | 8.4 | -0.38 | 39.6 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 32-16 | 66.7 | 54.9 | 11.7 | +13.24 | 27.6 | -0.03 | 22.9 | PROMOTE: beats break-even and its own base rate |
| money_level | total | 26-23 | 53.1 | 51.5 | 1.6 | +0.51 | 1.0 | -0.12 | 30.6 | no edge shown yet |
| sharp_gap | moneyline | 20-26 | 43.5 | 40.5 | 2.9 | -9.03 | -19.6 | -0.11 | 43.5 | no edge shown yet |
| sharp_gap | spread | 31-17 | 64.6 | 53.3 | 11.3 | +11.12 | 23.2 | 0.14 | 31.2 | PROMOTE: beats break-even and its own base rate |
| sharp_gap | total | 26-19 | 57.8 | 50.2 | 7.6 | +4.39 | 9.8 | -0.11 | 33.3 | no edge shown yet |
| money_moving | moneyline | 5-2 | 71.4 | 53.9 | 17.5 | +1.1 | 15.6 | 0.33 | 57.1 | keep collecting (7/30) |
| money_moving | spread | 5-5 | 50.0 | 52.6 | -2.6 | -0.41 | -4.1 | 0.0 | 30.0 | keep collecting (10/30) |
| money_moving | total | 5-2 | 71.4 | 49.6 | 21.8 | +2.7 | 38.6 | -0.43 | 14.3 | keep collecting (7/30) |
| pin_value | moneyline | 0-9 | 0.0 | 22.8 | -22.8 | -9.0 | -100.0 | 1.38 | 66.7 | keep collecting (9/30) |
| pin_value | spread | 17-6 | 73.9 | 56.3 | 17.6 | +8.9 | 38.7 | 0.2 | 30.4 | keep collecting (23/30) |
| pin_value | total | 7-9 | 43.8 | 50.0 | -6.3 | -2.77 | -17.3 | 0.0 | 25.0 | keep collecting (16/30) |
| pin_value | tt_away | 9-6 | 60.0 | 50.1 | 9.9 | +1.68 | 11.2 | -0.07 | 20.0 | keep collecting (15/30) |
| pin_value | tt_home | 10-8 | 55.6 | 49.9 | 5.7 | +0.61 | 3.4 | -0.06 | 27.8 | keep collecting (18/30) |
| book_lag | moneyline | 3-1 | 75.0 | 36.4 | 38.6 | +1.81 | 45.1 | -0.65 | 50.0 | keep collecting (4/30) |
| book_lag | spread | 2-2 | 50.0 | 56.6 | -6.6 | -0.26 | -6.5 | 0.38 | 75.0 | keep collecting (4/30) |
| consensus_gap | moneyline | 14-35 | 28.6 | 25.0 | 3.5 | -15.15 | -30.9 | -0.09 | 49.0 | DROP: below break-even |
| consensus_gap | spread | 11-8 | 57.9 | 53.5 | 4.4 | +1.38 | 7.3 | 0.39 | 42.1 | keep collecting (19/30) |
| money_level+sharp_gap | moneyline | 13-4 | 76.5 | 70.8 | 5.7 | +2.03 | 11.9 | -0.69 | 35.3 | keep collecting (17/30) |
| consensus_gap+pre_move | moneyline | 6-19 | 24.0 | 22.8 | 1.2 | -9.9 | -39.6 | -0.58 | 44.0 | redundant -- identical record to pre_move alone, not independent confirmation |
| consensus_gap+sharp_gap | moneyline | 10-23 | 30.3 | 26.1 | 4.2 | -10.16 | -30.8 | -0.12 | 48.5 | DROP: below break-even |
| pre_move+sharp_gap | moneyline | 6-19 | 24.0 | 22.8 | 1.2 | -9.9 | -39.6 | -0.58 | 44.0 | redundant -- identical record to pre_move alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 0-1 | 0.0 | 22.8 | -22.8 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm | moneyline | 0-1 | 0.0 | 22.8 | -22.8 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm alone, not independent confirmation |
| consensus_gap+rlm_quiet | moneyline | 0-1 | 0.0 | 22.8 | -22.8 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm | moneyline | 0-1 | 0.0 | 22.8 | -22.8 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | moneyline | 0-1 | 0.0 | 22.8 | -22.8 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 22.8 | -22.8 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm alone, not independent confirmation |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 22.8 | -22.8 | -3.0 | -100.0 | -0.47 | 33.3 | keep collecting (3/30) |
| money_level+money_moving | moneyline | 4-0 | 100.0 | 77.2 | 22.8 | +2.02 | 50.4 | -0.78 | 50.0 | keep collecting (4/30) |
| pin_move+sharp_gap | moneyline | 3-5 | 37.5 | 56.8 | -19.3 | -3.21 | -40.2 | 0.7 | 50.0 | keep collecting (8/30) |
| follow_move+money_level | moneyline | 1-0 | 100.0 | 77.2 | 22.8 | +0.56 | 56.2 | -3.1 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | moneyline | 1-0 | 100.0 | 77.2 | 22.8 | +0.56 | 56.2 | -3.1 | 0.0 | keep collecting (1/30) |
| consensus_gap+money_level | moneyline | 3-1 | 75.0 | 50.0 | 25.0 | +0.9 | 22.4 | -2.6 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_value | moneyline | 0-8 | 0.0 | 22.8 | -22.8 | -8.0 | -100.0 | 1.31 | 62.5 | keep collecting (8/30) |
| consensus_gap+pin_rlm | moneyline | 1-7 | 12.5 | 22.8 | -10.3 | -5.92 | -74.0 | -1.09 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 22.8 | -22.8 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| money_level+pre_move | moneyline | 0-1 | 0.0 | 22.8 | -22.8 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+pre_move | moneyline | 1-7 | 12.5 | 22.8 | -10.3 | -5.92 | -74.0 | -1.09 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 1-7 | 12.5 | 22.8 | -10.3 | -5.92 | -74.0 | -1.09 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | moneyline | 2-1 | 66.7 | 40.9 | 25.7 | +0.47 | 15.7 | 1.1 | 66.7 | keep collecting (3/30) |
| pin_value+pre_move | moneyline | 0-6 | 0.0 | 22.8 | -22.8 | -6.0 | -100.0 | 1.9 | 66.7 | keep collecting (6/30) |
| pin_value+sharp_gap | moneyline | 0-6 | 0.0 | 22.8 | -22.8 | -6.0 | -100.0 | 1.9 | 66.7 | keep collecting (6/30) |
| consensus_gap+money_moving | moneyline | 1-1 | 50.0 | 22.8 | 27.2 | +0.08 | 4.0 | 3.45 | 100.0 | keep collecting (2/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 22.8 | -22.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving+pre_move | moneyline | 1-1 | 50.0 | 22.8 | 27.2 | +0.08 | 4.0 | 3.45 | 100.0 | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-2 | 0.0 | 22.8 | -22.8 | -2.0 | -100.0 | 0.9 | 50.0 | keep collecting (2/30) |
| money_level+pin_move | moneyline | 10-3 | 76.9 | 77.2 | -0.3 | +0.78 | 6.0 | 1.63 | 69.2 | keep collecting (13/30) |
| book_lag+consensus_gap | moneyline | 2-1 | 66.7 | 22.8 | 43.9 | +1.42 | 47.3 | 0.63 | 66.7 | keep collecting (3/30) |
| book_lag+money_moving | moneyline | 1-0 | 100.0 | 22.8 | 77.2 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+pin_rlm | moneyline | 1-0 | 100.0 | 22.8 | 77.2 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+pre_move | moneyline | 2-0 | 100.0 | 22.8 | 77.2 | +2.42 | 121.0 | -0.25 | 50.0 | keep collecting (2/30) |
| book_lag+sharp_gap | moneyline | 2-0 | 100.0 | 22.8 | 77.2 | +2.42 | 121.0 | -0.25 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 1-0 | 100.0 | 22.8 | 77.2 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 0-2 | 0.0 | 22.8 | -22.8 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| pin_move+pre_move | moneyline | 0-2 | 0.0 | 22.8 | -22.8 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| book_lag+money_level | moneyline | 1-0 | 100.0 | 77.2 | 22.8 | +0.39 | 38.5 | -4.5 | 0.0 | keep collecting (1/30) |
| book_lag+pin_move | moneyline | 1-0 | 100.0 | 77.2 | 22.8 | +0.39 | 38.5 | -4.5 | 0.0 | keep collecting (1/30) |
| follow_move+rlm | spread | 2-7 | 22.2 | 45.6 | -23.4 | -5.17 | -57.4 | 0.0 | 11.1 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 3-7 | 30.0 | 47.4 | -17.4 | -4.33 | -43.3 | 0.0 | 10.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 1-2 | 33.3 | 45.6 | -12.3 | -1.17 | -38.9 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 13-8 | 61.9 | 54.4 | 7.5 | +4.01 | 19.1 | 0.07 | 23.8 | keep collecting (21/30) |
| rlm+rlm_quiet | spread | 2-7 | 22.2 | 45.6 | -23.4 | -5.17 | -57.4 | 0.0 | 11.1 | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+rlm_ratio | spread | 1-2 | 33.3 | 45.6 | -12.3 | -1.17 | -38.9 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 1-2 | 33.3 | 45.6 | -12.3 | -1.17 | -38.9 | 0.0 | 0.0 | keep collecting (3/30) |
| rlm_quiet+rlm_ratio | spread | 1-2 | 33.3 | 45.6 | -12.3 | -1.17 | -38.9 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | spread | 1-2 | 33.3 | 45.6 | -12.3 | -1.17 | -38.9 | 0.0 | 0.0 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | spread | 1-2 | 33.3 | 45.6 | -12.3 | -1.17 | -38.9 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+pin_value | spread | 6-4 | 60.0 | 55.3 | 4.7 | +1.04 | 10.4 | 0.4 | 40.0 | keep collecting (10/30) |
| money_level+sharp_gap | spread | 25-10 | 71.4 | 55.6 | 15.8 | +12.79 | 36.5 | 0.07 | 31.4 | PROMOTE: beats break-even and its own base rate |
| follow_move+pin_value | spread | 6-2 | 75.0 | 59.9 | 15.1 | +3.21 | 40.1 | 0.25 | 25.0 | keep collecting (8/30) |
| pin_value+sharp_gap | spread | 11-1 | 91.7 | 56.6 | 35.1 | +8.68 | 72.4 | 0.38 | 41.7 | keep collecting (12/30) |
| consensus_gap+follow_move | spread | 2-1 | 66.7 | 63.2 | 3.5 | +0.65 | 21.8 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+money_level | spread | 8-2 | 80.0 | 60.5 | 19.5 | +4.8 | 48.0 | 0.55 | 50.0 | keep collecting (10/30) |
| consensus_gap+sharp_gap | spread | 7-2 | 77.8 | 60.2 | 17.5 | +3.97 | 44.1 | 0.67 | 66.7 | keep collecting (9/30) |
| follow_move+money_level | spread | 12-8 | 60.0 | 57.9 | 2.1 | +3.17 | 15.9 | 0.07 | 25.0 | keep collecting (20/30) |
| money_level+pin_value | spread | 12-3 | 80.0 | 59.6 | 20.4 | +7.59 | 50.6 | 0.3 | 33.3 | keep collecting (15/30) |
| follow_move+money_moving | spread | 2-2 | 50.0 | 56.6 | -6.6 | -0.19 | -4.7 | 0.0 | 0.0 | keep collecting (4/30) |
| money_level+money_moving | spread | 3-2 | 60.0 | 52.6 | 7.4 | +0.8 | 16.0 | -0.6 | 20.0 | keep collecting (5/30) |
| money_moving+pin_value | spread | 4-1 | 80.0 | 52.6 | 27.4 | +2.63 | 52.7 | 0.4 | 40.0 | keep collecting (5/30) |
| money_moving+sharp_gap | spread | 2-2 | 50.0 | 56.6 | -6.6 | -0.15 | -3.8 | -0.25 | 25.0 | keep collecting (4/30) |
| book_lag+consensus_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.13 | -6.5 | 0.75 | 100.0 | keep collecting (2/30) |
| money_level+pre_move | spread | 1-1 | 50.0 | 36.8 | 13.2 | -0.09 | -4.5 | -1.0 | 0.0 | keep collecting (2/30) |
| pre_move+sharp_gap | spread | 1-2 | 33.3 | 45.6 | -12.3 | -1.09 | -36.4 | -0.5 | 33.3 | redundant -- identical record to pre_move alone, not independent confirmation |
| money_level+pin_move | spread | 6-4 | 60.0 | 57.9 | 2.1 | +1.5 | 15.1 | 0.0 | 40.0 | keep collecting (10/30) |
| money_moving+pin_move | spread | 1-0 | 100.0 | 36.8 | 63.2 | +0.95 | 95.2 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+money_level | spread | 2-1 | 66.7 | 63.2 | 3.5 | +0.74 | 24.7 | 0.33 | 66.7 | keep collecting (3/30) |
| book_lag+money_moving | spread | 0-1 | 0.0 | 63.2 | -63.2 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+sharp_gap | spread | 2-1 | 66.7 | 63.2 | 3.5 | +0.74 | 24.7 | 0.33 | 66.7 | keep collecting (3/30) |
| money_moving+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-0 | 100.0 | 63.2 | 36.8 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+pin_move | spread | 3-6 | 33.3 | 60.2 | -26.9 | -3.19 | -35.4 | -0.22 | 22.2 | keep collecting (9/30) |
| pin_move+pin_value | spread | 3-2 | 60.0 | 63.2 | -3.2 | +0.65 | 13.0 | 1.0 | 80.0 | keep collecting (5/30) |
| pin_move+sharp_gap | spread | 5-1 | 83.3 | 63.2 | 20.2 | +3.55 | 59.2 | 0.33 | 66.7 | keep collecting (6/30) |
| money_moving+rlm | spread | 0-1 | 0.0 | 36.8 | -36.8 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+rlm | spread | 0-2 | 0.0 | 63.2 | -63.2 | -2.0 | -100.0 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_move+rlm_quiet | spread | 0-2 | 0.0 | 63.2 | -63.2 | -2.0 | -100.0 | -0.5 | 0.0 | keep collecting (2/30) |
| book_lag+pin_move | spread | 2-0 | 100.0 | 63.2 | 36.8 | +1.74 | 87.0 | 1.5 | 100.0 | keep collecting (2/30) |
| book_lag+pin_value | spread | 2-0 | 100.0 | 63.2 | 36.8 | +1.74 | 87.0 | 1.5 | 100.0 | keep collecting (2/30) |
| consensus_gap+pin_move | spread | 1-1 | 50.0 | 63.2 | -13.2 | -0.13 | -6.5 | 1.0 | 100.0 | keep collecting (2/30) |
| consensus_gap+money_moving | spread | 1-0 | 100.0 | 36.8 | 63.2 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_value | total | 3-3 | 50.0 | 51.8 | -1.8 | -0.29 | -4.9 | -0.17 | 16.7 | keep collecting (6/30) |
| money_level+sharp_gap | total | 17-12 | 58.6 | 51.4 | 7.3 | +3.32 | 11.4 | -0.14 | 31.0 | keep collecting (29/30) |
| pin_value+sharp_gap | total | 6-4 | 60.0 | 50.0 | 10.0 | +1.32 | 13.2 | 0.1 | 30.0 | keep collecting (10/30) |
| money_level+pre_move | total | 1-2 | 33.3 | 49.1 | -15.8 | -1.13 | -37.7 | 1.0 | 33.3 | keep collecting (3/30) |
| pre_move+sharp_gap | total | 6-7 | 46.2 | 47.8 | -1.6 | -1.57 | -12.1 | 0.0 | 30.8 | redundant -- identical record to pre_move alone, not independent confirmation |
| pin_move+pin_value | total | 1-3 | 25.0 | 51.3 | -26.3 | -2.13 | -53.2 | 0.5 | 50.0 | keep collecting (4/30) |
| follow_move+money_level | total | 0-1 | 0.0 | 52.6 | -52.6 | -1.0 | -100.0 | -3.0 | 0.0 | redundant -- identical record to follow_move alone, not independent confirmation |
| money_level+money_moving | total | 3-1 | 75.0 | 51.3 | 23.7 | +1.75 | 43.7 | 0.0 | 25.0 | keep collecting (4/30) |
| money_moving+sharp_gap | total | 3-0 | 100.0 | 49.1 | 50.9 | +2.83 | 94.3 | -0.67 | 0.0 | keep collecting (3/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 47.4 | 52.6 | +0.93 | 92.6 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_move | total | 4-0 | 100.0 | 51.3 | 48.7 | +3.6 | 90.1 | 0.5 | 50.0 | keep collecting (4/30) |
| pin_move+sharp_gap | total | 5-0 | 100.0 | 49.5 | 50.5 | +4.47 | 89.5 | 1.0 | 80.0 | keep collecting (5/30) |
| money_moving+pre_move | total | 1-0 | 100.0 | 47.4 | 52.6 | +0.95 | 95.2 | -2.0 | 0.0 | keep collecting (1/30) |
| pin_value+pre_move | total | 2-0 | 100.0 | 47.4 | 52.6 | +1.74 | 87.1 | 0.5 | 50.0 | keep collecting (2/30) |
| pin_move+pin_rlm | total | 1-0 | 100.0 | 47.4 | 52.6 | +0.95 | 95.2 | 1.0 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pre_move | total | 1-0 | 100.0 | 47.4 | 52.6 | +0.95 | 95.2 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_rlm+pre_move | total | 1-0 | 100.0 | 47.4 | 52.6 | +0.95 | 95.2 | 1.0 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | total | 1-0 | 100.0 | 47.4 | 52.6 | +0.95 | 95.2 | 1.0 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 15-33 | 31.2 | 37.4 | -6.1 | -17.31 | -36.1 |  |  | DROP: below break-even |
| pin_move | both | 58-49 | 54.2 | 50.5 | 3.7 | -2.24 | -2.1 |  |  | no edge shown yet |
| money_delta | both | 15-31 | 32.6 | 37.8 | -5.1 | -13.75 | -29.9 |  |  | DROP: below break-even |
| pin_rlm | both | 5-14 | 26.3 | 31.6 | -5.3 | -9.07 | -47.7 |  |  | keep collecting (19/30) |
| pre_move | both | 4-11 | 26.7 | 36.0 | -9.4 | -5.42 | -36.1 |  |  | keep collecting (15/30) |
| follow_move | both | 91-84 | 52.0 | 50.7 | 1.3 | -7.43 | -4.2 |  |  | no edge shown yet |
| rlm | both | 18-37 | 32.7 | 36.9 | -4.2 | -17.5 | -31.8 |  |  | DROP: below break-even |
| rlm_ratio | both | 6-16 | 27.3 | 34.1 | -6.9 | -9.17 | -41.7 |  |  | keep collecting (22/30) |
| money_level | both | 102-65 | 61.1 | 60.3 | 0.8 | +7.09 | 4.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 75-91 | 45.2 | 48.0 | -2.8 | -24.3 | -14.6 |  |  | DROP: below break-even |
| money_moving | both | 58-79 | 42.3 | 46.7 | -4.4 | -28.6 | -20.9 |  |  | DROP: below break-even |
| pin_value | both | 73-66 | 52.5 | 48.3 | 4.2 | -1.37 | -1.0 |  |  | no edge shown yet |
| book_lag | both | 5-1 | 83.3 | 63.5 | 19.9 | +2.86 | 47.7 |  |  | keep collecting (6/30) |
| consensus_gap | both | 22-45 | 32.8 | 30.5 | 2.3 | -16.57 | -24.7 |  |  | DROP: below break-even |
| follow_move+rlm | both | 18-37 | 32.7 | 36.9 | -4.2 | -17.5 | -31.8 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | both | 15-33 | 31.2 | 37.4 | -6.1 | -17.31 | -36.1 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 6-16 | 27.3 | 34.1 | -6.9 | -9.17 | -41.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 32-38 | 45.7 | 49.0 | -3.3 | -9.94 | -14.2 |  |  | no edge shown yet |
| money_level+pin_value | both | 20-11 | 64.5 | 54.0 | 10.5 | +6.34 | 20.4 |  |  | no edge shown yet |
| rlm+rlm_quiet | both | 15-32 | 31.9 | 36.8 | -4.9 | -16.31 | -34.7 |  |  | DROP: below break-even |
| rlm+rlm_ratio | both | 6-16 | 27.3 | 34.1 | -6.9 | -9.17 | -41.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 10-22 | 31.2 | 37.4 | -6.2 | -11.49 | -35.9 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 3-12 | 20.0 | 33.2 | -13.2 | -8.98 | -59.9 |  |  | keep collecting (15/30) |
| rlm_quiet+sharp_gap | both | 7-17 | 29.2 | 37.4 | -8.3 | -10.3 | -42.9 |  |  | keep collecting (24/30) |
| rlm_ratio+sharp_gap | both | 6-16 | 27.3 | 34.1 | -6.9 | -9.17 | -41.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 48-38 | 55.8 | 57.8 | -2.0 | -1.41 | -1.6 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 7-4 | 63.6 | 53.6 | 10.0 | +1.86 | 16.9 |  |  | keep collecting (11/30) |
| pre_move+sharp_gap | both | 4-11 | 26.7 | 36.0 | -9.4 | -5.42 | -36.1 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+money_level | both | 41-25 | 62.1 | 61.9 | 0.3 | +3.49 | 5.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| book_lag+money_level | both | 2-1 | 66.7 | 72.5 | -5.8 | +0.4 | 13.4 |  |  | keep collecting (3/30) |
| consensus_gap+pre_move | both | 1-5 | 16.7 | 22.8 | -6.1 | -2.1 | -35.0 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 11-25 | 30.6 | 29.2 | 1.3 | -9.91 | -27.5 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 15-9 | 62.5 | 49.7 | 12.8 | +3.88 | 16.2 |  |  | keep collecting (24/30) |
| pin_value+rlm | both | 3-6 | 33.3 | 41.5 | -8.2 | -3.38 | -37.6 |  |  | keep collecting (9/30) |
| pin_value+rlm_quiet | both | 3-6 | 33.3 | 41.5 | -8.2 | -3.38 | -37.6 |  |  | keep collecting (9/30) |
| pin_value+pre_move | both | 1-2 | 33.3 | 31.0 | 2.3 | -1.15 | -38.4 |  |  | keep collecting (3/30) |
| pin_value+sharp_gap | both | 20-19 | 51.3 | 45.7 | 5.6 | -1.95 | -5.0 |  |  | no edge shown yet |
| consensus_gap+follow_move | both | 7-18 | 28.0 | 28.8 | -0.8 | -8.94 | -35.8 |  |  | keep collecting (25/30) |
| consensus_gap+rlm | both | 5-17 | 22.7 | 24.6 | -1.9 | -9.48 | -43.1 |  |  | keep collecting (22/30) |
| consensus_gap+rlm_quiet | both | 3-16 | 15.8 | 24.9 | -9.1 | -11.38 | -59.9 |  |  | keep collecting (19/30) |
| consensus_gap+pin_value | both | 4-12 | 25.0 | 27.1 | -2.1 | -6.97 | -43.6 |  |  | keep collecting (16/30) |
| book_lag+consensus_gap | both | 3-0 | 100.0 | 54.4 | 45.6 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| book_lag+money_moving | both | 1-0 | 100.0 | 36.8 | 63.2 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | both | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | both | 8-21 | 27.6 | 27.9 | -0.4 | -10.28 | -35.5 |  |  | keep collecting (29/30) |
| money_moving+pin_value | both | 13-15 | 46.4 | 44.4 | 2.0 | -4.01 | -14.3 |  |  | keep collecting (28/30) |
| money_moving+pre_move | both | 1-5 | 16.7 | 33.9 | -17.3 | -4.13 | -68.8 |  |  | keep collecting (6/30) |
| money_moving+sharp_gap | both | 37-53 | 41.1 | 45.5 | -4.3 | -18.36 | -20.4 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 25-36 | 41.0 | 47.7 | -6.7 | -14.27 | -23.4 |  |  | DROP: below break-even |
| money_moving+rlm | both | 8-23 | 25.8 | 35.1 | -9.3 | -14.31 | -46.2 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | both | 5-18 | 21.7 | 34.2 | -12.5 | -13.12 | -57.0 |  |  | keep collecting (23/30) |
| money_level+money_moving | both | 37-28 | 56.9 | 58.1 | -1.2 | +0.28 | 0.4 |  |  | no edge shown yet |
| money_level+pin_move | both | 35-18 | 66.0 | 61.0 | 5.0 | +5.85 | 11.0 |  |  | PROMOTE: beats break-even and its own base rate |
| money_moving+pin_move | both | 27-29 | 48.2 | 47.2 | 1.0 | -6.4 | -11.4 |  |  | no edge shown yet |
| pin_move+pin_value | both | 16-16 | 50.0 | 45.1 | 4.9 | -2.25 | -7.0 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 29-31 | 48.3 | 47.0 | 1.4 | -5.97 | -9.9 |  |  | no edge shown yet |
| consensus_gap+pin_move | both | 6-13 | 31.6 | 27.8 | 3.8 | -5.81 | -30.6 |  |  | keep collecting (19/30) |
| consensus_gap+money_delta | both | 5-7 | 41.7 | 22.8 | 18.9 | +1.05 | 8.7 |  |  | keep collecting (12/30) |
| consensus_gap+pin_rlm | both | 2-9 | 18.2 | 22.8 | -4.6 | -6.76 | -61.5 |  |  | keep collecting (11/30) |
| consensus_gap+rlm_ratio | both | 3-7 | 30.0 | 22.8 | 7.2 | -2.86 | -28.6 |  |  | keep collecting (10/30) |
| follow_move+money_delta | both | 7-14 | 33.3 | 36.3 | -2.9 | -6.13 | -29.2 |  |  | keep collecting (21/30) |
| follow_move+pin_rlm | both | 5-11 | 31.2 | 33.2 | -2.0 | -6.07 | -38.0 |  |  | keep collecting (16/30) |
| money_delta+money_level | both | 3-5 | 37.5 | 38.6 | -1.1 | -1.76 | -22.0 |  |  | keep collecting (8/30) |
| money_delta+money_moving | both | 14-25 | 35.9 | 37.5 | -1.6 | -8.66 | -22.2 |  |  | DROP: below break-even |
| money_delta+pin_rlm | both | 4-10 | 28.6 | 32.0 | -3.4 | -5.94 | -42.4 |  |  | keep collecting (14/30) |
| money_delta+rlm | both | 6-12 | 33.3 | 35.6 | -2.2 | -5.13 | -28.5 |  |  | keep collecting (18/30) |
| money_delta+rlm_ratio | both | 5-9 | 35.7 | 33.0 | 2.8 | -3.04 | -21.7 |  |  | keep collecting (14/30) |
| money_delta+sharp_gap | both | 13-27 | 32.5 | 37.1 | -4.6 | -11.61 | -29.0 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 0-3 | 0.0 | 40.9 | -40.9 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_level+rlm | both | 0-3 | 0.0 | 40.9 | -40.9 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_level+rlm_ratio | both | 0-3 | 0.0 | 40.9 | -40.9 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | both | 5-12 | 29.4 | 32.6 | -3.2 | -7.07 | -41.6 |  |  | keep collecting (17/30) |
| money_moving+rlm_ratio | both | 6-13 | 31.6 | 33.1 | -1.5 | -6.17 | -32.5 |  |  | keep collecting (19/30) |
| pin_rlm+rlm | both | 5-11 | 31.2 | 33.2 | -2.0 | -6.07 | -38.0 |  |  | keep collecting (16/30) |
| pin_rlm+rlm_ratio | both | 5-11 | 31.2 | 33.2 | -2.0 | -6.07 | -38.0 |  |  | keep collecting (16/30) |
| pin_rlm+sharp_gap | both | 5-14 | 26.3 | 31.6 | -5.3 | -9.07 | -47.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+pin_move | both | 49-38 | 56.3 | 51.9 | 4.4 | +0.73 | 0.8 |  |  | no edge shown yet |
| pin_move+rlm_quiet | both | 13-21 | 38.2 | 39.3 | -1.1 | -7.22 | -21.2 |  |  | DROP: below break-even |
| money_delta+pin_move | both | 7-14 | 33.3 | 38.2 | -4.8 | -7.2 | -34.3 |  |  | keep collecting (21/30) |
| money_delta+pin_value | both | 1-7 | 12.5 | 37.5 | -25.0 | -6.17 | -77.1 |  |  | keep collecting (8/30) |
| money_delta+rlm_quiet | both | 3-7 | 30.0 | 34.0 | -4.0 | -3.94 | -39.4 |  |  | keep collecting (10/30) |
| pin_move+pin_rlm | both | 5-12 | 29.4 | 32.6 | -3.2 | -7.07 | -41.6 |  |  | keep collecting (17/30) |
| pin_move+rlm | both | 15-23 | 39.5 | 39.2 | 0.2 | -7.31 | -19.2 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | both | 5-9 | 35.7 | 34.7 | 1.0 | -4.07 | -29.1 |  |  | keep collecting (14/30) |
| pin_rlm+pin_value | both | 1-5 | 16.7 | 31.0 | -14.3 | -4.13 | -68.8 |  |  | keep collecting (6/30) |
| pin_rlm+rlm_quiet | both | 3-8 | 27.3 | 30.8 | -3.5 | -4.98 | -45.3 |  |  | keep collecting (11/30) |
| pin_value+rlm_ratio | both | 1-3 | 25.0 | 35.1 | -10.1 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| money_delta+pre_move | both | 1-4 | 20.0 | 31.2 | -11.2 | -3.13 | -62.6 |  |  | keep collecting (5/30) |
| money_level+pre_move | both | 1-1 | 50.0 | 36.8 | 13.2 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| pin_move+pre_move | both | 0-2 | 0.0 | 22.8 | -22.8 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm+pre_move | both | 0-2 | 0.0 | 22.8 | -22.8 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| rlm_quiet | moneyline | 3-17 | 15.0 | 22.8 | -7.8 | -12.38 | -61.9 |  |  | keep collecting (20/30) |
| rlm_quiet | spread | 4-11 | 26.7 | 47.4 | -20.7 | -7.19 | -47.9 |  |  | keep collecting (15/30) |
| rlm_quiet | total | 8-5 | 61.5 | 48.2 | 13.4 | +2.26 | 17.4 |  |  | keep collecting (13/30) |
| pin_move | moneyline | 19-18 | 51.4 | 49.3 | 2.1 | -6.58 | -17.8 |  |  | no edge shown yet |
| pin_move | spread | 11-16 | 40.7 | 52.4 | -11.7 | -5.94 | -22.0 |  |  | keep collecting (27/30) |
| pin_move | total | 26-15 | 63.4 | 50.3 | 13.1 | +8.54 | 20.8 |  |  | no edge shown yet |
| pin_move | tt_away | 1-0 | 100.0 | 49.1 | 50.9 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| pin_move | tt_home | 1-0 | 100.0 | 49.1 | 50.9 | +0.89 | 88.5 |  |  | keep collecting (1/30) |
| money_delta | moneyline | 5-7 | 41.7 | 22.8 | 18.9 | +1.05 | 8.7 |  |  | keep collecting (12/30) |
| money_delta | spread | 4-14 | 22.2 | 38.3 | -16.1 | -10.39 | -57.7 |  |  | keep collecting (18/30) |
| money_delta | total | 6-10 | 37.5 | 48.4 | -10.9 | -4.41 | -27.6 |  |  | keep collecting (16/30) |
| pin_rlm | moneyline | 2-10 | 16.7 | 22.8 | -6.1 | -7.76 | -64.7 |  |  | keep collecting (12/30) |
| pin_rlm | spread | 0-3 | 0.0 | 45.6 | -45.6 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_rlm | total | 3-1 | 75.0 | 47.4 | 27.6 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| pre_move | moneyline | 1-6 | 14.3 | 30.6 | -16.3 | -3.1 | -44.3 |  |  | keep collecting (7/30) |
| pre_move | spread | 2-3 | 40.0 | 36.8 | 3.2 | -1.17 | -23.4 |  |  | keep collecting (5/30) |
| pre_move | total | 1-2 | 33.3 | 47.4 | -14.0 | -1.15 | -38.4 |  |  | keep collecting (3/30) |
| follow_move | moneyline | 22-24 | 47.8 | 48.8 | -1.0 | -9.95 | -21.6 |  |  | no edge shown yet |
| follow_move | spread | 22-28 | 44.0 | 53.7 | -9.7 | -7.63 | -15.3 |  |  | no edge shown yet |
| follow_move | total | 20-11 | 64.5 | 49.9 | 14.6 | +7.22 | 23.3 |  |  | no edge shown yet |
| follow_move | tt_away | 14-8 | 63.6 | 49.8 | 13.9 | +4.39 | 20.0 |  |  | keep collecting (22/30) |
| follow_move | tt_home | 13-13 | 50.0 | 49.9 | 0.1 | -1.47 | -5.7 |  |  | keep collecting (26/30) |
| rlm | moneyline | 5-18 | 21.7 | 22.8 | -1.1 | -10.48 | -45.6 |  |  | keep collecting (23/30) |
| rlm | spread | 4-13 | 23.5 | 46.1 | -22.6 | -9.19 | -54.0 |  |  | keep collecting (17/30) |
| rlm | total | 9-6 | 60.0 | 48.1 | 11.9 | +2.17 | 14.4 |  |  | keep collecting (15/30) |
| rlm_ratio | moneyline | 3-8 | 27.3 | 22.8 | 4.5 | -3.86 | -35.1 |  |  | keep collecting (11/30) |
| rlm_ratio | spread | 0-7 | 0.0 | 44.4 | -44.4 | -7.0 | -100.0 |  |  | keep collecting (7/30) |
| rlm_ratio | total | 3-1 | 75.0 | 47.4 | 27.6 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| money_level | moneyline | 44-12 | 78.6 | 73.3 | 5.3 | +7.4 | 13.2 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level | spread | 28-27 | 50.9 | 55.5 | -4.6 | -1.72 | -3.1 |  |  | no edge shown yet |
| money_level | total | 30-26 | 53.6 | 52.0 | 1.6 | +1.42 | 2.5 |  |  | no edge shown yet |
| sharp_gap | moneyline | 24-30 | 44.4 | 46.0 | -1.5 | -9.39 | -17.4 |  |  | no edge shown yet |
| sharp_gap | spread | 24-32 | 42.9 | 47.7 | -4.8 | -10.4 | -18.6 |  |  | no edge shown yet |
| sharp_gap | total | 27-29 | 48.2 | 50.3 | -2.1 | -4.51 | -8.1 |  |  | no edge shown yet |
| money_moving | moneyline | 20-26 | 43.5 | 44.1 | -0.6 | -10.13 | -22.0 |  |  | no edge shown yet |
| money_moving | spread | 16-29 | 35.6 | 45.6 | -10.1 | -14.58 | -32.4 |  |  | DROP: below break-even |
| money_moving | total | 22-24 | 47.8 | 50.3 | -2.5 | -3.88 | -8.4 |  |  | no edge shown yet |
| pin_value | moneyline | 3-11 | 21.4 | 26.7 | -5.3 | -7.14 | -51.0 |  |  | keep collecting (14/30) |
| pin_value | spread | 18-7 | 72.0 | 53.7 | 18.3 | +8.77 | 35.1 |  |  | keep collecting (25/30) |
| pin_value | total | 16-13 | 55.2 | 50.1 | 5.1 | +0.97 | 3.3 |  |  | keep collecting (29/30) |
| pin_value | tt_away | 16-19 | 45.7 | 50.1 | -4.4 | -5.01 | -14.3 |  |  | no edge shown yet |
| pin_value | tt_home | 20-16 | 55.6 | 49.9 | 5.7 | +1.04 | 2.9 |  |  | no edge shown yet |
| book_lag | moneyline | 1-1 | 50.0 | 77.2 | -27.2 | -0.43 | -21.6 |  |  | keep collecting (2/30) |
| book_lag | spread | 4-0 | 100.0 | 56.6 | 43.4 | +3.29 | 82.4 |  |  | keep collecting (4/30) |
| consensus_gap | moneyline | 17-40 | 29.8 | 26.6 | 3.2 | -15.7 | -27.5 |  |  | DROP: below break-even |
| consensus_gap | spread | 5-5 | 50.0 | 52.6 | -2.6 | -0.87 | -8.7 |  |  | keep collecting (10/30) |
| consensus_gap+money_level | moneyline | 6-2 | 75.0 | 50.0 | 25.0 | +3.02 | 37.8 |  |  | keep collecting (8/30) |
| pre_move+sharp_gap | moneyline | 1-6 | 14.3 | 30.6 | -16.3 | -3.1 | -44.3 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| book_lag+money_level | moneyline | 1-1 | 50.0 | 77.2 | -27.2 | -0.43 | -21.6 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pre_move | moneyline | 1-5 | 16.7 | 22.8 | -6.1 | -2.1 | -35.0 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | moneyline | 10-23 | 30.3 | 27.8 | 2.6 | -8.75 | -26.5 |  |  | DROP: below break-even |
| money_level+sharp_gap | moneyline | 18-7 | 72.0 | 70.7 | 1.3 | +2.64 | 10.6 |  |  | keep collecting (25/30) |
| consensus_gap+follow_move | moneyline | 7-17 | 29.2 | 27.3 | 1.8 | -7.94 | -33.1 |  |  | keep collecting (24/30) |
| consensus_gap+rlm | moneyline | 5-16 | 23.8 | 22.8 | 1.0 | -8.48 | -40.4 |  |  | keep collecting (21/30) |
| consensus_gap+rlm_quiet | moneyline | 3-15 | 16.7 | 22.8 | -6.1 | -10.38 | -57.7 |  |  | keep collecting (18/30) |
| follow_move+rlm | moneyline | 5-18 | 21.7 | 22.8 | -1.1 | -10.48 | -45.6 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | moneyline | 3-17 | 15.0 | 22.8 | -7.8 | -12.38 | -61.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm+rlm_quiet | moneyline | 3-17 | 15.0 | 22.8 | -7.8 | -12.38 | -61.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 2-11 | 15.4 | 22.8 | -7.4 | -7.59 | -58.4 |  |  | keep collecting (13/30) |
| pin_value+pre_move | moneyline | 0-2 | 0.0 | 22.8 | -22.8 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_value+sharp_gap | moneyline | 1-9 | 10.0 | 28.2 | -18.2 | -8.56 | -85.6 |  |  | keep collecting (10/30) |
| follow_move+money_level | moneyline | 17-6 | 73.9 | 72.5 | 1.4 | +0.53 | 2.3 |  |  | keep collecting (23/30) |
| follow_move+sharp_gap | moneyline | 9-11 | 45.0 | 44.6 | 0.4 | -3.89 | -19.5 |  |  | keep collecting (20/30) |
| follow_move+money_moving | moneyline | 10-15 | 40.0 | 44.6 | -4.6 | -7.16 | -28.6 |  |  | keep collecting (25/30) |
| money_moving+rlm | moneyline | 3-11 | 21.4 | 22.8 | -1.4 | -6.86 | -49.0 |  |  | keep collecting (14/30) |
| money_moving+rlm_quiet | moneyline | 1-10 | 9.1 | 22.8 | -13.7 | -8.76 | -79.6 |  |  | keep collecting (11/30) |
| consensus_gap+money_moving | moneyline | 7-19 | 26.9 | 24.9 | 2.0 | -9.06 | -34.9 |  |  | keep collecting (26/30) |
| consensus_gap+pin_move | moneyline | 6-12 | 33.3 | 25.8 | 7.5 | -4.81 | -26.7 |  |  | keep collecting (18/30) |
| money_moving+pin_move | moneyline | 8-9 | 47.1 | 42.0 | 5.1 | -3.7 | -21.8 |  |  | keep collecting (17/30) |
| money_moving+pin_value | moneyline | 2-7 | 22.2 | 28.8 | -6.6 | -5.59 | -62.2 |  |  | keep collecting (9/30) |
| pin_move+pin_value | moneyline | 2-6 | 25.0 | 29.6 | -4.6 | -4.59 | -57.4 |  |  | keep collecting (8/30) |
| consensus_gap+money_delta | moneyline | 5-7 | 41.7 | 22.8 | 18.9 | +1.05 | 8.7 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| consensus_gap+pin_rlm | moneyline | 2-9 | 18.2 | 22.8 | -4.6 | -6.76 | -61.5 |  |  | keep collecting (11/30) |
| consensus_gap+rlm_ratio | moneyline | 3-7 | 30.0 | 22.8 | 7.2 | -2.86 | -28.6 |  |  | keep collecting (10/30) |
| follow_move+money_delta | moneyline | 3-5 | 37.5 | 22.8 | 14.7 | -0.86 | -10.7 |  |  | keep collecting (8/30) |
| follow_move+pin_rlm | moneyline | 2-7 | 22.2 | 22.8 | -0.6 | -4.76 | -52.9 |  |  | keep collecting (9/30) |
| follow_move+rlm_ratio | moneyline | 3-8 | 27.3 | 22.8 | 4.5 | -3.86 | -35.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | moneyline | 1-1 | 50.0 | 22.8 | 27.2 | +0.46 | 23.0 |  |  | keep collecting (2/30) |
| money_delta+money_moving | moneyline | 5-6 | 45.5 | 22.8 | 22.6 | +2.05 | 18.6 |  |  | keep collecting (11/30) |
| money_delta+pin_rlm | moneyline | 2-7 | 22.2 | 22.8 | -0.6 | -4.76 | -52.9 |  |  | keep collecting (9/30) |
| money_delta+rlm | moneyline | 3-5 | 37.5 | 22.8 | 14.7 | -0.86 | -10.7 |  |  | keep collecting (8/30) |
| money_delta+rlm_ratio | moneyline | 3-5 | 37.5 | 22.8 | 14.7 | -0.86 | -10.7 |  |  | keep collecting (8/30) |
| money_delta+sharp_gap | moneyline | 5-7 | 41.7 | 22.8 | 18.9 | +1.05 | 8.7 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+money_moving | moneyline | 15-6 | 71.4 | 69.4 | 2.0 | +2.32 | 11.0 |  |  | keep collecting (21/30) |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 22.8 | -22.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+rlm | moneyline | 0-1 | 0.0 | 22.8 | -22.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+rlm_ratio | moneyline | 0-1 | 0.0 | 22.8 | -22.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 2-8 | 20.0 | 22.8 | -2.8 | -5.76 | -57.6 |  |  | keep collecting (10/30) |
| money_moving+rlm_ratio | moneyline | 3-7 | 30.0 | 22.8 | 7.2 | -2.86 | -28.6 |  |  | keep collecting (10/30) |
| money_moving+sharp_gap | moneyline | 12-18 | 40.0 | 40.9 | -0.9 | -6.04 | -20.1 |  |  | no edge shown yet |
| pin_rlm+rlm | moneyline | 2-7 | 22.2 | 22.8 | -0.6 | -4.76 | -52.9 |  |  | keep collecting (9/30) |
| pin_rlm+rlm_ratio | moneyline | 2-7 | 22.2 | 22.8 | -0.6 | -4.76 | -52.9 |  |  | keep collecting (9/30) |
| pin_rlm+sharp_gap | moneyline | 2-10 | 16.7 | 22.8 | -6.1 | -7.76 | -64.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm+rlm_ratio | moneyline | 3-8 | 27.3 | 22.8 | 4.5 | -3.86 | -35.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | moneyline | 3-8 | 27.3 | 22.8 | 4.5 | -3.86 | -35.1 |  |  | keep collecting (11/30) |
| rlm_ratio+sharp_gap | moneyline | 3-8 | 27.3 | 22.8 | 4.5 | -3.86 | -35.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_move | moneyline | 18-13 | 58.1 | 52.6 | 5.4 | -2.54 | -8.2 |  |  | no edge shown yet |
| follow_move+pin_value | moneyline | 1-4 | 20.0 | 33.7 | -13.7 | -3.56 | -71.1 |  |  | keep collecting (5/30) |
| money_delta+pin_move | moneyline | 2-5 | 28.6 | 22.8 | 5.8 | -2.76 | -39.4 |  |  | keep collecting (7/30) |
| money_delta+pin_value | moneyline | 0-3 | 0.0 | 22.8 | -22.8 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 1-4 | 20.0 | 22.8 | -2.8 | -2.76 | -55.2 |  |  | keep collecting (5/30) |
| pin_move+pin_rlm | moneyline | 2-8 | 20.0 | 22.8 | -2.8 | -5.76 | -57.6 |  |  | keep collecting (10/30) |
| pin_move+rlm | moneyline | 4-9 | 30.8 | 22.8 | 8.0 | -3.38 | -26.0 |  |  | keep collecting (13/30) |
| pin_move+rlm_quiet | moneyline | 3-9 | 25.0 | 22.8 | 2.2 | -4.38 | -36.5 |  |  | keep collecting (12/30) |
| pin_move+rlm_ratio | moneyline | 2-5 | 28.6 | 22.8 | 5.8 | -2.76 | -39.4 |  |  | keep collecting (7/30) |
| pin_move+sharp_gap | moneyline | 6-9 | 40.0 | 37.3 | 2.7 | -4.81 | -32.1 |  |  | keep collecting (15/30) |
| pin_rlm+pin_value | moneyline | 0-4 | 0.0 | 22.8 | -22.8 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| pin_rlm+rlm_quiet | moneyline | 1-6 | 14.3 | 22.8 | -8.5 | -4.76 | -68.0 |  |  | keep collecting (7/30) |
| pin_value+rlm | moneyline | 0-3 | 0.0 | 22.8 | -22.8 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_value+rlm_quiet | moneyline | 0-3 | 0.0 | 22.8 | -22.8 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_value+rlm_ratio | moneyline | 0-2 | 0.0 | 22.8 | -22.8 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | moneyline | 1-7 | 12.5 | 22.8 | -10.3 | -5.76 | -72.0 |  |  | keep collecting (8/30) |
| rlm_quiet+sharp_gap | moneyline | 1-7 | 12.5 | 22.8 | -10.3 | -5.76 | -72.0 |  |  | keep collecting (8/30) |
| money_level+pin_move | moneyline | 14-4 | 77.8 | 74.2 | 3.6 | +0.84 | 4.7 |  |  | keep collecting (18/30) |
| money_level+pin_value | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.56 | -27.8 |  |  | keep collecting (2/30) |
| money_delta+pre_move | moneyline | 0-2 | 0.0 | 22.8 | -22.8 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_moving+pre_move | moneyline | 0-2 | 0.0 | 22.8 | -22.8 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_move+pre_move | moneyline | 0-2 | 0.0 | 22.8 | -22.8 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm+pre_move | moneyline | 0-2 | 0.0 | 22.8 | -22.8 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| follow_move+rlm | spread | 4-13 | 23.5 | 46.1 | -22.6 | -9.19 | -54.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 4-11 | 26.7 | 47.4 | -20.7 | -7.19 | -47.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-7 | 0.0 | 44.4 | -44.4 | -7.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 13-19 | 40.6 | 51.6 | -11.0 | -7.11 | -22.2 |  |  | no edge shown yet |
| money_level+pin_value | spread | 10-5 | 66.7 | 56.1 | 10.5 | +3.96 | 26.4 |  |  | keep collecting (15/30) |
| rlm+rlm_quiet | spread | 4-10 | 28.6 | 46.2 | -17.7 | -6.19 | -44.2 |  |  | keep collecting (14/30) |
| rlm+rlm_ratio | spread | 0-7 | 0.0 | 44.4 | -44.4 | -7.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 2-10 | 16.7 | 43.4 | -26.8 | -8.1 | -67.5 |  |  | keep collecting (12/30) |
| rlm_quiet+rlm_ratio | spread | 0-4 | 0.0 | 43.4 | -43.4 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| rlm_quiet+sharp_gap | spread | 2-7 | 22.2 | 42.7 | -20.5 | -5.1 | -56.6 |  |  | keep collecting (9/30) |
| rlm_ratio+sharp_gap | spread | 0-7 | 0.0 | 44.4 | -44.4 | -7.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 13-15 | 46.4 | 58.5 | -12.0 | -3.09 | -11.1 |  |  | keep collecting (28/30) |
| follow_move+pin_value | spread | 7-1 | 87.5 | 59.9 | 27.6 | +5.19 | 64.9 |  |  | keep collecting (8/30) |
| pin_value+rlm | spread | 1-0 | 100.0 | 63.2 | 36.8 | +0.87 | 87.0 |  |  | keep collecting (1/30) |
| pin_value+rlm_quiet | spread | 1-0 | 100.0 | 63.2 | 36.8 | +0.87 | 87.0 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | spread | 13-16 | 44.8 | 53.2 | -8.3 | -4.46 | -15.4 |  |  | keep collecting (29/30) |
| consensus_gap+sharp_gap | spread | 1-2 | 33.3 | 45.6 | -12.3 | -1.17 | -38.9 |  |  | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 3-0 | 100.0 | 54.4 | 45.6 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| pin_value+sharp_gap | spread | 10-3 | 76.9 | 53.0 | 23.9 | +5.74 | 44.1 |  |  | keep collecting (13/30) |
| book_lag+money_moving | spread | 1-0 | 100.0 | 36.8 | 63.2 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | spread | 1-2 | 33.3 | 54.4 | -21.1 | -1.22 | -40.6 |  |  | keep collecting (3/30) |
| consensus_gap+pin_value | spread | 2-1 | 66.7 | 45.6 | 21.1 | +0.61 | 20.5 |  |  | keep collecting (3/30) |
| money_moving+pin_value | spread | 6-2 | 75.0 | 53.3 | 21.7 | +3.21 | 40.1 |  |  | keep collecting (8/30) |
| follow_move+pin_move | spread | 9-14 | 39.1 | 54.0 | -14.9 | -5.68 | -24.7 |  |  | keep collecting (23/30) |
| money_level+money_moving | spread | 9-12 | 42.9 | 53.1 | -10.3 | -3.92 | -18.7 |  |  | keep collecting (21/30) |
| money_moving+sharp_gap | spread | 10-19 | 34.5 | 45.0 | -10.5 | -9.91 | -34.2 |  |  | keep collecting (29/30) |
| pin_move+rlm_quiet | spread | 2-7 | 22.2 | 48.5 | -26.3 | -5.1 | -56.6 |  |  | keep collecting (9/30) |
| money_delta+money_moving | spread | 3-12 | 20.0 | 38.6 | -18.6 | -9.3 | -62.0 |  |  | keep collecting (15/30) |
| money_delta+sharp_gap | spread | 3-12 | 20.0 | 38.6 | -18.6 | -9.3 | -62.0 |  |  | keep collecting (15/30) |
| money_delta+money_level | spread | 1-4 | 20.0 | 42.1 | -22.1 | -3.13 | -62.6 |  |  | keep collecting (5/30) |
| money_delta+pre_move | spread | 1-2 | 33.3 | 36.8 | -3.5 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| money_level+pre_move | spread | 1-1 | 50.0 | 36.8 | 13.2 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| money_moving+pre_move | spread | 1-2 | 33.3 | 36.8 | -3.5 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| pre_move+sharp_gap | spread | 2-3 | 40.0 | 36.8 | 3.2 | -1.17 | -23.4 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+money_moving | spread | 6-14 | 30.0 | 50.0 | -20.0 | -8.4 | -42.0 |  |  | keep collecting (20/30) |
| money_moving+pin_move | spread | 4-10 | 28.6 | 48.1 | -19.5 | -6.31 | -45.0 |  |  | keep collecting (14/30) |
| money_moving+rlm | spread | 1-8 | 11.1 | 42.7 | -31.6 | -7.05 | -78.3 |  |  | keep collecting (9/30) |
| money_moving+rlm_quiet | spread | 1-5 | 16.7 | 41.2 | -24.6 | -4.05 | -67.5 |  |  | keep collecting (6/30) |
| pin_move+rlm | spread | 2-8 | 20.0 | 47.4 | -27.4 | -6.1 | -61.0 |  |  | keep collecting (10/30) |
| pin_move+sharp_gap | spread | 8-12 | 40.0 | 50.0 | -10.0 | -4.67 | -23.3 |  |  | keep collecting (20/30) |
| follow_move+money_delta | spread | 1-5 | 16.7 | 41.2 | -24.6 | -4.0 | -66.7 |  |  | keep collecting (6/30) |
| follow_move+pin_rlm | spread | 0-3 | 0.0 | 45.6 | -45.6 | -3.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+pin_move | spread | 2-3 | 40.0 | 42.1 | -2.1 | -1.17 | -23.3 |  |  | keep collecting (5/30) |
| money_delta+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_delta+rlm | spread | 0-4 | 0.0 | 43.4 | -43.4 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| money_delta+rlm_ratio | spread | 0-3 | 0.0 | 45.6 | -45.6 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_level+pin_move | spread | 6-8 | 42.9 | 57.5 | -14.7 | -2.58 | -18.5 |  |  | keep collecting (14/30) |
| money_level+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_moving+pin_rlm | spread | 0-3 | 0.0 | 45.6 | -45.6 | -3.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-5 | 0.0 | 42.1 | -42.1 | -5.0 | -100.0 |  |  | keep collecting (5/30) |
| pin_move+pin_rlm | spread | 0-3 | 0.0 | 45.6 | -45.6 | -3.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | spread | 0-3 | 0.0 | 45.6 | -45.6 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_rlm+rlm | spread | 0-3 | 0.0 | 45.6 | -45.6 | -3.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | spread | 0-3 | 0.0 | 45.6 | -45.6 | -3.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 0-3 | 0.0 | 45.6 | -45.6 | -3.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+rlm_quiet | spread | 0-1 | 0.0 | 36.8 | -36.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+follow_move | spread | 0-1 | 0.0 | 63.2 | -63.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+pin_move | spread | 0-1 | 0.0 | 63.2 | -63.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+rlm | spread | 0-1 | 0.0 | 63.2 | -63.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 0-1 | 0.0 | 63.2 | -63.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta+pin_value | spread | 1-0 | 100.0 | 36.8 | 63.2 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| pin_move+pin_value | spread | 4-2 | 66.7 | 50.0 | 16.7 | +1.52 | 25.3 |  |  | keep collecting (6/30) |
| book_lag+money_level | spread | 1-0 | 100.0 | 63.2 | 36.8 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| consensus_gap+money_level | spread | 1-2 | 33.3 | 63.2 | -29.8 | -1.17 | -38.9 |  |  | keep collecting (3/30) |
| pin_rlm+rlm_quiet | spread | 0-1 | 0.0 | 36.8 | -36.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | total | 17-15 | 53.1 | 52.0 | 1.2 | +0.4 | 1.2 |  |  | no edge shown yet |
| pin_value+pre_move | total | 1-0 | 100.0 | 47.4 | 52.6 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| pin_value+sharp_gap | total | 9-7 | 56.2 | 50.7 | 5.6 | +0.88 | 5.5 |  |  | keep collecting (16/30) |
| pre_move+sharp_gap | total | 1-2 | 33.3 | 47.4 | -14.0 | -1.15 | -38.4 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| money_level+pin_value | total | 9-5 | 64.3 | 52.3 | 12.0 | +2.93 | 20.9 |  |  | keep collecting (14/30) |
| money_moving+pre_move | total | 0-1 | 0.0 | 47.4 | -47.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+sharp_gap | total | 15-16 | 48.4 | 50.3 | -1.9 | -2.4 | -7.8 |  |  | no edge shown yet |
| money_level+money_moving | total | 13-10 | 56.5 | 52.4 | 4.1 | +1.88 | 8.2 |  |  | keep collecting (23/30) |
| money_level+pin_move | total | 15-6 | 71.4 | 52.1 | 19.3 | +7.6 | 36.2 |  |  | keep collecting (21/30) |
| money_moving+pin_move | total | 15-10 | 60.0 | 50.3 | 9.7 | +3.6 | 14.4 |  |  | keep collecting (25/30) |
| money_moving+pin_value | total | 5-6 | 45.5 | 50.7 | -5.3 | -1.63 | -14.8 |  |  | keep collecting (11/30) |
| pin_move+pin_value | total | 9-8 | 52.9 | 50.5 | 2.5 | -0.07 | -0.4 |  |  | keep collecting (17/30) |
| pin_move+sharp_gap | total | 15-10 | 60.0 | 50.3 | 9.7 | +3.51 | 14.0 |  |  | keep collecting (25/30) |
| money_delta+money_level | total | 1-0 | 100.0 | 52.6 | 47.4 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+money_moving | total | 6-7 | 46.2 | 48.6 | -2.4 | -1.41 | -10.9 |  |  | keep collecting (13/30) |
| money_delta+sharp_gap | total | 5-8 | 38.5 | 48.6 | -10.1 | -3.36 | -25.9 |  |  | keep collecting (13/30) |
| follow_move+money_delta | total | 3-4 | 42.9 | 47.4 | -4.5 | -1.27 | -18.2 |  |  | keep collecting (7/30) |
| follow_move+money_moving | total | 9-7 | 56.2 | 49.7 | 6.6 | +1.28 | 8.0 |  |  | keep collecting (16/30) |
| follow_move+pin_move | total | 20-11 | 64.5 | 49.9 | 14.6 | +7.22 | 23.3 |  |  | redundant -- identical record to follow_move alone, not independent confirmation |
| follow_move+pin_rlm | total | 3-1 | 75.0 | 47.4 | 27.6 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+pin_value | total | 5-4 | 55.6 | 49.7 | 5.8 | +0.43 | 4.8 |  |  | keep collecting (9/30) |
| follow_move+rlm | total | 9-6 | 60.0 | 48.1 | 11.9 | +2.17 | 14.4 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_quiet | total | 8-5 | 61.5 | 48.2 | 13.4 | +2.26 | 17.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 3-1 | 75.0 | 47.4 | 27.6 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 10-8 | 55.6 | 49.4 | 6.1 | +1.06 | 5.9 |  |  | keep collecting (18/30) |
| money_delta+pin_move | total | 3-6 | 33.3 | 48.0 | -14.6 | -3.27 | -36.4 |  |  | keep collecting (9/30) |
| money_delta+pin_rlm | total | 2-1 | 66.7 | 47.4 | 19.3 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| money_delta+pin_value | total | 0-4 | 0.0 | 48.7 | -48.7 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| money_delta+rlm | total | 3-3 | 50.0 | 47.4 | 2.6 | -0.27 | -4.5 |  |  | keep collecting (6/30) |
| money_delta+rlm_quiet | total | 2-2 | 50.0 | 47.4 | 2.6 | -0.18 | -4.5 |  |  | keep collecting (4/30) |
| money_delta+rlm_ratio | total | 2-1 | 66.7 | 47.4 | 19.3 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | total | 3-1 | 75.0 | 47.4 | 27.6 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm | total | 4-4 | 50.0 | 48.0 | 2.0 | -0.4 | -5.0 |  |  | keep collecting (8/30) |
| money_moving+rlm_quiet | total | 3-3 | 50.0 | 48.2 | 1.8 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| money_moving+rlm_ratio | total | 3-1 | 75.0 | 47.4 | 27.6 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_move+pin_rlm | total | 3-1 | 75.0 | 47.4 | 27.6 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm | total | 9-6 | 60.0 | 48.1 | 11.9 | +2.17 | 14.4 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| pin_move+rlm_quiet | total | 8-5 | 61.5 | 48.2 | 13.4 | +2.26 | 17.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_ratio | total | 3-1 | 75.0 | 47.4 | 27.6 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+pin_value | total | 1-1 | 50.0 | 47.4 | 2.6 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| pin_rlm+rlm | total | 3-1 | 75.0 | 47.4 | 27.6 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | total | 2-1 | 66.7 | 47.4 | 19.3 | +0.78 | 26.0 |  |  | keep collecting (3/30) |
| pin_rlm+rlm_ratio | total | 3-1 | 75.0 | 47.4 | 27.6 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | total | 3-1 | 75.0 | 47.4 | 27.6 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm | total | 2-3 | 40.0 | 48.4 | -8.4 | -1.25 | -25.1 |  |  | keep collecting (5/30) |
| pin_value+rlm_quiet | total | 2-3 | 40.0 | 48.4 | -8.4 | -1.25 | -25.1 |  |  | keep collecting (5/30) |
| pin_value+rlm_ratio | total | 1-1 | 50.0 | 47.4 | 2.6 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| rlm+rlm_quiet | total | 8-5 | 61.5 | 48.2 | 13.4 | +2.26 | 17.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm+rlm_ratio | total | 3-1 | 75.0 | 47.4 | 27.6 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | total | 5-4 | 55.6 | 47.4 | 8.2 | +0.47 | 5.2 |  |  | keep collecting (9/30) |
| rlm_quiet+rlm_ratio | total | 2-1 | 66.7 | 47.4 | 19.3 | +0.78 | 26.0 |  |  | keep collecting (3/30) |
| rlm_quiet+sharp_gap | total | 4-3 | 57.1 | 47.4 | 9.8 | +0.56 | 8.0 |  |  | keep collecting (7/30) |
| rlm_ratio+sharp_gap | total | 3-1 | 75.0 | 47.4 | 27.6 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | total | 11-4 | 73.3 | 51.9 | 21.4 | +6.05 | 40.4 |  |  | keep collecting (15/30) |
| follow_move+pin_move | tt_away | 1-0 | 100.0 | 49.1 | 50.9 | +0.85 | 84.7 |  |  | redundant -- identical record to pin_move alone, not independent confirmation |
| follow_move+pin_move | tt_home | 1-0 | 100.0 | 49.1 | 50.9 | +0.89 | 88.5 |  |  | redundant -- identical record to pin_move alone, not independent confirmation |
| follow_move+pin_value | tt_home | 2-0 | 100.0 | 49.1 | 50.9 | +1.81 | 90.5 |  |  | keep collecting (2/30) |
| pin_move+pin_value | tt_home | 1-0 | 100.0 | 49.1 | 50.9 | +0.89 | 88.5 |  |  | redundant -- identical record to pin_move alone, not independent confirmation |

## By ticket volume and Pinnacle limit (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| rlm_quiet | close | 40k+ bets | 15-33 | 31.2 | -6.1 | -36.1 |  |
| rlm_quiet | close | pin $10-50k | 7-8 | 46.7 | 3.9 | -11.1 |  |
| rlm_quiet | close | pin $50k+ | 8-25 | 24.2 | -10.6 | -47.4 |  |
| pin_move | close | 40k+ bets | 58-49 | 54.2 | 3.7 | -2.1 |  |
| pin_move | close | pin $10-50k | 25-15 | 62.5 | 11.0 | 14.6 |  |
| pin_move | close | pin $50k+ | 31-34 | 47.7 | -2.2 | -15.1 |  |
| pin_move | close | pin limit <$10k | 2-0 | 100.0 | 50.9 | 86.6 |  |
| money_delta | close | 40k+ bets | 15-31 | 32.6 | -5.1 | -29.9 |  |
| money_delta | close | pin $10-50k | 5-10 | 33.3 | -13.5 | -36.1 |  |
| money_delta | close | pin $50k+ | 10-21 | 32.3 | -1.1 | -26.9 |  |
| pin_rlm | close | 40k+ bets | 5-14 | 26.3 | -5.3 | -47.7 |  |
| pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| pin_rlm | close | pin $50k+ | 2-12 | 14.3 | -13.4 | -69.7 |  |
| pre_move | close | 40k+ bets | 4-11 | 26.7 | -9.4 | -36.1 |  |
| pre_move | close | pin $10-50k | 1-3 | 25.0 | -16.2 | -53.8 |  |
| pre_move | close | pin $50k+ | 3-8 | 27.3 | -6.9 | -29.7 |  |
| follow_move | close | 40k+ bets | 91-84 | 52.0 | 1.3 | -4.2 |  |
| follow_move | close | pin $10-50k | 21-13 | 61.8 | 11.2 | 10.3 |  |
| follow_move | close | pin $50k+ | 43-50 | 46.2 | -4.9 | -14.9 |  |
| follow_move | close | pin limit <$10k | 27-21 | 56.2 | 6.4 | 6.1 |  |
| rlm | close | 40k+ bets | 18-37 | 32.7 | -4.2 | -31.8 |  |
| rlm | close | pin $10-50k | 8-9 | 47.1 | 3.7 | -10.4 |  |
| rlm | close | pin $50k+ | 10-28 | 26.3 | -7.7 | -41.4 |  |
| rlm_ratio | close | 40k+ bets | 6-16 | 27.3 | -6.9 | -41.7 |  |
| rlm_ratio | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| rlm_ratio | close | pin $50k+ | 3-14 | 17.6 | -14.0 | -58.0 |  |
| money_level | close | 40k+ bets | 102-65 | 61.1 | 0.8 | 4.2 |  |
| money_level | close | pin $10-50k | 35-24 | 59.3 | 3.8 | 4.2 |  |
| money_level | close | pin $50k+ | 67-41 | 62.0 | -0.9 | 4.3 |  |
| sharp_gap | close | 40k+ bets | 75-91 | 45.2 | -2.8 | -14.6 |  |
| sharp_gap | close | pin $10-50k | 26-31 | 45.6 | -4.7 | -16.2 |  |
| sharp_gap | close | pin $50k+ | 49-60 | 45.0 | -1.8 | -13.8 |  |
| money_moving | close | 40k+ bets | 58-79 | 42.3 | -4.4 | -20.9 |  |
| money_moving | close | pin $10-50k | 21-28 | 42.9 | -6.9 | -21.8 |  |
| money_moving | close | pin $50k+ | 37-51 | 42.0 | -2.9 | -20.4 |  |
| pin_value | close | 40k+ bets | 73-66 | 52.5 | 4.2 | -1.0 |  |
| pin_value | close | pin $10-50k | 16-15 | 51.6 | 4.2 | -3.3 |  |
| pin_value | close | pin $50k+ | 21-16 | 56.8 | 10.8 | 9.8 |  |
| pin_value | close | pin limit <$10k | 36-35 | 50.7 | 0.7 | -5.6 |  |
| book_lag | close | 40k+ bets | 5-1 | 83.3 | 19.9 | 47.7 |  |
| book_lag | close | pin $50k+ | 5-1 | 83.3 | 19.9 | 47.7 |  |
| consensus_gap | close | 40k+ bets | 22-45 | 32.8 | 2.3 | -24.7 |  |
| consensus_gap | close | pin $10-50k | 1-7 | 12.5 | -17.1 | -83.9 |  |
| consensus_gap | close | pin $50k+ | 21-38 | 35.6 | 5.0 | -16.7 |  |
| follow_move+rlm | close | 40k+ bets | 18-37 | 32.7 | -4.2 | -31.8 |  |
| follow_move+rlm_quiet | close | 40k+ bets | 15-33 | 31.2 | -6.1 | -36.1 |  |
| follow_move+rlm_ratio | close | 40k+ bets | 6-16 | 27.3 | -6.9 | -41.7 |  |
| follow_move+sharp_gap | close | 40k+ bets | 32-38 | 45.7 | -3.3 | -14.2 |  |
| money_level+pin_value | close | 40k+ bets | 20-11 | 64.5 | 10.5 | 20.4 |  |
| rlm+rlm_quiet | close | 40k+ bets | 15-32 | 31.9 | -4.9 | -34.7 |  |
| rlm+rlm_ratio | close | 40k+ bets | 6-16 | 27.3 | -6.9 | -41.7 |  |
| rlm+sharp_gap | close | 40k+ bets | 10-22 | 31.2 | -6.2 | -35.9 |  |
| rlm_quiet+rlm_ratio | close | 40k+ bets | 3-12 | 20.0 | -13.2 | -59.9 |  |
| rlm_quiet+sharp_gap | close | 40k+ bets | 7-17 | 29.2 | -8.3 | -42.9 |  |
| rlm_ratio+sharp_gap | close | 40k+ bets | 6-16 | 27.3 | -6.9 | -41.7 |  |
| money_level+sharp_gap | close | 40k+ bets | 48-38 | 55.8 | -2.0 | -1.6 |  |
| consensus_gap+money_level | close | 40k+ bets | 7-4 | 63.6 | 10.0 | 16.9 |  |
| pre_move+sharp_gap | close | 40k+ bets | 4-11 | 26.7 | -9.4 | -36.1 |  |
| follow_move+money_level | close | 40k+ bets | 41-25 | 62.1 | 0.3 | 5.3 |  |
| book_lag+money_level | close | 40k+ bets | 2-1 | 66.7 | -5.8 | 13.4 |  |
| consensus_gap+pre_move | close | 40k+ bets | 1-5 | 16.7 | -6.1 | -35.0 |  |
| consensus_gap+sharp_gap | close | 40k+ bets | 11-25 | 30.6 | 1.3 | -27.5 |  |
| follow_move+pin_value | close | 40k+ bets | 15-9 | 62.5 | 12.8 | 16.2 |  |
| pin_value+rlm | close | 40k+ bets | 3-6 | 33.3 | -8.2 | -37.6 |  |
| pin_value+rlm_quiet | close | 40k+ bets | 3-6 | 33.3 | -8.2 | -37.6 |  |
| pin_value+pre_move | close | 40k+ bets | 1-2 | 33.3 | 2.3 | -38.4 |  |
| pin_value+sharp_gap | close | 40k+ bets | 20-19 | 51.3 | 5.6 | -5.0 |  |
| consensus_gap+follow_move | close | 40k+ bets | 7-18 | 28.0 | -0.8 | -35.8 |  |
| consensus_gap+rlm | close | 40k+ bets | 5-17 | 22.7 | -1.9 | -43.1 |  |
| consensus_gap+rlm_quiet | close | 40k+ bets | 3-16 | 15.8 | -9.1 | -59.9 |  |
| consensus_gap+pin_value | close | 40k+ bets | 4-12 | 25.0 | -2.1 | -43.6 |  |
| book_lag+consensus_gap | close | 40k+ bets | 3-0 | 100.0 | 45.6 | 82.0 |  |
| book_lag+money_moving | close | 40k+ bets | 1-0 | 100.0 | 63.2 | 78.1 |  |
| book_lag+pin_value | close | 40k+ bets | 2-0 | 100.0 | 50.0 | 80.7 |  |
| consensus_gap+money_moving | close | 40k+ bets | 8-21 | 27.6 | -0.4 | -35.5 |  |
| money_moving+pin_value | close | 40k+ bets | 13-15 | 46.4 | 2.0 | -14.3 |  |
| money_moving+pre_move | close | 40k+ bets | 1-5 | 16.7 | -17.3 | -68.8 |  |
| money_moving+sharp_gap | close | 40k+ bets | 37-53 | 41.1 | -4.3 | -20.4 |  |
| follow_move+money_moving | close | 40k+ bets | 25-36 | 41.0 | -6.7 | -23.4 |  |
| money_moving+rlm | close | 40k+ bets | 8-23 | 25.8 | -9.3 | -46.2 |  |
| money_moving+rlm_quiet | close | 40k+ bets | 5-18 | 21.7 | -12.5 | -57.0 |  |
| money_level+money_moving | close | 40k+ bets | 37-28 | 56.9 | -1.2 | 0.4 |  |
| money_level+pin_move | close | 40k+ bets | 35-18 | 66.0 | 5.0 | 11.0 |  |
| money_moving+pin_move | close | 40k+ bets | 27-29 | 48.2 | 1.0 | -11.4 |  |
| pin_move+pin_value | close | 40k+ bets | 16-16 | 50.0 | 4.9 | -7.0 |  |
| pin_move+sharp_gap | close | 40k+ bets | 29-31 | 48.3 | 1.4 | -9.9 |  |
| consensus_gap+pin_move | close | 40k+ bets | 6-13 | 31.6 | 3.8 | -30.6 |  |
| consensus_gap+money_delta | close | 40k+ bets | 5-7 | 41.7 | 18.9 | 8.7 |  |
| consensus_gap+pin_rlm | close | 40k+ bets | 2-9 | 18.2 | -4.6 | -61.5 |  |
| consensus_gap+rlm_ratio | close | 40k+ bets | 3-7 | 30.0 | 7.2 | -28.6 |  |
| follow_move+money_delta | close | 40k+ bets | 7-14 | 33.3 | -2.9 | -29.2 |  |
| follow_move+pin_rlm | close | 40k+ bets | 5-11 | 31.2 | -2.0 | -38.0 |  |
| money_delta+money_level | close | 40k+ bets | 3-5 | 37.5 | -1.1 | -22.0 |  |
| money_delta+money_moving | close | 40k+ bets | 14-25 | 35.9 | -1.6 | -22.2 |  |
| money_delta+pin_rlm | close | 40k+ bets | 4-10 | 28.6 | -3.4 | -42.4 |  |
| money_delta+rlm | close | 40k+ bets | 6-12 | 33.3 | -2.2 | -28.5 |  |
| money_delta+rlm_ratio | close | 40k+ bets | 5-9 | 35.7 | 2.8 | -21.7 |  |
| money_delta+sharp_gap | close | 40k+ bets | 13-27 | 32.5 | -4.6 | -29.0 |  |
| money_level+pin_rlm | close | 40k+ bets | 0-3 | 0.0 | -40.9 | -100.0 |  |
| money_level+rlm | close | 40k+ bets | 0-3 | 0.0 | -40.9 | -100.0 |  |
| money_level+rlm_ratio | close | 40k+ bets | 0-3 | 0.0 | -40.9 | -100.0 |  |
| money_moving+pin_rlm | close | 40k+ bets | 5-12 | 29.4 | -3.2 | -41.6 |  |
| money_moving+rlm_ratio | close | 40k+ bets | 6-13 | 31.6 | -1.5 | -32.5 |  |
| pin_rlm+rlm | close | 40k+ bets | 5-11 | 31.2 | -2.0 | -38.0 |  |
| pin_rlm+rlm_ratio | close | 40k+ bets | 5-11 | 31.2 | -2.0 | -38.0 |  |
| pin_rlm+sharp_gap | close | 40k+ bets | 5-14 | 26.3 | -5.3 | -47.7 |  |
| follow_move+pin_move | close | 40k+ bets | 49-38 | 56.3 | 4.4 | 0.8 |  |
| pin_move+rlm_quiet | close | 40k+ bets | 13-21 | 38.2 | -1.1 | -21.2 |  |
| money_delta+pin_move | close | 40k+ bets | 7-14 | 33.3 | -4.8 | -34.3 |  |
| money_delta+pin_value | close | 40k+ bets | 1-7 | 12.5 | -25.0 | -77.1 |  |
| money_delta+rlm_quiet | close | 40k+ bets | 3-7 | 30.0 | -4.0 | -39.4 |  |
| pin_move+pin_rlm | close | 40k+ bets | 5-12 | 29.4 | -3.2 | -41.6 |  |
| pin_move+rlm | close | 40k+ bets | 15-23 | 39.5 | 0.2 | -19.2 |  |
| pin_move+rlm_ratio | close | 40k+ bets | 5-9 | 35.7 | 1.0 | -29.1 |  |
| pin_rlm+pin_value | close | 40k+ bets | 1-5 | 16.7 | -14.3 | -68.8 |  |
| pin_rlm+rlm_quiet | close | 40k+ bets | 3-8 | 27.3 | -3.5 | -45.3 |  |
| pin_value+rlm_ratio | close | 40k+ bets | 1-3 | 25.0 | -10.1 | -53.2 |  |
| money_delta+pre_move | close | 40k+ bets | 1-4 | 20.0 | -11.2 | -62.6 |  |
| money_level+pre_move | close | 40k+ bets | 1-1 | 50.0 | 13.2 | -6.5 |  |
| pin_move+pre_move | close | 40k+ bets | 0-2 | 0.0 | -22.8 | -100.0 |  |
| pin_rlm+pre_move | close | 40k+ bets | 0-2 | 0.0 | -22.8 | -100.0 |  |
| money_level+sharp_gap | close | pin $10-50k | 17-14 | 54.8 | 0.2 | -1.1 |  |
| pin_value+pre_move | close | pin $10-50k | 1-0 | 100.0 | 52.6 | 84.7 |  |
| pin_value+sharp_gap | close | pin $10-50k | 9-9 | 50.0 | 2.4 | -6.3 |  |
| pre_move+sharp_gap | close | pin $10-50k | 1-3 | 25.0 | -16.2 | -53.8 |  |
| money_level+pin_value | close | pin $10-50k | 9-4 | 69.2 | 17.0 | 30.2 |  |
| consensus_gap+pin_value | close | pin $10-50k | 0-3 | 0.0 | -22.8 | -100.0 |  |
| follow_move+money_level | close | pin $10-50k | 13-3 | 81.2 | 22.8 | 39.1 |  |
| follow_move+sharp_gap | close | pin $10-50k | 10-9 | 52.6 | 1.8 | -5.6 |  |
| money_moving+pre_move | close | pin $10-50k | 0-2 | 0.0 | -35.1 | -100.0 |  |
| money_moving+sharp_gap | close | pin $10-50k | 12-18 | 40.0 | -9.4 | -25.1 |  |
| consensus_gap+money_level | close | pin $10-50k | 1-0 | 100.0 | 22.8 | 28.6 |  |
| consensus_gap+sharp_gap | close | pin $10-50k | 1-3 | 25.0 | -11.4 | -67.8 |  |
| follow_move+money_moving | close | pin $10-50k | 9-9 | 50.0 | 0.3 | -10.1 |  |
| follow_move+rlm | close | pin $10-50k | 8-9 | 47.1 | 3.7 | -10.4 |  |
| follow_move+rlm_quiet | close | pin $10-50k | 7-8 | 46.7 | 3.9 | -11.1 |  |
| money_moving+rlm | close | pin $10-50k | 4-6 | 40.0 | -3.0 | -24.0 |  |
| money_moving+rlm_quiet | close | pin $10-50k | 3-5 | 37.5 | -4.4 | -28.9 |  |
| rlm+rlm_quiet | close | pin $10-50k | 7-8 | 46.7 | 3.9 | -11.1 |  |
| money_level+money_moving | close | pin $10-50k | 13-10 | 56.5 | 0.7 | 0.3 |  |
| money_level+pin_move | close | pin $10-50k | 15-5 | 75.0 | 18.9 | 34.0 |  |
| money_moving+pin_move | close | pin $10-50k | 14-11 | 56.0 | 4.7 | 2.4 |  |
| money_moving+pin_value | close | pin $10-50k | 5-7 | 41.7 | -6.7 | -21.9 |  |
| pin_move+pin_value | close | pin $10-50k | 9-8 | 52.9 | 4.2 | -0.4 |  |
| pin_move+sharp_gap | close | pin $10-50k | 13-11 | 54.2 | 3.9 | 1.6 |  |
| money_delta+money_level | close | pin $10-50k | 1-0 | 100.0 | 47.4 | 90.9 |  |
| money_delta+money_moving | close | pin $10-50k | 5-8 | 38.5 | -8.2 | -26.2 |  |
| money_delta+sharp_gap | close | pin $10-50k | 4-9 | 30.8 | -15.9 | -41.3 |  |
| follow_move+money_delta | close | pin $10-50k | 3-5 | 37.5 | -6.8 | -28.4 |  |
| follow_move+pin_move | close | pin $10-50k | 20-11 | 64.5 | 13.0 | 17.5 |  |
| follow_move+pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| follow_move+pin_value | close | pin $10-50k | 5-4 | 55.6 | 9.2 | 4.8 |  |
| follow_move+rlm_ratio | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| money_delta+pin_move | close | pin $10-50k | 3-7 | 30.0 | -15.4 | -42.7 |  |
| money_delta+pin_rlm | close | pin $10-50k | 2-2 | 50.0 | 8.8 | -4.5 |  |
| money_delta+pin_value | close | pin $10-50k | 0-5 | 0.0 | -43.5 | -100.0 |  |
| money_delta+rlm | close | pin $10-50k | 3-4 | 42.9 | -1.0 | -18.2 |  |
| money_delta+rlm_quiet | close | pin $10-50k | 2-3 | 40.0 | -2.5 | -23.6 |  |
| money_delta+rlm_ratio | close | pin $10-50k | 2-2 | 50.0 | 8.8 | -4.5 |  |
| money_moving+pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| money_moving+rlm_ratio | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| pin_move+pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| pin_move+rlm | close | pin $10-50k | 8-7 | 53.3 | 7.3 | 1.6 |  |
| pin_move+rlm_quiet | close | pin $10-50k | 7-6 | 53.8 | 8.0 | 2.5 |  |
| pin_move+rlm_ratio | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| pin_rlm+pin_value | close | pin $10-50k | 1-2 | 33.3 | -5.8 | -37.7 |  |
| pin_rlm+rlm | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| pin_rlm+rlm_quiet | close | pin $10-50k | 2-2 | 50.0 | 8.8 | -5.5 |  |
| pin_rlm+rlm_ratio | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| pin_rlm+sharp_gap | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| pin_value+rlm | close | pin $10-50k | 2-4 | 33.3 | -10.8 | -37.6 |  |
| pin_value+rlm_quiet | close | pin $10-50k | 2-4 | 33.3 | -10.8 | -37.6 |  |
| pin_value+rlm_ratio | close | pin $10-50k | 1-2 | 33.3 | -5.8 | -37.7 |  |
| rlm+rlm_ratio | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| rlm+sharp_gap | close | pin $10-50k | 5-5 | 50.0 | 5.1 | -5.3 |  |
| rlm_quiet+rlm_ratio | close | pin $10-50k | 2-2 | 50.0 | 8.8 | -5.5 |  |
| rlm_quiet+sharp_gap | close | pin $10-50k | 4-4 | 50.0 | 5.7 | -5.5 |  |
| rlm_ratio+sharp_gap | close | pin $10-50k | 3-2 | 60.0 | 17.5 | 13.8 |  |
| consensus_gap+follow_move | close | pin $10-50k | 0-2 | 0.0 | -22.8 | -100.0 |  |
| consensus_gap+rlm | close | pin $10-50k | 0-2 | 0.0 | -22.8 | -100.0 |  |
| consensus_gap+rlm_quiet | close | pin $10-50k | 0-2 | 0.0 | -22.8 | -100.0 |  |
| consensus_gap+money_delta | close | pin $10-50k | 0-1 | 0.0 | -22.8 | -100.0 |  |
| consensus_gap+money_moving | close | pin $10-50k | 0-3 | 0.0 | -22.8 | -100.0 |  |
| consensus_gap+pin_move | close | pin $10-50k | 0-1 | 0.0 | -22.8 | -100.0 |  |
| consensus_gap+pin_rlm | close | pin $10-50k | 0-1 | 0.0 | -22.8 | -100.0 |  |
| consensus_gap+rlm_ratio | close | pin $10-50k | 0-1 | 0.0 | -22.8 | -100.0 |  |
| consensus_gap+pre_move | close | pin $10-50k | 0-1 | 0.0 | -22.8 | -100.0 |  |
| follow_move+rlm | close | pin $50k+ | 10-28 | 26.3 | -7.7 | -41.4 |  |
| follow_move+rlm_quiet | close | pin $50k+ | 8-25 | 24.2 | -10.6 | -47.4 |  |
| follow_move+rlm_ratio | close | pin $50k+ | 3-14 | 17.6 | -14.0 | -58.0 |  |
| follow_move+sharp_gap | close | pin $50k+ | 22-29 | 43.1 | -5.2 | -17.4 |  |
| money_level+pin_value | close | pin $50k+ | 11-7 | 61.1 | 5.8 | 13.4 |  |
| rlm+rlm_quiet | close | pin $50k+ | 8-24 | 25.0 | -9.0 | -45.8 |  |
| rlm+rlm_ratio | close | pin $50k+ | 3-14 | 17.6 | -14.0 | -58.0 |  |
| rlm+sharp_gap | close | pin $50k+ | 5-17 | 22.7 | -11.3 | -49.8 |  |
| rlm_quiet+rlm_ratio | close | pin $50k+ | 1-10 | 9.1 | -21.2 | -79.6 |  |
| rlm_quiet+sharp_gap | close | pin $50k+ | 3-13 | 18.8 | -15.2 | -61.6 |  |
| rlm_ratio+sharp_gap | close | pin $50k+ | 3-14 | 17.6 | -14.0 | -58.0 |  |
| consensus_gap+money_level | close | pin $50k+ | 6-4 | 60.0 | 8.8 | 15.7 |  |
| pre_move+sharp_gap | close | pin $50k+ | 3-8 | 27.3 | -6.9 | -29.7 |  |
| follow_move+money_level | close | pin $50k+ | 28-22 | 56.0 | -6.9 | -5.5 |  |
| book_lag+money_level | close | pin $50k+ | 2-1 | 66.7 | -5.8 | 13.4 |  |
| consensus_gap+pre_move | close | pin $50k+ | 1-4 | 20.0 | -2.8 | -22.0 |  |
| consensus_gap+sharp_gap | close | pin $50k+ | 10-22 | 31.2 | 2.9 | -22.5 |  |
| follow_move+pin_value | close | pin $50k+ | 8-5 | 61.5 | 9.4 | 12.6 |  |
| pin_value+rlm | close | pin $50k+ | 1-2 | 33.3 | -2.9 | -37.7 |  |
| pin_value+rlm_quiet | close | pin $50k+ | 1-2 | 33.3 | -2.9 | -37.7 |  |
| money_level+sharp_gap | close | pin $50k+ | 31-24 | 56.4 | -3.2 | -1.9 |  |
| consensus_gap+follow_move | close | pin $50k+ | 7-16 | 30.4 | 1.1 | -30.2 |  |
| consensus_gap+rlm | close | pin $50k+ | 5-15 | 25.0 | 0.2 | -37.4 |  |
| consensus_gap+rlm_quiet | close | pin $50k+ | 3-14 | 17.6 | -7.5 | -55.2 |  |
| consensus_gap+pin_value | close | pin $50k+ | 4-9 | 30.8 | 2.7 | -30.6 |  |
| pin_value+pre_move | close | pin $50k+ | 0-2 | 0.0 | -22.8 | -100.0 |  |
| pin_value+sharp_gap | close | pin $50k+ | 11-10 | 52.4 | 8.3 | -3.9 |  |
| book_lag+consensus_gap | close | pin $50k+ | 3-0 | 100.0 | 45.6 | 82.0 |  |
| book_lag+money_moving | close | pin $50k+ | 1-0 | 100.0 | 63.2 | 78.1 |  |
| book_lag+pin_value | close | pin $50k+ | 2-0 | 100.0 | 50.0 | 80.7 |  |
| consensus_gap+money_moving | close | pin $50k+ | 8-18 | 30.8 | 2.2 | -28.0 |  |
| money_moving+pin_value | close | pin $50k+ | 8-8 | 50.0 | 8.6 | -8.6 |  |
| consensus_gap+pin_move | close | pin $50k+ | 6-12 | 33.3 | 5.3 | -26.7 |  |
| money_moving+pin_move | close | pin $50k+ | 13-18 | 41.9 | -2.0 | -22.6 |  |
| pin_move+pin_value | close | pin $50k+ | 6-8 | 42.9 | 2.4 | -22.0 |  |
| consensus_gap+money_delta | close | pin $50k+ | 5-6 | 45.5 | 22.6 | 18.6 |  |
| consensus_gap+pin_rlm | close | pin $50k+ | 2-8 | 20.0 | -2.8 | -57.6 |  |
| consensus_gap+rlm_ratio | close | pin $50k+ | 3-6 | 33.3 | 10.5 | -20.7 |  |
| follow_move+money_delta | close | pin $50k+ | 4-9 | 30.8 | -0.5 | -29.7 |  |
| follow_move+money_moving | close | pin $50k+ | 16-27 | 37.2 | -9.6 | -29.0 |  |
| follow_move+pin_rlm | close | pin $50k+ | 2-9 | 18.2 | -10.8 | -61.5 |  |
| money_delta+money_level | close | pin $50k+ | 2-5 | 28.6 | -8.0 | -38.1 |  |
| money_delta+money_moving | close | pin $50k+ | 9-17 | 34.6 | 1.8 | -20.2 |  |
| money_delta+pin_rlm | close | pin $50k+ | 2-8 | 20.0 | -8.2 | -57.6 |  |
| money_delta+rlm | close | pin $50k+ | 3-8 | 27.3 | -3.0 | -35.1 |  |
| money_delta+rlm_ratio | close | pin $50k+ | 3-7 | 30.0 | 0.4 | -28.6 |  |
| money_delta+sharp_gap | close | pin $50k+ | 9-18 | 33.3 | 0.8 | -23.1 |  |
| money_level+money_moving | close | pin $50k+ | 24-18 | 57.1 | -2.3 | 0.5 |  |
| money_level+pin_rlm | close | pin $50k+ | 0-3 | 0.0 | -40.9 | -100.0 |  |
| money_level+rlm | close | pin $50k+ | 0-3 | 0.0 | -40.9 | -100.0 |  |
| money_level+rlm_ratio | close | pin $50k+ | 0-3 | 0.0 | -40.9 | -100.0 |  |
| money_moving+pin_rlm | close | pin $50k+ | 2-10 | 16.7 | -11.8 | -64.7 |  |
| money_moving+rlm | close | pin $50k+ | 4-17 | 19.0 | -12.3 | -56.7 |  |
| money_moving+rlm_ratio | close | pin $50k+ | 3-11 | 21.4 | -8.3 | -49.0 |  |
| money_moving+sharp_gap | close | pin $50k+ | 25-35 | 41.7 | -1.8 | -18.0 |  |
| pin_rlm+rlm | close | pin $50k+ | 2-9 | 18.2 | -10.8 | -61.5 |  |
| pin_rlm+rlm_ratio | close | pin $50k+ | 2-9 | 18.2 | -10.8 | -61.5 |  |
| pin_rlm+sharp_gap | close | pin $50k+ | 2-12 | 14.3 | -13.4 | -69.7 |  |
| follow_move+pin_move | close | pin $50k+ | 27-27 | 50.0 | -2.3 | -11.9 |  |
| pin_move+rlm_quiet | close | pin $50k+ | 6-15 | 28.6 | -6.7 | -36.0 |  |
| money_delta+pin_move | close | pin $50k+ | 4-7 | 36.4 | 4.8 | -26.6 |  |
| money_delta+pin_value | close | pin $50k+ | 1-2 | 33.3 | 5.8 | -38.9 |  |
| money_delta+rlm_quiet | close | pin $50k+ | 1-4 | 20.0 | -5.6 | -55.2 |  |
| money_moving+rlm_quiet | close | pin $50k+ | 2-13 | 13.3 | -16.8 | -72.1 |  |
| pin_move+pin_rlm | close | pin $50k+ | 2-10 | 16.7 | -11.8 | -64.7 |  |
| pin_move+rlm | close | pin $50k+ | 7-16 | 30.4 | -4.3 | -32.8 |  |
| pin_move+rlm_ratio | close | pin $50k+ | 2-7 | 22.2 | -8.2 | -52.9 |  |
| pin_move+sharp_gap | close | pin $50k+ | 16-20 | 44.4 | -0.3 | -17.6 |  |
| pin_rlm+pin_value | close | pin $50k+ | 0-3 | 0.0 | -22.8 | -100.0 |  |
| pin_rlm+rlm_quiet | close | pin $50k+ | 1-6 | 14.3 | -10.5 | -68.0 |  |
| pin_value+rlm_ratio | close | pin $50k+ | 0-1 | 0.0 | -22.8 | -100.0 |  |
| money_delta+pre_move | close | pin $50k+ | 1-4 | 20.0 | -11.2 | -62.6 |  |
| money_level+pre_move | close | pin $50k+ | 1-1 | 50.0 | 13.2 | -6.5 |  |
| money_moving+pre_move | close | pin $50k+ | 1-3 | 25.0 | -8.3 | -53.2 |  |
| money_level+pin_move | close | pin $50k+ | 20-13 | 60.6 | -3.5 | -2.9 |  |
| pin_move+pre_move | close | pin $50k+ | 0-2 | 0.0 | -22.8 | -100.0 |  |
| pin_rlm+pre_move | close | pin $50k+ | 0-2 | 0.0 | -22.8 | -100.0 |  |
| follow_move+pin_move | close | pin limit <$10k | 2-0 | 100.0 | 50.9 | 86.6 |  |
| follow_move+pin_value | close | pin limit <$10k | 2-0 | 100.0 | 50.9 | 90.5 |  |
| pin_move+pin_value | close | pin limit <$10k | 1-0 | 100.0 | 50.9 | 88.5 |  |
| rlm_quiet | early | 40k+ bets | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| rlm_quiet | early | <10k bets | 3-7 | 30.0 | -16.0 | -43.3 | 0.05 |
| rlm_quiet | early | pin $10-50k | 3-3 | 50.0 | 4.4 | -5.6 | 0.17 |
| rlm_quiet | early | pin $50k+ | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| rlm_quiet | early | pin limit <$10k | 0-3 | 0.0 | -49.7 | -100.0 | -0.17 |
| pin_move | early | <10k bets | 22-21 | 51.2 | -8.8 | -14.6 | 0.72 |
| pin_move | early | pin $10-50k | 3-3 | 50.0 | 2.3 | -4.5 | 0.17 |
| pin_move | early | pin limit <$10k | 19-18 | 51.4 | -10.6 | -16.3 | 0.81 |
| pin_rlm | early | <10k bets | 2-7 | 22.2 | -3.3 | -55.2 | -0.86 |
| pin_rlm | early | pin $10-50k | 1-2 | 33.3 | 10.5 | -30.7 | -0.93 |
| pin_rlm | early | pin limit <$10k | 1-5 | 16.7 | -10.2 | -67.5 | -0.82 |
| pre_move | early | 10-40k bets | 1-1 | 50.0 | 27.2 | 23.0 | 0.55 |
| pre_move | early | 40k+ bets | 0-1 | 0.0 | -47.4 | -100.0 | 0.0 |
| pre_move | early | <10k bets | 12-26 | 31.6 | -0.9 | -31.6 | -0.45 |
| pre_move | early | pin $10-50k | 2-5 | 28.6 | -5.5 | -35.1 | -0.47 |
| pre_move | early | pin $50k+ | 0-1 | 0.0 | -22.8 | -100.0 | 2.1 |
| pre_move | early | pin limit <$10k | 9-19 | 32.1 | 0.8 | -30.0 | -0.2 |
| follow_move | early | 10-40k bets | 1-0 | 100.0 | 36.8 | 82.0 | 0.0 |
| follow_move | early | 40k+ bets | 1-1 | 50.0 | 13.2 | -8.4 | 0.0 |
| follow_move | early | <10k bets | 16-19 | 45.7 | -7.4 | -13.0 | -0.22 |
| follow_move | early | pin $10-50k | 10-8 | 55.6 | 4.1 | 5.7 | 0.08 |
| follow_move | early | pin $50k+ | 2-1 | 66.7 | 21.1 | 21.8 | 0.0 |
| follow_move | early | pin limit <$10k | 5-8 | 38.5 | -19.8 | -27.6 | -0.43 |
| rlm | early | 40k+ bets | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| rlm | early | <10k bets | 2-7 | 22.2 | -21.8 | -57.4 | 0.06 |
| rlm | early | pin $10-50k | 2-3 | 40.0 | -2.1 | -23.3 | 0.2 |
| rlm | early | pin $50k+ | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| rlm | early | pin limit <$10k | 0-3 | 0.0 | -49.7 | -100.0 | -0.17 |
| rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| rlm_ratio | early | <10k bets | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm_ratio | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| money_level | early | 10-40k bets | 3-3 | 50.0 | -9.1 | -13.8 | -0.28 |
| money_level | early | 40k+ bets | 4-4 | 50.0 | -13.8 | -19.9 | -0.06 |
| money_level | early | <10k bets | 88-43 | 67.2 | 7.0 | 15.4 | -0.18 |
| money_level | early | pin $10-50k | 21-17 | 55.3 | -2.3 | 1.8 | -0.03 |
| money_level | early | pin $50k+ | 5-2 | 71.4 | 6.0 | 20.1 | -0.36 |
| money_level | early | pin limit <$10k | 62-26 | 70.5 | 9.5 | 17.1 | -0.24 |
| sharp_gap | early | 10-40k bets | 3-3 | 50.0 | 3.8 | 3.1 | 0.27 |
| sharp_gap | early | 40k+ bets | 4-5 | 44.4 | -13.5 | -29.5 | -0.06 |
| sharp_gap | early | <10k bets | 70-54 | 56.5 | 9.0 | 7.2 | -0.04 |
| sharp_gap | early | pin $10-50k | 21-15 | 58.3 | 7.5 | 10.5 | -0.03 |
| sharp_gap | early | pin $50k+ | 3-5 | 37.5 | -17.5 | -37.5 | 0.33 |
| sharp_gap | early | pin limit <$10k | 46-37 | 55.4 | 9.1 | 4.3 | -0.06 |
| money_moving | early | <10k bets | 15-9 | 62.5 | 10.4 | 14.1 | -0.03 |
| money_moving | early | pin $10-50k | 5-2 | 71.4 | 21.6 | 40.0 | -0.16 |
| money_moving | early | pin limit <$10k | 9-6 | 60.0 | 5.5 | 4.2 | 0.16 |
| pin_value | early | 10-40k bets | 1-2 | 33.3 | -21.1 | -39.3 | 0.0 |
| pin_value | early | 40k+ bets | 4-2 | 66.7 | 20.5 | 22.5 | 0.0 |
| pin_value | early | <10k bets | 38-34 | 52.8 | 4.0 | -1.0 | 0.21 |
| pin_value | early | pin $10-50k | 11-4 | 73.3 | 12.6 | 39.3 | 0.03 |
| pin_value | early | pin $50k+ | 3-0 | 100.0 | 54.4 | 81.1 | 0.0 |
| pin_value | early | pin limit <$10k | 29-34 | 46.0 | -0.0 | -14.1 | 0.23 |
| book_lag | early | <10k bets | 5-3 | 62.5 | 16.0 | 19.3 | -0.14 |
| book_lag | early | pin $10-50k | 2-2 | 50.0 | 3.5 | -1.2 | 0.6 |
| book_lag | early | pin limit <$10k | 2-1 | 66.7 | 12.3 | 8.5 | -0.37 |
| consensus_gap | early | 10-40k bets | 2-2 | 50.0 | 7.0 | 7.0 | 0.4 |
| consensus_gap | early | 40k+ bets | 2-2 | 50.0 | 23.7 | -6.4 | 0.17 |
| consensus_gap | early | <10k bets | 21-39 | 35.0 | 2.3 | -23.0 | 0.01 |
| consensus_gap | early | pin $10-50k | 8-9 | 47.1 | 5.2 | -2.3 | 0.22 |
| consensus_gap | early | pin $50k+ | 3-3 | 50.0 | 11.4 | -7.3 | 0.43 |
| consensus_gap | early | pin limit <$10k | 11-29 | 27.5 | -1.1 | -37.4 | -0.19 |
| consensus_gap+follow_move | early | 10-40k bets | 1-0 | 100.0 | 36.8 | 82.0 | 0.0 |
| consensus_gap+money_level | early | 10-40k bets | 1-0 | 100.0 | 36.8 | 82.0 | 0.0 |
| consensus_gap+pin_value | early | 10-40k bets | 1-0 | 100.0 | 36.8 | 82.0 | 0.0 |
| consensus_gap+sharp_gap | early | 10-40k bets | 2-2 | 50.0 | 7.0 | 7.0 | 0.4 |
| follow_move+money_level | early | 10-40k bets | 1-0 | 100.0 | 36.8 | 82.0 | 0.0 |
| follow_move+pin_value | early | 10-40k bets | 1-0 | 100.0 | 36.8 | 82.0 | 0.0 |
| follow_move+sharp_gap | early | 10-40k bets | 1-0 | 100.0 | 36.8 | 82.0 | 0.0 |
| money_level+pin_value | early | 10-40k bets | 1-0 | 100.0 | 36.8 | 82.0 | 0.0 |
| money_level+sharp_gap | early | 10-40k bets | 1-1 | 50.0 | -7.9 | -9.0 | 0.0 |
| pin_value+sharp_gap | early | 10-40k bets | 1-0 | 100.0 | 36.8 | 82.0 | 0.0 |
| consensus_gap+pre_move | early | 10-40k bets | 1-1 | 50.0 | 27.2 | 23.0 | 0.55 |
| pre_move+sharp_gap | early | 10-40k bets | 1-1 | 50.0 | 27.2 | 23.0 | 0.55 |
| follow_move+rlm | early | 40k+ bets | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| follow_move+rlm_quiet | early | 40k+ bets | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | 40k+ bets | 1-1 | 50.0 | 13.2 | -8.4 | 0.0 |
| rlm+rlm_quiet | early | 40k+ bets | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| rlm+rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| rlm+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| rlm_quiet+rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| rlm_quiet+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| rlm_ratio+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| money_level+pin_value | early | 40k+ bets | 0-1 | 0.0 | -52.6 | -100.0 | 0.0 |
| money_level+sharp_gap | early | 40k+ bets | 3-4 | 42.9 | -21.1 | -35.5 | -0.07 |
| pin_value+sharp_gap | early | 40k+ bets | 1-1 | 50.0 | 5.3 | -8.4 | 0.0 |
| consensus_gap+pin_value | early | 40k+ bets | 1-0 | 100.0 | 63.2 | 78.1 | 0.0 |
| money_level+pre_move | early | 40k+ bets | 0-1 | 0.0 | -47.4 | -100.0 | 0.0 |
| pre_move+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -47.4 | -100.0 | 0.0 |
| follow_move+pin_value | early | 40k+ bets | 1-0 | 100.0 | 63.2 | 83.3 | 0.0 |
| follow_move+money_level | early | <10k bets | 12-9 | 57.1 | -1.2 | 9.1 | -0.22 |
| follow_move+money_moving | early | <10k bets | 3-2 | 60.0 | -0.7 | 7.5 | -0.62 |
| follow_move+pin_value | early | <10k bets | 4-2 | 66.7 | 3.5 | 25.9 | 0.33 |
| follow_move+sharp_gap | early | <10k bets | 11-7 | 61.1 | 5.3 | 18.6 | 0.08 |
| money_level+money_moving | early | <10k bets | 10-3 | 76.9 | 17.1 | 35.1 | -0.47 |
| money_level+pin_value | early | <10k bets | 14-5 | 73.7 | 16.3 | 39.4 | 0.18 |
| money_level+sharp_gap | early | <10k bets | 51-21 | 70.8 | 14.2 | 28.9 | -0.18 |
| money_moving+pin_value | early | <10k bets | 5-2 | 71.4 | 23.8 | 36.6 | 1.0 |
| money_moving+sharp_gap | early | <10k bets | 7-3 | 70.0 | 20.4 | 31.5 | 0.03 |
| pin_value+sharp_gap | early | <10k bets | 15-10 | 60.0 | 13.5 | 13.4 | 0.68 |
| consensus_gap+follow_move | early | <10k bets | 1-2 | 33.3 | -16.4 | -38.9 | 0.5 |
| consensus_gap+rlm | early | <10k bets | 0-1 | 0.0 | -22.8 | -100.0 | 0.5 |
| consensus_gap+rlm_quiet | early | <10k bets | 0-1 | 0.0 | -22.8 | -100.0 | 0.5 |
| follow_move+rlm | early | <10k bets | 2-7 | 22.2 | -21.8 | -57.4 | 0.06 |
| follow_move+rlm_quiet | early | <10k bets | 3-7 | 30.0 | -16.0 | -43.3 | 0.05 |
| rlm+rlm_quiet | early | <10k bets | 2-7 | 22.2 | -21.8 | -57.4 | 0.06 |
| pin_move+pin_value | early | <10k bets | 4-5 | 44.4 | -13.5 | -16.5 | 0.78 |
| consensus_gap+pin_move | early | <10k bets | 1-4 | 20.0 | -18.9 | -62.6 | 0.12 |
| consensus_gap+sharp_gap | early | <10k bets | 15-23 | 39.5 | 7.1 | -17.0 | 0.02 |
| pin_move+sharp_gap | early | <10k bets | 13-6 | 68.4 | 11.5 | 25.3 | 0.66 |
| consensus_gap+money_level | early | <10k bets | 10-3 | 76.9 | 19.8 | 37.5 | -0.38 |
| book_lag+consensus_gap | early | <10k bets | 3-2 | 60.0 | 26.3 | 25.8 | 0.68 |
| money_level+pre_move | early | <10k bets | 2-3 | 40.0 | 0.7 | -24.4 | -1.92 |
| pre_move+sharp_gap | early | <10k bets | 12-26 | 31.6 | -0.9 | -31.6 | -0.45 |
| consensus_gap+pin_value | early | <10k bets | 4-12 | 25.0 | -14.7 | -53.5 | 0.91 |
| money_level+pin_move | early | <10k bets | 20-7 | 74.1 | 7.9 | 21.8 | 0.86 |
| money_moving+pin_move | early | <10k bets | 1-0 | 100.0 | 63.2 | 95.2 | -2.0 |
| consensus_gap+pin_rlm | early | <10k bets | 1-7 | 12.5 | -10.3 | -74.0 | -1.09 |
| consensus_gap+pre_move | early | <10k bets | 5-18 | 21.7 | -1.1 | -45.0 | -0.68 |
| money_level+pin_rlm | early | <10k bets | 0-1 | 0.0 | -22.8 | -100.0 | -10.6 |
| pin_rlm+pre_move | early | <10k bets | 2-7 | 22.2 | -3.3 | -55.2 | -0.86 |
| pin_rlm+sharp_gap | early | <10k bets | 2-7 | 22.2 | -3.3 | -55.2 | -0.86 |
| book_lag+money_level | early | <10k bets | 3-1 | 75.0 | 8.3 | 28.1 | -0.88 |
| book_lag+money_moving | early | <10k bets | 1-1 | 50.0 | 7.0 | 4.0 | -0.05 |
| book_lag+sharp_gap | early | <10k bets | 4-1 | 80.0 | 33.0 | 63.2 | 0.1 |
| money_moving+rlm_quiet | early | <10k bets | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| pin_value+rlm_quiet | early | <10k bets | 1-0 | 100.0 | 36.8 | 83.3 | 0.0 |
| pin_value+pre_move | early | <10k bets | 2-6 | 25.0 | -3.9 | -53.2 | 1.55 |
| consensus_gap+money_moving | early | <10k bets | 2-1 | 66.7 | 39.2 | 31.7 | 2.63 |
| money_moving+pre_move | early | <10k bets | 2-1 | 66.7 | 35.7 | 34.4 | 1.63 |
| pin_rlm+pin_value | early | <10k bets | 0-2 | 0.0 | -22.8 | -100.0 | 0.9 |
| book_lag+pin_rlm | early | <10k bets | 1-0 | 100.0 | 77.2 | 108.0 | 1.9 |
| book_lag+pre_move | early | <10k bets | 2-0 | 100.0 | 77.2 | 121.0 | -0.25 |
| money_moving+pin_rlm | early | <10k bets | 1-0 | 100.0 | 77.2 | 108.0 | 1.9 |
| follow_move+rlm_ratio | early | <10k bets | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm+rlm_ratio | early | <10k bets | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm+sharp_gap | early | <10k bets | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm_quiet+rlm_ratio | early | <10k bets | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm_quiet+sharp_gap | early | <10k bets | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm_ratio+sharp_gap | early | <10k bets | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| follow_move+pin_move | early | <10k bets | 3-6 | 33.3 | -26.9 | -35.4 | -0.22 |
| money_moving+rlm | early | <10k bets | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| pin_move+rlm | early | <10k bets | 0-2 | 0.0 | -63.2 | -100.0 | -0.5 |
| pin_move+rlm_quiet | early | <10k bets | 0-2 | 0.0 | -63.2 | -100.0 | -0.5 |
| pin_move+pin_rlm | early | <10k bets | 1-2 | 33.3 | 2.3 | -34.9 | 0.67 |
| pin_move+pre_move | early | <10k bets | 1-2 | 33.3 | 2.3 | -34.9 | 0.67 |
| book_lag+pin_move | early | <10k bets | 3-0 | 100.0 | 32.2 | 70.8 | -0.5 |
| book_lag+pin_value | early | <10k bets | 2-0 | 100.0 | 36.8 | 87.0 | 1.5 |
| money_level+pin_value | early | pin $10-50k | 8-2 | 80.0 | 17.9 | 52.0 | 0.15 |
| money_level+sharp_gap | early | pin $10-50k | 15-9 | 62.5 | 6.7 | 15.4 | -0.04 |
| pin_value+sharp_gap | early | pin $10-50k | 6-1 | 85.7 | 24.1 | 63.7 | 0.21 |
| money_level+pre_move | early | pin $10-50k | 0-2 | 0.0 | -42.1 | -100.0 | 0.0 |
| pre_move+sharp_gap | early | pin $10-50k | 2-5 | 28.6 | -5.5 | -35.1 | -0.47 |
| consensus_gap+pre_move | early | pin $10-50k | 2-2 | 50.0 | 27.2 | 13.5 | -0.95 |
| consensus_gap+sharp_gap | early | pin $10-50k | 5-2 | 71.4 | 31.3 | 44.5 | -0.33 |
| follow_move+money_level | early | pin $10-50k | 6-4 | 60.0 | 4.7 | 15.0 | 0.3 |
| follow_move+money_moving | early | pin $10-50k | 2-0 | 100.0 | 36.8 | 90.6 | 0.0 |
| follow_move+pin_value | early | pin $10-50k | 4-0 | 100.0 | 36.8 | 88.9 | 0.25 |
| follow_move+sharp_gap | early | pin $10-50k | 6-3 | 66.7 | 12.3 | 27.7 | 0.33 |
| money_level+money_moving | early | pin $10-50k | 2-1 | 66.7 | 12.3 | 31.1 | -1.33 |
| money_moving+pin_value | early | pin $10-50k | 3-1 | 75.0 | 18.4 | 44.1 | 0.25 |
| money_moving+sharp_gap | early | pin $10-50k | 2-1 | 66.7 | 17.0 | 35.3 | -0.03 |
| book_lag+consensus_gap | early | pin $10-50k | 1-1 | 50.0 | 20.2 | 4.0 | 1.2 |
| money_level+pin_move | early | pin $10-50k | 3-2 | 60.0 | 7.4 | 14.6 | 0.2 |
| money_moving+pin_move | early | pin $10-50k | 1-0 | 100.0 | 63.2 | 95.2 | -2.0 |
| follow_move+rlm | early | pin $10-50k | 2-3 | 40.0 | -2.1 | -23.3 | 0.2 |
| follow_move+rlm_quiet | early | pin $10-50k | 3-3 | 50.0 | 4.4 | -5.6 | 0.17 |
| rlm+rlm_quiet | early | pin $10-50k | 2-3 | 40.0 | -2.1 | -23.3 | 0.2 |
| book_lag+money_level | early | pin $10-50k | 1-1 | 50.0 | -13.2 | -6.5 | 0.0 |
| book_lag+money_moving | early | pin $10-50k | 1-1 | 50.0 | 7.0 | 4.0 | -0.05 |
| book_lag+sharp_gap | early | pin $10-50k | 2-1 | 66.7 | 17.0 | 31.7 | 0.63 |
| money_moving+rlm_quiet | early | pin $10-50k | 1-0 | 100.0 | 36.8 | 83.3 | 0.0 |
| pin_value+rlm_quiet | early | pin $10-50k | 1-0 | 100.0 | 36.8 | 83.3 | 0.0 |
| consensus_gap+money_level | early | pin $10-50k | 4-1 | 80.0 | 16.8 | 48.1 | 0.3 |
| consensus_gap+pin_value | early | pin $10-50k | 2-2 | 50.0 | -13.2 | -7.4 | 0.0 |
| book_lag+pin_rlm | early | pin $10-50k | 1-0 | 100.0 | 77.2 | 108.0 | 1.9 |
| book_lag+pre_move | early | pin $10-50k | 1-0 | 100.0 | 77.2 | 108.0 | 1.9 |
| consensus_gap+money_moving | early | pin $10-50k | 1-0 | 100.0 | 77.2 | 108.0 | 1.9 |
| consensus_gap+pin_rlm | early | pin $10-50k | 1-2 | 33.3 | 10.5 | -30.7 | -0.93 |
| money_moving+pin_rlm | early | pin $10-50k | 1-0 | 100.0 | 77.2 | 108.0 | 1.9 |
| money_moving+pre_move | early | pin $10-50k | 1-0 | 100.0 | 77.2 | 108.0 | 1.9 |
| pin_rlm+pre_move | early | pin $10-50k | 1-2 | 33.3 | 10.5 | -30.7 | -0.93 |
| pin_rlm+sharp_gap | early | pin $10-50k | 1-2 | 33.3 | 10.5 | -30.7 | -0.93 |
| follow_move+rlm_ratio | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm+rlm_ratio | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm+sharp_gap | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm_quiet+rlm_ratio | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm_quiet+sharp_gap | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.0 |
| follow_move+pin_move | early | pin $10-50k | 1-2 | 33.3 | -21.1 | -36.4 | 0.33 |
| pin_move+pin_value | early | pin $10-50k | 2-0 | 100.0 | 36.8 | 88.9 | 1.5 |
| pin_move+sharp_gap | early | pin $10-50k | 2-1 | 66.7 | 17.0 | 26.0 | 1.0 |
| consensus_gap+follow_move | early | pin $10-50k | 1-0 | 100.0 | 36.8 | 83.3 | 0.0 |
| book_lag+pin_move | early | pin $10-50k | 1-0 | 100.0 | 36.8 | 87.0 | 2.0 |
| book_lag+pin_value | early | pin $10-50k | 1-0 | 100.0 | 36.8 | 87.0 | 2.0 |
| consensus_gap+pin_move | early | pin $10-50k | 0-1 | 0.0 | -22.8 | -100.0 | 0.0 |
| pin_move+pin_rlm | early | pin $10-50k | 0-1 | 0.0 | -22.8 | -100.0 | 0.0 |
| pin_move+pre_move | early | pin $10-50k | 0-1 | 0.0 | -22.8 | -100.0 | 0.0 |
| follow_move+rlm | early | pin $50k+ | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| follow_move+rlm_quiet | early | pin $50k+ | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | pin $50k+ | 2-1 | 66.7 | 21.1 | 21.8 | 0.0 |
| rlm+rlm_quiet | early | pin $50k+ | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| rlm+rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| rlm+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| rlm_quiet+rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| rlm_quiet+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -36.8 | -100.0 | 0.0 |
| money_level+sharp_gap | early | pin $50k+ | 2-2 | 50.0 | -20.2 | -20.9 | 0.0 |
| consensus_gap+pin_value | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 80.0 | 0.0 |
| follow_move+pin_value | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 82.7 | 0.0 |
| pin_value+sharp_gap | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 82.7 | 0.0 |
| consensus_gap+follow_move | early | pin $50k+ | 1-0 | 100.0 | 36.8 | 82.0 | 0.0 |
| consensus_gap+money_level | early | pin $50k+ | 1-0 | 100.0 | 36.8 | 82.0 | 0.0 |
| consensus_gap+sharp_gap | early | pin $50k+ | 1-2 | 33.3 | -16.4 | -39.3 | 0.87 |
| follow_move+money_level | early | pin $50k+ | 1-0 | 100.0 | 36.8 | 82.0 | 0.0 |
| money_level+pin_value | early | pin $50k+ | 1-0 | 100.0 | 36.8 | 82.0 | 0.0 |
| consensus_gap+pre_move | early | pin $50k+ | 0-1 | 0.0 | -22.8 | -100.0 | 2.1 |
| pre_move+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -22.8 | -100.0 | 2.1 |
| money_level+pin_value | early | pin limit <$10k | 6-4 | 60.0 | 7.9 | 12.8 | 0.2 |
| money_level+sharp_gap | early | pin limit <$10k | 34-13 | 72.3 | 15.6 | 30.3 | -0.25 |
| pin_value+sharp_gap | early | pin limit <$10k | 9-10 | 47.4 | 6.1 | -11.1 | 0.81 |
| consensus_gap+follow_move | early | pin limit <$10k | 0-2 | 0.0 | -43.0 | -100.0 | 0.75 |
| consensus_gap+rlm | early | pin limit <$10k | 0-1 | 0.0 | -22.8 | -100.0 | 0.5 |
| consensus_gap+rlm_quiet | early | pin limit <$10k | 0-1 | 0.0 | -22.8 | -100.0 | 0.5 |
| follow_move+rlm | early | pin limit <$10k | 0-3 | 0.0 | -49.7 | -100.0 | -0.17 |
| follow_move+rlm_quiet | early | pin limit <$10k | 0-3 | 0.0 | -49.7 | -100.0 | -0.17 |
| rlm+rlm_quiet | early | pin limit <$10k | 0-3 | 0.0 | -49.7 | -100.0 | -0.17 |
| pin_move+pin_value | early | pin limit <$10k | 2-5 | 28.6 | -27.8 | -46.6 | 0.57 |
| consensus_gap+pin_move | early | pin limit <$10k | 1-3 | 25.0 | -18.0 | -53.2 | 0.15 |
| consensus_gap+sharp_gap | early | pin limit <$10k | 8-20 | 28.6 | -1.5 | -39.8 | -0.11 |
| money_level+money_moving | early | pin limit <$10k | 8-2 | 80.0 | 18.6 | 36.3 | -0.21 |
| pin_move+sharp_gap | early | pin limit <$10k | 11-5 | 68.8 | 10.5 | 25.2 | 0.6 |
| follow_move+money_level | early | pin limit <$10k | 5-4 | 55.6 | -8.0 | 4.6 | -0.57 |
| follow_move+money_moving | early | pin limit <$10k | 1-1 | 50.0 | -20.2 | -21.9 | -1.55 |
| consensus_gap+money_level | early | pin limit <$10k | 5-2 | 71.4 | 19.5 | 23.4 | -1.06 |
| money_level+pre_move | early | pin limit <$10k | 2-2 | 50.0 | 10.1 | -5.5 | -2.4 |
| pre_move+sharp_gap | early | pin limit <$10k | 9-19 | 32.1 | 0.8 | -30.0 | -0.2 |
| consensus_gap+pin_value | early | pin limit <$10k | 2-10 | 16.7 | -15.2 | -68.8 | 1.21 |
| money_moving+sharp_gap | early | pin limit <$10k | 4-2 | 66.7 | 16.7 | 19.0 | 0.4 |
| consensus_gap+pin_rlm | early | pin limit <$10k | 0-5 | 0.0 | -22.8 | -100.0 | -1.18 |
| consensus_gap+pre_move | early | pin limit <$10k | 3-15 | 16.7 | -6.1 | -54.3 | -0.42 |
| money_level+pin_rlm | early | pin limit <$10k | 0-1 | 0.0 | -22.8 | -100.0 | -10.6 |
| pin_rlm+pre_move | early | pin limit <$10k | 1-5 | 16.7 | -10.2 | -67.5 | -0.82 |
| pin_rlm+sharp_gap | early | pin limit <$10k | 1-5 | 16.7 | -10.2 | -67.5 | -0.82 |
| money_moving+pin_value | early | pin limit <$10k | 2-1 | 66.7 | 31.0 | 26.5 | 2.0 |
| pin_value+pre_move | early | pin limit <$10k | 2-6 | 25.0 | -3.9 | -53.2 | 1.55 |
| consensus_gap+money_moving | early | pin limit <$10k | 1-1 | 50.0 | 20.2 | -6.5 | 3.0 |
| money_moving+pre_move | early | pin limit <$10k | 0-1 | 0.0 | -22.8 | -100.0 | 5.0 |
| follow_move+sharp_gap | early | pin limit <$10k | 4-3 | 57.1 | -2.3 | 12.2 | 0.14 |
| pin_rlm+pin_value | early | pin limit <$10k | 0-2 | 0.0 | -22.8 | -100.0 | 0.9 |
| money_level+pin_move | early | pin limit <$10k | 17-5 | 77.3 | 8.0 | 23.4 | 1.01 |
| book_lag+consensus_gap | early | pin limit <$10k | 1-1 | 50.0 | 7.0 | -6.5 | 1.7 |
| follow_move+pin_move | early | pin limit <$10k | 2-4 | 33.3 | -29.8 | -34.9 | -0.5 |
| follow_move+pin_value | early | pin limit <$10k | 0-2 | 0.0 | -63.2 | -100.0 | 0.5 |
| pin_move+rlm | early | pin limit <$10k | 0-2 | 0.0 | -63.2 | -100.0 | -0.5 |
| pin_move+rlm_quiet | early | pin limit <$10k | 0-2 | 0.0 | -63.2 | -100.0 | -0.5 |
| pin_move+pin_rlm | early | pin limit <$10k | 1-1 | 50.0 | 14.9 | -2.4 | 1.0 |
| pin_move+pre_move | early | pin limit <$10k | 1-1 | 50.0 | 14.9 | -2.4 | 1.0 |
| book_lag+money_level | early | pin limit <$10k | 2-0 | 100.0 | 29.8 | 62.7 | -1.75 |
| book_lag+pin_move | early | pin limit <$10k | 2-0 | 100.0 | 29.8 | 62.7 | -1.75 |
| book_lag+pin_value | early | pin limit <$10k | 1-0 | 100.0 | 36.8 | 87.0 | 1.0 |
| book_lag+sharp_gap | early | pin limit <$10k | 1-0 | 100.0 | 36.8 | 87.0 | 1.0 |
