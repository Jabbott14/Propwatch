# CBB scorecard

Generated 2026-11-12 23:53 UTC. 340 graded games (11 finished games had no final score matched and are not graded).

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before tip. Break-even at -110 is 52.4%. CLV = points of closing-line
value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured
on this sample. `edge` is hit% minus that. A signal that is structurally long
favourites or overs beats 50% whenever those run, which is not an edge -- this
sample ran **49.7% favourites** (n=340) and **49.4% overs** (n=340) and **76.4% moneyline favourites** (n=284).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

## EARLY

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 1-1 | 50.0 | 23.6 | 26.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | both | 144-141 | 50.5 | 49.9 | 0.6 | -9.52 | -3.3 | 0.19 | 39.6 | no edge shown yet |
| rlm_ratio | both | 6-4 | 60.0 | 50.4 | 9.6 | +1.61 | 16.1 | -0.2 | 20.0 | keep collecting (10/30) |
| money_level | both | 87-50 | 63.5 | 59.6 | 3.9 | +3.49 | 2.5 | 0.39 | 43.8 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 71-56 | 55.9 | 48.1 | 7.8 | +21.43 | 16.9 | 0.44 | 41.7 | no edge shown yet |
| money_moving | both | 53-33 | 61.6 | 51.5 | 10.1 | +9.53 | 11.1 | 0.1 | 41.9 | PROMOTE: beats break-even and its own base rate |
| pin_value | both | 43-41 | 51.2 | 48.1 | 3.1 | -2.68 | -3.2 | 0.15 | 41.7 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 50.2 | -30.2 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 121-170 | 41.6 | 46.1 | -4.5 | -45.09 | -15.5 | 0.32 | 46.7 | DROP: below break-even |
| consensus_gap+money_level | both | 17-18 | 48.6 | 62.7 | -14.2 | -9.16 | -26.2 | 0.6 | 51.4 | no edge shown yet |
| consensus_gap+money_moving | both | 12-13 | 48.0 | 44.6 | 3.4 | +0.55 | 2.2 | 0.24 | 40.0 | keep collecting (25/30) |
| consensus_gap+pin_value | both | 17-26 | 39.5 | 46.2 | -6.7 | -11.16 | -26.0 | 0.46 | 53.5 | DROP: below break-even |
| follow_move+rlm_ratio | both | 6-4 | 60.0 | 50.4 | 9.6 | +1.61 | 16.1 | -0.2 | 20.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 22-14 | 61.1 | 50.0 | 11.2 | +5.98 | 16.6 | 0.39 | 36.1 | no edge shown yet |
| money_level+money_moving | both | 37-18 | 67.3 | 58.1 | 9.2 | +5.7 | 10.4 | 0.03 | 45.5 | PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | both | 10-8 | 55.6 | 50.1 | 5.4 | +0.9 | 5.0 | 0.5 | 50.0 | keep collecting (18/30) |
| money_moving+pin_value | both | 7-5 | 58.3 | 50.0 | 8.3 | +1.13 | 9.4 | 0.42 | 41.7 | keep collecting (12/30) |
| rlm_ratio+sharp_gap | both | 6-4 | 60.0 | 50.4 | 9.6 | +1.61 | 16.1 | -0.2 | 20.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 53-29 | 64.6 | 55.1 | 9.5 | +9.31 | 11.4 | 0.7 | 47.6 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 33-21 | 61.1 | 48.5 | 12.6 | +9.27 | 17.2 | 0.25 | 42.6 | no edge shown yet |
| pin_value+sharp_gap | both | 12-7 | 63.2 | 48.7 | 14.5 | +3.75 | 19.8 | -0.15 | 36.8 | keep collecting (19/30) |
| consensus_gap+follow_move | both | 12-13 | 48.0 | 49.8 | -1.8 | -2.63 | -10.5 | 0.92 | 48.0 | keep collecting (25/30) |
| consensus_gap+sharp_gap | both | 13-24 | 35.1 | 42.8 | -7.7 | +1.39 | 3.8 | 0.86 | 48.6 | DROP: below break-even |
| follow_move+money_level | both | 24-15 | 61.5 | 49.8 | 11.7 | +6.82 | 17.5 | 0.49 | 41.0 | no edge shown yet |
| follow_move+pin_value | both | 18-15 | 54.5 | 49.9 | 4.7 | +0.8 | 2.4 | 0.03 | 30.3 | no edge shown yet |
| money_level+rlm_ratio | both | 6-1 | 85.7 | 50.5 | 35.3 | +4.61 | 65.9 | 0.14 | 14.3 | keep collecting (7/30) |
| pin_value+rlm_ratio | both | 2-1 | 66.7 | 50.2 | 16.5 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| follow_move+money_moving | both | 15-7 | 68.2 | 49.9 | 18.3 | +6.67 | 30.3 | 0.05 | 31.8 | keep collecting (22/30) |
| money_moving+rlm_ratio | both | 3-1 | 75.0 | 50.2 | 24.8 | +1.81 | 45.3 | -0.75 | 0.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | both | 1-1 | 50.0 | 23.6 | 26.4 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 50.4 | -50.4 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 50.6 | -50.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 0-1 | 0.0 | 50.6 | -50.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 23.6 | 76.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-1 | 50.0 | 23.6 | 26.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | spread | 69-73 | 48.6 | 49.9 | -1.3 | -10.07 | -7.1 | 0.06 | 35.9 | no edge shown yet |
| follow_move | total | 75-68 | 52.4 | 50.0 | 2.5 | +0.55 | 0.4 | 0.31 | 43.4 | no edge shown yet |
| rlm_ratio | spread | 2-2 | 50.0 | 50.3 | -0.3 | -0.07 | -1.7 | -0.25 | 0.0 | keep collecting (4/30) |
| rlm_ratio | total | 4-2 | 66.7 | 50.4 | 16.3 | +1.68 | 28.0 | -0.17 | 33.3 | keep collecting (6/30) |
| money_level | moneyline | 41-19 | 68.3 | 72.0 | -3.7 | -7.2 | -12.0 | 0.31 | 50.0 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 15-14 | 51.7 | 49.9 | 1.8 | -0.54 | -1.9 | 0.86 | 44.8 | keep collecting (29/30) |
| money_level | total | 31-17 | 64.6 | 49.8 | 14.8 | +11.22 | 23.4 | 0.21 | 35.4 | PROMOTE: beats break-even and its own base rate |
| sharp_gap | moneyline | 28-23 | 54.9 | 45.3 | 9.6 | +15.41 | 30.2 | 0.5 | 52.9 | no edge shown yet |
| sharp_gap | spread | 16-14 | 53.3 | 50.0 | 3.3 | +0.41 | 1.4 | 0.63 | 33.3 | no edge shown yet |
| sharp_gap | total | 27-19 | 58.7 | 50.1 | 8.6 | +5.61 | 12.2 | 0.24 | 34.8 | no edge shown yet |
| money_moving | moneyline | 20-17 | 54.1 | 53.6 | 0.5 | -4.28 | -11.6 | 0.13 | 56.8 | no edge shown yet |
| money_moving | spread | 15-4 | 78.9 | 49.9 | 29.0 | +9.42 | 49.6 | 0.21 | 36.8 | keep collecting (19/30) |
| money_moving | total | 18-12 | 60.0 | 50.0 | 10.0 | +4.39 | 14.6 | 0.0 | 26.7 | no edge shown yet |
| pin_value | moneyline | 1-5 | 16.7 | 23.6 | -6.9 | -4.02 | -67.0 | -0.02 | 66.7 | keep collecting (6/30) |
| pin_value | spread | 22-17 | 56.4 | 49.9 | 6.5 | +2.35 | 6.0 | 0.28 | 41.0 | no edge shown yet |
| pin_value | total | 20-19 | 51.3 | 50.0 | 1.3 | -1.01 | -2.6 | 0.05 | 38.5 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 50.3 | -17.0 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 45-92 | 32.8 | 41.7 | -8.9 | -34.15 | -24.9 | 0.05 | 43.1 | DROP: below break-even |
| consensus_gap | spread | 42-35 | 54.5 | 49.9 | 4.6 | +1.57 | 2.0 | 0.51 | 48.1 | no edge shown yet |
| consensus_gap | total | 34-43 | 44.2 | 49.9 | -5.8 | -12.5 | -16.2 | 0.62 | 51.9 | no edge shown yet |
| money_level+sharp_gap | moneyline | 20-6 | 76.9 | 66.3 | 10.7 | +2.39 | 9.2 | 0.88 | 69.2 | keep collecting (26/30) |
| consensus_gap+pin_value | moneyline | 1-5 | 16.7 | 23.6 | -6.9 | -4.02 | -67.0 | -0.02 | 66.7 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_level+money_moving | moneyline | 14-7 | 66.7 | 71.4 | -4.7 | -4.27 | -20.3 | -0.53 | 52.4 | keep collecting (21/30) |
| consensus_gap+sharp_gap | moneyline | 7-15 | 31.8 | 38.0 | -6.2 | +5.17 | 23.5 | 0.9 | 54.5 | keep collecting (22/30) |
| consensus_gap+money_level | moneyline | 11-10 | 52.4 | 71.4 | -19.0 | -6.35 | -30.2 | 0.23 | 52.4 | keep collecting (21/30) |
| money_moving+sharp_gap | moneyline | 12-11 | 52.2 | 46.6 | 5.6 | +0.24 | 1.0 | 0.28 | 60.9 | keep collecting (23/30) |
| consensus_gap+money_moving | moneyline | 5-12 | 29.4 | 42.2 | -12.8 | -4.5 | -26.5 | 0.3 | 52.9 | keep collecting (17/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | moneyline | 1-1 | 50.0 | 23.6 | 26.4 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 23.6 | -23.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 23.6 | 76.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 4-5 | 44.4 | 49.7 | -5.3 | -1.59 | -17.7 | 1.67 | 66.7 | keep collecting (9/30) |
| consensus_gap+money_moving | spread | 4-0 | 100.0 | 49.7 | 50.3 | +3.41 | 85.2 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_value | spread | 9-8 | 52.9 | 49.8 | 3.1 | -0.31 | -1.8 | 0.53 | 52.9 | keep collecting (17/30) |
| follow_move+rlm_ratio | spread | 2-2 | 50.0 | 50.3 | -0.3 | -0.07 | -1.7 | -0.25 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 8-6 | 57.1 | 49.9 | 7.3 | +1.23 | 8.8 | 0.79 | 35.7 | keep collecting (14/30) |
| money_level+money_moving | spread | 8-4 | 66.7 | 49.9 | 16.8 | +3.27 | 27.2 | 0.75 | 58.3 | keep collecting (12/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 49.9 | -7.0 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.9 | 10.1 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | spread | 2-2 | 50.0 | 50.3 | -0.3 | -0.07 | -1.7 | -0.25 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 12-11 | 52.2 | 49.9 | 2.3 | -0.23 | -1.0 | 0.96 | 39.1 | keep collecting (23/30) |
| money_moving+sharp_gap | spread | 7-3 | 70.0 | 49.9 | 20.1 | +3.27 | 32.7 | 0.6 | 40.0 | keep collecting (10/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.9 | 16.8 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 8-7 | 53.3 | 49.8 | 3.5 | -0.18 | -1.2 | 0.87 | 40.0 | keep collecting (15/30) |
| consensus_gap+sharp_gap | spread | 3-3 | 50.0 | 49.7 | 0.3 | -0.43 | -7.1 | 2.17 | 66.7 | keep collecting (6/30) |
| follow_move+money_level | spread | 10-7 | 58.8 | 49.8 | 9.0 | +2.1 | 12.3 | 0.76 | 41.2 | keep collecting (17/30) |
| follow_move+pin_value | spread | 11-7 | 61.1 | 49.9 | 11.2 | +2.56 | 14.2 | 0.33 | 33.3 | keep collecting (18/30) |
| follow_move+money_moving | spread | 7-1 | 87.5 | 49.8 | 37.7 | +5.37 | 67.2 | 0.38 | 37.5 | keep collecting (8/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 50.3 | 16.4 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 1-0 | 100.0 | 50.3 | 49.7 | +0.95 | 95.2 | 0.0 | 0.0 | keep collecting (1/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 50.3 | -50.3 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 15-7 | 68.2 | 49.9 | 18.3 | +6.7 | 30.4 | 0.18 | 31.8 | keep collecting (22/30) |
| money_level+sharp_gap | total | 21-12 | 63.6 | 49.9 | 13.7 | +7.15 | 21.7 | 0.39 | 36.4 | no edge shown yet |
| money_moving+sharp_gap | total | 14-7 | 66.7 | 50.0 | 16.6 | +5.75 | 27.4 | 0.05 | 23.8 | keep collecting (21/30) |
| money_level+pin_value | total | 7-4 | 63.6 | 50.3 | 13.4 | +2.32 | 21.1 | 0.36 | 36.4 | keep collecting (11/30) |
| money_moving+pin_value | total | 4-3 | 57.1 | 50.1 | 7.1 | +0.56 | 8.0 | 0.29 | 28.6 | keep collecting (7/30) |
| pin_value+sharp_gap | total | 10-5 | 66.7 | 50.1 | 16.5 | +4.01 | 26.7 | 0.0 | 33.3 | keep collecting (15/30) |
| follow_move+money_level | total | 14-8 | 63.6 | 49.8 | 13.8 | +4.72 | 21.5 | 0.27 | 40.9 | keep collecting (22/30) |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.9 | -3.2 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 4-2 | 66.7 | 50.4 | 16.3 | +1.68 | 28.0 | -0.17 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 14-8 | 63.6 | 50.0 | 13.6 | +4.75 | 21.6 | 0.14 | 36.4 | keep collecting (22/30) |
| money_level+rlm_ratio | total | 4-0 | 100.0 | 50.6 | 49.4 | +3.68 | 92.0 | 0.25 | 25.0 | keep collecting (4/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 50.2 | 16.5 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 4-2 | 66.7 | 50.4 | 16.3 | +1.68 | 28.0 | -0.17 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 8-6 | 57.1 | 49.9 | 7.2 | +1.29 | 9.2 | -0.14 | 28.6 | keep collecting (14/30) |
| consensus_gap+money_level | total | 2-3 | 40.0 | 49.9 | -9.9 | -1.22 | -24.4 | 0.2 | 20.0 | keep collecting (5/30) |
| consensus_gap+money_moving | total | 3-1 | 75.0 | 49.7 | 25.3 | +1.65 | 41.2 | 0.0 | 0.0 | keep collecting (4/30) |
| consensus_gap+pin_value | total | 7-13 | 35.0 | 49.9 | -14.9 | -6.83 | -34.2 | 0.55 | 50.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | total | 3-6 | 33.3 | 50.1 | -16.7 | -3.35 | -37.2 | -0.11 | 22.2 | keep collecting (9/30) |
| money_moving+rlm_ratio | total | 2-1 | 66.7 | 50.2 | 16.5 | +0.86 | 28.7 | -1.0 | 0.0 | keep collecting (3/30) |
| consensus_gap+follow_move | total | 4-6 | 40.0 | 49.8 | -9.8 | -2.44 | -24.4 | 1.0 | 60.0 | keep collecting (10/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 50.6 | -50.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 50.6 | -50.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 0-1 | 0.0 | 50.6 | -50.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |

## CLOSE

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 63-64 | 49.6 | 41.2 | 8.4 | +21.43 | 16.9 |  |  | no edge shown yet |
| follow_move | both | 284-281 | 50.3 | 49.9 | 0.3 | -24.1 | -4.3 |  |  | no edge shown yet |
| rlm_ratio | both | 79-61 | 56.4 | 50.2 | 6.3 | +10.72 | 7.7 |  |  | no edge shown yet |
| money_level | both | 530-396 | 57.2 | 56.4 | 0.8 | -41.82 | -4.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 393-500 | 44.0 | 46.4 | -2.4 | -75.69 | -8.5 |  |  | DROP: below break-even |
| money_moving | both | 390-503 | 43.7 | 46.9 | -3.2 | -89.09 | -10.0 |  |  | DROP: below break-even |
| pin_value | both | 188-173 | 52.1 | 47.6 | 4.5 | +12.66 | 3.5 |  |  | no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 50.1 | 16.6 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 215-297 | 42.0 | 46.5 | -4.5 | -51.11 | -10.0 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 52-46 | 53.1 | 49.7 | 3.4 | -1.04 | -1.1 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 89-165 | 35.0 | 42.8 | -7.8 | -19.82 | -7.8 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 15-24 | 38.5 | 37.1 | 1.4 | +8.14 | 20.9 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 91-104 | 46.7 | 45.6 | 1.1 | -5.66 | -2.9 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | both | 14-10 | 58.3 | 49.8 | 8.6 | +2.2 | 9.2 |  |  | keep collecting (24/30) |
| consensus_gap+sharp_gap | both | 90-169 | 34.7 | 42.3 | -7.6 | -20.65 | -8.0 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 185-209 | 47.0 | 49.9 | -3.0 | -42.35 | -10.7 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 40-30 | 57.1 | 50.3 | 6.9 | +6.5 | 9.3 |  |  | no edge shown yet |
| follow_move+pin_value | both | 72-50 | 59.0 | 49.8 | 9.2 | +13.4 | 11.0 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 79-61 | 56.4 | 50.2 | 6.3 | +10.72 | 7.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 189-206 | 47.8 | 49.9 | -2.1 | -35.49 | -9.0 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 60-64 | 48.4 | 41.0 | 7.4 | +18.69 | 15.1 |  |  | no edge shown yet |
| money_moving+pin_value | both | 75-93 | 44.6 | 46.0 | -1.3 | -10.25 | -6.1 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 76-60 | 55.9 | 50.2 | 5.7 | +8.88 | 6.5 |  |  | no edge shown yet |
| money_moving+sharp_gap | both | 375-483 | 43.7 | 46.5 | -2.8 | -78.05 | -9.1 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 21-16 | 56.8 | 44.4 | 12.3 | +10.18 | 27.5 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 40-30 | 57.1 | 50.3 | 6.9 | +6.5 | 9.3 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 63-64 | 49.6 | 41.2 | 8.4 | +21.43 | 16.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 21-13 | 61.8 | 50.0 | 11.7 | +5.8 | 17.1 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 77-93 | 45.3 | 45.9 | -0.6 | -8.49 | -5.0 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 79-61 | 56.4 | 50.2 | 6.3 | +10.72 | 7.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+money_moving | both | 278-274 | 50.4 | 52.3 | -2.0 | -41.12 | -7.5 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 277-270 | 50.6 | 52.1 | -1.4 | -34.16 | -6.2 |  |  | no edge shown yet |
| follow_move+money_level | both | 167-178 | 48.4 | 49.8 | -1.4 | -27.95 | -8.1 |  |  | no edge shown yet |
| money_level+rlm_ratio | both | 34-31 | 52.3 | 50.1 | 2.3 | -0.49 | -0.8 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 133-106 | 55.6 | 58.0 | -2.3 | -8.29 | -3.5 |  |  | no edge shown yet |
| money_level+pin_value | both | 89-82 | 52.0 | 50.1 | 2.0 | -5.35 | -3.1 |  |  | no edge shown yet |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | both | 25-18 | 58.1 | 46.5 | 11.6 | +6.3 | 14.6 |  |  | no edge shown yet |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 50.6 | 49.4 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 17-30 | 36.2 | 25.8 | 10.3 | +13.6 | 28.9 |  |  | DROP: below break-even |
| pin_rlm | spread | 14-12 | 53.8 | 50.1 | 3.7 | +0.63 | 2.4 |  |  | keep collecting (26/30) |
| pin_rlm | total | 32-22 | 59.3 | 50.4 | 8.9 | +7.2 | 13.3 |  |  | no edge shown yet |
| follow_move | spread | 129-134 | 49.0 | 49.9 | -0.8 | -18.06 | -6.9 |  |  | no edge shown yet |
| follow_move | total | 155-147 | 51.3 | 50.0 | 1.4 | -6.04 | -2.0 |  |  | no edge shown yet |
| rlm_ratio | spread | 23-24 | 48.9 | 50.0 | -1.1 | -3.19 | -6.8 |  |  | no edge shown yet |
| rlm_ratio | total | 56-37 | 60.2 | 50.2 | 10.0 | +13.91 | 15.0 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level | moneyline | 211-67 | 75.9 | 71.8 | 4.1 | -0.1 | -0.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 158-158 | 50.0 | 49.9 | 0.1 | -16.57 | -5.2 |  |  | no edge shown yet |
| money_level | total | 161-171 | 48.5 | 49.8 | -1.3 | -25.15 | -7.6 |  |  | no edge shown yet |
| sharp_gap | moneyline | 83-173 | 32.4 | 37.6 | -5.2 | -28.69 | -11.2 |  |  | DROP: below break-even |
| sharp_gap | spread | 159-152 | 51.1 | 49.9 | 1.2 | -9.42 | -3.0 |  |  | no edge shown yet |
| sharp_gap | total | 151-175 | 46.3 | 50.1 | -3.7 | -37.58 | -11.5 |  |  | DROP: below break-even |
| money_moving | moneyline | 87-167 | 34.3 | 39.0 | -4.7 | -26.58 | -10.5 |  |  | DROP: below break-even |
| money_moving | spread | 156-155 | 50.2 | 49.9 | 0.2 | -15.29 | -4.9 |  |  | no edge shown yet |
| money_moving | total | 147-181 | 44.8 | 50.0 | -5.2 | -47.22 | -14.4 |  |  | DROP: below break-even |
| pin_value | moneyline | 9-29 | 23.7 | 27.8 | -4.1 | -1.86 | -4.9 |  |  | DROP: below break-even |
| pin_value | spread | 90-60 | 60.0 | 50.0 | 10.0 | +18.61 | 12.4 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_value | total | 89-84 | 51.4 | 49.9 | 1.6 | -4.09 | -2.4 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 50.3 | 49.7 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 82-171 | 32.4 | 43.2 | -10.8 | -41.07 | -16.2 |  |  | DROP: below break-even |
| consensus_gap | spread | 63-49 | 56.2 | 49.9 | 6.4 | +4.82 | 4.3 |  |  | no edge shown yet |
| consensus_gap | total | 70-77 | 47.6 | 49.7 | -2.1 | -14.85 | -10.1 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 60-35 | 63.2 | 64.2 | -1.0 | +1.85 | 1.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 55-34 | 61.8 | 63.4 | -1.6 | +2.17 | 2.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 78-162 | 32.5 | 37.7 | -5.2 | -25.13 | -10.5 |  |  | DROP: below break-even |
| consensus_gap+money_level | moneyline | 59-33 | 64.1 | 71.2 | -7.1 | +0.37 | 0.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 27-99 | 21.4 | 35.7 | -14.3 | -7.6 | -6.0 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 28-104 | 21.2 | 35.2 | -14.0 | -9.45 | -7.2 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | moneyline | 7-16 | 30.4 | 28.2 | 2.3 | +9.23 | 40.1 |  |  | keep collecting (23/30) |
| money_moving+pin_rlm | moneyline | 17-30 | 36.2 | 25.8 | 10.3 | +13.6 | 28.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 17-30 | 36.2 | 25.8 | 10.3 | +13.6 | 28.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 9-28 | 24.3 | 27.9 | -3.5 | -0.86 | -2.3 |  |  | DROP: below break-even |
| money_moving+pin_value | moneyline | 4-21 | 16.0 | 23.6 | -7.6 | -0.65 | -2.6 |  |  | keep collecting (25/30) |
| pin_rlm+pin_value | moneyline | 2-6 | 25.0 | 23.6 | 1.4 | +3.15 | 39.4 |  |  | keep collecting (8/30) |
| pin_value+sharp_gap | moneyline | 4-22 | 15.4 | 23.6 | -8.2 | -1.65 | -6.3 |  |  | keep collecting (26/30) |
| money_level+pin_rlm | moneyline | 5-3 | 62.5 | 30.2 | 32.3 | +3.4 | 42.5 |  |  | keep collecting (8/30) |
| money_level+pin_value | moneyline | 3-1 | 75.0 | 63.2 | 11.8 | +0.31 | 7.8 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 26-19 | 57.8 | 49.8 | 8.0 | +3.08 | 6.8 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 34-28 | 54.8 | 49.9 | 5.0 | +1.04 | 1.7 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 44-29 | 60.3 | 49.9 | 10.4 | +8.48 | 11.6 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.33 | -38.9 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | spread | 33-28 | 54.1 | 49.9 | 4.2 | +0.14 | 0.2 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 85-90 | 48.6 | 49.8 | -1.3 | -14.1 | -8.1 |  |  | no edge shown yet |
| follow_move+pin_rlm | spread | 12-12 | 50.0 | 50.1 | -0.1 | -1.13 | -4.7 |  |  | keep collecting (24/30) |
| follow_move+pin_value | spread | 34-19 | 64.2 | 49.8 | 14.3 | +10.38 | 19.6 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+rlm_ratio | spread | 23-24 | 48.9 | 50.0 | -1.1 | -3.19 | -6.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 86-89 | 49.1 | 49.9 | -0.7 | -11.97 | -6.8 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 12-12 | 50.0 | 50.1 | -0.1 | -1.2 | -5.0 |  |  | keep collecting (24/30) |
| money_moving+pin_value | spread | 40-32 | 55.6 | 49.9 | 5.7 | +2.54 | 3.5 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 21-23 | 47.7 | 50.0 | -2.3 | -4.12 | -9.4 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 151-147 | 50.7 | 49.9 | 0.7 | -11.79 | -4.0 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 6-3 | 66.7 | 50.0 | 16.6 | +2.21 | 24.5 |  |  | keep collecting (9/30) |
| pin_rlm+rlm_ratio | spread | 12-12 | 50.0 | 50.1 | -0.1 | -1.13 | -4.7 |  |  | keep collecting (24/30) |
| pin_rlm+sharp_gap | spread | 14-12 | 53.8 | 50.1 | 3.7 | +0.63 | 2.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 4-3 | 57.1 | 50.0 | 7.2 | +0.45 | 6.5 |  |  | keep collecting (7/30) |
| pin_value+sharp_gap | spread | 40-32 | 55.6 | 49.9 | 5.6 | +2.48 | 3.4 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 23-24 | 48.9 | 50.0 | -1.1 | -3.19 | -6.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 84-86 | 49.4 | 49.8 | -0.4 | -11.0 | -6.5 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 10-12 | 45.5 | 50.0 | -4.5 | -3.13 | -14.2 |  |  | keep collecting (22/30) |
| money_level+sharp_gap | spread | 124-118 | 51.2 | 49.9 | 1.4 | -7.14 | -2.9 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 42-32 | 56.8 | 49.8 | 6.9 | +3.96 | 5.4 |  |  | no edge shown yet |
| money_level+money_moving | spread | 123-119 | 50.8 | 49.9 | 1.0 | -9.06 | -3.7 |  |  | no edge shown yet |
| money_level+pin_value | spread | 47-37 | 56.0 | 49.9 | 6.1 | +3.54 | 4.2 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 7-5 | 58.3 | 50.0 | 8.3 | +1.16 | 9.7 |  |  | keep collecting (12/30) |
| money_level+money_moving | total | 95-120 | 44.2 | 49.9 | -5.7 | -33.92 | -15.8 |  |  | DROP: below break-even |
| money_level+sharp_gap | total | 98-118 | 45.4 | 49.9 | -4.5 | -29.19 | -13.5 |  |  | DROP: below break-even |
| money_moving+sharp_gap | total | 146-174 | 45.6 | 50.0 | -4.4 | -41.13 | -12.9 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 32-41 | 43.8 | 49.5 | -5.7 | -12.62 | -17.3 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 38-47 | 44.7 | 49.6 | -4.9 | -13.28 | -15.6 |  |  | no edge shown yet |
| follow_move+money_moving | total | 100-119 | 45.7 | 50.0 | -4.3 | -28.24 | -12.9 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 103-117 | 46.8 | 50.0 | -3.2 | -23.51 | -10.7 |  |  | DROP: below break-even |
| money_level+pin_value | total | 39-44 | 47.0 | 49.7 | -2.7 | -9.19 | -11.1 |  |  | no edge shown yet |
| follow_move+money_level | total | 83-92 | 47.4 | 49.8 | -2.4 | -16.94 | -9.7 |  |  | no edge shown yet |
| follow_move+pin_value | total | 38-31 | 55.1 | 49.8 | 5.3 | +3.02 | 4.4 |  |  | no edge shown yet |
| money_moving+pin_value | total | 31-40 | 43.7 | 49.9 | -6.3 | -12.14 | -17.1 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 33-39 | 45.8 | 50.0 | -4.1 | -9.32 | -12.9 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 28-38 | 42.4 | 49.7 | -7.2 | -13.25 | -20.1 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | total | 29-37 | 43.9 | 49.7 | -5.7 | -11.34 | -17.2 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 26-27 | 49.1 | 49.6 | -0.5 | -4.12 | -7.8 |  |  | no edge shown yet |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pin_rlm | total | 5-5 | 50.0 | 49.8 | 0.2 | -0.6 | -6.0 |  |  | keep collecting (10/30) |
| consensus_gap+rlm_ratio | total | 12-6 | 66.7 | 49.7 | 17.0 | +4.53 | 25.2 |  |  | keep collecting (18/30) |
| follow_move+pin_rlm | total | 28-18 | 60.9 | 50.3 | 10.5 | +7.62 | 16.6 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 56-37 | 60.2 | 50.2 | 10.0 | +13.91 | 15.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 13-10 | 56.5 | 50.3 | 6.2 | +1.74 | 7.6 |  |  | keep collecting (23/30) |
| money_level+rlm_ratio | total | 24-19 | 55.8 | 50.1 | 5.7 | +2.63 | 6.1 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 31-22 | 58.5 | 50.4 | 8.1 | +6.29 | 11.9 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 55-37 | 59.8 | 50.2 | 9.5 | +13.0 | 14.1 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 13-7 | 65.0 | 50.2 | 14.8 | +4.82 | 24.1 |  |  | keep collecting (20/30) |
| pin_rlm+rlm_ratio | total | 28-18 | 60.9 | 50.3 | 10.5 | +7.62 | 16.6 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 32-22 | 59.3 | 50.4 | 8.9 | +7.2 | 13.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 17-10 | 63.0 | 50.1 | 12.9 | +5.35 | 19.8 |  |  | keep collecting (27/30) |
| rlm_ratio+sharp_gap | total | 56-37 | 60.2 | 50.2 | 10.0 | +13.91 | 15.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 50.6 | 49.4 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_rlm | close | 1-3k bets | 34-39 | 46.6 | 4.3 | 15.1 |  |
| pin_rlm | close | 3k+ bets | 18-18 | 50.0 | 10.9 | 13.0 |  |
| pin_rlm | close | <1k bets | 11-7 | 61.1 | 19.6 | 31.8 |  |
| pin_rlm | close | pin $1-2k | 32-20 | 61.5 | 18.0 | 51.3 |  |
| pin_rlm | close | pin $2k+ | 12-34 | 26.1 | -7.9 | -46.9 |  |
| pin_rlm | close | pin limit <$1k | 19-10 | 65.5 | 17.0 | 56.3 |  |
| follow_move | close | 1-3k bets | 188-178 | 51.4 | 1.4 | -2.2 |  |
| follow_move | close | 3k+ bets | 63-70 | 47.4 | -2.6 | -9.7 |  |
| follow_move | close | <1k bets | 33-33 | 50.0 | 0.1 | -4.9 |  |
| follow_move | close | pin $1-2k | 91-113 | 44.6 | -5.3 | -15.1 |  |
| follow_move | close | pin $2k+ | 48-51 | 48.5 | -1.4 | -7.8 |  |
| follow_move | close | pin limit <$1k | 64-53 | 54.7 | 4.6 | 4.6 |  |
| rlm_ratio | close | 1-3k bets | 54-45 | 54.5 | 4.4 | 3.8 |  |
| rlm_ratio | close | 3k+ bets | 18-14 | 56.2 | 6.1 | 7.8 |  |
| rlm_ratio | close | <1k bets | 7-2 | 77.8 | 27.3 | 49.3 |  |
| rlm_ratio | close | pin $1-2k | 27-23 | 54.0 | 4.0 | 2.4 |  |
| rlm_ratio | close | pin $2k+ | 9-12 | 42.9 | -7.4 | -18.1 |  |
| rlm_ratio | close | pin limit <$1k | 21-14 | 60.0 | 9.6 | 15.3 |  |
| money_level | close | 1-3k bets | 358-227 | 61.2 | 4.5 | 2.5 |  |
| money_level | close | 3k+ bets | 116-106 | 52.3 | -3.7 | -11.1 |  |
| money_level | close | <1k bets | 56-62 | 47.5 | -9.1 | -26.1 |  |
| money_level | close | pin $1-2k | 148-138 | 51.7 | -2.8 | -8.3 |  |
| money_level | close | pin $2k+ | 126-93 | 57.5 | -0.8 | -6.7 |  |
| money_level | close | pin limit <$1k | 64-68 | 48.5 | -2.0 | -8.2 |  |
| sharp_gap | close | 1-3k bets | 247-320 | 43.6 | -3.0 | -11.3 |  |
| sharp_gap | close | 3k+ bets | 97-118 | 45.1 | -0.7 | 2.3 |  |
| sharp_gap | close | <1k bets | 49-61 | 44.5 | -2.6 | -14.4 |  |
| sharp_gap | close | pin $1-2k | 133-146 | 47.7 | -0.4 | -1.4 |  |
| sharp_gap | close | pin $2k+ | 79-131 | 37.6 | -7.3 | -25.5 |  |
| sharp_gap | close | pin limit <$1k | 60-66 | 47.6 | -2.1 | -1.8 |  |
| money_moving | close | 1-3k bets | 245-321 | 43.3 | -3.6 | -12.5 |  |
| money_moving | close | 3k+ bets | 96-121 | 44.2 | -2.3 | -1.2 |  |
| money_moving | close | <1k bets | 49-60 | 45.0 | -2.4 | -13.6 |  |
| money_moving | close | pin $1-2k | 128-151 | 45.9 | -2.4 | -5.0 |  |
| money_moving | close | pin $2k+ | 82-127 | 39.2 | -5.8 | -22.8 |  |
| money_moving | close | pin limit <$1k | 59-68 | 46.5 | -3.2 | -4.0 |  |
| pin_value | close | 1-3k bets | 115-116 | 49.8 | 2.2 | -1.8 |  |
| pin_value | close | 3k+ bets | 40-43 | 48.2 | 0.5 | -1.8 |  |
| pin_value | close | <1k bets | 33-14 | 70.2 | 22.5 | 39.1 |  |
| pin_value | close | pin $1-2k | 90-82 | 52.3 | 4.5 | 3.7 |  |
| pin_value | close | pin $2k+ | 48-50 | 49.0 | 3.6 | -1.8 |  |
| pin_value | close | pin limit <$1k | 50-41 | 54.9 | 5.4 | 9.0 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 49.7 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 49.7 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 135-183 | 42.5 | -4.5 | -12.0 |  |
| consensus_gap | close | 3k+ bets | 54-66 | 45.0 | -2.7 | 6.6 |  |
| consensus_gap | close | <1k bets | 26-47 | 35.6 | -7.5 | -27.3 |  |
| consensus_gap | close | pin $1-2k | 70-79 | 47.0 | -1.0 | 3.1 |  |
| consensus_gap | close | pin $2k+ | 52-63 | 45.2 | -6.1 | -20.6 |  |
| consensus_gap | close | pin limit <$1k | 34-31 | 52.3 | 2.7 | 4.3 |  |
| consensus_gap+follow_move | close | 1-3k bets | 38-28 | 57.6 | 7.9 | 7.5 |  |
| consensus_gap+money_level | close | 1-3k bets | 91-58 | 61.1 | 2.4 | 7.9 |  |
| consensus_gap+money_moving | close | 1-3k bets | 57-105 | 35.2 | -7.8 | -12.5 |  |
| consensus_gap+pin_value | close | 1-3k bets | 57-70 | 44.9 | -0.8 | -8.2 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 57-108 | 34.5 | -8.0 | -13.9 |  |
| follow_move+money_level | close | 1-3k bets | 119-110 | 52.0 | 2.2 | -1.3 |  |
| follow_move+money_moving | close | 1-3k bets | 130-136 | 48.9 | -1.1 | -7.1 |  |
| follow_move+pin_value | close | 1-3k bets | 43-31 | 58.1 | 8.3 | 9.1 |  |
| follow_move+sharp_gap | close | 1-3k bets | 130-134 | 49.2 | -0.7 | -6.4 |  |
| money_level+money_moving | close | 1-3k bets | 184-162 | 53.2 | 0.6 | -0.6 |  |
| money_level+pin_value | close | 1-3k bets | 60-48 | 55.6 | 5.5 | 4.0 |  |
| money_level+sharp_gap | close | 1-3k bets | 184-161 | 53.3 | 1.0 | 0.3 |  |
| money_moving+pin_value | close | 1-3k bets | 49-61 | 44.5 | -1.8 | -9.8 |  |
| money_moving+sharp_gap | close | 1-3k bets | 237-311 | 43.2 | -3.4 | -11.8 |  |
| pin_value+sharp_gap | close | 1-3k bets | 51-63 | 44.7 | -1.5 | -9.7 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 10-17 | 37.0 | -1.2 | 16.9 |  |
| money_level+pin_rlm | close | 1-3k bets | 16-11 | 59.3 | 9.0 | 12.9 |  |
| pin_rlm+pin_value | close | 1-3k bets | 12-11 | 52.2 | 9.0 | 30.6 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 34-39 | 46.6 | 4.3 | 15.1 |  |
| money_moving+pin_rlm | close | 1-3k bets | 32-39 | 45.1 | 3.1 | 13.1 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 13-7 | 65.0 | 15.2 | 21.6 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 54-45 | 54.5 | 4.4 | 3.8 |  |
| money_level+rlm_ratio | close | 1-3k bets | 26-22 | 54.2 | 4.1 | 2.8 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 53-45 | 54.1 | 3.9 | 2.9 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 54-45 | 54.5 | 4.4 | 3.8 |  |
| follow_move+pin_rlm | close | 1-3k bets | 21-21 | 50.0 | -0.3 | -4.8 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 21-21 | 50.0 | -0.3 | -4.8 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 14-9 | 60.9 | 10.9 | 14.9 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 49.4 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 12-12 | 50.0 | 0.3 | -6.9 |  |
| consensus_gap+money_moving | close | 3k+ bets | 21-37 | 36.2 | -6.9 | 18.3 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-5 | 37.5 | -2.5 | 19.3 |  |
| consensus_gap+pin_value | close | 3k+ bets | 25-26 | 49.0 | 2.9 | 4.1 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 1-3 | 25.0 | -24.6 | -53.2 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 22-37 | 37.3 | -5.5 | 22.8 |  |
| follow_move+money_moving | close | 3k+ bets | 39-50 | 43.8 | -6.1 | -16.8 |  |
| follow_move+pin_rlm | close | 3k+ bets | 12-8 | 60.0 | 9.8 | 15.4 |  |
| follow_move+pin_value | close | 3k+ bets | 18-17 | 51.4 | 1.6 | -3.6 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 18-14 | 56.2 | 6.1 | 7.8 |  |
| follow_move+sharp_gap | close | 3k+ bets | 43-49 | 46.7 | -3.2 | -11.0 |  |
| money_moving+pin_rlm | close | 3k+ bets | 17-18 | 48.6 | 9.8 | 10.6 |  |
| money_moving+pin_value | close | 3k+ bets | 17-27 | 38.6 | -6.4 | -11.5 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 16-13 | 55.2 | 5.1 | 5.4 |  |
| money_moving+sharp_gap | close | 3k+ bets | 89-111 | 44.5 | -1.4 | 1.3 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-5 | 50.0 | 5.2 | -5.2 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 12-8 | 60.0 | 9.8 | 15.4 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 18-18 | 50.0 | 10.9 | 13.0 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 4-4 | 50.0 | 0.1 | -4.9 |  |
| pin_value+sharp_gap | close | 3k+ bets | 17-25 | 40.5 | -4.4 | -7.2 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 18-14 | 56.2 | 6.1 | 7.8 |  |
| money_level+money_moving | close | 3k+ bets | 63-71 | 47.0 | -4.6 | -13.9 |  |
| money_level+sharp_gap | close | 3k+ bets | 62-68 | 47.7 | -3.4 | -11.2 |  |
| follow_move+money_level | close | 3k+ bets | 37-43 | 46.2 | -3.5 | -12.3 |  |
| money_level+rlm_ratio | close | 3k+ bets | 7-7 | 50.0 | 0.0 | -5.3 |  |
| consensus_gap+money_level | close | 3k+ bets | 30-30 | 50.0 | -7.7 | -15.3 |  |
| money_level+pin_value | close | 3k+ bets | 20-27 | 42.6 | -7.2 | -21.7 |  |
| money_level+pin_rlm | close | 3k+ bets | 6-6 | 50.0 | 8.8 | 4.6 |  |
| money_level+money_moving | close | <1k bets | 31-40 | 43.7 | -9.2 | -27.5 |  |
| money_level+sharp_gap | close | <1k bets | 31-40 | 43.7 | -9.2 | -27.5 |  |
| money_moving+sharp_gap | close | <1k bets | 49-60 | 45.0 | -2.4 | -13.6 |  |
| consensus_gap+money_level | close | <1k bets | 12-18 | 40.0 | -15.2 | -36.1 |  |
| consensus_gap+money_moving | close | <1k bets | 11-23 | 32.4 | -9.1 | -30.1 |  |
| consensus_gap+pin_value | close | <1k bets | 9-8 | 52.9 | 9.3 | 15.9 |  |
| consensus_gap+sharp_gap | close | <1k bets | 11-24 | 31.4 | -9.5 | -32.1 |  |
| money_level+pin_value | close | <1k bets | 9-7 | 56.2 | 4.8 | 3.6 |  |
| money_moving+pin_value | close | <1k bets | 9-5 | 64.3 | 17.9 | 39.6 |  |
| pin_value+sharp_gap | close | <1k bets | 9-5 | 64.3 | 17.9 | 39.6 |  |
| follow_move+money_moving | close | <1k bets | 16-23 | 41.0 | -8.9 | -22.0 |  |
| follow_move+sharp_gap | close | <1k bets | 16-23 | 41.0 | -8.9 | -22.0 |  |
| follow_move+money_level | close | <1k bets | 11-25 | 30.6 | -19.2 | -42.3 |  |
| consensus_gap+pin_rlm | close | <1k bets | 2-2 | 50.0 | 26.4 | 50.5 |  |
| money_moving+pin_rlm | close | <1k bets | 11-7 | 61.1 | 19.6 | 31.8 |  |
| pin_rlm+sharp_gap | close | <1k bets | 11-7 | 61.1 | 19.6 | 31.8 |  |
| consensus_gap+follow_move | close | <1k bets | 2-6 | 25.0 | -24.7 | -54.2 |  |
| follow_move+pin_rlm | close | <1k bets | 7-1 | 87.5 | 37.1 | 67.9 |  |
| follow_move+pin_value | close | <1k bets | 11-2 | 84.6 | 34.6 | 60.9 |  |
| follow_move+rlm_ratio | close | <1k bets | 7-2 | 77.8 | 27.3 | 49.3 |  |
| money_moving+rlm_ratio | close | <1k bets | 7-2 | 77.8 | 27.3 | 49.3 |  |
| pin_rlm+pin_value | close | <1k bets | 4-0 | 100.0 | 49.4 | 91.6 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 7-1 | 87.5 | 37.1 | 67.9 |  |
| pin_value+rlm_ratio | close | <1k bets | 3-0 | 100.0 | 49.4 | 91.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 7-2 | 77.8 | 27.3 | 49.3 |  |
| money_level+rlm_ratio | close | <1k bets | 1-2 | 33.3 | -17.3 | -36.9 |  |
| money_level+pin_rlm | close | <1k bets | 3-1 | 75.0 | 37.9 | 56.8 |  |
| consensus_gap+follow_move | close | pin $1-2k | 20-19 | 51.3 | 1.6 | -4.4 |  |
| consensus_gap+money_moving | close | pin $1-2k | 36-47 | 43.4 | -3.3 | -1.1 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 11-12 | 47.8 | 7.1 | 53.0 |  |
| consensus_gap+pin_value | close | pin $1-2k | 44-48 | 47.8 | 2.0 | -1.2 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 8-6 | 57.1 | 7.4 | 6.4 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 36-44 | 45.0 | -1.3 | 2.5 |  |
| follow_move+money_moving | close | pin $1-2k | 63-85 | 42.6 | -7.3 | -19.2 |  |
| follow_move+pin_rlm | close | pin $1-2k | 19-12 | 61.3 | 11.1 | 16.6 |  |
| follow_move+pin_value | close | pin $1-2k | 33-29 | 53.2 | 3.4 | -0.1 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 27-23 | 54.0 | 4.0 | 2.4 |  |
| follow_move+sharp_gap | close | pin $1-2k | 65-83 | 43.9 | -6.0 | -16.5 |  |
| money_moving+pin_rlm | close | pin $1-2k | 30-20 | 60.0 | 16.7 | 49.7 |  |
| money_moving+pin_value | close | pin $1-2k | 35-43 | 44.9 | -1.7 | -8.9 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 26-22 | 54.2 | 4.2 | 2.6 |  |
| money_moving+sharp_gap | close | pin $1-2k | 127-145 | 46.7 | -1.4 | -3.3 |  |
| pin_rlm+pin_value | close | pin $1-2k | 9-8 | 52.9 | 6.0 | 16.9 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 19-12 | 61.3 | 11.1 | 16.6 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 32-20 | 61.5 | 18.0 | 51.3 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 10-8 | 55.6 | 5.7 | 4.2 |  |
| pin_value+sharp_gap | close | pin $1-2k | 35-41 | 46.1 | -0.4 | -6.6 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 27-23 | 54.0 | 4.0 | 2.4 |  |
| follow_move+money_level | close | pin $1-2k | 60-77 | 43.8 | -6.0 | -16.9 |  |
| money_level+rlm_ratio | close | pin $1-2k | 15-12 | 55.6 | 5.7 | 4.5 |  |
| money_level+sharp_gap | close | pin $1-2k | 95-99 | 49.0 | -2.7 | -8.3 |  |
| money_level+money_moving | close | pin $1-2k | 93-102 | 47.7 | -4.1 | -10.7 |  |
| consensus_gap+money_level | close | pin $1-2k | 40-36 | 52.6 | -3.4 | -6.1 |  |
| money_level+pin_value | close | pin $1-2k | 39-37 | 51.3 | 1.2 | -4.3 |  |
| money_level+pin_rlm | close | pin $1-2k | 15-7 | 68.2 | 21.7 | 36.5 |  |
| follow_move+money_level | close | pin $2k+ | 28-29 | 49.1 | -0.7 | -6.7 |  |
| follow_move+money_moving | close | pin $2k+ | 29-36 | 44.6 | -5.3 | -15.2 |  |
| follow_move+sharp_gap | close | pin $2k+ | 30-36 | 45.5 | -4.5 | -13.6 |  |
| money_level+money_moving | close | pin $2k+ | 58-64 | 47.5 | -5.0 | -13.9 |  |
| money_level+sharp_gap | close | pin $2k+ | 57-66 | 46.3 | -6.1 | -15.1 |  |
| money_moving+sharp_gap | close | pin $2k+ | 77-126 | 37.9 | -6.8 | -24.5 |  |
| consensus_gap+money_moving | close | pin $2k+ | 14-38 | 26.9 | -15.4 | -39.3 |  |
| consensus_gap+pin_value | close | pin $2k+ | 24-29 | 45.3 | 3.4 | -4.2 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 15-41 | 26.8 | -17.0 | -41.2 |  |
| money_moving+pin_value | close | pin $2k+ | 20-31 | 39.2 | -3.5 | -13.1 |  |
| pin_value+sharp_gap | close | pin $2k+ | 20-32 | 38.5 | -3.9 | -14.7 |  |
| consensus_gap+follow_move | close | pin $2k+ | 7-4 | 63.6 | 13.9 | 17.6 |  |
| follow_move+pin_value | close | pin $2k+ | 16-8 | 66.7 | 16.9 | 24.7 |  |
| follow_move+pin_rlm | close | pin $2k+ | 6-11 | 35.3 | -15.0 | -32.4 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 9-12 | 42.9 | -7.4 | -18.1 |  |
| money_level+pin_rlm | close | pin $2k+ | 4-7 | 36.4 | -6.6 | -28.9 |  |
| money_level+pin_value | close | pin $2k+ | 25-22 | 53.2 | 2.8 | -2.6 |  |
| money_level+rlm_ratio | close | pin $2k+ | 3-6 | 33.3 | -16.9 | -36.2 |  |
| money_moving+pin_rlm | close | pin $2k+ | 12-34 | 26.1 | -7.9 | -46.9 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 9-12 | 42.9 | -7.4 | -18.1 |  |
| pin_rlm+pin_value | close | pin $2k+ | 2-6 | 25.0 | -8.6 | -53.1 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 6-11 | 35.3 | -15.0 | -32.4 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 12-34 | 26.1 | -7.9 | -46.9 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 1-1 | 50.0 | -0.3 | -6.2 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 9-12 | 42.9 | -7.4 | -18.1 |  |
| consensus_gap+money_level | close | pin $2k+ | 39-26 | 60.0 | -4.1 | -8.2 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 1-11 | 8.3 | -19.7 | -84.4 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -50.3 | -100.0 |  |
| money_level+money_moving | close | pin limit <$1k | 32-40 | 44.4 | -5.5 | -15.1 |  |
| money_level+sharp_gap | close | pin limit <$1k | 33-40 | 45.2 | -4.8 | -13.7 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 55-61 | 47.4 | -2.3 | -1.6 |  |
| consensus_gap+money_level | close | pin limit <$1k | 18-18 | 50.0 | -0.3 | -7.9 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 23-27 | 46.0 | -3.1 | -4.6 |  |
| follow_move+money_moving | close | pin limit <$1k | 38-40 | 48.7 | -1.4 | -6.8 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 39-40 | 49.4 | -0.8 | -5.5 |  |
| money_level+pin_value | close | pin limit <$1k | 25-23 | 52.1 | 2.4 | -1.7 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 11-8 | 57.9 | 8.3 | 8.4 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 14-13 | 51.9 | 3.2 | 14.2 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 15-14 | 51.7 | 2.9 | 12.7 |  |
| follow_move+money_level | close | pin limit <$1k | 29-29 | 50.0 | 0.1 | -4.8 |  |
| follow_move+pin_value | close | pin limit <$1k | 23-13 | 63.9 | 14.1 | 20.9 |  |
| money_moving+pin_value | close | pin limit <$1k | 20-19 | 51.3 | 2.1 | 8.7 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 22-20 | 52.4 | 3.1 | 9.9 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 3-1 | 75.0 | 32.0 | 152.0 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 18-10 | 64.3 | 15.8 | 55.1 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 10-2 | 83.3 | 35.3 | 96.3 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 19-10 | 65.5 | 17.0 | 56.3 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 15-7 | 68.2 | 17.8 | 31.1 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 21-14 | 60.0 | 9.6 | 15.3 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 20-14 | 58.8 | 8.5 | 13.1 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 15-7 | 68.2 | 17.8 | 31.1 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 21-14 | 60.0 | 9.6 | 15.3 |  |
| money_level+pin_rlm | close | pin limit <$1k | 6-4 | 60.0 | 9.5 | 14.5 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 6-6 | 50.0 | -0.4 | -3.9 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 10-4 | 71.4 | 21.2 | 36.9 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 3-2 | 60.0 | 10.4 | 13.8 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 49.4 | 87.7 |  |
| pin_rlm | early | <1k bets | 1-1 | 50.0 | 26.4 | -3.7 | -2.15 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -23.6 | -100.0 | -4.8 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 76.4 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 15-16 | 48.4 | -1.5 | -7.7 | -0.1 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -49.9 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 116-109 | 51.6 | 1.6 | -1.4 | 0.24 |
| follow_move | early | pin $1-2k | 10-8 | 55.6 | 5.6 | 5.0 | -0.06 |
| follow_move | early | pin limit <$1k | 33-29 | 53.2 | 3.4 | 1.1 | -0.35 |
| rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 16.4 | 29.2 | -0.5 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -50.3 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 2-1 | 66.7 | 16.1 | 28.7 | 0.67 |
| rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -0.3 | -1.0 | -0.5 |
| rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 29.6 | 53.6 | -0.4 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 0.1 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 41.1 | 59.7 | 0.33 |
| money_level | early | <1k bets | 58-30 | 65.9 | 4.7 | 5.5 | 0.57 |
| money_level | early | pin $1-2k | 14-8 | 63.6 | -1.9 | -3.2 | 0.01 |
| money_level | early | pin limit <$1k | 22-24 | 47.8 | -6.2 | -12.1 | 0.31 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 8.2 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 7.6 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 44-34 | 56.4 | 7.5 | 15.5 | 0.71 |
| sharp_gap | early | pin $1-2k | 11-9 | 55.0 | 3.6 | 13.8 | -0.57 |
| sharp_gap | early | pin limit <$1k | 27-16 | 62.8 | 14.6 | 30.8 | 0.2 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.4 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.9 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 29-22 | 56.9 | 3.8 | -5.9 | 0.05 |
| money_moving | early | pin $1-2k | 6-6 | 50.0 | -13.2 | -26.9 | 0.35 |
| money_moving | early | pin limit <$1k | 20-9 | 69.0 | 19.9 | 47.8 | 0.36 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.4 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 50.3 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 30-32 | 48.4 | 0.6 | -8.3 | 0.21 |
| pin_value | early | pin $1-2k | 11-14 | 44.0 | -0.6 | -16.7 | 0.17 |
| pin_value | early | pin limit <$1k | 32-27 | 54.2 | 4.7 | 2.5 | 0.15 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -49.4 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -25.4 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.7 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 13.4 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 96-135 | 41.6 | -4.4 | -15.9 | 0.32 |
| consensus_gap | early | pin $1-2k | 10-16 | 38.5 | -7.4 | -24.8 | 0.47 |
| consensus_gap | early | pin limit <$1k | 17-32 | 34.7 | -16.3 | -27.7 | 0.33 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 16.2 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 4.2 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.0 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.6 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 20.1 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.5 | 26.0 | -0.25 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 2.9 | -6.9 | 0.3 |
| consensus_gap+follow_move | early | 1-3k bets | 4-4 | 50.0 | 0.3 | -6.9 | 0.25 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -23.2 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -1.6 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 10-10 | 50.0 | -0.0 | -4.1 | 0.05 |
| follow_move+pin_value | early | 1-3k bets | 7-5 | 58.3 | 8.4 | 9.2 | -0.42 |
| follow_move+sharp_gap | early | 1-3k bets | 9-8 | 52.9 | 2.9 | 1.2 | -0.18 |
| follow_move+rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 16.4 | 29.2 | -0.5 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 29.6 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 4-2 | 66.7 | 16.4 | 29.2 | -0.5 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 18.0 | 56.1 | 0.15 |
| follow_move+money_moving | early | 1-3k bets | 9-4 | 69.2 | 19.3 | 32.1 | 0.08 |
| money_moving+rlm_ratio | early | 1-3k bets | 2-1 | 66.7 | 16.6 | 28.7 | -1.0 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 50.3 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 50.3 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 50.3 | 83.3 | 1.0 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -50.3 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -50.3 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.9 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 50.3 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 50.3 | 83.3 | 1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -50.3 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 36.5 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 49.4 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 8-9 | 47.1 | -2.8 | -12.2 | 1.24 |
| consensus_gap+money_level | early | <1k bets | 12-11 | 52.2 | -12.6 | -21.3 | 0.8 |
| consensus_gap+sharp_gap | early | <1k bets | 9-17 | 34.6 | -10.3 | 2.0 | 1.13 |
| follow_move+money_level | early | <1k bets | 14-5 | 73.7 | 24.1 | 40.2 | 0.95 |
| follow_move+sharp_gap | early | <1k bets | 13-5 | 72.2 | 22.4 | 37.7 | 1.0 |
| money_level+sharp_gap | early | <1k bets | 35-16 | 68.6 | 11.6 | 15.1 | 1.09 |
| money_level+money_moving | early | <1k bets | 22-13 | 62.9 | 3.2 | -1.0 | -0.12 |
| money_moving+sharp_gap | early | <1k bets | 19-14 | 57.6 | 6.9 | -0.4 | 0.25 |
| consensus_gap+money_moving | early | <1k bets | 5-9 | 35.7 | -10.4 | -42.1 | 0.26 |
| follow_move+pin_value | early | <1k bets | 11-10 | 52.4 | 2.5 | -1.5 | 0.29 |
| follow_move+money_moving | early | <1k bets | 6-3 | 66.7 | 16.9 | 27.7 | 0.0 |
| consensus_gap+pin_value | early | <1k bets | 11-21 | 34.4 | -11.4 | -35.3 | 0.5 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -23.6 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -23.6 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | <1k bets | 1-1 | 50.0 | 26.4 | -3.7 | -2.15 |
| pin_value+sharp_gap | early | <1k bets | 4-3 | 57.1 | 11.0 | 9.1 | 0.03 |
| money_level+pin_value | early | <1k bets | 3-3 | 50.0 | 0.2 | -4.5 | 1.33 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -50.4 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -50.6 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 0-2 | 0.0 | -49.9 | -100.0 | 2.5 |
| follow_move+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 16.1 | 28.7 | 0.67 |
| money_level+rlm_ratio | early | <1k bets | 2-0 | 100.0 | 49.4 | 93.0 | 0.5 |
| money_moving+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 49.4 | 95.2 | 0.0 |
| rlm_ratio+sharp_gap | early | <1k bets | 2-1 | 66.7 | 16.1 | 28.7 | 0.67 |
| consensus_gap+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -50.6 | -100.0 | 1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 49.4 | 90.9 | 1.0 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 76.4 | 92.6 | 0.5 |
| consensus_gap+money_level | early | pin $1-2k | 4-4 | 50.0 | -16.4 | -22.9 | 0.44 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -34.2 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 4-9 | 30.8 | -8.9 | -42.5 | 0.4 |
| follow_move+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -0.3 | -1.0 | -0.5 |
| follow_move+sharp_gap | early | pin $1-2k | 3-1 | 75.0 | 25.0 | 45.0 | -0.25 |
| money_level+money_moving | early | pin $1-2k | 6-5 | 54.5 | -12.2 | -20.3 | 0.02 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -9.8 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 1-1 | 50.0 | -0.3 | -1.0 | -0.5 |
| money_level+sharp_gap | early | pin $1-2k | 8-4 | 66.7 | 3.5 | 8.4 | -0.41 |
| money_moving+sharp_gap | early | pin $1-2k | 3-5 | 37.5 | -22.4 | -45.3 | -0.06 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -7.9 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 2-2 | 50.0 | 0.0 | -8.4 | 0.75 |
| follow_move+money_level | early | pin $1-2k | 3-2 | 60.0 | 10.2 | 16.0 | 0.2 |
| follow_move+pin_value | early | pin $1-2k | 4-3 | 57.1 | 7.2 | 6.9 | 0.29 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 49.7 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 1-0 | 100.0 | 50.3 | 90.9 | 0.0 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -23.6 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -25.0 | -62.8 | -0.72 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -23.6 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -23.6 | -100.0 | -4.8 |
| money_level+money_moving | early | pin limit <$1k | 11-7 | 61.1 | 8.1 | 12.1 | 0.53 |
| money_level+sharp_gap | early | pin limit <$1k | 18-14 | 56.2 | 5.3 | 2.3 | 0.25 |
| money_moving+sharp_gap | early | pin limit <$1k | 16-5 | 76.2 | 28.6 | 68.0 | 0.39 |
| money_level+pin_value | early | pin limit <$1k | 8-5 | 61.5 | 11.3 | 16.6 | 0.46 |
| money_moving+pin_value | early | pin limit <$1k | 6-4 | 60.0 | 10.0 | 13.0 | 0.3 |
| pin_value+sharp_gap | early | pin limit <$1k | 11-5 | 68.8 | 18.7 | 30.3 | 0.06 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-7 | 46.2 | -3.5 | -14.2 | 0.46 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -27.9 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 13-17 | 43.3 | -5.7 | -18.8 | 0.49 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.3 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 8-7 | 53.3 | 3.3 | 1.9 | 0.07 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 4.0 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 9-7 | 56.2 | 6.2 | 6.9 | -0.31 |
| follow_move+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 29.6 | 53.6 | -0.4 |
| money_level+rlm_ratio | early | pin limit <$1k | 4-0 | 100.0 | 49.4 | 92.0 | 0.25 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 16.5 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 4-1 | 80.0 | 29.6 | 53.6 | -0.4 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 22.8 | 72.3 | 0.54 |
| follow_move+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 20.0 | 33.3 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 16.5 | 28.7 | -1.0 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -50.6 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -50.6 | -100.0 | 1.0 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 76.4 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 76.4 | 92.6 | 0.5 |
