# CBB scorecard

Generated 2026-11-18 01:20 UTC. 531 graded games (56 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**512 games before 2026-11-17 (fit) · 19 on or after it (forward).**

Every signal, threshold and PROMOTE/DROP label here was chosen while looking at
the games before 2026-11-17. `pin_value` went 108-68 in first halves --
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
sample ran **47.4% favourites** (n=530) and **46.5% overs** (n=531) and **74.2% moneyline favourites** (n=450).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-17. Nothing in the engine was chosen using these. n=19 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| follow_move | both | 16-16 | 50.0 | 56.5 | -6.5 | -8.55 | -26.7 | 0.2 | 43.8 | no edge shown yet |
| money_level | both | 4-0 | 100.0 | 76.5 | 23.5 | +0.83 | 20.7 | -1.47 | 50.0 | keep collecting (4/30) |
| sharp_gap | both | 1-2 | 33.3 | 41.2 | -7.8 | -1.3 | -43.2 | -2.53 | 0.0 | keep collecting (3/30) |
| money_moving | both | 2-1 | 66.7 | 58.8 | 7.8 | -0.27 | -9.0 | -2.17 | 33.3 | keep collecting (3/30) |
| consensus_gap | both | 12-6 | 66.7 | 49.2 | 17.4 | +11.06 | 61.5 | 0.48 | 33.3 | keep collecting (18/30) |
| money_level+money_moving | both | 2-0 | 100.0 | 76.5 | 23.5 | +0.73 | 36.4 | -3.25 | 50.0 | keep collecting (2/30) |
| money_level+sharp_gap | both | 1-0 | 100.0 | 76.5 | 23.5 | +0.7 | 70.4 | -6.8 | 0.0 | keep collecting (1/30) |
| money_moving+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.3 | -14.8 | -3.4 | 0.0 | keep collecting (2/30) |
| consensus_gap+money_moving | both | 0-1 | 0.0 | 23.5 | -23.5 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+sharp_gap | both | 0-2 | 0.0 | 23.5 | -23.5 | -2.0 | -100.0 | -0.4 | 0.0 | keep collecting (2/30) |
| follow_move+money_level | both | 3-0 | 100.0 | 76.5 | 23.5 | +0.12 | 4.1 | 0.3 | 66.7 | keep collecting (3/30) |
| follow_move+money_moving | both | 1-0 | 100.0 | 76.5 | 23.5 | +0.03 | 2.5 | 0.3 | 100.0 | keep collecting (1/30) |
| follow_move | moneyline | 9-5 | 64.3 | 68.9 | -4.6 | -4.24 | -30.3 | -0.46 | 35.7 | keep collecting (14/30) |
| follow_move | spread | 4-6 | 40.0 | 47.9 | -7.9 | -2.08 | -20.8 | 0.0 | 40.0 | keep collecting (10/30) |
| follow_move | total | 3-5 | 37.5 | 45.4 | -7.9 | -2.23 | -27.8 | 1.62 | 62.5 | keep collecting (8/30) |
| money_level | moneyline | 4-0 | 100.0 | 76.5 | 23.5 | +0.83 | 20.7 | -1.47 | 50.0 | keep collecting (4/30) |
| sharp_gap | moneyline | 1-2 | 33.3 | 41.2 | -7.8 | -1.3 | -43.2 | -2.53 | 0.0 | keep collecting (3/30) |
| money_moving | moneyline | 2-1 | 66.7 | 58.8 | 7.8 | -0.27 | -9.0 | -2.17 | 33.3 | keep collecting (3/30) |
| consensus_gap | moneyline | 5-4 | 55.6 | 41.2 | 14.4 | +6.92 | 76.9 | 0.74 | 33.3 | keep collecting (9/30) |
| consensus_gap | spread | 4-2 | 66.7 | 51.8 | 14.9 | +1.54 | 25.6 | 0.0 | 16.7 | keep collecting (6/30) |
| consensus_gap | total | 3-0 | 100.0 | 68.4 | 31.6 | +2.61 | 87.0 | 0.67 | 66.7 | keep collecting (3/30) |
| money_level+money_moving | moneyline | 2-0 | 100.0 | 76.5 | 23.5 | +0.73 | 36.4 | -3.25 | 50.0 | keep collecting (2/30) |
| money_level+sharp_gap | moneyline | 1-0 | 100.0 | 76.5 | 23.5 | +0.7 | 70.4 | -6.8 | 0.0 | keep collecting (1/30) |
| money_moving+sharp_gap | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.3 | -14.8 | -3.4 | 0.0 | keep collecting (2/30) |
| consensus_gap+money_moving | moneyline | 0-1 | 0.0 | 23.5 | -23.5 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+sharp_gap | moneyline | 0-2 | 0.0 | 23.5 | -23.5 | -2.0 | -100.0 | -0.4 | 0.0 | keep collecting (2/30) |
| follow_move+money_level | moneyline | 3-0 | 100.0 | 76.5 | 23.5 | +0.12 | 4.1 | 0.3 | 66.7 | keep collecting (3/30) |
| follow_move+money_moving | moneyline | 1-0 | 100.0 | 76.5 | 23.5 | +0.03 | 2.5 | 0.3 | 100.0 | keep collecting (1/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 7-5 | 58.3 | 37.4 | 20.9 | +6.31 | 52.6 |  |  | keep collecting (12/30) |
| follow_move | both | 23-23 | 50.0 | 52.2 | -2.2 | -5.14 | -11.2 |  |  | no edge shown yet |
| rlm_ratio | both | 6-4 | 60.0 | 41.5 | 18.5 | +6.44 | 64.4 |  |  | keep collecting (10/30) |
| money_level | both | 36-19 | 65.5 | 58.7 | 6.7 | +5.65 | 10.3 |  |  | PROMOTE: beats break-even and its own base rate |
| sharp_gap | both | 28-25 | 52.8 | 44.8 | 8.1 | +3.12 | 5.9 |  |  | no edge shown yet |
| money_moving | both | 29-24 | 54.7 | 45.8 | 9.0 | +4.14 | 7.8 |  |  | no edge shown yet |
| pin_value | both | 8-11 | 42.1 | 50.5 | -8.4 | -3.9 | -20.6 |  |  | keep collecting (19/30) |
| consensus_gap | both | 8-13 | 38.1 | 45.3 | -7.2 | -1.55 | -7.4 |  |  | keep collecting (21/30) |
| money_level+money_moving | both | 22-10 | 68.8 | 53.3 | 15.5 | +9.34 | 29.2 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+pin_rlm | both | 5-1 | 83.3 | 46.0 | 37.3 | +5.9 | 98.3 |  |  | keep collecting (6/30) |
| money_level+sharp_gap | both | 21-10 | 67.7 | 52.6 | 15.2 | +9.31 | 30.0 |  |  | PROMOTE: beats break-even and its own base rate |
| money_moving+pin_rlm | both | 7-5 | 58.3 | 37.4 | 20.9 | +6.31 | 52.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | both | 28-24 | 53.8 | 45.2 | 8.7 | +4.12 | 7.9 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 7-5 | 58.3 | 37.4 | 20.9 | +6.31 | 52.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_value | both | 5-5 | 50.0 | 57.4 | -7.4 | -0.63 | -6.3 |  |  | keep collecting (10/30) |
| money_moving+pin_value | both | 5-5 | 50.0 | 47.6 | 2.4 | -0.63 | -6.3 |  |  | keep collecting (10/30) |
| pin_value+sharp_gap | both | 5-5 | 50.0 | 47.6 | 2.4 | -0.63 | -6.3 |  |  | keep collecting (10/30) |
| consensus_gap+money_level | both | 4-2 | 66.7 | 63.2 | 3.5 | +1.0 | 16.7 |  |  | keep collecting (6/30) |
| consensus_gap+money_moving | both | 4-6 | 40.0 | 37.6 | 2.4 | -2.56 | -25.6 |  |  | keep collecting (10/30) |
| consensus_gap+pin_value | both | 3-3 | 50.0 | 49.5 | 0.5 | -0.35 | -5.8 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 4-6 | 40.0 | 37.6 | 2.4 | -2.56 | -25.6 |  |  | keep collecting (10/30) |
| follow_move+money_level | both | 19-11 | 63.3 | 59.2 | 4.2 | +0.52 | 1.7 |  |  | no edge shown yet |
| follow_move+money_moving | both | 12-9 | 57.1 | 47.4 | 9.8 | +3.85 | 18.3 |  |  | keep collecting (21/30) |
| follow_move+sharp_gap | both | 11-9 | 55.0 | 45.9 | 9.1 | +3.82 | 19.1 |  |  | keep collecting (20/30) |
| follow_move+pin_value | both | 1-2 | 33.3 | 47.4 | -14.0 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| follow_move+pin_rlm | both | 4-2 | 66.7 | 33.7 | 33.0 | +6.62 | 110.3 |  |  | keep collecting (6/30) |
| follow_move+rlm_ratio | both | 6-4 | 60.0 | 41.5 | 18.5 | +6.44 | 64.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_ratio | both | 6-4 | 60.0 | 41.5 | 18.5 | +6.44 | 64.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+rlm_ratio | both | 4-2 | 66.7 | 33.7 | 33.0 | +6.62 | 110.3 |  |  | keep collecting (6/30) |
| rlm_ratio+sharp_gap | both | 6-4 | 60.0 | 41.5 | 18.5 | +6.44 | 64.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 0-3 | 0.0 | 49.1 | -49.1 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_level+rlm_ratio | both | 5-2 | 71.4 | 49.2 | 22.2 | +4.94 | 70.5 |  |  | keep collecting (7/30) |
| consensus_gap+pin_rlm | both | 1-1 | 50.0 | 27.6 | 22.4 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| pin_rlm+pin_value | both | 2-1 | 66.7 | 49.1 | 17.5 | +0.78 | 26.0 |  |  | keep collecting (3/30) |
| consensus_gap+rlm_ratio | both | 0-1 | 0.0 | 23.5 | -23.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 2-3 | 40.0 | 23.5 | 16.5 | +3.8 | 76.0 |  |  | keep collecting (5/30) |
| pin_rlm | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| pin_rlm | total | 4-1 | 80.0 | 46.3 | 33.7 | +2.6 | 51.9 |  |  | keep collecting (5/30) |
| follow_move | moneyline | 12-4 | 75.0 | 63.2 | 11.8 | +3.67 | 23.0 |  |  | keep collecting (16/30) |
| follow_move | spread | 4-11 | 26.7 | 48.8 | -22.1 | -7.22 | -48.1 |  |  | keep collecting (15/30) |
| follow_move | total | 7-8 | 46.7 | 43.9 | 2.8 | -1.59 | -10.6 |  |  | keep collecting (15/30) |
| rlm_ratio | moneyline | 2-2 | 50.0 | 23.5 | 26.5 | +4.8 | 120.0 |  |  | keep collecting (4/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 52.6 | -52.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_ratio | total | 4-1 | 80.0 | 53.7 | 26.3 | +2.64 | 52.7 |  |  | keep collecting (5/30) |
| money_level | moneyline | 15-2 | 88.2 | 70.2 | 18.0 | +3.56 | 20.9 |  |  | keep collecting (17/30) |
| money_level | spread | 10-9 | 52.6 | 50.4 | 2.2 | +0.13 | 0.7 |  |  | keep collecting (19/30) |
| money_level | total | 11-8 | 57.9 | 56.8 | 1.1 | +1.96 | 10.3 |  |  | keep collecting (19/30) |
| sharp_gap | moneyline | 6-10 | 37.5 | 33.5 | 4.0 | -1.77 | -11.1 |  |  | keep collecting (16/30) |
| sharp_gap | spread | 11-8 | 57.9 | 51.2 | 6.6 | +1.93 | 10.2 |  |  | keep collecting (19/30) |
| sharp_gap | total | 11-7 | 61.1 | 48.0 | 13.2 | +2.96 | 16.5 |  |  | keep collecting (18/30) |
| money_moving | moneyline | 7-9 | 43.8 | 36.8 | 7.0 | -0.75 | -4.7 |  |  | keep collecting (16/30) |
| money_moving | spread | 11-8 | 57.9 | 51.2 | 6.6 | +1.93 | 10.2 |  |  | keep collecting (19/30) |
| money_moving | total | 11-7 | 61.1 | 48.0 | 13.2 | +2.96 | 16.5 |  |  | keep collecting (18/30) |
| pin_value | moneyline | 0-1 | 0.0 | 23.5 | -23.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_value | spread | 3-5 | 37.5 | 50.0 | -12.5 | -2.41 | -30.1 |  |  | keep collecting (8/30) |
| pin_value | total | 5-5 | 50.0 | 53.7 | -3.7 | -0.49 | -4.9 |  |  | keep collecting (10/30) |
| consensus_gap | moneyline | 2-10 | 16.7 | 36.8 | -20.1 | -3.77 | -31.4 |  |  | keep collecting (12/30) |
| consensus_gap | spread | 2-2 | 50.0 | 51.3 | -1.3 | -0.33 | -8.4 |  |  | keep collecting (4/30) |
| consensus_gap | total | 4-1 | 80.0 | 61.1 | 18.9 | +2.56 | 51.2 |  |  | keep collecting (5/30) |
| money_moving+sharp_gap | moneyline | 6-9 | 40.0 | 34.1 | 5.9 | -0.77 | -5.2 |  |  | keep collecting (15/30) |
| follow_move+money_level | moneyline | 11-1 | 91.7 | 72.1 | 19.6 | +3.17 | 26.4 |  |  | keep collecting (12/30) |
| follow_move+money_moving | moneyline | 6-2 | 75.0 | 50.0 | 25.0 | +5.32 | 66.5 |  |  | keep collecting (8/30) |
| follow_move+sharp_gap | moneyline | 5-2 | 71.4 | 46.2 | 25.2 | +5.3 | 75.7 |  |  | keep collecting (7/30) |
| money_level+money_moving | moneyline | 6-0 | 100.0 | 58.8 | 41.2 | +4.75 | 79.1 |  |  | keep collecting (6/30) |
| money_level+sharp_gap | moneyline | 5-0 | 100.0 | 55.3 | 44.7 | +4.73 | 94.5 |  |  | keep collecting (5/30) |
| consensus_gap+money_level | moneyline | 1-1 | 50.0 | 76.5 | -26.5 | -0.57 | -28.7 |  |  | keep collecting (2/30) |
| follow_move+pin_rlm | moneyline | 2-1 | 66.7 | 23.5 | 43.1 | +5.8 | 193.3 |  |  | keep collecting (3/30) |
| follow_move+rlm_ratio | moneyline | 2-2 | 50.0 | 23.5 | 26.5 | +4.8 | 120.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_rlm | moneyline | 2-3 | 40.0 | 23.5 | 16.5 | +3.8 | 76.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | moneyline | 2-2 | 50.0 | 23.5 | 26.5 | +4.8 | 120.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+rlm_ratio | moneyline | 2-1 | 66.7 | 23.5 | 43.1 | +5.8 | 193.3 |  |  | keep collecting (3/30) |
| pin_rlm+sharp_gap | moneyline | 2-3 | 40.0 | 23.5 | 16.5 | +3.8 | 76.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 2-2 | 50.0 | 23.5 | 26.5 | +4.8 | 120.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 23.5 | 76.5 | +3.3 | 330.0 |  |  | keep collecting (1/30) |
| money_level+rlm_ratio | moneyline | 1-0 | 100.0 | 23.5 | 76.5 | +3.3 | 330.0 |  |  | keep collecting (1/30) |
| consensus_gap+money_moving | moneyline | 0-5 | 0.0 | 23.5 | -23.5 | -5.0 | -100.0 |  |  | keep collecting (5/30) |
| consensus_gap+rlm_ratio | moneyline | 0-1 | 0.0 | 23.5 | -23.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+sharp_gap | moneyline | 0-5 | 0.0 | 23.5 | -23.5 | -5.0 | -100.0 |  |  | keep collecting (5/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 23.5 | -23.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+pin_value | moneyline | 0-1 | 0.0 | 23.5 | -23.5 | -1.0 | -100.0 |  |  | redundant -- identical record to pin_value alone, not independent confirmation |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 23.5 | -23.5 | -1.0 | -100.0 |  |  | redundant -- identical record to pin_value alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 23.5 | -23.5 | -1.0 | -100.0 |  |  | redundant -- identical record to pin_value alone, not independent confirmation |
| money_level+money_moving | spread | 8-6 | 57.1 | 51.1 | 6.0 | +1.31 | 9.4 |  |  | keep collecting (14/30) |
| money_level+pin_rlm | spread | 1-0 | 100.0 | 52.6 | 47.4 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | spread | 8-6 | 57.1 | 51.1 | 6.0 | +1.31 | 9.4 |  |  | keep collecting (14/30) |
| money_moving+pin_rlm | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | spread | 11-8 | 57.9 | 51.2 | 6.6 | +1.93 | 10.2 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+money_level | spread | 2-1 | 66.7 | 52.6 | 14.0 | +0.67 | 22.2 |  |  | keep collecting (3/30) |
| consensus_gap+money_moving | spread | 2-1 | 66.7 | 52.6 | 14.0 | +0.67 | 22.2 |  |  | keep collecting (3/30) |
| consensus_gap+pin_value | spread | 1-1 | 50.0 | 52.6 | -2.6 | -0.17 | -8.4 |  |  | keep collecting (2/30) |
| consensus_gap+sharp_gap | spread | 2-1 | 66.7 | 52.6 | 14.0 | +0.67 | 22.2 |  |  | keep collecting (3/30) |
| money_level+pin_value | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.41 | -6.9 |  |  | keep collecting (6/30) |
| money_moving+pin_value | spread | 2-3 | 40.0 | 50.5 | -10.5 | -1.32 | -26.4 |  |  | keep collecting (5/30) |
| pin_value+sharp_gap | spread | 2-3 | 40.0 | 50.5 | -10.5 | -1.32 | -26.4 |  |  | keep collecting (5/30) |
| follow_move+money_level | spread | 3-6 | 33.3 | 49.1 | -15.8 | -3.2 | -35.6 |  |  | keep collecting (9/30) |
| follow_move+pin_value | spread | 1-2 | 33.3 | 47.4 | -14.0 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 0-1 | 0.0 | 47.4 | -47.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| follow_move+money_moving | spread | 1-3 | 25.0 | 50.0 | -25.0 | -2.02 | -50.5 |  |  | keep collecting (4/30) |
| follow_move+sharp_gap | spread | 1-3 | 25.0 | 50.0 | -25.0 | -2.02 | -50.5 |  |  | keep collecting (4/30) |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 52.6 | -52.6 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+rlm_ratio | spread | 0-1 | 0.0 | 52.6 | -52.6 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 52.6 | -52.6 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 52.6 | -52.6 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+pin_value | spread | 0-1 | 0.0 | 47.4 | -47.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+money_moving | total | 8-4 | 66.7 | 53.1 | 13.6 | +3.28 | 27.3 |  |  | keep collecting (12/30) |
| money_level+pin_value | total | 2-2 | 50.0 | 68.4 | -18.4 | -0.22 | -5.5 |  |  | keep collecting (4/30) |
| money_level+sharp_gap | total | 8-4 | 66.7 | 53.1 | 13.6 | +3.28 | 27.3 |  |  | keep collecting (12/30) |
| money_moving+pin_value | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| money_moving+sharp_gap | total | 11-7 | 61.1 | 48.0 | 13.2 | +2.96 | 16.5 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| pin_value+sharp_gap | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| follow_move+money_level | total | 5-4 | 55.6 | 52.0 | 3.5 | +0.54 | 6.1 |  |  | keep collecting (9/30) |
| follow_move+money_moving | total | 5-4 | 55.6 | 43.9 | 11.7 | +0.54 | 6.1 |  |  | keep collecting (9/30) |
| follow_move+sharp_gap | total | 5-4 | 55.6 | 43.9 | 11.7 | +0.54 | 6.1 |  |  | keep collecting (9/30) |
| consensus_gap+money_level | total | 1-0 | 100.0 | 68.4 | 31.6 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| consensus_gap+pin_value | total | 2-1 | 66.7 | 56.1 | 10.5 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| consensus_gap+money_moving | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 |  |  | keep collecting (2/30) |
| consensus_gap+pin_rlm | total | 1-0 | 100.0 | 31.6 | 68.4 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| consensus_gap+sharp_gap | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 |  |  | keep collecting (2/30) |
| money_moving+pin_rlm | total | 4-1 | 80.0 | 46.3 | 33.7 | +2.6 | 51.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 |  |  | keep collecting (2/30) |
| pin_rlm+sharp_gap | total | 4-1 | 80.0 | 46.3 | 33.7 | +2.6 | 51.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+pin_rlm | total | 2-1 | 66.7 | 43.9 | 22.8 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| follow_move+rlm_ratio | total | 4-1 | 80.0 | 53.7 | 26.3 | +2.64 | 52.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| money_level+rlm_ratio | total | 4-1 | 80.0 | 53.7 | 26.3 | +2.64 | 52.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_ratio | total | 4-1 | 80.0 | 53.7 | 26.3 | +2.64 | 52.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+rlm_ratio | total | 2-1 | 66.7 | 43.9 | 22.8 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 4-1 | 80.0 | 53.7 | 26.3 | +2.64 | 52.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |

# FIT (in-sample — this is the hypothesis)

Games before 2026-11-17. The engine was built by looking at these, so a strong record here is expected and proves nothing. n=512 games.

## EARLY  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | both | 325-302 | 51.8 | 52.1 | -0.3 | -58.99 | -9.4 | 0.24 | 42.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | both | 17-15 | 53.1 | 37.6 | 15.5 | +9.23 | 28.9 | 0.08 | 46.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | both | 119-76 | 61.0 | 58.4 | 2.6 | -8.05 | -4.1 | 0.21 | 41.5 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 105-79 | 57.1 | 49.3 | 7.7 | +23.97 | 13.0 | 0.36 | 42.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | both | 70-50 | 58.3 | 50.9 | 7.4 | +9.37 | 7.8 | 0.19 | 42.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | both | 43-42 | 50.6 | 47.8 | 2.8 | -3.68 | -4.3 | 0.14 | 41.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.7 | -31.7 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 158-223 | 41.5 | 46.6 | -5.1 | -65.4 | -17.2 | 0.31 | 45.7 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | both | 23-22 | 51.1 | 63.2 | -12.1 | -10.62 | -23.6 | 0.25 | 46.7 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | both | 15-19 | 44.1 | 45.7 | -1.6 | -3.69 | -10.9 | 0.17 | 38.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_value | both | 17-27 | 38.6 | 45.5 | -6.9 | -12.16 | -27.6 | 0.43 | 52.3 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_ratio | both | 17-15 | 53.1 | 37.6 | 15.5 | +9.23 | 28.9 | 0.08 | 46.9 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 52-29 | 64.2 | 49.9 | 14.3 | +15.17 | 18.7 | 0.44 | 48.1 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 45-27 | 62.5 | 56.7 | 5.8 | +2.08 | 2.9 | 0.16 | 48.6 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | both | 10-8 | 55.6 | 50.7 | 4.8 | +0.9 | 5.0 | 0.5 | 50.0 | keep collecting (18/30) |
| money_moving+pin_value | both | 7-5 | 58.3 | 50.1 | 8.2 | +1.13 | 9.4 | 0.42 | 41.7 | keep collecting (12/30) |
| rlm_ratio+sharp_gap | both | 17-15 | 53.1 | 37.6 | 15.5 | +9.23 | 28.9 | 0.08 | 46.9 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 72-41 | 63.7 | 55.6 | 8.2 | +7.11 | 6.3 | 0.49 | 46.0 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 44-28 | 61.1 | 49.5 | 11.6 | +12.34 | 17.1 | 0.44 | 45.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | both | 12-7 | 63.2 | 49.3 | 13.9 | +3.75 | 19.8 | -0.15 | 36.8 | keep collecting (19/30) |
| consensus_gap+follow_move | both | 24-34 | 41.4 | 50.8 | -9.4 | -15.5 | -26.7 | 0.77 | 56.9 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_value | both | 18-17 | 51.4 | 47.6 | 3.8 | -1.2 | -3.4 | -0.08 | 31.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+sharp_gap | both | 19-33 | 36.5 | 46.5 | -10.0 | -4.74 | -9.1 | 0.64 | 46.2 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | both | 64-36 | 64.0 | 58.2 | 5.8 | -3.53 | -3.5 | 0.33 | 44.0 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 9-6 | 60.0 | 42.6 | 17.4 | +2.84 | 18.9 | 1.01 | 53.3 | keep collecting (15/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 45.0 | 5.0 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 32-17 | 65.3 | 51.8 | 13.5 | +7.79 | 15.9 | 0.49 | 55.1 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+rlm_ratio | both | 6-5 | 54.5 | 42.4 | 12.1 | +2.5 | 22.7 | -0.05 | 45.5 | keep collecting (11/30) |
| consensus_gap+rlm_ratio | both | 1-4 | 20.0 | 37.2 | -17.2 | -3.09 | -61.8 | 0.2 | 60.0 | keep collecting (5/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 53.6 | -53.6 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 25.9 | 74.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | moneyline | 133-92 | 59.1 | 57.2 | 1.9 | -24.75 | -11.0 | 0.43 | 48.9 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 94-110 | 46.1 | 49.2 | -3.1 | -23.73 | -11.6 | -0.02 | 33.3 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | total | 98-100 | 49.5 | 49.4 | 0.1 | -10.51 | -5.3 | 0.28 | 44.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | moneyline | 9-9 | 50.0 | 25.9 | 24.1 | +7.81 | 43.4 | 0.14 | 61.1 | keep collecting (18/30) |
| rlm_ratio | spread | 3-2 | 60.0 | 51.7 | 8.3 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 5-4 | 55.6 | 53.3 | 2.2 | +0.59 | 6.5 | 0.33 | 44.4 | keep collecting (9/30) |
| money_level | moneyline | 64-27 | 70.3 | 69.4 | 1.0 | -8.93 | -9.8 | 0.18 | 46.2 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 16-16 | 50.0 | 49.1 | 0.9 | -1.6 | -5.0 | 0.81 | 46.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | total | 39-33 | 54.2 | 48.7 | 5.5 | +2.48 | 3.4 | -0.01 | 33.3 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 43-37 | 53.8 | 47.6 | 6.2 | +9.7 | 12.1 | 0.39 | 50.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | spread | 19-14 | 57.6 | 49.7 | 7.8 | +3.09 | 9.4 | 0.61 | 36.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 43-28 | 60.6 | 51.1 | 9.4 | +11.17 | 15.7 | 0.21 | 38.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | moneyline | 26-26 | 50.0 | 52.8 | -2.8 | -6.41 | -12.3 | 0.23 | 53.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | spread | 17-4 | 81.0 | 49.1 | 31.9 | +11.27 | 53.7 | 0.14 | 38.1 | keep collecting (21/30) |
| money_moving | total | 27-20 | 57.4 | 49.7 | 7.7 | +4.51 | 9.6 | 0.17 | 31.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | moneyline | 1-5 | 16.7 | 25.9 | -9.2 | -4.02 | -67.0 | -0.02 | 66.7 | keep collecting (6/30) |
| pin_value | spread | 22-17 | 56.4 | 49.2 | 7.2 | +2.35 | 6.0 | 0.28 | 41.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 20-20 | 50.0 | 49.8 | 0.2 | -2.01 | -5.0 | 0.03 | 37.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.8 | -19.5 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 63-121 | 34.2 | 43.7 | -9.5 | -47.49 | -25.8 | -0.03 | 42.4 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 51-49 | 51.0 | 49.1 | 1.9 | -4.52 | -4.5 | 0.49 | 45.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap | total | 44-53 | 45.4 | 49.3 | -4.0 | -13.39 | -13.8 | 0.76 | 52.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | moneyline | 33-12 | 73.3 | 64.5 | 8.9 | +0.72 | 1.6 | 0.53 | 57.8 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+follow_move | moneyline | 8-18 | 30.8 | 53.7 | -22.9 | -13.56 | -52.1 | 0.36 | 61.5 | keep collecting (26/30) |
| consensus_gap+pin_value | moneyline | 1-5 | 16.7 | 25.9 | -9.2 | -4.02 | -67.0 | -0.02 | 66.7 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_value | moneyline | 0-2 | 0.0 | 25.9 | -25.9 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| money_level+money_moving | moneyline | 17-9 | 65.4 | 70.4 | -5.0 | -5.47 | -21.0 | -0.07 | 57.7 | keep collecting (26/30) |
| consensus_gap+sharp_gap | moneyline | 11-24 | 31.4 | 45.2 | -13.7 | -2.71 | -7.7 | 0.55 | 48.6 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | moneyline | 37-12 | 75.5 | 68.2 | 7.3 | -4.09 | -8.4 | 0.18 | 46.9 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 14-5 | 73.7 | 56.4 | 17.3 | +3.36 | 17.7 | 0.68 | 73.7 | keep collecting (19/30) |
| consensus_gap+money_level | moneyline | 16-14 | 53.3 | 70.9 | -17.6 | -8.68 | -28.9 | -0.09 | 46.7 | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+sharp_gap | moneyline | 25-11 | 69.4 | 50.0 | 19.4 | +8.63 | 24.0 | 0.36 | 58.3 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 15-13 | 53.6 | 48.3 | 5.3 | +1.07 | 3.8 | 0.67 | 64.3 | keep collecting (28/30) |
| consensus_gap+money_moving | moneyline | 7-18 | 28.0 | 45.2 | -17.2 | -9.63 | -38.5 | 0.27 | 48.0 | keep collecting (25/30) |
| follow_move+rlm_ratio | moneyline | 9-9 | 50.0 | 25.9 | 24.1 | +7.81 | 43.4 | 0.14 | 61.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 9-9 | 50.0 | 25.9 | 24.1 | +7.81 | 43.4 | 0.14 | 61.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 0-3 | 0.0 | 25.9 | -25.9 | -3.0 | -100.0 | 0.0 | 66.7 | keep collecting (3/30) |
| money_moving+rlm_ratio | moneyline | 2-2 | 50.0 | 25.9 | 24.1 | +1.78 | 44.5 | 0.1 | 75.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| money_level+rlm_ratio | moneyline | 3-3 | 50.0 | 25.9 | 24.1 | +0.23 | 3.8 | 1.7 | 83.3 | keep collecting (6/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 25.9 | 74.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 4-5 | 44.4 | 47.2 | -2.7 | -1.59 | -17.7 | 1.67 | 66.7 | keep collecting (9/30) |
| consensus_gap+money_moving | spread | 4-0 | 100.0 | 47.2 | 52.8 | +3.41 | 85.2 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_value | spread | 9-8 | 52.9 | 48.2 | 4.8 | -0.31 | -1.8 | 0.53 | 52.9 | keep collecting (17/30) |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.7 | 8.3 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 48.6 | 13.9 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 9-4 | 69.2 | 48.5 | 20.8 | +4.21 | 32.4 | 0.77 | 61.5 | keep collecting (13/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.8 | -5.9 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.4 | 10.6 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 51.7 | 8.3 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 13-11 | 54.2 | 49.1 | 5.1 | +0.71 | 3.0 | 0.96 | 41.7 | keep collecting (24/30) |
| money_moving+sharp_gap | spread | 9-3 | 75.0 | 49.1 | 25.9 | +5.13 | 42.7 | 0.42 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.1 | 17.6 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 8-8 | 50.0 | 47.9 | 2.1 | -1.18 | -7.4 | 0.94 | 43.8 | keep collecting (16/30) |
| consensus_gap+sharp_gap | spread | 4-3 | 57.1 | 47.2 | 10.0 | +0.41 | 5.8 | 2.14 | 71.4 | keep collecting (7/30) |
| follow_move+money_level | spread | 11-8 | 57.9 | 48.4 | 9.5 | +2.04 | 10.7 | 0.63 | 42.1 | keep collecting (19/30) |
| follow_move+pin_value | spread | 11-7 | 61.1 | 48.7 | 12.4 | +2.56 | 14.2 | 0.33 | 33.3 | keep collecting (18/30) |
| follow_move+money_moving | spread | 9-1 | 90.0 | 47.7 | 42.3 | +7.22 | 72.2 | 0.2 | 40.0 | keep collecting (10/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 52.8 | 13.8 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 19-14 | 57.6 | 49.1 | 8.5 | +3.34 | 10.1 | 0.09 | 36.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | total | 26-18 | 59.1 | 50.0 | 9.1 | +5.68 | 12.9 | 0.18 | 36.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | total | 20-12 | 62.5 | 50.8 | 11.7 | +6.14 | 19.2 | 0.25 | 31.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | total | 7-4 | 63.6 | 52.0 | 11.7 | +2.32 | 21.1 | 0.36 | 36.4 | keep collecting (11/30) |
| money_moving+pin_value | total | 4-3 | 57.1 | 50.6 | 6.5 | +0.56 | 8.0 | 0.29 | 28.6 | keep collecting (7/30) |
| pin_value+sharp_gap | total | 10-5 | 66.7 | 50.9 | 15.8 | +4.01 | 26.7 | 0.0 | 33.3 | keep collecting (15/30) |
| follow_move+money_level | total | 16-16 | 50.0 | 48.7 | 1.3 | -1.47 | -4.6 | 0.38 | 40.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.1 | -2.5 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 5-4 | 55.6 | 53.3 | 2.2 | +0.59 | 6.5 | 0.33 | 44.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 17-12 | 58.6 | 50.4 | 8.2 | +3.46 | 11.9 | 0.45 | 41.4 | keep collecting (29/30) |
| money_level+rlm_ratio | total | 4-2 | 66.7 | 54.3 | 12.4 | +1.68 | 28.0 | 0.83 | 50.0 | keep collecting (6/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 51.4 | 15.2 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 5-4 | 55.6 | 53.3 | 2.2 | +0.59 | 6.5 | 0.33 | 44.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 9-11 | 45.0 | 49.6 | -4.6 | -2.8 | -14.0 | 0.45 | 45.0 | keep collecting (20/30) |
| consensus_gap+money_level | total | 3-3 | 50.0 | 48.6 | 1.4 | -0.34 | -5.7 | -0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 47.4 | 32.6 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 49.0 | -15.6 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 4-6 | 40.0 | 50.9 | -10.9 | -2.44 | -24.4 | -0.1 | 20.0 | keep collecting (10/30) |
| money_moving+rlm_ratio | total | 2-3 | 40.0 | 52.6 | -12.6 | -1.14 | -22.8 | 0.2 | 40.0 | keep collecting (5/30) |
| consensus_gap+follow_move | total | 8-8 | 50.0 | 48.9 | 1.1 | -0.76 | -4.8 | 1.25 | 62.5 | keep collecting (16/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 1-1 | 50.0 | 54.3 | -4.3 | -0.09 | -4.5 | 0.5 | 50.0 | keep collecting (2/30) |

## CLOSE  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 100-106 | 48.5 | 42.9 | 5.6 | +26.73 | 13.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | both | 652-576 | 53.1 | 52.0 | 1.1 | -69.75 | -5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | both | 151-161 | 48.4 | 45.0 | 3.4 | +9.17 | 2.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | both | 796-605 | 56.8 | 55.4 | 1.4 | -68.72 | -4.9 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 621-734 | 45.8 | 47.3 | -1.5 | -92.36 | -6.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | both | 617-739 | 45.5 | 47.5 | -2.0 | -105.46 | -7.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | both | 264-275 | 49.0 | 47.2 | 1.8 | -10.88 | -2.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 50.9 | 15.7 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 257-380 | 40.3 | 45.9 | -5.6 | -86.46 | -13.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+follow_move | both | 101-113 | 47.2 | 49.8 | -2.6 | -20.2 | -9.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_moving | both | 110-206 | 34.8 | 42.8 | -8.0 | -30.55 | -9.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_rlm | both | 18-32 | 36.0 | 36.1 | -0.1 | +12.56 | 25.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_value | both | 104-130 | 44.4 | 44.1 | 0.4 | -10.63 | -4.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | both | 20-38 | 34.5 | 38.4 | -4.0 | -1.02 | -1.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | both | 111-210 | 34.6 | 42.4 | -7.8 | -31.38 | -9.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_moving | both | 346-379 | 47.7 | 49.2 | -1.5 | -59.47 | -8.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_rlm | both | 81-77 | 51.3 | 45.3 | 6.0 | +7.88 | 5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | both | 97-91 | 51.6 | 47.9 | 3.7 | -4.48 | -2.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | both | 151-161 | 48.4 | 45.0 | 3.4 | +9.17 | 2.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 350-374 | 48.3 | 49.2 | -0.8 | -50.85 | -7.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_rlm | both | 97-105 | 48.0 | 42.8 | 5.2 | +24.99 | 12.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | both | 113-138 | 45.0 | 46.2 | -1.2 | -11.31 | -4.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | both | 147-157 | 48.4 | 45.0 | 3.3 | +9.43 | 3.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | both | 596-711 | 45.6 | 47.3 | -1.7 | -92.26 | -7.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+pin_value | both | 28-26 | 51.9 | 45.2 | 6.7 | +16.74 | 31.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_ratio | both | 81-77 | 51.3 | 45.3 | 6.0 | +7.88 | 5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | both | 100-106 | 48.5 | 42.9 | 5.6 | +26.73 | 13.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 28-22 | 56.0 | 48.7 | 7.3 | +3.7 | 7.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | both | 115-137 | 45.6 | 46.3 | -0.7 | -8.55 | -3.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio+sharp_gap | both | 151-161 | 48.4 | 45.0 | 3.4 | +9.17 | 2.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+money_moving | both | 435-409 | 51.5 | 52.0 | -0.5 | -48.42 | -5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | both | 435-404 | 51.8 | 51.9 | -0.1 | -40.24 | -4.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | both | 435-318 | 57.8 | 56.3 | 1.5 | -46.7 | -6.2 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 78-62 | 55.7 | 49.4 | 6.3 | +11.66 | 8.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | both | 156-139 | 52.9 | 56.3 | -3.4 | -26.12 | -8.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | both | 123-125 | 49.6 | 48.7 | 0.9 | -18.15 | -7.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | both | 47-31 | 60.3 | 48.5 | 11.8 | +13.99 | 17.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 54.3 | 45.7 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 26-53 | 32.9 | 27.7 | 5.2 | +11.98 | 15.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm | spread | 17-16 | 51.5 | 51.1 | 0.4 | -0.62 | -1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm | total | 57-37 | 60.6 | 52.8 | 7.8 | +15.36 | 16.3 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move | moneyline | 235-152 | 60.7 | 57.3 | 3.4 | -24.57 | -6.3 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 192-193 | 49.9 | 49.1 | 0.8 | -19.46 | -5.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | total | 225-231 | 49.3 | 50.0 | -0.7 | -25.72 | -5.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | moneyline | 26-64 | 28.9 | 28.5 | 0.3 | -8.07 | -9.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio | spread | 33-34 | 49.3 | 50.0 | -0.8 | -3.97 | -5.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | total | 92-63 | 59.4 | 52.4 | 7.0 | +21.21 | 13.7 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level | moneyline | 312-113 | 73.4 | 69.8 | 3.6 | -14.87 | -3.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 231-245 | 48.5 | 49.0 | -0.5 | -36.88 | -7.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level | total | 253-247 | 50.6 | 49.3 | 1.3 | -16.98 | -3.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 138-254 | 35.2 | 40.1 | -4.9 | -51.15 | -13.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| sharp_gap | spread | 239-231 | 50.9 | 49.5 | 1.3 | -15.18 | -3.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 244-249 | 49.5 | 51.0 | -1.5 | -26.04 | -5.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | moneyline | 142-248 | 36.4 | 40.8 | -4.4 | -45.82 | -11.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | spread | 236-234 | 50.2 | 49.4 | 0.8 | -21.05 | -4.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | total | 239-257 | 48.2 | 50.8 | -2.7 | -38.6 | -7.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | moneyline | 13-44 | 22.8 | 28.4 | -5.6 | -2.9 | -5.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | spread | 124-111 | 52.8 | 49.6 | 3.2 | -2.24 | -1.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 127-120 | 51.4 | 49.1 | 2.3 | -5.73 | -2.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.8 | 47.2 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 104-224 | 31.7 | 43.7 | -12.0 | -63.89 | -19.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 72-65 | 52.6 | 49.0 | 3.6 | -3.46 | -2.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap | total | 81-91 | 47.1 | 47.7 | -0.6 | -19.11 | -11.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | moneyline | 95-61 | 60.9 | 63.0 | -2.1 | -8.33 | -5.3 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 91-60 | 60.3 | 62.6 | -2.4 | -7.83 | -5.2 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 128-238 | 35.0 | 39.8 | -4.9 | -44.29 | -12.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+follow_move | moneyline | 39-57 | 40.6 | 52.5 | -11.9 | -17.96 | -18.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | moneyline | 70-50 | 58.3 | 68.9 | -10.6 | -11.95 | -10.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | moneyline | 36-128 | 22.0 | 37.6 | -15.7 | -16.8 | -10.2 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+money_level | moneyline | 188-59 | 76.1 | 71.4 | 4.7 | -11.11 | -4.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move+money_moving | moneyline | 71-86 | 45.2 | 47.1 | -1.9 | -15.71 | -10.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 37-133 | 21.8 | 36.9 | -15.2 | -18.65 | -11.0 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+sharp_gap | moneyline | 70-85 | 45.2 | 46.4 | -1.3 | -15.84 | -10.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_rlm | moneyline | 10-22 | 31.2 | 28.9 | 2.4 | +15.65 | 48.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 4-26 | 13.3 | 29.1 | -15.8 | -3.04 | -10.1 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_rlm | moneyline | 16-31 | 34.0 | 28.9 | 5.1 | -5.85 | -12.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 26-64 | 28.9 | 28.5 | 0.3 | -8.07 | -9.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_rlm | moneyline | 26-52 | 33.3 | 27.7 | 5.6 | +12.98 | 16.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 26-61 | 29.9 | 28.6 | 1.2 | -5.07 | -5.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 16-31 | 34.0 | 28.9 | 5.1 | -5.85 | -12.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 26-53 | 32.9 | 27.7 | 5.2 | +11.98 | 15.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 26-64 | 28.9 | 28.5 | 0.3 | -8.07 | -9.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 12-38 | 24.0 | 28.8 | -4.8 | +1.58 | 3.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_value | moneyline | 7-28 | 20.0 | 25.9 | -5.9 | +5.27 | 15.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+pin_value | moneyline | 5-8 | 38.5 | 25.9 | 12.6 | +14.07 | 108.2 |  |  | keep collecting (13/30) |
| pin_value+sharp_gap | moneyline | 7-28 | 20.0 | 25.9 | -5.9 | +5.27 | 15.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_rlm | moneyline | 8-7 | 53.3 | 32.3 | 21.0 | +2.35 | 15.6 |  |  | keep collecting (15/30) |
| money_level+rlm_ratio | moneyline | 10-8 | 55.6 | 36.6 | 19.0 | +3.72 | 20.6 |  |  | keep collecting (18/30) |
| money_level+pin_value | moneyline | 3-1 | 75.0 | 62.1 | 12.9 | +0.31 | 7.8 |  |  | keep collecting (4/30) |
| follow_move+pin_value | moneyline | 1-7 | 12.5 | 25.9 | -13.4 | -5.48 | -68.5 |  |  | keep collecting (8/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 25.9 | -0.9 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 31-24 | 56.4 | 48.1 | 8.3 | +2.4 | 4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | spread | 39-35 | 52.7 | 48.8 | 3.9 | -1.68 | -2.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 49-40 | 55.1 | 48.9 | 6.1 | +1.7 | 1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_ratio | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.33 | -38.9 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | spread | 38-35 | 52.1 | 49.1 | 2.9 | -2.58 | -3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | spread | 123-125 | 49.6 | 48.9 | 0.7 | -14.36 | -5.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_rlm | spread | 15-15 | 50.0 | 50.9 | -0.9 | -1.37 | -4.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | spread | 48-39 | 55.2 | 48.7 | 6.5 | +2.87 | 3.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | spread | 33-34 | 49.3 | 50.0 | -0.8 | -3.97 | -5.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 124-124 | 50.0 | 48.9 | 1.1 | -12.23 | -4.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | spread | 15-16 | 48.4 | 51.0 | -2.6 | -2.44 | -7.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | spread | 58-57 | 50.4 | 49.1 | 1.3 | -6.77 | -5.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_ratio | spread | 31-33 | 48.4 | 49.9 | -1.5 | -4.9 | -7.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | spread | 231-226 | 50.5 | 49.5 | 1.1 | -17.55 | -3.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+pin_value | spread | 6-7 | 46.2 | 50.2 | -4.1 | -1.79 | -13.8 |  |  | keep collecting (13/30) |
| pin_rlm+rlm_ratio | spread | 15-15 | 50.0 | 50.9 | -0.9 | -1.37 | -4.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | spread | 17-16 | 51.5 | 51.1 | 0.4 | -0.62 | -1.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 5-6 | 45.5 | 49.2 | -3.8 | -1.72 | -15.6 |  |  | keep collecting (11/30) |
| pin_value+sharp_gap | spread | 58-57 | 50.4 | 49.2 | 1.2 | -6.84 | -5.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | spread | 33-34 | 49.3 | 50.0 | -0.8 | -3.97 | -5.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 118-124 | 48.8 | 48.5 | 0.3 | -17.91 | -7.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+rlm_ratio | spread | 17-19 | 47.2 | 49.5 | -2.3 | -3.71 | -10.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | spread | 180-179 | 50.1 | 49.1 | 1.1 | -16.91 | -4.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | spread | 48-40 | 54.5 | 48.6 | 6.0 | +1.17 | 1.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | spread | 179-180 | 49.9 | 49.0 | 0.8 | -18.83 | -5.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | spread | 62-65 | 48.8 | 48.8 | 0.0 | -11.37 | -9.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_rlm | spread | 8-6 | 57.1 | 50.4 | 6.7 | +1.1 | 7.9 |  |  | keep collecting (14/30) |
| money_level+money_moving | total | 161-168 | 48.9 | 50.1 | -1.2 | -21.27 | -6.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | total | 164-165 | 49.8 | 50.2 | -0.3 | -15.51 | -4.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | total | 237-247 | 49.0 | 50.9 | -2.0 | -30.42 | -6.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | total | 38-49 | 43.7 | 46.7 | -3.0 | -15.34 | -17.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_value | total | 43-52 | 45.3 | 47.5 | -2.2 | -13.91 | -14.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | total | 152-168 | 47.5 | 50.6 | -3.1 | -29.4 | -9.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+sharp_gap | total | 156-165 | 48.6 | 50.7 | -2.1 | -22.78 | -7.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | total | 58-59 | 49.6 | 48.1 | 1.5 | -7.09 | -6.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | total | 129-135 | 48.9 | 49.3 | -0.5 | -17.68 | -6.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 48-45 | 51.6 | 49.1 | 2.5 | -1.87 | -2.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | total | 48-53 | 47.5 | 50.0 | -2.4 | -9.81 | -9.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | total | 50-52 | 49.0 | 50.1 | -1.1 | -6.99 | -6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | total | 35-43 | 44.9 | 47.8 | -2.9 | -12.06 | -15.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+sharp_gap | total | 36-42 | 46.2 | 47.9 | -1.8 | -10.15 | -13.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+follow_move | total | 31-32 | 49.2 | 47.1 | 2.1 | -4.64 | -7.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pin_rlm | total | 5-7 | 41.7 | 48.6 | -6.9 | -2.6 | -21.7 |  |  | keep collecting (12/30) |
| consensus_gap+rlm_ratio | total | 14-8 | 63.6 | 48.0 | 15.6 | +4.35 | 19.8 |  |  | keep collecting (22/30) |
| follow_move+pin_rlm | total | 50-31 | 61.7 | 52.7 | 9.0 | +15.1 | 18.6 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move+rlm_ratio | total | 92-63 | 59.4 | 52.4 | 7.0 | +21.21 | 13.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 31-18 | 63.3 | 52.9 | 10.4 | +10.54 | 21.5 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 51-35 | 59.3 | 52.0 | 7.3 | +11.65 | 13.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | total | 56-37 | 60.2 | 52.8 | 7.4 | +14.45 | 15.5 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+rlm_ratio | total | 90-63 | 58.8 | 52.3 | 6.5 | +19.41 | 12.7 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| pin_rlm+pin_value | total | 17-11 | 60.7 | 51.8 | 8.9 | +4.46 | 15.9 |  |  | keep collecting (28/30) |
| pin_rlm+rlm_ratio | total | 50-31 | 61.7 | 52.7 | 9.0 | +15.1 | 18.6 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| pin_rlm+sharp_gap | total | 57-37 | 60.6 | 52.8 | 7.8 | +15.36 | 16.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 22-13 | 62.9 | 51.1 | 11.8 | +6.89 | 19.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | total | 92-63 | 59.4 | 52.4 | 7.0 | +21.21 | 13.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 54.3 | 45.7 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

# Pooled (fit + forward together)

Kept for continuity. **Contaminated** — it mixes the games the engine was built
on with the games testing it. Use the forward table for any decision.

## EARLY  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 1-1 | 50.0 | 25.8 | 24.2 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | both | 341-318 | 51.7 | 52.5 | -0.8 | -67.54 | -10.2 | 0.23 | 42.6 | no edge shown yet |
| rlm_ratio | both | 17-15 | 53.1 | 37.4 | 15.7 | +9.23 | 28.9 | 0.08 | 46.9 | no edge shown yet |
| money_level | both | 123-76 | 61.8 | 58.9 | 3.0 | -7.22 | -3.6 | 0.18 | 41.7 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 106-81 | 56.7 | 49.1 | 7.5 | +22.67 | 12.1 | 0.31 | 42.2 | no edge shown yet |
| money_moving | both | 72-51 | 58.5 | 51.1 | 7.4 | +9.1 | 7.4 | 0.14 | 42.3 | no edge shown yet |
| pin_value | both | 43-42 | 50.6 | 47.9 | 2.7 | -3.68 | -4.3 | 0.14 | 41.2 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.6 | -31.6 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 170-229 | 42.6 | 46.5 | -3.9 | -54.34 | -13.6 | 0.32 | 45.1 | DROP: below break-even |
| consensus_gap+money_level | both | 23-22 | 51.1 | 63.3 | -12.2 | -10.62 | -23.6 | 0.25 | 46.7 | no edge shown yet |
| consensus_gap+money_moving | both | 15-20 | 42.9 | 45.2 | -2.4 | -4.7 | -13.4 | 0.17 | 37.1 | no edge shown yet |
| consensus_gap+pin_value | both | 17-27 | 38.6 | 45.6 | -7.0 | -12.16 | -27.6 | 0.43 | 52.3 | DROP: below break-even |
| follow_move+rlm_ratio | both | 17-15 | 53.1 | 37.4 | 15.7 | +9.23 | 28.9 | 0.08 | 46.9 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 52-29 | 64.2 | 49.9 | 14.3 | +15.17 | 18.7 | 0.44 | 48.1 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 47-27 | 63.5 | 57.3 | 6.2 | +2.81 | 3.8 | 0.06 | 48.6 | PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | both | 10-8 | 55.6 | 50.5 | 5.0 | +0.9 | 5.0 | 0.5 | 50.0 | keep collecting (18/30) |
| money_moving+pin_value | both | 7-5 | 58.3 | 50.1 | 8.3 | +1.13 | 9.4 | 0.42 | 41.7 | keep collecting (12/30) |
| rlm_ratio+sharp_gap | both | 17-15 | 53.1 | 37.4 | 15.7 | +9.23 | 28.9 | 0.08 | 46.9 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 73-41 | 64.0 | 55.8 | 8.3 | +7.81 | 6.9 | 0.42 | 45.6 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 45-29 | 60.8 | 49.5 | 11.3 | +12.05 | 16.3 | 0.34 | 44.6 | no edge shown yet |
| pin_value+sharp_gap | both | 12-7 | 63.2 | 49.1 | 14.0 | +3.75 | 19.8 | -0.15 | 36.8 | keep collecting (19/30) |
| consensus_gap+follow_move | both | 24-34 | 41.4 | 50.9 | -9.5 | -15.5 | -26.7 | 0.77 | 56.9 | DROP: below break-even |
| follow_move+pin_value | both | 18-17 | 51.4 | 47.7 | 3.7 | -1.2 | -3.4 | -0.08 | 31.4 | no edge shown yet |
| consensus_gap+sharp_gap | both | 19-35 | 35.2 | 45.7 | -10.6 | -6.74 | -12.5 | 0.6 | 44.4 | DROP: below break-even |
| follow_move+money_level | both | 67-36 | 65.0 | 58.8 | 6.3 | -3.41 | -3.3 | 0.33 | 44.7 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 9-6 | 60.0 | 42.2 | 17.8 | +2.84 | 18.9 | 1.01 | 53.3 | keep collecting (15/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 44.8 | 5.2 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 33-17 | 66.0 | 52.3 | 13.7 | +7.81 | 15.6 | 0.49 | 56.0 | PROMOTE: beats break-even and its own base rate |
| money_moving+rlm_ratio | both | 6-5 | 54.5 | 42.1 | 12.4 | +2.5 | 22.7 | -0.05 | 45.5 | keep collecting (11/30) |
| consensus_gap+rlm_ratio | both | 1-4 | 20.0 | 36.9 | -16.9 | -3.09 | -61.8 | 0.2 | 60.0 | keep collecting (5/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 25.8 | 24.2 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 25.8 | 24.2 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 1-1 | 50.0 | 25.8 | 24.2 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 53.1 | -53.1 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 53.5 | -53.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 25.8 | 74.2 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-1 | 50.0 | 25.8 | 24.2 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | moneyline | 142-97 | 59.4 | 57.8 | 1.6 | -28.99 | -12.1 | 0.37 | 48.1 | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 98-116 | 45.8 | 49.4 | -3.6 | -25.81 | -12.1 | -0.02 | 33.6 | DROP: below break-even |
| follow_move | total | 101-105 | 49.0 | 49.6 | -0.6 | -12.74 | -6.2 | 0.33 | 45.6 | no edge shown yet |
| rlm_ratio | moneyline | 9-9 | 50.0 | 25.8 | 24.2 | +7.81 | 43.4 | 0.14 | 61.1 | keep collecting (18/30) |
| rlm_ratio | spread | 3-2 | 60.0 | 51.6 | 8.4 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 5-4 | 55.6 | 52.7 | 2.8 | +0.59 | 6.5 | 0.33 | 44.4 | keep collecting (9/30) |
| money_level | moneyline | 68-27 | 71.6 | 69.6 | 1.9 | -8.11 | -8.5 | 0.11 | 46.3 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 16-16 | 50.0 | 49.2 | 0.8 | -1.6 | -5.0 | 0.81 | 46.9 | no edge shown yet |
| money_level | total | 39-33 | 54.2 | 48.9 | 5.2 | +2.48 | 3.4 | -0.01 | 33.3 | no edge shown yet |
| sharp_gap | moneyline | 44-39 | 53.0 | 47.4 | 5.6 | +8.4 | 10.1 | 0.29 | 48.2 | no edge shown yet |
| sharp_gap | spread | 19-14 | 57.6 | 49.8 | 7.8 | +3.09 | 9.4 | 0.61 | 36.4 | no edge shown yet |
| sharp_gap | total | 43-28 | 60.6 | 50.9 | 9.6 | +11.17 | 15.7 | 0.21 | 38.0 | no edge shown yet |
| money_moving | moneyline | 28-27 | 50.9 | 53.1 | -2.2 | -6.68 | -12.1 | 0.1 | 52.7 | no edge shown yet |
| money_moving | spread | 17-4 | 81.0 | 49.1 | 31.8 | +11.27 | 53.7 | 0.14 | 38.1 | keep collecting (21/30) |
| money_moving | total | 27-20 | 57.4 | 49.8 | 7.7 | +4.51 | 9.6 | 0.17 | 31.9 | no edge shown yet |
| pin_value | moneyline | 1-5 | 16.7 | 25.8 | -9.1 | -4.02 | -67.0 | -0.02 | 66.7 | keep collecting (6/30) |
| pin_value | spread | 22-17 | 56.4 | 49.3 | 7.2 | +2.35 | 6.0 | 0.28 | 41.0 | no edge shown yet |
| pin_value | total | 20-20 | 50.0 | 49.8 | 0.2 | -2.01 | -5.0 | 0.03 | 37.5 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.6 | -19.3 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 68-125 | 35.2 | 43.6 | -8.4 | -40.57 | -21.0 | 0.0 | 42.0 | DROP: below break-even |
| consensus_gap | spread | 55-51 | 51.9 | 49.1 | 2.8 | -2.98 | -2.8 | 0.46 | 43.4 | no edge shown yet |
| consensus_gap | total | 47-53 | 47.0 | 49.4 | -2.4 | -10.78 | -10.8 | 0.76 | 53.0 | no edge shown yet |
| money_level+sharp_gap | moneyline | 34-12 | 73.9 | 64.7 | 9.2 | +1.42 | 3.1 | 0.37 | 56.5 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+follow_move | moneyline | 8-18 | 30.8 | 53.7 | -23.0 | -13.56 | -52.1 | 0.36 | 61.5 | keep collecting (26/30) |
| consensus_gap+pin_value | moneyline | 1-5 | 16.7 | 25.8 | -9.1 | -4.02 | -67.0 | -0.02 | 66.7 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_value | moneyline | 0-2 | 0.0 | 25.8 | -25.8 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| money_level+money_moving | moneyline | 19-9 | 67.9 | 70.8 | -2.9 | -4.74 | -16.9 | -0.29 | 57.1 | keep collecting (28/30) |
| consensus_gap+sharp_gap | moneyline | 11-26 | 29.7 | 44.1 | -14.4 | -4.71 | -12.7 | 0.5 | 45.9 | DROP: below break-even |
| follow_move+money_level | moneyline | 40-12 | 76.9 | 68.6 | 8.3 | -3.97 | -7.6 | 0.19 | 48.1 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 15-5 | 75.0 | 57.3 | 17.7 | +3.39 | 16.9 | 0.66 | 75.0 | keep collecting (20/30) |
| consensus_gap+money_level | moneyline | 16-14 | 53.3 | 71.0 | -17.7 | -8.68 | -28.9 | -0.09 | 46.7 | INVERT candidate: wrong well beyond its base rate |
| follow_move+sharp_gap | moneyline | 25-11 | 69.4 | 50.0 | 19.4 | +8.63 | 24.0 | 0.36 | 58.3 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 16-14 | 53.3 | 48.4 | 4.9 | +0.78 | 2.6 | 0.4 | 60.0 | no edge shown yet |
| consensus_gap+money_moving | moneyline | 7-19 | 26.9 | 44.4 | -17.5 | -10.63 | -40.9 | 0.26 | 46.2 | keep collecting (26/30) |
| follow_move+rlm_ratio | moneyline | 9-9 | 50.0 | 25.8 | 24.2 | +7.81 | 43.4 | 0.14 | 61.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 9-9 | 50.0 | 25.8 | 24.2 | +7.81 | 43.4 | 0.14 | 61.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 0-3 | 0.0 | 25.8 | -25.8 | -3.0 | -100.0 | 0.0 | 66.7 | keep collecting (3/30) |
| money_moving+rlm_ratio | moneyline | 2-2 | 50.0 | 25.8 | 24.2 | +1.78 | 44.5 | 0.1 | 75.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-1 | 50.0 | 25.8 | 24.2 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-1 | 50.0 | 25.8 | 24.2 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 1-1 | 50.0 | 25.8 | 24.2 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| money_level+rlm_ratio | moneyline | 3-3 | 50.0 | 25.8 | 24.2 | +0.23 | 3.8 | 1.7 | 83.3 | keep collecting (6/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 25.8 | 74.2 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 4-5 | 44.4 | 47.4 | -2.9 | -1.59 | -17.7 | 1.67 | 66.7 | keep collecting (9/30) |
| consensus_gap+money_moving | spread | 4-0 | 100.0 | 47.4 | 52.6 | +3.41 | 85.2 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_value | spread | 9-8 | 52.9 | 48.3 | 4.7 | -0.31 | -1.8 | 0.53 | 52.9 | keep collecting (17/30) |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.6 | 8.4 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 48.7 | 13.8 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 9-4 | 69.2 | 48.6 | 20.7 | +4.21 | 32.4 | 0.77 | 61.5 | keep collecting (13/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.9 | -6.0 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.5 | 10.5 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 51.6 | 8.4 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 13-11 | 54.2 | 49.1 | 5.0 | +0.71 | 3.0 | 0.96 | 41.7 | keep collecting (24/30) |
| money_moving+sharp_gap | spread | 9-3 | 75.0 | 49.1 | 25.9 | +5.13 | 42.7 | 0.42 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.1 | 17.5 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 8-8 | 50.0 | 48.0 | 2.0 | -1.18 | -7.4 | 0.94 | 43.8 | keep collecting (16/30) |
| consensus_gap+sharp_gap | spread | 4-3 | 57.1 | 47.4 | 9.8 | +0.41 | 5.8 | 2.14 | 71.4 | keep collecting (7/30) |
| follow_move+money_level | spread | 11-8 | 57.9 | 48.5 | 9.4 | +2.04 | 10.7 | 0.63 | 42.1 | keep collecting (19/30) |
| follow_move+pin_value | spread | 11-7 | 61.1 | 48.8 | 12.3 | +2.56 | 14.2 | 0.33 | 33.3 | keep collecting (18/30) |
| follow_move+money_moving | spread | 9-1 | 90.0 | 47.9 | 42.1 | +7.22 | 72.2 | 0.2 | 40.0 | keep collecting (10/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 52.6 | 14.0 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.6 | -52.6 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 19-14 | 57.6 | 49.3 | 8.3 | +3.34 | 10.1 | 0.09 | 36.4 | no edge shown yet |
| money_level+sharp_gap | total | 26-18 | 59.1 | 50.0 | 9.1 | +5.68 | 12.9 | 0.18 | 36.4 | no edge shown yet |
| money_moving+sharp_gap | total | 20-12 | 62.5 | 50.7 | 11.8 | +6.14 | 19.2 | 0.25 | 31.2 | no edge shown yet |
| money_level+pin_value | total | 7-4 | 63.6 | 51.6 | 12.1 | +2.32 | 21.1 | 0.36 | 36.4 | keep collecting (11/30) |
| money_moving+pin_value | total | 4-3 | 57.1 | 50.5 | 6.6 | +0.56 | 8.0 | 0.29 | 28.6 | keep collecting (7/30) |
| pin_value+sharp_gap | total | 10-5 | 66.7 | 50.7 | 16.0 | +4.01 | 26.7 | 0.0 | 33.3 | keep collecting (15/30) |
| follow_move+money_level | total | 16-16 | 50.0 | 48.9 | 1.1 | -1.47 | -4.6 | 0.38 | 40.6 | no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.3 | -2.6 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 5-4 | 55.6 | 52.7 | 2.8 | +0.59 | 6.5 | 0.33 | 44.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 17-12 | 58.6 | 50.4 | 8.3 | +3.46 | 11.9 | 0.45 | 41.4 | keep collecting (29/30) |
| money_level+rlm_ratio | total | 4-2 | 66.7 | 53.5 | 13.2 | +1.68 | 28.0 | 0.83 | 50.0 | keep collecting (6/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 51.2 | 15.5 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 5-4 | 55.6 | 52.7 | 2.8 | +0.59 | 6.5 | 0.33 | 44.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 9-11 | 45.0 | 49.7 | -4.7 | -2.8 | -14.0 | 0.45 | 45.0 | keep collecting (20/30) |
| consensus_gap+money_level | total | 3-3 | 50.0 | 48.8 | 1.2 | -0.34 | -5.7 | -0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 47.9 | 32.1 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 49.2 | -15.8 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 4-6 | 40.0 | 50.7 | -10.7 | -2.44 | -24.4 | -0.1 | 20.0 | keep collecting (10/30) |
| money_moving+rlm_ratio | total | 2-3 | 40.0 | 52.1 | -12.1 | -1.14 | -22.8 | 0.2 | 40.0 | keep collecting (5/30) |
| consensus_gap+follow_move | total | 8-8 | 50.0 | 49.1 | 0.9 | -0.76 | -4.8 | 1.25 | 62.5 | keep collecting (16/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 53.5 | -53.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 53.5 | -53.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 1-1 | 50.0 | 53.5 | -3.5 | -0.09 | -4.5 | 0.5 | 50.0 | keep collecting (2/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 107-111 | 49.1 | 42.5 | 6.6 | +33.03 | 15.2 |  |  | no edge shown yet |
| follow_move | both | 675-599 | 53.0 | 52.2 | 0.8 | -74.89 | -5.9 |  |  | no edge shown yet |
| rlm_ratio | both | 157-165 | 48.8 | 44.6 | 4.2 | +15.6 | 4.8 |  |  | no edge shown yet |
| money_level | both | 832-624 | 57.1 | 55.5 | 1.6 | -63.07 | -4.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 649-759 | 46.1 | 47.2 | -1.1 | -89.24 | -6.3 |  |  | DROP: below break-even |
| money_moving | both | 646-763 | 45.8 | 47.4 | -1.5 | -101.32 | -7.2 |  |  | DROP: below break-even |
| pin_value | both | 272-286 | 48.7 | 47.3 | 1.5 | -14.78 | -2.6 |  |  | DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 50.9 | 15.8 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 265-393 | 40.3 | 45.9 | -5.6 | -88.01 | -13.4 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 101-116 | 46.5 | 50.0 | -3.4 | -23.2 | -10.7 |  |  | DROP: below break-even |
| consensus_gap+money_moving | both | 114-212 | 35.0 | 42.7 | -7.7 | -33.1 | -10.2 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 19-33 | 36.5 | 36.3 | 0.2 | +12.47 | 24.0 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 107-133 | 44.6 | 44.3 | 0.3 | -10.98 | -4.6 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | both | 20-39 | 33.9 | 38.3 | -4.4 | -2.02 | -3.4 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 115-216 | 34.7 | 42.3 | -7.6 | -33.94 | -10.3 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 358-388 | 48.0 | 49.3 | -1.3 | -55.62 | -7.5 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 85-79 | 51.8 | 44.8 | 7.1 | +14.5 | 8.8 |  |  | no edge shown yet |
| follow_move+pin_value | both | 98-93 | 51.3 | 48.1 | 3.2 | -5.57 | -2.9 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 157-165 | 48.8 | 44.6 | 4.2 | +15.6 | 4.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 361-383 | 48.5 | 49.1 | -0.6 | -47.03 | -6.3 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 104-110 | 48.6 | 42.4 | 6.2 | +31.3 | 14.6 |  |  | no edge shown yet |
| money_moving+pin_value | both | 118-143 | 45.2 | 46.3 | -1.1 | -11.94 | -4.6 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 153-161 | 48.7 | 44.6 | 4.1 | +15.87 | 5.1 |  |  | no edge shown yet |
| money_moving+sharp_gap | both | 624-735 | 45.9 | 47.2 | -1.3 | -88.14 | -6.5 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 30-27 | 52.6 | 45.3 | 7.3 | +17.52 | 30.7 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 85-79 | 51.8 | 44.8 | 7.1 | +14.5 | 8.8 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 107-111 | 49.1 | 42.5 | 6.6 | +33.03 | 15.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 28-22 | 56.0 | 48.5 | 7.5 | +3.7 | 7.4 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 120-142 | 45.8 | 46.4 | -0.6 | -9.19 | -3.5 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 157-165 | 48.8 | 44.6 | 4.2 | +15.6 | 4.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+money_moving | both | 457-419 | 52.2 | 52.0 | 0.2 | -39.09 | -4.5 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 456-414 | 52.4 | 51.9 | 0.5 | -30.93 | -3.6 |  |  | no edge shown yet |
| follow_move+money_level | both | 454-329 | 58.0 | 56.5 | 1.5 | -46.18 | -5.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 83-64 | 56.5 | 49.0 | 7.5 | +16.59 | 11.3 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 160-141 | 53.2 | 56.5 | -3.4 | -25.12 | -8.3 |  |  | no edge shown yet |
| money_level+pin_value | both | 128-130 | 49.6 | 48.9 | 0.7 | -18.78 | -7.3 |  |  | no edge shown yet |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | both | 52-32 | 61.9 | 47.9 | 14.0 | +19.89 | 23.7 |  |  | PROMOTE: beats break-even and its own base rate |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 53.5 | 46.5 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 28-56 | 33.3 | 27.5 | 5.8 | +15.78 | 18.8 |  |  | DROP: below break-even |
| pin_rlm | spread | 18-17 | 51.4 | 51.0 | 0.4 | -0.71 | -2.0 |  |  | no edge shown yet |
| pin_rlm | total | 61-38 | 61.6 | 52.2 | 9.4 | +17.96 | 18.1 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move | moneyline | 247-156 | 61.3 | 57.5 | 3.8 | -20.9 | -5.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 196-204 | 49.0 | 49.2 | -0.2 | -26.68 | -6.7 |  |  | no edge shown yet |
| follow_move | total | 232-239 | 49.3 | 50.0 | -0.8 | -27.31 | -5.8 |  |  | no edge shown yet |
| rlm_ratio | moneyline | 28-66 | 29.8 | 28.4 | 1.4 | -3.27 | -3.5 |  |  | DROP: below break-even |
| rlm_ratio | spread | 33-35 | 48.5 | 50.0 | -1.5 | -4.97 | -7.3 |  |  | no edge shown yet |
| rlm_ratio | total | 96-64 | 60.0 | 51.8 | 8.2 | +23.85 | 14.9 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level | moneyline | 327-115 | 74.0 | 69.8 | 4.1 | -11.31 | -2.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 241-254 | 48.7 | 49.1 | -0.4 | -36.75 | -7.4 |  |  | DROP: below break-even |
| money_level | total | 264-255 | 50.9 | 49.4 | 1.5 | -15.01 | -2.9 |  |  | no edge shown yet |
| sharp_gap | moneyline | 144-264 | 35.3 | 39.9 | -4.6 | -52.92 | -13.0 |  |  | DROP: below break-even |
| sharp_gap | spread | 250-239 | 51.1 | 49.5 | 1.6 | -13.25 | -2.7 |  |  | no edge shown yet |
| sharp_gap | total | 255-256 | 49.9 | 50.8 | -0.9 | -23.07 | -4.5 |  |  | no edge shown yet |
| money_moving | moneyline | 149-257 | 36.7 | 40.7 | -4.0 | -46.57 | -11.5 |  |  | DROP: below break-even |
| money_moving | spread | 247-242 | 50.5 | 49.5 | 1.1 | -19.12 | -3.9 |  |  | no edge shown yet |
| money_moving | total | 250-264 | 48.6 | 50.7 | -2.0 | -35.63 | -6.9 |  |  | DROP: below break-even |
| pin_value | moneyline | 13-45 | 22.4 | 28.3 | -5.9 | -3.9 | -6.7 |  |  | DROP: below break-even |
| pin_value | spread | 127-116 | 52.3 | 49.6 | 2.6 | -4.65 | -1.9 |  |  | no edge shown yet |
| pin_value | total | 132-125 | 51.4 | 49.3 | 2.1 | -6.23 | -2.4 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.6 | 47.4 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 106-234 | 31.2 | 43.4 | -12.3 | -67.67 | -19.9 |  |  | DROP: below break-even |
| consensus_gap | spread | 74-67 | 52.5 | 49.0 | 3.4 | -3.8 | -2.7 |  |  | no edge shown yet |
| consensus_gap | total | 85-92 | 48.0 | 48.1 | -0.1 | -16.55 | -9.3 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 101-61 | 62.3 | 62.9 | -0.5 | -3.58 | -2.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 96-60 | 61.5 | 62.4 | -0.9 | -3.1 | -2.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 134-247 | 35.2 | 39.6 | -4.5 | -45.07 | -11.8 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 39-59 | 39.8 | 52.5 | -12.7 | -19.96 | -20.4 |  |  | DROP: below break-even |
| consensus_gap+money_level | moneyline | 71-51 | 58.2 | 69.1 | -10.9 | -12.52 | -10.3 |  |  | no edge shown yet |
| consensus_gap+money_moving | moneyline | 36-133 | 21.3 | 37.2 | -15.9 | -21.8 | -12.9 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+money_level | moneyline | 199-60 | 76.8 | 71.4 | 5.4 | -7.93 | -3.1 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 77-88 | 46.7 | 47.2 | -0.5 | -10.38 | -6.3 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | moneyline | 37-138 | 21.1 | 36.6 | -15.4 | -23.65 | -13.5 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+sharp_gap | moneyline | 75-87 | 46.3 | 46.4 | -0.1 | -10.54 | -6.5 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | moneyline | 10-23 | 30.3 | 28.7 | 1.6 | +14.65 | 44.4 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 4-27 | 12.9 | 28.9 | -16.0 | -4.04 | -13.0 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_rlm | moneyline | 18-32 | 36.0 | 28.7 | 7.3 | -0.05 | -0.1 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 28-66 | 29.8 | 28.4 | 1.4 | -3.27 | -3.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_rlm | moneyline | 28-55 | 33.7 | 27.5 | 6.2 | +16.78 | 20.2 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 28-63 | 30.8 | 28.4 | 2.3 | -0.27 | -0.3 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 18-32 | 36.0 | 28.7 | 7.3 | -0.05 | -0.1 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 28-56 | 33.3 | 27.5 | 5.8 | +15.78 | 18.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 28-66 | 29.8 | 28.4 | 1.4 | -3.27 | -3.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 12-39 | 23.5 | 28.6 | -5.1 | +0.58 | 1.1 |  |  | DROP: below break-even |
| money_moving+pin_value | moneyline | 7-29 | 19.4 | 25.8 | -6.3 | +4.27 | 11.9 |  |  | DROP: below break-even |
| pin_rlm+pin_value | moneyline | 5-8 | 38.5 | 25.8 | 12.7 | +14.07 | 108.2 |  |  | keep collecting (13/30) |
| pin_value+sharp_gap | moneyline | 7-29 | 19.4 | 25.8 | -6.3 | +4.27 | 11.9 |  |  | DROP: below break-even |
| money_level+pin_rlm | moneyline | 9-7 | 56.2 | 31.8 | 24.4 | +5.65 | 35.3 |  |  | keep collecting (16/30) |
| money_level+rlm_ratio | moneyline | 11-8 | 57.9 | 36.0 | 21.9 | +7.02 | 36.9 |  |  | keep collecting (19/30) |
| money_level+pin_value | moneyline | 3-1 | 75.0 | 62.1 | 12.9 | +0.31 | 7.8 |  |  | keep collecting (4/30) |
| follow_move+pin_value | moneyline | 1-7 | 12.5 | 25.8 | -13.3 | -5.48 | -68.5 |  |  | keep collecting (8/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 25.8 | -0.8 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 31-25 | 55.4 | 48.3 | 7.1 | +1.4 | 2.5 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 41-36 | 53.2 | 48.9 | 4.4 | -1.02 | -1.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 50-41 | 54.9 | 49.0 | 6.0 | +1.53 | 1.7 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.33 | -38.9 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | spread | 40-36 | 52.6 | 49.1 | 3.5 | -1.91 | -2.5 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 124-128 | 49.2 | 49.0 | 0.3 | -16.38 | -6.5 |  |  | no edge shown yet |
| follow_move+pin_rlm | spread | 15-15 | 50.0 | 50.9 | -0.9 | -1.37 | -4.6 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 49-41 | 54.4 | 48.9 | 5.6 | +1.78 | 2.0 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 33-35 | 48.5 | 50.0 | -1.5 | -4.97 | -7.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 125-127 | 49.6 | 49.0 | 0.6 | -14.25 | -5.7 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 16-17 | 48.5 | 50.9 | -2.4 | -2.53 | -7.7 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 60-60 | 50.0 | 49.2 | 0.8 | -8.09 | -6.7 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 31-34 | 47.7 | 49.9 | -2.2 | -5.9 | -9.1 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 242-234 | 50.8 | 49.5 | 1.4 | -15.62 | -3.3 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 6-8 | 42.9 | 50.4 | -7.5 | -2.79 | -19.9 |  |  | keep collecting (14/30) |
| pin_rlm+rlm_ratio | spread | 15-15 | 50.0 | 50.9 | -0.9 | -1.37 | -4.6 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 18-17 | 51.4 | 51.0 | 0.4 | -0.71 | -2.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 5-6 | 45.5 | 49.3 | -3.8 | -1.72 | -15.6 |  |  | keep collecting (11/30) |
| pin_value+sharp_gap | spread | 60-60 | 50.0 | 49.3 | 0.7 | -8.16 | -6.8 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 33-35 | 48.5 | 50.0 | -1.5 | -4.97 | -7.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 121-130 | 48.2 | 48.7 | -0.5 | -21.11 | -8.4 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 17-20 | 45.9 | 49.5 | -3.6 | -4.71 | -12.7 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 188-185 | 50.4 | 49.1 | 1.3 | -15.6 | -4.2 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 50-41 | 54.9 | 48.6 | 6.3 | +1.84 | 2.0 |  |  | no edge shown yet |
| money_level+money_moving | spread | 187-186 | 50.1 | 49.1 | 1.0 | -17.51 | -4.7 |  |  | no edge shown yet |
| money_level+pin_value | spread | 65-68 | 48.9 | 48.9 | -0.1 | -11.78 | -8.9 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 9-6 | 60.0 | 50.2 | 9.8 | +2.01 | 13.4 |  |  | keep collecting (15/30) |
| money_level+money_moving | total | 169-172 | 49.6 | 50.1 | -0.5 | -17.99 | -5.3 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 172-169 | 50.4 | 50.1 | 0.3 | -12.23 | -3.6 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 248-254 | 49.4 | 50.7 | -1.3 | -27.45 | -5.5 |  |  | no edge shown yet |
| consensus_gap+money_level | total | 39-49 | 44.3 | 47.3 | -3.0 | -14.43 | -16.4 |  |  | DROP: below break-even |
| consensus_gap+pin_value | total | 45-53 | 45.9 | 48.0 | -2.1 | -13.09 | -13.4 |  |  | no edge shown yet |
| follow_move+money_moving | total | 157-172 | 47.7 | 50.5 | -2.8 | -28.86 | -8.8 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 161-169 | 48.8 | 50.5 | -1.8 | -22.24 | -6.7 |  |  | no edge shown yet |
| money_level+pin_value | total | 60-61 | 49.6 | 48.4 | 1.2 | -7.31 | -6.0 |  |  | no edge shown yet |
| follow_move+money_level | total | 134-139 | 49.1 | 49.5 | -0.4 | -17.14 | -6.3 |  |  | no edge shown yet |
| follow_move+pin_value | total | 48-45 | 51.6 | 49.3 | 2.3 | -1.87 | -2.0 |  |  | no edge shown yet |
| money_moving+pin_value | total | 51-54 | 48.6 | 50.0 | -1.4 | -8.12 | -7.7 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 53-53 | 50.0 | 50.1 | -0.1 | -5.3 | -5.0 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 37-43 | 46.2 | 48.3 | -2.0 | -10.28 | -12.9 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 38-42 | 47.5 | 48.3 | -0.8 | -8.37 | -10.5 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 31-32 | 49.2 | 47.6 | 1.6 | -4.64 | -7.4 |  |  | no edge shown yet |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pin_rlm | total | 6-7 | 46.2 | 49.2 | -3.0 | -1.7 | -13.0 |  |  | keep collecting (13/30) |
| consensus_gap+rlm_ratio | total | 14-8 | 63.6 | 48.4 | 15.2 | +4.35 | 19.8 |  |  | keep collecting (22/30) |
| follow_move+pin_rlm | total | 52-32 | 61.9 | 52.2 | 9.7 | +15.92 | 19.0 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+rlm_ratio | total | 96-64 | 60.0 | 51.8 | 8.2 | +23.85 | 14.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 34-19 | 64.2 | 52.2 | 12.0 | +12.23 | 23.1 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 55-36 | 60.4 | 51.5 | 8.9 | +14.28 | 15.7 |  |  | PROMOTE: beats break-even and its own base rate |
| money_moving+pin_rlm | total | 60-38 | 61.2 | 52.2 | 9.0 | +17.05 | 17.4 |  |  | PROMOTE: beats break-even and its own base rate |
| money_moving+rlm_ratio | total | 94-64 | 59.5 | 51.8 | 7.7 | +22.05 | 14.0 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_rlm+pin_value | total | 19-11 | 63.3 | 51.4 | 11.9 | +6.24 | 20.8 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 52-32 | 61.9 | 52.2 | 9.7 | +15.92 | 19.0 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_rlm+sharp_gap | total | 61-38 | 61.6 | 52.2 | 9.4 | +17.96 | 18.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 22-13 | 62.9 | 50.9 | 12.0 | +6.89 | 19.7 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 96-64 | 60.0 | 51.8 | 8.2 | +23.85 | 14.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 53.5 | 46.5 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_rlm | close | 1-3k bets | 64-65 | 49.6 | 6.4 | 19.1 |  |
| pin_rlm | close | 3k+ bets | 22-26 | 45.8 | 5.0 | 5.8 |  |
| pin_rlm | close | <1k bets | 21-20 | 51.2 | 9.2 | 13.7 |  |
| pin_rlm | close | pin $1-2k | 47-42 | 52.8 | 8.1 | 21.5 |  |
| pin_rlm | close | pin $2k+ | 24-53 | 31.2 | -2.9 | -15.6 |  |
| pin_rlm | close | pin limit <$1k | 36-16 | 69.2 | 18.0 | 49.9 |  |
| follow_move | close | 1-3k bets | 421-355 | 54.3 | 2.6 | -3.3 |  |
| follow_move | close | 3k+ bets | 145-143 | 50.3 | -2.3 | -8.6 |  |
| follow_move | close | <1k bets | 109-101 | 51.9 | -1.4 | -11.9 |  |
| follow_move | close | pin $1-2k | 199-219 | 47.6 | -3.5 | -11.5 |  |
| follow_move | close | pin $2k+ | 160-139 | 53.5 | 1.5 | -6.0 |  |
| follow_move | close | pin limit <$1k | 93-80 | 53.8 | 3.2 | 2.6 |  |
| rlm_ratio | close | 1-3k bets | 98-113 | 46.4 | 1.4 | 0.4 |  |
| rlm_ratio | close | 3k+ bets | 35-30 | 53.8 | 10.3 | 18.7 |  |
| rlm_ratio | close | <1k bets | 24-22 | 52.2 | 8.4 | 5.7 |  |
| rlm_ratio | close | pin $1-2k | 56-50 | 52.8 | 5.9 | 9.8 |  |
| rlm_ratio | close | pin $2k+ | 27-43 | 38.6 | 1.7 | -11.7 |  |
| rlm_ratio | close | pin limit <$1k | 39-20 | 66.1 | 14.3 | 27.8 |  |
| money_level | close | 1-3k bets | 523-362 | 59.1 | 3.6 | -1.1 |  |
| money_level | close | 3k+ bets | 181-148 | 55.0 | -0.3 | -5.4 |  |
| money_level | close | <1k bets | 128-113 | 53.1 | -2.7 | -14.3 |  |
| money_level | close | pin $1-2k | 240-216 | 52.6 | -1.0 | -6.6 |  |
| money_level | close | pin $2k+ | 206-160 | 56.3 | -1.4 | -7.8 |  |
| money_level | close | pin limit <$1k | 98-98 | 50.0 | 0.5 | -4.8 |  |
| sharp_gap | close | 1-3k bets | 385-467 | 45.2 | -1.9 | -8.8 |  |
| sharp_gap | close | 3k+ bets | 158-165 | 48.9 | 2.2 | 5.7 |  |
| sharp_gap | close | <1k bets | 106-126 | 45.7 | -2.6 | -13.7 |  |
| sharp_gap | close | pin $1-2k | 216-228 | 48.6 | -0.1 | -2.6 |  |
| sharp_gap | close | pin $2k+ | 157-196 | 44.5 | -1.2 | -8.4 |  |
| sharp_gap | close | pin limit <$1k | 96-93 | 50.8 | 0.1 | 2.2 |  |
| money_moving | close | 1-3k bets | 385-468 | 45.1 | -2.2 | -9.7 |  |
| money_moving | close | 3k+ bets | 157-168 | 48.3 | 1.2 | 3.4 |  |
| money_moving | close | <1k bets | 104-126 | 45.2 | -2.6 | -12.5 |  |
| money_moving | close | pin $1-2k | 211-234 | 47.4 | -1.1 | -4.3 |  |
| money_moving | close | pin $2k+ | 159-193 | 45.2 | -0.4 | -7.2 |  |
| money_moving | close | pin limit <$1k | 93-98 | 48.7 | -1.8 | -1.8 |  |
| pin_value | close | 1-3k bets | 166-177 | 48.4 | 0.9 | -3.6 |  |
| pin_value | close | 3k+ bets | 57-65 | 46.7 | -0.6 | -6.8 |  |
| pin_value | close | <1k bets | 49-44 | 52.7 | 6.4 | 6.4 |  |
| pin_value | close | pin $1-2k | 127-144 | 46.9 | -0.9 | -8.2 |  |
| pin_value | close | pin $2k+ | 76-86 | 46.9 | 1.5 | -1.8 |  |
| pin_value | close | pin limit <$1k | 69-56 | 55.2 | 6.6 | 8.1 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.4 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.4 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 162-238 | 40.5 | -5.8 | -15.1 |  |
| consensus_gap | close | 3k+ bets | 66-83 | 44.3 | -2.5 | 2.9 |  |
| consensus_gap | close | <1k bets | 37-71 | 34.3 | -9.3 | -28.7 |  |
| consensus_gap | close | pin $1-2k | 85-106 | 44.5 | -3.2 | -4.0 |  |
| consensus_gap | close | pin $2k+ | 68-87 | 43.9 | -5.2 | -11.2 |  |
| consensus_gap | close | pin limit <$1k | 39-39 | 50.0 | 1.6 | -1.1 |  |
| consensus_gap+follow_move | close | 1-3k bets | 70-71 | 49.6 | -0.2 | -3.4 |  |
| consensus_gap+money_level | close | 1-3k bets | 108-80 | 57.4 | 0.5 | 1.0 |  |
| consensus_gap+money_moving | close | 1-3k bets | 72-131 | 35.5 | -7.5 | -13.4 |  |
| consensus_gap+pin_value | close | 1-3k bets | 65-89 | 42.2 | -2.5 | -10.4 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 72-134 | 35.0 | -7.5 | -14.5 |  |
| follow_move+money_level | close | 1-3k bets | 293-195 | 60.0 | 4.1 | -2.3 |  |
| follow_move+money_moving | close | 1-3k bets | 233-246 | 48.6 | -0.5 | -6.4 |  |
| follow_move+pin_value | close | 1-3k bets | 59-57 | 50.9 | 3.2 | -3.6 |  |
| follow_move+sharp_gap | close | 1-3k bets | 232-242 | 48.9 | 0.1 | -4.9 |  |
| money_level+money_moving | close | 1-3k bets | 281-249 | 53.0 | 1.0 | -2.0 |  |
| money_level+pin_value | close | 1-3k bets | 83-78 | 51.6 | 2.7 | -3.2 |  |
| money_level+sharp_gap | close | 1-3k bets | 278-247 | 53.0 | 1.2 | -1.3 |  |
| money_moving+pin_value | close | 1-3k bets | 76-91 | 45.5 | -1.1 | -5.9 |  |
| money_moving+sharp_gap | close | 1-3k bets | 372-452 | 45.1 | -2.0 | -8.8 |  |
| pin_value+sharp_gap | close | 1-3k bets | 78-93 | 45.6 | -1.0 | -6.0 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 13-21 | 38.2 | 1.2 | 28.5 |  |
| money_level+pin_rlm | close | 1-3k bets | 33-19 | 63.5 | 13.0 | 21.9 |  |
| pin_rlm+pin_value | close | 1-3k bets | 20-17 | 54.1 | 8.6 | 41.0 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 64-65 | 49.6 | 6.4 | 19.1 |  |
| money_moving+pin_rlm | close | 1-3k bets | 62-64 | 49.2 | 6.0 | 19.0 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 15-27 | 35.7 | -3.3 | 3.5 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 98-113 | 46.4 | 1.4 | 0.4 |  |
| money_level+rlm_ratio | close | 1-3k bets | 52-42 | 55.3 | 5.0 | 6.7 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 96-111 | 46.4 | 1.2 | 0.5 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 98-113 | 46.4 | 1.4 | 0.4 |  |
| follow_move+pin_rlm | close | 1-3k bets | 48-50 | 49.0 | 3.4 | -0.1 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 48-50 | 49.0 | 3.4 | -0.1 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 19-16 | 54.3 | 6.7 | 4.7 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 46.5 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 23-27 | 46.0 | -3.8 | -9.3 |  |
| consensus_gap+money_moving | close | 3k+ bets | 27-45 | 37.5 | -5.4 | 15.1 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-5 | 37.5 | -2.9 | 19.3 |  |
| consensus_gap+pin_value | close | 3k+ bets | 30-30 | 50.0 | 5.3 | 4.0 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | 0.5 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 28-45 | 38.4 | -4.4 | 18.8 |  |
| follow_move+money_moving | close | 3k+ bets | 76-84 | 47.5 | -1.6 | -6.1 |  |
| follow_move+pin_rlm | close | 3k+ bets | 21-18 | 53.8 | 10.9 | 25.4 |  |
| follow_move+pin_value | close | 3k+ bets | 23-24 | 48.9 | -0.1 | -8.2 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 35-30 | 53.8 | 10.3 | 18.7 |  |
| follow_move+sharp_gap | close | 3k+ bets | 78-83 | 48.4 | -0.1 | -3.3 |  |
| money_moving+pin_rlm | close | 3k+ bets | 21-26 | 44.7 | 4.1 | 3.9 |  |
| money_moving+pin_value | close | 3k+ bets | 27-36 | 42.9 | -2.9 | -8.3 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 33-28 | 54.1 | 10.7 | 20.0 |  |
| money_moving+sharp_gap | close | 3k+ bets | 150-158 | 48.7 | 1.9 | 5.2 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-7 | 41.7 | -5.2 | -21.0 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 21-18 | 53.8 | 10.9 | 25.4 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 22-26 | 45.8 | 5.0 | 5.8 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 6-5 | 54.5 | 4.4 | 2.8 |  |
| pin_value+sharp_gap | close | 3k+ bets | 27-34 | 44.3 | -1.5 | -5.2 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 35-30 | 53.8 | 10.3 | 18.7 |  |
| money_level+money_moving | close | 3k+ bets | 106-94 | 53.0 | 1.2 | -1.6 |  |
| money_level+sharp_gap | close | 3k+ bets | 105-91 | 53.6 | 2.1 | 0.4 |  |
| follow_move+money_level | close | 3k+ bets | 95-76 | 55.6 | -1.1 | -6.5 |  |
| money_level+rlm_ratio | close | 3k+ bets | 19-10 | 65.5 | 18.6 | 36.6 |  |
| consensus_gap+money_level | close | 3k+ bets | 36-35 | 50.7 | -5.3 | -13.3 |  |
| money_level+pin_value | close | 3k+ bets | 28-35 | 44.4 | -4.0 | -17.9 |  |
| money_level+pin_rlm | close | 3k+ bets | 10-7 | 58.8 | 14.9 | 33.3 |  |
| money_level+money_moving | close | <1k bets | 70-75 | 48.3 | -4.4 | -16.7 |  |
| money_level+sharp_gap | close | <1k bets | 73-75 | 49.3 | -3.8 | -16.1 |  |
| money_moving+sharp_gap | close | <1k bets | 102-124 | 45.1 | -2.9 | -13.7 |  |
| consensus_gap+money_level | close | <1k bets | 16-26 | 38.1 | -17.6 | -41.8 |  |
| consensus_gap+money_moving | close | <1k bets | 15-36 | 29.4 | -11.8 | -32.8 |  |
| consensus_gap+pin_value | close | <1k bets | 12-14 | 46.2 | 5.6 | 9.9 |  |
| consensus_gap+sharp_gap | close | <1k bets | 15-37 | 28.8 | -12.0 | -34.1 |  |
| money_level+pin_value | close | <1k bets | 17-17 | 50.0 | 0.5 | -6.7 |  |
| money_moving+pin_value | close | <1k bets | 15-16 | 48.4 | 3.0 | 10.3 |  |
| pin_value+sharp_gap | close | <1k bets | 15-15 | 50.0 | 4.0 | 13.9 |  |
| follow_move+money_moving | close | <1k bets | 49-58 | 45.8 | -4.3 | -14.4 |  |
| follow_move+sharp_gap | close | <1k bets | 51-58 | 46.8 | -4.2 | -17.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 24-22 | 52.2 | 8.4 | 5.7 |  |
| money_moving+rlm_ratio | close | <1k bets | 24-22 | 52.2 | 8.4 | 5.7 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 24-22 | 52.2 | 8.4 | 5.7 |  |
| follow_move+money_level | close | <1k bets | 66-58 | 53.2 | -5.1 | -19.2 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -0.6 | 12.2 |  |
| money_moving+pin_rlm | close | <1k bets | 21-20 | 51.2 | 9.2 | 13.7 |  |
| pin_rlm+sharp_gap | close | <1k bets | 21-20 | 51.2 | 9.2 | 13.7 |  |
| consensus_gap+follow_move | close | <1k bets | 8-18 | 30.8 | -20.2 | -52.8 |  |
| follow_move+pin_rlm | close | <1k bets | 16-11 | 59.3 | 15.0 | 17.3 |  |
| follow_move+pin_value | close | <1k bets | 16-12 | 57.1 | 8.7 | 8.5 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 20.2 | 60.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 16-11 | 59.3 | 15.0 | 17.3 |  |
| pin_value+rlm_ratio | close | <1k bets | 3-1 | 75.0 | 23.0 | 43.9 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 1-6 | 14.3 | -18.4 | -71.1 |  |
| money_level+rlm_ratio | close | <1k bets | 12-12 | 50.0 | 3.6 | -1.3 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 16.2 | 19.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 31-41 | 43.1 | -7.3 | -14.8 |  |
| consensus_gap+money_moving | close | pin $1-2k | 44-58 | 43.1 | -3.8 | -4.5 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 12-16 | 42.9 | 2.5 | 32.5 |  |
| consensus_gap+pin_value | close | pin $1-2k | 50-64 | 43.9 | -0.7 | -10.3 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 12-12 | 50.0 | 5.1 | 11.5 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 44-55 | 44.4 | -1.7 | -1.6 |  |
| follow_move+money_moving | close | pin $1-2k | 118-145 | 44.9 | -4.7 | -11.8 |  |
| follow_move+pin_rlm | close | pin $1-2k | 38-32 | 54.3 | 7.2 | 12.6 |  |
| follow_move+pin_value | close | pin $1-2k | 44-49 | 47.3 | -1.6 | -10.9 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 56-50 | 52.8 | 5.9 | 9.8 |  |
| follow_move+sharp_gap | close | pin $1-2k | 122-142 | 46.2 | -3.6 | -10.3 |  |
| money_moving+pin_rlm | close | pin $1-2k | 45-41 | 52.3 | 7.6 | 21.2 |  |
| money_moving+pin_value | close | pin $1-2k | 51-70 | 42.1 | -4.9 | -16.3 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 55-48 | 53.4 | 6.4 | 11.0 |  |
| money_moving+sharp_gap | close | pin $1-2k | 207-224 | 48.0 | -0.5 | -3.5 |  |
| pin_rlm+pin_value | close | pin $1-2k | 11-16 | 40.7 | -7.4 | -12.3 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 38-32 | 54.3 | 7.2 | 12.6 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 47-42 | 52.8 | 8.1 | 21.5 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 13-13 | 50.0 | 0.1 | -6.0 |  |
| pin_value+sharp_gap | close | pin $1-2k | 51-68 | 42.9 | -4.2 | -14.9 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 56-50 | 52.8 | 5.9 | 9.8 |  |
| follow_move+money_level | close | pin $1-2k | 139-136 | 50.5 | -3.4 | -11.7 |  |
| money_level+rlm_ratio | close | pin $1-2k | 36-24 | 60.0 | 11.5 | 17.5 |  |
| money_level+sharp_gap | close | pin $1-2k | 159-153 | 51.0 | -0.5 | -5.1 |  |
| money_level+money_moving | close | pin $1-2k | 156-156 | 50.0 | -1.3 | -6.6 |  |
| consensus_gap+money_level | close | pin $1-2k | 48-49 | 49.5 | -5.9 | -11.9 |  |
| money_level+pin_value | close | pin $1-2k | 55-61 | 47.4 | -1.8 | -11.2 |  |
| money_level+pin_rlm | close | pin $1-2k | 25-16 | 61.0 | 13.4 | 20.4 |  |
| follow_move+money_level | close | pin $2k+ | 104-68 | 60.5 | 0.9 | -4.0 |  |
| follow_move+money_moving | close | pin $2k+ | 77-84 | 47.8 | 0.9 | -7.4 |  |
| follow_move+sharp_gap | close | pin $2k+ | 78-86 | 47.6 | 0.6 | -7.8 |  |
| money_level+money_moving | close | pin $2k+ | 104-98 | 51.5 | -1.0 | -5.6 |  |
| money_level+sharp_gap | close | pin $2k+ | 104-100 | 51.0 | -1.6 | -6.2 |  |
| money_moving+sharp_gap | close | pin $2k+ | 154-191 | 44.6 | -0.9 | -7.6 |  |
| consensus_gap+money_moving | close | pin $2k+ | 23-50 | 31.5 | -10.2 | -16.2 |  |
| consensus_gap+pin_value | close | pin $2k+ | 30-39 | 43.5 | 2.4 | 3.7 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 24-53 | 31.2 | -11.6 | -18.7 |  |
| money_moving+pin_value | close | pin $2k+ | 39-49 | 44.3 | 0.5 | 2.5 |  |
| pin_value+sharp_gap | close | pin $2k+ | 39-49 | 44.3 | 0.5 | 2.5 |  |
| consensus_gap+follow_move | close | pin $2k+ | 21-23 | 47.7 | -4.0 | -22.1 |  |
| follow_move+pin_value | close | pin $2k+ | 26-25 | 51.0 | 4.9 | -2.9 |  |
| follow_move+pin_rlm | close | pin $2k+ | 19-35 | 35.2 | -1.1 | -15.2 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 27-43 | 38.6 | 1.7 | -11.7 |  |
| money_level+pin_rlm | close | pin $2k+ | 9-8 | 52.9 | 11.0 | 17.5 |  |
| money_level+pin_value | close | pin $2k+ | 38-39 | 49.4 | 0.1 | -9.0 |  |
| money_level+rlm_ratio | close | pin $2k+ | 10-9 | 52.6 | 6.2 | 14.2 |  |
| money_moving+pin_rlm | close | pin $2k+ | 24-53 | 31.2 | -2.9 | -15.6 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 27-42 | 39.1 | 2.1 | -10.5 |  |
| pin_rlm+pin_value | close | pin $2k+ | 5-9 | 35.7 | 0.3 | 40.5 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 19-35 | 35.2 | -1.1 | -15.2 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 24-53 | 31.2 | -2.9 | -15.6 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 3-5 | 37.5 | -1.0 | -22.1 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 27-43 | 38.6 | 1.7 | -11.7 |  |
| consensus_gap+money_level | close | pin $2k+ | 47-36 | 56.6 | -5.5 | -12.1 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-15 | 21.1 | -7.6 | -9.0 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-10 | 0.0 | -28.5 | -100.0 |  |
| money_level+money_moving | close | pin limit <$1k | 56-60 | 48.3 | -1.6 | -7.2 |  |
| money_level+sharp_gap | close | pin limit <$1k | 58-59 | 49.6 | -0.6 | -4.8 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 89-88 | 50.3 | -0.4 | 1.6 |  |
| consensus_gap+money_level | close | pin limit <$1k | 21-22 | 48.8 | 0.4 | -9.8 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 27-30 | 47.4 | -0.2 | -3.2 |  |
| follow_move+money_moving | close | pin limit <$1k | 58-56 | 50.9 | 0.2 | -2.1 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 60-54 | 52.6 | 1.8 | 1.2 |  |
| money_level+pin_value | close | pin limit <$1k | 35-30 | 53.8 | 6.0 | 1.7 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 14-10 | 58.3 | 9.5 | 6.1 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 17-15 | 53.1 | 5.8 | 13.9 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 18-16 | 52.9 | 5.1 | 12.7 |  |
| follow_move+money_level | close | pin limit <$1k | 49-46 | 51.6 | 1.5 | -1.8 |  |
| follow_move+pin_value | close | pin limit <$1k | 28-19 | 59.6 | 10.8 | 12.8 |  |
| money_moving+pin_value | close | pin limit <$1k | 28-24 | 53.8 | 5.3 | 10.7 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 30-25 | 54.5 | 5.6 | 11.5 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 3-2 | 60.0 | 17.6 | 101.6 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 35-16 | 68.6 | 17.5 | 49.1 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 14-2 | 87.5 | 38.4 | 94.7 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 36-16 | 69.2 | 18.0 | 49.9 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 28-12 | 70.0 | 17.8 | 34.7 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 39-20 | 66.1 | 14.3 | 27.8 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 37-20 | 64.9 | 13.2 | 25.6 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 28-12 | 70.0 | 17.8 | 34.7 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 39-20 | 66.1 | 14.3 | 27.8 |  |
| money_level+pin_rlm | close | pin limit <$1k | 18-8 | 69.2 | 16.8 | 32.9 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 20-11 | 64.5 | 13.0 | 25.7 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 12-4 | 75.0 | 23.7 | 43.9 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 3-3 | 50.0 | 2.3 | -5.2 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 46.5 | 87.7 |  |
| pin_rlm | early | <1k bets | 1-1 | 50.0 | 24.2 | -3.7 | -2.15 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.4 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -49.6 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 274-249 | 52.4 | 0.1 | -9.5 | 0.27 |
| follow_move | early | pin $1-2k | 19-15 | 55.9 | 3.7 | 4.8 | -0.25 |
| follow_move | early | pin limit <$1k | 41-35 | 53.9 | 4.4 | 1.2 | -0.22 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.5 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.6 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 11-11 | 50.0 | 15.7 | 16.4 | 0.21 |
| rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.5 | 55.6 | -1.52 |
| rlm_ratio | early | pin limit <$1k | 6-1 | 85.7 | 41.1 | 74.9 | 0.19 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 0.0 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 41.6 | 59.7 | 0.33 |
| money_level | early | <1k bets | 94-56 | 62.7 | 3.1 | -3.9 | 0.21 |
| money_level | early | pin $1-2k | 15-8 | 65.2 | 0.8 | -2.7 | -0.03 |
| money_level | early | pin limit <$1k | 22-24 | 47.8 | -6.1 | -12.1 | 0.31 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.0 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 6.6 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 79-59 | 57.2 | 7.7 | 9.6 | 0.42 |
| sharp_gap | early | pin $1-2k | 12-9 | 57.1 | 4.5 | 13.4 | -0.59 |
| sharp_gap | early | pin limit <$1k | 27-16 | 62.8 | 14.0 | 30.8 | 0.2 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.1 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.6 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 48-40 | 54.5 | 2.8 | -3.9 | 0.12 |
| money_moving | early | pin $1-2k | 6-6 | 50.0 | -11.7 | -26.9 | 0.35 |
| money_moving | early | pin limit <$1k | 20-9 | 69.0 | 19.7 | 47.8 | 0.36 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.4 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.6 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 30-33 | 47.6 | 0.0 | -9.7 | 0.19 |
| pin_value | early | pin $1-2k | 11-14 | 44.0 | -0.3 | -16.7 | 0.17 |
| pin_value | early | pin limit <$1k | 32-28 | 53.3 | 4.0 | 0.8 | 0.13 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -46.5 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -27.9 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -10.9 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 13.4 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 133-180 | 42.5 | -4.4 | -17.2 | 0.29 |
| consensus_gap | early | pin $1-2k | 10-17 | 37.0 | -8.1 | -27.6 | 0.49 |
| consensus_gap | early | pin limit <$1k | 17-33 | 34.0 | -16.1 | -29.1 | 0.31 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 16.0 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 2.8 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 3.0 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.2 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 18.9 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 15.5 | 26.0 | -0.25 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -0.3 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 4.4 | -6.9 | 0.3 |
| follow_move+pin_value | early | 1-3k bets | 7-6 | 53.8 | 6.4 | 0.8 | -0.31 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.9 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.2 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 2.2 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.2 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.5 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 27.0 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.5 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.0 | 25.3 | 0.18 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 18.1 | 56.1 | 0.15 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 19.2 | 18.8 | -0.24 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -25.8 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.6 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.6 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.6 | 83.3 | 1.0 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.6 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.6 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.6 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.6 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.6 | 83.3 | 1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.6 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 36.1 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 46.5 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 19-27 | 41.3 | -10.3 | -26.0 | 0.92 |
| consensus_gap+money_level | early | <1k bets | 18-15 | 54.5 | -10.9 | -19.3 | 0.26 |
| consensus_gap+sharp_gap | early | <1k bets | 15-28 | 34.9 | -12.7 | -17.7 | 0.7 |
| follow_move+money_level | early | <1k bets | 52-25 | 67.5 | 7.6 | -2.2 | 0.43 |
| follow_move+sharp_gap | early | <1k bets | 40-19 | 67.8 | 17.3 | 18.8 | 0.64 |
| money_level+sharp_gap | early | <1k bets | 55-28 | 66.3 | 9.4 | 7.4 | 0.55 |
| follow_move+money_moving | early | <1k bets | 21-12 | 63.6 | 9.9 | 10.7 | 0.64 |
| money_level+money_moving | early | <1k bets | 32-22 | 59.3 | 1.4 | -6.0 | -0.03 |
| money_moving+sharp_gap | early | <1k bets | 31-22 | 58.5 | 7.8 | 5.0 | 0.37 |
| consensus_gap+money_moving | early | <1k bets | 8-16 | 33.3 | -13.2 | -46.4 | 0.14 |
| follow_move+pin_value | early | <1k bets | 11-11 | 50.0 | 2.1 | -5.9 | 0.05 |
| follow_move+rlm_ratio | early | <1k bets | 11-11 | 50.0 | 15.7 | 16.4 | 0.21 |
| rlm_ratio+sharp_gap | early | <1k bets | 11-11 | 50.0 | 15.7 | 16.4 | 0.21 |
| consensus_gap+pin_value | early | <1k bets | 11-22 | 33.3 | -12.3 | -37.3 | 0.45 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | <1k bets | 1-3 | 25.0 | -14.6 | -52.3 | -0.07 |
| follow_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 24.2 | -3.7 | -2.15 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 24.2 | -3.7 | -2.15 |
| pin_rlm+sharp_gap | early | <1k bets | 1-1 | 50.0 | 24.2 | -3.7 | -2.15 |
| pin_value+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 10.4 | -4.5 | -1.9 |
| pin_value+sharp_gap | early | <1k bets | 4-3 | 57.1 | 11.5 | 9.1 | 0.03 |
| money_level+pin_value | early | <1k bets | 3-3 | 50.0 | 1.2 | -4.5 | 1.33 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -53.1 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -53.5 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 0-2 | 0.0 | -49.6 | -100.0 | 2.5 |
| money_level+rlm_ratio | early | <1k bets | 5-5 | 50.0 | 13.1 | 0.9 | 1.52 |
| money_moving+rlm_ratio | early | <1k bets | 3-3 | 50.0 | 6.8 | 26.0 | 0.1 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| consensus_gap+money_level | early | pin $1-2k | 4-4 | 50.0 | -14.1 | -22.9 | 0.44 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -31.9 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 4-9 | 30.8 | -8.7 | -42.5 | 0.4 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.5 | 55.6 | -1.52 |
| follow_move+sharp_gap | early | pin $1-2k | 7-4 | 63.6 | 11.4 | 42.5 | -0.87 |
| money_level+money_moving | early | pin $1-2k | 6-5 | 54.5 | -10.4 | -20.3 | 0.02 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.4 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-3 | 40.0 | 3.5 | 55.6 | -1.52 |
| money_level+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 6.2 | 8.3 | -0.45 |
| money_moving+sharp_gap | early | pin $1-2k | 3-5 | 37.5 | -21.3 | -45.3 | -0.06 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.6 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 3-6 | 33.3 | -14.0 | -42.7 | 0.43 |
| follow_move+pin_value | early | pin $1-2k | 4-5 | 44.4 | 0.1 | -16.8 | -0.2 |
| follow_move+money_level | early | pin $1-2k | 7-4 | 63.6 | 1.1 | -0.7 | 0.07 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 47.4 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 2-1 | 66.7 | 1.4 | 4.7 | -0.53 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -25.0 | -62.8 | -0.72 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| money_level+money_moving | early | pin limit <$1k | 11-7 | 61.1 | 8.0 | 12.1 | 0.53 |
| money_level+sharp_gap | early | pin limit <$1k | 18-14 | 56.2 | 4.9 | 2.3 | 0.25 |
| money_moving+sharp_gap | early | pin limit <$1k | 16-5 | 76.2 | 28.0 | 68.0 | 0.39 |
| money_level+pin_value | early | pin limit <$1k | 8-5 | 61.5 | 10.2 | 16.6 | 0.46 |
| money_moving+pin_value | early | pin limit <$1k | 6-4 | 60.0 | 9.9 | 13.0 | 0.3 |
| pin_value+sharp_gap | early | pin limit <$1k | 11-5 | 68.8 | 18.3 | 30.3 | 0.06 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-9 | 40.0 | -11.1 | -25.7 | 0.53 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -27.1 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 13-18 | 41.9 | -6.3 | -21.4 | 0.44 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.4 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 10-11 | 47.6 | -7.0 | -12.3 | -0.09 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 5.0 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 12-7 | 63.2 | 14.3 | 20.4 | -0.13 |
| follow_move+rlm_ratio | early | pin limit <$1k | 6-1 | 85.7 | 41.1 | 74.9 | 0.19 |
| money_level+rlm_ratio | early | pin limit <$1k | 5-0 | 100.0 | 52.1 | 92.1 | 0.3 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.5 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 6-1 | 85.7 | 41.1 | 74.9 | 0.19 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 23.3 | 72.3 | 0.54 |
| follow_move+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 20.4 | 33.3 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.5 | 28.7 | -1.0 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -53.5 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -53.5 | -100.0 | 1.0 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| pin_rlm | close | 1-3k bets | 59-64 | 48.0 | 4.3 | 15.1 |  |
| pin_rlm | close | 3k+ bets | 20-22 | 47.6 | 6.4 | 6.1 |  |
| pin_rlm | close | <1k bets | 21-20 | 51.2 | 8.8 | 13.7 |  |
| pin_rlm | close | pin $1-2k | 44-41 | 51.8 | 7.1 | 20.4 |  |
| pin_rlm | close | pin $2k+ | 21-49 | 30.0 | -4.4 | -22.4 |  |
| pin_rlm | close | pin limit <$1k | 35-16 | 68.6 | 16.8 | 49.1 |  |
| follow_move | close | 1-3k bets | 408-344 | 54.3 | 2.7 | -3.2 |  |
| follow_move | close | 3k+ bets | 135-131 | 50.8 | -1.6 | -7.7 |  |
| follow_move | close | <1k bets | 109-101 | 51.9 | -1.4 | -11.9 |  |
| follow_move | close | pin $1-2k | 193-212 | 47.7 | -3.3 | -11.3 |  |
| follow_move | close | pin $2k+ | 150-132 | 53.2 | 1.4 | -7.8 |  |
| follow_move | close | pin limit <$1k | 92-80 | 53.5 | 2.8 | 2.1 |  |
| rlm_ratio | close | 1-3k bets | 94-111 | 45.9 | 0.4 | -1.6 |  |
| rlm_ratio | close | 3k+ bets | 33-28 | 54.1 | 10.2 | 16.3 |  |
| rlm_ratio | close | <1k bets | 24-22 | 52.2 | 8.0 | 5.7 |  |
| rlm_ratio | close | pin $1-2k | 54-49 | 52.4 | 5.4 | 9.3 |  |
| rlm_ratio | close | pin $2k+ | 25-42 | 37.3 | -0.1 | -20.9 |  |
| rlm_ratio | close | pin limit <$1k | 38-20 | 65.5 | 13.1 | 26.7 |  |
| money_level | close | 1-3k bets | 506-348 | 59.3 | 3.8 | -0.6 |  |
| money_level | close | 3k+ bets | 162-143 | 53.1 | -2.2 | -9.3 |  |
| money_level | close | <1k bets | 128-113 | 53.1 | -2.6 | -14.3 |  |
| money_level | close | pin $1-2k | 233-208 | 52.8 | -0.8 | -6.3 |  |
| money_level | close | pin $2k+ | 193-154 | 55.6 | -2.0 | -9.6 |  |
| money_level | close | pin limit <$1k | 96-97 | 49.7 | 0.3 | -5.3 |  |
| sharp_gap | close | 1-3k bets | 369-453 | 44.9 | -2.4 | -9.4 |  |
| sharp_gap | close | 3k+ bets | 146-154 | 48.7 | 1.9 | 5.8 |  |
| sharp_gap | close | <1k bets | 106-126 | 45.7 | -2.8 | -13.7 |  |
| sharp_gap | close | pin $1-2k | 209-221 | 48.6 | -0.2 | -2.5 |  |
| sharp_gap | close | pin $2k+ | 146-189 | 43.6 | -2.1 | -10.8 |  |
| sharp_gap | close | pin limit <$1k | 94-92 | 50.5 | -0.5 | 1.8 |  |
| money_moving | close | 1-3k bets | 368-455 | 44.7 | -2.8 | -10.4 |  |
| money_moving | close | 3k+ bets | 145-157 | 48.0 | 0.9 | 3.2 |  |
| money_moving | close | <1k bets | 104-126 | 45.2 | -2.7 | -12.5 |  |
| money_moving | close | pin $1-2k | 204-227 | 47.3 | -1.2 | -4.2 |  |
| money_moving | close | pin $2k+ | 148-186 | 44.3 | -1.3 | -9.5 |  |
| money_moving | close | pin limit <$1k | 91-97 | 48.4 | -2.3 | -2.3 |  |
| pin_value | close | 1-3k bets | 160-170 | 48.5 | 1.1 | -3.3 |  |
| pin_value | close | 3k+ bets | 55-61 | 47.4 | 0.2 | -5.2 |  |
| pin_value | close | <1k bets | 49-44 | 52.7 | 6.5 | 6.4 |  |
| pin_value | close | pin $1-2k | 124-139 | 47.1 | -0.6 | -7.5 |  |
| pin_value | close | pin $2k+ | 73-81 | 47.4 | 2.2 | -0.3 |  |
| pin_value | close | pin limit <$1k | 67-55 | 54.9 | 6.6 | 7.7 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.2 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.2 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 158-230 | 40.7 | -5.6 | -15.7 |  |
| consensus_gap | close | 3k+ bets | 62-78 | 44.3 | -2.3 | 4.5 |  |
| consensus_gap | close | <1k bets | 37-71 | 34.3 | -9.3 | -28.7 |  |
| consensus_gap | close | pin $1-2k | 81-104 | 43.8 | -3.8 | -5.0 |  |
| consensus_gap | close | pin $2k+ | 65-82 | 44.2 | -5.2 | -13.2 |  |
| consensus_gap | close | pin limit <$1k | 39-39 | 50.0 | 2.1 | -1.1 |  |
| consensus_gap+follow_move | close | 1-3k bets | 70-70 | 50.0 | 0.2 | -2.7 |  |
| consensus_gap+money_level | close | 1-3k bets | 107-78 | 57.8 | 1.2 | 1.6 |  |
| consensus_gap+money_moving | close | 1-3k bets | 69-126 | 35.4 | -7.7 | -12.8 |  |
| consensus_gap+pin_value | close | 1-3k bets | 64-86 | 42.7 | -1.9 | -9.2 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 69-129 | 34.8 | -7.7 | -13.9 |  |
| follow_move+money_level | close | 1-3k bets | 283-188 | 60.1 | 4.3 | -1.9 |  |
| follow_move+money_moving | close | 1-3k bets | 226-243 | 48.2 | -1.0 | -7.4 |  |
| follow_move+pin_value | close | 1-3k bets | 58-56 | 50.9 | 3.4 | -3.5 |  |
| follow_move+sharp_gap | close | 1-3k bets | 226-239 | 48.6 | -0.4 | -5.9 |  |
| money_level+money_moving | close | 1-3k bets | 271-243 | 52.7 | 0.8 | -2.3 |  |
| money_level+pin_value | close | 1-3k bets | 80-75 | 51.6 | 2.9 | -3.1 |  |
| money_level+sharp_gap | close | 1-3k bets | 269-241 | 52.7 | 1.0 | -1.6 |  |
| money_moving+pin_value | close | 1-3k bets | 72-88 | 45.0 | -1.6 | -6.5 |  |
| money_moving+sharp_gap | close | 1-3k bets | 356-439 | 44.8 | -2.5 | -9.5 |  |
| pin_value+sharp_gap | close | 1-3k bets | 74-90 | 45.1 | -1.6 | -6.5 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 12-20 | 37.5 | 0.7 | 30.6 |  |
| money_level+pin_rlm | close | 1-3k bets | 30-19 | 61.2 | 10.2 | 17.7 |  |
| pin_rlm+pin_value | close | 1-3k bets | 18-17 | 51.4 | 6.0 | 38.3 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 59-64 | 48.0 | 4.3 | 15.1 |  |
| money_moving+pin_rlm | close | 1-3k bets | 57-63 | 47.5 | 3.9 | 14.8 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 15-26 | 36.6 | -2.6 | 6.0 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 94-111 | 45.9 | 0.4 | -1.6 |  |
| money_level+rlm_ratio | close | 1-3k bets | 49-41 | 54.4 | 3.8 | 5.1 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 92-109 | 45.8 | 0.2 | -1.6 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 94-111 | 45.9 | 0.4 | -1.6 |  |
| follow_move+pin_rlm | close | 1-3k bets | 46-50 | 47.9 | 1.8 | -4.7 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 46-50 | 47.9 | 1.8 | -4.7 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 19-16 | 54.3 | 6.5 | 4.7 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 45.7 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 23-25 | 47.9 | -1.1 | -5.5 |  |
| consensus_gap+money_moving | close | 3k+ bets | 26-44 | 37.1 | -5.8 | 15.8 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-5 | 37.5 | -2.7 | 19.3 |  |
| consensus_gap+pin_value | close | 3k+ bets | 28-30 | 48.3 | 3.9 | 1.1 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | 0.7 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 27-44 | 38.0 | -4.8 | 19.6 |  |
| follow_move+money_moving | close | 3k+ bets | 71-78 | 47.7 | -1.2 | -6.3 |  |
| follow_move+pin_rlm | close | 3k+ bets | 19-16 | 54.3 | 10.8 | 22.0 |  |
| follow_move+pin_value | close | 3k+ bets | 23-23 | 50.0 | 1.1 | -6.2 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 33-28 | 54.1 | 10.2 | 16.3 |  |
| follow_move+sharp_gap | close | 3k+ bets | 73-77 | 48.7 | 0.4 | -3.3 |  |
| money_moving+pin_rlm | close | 3k+ bets | 19-22 | 46.3 | 5.4 | 3.9 |  |
| money_moving+pin_value | close | 3k+ bets | 26-34 | 43.3 | -2.0 | -6.8 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 31-26 | 54.4 | 10.6 | 17.5 |  |
| money_moving+sharp_gap | close | 3k+ bets | 138-147 | 48.4 | 1.6 | 5.2 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-6 | 45.5 | -0.9 | -13.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 19-16 | 54.3 | 10.8 | 22.0 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 20-22 | 47.6 | 6.4 | 6.1 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 6-5 | 54.5 | 4.4 | 2.8 |  |
| pin_value+sharp_gap | close | 3k+ bets | 26-32 | 44.8 | -0.6 | -3.5 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 33-28 | 54.1 | 10.2 | 16.3 |  |
| money_level+money_moving | close | 3k+ bets | 94-90 | 51.1 | -0.7 | -6.3 |  |
| money_level+sharp_gap | close | 3k+ bets | 93-87 | 51.7 | 0.2 | -4.2 |  |
| follow_move+money_level | close | 3k+ bets | 86-72 | 54.4 | -1.9 | -8.8 |  |
| money_level+rlm_ratio | close | 3k+ bets | 17-9 | 65.4 | 18.1 | 28.5 |  |
| consensus_gap+money_level | close | 3k+ bets | 33-35 | 48.5 | -7.2 | -17.0 |  |
| money_level+pin_value | close | 3k+ bets | 26-33 | 44.1 | -4.2 | -18.7 |  |
| money_level+pin_rlm | close | 3k+ bets | 8-6 | 57.1 | 13.1 | 17.5 |  |
| money_level+money_moving | close | <1k bets | 70-75 | 48.3 | -4.4 | -16.7 |  |
| money_level+sharp_gap | close | <1k bets | 73-75 | 49.3 | -3.9 | -16.1 |  |
| money_moving+sharp_gap | close | <1k bets | 102-124 | 45.1 | -3.0 | -13.7 |  |
| consensus_gap+money_level | close | <1k bets | 16-26 | 38.1 | -17.5 | -41.8 |  |
| consensus_gap+money_moving | close | <1k bets | 15-36 | 29.4 | -11.8 | -32.8 |  |
| consensus_gap+pin_value | close | <1k bets | 12-14 | 46.2 | 5.7 | 9.9 |  |
| consensus_gap+sharp_gap | close | <1k bets | 15-37 | 28.8 | -12.1 | -34.1 |  |
| money_level+pin_value | close | <1k bets | 17-17 | 50.0 | 0.7 | -6.7 |  |
| money_moving+pin_value | close | <1k bets | 15-16 | 48.4 | 2.9 | 10.3 |  |
| pin_value+sharp_gap | close | <1k bets | 15-15 | 50.0 | 3.9 | 13.9 |  |
| follow_move+money_moving | close | <1k bets | 49-58 | 45.8 | -4.4 | -14.4 |  |
| follow_move+sharp_gap | close | <1k bets | 51-58 | 46.8 | -4.3 | -17.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 24-22 | 52.2 | 8.0 | 5.7 |  |
| money_moving+rlm_ratio | close | <1k bets | 24-22 | 52.2 | 8.0 | 5.7 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 24-22 | 52.2 | 8.0 | 5.7 |  |
| follow_move+money_level | close | <1k bets | 66-58 | 53.2 | -5.0 | -19.2 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -0.7 | 12.2 |  |
| money_moving+pin_rlm | close | <1k bets | 21-20 | 51.2 | 8.8 | 13.7 |  |
| pin_rlm+sharp_gap | close | <1k bets | 21-20 | 51.2 | 8.8 | 13.7 |  |
| consensus_gap+follow_move | close | <1k bets | 8-18 | 30.8 | -20.2 | -52.8 |  |
| follow_move+pin_rlm | close | <1k bets | 16-11 | 59.3 | 14.6 | 17.3 |  |
| follow_move+pin_value | close | <1k bets | 16-12 | 57.1 | 8.8 | 8.5 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 19.8 | 60.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 16-11 | 59.3 | 14.6 | 17.3 |  |
| pin_value+rlm_ratio | close | <1k bets | 3-1 | 75.0 | 22.5 | 43.9 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 1-6 | 14.3 | -18.5 | -71.1 |  |
| money_level+rlm_ratio | close | <1k bets | 12-12 | 50.0 | 3.2 | -1.3 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 15.8 | 19.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 31-41 | 43.1 | -7.0 | -14.8 |  |
| consensus_gap+money_moving | close | pin $1-2k | 42-57 | 42.4 | -4.5 | -5.4 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 11-16 | 40.7 | 0.8 | 30.3 |  |
| consensus_gap+pin_value | close | pin $1-2k | 48-62 | 43.6 | -0.7 | -10.5 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 12-12 | 50.0 | 5.3 | 11.5 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 42-54 | 43.8 | -2.5 | -2.4 |  |
| follow_move+money_moving | close | pin $1-2k | 115-142 | 44.7 | -4.7 | -12.0 |  |
| follow_move+pin_rlm | close | pin $1-2k | 36-31 | 53.7 | 6.5 | 11.9 |  |
| follow_move+pin_value | close | pin $1-2k | 44-49 | 47.3 | -1.5 | -10.9 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 54-49 | 52.4 | 5.4 | 9.3 |  |
| follow_move+sharp_gap | close | pin $1-2k | 119-139 | 46.1 | -3.6 | -10.4 |  |
| money_moving+pin_rlm | close | pin $1-2k | 42-40 | 51.2 | 6.6 | 20.2 |  |
| money_moving+pin_value | close | pin $1-2k | 49-68 | 41.9 | -5.3 | -16.7 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 53-47 | 53.0 | 5.9 | 10.5 |  |
| money_moving+sharp_gap | close | pin $1-2k | 200-217 | 48.0 | -0.6 | -3.4 |  |
| pin_rlm+pin_value | close | pin $1-2k | 10-16 | 38.5 | -9.7 | -16.2 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 36-31 | 53.7 | 6.5 | 11.9 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 44-41 | 51.8 | 7.1 | 20.4 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 13-13 | 50.0 | 0.0 | -6.0 |  |
| pin_value+sharp_gap | close | pin $1-2k | 49-66 | 42.6 | -4.6 | -15.3 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 54-49 | 52.4 | 5.4 | 9.3 |  |
| follow_move+money_level | close | pin $1-2k | 135-131 | 50.8 | -3.1 | -11.3 |  |
| money_level+rlm_ratio | close | pin $1-2k | 34-23 | 59.6 | 11.2 | 17.0 |  |
| money_level+sharp_gap | close | pin $1-2k | 155-149 | 51.0 | -0.5 | -5.1 |  |
| money_level+money_moving | close | pin $1-2k | 152-152 | 50.0 | -1.3 | -6.6 |  |
| consensus_gap+money_level | close | pin $1-2k | 46-49 | 48.4 | -6.8 | -13.9 |  |
| money_level+pin_value | close | pin $1-2k | 54-59 | 47.8 | -1.3 | -10.5 |  |
| money_level+pin_rlm | close | pin $1-2k | 23-15 | 60.5 | 12.9 | 19.8 |  |
| follow_move+money_level | close | pin $2k+ | 96-64 | 60.0 | 0.5 | -6.0 |  |
| follow_move+money_moving | close | pin $2k+ | 72-82 | 46.8 | -0.1 | -11.8 |  |
| follow_move+sharp_gap | close | pin $2k+ | 73-84 | 46.5 | -0.4 | -12.1 |  |
| money_level+money_moving | close | pin $2k+ | 96-96 | 50.0 | -2.5 | -9.2 |  |
| money_level+sharp_gap | close | pin $2k+ | 96-98 | 49.5 | -3.1 | -9.8 |  |
| money_moving+sharp_gap | close | pin $2k+ | 143-184 | 43.7 | -1.8 | -10.0 |  |
| consensus_gap+money_moving | close | pin $2k+ | 22-48 | 31.4 | -10.4 | -15.2 |  |
| consensus_gap+pin_value | close | pin $2k+ | 29-38 | 43.3 | 2.4 | 4.0 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 23-51 | 31.1 | -11.8 | -17.9 |  |
| money_moving+pin_value | close | pin $2k+ | 37-46 | 44.6 | 1.1 | 4.2 |  |
| pin_value+sharp_gap | close | pin $2k+ | 37-46 | 44.6 | 1.1 | 4.2 |  |
| consensus_gap+follow_move | close | pin $2k+ | 21-23 | 47.7 | -3.9 | -22.1 |  |
| follow_move+pin_value | close | pin $2k+ | 25-23 | 52.1 | 6.5 | -0.8 |  |
| follow_move+pin_rlm | close | pin $2k+ | 17-34 | 33.3 | -3.6 | -27.4 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 25-42 | 37.3 | -0.1 | -20.9 |  |
| money_level+pin_rlm | close | pin $2k+ | 7-8 | 46.7 | 3.9 | -8.2 |  |
| money_level+pin_value | close | pin $2k+ | 35-36 | 49.3 | 0.2 | -9.2 |  |
| money_level+rlm_ratio | close | pin $2k+ | 9-9 | 50.0 | 2.4 | -3.4 |  |
| money_moving+pin_rlm | close | pin $2k+ | 21-49 | 30.0 | -4.4 | -22.4 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 25-41 | 37.9 | 0.3 | -19.7 |  |
| pin_rlm+pin_value | close | pin $2k+ | 5-8 | 38.5 | 4.2 | 51.3 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 17-34 | 33.3 | -3.6 | -27.4 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 21-49 | 30.0 | -4.4 | -22.4 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 3-5 | 37.5 | -1.1 | -22.1 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 25-42 | 37.3 | -0.1 | -20.9 |  |
| consensus_gap+money_level | close | pin $2k+ | 45-34 | 57.0 | -5.1 | -11.8 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-14 | 22.2 | -6.7 | -3.9 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-10 | 0.0 | -28.6 | -100.0 |  |
| money_level+money_moving | close | pin limit <$1k | 54-59 | 47.8 | -2.2 | -8.1 |  |
| money_level+sharp_gap | close | pin limit <$1k | 56-58 | 49.1 | -1.1 | -5.6 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 87-87 | 50.0 | -1.0 | 1.2 |  |
| consensus_gap+money_level | close | pin limit <$1k | 21-22 | 48.8 | 0.9 | -9.8 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 27-30 | 47.4 | 0.2 | -3.2 |  |
| follow_move+money_moving | close | pin limit <$1k | 57-56 | 50.4 | -0.6 | -2.9 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 59-54 | 52.2 | 1.1 | 0.4 |  |
| money_level+pin_value | close | pin limit <$1k | 34-30 | 53.1 | 5.7 | 0.4 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 14-10 | 58.3 | 9.9 | 6.1 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 17-15 | 53.1 | 6.2 | 13.9 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 18-16 | 52.9 | 5.5 | 12.7 |  |
| follow_move+money_level | close | pin limit <$1k | 48-46 | 51.1 | 1.0 | -2.8 |  |
| follow_move+pin_value | close | pin limit <$1k | 28-19 | 59.6 | 11.1 | 12.8 |  |
| money_moving+pin_value | close | pin limit <$1k | 27-24 | 52.9 | 4.5 | 9.2 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 29-25 | 53.7 | 4.8 | 10.1 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 3-2 | 60.0 | 18.3 | 101.6 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 34-16 | 68.0 | 16.2 | 48.3 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 13-2 | 86.7 | 37.1 | 95.2 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 35-16 | 68.6 | 16.8 | 49.1 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 28-12 | 70.0 | 17.2 | 34.7 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 38-20 | 65.5 | 13.1 | 26.7 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 36-20 | 64.3 | 11.9 | 24.5 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 28-12 | 70.0 | 17.2 | 34.7 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 38-20 | 65.5 | 13.1 | 26.7 |  |
| money_level+pin_rlm | close | pin limit <$1k | 17-8 | 68.0 | 14.7 | 30.7 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 19-11 | 63.3 | 11.1 | 23.5 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 12-4 | 75.0 | 23.4 | 43.9 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 3-3 | 50.0 | 2.9 | -5.2 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 45.7 | 87.7 |  |
| pin_rlm | early | <1k bets | 1-1 | 50.0 | 24.1 | -3.7 | -2.15 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.4 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -49.3 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 262-238 | 52.4 | 0.5 | -8.6 | 0.28 |
| follow_move | early | pin $1-2k | 19-15 | 55.9 | 3.7 | 4.8 | -0.25 |
| follow_move | early | pin limit <$1k | 41-35 | 53.9 | 4.5 | 1.2 | -0.22 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.3 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.8 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 11-11 | 50.0 | 15.4 | 16.4 | 0.21 |
| rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.3 | 55.6 | -1.52 |
| rlm_ratio | early | pin limit <$1k | 6-1 | 85.7 | 40.8 | 74.9 | 0.19 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | -0.1 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 41.5 | 59.7 | 0.33 |
| money_level | early | <1k bets | 90-56 | 61.6 | 2.7 | -4.6 | 0.26 |
| money_level | early | pin $1-2k | 15-8 | 65.2 | 0.9 | -2.7 | -0.03 |
| money_level | early | pin limit <$1k | 22-24 | 47.8 | -6.2 | -12.1 | 0.31 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 6.9 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 6.2 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 78-57 | 57.8 | 8.0 | 10.8 | 0.49 |
| sharp_gap | early | pin $1-2k | 12-9 | 57.1 | 4.4 | 13.4 | -0.59 |
| sharp_gap | early | pin limit <$1k | 27-16 | 62.8 | 13.9 | 30.8 | 0.2 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.0 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.3 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 46-39 | 54.1 | 2.7 | -3.8 | 0.2 |
| money_moving | early | pin $1-2k | 6-6 | 50.0 | -11.6 | -26.9 | 0.35 |
| money_moving | early | pin limit <$1k | 20-9 | 69.0 | 19.7 | 47.8 | 0.36 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.4 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 30-33 | 47.6 | 0.1 | -9.7 | 0.19 |
| pin_value | early | pin $1-2k | 11-14 | 44.0 | -0.3 | -16.7 | 0.17 |
| pin_value | early | pin limit <$1k | 32-28 | 53.3 | 4.0 | 0.8 | 0.13 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -45.7 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -28.2 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -10.8 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 13.5 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 125-175 | 41.7 | -5.2 | -18.1 | 0.3 |
| consensus_gap | early | pin $1-2k | 10-17 | 37.0 | -8.1 | -27.6 | 0.49 |
| consensus_gap | early | pin limit <$1k | 17-33 | 34.0 | -16.0 | -29.1 | 0.31 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 15.8 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 2.3 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 2.7 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.0 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 18.7 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 15.2 | 26.0 | -0.25 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -0.2 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 4.5 | -6.9 | 0.3 |
| follow_move+pin_value | early | 1-3k bets | 7-6 | 53.8 | 6.4 | 0.8 | -0.31 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.9 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.3 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 2.1 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.1 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.3 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 26.6 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.3 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.0 | 25.3 | 0.18 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 18.1 | 56.1 | 0.15 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 19.1 | 18.8 | -0.24 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -25.9 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.8 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.8 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.3 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.8 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 35.8 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 45.7 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 19-27 | 41.3 | -10.2 | -26.0 | 0.92 |
| consensus_gap+money_level | early | <1k bets | 18-15 | 54.5 | -10.8 | -19.3 | 0.26 |
| consensus_gap+sharp_gap | early | <1k bets | 15-26 | 36.6 | -12.1 | -13.7 | 0.75 |
| follow_move+money_level | early | <1k bets | 49-25 | 66.2 | 7.1 | -2.4 | 0.43 |
| follow_move+sharp_gap | early | <1k bets | 40-19 | 67.8 | 17.3 | 18.8 | 0.64 |
| money_level+sharp_gap | early | <1k bets | 54-28 | 65.9 | 9.4 | 6.7 | 0.64 |
| follow_move+money_moving | early | <1k bets | 20-12 | 62.5 | 9.5 | 10.9 | 0.65 |
| money_level+money_moving | early | <1k bets | 30-22 | 57.7 | 0.7 | -7.6 | 0.1 |
| money_moving+sharp_gap | early | <1k bets | 30-21 | 58.8 | 8.1 | 5.8 | 0.52 |
| consensus_gap+money_moving | early | <1k bets | 8-15 | 34.8 | -12.6 | -44.1 | 0.14 |
| follow_move+pin_value | early | <1k bets | 11-11 | 50.0 | 2.3 | -5.9 | 0.05 |
| follow_move+rlm_ratio | early | <1k bets | 11-11 | 50.0 | 15.4 | 16.4 | 0.21 |
| rlm_ratio+sharp_gap | early | <1k bets | 11-11 | 50.0 | 15.4 | 16.4 | 0.21 |
| consensus_gap+pin_value | early | <1k bets | 11-22 | 33.3 | -12.1 | -37.3 | 0.45 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | <1k bets | 1-3 | 25.0 | -15.1 | -52.3 | -0.07 |
| follow_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 24.1 | -3.7 | -2.15 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 24.1 | -3.7 | -2.15 |
| pin_rlm+sharp_gap | early | <1k bets | 1-1 | 50.0 | 24.1 | -3.7 | -2.15 |
| pin_value+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 9.9 | -4.5 | -1.9 |
| pin_value+sharp_gap | early | <1k bets | 4-3 | 57.1 | 11.6 | 9.1 | 0.03 |
| money_level+pin_value | early | <1k bets | 3-3 | 50.0 | 1.4 | -4.5 | 1.33 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -53.6 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -54.3 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 0-2 | 0.0 | -49.3 | -100.0 | 2.5 |
| money_level+rlm_ratio | early | <1k bets | 5-5 | 50.0 | 12.8 | 0.9 | 1.52 |
| money_moving+rlm_ratio | early | <1k bets | 3-3 | 50.0 | 6.4 | 26.0 | 0.1 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| consensus_gap+money_level | early | pin $1-2k | 4-4 | 50.0 | -14.0 | -22.9 | 0.44 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -31.8 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 4-9 | 30.8 | -8.6 | -42.5 | 0.4 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.3 | 55.6 | -1.52 |
| follow_move+sharp_gap | early | pin $1-2k | 7-4 | 63.6 | 11.4 | 42.5 | -0.87 |
| money_level+money_moving | early | pin $1-2k | 6-5 | 54.5 | -10.3 | -20.3 | 0.02 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.3 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-3 | 40.0 | 3.3 | 55.6 | -1.52 |
| money_level+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 6.2 | 8.3 | -0.45 |
| money_moving+sharp_gap | early | pin $1-2k | 3-5 | 37.5 | -21.2 | -45.3 | -0.06 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.6 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 3-6 | 33.3 | -14.0 | -42.7 | 0.43 |
| follow_move+pin_value | early | pin $1-2k | 4-5 | 44.4 | 0.1 | -16.8 | -0.2 |
| follow_move+money_level | early | pin $1-2k | 7-4 | 63.6 | 1.2 | -0.7 | 0.07 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 47.2 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 2-1 | 66.7 | 1.5 | 4.7 | -0.53 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -25.0 | -62.8 | -0.72 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| money_level+money_moving | early | pin limit <$1k | 11-7 | 61.1 | 7.9 | 12.1 | 0.53 |
| money_level+sharp_gap | early | pin limit <$1k | 18-14 | 56.2 | 4.8 | 2.3 | 0.25 |
| money_moving+sharp_gap | early | pin limit <$1k | 16-5 | 76.2 | 27.9 | 68.0 | 0.39 |
| money_level+pin_value | early | pin limit <$1k | 8-5 | 61.5 | 9.9 | 16.6 | 0.46 |
| money_moving+pin_value | early | pin limit <$1k | 6-4 | 60.0 | 9.9 | 13.0 | 0.3 |
| pin_value+sharp_gap | early | pin limit <$1k | 11-5 | 68.8 | 18.1 | 30.3 | 0.06 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-9 | 40.0 | -10.7 | -25.7 | 0.53 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -27.1 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 13-18 | 41.9 | -6.1 | -21.4 | 0.44 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.4 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 10-11 | 47.6 | -7.1 | -12.3 | -0.09 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 5.1 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 12-7 | 63.2 | 14.2 | 20.4 | -0.13 |
| follow_move+rlm_ratio | early | pin limit <$1k | 6-1 | 85.7 | 40.8 | 74.9 | 0.19 |
| money_level+rlm_ratio | early | pin limit <$1k | 5-0 | 100.0 | 51.4 | 92.1 | 0.3 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.2 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 6-1 | 85.7 | 40.8 | 74.9 | 0.19 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 23.4 | 72.3 | 0.54 |
| follow_move+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 20.4 | 33.3 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.2 | 28.7 | -1.0 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -54.3 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -54.3 | -100.0 | 1.0 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| pin_rlm | close | 1-3k bets | 5-1 | 83.3 | 38.6 | 101.6 |  |
| pin_rlm | close | 3k+ bets | 2-4 | 33.3 | 3.1 | 3.5 |  |
| pin_rlm | close | pin $1-2k | 3-1 | 75.0 | 34.2 | 43.2 |  |
| pin_rlm | close | pin $2k+ | 3-4 | 42.9 | 11.8 | 53.0 |  |
| pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 31.6 | 87.0 |  |
| follow_move | close | 1-3k bets | 13-11 | 54.2 | -1.1 | -3.8 |  |
| follow_move | close | 3k+ bets | 10-12 | 45.5 | -3.4 | -19.2 |  |
| follow_move | close | pin $1-2k | 6-7 | 46.2 | 0.2 | -18.3 |  |
| follow_move | close | pin $2k+ | 10-7 | 58.8 | 6.8 | 25.1 |  |
| follow_move | close | pin limit <$1k | 1-0 | 100.0 | 31.6 | 90.9 |  |
| rlm_ratio | close | 1-3k bets | 4-2 | 66.7 | 15.8 | 70.4 |  |
| rlm_ratio | close | 3k+ bets | 2-2 | 50.0 | 22.4 | 55.2 |  |
| rlm_ratio | close | pin $1-2k | 2-1 | 66.7 | 22.8 | 27.3 |  |
| rlm_ratio | close | pin $2k+ | 2-1 | 66.7 | 43.1 | 193.3 |  |
| rlm_ratio | close | pin limit <$1k | 1-0 | 100.0 | 31.6 | 90.9 |  |
| money_level | close | 1-3k bets | 17-14 | 54.8 | -6.1 | -15.9 |  |
| money_level | close | 3k+ bets | 19-5 | 79.2 | 23.2 | 44.1 |  |
| money_level | close | pin $1-2k | 7-8 | 46.7 | -9.0 | -17.5 |  |
| money_level | close | pin $2k+ | 13-6 | 68.4 | 10.2 | 25.1 |  |
| money_level | close | pin limit <$1k | 2-1 | 66.7 | 10.5 | 26.0 |  |
| sharp_gap | close | 1-3k bets | 16-14 | 53.3 | 7.0 | 6.4 |  |
| sharp_gap | close | 3k+ bets | 12-11 | 52.2 | 9.4 | 5.2 |  |
| sharp_gap | close | pin $1-2k | 7-7 | 50.0 | 9.2 | -5.1 |  |
| sharp_gap | close | pin $2k+ | 11-7 | 61.1 | 15.1 | 36.4 |  |
| sharp_gap | close | pin limit <$1k | 2-1 | 66.7 | 10.5 | 26.0 |  |
| money_moving | close | 1-3k bets | 17-13 | 56.7 | 8.6 | 9.8 |  |
| money_moving | close | 3k+ bets | 12-11 | 52.2 | 9.4 | 5.2 |  |
| money_moving | close | pin $1-2k | 7-7 | 50.0 | 9.2 | -5.1 |  |
| money_moving | close | pin $2k+ | 11-7 | 61.1 | 15.1 | 36.4 |  |
| money_moving | close | pin limit <$1k | 2-1 | 66.7 | 10.5 | 26.0 |  |
| pin_value | close | 1-3k bets | 6-7 | 46.2 | -1.8 | -12.7 |  |
| pin_value | close | 3k+ bets | 2-4 | 33.3 | -22.8 | -37.6 |  |
| pin_value | close | pin $1-2k | 3-5 | 37.5 | -11.5 | -28.4 |  |
| pin_value | close | pin $2k+ | 3-5 | 37.5 | -12.5 | -30.1 |  |
| pin_value | close | pin limit <$1k | 2-1 | 66.7 | 10.5 | 26.0 |  |
| consensus_gap | close | 1-3k bets | 4-8 | 33.3 | -7.6 | 3.4 |  |
| consensus_gap | close | 3k+ bets | 4-5 | 44.4 | -6.7 | -21.8 |  |
| consensus_gap | close | pin $1-2k | 4-2 | 66.7 | 14.5 | 25.3 |  |
| consensus_gap | close | pin $2k+ | 3-5 | 37.5 | -6.5 | 25.7 |  |
| money_level+money_moving | close | 1-3k bets | 10-6 | 62.5 | 4.6 | 7.1 |  |
| money_level+pin_rlm | close | 1-3k bets | 3-0 | 100.0 | 36.8 | 89.6 |  |
| money_level+sharp_gap | close | 1-3k bets | 9-6 | 60.0 | 3.3 | 7.4 |  |
| money_moving+pin_rlm | close | 1-3k bets | 5-1 | 83.3 | 38.6 | 101.6 |  |
| money_moving+sharp_gap | close | 1-3k bets | 16-13 | 55.2 | 8.1 | 10.1 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 5-1 | 83.3 | 38.6 | 101.6 |  |
| money_level+pin_value | close | 1-3k bets | 3-3 | 50.0 | -6.1 | -6.2 |  |
| money_moving+pin_value | close | 1-3k bets | 4-3 | 57.1 | 10.2 | 7.6 |  |
| pin_value+sharp_gap | close | 1-3k bets | 4-3 | 57.1 | 10.2 | 7.6 |  |
| follow_move+money_level | close | 1-3k bets | 10-7 | 58.8 | -4.4 | -13.5 |  |
| follow_move+pin_value | close | 1-3k bets | 1-1 | 50.0 | 2.6 | -4.5 |  |
| consensus_gap+money_level | close | 1-3k bets | 1-2 | 33.3 | -27.2 | -38.9 |  |
| follow_move+money_moving | close | 1-3k bets | 7-3 | 70.0 | 17.9 | 41.7 |  |
| follow_move+pin_rlm | close | 1-3k bets | 2-0 | 100.0 | 54.0 | 220.4 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 4-2 | 66.7 | 15.8 | 70.4 |  |
| follow_move+sharp_gap | close | 1-3k bets | 6-3 | 66.7 | 17.3 | 46.1 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 4-2 | 66.7 | 15.8 | 70.4 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 2-0 | 100.0 | 54.0 | 220.4 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 4-2 | 66.7 | 15.8 | 70.4 |  |
| consensus_gap+money_moving | close | 1-3k bets | 3-5 | 37.5 | 0.1 | -29.8 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 3-5 | 37.5 | 0.1 | -29.8 |  |
| consensus_gap+pin_value | close | 1-3k bets | 1-3 | 25.0 | -19.0 | -52.3 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 1-1 | 50.0 | 22.4 | -4.5 |  |
| pin_rlm+pin_value | close | 1-3k bets | 2-0 | 100.0 | 50.0 | 88.9 |  |
| money_level+rlm_ratio | close | 1-3k bets | 3-1 | 75.0 | 10.5 | 43.2 |  |
| consensus_gap+follow_move | close | 1-3k bets | 0-1 | 0.0 | -23.5 | -100.0 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 0-1 | 0.0 | -23.5 | -100.0 |  |
| consensus_gap+money_level | close | 3k+ bets | 3-0 | 100.0 | 34.2 | 72.3 |  |
| consensus_gap+money_moving | close | 3k+ bets | 1-1 | 50.0 | 11.9 | -8.4 |  |
| consensus_gap+pin_value | close | 3k+ bets | 2-0 | 100.0 | 39.5 | 87.1 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 1-1 | 50.0 | 11.9 | -8.4 |  |
| money_level+money_moving | close | 3k+ bets | 12-4 | 75.0 | 26.3 | 51.3 |  |
| money_level+pin_value | close | 3k+ bets | 2-2 | 50.0 | -9.2 | -6.5 |  |
| money_level+sharp_gap | close | 3k+ bets | 12-4 | 75.0 | 26.3 | 51.3 |  |
| money_moving+pin_value | close | 3k+ bets | 1-2 | 33.3 | -15.8 | -38.9 |  |
| money_moving+sharp_gap | close | 3k+ bets | 12-11 | 52.2 | 9.4 | 5.2 |  |
| pin_value+sharp_gap | close | 3k+ bets | 1-2 | 33.3 | -15.8 | -38.9 |  |
| follow_move+money_level | close | 3k+ bets | 9-4 | 69.2 | 15.3 | 21.6 |  |
| follow_move+money_moving | close | 3k+ bets | 5-6 | 45.5 | 2.4 | -2.9 |  |
| follow_move+sharp_gap | close | 3k+ bets | 5-6 | 45.5 | 2.4 | -2.9 |  |
| consensus_gap+follow_move | close | 3k+ bets | 0-2 | 0.0 | -61.9 | -100.0 |  |
| follow_move+pin_rlm | close | 3k+ bets | 2-2 | 50.0 | 22.4 | 55.2 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 2-2 | 50.0 | 22.4 | 55.2 |  |
| money_level+pin_rlm | close | 3k+ bets | 2-1 | 66.7 | 37.8 | 107.0 |  |
| money_level+rlm_ratio | close | 3k+ bets | 2-1 | 66.7 | 37.8 | 107.0 |  |
| money_moving+pin_rlm | close | 3k+ bets | 2-4 | 33.3 | 3.1 | 3.5 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 2-2 | 50.0 | 22.4 | 55.2 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 2-2 | 50.0 | 22.4 | 55.2 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 2-4 | 33.3 | 3.1 | 3.5 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 2-2 | 50.0 | 22.4 | 55.2 |  |
| follow_move+pin_value | close | 3k+ bets | 0-1 | 0.0 | -47.4 | -100.0 |  |
| pin_rlm+pin_value | close | 3k+ bets | 0-1 | 0.0 | -47.4 | -100.0 |  |
| money_level+money_moving | close | pin $1-2k | 4-4 | 50.0 | 3.9 | -5.5 |  |
| money_level+pin_value | close | pin $1-2k | 1-2 | 33.3 | -35.1 | -36.4 |  |
| money_level+sharp_gap | close | pin $1-2k | 4-4 | 50.0 | 3.9 | -5.5 |  |
| money_moving+pin_value | close | pin $1-2k | 2-2 | 50.0 | 11.2 | -4.5 |  |
| money_moving+sharp_gap | close | pin $1-2k | 7-7 | 50.0 | 9.2 | -5.1 |  |
| pin_value+sharp_gap | close | pin $1-2k | 2-2 | 50.0 | 11.2 | -4.5 |  |
| follow_move+money_level | close | pin $1-2k | 4-5 | 44.4 | -6.2 | -24.9 |  |
| follow_move+money_moving | close | pin $1-2k | 3-3 | 50.0 | 12.3 | -4.5 |  |
| follow_move+sharp_gap | close | pin $1-2k | 3-3 | 50.0 | 12.3 | -4.5 |  |
| consensus_gap+money_level | close | pin $1-2k | 2-0 | 100.0 | 39.5 | 87.1 |  |
| consensus_gap+money_moving | close | pin $1-2k | 2-1 | 66.7 | 30.8 | 24.7 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 2-1 | 66.7 | 30.8 | 24.7 |  |
| consensus_gap+pin_value | close | pin $1-2k | 2-2 | 50.0 | 2.0 | -4.5 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 1-0 | 100.0 | 68.4 | 90.9 |  |
| money_moving+pin_rlm | close | pin $1-2k | 3-1 | 75.0 | 34.2 | 43.2 |  |
| pin_rlm+pin_value | close | pin $1-2k | 1-0 | 100.0 | 68.4 | 90.9 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 3-1 | 75.0 | 34.2 | 43.2 |  |
| follow_move+pin_rlm | close | pin $1-2k | 2-1 | 66.7 | 22.8 | 27.3 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 2-1 | 66.7 | 22.8 | 27.3 |  |
| money_level+pin_rlm | close | pin $1-2k | 2-1 | 66.7 | 22.8 | 27.3 |  |
| money_level+rlm_ratio | close | pin $1-2k | 2-1 | 66.7 | 22.8 | 27.3 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 2-1 | 66.7 | 22.8 | 27.3 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 2-1 | 66.7 | 22.8 | 27.3 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 2-1 | 66.7 | 22.8 | 27.3 |  |
| money_level+money_moving | close | pin $2k+ | 8-2 | 80.0 | 27.1 | 63.4 |  |
| money_level+pin_rlm | close | pin $2k+ | 2-0 | 100.0 | 61.9 | 210.4 |  |
| money_level+sharp_gap | close | pin $2k+ | 8-2 | 80.0 | 27.1 | 63.4 |  |
| money_moving+pin_rlm | close | pin $2k+ | 3-4 | 42.9 | 11.8 | 53.0 |  |
| money_moving+sharp_gap | close | pin $2k+ | 11-7 | 61.1 | 15.1 | 36.4 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 3-4 | 42.9 | 11.8 | 53.0 |  |
| consensus_gap+money_level | close | pin $2k+ | 2-2 | 50.0 | -14.6 | -18.5 |  |
| consensus_gap+money_moving | close | pin $2k+ | 1-2 | 33.3 | -9.6 | -38.9 |  |
| consensus_gap+pin_value | close | pin $2k+ | 1-1 | 50.0 | -2.6 | -8.4 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 1-2 | 33.3 | -9.6 | -38.9 |  |
| money_level+pin_value | close | pin $2k+ | 3-3 | 50.0 | 0.0 | -6.9 |  |
| money_moving+pin_value | close | pin $2k+ | 2-3 | 40.0 | -10.5 | -26.4 |  |
| pin_value+sharp_gap | close | pin $2k+ | 2-3 | 40.0 | -10.5 | -26.4 |  |
| follow_move+money_level | close | pin $2k+ | 8-4 | 66.7 | 8.7 | 23.2 |  |
| follow_move+money_moving | close | pin $2k+ | 5-2 | 71.4 | 26.0 | 89.5 |  |
| follow_move+sharp_gap | close | pin $2k+ | 5-2 | 71.4 | 26.0 | 89.5 |  |
| follow_move+pin_value | close | pin $2k+ | 1-2 | 33.3 | -14.0 | -36.4 |  |
| follow_move+pin_rlm | close | pin $2k+ | 2-1 | 66.7 | 43.1 | 193.3 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 2-1 | 66.7 | 43.1 | 193.3 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 2-1 | 66.7 | 43.1 | 193.3 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 2-1 | 66.7 | 43.1 | 193.3 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 2-1 | 66.7 | 43.1 | 193.3 |  |
| money_level+rlm_ratio | close | pin $2k+ | 1-0 | 100.0 | 76.5 | 330.0 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -23.5 | -100.0 |  |
| pin_rlm+pin_value | close | pin $2k+ | 0-1 | 0.0 | -47.4 | -100.0 |  |
| money_level+money_moving | close | pin limit <$1k | 2-1 | 66.7 | 10.5 | 26.0 |  |
| money_level+sharp_gap | close | pin limit <$1k | 2-1 | 66.7 | 10.5 | 26.0 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 2-1 | 66.7 | 10.5 | 26.0 |  |
| follow_move+money_level | close | pin limit <$1k | 1-0 | 100.0 | 31.6 | 90.9 |  |
| follow_move+money_moving | close | pin limit <$1k | 1-0 | 100.0 | 31.6 | 90.9 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 1-0 | 100.0 | 31.6 | 90.9 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 1-0 | 100.0 | 31.6 | 90.9 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 1-0 | 100.0 | 31.6 | 90.9 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 1-0 | 100.0 | 31.6 | 90.9 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 1-0 | 100.0 | 31.6 | 90.9 |  |
| money_level+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 31.6 | 87.0 |  |
| money_level+pin_value | close | pin limit <$1k | 1-0 | 100.0 | 31.6 | 87.0 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 31.6 | 87.0 |  |
| money_moving+pin_value | close | pin limit <$1k | 1-0 | 100.0 | 31.6 | 87.0 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 1-0 | 100.0 | 31.6 | 87.0 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 1-0 | 100.0 | 31.6 | 87.0 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 1-0 | 100.0 | 31.6 | 87.0 |  |
| follow_move | early | <1k bets | 12-11 | 52.2 | -2.9 | -28.2 | 0.08 |
| money_level | early | <1k bets | 4-0 | 100.0 | 23.5 | 20.7 | -1.47 |
| sharp_gap | early | <1k bets | 1-2 | 33.3 | -7.8 | -43.2 | -2.53 |
| money_moving | early | <1k bets | 2-1 | 66.7 | 7.8 | -9.0 | -2.17 |
| consensus_gap | early | <1k bets | 8-5 | 61.5 | 8.7 | 5.4 | 0.04 |
| money_level+money_moving | early | <1k bets | 2-0 | 100.0 | 23.5 | 36.4 | -3.25 |
| money_level+sharp_gap | early | <1k bets | 1-0 | 100.0 | 23.5 | 70.4 | -6.8 |
| money_moving+sharp_gap | early | <1k bets | 1-1 | 50.0 | 0.0 | -14.8 | -3.4 |
| consensus_gap+money_moving | early | <1k bets | 0-1 | 0.0 | -23.5 | -100.0 | 0.0 |
| consensus_gap+sharp_gap | early | <1k bets | 0-2 | 0.0 | -23.5 | -100.0 | -0.4 |
| follow_move+money_level | early | <1k bets | 3-0 | 100.0 | 23.5 | 4.1 | 0.3 |
| follow_move+money_moving | early | <1k bets | 1-0 | 100.0 | 23.5 | 2.5 | 0.3 |
