# CBB scorecard

Generated 2026-11-23 13:42 UTC. 806 graded games (22 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**684 games before 2026-11-21 (fit) · 122 on or after it (forward).**

Every signal, threshold and PROMOTE/DROP label here was chosen while looking at
the games before 2026-11-21. `pin_value` went 108-68 in first halves --
fitted and scored on the same 176 games, never tested on one it did not help
choose. So every record appears twice:

- **FIT** — in-sample. A label here is a **hypothesis**.
- **FORWARD** — out-of-sample. A label here is **evidence**.

Base rates are measured separately in each period, so the forward test is not
scored against the fit window's own favourite rate.

The board weights a signal by its FIT edge until it has
30 decided forward outcomes, then by its FORWARD edge. Changing any
threshold moves the holdout date and restarts the forward test.

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before tip. Break-even at -110 is 52.4%. CLV = points of closing-line
value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured
on this sample. `edge` is hit% minus that. A signal that is structurally long
favourites or overs beats 50% whenever those run, which is not an edge -- this
sample ran **46.8% favourites** (n=805) and **51.1% overs** (n=806) and **71.8% moneyline favourites** (n=692).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-21. Nothing in the engine was chosen using these. n=122 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 8-12 | 40.0 | 38.4 | 1.6 | -2.19 | -11.0 | 0.33 | 40.0 | keep collecting (20/30) |
| pin_move | both | 4-4 | 50.0 | 50.0 | 0.0 | -0.36 | -4.6 | -0.25 | 12.5 | keep collecting (8/30) |
| money_delta | both | 1-1 | 50.0 | 41.0 | 9.0 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| pin_rlm | both | 0-1 | 0.0 | 63.6 | -63.6 | -1.0 | -100.0 | 1.5 | 100.0 | keep collecting (1/30) |
| follow_move | both | 80-97 | 45.2 | 48.3 | -3.1 | -21.0 | -11.9 | 0.17 | 36.7 | DROP: below break-even |
| rlm_ratio | both | 5-7 | 41.7 | 42.8 | -1.2 | -1.6 | -13.4 | 0.82 | 58.3 | keep collecting (12/30) |
| money_level | both | 21-20 | 51.2 | 59.3 | -8.1 | -7.12 | -17.4 | 0.01 | 39.0 | no edge shown yet |
| sharp_gap | both | 15-19 | 44.1 | 47.2 | -3.1 | -4.38 | -12.9 | 0.33 | 47.1 | no edge shown yet |
| money_moving | both | 18-16 | 52.9 | 49.6 | 3.3 | -0.12 | -0.3 | 0.61 | 50.0 | no edge shown yet |
| pin_value | both | 10-9 | 52.6 | 48.8 | 3.8 | -0.14 | -0.7 | -0.28 | 26.3 | keep collecting (19/30) |
| consensus_gap | both | 54-41 | 56.8 | 50.5 | 6.3 | +4.67 | 4.9 | 0.33 | 47.4 | no edge shown yet |
| follow_move+money_level | both | 5-8 | 38.5 | 58.4 | -19.9 | -5.49 | -42.2 | 0.39 | 38.5 | keep collecting (13/30) |
| follow_move+sharp_gap | both | 6-10 | 37.5 | 45.8 | -8.3 | -3.69 | -23.1 | 0.68 | 50.0 | keep collecting (16/30) |
| money_level+sharp_gap | both | 7-10 | 41.2 | 55.9 | -14.7 | -4.57 | -26.9 | 0.31 | 52.9 | keep collecting (17/30) |
| follow_move+money_moving | both | 9-9 | 50.0 | 48.0 | 2.0 | -1.23 | -6.8 | 0.79 | 50.0 | keep collecting (18/30) |
| money_level+money_moving | both | 9-9 | 50.0 | 57.8 | -7.8 | -3.28 | -18.2 | 0.48 | 44.4 | keep collecting (18/30) |
| consensus_gap+money_level | both | 8-5 | 61.5 | 57.0 | 4.6 | -1.01 | -7.8 | -0.32 | 38.5 | keep collecting (13/30) |
| follow_move+rlm_quiet | both | 8-12 | 40.0 | 38.4 | 1.6 | -2.19 | -11.0 | 0.33 | 40.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 5-7 | 41.7 | 42.8 | -1.2 | -1.6 | -13.4 | 0.82 | 58.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | both | 4-4 | 50.0 | 38.7 | 11.3 | +0.49 | 6.1 | 0.04 | 37.5 | keep collecting (8/30) |
| rlm_quiet+sharp_gap | both | 4-5 | 44.4 | 38.9 | 5.5 | -0.51 | -5.7 | 0.03 | 33.3 | keep collecting (9/30) |
| rlm_ratio+sharp_gap | both | 5-7 | 41.7 | 42.8 | -1.2 | -1.6 | -13.4 | 0.82 | 58.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 5-5 | 50.0 | 49.1 | 0.9 | -1.33 | -13.3 | 0.96 | 70.0 | keep collecting (10/30) |
| money_moving+rlm_quiet | both | 5-4 | 55.6 | 38.9 | 16.6 | +2.37 | 26.3 | 0.97 | 55.6 | keep collecting (9/30) |
| money_moving+rlm_ratio | both | 5-3 | 62.5 | 42.1 | 20.4 | +2.4 | 29.9 | 1.57 | 75.0 | keep collecting (8/30) |
| money_moving+sharp_gap | both | 11-10 | 52.4 | 48.5 | 3.9 | +1.27 | 6.1 | 0.72 | 57.1 | keep collecting (21/30) |
| consensus_gap+money_moving | both | 4-2 | 66.7 | 50.8 | 15.9 | +0.17 | 2.8 | 0.35 | 50.0 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 4-3 | 57.1 | 48.1 | 9.1 | +0.17 | 2.4 | 0.04 | 57.1 | keep collecting (7/30) |
| money_level+rlm_ratio | both | 1-3 | 25.0 | 51.2 | -26.2 | -2.09 | -52.3 | 2.38 | 100.0 | keep collecting (4/30) |
| follow_move+pin_move | both | 1-3 | 25.0 | 45.5 | -20.5 | -2.09 | -52.3 | 0.5 | 25.0 | keep collecting (4/30) |
| follow_move+money_delta | both | 1-1 | 50.0 | 41.0 | 9.0 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_level | both | 1-1 | 50.0 | 41.0 | 9.0 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_moving | both | 1-1 | 50.0 | 41.0 | 9.0 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | both | 1-1 | 50.0 | 41.0 | 9.0 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | both | 1-1 | 50.0 | 41.0 | 9.0 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| follow_move+pin_value | both | 3-3 | 50.0 | 44.0 | 6.0 | -0.27 | -4.5 | -0.83 | 16.7 | keep collecting (6/30) |
| consensus_gap+pin_move | both | 1-0 | 100.0 | 59.0 | 41.0 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+pin_value | both | 4-1 | 80.0 | 51.8 | 28.2 | +2.6 | 51.9 | 0.2 | 40.0 | keep collecting (5/30) |
| money_level+pin_move | both | 1-0 | 100.0 | 59.0 | 41.0 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | both | 2-1 | 66.7 | 54.5 | 12.1 | +0.82 | 27.3 | 0.9 | 66.7 | keep collecting (3/30) |
| pin_move+pin_value | both | 2-3 | 40.0 | 51.8 | -11.8 | -1.18 | -23.6 | -0.4 | 0.0 | keep collecting (5/30) |
| money_moving+pin_value | both | 1-1 | 50.0 | 52.3 | -2.3 | -0.09 | -4.5 | 1.35 | 100.0 | keep collecting (2/30) |
| pin_value+sharp_gap | both | 1-1 | 50.0 | 52.3 | -2.3 | -0.09 | -4.5 | 1.35 | 100.0 | keep collecting (2/30) |
| consensus_gap+money_delta | both | 1-0 | 100.0 | 41.0 | 59.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 1-0 | 100.0 | 41.0 | 59.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | both | 1-0 | 100.0 | 41.0 | 59.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+rlm_ratio | both | 1-0 | 100.0 | 41.0 | 59.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 0-1 | 0.0 | 63.6 | -63.6 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-1 | 0.0 | 63.6 | -63.6 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | both | 0-1 | 0.0 | 63.6 | -63.6 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 0-1 | 0.0 | 63.6 | -63.6 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet | moneyline | 4-7 | 36.4 | 36.4 | -0.0 | -0.79 | -7.2 | 0.33 | 36.4 | keep collecting (11/30) |
| rlm_quiet | total | 4-5 | 44.4 | 41.0 | 3.5 | -1.4 | -15.6 | 0.33 | 44.4 | keep collecting (9/30) |
| pin_move | spread | 0-2 | 0.0 | 41.0 | -41.0 | -2.0 | -100.0 | 0.0 | 0.0 | keep collecting (2/30) |
| pin_move | total | 4-2 | 66.7 | 53.0 | 13.7 | +1.64 | 27.3 | -0.33 | 16.7 | keep collecting (6/30) |
| money_delta | total | 1-1 | 50.0 | 41.0 | 9.0 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| pin_rlm | moneyline | 0-1 | 0.0 | 63.6 | -63.6 | -1.0 | -100.0 | 1.5 | 100.0 | keep collecting (1/30) |
| follow_move | moneyline | 33-27 | 55.0 | 46.8 | 8.2 | +5.75 | 9.6 | -0.13 | 33.3 | no edge shown yet |
| follow_move | spread | 21-31 | 40.4 | 52.1 | -11.7 | -11.48 | -22.1 | -0.08 | 28.8 | DROP: below break-even |
| follow_move | total | 26-39 | 40.0 | 46.5 | -6.5 | -15.27 | -23.5 | 0.65 | 46.2 | DROP: below break-even |
| rlm_ratio | moneyline | 1-4 | 20.0 | 41.8 | -21.8 | -2.24 | -44.8 | 0.56 | 40.0 | keep collecting (5/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 59.0 | -59.0 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| rlm_ratio | total | 4-2 | 66.7 | 41.0 | 25.7 | +1.64 | 27.3 | 0.33 | 66.7 | keep collecting (6/30) |
| money_level | moneyline | 12-10 | 54.5 | 61.2 | -6.6 | -5.33 | -24.2 | -0.38 | 27.3 | keep collecting (22/30) |
| money_level | spread | 0-1 | 0.0 | 59.0 | -59.0 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level | total | 9-9 | 50.0 | 57.0 | -7.0 | -0.79 | -4.4 | 0.22 | 50.0 | keep collecting (18/30) |
| sharp_gap | moneyline | 6-11 | 35.3 | 46.0 | -10.7 | -4.6 | -27.0 | 0.54 | 52.9 | keep collecting (17/30) |
| sharp_gap | spread | 0-1 | 0.0 | 59.0 | -59.0 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| sharp_gap | total | 9-7 | 56.2 | 47.7 | 8.5 | +1.21 | 7.6 | -0.19 | 37.5 | keep collecting (16/30) |
| money_moving | moneyline | 9-8 | 52.9 | 50.8 | 2.1 | -0.33 | -1.9 | 0.92 | 58.8 | keep collecting (17/30) |
| money_moving | spread | 0-1 | 0.0 | 59.0 | -59.0 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving | total | 9-7 | 56.2 | 47.7 | 8.5 | +1.22 | 7.6 | 0.0 | 37.5 | keep collecting (16/30) |
| pin_value | moneyline | 0-1 | 0.0 | 63.6 | -63.6 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| pin_value | spread | 5-6 | 45.5 | 45.9 | -0.4 | -1.69 | -15.3 | -0.18 | 18.2 | keep collecting (11/30) |
| pin_value | total | 5-2 | 71.4 | 51.3 | 20.1 | +2.54 | 36.4 | -0.71 | 28.6 | keep collecting (7/30) |
| consensus_gap | moneyline | 22-19 | 53.7 | 53.0 | 0.7 | -1.89 | -4.6 | -0.18 | 41.5 | no edge shown yet |
| consensus_gap | spread | 13-10 | 56.5 | 48.0 | 8.5 | +1.44 | 6.2 | 0.35 | 39.1 | keep collecting (23/30) |
| consensus_gap | total | 19-12 | 61.3 | 49.1 | 12.2 | +5.12 | 16.5 | 1.0 | 61.3 | no edge shown yet |
| consensus_gap+money_level | moneyline | 6-4 | 60.0 | 58.2 | 1.8 | -1.83 | -18.3 | -0.71 | 30.0 | keep collecting (10/30) |
| follow_move+rlm_quiet | moneyline | 4-7 | 36.4 | 36.4 | -0.0 | -0.79 | -7.2 | 0.33 | 36.4 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 1-4 | 20.0 | 41.8 | -21.8 | -2.24 | -44.8 | 0.56 | 40.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 1-4 | 20.0 | 41.8 | -21.8 | -2.24 | -44.8 | 0.56 | 40.0 | keep collecting (5/30) |
| rlm_quiet+rlm_ratio | moneyline | 1-3 | 25.0 | 36.4 | -11.4 | -1.24 | -31.0 | 0.33 | 25.0 | keep collecting (4/30) |
| rlm_quiet+sharp_gap | moneyline | 1-3 | 25.0 | 36.4 | -11.4 | -1.24 | -31.0 | 0.33 | 25.0 | keep collecting (4/30) |
| rlm_ratio+sharp_gap | moneyline | 1-4 | 20.0 | 41.8 | -21.8 | -2.24 | -44.8 | 0.56 | 40.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 3-1 | 75.0 | 56.8 | 18.2 | +0.86 | 21.4 | -0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+money_moving | moneyline | 3-2 | 60.0 | 52.7 | 7.3 | -0.74 | -14.8 | 0.22 | 40.0 | keep collecting (5/30) |
| consensus_gap+sharp_gap | moneyline | 3-2 | 60.0 | 47.3 | 12.7 | +0.26 | 5.2 | -0.54 | 40.0 | keep collecting (5/30) |
| money_level+money_moving | moneyline | 5-4 | 55.6 | 60.6 | -5.1 | -1.95 | -21.6 | 0.3 | 33.3 | keep collecting (9/30) |
| money_level+sharp_gap | moneyline | 3-5 | 37.5 | 56.8 | -19.3 | -3.24 | -40.5 | 0.15 | 50.0 | keep collecting (8/30) |
| money_moving+sharp_gap | moneyline | 4-5 | 44.4 | 48.5 | -4.0 | -0.12 | -1.4 | 1.24 | 66.7 | keep collecting (9/30) |
| follow_move+money_level | moneyline | 3-3 | 50.0 | 63.6 | -13.6 | -2.31 | -38.5 | -0.65 | 16.7 | keep collecting (6/30) |
| follow_move+money_moving | moneyline | 5-3 | 62.5 | 50.0 | 12.5 | +1.14 | 14.2 | 0.65 | 50.0 | keep collecting (8/30) |
| money_moving+rlm_quiet | moneyline | 2-2 | 50.0 | 36.4 | 13.6 | +1.64 | 41.0 | 1.68 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | moneyline | 1-1 | 50.0 | 36.4 | 13.6 | +0.76 | 38.0 | 0.8 | 50.0 | keep collecting (2/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 63.6 | -63.6 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 63.6 | -63.6 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 63.6 | -63.6 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_rlm | moneyline | 0-1 | 0.0 | 63.6 | -63.6 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 63.6 | -63.6 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | moneyline | 0-1 | 0.0 | 63.6 | -63.6 | -1.0 | -100.0 | 1.5 | 100.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 0-1 | 0.0 | 63.6 | -63.6 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 0-1 | 0.0 | 63.6 | -63.6 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+money_level | spread | 0-1 | 0.0 | 59.0 | -59.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| follow_move+money_moving | spread | 0-1 | 0.0 | 59.0 | -59.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 59.0 | -59.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 0-1 | 0.0 | 59.0 | -59.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to sharp_gap alone, not independent confirmation |
| money_level+money_moving | spread | 0-1 | 0.0 | 59.0 | -59.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+rlm_ratio | spread | 0-1 | 0.0 | 59.0 | -59.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+sharp_gap | spread | 0-1 | 0.0 | 59.0 | -59.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 59.0 | -59.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| money_moving+sharp_gap | spread | 0-1 | 0.0 | 59.0 | -59.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 59.0 | -59.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 1-1 | 50.0 | 41.0 | 9.0 | -0.09 | -4.5 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | spread | 0-2 | 0.0 | 41.0 | -41.0 | -2.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| consensus_gap+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.13 | -6.5 | -0.5 | 0.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 0-1 | 0.0 | 41.0 | -41.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_level | total | 2-4 | 33.3 | 53.0 | -19.7 | -2.18 | -36.4 | 0.67 | 50.0 | keep collecting (6/30) |
| follow_move+sharp_gap | total | 5-5 | 50.0 | 46.4 | 3.6 | -0.45 | -4.5 | 0.3 | 50.0 | keep collecting (10/30) |
| money_level+sharp_gap | total | 4-4 | 50.0 | 54.5 | -4.5 | -0.33 | -4.1 | -0.12 | 50.0 | keep collecting (8/30) |
| follow_move+money_moving | total | 4-5 | 44.4 | 45.0 | -0.5 | -1.36 | -15.2 | 0.44 | 44.4 | keep collecting (9/30) |
| money_level+money_moving | total | 4-4 | 50.0 | 54.5 | -4.5 | -0.33 | -4.1 | 0.12 | 50.0 | keep collecting (8/30) |
| follow_move+rlm_quiet | total | 4-5 | 44.4 | 41.0 | 3.5 | -1.4 | -15.6 | 0.33 | 44.4 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 4-2 | 66.7 | 41.0 | 25.7 | +1.64 | 27.3 | 0.33 | 66.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 3-1 | 75.0 | 41.0 | 34.0 | +1.73 | 43.2 | -0.25 | 50.0 | keep collecting (4/30) |
| rlm_quiet+sharp_gap | total | 3-2 | 60.0 | 41.0 | 19.0 | +0.73 | 14.5 | -0.2 | 40.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | total | 4-2 | 66.7 | 41.0 | 25.7 | +1.64 | 27.3 | 0.33 | 66.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | total | 3-2 | 60.0 | 41.0 | 19.0 | +0.73 | 14.5 | 0.4 | 40.0 | keep collecting (5/30) |
| money_moving+rlm_ratio | total | 4-1 | 80.0 | 41.0 | 39.0 | +2.64 | 52.7 | 1.2 | 80.0 | keep collecting (5/30) |
| money_moving+sharp_gap | total | 7-4 | 63.6 | 47.5 | 16.1 | +2.4 | 21.8 | -0.09 | 45.5 | keep collecting (11/30) |
| follow_move+pin_move | total | 1-2 | 33.3 | 47.0 | -13.7 | -1.09 | -36.4 | 0.67 | 33.3 | keep collecting (3/30) |
| consensus_gap+follow_move | total | 2-4 | 33.3 | 44.0 | -10.7 | -2.18 | -36.4 | 1.67 | 83.3 | keep collecting (6/30) |
| consensus_gap+money_level | total | 2-1 | 66.7 | 53.0 | 13.7 | +0.82 | 27.3 | 1.0 | 66.7 | keep collecting (3/30) |
| consensus_gap+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| follow_move+money_delta | total | 1-1 | 50.0 | 41.0 | 9.0 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_level | total | 1-1 | 50.0 | 41.0 | 9.0 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_moving | total | 1-1 | 50.0 | 41.0 | 9.0 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | total | 1-1 | 50.0 | 41.0 | 9.0 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | total | 1-1 | 50.0 | 41.0 | 9.0 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+rlm_ratio | total | 1-1 | 50.0 | 41.0 | 9.0 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| follow_move+pin_value | total | 2-2 | 50.0 | 45.5 | 4.5 | -0.18 | -4.5 | -1.0 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | total | 1-0 | 100.0 | 59.0 | 41.0 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+pin_value | total | 3-0 | 100.0 | 53.0 | 47.0 | +2.73 | 90.9 | 0.67 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | total | 1-0 | 100.0 | 59.0 | 41.0 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.82 | 90.9 | 0.5 | 50.0 | keep collecting (2/30) |
| pin_move+pin_value | total | 2-1 | 66.7 | 59.0 | 7.7 | +0.82 | 27.3 | -0.67 | 0.0 | keep collecting (3/30) |
| consensus_gap+money_delta | total | 1-0 | 100.0 | 41.0 | 59.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_moving | total | 1-0 | 100.0 | 41.0 | 59.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 1-0 | 100.0 | 41.0 | 59.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | total | 1-0 | 100.0 | 41.0 | 59.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 41.0 | 59.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+rlm_ratio | total | 1-0 | 100.0 | 41.0 | 59.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | total | 1-0 | 100.0 | 41.0 | 59.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 42-82 | 33.9 | 41.8 | -7.9 | -26.81 | -21.6 |  |  | DROP: below break-even |
| pin_move | both | 80-89 | 47.3 | 49.6 | -2.3 | -13.1 | -7.7 |  |  | no edge shown yet |
| money_delta | both | 48-53 | 47.5 | 42.1 | 5.4 | -2.46 | -2.4 |  |  | no edge shown yet |
| pin_rlm | both | 15-23 | 39.5 | 40.1 | -0.6 | -6.49 | -17.1 |  |  | DROP: below break-even |
| follow_move | both | 131-164 | 44.4 | 49.3 | -4.9 | -39.5 | -13.4 |  |  | DROP: below break-even |
| rlm_ratio | both | 26-48 | 35.1 | 40.9 | -5.7 | -21.24 | -28.7 |  |  | DROP: below break-even |
| money_level | both | 176-120 | 59.5 | 56.5 | 2.9 | +5.75 | 1.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 130-142 | 47.8 | 48.0 | -0.2 | -20.77 | -7.6 |  |  | DROP: below break-even |
| money_moving | both | 134-142 | 48.6 | 48.5 | 0.0 | -20.23 | -7.3 |  |  | no edge shown yet |
| pin_value | both | 72-50 | 59.0 | 51.1 | 7.9 | +29.3 | 24.0 |  |  | no edge shown yet |
| consensus_gap | both | 69-38 | 64.5 | 53.4 | 11.1 | +20.44 | 19.1 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+pin_move | both | 52-78 | 40.0 | 49.1 | -9.1 | -28.67 | -22.1 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 36-37 | 49.3 | 41.3 | 8.0 | +2.46 | 3.4 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 36-36 | 50.0 | 41.3 | 8.7 | +3.46 | 4.8 |  |  | no edge shown yet |
| money_moving+sharp_gap | both | 127-137 | 48.1 | 48.2 | -0.1 | -18.04 | -6.8 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 47-21 | 69.1 | 59.0 | 10.1 | +8.23 | 12.1 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+rlm_quiet | both | 42-82 | 33.9 | 41.8 | -7.9 | -26.81 | -21.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | both | 22-37 | 37.3 | 43.3 | -6.0 | -12.89 | -21.8 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 22-13 | 62.9 | 53.4 | 9.5 | +5.07 | 14.5 |  |  | no edge shown yet |
| follow_move+money_level | both | 63-51 | 55.3 | 57.1 | -1.8 | -5.54 | -4.9 |  |  | no edge shown yet |
| money_level+money_moving | both | 93-71 | 56.7 | 53.9 | 2.8 | +1.6 | 1.0 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 89-70 | 56.0 | 53.5 | 2.4 | +2.06 | 1.3 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 26-21 | 55.3 | 51.8 | 3.5 | +5.27 | 11.2 |  |  | no edge shown yet |
| consensus_gap+pin_move | both | 17-6 | 73.9 | 51.2 | 22.7 | +11.33 | 49.3 |  |  | keep collecting (23/30) |
| consensus_gap+pin_value | both | 25-13 | 65.8 | 50.4 | 15.4 | +12.77 | 33.6 |  |  | PROMOTE: beats break-even and its own base rate |
| consensus_gap+sharp_gap | both | 26-21 | 55.3 | 51.4 | 4.0 | +5.55 | 11.8 |  |  | no edge shown yet |
| follow_move+money_moving | both | 61-78 | 43.9 | 48.2 | -4.3 | -25.73 | -18.5 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 22-16 | 57.9 | 52.4 | 5.5 | +13.34 | 35.1 |  |  | no edge shown yet |
| follow_move+sharp_gap | both | 62-79 | 44.0 | 47.9 | -3.9 | -24.8 | -17.6 |  |  | DROP: below break-even |
| money_level+pin_move | both | 34-31 | 52.3 | 55.6 | -3.3 | -3.52 | -5.4 |  |  | no edge shown yet |
| money_level+pin_value | both | 28-18 | 60.9 | 54.0 | 6.8 | +6.6 | 14.3 |  |  | no edge shown yet |
| money_moving+pin_move | both | 34-35 | 49.3 | 47.5 | 1.8 | -2.77 | -4.0 |  |  | no edge shown yet |
| money_moving+pin_value | both | 24-20 | 54.5 | 50.7 | 3.8 | +4.89 | 11.1 |  |  | no edge shown yet |
| pin_move+pin_value | both | 27-19 | 58.7 | 52.7 | 6.0 | +5.08 | 11.0 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 32-36 | 47.1 | 47.0 | 0.1 | -5.55 | -8.2 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 23-18 | 56.1 | 50.1 | 6.0 | +5.98 | 14.6 |  |  | no edge shown yet |
| follow_move+money_delta | both | 28-38 | 42.4 | 43.3 | -0.9 | -11.71 | -17.7 |  |  | DROP: below break-even |
| money_delta+pin_move | both | 15-18 | 45.5 | 41.5 | 4.0 | -3.8 | -11.5 |  |  | no edge shown yet |
| money_delta+rlm_quiet | both | 16-29 | 35.6 | 40.9 | -5.4 | -13.6 | -30.2 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | both | 26-48 | 35.1 | 40.9 | -5.7 | -21.24 | -28.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | both | 17-39 | 30.4 | 39.3 | -9.0 | -20.66 | -36.9 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 26-46 | 36.1 | 41.0 | -4.9 | -19.24 | -26.7 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 12-36 | 25.0 | 38.8 | -13.8 | -22.81 | -47.5 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | both | 17-41 | 29.3 | 39.2 | -9.9 | -22.66 | -39.1 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 26-48 | 35.1 | 40.9 | -5.7 | -21.24 | -28.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | both | 12-6 | 66.7 | 47.3 | 19.4 | +5.8 | 32.2 |  |  | keep collecting (18/30) |
| consensus_gap+rlm_quiet | both | 6-7 | 46.2 | 40.9 | 5.2 | +0.04 | 0.3 |  |  | keep collecting (13/30) |
| consensus_gap+rlm_ratio | both | 5-4 | 55.6 | 39.9 | 15.6 | +2.05 | 22.8 |  |  | keep collecting (9/30) |
| money_delta+rlm_ratio | both | 19-27 | 41.3 | 41.3 | -0.0 | -8.91 | -19.4 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 2-2 | 50.0 | 44.3 | 5.7 | +1.4 | 35.0 |  |  | keep collecting (4/30) |
| money_level+pin_rlm | both | 5-4 | 55.6 | 43.0 | 12.6 | +0.74 | 8.2 |  |  | keep collecting (9/30) |
| money_moving+pin_rlm | both | 15-22 | 40.5 | 40.2 | 0.3 | -5.49 | -14.8 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 15-23 | 39.5 | 40.1 | -0.6 | -6.49 | -17.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | both | 11-9 | 55.0 | 45.7 | 9.3 | +1.18 | 5.9 |  |  | keep collecting (20/30) |
| consensus_gap+money_delta | both | 8-2 | 80.0 | 45.0 | 35.0 | +8.81 | 88.1 |  |  | keep collecting (10/30) |
| follow_move+pin_rlm | both | 13-20 | 39.4 | 39.0 | 0.4 | -5.72 | -17.3 |  |  | no edge shown yet |
| money_delta+pin_rlm | both | 9-14 | 39.1 | 39.0 | 0.2 | -5.27 | -22.9 |  |  | keep collecting (23/30) |
| pin_move+pin_rlm | both | 14-18 | 43.8 | 40.0 | 3.8 | -2.83 | -8.8 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 13-17 | 43.3 | 40.0 | 3.3 | -3.21 | -10.7 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | both | 7-15 | 31.8 | 38.7 | -6.9 | -6.8 | -30.9 |  |  | keep collecting (22/30) |
| pin_rlm+rlm_ratio | both | 13-20 | 39.4 | 39.0 | 0.4 | -5.72 | -17.3 |  |  | no edge shown yet |
| money_delta+pin_value | both | 12-3 | 80.0 | 44.3 | 35.7 | +11.44 | 76.3 |  |  | keep collecting (15/30) |
| pin_value+rlm_quiet | both | 8-6 | 57.1 | 45.8 | 11.3 | +11.01 | 78.6 |  |  | keep collecting (14/30) |
| pin_value+rlm_ratio | both | 4-0 | 100.0 | 50.0 | 50.0 | +3.53 | 88.4 |  |  | keep collecting (4/30) |
| pin_rlm+pin_value | both | 2-1 | 66.7 | 47.0 | 19.7 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| rlm_quiet | moneyline | 15-35 | 30.0 | 36.9 | -6.9 | -4.97 | -9.9 |  |  | DROP: below break-even |
| rlm_quiet | spread | 8-11 | 42.1 | 56.2 | -14.1 | -3.46 | -18.2 |  |  | keep collecting (19/30) |
| rlm_quiet | total | 19-36 | 34.5 | 41.3 | -6.8 | -18.38 | -33.4 |  |  | DROP: below break-even |
| pin_move | moneyline | 22-19 | 53.7 | 47.7 | 6.0 | +4.17 | 10.2 |  |  | no edge shown yet |
| pin_move | spread | 29-27 | 51.8 | 52.6 | -0.8 | -0.75 | -1.3 |  |  | no edge shown yet |
| pin_move | total | 29-43 | 40.3 | 48.5 | -8.2 | -16.53 | -23.0 |  |  | DROP: below break-even |
| money_delta | moneyline | 13-21 | 38.2 | 39.6 | -1.3 | -2.69 | -7.9 |  |  | DROP: below break-even |
| money_delta | spread | 7-4 | 63.6 | 50.8 | 12.8 | +2.44 | 22.2 |  |  | keep collecting (11/30) |
| money_delta | total | 28-28 | 50.0 | 41.9 | 8.1 | -2.22 | -4.0 |  |  | no edge shown yet |
| pin_rlm | moneyline | 6-11 | 35.3 | 38.0 | -2.7 | -2.84 | -16.7 |  |  | keep collecting (17/30) |
| pin_rlm | spread | 1-0 | 100.0 | 59.0 | 41.0 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| pin_rlm | total | 8-12 | 40.0 | 41.0 | -1.0 | -4.56 | -22.8 |  |  | keep collecting (20/30) |
| follow_move | moneyline | 48-55 | 46.6 | 48.5 | -1.9 | -6.63 | -6.4 |  |  | no edge shown yet |
| follow_move | spread | 36-43 | 45.6 | 52.4 | -6.8 | -9.9 | -12.5 |  |  | no edge shown yet |
| follow_move | total | 47-66 | 41.6 | 47.8 | -6.3 | -22.98 | -20.3 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 9-26 | 25.7 | 37.1 | -11.4 | -14.79 | -42.3 |  |  | DROP: below break-even |
| rlm_ratio | spread | 1-2 | 33.3 | 53.0 | -19.7 | -1.15 | -38.4 |  |  | keep collecting (3/30) |
| rlm_ratio | total | 16-20 | 44.4 | 43.5 | 1.0 | -5.3 | -14.7 |  |  | no edge shown yet |
| money_level | moneyline | 70-40 | 63.6 | 61.2 | 2.5 | -9.51 | -8.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 34-31 | 52.3 | 48.5 | 3.8 | -0.54 | -0.8 |  |  | no edge shown yet |
| money_level | total | 72-49 | 59.5 | 56.6 | 2.9 | +15.81 | 13.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | moneyline | 45-54 | 45.5 | 46.3 | -0.8 | -9.75 | -9.8 |  |  | no edge shown yet |
| sharp_gap | spread | 31-33 | 48.4 | 47.2 | 1.3 | -5.11 | -8.0 |  |  | no edge shown yet |
| sharp_gap | total | 54-55 | 49.5 | 50.1 | -0.5 | -5.91 | -5.4 |  |  | no edge shown yet |
| money_moving | moneyline | 49-50 | 49.5 | 47.4 | 2.1 | -5.13 | -5.2 |  |  | no edge shown yet |
| money_moving | spread | 31-33 | 48.4 | 47.2 | 1.3 | -5.11 | -8.0 |  |  | no edge shown yet |
| money_moving | total | 54-59 | 47.8 | 50.2 | -2.5 | -9.98 | -8.8 |  |  | no edge shown yet |
| pin_value | moneyline | 5-1 | 83.3 | 45.5 | 37.9 | +19.16 | 319.4 |  |  | keep collecting (6/30) |
| pin_value | spread | 31-23 | 57.4 | 50.0 | 7.4 | +3.86 | 7.1 |  |  | no edge shown yet |
| pin_value | total | 36-26 | 58.1 | 52.6 | 5.4 | +6.28 | 10.1 |  |  | no edge shown yet |
| consensus_gap | moneyline | 36-22 | 62.1 | 55.2 | 6.9 | +7.48 | 12.9 |  |  | no edge shown yet |
| consensus_gap | spread | 13-7 | 65.0 | 47.3 | 17.7 | +4.19 | 20.9 |  |  | keep collecting (20/30) |
| consensus_gap | total | 20-9 | 69.0 | 54.0 | 14.9 | +8.77 | 30.2 |  |  | keep collecting (29/30) |
| consensus_gap+money_level | moneyline | 27-10 | 73.0 | 62.9 | 10.1 | +1.66 | 4.5 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+pin_move | moneyline | 14-19 | 42.4 | 47.1 | -4.7 | -4.44 | -13.5 |  |  | no edge shown yet |
| follow_move+rlm_quiet | moneyline | 15-35 | 30.0 | 36.9 | -6.9 | -4.97 | -9.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | moneyline | 7-12 | 36.8 | 37.8 | -1.0 | -1.85 | -9.8 |  |  | keep collecting (19/30) |
| consensus_gap+follow_move | moneyline | 12-8 | 60.0 | 52.7 | 7.3 | +1.17 | 5.9 |  |  | keep collecting (20/30) |
| follow_move+money_level | moneyline | 28-18 | 60.9 | 61.3 | -0.4 | -4.46 | -9.7 |  |  | no edge shown yet |
| money_moving+sharp_gap | moneyline | 44-49 | 47.3 | 46.6 | 0.7 | -5.16 | -5.6 |  |  | no edge shown yet |
| follow_move+money_moving | moneyline | 26-31 | 45.6 | 46.9 | -1.3 | -10.61 | -18.6 |  |  | no edge shown yet |
| follow_move+sharp_gap | moneyline | 25-33 | 43.1 | 46.2 | -3.1 | -12.54 | -21.6 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 32-18 | 64.0 | 58.2 | 5.8 | -0.26 | -0.5 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+sharp_gap | moneyline | 28-18 | 60.9 | 57.7 | 3.2 | -0.88 | -1.9 |  |  | no edge shown yet |
| follow_move+rlm_ratio | moneyline | 9-26 | 25.7 | 37.1 | -11.4 | -14.79 | -42.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | moneyline | 7-21 | 25.0 | 36.4 | -11.4 | -11.88 | -42.4 |  |  | keep collecting (28/30) |
| money_moving+rlm_ratio | moneyline | 9-24 | 27.3 | 37.2 | -9.9 | -12.79 | -38.8 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | moneyline | 5-22 | 18.5 | 36.4 | -17.8 | -15.26 | -56.5 |  |  | keep collecting (27/30) |
| rlm_quiet+sharp_gap | moneyline | 7-23 | 23.3 | 36.4 | -13.0 | -13.88 | -46.3 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 9-26 | 25.7 | 37.1 | -11.4 | -14.79 | -42.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 14-11 | 56.0 | 52.7 | 3.3 | +4.63 | 18.5 |  |  | keep collecting (25/30) |
| consensus_gap+rlm_quiet | moneyline | 2-6 | 25.0 | 36.4 | -11.4 | -2.6 | -32.5 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_ratio | moneyline | 2-4 | 33.3 | 36.4 | -3.0 | -0.6 | -10.0 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | moneyline | 14-12 | 53.8 | 52.1 | 1.7 | +3.91 | 15.0 |  |  | keep collecting (26/30) |
| consensus_gap+pin_rlm | moneyline | 2-1 | 66.7 | 45.5 | 21.2 | +2.4 | 80.0 |  |  | keep collecting (3/30) |
| money_level+pin_rlm | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | +0.02 | 1.0 |  |  | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 6-10 | 37.5 | 38.1 | -0.6 | -1.84 | -11.5 |  |  | keep collecting (16/30) |
| pin_rlm+sharp_gap | moneyline | 6-11 | 35.3 | 38.0 | -2.7 | -2.84 | -16.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 3-0 | 100.0 | 45.5 | 54.5 | +6.46 | 215.5 |  |  | keep collecting (3/30) |
| money_level+rlm_ratio | moneyline | 2-3 | 40.0 | 41.8 | -1.8 | -1.05 | -21.1 |  |  | keep collecting (5/30) |
| consensus_gap+pin_move | moneyline | 10-2 | 83.3 | 50.0 | 33.3 | +9.18 | 76.5 |  |  | keep collecting (12/30) |
| money_level+pin_move | moneyline | 10-6 | 62.5 | 61.9 | 0.6 | -0.08 | -0.5 |  |  | keep collecting (16/30) |
| consensus_gap+money_delta | moneyline | 3-2 | 60.0 | 41.8 | 18.2 | +4.35 | 86.9 |  |  | keep collecting (5/30) |
| follow_move+money_delta | moneyline | 7-15 | 31.8 | 41.3 | -9.5 | -8.06 | -36.6 |  |  | keep collecting (22/30) |
| follow_move+pin_rlm | moneyline | 5-9 | 35.7 | 36.4 | -0.6 | -2.16 | -15.4 |  |  | keep collecting (14/30) |
| money_delta+money_moving | moneyline | 12-20 | 37.5 | 38.9 | -1.4 | -2.54 | -7.9 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 3-5 | 37.5 | 36.4 | 1.1 | -1.9 | -23.8 |  |  | keep collecting (8/30) |
| money_delta+pin_rlm | moneyline | 3-7 | 30.0 | 36.4 | -6.4 | -3.9 | -39.0 |  |  | keep collecting (10/30) |
| money_delta+rlm_quiet | moneyline | 3-13 | 18.8 | 36.4 | -17.6 | -9.66 | -60.4 |  |  | keep collecting (16/30) |
| money_delta+rlm_ratio | moneyline | 4-14 | 22.2 | 37.9 | -15.7 | -9.64 | -53.6 |  |  | keep collecting (18/30) |
| money_delta+sharp_gap | moneyline | 12-20 | 37.5 | 38.9 | -1.4 | -2.54 | -7.9 |  |  | DROP: below break-even |
| money_moving+pin_move | moneyline | 8-6 | 57.1 | 42.2 | 14.9 | +2.73 | 19.5 |  |  | keep collecting (14/30) |
| pin_move+pin_rlm | moneyline | 5-6 | 45.5 | 36.4 | 9.1 | +0.82 | 7.5 |  |  | keep collecting (11/30) |
| pin_move+rlm_ratio | moneyline | 4-6 | 40.0 | 36.4 | 3.6 | -0.5 | -5.0 |  |  | keep collecting (10/30) |
| pin_move+sharp_gap | moneyline | 8-7 | 53.3 | 41.8 | 11.5 | +1.74 | 11.6 |  |  | keep collecting (15/30) |
| pin_rlm+rlm_quiet | moneyline | 3-8 | 27.3 | 36.4 | -9.1 | -3.52 | -32.0 |  |  | keep collecting (11/30) |
| pin_rlm+rlm_ratio | moneyline | 5-9 | 35.7 | 36.4 | -0.6 | -2.16 | -15.4 |  |  | keep collecting (14/30) |
| follow_move+pin_value | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | +9.6 | 480.0 |  |  | keep collecting (2/30) |
| pin_value+rlm_quiet | moneyline | 1-0 | 100.0 | 36.4 | 63.6 | +10.6 | 1060.0 |  |  | keep collecting (1/30) |
| money_delta+money_level | moneyline | 4-1 | 80.0 | 52.7 | 27.3 | +3.47 | 69.5 |  |  | keep collecting (5/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 63.6 | -63.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_move+pin_value | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | +0.08 | 4.0 |  |  | keep collecting (2/30) |
| money_delta+pin_value | moneyline | 1-0 | 100.0 | 36.4 | 63.6 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 1-0 | 100.0 | 36.4 | 63.6 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 1-0 | 100.0 | 36.4 | 63.6 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| follow_move+pin_move | spread | 16-23 | 41.0 | 53.0 | -12.0 | -8.46 | -21.7 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 31-33 | 48.4 | 47.2 | 1.3 | -5.11 | -8.0 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 8-11 | 42.1 | 56.2 | -14.1 | -3.46 | -18.2 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | spread | 22-22 | 50.0 | 46.7 | 3.3 | -2.35 | -5.3 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 22-22 | 50.0 | 46.7 | 3.3 | -2.35 | -5.3 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 4-8 | 33.3 | 56.0 | -22.7 | -4.29 | -35.8 |  |  | keep collecting (12/30) |
| consensus_gap+pin_value | spread | 10-7 | 58.8 | 47.3 | 11.5 | +1.67 | 9.8 |  |  | keep collecting (17/30) |
| follow_move+money_level | spread | 9-7 | 56.2 | 53.4 | 2.9 | +1.29 | 8.1 |  |  | keep collecting (16/30) |
| follow_move+money_moving | spread | 8-9 | 47.1 | 52.7 | -5.6 | -1.74 | -10.2 |  |  | keep collecting (17/30) |
| follow_move+sharp_gap | spread | 8-9 | 47.1 | 52.7 | -5.6 | -1.74 | -10.2 |  |  | keep collecting (17/30) |
| money_level+pin_move | spread | 7-7 | 50.0 | 51.3 | -1.3 | -0.75 | -5.3 |  |  | keep collecting (14/30) |
| money_moving+pin_move | spread | 9-7 | 56.2 | 51.1 | 5.1 | +1.02 | 6.4 |  |  | keep collecting (16/30) |
| pin_move+sharp_gap | spread | 9-7 | 56.2 | 51.1 | 5.1 | +1.02 | 6.4 |  |  | keep collecting (16/30) |
| money_delta+money_level | spread | 2-1 | 66.7 | 47.0 | 19.7 | +0.76 | 25.2 |  |  | keep collecting (3/30) |
| money_delta+money_moving | spread | 4-2 | 66.7 | 47.0 | 19.7 | +1.57 | 26.2 |  |  | keep collecting (6/30) |
| money_delta+sharp_gap | spread | 4-2 | 66.7 | 47.0 | 19.7 | +1.57 | 26.2 |  |  | keep collecting (6/30) |
| consensus_gap+money_level | spread | 4-5 | 44.4 | 45.0 | -0.5 | -1.57 | -17.4 |  |  | keep collecting (9/30) |
| consensus_gap+money_moving | spread | 3-4 | 42.9 | 46.1 | -3.3 | -1.37 | -19.5 |  |  | keep collecting (7/30) |
| consensus_gap+sharp_gap | spread | 3-4 | 42.9 | 46.1 | -3.3 | -1.37 | -19.5 |  |  | keep collecting (7/30) |
| money_level+pin_value | spread | 9-6 | 60.0 | 45.8 | 14.2 | +1.75 | 11.7 |  |  | keep collecting (15/30) |
| money_moving+pin_value | spread | 9-8 | 52.9 | 48.4 | 4.5 | -0.14 | -0.8 |  |  | keep collecting (17/30) |
| pin_value+sharp_gap | spread | 9-8 | 52.9 | 48.4 | 4.5 | -0.14 | -0.8 |  |  | keep collecting (17/30) |
| follow_move+money_delta | spread | 4-2 | 66.7 | 56.0 | 10.7 | +1.65 | 27.4 |  |  | keep collecting (6/30) |
| follow_move+rlm_ratio | spread | 1-2 | 33.3 | 53.0 | -19.7 | -1.15 | -38.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.15 | -7.7 |  |  | keep collecting (2/30) |
| money_moving+rlm_ratio | spread | 1-2 | 33.3 | 53.0 | -19.7 | -1.15 | -38.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 1-2 | 33.3 | 53.0 | -19.7 | -1.15 | -38.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 9-5 | 64.3 | 53.9 | 10.4 | +2.98 | 21.3 |  |  | keep collecting (14/30) |
| pin_move+pin_value | spread | 15-6 | 71.4 | 53.0 | 18.4 | +7.15 | 34.0 |  |  | keep collecting (21/30) |
| consensus_gap+pin_move | spread | 4-2 | 66.7 | 53.0 | 13.7 | +1.5 | 25.0 |  |  | keep collecting (6/30) |
| consensus_gap+follow_move | spread | 3-1 | 75.0 | 59.0 | 16.0 | +1.67 | 41.6 |  |  | keep collecting (4/30) |
| consensus_gap+rlm_quiet | spread | 2-0 | 100.0 | 59.0 | 41.0 | +1.82 | 90.9 |  |  | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 2-2 | 50.0 | 59.0 | -9.0 | -0.18 | -4.5 |  |  | keep collecting (4/30) |
| money_delta+rlm_quiet | spread | 3-1 | 75.0 | 59.0 | 16.0 | +1.8 | 45.0 |  |  | keep collecting (4/30) |
| money_moving+rlm_quiet | spread | 1-2 | 33.3 | 53.0 | -19.7 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| rlm_quiet+rlm_ratio | spread | 0-1 | 0.0 | 59.0 | -59.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_quiet+sharp_gap | spread | 1-2 | 33.3 | 53.0 | -19.7 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| consensus_gap+money_delta | spread | 2-0 | 100.0 | 59.0 | 41.0 | +1.76 | 87.8 |  |  | keep collecting (2/30) |
| money_delta+pin_move | spread | 3-0 | 100.0 | 59.0 | 41.0 | +2.67 | 88.8 |  |  | keep collecting (3/30) |
| money_delta+pin_value | spread | 2-0 | 100.0 | 59.0 | 41.0 | +1.76 | 87.8 |  |  | keep collecting (2/30) |
| money_moving+pin_rlm | spread | 1-0 | 100.0 | 59.0 | 41.0 | +0.91 | 90.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | spread | 1-0 | 100.0 | 59.0 | 41.0 | +0.91 | 90.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | spread | 1-0 | 100.0 | 59.0 | 41.0 | +0.91 | 90.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 1-0 | 100.0 | 59.0 | 41.0 | +0.91 | 90.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+rlm_ratio | spread | 1-0 | 100.0 | 59.0 | 41.0 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| money_level+rlm_ratio | spread | 1-0 | 100.0 | 59.0 | 41.0 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| pin_move+rlm_ratio | spread | 1-0 | 100.0 | 59.0 | 41.0 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| pin_value+rlm_ratio | spread | 1-0 | 100.0 | 59.0 | 41.0 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| money_delta+money_moving | total | 20-15 | 57.1 | 42.5 | 14.6 | +3.43 | 9.8 |  |  | no edge shown yet |
| money_delta+sharp_gap | total | 20-14 | 58.8 | 42.6 | 16.2 | +4.43 | 13.0 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 52-55 | 48.6 | 50.1 | -1.5 | -7.76 | -7.3 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 19-36 | 34.5 | 41.3 | -6.8 | -18.38 | -33.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+follow_move | total | 7-4 | 63.6 | 52.5 | 11.2 | +2.23 | 20.3 |  |  | keep collecting (11/30) |
| consensus_gap+money_level | total | 16-6 | 72.7 | 58.2 | 14.5 | +8.14 | 37.0 |  |  | keep collecting (22/30) |
| consensus_gap+money_moving | total | 9-6 | 60.0 | 53.0 | 7.0 | +2.01 | 13.4 |  |  | keep collecting (15/30) |
| consensus_gap+pin_move | total | 3-2 | 60.0 | 51.8 | 8.2 | +0.65 | 13.0 |  |  | keep collecting (5/30) |
| consensus_gap+pin_value | total | 12-6 | 66.7 | 54.0 | 12.7 | +4.63 | 25.7 |  |  | keep collecting (18/30) |
| consensus_gap+sharp_gap | total | 9-5 | 64.3 | 52.6 | 11.7 | +3.01 | 21.5 |  |  | keep collecting (14/30) |
| follow_move+money_level | total | 26-26 | 50.0 | 54.5 | -4.5 | -2.37 | -4.6 |  |  | no edge shown yet |
| follow_move+money_moving | total | 27-38 | 41.5 | 48.2 | -6.7 | -13.37 | -20.6 |  |  | DROP: below break-even |
| follow_move+pin_move | total | 22-36 | 37.9 | 47.5 | -9.6 | -15.77 | -27.2 |  |  | DROP: below break-even |
| follow_move+pin_value | total | 12-10 | 54.5 | 51.6 | 2.9 | +0.76 | 3.5 |  |  | keep collecting (22/30) |
| follow_move+sharp_gap | total | 29-37 | 43.9 | 48.1 | -4.1 | -10.52 | -15.9 |  |  | no edge shown yet |
| money_level+money_moving | total | 39-31 | 55.7 | 55.4 | 0.3 | +4.21 | 6.0 |  |  | no edge shown yet |
| money_level+pin_move | total | 17-18 | 48.6 | 54.4 | -5.8 | -2.69 | -7.7 |  |  | no edge shown yet |
| money_level+pin_value | total | 19-11 | 63.3 | 57.8 | 5.5 | +5.84 | 19.5 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 39-30 | 56.5 | 55.1 | 1.4 | +5.28 | 7.7 |  |  | no edge shown yet |
| money_moving+pin_move | total | 17-22 | 43.6 | 47.9 | -4.3 | -6.53 | -16.7 |  |  | no edge shown yet |
| money_moving+pin_value | total | 14-12 | 53.8 | 52.8 | 1.1 | +0.53 | 2.1 |  |  | keep collecting (26/30) |
| pin_move+pin_value | total | 11-12 | 47.8 | 52.7 | -4.9 | -2.15 | -9.4 |  |  | keep collecting (23/30) |
| pin_move+sharp_gap | total | 15-22 | 40.5 | 47.3 | -6.8 | -8.31 | -22.4 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 13-10 | 56.5 | 52.0 | 4.6 | +1.63 | 7.1 |  |  | keep collecting (23/30) |
| follow_move+money_delta | total | 17-21 | 44.7 | 42.4 | 2.3 | -5.3 | -14.0 |  |  | no edge shown yet |
| money_delta+pin_move | total | 9-13 | 40.9 | 41.0 | -0.1 | -4.56 | -20.7 |  |  | keep collecting (22/30) |
| money_delta+rlm_quiet | total | 10-15 | 40.0 | 41.0 | -1.0 | -5.74 | -23.0 |  |  | keep collecting (25/30) |
| pin_move+rlm_quiet | total | 11-17 | 39.3 | 41.6 | -2.3 | -6.74 | -24.1 |  |  | keep collecting (28/30) |
| follow_move+rlm_ratio | total | 16-20 | 44.4 | 43.5 | 1.0 | -5.3 | -14.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | total | 14-12 | 53.8 | 43.1 | 10.8 | +0.89 | 3.4 |  |  | keep collecting (26/30) |
| money_moving+rlm_quiet | total | 9-16 | 36.0 | 41.0 | -5.0 | -7.69 | -30.8 |  |  | keep collecting (25/30) |
| money_moving+rlm_ratio | total | 16-20 | 44.4 | 43.5 | 1.0 | -5.3 | -14.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 7-13 | 35.0 | 41.0 | -6.0 | -6.55 | -32.8 |  |  | keep collecting (20/30) |
| rlm_quiet+sharp_gap | total | 9-16 | 36.0 | 41.0 | -5.0 | -7.69 | -30.8 |  |  | keep collecting (25/30) |
| rlm_ratio+sharp_gap | total | 16-20 | 44.4 | 43.5 | 1.0 | -5.3 | -14.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | total | 3-0 | 100.0 | 41.0 | 59.0 | +2.71 | 90.4 |  |  | keep collecting (3/30) |
| consensus_gap+rlm_quiet | total | 2-1 | 66.7 | 41.0 | 25.7 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| consensus_gap+rlm_ratio | total | 2-0 | 100.0 | 41.0 | 59.0 | +1.8 | 90.1 |  |  | keep collecting (2/30) |
| money_delta+pin_value | total | 9-3 | 75.0 | 42.5 | 32.5 | +5.18 | 43.2 |  |  | keep collecting (12/30) |
| pin_value+rlm_quiet | total | 5-4 | 55.6 | 41.0 | 14.6 | +0.59 | 6.5 |  |  | keep collecting (9/30) |
| pin_value+rlm_ratio | total | 3-0 | 100.0 | 47.0 | 53.0 | +2.69 | 89.6 |  |  | keep collecting (3/30) |
| follow_move+pin_rlm | total | 8-11 | 42.1 | 41.0 | 1.1 | -3.56 | -18.7 |  |  | keep collecting (19/30) |
| money_delta+money_level | total | 6-4 | 60.0 | 44.6 | 15.4 | +1.57 | 15.7 |  |  | keep collecting (10/30) |
| money_delta+pin_rlm | total | 6-7 | 46.2 | 41.0 | 5.2 | -1.37 | -10.6 |  |  | keep collecting (13/30) |
| money_level+pin_rlm | total | 4-3 | 57.1 | 41.0 | 16.2 | +0.72 | 10.3 |  |  | keep collecting (7/30) |
| money_level+rlm_ratio | total | 8-6 | 57.1 | 46.1 | 11.0 | +1.39 | 9.9 |  |  | keep collecting (14/30) |
| money_moving+pin_rlm | total | 8-12 | 40.0 | 41.0 | -1.0 | -4.56 | -22.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | total | 8-12 | 40.0 | 41.0 | -1.0 | -4.56 | -22.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 8-11 | 42.1 | 41.0 | 1.1 | -3.56 | -18.7 |  |  | keep collecting (19/30) |
| pin_rlm+rlm_ratio | total | 8-11 | 42.1 | 41.0 | 1.1 | -3.56 | -18.7 |  |  | keep collecting (19/30) |
| pin_rlm+sharp_gap | total | 8-12 | 40.0 | 41.0 | -1.0 | -4.56 | -22.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | total | 4-7 | 36.4 | 41.0 | -4.6 | -3.28 | -29.8 |  |  | keep collecting (11/30) |
| consensus_gap+pin_rlm | total | 0-1 | 0.0 | 41.0 | -41.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+pin_value | total | 1-1 | 50.0 | 41.0 | 9.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |

# FIT (in-sample — this is the hypothesis)

Games before 2026-11-21. The engine was built by looking at these, so a strong record here is expected and proves nothing. n=684 games.

## EARLY  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 30-36 | 45.5 | 35.9 | 9.6 | +10.59 | 16.0 | 0.18 | 43.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move | both | 5-9 | 35.7 | 48.2 | -12.5 | -5.1 | -36.4 | 0.22 | 50.0 | keep collecting (14/30) |
| money_delta | both | 10-7 | 58.8 | 41.8 | 17.0 | +4.43 | 26.1 | -0.22 | 29.4 | keep collecting (17/30) |
| pin_rlm | both | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | both | 474-402 | 54.1 | 52.4 | 1.7 | -44.48 | -5.1 | 0.19 | 42.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | both | 29-17 | 63.0 | 38.5 | 24.5 | +20.54 | 44.6 | 0.42 | 52.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | both | 169-109 | 60.8 | 59.0 | 1.8 | -11.33 | -4.1 | -0.12 | 39.2 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 143-120 | 54.4 | 48.4 | 6.0 | +19.09 | 7.3 | 0.29 | 43.3 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | both | 102-80 | 56.0 | 51.3 | 4.7 | +1.19 | 0.7 | 0.04 | 41.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | both | 50-49 | 50.5 | 48.3 | 2.2 | -4.6 | -4.6 | 0.09 | 37.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.3 | -31.3 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 219-290 | 43.0 | 47.2 | -4.2 | -61.46 | -12.1 | 0.39 | 45.0 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | both | 32-28 | 53.3 | 63.6 | -10.3 | -9.71 | -16.2 | 0.33 | 48.3 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | both | 17-23 | 42.5 | 46.7 | -4.2 | -6.42 | -16.1 | 0.25 | 42.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_value | both | 20-28 | 41.7 | 46.6 | -4.9 | -10.7 | -22.3 | 0.38 | 47.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_quiet | both | 30-36 | 45.5 | 35.9 | 9.6 | +10.59 | 16.0 | 0.18 | 43.9 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 29-17 | 63.0 | 38.5 | 24.5 | +20.54 | 44.6 | 0.42 | 52.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 75-37 | 67.0 | 50.1 | 16.9 | +25.31 | 22.6 | 0.37 | 48.2 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 64-39 | 62.1 | 58.2 | 4.0 | +0.13 | 0.1 | -0.17 | 46.6 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 11-9 | 55.0 | 49.8 | 5.2 | +0.81 | 4.0 | 0.4 | 45.0 | keep collecting (20/30) |
| money_moving+pin_value | both | 9-6 | 60.0 | 49.8 | 10.2 | +1.88 | 12.5 | 0.27 | 33.3 | keep collecting (15/30) |
| rlm_quiet+rlm_ratio | both | 16-10 | 61.5 | 35.7 | 25.9 | +14.25 | 54.8 | -0.07 | 50.0 | keep collecting (26/30) |
| rlm_quiet+sharp_gap | both | 18-13 | 58.1 | 35.8 | 22.3 | +13.06 | 42.1 | -0.08 | 48.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | both | 29-17 | 63.0 | 38.5 | 24.5 | +20.54 | 44.6 | 0.42 | 52.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 97-60 | 61.8 | 55.7 | 6.1 | +4.17 | 2.7 | 0.14 | 43.3 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 60-47 | 56.1 | 48.8 | 7.2 | +6.0 | 5.6 | 0.19 | 44.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_level | both | 3-2 | 60.0 | 45.8 | 14.2 | +1.46 | 29.2 | 1.16 | 60.0 | keep collecting (5/30) |
| money_delta+money_moving | both | 9-7 | 56.2 | 41.3 | 14.9 | +3.53 | 22.0 | -0.23 | 31.2 | keep collecting (16/30) |
| money_delta+pin_value | both | 3-1 | 75.0 | 50.0 | 25.0 | +1.61 | 40.3 | 0.0 | 25.0 | keep collecting (4/30) |
| money_delta+sharp_gap | both | 7-5 | 58.3 | 40.5 | 17.8 | +3.78 | 31.5 | -0.31 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | both | 13-8 | 61.9 | 48.8 | 13.1 | +3.66 | 17.4 | -0.18 | 33.3 | keep collecting (21/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 49.7 | -49.7 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 32-41 | 43.8 | 51.2 | -7.3 | -15.02 | -20.6 | 0.72 | 54.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_quiet | both | 4-7 | 36.4 | 37.2 | -0.8 | -2.99 | -27.1 | 0.95 | 72.7 | keep collecting (11/30) |
| follow_move+pin_value | both | 20-18 | 52.6 | 48.9 | 3.8 | -0.59 | -1.6 | -0.11 | 28.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 42.2 | -25.5 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 26-45 | 36.6 | 45.5 | -8.9 | -10.29 | -14.5 | 0.88 | 49.3 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | both | 91-44 | 67.4 | 60.2 | 7.2 | +1.24 | 0.9 | 0.0 | 43.7 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 11-7 | 61.1 | 41.4 | 19.7 | +4.43 | 24.6 | 1.22 | 61.1 | keep collecting (18/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 44.2 | 5.8 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 53-28 | 65.4 | 53.2 | 12.2 | +10.8 | 13.3 | 0.3 | 51.9 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 3-0 | 100.0 | 49.1 | 50.9 | +2.61 | 87.1 | 0.0 | 0.0 | keep collecting (3/30) |
| follow_move+money_delta | both | 5-3 | 62.5 | 41.0 | 21.5 | +3.95 | 49.4 | 0.05 | 37.5 | keep collecting (8/30) |
| money_delta+rlm_quiet | both | 2-2 | 50.0 | 37.9 | 12.1 | +1.53 | 38.3 | -2.1 | 0.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | both | 11-10 | 52.4 | 36.5 | 15.9 | +4.87 | 23.2 | 0.3 | 42.9 | keep collecting (21/30) |
| money_moving+rlm_ratio | both | 12-7 | 63.2 | 41.5 | 21.7 | +7.66 | 40.3 | 0.21 | 47.4 | keep collecting (19/30) |
| consensus_gap+rlm_ratio | both | 4-4 | 50.0 | 38.5 | 11.5 | +0.09 | 1.1 | 0.69 | 62.5 | keep collecting (8/30) |
| pin_move+pin_value | both | 1-4 | 20.0 | 49.1 | -29.1 | -3.09 | -61.8 | 0.2 | 20.0 | keep collecting (5/30) |
| follow_move+pin_move | both | 5-3 | 62.5 | 52.2 | 10.3 | +0.9 | 11.2 | 0.42 | 62.5 | keep collecting (8/30) |
| consensus_gap+pin_move | both | 0-5 | 0.0 | 44.5 | -44.5 | -5.0 | -100.0 | 0.26 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | both | 2-2 | 50.0 | 55.8 | -5.8 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 26.6 | 23.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 26.6 | 23.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | both | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.2 | -51.2 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 50.3 | -50.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-1 | 66.7 | 49.9 | 16.8 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 2-1 | 66.7 | 34.5 | 32.1 | +3.34 | 111.3 | 0.87 | 66.7 | keep collecting (3/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 16-24 | 40.0 | 26.6 | 13.4 | +9.89 | 24.7 | -0.05 | 45.0 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 11-10 | 52.4 | 50.2 | 2.2 | +0.04 | 0.2 | 0.86 | 52.4 | keep collecting (21/30) |
| pin_move | moneyline | 2-3 | 40.0 | 45.3 | -5.3 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-4 | 20.0 | 49.6 | -29.6 | -3.09 | -61.8 | 0.4 | 40.0 | keep collecting (5/30) |
| pin_move | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.14 | -3.5 | 0.25 | 50.0 | keep collecting (4/30) |
| money_delta | moneyline | 2-4 | 33.3 | 26.6 | 6.7 | +0.34 | 5.7 | -1.45 | 33.3 | keep collecting (6/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 7-2 | 77.8 | 50.2 | 27.6 | +4.26 | 47.4 | 0.44 | 22.2 | keep collecting (9/30) |
| pin_rlm | moneyline | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | moneyline | 195-126 | 60.7 | 56.9 | 3.8 | -24.09 | -7.5 | 0.19 | 46.1 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 128-140 | 47.8 | 49.7 | -1.9 | -22.21 | -8.3 | 0.02 | 34.3 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | total | 151-136 | 52.6 | 50.0 | 2.6 | +1.82 | 0.6 | 0.34 | 44.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | moneyline | 13-10 | 56.5 | 26.6 | 29.9 | +12.71 | 55.2 | 0.45 | 60.9 | keep collecting (23/30) |
| rlm_ratio | spread | 3-2 | 60.0 | 51.3 | 8.7 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 13-5 | 72.2 | 50.2 | 22.0 | +6.99 | 38.8 | 0.67 | 55.6 | keep collecting (18/30) |
| money_level | moneyline | 96-39 | 71.1 | 68.9 | 2.2 | -7.5 | -5.6 | -0.25 | 44.4 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-17 | 50.0 | 49.3 | 0.7 | -1.69 | -5.0 | 0.88 | 50.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | total | 56-53 | 51.4 | 49.9 | 1.5 | -2.14 | -2.0 | -0.28 | 29.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 61-61 | 50.0 | 46.6 | 3.4 | +3.59 | 2.9 | 0.32 | 50.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | spread | 20-14 | 58.8 | 49.8 | 9.1 | +4.0 | 11.8 | 0.65 | 38.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 62-45 | 57.9 | 50.1 | 7.9 | +11.5 | 10.7 | 0.13 | 37.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | moneyline | 44-41 | 51.8 | 53.0 | -1.3 | -12.4 | -14.6 | -0.15 | 47.1 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | spread | 18-5 | 78.3 | 49.2 | 29.1 | +11.18 | 48.6 | 0.3 | 43.5 | keep collecting (23/30) |
| money_moving | total | 40-34 | 54.1 | 50.0 | 4.0 | +2.41 | 3.3 | 0.18 | 35.1 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | moneyline | 2-6 | 25.0 | 32.5 | -7.5 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| pin_value | spread | 25-20 | 55.6 | 49.5 | 6.1 | +1.99 | 4.4 | 0.24 | 37.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 23-23 | 50.0 | 50.0 | 0.0 | -2.28 | -5.0 | -0.02 | 34.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.1 | -18.8 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 89-164 | 35.2 | 44.7 | -9.6 | -50.6 | -20.0 | 0.15 | 42.3 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 64-61 | 51.2 | 49.2 | 2.0 | -5.08 | -4.1 | 0.34 | 40.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap | total | 66-65 | 50.4 | 50.0 | 0.4 | -5.78 | -4.4 | 0.91 | 55.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | moneyline | 46-19 | 70.8 | 64.0 | 6.7 | -1.1 | -1.7 | 0.04 | 53.8 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+follow_move | moneyline | 11-22 | 33.3 | 53.5 | -20.2 | -14.69 | -44.5 | 0.2 | 54.5 | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 32.5 | -7.5 | -4.31 | -53.8 | -0.08 | 50.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| consensus_gap+rlm_quiet | moneyline | 1-5 | 16.7 | 26.6 | -10.0 | -3.68 | -61.3 | 1.07 | 83.3 | keep collecting (6/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.2 | -8.9 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 16-24 | 40.0 | 26.6 | 13.4 | +9.89 | 24.7 | -0.05 | 45.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 30-13 | 69.8 | 70.1 | -0.3 | -4.91 | -11.4 | -0.67 | 51.2 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 26.6 | -26.6 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 15-36 | 29.4 | 44.0 | -14.6 | -11.03 | -21.6 | 0.91 | 51.0 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | moneyline | 58-16 | 78.4 | 68.9 | 9.4 | -0.74 | -1.0 | -0.27 | 45.9 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 28-12 | 70.0 | 57.0 | 13.0 | +3.92 | 9.8 | 0.08 | 55.0 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 23-19 | 54.8 | 70.0 | -15.3 | -8.55 | -20.4 | 0.09 | 47.6 | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+sharp_gap | moneyline | 36-17 | 67.9 | 50.4 | 17.5 | +9.81 | 18.5 | 0.24 | 54.7 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 22-25 | 46.8 | 47.5 | -0.7 | -6.54 | -13.9 | 0.03 | 53.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | moneyline | 8-21 | 27.6 | 46.0 | -18.4 | -12.26 | -42.3 | 0.24 | 48.3 | keep collecting (29/30) |
| follow_move+rlm_ratio | moneyline | 13-10 | 56.5 | 26.6 | 29.9 | +12.71 | 55.2 | 0.45 | 60.9 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 9-7 | 56.2 | 26.6 | 29.6 | +10.84 | 67.8 | -0.23 | 50.0 | keep collecting (16/30) |
| rlm_quiet+sharp_gap | moneyline | 9-10 | 47.4 | 26.6 | 20.7 | +7.84 | 41.3 | -0.4 | 47.4 | keep collecting (19/30) |
| rlm_ratio+sharp_gap | moneyline | 13-10 | 56.5 | 26.6 | 29.9 | +12.71 | 55.2 | 0.45 | 60.9 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 26.6 | -1.6 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 5-7 | 41.7 | 26.6 | 15.0 | +2.49 | 20.8 | 0.44 | 50.0 | keep collecting (12/30) |
| money_moving+rlm_ratio | moneyline | 4-3 | 57.1 | 26.6 | 30.5 | +4.22 | 60.3 | 0.27 | 57.1 | keep collecting (7/30) |
| money_delta+money_moving | moneyline | 2-4 | 33.3 | 26.6 | 6.7 | +0.34 | 5.7 | -1.45 | 33.3 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-3 | 40.0 | 26.6 | 13.4 | +1.34 | 26.8 | -1.74 | 40.0 | keep collecting (5/30) |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 42.2 | -42.2 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-1 | 66.7 | 57.8 | 8.9 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | moneyline | 2-1 | 66.7 | 57.8 | 8.9 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-1 | 50.0 | 26.6 | 23.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-1 | 50.0 | 26.6 | 23.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | moneyline | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.13 | 56.5 | -0.1 | 50.0 | keep collecting (2/30) |
| money_level+rlm_ratio | moneyline | 4-3 | 57.1 | 26.6 | 30.5 | +1.87 | 26.7 | 2.0 | 85.7 | keep collecting (7/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 26.6 | 40.0 | +3.34 | 111.3 | -1.53 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 1-1 | 50.0 | 26.6 | 23.4 | +1.7 | 85.0 | -4.2 | 0.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 26.6 | 73.4 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-0 | 100.0 | 26.6 | 73.4 | +1.64 | 164.0 | 3.8 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 47.9 | -2.4 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 47.9 | 35.5 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 11-8 | 57.9 | 48.8 | 9.1 | +1.43 | 7.6 | 0.47 | 47.4 | keep collecting (19/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.3 | 8.7 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 48.9 | 13.6 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 10-5 | 66.7 | 48.7 | 17.9 | +4.12 | 27.5 | 0.93 | 66.7 | keep collecting (15/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 49.1 | -6.2 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 4-2 | 66.7 | 49.3 | 17.4 | +1.41 | 23.5 | 0.5 | 50.0 | keep collecting (6/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 51.3 | 8.7 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 52.1 | -52.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 52.1 | -52.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-11 | 56.0 | 49.2 | 6.8 | +1.62 | 6.5 | 1.0 | 44.0 | keep collecting (25/30) |
| money_moving+sharp_gap | spread | 10-3 | 76.9 | 49.2 | 27.7 | +6.04 | 46.4 | 0.54 | 46.2 | keep collecting (13/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.3 | 17.4 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-11 | 45.0 | 48.5 | -3.5 | -3.2 | -16.0 | 0.85 | 45.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 47.9 | 14.6 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 11-9 | 55.0 | 48.7 | 6.3 | +1.04 | 5.2 | 0.7 | 45.0 | keep collecting (20/30) |
| follow_move+pin_value | spread | 12-7 | 63.2 | 49.0 | 14.2 | +3.45 | 18.2 | 0.26 | 31.6 | keep collecting (19/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 47.9 | 52.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 47.9 | 52.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 47.9 | 52.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-2 | 81.8 | 48.3 | 33.6 | +6.22 | 56.6 | 0.36 | 45.5 | keep collecting (11/30) |
| money_delta+rlm_quiet | spread | 1-0 | 100.0 | 47.9 | 52.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 2-0 | 100.0 | 47.9 | 52.1 | +1.74 | 87.1 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 52.1 | 14.5 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | spread | 1-3 | 25.0 | 48.9 | -23.9 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 47.9 | -47.9 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-2 | 33.3 | 47.9 | -14.5 | -1.09 | -36.4 | 0.33 | 33.3 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.1 | -52.1 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 11-10 | 52.4 | 50.2 | 2.2 | +0.04 | 0.2 | 0.86 | 52.4 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 24-21 | 53.3 | 49.9 | 3.4 | +0.92 | 2.1 | -0.07 | 35.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | total | 37-30 | 55.2 | 50.0 | 5.3 | +3.65 | 5.4 | -0.09 | 32.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | total | 28-19 | 59.6 | 50.1 | 9.5 | +6.5 | 13.8 | 0.26 | 36.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 49.7 | -49.7 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 8-5 | 61.5 | 50.1 | 11.4 | +2.23 | 17.2 | 0.23 | 30.8 | keep collecting (13/30) |
| money_moving+pin_value | total | 5-4 | 55.6 | 50.1 | 5.5 | +0.47 | 5.2 | 0.11 | 22.2 | keep collecting (9/30) |
| pin_value+sharp_gap | total | 11-6 | 64.7 | 50.1 | 14.7 | +3.92 | 23.1 | -0.06 | 29.4 | keep collecting (17/30) |
| follow_move+money_level | total | 22-19 | 53.7 | 49.9 | 3.8 | +0.94 | 2.3 | 0.15 | 39.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 7-9 | 43.8 | 50.0 | -6.2 | -2.75 | -17.2 | -0.31 | 25.0 | keep collecting (16/30) |
| follow_move+rlm_ratio | total | 13-5 | 72.2 | 50.2 | 22.0 | +6.99 | 38.8 | 0.67 | 55.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 29-14 | 67.4 | 50.0 | 17.4 | +12.42 | 28.9 | 0.44 | 44.2 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 5-3 | 62.5 | 50.2 | 12.3 | +1.63 | 20.4 | 1.0 | 62.5 | keep collecting (8/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 50.1 | 16.6 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 13-5 | 72.2 | 50.2 | 22.0 | +6.99 | 38.8 | 0.67 | 55.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 16-14 | 53.3 | 50.0 | 3.3 | +0.65 | 2.2 | 0.57 | 50.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | total | 4-3 | 57.1 | 49.9 | 7.3 | +0.53 | 7.5 | -0.43 | 14.3 | keep collecting (7/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 49.8 | 30.2 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 49.9 | -16.6 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 6-6 | 50.0 | 50.1 | -0.1 | -0.58 | -4.8 | -0.08 | 25.0 | keep collecting (12/30) |
| money_moving+rlm_ratio | total | 6-4 | 60.0 | 50.2 | 9.8 | +1.58 | 15.8 | 0.4 | 50.0 | keep collecting (10/30) |
| consensus_gap+follow_move | total | 12-8 | 60.0 | 50.0 | 10.0 | +2.88 | 14.4 | 1.45 | 65.0 | keep collecting (20/30) |
| consensus_gap+money_delta | total | 2-0 | 100.0 | 49.7 | 50.3 | +1.78 | 88.9 | 0.0 | 0.0 | keep collecting (2/30) |
| follow_move+money_delta | total | 2-2 | 50.0 | 50.1 | -0.1 | -0.22 | -5.5 | 1.25 | 50.0 | keep collecting (4/30) |
| money_delta+money_moving | total | 6-2 | 75.0 | 50.1 | 24.9 | +3.35 | 41.9 | 0.5 | 25.0 | keep collecting (8/30) |
| money_delta+pin_value | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 | -0.5 | 0.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 5-1 | 83.3 | 50.1 | 33.2 | +3.44 | 57.4 | 0.67 | 33.3 | keep collecting (6/30) |
| money_moving+rlm_quiet | total | 4-3 | 57.1 | 50.2 | 6.9 | +0.64 | 9.1 | 0.43 | 42.9 | keep collecting (7/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 6-2 | 75.0 | 50.2 | 24.8 | +3.5 | 43.7 | 0.62 | 62.5 | keep collecting (8/30) |
| rlm_quiet+sharp_gap | total | 8-2 | 80.0 | 50.2 | 29.8 | +5.31 | 53.1 | 0.8 | 60.0 | keep collecting (10/30) |
| follow_move+pin_move | total | 2-0 | 100.0 | 50.3 | 49.7 | +1.86 | 93.0 | 1.0 | 100.0 | keep collecting (2/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 50.3 | -50.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 50.3 | -50.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 2-1 | 66.7 | 50.1 | 16.6 | +0.82 | 27.3 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 50.3 | -0.3 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 3-1 | 75.0 | 50.3 | 24.7 | +1.77 | 44.2 | 0.25 | 50.0 | keep collecting (4/30) |
| money_level+pin_move | total | 0-1 | 0.0 | 49.7 | -49.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_value | total | 0-1 | 0.0 | 49.7 | -49.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 49.7 | -49.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 50.3 | -50.3 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 0-1 | 0.0 | 50.3 | -50.3 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 182-256 | 41.6 | 41.9 | -0.3 | -33.92 | -7.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move | both | 496-500 | 49.8 | 49.9 | -0.1 | -33.5 | -3.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta | both | 316-422 | 42.8 | 44.0 | -1.2 | -57.17 | -7.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm | both | 140-161 | 46.5 | 42.2 | 4.4 | +27.28 | 9.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | both | 856-763 | 52.9 | 51.9 | 1.0 | -89.6 | -5.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | both | 200-225 | 47.1 | 44.6 | 2.5 | +1.15 | 0.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level | both | 1082-804 | 57.4 | 55.5 | 1.8 | -66.84 | -3.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 845-975 | 46.4 | 47.5 | -1.0 | -118.59 | -6.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | both | 846-975 | 46.5 | 47.8 | -1.3 | -126.2 | -6.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | both | 355-360 | 49.7 | 47.9 | 1.8 | +3.77 | 0.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 330-448 | 42.4 | 47.1 | -4.7 | -87.6 | -11.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+follow_move | both | 127-127 | 50.0 | 51.2 | -1.2 | -15.22 | -6.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | both | 147-241 | 37.9 | 44.3 | -6.4 | -31.8 | -8.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_move | both | 81-85 | 48.8 | 50.9 | -2.1 | +1.11 | 0.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | both | 23-40 | 36.5 | 37.0 | -0.5 | +9.03 | 14.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_value | both | 135-147 | 47.9 | 45.5 | 2.4 | +5.35 | 1.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | both | 25-43 | 36.8 | 39.7 | -2.9 | -1.66 | -2.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | both | 146-245 | 37.3 | 43.8 | -6.4 | -32.79 | -8.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_moving | both | 457-486 | 48.5 | 49.4 | -0.9 | -66.32 | -7.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_move | both | 357-356 | 50.1 | 50.3 | -0.2 | -32.74 | -4.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_rlm | both | 108-114 | 48.6 | 44.3 | 4.3 | +4.57 | 2.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | both | 125-121 | 50.8 | 48.9 | 1.9 | -9.65 | -3.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | both | 200-225 | 47.1 | 44.6 | 2.5 | +1.15 | 0.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 462-483 | 48.9 | 49.2 | -0.3 | -56.21 | -5.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_move | both | 299-331 | 47.5 | 48.6 | -1.2 | -27.98 | -4.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_rlm | both | 134-157 | 46.0 | 42.1 | 3.9 | +25.32 | 8.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_value | both | 157-186 | 45.8 | 47.2 | -1.4 | -15.12 | -4.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | both | 192-218 | 46.8 | 44.6 | 2.2 | +0.23 | 0.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+sharp_gap | both | 811-937 | 46.4 | 47.5 | -1.1 | -110.22 | -6.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_rlm | both | 129-134 | 49.0 | 44.2 | 4.8 | +21.5 | 8.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_value | both | 157-157 | 50.0 | 49.0 | 1.0 | -6.0 | -1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_ratio | both | 116-113 | 50.7 | 45.7 | 4.9 | +12.25 | 5.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | both | 306-332 | 48.0 | 48.6 | -0.6 | -22.74 | -3.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+pin_value | both | 40-42 | 48.8 | 45.7 | 3.1 | +11.58 | 14.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_ratio | both | 108-114 | 48.6 | 44.3 | 4.3 | +4.57 | 2.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | both | 140-161 | 46.5 | 42.2 | 4.4 | +27.28 | 9.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 38-33 | 53.5 | 48.7 | 4.8 | +1.73 | 2.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | both | 159-187 | 46.0 | 47.1 | -1.1 | -14.32 | -4.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio+sharp_gap | both | 200-225 | 47.1 | 44.6 | 2.5 | +1.15 | 0.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 151-176 | 46.2 | 46.0 | 0.2 | -22.47 | -6.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+money_moving | both | 596-531 | 52.9 | 52.4 | 0.5 | -46.31 | -4.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | both | 587-522 | 52.9 | 52.2 | 0.8 | -38.85 | -3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | both | 564-401 | 58.4 | 56.6 | 1.9 | -44.59 | -4.6 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 95-81 | 54.0 | 48.4 | 5.5 | +10.68 | 6.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | both | 202-165 | 55.0 | 57.9 | -2.9 | -23.58 | -6.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | both | 293-269 | 52.1 | 53.1 | -1.0 | -28.76 | -5.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | both | 174-159 | 52.3 | 49.8 | 2.4 | -7.73 | -2.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_quiet | both | 19-47 | 28.8 | 36.2 | -7.4 | -9.07 | -13.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_quiet | both | 182-256 | 41.6 | 41.9 | -0.3 | -33.92 | -7.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 98-149 | 39.7 | 41.9 | -2.2 | -20.73 | -8.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_moving | both | 226-330 | 40.6 | 42.4 | -1.8 | -48.17 | -8.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_delta | both | 41-109 | 27.3 | 36.7 | -9.3 | -30.68 | -20.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_level | both | 117-111 | 51.3 | 46.9 | 4.4 | +11.59 | 5.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | both | 68-72 | 48.6 | 46.9 | 1.7 | -6.57 | -4.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+sharp_gap | both | 223-325 | 40.7 | 42.5 | -1.8 | -46.34 | -8.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 79-122 | 39.3 | 40.4 | -1.1 | -11.64 | -5.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_quiet | both | 90-146 | 38.1 | 41.7 | -3.5 | -23.63 | -10.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+rlm_quiet | both | 49-87 | 36.0 | 42.8 | -6.7 | -30.79 | -22.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+rlm_quiet | both | 88-108 | 44.9 | 44.1 | 0.8 | -6.25 | -3.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_quiet | both | 42-64 | 39.6 | 40.7 | -1.1 | -10.48 | -9.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 118-139 | 45.9 | 46.5 | -0.5 | -9.93 | -3.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_rlm | both | 63-44 | 58.9 | 46.7 | 12.2 | +18.25 | 17.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_rlm | both | 82-95 | 46.3 | 42.3 | 4.0 | +11.43 | 6.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+rlm_ratio | both | 110-116 | 48.7 | 45.0 | 3.6 | -0.1 | -0.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+rlm_quiet | both | 24-36 | 40.0 | 47.2 | -7.2 | -13.58 | -22.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 50.3 | 49.7 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 52-110 | 32.1 | 27.5 | 4.6 | -7.46 | -4.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet | spread | 45-44 | 50.6 | 50.6 | -0.1 | -2.33 | -2.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_quiet | total | 85-102 | 45.5 | 50.1 | -4.7 | -24.13 | -12.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move | moneyline | 103-103 | 50.0 | 49.3 | 0.7 | +4.99 | 2.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move | spread | 194-208 | 48.3 | 50.2 | -1.9 | -31.15 | -7.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move | total | 199-189 | 51.3 | 50.1 | 1.2 | -7.34 | -1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | moneyline | 49-165 | 22.9 | 28.2 | -5.3 | -43.92 | -20.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta | spread | 122-125 | 49.4 | 50.8 | -1.4 | -13.91 | -5.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | total | 145-132 | 52.3 | 50.2 | 2.2 | +0.66 | 0.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm | moneyline | 38-74 | 33.9 | 28.3 | 5.6 | +20.97 | 18.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm | spread | 25-23 | 52.1 | 50.9 | 1.2 | -0.21 | -0.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm | total | 77-64 | 54.6 | 50.2 | 4.4 | +6.52 | 4.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | moneyline | 313-205 | 60.4 | 56.4 | 4.0 | -25.85 | -5.0 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 247-261 | 48.6 | 49.6 | -0.9 | -36.75 | -7.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | total | 296-297 | 49.9 | 50.0 | -0.1 | -27.0 | -4.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | moneyline | 37-80 | 31.6 | 29.8 | 1.8 | -2.78 | -2.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio | spread | 41-43 | 48.8 | 50.2 | -1.3 | -5.76 | -6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | total | 122-102 | 54.5 | 50.2 | 4.3 | +9.69 | 4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | moneyline | 416-157 | 72.6 | 69.0 | 3.6 | -22.78 | -4.0 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 315-326 | 49.1 | 49.3 | -0.2 | -41.85 | -6.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level | total | 351-321 | 52.2 | 49.9 | 2.3 | -2.21 | -0.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 201-326 | 38.1 | 41.6 | -3.5 | -54.15 | -10.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| sharp_gap | spread | 323-310 | 51.0 | 49.6 | 1.4 | -18.56 | -2.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 321-339 | 48.6 | 50.1 | -1.4 | -45.88 | -7.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | moneyline | 209-316 | 39.8 | 42.7 | -2.8 | -45.1 | -8.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | spread | 320-313 | 50.6 | 49.6 | 1.0 | -24.43 | -3.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | total | 317-346 | 47.8 | 50.1 | -2.2 | -56.67 | -8.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | moneyline | 18-54 | 25.0 | 30.5 | -5.5 | +10.87 | 15.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | spread | 159-148 | 51.8 | 49.6 | 2.2 | -9.27 | -3.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 178-158 | 53.0 | 50.0 | 3.0 | +2.17 | 0.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.1 | 47.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 140-272 | 34.0 | 44.9 | -10.9 | -77.34 | -18.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 85-75 | 53.1 | 49.3 | 3.9 | -2.53 | -1.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap | total | 105-101 | 51.0 | 49.8 | 1.1 | -7.73 | -3.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | moneyline | 145-83 | 63.6 | 63.1 | 0.5 | -6.7 | -2.9 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 136-81 | 62.7 | 62.6 | 0.1 | -6.32 | -2.9 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 187-302 | 38.2 | 41.5 | -3.3 | -41.39 | -8.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+follow_move | moneyline | 52-67 | 43.7 | 53.3 | -9.6 | -20.43 | -17.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 7-36 | 16.3 | 28.8 | -12.5 | -8.64 | -20.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 52-110 | 32.1 | 27.5 | 4.6 | -7.46 | -4.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 95-65 | 59.4 | 69.0 | -9.6 | -16.77 | -10.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 55-153 | 26.4 | 39.9 | -13.4 | -23.75 | -11.4 |  |  | !! CHECK: consensus_gap+money_moving close moneyline all sits -13.4 pts from its base (39.9%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | moneyline | 245-79 | 75.6 | 70.5 | 5.1 | -11.75 | -3.6 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 101-109 | 48.1 | 48.2 | -0.1 | -12.65 | -6.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_moving | moneyline | 46-148 | 23.7 | 27.8 | -4.1 | -29.89 | -15.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+sharp_gap | moneyline | 44-147 | 23.0 | 27.9 | -4.8 | -31.08 | -16.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 53-158 | 25.1 | 38.8 | -13.7 | -26.63 | -12.6 |  |  | !! CHECK: consensus_gap+sharp_gap close moneyline all sits -13.7 pts from its base (38.8%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+sharp_gap | moneyline | 98-108 | 47.6 | 47.3 | 0.3 | -12.08 | -5.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_quiet | moneyline | 23-67 | 25.6 | 27.7 | -2.1 | -5.91 | -6.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 24-68 | 26.1 | 27.6 | -1.6 | -7.45 | -8.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_move | moneyline | 28-36 | 43.8 | 52.9 | -9.2 | +3.93 | 6.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 10-29 | 25.6 | 29.0 | -3.4 | +8.65 | 22.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 4-30 | 11.8 | 29.4 | -17.6 | -7.04 | -20.7 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 83-68 | 55.0 | 51.4 | 3.6 | +5.35 | 3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_rlm | moneyline | 24-40 | 37.5 | 29.6 | 7.9 | +1.46 | 2.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 37-80 | 31.6 | 29.8 | 1.8 | -2.78 | -2.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 46-64 | 41.8 | 42.4 | -0.5 | +8.69 | 7.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_rlm | moneyline | 37-72 | 33.9 | 28.3 | 5.6 | +21.57 | 19.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 36-76 | 32.1 | 30.0 | 2.2 | -0.18 | -0.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_rlm | moneyline | 27-47 | 36.5 | 28.5 | 8.0 | +15.19 | 20.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 23-33 | 41.1 | 28.3 | 12.8 | +8.87 | 15.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 21-31 | 40.4 | 30.2 | 10.2 | +7.28 | 14.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+sharp_gap | moneyline | 46-65 | 41.4 | 41.8 | -0.3 | +7.51 | 6.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 14-33 | 29.8 | 28.6 | 1.2 | -5.18 | -11.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 24-40 | 37.5 | 29.6 | 7.9 | +1.46 | 2.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 38-74 | 33.9 | 28.3 | 5.6 | +20.97 | 18.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 23-65 | 26.1 | 27.7 | -1.6 | -5.91 | -6.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 37-80 | 31.6 | 29.8 | 1.8 | -2.78 | -2.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 11-81 | 12.0 | 28.2 | -16.2 | -28.62 | -31.1 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 13-45 | 22.4 | 29.9 | -7.4 | +1.38 | 2.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_move | moneyline | 16-35 | 31.4 | 30.3 | 1.1 | +0.84 | 1.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_rlm | moneyline | 22-44 | 33.3 | 28.8 | 4.6 | +7.63 | 11.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_value | moneyline | 2-18 | 10.0 | 26.6 | -16.6 | -11.18 | -55.9 |  |  | keep collecting (20/30) |
| money_moving+pin_value | moneyline | 10-33 | 23.3 | 29.9 | -6.6 | +8.44 | 19.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_value | moneyline | 6-9 | 40.0 | 32.9 | 7.1 | +7.27 | 48.5 |  |  | keep collecting (15/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 26.6 | 4.6 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 10-35 | 22.2 | 29.7 | -7.5 | +6.44 | 14.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_delta | moneyline | 23-47 | 32.9 | 30.6 | 2.2 | -10.09 | -14.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_level | moneyline | 14-23 | 37.8 | 30.4 | 7.4 | +6.11 | 16.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+rlm_ratio | moneyline | 21-38 | 35.6 | 30.6 | 5.0 | -3.0 | -5.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_move | moneyline | 67-42 | 61.5 | 66.9 | -5.5 | -6.77 | -6.2 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 11-9 | 55.0 | 31.3 | 23.7 | +5.77 | 28.8 |  |  | keep collecting (20/30) |
| money_level+rlm_ratio | moneyline | 13-11 | 54.2 | 38.3 | 15.9 | +6.1 | 25.4 |  |  | keep collecting (24/30) |
| money_delta+rlm_quiet | moneyline | 15-35 | 30.0 | 29.4 | 0.6 | -9.95 | -19.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_value | moneyline | 5-2 | 71.4 | 66.7 | 4.7 | +0.68 | 9.7 |  |  | keep collecting (7/30) |
| follow_move+pin_value | moneyline | 2-7 | 22.2 | 31.8 | -9.6 | -4.79 | -53.3 |  |  | keep collecting (9/30) |
| pin_value+rlm_quiet | moneyline | 1-6 | 14.3 | 26.6 | -12.3 | -4.48 | -64.0 |  |  | keep collecting (7/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 26.6 | -1.6 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 34-27 | 55.7 | 48.6 | 7.1 | +1.9 | 3.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | spread | 47-42 | 52.8 | 49.1 | 3.7 | -1.97 | -2.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_move | spread | 24-28 | 46.2 | 49.3 | -3.1 | -7.56 | -14.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 60-45 | 57.1 | 49.2 | 8.0 | +5.95 | 5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_ratio | spread | 4-4 | 50.0 | 50.0 | 0.0 | -0.67 | -8.3 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | spread | 46-42 | 52.3 | 49.2 | 3.0 | -2.86 | -3.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | spread | 157-160 | 49.5 | 49.3 | 0.2 | -18.11 | -5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_move | spread | 123-137 | 47.3 | 49.9 | -2.6 | -24.95 | -9.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_rlm | spread | 19-19 | 50.0 | 50.7 | -0.7 | -1.65 | -4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | spread | 56-51 | 52.3 | 49.1 | 3.3 | -2.23 | -2.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | spread | 41-43 | 48.8 | 50.2 | -1.3 | -5.76 | -6.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 158-159 | 49.8 | 49.4 | 0.5 | -15.97 | -5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_move | spread | 116-126 | 47.9 | 49.8 | -1.9 | -20.83 | -8.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | spread | 23-23 | 50.0 | 50.8 | -0.8 | -2.04 | -4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | spread | 79-80 | 49.7 | 49.3 | 0.4 | -11.83 | -7.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_ratio | spread | 39-42 | 48.1 | 50.1 | -1.9 | -6.69 | -8.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | spread | 315-305 | 50.8 | 49.6 | 1.2 | -20.93 | -3.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_rlm | spread | 25-23 | 52.1 | 50.9 | 1.2 | -0.21 | -0.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 72-80 | 47.4 | 49.7 | -2.4 | -16.54 | -10.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_ratio | spread | 22-26 | 45.8 | 50.5 | -4.7 | -5.94 | -12.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | spread | 119-126 | 48.6 | 49.9 | -1.3 | -18.1 | -7.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+pin_value | spread | 7-10 | 41.2 | 50.6 | -9.4 | -3.88 | -22.8 |  |  | keep collecting (17/30) |
| pin_rlm+rlm_ratio | spread | 19-19 | 50.0 | 50.7 | -0.7 | -1.65 | -4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | spread | 25-23 | 52.1 | 50.9 | 1.2 | -0.21 | -0.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 7-8 | 46.7 | 49.6 | -2.9 | -2.01 | -13.4 |  |  | keep collecting (15/30) |
| pin_value+sharp_gap | spread | 79-80 | 49.7 | 49.4 | 0.3 | -11.89 | -7.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | spread | 41-43 | 48.8 | 50.2 | -1.3 | -5.76 | -6.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 152-164 | 48.1 | 49.1 | -1.0 | -26.69 | -8.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+rlm_ratio | spread | 21-28 | 42.9 | 49.9 | -7.0 | -9.13 | -18.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | spread | 248-243 | 50.5 | 49.3 | 1.2 | -19.56 | -4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | spread | 56-46 | 54.9 | 48.9 | 6.0 | +1.89 | 1.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | spread | 247-244 | 50.3 | 49.3 | 1.0 | -21.47 | -4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | spread | 106-126 | 45.7 | 49.6 | -3.9 | -30.32 | -13.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_value | spread | 85-87 | 49.4 | 49.1 | 0.3 | -13.64 | -7.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_delta | spread | 14-14 | 50.0 | 50.5 | -0.5 | -2.09 | -7.5 |  |  | keep collecting (28/30) |
| follow_move+money_delta | spread | 38-47 | 44.7 | 50.2 | -5.5 | -12.62 | -14.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_level | spread | 40-40 | 50.0 | 50.1 | -0.1 | -3.96 | -4.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_moving | spread | 68-74 | 47.9 | 50.4 | -2.6 | -12.64 | -8.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | spread | 32-27 | 54.2 | 50.5 | 3.8 | +0.88 | 1.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+sharp_gap | spread | 67-72 | 48.2 | 50.4 | -2.2 | -11.62 | -8.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_quiet | spread | 45-44 | 50.6 | 50.6 | -0.1 | -2.33 | -2.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 14-4 | 77.8 | 50.7 | 27.1 | +8.78 | 48.8 |  |  | keep collecting (18/30) |
| rlm_quiet+sharp_gap | spread | 21-10 | 67.7 | 50.9 | 16.9 | +9.22 | 29.7 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+pin_rlm | spread | 14-11 | 56.0 | 50.4 | 5.6 | +1.57 | 6.3 |  |  | keep collecting (25/30) |
| money_delta+pin_move | spread | 36-45 | 44.4 | 50.9 | -6.4 | -12.09 | -14.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+rlm_ratio | spread | 16-26 | 38.1 | 50.0 | -11.9 | -11.78 | -28.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 52.1 | 47.9 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_rlm | spread | 13-16 | 44.8 | 50.7 | -5.8 | -4.31 | -14.8 |  |  | keep collecting (29/30) |
| money_delta+rlm_quiet | spread | 14-17 | 45.2 | 51.0 | -5.9 | -4.07 | -13.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_quiet | spread | 20-10 | 66.7 | 50.8 | 15.8 | +8.27 | 27.6 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| pin_move+rlm_quiet | spread | 26-21 | 55.3 | 51.0 | 4.3 | +3.15 | 6.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-2 | 75.0 | 51.6 | 23.4 | +3.56 | 44.5 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_quiet | spread | 2-3 | 40.0 | 50.4 | -10.4 | -1.33 | -26.7 |  |  | keep collecting (5/30) |
| pin_value+rlm_quiet | spread | 4-4 | 50.0 | 48.9 | 1.1 | -0.52 | -6.5 |  |  | keep collecting (8/30) |
| follow_move+money_delta | total | 90-82 | 52.3 | 50.1 | 2.2 | +0.24 | 0.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | total | 204-204 | 50.0 | 50.0 | 0.0 | -18.14 | -4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | total | 203-198 | 50.6 | 50.0 | 0.6 | -12.98 | -3.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | total | 309-330 | 48.4 | 50.1 | -1.7 | -47.91 | -7.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | total | 51-54 | 48.6 | 49.8 | -1.2 | -8.7 | -8.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_move | total | 29-21 | 58.0 | 49.9 | 8.1 | +4.74 | 9.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_value | total | 62-57 | 52.1 | 49.8 | 2.3 | -1.98 | -1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | total | 199-217 | 47.8 | 50.1 | -2.2 | -35.56 | -8.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+sharp_gap | total | 206-216 | 48.8 | 50.1 | -1.2 | -28.16 | -6.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | total | 120-101 | 54.3 | 50.0 | 4.3 | +8.33 | 3.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | total | 84-70 | 54.5 | 49.9 | 4.7 | +5.23 | 3.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_value | total | 79-68 | 53.7 | 50.0 | 3.7 | +3.27 | 2.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_quiet | total | 85-102 | 45.5 | 50.1 | -4.7 | -24.13 | -12.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 137-141 | 49.3 | 50.1 | -0.8 | -15.84 | -5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_quiet+sharp_gap | total | 53-71 | 42.7 | 50.2 | -7.4 | -22.49 | -18.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_moving | total | 112-108 | 50.9 | 50.2 | 0.7 | -5.64 | -2.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | total | 167-158 | 51.4 | 50.0 | 1.4 | -6.16 | -1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 67-63 | 51.5 | 50.0 | 1.6 | -2.62 | -2.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | total | 68-73 | 48.2 | 50.0 | -1.8 | -11.73 | -8.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | total | 70-72 | 49.3 | 50.0 | -0.7 | -8.87 | -6.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | total | 45-46 | 49.5 | 49.9 | -0.4 | -6.08 | -6.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+sharp_gap | total | 47-45 | 51.1 | 49.9 | 1.2 | -3.3 | -3.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+follow_move | total | 41-33 | 55.4 | 49.8 | 5.6 | +3.3 | 4.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_delta | total | 16-14 | 53.3 | 50.0 | 3.4 | +0.03 | 0.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_quiet | total | 10-8 | 55.6 | 50.0 | 5.5 | +0.9 | 5.0 |  |  | keep collecting (18/30) |
| money_delta+rlm_quiet | total | 20-35 | 36.4 | 50.2 | -13.9 | -16.76 | -30.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+sharp_gap | total | 112-106 | 51.4 | 50.2 | 1.2 | -3.64 | -1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_quiet | total | 47-69 | 40.5 | 50.2 | -9.7 | -25.99 | -22.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 63-48 | 56.8 | 50.1 | 6.6 | +9.44 | 8.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_move | total | 66-59 | 52.8 | 50.2 | 2.6 | +1.32 | 1.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | total | 141-141 | 50.0 | 50.1 | -0.1 | -12.15 | -4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_move | total | 151-151 | 50.0 | 50.1 | -0.1 | -13.15 | -4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+rlm_quiet | total | 19-26 | 42.2 | 50.1 | -7.9 | -8.58 | -19.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | total | 10-8 | 55.6 | 50.0 | 5.6 | +0.87 | 4.8 |  |  | keep collecting (18/30) |
| consensus_gap+rlm_ratio | total | 17-9 | 65.4 | 49.9 | 15.5 | +6.04 | 23.2 |  |  | keep collecting (26/30) |
| follow_move+pin_rlm | total | 65-55 | 54.2 | 50.2 | 4.0 | +4.75 | 4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | total | 122-102 | 54.5 | 50.2 | 4.3 | +9.69 | 4.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 38-24 | 61.3 | 50.2 | 11.1 | +10.91 | 17.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+rlm_ratio | total | 61-42 | 59.2 | 50.1 | 9.1 | +13.72 | 13.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | total | 74-62 | 54.4 | 50.2 | 4.2 | +5.79 | 4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_ratio | total | 117-100 | 53.9 | 50.2 | 3.8 | +7.11 | 3.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_rlm | total | 77-64 | 54.6 | 50.2 | 4.4 | +6.52 | 4.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 73-56 | 56.6 | 50.2 | 6.4 | +10.92 | 8.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+pin_value | total | 28-21 | 57.1 | 50.1 | 7.0 | +4.4 | 9.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_ratio | total | 65-55 | 54.2 | 50.2 | 4.0 | +4.75 | 4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | total | 77-64 | 54.6 | 50.2 | 4.4 | +6.52 | 4.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 30-22 | 57.7 | 50.1 | 7.6 | +5.22 | 10.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | total | 122-102 | 54.5 | 50.2 | 4.3 | +9.69 | 4.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 47-35 | 57.3 | 50.2 | 7.1 | +8.11 | 9.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+rlm_ratio | total | 73-52 | 58.4 | 50.2 | 8.2 | +14.68 | 11.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | total | 34-27 | 55.7 | 50.1 | 5.6 | +3.73 | 6.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_quiet | total | 39-54 | 41.9 | 50.1 | -8.2 | -18.27 | -19.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_quiet | total | 22-29 | 43.1 | 50.2 | -7.1 | -8.86 | -17.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_quiet+rlm_ratio | total | 42-53 | 44.2 | 50.2 | -6.0 | -14.5 | -15.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 50.3 | 49.7 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

# Pooled (fit + forward together)

Kept for continuity. **Contaminated** — it mixes the games the engine was built
on with the games testing it. Use the forward table for any decision.

## EARLY  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 38-48 | 44.2 | 36.7 | 7.4 | +8.39 | 9.8 | 0.22 | 43.0 | DROP: below break-even |
| pin_move | both | 9-13 | 40.9 | 48.7 | -7.8 | -5.46 | -24.8 | 0.05 | 36.4 | keep collecting (22/30) |
| money_delta | both | 11-8 | 57.9 | 42.7 | 15.2 | +4.34 | 22.9 | -0.04 | 36.8 | keep collecting (19/30) |
| pin_rlm | both | 1-3 | 25.0 | 39.1 | -14.1 | -2.07 | -51.8 | -0.37 | 75.0 | keep collecting (4/30) |
| follow_move | both | 554-499 | 52.6 | 51.6 | 1.0 | -65.48 | -6.2 | 0.19 | 41.1 | no edge shown yet |
| rlm_ratio | both | 34-24 | 58.6 | 40.1 | 18.6 | +18.93 | 32.6 | 0.5 | 53.4 | no edge shown yet |
| money_level | both | 190-129 | 59.6 | 58.8 | 0.8 | -18.45 | -5.8 | -0.1 | 39.2 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 158-139 | 53.2 | 48.2 | 5.0 | +14.71 | 5.0 | 0.29 | 43.8 | no edge shown yet |
| money_moving | both | 120-96 | 55.6 | 51.1 | 4.5 | +1.07 | 0.5 | 0.13 | 43.1 | no edge shown yet |
| pin_value | both | 60-58 | 50.8 | 48.7 | 2.2 | -4.74 | -4.0 | 0.03 | 35.6 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.9 | -31.9 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 273-331 | 45.2 | 48.0 | -2.8 | -56.8 | -9.4 | 0.38 | 45.4 | DROP: below break-even |
| consensus_gap+money_level | both | 40-33 | 54.8 | 62.1 | -7.3 | -10.72 | -14.7 | 0.22 | 46.6 | no edge shown yet |
| consensus_gap+money_moving | both | 21-25 | 45.7 | 47.7 | -2.1 | -6.26 | -13.6 | 0.26 | 43.5 | no edge shown yet |
| consensus_gap+pin_value | both | 24-29 | 45.3 | 47.0 | -1.7 | -8.11 | -15.3 | 0.37 | 47.2 | no edge shown yet |
| follow_move+rlm_quiet | both | 38-48 | 44.2 | 36.7 | 7.4 | +8.39 | 9.8 | 0.22 | 43.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 34-24 | 58.6 | 40.1 | 18.6 | +18.93 | 32.6 | 0.5 | 53.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 81-47 | 63.3 | 49.4 | 13.9 | +21.62 | 16.9 | 0.41 | 48.4 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 73-48 | 60.3 | 57.9 | 2.4 | -3.14 | -2.6 | -0.08 | 46.3 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 13-10 | 56.5 | 50.3 | 6.2 | +1.63 | 7.1 | 0.47 | 47.8 | keep collecting (23/30) |
| money_moving+pin_value | both | 10-7 | 58.8 | 50.6 | 8.2 | +1.78 | 10.5 | 0.39 | 41.2 | keep collecting (17/30) |
| rlm_quiet+rlm_ratio | both | 20-14 | 58.8 | 36.8 | 22.0 | +14.73 | 43.3 | -0.04 | 47.1 | no edge shown yet |
| rlm_quiet+sharp_gap | both | 22-18 | 55.0 | 37.1 | 17.9 | +12.55 | 31.4 | -0.06 | 45.0 | no edge shown yet |
| rlm_ratio+sharp_gap | both | 34-24 | 58.6 | 40.1 | 18.6 | +18.93 | 32.6 | 0.5 | 53.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 104-70 | 59.8 | 55.3 | 4.4 | -0.4 | -0.2 | 0.16 | 44.3 | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | both | 71-57 | 55.5 | 48.8 | 6.7 | +7.27 | 5.7 | 0.28 | 46.9 | no edge shown yet |
| money_delta+money_level | both | 4-3 | 57.1 | 46.9 | 10.3 | +1.37 | 19.5 | 1.26 | 71.4 | keep collecting (7/30) |
| money_delta+money_moving | both | 10-8 | 55.6 | 42.4 | 13.2 | +3.43 | 19.1 | -0.04 | 38.9 | keep collecting (18/30) |
| money_delta+pin_value | both | 4-1 | 80.0 | 49.8 | 30.2 | +2.52 | 50.4 | 0.2 | 40.0 | keep collecting (5/30) |
| money_delta+sharp_gap | both | 8-6 | 57.1 | 42.1 | 15.0 | +3.69 | 26.4 | -0.05 | 50.0 | keep collecting (14/30) |
| pin_value+sharp_gap | both | 14-9 | 60.9 | 49.7 | 11.2 | +3.57 | 15.5 | -0.05 | 39.1 | keep collecting (23/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 37-46 | 44.6 | 51.3 | -6.7 | -16.34 | -19.7 | 0.75 | 56.6 | no edge shown yet |
| consensus_gap+rlm_quiet | both | 4-7 | 36.4 | 37.4 | -1.0 | -2.99 | -27.1 | 0.95 | 72.7 | keep collecting (11/30) |
| follow_move+pin_value | both | 23-21 | 52.3 | 48.7 | 3.6 | -0.86 | -2.0 | -0.21 | 27.3 | no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 42.7 | -26.1 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 30-48 | 38.5 | 45.7 | -7.2 | -10.13 | -13.0 | 0.81 | 50.0 | DROP: below break-even |
| follow_move+money_level | both | 96-52 | 64.9 | 59.6 | 5.2 | -4.25 | -2.9 | 0.04 | 43.2 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 12-10 | 54.5 | 44.2 | 10.3 | +2.34 | 10.6 | 1.43 | 68.2 | keep collecting (22/30) |
| pin_value+rlm_ratio | both | 3-2 | 60.0 | 45.2 | 14.8 | +0.73 | 14.5 | -1.16 | 40.0 | keep collecting (5/30) |
| follow_move+money_moving | both | 62-37 | 62.6 | 52.3 | 10.3 | +9.57 | 9.7 | 0.39 | 51.5 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 4-0 | 100.0 | 49.5 | 50.5 | +3.52 | 88.0 | 0.25 | 25.0 | keep collecting (4/30) |
| follow_move+money_delta | both | 6-4 | 60.0 | 42.7 | 17.3 | +3.86 | 38.6 | 0.34 | 50.0 | keep collecting (10/30) |
| money_delta+rlm_quiet | both | 2-2 | 50.0 | 38.0 | 12.0 | +1.53 | 38.3 | -2.1 | 0.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | both | 16-14 | 53.3 | 37.8 | 15.6 | +7.23 | 24.1 | 0.5 | 46.7 | no edge shown yet |
| money_moving+rlm_ratio | both | 17-10 | 63.0 | 42.4 | 20.6 | +10.06 | 37.3 | 0.61 | 55.6 | keep collecting (27/30) |
| consensus_gap+rlm_ratio | both | 5-4 | 55.6 | 39.7 | 15.9 | +1.0 | 11.1 | 0.72 | 66.7 | keep collecting (9/30) |
| pin_move+pin_value | both | 3-7 | 30.0 | 49.2 | -19.2 | -4.27 | -42.7 | -0.1 | 10.0 | keep collecting (10/30) |
| follow_move+pin_move | both | 6-6 | 50.0 | 50.5 | -0.5 | -1.19 | -9.9 | 0.45 | 50.0 | keep collecting (12/30) |
| consensus_gap+pin_move | both | 1-5 | 16.7 | 45.5 | -28.8 | -4.09 | -68.2 | 0.22 | 50.0 | keep collecting (6/30) |
| money_level+pin_move | both | 3-2 | 60.0 | 54.8 | 5.2 | +0.04 | 0.8 | 0.08 | 40.0 | keep collecting (5/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 28.2 | -28.2 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-2 | 33.3 | 42.7 | -9.4 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 28.2 | -28.2 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 28.2 | -28.2 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-2 | 33.3 | 42.7 | -9.4 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+sharp_gap | both | 1-3 | 25.0 | 39.1 | -14.1 | -2.07 | -51.8 | -0.37 | 75.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.0 | -51.0 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-1 | 66.7 | 50.4 | 16.3 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+pin_rlm | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.07 | -3.7 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 28.2 | 71.8 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 28.2 | 71.8 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 3-2 | 60.0 | 40.6 | 19.4 | +3.25 | 65.0 | 1.12 | 80.0 | keep collecting (5/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 28.2 | -28.2 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 20-31 | 39.2 | 28.2 | 11.0 | +9.1 | 17.8 | 0.03 | 43.1 | DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.4 | 10.6 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 15-15 | 50.0 | 49.2 | 0.8 | -1.36 | -4.5 | 0.7 | 50.0 | no edge shown yet |
| pin_move | moneyline | 2-3 | 40.0 | 45.6 | -5.6 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-6 | 14.3 | 48.6 | -34.4 | -5.09 | -72.7 | 0.29 | 28.6 | keep collecting (7/30) |
| pin_move | total | 6-4 | 60.0 | 50.2 | 9.8 | +1.5 | 15.0 | -0.1 | 30.0 | keep collecting (10/30) |
| money_delta | moneyline | 2-4 | 33.3 | 28.2 | 5.2 | +0.34 | 5.7 | -1.45 | 33.3 | keep collecting (6/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 8-3 | 72.7 | 49.3 | 23.4 | +4.17 | 37.9 | 0.64 | 36.4 | keep collecting (11/30) |
| pin_rlm | moneyline | 1-3 | 25.0 | 39.1 | -14.1 | -2.07 | -51.8 | -0.37 | 75.0 | keep collecting (4/30) |
| follow_move | moneyline | 228-153 | 59.8 | 54.6 | 5.2 | -18.34 | -4.8 | 0.14 | 44.1 | PROMOTE: beats break-even and its own base rate |
| follow_move | spread | 149-171 | 46.6 | 49.7 | -3.2 | -33.69 | -10.5 | 0.01 | 33.4 | DROP: below break-even |
| follow_move | total | 177-175 | 50.3 | 50.0 | 0.3 | -13.45 | -3.8 | 0.4 | 44.9 | no edge shown yet |
| rlm_ratio | moneyline | 14-14 | 50.0 | 29.7 | 20.3 | +10.47 | 37.4 | 0.47 | 57.1 | keep collecting (28/30) |
| rlm_ratio | spread | 3-3 | 50.0 | 52.1 | -2.1 | -0.16 | -2.7 | 0.33 | 16.7 | keep collecting (6/30) |
| rlm_ratio | total | 17-7 | 70.8 | 49.1 | 21.8 | +8.62 | 35.9 | 0.58 | 58.3 | keep collecting (24/30) |
| money_level | moneyline | 108-49 | 68.8 | 67.7 | 1.1 | -12.83 | -8.2 | -0.27 | 42.0 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-18 | 48.6 | 49.0 | -0.4 | -2.69 | -7.7 | 1.0 | 51.4 | no edge shown yet |
| money_level | total | 65-62 | 51.2 | 50.5 | 0.6 | -2.92 | -2.3 | -0.2 | 32.3 | no edge shown yet |
| sharp_gap | moneyline | 67-72 | 48.2 | 46.4 | 1.8 | -1.01 | -0.7 | 0.35 | 50.4 | no edge shown yet |
| sharp_gap | spread | 20-15 | 57.1 | 49.7 | 7.4 | +3.0 | 8.6 | 0.77 | 40.0 | no edge shown yet |
| sharp_gap | total | 71-52 | 57.7 | 49.8 | 8.0 | +12.71 | 10.3 | 0.09 | 37.4 | no edge shown yet |
| money_moving | moneyline | 53-49 | 52.0 | 52.6 | -0.6 | -12.73 | -12.5 | 0.03 | 49.0 | no edge shown yet |
| money_moving | spread | 18-6 | 75.0 | 48.9 | 26.1 | +10.18 | 42.4 | 0.5 | 45.8 | keep collecting (24/30) |
| money_moving | total | 49-41 | 54.4 | 49.9 | 4.5 | +3.63 | 4.0 | 0.14 | 35.6 | no edge shown yet |
| pin_value | moneyline | 2-7 | 22.2 | 37.9 | -15.7 | -5.31 | -59.0 | 0.12 | 55.6 | keep collecting (9/30) |
| pin_value | spread | 30-26 | 53.6 | 49.1 | 4.5 | +0.3 | 0.5 | 0.16 | 33.9 | no edge shown yet |
| pin_value | total | 28-25 | 52.8 | 50.1 | 2.8 | +0.26 | 0.5 | -0.11 | 34.0 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 53.2 | -19.8 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 111-183 | 37.8 | 46.4 | -8.7 | -52.48 | -17.9 | 0.1 | 42.2 | DROP: below break-even |
| consensus_gap | spread | 77-71 | 52.0 | 48.9 | 3.1 | -3.65 | -2.5 | 0.34 | 39.9 | no edge shown yet |
| consensus_gap | total | 85-77 | 52.5 | 50.1 | 2.4 | -0.66 | -0.4 | 0.93 | 56.2 | no edge shown yet |
| money_level+sharp_gap | moneyline | 49-24 | 67.1 | 62.9 | 4.3 | -4.34 | -5.9 | 0.05 | 53.4 | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+follow_move | moneyline | 14-23 | 37.8 | 54.1 | -16.3 | -13.83 | -37.4 | 0.17 | 54.1 | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 33.6 | -8.6 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| consensus_gap+rlm_quiet | moneyline | 1-5 | 16.7 | 28.2 | -11.5 | -3.68 | -61.3 | 1.07 | 83.3 | keep collecting (6/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.7 | -9.4 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 20-31 | 39.2 | 28.2 | 11.0 | +9.1 | 17.8 | 0.03 | 43.1 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 35-17 | 67.3 | 68.5 | -1.2 | -6.85 | -13.2 | -0.5 | 48.1 | beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 28.2 | -28.2 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 18-38 | 32.1 | 44.5 | -12.4 | -10.77 | -19.2 | 0.78 | 50.0 | DROP: below break-even |
| follow_move+money_level | moneyline | 61-19 | 76.2 | 68.0 | 8.2 | -3.05 | -3.8 | -0.3 | 43.8 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 33-15 | 68.8 | 55.5 | 13.3 | +5.06 | 10.5 | 0.18 | 54.2 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 29-23 | 55.8 | 67.6 | -11.9 | -10.38 | -20.0 | -0.06 | 44.2 | no edge shown yet |
| follow_move+sharp_gap | moneyline | 37-21 | 63.8 | 49.2 | 14.5 | +7.57 | 13.0 | 0.27 | 53.4 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 26-30 | 46.4 | 47.7 | -1.2 | -6.66 | -11.9 | 0.23 | 55.4 | no edge shown yet |
| consensus_gap+money_moving | moneyline | 11-23 | 32.4 | 47.4 | -15.1 | -13.01 | -38.3 | 0.24 | 47.1 | INVERT candidate: wrong well beyond its base rate |
| follow_move+rlm_ratio | moneyline | 14-14 | 50.0 | 29.7 | 20.3 | +10.47 | 37.4 | 0.47 | 57.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 10-10 | 50.0 | 28.2 | 21.8 | +9.6 | 48.0 | -0.12 | 45.0 | keep collecting (20/30) |
| rlm_quiet+sharp_gap | moneyline | 10-13 | 43.5 | 28.2 | 15.3 | +6.6 | 28.7 | -0.27 | 43.5 | keep collecting (23/30) |
| rlm_ratio+sharp_gap | moneyline | 14-14 | 50.0 | 29.7 | 20.3 | +10.47 | 37.4 | 0.47 | 57.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 28.2 | -3.2 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 7-9 | 43.8 | 28.2 | 15.6 | +4.13 | 25.8 | 0.75 | 56.2 | keep collecting (16/30) |
| money_moving+rlm_ratio | moneyline | 5-4 | 55.6 | 28.2 | 27.4 | +4.98 | 55.3 | 0.39 | 55.6 | keep collecting (9/30) |
| money_delta+money_moving | moneyline | 2-4 | 33.3 | 28.2 | 5.2 | +0.34 | 5.7 | -1.45 | 33.3 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-3 | 40.0 | 28.2 | 11.8 | +1.34 | 26.8 | -1.74 | 40.0 | keep collecting (5/30) |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 42.7 | -42.7 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-1 | 66.7 | 57.3 | 9.4 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | moneyline | 2-1 | 66.7 | 57.3 | 9.4 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 28.2 | -28.2 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-2 | 33.3 | 42.7 | -9.4 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 28.2 | -28.2 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 28.2 | -28.2 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-2 | 33.3 | 42.7 | -9.4 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+sharp_gap | moneyline | 1-3 | 25.0 | 39.1 | -14.1 | -2.07 | -51.8 | -0.37 | 75.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 28.2 | -28.2 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | -1.55 | 50.0 | keep collecting (2/30) |
| pin_move+sharp_gap | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.13 | 56.5 | -0.1 | 50.0 | keep collecting (2/30) |
| money_level+rlm_ratio | moneyline | 4-4 | 50.0 | 33.6 | 16.4 | +0.87 | 10.8 | 1.94 | 87.5 | keep collecting (8/30) |
| money_level+pin_rlm | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.07 | -3.7 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+pin_rlm | moneyline | 1-0 | 100.0 | 28.2 | 71.8 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 1-0 | 100.0 | 28.2 | 71.8 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 28.2 | 38.5 | +3.34 | 111.3 | -1.53 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 1-1 | 50.0 | 28.2 | 21.8 | +1.7 | 85.0 | -4.2 | 0.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 28.2 | 71.8 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 28.2 | -28.2 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-0 | 100.0 | 28.2 | 71.8 | +1.64 | 164.0 | 3.8 | 100.0 | keep collecting (1/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 71.8 | -71.8 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 71.8 | -71.8 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 46.8 | -1.4 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 46.8 | 36.5 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 12-9 | 57.1 | 48.3 | 8.8 | +1.3 | 6.2 | 0.38 | 42.9 | keep collecting (21/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.4 | 10.6 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-3 | 50.0 | 52.1 | -2.1 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-7 | 58.8 | 48.7 | 10.1 | +2.09 | 12.3 | 0.88 | 41.2 | keep collecting (17/30) |
| money_level+money_moving | spread | 10-6 | 62.5 | 48.4 | 14.1 | +3.12 | 19.5 | 1.19 | 68.8 | keep collecting (16/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.6 | -5.8 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 4-2 | 66.7 | 48.9 | 17.7 | +1.41 | 23.5 | 0.5 | 50.0 | keep collecting (6/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 3-3 | 50.0 | 52.1 | -2.1 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 53.2 | -53.2 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 53.2 | -53.2 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-12 | 53.8 | 49.0 | 4.8 | +0.62 | 2.4 | 1.15 | 46.2 | keep collecting (26/30) |
| money_moving+sharp_gap | spread | 10-4 | 71.4 | 49.1 | 22.3 | +5.04 | 36.0 | 0.86 | 50.0 | keep collecting (14/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 48.9 | 17.7 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-11 | 45.0 | 47.8 | -2.8 | -3.2 | -16.0 | 0.85 | 45.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 46.8 | 15.7 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 11-10 | 52.4 | 48.3 | 4.0 | +0.04 | 0.2 | 0.9 | 47.6 | keep collecting (21/30) |
| follow_move+pin_value | spread | 13-8 | 61.9 | 48.3 | 13.6 | +3.36 | 16.0 | 0.19 | 28.6 | keep collecting (21/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 46.8 | 53.2 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 46.8 | 53.2 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 46.8 | 53.2 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-3 | 75.0 | 47.9 | 27.1 | +5.22 | 43.5 | 0.75 | 50.0 | keep collecting (12/30) |
| money_delta+rlm_quiet | spread | 1-0 | 100.0 | 46.8 | 53.2 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 2-0 | 100.0 | 46.8 | 53.2 | +1.74 | 87.1 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 2-2 | 50.0 | 53.2 | -3.2 | -0.07 | -1.7 | 1.25 | 25.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | spread | 2-1 | 66.7 | 51.1 | 15.6 | +0.86 | 28.7 | 1.0 | 33.3 | keep collecting (3/30) |
| pin_move+pin_value | spread | 1-5 | 16.7 | 47.9 | -31.2 | -4.09 | -68.2 | 0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 46.8 | -46.8 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-3 | 25.0 | 46.8 | -21.8 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 53.2 | -53.2 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 15-15 | 50.0 | 49.2 | 0.8 | -1.36 | -4.5 | 0.7 | 50.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 28-25 | 52.8 | 50.4 | 2.5 | +0.59 | 1.1 | -0.04 | 37.7 | no edge shown yet |
| money_level+sharp_gap | total | 41-34 | 54.7 | 50.2 | 4.4 | +3.32 | 4.4 | -0.09 | 34.7 | no edge shown yet |
| money_moving+sharp_gap | total | 35-23 | 60.3 | 49.7 | 10.6 | +8.9 | 15.3 | 0.19 | 37.9 | no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 10-5 | 66.7 | 49.6 | 17.0 | +4.05 | 27.0 | 0.27 | 33.3 | keep collecting (15/30) |
| money_moving+pin_value | total | 6-4 | 60.0 | 49.6 | 10.4 | +1.38 | 13.8 | 0.2 | 30.0 | keep collecting (10/30) |
| pin_value+sharp_gap | total | 12-6 | 66.7 | 49.8 | 16.9 | +4.83 | 26.8 | 0.0 | 33.3 | keep collecting (18/30) |
| follow_move+money_level | total | 24-23 | 51.1 | 50.5 | 0.6 | -1.24 | -2.6 | 0.21 | 40.4 | no edge shown yet |
| follow_move+pin_value | total | 9-11 | 45.0 | 50.0 | -5.0 | -2.94 | -14.7 | -0.45 | 25.0 | keep collecting (20/30) |
| follow_move+rlm_ratio | total | 17-7 | 70.8 | 49.1 | 21.8 | +8.62 | 35.9 | 0.58 | 58.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 34-19 | 64.2 | 49.8 | 14.3 | +11.96 | 22.6 | 0.42 | 45.3 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 6-4 | 60.0 | 49.1 | 10.9 | +1.54 | 15.4 | 1.1 | 70.0 | keep collecting (10/30) |
| pin_value+rlm_ratio | total | 3-1 | 75.0 | 49.4 | 25.6 | +1.73 | 43.2 | -0.25 | 50.0 | keep collecting (4/30) |
| rlm_ratio+sharp_gap | total | 17-7 | 70.8 | 49.1 | 21.8 | +8.62 | 35.9 | 0.58 | 58.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 20-19 | 51.3 | 49.8 | 1.5 | -0.71 | -1.8 | 0.54 | 48.7 | no edge shown yet |
| consensus_gap+money_level | total | 6-4 | 60.0 | 50.4 | 9.6 | +1.34 | 13.4 | 0.0 | 30.0 | keep collecting (10/30) |
| consensus_gap+money_moving | total | 5-1 | 83.3 | 50.4 | 33.0 | +3.43 | 57.2 | -0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+pin_value | total | 10-14 | 41.7 | 50.3 | -8.6 | -5.11 | -21.3 | 0.5 | 50.0 | keep collecting (24/30) |
| consensus_gap+sharp_gap | total | 7-7 | 50.0 | 49.7 | 0.3 | -0.67 | -4.8 | 0.14 | 35.7 | keep collecting (14/30) |
| money_moving+rlm_ratio | total | 10-5 | 66.7 | 49.2 | 17.5 | +4.22 | 28.1 | 0.67 | 60.0 | keep collecting (15/30) |
| consensus_gap+follow_move | total | 14-12 | 53.8 | 49.9 | 3.9 | +0.69 | 2.7 | 1.5 | 69.2 | keep collecting (26/30) |
| consensus_gap+money_delta | total | 3-0 | 100.0 | 50.4 | 49.6 | +2.69 | 89.6 | 0.33 | 33.3 | keep collecting (3/30) |
| follow_move+money_delta | total | 3-3 | 50.0 | 49.3 | 0.7 | -0.31 | -5.2 | 1.33 | 66.7 | keep collecting (6/30) |
| money_delta+money_moving | total | 7-3 | 70.0 | 49.3 | 20.7 | +3.26 | 32.6 | 0.7 | 40.0 | keep collecting (10/30) |
| money_delta+pin_value | total | 3-0 | 100.0 | 49.6 | 50.4 | +2.69 | 89.6 | 0.0 | 33.3 | keep collecting (3/30) |
| money_delta+sharp_gap | total | 6-2 | 75.0 | 49.4 | 25.6 | +3.35 | 41.9 | 0.88 | 50.0 | keep collecting (8/30) |
| money_moving+rlm_quiet | total | 7-5 | 58.3 | 49.1 | 9.3 | +1.36 | 11.4 | 0.42 | 41.7 | keep collecting (12/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 9-3 | 75.0 | 49.1 | 25.9 | +5.22 | 43.5 | 0.33 | 58.3 | keep collecting (12/30) |
| rlm_quiet+sharp_gap | total | 11-4 | 73.3 | 49.0 | 24.3 | +6.04 | 40.3 | 0.47 | 53.3 | keep collecting (15/30) |
| follow_move+pin_move | total | 3-2 | 60.0 | 49.3 | 10.7 | +0.77 | 15.4 | 0.8 | 60.0 | keep collecting (5/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 3-2 | 60.0 | 49.3 | 10.7 | +0.73 | 14.5 | 0.8 | 60.0 | keep collecting (5/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 48.9 | 1.1 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 4-1 | 80.0 | 48.9 | 31.1 | +2.68 | 53.6 | 0.4 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | total | 1-1 | 50.0 | 51.1 | -1.1 | -0.09 | -4.5 | 0.0 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | total | 2-2 | 50.0 | 51.1 | -1.1 | -0.18 | -4.5 | -0.5 | 0.0 | keep collecting (4/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 1-2 | 33.3 | 48.9 | -15.6 | -1.09 | -36.4 | 1.67 | 100.0 | keep collecting (3/30) |
| consensus_gap+pin_move | total | 1-0 | 100.0 | 51.1 | 48.9 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 224-338 | 39.9 | 42.0 | -2.2 | -60.73 | -10.8 |  |  | DROP: below break-even |
| pin_move | both | 576-589 | 49.4 | 49.8 | -0.3 | -46.59 | -4.0 |  |  | DROP: below break-even |
| money_delta | both | 364-475 | 43.4 | 44.2 | -0.8 | -59.63 | -7.1 |  |  | DROP: below break-even |
| pin_rlm | both | 155-184 | 45.7 | 42.2 | 3.6 | +20.8 | 6.1 |  |  | DROP: below break-even |
| follow_move | both | 987-927 | 51.6 | 51.3 | 0.2 | -129.1 | -6.7 |  |  | no edge shown yet |
| rlm_ratio | both | 226-273 | 45.3 | 43.8 | 1.4 | -20.09 | -4.0 |  |  | DROP: below break-even |
| money_level | both | 1258-924 | 57.7 | 55.4 | 2.3 | -61.08 | -2.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 975-1117 | 46.6 | 47.5 | -0.9 | -139.36 | -6.7 |  |  | DROP: below break-even |
| money_moving | both | 980-1117 | 46.7 | 47.8 | -1.1 | -146.42 | -7.0 |  |  | DROP: below break-even |
| pin_value | both | 427-410 | 51.0 | 48.3 | 2.7 | +33.07 | 4.0 |  |  | no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 51.1 | 15.6 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 399-486 | 45.1 | 48.3 | -3.2 | -67.16 | -7.6 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 149-140 | 51.6 | 51.4 | 0.2 | -10.16 | -3.5 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 173-262 | 39.8 | 45.6 | -5.8 | -26.53 | -6.1 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 98-91 | 51.9 | 50.8 | 1.0 | +12.44 | 6.6 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 25-42 | 37.3 | 38.3 | -1.0 | +10.43 | 15.6 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 160-160 | 50.0 | 46.3 | 3.7 | +18.12 | 5.7 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | both | 30-47 | 39.0 | 39.9 | -1.0 | +0.39 | 0.5 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 172-266 | 39.3 | 45.0 | -5.8 | -27.24 | -6.2 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 518-564 | 47.9 | 49.0 | -1.2 | -92.05 | -8.5 |  |  | DROP: below break-even |
| follow_move+pin_move | both | 409-434 | 48.5 | 50.0 | -1.4 | -61.41 | -7.3 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 121-134 | 47.5 | 43.7 | 3.7 | -1.15 | -0.4 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 147-137 | 51.8 | 49.1 | 2.7 | +3.69 | 1.3 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 226-273 | 45.3 | 43.8 | 1.4 | -20.09 | -4.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 524-562 | 48.3 | 48.8 | -0.6 | -81.01 | -7.5 |  |  | DROP: below break-even |
| money_moving+pin_move | both | 333-366 | 47.6 | 48.4 | -0.8 | -30.75 | -4.4 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 149-179 | 45.4 | 42.2 | 3.3 | +19.83 | 6.0 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 181-206 | 46.8 | 47.4 | -0.7 | -10.23 | -2.6 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 218-264 | 45.2 | 43.9 | 1.3 | -19.01 | -3.9 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 938-1074 | 46.6 | 47.5 | -0.9 | -128.26 | -6.4 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 143-152 | 48.5 | 44.0 | 4.5 | +18.67 | 6.3 |  |  | no edge shown yet |
| pin_move+pin_value | both | 184-176 | 51.1 | 49.2 | 1.9 | -0.92 | -0.3 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 129-130 | 49.8 | 45.2 | 4.6 | +9.04 | 3.5 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 338-368 | 47.9 | 48.3 | -0.4 | -28.29 | -4.0 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 42-43 | 49.4 | 45.8 | 3.6 | +12.4 | 14.6 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 121-134 | 47.5 | 43.7 | 3.7 | -1.15 | -0.4 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 155-184 | 45.7 | 42.2 | 3.6 | +20.8 | 6.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 42-33 | 56.0 | 48.4 | 7.6 | +5.27 | 7.0 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 182-205 | 47.0 | 47.3 | -0.3 | -8.34 | -2.2 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 226-273 | 45.3 | 43.8 | 1.4 | -20.09 | -4.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 179-214 | 45.5 | 45.8 | -0.2 | -34.18 | -8.7 |  |  | DROP: below break-even |
| money_level+money_moving | both | 689-602 | 53.4 | 52.3 | 1.1 | -44.71 | -3.5 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 676-592 | 53.3 | 52.1 | 1.3 | -36.8 | -2.9 |  |  | no edge shown yet |
| follow_move+money_level | both | 627-452 | 58.1 | 56.2 | 1.9 | -50.13 | -4.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 106-90 | 54.1 | 48.0 | 6.1 | +11.86 | 6.1 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 249-186 | 57.2 | 58.1 | -0.9 | -15.36 | -3.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_move | both | 327-300 | 52.2 | 53.1 | -0.9 | -32.28 | -5.1 |  |  | no edge shown yet |
| money_level+pin_value | both | 202-177 | 53.3 | 50.0 | 3.3 | -1.14 | -0.3 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 25-54 | 31.6 | 37.1 | -5.4 | -9.04 | -11.4 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | both | 224-338 | 39.9 | 42.0 | -2.2 | -60.73 | -10.8 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 115-190 | 37.7 | 41.3 | -3.6 | -43.39 | -14.2 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 262-367 | 41.7 | 42.6 | -0.9 | -45.71 | -7.3 |  |  | DROP: below break-even |
| consensus_gap+money_delta | both | 49-111 | 30.6 | 38.0 | -7.4 | -21.86 | -13.7 |  |  | DROP: below break-even |
| money_delta+money_level | both | 129-117 | 52.4 | 47.1 | 5.3 | +17.39 | 7.1 |  |  | no edge shown yet |
| money_delta+pin_value | both | 80-75 | 51.6 | 47.1 | 4.5 | +4.87 | 3.1 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 259-361 | 41.8 | 42.6 | -0.8 | -42.88 | -6.9 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 91-158 | 36.5 | 40.0 | -3.4 | -34.45 | -13.8 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | both | 107-185 | 36.6 | 41.3 | -4.6 | -44.29 | -15.2 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 65-116 | 35.9 | 42.7 | -6.8 | -44.39 | -24.5 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | both | 110-145 | 43.1 | 44.2 | -1.0 | -19.14 | -7.5 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 49-79 | 38.3 | 40.5 | -2.2 | -17.28 | -13.5 |  |  | DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 51.1 | 15.6 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 133-157 | 45.9 | 46.2 | -0.3 | -13.73 | -4.7 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 68-48 | 58.6 | 46.7 | 12.0 | +18.99 | 16.4 |  |  | no edge shown yet |
| money_delta+pin_rlm | both | 91-109 | 45.5 | 42.1 | 3.4 | +6.16 | 3.1 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | both | 129-143 | 47.4 | 44.4 | 3.0 | -9.0 | -3.3 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | both | 32-42 | 43.2 | 47.2 | -3.9 | -2.57 | -3.5 |  |  | DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 48.9 | 51.1 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 67-145 | 31.6 | 29.0 | 2.6 | -12.43 | -5.9 |  |  | DROP: below break-even |
| rlm_quiet | spread | 53-55 | 49.1 | 51.2 | -2.1 | -5.78 | -5.4 |  |  | no edge shown yet |
| rlm_quiet | total | 104-138 | 43.0 | 49.4 | -6.4 | -42.52 | -17.6 |  |  | DROP: below break-even |
| pin_move | moneyline | 125-122 | 50.6 | 48.9 | 1.8 | +9.17 | 3.7 |  |  | no edge shown yet |
| pin_move | spread | 223-235 | 48.7 | 50.3 | -1.6 | -31.9 | -7.0 |  |  | DROP: below break-even |
| pin_move | total | 228-232 | 49.6 | 49.8 | -0.2 | -23.87 | -5.2 |  |  | no edge shown yet |
| money_delta | moneyline | 62-186 | 25.0 | 30.1 | -5.1 | -46.61 | -18.8 |  |  | DROP: below break-even |
| money_delta | spread | 129-129 | 50.0 | 51.1 | -1.1 | -11.46 | -4.4 |  |  | no edge shown yet |
| money_delta | total | 173-160 | 52.0 | 49.3 | 2.6 | -1.55 | -0.5 |  |  | no edge shown yet |
| pin_rlm | moneyline | 44-85 | 34.1 | 29.9 | 4.2 | +18.13 | 14.1 |  |  | DROP: below break-even |
| pin_rlm | spread | 26-23 | 53.1 | 51.4 | 1.7 | +0.7 | 1.4 |  |  | no edge shown yet |
| pin_rlm | total | 85-76 | 52.8 | 49.2 | 3.6 | +1.97 | 1.2 |  |  | no edge shown yet |
| follow_move | moneyline | 361-260 | 58.1 | 54.6 | 3.5 | -32.47 | -5.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 283-304 | 48.2 | 49.6 | -1.3 | -46.65 | -7.9 |  |  | DROP: below break-even |
| follow_move | total | 343-363 | 48.6 | 49.9 | -1.3 | -49.98 | -7.1 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 46-106 | 30.3 | 30.8 | -0.5 | -17.57 | -11.6 |  |  | DROP: below break-even |
| rlm_ratio | spread | 42-45 | 48.3 | 50.3 | -2.0 | -6.92 | -7.9 |  |  | no edge shown yet |
| rlm_ratio | total | 138-122 | 53.1 | 49.3 | 3.7 | +4.39 | 1.7 |  |  | no edge shown yet |
| money_level | moneyline | 486-197 | 71.2 | 67.8 | 3.4 | -32.3 | -4.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 349-357 | 49.4 | 49.0 | 0.4 | -42.39 | -6.0 |  |  | DROP: below break-even |
| money_level | total | 423-370 | 53.3 | 50.3 | 3.0 | +13.6 | 1.7 |  |  | no edge shown yet |
| sharp_gap | moneyline | 246-380 | 39.3 | 42.5 | -3.2 | -63.9 | -10.2 |  |  | DROP: below break-even |
| sharp_gap | spread | 354-343 | 50.8 | 49.4 | 1.4 | -23.67 | -3.4 |  |  | no edge shown yet |
| sharp_gap | total | 375-394 | 48.8 | 49.8 | -1.0 | -51.79 | -6.7 |  |  | DROP: below break-even |
| money_moving | moneyline | 258-366 | 41.3 | 43.6 | -2.2 | -50.23 | -8.1 |  |  | DROP: below break-even |
| money_moving | spread | 351-346 | 50.4 | 49.4 | 1.0 | -29.54 | -4.2 |  |  | no edge shown yet |
| money_moving | total | 371-405 | 47.8 | 49.8 | -2.0 | -66.65 | -8.6 |  |  | DROP: below break-even |
| pin_value | moneyline | 23-55 | 29.5 | 32.7 | -3.2 | +30.04 | 38.5 |  |  | DROP: below break-even |
| pin_value | spread | 190-171 | 52.6 | 49.5 | 3.1 | -5.42 | -1.5 |  |  | no edge shown yet |
| pin_value | total | 214-184 | 53.8 | 50.2 | 3.6 | +8.45 | 2.1 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 53.2 | 46.8 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 176-294 | 37.4 | 46.8 | -9.4 | -69.86 | -14.9 |  |  | DROP: below break-even |
| consensus_gap | spread | 98-82 | 54.4 | 48.9 | 5.5 | +1.65 | 0.9 |  |  | no edge shown yet |
| consensus_gap | total | 125-110 | 53.2 | 50.6 | 2.6 | +1.04 | 0.4 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 177-101 | 63.7 | 62.4 | 1.3 | -6.96 | -2.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 164-99 | 62.4 | 61.9 | 0.5 | -7.19 | -2.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 231-351 | 39.7 | 42.5 | -2.8 | -46.55 | -8.0 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 64-75 | 46.0 | 53.3 | -7.3 | -19.25 | -13.9 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | moneyline | 9-42 | 17.6 | 29.9 | -12.2 | -11.24 | -22.0 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 67-145 | 31.6 | 29.0 | 2.6 | -12.43 | -5.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 122-75 | 61.9 | 68.3 | -6.3 | -15.11 | -7.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 69-164 | 29.6 | 42.0 | -12.4 | -19.12 | -8.2 |  |  | !! CHECK: consensus_gap+money_moving close moneyline all sits -12.4 pts from its base (42.0%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+money_level | moneyline | 273-97 | 73.8 | 69.0 | 4.8 | -16.21 | -4.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+money_moving | moneyline | 127-140 | 47.6 | 47.6 | -0.1 | -23.27 | -8.7 |  |  | DROP: below break-even |
| money_delta+money_moving | moneyline | 58-168 | 25.7 | 29.7 | -4.1 | -32.43 | -14.3 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 56-167 | 25.1 | 29.7 | -4.6 | -33.62 | -15.1 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 67-170 | 28.3 | 41.1 | -12.8 | -22.72 | -9.6 |  |  | !! CHECK: consensus_gap+sharp_gap close moneyline all sits -12.8 pts from its base (41.1%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+sharp_gap | moneyline | 123-141 | 46.6 | 46.7 | -0.1 | -24.62 | -9.3 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | moneyline | 30-88 | 25.4 | 28.9 | -3.5 | -17.79 | -15.1 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 31-91 | 25.4 | 28.9 | -3.5 | -21.33 | -17.5 |  |  | DROP: below break-even |
| consensus_gap+pin_move | moneyline | 38-38 | 50.0 | 52.3 | -2.3 | +13.11 | 17.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 12-30 | 28.6 | 31.3 | -2.7 | +11.05 | 26.3 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 6-34 | 15.0 | 30.4 | -15.4 | -7.64 | -19.1 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 97-87 | 52.7 | 50.2 | 2.5 | +0.91 | 0.5 |  |  | no edge shown yet |
| follow_move+pin_rlm | moneyline | 29-49 | 37.2 | 30.4 | 6.8 | -0.7 | -0.9 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 46-106 | 30.3 | 30.8 | -0.5 | -17.57 | -11.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 54-70 | 43.5 | 42.3 | 1.3 | +11.42 | 9.2 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 43-82 | 34.4 | 29.9 | 4.5 | +19.73 | 15.8 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 45-100 | 31.0 | 30.9 | 0.1 | -12.97 | -8.9 |  |  | DROP: below break-even |
| pin_move+pin_rlm | moneyline | 32-53 | 37.6 | 29.7 | 7.9 | +16.01 | 18.8 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 30-45 | 40.0 | 29.9 | 10.1 | +7.01 | 9.4 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 25-37 | 40.3 | 31.0 | 9.3 | +6.78 | 10.9 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 54-72 | 42.9 | 41.7 | 1.2 | +9.25 | 7.3 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 17-41 | 29.3 | 29.7 | -0.4 | -8.7 | -15.0 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 29-49 | 37.2 | 30.4 | 6.8 | -0.7 | -0.9 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 44-85 | 34.1 | 29.9 | 4.2 | +18.13 | 14.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 28-87 | 24.3 | 28.9 | -4.6 | -21.17 | -18.4 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 46-106 | 30.3 | 30.8 | -0.5 | -17.57 | -11.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 14-83 | 14.4 | 30.0 | -15.5 | -24.27 | -25.0 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 16-45 | 26.2 | 31.8 | -5.5 | +7.85 | 12.9 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 19-40 | 32.2 | 31.1 | 1.1 | -1.06 | -1.8 |  |  | DROP: below break-even |
| money_delta+pin_rlm | moneyline | 25-51 | 32.9 | 29.9 | 3.0 | +3.73 | 4.9 |  |  | DROP: below break-even |
| money_delta+pin_value | moneyline | 3-18 | 14.3 | 28.2 | -13.9 | -6.68 | -31.8 |  |  | keep collecting (21/30) |
| money_moving+pin_value | moneyline | 11-33 | 25.0 | 31.2 | -6.2 | +12.94 | 29.4 |  |  | DROP: below break-even |
| pin_move+pin_value | moneyline | 7-10 | 41.2 | 35.9 | 5.3 | +7.35 | 43.2 |  |  | keep collecting (17/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 28.2 | 3.1 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 11-35 | 23.9 | 31.0 | -7.1 | +10.94 | 23.8 |  |  | DROP: below break-even |
| follow_move+money_delta | moneyline | 30-62 | 32.6 | 32.9 | -0.3 | -18.15 | -19.7 |  |  | DROP: below break-even |
| money_delta+money_level | moneyline | 18-24 | 42.9 | 34.4 | 8.4 | +9.58 | 22.8 |  |  | no edge shown yet |
| money_delta+rlm_ratio | moneyline | 25-52 | 32.5 | 31.6 | 0.9 | -12.64 | -16.4 |  |  | DROP: below break-even |
| money_level+pin_move | moneyline | 77-48 | 61.6 | 66.2 | -4.6 | -6.85 | -5.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 12-10 | 54.5 | 34.1 | 20.4 | +5.79 | 26.3 |  |  | keep collecting (22/30) |
| money_level+rlm_ratio | moneyline | 15-14 | 51.7 | 38.7 | 13.0 | +5.04 | 17.4 |  |  | keep collecting (29/30) |
| money_delta+rlm_quiet | moneyline | 18-48 | 27.3 | 30.2 | -2.9 | -19.61 | -29.7 |  |  | DROP: below break-even |
| money_level+pin_value | moneyline | 5-3 | 62.5 | 66.4 | -3.9 | -0.32 | -4.0 |  |  | keep collecting (8/30) |
| follow_move+pin_value | moneyline | 3-8 | 27.3 | 36.1 | -8.8 | +4.8 | 43.7 |  |  | keep collecting (11/30) |
| pin_value+rlm_quiet | moneyline | 2-6 | 25.0 | 28.2 | -3.2 | +6.12 | 76.5 |  |  | keep collecting (8/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 28.2 | -3.2 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 37-28 | 56.9 | 48.3 | 8.6 | +3.57 | 5.5 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 50-46 | 52.1 | 48.6 | 3.5 | -3.34 | -3.5 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 28-30 | 48.3 | 49.1 | -0.9 | -6.06 | -10.5 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | -0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 70-52 | 57.4 | 48.8 | 8.6 | +7.62 | 6.2 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 5-4 | 55.6 | 50.4 | 5.2 | +0.18 | 2.0 |  |  | keep collecting (9/30) |
| consensus_gap+sharp_gap | spread | 49-46 | 51.6 | 48.8 | 2.7 | -4.23 | -4.5 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 165-169 | 49.4 | 49.1 | 0.3 | -19.85 | -5.9 |  |  | no edge shown yet |
| follow_move+pin_move | spread | 139-160 | 46.5 | 50.0 | -3.5 | -33.41 | -11.2 |  |  | DROP: below break-even |
| follow_move+pin_rlm | spread | 19-19 | 50.0 | 51.0 | -1.0 | -1.65 | -4.3 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 65-56 | 53.7 | 48.9 | 4.8 | +0.75 | 0.6 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 42-45 | 48.3 | 50.3 | -2.0 | -6.92 | -7.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 166-168 | 49.7 | 49.1 | 0.6 | -17.71 | -5.3 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 125-133 | 48.4 | 49.8 | -1.4 | -19.81 | -7.7 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 24-23 | 51.1 | 51.3 | -0.2 | -1.13 | -2.4 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 88-88 | 50.0 | 49.0 | 1.0 | -11.97 | -6.8 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 40-44 | 47.6 | 50.2 | -2.5 | -7.85 | -9.3 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 346-338 | 50.6 | 49.4 | 1.2 | -26.04 | -3.8 |  |  | no edge shown yet |
| pin_move+pin_rlm | spread | 26-23 | 53.1 | 51.4 | 1.7 | +0.7 | 1.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 87-86 | 50.3 | 49.8 | 0.5 | -9.39 | -5.4 |  |  | no edge shown yet |
| pin_move+rlm_ratio | spread | 23-26 | 46.9 | 50.8 | -3.9 | -5.1 | -10.4 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 128-133 | 49.0 | 49.8 | -0.8 | -17.08 | -6.5 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 8-10 | 44.4 | 51.1 | -6.6 | -2.97 | -16.5 |  |  | keep collecting (18/30) |
| pin_rlm+rlm_ratio | spread | 19-19 | 50.0 | 51.0 | -1.0 | -1.65 | -4.3 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 26-23 | 53.1 | 51.4 | 1.7 | +0.7 | 1.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 8-8 | 50.0 | 49.6 | 0.4 | -1.17 | -7.3 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | spread | 88-88 | 50.0 | 49.1 | 0.9 | -12.03 | -6.8 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 42-45 | 48.3 | 50.3 | -2.0 | -6.92 | -7.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 161-171 | 48.5 | 48.8 | -0.3 | -25.4 | -7.6 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 22-28 | 44.0 | 49.9 | -5.9 | -8.28 | -16.6 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 270-265 | 50.5 | 49.0 | 1.5 | -21.9 | -4.1 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 60-51 | 54.1 | 48.3 | 5.7 | +0.32 | 0.3 |  |  | no edge shown yet |
| money_level+money_moving | spread | 269-266 | 50.3 | 49.0 | 1.3 | -23.82 | -4.5 |  |  | no edge shown yet |
| money_level+pin_move | spread | 113-133 | 45.9 | 49.5 | -3.5 | -31.07 | -12.6 |  |  | DROP: below break-even |
| money_level+pin_value | spread | 94-93 | 50.3 | 48.7 | 1.6 | -11.89 | -6.4 |  |  | no edge shown yet |
| consensus_gap+money_delta | spread | 16-14 | 53.3 | 50.8 | 2.5 | -0.33 | -1.1 |  |  | no edge shown yet |
| follow_move+money_delta | spread | 42-49 | 46.2 | 50.5 | -4.3 | -10.97 | -12.1 |  |  | no edge shown yet |
| money_delta+money_level | spread | 42-41 | 50.6 | 50.0 | 0.6 | -3.2 | -3.9 |  |  | no edge shown yet |
| money_delta+money_moving | spread | 72-76 | 48.6 | 50.6 | -2.0 | -11.06 | -7.5 |  |  | no edge shown yet |
| money_delta+pin_value | spread | 34-27 | 55.7 | 50.8 | 5.0 | +2.63 | 4.3 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 71-74 | 49.0 | 50.5 | -1.6 | -10.04 | -6.9 |  |  | no edge shown yet |
| follow_move+rlm_quiet | spread | 53-55 | 49.1 | 51.2 | -2.1 | -5.78 | -5.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 14-5 | 73.7 | 51.2 | 22.5 | +7.78 | 40.9 |  |  | keep collecting (19/30) |
| rlm_quiet+sharp_gap | spread | 22-12 | 64.7 | 51.3 | 13.4 | +8.13 | 23.9 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 14-11 | 56.0 | 50.6 | 5.4 | +1.57 | 6.3 |  |  | keep collecting (25/30) |
| money_delta+pin_move | spread | 39-45 | 46.4 | 51.4 | -4.9 | -9.42 | -11.2 |  |  | no edge shown yet |
| money_delta+rlm_ratio | spread | 17-27 | 38.6 | 50.0 | -11.4 | -11.93 | -27.1 |  |  | DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 53.2 | 46.8 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_rlm | spread | 13-16 | 44.8 | 51.0 | -6.2 | -4.31 | -14.8 |  |  | keep collecting (29/30) |
| money_delta+rlm_quiet | spread | 17-18 | 48.6 | 51.7 | -3.1 | -2.27 | -6.5 |  |  | no edge shown yet |
| money_moving+rlm_quiet | spread | 21-12 | 63.6 | 51.2 | 12.4 | +7.18 | 21.7 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 30-29 | 50.8 | 51.7 | -0.8 | -1.14 | -1.9 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-2 | 75.0 | 52.4 | 22.6 | +3.56 | 44.5 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_quiet | spread | 4-3 | 57.1 | 51.4 | 5.8 | +0.48 | 6.9 |  |  | keep collecting (7/30) |
| pin_value+rlm_quiet | spread | 6-6 | 50.0 | 50.0 | 0.0 | -0.7 | -5.8 |  |  | keep collecting (12/30) |
| follow_move+money_delta | total | 107-103 | 51.0 | 49.4 | 1.6 | -5.06 | -2.4 |  |  | no edge shown yet |
| money_level+money_moving | total | 243-235 | 50.8 | 50.1 | 0.7 | -13.93 | -2.9 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 242-228 | 51.5 | 50.1 | 1.4 | -7.7 | -1.6 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 361-385 | 48.4 | 49.8 | -1.4 | -55.67 | -7.5 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 67-60 | 52.8 | 50.9 | 1.9 | -0.56 | -0.4 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 32-23 | 58.2 | 50.5 | 7.7 | +5.39 | 9.8 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 74-63 | 54.0 | 50.6 | 3.4 | +2.65 | 1.9 |  |  | no edge shown yet |
| follow_move+money_moving | total | 226-255 | 47.0 | 49.8 | -2.8 | -48.93 | -10.2 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 235-253 | 48.2 | 49.8 | -1.6 | -38.68 | -7.9 |  |  | DROP: below break-even |
| money_level+pin_move | total | 137-119 | 53.5 | 50.1 | 3.5 | +5.63 | 2.2 |  |  | no edge shown yet |
| money_level+pin_value | total | 103-81 | 56.0 | 50.6 | 5.4 | +11.07 | 6.0 |  |  | no edge shown yet |
| pin_move+pin_value | total | 90-80 | 52.9 | 50.0 | 2.9 | +1.11 | 0.7 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 104-138 | 43.0 | 49.4 | -6.4 | -42.52 | -17.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 154-163 | 48.6 | 49.7 | -1.1 | -22.37 | -7.1 |  |  | no edge shown yet |
| rlm_quiet+sharp_gap | total | 62-87 | 41.6 | 49.2 | -7.6 | -30.18 | -20.3 |  |  | DROP: below break-even |
| money_delta+money_moving | total | 132-123 | 51.8 | 49.3 | 2.4 | -2.22 | -0.9 |  |  | no edge shown yet |
| follow_move+money_level | total | 193-184 | 51.2 | 50.2 | 1.0 | -8.53 | -2.3 |  |  | no edge shown yet |
| follow_move+pin_value | total | 79-73 | 52.0 | 50.1 | 1.9 | -1.86 | -1.2 |  |  | no edge shown yet |
| money_moving+pin_value | total | 82-85 | 49.1 | 50.1 | -1.0 | -11.19 | -6.7 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 83-82 | 50.3 | 50.0 | 0.3 | -7.24 | -4.4 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 54-52 | 50.9 | 50.5 | 0.4 | -4.08 | -3.8 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 56-50 | 52.8 | 50.5 | 2.4 | -0.29 | -0.3 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 48-37 | 56.5 | 50.6 | 5.8 | +5.53 | 6.5 |  |  | no edge shown yet |
| consensus_gap+money_delta | total | 19-14 | 57.6 | 50.0 | 7.5 | +2.74 | 8.3 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | total | 12-9 | 57.1 | 49.7 | 7.4 | +1.72 | 8.2 |  |  | keep collecting (21/30) |
| money_delta+rlm_quiet | total | 30-50 | 37.5 | 49.1 | -11.6 | -22.5 | -28.1 |  |  | DROP: below break-even |
| money_delta+sharp_gap | total | 132-120 | 52.4 | 49.3 | 3.1 | +0.78 | 0.3 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 56-85 | 39.7 | 49.2 | -9.5 | -33.68 | -23.9 |  |  | DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 69-52 | 57.0 | 49.5 | 7.5 | +11.01 | 9.1 |  |  | no edge shown yet |
| money_delta+pin_move | total | 75-72 | 51.0 | 49.2 | 1.8 | -3.24 | -2.2 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 156-163 | 48.9 | 49.6 | -0.7 | -20.46 | -6.4 |  |  | no edge shown yet |
| follow_move+pin_move | total | 173-187 | 48.1 | 49.8 | -1.7 | -28.92 | -8.0 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | total | 24-30 | 44.4 | 49.4 | -4.9 | -7.99 | -14.8 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | total | 10-9 | 52.6 | 50.1 | 2.6 | -0.13 | -0.7 |  |  | keep collecting (19/30) |
| consensus_gap+rlm_ratio | total | 19-9 | 67.9 | 50.2 | 17.6 | +7.85 | 28.0 |  |  | keep collecting (28/30) |
| follow_move+pin_rlm | total | 73-66 | 52.5 | 49.2 | 3.3 | +1.2 | 0.9 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 138-122 | 53.1 | 49.3 | 3.7 | +4.39 | 1.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 42-27 | 60.9 | 49.2 | 11.7 | +11.63 | 16.9 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 69-48 | 59.0 | 49.5 | 9.5 | +15.1 | 12.9 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 82-74 | 52.6 | 49.2 | 3.4 | +1.23 | 0.8 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 133-120 | 52.6 | 49.4 | 3.2 | +1.81 | 0.7 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 85-76 | 52.8 | 49.2 | 3.6 | +1.97 | 1.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 81-67 | 54.7 | 49.3 | 5.5 | +7.36 | 5.0 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 29-22 | 56.9 | 49.5 | 7.4 | +4.3 | 8.4 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 73-66 | 52.5 | 49.2 | 3.3 | +1.2 | 0.9 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 85-76 | 52.8 | 49.2 | 3.6 | +1.97 | 1.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 33-22 | 60.0 | 49.6 | 10.4 | +7.91 | 14.4 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 138-122 | 53.1 | 49.3 | 3.7 | +4.39 | 1.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 53-42 | 55.8 | 49.1 | 6.7 | +6.73 | 7.1 |  |  | no edge shown yet |
| money_delta+rlm_ratio | total | 87-64 | 57.6 | 49.3 | 8.3 | +15.56 | 10.3 |  |  | no edge shown yet |
| money_delta+pin_value | total | 43-30 | 58.9 | 49.5 | 9.4 | +8.92 | 12.2 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 50-71 | 41.3 | 49.3 | -8.0 | -25.01 | -20.7 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | total | 26-36 | 41.9 | 49.1 | -7.2 | -12.14 | -19.6 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | total | 49-66 | 42.6 | 49.1 | -6.5 | -21.05 | -18.3 |  |  | DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 48.9 | 51.1 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| rlm_quiet | close | 1-3k bets | 151-225 | 40.2 | -1.7 | -8.3 |  |
| rlm_quiet | close | 3k+ bets | 47-68 | 40.9 | -2.1 | -11.5 |  |
| rlm_quiet | close | <1k bets | 26-45 | 36.6 | -4.7 | -23.0 |  |
| rlm_quiet | close | pin $1-2k | 61-110 | 35.7 | -7.7 | -20.7 |  |
| rlm_quiet | close | pin $2k+ | 66-80 | 45.2 | 6.6 | 4.5 |  |
| rlm_quiet | close | pin limit <$1k | 41-44 | 48.2 | -0.7 | -7.5 |  |
| pin_move | close | 1-3k bets | 370-373 | 49.8 | 0.1 | -2.9 |  |
| pin_move | close | 3k+ bets | 129-137 | 48.5 | -1.1 | -6.2 |  |
| pin_move | close | <1k bets | 77-79 | 49.4 | -1.1 | -5.4 |  |
| pin_move | close | pin $1-2k | 270-269 | 50.1 | 0.0 | -1.8 |  |
| pin_move | close | pin $2k+ | 204-218 | 48.3 | -1.2 | -7.7 |  |
| pin_move | close | pin limit <$1k | 102-102 | 50.0 | 0.6 | -2.2 |  |
| money_delta | close | 1-3k bets | 231-290 | 44.3 | -0.5 | -7.0 |  |
| money_delta | close | 3k+ bets | 85-113 | 42.9 | -0.7 | -2.0 |  |
| money_delta | close | <1k bets | 48-72 | 40.0 | -2.6 | -16.1 |  |
| money_delta | close | pin $1-2k | 131-129 | 50.4 | 4.4 | 5.7 |  |
| money_delta | close | pin $2k+ | 90-124 | 42.1 | 0.6 | -10.6 |  |
| money_delta | close | pin limit <$1k | 58-65 | 47.2 | -1.7 | -6.0 |  |
| pin_rlm | close | 1-3k bets | 99-112 | 46.9 | 4.6 | 12.3 |  |
| pin_rlm | close | 3k+ bets | 34-48 | 41.5 | -0.8 | -9.4 |  |
| pin_rlm | close | <1k bets | 22-24 | 47.8 | 6.6 | 5.5 |  |
| pin_rlm | close | pin $1-2k | 69-73 | 48.6 | 4.7 | 10.1 |  |
| pin_rlm | close | pin $2k+ | 42-74 | 36.2 | 0.4 | -5.0 |  |
| pin_rlm | close | pin limit <$1k | 44-37 | 54.3 | 6.1 | 15.2 |  |
| follow_move | close | 1-3k bets | 642-597 | 51.8 | 0.8 | -5.4 |  |
| follow_move | close | 3k+ bets | 202-191 | 51.4 | -0.3 | -5.9 |  |
| follow_move | close | <1k bets | 143-139 | 50.7 | -1.5 | -13.8 |  |
| follow_move | close | pin $1-2k | 305-338 | 47.4 | -3.2 | -11.2 |  |
| follow_move | close | pin $2k+ | 256-222 | 53.6 | 2.0 | -2.2 |  |
| follow_move | close | pin limit <$1k | 120-127 | 48.6 | -1.1 | -7.2 |  |
| rlm_ratio | close | 1-3k bets | 146-193 | 43.1 | -0.8 | -8.0 |  |
| rlm_ratio | close | 3k+ bets | 51-47 | 52.0 | 7.5 | 11.3 |  |
| rlm_ratio | close | <1k bets | 29-33 | 46.8 | 4.0 | -6.3 |  |
| rlm_ratio | close | pin $1-2k | 82-82 | 50.0 | 4.4 | 3.8 |  |
| rlm_ratio | close | pin $2k+ | 42-63 | 40.0 | 1.9 | -10.7 |  |
| rlm_ratio | close | pin limit <$1k | 49-44 | 52.7 | 4.1 | 1.7 |  |
| money_level | close | 1-3k bets | 812-586 | 58.1 | 2.6 | -2.2 |  |
| money_level | close | 3k+ bets | 263-208 | 55.8 | 0.9 | -3.1 |  |
| money_level | close | <1k bets | 183-129 | 58.7 | 3.0 | -4.5 |  |
| money_level | close | pin $1-2k | 375-314 | 54.4 | 0.5 | -3.1 |  |
| money_level | close | pin $2k+ | 317-255 | 55.4 | -1.7 | -8.7 |  |
| money_level | close | pin limit <$1k | 147-138 | 51.6 | 1.1 | -2.0 |  |
| sharp_gap | close | 1-3k bets | 609-725 | 45.7 | -1.7 | -9.0 |  |
| sharp_gap | close | 3k+ bets | 227-234 | 49.2 | 1.5 | 3.1 |  |
| sharp_gap | close | <1k bets | 139-157 | 47.0 | -0.8 | -11.1 |  |
| sharp_gap | close | pin $1-2k | 322-341 | 48.6 | -0.1 | -3.5 |  |
| sharp_gap | close | pin $2k+ | 256-294 | 46.5 | 0.1 | -3.2 |  |
| sharp_gap | close | pin limit <$1k | 128-145 | 46.9 | -2.3 | -6.8 |  |
| money_moving | close | 1-3k bets | 616-724 | 46.0 | -1.8 | -9.3 |  |
| money_moving | close | 3k+ bets | 226-236 | 48.9 | 0.9 | 1.6 |  |
| money_moving | close | <1k bets | 138-156 | 46.9 | -0.7 | -9.9 |  |
| money_moving | close | pin $1-2k | 318-346 | 47.9 | -1.0 | -4.8 |  |
| money_moving | close | pin $2k+ | 257-292 | 46.8 | 0.4 | -3.1 |  |
| money_moving | close | pin limit <$1k | 126-152 | 45.3 | -4.0 | -9.9 |  |
| pin_value | close | 1-3k bets | 276-267 | 50.8 | 2.5 | 4.8 |  |
| pin_value | close | 3k+ bets | 86-92 | 48.3 | -0.4 | -5.4 |  |
| pin_value | close | <1k bets | 65-51 | 56.0 | 8.5 | 14.5 |  |
| pin_value | close | pin $1-2k | 196-211 | 48.2 | -0.3 | -2.2 |  |
| pin_value | close | pin $2k+ | 118-127 | 48.2 | 1.7 | 3.3 |  |
| pin_value | close | pin limit <$1k | 113-72 | 61.1 | 10.9 | 18.2 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 46.8 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 46.8 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 257-306 | 45.6 | -3.4 | -8.9 |  |
| consensus_gap | close | 3k+ bets | 87-98 | 47.0 | -0.8 | 5.5 |  |
| consensus_gap | close | <1k bets | 55-81 | 40.4 | -5.1 | -19.2 |  |
| consensus_gap | close | pin $1-2k | 125-132 | 48.6 | -1.2 | 1.1 |  |
| consensus_gap | close | pin $2k+ | 113-116 | 49.3 | -1.4 | 0.3 |  |
| consensus_gap | close | pin limit <$1k | 57-45 | 55.9 | 5.3 | 8.8 |  |
| consensus_gap+follow_move | close | 1-3k bets | 102-93 | 52.3 | 0.7 | -1.4 |  |
| consensus_gap+money_level | close | 1-3k bets | 172-113 | 60.4 | 1.6 | 2.7 |  |
| consensus_gap+money_moving | close | 1-3k bets | 112-168 | 40.0 | -6.1 | -9.8 |  |
| consensus_gap+pin_move | close | 1-3k bets | 65-59 | 52.4 | 1.3 | 7.9 |  |
| consensus_gap+pin_value | close | 1-3k bets | 103-112 | 47.9 | 1.2 | 0.0 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 109-170 | 39.1 | -6.3 | -10.5 |  |
| follow_move+money_level | close | 1-3k bets | 414-295 | 58.4 | 2.5 | -3.8 |  |
| follow_move+money_moving | close | 1-3k bets | 345-379 | 47.7 | -1.3 | -8.9 |  |
| follow_move+pin_move | close | 1-3k bets | 263-283 | 48.2 | -1.6 | -8.1 |  |
| follow_move+pin_value | close | 1-3k bets | 91-88 | 50.8 | 2.1 | 1.7 |  |
| follow_move+sharp_gap | close | 1-3k bets | 348-378 | 47.9 | -0.7 | -7.6 |  |
| money_level+money_moving | close | 1-3k bets | 439-388 | 53.1 | 0.8 | -3.8 |  |
| money_level+pin_move | close | 1-3k bets | 218-198 | 52.4 | -0.4 | -4.5 |  |
| money_level+pin_value | close | 1-3k bets | 131-113 | 53.7 | 4.0 | 0.8 |  |
| money_level+sharp_gap | close | 1-3k bets | 425-381 | 52.7 | 0.8 | -3.5 |  |
| money_moving+pin_move | close | 1-3k bets | 219-235 | 48.2 | -0.4 | -3.1 |  |
| money_moving+pin_value | close | 1-3k bets | 117-137 | 46.1 | -1.6 | -5.6 |  |
| money_moving+sharp_gap | close | 1-3k bets | 585-694 | 45.7 | -1.7 | -8.6 |  |
| pin_move+pin_value | close | 1-3k bets | 119-111 | 51.7 | 2.4 | 1.2 |  |
| pin_move+sharp_gap | close | 1-3k bets | 224-236 | 48.7 | 0.2 | -1.8 |  |
| pin_value+sharp_gap | close | 1-3k bets | 118-138 | 46.1 | -1.3 | -5.6 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 151-225 | 40.2 | -1.7 | -8.3 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 76-135 | 36.0 | -5.0 | -15.9 |  |
| consensus_gap+money_delta | close | 1-3k bets | 29-66 | 30.5 | -7.9 | -20.1 |  |
| follow_move+money_delta | close | 1-3k bets | 115-137 | 45.6 | -0.8 | -9.6 |  |
| money_delta+money_level | close | 1-3k bets | 82-77 | 51.6 | 3.4 | 6.0 |  |
| money_delta+money_moving | close | 1-3k bets | 163-228 | 41.7 | -1.4 | -9.4 |  |
| money_delta+pin_value | close | 1-3k bets | 52-48 | 52.0 | 4.3 | 3.4 |  |
| money_delta+sharp_gap | close | 1-3k bets | 162-225 | 41.9 | -1.3 | -9.0 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 82-93 | 46.9 | -0.1 | -0.8 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 19-29 | 39.6 | 0.6 | 18.1 |  |
| money_level+pin_rlm | close | 1-3k bets | 43-32 | 57.3 | 9.3 | 10.5 |  |
| pin_move+pin_rlm | close | 1-3k bets | 91-91 | 50.0 | 5.9 | 10.8 |  |
| pin_rlm+pin_value | close | 1-3k bets | 30-25 | 54.5 | 8.3 | 29.4 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 99-112 | 46.9 | 4.6 | 12.3 |  |
| money_delta+pin_rlm | close | 1-3k bets | 56-64 | 46.7 | 3.9 | 9.6 |  |
| money_moving+pin_rlm | close | 1-3k bets | 94-108 | 46.5 | 4.1 | 12.4 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 23-34 | 40.4 | 0.2 | 5.5 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 146-193 | 43.1 | -0.8 | -8.0 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 80-97 | 45.2 | 0.3 | -9.2 |  |
| money_level+rlm_ratio | close | 1-3k bets | 67-64 | 51.1 | 2.3 | -1.3 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 140-186 | 42.9 | -1.1 | -8.1 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 78-80 | 49.4 | 4.3 | 2.0 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 28-22 | 56.0 | 8.2 | 7.4 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 146-193 | 43.1 | -0.8 | -8.0 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 16-37 | 30.2 | -5.9 | -9.1 |  |
| follow_move+pin_rlm | close | 1-3k bets | 72-87 | 45.3 | 1.7 | -5.8 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 69-132 | 34.3 | -6.7 | -19.0 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 69-95 | 42.1 | -1.9 | -10.1 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 30-54 | 35.7 | -3.8 | -18.1 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 72-87 | 45.3 | 1.7 | -5.8 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 60-116 | 34.1 | -5.6 | -17.2 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 43-75 | 36.4 | -6.7 | -24.1 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 19-25 | 43.2 | -2.5 | 5.8 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 51.1 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 33-27 | 55.0 | 4.6 | 6.6 |  |
| consensus_gap+money_moving | close | 3k+ bets | 36-54 | 40.0 | -5.1 | 13.8 |  |
| consensus_gap+pin_move | close | 3k+ bets | 25-19 | 56.8 | 6.9 | 14.3 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-6 | 33.3 | -7.6 | 6.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 39-33 | 54.2 | 7.3 | 10.5 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -1.9 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 37-54 | 40.7 | -4.3 | 16.7 |  |
| follow_move+money_moving | close | 3k+ bets | 109-112 | 49.3 | 0.1 | -3.5 |  |
| follow_move+pin_move | close | 3k+ bets | 98-99 | 49.7 | -0.3 | -3.3 |  |
| follow_move+pin_rlm | close | 3k+ bets | 32-33 | 49.2 | 5.0 | 8.4 |  |
| follow_move+pin_value | close | 3k+ bets | 35-35 | 50.0 | -0.1 | -6.1 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 51-47 | 52.0 | 7.5 | 11.3 |  |
| follow_move+sharp_gap | close | 3k+ bets | 111-111 | 50.0 | 1.1 | -1.5 |  |
| money_moving+pin_move | close | 3k+ bets | 75-87 | 46.3 | -1.8 | -8.2 |  |
| money_moving+pin_rlm | close | 3k+ bets | 33-47 | 41.2 | -0.8 | -9.6 |  |
| money_moving+pin_value | close | 3k+ bets | 43-52 | 45.3 | -2.5 | -7.6 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 49-45 | 52.1 | 7.7 | 11.8 |  |
| money_moving+sharp_gap | close | 3k+ bets | 219-226 | 49.2 | 1.5 | 2.9 |  |
| pin_move+pin_rlm | close | 3k+ bets | 32-42 | 43.2 | -0.6 | -5.5 |  |
| pin_move+pin_value | close | 3k+ bets | 36-44 | 45.0 | -4.3 | -15.1 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 34-34 | 50.0 | 4.5 | 8.3 |  |
| pin_move+sharp_gap | close | 3k+ bets | 75-87 | 46.3 | -1.5 | -7.6 |  |
| pin_rlm+pin_value | close | 3k+ bets | 6-15 | 28.6 | -17.8 | -45.5 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 32-33 | 49.2 | 5.0 | 8.4 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 34-48 | 41.5 | -0.8 | -9.4 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 9-10 | 47.4 | -2.8 | -10.1 |  |
| pin_value+sharp_gap | close | 3k+ bets | 43-51 | 45.7 | -2.1 | -6.6 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 51-47 | 52.0 | 7.5 | 11.3 |  |
| follow_move+money_delta | close | 3k+ bets | 41-50 | 45.1 | -0.3 | -6.9 |  |
| money_level+money_moving | close | 3k+ bets | 154-131 | 54.0 | 1.8 | 0.0 |  |
| money_level+sharp_gap | close | 3k+ bets | 153-128 | 54.4 | 2.4 | 1.4 |  |
| follow_move+money_level | close | 3k+ bets | 126-94 | 57.3 | 1.0 | -3.0 |  |
| money_level+rlm_ratio | close | 3k+ bets | 25-12 | 67.6 | 20.2 | 38.4 |  |
| consensus_gap+money_level | close | 3k+ bets | 48-45 | 51.6 | -5.1 | -11.3 |  |
| money_level+pin_move | close | 3k+ bets | 69-64 | 51.9 | -1.6 | -4.7 |  |
| money_level+pin_value | close | 3k+ bets | 48-46 | 51.1 | 0.5 | -5.3 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 8-12 | 40.0 | 0.7 | -0.6 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 47-68 | 40.9 | -2.1 | -11.5 |  |
| money_delta+money_moving | close | 3k+ bets | 65-85 | 43.3 | 0.8 | 3.5 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 19-27 | 41.3 | 0.0 | -4.4 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 24-36 | 40.0 | -2.3 | -10.7 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 22-35 | 38.6 | -3.6 | -12.8 |  |
| consensus_gap+money_delta | close | 3k+ bets | 13-23 | 36.1 | -3.6 | 20.4 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 11-27 | 28.9 | -13.9 | -36.8 |  |
| money_delta+sharp_gap | close | 3k+ bets | 63-82 | 43.4 | 1.1 | 4.2 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 29-36 | 44.6 | 0.3 | -3.6 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 11-19 | 36.7 | -5.4 | -12.9 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 8-13 | 38.1 | -11.4 | -27.2 |  |
| money_delta+money_level | close | 3k+ bets | 33-22 | 60.0 | 13.7 | 21.2 |  |
| money_level+pin_rlm | close | 3k+ bets | 16-9 | 64.0 | 18.9 | 37.0 |  |
| money_delta+pin_value | close | 3k+ bets | 19-19 | 50.0 | 3.7 | -5.7 |  |
| money_delta+pin_move | close | 3k+ bets | 37-45 | 45.1 | -0.2 | -8.0 |  |
| money_delta+pin_rlm | close | 3k+ bets | 22-29 | 43.1 | 1.1 | -8.2 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 30-26 | 53.6 | 9.1 | 13.5 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 46.8 | 87.7 |  |
| money_level+money_moving | close | <1k bets | 96-82 | 53.9 | 1.5 | -7.0 |  |
| money_level+sharp_gap | close | <1k bets | 98-82 | 54.4 | 1.8 | -6.6 |  |
| money_moving+sharp_gap | close | <1k bets | 134-153 | 46.7 | -0.9 | -10.7 |  |
| consensus_gap+money_level | close | <1k bets | 29-28 | 50.9 | -6.0 | -22.2 |  |
| consensus_gap+money_moving | close | <1k bets | 25-40 | 38.5 | -5.4 | -17.8 |  |
| consensus_gap+pin_move | close | <1k bets | 8-13 | 38.1 | -12.5 | -17.2 |  |
| consensus_gap+pin_value | close | <1k bets | 18-15 | 54.5 | 11.9 | 31.8 |  |
| consensus_gap+sharp_gap | close | <1k bets | 26-42 | 38.2 | -5.6 | -19.4 |  |
| money_level+pin_move | close | <1k bets | 40-38 | 51.3 | -2.7 | -9.3 |  |
| money_level+pin_value | close | <1k bets | 23-18 | 56.1 | 6.0 | 4.7 |  |
| money_moving+pin_move | close | <1k bets | 39-44 | 47.0 | -0.6 | -4.3 |  |
| money_moving+pin_value | close | <1k bets | 21-17 | 55.3 | 10.2 | 29.4 |  |
| pin_move+pin_value | close | <1k bets | 29-21 | 58.0 | 9.5 | 16.9 |  |
| pin_move+sharp_gap | close | <1k bets | 39-45 | 46.4 | -1.7 | -9.2 |  |
| pin_value+sharp_gap | close | <1k bets | 21-16 | 56.8 | 11.2 | 32.9 |  |
| follow_move+money_delta | close | <1k bets | 23-27 | 46.0 | 2.8 | -7.4 |  |
| follow_move+money_moving | close | <1k bets | 64-73 | 46.7 | -2.7 | -14.4 |  |
| follow_move+pin_move | close | <1k bets | 48-52 | 48.0 | -3.0 | -10.9 |  |
| follow_move+sharp_gap | close | <1k bets | 65-73 | 47.1 | -2.8 | -16.4 |  |
| money_delta+money_moving | close | <1k bets | 34-54 | 38.6 | -1.8 | -15.9 |  |
| money_delta+pin_move | close | <1k bets | 14-19 | 42.4 | -1.8 | -17.4 |  |
| money_delta+sharp_gap | close | <1k bets | 34-54 | 38.6 | -1.8 | -15.9 |  |
| follow_move+rlm_quiet | close | <1k bets | 26-45 | 36.6 | -4.7 | -23.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 29-33 | 46.8 | 4.0 | -6.3 |  |
| money_delta+rlm_quiet | close | <1k bets | 11-14 | 44.0 | 3.9 | -7.9 |  |
| money_delta+rlm_ratio | close | <1k bets | 19-20 | 48.7 | 6.8 | -0.8 |  |
| money_moving+rlm_quiet | close | <1k bets | 16-18 | 47.1 | 6.1 | 3.1 |  |
| money_moving+rlm_ratio | close | <1k bets | 29-33 | 46.8 | 4.0 | -6.3 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 12-15 | 44.4 | 4.7 | -7.6 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 15-19 | 44.1 | 2.5 | -9.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 29-33 | 46.8 | 4.0 | -6.3 |  |
| follow_move+money_level | close | <1k bets | 87-63 | 58.0 | 0.2 | -11.2 |  |
| consensus_gap+money_delta | close | <1k bets | 7-22 | 24.1 | -10.5 | -35.0 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -2.5 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 13-16 | 44.8 | 5.3 | -3.9 |  |
| money_moving+pin_rlm | close | <1k bets | 22-24 | 47.8 | 6.6 | 5.5 |  |
| pin_rlm+sharp_gap | close | <1k bets | 22-24 | 47.8 | 6.6 | 5.5 |  |
| money_delta+pin_value | close | <1k bets | 9-8 | 52.9 | 7.4 | 21.5 |  |
| consensus_gap+follow_move | close | <1k bets | 14-20 | 41.2 | -10.5 | -33.3 |  |
| follow_move+pin_rlm | close | <1k bets | 17-14 | 54.8 | 11.3 | 8.4 |  |
| follow_move+pin_value | close | <1k bets | 21-14 | 60.0 | 11.2 | 14.0 |  |
| pin_move+pin_rlm | close | <1k bets | 20-19 | 51.3 | 7.7 | 8.1 |  |
| pin_move+rlm_quiet | close | <1k bets | 12-14 | 46.2 | 0.8 | -1.0 |  |
| pin_move+rlm_ratio | close | <1k bets | 17-16 | 51.5 | 6.4 | 0.5 |  |
| pin_rlm+pin_value | close | <1k bets | 6-3 | 66.7 | 24.9 | 64.1 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 8-6 | 57.1 | 14.0 | 12.9 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 17-14 | 54.8 | 11.3 | 8.4 |  |
| pin_value+rlm_quiet | close | <1k bets | 5-4 | 55.6 | 6.6 | 6.5 |  |
| pin_value+rlm_ratio | close | <1k bets | 5-1 | 83.3 | 35.1 | 58.3 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -6.5 | -42.5 |  |
| money_delta+money_level | close | <1k bets | 14-18 | 43.8 | 0.7 | -12.1 |  |
| money_level+rlm_ratio | close | <1k bets | 14-14 | 50.0 | 4.9 | -2.1 |  |
| money_level+pin_rlm | close | <1k bets | 9-7 | 56.2 | 13.7 | 11.6 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-5 | 16.7 | -21.5 | -68.2 |  |
| consensus_gap+follow_move | close | pin $1-2k | 48-52 | 48.0 | -4.2 | -8.9 |  |
| consensus_gap+money_moving | close | pin $1-2k | 59-70 | 45.7 | -2.9 | -1.9 |  |
| consensus_gap+pin_move | close | pin $1-2k | 47-47 | 50.0 | -1.9 | 6.7 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-18 | 41.9 | 0.5 | 25.8 |  |
| consensus_gap+pin_value | close | pin $1-2k | 72-76 | 48.6 | 2.0 | -0.6 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-15 | 48.3 | 2.9 | 5.2 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 57-67 | 46.0 | -1.9 | 0.1 |  |
| follow_move+money_moving | close | pin $1-2k | 176-207 | 46.0 | -3.5 | -10.4 |  |
| follow_move+pin_move | close | pin $1-2k | 187-209 | 47.2 | -2.9 | -9.1 |  |
| follow_move+pin_rlm | close | pin $1-2k | 56-57 | 49.6 | 4.1 | 3.5 |  |
| follow_move+pin_value | close | pin $1-2k | 66-77 | 46.2 | -3.3 | -12.9 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 82-82 | 50.0 | 4.4 | 3.8 |  |
| follow_move+sharp_gap | close | pin $1-2k | 181-205 | 46.9 | -2.5 | -9.1 |  |
| money_moving+pin_move | close | pin $1-2k | 162-176 | 47.9 | -1.2 | -3.2 |  |
| money_moving+pin_rlm | close | pin $1-2k | 66-70 | 48.5 | 4.3 | 10.4 |  |
| money_moving+pin_value | close | pin $1-2k | 77-106 | 42.1 | -5.8 | -16.1 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 80-78 | 50.6 | 4.7 | 4.9 |  |
| money_moving+sharp_gap | close | pin $1-2k | 308-331 | 48.2 | -0.5 | -3.8 |  |
| pin_move+pin_rlm | close | pin $1-2k | 66-65 | 50.4 | 5.2 | 11.7 |  |
| pin_move+pin_value | close | pin $1-2k | 83-95 | 46.6 | -3.0 | -10.2 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 64-59 | 52.0 | 5.3 | 7.1 |  |
| pin_move+sharp_gap | close | pin $1-2k | 165-176 | 48.4 | -0.5 | -2.7 |  |
| pin_rlm+pin_value | close | pin $1-2k | 17-25 | 40.5 | -7.6 | -16.3 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 56-57 | 49.6 | 4.1 | 3.5 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 69-73 | 48.6 | 4.7 | 10.1 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 19-21 | 47.5 | -1.8 | -10.3 |  |
| pin_value+sharp_gap | close | pin $1-2k | 77-102 | 43.0 | -4.8 | -14.2 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 82-82 | 50.0 | 4.4 | 3.8 |  |
| follow_move+money_level | close | pin $1-2k | 202-185 | 52.2 | -1.8 | -8.2 |  |
| money_level+rlm_ratio | close | pin $1-2k | 46-34 | 57.5 | 9.7 | 12.1 |  |
| money_level+sharp_gap | close | pin $1-2k | 232-212 | 52.3 | 0.6 | -3.2 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 4-14 | 22.2 | -18.3 | -36.2 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 61-110 | 35.7 | -7.7 | -20.7 |  |
| money_level+money_moving | close | pin $1-2k | 231-216 | 51.7 | -0.1 | -4.5 |  |
| consensus_gap+money_level | close | pin $1-2k | 74-63 | 54.0 | -2.8 | -5.1 |  |
| money_level+pin_value | close | pin $1-2k | 86-85 | 50.3 | 0.3 | -5.9 |  |
| money_level+pin_move | close | pin $1-2k | 157-145 | 52.0 | -0.6 | -5.0 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 30-48 | 38.5 | -5.2 | -9.4 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 44-65 | 40.4 | -5.1 | -10.6 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 19-33 | 36.5 | -7.4 | -14.7 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 25-40 | 38.5 | -4.3 | -9.1 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 31-50 | 38.3 | -5.0 | -12.2 |  |
| money_level+pin_rlm | close | pin $1-2k | 32-23 | 58.2 | 12.0 | 14.4 |  |
| follow_move+money_delta | close | pin $1-2k | 67-69 | 49.3 | 2.9 | 0.5 |  |
| money_delta+money_moving | close | pin $1-2k | 88-97 | 47.6 | 3.2 | 3.9 |  |
| money_delta+pin_move | close | pin $1-2k | 67-70 | 48.9 | 1.7 | 2.7 |  |
| money_delta+pin_rlm | close | pin $1-2k | 43-45 | 48.9 | 5.3 | 10.7 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 50-45 | 52.6 | 7.0 | 9.5 |  |
| money_delta+sharp_gap | close | pin $1-2k | 88-95 | 48.1 | 3.7 | 5.0 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 46.8 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 46-37 | 55.4 | 7.6 | 7.9 |  |
| consensus_gap+money_delta | close | pin $1-2k | 18-26 | 40.9 | -0.8 | 2.5 |  |
| money_delta+pin_value | close | pin $1-2k | 43-45 | 48.9 | 0.8 | -3.4 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 20-37 | 35.1 | -9.1 | -20.8 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 12-27 | 30.8 | -18.1 | -40.9 |  |
| consensus_gap+follow_move | close | pin $2k+ | 36-29 | 55.4 | 2.5 | -4.4 |  |
| consensus_gap+money_delta | close | pin $2k+ | 9-26 | 25.7 | -9.1 | -49.8 |  |
| consensus_gap+money_level | close | pin $2k+ | 74-56 | 56.9 | -5.2 | -11.2 |  |
| consensus_gap+money_moving | close | pin $2k+ | 41-69 | 37.3 | -8.0 | -4.1 |  |
| consensus_gap+pin_move | close | pin $2k+ | 34-33 | 50.7 | 0.6 | -3.5 |  |
| consensus_gap+pin_value | close | pin $2k+ | 46-51 | 47.4 | 4.4 | 10.9 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 2-13 | 13.3 | -19.8 | -65.0 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 43-72 | 37.4 | -8.3 | -3.8 |  |
| follow_move+money_delta | close | pin $2k+ | 35-46 | 43.2 | 1.3 | -10.9 |  |
| follow_move+money_level | close | pin $2k+ | 151-101 | 59.9 | 0.7 | -4.0 |  |
| follow_move+money_moving | close | pin $2k+ | 121-122 | 49.8 | 1.9 | -4.4 |  |
| follow_move+pin_move | close | pin $2k+ | 154-152 | 50.3 | 0.3 | -4.8 |  |
| follow_move+pin_value | close | pin $2k+ | 38-34 | 52.8 | 5.2 | 13.3 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 42-63 | 40.0 | 1.9 | -10.7 |  |
| follow_move+sharp_gap | close | pin $2k+ | 122-123 | 49.8 | 2.0 | -4.2 |  |
| money_delta+money_level | close | pin $2k+ | 26-22 | 54.2 | 9.3 | 9.2 |  |
| money_delta+money_moving | close | pin $2k+ | 63-92 | 40.6 | 1.7 | -10.2 |  |
| money_delta+pin_move | close | pin $2k+ | 35-51 | 40.7 | -2.0 | -16.7 |  |
| money_delta+pin_value | close | pin $2k+ | 20-22 | 47.6 | 3.7 | -9.2 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 21-32 | 39.6 | 1.1 | -14.7 |  |
| money_delta+sharp_gap | close | pin $2k+ | 61-91 | 40.1 | 1.2 | -11.2 |  |
| money_level+money_moving | close | pin $2k+ | 169-157 | 51.8 | -0.8 | -6.0 |  |
| money_level+pin_move | close | pin $2k+ | 110-99 | 52.6 | -2.9 | -7.5 |  |
| money_level+pin_value | close | pin $2k+ | 59-56 | 51.3 | 1.7 | -5.0 |  |
| money_level+rlm_ratio | close | pin $2k+ | 15-14 | 51.7 | 5.4 | 7.7 |  |
| money_level+sharp_gap | close | pin $2k+ | 169-158 | 51.7 | -1.0 | -5.9 |  |
| money_moving+pin_move | close | pin $2k+ | 105-118 | 47.1 | 0.2 | -5.6 |  |
| money_moving+pin_value | close | pin $2k+ | 61-70 | 46.6 | 1.1 | 4.7 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 42-62 | 40.4 | 2.2 | -9.8 |  |
| money_moving+sharp_gap | close | pin $2k+ | 251-288 | 46.6 | 0.2 | -3.0 |  |
| pin_move+pin_value | close | pin $2k+ | 53-51 | 51.0 | 3.0 | -0.3 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 30-42 | 41.7 | 2.1 | -4.3 |  |
| pin_move+sharp_gap | close | pin $2k+ | 105-119 | 46.9 | -0.1 | -5.7 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 5-7 | 41.7 | -1.8 | -17.1 |  |
| pin_value+sharp_gap | close | pin $2k+ | 61-71 | 46.2 | 0.9 | 3.9 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 42-63 | 40.0 | 1.9 | -10.7 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 5-21 | 19.2 | -12.4 | -20.4 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 6-13 | 31.6 | 1.1 | -27.1 |  |
| follow_move+pin_rlm | close | pin $2k+ | 30-48 | 38.5 | 1.2 | -10.9 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 66-80 | 45.2 | 6.6 | 4.5 |  |
| money_moving+pin_rlm | close | pin $2k+ | 42-74 | 36.2 | 0.4 | -5.0 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 30-44 | 40.5 | 4.9 | -7.9 |  |
| pin_move+pin_rlm | close | pin $2k+ | 34-50 | 40.5 | 2.8 | -4.3 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 43-55 | 43.9 | 3.3 | -3.8 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 15-33 | 31.2 | -1.3 | -21.9 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 30-48 | 38.5 | 1.2 | -10.9 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 42-74 | 36.2 | 0.4 | -5.0 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 22-40 | 35.5 | 2.6 | -15.5 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 30-45 | 40.0 | 4.4 | -9.1 |  |
| money_delta+pin_rlm | close | pin $2k+ | 22-42 | 34.4 | -1.3 | -15.1 |  |
| money_level+pin_rlm | close | pin $2k+ | 15-10 | 60.0 | 15.9 | 27.1 |  |
| pin_rlm+pin_value | close | pin $2k+ | 6-13 | 31.6 | -5.4 | 13.6 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 19-26 | 42.2 | 3.7 | -12.9 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 6-8 | 42.9 | 3.8 | 54.3 |  |
| follow_move+money_delta | close | pin limit <$1k | 35-45 | 43.8 | -5.1 | -16.0 |  |
| money_level+money_moving | close | pin limit <$1k | 78-89 | 46.7 | -3.0 | -10.5 |  |
| money_level+sharp_gap | close | pin limit <$1k | 75-83 | 47.5 | -2.2 | -9.0 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 117-136 | 46.2 | -2.9 | -7.8 |  |
| consensus_gap+money_level | close | pin limit <$1k | 32-26 | 55.2 | 4.1 | 2.2 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 17-11 | 60.7 | 12.0 | 30.2 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 42-33 | 56.0 | 6.0 | 11.3 |  |
| follow_move+money_moving | close | pin limit <$1k | 72-90 | 44.4 | -4.7 | -14.6 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 77-89 | 46.4 | -2.7 | -10.9 |  |
| money_level+pin_move | close | pin limit <$1k | 60-56 | 51.7 | 1.8 | -1.3 |  |
| money_level+pin_value | close | pin limit <$1k | 57-36 | 61.3 | 10.8 | 15.9 |  |
| pin_move+pin_value | close | pin limit <$1k | 48-30 | 61.5 | 11.5 | 22.6 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 22-11 | 66.7 | 17.0 | 23.4 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 25-19 | 56.8 | 7.7 | 17.6 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 27-19 | 58.7 | 9.5 | 20.6 |  |
| follow_move+money_level | close | pin limit <$1k | 62-66 | 48.4 | -1.7 | -7.8 |  |
| follow_move+pin_move | close | pin limit <$1k | 68-73 | 48.2 | -1.1 | -7.6 |  |
| follow_move+pin_value | close | pin limit <$1k | 43-26 | 62.3 | 12.4 | 18.2 |  |
| money_moving+pin_move | close | pin limit <$1k | 66-72 | 47.8 | -1.3 | -5.3 |  |
| money_moving+pin_value | close | pin limit <$1k | 43-30 | 58.9 | 9.1 | 17.8 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 68-73 | 48.2 | -0.9 | -4.6 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 44-32 | 57.9 | 8.1 | 15.7 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 41-44 | 48.2 | -0.7 | -7.5 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 27-31 | 46.6 | -2.0 | -10.7 |  |
| money_delta+money_moving | close | pin limit <$1k | 50-54 | 48.1 | -0.7 | -3.6 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 9-6 | 60.0 | 13.1 | 43.2 |  |
| money_delta+money_level | close | pin limit <$1k | 26-23 | 53.1 | 3.8 | 1.7 |  |
| money_delta+pin_value | close | pin limit <$1k | 17-8 | 68.0 | 19.0 | 46.9 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 49-52 | 48.5 | -0.2 | -2.7 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 31-36 | 46.3 | -2.1 | -4.6 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 7-3 | 70.0 | 24.1 | 77.3 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 26-22 | 54.2 | 6.3 | 13.3 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 41-35 | 53.9 | 5.8 | 15.2 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 43-37 | 53.8 | 5.3 | 8.6 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-5 | 79.2 | 30.4 | 69.5 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 44-37 | 54.3 | 6.1 | 15.2 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 7-1 | 87.5 | 40.6 | 67.3 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 14-7 | 66.7 | 17.1 | 27.5 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 11-19 | 36.7 | -11.2 | -29.6 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 23-25 | 47.9 | -0.7 | -7.9 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 35-29 | 54.7 | 6.1 | 5.3 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 49-44 | 52.7 | 4.1 | 1.7 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 29-28 | 50.9 | 2.4 | -2.1 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 21-30 | 41.2 | -7.2 | -20.8 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 45-42 | 51.7 | 3.2 | -0.0 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 35-29 | 54.7 | 6.1 | 5.3 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 15-13 | 53.6 | 5.8 | 3.1 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 35-29 | 54.7 | 6.1 | 5.3 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 23-23 | 50.0 | 1.7 | -4.0 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 49-44 | 52.7 | 4.1 | 1.7 |  |
| money_level+pin_rlm | close | pin limit <$1k | 21-15 | 58.3 | 9.2 | 12.0 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 23-18 | 56.1 | 7.4 | 9.1 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 18-5 | 78.3 | 28.7 | 49.8 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 7-3 | 70.0 | 22.1 | 33.8 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 51.1 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.6 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -52.1 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 35-40 | 46.7 | 10.5 | 12.9 | 0.26 |
| rlm_quiet | early | pin $1-2k | 2-5 | 28.6 | -3.2 | 16.0 | -1.07 |
| rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.2 | -100.0 | 1.3 |
| rlm_quiet | early | pin limit <$1k | 5-8 | 38.5 | -6.2 | -21.5 | 0.25 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -51.1 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 9-12 | 42.9 | -5.7 | -21.3 | 0.1 |
| pin_move | early | pin $1-2k | 0-5 | 0.0 | -40.6 | -100.0 | 0.14 |
| pin_move | early | pin limit <$1k | 9-8 | 52.9 | 1.9 | -2.7 | 0.02 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.3 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 9-7 | 56.2 | 15.0 | 22.8 | -0.11 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -40.7 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 5-0 | 100.0 | 51.1 | 88.6 | 0.0 |
| pin_rlm | early | <1k bets | 1-3 | 25.0 | -14.1 | -51.8 | -0.37 |
| pin_rlm | early | pin $1-2k | 0-3 | 0.0 | -42.7 | -100.0 | -0.67 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 71.8 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.6 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -52.1 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 468-412 | 53.2 | 1.7 | -5.9 | 0.17 |
| follow_move | early | pin $1-2k | 36-24 | 60.0 | 8.9 | 10.7 | -0.33 |
| follow_move | early | pin $2k+ | 0-2 | 0.0 | -40.7 | -100.0 | 0.65 |
| follow_move | early | pin limit <$1k | 53-47 | 53.0 | 3.0 | 0.0 | -0.16 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.0 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.2 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 28-20 | 58.3 | 19.2 | 27.7 | 0.65 |
| rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.4 | 29.7 | -1.02 |
| rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.7 | -100.0 | 0.65 |
| rlm_ratio | early | pin limit <$1k | 8-1 | 88.9 | 44.1 | 79.0 | 0.37 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 1.6 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 44.2 | 59.7 | 0.33 |
| money_level | early | <1k bets | 161-109 | 59.6 | 0.1 | -6.3 | -0.13 |
| money_level | early | pin $1-2k | 21-10 | 67.7 | 3.2 | 0.1 | 0.12 |
| money_level | early | pin $2k+ | 1-1 | 50.0 | -12.5 | -47.2 | -0.7 |
| money_level | early | pin limit <$1k | 26-27 | 49.1 | -3.7 | -9.2 | 0.25 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.3 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.7 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 131-117 | 52.8 | 4.5 | 2.2 | 0.35 |
| sharp_gap | early | pin $1-2k | 16-13 | 55.2 | 1.0 | 2.2 | -0.24 |
| sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.7 | -100.0 | 0.65 |
| sharp_gap | early | pin limit <$1k | 31-19 | 62.0 | 13.4 | 27.8 | 0.11 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.7 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 52.1 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 96-85 | 53.0 | 1.6 | -6.3 | 0.12 |
| money_moving | early | pin $1-2k | 8-10 | 44.4 | -13.6 | -39.0 | 0.28 |
| money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.5 | -8.4 | 0.65 |
| money_moving | early | pin limit <$1k | 25-10 | 71.4 | 22.4 | 49.9 | 0.39 |
| pin_value | early | 1-3k bets | 13-10 | 56.5 | 8.5 | 6.3 | -0.04 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.2 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 46-48 | 48.9 | 0.1 | -7.5 | 0.04 |
| pin_value | early | pin $1-2k | 15-26 | 36.6 | -10.2 | -31.3 | 0.11 |
| pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.2 | 83.3 | 0.0 |
| pin_value | early | pin limit <$1k | 44-32 | 57.9 | 8.2 | 9.5 | -0.0 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -51.1 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -27.1 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.0 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.5 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 223-269 | 45.3 | -2.9 | -10.9 | 0.38 |
| consensus_gap | early | pin $1-2k | 16-23 | 41.0 | -4.7 | -22.6 | 0.33 |
| consensus_gap | early | pin $2k+ | 1-1 | 50.0 | 12.5 | -8.4 | 0.65 |
| consensus_gap | early | pin limit <$1k | 22-35 | 38.6 | -11.6 | -21.2 | 0.31 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -53.2 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.3 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.3 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -2.1 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.9 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 5.8 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.4 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 7-4 | 63.6 | 14.5 | 19.4 | -0.09 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.3 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 17.0 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -51.1 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -0.6 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 6-5 | 54.5 | 8.4 | 1.3 | 0.27 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -1.1 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-7 | 50.0 | 3.2 | -6.4 | -0.29 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.6 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.7 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -19.9 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.8 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 3.6 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.7 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.0 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.5 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.0 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.4 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.0 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.5 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.0 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 53.2 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 11.4 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 18.1 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 16.1 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 16.1 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -28.2 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 53.2 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 53.2 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.2 | 83.3 | 1.0 |
| follow_move+rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -52.1 | -100.0 | -0.5 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.2 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.2 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 52.1 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.2 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.2 | 83.3 | 1.0 |
| rlm_quiet+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.2 | -100.0 | -1.0 |
| rlm_quiet+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.2 | -100.0 | -1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.2 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 39.6 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 51.1 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 31-38 | 44.9 | -6.9 | -18.5 | 0.86 |
| consensus_gap+money_level | early | <1k bets | 35-26 | 57.4 | -6.1 | -10.6 | 0.21 |
| consensus_gap+sharp_gap | early | <1k bets | 26-41 | 38.8 | -8.0 | -16.4 | 0.9 |
| follow_move+money_level | early | <1k bets | 81-41 | 66.4 | 5.6 | -2.1 | 0.04 |
| follow_move+sharp_gap | early | <1k bets | 69-37 | 65.1 | 15.3 | 16.5 | 0.52 |
| money_level+sharp_gap | early | <1k bets | 86-57 | 60.1 | 3.9 | -1.4 | 0.17 |
| follow_move+money_moving | early | <1k bets | 50-32 | 61.0 | 8.0 | 6.4 | 0.43 |
| money_level+money_moving | early | <1k bets | 58-43 | 57.4 | -1.3 | -9.1 | -0.15 |
| money_moving+sharp_gap | early | <1k bets | 57-50 | 53.3 | 4.0 | -2.0 | 0.28 |
| consensus_gap+money_moving | early | <1k bets | 14-21 | 40.0 | -9.3 | -36.3 | 0.27 |
| follow_move+pin_value | early | <1k bets | 16-14 | 53.3 | 3.7 | 0.1 | -0.18 |
| follow_move+rlm_quiet | early | <1k bets | 35-40 | 46.7 | 10.5 | 12.9 | 0.26 |
| money_moving+rlm_quiet | early | <1k bets | 14-12 | 53.8 | 16.2 | 28.2 | 0.62 |
| rlm_quiet+sharp_gap | early | <1k bets | 20-15 | 57.1 | 20.1 | 27.6 | -0.0 |
| follow_move+rlm_ratio | early | <1k bets | 28-20 | 58.3 | 19.2 | 27.7 | 0.65 |
| rlm_quiet+rlm_ratio | early | <1k bets | 18-11 | 62.1 | 25.4 | 40.9 | 0.03 |
| rlm_ratio+sharp_gap | early | <1k bets | 28-20 | 58.3 | 19.2 | 27.7 | 0.65 |
| pin_move+pin_value | early | <1k bets | 3-7 | 30.0 | -19.2 | -42.7 | -0.1 |
| follow_move+pin_move | early | <1k bets | 6-6 | 50.0 | -0.5 | -9.9 | 0.45 |
| consensus_gap+pin_value | early | <1k bets | 17-24 | 41.5 | -5.8 | -22.2 | 0.38 |
| pin_value+rlm_quiet | early | <1k bets | 0-3 | 0.0 | -43.4 | -100.0 | -0.6 |
| money_delta+money_moving | early | <1k bets | 8-7 | 53.3 | 12.6 | 18.2 | -0.11 |
| money_delta+sharp_gap | early | <1k bets | 7-5 | 58.3 | 17.9 | 31.9 | -0.14 |
| consensus_gap+pin_move | early | <1k bets | 1-5 | 16.7 | -28.8 | -68.2 | 0.22 |
| money_level+pin_move | early | <1k bets | 3-2 | 60.0 | 5.2 | 0.8 | 0.08 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -28.2 | -100.0 | -4.8 |
| consensus_gap+rlm_quiet | early | <1k bets | 3-5 | 37.5 | -1.0 | -22.7 | 1.01 |
| consensus_gap+rlm_ratio | early | <1k bets | 5-3 | 62.5 | 21.4 | 25.0 | 0.65 |
| follow_move+pin_rlm | early | <1k bets | 1-2 | 33.3 | -9.4 | -35.8 | -0.93 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -28.2 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | <1k bets | 0-1 | 0.0 | -28.2 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-2 | 33.3 | -9.4 | -35.8 | -0.93 |
| pin_rlm+sharp_gap | early | <1k bets | 1-3 | 25.0 | -14.1 | -51.8 | -0.37 |
| pin_value+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 24.7 | 27.3 | -0.93 |
| pin_value+sharp_gap | early | <1k bets | 6-5 | 54.5 | 4.8 | 4.1 | 0.17 |
| money_level+pin_value | early | <1k bets | 6-5 | 54.5 | 2.4 | 4.1 | 0.88 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -51.0 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -48.9 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 2-3 | 40.0 | -14.8 | -23.6 | 1.34 |
| money_level+rlm_ratio | early | <1k bets | 8-9 | 47.1 | 5.0 | -2.4 | 1.85 |
| money_moving+rlm_ratio | early | <1k bets | 14-8 | 63.6 | 21.1 | 41.4 | 0.8 |
| consensus_gap+money_delta | early | <1k bets | 2-0 | 100.0 | 50.0 | 90.9 | 0.5 |
| money_delta+money_level | early | <1k bets | 4-2 | 66.7 | 20.9 | 39.4 | 1.3 |
| pin_move+sharp_gap | early | <1k bets | 2-1 | 66.7 | 16.3 | 4.3 | -0.07 |
| money_level+pin_rlm | early | <1k bets | 1-1 | 50.0 | 0.0 | -3.7 | 1.0 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 71.8 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 71.8 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 4-4 | 50.0 | 8.9 | 27.0 | 0.42 |
| money_delta+rlm_quiet | early | <1k bets | 1-2 | 33.3 | -1.7 | 23.3 | -2.8 |
| money_delta+rlm_ratio | early | <1k bets | 3-2 | 60.0 | 19.4 | 65.0 | 1.12 |
| money_delta+pin_value | early | <1k bets | 2-0 | 100.0 | 51.1 | 90.9 | 0.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -28.2 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 5-4 | 55.6 | -7.9 | -12.6 | 0.71 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -30.2 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 6-11 | 35.3 | -7.2 | -34.9 | 0.22 |
| follow_move+rlm_quiet | early | pin $1-2k | 2-5 | 28.6 | -3.2 | 16.0 | -1.07 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.4 | 29.7 | -1.02 |
| follow_move+sharp_gap | early | pin $1-2k | 9-5 | 64.3 | 8.1 | 27.7 | -0.66 |
| money_level+money_moving | early | pin $1-2k | 8-6 | 57.1 | -8.0 | -21.6 | 0.19 |
| money_level+pin_value | early | pin $1-2k | 2-4 | 33.3 | -18.7 | -37.6 | 0.78 |
| money_moving+pin_value | early | pin $1-2k | 1-3 | 25.0 | -30.2 | -54.2 | 0.93 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -9.4 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -9.4 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -10.4 | 29.7 | -1.02 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -53.2 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -40.7 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -53.2 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -40.7 | -100.0 | 2.5 |
| money_level+sharp_gap | early | pin $1-2k | 13-6 | 68.4 | 4.6 | 4.7 | -0.05 |
| money_moving+sharp_gap | early | pin $1-2k | 4-7 | 36.4 | -21.3 | -50.4 | 0.23 |
| pin_value+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -25.0 | -52.3 | -0.52 |
| consensus_gap+follow_move | early | pin $1-2k | 5-6 | 45.5 | -2.6 | -18.8 | 0.45 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 0-3 | 0.0 | -28.2 | -100.0 | -0.97 |
| follow_move+pin_value | early | pin $1-2k | 6-7 | 46.2 | -1.4 | -14.7 | -0.25 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -28.2 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 11-5 | 68.8 | 4.3 | -0.1 | 0.03 |
| money_level+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -12.5 | -1.0 | 0.75 |
| follow_move+money_moving | early | pin $1-2k | 4-2 | 66.7 | 2.8 | -10.9 | -0.15 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -28.2 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -28.2 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -16.7 | -46.8 | -0.12 |
| follow_move+pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -28.2 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | pin $1-2k | 0-1 | 0.0 | -28.2 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-3 | 0.0 | -42.7 | -100.0 | -0.67 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -28.2 | -100.0 | -4.8 |
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -28.2 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -28.2 | -100.0 | 1.3 |
| pin_move+pin_value | early | pin $1-2k | 0-2 | 0.0 | -46.8 | -100.0 | 0.0 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -71.8 | -100.0 | 1.5 |
| follow_move+pin_move | early | pin $1-2k | 0-1 | 0.0 | -46.8 | -100.0 | 0.0 |
| consensus_gap+money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.5 | -8.4 | 0.65 |
| consensus_gap+pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.2 | 83.3 | 0.0 |
| follow_move+money_level | early | pin $2k+ | 0-1 | 0.0 | -53.2 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.7 | -100.0 | 0.65 |
| follow_move+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.7 | -100.0 | 0.65 |
| money_level+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -53.2 | -100.0 | 0.0 |
| money_level+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -53.2 | -100.0 | 0.0 |
| money_moving+pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.2 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.7 | -100.0 | 0.65 |
| consensus_gap+follow_move | early | pin $2k+ | 0-1 | 0.0 | -28.2 | -100.0 | 1.3 |
| consensus_gap+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.2 | -100.0 | 1.3 |
| consensus_gap+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.2 | -100.0 | 1.3 |
| consensus_gap+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.2 | -100.0 | 1.3 |
| follow_move+money_moving | early | pin $2k+ | 0-1 | 0.0 | -28.2 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.2 | -100.0 | 1.3 |
| money_moving+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.2 | -100.0 | 1.3 |
| money_moving+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.2 | -100.0 | 1.3 |
| money_moving+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.2 | -100.0 | 1.3 |
| rlm_quiet+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.2 | -100.0 | 1.3 |
| rlm_quiet+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.2 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin limit <$1k | 5-8 | 38.5 | -6.2 | -21.5 | 0.25 |
| money_level+money_moving | early | pin limit <$1k | 14-7 | 66.7 | 15.0 | 23.6 | 0.5 |
| money_level+sharp_gap | early | pin limit <$1k | 21-16 | 56.8 | 6.4 | 4.1 | 0.16 |
| money_moving+sharp_gap | early | pin limit <$1k | 20-6 | 76.9 | 28.9 | 65.2 | 0.31 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -51.1 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 11-6 | 64.7 | 15.0 | 22.8 | 0.35 |
| money_moving+pin_value | early | pin limit <$1k | 8-4 | 66.7 | 17.2 | 26.0 | 0.25 |
| pin_value+sharp_gap | early | pin limit <$1k | 13-6 | 68.4 | 18.8 | 29.8 | 0.05 |
| consensus_gap+follow_move | early | pin limit <$1k | 7-9 | 43.8 | -7.8 | -18.4 | 0.56 |
| consensus_gap+money_level | early | pin limit <$1k | 5-7 | 41.7 | -13.2 | -28.1 | 0.42 |
| consensus_gap+pin_value | early | pin limit <$1k | 17-18 | 48.6 | -0.6 | -8.6 | 0.45 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 7-4 | 63.6 | 18.3 | 56.6 | 0.91 |
| follow_move+money_level | early | pin limit <$1k | 12-11 | 52.2 | -0.9 | -3.2 | 0.01 |
| follow_move+pin_value | early | pin limit <$1k | 17-14 | 54.8 | 5.6 | 3.4 | -0.19 |
| follow_move+sharp_gap | early | pin limit <$1k | 14-8 | 63.6 | 15.3 | 21.5 | -0.02 |
| follow_move+rlm_ratio | early | pin limit <$1k | 8-1 | 88.9 | 44.1 | 79.0 | 0.37 |
| money_level+rlm_ratio | early | pin limit <$1k | 7-0 | 100.0 | 53.8 | 92.4 | 0.5 |
| pin_value+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.6 | 43.2 | -0.25 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 8-1 | 88.9 | 44.1 | 79.0 | 0.37 |
| consensus_gap+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 51.1 | 87.1 | 0.33 |
| consensus_gap+money_moving | early | pin limit <$1k | 8-3 | 72.7 | 25.3 | 74.0 | 0.58 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 2.1 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 51.1 | 87.1 | 0.33 |
| follow_move+money_moving | early | pin limit <$1k | 10-4 | 71.4 | 22.3 | 36.5 | 0.36 |
| money_delta+money_moving | early | pin limit <$1k | 4-0 | 100.0 | 51.1 | 88.0 | 0.0 |
| money_delta+pin_value | early | pin limit <$1k | 4-0 | 100.0 | 51.1 | 88.0 | 0.0 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 53.2 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 3-2 | 60.0 | 11.1 | 13.0 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 30.2 | 54.4 | -0.2 |
| money_delta+sharp_gap | early | pin limit <$1k | 3-0 | 100.0 | 50.4 | 89.6 | 0.0 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 10.4 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | 5.7 | 13.7 | -0.05 |
| pin_move+pin_value | early | pin limit <$1k | 3-5 | 37.5 | -12.3 | -28.4 | -0.12 |
| follow_move+pin_move | early | pin limit <$1k | 6-5 | 54.5 | 3.7 | -1.7 | 0.49 |
| consensus_gap+pin_move | early | pin limit <$1k | 1-3 | 25.0 | -29.2 | -52.3 | 0.4 |
| money_level+pin_move | early | pin limit <$1k | 3-2 | 60.0 | 5.2 | 0.8 | 0.08 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -48.9 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -48.9 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 16.3 | 4.3 | -0.07 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 71.8 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 71.8 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 71.8 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 71.8 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 71.8 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 71.8 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 2-0 | 100.0 | 51.1 | 90.9 | 0.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 51.1 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 51.1 | 90.9 | 1.0 |
| rlm_quiet | close | 1-3k bets | 116-168 | 40.8 | -0.8 | -7.9 |  |
| rlm_quiet | close | 3k+ bets | 44-60 | 42.3 | -0.3 | -8.1 |  |
| rlm_quiet | close | <1k bets | 22-28 | 44.0 | 2.5 | -6.0 |  |
| rlm_quiet | close | pin $1-2k | 46-81 | 36.2 | -6.8 | -17.4 |  |
| rlm_quiet | close | pin $2k+ | 53-63 | 45.7 | 8.0 | -1.7 |  |
| rlm_quiet | close | pin limit <$1k | 36-36 | 50.0 | 0.1 | -4.2 |  |
| pin_move | close | 1-3k bets | 308-306 | 50.2 | 0.2 | -2.3 |  |
| pin_move | close | 3k+ bets | 121-126 | 49.0 | -0.6 | -5.4 |  |
| pin_move | close | <1k bets | 67-68 | 49.6 | -1.0 | -4.6 |  |
| pin_move | close | pin $1-2k | 232-229 | 50.3 | -0.1 | -1.3 |  |
| pin_move | close | pin $2k+ | 176-187 | 48.5 | -1.0 | -7.7 |  |
| pin_move | close | pin limit <$1k | 88-84 | 51.2 | 1.4 | 0.4 |  |
| money_delta | close | 1-3k bets | 199-251 | 44.2 | -0.5 | -6.2 |  |
| money_delta | close | 3k+ bets | 79-109 | 42.0 | -1.1 | -3.3 |  |
| money_delta | close | <1k bets | 38-62 | 38.0 | -4.1 | -22.9 |  |
| money_delta | close | pin $1-2k | 112-115 | 49.3 | 3.5 | 3.3 |  |
| money_delta | close | pin $2k+ | 82-112 | 42.3 | 1.0 | -9.8 |  |
| money_delta | close | pin limit <$1k | 50-54 | 48.1 | -1.7 | -3.7 |  |
| pin_rlm | close | 1-3k bets | 87-94 | 48.1 | 5.5 | 17.0 |  |
| pin_rlm | close | 3k+ bets | 32-46 | 41.0 | -1.0 | -10.3 |  |
| pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| pin_rlm | close | pin $1-2k | 61-66 | 48.0 | 4.1 | 10.9 |  |
| pin_rlm | close | pin $2k+ | 38-66 | 36.5 | 1.3 | -3.8 |  |
| pin_rlm | close | pin limit <$1k | 41-29 | 58.6 | 9.4 | 24.9 |  |
| follow_move | close | 1-3k bets | 546-478 | 53.3 | 1.7 | -4.4 |  |
| follow_move | close | 3k+ bets | 190-177 | 51.8 | -0.2 | -5.2 |  |
| follow_move | close | <1k bets | 120-108 | 52.6 | -0.6 | -11.2 |  |
| follow_move | close | pin $1-2k | 257-283 | 47.6 | -3.5 | -11.2 |  |
| follow_move | close | pin $2k+ | 220-183 | 54.6 | 2.5 | -3.7 |  |
| follow_move | close | pin limit <$1k | 106-104 | 50.5 | 0.4 | -3.7 |  |
| rlm_ratio | close | 1-3k bets | 126-155 | 44.8 | 0.0 | -3.6 |  |
| rlm_ratio | close | 3k+ bets | 48-44 | 52.2 | 7.5 | 11.8 |  |
| rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.9 | 0.8 |  |
| rlm_ratio | close | pin $1-2k | 70-73 | 49.0 | 2.4 | 2.5 |  |
| rlm_ratio | close | pin $2k+ | 38-53 | 41.8 | 3.4 | -7.6 |  |
| rlm_ratio | close | pin limit <$1k | 44-34 | 56.4 | 6.8 | 8.9 |  |
| money_level | close | 1-3k bets | 693-492 | 58.5 | 2.9 | -1.9 |  |
| money_level | close | 3k+ bets | 244-193 | 55.8 | 0.7 | -3.1 |  |
| money_level | close | <1k bets | 145-118 | 55.1 | -0.8 | -11.5 |  |
| money_level | close | pin $1-2k | 318-277 | 53.4 | -0.5 | -4.8 |  |
| money_level | close | pin $2k+ | 279-216 | 56.4 | -1.0 | -7.0 |  |
| money_level | close | pin limit <$1k | 125-120 | 51.0 | 0.9 | -3.0 |  |
| sharp_gap | close | 1-3k bets | 521-619 | 45.7 | -1.7 | -8.4 |  |
| sharp_gap | close | 3k+ bets | 210-218 | 49.1 | 1.7 | 3.4 |  |
| sharp_gap | close | <1k bets | 114-137 | 45.4 | -2.4 | -14.6 |  |
| sharp_gap | close | pin $1-2k | 275-304 | 47.5 | -1.3 | -5.2 |  |
| sharp_gap | close | pin $2k+ | 223-255 | 46.7 | 0.4 | -2.7 |  |
| sharp_gap | close | pin limit <$1k | 115-122 | 48.5 | -1.2 | -3.2 |  |
| money_moving | close | 1-3k bets | 525-617 | 46.0 | -1.9 | -8.7 |  |
| money_moving | close | 3k+ bets | 209-220 | 48.7 | 1.0 | 1.8 |  |
| money_moving | close | <1k bets | 112-137 | 45.0 | -2.5 | -13.5 |  |
| money_moving | close | pin $1-2k | 271-309 | 46.7 | -2.3 | -6.5 |  |
| money_moving | close | pin $2k+ | 224-253 | 47.0 | 0.6 | -2.7 |  |
| money_moving | close | pin limit <$1k | 111-127 | 46.6 | -3.0 | -6.8 |  |
| pin_value | close | 1-3k bets | 220-230 | 48.9 | 1.1 | 0.4 |  |
| pin_value | close | 3k+ bets | 81-86 | 48.5 | 0.0 | -5.0 |  |
| pin_value | close | <1k bets | 54-44 | 55.1 | 8.0 | 10.6 |  |
| pin_value | close | pin $1-2k | 163-184 | 47.0 | -1.3 | -4.8 |  |
| pin_value | close | pin $2k+ | 99-113 | 46.7 | 0.8 | -2.0 |  |
| pin_value | close | pin limit <$1k | 93-63 | 59.6 | 9.9 | 15.9 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.9 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.9 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 209-274 | 43.3 | -4.6 | -12.3 |  |
| consensus_gap | close | 3k+ bets | 81-95 | 46.0 | -1.4 | 5.1 |  |
| consensus_gap | close | <1k bets | 40-78 | 33.9 | -9.7 | -30.7 |  |
| consensus_gap | close | pin $1-2k | 108-119 | 47.6 | -1.5 | -1.2 |  |
| consensus_gap | close | pin $2k+ | 83-105 | 44.1 | -4.8 | -6.5 |  |
| consensus_gap | close | pin limit <$1k | 50-43 | 53.8 | 3.5 | 5.0 |  |
| consensus_gap+follow_move | close | 1-3k bets | 88-80 | 52.4 | 0.5 | -1.3 |  |
| consensus_gap+money_level | close | 1-3k bets | 140-94 | 59.8 | 1.0 | 2.5 |  |
| consensus_gap+money_moving | close | 1-3k bets | 97-149 | 39.4 | -5.7 | -9.9 |  |
| consensus_gap+pin_move | close | 1-3k bets | 53-53 | 50.0 | -1.3 | 2.5 |  |
| consensus_gap+pin_value | close | 1-3k bets | 86-100 | 46.2 | 0.6 | -1.5 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 95-152 | 38.5 | -5.8 | -11.0 |  |
| follow_move+money_level | close | 1-3k bets | 370-252 | 59.5 | 3.2 | -2.8 |  |
| follow_move+money_moving | close | 1-3k bets | 302-317 | 48.8 | -0.6 | -6.7 |  |
| follow_move+pin_move | close | 1-3k bets | 223-224 | 49.9 | -0.3 | -5.2 |  |
| follow_move+pin_value | close | 1-3k bets | 74-76 | 49.3 | 0.8 | -6.5 |  |
| follow_move+sharp_gap | close | 1-3k bets | 303-315 | 49.0 | -0.1 | -5.3 |  |
| money_level+money_moving | close | 1-3k bets | 378-332 | 53.2 | 0.8 | -3.3 |  |
| money_level+pin_move | close | 1-3k bets | 193-173 | 52.7 | -0.1 | -3.8 |  |
| money_level+pin_value | close | 1-3k bets | 111-99 | 52.9 | 3.3 | -0.8 |  |
| money_level+sharp_gap | close | 1-3k bets | 367-326 | 53.0 | 0.8 | -2.9 |  |
| money_moving+pin_move | close | 1-3k bets | 192-207 | 48.1 | -0.9 | -3.0 |  |
| money_moving+pin_value | close | 1-3k bets | 100-121 | 45.2 | -2.1 | -5.9 |  |
| money_moving+sharp_gap | close | 1-3k bets | 499-591 | 45.8 | -1.8 | -7.9 |  |
| pin_move+pin_value | close | 1-3k bets | 99-97 | 50.5 | 1.4 | -0.5 |  |
| pin_move+sharp_gap | close | 1-3k bets | 199-207 | 49.0 | 0.1 | -0.9 |  |
| pin_value+sharp_gap | close | 1-3k bets | 102-124 | 45.1 | -2.0 | -6.3 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 116-168 | 40.8 | -0.8 | -7.9 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 62-104 | 37.3 | -4.4 | -11.0 |  |
| consensus_gap+money_delta | close | 1-3k bets | 25-64 | 28.1 | -9.4 | -23.3 |  |
| follow_move+money_delta | close | 1-3k bets | 95-109 | 46.6 | -0.4 | -7.4 |  |
| money_delta+money_level | close | 1-3k bets | 74-72 | 50.7 | 2.7 | 5.0 |  |
| money_delta+money_moving | close | 1-3k bets | 139-201 | 40.9 | -2.2 | -9.8 |  |
| money_delta+pin_value | close | 1-3k bets | 44-45 | 49.4 | 2.0 | -0.9 |  |
| money_delta+sharp_gap | close | 1-3k bets | 138-199 | 40.9 | -2.2 | -9.6 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 70-80 | 46.7 | -0.9 | 0.1 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 17-27 | 38.6 | 0.9 | 16.5 |  |
| money_level+pin_rlm | close | 1-3k bets | 39-29 | 57.4 | 8.9 | 10.4 |  |
| pin_move+pin_rlm | close | 1-3k bets | 79-78 | 50.3 | 5.6 | 12.3 |  |
| pin_rlm+pin_value | close | 1-3k bets | 29-24 | 54.7 | 8.6 | 30.7 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 87-94 | 48.1 | 5.5 | 17.0 |  |
| money_delta+pin_rlm | close | 1-3k bets | 49-54 | 47.6 | 4.0 | 14.2 |  |
| money_moving+pin_rlm | close | 1-3k bets | 82-91 | 47.4 | 4.8 | 16.6 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 19-30 | 38.8 | -1.7 | 4.1 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 126-155 | 44.8 | 0.0 | -3.6 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 66-77 | 46.2 | 0.2 | -6.8 |  |
| money_level+rlm_ratio | close | 1-3k bets | 59-56 | 51.3 | 1.7 | -1.0 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 120-150 | 44.4 | -0.5 | -4.1 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 67-68 | 49.6 | 3.6 | 2.4 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 25-22 | 53.2 | 5.2 | 2.3 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 126-155 | 44.8 | 0.0 | -3.6 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 12-30 | 28.6 | -7.1 | -7.2 |  |
| follow_move+pin_rlm | close | 1-3k bets | 62-72 | 46.3 | 1.7 | -4.0 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 55-103 | 34.8 | -6.8 | -15.6 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 52-68 | 43.3 | -0.6 | -7.1 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 24-42 | 36.4 | -3.6 | -15.9 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 62-72 | 46.3 | 1.7 | -4.0 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 50-88 | 36.2 | -3.9 | -9.9 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 31-53 | 36.9 | -6.6 | -21.6 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 14-20 | 41.2 | -4.1 | -19.8 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 49.7 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 30-27 | 52.6 | 2.9 | 3.3 |  |
| consensus_gap+money_moving | close | 3k+ bets | 33-52 | 38.8 | -5.2 | 14.5 |  |
| consensus_gap+pin_move | close | 3k+ bets | 22-19 | 53.7 | 3.4 | 8.4 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-6 | 33.3 | -6.5 | 6.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 35-33 | 51.5 | 5.0 | 5.6 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -0.8 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 34-52 | 39.5 | -4.3 | 17.6 |  |
| follow_move+money_moving | close | 3k+ bets | 101-106 | 48.8 | -0.4 | -4.1 |  |
| follow_move+pin_move | close | 3k+ bets | 92-90 | 50.5 | 0.5 | -1.8 |  |
| follow_move+pin_rlm | close | 3k+ bets | 30-31 | 49.2 | 4.9 | 8.5 |  |
| follow_move+pin_value | close | 3k+ bets | 33-33 | 50.0 | 0.1 | -6.1 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 48-44 | 52.2 | 7.5 | 11.8 |  |
| follow_move+sharp_gap | close | 3k+ bets | 103-105 | 49.5 | 0.8 | -2.0 |  |
| money_moving+pin_move | close | 3k+ bets | 71-83 | 46.1 | -1.9 | -8.2 |  |
| money_moving+pin_rlm | close | 3k+ bets | 31-45 | 40.8 | -1.0 | -10.5 |  |
| money_moving+pin_value | close | 3k+ bets | 40-49 | 44.9 | -2.5 | -7.8 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 46-42 | 52.3 | 7.6 | 12.4 |  |
| money_moving+sharp_gap | close | 3k+ bets | 202-210 | 49.0 | 1.6 | 3.2 |  |
| pin_move+pin_rlm | close | 3k+ bets | 31-40 | 43.7 | 0.1 | -4.2 |  |
| pin_move+pin_value | close | 3k+ bets | 33-40 | 45.2 | -4.2 | -14.9 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 33-32 | 50.8 | 5.4 | 10.3 |  |
| pin_move+sharp_gap | close | 3k+ bets | 71-83 | 46.1 | -1.6 | -7.6 |  |
| pin_rlm+pin_value | close | 3k+ bets | 6-15 | 28.6 | -17.5 | -45.5 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 30-31 | 49.2 | 4.9 | 8.5 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 32-46 | 41.0 | -1.0 | -10.3 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 9-10 | 47.4 | -2.9 | -10.1 |  |
| pin_value+sharp_gap | close | 3k+ bets | 40-48 | 45.5 | -2.0 | -6.7 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 48-44 | 52.2 | 7.5 | 11.8 |  |
| follow_move+money_delta | close | 3k+ bets | 38-47 | 44.7 | -0.5 | -7.2 |  |
| money_level+money_moving | close | 3k+ bets | 142-121 | 54.0 | 1.9 | 0.0 |  |
| money_level+sharp_gap | close | 3k+ bets | 141-118 | 54.4 | 2.5 | 1.5 |  |
| follow_move+money_level | close | 3k+ bets | 119-90 | 56.9 | 0.6 | -3.4 |  |
| money_level+rlm_ratio | close | 3k+ bets | 23-12 | 65.7 | 18.8 | 35.2 |  |
| consensus_gap+money_level | close | 3k+ bets | 44-44 | 50.0 | -6.5 | -13.3 |  |
| money_level+pin_move | close | 3k+ bets | 66-61 | 52.0 | -1.4 | -4.5 |  |
| money_level+pin_value | close | 3k+ bets | 45-43 | 51.1 | 0.9 | -5.2 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 7-12 | 36.8 | -0.8 | -5.4 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 44-60 | 42.3 | -0.3 | -8.1 |  |
| money_delta+money_moving | close | 3k+ bets | 60-83 | 42.0 | -0.2 | 1.4 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 19-24 | 44.2 | 2.7 | 2.2 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 23-32 | 41.8 | -0.3 | -6.0 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 21-31 | 40.4 | -1.7 | -8.0 |  |
| consensus_gap+money_delta | close | 3k+ bets | 12-23 | 34.3 | -4.0 | 18.4 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 10-24 | 29.4 | -13.2 | -34.9 |  |
| money_delta+sharp_gap | close | 3k+ bets | 58-80 | 42.0 | 0.0 | 2.1 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 26-30 | 46.4 | 2.4 | 0.6 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 11-17 | 39.3 | -2.7 | -6.7 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 7-12 | 36.8 | -13.1 | -29.6 |  |
| money_delta+money_level | close | 3k+ bets | 31-22 | 58.5 | 12.6 | 18.5 |  |
| money_level+pin_rlm | close | 3k+ bets | 15-9 | 62.5 | 17.8 | 34.6 |  |
| money_delta+pin_value | close | 3k+ bets | 18-19 | 48.6 | 2.7 | -8.3 |  |
| money_delta+pin_move | close | 3k+ bets | 35-42 | 45.5 | 0.2 | -7.0 |  |
| money_delta+pin_rlm | close | 3k+ bets | 21-27 | 43.8 | 2.1 | -6.6 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 28-24 | 53.8 | 9.4 | 14.8 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 47.9 | 87.7 |  |
| money_level+money_moving | close | <1k bets | 76-77 | 49.7 | -2.8 | -14.4 |  |
| money_level+sharp_gap | close | <1k bets | 79-77 | 50.6 | -2.2 | -13.9 |  |
| money_moving+sharp_gap | close | <1k bets | 110-135 | 44.9 | -2.7 | -14.7 |  |
| consensus_gap+money_level | close | <1k bets | 18-27 | 40.0 | -15.9 | -39.4 |  |
| consensus_gap+money_moving | close | <1k bets | 17-40 | 29.8 | -11.7 | -34.9 |  |
| consensus_gap+pin_move | close | <1k bets | 6-13 | 31.6 | -18.2 | -26.5 |  |
| consensus_gap+pin_value | close | <1k bets | 14-14 | 50.0 | 8.1 | 15.4 |  |
| consensus_gap+sharp_gap | close | <1k bets | 17-41 | 29.3 | -12.0 | -36.0 |  |
| money_level+pin_move | close | <1k bets | 34-35 | 49.3 | -5.1 | -13.5 |  |
| money_level+pin_value | close | <1k bets | 18-17 | 51.4 | 1.2 | -4.2 |  |
| money_moving+pin_move | close | <1k bets | 36-41 | 46.8 | -1.1 | -4.2 |  |
| money_moving+pin_value | close | <1k bets | 17-16 | 51.5 | 6.2 | 14.9 |  |
| pin_move+pin_value | close | <1k bets | 25-20 | 55.6 | 7.3 | 12.9 |  |
| pin_move+sharp_gap | close | <1k bets | 36-42 | 46.2 | -2.3 | -9.5 |  |
| pin_value+sharp_gap | close | <1k bets | 17-15 | 53.1 | 7.2 | 18.5 |  |
| follow_move+money_delta | close | <1k bets | 18-20 | 47.4 | 4.9 | -3.2 |  |
| follow_move+money_moving | close | <1k bets | 54-63 | 46.2 | -3.5 | -13.8 |  |
| follow_move+pin_move | close | <1k bets | 42-42 | 50.0 | -1.3 | -7.2 |  |
| follow_move+sharp_gap | close | <1k bets | 56-63 | 47.1 | -3.4 | -16.1 |  |
| money_delta+money_moving | close | <1k bets | 27-46 | 37.0 | -3.0 | -23.1 |  |
| money_delta+pin_move | close | <1k bets | 13-17 | 43.3 | -0.6 | -15.5 |  |
| money_delta+sharp_gap | close | <1k bets | 27-46 | 37.0 | -3.0 | -23.1 |  |
| follow_move+rlm_quiet | close | <1k bets | 22-28 | 44.0 | 2.5 | -6.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.9 | 0.8 |  |
| money_delta+rlm_quiet | close | <1k bets | 8-10 | 44.4 | 4.9 | -4.3 |  |
| money_delta+rlm_ratio | close | <1k bets | 16-15 | 51.6 | 10.0 | 6.3 |  |
| money_moving+rlm_quiet | close | <1k bets | 14-12 | 53.8 | 12.9 | 20.2 |  |
| money_moving+rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.9 | 0.8 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 10-10 | 50.0 | 10.4 | 5.6 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 13-13 | 50.0 | 8.1 | 3.3 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 26-26 | 50.0 | 6.9 | 0.8 |  |
| follow_move+money_level | close | <1k bets | 75-59 | 56.0 | -2.3 | -15.1 |  |
| consensus_gap+money_delta | close | <1k bets | 4-22 | 15.4 | -16.5 | -63.0 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -1.3 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 12-14 | 46.2 | 7.9 | -0.2 |  |
| money_moving+pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| pin_rlm+sharp_gap | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| money_delta+pin_value | close | <1k bets | 6-8 | 42.9 | -3.1 | -19.4 |  |
| consensus_gap+follow_move | close | <1k bets | 9-20 | 31.0 | -19.1 | -51.4 |  |
| follow_move+pin_rlm | close | <1k bets | 16-11 | 59.3 | 16.2 | 17.3 |  |
| follow_move+pin_value | close | <1k bets | 18-12 | 60.0 | 11.2 | 13.8 |  |
| pin_move+pin_rlm | close | <1k bets | 19-16 | 54.3 | 10.9 | 15.0 |  |
| pin_move+rlm_quiet | close | <1k bets | 10-10 | 50.0 | 4.8 | 9.6 |  |
| pin_move+rlm_ratio | close | <1k bets | 16-13 | 55.2 | 10.1 | 7.8 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 21.4 | 60.8 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 7-5 | 58.3 | 16.0 | 15.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 16-11 | 59.3 | 16.2 | 17.3 |  |
| pin_value+rlm_quiet | close | <1k bets | 3-4 | 42.9 | -6.6 | -17.6 |  |
| pin_value+rlm_ratio | close | <1k bets | 4-1 | 80.0 | 30.7 | 51.7 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 2-7 | 22.2 | -12.0 | -57.2 |  |
| money_delta+money_level | close | <1k bets | 12-17 | 41.4 | -2.1 | -18.9 |  |
| money_level+rlm_ratio | close | <1k bets | 13-13 | 50.0 | 4.7 | -1.9 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 17.6 | 19.0 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 0-5 | 0.0 | -35.6 | -100.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 41-46 | 47.1 | -5.1 | -9.7 |  |
| consensus_gap+money_moving | close | pin $1-2k | 53-64 | 45.3 | -3.1 | -3.4 |  |
| consensus_gap+pin_move | close | pin $1-2k | 42-43 | 49.4 | -3.2 | 4.6 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-18 | 41.9 | 1.0 | 25.8 |  |
| consensus_gap+pin_value | close | pin $1-2k | 65-70 | 48.1 | 2.2 | -3.5 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-14 | 50.0 | 4.5 | 9.0 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 51-62 | 45.1 | -2.1 | -2.4 |  |
| follow_move+money_moving | close | pin $1-2k | 152-187 | 44.8 | -5.0 | -12.0 |  |
| follow_move+pin_move | close | pin $1-2k | 164-172 | 48.8 | -1.9 | -6.3 |  |
| follow_move+pin_rlm | close | pin $1-2k | 49-50 | 49.5 | 3.4 | 4.4 |  |
| follow_move+pin_value | close | pin $1-2k | 56-67 | 45.5 | -3.9 | -14.1 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 70-73 | 49.0 | 2.4 | 2.5 |  |
| follow_move+sharp_gap | close | pin $1-2k | 155-184 | 45.7 | -4.0 | -10.7 |  |
| money_moving+pin_move | close | pin $1-2k | 144-163 | 46.9 | -2.4 | -4.5 |  |
| money_moving+pin_rlm | close | pin $1-2k | 58-64 | 47.5 | 3.3 | 10.3 |  |
| money_moving+pin_value | close | pin $1-2k | 65-97 | 40.1 | -7.7 | -21.3 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 68-70 | 49.3 | 2.3 | 3.1 |  |
| money_moving+sharp_gap | close | pin $1-2k | 263-296 | 47.0 | -1.7 | -5.7 |  |
| pin_move+pin_rlm | close | pin $1-2k | 58-60 | 49.2 | 3.9 | 10.9 |  |
| pin_move+pin_value | close | pin $1-2k | 70-87 | 44.6 | -5.0 | -13.8 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 57-54 | 51.4 | 4.2 | 6.4 |  |
| pin_move+sharp_gap | close | pin $1-2k | 147-162 | 47.6 | -1.5 | -3.6 |  |
| pin_rlm+pin_value | close | pin $1-2k | 15-25 | 37.5 | -10.9 | -21.7 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 49-50 | 49.5 | 3.4 | 4.4 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 61-66 | 48.0 | 4.1 | 10.9 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 18-21 | 46.2 | -3.6 | -12.9 |  |
| pin_value+sharp_gap | close | pin $1-2k | 65-94 | 40.9 | -6.8 | -19.9 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 70-73 | 49.0 | 2.4 | 2.5 |  |
| follow_move+money_level | close | pin $1-2k | 178-169 | 51.3 | -3.1 | -10.0 |  |
| money_level+rlm_ratio | close | pin $1-2k | 40-33 | 54.8 | 6.2 | 6.9 |  |
| money_level+sharp_gap | close | pin $1-2k | 197-192 | 50.6 | -1.1 | -5.9 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 3-11 | 21.4 | -20.4 | -31.6 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 46-81 | 36.2 | -6.8 | -17.4 |  |
| money_level+money_moving | close | pin $1-2k | 196-196 | 50.0 | -1.9 | -7.2 |  |
| consensus_gap+money_level | close | pin $1-2k | 63-56 | 52.9 | -3.9 | -6.3 |  |
| money_level+pin_value | close | pin $1-2k | 74-77 | 49.0 | -0.9 | -8.3 |  |
| money_level+pin_move | close | pin $1-2k | 142-133 | 51.6 | -1.3 | -5.7 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 23-39 | 37.1 | -7.0 | -7.9 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 33-46 | 41.8 | -3.5 | -4.5 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 15-26 | 36.6 | -7.9 | -10.6 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 20-32 | 38.5 | -4.9 | -5.1 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 24-40 | 37.5 | -6.5 | -10.1 |  |
| money_level+pin_rlm | close | pin $1-2k | 29-23 | 55.8 | 9.1 | 9.7 |  |
| follow_move+money_delta | close | pin $1-2k | 54-57 | 48.6 | 2.4 | 0.4 |  |
| money_delta+money_moving | close | pin $1-2k | 77-92 | 45.6 | 1.1 | -1.0 |  |
| money_delta+pin_move | close | pin $1-2k | 58-63 | 47.9 | 0.6 | 1.8 |  |
| money_delta+pin_rlm | close | pin $1-2k | 37-42 | 46.8 | 3.2 | 8.6 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 42-41 | 50.6 | 4.5 | 6.6 |  |
| money_delta+sharp_gap | close | pin $1-2k | 77-90 | 46.1 | 1.6 | 0.2 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 47.9 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 42-37 | 53.2 | 5.2 | 3.5 |  |
| consensus_gap+money_delta | close | pin $1-2k | 16-25 | 39.0 | -2.0 | -7.9 |  |
| money_delta+pin_value | close | pin $1-2k | 37-42 | 46.8 | -1.6 | -11.5 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 12-25 | 32.4 | -10.2 | -19.9 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 8-22 | 26.7 | -22.5 | -48.8 |  |
| consensus_gap+follow_move | close | pin $2k+ | 27-28 | 49.1 | -2.0 | -17.0 |  |
| consensus_gap+money_delta | close | pin $2k+ | 7-26 | 21.2 | -11.2 | -58.2 |  |
| consensus_gap+money_level | close | pin $2k+ | 54-46 | 54.0 | -8.6 | -15.6 |  |
| consensus_gap+money_moving | close | pin $2k+ | 31-61 | 33.7 | -9.2 | -8.7 |  |
| consensus_gap+pin_move | close | pin $2k+ | 24-32 | 42.9 | -6.3 | -18.5 |  |
| consensus_gap+pin_value | close | pin $2k+ | 34-46 | 42.5 | 1.0 | 6.1 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-13 | 0.0 | -30.6 | -100.0 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 33-64 | 34.0 | -9.5 | -8.1 |  |
| follow_move+money_delta | close | pin $2k+ | 31-38 | 44.9 | 2.5 | -6.6 |  |
| follow_move+money_level | close | pin $2k+ | 139-88 | 61.2 | 1.8 | -2.0 |  |
| follow_move+money_moving | close | pin $2k+ | 107-104 | 50.7 | 2.8 | -3.0 |  |
| follow_move+pin_move | close | pin $2k+ | 133-124 | 51.8 | 1.8 | -2.5 |  |
| follow_move+pin_value | close | pin $2k+ | 33-31 | 51.6 | 4.3 | -2.4 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 38-53 | 41.8 | 3.4 | -7.6 |  |
| follow_move+sharp_gap | close | pin $2k+ | 108-105 | 50.7 | 2.9 | -2.7 |  |
| money_delta+money_level | close | pin $2k+ | 24-21 | 53.3 | 9.1 | 8.1 |  |
| money_delta+money_moving | close | pin $2k+ | 56-80 | 41.2 | 2.4 | -8.2 |  |
| money_delta+pin_move | close | pin $2k+ | 31-46 | 40.3 | -2.4 | -17.0 |  |
| money_delta+pin_value | close | pin $2k+ | 18-22 | 45.0 | 2.2 | -14.0 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 19-24 | 44.2 | 5.0 | -4.0 |  |
| money_delta+sharp_gap | close | pin $2k+ | 54-79 | 40.6 | 1.8 | -9.3 |  |
| money_level+money_moving | close | pin $2k+ | 150-133 | 53.0 | 0.2 | -3.8 |  |
| money_level+pin_move | close | pin $2k+ | 101-89 | 53.2 | -1.9 | -6.0 |  |
| money_level+pin_value | close | pin $2k+ | 54-50 | 51.9 | 2.1 | -4.0 |  |
| money_level+rlm_ratio | close | pin $2k+ | 14-13 | 51.9 | 5.3 | 8.9 |  |
| money_level+sharp_gap | close | pin $2k+ | 150-134 | 52.8 | 0.0 | -3.7 |  |
| money_moving+pin_move | close | pin $2k+ | 96-107 | 47.3 | 0.3 | -5.6 |  |
| money_moving+pin_value | close | pin $2k+ | 56-64 | 46.7 | 1.6 | 6.4 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 38-52 | 42.2 | 3.7 | -6.6 |  |
| money_moving+sharp_gap | close | pin $2k+ | 218-249 | 46.7 | 0.5 | -2.5 |  |
| pin_move+pin_value | close | pin $2k+ | 46-45 | 50.5 | 2.9 | -0.7 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 27-37 | 42.2 | 2.4 | -3.7 |  |
| pin_move+sharp_gap | close | pin $2k+ | 96-108 | 47.1 | 0.0 | -5.6 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 4-7 | 36.4 | -5.6 | -26.4 |  |
| pin_value+sharp_gap | close | pin $2k+ | 56-65 | 46.3 | 1.4 | 5.5 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 38-53 | 41.8 | 3.4 | -7.6 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-20 | 16.7 | -12.0 | -27.9 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 4-13 | 23.5 | -4.4 | -49.8 |  |
| follow_move+pin_rlm | close | pin $2k+ | 27-42 | 39.1 | 1.7 | -10.6 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 53-63 | 45.7 | 8.0 | -1.7 |  |
| money_moving+pin_rlm | close | pin $2k+ | 38-66 | 36.5 | 1.3 | -3.8 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 26-36 | 41.9 | 6.7 | -5.7 |  |
| pin_move+pin_rlm | close | pin $2k+ | 31-45 | 40.8 | 3.0 | -4.5 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 35-41 | 46.1 | 6.2 | -0.0 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 13-28 | 31.7 | -0.3 | -21.9 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 27-42 | 39.1 | 1.7 | -10.6 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 38-66 | 36.5 | 1.3 | -3.8 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 20-33 | 37.7 | 5.2 | -11.5 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 26-37 | 41.3 | 6.2 | -7.2 |  |
| money_delta+pin_rlm | close | pin $2k+ | 21-36 | 36.8 | 1.3 | -8.3 |  |
| money_level+pin_rlm | close | pin $2k+ | 15-9 | 62.5 | 20.1 | 32.4 |  |
| pin_rlm+pin_value | close | pin $2k+ | 6-13 | 31.6 | -4.3 | 13.6 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 16-20 | 44.4 | 5.7 | -7.5 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 4-7 | 36.4 | -0.5 | -26.4 |  |
| follow_move+money_delta | close | pin limit <$1k | 31-37 | 45.6 | -4.3 | -12.5 |  |
| money_level+money_moving | close | pin limit <$1k | 69-76 | 47.6 | -2.2 | -8.7 |  |
| money_level+sharp_gap | close | pin limit <$1k | 68-71 | 48.9 | -0.9 | -6.1 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 104-113 | 47.9 | -1.7 | -4.0 |  |
| consensus_gap+money_level | close | pin limit <$1k | 28-25 | 52.8 | 2.3 | -2.4 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 15-10 | 60.0 | 11.3 | 30.2 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 36-31 | 53.7 | 4.4 | 7.6 |  |
| follow_move+money_moving | close | pin limit <$1k | 65-73 | 47.1 | -2.6 | -9.5 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 70-73 | 49.0 | -0.8 | -6.0 |  |
| money_level+pin_move | close | pin limit <$1k | 50-47 | 51.5 | 1.6 | -1.6 |  |
| money_level+pin_value | close | pin limit <$1k | 46-32 | 59.0 | 9.3 | 11.5 |  |
| pin_move+pin_value | close | pin limit <$1k | 41-25 | 62.1 | 12.6 | 24.7 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 18-10 | 64.3 | 14.1 | 18.0 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 22-17 | 56.4 | 7.3 | 17.8 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 24-18 | 57.1 | 7.9 | 18.4 |  |
| follow_move+money_level | close | pin limit <$1k | 54-54 | 50.0 | -0.2 | -4.8 |  |
| follow_move+pin_move | close | pin limit <$1k | 60-60 | 50.0 | 0.2 | -4.3 |  |
| follow_move+pin_value | close | pin limit <$1k | 36-23 | 61.0 | 11.3 | 15.7 |  |
| money_moving+pin_move | close | pin limit <$1k | 59-61 | 49.2 | -0.5 | -2.3 |  |
| money_moving+pin_value | close | pin limit <$1k | 36-25 | 59.0 | 9.6 | 19.2 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 63-62 | 50.4 | 0.7 | -0.1 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 38-28 | 57.6 | 8.0 | 16.0 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 36-36 | 50.0 | 0.1 | -4.2 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 25-26 | 49.0 | -0.8 | -6.1 |  |
| money_delta+money_moving | close | pin limit <$1k | 43-45 | 48.9 | -0.8 | -1.4 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 7-6 | 53.8 | 5.8 | 35.2 |  |
| money_delta+money_level | close | pin limit <$1k | 25-19 | 56.8 | 6.7 | 8.8 |  |
| money_delta+pin_value | close | pin limit <$1k | 13-8 | 61.9 | 13.0 | 38.5 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 42-43 | 49.4 | -0.2 | -0.3 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 29-30 | 49.2 | -0.4 | 1.6 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 6-2 | 75.0 | 28.0 | 96.7 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 24-17 | 58.5 | 9.4 | 23.0 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 38-27 | 58.5 | 9.3 | 25.7 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 40-29 | 58.0 | 8.4 | 17.5 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-4 | 82.6 | 33.5 | 76.8 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 41-29 | 58.6 | 9.4 | 24.9 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 4-1 | 80.0 | 29.9 | 51.3 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 12-7 | 63.2 | 13.1 | 20.9 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 9-17 | 34.6 | -14.9 | -33.8 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 20-21 | 48.8 | -0.9 | -6.4 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 32-22 | 59.3 | 9.5 | 14.0 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 44-34 | 56.4 | 6.8 | 8.9 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 25-21 | 54.3 | 4.6 | 4.4 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 19-25 | 43.2 | -6.6 | -17.1 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 40-32 | 55.6 | 6.0 | 7.4 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 32-22 | 59.3 | 9.5 | 14.0 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 14-10 | 58.3 | 9.0 | 11.9 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 32-22 | 59.3 | 9.5 | 14.0 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 21-18 | 53.8 | 4.2 | 3.2 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 44-34 | 56.4 | 6.8 | 8.9 |  |
| money_level+pin_rlm | close | pin limit <$1k | 19-12 | 61.3 | 11.1 | 17.6 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 21-14 | 60.0 | 10.5 | 16.8 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 16-5 | 76.2 | 26.1 | 46.1 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 5-3 | 62.5 | 12.6 | 18.4 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 49.7 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -3.4 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -50.9 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 27-28 | 49.1 | 13.9 | 21.6 | 0.24 |
| rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -14.2 | -3.3 | -0.95 |
| rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| rlm_quiet | early | pin limit <$1k | 5-7 | 41.7 | -2.3 | -15.0 | 0.27 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -49.7 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 5-8 | 38.5 | -9.6 | -31.5 | 0.32 |
| pin_move | early | pin $1-2k | 0-3 | 0.0 | -35.1 | -100.0 | 0.23 |
| pin_move | early | pin limit <$1k | 5-6 | 45.5 | -6.3 | -19.1 | 0.22 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.8 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 8-6 | 57.1 | 17.0 | 26.7 | -0.34 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -39.4 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 4-0 | 100.0 | 50.5 | 88.0 | -0.25 |
| pin_rlm | early | <1k bets | 1-2 | 33.3 | 6.7 | -35.8 | -1.0 |
| pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -26.6 | -100.0 | -1.75 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.3 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -50.9 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 394-323 | 55.0 | 2.6 | -4.6 | 0.2 |
| follow_move | early | pin $1-2k | 27-17 | 61.4 | 7.2 | 9.4 | -0.34 |
| follow_move | early | pin $2k+ | 0-2 | 0.0 | -39.4 | -100.0 | 0.65 |
| follow_move | early | pin limit <$1k | 47-39 | 54.7 | 4.4 | 1.9 | -0.11 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 23-13 | 63.9 | 26.8 | 41.4 | 0.6 |
| rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.2 | 55.6 | -1.52 |
| rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -39.4 | -100.0 | 0.65 |
| rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 0.9 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 42.8 | 59.7 | 0.33 |
| money_level | early | <1k bets | 140-89 | 61.1 | 1.4 | -4.4 | -0.16 |
| money_level | early | pin $1-2k | 21-8 | 72.4 | 7.3 | 7.1 | 0.01 |
| money_level | early | pin $2k+ | 1-1 | 50.0 | -12.7 | -47.2 | -0.7 |
| money_level | early | pin limit <$1k | 24-26 | 48.0 | -5.2 | -11.4 | 0.22 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.5 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.1 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 116-98 | 54.2 | 5.6 | 4.5 | 0.35 |
| sharp_gap | early | pin $1-2k | 16-11 | 59.3 | 6.4 | 9.8 | -0.37 |
| sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -39.4 | -100.0 | 0.65 |
| sharp_gap | early | pin limit <$1k | 29-18 | 61.7 | 13.1 | 27.9 | 0.12 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.5 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.9 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 78-69 | 53.1 | 1.2 | -7.7 | 0.01 |
| money_moving | early | pin $1-2k | 8-9 | 47.1 | -11.0 | -35.5 | 0.2 |
| money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.7 | -8.4 | 0.65 |
| money_moving | early | pin limit <$1k | 23-9 | 71.9 | 22.7 | 52.0 | 0.42 |
| pin_value | early | 1-3k bets | 13-10 | 56.5 | 8.0 | 6.3 | -0.04 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 36-39 | 48.0 | -0.3 | -9.2 | 0.13 |
| pin_value | early | pin $1-2k | 13-19 | 40.6 | -5.2 | -23.6 | 0.12 |
| pin_value | early | pin $2k+ | 1-0 | 100.0 | 52.1 | 83.3 | 0.0 |
| pin_value | early | pin limit <$1k | 36-30 | 54.5 | 5.0 | 3.2 | 0.09 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -49.7 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -26.7 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.3 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.7 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 175-236 | 42.6 | -4.8 | -14.8 | 0.36 |
| consensus_gap | early | pin $1-2k | 12-20 | 37.5 | -7.9 | -28.2 | 0.51 |
| consensus_gap | early | pin $2k+ | 1-1 | 50.0 | 12.7 | -8.4 | 0.65 |
| consensus_gap | early | pin limit <$1k | 18-34 | 34.6 | -15.5 | -28.2 | 0.28 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.8 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.8 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -0.9 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.1 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 4.7 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.1 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 7-4 | 63.6 | 13.9 | 19.4 | -0.09 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.4 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.6 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -49.7 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -1.0 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 6-5 | 54.5 | 8.0 | 1.3 | 0.27 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -0.4 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-7 | 50.0 | 2.5 | -6.4 | -0.29 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -3.4 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.1 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.2 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.5 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 2.7 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.5 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.6 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.1 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.6 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 52.1 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 12.3 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 18.9 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 17.6 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 17.6 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| follow_move+rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -50.9 | -100.0 | -0.5 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.9 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| rlm_quiet+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| rlm_quiet+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 38.2 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 49.7 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 26-33 | 44.1 | -7.7 | -19.4 | 0.84 |
| consensus_gap+money_level | early | <1k bets | 27-21 | 56.2 | -9.1 | -11.4 | 0.36 |
| consensus_gap+sharp_gap | early | <1k bets | 22-38 | 36.7 | -10.1 | -18.6 | 1.0 |
| follow_move+money_level | early | <1k bets | 76-33 | 69.7 | 8.3 | 2.7 | -0.01 |
| follow_move+sharp_gap | early | <1k bets | 63-27 | 70.0 | 19.4 | 23.6 | 0.49 |
| money_level+sharp_gap | early | <1k bets | 79-47 | 62.7 | 6.1 | 2.0 | 0.15 |
| follow_move+money_moving | early | <1k bets | 41-23 | 64.1 | 9.8 | 10.2 | 0.33 |
| money_level+money_moving | early | <1k bets | 49-34 | 59.0 | -0.0 | -7.1 | -0.29 |
| money_moving+sharp_gap | early | <1k bets | 46-40 | 53.5 | 3.9 | -3.9 | 0.18 |
| consensus_gap+money_moving | early | <1k bets | 10-19 | 34.5 | -13.7 | -44.4 | 0.26 |
| follow_move+pin_value | early | <1k bets | 13-11 | 54.2 | 4.5 | 1.3 | -0.01 |
| follow_move+rlm_quiet | early | <1k bets | 27-28 | 49.1 | 13.9 | 21.6 | 0.24 |
| money_moving+rlm_quiet | early | <1k bets | 9-8 | 52.9 | 16.7 | 29.1 | 0.44 |
| rlm_quiet+sharp_gap | early | <1k bets | 16-10 | 61.5 | 25.9 | 39.2 | -0.02 |
| follow_move+rlm_ratio | early | <1k bets | 23-13 | 63.9 | 26.8 | 41.4 | 0.6 |
| rlm_quiet+rlm_ratio | early | <1k bets | 14-7 | 66.7 | 31.1 | 54.1 | 0.02 |
| rlm_ratio+sharp_gap | early | <1k bets | 23-13 | 63.9 | 26.8 | 41.4 | 0.6 |
| pin_move+pin_value | early | <1k bets | 1-4 | 20.0 | -29.1 | -61.8 | 0.2 |
| follow_move+pin_move | early | <1k bets | 5-3 | 62.5 | 10.3 | 11.2 | 0.42 |
| consensus_gap+pin_value | early | <1k bets | 13-23 | 36.1 | -10.4 | -32.5 | 0.4 |
| pin_value+rlm_quiet | early | <1k bets | 0-3 | 0.0 | -43.0 | -100.0 | -0.6 |
| money_delta+money_moving | early | <1k bets | 7-6 | 53.8 | 14.5 | 21.7 | -0.36 |
| money_delta+sharp_gap | early | <1k bets | 6-4 | 60.0 | 21.6 | 39.1 | -0.47 |
| consensus_gap+pin_move | early | <1k bets | 0-5 | 0.0 | -44.5 | -100.0 | 0.26 |
| money_level+pin_move | early | <1k bets | 2-2 | 50.0 | -5.8 | -21.8 | 0.1 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| consensus_gap+rlm_quiet | early | <1k bets | 3-5 | 37.5 | -1.0 | -22.7 | 1.01 |
| consensus_gap+rlm_ratio | early | <1k bets | 4-3 | 57.1 | 17.0 | 15.6 | 0.6 |
| follow_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 23.4 | -3.7 | -2.15 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | <1k bets | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 23.4 | -3.7 | -2.15 |
| pin_rlm+sharp_gap | early | <1k bets | 1-2 | 33.3 | 6.7 | -35.8 | -1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 11.5 | -4.5 | -1.9 |
| pin_value+sharp_gap | early | <1k bets | 5-4 | 55.6 | 8.4 | 6.1 | -0.09 |
| money_level+pin_value | early | <1k bets | 4-4 | 50.0 | 0.1 | -4.5 | 0.88 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -51.2 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -50.3 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 1-2 | 33.3 | -17.4 | -36.4 | 1.33 |
| money_level+rlm_ratio | early | <1k bets | 7-6 | 53.8 | 16.3 | 12.9 | 1.69 |
| money_moving+rlm_ratio | early | <1k bets | 9-5 | 64.3 | 22.7 | 48.0 | 0.36 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 50.3 | 90.9 | 0.0 |
| money_delta+money_level | early | <1k bets | 3-1 | 75.0 | 30.8 | 61.5 | 1.2 |
| pin_move+sharp_gap | early | <1k bets | 2-1 | 66.7 | 16.8 | 4.3 | -0.07 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 3-3 | 50.0 | 11.5 | 37.5 | 0.07 |
| money_delta+rlm_quiet | early | <1k bets | 1-2 | 33.3 | -1.2 | 23.3 | -2.8 |
| money_delta+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 32.1 | 111.3 | 0.87 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 49.7 | 90.9 | -1.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 5-4 | 55.6 | -9.3 | -12.6 | 0.71 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -31.5 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 5-10 | 33.3 | -8.0 | -38.7 | 0.31 |
| follow_move+rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -14.2 | -3.3 | -0.95 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.2 | 55.6 | -1.52 |
| follow_move+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 13.8 | 37.5 | -0.83 |
| money_level+money_moving | early | pin $1-2k | 8-5 | 61.5 | -4.3 | -15.6 | 0.07 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.7 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-2 | 33.3 | -16.8 | -38.9 | 0.67 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -8.0 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -8.0 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-3 | 40.0 | 3.2 | 55.6 | -1.52 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -39.4 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -39.4 | -100.0 | 2.5 |
| money_level+sharp_gap | early | pin $1-2k | 13-4 | 76.5 | 12.7 | 17.1 | -0.25 |
| money_moving+sharp_gap | early | pin $1-2k | 4-6 | 40.0 | -16.8 | -45.4 | 0.08 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.9 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 4-6 | 40.0 | -10.0 | -31.3 | 0.34 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 0-3 | 0.0 | -26.6 | -100.0 | -0.97 |
| follow_move+pin_value | early | pin $1-2k | 6-6 | 50.0 | 2.3 | -7.6 | -0.27 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -26.6 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 11-4 | 73.3 | 8.2 | 6.6 | -0.07 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 47.9 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 4-2 | 66.7 | 1.4 | -10.9 | -0.15 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -16.7 | -46.8 | -0.12 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -26.6 | -100.0 | -1.75 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -26.6 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.7 | -8.4 | 0.65 |
| consensus_gap+pin_value | early | pin $2k+ | 1-0 | 100.0 | 52.1 | 83.3 | 0.0 |
| follow_move+money_level | early | pin $2k+ | 0-1 | 0.0 | -52.1 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -39.4 | -100.0 | 0.65 |
| follow_move+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -39.4 | -100.0 | 0.65 |
| money_level+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -52.1 | -100.0 | 0.0 |
| money_level+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -52.1 | -100.0 | 0.0 |
| money_moving+pin_value | early | pin $2k+ | 1-0 | 100.0 | 52.1 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -39.4 | -100.0 | 0.65 |
| consensus_gap+follow_move | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| follow_move+money_moving | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| money_moving+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| money_moving+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| money_moving+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| rlm_quiet+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| rlm_quiet+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin limit <$1k | 5-7 | 41.7 | -2.3 | -15.0 | 0.27 |
| money_level+money_moving | early | pin limit <$1k | 13-7 | 65.0 | 12.7 | 20.2 | 0.48 |
| money_level+sharp_gap | early | pin limit <$1k | 20-16 | 55.6 | 4.9 | 1.6 | 0.14 |
| money_moving+sharp_gap | early | pin limit <$1k | 18-5 | 78.3 | 30.3 | 70.1 | 0.35 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -49.7 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 9-6 | 60.0 | 9.9 | 13.8 | 0.33 |
| money_moving+pin_value | early | pin limit <$1k | 7-4 | 63.6 | 13.8 | 20.1 | 0.18 |
| pin_value+sharp_gap | early | pin limit <$1k | 12-6 | 66.7 | 16.7 | 26.4 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-9 | 40.0 | -12.0 | -25.7 | 0.53 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -26.6 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 14-18 | 43.8 | -5.2 | -17.9 | 0.43 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.1 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 11-11 | 50.0 | -3.9 | -7.4 | -0.04 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 4.5 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 13-7 | 65.0 | 16.5 | 24.2 | -0.07 |
| follow_move+rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level+rlm_ratio | early | pin limit <$1k | 6-0 | 100.0 | 53.7 | 92.6 | 0.42 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 16.6 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| consensus_gap+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 22.8 | 72.3 | 0.54 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 0.9 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 9-3 | 75.0 | 25.5 | 43.3 | 0.33 |
| money_delta+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_delta+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 52.1 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 3-1 | 75.0 | 25.5 | 41.3 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.0 | 45.3 | -0.5 |
| money_delta+sharp_gap | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 | -0.5 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 11.8 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 24.5 | 51.6 | -0.07 |
| pin_move+pin_value | early | pin limit <$1k | 1-4 | 20.0 | -29.1 | -61.8 | 0.2 |
| follow_move+pin_move | early | pin limit <$1k | 5-3 | 62.5 | 10.3 | 11.2 | 0.42 |
| consensus_gap+pin_move | early | pin limit <$1k | 0-3 | 0.0 | -56.4 | -100.0 | 0.53 |
| money_level+pin_move | early | pin limit <$1k | 2-2 | 50.0 | -5.8 | -21.8 | 0.1 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -50.3 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -50.3 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 16.8 | 4.3 | -0.07 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 49.7 | 90.9 | -1.0 |
| rlm_quiet | close | 1-3k bets | 35-57 | 38.0 | -3.7 | -9.6 |  |
| rlm_quiet | close | 3k+ bets | 3-8 | 27.3 | -15.7 | -42.9 |  |
| rlm_quiet | close | <1k bets | 4-17 | 19.0 | -22.5 | -63.3 |  |
| rlm_quiet | close | pin $1-2k | 15-29 | 34.1 | -8.1 | -30.4 |  |
| rlm_quiet | close | pin $2k+ | 13-17 | 43.3 | -0.4 | 28.5 |  |
| rlm_quiet | close | pin limit <$1k | 5-8 | 38.5 | -3.6 | -25.5 |  |
| pin_move | close | 1-3k bets | 62-67 | 48.1 | -1.4 | -5.9 |  |
| pin_move | close | 3k+ bets | 8-11 | 42.1 | -6.5 | -17.0 |  |
| pin_move | close | <1k bets | 10-11 | 47.6 | -3.9 | -10.9 |  |
| pin_move | close | pin $1-2k | 38-40 | 48.7 | -0.4 | -4.3 |  |
| pin_move | close | pin $2k+ | 28-31 | 47.5 | -3.1 | -7.7 |  |
| pin_move | close | pin limit <$1k | 14-18 | 43.8 | -5.5 | -16.4 |  |
| money_delta | close | 1-3k bets | 32-39 | 45.1 | 3.2 | -11.6 |  |
| money_delta | close | 3k+ bets | 6-4 | 60.0 | 15.0 | 21.7 |  |
| money_delta | close | <1k bets | 10-10 | 50.0 | 8.4 | 17.9 |  |
| money_delta | close | pin $1-2k | 19-14 | 57.6 | 15.0 | 21.9 |  |
| money_delta | close | pin $2k+ | 8-12 | 40.0 | -0.5 | -18.7 |  |
| money_delta | close | pin limit <$1k | 8-11 | 42.1 | 0.4 | -18.7 |  |
| pin_rlm | close | 1-3k bets | 12-18 | 40.0 | -0.2 | -15.6 |  |
| pin_rlm | close | 3k+ bets | 2-2 | 50.0 | 11.3 | 7.3 |  |
| pin_rlm | close | <1k bets | 1-3 | 25.0 | -16.0 | -52.3 |  |
| pin_rlm | close | pin $1-2k | 8-7 | 53.3 | 12.4 | 3.4 |  |
| pin_rlm | close | pin $2k+ | 4-8 | 33.3 | -5.3 | -15.5 |  |
| pin_rlm | close | pin limit <$1k | 3-8 | 27.3 | -13.3 | -46.7 |  |
| follow_move | close | 1-3k bets | 96-119 | 44.7 | -4.8 | -10.3 |  |
| follow_move | close | 3k+ bets | 12-14 | 46.2 | -4.4 | -14.9 |  |
| follow_move | close | <1k bets | 23-31 | 42.6 | -5.7 | -25.0 |  |
| follow_move | close | pin $1-2k | 48-55 | 46.6 | -2.2 | -11.4 |  |
| follow_move | close | pin $2k+ | 36-39 | 48.0 | -2.4 | 5.7 |  |
| follow_move | close | pin limit <$1k | 14-23 | 37.8 | -10.8 | -27.5 |  |
| rlm_ratio | close | 1-3k bets | 20-38 | 34.5 | -6.5 | -29.6 |  |
| rlm_ratio | close | 3k+ bets | 3-3 | 50.0 | 8.3 | 3.3 |  |
| rlm_ratio | close | <1k bets | 3-7 | 30.0 | -9.6 | -42.9 |  |
| rlm_ratio | close | pin $1-2k | 12-9 | 57.1 | 17.3 | 12.2 |  |
| rlm_ratio | close | pin $2k+ | 4-10 | 28.6 | -9.7 | -30.9 |  |
| rlm_ratio | close | pin limit <$1k | 5-10 | 33.3 | -8.5 | -35.7 |  |
| money_level | close | 1-3k bets | 119-94 | 55.9 | -0.9 | -4.3 |  |
| money_level | close | 3k+ bets | 19-15 | 55.9 | 1.1 | -3.5 |  |
| money_level | close | <1k bets | 38-11 | 77.6 | 21.0 | 32.8 |  |
| money_level | close | pin $1-2k | 57-37 | 60.6 | 4.7 | 7.2 |  |
| money_level | close | pin $2k+ | 38-39 | 49.4 | -6.3 | -19.4 |  |
| money_level | close | pin limit <$1k | 22-18 | 55.0 | -0.1 | 4.4 |  |
| sharp_gap | close | 1-3k bets | 88-106 | 45.4 | -2.5 | -12.5 |  |
| sharp_gap | close | 3k+ bets | 17-16 | 51.5 | 1.4 | -1.1 |  |
| sharp_gap | close | <1k bets | 25-20 | 55.6 | 8.4 | 8.4 |  |
| sharp_gap | close | pin $1-2k | 47-37 | 56.0 | 6.8 | 7.8 |  |
| sharp_gap | close | pin $2k+ | 33-39 | 45.8 | -0.9 | -6.4 |  |
| sharp_gap | close | pin limit <$1k | 13-23 | 36.1 | -10.8 | -30.9 |  |
| money_moving | close | 1-3k bets | 91-107 | 46.0 | -2.4 | -12.4 |  |
| money_moving | close | 3k+ bets | 17-16 | 51.5 | 1.4 | -1.1 |  |
| money_moving | close | <1k bets | 26-19 | 57.8 | 9.9 | 10.5 |  |
| money_moving | close | pin $1-2k | 47-37 | 56.0 | 6.3 | 6.9 |  |
| money_moving | close | pin $2k+ | 33-39 | 45.8 | -0.9 | -6.4 |  |
| money_moving | close | pin limit <$1k | 15-25 | 37.5 | -10.1 | -28.4 |  |
| pin_value | close | 1-3k bets | 56-37 | 60.2 | 9.0 | 26.0 |  |
| pin_value | close | 3k+ bets | 5-6 | 45.5 | -8.6 | -12.2 |  |
| pin_value | close | <1k bets | 11-7 | 61.1 | 12.4 | 35.7 |  |
| pin_value | close | pin $1-2k | 33-27 | 55.0 | 4.9 | 13.3 |  |
| pin_value | close | pin $2k+ | 19-14 | 57.6 | 7.8 | 37.5 |  |
| pin_value | close | pin limit <$1k | 20-9 | 69.0 | 14.3 | 30.8 |  |
| consensus_gap | close | 1-3k bets | 48-32 | 60.0 | 6.5 | 11.3 |  |
| consensus_gap | close | 3k+ bets | 6-3 | 66.7 | 13.7 | 13.8 |  |
| consensus_gap | close | <1k bets | 15-3 | 83.3 | 30.0 | 56.5 |  |
| consensus_gap | close | pin $1-2k | 17-13 | 56.7 | 1.7 | 18.2 |  |
| consensus_gap | close | pin $2k+ | 30-11 | 73.2 | 18.3 | 31.5 |  |
| consensus_gap | close | pin limit <$1k | 7-2 | 77.8 | 27.3 | 48.3 |  |
| follow_move+pin_move | close | 1-3k bets | 40-59 | 40.4 | -8.5 | -20.8 |  |
| money_delta+money_moving | close | 1-3k bets | 24-27 | 47.1 | 5.6 | -7.0 |  |
| money_delta+sharp_gap | close | 1-3k bets | 24-26 | 48.0 | 6.5 | -5.1 |  |
| money_moving+sharp_gap | close | 1-3k bets | 86-103 | 45.5 | -2.5 | -12.2 |  |
| consensus_gap+money_level | close | 1-3k bets | 32-19 | 62.7 | 3.6 | 3.7 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 35-57 | 38.0 | -3.7 | -9.6 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 17-27 | 38.6 | -4.2 | -18.2 |  |
| consensus_gap+follow_move | close | 1-3k bets | 14-13 | 51.9 | -0.5 | -2.1 |  |
| follow_move+money_level | close | 1-3k bets | 44-43 | 50.6 | -6.2 | -11.0 |  |
| money_level+money_moving | close | 1-3k bets | 61-56 | 52.1 | -1.8 | -6.8 |  |
| money_level+sharp_gap | close | 1-3k bets | 58-55 | 51.3 | -2.1 | -6.7 |  |
| consensus_gap+money_moving | close | 1-3k bets | 15-19 | 44.1 | -6.5 | -9.1 |  |
| consensus_gap+pin_move | close | 1-3k bets | 12-6 | 66.7 | 15.7 | 39.2 |  |
| consensus_gap+pin_value | close | 1-3k bets | 17-12 | 58.6 | 7.5 | 9.9 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 14-18 | 43.8 | -6.2 | -6.9 |  |
| follow_move+money_moving | close | 1-3k bets | 43-62 | 41.0 | -7.1 | -21.9 |  |
| follow_move+pin_value | close | 1-3k bets | 17-12 | 58.6 | 6.6 | 44.1 |  |
| follow_move+sharp_gap | close | 1-3k bets | 45-63 | 41.7 | -6.1 | -20.5 |  |
| money_level+pin_move | close | 1-3k bets | 25-25 | 50.0 | -5.5 | -10.0 |  |
| money_level+pin_value | close | 1-3k bets | 20-14 | 58.8 | 4.1 | 10.4 |  |
| money_moving+pin_move | close | 1-3k bets | 27-28 | 49.1 | 1.2 | -3.3 |  |
| money_moving+pin_value | close | 1-3k bets | 17-16 | 51.5 | -0.4 | -3.1 |  |
| pin_move+pin_value | close | 1-3k bets | 20-14 | 58.8 | 6.2 | 10.5 |  |
| pin_move+sharp_gap | close | 1-3k bets | 25-29 | 46.3 | -0.9 | -8.5 |  |
| pin_value+sharp_gap | close | 1-3k bets | 16-14 | 53.3 | 2.1 | 0.2 |  |
| follow_move+money_delta | close | 1-3k bets | 20-28 | 41.7 | -1.3 | -18.8 |  |
| money_delta+pin_move | close | 1-3k bets | 12-13 | 48.0 | 6.9 | -6.3 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 12-22 | 35.3 | -5.1 | -30.3 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 20-38 | 34.5 | -6.5 | -29.6 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 14-29 | 32.6 | -6.4 | -31.1 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 20-36 | 35.7 | -5.5 | -27.1 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 10-28 | 26.3 | -12.5 | -43.8 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 14-31 | 31.1 | -7.7 | -34.2 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 20-38 | 34.5 | -6.5 | -29.6 |  |
| money_delta+money_level | close | 1-3k bets | 8-5 | 61.5 | 12.9 | 17.9 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 4-7 | 36.4 | -2.9 | -16.2 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 4-4 | 50.0 | 10.2 | 14.4 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 14-20 | 41.2 | -0.2 | -19.1 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 2-2 | 50.0 | 5.7 | 35.0 |  |
| money_level+pin_rlm | close | 1-3k bets | 4-3 | 57.1 | 13.6 | 11.3 |  |
| money_moving+pin_rlm | close | 1-3k bets | 12-17 | 41.4 | 1.1 | -12.7 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 12-18 | 40.0 | -0.2 | -15.6 |  |
| money_level+rlm_ratio | close | 1-3k bets | 8-8 | 50.0 | 4.2 | -3.6 |  |
| consensus_gap+money_delta | close | 1-3k bets | 4-2 | 66.7 | 25.0 | 27.8 |  |
| follow_move+pin_rlm | close | 1-3k bets | 10-15 | 40.0 | 1.2 | -15.7 |  |
| money_delta+pin_rlm | close | 1-3k bets | 7-10 | 41.2 | 2.6 | -18.4 |  |
| pin_move+pin_rlm | close | 1-3k bets | 12-13 | 48.0 | 8.1 | 1.2 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 11-12 | 47.8 | 7.9 | -0.3 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 6-12 | 33.3 | -5.1 | -26.2 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 10-15 | 40.0 | 1.2 | -15.7 |  |
| money_delta+pin_value | close | 1-3k bets | 8-3 | 72.7 | 28.5 | 37.9 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 5-5 | 50.0 | 5.9 | 92.8 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 3-0 | 100.0 | 47.0 | 87.5 |  |
| pin_rlm+pin_value | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 |  |
| money_level+money_moving | close | 3k+ bets | 12-10 | 54.5 | 1.0 | 0.0 |  |
| money_level+sharp_gap | close | 3k+ bets | 12-10 | 54.5 | 1.0 | 0.0 |  |
| money_moving+sharp_gap | close | 3k+ bets | 17-16 | 51.5 | 1.4 | -1.1 |  |
| follow_move+money_delta | close | 3k+ bets | 3-3 | 50.0 | 3.8 | -3.8 |  |
| follow_move+money_level | close | 3k+ bets | 7-4 | 63.6 | 5.0 | 5.4 |  |
| follow_move+money_moving | close | 3k+ bets | 8-6 | 57.1 | 6.8 | 5.7 |  |
| follow_move+pin_move | close | 3k+ bets | 6-9 | 40.0 | -8.5 | -21.8 |  |
| follow_move+pin_rlm | close | 3k+ bets | 2-2 | 50.0 | 11.3 | 7.3 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 3-3 | 50.0 | 8.3 | 3.3 |  |
| follow_move+sharp_gap | close | 3k+ bets | 8-6 | 57.1 | 6.8 | 5.7 |  |
| money_delta+money_level | close | 3k+ bets | 2-0 | 100.0 | 50.0 | 93.0 |  |
| money_delta+money_moving | close | 3k+ bets | 5-2 | 71.4 | 27.3 | 45.6 |  |
| money_delta+pin_move | close | 3k+ bets | 2-3 | 40.0 | -3.7 | -22.8 |  |
| money_delta+pin_rlm | close | 3k+ bets | 1-2 | 33.3 | -6.1 | -34.9 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 2-2 | 50.0 | 5.7 | -3.5 |  |
| money_delta+sharp_gap | close | 3k+ bets | 5-2 | 71.4 | 27.3 | 45.6 |  |
| money_level+pin_move | close | 3k+ bets | 3-3 | 50.0 | -5.3 | -9.2 |  |
| money_level+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 59.0 | 95.2 |  |
| money_level+rlm_ratio | close | 3k+ bets | 2-0 | 100.0 | 50.0 | 93.0 |  |
| money_moving+pin_move | close | 3k+ bets | 4-4 | 50.0 | 2.3 | -8.1 |  |
| money_moving+pin_rlm | close | 3k+ bets | 2-2 | 50.0 | 11.3 | 7.3 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 3-3 | 50.0 | 8.3 | 3.3 |  |
| pin_move+pin_rlm | close | 3k+ bets | 1-2 | 33.3 | -6.1 | -34.9 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 1-2 | 33.3 | -6.1 | -34.9 |  |
| pin_move+sharp_gap | close | 3k+ bets | 4-4 | 50.0 | 2.3 | -8.1 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 2-2 | 50.0 | 11.3 | 7.3 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 2-2 | 50.0 | 11.3 | 7.3 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 3-3 | 50.0 | 8.3 | 3.3 |  |
| consensus_gap+money_level | close | 3k+ bets | 4-1 | 80.0 | 18.2 | 25.1 |  |
| consensus_gap+money_moving | close | 3k+ bets | 3-2 | 60.0 | 3.7 | 1.4 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 3-2 | 60.0 | 3.7 | 1.4 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 3-8 | 27.3 | -15.7 | -42.9 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 3-6 | 33.3 | -10.6 | -30.2 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 1-3 | 25.0 | -19.3 | -52.3 |  |
| money_level+pin_value | close | 3k+ bets | 3-3 | 50.0 | -3.8 | -5.5 |  |
| money_moving+pin_value | close | 3k+ bets | 3-3 | 50.0 | -3.0 | -5.2 |  |
| pin_value+sharp_gap | close | 3k+ bets | 3-3 | 50.0 | -3.0 | -5.2 |  |
| consensus_gap+follow_move | close | 3k+ bets | 3-0 | 100.0 | 39.4 | 69.0 |  |
| consensus_gap+pin_value | close | 3k+ bets | 4-0 | 100.0 | 46.6 | 93.8 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 1-4 | 20.0 | -22.7 | -61.8 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 1-4 | 20.0 | -22.7 | -61.8 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 0-2 | 0.0 | -38.7 | -100.0 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 0-3 | 0.0 | -37.9 | -100.0 |  |
| pin_move+pin_value | close | 3k+ bets | 3-4 | 42.9 | -11.0 | -16.3 |  |
| follow_move+pin_value | close | 3k+ bets | 2-2 | 50.0 | -10.2 | -5.5 |  |
| consensus_gap+money_delta | close | 3k+ bets | 1-0 | 100.0 | 41.0 | 90.9 |  |
| consensus_gap+pin_move | close | 3k+ bets | 3-0 | 100.0 | 48.5 | 95.3 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 1-0 | 100.0 | 41.0 | 90.9 |  |
| money_delta+pin_value | close | 3k+ bets | 1-0 | 100.0 | 41.0 | 90.9 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 1-1 | 50.0 | -9.0 | -4.5 |  |
| consensus_gap+money_level | close | <1k bets | 11-1 | 91.7 | 34.5 | 42.3 |  |
| consensus_gap+money_moving | close | <1k bets | 8-0 | 100.0 | 46.0 | 103.6 |  |
| consensus_gap+pin_value | close | <1k bets | 4-1 | 80.0 | 36.3 | 123.1 |  |
| consensus_gap+sharp_gap | close | <1k bets | 9-1 | 90.0 | 36.8 | 77.0 |  |
| follow_move+pin_move | close | <1k bets | 6-10 | 37.5 | -12.8 | -30.3 |  |
| follow_move+rlm_quiet | close | <1k bets | 4-17 | 19.0 | -22.5 | -63.3 |  |
| money_level+money_moving | close | <1k bets | 20-5 | 80.0 | 25.6 | 38.3 |  |
| money_level+pin_value | close | <1k bets | 5-1 | 83.3 | 33.3 | 56.7 |  |
| money_level+sharp_gap | close | <1k bets | 19-5 | 79.2 | 25.2 | 40.2 |  |
| money_moving+pin_value | close | <1k bets | 4-1 | 80.0 | 39.9 | 124.8 |  |
| money_moving+sharp_gap | close | <1k bets | 24-18 | 57.1 | 9.8 | 12.8 |  |
| pin_move+rlm_quiet | close | <1k bets | 2-4 | 33.3 | -12.9 | -36.4 |  |
| pin_value+sharp_gap | close | <1k bets | 4-1 | 80.0 | 39.9 | 124.8 |  |
| follow_move+money_moving | close | <1k bets | 10-10 | 50.0 | 2.5 | -17.8 |  |
| follow_move+sharp_gap | close | <1k bets | 9-10 | 47.4 | 0.7 | -18.3 |  |
| money_level+pin_move | close | <1k bets | 6-3 | 66.7 | 10.6 | 22.8 |  |
| money_moving+rlm_quiet | close | <1k bets | 2-6 | 25.0 | -14.3 | -52.3 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 2-6 | 25.0 | -14.3 | -52.3 |  |
| follow_move+money_delta | close | <1k bets | 5-7 | 41.7 | -1.6 | -20.5 |  |
| follow_move+pin_rlm | close | <1k bets | 1-3 | 25.0 | -16.0 | -52.3 |  |
| follow_move+pin_value | close | <1k bets | 3-2 | 60.0 | 11.8 | 15.4 |  |
| follow_move+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -9.6 | -42.9 |  |
| money_delta+money_moving | close | <1k bets | 7-8 | 46.7 | 7.2 | 18.9 |  |
| money_delta+pin_move | close | <1k bets | 1-2 | 33.3 | -7.7 | -36.4 |  |
| money_delta+pin_rlm | close | <1k bets | 1-2 | 33.3 | -7.7 | -36.4 |  |
| money_delta+pin_value | close | <1k bets | 3-0 | 100.0 | 60.6 | 212.0 |  |
| money_delta+rlm_quiet | close | <1k bets | 3-4 | 42.9 | 1.3 | -17.2 |  |
| money_delta+rlm_ratio | close | <1k bets | 3-5 | 37.5 | -2.3 | -28.6 |  |
| money_delta+sharp_gap | close | <1k bets | 7-8 | 46.7 | 7.2 | 18.9 |  |
| money_moving+pin_move | close | <1k bets | 3-3 | 50.0 | 6.0 | -5.2 |  |
| money_moving+pin_rlm | close | <1k bets | 1-3 | 25.0 | -16.0 | -52.3 |  |
| money_moving+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -9.6 | -42.9 |  |
| pin_move+pin_rlm | close | <1k bets | 1-3 | 25.0 | -16.0 | -52.3 |  |
| pin_move+pin_value | close | <1k bets | 4-1 | 80.0 | 28.2 | 52.8 |  |
| pin_move+rlm_ratio | close | <1k bets | 1-3 | 25.0 | -16.0 | -52.3 |  |
| pin_move+sharp_gap | close | <1k bets | 3-3 | 50.0 | 6.0 | -5.2 |  |
| pin_rlm+pin_value | close | <1k bets | 1-0 | 100.0 | 59.0 | 90.9 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 1-1 | 50.0 | 9.0 | -4.5 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 1-3 | 25.0 | -16.0 | -52.3 |  |
| pin_rlm+sharp_gap | close | <1k bets | 1-3 | 25.0 | -16.0 | -52.3 |  |
| pin_value+rlm_quiet | close | <1k bets | 2-0 | 100.0 | 59.0 | 90.9 |  |
| pin_value+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 59.0 | 90.9 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 2-5 | 28.6 | -10.4 | -45.5 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 3-7 | 30.0 | -9.6 | -42.9 |  |
| consensus_gap+follow_move | close | <1k bets | 5-0 | 100.0 | 45.4 | 71.3 |  |
| consensus_gap+pin_move | close | <1k bets | 2-0 | 100.0 | 47.7 | 70.5 |  |
| follow_move+money_level | close | <1k bets | 12-4 | 75.0 | 17.3 | 21.7 |  |
| money_delta+money_level | close | <1k bets | 2-1 | 66.7 | 27.2 | 53.8 |  |
| money_level+pin_rlm | close | <1k bets | 0-1 | 0.0 | -41.0 | -100.0 |  |
| money_level+rlm_ratio | close | <1k bets | 1-1 | 50.0 | 9.0 | -5.3 |  |
| consensus_gap+money_delta | close | <1k bets | 3-0 | 100.0 | 53.0 | 208.0 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 59.0 | 89.3 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-0 | 100.0 | 59.0 | 90.9 |  |
| money_delta+money_moving | close | pin $1-2k | 11-5 | 68.8 | 28.1 | 55.5 |  |
| money_delta+sharp_gap | close | pin $1-2k | 11-5 | 68.8 | 28.1 | 55.5 |  |
| money_moving+sharp_gap | close | pin $1-2k | 45-35 | 56.2 | 6.9 | 9.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 7-6 | 53.8 | -1.4 | -4.0 |  |
| consensus_gap+money_level | close | pin $1-2k | 11-7 | 61.1 | 1.3 | 3.2 |  |
| consensus_gap+money_moving | close | pin $1-2k | 6-6 | 50.0 | -3.0 | 12.7 |  |
| consensus_gap+pin_move | close | pin $1-2k | 5-4 | 55.6 | 3.6 | 26.2 |  |
| consensus_gap+pin_value | close | pin $1-2k | 7-6 | 53.8 | 0.7 | 29.3 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 6-5 | 54.5 | 0.0 | 25.4 |  |
| follow_move+money_level | close | pin $1-2k | 24-16 | 60.0 | 5.1 | 8.1 |  |
| follow_move+money_moving | close | pin $1-2k | 24-20 | 54.5 | 6.6 | 2.1 |  |
| follow_move+pin_move | close | pin $1-2k | 23-37 | 38.3 | -9.8 | -25.0 |  |
| follow_move+pin_value | close | pin $1-2k | 10-10 | 50.0 | -0.9 | -5.3 |  |
| follow_move+sharp_gap | close | pin $1-2k | 26-21 | 55.3 | 7.4 | 2.7 |  |
| money_level+money_moving | close | pin $1-2k | 35-20 | 63.6 | 9.6 | 14.2 |  |
| money_level+pin_move | close | pin $1-2k | 15-12 | 55.6 | 0.9 | 2.6 |  |
| money_level+pin_value | close | pin $1-2k | 12-8 | 60.0 | 6.4 | 11.9 |  |
| money_level+sharp_gap | close | pin $1-2k | 35-20 | 63.6 | 10.0 | 15.6 |  |
| money_moving+pin_move | close | pin $1-2k | 18-13 | 58.1 | 10.2 | 9.8 |  |
| money_moving+pin_value | close | pin $1-2k | 12-9 | 57.1 | 6.1 | 24.5 |  |
| pin_move+pin_value | close | pin $1-2k | 13-8 | 61.9 | 8.9 | 16.7 |  |
| pin_move+sharp_gap | close | pin $1-2k | 18-14 | 56.2 | 8.8 | 6.4 |  |
| pin_value+sharp_gap | close | pin $1-2k | 12-8 | 60.0 | 9.3 | 30.8 |  |
| follow_move+money_delta | close | pin $1-2k | 13-12 | 52.0 | 8.5 | 0.8 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 15-29 | 34.1 | -8.1 | -30.4 |  |
| money_delta+pin_move | close | pin $1-2k | 9-7 | 56.2 | 15.6 | 9.4 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 8-12 | 40.0 | -2.3 | -22.4 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 11-19 | 36.7 | -6.0 | -26.7 |  |
| follow_move+pin_rlm | close | pin $1-2k | 7-7 | 50.0 | 10.3 | -2.8 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 12-9 | 57.1 | 17.3 | 12.2 |  |
| pin_move+pin_rlm | close | pin $1-2k | 8-5 | 61.5 | 19.9 | 19.3 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 7-5 | 58.3 | 18.1 | 13.4 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 4-7 | 36.4 | -3.4 | -29.8 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 7-7 | 50.0 | 10.3 | -2.8 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 8-7 | 53.3 | 12.4 | 3.4 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 5-8 | 38.5 | -0.7 | -25.2 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 7-10 | 41.2 | 1.8 | -20.1 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 12-9 | 57.1 | 17.3 | 12.2 |  |
| money_delta+money_level | close | pin $1-2k | 4-0 | 100.0 | 55.7 | 95.8 |  |
| money_delta+pin_rlm | close | pin $1-2k | 6-3 | 66.7 | 26.7 | 29.9 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 8-4 | 66.7 | 25.3 | 29.6 |  |
| money_level+pin_rlm | close | pin $1-2k | 3-0 | 100.0 | 60.6 | 96.0 |  |
| money_level+rlm_ratio | close | pin $1-2k | 6-1 | 85.7 | 44.1 | 66.7 |  |
| money_moving+pin_rlm | close | pin $1-2k | 8-6 | 57.1 | 15.9 | 10.8 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 12-8 | 60.0 | 20.0 | 17.8 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 7-9 | 43.8 | 4.2 | -15.1 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 1-3 | 25.0 | -17.0 | -52.3 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 4-5 | 44.4 | -0.5 | -14.7 |  |
| money_delta+pin_value | close | pin $1-2k | 6-3 | 66.7 | 26.2 | 67.2 |  |
| consensus_gap+money_delta | close | pin $1-2k | 2-1 | 66.7 | 21.2 | 144.9 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 0-1 | 0.0 | -36.4 | -100.0 |  |
| pin_rlm+pin_value | close | pin $1-2k | 2-0 | 100.0 | 50.0 | 90.9 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 1-0 | 100.0 | 59.0 | 90.9 |  |
| follow_move+pin_move | close | pin $2k+ | 21-28 | 42.9 | -8.0 | -16.5 |  |
| consensus_gap+money_level | close | pin $2k+ | 20-10 | 66.7 | 8.2 | 3.3 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 13-17 | 43.3 | -0.4 | 28.5 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 8-14 | 36.4 | -8.0 | -16.8 |  |
| money_level+money_moving | close | pin $2k+ | 19-24 | 44.2 | -7.1 | -20.6 |  |
| money_level+sharp_gap | close | pin $2k+ | 19-24 | 44.2 | -7.1 | -20.6 |  |
| money_moving+sharp_gap | close | pin $2k+ | 33-39 | 45.8 | -0.9 | -6.4 |  |
| consensus_gap+pin_value | close | pin $2k+ | 12-5 | 70.6 | 23.2 | 33.1 |  |
| follow_move+money_level | close | pin $2k+ | 12-13 | 48.0 | -11.8 | -21.5 |  |
| follow_move+money_moving | close | pin $2k+ | 14-18 | 43.8 | -5.0 | -13.8 |  |
| follow_move+sharp_gap | close | pin $2k+ | 14-18 | 43.8 | -5.0 | -13.8 |  |
| money_level+pin_move | close | pin $2k+ | 9-10 | 47.4 | -12.7 | -22.3 |  |
| money_moving+pin_move | close | pin $2k+ | 9-11 | 45.0 | -2.7 | -6.0 |  |
| pin_move+sharp_gap | close | pin $2k+ | 9-11 | 45.0 | -2.7 | -6.0 |  |
| money_delta+money_level | close | pin $2k+ | 2-1 | 66.7 | 19.7 | 25.2 |  |
| money_delta+money_moving | close | pin $2k+ | 7-12 | 36.8 | -2.6 | -24.5 |  |
| money_delta+sharp_gap | close | pin $2k+ | 7-12 | 36.8 | -2.6 | -24.5 |  |
| consensus_gap+money_moving | close | pin $2k+ | 10-8 | 55.6 | 3.3 | 19.3 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 10-8 | 55.6 | 3.3 | 19.3 |  |
| money_level+pin_value | close | pin $2k+ | 5-6 | 45.5 | -4.1 | -14.5 |  |
| money_moving+pin_value | close | pin $2k+ | 5-6 | 45.5 | -3.7 | -14.1 |  |
| pin_value+sharp_gap | close | pin $2k+ | 5-6 | 45.5 | -3.7 | -14.1 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 1-1 | 50.0 | 0.0 | 70.0 |  |
| money_level+pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -63.6 | -100.0 |  |
| money_moving+pin_rlm | close | pin $2k+ | 4-8 | 33.3 | -5.3 | -15.5 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 4-8 | 33.3 | -5.3 | -15.5 |  |
| follow_move+money_delta | close | pin $2k+ | 4-8 | 33.3 | -9.1 | -35.5 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 4-10 | 28.6 | -9.7 | -30.9 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 2-8 | 20.0 | -19.1 | -60.7 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 4-10 | 28.6 | -9.7 | -30.9 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 4-10 | 28.6 | -9.7 | -30.9 |  |
| money_level+rlm_ratio | close | pin $2k+ | 1-1 | 50.0 | 2.3 | -7.7 |  |
| consensus_gap+follow_move | close | pin $2k+ | 9-1 | 90.0 | 30.0 | 64.9 |  |
| consensus_gap+pin_move | close | pin $2k+ | 10-1 | 90.9 | 37.2 | 73.3 |  |
| follow_move+pin_value | close | pin $2k+ | 5-3 | 62.5 | 10.2 | 138.7 |  |
| pin_move+pin_value | close | pin $2k+ | 7-6 | 53.8 | 3.2 | 1.9 |  |
| follow_move+pin_rlm | close | pin $2k+ | 3-6 | 33.3 | -3.0 | -13.1 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 3-6 | 33.3 | -3.0 | -13.1 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 2-1 | 66.7 | 15.2 | 350.3 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 4-8 | 33.3 | -5.3 | -19.1 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 4-8 | 33.3 | -5.3 | -19.1 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 3-6 | 33.3 | -8.1 | -34.5 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 2-7 | 22.2 | -14.1 | -39.1 |  |
| money_delta+pin_move | close | pin $2k+ | 4-5 | 44.4 | 0.5 | -13.9 |  |
| money_delta+pin_rlm | close | pin $2k+ | 1-6 | 14.3 | -22.1 | -70.3 |  |
| pin_move+pin_rlm | close | pin $2k+ | 3-5 | 37.5 | 1.1 | -2.5 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 3-5 | 37.5 | -1.7 | -8.4 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 2-5 | 28.6 | -7.8 | -21.7 |  |
| consensus_gap+money_delta | close | pin $2k+ | 2-0 | 100.0 | 41.0 | 87.8 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 2-0 | 100.0 | 52.3 | 165.5 |  |
| money_delta+pin_value | close | pin $2k+ | 2-0 | 100.0 | 41.0 | 87.8 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 2-0 | 100.0 | 52.3 | 162.3 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 1-0 | 100.0 | 41.0 | 84.7 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 4-1 | 80.0 | 32.7 | 53.8 |  |
| consensus_gap+money_level | close | pin limit <$1k | 4-1 | 80.0 | 21.0 | 50.5 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 3-2 | 60.0 | 12.7 | 15.6 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 6-2 | 75.0 | 22.7 | 41.8 |  |
| follow_move+money_level | close | pin limit <$1k | 8-12 | 40.0 | -12.7 | -23.6 |  |
| follow_move+money_moving | close | pin limit <$1k | 7-17 | 29.2 | -17.6 | -44.1 |  |
| follow_move+pin_value | close | pin limit <$1k | 7-3 | 70.0 | 14.6 | 32.9 |  |
| money_level+money_moving | close | pin limit <$1k | 9-13 | 40.9 | -11.5 | -22.4 |  |
| money_level+pin_value | close | pin limit <$1k | 11-4 | 73.3 | 15.5 | 38.8 |  |
| money_moving+pin_value | close | pin limit <$1k | 7-5 | 58.3 | 6.8 | 10.7 |  |
| follow_move+pin_move | close | pin limit <$1k | 8-13 | 38.1 | -9.5 | -26.6 |  |
| money_level+pin_move | close | pin limit <$1k | 10-9 | 52.6 | 0.3 | 0.1 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 13-23 | 36.1 | -10.8 | -30.9 |  |
| pin_move+pin_value | close | pin limit <$1k | 7-5 | 58.3 | 3.8 | 11.1 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 5-8 | 38.5 | -3.6 | -25.5 |  |
| money_moving+pin_move | close | pin limit <$1k | 7-11 | 38.9 | -7.8 | -25.7 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 2-0 | 100.0 | 61.3 | 95.5 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 2-1 | 66.7 | 27.2 | 30.3 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 1-1 | 50.0 | 11.3 | 0.0 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 3-0 | 100.0 | 60.6 | 93.9 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 2-0 | 100.0 | 61.3 | 95.5 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 3-1 | 75.0 | 30.7 | 44.5 |  |
| follow_move+money_delta | close | pin limit <$1k | 4-8 | 33.3 | -8.8 | -35.6 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 3-7 | 30.0 | -10.5 | -41.4 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 5-10 | 33.3 | -8.5 | -35.7 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 7-16 | 30.4 | -15.8 | -41.7 |  |
| money_delta+money_moving | close | pin limit <$1k | 7-9 | 43.8 | 1.9 | -15.4 |  |
| money_delta+pin_move | close | pin limit <$1k | 2-6 | 25.0 | -15.4 | -50.6 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 2-5 | 28.6 | -11.8 | -43.5 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 2-2 | 50.0 | 10.2 | -2.3 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 4-7 | 36.4 | -5.8 | -29.7 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 7-9 | 43.8 | 1.9 | -15.4 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 3-8 | 27.3 | -13.3 | -46.7 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 2-5 | 28.6 | -11.8 | -44.2 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 5-10 | 33.3 | -8.5 | -35.7 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 3-8 | 27.3 | -13.3 | -46.7 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 3-4 | 42.9 | -0.0 | -16.9 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 3-7 | 30.0 | -10.5 | -41.4 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 5-11 | 31.2 | -14.0 | -40.0 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 1-3 | 25.0 | -14.8 | -50.0 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 3-7 | 30.0 | -10.5 | -41.4 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 3-8 | 27.3 | -13.3 | -46.7 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 2-5 | 28.6 | -11.8 | -44.2 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 2-5 | 28.6 | -11.8 | -44.2 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 5-10 | 33.3 | -8.5 | -35.7 |  |
| money_delta+pin_value | close | pin limit <$1k | 4-0 | 100.0 | 54.5 | 91.0 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 2-0 | 100.0 | 59.0 | 90.9 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 6-4 | 60.0 | 10.0 | 13.8 |  |
| money_level+sharp_gap | close | pin limit <$1k | 7-12 | 36.8 | -14.6 | -30.1 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 0-1 | 0.0 | -41.0 | -100.0 |  |
| money_delta+money_level | close | pin limit <$1k | 1-4 | 20.0 | -21.0 | -61.0 |  |
| money_level+pin_rlm | close | pin limit <$1k | 2-3 | 40.0 | -1.0 | -22.8 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 2-4 | 33.3 | -7.7 | -35.7 |  |
| rlm_quiet | early | <1k bets | 8-12 | 40.0 | 1.6 | -11.0 | 0.33 |
| rlm_quiet | early | pin $1-2k | 1-0 | 100.0 | 63.6 | 132.0 | -1.8 |
| rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -41.0 | -100.0 | 0.0 |
| pin_move | early | <1k bets | 4-4 | 50.0 | 0.0 | -4.6 | -0.25 |
| pin_move | early | pin $1-2k | 0-2 | 0.0 | -41.0 | -100.0 | 0.0 |
| pin_move | early | pin limit <$1k | 4-2 | 66.7 | 13.7 | 27.3 | -0.33 |
| money_delta | early | <1k bets | 1-1 | 50.0 | 9.0 | -4.5 | 1.5 |
| money_delta | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| pin_rlm | early | <1k bets | 0-1 | 0.0 | -63.6 | -100.0 | 1.5 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -63.6 | -100.0 | 1.5 |
| follow_move | early | <1k bets | 74-89 | 45.4 | -2.7 | -11.4 | 0.05 |
| follow_move | early | pin $1-2k | 9-7 | 56.2 | 9.9 | 14.4 | -0.32 |
| follow_move | early | pin limit <$1k | 6-8 | 42.9 | -0.7 | -11.2 | -0.45 |
| rlm_ratio | early | <1k bets | 5-7 | 41.7 | -1.2 | -13.4 | 0.82 |
| rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -63.6 | -100.0 | 1.5 |
| rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| money_level | early | <1k bets | 21-20 | 51.2 | -8.1 | -17.4 | 0.01 |
| money_level | early | pin $1-2k | 0-2 | 0.0 | -63.6 | -100.0 | 1.6 |
| money_level | early | pin limit <$1k | 2-1 | 66.7 | 13.7 | 27.3 | 0.67 |
| sharp_gap | early | <1k bets | 15-19 | 44.1 | -3.1 | -12.9 | 0.33 |
| sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -63.6 | -100.0 | 1.6 |
| sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 25.7 | 27.3 | 0.0 |
| money_moving | early | <1k bets | 18-16 | 52.9 | 3.3 | -0.3 | 0.61 |
| money_moving | early | pin $1-2k | 0-1 | 0.0 | -63.6 | -100.0 | 1.7 |
| money_moving | early | pin limit <$1k | 2-1 | 66.7 | 25.7 | 27.3 | 0.0 |
| pin_value | early | <1k bets | 10-9 | 52.6 | 3.8 | -0.7 | -0.28 |
| pin_value | early | pin $1-2k | 2-7 | 22.2 | -23.3 | -58.4 | 0.08 |
| pin_value | early | pin limit <$1k | 8-2 | 80.0 | 28.2 | 51.2 | -0.6 |
| consensus_gap | early | <1k bets | 48-33 | 59.3 | 8.9 | 9.0 | 0.45 |
| consensus_gap | early | pin $1-2k | 4-3 | 57.1 | 9.1 | 2.9 | -0.46 |
| consensus_gap | early | pin limit <$1k | 4-1 | 80.0 | 28.2 | 51.9 | 0.6 |
| follow_move+money_level | early | <1k bets | 5-8 | 38.5 | -19.9 | -42.2 | 0.39 |
| follow_move+sharp_gap | early | <1k bets | 6-10 | 37.5 | -8.3 | -23.1 | 0.68 |
| money_level+sharp_gap | early | <1k bets | 7-10 | 41.2 | -14.7 | -26.9 | 0.31 |
| follow_move+money_moving | early | <1k bets | 9-9 | 50.0 | 2.0 | -6.8 | 0.79 |
| money_level+money_moving | early | <1k bets | 9-9 | 50.0 | -7.8 | -18.2 | 0.48 |
| consensus_gap+money_level | early | <1k bets | 8-5 | 61.5 | 4.6 | -7.8 | -0.32 |
| follow_move+rlm_quiet | early | <1k bets | 8-12 | 40.0 | 1.6 | -11.0 | 0.33 |
| follow_move+rlm_ratio | early | <1k bets | 5-7 | 41.7 | -1.2 | -13.4 | 0.82 |
| rlm_quiet+rlm_ratio | early | <1k bets | 4-4 | 50.0 | 11.3 | 6.1 | 0.04 |
| rlm_quiet+sharp_gap | early | <1k bets | 4-5 | 44.4 | 5.5 | -5.7 | 0.03 |
| rlm_ratio+sharp_gap | early | <1k bets | 5-7 | 41.7 | -1.2 | -13.4 | 0.82 |
| consensus_gap+follow_move | early | <1k bets | 5-5 | 50.0 | 0.9 | -13.3 | 0.96 |
| money_moving+rlm_quiet | early | <1k bets | 5-4 | 55.6 | 16.6 | 26.3 | 0.97 |
| money_moving+rlm_ratio | early | <1k bets | 5-3 | 62.5 | 20.4 | 29.9 | 1.57 |
| money_moving+sharp_gap | early | <1k bets | 11-10 | 52.4 | 3.9 | 6.1 | 0.72 |
| consensus_gap+money_moving | early | <1k bets | 4-2 | 66.7 | 15.9 | 2.8 | 0.35 |
| consensus_gap+sharp_gap | early | <1k bets | 4-3 | 57.1 | 9.1 | 2.4 | 0.04 |
| money_level+rlm_ratio | early | <1k bets | 1-3 | 25.0 | -26.2 | -52.3 | 2.38 |
| follow_move+pin_move | early | <1k bets | 1-3 | 25.0 | -20.5 | -52.3 | 0.5 |
| follow_move+money_delta | early | <1k bets | 1-1 | 50.0 | 9.0 | -4.5 | 1.5 |
| money_delta+money_level | early | <1k bets | 1-1 | 50.0 | 9.0 | -4.5 | 1.5 |
| money_delta+money_moving | early | <1k bets | 1-1 | 50.0 | 9.0 | -4.5 | 1.5 |
| money_delta+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 9.0 | -4.5 | 1.5 |
| money_delta+sharp_gap | early | <1k bets | 1-1 | 50.0 | 9.0 | -4.5 | 1.5 |
| follow_move+pin_value | early | <1k bets | 3-3 | 50.0 | 6.0 | -4.5 | -0.83 |
| consensus_gap+pin_move | early | <1k bets | 1-0 | 100.0 | 41.0 | 90.9 | 0.0 |
| consensus_gap+pin_value | early | <1k bets | 4-1 | 80.0 | 28.2 | 51.9 | 0.2 |
| money_level+pin_move | early | <1k bets | 1-0 | 100.0 | 41.0 | 90.9 | 0.0 |
| money_level+pin_value | early | <1k bets | 2-1 | 66.7 | 12.1 | 27.3 | 0.9 |
| pin_move+pin_value | early | <1k bets | 2-3 | 40.0 | -11.8 | -23.6 | -0.4 |
| money_moving+pin_value | early | <1k bets | 1-1 | 50.0 | -2.3 | -4.5 | 1.35 |
| pin_value+sharp_gap | early | <1k bets | 1-1 | 50.0 | -2.3 | -4.5 | 1.35 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| consensus_gap+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| follow_move+pin_rlm | early | <1k bets | 0-1 | 0.0 | -63.6 | -100.0 | 1.5 |
| money_level+pin_rlm | early | <1k bets | 0-1 | 0.0 | -63.6 | -100.0 | 1.5 |
| pin_rlm+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -63.6 | -100.0 | 1.5 |
| pin_rlm+sharp_gap | early | <1k bets | 0-1 | 0.0 | -63.6 | -100.0 | 1.5 |
| pin_move+pin_value | early | pin $1-2k | 0-2 | 0.0 | -41.0 | -100.0 | 0.0 |
| follow_move+rlm_quiet | early | pin $1-2k | 1-0 | 100.0 | 63.6 | 132.0 | -1.8 |
| money_level+money_moving | early | pin $1-2k | 0-1 | 0.0 | -63.6 | -100.0 | 1.7 |
| money_level+pin_value | early | pin $1-2k | 0-1 | 0.0 | -63.6 | -100.0 | 1.7 |
| money_level+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -63.6 | -100.0 | 1.6 |
| money_moving+pin_value | early | pin $1-2k | 0-1 | 0.0 | -63.6 | -100.0 | 1.7 |
| money_moving+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -63.6 | -100.0 | 1.7 |
| pin_value+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -63.6 | -100.0 | 1.7 |
| consensus_gap+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -6.5 | -0.5 |
| follow_move+money_level | early | pin $1-2k | 0-1 | 0.0 | -63.6 | -100.0 | 1.5 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -63.6 | -100.0 | 1.5 |
| follow_move+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -63.6 | -100.0 | 1.5 |
| follow_move+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -63.6 | -100.0 | 1.5 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -63.6 | -100.0 | 1.5 |
| money_level+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -63.6 | -100.0 | 1.5 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -63.6 | -100.0 | 1.5 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -63.6 | -100.0 | 1.5 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -63.6 | -100.0 | 1.5 |
| consensus_gap+follow_move | early | pin $1-2k | 1-0 | 100.0 | 63.6 | 106.0 | 1.5 |
| follow_move+pin_move | early | pin $1-2k | 0-1 | 0.0 | -41.0 | -100.0 | 0.0 |
| follow_move+pin_value | early | pin $1-2k | 0-1 | 0.0 | -41.0 | -100.0 | 0.0 |
| follow_move+pin_move | early | pin limit <$1k | 1-2 | 33.3 | -13.7 | -36.4 | 0.67 |
| follow_move+pin_value | early | pin limit <$1k | 3-2 | 60.0 | 15.4 | 14.5 | -1.0 |
| consensus_gap+money_level | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 90.9 | 0.5 |
| consensus_gap+pin_move | early | pin limit <$1k | 1-0 | 100.0 | 41.0 | 90.9 | 0.0 |
| consensus_gap+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 47.0 | 90.9 | 0.67 |
| follow_move+money_moving | early | pin limit <$1k | 1-1 | 50.0 | 9.0 | -4.5 | 0.5 |
| follow_move+rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -41.0 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 9.0 | -4.5 | 0.5 |
| money_level+pin_move | early | pin limit <$1k | 1-0 | 100.0 | 41.0 | 90.9 | 0.0 |
| money_level+pin_value | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 90.9 | 0.5 |
| money_moving+rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -41.0 | -100.0 | 0.0 |
| money_moving+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 25.7 | 27.3 | 0.0 |
| pin_move+pin_value | early | pin limit <$1k | 2-1 | 66.7 | 7.7 | 27.3 | -0.67 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -41.0 | -100.0 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| consensus_gap+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| follow_move+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| follow_move+money_level | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| follow_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| money_delta+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| money_delta+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| money_delta+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| money_level+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| money_level+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| money_level+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| money_moving+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| pin_value+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 59.0 | 90.9 | 1.0 |
