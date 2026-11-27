# CBB scorecard

Generated 2026-11-27 19:12 UTC. 992 graded games (37 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**684 games before 2026-11-21 (fit) · 308 on or after it (forward).**

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
sample ran **46.4% favourites** (n=991) and **50.5% overs** (n=992) and **70.9% moneyline favourites** (n=870).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-21. Nothing in the engine was chosen using these. n=308 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 26-36 | 41.9 | 39.8 | 2.1 | +0.11 | 0.2 | 1.03 | 51.6 | DROP: below break-even |
| pin_move | both | 9-16 | 36.0 | 49.7 | -13.7 | -8.09 | -32.4 | 0.49 | 40.0 | keep collecting (25/30) |
| money_delta | both | 4-5 | 44.4 | 38.6 | 5.9 | +1.47 | 16.3 | 3.02 | 100.0 | keep collecting (9/30) |
| pin_rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | keep collecting (2/30) |
| follow_move | both | 255-274 | 48.2 | 49.0 | -0.8 | -43.27 | -8.2 | 0.09 | 38.8 | DROP: below break-even |
| rlm_ratio | both | 10-17 | 37.0 | 42.8 | -5.8 | -2.99 | -11.1 | 0.72 | 55.6 | keep collecting (27/30) |
| money_level | both | 78-64 | 54.9 | 57.0 | -2.1 | -16.56 | -11.7 | -0.43 | 35.2 | no edge shown yet |
| sharp_gap | both | 60-67 | 47.2 | 50.1 | -2.9 | -13.26 | -10.4 | 0.25 | 45.7 | no edge shown yet |
| money_moving | both | 51-45 | 53.1 | 49.6 | 3.5 | -0.4 | -0.4 | 0.58 | 50.0 | no edge shown yet |
| pin_value | both | 23-20 | 53.5 | 49.3 | 4.2 | +0.49 | 1.1 | 0.11 | 34.9 | no edge shown yet |
| consensus_gap | both | 147-136 | 51.9 | 52.6 | -0.6 | -25.68 | -9.1 | 0.48 | 49.1 | no edge shown yet |
| follow_move+money_level | both | 28-20 | 58.3 | 57.1 | 1.2 | -6.67 | -13.9 | 0.22 | 37.5 | no edge shown yet |
| follow_move+sharp_gap | both | 25-28 | 47.2 | 48.6 | -1.4 | -4.92 | -9.3 | 0.82 | 47.2 | no edge shown yet |
| money_level+sharp_gap | both | 40-38 | 51.3 | 55.5 | -4.2 | -11.44 | -14.7 | -0.21 | 39.7 | no edge shown yet |
| follow_move+money_moving | both | 21-20 | 51.2 | 49.2 | 2.1 | -0.61 | -1.5 | 0.84 | 46.3 | no edge shown yet |
| money_level+money_moving | both | 25-18 | 58.1 | 55.4 | 2.8 | -0.84 | -2.0 | 0.39 | 46.5 | no edge shown yet |
| consensus_gap+money_level | both | 26-19 | 57.8 | 60.3 | -2.5 | -5.32 | -11.8 | -0.63 | 31.1 | no edge shown yet |
| follow_move+rlm_quiet | both | 26-36 | 41.9 | 39.8 | 2.1 | +0.11 | 0.2 | 1.03 | 51.6 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 10-17 | 37.0 | 42.8 | -5.8 | -2.99 | -11.1 | 0.72 | 55.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | both | 9-11 | 45.0 | 41.1 | 3.9 | +2.1 | 10.5 | 0.74 | 50.0 | keep collecting (20/30) |
| rlm_quiet+sharp_gap | both | 10-14 | 41.7 | 41.6 | 0.0 | +0.01 | 0.1 | 1.05 | 50.0 | keep collecting (24/30) |
| rlm_ratio+sharp_gap | both | 10-17 | 37.0 | 42.8 | -5.8 | -2.99 | -11.1 | 0.72 | 55.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 18-21 | 46.2 | 55.1 | -8.9 | -9.16 | -23.5 | 0.97 | 59.0 | no edge shown yet |
| money_moving+rlm_quiet | both | 9-11 | 45.0 | 41.1 | 3.9 | +1.99 | 9.9 | 1.31 | 50.0 | keep collecting (20/30) |
| money_moving+rlm_ratio | both | 7-7 | 50.0 | 42.8 | 7.2 | +3.05 | 21.8 | 2.11 | 71.4 | keep collecting (14/30) |
| money_moving+sharp_gap | both | 29-30 | 49.2 | 47.9 | 1.2 | -0.36 | -0.6 | 0.81 | 54.2 | no edge shown yet |
| consensus_gap+money_moving | both | 11-6 | 64.7 | 54.2 | 10.5 | +0.88 | 5.2 | 1.21 | 58.8 | keep collecting (17/30) |
| consensus_gap+sharp_gap | both | 16-17 | 48.5 | 55.5 | -7.0 | -7.48 | -22.7 | -0.34 | 36.4 | no edge shown yet |
| money_level+rlm_ratio | both | 1-6 | 14.3 | 47.7 | -33.4 | -5.09 | -72.7 | 0.64 | 71.4 | keep collecting (7/30) |
| follow_move+pin_move | both | 4-8 | 33.3 | 47.3 | -14.0 | -4.29 | -35.7 | 0.58 | 41.7 | keep collecting (12/30) |
| follow_move+money_delta | both | 3-2 | 60.0 | 39.5 | 20.5 | +3.56 | 71.2 | 2.74 | 100.0 | keep collecting (5/30) |
| money_delta+money_level | both | 1-3 | 25.0 | 40.9 | -15.9 | -2.09 | -52.3 | 1.68 | 100.0 | keep collecting (4/30) |
| money_delta+money_moving | both | 4-5 | 44.4 | 38.6 | 5.9 | +1.47 | 16.3 | 3.02 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | both | 3-2 | 60.0 | 39.5 | 20.5 | +3.56 | 71.2 | 2.74 | 100.0 | keep collecting (5/30) |
| money_delta+sharp_gap | both | 4-5 | 44.4 | 38.6 | 5.9 | +1.47 | 16.3 | 3.02 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| follow_move+pin_value | both | 5-5 | 50.0 | 49.1 | 0.9 | -0.41 | -4.1 | -0.3 | 30.0 | keep collecting (10/30) |
| consensus_gap+pin_move | both | 2-1 | 66.7 | 52.3 | 14.4 | +0.86 | 28.7 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+pin_value | both | 10-3 | 76.9 | 48.8 | 28.1 | +5.9 | 45.4 | -0.15 | 30.8 | keep collecting (13/30) |
| money_level+pin_move | both | 2-4 | 33.3 | 47.7 | -14.4 | -2.15 | -35.8 | 0.17 | 16.7 | keep collecting (6/30) |
| money_level+pin_value | both | 4-3 | 57.1 | 53.6 | 3.6 | +0.6 | 8.5 | 0.53 | 42.9 | keep collecting (7/30) |
| pin_move+pin_value | both | 4-8 | 33.3 | 49.2 | -15.9 | -4.28 | -35.7 | 0.67 | 41.7 | keep collecting (12/30) |
| money_moving+pin_value | both | 4-2 | 66.7 | 53.0 | 13.6 | +1.64 | 27.3 | 0.78 | 83.3 | keep collecting (6/30) |
| pin_value+sharp_gap | both | 2-4 | 33.3 | 54.6 | -21.2 | -2.22 | -37.0 | 0.95 | 66.7 | keep collecting (6/30) |
| consensus_gap+money_delta | both | 1-0 | 100.0 | 47.7 | 52.3 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 1-0 | 100.0 | 47.7 | 52.3 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | both | 1-0 | 100.0 | 47.7 | 52.3 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+rlm_ratio | both | 1-0 | 100.0 | 47.7 | 52.3 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+sharp_gap | both | 0-3 | 0.0 | 46.2 | -46.2 | -3.0 | -100.0 | 1.0 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | both | 2-1 | 66.7 | 34.0 | 32.6 | +3.65 | 121.7 | 3.57 | 100.0 | keep collecting (3/30) |
| consensus_gap+rlm_quiet | both | 1-1 | 50.0 | 34.0 | 16.0 | +0.6 | 30.0 | 1.1 | 100.0 | keep collecting (2/30) |
| money_moving+pin_move | both | 1-1 | 50.0 | 47.7 | 2.3 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+pin_rlm | both | 0-1 | 0.0 | 34.0 | -34.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 0-1 | 0.0 | 34.0 | -34.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+rlm_quiet | both | 0-1 | 0.0 | 47.7 | -47.7 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 15-23 | 39.5 | 34.9 | 4.6 | +3.11 | 8.2 | 1.2 | 47.4 | DROP: below break-even |
| rlm_quiet | total | 11-13 | 45.8 | 47.7 | -1.9 | -3.0 | -12.5 | 0.75 | 58.3 | keep collecting (24/30) |
| pin_move | moneyline | 1-2 | 33.3 | 55.3 | -22.0 | -1.48 | -49.5 | 0.77 | 33.3 | keep collecting (3/30) |
| pin_move | spread | 1-6 | 14.3 | 47.1 | -32.8 | -5.06 | -72.2 | 0.0 | 14.3 | keep collecting (7/30) |
| pin_move | total | 7-8 | 46.7 | 49.8 | -3.2 | -1.55 | -10.3 | 0.67 | 53.3 | keep collecting (15/30) |
| money_delta | moneyline | 2-4 | 33.3 | 34.0 | -0.7 | +0.65 | 10.8 | 2.7 | 100.0 | keep collecting (6/30) |
| money_delta | total | 2-1 | 66.7 | 47.7 | 18.9 | +0.82 | 27.3 | 3.67 | 100.0 | keep collecting (3/30) |
| pin_rlm | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | keep collecting (2/30) |
| follow_move | moneyline | 109-95 | 53.4 | 47.3 | 6.1 | +1.33 | 0.7 | -0.09 | 37.3 | no edge shown yet |
| follow_move | spread | 55-73 | 43.0 | 50.7 | -7.8 | -21.83 | -17.1 | 0.05 | 30.5 | DROP: below break-even |
| follow_move | total | 91-106 | 46.2 | 49.5 | -3.3 | -22.77 | -11.6 | 0.3 | 45.7 | DROP: below break-even |
| rlm_ratio | moneyline | 4-11 | 26.7 | 38.3 | -11.6 | -2.44 | -16.3 | 0.36 | 40.0 | keep collecting (15/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| rlm_ratio | total | 6-5 | 54.5 | 47.7 | 6.8 | +0.45 | 4.1 | 0.82 | 72.7 | keep collecting (11/30) |
| money_level | moneyline | 41-32 | 56.2 | 62.0 | -5.9 | -18.15 | -24.9 | -0.53 | 35.6 | no edge shown yet |
| money_level | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.06 | -2.9 | 2.0 | 50.0 | keep collecting (2/30) |
| money_level | total | 36-31 | 53.7 | 51.8 | 1.9 | +1.64 | 2.5 | -0.4 | 34.3 | no edge shown yet |
| sharp_gap | moneyline | 26-38 | 40.6 | 50.0 | -9.4 | -15.08 | -23.6 | 0.02 | 46.9 | DROP: below break-even |
| sharp_gap | spread | 0-2 | 0.0 | 56.8 | -56.8 | -2.0 | -100.0 | 3.0 | 100.0 | keep collecting (2/30) |
| sharp_gap | total | 34-27 | 55.7 | 50.0 | 5.7 | +3.83 | 6.3 | 0.41 | 42.6 | no edge shown yet |
| money_moving | moneyline | 22-22 | 50.0 | 49.3 | 0.7 | -3.81 | -8.6 | 0.89 | 59.1 | no edge shown yet |
| money_moving | spread | 0-2 | 0.0 | 56.8 | -56.8 | -2.0 | -100.0 | 3.0 | 100.0 | keep collecting (2/30) |
| money_moving | total | 29-21 | 58.0 | 49.6 | 8.4 | +5.4 | 10.8 | 0.22 | 40.0 | no edge shown yet |
| pin_value | moneyline | 0-1 | 0.0 | 66.0 | -66.0 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| pin_value | spread | 11-11 | 50.0 | 47.5 | 2.5 | -1.42 | -6.5 | 0.14 | 27.3 | keep collecting (22/30) |
| pin_value | total | 12-8 | 60.0 | 50.5 | 9.5 | +2.92 | 14.6 | 0.0 | 40.0 | keep collecting (20/30) |
| consensus_gap | moneyline | 71-67 | 51.4 | 56.3 | -4.8 | -24.21 | -17.5 | 0.36 | 48.6 | no edge shown yet |
| consensus_gap | spread | 31-20 | 60.8 | 47.5 | 13.3 | +6.92 | 13.6 | 0.25 | 35.3 | no edge shown yet |
| consensus_gap | total | 45-49 | 47.9 | 49.9 | -2.0 | -8.39 | -8.9 | 0.79 | 57.4 | no edge shown yet |
| consensus_gap+money_level | moneyline | 21-15 | 58.3 | 62.4 | -4.1 | -5.82 | -16.2 | -0.71 | 33.3 | no edge shown yet |
| follow_move+rlm_quiet | moneyline | 15-23 | 39.5 | 34.9 | 4.6 | +3.11 | 8.2 | 1.2 | 47.4 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 4-11 | 26.7 | 38.3 | -11.6 | -2.44 | -16.3 | 0.36 | 40.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 10-14 | 41.7 | 47.3 | -5.7 | -4.6 | -19.2 | 0.72 | 37.5 | keep collecting (24/30) |
| rlm_quiet+rlm_ratio | moneyline | 4-8 | 33.3 | 36.7 | -3.4 | +0.56 | 4.7 | 0.83 | 41.7 | keep collecting (12/30) |
| rlm_quiet+sharp_gap | moneyline | 4-9 | 30.8 | 36.5 | -5.7 | -0.44 | -3.4 | 1.17 | 46.2 | keep collecting (13/30) |
| rlm_ratio+sharp_gap | moneyline | 4-11 | 26.7 | 38.3 | -11.6 | -2.44 | -16.3 | 0.36 | 40.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 12-8 | 60.0 | 61.2 | -1.2 | -1.62 | -8.1 | 0.49 | 45.0 | keep collecting (20/30) |
| consensus_gap+money_moving | moneyline | 7-4 | 63.6 | 57.3 | 6.4 | -0.8 | -7.3 | 1.5 | 54.5 | keep collecting (11/30) |
| consensus_gap+sharp_gap | moneyline | 12-11 | 52.2 | 57.6 | -5.5 | -5.08 | -22.1 | -0.53 | 34.8 | keep collecting (23/30) |
| money_level+money_moving | moneyline | 10-8 | 55.6 | 60.6 | -5.1 | -4.48 | -24.9 | 0.99 | 55.6 | keep collecting (18/30) |
| money_level+sharp_gap | moneyline | 18-21 | 46.2 | 59.4 | -13.3 | -14.36 | -36.8 | -0.52 | 38.5 | no edge shown yet |
| money_moving+sharp_gap | moneyline | 9-17 | 34.6 | 45.1 | -10.5 | -5.54 | -21.3 | 1.27 | 69.2 | keep collecting (26/30) |
| follow_move+money_level | moneyline | 16-8 | 66.7 | 63.3 | 3.4 | -5.65 | -23.6 | -0.02 | 25.0 | keep collecting (24/30) |
| follow_move+money_moving | moneyline | 12-9 | 57.1 | 49.2 | 7.9 | +2.17 | 10.3 | 0.82 | 42.9 | keep collecting (21/30) |
| money_moving+rlm_quiet | moneyline | 5-7 | 41.7 | 36.7 | 5.0 | +2.35 | 19.6 | 1.93 | 58.3 | keep collecting (12/30) |
| money_moving+rlm_ratio | moneyline | 3-5 | 37.5 | 38.0 | -0.5 | +1.41 | 17.6 | 2.31 | 62.5 | keep collecting (8/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 66.0 | -66.0 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 66.0 | -66.0 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 66.0 | -66.0 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_rlm | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | moneyline | 0-3 | 0.0 | 44.7 | -44.7 | -3.0 | -100.0 | -1.5 | 33.3 | keep collecting (3/30) |
| pin_rlm+rlm_ratio | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+money_moving | moneyline | 2-4 | 33.3 | 34.0 | -0.7 | +0.65 | 10.8 | 2.7 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-4 | 33.3 | 34.0 | -0.7 | +0.65 | 10.8 | 2.7 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_level | moneyline | 0-2 | 0.0 | 34.0 | -34.0 | -2.0 | -100.0 | 1.85 | 100.0 | keep collecting (2/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 34.0 | 32.6 | +3.65 | 121.7 | 3.57 | 100.0 | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 2-1 | 66.7 | 34.0 | 32.6 | +3.65 | 121.7 | 3.57 | 100.0 | keep collecting (3/30) |
| money_delta+rlm_ratio | moneyline | 2-1 | 66.7 | 34.0 | 32.6 | +3.65 | 121.7 | 3.57 | 100.0 | keep collecting (3/30) |
| consensus_gap+rlm_quiet | moneyline | 1-1 | 50.0 | 34.0 | 16.0 | +0.6 | 30.0 | 1.1 | 100.0 | keep collecting (2/30) |
| follow_move+pin_move | moneyline | 0-1 | 0.0 | 34.0 | -34.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_move | moneyline | 0-1 | 0.0 | 34.0 | -34.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 0-1 | 0.0 | 34.0 | -34.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 0-1 | 0.0 | 34.0 | -34.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | moneyline | 0-1 | 0.0 | 34.0 | -34.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_level | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.06 | -2.9 | 2.0 | 50.0 | redundant -- identical record to money_level alone, not independent confirmation |
| follow_move+money_moving | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level+money_moving | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level+rlm_ratio | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+sharp_gap | spread | 0-2 | 0.0 | 56.8 | -56.8 | -2.0 | -100.0 | 3.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 1-2 | 33.3 | 47.7 | -14.4 | -1.09 | -36.4 | -0.33 | 0.0 | keep collecting (3/30) |
| pin_move+pin_value | spread | 0-4 | 0.0 | 46.6 | -46.6 | -4.0 | -100.0 | 0.5 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_value | spread | 4-1 | 80.0 | 45.9 | 34.1 | +2.41 | 48.1 | -0.4 | 0.0 | keep collecting (5/30) |
| follow_move+pin_move | spread | 1-2 | 33.3 | 47.7 | -14.4 | -1.06 | -35.2 | -0.33 | 0.0 | keep collecting (3/30) |
| consensus_gap+pin_move | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | spread | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 | 4.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_move | spread | 1-0 | 100.0 | 43.2 | 56.8 | +0.94 | 94.3 | -1.0 | 0.0 | keep collecting (1/30) |
| money_moving+pin_value | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| follow_move+money_level | total | 11-11 | 50.0 | 51.0 | -1.0 | -0.96 | -4.4 | 0.32 | 50.0 | keep collecting (22/30) |
| follow_move+sharp_gap | total | 15-13 | 53.6 | 49.4 | 4.2 | +0.68 | 2.4 | 0.75 | 53.6 | keep collecting (28/30) |
| money_level+sharp_gap | total | 22-16 | 57.9 | 51.4 | 6.5 | +3.92 | 10.3 | -0.03 | 39.5 | no edge shown yet |
| follow_move+money_moving | total | 9-10 | 47.4 | 48.7 | -1.3 | -1.78 | -9.3 | 0.63 | 47.4 | keep collecting (19/30) |
| money_level+money_moving | total | 15-9 | 62.5 | 51.3 | 11.2 | +4.63 | 19.3 | -0.25 | 37.5 | keep collecting (24/30) |
| follow_move+rlm_quiet | total | 11-13 | 45.8 | 47.7 | -1.9 | -3.0 | -12.5 | 0.75 | 58.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 6-5 | 54.5 | 47.7 | 6.8 | +0.45 | 4.1 | 0.82 | 72.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 5-3 | 62.5 | 47.7 | 14.8 | +1.55 | 19.3 | 0.62 | 62.5 | keep collecting (8/30) |
| rlm_quiet+sharp_gap | total | 6-5 | 54.5 | 47.7 | 6.8 | +0.45 | 4.1 | 0.91 | 54.5 | keep collecting (11/30) |
| rlm_ratio+sharp_gap | total | 6-5 | 54.5 | 47.7 | 6.8 | +0.45 | 4.1 | 0.82 | 72.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | total | 4-4 | 50.0 | 47.7 | 2.3 | -0.36 | -4.5 | 0.38 | 37.5 | keep collecting (8/30) |
| money_moving+rlm_ratio | total | 4-1 | 80.0 | 47.7 | 32.3 | +2.64 | 52.7 | 1.2 | 80.0 | keep collecting (5/30) |
| money_moving+sharp_gap | total | 20-11 | 64.5 | 49.8 | 14.7 | +7.18 | 23.2 | 0.29 | 38.7 | no edge shown yet |
| follow_move+pin_move | total | 3-5 | 37.5 | 48.9 | -11.4 | -2.23 | -27.9 | 1.0 | 62.5 | keep collecting (8/30) |
| consensus_gap+follow_move | total | 6-12 | 33.3 | 49.0 | -15.7 | -6.55 | -36.4 | 1.33 | 72.2 | keep collecting (18/30) |
| consensus_gap+money_level | total | 5-4 | 55.6 | 51.8 | 3.8 | +0.51 | 5.6 | -0.33 | 22.2 | keep collecting (9/30) |
| consensus_gap+sharp_gap | total | 4-6 | 40.0 | 50.5 | -10.5 | -2.4 | -24.0 | 0.1 | 40.0 | keep collecting (10/30) |
| follow_move+money_delta | total | 1-1 | 50.0 | 47.7 | 2.3 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+money_level | total | 1-1 | 50.0 | 47.7 | 2.3 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+money_moving | total | 2-1 | 66.7 | 47.7 | 18.9 | +0.82 | 27.3 | 3.67 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | total | 1-1 | 50.0 | 47.7 | 2.3 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 2-1 | 66.7 | 47.7 | 18.9 | +0.82 | 27.3 | 3.67 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+rlm_ratio | total | 1-2 | 33.3 | 47.7 | -14.4 | -1.09 | -36.4 | 1.33 | 100.0 | keep collecting (3/30) |
| follow_move+pin_value | total | 4-3 | 57.1 | 49.7 | 7.5 | +0.68 | 9.7 | -0.29 | 42.9 | keep collecting (7/30) |
| consensus_gap+pin_move | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | 0.5 | 50.0 | keep collecting (2/30) |
| consensus_gap+pin_value | total | 6-2 | 75.0 | 50.6 | 24.4 | +3.5 | 43.7 | 0.0 | 50.0 | keep collecting (8/30) |
| money_level+pin_move | total | 1-3 | 25.0 | 52.3 | -27.3 | -2.09 | -52.3 | 0.5 | 25.0 | keep collecting (4/30) |
| money_level+pin_value | total | 4-2 | 66.7 | 51.5 | 15.2 | +1.6 | 26.6 | 0.33 | 33.3 | keep collecting (6/30) |
| pin_move+pin_value | total | 4-4 | 50.0 | 50.6 | -0.6 | -0.28 | -3.5 | 0.75 | 50.0 | keep collecting (8/30) |
| consensus_gap+money_delta | total | 1-0 | 100.0 | 47.7 | 52.3 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_moving | total | 4-2 | 66.7 | 48.5 | 18.2 | +1.68 | 28.0 | 0.67 | 66.7 | keep collecting (6/30) |
| consensus_gap+rlm_ratio | total | 1-0 | 100.0 | 47.7 | 52.3 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | total | 1-0 | 100.0 | 47.7 | 52.3 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | total | 4-0 | 100.0 | 48.9 | 51.1 | +3.64 | 91.0 | 0.5 | 75.0 | keep collecting (4/30) |
| pin_value+rlm_ratio | total | 1-0 | 100.0 | 47.7 | 52.3 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | total | 2-2 | 50.0 | 51.1 | -1.1 | -0.22 | -5.5 | 0.75 | 50.0 | keep collecting (4/30) |
| pin_move+sharp_gap | total | 0-2 | 0.0 | 52.3 | -52.3 | -2.0 | -100.0 | 1.5 | 50.0 | keep collecting (2/30) |
| money_moving+pin_move | total | 1-1 | 50.0 | 47.7 | 2.3 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+rlm_quiet | total | 0-1 | 0.0 | 47.7 | -47.7 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 129-190 | 40.4 | 43.5 | -3.1 | -35.76 | -11.2 |  |  | DROP: below break-even |
| pin_move | both | 215-239 | 47.4 | 49.7 | -2.3 | -32.54 | -7.2 |  |  | DROP: below break-even |
| money_delta | both | 119-143 | 45.4 | 44.6 | 0.8 | -15.62 | -6.0 |  |  | DROP: below break-even |
| pin_rlm | both | 48-69 | 41.0 | 43.1 | -2.1 | -16.92 | -14.5 |  |  | DROP: below break-even |
| follow_move | both | 360-392 | 47.9 | 49.3 | -1.4 | -64.48 | -8.6 |  |  | DROP: below break-even |
| rlm_ratio | both | 83-127 | 39.5 | 43.3 | -3.8 | -35.65 | -17.0 |  |  | DROP: below break-even |
| money_level | both | 455-362 | 55.7 | 54.4 | 1.3 | -39.42 | -4.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 358-412 | 46.5 | 48.4 | -1.9 | -82.04 | -10.7 |  |  | DROP: below break-even |
| money_moving | both | 372-402 | 48.1 | 48.7 | -0.7 | -64.66 | -8.4 |  |  | DROP: below break-even |
| pin_value | both | 165-163 | 50.3 | 49.7 | 0.6 | -0.35 | -0.1 |  |  | no edge shown yet |
| consensus_gap | both | 148-120 | 55.2 | 52.9 | 2.3 | -1.26 | -0.5 |  |  | no edge shown yet |
| follow_move+pin_move | both | 149-189 | 44.1 | 49.3 | -5.2 | -49.91 | -14.8 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 91-110 | 45.3 | 43.4 | 1.8 | -9.09 | -4.5 |  |  | DROP: below break-even |
| money_delta+sharp_gap | both | 91-109 | 45.5 | 43.4 | 2.1 | -8.09 | -4.0 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 349-390 | 47.2 | 48.5 | -1.3 | -65.93 | -8.9 |  |  | DROP: below break-even |
| consensus_gap+money_level | both | 97-62 | 61.0 | 58.1 | 2.9 | -3.42 | -2.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+rlm_quiet | both | 129-190 | 40.4 | 43.5 | -3.1 | -35.76 | -11.2 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | both | 59-86 | 40.7 | 44.5 | -3.8 | -18.8 | -13.0 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 45-42 | 51.7 | 51.7 | 0.1 | -7.39 | -8.5 |  |  | no edge shown yet |
| follow_move+money_level | both | 170-139 | 55.0 | 54.7 | 0.3 | -21.09 | -6.8 |  |  | no edge shown yet |
| money_level+money_moving | both | 244-222 | 52.4 | 52.2 | 0.1 | -27.92 | -6.0 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 231-223 | 50.9 | 52.0 | -1.1 | -35.75 | -7.9 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 52-61 | 46.0 | 51.1 | -5.1 | -13.87 | -12.3 |  |  | no edge shown yet |
| consensus_gap+pin_move | both | 42-28 | 60.0 | 51.3 | 8.7 | +13.54 | 19.3 |  |  | no edge shown yet |
| consensus_gap+pin_value | both | 47-42 | 52.8 | 49.3 | 3.5 | +3.77 | 4.2 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | both | 52-65 | 44.4 | 50.6 | -6.2 | -17.73 | -15.2 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 191-218 | 46.7 | 48.4 | -1.7 | -44.16 | -10.8 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 55-53 | 50.9 | 50.2 | 0.8 | +6.03 | 5.6 |  |  | no edge shown yet |
| follow_move+sharp_gap | both | 187-222 | 45.7 | 48.2 | -2.4 | -47.87 | -11.7 |  |  | DROP: below break-even |
| money_level+pin_move | both | 95-94 | 50.3 | 53.2 | -3.0 | -19.83 | -10.5 |  |  | no edge shown yet |
| money_level+pin_value | both | 71-77 | 48.0 | 50.4 | -2.4 | -14.79 | -10.0 |  |  | no edge shown yet |
| money_moving+pin_move | both | 107-120 | 47.1 | 48.5 | -1.4 | -20.66 | -9.1 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 67-77 | 46.5 | 49.8 | -3.3 | -13.95 | -9.7 |  |  | no edge shown yet |
| pin_move+pin_value | both | 67-73 | 47.9 | 51.0 | -3.2 | -13.07 | -9.3 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 102-127 | 44.5 | 48.2 | -3.6 | -30.78 | -13.4 |  |  | DROP: below break-even |
| pin_value+sharp_gap | both | 66-82 | 44.6 | 50.0 | -5.4 | -19.86 | -13.4 |  |  | DROP: below break-even |
| follow_move+money_delta | both | 65-91 | 41.7 | 44.5 | -2.8 | -22.98 | -14.7 |  |  | DROP: below break-even |
| money_delta+pin_move | both | 37-48 | 43.5 | 45.5 | -1.9 | -12.55 | -14.8 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 40-61 | 39.6 | 42.5 | -2.9 | -15.9 | -15.7 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | both | 83-127 | 39.5 | 43.3 | -3.8 | -35.65 | -17.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | both | 65-101 | 39.2 | 42.7 | -3.5 | -26.68 | -16.1 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 81-120 | 40.3 | 43.4 | -3.1 | -31.28 | -15.6 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 47-90 | 34.3 | 41.7 | -7.4 | -32.85 | -24.0 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | both | 65-104 | 38.5 | 42.7 | -4.2 | -29.58 | -17.5 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 83-127 | 39.5 | 43.3 | -3.8 | -35.65 | -17.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | both | 30-29 | 50.8 | 47.4 | 3.4 | +1.66 | 2.8 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 12-19 | 38.7 | 41.4 | -2.7 | -6.0 | -19.3 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | both | 11-14 | 44.0 | 42.2 | 1.8 | -2.1 | -8.4 |  |  | keep collecting (25/30) |
| money_delta+rlm_ratio | both | 42-67 | 38.5 | 42.7 | -4.2 | -20.74 | -19.0 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 8-9 | 47.1 | 44.8 | 2.3 | +0.48 | 2.8 |  |  | keep collecting (17/30) |
| money_level+pin_rlm | both | 13-18 | 41.9 | 47.0 | -5.1 | -5.66 | -18.3 |  |  | no edge shown yet |
| money_moving+pin_rlm | both | 48-62 | 43.6 | 43.4 | 0.2 | -9.92 | -9.0 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 48-69 | 41.0 | 43.1 | -2.1 | -16.92 | -14.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | both | 27-29 | 48.2 | 47.1 | 1.1 | -3.83 | -6.8 |  |  | no edge shown yet |
| consensus_gap+money_delta | both | 17-11 | 60.7 | 44.1 | 16.6 | +9.56 | 34.1 |  |  | keep collecting (28/30) |
| follow_move+pin_rlm | both | 40-59 | 40.4 | 42.7 | -2.3 | -14.85 | -15.0 |  |  | DROP: below break-even |
| money_delta+pin_rlm | both | 26-36 | 41.9 | 43.3 | -1.4 | -10.12 | -16.3 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 45-59 | 43.3 | 43.9 | -0.6 | -11.0 | -10.6 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | both | 40-56 | 41.7 | 44.0 | -2.3 | -13.33 | -13.9 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 23-43 | 34.8 | 41.2 | -6.4 | -15.17 | -23.0 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | both | 40-59 | 40.4 | 42.7 | -2.3 | -14.85 | -15.0 |  |  | DROP: below break-even |
| money_delta+pin_value | both | 26-14 | 65.0 | 49.7 | 15.3 | +13.49 | 33.7 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_value+rlm_quiet | both | 17-20 | 45.9 | 48.5 | -2.5 | +5.6 | 15.1 |  |  | no edge shown yet |
| pin_value+rlm_ratio | both | 9-10 | 47.4 | 49.2 | -1.8 | -1.49 | -7.8 |  |  | keep collecting (19/30) |
| pin_rlm+pin_value | both | 11-12 | 47.8 | 50.3 | -2.5 | -1.64 | -7.1 |  |  | keep collecting (23/30) |
| rlm_quiet | moneyline | 46-85 | 35.1 | 34.5 | 0.6 | -7.84 | -6.0 |  |  | DROP: below break-even |
| rlm_quiet | spread | 26-30 | 46.4 | 54.1 | -7.7 | -5.73 | -10.2 |  |  | no edge shown yet |
| rlm_quiet | total | 57-75 | 43.2 | 48.0 | -4.8 | -22.19 | -16.8 |  |  | DROP: below break-even |
| pin_move | moneyline | 62-61 | 50.4 | 47.3 | 3.1 | +6.14 | 5.0 |  |  | no edge shown yet |
| pin_move | spread | 70-83 | 45.8 | 51.6 | -5.9 | -19.61 | -12.8 |  |  | DROP: below break-even |
| pin_move | total | 83-95 | 46.6 | 49.6 | -3.0 | -19.07 | -10.7 |  |  | DROP: below break-even |
| money_delta | moneyline | 33-58 | 36.3 | 36.1 | 0.1 | -9.51 | -10.5 |  |  | DROP: below break-even |
| money_delta | spread | 24-25 | 49.0 | 51.5 | -2.6 | -3.06 | -6.2 |  |  | no edge shown yet |
| money_delta | total | 62-60 | 50.8 | 48.1 | 2.7 | -3.05 | -2.5 |  |  | no edge shown yet |
| pin_rlm | moneyline | 16-35 | 31.4 | 35.3 | -3.9 | -12.12 | -23.8 |  |  | DROP: below break-even |
| pin_rlm | spread | 6-6 | 50.0 | 52.3 | -2.3 | -0.58 | -4.8 |  |  | keep collecting (12/30) |
| pin_rlm | total | 26-28 | 48.1 | 48.4 | -0.3 | -4.22 | -7.8 |  |  | no edge shown yet |
| follow_move | moneyline | 128-137 | 48.3 | 47.8 | 0.5 | -21.96 | -8.3 |  |  | no edge shown yet |
| follow_move | spread | 99-109 | 47.6 | 51.1 | -3.5 | -18.43 | -8.9 |  |  | no edge shown yet |
| follow_move | total | 133-146 | 47.7 | 49.3 | -1.7 | -24.09 | -8.6 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 26-61 | 29.9 | 34.8 | -4.9 | -21.6 | -24.8 |  |  | DROP: below break-even |
| rlm_ratio | spread | 14-12 | 53.8 | 52.6 | 1.2 | +0.52 | 2.0 |  |  | keep collecting (26/30) |
| rlm_ratio | total | 43-54 | 44.3 | 48.4 | -4.1 | -14.57 | -15.0 |  |  | DROP: below break-even |
| money_level | moneyline | 183-103 | 64.0 | 62.5 | 1.5 | -25.16 | -8.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 114-112 | 50.4 | 48.1 | 2.3 | -9.82 | -4.3 |  |  | no edge shown yet |
| money_level | total | 158-147 | 51.8 | 51.4 | 0.4 | -4.44 | -1.5 |  |  | no edge shown yet |
| sharp_gap | moneyline | 108-149 | 42.0 | 45.7 | -3.7 | -45.42 | -17.7 |  |  | DROP: below break-even |
| sharp_gap | spread | 113-114 | 49.8 | 49.4 | 0.4 | -12.28 | -5.4 |  |  | no edge shown yet |
| sharp_gap | total | 137-149 | 47.9 | 50.0 | -2.1 | -24.34 | -8.5 |  |  | DROP: below break-even |
| money_moving | moneyline | 117-138 | 45.9 | 46.7 | -0.8 | -31.52 | -12.4 |  |  | DROP: below break-even |
| money_moving | spread | 113-114 | 49.8 | 49.4 | 0.4 | -12.28 | -5.4 |  |  | no edge shown yet |
| money_moving | total | 142-150 | 48.6 | 50.1 | -1.4 | -20.86 | -7.1 |  |  | no edge shown yet |
| pin_value | moneyline | 8-14 | 36.4 | 44.2 | -7.8 | +9.75 | 44.3 |  |  | keep collecting (22/30) |
| pin_value | spread | 78-69 | 53.1 | 49.8 | 3.3 | -1.26 | -0.9 |  |  | no edge shown yet |
| pin_value | total | 79-80 | 49.7 | 50.4 | -0.7 | -8.84 | -5.6 |  |  | no edge shown yet |
| consensus_gap | moneyline | 78-65 | 54.5 | 55.5 | -0.9 | -7.94 | -5.5 |  |  | no edge shown yet |
| consensus_gap | spread | 30-22 | 57.7 | 49.0 | 8.7 | +3.99 | 7.7 |  |  | no edge shown yet |
| consensus_gap | total | 40-33 | 54.8 | 50.8 | 4.0 | +2.68 | 3.7 |  |  | no edge shown yet |
| consensus_gap+money_level | moneyline | 60-30 | 66.7 | 63.8 | 2.8 | -3.8 | -4.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+pin_move | moneyline | 46-54 | 46.0 | 46.8 | -0.8 | -9.21 | -9.2 |  |  | no edge shown yet |
| follow_move+rlm_quiet | moneyline | 46-85 | 35.1 | 34.5 | 0.6 | -7.84 | -6.0 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | moneyline | 21-33 | 38.9 | 34.6 | 4.3 | -1.17 | -2.2 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 24-23 | 51.1 | 53.1 | -2.0 | -7.13 | -15.2 |  |  | no edge shown yet |
| follow_move+money_level | moneyline | 71-43 | 62.3 | 62.0 | 0.2 | -14.91 | -13.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 103-133 | 43.6 | 45.8 | -2.2 | -31.64 | -13.4 |  |  | DROP: below break-even |
| follow_move+money_moving | moneyline | 64-80 | 44.4 | 45.3 | -0.9 | -21.76 | -15.1 |  |  | DROP: below break-even |
| follow_move+sharp_gap | moneyline | 59-83 | 41.5 | 44.6 | -3.1 | -25.37 | -17.9 |  |  | DROP: below break-even |
| money_level+money_moving | moneyline | 75-53 | 58.6 | 58.7 | -0.1 | -11.07 | -8.6 |  |  | no edge shown yet |
| money_level+sharp_gap | moneyline | 67-56 | 54.5 | 58.2 | -3.7 | -16.46 | -13.4 |  |  | no edge shown yet |
| follow_move+rlm_ratio | moneyline | 26-61 | 29.9 | 34.8 | -4.9 | -21.6 | -24.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | moneyline | 23-50 | 31.5 | 34.0 | -2.5 | -14.28 | -19.6 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 25-57 | 30.5 | 34.8 | -4.3 | -19.32 | -23.6 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | moneyline | 19-48 | 28.4 | 34.0 | -5.7 | -16.52 | -24.7 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 23-51 | 31.1 | 34.0 | -2.9 | -15.14 | -20.5 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 26-61 | 29.9 | 34.8 | -4.9 | -21.6 | -24.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 24-32 | 42.9 | 51.7 | -8.9 | -9.72 | -17.4 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | moneyline | 3-13 | 18.8 | 34.0 | -15.3 | -8.22 | -51.4 |  |  | keep collecting (16/30) |
| consensus_gap+rlm_ratio | moneyline | 3-9 | 25.0 | 34.0 | -9.0 | -4.22 | -35.2 |  |  | keep collecting (12/30) |
| consensus_gap+sharp_gap | moneyline | 24-35 | 40.7 | 50.8 | -10.1 | -12.58 | -21.3 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | moneyline | 4-4 | 50.0 | 38.0 | 12.0 | +1.88 | 23.5 |  |  | keep collecting (8/30) |
| money_level+pin_rlm | moneyline | 3-5 | 37.5 | 42.0 | -4.5 | -1.8 | -22.5 |  |  | keep collecting (8/30) |
| money_moving+pin_rlm | moneyline | 16-30 | 34.8 | 35.4 | -0.6 | -7.12 | -15.5 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 16-35 | 31.4 | 35.3 | -3.9 | -12.12 | -23.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 4-7 | 36.4 | 42.7 | -6.4 | +0.84 | 7.7 |  |  | keep collecting (11/30) |
| money_level+rlm_ratio | moneyline | 4-10 | 28.6 | 38.6 | -10.0 | -5.66 | -40.5 |  |  | keep collecting (14/30) |
| consensus_gap+pin_move | moneyline | 23-9 | 71.9 | 52.0 | 19.9 | +15.71 | 49.1 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+pin_move | moneyline | 29-18 | 61.7 | 61.9 | -0.2 | -3.12 | -6.6 |  |  | no edge shown yet |
| consensus_gap+money_delta | moneyline | 6-7 | 46.2 | 36.5 | 9.7 | +3.67 | 28.2 |  |  | keep collecting (13/30) |
| follow_move+money_delta | moneyline | 19-39 | 32.8 | 36.8 | -4.0 | -13.09 | -22.6 |  |  | DROP: below break-even |
| follow_move+pin_rlm | moneyline | 13-29 | 31.0 | 34.8 | -3.8 | -9.58 | -22.8 |  |  | DROP: below break-even |
| money_delta+money_moving | moneyline | 30-53 | 36.1 | 35.6 | 0.6 | -7.85 | -9.5 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 9-14 | 39.1 | 35.4 | 3.7 | -4.14 | -18.0 |  |  | keep collecting (23/30) |
| money_delta+pin_rlm | moneyline | 9-18 | 33.3 | 35.2 | -1.9 | -7.72 | -28.6 |  |  | keep collecting (27/30) |
| money_delta+rlm_quiet | moneyline | 13-31 | 29.5 | 34.0 | -4.5 | -10.89 | -24.8 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | moneyline | 13-36 | 26.5 | 35.3 | -8.8 | -16.27 | -33.2 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 30-53 | 36.1 | 35.6 | 0.6 | -7.85 | -9.5 |  |  | DROP: below break-even |
| money_moving+pin_move | moneyline | 24-28 | 46.2 | 43.2 | 2.9 | -3.65 | -7.0 |  |  | no edge shown yet |
| pin_move+pin_rlm | moneyline | 13-25 | 34.2 | 34.9 | -0.7 | -6.2 | -16.3 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 10-24 | 29.4 | 35.0 | -5.6 | -8.66 | -25.5 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 22-33 | 40.0 | 42.2 | -2.2 | -9.04 | -16.4 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 10-24 | 29.4 | 34.0 | -4.6 | -8.08 | -23.8 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 13-29 | 31.0 | 34.8 | -3.8 | -9.58 | -22.8 |  |  | DROP: below break-even |
| follow_move+pin_value | moneyline | 3-3 | 50.0 | 50.0 | 0.0 | +9.55 | 159.1 |  |  | keep collecting (6/30) |
| pin_value+rlm_quiet | moneyline | 2-1 | 66.7 | 34.0 | 32.6 | +10.98 | 366.0 |  |  | keep collecting (3/30) |
| money_delta+money_level | moneyline | 9-5 | 64.3 | 43.2 | 21.1 | +6.57 | 47.0 |  |  | keep collecting (14/30) |
| money_level+pin_value | moneyline | 1-6 | 14.3 | 61.4 | -47.1 | -5.43 | -77.6 |  |  | keep collecting (7/30) |
| pin_move+pin_value | moneyline | 3-4 | 42.9 | 52.3 | -9.4 | -0.97 | -13.9 |  |  | keep collecting (7/30) |
| money_delta+pin_value | moneyline | 2-0 | 100.0 | 34.0 | 66.0 | +5.88 | 294.0 |  |  | keep collecting (2/30) |
| money_moving+pin_value | moneyline | 3-4 | 42.9 | 43.2 | -0.3 | +2.45 | 35.0 |  |  | keep collecting (7/30) |
| pin_value+sharp_gap | moneyline | 3-6 | 33.3 | 48.2 | -14.9 | +0.45 | 5.0 |  |  | keep collecting (9/30) |
| pin_rlm+pin_value | moneyline | 1-0 | 100.0 | 34.0 | 66.0 | +1.38 | 138.0 |  |  | keep collecting (1/30) |
| pin_value+rlm_ratio | moneyline | 1-0 | 100.0 | 34.0 | 66.0 | +1.38 | 138.0 |  |  | keep collecting (1/30) |
| follow_move+pin_move | spread | 42-60 | 41.2 | 51.5 | -10.3 | -21.69 | -21.3 |  |  | DROP: below break-even |
| money_moving+sharp_gap | spread | 113-114 | 49.8 | 49.4 | 0.4 | -12.28 | -5.4 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 26-30 | 46.4 | 54.1 | -7.7 | -5.73 | -10.2 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | spread | 82-82 | 50.0 | 48.3 | 1.7 | -8.54 | -5.2 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 82-82 | 50.0 | 48.3 | 1.7 | -8.54 | -5.2 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 13-20 | 39.4 | 54.3 | -14.9 | -7.84 | -23.7 |  |  | no edge shown yet |
| consensus_gap+pin_value | spread | 21-16 | 56.8 | 49.8 | 6.9 | +2.32 | 6.3 |  |  | no edge shown yet |
| follow_move+money_level | spread | 36-36 | 50.0 | 49.8 | 0.2 | -3.46 | -4.8 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 45-47 | 48.9 | 51.0 | -2.1 | -6.27 | -6.8 |  |  | no edge shown yet |
| follow_move+sharp_gap | spread | 45-47 | 48.9 | 51.0 | -2.1 | -6.27 | -6.8 |  |  | no edge shown yet |
| money_level+pin_move | spread | 25-32 | 43.9 | 49.6 | -5.8 | -9.8 | -17.2 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 33-40 | 45.2 | 50.7 | -5.4 | -10.54 | -14.4 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 33-40 | 45.2 | 50.7 | -5.4 | -10.54 | -14.4 |  |  | no edge shown yet |
| money_delta+money_level | spread | 9-8 | 52.9 | 48.8 | 4.1 | +0.02 | 0.1 |  |  | keep collecting (17/30) |
| money_delta+money_moving | spread | 17-18 | 48.6 | 50.6 | -2.0 | -2.67 | -7.6 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 17-18 | 48.6 | 50.6 | -2.0 | -2.67 | -7.6 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 11-13 | 45.8 | 47.7 | -1.9 | -3.57 | -14.9 |  |  | keep collecting (24/30) |
| consensus_gap+money_moving | spread | 8-10 | 44.4 | 50.0 | -5.6 | -3.08 | -17.1 |  |  | keep collecting (18/30) |
| consensus_gap+sharp_gap | spread | 8-10 | 44.4 | 50.0 | -5.6 | -3.08 | -17.1 |  |  | keep collecting (18/30) |
| money_level+pin_value | spread | 29-32 | 47.5 | 47.7 | -0.1 | -7.09 | -11.6 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 29-36 | 44.6 | 49.7 | -5.1 | -10.87 | -16.7 |  |  | no edge shown yet |
| pin_value+sharp_gap | spread | 29-36 | 44.6 | 49.7 | -5.1 | -10.87 | -16.7 |  |  | no edge shown yet |
| follow_move+money_delta | spread | 11-12 | 47.8 | 52.7 | -4.8 | -2.12 | -9.2 |  |  | keep collecting (23/30) |
| follow_move+rlm_ratio | spread | 14-12 | 53.8 | 52.6 | 1.2 | +0.52 | 2.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | spread | 4-5 | 44.4 | 52.3 | -7.8 | -1.49 | -16.5 |  |  | keep collecting (9/30) |
| money_moving+rlm_ratio | spread | 14-12 | 53.8 | 52.6 | 1.2 | +0.52 | 2.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 14-12 | 53.8 | 52.6 | 1.2 | +0.52 | 2.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 20-19 | 51.3 | 50.9 | 0.4 | -1.47 | -3.8 |  |  | no edge shown yet |
| pin_move+pin_value | spread | 33-31 | 51.6 | 52.1 | -0.6 | -2.1 | -3.3 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 9-11 | 45.0 | 51.4 | -6.4 | -3.14 | -15.7 |  |  | keep collecting (20/30) |
| consensus_gap+follow_move | spread | 7-6 | 53.8 | 50.5 | 3.3 | +0.15 | 1.1 |  |  | keep collecting (13/30) |
| consensus_gap+rlm_quiet | spread | 2-0 | 100.0 | 56.8 | 43.2 | +1.82 | 90.9 |  |  | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 4-4 | 50.0 | 55.1 | -5.1 | -0.43 | -5.3 |  |  | keep collecting (8/30) |
| money_delta+rlm_quiet | spread | 6-5 | 54.5 | 54.3 | 0.2 | +0.6 | 5.4 |  |  | keep collecting (11/30) |
| money_moving+rlm_quiet | spread | 11-10 | 52.4 | 54.2 | -1.8 | +0.06 | 0.3 |  |  | keep collecting (21/30) |
| rlm_quiet+rlm_ratio | spread | 3-4 | 42.9 | 56.8 | -14.0 | -1.33 | -19.0 |  |  | keep collecting (7/30) |
| rlm_quiet+sharp_gap | spread | 11-10 | 52.4 | 54.2 | -1.8 | +0.06 | 0.3 |  |  | keep collecting (21/30) |
| consensus_gap+money_delta | spread | 3-2 | 60.0 | 56.8 | 3.2 | +0.63 | 12.7 |  |  | keep collecting (5/30) |
| money_delta+pin_move | spread | 8-9 | 47.1 | 52.8 | -5.7 | -1.9 | -11.2 |  |  | keep collecting (17/30) |
| money_delta+pin_value | spread | 8-5 | 61.5 | 54.7 | 6.8 | +2.14 | 16.4 |  |  | keep collecting (13/30) |
| money_moving+pin_rlm | spread | 6-6 | 50.0 | 52.3 | -2.3 | -0.58 | -4.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | spread | 6-6 | 50.0 | 52.3 | -2.3 | -0.58 | -4.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | spread | 4-3 | 57.1 | 56.8 | 0.3 | +0.6 | 8.6 |  |  | keep collecting (7/30) |
| pin_rlm+sharp_gap | spread | 6-6 | 50.0 | 52.3 | -2.3 | -0.58 | -4.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+rlm_ratio | spread | 3-1 | 75.0 | 53.4 | 21.6 | +1.59 | 39.7 |  |  | keep collecting (4/30) |
| money_level+rlm_ratio | spread | 10-5 | 66.7 | 51.4 | 15.3 | +3.94 | 26.3 |  |  | keep collecting (15/30) |
| pin_move+rlm_ratio | spread | 6-5 | 54.5 | 50.6 | 3.9 | +0.33 | 3.0 |  |  | keep collecting (11/30) |
| pin_value+rlm_ratio | spread | 2-1 | 66.7 | 56.8 | 9.8 | +0.76 | 25.2 |  |  | keep collecting (3/30) |
| follow_move+pin_rlm | spread | 3-4 | 42.9 | 49.0 | -6.2 | -1.27 | -18.2 |  |  | keep collecting (7/30) |
| money_delta+pin_rlm | spread | 4-4 | 50.0 | 55.1 | -5.1 | -0.4 | -4.9 |  |  | keep collecting (8/30) |
| pin_rlm+rlm_quiet | spread | 1-1 | 50.0 | 56.8 | -6.8 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| pin_rlm+rlm_ratio | spread | 3-4 | 42.9 | 49.0 | -6.2 | -1.27 | -18.2 |  |  | keep collecting (7/30) |
| money_level+pin_rlm | spread | 2-5 | 28.6 | 49.0 | -20.5 | -3.18 | -45.5 |  |  | keep collecting (7/30) |
| consensus_gap+pin_rlm | spread | 2-2 | 50.0 | 53.4 | -3.4 | -0.21 | -5.3 |  |  | keep collecting (4/30) |
| money_delta+money_moving | total | 44-39 | 53.0 | 48.3 | 4.7 | +1.42 | 1.7 |  |  | no edge shown yet |
| money_delta+sharp_gap | total | 44-38 | 53.7 | 48.3 | 5.4 | +2.42 | 2.9 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 133-143 | 48.2 | 50.0 | -1.9 | -22.01 | -8.0 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 57-75 | 43.2 | 48.0 | -4.8 | -22.19 | -16.8 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+follow_move | total | 14-13 | 51.9 | 49.7 | 2.1 | -0.4 | -1.5 |  |  | keep collecting (27/30) |
| consensus_gap+money_level | total | 26-19 | 57.8 | 52.1 | 5.7 | +3.95 | 8.8 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 20-19 | 51.3 | 50.6 | 0.6 | -1.07 | -2.7 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 10-8 | 55.6 | 50.0 | 5.6 | +0.97 | 5.4 |  |  | keep collecting (18/30) |
| consensus_gap+pin_value | total | 22-19 | 53.7 | 50.6 | 3.0 | +0.61 | 1.5 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 20-20 | 50.0 | 50.6 | -0.6 | -2.07 | -5.2 |  |  | no edge shown yet |
| follow_move+money_level | total | 63-60 | 51.2 | 50.7 | 0.5 | -2.73 | -2.2 |  |  | no edge shown yet |
| follow_move+money_moving | total | 82-91 | 47.4 | 49.5 | -2.1 | -16.14 | -9.3 |  |  | no edge shown yet |
| follow_move+pin_move | total | 61-75 | 44.9 | 49.5 | -4.6 | -19.01 | -14.0 |  |  | DROP: below break-even |
| follow_move+pin_value | total | 32-31 | 50.8 | 49.7 | 1.0 | -2.05 | -3.3 |  |  | no edge shown yet |
| follow_move+sharp_gap | total | 83-92 | 47.4 | 49.5 | -2.1 | -16.24 | -9.3 |  |  | no edge shown yet |
| money_level+money_moving | total | 87-87 | 50.0 | 51.1 | -1.1 | -8.32 | -4.8 |  |  | no edge shown yet |
| money_level+pin_move | total | 41-44 | 48.2 | 50.8 | -2.6 | -6.91 | -8.1 |  |  | no edge shown yet |
| money_level+pin_value | total | 41-39 | 51.2 | 51.5 | -0.2 | -2.27 | -2.8 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 82-85 | 49.1 | 51.2 | -2.1 | -10.75 | -6.4 |  |  | no edge shown yet |
| money_moving+pin_move | total | 50-52 | 49.0 | 49.7 | -0.7 | -6.47 | -6.3 |  |  | no edge shown yet |
| money_moving+pin_value | total | 35-37 | 48.6 | 50.6 | -2.0 | -5.53 | -7.7 |  |  | no edge shown yet |
| pin_move+pin_value | total | 31-38 | 44.9 | 49.9 | -5.0 | -10.0 | -14.5 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 47-54 | 46.5 | 49.7 | -3.1 | -11.2 | -11.1 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 34-40 | 45.9 | 50.5 | -4.5 | -9.44 | -12.8 |  |  | no edge shown yet |
| follow_move+money_delta | total | 35-40 | 46.7 | 48.0 | -1.3 | -7.77 | -10.4 |  |  | no edge shown yet |
| money_delta+pin_move | total | 20-25 | 44.4 | 47.8 | -3.4 | -6.51 | -14.5 |  |  | no edge shown yet |
| money_delta+rlm_quiet | total | 21-25 | 45.7 | 47.7 | -2.1 | -5.61 | -12.2 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 25-33 | 43.1 | 48.2 | -5.1 | -9.79 | -16.9 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 43-54 | 44.3 | 48.4 | -4.1 | -14.57 | -15.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | total | 25-26 | 49.0 | 48.1 | 0.9 | -2.99 | -5.9 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 31-41 | 43.1 | 48.1 | -5.1 | -12.46 | -17.3 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | total | 42-51 | 45.2 | 48.5 | -3.3 | -12.47 | -13.4 |  |  | no edge shown yet |
| rlm_quiet+rlm_ratio | total | 25-38 | 39.7 | 48.1 | -8.4 | -15.01 | -23.8 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | total | 31-43 | 41.9 | 48.1 | -6.2 | -14.51 | -19.6 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | total | 43-54 | 44.3 | 48.4 | -4.1 | -14.57 | -15.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | total | 8-2 | 80.0 | 47.7 | 32.3 | +5.26 | 52.6 |  |  | keep collecting (10/30) |
| consensus_gap+rlm_quiet | total | 7-6 | 53.8 | 48.1 | 5.8 | +0.41 | 3.1 |  |  | keep collecting (13/30) |
| consensus_gap+rlm_ratio | total | 5-4 | 55.6 | 48.2 | 7.3 | +0.53 | 5.9 |  |  | keep collecting (9/30) |
| money_delta+pin_value | total | 16-9 | 64.0 | 48.3 | 15.7 | +5.47 | 21.9 |  |  | keep collecting (25/30) |
| pin_value+rlm_quiet | total | 11-15 | 42.3 | 48.1 | -5.8 | -4.95 | -19.1 |  |  | keep collecting (26/30) |
| pin_value+rlm_ratio | total | 6-9 | 40.0 | 48.6 | -8.6 | -3.62 | -24.2 |  |  | keep collecting (15/30) |
| follow_move+pin_rlm | total | 24-26 | 48.0 | 48.5 | -0.5 | -4.0 | -8.0 |  |  | no edge shown yet |
| money_delta+money_level | total | 12-16 | 42.9 | 48.7 | -5.8 | -4.94 | -17.6 |  |  | keep collecting (28/30) |
| money_delta+pin_rlm | total | 13-14 | 48.1 | 47.9 | 0.3 | -2.01 | -7.4 |  |  | keep collecting (27/30) |
| money_level+pin_rlm | total | 8-8 | 50.0 | 48.6 | 1.4 | -0.68 | -4.3 |  |  | keep collecting (16/30) |
| money_level+rlm_ratio | total | 13-14 | 48.1 | 49.1 | -0.9 | -2.11 | -7.8 |  |  | keep collecting (27/30) |
| money_moving+pin_rlm | total | 26-26 | 50.0 | 48.4 | 1.6 | -2.22 | -4.3 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 26-28 | 48.1 | 48.4 | -0.3 | -4.22 | -7.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 24-27 | 47.1 | 48.5 | -1.5 | -5.0 | -9.8 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 24-26 | 48.0 | 48.5 | -0.5 | -4.0 | -8.0 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 26-28 | 48.1 | 48.4 | -0.3 | -4.22 | -7.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | total | 12-18 | 40.0 | 48.3 | -8.3 | -6.99 | -23.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | total | 2-3 | 40.0 | 48.6 | -8.6 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| pin_rlm+pin_value | total | 6-9 | 40.0 | 48.3 | -8.3 | -3.62 | -24.2 |  |  | keep collecting (15/30) |

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
| rlm_quiet | both | 56-72 | 43.8 | 37.4 | 6.3 | +10.7 | 8.4 | 0.59 | 47.7 | DROP: below break-even |
| pin_move | both | 14-25 | 35.9 | 49.6 | -13.7 | -13.19 | -33.8 | 0.39 | 43.6 | DROP: below break-even |
| money_delta | both | 14-12 | 53.8 | 40.2 | 13.7 | +5.9 | 22.7 | 0.9 | 53.8 | keep collecting (26/30) |
| pin_rlm | both | 1-4 | 20.0 | 37.4 | -17.4 | -3.07 | -61.5 | -0.3 | 60.0 | keep collecting (5/30) |
| follow_move | both | 729-676 | 51.9 | 50.8 | 1.0 | -87.75 | -6.2 | 0.15 | 40.8 | no edge shown yet |
| rlm_ratio | both | 39-34 | 53.4 | 40.3 | 13.1 | +17.55 | 24.0 | 0.53 | 53.4 | no edge shown yet |
| money_level | both | 247-173 | 58.8 | 58.2 | 0.6 | -27.89 | -6.6 | -0.23 | 37.9 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 203-187 | 52.1 | 49.0 | 3.1 | +5.84 | 1.5 | 0.28 | 44.1 | no edge shown yet |
| money_moving | both | 153-125 | 55.0 | 50.6 | 4.5 | +0.79 | 0.3 | 0.23 | 44.6 | no edge shown yet |
| pin_value | both | 73-69 | 51.4 | 48.8 | 2.6 | -4.11 | -2.9 | 0.1 | 36.6 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 52.1 | -32.1 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 366-426 | 46.2 | 49.6 | -3.4 | -87.14 | -11.0 | 0.42 | 46.5 | DROP: below break-even |
| consensus_gap+money_level | both | 58-47 | 55.2 | 62.4 | -7.2 | -15.02 | -14.3 | -0.08 | 41.0 | no edge shown yet |
| consensus_gap+money_moving | both | 28-29 | 49.1 | 49.6 | -0.5 | -5.54 | -9.7 | 0.54 | 47.4 | no edge shown yet |
| consensus_gap+pin_value | both | 30-31 | 49.2 | 47.2 | 2.0 | -4.8 | -7.9 | 0.27 | 44.3 | no edge shown yet |
| follow_move+rlm_quiet | both | 56-72 | 43.8 | 37.4 | 6.3 | +10.7 | 8.4 | 0.59 | 47.7 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 39-34 | 53.4 | 40.3 | 13.1 | +17.55 | 24.0 | 0.53 | 53.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 100-65 | 60.6 | 49.4 | 11.2 | +20.39 | 12.4 | 0.52 | 47.9 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 89-57 | 61.0 | 56.9 | 4.0 | -0.71 | -0.5 | -0.01 | 46.6 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 15-12 | 55.6 | 50.4 | 5.2 | +1.41 | 5.2 | 0.43 | 44.4 | keep collecting (27/30) |
| money_moving+pin_value | both | 13-8 | 61.9 | 50.7 | 11.2 | +3.52 | 16.7 | 0.41 | 47.6 | keep collecting (21/30) |
| rlm_quiet+rlm_ratio | both | 25-21 | 54.3 | 38.0 | 16.3 | +16.35 | 35.5 | 0.29 | 50.0 | no edge shown yet |
| rlm_quiet+sharp_gap | both | 28-27 | 50.9 | 38.4 | 12.5 | +13.08 | 23.8 | 0.41 | 49.1 | no edge shown yet |
| rlm_ratio+sharp_gap | both | 39-34 | 53.4 | 40.3 | 13.1 | +17.55 | 24.0 | 0.53 | 53.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 137-98 | 58.3 | 55.5 | 2.8 | -7.28 | -3.1 | 0.02 | 42.1 | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | both | 89-77 | 53.6 | 48.3 | 5.4 | +5.64 | 3.4 | 0.41 | 48.2 | no edge shown yet |
| money_delta+money_level | both | 4-5 | 44.4 | 43.3 | 1.2 | -0.63 | -7.0 | 1.39 | 77.8 | keep collecting (9/30) |
| money_delta+money_moving | both | 13-12 | 52.0 | 39.8 | 12.2 | +4.99 | 20.0 | 0.94 | 56.0 | keep collecting (25/30) |
| money_delta+pin_value | both | 4-1 | 80.0 | 49.9 | 30.1 | +2.52 | 50.4 | 0.2 | 40.0 | keep collecting (5/30) |
| money_delta+sharp_gap | both | 11-10 | 52.4 | 39.1 | 13.3 | +5.25 | 25.0 | 1.12 | 66.7 | keep collecting (21/30) |
| pin_value+sharp_gap | both | 15-12 | 55.6 | 50.0 | 5.6 | +1.44 | 5.3 | 0.07 | 40.7 | keep collecting (27/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 50.5 | -50.5 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 50-62 | 44.6 | 53.0 | -8.4 | -24.18 | -21.6 | 0.81 | 56.2 | DROP: below break-even |
| consensus_gap+rlm_quiet | both | 5-8 | 38.5 | 36.7 | 1.8 | -2.39 | -18.4 | 0.97 | 76.9 | keep collecting (13/30) |
| follow_move+pin_value | both | 25-23 | 52.1 | 48.8 | 3.3 | -1.0 | -2.1 | -0.15 | 29.2 | no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 43.0 | -26.4 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 42-62 | 40.4 | 49.3 | -8.9 | -17.78 | -17.1 | 0.49 | 45.2 | DROP: below break-even |
| follow_move+money_level | both | 119-64 | 65.0 | 59.0 | 6.0 | -5.43 | -3.0 | 0.06 | 42.1 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 12-13 | 48.0 | 43.7 | 4.3 | -0.66 | -2.6 | 1.06 | 64.0 | keep collecting (25/30) |
| pin_value+rlm_ratio | both | 3-2 | 60.0 | 45.6 | 14.4 | +0.73 | 14.5 | -1.16 | 40.0 | keep collecting (5/30) |
| follow_move+money_moving | both | 74-48 | 60.7 | 51.6 | 9.1 | +10.19 | 8.4 | 0.48 | 50.0 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 4-0 | 100.0 | 49.2 | 50.8 | +3.52 | 88.0 | 0.25 | 25.0 | keep collecting (4/30) |
| follow_move+money_delta | both | 8-5 | 61.5 | 39.9 | 21.6 | +7.51 | 57.8 | 1.08 | 61.5 | keep collecting (13/30) |
| money_delta+rlm_quiet | both | 4-3 | 57.1 | 34.5 | 22.7 | +5.18 | 74.0 | 0.33 | 42.9 | keep collecting (7/30) |
| money_moving+rlm_quiet | both | 20-21 | 48.8 | 38.4 | 10.3 | +6.85 | 16.7 | 0.79 | 46.3 | no edge shown yet |
| money_moving+rlm_ratio | both | 19-14 | 57.6 | 41.7 | 15.9 | +10.71 | 32.5 | 1.01 | 57.6 | no edge shown yet |
| consensus_gap+rlm_ratio | both | 5-4 | 55.6 | 40.4 | 15.1 | +1.0 | 11.1 | 0.72 | 66.7 | keep collecting (9/30) |
| pin_move+pin_value | both | 5-12 | 29.4 | 49.2 | -19.8 | -7.37 | -43.3 | 0.53 | 35.3 | keep collecting (17/30) |
| follow_move+pin_move | both | 9-11 | 45.0 | 49.1 | -4.1 | -3.39 | -16.9 | 0.52 | 50.0 | keep collecting (20/30) |
| consensus_gap+pin_move | both | 2-6 | 25.0 | 46.9 | -21.9 | -4.14 | -51.7 | 0.29 | 50.0 | keep collecting (8/30) |
| money_level+pin_move | both | 4-6 | 40.0 | 49.9 | -9.9 | -3.02 | -30.2 | 0.14 | 30.0 | keep collecting (10/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 29.1 | -29.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-3 | 25.0 | 39.5 | -14.5 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 29.1 | -29.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 29.1 | -29.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-3 | 25.0 | 39.5 | -14.5 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+sharp_gap | both | 1-4 | 20.0 | 37.4 | -17.4 | -3.07 | -61.5 | -0.3 | 60.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.5 | -51.5 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 49.5 | -49.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-4 | 33.3 | 46.8 | -13.4 | -2.87 | -47.8 | 0.47 | 33.3 | keep collecting (6/30) |
| money_level+pin_rlm | both | 1-2 | 33.3 | 43.0 | -9.7 | -1.07 | -35.8 | 0.67 | 66.7 | keep collecting (3/30) |
| pin_move+pin_rlm | both | 1-1 | 50.0 | 29.1 | 20.9 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| pin_move+rlm_ratio | both | 1-1 | 50.0 | 29.1 | 20.9 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | both | 5-3 | 62.5 | 36.7 | 25.8 | +6.9 | 86.2 | 2.04 | 87.5 | keep collecting (8/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 29.1 | -29.1 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_moving+pin_move | both | 1-1 | 50.0 | 49.5 | 0.5 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+rlm_quiet | both | 0-1 | 0.0 | 49.5 | -49.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 31-47 | 39.7 | 29.6 | 10.1 | +13.0 | 16.7 | 0.56 | 46.2 | DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.3 | 10.7 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 22-23 | 48.9 | 49.6 | -0.7 | -2.96 | -6.6 | 0.8 | 55.6 | no edge shown yet |
| pin_move | moneyline | 3-5 | 37.5 | 50.0 | -12.5 | -3.35 | -41.9 | 0.3 | 50.0 | keep collecting (8/30) |
| pin_move | spread | 2-10 | 16.7 | 48.8 | -32.1 | -8.15 | -67.9 | 0.17 | 25.0 | keep collecting (12/30) |
| pin_move | total | 9-10 | 47.4 | 50.0 | -2.6 | -1.69 | -8.9 | 0.58 | 52.6 | keep collecting (19/30) |
| money_delta | moneyline | 4-8 | 33.3 | 29.1 | 4.3 | +0.99 | 8.2 | 0.62 | 66.7 | keep collecting (12/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 9-3 | 75.0 | 49.7 | 25.3 | +5.08 | 42.3 | 1.25 | 41.7 | keep collecting (12/30) |
| pin_rlm | moneyline | 1-4 | 20.0 | 37.4 | -17.4 | -3.07 | -61.5 | -0.3 | 60.0 | keep collecting (5/30) |
| follow_move | moneyline | 304-221 | 57.9 | 52.4 | 5.5 | -22.76 | -4.3 | 0.08 | 42.7 | PROMOTE: beats break-even and its own base rate |
| follow_move | spread | 183-213 | 46.2 | 49.8 | -3.6 | -44.04 | -11.1 | 0.03 | 33.1 | DROP: below break-even |
| follow_move | total | 242-242 | 50.0 | 50.0 | 0.0 | -20.95 | -4.3 | 0.33 | 45.0 | no edge shown yet |
| rlm_ratio | moneyline | 17-21 | 44.7 | 31.3 | 13.5 | +10.27 | 27.0 | 0.41 | 52.6 | no edge shown yet |
| rlm_ratio | spread | 3-3 | 50.0 | 52.4 | -2.4 | -0.16 | -2.7 | 0.33 | 16.7 | keep collecting (6/30) |
| rlm_ratio | total | 19-10 | 65.5 | 49.6 | 16.0 | +7.44 | 25.7 | 0.72 | 62.1 | keep collecting (29/30) |
| money_level | moneyline | 137-71 | 65.9 | 66.5 | -0.6 | -25.65 | -12.3 | -0.35 | 41.3 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 18-18 | 50.0 | 48.8 | 1.2 | -1.75 | -4.8 | 0.94 | 50.0 | no edge shown yet |
| money_level | total | 92-84 | 52.3 | 50.3 | 2.0 | -0.49 | -0.3 | -0.32 | 31.2 | no edge shown yet |
| sharp_gap | moneyline | 87-99 | 46.8 | 48.0 | -1.2 | -11.49 | -6.2 | 0.22 | 48.9 | DROP: below break-even |
| sharp_gap | spread | 20-16 | 55.6 | 49.8 | 5.8 | +2.0 | 5.6 | 0.78 | 41.7 | no edge shown yet |
| sharp_gap | total | 96-72 | 57.1 | 49.9 | 7.2 | +15.32 | 9.1 | 0.23 | 39.3 | no edge shown yet |
| money_moving | moneyline | 66-63 | 51.2 | 51.5 | -0.3 | -16.2 | -12.6 | 0.21 | 51.2 | no edge shown yet |
| money_moving | spread | 18-7 | 72.0 | 49.0 | 23.0 | +9.18 | 36.7 | 0.52 | 48.0 | keep collecting (25/30) |
| money_moving | total | 69-55 | 55.6 | 50.0 | 5.7 | +7.81 | 6.3 | 0.19 | 37.1 | no edge shown yet |
| pin_value | moneyline | 2-7 | 22.2 | 38.4 | -16.2 | -5.31 | -59.0 | 0.12 | 55.6 | keep collecting (9/30) |
| pin_value | spread | 36-31 | 53.7 | 49.0 | 4.7 | +0.57 | 0.8 | 0.21 | 34.3 | no edge shown yet |
| pin_value | total | 35-31 | 53.0 | 50.0 | 3.0 | +0.63 | 1.0 | -0.02 | 36.4 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 53.6 | -20.2 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 160-231 | 40.9 | 49.8 | -8.9 | -74.81 | -19.1 | 0.22 | 44.5 | DROP: below break-even |
| consensus_gap | spread | 95-81 | 54.0 | 48.7 | 5.3 | +1.84 | 1.0 | 0.32 | 38.6 | no edge shown yet |
| consensus_gap | total | 111-114 | 49.3 | 50.0 | -0.7 | -14.17 | -6.3 | 0.86 | 56.0 | no edge shown yet |
| money_level+sharp_gap | moneyline | 64-40 | 61.5 | 62.5 | -0.9 | -15.46 | -14.9 | -0.17 | 48.1 | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+follow_move | moneyline | 23-30 | 43.4 | 57.5 | -14.1 | -16.31 | -30.8 | 0.31 | 50.9 | no edge shown yet |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 34.3 | -9.3 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| consensus_gap+rlm_quiet | moneyline | 2-6 | 25.0 | 29.1 | -4.1 | -3.08 | -38.5 | 1.07 | 87.5 | keep collecting (8/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 43.0 | -9.7 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 31-47 | 39.7 | 29.6 | 10.1 | +13.0 | 16.7 | 0.56 | 46.2 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 40-21 | 65.6 | 66.8 | -1.2 | -9.39 | -15.4 | -0.18 | 52.5 | beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 29.1 | -29.1 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 27-47 | 36.5 | 49.4 | -12.9 | -16.11 | -21.8 | 0.46 | 45.9 | DROP: below break-even |
| follow_move+money_level | moneyline | 74-24 | 75.5 | 67.1 | 8.4 | -6.39 | -6.5 | -0.21 | 40.8 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 40-21 | 65.6 | 53.8 | 11.8 | +6.09 | 10.0 | 0.34 | 50.8 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 44-34 | 56.4 | 67.2 | -10.8 | -14.37 | -18.4 | -0.28 | 41.0 | no edge shown yet |
| follow_move+sharp_gap | moneyline | 46-31 | 59.7 | 49.2 | 10.6 | +5.21 | 6.8 | 0.39 | 49.4 | no edge shown yet |
| money_moving+sharp_gap | moneyline | 31-42 | 42.5 | 46.3 | -3.8 | -12.08 | -16.5 | 0.47 | 58.9 | DROP: below break-even |
| consensus_gap+money_moving | moneyline | 15-25 | 37.5 | 50.0 | -12.5 | -13.06 | -32.7 | 0.59 | 50.0 | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 17-21 | 44.7 | 31.3 | 13.5 | +10.27 | 27.0 | 0.41 | 52.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 13-15 | 46.4 | 30.6 | 15.9 | +11.4 | 40.7 | 0.22 | 46.4 | keep collecting (28/30) |
| rlm_quiet+sharp_gap | moneyline | 13-19 | 40.6 | 30.4 | 10.2 | +7.4 | 23.1 | 0.24 | 46.9 | no edge shown yet |
| rlm_ratio+sharp_gap | moneyline | 17-21 | 44.7 | 31.3 | 13.5 | +10.27 | 27.0 | 0.41 | 52.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 29.1 | -4.1 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 10-14 | 41.7 | 30.8 | 10.8 | +4.84 | 20.2 | 1.19 | 54.2 | keep collecting (24/30) |
| money_moving+rlm_ratio | moneyline | 7-8 | 46.7 | 31.9 | 14.8 | +5.63 | 37.5 | 1.36 | 60.0 | keep collecting (15/30) |
| money_delta+money_moving | moneyline | 4-8 | 33.3 | 29.1 | 4.3 | +0.99 | 8.2 | 0.62 | 66.7 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 4-7 | 36.4 | 29.1 | 7.3 | +1.99 | 18.1 | 0.68 | 72.7 | keep collecting (11/30) |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 43.0 | -43.0 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-2 | 50.0 | 50.0 | 0.0 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| money_level+pin_move | moneyline | 2-2 | 50.0 | 50.0 | 0.0 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 29.1 | -29.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-3 | 25.0 | 39.5 | -14.5 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 29.1 | -29.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 29.1 | -29.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-3 | 25.0 | 39.5 | -14.5 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+sharp_gap | moneyline | 1-4 | 20.0 | 37.4 | -17.4 | -3.07 | -61.5 | -0.3 | 60.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 29.1 | -29.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | -1.55 | 50.0 | keep collecting (2/30) |
| pin_move+sharp_gap | moneyline | 2-1 | 66.7 | 43.0 | 23.6 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+rlm_ratio | moneyline | 4-6 | 40.0 | 33.3 | 6.7 | -1.13 | -11.3 | 0.95 | 70.0 | keep collecting (10/30) |
| money_level+pin_rlm | moneyline | 1-2 | 33.3 | 43.0 | -9.7 | -1.07 | -35.8 | 0.67 | 66.7 | keep collecting (3/30) |
| pin_move+pin_rlm | moneyline | 1-1 | 50.0 | 29.1 | 20.9 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| pin_move+rlm_ratio | moneyline | 1-1 | 50.0 | 29.1 | 20.9 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| follow_move+money_delta | moneyline | 4-2 | 66.7 | 29.1 | 37.6 | +6.99 | 116.5 | 1.02 | 66.7 | keep collecting (6/30) |
| money_delta+rlm_quiet | moneyline | 3-2 | 60.0 | 29.1 | 30.9 | +5.35 | 107.0 | 0.46 | 60.0 | keep collecting (5/30) |
| money_delta+rlm_ratio | moneyline | 4-1 | 80.0 | 29.1 | 50.9 | +7.99 | 159.8 | 2.26 | 80.0 | keep collecting (5/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 29.1 | -29.1 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-2 | 33.3 | 29.1 | 4.3 | -0.36 | -12.0 | 2.5 | 100.0 | keep collecting (3/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 70.9 | -70.9 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 70.9 | -70.9 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 46.4 | -1.0 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 46.4 | 36.9 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 15-9 | 62.5 | 47.9 | 14.6 | +3.84 | 16.0 | 0.29 | 37.5 | keep collecting (24/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.3 | 10.7 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-3 | 50.0 | 52.4 | -2.4 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-7 | 58.8 | 48.5 | 10.3 | +2.09 | 12.3 | 0.88 | 41.2 | keep collecting (17/30) |
| money_level+money_moving | spread | 10-6 | 62.5 | 48.2 | 14.3 | +3.12 | 19.5 | 1.19 | 68.8 | keep collecting (16/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.5 | -5.6 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 4-3 | 57.1 | 49.5 | 7.7 | +0.41 | 5.8 | 0.57 | 57.1 | keep collecting (7/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 3-3 | 50.0 | 52.4 | -2.4 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 53.6 | -53.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 53.6 | -53.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-12 | 53.8 | 48.9 | 4.9 | +0.62 | 2.4 | 1.15 | 46.2 | keep collecting (26/30) |
| money_moving+sharp_gap | spread | 10-5 | 66.7 | 49.3 | 17.4 | +4.04 | 26.9 | 0.87 | 53.3 | keep collecting (15/30) |
| pin_value+sharp_gap | spread | 2-2 | 50.0 | 50.0 | 0.0 | -0.26 | -6.5 | 0.75 | 75.0 | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 9-12 | 42.9 | 47.4 | -4.6 | -4.2 | -20.0 | 1.0 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 46.4 | 16.1 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 12-10 | 54.5 | 48.0 | 6.5 | +0.98 | 4.5 | 0.82 | 45.5 | keep collecting (22/30) |
| follow_move+pin_value | spread | 13-9 | 59.1 | 48.4 | 10.7 | +2.36 | 10.7 | 0.18 | 27.3 | keep collecting (22/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 46.4 | 53.6 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 46.4 | 53.6 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 46.4 | 53.6 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-3 | 75.0 | 47.6 | 27.4 | +5.22 | 43.5 | 0.75 | 50.0 | keep collecting (12/30) |
| money_delta+rlm_quiet | spread | 1-0 | 100.0 | 46.4 | 53.6 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 2-0 | 100.0 | 46.4 | 53.6 | +1.74 | 87.1 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 2-2 | 50.0 | 53.6 | -3.6 | -0.07 | -1.7 | 1.25 | 25.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | spread | 2-1 | 66.7 | 51.2 | 15.5 | +0.86 | 28.7 | 1.0 | 33.3 | keep collecting (3/30) |
| pin_move+pin_value | spread | 1-7 | 12.5 | 48.2 | -35.7 | -6.09 | -76.1 | 0.38 | 25.0 | keep collecting (8/30) |
| consensus_gap+pin_move | spread | 0-3 | 0.0 | 48.8 | -48.8 | -3.0 | -100.0 | 0.33 | 33.3 | keep collecting (3/30) |
| follow_move+pin_move | spread | 2-4 | 33.3 | 47.6 | -14.3 | -2.15 | -35.8 | 0.0 | 16.7 | keep collecting (6/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 53.6 | -53.6 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_move | spread | 1-0 | 100.0 | 46.4 | 53.6 | +0.94 | 94.3 | -1.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 22-23 | 48.9 | 49.6 | -0.7 | -2.96 | -6.6 | 0.8 | 55.6 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 39-30 | 56.5 | 50.2 | 6.3 | +5.56 | 8.1 | -0.13 | 36.2 | no edge shown yet |
| money_level+sharp_gap | total | 59-46 | 56.2 | 50.2 | 6.0 | +7.56 | 7.2 | -0.07 | 35.2 | no edge shown yet |
| money_moving+sharp_gap | total | 48-30 | 61.5 | 49.9 | 11.6 | +13.68 | 17.5 | 0.27 | 37.2 | PROMOTE: beats break-even and its own base rate |
| book_lag+pin_move | total | 0-1 | 0.0 | 50.5 | -50.5 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 12-7 | 63.2 | 50.0 | 13.2 | +3.83 | 20.2 | 0.26 | 31.6 | keep collecting (19/30) |
| money_moving+pin_value | total | 9-4 | 69.2 | 49.8 | 19.4 | +4.11 | 31.6 | 0.23 | 38.5 | keep collecting (13/30) |
| pin_value+sharp_gap | total | 13-8 | 61.9 | 50.0 | 11.9 | +3.7 | 17.6 | 0.1 | 33.3 | keep collecting (21/30) |
| follow_move+money_level | total | 33-30 | 52.4 | 50.2 | 2.2 | -0.01 | -0.0 | 0.21 | 42.9 | no edge shown yet |
| follow_move+pin_value | total | 11-12 | 47.8 | 50.0 | -2.2 | -2.08 | -9.0 | -0.3 | 30.4 | keep collecting (23/30) |
| follow_move+rlm_ratio | total | 19-10 | 65.5 | 49.6 | 16.0 | +7.44 | 25.7 | 0.72 | 62.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 44-27 | 62.0 | 49.9 | 12.1 | +13.1 | 18.4 | 0.56 | 47.9 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 6-5 | 54.5 | 49.6 | 5.0 | +0.54 | 4.9 | 1.09 | 72.7 | keep collecting (11/30) |
| pin_value+rlm_ratio | total | 3-1 | 75.0 | 49.7 | 25.3 | +1.73 | 43.2 | -0.25 | 50.0 | keep collecting (4/30) |
| rlm_ratio+sharp_gap | total | 19-10 | 65.5 | 49.6 | 16.0 | +7.44 | 25.7 | 0.72 | 62.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 25-24 | 51.0 | 49.9 | 1.2 | -1.12 | -2.3 | 0.59 | 49.0 | no edge shown yet |
| consensus_gap+money_level | total | 9-7 | 56.2 | 50.3 | 5.9 | +1.03 | 6.5 | -0.38 | 18.8 | keep collecting (16/30) |
| consensus_gap+money_moving | total | 8-3 | 72.7 | 50.0 | 22.8 | +4.2 | 38.2 | 0.18 | 36.4 | keep collecting (11/30) |
| consensus_gap+pin_value | total | 13-16 | 44.8 | 50.1 | -5.3 | -4.34 | -14.9 | 0.34 | 48.3 | keep collecting (29/30) |
| consensus_gap+sharp_gap | total | 10-12 | 45.5 | 50.0 | -4.5 | -2.98 | -13.6 | 0.0 | 31.8 | keep collecting (22/30) |
| money_moving+rlm_ratio | total | 10-5 | 66.7 | 49.6 | 17.0 | +4.22 | 28.1 | 0.67 | 60.0 | keep collecting (15/30) |
| consensus_gap+follow_move | total | 18-20 | 47.4 | 49.9 | -2.6 | -3.67 | -9.7 | 1.39 | 68.4 | no edge shown yet |
| consensus_gap+money_delta | total | 3-0 | 100.0 | 50.2 | 49.8 | +2.69 | 89.6 | 0.33 | 33.3 | keep collecting (3/30) |
| follow_move+money_delta | total | 3-3 | 50.0 | 49.7 | 0.3 | -0.31 | -5.2 | 1.33 | 66.7 | keep collecting (6/30) |
| money_delta+money_moving | total | 8-3 | 72.7 | 49.7 | 23.0 | +4.17 | 37.9 | 1.36 | 45.5 | keep collecting (11/30) |
| money_delta+pin_value | total | 3-0 | 100.0 | 49.8 | 50.2 | +2.69 | 89.6 | 0.0 | 33.3 | keep collecting (3/30) |
| money_delta+sharp_gap | total | 7-2 | 77.8 | 49.7 | 28.1 | +4.26 | 47.4 | 1.67 | 55.6 | keep collecting (9/30) |
| money_moving+rlm_quiet | total | 8-7 | 53.3 | 49.6 | 3.8 | +0.27 | 1.8 | 0.4 | 40.0 | keep collecting (15/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 11-5 | 68.8 | 49.6 | 19.2 | +5.04 | 31.5 | 0.62 | 62.5 | keep collecting (16/30) |
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
| rlm_quiet | both | 311-446 | 41.1 | 42.3 | -1.3 | -69.68 | -9.2 |  |  | DROP: below break-even |
| pin_move | both | 711-739 | 49.0 | 49.7 | -0.7 | -66.03 | -4.6 |  |  | DROP: below break-even |
| money_delta | both | 435-565 | 43.5 | 44.4 | -0.9 | -72.79 | -7.3 |  |  | DROP: below break-even |
| pin_rlm | both | 188-230 | 45.0 | 42.5 | 2.5 | +10.37 | 2.5 |  |  | DROP: below break-even |
| follow_move | both | 1216-1155 | 51.3 | 50.8 | 0.5 | -154.08 | -6.5 |  |  | no edge shown yet |
| rlm_ratio | both | 283-352 | 44.6 | 43.9 | 0.7 | -34.5 | -5.4 |  |  | DROP: below break-even |
| money_level | both | 1537-1166 | 56.9 | 55.0 | 1.8 | -106.26 | -3.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 1203-1387 | 46.4 | 47.7 | -1.3 | -200.63 | -7.7 |  |  | DROP: below break-even |
| money_moving | both | 1218-1377 | 46.9 | 48.0 | -1.1 | -190.86 | -7.4 |  |  | DROP: below break-even |
| pin_value | both | 520-523 | 49.9 | 48.5 | 1.4 | +3.41 | 0.3 |  |  | DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 51.2 | 15.5 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 478-568 | 45.7 | 49.0 | -3.3 | -88.86 | -8.5 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 172-169 | 50.4 | 51.3 | -0.8 | -22.61 | -6.6 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 199-302 | 39.7 | 46.3 | -6.5 | -45.67 | -9.1 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 123-113 | 52.1 | 50.9 | 1.2 | +14.65 | 6.2 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 31-49 | 38.8 | 39.4 | -0.6 | +9.52 | 11.9 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 182-189 | 49.1 | 46.6 | 2.5 | +9.12 | 2.5 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | both | 36-57 | 38.7 | 40.6 | -1.9 | -3.76 | -4.0 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 198-310 | 39.0 | 45.8 | -6.8 | -50.52 | -9.9 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 648-704 | 47.9 | 48.8 | -0.9 | -110.48 | -8.2 |  |  | DROP: below break-even |
| follow_move+pin_move | both | 506-545 | 48.1 | 49.8 | -1.6 | -82.65 | -7.9 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 148-173 | 46.1 | 43.7 | 2.4 | -10.28 | -3.2 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 180-174 | 50.8 | 49.2 | 1.7 | -3.62 | -1.0 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 283-352 | 44.6 | 43.9 | 0.7 | -34.5 | -5.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 649-705 | 47.9 | 48.6 | -0.7 | -104.08 | -7.7 |  |  | DROP: below break-even |
| money_moving+pin_move | both | 406-451 | 47.4 | 48.5 | -1.1 | -48.64 | -5.7 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 182-219 | 45.4 | 42.6 | 2.8 | +15.4 | 3.8 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 224-263 | 46.0 | 47.9 | -1.9 | -29.07 | -6.0 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 273-338 | 44.7 | 44.0 | 0.7 | -31.04 | -5.1 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 1160-1327 | 46.6 | 47.8 | -1.1 | -176.15 | -7.1 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 174-193 | 47.4 | 44.1 | 3.3 | +10.5 | 2.9 |  |  | DROP: below break-even |
| pin_move+pin_value | both | 224-230 | 49.3 | 49.5 | -0.2 | -19.07 | -4.2 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 156-169 | 48.0 | 45.1 | 2.9 | -1.07 | -0.3 |  |  | DROP: below break-even |
| pin_move+sharp_gap | both | 408-459 | 47.1 | 48.3 | -1.2 | -53.52 | -6.2 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 51-54 | 48.6 | 46.9 | 1.7 | +9.94 | 9.5 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 148-173 | 46.1 | 43.7 | 2.4 | -10.28 | -3.2 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 188-230 | 45.0 | 42.5 | 2.5 | +10.37 | 2.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 47-43 | 52.2 | 48.7 | 3.5 | +0.24 | 0.3 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 225-269 | 45.5 | 48.0 | -2.4 | -34.18 | -6.9 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 283-352 | 44.6 | 43.9 | 0.7 | -34.5 | -5.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 216-267 | 44.7 | 45.4 | -0.7 | -45.44 | -9.4 |  |  | DROP: below break-even |
| money_level+money_moving | both | 840-753 | 52.7 | 52.2 | 0.6 | -74.23 | -4.7 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 818-745 | 52.3 | 52.0 | 0.4 | -74.61 | -4.8 |  |  | no edge shown yet |
| follow_move+money_level | both | 734-540 | 57.6 | 55.7 | 1.9 | -65.68 | -5.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 122-110 | 52.6 | 47.9 | 4.7 | +6.85 | 3.0 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 299-227 | 56.8 | 58.0 | -1.1 | -27.0 | -5.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_move | both | 388-363 | 51.7 | 53.0 | -1.3 | -48.59 | -6.5 |  |  | no edge shown yet |
| money_level+pin_value | both | 245-236 | 50.9 | 49.9 | 1.1 | -22.52 | -4.7 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 31-66 | 32.0 | 38.2 | -6.2 | -15.07 | -15.5 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | both | 311-446 | 41.1 | 42.3 | -1.3 | -69.68 | -9.2 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 163-253 | 39.2 | 41.9 | -2.7 | -50.31 | -12.1 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 317-440 | 41.9 | 42.9 | -1.0 | -57.27 | -7.6 |  |  | DROP: below break-even |
| consensus_gap+money_delta | both | 58-120 | 32.6 | 38.8 | -6.2 | -21.12 | -11.9 |  |  | DROP: below break-even |
| money_delta+money_level | both | 147-140 | 51.2 | 47.2 | 4.0 | +13.25 | 4.6 |  |  | no edge shown yet |
| money_delta+pin_value | both | 94-86 | 52.2 | 47.8 | 4.5 | +6.92 | 3.8 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 314-434 | 42.0 | 42.9 | -0.9 | -54.44 | -7.3 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 126-212 | 37.3 | 40.6 | -3.3 | -44.49 | -13.2 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | both | 155-247 | 38.6 | 41.8 | -3.2 | -50.31 | -12.5 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 89-148 | 37.6 | 42.4 | -4.8 | -46.69 | -19.7 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | both | 147-194 | 43.1 | 43.9 | -0.8 | -25.04 | -7.3 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 65-107 | 37.8 | 40.6 | -2.8 | -25.65 | -14.9 |  |  | DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 51.2 | 15.5 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 155-187 | 45.3 | 46.3 | -1.0 | -22.49 | -6.6 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 76-62 | 55.1 | 46.9 | 8.2 | +12.58 | 9.1 |  |  | no edge shown yet |
| money_delta+pin_rlm | both | 108-131 | 45.2 | 42.6 | 2.6 | +1.31 | 0.5 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | both | 152-183 | 45.4 | 44.0 | 1.4 | -20.84 | -6.2 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | both | 41-56 | 42.3 | 47.7 | -5.4 | -7.98 | -8.2 |  |  | DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 49.5 | 50.5 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 98-195 | 33.4 | 29.8 | 3.7 | -15.3 | -5.2 |  |  | DROP: below break-even |
| rlm_quiet | spread | 71-74 | 49.0 | 51.5 | -2.5 | -8.05 | -5.6 |  |  | no edge shown yet |
| rlm_quiet | total | 142-177 | 44.5 | 49.7 | -5.2 | -46.32 | -14.5 |  |  | DROP: below break-even |
| pin_move | moneyline | 165-164 | 50.2 | 48.3 | 1.9 | +11.14 | 3.4 |  |  | no edge shown yet |
| pin_move | spread | 264-291 | 47.6 | 50.4 | -2.9 | -50.76 | -9.1 |  |  | DROP: below break-even |
| pin_move | total | 282-284 | 49.8 | 49.9 | -0.1 | -26.41 | -4.7 |  |  | no edge shown yet |
| money_delta | moneyline | 82-223 | 26.9 | 30.9 | -4.0 | -53.44 | -17.5 |  |  | DROP: below break-even |
| money_delta | spread | 146-150 | 49.3 | 51.2 | -1.9 | -16.96 | -5.7 |  |  | no edge shown yet |
| money_delta | total | 207-192 | 51.9 | 49.7 | 2.2 | -2.39 | -0.6 |  |  | no edge shown yet |
| pin_rlm | moneyline | 54-109 | 33.1 | 30.6 | 2.5 | +8.85 | 5.4 |  |  | DROP: below break-even |
| pin_rlm | spread | 31-29 | 51.7 | 51.4 | 0.2 | -0.79 | -1.3 |  |  | no edge shown yet |
| pin_rlm | total | 103-92 | 52.8 | 49.7 | 3.2 | +2.3 | 1.2 |  |  | no edge shown yet |
| follow_move | moneyline | 441-342 | 56.3 | 52.8 | 3.5 | -47.81 | -6.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 346-370 | 48.3 | 49.6 | -1.3 | -55.18 | -7.7 |  |  | DROP: below break-even |
| follow_move | total | 429-443 | 49.2 | 49.9 | -0.7 | -51.09 | -5.9 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 63-141 | 30.9 | 31.1 | -0.2 | -24.38 | -12.0 |  |  | DROP: below break-even |
| rlm_ratio | spread | 55-55 | 50.0 | 50.5 | -0.5 | -5.24 | -4.8 |  |  | no edge shown yet |
| rlm_ratio | total | 165-156 | 51.4 | 49.7 | 1.7 | -4.88 | -1.5 |  |  | no edge shown yet |
| money_level | moneyline | 599-260 | 69.7 | 66.8 | 2.9 | -47.95 | -5.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 429-438 | 49.5 | 48.9 | 0.6 | -51.67 | -6.0 |  |  | DROP: below break-even |
| money_level | total | 509-468 | 52.1 | 50.2 | 1.9 | -6.64 | -0.7 |  |  | no edge shown yet |
| sharp_gap | moneyline | 309-475 | 39.4 | 43.1 | -3.7 | -99.57 | -12.7 |  |  | DROP: below break-even |
| sharp_gap | spread | 436-424 | 50.7 | 49.5 | 1.2 | -30.84 | -3.6 |  |  | no edge shown yet |
| sharp_gap | total | 458-488 | 48.4 | 49.9 | -1.5 | -70.22 | -7.4 |  |  | DROP: below break-even |
| money_moving | moneyline | 326-454 | 41.8 | 44.2 | -2.4 | -76.62 | -9.8 |  |  | DROP: below break-even |
| money_moving | spread | 433-427 | 50.3 | 49.4 | 0.9 | -36.71 | -4.3 |  |  | no edge shown yet |
| money_moving | total | 459-496 | 48.1 | 49.9 | -1.9 | -77.53 | -8.1 |  |  | DROP: below break-even |
| pin_value | moneyline | 26-68 | 27.7 | 34.9 | -7.2 | +20.62 | 21.9 |  |  | DROP: below break-even |
| pin_value | spread | 237-217 | 52.2 | 49.5 | 2.7 | -10.54 | -2.3 |  |  | no edge shown yet |
| pin_value | total | 257-238 | 51.9 | 50.1 | 1.8 | -6.67 | -1.3 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 53.6 | 46.4 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 218-337 | 39.3 | 48.5 | -9.2 | -85.28 | -15.4 |  |  | DROP: below break-even |
| consensus_gap | spread | 115-97 | 54.2 | 48.9 | 5.3 | +1.46 | 0.7 |  |  | no edge shown yet |
| consensus_gap | total | 145-134 | 52.0 | 50.2 | 1.7 | -5.05 | -1.8 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 220-136 | 61.8 | 61.6 | 0.2 | -17.77 | -5.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 203-137 | 59.7 | 61.1 | -1.4 | -22.78 | -6.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 290-435 | 40.0 | 43.1 | -3.1 | -73.02 | -10.1 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 76-90 | 45.8 | 53.3 | -7.5 | -27.56 | -16.6 |  |  | DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 10-49 | 16.9 | 30.5 | -13.5 | -16.86 | -28.6 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 98-195 | 33.4 | 29.8 | 3.7 | -15.3 | -5.2 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 155-95 | 62.0 | 67.4 | -5.4 | -20.57 | -8.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 79-185 | 29.9 | 43.3 | -13.4 | -33.47 | -12.7 |  |  | !! CHECK: consensus_gap+money_moving close moneyline all sits -13.4 pts from its base (43.3%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+money_level | moneyline | 316-122 | 72.1 | 67.7 | 4.5 | -26.65 | -6.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+money_moving | moneyline | 165-189 | 46.6 | 46.6 | 0.0 | -34.42 | -9.7 |  |  | DROP: below break-even |
| money_delta+money_moving | moneyline | 76-201 | 27.4 | 30.4 | -3.0 | -37.74 | -13.6 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 74-200 | 27.0 | 30.5 | -3.4 | -38.93 | -14.2 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 77-193 | 28.5 | 42.4 | -13.9 | -39.2 | -14.5 |  |  | !! CHECK: consensus_gap+sharp_gap close moneyline all sits -13.9 pts from its base (42.4%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+sharp_gap | moneyline | 157-191 | 45.1 | 45.7 | -0.6 | -37.45 | -10.8 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | moneyline | 46-117 | 28.2 | 29.6 | -1.4 | -20.19 | -12.4 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 47-119 | 28.3 | 29.6 | -1.3 | -22.59 | -13.6 |  |  | DROP: below break-even |
| consensus_gap+pin_move | moneyline | 51-45 | 53.1 | 52.6 | 0.5 | +19.64 | 20.5 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 14-33 | 29.8 | 31.8 | -2.0 | +10.53 | 22.4 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 7-39 | 15.2 | 30.9 | -15.7 | -11.26 | -24.5 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 129-122 | 51.4 | 49.1 | 2.3 | -3.86 | -1.5 |  |  | no edge shown yet |
| follow_move+pin_rlm | moneyline | 37-69 | 34.9 | 31.1 | 3.9 | -8.12 | -7.7 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 63-141 | 30.9 | 31.1 | -0.2 | -24.38 | -12.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 70-92 | 43.2 | 42.5 | 0.7 | +5.04 | 3.1 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 53-102 | 34.2 | 30.7 | 3.5 | +14.45 | 9.3 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 61-133 | 31.4 | 31.2 | 0.2 | -19.5 | -10.1 |  |  | DROP: below break-even |
| pin_move+pin_rlm | moneyline | 40-72 | 35.7 | 30.6 | 5.1 | +8.99 | 8.0 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 44-66 | 40.0 | 30.2 | 9.8 | +7.7 | 7.0 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 31-55 | 36.0 | 31.5 | 4.5 | -1.38 | -1.6 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 68-98 | 41.0 | 41.7 | -0.7 | -1.53 | -0.9 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 24-57 | 29.6 | 30.1 | -0.5 | -13.26 | -16.4 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 37-69 | 34.9 | 31.1 | 3.9 | -8.12 | -7.7 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 54-109 | 33.1 | 30.6 | 2.5 | +8.85 | 5.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 42-113 | 27.1 | 29.6 | -2.5 | -22.43 | -14.5 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 63-141 | 30.9 | 31.1 | -0.2 | -24.38 | -12.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 17-88 | 16.2 | 30.7 | -14.5 | -24.95 | -23.8 |  |  | DROP: below break-even |
| consensus_gap+pin_value | moneyline | 17-52 | 24.6 | 33.3 | -8.7 | +2.23 | 3.2 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 25-49 | 33.8 | 31.9 | 1.9 | -3.3 | -4.5 |  |  | DROP: below break-even |
| money_delta+pin_rlm | moneyline | 31-62 | 33.3 | 30.9 | 2.5 | -0.09 | -0.1 |  |  | DROP: below break-even |
| money_delta+pin_value | moneyline | 4-18 | 18.2 | 29.1 | -10.9 | -5.3 | -24.1 |  |  | keep collecting (22/30) |
| money_moving+pin_value | moneyline | 13-37 | 26.0 | 33.3 | -7.3 | +10.89 | 21.8 |  |  | DROP: below break-even |
| pin_move+pin_value | moneyline | 9-13 | 40.9 | 40.5 | 0.4 | +6.3 | 28.6 |  |  | keep collecting (22/30) |
| pin_rlm+pin_value | moneyline | 6-11 | 35.3 | 29.1 | 6.2 | +12.45 | 73.2 |  |  | keep collecting (17/30) |
| pin_value+sharp_gap | moneyline | 13-41 | 24.1 | 34.5 | -10.4 | +6.89 | 12.8 |  |  | DROP: below break-even |
| follow_move+money_delta | moneyline | 42-86 | 32.8 | 32.7 | 0.1 | -23.18 | -18.1 |  |  | DROP: below break-even |
| money_delta+money_level | moneyline | 23-28 | 45.1 | 34.8 | 10.3 | +12.68 | 24.9 |  |  | no edge shown yet |
| money_delta+rlm_ratio | moneyline | 34-74 | 31.5 | 31.8 | -0.3 | -19.27 | -17.8 |  |  | DROP: below break-even |
| money_level+pin_move | moneyline | 96-60 | 61.5 | 65.3 | -3.7 | -9.88 | -6.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 14-14 | 50.0 | 35.1 | 14.9 | +3.97 | 14.2 |  |  | keep collecting (28/30) |
| money_level+rlm_ratio | moneyline | 17-21 | 44.7 | 37.9 | 6.8 | +0.43 | 1.1 |  |  | no edge shown yet |
| money_delta+rlm_quiet | moneyline | 28-66 | 29.8 | 30.4 | -0.6 | -20.84 | -22.2 |  |  | DROP: below break-even |
| money_level+pin_value | moneyline | 6-8 | 42.9 | 64.9 | -22.1 | -4.75 | -33.9 |  |  | keep collecting (14/30) |
| follow_move+pin_value | moneyline | 5-10 | 33.3 | 40.2 | -6.9 | +4.75 | 31.7 |  |  | keep collecting (15/30) |
| pin_value+rlm_quiet | moneyline | 3-7 | 30.0 | 29.1 | 0.9 | +6.5 | 65.0 |  |  | keep collecting (10/30) |
| pin_value+rlm_ratio | moneyline | 2-3 | 40.0 | 29.1 | 10.9 | -0.1 | -2.0 |  |  | keep collecting (5/30) |
| consensus_gap+follow_move | spread | 41-33 | 55.4 | 48.2 | 7.2 | +2.05 | 2.8 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 55-52 | 51.4 | 48.7 | 2.7 | -5.05 | -4.7 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 33-39 | 45.8 | 49.3 | -3.5 | -10.7 | -14.9 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 5-5 | 50.0 | 50.7 | -0.7 | -0.7 | -7.0 |  |  | keep collecting (10/30) |
| consensus_gap+pin_value | spread | 81-61 | 57.0 | 48.9 | 8.1 | +8.27 | 5.8 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 7-5 | 58.3 | 50.6 | 7.7 | +0.92 | 7.7 |  |  | keep collecting (12/30) |
| consensus_gap+sharp_gap | spread | 54-52 | 50.9 | 48.9 | 2.0 | -5.95 | -5.6 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 202-207 | 49.4 | 49.2 | 0.2 | -24.37 | -6.0 |  |  | no edge shown yet |
| follow_move+pin_move | spread | 165-197 | 45.6 | 50.1 | -4.5 | -46.64 | -12.9 |  |  | DROP: below break-even |
| follow_move+pin_rlm | spread | 22-23 | 48.9 | 50.9 | -2.0 | -2.92 | -6.5 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 76-70 | 52.1 | 49.0 | 3.1 | -3.7 | -2.5 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 55-55 | 50.0 | 50.5 | -0.5 | -5.24 | -4.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 203-206 | 49.6 | 49.3 | 0.4 | -22.24 | -5.4 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 149-166 | 47.3 | 49.9 | -2.6 | -31.37 | -10.0 |  |  | DROP: below break-even |
| money_moving+pin_rlm | spread | 29-29 | 50.0 | 51.4 | -1.4 | -2.62 | -4.5 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 108-116 | 48.2 | 49.1 | -0.9 | -22.7 | -10.1 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 53-54 | 49.5 | 50.4 | -0.9 | -6.17 | -5.8 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 428-419 | 50.5 | 49.4 | 1.1 | -33.21 | -3.9 |  |  | no edge shown yet |
| pin_move+pin_rlm | spread | 31-29 | 51.7 | 51.4 | 0.2 | -0.79 | -1.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 105-111 | 48.6 | 50.0 | -1.4 | -18.64 | -8.6 |  |  | no edge shown yet |
| pin_move+rlm_ratio | spread | 28-31 | 47.5 | 50.8 | -3.3 | -5.61 | -9.5 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 152-166 | 47.8 | 49.9 | -2.1 | -28.64 | -9.0 |  |  | DROP: below break-even |
| pin_rlm+pin_value | spread | 11-13 | 45.8 | 51.8 | -6.0 | -3.28 | -13.7 |  |  | keep collecting (24/30) |
| pin_rlm+rlm_ratio | spread | 22-23 | 48.9 | 50.9 | -2.0 | -2.92 | -6.5 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 31-29 | 51.7 | 51.4 | 0.2 | -0.79 | -1.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 9-9 | 50.0 | 50.0 | -0.0 | -1.26 | -7.0 |  |  | keep collecting (18/30) |
| pin_value+sharp_gap | spread | 108-116 | 48.2 | 49.2 | -1.0 | -22.76 | -10.2 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 55-55 | 50.0 | 50.5 | -0.5 | -5.24 | -4.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 188-200 | 48.5 | 48.7 | -0.3 | -30.15 | -7.8 |  |  | DROP: below break-even |
| money_level+rlm_ratio | spread | 31-33 | 48.4 | 50.0 | -1.6 | -5.19 | -8.1 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 330-325 | 50.4 | 48.9 | 1.5 | -28.09 | -4.3 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 67-59 | 53.2 | 48.2 | 4.9 | -1.68 | -1.3 |  |  | no edge shown yet |
| money_level+money_moving | spread | 329-326 | 50.2 | 48.9 | 1.3 | -30.01 | -4.6 |  |  | no edge shown yet |
| money_level+pin_move | spread | 131-158 | 45.3 | 49.4 | -4.1 | -40.13 | -13.9 |  |  | DROP: below break-even |
| money_level+pin_value | spread | 114-119 | 48.9 | 48.6 | 0.4 | -20.73 | -8.9 |  |  | no edge shown yet |
| consensus_gap+money_delta | spread | 17-16 | 51.5 | 51.2 | 0.3 | -1.46 | -4.4 |  |  | no edge shown yet |
| follow_move+money_delta | spread | 49-59 | 45.4 | 50.6 | -5.2 | -14.74 | -13.6 |  |  | no edge shown yet |
| money_delta+money_level | spread | 49-48 | 50.5 | 50.0 | 0.6 | -3.93 | -4.1 |  |  | no edge shown yet |
| money_delta+money_moving | spread | 85-92 | 48.0 | 50.7 | -2.6 | -15.3 | -8.6 |  |  | no edge shown yet |
| money_delta+pin_value | spread | 40-32 | 55.6 | 51.1 | 4.5 | +3.01 | 4.2 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 84-90 | 48.3 | 50.6 | -2.3 | -14.28 | -8.2 |  |  | no edge shown yet |
| follow_move+rlm_quiet | spread | 71-74 | 49.0 | 51.5 | -2.5 | -8.05 | -5.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 17-8 | 68.0 | 51.9 | 16.1 | +7.45 | 29.8 |  |  | keep collecting (25/30) |
| rlm_quiet+sharp_gap | spread | 32-20 | 61.5 | 51.8 | 9.7 | +9.28 | 17.9 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 16-16 | 50.0 | 50.4 | -0.4 | -1.61 | -5.0 |  |  | no edge shown yet |
| money_delta+pin_move | spread | 44-54 | 44.9 | 51.5 | -6.6 | -13.99 | -14.3 |  |  | no edge shown yet |
| money_delta+rlm_ratio | spread | 20-31 | 39.2 | 50.2 | -11.0 | -13.27 | -26.0 |  |  | DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 53.6 | 46.4 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_rlm | spread | 17-20 | 45.9 | 51.5 | -5.5 | -4.7 | -12.7 |  |  | no edge shown yet |
| money_delta+rlm_quiet | spread | 20-22 | 47.6 | 51.9 | -4.3 | -3.47 | -8.3 |  |  | no edge shown yet |
| money_moving+rlm_quiet | spread | 31-20 | 60.8 | 51.8 | 9.0 | +8.33 | 16.3 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 39-41 | 48.8 | 52.0 | -3.2 | -4.68 | -5.9 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | spread | 7-3 | 70.0 | 52.9 | 17.1 | +3.47 | 34.7 |  |  | keep collecting (10/30) |
| consensus_gap+rlm_quiet | spread | 4-3 | 57.1 | 51.5 | 5.6 | +0.48 | 6.9 |  |  | keep collecting (7/30) |
| pin_value+rlm_quiet | spread | 8-8 | 50.0 | 50.4 | -0.4 | -0.94 | -5.9 |  |  | keep collecting (16/30) |
| follow_move+money_delta | total | 125-122 | 50.6 | 49.7 | 0.9 | -7.52 | -3.0 |  |  | no edge shown yet |
| money_level+money_moving | total | 291-291 | 50.0 | 50.1 | -0.1 | -26.45 | -4.5 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 285-283 | 50.2 | 50.1 | 0.1 | -23.73 | -4.2 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 442-473 | 48.3 | 49.9 | -1.6 | -69.91 | -7.6 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 77-73 | 51.3 | 50.4 | 0.9 | -4.75 | -3.2 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 39-29 | 57.4 | 50.2 | 7.2 | +5.71 | 8.4 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 84-76 | 52.5 | 50.2 | 2.3 | -1.37 | -0.9 |  |  | no edge shown yet |
| follow_move+money_moving | total | 281-308 | 47.7 | 49.9 | -2.2 | -51.69 | -8.8 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 289-308 | 48.4 | 49.9 | -1.5 | -44.39 | -7.4 |  |  | DROP: below break-even |
| money_level+pin_move | total | 161-145 | 52.6 | 50.0 | 2.6 | +1.41 | 0.5 |  |  | no edge shown yet |
| money_level+pin_value | total | 125-109 | 53.4 | 50.3 | 3.2 | +2.96 | 1.3 |  |  | no edge shown yet |
| pin_move+pin_value | total | 110-106 | 50.9 | 50.0 | 0.9 | -6.73 | -3.1 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 142-177 | 44.5 | 49.7 | -5.2 | -46.32 | -14.5 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 187-193 | 49.2 | 49.9 | -0.7 | -22.31 | -5.9 |  |  | no edge shown yet |
| rlm_quiet+sharp_gap | total | 84-114 | 42.4 | 49.6 | -7.2 | -37.0 | -18.7 |  |  | DROP: below break-even |
| money_delta+money_moving | total | 156-147 | 51.5 | 49.7 | 1.8 | -4.23 | -1.4 |  |  | no edge shown yet |
| follow_move+money_level | total | 230-218 | 51.3 | 50.1 | 1.2 | -8.88 | -2.0 |  |  | no edge shown yet |
| follow_move+pin_value | total | 99-94 | 51.3 | 50.0 | 1.3 | -4.68 | -2.4 |  |  | no edge shown yet |
| money_moving+pin_value | total | 103-110 | 48.4 | 50.0 | -1.7 | -17.26 | -8.1 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 104-112 | 48.1 | 50.0 | -1.9 | -18.31 | -8.5 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 65-65 | 50.0 | 50.2 | -0.2 | -7.15 | -5.5 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 67-65 | 50.8 | 50.2 | 0.6 | -5.36 | -4.1 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 55-46 | 54.5 | 50.2 | 4.2 | +2.9 | 2.9 |  |  | no edge shown yet |
| consensus_gap+money_delta | total | 24-16 | 60.0 | 49.9 | 10.1 | +5.28 | 13.2 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | total | 17-14 | 54.8 | 49.8 | 5.1 | +1.31 | 4.2 |  |  | no edge shown yet |
| money_delta+rlm_quiet | total | 41-60 | 40.6 | 49.6 | -9.0 | -22.38 | -22.2 |  |  | DROP: below break-even |
| money_delta+sharp_gap | total | 156-144 | 52.0 | 49.7 | 2.3 | -1.23 | -0.4 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 78-110 | 41.5 | 49.6 | -8.2 | -38.45 | -20.5 |  |  | DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 75-64 | 54.0 | 49.8 | 4.2 | +4.5 | 3.2 |  |  | no edge shown yet |
| money_delta+pin_move | total | 86-84 | 50.6 | 49.6 | 1.0 | -5.19 | -3.1 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 188-195 | 49.1 | 49.9 | -0.8 | -23.35 | -6.1 |  |  | no edge shown yet |
| follow_move+pin_move | total | 212-226 | 48.4 | 49.9 | -1.5 | -32.15 | -7.3 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | total | 30-41 | 42.3 | 49.7 | -7.4 | -13.53 | -19.1 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | total | 12-11 | 52.2 | 50.0 | 2.2 | -0.31 | -1.4 |  |  | keep collecting (23/30) |
| consensus_gap+rlm_ratio | total | 22-13 | 62.9 | 50.0 | 12.8 | +6.57 | 18.8 |  |  | no edge shown yet |
| follow_move+pin_rlm | total | 89-81 | 52.4 | 49.7 | 2.7 | +0.76 | 0.4 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 165-156 | 51.4 | 49.7 | 1.7 | -4.88 | -1.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 46-32 | 59.0 | 49.7 | 9.3 | +10.22 | 13.1 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 74-56 | 56.9 | 49.8 | 7.1 | +11.61 | 8.9 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 100-88 | 53.2 | 49.7 | 3.5 | +3.57 | 1.9 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 159-151 | 51.3 | 49.7 | 1.6 | -5.37 | -1.7 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 103-92 | 52.8 | 49.7 | 3.2 | +2.3 | 1.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 97-83 | 53.9 | 49.7 | 4.2 | +5.92 | 3.3 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 34-30 | 53.1 | 49.7 | 3.4 | +0.77 | 1.2 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 89-81 | 52.4 | 49.7 | 2.7 | +0.76 | 0.4 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 103-92 | 52.8 | 49.7 | 3.2 | +2.3 | 1.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 36-31 | 53.7 | 49.8 | 3.9 | +1.6 | 2.4 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 165-156 | 51.4 | 49.7 | 1.7 | -4.88 | -1.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 60-49 | 55.0 | 49.6 | 5.4 | +6.1 | 5.6 |  |  | no edge shown yet |
| money_delta+rlm_ratio | total | 98-78 | 55.7 | 49.7 | 6.0 | +11.69 | 6.6 |  |  | no edge shown yet |
| money_delta+pin_value | total | 50-36 | 58.1 | 49.8 | 8.4 | +9.2 | 10.7 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 64-87 | 42.4 | 49.7 | -7.3 | -28.06 | -18.6 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | total | 34-47 | 42.0 | 49.6 | -7.7 | -15.85 | -19.6 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | total | 67-91 | 42.4 | 49.6 | -7.2 | -29.5 | -18.7 |  |  | DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 49.5 | 50.5 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| rlm_quiet | close | 1-3k bets | 189-280 | 40.3 | -2.0 | -8.0 |  |
| rlm_quiet | close | 3k+ bets | 90-119 | 43.1 | 0.5 | -9.2 |  |
| rlm_quiet | close | <1k bets | 32-47 | 40.5 | -1.6 | -16.0 |  |
| rlm_quiet | close | pin $1-2k | 81-136 | 37.3 | -6.5 | -18.2 |  |
| rlm_quiet | close | pin $2k+ | 98-116 | 45.8 | 7.1 | 4.1 |  |
| rlm_quiet | close | pin limit <$1k | 51-55 | 48.1 | -1.3 | -7.6 |  |
| pin_move | close | 1-3k bets | 440-445 | 49.7 | 0.1 | -2.3 |  |
| pin_move | close | 3k+ bets | 184-204 | 47.4 | -2.4 | -9.0 |  |
| pin_move | close | <1k bets | 87-87 | 50.0 | -0.3 | -4.3 |  |
| pin_move | close | pin $1-2k | 319-337 | 48.6 | -1.4 | -4.7 |  |
| pin_move | close | pin $2k+ | 267-285 | 48.4 | -1.1 | -6.7 |  |
| pin_move | close | pin limit <$1k | 125-117 | 51.7 | 2.0 | 0.6 |  |
| money_delta | close | 1-3k bets | 261-335 | 43.8 | -1.1 | -7.6 |  |
| money_delta | close | 3k+ bets | 122-154 | 44.2 | 0.3 | -2.9 |  |
| money_delta | close | <1k bets | 52-76 | 40.6 | -2.5 | -15.4 |  |
| money_delta | close | pin $1-2k | 156-154 | 50.3 | 3.9 | 4.6 |  |
| money_delta | close | pin $2k+ | 114-150 | 43.2 | 1.4 | -8.6 |  |
| money_delta | close | pin limit <$1k | 63-73 | 46.3 | -3.0 | -8.0 |  |
| pin_rlm | close | 1-3k bets | 114-135 | 45.8 | 3.3 | 8.5 |  |
| pin_rlm | close | 3k+ bets | 48-69 | 41.0 | -1.6 | -12.7 |  |
| pin_rlm | close | <1k bets | 26-26 | 50.0 | 7.6 | 7.9 |  |
| pin_rlm | close | pin $1-2k | 80-92 | 46.5 | 2.3 | 4.8 |  |
| pin_rlm | close | pin $2k+ | 58-97 | 37.4 | 0.5 | -7.5 |  |
| pin_rlm | close | pin limit <$1k | 50-41 | 54.9 | 6.1 | 15.1 |  |
| follow_move | close | 1-3k bets | 753-716 | 51.3 | 0.7 | -5.6 |  |
| follow_move | close | 3k+ bets | 299-282 | 51.5 | 0.8 | -5.4 |  |
| follow_move | close | <1k bets | 164-154 | 51.6 | -0.4 | -11.8 |  |
| follow_move | close | pin $1-2k | 360-414 | 46.5 | -3.9 | -12.8 |  |
| follow_move | close | pin $2k+ | 333-295 | 53.0 | 2.3 | -2.5 |  |
| follow_move | close | pin limit <$1k | 150-145 | 50.8 | 1.0 | -3.1 |  |
| rlm_ratio | close | 1-3k bets | 174-232 | 42.9 | -1.0 | -7.5 |  |
| rlm_ratio | close | 3k+ bets | 73-82 | 47.1 | 3.1 | -1.2 |  |
| rlm_ratio | close | <1k bets | 36-38 | 48.6 | 5.2 | -3.3 |  |
| rlm_ratio | close | pin $1-2k | 98-107 | 47.8 | 2.0 | -0.6 |  |
| rlm_ratio | close | pin $2k+ | 57-85 | 40.1 | 1.6 | -12.1 |  |
| rlm_ratio | close | pin limit <$1k | 54-51 | 51.4 | 2.3 | -0.8 |  |
| money_level | close | 1-3k bets | 961-701 | 57.8 | 2.7 | -2.6 |  |
| money_level | close | 3k+ bets | 371-312 | 54.3 | -0.4 | -5.5 |  |
| money_level | close | <1k bets | 205-149 | 57.9 | 2.6 | -6.2 |  |
| money_level | close | pin $1-2k | 447-400 | 52.8 | -0.8 | -6.4 |  |
| money_level | close | pin $2k+ | 404-333 | 54.8 | -1.9 | -9.1 |  |
| money_level | close | pin limit <$1k | 179-158 | 53.1 | 2.8 | 0.8 |  |
| sharp_gap | close | 1-3k bets | 729-859 | 45.9 | -1.7 | -8.9 |  |
| sharp_gap | close | 3k+ bets | 314-348 | 47.4 | -0.1 | -2.6 |  |
| sharp_gap | close | <1k bets | 160-176 | 47.6 | -0.6 | -11.1 |  |
| sharp_gap | close | pin $1-2k | 388-426 | 47.7 | -1.0 | -5.8 |  |
| sharp_gap | close | pin $2k+ | 324-385 | 45.7 | -1.0 | -6.2 |  |
| sharp_gap | close | pin limit <$1k | 154-169 | 47.7 | -1.8 | -5.9 |  |
| money_moving | close | 1-3k bets | 743-852 | 46.6 | -1.5 | -8.4 |  |
| money_moving | close | 3k+ bets | 317-347 | 47.7 | -0.2 | -3.2 |  |
| money_moving | close | <1k bets | 158-174 | 47.6 | -0.4 | -9.8 |  |
| money_moving | close | pin $1-2k | 389-427 | 47.7 | -1.3 | -6.0 |  |
| money_moving | close | pin $2k+ | 330-379 | 46.5 | -0.2 | -5.1 |  |
| money_moving | close | pin limit <$1k | 154-175 | 46.8 | -2.7 | -7.6 |  |
| pin_value | close | 1-3k bets | 331-323 | 50.6 | 2.2 | 2.9 |  |
| pin_value | close | 3k+ bets | 115-141 | 44.9 | -4.2 | -12.8 |  |
| pin_value | close | <1k bets | 72-58 | 55.4 | 8.0 | 12.3 |  |
| pin_value | close | pin $1-2k | 237-261 | 47.6 | -1.0 | -4.5 |  |
| pin_value | close | pin $2k+ | 152-170 | 47.2 | -0.0 | -1.3 |  |
| pin_value | close | pin limit <$1k | 131-92 | 58.7 | 8.9 | 13.4 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 46.4 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 46.4 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 296-346 | 46.1 | -3.2 | -9.2 |  |
| consensus_gap | close | 3k+ bets | 123-134 | 47.9 | -2.5 | -0.0 |  |
| consensus_gap | close | <1k bets | 58-86 | 40.3 | -5.1 | -19.8 |  |
| consensus_gap | close | pin $1-2k | 140-148 | 48.6 | -1.1 | 0.2 |  |
| consensus_gap | close | pin $2k+ | 146-141 | 50.9 | -1.2 | 0.7 |  |
| consensus_gap | close | pin limit <$1k | 60-56 | 51.7 | 1.7 | 0.6 |  |
| consensus_gap+follow_move | close | 1-3k bets | 110-106 | 50.9 | -0.3 | -4.3 |  |
| consensus_gap+money_level | close | 1-3k bets | 194-133 | 59.3 | 1.0 | -0.5 |  |
| consensus_gap+money_moving | close | 1-3k bets | 124-185 | 40.1 | -6.3 | -11.4 |  |
| consensus_gap+pin_move | close | 1-3k bets | 76-67 | 53.1 | 2.7 | 11.4 |  |
| consensus_gap+pin_value | close | 1-3k bets | 115-128 | 47.3 | 0.7 | -2.0 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 122-190 | 39.1 | -6.8 | -12.9 |  |
| follow_move+money_level | close | 1-3k bets | 471-340 | 58.1 | 2.6 | -3.9 |  |
| follow_move+money_moving | close | 1-3k bets | 411-449 | 47.8 | -1.0 | -7.9 |  |
| follow_move+pin_move | close | 1-3k bets | 308-337 | 47.8 | -1.8 | -8.5 |  |
| follow_move+pin_value | close | 1-3k bets | 109-104 | 51.2 | 2.3 | 1.5 |  |
| follow_move+sharp_gap | close | 1-3k bets | 412-450 | 47.8 | -0.8 | -7.3 |  |
| money_level+money_moving | close | 1-3k bets | 529-466 | 53.2 | 1.0 | -3.7 |  |
| money_level+pin_move | close | 1-3k bets | 253-223 | 53.2 | 0.5 | -3.4 |  |
| money_level+pin_value | close | 1-3k bets | 158-140 | 53.0 | 3.4 | -0.5 |  |
| money_level+sharp_gap | close | 1-3k bets | 510-460 | 52.6 | 0.6 | -4.0 |  |
| money_moving+pin_move | close | 1-3k bets | 257-271 | 48.7 | 0.0 | -2.6 |  |
| money_moving+pin_value | close | 1-3k bets | 141-163 | 46.4 | -1.5 | -6.2 |  |
| money_moving+sharp_gap | close | 1-3k bets | 701-817 | 46.2 | -1.6 | -8.1 |  |
| pin_move+pin_value | close | 1-3k bets | 139-136 | 50.5 | 0.9 | -1.5 |  |
| pin_move+sharp_gap | close | 1-3k bets | 261-277 | 48.5 | 0.1 | -2.6 |  |
| pin_value+sharp_gap | close | 1-3k bets | 142-169 | 45.7 | -2.1 | -7.7 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 189-280 | 40.3 | -2.0 | -8.0 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 93-165 | 36.0 | -5.5 | -14.8 |  |
| consensus_gap+money_delta | close | 1-3k bets | 34-70 | 32.7 | -6.4 | -17.2 |  |
| follow_move+money_delta | close | 1-3k bets | 130-165 | 44.1 | -2.0 | -10.9 |  |
| money_delta+money_level | close | 1-3k bets | 92-88 | 51.1 | 3.1 | 4.8 |  |
| money_delta+money_moving | close | 1-3k bets | 189-265 | 41.6 | -1.6 | -9.1 |  |
| money_delta+pin_value | close | 1-3k bets | 57-52 | 52.3 | 4.4 | 4.0 |  |
| money_delta+sharp_gap | close | 1-3k bets | 188-262 | 41.8 | -1.5 | -8.8 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 92-107 | 46.2 | -0.5 | -2.7 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 22-30 | 42.3 | 2.9 | 21.3 |  |
| money_level+pin_rlm | close | 1-3k bets | 49-39 | 55.7 | 7.9 | 7.6 |  |
| pin_move+pin_rlm | close | 1-3k bets | 105-113 | 48.2 | 4.2 | 6.6 |  |
| pin_rlm+pin_value | close | 1-3k bets | 33-30 | 52.4 | 5.7 | 22.8 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 114-135 | 45.8 | 3.3 | 8.5 |  |
| money_delta+pin_rlm | close | 1-3k bets | 64-76 | 45.7 | 2.9 | 5.6 |  |
| money_moving+pin_rlm | close | 1-3k bets | 109-127 | 46.2 | 3.5 | 10.2 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 27-38 | 41.5 | 0.5 | 4.9 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 174-232 | 42.9 | -1.0 | -7.5 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 91-122 | 42.7 | -1.7 | -11.6 |  |
| money_level+rlm_ratio | close | 1-3k bets | 79-74 | 51.6 | 3.1 | -0.2 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 167-221 | 43.0 | -1.0 | -6.7 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 90-100 | 47.4 | 2.5 | -1.2 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 30-27 | 52.6 | 4.8 | 1.6 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 174-232 | 42.9 | -1.0 | -7.5 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 18-42 | 30.0 | -7.2 | -12.6 |  |
| follow_move+pin_rlm | close | 1-3k bets | 84-107 | 44.0 | 0.4 | -7.4 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 87-161 | 35.1 | -6.3 | -16.2 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 84-121 | 41.0 | -2.9 | -11.1 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 35-68 | 34.0 | -5.8 | -20.2 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 84-107 | 44.0 | 0.4 | -7.4 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 73-142 | 34.0 | -6.2 | -16.1 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 50-93 | 35.0 | -8.0 | -23.8 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 22-30 | 42.3 | -4.0 | 1.4 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 50.5 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 48-42 | 53.3 | 1.8 | -1.1 |  |
| consensus_gap+money_moving | close | 3k+ bets | 50-76 | 39.7 | -7.4 | 1.8 |  |
| consensus_gap+pin_move | close | 3k+ bets | 39-33 | 54.2 | 2.4 | 2.8 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 6-12 | 33.3 | -9.4 | -15.3 |  |
| consensus_gap+pin_value | close | 3k+ bets | 47-45 | 51.1 | 3.2 | 2.9 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 6-12 | 33.3 | -7.8 | -15.0 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 50-77 | 39.4 | -7.3 | 3.1 |  |
| follow_move+money_moving | close | 3k+ bets | 161-171 | 48.5 | -0.1 | -6.6 |  |
| follow_move+pin_move | close | 3k+ bets | 142-148 | 49.0 | -0.9 | -5.7 |  |
| follow_move+pin_rlm | close | 3k+ bets | 44-50 | 46.8 | 3.1 | 0.6 |  |
| follow_move+pin_value | close | 3k+ bets | 48-54 | 47.1 | -2.7 | -11.3 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 73-82 | 47.1 | 3.1 | -1.2 |  |
| follow_move+sharp_gap | close | 3k+ bets | 160-170 | 48.5 | 0.5 | -5.1 |  |
| money_moving+pin_move | close | 3k+ bets | 102-127 | 44.5 | -3.7 | -12.9 |  |
| money_moving+pin_rlm | close | 3k+ bets | 47-66 | 41.6 | -0.9 | -11.4 |  |
| money_moving+pin_value | close | 3k+ bets | 60-78 | 43.5 | -5.3 | -13.2 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 70-79 | 47.0 | 3.0 | -1.6 |  |
| money_moving+sharp_gap | close | 3k+ bets | 305-335 | 47.7 | -0.0 | -2.4 |  |
| pin_move+pin_rlm | close | 3k+ bets | 45-59 | 43.3 | -1.0 | -8.3 |  |
| pin_move+pin_value | close | 3k+ bets | 53-69 | 43.4 | -6.2 | -18.0 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 46-51 | 47.4 | 2.2 | 0.3 |  |
| pin_move+sharp_gap | close | 3k+ bets | 100-128 | 43.9 | -4.0 | -13.1 |  |
| pin_rlm+pin_value | close | 3k+ bets | 11-21 | 34.4 | -14.0 | -34.7 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 44-50 | 46.8 | 3.1 | 0.6 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 48-69 | 41.0 | -1.6 | -12.7 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 12-15 | 44.4 | -6.0 | -15.5 |  |
| pin_value+sharp_gap | close | 3k+ bets | 60-79 | 43.2 | -5.8 | -13.8 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 73-82 | 47.1 | 3.1 | -1.2 |  |
| follow_move+money_delta | close | 3k+ bets | 60-73 | 45.1 | 0.5 | -7.8 |  |
| money_level+money_moving | close | 3k+ bets | 201-188 | 51.7 | -0.4 | -4.3 |  |
| money_level+sharp_gap | close | 3k+ bets | 195-185 | 51.3 | -0.4 | -3.8 |  |
| follow_move+money_level | close | 3k+ bets | 164-125 | 56.7 | 0.9 | -4.7 |  |
| money_level+rlm_ratio | close | 3k+ bets | 26-19 | 57.8 | 9.8 | 18.0 |  |
| consensus_gap+money_level | close | 3k+ bets | 74-66 | 52.9 | -5.0 | -10.3 |  |
| money_level+pin_move | close | 3k+ bets | 87-93 | 48.3 | -5.5 | -13.0 |  |
| money_level+pin_value | close | 3k+ bets | 61-74 | 45.2 | -5.4 | -15.9 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 12-18 | 40.0 | -0.3 | -8.1 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 90-119 | 43.1 | 0.5 | -9.2 |  |
| money_delta+money_moving | close | 3k+ bets | 92-118 | 43.8 | 0.9 | -0.3 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 38-54 | 41.3 | -0.2 | -10.5 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 52-68 | 43.3 | 0.8 | -8.8 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 49-67 | 42.2 | -0.3 | -11.4 |  |
| consensus_gap+money_delta | close | 3k+ bets | 17-28 | 37.8 | -2.7 | 15.3 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 26-41 | 38.8 | -2.8 | -18.8 |  |
| money_delta+sharp_gap | close | 3k+ bets | 90-115 | 43.9 | 1.1 | 0.1 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 50-59 | 45.9 | 2.4 | -2.7 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 21-33 | 38.9 | -2.4 | -14.0 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 13-22 | 37.1 | -12.2 | -29.2 |  |
| money_delta+money_level | close | 3k+ bets | 40-32 | 55.6 | 8.6 | 13.4 |  |
| money_level+pin_rlm | close | 3k+ bets | 16-14 | 53.3 | 6.8 | 14.2 |  |
| money_delta+pin_value | close | 3k+ bets | 27-26 | 50.9 | 2.8 | -3.7 |  |
| money_delta+pin_move | close | 3k+ bets | 49-60 | 45.0 | -1.1 | -9.5 |  |
| money_delta+pin_rlm | close | 3k+ bets | 31-38 | 44.9 | 1.9 | -6.4 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 40-39 | 50.6 | 7.1 | 5.7 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 46.4 | 87.7 |  |
| money_level+money_moving | close | <1k bets | 110-95 | 53.7 | 1.4 | -8.2 |  |
| money_level+sharp_gap | close | <1k bets | 113-96 | 54.1 | 1.4 | -8.3 |  |
| money_moving+sharp_gap | close | <1k bets | 154-171 | 47.4 | -0.5 | -10.5 |  |
| consensus_gap+money_level | close | <1k bets | 31-28 | 52.5 | -3.6 | -18.5 |  |
| consensus_gap+money_moving | close | <1k bets | 25-41 | 37.9 | -6.0 | -19.1 |  |
| consensus_gap+pin_move | close | <1k bets | 8-13 | 38.1 | -12.5 | -17.2 |  |
| consensus_gap+pin_value | close | <1k bets | 19-16 | 54.3 | 11.8 | 29.5 |  |
| consensus_gap+sharp_gap | close | <1k bets | 26-43 | 37.7 | -6.1 | -20.5 |  |
| money_level+pin_move | close | <1k bets | 48-44 | 52.2 | -0.7 | -6.6 |  |
| money_level+pin_value | close | <1k bets | 26-21 | 55.3 | 5.6 | 3.3 |  |
| money_moving+pin_move | close | <1k bets | 47-50 | 48.5 | 0.6 | -2.4 |  |
| money_moving+pin_value | close | <1k bets | 23-21 | 52.3 | 7.0 | 20.2 |  |
| pin_move+pin_value | close | <1k bets | 32-24 | 57.1 | 8.5 | 14.5 |  |
| pin_move+sharp_gap | close | <1k bets | 47-51 | 48.0 | -0.3 | -6.7 |  |
| pin_value+sharp_gap | close | <1k bets | 23-20 | 53.5 | 7.8 | 23.0 |  |
| follow_move+money_delta | close | <1k bets | 26-29 | 47.3 | 3.5 | -5.4 |  |
| follow_move+money_moving | close | <1k bets | 76-81 | 48.4 | -0.9 | -11.2 |  |
| follow_move+pin_move | close | <1k bets | 56-57 | 49.6 | -1.2 | -7.7 |  |
| follow_move+sharp_gap | close | <1k bets | 77-82 | 48.4 | -1.4 | -13.6 |  |
| money_delta+money_moving | close | <1k bets | 36-57 | 38.7 | -2.2 | -16.4 |  |
| money_delta+pin_move | close | <1k bets | 14-20 | 41.2 | -3.7 | -19.8 |  |
| money_delta+sharp_gap | close | <1k bets | 36-57 | 38.7 | -2.2 | -16.4 |  |
| follow_move+rlm_quiet | close | <1k bets | 32-47 | 40.5 | -1.6 | -16.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 36-38 | 48.6 | 5.2 | -3.3 |  |
| money_delta+rlm_quiet | close | <1k bets | 13-14 | 48.1 | 6.8 | -0.5 |  |
| money_delta+rlm_ratio | close | <1k bets | 21-22 | 48.8 | 6.2 | -1.2 |  |
| money_moving+rlm_quiet | close | <1k bets | 19-19 | 50.0 | 8.1 | 7.8 |  |
| money_moving+rlm_ratio | close | <1k bets | 36-38 | 48.6 | 5.2 | -3.3 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 15-16 | 48.4 | 7.4 | -0.6 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 18-20 | 47.4 | 4.9 | -3.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 36-38 | 48.6 | 5.2 | -3.3 |  |
| follow_move+money_level | close | <1k bets | 99-72 | 57.9 | 1.0 | -10.3 |  |
| consensus_gap+money_delta | close | <1k bets | 7-22 | 24.1 | -11.1 | -35.0 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -3.3 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 13-17 | 43.3 | 2.9 | -7.1 |  |
| money_moving+pin_rlm | close | <1k bets | 26-26 | 50.0 | 7.6 | 7.9 |  |
| pin_rlm+sharp_gap | close | <1k bets | 26-26 | 50.0 | 7.6 | 7.9 |  |
| money_delta+pin_value | close | <1k bets | 10-8 | 55.6 | 9.8 | 25.3 |  |
| consensus_gap+follow_move | close | <1k bets | 14-21 | 40.0 | -10.9 | -35.2 |  |
| follow_move+pin_rlm | close | <1k bets | 20-16 | 55.6 | 11.2 | 9.1 |  |
| follow_move+pin_value | close | <1k bets | 23-15 | 60.5 | 11.7 | 15.1 |  |
| pin_move+pin_rlm | close | <1k bets | 24-21 | 53.3 | 8.9 | 10.6 |  |
| pin_move+rlm_quiet | close | <1k bets | 13-14 | 48.1 | 2.2 | 2.3 |  |
| pin_move+rlm_ratio | close | <1k bets | 20-18 | 52.6 | 7.0 | 2.3 |  |
| pin_rlm+pin_value | close | <1k bets | 7-3 | 70.0 | 26.9 | 66.8 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 9-6 | 60.0 | 15.8 | 17.9 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 20-16 | 55.6 | 11.2 | 9.1 |  |
| pin_value+rlm_quiet | close | <1k bets | 6-4 | 60.0 | 10.9 | 15.0 |  |
| pin_value+rlm_ratio | close | <1k bets | 5-1 | 83.3 | 34.9 | 58.3 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -7.0 | -42.5 |  |
| money_delta+money_level | close | <1k bets | 15-20 | 42.9 | -0.5 | -14.3 |  |
| money_level+rlm_ratio | close | <1k bets | 17-17 | 50.0 | 5.0 | -2.7 |  |
| money_level+pin_rlm | close | <1k bets | 11-9 | 55.0 | 11.5 | 8.4 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-6 | 14.3 | -23.1 | -72.7 |  |
| consensus_gap+follow_move | close | pin $1-2k | 51-57 | 47.2 | -4.3 | -10.0 |  |
| consensus_gap+money_moving | close | pin $1-2k | 62-77 | 44.6 | -3.9 | -4.5 |  |
| consensus_gap+pin_move | close | pin $1-2k | 54-54 | 50.0 | -1.3 | 6.7 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 14-19 | 42.4 | 0.8 | 25.4 |  |
| consensus_gap+pin_value | close | pin $1-2k | 82-85 | 49.1 | 2.5 | -0.3 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 15-16 | 48.4 | 3.3 | 6.1 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 60-75 | 44.4 | -3.2 | -3.5 |  |
| follow_move+money_moving | close | pin $1-2k | 212-255 | 45.4 | -4.0 | -11.7 |  |
| follow_move+pin_move | close | pin $1-2k | 219-261 | 45.6 | -4.4 | -12.0 |  |
| follow_move+pin_rlm | close | pin $1-2k | 66-73 | 47.5 | 1.8 | -0.1 |  |
| follow_move+pin_value | close | pin $1-2k | 82-97 | 45.8 | -3.6 | -13.4 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 98-107 | 47.8 | 2.0 | -0.6 |  |
| follow_move+sharp_gap | close | pin $1-2k | 216-255 | 45.9 | -3.4 | -11.1 |  |
| money_moving+pin_move | close | pin $1-2k | 191-213 | 47.3 | -2.0 | -5.1 |  |
| money_moving+pin_rlm | close | pin $1-2k | 77-85 | 47.5 | 2.8 | 7.4 |  |
| money_moving+pin_value | close | pin $1-2k | 92-126 | 42.2 | -5.8 | -16.5 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 96-100 | 49.0 | 2.7 | 1.8 |  |
| money_moving+sharp_gap | close | pin $1-2k | 373-409 | 47.7 | -1.1 | -5.4 |  |
| pin_move+pin_rlm | close | pin $1-2k | 77-83 | 48.1 | 2.8 | 6.4 |  |
| pin_move+pin_value | close | pin $1-2k | 98-124 | 44.1 | -5.6 | -15.2 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 74-76 | 49.3 | 2.6 | 2.4 |  |
| pin_move+sharp_gap | close | pin $1-2k | 193-218 | 47.0 | -1.9 | -5.9 |  |
| pin_rlm+pin_value | close | pin $1-2k | 19-30 | 38.8 | -9.4 | -19.6 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 66-73 | 47.5 | 1.8 | -0.1 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 80-92 | 46.5 | 2.3 | 4.8 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 21-26 | 44.7 | -4.4 | -14.6 |  |
| pin_value+sharp_gap | close | pin $1-2k | 92-123 | 42.8 | -5.2 | -15.4 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 98-107 | 47.8 | 2.0 | -0.6 |  |
| follow_move+money_level | close | pin $1-2k | 227-222 | 50.6 | -3.2 | -11.3 |  |
| money_level+rlm_ratio | close | pin $1-2k | 49-42 | 53.8 | 5.9 | 4.8 |  |
| money_level+sharp_gap | close | pin $1-2k | 270-268 | 50.2 | -1.3 | -7.3 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 6-15 | 28.6 | -12.8 | -24.9 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 81-136 | 37.3 | -6.5 | -18.2 |  |
| money_level+money_moving | close | pin $1-2k | 274-271 | 50.3 | -1.4 | -7.6 |  |
| consensus_gap+money_level | close | pin $1-2k | 80-71 | 53.0 | -3.2 | -7.5 |  |
| money_level+pin_value | close | pin $1-2k | 106-110 | 49.1 | -0.7 | -8.3 |  |
| money_level+pin_move | close | pin $1-2k | 181-182 | 49.9 | -2.5 | -9.1 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 43-65 | 39.8 | -4.4 | -8.8 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 56-81 | 40.9 | -4.6 | -9.7 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 25-43 | 36.8 | -7.5 | -13.8 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 35-55 | 38.9 | -4.6 | -9.8 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 44-67 | 39.6 | -4.5 | -10.8 |  |
| money_level+pin_rlm | close | pin $1-2k | 35-30 | 53.8 | 7.4 | 5.7 |  |
| follow_move+money_delta | close | pin $1-2k | 77-84 | 47.8 | 1.2 | -2.8 |  |
| money_delta+money_moving | close | pin $1-2k | 106-117 | 47.5 | 2.7 | 2.4 |  |
| money_delta+pin_move | close | pin $1-2k | 75-80 | 48.4 | 1.0 | 1.0 |  |
| money_delta+pin_rlm | close | pin $1-2k | 48-54 | 47.1 | 3.0 | 5.5 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 56-56 | 50.0 | 4.2 | 3.7 |  |
| money_delta+sharp_gap | close | pin $1-2k | 106-115 | 48.0 | 3.1 | 3.3 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 46.4 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 53-48 | 52.5 | 4.3 | 2.1 |  |
| consensus_gap+money_delta | close | pin $1-2k | 21-26 | 44.7 | 2.6 | 9.2 |  |
| money_delta+pin_value | close | pin $1-2k | 48-49 | 49.5 | 1.2 | -2.2 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 25-42 | 37.3 | -7.0 | -17.6 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 15-35 | 30.0 | -18.8 | -41.4 |  |
| consensus_gap+follow_move | close | pin $2k+ | 47-39 | 54.7 | 1.1 | -7.7 |  |
| consensus_gap+money_delta | close | pin $2k+ | 13-29 | 31.0 | -5.7 | -37.4 |  |
| consensus_gap+money_level | close | pin $2k+ | 95-71 | 57.2 | -4.6 | -10.3 |  |
| consensus_gap+money_moving | close | pin $2k+ | 52-83 | 38.5 | -8.0 | -6.6 |  |
| consensus_gap+pin_move | close | pin $2k+ | 50-45 | 52.6 | 1.4 | 0.1 |  |
| consensus_gap+pin_value | close | pin $2k+ | 56-61 | 47.9 | 3.4 | 8.0 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 5-17 | 22.7 | -13.5 | -50.1 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 53-87 | 37.9 | -8.9 | -7.1 |  |
| follow_move+money_delta | close | pin $2k+ | 46-60 | 43.4 | 1.9 | -10.4 |  |
| follow_move+money_level | close | pin $2k+ | 184-129 | 58.8 | 0.4 | -6.0 |  |
| follow_move+money_moving | close | pin $2k+ | 159-169 | 48.5 | 1.0 | -7.4 |  |
| follow_move+pin_move | close | pin $2k+ | 203-202 | 50.1 | 0.5 | -4.9 |  |
| follow_move+pin_value | close | pin $2k+ | 48-46 | 51.1 | 2.9 | 6.8 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 57-85 | 40.1 | 1.6 | -12.1 |  |
| follow_move+sharp_gap | close | pin $2k+ | 156-170 | 47.9 | 0.5 | -7.9 |  |
| money_delta+money_level | close | pin $2k+ | 33-27 | 55.0 | 10.5 | 13.7 |  |
| money_delta+money_moving | close | pin $2k+ | 83-116 | 41.7 | 2.0 | -9.1 |  |
| money_delta+pin_move | close | pin $2k+ | 46-67 | 40.7 | -2.4 | -17.4 |  |
| money_delta+pin_value | close | pin $2k+ | 26-27 | 49.1 | 3.0 | -6.4 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 28-42 | 40.0 | 1.1 | -15.0 |  |
| money_delta+sharp_gap | close | pin $2k+ | 81-115 | 41.3 | 1.6 | -9.9 |  |
| money_level+money_moving | close | pin $2k+ | 214-207 | 50.8 | -1.7 | -7.3 |  |
| money_level+pin_move | close | pin $2k+ | 133-120 | 52.6 | -3.0 | -8.6 |  |
| money_level+pin_value | close | pin $2k+ | 72-81 | 47.1 | -2.8 | -12.8 |  |
| money_level+rlm_ratio | close | pin $2k+ | 19-21 | 47.5 | 1.6 | -2.4 |  |
| money_level+sharp_gap | close | pin $2k+ | 210-210 | 50.0 | -2.5 | -8.2 |  |
| money_moving+pin_move | close | pin $2k+ | 135-158 | 46.1 | -0.8 | -8.7 |  |
| money_moving+pin_value | close | pin $2k+ | 78-95 | 45.1 | -1.7 | -2.3 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 57-83 | 40.7 | 2.2 | -10.8 |  |
| money_moving+sharp_gap | close | pin $2k+ | 319-374 | 46.0 | -0.6 | -5.4 |  |
| pin_move+pin_value | close | pin $2k+ | 69-69 | 50.0 | 1.1 | -3.0 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 43-60 | 41.7 | 1.9 | -7.5 |  |
| pin_move+sharp_gap | close | pin $2k+ | 134-161 | 45.4 | -1.5 | -9.4 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 8-9 | 47.1 | 1.0 | -7.8 |  |
| pin_value+sharp_gap | close | pin $2k+ | 78-99 | 44.1 | -2.9 | -4.5 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 57-85 | 40.1 | 1.6 | -12.1 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 10-26 | 27.8 | -7.4 | -15.6 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 8-17 | 32.0 | -0.4 | -29.4 |  |
| follow_move+pin_rlm | close | pin $2k+ | 43-67 | 39.1 | 1.5 | -12.0 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 98-116 | 45.8 | 7.1 | 4.1 |  |
| money_moving+pin_rlm | close | pin $2k+ | 58-95 | 37.9 | 1.1 | -6.3 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 46-64 | 41.8 | 5.2 | -7.4 |  |
| pin_move+pin_rlm | close | pin $2k+ | 48-69 | 41.0 | 2.3 | -6.9 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 65-82 | 44.2 | 3.7 | -3.3 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 25-48 | 34.2 | 0.3 | -19.3 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 43-67 | 39.1 | 1.5 | -12.0 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 58-97 | 37.4 | 0.5 | -7.5 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 32-55 | 36.8 | 2.7 | -15.2 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 45-65 | 40.9 | 4.1 | -9.7 |  |
| money_delta+pin_rlm | close | pin $2k+ | 32-53 | 37.6 | 0.4 | -12.3 |  |
| money_level+pin_rlm | close | pin $2k+ | 17-16 | 51.5 | 7.0 | 8.5 |  |
| pin_rlm+pin_value | close | pin $2k+ | 11-17 | 39.3 | -3.1 | 11.1 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 27-36 | 42.9 | 4.5 | -11.1 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 10-11 | 47.6 | 5.2 | 38.9 |  |
| follow_move+money_delta | close | pin limit <$1k | 37-49 | 43.0 | -6.2 | -17.4 |  |
| money_level+money_moving | close | pin limit <$1k | 100-103 | 49.3 | -0.5 | -5.7 |  |
| money_level+sharp_gap | close | pin limit <$1k | 95-97 | 49.5 | -0.3 | -5.2 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 142-157 | 47.5 | -1.9 | -6.0 |  |
| consensus_gap+money_level | close | pin limit <$1k | 34-31 | 52.3 | 1.6 | -3.0 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 19-14 | 57.6 | 8.9 | 22.0 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 44-43 | 50.6 | 1.1 | 0.3 |  |
| follow_move+money_moving | close | pin limit <$1k | 89-101 | 46.8 | -2.6 | -10.1 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 93-100 | 48.2 | -1.2 | -7.5 |  |
| money_level+pin_move | close | pin limit <$1k | 74-61 | 54.8 | 4.9 | 4.6 |  |
| money_level+pin_value | close | pin limit <$1k | 67-45 | 59.8 | 9.7 | 13.3 |  |
| pin_move+pin_value | close | pin limit <$1k | 57-37 | 60.6 | 10.8 | 20.0 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 23-15 | 60.5 | 11.1 | 12.2 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 28-27 | 50.9 | 2.1 | 4.5 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 30-29 | 50.8 | 1.9 | 3.8 |  |
| follow_move+money_level | close | pin limit <$1k | 80-72 | 52.6 | 2.4 | -0.2 |  |
| follow_move+pin_move | close | pin limit <$1k | 84-82 | 50.6 | 1.1 | -3.0 |  |
| follow_move+pin_value | close | pin limit <$1k | 50-31 | 61.7 | 12.0 | 17.2 |  |
| money_moving+pin_move | close | pin limit <$1k | 80-80 | 50.0 | 0.6 | -1.6 |  |
| money_moving+pin_value | close | pin limit <$1k | 54-42 | 56.2 | 6.7 | 11.4 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 81-80 | 50.3 | 0.9 | -1.0 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 55-47 | 53.9 | 4.3 | 6.7 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 51-55 | 48.1 | -1.3 | -7.6 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 29-37 | 43.9 | -5.2 | -15.8 |  |
| money_delta+money_moving | close | pin limit <$1k | 53-59 | 47.3 | -1.9 | -5.4 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 10-8 | 55.6 | 8.2 | 30.0 |  |
| money_delta+money_level | close | pin limit <$1k | 26-25 | 51.0 | 1.3 | -2.3 |  |
| money_delta+pin_value | close | pin limit <$1k | 20-10 | 66.7 | 17.5 | 41.4 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 52-57 | 47.7 | -1.4 | -4.6 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 34-40 | 45.9 | -3.0 | -5.9 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 7-4 | 63.6 | 17.4 | 61.2 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 28-24 | 53.8 | 5.4 | 11.8 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 47-39 | 54.7 | 5.9 | 15.1 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 49-41 | 54.4 | 5.4 | 9.2 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 21-7 | 75.0 | 25.9 | 58.8 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 50-41 | 54.9 | 6.1 | 15.1 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 7-4 | 63.6 | 15.8 | 21.7 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 16-10 | 61.5 | 11.8 | 17.5 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 12-22 | 35.3 | -13.3 | -32.2 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 26-31 | 45.6 | -3.5 | -12.2 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 39-33 | 54.2 | 5.0 | 4.2 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 54-51 | 51.4 | 2.3 | -0.8 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 30-32 | 48.4 | -0.6 | -7.0 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 23-36 | 39.0 | -10.1 | -25.1 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 49-48 | 50.5 | 1.5 | -2.5 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 39-33 | 54.2 | 5.0 | 4.2 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 15-16 | 48.4 | -0.1 | -6.9 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 39-33 | 54.2 | 5.0 | 4.2 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 24-29 | 45.3 | -3.6 | -13.1 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 54-51 | 51.4 | 2.3 | -0.8 |  |
| money_level+pin_rlm | close | pin limit <$1k | 24-16 | 60.0 | 10.4 | 15.1 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 26-19 | 57.8 | 8.6 | 12.1 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 18-8 | 69.2 | 19.5 | 32.5 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 7-6 | 53.8 | 5.5 | 2.9 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 50.5 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.8 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -52.0 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 53-63 | 45.7 | 8.7 | 11.2 | 0.65 |
| rlm_quiet | early | pin $1-2k | 3-7 | 30.0 | -1.5 | 7.2 | -0.12 |
| rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -29.1 | -100.0 | 1.3 |
| rlm_quiet | early | pin limit <$1k | 6-9 | 40.0 | -5.5 | -19.3 | 0.28 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.5 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 14-21 | 40.0 | -9.1 | -26.3 | 0.19 |
| pin_move | early | pin $1-2k | 2-9 | 18.2 | -30.8 | -68.6 | 0.27 |
| pin_move | early | pin limit <$1k | 12-16 | 42.9 | -7.0 | -20.2 | 0.44 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 12-11 | 52.2 | 13.3 | 22.6 | 0.98 |
| money_delta | early | pin $1-2k | 0-3 | 0.0 | -37.2 | -100.0 | 2.17 |
| money_delta | early | pin limit <$1k | 5-0 | 100.0 | 50.9 | 88.6 | 0.0 |
| pin_rlm | early | <1k bets | 1-4 | 20.0 | -17.4 | -61.5 | -0.3 |
| pin_rlm | early | pin $1-2k | 0-3 | 0.0 | -43.0 | -100.0 | -0.67 |
| pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 20.9 | -3.7 | 0.25 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.7 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -52.0 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 619-563 | 52.4 | 1.5 | -5.9 | 0.18 |
| follow_move | early | pin $1-2k | 41-32 | 56.2 | 6.4 | 4.5 | -0.34 |
| follow_move | early | pin $2k+ | 0-2 | 0.0 | -41.3 | -100.0 | 0.65 |
| follow_move | early | pin limit <$1k | 60-60 | 50.0 | 0.1 | -5.9 | -0.08 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 22.5 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.6 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 33-30 | 52.4 | 12.9 | 18.9 | 0.65 |
| rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.9 | 29.7 | -1.02 |
| rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -41.3 | -100.0 | 0.65 |
| rlm_ratio | early | pin limit <$1k | 8-2 | 80.0 | 36.4 | 61.1 | 0.33 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 1.7 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 44.4 | 59.7 | 0.33 |
| money_level | early | <1k bets | 217-153 | 58.6 | 0.0 | -7.4 | -0.26 |
| money_level | early | pin $1-2k | 24-13 | 64.9 | 1.7 | -2.9 | -0.05 |
| money_level | early | pin $2k+ | 1-1 | 50.0 | -12.3 | -47.2 | -0.7 |
| money_level | early | pin limit <$1k | 32-32 | 50.0 | -2.0 | -6.9 | 0.24 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.0 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.7 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 175-165 | 51.5 | 2.3 | -1.3 | 0.32 |
| sharp_gap | early | pin $1-2k | 18-17 | 51.4 | -3.8 | -6.9 | -0.3 |
| sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -41.3 | -100.0 | 0.65 |
| sharp_gap | early | pin limit <$1k | 36-23 | 61.0 | 12.4 | 24.5 | 0.16 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.6 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 52.0 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 128-114 | 52.9 | 2.1 | -5.2 | 0.24 |
| money_moving | early | pin $1-2k | 8-13 | 38.1 | -18.7 | -47.8 | 0.36 |
| money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.3 | -8.4 | 0.65 |
| money_moving | early | pin limit <$1k | 33-11 | 75.0 | 25.3 | 53.4 | 0.38 |
| pin_value | early | 1-3k bets | 13-10 | 56.5 | 8.5 | 6.3 | -0.04 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.6 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 58-58 | 50.0 | 1.0 | -5.4 | 0.11 |
| pin_value | early | pin $1-2k | 19-30 | 38.8 | -8.5 | -27.1 | 0.19 |
| pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.6 | 83.3 | 0.0 |
| pin_value | early | pin limit <$1k | 53-39 | 57.6 | 8.0 | 9.1 | 0.05 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -50.5 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -27.6 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -10.9 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.3 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 296-349 | 45.9 | -3.9 | -12.9 | 0.41 |
| consensus_gap | early | pin $1-2k | 22-25 | 46.8 | -0.5 | -11.9 | 0.29 |
| consensus_gap | early | pin $2k+ | 1-1 | 50.0 | 12.3 | -8.4 | 0.65 |
| consensus_gap | early | pin limit <$1k | 26-38 | 40.6 | -9.4 | -17.9 | 0.24 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -53.6 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -2.0 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.9 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 5.5 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.2 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 7-4 | 63.6 | 14.4 | 19.4 | -0.09 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 18.9 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.8 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.5 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -0.4 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 6-5 | 54.5 | 8.7 | 1.3 | 0.27 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -1.5 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-7 | 50.0 | 3.1 | -6.4 | -0.29 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.8 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.7 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -19.5 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -3.1 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 3.8 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.5 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 22.5 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.1 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 22.5 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.5 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.5 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.4 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.5 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 53.6 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 11.2 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 17.7 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 15.6 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 15.6 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -29.1 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 53.6 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 53.6 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.6 | 83.3 | 1.0 |
| follow_move+rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -52.0 | -100.0 | -0.5 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.6 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.6 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 52.0 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.6 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.6 | 83.3 | 1.0 |
| rlm_quiet+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.6 | -100.0 | -1.0 |
| rlm_quiet+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.6 | -100.0 | -1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.6 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 39.8 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 50.5 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 42-54 | 43.8 | -9.8 | -22.8 | 0.92 |
| consensus_gap+money_level | early | <1k bets | 53-40 | 57.0 | -6.4 | -11.6 | -0.12 |
| consensus_gap+sharp_gap | early | <1k bets | 38-55 | 40.9 | -9.6 | -20.1 | 0.53 |
| follow_move+money_level | early | <1k bets | 104-53 | 66.2 | 6.4 | -2.4 | 0.06 |
| follow_move+sharp_gap | early | <1k bets | 88-55 | 61.5 | 11.9 | 11.4 | 0.61 |
| money_level+sharp_gap | early | <1k bets | 118-85 | 58.1 | 2.0 | -4.8 | 0.02 |
| follow_move+money_moving | early | <1k bets | 62-43 | 59.0 | 7.1 | 5.6 | 0.53 |
| money_level+money_moving | early | <1k bets | 73-52 | 58.4 | 0.9 | -6.1 | -0.05 |
| money_moving+sharp_gap | early | <1k bets | 74-70 | 51.4 | 2.9 | -3.2 | 0.45 |
| consensus_gap+money_moving | early | <1k bets | 21-25 | 45.7 | -5.5 | -26.1 | 0.61 |
| follow_move+pin_value | early | <1k bets | 18-16 | 52.9 | 3.3 | -0.3 | -0.1 |
| follow_move+rlm_quiet | early | <1k bets | 53-63 | 45.7 | 8.7 | 11.2 | 0.65 |
| money_moving+rlm_quiet | early | <1k bets | 18-19 | 48.6 | 10.2 | 18.8 | 0.91 |
| rlm_quiet+sharp_gap | early | <1k bets | 26-24 | 52.0 | 13.6 | 20.4 | 0.5 |
| follow_move+rlm_ratio | early | <1k bets | 33-30 | 52.4 | 12.9 | 18.9 | 0.65 |
| rlm_quiet+rlm_ratio | early | <1k bets | 23-18 | 56.1 | 18.1 | 32.9 | 0.38 |
| rlm_ratio+sharp_gap | early | <1k bets | 33-30 | 52.4 | 12.9 | 18.9 | 0.65 |
| pin_move+pin_value | early | <1k bets | 5-11 | 31.2 | -18.2 | -39.8 | 0.44 |
| follow_move+pin_move | early | <1k bets | 9-10 | 47.4 | -1.7 | -12.6 | 0.49 |
| consensus_gap+pin_value | early | <1k bets | 23-26 | 46.9 | -0.5 | -11.8 | 0.25 |
| pin_value+rlm_quiet | early | <1k bets | 0-3 | 0.0 | -44.1 | -100.0 | -0.6 |
| money_delta+money_moving | early | <1k bets | 11-11 | 50.0 | 11.6 | 19.5 | 1.02 |
| money_delta+sharp_gap | early | <1k bets | 10-9 | 52.6 | 14.9 | 28.3 | 1.18 |
| consensus_gap+pin_move | early | <1k bets | 2-6 | 25.0 | -21.9 | -51.7 | 0.29 |
| money_level+pin_move | early | <1k bets | 4-6 | 40.0 | -9.9 | -30.2 | 0.14 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -29.1 | -100.0 | -4.8 |
| consensus_gap+rlm_quiet | early | <1k bets | 4-6 | 40.0 | 2.8 | -12.2 | 1.03 |
| consensus_gap+rlm_ratio | early | <1k bets | 5-3 | 62.5 | 20.7 | 25.0 | 0.65 |
| follow_move+pin_rlm | early | <1k bets | 1-3 | 25.0 | -14.5 | -51.8 | -0.7 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -29.1 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | <1k bets | 0-1 | 0.0 | -29.1 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-3 | 25.0 | -14.5 | -51.8 | -0.7 |
| pin_rlm+sharp_gap | early | <1k bets | 1-4 | 20.0 | -17.4 | -61.5 | -0.3 |
| pin_value+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 24.0 | 27.3 | -0.93 |
| pin_value+sharp_gap | early | <1k bets | 6-8 | 42.9 | -7.2 | -18.2 | 0.42 |
| money_level+pin_value | early | <1k bets | 7-7 | 50.0 | -1.7 | -4.5 | 0.84 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -51.5 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -49.5 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 4-4 | 50.0 | -3.3 | -4.0 | 1.21 |
| money_level+rlm_ratio | early | <1k bets | 8-12 | 40.0 | -1.6 | -17.1 | 1.32 |
| money_moving+rlm_ratio | early | <1k bets | 16-12 | 57.1 | 15.6 | 34.9 | 1.24 |
| consensus_gap+money_delta | early | <1k bets | 2-0 | 100.0 | 50.0 | 90.9 | 0.5 |
| money_delta+money_level | early | <1k bets | 4-4 | 50.0 | 8.0 | 4.6 | 1.44 |
| pin_move+sharp_gap | early | <1k bets | 2-4 | 33.3 | -13.4 | -47.8 | 0.47 |
| money_level+pin_rlm | early | <1k bets | 1-2 | 33.3 | -9.7 | -35.8 | 0.67 |
| pin_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 20.9 | -3.7 | 0.25 |
| pin_move+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 20.9 | -3.7 | 0.25 |
| follow_move+money_delta | early | <1k bets | 6-5 | 54.5 | 16.2 | 52.8 | 1.28 |
| money_delta+rlm_quiet | early | <1k bets | 3-3 | 50.0 | 17.5 | 72.5 | 0.38 |
| money_delta+rlm_ratio | early | <1k bets | 5-3 | 62.5 | 25.8 | 86.2 | 2.04 |
| money_delta+pin_value | early | <1k bets | 2-0 | 100.0 | 50.5 | 90.9 | 0.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -29.1 | -100.0 | 1.3 |
| money_moving+pin_move | early | <1k bets | 1-1 | 50.0 | 0.5 | -2.4 | 1.0 |
| consensus_gap+money_level | early | pin $1-2k | 7-5 | 58.3 | -6.5 | -9.8 | 0.07 |
| consensus_gap+money_moving | early | pin $1-2k | 1-3 | 25.0 | -39.8 | -54.2 | 0.95 |
| consensus_gap+pin_value | early | pin $1-2k | 8-11 | 42.1 | -0.9 | -22.3 | 0.14 |
| follow_move+rlm_quiet | early | pin $1-2k | 3-7 | 30.0 | -1.5 | 7.2 | -0.12 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.9 | 29.7 | -1.02 |
| follow_move+sharp_gap | early | pin $1-2k | 9-6 | 60.0 | 3.0 | 19.2 | -0.62 |
| money_level+money_moving | early | pin $1-2k | 8-8 | 50.0 | -12.6 | -31.4 | 0.26 |
| money_level+pin_value | early | pin $1-2k | 2-4 | 33.3 | -18.4 | -37.6 | 0.78 |
| money_moving+pin_value | early | pin $1-2k | 1-4 | 20.0 | -34.8 | -63.3 | 0.94 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -10.2 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -10.2 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -10.9 | 29.7 | -1.02 |
| money_delta+money_level | early | pin $1-2k | 0-2 | 0.0 | -41.3 | -100.0 | 1.25 |
| money_delta+money_moving | early | pin $1-2k | 0-3 | 0.0 | -37.2 | -100.0 | 2.17 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -53.6 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-3 | 0.0 | -37.2 | -100.0 | 2.17 |
| money_level+sharp_gap | early | pin $1-2k | 15-9 | 62.5 | -0.6 | -4.8 | -0.23 |
| money_moving+sharp_gap | early | pin $1-2k | 4-10 | 28.6 | -27.4 | -61.0 | 0.36 |
| pin_value+sharp_gap | early | pin $1-2k | 1-4 | 20.0 | -30.7 | -61.8 | -0.22 |
| consensus_gap+follow_move | early | pin $1-2k | 6-7 | 46.2 | -2.2 | -11.3 | 0.4 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 1-3 | 25.0 | -4.1 | -35.0 | -0.65 |
| follow_move+pin_value | early | pin $1-2k | 6-8 | 42.9 | -5.1 | -20.8 | -0.24 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -29.1 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 12-6 | 66.7 | 3.5 | -0.4 | -0.03 |
| money_level+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -12.3 | -1.0 | 0.75 |
| follow_move+money_moving | early | pin $1-2k | 4-3 | 57.1 | -7.2 | -23.6 | -0.13 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -29.1 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -29.1 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 4-5 | 44.4 | -12.5 | -31.7 | -0.69 |
| follow_move+pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -29.1 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | pin $1-2k | 0-1 | 0.0 | -29.1 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-3 | 0.0 | -43.0 | -100.0 | -0.67 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -29.1 | -100.0 | -4.8 |
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -29.1 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -29.1 | -100.0 | 1.3 |
| pin_move+pin_value | early | pin $1-2k | 0-4 | 0.0 | -48.2 | -100.0 | 0.5 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -70.9 | -100.0 | 1.5 |
| follow_move+pin_move | early | pin $1-2k | 1-2 | 33.3 | -15.5 | -35.2 | -0.33 |
| money_level+pin_move | early | pin $1-2k | 1-0 | 100.0 | 53.6 | 94.3 | -1.0 |
| consensus_gap+money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.3 | -8.4 | 0.65 |
| consensus_gap+pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.6 | 83.3 | 0.0 |
| follow_move+money_level | early | pin $2k+ | 0-1 | 0.0 | -53.6 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -41.3 | -100.0 | 0.65 |
| follow_move+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -41.3 | -100.0 | 0.65 |
| money_level+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -53.6 | -100.0 | 0.0 |
| money_level+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -53.6 | -100.0 | 0.0 |
| money_moving+pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.6 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -41.3 | -100.0 | 0.65 |
| consensus_gap+follow_move | early | pin $2k+ | 0-1 | 0.0 | -29.1 | -100.0 | 1.3 |
| consensus_gap+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -29.1 | -100.0 | 1.3 |
| consensus_gap+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -29.1 | -100.0 | 1.3 |
| consensus_gap+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -29.1 | -100.0 | 1.3 |
| follow_move+money_moving | early | pin $2k+ | 0-1 | 0.0 | -29.1 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -29.1 | -100.0 | 1.3 |
| money_moving+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -29.1 | -100.0 | 1.3 |
| money_moving+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -29.1 | -100.0 | 1.3 |
| money_moving+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -29.1 | -100.0 | 1.3 |
| rlm_quiet+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -29.1 | -100.0 | 1.3 |
| rlm_quiet+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -29.1 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin limit <$1k | 6-9 | 40.0 | -5.5 | -19.3 | 0.28 |
| money_level+money_moving | early | pin limit <$1k | 18-7 | 72.0 | 20.5 | 34.3 | 0.42 |
| money_level+sharp_gap | early | pin limit <$1k | 26-20 | 56.5 | 6.6 | 4.5 | 0.22 |
| money_moving+sharp_gap | early | pin limit <$1k | 24-6 | 80.0 | 31.5 | 68.6 | 0.27 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -50.5 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 13-8 | 61.9 | 11.9 | 17.4 | 0.33 |
| money_moving+pin_value | early | pin limit <$1k | 11-4 | 73.3 | 23.7 | 39.0 | 0.27 |
| pin_value+sharp_gap | early | pin limit <$1k | 14-8 | 63.6 | 13.8 | 20.6 | 0.14 |
| consensus_gap+follow_move | early | pin limit <$1k | 7-10 | 41.2 | -9.9 | -23.2 | 0.41 |
| consensus_gap+money_level | early | pin limit <$1k | 6-7 | 46.2 | -8.1 | -19.0 | 0.31 |
| consensus_gap+pin_value | early | pin limit <$1k | 21-20 | 51.2 | 2.1 | -3.4 | 0.33 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 7-4 | 63.6 | 18.1 | 56.6 | 0.91 |
| follow_move+money_level | early | pin limit <$1k | 14-14 | 50.0 | -1.7 | -6.7 | -0.03 |
| follow_move+pin_value | early | pin limit <$1k | 19-15 | 55.9 | 6.7 | 5.6 | -0.12 |
| follow_move+sharp_gap | early | pin limit <$1k | 16-10 | 61.5 | 13.6 | 17.7 | -0.02 |
| follow_move+rlm_ratio | early | pin limit <$1k | 8-2 | 80.0 | 36.4 | 61.1 | 0.33 |
| money_level+rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.0 | 68.3 | 0.44 |
| pin_value+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.3 | 43.2 | -0.25 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 8-2 | 80.0 | 36.4 | 61.1 | 0.33 |
| consensus_gap+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 51.2 | 87.1 | 0.33 |
| consensus_gap+money_moving | early | pin limit <$1k | 10-3 | 76.9 | 29.2 | 76.9 | 0.65 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 2.0 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 51.2 | 87.1 | 0.33 |
| follow_move+money_moving | early | pin limit <$1k | 13-5 | 72.2 | 23.0 | 38.2 | 0.39 |
| money_delta+money_moving | early | pin limit <$1k | 4-0 | 100.0 | 51.0 | 88.0 | 0.0 |
| money_delta+pin_value | early | pin limit <$1k | 4-0 | 100.0 | 51.0 | 88.0 | 0.0 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 53.6 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 4-2 | 66.7 | 17.5 | 26.0 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 30.1 | 54.4 | -0.2 |
| money_delta+sharp_gap | early | pin limit <$1k | 3-0 | 100.0 | 50.2 | 89.6 | 0.0 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 10.2 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | 5.4 | 13.7 | -0.05 |
| pin_move+pin_value | early | pin limit <$1k | 5-8 | 38.5 | -11.1 | -25.9 | 0.54 |
| follow_move+pin_move | early | pin limit <$1k | 8-9 | 47.1 | -2.1 | -13.7 | 0.67 |
| consensus_gap+pin_move | early | pin limit <$1k | 2-4 | 33.3 | -19.6 | -35.7 | 0.43 |
| money_level+pin_move | early | pin limit <$1k | 3-6 | 33.3 | -16.9 | -44.0 | 0.27 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -49.5 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -49.5 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-4 | 33.3 | -13.4 | -47.8 | 0.47 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 20.9 | -3.7 | 0.25 |
| money_level+pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 20.9 | -3.7 | 0.25 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 20.9 | -3.7 | 0.25 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 20.9 | -3.7 | 0.25 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 20.9 | -3.7 | 0.25 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 20.9 | -3.7 | 0.25 |
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
| rlm_quiet | close | 1-3k bets | 73-112 | 39.5 | -4.2 | -8.3 |  |
| rlm_quiet | close | 3k+ bets | 46-59 | 43.8 | 0.4 | -10.3 |  |
| rlm_quiet | close | <1k bets | 10-19 | 34.5 | -9.1 | -33.2 |  |
| rlm_quiet | close | pin $1-2k | 35-55 | 38.9 | -6.1 | -19.4 |  |
| rlm_quiet | close | pin $2k+ | 45-53 | 45.9 | 4.4 | 10.9 |  |
| rlm_quiet | close | pin limit <$1k | 15-19 | 44.1 | -3.7 | -14.9 |  |
| pin_move | close | 1-3k bets | 132-139 | 48.7 | -0.6 | -2.4 |  |
| pin_move | close | 3k+ bets | 63-78 | 44.7 | -5.7 | -15.4 |  |
| pin_move | close | <1k bets | 20-19 | 51.3 | 1.7 | -3.3 |  |
| pin_move | close | pin $1-2k | 87-108 | 44.6 | -4.8 | -12.5 |  |
| pin_move | close | pin $2k+ | 91-98 | 48.1 | -1.8 | -4.7 |  |
| pin_move | close | pin limit <$1k | 37-33 | 52.9 | 3.4 | 1.2 |  |
| money_delta | close | 1-3k bets | 62-84 | 42.5 | -1.8 | -11.7 |  |
| money_delta | close | 3k+ bets | 43-45 | 48.9 | 3.8 | -1.9 |  |
| money_delta | close | <1k bets | 14-14 | 50.0 | 5.0 | 11.4 |  |
| money_delta | close | pin $1-2k | 44-39 | 53.0 | 6.3 | 8.2 |  |
| money_delta | close | pin $2k+ | 32-38 | 45.7 | 3.1 | -5.2 |  |
| money_delta | close | pin limit <$1k | 13-19 | 40.6 | -6.8 | -22.0 |  |
| pin_rlm | close | 1-3k bets | 27-41 | 39.7 | -2.3 | -14.1 |  |
| pin_rlm | close | 3k+ bets | 16-23 | 41.0 | -2.7 | -17.5 |  |
| pin_rlm | close | <1k bets | 5-5 | 50.0 | 2.3 | -4.9 |  |
| pin_rlm | close | pin $1-2k | 19-26 | 42.2 | -2.2 | -12.4 |  |
| pin_rlm | close | pin $2k+ | 20-31 | 39.2 | -0.8 | -14.9 |  |
| pin_rlm | close | pin limit <$1k | 9-12 | 42.9 | -4.9 | -17.7 |  |
| follow_move | close | 1-3k bets | 207-238 | 46.5 | -2.7 | -8.5 |  |
| follow_move | close | 3k+ bets | 109-105 | 50.9 | 1.8 | -5.6 |  |
| follow_move | close | <1k bets | 44-46 | 48.9 | -0.9 | -13.1 |  |
| follow_move | close | pin $1-2k | 103-131 | 44.0 | -5.2 | -16.6 |  |
| follow_move | close | pin $2k+ | 113-112 | 50.2 | 1.0 | -0.3 |  |
| follow_move | close | pin limit <$1k | 44-41 | 51.8 | 2.1 | -1.8 |  |
| rlm_ratio | close | 1-3k bets | 48-77 | 38.4 | -4.4 | -16.1 |  |
| rlm_ratio | close | 3k+ bets | 25-38 | 39.7 | -4.1 | -20.1 |  |
| rlm_ratio | close | <1k bets | 10-12 | 45.5 | 0.8 | -12.8 |  |
| rlm_ratio | close | pin $1-2k | 28-34 | 45.2 | 0.4 | -7.7 |  |
| rlm_ratio | close | pin $2k+ | 19-32 | 37.3 | -2.5 | -20.0 |  |
| rlm_ratio | close | pin limit <$1k | 10-17 | 37.0 | -10.9 | -28.9 |  |
| money_level | close | 1-3k bets | 268-209 | 56.2 | 1.5 | -4.3 |  |
| money_level | close | 3k+ bets | 127-119 | 51.6 | -2.1 | -9.8 |  |
| money_level | close | <1k bets | 60-31 | 65.9 | 11.4 | 9.2 |  |
| money_level | close | pin $1-2k | 129-123 | 51.2 | -1.9 | -10.1 |  |
| money_level | close | pin $2k+ | 125-117 | 51.7 | -3.7 | -13.3 |  |
| money_level | close | pin limit <$1k | 54-38 | 58.7 | 7.2 | 10.9 |  |
| sharp_gap | close | 1-3k bets | 208-240 | 46.4 | -2.0 | -10.4 |  |
| sharp_gap | close | 3k+ bets | 104-130 | 44.4 | -3.6 | -13.6 |  |
| sharp_gap | close | <1k bets | 46-39 | 54.1 | 4.9 | -0.8 |  |
| sharp_gap | close | pin $1-2k | 113-122 | 48.1 | -0.5 | -7.3 |  |
| sharp_gap | close | pin $2k+ | 101-130 | 43.7 | -3.8 | -13.3 |  |
| sharp_gap | close | pin limit <$1k | 39-47 | 45.3 | -4.2 | -13.4 |  |
| money_moving | close | 1-3k bets | 218-235 | 48.1 | -0.6 | -7.5 |  |
| money_moving | close | 3k+ bets | 108-127 | 46.0 | -2.6 | -12.3 |  |
| money_moving | close | <1k bets | 46-37 | 55.4 | 6.1 | 1.5 |  |
| money_moving | close | pin $1-2k | 118-118 | 50.0 | 0.9 | -4.8 |  |
| money_moving | close | pin $2k+ | 106-126 | 45.7 | -2.0 | -10.2 |  |
| money_moving | close | pin limit <$1k | 43-48 | 47.3 | -2.3 | -9.8 |  |
| pin_value | close | 1-3k bets | 111-93 | 54.4 | 4.7 | 8.3 |  |
| pin_value | close | 3k+ bets | 34-55 | 38.2 | -12.5 | -27.6 |  |
| pin_value | close | <1k bets | 18-14 | 56.2 | 9.1 | 17.6 |  |
| pin_value | close | pin $1-2k | 74-77 | 49.0 | -0.3 | -3.7 |  |
| pin_value | close | pin $2k+ | 53-57 | 48.2 | -1.5 | 0.0 |  |
| pin_value | close | pin limit <$1k | 38-29 | 56.7 | 6.2 | 7.8 |  |
| consensus_gap | close | 1-3k bets | 87-72 | 54.7 | 2.5 | 0.1 |  |
| consensus_gap | close | 3k+ bets | 42-39 | 51.9 | -3.5 | -11.2 |  |
| consensus_gap | close | <1k bets | 18-8 | 69.2 | 18.7 | 29.9 |  |
| consensus_gap | close | pin $1-2k | 32-29 | 52.5 | 0.7 | 5.1 |  |
| consensus_gap | close | pin $2k+ | 63-36 | 63.6 | 7.4 | 14.5 |  |
| consensus_gap | close | pin limit <$1k | 10-13 | 43.5 | -5.4 | -17.1 |  |
| follow_move+pin_move | close | 1-3k bets | 85-113 | 42.9 | -5.9 | -15.7 |  |
| money_delta+money_moving | close | 1-3k bets | 50-64 | 43.9 | 0.9 | -7.1 |  |
| money_delta+sharp_gap | close | 1-3k bets | 50-63 | 44.2 | 1.4 | -6.3 |  |
| money_moving+sharp_gap | close | 1-3k bets | 202-226 | 47.2 | -1.3 | -8.5 |  |
| consensus_gap+money_level | close | 1-3k bets | 54-39 | 58.1 | 0.4 | -8.1 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 73-112 | 39.5 | -4.2 | -8.3 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 32-53 | 37.6 | -6.8 | -16.7 |  |
| consensus_gap+follow_move | close | 1-3k bets | 22-26 | 45.8 | -4.2 | -14.8 |  |
| follow_move+money_level | close | 1-3k bets | 101-88 | 53.4 | -1.1 | -7.5 |  |
| money_level+money_moving | close | 1-3k bets | 151-134 | 53.0 | 0.7 | -4.7 |  |
| money_level+sharp_gap | close | 1-3k bets | 143-134 | 51.6 | -0.5 | -6.7 |  |
| consensus_gap+money_moving | close | 1-3k bets | 27-36 | 42.9 | -7.2 | -17.6 |  |
| consensus_gap+pin_move | close | 1-3k bets | 23-14 | 62.2 | 13.1 | 36.6 |  |
| consensus_gap+pin_value | close | 1-3k bets | 29-28 | 50.9 | 2.0 | -3.6 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 27-38 | 41.5 | -8.2 | -20.3 |  |
| follow_move+money_moving | close | 1-3k bets | 109-132 | 45.2 | -3.1 | -10.8 |  |
| follow_move+pin_value | close | 1-3k bets | 35-28 | 55.6 | 5.3 | 20.5 |  |
| follow_move+sharp_gap | close | 1-3k bets | 109-135 | 44.7 | -3.6 | -12.2 |  |
| money_level+pin_move | close | 1-3k bets | 60-50 | 54.5 | 1.5 | -2.2 |  |
| money_level+pin_value | close | 1-3k bets | 47-41 | 53.4 | 3.3 | 0.1 |  |
| money_moving+pin_move | close | 1-3k bets | 65-64 | 50.4 | 2.2 | -1.2 |  |
| money_moving+pin_value | close | 1-3k bets | 41-42 | 49.4 | -0.0 | -6.8 |  |
| pin_move+pin_value | close | 1-3k bets | 40-39 | 50.6 | -0.7 | -4.2 |  |
| pin_move+sharp_gap | close | 1-3k bets | 62-70 | 47.0 | -0.8 | -7.8 |  |
| pin_value+sharp_gap | close | 1-3k bets | 40-45 | 47.1 | -2.5 | -11.3 |  |
| follow_move+money_delta | close | 1-3k bets | 35-56 | 38.5 | -5.8 | -18.6 |  |
| money_delta+pin_move | close | 1-3k bets | 22-27 | 44.9 | 1.0 | -11.2 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 19-40 | 32.2 | -10.3 | -26.9 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 48-77 | 38.4 | -4.4 | -16.1 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 32-58 | 35.6 | -6.1 | -17.1 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 47-71 | 39.8 | -3.2 | -12.8 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 23-54 | 29.9 | -10.9 | -27.2 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 31-61 | 33.7 | -8.1 | -21.7 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 48-77 | 38.4 | -4.4 | -16.1 |  |
| money_delta+money_level | close | 1-3k bets | 18-16 | 52.9 | 5.6 | 3.9 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 6-12 | 33.3 | -6.5 | -25.0 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 8-8 | 50.0 | 8.3 | 7.4 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 25-45 | 35.7 | -6.7 | -21.5 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 5-3 | 62.5 | 19.9 | 47.4 |  |
| money_level+pin_rlm | close | 1-3k bets | 10-10 | 50.0 | 4.3 | -2.2 |  |
| money_moving+pin_rlm | close | 1-3k bets | 27-36 | 42.9 | 0.4 | -7.3 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 27-41 | 39.7 | -2.3 | -14.1 |  |
| money_level+rlm_ratio | close | 1-3k bets | 20-18 | 52.6 | 5.8 | 2.2 |  |
| consensus_gap+money_delta | close | 1-3k bets | 9-6 | 60.0 | 18.1 | 19.1 |  |
| follow_move+pin_rlm | close | 1-3k bets | 22-35 | 38.6 | -3.1 | -15.6 |  |
| money_delta+pin_rlm | close | 1-3k bets | 15-22 | 40.5 | -0.8 | -18.4 |  |
| pin_move+pin_rlm | close | 1-3k bets | 26-35 | 42.6 | 0.2 | -8.1 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 23-32 | 41.8 | -1.0 | -10.0 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 11-26 | 29.7 | -10.3 | -27.7 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 22-35 | 38.6 | -3.1 | -15.6 |  |
| money_delta+pin_value | close | 1-3k bets | 13-7 | 65.0 | 17.3 | 25.6 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 8-10 | 44.4 | -3.0 | 41.6 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 5-5 | 50.0 | 1.8 | -1.2 |  |
| pin_rlm+pin_value | close | 1-3k bets | 4-6 | 40.0 | -8.6 | -19.3 |  |
| money_level+money_moving | close | 3k+ bets | 59-67 | 46.8 | -5.0 | -13.3 |  |
| money_level+sharp_gap | close | 3k+ bets | 54-67 | 44.6 | -6.7 | -15.3 |  |
| money_moving+sharp_gap | close | 3k+ bets | 103-125 | 45.2 | -3.0 | -12.5 |  |
| follow_move+money_delta | close | 3k+ bets | 22-26 | 45.8 | 1.4 | -8.9 |  |
| follow_move+money_level | close | 3k+ bets | 45-35 | 56.2 | 1.2 | -8.2 |  |
| follow_move+money_moving | close | 3k+ bets | 60-65 | 48.0 | -0.1 | -10.9 |  |
| follow_move+pin_move | close | 3k+ bets | 50-58 | 46.3 | -3.5 | -12.2 |  |
| follow_move+pin_rlm | close | 3k+ bets | 14-19 | 42.4 | -0.6 | -13.9 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 25-38 | 39.7 | -4.1 | -20.1 |  |
| follow_move+sharp_gap | close | 3k+ bets | 57-65 | 46.7 | -0.7 | -10.4 |  |
| money_delta+money_level | close | 3k+ bets | 9-10 | 47.4 | -1.8 | -0.7 |  |
| money_delta+money_moving | close | 3k+ bets | 32-35 | 47.8 | 3.2 | -3.9 |  |
| money_delta+pin_move | close | 3k+ bets | 14-18 | 43.8 | -3.8 | -15.6 |  |
| money_delta+pin_rlm | close | 3k+ bets | 10-11 | 47.6 | 1.6 | -5.9 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 12-15 | 44.4 | 1.5 | -11.9 |  |
| money_delta+sharp_gap | close | 3k+ bets | 32-35 | 47.8 | 3.2 | -3.9 |  |
| money_level+pin_move | close | 3k+ bets | 21-32 | 39.6 | -15.4 | -33.3 |  |
| money_level+pin_rlm | close | 3k+ bets | 1-5 | 16.7 | -34.8 | -67.5 |  |
| money_level+rlm_ratio | close | 3k+ bets | 3-7 | 30.0 | -19.5 | -42.3 |  |
| money_moving+pin_move | close | 3k+ bets | 31-44 | 41.3 | -8.0 | -22.6 |  |
| money_moving+pin_rlm | close | 3k+ bets | 16-21 | 43.2 | -0.7 | -13.1 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 24-37 | 39.3 | -4.5 | -21.9 |  |
| pin_move+pin_rlm | close | 3k+ bets | 14-19 | 42.4 | -3.1 | -17.0 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 13-19 | 40.6 | -4.2 | -20.1 |  |
| pin_move+sharp_gap | close | 3k+ bets | 29-45 | 39.2 | -9.6 | -24.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 14-19 | 42.4 | -0.6 | -13.9 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 16-23 | 41.0 | -2.7 | -17.5 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 25-38 | 39.7 | -4.1 | -20.1 |  |
| consensus_gap+money_level | close | 3k+ bets | 30-22 | 57.7 | -1.4 | -5.1 |  |
| consensus_gap+money_moving | close | 3k+ bets | 17-24 | 41.5 | -10.8 | -24.6 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 16-25 | 39.0 | -12.5 | -27.5 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 46-59 | 43.8 | 0.4 | -10.3 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 24-29 | 45.3 | 1.3 | -6.3 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 16-17 | 48.5 | 6.6 | -2.1 |  |
| money_level+pin_value | close | 3k+ bets | 16-31 | 34.0 | -17.6 | -35.9 |  |
| money_moving+pin_value | close | 3k+ bets | 20-29 | 40.8 | -10.8 | -23.0 |  |
| pin_value+sharp_gap | close | 3k+ bets | 20-31 | 39.2 | -12.6 | -26.0 |  |
| consensus_gap+follow_move | close | 3k+ bets | 18-15 | 54.5 | 1.0 | -8.7 |  |
| consensus_gap+pin_value | close | 3k+ bets | 12-12 | 50.0 | -2.1 | -4.8 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 28-36 | 43.8 | -0.2 | -14.1 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 29-36 | 44.6 | 0.8 | -11.2 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 10-16 | 38.5 | -3.5 | -21.9 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 19-30 | 38.8 | -3.9 | -21.6 |  |
| pin_move+pin_value | close | 3k+ bets | 20-29 | 40.8 | -10.2 | -22.6 |  |
| follow_move+pin_value | close | 3k+ bets | 15-21 | 41.7 | -8.6 | -20.8 |  |
| consensus_gap+money_delta | close | 3k+ bets | 5-5 | 50.0 | 4.1 | 4.4 |  |
| consensus_gap+pin_move | close | 3k+ bets | 17-14 | 54.8 | 1.2 | -4.6 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 5-6 | 45.5 | 1.5 | -12.8 |  |
| money_delta+pin_value | close | 3k+ bets | 9-7 | 56.2 | 2.8 | 6.9 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 6-10 | 37.5 | -12.2 | -28.8 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-6 | 33.3 | -13.4 | -36.7 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 2-6 | 25.0 | -17.6 | -52.3 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-6 | 45.5 | -6.8 | -13.9 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 3-5 | 37.5 | -13.1 | -28.4 |  |
| consensus_gap+money_level | close | <1k bets | 13-1 | 92.9 | 36.0 | 48.5 |  |
| consensus_gap+money_moving | close | <1k bets | 8-1 | 88.9 | 36.1 | 81.0 |  |
| consensus_gap+pin_value | close | <1k bets | 5-2 | 71.4 | 28.9 | 85.8 |  |
| consensus_gap+sharp_gap | close | <1k bets | 9-2 | 81.8 | 29.5 | 60.9 |  |
| follow_move+pin_move | close | <1k bets | 14-15 | 48.3 | -1.8 | -9.0 |  |
| follow_move+rlm_quiet | close | <1k bets | 10-19 | 34.5 | -9.1 | -33.2 |  |
| money_level+money_moving | close | <1k bets | 34-18 | 65.4 | 12.6 | 10.0 |  |
| money_level+pin_value | close | <1k bets | 8-4 | 66.7 | 18.9 | 24.9 |  |
| money_level+sharp_gap | close | <1k bets | 34-19 | 64.2 | 11.1 | 8.1 |  |
| money_moving+pin_value | close | <1k bets | 6-5 | 54.5 | 9.7 | 36.2 |  |
| money_moving+sharp_gap | close | <1k bets | 44-36 | 55.0 | 6.0 | 2.4 |  |
| pin_move+rlm_quiet | close | <1k bets | 3-4 | 42.9 | -6.2 | -18.6 |  |
| pin_value+sharp_gap | close | <1k bets | 6-5 | 54.5 | 9.7 | 36.2 |  |
| follow_move+money_moving | close | <1k bets | 22-18 | 55.0 | 5.7 | -3.6 |  |
| follow_move+sharp_gap | close | <1k bets | 21-19 | 52.5 | 3.2 | -5.9 |  |
| money_level+pin_move | close | <1k bets | 14-9 | 60.9 | 10.8 | 14.1 |  |
| money_moving+rlm_quiet | close | <1k bets | 5-7 | 41.7 | -1.9 | -19.1 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 5-7 | 41.7 | -1.9 | -19.1 |  |
| follow_move+money_delta | close | <1k bets | 8-9 | 47.1 | 1.2 | -10.3 |  |
| follow_move+pin_rlm | close | <1k bets | 4-5 | 44.4 | -3.3 | -15.5 |  |
| follow_move+pin_value | close | <1k bets | 5-3 | 62.5 | 13.1 | 19.9 |  |
| follow_move+rlm_ratio | close | <1k bets | 10-12 | 45.5 | 0.8 | -12.8 |  |
| money_delta+money_moving | close | <1k bets | 9-11 | 45.0 | 2.3 | 8.2 |  |
| money_delta+pin_move | close | <1k bets | 1-3 | 25.0 | -22.7 | -52.3 |  |
| money_delta+pin_rlm | close | <1k bets | 1-3 | 25.0 | -22.7 | -52.3 |  |
| money_delta+pin_value | close | <1k bets | 4-0 | 100.0 | 55.7 | 181.8 |  |
| money_delta+rlm_quiet | close | <1k bets | 5-4 | 55.6 | 11.4 | 7.3 |  |
| money_delta+rlm_ratio | close | <1k bets | 5-7 | 41.7 | -2.3 | -20.7 |  |
| money_delta+sharp_gap | close | <1k bets | 9-11 | 45.0 | 2.3 | 8.2 |  |
| money_moving+pin_move | close | <1k bets | 11-9 | 55.0 | 7.3 | 4.3 |  |
| money_moving+pin_rlm | close | <1k bets | 5-5 | 50.0 | 2.3 | -4.9 |  |
| money_moving+rlm_ratio | close | <1k bets | 10-12 | 45.5 | 0.8 | -12.8 |  |
| pin_move+pin_rlm | close | <1k bets | 5-5 | 50.0 | 2.3 | -4.9 |  |
| pin_move+pin_value | close | <1k bets | 7-4 | 63.6 | 14.3 | 20.8 |  |
| pin_move+rlm_ratio | close | <1k bets | 4-5 | 44.4 | -3.3 | -15.5 |  |
| pin_move+sharp_gap | close | <1k bets | 11-9 | 55.0 | 7.3 | 4.3 |  |
| pin_rlm+pin_value | close | <1k bets | 2-0 | 100.0 | 52.3 | 90.9 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 2-1 | 66.7 | 17.4 | 26.2 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 4-5 | 44.4 | -3.3 | -15.5 |  |
| pin_rlm+sharp_gap | close | <1k bets | 5-5 | 50.0 | 2.3 | -4.9 |  |
| pin_value+rlm_quiet | close | <1k bets | 3-0 | 100.0 | 52.3 | 90.9 |  |
| pin_value+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 52.3 | 90.9 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 5-6 | 45.5 | 2.3 | -11.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 10-12 | 45.5 | 0.8 | -12.8 |  |
| consensus_gap+follow_move | close | <1k bets | 5-1 | 83.3 | 28.8 | 42.8 |  |
| consensus_gap+pin_move | close | <1k bets | 2-0 | 100.0 | 43.2 | 70.5 |  |
| follow_move+money_level | close | <1k bets | 24-13 | 64.9 | 10.0 | 7.3 |  |
| money_delta+money_level | close | <1k bets | 3-3 | 50.0 | 7.6 | 7.7 |  |
| money_level+pin_rlm | close | <1k bets | 2-3 | 40.0 | -6.8 | -23.6 |  |
| money_level+rlm_ratio | close | <1k bets | 4-4 | 50.0 | 5.1 | -5.5 |  |
| consensus_gap+money_delta | close | <1k bets | 3-0 | 100.0 | 50.8 | 208.0 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 52.3 | 89.3 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-1 | 50.0 | 9.1 | -4.5 |  |
| money_delta+money_moving | close | pin $1-2k | 29-25 | 53.7 | 8.8 | 13.0 |  |
| money_delta+sharp_gap | close | pin $1-2k | 29-25 | 53.7 | 8.8 | 13.0 |  |
| money_moving+sharp_gap | close | pin $1-2k | 110-113 | 49.3 | 0.5 | -4.7 |  |
| consensus_gap+follow_move | close | pin $1-2k | 10-11 | 47.6 | -2.9 | -11.2 |  |
| consensus_gap+money_level | close | pin $1-2k | 17-15 | 53.1 | -2.6 | -11.9 |  |
| consensus_gap+money_moving | close | pin $1-2k | 9-13 | 40.9 | -8.5 | -10.5 |  |
| consensus_gap+pin_move | close | pin $1-2k | 12-11 | 52.2 | 3.5 | 14.4 |  |
| consensus_gap+pin_value | close | pin $1-2k | 17-15 | 53.1 | 4.7 | 12.8 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 9-13 | 40.9 | -8.5 | -9.3 |  |
| follow_move+money_level | close | pin $1-2k | 49-53 | 48.0 | -5.0 | -15.5 |  |
| follow_move+money_moving | close | pin $1-2k | 60-68 | 46.9 | -1.9 | -10.9 |  |
| follow_move+pin_move | close | pin $1-2k | 55-89 | 38.2 | -10.7 | -25.5 |  |
| follow_move+pin_value | close | pin $1-2k | 26-30 | 46.4 | -2.8 | -11.8 |  |
| follow_move+sharp_gap | close | pin $1-2k | 61-71 | 46.2 | -2.6 | -12.0 |  |
| money_level+money_moving | close | pin $1-2k | 78-75 | 51.0 | -0.6 | -8.7 |  |
| money_level+pin_move | close | pin $1-2k | 39-49 | 44.3 | -7.4 | -19.7 |  |
| money_level+pin_value | close | pin $1-2k | 32-33 | 49.2 | -0.4 | -8.1 |  |
| money_level+sharp_gap | close | pin $1-2k | 73-76 | 49.0 | -2.2 | -11.1 |  |
| money_moving+pin_move | close | pin $1-2k | 47-50 | 48.5 | -0.7 | -7.0 |  |
| money_moving+pin_value | close | pin $1-2k | 27-29 | 48.2 | -0.2 | -2.5 |  |
| pin_move+pin_value | close | pin $1-2k | 28-37 | 43.1 | -7.6 | -18.4 |  |
| pin_move+sharp_gap | close | pin $1-2k | 46-56 | 45.1 | -3.3 | -12.8 |  |
| pin_value+sharp_gap | close | pin $1-2k | 27-29 | 48.2 | -0.2 | -2.5 |  |
| follow_move+money_delta | close | pin $1-2k | 23-27 | 46.0 | -0.6 | -10.2 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 35-55 | 38.9 | -6.1 | -19.4 |  |
| money_delta+pin_move | close | pin $1-2k | 17-17 | 50.0 | 4.0 | -1.8 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 13-17 | 43.3 | -2.3 | -14.8 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 23-35 | 39.7 | -6.0 | -16.7 |  |
| follow_move+pin_rlm | close | pin $1-2k | 17-23 | 42.5 | -2.3 | -11.3 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 28-34 | 45.2 | 0.4 | -7.7 |  |
| pin_move+pin_rlm | close | pin $1-2k | 19-23 | 45.2 | 0.1 | -6.1 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 17-22 | 43.6 | -1.9 | -9.1 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 10-17 | 37.0 | -7.1 | -18.7 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 17-23 | 42.5 | -2.3 | -11.3 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 19-26 | 42.2 | -2.2 | -12.4 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 15-23 | 39.5 | -4.5 | -16.4 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 20-27 | 42.6 | -2.0 | -11.8 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 28-34 | 45.2 | 0.4 | -7.7 |  |
| money_delta+money_level | close | pin $1-2k | 11-11 | 50.0 | 2.5 | -2.9 |  |
| money_delta+pin_rlm | close | pin $1-2k | 11-12 | 47.8 | 3.7 | -4.9 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 14-15 | 48.3 | 3.4 | -4.6 |  |
| money_level+pin_rlm | close | pin $1-2k | 6-7 | 46.2 | 1.2 | -10.0 |  |
| money_level+rlm_ratio | close | pin $1-2k | 9-9 | 50.0 | 4.1 | -3.6 |  |
| money_moving+pin_rlm | close | pin $1-2k | 19-21 | 47.5 | 2.2 | -1.5 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 28-30 | 48.3 | 3.0 | -1.3 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 20-26 | 43.5 | -1.0 | -9.9 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 3-4 | 42.9 | 1.0 | -11.5 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 7-13 | 35.0 | -13.0 | -30.4 |  |
| money_delta+pin_value | close | pin $1-2k | 11-7 | 61.1 | 14.7 | 38.6 |  |
| consensus_gap+money_delta | close | pin $1-2k | 5-1 | 83.3 | 39.4 | 125.7 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 1-2 | 33.3 | -6.8 | -20.7 |  |
| pin_rlm+pin_value | close | pin $1-2k | 4-5 | 44.4 | -3.8 | -10.4 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 3-5 | 37.5 | -9.7 | -23.0 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 1-1 | 50.0 | 6.8 | 19.0 |  |
| follow_move+pin_move | close | pin $2k+ | 70-78 | 47.3 | -2.4 | -9.0 |  |
| consensus_gap+money_level | close | pin $2k+ | 41-25 | 62.1 | 2.0 | -2.2 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 45-53 | 45.9 | 4.4 | 10.9 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 30-41 | 42.3 | -0.6 | -6.7 |  |
| money_level+money_moving | close | pin $2k+ | 64-74 | 46.4 | -5.5 | -14.7 |  |
| money_level+sharp_gap | close | pin $2k+ | 60-76 | 44.1 | -7.7 | -17.4 |  |
| money_moving+sharp_gap | close | pin $2k+ | 101-125 | 44.7 | -2.8 | -11.4 |  |
| consensus_gap+pin_value | close | pin $2k+ | 22-15 | 59.5 | 9.5 | 12.2 |  |
| follow_move+money_level | close | pin $2k+ | 45-41 | 52.3 | -4.4 | -16.3 |  |
| follow_move+money_moving | close | pin $2k+ | 52-65 | 44.4 | -3.2 | -15.2 |  |
| follow_move+sharp_gap | close | pin $2k+ | 48-65 | 42.5 | -4.9 | -17.7 |  |
| money_level+pin_move | close | pin $2k+ | 32-31 | 50.8 | -6.2 | -16.4 |  |
| money_moving+pin_move | close | pin $2k+ | 39-51 | 43.3 | -4.3 | -15.6 |  |
| pin_move+sharp_gap | close | pin $2k+ | 38-53 | 41.8 | -5.9 | -17.8 |  |
| money_delta+money_level | close | pin $2k+ | 9-6 | 60.0 | 14.1 | 30.5 |  |
| money_delta+money_moving | close | pin $2k+ | 27-36 | 42.9 | 0.9 | -11.1 |  |
| money_delta+sharp_gap | close | pin $2k+ | 27-36 | 42.9 | 0.9 | -11.1 |  |
| consensus_gap+money_moving | close | pin $2k+ | 21-22 | 48.8 | -3.4 | -2.2 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 20-23 | 46.5 | -5.8 | -5.0 |  |
| money_level+pin_value | close | pin $2k+ | 18-31 | 36.7 | -13.7 | -31.4 |  |
| money_moving+pin_value | close | pin $2k+ | 22-31 | 41.5 | -9.5 | -22.1 |  |
| pin_value+sharp_gap | close | pin $2k+ | 22-34 | 39.3 | -12.2 | -26.2 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 6-6 | 50.0 | 4.6 | 9.2 |  |
| money_level+pin_rlm | close | pin $2k+ | 2-7 | 22.2 | -26.0 | -55.0 |  |
| money_moving+pin_rlm | close | pin $2k+ | 20-29 | 40.8 | 0.8 | -11.5 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 20-31 | 39.2 | -0.8 | -14.9 |  |
| follow_move+money_delta | close | pin $2k+ | 15-22 | 40.5 | -1.1 | -17.4 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 19-32 | 37.3 | -2.5 | -20.0 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 9-18 | 33.3 | -6.9 | -32.5 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 19-31 | 38.0 | -1.6 | -18.4 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 19-32 | 37.3 | -2.5 | -20.0 |  |
| money_level+rlm_ratio | close | pin $2k+ | 5-8 | 38.5 | -7.1 | -25.8 |  |
| consensus_gap+follow_move | close | pin $2k+ | 20-11 | 64.5 | 7.8 | 8.9 |  |
| consensus_gap+pin_move | close | pin $2k+ | 26-13 | 66.7 | 13.0 | 26.9 |  |
| follow_move+pin_value | close | pin $2k+ | 15-15 | 50.0 | -1.4 | 26.6 |  |
| pin_move+pin_value | close | pin $2k+ | 23-24 | 48.9 | -3.1 | -7.6 |  |
| follow_move+pin_rlm | close | pin $2k+ | 16-25 | 39.0 | 0.5 | -14.2 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 16-25 | 39.0 | 0.5 | -14.2 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 6-4 | 60.0 | 10.5 | 110.8 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 20-28 | 41.7 | 1.7 | -9.5 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 19-28 | 40.4 | 0.1 | -13.1 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 11-16 | 40.7 | 1.1 | -15.8 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 12-22 | 35.3 | -2.1 | -20.9 |  |
| money_delta+pin_move | close | pin $2k+ | 15-21 | 41.7 | -2.7 | -18.3 |  |
| money_delta+pin_rlm | close | pin $2k+ | 11-17 | 39.3 | -2.1 | -20.5 |  |
| pin_move+pin_rlm | close | pin $2k+ | 17-24 | 41.5 | 0.8 | -11.4 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 16-23 | 41.0 | 0.3 | -13.6 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 12-20 | 37.5 | -0.1 | -16.0 |  |
| consensus_gap+money_delta | close | pin $2k+ | 6-3 | 66.7 | 18.5 | 38.7 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 4-4 | 50.0 | 9.7 | 14.1 |  |
| money_delta+pin_value | close | pin $2k+ | 8-5 | 61.5 | 6.5 | 17.0 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 5-4 | 55.6 | 12.4 | 21.9 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 4-2 | 66.7 | 14.4 | 26.2 |  |
| pin_rlm+pin_value | close | pin $2k+ | 5-4 | 55.6 | 1.8 | 5.7 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 5-5 | 50.0 | 2.3 | -4.0 |  |
| consensus_gap+money_level | close | pin limit <$1k | 6-6 | 50.0 | -1.9 | -5.5 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 6-10 | 37.5 | -10.8 | -28.1 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 8-12 | 40.0 | -9.5 | -24.2 |  |
| follow_move+money_level | close | pin limit <$1k | 26-18 | 59.1 | 8.1 | 11.0 |  |
| follow_move+money_moving | close | pin limit <$1k | 24-28 | 46.2 | -3.2 | -11.6 |  |
| follow_move+pin_value | close | pin limit <$1k | 14-8 | 63.6 | 12.8 | 21.1 |  |
| money_level+money_moving | close | pin limit <$1k | 31-27 | 53.4 | 2.6 | 1.8 |  |
| money_level+pin_value | close | pin limit <$1k | 21-13 | 61.8 | 10.0 | 17.4 |  |
| money_moving+pin_value | close | pin limit <$1k | 18-17 | 51.4 | 1.2 | -2.4 |  |
| follow_move+pin_move | close | pin limit <$1k | 24-22 | 52.2 | 3.0 | 0.3 |  |
| money_level+pin_move | close | pin limit <$1k | 24-14 | 63.2 | 12.7 | 20.6 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 38-44 | 46.3 | -3.2 | -11.6 |  |
| pin_move+pin_value | close | pin limit <$1k | 16-12 | 57.1 | 7.0 | 9.0 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 15-19 | 44.1 | -3.7 | -14.9 |  |
| money_moving+pin_move | close | pin limit <$1k | 21-19 | 52.5 | 3.4 | 0.5 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 3-2 | 60.0 | 15.0 | 16.4 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 4-4 | 50.0 | 2.8 | -3.4 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 1-2 | 33.3 | -9.8 | -33.3 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 3-3 | 50.0 | 4.6 | -3.0 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 2-3 | 40.0 | -5.0 | -21.8 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 6-11 | 35.3 | -13.0 | -32.3 |  |
| follow_move+money_delta | close | pin limit <$1k | 6-12 | 33.3 | -13.9 | -35.8 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 7-11 | 38.9 | -8.8 | -25.0 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 10-17 | 37.0 | -10.9 | -28.9 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 23-27 | 46.0 | -3.4 | -12.0 |  |
| money_delta+money_moving | close | pin limit <$1k | 10-14 | 41.7 | -5.7 | -19.9 |  |
| money_delta+pin_move | close | pin limit <$1k | 5-10 | 33.3 | -13.5 | -35.7 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 4-7 | 36.4 | -10.1 | -29.7 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 3-5 | 37.5 | -8.5 | -27.3 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 5-11 | 31.2 | -15.9 | -39.8 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 10-14 | 41.7 | -5.7 | -19.9 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 9-12 | 42.9 | -4.9 | -17.7 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 4-11 | 26.7 | -20.8 | -48.5 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 9-16 | 36.0 | -11.9 | -30.9 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 9-12 | 42.9 | -4.9 | -17.7 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 6-10 | 37.5 | -10.2 | -27.0 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 7-11 | 38.9 | -8.8 | -25.0 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 18-18 | 50.0 | 1.1 | -4.3 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 1-6 | 14.3 | -32.1 | -71.4 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 7-11 | 38.9 | -8.8 | -25.0 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 9-12 | 42.9 | -4.9 | -17.7 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 3-11 | 21.4 | -25.6 | -58.4 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 4-11 | 26.7 | -20.8 | -48.7 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 10-17 | 37.0 | -10.9 | -28.9 |  |
| money_delta+pin_value | close | pin limit <$1k | 7-2 | 77.8 | 29.5 | 48.1 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 4-3 | 57.1 | 8.8 | 8.5 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 2-3 | 40.0 | -8.6 | -24.4 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 17-19 | 47.2 | -2.9 | -10.4 |  |
| money_level+sharp_gap | close | pin limit <$1k | 27-26 | 50.9 | 0.1 | -2.9 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 2-3 | 40.0 | -7.7 | -24.4 |  |
| money_delta+money_level | close | pin limit <$1k | 1-6 | 14.3 | -33.4 | -72.1 |  |
| money_level+pin_rlm | close | pin limit <$1k | 5-4 | 55.6 | 6.8 | 6.5 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 5-5 | 50.0 | 1.4 | -4.1 |  |
| rlm_quiet | early | <1k bets | 26-35 | 42.6 | 2.9 | 1.8 | 1.03 |
| rlm_quiet | early | pin $1-2k | 2-2 | 50.0 | 16.0 | 23.0 | 1.12 |
| rlm_quiet | early | pin limit <$1k | 1-2 | 33.3 | -14.4 | -36.4 | 0.33 |
| pin_move | early | <1k bets | 9-13 | 40.9 | -8.5 | -23.2 | 0.12 |
| pin_move | early | pin $1-2k | 2-6 | 25.0 | -25.6 | -56.8 | 0.29 |
| pin_move | early | pin limit <$1k | 7-10 | 41.2 | -8.2 | -20.9 | 0.59 |
| money_delta | early | <1k bets | 4-5 | 44.4 | 5.9 | 16.3 | 3.02 |
| money_delta | early | pin $1-2k | 0-1 | 0.0 | -34.0 | -100.0 | 1.5 |
| money_delta | early | pin limit <$1k | 1-0 | 100.0 | 52.3 | 90.9 | 1.0 |
| pin_rlm | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -66.0 | -100.0 | 1.5 |
| pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -34.0 | -100.0 | 0.0 |
| follow_move | early | <1k bets | 225-240 | 48.4 | -0.7 | -7.8 | 0.15 |
| follow_move | early | pin $1-2k | 14-15 | 48.3 | 2.8 | -2.9 | -0.35 |
| follow_move | early | pin limit <$1k | 13-21 | 38.2 | -10.4 | -25.6 | 0.01 |
| rlm_ratio | early | <1k bets | 10-17 | 37.0 | -5.8 | -11.1 | 0.72 |
| rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -66.0 | -100.0 | 1.5 |
| rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 9.1 | -4.5 | 0.5 |
| money_level | early | <1k bets | 77-64 | 54.6 | -2.5 | -12.4 | -0.43 |
| money_level | early | pin $1-2k | 3-5 | 37.5 | -21.6 | -38.8 | -0.29 |
| money_level | early | pin limit <$1k | 8-6 | 57.1 | 6.8 | 9.1 | 0.29 |
| sharp_gap | early | <1k bets | 59-67 | 46.8 | -3.3 | -11.2 | 0.26 |
| sharp_gap | early | pin $1-2k | 2-6 | 25.0 | -35.8 | -63.1 | -0.04 |
| sharp_gap | early | pin limit <$1k | 7-5 | 58.3 | 9.1 | 11.4 | 0.33 |
| money_moving | early | <1k bets | 50-45 | 52.6 | 3.0 | -1.3 | 0.6 |
| money_moving | early | pin $1-2k | 0-4 | 0.0 | -55.7 | -100.0 | 1.05 |
| money_moving | early | pin limit <$1k | 10-2 | 83.3 | 32.9 | 57.2 | 0.25 |
| pin_value | early | <1k bets | 22-19 | 53.7 | 4.3 | 1.5 | 0.09 |
| pin_value | early | pin $1-2k | 6-11 | 35.3 | -13.2 | -33.8 | 0.34 |
| pin_value | early | pin limit <$1k | 17-9 | 65.4 | 15.6 | 24.0 | -0.04 |
| consensus_gap | early | <1k bets | 121-113 | 51.7 | -0.8 | -9.5 | 0.48 |
| consensus_gap | early | pin $1-2k | 10-5 | 66.7 | 16.5 | 23.1 | -0.17 |
| consensus_gap | early | pin limit <$1k | 8-4 | 66.7 | 16.3 | 26.7 | 0.08 |
| follow_move+money_level | early | <1k bets | 28-20 | 58.3 | 1.2 | -13.9 | 0.22 |
| follow_move+sharp_gap | early | <1k bets | 25-28 | 47.2 | -1.4 | -9.3 | 0.82 |
| money_level+sharp_gap | early | <1k bets | 39-38 | 50.6 | -4.9 | -16.0 | -0.2 |
| follow_move+money_moving | early | <1k bets | 21-20 | 51.2 | 2.1 | -1.5 | 0.84 |
| money_level+money_moving | early | <1k bets | 24-18 | 57.1 | 1.7 | -4.1 | 0.42 |
| consensus_gap+money_level | early | <1k bets | 26-19 | 57.8 | -2.5 | -11.8 | -0.63 |
| follow_move+rlm_quiet | early | <1k bets | 26-35 | 42.6 | 2.9 | 1.8 | 1.03 |
| follow_move+rlm_ratio | early | <1k bets | 10-17 | 37.0 | -5.8 | -11.1 | 0.72 |
| rlm_quiet+rlm_ratio | early | <1k bets | 9-11 | 45.0 | 3.9 | 10.5 | 0.74 |
| rlm_quiet+sharp_gap | early | <1k bets | 10-14 | 41.7 | 0.0 | 0.1 | 1.05 |
| rlm_ratio+sharp_gap | early | <1k bets | 10-17 | 37.0 | -5.8 | -11.1 | 0.72 |
| consensus_gap+follow_move | early | <1k bets | 16-21 | 43.2 | -11.8 | -28.1 | 1.06 |
| money_moving+rlm_quiet | early | <1k bets | 9-11 | 45.0 | 3.9 | 9.9 | 1.31 |
| money_moving+rlm_ratio | early | <1k bets | 7-7 | 50.0 | 7.2 | 21.8 | 2.11 |
| money_moving+sharp_gap | early | <1k bets | 28-30 | 48.3 | 0.4 | -2.1 | 0.84 |
| consensus_gap+money_moving | early | <1k bets | 11-6 | 64.7 | 10.5 | 5.2 | 1.21 |
| consensus_gap+sharp_gap | early | <1k bets | 16-17 | 48.5 | -7.0 | -22.7 | -0.34 |
| money_level+rlm_ratio | early | <1k bets | 1-6 | 14.3 | -33.4 | -72.7 | 0.64 |
| follow_move+pin_move | early | <1k bets | 4-7 | 36.4 | -10.9 | -29.9 | 0.55 |
| follow_move+money_delta | early | <1k bets | 3-2 | 60.0 | 20.5 | 71.2 | 2.74 |
| money_delta+money_level | early | <1k bets | 1-3 | 25.0 | -15.9 | -52.3 | 1.68 |
| money_delta+money_moving | early | <1k bets | 4-5 | 44.4 | 5.9 | 16.3 | 3.02 |
| money_delta+rlm_ratio | early | <1k bets | 3-2 | 60.0 | 20.5 | 71.2 | 2.74 |
| money_delta+sharp_gap | early | <1k bets | 4-5 | 44.4 | 5.9 | 16.3 | 3.02 |
| follow_move+pin_value | early | <1k bets | 5-5 | 50.0 | 0.9 | -4.1 | -0.3 |
| consensus_gap+pin_move | early | <1k bets | 2-1 | 66.7 | 14.4 | 28.7 | 0.33 |
| consensus_gap+pin_value | early | <1k bets | 10-3 | 76.9 | 28.1 | 45.4 | -0.15 |
| money_level+pin_move | early | <1k bets | 2-4 | 33.3 | -14.4 | -35.8 | 0.17 |
| money_level+pin_value | early | <1k bets | 3-3 | 50.0 | -3.8 | -4.5 | 0.78 |
| pin_move+pin_value | early | <1k bets | 4-7 | 36.4 | -13.4 | -29.8 | 0.55 |
| money_moving+pin_value | early | <1k bets | 3-2 | 60.0 | 6.8 | 15.4 | 1.14 |
| pin_value+sharp_gap | early | <1k bets | 1-4 | 20.0 | -35.0 | -61.8 | 1.34 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 52.3 | 90.9 | 1.0 |
| consensus_gap+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 52.3 | 90.9 | 1.0 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 52.3 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 52.3 | 90.9 | 1.0 |
| follow_move+pin_rlm | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| money_level+pin_rlm | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_rlm+rlm_ratio | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_rlm+sharp_gap | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_move+sharp_gap | early | <1k bets | 0-3 | 0.0 | -46.2 | -100.0 | 1.0 |
| money_delta+rlm_quiet | early | <1k bets | 2-1 | 66.7 | 32.6 | 121.7 | 3.57 |
| consensus_gap+rlm_quiet | early | <1k bets | 1-1 | 50.0 | 16.0 | 30.0 | 1.1 |
| money_moving+pin_move | early | <1k bets | 1-1 | 50.0 | 2.3 | -2.4 | 1.0 |
| pin_move+pin_rlm | early | <1k bets | 0-1 | 0.0 | -34.0 | -100.0 | 0.0 |
| pin_move+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -34.0 | -100.0 | 0.0 |
| pin_move+pin_value | early | pin $1-2k | 0-4 | 0.0 | -46.6 | -100.0 | 0.5 |
| follow_move+rlm_quiet | early | pin $1-2k | 2-2 | 50.0 | 16.0 | 23.0 | 1.12 |
| money_level+money_moving | early | pin $1-2k | 0-3 | 0.0 | -55.3 | -100.0 | 1.07 |
| money_level+pin_value | early | pin $1-2k | 0-1 | 0.0 | -66.0 | -100.0 | 1.7 |
| money_level+sharp_gap | early | pin $1-2k | 2-5 | 28.6 | -32.8 | -57.8 | -0.19 |
| money_moving+pin_value | early | pin $1-2k | 0-2 | 0.0 | -61.4 | -100.0 | 1.35 |
| money_moving+sharp_gap | early | pin $1-2k | 0-4 | 0.0 | -55.7 | -100.0 | 1.05 |
| pin_value+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -61.4 | -100.0 | 1.35 |
| consensus_gap+pin_value | early | pin $1-2k | 3-1 | 75.0 | 28.4 | 39.3 | -0.5 |
| follow_move+money_level | early | pin $1-2k | 1-2 | 33.3 | -25.0 | -35.2 | 0.17 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -66.0 | -100.0 | 1.5 |
| follow_move+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -66.0 | -100.0 | 1.5 |
| follow_move+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -66.0 | -100.0 | 0.75 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -66.0 | -100.0 | 1.5 |
| money_level+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -66.0 | -100.0 | 1.5 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -66.0 | -100.0 | 1.5 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -66.0 | -100.0 | 1.5 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -66.0 | -100.0 | 1.5 |
| consensus_gap+follow_move | early | pin $1-2k | 2-1 | 66.7 | 22.0 | 55.3 | 0.6 |
| follow_move+pin_move | early | pin $1-2k | 1-2 | 33.3 | -14.4 | -35.2 | -0.33 |
| follow_move+pin_value | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap+money_level | early | pin $1-2k | 2-1 | 66.7 | 0.7 | -1.6 | -1.83 |
| consensus_gap+sharp_gap | early | pin $1-2k | 2-1 | 66.7 | 0.7 | -1.6 | -1.83 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 1-0 | 100.0 | 66.0 | 160.0 | 0.3 |
| consensus_gap+money_moving | early | pin $1-2k | 0-1 | 0.0 | -66.0 | -100.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 0-1 | 0.0 | -66.0 | -100.0 | 0.0 |
| money_level+pin_move | early | pin $1-2k | 1-0 | 100.0 | 56.8 | 94.3 | -1.0 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -34.0 | -100.0 | 1.5 |
| money_delta+money_moving | early | pin $1-2k | 0-1 | 0.0 | -34.0 | -100.0 | 1.5 |
| money_delta+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -34.0 | -100.0 | 1.5 |
| follow_move+pin_move | early | pin limit <$1k | 3-6 | 33.3 | -13.9 | -35.9 | 0.89 |
| follow_move+pin_value | early | pin limit <$1k | 5-3 | 62.5 | 13.6 | 19.9 | -0.38 |
| consensus_gap+money_level | early | pin limit <$1k | 3-0 | 100.0 | 49.2 | 90.9 | 0.0 |
| consensus_gap+pin_move | early | pin limit <$1k | 2-1 | 66.7 | 14.4 | 28.7 | 0.33 |
| consensus_gap+pin_value | early | pin limit <$1k | 7-2 | 77.8 | 28.0 | 48.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 4-2 | 66.7 | 18.2 | 28.0 | 0.5 |
| follow_move+rlm_quiet | early | pin limit <$1k | 1-2 | 33.3 | -14.4 | -36.4 | 0.33 |
| follow_move+sharp_gap | early | pin limit <$1k | 3-3 | 50.0 | 3.0 | -3.8 | 0.17 |
| money_level+pin_move | early | pin limit <$1k | 1-4 | 20.0 | -28.6 | -61.8 | 0.4 |
| money_level+pin_value | early | pin limit <$1k | 4-2 | 66.7 | 15.2 | 26.6 | 0.33 |
| money_moving+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 2.3 | -4.5 | 0.0 |
| money_moving+sharp_gap | early | pin limit <$1k | 6-1 | 85.7 | 36.0 | 63.7 | 0.0 |
| pin_move+pin_value | early | pin limit <$1k | 4-4 | 50.0 | -0.6 | -3.5 | 0.75 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -47.7 | -100.0 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 | -0.5 |
| consensus_gap+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 52.3 | 90.9 | 1.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 52.3 | 92.3 | 1.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.3 | 90.9 | 1.0 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 52.3 | 90.9 | 1.0 |
| follow_move+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 52.3 | 90.9 | 1.0 |
| follow_move+money_level | early | pin limit <$1k | 3-3 | 50.0 | 2.3 | -3.8 | 0.0 |
| follow_move+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 9.1 | -4.5 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 52.3 | 90.9 | 1.0 |
| money_delta+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 52.3 | 90.9 | 1.0 |
| money_delta+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 52.3 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.3 | 90.9 | 1.0 |
| money_delta+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 52.3 | 90.9 | 1.0 |
| money_level+money_moving | early | pin limit <$1k | 5-0 | 100.0 | 49.5 | 91.0 | 0.2 |
| money_level+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 9.1 | -4.5 | 0.5 |
| money_level+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 10.5 | 14.6 | 0.5 |
| money_moving+pin_value | early | pin limit <$1k | 4-0 | 100.0 | 51.1 | 91.0 | 0.5 |
| money_moving+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.3 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.3 | 90.9 | 1.0 |
| pin_value+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | -1.1 | -5.5 | 0.75 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 9.1 | -4.5 | 0.5 |
| pin_move+sharp_gap | early | pin limit <$1k | 0-3 | 0.0 | -46.2 | -100.0 | 1.0 |
| money_moving+pin_move | early | pin limit <$1k | 1-1 | 50.0 | 2.3 | -2.4 | 1.0 |
| follow_move+pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -34.0 | -100.0 | 0.0 |
| money_level+pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -34.0 | -100.0 | 0.0 |
| pin_move+pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -34.0 | -100.0 | 0.0 |
| pin_move+rlm_ratio | early | pin limit <$1k | 0-1 | 0.0 | -34.0 | -100.0 | 0.0 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 0-1 | 0.0 | -34.0 | -100.0 | 0.0 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -34.0 | -100.0 | 0.0 |
| pin_move+rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -47.7 | -100.0 | 1.0 |
