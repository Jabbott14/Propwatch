# CBB scorecard

Generated 2026-11-18 20:55 UTC. 584 graded games (16 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**512 games before 2026-11-17 (fit) · 72 on or after it (forward).**

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
sample ran **47.2% favourites** (n=583) and **47.9% overs** (n=584) and **73.4% moneyline favourites** (n=496).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-17. Nothing in the engine was chosen using these. n=72 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 0-1 | 0.0 | 31.7 | -31.7 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| follow_move | both | 66-50 | 56.9 | 52.8 | 4.1 | +1.55 | 1.3 | 0.15 | 42.2 | no edge shown yet |
| rlm_ratio | both | 4-0 | 100.0 | 40.9 | 59.1 | +4.98 | 124.5 | 1.62 | 75.0 | keep collecting (4/30) |
| money_level | both | 17-9 | 65.4 | 65.7 | -0.3 | -1.18 | -4.5 | -0.9 | 30.8 | keep collecting (26/30) |
| sharp_gap | both | 14-11 | 56.0 | 51.7 | 4.3 | +0.08 | 0.3 | -0.18 | 36.0 | keep collecting (25/30) |
| money_moving | both | 14-7 | 66.7 | 50.0 | 16.7 | +2.53 | 12.0 | -0.74 | 38.1 | keep collecting (21/30) |
| pin_value | both | 6-6 | 50.0 | 51.4 | -1.4 | -0.76 | -6.3 | -0.21 | 16.7 | keep collecting (12/30) |
| consensus_gap | both | 34-27 | 55.7 | 48.4 | 7.3 | +23.84 | 39.1 | 0.94 | 42.6 | no edge shown yet |
| money_level+money_moving | both | 9-2 | 81.8 | 64.5 | 17.3 | +2.09 | 19.0 | -1.57 | 36.4 | keep collecting (11/30) |
| money_level+sharp_gap | both | 10-5 | 66.7 | 64.4 | 2.3 | +1.14 | 7.6 | -0.93 | 26.7 | keep collecting (15/30) |
| money_moving+sharp_gap | both | 9-5 | 64.3 | 50.3 | 14.0 | +2.2 | 15.7 | -0.84 | 35.7 | keep collecting (14/30) |
| consensus_gap+money_moving | both | 0-2 | 0.0 | 31.7 | -31.7 | -2.0 | -100.0 | -1.4 | 0.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | both | 3-5 | 37.5 | 40.9 | -3.4 | -2.16 | -27.0 | 1.09 | 50.0 | keep collecting (8/30) |
| follow_move+money_level | both | 10-4 | 71.4 | 67.3 | 4.1 | -1.16 | -8.3 | -0.54 | 42.9 | keep collecting (14/30) |
| follow_move+money_moving | both | 8-3 | 72.7 | 55.8 | 17.0 | +2.16 | 19.7 | -0.23 | 54.5 | keep collecting (11/30) |
| follow_move+rlm_ratio | both | 4-0 | 100.0 | 40.9 | 59.1 | +4.98 | 124.5 | 1.62 | 75.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 6-3 | 66.7 | 55.6 | 11.1 | +2.19 | 24.3 | 0.21 | 44.4 | keep collecting (9/30) |
| money_moving+rlm_ratio | both | 3-0 | 100.0 | 43.9 | 56.1 | +3.66 | 122.0 | 0.67 | 66.7 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | both | 4-0 | 100.0 | 40.9 | 59.1 | +4.98 | 124.5 | 1.62 | 75.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 5-2 | 71.4 | 47.4 | 24.0 | +2.79 | 39.9 | 2.19 | 71.4 | keep collecting (7/30) |
| consensus_gap+pin_value | both | 2-1 | 66.7 | 50.9 | 15.7 | +0.62 | 20.8 | -0.17 | 0.0 | keep collecting (3/30) |
| money_level+pin_value | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_value+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -0.5 | 0.0 | keep collecting (2/30) |
| consensus_gap+money_level | both | 2-1 | 66.7 | 68.3 | -1.6 | +0.52 | 17.5 | 1.17 | 66.7 | keep collecting (3/30) |
| money_moving+pin_value | both | 1-0 | 100.0 | 36.1 | 63.9 | +0.91 | 90.9 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+rlm_ratio | both | 1-0 | 100.0 | 63.9 | 36.1 | +0.95 | 95.2 | 1.0 | 100.0 | keep collecting (1/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 31.7 | -31.7 | -1.0 | -100.0 | 1.3 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 0-1 | 0.0 | 31.7 | -31.7 | -1.0 | -100.0 | 1.3 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+pin_value | both | 2-0 | 100.0 | 57.7 | 42.3 | +1.61 | 80.3 | -0.75 | 0.0 | keep collecting (2/30) |
| consensus_gap+rlm_ratio | both | 1-0 | 100.0 | 31.7 | 68.3 | +1.32 | 132.0 | 4.5 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 0-1 | 0.0 | 31.7 | -31.7 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| follow_move | moneyline | 30-16 | 65.2 | 56.3 | 8.9 | +2.29 | 5.0 | -0.37 | 41.3 | PROMOTE: beats break-even and its own base rate |
| follow_move | spread | 15-14 | 51.7 | 50.5 | 1.2 | +0.12 | 0.4 | -0.38 | 24.1 | keep collecting (29/30) |
| follow_move | total | 21-20 | 51.2 | 50.3 | 0.9 | -0.86 | -2.1 | 1.1 | 56.1 | no edge shown yet |
| rlm_ratio | moneyline | 2-0 | 100.0 | 31.7 | 68.3 | +3.12 | 156.0 | 2.25 | 50.0 | keep collecting (2/30) |
| rlm_ratio | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | 1.0 | 100.0 | keep collecting (2/30) |
| money_level | moneyline | 13-4 | 76.5 | 68.3 | 8.2 | +0.14 | 0.8 | -0.91 | 41.2 | keep collecting (17/30) |
| money_level | total | 4-5 | 44.4 | 60.8 | -16.4 | -1.32 | -14.7 | -0.89 | 11.1 | keep collecting (9/30) |
| sharp_gap | moneyline | 8-8 | 50.0 | 50.0 | 0.0 | -2.42 | -15.1 | -0.15 | 37.5 | keep collecting (16/30) |
| sharp_gap | total | 6-3 | 66.7 | 54.6 | 12.0 | +2.5 | 27.7 | -0.22 | 33.3 | keep collecting (9/30) |
| money_moving | moneyline | 7-6 | 53.8 | 54.2 | -0.4 | -2.88 | -22.1 | -1.51 | 30.8 | keep collecting (13/30) |
| money_moving | total | 7-1 | 87.5 | 43.1 | 44.4 | +5.41 | 67.6 | 0.5 | 50.0 | keep collecting (8/30) |
| pin_value | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.29 | -14.3 | -0.25 | 0.0 | keep collecting (2/30) |
| pin_value | spread | 2-3 | 40.0 | 50.6 | -10.6 | -1.2 | -24.0 | 0.0 | 20.0 | keep collecting (5/30) |
| pin_value | total | 3-2 | 60.0 | 52.8 | 7.2 | +0.73 | 14.5 | -0.4 | 20.0 | keep collecting (5/30) |
| consensus_gap | moneyline | 16-20 | 44.4 | 44.9 | -0.5 | +14.82 | 41.2 | 0.73 | 41.7 | no edge shown yet |
| consensus_gap | spread | 6-4 | 60.0 | 48.9 | 11.1 | +1.42 | 14.2 | 0.0 | 20.0 | keep collecting (10/30) |
| consensus_gap | total | 12-3 | 80.0 | 56.5 | 23.5 | +7.6 | 50.6 | 2.07 | 60.0 | keep collecting (15/30) |
| money_level+money_moving | moneyline | 6-2 | 75.0 | 68.3 | 6.7 | -0.68 | -8.5 | -1.91 | 37.5 | keep collecting (8/30) |
| money_level+sharp_gap | moneyline | 6-2 | 75.0 | 68.3 | 6.7 | +0.46 | 5.8 | -1.11 | 37.5 | keep collecting (8/30) |
| money_moving+sharp_gap | moneyline | 4-5 | 44.4 | 52.0 | -7.6 | -2.39 | -26.5 | -1.41 | 22.2 | keep collecting (9/30) |
| consensus_gap+money_moving | moneyline | 0-2 | 0.0 | 31.7 | -31.7 | -2.0 | -100.0 | -1.4 | 0.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 3-5 | 37.5 | 40.9 | -3.4 | -2.16 | -27.0 | 1.09 | 50.0 | keep collecting (8/30) |
| follow_move+money_level | moneyline | 9-2 | 81.8 | 68.3 | 13.6 | -0.11 | -1.0 | -0.6 | 45.5 | keep collecting (11/30) |
| follow_move+money_moving | moneyline | 5-2 | 71.4 | 63.0 | 8.4 | +0.39 | 5.6 | -1.07 | 42.9 | keep collecting (7/30) |
| consensus_gap+money_level | moneyline | 2-1 | 66.7 | 68.3 | -1.6 | +0.52 | 17.5 | 1.17 | 66.7 | keep collecting (3/30) |
| follow_move+sharp_gap | moneyline | 4-2 | 66.7 | 56.1 | 10.6 | +1.33 | 22.1 | -0.02 | 33.3 | keep collecting (6/30) |
| follow_move+rlm_ratio | moneyline | 2-0 | 100.0 | 31.7 | 68.3 | +3.12 | 156.0 | 2.25 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_ratio | moneyline | 1-0 | 100.0 | 31.7 | 68.3 | +1.8 | 180.0 | 0.0 | 0.0 | keep collecting (1/30) |
| rlm_ratio+sharp_gap | moneyline | 2-0 | 100.0 | 31.7 | 68.3 | +3.12 | 156.0 | 2.25 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 31.7 | -31.7 | -1.0 | -100.0 | 1.3 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 0-1 | 0.0 | 31.7 | -31.7 | -1.0 | -100.0 | 1.3 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 2-1 | 66.7 | 43.9 | 22.8 | +1.03 | 34.5 | 1.77 | 66.7 | keep collecting (3/30) |
| consensus_gap+pin_value | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.29 | -14.3 | -0.25 | 0.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_value | moneyline | 1-0 | 100.0 | 68.3 | 31.7 | +0.71 | 71.4 | -0.5 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | moneyline | 1-0 | 100.0 | 31.7 | 68.3 | +1.32 | 132.0 | 4.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+follow_move | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.02 | -1.0 | 0.5 | 50.0 | keep collecting (2/30) |
| consensus_gap+pin_value | spread | 1-0 | 100.0 | 52.8 | 47.2 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+pin_value | spread | 1-0 | 100.0 | 47.2 | 52.8 | +0.89 | 89.3 | -1.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | total | 3-1 | 75.0 | 43.1 | 31.9 | +1.77 | 44.2 | 1.25 | 75.0 | keep collecting (4/30) |
| follow_move+rlm_ratio | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | 1.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 2-1 | 66.7 | 54.6 | 12.0 | +0.86 | 28.7 | 0.67 | 66.7 | keep collecting (3/30) |
| money_moving+rlm_ratio | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | 1.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+sharp_gap | total | 5-0 | 100.0 | 47.2 | 52.8 | +4.59 | 91.8 | 0.2 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | 1.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 | 4.5 | 100.0 | keep collecting (2/30) |
| money_level+pin_value | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -0.5 | 0.0 | keep collecting (2/30) |
| money_level+sharp_gap | total | 4-3 | 57.1 | 59.9 | -2.8 | +0.68 | 9.7 | -0.71 | 14.3 | keep collecting (7/30) |
| pin_value+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -0.5 | 0.0 | keep collecting (2/30) |
| money_level+money_moving | total | 3-0 | 100.0 | 54.6 | 45.4 | +2.77 | 92.3 | -0.67 | 33.3 | keep collecting (3/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 36.1 | 63.9 | +0.91 | 90.9 | -1.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_level | total | 1-2 | 33.3 | 63.9 | -30.6 | -1.05 | -34.9 | -0.33 | 33.3 | keep collecting (3/30) |
| money_level+rlm_ratio | total | 1-0 | 100.0 | 63.9 | 36.1 | +0.95 | 95.2 | 1.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 13-17 | 43.3 | 40.4 | 2.9 | +2.89 | 9.6 |  |  | no edge shown yet |
| follow_move | both | 86-79 | 52.1 | 51.9 | 0.3 | -9.82 | -6.0 |  |  | no edge shown yet |
| rlm_ratio | both | 20-22 | 47.6 | 42.2 | 5.5 | +4.51 | 10.7 |  |  | no edge shown yet |
| money_level | both | 122-84 | 59.2 | 56.4 | 2.8 | +1.88 | 0.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 97-99 | 49.5 | 47.8 | 1.7 | -1.81 | -0.9 |  |  | no edge shown yet |
| money_moving | both | 97-100 | 49.2 | 48.1 | 1.2 | -4.25 | -2.2 |  |  | no edge shown yet |
| pin_value | both | 28-38 | 42.4 | 46.4 | -4.0 | +6.47 | 9.8 |  |  | DROP: below break-even |
| consensus_gap | both | 24-33 | 42.1 | 44.4 | -2.3 | +0.58 | 1.0 |  |  | DROP: below break-even |
| money_level+money_moving | both | 73-53 | 57.9 | 53.2 | 4.7 | +6.9 | 5.5 |  |  | no edge shown yet |
| money_level+pin_rlm | both | 6-5 | 54.5 | 43.9 | 10.6 | +2.81 | 25.5 |  |  | keep collecting (11/30) |
| money_level+sharp_gap | both | 72-52 | 58.1 | 53.0 | 5.1 | +8.39 | 6.8 |  |  | no edge shown yet |
| money_moving+pin_rlm | both | 13-17 | 43.3 | 40.4 | 2.9 | +2.89 | 9.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | both | 95-97 | 49.5 | 47.9 | 1.6 | -1.39 | -0.7 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 13-17 | 43.3 | 40.4 | 2.9 | +2.89 | 9.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_value | both | 12-16 | 42.9 | 53.0 | -10.1 | -5.61 | -20.0 |  |  | keep collecting (28/30) |
| money_moving+pin_value | both | 12-21 | 36.4 | 46.3 | -10.0 | -4.61 | -14.0 |  |  | DROP: below break-even |
| pin_value+sharp_gap | both | 12-21 | 36.4 | 46.2 | -9.8 | -4.61 | -14.0 |  |  | DROP: below break-even |
| consensus_gap+money_level | both | 9-7 | 56.2 | 57.5 | -1.3 | -0.52 | -3.2 |  |  | keep collecting (16/30) |
| consensus_gap+money_moving | both | 12-17 | 41.4 | 41.8 | -0.4 | +1.17 | 4.0 |  |  | keep collecting (29/30) |
| consensus_gap+pin_value | both | 8-8 | 50.0 | 43.7 | 6.3 | +4.97 | 31.1 |  |  | keep collecting (16/30) |
| consensus_gap+sharp_gap | both | 12-17 | 41.4 | 41.8 | -0.4 | +1.17 | 4.0 |  |  | keep collecting (29/30) |
| follow_move+money_level | both | 62-41 | 60.2 | 57.3 | 2.9 | -0.89 | -0.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+money_moving | both | 52-48 | 52.0 | 50.2 | 1.8 | +1.03 | 1.0 |  |  | no edge shown yet |
| follow_move+sharp_gap | both | 52-48 | 52.0 | 49.8 | 2.2 | +2.47 | 2.5 |  |  | no edge shown yet |
| follow_move+pin_value | both | 4-11 | 26.7 | 49.1 | -22.4 | -7.44 | -49.6 |  |  | keep collecting (15/30) |
| follow_move+pin_rlm | both | 8-8 | 50.0 | 39.2 | 10.8 | +7.35 | 45.9 |  |  | keep collecting (16/30) |
| follow_move+rlm_ratio | both | 20-22 | 47.6 | 42.2 | 5.5 | +4.51 | 10.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_ratio | both | 19-22 | 46.3 | 42.3 | 4.0 | +3.56 | 8.7 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 8-8 | 50.0 | 39.2 | 10.8 | +7.35 | 45.9 |  |  | keep collecting (16/30) |
| rlm_ratio+sharp_gap | both | 20-22 | 47.6 | 42.2 | 5.5 | +4.51 | 10.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 6-7 | 46.2 | 48.3 | -2.1 | -2.22 | -17.0 |  |  | keep collecting (13/30) |
| money_level+rlm_ratio | both | 10-8 | 55.6 | 47.9 | 7.6 | +3.72 | 20.7 |  |  | keep collecting (18/30) |
| consensus_gap+pin_rlm | both | 2-3 | 40.0 | 33.5 | 6.5 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| pin_rlm+pin_value | both | 4-5 | 44.4 | 42.4 | 2.0 | -1.4 | -15.6 |  |  | keep collecting (9/30) |
| consensus_gap+rlm_ratio | both | 1-2 | 33.3 | 33.2 | 0.1 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| pin_value+rlm_ratio | both | 1-2 | 33.3 | 36.1 | -2.8 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| pin_rlm | moneyline | 3-7 | 30.0 | 31.7 | -1.7 | +3.8 | 38.0 |  |  | keep collecting (10/30) |
| pin_rlm | spread | 2-4 | 33.3 | 50.9 | -17.6 | -2.14 | -35.7 |  |  | keep collecting (6/30) |
| pin_rlm | total | 8-6 | 57.1 | 42.1 | 15.1 | +1.23 | 8.8 |  |  | keep collecting (14/30) |
| follow_move | moneyline | 36-20 | 64.3 | 56.5 | 7.8 | +3.14 | 5.6 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move | spread | 16-31 | 34.0 | 50.5 | -16.5 | -16.06 | -34.2 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move | total | 34-28 | 54.8 | 48.7 | 6.2 | +3.1 | 5.0 |  |  | no edge shown yet |
| rlm_ratio | moneyline | 5-7 | 41.7 | 37.8 | 3.8 | +5.69 | 47.4 |  |  | keep collecting (12/30) |
| rlm_ratio | spread | 2-3 | 40.0 | 49.4 | -9.4 | -1.15 | -23.0 |  |  | keep collecting (5/30) |
| rlm_ratio | total | 13-12 | 52.0 | 42.8 | 9.2 | -0.04 | -0.1 |  |  | keep collecting (25/30) |
| money_level | moneyline | 45-17 | 72.6 | 64.1 | 8.4 | -0.97 | -1.6 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level | spread | 34-38 | 47.2 | 48.9 | -1.7 | -7.28 | -10.1 |  |  | no edge shown yet |
| money_level | total | 43-29 | 59.7 | 57.3 | 2.4 | +10.12 | 14.1 |  |  | no edge shown yet |
| sharp_gap | moneyline | 23-33 | 41.1 | 45.4 | -4.4 | -2.96 | -5.3 |  |  | DROP: below break-even |
| sharp_gap | spread | 34-37 | 47.9 | 49.3 | -1.4 | -6.3 | -8.9 |  |  | no edge shown yet |
| sharp_gap | total | 40-29 | 58.0 | 48.2 | 9.8 | +7.44 | 10.8 |  |  | no edge shown yet |
| money_moving | moneyline | 24-32 | 42.9 | 46.1 | -3.2 | -2.44 | -4.4 |  |  | no edge shown yet |
| money_moving | spread | 34-37 | 47.9 | 49.3 | -1.4 | -6.3 | -8.9 |  |  | no edge shown yet |
| money_moving | total | 39-31 | 55.7 | 48.4 | 7.3 | +4.49 | 6.4 |  |  | no edge shown yet |
| pin_value | moneyline | 3-5 | 37.5 | 31.7 | 5.8 | +17.4 | 217.5 |  |  | keep collecting (8/30) |
| pin_value | spread | 10-16 | 38.5 | 48.7 | -10.3 | -7.41 | -28.5 |  |  | keep collecting (26/30) |
| pin_value | total | 15-17 | 46.9 | 48.3 | -1.4 | -3.51 | -11.0 |  |  | no edge shown yet |
| consensus_gap | moneyline | 10-25 | 28.6 | 40.1 | -11.5 | -3.57 | -10.2 |  |  | DROP: below break-even |
| consensus_gap | spread | 6-5 | 54.5 | 48.7 | 5.8 | +0.07 | 0.7 |  |  | keep collecting (11/30) |
| consensus_gap | total | 8-3 | 72.7 | 53.8 | 18.9 | +4.08 | 37.1 |  |  | keep collecting (11/30) |
| money_moving+sharp_gap | moneyline | 22-31 | 41.5 | 45.5 | -4.0 | -1.58 | -3.0 |  |  | DROP: below break-even |
| follow_move+money_level | moneyline | 28-8 | 77.8 | 66.2 | 11.6 | +0.89 | 2.5 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 14-11 | 56.0 | 53.7 | 2.3 | +3.13 | 12.5 |  |  | keep collecting (25/30) |
| follow_move+sharp_gap | moneyline | 13-11 | 54.2 | 53.0 | 1.1 | +3.62 | 15.1 |  |  | keep collecting (24/30) |
| money_level+money_moving | moneyline | 19-8 | 70.4 | 60.1 | 10.2 | +2.96 | 11.0 |  |  | keep collecting (27/30) |
| money_level+sharp_gap | moneyline | 18-8 | 69.2 | 59.8 | 9.4 | +3.45 | 13.3 |  |  | keep collecting (26/30) |
| consensus_gap+money_level | moneyline | 4-4 | 50.0 | 63.7 | -13.7 | -1.79 | -22.4 |  |  | keep collecting (8/30) |
| follow_move+pin_rlm | moneyline | 3-1 | 75.0 | 31.7 | 43.3 | +9.8 | 245.0 |  |  | keep collecting (4/30) |
| follow_move+rlm_ratio | moneyline | 5-7 | 41.7 | 37.8 | 3.8 | +5.69 | 47.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_rlm | moneyline | 3-7 | 30.0 | 31.7 | -1.7 | +3.8 | 38.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | moneyline | 5-7 | 41.7 | 37.8 | 3.8 | +5.69 | 47.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+rlm_ratio | moneyline | 3-1 | 75.0 | 31.7 | 43.3 | +9.8 | 245.0 |  |  | keep collecting (4/30) |
| pin_rlm+sharp_gap | moneyline | 3-7 | 30.0 | 31.7 | -1.7 | +3.8 | 38.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 5-7 | 41.7 | 37.8 | 3.8 | +5.69 | 47.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 3-5 | 37.5 | 45.4 | -7.9 | -2.86 | -35.8 |  |  | keep collecting (8/30) |
| money_level+pin_rlm | moneyline | 1-1 | 50.0 | 31.7 | 18.3 | +2.3 | 115.0 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | moneyline | 2-1 | 66.7 | 43.9 | 22.8 | +3.4 | 113.3 |  |  | keep collecting (3/30) |
| consensus_gap+money_moving | moneyline | 5-14 | 26.3 | 37.5 | -11.2 | -1.92 | -10.1 |  |  | keep collecting (19/30) |
| consensus_gap+rlm_ratio | moneyline | 0-2 | 0.0 | 31.7 | -31.7 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 5-14 | 26.3 | 37.5 | -11.2 | -1.92 | -10.1 |  |  | keep collecting (19/30) |
| consensus_gap+pin_rlm | moneyline | 0-3 | 0.0 | 31.7 | -31.7 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| consensus_gap+pin_value | moneyline | 1-3 | 25.0 | 31.7 | -6.7 | +3.8 | 95.0 |  |  | keep collecting (4/30) |
| money_moving+pin_value | moneyline | 1-2 | 33.3 | 31.7 | 1.6 | +4.8 | 160.0 |  |  | keep collecting (3/30) |
| pin_value+sharp_gap | moneyline | 1-3 | 25.0 | 31.7 | -6.7 | +3.8 | 95.0 |  |  | keep collecting (4/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 31.7 | -31.7 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+money_moving | spread | 27-30 | 47.4 | 48.9 | -1.5 | -5.63 | -9.9 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 1-2 | 33.3 | 49.1 | -15.7 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| money_level+sharp_gap | spread | 27-30 | 47.4 | 48.9 | -1.5 | -5.63 | -9.9 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 2-4 | 33.3 | 50.9 | -17.6 | -2.14 | -35.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | spread | 34-37 | 47.9 | 49.3 | -1.4 | -6.3 | -8.9 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 2-4 | 33.3 | 50.9 | -17.6 | -2.14 | -35.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+money_level | spread | 3-3 | 50.0 | 47.2 | 2.8 | -0.5 | -8.4 |  |  | keep collecting (6/30) |
| consensus_gap+money_moving | spread | 2-3 | 40.0 | 47.2 | -7.2 | -1.33 | -26.7 |  |  | keep collecting (5/30) |
| consensus_gap+pin_value | spread | 3-2 | 60.0 | 47.2 | 12.8 | +0.57 | 11.5 |  |  | keep collecting (5/30) |
| consensus_gap+sharp_gap | spread | 2-3 | 40.0 | 47.2 | -7.2 | -1.33 | -26.7 |  |  | keep collecting (5/30) |
| money_level+pin_value | spread | 8-10 | 44.4 | 48.5 | -4.0 | -3.17 | -17.6 |  |  | keep collecting (18/30) |
| money_moving+pin_value | spread | 6-11 | 35.3 | 48.5 | -13.2 | -5.91 | -34.8 |  |  | keep collecting (17/30) |
| pin_value+sharp_gap | spread | 6-11 | 35.3 | 48.5 | -13.2 | -5.91 | -34.8 |  |  | keep collecting (17/30) |
| follow_move+money_level | spread | 11-19 | 36.7 | 49.6 | -13.0 | -8.75 | -29.2 |  |  | DROP: below break-even |
| follow_move+pin_value | spread | 2-6 | 25.0 | 50.0 | -25.0 | -4.26 | -53.2 |  |  | keep collecting (8/30) |
| consensus_gap+follow_move | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| follow_move+money_moving | spread | 10-16 | 38.5 | 49.8 | -11.3 | -6.62 | -25.5 |  |  | keep collecting (26/30) |
| follow_move+sharp_gap | spread | 10-16 | 38.5 | 49.8 | -11.3 | -6.62 | -25.5 |  |  | keep collecting (26/30) |
| follow_move+rlm_ratio | spread | 2-3 | 40.0 | 49.4 | -9.4 | -1.15 | -23.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+rlm_ratio | spread | 1-3 | 25.0 | 48.6 | -23.6 | -2.06 | -51.4 |  |  | keep collecting (4/30) |
| money_moving+rlm_ratio | spread | 2-3 | 40.0 | 49.4 | -9.4 | -1.15 | -23.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 2-3 | 40.0 | 49.4 | -9.4 | -1.15 | -23.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+pin_value | spread | 0-2 | 0.0 | 52.8 | -52.8 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| follow_move+pin_rlm | spread | 0-1 | 0.0 | 47.2 | -47.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+rlm_ratio | spread | 0-1 | 0.0 | 47.2 | -47.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+money_moving | total | 27-15 | 64.3 | 54.6 | 9.7 | +9.57 | 22.8 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | total | 4-6 | 40.0 | 61.1 | -21.1 | -2.44 | -24.4 |  |  | keep collecting (10/30) |
| money_level+sharp_gap | total | 27-14 | 65.9 | 54.4 | 11.4 | +10.57 | 25.8 |  |  | PROMOTE: beats break-even and its own base rate |
| money_moving+pin_value | total | 5-8 | 38.5 | 46.8 | -8.3 | -3.49 | -26.9 |  |  | keep collecting (13/30) |
| money_moving+sharp_gap | total | 39-29 | 57.4 | 48.4 | 9.0 | +6.49 | 9.5 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 5-7 | 41.7 | 47.7 | -6.0 | -2.49 | -20.8 |  |  | keep collecting (12/30) |
| follow_move+money_level | total | 23-14 | 62.2 | 54.9 | 7.3 | +6.97 | 18.8 |  |  | no edge shown yet |
| follow_move+money_moving | total | 28-21 | 57.1 | 48.6 | 8.6 | +4.52 | 9.2 |  |  | no edge shown yet |
| follow_move+sharp_gap | total | 29-21 | 58.0 | 48.3 | 9.7 | +5.47 | 10.9 |  |  | no edge shown yet |
| consensus_gap+money_level | total | 2-0 | 100.0 | 63.9 | 36.1 | +1.78 | 88.9 |  |  | keep collecting (2/30) |
| consensus_gap+pin_value | total | 4-3 | 57.1 | 48.0 | 9.1 | +0.6 | 8.5 |  |  | keep collecting (7/30) |
| consensus_gap+money_moving | total | 5-0 | 100.0 | 52.8 | 47.2 | +4.43 | 88.6 |  |  | keep collecting (5/30) |
| consensus_gap+pin_rlm | total | 2-0 | 100.0 | 36.1 | 63.9 | +1.82 | 90.9 |  |  | keep collecting (2/30) |
| consensus_gap+sharp_gap | total | 5-0 | 100.0 | 52.8 | 47.2 | +4.43 | 88.6 |  |  | keep collecting (5/30) |
| money_moving+pin_rlm | total | 8-6 | 57.1 | 42.1 | 15.1 | +1.23 | 8.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | total | 4-2 | 66.7 | 40.7 | 25.9 | +1.6 | 26.6 |  |  | keep collecting (6/30) |
| pin_rlm+sharp_gap | total | 8-6 | 57.1 | 42.1 | 15.1 | +1.23 | 8.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+pin_rlm | total | 5-6 | 45.5 | 41.2 | 4.3 | -1.45 | -13.2 |  |  | keep collecting (11/30) |
| follow_move+rlm_ratio | total | 13-12 | 52.0 | 42.8 | 9.2 | -0.04 | -0.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 4-2 | 66.7 | 45.4 | 21.3 | +1.6 | 26.6 |  |  | keep collecting (6/30) |
| money_level+rlm_ratio | total | 7-4 | 63.6 | 48.7 | 14.9 | +2.38 | 21.6 |  |  | keep collecting (11/30) |
| money_moving+rlm_ratio | total | 12-12 | 50.0 | 43.1 | 6.9 | -0.99 | -4.1 |  |  | keep collecting (24/30) |
| pin_rlm+rlm_ratio | total | 5-6 | 45.5 | 41.2 | 4.3 | -1.45 | -13.2 |  |  | keep collecting (11/30) |
| rlm_ratio+sharp_gap | total | 13-12 | 52.0 | 42.8 | 9.2 | -0.04 | -0.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | total | 3-0 | 100.0 | 54.6 | 45.4 | +2.65 | 88.3 |  |  | keep collecting (3/30) |
| consensus_gap+rlm_ratio | total | 1-0 | 100.0 | 36.1 | 63.9 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| follow_move+pin_value | total | 2-5 | 28.6 | 48.0 | -19.4 | -3.18 | -45.5 |  |  | keep collecting (7/30) |
| pin_value+rlm_ratio | total | 1-2 | 33.3 | 36.1 | -2.8 | -1.09 | -36.4 |  |  | keep collecting (3/30) |

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
| pin_rlm | both | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | both | 391-352 | 52.6 | 52.3 | 0.3 | -57.44 | -7.7 | 0.22 | 42.5 | no edge shown yet |
| rlm_ratio | both | 21-15 | 58.3 | 37.6 | 20.7 | +14.22 | 39.5 | 0.25 | 50.0 | no edge shown yet |
| money_level | both | 136-85 | 61.5 | 59.1 | 2.4 | -9.23 | -4.2 | 0.08 | 40.3 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 119-90 | 56.9 | 49.2 | 7.7 | +24.05 | 11.5 | 0.3 | 42.1 | no edge shown yet |
| money_moving | both | 84-57 | 59.6 | 51.4 | 8.2 | +11.9 | 8.4 | 0.05 | 41.8 | PROMOTE: beats break-even and its own base rate |
| pin_value | both | 49-48 | 50.5 | 48.2 | 2.3 | -4.43 | -4.6 | 0.1 | 38.1 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.7 | -31.7 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 192-250 | 43.4 | 46.6 | -3.2 | -41.56 | -9.4 | 0.39 | 45.2 | DROP: below break-even |
| consensus_gap+money_level | both | 25-23 | 52.1 | 63.5 | -11.4 | -10.09 | -21.0 | 0.31 | 47.9 | no edge shown yet |
| consensus_gap+money_moving | both | 15-21 | 41.7 | 45.0 | -3.3 | -5.7 | -15.8 | 0.08 | 36.1 | no edge shown yet |
| consensus_gap+pin_value | both | 19-28 | 40.4 | 46.2 | -5.8 | -11.54 | -24.5 | 0.39 | 48.9 | DROP: below break-even |
| follow_move+rlm_ratio | both | 21-15 | 58.3 | 37.6 | 20.7 | +14.22 | 39.5 | 0.25 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 58-32 | 64.4 | 50.3 | 14.1 | +17.36 | 19.3 | 0.42 | 47.8 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 54-29 | 65.1 | 58.0 | 7.0 | +4.17 | 5.0 | -0.07 | 47.0 | PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | both | 11-9 | 55.0 | 50.1 | 4.9 | +0.81 | 4.0 | 0.4 | 45.0 | keep collecting (20/30) |
| money_moving+pin_value | both | 8-5 | 61.5 | 50.1 | 11.4 | +2.04 | 15.7 | 0.31 | 38.5 | keep collecting (13/30) |
| rlm_ratio+sharp_gap | both | 21-15 | 58.3 | 37.6 | 20.7 | +14.22 | 39.5 | 0.25 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 82-46 | 64.1 | 56.1 | 7.9 | +8.25 | 6.4 | 0.32 | 43.8 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 53-33 | 61.6 | 49.8 | 11.9 | +14.54 | 16.9 | 0.23 | 44.2 | PROMOTE: beats break-even and its own base rate |
| pin_value+sharp_gap | both | 13-8 | 61.9 | 49.0 | 12.9 | +3.66 | 17.4 | -0.18 | 33.3 | keep collecting (21/30) |
| consensus_gap+follow_move | both | 29-36 | 44.6 | 50.4 | -5.8 | -12.71 | -19.6 | 0.92 | 58.5 | no edge shown yet |
| follow_move+pin_value | both | 20-17 | 54.1 | 48.5 | 5.5 | +0.41 | 1.1 | -0.12 | 29.7 | no edge shown yet |
| consensus_gap+sharp_gap | both | 22-38 | 36.7 | 45.5 | -8.8 | -6.9 | -11.5 | 0.7 | 46.7 | DROP: below break-even |
| follow_move+money_level | both | 74-40 | 64.9 | 59.3 | 5.6 | -4.69 | -4.1 | 0.22 | 43.9 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 10-6 | 62.5 | 42.4 | 20.1 | +3.79 | 23.7 | 1.01 | 56.2 | keep collecting (16/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 44.7 | 5.3 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 40-20 | 66.7 | 53.5 | 13.1 | +9.95 | 16.6 | 0.36 | 55.0 | PROMOTE: beats break-even and its own base rate |
| money_moving+rlm_ratio | both | 9-5 | 64.3 | 42.1 | 22.2 | +6.16 | 44.0 | 0.1 | 50.0 | keep collecting (14/30) |
| consensus_gap+rlm_ratio | both | 2-4 | 33.3 | 35.1 | -1.8 | -1.77 | -29.5 | 0.92 | 66.7 | keep collecting (6/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 26.6 | 23.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 26.6 | 23.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | both | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 52.4 | -52.4 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 52.1 | -52.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | moneyline | 163-108 | 60.1 | 57.2 | 3.0 | -22.46 | -8.3 | 0.29 | 47.6 | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 109-124 | 46.8 | 49.4 | -2.6 | -23.61 | -10.1 | -0.06 | 32.2 | DROP: below break-even |
| follow_move | total | 119-120 | 49.8 | 49.8 | 0.0 | -11.37 | -4.8 | 0.42 | 46.9 | no edge shown yet |
| rlm_ratio | moneyline | 11-9 | 55.0 | 26.6 | 28.4 | +10.93 | 54.6 | 0.35 | 60.0 | keep collecting (20/30) |
| rlm_ratio | spread | 3-2 | 60.0 | 51.7 | 8.3 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 7-4 | 63.6 | 51.3 | 12.3 | +2.45 | 22.3 | 0.45 | 54.5 | keep collecting (11/30) |
| money_level | moneyline | 77-31 | 71.3 | 69.5 | 1.8 | -8.79 | -8.1 | 0.01 | 45.4 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 16-16 | 50.0 | 49.1 | 0.9 | -1.6 | -5.0 | 0.81 | 46.9 | no edge shown yet |
| money_level | total | 43-38 | 53.1 | 49.3 | 3.8 | +1.16 | 1.4 | -0.11 | 30.9 | no edge shown yet |
| sharp_gap | moneyline | 51-45 | 53.1 | 48.1 | 5.1 | +7.28 | 7.6 | 0.3 | 47.9 | no edge shown yet |
| sharp_gap | spread | 19-14 | 57.6 | 49.7 | 7.8 | +3.09 | 9.4 | 0.61 | 36.4 | no edge shown yet |
| sharp_gap | total | 49-31 | 61.3 | 50.4 | 10.8 | +13.67 | 17.1 | 0.16 | 37.5 | PROMOTE: beats break-even and its own base rate |
| money_moving | moneyline | 33-32 | 50.8 | 53.2 | -2.5 | -9.28 | -14.3 | -0.11 | 49.2 | no edge shown yet |
| money_moving | spread | 17-4 | 81.0 | 49.1 | 31.9 | +11.27 | 53.7 | 0.14 | 38.1 | keep collecting (21/30) |
| money_moving | total | 34-21 | 61.8 | 50.0 | 11.8 | +9.91 | 18.0 | 0.22 | 34.5 | no edge shown yet |
| pin_value | moneyline | 2-6 | 25.0 | 32.5 | -7.5 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| pin_value | spread | 24-20 | 54.5 | 49.4 | 5.2 | +1.16 | 2.6 | 0.25 | 38.6 | no edge shown yet |
| pin_value | total | 23-22 | 51.1 | 49.9 | 1.2 | -1.28 | -2.9 | -0.02 | 35.6 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.8 | -19.5 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 79-141 | 35.9 | 43.8 | -7.9 | -32.67 | -14.8 | 0.09 | 42.3 | DROP: below break-even |
| consensus_gap | spread | 57-53 | 51.8 | 49.1 | 2.7 | -3.09 | -2.8 | 0.45 | 42.7 | no edge shown yet |
| consensus_gap | total | 56-56 | 50.0 | 49.6 | 0.4 | -5.8 | -5.2 | 0.94 | 53.6 | no edge shown yet |
| money_level+sharp_gap | moneyline | 39-14 | 73.6 | 65.4 | 8.1 | +1.18 | 2.2 | 0.28 | 54.7 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+follow_move | moneyline | 10-19 | 34.5 | 52.4 | -17.9 | -12.52 | -43.2 | 0.51 | 62.1 | keep collecting (29/30) |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 32.5 | -7.5 | -4.31 | -53.8 | -0.08 | 50.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.2 | -8.9 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| money_level+money_moving | moneyline | 23-11 | 67.6 | 70.6 | -3.0 | -6.14 | -18.1 | -0.5 | 52.9 | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+sharp_gap | moneyline | 14-29 | 32.6 | 44.0 | -11.5 | -4.86 | -11.3 | 0.65 | 48.8 | DROP: below break-even |
| follow_move+money_level | moneyline | 46-14 | 76.7 | 68.7 | 8.0 | -4.21 | -7.0 | 0.04 | 46.7 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 19-7 | 73.1 | 59.0 | 14.1 | +3.75 | 14.4 | 0.21 | 65.4 | keep collecting (26/30) |
| consensus_gap+money_level | moneyline | 18-15 | 54.5 | 70.6 | -16.0 | -8.16 | -24.7 | 0.02 | 48.5 | INVERT candidate: wrong well beyond its base rate |
| follow_move+sharp_gap | moneyline | 29-13 | 69.0 | 51.1 | 17.9 | +9.96 | 23.7 | 0.3 | 54.8 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 19-18 | 51.4 | 49.4 | 2.0 | -1.31 | -3.6 | 0.17 | 54.1 | no edge shown yet |
| consensus_gap+money_moving | moneyline | 7-20 | 25.9 | 43.9 | -18.0 | -11.63 | -43.1 | 0.15 | 44.4 | keep collecting (27/30) |
| follow_move+rlm_ratio | moneyline | 11-9 | 55.0 | 26.6 | 28.4 | +10.93 | 54.6 | 0.35 | 60.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 11-9 | 55.0 | 26.6 | 28.4 | +10.93 | 54.6 | 0.35 | 60.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 26.6 | -1.6 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | moneyline | 3-2 | 60.0 | 26.6 | 33.4 | +3.58 | 71.6 | 0.08 | 60.0 | keep collecting (5/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-1 | 50.0 | 26.6 | 23.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-1 | 50.0 | 26.6 | 23.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | moneyline | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| money_level+rlm_ratio | moneyline | 3-3 | 50.0 | 26.6 | 23.4 | +0.23 | 3.8 | 1.7 | 83.3 | keep collecting (6/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 4-5 | 44.4 | 47.2 | -2.7 | -1.59 | -17.7 | 1.67 | 66.7 | keep collecting (9/30) |
| consensus_gap+money_moving | spread | 4-0 | 100.0 | 47.2 | 52.8 | +3.41 | 85.2 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_value | spread | 10-8 | 55.6 | 48.4 | 7.1 | +0.6 | 3.3 | 0.5 | 50.0 | keep collecting (18/30) |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.7 | 8.3 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 48.6 | 13.9 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 9-4 | 69.2 | 48.5 | 20.8 | +4.21 | 32.4 | 0.77 | 61.5 | keep collecting (13/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.8 | -5.9 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.4 | 10.6 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 51.7 | 8.3 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 13-11 | 54.2 | 49.1 | 5.1 | +0.71 | 3.0 | 0.96 | 41.7 | keep collecting (24/30) |
| money_moving+sharp_gap | spread | 9-3 | 75.0 | 49.1 | 25.9 | +5.13 | 42.7 | 0.42 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.1 | 17.6 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-9 | 50.0 | 48.1 | 1.9 | -1.2 | -6.7 | 0.89 | 44.4 | keep collecting (18/30) |
| consensus_gap+sharp_gap | spread | 4-3 | 57.1 | 47.2 | 10.0 | +0.41 | 5.8 | 2.14 | 71.4 | keep collecting (7/30) |
| follow_move+money_level | spread | 11-8 | 57.9 | 48.4 | 9.5 | +2.04 | 10.7 | 0.63 | 42.1 | keep collecting (19/30) |
| follow_move+pin_value | spread | 12-7 | 63.2 | 48.7 | 14.5 | +3.45 | 18.2 | 0.26 | 31.6 | keep collecting (19/30) |
| follow_move+money_moving | spread | 9-1 | 90.0 | 47.7 | 42.3 | +7.22 | 72.2 | 0.2 | 40.0 | keep collecting (10/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 52.8 | 13.8 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 22-14 | 61.1 | 49.5 | 11.6 | +6.11 | 17.0 | 0.03 | 36.1 | no edge shown yet |
| money_level+sharp_gap | total | 30-21 | 58.8 | 49.8 | 9.0 | +6.36 | 12.5 | 0.06 | 33.3 | no edge shown yet |
| money_moving+sharp_gap | total | 25-12 | 67.6 | 50.4 | 17.2 | +10.73 | 29.0 | 0.24 | 35.1 | PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | total | 8-5 | 61.5 | 50.8 | 10.7 | +2.23 | 17.2 | 0.23 | 30.8 | keep collecting (13/30) |
| money_moving+pin_value | total | 5-3 | 62.5 | 50.5 | 12.0 | +1.47 | 18.3 | 0.12 | 25.0 | keep collecting (8/30) |
| pin_value+sharp_gap | total | 11-6 | 64.7 | 50.4 | 14.3 | +3.92 | 23.1 | -0.06 | 29.4 | keep collecting (17/30) |
| follow_move+money_level | total | 17-18 | 48.6 | 49.2 | -0.7 | -2.52 | -7.2 | 0.31 | 40.0 | no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.6 | -2.9 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 7-4 | 63.6 | 51.3 | 12.3 | +2.45 | 22.3 | 0.45 | 54.5 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 19-13 | 59.4 | 50.1 | 9.2 | +4.32 | 13.5 | 0.47 | 43.8 | no edge shown yet |
| money_level+rlm_ratio | total | 5-2 | 71.4 | 51.5 | 20.0 | +2.63 | 37.6 | 0.86 | 57.1 | keep collecting (7/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 50.7 | 16.0 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 7-4 | 63.6 | 51.3 | 12.3 | +2.45 | 22.3 | 0.45 | 54.5 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 12-12 | 50.0 | 50.0 | 0.0 | -1.03 | -4.3 | 0.58 | 50.0 | keep collecting (24/30) |
| consensus_gap+money_level | total | 3-3 | 50.0 | 49.3 | 0.7 | -0.34 | -5.7 | -0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 48.8 | 31.2 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 49.5 | -16.2 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 4-6 | 40.0 | 50.4 | -10.4 | -2.44 | -24.4 | -0.1 | 20.0 | keep collecting (10/30) |
| money_moving+rlm_ratio | total | 4-3 | 57.1 | 50.9 | 6.3 | +0.72 | 10.3 | 0.43 | 57.1 | keep collecting (7/30) |
| consensus_gap+follow_move | total | 10-8 | 55.6 | 49.5 | 6.0 | +1.02 | 5.6 | 1.61 | 66.7 | keep collecting (18/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 52.1 | -52.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 52.1 | -52.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 1-1 | 50.0 | 52.1 | -2.1 | -0.09 | -4.5 | 0.5 | 50.0 | keep collecting (2/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 113-123 | 47.9 | 42.6 | 5.3 | +29.62 | 12.6 |  |  | no edge shown yet |
| follow_move | both | 738-655 | 53.0 | 52.1 | 0.9 | -79.57 | -5.7 |  |  | no edge shown yet |
| rlm_ratio | both | 171-183 | 48.3 | 44.8 | 3.5 | +13.68 | 3.9 |  |  | DROP: below break-even |
| money_level | both | 918-689 | 57.1 | 55.3 | 1.8 | -66.84 | -4.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 718-833 | 46.3 | 47.4 | -1.1 | -94.17 | -6.1 |  |  | DROP: below break-even |
| money_moving | both | 714-839 | 46.0 | 47.5 | -1.6 | -109.72 | -7.1 |  |  | DROP: below break-even |
| pin_value | both | 292-313 | 48.3 | 47.4 | 0.9 | -4.4 | -0.7 |  |  | DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 50.9 | 15.7 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 281-413 | 40.5 | 46.0 | -5.5 | -85.88 | -12.4 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 107-120 | 47.1 | 50.0 | -2.8 | -22.41 | -9.9 |  |  | DROP: below break-even |
| consensus_gap+money_moving | both | 122-223 | 35.4 | 42.9 | -7.5 | -29.38 | -8.5 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 20-35 | 36.4 | 36.7 | -0.4 | +11.38 | 20.7 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 112-138 | 44.8 | 44.6 | 0.2 | -5.66 | -2.3 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | both | 21-40 | 34.4 | 39.0 | -4.5 | -2.11 | -3.5 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 123-227 | 35.1 | 42.5 | -7.4 | -30.21 | -8.6 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 398-427 | 48.2 | 49.4 | -1.1 | -58.44 | -7.1 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 89-85 | 51.1 | 44.8 | 6.4 | +15.23 | 8.8 |  |  | no edge shown yet |
| follow_move+pin_value | both | 101-102 | 49.8 | 48.3 | 1.4 | -11.92 | -5.9 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 171-183 | 48.3 | 44.8 | 3.5 | +13.68 | 3.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 402-422 | 48.8 | 49.3 | -0.5 | -48.38 | -5.9 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 110-122 | 47.4 | 42.5 | 4.9 | +27.88 | 12.0 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 125-159 | 44.0 | 46.4 | -2.4 | -15.92 | -5.6 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 166-179 | 48.1 | 44.8 | 3.3 | +12.99 | 3.8 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 691-808 | 46.1 | 47.4 | -1.3 | -93.65 | -6.2 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 32-31 | 50.8 | 45.5 | 5.3 | +15.34 | 24.3 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 89-85 | 51.1 | 44.8 | 6.4 | +15.23 | 8.8 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 113-123 | 47.9 | 42.6 | 5.3 | +29.62 | 12.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 29-24 | 54.7 | 48.5 | 6.2 | +2.61 | 4.9 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 127-158 | 44.6 | 46.4 | -1.9 | -13.16 | -4.6 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 171-183 | 48.3 | 44.8 | 3.5 | +13.68 | 3.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+money_moving | both | 508-462 | 52.4 | 51.9 | 0.4 | -41.52 | -4.3 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 507-456 | 52.6 | 51.8 | 0.8 | -31.85 | -3.3 |  |  | no edge shown yet |
| follow_move+money_level | both | 497-359 | 58.1 | 56.3 | 1.8 | -47.59 | -5.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 88-70 | 55.7 | 48.8 | 6.9 | +15.38 | 9.7 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 165-146 | 53.1 | 56.6 | -3.6 | -26.64 | -8.6 |  |  | no edge shown yet |
| money_level+pin_value | both | 135-141 | 48.9 | 49.1 | -0.2 | -23.75 | -8.6 |  |  | no edge shown yet |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | both | 53-36 | 59.6 | 47.4 | 12.1 | +16.79 | 18.9 |  |  | no edge shown yet |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 52.1 | 47.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 29-60 | 32.6 | 28.2 | 4.4 | +15.78 | 17.7 |  |  | DROP: below break-even |
| pin_rlm | spread | 19-20 | 48.7 | 51.1 | -2.4 | -2.75 | -7.1 |  |  | no edge shown yet |
| pin_rlm | total | 65-43 | 60.2 | 51.3 | 8.9 | +16.6 | 15.4 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move | moneyline | 271-172 | 61.2 | 57.2 | 3.9 | -21.43 | -4.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 208-224 | 48.1 | 49.3 | -1.1 | -35.52 | -8.2 |  |  | DROP: below break-even |
| follow_move | total | 259-259 | 50.0 | 50.0 | -0.0 | -22.61 | -4.4 |  |  | no edge shown yet |
| rlm_ratio | moneyline | 31-71 | 30.4 | 29.8 | 0.6 | -2.38 | -2.3 |  |  | DROP: below break-even |
| rlm_ratio | spread | 35-37 | 48.6 | 50.0 | -1.4 | -5.12 | -7.1 |  |  | no edge shown yet |
| rlm_ratio | total | 105-75 | 58.3 | 51.1 | 7.2 | +21.17 | 11.8 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level | moneyline | 357-130 | 73.3 | 69.1 | 4.2 | -15.83 | -3.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 265-283 | 48.4 | 49.0 | -0.7 | -44.16 | -8.1 |  |  | DROP: below break-even |
| money_level | total | 296-276 | 51.7 | 49.6 | 2.2 | -6.86 | -1.2 |  |  | no edge shown yet |
| sharp_gap | moneyline | 161-287 | 35.9 | 40.9 | -5.0 | -54.1 | -12.1 |  |  | DROP: below break-even |
| sharp_gap | spread | 273-268 | 50.5 | 49.5 | 1.0 | -21.47 | -4.0 |  |  | no edge shown yet |
| sharp_gap | total | 284-278 | 50.5 | 50.4 | 0.1 | -18.6 | -3.3 |  |  | no edge shown yet |
| money_moving | moneyline | 166-280 | 37.2 | 41.6 | -4.4 | -48.26 | -10.8 |  |  | DROP: below break-even |
| money_moving | spread | 270-271 | 49.9 | 49.4 | 0.5 | -27.34 | -5.1 |  |  | no edge shown yet |
| money_moving | total | 278-288 | 49.1 | 50.4 | -1.3 | -34.11 | -6.0 |  |  | DROP: below break-even |
| pin_value | moneyline | 16-49 | 24.6 | 28.8 | -4.2 | +14.5 | 22.3 |  |  | DROP: below break-even |
| pin_value | spread | 134-127 | 51.3 | 49.5 | 1.8 | -9.66 | -3.7 |  |  | no edge shown yet |
| pin_value | total | 142-137 | 50.9 | 49.7 | 1.2 | -9.25 | -3.3 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.8 | 47.2 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 114-249 | 31.4 | 43.2 | -11.8 | -67.46 | -18.6 |  |  | DROP: below break-even |
| consensus_gap | spread | 78-70 | 52.7 | 49.0 | 3.7 | -3.39 | -2.3 |  |  | no edge shown yet |
| consensus_gap | total | 89-94 | 48.6 | 48.9 | -0.3 | -15.03 | -8.2 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 114-69 | 62.3 | 62.7 | -0.4 | -5.37 | -2.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 109-68 | 61.6 | 62.3 | -0.7 | -4.38 | -2.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 150-269 | 35.8 | 40.7 | -4.9 | -45.87 | -10.9 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 42-62 | 40.4 | 51.8 | -11.4 | -20.83 | -20.0 |  |  | DROP: below break-even |
| consensus_gap+money_level | moneyline | 74-54 | 57.8 | 68.3 | -10.5 | -13.74 | -10.7 |  |  | no edge shown yet |
| consensus_gap+money_moving | moneyline | 41-142 | 22.4 | 37.6 | -15.2 | -18.73 | -10.2 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+money_level | moneyline | 216-67 | 76.3 | 70.7 | 5.6 | -10.22 | -3.6 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 85-97 | 46.7 | 48.2 | -1.5 | -12.57 | -6.9 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 42-147 | 22.2 | 37.0 | -14.8 | -20.57 | -10.9 |  |  | DROP: below break-even |
| follow_move+sharp_gap | moneyline | 83-96 | 46.4 | 47.5 | -1.1 | -12.22 | -6.8 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | moneyline | 10-25 | 28.6 | 29.3 | -0.7 | +12.65 | 36.1 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 4-28 | 12.5 | 29.5 | -17.0 | -5.04 | -15.7 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_rlm | moneyline | 19-32 | 37.3 | 29.4 | 7.9 | +3.95 | 7.7 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 31-71 | 30.4 | 29.8 | 0.6 | -2.38 | -2.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_rlm | moneyline | 29-59 | 33.0 | 28.2 | 4.7 | +16.78 | 19.1 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 31-68 | 31.3 | 29.9 | 1.4 | +0.62 | 0.6 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 19-32 | 37.3 | 29.4 | 7.9 | +3.95 | 7.7 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 29-60 | 32.6 | 28.2 | 4.4 | +15.78 | 17.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 31-71 | 30.4 | 29.8 | 0.6 | -2.38 | -2.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 13-41 | 24.1 | 29.2 | -5.1 | +5.38 | 10.0 |  |  | DROP: below break-even |
| money_moving+pin_value | moneyline | 8-30 | 21.1 | 26.6 | -5.6 | +10.07 | 26.5 |  |  | DROP: below break-even |
| pin_rlm+pin_value | moneyline | 5-9 | 35.7 | 26.6 | 9.1 | +13.07 | 93.4 |  |  | keep collecting (14/30) |
| pin_value+sharp_gap | moneyline | 8-31 | 20.5 | 26.6 | -6.1 | +9.07 | 23.3 |  |  | DROP: below break-even |
| money_level+pin_rlm | moneyline | 9-8 | 52.9 | 32.1 | 20.8 | +4.65 | 27.3 |  |  | keep collecting (17/30) |
| money_level+rlm_ratio | moneyline | 12-9 | 57.1 | 37.7 | 19.4 | +7.12 | 33.9 |  |  | keep collecting (21/30) |
| money_level+pin_value | moneyline | 3-1 | 75.0 | 61.7 | 13.3 | +0.31 | 7.8 |  |  | keep collecting (4/30) |
| follow_move+pin_value | moneyline | 1-7 | 12.5 | 26.6 | -14.1 | -5.48 | -68.5 |  |  | keep collecting (8/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 26.6 | -1.6 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 31-26 | 54.4 | 48.2 | 6.2 | +0.4 | 0.7 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 41-38 | 51.9 | 48.7 | 3.2 | -3.02 | -3.8 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | -0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 52-42 | 55.3 | 48.9 | 6.5 | +2.27 | 2.4 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.33 | -38.9 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | spread | 40-38 | 51.3 | 49.0 | 2.3 | -3.91 | -5.0 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 133-141 | 48.5 | 48.9 | -0.4 | -20.98 | -7.7 |  |  | no edge shown yet |
| follow_move+pin_rlm | spread | 15-16 | 48.4 | 50.8 | -2.4 | -2.37 | -7.7 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 50-45 | 52.6 | 48.8 | 3.9 | -1.38 | -1.5 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 35-37 | 48.6 | 50.0 | -1.4 | -5.12 | -7.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 134-140 | 48.9 | 49.0 | -0.1 | -18.85 | -6.9 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 17-20 | 45.9 | 51.0 | -5.0 | -4.58 | -12.4 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 64-68 | 48.5 | 49.0 | -0.5 | -12.69 | -9.6 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 33-36 | 47.8 | 49.9 | -2.1 | -6.05 | -8.8 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 265-263 | 50.2 | 49.4 | 0.7 | -23.85 | -4.5 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 6-9 | 40.0 | 50.6 | -10.6 | -3.79 | -25.3 |  |  | keep collecting (15/30) |
| pin_rlm+rlm_ratio | spread | 15-16 | 48.4 | 50.8 | -2.4 | -2.37 | -7.7 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 19-20 | 48.7 | 51.1 | -2.4 | -2.75 | -7.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 5-6 | 45.5 | 49.2 | -3.8 | -1.72 | -15.6 |  |  | keep collecting (11/30) |
| pin_value+sharp_gap | spread | 64-68 | 48.5 | 49.1 | -0.7 | -12.75 | -9.7 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 35-37 | 48.6 | 50.0 | -1.4 | -5.12 | -7.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 129-143 | 47.4 | 48.6 | -1.2 | -26.66 | -9.8 |  |  | DROP: below break-even |
| money_level+rlm_ratio | spread | 18-22 | 45.0 | 49.4 | -4.4 | -5.76 | -14.4 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 207-209 | 49.8 | 49.0 | 0.7 | -22.54 | -5.4 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 51-43 | 54.3 | 48.5 | 5.8 | +0.67 | 0.7 |  |  | no edge shown yet |
| money_level+money_moving | spread | 206-210 | 49.5 | 49.0 | 0.5 | -24.45 | -5.9 |  |  | no edge shown yet |
| money_level+pin_value | spread | 70-75 | 48.3 | 48.8 | -0.5 | -14.54 | -10.0 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 9-8 | 52.9 | 50.2 | 2.8 | +0.01 | 0.1 |  |  | keep collecting (17/30) |
| money_level+money_moving | total | 188-183 | 50.7 | 50.0 | 0.7 | -11.7 | -3.2 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 191-179 | 51.6 | 50.0 | 1.6 | -4.94 | -1.3 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 276-276 | 50.0 | 50.4 | -0.4 | -23.93 | -4.3 |  |  | no edge shown yet |
| consensus_gap+money_level | total | 40-49 | 44.9 | 48.4 | -3.5 | -13.56 | -15.2 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 47-55 | 46.1 | 48.9 | -2.8 | -13.31 | -13.0 |  |  | no edge shown yet |
| follow_move+money_moving | total | 180-189 | 48.8 | 50.3 | -1.5 | -24.88 | -6.7 |  |  | no edge shown yet |
| follow_move+sharp_gap | total | 185-186 | 49.9 | 50.3 | -0.4 | -17.31 | -4.7 |  |  | no edge shown yet |
| money_level+pin_value | total | 62-65 | 48.8 | 49.0 | -0.2 | -9.52 | -7.5 |  |  | no edge shown yet |
| follow_move+money_level | total | 152-149 | 50.5 | 49.6 | 0.9 | -10.71 | -3.6 |  |  | no edge shown yet |
| follow_move+pin_value | total | 50-50 | 50.0 | 49.6 | 0.4 | -5.06 | -5.1 |  |  | no edge shown yet |
| money_moving+pin_value | total | 53-61 | 46.5 | 50.0 | -3.5 | -13.3 | -11.7 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 55-59 | 48.2 | 50.1 | -1.8 | -9.48 | -8.3 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 40-43 | 48.2 | 49.0 | -0.8 | -7.63 | -9.2 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 41-42 | 49.4 | 49.0 | 0.4 | -5.72 | -6.9 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 34-32 | 51.5 | 48.6 | 2.9 | -1.99 | -3.0 |  |  | no edge shown yet |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pin_rlm | total | 7-7 | 50.0 | 49.7 | 0.3 | -0.79 | -5.6 |  |  | keep collecting (14/30) |
| consensus_gap+rlm_ratio | total | 15-8 | 65.2 | 49.2 | 16.0 | +5.26 | 22.9 |  |  | keep collecting (23/30) |
| follow_move+pin_rlm | total | 55-37 | 59.8 | 51.3 | 8.5 | +13.65 | 14.8 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 105-75 | 58.3 | 51.1 | 7.2 | +21.17 | 11.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 35-20 | 63.6 | 51.3 | 12.3 | +12.13 | 22.1 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 58-39 | 59.8 | 50.9 | 8.9 | +14.03 | 14.5 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 64-43 | 59.8 | 51.3 | 8.5 | +15.69 | 14.7 |  |  | PROMOTE: beats break-even and its own base rate |
| money_moving+rlm_ratio | total | 102-75 | 57.6 | 51.1 | 6.5 | +18.42 | 10.4 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 21-13 | 61.8 | 51.0 | 10.8 | +6.06 | 17.8 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 55-37 | 59.8 | 51.3 | 8.5 | +13.65 | 14.8 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 65-43 | 60.2 | 51.3 | 8.9 | +16.6 | 15.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 23-15 | 60.5 | 50.6 | 9.9 | +5.8 | 15.3 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 105-75 | 58.3 | 51.1 | 7.2 | +21.17 | 11.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 52.1 | 47.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_rlm | close | 1-3k bets | 68-75 | 47.6 | 4.3 | 15.0 |  |
| pin_rlm | close | 3k+ bets | 24-27 | 47.1 | 5.4 | 7.1 |  |
| pin_rlm | close | <1k bets | 21-21 | 50.0 | 8.7 | 11.0 |  |
| pin_rlm | close | pin $1-2k | 49-49 | 50.0 | 5.6 | 17.3 |  |
| pin_rlm | close | pin $2k+ | 27-56 | 32.5 | -2.7 | -14.7 |  |
| pin_rlm | close | pin limit <$1k | 37-18 | 67.3 | 16.8 | 45.2 |  |
| follow_move | close | 1-3k bets | 465-400 | 53.8 | 2.1 | -3.8 |  |
| follow_move | close | 3k+ bets | 158-150 | 51.3 | -1.2 | -6.9 |  |
| follow_move | close | <1k bets | 115-105 | 52.3 | -0.9 | -11.5 |  |
| follow_move | close | pin $1-2k | 212-239 | 47.0 | -4.1 | -11.9 |  |
| follow_move | close | pin $2k+ | 173-148 | 53.9 | 1.6 | -6.0 |  |
| follow_move | close | pin limit <$1k | 97-86 | 53.0 | 2.6 | 1.2 |  |
| rlm_ratio | close | 1-3k bets | 108-127 | 46.0 | 0.8 | -0.3 |  |
| rlm_ratio | close | 3k+ bets | 39-31 | 55.7 | 11.2 | 21.0 |  |
| rlm_ratio | close | <1k bets | 24-25 | 49.0 | 5.6 | -0.8 |  |
| rlm_ratio | close | pin $1-2k | 57-55 | 50.9 | 4.1 | 8.3 |  |
| rlm_ratio | close | pin $2k+ | 29-44 | 39.7 | 1.9 | -10.1 |  |
| rlm_ratio | close | pin limit <$1k | 40-23 | 63.5 | 12.5 | 22.7 |  |
| money_level | close | 1-3k bets | 586-411 | 58.8 | 3.5 | -1.3 |  |
| money_level | close | 3k+ bets | 195-161 | 54.8 | -0.3 | -5.8 |  |
| money_level | close | <1k bets | 137-116 | 54.2 | -1.5 | -12.6 |  |
| money_level | close | pin $1-2k | 256-238 | 51.8 | -1.7 | -7.8 |  |
| money_level | close | pin $2k+ | 225-176 | 56.1 | -1.3 | -8.2 |  |
| money_level | close | pin limit <$1k | 104-104 | 50.0 | 0.3 | -4.8 |  |
| sharp_gap | close | 1-3k bets | 437-521 | 45.6 | -1.7 | -8.1 |  |
| sharp_gap | close | 3k+ bets | 172-177 | 49.3 | 2.3 | 6.2 |  |
| sharp_gap | close | <1k bets | 109-134 | 44.9 | -3.2 | -15.3 |  |
| sharp_gap | close | pin $1-2k | 228-252 | 47.5 | -1.3 | -4.5 |  |
| sharp_gap | close | pin $2k+ | 172-215 | 44.4 | -1.5 | -7.3 |  |
| sharp_gap | close | pin limit <$1k | 101-99 | 50.5 | 0.2 | 1.3 |  |
| money_moving | close | 1-3k bets | 436-524 | 45.4 | -2.2 | -9.2 |  |
| money_moving | close | 3k+ bets | 171-180 | 48.7 | 1.4 | 4.0 |  |
| money_moving | close | <1k bets | 107-134 | 44.4 | -3.2 | -14.2 |  |
| money_moving | close | pin $1-2k | 223-259 | 46.3 | -2.3 | -6.3 |  |
| money_moving | close | pin $2k+ | 174-212 | 45.1 | -0.8 | -6.2 |  |
| money_moving | close | pin limit <$1k | 98-104 | 48.5 | -1.6 | -2.4 |  |
| pin_value | close | 1-3k bets | 180-201 | 47.2 | -0.2 | -1.1 |  |
| pin_value | close | 3k+ bets | 60-68 | 46.9 | -0.8 | -6.8 |  |
| pin_value | close | <1k bets | 52-44 | 54.2 | 7.4 | 9.0 |  |
| pin_value | close | pin $1-2k | 135-160 | 45.8 | -2.1 | -5.8 |  |
| pin_value | close | pin $2k+ | 82-96 | 46.1 | 0.9 | -1.0 |  |
| pin_value | close | pin limit <$1k | 75-57 | 56.8 | 7.7 | 11.1 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.2 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.2 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 171-253 | 40.3 | -6.2 | -14.7 |  |
| consensus_gap | close | 3k+ bets | 72-85 | 45.9 | -0.6 | 6.8 |  |
| consensus_gap | close | <1k bets | 38-74 | 33.9 | -9.5 | -29.5 |  |
| consensus_gap | close | pin $1-2k | 87-111 | 43.9 | -4.3 | -5.5 |  |
| consensus_gap | close | pin $2k+ | 73-92 | 44.2 | -4.0 | -5.6 |  |
| consensus_gap | close | pin limit <$1k | 40-39 | 50.6 | 1.5 | 0.1 |  |
| consensus_gap+follow_move | close | 1-3k bets | 73-74 | 49.7 | -0.6 | -4.1 |  |
| consensus_gap+money_level | close | 1-3k bets | 111-84 | 56.9 | -0.3 | -0.3 |  |
| consensus_gap+money_moving | close | 1-3k bets | 77-138 | 35.8 | -7.6 | -11.6 |  |
| consensus_gap+pin_value | close | 1-3k bets | 69-94 | 42.3 | -2.6 | -7.1 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 77-141 | 35.3 | -7.6 | -12.7 |  |
| follow_move+money_level | close | 1-3k bets | 323-219 | 59.6 | 3.8 | -2.8 |  |
| follow_move+money_moving | close | 1-3k bets | 263-278 | 48.6 | -0.7 | -6.5 |  |
| follow_move+pin_value | close | 1-3k bets | 60-64 | 48.4 | 0.4 | -8.2 |  |
| follow_move+sharp_gap | close | 1-3k bets | 263-274 | 49.0 | -0.1 | -4.9 |  |
| money_level+money_moving | close | 1-3k bets | 319-282 | 53.1 | 1.1 | -2.4 |  |
| money_level+pin_value | close | 1-3k bets | 88-86 | 50.6 | 1.5 | -5.1 |  |
| money_level+sharp_gap | close | 1-3k bets | 316-279 | 53.1 | 1.4 | -1.6 |  |
| money_moving+pin_value | close | 1-3k bets | 82-106 | 43.6 | -3.2 | -7.3 |  |
| money_moving+sharp_gap | close | 1-3k bets | 422-505 | 45.5 | -1.9 | -8.1 |  |
| pin_value+sharp_gap | close | 1-3k bets | 84-108 | 43.8 | -2.9 | -7.3 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 14-23 | 37.8 | 0.6 | 23.3 |  |
| money_level+pin_rlm | close | 1-3k bets | 33-23 | 58.9 | 9.4 | 13.2 |  |
| pin_rlm+pin_value | close | 1-3k bets | 22-21 | 51.2 | 5.5 | 30.2 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 68-75 | 47.6 | 4.3 | 15.0 |  |
| money_moving+pin_rlm | close | 1-3k bets | 66-74 | 47.1 | 3.9 | 14.7 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 16-27 | 37.2 | -2.6 | 5.5 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 108-127 | 46.0 | 0.8 | -0.3 |  |
| money_level+rlm_ratio | close | 1-3k bets | 55-47 | 53.9 | 4.0 | 4.2 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 105-125 | 45.7 | 0.5 | -0.6 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 108-127 | 46.0 | 0.8 | -0.3 |  |
| follow_move+pin_rlm | close | 1-3k bets | 50-55 | 47.6 | 2.2 | -0.2 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 50-55 | 47.6 | 2.2 | -0.2 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 20-18 | 52.6 | 4.9 | 1.4 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 47.9 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 26-27 | 49.1 | -0.1 | -3.1 |  |
| consensus_gap+money_moving | close | 3k+ bets | 30-47 | 39.0 | -3.8 | 18.5 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-5 | 37.5 | -3.6 | 19.3 |  |
| consensus_gap+pin_value | close | 3k+ bets | 30-30 | 50.0 | 4.7 | 4.0 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -0.3 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 31-47 | 39.7 | -2.9 | 21.9 |  |
| follow_move+money_moving | close | 3k+ bets | 84-88 | 48.8 | -0.5 | -3.9 |  |
| follow_move+pin_rlm | close | 3k+ bets | 23-19 | 54.8 | 11.1 | 25.6 |  |
| follow_move+pin_value | close | 3k+ bets | 24-26 | 48.0 | -1.1 | -10.0 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 39-31 | 55.7 | 11.2 | 21.0 |  |
| follow_move+sharp_gap | close | 3k+ bets | 86-87 | 49.7 | 0.8 | -1.3 |  |
| money_moving+pin_rlm | close | 3k+ bets | 23-27 | 46.0 | 4.5 | 5.3 |  |
| money_moving+pin_value | close | 3k+ bets | 28-37 | 43.1 | -2.9 | -8.3 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 37-29 | 56.1 | 11.7 | 22.4 |  |
| money_moving+sharp_gap | close | 3k+ bets | 164-170 | 49.1 | 2.1 | 5.8 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-7 | 41.7 | -5.4 | -21.0 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 23-19 | 54.8 | 11.1 | 25.6 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 24-27 | 47.1 | 5.4 | 7.1 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 6-5 | 54.5 | 4.2 | 2.8 |  |
| pin_value+sharp_gap | close | 3k+ bets | 28-35 | 44.4 | -1.6 | -5.3 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 39-31 | 55.7 | 11.2 | 21.0 |  |
| money_level+money_moving | close | 3k+ bets | 116-102 | 53.2 | 1.5 | -1.0 |  |
| money_level+sharp_gap | close | 3k+ bets | 115-99 | 53.7 | 2.2 | 0.8 |  |
| follow_move+money_level | close | 3k+ bets | 103-81 | 56.0 | -0.4 | -5.8 |  |
| money_level+rlm_ratio | close | 3k+ bets | 21-10 | 67.7 | 20.5 | 40.2 |  |
| consensus_gap+money_level | close | 3k+ bets | 38-36 | 51.4 | -4.2 | -11.5 |  |
| money_level+pin_value | close | 3k+ bets | 30-38 | 44.1 | -4.7 | -18.5 |  |
| money_level+pin_rlm | close | 3k+ bets | 11-7 | 61.1 | 16.7 | 36.5 |  |
| money_level+money_moving | close | <1k bets | 73-77 | 48.7 | -3.8 | -15.8 |  |
| money_level+sharp_gap | close | <1k bets | 76-77 | 49.7 | -3.2 | -15.3 |  |
| money_moving+sharp_gap | close | <1k bets | 105-132 | 44.3 | -3.5 | -15.4 |  |
| consensus_gap+money_level | close | <1k bets | 16-26 | 38.1 | -17.5 | -41.8 |  |
| consensus_gap+money_moving | close | <1k bets | 15-38 | 28.3 | -12.6 | -35.3 |  |
| consensus_gap+pin_value | close | <1k bets | 13-14 | 48.1 | 6.9 | 12.9 |  |
| consensus_gap+sharp_gap | close | <1k bets | 15-39 | 27.8 | -12.9 | -36.5 |  |
| money_level+pin_value | close | <1k bets | 17-17 | 50.0 | 0.2 | -6.7 |  |
| money_moving+pin_value | close | <1k bets | 15-16 | 48.4 | 3.1 | 10.3 |  |
| pin_value+sharp_gap | close | <1k bets | 15-15 | 50.0 | 4.1 | 13.9 |  |
| follow_move+money_moving | close | <1k bets | 51-61 | 45.5 | -4.3 | -15.0 |  |
| follow_move+sharp_gap | close | <1k bets | 53-61 | 46.5 | -4.2 | -17.4 |  |
| follow_move+rlm_ratio | close | <1k bets | 24-25 | 49.0 | 5.6 | -0.8 |  |
| money_moving+rlm_ratio | close | <1k bets | 24-25 | 49.0 | 5.6 | -0.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 24-25 | 49.0 | 5.6 | -0.8 |  |
| follow_move+money_level | close | <1k bets | 71-59 | 54.6 | -3.5 | -16.9 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -1.3 | 12.2 |  |
| money_moving+pin_rlm | close | <1k bets | 21-21 | 50.0 | 8.7 | 11.0 |  |
| pin_rlm+sharp_gap | close | <1k bets | 21-21 | 50.0 | 8.7 | 11.0 |  |
| consensus_gap+follow_move | close | <1k bets | 8-19 | 29.6 | -20.4 | -54.6 |  |
| follow_move+pin_rlm | close | <1k bets | 16-11 | 59.3 | 15.4 | 17.3 |  |
| follow_move+pin_value | close | <1k bets | 17-12 | 58.6 | 10.0 | 11.4 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 20.6 | 60.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 16-11 | 59.3 | 15.4 | 17.3 |  |
| pin_value+rlm_ratio | close | <1k bets | 3-1 | 75.0 | 24.2 | 43.9 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 1-7 | 12.5 | -20.0 | -74.8 |  |
| money_level+rlm_ratio | close | <1k bets | 12-13 | 48.0 | 1.9 | -5.3 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 16.7 | 19.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 31-43 | 41.9 | -9.0 | -17.1 |  |
| consensus_gap+money_moving | close | pin $1-2k | 44-60 | 42.3 | -5.1 | -6.3 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 12-16 | 42.9 | 2.1 | 32.5 |  |
| consensus_gap+pin_value | close | pin $1-2k | 52-67 | 43.7 | -1.5 | -10.9 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 12-12 | 50.0 | 4.6 | 11.5 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 44-57 | 43.6 | -3.2 | -3.6 |  |
| follow_move+money_moving | close | pin $1-2k | 127-162 | 43.9 | -5.7 | -12.7 |  |
| follow_move+pin_rlm | close | pin $1-2k | 39-35 | 52.7 | 6.1 | 13.3 |  |
| follow_move+pin_value | close | pin $1-2k | 44-57 | 43.6 | -5.5 | -18.0 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 57-55 | 50.9 | 4.1 | 8.3 |  |
| follow_move+sharp_gap | close | pin $1-2k | 131-159 | 45.2 | -4.7 | -11.3 |  |
| money_moving+pin_rlm | close | pin $1-2k | 47-48 | 49.5 | 5.1 | 17.0 |  |
| money_moving+pin_value | close | pin $1-2k | 52-82 | 38.8 | -8.5 | -23.0 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 56-53 | 51.4 | 4.6 | 9.5 |  |
| money_moving+sharp_gap | close | pin $1-2k | 219-248 | 46.9 | -1.8 | -5.4 |  |
| pin_rlm+pin_value | close | pin $1-2k | 12-19 | 38.7 | -9.7 | -17.4 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 39-35 | 52.7 | 6.1 | 13.3 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 49-49 | 50.0 | 5.6 | 17.3 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 13-15 | 46.4 | -3.4 | -12.7 |  |
| pin_value+sharp_gap | close | pin $1-2k | 52-79 | 39.7 | -7.6 | -21.2 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 57-55 | 50.9 | 4.1 | 8.3 |  |
| follow_move+money_level | close | pin $1-2k | 149-152 | 49.5 | -4.4 | -13.2 |  |
| money_level+rlm_ratio | close | pin $1-2k | 36-26 | 58.1 | 9.7 | 13.7 |  |
| money_level+sharp_gap | close | pin $1-2k | 167-170 | 49.6 | -1.9 | -7.7 |  |
| money_level+money_moving | close | pin $1-2k | 164-173 | 48.7 | -2.6 | -9.1 |  |
| consensus_gap+money_level | close | pin $1-2k | 48-52 | 48.0 | -7.8 | -14.5 |  |
| money_level+pin_value | close | pin $1-2k | 56-68 | 45.2 | -4.2 | -15.4 |  |
| money_level+pin_rlm | close | pin $1-2k | 25-18 | 58.1 | 11.3 | 14.8 |  |
| follow_move+money_level | close | pin $2k+ | 114-73 | 61.0 | 1.4 | -3.9 |  |
| follow_move+money_moving | close | pin $2k+ | 83-88 | 48.5 | 1.0 | -7.0 |  |
| follow_move+sharp_gap | close | pin $2k+ | 84-90 | 48.3 | 0.7 | -7.2 |  |
| money_level+money_moving | close | pin $2k+ | 114-109 | 51.1 | -1.4 | -6.8 |  |
| money_level+sharp_gap | close | pin $2k+ | 114-111 | 50.7 | -1.9 | -7.2 |  |
| money_moving+sharp_gap | close | pin $2k+ | 168-209 | 44.6 | -1.2 | -6.4 |  |
| consensus_gap+money_moving | close | pin $2k+ | 26-54 | 32.5 | -9.0 | -5.9 |  |
| consensus_gap+pin_value | close | pin $2k+ | 32-41 | 43.8 | 3.1 | 11.2 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 27-57 | 32.1 | -10.3 | -8.8 |  |
| money_moving+pin_value | close | pin $2k+ | 44-53 | 45.4 | 1.6 | 8.7 |  |
| pin_value+sharp_gap | close | pin $2k+ | 44-54 | 44.9 | 1.3 | 7.6 |  |
| consensus_gap+follow_move | close | pin $2k+ | 22-23 | 48.9 | -2.2 | -19.0 |  |
| follow_move+pin_value | close | pin $2k+ | 27-26 | 50.9 | 4.8 | -3.1 |  |
| follow_move+pin_rlm | close | pin $2k+ | 21-36 | 36.8 | -0.6 | -12.9 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 29-44 | 39.7 | 1.9 | -10.1 |  |
| money_level+pin_rlm | close | pin $2k+ | 10-9 | 52.6 | 9.7 | 15.2 |  |
| money_level+pin_value | close | pin $2k+ | 43-43 | 50.0 | 0.9 | -7.8 |  |
| money_level+rlm_ratio | close | pin $2k+ | 11-10 | 52.4 | 5.5 | 12.4 |  |
| money_moving+pin_rlm | close | pin $2k+ | 27-56 | 32.5 | -2.7 | -14.7 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 29-43 | 40.3 | 2.3 | -8.9 |  |
| pin_rlm+pin_value | close | pin $2k+ | 5-10 | 33.3 | -2.0 | 31.2 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 21-36 | 36.8 | -0.6 | -12.9 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 27-56 | 32.5 | -2.7 | -14.7 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 3-5 | 37.5 | -1.5 | -22.1 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 29-44 | 39.7 | 1.9 | -10.1 |  |
| consensus_gap+money_level | close | pin $2k+ | 49-37 | 57.0 | -4.5 | -11.0 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-17 | 19.0 | -10.0 | -17.6 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-10 | 0.0 | -29.2 | -100.0 |  |
| money_level+money_moving | close | pin limit <$1k | 60-64 | 48.4 | -1.4 | -7.1 |  |
| money_level+sharp_gap | close | pin limit <$1k | 62-63 | 49.6 | -0.3 | -4.8 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 94-94 | 50.0 | -0.2 | 0.7 |  |
| consensus_gap+money_level | close | pin limit <$1k | 21-22 | 48.8 | -0.3 | -9.8 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 28-30 | 48.3 | -0.1 | -1.6 |  |
| follow_move+money_moving | close | pin limit <$1k | 61-61 | 50.0 | -0.3 | -3.8 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 63-59 | 51.6 | 1.2 | -0.7 |  |
| money_level+pin_value | close | pin limit <$1k | 36-30 | 54.5 | 5.9 | 3.1 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 15-10 | 60.0 | 10.6 | 9.5 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 18-15 | 54.5 | 6.5 | 16.2 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 19-16 | 54.3 | 5.8 | 14.9 |  |
| follow_move+money_level | close | pin limit <$1k | 51-49 | 51.0 | 0.9 | -2.9 |  |
| follow_move+pin_value | close | pin limit <$1k | 30-19 | 61.2 | 12.1 | 16.0 |  |
| money_moving+pin_value | close | pin limit <$1k | 29-24 | 54.7 | 5.8 | 12.2 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 31-25 | 55.4 | 6.1 | 13.0 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 4-2 | 66.7 | 21.6 | 99.8 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 36-18 | 66.7 | 16.2 | 44.3 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 15-2 | 88.2 | 39.1 | 94.5 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 37-18 | 67.3 | 16.8 | 45.2 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 29-14 | 67.4 | 16.0 | 29.8 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 40-23 | 63.5 | 12.5 | 22.7 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 38-23 | 62.3 | 11.3 | 20.5 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 29-14 | 67.4 | 16.0 | 29.8 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 40-23 | 63.5 | 12.5 | 22.7 |  |
| money_level+pin_rlm | close | pin limit <$1k | 18-9 | 66.7 | 15.2 | 28.0 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 20-12 | 62.5 | 11.9 | 21.7 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 13-4 | 76.5 | 25.6 | 46.7 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 4-3 | 57.1 | 8.0 | 8.5 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 47.9 | 87.7 |  |
| pin_rlm | early | <1k bets | 1-2 | 33.3 | 6.7 | -35.8 | -1.0 |
| pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -26.6 | -100.0 | -1.75 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.4 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -50.4 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 319-277 | 53.5 | 1.3 | -7.4 | 0.25 |
| follow_move | early | pin $1-2k | 27-16 | 62.8 | 8.5 | 11.9 | -0.35 |
| follow_move | early | pin limit <$1k | 47-39 | 54.7 | 4.7 | 1.9 | -0.11 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.3 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.8 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 15-11 | 57.7 | 22.6 | 33.0 | 0.43 |
| rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 2.9 | 55.6 | -1.52 |
| rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 42.8 | 77.5 | 0.29 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 0.5 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 42.5 | 59.7 | 0.33 |
| money_level | early | <1k bets | 107-65 | 62.2 | 2.2 | -4.6 | 0.08 |
| money_level | early | pin $1-2k | 20-8 | 71.4 | 5.9 | 4.1 | 0.01 |
| money_level | early | pin limit <$1k | 24-26 | 48.0 | -5.3 | -11.4 | 0.22 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.1 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 7.2 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 92-68 | 57.5 | 7.9 | 9.2 | 0.39 |
| sharp_gap | early | pin $1-2k | 15-11 | 57.7 | 4.7 | 6.7 | -0.39 |
| sharp_gap | early | pin limit <$1k | 29-18 | 61.7 | 13.0 | 27.9 | 0.12 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.3 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.4 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 60-46 | 56.6 | 4.6 | -0.6 | 0.01 |
| money_moving | early | pin $1-2k | 8-8 | 50.0 | -8.4 | -31.4 | 0.21 |
| money_moving | early | pin limit <$1k | 23-9 | 71.9 | 22.6 | 52.0 | 0.42 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.6 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 36-39 | 48.0 | -0.1 | -9.2 | 0.13 |
| pin_value | early | pin $1-2k | 13-18 | 41.9 | -3.6 | -21.1 | 0.12 |
| pin_value | early | pin limit <$1k | 36-30 | 54.5 | 5.1 | 3.2 | 0.09 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -47.9 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -27.6 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -10.9 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 13.1 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 152-198 | 43.4 | -3.5 | -11.6 | 0.35 |
| consensus_gap | early | pin $1-2k | 12-20 | 37.5 | -7.8 | -28.2 | 0.51 |
| consensus_gap | early | pin limit <$1k | 18-34 | 34.6 | -15.2 | -28.2 | 0.28 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 16.6 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 3.8 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 3.4 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.5 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.0 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.0 | 26.0 | -0.25 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -0.4 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 4.2 | -6.9 | 0.3 |
| follow_move+pin_value | early | 1-3k bets | 7-6 | 53.8 | 6.6 | 0.8 | -0.31 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.2 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.4 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 2.6 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.3 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.3 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 27.5 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.3 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.1 | 25.3 | 0.18 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.9 | 56.1 | 0.15 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 18.8 | 18.8 | -0.24 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.8 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.8 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.4 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.8 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 37.3 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 47.9 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 23-28 | 45.1 | -5.9 | -18.0 | 1.11 |
| consensus_gap+money_level | early | <1k bets | 20-16 | 55.6 | -10.2 | -16.2 | 0.34 |
| consensus_gap+sharp_gap | early | <1k bets | 18-31 | 36.7 | -10.2 | -15.9 | 0.8 |
| follow_move+money_level | early | <1k bets | 59-29 | 67.0 | 6.4 | -3.4 | 0.28 |
| follow_move+sharp_gap | early | <1k bets | 46-22 | 67.6 | 16.6 | 19.5 | 0.58 |
| money_level+sharp_gap | early | <1k bets | 64-33 | 66.0 | 8.7 | 6.8 | 0.4 |
| follow_move+money_moving | early | <1k bets | 28-15 | 65.1 | 10.0 | 13.2 | 0.43 |
| money_level+money_moving | early | <1k bets | 39-24 | 61.9 | 2.9 | -3.0 | -0.19 |
| money_moving+sharp_gap | early | <1k bets | 39-26 | 60.0 | 9.1 | 7.9 | 0.23 |
| consensus_gap+money_moving | early | <1k bets | 8-17 | 32.0 | -14.0 | -48.6 | 0.02 |
| follow_move+pin_value | early | <1k bets | 13-11 | 54.2 | 4.9 | 1.3 | -0.01 |
| follow_move+rlm_ratio | early | <1k bets | 15-11 | 57.7 | 22.6 | 33.0 | 0.43 |
| rlm_ratio+sharp_gap | early | <1k bets | 15-11 | 57.7 | 22.6 | 33.0 | 0.43 |
| consensus_gap+pin_value | early | <1k bets | 13-23 | 36.1 | -10.2 | -32.5 | 0.4 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | <1k bets | 2-3 | 40.0 | 3.2 | -15.4 | 0.84 |
| follow_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 23.4 | -3.7 | -2.15 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 23.4 | -3.7 | -2.15 |
| pin_rlm+sharp_gap | early | <1k bets | 1-2 | 33.3 | 6.7 | -35.8 | -1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 10.7 | -4.5 | -1.9 |
| pin_value+sharp_gap | early | <1k bets | 5-4 | 55.6 | 8.7 | 6.1 | -0.09 |
| money_level+pin_value | early | <1k bets | 4-4 | 50.0 | 0.5 | -4.5 | 0.88 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -52.4 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 1-2 | 33.3 | -17.6 | -36.4 | 1.33 |
| money_level+rlm_ratio | early | <1k bets | 6-5 | 54.5 | 16.7 | 9.4 | 1.47 |
| money_moving+rlm_ratio | early | <1k bets | 6-3 | 66.7 | 24.1 | 58.0 | 0.29 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 5-4 | 55.6 | -9.1 | -12.6 | 0.71 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -31.3 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 5-10 | 33.3 | -7.7 | -38.7 | 0.31 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 2.9 | 55.6 | -1.52 |
| follow_move+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 13.8 | 37.5 | -0.83 |
| money_level+money_moving | early | pin $1-2k | 8-5 | 61.5 | -4.2 | -15.6 | 0.07 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.3 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-3 | 40.0 | 2.9 | 55.6 | -1.52 |
| money_level+sharp_gap | early | pin $1-2k | 12-4 | 75.0 | 10.4 | 12.5 | -0.26 |
| money_moving+sharp_gap | early | pin $1-2k | 4-6 | 40.0 | -16.7 | -45.4 | 0.08 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.9 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 4-6 | 40.0 | -10.0 | -31.3 | 0.34 |
| follow_move+pin_value | early | pin $1-2k | 6-5 | 54.5 | 7.2 | 0.8 | -0.3 |
| follow_move+money_level | early | pin $1-2k | 11-4 | 73.3 | 8.3 | 6.6 | -0.07 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 47.2 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 4-1 | 80.0 | 11.9 | 6.9 | -0.18 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -16.7 | -46.8 | -0.12 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -26.6 | -100.0 | -1.75 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| money_level+money_moving | early | pin limit <$1k | 13-7 | 65.0 | 12.5 | 20.2 | 0.48 |
| money_level+sharp_gap | early | pin limit <$1k | 20-16 | 55.6 | 4.8 | 1.6 | 0.14 |
| money_moving+sharp_gap | early | pin limit <$1k | 18-5 | 78.3 | 30.0 | 70.1 | 0.35 |
| money_level+pin_value | early | pin limit <$1k | 9-6 | 60.0 | 9.3 | 13.8 | 0.33 |
| money_moving+pin_value | early | pin limit <$1k | 7-4 | 63.6 | 13.5 | 20.1 | 0.18 |
| pin_value+sharp_gap | early | pin limit <$1k | 12-6 | 66.7 | 16.5 | 26.4 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-9 | 40.0 | -11.2 | -25.7 | 0.53 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -26.7 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 14-18 | 43.8 | -4.8 | -17.9 | 0.43 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.2 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 11-11 | 50.0 | -3.9 | -7.4 | -0.04 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 4.8 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 13-7 | 65.0 | 16.4 | 24.2 | -0.07 |
| follow_move+rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 42.8 | 77.5 | 0.29 |
| money_level+rlm_ratio | early | pin limit <$1k | 6-0 | 100.0 | 52.9 | 92.6 | 0.42 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 16.0 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 7-1 | 87.5 | 42.8 | 77.5 | 0.29 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 23.1 | 72.3 | 0.54 |
| follow_move+money_moving | early | pin limit <$1k | 9-3 | 75.0 | 25.5 | 43.3 | 0.33 |
| money_moving+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.0 | 45.3 | -0.5 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
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
| pin_rlm | close | 1-3k bets | 9-11 | 45.0 | 3.8 | 14.3 |  |
| pin_rlm | close | 3k+ bets | 4-5 | 44.4 | 4.9 | 11.4 |  |
| pin_rlm | close | <1k bets | 0-1 | 0.0 | -31.7 | -100.0 |  |
| pin_rlm | close | pin $1-2k | 5-8 | 38.5 | -1.3 | -2.8 |  |
| pin_rlm | close | pin $2k+ | 6-7 | 46.2 | 6.0 | 26.8 |  |
| pin_rlm | close | pin limit <$1k | 2-2 | 50.0 | 6.9 | -5.5 |  |
| follow_move | close | 1-3k bets | 57-56 | 50.4 | -1.6 | -7.6 |  |
| follow_move | close | 3k+ bets | 23-19 | 54.8 | 3.1 | -2.2 |  |
| follow_move | close | <1k bets | 6-4 | 60.0 | 9.1 | -2.7 |  |
| follow_move | close | pin $1-2k | 19-27 | 41.3 | -11.3 | -17.8 |  |
| follow_move | close | pin $2k+ | 23-16 | 59.0 | 4.3 | 7.5 |  |
| follow_move | close | pin limit <$1k | 5-6 | 45.5 | -0.8 | -13.2 |  |
| rlm_ratio | close | 1-3k bets | 14-16 | 46.7 | 4.6 | 9.1 |  |
| rlm_ratio | close | 3k+ bets | 6-3 | 66.7 | 23.6 | 52.9 |  |
| rlm_ratio | close | <1k bets | 0-3 | 0.0 | -40.2 | -100.0 |  |
| rlm_ratio | close | pin $1-2k | 3-6 | 33.3 | -10.3 | -2.0 |  |
| rlm_ratio | close | pin $2k+ | 4-2 | 66.7 | 26.3 | 110.3 |  |
| rlm_ratio | close | pin limit <$1k | 2-3 | 40.0 | -1.7 | -23.6 |  |
| money_level | close | 1-3k bets | 80-63 | 55.9 | -0.8 | -5.8 |  |
| money_level | close | 3k+ bets | 33-18 | 64.7 | 10.0 | 15.1 |  |
| money_level | close | <1k bets | 9-3 | 75.0 | 14.7 | 20.9 |  |
| money_level | close | pin $1-2k | 23-30 | 43.4 | -13.2 | -20.8 |  |
| money_level | close | pin $2k+ | 32-22 | 59.3 | 4.2 | 0.6 |  |
| money_level | close | pin limit <$1k | 8-7 | 53.3 | -1.3 | 1.6 |  |
| sharp_gap | close | 1-3k bets | 68-68 | 50.0 | 2.3 | -0.5 |  |
| sharp_gap | close | 3k+ bets | 26-23 | 53.1 | 4.5 | 9.1 |  |
| sharp_gap | close | <1k bets | 3-8 | 27.3 | -18.1 | -50.5 |  |
| sharp_gap | close | pin $1-2k | 19-31 | 38.0 | -10.6 | -22.1 |  |
| sharp_gap | close | pin $2k+ | 26-26 | 50.0 | 2.6 | 15.8 |  |
| sharp_gap | close | pin limit <$1k | 7-7 | 50.0 | 2.0 | -4.8 |  |
| money_moving | close | 1-3k bets | 68-69 | 49.6 | 1.6 | -2.3 |  |
| money_moving | close | 3k+ bets | 26-23 | 53.1 | 4.5 | 9.1 |  |
| money_moving | close | <1k bets | 3-8 | 27.3 | -18.1 | -50.5 |  |
| money_moving | close | pin $1-2k | 19-32 | 37.3 | -11.1 | -23.7 |  |
| money_moving | close | pin $2k+ | 26-26 | 50.0 | 2.6 | 14.9 |  |
| money_moving | close | pin limit <$1k | 7-7 | 50.0 | 2.0 | -4.8 |  |
| pin_value | close | 1-3k bets | 20-31 | 39.2 | -6.3 | 12.5 |  |
| pin_value | close | 3k+ bets | 5-7 | 41.7 | -10.2 | -22.0 |  |
| pin_value | close | <1k bets | 3-0 | 100.0 | 60.2 | 90.9 |  |
| pin_value | close | pin $1-2k | 11-21 | 34.4 | -12.3 | 8.3 |  |
| pin_value | close | pin $2k+ | 9-15 | 37.5 | -7.2 | -5.7 |  |
| pin_value | close | pin limit <$1k | 8-2 | 80.0 | 30.0 | 51.9 |  |
| consensus_gap | close | 1-3k bets | 13-23 | 36.1 | -8.5 | -4.7 |  |
| consensus_gap | close | 3k+ bets | 10-7 | 58.8 | 12.8 | 25.7 |  |
| consensus_gap | close | <1k bets | 1-3 | 25.0 | -10.6 | -52.3 |  |
| consensus_gap | close | pin $1-2k | 6-7 | 46.2 | -5.7 | -13.1 |  |
| consensus_gap | close | pin $2k+ | 8-10 | 44.4 | 3.2 | 56.2 |  |
| consensus_gap | close | pin limit <$1k | 1-0 | 100.0 | 63.9 | 90.9 |  |
| money_level+money_moving | close | 1-3k bets | 48-39 | 55.2 | 1.8 | -3.3 |  |
| money_level+pin_rlm | close | 1-3k bets | 3-4 | 42.9 | -6.1 | -18.7 |  |
| money_level+sharp_gap | close | 1-3k bets | 47-38 | 55.3 | 2.2 | -1.6 |  |
| money_moving+pin_rlm | close | 1-3k bets | 9-11 | 45.0 | 3.8 | 14.3 |  |
| money_moving+sharp_gap | close | 1-3k bets | 66-66 | 50.0 | 2.1 | -0.2 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 9-11 | 45.0 | 3.8 | 14.3 |  |
| money_level+pin_value | close | 1-3k bets | 8-11 | 42.1 | -10.4 | -21.4 |  |
| money_moving+pin_value | close | 1-3k bets | 10-18 | 35.7 | -9.5 | -11.7 |  |
| pin_value+sharp_gap | close | 1-3k bets | 10-18 | 35.7 | -9.3 | -11.7 |  |
| follow_move+money_level | close | 1-3k bets | 40-31 | 56.3 | -1.4 | -8.5 |  |
| follow_move+pin_value | close | 1-3k bets | 2-8 | 20.0 | -28.9 | -61.8 |  |
| consensus_gap+money_level | close | 1-3k bets | 4-6 | 40.0 | -19.8 | -35.8 |  |
| follow_move+money_moving | close | 1-3k bets | 37-35 | 51.4 | 1.4 | -0.5 |  |
| follow_move+pin_rlm | close | 1-3k bets | 4-5 | 44.4 | 5.0 | 48.0 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 14-16 | 46.7 | 4.6 | 9.1 |  |
| follow_move+sharp_gap | close | 1-3k bets | 37-35 | 51.4 | 1.9 | 1.5 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 13-16 | 44.8 | 2.5 | 6.2 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 4-5 | 44.4 | 5.0 | 48.0 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 14-16 | 46.7 | 4.6 | 9.1 |  |
| consensus_gap+money_moving | close | 1-3k bets | 8-12 | 40.0 | -3.2 | -0.3 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 8-12 | 40.0 | -3.2 | -0.3 |  |
| consensus_gap+pin_value | close | 1-3k bets | 5-8 | 38.5 | -3.1 | 17.9 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 2-3 | 40.0 | 6.5 | -23.6 |  |
| pin_rlm+pin_value | close | 1-3k bets | 4-4 | 50.0 | 8.9 | -5.0 |  |
| money_level+rlm_ratio | close | 1-3k bets | 6-6 | 50.0 | -1.9 | -2.8 |  |
| consensus_gap+follow_move | close | 1-3k bets | 3-4 | 42.9 | -6.7 | -31.5 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 1-1 | 50.0 | 16.1 | -4.5 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 1-2 | 33.3 | -2.8 | -36.4 |  |
| consensus_gap+money_level | close | 3k+ bets | 5-1 | 83.3 | 29.6 | 51.0 |  |
| consensus_gap+money_moving | close | 3k+ bets | 4-3 | 57.1 | 16.4 | 46.0 |  |
| consensus_gap+pin_value | close | 3k+ bets | 2-0 | 100.0 | 44.4 | 87.1 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 4-3 | 57.1 | 16.4 | 46.0 |  |
| money_level+money_moving | close | 3k+ bets | 22-12 | 64.7 | 12.3 | 27.4 |  |
| money_level+pin_value | close | 3k+ bets | 4-5 | 44.4 | -9.6 | -17.2 |  |
| money_level+sharp_gap | close | 3k+ bets | 22-12 | 64.7 | 12.3 | 27.4 |  |
| money_moving+pin_value | close | 3k+ bets | 2-3 | 40.0 | -12.8 | -26.7 |  |
| money_moving+sharp_gap | close | 3k+ bets | 26-23 | 53.1 | 4.5 | 9.1 |  |
| pin_value+sharp_gap | close | 3k+ bets | 2-3 | 40.0 | -12.8 | -26.7 |  |
| follow_move+money_level | close | 3k+ bets | 17-9 | 65.4 | 9.6 | 12.7 |  |
| follow_move+money_moving | close | 3k+ bets | 13-10 | 56.5 | 5.1 | 12.0 |  |
| follow_move+sharp_gap | close | 3k+ bets | 13-10 | 56.5 | 5.1 | 12.0 |  |
| consensus_gap+follow_move | close | 3k+ bets | 3-2 | 60.0 | 10.3 | 19.9 |  |
| follow_move+pin_rlm | close | 3k+ bets | 4-3 | 57.1 | 18.3 | 43.2 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 6-3 | 66.7 | 23.6 | 52.9 |  |
| money_level+pin_rlm | close | 3k+ bets | 3-1 | 75.0 | 40.0 | 102.9 |  |
| money_level+rlm_ratio | close | 3k+ bets | 4-1 | 80.0 | 42.5 | 101.2 |  |
| money_moving+pin_rlm | close | 3k+ bets | 4-5 | 44.4 | 4.9 | 11.4 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 6-3 | 66.7 | 23.6 | 52.9 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 4-3 | 57.1 | 18.3 | 43.2 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 4-5 | 44.4 | 4.9 | 11.4 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 6-3 | 66.7 | 23.6 | 52.9 |  |
| follow_move+pin_value | close | 3k+ bets | 1-3 | 25.0 | -27.8 | -54.2 |  |
| pin_rlm+pin_value | close | 3k+ bets | 0-1 | 0.0 | -52.8 | -100.0 |  |
| money_level+money_moving | close | <1k bets | 3-2 | 60.0 | 4.1 | 8.9 |  |
| money_level+sharp_gap | close | <1k bets | 3-2 | 60.0 | 4.1 | 8.9 |  |
| money_moving+sharp_gap | close | <1k bets | 3-8 | 27.3 | -18.1 | -50.5 |  |
| follow_move+money_moving | close | <1k bets | 2-3 | 40.0 | -7.2 | -27.7 |  |
| follow_move+rlm_ratio | close | <1k bets | 0-3 | 0.0 | -40.2 | -100.0 |  |
| follow_move+sharp_gap | close | <1k bets | 2-3 | 40.0 | -7.2 | -27.7 |  |
| money_moving+rlm_ratio | close | <1k bets | 0-3 | 0.0 | -40.2 | -100.0 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 0-3 | 0.0 | -40.2 | -100.0 |  |
| consensus_gap+money_moving | close | <1k bets | 0-2 | 0.0 | -31.7 | -100.0 |  |
| consensus_gap+sharp_gap | close | <1k bets | 0-2 | 0.0 | -31.7 | -100.0 |  |
| follow_move+money_level | close | <1k bets | 5-1 | 83.3 | 24.7 | 30.3 |  |
| consensus_gap+pin_value | close | <1k bets | 1-0 | 100.0 | 52.8 | 90.9 |  |
| money_level+rlm_ratio | close | <1k bets | 0-1 | 0.0 | -52.8 | -100.0 |  |
| follow_move+pin_value | close | <1k bets | 1-0 | 100.0 | 63.9 | 90.9 |  |
| consensus_gap+follow_move | close | <1k bets | 0-1 | 0.0 | -31.7 | -100.0 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 0-1 | 0.0 | -31.7 | -100.0 |  |
| money_moving+pin_rlm | close | <1k bets | 0-1 | 0.0 | -31.7 | -100.0 |  |
| pin_rlm+sharp_gap | close | <1k bets | 0-1 | 0.0 | -31.7 | -100.0 |  |
| money_level+money_moving | close | pin $1-2k | 12-21 | 36.4 | -17.1 | -31.9 |  |
| money_level+pin_value | close | pin $1-2k | 2-9 | 18.2 | -40.2 | -65.6 |  |
| money_level+sharp_gap | close | pin $1-2k | 12-21 | 36.4 | -17.1 | -31.9 |  |
| money_moving+pin_value | close | pin $1-2k | 3-14 | 17.6 | -28.7 | -66.3 |  |
| money_moving+sharp_gap | close | pin $1-2k | 19-31 | 38.0 | -10.6 | -22.1 |  |
| pin_value+sharp_gap | close | pin $1-2k | 3-13 | 18.8 | -28.2 | -64.2 |  |
| follow_move+money_level | close | pin $1-2k | 14-21 | 40.0 | -16.2 | -27.6 |  |
| follow_move+money_moving | close | pin $1-2k | 12-20 | 37.5 | -13.6 | -18.5 |  |
| follow_move+sharp_gap | close | pin $1-2k | 12-20 | 37.5 | -13.6 | -18.5 |  |
| consensus_gap+money_level | close | pin $1-2k | 2-3 | 40.0 | -19.0 | -25.2 |  |
| consensus_gap+money_moving | close | pin $1-2k | 2-3 | 40.0 | -6.1 | -25.2 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 2-3 | 40.0 | -6.1 | -25.2 |  |
| consensus_gap+pin_value | close | pin $1-2k | 4-5 | 44.4 | -2.9 | -15.6 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 1-0 | 100.0 | 63.9 | 90.9 |  |
| money_moving+pin_rlm | close | pin $1-2k | 5-8 | 38.5 | -1.3 | -2.8 |  |
| pin_rlm+pin_value | close | pin $1-2k | 2-3 | 40.0 | 0.6 | -23.6 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 5-8 | 38.5 | -1.3 | -2.8 |  |
| follow_move+pin_rlm | close | pin $1-2k | 3-4 | 42.9 | 3.4 | 26.0 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 3-6 | 33.3 | -10.3 | -2.0 |  |
| money_level+pin_rlm | close | pin $1-2k | 2-3 | 40.0 | -4.1 | -23.6 |  |
| money_level+rlm_ratio | close | pin $1-2k | 2-3 | 40.0 | -10.6 | -23.6 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 3-6 | 33.3 | -10.3 | -2.0 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 3-4 | 42.9 | 3.4 | 26.0 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 3-6 | 33.3 | -10.3 | -2.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 0-2 | 0.0 | -57.7 | -100.0 |  |
| follow_move+pin_value | close | pin $1-2k | 0-8 | 0.0 | -51.4 | -100.0 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 0-2 | 0.0 | -36.1 | -100.0 |  |
| money_level+money_moving | close | pin $2k+ | 18-13 | 58.1 | 6.4 | 7.8 |  |
| money_level+pin_rlm | close | pin $2k+ | 3-1 | 75.0 | 34.4 | 102.9 |  |
| money_level+sharp_gap | close | pin $2k+ | 18-13 | 58.1 | 6.4 | 9.4 |  |
| money_moving+pin_rlm | close | pin $2k+ | 6-7 | 46.2 | 6.0 | 26.8 |  |
| money_moving+sharp_gap | close | pin $2k+ | 25-25 | 50.0 | 2.7 | 17.2 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 6-7 | 46.2 | 6.0 | 26.8 |  |
| consensus_gap+money_level | close | pin $2k+ | 4-3 | 57.1 | 0.9 | -2.3 |  |
| consensus_gap+money_moving | close | pin $2k+ | 4-6 | 40.0 | -0.0 | 58.8 |  |
| consensus_gap+pin_value | close | pin $2k+ | 3-3 | 50.0 | 10.5 | 91.1 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 4-6 | 40.0 | -0.0 | 58.8 |  |
| money_level+pin_value | close | pin $2k+ | 8-7 | 53.3 | 5.7 | -1.1 |  |
| money_moving+pin_value | close | pin $2k+ | 7-7 | 50.0 | 4.2 | 34.9 |  |
| pin_value+sharp_gap | close | pin $2k+ | 7-8 | 46.7 | 1.8 | 25.9 |  |
| follow_move+money_level | close | pin $2k+ | 18-9 | 66.7 | 8.5 | 8.8 |  |
| follow_move+money_moving | close | pin $2k+ | 11-6 | 64.7 | 12.7 | 35.9 |  |
| follow_move+sharp_gap | close | pin $2k+ | 11-6 | 64.7 | 12.7 | 38.9 |  |
| follow_move+pin_value | close | pin $2k+ | 2-3 | 40.0 | -10.6 | -25.2 |  |
| follow_move+pin_rlm | close | pin $2k+ | 4-2 | 66.7 | 26.3 | 110.3 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 4-2 | 66.7 | 26.3 | 110.3 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 4-2 | 66.7 | 26.3 | 110.3 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 4-2 | 66.7 | 26.3 | 110.3 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 4-2 | 66.7 | 26.3 | 110.3 |  |
| money_level+rlm_ratio | close | pin $2k+ | 2-1 | 66.7 | 28.3 | 107.0 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 0-3 | 0.0 | -31.7 | -100.0 |  |
| pin_rlm+pin_value | close | pin $2k+ | 0-2 | 0.0 | -42.3 | -100.0 |  |
| consensus_gap+follow_move | close | pin $2k+ | 1-0 | 100.0 | 68.3 | 118.0 |  |
| money_level+money_moving | close | pin limit <$1k | 6-5 | 54.5 | 3.3 | 3.8 |  |
| money_level+sharp_gap | close | pin limit <$1k | 6-5 | 54.5 | 3.3 | 3.8 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 7-7 | 50.0 | 2.0 | -4.8 |  |
| follow_move+money_level | close | pin limit <$1k | 3-3 | 50.0 | 0.0 | -4.5 |  |
| follow_move+money_moving | close | pin limit <$1k | 4-5 | 44.4 | -0.9 | -15.2 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 2-3 | 40.0 | -1.7 | -23.6 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 4-5 | 44.4 | -0.9 | -15.2 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 2-3 | 40.0 | -1.7 | -23.6 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 2-3 | 40.0 | -1.7 | -23.6 |  |
| money_level+pin_rlm | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.5 |  |
| money_level+pin_value | close | pin limit <$1k | 2-0 | 100.0 | 36.1 | 88.9 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 2-2 | 50.0 | 6.9 | -5.5 |  |
| money_moving+pin_value | close | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 2-2 | 50.0 | 6.9 | -5.5 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 1-2 | 33.3 | -2.8 | -36.4 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 1-2 | 33.3 | -2.8 | -36.4 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 1-0 | 100.0 | 63.9 | 90.9 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 1-0 | 100.0 | 63.9 | 90.9 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 63.9 | 90.9 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 1-0 | 100.0 | 63.9 | 90.9 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 1-0 | 100.0 | 63.9 | 90.9 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 1-0 | 100.0 | 63.9 | 90.9 |  |
| follow_move+pin_value | close | pin limit <$1k | 2-0 | 100.0 | 63.9 | 90.9 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 1-0 | 100.0 | 63.9 | 90.9 |  |
| pin_rlm | early | <1k bets | 0-1 | 0.0 | -31.7 | -100.0 | 1.3 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -31.7 | -100.0 | 1.3 |
| follow_move | early | <1k bets | 57-39 | 59.4 | 6.8 | -0.9 | 0.07 |
| follow_move | early | pin $1-2k | 8-1 | 88.9 | 29.4 | 38.7 | -0.7 |
| follow_move | early | pin limit <$1k | 6-4 | 60.0 | 6.8 | 7.2 | 0.7 |
| rlm_ratio | early | <1k bets | 4-0 | 100.0 | 59.1 | 124.5 | 1.62 |
| rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 36.1 | 95.2 | 1.0 |
| money_level | early | <1k bets | 17-9 | 65.4 | -0.3 | -4.5 | -0.9 |
| money_level | early | pin $1-2k | 5-0 | 100.0 | 31.7 | 35.3 | 0.22 |
| money_level | early | pin limit <$1k | 2-2 | 50.0 | -6.9 | -3.5 | -0.75 |
| sharp_gap | early | <1k bets | 14-11 | 56.0 | 4.3 | 0.3 | -0.18 |
| sharp_gap | early | pin $1-2k | 3-2 | 60.0 | 6.3 | -21.8 | 0.46 |
| sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | -6.9 | -3.5 | -0.75 |
| money_moving | early | <1k bets | 14-7 | 66.7 | 16.7 | 12.0 | -0.74 |
| money_moving | early | pin $1-2k | 2-2 | 50.0 | 0.0 | -44.9 | -0.2 |
| money_moving | early | pin limit <$1k | 3-0 | 100.0 | 54.6 | 92.3 | 1.0 |
| pin_value | early | <1k bets | 6-6 | 50.0 | -1.4 | -6.3 | -0.21 |
| pin_value | early | pin $1-2k | 2-4 | 33.3 | -16.7 | -39.9 | -0.08 |
| pin_value | early | pin limit <$1k | 4-2 | 66.7 | 13.9 | 27.3 | -0.33 |
| consensus_gap | early | <1k bets | 27-23 | 54.0 | 5.1 | 27.4 | 0.63 |
| consensus_gap | early | pin $1-2k | 2-3 | 40.0 | -6.3 | -31.6 | 0.6 |
| consensus_gap | early | pin limit <$1k | 1-1 | 50.0 | 7.7 | -4.5 | -0.4 |
| money_level+money_moving | early | <1k bets | 9-2 | 81.8 | 17.3 | 19.0 | -1.57 |
| money_level+sharp_gap | early | <1k bets | 10-5 | 66.7 | 2.3 | 7.6 | -0.93 |
| money_moving+sharp_gap | early | <1k bets | 9-5 | 64.3 | 14.0 | 15.7 | -0.84 |
| consensus_gap+money_moving | early | <1k bets | 0-2 | 0.0 | -31.7 | -100.0 | -1.4 |
| consensus_gap+sharp_gap | early | <1k bets | 3-5 | 37.5 | -3.4 | -27.0 | 1.09 |
| follow_move+money_level | early | <1k bets | 10-4 | 71.4 | 4.1 | -8.3 | -0.54 |
| follow_move+money_moving | early | <1k bets | 8-3 | 72.7 | 17.0 | 19.7 | -0.23 |
| follow_move+rlm_ratio | early | <1k bets | 4-0 | 100.0 | 59.1 | 124.5 | 1.62 |
| follow_move+sharp_gap | early | <1k bets | 6-3 | 66.7 | 11.1 | 24.3 | 0.21 |
| money_moving+rlm_ratio | early | <1k bets | 3-0 | 100.0 | 56.1 | 122.0 | 0.67 |
| rlm_ratio+sharp_gap | early | <1k bets | 4-0 | 100.0 | 59.1 | 124.5 | 1.62 |
| consensus_gap+follow_move | early | <1k bets | 4-1 | 80.0 | 33.7 | 56.3 | 2.86 |
| consensus_gap+pin_value | early | <1k bets | 2-1 | 66.7 | 15.7 | 20.8 | -0.17 |
| money_level+pin_value | early | <1k bets | 1-1 | 50.0 | 0.0 | -4.5 | -0.5 |
| pin_value+sharp_gap | early | <1k bets | 1-1 | 50.0 | 0.0 | -4.5 | -0.5 |
| consensus_gap+money_level | early | <1k bets | 2-1 | 66.7 | -1.6 | 17.5 | 1.17 |
| money_moving+pin_value | early | <1k bets | 1-0 | 100.0 | 63.9 | 90.9 | -1.0 |
| money_level+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 36.1 | 95.2 | 1.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -31.7 | -100.0 | 1.3 |
| pin_rlm+sharp_gap | early | <1k bets | 0-1 | 0.0 | -31.7 | -100.0 | 1.3 |
| follow_move+pin_value | early | <1k bets | 2-0 | 100.0 | 42.3 | 80.3 | -0.75 |
| consensus_gap+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 68.3 | 132.0 | 4.5 |
| consensus_gap+money_level | early | pin $1-2k | 1-0 | 100.0 | 31.7 | 70.4 | 2.9 |
| consensus_gap+sharp_gap | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -14.8 | 1.1 |
| money_level+sharp_gap | early | pin $1-2k | 3-0 | 100.0 | 31.7 | 30.4 | 0.57 |
| follow_move+money_level | early | pin $1-2k | 4-0 | 100.0 | 31.7 | 26.5 | -0.45 |
| follow_move+money_moving | early | pin $1-2k | 2-0 | 100.0 | 31.7 | 10.2 | 0.35 |
| money_level+money_moving | early | pin $1-2k | 2-0 | 100.0 | 31.7 | 10.2 | 0.35 |
| follow_move+sharp_gap | early | pin $1-2k | 2-0 | 100.0 | 31.7 | 10.4 | -0.6 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -31.7 | -100.0 | 1.3 |
| money_moving+sharp_gap | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -45.9 | 0.65 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -31.7 | -100.0 | 1.3 |
| follow_move+pin_value | early | pin $1-2k | 2-0 | 100.0 | 42.3 | 80.3 | -0.75 |
| consensus_gap+follow_move | early | pin $1-2k | 1-0 | 100.0 | 31.7 | 71.4 | -0.5 |
| consensus_gap+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -14.3 | -0.25 |
| consensus_gap+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 47.2 | 90.9 | 0.0 |
| money_level+pin_value | early | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 | -0.5 |
| money_level+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | -6.9 | -3.5 | -0.75 |
| pin_value+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 | -0.5 |
| money_level+money_moving | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 93.0 | 0.0 |
| money_moving+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 63.9 | 90.9 | -1.0 |
| money_moving+sharp_gap | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 93.0 | 0.0 |
| follow_move+money_level | early | pin limit <$1k | 1-0 | 100.0 | 36.1 | 95.2 | 1.0 |
| follow_move+money_moving | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 93.0 | 2.0 |
| follow_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 36.1 | 95.2 | 1.0 |
| follow_move+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 36.1 | 95.2 | 1.0 |
| money_level+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 36.1 | 95.2 | 1.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 36.1 | 95.2 | 1.0 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 36.1 | 95.2 | 1.0 |
