# CBB scorecard

Generated 2026-11-21 02:51 UTC. 701 graded games (36 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**685 games before 2026-11-21 (fit) · 16 on or after it (forward).**

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
sample ran **47.9% favourites** (n=700) and **49.6% overs** (n=701) and **73.4% moneyline favourites** (n=597).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-21. Nothing in the engine was chosen using these. n=16 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 1-2 | 33.3 | 35.7 | -2.4 | -1.09 | -36.4 | -0.73 | 33.3 | keep collecting (3/30) |
| follow_move | both | 6-4 | 60.0 | 44.8 | 15.2 | +2.76 | 27.6 | -0.86 | 10.0 | keep collecting (10/30) |
| rlm_ratio | both | 1-1 | 50.0 | 39.3 | 10.7 | -0.09 | -4.5 | 0.35 | 50.0 | keep collecting (2/30) |
| money_level | both | 6-3 | 66.7 | 59.5 | 7.1 | +0.71 | 7.9 | 0.63 | 44.4 | keep collecting (9/30) |
| sharp_gap | both | 4-3 | 57.1 | 46.9 | 10.2 | +0.46 | 6.5 | 0.74 | 42.9 | keep collecting (7/30) |
| money_moving | both | 3-2 | 60.0 | 58.6 | 1.4 | -0.25 | -5.0 | 0.26 | 40.0 | keep collecting (5/30) |
| pin_value | both | 0-1 | 0.0 | 43.8 | -43.8 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap | both | 3-1 | 75.0 | 71.4 | 3.6 | -0.02 | -0.5 | 1.17 | 75.0 | keep collecting (4/30) |
| follow_move+money_level | both | 2-1 | 66.7 | 57.1 | 9.5 | +0.02 | 0.7 | -0.73 | 0.0 | keep collecting (3/30) |
| follow_move+sharp_gap | both | 2-1 | 66.7 | 42.9 | 23.8 | +0.82 | 27.3 | 0.23 | 33.3 | keep collecting (3/30) |
| money_level+sharp_gap | both | 2-0 | 100.0 | 60.7 | 39.3 | +1.64 | 82.0 | 1.25 | 50.0 | keep collecting (2/30) |
| follow_move+money_moving | both | 2-1 | 66.7 | 57.1 | 9.5 | +0.02 | 0.7 | -0.4 | 33.3 | keep collecting (3/30) |
| money_level+money_moving | both | 2-1 | 66.7 | 64.3 | 2.4 | -0.16 | -5.3 | 0.1 | 33.3 | keep collecting (3/30) |
| consensus_gap+money_level | both | 3-1 | 75.0 | 71.4 | 3.6 | -0.02 | -0.5 | 1.17 | 75.0 | redundant -- identical record to consensus_gap alone, not independent confirmation |
| follow_move+rlm_quiet | both | 1-2 | 33.3 | 35.7 | -2.4 | -1.09 | -36.4 | -0.73 | 33.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 1-1 | 50.0 | 39.3 | 10.7 | -0.09 | -4.5 | 0.35 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | both | 1-1 | 50.0 | 39.3 | 10.7 | -0.09 | -4.5 | 0.35 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 1-1 | 50.0 | 39.3 | 10.7 | -0.09 | -4.5 | 0.35 | 50.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | both | 1-1 | 50.0 | 39.3 | 10.7 | -0.09 | -4.5 | 0.35 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | both | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_moving+rlm_ratio | both | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_moving+sharp_gap | both | 2-0 | 100.0 | 60.7 | 39.3 | +1.64 | 82.0 | 1.75 | 100.0 | keep collecting (2/30) |
| consensus_gap+money_moving | both | 2-0 | 100.0 | 71.4 | 28.6 | +0.84 | 42.0 | 0.15 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | both | 1-0 | 100.0 | 71.4 | 28.6 | +0.73 | 73.0 | 2.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 1-0 | 100.0 | 71.4 | 28.6 | +0.11 | 11.1 | -2.2 | 0.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 | -1.6 | 0.0 | keep collecting (2/30) |
| rlm_quiet | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| follow_move | moneyline | 3-2 | 60.0 | 37.1 | 22.9 | +2.03 | 40.6 | -1.92 | 0.0 | keep collecting (5/30) |
| follow_move | spread | 1-1 | 50.0 | 56.2 | -6.2 | -0.09 | -4.5 | 0.0 | 0.0 | keep collecting (2/30) |
| follow_move | total | 2-1 | 66.7 | 50.0 | 16.7 | +0.82 | 27.3 | 0.33 | 33.3 | keep collecting (3/30) |
| rlm_ratio | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | -0.3 | 0.0 | keep collecting (1/30) |
| rlm_ratio | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level | moneyline | 3-1 | 75.0 | 71.4 | 3.6 | -0.02 | -0.5 | 1.17 | 75.0 | keep collecting (4/30) |
| money_level | total | 3-2 | 60.0 | 50.0 | 10.0 | +0.73 | 14.5 | 0.2 | 20.0 | keep collecting (5/30) |
| sharp_gap | moneyline | 1-2 | 33.3 | 42.9 | -9.5 | -1.27 | -42.3 | 1.4 | 66.7 | keep collecting (3/30) |
| sharp_gap | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.73 | 43.2 | 0.25 | 25.0 | keep collecting (4/30) |
| money_moving | moneyline | 2-0 | 100.0 | 71.4 | 28.6 | +0.84 | 42.0 | 0.15 | 50.0 | keep collecting (2/30) |
| money_moving | total | 1-2 | 33.3 | 50.0 | -16.7 | -1.09 | -36.4 | 0.33 | 33.3 | keep collecting (3/30) |
| pin_value | spread | 0-1 | 0.0 | 43.8 | -43.8 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap | moneyline | 3-1 | 75.0 | 71.4 | 3.6 | -0.02 | -0.5 | 1.17 | 75.0 | keep collecting (4/30) |
| consensus_gap+money_level | moneyline | 3-1 | 75.0 | 71.4 | 3.6 | -0.02 | -0.5 | 1.17 | 75.0 | redundant -- identical record to consensus_gap alone, not independent confirmation |
| follow_move+rlm_quiet | moneyline | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 | -1.6 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | -0.3 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | -0.3 | 0.0 | keep collecting (1/30) |
| rlm_quiet+rlm_ratio | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | -0.3 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | -0.3 | 0.0 | keep collecting (1/30) |
| rlm_ratio+sharp_gap | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | -0.3 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 2-0 | 100.0 | 71.4 | 28.6 | +0.84 | 42.0 | 0.15 | 50.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| consensus_gap+sharp_gap | moneyline | 1-0 | 100.0 | 71.4 | 28.6 | +0.73 | 73.0 | 2.5 | 100.0 | keep collecting (1/30) |
| money_level+money_moving | moneyline | 2-0 | 100.0 | 71.4 | 28.6 | +0.84 | 42.0 | 0.15 | 50.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| money_level+sharp_gap | moneyline | 1-0 | 100.0 | 71.4 | 28.6 | +0.73 | 73.0 | 2.5 | 100.0 | keep collecting (1/30) |
| money_moving+sharp_gap | moneyline | 1-0 | 100.0 | 71.4 | 28.6 | +0.73 | 73.0 | 2.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+follow_move | moneyline | 1-0 | 100.0 | 71.4 | 28.6 | +0.11 | 11.1 | -2.2 | 0.0 | keep collecting (1/30) |
| follow_move+money_level | moneyline | 1-0 | 100.0 | 71.4 | 28.6 | +0.11 | 11.1 | -2.2 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | moneyline | 1-0 | 100.0 | 71.4 | 28.6 | +0.11 | 11.1 | -2.2 | 0.0 | keep collecting (1/30) |
| follow_move+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | 0.0 | 0.0 | keep collecting (2/30) |
| follow_move+sharp_gap | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.82 | 90.9 | 0.5 | 50.0 | keep collecting (2/30) |
| money_level+sharp_gap | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | 0.5 | 50.0 | keep collecting (2/30) |
| money_level+money_moving | total | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 | 1.0 | 100.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 | 1.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 | 1.0 | 100.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+rlm_ratio | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 | 1.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+sharp_gap | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| rlm_quiet+rlm_ratio | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 | 1.0 | 100.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 | 1.0 | 100.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_ratio+sharp_gap | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 | 1.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 7-10 | 41.2 | 41.9 | -0.7 | -2.48 | -14.6 |  |  | keep collecting (17/30) |
| pin_move | both | 10-10 | 50.0 | 49.7 | 0.3 | -0.59 | -2.9 |  |  | keep collecting (20/30) |
| money_delta | both | 5-7 | 41.7 | 46.7 | -5.0 | -2.37 | -19.7 |  |  | keep collecting (12/30) |
| pin_rlm | both | 1-2 | 33.3 | 50.0 | -16.7 | -1.05 | -34.9 |  |  | keep collecting (3/30) |
| follow_move | both | 18-21 | 46.2 | 48.6 | -2.4 | -5.27 | -13.5 |  |  | no edge shown yet |
| rlm_ratio | both | 2-7 | 22.2 | 37.4 | -15.2 | -5.14 | -57.1 |  |  | keep collecting (9/30) |
| money_level | both | 23-19 | 54.8 | 55.5 | -0.8 | -4.0 | -9.5 |  |  | no edge shown yet |
| sharp_gap | both | 11-22 | 33.3 | 47.3 | -14.0 | -12.96 | -39.3 |  |  | DROP: below break-even |
| money_moving | both | 13-22 | 37.1 | 49.9 | -12.8 | -12.73 | -36.4 |  |  | DROP: below break-even |
| pin_value | both | 8-7 | 53.3 | 49.6 | 3.8 | +2.23 | 14.9 |  |  | keep collecting (15/30) |
| consensus_gap | both | 15-11 | 57.7 | 56.1 | 1.6 | -0.83 | -3.2 |  |  | keep collecting (26/30) |
| follow_move+pin_move | both | 7-10 | 41.2 | 48.9 | -7.8 | -3.38 | -19.9 |  |  | keep collecting (17/30) |
| money_delta+money_moving | both | 4-4 | 50.0 | 45.8 | 4.2 | -0.32 | -4.0 |  |  | keep collecting (8/30) |
| money_delta+sharp_gap | both | 4-3 | 57.1 | 45.2 | 12.0 | +0.68 | 9.7 |  |  | keep collecting (7/30) |
| money_moving+sharp_gap | both | 10-20 | 33.3 | 48.5 | -15.1 | -11.87 | -39.6 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+money_level | both | 10-8 | 55.6 | 61.9 | -6.3 | -2.21 | -12.3 |  |  | keep collecting (18/30) |
| follow_move+rlm_quiet | both | 7-10 | 41.2 | 41.9 | -0.7 | -2.48 | -14.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | both | 3-4 | 42.9 | 41.7 | 1.1 | -0.72 | -10.3 |  |  | keep collecting (7/30) |
| consensus_gap+follow_move | both | 4-5 | 44.4 | 54.8 | -10.3 | -2.35 | -26.1 |  |  | keep collecting (9/30) |
| follow_move+money_level | both | 8-7 | 53.3 | 55.3 | -2.0 | -1.52 | -10.1 |  |  | keep collecting (15/30) |
| money_level+money_moving | both | 10-13 | 43.5 | 53.6 | -10.1 | -6.46 | -28.1 |  |  | keep collecting (23/30) |
| money_level+sharp_gap | both | 8-12 | 40.0 | 52.0 | -12.0 | -5.69 | -28.4 |  |  | keep collecting (20/30) |
| consensus_gap+money_moving | both | 3-8 | 27.3 | 55.3 | -28.0 | -6.04 | -54.9 |  |  | keep collecting (11/30) |
| consensus_gap+pin_move | both | 1-1 | 50.0 | 60.7 | -10.7 | -0.43 | -21.6 |  |  | keep collecting (2/30) |
| consensus_gap+pin_value | both | 6-4 | 60.0 | 50.9 | 9.1 | +1.26 | 12.6 |  |  | keep collecting (10/30) |
| consensus_gap+sharp_gap | both | 2-8 | 20.0 | 51.5 | -31.5 | -6.18 | -61.8 |  |  | keep collecting (10/30) |
| follow_move+money_moving | both | 4-9 | 30.8 | 46.2 | -15.5 | -6.23 | -47.9 |  |  | keep collecting (13/30) |
| follow_move+pin_value | both | 1-2 | 33.3 | 50.0 | -16.7 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| follow_move+sharp_gap | both | 5-10 | 33.3 | 43.9 | -10.5 | -6.32 | -42.1 |  |  | keep collecting (15/30) |
| money_level+pin_move | both | 5-4 | 55.6 | 53.1 | 2.5 | +0.26 | 2.9 |  |  | keep collecting (9/30) |
| money_level+pin_value | both | 2-5 | 28.6 | 50.0 | -21.4 | -3.25 | -46.5 |  |  | keep collecting (7/30) |
| money_moving+pin_move | both | 3-3 | 50.0 | 50.0 | 0.0 | -0.27 | -4.5 |  |  | keep collecting (6/30) |
| money_moving+pin_value | both | 1-6 | 14.3 | 50.0 | -35.7 | -5.09 | -72.7 |  |  | keep collecting (7/30) |
| pin_move+pin_value | both | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-4 | 33.3 | 46.4 | -13.1 | -2.14 | -35.7 |  |  | keep collecting (6/30) |
| pin_value+sharp_gap | both | 1-5 | 16.7 | 50.0 | -33.3 | -4.09 | -68.2 |  |  | keep collecting (6/30) |
| follow_move+money_delta | both | 3-4 | 42.9 | 49.1 | -6.2 | -1.19 | -17.0 |  |  | keep collecting (7/30) |
| money_delta+pin_move | both | 2-1 | 66.7 | 50.0 | 16.7 | +0.9 | 30.1 |  |  | keep collecting (3/30) |
| money_delta+rlm_quiet | both | 2-3 | 40.0 | 50.0 | -10.0 | -1.14 | -22.8 |  |  | keep collecting (5/30) |
| follow_move+rlm_ratio | both | 2-7 | 22.2 | 37.4 | -15.2 | -5.14 | -57.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | both | 1-3 | 25.0 | 39.3 | -14.3 | -2.09 | -52.3 |  |  | keep collecting (4/30) |
| money_moving+rlm_ratio | both | 2-5 | 28.6 | 39.9 | -11.4 | -3.14 | -44.8 |  |  | keep collecting (7/30) |
| rlm_quiet+rlm_ratio | both | 1-5 | 16.7 | 35.7 | -19.0 | -4.09 | -68.2 |  |  | keep collecting (6/30) |
| rlm_quiet+sharp_gap | both | 1-5 | 16.7 | 35.7 | -19.0 | -4.09 | -68.2 |  |  | keep collecting (6/30) |
| rlm_ratio+sharp_gap | both | 2-7 | 22.2 | 37.4 | -15.2 | -5.14 | -57.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | both | 2-0 | 100.0 | 46.9 | 53.1 | +1.86 | 93.0 |  |  | keep collecting (2/30) |
| consensus_gap+rlm_quiet | both | 1-2 | 33.3 | 35.7 | -2.4 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| consensus_gap+rlm_ratio | both | 1-2 | 33.3 | 35.7 | -2.4 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| money_delta+rlm_ratio | both | 2-2 | 50.0 | 48.4 | 1.6 | -0.14 | -3.5 |  |  | keep collecting (4/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 71.4 | -71.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+pin_rlm | both | 1-1 | 50.0 | 60.7 | -10.7 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| money_moving+pin_rlm | both | 1-1 | 50.0 | 60.7 | -10.7 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| pin_rlm+sharp_gap | both | 1-2 | 33.3 | 50.0 | -16.7 | -1.05 | -34.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | both | 1-1 | 50.0 | 39.3 | 10.7 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| consensus_gap+money_delta | both | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+pin_value | both | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| pin_value+rlm_quiet | both | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| pin_value+rlm_ratio | both | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 39.3 | 10.7 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| pin_move+pin_rlm | both | 1-1 | 50.0 | 39.3 | 10.7 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| pin_move+rlm_ratio | both | 1-1 | 50.0 | 39.3 | 10.7 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 39.3 | 10.7 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| money_delta+pin_rlm | both | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 2-5 | 28.6 | 28.6 | 0.0 | -2.08 | -29.7 |  |  | keep collecting (7/30) |
| rlm_quiet | spread | 1-1 | 50.0 | 56.2 | -6.2 | -0.07 | -3.7 |  |  | keep collecting (2/30) |
| rlm_quiet | total | 4-4 | 50.0 | 50.0 | 0.0 | -0.32 | -4.0 |  |  | keep collecting (8/30) |
| pin_move | moneyline | 2-2 | 50.0 | 39.3 | 10.7 | -0.01 | -0.3 |  |  | keep collecting (4/30) |
| pin_move | spread | 3-5 | 37.5 | 54.7 | -17.2 | -2.17 | -27.1 |  |  | keep collecting (8/30) |
| pin_move | total | 5-3 | 62.5 | 50.0 | 12.5 | +1.59 | 19.9 |  |  | keep collecting (8/30) |
| money_delta | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta | spread | 1-2 | 33.3 | 43.8 | -10.4 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| money_delta | total | 4-4 | 50.0 | 50.0 | 0.0 | -0.28 | -3.5 |  |  | keep collecting (8/30) |
| pin_rlm | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 |  |  | keep collecting (1/30) |
| follow_move | moneyline | 7-7 | 50.0 | 43.9 | 6.1 | -1.43 | -10.2 |  |  | keep collecting (14/30) |
| follow_move | spread | 4-7 | 36.4 | 52.8 | -16.5 | -3.29 | -29.9 |  |  | keep collecting (11/30) |
| follow_move | total | 7-7 | 50.0 | 50.0 | 0.0 | -0.55 | -3.9 |  |  | keep collecting (14/30) |
| rlm_ratio | moneyline | 0-5 | 0.0 | 28.6 | -28.6 | -5.0 | -100.0 |  |  | keep collecting (5/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 43.8 | -43.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_ratio | total | 2-1 | 66.7 | 50.0 | 16.7 | +0.86 | 28.7 |  |  | keep collecting (3/30) |
| money_level | moneyline | 9-5 | 64.3 | 68.4 | -4.1 | -2.62 | -18.7 |  |  | keep collecting (14/30) |
| money_level | spread | 6-6 | 50.0 | 47.9 | 2.1 | -0.57 | -4.8 |  |  | keep collecting (12/30) |
| money_level | total | 8-8 | 50.0 | 50.0 | 0.0 | -0.8 | -5.0 |  |  | keep collecting (16/30) |
| sharp_gap | moneyline | 1-10 | 9.1 | 44.2 | -35.1 | -10.0 | -90.9 |  |  | keep collecting (11/30) |
| sharp_gap | spread | 4-8 | 33.3 | 47.9 | -14.6 | -4.46 | -37.2 |  |  | keep collecting (12/30) |
| sharp_gap | total | 6-4 | 60.0 | 50.0 | 10.0 | +1.5 | 15.0 |  |  | keep collecting (10/30) |
| money_moving | moneyline | 3-8 | 27.3 | 51.9 | -24.7 | -7.72 | -70.2 |  |  | keep collecting (11/30) |
| money_moving | spread | 4-8 | 33.3 | 47.9 | -14.6 | -4.46 | -37.2 |  |  | keep collecting (12/30) |
| money_moving | total | 6-6 | 50.0 | 50.0 | 0.0 | -0.54 | -4.5 |  |  | keep collecting (12/30) |
| pin_value | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +3.99 | 199.3 |  |  | keep collecting (2/30) |
| pin_value | spread | 3-2 | 60.0 | 48.8 | 11.2 | +0.56 | 11.1 |  |  | keep collecting (5/30) |
| pin_value | total | 3-5 | 37.5 | 50.0 | -12.5 | -2.31 | -28.9 |  |  | keep collecting (8/30) |
| consensus_gap | moneyline | 7-7 | 50.0 | 62.2 | -12.2 | -3.89 | -27.8 |  |  | keep collecting (14/30) |
| consensus_gap | spread | 3-1 | 75.0 | 46.9 | 28.1 | +1.56 | 38.9 |  |  | keep collecting (4/30) |
| consensus_gap | total | 5-3 | 62.5 | 50.0 | 12.5 | +1.51 | 18.8 |  |  | keep collecting (8/30) |
| consensus_gap+money_level | moneyline | 6-4 | 60.0 | 71.4 | -11.4 | -1.77 | -17.8 |  |  | keep collecting (10/30) |
| follow_move+pin_move | moneyline | 2-2 | 50.0 | 39.3 | 10.7 | -0.01 | -0.3 |  |  | redundant -- identical record to pin_move alone, not independent confirmation |
| follow_move+rlm_quiet | moneyline | 2-5 | 28.6 | 28.6 | 0.0 | -2.08 | -29.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | moneyline | 1-2 | 33.3 | 28.6 | 4.8 | -0.58 | -19.3 |  |  | keep collecting (3/30) |
| consensus_gap+follow_move | moneyline | 3-3 | 50.0 | 57.1 | -7.1 | -1.26 | -21.0 |  |  | keep collecting (6/30) |
| follow_move+money_level | moneyline | 4-2 | 66.7 | 64.3 | 2.4 | -0.25 | -4.2 |  |  | keep collecting (6/30) |
| money_moving+sharp_gap | moneyline | 1-8 | 11.1 | 47.6 | -36.5 | -8.0 | -88.8 |  |  | keep collecting (9/30) |
| follow_move+money_moving | moneyline | 1-3 | 25.0 | 39.3 | -14.3 | -3.0 | -74.9 |  |  | keep collecting (4/30) |
| follow_move+sharp_gap | moneyline | 1-5 | 16.7 | 35.7 | -19.0 | -5.0 | -83.2 |  |  | keep collecting (6/30) |
| money_level+money_moving | moneyline | 3-4 | 42.9 | 65.3 | -22.4 | -3.72 | -53.2 |  |  | keep collecting (7/30) |
| money_level+sharp_gap | moneyline | 1-4 | 20.0 | 62.9 | -42.9 | -4.0 | -79.9 |  |  | keep collecting (5/30) |
| follow_move+rlm_ratio | moneyline | 0-5 | 0.0 | 28.6 | -28.6 | -5.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | moneyline | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_moving+rlm_ratio | moneyline | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| rlm_quiet+rlm_ratio | moneyline | 0-4 | 0.0 | 28.6 | -28.6 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| rlm_quiet+sharp_gap | moneyline | 0-4 | 0.0 | 28.6 | -28.6 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| rlm_ratio+sharp_gap | moneyline | 0-5 | 0.0 | 28.6 | -28.6 | -5.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 1-4 | 20.0 | 62.9 | -42.9 | -3.86 | -77.2 |  |  | keep collecting (5/30) |
| consensus_gap+rlm_quiet | moneyline | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+rlm_ratio | moneyline | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 0-5 | 0.0 | 54.3 | -54.3 | -5.0 | -100.0 |  |  | keep collecting (5/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 71.4 | -71.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 71.4 | -71.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 71.4 | -71.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+sharp_gap | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 1-0 | 100.0 | 71.4 | 28.6 | +0.89 | 88.5 |  |  | keep collecting (1/30) |
| money_level+rlm_ratio | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+pin_move | moneyline | 1-0 | 100.0 | 71.4 | 28.6 | +0.57 | 56.8 |  |  | keep collecting (1/30) |
| money_level+pin_move | moneyline | 1-0 | 100.0 | 71.4 | 28.6 | +0.57 | 56.8 |  |  | keep collecting (1/30) |
| money_delta+money_moving | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| follow_move+pin_rlm | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_move+sharp_gap | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| follow_move+pin_move | spread | 1-5 | 16.7 | 54.2 | -37.5 | -4.09 | -68.2 |  |  | keep collecting (6/30) |
| money_moving+sharp_gap | spread | 4-8 | 33.3 | 47.9 | -14.6 | -4.46 | -37.2 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 1-1 | 50.0 | 56.2 | -6.2 | -0.07 | -3.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | spread | 3-5 | 37.5 | 46.9 | -9.4 | -2.37 | -29.7 |  |  | keep collecting (8/30) |
| money_level+sharp_gap | spread | 3-5 | 37.5 | 46.9 | -9.4 | -2.37 | -29.7 |  |  | keep collecting (8/30) |
| pin_move+rlm_quiet | spread | 0-1 | 0.0 | 56.2 | -56.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+pin_value | spread | 3-1 | 75.0 | 46.9 | 28.1 | +1.56 | 38.9 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| follow_move+money_level | spread | 1-2 | 33.3 | 47.9 | -14.6 | -1.04 | -34.6 |  |  | keep collecting (3/30) |
| follow_move+money_moving | spread | 0-3 | 0.0 | 47.9 | -47.9 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| follow_move+sharp_gap | spread | 0-3 | 0.0 | 47.9 | -47.9 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_level+pin_move | spread | 1-2 | 33.3 | 52.1 | -18.8 | -1.04 | -34.6 |  |  | keep collecting (3/30) |
| money_moving+pin_move | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_move+sharp_gap | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_delta+money_level | spread | 1-0 | 100.0 | 43.8 | 56.2 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 43.8 | 6.2 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_delta+sharp_gap | spread | 1-1 | 50.0 | 43.8 | 6.2 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| consensus_gap+money_level | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | spread | 0-1 | 0.0 | 43.8 | -43.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+sharp_gap | spread | 0-1 | 0.0 | 43.8 | -43.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_moving+pin_value | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_value+sharp_gap | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| follow_move+money_delta | spread | 0-1 | 0.0 | 43.8 | -43.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 43.8 | -43.8 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | spread | 0-1 | 0.0 | 43.8 | -43.8 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 43.8 | -43.8 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 43.8 | -43.8 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_moving | total | 3-2 | 60.0 | 50.0 | 10.0 | +0.77 | 15.4 |  |  | keep collecting (5/30) |
| money_delta+sharp_gap | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.77 | 44.2 |  |  | keep collecting (4/30) |
| money_moving+sharp_gap | total | 5-4 | 55.6 | 50.0 | 5.6 | +0.59 | 6.5 |  |  | keep collecting (9/30) |
| follow_move+rlm_quiet | total | 4-4 | 50.0 | 50.0 | 0.0 | -0.32 | -4.0 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+follow_move | total | 1-2 | 33.3 | 50.0 | -16.7 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| consensus_gap+money_level | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| consensus_gap+money_moving | total | 2-3 | 40.0 | 50.0 | -10.0 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| consensus_gap+pin_move | total | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+pin_value | total | 2-3 | 40.0 | 50.0 | -10.0 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| consensus_gap+sharp_gap | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.18 | -4.5 |  |  | keep collecting (4/30) |
| follow_move+money_level | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.23 | -3.8 |  |  | keep collecting (6/30) |
| follow_move+money_moving | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.23 | -3.8 |  |  | keep collecting (6/30) |
| follow_move+pin_move | total | 4-3 | 57.1 | 50.0 | 7.1 | +0.72 | 10.3 |  |  | keep collecting (7/30) |
| follow_move+pin_value | total | 1-2 | 33.3 | 50.0 | -16.7 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| follow_move+sharp_gap | total | 4-2 | 66.7 | 50.0 | 16.7 | +1.68 | 28.0 |  |  | keep collecting (6/30) |
| money_level+money_moving | total | 4-4 | 50.0 | 50.0 | 0.0 | -0.36 | -4.5 |  |  | keep collecting (8/30) |
| money_level+pin_move | total | 3-2 | 60.0 | 50.0 | 10.0 | +0.73 | 14.6 |  |  | keep collecting (5/30) |
| money_level+pin_value | total | 1-4 | 20.0 | 50.0 | -30.0 | -3.13 | -62.6 |  |  | keep collecting (5/30) |
| money_level+sharp_gap | total | 4-3 | 57.1 | 50.0 | 7.1 | +0.68 | 9.7 |  |  | keep collecting (7/30) |
| money_moving+pin_move | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.73 | 43.3 |  |  | keep collecting (4/30) |
| money_moving+pin_value | total | 1-4 | 20.0 | 50.0 | -30.0 | -3.09 | -61.8 |  |  | keep collecting (5/30) |
| pin_move+pin_value | total | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_move+sharp_gap | total | 2-1 | 66.7 | 50.0 | 16.7 | +0.86 | 28.7 |  |  | keep collecting (3/30) |
| pin_value+sharp_gap | total | 1-3 | 25.0 | 50.0 | -25.0 | -2.09 | -52.3 |  |  | keep collecting (4/30) |
| follow_move+money_delta | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.19 | -3.1 |  |  | keep collecting (6/30) |
| money_delta+pin_move | total | 2-1 | 66.7 | 50.0 | 16.7 | +0.9 | 30.1 |  |  | keep collecting (3/30) |
| money_delta+rlm_quiet | total | 2-3 | 40.0 | 50.0 | -10.0 | -1.14 | -22.8 |  |  | keep collecting (5/30) |
| pin_move+rlm_quiet | total | 2-1 | 66.7 | 50.0 | 16.7 | +0.86 | 28.7 |  |  | keep collecting (3/30) |
| follow_move+rlm_ratio | total | 2-1 | 66.7 | 50.0 | 16.7 | +0.86 | 28.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | total | 2-1 | 66.7 | 50.0 | 16.7 | +0.86 | 28.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_moving+rlm_ratio | total | 2-1 | 66.7 | 50.0 | 16.7 | +0.86 | 28.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| rlm_quiet+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| rlm_ratio+sharp_gap | total | 2-1 | 66.7 | 50.0 | 16.7 | +0.86 | 28.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| consensus_gap+rlm_quiet | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+pin_value | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| pin_value+rlm_quiet | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| pin_value+rlm_ratio | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| follow_move+pin_rlm | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+money_level | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 |  |  | keep collecting (1/30) |
| money_delta+pin_rlm | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 |  |  | keep collecting (1/30) |
| money_moving+pin_rlm | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 |  |  | keep collecting (1/30) |
| pin_rlm+rlm_ratio | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.95 | 95.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |

# FIT (in-sample — this is the hypothesis)

Games before 2026-11-21. The engine was built by looking at these, so a strong record here is expected and proves nothing. n=685 games.

## EARLY  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 31-37 | 45.6 | 35.9 | 9.7 | +10.5 | 15.4 | 0.15 | 42.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move | both | 5-9 | 35.7 | 48.2 | -12.5 | -5.1 | -36.4 | 0.22 | 50.0 | keep collecting (14/30) |
| money_delta | both | 10-7 | 58.8 | 41.8 | 17.0 | +4.43 | 26.1 | -0.22 | 29.4 | keep collecting (17/30) |
| pin_rlm | both | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | both | 475-404 | 54.0 | 52.4 | 1.6 | -45.57 | -5.2 | 0.19 | 41.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | both | 30-18 | 62.5 | 38.5 | 24.0 | +20.45 | 42.6 | 0.37 | 50.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | both | 170-110 | 60.7 | 59.0 | 1.7 | -12.24 | -4.4 | -0.11 | 39.6 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 144-121 | 54.3 | 48.3 | 6.0 | +19.0 | 7.2 | 0.28 | 43.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | both | 102-82 | 55.4 | 51.2 | 4.3 | -0.81 | -0.4 | 0.04 | 41.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | both | 49-48 | 50.5 | 48.3 | 2.2 | -4.43 | -4.6 | 0.1 | 38.1 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.2 | -31.2 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 220-290 | 43.1 | 47.2 | -4.1 | -61.37 | -12.0 | 0.39 | 45.1 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | both | 33-28 | 54.1 | 63.8 | -9.7 | -9.61 | -15.8 | 0.35 | 49.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | both | 17-23 | 42.5 | 46.7 | -4.2 | -6.42 | -16.1 | 0.25 | 42.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_value | both | 19-28 | 40.4 | 46.5 | -6.1 | -11.54 | -24.5 | 0.39 | 48.9 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_quiet | both | 31-37 | 45.6 | 35.9 | 9.7 | +10.5 | 15.4 | 0.15 | 42.6 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 30-18 | 62.5 | 38.5 | 24.0 | +20.45 | 42.6 | 0.37 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 76-38 | 66.7 | 49.9 | 16.8 | +25.22 | 22.1 | 0.35 | 47.4 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 64-40 | 61.5 | 58.1 | 3.4 | -0.87 | -0.8 | -0.16 | 47.1 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 11-9 | 55.0 | 49.8 | 5.2 | +0.81 | 4.0 | 0.4 | 45.0 | keep collecting (20/30) |
| money_moving+pin_value | both | 8-5 | 61.5 | 49.9 | 11.6 | +2.04 | 15.7 | 0.31 | 38.5 | keep collecting (13/30) |
| rlm_quiet+rlm_ratio | both | 17-11 | 60.7 | 35.9 | 24.8 | +14.16 | 50.6 | -0.12 | 46.4 | keep collecting (28/30) |
| rlm_quiet+sharp_gap | both | 19-14 | 57.6 | 35.9 | 21.7 | +12.97 | 39.3 | -0.13 | 45.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | both | 30-18 | 62.5 | 38.5 | 24.0 | +20.45 | 42.6 | 0.37 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 97-60 | 61.8 | 55.7 | 6.1 | +4.17 | 2.7 | 0.14 | 43.3 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 60-48 | 55.6 | 48.6 | 6.9 | +5.0 | 4.6 | 0.18 | 44.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_level | both | 3-2 | 60.0 | 45.8 | 14.2 | +1.46 | 29.2 | 1.16 | 60.0 | keep collecting (5/30) |
| money_delta+money_moving | both | 9-7 | 56.2 | 41.3 | 14.9 | +3.53 | 22.0 | -0.23 | 31.2 | keep collecting (16/30) |
| money_delta+pin_value | both | 3-1 | 75.0 | 50.0 | 25.0 | +1.61 | 40.3 | 0.0 | 25.0 | keep collecting (4/30) |
| money_delta+sharp_gap | both | 7-5 | 58.3 | 40.5 | 17.9 | +3.78 | 31.5 | -0.31 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | both | 13-8 | 61.9 | 48.8 | 13.1 | +3.66 | 17.4 | -0.18 | 33.3 | keep collecting (21/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 32-41 | 43.8 | 51.2 | -7.4 | -15.02 | -20.6 | 0.72 | 54.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_quiet | both | 4-7 | 36.4 | 37.2 | -0.8 | -2.99 | -27.1 | 0.95 | 72.7 | keep collecting (11/30) |
| follow_move+pin_value | both | 20-17 | 54.1 | 48.8 | 5.2 | +0.41 | 1.1 | -0.12 | 29.7 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 42.2 | -25.5 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 26-45 | 36.6 | 45.5 | -8.9 | -10.29 | -14.5 | 0.88 | 49.3 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | both | 91-44 | 67.4 | 60.2 | 7.2 | +1.24 | 0.9 | 0.0 | 43.7 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 11-7 | 61.1 | 41.4 | 19.8 | +4.43 | 24.6 | 1.22 | 61.1 | keep collecting (18/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 44.2 | 5.8 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 53-29 | 64.6 | 52.9 | 11.7 | +9.8 | 12.0 | 0.29 | 51.2 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 3-0 | 100.0 | 49.1 | 50.9 | +2.61 | 87.1 | 0.0 | 0.0 | keep collecting (3/30) |
| follow_move+money_delta | both | 5-3 | 62.5 | 41.1 | 21.4 | +3.95 | 49.4 | 0.05 | 37.5 | keep collecting (8/30) |
| money_delta+rlm_quiet | both | 2-2 | 50.0 | 37.9 | 12.1 | +1.53 | 38.3 | -2.1 | 0.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | both | 11-11 | 50.0 | 36.1 | 13.9 | +3.87 | 17.6 | 0.26 | 40.9 | keep collecting (22/30) |
| money_moving+rlm_ratio | both | 12-8 | 60.0 | 40.7 | 19.3 | +6.66 | 33.3 | 0.16 | 45.0 | keep collecting (20/30) |
| consensus_gap+rlm_ratio | both | 4-4 | 50.0 | 38.5 | 11.5 | +0.09 | 1.1 | 0.69 | 62.5 | keep collecting (8/30) |
| pin_move+pin_value | both | 1-4 | 20.0 | 49.1 | -29.1 | -3.09 | -61.8 | 0.2 | 20.0 | keep collecting (5/30) |
| follow_move+pin_move | both | 5-3 | 62.5 | 52.3 | 10.2 | +0.9 | 11.2 | 0.42 | 62.5 | keep collecting (8/30) |
| consensus_gap+pin_move | both | 0-5 | 0.0 | 44.5 | -44.5 | -5.0 | -100.0 | 0.26 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | both | 2-2 | 50.0 | 55.8 | -5.8 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 26.6 | 23.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 26.6 | 23.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | both | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.2 | -51.2 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-1 | 66.7 | 49.9 | 16.8 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 2-1 | 66.7 | 34.5 | 32.2 | +3.34 | 111.3 | 0.87 | 66.7 | keep collecting (3/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 16-25 | 39.0 | 26.6 | 12.4 | +8.89 | 21.7 | -0.07 | 43.9 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 12-10 | 54.5 | 50.2 | 4.3 | +0.95 | 4.3 | 0.77 | 50.0 | keep collecting (22/30) |
| pin_move | moneyline | 2-3 | 40.0 | 45.3 | -5.3 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-4 | 20.0 | 49.6 | -29.6 | -3.09 | -61.8 | 0.4 | 40.0 | keep collecting (5/30) |
| pin_move | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.14 | -3.5 | 0.25 | 50.0 | keep collecting (4/30) |
| money_delta | moneyline | 2-4 | 33.3 | 26.6 | 6.7 | +0.34 | 5.7 | -1.45 | 33.3 | keep collecting (6/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 7-2 | 77.8 | 50.2 | 27.6 | +4.26 | 47.4 | 0.44 | 22.2 | keep collecting (9/30) |
| pin_rlm | moneyline | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | moneyline | 195-127 | 60.6 | 56.8 | 3.7 | -25.09 | -7.8 | 0.19 | 46.0 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 128-141 | 47.6 | 49.7 | -2.1 | -23.21 | -8.6 | 0.02 | 34.2 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | total | 152-136 | 52.8 | 50.0 | 2.8 | +2.73 | 0.9 | 0.34 | 44.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | moneyline | 13-11 | 54.2 | 26.6 | 27.6 | +11.71 | 48.8 | 0.4 | 58.3 | keep collecting (24/30) |
| rlm_ratio | spread | 3-2 | 60.0 | 51.2 | 8.8 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 14-5 | 73.7 | 50.3 | 23.4 | +7.9 | 41.6 | 0.58 | 52.6 | keep collecting (19/30) |
| money_level | moneyline | 97-39 | 71.3 | 68.9 | 2.4 | -7.41 | -5.4 | -0.24 | 44.9 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-17 | 50.0 | 49.3 | 0.7 | -1.69 | -5.0 | 0.88 | 50.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | total | 56-54 | 50.9 | 49.8 | 1.1 | -3.14 | -2.9 | -0.26 | 30.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 61-62 | 49.6 | 46.4 | 3.2 | +2.59 | 2.1 | 0.32 | 49.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | spread | 20-14 | 58.8 | 49.8 | 9.1 | +4.0 | 11.8 | 0.65 | 38.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 63-45 | 58.3 | 50.1 | 8.3 | +12.4 | 11.5 | 0.12 | 37.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | moneyline | 44-42 | 51.2 | 52.7 | -1.6 | -13.4 | -15.6 | -0.15 | 46.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | spread | 18-5 | 78.3 | 49.2 | 29.1 | +11.18 | 48.6 | 0.3 | 43.5 | keep collecting (23/30) |
| money_moving | total | 40-35 | 53.3 | 50.0 | 3.3 | +1.41 | 1.9 | 0.19 | 36.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | moneyline | 2-6 | 25.0 | 32.4 | -7.4 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| pin_value | spread | 24-20 | 54.5 | 49.5 | 5.0 | +1.16 | 2.6 | 0.25 | 38.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 23-22 | 51.1 | 50.0 | 1.1 | -1.28 | -2.9 | -0.02 | 35.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.0 | -18.7 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 90-164 | 35.4 | 44.8 | -9.4 | -50.5 | -19.9 | 0.15 | 42.5 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 64-61 | 51.2 | 49.2 | 2.0 | -5.08 | -4.1 | 0.34 | 40.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap | total | 66-65 | 50.4 | 50.0 | 0.4 | -5.78 | -4.4 | 0.91 | 55.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | moneyline | 46-19 | 70.8 | 64.0 | 6.7 | -1.1 | -1.7 | 0.04 | 53.8 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+follow_move | moneyline | 11-22 | 33.3 | 53.5 | -20.2 | -14.69 | -44.5 | 0.2 | 54.5 | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 32.4 | -7.4 | -4.31 | -53.8 | -0.08 | 50.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| consensus_gap+rlm_quiet | moneyline | 1-5 | 16.7 | 26.6 | -9.9 | -3.68 | -61.3 | 1.07 | 83.3 | keep collecting (6/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.2 | -8.9 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 16-25 | 39.0 | 26.6 | 12.4 | +8.89 | 21.7 | -0.07 | 43.9 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 30-13 | 69.8 | 70.1 | -0.4 | -4.91 | -11.4 | -0.67 | 51.2 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 26.6 | -26.6 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 15-36 | 29.4 | 44.0 | -14.6 | -11.03 | -21.6 | 0.91 | 51.0 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | moneyline | 58-16 | 78.4 | 69.0 | 9.4 | -0.74 | -1.0 | -0.27 | 45.9 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 28-13 | 68.3 | 56.3 | 12.0 | +2.92 | 7.1 | 0.07 | 53.7 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 24-19 | 55.8 | 70.1 | -14.3 | -8.46 | -19.7 | 0.12 | 48.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+sharp_gap | moneyline | 36-18 | 66.7 | 50.0 | 16.7 | +8.81 | 16.3 | 0.23 | 53.7 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 22-26 | 45.8 | 47.1 | -1.2 | -7.54 | -15.7 | 0.02 | 52.1 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | moneyline | 8-21 | 27.6 | 46.0 | -18.4 | -12.26 | -42.3 | 0.24 | 48.3 | keep collecting (29/30) |
| follow_move+rlm_ratio | moneyline | 13-11 | 54.2 | 26.6 | 27.6 | +11.71 | 48.8 | 0.4 | 58.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 9-8 | 52.9 | 26.6 | 26.4 | +9.84 | 57.9 | -0.25 | 47.1 | keep collecting (17/30) |
| rlm_quiet+sharp_gap | moneyline | 9-11 | 45.0 | 26.6 | 18.4 | +6.84 | 34.2 | -0.41 | 45.0 | keep collecting (20/30) |
| rlm_ratio+sharp_gap | moneyline | 13-11 | 54.2 | 26.6 | 27.6 | +11.71 | 48.8 | 0.4 | 58.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 26.6 | -1.6 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 5-8 | 38.5 | 26.6 | 11.9 | +1.49 | 11.5 | 0.36 | 46.2 | keep collecting (13/30) |
| money_moving+rlm_ratio | moneyline | 4-4 | 50.0 | 26.6 | 23.4 | +3.22 | 40.2 | 0.16 | 50.0 | keep collecting (8/30) |
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
| money_level+rlm_ratio | moneyline | 4-3 | 57.1 | 26.6 | 30.6 | +1.87 | 26.7 | 2.0 | 85.7 | keep collecting (7/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 26.6 | 40.1 | +3.34 | 111.3 | -1.53 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 1-1 | 50.0 | 26.6 | 23.4 | +1.7 | 85.0 | -4.2 | 0.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 26.6 | 73.4 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-0 | 100.0 | 26.6 | 73.4 | +1.64 | 164.0 | 3.8 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 48.0 | -2.5 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 48.0 | 35.4 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 10-8 | 55.6 | 48.9 | 6.7 | +0.6 | 3.3 | 0.5 | 50.0 | keep collecting (18/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.2 | 8.8 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 49.0 | 13.5 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 10-5 | 66.7 | 48.8 | 17.9 | +4.12 | 27.5 | 0.93 | 66.7 | keep collecting (15/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 49.1 | -6.3 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 51.2 | 8.8 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 52.0 | -52.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 52.0 | -52.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-11 | 56.0 | 49.3 | 6.7 | +1.62 | 6.5 | 1.0 | 44.0 | keep collecting (25/30) |
| money_moving+sharp_gap | spread | 10-3 | 76.9 | 49.2 | 27.7 | +6.04 | 46.4 | 0.54 | 46.2 | keep collecting (13/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.3 | 17.3 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-11 | 45.0 | 48.6 | -3.6 | -3.2 | -16.0 | 0.85 | 45.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 48.0 | 14.5 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 11-9 | 55.0 | 48.8 | 6.2 | +1.04 | 5.2 | 0.7 | 45.0 | keep collecting (20/30) |
| follow_move+pin_value | spread | 12-7 | 63.2 | 49.0 | 14.1 | +3.45 | 18.2 | 0.26 | 31.6 | keep collecting (19/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 48.0 | 52.0 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 48.0 | 52.0 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 48.0 | 52.0 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-2 | 81.8 | 48.3 | 33.5 | +6.22 | 56.6 | 0.36 | 45.5 | keep collecting (11/30) |
| money_delta+rlm_quiet | spread | 1-0 | 100.0 | 48.0 | 52.0 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 2-0 | 100.0 | 48.0 | 52.0 | +1.74 | 87.1 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 52.0 | 14.6 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | spread | 1-3 | 25.0 | 49.0 | -24.0 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 48.0 | -48.0 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-2 | 33.3 | 48.0 | -14.6 | -1.09 | -36.4 | 0.33 | 33.3 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.0 | -52.0 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 12-10 | 54.5 | 50.2 | 4.3 | +0.95 | 4.3 | 0.77 | 50.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 24-22 | 52.2 | 49.9 | 2.3 | -0.08 | -0.2 | -0.04 | 37.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | total | 37-30 | 55.2 | 49.9 | 5.3 | +3.65 | 5.4 | -0.09 | 32.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | total | 28-19 | 59.6 | 50.1 | 9.5 | +6.5 | 13.8 | 0.26 | 36.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 8-5 | 61.5 | 50.1 | 11.4 | +2.23 | 17.2 | 0.23 | 30.8 | keep collecting (13/30) |
| money_moving+pin_value | total | 5-3 | 62.5 | 50.1 | 12.4 | +1.47 | 18.3 | 0.12 | 25.0 | keep collecting (8/30) |
| pin_value+sharp_gap | total | 11-6 | 64.7 | 50.1 | 14.6 | +3.92 | 23.1 | -0.06 | 29.4 | keep collecting (17/30) |
| follow_move+money_level | total | 22-19 | 53.7 | 49.8 | 3.8 | +0.94 | 2.3 | 0.15 | 39.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.9 | -3.3 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 14-5 | 73.7 | 50.3 | 23.4 | +7.9 | 41.6 | 0.58 | 52.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 30-14 | 68.2 | 50.0 | 18.1 | +13.33 | 30.3 | 0.41 | 43.2 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 5-3 | 62.5 | 50.3 | 12.2 | +1.63 | 20.4 | 1.0 | 62.5 | keep collecting (8/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 50.1 | 16.5 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 14-5 | 73.7 | 50.3 | 23.4 | +7.9 | 41.6 | 0.58 | 52.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 16-14 | 53.3 | 50.0 | 3.3 | +0.65 | 2.2 | 0.57 | 50.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | total | 4-3 | 57.1 | 49.8 | 7.3 | +0.53 | 7.5 | -0.43 | 14.3 | keep collecting (7/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 49.8 | 30.2 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 49.9 | -16.6 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 6-6 | 50.0 | 50.1 | -0.1 | -0.58 | -4.8 | -0.08 | 25.0 | keep collecting (12/30) |
| money_moving+rlm_ratio | total | 6-4 | 60.0 | 50.2 | 9.8 | +1.58 | 15.8 | 0.4 | 50.0 | keep collecting (10/30) |
| consensus_gap+follow_move | total | 12-8 | 60.0 | 50.0 | 10.0 | +2.88 | 14.4 | 1.45 | 65.0 | keep collecting (20/30) |
| consensus_gap+money_delta | total | 2-0 | 100.0 | 49.6 | 50.4 | +1.78 | 88.9 | 0.0 | 0.0 | keep collecting (2/30) |
| follow_move+money_delta | total | 2-2 | 50.0 | 50.2 | -0.2 | -0.22 | -5.5 | 1.25 | 50.0 | keep collecting (4/30) |
| money_delta+money_moving | total | 6-2 | 75.0 | 50.2 | 24.8 | +3.35 | 41.9 | 0.5 | 25.0 | keep collecting (8/30) |
| money_delta+pin_value | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 | -0.5 | 0.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 5-1 | 83.3 | 50.1 | 33.2 | +3.44 | 57.4 | 0.67 | 33.3 | keep collecting (6/30) |
| money_moving+rlm_quiet | total | 4-3 | 57.1 | 50.3 | 6.9 | +0.64 | 9.1 | 0.43 | 42.9 | keep collecting (7/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 7-2 | 77.8 | 50.3 | 27.5 | +4.41 | 49.0 | 0.44 | 55.6 | keep collecting (9/30) |
| rlm_quiet+sharp_gap | total | 9-2 | 81.8 | 50.3 | 31.5 | +6.22 | 56.6 | 0.64 | 54.5 | keep collecting (11/30) |
| follow_move+pin_move | total | 2-0 | 100.0 | 50.4 | 49.6 | +1.86 | 93.0 | 1.0 | 100.0 | keep collecting (2/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 2-1 | 66.7 | 50.1 | 16.5 | +0.82 | 27.3 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 50.4 | -0.4 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 3-1 | 75.0 | 50.4 | 24.6 | +1.77 | 44.2 | 0.25 | 50.0 | keep collecting (4/30) |
| money_level+pin_move | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_value | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 182-257 | 41.5 | 41.9 | -0.4 | -34.92 | -8.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move | both | 495-494 | 50.1 | 50.0 | 0.1 | -28.51 | -2.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | both | 316-423 | 42.8 | 44.0 | -1.2 | -58.17 | -7.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm | both | 140-157 | 47.1 | 42.2 | 4.9 | +31.28 | 10.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | both | 857-764 | 52.9 | 51.9 | 0.9 | -90.52 | -5.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | both | 200-225 | 47.1 | 44.6 | 2.5 | +1.15 | 0.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level | both | 1084-805 | 57.4 | 55.5 | 1.8 | -66.92 | -3.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 847-976 | 46.5 | 47.5 | -1.0 | -117.8 | -6.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | both | 847-977 | 46.4 | 47.8 | -1.3 | -127.36 | -7.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | both | 351-357 | 49.6 | 47.8 | 1.7 | +3.28 | 0.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 331-449 | 42.4 | 47.1 | -4.6 | -87.77 | -11.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+follow_move | both | 127-127 | 50.0 | 51.2 | -1.2 | -15.22 | -6.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | both | 148-242 | 37.9 | 44.3 | -6.3 | -31.97 | -8.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_move | both | 80-83 | 49.1 | 51.0 | -1.9 | +2.16 | 1.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | both | 23-39 | 37.1 | 37.1 | -0.1 | +10.03 | 16.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_value | both | 132-146 | 47.5 | 45.4 | 2.1 | +3.7 | 1.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | both | 25-43 | 36.8 | 39.6 | -2.9 | -1.66 | -2.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | both | 147-246 | 37.4 | 43.7 | -6.3 | -32.96 | -8.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_moving | both | 457-486 | 48.5 | 49.4 | -0.9 | -66.32 | -7.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_move | both | 355-351 | 50.3 | 50.3 | -0.0 | -29.59 | -4.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_rlm | both | 108-111 | 49.3 | 44.4 | 5.0 | +7.57 | 3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | both | 123-118 | 51.0 | 48.9 | 2.1 | -8.43 | -3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | both | 200-225 | 47.1 | 44.6 | 2.5 | +1.15 | 0.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 462-483 | 48.9 | 49.2 | -0.3 | -56.21 | -5.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_move | both | 298-325 | 47.8 | 48.7 | -0.9 | -22.93 | -3.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_rlm | both | 134-153 | 46.7 | 42.2 | 4.5 | +29.32 | 10.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_value | both | 155-183 | 45.9 | 47.1 | -1.3 | -13.9 | -4.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | both | 192-218 | 46.8 | 44.6 | 2.2 | +0.23 | 0.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+sharp_gap | both | 812-938 | 46.4 | 47.5 | -1.1 | -110.39 | -6.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_rlm | both | 129-130 | 49.8 | 44.3 | 5.5 | +25.5 | 9.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_value | both | 156-155 | 50.2 | 49.0 | 1.1 | -4.95 | -1.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_ratio | both | 116-109 | 51.6 | 45.7 | 5.8 | +16.25 | 7.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | both | 305-325 | 48.4 | 48.6 | -0.2 | -16.69 | -2.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+pin_value | both | 40-41 | 49.4 | 45.6 | 3.8 | +12.58 | 15.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_ratio | both | 108-111 | 49.3 | 44.4 | 5.0 | +7.57 | 3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | both | 140-157 | 47.1 | 42.2 | 4.9 | +31.28 | 10.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 38-31 | 55.1 | 48.6 | 6.4 | +3.73 | 5.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | both | 157-185 | 45.9 | 47.1 | -1.1 | -14.1 | -4.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio+sharp_gap | both | 200-225 | 47.1 | 44.6 | 2.5 | +1.15 | 0.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 151-176 | 46.2 | 46.0 | 0.2 | -22.47 | -6.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+money_moving | both | 597-532 | 52.9 | 52.4 | 0.5 | -46.48 | -4.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | both | 588-522 | 53.0 | 52.2 | 0.8 | -38.02 | -3.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | both | 565-401 | 58.5 | 56.6 | 1.9 | -44.51 | -4.6 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 95-81 | 54.0 | 48.5 | 5.5 | +10.68 | 6.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | both | 203-165 | 55.2 | 57.9 | -2.7 | -22.75 | -6.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | both | 293-268 | 52.2 | 53.1 | -0.9 | -27.8 | -5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | both | 172-158 | 52.1 | 49.8 | 2.3 | -8.55 | -2.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_quiet | both | 19-47 | 28.8 | 36.2 | -7.4 | -9.07 | -13.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_quiet | both | 182-257 | 41.5 | 41.9 | -0.4 | -34.92 | -8.0 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 98-149 | 39.7 | 41.9 | -2.2 | -20.73 | -8.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_moving | both | 226-331 | 40.6 | 42.4 | -1.8 | -49.17 | -8.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_delta | both | 41-110 | 27.2 | 36.6 | -9.4 | -31.68 | -21.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_level | both | 117-111 | 51.3 | 46.9 | 4.4 | +11.59 | 5.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | both | 68-71 | 48.9 | 46.9 | 2.1 | -5.57 | -4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+sharp_gap | both | 223-326 | 40.6 | 42.4 | -1.8 | -47.34 | -8.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 79-122 | 39.3 | 40.4 | -1.1 | -11.64 | -5.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_quiet | both | 90-146 | 38.1 | 41.7 | -3.5 | -23.63 | -10.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+rlm_quiet | both | 49-87 | 36.0 | 42.8 | -6.7 | -30.79 | -22.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+rlm_quiet | both | 87-105 | 45.3 | 44.1 | 1.2 | -4.23 | -2.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_quiet | both | 42-62 | 40.4 | 40.8 | -0.4 | -8.48 | -8.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 118-135 | 46.6 | 46.4 | 0.3 | -5.93 | -2.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_rlm | both | 63-43 | 59.4 | 46.7 | 12.7 | +19.25 | 18.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_rlm | both | 82-94 | 46.6 | 42.2 | 4.4 | +12.43 | 7.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+rlm_ratio | both | 110-116 | 48.7 | 45.0 | 3.6 | -0.1 | -0.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+rlm_quiet | both | 24-35 | 40.7 | 47.2 | -6.5 | -12.58 | -21.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 50.4 | 49.6 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 52-110 | 32.1 | 27.5 | 4.6 | -7.46 | -4.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet | spread | 45-45 | 50.0 | 50.6 | -0.6 | -3.33 | -3.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_quiet | total | 85-102 | 45.5 | 50.2 | -4.7 | -24.13 | -12.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move | moneyline | 103-101 | 50.5 | 49.5 | 0.9 | +6.99 | 3.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move | spread | 194-205 | 48.6 | 50.1 | -1.5 | -28.3 | -7.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move | total | 198-188 | 51.3 | 50.1 | 1.2 | -7.21 | -1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | moneyline | 49-166 | 22.8 | 28.1 | -5.3 | -44.92 | -20.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta | spread | 122-125 | 49.4 | 50.7 | -1.3 | -13.91 | -5.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | total | 145-132 | 52.3 | 50.2 | 2.2 | +0.66 | 0.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm | moneyline | 38-72 | 34.5 | 28.3 | 6.3 | +22.97 | 20.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm | spread | 25-22 | 53.2 | 50.8 | 2.4 | +0.79 | 1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm | total | 77-63 | 55.0 | 50.2 | 4.8 | +7.52 | 5.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | moneyline | 314-205 | 60.5 | 56.5 | 4.0 | -25.77 | -5.0 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 247-262 | 48.5 | 49.6 | -1.1 | -37.75 | -7.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | total | 296-297 | 49.9 | 50.0 | -0.1 | -27.0 | -4.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | moneyline | 37-80 | 31.6 | 29.8 | 1.8 | -2.78 | -2.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio | spread | 41-43 | 48.8 | 50.1 | -1.3 | -5.76 | -6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | total | 122-102 | 54.5 | 50.2 | 4.3 | +9.69 | 4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | moneyline | 417-157 | 72.6 | 69.1 | 3.6 | -22.7 | -4.0 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 316-326 | 49.2 | 49.3 | -0.1 | -41.01 | -6.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level | total | 351-322 | 52.2 | 49.9 | 2.2 | -3.21 | -0.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 201-327 | 38.1 | 41.6 | -3.5 | -55.15 | -10.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| sharp_gap | spread | 324-310 | 51.1 | 49.6 | 1.5 | -17.72 | -2.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 322-339 | 48.7 | 50.1 | -1.4 | -44.93 | -6.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | moneyline | 209-317 | 39.7 | 42.6 | -2.9 | -46.1 | -8.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | spread | 321-313 | 50.6 | 49.6 | 1.0 | -23.6 | -3.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | total | 317-347 | 47.7 | 50.1 | -2.3 | -57.67 | -8.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | moneyline | 18-54 | 25.0 | 30.5 | -5.5 | +10.87 | 15.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | spread | 158-147 | 51.8 | 49.6 | 2.2 | -9.11 | -3.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 175-156 | 52.9 | 49.9 | 2.9 | +1.52 | 0.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.0 | 48.0 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 140-273 | 33.9 | 44.8 | -10.9 | -78.34 | -19.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 86-75 | 53.4 | 49.3 | 4.1 | -1.7 | -1.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap | total | 105-101 | 51.0 | 49.8 | 1.2 | -7.73 | -3.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | moneyline | 145-83 | 63.6 | 63.1 | 0.5 | -6.7 | -2.9 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 136-81 | 62.7 | 62.6 | 0.0 | -6.32 | -2.9 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 187-303 | 38.2 | 41.5 | -3.3 | -42.39 | -8.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+follow_move | moneyline | 52-67 | 43.7 | 53.3 | -9.6 | -20.43 | -17.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 7-36 | 16.3 | 28.8 | -12.5 | -8.64 | -20.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 52-110 | 32.1 | 27.5 | 4.6 | -7.46 | -4.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 95-65 | 59.4 | 69.0 | -9.6 | -16.77 | -10.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 55-154 | 26.3 | 39.8 | -13.5 | -24.75 | -11.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | moneyline | 246-79 | 75.7 | 70.5 | 5.2 | -11.67 | -3.6 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 101-109 | 48.1 | 48.2 | -0.1 | -12.65 | -6.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_moving | moneyline | 46-149 | 23.6 | 27.8 | -4.2 | -30.89 | -15.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+sharp_gap | moneyline | 44-148 | 22.9 | 27.8 | -4.9 | -32.08 | -16.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 53-159 | 25.0 | 38.7 | -13.7 | -27.63 | -13.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+sharp_gap | moneyline | 98-108 | 47.6 | 47.3 | 0.3 | -12.08 | -5.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_quiet | moneyline | 23-67 | 25.6 | 27.6 | -2.1 | -5.91 | -6.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 24-68 | 26.1 | 27.6 | -1.5 | -7.45 | -8.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_move | moneyline | 28-35 | 44.4 | 53.3 | -8.9 | +4.93 | 7.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 10-28 | 26.3 | 29.1 | -2.7 | +9.65 | 25.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 4-30 | 11.8 | 29.3 | -17.6 | -7.04 | -20.7 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 83-67 | 55.3 | 51.6 | 3.8 | +6.35 | 4.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_rlm | moneyline | 24-39 | 38.1 | 29.6 | 8.5 | +2.46 | 3.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 37-80 | 31.6 | 29.8 | 1.8 | -2.78 | -2.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 46-62 | 42.6 | 42.6 | -0.0 | +10.69 | 9.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_rlm | moneyline | 37-70 | 34.6 | 28.3 | 6.2 | +23.57 | 22.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 36-76 | 32.1 | 29.9 | 2.2 | -0.18 | -0.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_rlm | moneyline | 27-45 | 37.5 | 28.5 | 9.0 | +17.19 | 23.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 23-32 | 41.8 | 28.3 | 13.5 | +9.87 | 17.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 21-30 | 41.2 | 30.3 | 10.9 | +8.28 | 16.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+sharp_gap | moneyline | 46-63 | 42.2 | 42.1 | 0.1 | +9.51 | 8.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 14-32 | 30.4 | 28.6 | 1.8 | -4.18 | -9.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 24-39 | 38.1 | 29.6 | 8.5 | +2.46 | 3.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 38-72 | 34.5 | 28.3 | 6.3 | +22.97 | 20.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 23-65 | 26.1 | 27.7 | -1.5 | -5.91 | -6.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 37-80 | 31.6 | 29.8 | 1.8 | -2.78 | -2.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 11-82 | 11.8 | 28.1 | -16.3 | -29.62 | -31.8 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 13-45 | 22.4 | 29.8 | -7.4 | +1.38 | 2.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_move | moneyline | 16-35 | 31.4 | 30.3 | 1.1 | +0.84 | 1.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_rlm | moneyline | 22-44 | 33.3 | 28.7 | 4.6 | +7.63 | 11.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_value | moneyline | 2-18 | 10.0 | 26.6 | -16.6 | -11.18 | -55.9 |  |  | keep collecting (20/30) |
| money_moving+pin_value | moneyline | 10-33 | 23.3 | 29.9 | -6.6 | +8.44 | 19.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_value | moneyline | 6-9 | 40.0 | 32.8 | 7.2 | +7.27 | 48.5 |  |  | keep collecting (15/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 26.6 | 4.7 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 10-35 | 22.2 | 29.7 | -7.5 | +6.44 | 14.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_delta | moneyline | 23-47 | 32.9 | 30.6 | 2.3 | -10.09 | -14.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_level | moneyline | 14-23 | 37.8 | 30.4 | 7.5 | +6.11 | 16.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+rlm_ratio | moneyline | 21-38 | 35.6 | 30.6 | 5.0 | -3.0 | -5.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_move | moneyline | 67-42 | 61.5 | 67.0 | -5.5 | -6.77 | -6.2 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 11-9 | 55.0 | 31.3 | 23.7 | +5.77 | 28.8 |  |  | keep collecting (20/30) |
| money_level+rlm_ratio | moneyline | 13-11 | 54.2 | 38.3 | 15.9 | +6.1 | 25.4 |  |  | keep collecting (24/30) |
| money_delta+rlm_quiet | moneyline | 15-35 | 30.0 | 29.4 | 0.6 | -9.95 | -19.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_value | moneyline | 5-2 | 71.4 | 66.7 | 4.7 | +0.68 | 9.7 |  |  | keep collecting (7/30) |
| follow_move+pin_value | moneyline | 2-7 | 22.2 | 31.8 | -9.6 | -4.79 | -53.3 |  |  | keep collecting (9/30) |
| pin_value+rlm_quiet | moneyline | 1-6 | 14.3 | 26.6 | -12.3 | -4.48 | -64.0 |  |  | keep collecting (7/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 26.6 | -1.6 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 34-27 | 55.7 | 48.7 | 7.0 | +1.9 | 3.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | spread | 48-42 | 53.3 | 49.1 | 4.2 | -1.14 | -1.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_move | spread | 25-27 | 48.1 | 49.2 | -1.1 | -5.73 | -11.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 60-44 | 57.7 | 49.2 | 8.5 | +6.95 | 6.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_ratio | spread | 4-4 | 50.0 | 50.0 | 0.0 | -0.67 | -8.3 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | spread | 47-42 | 52.8 | 49.2 | 3.6 | -2.03 | -2.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | spread | 157-160 | 49.5 | 49.3 | 0.2 | -18.11 | -5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_move | spread | 122-135 | 47.5 | 49.9 | -2.4 | -23.93 | -9.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_rlm | spread | 19-18 | 51.4 | 50.6 | 0.7 | -0.65 | -1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | spread | 56-50 | 52.8 | 49.1 | 3.8 | -1.23 | -1.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | spread | 41-43 | 48.8 | 50.1 | -1.3 | -5.76 | -6.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 158-159 | 49.8 | 49.4 | 0.5 | -15.97 | -5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_move | spread | 117-123 | 48.8 | 49.8 | -1.1 | -17.0 | -7.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | spread | 23-22 | 51.1 | 50.8 | 0.3 | -1.04 | -2.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | spread | 79-79 | 50.0 | 49.3 | 0.7 | -10.83 | -6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_ratio | spread | 39-42 | 48.1 | 50.1 | -1.9 | -6.69 | -8.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | spread | 316-305 | 50.9 | 49.6 | 1.3 | -20.1 | -3.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_rlm | spread | 25-22 | 53.2 | 50.8 | 2.4 | +0.79 | 1.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 73-79 | 48.0 | 49.7 | -1.7 | -14.7 | -9.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_ratio | spread | 22-24 | 47.8 | 50.4 | -2.6 | -3.94 | -8.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | spread | 120-123 | 49.4 | 49.8 | -0.4 | -14.27 | -5.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+pin_value | spread | 7-10 | 41.2 | 50.6 | -9.4 | -3.88 | -22.8 |  |  | keep collecting (17/30) |
| pin_rlm+rlm_ratio | spread | 19-18 | 51.4 | 50.6 | 0.7 | -0.65 | -1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | spread | 25-22 | 53.2 | 50.8 | 2.4 | +0.79 | 1.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 7-7 | 50.0 | 49.4 | 0.6 | -1.01 | -7.2 |  |  | keep collecting (14/30) |
| pin_value+sharp_gap | spread | 79-79 | 50.0 | 49.4 | 0.6 | -10.89 | -6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | spread | 41-43 | 48.8 | 50.1 | -1.3 | -5.76 | -6.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 152-164 | 48.1 | 49.1 | -1.0 | -26.69 | -8.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+rlm_ratio | spread | 21-28 | 42.9 | 49.9 | -7.0 | -9.13 | -18.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | spread | 249-243 | 50.6 | 49.4 | 1.3 | -18.72 | -3.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | spread | 57-46 | 55.3 | 48.9 | 6.4 | +2.72 | 2.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | spread | 248-244 | 50.4 | 49.3 | 1.1 | -20.64 | -4.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | spread | 107-124 | 46.3 | 49.6 | -3.3 | -27.49 | -11.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_value | spread | 86-86 | 50.0 | 49.1 | 0.9 | -11.81 | -6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_delta | spread | 14-14 | 50.0 | 50.4 | -0.4 | -2.09 | -7.5 |  |  | keep collecting (28/30) |
| follow_move+money_delta | spread | 38-47 | 44.7 | 50.2 | -5.5 | -12.62 | -14.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_level | spread | 40-40 | 50.0 | 50.1 | -0.1 | -3.96 | -4.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_moving | spread | 68-74 | 47.9 | 50.4 | -2.5 | -12.64 | -8.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | spread | 32-26 | 55.2 | 50.4 | 4.7 | +1.88 | 3.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+sharp_gap | spread | 67-72 | 48.2 | 50.4 | -2.2 | -11.62 | -8.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_quiet | spread | 45-45 | 50.0 | 50.6 | -0.6 | -3.33 | -3.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 14-4 | 77.8 | 50.7 | 27.1 | +8.78 | 48.8 |  |  | keep collecting (18/30) |
| rlm_quiet+sharp_gap | spread | 21-10 | 67.7 | 50.9 | 16.9 | +9.22 | 29.7 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+pin_rlm | spread | 14-10 | 58.3 | 50.3 | 8.0 | +2.58 | 10.7 |  |  | keep collecting (24/30) |
| money_delta+rlm_ratio | spread | 16-26 | 38.1 | 50.0 | -11.9 | -11.78 | -28.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 52.0 | 48.0 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_move | spread | 36-42 | 46.2 | 50.8 | -4.6 | -9.09 | -11.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_rlm | spread | 13-15 | 46.4 | 50.6 | -4.2 | -3.31 | -11.8 |  |  | keep collecting (28/30) |
| money_delta+rlm_quiet | spread | 14-17 | 45.2 | 51.0 | -5.8 | -4.07 | -13.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_quiet | spread | 20-10 | 66.7 | 50.8 | 15.8 | +8.27 | 27.6 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| pin_move+rlm_quiet | spread | 25-21 | 54.3 | 51.0 | 3.4 | +2.17 | 4.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-2 | 75.0 | 51.5 | 23.5 | +3.56 | 44.5 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_quiet | spread | 2-3 | 40.0 | 50.4 | -10.4 | -1.33 | -26.7 |  |  | keep collecting (5/30) |
| pin_value+rlm_quiet | spread | 4-4 | 50.0 | 49.0 | 1.0 | -0.52 | -6.5 |  |  | keep collecting (8/30) |
| follow_move+money_delta | total | 90-82 | 52.3 | 50.2 | 2.1 | +0.24 | 0.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | total | 204-205 | 49.9 | 50.0 | -0.1 | -19.14 | -4.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | total | 203-198 | 50.6 | 50.0 | 0.6 | -12.98 | -3.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | total | 309-330 | 48.4 | 50.1 | -1.7 | -47.91 | -7.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | total | 51-54 | 48.6 | 49.7 | -1.2 | -8.7 | -8.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_move | total | 27-21 | 56.2 | 49.8 | 6.4 | +2.96 | 6.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_value | total | 59-57 | 50.9 | 49.8 | 1.1 | -4.63 | -4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | total | 199-217 | 47.8 | 50.1 | -2.2 | -35.56 | -8.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+sharp_gap | total | 206-216 | 48.8 | 50.1 | -1.3 | -28.16 | -6.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | total | 119-102 | 53.8 | 50.0 | 3.8 | +6.46 | 2.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | total | 81-70 | 53.6 | 49.8 | 3.8 | +2.58 | 1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_value | total | 77-67 | 53.5 | 50.0 | 3.5 | +2.49 | 1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_quiet | total | 85-102 | 45.5 | 50.2 | -4.7 | -24.13 | -12.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 135-140 | 49.1 | 50.1 | -1.0 | -16.62 | -6.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_quiet+sharp_gap | total | 53-71 | 42.7 | 50.2 | -7.5 | -22.49 | -18.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_moving | total | 112-108 | 50.9 | 50.2 | 0.7 | -5.64 | -2.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | total | 167-158 | 51.4 | 49.9 | 1.4 | -6.16 | -1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 65-61 | 51.6 | 50.0 | 1.6 | -2.4 | -1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | total | 66-71 | 48.2 | 50.0 | -1.8 | -11.51 | -8.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | total | 68-71 | 48.9 | 50.0 | -1.1 | -9.65 | -6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | total | 45-46 | 49.5 | 49.8 | -0.4 | -6.08 | -6.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+sharp_gap | total | 47-45 | 51.1 | 49.8 | 1.2 | -3.3 | -3.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+follow_move | total | 41-33 | 55.4 | 49.8 | 5.6 | +3.3 | 4.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_delta | total | 16-14 | 53.3 | 50.0 | 3.4 | +0.03 | 0.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_quiet | total | 10-8 | 55.6 | 50.0 | 5.5 | +0.9 | 5.0 |  |  | keep collecting (18/30) |
| money_delta+rlm_quiet | total | 20-35 | 36.4 | 50.3 | -13.9 | -16.76 | -30.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+sharp_gap | total | 112-106 | 51.4 | 50.2 | 1.2 | -3.64 | -1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_quiet | total | 47-69 | 40.5 | 50.2 | -9.7 | -25.99 | -22.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 63-48 | 56.8 | 50.2 | 6.6 | +9.44 | 8.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_move | total | 66-58 | 53.2 | 50.2 | 3.0 | +2.32 | 1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | total | 139-139 | 50.0 | 50.1 | -0.1 | -11.93 | -4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_move | total | 150-149 | 50.2 | 50.1 | 0.1 | -12.02 | -4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+rlm_quiet | total | 19-25 | 43.2 | 50.2 | -7.0 | -7.58 | -17.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | total | 10-8 | 55.6 | 50.0 | 5.6 | +0.87 | 4.8 |  |  | keep collecting (18/30) |
| consensus_gap+rlm_ratio | total | 17-9 | 65.4 | 49.9 | 15.5 | +6.04 | 23.2 |  |  | keep collecting (26/30) |
| follow_move+pin_rlm | total | 65-54 | 54.6 | 50.2 | 4.4 | +5.75 | 4.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | total | 122-102 | 54.5 | 50.2 | 4.3 | +9.69 | 4.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 38-24 | 61.3 | 50.2 | 11.0 | +10.91 | 17.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+rlm_ratio | total | 61-42 | 59.2 | 50.2 | 9.1 | +13.72 | 13.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | total | 74-61 | 54.8 | 50.2 | 4.6 | +6.79 | 5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_ratio | total | 117-100 | 53.9 | 50.2 | 3.7 | +7.11 | 3.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_rlm | total | 77-63 | 55.0 | 50.2 | 4.8 | +7.52 | 5.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 73-55 | 57.0 | 50.2 | 6.8 | +11.92 | 9.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+pin_value | total | 28-20 | 58.3 | 50.2 | 8.2 | +5.4 | 11.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_ratio | total | 65-54 | 54.6 | 50.2 | 4.4 | +5.75 | 4.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | total | 77-63 | 55.0 | 50.2 | 4.8 | +7.52 | 5.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 30-21 | 58.8 | 50.2 | 8.7 | +6.22 | 12.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | total | 122-102 | 54.5 | 50.2 | 4.3 | +9.69 | 4.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 47-35 | 57.3 | 50.3 | 7.0 | +8.11 | 9.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+rlm_ratio | total | 73-52 | 58.4 | 50.2 | 8.2 | +14.68 | 11.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | total | 34-27 | 55.7 | 50.1 | 5.6 | +3.73 | 6.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_quiet | total | 39-52 | 42.9 | 50.2 | -7.3 | -16.27 | -17.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_quiet | total | 22-28 | 44.0 | 50.3 | -6.3 | -7.86 | -15.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_quiet+rlm_ratio | total | 42-53 | 44.2 | 50.3 | -6.1 | -14.5 | -15.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 50.4 | 49.6 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

# Pooled (fit + forward together)

Kept for continuity. **Contaminated** — it mixes the games the engine was built
on with the games testing it. Use the forward table for any decision.

## EARLY  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 32-39 | 45.1 | 35.9 | 9.2 | +9.4 | 13.2 | 0.11 | 42.3 | no edge shown yet |
| pin_move | both | 5-9 | 35.7 | 48.2 | -12.5 | -5.1 | -36.4 | 0.22 | 50.0 | keep collecting (14/30) |
| money_delta | both | 10-7 | 58.8 | 41.9 | 17.0 | +4.43 | 26.1 | -0.22 | 29.4 | keep collecting (17/30) |
| pin_rlm | both | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | both | 481-408 | 54.1 | 52.3 | 1.8 | -42.81 | -4.8 | 0.18 | 41.5 | no edge shown yet |
| rlm_ratio | both | 31-19 | 62.0 | 38.6 | 23.4 | +20.35 | 40.7 | 0.37 | 50.0 | no edge shown yet |
| money_level | both | 176-113 | 60.9 | 59.1 | 1.8 | -11.53 | -4.0 | -0.09 | 39.8 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 148-124 | 54.4 | 48.3 | 6.1 | +19.46 | 7.2 | 0.29 | 43.0 | no edge shown yet |
| money_moving | both | 105-84 | 55.6 | 51.4 | 4.2 | -1.06 | -0.6 | 0.05 | 41.8 | no edge shown yet |
| pin_value | both | 49-49 | 50.0 | 48.3 | 1.7 | -5.43 | -5.5 | 0.1 | 37.8 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.3 | -31.3 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 223-291 | 43.4 | 47.4 | -4.0 | -61.39 | -11.9 | 0.4 | 45.3 | DROP: below break-even |
| consensus_gap+money_level | both | 36-29 | 55.4 | 64.4 | -9.0 | -9.63 | -14.8 | 0.4 | 50.8 | no edge shown yet |
| consensus_gap+money_moving | both | 19-23 | 45.2 | 48.0 | -2.8 | -5.58 | -13.3 | 0.25 | 42.9 | no edge shown yet |
| consensus_gap+pin_value | both | 19-28 | 40.4 | 46.5 | -6.1 | -11.54 | -24.5 | 0.39 | 48.9 | DROP: below break-even |
| follow_move+rlm_quiet | both | 32-39 | 45.1 | 35.9 | 9.2 | +9.4 | 13.2 | 0.11 | 42.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 31-19 | 62.0 | 38.6 | 23.4 | +20.35 | 40.7 | 0.37 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 78-39 | 66.7 | 49.7 | 17.0 | +26.04 | 22.3 | 0.35 | 47.0 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 66-41 | 61.7 | 58.3 | 3.4 | -1.03 | -1.0 | -0.15 | 46.7 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 11-9 | 55.0 | 49.8 | 5.2 | +0.81 | 4.0 | 0.4 | 45.0 | keep collecting (20/30) |
| money_moving+pin_value | both | 8-5 | 61.5 | 49.9 | 11.6 | +2.04 | 15.7 | 0.31 | 38.5 | keep collecting (13/30) |
| rlm_quiet+rlm_ratio | both | 18-12 | 60.0 | 36.1 | 23.9 | +14.06 | 46.9 | -0.09 | 46.7 | no edge shown yet |
| rlm_quiet+sharp_gap | both | 20-15 | 57.1 | 36.1 | 21.1 | +12.88 | 36.8 | -0.1 | 45.7 | no edge shown yet |
| rlm_ratio+sharp_gap | both | 31-19 | 62.0 | 38.6 | 23.4 | +20.35 | 40.7 | 0.37 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 99-60 | 62.3 | 55.7 | 6.5 | +5.8 | 3.7 | 0.15 | 43.4 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 62-48 | 56.4 | 48.9 | 7.5 | +6.64 | 6.0 | 0.21 | 45.5 | no edge shown yet |
| money_delta+money_level | both | 3-2 | 60.0 | 45.8 | 14.2 | +1.46 | 29.2 | 1.16 | 60.0 | keep collecting (5/30) |
| money_delta+money_moving | both | 9-7 | 56.2 | 41.3 | 14.9 | +3.53 | 22.0 | -0.23 | 31.2 | keep collecting (16/30) |
| money_delta+pin_value | both | 3-1 | 75.0 | 50.0 | 25.0 | +1.61 | 40.3 | 0.0 | 25.0 | keep collecting (4/30) |
| money_delta+sharp_gap | both | 7-5 | 58.3 | 40.5 | 17.8 | +3.78 | 31.5 | -0.31 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | both | 13-8 | 61.9 | 48.8 | 13.1 | +3.66 | 17.4 | -0.18 | 33.3 | keep collecting (21/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 33-41 | 44.6 | 51.5 | -6.9 | -14.91 | -20.1 | 0.68 | 54.1 | no edge shown yet |
| consensus_gap+rlm_quiet | both | 4-7 | 36.4 | 37.2 | -0.8 | -2.99 | -27.1 | 0.95 | 72.7 | keep collecting (11/30) |
| follow_move+pin_value | both | 20-17 | 54.1 | 48.8 | 5.2 | +0.41 | 1.1 | -0.12 | 29.7 | no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 42.2 | -25.5 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 27-45 | 37.5 | 45.9 | -8.4 | -9.56 | -13.3 | 0.9 | 50.0 | DROP: below break-even |
| follow_move+money_level | both | 93-45 | 67.4 | 60.1 | 7.3 | +1.26 | 0.9 | -0.01 | 42.8 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 11-7 | 61.1 | 41.4 | 19.7 | +4.43 | 24.6 | 1.22 | 61.1 | keep collecting (18/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 44.2 | 5.8 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 55-30 | 64.7 | 53.1 | 11.6 | +9.82 | 11.6 | 0.27 | 50.6 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 3-0 | 100.0 | 49.0 | 51.0 | +2.61 | 87.1 | 0.0 | 0.0 | keep collecting (3/30) |
| follow_move+money_delta | both | 5-3 | 62.5 | 41.1 | 21.4 | +3.95 | 49.4 | 0.05 | 37.5 | keep collecting (8/30) |
| money_delta+rlm_quiet | both | 2-2 | 50.0 | 37.9 | 12.1 | +1.53 | 38.3 | -2.1 | 0.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | both | 12-11 | 52.2 | 36.7 | 15.5 | +4.78 | 20.8 | 0.29 | 43.5 | keep collecting (23/30) |
| money_moving+rlm_ratio | both | 13-8 | 61.9 | 41.2 | 20.7 | +7.57 | 36.1 | 0.2 | 47.6 | keep collecting (21/30) |
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
| book_lag+pin_value | both | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-1 | 66.7 | 49.9 | 16.8 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 2-1 | 66.7 | 34.5 | 32.1 | +3.34 | 111.3 | 0.87 | 66.7 | keep collecting (3/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 16-27 | 37.2 | 26.6 | 10.6 | +6.89 | 16.0 | -0.14 | 41.9 | DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 13-10 | 56.5 | 50.2 | 6.3 | +1.86 | 8.1 | 0.78 | 52.2 | keep collecting (23/30) |
| pin_move | moneyline | 2-3 | 40.0 | 45.3 | -5.3 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-4 | 20.0 | 49.6 | -29.6 | -3.09 | -61.8 | 0.4 | 40.0 | keep collecting (5/30) |
| pin_move | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.14 | -3.5 | 0.25 | 50.0 | keep collecting (4/30) |
| money_delta | moneyline | 2-4 | 33.3 | 26.6 | 6.7 | +0.34 | 5.7 | -1.45 | 33.3 | keep collecting (6/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 7-2 | 77.8 | 50.2 | 27.6 | +4.26 | 47.4 | 0.44 | 22.2 | keep collecting (9/30) |
| pin_rlm | moneyline | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | moneyline | 198-129 | 60.6 | 56.5 | 4.0 | -23.06 | -7.1 | 0.16 | 45.3 | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 129-142 | 47.6 | 49.7 | -2.1 | -23.3 | -8.6 | 0.02 | 33.9 | DROP: below break-even |
| follow_move | total | 154-137 | 52.9 | 50.0 | 2.9 | +3.55 | 1.2 | 0.34 | 44.3 | no edge shown yet |
| rlm_ratio | moneyline | 13-12 | 52.0 | 26.6 | 25.4 | +10.71 | 42.8 | 0.38 | 56.0 | keep collecting (25/30) |
| rlm_ratio | spread | 3-2 | 60.0 | 51.3 | 8.7 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 15-5 | 75.0 | 50.3 | 24.7 | +8.81 | 44.0 | 0.6 | 55.0 | keep collecting (20/30) |
| money_level | moneyline | 100-40 | 71.4 | 69.0 | 2.4 | -7.43 | -5.3 | -0.2 | 45.7 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-17 | 50.0 | 49.2 | 0.8 | -1.69 | -5.0 | 0.88 | 50.0 | no edge shown yet |
| money_level | total | 59-56 | 51.3 | 49.8 | 1.5 | -2.41 | -2.1 | -0.24 | 29.6 | no edge shown yet |
| sharp_gap | moneyline | 62-64 | 49.2 | 46.3 | 2.9 | +1.32 | 1.0 | 0.34 | 50.0 | no edge shown yet |
| sharp_gap | spread | 20-14 | 58.8 | 49.7 | 9.1 | +4.0 | 11.8 | 0.65 | 38.2 | no edge shown yet |
| sharp_gap | total | 66-46 | 58.9 | 50.1 | 8.9 | +14.13 | 12.6 | 0.12 | 36.6 | no edge shown yet |
| money_moving | moneyline | 46-42 | 52.3 | 53.2 | -0.9 | -12.56 | -14.3 | -0.14 | 46.6 | no edge shown yet |
| money_moving | spread | 18-5 | 78.3 | 49.2 | 29.1 | +11.18 | 48.6 | 0.3 | 43.5 | keep collecting (23/30) |
| money_moving | total | 41-37 | 52.6 | 50.0 | 2.6 | +0.32 | 0.4 | 0.19 | 35.9 | no edge shown yet |
| pin_value | moneyline | 2-6 | 25.0 | 32.5 | -7.5 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| pin_value | spread | 24-21 | 53.3 | 49.5 | 3.9 | +0.16 | 0.3 | 0.24 | 37.8 | no edge shown yet |
| pin_value | total | 23-22 | 51.1 | 50.0 | 1.1 | -1.28 | -2.9 | -0.02 | 35.6 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.1 | -18.8 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 93-165 | 36.0 | 45.3 | -9.2 | -50.52 | -19.6 | 0.17 | 43.0 | DROP: below break-even |
| consensus_gap | spread | 64-61 | 51.2 | 49.2 | 2.0 | -5.08 | -4.1 | 0.34 | 40.0 | no edge shown yet |
| consensus_gap | total | 66-65 | 50.4 | 50.0 | 0.4 | -5.78 | -4.4 | 0.91 | 55.0 | no edge shown yet |
| money_level+sharp_gap | moneyline | 47-19 | 71.2 | 64.2 | 7.1 | -0.37 | -0.6 | 0.08 | 54.5 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+follow_move | moneyline | 12-22 | 35.3 | 54.1 | -18.8 | -14.58 | -42.9 | 0.13 | 52.9 | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 32.5 | -7.5 | -4.31 | -53.8 | -0.08 | 50.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| consensus_gap+rlm_quiet | moneyline | 1-5 | 16.7 | 26.6 | -10.0 | -3.68 | -61.3 | 1.07 | 83.3 | keep collecting (6/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.2 | -8.9 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 16-27 | 37.2 | 26.6 | 10.6 | +6.89 | 16.0 | -0.14 | 41.9 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 32-13 | 71.1 | 70.3 | 0.9 | -4.07 | -9.0 | -0.63 | 51.1 | beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 26.6 | -26.6 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 16-36 | 30.8 | 44.6 | -13.8 | -10.3 | -19.8 | 0.94 | 51.9 | DROP: below break-even |
| follow_move+money_level | moneyline | 59-16 | 78.7 | 69.0 | 9.7 | -0.63 | -0.8 | -0.29 | 45.3 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 29-13 | 69.0 | 56.7 | 12.4 | +3.04 | 7.2 | 0.01 | 52.4 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 27-20 | 57.4 | 70.4 | -12.9 | -8.47 | -18.0 | 0.21 | 51.1 | no edge shown yet |
| follow_move+sharp_gap | moneyline | 36-19 | 65.5 | 49.6 | 15.9 | +7.81 | 14.2 | 0.22 | 52.7 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 23-26 | 46.9 | 47.6 | -0.7 | -6.8 | -13.9 | 0.07 | 53.1 | no edge shown yet |
| consensus_gap+money_moving | moneyline | 10-21 | 32.3 | 47.7 | -15.5 | -11.42 | -36.9 | 0.24 | 48.4 | INVERT candidate: wrong well beyond its base rate |
| follow_move+rlm_ratio | moneyline | 13-12 | 52.0 | 26.6 | 25.4 | +10.71 | 42.8 | 0.38 | 56.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 9-9 | 50.0 | 26.6 | 23.4 | +8.84 | 49.1 | -0.26 | 44.4 | keep collecting (18/30) |
| rlm_quiet+sharp_gap | moneyline | 9-12 | 42.9 | 26.6 | 16.2 | +5.84 | 27.8 | -0.4 | 42.9 | keep collecting (21/30) |
| rlm_ratio+sharp_gap | moneyline | 13-12 | 52.0 | 26.6 | 25.4 | +10.71 | 42.8 | 0.38 | 56.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 26.6 | -1.6 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 5-8 | 38.5 | 26.6 | 11.8 | +1.49 | 11.5 | 0.36 | 46.2 | keep collecting (13/30) |
| money_moving+rlm_ratio | moneyline | 4-4 | 50.0 | 26.6 | 23.4 | +3.22 | 40.2 | 0.16 | 50.0 | keep collecting (8/30) |
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
| consensus_gap+pin_value | spread | 10-8 | 55.6 | 48.8 | 6.7 | +0.6 | 3.3 | 0.5 | 50.0 | keep collecting (18/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.3 | 8.7 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 48.9 | 13.6 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 10-5 | 66.7 | 48.7 | 18.0 | +4.12 | 27.5 | 0.93 | 66.7 | keep collecting (15/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 49.1 | -6.2 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
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
| follow_move+money_moving | spread | 9-2 | 81.8 | 48.2 | 33.6 | +6.22 | 56.6 | 0.36 | 45.5 | keep collecting (11/30) |
| money_delta+rlm_quiet | spread | 1-0 | 100.0 | 47.9 | 52.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 2-0 | 100.0 | 47.9 | 52.1 | +1.74 | 87.1 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 52.1 | 14.5 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | spread | 1-3 | 25.0 | 48.9 | -23.9 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 47.9 | -47.9 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-2 | 33.3 | 47.9 | -14.5 | -1.09 | -36.4 | 0.33 | 33.3 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.1 | -52.1 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 13-10 | 56.5 | 50.2 | 6.3 | +1.86 | 8.1 | 0.78 | 52.2 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 24-23 | 51.1 | 49.9 | 1.2 | -1.08 | -2.3 | -0.04 | 36.2 | no edge shown yet |
| money_level+sharp_gap | total | 38-30 | 55.9 | 49.9 | 5.9 | +4.55 | 6.7 | -0.09 | 32.4 | no edge shown yet |
| money_moving+sharp_gap | total | 29-19 | 60.4 | 50.1 | 10.3 | +7.41 | 15.4 | 0.27 | 37.5 | no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 8-5 | 61.5 | 50.1 | 11.4 | +2.23 | 17.2 | 0.23 | 30.8 | keep collecting (13/30) |
| money_moving+pin_value | total | 5-3 | 62.5 | 50.1 | 12.4 | +1.47 | 18.3 | 0.12 | 25.0 | keep collecting (8/30) |
| pin_value+sharp_gap | total | 11-6 | 64.7 | 50.1 | 14.6 | +3.92 | 23.1 | -0.06 | 29.4 | keep collecting (17/30) |
| follow_move+money_level | total | 23-20 | 53.5 | 49.8 | 3.6 | +0.85 | 2.0 | 0.14 | 37.2 | no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.9 | -3.3 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 15-5 | 75.0 | 50.3 | 24.7 | +8.81 | 44.0 | 0.6 | 55.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 32-14 | 69.6 | 50.0 | 19.5 | +15.14 | 32.9 | 0.41 | 43.5 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 5-3 | 62.5 | 50.3 | 12.2 | +1.63 | 20.4 | 1.0 | 62.5 | keep collecting (8/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 50.1 | 16.5 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 15-5 | 75.0 | 50.3 | 24.7 | +8.81 | 44.0 | 0.6 | 55.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 17-15 | 53.1 | 50.0 | 3.1 | +0.56 | 1.8 | 0.56 | 50.0 | no edge shown yet |
| consensus_gap+money_level | total | 4-3 | 57.1 | 49.8 | 7.3 | +0.53 | 7.5 | -0.43 | 14.3 | keep collecting (7/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 49.8 | 30.2 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 49.9 | -16.6 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 6-6 | 50.0 | 50.1 | -0.1 | -0.58 | -4.8 | -0.08 | 25.0 | keep collecting (12/30) |
| money_moving+rlm_ratio | total | 7-4 | 63.6 | 50.2 | 13.4 | +2.49 | 22.7 | 0.45 | 54.5 | keep collecting (11/30) |
| consensus_gap+follow_move | total | 12-8 | 60.0 | 50.0 | 10.0 | +2.88 | 14.4 | 1.45 | 65.0 | keep collecting (20/30) |
| consensus_gap+money_delta | total | 2-0 | 100.0 | 49.6 | 50.4 | +1.78 | 88.9 | 0.0 | 0.0 | keep collecting (2/30) |
| follow_move+money_delta | total | 2-2 | 50.0 | 50.2 | -0.2 | -0.22 | -5.5 | 1.25 | 50.0 | keep collecting (4/30) |
| money_delta+money_moving | total | 6-2 | 75.0 | 50.2 | 24.8 | +3.35 | 41.9 | 0.5 | 25.0 | keep collecting (8/30) |
| money_delta+pin_value | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 | -0.5 | 0.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 5-1 | 83.3 | 50.1 | 33.2 | +3.44 | 57.4 | 0.67 | 33.3 | keep collecting (6/30) |
| money_moving+rlm_quiet | total | 5-3 | 62.5 | 50.3 | 12.2 | +1.55 | 19.3 | 0.5 | 50.0 | keep collecting (8/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 8-2 | 80.0 | 50.3 | 29.7 | +5.31 | 53.1 | 0.5 | 60.0 | keep collecting (10/30) |
| rlm_quiet+sharp_gap | total | 10-2 | 83.3 | 50.3 | 33.0 | +7.13 | 59.4 | 0.67 | 58.3 | keep collecting (12/30) |
| follow_move+pin_move | total | 2-0 | 100.0 | 50.4 | 49.6 | +1.86 | 93.0 | 1.0 | 100.0 | keep collecting (2/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 2-1 | 66.7 | 50.1 | 16.5 | +0.82 | 27.3 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 50.4 | -0.4 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 3-1 | 75.0 | 50.4 | 24.6 | +1.77 | 44.2 | 0.25 | 50.0 | keep collecting (4/30) |
| money_level+pin_move | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_value | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 189-267 | 41.4 | 41.9 | -0.4 | -37.39 | -8.2 |  |  | DROP: below break-even |
| pin_move | both | 505-504 | 50.0 | 50.0 | 0.1 | -29.1 | -2.9 |  |  | no edge shown yet |
| money_delta | both | 321-430 | 42.7 | 44.0 | -1.3 | -60.54 | -8.1 |  |  | DROP: below break-even |
| pin_rlm | both | 141-159 | 47.0 | 42.3 | 4.7 | +30.24 | 10.1 |  |  | DROP: below break-even |
| follow_move | both | 875-785 | 52.7 | 51.8 | 0.9 | -95.79 | -5.8 |  |  | no edge shown yet |
| rlm_ratio | both | 202-232 | 46.5 | 44.4 | 2.1 | -3.99 | -0.9 |  |  | DROP: below break-even |
| money_level | both | 1107-824 | 57.3 | 55.5 | 1.8 | -70.92 | -3.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 858-998 | 46.2 | 47.5 | -1.2 | -130.77 | -7.0 |  |  | DROP: below break-even |
| money_moving | both | 860-999 | 46.3 | 47.8 | -1.5 | -140.09 | -7.5 |  |  | DROP: below break-even |
| pin_value | both | 359-364 | 49.7 | 47.9 | 1.8 | +5.51 | 0.8 |  |  | no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 346-460 | 42.9 | 47.4 | -4.5 | -88.6 | -11.0 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 131-132 | 49.8 | 51.3 | -1.5 | -17.57 | -6.7 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 151-250 | 37.7 | 44.6 | -7.0 | -38.01 | -9.5 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 81-84 | 49.1 | 51.1 | -2.0 | +1.73 | 1.1 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 23-40 | 36.5 | 37.7 | -1.2 | +9.03 | 14.3 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 138-150 | 47.9 | 45.6 | 2.3 | +4.96 | 1.7 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | both | 26-45 | 36.6 | 39.4 | -2.8 | -2.75 | -3.9 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 149-254 | 37.0 | 43.9 | -7.0 | -39.14 | -9.7 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 461-495 | 48.2 | 49.4 | -1.1 | -72.55 | -7.6 |  |  | DROP: below break-even |
| follow_move+pin_move | both | 362-361 | 50.1 | 50.3 | -0.2 | -32.97 | -4.6 |  |  | no edge shown yet |
| follow_move+pin_rlm | both | 109-112 | 49.3 | 44.3 | 5.0 | +7.52 | 3.4 |  |  | no edge shown yet |
| follow_move+pin_value | both | 124-120 | 50.8 | 48.9 | 1.9 | -9.52 | -3.9 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 202-232 | 46.5 | 44.4 | 2.1 | -3.99 | -0.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 467-493 | 48.6 | 49.1 | -0.5 | -62.52 | -6.5 |  |  | DROP: below break-even |
| money_moving+pin_move | both | 301-328 | 47.9 | 48.7 | -0.9 | -23.2 | -3.7 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 135-154 | 46.7 | 42.3 | 4.4 | +29.27 | 10.1 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 156-189 | 45.2 | 47.2 | -1.9 | -18.99 | -5.5 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 194-223 | 46.5 | 44.6 | 2.0 | -2.9 | -0.7 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 822-958 | 46.2 | 47.5 | -1.4 | -122.26 | -6.9 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 130-131 | 49.8 | 44.3 | 5.5 | +25.45 | 9.8 |  |  | no edge shown yet |
| pin_move+pin_value | both | 156-156 | 50.0 | 49.0 | 1.0 | -5.95 | -1.9 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 117-110 | 51.5 | 45.7 | 5.9 | +16.2 | 7.1 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 307-329 | 48.3 | 48.6 | -0.3 | -18.83 | -3.0 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 40-41 | 49.4 | 45.6 | 3.8 | +12.58 | 15.5 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 109-112 | 49.3 | 44.3 | 5.0 | +7.52 | 3.4 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 141-159 | 47.0 | 42.3 | 4.7 | +30.24 | 10.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 39-31 | 55.7 | 48.7 | 7.1 | +4.64 | 6.6 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 158-190 | 45.4 | 47.1 | -1.7 | -18.19 | -5.2 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 202-232 | 46.5 | 44.4 | 2.1 | -3.99 | -0.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 154-180 | 46.1 | 46.1 | 0.0 | -23.65 | -7.1 |  |  | DROP: below break-even |
| money_level+money_moving | both | 607-545 | 52.7 | 52.4 | 0.3 | -52.94 | -4.6 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 596-534 | 52.7 | 52.2 | 0.6 | -43.71 | -3.9 |  |  | no edge shown yet |
| follow_move+money_level | both | 573-408 | 58.4 | 56.6 | 1.8 | -46.03 | -4.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 96-82 | 53.9 | 48.3 | 5.6 | +10.64 | 6.0 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 213-173 | 55.2 | 58.1 | -2.9 | -24.96 | -6.5 |  |  | no edge shown yet |
| money_level+pin_move | both | 298-272 | 52.3 | 53.1 | -0.8 | -27.54 | -4.8 |  |  | no edge shown yet |
| money_level+pin_value | both | 174-163 | 51.6 | 49.8 | 1.8 | -11.8 | -3.5 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 20-49 | 29.0 | 36.2 | -7.2 | -10.16 | -14.7 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | both | 189-267 | 41.4 | 41.9 | -0.4 | -37.39 | -8.2 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 99-154 | 39.1 | 41.7 | -2.6 | -24.82 | -9.8 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 230-335 | 40.7 | 42.5 | -1.8 | -49.49 | -8.8 |  |  | DROP: below break-even |
| consensus_gap+money_delta | both | 42-110 | 27.6 | 36.7 | -9.1 | -30.77 | -20.2 |  |  | DROP: below break-even |
| money_delta+money_level | both | 119-111 | 51.7 | 46.9 | 4.8 | +13.45 | 5.8 |  |  | no edge shown yet |
| money_delta+pin_value | both | 69-71 | 49.3 | 46.9 | 2.4 | -4.66 | -3.3 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 227-329 | 40.8 | 42.5 | -1.7 | -46.66 | -8.4 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 80-127 | 38.6 | 40.3 | -1.6 | -15.73 | -7.6 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | both | 91-149 | 37.9 | 41.6 | -3.7 | -25.72 | -10.7 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 51-90 | 36.2 | 43.1 | -6.9 | -31.93 | -22.6 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | both | 90-109 | 45.2 | 44.0 | 1.2 | -4.95 | -2.5 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 42-63 | 40.0 | 40.7 | -0.7 | -9.48 | -9.0 |  |  | DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 120-136 | 46.9 | 46.4 | 0.4 | -5.03 | -2.0 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 64-44 | 59.3 | 47.0 | 12.3 | +19.2 | 17.8 |  |  | no edge shown yet |
| money_delta+pin_rlm | both | 83-94 | 46.9 | 42.3 | 4.6 | +13.39 | 7.6 |  |  | no edge shown yet |
| money_delta+rlm_ratio | both | 112-118 | 48.7 | 45.1 | 3.6 | -0.24 | -0.1 |  |  | no edge shown yet |
| pin_value+rlm_quiet | both | 25-35 | 41.7 | 47.3 | -5.6 | -11.67 | -19.4 |  |  | DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 50.4 | 49.6 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 54-115 | 32.0 | 27.5 | 4.5 | -9.54 | -5.6 |  |  | DROP: below break-even |
| rlm_quiet | spread | 46-46 | 50.0 | 50.7 | -0.7 | -3.4 | -3.7 |  |  | no edge shown yet |
| rlm_quiet | total | 89-106 | 45.6 | 50.2 | -4.5 | -24.45 | -12.5 |  |  | DROP: below break-even |
| pin_move | moneyline | 105-103 | 50.5 | 49.3 | 1.2 | +6.98 | 3.4 |  |  | no edge shown yet |
| pin_move | spread | 197-210 | 48.4 | 50.2 | -1.8 | -30.46 | -7.5 |  |  | DROP: below break-even |
| pin_move | total | 203-191 | 51.5 | 50.1 | 1.4 | -5.62 | -1.4 |  |  | no edge shown yet |
| money_delta | moneyline | 49-167 | 22.7 | 28.1 | -5.5 | -45.92 | -21.3 |  |  | DROP: below break-even |
| money_delta | spread | 123-127 | 49.2 | 50.7 | -1.5 | -15.0 | -6.0 |  |  | no edge shown yet |
| money_delta | total | 149-136 | 52.3 | 50.2 | 2.1 | +0.38 | 0.1 |  |  | no edge shown yet |
| pin_rlm | moneyline | 38-74 | 33.9 | 28.7 | 5.2 | +20.97 | 18.7 |  |  | DROP: below break-even |
| pin_rlm | spread | 25-22 | 53.2 | 50.9 | 2.3 | +0.79 | 1.7 |  |  | no edge shown yet |
| pin_rlm | total | 78-63 | 55.3 | 50.2 | 5.1 | +8.47 | 6.0 |  |  | no edge shown yet |
| follow_move | moneyline | 321-212 | 60.2 | 56.1 | 4.1 | -27.19 | -5.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 251-269 | 48.3 | 49.6 | -1.3 | -41.04 | -7.9 |  |  | DROP: below break-even |
| follow_move | total | 303-304 | 49.9 | 50.0 | -0.1 | -27.55 | -4.5 |  |  | no edge shown yet |
| rlm_ratio | moneyline | 37-85 | 30.3 | 29.7 | 0.6 | -7.78 | -6.4 |  |  | DROP: below break-even |
| rlm_ratio | spread | 41-44 | 48.2 | 50.1 | -1.9 | -6.76 | -8.0 |  |  | no edge shown yet |
| rlm_ratio | total | 124-103 | 54.6 | 50.2 | 4.4 | +10.55 | 4.6 |  |  | no edge shown yet |
| money_level | moneyline | 426-162 | 72.4 | 69.1 | 3.4 | -25.33 | -4.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 322-332 | 49.2 | 49.3 | -0.1 | -41.59 | -6.4 |  |  | DROP: below break-even |
| money_level | total | 359-330 | 52.1 | 49.9 | 2.2 | -4.01 | -0.6 |  |  | no edge shown yet |
| sharp_gap | moneyline | 202-337 | 37.5 | 41.6 | -4.2 | -65.14 | -12.1 |  |  | DROP: below break-even |
| sharp_gap | spread | 328-318 | 50.8 | 49.6 | 1.2 | -22.19 | -3.4 |  |  | no edge shown yet |
| sharp_gap | total | 328-343 | 48.9 | 50.1 | -1.2 | -43.43 | -6.5 |  |  | DROP: below break-even |
| money_moving | moneyline | 212-325 | 39.5 | 42.8 | -3.3 | -53.83 | -10.0 |  |  | DROP: below break-even |
| money_moving | spread | 325-321 | 50.3 | 49.6 | 0.7 | -28.06 | -4.3 |  |  | no edge shown yet |
| money_moving | total | 323-353 | 47.8 | 50.1 | -2.3 | -58.21 | -8.6 |  |  | DROP: below break-even |
| pin_value | moneyline | 20-54 | 27.0 | 31.1 | -4.0 | +14.86 | 20.1 |  |  | DROP: below break-even |
| pin_value | spread | 161-149 | 51.9 | 49.6 | 2.3 | -8.55 | -2.8 |  |  | no edge shown yet |
| pin_value | total | 178-161 | 52.5 | 49.9 | 2.6 | -0.79 | -0.2 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.1 | 47.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 147-280 | 34.4 | 45.5 | -11.0 | -82.23 | -19.3 |  |  | DROP: below break-even |
| consensus_gap | spread | 89-76 | 53.9 | 49.2 | 4.7 | -0.14 | -0.1 |  |  | no edge shown yet |
| consensus_gap | total | 110-104 | 51.4 | 49.8 | 1.6 | -6.22 | -2.9 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 148-87 | 63.0 | 63.2 | -0.2 | -10.43 | -4.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 137-85 | 61.7 | 62.6 | -0.9 | -10.31 | -4.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 188-311 | 37.7 | 41.6 | -3.9 | -50.38 | -10.1 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 55-70 | 44.0 | 53.6 | -9.6 | -21.69 | -17.3 |  |  | DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 7-38 | 15.6 | 28.7 | -13.2 | -10.64 | -23.6 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 54-115 | 32.0 | 27.5 | 4.5 | -9.54 | -5.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 101-69 | 59.4 | 69.2 | -9.8 | -18.55 | -10.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 56-158 | 26.2 | 40.4 | -14.2 | -28.61 | -13.4 |  |  | DROP: below break-even |
| follow_move+money_level | moneyline | 250-81 | 75.5 | 70.4 | 5.1 | -11.92 | -3.6 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 102-112 | 47.7 | 48.0 | -0.4 | -15.65 | -7.3 |  |  | no edge shown yet |
| money_delta+money_moving | moneyline | 46-150 | 23.5 | 27.8 | -4.4 | -31.89 | -16.3 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 44-149 | 22.8 | 27.8 | -5.0 | -33.08 | -17.1 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 53-164 | 24.4 | 39.1 | -14.7 | -32.63 | -15.0 |  |  | DROP: below break-even |
| follow_move+sharp_gap | moneyline | 99-113 | 46.7 | 46.9 | -0.2 | -17.07 | -8.1 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | moneyline | 23-69 | 25.0 | 27.6 | -2.6 | -7.91 | -8.6 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 24-72 | 25.0 | 27.6 | -2.6 | -11.45 | -11.9 |  |  | DROP: below break-even |
| consensus_gap+pin_move | moneyline | 29-35 | 45.3 | 53.7 | -8.3 | +5.5 | 8.6 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 10-29 | 25.6 | 30.2 | -4.6 | +8.65 | 22.2 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 4-32 | 11.1 | 29.2 | -18.1 | -9.04 | -25.1 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 85-69 | 55.2 | 51.2 | 4.0 | +6.34 | 4.1 |  |  | no edge shown yet |
| follow_move+pin_rlm | moneyline | 24-40 | 37.5 | 29.6 | 7.9 | +1.46 | 2.3 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 37-85 | 30.3 | 29.7 | 0.6 | -7.78 | -6.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 46-62 | 42.6 | 42.6 | -0.1 | +10.69 | 9.9 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 37-71 | 34.3 | 28.8 | 5.5 | +22.57 | 20.9 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 36-79 | 31.3 | 29.9 | 1.4 | -3.18 | -2.8 |  |  | DROP: below break-even |
| pin_move+pin_rlm | moneyline | 27-46 | 37.0 | 28.6 | 8.4 | +16.19 | 22.2 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 24-34 | 41.4 | 28.2 | 13.1 | +9.29 | 16.0 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 21-31 | 40.4 | 30.2 | 10.2 | +7.28 | 14.0 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 46-64 | 41.8 | 41.9 | -0.1 | +8.51 | 7.7 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 14-33 | 29.8 | 28.6 | 1.2 | -5.18 | -11.0 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 24-40 | 37.5 | 29.6 | 7.9 | +1.46 | 2.3 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 38-74 | 33.9 | 28.7 | 5.2 | +20.97 | 18.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 23-69 | 25.0 | 27.6 | -2.6 | -9.91 | -10.8 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 37-85 | 30.3 | 29.7 | 0.6 | -7.78 | -6.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 11-82 | 11.8 | 28.1 | -16.3 | -29.62 | -31.8 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 14-45 | 23.7 | 30.6 | -6.9 | +2.27 | 3.8 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 16-35 | 31.4 | 30.3 | 1.1 | +0.84 | 1.6 |  |  | DROP: below break-even |
| money_delta+pin_rlm | moneyline | 22-44 | 33.3 | 28.8 | 4.6 | +7.63 | 11.6 |  |  | DROP: below break-even |
| money_delta+pin_value | moneyline | 2-18 | 10.0 | 26.6 | -16.6 | -11.18 | -55.9 |  |  | keep collecting (20/30) |
| money_moving+pin_value | moneyline | 10-33 | 23.3 | 29.9 | -6.6 | +8.44 | 19.6 |  |  | DROP: below break-even |
| pin_move+pin_value | moneyline | 6-9 | 40.0 | 32.9 | 7.1 | +7.27 | 48.5 |  |  | keep collecting (15/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 26.6 | 4.6 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 10-35 | 22.2 | 29.7 | -7.5 | +6.44 | 14.3 |  |  | DROP: below break-even |
| follow_move+money_delta | moneyline | 23-47 | 32.9 | 30.6 | 2.2 | -10.09 | -14.4 |  |  | DROP: below break-even |
| money_delta+money_level | moneyline | 14-23 | 37.8 | 30.4 | 7.4 | +6.11 | 16.5 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | moneyline | 21-38 | 35.6 | 30.6 | 5.0 | -3.0 | -5.1 |  |  | DROP: below break-even |
| money_level+pin_move | moneyline | 68-42 | 61.8 | 67.0 | -5.2 | -6.2 | -5.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 11-10 | 52.4 | 33.3 | 19.1 | +4.77 | 22.7 |  |  | keep collecting (21/30) |
| money_level+rlm_ratio | moneyline | 13-12 | 52.0 | 37.8 | 14.2 | +5.1 | 20.4 |  |  | keep collecting (25/30) |
| money_delta+rlm_quiet | moneyline | 15-35 | 30.0 | 29.4 | 0.6 | -9.95 | -19.9 |  |  | DROP: below break-even |
| money_level+pin_value | moneyline | 5-2 | 71.4 | 66.7 | 4.7 | +0.68 | 9.7 |  |  | keep collecting (7/30) |
| follow_move+pin_value | moneyline | 2-7 | 22.2 | 31.8 | -9.6 | -4.79 | -53.3 |  |  | keep collecting (9/30) |
| pin_value+rlm_quiet | moneyline | 1-6 | 14.3 | 26.6 | -12.3 | -4.48 | -64.0 |  |  | keep collecting (7/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 26.6 | -1.6 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 34-27 | 55.7 | 48.6 | 7.1 | +1.9 | 3.1 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 48-43 | 52.7 | 49.0 | 3.7 | -2.14 | -2.3 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 25-27 | 48.1 | 49.2 | -1.1 | -5.73 | -11.0 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 63-45 | 58.3 | 49.2 | 9.2 | +8.5 | 7.9 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 4-4 | 50.0 | 50.0 | 0.0 | -0.67 | -8.3 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | spread | 47-43 | 52.2 | 49.2 | 3.0 | -3.03 | -3.4 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 157-163 | 49.1 | 49.3 | -0.2 | -21.11 | -6.6 |  |  | no edge shown yet |
| follow_move+pin_move | spread | 123-140 | 46.8 | 49.9 | -3.1 | -28.02 | -10.7 |  |  | DROP: below break-even |
| follow_move+pin_rlm | spread | 19-18 | 51.4 | 50.6 | 0.7 | -0.65 | -1.7 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 56-50 | 52.8 | 49.0 | 3.8 | -1.23 | -1.2 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 41-44 | 48.2 | 50.1 | -1.9 | -6.76 | -8.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 158-162 | 49.4 | 49.3 | 0.0 | -18.97 | -5.9 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 117-125 | 48.3 | 49.8 | -1.5 | -19.0 | -7.8 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 23-22 | 51.1 | 50.8 | 0.3 | -1.04 | -2.3 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 79-81 | 49.4 | 49.3 | 0.1 | -12.83 | -8.0 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 39-43 | 47.6 | 50.1 | -2.5 | -7.69 | -9.4 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 320-313 | 50.6 | 49.6 | 1.0 | -24.56 | -3.9 |  |  | no edge shown yet |
| pin_move+pin_rlm | spread | 25-22 | 53.2 | 50.9 | 2.3 | +0.79 | 1.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 73-79 | 48.0 | 49.7 | -1.7 | -14.7 | -9.7 |  |  | no edge shown yet |
| pin_move+rlm_ratio | spread | 22-24 | 47.8 | 50.5 | -2.6 | -3.94 | -8.6 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 120-125 | 49.0 | 49.8 | -0.8 | -16.27 | -6.6 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 7-10 | 41.2 | 50.6 | -9.5 | -3.88 | -22.8 |  |  | keep collecting (17/30) |
| pin_rlm+rlm_ratio | spread | 19-18 | 51.4 | 50.6 | 0.7 | -0.65 | -1.7 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 25-22 | 53.2 | 50.9 | 2.3 | +0.79 | 1.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 7-7 | 50.0 | 49.4 | 0.6 | -1.01 | -7.2 |  |  | keep collecting (14/30) |
| pin_value+sharp_gap | spread | 79-81 | 49.4 | 49.4 | 0.0 | -12.89 | -8.1 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 41-44 | 48.2 | 50.1 | -1.9 | -6.76 | -8.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 153-166 | 48.0 | 49.1 | -1.1 | -27.73 | -8.7 |  |  | DROP: below break-even |
| money_level+rlm_ratio | spread | 21-28 | 42.9 | 49.9 | -7.0 | -9.13 | -18.6 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 252-248 | 50.4 | 49.3 | 1.1 | -21.1 | -4.2 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 58-47 | 55.2 | 48.9 | 6.4 | +2.6 | 2.5 |  |  | no edge shown yet |
| money_level+money_moving | spread | 251-249 | 50.2 | 49.3 | 0.9 | -23.02 | -4.6 |  |  | no edge shown yet |
| money_level+pin_move | spread | 108-126 | 46.2 | 49.6 | -3.4 | -28.53 | -12.2 |  |  | DROP: below break-even |
| money_level+pin_value | spread | 87-87 | 50.0 | 49.1 | 0.9 | -11.93 | -6.9 |  |  | no edge shown yet |
| consensus_gap+money_delta | spread | 14-14 | 50.0 | 50.5 | -0.5 | -2.09 | -7.5 |  |  | keep collecting (28/30) |
| follow_move+money_delta | spread | 38-48 | 44.2 | 50.2 | -6.0 | -13.62 | -15.8 |  |  | DROP: below break-even |
| money_delta+money_level | spread | 41-40 | 50.6 | 50.0 | 0.6 | -3.05 | -3.8 |  |  | no edge shown yet |
| money_delta+money_moving | spread | 69-75 | 47.9 | 50.4 | -2.5 | -12.73 | -8.8 |  |  | no edge shown yet |
| money_delta+pin_value | spread | 32-26 | 55.2 | 50.4 | 4.7 | +1.88 | 3.2 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 68-73 | 48.2 | 50.4 | -2.2 | -11.71 | -8.3 |  |  | no edge shown yet |
| follow_move+rlm_quiet | spread | 46-46 | 50.0 | 50.7 | -0.7 | -3.4 | -3.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 14-4 | 77.8 | 50.7 | 27.1 | +8.78 | 48.8 |  |  | keep collecting (18/30) |
| rlm_quiet+sharp_gap | spread | 21-10 | 67.7 | 50.9 | 16.8 | +9.22 | 29.7 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+pin_rlm | spread | 14-10 | 58.3 | 50.4 | 8.0 | +2.58 | 10.7 |  |  | keep collecting (24/30) |
| money_delta+rlm_ratio | spread | 16-27 | 37.2 | 50.0 | -12.7 | -12.78 | -29.7 |  |  | DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 52.1 | 47.9 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_move | spread | 36-42 | 46.2 | 50.8 | -4.7 | -9.09 | -11.7 |  |  | no edge shown yet |
| money_delta+pin_rlm | spread | 13-15 | 46.4 | 50.6 | -4.2 | -3.31 | -11.8 |  |  | keep collecting (28/30) |
| money_delta+rlm_quiet | spread | 14-17 | 45.2 | 51.0 | -5.9 | -4.07 | -13.1 |  |  | no edge shown yet |
| money_moving+rlm_quiet | spread | 20-10 | 66.7 | 50.9 | 15.8 | +8.27 | 27.6 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_move+rlm_quiet | spread | 25-22 | 53.2 | 51.0 | 2.1 | +1.17 | 2.5 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-2 | 75.0 | 51.6 | 23.4 | +3.56 | 44.5 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_quiet | spread | 2-3 | 40.0 | 50.4 | -10.4 | -1.33 | -26.7 |  |  | keep collecting (5/30) |
| pin_value+rlm_quiet | spread | 4-4 | 50.0 | 48.9 | 1.1 | -0.52 | -6.5 |  |  | keep collecting (8/30) |
| follow_move+money_delta | total | 93-85 | 52.2 | 50.2 | 2.1 | +0.06 | 0.0 |  |  | no edge shown yet |
| money_level+money_moving | total | 208-209 | 49.9 | 50.0 | -0.1 | -19.5 | -4.7 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 207-201 | 50.7 | 50.0 | 0.7 | -12.3 | -3.0 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 314-334 | 48.5 | 50.1 | -1.6 | -47.32 | -7.3 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 54-57 | 48.6 | 49.7 | -1.1 | -9.01 | -8.1 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 27-22 | 55.1 | 49.8 | 5.3 | +1.96 | 4.0 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 61-60 | 50.4 | 49.8 | 0.6 | -5.81 | -4.8 |  |  | no edge shown yet |
| follow_move+money_moving | total | 202-220 | 47.9 | 50.1 | -2.2 | -35.79 | -8.5 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 210-218 | 49.1 | 50.1 | -1.0 | -26.48 | -6.2 |  |  | no edge shown yet |
| money_level+pin_move | total | 122-104 | 54.0 | 50.0 | 4.0 | +7.19 | 3.2 |  |  | no edge shown yet |
| money_level+pin_value | total | 82-74 | 52.6 | 49.8 | 2.7 | -0.55 | -0.4 |  |  | no edge shown yet |
| pin_move+pin_value | total | 77-68 | 53.1 | 50.0 | 3.1 | +1.49 | 1.0 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 89-106 | 45.6 | 50.2 | -4.5 | -24.45 | -12.5 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 138-141 | 49.5 | 50.1 | -0.6 | -14.89 | -5.3 |  |  | no edge shown yet |
| rlm_quiet+sharp_gap | total | 54-72 | 42.9 | 50.2 | -7.4 | -22.59 | -17.9 |  |  | DROP: below break-even |
| money_delta+money_moving | total | 115-110 | 51.1 | 50.2 | 0.9 | -4.87 | -2.2 |  |  | no edge shown yet |
| follow_move+money_level | total | 170-161 | 51.4 | 49.9 | 1.4 | -6.39 | -1.9 |  |  | no edge shown yet |
| follow_move+pin_value | total | 66-63 | 51.2 | 50.0 | 1.2 | -3.49 | -2.7 |  |  | no edge shown yet |
| money_moving+pin_value | total | 67-75 | 47.2 | 50.0 | -2.8 | -14.6 | -10.3 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 69-74 | 48.3 | 50.0 | -1.8 | -11.74 | -8.2 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 47-49 | 49.0 | 49.8 | -0.9 | -7.27 | -7.6 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 49-47 | 51.0 | 49.8 | 1.2 | -3.48 | -3.6 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 42-35 | 54.5 | 49.8 | 4.8 | +2.21 | 2.9 |  |  | no edge shown yet |
| consensus_gap+money_delta | total | 17-14 | 54.8 | 50.0 | 4.9 | +0.94 | 3.0 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | total | 11-8 | 57.9 | 50.1 | 7.8 | +1.81 | 9.5 |  |  | keep collecting (19/30) |
| money_delta+rlm_quiet | total | 22-38 | 36.7 | 50.3 | -13.6 | -17.9 | -29.8 |  |  | DROP: below break-even |
| money_delta+sharp_gap | total | 115-107 | 51.8 | 50.2 | 1.6 | -1.87 | -0.8 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 48-70 | 40.7 | 50.2 | -9.5 | -26.08 | -22.1 |  |  | DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 64-48 | 57.1 | 50.2 | 7.0 | +10.39 | 9.3 |  |  | no edge shown yet |
| money_delta+pin_move | total | 68-59 | 53.5 | 50.2 | 3.3 | +3.22 | 2.5 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 141-140 | 50.2 | 50.1 | 0.1 | -11.07 | -3.9 |  |  | no edge shown yet |
| follow_move+pin_move | total | 154-152 | 50.3 | 50.1 | 0.3 | -11.29 | -3.7 |  |  | no edge shown yet |
| pin_value+rlm_quiet | total | 20-25 | 44.4 | 50.2 | -5.7 | -6.67 | -14.8 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | total | 10-8 | 55.6 | 50.0 | 5.6 | +0.87 | 4.8 |  |  | keep collecting (18/30) |
| consensus_gap+rlm_ratio | total | 18-9 | 66.7 | 49.9 | 16.8 | +6.95 | 25.8 |  |  | keep collecting (27/30) |
| follow_move+pin_rlm | total | 66-54 | 55.0 | 50.2 | 4.8 | +6.71 | 5.6 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 124-103 | 54.6 | 50.2 | 4.4 | +10.55 | 4.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 39-24 | 61.9 | 50.2 | 11.7 | +11.86 | 18.8 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 62-42 | 59.6 | 50.2 | 9.5 | +14.67 | 14.1 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 75-61 | 55.1 | 50.2 | 4.9 | +7.74 | 5.7 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 119-101 | 54.1 | 50.2 | 3.9 | +7.97 | 3.6 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 78-63 | 55.3 | 50.2 | 5.1 | +8.47 | 6.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 74-55 | 57.4 | 50.2 | 7.1 | +12.87 | 10.0 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 28-20 | 58.3 | 50.2 | 8.2 | +5.4 | 11.2 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 66-54 | 55.0 | 50.2 | 4.8 | +6.71 | 5.6 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 78-63 | 55.3 | 50.2 | 5.1 | +8.47 | 6.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 31-21 | 59.6 | 50.2 | 9.5 | +7.13 | 13.7 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 124-103 | 54.6 | 50.2 | 4.4 | +10.55 | 4.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 48-35 | 57.8 | 50.3 | 7.6 | +9.06 | 10.9 |  |  | no edge shown yet |
| money_delta+rlm_ratio | total | 75-53 | 58.6 | 50.2 | 8.4 | +15.54 | 12.1 |  |  | no edge shown yet |
| money_delta+pin_value | total | 35-27 | 56.5 | 50.1 | 6.3 | +4.64 | 7.5 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 41-53 | 43.6 | 50.2 | -6.6 | -15.41 | -16.4 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | total | 22-28 | 44.0 | 50.3 | -6.3 | -7.86 | -15.7 |  |  | no edge shown yet |
| rlm_quiet+rlm_ratio | total | 43-54 | 44.3 | 50.3 | -5.9 | -14.59 | -15.0 |  |  | DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 50.4 | 49.6 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| rlm_quiet | close | 1-3k bets | 122-179 | 40.5 | -1.2 | -9.1 |  |
| rlm_quiet | close | 3k+ bets | 45-60 | 42.9 | 0.4 | -6.7 |  |
| rlm_quiet | close | <1k bets | 22-28 | 44.0 | 2.4 | -6.0 |  |
| rlm_quiet | close | pin $1-2k | 47-83 | 36.2 | -6.9 | -17.8 |  |
| rlm_quiet | close | pin $2k+ | 53-64 | 45.3 | 7.5 | -2.1 |  |
| rlm_quiet | close | pin limit <$1k | 38-36 | 51.4 | 1.4 | -1.7 |  |
| pin_move | close | 1-3k bets | 315-313 | 50.2 | 0.2 | -2.4 |  |
| pin_move | close | 3k+ bets | 123-123 | 50.0 | 0.4 | -3.2 |  |
| pin_move | close | <1k bets | 67-68 | 49.6 | -1.0 | -4.6 |  |
| pin_move | close | pin $1-2k | 238-232 | 50.6 | 0.3 | -0.8 |  |
| pin_move | close | pin $2k+ | 178-187 | 48.8 | -0.8 | -7.1 |  |
| pin_move | close | pin limit <$1k | 89-85 | 51.1 | 1.3 | 0.3 |  |
| money_delta | close | 1-3k bets | 203-259 | 43.9 | -0.9 | -7.0 |  |
| money_delta | close | 3k+ bets | 80-109 | 42.3 | -0.8 | -2.8 |  |
| money_delta | close | <1k bets | 38-62 | 38.0 | -4.1 | -22.9 |  |
| money_delta | close | pin $1-2k | 115-118 | 49.4 | 3.6 | 3.1 |  |
| money_delta | close | pin $2k+ | 83-111 | 42.8 | 1.6 | -8.8 |  |
| money_delta | close | pin limit <$1k | 51-54 | 48.6 | -1.2 | -2.8 |  |
| pin_rlm | close | 1-3k bets | 87-94 | 48.1 | 5.3 | 17.0 |  |
| pin_rlm | close | 3k+ bets | 33-44 | 42.9 | 0.6 | -6.6 |  |
| pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| pin_rlm | close | pin $1-2k | 62-65 | 48.8 | 5.0 | 12.4 |  |
| pin_rlm | close | pin $2k+ | 38-65 | 36.9 | 1.1 | -2.9 |  |
| pin_rlm | close | pin limit <$1k | 41-29 | 58.6 | 9.3 | 24.9 |  |
| follow_move | close | 1-3k bets | 563-500 | 53.0 | 1.4 | -5.0 |  |
| follow_move | close | 3k+ bets | 192-177 | 52.0 | 0.2 | -4.5 |  |
| follow_move | close | <1k bets | 120-108 | 52.6 | -0.6 | -11.2 |  |
| follow_move | close | pin $1-2k | 264-288 | 47.8 | -3.4 | -10.9 |  |
| follow_move | close | pin $2k+ | 222-187 | 54.3 | 2.3 | -4.1 |  |
| follow_move | close | pin limit <$1k | 107-105 | 50.5 | 0.4 | -3.7 |  |
| rlm_ratio | close | 1-3k bets | 127-162 | 43.9 | -0.6 | -5.6 |  |
| rlm_ratio | close | 3k+ bets | 49-44 | 52.7 | 7.9 | 12.7 |  |
| rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.9 | 0.8 |  |
| rlm_ratio | close | pin $1-2k | 71-72 | 49.7 | 3.2 | 3.9 |  |
| rlm_ratio | close | pin $2k+ | 38-52 | 42.2 | 4.0 | -6.6 |  |
| rlm_ratio | close | pin limit <$1k | 45-34 | 57.0 | 7.3 | 10.0 |  |
| money_level | close | 1-3k bets | 717-510 | 58.4 | 2.8 | -2.0 |  |
| money_level | close | 3k+ bets | 245-195 | 55.7 | 0.6 | -3.3 |  |
| money_level | close | <1k bets | 145-118 | 55.1 | -0.8 | -11.5 |  |
| money_level | close | pin $1-2k | 325-282 | 53.5 | -0.5 | -4.8 |  |
| money_level | close | pin $2k+ | 280-219 | 56.1 | -1.2 | -7.4 |  |
| money_level | close | pin limit <$1k | 125-124 | 50.2 | 0.1 | -4.6 |  |
| sharp_gap | close | 1-3k bets | 533-640 | 45.4 | -2.0 | -9.1 |  |
| sharp_gap | close | 3k+ bets | 211-220 | 49.0 | 1.5 | 3.1 |  |
| sharp_gap | close | <1k bets | 114-137 | 45.4 | -2.4 | -14.6 |  |
| sharp_gap | close | pin $1-2k | 278-309 | 47.4 | -1.3 | -5.5 |  |
| sharp_gap | close | pin $2k+ | 223-257 | 46.5 | 0.1 | -3.1 |  |
| sharp_gap | close | pin limit <$1k | 116-123 | 48.5 | -1.2 | -3.2 |  |
| money_moving | close | 1-3k bets | 538-639 | 45.7 | -2.2 | -9.5 |  |
| money_moving | close | 3k+ bets | 210-222 | 48.6 | 0.8 | 1.6 |  |
| money_moving | close | <1k bets | 112-137 | 45.0 | -2.5 | -13.5 |  |
| money_moving | close | pin $1-2k | 276-312 | 46.9 | -2.0 | -6.2 |  |
| money_moving | close | pin $2k+ | 224-255 | 46.8 | 0.4 | -3.1 |  |
| money_moving | close | pin limit <$1k | 112-130 | 46.3 | -3.4 | -7.6 |  |
| pin_value | close | 1-3k bets | 225-235 | 48.9 | 1.1 | 0.7 |  |
| pin_value | close | 3k+ bets | 80-85 | 48.5 | -0.0 | -5.0 |  |
| pin_value | close | <1k bets | 54-44 | 55.1 | 8.0 | 10.6 |  |
| pin_value | close | pin $1-2k | 165-186 | 47.0 | -1.2 | -4.2 |  |
| pin_value | close | pin $2k+ | 101-113 | 47.2 | 1.2 | -1.2 |  |
| pin_value | close | pin limit <$1k | 93-65 | 58.9 | 9.2 | 14.4 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.9 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.9 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 225-285 | 44.1 | -4.1 | -11.6 |  |
| consensus_gap | close | 3k+ bets | 81-96 | 45.8 | -1.8 | 4.5 |  |
| consensus_gap | close | <1k bets | 40-78 | 33.9 | -9.7 | -30.7 |  |
| consensus_gap | close | pin $1-2k | 111-123 | 47.4 | -1.8 | -2.1 |  |
| consensus_gap | close | pin $2k+ | 88-105 | 45.6 | -4.0 | -4.6 |  |
| consensus_gap | close | pin limit <$1k | 50-44 | 53.2 | 3.0 | 3.9 |  |
| consensus_gap+follow_move | close | 1-3k bets | 92-85 | 52.0 | -0.0 | -2.6 |  |
| consensus_gap+money_level | close | 1-3k bets | 151-101 | 59.9 | 0.9 | 2.2 |  |
| consensus_gap+money_moving | close | 1-3k bets | 101-157 | 39.1 | -6.2 | -11.4 |  |
| consensus_gap+pin_move | close | 1-3k bets | 54-52 | 50.9 | -0.7 | 4.0 |  |
| consensus_gap+pin_value | close | 1-3k bets | 90-103 | 46.6 | 0.7 | -1.2 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 98-160 | 38.0 | -6.4 | -12.6 |  |
| follow_move+money_level | close | 1-3k bets | 378-259 | 59.3 | 3.0 | -3.1 |  |
| follow_move+money_moving | close | 1-3k bets | 305-326 | 48.3 | -1.0 | -7.7 |  |
| follow_move+pin_move | close | 1-3k bets | 227-230 | 49.7 | -0.5 | -5.7 |  |
| follow_move+pin_value | close | 1-3k bets | 74-76 | 49.3 | 0.8 | -6.5 |  |
| follow_move+sharp_gap | close | 1-3k bets | 307-325 | 48.6 | -0.4 | -6.4 |  |
| money_level+money_moving | close | 1-3k bets | 388-344 | 53.0 | 0.5 | -3.9 |  |
| money_level+pin_move | close | 1-3k bets | 197-176 | 52.8 | 0.0 | -3.6 |  |
| money_level+pin_value | close | 1-3k bets | 112-103 | 52.1 | 2.5 | -2.2 |  |
| money_level+sharp_gap | close | 1-3k bets | 375-336 | 52.7 | 0.6 | -3.4 |  |
| money_moving+pin_move | close | 1-3k bets | 194-207 | 48.4 | -0.7 | -2.6 |  |
| money_moving+pin_value | close | 1-3k bets | 100-125 | 44.4 | -2.9 | -7.6 |  |
| money_moving+sharp_gap | close | 1-3k bets | 509-610 | 45.5 | -2.0 | -8.7 |  |
| pin_move+pin_value | close | 1-3k bets | 99-97 | 50.5 | 1.5 | -0.5 |  |
| pin_move+sharp_gap | close | 1-3k bets | 200-207 | 49.1 | 0.3 | -0.7 |  |
| pin_value+sharp_gap | close | 1-3k bets | 102-128 | 44.3 | -2.8 | -8.0 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 122-179 | 40.5 | -1.2 | -9.1 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 63-109 | 36.6 | -4.9 | -13.0 |  |
| consensus_gap+money_delta | close | 1-3k bets | 26-65 | 28.6 | -8.9 | -22.9 |  |
| follow_move+money_delta | close | 1-3k bets | 97-113 | 46.2 | -0.9 | -8.2 |  |
| money_delta+money_level | close | 1-3k bets | 75-72 | 51.0 | 3.0 | 5.6 |  |
| money_delta+money_moving | close | 1-3k bets | 142-206 | 40.8 | -2.3 | -10.2 |  |
| money_delta+pin_value | close | 1-3k bets | 45-44 | 50.6 | 3.1 | 1.3 |  |
| money_delta+sharp_gap | close | 1-3k bets | 141-203 | 41.0 | -2.2 | -9.8 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 71-78 | 47.7 | 0.1 | 2.0 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 17-27 | 38.6 | -0.2 | 16.5 |  |
| money_level+pin_rlm | close | 1-3k bets | 39-29 | 57.4 | 8.6 | 10.4 |  |
| pin_move+pin_rlm | close | 1-3k bets | 79-77 | 50.6 | 5.9 | 13.0 |  |
| pin_rlm+pin_value | close | 1-3k bets | 29-24 | 54.7 | 8.5 | 30.7 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 87-94 | 48.1 | 5.3 | 17.0 |  |
| money_delta+pin_rlm | close | 1-3k bets | 49-53 | 48.0 | 4.5 | 15.3 |  |
| money_moving+pin_rlm | close | 1-3k bets | 82-90 | 47.7 | 4.8 | 17.3 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 20-32 | 38.5 | -1.6 | 1.7 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 127-162 | 43.9 | -0.6 | -5.6 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 67-79 | 45.9 | -0.2 | -7.4 |  |
| money_level+rlm_ratio | close | 1-3k bets | 59-57 | 50.9 | 1.4 | -1.9 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 121-155 | 43.8 | -1.0 | -5.5 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 127-162 | 43.9 | -0.6 | -5.6 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 13-32 | 28.9 | -6.7 | -9.2 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 56-106 | 34.6 | -7.0 | -16.5 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 51-93 | 35.4 | -4.5 | -12.4 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 54-70 | 43.5 | -0.5 | -7.0 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 33-56 | 37.1 | -6.8 | -21.6 |  |
| follow_move+pin_rlm | close | 1-3k bets | 62-71 | 46.6 | 2.1 | -3.2 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 67-66 | 50.4 | 4.4 | 4.0 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 24-42 | 36.4 | -3.6 | -15.9 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 62-71 | 46.6 | 2.1 | -3.2 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 26-21 | 55.3 | 7.4 | 6.3 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 15-20 | 42.9 | -2.6 | -16.6 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 49.6 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 30-27 | 52.6 | 2.9 | 3.3 |  |
| consensus_gap+money_moving | close | 3k+ bets | 33-53 | 38.4 | -6.0 | 13.2 |  |
| consensus_gap+pin_move | close | 3k+ bets | 21-19 | 52.5 | 2.3 | 6.4 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-6 | 33.3 | -6.4 | 6.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 34-33 | 50.7 | 4.3 | 4.3 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -0.8 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 34-53 | 39.1 | -5.1 | 16.3 |  |
| follow_move+money_moving | close | 3k+ bets | 102-106 | 49.0 | -0.1 | -3.6 |  |
| follow_move+pin_move | close | 3k+ bets | 93-89 | 51.1 | 1.2 | -0.5 |  |
| follow_move+pin_rlm | close | 3k+ bets | 31-30 | 50.8 | 6.5 | 11.7 |  |
| follow_move+pin_value | close | 3k+ bets | 32-32 | 50.0 | 0.1 | -6.2 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 49-44 | 52.7 | 7.9 | 12.7 |  |
| follow_move+sharp_gap | close | 3k+ bets | 104-105 | 49.8 | 1.0 | -1.5 |  |
| money_moving+pin_move | close | 3k+ bets | 71-80 | 47.0 | -1.1 | -6.4 |  |
| money_moving+pin_rlm | close | 3k+ bets | 32-43 | 42.7 | 0.7 | -6.7 |  |
| money_moving+pin_value | close | 3k+ bets | 39-48 | 44.8 | -2.6 | -7.9 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 47-42 | 52.8 | 8.1 | 13.3 |  |
| money_moving+sharp_gap | close | 3k+ bets | 203-212 | 48.9 | 1.4 | 2.9 |  |
| pin_move+pin_rlm | close | 3k+ bets | 32-38 | 45.7 | 1.9 | -0.1 |  |
| pin_move+pin_value | close | 3k+ bets | 32-39 | 45.1 | -4.4 | -15.2 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 34-31 | 52.3 | 6.9 | 13.3 |  |
| pin_move+sharp_gap | close | 3k+ bets | 71-80 | 47.0 | -0.8 | -5.7 |  |
| pin_rlm+pin_value | close | 3k+ bets | 6-14 | 30.0 | -16.0 | -42.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 31-30 | 50.8 | 6.5 | 11.7 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 33-44 | 42.9 | 0.6 | -6.6 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 9-9 | 50.0 | -0.3 | -5.1 |  |
| pin_value+sharp_gap | close | 3k+ bets | 39-47 | 45.3 | -2.1 | -6.8 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 49-44 | 52.7 | 7.9 | 12.7 |  |
| follow_move+money_delta | close | 3k+ bets | 39-47 | 45.3 | 0.1 | -6.0 |  |
| money_level+money_moving | close | 3k+ bets | 143-123 | 53.8 | 1.6 | -0.4 |  |
| money_level+sharp_gap | close | 3k+ bets | 142-120 | 54.2 | 2.2 | 1.1 |  |
| follow_move+money_level | close | 3k+ bets | 120-90 | 57.1 | 0.9 | -2.9 |  |
| money_level+rlm_ratio | close | 3k+ bets | 24-12 | 66.7 | 19.6 | 36.9 |  |
| consensus_gap+money_level | close | 3k+ bets | 44-45 | 49.4 | -7.3 | -14.3 |  |
| money_level+pin_move | close | 3k+ bets | 67-61 | 52.3 | -1.0 | -3.7 |  |
| money_level+pin_value | close | 3k+ bets | 44-43 | 50.6 | 0.3 | -6.3 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 7-12 | 36.8 | -0.8 | -5.4 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 45-60 | 42.9 | 0.4 | -6.7 |  |
| money_delta+money_moving | close | 3k+ bets | 61-83 | 42.4 | 0.2 | 2.1 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 19-24 | 44.2 | 2.7 | 2.2 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 23-32 | 41.8 | -0.4 | -6.0 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 21-31 | 40.4 | -1.8 | -8.0 |  |
| consensus_gap+money_delta | close | 3k+ bets | 12-23 | 34.3 | -4.0 | 18.4 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 10-24 | 29.4 | -13.2 | -34.9 |  |
| money_delta+sharp_gap | close | 3k+ bets | 59-80 | 42.4 | 0.4 | 2.8 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 26-29 | 47.3 | 3.8 | 3.3 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 11-16 | 40.7 | -0.9 | -3.2 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 7-11 | 38.9 | -11.1 | -25.7 |  |
| money_delta+money_level | close | 3k+ bets | 32-22 | 59.3 | 13.3 | 19.9 |  |
| money_level+pin_rlm | close | 3k+ bets | 16-9 | 64.0 | 19.1 | 37.0 |  |
| money_delta+pin_value | close | 3k+ bets | 18-19 | 48.6 | 2.7 | -8.3 |  |
| money_delta+pin_move | close | 3k+ bets | 36-41 | 46.8 | 1.5 | -4.5 |  |
| money_delta+pin_rlm | close | 3k+ bets | 22-27 | 44.9 | 3.0 | -4.5 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 29-24 | 54.7 | 10.2 | 16.3 |  |
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
| pin_move+sharp_gap | close | <1k bets | 36-42 | 46.2 | -2.4 | -9.5 |  |
| pin_value+sharp_gap | close | <1k bets | 17-15 | 53.1 | 7.2 | 18.5 |  |
| follow_move+money_delta | close | <1k bets | 18-20 | 47.4 | 4.8 | -3.2 |  |
| follow_move+money_moving | close | <1k bets | 54-63 | 46.2 | -3.5 | -13.8 |  |
| follow_move+pin_move | close | <1k bets | 42-42 | 50.0 | -1.4 | -7.2 |  |
| follow_move+sharp_gap | close | <1k bets | 56-63 | 47.1 | -3.4 | -16.1 |  |
| money_delta+money_moving | close | <1k bets | 27-46 | 37.0 | -3.0 | -23.1 |  |
| money_delta+pin_move | close | <1k bets | 13-17 | 43.3 | -0.6 | -15.5 |  |
| money_delta+sharp_gap | close | <1k bets | 27-46 | 37.0 | -3.0 | -23.1 |  |
| follow_move+rlm_quiet | close | <1k bets | 22-28 | 44.0 | 2.4 | -6.0 |  |
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
| pin_move+rlm_quiet | close | <1k bets | 10-10 | 50.0 | 4.7 | 9.6 |  |
| pin_move+rlm_ratio | close | <1k bets | 16-13 | 55.2 | 10.1 | 7.8 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 21.4 | 60.8 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 7-5 | 58.3 | 15.9 | 15.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 16-11 | 59.3 | 16.2 | 17.3 |  |
| pin_value+rlm_quiet | close | <1k bets | 3-4 | 42.9 | -6.6 | -17.6 |  |
| pin_value+rlm_ratio | close | <1k bets | 4-1 | 80.0 | 30.6 | 51.7 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 2-7 | 22.2 | -12.0 | -57.2 |  |
| money_delta+money_level | close | <1k bets | 12-17 | 41.4 | -2.1 | -18.9 |  |
| money_level+rlm_ratio | close | <1k bets | 13-13 | 50.0 | 4.6 | -1.9 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 17.6 | 19.0 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 0-5 | 0.0 | -35.6 | -100.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 42-48 | 46.7 | -6.0 | -10.8 |  |
| consensus_gap+money_moving | close | pin $1-2k | 55-67 | 45.1 | -3.4 | -4.9 |  |
| consensus_gap+pin_move | close | pin $1-2k | 43-44 | 49.4 | -3.0 | 4.3 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-18 | 41.9 | 1.0 | 25.8 |  |
| consensus_gap+pin_value | close | pin $1-2k | 65-72 | 47.4 | 1.5 | -4.8 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-14 | 50.0 | 4.5 | 9.0 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 52-65 | 44.4 | -2.6 | -4.1 |  |
| follow_move+money_moving | close | pin $1-2k | 154-185 | 45.4 | -4.4 | -10.9 |  |
| follow_move+pin_move | close | pin $1-2k | 168-175 | 49.0 | -1.6 | -5.9 |  |
| follow_move+pin_rlm | close | pin $1-2k | 50-49 | 50.5 | 4.6 | 6.4 |  |
| follow_move+pin_value | close | pin $1-2k | 56-66 | 45.9 | -3.5 | -13.4 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 71-72 | 49.7 | 3.2 | 3.9 |  |
| follow_move+sharp_gap | close | pin $1-2k | 157-184 | 46.0 | -3.6 | -10.1 |  |
| money_moving+pin_move | close | pin $1-2k | 147-162 | 47.6 | -1.7 | -3.3 |  |
| money_moving+pin_rlm | close | pin $1-2k | 59-62 | 48.8 | 4.6 | 12.9 |  |
| money_moving+pin_value | close | pin $1-2k | 66-98 | 40.2 | -7.6 | -21.2 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 69-68 | 50.4 | 3.5 | 5.2 |  |
| money_moving+sharp_gap | close | pin $1-2k | 267-300 | 47.1 | -1.6 | -5.7 |  |
| pin_move+pin_rlm | close | pin $1-2k | 59-59 | 50.0 | 4.9 | 12.6 |  |
| pin_move+pin_value | close | pin $1-2k | 71-87 | 44.9 | -4.7 | -13.2 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 58-53 | 52.3 | 5.3 | 8.2 |  |
| pin_move+sharp_gap | close | pin $1-2k | 150-162 | 48.1 | -1.0 | -2.7 |  |
| pin_rlm+pin_value | close | pin $1-2k | 15-24 | 38.5 | -9.9 | -19.7 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 50-49 | 50.5 | 4.6 | 6.4 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 62-65 | 48.8 | 5.0 | 12.4 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 18-20 | 47.4 | -2.5 | -10.6 |  |
| pin_value+sharp_gap | close | pin $1-2k | 66-96 | 40.7 | -7.0 | -20.2 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 71-72 | 49.7 | 3.2 | 3.9 |  |
| follow_move+money_level | close | pin $1-2k | 184-172 | 51.7 | -2.7 | -9.4 |  |
| money_level+rlm_ratio | close | pin $1-2k | 41-32 | 56.2 | 7.5 | 9.6 |  |
| money_level+sharp_gap | close | pin $1-2k | 199-194 | 50.6 | -1.1 | -5.9 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 3-11 | 21.4 | -20.4 | -31.6 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 47-83 | 36.2 | -6.9 | -17.8 |  |
| money_level+money_moving | close | pin $1-2k | 200-198 | 50.3 | -1.7 | -6.8 |  |
| consensus_gap+money_level | close | pin $1-2k | 66-59 | 52.8 | -4.2 | -7.1 |  |
| money_level+pin_value | close | pin $1-2k | 75-79 | 48.7 | -1.2 | -8.9 |  |
| money_level+pin_move | close | pin $1-2k | 147-135 | 52.1 | -0.7 | -4.7 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 23-37 | 38.3 | -5.6 | -4.8 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 34-46 | 42.5 | -2.6 | -3.3 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 15-26 | 36.6 | -7.3 | -10.6 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 20-32 | 38.5 | -4.5 | -5.1 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 24-39 | 38.1 | -5.4 | -8.6 |  |
| money_level+pin_rlm | close | pin $1-2k | 30-22 | 57.7 | 11.1 | 13.4 |  |
| follow_move+money_delta | close | pin $1-2k | 56-57 | 49.6 | 3.2 | 2.1 |  |
| money_delta+money_moving | close | pin $1-2k | 79-93 | 45.9 | 1.6 | -0.5 |  |
| money_delta+pin_move | close | pin $1-2k | 60-62 | 49.2 | 1.8 | 4.2 |  |
| money_delta+pin_rlm | close | pin $1-2k | 38-41 | 48.1 | 4.5 | 11.0 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 43-40 | 51.8 | 5.7 | 9.0 |  |
| money_delta+sharp_gap | close | pin $1-2k | 79-91 | 46.5 | 2.1 | 0.7 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 47.9 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 43-36 | 54.4 | 6.4 | 5.9 |  |
| consensus_gap+money_delta | close | pin $1-2k | 16-26 | 38.1 | -2.5 | -10.1 |  |
| money_delta+pin_value | close | pin $1-2k | 37-42 | 46.8 | -1.7 | -11.5 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 13-26 | 33.3 | -9.7 | -19.0 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 8-21 | 27.6 | -21.6 | -47.0 |  |
| follow_move+money_level | close | pin $2k+ | 139-89 | 61.0 | 1.7 | -2.6 |  |
| follow_move+money_moving | close | pin $2k+ | 106-105 | 50.2 | 2.4 | -3.9 |  |
| follow_move+pin_move | close | pin $2k+ | 134-126 | 51.5 | 1.6 | -2.9 |  |
| follow_move+sharp_gap | close | pin $2k+ | 107-106 | 50.2 | 2.5 | -3.6 |  |
| money_level+money_moving | close | pin $2k+ | 151-137 | 52.4 | -0.2 | -4.8 |  |
| money_level+pin_move | close | pin $2k+ | 101-89 | 53.2 | -2.1 | -6.2 |  |
| money_level+sharp_gap | close | pin $2k+ | 151-138 | 52.2 | -0.4 | -4.7 |  |
| money_moving+pin_move | close | pin $2k+ | 95-104 | 47.7 | 0.6 | -4.7 |  |
| money_moving+sharp_gap | close | pin $2k+ | 218-251 | 46.5 | 0.2 | -2.9 |  |
| pin_move+sharp_gap | close | pin $2k+ | 95-105 | 47.5 | 0.3 | -4.7 |  |
| consensus_gap+money_delta | close | pin $2k+ | 7-25 | 21.9 | -9.9 | -56.9 |  |
| consensus_gap+money_moving | close | pin $2k+ | 30-61 | 33.0 | -10.4 | -9.8 |  |
| consensus_gap+pin_value | close | pin $2k+ | 37-46 | 44.6 | 2.5 | 9.0 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 32-64 | 33.3 | -10.6 | -9.1 |  |
| money_delta+money_moving | close | pin $2k+ | 57-79 | 41.9 | 3.4 | -6.8 |  |
| money_delta+pin_value | close | pin $2k+ | 18-21 | 46.2 | 3.6 | -11.8 |  |
| money_delta+sharp_gap | close | pin $2k+ | 55-78 | 41.4 | 2.8 | -7.9 |  |
| money_moving+pin_value | close | pin $2k+ | 54-64 | 45.8 | 0.8 | 5.1 |  |
| pin_value+sharp_gap | close | pin $2k+ | 54-65 | 45.4 | 0.6 | 4.2 |  |
| consensus_gap+pin_move | close | pin $2k+ | 24-30 | 44.4 | -5.6 | -16.2 |  |
| money_delta+pin_move | close | pin $2k+ | 31-44 | 41.3 | -1.1 | -14.8 |  |
| consensus_gap+follow_move | close | pin $2k+ | 27-26 | 50.9 | -1.0 | -14.6 |  |
| follow_move+pin_value | close | pin $2k+ | 32-30 | 51.6 | 4.5 | -2.3 |  |
| pin_move+pin_value | close | pin $2k+ | 45-44 | 50.6 | 2.9 | -0.6 |  |
| follow_move+money_delta | close | pin $2k+ | 31-38 | 44.9 | 2.9 | -6.6 |  |
| follow_move+pin_rlm | close | pin $2k+ | 27-41 | 39.7 | 2.1 | -9.3 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 38-52 | 42.2 | 4.0 | -6.6 |  |
| money_delta+money_level | close | pin $2k+ | 25-20 | 55.6 | 11.9 | 12.4 |  |
| money_delta+pin_rlm | close | pin $2k+ | 21-36 | 36.8 | 1.3 | -8.3 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 19-23 | 45.2 | 6.3 | -1.7 |  |
| money_level+pin_rlm | close | pin $2k+ | 15-10 | 60.0 | 16.3 | 27.1 |  |
| money_level+pin_value | close | pin $2k+ | 54-50 | 51.9 | 2.1 | -4.1 |  |
| money_level+rlm_ratio | close | pin $2k+ | 14-12 | 53.8 | 8.3 | 13.1 |  |
| money_moving+pin_rlm | close | pin $2k+ | 38-65 | 36.9 | 1.1 | -2.9 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 38-51 | 42.7 | 4.4 | -5.5 |  |
| pin_move+pin_rlm | close | pin $2k+ | 31-43 | 41.9 | 3.8 | -1.9 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 27-35 | 43.5 | 3.7 | -0.6 |  |
| pin_rlm+pin_value | close | pin $2k+ | 6-13 | 31.6 | -4.3 | 13.6 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 27-41 | 39.7 | 2.1 | -9.3 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 38-65 | 36.9 | 1.1 | -2.9 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 4-6 | 40.0 | -0.9 | -19.0 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 38-52 | 42.2 | 4.0 | -6.6 |  |
| consensus_gap+money_level | close | pin $2k+ | 56-47 | 54.4 | -8.6 | -15.3 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 53-64 | 45.3 | 7.5 | -2.1 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 16-20 | 44.4 | 5.7 | -7.5 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 26-35 | 42.6 | 7.2 | -4.2 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 13-27 | 32.5 | 0.3 | -20.0 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 20-32 | 38.5 | 5.8 | -9.7 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 26-36 | 41.9 | 6.7 | -5.7 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-20 | 16.7 | -14.0 | -27.9 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 4-12 | 25.0 | -3.0 | -46.7 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-11 | 0.0 | -29.0 | -100.0 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 35-42 | 45.5 | 5.8 | -0.8 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 4-7 | 36.4 | -0.5 | -26.4 |  |
| follow_move+money_delta | close | pin limit <$1k | 32-37 | 46.4 | -3.5 | -11.0 |  |
| money_level+money_moving | close | pin limit <$1k | 69-79 | 46.6 | -3.2 | -10.5 |  |
| money_level+sharp_gap | close | pin limit <$1k | 67-72 | 48.2 | -1.6 | -7.5 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 104-114 | 47.7 | -2.0 | -4.4 |  |
| consensus_gap+money_level | close | pin limit <$1k | 27-26 | 50.9 | 0.5 | -5.9 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 14-10 | 58.3 | 9.7 | 27.8 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 36-32 | 52.9 | 3.6 | 6.1 |  |
| follow_move+money_moving | close | pin limit <$1k | 65-74 | 46.8 | -2.9 | -10.1 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 70-73 | 49.0 | -0.8 | -5.9 |  |
| money_level+pin_move | close | pin limit <$1k | 50-48 | 51.0 | 1.1 | -2.6 |  |
| money_level+pin_value | close | pin limit <$1k | 45-34 | 57.0 | 7.3 | 7.8 |  |
| pin_move+pin_value | close | pin limit <$1k | 40-25 | 61.5 | 12.0 | 23.8 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 18-11 | 62.1 | 11.9 | 14.0 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 22-18 | 55.0 | 5.9 | 15.0 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 24-18 | 57.1 | 7.9 | 18.4 |  |
| follow_move+money_level | close | pin limit <$1k | 53-55 | 49.1 | -1.2 | -6.6 |  |
| follow_move+pin_move | close | pin limit <$1k | 60-60 | 50.0 | 0.2 | -4.3 |  |
| follow_move+pin_value | close | pin limit <$1k | 36-24 | 60.0 | 10.3 | 13.9 |  |
| money_moving+pin_move | close | pin limit <$1k | 59-62 | 48.8 | -1.0 | -3.1 |  |
| money_moving+pin_value | close | pin limit <$1k | 36-27 | 57.1 | 7.7 | 15.5 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 62-62 | 50.0 | 0.3 | -0.8 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 38-29 | 56.7 | 7.2 | 14.3 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 38-36 | 51.4 | 1.4 | -1.7 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 26-26 | 50.0 | 0.1 | -4.2 |  |
| money_delta+money_moving | close | pin limit <$1k | 44-45 | 49.4 | -0.3 | -0.4 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 8-6 | 57.1 | 9.0 | 39.2 |  |
| money_delta+money_level | close | pin limit <$1k | 25-19 | 56.8 | 6.7 | 8.8 |  |
| money_delta+pin_value | close | pin limit <$1k | 14-8 | 63.6 | 14.7 | 40.9 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 43-43 | 50.0 | 0.3 | 0.8 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 29-30 | 49.2 | -0.4 | 1.6 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 6-2 | 75.0 | 28.1 | 96.7 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 24-17 | 58.5 | 9.4 | 23.0 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 38-27 | 58.5 | 9.3 | 25.7 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 40-29 | 58.0 | 8.4 | 17.5 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-4 | 82.6 | 33.5 | 76.8 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 41-29 | 58.6 | 9.3 | 24.9 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 5-1 | 83.3 | 33.2 | 57.9 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 13-7 | 65.0 | 14.9 | 24.4 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 10-17 | 37.0 | -12.5 | -29.1 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 21-21 | 50.0 | 0.3 | -4.1 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 32-22 | 59.3 | 9.4 | 14.0 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 45-34 | 57.0 | 7.3 | 10.0 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 26-21 | 55.3 | 5.5 | 6.3 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 20-25 | 44.4 | -5.4 | -14.7 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 41-32 | 56.2 | 6.5 | 8.5 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 32-22 | 59.3 | 9.4 | 14.0 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 14-10 | 58.3 | 9.0 | 11.9 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 32-22 | 59.3 | 9.4 | 14.0 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 22-18 | 55.0 | 5.3 | 5.3 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 45-34 | 57.0 | 7.3 | 10.0 |  |
| money_level+pin_rlm | close | pin limit <$1k | 19-12 | 61.3 | 11.0 | 17.6 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 21-14 | 60.0 | 10.4 | 16.8 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 17-5 | 77.3 | 27.1 | 48.1 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 6-3 | 66.7 | 16.7 | 26.5 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 49.6 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -3.3 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -50.9 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 29-31 | 48.3 | 13.1 | 17.8 | 0.15 |
| rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -14.2 | -3.3 | -0.95 |
| rlm_quiet | early | pin limit <$1k | 5-7 | 41.7 | -2.3 | -15.0 | 0.27 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -49.6 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 5-8 | 38.5 | -9.6 | -31.5 | 0.32 |
| pin_move | early | pin $1-2k | 0-3 | 0.0 | -35.1 | -100.0 | 0.23 |
| pin_move | early | pin limit <$1k | 5-6 | 45.5 | -6.3 | -19.1 | 0.22 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.8 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 8-6 | 57.1 | 17.0 | 26.7 | -0.34 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -39.4 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 4-0 | 100.0 | 50.4 | 88.0 | -0.25 |
| pin_rlm | early | <1k bets | 1-2 | 33.3 | 6.7 | -35.8 | -1.0 |
| pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -26.6 | -100.0 | -1.75 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.3 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -50.9 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 401-329 | 54.9 | 2.8 | -4.3 | 0.18 |
| follow_move | early | pin $1-2k | 28-16 | 63.6 | 10.0 | 14.9 | -0.34 |
| follow_move | early | pin limit <$1k | 47-39 | 54.7 | 4.4 | 1.9 | -0.11 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 25-15 | 62.5 | 25.3 | 36.8 | 0.51 |
| rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.2 | 55.6 | -1.52 |
| rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 0.9 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 42.8 | 59.7 | 0.33 |
| money_level | early | <1k bets | 147-93 | 61.3 | 1.5 | -4.2 | -0.12 |
| money_level | early | pin $1-2k | 20-8 | 71.4 | 5.8 | 4.1 | 0.01 |
| money_level | early | pin limit <$1k | 24-26 | 48.0 | -5.2 | -11.4 | 0.22 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.5 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.0 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 121-102 | 54.3 | 5.8 | 4.5 | 0.35 |
| sharp_gap | early | pin $1-2k | 15-11 | 57.7 | 4.7 | 6.7 | -0.39 |
| sharp_gap | early | pin limit <$1k | 29-18 | 61.7 | 13.1 | 27.9 | 0.12 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.5 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.9 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 81-73 | 52.6 | 0.7 | -8.8 | 0.02 |
| money_moving | early | pin $1-2k | 8-8 | 50.0 | -8.5 | -31.4 | 0.21 |
| money_moving | early | pin limit <$1k | 23-9 | 71.9 | 22.7 | 52.0 | 0.42 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.7 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 36-40 | 47.4 | -0.9 | -10.4 | 0.12 |
| pin_value | early | pin $1-2k | 13-19 | 40.6 | -5.1 | -23.6 | 0.12 |
| pin_value | early | pin limit <$1k | 36-30 | 54.5 | 5.0 | 3.2 | 0.09 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -49.6 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -26.7 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.3 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.8 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 179-237 | 43.0 | -4.7 | -14.6 | 0.37 |
| consensus_gap | early | pin $1-2k | 12-20 | 37.5 | -7.9 | -28.2 | 0.51 |
| consensus_gap | early | pin limit <$1k | 18-34 | 34.6 | -15.5 | -28.2 | 0.28 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.8 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.8 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -0.9 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.0 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 4.7 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.0 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.8 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.4 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.5 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -49.6 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -1.0 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 3.7 | -6.9 | 0.3 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -0.4 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-6 | 53.8 | 6.6 | 0.8 | -0.31 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -3.3 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.0 | -38.9 | -0.67 |
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
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.7 | 56.1 | 0.15 |
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
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 38.1 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 49.6 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 27-33 | 45.0 | -7.1 | -18.9 | 0.79 |
| consensus_gap+money_level | early | <1k bets | 31-22 | 58.5 | -7.6 | -10.1 | 0.44 |
| consensus_gap+sharp_gap | early | <1k bets | 23-38 | 37.7 | -9.5 | -17.1 | 1.02 |
| follow_move+money_level | early | <1k bets | 78-34 | 69.6 | 8.4 | 2.7 | -0.03 |
| follow_move+sharp_gap | early | <1k bets | 66-29 | 69.5 | 19.4 | 23.1 | 0.45 |
| money_level+sharp_gap | early | <1k bets | 81-47 | 63.3 | 6.6 | 3.3 | 0.17 |
| follow_move+money_moving | early | <1k bets | 43-25 | 63.2 | 9.3 | 8.1 | 0.29 |
| money_level+money_moving | early | <1k bets | 51-36 | 58.6 | -0.5 | -8.1 | -0.26 |
| money_moving+sharp_gap | early | <1k bets | 48-41 | 53.9 | 4.3 | -3.1 | 0.2 |
| consensus_gap+money_moving | early | <1k bets | 12-19 | 38.7 | -11.1 | -38.8 | 0.25 |
| follow_move+pin_value | early | <1k bets | 13-11 | 54.2 | 4.5 | 1.3 | -0.01 |
| follow_move+rlm_quiet | early | <1k bets | 29-31 | 48.3 | 13.1 | 17.8 | 0.15 |
| money_moving+rlm_quiet | early | <1k bets | 10-9 | 52.6 | 16.1 | 25.6 | 0.42 |
| rlm_quiet+sharp_gap | early | <1k bets | 18-12 | 60.0 | 24.0 | 33.3 | -0.04 |
| follow_move+rlm_ratio | early | <1k bets | 25-15 | 62.5 | 25.3 | 36.8 | 0.51 |
| rlm_quiet+rlm_ratio | early | <1k bets | 16-9 | 64.0 | 28.0 | 44.7 | -0.02 |
| rlm_ratio+sharp_gap | early | <1k bets | 25-15 | 62.5 | 25.3 | 36.8 | 0.51 |
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
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -50.4 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 1-2 | 33.3 | -17.4 | -36.4 | 1.33 |
| money_level+rlm_ratio | early | <1k bets | 7-6 | 53.8 | 16.3 | 12.9 | 1.69 |
| money_moving+rlm_ratio | early | <1k bets | 10-6 | 62.5 | 21.2 | 41.4 | 0.34 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 50.4 | 90.9 | 0.0 |
| money_delta+money_level | early | <1k bets | 3-1 | 75.0 | 30.8 | 61.5 | 1.2 |
| pin_move+sharp_gap | early | <1k bets | 2-1 | 66.7 | 16.8 | 4.3 | -0.07 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 3-3 | 50.0 | 11.5 | 37.5 | 0.07 |
| money_delta+rlm_quiet | early | <1k bets | 1-2 | 33.3 | -1.2 | 23.3 | -2.8 |
| money_delta+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 32.1 | 111.3 | 0.87 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 49.6 | 90.9 | -1.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 5-4 | 55.6 | -9.3 | -12.6 | 0.71 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -31.5 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 5-10 | 33.3 | -8.0 | -38.7 | 0.31 |
| follow_move+rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -14.2 | -3.3 | -0.95 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.2 | 55.6 | -1.52 |
| follow_move+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 13.8 | 37.5 | -0.83 |
| money_level+money_moving | early | pin $1-2k | 8-5 | 61.5 | -4.3 | -15.6 | 0.07 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.7 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -8.0 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -8.0 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-3 | 40.0 | 3.2 | 55.6 | -1.52 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -39.4 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -39.4 | -100.0 | 2.5 |
| money_level+sharp_gap | early | pin $1-2k | 12-4 | 75.0 | 10.4 | 12.5 | -0.26 |
| money_moving+sharp_gap | early | pin $1-2k | 4-6 | 40.0 | -16.8 | -45.4 | 0.08 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.9 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 4-6 | 40.0 | -10.0 | -31.3 | 0.34 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 0-3 | 0.0 | -26.6 | -100.0 | -0.97 |
| follow_move+pin_value | early | pin $1-2k | 6-5 | 54.5 | 7.1 | 0.8 | -0.3 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -26.6 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 11-4 | 73.3 | 8.2 | 6.6 | -0.07 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 47.9 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 4-1 | 80.0 | 11.7 | 6.9 | -0.18 |
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
| follow_move+rlm_quiet | early | pin limit <$1k | 5-7 | 41.7 | -2.3 | -15.0 | 0.27 |
| money_level+money_moving | early | pin limit <$1k | 13-7 | 65.0 | 12.7 | 20.2 | 0.48 |
| money_level+sharp_gap | early | pin limit <$1k | 20-16 | 55.6 | 4.9 | 1.6 | 0.14 |
| money_moving+sharp_gap | early | pin limit <$1k | 18-5 | 78.3 | 30.2 | 70.1 | 0.35 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -49.6 | -100.0 | -1.0 |
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
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 16.5 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| consensus_gap+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 22.8 | 72.3 | 0.54 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 0.9 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 9-3 | 75.0 | 25.5 | 43.3 | 0.33 |
| money_delta+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_delta+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 52.1 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 3-1 | 75.0 | 25.4 | 41.3 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.0 | 45.3 | -0.5 |
| money_delta+sharp_gap | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 | -0.5 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 11.9 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 24.5 | 51.6 | -0.07 |
| pin_move+pin_value | early | pin limit <$1k | 1-4 | 20.0 | -29.1 | -61.8 | 0.2 |
| follow_move+pin_move | early | pin limit <$1k | 5-3 | 62.5 | 10.3 | 11.2 | 0.42 |
| consensus_gap+pin_move | early | pin limit <$1k | 0-3 | 0.0 | -56.4 | -100.0 | 0.53 |
| money_level+pin_move | early | pin limit <$1k | 2-2 | 50.0 | -5.8 | -21.8 | 0.1 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -50.4 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -50.4 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 16.8 | 4.3 | -0.07 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 49.6 | 90.9 | -1.0 |
| rlm_quiet | close | 1-3k bets | 116-169 | 40.7 | -1.0 | -8.2 |  |
| rlm_quiet | close | 3k+ bets | 44-60 | 42.3 | -0.3 | -8.1 |  |
| rlm_quiet | close | <1k bets | 22-28 | 44.0 | 2.4 | -6.0 |  |
| rlm_quiet | close | pin $1-2k | 46-80 | 36.5 | -6.5 | -16.7 |  |
| rlm_quiet | close | pin $2k+ | 51-62 | 45.1 | 7.4 | -2.5 |  |
| rlm_quiet | close | pin limit <$1k | 36-36 | 50.0 | 0.1 | -4.2 |  |
| pin_move | close | 1-3k bets | 308-303 | 50.4 | 0.5 | -1.8 |  |
| pin_move | close | 3k+ bets | 120-123 | 49.4 | -0.3 | -4.6 |  |
| pin_move | close | <1k bets | 67-68 | 49.6 | -1.0 | -4.6 |  |
| pin_move | close | pin $1-2k | 234-226 | 50.9 | 0.5 | -0.3 |  |
| pin_move | close | pin $2k+ | 174-183 | 48.7 | -0.8 | -7.2 |  |
| pin_move | close | pin limit <$1k | 87-85 | 50.6 | 0.8 | -0.7 |  |
| money_delta | close | 1-3k bets | 199-252 | 44.1 | -0.6 | -6.4 |  |
| money_delta | close | 3k+ bets | 79-109 | 42.0 | -1.1 | -3.3 |  |
| money_delta | close | <1k bets | 38-62 | 38.0 | -4.1 | -22.9 |  |
| money_delta | close | pin $1-2k | 112-115 | 49.3 | 3.6 | 3.3 |  |
| money_delta | close | pin $2k+ | 82-110 | 42.7 | 1.7 | -8.9 |  |
| money_delta | close | pin limit <$1k | 50-54 | 48.1 | -1.7 | -3.7 |  |
| pin_rlm | close | 1-3k bets | 87-92 | 48.6 | 6.0 | 18.3 |  |
| pin_rlm | close | 3k+ bets | 32-44 | 42.1 | -0.0 | -7.9 |  |
| pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| pin_rlm | close | pin $1-2k | 61-64 | 48.8 | 5.0 | 12.7 |  |
| pin_rlm | close | pin $2k+ | 38-64 | 37.3 | 1.9 | -1.9 |  |
| pin_rlm | close | pin limit <$1k | 41-29 | 58.6 | 9.3 | 24.9 |  |
| follow_move | close | 1-3k bets | 547-479 | 53.3 | 1.7 | -4.5 |  |
| follow_move | close | 3k+ bets | 190-177 | 51.8 | -0.2 | -5.2 |  |
| follow_move | close | <1k bets | 120-108 | 52.6 | -0.6 | -11.2 |  |
| follow_move | close | pin $1-2k | 259-280 | 48.1 | -3.1 | -10.5 |  |
| follow_move | close | pin $2k+ | 217-181 | 54.5 | 2.3 | -3.9 |  |
| follow_move | close | pin limit <$1k | 105-104 | 50.2 | 0.2 | -4.1 |  |
| rlm_ratio | close | 1-3k bets | 126-155 | 44.8 | 0.0 | -3.6 |  |
| rlm_ratio | close | 3k+ bets | 48-44 | 52.2 | 7.5 | 11.8 |  |
| rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.9 | 0.8 |  |
| rlm_ratio | close | pin $1-2k | 70-71 | 49.6 | 3.1 | 4.0 |  |
| rlm_ratio | close | pin $2k+ | 38-50 | 43.2 | 5.0 | -4.4 |  |
| rlm_ratio | close | pin limit <$1k | 44-34 | 56.4 | 6.7 | 8.9 |  |
| money_level | close | 1-3k bets | 695-493 | 58.5 | 2.9 | -1.9 |  |
| money_level | close | 3k+ bets | 244-193 | 55.8 | 0.7 | -3.1 |  |
| money_level | close | <1k bets | 145-118 | 55.1 | -0.8 | -11.5 |  |
| money_level | close | pin $1-2k | 317-276 | 53.5 | -0.6 | -4.9 |  |
| money_level | close | pin $2k+ | 275-213 | 56.4 | -1.0 | -7.0 |  |
| money_level | close | pin limit <$1k | 124-121 | 50.6 | 0.5 | -3.8 |  |
| sharp_gap | close | 1-3k bets | 523-620 | 45.8 | -1.7 | -8.3 |  |
| sharp_gap | close | 3k+ bets | 210-218 | 49.1 | 1.7 | 3.4 |  |
| sharp_gap | close | <1k bets | 114-137 | 45.4 | -2.4 | -14.6 |  |
| sharp_gap | close | pin $1-2k | 275-302 | 47.7 | -1.1 | -4.8 |  |
| sharp_gap | close | pin $2k+ | 221-250 | 46.9 | 0.7 | -2.0 |  |
| sharp_gap | close | pin limit <$1k | 115-122 | 48.5 | -1.2 | -3.2 |  |
| money_moving | close | 1-3k bets | 526-619 | 45.9 | -1.9 | -8.8 |  |
| money_moving | close | 3k+ bets | 209-220 | 48.7 | 1.0 | 1.8 |  |
| money_moving | close | <1k bets | 112-137 | 45.0 | -2.5 | -13.5 |  |
| money_moving | close | pin $1-2k | 272-306 | 47.1 | -1.9 | -5.8 |  |
| money_moving | close | pin $2k+ | 222-248 | 47.2 | 1.0 | -2.0 |  |
| money_moving | close | pin limit <$1k | 110-128 | 46.2 | -3.5 | -7.6 |  |
| pin_value | close | 1-3k bets | 217-228 | 48.8 | 1.0 | 0.3 |  |
| pin_value | close | 3k+ bets | 80-85 | 48.5 | -0.0 | -5.0 |  |
| pin_value | close | <1k bets | 54-44 | 55.1 | 8.0 | 10.6 |  |
| pin_value | close | pin $1-2k | 162-182 | 47.1 | -1.1 | -4.5 |  |
| pin_value | close | pin $2k+ | 97-112 | 46.4 | 0.6 | -2.4 |  |
| pin_value | close | pin limit <$1k | 92-63 | 59.4 | 9.7 | 15.4 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 48.0 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 48.0 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 210-275 | 43.3 | -4.5 | -12.3 |  |
| consensus_gap | close | 3k+ bets | 81-95 | 46.0 | -1.4 | 5.1 |  |
| consensus_gap | close | <1k bets | 40-78 | 33.9 | -9.7 | -30.7 |  |
| consensus_gap | close | pin $1-2k | 107-120 | 47.1 | -1.8 | -2.0 |  |
| consensus_gap | close | pin $2k+ | 82-102 | 44.6 | -4.4 | -5.5 |  |
| consensus_gap | close | pin limit <$1k | 49-43 | 53.3 | 3.1 | 4.1 |  |
| consensus_gap+follow_move | close | 1-3k bets | 88-80 | 52.4 | 0.5 | -1.3 |  |
| consensus_gap+money_level | close | 1-3k bets | 141-94 | 60.0 | 1.2 | 2.9 |  |
| consensus_gap+money_moving | close | 1-3k bets | 98-150 | 39.5 | -5.5 | -9.8 |  |
| consensus_gap+pin_move | close | 1-3k bets | 53-51 | 51.0 | -0.5 | 4.5 |  |
| consensus_gap+pin_value | close | 1-3k bets | 84-99 | 45.9 | 0.3 | -1.9 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 96-153 | 38.6 | -5.7 | -10.9 |  |
| follow_move+money_level | close | 1-3k bets | 371-252 | 59.6 | 3.2 | -2.8 |  |
| follow_move+money_moving | close | 1-3k bets | 302-317 | 48.8 | -0.7 | -6.7 |  |
| follow_move+pin_move | close | 1-3k bets | 222-220 | 50.2 | 0.0 | -4.6 |  |
| follow_move+pin_value | close | 1-3k bets | 73-74 | 49.7 | 1.2 | -5.9 |  |
| follow_move+sharp_gap | close | 1-3k bets | 303-315 | 49.0 | -0.1 | -5.3 |  |
| money_level+money_moving | close | 1-3k bets | 379-333 | 53.2 | 0.8 | -3.3 |  |
| money_level+pin_move | close | 1-3k bets | 193-172 | 52.9 | 0.1 | -3.5 |  |
| money_level+pin_value | close | 1-3k bets | 110-98 | 52.9 | 3.3 | -0.8 |  |
| money_level+sharp_gap | close | 1-3k bets | 368-326 | 53.0 | 0.9 | -2.8 |  |
| money_moving+pin_move | close | 1-3k bets | 192-204 | 48.5 | -0.6 | -2.3 |  |
| money_moving+pin_value | close | 1-3k bets | 99-119 | 45.4 | -1.8 | -5.5 |  |
| money_moving+sharp_gap | close | 1-3k bets | 500-592 | 45.8 | -1.7 | -7.9 |  |
| pin_move+pin_value | close | 1-3k bets | 99-96 | 50.8 | 1.7 | 0.0 |  |
| pin_move+sharp_gap | close | 1-3k bets | 199-203 | 49.5 | 0.6 | 0.1 |  |
| pin_value+sharp_gap | close | 1-3k bets | 101-123 | 45.1 | -2.0 | -6.3 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 116-169 | 40.7 | -1.0 | -8.2 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 62-104 | 37.3 | -4.4 | -11.0 |  |
| consensus_gap+money_delta | close | 1-3k bets | 25-65 | 27.8 | -9.5 | -24.2 |  |
| follow_move+money_delta | close | 1-3k bets | 95-109 | 46.6 | -0.4 | -7.4 |  |
| money_delta+money_level | close | 1-3k bets | 74-72 | 50.7 | 2.7 | 5.0 |  |
| money_delta+money_moving | close | 1-3k bets | 139-202 | 40.8 | -2.3 | -10.1 |  |
| money_delta+pin_value | close | 1-3k bets | 44-44 | 50.0 | 2.6 | 0.2 |  |
| money_delta+sharp_gap | close | 1-3k bets | 138-200 | 40.8 | -2.3 | -9.9 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 70-77 | 47.6 | 0.1 | 2.1 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 17-26 | 39.5 | 1.6 | 19.2 |  |
| money_level+pin_rlm | close | 1-3k bets | 39-28 | 58.2 | 9.8 | 12.1 |  |
| pin_move+pin_rlm | close | 1-3k bets | 79-76 | 51.0 | 6.2 | 13.7 |  |
| pin_rlm+pin_value | close | 1-3k bets | 29-24 | 54.7 | 8.6 | 30.7 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 87-92 | 48.6 | 6.0 | 18.3 |  |
| money_delta+pin_rlm | close | 1-3k bets | 49-53 | 48.0 | 4.5 | 15.3 |  |
| money_moving+pin_rlm | close | 1-3k bets | 82-89 | 48.0 | 5.3 | 18.0 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 19-30 | 38.8 | -1.6 | 4.1 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 126-155 | 44.8 | 0.0 | -3.6 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 66-77 | 46.2 | 0.1 | -6.8 |  |
| money_level+rlm_ratio | close | 1-3k bets | 59-56 | 51.3 | 1.7 | -1.0 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 120-150 | 44.4 | -0.5 | -4.1 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 126-155 | 44.8 | 0.0 | -3.6 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 12-30 | 28.6 | -7.0 | -7.2 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 55-103 | 34.8 | -6.8 | -15.6 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 50-88 | 36.2 | -3.9 | -9.9 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 52-66 | 44.1 | 0.0 | -5.5 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 31-53 | 36.9 | -6.6 | -21.6 |  |
| follow_move+pin_rlm | close | 1-3k bets | 62-70 | 47.0 | 2.3 | -2.5 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 67-65 | 50.8 | 4.7 | 4.7 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 24-41 | 36.9 | -3.2 | -14.6 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 62-70 | 47.0 | 2.3 | -2.5 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 25-21 | 54.3 | 6.5 | 4.5 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 14-20 | 41.2 | -4.1 | -19.8 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 49.6 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 30-27 | 52.6 | 2.9 | 3.3 |  |
| consensus_gap+money_moving | close | 3k+ bets | 33-52 | 38.8 | -5.2 | 14.5 |  |
| consensus_gap+pin_move | close | 3k+ bets | 21-19 | 52.5 | 2.2 | 6.4 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-6 | 33.3 | -6.4 | 6.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 34-33 | 50.7 | 4.3 | 4.3 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -0.7 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 34-52 | 39.5 | -4.3 | 17.6 |  |
| follow_move+money_moving | close | 3k+ bets | 101-106 | 48.8 | -0.4 | -4.1 |  |
| follow_move+pin_move | close | 3k+ bets | 91-89 | 50.6 | 0.5 | -1.8 |  |
| follow_move+pin_rlm | close | 3k+ bets | 30-30 | 50.0 | 5.8 | 10.3 |  |
| follow_move+pin_value | close | 3k+ bets | 32-32 | 50.0 | 0.1 | -6.2 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 48-44 | 52.2 | 7.5 | 11.8 |  |
| follow_move+sharp_gap | close | 3k+ bets | 103-105 | 49.5 | 0.8 | -2.0 |  |
| money_moving+pin_move | close | 3k+ bets | 70-80 | 46.7 | -1.5 | -7.1 |  |
| money_moving+pin_rlm | close | 3k+ bets | 31-43 | 41.9 | 0.0 | -8.1 |  |
| money_moving+pin_value | close | 3k+ bets | 39-48 | 44.8 | -2.6 | -7.9 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 46-42 | 52.3 | 7.6 | 12.4 |  |
| money_moving+sharp_gap | close | 3k+ bets | 202-210 | 49.0 | 1.6 | 3.2 |  |
| pin_move+pin_rlm | close | 3k+ bets | 31-38 | 44.9 | 1.2 | -1.5 |  |
| pin_move+pin_value | close | 3k+ bets | 32-39 | 45.1 | -4.4 | -15.2 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 33-31 | 51.6 | 6.2 | 12.1 |  |
| pin_move+sharp_gap | close | 3k+ bets | 70-80 | 46.7 | -1.1 | -6.4 |  |
| pin_rlm+pin_value | close | 3k+ bets | 6-14 | 30.0 | -15.9 | -42.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 30-30 | 50.0 | 5.8 | 10.3 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 32-44 | 42.1 | -0.0 | -7.9 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 9-9 | 50.0 | -0.3 | -5.1 |  |
| pin_value+sharp_gap | close | 3k+ bets | 39-47 | 45.3 | -2.1 | -6.8 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 48-44 | 52.2 | 7.5 | 11.8 |  |
| follow_move+money_delta | close | 3k+ bets | 38-47 | 44.7 | -0.5 | -7.2 |  |
| money_level+money_moving | close | 3k+ bets | 142-121 | 54.0 | 1.9 | 0.0 |  |
| money_level+sharp_gap | close | 3k+ bets | 141-118 | 54.4 | 2.5 | 1.5 |  |
| follow_move+money_level | close | 3k+ bets | 119-90 | 56.9 | 0.6 | -3.4 |  |
| money_level+rlm_ratio | close | 3k+ bets | 23-12 | 65.7 | 18.8 | 35.2 |  |
| consensus_gap+money_level | close | 3k+ bets | 44-44 | 50.0 | -6.5 | -13.3 |  |
| money_level+pin_move | close | 3k+ bets | 66-61 | 52.0 | -1.5 | -4.5 |  |
| money_level+pin_value | close | 3k+ bets | 44-43 | 50.6 | 0.3 | -6.3 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 7-12 | 36.8 | -0.8 | -5.4 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 44-60 | 42.3 | -0.3 | -8.1 |  |
| money_delta+money_moving | close | 3k+ bets | 60-83 | 42.0 | -0.2 | 1.4 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 19-24 | 44.2 | 2.7 | 2.2 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 23-32 | 41.8 | -0.3 | -6.0 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 21-31 | 40.4 | -1.7 | -8.0 |  |
| consensus_gap+money_delta | close | 3k+ bets | 12-23 | 34.3 | -3.9 | 18.4 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 10-24 | 29.4 | -13.2 | -34.9 |  |
| money_delta+sharp_gap | close | 3k+ bets | 58-80 | 42.0 | 0.0 | 2.1 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 25-29 | 46.3 | 2.5 | 0.7 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 11-16 | 40.7 | -0.9 | -3.2 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 7-11 | 38.9 | -11.1 | -25.7 |  |
| money_delta+money_level | close | 3k+ bets | 31-22 | 58.5 | 12.6 | 18.5 |  |
| money_level+pin_rlm | close | 3k+ bets | 15-9 | 62.5 | 17.9 | 34.6 |  |
| money_delta+pin_value | close | 3k+ bets | 18-19 | 48.6 | 2.8 | -8.3 |  |
| money_delta+pin_move | close | 3k+ bets | 35-41 | 46.1 | 0.9 | -5.8 |  |
| money_delta+pin_rlm | close | 3k+ bets | 21-27 | 43.8 | 2.1 | -6.6 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 28-24 | 53.8 | 9.4 | 14.8 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 48.0 | 87.7 |  |
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
| pin_move+sharp_gap | close | <1k bets | 36-42 | 46.2 | -2.4 | -9.5 |  |
| pin_value+sharp_gap | close | <1k bets | 17-15 | 53.1 | 7.2 | 18.5 |  |
| follow_move+money_delta | close | <1k bets | 18-20 | 47.4 | 4.8 | -3.2 |  |
| follow_move+money_moving | close | <1k bets | 54-63 | 46.2 | -3.5 | -13.8 |  |
| follow_move+pin_move | close | <1k bets | 42-42 | 50.0 | -1.4 | -7.2 |  |
| follow_move+sharp_gap | close | <1k bets | 56-63 | 47.1 | -3.4 | -16.1 |  |
| money_delta+money_moving | close | <1k bets | 27-46 | 37.0 | -3.0 | -23.1 |  |
| money_delta+pin_move | close | <1k bets | 13-17 | 43.3 | -0.6 | -15.5 |  |
| money_delta+sharp_gap | close | <1k bets | 27-46 | 37.0 | -3.0 | -23.1 |  |
| follow_move+rlm_quiet | close | <1k bets | 22-28 | 44.0 | 2.4 | -6.0 |  |
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
| pin_move+rlm_quiet | close | <1k bets | 10-10 | 50.0 | 4.7 | 9.6 |  |
| pin_move+rlm_ratio | close | <1k bets | 16-13 | 55.2 | 10.1 | 7.8 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 21.4 | 60.8 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 7-5 | 58.3 | 16.0 | 15.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 16-11 | 59.3 | 16.2 | 17.3 |  |
| pin_value+rlm_quiet | close | <1k bets | 3-4 | 42.9 | -6.6 | -17.6 |  |
| pin_value+rlm_ratio | close | <1k bets | 4-1 | 80.0 | 30.6 | 51.7 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 2-7 | 22.2 | -11.9 | -57.2 |  |
| money_delta+money_level | close | <1k bets | 12-17 | 41.4 | -2.1 | -18.9 |  |
| money_level+rlm_ratio | close | <1k bets | 13-13 | 50.0 | 4.6 | -1.9 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 17.6 | 19.0 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 0-5 | 0.0 | -35.6 | -100.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 41-46 | 47.1 | -5.1 | -9.7 |  |
| consensus_gap+money_moving | close | pin $1-2k | 54-65 | 45.4 | -2.9 | -3.4 |  |
| consensus_gap+pin_move | close | pin $1-2k | 43-43 | 50.0 | -2.5 | 5.6 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-18 | 41.9 | 1.1 | 25.8 |  |
| consensus_gap+pin_value | close | pin $1-2k | 64-70 | 47.8 | 1.9 | -4.1 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-14 | 50.0 | 4.5 | 9.0 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 52-63 | 45.2 | -1.8 | -2.5 |  |
| follow_move+money_moving | close | pin $1-2k | 152-183 | 45.4 | -4.5 | -11.0 |  |
| follow_move+pin_move | close | pin $1-2k | 165-169 | 49.4 | -1.3 | -5.1 |  |
| follow_move+pin_rlm | close | pin $1-2k | 49-48 | 50.5 | 4.5 | 6.6 |  |
| follow_move+pin_value | close | pin $1-2k | 56-65 | 46.3 | -3.2 | -12.7 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 70-71 | 49.6 | 3.1 | 4.0 |  |
| follow_move+sharp_gap | close | pin $1-2k | 155-181 | 46.1 | -3.6 | -9.9 |  |
| money_moving+pin_move | close | pin $1-2k | 145-160 | 47.5 | -1.8 | -3.3 |  |
| money_moving+pin_rlm | close | pin $1-2k | 58-62 | 48.3 | 4.2 | 12.2 |  |
| money_moving+pin_value | close | pin $1-2k | 66-95 | 41.0 | -6.9 | -19.7 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 68-68 | 50.0 | 3.1 | 4.6 |  |
| money_moving+sharp_gap | close | pin $1-2k | 264-294 | 47.3 | -1.4 | -5.2 |  |
| pin_move+pin_rlm | close | pin $1-2k | 58-58 | 50.0 | 4.8 | 12.8 |  |
| pin_move+pin_value | close | pin $1-2k | 71-86 | 45.2 | -4.4 | -12.7 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 57-52 | 52.3 | 5.2 | 8.4 |  |
| pin_move+sharp_gap | close | pin $1-2k | 148-159 | 48.2 | -0.9 | -2.4 |  |
| pin_rlm+pin_value | close | pin $1-2k | 15-24 | 38.5 | -9.9 | -19.7 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 49-48 | 50.5 | 4.5 | 6.6 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 61-64 | 48.8 | 5.0 | 12.7 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 18-20 | 47.4 | -2.5 | -10.6 |  |
| pin_value+sharp_gap | close | pin $1-2k | 66-93 | 41.5 | -6.2 | -18.7 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 70-71 | 49.6 | 3.1 | 4.0 |  |
| follow_move+money_level | close | pin $1-2k | 180-168 | 51.7 | -2.7 | -9.4 |  |
| money_level+rlm_ratio | close | pin $1-2k | 40-32 | 55.6 | 7.0 | 8.4 |  |
| money_level+sharp_gap | close | pin $1-2k | 197-191 | 50.8 | -1.0 | -5.7 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 3-11 | 21.4 | -20.4 | -31.6 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 46-80 | 36.5 | -6.5 | -16.7 |  |
| money_level+money_moving | close | pin $1-2k | 197-195 | 50.3 | -1.7 | -6.7 |  |
| consensus_gap+money_level | close | pin $1-2k | 63-56 | 52.9 | -3.9 | -6.4 |  |
| money_level+pin_value | close | pin $1-2k | 74-77 | 49.0 | -0.9 | -8.3 |  |
| money_level+pin_move | close | pin $1-2k | 144-132 | 52.2 | -0.7 | -4.7 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 23-37 | 38.3 | -5.6 | -4.8 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 33-44 | 42.9 | -2.4 | -2.1 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 15-25 | 37.5 | -6.8 | -8.4 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 20-31 | 39.2 | -4.1 | -3.2 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 24-38 | 38.7 | -5.1 | -7.2 |  |
| money_level+pin_rlm | close | pin $1-2k | 29-22 | 56.9 | 10.3 | 11.8 |  |
| follow_move+money_delta | close | pin $1-2k | 54-55 | 49.5 | 3.4 | 2.3 |  |
| money_delta+money_moving | close | pin $1-2k | 77-92 | 45.6 | 1.2 | -1.0 |  |
| money_delta+pin_move | close | pin $1-2k | 58-61 | 48.7 | 1.4 | 3.6 |  |
| money_delta+pin_rlm | close | pin $1-2k | 37-41 | 47.4 | 3.9 | 9.9 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 42-40 | 51.2 | 5.2 | 7.9 |  |
| money_delta+sharp_gap | close | pin $1-2k | 77-90 | 46.1 | 1.7 | 0.2 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 48.0 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 42-36 | 53.8 | 5.9 | 4.8 |  |
| consensus_gap+money_delta | close | pin $1-2k | 16-26 | 38.1 | -2.5 | -10.1 |  |
| money_delta+pin_value | close | pin $1-2k | 37-42 | 46.8 | -1.6 | -11.5 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 12-24 | 33.3 | -9.1 | -17.6 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 8-21 | 27.6 | -21.6 | -47.0 |  |
| follow_move+money_level | close | pin $2k+ | 138-87 | 61.3 | 1.9 | -2.0 |  |
| follow_move+money_moving | close | pin $2k+ | 106-102 | 51.0 | 3.1 | -2.5 |  |
| follow_move+pin_move | close | pin $2k+ | 131-122 | 51.8 | 1.8 | -2.5 |  |
| follow_move+sharp_gap | close | pin $2k+ | 107-103 | 51.0 | 3.2 | -2.2 |  |
| money_level+money_moving | close | pin $2k+ | 149-131 | 53.2 | 0.5 | -3.4 |  |
| money_level+pin_move | close | pin $2k+ | 100-88 | 53.2 | -2.0 | -6.0 |  |
| money_level+sharp_gap | close | pin $2k+ | 149-132 | 53.0 | 0.3 | -3.4 |  |
| money_moving+pin_move | close | pin $2k+ | 95-103 | 48.0 | 0.8 | -4.2 |  |
| money_moving+sharp_gap | close | pin $2k+ | 216-244 | 47.0 | 0.8 | -1.9 |  |
| pin_move+sharp_gap | close | pin $2k+ | 95-104 | 47.7 | 0.6 | -4.2 |  |
| consensus_gap+money_delta | close | pin $2k+ | 7-25 | 21.9 | -9.9 | -56.9 |  |
| consensus_gap+money_moving | close | pin $2k+ | 30-58 | 34.1 | -8.5 | -6.7 |  |
| consensus_gap+pin_value | close | pin $2k+ | 33-45 | 42.3 | 1.0 | 6.4 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 32-61 | 34.4 | -8.8 | -6.2 |  |
| money_delta+money_moving | close | pin $2k+ | 56-78 | 41.8 | 3.4 | -6.8 |  |
| money_delta+pin_value | close | pin $2k+ | 18-21 | 46.2 | 3.6 | -11.8 |  |
| money_delta+sharp_gap | close | pin $2k+ | 54-77 | 41.2 | 2.8 | -7.9 |  |
| money_moving+pin_value | close | pin $2k+ | 54-63 | 46.2 | 1.2 | 6.0 |  |
| pin_value+sharp_gap | close | pin $2k+ | 54-64 | 45.8 | 1.0 | 5.1 |  |
| consensus_gap+pin_move | close | pin $2k+ | 23-30 | 43.4 | -6.2 | -17.5 |  |
| money_delta+pin_move | close | pin $2k+ | 31-44 | 41.3 | -1.1 | -14.8 |  |
| consensus_gap+follow_move | close | pin $2k+ | 26-26 | 50.0 | -1.6 | -15.9 |  |
| follow_move+pin_value | close | pin $2k+ | 32-30 | 51.6 | 4.5 | -2.3 |  |
| pin_move+pin_value | close | pin $2k+ | 45-44 | 50.6 | 2.9 | -0.6 |  |
| follow_move+money_delta | close | pin $2k+ | 31-37 | 45.6 | 3.7 | -5.3 |  |
| follow_move+pin_rlm | close | pin $2k+ | 27-41 | 39.7 | 2.1 | -9.3 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 38-50 | 43.2 | 5.0 | -4.4 |  |
| money_delta+money_level | close | pin $2k+ | 24-20 | 54.5 | 11.0 | 10.6 |  |
| money_delta+pin_rlm | close | pin $2k+ | 21-36 | 36.8 | 1.4 | -8.3 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 19-22 | 46.3 | 7.7 | 0.7 |  |
| money_level+pin_rlm | close | pin $2k+ | 15-9 | 62.5 | 20.1 | 32.4 |  |
| money_level+pin_value | close | pin $2k+ | 53-49 | 52.0 | 2.1 | -4.0 |  |
| money_level+rlm_ratio | close | pin $2k+ | 14-11 | 56.0 | 9.7 | 17.6 |  |
| money_moving+pin_rlm | close | pin $2k+ | 38-64 | 37.3 | 1.9 | -1.9 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 38-49 | 43.7 | 5.3 | -3.3 |  |
| pin_move+pin_rlm | close | pin $2k+ | 31-43 | 41.9 | 3.9 | -1.9 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 27-35 | 43.5 | 3.7 | -0.6 |  |
| pin_rlm+pin_value | close | pin $2k+ | 6-13 | 31.6 | -4.2 | 13.6 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 27-41 | 39.7 | 2.1 | -9.3 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 38-64 | 37.3 | 1.9 | -1.9 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 4-6 | 40.0 | -0.9 | -19.0 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 38-50 | 43.2 | 5.0 | -4.4 |  |
| consensus_gap+money_level | close | pin $2k+ | 53-44 | 54.6 | -8.2 | -15.0 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 51-62 | 45.1 | 7.4 | -2.5 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 16-20 | 44.4 | 5.7 | -7.5 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 26-35 | 42.6 | 7.3 | -4.2 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 13-27 | 32.5 | 0.4 | -20.0 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 20-32 | 38.5 | 5.9 | -9.7 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 26-36 | 41.9 | 6.7 | -5.7 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-19 | 17.4 | -11.3 | -24.8 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 4-12 | 25.0 | -2.9 | -46.7 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-11 | 0.0 | -28.9 | -100.0 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 34-40 | 45.9 | 6.1 | -0.0 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 4-7 | 36.4 | -0.5 | -26.4 |  |
| follow_move+money_delta | close | pin limit <$1k | 31-37 | 45.6 | -4.3 | -12.5 |  |
| money_level+money_moving | close | pin limit <$1k | 68-77 | 46.9 | -2.9 | -10.0 |  |
| money_level+sharp_gap | close | pin limit <$1k | 67-71 | 48.6 | -1.3 | -6.8 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 103-113 | 47.7 | -2.0 | -4.4 |  |
| consensus_gap+money_level | close | pin limit <$1k | 27-25 | 51.9 | 1.4 | -4.1 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 14-10 | 58.3 | 9.7 | 27.8 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 35-31 | 53.0 | 3.8 | 6.4 |  |
| follow_move+money_moving | close | pin limit <$1k | 64-73 | 46.7 | -3.0 | -10.2 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 69-73 | 48.6 | -1.1 | -6.6 |  |
| money_level+pin_move | close | pin limit <$1k | 49-48 | 50.5 | 0.6 | -3.5 |  |
| money_level+pin_value | close | pin limit <$1k | 45-32 | 58.4 | 8.8 | 10.6 |  |
| pin_move+pin_value | close | pin limit <$1k | 40-25 | 61.5 | 12.0 | 23.8 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 17-10 | 63.0 | 12.7 | 15.4 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 21-17 | 55.3 | 6.2 | 16.0 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 23-18 | 56.1 | 6.9 | 16.7 |  |
| follow_move+money_level | close | pin limit <$1k | 53-54 | 49.5 | -0.7 | -5.7 |  |
| follow_move+pin_move | close | pin limit <$1k | 59-60 | 49.6 | -0.3 | -5.1 |  |
| follow_move+pin_value | close | pin limit <$1k | 35-23 | 60.3 | 10.7 | 14.5 |  |
| money_moving+pin_move | close | pin limit <$1k | 58-62 | 48.3 | -1.4 | -3.8 |  |
| money_moving+pin_value | close | pin limit <$1k | 35-25 | 58.3 | 9.0 | 18.1 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 62-62 | 50.0 | 0.2 | -0.8 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 37-28 | 56.9 | 7.4 | 14.9 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 36-36 | 50.0 | 0.1 | -4.2 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 25-26 | 49.0 | -0.8 | -6.1 |  |
| money_delta+money_moving | close | pin limit <$1k | 43-45 | 48.9 | -0.8 | -1.4 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 7-6 | 53.8 | 5.8 | 35.2 |  |
| money_delta+money_level | close | pin limit <$1k | 25-19 | 56.8 | 6.7 | 8.8 |  |
| money_delta+pin_value | close | pin limit <$1k | 13-8 | 61.9 | 13.0 | 38.5 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 42-43 | 49.4 | -0.3 | -0.3 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 29-30 | 49.2 | -0.4 | 1.6 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 6-2 | 75.0 | 28.1 | 96.7 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 24-17 | 58.5 | 9.4 | 23.0 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 38-27 | 58.5 | 9.3 | 25.7 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 40-29 | 58.0 | 8.4 | 17.5 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-4 | 82.6 | 33.5 | 76.8 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 41-29 | 58.6 | 9.3 | 24.9 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 4-1 | 80.0 | 29.9 | 51.3 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 12-7 | 63.2 | 13.0 | 20.9 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 9-17 | 34.6 | -14.9 | -33.8 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 20-21 | 48.8 | -0.9 | -6.4 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 32-22 | 59.3 | 9.4 | 14.0 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 44-34 | 56.4 | 6.7 | 8.9 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 25-21 | 54.3 | 4.5 | 4.4 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 19-25 | 43.2 | -6.7 | -17.1 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 40-32 | 55.6 | 5.9 | 7.4 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 32-22 | 59.3 | 9.4 | 14.0 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 14-10 | 58.3 | 9.0 | 11.9 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 32-22 | 59.3 | 9.4 | 14.0 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 21-18 | 53.8 | 4.1 | 3.2 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 44-34 | 56.4 | 6.7 | 8.9 |  |
| money_level+pin_rlm | close | pin limit <$1k | 19-12 | 61.3 | 11.0 | 17.6 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 21-14 | 60.0 | 10.4 | 16.8 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 16-5 | 76.2 | 26.0 | 46.1 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 5-3 | 62.5 | 12.6 | 18.4 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 49.6 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -3.3 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -50.8 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 28-29 | 49.1 | 13.8 | 20.7 | 0.2 |
| rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -14.2 | -3.3 | -0.95 |
| rlm_quiet | early | pin limit <$1k | 5-7 | 41.7 | -2.3 | -15.0 | 0.27 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -49.6 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 5-8 | 38.5 | -9.6 | -31.5 | 0.32 |
| pin_move | early | pin $1-2k | 0-3 | 0.0 | -35.1 | -100.0 | 0.23 |
| pin_move | early | pin limit <$1k | 5-6 | 45.5 | -6.3 | -19.1 | 0.22 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.8 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 8-6 | 57.1 | 17.0 | 26.7 | -0.34 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -39.3 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 4-0 | 100.0 | 50.4 | 88.0 | -0.25 |
| pin_rlm | early | <1k bets | 1-2 | 33.3 | 6.7 | -35.8 | -1.0 |
| pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -26.6 | -100.0 | -1.75 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.3 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -50.8 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 395-325 | 54.9 | 2.6 | -4.8 | 0.2 |
| follow_move | early | pin $1-2k | 27-16 | 62.8 | 8.5 | 11.9 | -0.35 |
| follow_move | early | pin limit <$1k | 47-39 | 54.7 | 4.4 | 1.9 | -0.11 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.0 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 24-14 | 63.2 | 26.0 | 39.0 | 0.52 |
| rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.2 | 55.6 | -1.52 |
| rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 0.9 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 42.8 | 59.7 | 0.33 |
| money_level | early | <1k bets | 141-90 | 61.0 | 1.3 | -4.7 | -0.15 |
| money_level | early | pin $1-2k | 20-8 | 71.4 | 5.8 | 4.1 | 0.01 |
| money_level | early | pin limit <$1k | 24-26 | 48.0 | -5.3 | -11.4 | 0.22 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.5 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.1 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 117-99 | 54.2 | 5.7 | 4.5 | 0.34 |
| sharp_gap | early | pin $1-2k | 15-11 | 57.7 | 4.8 | 6.7 | -0.39 |
| sharp_gap | early | pin limit <$1k | 29-18 | 61.7 | 13.1 | 27.9 | 0.12 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.5 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.8 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 78-71 | 52.3 | 0.7 | -9.0 | 0.01 |
| money_moving | early | pin $1-2k | 8-8 | 50.0 | -8.5 | -31.4 | 0.21 |
| money_moving | early | pin limit <$1k | 23-9 | 71.9 | 22.7 | 52.0 | 0.42 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.7 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 36-39 | 48.0 | -0.3 | -9.2 | 0.13 |
| pin_value | early | pin $1-2k | 13-18 | 41.9 | -3.8 | -21.1 | 0.12 |
| pin_value | early | pin limit <$1k | 36-30 | 54.5 | 5.0 | 3.2 | 0.09 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -49.6 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -26.6 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.3 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.7 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 176-236 | 42.7 | -4.7 | -14.8 | 0.37 |
| consensus_gap | early | pin $1-2k | 12-20 | 37.5 | -7.9 | -28.2 | 0.51 |
| consensus_gap | early | pin limit <$1k | 18-34 | 34.6 | -15.5 | -28.2 | 0.28 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -52.0 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.8 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.8 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -0.8 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.0 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 4.7 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.0 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.8 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.4 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.5 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -49.6 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -1.1 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 3.6 | -6.9 | 0.3 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -0.4 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-6 | 53.8 | 6.5 | 0.8 | -0.31 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -3.3 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.1 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.3 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.5 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 2.7 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.5 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.6 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.0 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.6 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 52.0 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 12.3 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 19.0 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 17.7 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 17.7 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| follow_move+rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -50.8 | -100.0 | -0.5 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.0 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.0 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.8 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| rlm_quiet+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.0 | -100.0 | -1.0 |
| rlm_quiet+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.0 | -100.0 | -1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.0 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 38.1 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 49.6 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 26-33 | 44.1 | -7.7 | -19.4 | 0.84 |
| consensus_gap+money_level | early | <1k bets | 28-21 | 57.1 | -8.4 | -10.9 | 0.38 |
| consensus_gap+sharp_gap | early | <1k bets | 22-38 | 36.7 | -10.1 | -18.6 | 1.0 |
| follow_move+money_level | early | <1k bets | 76-33 | 69.7 | 8.3 | 2.7 | -0.01 |
| follow_move+sharp_gap | early | <1k bets | 64-28 | 69.6 | 19.2 | 23.0 | 0.46 |
| money_level+sharp_gap | early | <1k bets | 79-47 | 62.7 | 6.1 | 2.0 | 0.15 |
| follow_move+money_moving | early | <1k bets | 41-24 | 63.1 | 9.3 | 8.5 | 0.32 |
| money_level+money_moving | early | <1k bets | 49-35 | 58.3 | -0.6 | -8.2 | -0.27 |
| money_moving+sharp_gap | early | <1k bets | 46-41 | 52.9 | 3.6 | -5.0 | 0.17 |
| consensus_gap+money_moving | early | <1k bets | 10-19 | 34.5 | -13.7 | -44.4 | 0.26 |
| follow_move+pin_value | early | <1k bets | 13-11 | 54.2 | 4.5 | 1.3 | -0.01 |
| follow_move+rlm_quiet | early | <1k bets | 28-29 | 49.1 | 13.8 | 20.7 | 0.2 |
| money_moving+rlm_quiet | early | <1k bets | 9-9 | 50.0 | 14.3 | 22.0 | 0.38 |
| rlm_quiet+sharp_gap | early | <1k bets | 17-11 | 60.7 | 24.9 | 36.0 | -0.07 |
| follow_move+rlm_ratio | early | <1k bets | 24-14 | 63.2 | 26.0 | 39.0 | 0.52 |
| rlm_quiet+rlm_ratio | early | <1k bets | 15-8 | 65.2 | 29.4 | 49.0 | -0.05 |
| rlm_ratio+sharp_gap | early | <1k bets | 24-14 | 63.2 | 26.0 | 39.0 | 0.52 |
| pin_move+pin_value | early | <1k bets | 1-4 | 20.0 | -29.1 | -61.8 | 0.2 |
| follow_move+pin_move | early | <1k bets | 5-3 | 62.5 | 10.2 | 11.2 | 0.42 |
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
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -50.4 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 1-2 | 33.3 | -17.3 | -36.4 | 1.33 |
| money_level+rlm_ratio | early | <1k bets | 7-6 | 53.8 | 16.3 | 12.9 | 1.69 |
| money_moving+rlm_ratio | early | <1k bets | 9-6 | 60.0 | 19.4 | 38.2 | 0.3 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 50.4 | 90.9 | 0.0 |
| money_delta+money_level | early | <1k bets | 3-1 | 75.0 | 30.8 | 61.5 | 1.2 |
| pin_move+sharp_gap | early | <1k bets | 2-1 | 66.7 | 16.8 | 4.3 | -0.07 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 3-3 | 50.0 | 11.5 | 37.5 | 0.07 |
| money_delta+rlm_quiet | early | <1k bets | 1-2 | 33.3 | -1.2 | 23.3 | -2.8 |
| money_delta+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 32.2 | 111.3 | 0.87 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 49.6 | 90.9 | -1.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 5-4 | 55.6 | -9.4 | -12.6 | 0.71 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -31.6 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 5-10 | 33.3 | -8.0 | -38.7 | 0.31 |
| follow_move+rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -14.2 | -3.3 | -0.95 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.2 | 55.6 | -1.52 |
| follow_move+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 13.8 | 37.5 | -0.83 |
| money_level+money_moving | early | pin $1-2k | 8-5 | 61.5 | -4.4 | -15.6 | 0.07 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.8 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -8.0 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -8.0 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-3 | 40.0 | 3.2 | 55.6 | -1.52 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -52.0 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -39.3 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -52.0 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -39.3 | -100.0 | 2.5 |
| money_level+sharp_gap | early | pin $1-2k | 12-4 | 75.0 | 10.4 | 12.5 | -0.26 |
| money_moving+sharp_gap | early | pin $1-2k | 4-6 | 40.0 | -16.8 | -45.4 | 0.08 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.9 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 4-6 | 40.0 | -10.0 | -31.3 | 0.34 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 0-3 | 0.0 | -26.6 | -100.0 | -0.97 |
| follow_move+pin_value | early | pin $1-2k | 6-5 | 54.5 | 7.0 | 0.8 | -0.3 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -26.6 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 11-4 | 73.3 | 8.1 | 6.6 | -0.07 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 48.0 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 4-1 | 80.0 | 11.7 | 6.9 | -0.18 |
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
| follow_move+rlm_quiet | early | pin limit <$1k | 5-7 | 41.7 | -2.3 | -15.0 | 0.27 |
| money_level+money_moving | early | pin limit <$1k | 13-7 | 65.0 | 12.7 | 20.2 | 0.48 |
| money_level+sharp_gap | early | pin limit <$1k | 20-16 | 55.6 | 4.9 | 1.6 | 0.14 |
| money_moving+sharp_gap | early | pin limit <$1k | 18-5 | 78.3 | 30.2 | 70.1 | 0.35 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -49.6 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 9-6 | 60.0 | 9.9 | 13.8 | 0.33 |
| money_moving+pin_value | early | pin limit <$1k | 7-4 | 63.6 | 13.8 | 20.1 | 0.18 |
| pin_value+sharp_gap | early | pin limit <$1k | 12-6 | 66.7 | 16.7 | 26.4 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-9 | 40.0 | -12.1 | -25.7 | 0.53 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -26.7 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 14-18 | 43.8 | -5.2 | -17.9 | 0.43 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.1 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 11-11 | 50.0 | -3.9 | -7.4 | -0.04 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 4.4 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 13-7 | 65.0 | 16.4 | 24.2 | -0.07 |
| follow_move+rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level+rlm_ratio | early | pin limit <$1k | 6-0 | 100.0 | 53.7 | 92.6 | 0.42 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 16.5 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| consensus_gap+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 22.8 | 72.3 | 0.54 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 0.8 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 9-3 | 75.0 | 25.5 | 43.3 | 0.33 |
| money_delta+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_delta+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 52.0 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 3-1 | 75.0 | 25.4 | 41.3 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.0 | 45.3 | -0.5 |
| money_delta+sharp_gap | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 | -0.5 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 11.9 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 24.5 | 51.6 | -0.07 |
| pin_move+pin_value | early | pin limit <$1k | 1-4 | 20.0 | -29.1 | -61.8 | 0.2 |
| follow_move+pin_move | early | pin limit <$1k | 5-3 | 62.5 | 10.2 | 11.2 | 0.42 |
| consensus_gap+pin_move | early | pin limit <$1k | 0-3 | 0.0 | -56.4 | -100.0 | 0.53 |
| money_level+pin_move | early | pin limit <$1k | 2-2 | 50.0 | -5.8 | -21.8 | 0.1 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -50.4 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -50.4 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 16.8 | 4.3 | -0.07 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 49.6 | 90.9 | -1.0 |
| rlm_quiet | close | 1-3k bets | 6-10 | 37.5 | -5.2 | -24.3 |  |
| rlm_quiet | close | 3k+ bets | 1-0 | 100.0 | 71.4 | 142.0 |  |
| rlm_quiet | close | pin $1-2k | 1-3 | 25.0 | -19.6 | -51.2 |  |
| rlm_quiet | close | pin $2k+ | 2-2 | 50.0 | 7.6 | 8.7 |  |
| rlm_quiet | close | pin limit <$1k | 2-0 | 100.0 | 50.0 | 90.9 |  |
| pin_move | close | 1-3k bets | 7-10 | 41.2 | -9.4 | -23.1 |  |
| pin_move | close | 3k+ bets | 3-0 | 100.0 | 55.1 | 111.1 |  |
| pin_move | close | pin $1-2k | 4-6 | 40.0 | -8.5 | -22.2 |  |
| pin_move | close | pin $2k+ | 4-4 | 50.0 | -1.2 | -1.8 |  |
| pin_move | close | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 |  |
| money_delta | close | 1-3k bets | 4-7 | 36.4 | -10.0 | -30.2 |  |
| money_delta | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_delta | close | pin $1-2k | 3-3 | 50.0 | 3.6 | -3.1 |  |
| money_delta | close | pin $2k+ | 1-1 | 50.0 | 6.2 | -4.5 |  |
| money_delta | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| pin_rlm | close | 1-3k bets | 0-2 | 0.0 | -50.0 | -100.0 |  |
| pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| pin_rlm | close | pin $1-2k | 1-1 | 50.0 | 10.7 | -2.4 |  |
| pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -71.4 | -100.0 |  |
| follow_move | close | 1-3k bets | 16-21 | 43.2 | -5.9 | -20.7 |  |
| follow_move | close | 3k+ bets | 2-0 | 100.0 | 60.7 | 118.6 |  |
| follow_move | close | pin $1-2k | 5-8 | 38.5 | -12.7 | -27.4 |  |
| follow_move | close | pin $2k+ | 5-6 | 45.5 | -1.0 | -11.5 |  |
| follow_move | close | pin limit <$1k | 2-1 | 66.7 | 16.7 | 27.3 |  |
| rlm_ratio | close | 1-3k bets | 1-7 | 12.5 | -23.3 | -76.1 |  |
| rlm_ratio | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| rlm_ratio | close | pin $1-2k | 1-1 | 50.0 | 10.7 | -2.4 |  |
| rlm_ratio | close | pin $2k+ | 0-2 | 0.0 | -36.2 | -100.0 |  |
| rlm_ratio | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| money_level | close | 1-3k bets | 22-17 | 56.4 | 0.8 | -7.6 |  |
| money_level | close | 3k+ bets | 1-2 | 33.3 | -21.7 | -34.9 |  |
| money_level | close | pin $1-2k | 8-6 | 57.1 | 3.0 | 2.3 |  |
| money_level | close | pin $2k+ | 5-6 | 45.5 | -9.3 | -22.5 |  |
| money_level | close | pin limit <$1k | 1-3 | 25.0 | -25.0 | -53.2 |  |
| sharp_gap | close | 1-3k bets | 10-20 | 33.3 | -13.2 | -39.7 |  |
| sharp_gap | close | 3k+ bets | 1-2 | 33.3 | -21.7 | -34.9 |  |
| sharp_gap | close | pin $1-2k | 3-7 | 30.0 | -15.1 | -42.3 |  |
| sharp_gap | close | pin $2k+ | 2-7 | 22.2 | -27.4 | -58.3 |  |
| sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 |  |
| money_moving | close | 1-3k bets | 12-20 | 37.5 | -11.9 | -36.5 |  |
| money_moving | close | 3k+ bets | 1-2 | 33.3 | -21.7 | -34.9 |  |
| money_moving | close | pin $1-2k | 4-6 | 40.0 | -9.4 | -30.9 |  |
| money_moving | close | pin $2k+ | 2-7 | 22.2 | -27.4 | -58.3 |  |
| money_moving | close | pin limit <$1k | 2-2 | 50.0 | 0.0 | -5.5 |  |
| pin_value | close | 1-3k bets | 8-7 | 53.3 | 3.8 | 14.9 |  |
| pin_value | close | pin $1-2k | 3-4 | 42.9 | -5.0 | 12.6 |  |
| pin_value | close | pin $2k+ | 4-1 | 80.0 | 28.2 | 48.8 |  |
| pin_value | close | pin limit <$1k | 1-2 | 33.3 | -16.7 | -36.4 |  |
| consensus_gap | close | 1-3k bets | 15-10 | 60.0 | 4.5 | 0.7 |  |
| consensus_gap | close | 3k+ bets | 0-1 | 0.0 | -71.4 | -100.0 |  |
| consensus_gap | close | pin $1-2k | 4-3 | 57.1 | -2.0 | -6.1 |  |
| consensus_gap | close | pin $2k+ | 6-3 | 66.7 | 6.2 | 14.8 |  |
| consensus_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 |  |
| follow_move+pin_move | close | 1-3k bets | 5-10 | 33.3 | -16.9 | -38.4 |  |
| money_delta+money_moving | close | 1-3k bets | 3-4 | 42.9 | -2.3 | -18.2 |  |
| money_delta+sharp_gap | close | 1-3k bets | 3-3 | 50.0 | 5.7 | -4.5 |  |
| money_moving+sharp_gap | close | 1-3k bets | 9-18 | 33.3 | -14.4 | -40.1 |  |
| consensus_gap+money_level | close | 1-3k bets | 10-7 | 58.8 | -2.5 | -7.1 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 6-10 | 37.5 | -5.2 | -24.3 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 2-4 | 33.3 | -10.6 | -35.7 |  |
| consensus_gap+follow_move | close | 1-3k bets | 4-5 | 44.4 | -10.3 | -26.1 |  |
| follow_move+money_level | close | 1-3k bets | 7-7 | 50.0 | -5.7 | -17.7 |  |
| money_level+money_moving | close | 1-3k bets | 9-11 | 45.0 | -8.3 | -27.0 |  |
| money_level+sharp_gap | close | 1-3k bets | 7-10 | 41.2 | -10.2 | -27.3 |  |
| consensus_gap+money_moving | close | 1-3k bets | 3-7 | 30.0 | -23.7 | -50.4 |  |
| consensus_gap+pin_move | close | 1-3k bets | 1-1 | 50.0 | -10.7 | -21.6 |  |
| consensus_gap+pin_value | close | 1-3k bets | 6-4 | 60.0 | 9.1 | 12.6 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 2-7 | 22.2 | -27.1 | -57.6 |  |
| follow_move+money_moving | close | 1-3k bets | 3-9 | 25.0 | -20.9 | -59.8 |  |
| follow_move+pin_value | close | 1-3k bets | 1-2 | 33.3 | -16.7 | -36.4 |  |
| follow_move+sharp_gap | close | 1-3k bets | 4-10 | 28.6 | -14.9 | -51.9 |  |
| money_level+pin_move | close | 1-3k bets | 4-4 | 50.0 | -3.5 | -8.6 |  |
| money_level+pin_value | close | 1-3k bets | 2-5 | 28.6 | -21.4 | -46.5 |  |
| money_moving+pin_move | close | 1-3k bets | 2-3 | 40.0 | -10.0 | -24.4 |  |
| money_moving+pin_value | close | 1-3k bets | 1-6 | 14.3 | -35.7 | -72.7 |  |
| pin_move+pin_value | close | 1-3k bets | 0-1 | 0.0 | -50.0 | -100.0 |  |
| pin_move+sharp_gap | close | 1-3k bets | 1-4 | 20.0 | -25.7 | -61.8 |  |
| pin_value+sharp_gap | close | 1-3k bets | 1-5 | 16.7 | -33.3 | -68.2 |  |
| follow_move+money_delta | close | 1-3k bets | 2-4 | 33.3 | -15.6 | -35.7 |  |
| money_delta+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -2.4 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 2-3 | 40.0 | -10.0 | -22.8 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 1-7 | 12.5 | -23.3 | -76.1 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 1-3 | 25.0 | -14.3 | -52.3 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 1-5 | 16.7 | -21.6 | -68.2 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 1-5 | 16.7 | -19.0 | -68.2 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 1-5 | 16.7 | -19.0 | -68.2 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 1-7 | 12.5 | -23.3 | -76.1 |  |
| money_delta+money_level | close | 1-3k bets | 1-0 | 100.0 | 56.2 | 90.9 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 1-2 | 33.3 | -2.4 | -36.4 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 1-2 | 33.3 | -2.4 | -36.4 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 1-2 | 33.3 | -14.6 | -36.4 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 0-1 | 0.0 | -71.4 | -100.0 |  |
| money_level+pin_rlm | close | 1-3k bets | 0-1 | 0.0 | -71.4 | -100.0 |  |
| money_moving+pin_rlm | close | 1-3k bets | 0-1 | 0.0 | -71.4 | -100.0 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_level+rlm_ratio | close | 1-3k bets | 0-1 | 0.0 | -28.6 | -100.0 |  |
| consensus_gap+money_delta | close | 1-3k bets | 1-0 | 100.0 | 50.0 | 90.9 |  |
| money_delta+pin_value | close | 1-3k bets | 1-0 | 100.0 | 50.0 | 90.9 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 1-0 | 100.0 | 50.0 | 90.9 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 1-0 | 100.0 | 50.0 | 90.9 |  |
| follow_move+pin_rlm | close | 1-3k bets | 0-1 | 0.0 | -28.6 | -100.0 |  |
| pin_move+pin_rlm | close | 1-3k bets | 0-1 | 0.0 | -28.6 | -100.0 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 0-1 | 0.0 | -28.6 | -100.0 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 0-1 | 0.0 | -28.6 | -100.0 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 0-1 | 0.0 | -28.6 | -100.0 |  |
| money_level+money_moving | close | 3k+ bets | 1-2 | 33.3 | -21.7 | -34.9 |  |
| money_level+sharp_gap | close | 3k+ bets | 1-2 | 33.3 | -21.7 | -34.9 |  |
| money_moving+sharp_gap | close | 3k+ bets | 1-2 | 33.3 | -21.7 | -34.9 |  |
| follow_move+money_delta | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| follow_move+money_level | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| follow_move+money_moving | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| follow_move+pin_move | close | 3k+ bets | 2-0 | 100.0 | 60.7 | 118.6 |  |
| follow_move+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| follow_move+sharp_gap | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_delta+money_level | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_delta+money_moving | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_delta+pin_move | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_delta+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_delta+sharp_gap | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_level+pin_move | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_level+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_level+rlm_ratio | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_moving+pin_move | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_moving+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| pin_move+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| pin_move+sharp_gap | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 1-0 | 100.0 | 50.0 | 95.2 |  |
| consensus_gap+money_level | close | 3k+ bets | 0-1 | 0.0 | -71.4 | -100.0 |  |
| consensus_gap+money_moving | close | 3k+ bets | 0-1 | 0.0 | -71.4 | -100.0 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 0-1 | 0.0 | -71.4 | -100.0 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 1-0 | 100.0 | 71.4 | 142.0 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 1-0 | 100.0 | 71.4 | 142.0 |  |
| money_delta+money_moving | close | pin $1-2k | 2-1 | 66.7 | 23.8 | 28.7 |  |
| money_delta+sharp_gap | close | pin $1-2k | 2-1 | 66.7 | 23.8 | 28.7 |  |
| money_moving+sharp_gap | close | pin $1-2k | 3-6 | 33.3 | -13.6 | -35.9 |  |
| consensus_gap+follow_move | close | pin $1-2k | 1-2 | 33.3 | -31.0 | -44.7 |  |
| consensus_gap+money_level | close | pin $1-2k | 3-3 | 50.0 | -10.7 | -22.2 |  |
| consensus_gap+money_moving | close | pin $1-2k | 1-2 | 33.3 | -23.8 | -62.0 |  |
| consensus_gap+pin_move | close | pin $1-2k | 0-1 | 0.0 | -50.0 | -100.0 |  |
| consensus_gap+pin_value | close | pin $1-2k | 1-2 | 33.3 | -16.7 | -36.4 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 |  |
| follow_move+money_level | close | pin $1-2k | 4-4 | 50.0 | -3.8 | -6.5 |  |
| follow_move+money_moving | close | pin $1-2k | 2-2 | 50.0 | 1.6 | -3.5 |  |
| follow_move+pin_move | close | pin $1-2k | 3-6 | 33.3 | -14.3 | -35.4 |  |
| follow_move+pin_value | close | pin $1-2k | 0-1 | 0.0 | -50.0 | -100.0 |  |
| follow_move+sharp_gap | close | pin $1-2k | 2-3 | 40.0 | -4.5 | -22.8 |  |
| money_level+money_moving | close | pin $1-2k | 3-3 | 50.0 | -2.5 | -16.7 |  |
| money_level+pin_move | close | pin $1-2k | 3-3 | 50.0 | 0.0 | -3.0 |  |
| money_level+pin_value | close | pin $1-2k | 1-2 | 33.3 | -16.7 | -37.7 |  |
| money_level+sharp_gap | close | pin $1-2k | 2-3 | 40.0 | -8.8 | -22.8 |  |
| money_moving+pin_move | close | pin $1-2k | 2-2 | 50.0 | 1.6 | -3.5 |  |
| money_moving+pin_value | close | pin $1-2k | 0-3 | 0.0 | -52.1 | -100.0 |  |
| pin_move+pin_value | close | pin $1-2k | 0-1 | 0.0 | -50.0 | -100.0 |  |
| pin_move+sharp_gap | close | pin $1-2k | 2-3 | 40.0 | -4.5 | -22.8 |  |
| pin_value+sharp_gap | close | pin $1-2k | 0-3 | 0.0 | -52.1 | -100.0 |  |
| follow_move+money_delta | close | pin $1-2k | 2-2 | 50.0 | 0.0 | -2.4 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 1-3 | 25.0 | -19.6 | -51.2 |  |
| money_delta+pin_move | close | pin $1-2k | 2-1 | 66.7 | 16.7 | 30.1 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 1-2 | 33.3 | -16.7 | -34.9 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 1-2 | 33.3 | -9.5 | -34.9 |  |
| follow_move+pin_rlm | close | pin $1-2k | 1-1 | 50.0 | 10.7 | -2.4 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 1-1 | 50.0 | 10.7 | -2.4 |  |
| pin_move+pin_rlm | close | pin $1-2k | 1-1 | 50.0 | 10.7 | -2.4 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 1-1 | 50.0 | 10.7 | -2.4 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 0-1 | 0.0 | -28.6 | -100.0 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 1-1 | 50.0 | 10.7 | -2.4 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 1-1 | 50.0 | 10.7 | -2.4 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 0-1 | 0.0 | -28.6 | -100.0 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 0-1 | 0.0 | -28.6 | -100.0 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 1-1 | 50.0 | 10.7 | -2.4 |  |
| money_delta+money_level | close | pin $1-2k | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_delta+pin_rlm | close | pin $1-2k | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_level+pin_rlm | close | pin $1-2k | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_level+rlm_ratio | close | pin $1-2k | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_moving+pin_rlm | close | pin $1-2k | 1-0 | 100.0 | 50.0 | 95.2 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 1-0 | 100.0 | 50.0 | 95.2 |  |
| follow_move+pin_move | close | pin $2k+ | 3-4 | 42.9 | -7.7 | -15.8 |  |
| consensus_gap+money_level | close | pin $2k+ | 3-3 | 50.0 | -14.3 | -20.5 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 2-2 | 50.0 | 7.6 | 8.7 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 1-2 | 33.3 | -4.5 | -19.3 |  |
| money_level+money_moving | close | pin $2k+ | 2-6 | 25.0 | -25.3 | -53.0 |  |
| money_level+sharp_gap | close | pin $2k+ | 2-6 | 25.0 | -25.3 | -53.0 |  |
| money_moving+sharp_gap | close | pin $2k+ | 2-7 | 22.2 | -27.4 | -58.3 |  |
| consensus_gap+pin_value | close | pin $2k+ | 4-1 | 80.0 | 28.2 | 48.8 |  |
| follow_move+money_level | close | pin $2k+ | 1-2 | 33.3 | -18.8 | -47.7 |  |
| follow_move+money_moving | close | pin $2k+ | 0-3 | 0.0 | -42.9 | -100.0 |  |
| follow_move+sharp_gap | close | pin $2k+ | 0-3 | 0.0 | -42.9 | -100.0 |  |
| money_level+pin_move | close | pin $2k+ | 1-1 | 50.0 | -13.8 | -21.6 |  |
| money_moving+pin_move | close | pin $2k+ | 0-1 | 0.0 | -56.2 | -100.0 |  |
| pin_move+sharp_gap | close | pin $2k+ | 0-1 | 0.0 | -56.2 | -100.0 |  |
| money_delta+money_level | close | pin $2k+ | 1-0 | 100.0 | 56.2 | 90.9 |  |
| money_delta+money_moving | close | pin $2k+ | 1-1 | 50.0 | 6.2 | -4.5 |  |
| money_delta+sharp_gap | close | pin $2k+ | 1-1 | 50.0 | 6.2 | -4.5 |  |
| consensus_gap+money_moving | close | pin $2k+ | 0-3 | 0.0 | -62.2 | -100.0 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 0-3 | 0.0 | -62.2 | -100.0 |  |
| money_level+pin_value | close | pin $2k+ | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_moving+pin_value | close | pin $2k+ | 0-1 | 0.0 | -43.8 | -100.0 |  |
| pin_value+sharp_gap | close | pin $2k+ | 0-1 | 0.0 | -43.8 | -100.0 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -71.4 | -100.0 |  |
| money_level+pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -71.4 | -100.0 |  |
| money_moving+pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -71.4 | -100.0 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 0-1 | 0.0 | -71.4 | -100.0 |  |
| follow_move+money_delta | close | pin $2k+ | 0-1 | 0.0 | -43.8 | -100.0 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 0-2 | 0.0 | -36.2 | -100.0 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -43.8 | -100.0 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 0-2 | 0.0 | -36.2 | -100.0 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 0-2 | 0.0 | -36.2 | -100.0 |  |
| money_level+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -28.6 | -100.0 |  |
| consensus_gap+follow_move | close | pin $2k+ | 1-0 | 100.0 | 28.6 | 56.8 |  |
| consensus_gap+pin_move | close | pin $2k+ | 1-0 | 100.0 | 28.6 | 56.8 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 |  |
| consensus_gap+money_level | close | pin limit <$1k | 0-1 | 0.0 | -50.0 | -100.0 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 |  |
| follow_move+money_level | close | pin limit <$1k | 0-1 | 0.0 | -50.0 | -100.0 |  |
| follow_move+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 |  |
| follow_move+pin_value | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 |  |
| money_level+money_moving | close | pin limit <$1k | 1-2 | 33.3 | -16.7 | -37.7 |  |
| money_level+pin_value | close | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_moving+pin_value | close | pin limit <$1k | 1-2 | 33.3 | -16.7 | -36.4 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| follow_move+money_delta | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 2-0 | 100.0 | 50.0 | 90.9 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| money_delta+money_moving | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| money_delta+pin_value | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| money_level+pin_move | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 87.0 |  |
| money_moving+pin_move | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 87.0 |  |
| follow_move+pin_move | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| money_level+sharp_gap | close | pin limit <$1k | 0-1 | 0.0 | -50.0 | -100.0 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 1-0 | 100.0 | 50.0 | 90.9 |  |
| rlm_quiet | early | <1k bets | 1-2 | 33.3 | -2.4 | -36.4 | -0.73 |
| follow_move | early | <1k bets | 6-4 | 60.0 | 15.2 | 27.6 | -0.86 |
| follow_move | early | pin $1-2k | 1-0 | 100.0 | 71.4 | 142.0 | 0.0 |
| rlm_ratio | early | <1k bets | 1-1 | 50.0 | 10.7 | -4.5 | 0.35 |
| money_level | early | <1k bets | 6-3 | 66.7 | 7.1 | 7.9 | 0.63 |
| sharp_gap | early | <1k bets | 4-3 | 57.1 | 10.2 | 6.5 | 0.74 |
| money_moving | early | <1k bets | 3-2 | 60.0 | 1.4 | -5.0 | 0.26 |
| pin_value | early | <1k bets | 0-1 | 0.0 | -43.8 | -100.0 | 0.0 |
| pin_value | early | pin $1-2k | 0-1 | 0.0 | -43.8 | -100.0 | 0.0 |
| consensus_gap | early | <1k bets | 3-1 | 75.0 | 3.6 | -0.5 | 1.17 |
| follow_move+money_level | early | <1k bets | 2-1 | 66.7 | 9.5 | 0.7 | -0.73 |
| follow_move+sharp_gap | early | <1k bets | 2-1 | 66.7 | 23.8 | 27.3 | 0.23 |
| money_level+sharp_gap | early | <1k bets | 2-0 | 100.0 | 39.3 | 82.0 | 1.25 |
| follow_move+money_moving | early | <1k bets | 2-1 | 66.7 | 9.5 | 0.7 | -0.4 |
| money_level+money_moving | early | <1k bets | 2-1 | 66.7 | 2.4 | -5.3 | 0.1 |
| consensus_gap+money_level | early | <1k bets | 3-1 | 75.0 | 3.6 | -0.5 | 1.17 |
| follow_move+rlm_quiet | early | <1k bets | 1-2 | 33.3 | -2.4 | -36.4 | -0.73 |
| follow_move+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 10.7 | -4.5 | 0.35 |
| rlm_quiet+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 10.7 | -4.5 | 0.35 |
| rlm_quiet+sharp_gap | early | <1k bets | 1-1 | 50.0 | 10.7 | -4.5 | 0.35 |
| rlm_ratio+sharp_gap | early | <1k bets | 1-1 | 50.0 | 10.7 | -4.5 | 0.35 |
| money_moving+rlm_quiet | early | <1k bets | 1-0 | 100.0 | 50.0 | 90.9 | 1.0 |
| money_moving+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 50.0 | 90.9 | 1.0 |
| money_moving+sharp_gap | early | <1k bets | 2-0 | 100.0 | 39.3 | 82.0 | 1.75 |
| consensus_gap+money_moving | early | <1k bets | 2-0 | 100.0 | 28.6 | 42.0 | 0.15 |
| consensus_gap+sharp_gap | early | <1k bets | 1-0 | 100.0 | 28.6 | 73.0 | 2.5 |
| consensus_gap+follow_move | early | <1k bets | 1-0 | 100.0 | 28.6 | 11.1 | -2.2 |
