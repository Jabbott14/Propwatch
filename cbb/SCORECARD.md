# CBB scorecard

Generated 2026-11-26 13:14 UTC. 970 graded games (28 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**684 games before 2026-11-21 (fit) · 286 on or after it (forward).**

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
sample ran **46.7% favourites** (n=969) and **50.5% overs** (n=970) and **71.5% moneyline favourites** (n=848).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-21. Nothing in the engine was chosen using these. n=286 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 26-34 | 43.3 | 38.6 | 4.7 | +2.11 | 3.5 | 0.82 | 50.0 | no edge shown yet |
| pin_move | both | 9-16 | 36.0 | 49.9 | -13.9 | -8.09 | -32.4 | 0.49 | 40.0 | keep collecting (25/30) |
| money_delta | both | 4-5 | 44.4 | 37.7 | 6.8 | +1.47 | 16.3 | 3.02 | 100.0 | keep collecting (9/30) |
| pin_rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | keep collecting (2/30) |
| follow_move | both | 232-252 | 47.9 | 48.7 | -0.8 | -41.28 | -8.5 | 0.03 | 37.6 | DROP: below break-even |
| rlm_ratio | both | 10-16 | 38.5 | 41.2 | -2.8 | -1.99 | -7.6 | 0.4 | 53.8 | keep collecting (26/30) |
| money_level | both | 74-61 | 54.8 | 57.6 | -2.8 | -15.7 | -11.6 | -0.4 | 35.6 | no edge shown yet |
| sharp_gap | both | 57-63 | 47.5 | 50.3 | -2.8 | -11.56 | -9.6 | 0.22 | 45.8 | no edge shown yet |
| money_moving | both | 47-43 | 52.2 | 49.1 | 3.1 | -0.91 | -1.0 | 0.58 | 50.0 | no edge shown yet |
| pin_value | both | 23-20 | 53.5 | 49.5 | 4.0 | +0.49 | 1.1 | 0.11 | 34.9 | no edge shown yet |
| consensus_gap | both | 138-123 | 52.9 | 52.9 | -0.1 | -20.31 | -7.8 | 0.5 | 49.0 | no edge shown yet |
| follow_move+money_level | both | 26-18 | 59.1 | 57.2 | 1.9 | -4.93 | -11.2 | 0.11 | 36.4 | no edge shown yet |
| follow_move+sharp_gap | both | 24-26 | 48.0 | 48.0 | 0.0 | -2.98 | -6.0 | 0.62 | 46.0 | no edge shown yet |
| money_level+sharp_gap | both | 39-37 | 51.3 | 55.8 | -4.5 | -10.5 | -13.8 | -0.19 | 40.8 | no edge shown yet |
| follow_move+money_moving | both | 19-19 | 50.0 | 47.6 | 2.4 | +0.13 | 0.4 | 0.67 | 44.7 | no edge shown yet |
| money_level+money_moving | both | 23-17 | 57.5 | 55.3 | 2.2 | -0.1 | -0.3 | 0.42 | 47.5 | no edge shown yet |
| consensus_gap+money_level | both | 24-17 | 58.5 | 61.7 | -3.2 | -5.2 | -12.7 | -0.54 | 31.7 | no edge shown yet |
| follow_move+rlm_quiet | both | 26-34 | 43.3 | 38.6 | 4.7 | +2.11 | 3.5 | 0.82 | 50.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 10-16 | 38.5 | 41.2 | -2.8 | -1.99 | -7.6 | 0.4 | 53.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | both | 9-10 | 47.4 | 39.0 | 8.4 | +3.1 | 16.3 | 0.32 | 47.4 | keep collecting (19/30) |
| rlm_quiet+sharp_gap | both | 10-12 | 45.5 | 40.1 | 5.3 | +2.01 | 9.2 | 0.5 | 45.5 | keep collecting (22/30) |
| rlm_ratio+sharp_gap | both | 10-16 | 38.5 | 41.2 | -2.8 | -1.99 | -7.6 | 0.4 | 53.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 18-20 | 47.4 | 55.2 | -7.9 | -8.16 | -21.5 | 0.79 | 57.9 | no edge shown yet |
| money_moving+rlm_quiet | both | 9-10 | 47.4 | 39.0 | 8.4 | +2.99 | 15.7 | 0.91 | 47.4 | keep collecting (19/30) |
| money_moving+rlm_ratio | both | 7-6 | 53.8 | 40.2 | 13.6 | +4.05 | 31.1 | 1.58 | 69.2 | keep collecting (13/30) |
| money_moving+sharp_gap | both | 26-28 | 48.1 | 47.2 | 0.9 | -0.67 | -1.2 | 0.86 | 55.6 | no edge shown yet |
| consensus_gap+money_moving | both | 10-5 | 66.7 | 55.1 | 11.6 | +0.97 | 6.5 | 1.23 | 60.0 | keep collecting (15/30) |
| consensus_gap+sharp_gap | both | 15-15 | 50.0 | 57.1 | -7.1 | -6.39 | -21.3 | -0.38 | 36.7 | no edge shown yet |
| money_level+rlm_ratio | both | 1-6 | 14.3 | 47.3 | -33.0 | -5.09 | -72.7 | 0.64 | 71.4 | keep collecting (7/30) |
| follow_move+pin_move | both | 4-8 | 33.3 | 47.2 | -13.9 | -4.29 | -35.7 | 0.58 | 41.7 | keep collecting (12/30) |
| follow_move+money_delta | both | 3-2 | 60.0 | 38.6 | 21.4 | +3.56 | 71.2 | 2.74 | 100.0 | keep collecting (5/30) |
| money_delta+money_level | both | 1-3 | 25.0 | 40.1 | -15.1 | -2.09 | -52.3 | 1.68 | 100.0 | keep collecting (4/30) |
| money_delta+money_moving | both | 4-5 | 44.4 | 37.7 | 6.8 | +1.47 | 16.3 | 3.02 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | both | 3-2 | 60.0 | 38.6 | 21.4 | +3.56 | 71.2 | 2.74 | 100.0 | keep collecting (5/30) |
| money_delta+sharp_gap | both | 4-5 | 44.4 | 37.7 | 6.8 | +1.47 | 16.3 | 3.02 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| follow_move+pin_value | both | 5-5 | 50.0 | 49.2 | 0.8 | -0.41 | -4.1 | -0.3 | 30.0 | keep collecting (10/30) |
| consensus_gap+pin_move | both | 2-1 | 66.7 | 52.0 | 14.7 | +0.86 | 28.7 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+pin_value | both | 10-3 | 76.9 | 49.0 | 27.9 | +5.9 | 45.4 | -0.15 | 30.8 | keep collecting (13/30) |
| money_level+pin_move | both | 2-4 | 33.3 | 47.8 | -14.4 | -2.15 | -35.8 | 0.17 | 16.7 | keep collecting (6/30) |
| money_level+pin_value | both | 4-3 | 57.1 | 53.9 | 3.3 | +0.6 | 8.5 | 0.53 | 42.9 | keep collecting (7/30) |
| pin_move+pin_value | both | 4-8 | 33.3 | 49.4 | -16.1 | -4.28 | -35.7 | 0.67 | 41.7 | keep collecting (12/30) |
| money_moving+pin_value | both | 4-2 | 66.7 | 53.1 | 13.6 | +1.64 | 27.3 | 0.78 | 83.3 | keep collecting (6/30) |
| pin_value+sharp_gap | both | 2-4 | 33.3 | 54.7 | -21.4 | -2.22 | -37.0 | 0.95 | 66.7 | keep collecting (6/30) |
| consensus_gap+money_delta | both | 1-0 | 100.0 | 47.6 | 52.4 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 1-0 | 100.0 | 47.6 | 52.4 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | both | 1-0 | 100.0 | 47.6 | 52.4 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+rlm_ratio | both | 1-0 | 100.0 | 47.6 | 52.4 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+sharp_gap | both | 0-3 | 0.0 | 45.9 | -45.9 | -3.0 | -100.0 | 1.0 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | both | 2-1 | 66.7 | 32.7 | 34.0 | +3.65 | 121.7 | 3.57 | 100.0 | keep collecting (3/30) |
| consensus_gap+rlm_quiet | both | 1-1 | 50.0 | 32.7 | 17.3 | +0.6 | 30.0 | 1.1 | 100.0 | keep collecting (2/30) |
| money_moving+pin_move | both | 1-1 | 50.0 | 47.6 | 2.4 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+pin_rlm | both | 0-1 | 0.0 | 32.7 | -32.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 0-1 | 0.0 | 32.7 | -32.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+rlm_quiet | both | 0-1 | 0.0 | 47.6 | -47.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 15-21 | 41.7 | 32.7 | 9.0 | +5.11 | 14.2 | 0.87 | 44.4 | no edge shown yet |
| rlm_quiet | total | 11-13 | 45.8 | 47.6 | -1.7 | -3.0 | -12.5 | 0.75 | 58.3 | keep collecting (24/30) |
| pin_move | moneyline | 1-2 | 33.3 | 55.8 | -22.4 | -1.48 | -49.5 | 0.77 | 33.3 | keep collecting (3/30) |
| pin_move | spread | 1-6 | 14.3 | 47.5 | -33.2 | -5.06 | -72.2 | 0.0 | 14.3 | keep collecting (7/30) |
| pin_move | total | 7-8 | 46.7 | 49.8 | -3.2 | -1.55 | -10.3 | 0.67 | 53.3 | keep collecting (15/30) |
| money_delta | moneyline | 2-4 | 33.3 | 32.7 | 0.6 | +0.65 | 10.8 | 2.7 | 100.0 | keep collecting (6/30) |
| money_delta | total | 2-1 | 66.7 | 47.6 | 19.1 | +0.82 | 27.3 | 3.67 | 100.0 | keep collecting (3/30) |
| pin_rlm | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | keep collecting (2/30) |
| follow_move | moneyline | 97-88 | 52.4 | 46.5 | 5.9 | -1.44 | -0.8 | -0.27 | 34.6 | no edge shown yet |
| follow_move | spread | 51-67 | 43.2 | 50.9 | -7.7 | -19.67 | -16.7 | 0.02 | 28.0 | DROP: below break-even |
| follow_move | total | 84-97 | 46.4 | 49.4 | -3.0 | -20.17 | -11.1 | 0.34 | 47.0 | DROP: below break-even |
| rlm_ratio | moneyline | 4-10 | 28.6 | 35.2 | -6.6 | -1.44 | -10.3 | -0.25 | 35.7 | keep collecting (14/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 55.9 | -55.9 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| rlm_ratio | total | 6-5 | 54.5 | 47.6 | 7.0 | +0.45 | 4.1 | 0.82 | 72.7 | keep collecting (11/30) |
| money_level | moneyline | 37-31 | 54.4 | 63.2 | -8.8 | -19.29 | -28.4 | -0.48 | 35.3 | no edge shown yet |
| money_level | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.06 | -2.9 | 2.0 | 50.0 | keep collecting (2/30) |
| money_level | total | 36-29 | 55.4 | 51.9 | 3.5 | +3.64 | 5.6 | -0.38 | 35.4 | no edge shown yet |
| sharp_gap | moneyline | 24-35 | 40.7 | 50.3 | -9.6 | -13.48 | -22.9 | -0.03 | 47.5 | DROP: below break-even |
| sharp_gap | spread | 0-2 | 0.0 | 55.9 | -55.9 | -2.0 | -100.0 | 3.0 | 100.0 | keep collecting (2/30) |
| sharp_gap | total | 33-26 | 55.9 | 50.0 | 5.9 | +3.92 | 6.6 | 0.39 | 42.4 | no edge shown yet |
| money_moving | moneyline | 19-21 | 47.5 | 48.3 | -0.8 | -4.4 | -11.0 | 0.94 | 60.0 | no edge shown yet |
| money_moving | spread | 0-2 | 0.0 | 55.9 | -55.9 | -2.0 | -100.0 | 3.0 | 100.0 | keep collecting (2/30) |
| money_moving | total | 28-20 | 58.3 | 49.6 | 8.7 | +5.49 | 11.4 | 0.19 | 39.6 | no edge shown yet |
| pin_value | moneyline | 0-1 | 0.0 | 67.3 | -67.3 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| pin_value | spread | 11-11 | 50.0 | 47.8 | 2.2 | -1.42 | -6.5 | 0.14 | 27.3 | keep collecting (22/30) |
| pin_value | total | 12-8 | 60.0 | 50.5 | 9.5 | +2.92 | 14.6 | 0.0 | 40.0 | keep collecting (20/30) |
| consensus_gap | moneyline | 68-59 | 53.5 | 56.9 | -3.4 | -18.43 | -14.5 | 0.39 | 48.8 | no edge shown yet |
| consensus_gap | spread | 30-18 | 62.5 | 47.8 | 14.7 | +8.01 | 16.7 | 0.23 | 33.3 | no edge shown yet |
| consensus_gap | total | 40-46 | 46.5 | 49.9 | -3.4 | -9.9 | -11.5 | 0.81 | 58.1 | no edge shown yet |
| consensus_gap+money_level | moneyline | 19-14 | 57.6 | 64.1 | -6.6 | -6.71 | -20.3 | -0.58 | 33.3 | no edge shown yet |
| follow_move+rlm_quiet | moneyline | 15-21 | 41.7 | 32.7 | 9.0 | +5.11 | 14.2 | 0.87 | 44.4 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 4-10 | 28.6 | 35.2 | -6.6 | -1.44 | -10.3 | -0.25 | 35.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 9-12 | 42.9 | 45.9 | -3.0 | -2.66 | -12.7 | 0.24 | 33.3 | keep collecting (21/30) |
| rlm_quiet+rlm_ratio | moneyline | 4-7 | 36.4 | 32.7 | 3.7 | +1.56 | 14.2 | 0.09 | 36.4 | keep collecting (11/30) |
| rlm_quiet+sharp_gap | moneyline | 4-7 | 36.4 | 32.7 | 3.7 | +1.56 | 14.2 | 0.09 | 36.4 | keep collecting (11/30) |
| rlm_ratio+sharp_gap | moneyline | 4-10 | 28.6 | 35.2 | -6.6 | -1.44 | -10.3 | -0.25 | 35.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 12-7 | 63.2 | 61.8 | 1.3 | -0.62 | -3.2 | 0.11 | 42.1 | keep collecting (19/30) |
| consensus_gap+money_moving | moneyline | 7-4 | 63.6 | 57.9 | 5.8 | -0.8 | -7.3 | 1.5 | 54.5 | keep collecting (11/30) |
| consensus_gap+sharp_gap | moneyline | 12-10 | 54.5 | 59.4 | -4.9 | -4.08 | -18.5 | -0.47 | 36.4 | keep collecting (22/30) |
| money_level+money_moving | moneyline | 8-8 | 50.0 | 60.8 | -10.8 | -4.74 | -29.6 | 1.11 | 56.2 | keep collecting (16/30) |
| money_level+sharp_gap | moneyline | 17-21 | 44.7 | 60.0 | -15.3 | -14.42 | -38.0 | -0.48 | 39.5 | INVERT candidate: wrong well beyond its base rate |
| money_moving+sharp_gap | moneyline | 7-16 | 30.4 | 43.2 | -12.8 | -5.94 | -25.8 | 1.45 | 73.9 | keep collecting (23/30) |
| follow_move+money_level | moneyline | 14-7 | 66.7 | 64.0 | 2.7 | -4.91 | -23.4 | -0.4 | 19.0 | keep collecting (21/30) |
| follow_move+money_moving | moneyline | 10-8 | 55.6 | 46.2 | 9.4 | +2.91 | 16.2 | 0.46 | 38.9 | keep collecting (18/30) |
| money_moving+rlm_quiet | moneyline | 5-6 | 45.5 | 32.7 | 12.7 | +3.35 | 30.5 | 1.3 | 54.5 | keep collecting (11/30) |
| money_moving+rlm_ratio | moneyline | 3-4 | 42.9 | 32.7 | 10.2 | +2.41 | 34.4 | 1.37 | 57.1 | keep collecting (7/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 67.3 | -67.3 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 67.3 | -67.3 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 67.3 | -67.3 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_rlm | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | moneyline | 0-3 | 0.0 | 44.2 | -44.2 | -3.0 | -100.0 | -1.5 | 33.3 | keep collecting (3/30) |
| pin_rlm+rlm_ratio | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+money_moving | moneyline | 2-4 | 33.3 | 32.7 | 0.6 | +0.65 | 10.8 | 2.7 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-4 | 33.3 | 32.7 | 0.6 | +0.65 | 10.8 | 2.7 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_level | moneyline | 0-2 | 0.0 | 32.7 | -32.7 | -2.0 | -100.0 | 1.85 | 100.0 | keep collecting (2/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 32.7 | 34.0 | +3.65 | 121.7 | 3.57 | 100.0 | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 2-1 | 66.7 | 32.7 | 34.0 | +3.65 | 121.7 | 3.57 | 100.0 | keep collecting (3/30) |
| money_delta+rlm_ratio | moneyline | 2-1 | 66.7 | 32.7 | 34.0 | +3.65 | 121.7 | 3.57 | 100.0 | keep collecting (3/30) |
| consensus_gap+rlm_quiet | moneyline | 1-1 | 50.0 | 32.7 | 17.3 | +0.6 | 30.0 | 1.1 | 100.0 | keep collecting (2/30) |
| follow_move+pin_move | moneyline | 0-1 | 0.0 | 32.7 | -32.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_move | moneyline | 0-1 | 0.0 | 32.7 | -32.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 0-1 | 0.0 | 32.7 | -32.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 0-1 | 0.0 | 32.7 | -32.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | moneyline | 0-1 | 0.0 | 32.7 | -32.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_level | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.06 | -2.9 | 2.0 | 50.0 | redundant -- identical record to money_level alone, not independent confirmation |
| follow_move+money_moving | spread | 0-1 | 0.0 | 55.9 | -55.9 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 55.9 | -55.9 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 0-1 | 0.0 | 55.9 | -55.9 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level+money_moving | spread | 0-1 | 0.0 | 55.9 | -55.9 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level+rlm_ratio | spread | 0-1 | 0.0 | 55.9 | -55.9 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 0-1 | 0.0 | 55.9 | -55.9 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 55.9 | -55.9 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+sharp_gap | spread | 0-2 | 0.0 | 55.9 | -55.9 | -2.0 | -100.0 | 3.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 55.9 | -55.9 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 1-2 | 33.3 | 48.0 | -14.7 | -1.09 | -36.4 | -0.33 | 0.0 | keep collecting (3/30) |
| pin_move+pin_value | spread | 0-4 | 0.0 | 47.0 | -47.0 | -4.0 | -100.0 | 0.5 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_value | spread | 4-1 | 80.0 | 46.4 | 33.6 | +2.41 | 48.1 | -0.4 | 0.0 | keep collecting (5/30) |
| follow_move+pin_move | spread | 1-2 | 33.3 | 48.0 | -14.7 | -1.06 | -35.2 | -0.33 | 0.0 | keep collecting (3/30) |
| consensus_gap+pin_move | spread | 0-1 | 0.0 | 55.9 | -55.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | spread | 0-1 | 0.0 | 44.1 | -44.1 | -1.0 | -100.0 | 4.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_move | spread | 1-0 | 100.0 | 44.1 | 55.9 | +0.94 | 94.3 | -1.0 | 0.0 | keep collecting (1/30) |
| money_moving+pin_value | spread | 0-1 | 0.0 | 55.9 | -55.9 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | spread | 0-1 | 0.0 | 55.9 | -55.9 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| follow_move+money_level | total | 11-10 | 52.4 | 51.0 | 1.3 | +0.04 | 0.2 | 0.43 | 52.4 | keep collecting (21/30) |
| follow_move+sharp_gap | total | 15-13 | 53.6 | 49.3 | 4.3 | +0.68 | 2.4 | 0.75 | 53.6 | keep collecting (28/30) |
| money_level+sharp_gap | total | 22-15 | 59.5 | 51.5 | 7.9 | +4.92 | 13.3 | -0.03 | 40.5 | no edge shown yet |
| follow_move+money_moving | total | 9-10 | 47.4 | 48.6 | -1.2 | -1.78 | -9.3 | 0.63 | 47.4 | keep collecting (19/30) |
| money_level+money_moving | total | 15-8 | 65.2 | 51.4 | 13.8 | +5.63 | 24.5 | -0.26 | 39.1 | keep collecting (23/30) |
| follow_move+rlm_quiet | total | 11-13 | 45.8 | 47.6 | -1.7 | -3.0 | -12.5 | 0.75 | 58.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 6-5 | 54.5 | 47.6 | 7.0 | +0.45 | 4.1 | 0.82 | 72.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 5-3 | 62.5 | 47.6 | 14.9 | +1.55 | 19.3 | 0.62 | 62.5 | keep collecting (8/30) |
| rlm_quiet+sharp_gap | total | 6-5 | 54.5 | 47.6 | 7.0 | +0.45 | 4.1 | 0.91 | 54.5 | keep collecting (11/30) |
| rlm_ratio+sharp_gap | total | 6-5 | 54.5 | 47.6 | 7.0 | +0.45 | 4.1 | 0.82 | 72.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | total | 4-4 | 50.0 | 47.6 | 2.4 | -0.36 | -4.5 | 0.38 | 37.5 | keep collecting (8/30) |
| money_moving+rlm_ratio | total | 4-1 | 80.0 | 47.6 | 32.4 | +2.64 | 52.7 | 1.2 | 80.0 | keep collecting (5/30) |
| money_moving+sharp_gap | total | 19-10 | 65.5 | 49.7 | 15.8 | +7.27 | 25.1 | 0.24 | 37.9 | keep collecting (29/30) |
| follow_move+pin_move | total | 3-5 | 37.5 | 48.8 | -11.3 | -2.23 | -27.9 | 1.0 | 62.5 | keep collecting (8/30) |
| consensus_gap+follow_move | total | 6-12 | 33.3 | 48.9 | -15.6 | -6.55 | -36.4 | 1.33 | 72.2 | keep collecting (18/30) |
| consensus_gap+money_level | total | 5-3 | 62.5 | 51.8 | 10.7 | +1.51 | 18.8 | -0.38 | 25.0 | keep collecting (8/30) |
| consensus_gap+sharp_gap | total | 3-5 | 37.5 | 50.6 | -13.1 | -2.31 | -28.9 | -0.12 | 37.5 | keep collecting (8/30) |
| follow_move+money_delta | total | 1-1 | 50.0 | 47.6 | 2.4 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+money_level | total | 1-1 | 50.0 | 47.6 | 2.4 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+money_moving | total | 2-1 | 66.7 | 47.6 | 19.1 | +0.82 | 27.3 | 3.67 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | total | 1-1 | 50.0 | 47.6 | 2.4 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 2-1 | 66.7 | 47.6 | 19.1 | +0.82 | 27.3 | 3.67 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+rlm_ratio | total | 1-2 | 33.3 | 47.6 | -14.2 | -1.09 | -36.4 | 1.33 | 100.0 | keep collecting (3/30) |
| follow_move+pin_value | total | 4-3 | 57.1 | 49.7 | 7.5 | +0.68 | 9.7 | -0.29 | 42.9 | keep collecting (7/30) |
| consensus_gap+pin_move | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | 0.5 | 50.0 | keep collecting (2/30) |
| consensus_gap+pin_value | total | 6-2 | 75.0 | 50.6 | 24.4 | +3.5 | 43.7 | 0.0 | 50.0 | keep collecting (8/30) |
| money_level+pin_move | total | 1-3 | 25.0 | 52.4 | -27.4 | -2.09 | -52.3 | 0.5 | 25.0 | keep collecting (4/30) |
| money_level+pin_value | total | 4-2 | 66.7 | 51.6 | 15.0 | +1.6 | 26.6 | 0.33 | 33.3 | keep collecting (6/30) |
| pin_move+pin_value | total | 4-4 | 50.0 | 50.6 | -0.6 | -0.28 | -3.5 | 0.75 | 50.0 | keep collecting (8/30) |
| consensus_gap+money_delta | total | 1-0 | 100.0 | 47.6 | 52.4 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_moving | total | 3-1 | 75.0 | 47.6 | 27.4 | +1.77 | 44.2 | 0.5 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 1-0 | 100.0 | 47.6 | 52.4 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | total | 1-0 | 100.0 | 47.6 | 52.4 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | total | 4-0 | 100.0 | 48.8 | 51.2 | +3.64 | 91.0 | 0.5 | 75.0 | keep collecting (4/30) |
| pin_value+rlm_ratio | total | 1-0 | 100.0 | 47.6 | 52.4 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | total | 2-2 | 50.0 | 51.2 | -1.2 | -0.22 | -5.5 | 0.75 | 50.0 | keep collecting (4/30) |
| pin_move+sharp_gap | total | 0-2 | 0.0 | 52.4 | -52.4 | -2.0 | -100.0 | 1.5 | 50.0 | keep collecting (2/30) |
| money_moving+pin_move | total | 1-1 | 50.0 | 47.6 | 2.4 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+rlm_quiet | total | 0-1 | 0.0 | 47.6 | -47.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 111-177 | 38.5 | 42.8 | -4.3 | -43.27 | -15.0 |  |  | DROP: below break-even |
| pin_move | both | 205-217 | 48.6 | 49.4 | -0.8 | -18.63 | -4.4 |  |  | DROP: below break-even |
| money_delta | both | 100-129 | 43.7 | 44.0 | -0.3 | -24.55 | -10.7 |  |  | DROP: below break-even |
| pin_rlm | both | 42-63 | 40.0 | 42.0 | -2.0 | -16.33 | -15.6 |  |  | DROP: below break-even |
| follow_move | both | 329-365 | 47.4 | 49.1 | -1.7 | -66.71 | -9.6 |  |  | DROP: below break-even |
| rlm_ratio | both | 71-117 | 37.8 | 42.4 | -4.6 | -39.92 | -21.2 |  |  | DROP: below break-even |
| money_level | both | 424-328 | 56.4 | 55.0 | 1.4 | -31.3 | -4.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 324-383 | 45.8 | 48.5 | -2.6 | -89.08 | -12.6 |  |  | DROP: below break-even |
| money_moving | both | 337-374 | 47.4 | 48.9 | -1.5 | -73.57 | -10.3 |  |  | DROP: below break-even |
| pin_value | both | 156-153 | 50.5 | 49.6 | 0.9 | +1.62 | 0.5 |  |  | no edge shown yet |
| consensus_gap | both | 138-108 | 56.1 | 52.8 | 3.3 | +2.91 | 1.2 |  |  | no edge shown yet |
| follow_move+pin_move | both | 140-173 | 44.7 | 48.9 | -4.2 | -41.13 | -13.1 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 75-100 | 42.9 | 42.6 | 0.2 | -18.61 | -10.6 |  |  | DROP: below break-even |
| money_delta+sharp_gap | both | 75-99 | 43.1 | 42.6 | 0.5 | -17.61 | -10.1 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 315-362 | 46.5 | 48.6 | -2.1 | -73.97 | -10.9 |  |  | DROP: below break-even |
| consensus_gap+money_level | both | 92-55 | 62.6 | 58.7 | 3.9 | -0.0 | -0.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+rlm_quiet | both | 111-177 | 38.5 | 42.8 | -4.3 | -43.27 | -15.0 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | both | 54-80 | 40.3 | 43.8 | -3.5 | -17.34 | -12.9 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 38-36 | 51.4 | 51.0 | 0.3 | -6.64 | -9.0 |  |  | no edge shown yet |
| follow_move+money_level | both | 160-131 | 55.0 | 55.1 | -0.2 | -19.38 | -6.7 |  |  | no edge shown yet |
| money_level+money_moving | both | 229-208 | 52.4 | 52.8 | -0.4 | -28.86 | -6.6 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 217-209 | 50.9 | 52.5 | -1.6 | -35.82 | -8.4 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 47-56 | 45.6 | 50.9 | -5.3 | -13.82 | -13.4 |  |  | no edge shown yet |
| consensus_gap+pin_move | both | 38-23 | 62.3 | 50.4 | 11.9 | +15.83 | 25.9 |  |  | PROMOTE: beats break-even and its own base rate |
| consensus_gap+pin_value | both | 45-41 | 52.3 | 49.2 | 3.1 | +2.95 | 3.4 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | both | 47-60 | 43.9 | 50.4 | -6.5 | -17.69 | -16.5 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 171-202 | 45.8 | 48.4 | -2.6 | -49.07 | -13.2 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 51-47 | 52.0 | 50.2 | 1.8 | +8.39 | 8.6 |  |  | no edge shown yet |
| follow_move+sharp_gap | both | 167-205 | 44.9 | 48.1 | -3.2 | -51.78 | -13.9 |  |  | DROP: below break-even |
| money_level+pin_move | both | 93-86 | 52.0 | 53.6 | -1.6 | -12.87 | -7.2 |  |  | no edge shown yet |
| money_level+pin_value | both | 69-72 | 48.9 | 50.6 | -1.6 | -11.57 | -8.2 |  |  | no edge shown yet |
| money_moving+pin_move | both | 99-108 | 47.8 | 48.5 | -0.7 | -15.85 | -7.7 |  |  | no edge shown yet |
| money_moving+pin_value | both | 60-72 | 45.5 | 49.8 | -4.3 | -15.23 | -11.5 |  |  | DROP: below break-even |
| pin_move+pin_value | both | 63-66 | 48.8 | 51.0 | -2.2 | -9.67 | -7.5 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 94-114 | 45.2 | 48.1 | -2.9 | -24.97 | -12.0 |  |  | DROP: below break-even |
| pin_value+sharp_gap | both | 59-76 | 43.7 | 50.0 | -6.3 | -20.14 | -14.9 |  |  | DROP: below break-even |
| follow_move+money_delta | both | 52-84 | 38.2 | 43.9 | -5.6 | -31.9 | -23.5 |  |  | DROP: below break-even |
| money_delta+pin_move | both | 32-41 | 43.8 | 44.4 | -0.6 | -10.06 | -13.8 |  |  | no edge shown yet |
| money_delta+rlm_quiet | both | 29-57 | 33.7 | 41.8 | -8.1 | -26.07 | -30.3 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | both | 71-117 | 37.8 | 42.4 | -4.6 | -39.92 | -21.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | both | 51-93 | 35.4 | 41.8 | -6.4 | -34.83 | -24.2 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 69-111 | 38.3 | 42.6 | -4.2 | -36.55 | -20.3 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 36-84 | 30.0 | 40.4 | -10.4 | -40.22 | -33.5 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | both | 51-95 | 34.9 | 41.8 | -6.8 | -36.73 | -25.2 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 71-117 | 37.8 | 42.4 | -4.6 | -39.92 | -21.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | both | 26-27 | 49.1 | 47.2 | 1.9 | -1.56 | -2.9 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 9-17 | 34.6 | 39.8 | -5.2 | -6.72 | -25.9 |  |  | keep collecting (26/30) |
| consensus_gap+rlm_ratio | both | 9-12 | 42.9 | 40.6 | 2.2 | -1.92 | -9.1 |  |  | keep collecting (21/30) |
| money_delta+rlm_ratio | both | 35-64 | 35.4 | 41.9 | -6.6 | -27.49 | -27.8 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 7-7 | 50.0 | 43.9 | 6.1 | +1.58 | 11.3 |  |  | keep collecting (14/30) |
| money_level+pin_rlm | both | 13-15 | 46.4 | 46.2 | 0.2 | -2.66 | -9.5 |  |  | keep collecting (28/30) |
| money_moving+pin_rlm | both | 42-57 | 42.4 | 42.4 | 0.1 | -10.33 | -10.4 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 42-63 | 40.0 | 42.0 | -2.0 | -16.33 | -15.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | both | 27-25 | 51.9 | 46.7 | 5.3 | +0.17 | 0.3 |  |  | no edge shown yet |
| consensus_gap+money_delta | both | 14-10 | 58.3 | 43.0 | 15.4 | +6.9 | 28.7 |  |  | keep collecting (24/30) |
| follow_move+pin_rlm | both | 35-55 | 38.9 | 41.6 | -2.7 | -15.4 | -17.1 |  |  | DROP: below break-even |
| money_delta+pin_rlm | both | 22-33 | 40.0 | 41.8 | -1.8 | -10.72 | -19.5 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 39-54 | 41.9 | 42.8 | -0.8 | -11.41 | -12.3 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | both | 35-51 | 40.7 | 43.0 | -2.3 | -12.87 | -15.0 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 19-41 | 31.7 | 39.9 | -8.2 | -16.8 | -28.0 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | both | 35-55 | 38.9 | 41.6 | -2.7 | -15.4 | -17.1 |  |  | DROP: below break-even |
| money_delta+pin_value | both | 21-11 | 65.6 | 48.5 | 17.1 | +12.02 | 37.6 |  |  | no edge shown yet |
| pin_value+rlm_quiet | both | 14-16 | 46.7 | 48.1 | -1.4 | +6.87 | 22.9 |  |  | no edge shown yet |
| pin_value+rlm_ratio | both | 7-7 | 50.0 | 48.1 | 1.9 | -0.31 | -2.2 |  |  | keep collecting (14/30) |
| pin_rlm+pin_value | both | 8-9 | 47.1 | 49.2 | -2.2 | -1.33 | -7.8 |  |  | keep collecting (17/30) |
| rlm_quiet | moneyline | 41-80 | 33.9 | 33.3 | 0.6 | -11.58 | -9.6 |  |  | DROP: below break-even |
| rlm_quiet | spread | 22-28 | 44.0 | 54.0 | -10.0 | -7.32 | -14.6 |  |  | no edge shown yet |
| rlm_quiet | total | 48-69 | 41.0 | 47.9 | -6.9 | -24.37 | -20.8 |  |  | DROP: below break-even |
| pin_move | moneyline | 60-53 | 53.1 | 46.2 | 6.9 | +13.25 | 11.7 |  |  | no edge shown yet |
| pin_move | spread | 69-73 | 48.6 | 51.7 | -3.1 | -10.52 | -7.4 |  |  | no edge shown yet |
| pin_move | total | 76-91 | 45.5 | 49.6 | -4.1 | -21.36 | -12.8 |  |  | DROP: below break-even |
| money_delta | moneyline | 27-53 | 33.8 | 35.3 | -1.6 | -15.77 | -19.7 |  |  | DROP: below break-even |
| money_delta | spread | 19-19 | 50.0 | 50.6 | -0.6 | -1.54 | -4.0 |  |  | no edge shown yet |
| money_delta | total | 54-57 | 48.6 | 47.9 | 0.7 | -7.24 | -6.5 |  |  | no edge shown yet |
| pin_rlm | moneyline | 16-33 | 32.7 | 34.1 | -1.5 | -10.12 | -20.7 |  |  | DROP: below break-even |
| pin_rlm | spread | 5-3 | 62.5 | 51.5 | 11.0 | +1.51 | 18.9 |  |  | keep collecting (8/30) |
| pin_rlm | total | 21-27 | 43.8 | 48.4 | -4.6 | -7.72 | -16.1 |  |  | no edge shown yet |
| follow_move | moneyline | 116-127 | 47.7 | 47.4 | 0.4 | -24.14 | -9.9 |  |  | no edge shown yet |
| follow_move | spread | 93-100 | 48.2 | 51.1 | -2.9 | -14.7 | -7.6 |  |  | no edge shown yet |
| follow_move | total | 120-138 | 46.5 | 49.4 | -2.8 | -27.87 | -10.8 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 24-58 | 29.3 | 33.6 | -4.3 | -23.8 | -29.0 |  |  | DROP: below break-even |
| rlm_ratio | spread | 12-9 | 57.1 | 52.5 | 4.6 | +1.72 | 8.2 |  |  | keep collecting (21/30) |
| rlm_ratio | total | 35-50 | 41.2 | 48.4 | -7.2 | -17.84 | -21.0 |  |  | DROP: below break-even |
| money_level | moneyline | 170-94 | 64.4 | 64.0 | 0.4 | -25.87 | -9.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 105-99 | 51.5 | 48.4 | 3.1 | -4.9 | -2.4 |  |  | no edge shown yet |
| money_level | total | 149-135 | 52.5 | 51.4 | 1.1 | -0.53 | -0.2 |  |  | no edge shown yet |
| sharp_gap | moneyline | 98-138 | 41.5 | 45.7 | -4.2 | -48.73 | -20.6 |  |  | DROP: below break-even |
| sharp_gap | spread | 104-101 | 50.7 | 49.4 | 1.3 | -7.46 | -3.6 |  |  | no edge shown yet |
| sharp_gap | total | 122-144 | 45.9 | 50.1 | -4.3 | -32.89 | -12.4 |  |  | DROP: below break-even |
| money_moving | moneyline | 107-127 | 45.7 | 46.9 | -1.2 | -34.83 | -14.9 |  |  | DROP: below break-even |
| money_moving | spread | 104-101 | 50.7 | 49.4 | 1.3 | -7.46 | -3.6 |  |  | no edge shown yet |
| money_moving | total | 126-146 | 46.3 | 50.1 | -3.8 | -31.28 | -11.5 |  |  | DROP: below break-even |
| pin_value | moneyline | 8-14 | 36.4 | 43.7 | -7.3 | +9.75 | 44.3 |  |  | keep collecting (22/30) |
| pin_value | spread | 74-64 | 53.6 | 49.7 | 4.0 | +0.18 | 0.1 |  |  | no edge shown yet |
| pin_value | total | 74-75 | 49.7 | 50.5 | -0.8 | -8.31 | -5.6 |  |  | no edge shown yet |
| consensus_gap | moneyline | 72-56 | 56.2 | 55.1 | 1.1 | -3.21 | -2.5 |  |  | no edge shown yet |
| consensus_gap | spread | 29-21 | 58.0 | 49.0 | 9.0 | +4.16 | 8.3 |  |  | no edge shown yet |
| consensus_gap | total | 37-31 | 54.4 | 51.0 | 3.4 | +1.96 | 2.9 |  |  | no edge shown yet |
| consensus_gap+money_level | moneyline | 56-25 | 69.1 | 65.2 | 4.0 | -1.56 | -1.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+pin_move | moneyline | 44-48 | 47.8 | 45.5 | 2.3 | -4.11 | -4.5 |  |  | no edge shown yet |
| follow_move+rlm_quiet | moneyline | 41-80 | 33.9 | 33.3 | 0.6 | -11.58 | -9.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | moneyline | 21-31 | 40.4 | 33.4 | 7.0 | +0.83 | 1.6 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 21-19 | 52.5 | 51.7 | 0.8 | -4.82 | -12.1 |  |  | no edge shown yet |
| follow_move+money_level | moneyline | 66-41 | 61.7 | 63.1 | -1.4 | -14.83 | -13.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 93-122 | 43.3 | 45.9 | -2.6 | -34.95 | -16.3 |  |  | DROP: below break-even |
| follow_move+money_moving | moneyline | 59-75 | 44.0 | 45.4 | -1.3 | -24.18 | -18.0 |  |  | DROP: below break-even |
| follow_move+sharp_gap | moneyline | 54-78 | 40.9 | 44.5 | -3.6 | -27.8 | -21.1 |  |  | DROP: below break-even |
| money_level+money_moving | moneyline | 69-48 | 59.0 | 60.5 | -1.5 | -12.9 | -11.0 |  |  | no edge shown yet |
| money_level+sharp_gap | moneyline | 61-51 | 54.5 | 59.9 | -5.4 | -18.3 | -16.3 |  |  | no edge shown yet |
| follow_move+rlm_ratio | moneyline | 24-58 | 29.3 | 33.6 | -4.3 | -23.8 | -29.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | moneyline | 20-46 | 30.3 | 32.7 | -2.4 | -16.48 | -25.0 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 23-54 | 29.9 | 33.6 | -3.7 | -21.52 | -28.0 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | moneyline | 17-45 | 27.4 | 32.7 | -5.3 | -18.72 | -30.2 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 20-47 | 29.9 | 32.7 | -2.9 | -17.34 | -25.9 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 24-58 | 29.3 | 33.6 | -4.3 | -23.8 | -29.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 22-28 | 44.0 | 51.4 | -7.4 | -7.95 | -15.9 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | moneyline | 3-12 | 20.0 | 32.7 | -12.7 | -7.22 | -48.1 |  |  | keep collecting (15/30) |
| consensus_gap+rlm_ratio | moneyline | 3-8 | 27.3 | 32.7 | -5.4 | -3.22 | -29.3 |  |  | keep collecting (11/30) |
| consensus_gap+sharp_gap | moneyline | 22-31 | 41.5 | 50.3 | -8.8 | -10.81 | -20.4 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | moneyline | 4-3 | 57.1 | 37.6 | 19.5 | +2.88 | 41.1 |  |  | keep collecting (7/30) |
| money_level+pin_rlm | moneyline | 3-5 | 37.5 | 41.4 | -3.9 | -1.8 | -22.5 |  |  | keep collecting (8/30) |
| money_moving+pin_rlm | moneyline | 16-28 | 36.4 | 34.3 | 2.1 | -5.12 | -11.6 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 16-33 | 32.7 | 34.1 | -1.5 | -10.12 | -20.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 4-7 | 36.4 | 42.1 | -5.8 | +0.84 | 7.7 |  |  | keep collecting (11/30) |
| money_level+rlm_ratio | moneyline | 4-10 | 28.6 | 37.6 | -9.1 | -5.66 | -40.5 |  |  | keep collecting (14/30) |
| consensus_gap+pin_move | moneyline | 21-5 | 80.8 | 50.0 | 30.8 | +18.81 | 72.4 |  |  | keep collecting (26/30) |
| money_level+pin_move | moneyline | 28-17 | 62.2 | 62.7 | -0.5 | -2.29 | -5.1 |  |  | no edge shown yet |
| consensus_gap+money_delta | moneyline | 5-7 | 41.7 | 35.6 | 6.1 | +1.83 | 15.2 |  |  | keep collecting (12/30) |
| follow_move+money_delta | moneyline | 15-36 | 29.4 | 36.1 | -6.7 | -17.89 | -35.1 |  |  | DROP: below break-even |
| follow_move+pin_rlm | moneyline | 13-28 | 31.7 | 33.6 | -1.8 | -8.58 | -20.9 |  |  | DROP: below break-even |
| money_delta+money_moving | moneyline | 25-49 | 33.8 | 34.6 | -0.8 | -13.51 | -18.3 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 9-13 | 40.9 | 34.3 | 6.6 | -3.14 | -14.3 |  |  | keep collecting (22/30) |
| money_delta+pin_rlm | moneyline | 9-17 | 34.6 | 34.0 | 0.6 | -6.72 | -25.8 |  |  | keep collecting (26/30) |
| money_delta+rlm_quiet | moneyline | 9-28 | 24.3 | 32.7 | -8.4 | -15.69 | -42.4 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | moneyline | 11-34 | 24.4 | 34.2 | -9.8 | -19.47 | -43.3 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 25-49 | 33.8 | 34.6 | -0.8 | -13.51 | -18.3 |  |  | DROP: below break-even |
| money_moving+pin_move | moneyline | 24-26 | 48.0 | 43.1 | 4.9 | -1.65 | -3.3 |  |  | no edge shown yet |
| pin_move+pin_rlm | moneyline | 13-24 | 35.1 | 33.6 | 1.5 | -5.2 | -14.1 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 10-23 | 30.3 | 33.8 | -3.5 | -7.66 | -23.2 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 22-31 | 41.5 | 41.8 | -0.3 | -7.04 | -13.3 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 10-23 | 30.3 | 32.7 | -2.4 | -7.08 | -21.5 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 13-28 | 31.7 | 33.6 | -1.8 | -8.58 | -20.9 |  |  | DROP: below break-even |
| follow_move+pin_value | moneyline | 3-3 | 50.0 | 50.0 | 0.0 | +9.55 | 159.1 |  |  | keep collecting (6/30) |
| pin_value+rlm_quiet | moneyline | 2-1 | 66.7 | 32.7 | 34.0 | +10.98 | 366.0 |  |  | keep collecting (3/30) |
| money_delta+money_level | moneyline | 7-5 | 58.3 | 44.2 | 14.1 | +3.11 | 25.9 |  |  | keep collecting (12/30) |
| money_level+pin_value | moneyline | 1-6 | 14.3 | 62.4 | -48.1 | -5.43 | -77.6 |  |  | keep collecting (7/30) |
| pin_move+pin_value | moneyline | 3-4 | 42.9 | 52.5 | -9.6 | -0.97 | -13.9 |  |  | keep collecting (7/30) |
| money_delta+pin_value | moneyline | 2-0 | 100.0 | 32.7 | 67.3 | +5.88 | 294.0 |  |  | keep collecting (2/30) |
| money_moving+pin_value | moneyline | 3-4 | 42.9 | 42.6 | 0.3 | +2.45 | 35.0 |  |  | keep collecting (7/30) |
| pin_value+sharp_gap | moneyline | 3-6 | 33.3 | 48.1 | -14.7 | +0.45 | 5.0 |  |  | keep collecting (9/30) |
| pin_rlm+pin_value | moneyline | 1-0 | 100.0 | 32.7 | 67.3 | +1.38 | 138.0 |  |  | keep collecting (1/30) |
| pin_value+rlm_ratio | moneyline | 1-0 | 100.0 | 32.7 | 67.3 | +1.38 | 138.0 |  |  | keep collecting (1/30) |
| follow_move+pin_move | spread | 41-52 | 44.1 | 51.6 | -7.5 | -14.6 | -15.7 |  |  | DROP: below break-even |
| money_moving+sharp_gap | spread | 104-101 | 50.7 | 49.4 | 1.3 | -7.46 | -3.6 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 22-28 | 44.0 | 54.0 | -10.0 | -7.32 | -14.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | spread | 78-74 | 51.3 | 48.5 | 2.8 | -4.14 | -2.7 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 78-74 | 51.3 | 48.5 | 2.8 | -4.14 | -2.7 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 12-18 | 40.0 | 54.4 | -14.4 | -6.75 | -22.5 |  |  | no edge shown yet |
| consensus_gap+pin_value | spread | 21-15 | 58.3 | 49.7 | 8.7 | +3.32 | 9.2 |  |  | no edge shown yet |
| follow_move+money_level | spread | 34-31 | 52.3 | 50.1 | 2.2 | -0.14 | -0.2 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 41-39 | 51.2 | 51.2 | 0.1 | -1.79 | -2.2 |  |  | no edge shown yet |
| follow_move+sharp_gap | spread | 41-39 | 51.2 | 51.2 | 0.1 | -1.79 | -2.2 |  |  | no edge shown yet |
| money_level+pin_move | spread | 25-26 | 49.0 | 49.9 | -0.9 | -3.8 | -7.5 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 32-30 | 51.6 | 51.0 | 0.7 | -1.45 | -2.3 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 32-30 | 51.6 | 51.0 | 0.7 | -1.45 | -2.3 |  |  | no edge shown yet |
| money_delta+money_level | spread | 7-6 | 53.8 | 46.8 | 7.0 | +0.27 | 2.1 |  |  | keep collecting (13/30) |
| money_delta+money_moving | spread | 13-13 | 50.0 | 49.5 | 0.5 | -1.24 | -4.8 |  |  | keep collecting (26/30) |
| money_delta+sharp_gap | spread | 13-13 | 50.0 | 49.5 | 0.5 | -1.24 | -4.8 |  |  | keep collecting (26/30) |
| consensus_gap+money_level | spread | 10-12 | 45.5 | 47.8 | -2.4 | -3.4 | -15.5 |  |  | keep collecting (22/30) |
| consensus_gap+money_moving | spread | 8-9 | 47.1 | 49.7 | -2.6 | -2.08 | -12.2 |  |  | keep collecting (17/30) |
| consensus_gap+sharp_gap | spread | 8-9 | 47.1 | 49.7 | -2.6 | -2.08 | -12.2 |  |  | keep collecting (17/30) |
| money_level+pin_value | spread | 28-28 | 50.0 | 47.7 | 2.3 | -3.96 | -7.1 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 27-32 | 45.8 | 49.5 | -3.7 | -8.69 | -14.7 |  |  | no edge shown yet |
| pin_value+sharp_gap | spread | 27-32 | 45.8 | 49.5 | -3.7 | -8.69 | -14.7 |  |  | no edge shown yet |
| follow_move+money_delta | spread | 8-8 | 50.0 | 51.5 | -1.5 | -0.79 | -4.9 |  |  | keep collecting (16/30) |
| follow_move+rlm_ratio | spread | 12-9 | 57.1 | 52.5 | 4.6 | +1.72 | 8.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | spread | 3-4 | 42.9 | 50.8 | -8.0 | -1.4 | -20.0 |  |  | keep collecting (7/30) |
| money_moving+rlm_ratio | spread | 12-9 | 57.1 | 52.5 | 4.6 | +1.72 | 8.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 12-9 | 57.1 | 52.5 | 4.6 | +1.72 | 8.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 19-16 | 54.3 | 50.8 | 3.4 | +0.62 | 1.8 |  |  | no edge shown yet |
| pin_move+pin_value | spread | 32-27 | 54.2 | 51.9 | 2.3 | +0.99 | 1.7 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 9-10 | 47.4 | 50.9 | -3.6 | -2.14 | -11.3 |  |  | keep collecting (19/30) |
| consensus_gap+follow_move | spread | 6-5 | 54.5 | 50.5 | 4.0 | +0.32 | 2.9 |  |  | keep collecting (11/30) |
| consensus_gap+rlm_quiet | spread | 2-0 | 100.0 | 55.9 | 44.1 | +1.82 | 90.9 |  |  | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 3-3 | 50.0 | 55.9 | -5.9 | -0.33 | -5.6 |  |  | keep collecting (6/30) |
| money_delta+rlm_quiet | spread | 4-4 | 50.0 | 54.5 | -4.5 | -0.22 | -2.8 |  |  | keep collecting (8/30) |
| money_moving+rlm_quiet | spread | 8-8 | 50.0 | 55.2 | -5.2 | -0.62 | -3.9 |  |  | keep collecting (16/30) |
| rlm_quiet+rlm_ratio | spread | 1-4 | 20.0 | 55.9 | -35.9 | -3.13 | -62.6 |  |  | keep collecting (5/30) |
| rlm_quiet+sharp_gap | spread | 8-8 | 50.0 | 55.2 | -5.2 | -0.62 | -3.9 |  |  | keep collecting (16/30) |
| consensus_gap+money_delta | spread | 3-1 | 75.0 | 55.9 | 19.1 | +1.63 | 40.8 |  |  | keep collecting (4/30) |
| money_delta+pin_move | spread | 7-4 | 63.6 | 52.7 | 10.9 | +2.19 | 19.9 |  |  | keep collecting (11/30) |
| money_delta+pin_value | spread | 6-3 | 66.7 | 53.3 | 13.4 | +2.32 | 25.8 |  |  | keep collecting (9/30) |
| money_moving+pin_rlm | spread | 5-3 | 62.5 | 51.5 | 11.0 | +1.51 | 18.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | spread | 5-3 | 62.5 | 51.5 | 11.0 | +1.51 | 18.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | spread | 3-1 | 75.0 | 55.9 | 19.1 | +1.7 | 42.4 |  |  | keep collecting (4/30) |
| pin_rlm+sharp_gap | spread | 5-3 | 62.5 | 51.5 | 11.0 | +1.51 | 18.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+rlm_ratio | spread | 3-0 | 100.0 | 52.0 | 48.0 | +2.59 | 86.3 |  |  | keep collecting (3/30) |
| money_level+rlm_ratio | spread | 10-2 | 83.3 | 52.0 | 31.4 | +6.94 | 57.9 |  |  | keep collecting (12/30) |
| pin_move+rlm_ratio | spread | 5-2 | 71.4 | 50.8 | 20.6 | +2.42 | 34.6 |  |  | keep collecting (7/30) |
| pin_value+rlm_ratio | spread | 1-0 | 100.0 | 55.9 | 44.1 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| follow_move+pin_rlm | spread | 2-2 | 50.0 | 47.0 | 3.0 | -0.18 | -4.5 |  |  | keep collecting (4/30) |
| money_delta+pin_rlm | spread | 3-2 | 60.0 | 53.6 | 6.4 | +0.7 | 13.9 |  |  | keep collecting (5/30) |
| pin_rlm+rlm_quiet | spread | 0-1 | 0.0 | 55.9 | -55.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+rlm_ratio | spread | 2-2 | 50.0 | 47.0 | 3.0 | -0.18 | -4.5 |  |  | keep collecting (4/30) |
| money_level+pin_rlm | spread | 2-2 | 50.0 | 47.0 | 3.0 | -0.18 | -4.5 |  |  | keep collecting (4/30) |
| consensus_gap+pin_rlm | spread | 2-1 | 66.7 | 52.0 | 14.7 | +0.79 | 26.2 |  |  | keep collecting (3/30) |
| money_delta+money_moving | total | 37-38 | 49.3 | 48.1 | 1.2 | -3.87 | -5.2 |  |  | no edge shown yet |
| money_delta+sharp_gap | total | 37-37 | 50.0 | 48.1 | 1.9 | -2.87 | -3.9 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 118-139 | 45.9 | 50.1 | -4.2 | -31.56 | -12.3 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | total | 48-69 | 41.0 | 47.9 | -6.9 | -24.37 | -20.8 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+follow_move | total | 11-12 | 47.8 | 50.1 | -2.3 | -2.13 | -9.3 |  |  | keep collecting (23/30) |
| consensus_gap+money_level | total | 26-18 | 59.1 | 52.2 | 6.9 | +4.95 | 11.3 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 17-19 | 47.2 | 51.0 | -3.7 | -3.79 | -10.5 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 8-8 | 50.0 | 50.3 | -0.3 | -0.84 | -5.3 |  |  | keep collecting (16/30) |
| consensus_gap+pin_value | total | 20-19 | 51.3 | 50.8 | 0.5 | -1.21 | -3.1 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 17-20 | 45.9 | 50.9 | -4.9 | -4.79 | -13.0 |  |  | no edge shown yet |
| follow_move+money_level | total | 60-59 | 50.4 | 50.8 | -0.3 | -4.42 | -3.7 |  |  | no edge shown yet |
| follow_move+money_moving | total | 71-88 | 44.7 | 49.6 | -4.9 | -23.1 | -14.5 |  |  | DROP: below break-even |
| follow_move+pin_move | total | 55-73 | 43.0 | 49.5 | -6.5 | -22.42 | -17.5 |  |  | DROP: below break-even |
| follow_move+pin_value | total | 29-28 | 50.9 | 49.9 | 1.0 | -1.78 | -3.1 |  |  | no edge shown yet |
| follow_move+sharp_gap | total | 72-88 | 45.0 | 49.6 | -4.6 | -22.2 | -13.9 |  |  | DROP: below break-even |
| money_level+money_moving | total | 82-86 | 48.8 | 51.2 | -2.4 | -11.82 | -7.0 |  |  | no edge shown yet |
| money_level+pin_move | total | 40-43 | 48.2 | 50.9 | -2.7 | -6.78 | -8.2 |  |  | no edge shown yet |
| money_level+pin_value | total | 40-38 | 51.3 | 51.6 | -0.3 | -2.18 | -2.8 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 78-84 | 48.1 | 51.2 | -3.1 | -13.38 | -8.3 |  |  | no edge shown yet |
| money_moving+pin_move | total | 43-52 | 45.3 | 49.8 | -4.6 | -12.75 | -13.4 |  |  | no edge shown yet |
| money_moving+pin_value | total | 30-36 | 45.5 | 50.7 | -5.3 | -9.0 | -13.6 |  |  | no edge shown yet |
| pin_move+pin_value | total | 28-35 | 44.4 | 50.0 | -5.6 | -9.69 | -15.4 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 40-53 | 43.0 | 49.8 | -6.8 | -16.49 | -17.7 |  |  | DROP: below break-even |
| pin_value+sharp_gap | total | 29-38 | 43.3 | 50.7 | -7.4 | -11.91 | -17.8 |  |  | no edge shown yet |
| follow_move+money_delta | total | 29-40 | 42.0 | 47.8 | -5.8 | -13.22 | -19.2 |  |  | DROP: below break-even |
| money_delta+pin_move | total | 16-24 | 40.0 | 47.7 | -7.7 | -9.11 | -22.8 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | total | 16-25 | 39.0 | 47.6 | -8.5 | -10.16 | -24.8 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | total | 21-31 | 40.4 | 48.1 | -7.7 | -11.43 | -22.0 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | total | 35-50 | 41.2 | 48.4 | -7.2 | -17.84 | -21.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | total | 21-26 | 44.7 | 48.0 | -3.3 | -6.62 | -14.1 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 23-39 | 37.1 | 48.0 | -10.9 | -17.73 | -28.6 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | total | 34-48 | 41.5 | 48.4 | -7.0 | -16.75 | -20.4 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | total | 18-35 | 34.0 | 48.0 | -14.1 | -18.37 | -34.7 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | total | 23-40 | 36.5 | 48.0 | -11.5 | -18.78 | -29.8 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | total | 35-50 | 41.2 | 48.4 | -7.2 | -17.84 | -21.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | total | 6-2 | 75.0 | 47.6 | 27.4 | +3.44 | 43.0 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_quiet | total | 4-5 | 44.4 | 48.1 | -3.7 | -1.32 | -14.7 |  |  | keep collecting (9/30) |
| consensus_gap+rlm_ratio | total | 3-4 | 42.9 | 48.3 | -5.4 | -1.29 | -18.4 |  |  | keep collecting (7/30) |
| money_delta+pin_value | total | 13-8 | 61.9 | 48.0 | 13.9 | +3.82 | 18.2 |  |  | keep collecting (21/30) |
| pin_value+rlm_quiet | total | 9-12 | 42.9 | 48.0 | -5.2 | -3.77 | -18.0 |  |  | keep collecting (21/30) |
| pin_value+rlm_ratio | total | 5-7 | 41.7 | 48.8 | -7.1 | -2.53 | -21.1 |  |  | keep collecting (12/30) |
| follow_move+pin_rlm | total | 20-25 | 44.4 | 48.4 | -4.0 | -6.63 | -14.7 |  |  | no edge shown yet |
| money_delta+money_level | total | 12-16 | 42.9 | 48.6 | -5.7 | -4.94 | -17.6 |  |  | keep collecting (28/30) |
| money_delta+pin_rlm | total | 10-14 | 41.7 | 47.8 | -6.1 | -4.7 | -19.6 |  |  | keep collecting (24/30) |
| money_level+pin_rlm | total | 8-8 | 50.0 | 48.5 | 1.5 | -0.68 | -4.3 |  |  | keep collecting (16/30) |
| money_level+rlm_ratio | total | 13-13 | 50.0 | 49.1 | 0.9 | -1.11 | -4.3 |  |  | keep collecting (26/30) |
| money_moving+pin_rlm | total | 21-26 | 44.7 | 48.4 | -3.7 | -6.72 | -14.3 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 21-27 | 43.8 | 48.4 | -4.6 | -7.72 | -16.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 20-26 | 43.5 | 48.5 | -5.0 | -7.63 | -16.6 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 20-25 | 44.4 | 48.4 | -4.0 | -6.63 | -14.7 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 21-27 | 43.8 | 48.4 | -4.6 | -7.72 | -16.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | total | 9-17 | 34.6 | 48.3 | -13.7 | -8.72 | -33.5 |  |  | keep collecting (26/30) |
| consensus_gap+pin_rlm | total | 1-3 | 25.0 | 48.8 | -23.8 | -2.09 | -52.3 |  |  | keep collecting (4/30) |
| pin_rlm+pin_value | total | 4-8 | 33.3 | 48.4 | -15.0 | -4.4 | -36.7 |  |  | keep collecting (12/30) |

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
| rlm_quiet | both | 56-70 | 44.4 | 36.9 | 7.6 | +12.7 | 10.1 | 0.49 | 46.8 | DROP: below break-even |
| pin_move | both | 14-25 | 35.9 | 49.7 | -13.8 | -13.19 | -33.8 | 0.39 | 43.6 | DROP: below break-even |
| money_delta | both | 14-12 | 53.8 | 39.9 | 13.9 | +5.9 | 22.7 | 0.9 | 53.8 | keep collecting (26/30) |
| pin_rlm | both | 1-4 | 20.0 | 37.1 | -17.1 | -3.07 | -61.5 | -0.3 | 60.0 | keep collecting (5/30) |
| follow_move | both | 706-654 | 51.9 | 50.9 | 1.1 | -85.76 | -6.3 | 0.13 | 40.4 | no edge shown yet |
| rlm_ratio | both | 39-33 | 54.2 | 39.6 | 14.6 | +18.55 | 25.8 | 0.41 | 52.8 | no edge shown yet |
| money_level | both | 243-170 | 58.8 | 58.4 | 0.4 | -27.04 | -6.5 | -0.21 | 38.0 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 200-183 | 52.2 | 49.0 | 3.2 | +7.53 | 2.0 | 0.27 | 44.1 | no edge shown yet |
| money_moving | both | 149-123 | 54.8 | 50.4 | 4.3 | +0.28 | 0.1 | 0.22 | 44.5 | no edge shown yet |
| pin_value | both | 73-69 | 51.4 | 48.8 | 2.6 | -4.11 | -2.9 | 0.1 | 36.6 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 52.0 | -32.0 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 357-413 | 46.4 | 49.6 | -3.2 | -81.78 | -10.6 | 0.43 | 46.4 | DROP: below break-even |
| consensus_gap+money_level | both | 56-45 | 55.4 | 63.1 | -7.6 | -14.91 | -14.8 | -0.02 | 41.6 | no edge shown yet |
| consensus_gap+money_moving | both | 27-28 | 49.1 | 49.6 | -0.5 | -5.45 | -9.9 | 0.52 | 47.3 | no edge shown yet |
| consensus_gap+pin_value | both | 30-31 | 49.2 | 47.2 | 2.0 | -4.8 | -7.9 | 0.27 | 44.3 | no edge shown yet |
| follow_move+rlm_quiet | both | 56-70 | 44.4 | 36.9 | 7.6 | +12.7 | 10.1 | 0.49 | 46.8 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 39-33 | 54.2 | 39.6 | 14.6 | +18.55 | 25.8 | 0.41 | 52.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 99-63 | 61.1 | 49.3 | 11.8 | +22.33 | 13.8 | 0.45 | 47.5 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 87-56 | 60.8 | 57.0 | 3.9 | +0.03 | 0.0 | -0.01 | 46.9 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 15-12 | 55.6 | 50.4 | 5.1 | +1.41 | 5.2 | 0.43 | 44.4 | keep collecting (27/30) |
| money_moving+pin_value | both | 13-8 | 61.9 | 50.7 | 11.2 | +3.52 | 16.7 | 0.41 | 47.6 | keep collecting (21/30) |
| rlm_quiet+rlm_ratio | both | 25-20 | 55.6 | 37.0 | 18.6 | +17.35 | 38.6 | 0.1 | 48.9 | no edge shown yet |
| rlm_quiet+sharp_gap | both | 28-25 | 52.8 | 37.7 | 15.2 | +15.08 | 28.4 | 0.16 | 47.2 | no edge shown yet |
| rlm_ratio+sharp_gap | both | 39-33 | 54.2 | 39.6 | 14.6 | +18.55 | 25.8 | 0.41 | 52.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 136-97 | 58.4 | 55.6 | 2.8 | -6.34 | -2.7 | 0.03 | 42.5 | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | both | 86-75 | 53.4 | 48.0 | 5.4 | +5.33 | 3.3 | 0.42 | 48.4 | no edge shown yet |
| money_delta+money_level | both | 4-5 | 44.4 | 43.0 | 1.4 | -0.63 | -7.0 | 1.39 | 77.8 | keep collecting (9/30) |
| money_delta+money_moving | both | 13-12 | 52.0 | 39.6 | 12.4 | +4.99 | 20.0 | 0.94 | 56.0 | keep collecting (25/30) |
| money_delta+pin_value | both | 4-1 | 80.0 | 49.9 | 30.1 | +2.52 | 50.4 | 0.2 | 40.0 | keep collecting (5/30) |
| money_delta+sharp_gap | both | 11-10 | 52.4 | 38.8 | 13.6 | +5.25 | 25.0 | 1.12 | 66.7 | keep collecting (21/30) |
| pin_value+sharp_gap | both | 15-12 | 55.6 | 50.0 | 5.6 | +1.44 | 5.3 | 0.07 | 40.7 | keep collecting (27/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 50.5 | -50.5 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 50-61 | 45.0 | 53.0 | -8.0 | -23.18 | -20.9 | 0.75 | 55.9 | DROP: below break-even |
| consensus_gap+rlm_quiet | both | 5-8 | 38.5 | 36.4 | 2.1 | -2.39 | -18.4 | 0.97 | 76.9 | keep collecting (13/30) |
| follow_move+pin_value | both | 25-23 | 52.1 | 48.9 | 3.2 | -1.0 | -2.1 | -0.15 | 29.2 | no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 42.8 | -26.2 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 41-60 | 40.6 | 49.5 | -8.9 | -16.69 | -16.5 | 0.51 | 45.5 | DROP: below break-even |
| follow_move+money_level | both | 117-62 | 65.4 | 59.1 | 6.3 | -3.69 | -2.1 | 0.03 | 41.9 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 12-13 | 48.0 | 43.5 | 4.5 | -0.66 | -2.6 | 1.06 | 64.0 | keep collecting (25/30) |
| pin_value+rlm_ratio | both | 3-2 | 60.0 | 45.5 | 14.5 | +0.73 | 14.5 | -1.16 | 40.0 | keep collecting (5/30) |
| follow_move+money_moving | both | 72-47 | 60.5 | 51.2 | 9.3 | +10.93 | 9.2 | 0.42 | 49.6 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 4-0 | 100.0 | 49.3 | 50.7 | +3.52 | 88.0 | 0.25 | 25.0 | keep collecting (4/30) |
| follow_move+money_delta | both | 8-5 | 61.5 | 39.7 | 21.9 | +7.51 | 57.8 | 1.08 | 61.5 | keep collecting (13/30) |
| money_delta+rlm_quiet | both | 4-3 | 57.1 | 34.1 | 23.0 | +5.18 | 74.0 | 0.33 | 42.9 | keep collecting (7/30) |
| money_moving+rlm_quiet | both | 20-20 | 50.0 | 37.3 | 12.7 | +7.85 | 19.6 | 0.59 | 45.0 | no edge shown yet |
| money_moving+rlm_ratio | both | 19-13 | 59.4 | 40.5 | 18.8 | +11.71 | 36.6 | 0.77 | 56.2 | no edge shown yet |
| consensus_gap+rlm_ratio | both | 5-4 | 55.6 | 40.2 | 15.4 | +1.0 | 11.1 | 0.72 | 66.7 | keep collecting (9/30) |
| pin_move+pin_value | both | 5-12 | 29.4 | 49.3 | -19.9 | -7.37 | -43.3 | 0.53 | 35.3 | keep collecting (17/30) |
| follow_move+pin_move | both | 9-11 | 45.0 | 49.2 | -4.2 | -3.39 | -16.9 | 0.52 | 50.0 | keep collecting (20/30) |
| consensus_gap+pin_move | both | 2-6 | 25.0 | 46.9 | -21.9 | -4.14 | -51.7 | 0.29 | 50.0 | keep collecting (8/30) |
| money_level+pin_move | both | 4-6 | 40.0 | 49.9 | -9.9 | -3.02 | -30.2 | 0.14 | 30.0 | keep collecting (10/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 28.5 | -28.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-3 | 25.0 | 39.3 | -14.3 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 28.5 | -28.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 28.5 | -28.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-3 | 25.0 | 39.3 | -14.3 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+sharp_gap | both | 1-4 | 20.0 | 37.1 | -17.1 | -3.07 | -61.5 | -0.3 | 60.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.4 | -51.4 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 49.5 | -49.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-4 | 33.3 | 46.7 | -13.3 | -2.87 | -47.8 | 0.47 | 33.3 | keep collecting (6/30) |
| money_level+pin_rlm | both | 1-2 | 33.3 | 42.8 | -9.5 | -1.07 | -35.8 | 0.67 | 66.7 | keep collecting (3/30) |
| pin_move+pin_rlm | both | 1-1 | 50.0 | 28.5 | 21.5 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| pin_move+rlm_ratio | both | 1-1 | 50.0 | 28.5 | 21.5 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | both | 5-3 | 62.5 | 36.4 | 26.1 | +6.9 | 86.2 | 2.04 | 87.5 | keep collecting (8/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 28.5 | -28.5 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_moving+pin_move | both | 1-1 | 50.0 | 49.5 | 0.5 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+rlm_quiet | both | 0-1 | 0.0 | 49.5 | -49.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 31-45 | 40.8 | 28.5 | 12.3 | +15.0 | 19.7 | 0.39 | 44.7 | DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.3 | 10.7 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 22-23 | 48.9 | 49.6 | -0.7 | -2.96 | -6.6 | 0.8 | 55.6 | no edge shown yet |
| pin_move | moneyline | 3-5 | 37.5 | 50.0 | -12.5 | -3.35 | -41.9 | 0.3 | 50.0 | keep collecting (8/30) |
| pin_move | spread | 2-10 | 16.7 | 48.9 | -32.2 | -8.15 | -67.9 | 0.17 | 25.0 | keep collecting (12/30) |
| pin_move | total | 9-10 | 47.4 | 50.0 | -2.6 | -1.69 | -8.9 | 0.58 | 52.6 | keep collecting (19/30) |
| money_delta | moneyline | 4-8 | 33.3 | 28.5 | 4.8 | +0.99 | 8.2 | 0.62 | 66.7 | keep collecting (12/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 9-3 | 75.0 | 49.7 | 25.3 | +5.08 | 42.3 | 1.25 | 41.7 | keep collecting (12/30) |
| pin_rlm | moneyline | 1-4 | 20.0 | 37.1 | -17.1 | -3.07 | -61.5 | -0.3 | 60.0 | keep collecting (5/30) |
| follow_move | moneyline | 292-214 | 57.7 | 52.5 | 5.2 | -25.53 | -5.0 | 0.02 | 41.9 | PROMOTE: beats break-even and its own base rate |
| follow_move | spread | 179-207 | 46.4 | 49.8 | -3.5 | -41.87 | -10.8 | 0.02 | 32.4 | DROP: below break-even |
| follow_move | total | 235-233 | 50.2 | 50.0 | 0.2 | -18.36 | -3.9 | 0.34 | 45.5 | no edge shown yet |
| rlm_ratio | moneyline | 17-20 | 45.9 | 29.7 | 16.2 | +11.27 | 30.4 | 0.18 | 51.4 | no edge shown yet |
| rlm_ratio | spread | 3-3 | 50.0 | 52.2 | -2.2 | -0.16 | -2.7 | 0.33 | 16.7 | keep collecting (6/30) |
| rlm_ratio | total | 19-10 | 65.5 | 49.6 | 16.0 | +7.44 | 25.7 | 0.72 | 62.1 | keep collecting (29/30) |
| money_level | moneyline | 133-70 | 65.5 | 67.0 | -1.5 | -26.8 | -13.2 | -0.33 | 41.4 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 18-18 | 50.0 | 48.9 | 1.1 | -1.75 | -4.8 | 0.94 | 50.0 | no edge shown yet |
| money_level | total | 92-82 | 52.9 | 50.3 | 2.6 | +1.51 | 0.9 | -0.32 | 31.6 | no edge shown yet |
| sharp_gap | moneyline | 85-96 | 47.0 | 48.0 | -1.0 | -9.89 | -5.5 | 0.21 | 49.2 | no edge shown yet |
| sharp_gap | spread | 20-16 | 55.6 | 49.8 | 5.7 | +2.0 | 5.6 | 0.78 | 41.7 | no edge shown yet |
| sharp_gap | total | 95-71 | 57.2 | 49.9 | 7.3 | +15.41 | 9.3 | 0.22 | 39.2 | no edge shown yet |
| money_moving | moneyline | 63-62 | 50.4 | 51.2 | -0.8 | -16.8 | -13.4 | 0.2 | 51.2 | no edge shown yet |
| money_moving | spread | 18-7 | 72.0 | 49.1 | 22.9 | +9.18 | 36.7 | 0.52 | 48.0 | keep collecting (25/30) |
| money_moving | total | 68-54 | 55.7 | 50.0 | 5.8 | +7.91 | 6.5 | 0.18 | 36.9 | no edge shown yet |
| pin_value | moneyline | 2-7 | 22.2 | 38.1 | -15.9 | -5.31 | -59.0 | 0.12 | 55.6 | keep collecting (9/30) |
| pin_value | spread | 36-31 | 53.7 | 49.1 | 4.7 | +0.57 | 0.8 | 0.21 | 34.3 | no edge shown yet |
| pin_value | total | 35-31 | 53.0 | 50.0 | 3.0 | +0.63 | 1.0 | -0.02 | 36.4 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 53.3 | -19.9 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 157-223 | 41.3 | 49.7 | -8.3 | -69.03 | -18.2 | 0.23 | 44.5 | DROP: below break-even |
| consensus_gap | spread | 94-79 | 54.3 | 48.8 | 5.6 | +2.93 | 1.7 | 0.31 | 38.2 | no edge shown yet |
| consensus_gap | total | 106-111 | 48.8 | 50.0 | -1.2 | -15.68 | -7.2 | 0.87 | 56.2 | no edge shown yet |
| money_level+sharp_gap | moneyline | 63-40 | 61.2 | 62.7 | -1.5 | -15.52 | -15.1 | -0.15 | 48.5 | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+follow_move | moneyline | 23-29 | 44.2 | 57.4 | -13.2 | -15.31 | -29.4 | 0.17 | 50.0 | no edge shown yet |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 33.9 | -8.9 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| consensus_gap+rlm_quiet | moneyline | 2-6 | 25.0 | 28.5 | -3.5 | -3.08 | -38.5 | 1.07 | 87.5 | keep collecting (8/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.8 | -9.5 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 31-45 | 40.8 | 28.5 | 12.3 | +15.0 | 19.7 | 0.39 | 44.7 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 38-21 | 64.4 | 67.1 | -2.7 | -9.64 | -16.3 | -0.19 | 52.5 | beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 28.5 | -28.5 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 27-46 | 37.0 | 49.7 | -12.7 | -15.11 | -20.7 | 0.5 | 46.6 | DROP: below break-even |
| follow_move+money_level | moneyline | 72-23 | 75.8 | 67.4 | 8.4 | -5.65 | -6.0 | -0.29 | 40.0 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 38-20 | 65.5 | 53.0 | 12.6 | +6.83 | 11.8 | 0.2 | 50.0 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 42-33 | 56.0 | 68.0 | -12.0 | -15.26 | -20.3 | -0.21 | 41.3 | no edge shown yet |
| follow_move+sharp_gap | moneyline | 45-29 | 60.8 | 48.8 | 12.0 | +7.15 | 9.7 | 0.24 | 48.6 | no edge shown yet |
| money_moving+sharp_gap | moneyline | 29-41 | 41.4 | 45.7 | -4.3 | -12.48 | -17.8 | 0.5 | 60.0 | DROP: below break-even |
| consensus_gap+money_moving | moneyline | 15-25 | 37.5 | 50.0 | -12.5 | -13.06 | -32.7 | 0.59 | 50.0 | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 17-20 | 45.9 | 29.7 | 16.2 | +11.27 | 30.4 | 0.18 | 51.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 13-14 | 48.1 | 28.5 | 19.6 | +12.4 | 45.9 | -0.1 | 44.4 | keep collecting (27/30) |
| rlm_quiet+sharp_gap | moneyline | 13-17 | 43.3 | 28.5 | 14.8 | +9.4 | 31.3 | -0.22 | 43.3 | no edge shown yet |
| rlm_ratio+sharp_gap | moneyline | 17-20 | 45.9 | 29.7 | 16.2 | +11.27 | 30.4 | 0.18 | 51.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 28.5 | -3.5 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 10-13 | 43.5 | 28.5 | 14.9 | +5.84 | 25.4 | 0.85 | 52.2 | keep collecting (23/30) |
| money_moving+rlm_ratio | moneyline | 7-7 | 50.0 | 28.5 | 21.5 | +6.63 | 47.4 | 0.82 | 57.1 | keep collecting (14/30) |
| money_delta+money_moving | moneyline | 4-8 | 33.3 | 28.5 | 4.8 | +0.99 | 8.2 | 0.62 | 66.7 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 4-7 | 36.4 | 28.5 | 7.8 | +1.99 | 18.1 | 0.68 | 72.7 | keep collecting (11/30) |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 42.8 | -42.8 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-2 | 50.0 | 50.0 | 0.0 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| money_level+pin_move | moneyline | 2-2 | 50.0 | 50.0 | 0.0 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 28.5 | -28.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-3 | 25.0 | 39.3 | -14.3 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 28.5 | -28.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 28.5 | -28.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-3 | 25.0 | 39.3 | -14.3 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+sharp_gap | moneyline | 1-4 | 20.0 | 37.1 | -17.1 | -3.07 | -61.5 | -0.3 | 60.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 28.5 | -28.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | -1.55 | 50.0 | keep collecting (2/30) |
| pin_move+sharp_gap | moneyline | 2-1 | 66.7 | 42.8 | 23.8 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+rlm_ratio | moneyline | 4-6 | 40.0 | 32.8 | 7.2 | -1.13 | -11.3 | 0.95 | 70.0 | keep collecting (10/30) |
| money_level+pin_rlm | moneyline | 1-2 | 33.3 | 42.8 | -9.5 | -1.07 | -35.8 | 0.67 | 66.7 | keep collecting (3/30) |
| pin_move+pin_rlm | moneyline | 1-1 | 50.0 | 28.5 | 21.5 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| pin_move+rlm_ratio | moneyline | 1-1 | 50.0 | 28.5 | 21.5 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| follow_move+money_delta | moneyline | 4-2 | 66.7 | 28.5 | 38.1 | +6.99 | 116.5 | 1.02 | 66.7 | keep collecting (6/30) |
| money_delta+rlm_quiet | moneyline | 3-2 | 60.0 | 28.5 | 31.5 | +5.35 | 107.0 | 0.46 | 60.0 | keep collecting (5/30) |
| money_delta+rlm_ratio | moneyline | 4-1 | 80.0 | 28.5 | 51.5 | +7.99 | 159.8 | 2.26 | 80.0 | keep collecting (5/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 28.5 | -28.5 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-2 | 33.3 | 28.5 | 4.8 | -0.36 | -12.0 | 2.5 | 100.0 | keep collecting (3/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 71.5 | -71.5 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 71.5 | -71.5 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 46.7 | -1.3 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 46.7 | 36.6 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 15-9 | 62.5 | 48.1 | 14.4 | +3.84 | 16.0 | 0.29 | 37.5 | keep collecting (24/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.3 | 10.7 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-3 | 50.0 | 52.2 | -2.2 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-7 | 58.8 | 48.7 | 10.2 | +2.09 | 12.3 | 0.88 | 41.2 | keep collecting (17/30) |
| money_level+money_moving | spread | 10-6 | 62.5 | 48.4 | 14.1 | +3.12 | 19.5 | 1.19 | 68.8 | keep collecting (16/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.6 | -5.7 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 4-3 | 57.1 | 49.5 | 7.6 | +0.41 | 5.8 | 0.57 | 57.1 | keep collecting (7/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 3-3 | 50.0 | 52.2 | -2.2 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 53.3 | -53.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 53.3 | -53.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-12 | 53.8 | 49.0 | 4.8 | +0.62 | 2.4 | 1.15 | 46.2 | keep collecting (26/30) |
| money_moving+sharp_gap | spread | 10-5 | 66.7 | 49.3 | 17.3 | +4.04 | 26.9 | 0.87 | 53.3 | keep collecting (15/30) |
| pin_value+sharp_gap | spread | 2-2 | 50.0 | 50.0 | 0.0 | -0.26 | -6.5 | 0.75 | 75.0 | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 9-12 | 42.9 | 47.7 | -4.8 | -4.2 | -20.0 | 1.0 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 46.7 | 15.8 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 12-10 | 54.5 | 48.2 | 6.3 | +0.98 | 4.5 | 0.82 | 45.5 | keep collecting (22/30) |
| follow_move+pin_value | spread | 13-9 | 59.1 | 48.5 | 10.6 | +2.36 | 10.7 | 0.18 | 27.3 | keep collecting (22/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 46.7 | 53.3 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 46.7 | 53.3 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 46.7 | 53.3 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-3 | 75.0 | 47.8 | 27.2 | +5.22 | 43.5 | 0.75 | 50.0 | keep collecting (12/30) |
| money_delta+rlm_quiet | spread | 1-0 | 100.0 | 46.7 | 53.3 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 2-0 | 100.0 | 46.7 | 53.3 | +1.74 | 87.1 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 2-2 | 50.0 | 53.3 | -3.3 | -0.07 | -1.7 | 1.25 | 25.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | spread | 2-1 | 66.7 | 51.1 | 15.6 | +0.86 | 28.7 | 1.0 | 33.3 | keep collecting (3/30) |
| pin_move+pin_value | spread | 1-7 | 12.5 | 48.4 | -35.9 | -6.09 | -76.1 | 0.38 | 25.0 | keep collecting (8/30) |
| consensus_gap+pin_move | spread | 0-3 | 0.0 | 48.9 | -48.9 | -3.0 | -100.0 | 0.33 | 33.3 | keep collecting (3/30) |
| follow_move+pin_move | spread | 2-4 | 33.3 | 47.8 | -14.5 | -2.15 | -35.8 | 0.0 | 16.7 | keep collecting (6/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 53.3 | -53.3 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_move | spread | 1-0 | 100.0 | 46.7 | 53.3 | +0.94 | 94.3 | -1.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 22-23 | 48.9 | 49.6 | -0.7 | -2.96 | -6.6 | 0.8 | 55.6 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 39-29 | 57.4 | 50.2 | 7.2 | +6.56 | 9.6 | -0.13 | 36.8 | no edge shown yet |
| money_level+sharp_gap | total | 59-45 | 56.7 | 50.2 | 6.6 | +8.56 | 8.2 | -0.07 | 35.6 | no edge shown yet |
| money_moving+sharp_gap | total | 47-29 | 61.8 | 49.9 | 11.9 | +13.77 | 18.1 | 0.25 | 36.8 | PROMOTE: beats break-even and its own base rate |
| book_lag+pin_move | total | 0-1 | 0.0 | 50.5 | -50.5 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 12-7 | 63.2 | 50.0 | 13.2 | +3.83 | 20.2 | 0.26 | 31.6 | keep collecting (19/30) |
| money_moving+pin_value | total | 9-4 | 69.2 | 49.8 | 19.4 | +4.11 | 31.6 | 0.23 | 38.5 | keep collecting (13/30) |
| pin_value+sharp_gap | total | 13-8 | 61.9 | 50.0 | 11.9 | +3.7 | 17.6 | 0.1 | 33.3 | keep collecting (21/30) |
| follow_move+money_level | total | 33-29 | 53.2 | 50.2 | 3.0 | +0.99 | 1.6 | 0.24 | 43.5 | no edge shown yet |
| follow_move+pin_value | total | 11-12 | 47.8 | 50.0 | -2.2 | -2.08 | -9.0 | -0.3 | 30.4 | keep collecting (23/30) |
| follow_move+rlm_ratio | total | 19-10 | 65.5 | 49.6 | 16.0 | +7.44 | 25.7 | 0.72 | 62.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 44-27 | 62.0 | 49.9 | 12.1 | +13.1 | 18.4 | 0.56 | 47.9 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 6-5 | 54.5 | 49.6 | 5.0 | +0.54 | 4.9 | 1.09 | 72.7 | keep collecting (11/30) |
| pin_value+rlm_ratio | total | 3-1 | 75.0 | 49.7 | 25.3 | +1.73 | 43.2 | -0.25 | 50.0 | keep collecting (4/30) |
| rlm_ratio+sharp_gap | total | 19-10 | 65.5 | 49.6 | 16.0 | +7.44 | 25.7 | 0.72 | 62.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 25-24 | 51.0 | 49.9 | 1.2 | -1.12 | -2.3 | 0.59 | 49.0 | no edge shown yet |
| consensus_gap+money_level | total | 9-6 | 60.0 | 50.3 | 9.7 | +2.03 | 13.5 | -0.4 | 20.0 | keep collecting (15/30) |
| consensus_gap+money_moving | total | 7-2 | 77.8 | 49.9 | 27.8 | +4.3 | 47.7 | 0.0 | 33.3 | keep collecting (9/30) |
| consensus_gap+pin_value | total | 13-16 | 44.8 | 50.1 | -5.3 | -4.34 | -14.9 | 0.34 | 48.3 | keep collecting (29/30) |
| consensus_gap+sharp_gap | total | 9-11 | 45.0 | 49.9 | -4.9 | -2.89 | -14.5 | -0.1 | 30.0 | keep collecting (20/30) |
| money_moving+rlm_ratio | total | 10-5 | 66.7 | 49.6 | 17.0 | +4.22 | 28.1 | 0.67 | 60.0 | keep collecting (15/30) |
| consensus_gap+follow_move | total | 18-20 | 47.4 | 49.9 | -2.6 | -3.67 | -9.7 | 1.39 | 68.4 | no edge shown yet |
| consensus_gap+money_delta | total | 3-0 | 100.0 | 50.2 | 49.8 | +2.69 | 89.6 | 0.33 | 33.3 | keep collecting (3/30) |
| follow_move+money_delta | total | 3-3 | 50.0 | 49.7 | 0.3 | -0.31 | -5.2 | 1.33 | 66.7 | keep collecting (6/30) |
| money_delta+money_moving | total | 8-3 | 72.7 | 49.7 | 23.1 | +4.17 | 37.9 | 1.36 | 45.5 | keep collecting (11/30) |
| money_delta+pin_value | total | 3-0 | 100.0 | 49.8 | 50.2 | +2.69 | 89.6 | 0.0 | 33.3 | keep collecting (3/30) |
| money_delta+sharp_gap | total | 7-2 | 77.8 | 49.7 | 28.1 | +4.26 | 47.4 | 1.67 | 55.6 | keep collecting (9/30) |
| money_moving+rlm_quiet | total | 8-7 | 53.3 | 49.6 | 3.8 | +0.27 | 1.8 | 0.4 | 40.0 | keep collecting (15/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 11-5 | 68.8 | 49.5 | 19.2 | +5.04 | 31.5 | 0.62 | 62.5 | keep collecting (16/30) |
| rlm_quiet+sharp_gap | total | 14-7 | 66.7 | 49.5 | 17.1 | +5.77 | 27.5 | 0.86 | 57.1 | keep collecting (21/30) |
| follow_move+pin_move | total | 5-5 | 50.0 | 49.7 | 0.3 | -0.37 | -3.7 | 1.0 | 70.0 | keep collecting (10/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 49.5 | -49.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 49.5 | -49.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 3-2 | 60.0 | 49.7 | 10.3 | +0.73 | 14.5 | 0.8 | 60.0 | keep collecting (5/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 49.5 | 0.5 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 4-1 | 80.0 | 49.5 | 30.5 | +2.68 | 53.6 | 0.4 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | total | 1-4 | 20.0 | 50.5 | -30.5 | -3.09 | -61.8 | 0.4 | 20.0 | keep collecting (5/30) |
| pin_move+pin_value | total | 4-5 | 44.4 | 50.2 | -5.7 | -1.28 | -14.2 | 0.67 | 44.4 | keep collecting (9/30) |
| pin_move+sharp_gap | total | 0-3 | 0.0 | 50.5 | -50.5 | -3.0 | -100.0 | 1.0 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 49.5 | -49.5 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 1-2 | 33.3 | 49.5 | -16.2 | -1.09 | -36.4 | 1.67 | 100.0 | keep collecting (3/30) |
| consensus_gap+pin_move | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | 0.5 | 50.0 | keep collecting (2/30) |
| money_moving+pin_move | total | 1-1 | 50.0 | 49.5 | 0.5 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+rlm_quiet | total | 0-1 | 0.0 | 49.5 | -49.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 293-433 | 40.4 | 42.1 | -1.7 | -77.19 | -10.6 |  |  | DROP: below break-even |
| pin_move | both | 701-717 | 49.4 | 49.7 | -0.2 | -52.12 | -3.7 |  |  | DROP: below break-even |
| money_delta | both | 416-551 | 43.0 | 44.2 | -1.2 | -81.73 | -8.5 |  |  | DROP: below break-even |
| pin_rlm | both | 182-224 | 44.8 | 42.1 | 2.7 | +10.95 | 2.7 |  |  | DROP: below break-even |
| follow_move | both | 1185-1128 | 51.2 | 50.9 | 0.4 | -156.31 | -6.8 |  |  | no edge shown yet |
| rlm_ratio | both | 271-342 | 44.2 | 43.7 | 0.5 | -38.77 | -6.3 |  |  | DROP: below break-even |
| money_level | both | 1506-1132 | 57.1 | 55.3 | 1.8 | -98.14 | -3.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 1169-1358 | 46.3 | 47.7 | -1.4 | -207.67 | -8.2 |  |  | DROP: below break-even |
| money_moving | both | 1183-1349 | 46.7 | 48.0 | -1.3 | -199.77 | -7.9 |  |  | DROP: below break-even |
| pin_value | both | 511-513 | 49.9 | 48.4 | 1.5 | +5.39 | 0.5 |  |  | DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 51.1 | 15.6 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 468-556 | 45.7 | 48.8 | -3.1 | -84.69 | -8.3 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 165-163 | 50.3 | 51.1 | -0.8 | -21.86 | -6.7 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 194-297 | 39.5 | 46.0 | -6.5 | -45.63 | -9.3 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 119-108 | 52.4 | 50.6 | 1.8 | +16.94 | 7.5 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 30-47 | 39.0 | 38.9 | 0.1 | +10.61 | 13.8 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 180-188 | 48.9 | 46.5 | 2.4 | +8.3 | 2.3 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | both | 34-55 | 38.2 | 40.2 | -2.0 | -3.58 | -4.0 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 193-305 | 38.8 | 45.5 | -6.8 | -50.47 | -10.1 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 628-688 | 47.7 | 48.9 | -1.2 | -115.39 | -8.8 |  |  | DROP: below break-even |
| follow_move+pin_move | both | 497-529 | 48.4 | 49.7 | -1.2 | -73.87 | -7.2 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 143-169 | 45.8 | 43.4 | 2.4 | -10.83 | -3.5 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 176-168 | 51.2 | 49.2 | 2.0 | -1.26 | -0.4 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 271-342 | 44.2 | 43.7 | 0.5 | -38.77 | -6.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 629-688 | 47.8 | 48.7 | -0.9 | -107.99 | -8.2 |  |  | DROP: below break-even |
| money_moving+pin_move | both | 398-439 | 47.6 | 48.5 | -0.9 | -43.83 | -5.2 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 176-214 | 45.1 | 42.2 | 2.9 | +14.99 | 3.8 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 217-258 | 45.7 | 47.8 | -2.1 | -30.35 | -6.4 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 261-329 | 44.2 | 43.8 | 0.5 | -36.32 | -6.2 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 1126-1299 | 46.4 | 47.8 | -1.3 | -184.19 | -7.6 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 168-188 | 47.2 | 43.8 | 3.4 | +10.09 | 2.8 |  |  | DROP: below break-even |
| pin_move+pin_value | both | 220-223 | 49.7 | 49.5 | 0.2 | -15.67 | -3.5 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 151-164 | 47.9 | 44.9 | 3.1 | -0.62 | -0.2 |  |  | DROP: below break-even |
| pin_move+sharp_gap | both | 400-446 | 47.3 | 48.3 | -1.0 | -47.71 | -5.6 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 48-51 | 48.5 | 46.4 | 2.0 | +10.26 | 10.4 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 143-169 | 45.8 | 43.4 | 2.4 | -10.83 | -3.5 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 182-224 | 44.8 | 42.1 | 2.7 | +10.95 | 2.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 45-40 | 52.9 | 48.5 | 4.4 | +1.43 | 1.7 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 218-263 | 45.3 | 47.9 | -2.6 | -34.46 | -7.2 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 271-342 | 44.2 | 43.7 | 0.5 | -38.77 | -6.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 203-260 | 43.8 | 45.3 | -1.5 | -54.36 | -11.7 |  |  | DROP: below break-even |
| money_level+money_moving | both | 825-739 | 52.7 | 52.3 | 0.4 | -75.18 | -4.8 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 804-731 | 52.4 | 52.1 | 0.2 | -74.68 | -4.9 |  |  | no edge shown yet |
| follow_move+money_level | both | 724-532 | 57.6 | 55.9 | 1.7 | -63.97 | -5.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 122-106 | 53.5 | 47.8 | 5.7 | +10.85 | 4.8 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 294-220 | 57.2 | 58.1 | -0.9 | -23.59 | -4.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_move | both | 386-355 | 52.1 | 53.1 | -1.0 | -41.63 | -5.6 |  |  | no edge shown yet |
| money_level+pin_value | both | 243-231 | 51.3 | 49.9 | 1.3 | -19.3 | -4.1 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 28-64 | 30.4 | 37.5 | -7.0 | -15.79 | -17.2 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | both | 293-433 | 40.4 | 42.1 | -1.7 | -77.19 | -10.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 149-244 | 37.9 | 41.6 | -3.7 | -57.46 | -14.6 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 301-430 | 41.2 | 42.7 | -1.5 | -66.79 | -9.1 |  |  | DROP: below break-even |
| consensus_gap+money_delta | both | 55-119 | 31.6 | 38.3 | -6.7 | -23.78 | -13.7 |  |  | DROP: below break-even |
| money_delta+money_level | both | 143-138 | 50.9 | 47.1 | 3.7 | +10.03 | 3.6 |  |  | no edge shown yet |
| money_delta+pin_value | both | 89-83 | 51.7 | 47.5 | 4.3 | +5.45 | 3.2 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 298-424 | 41.3 | 42.6 | -1.4 | -63.96 | -8.9 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 115-206 | 35.8 | 40.2 | -4.3 | -51.85 | -16.2 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | both | 141-239 | 37.1 | 41.5 | -4.4 | -58.46 | -15.4 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 78-144 | 35.1 | 42.3 | -7.2 | -56.86 | -25.6 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | both | 142-188 | 43.0 | 43.7 | -0.6 | -23.59 | -7.1 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 61-105 | 36.7 | 40.1 | -3.4 | -27.29 | -16.4 |  |  | DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 51.1 | 15.6 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 150-180 | 45.5 | 46.1 | -0.6 | -19.99 | -6.1 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 76-59 | 56.3 | 46.7 | 9.6 | +15.58 | 11.5 |  |  | no edge shown yet |
| money_delta+pin_rlm | both | 104-128 | 44.8 | 42.2 | 2.6 | +0.71 | 0.3 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | both | 145-180 | 44.6 | 43.9 | 0.7 | -27.59 | -8.5 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | both | 38-52 | 42.2 | 47.5 | -5.2 | -6.7 | -7.4 |  |  | DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 49.5 | 50.5 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 93-190 | 32.9 | 29.3 | 3.6 | -19.04 | -6.7 |  |  | DROP: below break-even |
| rlm_quiet | spread | 67-72 | 48.2 | 51.4 | -3.2 | -9.64 | -6.9 |  |  | no edge shown yet |
| rlm_quiet | total | 133-171 | 43.8 | 49.7 | -5.9 | -48.51 | -16.0 |  |  | DROP: below break-even |
| pin_move | moneyline | 163-156 | 51.1 | 47.9 | 3.2 | +18.24 | 5.7 |  |  | no edge shown yet |
| pin_move | spread | 263-281 | 48.3 | 50.4 | -2.1 | -41.67 | -7.7 |  |  | DROP: below break-even |
| pin_move | total | 275-280 | 49.5 | 49.9 | -0.3 | -28.7 | -5.2 |  |  | no edge shown yet |
| money_delta | moneyline | 76-218 | 25.9 | 30.4 | -4.6 | -59.7 | -20.3 |  |  | DROP: below break-even |
| money_delta | spread | 141-144 | 49.5 | 51.1 | -1.6 | -15.45 | -5.4 |  |  | no edge shown yet |
| money_delta | total | 199-189 | 51.3 | 49.7 | 1.6 | -6.58 | -1.7 |  |  | no edge shown yet |
| pin_rlm | moneyline | 54-107 | 33.5 | 30.1 | 3.4 | +10.85 | 6.7 |  |  | DROP: below break-even |
| pin_rlm | spread | 30-26 | 53.6 | 51.3 | 2.3 | +1.3 | 2.3 |  |  | no edge shown yet |
| pin_rlm | total | 98-91 | 51.9 | 49.7 | 2.2 | -1.2 | -0.6 |  |  | no edge shown yet |
| follow_move | moneyline | 429-332 | 56.4 | 53.0 | 3.4 | -49.99 | -6.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 340-361 | 48.5 | 49.7 | -1.2 | -51.45 | -7.3 |  |  | DROP: below break-even |
| follow_move | total | 416-435 | 48.9 | 49.9 | -1.1 | -54.87 | -6.4 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 61-138 | 30.7 | 30.7 | -0.0 | -26.58 | -13.4 |  |  | DROP: below break-even |
| rlm_ratio | spread | 53-52 | 50.5 | 50.5 | 0.0 | -4.04 | -3.8 |  |  | no edge shown yet |
| rlm_ratio | total | 157-152 | 50.8 | 49.7 | 1.1 | -8.15 | -2.6 |  |  | no edge shown yet |
| money_level | moneyline | 586-251 | 70.0 | 67.5 | 2.5 | -48.65 | -5.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 420-425 | 49.7 | 49.0 | 0.7 | -46.74 | -5.5 |  |  | DROP: below break-even |
| money_level | total | 500-456 | 52.3 | 50.2 | 2.1 | -2.74 | -0.3 |  |  | no edge shown yet |
| sharp_gap | moneyline | 299-464 | 39.2 | 43.1 | -3.9 | -102.88 | -13.5 |  |  | DROP: below break-even |
| sharp_gap | spread | 427-411 | 51.0 | 49.5 | 1.5 | -26.02 | -3.1 |  |  | no edge shown yet |
| sharp_gap | total | 443-483 | 47.8 | 49.9 | -2.1 | -78.77 | -8.5 |  |  | DROP: below break-even |
| money_moving | moneyline | 316-443 | 41.6 | 44.1 | -2.5 | -79.94 | -10.5 |  |  | DROP: below break-even |
| money_moving | spread | 424-414 | 50.6 | 49.4 | 1.1 | -31.89 | -3.8 |  |  | no edge shown yet |
| money_moving | total | 443-492 | 47.4 | 49.9 | -2.6 | -87.95 | -9.4 |  |  | DROP: below break-even |
| pin_value | moneyline | 26-68 | 27.7 | 34.5 | -6.8 | +20.62 | 21.9 |  |  | DROP: below break-even |
| pin_value | spread | 233-212 | 52.4 | 49.5 | 2.8 | -9.1 | -2.0 |  |  | no edge shown yet |
| pin_value | total | 252-233 | 52.0 | 50.1 | 1.9 | -6.14 | -1.3 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 53.3 | 46.7 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 212-328 | 39.3 | 47.9 | -8.7 | -80.55 | -14.9 |  |  | DROP: below break-even |
| consensus_gap | spread | 114-96 | 54.3 | 49.0 | 5.3 | +1.63 | 0.8 |  |  | no edge shown yet |
| consensus_gap | total | 142-132 | 51.8 | 50.3 | 1.6 | -5.77 | -2.1 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 214-131 | 62.0 | 62.4 | -0.4 | -19.6 | -5.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 197-132 | 59.9 | 61.8 | -1.9 | -24.62 | -7.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 280-424 | 39.8 | 43.0 | -3.3 | -76.34 | -10.8 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 73-86 | 45.9 | 52.8 | -6.9 | -25.25 | -15.9 |  |  | DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 10-48 | 17.2 | 30.0 | -12.8 | -15.86 | -27.3 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 93-190 | 32.9 | 29.3 | 3.6 | -19.04 | -6.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 151-90 | 62.7 | 67.9 | -5.2 | -18.33 | -7.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 77-181 | 29.8 | 42.8 | -13.0 | -31.7 | -12.3 |  |  | !! CHECK: consensus_gap+money_moving close moneyline all sits -13.0 pts from its base (42.8%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+money_level | moneyline | 311-120 | 72.2 | 68.2 | 4.0 | -26.57 | -6.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+money_moving | moneyline | 160-184 | 46.5 | 46.8 | -0.2 | -36.84 | -10.7 |  |  | DROP: below break-even |
| money_delta+money_moving | moneyline | 71-197 | 26.5 | 30.0 | -3.5 | -43.4 | -16.2 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 69-196 | 26.0 | 30.0 | -4.0 | -44.59 | -16.8 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 75-189 | 28.4 | 41.9 | -13.5 | -37.44 | -14.2 |  |  | !! CHECK: consensus_gap+sharp_gap close moneyline all sits -13.5 pts from its base (41.9%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+sharp_gap | moneyline | 152-186 | 45.0 | 45.8 | -0.8 | -39.87 | -11.8 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | moneyline | 43-113 | 27.6 | 29.1 | -1.5 | -22.39 | -14.4 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 44-115 | 27.7 | 29.1 | -1.4 | -24.79 | -15.6 |  |  | DROP: below break-even |
| consensus_gap+pin_move | moneyline | 49-41 | 54.4 | 51.9 | 2.5 | +22.74 | 25.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 14-32 | 30.4 | 31.3 | -0.9 | +11.53 | 25.1 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 7-38 | 15.6 | 30.4 | -14.9 | -10.26 | -22.8 |  |  | DROP: below break-even |
| follow_move+pin_move | moneyline | 127-116 | 52.3 | 48.7 | 3.6 | +1.25 | 0.5 |  |  | no edge shown yet |
| follow_move+pin_rlm | moneyline | 37-68 | 35.2 | 30.6 | 4.7 | -7.12 | -6.8 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 61-138 | 30.7 | 30.7 | -0.0 | -26.58 | -13.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 70-90 | 43.8 | 42.5 | 1.3 | +7.04 | 4.4 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 53-100 | 34.6 | 30.2 | 4.4 | +16.45 | 10.8 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 59-130 | 31.2 | 30.8 | 0.4 | -21.7 | -11.5 |  |  | DROP: below break-even |
| pin_move+pin_rlm | moneyline | 40-71 | 36.0 | 30.1 | 6.0 | +9.99 | 9.0 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 44-64 | 40.7 | 29.7 | 11.0 | +9.7 | 9.0 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 31-54 | 36.5 | 31.1 | 5.4 | -0.38 | -0.5 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 68-96 | 41.5 | 41.6 | -0.2 | +0.47 | 0.3 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 24-56 | 30.0 | 29.6 | 0.4 | -12.26 | -15.3 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 37-68 | 35.2 | 30.6 | 4.7 | -7.12 | -6.8 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 54-107 | 33.5 | 30.1 | 3.4 | +10.85 | 6.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 40-110 | 26.7 | 29.1 | -2.4 | -24.63 | -16.4 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 61-138 | 30.7 | 30.7 | -0.0 | -26.58 | -13.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 16-88 | 15.4 | 30.2 | -14.8 | -26.79 | -25.8 |  |  | DROP: below break-even |
| consensus_gap+pin_value | moneyline | 17-52 | 24.6 | 32.9 | -8.3 | +2.23 | 3.2 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 25-48 | 34.2 | 31.5 | 2.8 | -2.3 | -3.2 |  |  | DROP: below break-even |
| money_delta+pin_rlm | moneyline | 31-61 | 33.7 | 30.4 | 3.3 | +0.91 | 1.0 |  |  | DROP: below break-even |
| money_delta+pin_value | moneyline | 4-18 | 18.2 | 28.5 | -10.4 | -5.3 | -24.1 |  |  | keep collecting (22/30) |
| money_moving+pin_value | moneyline | 13-37 | 26.0 | 32.8 | -6.8 | +10.89 | 21.8 |  |  | DROP: below break-even |
| pin_move+pin_value | moneyline | 9-13 | 40.9 | 40.2 | 0.7 | +6.3 | 28.6 |  |  | keep collecting (22/30) |
| pin_rlm+pin_value | moneyline | 6-11 | 35.3 | 28.5 | 6.8 | +12.45 | 73.2 |  |  | keep collecting (17/30) |
| pin_value+sharp_gap | moneyline | 13-41 | 24.1 | 34.1 | -10.0 | +6.89 | 12.8 |  |  | DROP: below break-even |
| follow_move+money_delta | moneyline | 38-83 | 31.4 | 32.4 | -1.0 | -27.98 | -23.1 |  |  | DROP: below break-even |
| money_delta+money_level | moneyline | 21-28 | 42.9 | 34.7 | 8.2 | +9.22 | 18.8 |  |  | no edge shown yet |
| money_delta+rlm_ratio | moneyline | 32-72 | 30.8 | 31.4 | -0.7 | -22.47 | -21.6 |  |  | DROP: below break-even |
| money_level+pin_move | moneyline | 95-59 | 61.7 | 65.6 | -3.9 | -9.05 | -5.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 14-14 | 50.0 | 34.7 | 15.3 | +3.97 | 14.2 |  |  | keep collecting (28/30) |
| money_level+rlm_ratio | moneyline | 17-21 | 44.7 | 37.6 | 7.2 | +0.43 | 1.1 |  |  | no edge shown yet |
| money_delta+rlm_quiet | moneyline | 24-63 | 27.6 | 30.0 | -2.4 | -25.64 | -29.5 |  |  | DROP: below break-even |
| money_level+pin_value | moneyline | 6-8 | 42.9 | 65.3 | -22.5 | -4.75 | -33.9 |  |  | keep collecting (14/30) |
| follow_move+pin_value | moneyline | 5-10 | 33.3 | 40.0 | -6.7 | +4.75 | 31.7 |  |  | keep collecting (15/30) |
| pin_value+rlm_quiet | moneyline | 3-7 | 30.0 | 28.5 | 1.5 | +6.5 | 65.0 |  |  | keep collecting (10/30) |
| pin_value+rlm_ratio | moneyline | 2-3 | 40.0 | 28.5 | 11.5 | -0.1 | -2.0 |  |  | keep collecting (5/30) |
| consensus_gap+follow_move | spread | 40-32 | 55.6 | 48.3 | 7.3 | +2.22 | 3.1 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 55-51 | 51.9 | 48.8 | 3.1 | -4.05 | -3.8 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 33-38 | 46.5 | 49.3 | -2.8 | -9.7 | -13.7 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 5-4 | 55.6 | 50.4 | 5.2 | +0.3 | 3.3 |  |  | keep collecting (9/30) |
| consensus_gap+pin_value | spread | 81-60 | 57.4 | 49.0 | 8.4 | +9.27 | 6.6 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 7-4 | 63.6 | 50.3 | 13.3 | +1.92 | 17.5 |  |  | keep collecting (11/30) |
| consensus_gap+sharp_gap | spread | 54-51 | 51.4 | 49.0 | 2.5 | -4.95 | -4.7 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 198-199 | 49.9 | 49.3 | 0.6 | -19.9 | -5.0 |  |  | no edge shown yet |
| follow_move+pin_move | spread | 164-189 | 46.5 | 50.1 | -3.7 | -39.55 | -11.2 |  |  | DROP: below break-even |
| follow_move+pin_rlm | spread | 21-21 | 50.0 | 50.8 | -0.8 | -1.83 | -4.4 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 75-67 | 52.8 | 49.0 | 3.8 | -1.61 | -1.1 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 53-52 | 50.5 | 50.5 | 0.0 | -4.04 | -3.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 199-198 | 50.1 | 49.3 | 0.8 | -17.76 | -4.5 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 148-156 | 48.7 | 49.9 | -1.2 | -22.28 | -7.3 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 28-26 | 51.9 | 51.2 | 0.6 | -0.53 | -1.0 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 106-112 | 48.6 | 49.1 | -0.5 | -20.52 | -9.4 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 51-51 | 50.0 | 50.4 | -0.4 | -4.97 | -4.9 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 419-406 | 50.8 | 49.5 | 1.3 | -28.39 | -3.4 |  |  | no edge shown yet |
| pin_move+pin_rlm | spread | 30-26 | 53.6 | 51.3 | 2.3 | +1.3 | 2.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 104-107 | 49.3 | 50.0 | -0.7 | -15.54 | -7.4 |  |  | no edge shown yet |
| pin_move+rlm_ratio | spread | 27-28 | 49.1 | 50.8 | -1.7 | -3.52 | -6.4 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 151-156 | 49.2 | 49.9 | -0.7 | -19.55 | -6.4 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 10-11 | 47.6 | 51.4 | -3.8 | -2.19 | -10.4 |  |  | keep collecting (21/30) |
| pin_rlm+rlm_ratio | spread | 21-21 | 50.0 | 50.8 | -0.8 | -1.83 | -4.4 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 30-26 | 53.6 | 51.3 | 2.3 | +1.3 | 2.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 8-8 | 50.0 | 49.6 | 0.4 | -1.17 | -7.3 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | spread | 106-112 | 48.6 | 49.2 | -0.6 | -20.58 | -9.4 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 53-52 | 50.5 | 50.5 | 0.0 | -4.04 | -3.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 186-195 | 48.8 | 48.9 | -0.0 | -26.83 | -7.0 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 31-30 | 50.8 | 50.1 | 0.8 | -2.19 | -3.6 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 326-317 | 50.7 | 49.0 | 1.7 | -23.7 | -3.7 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 66-58 | 53.2 | 48.4 | 4.9 | -1.52 | -1.2 |  |  | no edge shown yet |
| money_level+money_moving | spread | 325-318 | 50.5 | 49.0 | 1.6 | -25.62 | -4.0 |  |  | no edge shown yet |
| money_level+pin_move | spread | 131-152 | 46.3 | 49.5 | -3.2 | -34.13 | -12.1 |  |  | DROP: below break-even |
| money_level+pin_value | spread | 113-115 | 49.6 | 48.7 | 0.9 | -17.6 | -7.7 |  |  | no edge shown yet |
| consensus_gap+money_delta | spread | 17-15 | 53.1 | 51.0 | 2.1 | -0.46 | -1.4 |  |  | no edge shown yet |
| follow_move+money_delta | spread | 46-55 | 45.5 | 50.4 | -4.9 | -13.4 | -13.3 |  |  | no edge shown yet |
| money_delta+money_level | spread | 47-46 | 50.5 | 49.8 | 0.7 | -3.69 | -4.0 |  |  | no edge shown yet |
| money_delta+money_moving | spread | 81-87 | 48.2 | 50.5 | -2.3 | -13.88 | -8.3 |  |  | no edge shown yet |
| money_delta+pin_value | spread | 38-30 | 55.9 | 50.9 | 5.0 | +3.19 | 4.7 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 80-85 | 48.5 | 50.5 | -2.0 | -12.86 | -7.8 |  |  | no edge shown yet |
| follow_move+rlm_quiet | spread | 67-72 | 48.2 | 51.4 | -3.2 | -9.64 | -6.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 15-8 | 65.2 | 51.6 | 13.7 | +5.65 | 24.5 |  |  | keep collecting (23/30) |
| rlm_quiet+sharp_gap | spread | 29-18 | 61.7 | 51.9 | 9.8 | +8.6 | 18.3 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 16-13 | 55.2 | 50.3 | 4.8 | +1.39 | 4.8 |  |  | keep collecting (29/30) |
| money_delta+pin_move | spread | 43-49 | 46.7 | 51.3 | -4.6 | -9.9 | -10.8 |  |  | no edge shown yet |
| money_delta+rlm_ratio | spread | 19-30 | 38.8 | 50.1 | -11.3 | -13.18 | -26.9 |  |  | DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 53.3 | 46.7 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_rlm | spread | 16-18 | 47.1 | 51.1 | -4.1 | -3.61 | -10.6 |  |  | no edge shown yet |
| money_delta+rlm_quiet | spread | 18-21 | 46.2 | 51.8 | -5.6 | -4.29 | -11.0 |  |  | no edge shown yet |
| money_moving+rlm_quiet | spread | 28-18 | 60.9 | 51.8 | 9.0 | +7.65 | 16.6 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 38-39 | 49.4 | 51.9 | -2.5 | -3.59 | -4.7 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-3 | 66.7 | 52.5 | 14.1 | +2.56 | 28.4 |  |  | keep collecting (9/30) |
| consensus_gap+rlm_quiet | spread | 4-3 | 57.1 | 51.4 | 5.7 | +0.48 | 6.9 |  |  | keep collecting (7/30) |
| pin_value+rlm_quiet | spread | 7-7 | 50.0 | 50.5 | -0.5 | -0.85 | -6.1 |  |  | keep collecting (14/30) |
| follow_move+money_delta | total | 119-122 | 49.4 | 49.7 | -0.3 | -12.98 | -5.4 |  |  | no edge shown yet |
| money_level+money_moving | total | 286-290 | 49.7 | 50.1 | -0.4 | -29.96 | -5.2 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 281-282 | 49.9 | 50.1 | -0.2 | -26.36 | -4.7 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 427-469 | 47.7 | 49.9 | -2.3 | -79.47 | -8.9 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 77-72 | 51.7 | 50.4 | 1.3 | -3.75 | -2.5 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 37-29 | 56.1 | 50.2 | 5.9 | +3.9 | 5.9 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 82-76 | 51.9 | 50.2 | 1.7 | -3.19 | -2.0 |  |  | no edge shown yet |
| follow_move+money_moving | total | 270-305 | 47.0 | 49.9 | -3.0 | -58.65 | -10.2 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 278-304 | 47.8 | 49.9 | -2.1 | -50.35 | -8.7 |  |  | DROP: below break-even |
| money_level+pin_move | total | 160-144 | 52.6 | 50.0 | 2.6 | +1.54 | 0.5 |  |  | no edge shown yet |
| money_level+pin_value | total | 124-108 | 53.4 | 50.3 | 3.2 | +3.05 | 1.3 |  |  | no edge shown yet |
| pin_move+pin_value | total | 107-103 | 51.0 | 50.0 | 1.0 | -6.42 | -3.1 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 133-171 | 43.8 | 49.7 | -5.9 | -48.51 | -16.0 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 180-193 | 48.3 | 49.9 | -1.6 | -28.6 | -7.7 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | total | 76-111 | 40.6 | 49.6 | -9.0 | -41.27 | -22.1 |  |  | DROP: below break-even |
| money_delta+money_moving | total | 149-146 | 50.5 | 49.7 | 0.8 | -9.51 | -3.2 |  |  | no edge shown yet |
| follow_move+money_level | total | 227-217 | 51.1 | 50.1 | 1.0 | -10.57 | -2.4 |  |  | no edge shown yet |
| follow_move+pin_value | total | 96-91 | 51.3 | 50.0 | 1.3 | -4.4 | -2.4 |  |  | no edge shown yet |
| money_moving+pin_value | total | 98-109 | 47.3 | 50.1 | -2.7 | -20.72 | -10.0 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 99-110 | 47.4 | 50.0 | -2.7 | -20.77 | -9.9 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 62-65 | 48.8 | 50.2 | -1.4 | -9.88 | -7.8 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 64-65 | 49.6 | 50.2 | -0.6 | -8.09 | -6.3 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 52-45 | 53.6 | 50.2 | 3.4 | +1.17 | 1.2 |  |  | no edge shown yet |
| consensus_gap+money_delta | total | 22-16 | 57.9 | 49.9 | 7.9 | +3.47 | 9.1 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | total | 14-13 | 51.9 | 49.8 | 2.0 | -0.42 | -1.6 |  |  | keep collecting (27/30) |
| money_delta+rlm_quiet | total | 36-60 | 37.5 | 49.6 | -12.1 | -26.92 | -28.0 |  |  | DROP: below break-even |
| money_delta+sharp_gap | total | 149-143 | 51.0 | 49.7 | 1.3 | -6.51 | -2.2 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 70-108 | 39.3 | 49.6 | -10.3 | -43.72 | -24.6 |  |  | !! IMPLAUSIBLE: money_moving+rlm_quiet close total all 39.3% on n=178. A -110 market outside 40-60% at this sample is a measurement bug until proven otherwise. Recompute from source.  ||  DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 75-64 | 54.0 | 49.8 | 4.2 | +4.5 | 3.2 |  |  | no edge shown yet |
| money_delta+pin_move | total | 82-83 | 49.7 | 49.6 | 0.1 | -7.79 | -4.7 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 181-194 | 48.3 | 49.9 | -1.6 | -28.64 | -7.6 |  |  | DROP: below break-even |
| follow_move+pin_move | total | 206-224 | 47.9 | 49.9 | -2.0 | -35.57 | -8.3 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | total | 28-38 | 42.4 | 49.7 | -7.3 | -12.35 | -18.7 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | total | 11-11 | 50.0 | 50.0 | 0.0 | -1.22 | -5.5 |  |  | keep collecting (22/30) |
| consensus_gap+rlm_ratio | total | 20-13 | 60.6 | 50.0 | 10.6 | +4.76 | 14.4 |  |  | no edge shown yet |
| follow_move+pin_rlm | total | 85-80 | 51.5 | 49.7 | 1.8 | -1.88 | -1.1 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 157-152 | 50.8 | 49.7 | 1.1 | -8.15 | -2.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 46-32 | 59.0 | 49.7 | 9.3 | +10.22 | 13.1 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 74-55 | 57.4 | 49.8 | 7.6 | +12.61 | 9.8 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 95-88 | 51.9 | 49.7 | 2.3 | -0.94 | -0.5 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 151-148 | 50.5 | 49.7 | 0.8 | -9.64 | -3.2 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 98-91 | 51.9 | 49.7 | 2.2 | -1.2 | -0.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 93-82 | 53.1 | 49.7 | 3.5 | +3.29 | 1.9 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 32-29 | 52.5 | 49.7 | 2.7 | -0.01 | -0.0 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 85-80 | 51.5 | 49.7 | 1.8 | -1.88 | -1.1 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 98-91 | 51.9 | 49.7 | 2.2 | -1.2 | -0.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 35-29 | 54.7 | 49.8 | 4.9 | +2.69 | 4.2 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 157-152 | 50.8 | 49.7 | 1.1 | -8.15 | -2.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 57-49 | 53.8 | 49.6 | 4.2 | +3.41 | 3.2 |  |  | no edge shown yet |
| money_delta+rlm_ratio | total | 94-78 | 54.7 | 49.7 | 5.0 | +8.05 | 4.7 |  |  | no edge shown yet |
| money_delta+pin_value | total | 47-35 | 57.3 | 49.7 | 7.6 | +7.55 | 9.2 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 60-85 | 41.4 | 49.7 | -8.3 | -29.7 | -20.5 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | total | 31-46 | 40.3 | 49.6 | -9.4 | -17.58 | -22.8 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | total | 60-88 | 40.5 | 49.6 | -9.1 | -32.87 | -22.2 |  |  | DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 49.5 | 50.5 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| rlm_quiet | close | 1-3k bets | 186-280 | 39.9 | -2.1 | -9.4 |  |
| rlm_quiet | close | 3k+ bets | 75-106 | 41.4 | -0.9 | -11.5 |  |
| rlm_quiet | close | <1k bets | 32-47 | 40.5 | -1.4 | -16.0 |  |
| rlm_quiet | close | pin $1-2k | 78-133 | 37.0 | -6.6 | -18.6 |  |
| rlm_quiet | close | pin $2k+ | 92-112 | 45.1 | 6.9 | 3.2 |  |
| rlm_quiet | close | pin limit <$1k | 51-55 | 48.1 | -1.2 | -7.6 |  |
| pin_move | close | 1-3k bets | 440-445 | 49.7 | 0.2 | -2.3 |  |
| pin_move | close | 3k+ bets | 174-182 | 48.9 | -0.7 | -5.9 |  |
| pin_move | close | <1k bets | 87-87 | 50.0 | -0.3 | -4.3 |  |
| pin_move | close | pin $1-2k | 316-333 | 48.7 | -1.3 | -4.5 |  |
| pin_move | close | pin $2k+ | 261-267 | 49.4 | 0.2 | -4.4 |  |
| pin_move | close | pin limit <$1k | 124-117 | 51.5 | 1.8 | 0.3 |  |
| money_delta | close | 1-3k bets | 258-335 | 43.5 | -1.2 | -8.6 |  |
| money_delta | close | 3k+ bets | 106-140 | 43.1 | -0.6 | -4.4 |  |
| money_delta | close | <1k bets | 52-76 | 40.6 | -2.3 | -15.4 |  |
| money_delta | close | pin $1-2k | 152-153 | 49.8 | 3.6 | 3.8 |  |
| money_delta | close | pin $2k+ | 106-141 | 42.9 | 1.4 | -9.5 |  |
| money_delta | close | pin limit <$1k | 62-73 | 45.9 | -3.4 | -8.7 |  |
| pin_rlm | close | 1-3k bets | 114-135 | 45.8 | 3.5 | 8.5 |  |
| pin_rlm | close | 3k+ bets | 42-63 | 40.0 | -1.8 | -13.6 |  |
| pin_rlm | close | <1k bets | 26-26 | 50.0 | 7.8 | 7.9 |  |
| pin_rlm | close | pin $1-2k | 79-92 | 46.2 | 2.2 | 4.3 |  |
| pin_rlm | close | pin $2k+ | 54-91 | 37.2 | 1.4 | -6.4 |  |
| pin_rlm | close | pin limit <$1k | 49-41 | 54.4 | 5.7 | 14.3 |  |
| follow_move | close | 1-3k bets | 750-716 | 51.2 | 0.6 | -6.0 |  |
| follow_move | close | 3k+ bets | 271-255 | 51.5 | 0.7 | -5.2 |  |
| follow_move | close | <1k bets | 164-154 | 51.6 | -0.4 | -11.8 |  |
| follow_move | close | pin $1-2k | 355-409 | 46.5 | -3.9 | -12.9 |  |
| follow_move | close | pin $2k+ | 320-282 | 53.2 | 2.5 | -2.0 |  |
| follow_move | close | pin limit <$1k | 150-145 | 50.8 | 1.0 | -3.1 |  |
| rlm_ratio | close | 1-3k bets | 172-232 | 42.6 | -1.2 | -8.8 |  |
| rlm_ratio | close | 3k+ bets | 63-72 | 46.7 | 3.1 | -0.7 |  |
| rlm_ratio | close | <1k bets | 36-38 | 48.6 | 5.3 | -3.3 |  |
| rlm_ratio | close | pin $1-2k | 95-106 | 47.3 | 1.6 | -1.4 |  |
| rlm_ratio | close | pin $2k+ | 53-80 | 39.8 | 2.2 | -11.8 |  |
| rlm_ratio | close | pin limit <$1k | 54-51 | 51.4 | 2.3 | -0.8 |  |
| money_level | close | 1-3k bets | 961-698 | 57.9 | 2.6 | -2.4 |  |
| money_level | close | 3k+ bets | 340-281 | 54.8 | -0.3 | -5.2 |  |
| money_level | close | <1k bets | 205-149 | 57.9 | 2.5 | -6.2 |  |
| money_level | close | pin $1-2k | 443-395 | 52.9 | -0.8 | -6.3 |  |
| money_level | close | pin $2k+ | 388-318 | 55.0 | -2.3 | -9.3 |  |
| money_level | close | pin limit <$1k | 179-157 | 53.3 | 2.9 | 1.1 |  |
| sharp_gap | close | 1-3k bets | 727-858 | 45.9 | -1.8 | -9.2 |  |
| sharp_gap | close | 3k+ bets | 282-320 | 46.8 | -0.8 | -3.4 |  |
| sharp_gap | close | <1k bets | 160-176 | 47.6 | -0.6 | -11.1 |  |
| sharp_gap | close | pin $1-2k | 381-424 | 47.3 | -1.3 | -6.4 |  |
| sharp_gap | close | pin $2k+ | 310-369 | 45.7 | -1.1 | -6.2 |  |
| sharp_gap | close | pin limit <$1k | 153-169 | 47.5 | -1.9 | -6.2 |  |
| money_moving | close | 1-3k bets | 741-851 | 46.5 | -1.5 | -8.6 |  |
| money_moving | close | 3k+ bets | 284-320 | 47.0 | -1.1 | -4.3 |  |
| money_moving | close | <1k bets | 158-174 | 47.6 | -0.4 | -9.8 |  |
| money_moving | close | pin $1-2k | 382-425 | 47.3 | -1.7 | -6.6 |  |
| money_moving | close | pin $2k+ | 315-364 | 46.4 | -0.4 | -5.4 |  |
| money_moving | close | pin limit <$1k | 153-175 | 46.6 | -2.8 | -7.9 |  |
| pin_value | close | 1-3k bets | 331-323 | 50.6 | 2.2 | 2.9 |  |
| pin_value | close | 3k+ bets | 106-131 | 44.7 | -4.3 | -13.0 |  |
| pin_value | close | <1k bets | 72-58 | 55.4 | 8.0 | 12.3 |  |
| pin_value | close | pin $1-2k | 235-256 | 47.9 | -0.7 | -3.9 |  |
| pin_value | close | pin $2k+ | 146-165 | 46.9 | -0.1 | -1.5 |  |
| pin_value | close | pin limit <$1k | 130-92 | 58.6 | 8.7 | 13.1 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 46.7 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 46.7 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 295-345 | 46.1 | -3.2 | -9.2 |  |
| consensus_gap | close | 3k+ bets | 114-123 | 48.1 | -1.5 | 1.7 |  |
| consensus_gap | close | <1k bets | 58-86 | 40.3 | -5.1 | -19.8 |  |
| consensus_gap | close | pin $1-2k | 139-148 | 48.4 | -1.3 | -0.2 |  |
| consensus_gap | close | pin $2k+ | 142-134 | 51.4 | -0.4 | 2.0 |  |
| consensus_gap | close | pin limit <$1k | 60-56 | 51.7 | 1.7 | 0.6 |  |
| consensus_gap+follow_move | close | 1-3k bets | 109-106 | 50.7 | -0.6 | -4.8 |  |
| consensus_gap+money_level | close | 1-3k bets | 194-132 | 59.5 | 0.9 | -0.2 |  |
| consensus_gap+money_moving | close | 1-3k bets | 123-185 | 39.9 | -6.5 | -11.8 |  |
| consensus_gap+pin_move | close | 1-3k bets | 76-67 | 53.1 | 2.6 | 11.4 |  |
| consensus_gap+pin_value | close | 1-3k bets | 115-128 | 47.3 | 0.7 | -2.0 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 121-190 | 38.9 | -6.9 | -13.2 |  |
| follow_move+money_level | close | 1-3k bets | 471-340 | 58.1 | 2.5 | -3.9 |  |
| follow_move+money_moving | close | 1-3k bets | 409-449 | 47.7 | -1.2 | -8.5 |  |
| follow_move+pin_move | close | 1-3k bets | 308-337 | 47.8 | -1.8 | -8.5 |  |
| follow_move+pin_value | close | 1-3k bets | 109-104 | 51.2 | 2.2 | 1.5 |  |
| follow_move+sharp_gap | close | 1-3k bets | 410-450 | 47.7 | -0.9 | -7.9 |  |
| money_level+money_moving | close | 1-3k bets | 529-465 | 53.2 | 0.9 | -3.6 |  |
| money_level+pin_move | close | 1-3k bets | 253-223 | 53.2 | 0.4 | -3.4 |  |
| money_level+pin_value | close | 1-3k bets | 158-140 | 53.0 | 3.4 | -0.5 |  |
| money_level+sharp_gap | close | 1-3k bets | 510-459 | 52.6 | 0.6 | -3.9 |  |
| money_moving+pin_move | close | 1-3k bets | 257-271 | 48.7 | 0.0 | -2.6 |  |
| money_moving+pin_value | close | 1-3k bets | 141-163 | 46.4 | -1.5 | -6.2 |  |
| money_moving+sharp_gap | close | 1-3k bets | 699-816 | 46.1 | -1.6 | -8.4 |  |
| pin_move+pin_value | close | 1-3k bets | 139-136 | 50.5 | 0.9 | -1.5 |  |
| pin_move+sharp_gap | close | 1-3k bets | 261-277 | 48.5 | 0.1 | -2.6 |  |
| pin_value+sharp_gap | close | 1-3k bets | 142-169 | 45.7 | -2.2 | -7.7 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 186-280 | 39.9 | -2.1 | -9.4 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 91-165 | 35.5 | -5.8 | -16.9 |  |
| consensus_gap+money_delta | close | 1-3k bets | 33-70 | 32.0 | -6.6 | -18.2 |  |
| follow_move+money_delta | close | 1-3k bets | 127-165 | 43.5 | -2.4 | -13.1 |  |
| money_delta+money_level | close | 1-3k bets | 92-88 | 51.1 | 3.1 | 4.8 |  |
| money_delta+money_moving | close | 1-3k bets | 187-265 | 41.4 | -1.7 | -10.3 |  |
| money_delta+pin_value | close | 1-3k bets | 57-52 | 52.3 | 4.5 | 4.0 |  |
| money_delta+sharp_gap | close | 1-3k bets | 186-262 | 41.5 | -1.6 | -10.0 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 92-107 | 46.2 | -0.4 | -2.7 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 22-30 | 42.3 | 3.2 | 21.3 |  |
| money_level+pin_rlm | close | 1-3k bets | 49-39 | 55.7 | 8.0 | 7.6 |  |
| pin_move+pin_rlm | close | 1-3k bets | 105-113 | 48.2 | 4.3 | 6.6 |  |
| pin_rlm+pin_value | close | 1-3k bets | 33-30 | 52.4 | 5.8 | 22.8 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 114-135 | 45.8 | 3.5 | 8.5 |  |
| money_delta+pin_rlm | close | 1-3k bets | 64-76 | 45.7 | 3.0 | 5.6 |  |
| money_moving+pin_rlm | close | 1-3k bets | 109-127 | 46.2 | 3.7 | 10.2 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 26-38 | 40.6 | -0.0 | 3.6 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 172-232 | 42.6 | -1.2 | -8.8 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 89-122 | 42.2 | -2.1 | -14.2 |  |
| money_level+rlm_ratio | close | 1-3k bets | 79-74 | 51.6 | 3.1 | -0.2 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 165-221 | 42.7 | -1.2 | -8.1 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 90-100 | 47.4 | 2.6 | -1.2 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 30-27 | 52.6 | 4.8 | 1.6 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 172-232 | 42.6 | -1.2 | -8.8 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 17-42 | 28.8 | -7.8 | -14.3 |  |
| follow_move+pin_rlm | close | 1-3k bets | 84-107 | 44.0 | 0.6 | -7.4 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 85-161 | 34.6 | -6.6 | -18.4 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 84-121 | 41.0 | -2.7 | -11.1 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 35-68 | 34.0 | -5.5 | -20.2 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 84-107 | 44.0 | 0.6 | -7.4 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 71-142 | 33.3 | -6.6 | -18.7 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 47-93 | 33.6 | -9.1 | -28.6 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 22-30 | 42.3 | -3.9 | 1.4 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 50.5 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 42-36 | 53.8 | 3.4 | 0.9 |  |
| consensus_gap+money_moving | close | 3k+ bets | 46-71 | 39.3 | -7.0 | 2.7 |  |
| consensus_gap+pin_move | close | 3k+ bets | 35-28 | 55.6 | 4.8 | 6.9 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 5-10 | 33.3 | -8.8 | -11.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 45-44 | 50.6 | 2.8 | 2.1 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 5-10 | 33.3 | -7.0 | -10.7 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 46-72 | 39.0 | -6.9 | 4.1 |  |
| follow_move+money_moving | close | 3k+ bets | 143-155 | 48.0 | -0.8 | -7.3 |  |
| follow_move+pin_move | close | 3k+ bets | 133-132 | 50.2 | 0.6 | -2.9 |  |
| follow_move+pin_rlm | close | 3k+ bets | 39-46 | 45.9 | 2.8 | 0.1 |  |
| follow_move+pin_value | close | 3k+ bets | 44-48 | 47.8 | -2.0 | -10.0 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 63-72 | 46.7 | 3.1 | -0.7 |  |
| follow_move+sharp_gap | close | 3k+ bets | 142-153 | 48.1 | -0.0 | -5.3 |  |
| money_moving+pin_move | close | 3k+ bets | 94-115 | 45.0 | -3.3 | -11.9 |  |
| money_moving+pin_rlm | close | 3k+ bets | 41-61 | 40.2 | -1.6 | -13.0 |  |
| money_moving+pin_value | close | 3k+ bets | 53-73 | 42.1 | -6.5 | -15.5 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 60-70 | 46.2 | 2.6 | -2.0 |  |
| money_moving+sharp_gap | close | 3k+ bets | 273-308 | 47.0 | -0.7 | -3.3 |  |
| pin_move+pin_rlm | close | 3k+ bets | 39-54 | 41.9 | -1.6 | -9.7 |  |
| pin_move+pin_value | close | 3k+ bets | 49-62 | 44.1 | -5.5 | -16.7 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 41-46 | 47.1 | 2.4 | 0.9 |  |
| pin_move+sharp_gap | close | 3k+ bets | 92-115 | 44.4 | -3.4 | -11.7 |  |
| pin_rlm+pin_value | close | 3k+ bets | 8-18 | 30.8 | -16.7 | -41.4 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 39-46 | 45.9 | 2.8 | 0.1 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 42-63 | 40.0 | -1.8 | -13.6 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 10-12 | 45.5 | -4.7 | -13.7 |  |
| pin_value+sharp_gap | close | 3k+ bets | 53-73 | 42.1 | -6.7 | -15.4 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 63-72 | 46.7 | 3.1 | -0.7 |  |
| follow_move+money_delta | close | 3k+ bets | 50-66 | 43.1 | -1.5 | -11.4 |  |
| money_level+money_moving | close | 3k+ bets | 186-175 | 51.5 | -0.9 | -5.2 |  |
| money_level+sharp_gap | close | 3k+ bets | 181-172 | 51.3 | -0.8 | -4.4 |  |
| follow_move+money_level | close | 3k+ bets | 154-117 | 56.8 | 0.7 | -4.4 |  |
| money_level+rlm_ratio | close | 3k+ bets | 26-15 | 63.4 | 15.7 | 29.5 |  |
| consensus_gap+money_level | close | 3k+ bets | 69-60 | 53.5 | -4.2 | -9.3 |  |
| money_level+pin_move | close | 3k+ bets | 85-85 | 50.0 | -4.0 | -9.7 |  |
| money_level+pin_value | close | 3k+ bets | 59-69 | 46.1 | -4.6 | -14.2 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 10-16 | 38.5 | -0.9 | -8.7 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 75-106 | 41.4 | -0.9 | -11.5 |  |
| money_delta+money_moving | close | 3k+ bets | 78-108 | 41.9 | -0.6 | -2.7 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 29-48 | 37.7 | -2.9 | -15.4 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 40-59 | 40.4 | -1.6 | -12.8 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 37-59 | 38.5 | -3.6 | -16.9 |  |
| consensus_gap+money_delta | close | 3k+ bets | 15-27 | 35.7 | -4.2 | 12.2 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 18-37 | 32.7 | -9.1 | -30.4 |  |
| money_delta+sharp_gap | close | 3k+ bets | 76-105 | 42.0 | -0.5 | -2.3 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 45-53 | 45.9 | 2.9 | -1.6 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 17-31 | 35.4 | -4.9 | -19.1 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 10-18 | 35.7 | -13.5 | -32.0 |  |
| money_delta+money_level | close | 3k+ bets | 36-30 | 54.5 | 7.6 | 9.8 |  |
| money_level+pin_rlm | close | 3k+ bets | 16-11 | 59.3 | 13.4 | 26.8 |  |
| money_delta+pin_value | close | 3k+ bets | 22-23 | 48.9 | 1.6 | -7.6 |  |
| money_delta+pin_move | close | 3k+ bets | 44-53 | 45.4 | -0.1 | -8.1 |  |
| money_delta+pin_rlm | close | 3k+ bets | 27-35 | 43.5 | 1.4 | -8.0 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 35-36 | 49.3 | 5.9 | 4.0 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 46.7 | 87.7 |  |
| money_level+money_moving | close | <1k bets | 110-95 | 53.7 | 1.3 | -8.2 |  |
| money_level+sharp_gap | close | <1k bets | 113-96 | 54.1 | 1.3 | -8.3 |  |
| money_moving+sharp_gap | close | <1k bets | 154-171 | 47.4 | -0.5 | -10.5 |  |
| consensus_gap+money_level | close | <1k bets | 31-28 | 52.5 | -3.9 | -18.5 |  |
| consensus_gap+money_moving | close | <1k bets | 25-41 | 37.9 | -5.9 | -19.1 |  |
| consensus_gap+pin_move | close | <1k bets | 8-13 | 38.1 | -12.6 | -17.2 |  |
| consensus_gap+pin_value | close | <1k bets | 19-16 | 54.3 | 11.9 | 29.5 |  |
| consensus_gap+sharp_gap | close | <1k bets | 26-43 | 37.7 | -6.0 | -20.5 |  |
| money_level+pin_move | close | <1k bets | 48-44 | 52.2 | -0.8 | -6.6 |  |
| money_level+pin_value | close | <1k bets | 26-21 | 55.3 | 5.5 | 3.3 |  |
| money_moving+pin_move | close | <1k bets | 47-50 | 48.5 | 0.6 | -2.4 |  |
| money_moving+pin_value | close | <1k bets | 23-21 | 52.3 | 7.0 | 20.2 |  |
| pin_move+pin_value | close | <1k bets | 32-24 | 57.1 | 8.6 | 14.5 |  |
| pin_move+sharp_gap | close | <1k bets | 47-51 | 48.0 | -0.3 | -6.7 |  |
| pin_value+sharp_gap | close | <1k bets | 23-20 | 53.5 | 7.8 | 23.0 |  |
| follow_move+money_delta | close | <1k bets | 26-29 | 47.3 | 3.6 | -5.4 |  |
| follow_move+money_moving | close | <1k bets | 76-81 | 48.4 | -0.9 | -11.2 |  |
| follow_move+pin_move | close | <1k bets | 56-57 | 49.6 | -1.2 | -7.7 |  |
| follow_move+sharp_gap | close | <1k bets | 77-82 | 48.4 | -1.4 | -13.6 |  |
| money_delta+money_moving | close | <1k bets | 36-57 | 38.7 | -2.0 | -16.4 |  |
| money_delta+pin_move | close | <1k bets | 14-20 | 41.2 | -3.5 | -19.8 |  |
| money_delta+sharp_gap | close | <1k bets | 36-57 | 38.7 | -2.0 | -16.4 |  |
| follow_move+rlm_quiet | close | <1k bets | 32-47 | 40.5 | -1.4 | -16.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 36-38 | 48.6 | 5.3 | -3.3 |  |
| money_delta+rlm_quiet | close | <1k bets | 13-14 | 48.1 | 7.0 | -0.5 |  |
| money_delta+rlm_ratio | close | <1k bets | 21-22 | 48.8 | 6.4 | -1.2 |  |
| money_moving+rlm_quiet | close | <1k bets | 19-19 | 50.0 | 8.3 | 7.8 |  |
| money_moving+rlm_ratio | close | <1k bets | 36-38 | 48.6 | 5.3 | -3.3 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 15-16 | 48.4 | 7.6 | -0.6 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 18-20 | 47.4 | 5.1 | -3.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 36-38 | 48.6 | 5.3 | -3.3 |  |
| follow_move+money_level | close | <1k bets | 99-72 | 57.9 | 0.8 | -10.3 |  |
| consensus_gap+money_delta | close | <1k bets | 7-22 | 24.1 | -10.8 | -35.0 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -2.8 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 13-17 | 43.3 | 3.1 | -7.1 |  |
| money_moving+pin_rlm | close | <1k bets | 26-26 | 50.0 | 7.8 | 7.9 |  |
| pin_rlm+sharp_gap | close | <1k bets | 26-26 | 50.0 | 7.8 | 7.9 |  |
| money_delta+pin_value | close | <1k bets | 10-8 | 55.6 | 9.8 | 25.3 |  |
| consensus_gap+follow_move | close | <1k bets | 14-21 | 40.0 | -11.0 | -35.2 |  |
| follow_move+pin_rlm | close | <1k bets | 20-16 | 55.6 | 11.3 | 9.1 |  |
| follow_move+pin_value | close | <1k bets | 23-15 | 60.5 | 11.6 | 15.1 |  |
| pin_move+pin_rlm | close | <1k bets | 24-21 | 53.3 | 9.0 | 10.6 |  |
| pin_move+rlm_quiet | close | <1k bets | 13-14 | 48.1 | 2.3 | 2.3 |  |
| pin_move+rlm_ratio | close | <1k bets | 20-18 | 52.6 | 7.1 | 2.3 |  |
| pin_rlm+pin_value | close | <1k bets | 7-3 | 70.0 | 27.1 | 66.8 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 9-6 | 60.0 | 16.0 | 17.9 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 20-16 | 55.6 | 11.3 | 9.1 |  |
| pin_value+rlm_quiet | close | <1k bets | 6-4 | 60.0 | 10.9 | 15.0 |  |
| pin_value+rlm_ratio | close | <1k bets | 5-1 | 83.3 | 34.8 | 58.3 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -6.7 | -42.5 |  |
| money_delta+money_level | close | <1k bets | 15-20 | 42.9 | -0.4 | -14.3 |  |
| money_level+rlm_ratio | close | <1k bets | 17-17 | 50.0 | 5.1 | -2.7 |  |
| money_level+pin_rlm | close | <1k bets | 11-9 | 55.0 | 11.6 | 8.4 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-6 | 14.3 | -22.8 | -72.7 |  |
| consensus_gap+follow_move | close | pin $1-2k | 50-57 | 46.7 | -4.9 | -10.9 |  |
| consensus_gap+money_moving | close | pin $1-2k | 61-77 | 44.2 | -4.3 | -5.2 |  |
| consensus_gap+pin_move | close | pin $1-2k | 53-54 | 49.5 | -1.8 | 5.9 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 14-19 | 42.4 | 1.0 | 25.4 |  |
| consensus_gap+pin_value | close | pin $1-2k | 81-85 | 48.8 | 2.3 | -0.9 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 15-16 | 48.4 | 3.4 | 6.1 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 59-75 | 44.0 | -3.6 | -4.2 |  |
| follow_move+money_moving | close | pin $1-2k | 207-253 | 45.0 | -4.4 | -12.4 |  |
| follow_move+pin_move | close | pin $1-2k | 216-258 | 45.6 | -4.4 | -12.1 |  |
| follow_move+pin_rlm | close | pin $1-2k | 65-73 | 47.1 | 1.5 | -0.8 |  |
| follow_move+pin_value | close | pin $1-2k | 81-94 | 46.3 | -3.2 | -12.5 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 95-106 | 47.3 | 1.6 | -1.4 |  |
| follow_move+sharp_gap | close | pin $1-2k | 211-253 | 45.5 | -3.9 | -11.8 |  |
| money_moving+pin_move | close | pin $1-2k | 188-212 | 47.0 | -2.3 | -5.6 |  |
| money_moving+pin_rlm | close | pin $1-2k | 76-85 | 47.2 | 2.7 | 6.9 |  |
| money_moving+pin_value | close | pin $1-2k | 90-124 | 42.1 | -5.9 | -16.7 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 93-99 | 48.4 | 2.4 | 0.9 |  |
| money_moving+sharp_gap | close | pin $1-2k | 366-407 | 47.3 | -1.4 | -6.1 |  |
| pin_move+pin_rlm | close | pin $1-2k | 76-83 | 47.8 | 2.6 | 5.9 |  |
| pin_move+pin_value | close | pin $1-2k | 97-121 | 44.5 | -5.3 | -14.5 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 73-76 | 49.0 | 2.4 | 1.8 |  |
| pin_move+sharp_gap | close | pin $1-2k | 190-217 | 46.7 | -2.2 | -6.4 |  |
| pin_rlm+pin_value | close | pin $1-2k | 19-30 | 38.8 | -9.3 | -19.6 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 65-73 | 47.1 | 1.5 | -0.8 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 79-92 | 46.2 | 2.2 | 4.3 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 21-25 | 45.7 | -3.4 | -12.8 |  |
| pin_value+sharp_gap | close | pin $1-2k | 90-121 | 42.7 | -5.3 | -15.5 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 95-106 | 47.3 | 1.6 | -1.4 |  |
| follow_move+money_level | close | pin $1-2k | 226-221 | 50.6 | -3.3 | -11.3 |  |
| money_level+rlm_ratio | close | pin $1-2k | 49-42 | 53.8 | 5.9 | 4.8 |  |
| money_level+sharp_gap | close | pin $1-2k | 269-268 | 50.1 | -1.4 | -7.5 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 5-15 | 25.0 | -15.6 | -30.7 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 78-133 | 37.0 | -6.6 | -18.6 |  |
| money_level+money_moving | close | pin $1-2k | 273-271 | 50.2 | -1.6 | -7.8 |  |
| consensus_gap+money_level | close | pin $1-2k | 80-71 | 53.0 | -3.5 | -7.5 |  |
| money_level+pin_value | close | pin $1-2k | 106-109 | 49.3 | -0.5 | -7.8 |  |
| money_level+pin_move | close | pin $1-2k | 180-180 | 50.0 | -2.4 | -8.9 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 40-63 | 38.8 | -5.0 | -9.9 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 55-79 | 41.0 | -4.2 | -9.1 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 25-43 | 36.8 | -7.3 | -13.8 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 33-54 | 37.9 | -5.2 | -11.1 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 41-65 | 38.7 | -5.1 | -12.0 |  |
| money_level+pin_rlm | close | pin $1-2k | 35-30 | 53.8 | 7.6 | 5.7 |  |
| follow_move+money_delta | close | pin $1-2k | 74-84 | 46.8 | 0.3 | -4.6 |  |
| money_delta+money_moving | close | pin $1-2k | 102-117 | 46.6 | 2.0 | 0.8 |  |
| money_delta+pin_move | close | pin $1-2k | 73-80 | 47.7 | 0.4 | -0.1 |  |
| money_delta+pin_rlm | close | pin $1-2k | 47-54 | 46.5 | 2.7 | 4.7 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 54-56 | 49.1 | 3.5 | 2.1 |  |
| money_delta+sharp_gap | close | pin $1-2k | 102-115 | 47.0 | 2.4 | 1.7 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 46.7 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 53-48 | 52.5 | 4.4 | 2.1 |  |
| consensus_gap+money_delta | close | pin $1-2k | 20-26 | 43.5 | 1.7 | 7.4 |  |
| money_delta+pin_value | close | pin $1-2k | 46-48 | 48.9 | 0.8 | -3.1 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 23-42 | 35.4 | -8.6 | -20.9 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 14-32 | 30.4 | -18.4 | -40.5 |  |
| consensus_gap+follow_move | close | pin $2k+ | 44-35 | 55.7 | 2.5 | -5.6 |  |
| consensus_gap+money_delta | close | pin $2k+ | 12-28 | 30.0 | -6.0 | -41.4 |  |
| consensus_gap+money_level | close | pin $2k+ | 93-68 | 57.8 | -4.5 | -10.0 |  |
| consensus_gap+money_moving | close | pin $2k+ | 50-80 | 38.5 | -8.0 | -6.7 |  |
| consensus_gap+pin_move | close | pin $2k+ | 47-40 | 54.0 | 3.6 | 3.8 |  |
| consensus_gap+pin_value | close | pin $2k+ | 55-60 | 47.8 | 3.5 | 8.3 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 4-15 | 21.1 | -13.4 | -52.3 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 51-84 | 37.8 | -9.0 | -7.2 |  |
| follow_move+money_delta | close | pin $2k+ | 42-56 | 42.9 | 1.7 | -11.7 |  |
| follow_move+money_level | close | pin $2k+ | 178-124 | 58.9 | 0.2 | -5.5 |  |
| follow_move+money_moving | close | pin $2k+ | 151-160 | 48.6 | 1.0 | -7.1 |  |
| follow_move+pin_move | close | pin $2k+ | 197-189 | 51.0 | 1.6 | -3.0 |  |
| follow_move+pin_value | close | pin $2k+ | 45-43 | 51.1 | 3.2 | 7.6 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 53-80 | 39.8 | 2.2 | -11.8 |  |
| follow_move+sharp_gap | close | pin $2k+ | 148-160 | 48.1 | 0.7 | -7.3 |  |
| money_delta+money_level | close | pin $2k+ | 30-25 | 54.5 | 10.1 | 10.7 |  |
| money_delta+money_moving | close | pin $2k+ | 76-109 | 41.1 | 2.0 | -10.4 |  |
| money_delta+pin_move | close | pin $2k+ | 44-60 | 42.3 | -0.1 | -14.0 |  |
| money_delta+pin_value | close | pin $2k+ | 24-25 | 49.0 | 3.8 | -6.5 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 26-41 | 38.8 | 0.8 | -16.9 |  |
| money_delta+sharp_gap | close | pin $2k+ | 74-108 | 40.7 | 1.5 | -11.2 |  |
| money_level+money_moving | close | pin $2k+ | 206-199 | 50.9 | -2.1 | -7.9 |  |
| money_level+pin_move | close | pin $2k+ | 132-114 | 53.7 | -2.1 | -6.5 |  |
| money_level+pin_value | close | pin $2k+ | 70-77 | 47.6 | -2.3 | -11.8 |  |
| money_level+rlm_ratio | close | pin $2k+ | 19-18 | 51.4 | 5.8 | 5.5 |  |
| money_level+sharp_gap | close | pin $2k+ | 203-202 | 50.1 | -2.7 | -8.5 |  |
| money_moving+pin_move | close | pin $2k+ | 131-147 | 47.1 | 0.3 | -6.5 |  |
| money_moving+pin_value | close | pin $2k+ | 74-92 | 44.6 | -2.0 | -2.8 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 53-79 | 40.2 | 2.5 | -11.2 |  |
| money_moving+sharp_gap | close | pin $2k+ | 305-359 | 45.9 | -0.7 | -5.6 |  |
| pin_move+pin_value | close | pin $2k+ | 67-65 | 50.8 | 2.0 | -1.5 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 39-55 | 41.5 | 2.7 | -6.7 |  |
| pin_move+sharp_gap | close | pin $2k+ | 130-149 | 46.6 | -0.2 | -6.9 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 6-7 | 46.2 | 2.1 | -8.8 |  |
| pin_value+sharp_gap | close | pin $2k+ | 74-95 | 43.8 | -3.0 | -4.5 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 53-80 | 39.8 | 2.2 | -11.8 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 9-24 | 27.3 | -6.6 | -13.7 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 7-16 | 30.4 | -0.9 | -31.5 |  |
| follow_move+pin_rlm | close | pin $2k+ | 39-63 | 38.2 | 1.9 | -12.5 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 92-112 | 45.1 | 6.9 | 3.2 |  |
| money_moving+pin_rlm | close | pin $2k+ | 54-90 | 37.5 | 1.6 | -5.7 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 41-61 | 40.2 | 4.4 | -9.5 |  |
| pin_move+pin_rlm | close | pin $2k+ | 44-64 | 40.7 | 3.2 | -6.2 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 61-78 | 43.9 | 4.0 | -3.2 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 21-46 | 31.3 | -1.0 | -23.5 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 39-63 | 38.2 | 1.9 | -12.5 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 54-91 | 37.2 | 1.4 | -6.4 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 28-53 | 34.6 | 1.9 | -18.3 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 40-61 | 39.6 | 3.7 | -11.2 |  |
| money_delta+pin_rlm | close | pin $2k+ | 30-50 | 37.5 | 1.3 | -11.6 |  |
| money_level+pin_rlm | close | pin $2k+ | 17-13 | 56.7 | 13.0 | 19.4 |  |
| pin_rlm+pin_value | close | pin $2k+ | 9-14 | 39.1 | -0.7 | 18.6 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 23-34 | 40.4 | 2.5 | -16.5 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 8-10 | 44.4 | 3.7 | 40.9 |  |
| follow_move+money_delta | close | pin limit <$1k | 37-49 | 43.0 | -6.2 | -17.4 |  |
| money_level+money_moving | close | pin limit <$1k | 100-103 | 49.3 | -0.6 | -5.7 |  |
| money_level+sharp_gap | close | pin limit <$1k | 95-97 | 49.5 | -0.3 | -5.2 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 141-157 | 47.3 | -2.1 | -6.4 |  |
| consensus_gap+money_level | close | pin limit <$1k | 34-31 | 52.3 | 1.6 | -3.0 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 19-14 | 57.6 | 8.9 | 22.0 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 44-43 | 50.6 | 1.1 | 0.3 |  |
| follow_move+money_moving | close | pin limit <$1k | 89-101 | 46.8 | -2.6 | -10.1 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 93-100 | 48.2 | -1.2 | -7.5 |  |
| money_level+pin_move | close | pin limit <$1k | 74-61 | 54.8 | 4.9 | 4.6 |  |
| money_level+pin_value | close | pin limit <$1k | 67-45 | 59.8 | 9.7 | 13.3 |  |
| pin_move+pin_value | close | pin limit <$1k | 56-37 | 60.2 | 10.3 | 19.3 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 23-15 | 60.5 | 11.0 | 12.2 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 28-27 | 50.9 | 2.1 | 4.5 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 30-29 | 50.8 | 1.9 | 3.8 |  |
| follow_move+money_level | close | pin limit <$1k | 80-72 | 52.6 | 2.4 | -0.2 |  |
| follow_move+pin_move | close | pin limit <$1k | 84-82 | 50.6 | 1.1 | -3.0 |  |
| follow_move+pin_value | close | pin limit <$1k | 50-31 | 61.7 | 11.9 | 17.2 |  |
| money_moving+pin_move | close | pin limit <$1k | 79-80 | 49.7 | 0.3 | -2.2 |  |
| money_moving+pin_value | close | pin limit <$1k | 53-42 | 55.8 | 6.2 | 10.6 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 80-80 | 50.0 | 0.6 | -1.6 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 54-47 | 53.5 | 3.9 | 5.9 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 51-55 | 48.1 | -1.2 | -7.6 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 29-37 | 43.9 | -5.2 | -15.8 |  |
| money_delta+money_moving | close | pin limit <$1k | 52-59 | 46.8 | -2.3 | -6.2 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 10-8 | 55.6 | 8.2 | 30.0 |  |
| money_delta+money_level | close | pin limit <$1k | 26-25 | 51.0 | 1.3 | -2.3 |  |
| money_delta+pin_value | close | pin limit <$1k | 19-10 | 65.5 | 16.4 | 39.8 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 51-57 | 47.2 | -1.9 | -5.4 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 33-40 | 45.2 | -3.7 | -7.2 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 7-4 | 63.6 | 17.5 | 61.2 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 27-24 | 52.9 | 4.5 | 10.3 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 46-39 | 54.1 | 5.4 | 14.3 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 48-41 | 53.9 | 4.9 | 8.4 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 20-7 | 74.1 | 25.1 | 57.7 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 49-41 | 54.4 | 5.7 | 14.3 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 7-4 | 63.6 | 15.9 | 21.7 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 16-10 | 61.5 | 11.8 | 17.5 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 12-22 | 35.3 | -13.2 | -32.2 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 26-31 | 45.6 | -3.5 | -12.2 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 39-33 | 54.2 | 5.1 | 4.2 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 54-51 | 51.4 | 2.3 | -0.8 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 30-32 | 48.4 | -0.6 | -7.0 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 23-36 | 39.0 | -10.0 | -25.1 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 49-48 | 50.5 | 1.5 | -2.5 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 39-33 | 54.2 | 5.1 | 4.2 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 15-16 | 48.4 | -0.0 | -6.9 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 39-33 | 54.2 | 5.1 | 4.2 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 24-29 | 45.3 | -3.6 | -13.1 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 54-51 | 51.4 | 2.3 | -0.8 |  |
| money_level+pin_rlm | close | pin limit <$1k | 24-16 | 60.0 | 10.4 | 15.1 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 26-19 | 57.8 | 8.6 | 12.1 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 18-8 | 69.2 | 19.5 | 32.5 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 7-6 | 53.8 | 5.6 | 2.9 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 50.5 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.6 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -51.9 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 53-61 | 46.5 | 10.1 | 13.1 | 0.54 |
| rlm_quiet | early | pin $1-2k | 3-7 | 30.0 | -1.0 | 7.2 | -0.12 |
| rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.5 | -100.0 | 1.3 |
| rlm_quiet | early | pin limit <$1k | 6-9 | 40.0 | -5.4 | -19.3 | 0.28 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.5 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 14-21 | 40.0 | -9.1 | -26.3 | 0.19 |
| pin_move | early | pin $1-2k | 2-9 | 18.2 | -30.9 | -68.6 | 0.27 |
| pin_move | early | pin limit <$1k | 12-16 | 42.9 | -7.0 | -20.2 | 0.44 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 12-11 | 52.2 | 13.6 | 22.6 | 0.98 |
| money_delta | early | pin $1-2k | 0-3 | 0.0 | -36.8 | -100.0 | 2.17 |
| money_delta | early | pin limit <$1k | 5-0 | 100.0 | 50.9 | 88.6 | 0.0 |
| pin_rlm | early | <1k bets | 1-4 | 20.0 | -17.1 | -61.5 | -0.3 |
| pin_rlm | early | pin $1-2k | 0-3 | 0.0 | -42.8 | -100.0 | -0.67 |
| pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 21.5 | -3.7 | 0.25 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.7 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -51.9 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 597-542 | 52.4 | 1.6 | -5.9 | 0.15 |
| follow_move | early | pin $1-2k | 41-32 | 56.2 | 6.4 | 4.5 | -0.34 |
| follow_move | early | pin $2k+ | 0-2 | 0.0 | -40.9 | -100.0 | 0.65 |
| follow_move | early | pin limit <$1k | 60-60 | 50.0 | 0.1 | -5.9 | -0.08 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 22.8 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.3 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 33-29 | 53.2 | 14.5 | 20.8 | 0.52 |
| rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.6 | 29.7 | -1.02 |
| rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.9 | -100.0 | 0.65 |
| rlm_ratio | early | pin limit <$1k | 8-2 | 80.0 | 36.6 | 61.1 | 0.33 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 1.6 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 44.1 | 59.7 | 0.33 |
| money_level | early | <1k bets | 213-150 | 58.7 | -0.2 | -7.3 | -0.25 |
| money_level | early | pin $1-2k | 24-13 | 64.9 | 1.3 | -2.9 | -0.05 |
| money_level | early | pin $2k+ | 1-1 | 50.0 | -12.4 | -47.2 | -0.7 |
| money_level | early | pin limit <$1k | 32-32 | 50.0 | -2.0 | -6.9 | 0.24 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.1 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.6 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 172-161 | 51.7 | 2.5 | -0.8 | 0.31 |
| sharp_gap | early | pin $1-2k | 18-17 | 51.4 | -3.9 | -6.9 | -0.3 |
| sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.9 | -100.0 | 0.65 |
| sharp_gap | early | pin limit <$1k | 36-23 | 61.0 | 12.4 | 24.5 | 0.16 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.6 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 51.9 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 124-112 | 52.5 | 1.9 | -5.6 | 0.23 |
| money_moving | early | pin $1-2k | 8-13 | 38.1 | -18.9 | -47.8 | 0.36 |
| money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.4 | -8.4 | 0.65 |
| money_moving | early | pin limit <$1k | 33-11 | 75.0 | 25.2 | 53.4 | 0.38 |
| pin_value | early | 1-3k bets | 13-10 | 56.5 | 8.4 | 6.3 | -0.04 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.3 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 58-58 | 50.0 | 1.0 | -5.4 | 0.11 |
| pin_value | early | pin $1-2k | 19-30 | 38.8 | -8.5 | -27.1 | 0.19 |
| pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.3 | 83.3 | 0.0 |
| pin_value | early | pin limit <$1k | 53-39 | 57.6 | 7.9 | 9.1 | 0.05 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -50.5 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -27.3 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.0 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.4 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 288-337 | 46.1 | -3.6 | -12.5 | 0.42 |
| consensus_gap | early | pin $1-2k | 22-25 | 46.8 | -0.5 | -11.9 | 0.29 |
| consensus_gap | early | pin $2k+ | 1-1 | 50.0 | 12.4 | -8.4 | 0.65 |
| consensus_gap | early | pin limit <$1k | 26-38 | 40.6 | -9.5 | -17.9 | 0.24 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -53.3 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -1.9 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.8 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 5.5 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.3 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 7-4 | 63.6 | 14.4 | 19.4 | -0.09 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.1 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.8 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.5 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -0.6 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 6-5 | 54.5 | 8.5 | 1.3 | 0.27 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -1.3 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-7 | 50.0 | 3.0 | -6.4 | -0.29 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.6 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.6 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -19.9 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.9 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 3.6 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.6 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 22.8 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.3 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 22.8 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.4 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.4 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.4 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.4 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 53.3 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 11.4 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 17.9 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 16.0 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 16.0 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -28.5 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 53.3 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 53.3 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.3 | 83.3 | 1.0 |
| follow_move+rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -51.9 | -100.0 | -0.5 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.3 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.3 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 51.9 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.3 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.3 | 83.3 | 1.0 |
| rlm_quiet+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.3 | -100.0 | -1.0 |
| rlm_quiet+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.3 | -100.0 | -1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.3 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 39.5 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 50.5 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 42-53 | 44.2 | -9.3 | -22.0 | 0.85 |
| consensus_gap+money_level | early | <1k bets | 51-38 | 57.3 | -6.8 | -12.0 | -0.06 |
| consensus_gap+sharp_gap | early | <1k bets | 37-53 | 41.1 | -9.7 | -19.5 | 0.54 |
| follow_move+money_level | early | <1k bets | 102-51 | 66.7 | 6.7 | -1.3 | 0.03 |
| follow_move+sharp_gap | early | <1k bets | 87-53 | 62.1 | 12.6 | 13.0 | 0.53 |
| money_level+sharp_gap | early | <1k bets | 117-84 | 58.2 | 2.0 | -4.4 | 0.03 |
| follow_move+money_moving | early | <1k bets | 60-42 | 58.8 | 7.3 | 6.5 | 0.46 |
| money_level+money_moving | early | <1k bets | 71-51 | 58.2 | 0.7 | -5.6 | -0.05 |
| money_moving+sharp_gap | early | <1k bets | 71-68 | 51.1 | 2.8 | -3.5 | 0.45 |
| consensus_gap+money_moving | early | <1k bets | 20-24 | 45.5 | -5.8 | -27.0 | 0.59 |
| follow_move+pin_value | early | <1k bets | 18-16 | 52.9 | 3.3 | -0.3 | -0.1 |
| follow_move+rlm_quiet | early | <1k bets | 53-61 | 46.5 | 10.1 | 13.1 | 0.54 |
| money_moving+rlm_quiet | early | <1k bets | 18-18 | 50.0 | 12.8 | 22.1 | 0.69 |
| rlm_quiet+sharp_gap | early | <1k bets | 26-22 | 54.2 | 16.5 | 25.4 | 0.22 |
| follow_move+rlm_ratio | early | <1k bets | 33-29 | 53.2 | 14.5 | 20.8 | 0.52 |
| rlm_quiet+rlm_ratio | early | <1k bets | 23-17 | 57.5 | 20.7 | 36.2 | 0.16 |
| rlm_ratio+sharp_gap | early | <1k bets | 33-29 | 53.2 | 14.5 | 20.8 | 0.52 |
| pin_move+pin_value | early | <1k bets | 5-11 | 31.2 | -18.2 | -39.8 | 0.44 |
| follow_move+pin_move | early | <1k bets | 9-10 | 47.4 | -1.8 | -12.6 | 0.49 |
| consensus_gap+pin_value | early | <1k bets | 23-26 | 46.9 | -0.5 | -11.8 | 0.25 |
| pin_value+rlm_quiet | early | <1k bets | 0-3 | 0.0 | -43.8 | -100.0 | -0.6 |
| money_delta+money_moving | early | <1k bets | 11-11 | 50.0 | 11.9 | 19.5 | 1.02 |
| money_delta+sharp_gap | early | <1k bets | 10-9 | 52.6 | 15.2 | 28.3 | 1.18 |
| consensus_gap+pin_move | early | <1k bets | 2-6 | 25.0 | -21.9 | -51.7 | 0.29 |
| money_level+pin_move | early | <1k bets | 4-6 | 40.0 | -9.9 | -30.2 | 0.14 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -28.5 | -100.0 | -4.8 |
| consensus_gap+rlm_quiet | early | <1k bets | 4-6 | 40.0 | 3.1 | -12.2 | 1.03 |
| consensus_gap+rlm_ratio | early | <1k bets | 5-3 | 62.5 | 20.9 | 25.0 | 0.65 |
| follow_move+pin_rlm | early | <1k bets | 1-3 | 25.0 | -14.3 | -51.8 | -0.7 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -28.5 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | <1k bets | 0-1 | 0.0 | -28.5 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-3 | 25.0 | -14.3 | -51.8 | -0.7 |
| pin_rlm+sharp_gap | early | <1k bets | 1-4 | 20.0 | -17.1 | -61.5 | -0.3 |
| pin_value+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 24.2 | 27.3 | -0.93 |
| pin_value+sharp_gap | early | <1k bets | 6-8 | 42.9 | -7.2 | -18.2 | 0.42 |
| money_level+pin_value | early | <1k bets | 7-7 | 50.0 | -1.7 | -4.5 | 0.84 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -51.4 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -49.5 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 4-4 | 50.0 | -3.3 | -4.0 | 1.21 |
| money_level+rlm_ratio | early | <1k bets | 8-12 | 40.0 | -1.4 | -17.1 | 1.32 |
| money_moving+rlm_ratio | early | <1k bets | 16-11 | 59.3 | 19.0 | 39.9 | 0.95 |
| consensus_gap+money_delta | early | <1k bets | 2-0 | 100.0 | 50.0 | 90.9 | 0.5 |
| money_delta+money_level | early | <1k bets | 4-4 | 50.0 | 8.2 | 4.6 | 1.44 |
| pin_move+sharp_gap | early | <1k bets | 2-4 | 33.3 | -13.3 | -47.8 | 0.47 |
| money_level+pin_rlm | early | <1k bets | 1-2 | 33.3 | -9.5 | -35.8 | 0.67 |
| pin_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 21.5 | -3.7 | 0.25 |
| pin_move+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 21.5 | -3.7 | 0.25 |
| follow_move+money_delta | early | <1k bets | 6-5 | 54.5 | 16.5 | 52.8 | 1.28 |
| money_delta+rlm_quiet | early | <1k bets | 3-3 | 50.0 | 18.0 | 72.5 | 0.38 |
| money_delta+rlm_ratio | early | <1k bets | 5-3 | 62.5 | 26.1 | 86.2 | 2.04 |
| money_delta+pin_value | early | <1k bets | 2-0 | 100.0 | 50.5 | 90.9 | 0.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -28.5 | -100.0 | 1.3 |
| money_moving+pin_move | early | <1k bets | 1-1 | 50.0 | 0.5 | -2.4 | 1.0 |
| consensus_gap+money_level | early | pin $1-2k | 7-5 | 58.3 | -7.0 | -9.8 | 0.07 |
| consensus_gap+money_moving | early | pin $1-2k | 1-3 | 25.0 | -40.3 | -54.2 | 0.95 |
| consensus_gap+pin_value | early | pin $1-2k | 8-11 | 42.1 | -0.9 | -22.3 | 0.14 |
| follow_move+rlm_quiet | early | pin $1-2k | 3-7 | 30.0 | -1.0 | 7.2 | -0.12 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.6 | 29.7 | -1.02 |
| follow_move+sharp_gap | early | pin $1-2k | 9-6 | 60.0 | 2.8 | 19.2 | -0.62 |
| money_level+money_moving | early | pin $1-2k | 8-8 | 50.0 | -13.0 | -31.4 | 0.26 |
| money_level+pin_value | early | pin $1-2k | 2-4 | 33.3 | -18.6 | -37.6 | 0.78 |
| money_moving+pin_value | early | pin $1-2k | 1-4 | 20.0 | -34.8 | -63.3 | 0.94 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -9.7 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -9.7 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -10.6 | 29.7 | -1.02 |
| money_delta+money_level | early | pin $1-2k | 0-2 | 0.0 | -40.9 | -100.0 | 1.25 |
| money_delta+money_moving | early | pin $1-2k | 0-3 | 0.0 | -36.8 | -100.0 | 2.17 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -53.3 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-3 | 0.0 | -36.8 | -100.0 | 2.17 |
| money_level+sharp_gap | early | pin $1-2k | 15-9 | 62.5 | -0.9 | -4.8 | -0.23 |
| money_moving+sharp_gap | early | pin $1-2k | 4-10 | 28.6 | -27.6 | -61.0 | 0.36 |
| pin_value+sharp_gap | early | pin $1-2k | 1-4 | 20.0 | -30.7 | -61.8 | -0.22 |
| consensus_gap+follow_move | early | pin $1-2k | 6-7 | 46.2 | -2.2 | -11.3 | 0.4 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 1-3 | 25.0 | -3.5 | -35.0 | -0.65 |
| follow_move+pin_value | early | pin $1-2k | 6-8 | 42.9 | -5.1 | -20.8 | -0.24 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -28.5 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 12-6 | 66.7 | 3.1 | -0.4 | -0.03 |
| money_level+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -12.4 | -1.0 | 0.75 |
| follow_move+money_moving | early | pin $1-2k | 4-3 | 57.1 | -7.6 | -23.6 | -0.13 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -28.5 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -28.5 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 4-5 | 44.4 | -12.7 | -31.7 | -0.69 |
| follow_move+pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -28.5 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | pin $1-2k | 0-1 | 0.0 | -28.5 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-3 | 0.0 | -42.8 | -100.0 | -0.67 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -28.5 | -100.0 | -4.8 |
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -28.5 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -28.5 | -100.0 | 1.3 |
| pin_move+pin_value | early | pin $1-2k | 0-4 | 0.0 | -48.4 | -100.0 | 0.5 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -71.5 | -100.0 | 1.5 |
| follow_move+pin_move | early | pin $1-2k | 1-2 | 33.3 | -15.6 | -35.2 | -0.33 |
| money_level+pin_move | early | pin $1-2k | 1-0 | 100.0 | 53.3 | 94.3 | -1.0 |
| consensus_gap+money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.4 | -8.4 | 0.65 |
| consensus_gap+pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.3 | 83.3 | 0.0 |
| follow_move+money_level | early | pin $2k+ | 0-1 | 0.0 | -53.3 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.9 | -100.0 | 0.65 |
| follow_move+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.9 | -100.0 | 0.65 |
| money_level+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -53.3 | -100.0 | 0.0 |
| money_level+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -53.3 | -100.0 | 0.0 |
| money_moving+pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.3 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.9 | -100.0 | 0.65 |
| consensus_gap+follow_move | early | pin $2k+ | 0-1 | 0.0 | -28.5 | -100.0 | 1.3 |
| consensus_gap+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.5 | -100.0 | 1.3 |
| consensus_gap+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.5 | -100.0 | 1.3 |
| consensus_gap+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.5 | -100.0 | 1.3 |
| follow_move+money_moving | early | pin $2k+ | 0-1 | 0.0 | -28.5 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.5 | -100.0 | 1.3 |
| money_moving+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.5 | -100.0 | 1.3 |
| money_moving+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.5 | -100.0 | 1.3 |
| money_moving+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.5 | -100.0 | 1.3 |
| rlm_quiet+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.5 | -100.0 | 1.3 |
| rlm_quiet+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.5 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin limit <$1k | 6-9 | 40.0 | -5.4 | -19.3 | 0.28 |
| money_level+money_moving | early | pin limit <$1k | 18-7 | 72.0 | 20.5 | 34.3 | 0.42 |
| money_level+sharp_gap | early | pin limit <$1k | 26-20 | 56.5 | 6.6 | 4.5 | 0.22 |
| money_moving+sharp_gap | early | pin limit <$1k | 24-6 | 80.0 | 31.5 | 68.6 | 0.27 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -50.5 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 13-8 | 61.9 | 11.9 | 17.4 | 0.33 |
| money_moving+pin_value | early | pin limit <$1k | 11-4 | 73.3 | 23.7 | 39.0 | 0.27 |
| pin_value+sharp_gap | early | pin limit <$1k | 14-8 | 63.6 | 13.8 | 20.6 | 0.14 |
| consensus_gap+follow_move | early | pin limit <$1k | 7-10 | 41.2 | -10.1 | -23.2 | 0.41 |
| consensus_gap+money_level | early | pin limit <$1k | 6-7 | 46.2 | -8.3 | -19.0 | 0.31 |
| consensus_gap+pin_value | early | pin limit <$1k | 21-20 | 51.2 | 2.1 | -3.4 | 0.33 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 7-4 | 63.6 | 18.2 | 56.6 | 0.91 |
| follow_move+money_level | early | pin limit <$1k | 14-14 | 50.0 | -1.8 | -6.7 | -0.03 |
| follow_move+pin_value | early | pin limit <$1k | 19-15 | 55.9 | 6.6 | 5.6 | -0.12 |
| follow_move+sharp_gap | early | pin limit <$1k | 16-10 | 61.5 | 13.6 | 17.7 | -0.02 |
| follow_move+rlm_ratio | early | pin limit <$1k | 8-2 | 80.0 | 36.6 | 61.1 | 0.33 |
| money_level+rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.1 | 68.3 | 0.44 |
| pin_value+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.3 | 43.2 | -0.25 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 8-2 | 80.0 | 36.6 | 61.1 | 0.33 |
| consensus_gap+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 51.1 | 87.1 | 0.33 |
| consensus_gap+money_moving | early | pin limit <$1k | 10-3 | 76.9 | 29.2 | 76.9 | 0.65 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 1.9 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 51.1 | 87.1 | 0.33 |
| follow_move+money_moving | early | pin limit <$1k | 13-5 | 72.2 | 22.9 | 38.2 | 0.39 |
| money_delta+money_moving | early | pin limit <$1k | 4-0 | 100.0 | 50.9 | 88.0 | 0.0 |
| money_delta+pin_value | early | pin limit <$1k | 4-0 | 100.0 | 50.9 | 88.0 | 0.0 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 53.3 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 4-2 | 66.7 | 17.5 | 26.0 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 30.1 | 54.4 | -0.2 |
| money_delta+sharp_gap | early | pin limit <$1k | 3-0 | 100.0 | 50.2 | 89.6 | 0.0 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 10.5 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | 5.5 | 13.7 | -0.05 |
| pin_move+pin_value | early | pin limit <$1k | 5-8 | 38.5 | -11.2 | -25.9 | 0.54 |
| follow_move+pin_move | early | pin limit <$1k | 8-9 | 47.1 | -2.2 | -13.7 | 0.67 |
| consensus_gap+pin_move | early | pin limit <$1k | 2-4 | 33.3 | -19.7 | -35.7 | 0.43 |
| money_level+pin_move | early | pin limit <$1k | 3-6 | 33.3 | -17.0 | -44.0 | 0.27 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -49.5 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -49.5 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-4 | 33.3 | -13.3 | -47.8 | 0.47 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 21.5 | -3.7 | 0.25 |
| money_level+pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 21.5 | -3.7 | 0.25 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 21.5 | -3.7 | 0.25 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 21.5 | -3.7 | 0.25 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 21.5 | -3.7 | 0.25 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 21.5 | -3.7 | 0.25 |
| money_delta+money_level | early | pin limit <$1k | 2-0 | 100.0 | 50.5 | 90.9 | 0.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 50.5 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 50.5 | 90.9 | 1.0 |
| money_moving+pin_move | early | pin limit <$1k | 1-1 | 50.0 | 0.5 | -2.4 | 1.0 |
| pin_move+rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -49.5 | -100.0 | 1.0 |
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
| rlm_quiet | close | 1-3k bets | 70-112 | 38.5 | -4.4 | -11.7 |  |
| rlm_quiet | close | 3k+ bets | 31-46 | 40.3 | -2.4 | -16.0 |  |
| rlm_quiet | close | <1k bets | 10-19 | 34.5 | -8.5 | -33.2 |  |
| rlm_quiet | close | pin $1-2k | 32-52 | 38.1 | -6.2 | -20.5 |  |
| rlm_quiet | close | pin $2k+ | 39-49 | 44.3 | 3.9 | 9.6 |  |
| rlm_quiet | close | pin limit <$1k | 15-19 | 44.1 | -3.6 | -14.9 |  |
| pin_move | close | 1-3k bets | 132-139 | 48.7 | -0.3 | -2.4 |  |
| pin_move | close | 3k+ bets | 53-56 | 48.6 | -1.4 | -7.2 |  |
| pin_move | close | <1k bets | 20-19 | 51.3 | 1.6 | -3.3 |  |
| pin_move | close | pin $1-2k | 84-104 | 44.7 | -4.6 | -12.3 |  |
| pin_move | close | pin $2k+ | 85-80 | 51.5 | 2.0 | 2.7 |  |
| pin_move | close | pin limit <$1k | 36-33 | 52.2 | 2.8 | -0.1 |  |
| money_delta | close | 1-3k bets | 59-84 | 41.3 | -2.5 | -16.2 |  |
| money_delta | close | 3k+ bets | 27-31 | 46.6 | 2.2 | -8.0 |  |
| money_delta | close | <1k bets | 14-14 | 50.0 | 5.5 | 11.4 |  |
| money_delta | close | pin $1-2k | 40-38 | 51.3 | 5.0 | 5.4 |  |
| money_delta | close | pin $2k+ | 24-29 | 45.3 | 4.2 | -8.2 |  |
| money_delta | close | pin limit <$1k | 12-19 | 38.7 | -8.5 | -25.5 |  |
| pin_rlm | close | 1-3k bets | 27-41 | 39.7 | -1.7 | -14.1 |  |
| pin_rlm | close | 3k+ bets | 10-17 | 37.0 | -4.3 | -23.2 |  |
| pin_rlm | close | <1k bets | 5-5 | 50.0 | 2.5 | -4.9 |  |
| pin_rlm | close | pin $1-2k | 18-26 | 40.9 | -2.9 | -14.8 |  |
| pin_rlm | close | pin $2k+ | 16-25 | 39.0 | 1.8 | -12.8 |  |
| pin_rlm | close | pin limit <$1k | 8-12 | 40.0 | -7.5 | -23.0 |  |
| follow_move | close | 1-3k bets | 204-238 | 46.2 | -2.9 | -9.9 |  |
| follow_move | close | 3k+ bets | 81-78 | 50.9 | 2.1 | -5.2 |  |
| follow_move | close | <1k bets | 44-46 | 48.9 | -0.9 | -13.1 |  |
| follow_move | close | pin $1-2k | 98-126 | 43.8 | -5.4 | -17.1 |  |
| follow_move | close | pin $2k+ | 100-99 | 50.3 | 1.5 | 1.3 |  |
| follow_move | close | pin limit <$1k | 44-41 | 51.8 | 2.1 | -1.8 |  |
| rlm_ratio | close | 1-3k bets | 46-77 | 37.4 | -4.8 | -20.6 |  |
| rlm_ratio | close | 3k+ bets | 15-28 | 34.9 | -7.1 | -27.5 |  |
| rlm_ratio | close | <1k bets | 10-12 | 45.5 | 1.2 | -12.8 |  |
| rlm_ratio | close | pin $1-2k | 25-33 | 43.1 | -1.0 | -11.2 |  |
| rlm_ratio | close | pin $2k+ | 15-27 | 35.7 | -1.4 | -21.1 |  |
| rlm_ratio | close | pin limit <$1k | 10-17 | 37.0 | -10.7 | -28.9 |  |
| money_level | close | 1-3k bets | 268-206 | 56.5 | 1.4 | -3.7 |  |
| money_level | close | 3k+ bets | 96-88 | 52.2 | -2.6 | -10.3 |  |
| money_level | close | <1k bets | 60-31 | 65.9 | 11.0 | 9.2 |  |
| money_level | close | pin $1-2k | 125-118 | 51.4 | -2.0 | -9.9 |  |
| money_level | close | pin $2k+ | 109-102 | 51.7 | -5.0 | -14.5 |  |
| money_level | close | pin limit <$1k | 54-37 | 59.3 | 7.8 | 12.1 |  |
| sharp_gap | close | 1-3k bets | 206-239 | 46.3 | -2.1 | -11.4 |  |
| sharp_gap | close | 3k+ bets | 72-102 | 41.4 | -6.8 | -20.0 |  |
| sharp_gap | close | <1k bets | 46-39 | 54.1 | 4.8 | -0.8 |  |
| sharp_gap | close | pin $1-2k | 106-120 | 46.9 | -1.8 | -9.7 |  |
| sharp_gap | close | pin $2k+ | 87-114 | 43.3 | -4.4 | -14.7 |  |
| sharp_gap | close | pin limit <$1k | 38-47 | 44.7 | -4.8 | -14.6 |  |
| money_moving | close | 1-3k bets | 216-234 | 48.0 | -0.7 | -8.5 |  |
| money_moving | close | 3k+ bets | 75-100 | 42.9 | -6.1 | -19.2 |  |
| money_moving | close | <1k bets | 46-37 | 55.4 | 6.0 | 1.5 |  |
| money_moving | close | pin $1-2k | 111-116 | 48.9 | -0.4 | -7.0 |  |
| money_moving | close | pin $2k+ | 91-111 | 45.0 | -2.7 | -12.0 |  |
| money_moving | close | pin limit <$1k | 42-48 | 46.7 | -2.9 | -10.9 |  |
| pin_value | close | 1-3k bets | 111-93 | 54.4 | 4.7 | 8.3 |  |
| pin_value | close | 3k+ bets | 25-45 | 35.7 | -14.9 | -32.2 |  |
| pin_value | close | <1k bets | 18-14 | 56.2 | 9.1 | 17.6 |  |
| pin_value | close | pin $1-2k | 72-72 | 50.0 | 0.6 | -1.6 |  |
| pin_value | close | pin $2k+ | 47-52 | 47.5 | -1.9 | -0.4 |  |
| pin_value | close | pin limit <$1k | 37-29 | 56.1 | 5.5 | 6.6 |  |
| consensus_gap | close | 1-3k bets | 86-71 | 54.8 | 2.3 | 0.1 |  |
| consensus_gap | close | 3k+ bets | 33-28 | 54.1 | -0.6 | -8.2 |  |
| consensus_gap | close | <1k bets | 18-8 | 69.2 | 18.5 | 29.9 |  |
| consensus_gap | close | pin $1-2k | 31-29 | 51.7 | -0.4 | 3.6 |  |
| consensus_gap | close | pin $2k+ | 59-29 | 67.0 | 10.5 | 20.1 |  |
| consensus_gap | close | pin limit <$1k | 10-13 | 43.5 | -5.3 | -17.1 |  |
| follow_move+pin_move | close | 1-3k bets | 85-113 | 42.9 | -5.7 | -15.7 |  |
| money_delta+money_moving | close | 1-3k bets | 48-64 | 42.9 | 0.4 | -11.8 |  |
| money_delta+sharp_gap | close | 1-3k bets | 48-63 | 43.2 | 0.8 | -11.0 |  |
| money_moving+sharp_gap | close | 1-3k bets | 200-225 | 47.1 | -1.5 | -9.5 |  |
| consensus_gap+money_level | close | 1-3k bets | 54-38 | 58.7 | 0.4 | -7.1 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 70-112 | 38.5 | -4.4 | -11.7 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 32-53 | 37.6 | -6.2 | -16.7 |  |
| consensus_gap+follow_move | close | 1-3k bets | 21-26 | 44.7 | -5.4 | -17.0 |  |
| follow_move+money_level | close | 1-3k bets | 101-88 | 53.4 | -1.5 | -7.5 |  |
| money_level+money_moving | close | 1-3k bets | 151-133 | 53.2 | 0.6 | -4.3 |  |
| money_level+sharp_gap | close | 1-3k bets | 143-133 | 51.8 | -0.6 | -6.4 |  |
| consensus_gap+money_moving | close | 1-3k bets | 26-36 | 41.9 | -8.3 | -19.3 |  |
| consensus_gap+pin_move | close | 1-3k bets | 23-14 | 62.2 | 13.1 | 36.6 |  |
| consensus_gap+pin_value | close | 1-3k bets | 29-28 | 50.9 | 2.0 | -3.6 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 26-38 | 40.6 | -9.3 | -22.0 |  |
| follow_move+money_moving | close | 1-3k bets | 107-132 | 44.8 | -3.4 | -13.1 |  |
| follow_move+pin_value | close | 1-3k bets | 35-28 | 55.6 | 5.3 | 20.5 |  |
| follow_move+sharp_gap | close | 1-3k bets | 107-135 | 44.2 | -3.9 | -14.4 |  |
| money_level+pin_move | close | 1-3k bets | 60-50 | 54.5 | 1.3 | -2.2 |  |
| money_level+pin_value | close | 1-3k bets | 47-41 | 53.4 | 3.0 | 0.1 |  |
| money_moving+pin_move | close | 1-3k bets | 65-64 | 50.4 | 2.4 | -1.2 |  |
| money_moving+pin_value | close | 1-3k bets | 41-42 | 49.4 | -0.2 | -6.8 |  |
| pin_move+pin_value | close | 1-3k bets | 40-39 | 50.6 | -0.6 | -4.2 |  |
| pin_move+sharp_gap | close | 1-3k bets | 62-70 | 47.0 | -0.6 | -7.8 |  |
| pin_value+sharp_gap | close | 1-3k bets | 40-45 | 47.1 | -2.7 | -11.3 |  |
| follow_move+money_delta | close | 1-3k bets | 32-56 | 36.4 | -7.4 | -26.1 |  |
| money_delta+pin_move | close | 1-3k bets | 22-27 | 44.9 | 1.5 | -11.2 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 16-40 | 28.6 | -13.1 | -39.1 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 46-77 | 37.4 | -4.8 | -20.6 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 30-58 | 34.1 | -6.8 | -23.3 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 45-71 | 38.8 | -3.6 | -17.4 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 21-54 | 28.0 | -12.0 | -34.8 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 29-61 | 32.2 | -8.8 | -27.9 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 46-77 | 37.4 | -4.8 | -20.6 |  |
| money_delta+money_level | close | 1-3k bets | 18-16 | 52.9 | 5.6 | 3.9 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 5-12 | 29.4 | -9.0 | -31.8 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 7-8 | 46.7 | 6.1 | 1.9 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 23-45 | 33.8 | -8.0 | -29.6 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 5-3 | 62.5 | 20.3 | 47.4 |  |
| money_level+pin_rlm | close | 1-3k bets | 10-10 | 50.0 | 4.5 | -2.2 |  |
| money_moving+pin_rlm | close | 1-3k bets | 27-36 | 42.9 | 1.0 | -7.3 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 27-41 | 39.7 | -1.7 | -14.1 |  |
| money_level+rlm_ratio | close | 1-3k bets | 20-18 | 52.6 | 6.2 | 2.2 |  |
| consensus_gap+money_delta | close | 1-3k bets | 8-6 | 57.1 | 16.4 | 14.0 |  |
| follow_move+pin_rlm | close | 1-3k bets | 22-35 | 38.6 | -2.5 | -15.6 |  |
| money_delta+pin_rlm | close | 1-3k bets | 15-22 | 40.5 | -0.1 | -18.4 |  |
| pin_move+pin_rlm | close | 1-3k bets | 26-35 | 42.6 | 0.8 | -8.1 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 23-32 | 41.8 | -0.4 | -10.0 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 11-26 | 29.7 | -9.5 | -27.7 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 22-35 | 38.6 | -2.5 | -15.6 |  |
| money_delta+pin_value | close | 1-3k bets | 13-7 | 65.0 | 17.5 | 25.6 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 8-10 | 44.4 | -2.7 | 41.6 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 5-5 | 50.0 | 2.1 | -1.2 |  |
| pin_rlm+pin_value | close | 1-3k bets | 4-6 | 40.0 | -8.2 | -19.3 |  |
| money_level+money_moving | close | 3k+ bets | 44-54 | 44.9 | -8.1 | -19.1 |  |
| money_level+sharp_gap | close | 3k+ bets | 40-54 | 42.6 | -9.8 | -20.8 |  |
| money_moving+sharp_gap | close | 3k+ bets | 71-98 | 42.0 | -6.5 | -19.2 |  |
| follow_move+money_delta | close | 3k+ bets | 12-19 | 38.7 | -4.6 | -23.1 |  |
| follow_move+money_level | close | 3k+ bets | 35-27 | 56.5 | 0.5 | -7.8 |  |
| follow_move+money_moving | close | 3k+ bets | 42-49 | 46.2 | -2.3 | -14.7 |  |
| follow_move+pin_move | close | 3k+ bets | 41-42 | 49.4 | 0.2 | -5.3 |  |
| follow_move+pin_rlm | close | 3k+ bets | 9-15 | 37.5 | -3.0 | -21.4 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 15-28 | 34.9 | -7.1 | -27.5 |  |
| follow_move+sharp_gap | close | 3k+ bets | 39-48 | 44.8 | -2.6 | -13.2 |  |
| money_delta+money_level | close | 3k+ bets | 5-8 | 38.5 | -10.7 | -25.7 |  |
| money_delta+money_moving | close | 3k+ bets | 18-25 | 41.9 | -1.4 | -16.4 |  |
| money_delta+pin_move | close | 3k+ bets | 9-11 | 45.0 | -1.2 | -12.4 |  |
| money_delta+pin_rlm | close | 3k+ bets | 6-8 | 42.9 | -0.5 | -13.1 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 7-12 | 36.8 | -4.6 | -25.5 |  |
| money_delta+sharp_gap | close | 3k+ bets | 18-25 | 41.9 | -1.4 | -16.4 |  |
| money_level+pin_move | close | 3k+ bets | 19-24 | 44.2 | -11.9 | -24.9 |  |
| money_level+pin_rlm | close | 3k+ bets | 1-2 | 33.3 | -17.0 | -34.9 |  |
| money_level+rlm_ratio | close | 3k+ bets | 3-3 | 50.0 | -0.6 | -3.8 |  |
| money_moving+pin_move | close | 3k+ bets | 23-32 | 41.8 | -8.1 | -22.1 |  |
| money_moving+pin_rlm | close | 3k+ bets | 10-16 | 38.5 | -3.2 | -20.2 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 14-28 | 33.3 | -8.9 | -32.2 |  |
| pin_move+pin_rlm | close | 3k+ bets | 8-14 | 36.4 | -6.9 | -27.3 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 8-14 | 36.4 | -6.8 | -27.2 |  |
| pin_move+sharp_gap | close | 3k+ bets | 21-32 | 39.6 | -9.6 | -23.6 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 9-15 | 37.5 | -3.0 | -21.4 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 10-17 | 37.0 | -4.3 | -23.2 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 15-28 | 34.9 | -7.1 | -27.5 |  |
| consensus_gap+money_level | close | 3k+ bets | 25-16 | 61.0 | 1.1 | -0.6 |  |
| consensus_gap+money_moving | close | 3k+ bets | 13-19 | 40.6 | -11.2 | -28.6 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 12-20 | 37.5 | -13.2 | -32.2 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 31-46 | 40.3 | -2.4 | -16.0 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 19-23 | 45.2 | 2.3 | -4.5 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 8-13 | 38.1 | -3.4 | -23.1 |  |
| money_level+pin_value | close | 3k+ bets | 14-26 | 35.0 | -16.7 | -34.1 |  |
| money_moving+pin_value | close | 3k+ bets | 13-24 | 35.1 | -16.5 | -33.9 |  |
| pin_value+sharp_gap | close | 3k+ bets | 13-25 | 34.2 | -17.9 | -35.6 |  |
| consensus_gap+follow_move | close | 3k+ bets | 12-9 | 57.1 | 5.0 | -5.8 |  |
| consensus_gap+pin_value | close | 3k+ bets | 10-11 | 47.6 | -4.4 | -9.4 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 16-28 | 36.4 | -6.9 | -27.4 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 17-27 | 38.6 | -4.3 | -21.2 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 6-14 | 30.0 | -9.6 | -36.6 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 10-24 | 29.4 | -11.3 | -37.8 |  |
| pin_move+pin_value | close | 3k+ bets | 16-22 | 42.1 | -9.1 | -20.1 |  |
| follow_move+pin_value | close | 3k+ bets | 11-15 | 42.3 | -8.2 | -19.8 |  |
| consensus_gap+money_delta | close | 3k+ bets | 3-4 | 42.9 | -1.9 | -18.6 |  |
| consensus_gap+pin_move | close | 3k+ bets | 13-9 | 59.1 | 7.1 | 4.0 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 3-4 | 42.9 | -0.2 | -17.6 |  |
| money_delta+pin_value | close | 3k+ bets | 4-4 | 50.0 | -3.4 | -4.5 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 3-6 | 33.3 | -16.8 | -37.1 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 2-4 | 33.3 | -12.9 | -36.9 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 1-4 | 20.0 | -19.6 | -61.8 |  |
| pin_rlm+pin_value | close | 3k+ bets | 2-3 | 40.0 | -11.9 | -24.3 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 1-2 | 33.3 | -15.9 | -36.4 |  |
| consensus_gap+money_level | close | <1k bets | 13-1 | 92.9 | 35.1 | 48.5 |  |
| consensus_gap+money_moving | close | <1k bets | 8-1 | 88.9 | 35.7 | 81.0 |  |
| consensus_gap+pin_value | close | <1k bets | 5-2 | 71.4 | 28.9 | 85.8 |  |
| consensus_gap+sharp_gap | close | <1k bets | 9-2 | 81.8 | 29.2 | 60.9 |  |
| follow_move+pin_move | close | <1k bets | 14-15 | 48.3 | -1.8 | -9.0 |  |
| follow_move+rlm_quiet | close | <1k bets | 10-19 | 34.5 | -8.5 | -33.2 |  |
| money_level+money_moving | close | <1k bets | 34-18 | 65.4 | 12.2 | 10.0 |  |
| money_level+pin_value | close | <1k bets | 8-4 | 66.7 | 18.5 | 24.9 |  |
| money_level+sharp_gap | close | <1k bets | 34-19 | 64.2 | 10.7 | 8.1 |  |
| money_moving+pin_value | close | <1k bets | 6-5 | 54.5 | 9.8 | 36.2 |  |
| money_moving+sharp_gap | close | <1k bets | 44-36 | 55.0 | 6.0 | 2.4 |  |
| pin_move+rlm_quiet | close | <1k bets | 3-4 | 42.9 | -5.7 | -18.6 |  |
| pin_value+sharp_gap | close | <1k bets | 6-5 | 54.5 | 9.8 | 36.2 |  |
| follow_move+money_moving | close | <1k bets | 22-18 | 55.0 | 5.7 | -3.6 |  |
| follow_move+sharp_gap | close | <1k bets | 21-19 | 52.5 | 3.2 | -5.9 |  |
| money_level+pin_move | close | <1k bets | 14-9 | 60.9 | 10.5 | 14.1 |  |
| money_moving+rlm_quiet | close | <1k bets | 5-7 | 41.7 | -1.3 | -19.1 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 5-7 | 41.7 | -1.3 | -19.1 |  |
| follow_move+money_delta | close | <1k bets | 8-9 | 47.1 | 1.6 | -10.3 |  |
| follow_move+pin_rlm | close | <1k bets | 4-5 | 44.4 | -3.1 | -15.5 |  |
| follow_move+pin_value | close | <1k bets | 5-3 | 62.5 | 13.1 | 19.9 |  |
| follow_move+rlm_ratio | close | <1k bets | 10-12 | 45.5 | 1.2 | -12.8 |  |
| money_delta+money_moving | close | <1k bets | 9-11 | 45.0 | 2.8 | 8.2 |  |
| money_delta+pin_move | close | <1k bets | 1-3 | 25.0 | -22.6 | -52.3 |  |
| money_delta+pin_rlm | close | <1k bets | 1-3 | 25.0 | -22.6 | -52.3 |  |
| money_delta+pin_value | close | <1k bets | 4-0 | 100.0 | 56.2 | 181.8 |  |
| money_delta+rlm_quiet | close | <1k bets | 5-4 | 55.6 | 12.0 | 7.3 |  |
| money_delta+rlm_ratio | close | <1k bets | 5-7 | 41.7 | -1.9 | -20.7 |  |
| money_delta+sharp_gap | close | <1k bets | 9-11 | 45.0 | 2.8 | 8.2 |  |
| money_moving+pin_move | close | <1k bets | 11-9 | 55.0 | 7.2 | 4.3 |  |
| money_moving+pin_rlm | close | <1k bets | 5-5 | 50.0 | 2.5 | -4.9 |  |
| money_moving+rlm_ratio | close | <1k bets | 10-12 | 45.5 | 1.2 | -12.8 |  |
| pin_move+pin_rlm | close | <1k bets | 5-5 | 50.0 | 2.5 | -4.9 |  |
| pin_move+pin_value | close | <1k bets | 7-4 | 63.6 | 14.3 | 20.8 |  |
| pin_move+rlm_ratio | close | <1k bets | 4-5 | 44.4 | -3.1 | -15.5 |  |
| pin_move+sharp_gap | close | <1k bets | 11-9 | 55.0 | 7.2 | 4.3 |  |
| pin_rlm+pin_value | close | <1k bets | 2-0 | 100.0 | 52.4 | 90.9 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 2-1 | 66.7 | 17.5 | 26.2 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 4-5 | 44.4 | -3.1 | -15.5 |  |
| pin_rlm+sharp_gap | close | <1k bets | 5-5 | 50.0 | 2.5 | -4.9 |  |
| pin_value+rlm_quiet | close | <1k bets | 3-0 | 100.0 | 52.4 | 90.9 |  |
| pin_value+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 52.4 | 90.9 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 5-6 | 45.5 | 2.9 | -11.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 10-12 | 45.5 | 1.2 | -12.8 |  |
| consensus_gap+follow_move | close | <1k bets | 5-1 | 83.3 | 28.4 | 42.8 |  |
| consensus_gap+pin_move | close | <1k bets | 2-0 | 100.0 | 42.6 | 70.5 |  |
| follow_move+money_level | close | <1k bets | 24-13 | 64.9 | 9.6 | 7.3 |  |
| money_delta+money_level | close | <1k bets | 3-3 | 50.0 | 8.0 | 7.7 |  |
| money_level+pin_rlm | close | <1k bets | 2-3 | 40.0 | -6.5 | -23.6 |  |
| money_level+rlm_ratio | close | <1k bets | 4-4 | 50.0 | 5.4 | -5.5 |  |
| consensus_gap+money_delta | close | <1k bets | 3-0 | 100.0 | 50.8 | 208.0 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 52.4 | 89.3 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-1 | 50.0 | 9.9 | -4.5 |  |
| money_delta+money_moving | close | pin $1-2k | 25-25 | 50.0 | 5.7 | 6.8 |  |
| money_delta+sharp_gap | close | pin $1-2k | 25-25 | 50.0 | 5.7 | 6.8 |  |
| money_moving+sharp_gap | close | pin $1-2k | 103-111 | 48.1 | -0.8 | -7.1 |  |
| consensus_gap+follow_move | close | pin $1-2k | 9-11 | 45.0 | -5.7 | -16.3 |  |
| consensus_gap+money_level | close | pin $1-2k | 17-15 | 53.1 | -3.2 | -11.9 |  |
| consensus_gap+money_moving | close | pin $1-2k | 8-13 | 38.1 | -11.4 | -15.4 |  |
| consensus_gap+pin_move | close | pin $1-2k | 11-11 | 50.0 | 1.4 | 10.9 |  |
| consensus_gap+pin_value | close | pin $1-2k | 16-15 | 51.6 | 3.2 | 10.3 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 8-13 | 38.1 | -11.4 | -14.1 |  |
| follow_move+money_level | close | pin $1-2k | 48-52 | 48.0 | -5.3 | -15.7 |  |
| follow_move+money_moving | close | pin $1-2k | 55-66 | 45.5 | -3.3 | -13.6 |  |
| follow_move+pin_move | close | pin $1-2k | 52-86 | 37.7 | -11.0 | -26.4 |  |
| follow_move+pin_value | close | pin $1-2k | 25-27 | 48.1 | -1.5 | -8.7 |  |
| follow_move+sharp_gap | close | pin $1-2k | 56-69 | 44.8 | -4.0 | -14.6 |  |
| money_level+money_moving | close | pin $1-2k | 77-75 | 50.7 | -1.2 | -9.3 |  |
| money_level+pin_move | close | pin $1-2k | 38-47 | 44.7 | -7.1 | -19.0 |  |
| money_level+pin_value | close | pin $1-2k | 32-32 | 50.0 | 0.1 | -6.7 |  |
| money_level+sharp_gap | close | pin $1-2k | 72-76 | 48.6 | -2.8 | -11.7 |  |
| money_moving+pin_move | close | pin $1-2k | 44-49 | 47.3 | -2.0 | -9.2 |  |
| money_moving+pin_value | close | pin $1-2k | 25-27 | 48.1 | -0.6 | -2.3 |  |
| pin_move+pin_value | close | pin $1-2k | 27-34 | 44.3 | -6.5 | -16.2 |  |
| pin_move+sharp_gap | close | pin $1-2k | 43-55 | 43.9 | -4.6 | -15.0 |  |
| pin_value+sharp_gap | close | pin $1-2k | 25-27 | 48.1 | -0.6 | -2.3 |  |
| follow_move+money_delta | close | pin $1-2k | 20-27 | 42.6 | -3.7 | -16.6 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 32-52 | 38.1 | -6.2 | -20.5 |  |
| money_delta+pin_move | close | pin $1-2k | 15-17 | 46.9 | 1.2 | -7.6 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 11-17 | 39.3 | -5.7 | -22.3 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 22-33 | 40.0 | -5.2 | -15.7 |  |
| follow_move+pin_rlm | close | pin $1-2k | 16-23 | 41.0 | -3.3 | -13.9 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 25-33 | 43.1 | -1.0 | -11.2 |  |
| pin_move+pin_rlm | close | pin $1-2k | 18-23 | 43.9 | -0.7 | -8.5 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 16-22 | 42.1 | -3.0 | -11.7 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 10-17 | 37.0 | -6.7 | -18.7 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 16-23 | 41.0 | -3.3 | -13.9 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 18-26 | 40.9 | -2.9 | -14.8 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 13-22 | 37.1 | -6.0 | -20.1 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 17-25 | 40.5 | -3.2 | -15.0 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 25-33 | 43.1 | -1.0 | -11.2 |  |
| money_delta+money_level | close | pin $1-2k | 11-11 | 50.0 | 2.4 | -2.9 |  |
| money_delta+pin_rlm | close | pin $1-2k | 10-12 | 45.5 | 1.9 | -9.2 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 12-15 | 44.4 | 0.2 | -11.6 |  |
| money_level+pin_rlm | close | pin $1-2k | 6-7 | 46.2 | 1.5 | -10.0 |  |
| money_level+rlm_ratio | close | pin $1-2k | 9-9 | 50.0 | 4.4 | -3.6 |  |
| money_moving+pin_rlm | close | pin $1-2k | 18-21 | 46.2 | 1.3 | -3.8 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 25-29 | 46.3 | 1.7 | -4.6 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 17-24 | 41.5 | -2.1 | -12.9 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 2-4 | 33.3 | -6.5 | -28.5 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 6-10 | 37.5 | -10.5 | -24.9 |  |
| money_delta+pin_value | close | pin $1-2k | 9-6 | 60.0 | 14.3 | 41.1 |  |
| consensus_gap+money_delta | close | pin $1-2k | 4-1 | 80.0 | 37.4 | 132.7 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 1-2 | 33.3 | -6.0 | -20.7 |  |
| pin_rlm+pin_value | close | pin $1-2k | 4-5 | 44.4 | -3.5 | -10.4 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 3-4 | 42.9 | -4.0 | -12.0 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 1-1 | 50.0 | 7.4 | 19.0 |  |
| follow_move+pin_move | close | pin $2k+ | 64-65 | 49.6 | 0.5 | -3.8 |  |
| consensus_gap+money_level | close | pin $2k+ | 39-22 | 63.9 | 2.7 | -0.7 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 39-49 | 44.3 | 3.9 | 9.6 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 26-37 | 41.3 | -0.4 | -7.0 |  |
| money_level+money_moving | close | pin $2k+ | 56-66 | 45.9 | -7.1 | -17.5 |  |
| money_level+sharp_gap | close | pin $2k+ | 53-68 | 43.8 | -9.0 | -19.8 |  |
| money_moving+sharp_gap | close | pin $2k+ | 87-110 | 44.2 | -3.5 | -12.9 |  |
| consensus_gap+pin_value | close | pin $2k+ | 21-14 | 60.0 | 10.2 | 13.1 |  |
| follow_move+money_level | close | pin $2k+ | 39-36 | 52.0 | -5.9 | -15.8 |  |
| follow_move+money_moving | close | pin $2k+ | 44-56 | 44.0 | -3.5 | -15.6 |  |
| follow_move+sharp_gap | close | pin $2k+ | 40-55 | 42.1 | -5.1 | -17.7 |  |
| money_level+pin_move | close | pin $2k+ | 31-25 | 55.4 | -3.0 | -8.1 |  |
| money_moving+pin_move | close | pin $2k+ | 35-40 | 46.7 | -0.6 | -8.9 |  |
| pin_move+sharp_gap | close | pin $2k+ | 34-41 | 45.3 | -2.0 | -10.4 |  |
| money_delta+money_level | close | pin $2k+ | 6-4 | 60.0 | 15.4 | 22.1 |  |
| money_delta+money_moving | close | pin $2k+ | 20-29 | 40.8 | 1.0 | -16.5 |  |
| money_delta+sharp_gap | close | pin $2k+ | 20-29 | 40.8 | 1.0 | -16.5 |  |
| consensus_gap+money_moving | close | pin $2k+ | 19-19 | 50.0 | -3.1 | -1.9 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 18-20 | 47.4 | -5.8 | -5.0 |  |
| money_level+pin_value | close | pin $2k+ | 16-27 | 37.2 | -13.4 | -30.7 |  |
| money_moving+pin_value | close | pin $2k+ | 18-28 | 39.1 | -11.5 | -26.8 |  |
| pin_value+sharp_gap | close | pin $2k+ | 18-30 | 37.5 | -13.8 | -29.9 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 5-4 | 55.6 | 10.9 | 24.4 |  |
| money_level+pin_rlm | close | pin $2k+ | 2-4 | 33.3 | -12.8 | -32.5 |  |
| money_moving+pin_rlm | close | pin $2k+ | 16-24 | 40.0 | 2.7 | -10.6 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 16-25 | 39.0 | 1.8 | -12.8 |  |
| follow_move+money_delta | close | pin $2k+ | 11-18 | 37.9 | -1.7 | -23.7 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 15-27 | 35.7 | -1.4 | -21.1 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 7-17 | 29.2 | -8.4 | -40.0 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 15-27 | 35.7 | -1.4 | -21.1 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 15-27 | 35.7 | -1.4 | -21.1 |  |
| money_level+rlm_ratio | close | pin $2k+ | 5-5 | 50.0 | 5.7 | -3.5 |  |
| consensus_gap+follow_move | close | pin $2k+ | 17-7 | 70.8 | 14.0 | 20.6 |  |
| consensus_gap+pin_move | close | pin $2k+ | 23-8 | 74.2 | 21.7 | 44.2 |  |
| follow_move+pin_value | close | pin $2k+ | 12-12 | 50.0 | -1.2 | 34.4 |  |
| pin_move+pin_value | close | pin $2k+ | 21-20 | 51.2 | -0.7 | -3.4 |  |
| follow_move+pin_rlm | close | pin $2k+ | 12-21 | 36.4 | 1.2 | -16.5 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 12-21 | 36.4 | 1.2 | -16.5 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 4-3 | 57.1 | 9.0 | 146.6 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 15-25 | 37.5 | -0.6 | -15.5 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 14-24 | 36.8 | -1.5 | -17.9 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 7-14 | 33.3 | -4.5 | -31.8 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 8-20 | 28.6 | -5.5 | -31.3 |  |
| money_delta+pin_move | close | pin $2k+ | 13-14 | 48.1 | 6.3 | -5.2 |  |
| money_delta+pin_rlm | close | pin $2k+ | 9-14 | 39.1 | 0.9 | -19.8 |  |
| pin_move+pin_rlm | close | pin $2k+ | 13-19 | 40.6 | 3.2 | -10.4 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 12-18 | 40.0 | 2.3 | -13.1 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 8-18 | 30.8 | -3.4 | -26.0 |  |
| consensus_gap+money_delta | close | pin $2k+ | 5-2 | 71.4 | 23.3 | 37.7 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 3-3 | 50.0 | 10.9 | 20.3 |  |
| money_delta+pin_value | close | pin $2k+ | 6-3 | 66.7 | 13.0 | 26.6 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 4-2 | 66.7 | 25.7 | 51.1 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 2-0 | 100.0 | 48.3 | 87.8 |  |
| pin_rlm+pin_value | close | pin $2k+ | 3-1 | 75.0 | 21.2 | 42.4 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 5-5 | 50.0 | 2.5 | -4.0 |  |
| consensus_gap+money_level | close | pin limit <$1k | 6-6 | 50.0 | -2.0 | -5.5 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 6-10 | 37.5 | -10.6 | -28.1 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 8-12 | 40.0 | -9.5 | -24.2 |  |
| follow_move+money_level | close | pin limit <$1k | 26-18 | 59.1 | 8.0 | 11.0 |  |
| follow_move+money_moving | close | pin limit <$1k | 24-28 | 46.2 | -3.2 | -11.6 |  |
| follow_move+pin_value | close | pin limit <$1k | 14-8 | 63.6 | 12.8 | 21.1 |  |
| money_level+money_moving | close | pin limit <$1k | 31-27 | 53.4 | 2.5 | 1.8 |  |
| money_level+pin_value | close | pin limit <$1k | 21-13 | 61.8 | 9.9 | 17.4 |  |
| money_moving+pin_value | close | pin limit <$1k | 17-17 | 50.0 | -0.3 | -5.0 |  |
| follow_move+pin_move | close | pin limit <$1k | 24-22 | 52.2 | 3.0 | 0.3 |  |
| money_level+pin_move | close | pin limit <$1k | 24-14 | 63.2 | 12.6 | 20.6 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 37-44 | 45.7 | -3.8 | -12.8 |  |
| pin_move+pin_value | close | pin limit <$1k | 15-12 | 55.6 | 5.3 | 6.1 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 15-19 | 44.1 | -3.6 | -14.9 |  |
| money_moving+pin_move | close | pin limit <$1k | 20-19 | 51.3 | 2.2 | -1.8 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 3-2 | 60.0 | 15.4 | 16.4 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 4-4 | 50.0 | 3.1 | -3.4 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 1-2 | 33.3 | -9.3 | -33.3 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 3-3 | 50.0 | 4.9 | -3.0 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 2-3 | 40.0 | -4.6 | -21.8 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 6-11 | 35.3 | -12.8 | -32.3 |  |
| follow_move+money_delta | close | pin limit <$1k | 6-12 | 33.3 | -13.7 | -35.8 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 7-11 | 38.9 | -8.7 | -25.0 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 10-17 | 37.0 | -10.7 | -28.9 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 23-27 | 46.0 | -3.3 | -12.0 |  |
| money_delta+money_moving | close | pin limit <$1k | 9-14 | 39.1 | -8.0 | -24.5 |  |
| money_delta+pin_move | close | pin limit <$1k | 4-10 | 28.6 | -17.9 | -44.5 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 3-7 | 30.0 | -16.1 | -41.4 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 3-5 | 37.5 | -8.2 | -27.3 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 5-11 | 31.2 | -15.7 | -39.8 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 9-14 | 39.1 | -8.0 | -24.5 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 8-12 | 40.0 | -7.5 | -23.0 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 4-11 | 26.7 | -20.5 | -48.5 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 9-16 | 36.0 | -11.7 | -30.9 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 8-12 | 40.0 | -7.5 | -23.0 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 6-10 | 37.5 | -10.0 | -27.0 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 7-11 | 38.9 | -8.7 | -25.0 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 17-18 | 48.6 | -0.3 | -6.9 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 1-6 | 14.3 | -31.8 | -71.4 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 7-11 | 38.9 | -8.7 | -25.0 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 8-12 | 40.0 | -7.5 | -23.0 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 3-11 | 21.4 | -25.4 | -58.4 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 4-11 | 26.7 | -20.5 | -48.7 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 10-17 | 37.0 | -10.7 | -28.9 |  |
| money_delta+pin_value | close | pin limit <$1k | 6-2 | 75.0 | 26.8 | 43.2 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 4-3 | 57.1 | 8.9 | 8.5 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 2-3 | 40.0 | -8.5 | -24.4 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 16-19 | 45.7 | -4.5 | -13.2 |  |
| money_level+sharp_gap | close | pin limit <$1k | 27-26 | 50.9 | 0.0 | -2.9 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 1-3 | 25.0 | -22.6 | -52.3 |  |
| money_delta+money_level | close | pin limit <$1k | 1-6 | 14.3 | -33.3 | -72.1 |  |
| money_level+pin_rlm | close | pin limit <$1k | 5-4 | 55.6 | 6.9 | 6.5 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 5-5 | 50.0 | 1.5 | -4.1 |  |
| rlm_quiet | early | <1k bets | 26-33 | 44.1 | 5.6 | 5.3 | 0.82 |
| rlm_quiet | early | pin $1-2k | 2-2 | 50.0 | 17.3 | 23.0 | 1.12 |
| rlm_quiet | early | pin limit <$1k | 1-2 | 33.3 | -14.2 | -36.4 | 0.33 |
| pin_move | early | <1k bets | 9-13 | 40.9 | -8.6 | -23.2 | 0.12 |
| pin_move | early | pin $1-2k | 2-6 | 25.0 | -26.4 | -56.8 | 0.29 |
| pin_move | early | pin limit <$1k | 7-10 | 41.2 | -8.0 | -20.9 | 0.59 |
| money_delta | early | <1k bets | 4-5 | 44.4 | 6.8 | 16.3 | 3.02 |
| money_delta | early | pin $1-2k | 0-1 | 0.0 | -32.7 | -100.0 | 1.5 |
| money_delta | early | pin limit <$1k | 1-0 | 100.0 | 52.4 | 90.9 | 1.0 |
| pin_rlm | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
| follow_move | early | <1k bets | 203-219 | 48.1 | -0.7 | -8.1 | 0.07 |
| follow_move | early | pin $1-2k | 14-15 | 48.3 | 3.2 | -2.9 | -0.35 |
| follow_move | early | pin limit <$1k | 13-21 | 38.2 | -10.4 | -25.6 | 0.01 |
| rlm_ratio | early | <1k bets | 10-16 | 38.5 | -2.8 | -7.6 | 0.4 |
| rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 9.9 | -4.5 | 0.5 |
| money_level | early | <1k bets | 73-61 | 54.5 | -3.1 | -12.4 | -0.39 |
| money_level | early | pin $1-2k | 3-5 | 37.5 | -22.6 | -38.8 | -0.29 |
| money_level | early | pin limit <$1k | 8-6 | 57.1 | 6.8 | 9.1 | 0.29 |
| sharp_gap | early | <1k bets | 56-63 | 47.1 | -3.2 | -10.4 | 0.24 |
| sharp_gap | early | pin $1-2k | 2-6 | 25.0 | -36.6 | -63.1 | -0.04 |
| sharp_gap | early | pin limit <$1k | 7-5 | 58.3 | 9.2 | 11.4 | 0.33 |
| money_moving | early | <1k bets | 46-43 | 51.7 | 2.6 | -2.0 | 0.6 |
| money_moving | early | pin $1-2k | 0-4 | 0.0 | -55.8 | -100.0 | 1.05 |
| money_moving | early | pin limit <$1k | 10-2 | 83.3 | 32.9 | 57.2 | 0.25 |
| pin_value | early | <1k bets | 22-19 | 53.7 | 4.1 | 1.5 | 0.09 |
| pin_value | early | pin $1-2k | 6-11 | 35.3 | -13.6 | -33.8 | 0.34 |
| pin_value | early | pin limit <$1k | 17-9 | 65.4 | 15.5 | 24.0 | -0.04 |
| consensus_gap | early | <1k bets | 113-101 | 52.8 | -0.1 | -7.9 | 0.54 |
| consensus_gap | early | pin $1-2k | 10-5 | 66.7 | 16.3 | 23.1 | -0.17 |
| consensus_gap | early | pin limit <$1k | 8-4 | 66.7 | 16.3 | 26.7 | 0.08 |
| follow_move+money_level | early | <1k bets | 26-18 | 59.1 | 1.9 | -11.2 | 0.11 |
| follow_move+sharp_gap | early | <1k bets | 24-26 | 48.0 | 0.0 | -6.0 | 0.62 |
| money_level+sharp_gap | early | <1k bets | 38-37 | 50.7 | -5.2 | -15.2 | -0.18 |
| follow_move+money_moving | early | <1k bets | 19-19 | 50.0 | 2.4 | 0.4 | 0.67 |
| money_level+money_moving | early | <1k bets | 22-17 | 56.4 | 1.1 | -2.5 | 0.45 |
| consensus_gap+money_level | early | <1k bets | 24-17 | 58.5 | -3.2 | -12.7 | -0.54 |
| follow_move+rlm_quiet | early | <1k bets | 26-33 | 44.1 | 5.6 | 5.3 | 0.82 |
| follow_move+rlm_ratio | early | <1k bets | 10-16 | 38.5 | -2.8 | -7.6 | 0.4 |
| rlm_quiet+rlm_ratio | early | <1k bets | 9-10 | 47.4 | 8.4 | 16.3 | 0.32 |
| rlm_quiet+sharp_gap | early | <1k bets | 10-12 | 45.5 | 5.3 | 9.2 | 0.5 |
| rlm_ratio+sharp_gap | early | <1k bets | 10-16 | 38.5 | -2.8 | -7.6 | 0.4 |
| consensus_gap+follow_move | early | <1k bets | 16-20 | 44.4 | -10.7 | -26.1 | 0.87 |
| money_moving+rlm_quiet | early | <1k bets | 9-10 | 47.4 | 8.4 | 15.7 | 0.91 |
| money_moving+rlm_ratio | early | <1k bets | 7-6 | 53.8 | 13.6 | 31.1 | 1.58 |
| money_moving+sharp_gap | early | <1k bets | 25-28 | 47.2 | 0.1 | -2.9 | 0.89 |
| consensus_gap+money_moving | early | <1k bets | 10-5 | 66.7 | 11.6 | 6.5 | 1.23 |
| consensus_gap+sharp_gap | early | <1k bets | 15-15 | 50.0 | -7.1 | -21.3 | -0.38 |
| money_level+rlm_ratio | early | <1k bets | 1-6 | 14.3 | -33.0 | -72.7 | 0.64 |
| follow_move+pin_move | early | <1k bets | 4-7 | 36.4 | -10.9 | -29.9 | 0.55 |
| follow_move+money_delta | early | <1k bets | 3-2 | 60.0 | 21.4 | 71.2 | 2.74 |
| money_delta+money_level | early | <1k bets | 1-3 | 25.0 | -15.1 | -52.3 | 1.68 |
| money_delta+money_moving | early | <1k bets | 4-5 | 44.4 | 6.8 | 16.3 | 3.02 |
| money_delta+rlm_ratio | early | <1k bets | 3-2 | 60.0 | 21.4 | 71.2 | 2.74 |
| money_delta+sharp_gap | early | <1k bets | 4-5 | 44.4 | 6.8 | 16.3 | 3.02 |
| follow_move+pin_value | early | <1k bets | 5-5 | 50.0 | 0.8 | -4.1 | -0.3 |
| consensus_gap+pin_move | early | <1k bets | 2-1 | 66.7 | 14.7 | 28.7 | 0.33 |
| consensus_gap+pin_value | early | <1k bets | 10-3 | 76.9 | 27.9 | 45.4 | -0.15 |
| money_level+pin_move | early | <1k bets | 2-4 | 33.3 | -14.4 | -35.8 | 0.17 |
| money_level+pin_value | early | <1k bets | 3-3 | 50.0 | -4.1 | -4.5 | 0.78 |
| pin_move+pin_value | early | <1k bets | 4-7 | 36.4 | -13.5 | -29.8 | 0.55 |
| money_moving+pin_value | early | <1k bets | 3-2 | 60.0 | 6.8 | 15.4 | 1.14 |
| pin_value+sharp_gap | early | <1k bets | 1-4 | 20.0 | -35.1 | -61.8 | 1.34 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 52.4 | 90.9 | 1.0 |
| consensus_gap+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 52.4 | 90.9 | 1.0 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 52.4 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 52.4 | 90.9 | 1.0 |
| follow_move+pin_rlm | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| money_level+pin_rlm | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_rlm+rlm_ratio | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_rlm+sharp_gap | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_move+sharp_gap | early | <1k bets | 0-3 | 0.0 | -45.9 | -100.0 | 1.0 |
| money_delta+rlm_quiet | early | <1k bets | 2-1 | 66.7 | 34.0 | 121.7 | 3.57 |
| consensus_gap+rlm_quiet | early | <1k bets | 1-1 | 50.0 | 17.3 | 30.0 | 1.1 |
| money_moving+pin_move | early | <1k bets | 1-1 | 50.0 | 2.4 | -2.4 | 1.0 |
| pin_move+pin_rlm | early | <1k bets | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
| pin_move+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
| pin_move+pin_value | early | pin $1-2k | 0-4 | 0.0 | -47.0 | -100.0 | 0.5 |
| follow_move+rlm_quiet | early | pin $1-2k | 2-2 | 50.0 | 17.3 | 23.0 | 1.12 |
| money_level+money_moving | early | pin $1-2k | 0-3 | 0.0 | -55.8 | -100.0 | 1.07 |
| money_level+pin_value | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.7 |
| money_level+sharp_gap | early | pin $1-2k | 2-5 | 28.6 | -33.8 | -57.8 | -0.19 |
| money_moving+pin_value | early | pin $1-2k | 0-2 | 0.0 | -61.6 | -100.0 | 1.35 |
| money_moving+sharp_gap | early | pin $1-2k | 0-4 | 0.0 | -55.8 | -100.0 | 1.05 |
| pin_value+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -61.6 | -100.0 | 1.35 |
| consensus_gap+pin_value | early | pin $1-2k | 3-1 | 75.0 | 28.0 | 39.3 | -0.5 |
| follow_move+money_level | early | pin $1-2k | 1-2 | 33.3 | -26.2 | -35.2 | 0.17 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| follow_move+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| follow_move+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -67.3 | -100.0 | 0.75 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| money_level+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| consensus_gap+follow_move | early | pin $1-2k | 2-1 | 66.7 | 22.4 | 55.3 | 0.6 |
| follow_move+pin_move | early | pin $1-2k | 1-2 | 33.3 | -14.7 | -35.2 | -0.33 |
| follow_move+pin_value | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap+money_level | early | pin $1-2k | 2-1 | 66.7 | -0.6 | -1.6 | -1.83 |
| consensus_gap+sharp_gap | early | pin $1-2k | 2-1 | 66.7 | -0.6 | -1.6 | -1.83 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 1-0 | 100.0 | 67.3 | 160.0 | 0.3 |
| consensus_gap+money_moving | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 0.0 |
| money_level+pin_move | early | pin $1-2k | 1-0 | 100.0 | 55.9 | 94.3 | -1.0 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -32.7 | -100.0 | 1.5 |
| money_delta+money_moving | early | pin $1-2k | 0-1 | 0.0 | -32.7 | -100.0 | 1.5 |
| money_delta+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -32.7 | -100.0 | 1.5 |
| follow_move+pin_move | early | pin limit <$1k | 3-6 | 33.3 | -13.7 | -35.9 | 0.89 |
| follow_move+pin_value | early | pin limit <$1k | 5-3 | 62.5 | 13.5 | 19.9 | -0.38 |
| consensus_gap+money_level | early | pin limit <$1k | 3-0 | 100.0 | 49.2 | 90.9 | 0.0 |
| consensus_gap+pin_move | early | pin limit <$1k | 2-1 | 66.7 | 14.7 | 28.7 | 0.33 |
| consensus_gap+pin_value | early | pin limit <$1k | 7-2 | 77.8 | 27.9 | 48.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 4-2 | 66.7 | 18.3 | 28.0 | 0.5 |
| follow_move+rlm_quiet | early | pin limit <$1k | 1-2 | 33.3 | -14.2 | -36.4 | 0.33 |
| follow_move+sharp_gap | early | pin limit <$1k | 3-3 | 50.0 | 3.3 | -3.8 | 0.17 |
| money_level+pin_move | early | pin limit <$1k | 1-4 | 20.0 | -28.5 | -61.8 | 0.4 |
| money_level+pin_value | early | pin limit <$1k | 4-2 | 66.7 | 15.0 | 26.6 | 0.33 |
| money_moving+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 2.4 | -4.5 | 0.0 |
| money_moving+sharp_gap | early | pin limit <$1k | 6-1 | 85.7 | 36.1 | 63.7 | 0.0 |
| pin_move+pin_value | early | pin limit <$1k | 4-4 | 50.0 | -0.6 | -3.5 | 0.75 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -47.6 | -100.0 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 | -0.5 |
| consensus_gap+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 52.4 | 90.9 | 1.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 52.4 | 92.3 | 1.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.4 | 90.9 | 1.0 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 52.4 | 90.9 | 1.0 |
| follow_move+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 52.4 | 90.9 | 1.0 |
| follow_move+money_level | early | pin limit <$1k | 3-3 | 50.0 | 2.5 | -3.8 | 0.0 |
| follow_move+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 9.9 | -4.5 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 52.4 | 90.9 | 1.0 |
| money_delta+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 52.4 | 90.9 | 1.0 |
| money_delta+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 52.4 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.4 | 90.9 | 1.0 |
| money_delta+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 52.4 | 90.9 | 1.0 |
| money_level+money_moving | early | pin limit <$1k | 5-0 | 100.0 | 49.5 | 91.0 | 0.2 |
| money_level+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 9.9 | -4.5 | 0.5 |
| money_level+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 10.5 | 14.6 | 0.5 |
| money_moving+pin_value | early | pin limit <$1k | 4-0 | 100.0 | 51.2 | 91.0 | 0.5 |
| money_moving+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.4 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.4 | 90.9 | 1.0 |
| pin_value+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | -1.2 | -5.5 | 0.75 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 9.9 | -4.5 | 0.5 |
| pin_move+sharp_gap | early | pin limit <$1k | 0-3 | 0.0 | -45.9 | -100.0 | 1.0 |
| money_moving+pin_move | early | pin limit <$1k | 1-1 | 50.0 | 2.4 | -2.4 | 1.0 |
| follow_move+pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
| money_level+pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
| pin_move+pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
| pin_move+rlm_ratio | early | pin limit <$1k | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
| pin_move+rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -47.6 | -100.0 | 1.0 |
