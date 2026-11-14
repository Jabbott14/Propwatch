# CBB scorecard

Generated 2026-11-14 22:46 UTC. 429 graded games (28 finished games had no final score matched and are not graded).

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before tip. Break-even at -110 is 52.4%. CLV = points of closing-line
value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured
on this sample. `edge` is hit% minus that. A signal that is structurally long
favourites or overs beats 50% whenever those run, which is not an edge -- this
sample ran **46.3% favourites** (n=428) and **47.3% overs** (n=429) and **75.1% moneyline favourites** (n=357).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

## EARLY

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 1-1 | 50.0 | 24.9 | 25.1 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | both | 166-174 | 48.8 | 49.3 | -0.5 | -22.26 | -6.5 | 0.15 | 39.1 | no edge shown yet |
| rlm_ratio | both | 7-4 | 63.6 | 52.0 | 11.6 | +2.52 | 22.9 | -0.36 | 18.2 | keep collecting (11/30) |
| money_level | both | 100-62 | 61.7 | 58.4 | 3.4 | -0.97 | -0.6 | 0.21 | 41.4 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 85-68 | 55.6 | 48.4 | 7.2 | +21.54 | 14.1 | 0.36 | 42.5 | no edge shown yet |
| money_moving | both | 62-37 | 62.6 | 51.4 | 11.2 | +14.46 | 14.6 | 0.17 | 42.4 | PROMOTE: beats break-even and its own base rate |
| pin_value | both | 43-41 | 51.2 | 47.7 | 3.5 | -2.68 | -3.2 | 0.15 | 41.7 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 52.2 | -32.2 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 132-190 | 41.0 | 46.2 | -5.2 | -54.05 | -16.8 | 0.33 | 46.6 | DROP: below break-even |
| consensus_gap+money_level | both | 20-21 | 48.8 | 62.5 | -13.7 | -10.17 | -24.8 | 0.19 | 46.3 | no edge shown yet |
| consensus_gap+money_moving | both | 13-14 | 48.1 | 45.4 | 2.7 | +0.43 | 1.6 | -0.07 | 37.0 | keep collecting (27/30) |
| consensus_gap+pin_value | both | 17-26 | 39.5 | 45.3 | -5.8 | -11.16 | -26.0 | 0.46 | 53.5 | DROP: below break-even |
| follow_move+rlm_ratio | both | 7-4 | 63.6 | 52.0 | 11.6 | +2.52 | 22.9 | -0.36 | 18.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 25-15 | 62.5 | 49.3 | 13.2 | +7.74 | 19.4 | 0.38 | 37.5 | no edge shown yet |
| money_level+money_moving | both | 40-20 | 66.7 | 56.8 | 9.9 | +5.6 | 9.3 | 0.07 | 46.7 | PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | both | 10-8 | 55.6 | 50.1 | 5.4 | +0.9 | 5.0 | 0.5 | 50.0 | keep collecting (18/30) |
| money_moving+pin_value | both | 7-5 | 58.3 | 49.9 | 8.4 | +1.13 | 9.4 | 0.42 | 41.7 | keep collecting (12/30) |
| rlm_ratio+sharp_gap | both | 7-4 | 63.6 | 52.0 | 11.6 | +2.52 | 22.9 | -0.36 | 18.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 59-34 | 63.4 | 54.7 | 8.7 | +9.11 | 9.8 | 0.5 | 46.2 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 39-22 | 63.9 | 49.1 | 14.9 | +12.86 | 21.1 | 0.29 | 42.6 | PROMOTE: beats break-even and its own base rate |
| pin_value+sharp_gap | both | 12-7 | 63.2 | 48.9 | 14.3 | +3.75 | 19.8 | -0.15 | 36.8 | keep collecting (19/30) |
| consensus_gap+follow_move | both | 15-15 | 50.0 | 48.1 | 1.9 | -1.86 | -6.2 | 1.07 | 53.3 | no edge shown yet |
| consensus_gap+sharp_gap | both | 14-29 | 32.6 | 44.9 | -12.3 | -3.04 | -7.1 | 0.48 | 44.2 | DROP: below break-even |
| follow_move+money_level | both | 26-19 | 57.8 | 48.3 | 9.4 | +4.67 | 10.4 | 0.4 | 40.0 | no edge shown yet |
| follow_move+pin_value | both | 18-15 | 54.5 | 48.9 | 5.7 | +0.8 | 2.4 | 0.03 | 30.3 | no edge shown yet |
| money_level+rlm_ratio | both | 6-1 | 85.7 | 53.1 | 32.6 | +4.61 | 65.9 | 0.14 | 14.3 | keep collecting (7/30) |
| pin_value+rlm_ratio | both | 2-1 | 66.7 | 50.9 | 15.8 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| follow_move+money_moving | both | 18-9 | 66.7 | 48.6 | 18.1 | +7.43 | 27.5 | 0.11 | 37.0 | keep collecting (27/30) |
| money_moving+rlm_ratio | both | 4-1 | 80.0 | 50.5 | 29.5 | +2.72 | 54.4 | -1.0 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 24.9 | -24.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 24.9 | -24.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | both | 1-1 | 50.0 | 24.9 | 25.1 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 53.2 | -53.2 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 52.7 | -52.7 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 0-1 | 0.0 | 52.7 | -52.7 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 24.9 | 75.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-1 | 50.0 | 24.9 | 25.1 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | spread | 82-91 | 47.4 | 48.9 | -1.5 | -16.07 | -9.3 | 0.01 | 34.7 | no edge shown yet |
| follow_move | total | 84-83 | 50.3 | 49.6 | 0.7 | -6.19 | -3.7 | 0.29 | 43.7 | no edge shown yet |
| rlm_ratio | spread | 3-2 | 60.0 | 52.2 | 7.8 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 4-2 | 66.7 | 51.8 | 14.9 | +1.68 | 28.0 | -0.17 | 33.3 | keep collecting (6/30) |
| money_level | moneyline | 50-22 | 69.4 | 70.2 | -0.8 | -6.3 | -8.7 | 0.19 | 47.2 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 16-15 | 51.6 | 48.7 | 2.9 | -0.6 | -1.9 | 0.9 | 48.4 | no edge shown yet |
| money_level | total | 34-25 | 57.6 | 49.0 | 8.6 | +5.92 | 10.0 | -0.14 | 30.5 | no edge shown yet |
| sharp_gap | moneyline | 32-31 | 50.8 | 45.6 | 5.2 | +10.36 | 16.4 | 0.33 | 50.8 | no edge shown yet |
| sharp_gap | spread | 18-14 | 56.2 | 49.8 | 6.5 | +2.26 | 7.1 | 0.56 | 34.4 | no edge shown yet |
| sharp_gap | total | 35-23 | 60.3 | 50.6 | 9.7 | +8.92 | 15.4 | 0.28 | 37.9 | no edge shown yet |
| money_moving | moneyline | 22-19 | 53.7 | 54.3 | -0.6 | -3.65 | -8.9 | 0.16 | 56.1 | no edge shown yet |
| money_moving | spread | 17-4 | 81.0 | 48.8 | 32.2 | +11.27 | 53.7 | 0.14 | 38.1 | keep collecting (21/30) |
| money_moving | total | 23-14 | 62.2 | 49.8 | 12.4 | +6.84 | 18.5 | 0.19 | 29.7 | no edge shown yet |
| pin_value | moneyline | 1-5 | 16.7 | 24.9 | -8.3 | -4.02 | -67.0 | -0.02 | 66.7 | keep collecting (6/30) |
| pin_value | spread | 22-17 | 56.4 | 48.9 | 7.5 | +2.35 | 6.0 | 0.28 | 41.0 | no edge shown yet |
| pin_value | total | 20-19 | 51.3 | 49.9 | 1.4 | -1.01 | -2.6 | 0.05 | 38.5 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 53.7 | -20.4 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 50-101 | 33.1 | 42.9 | -9.7 | -37.62 | -24.9 | -0.02 | 42.4 | DROP: below break-even |
| consensus_gap | spread | 43-42 | 50.6 | 48.8 | 1.8 | -4.52 | -5.3 | 0.54 | 47.1 | no edge shown yet |
| consensus_gap | total | 39-47 | 45.3 | 49.6 | -4.3 | -11.9 | -13.8 | 0.74 | 53.5 | no edge shown yet |
| money_level+sharp_gap | moneyline | 24-9 | 72.7 | 64.4 | 8.3 | +2.34 | 7.1 | 0.55 | 63.6 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+pin_value | moneyline | 1-5 | 16.7 | 24.9 | -8.3 | -4.02 | -67.0 | -0.02 | 66.7 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_level+money_moving | moneyline | 15-7 | 68.2 | 70.5 | -2.3 | -4.19 | -19.0 | -0.35 | 54.5 | keep collecting (22/30) |
| consensus_gap+sharp_gap | moneyline | 8-20 | 28.6 | 42.8 | -14.3 | +0.74 | 2.6 | 0.31 | 46.4 | keep collecting (28/30) |
| consensus_gap+money_level | moneyline | 13-13 | 50.0 | 71.2 | -21.2 | -8.23 | -31.7 | -0.24 | 46.2 | keep collecting (26/30) |
| money_moving+sharp_gap | moneyline | 13-11 | 54.2 | 47.9 | 6.3 | +0.32 | 1.3 | 0.41 | 62.5 | keep collecting (24/30) |
| consensus_gap+money_moving | moneyline | 5-13 | 27.8 | 44.4 | -16.7 | -5.5 | -30.6 | -0.05 | 50.0 | keep collecting (18/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 24.9 | -24.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 24.9 | -24.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | moneyline | 1-1 | 50.0 | 24.9 | 25.1 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 24.9 | -24.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 24.9 | 75.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 4-5 | 44.4 | 46.3 | -1.8 | -1.59 | -17.7 | 1.67 | 66.7 | keep collecting (9/30) |
| consensus_gap+money_moving | spread | 4-0 | 100.0 | 46.3 | 53.7 | +3.41 | 85.2 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_value | spread | 9-8 | 52.9 | 47.6 | 5.4 | -0.31 | -1.8 | 0.53 | 52.9 | keep collecting (17/30) |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 52.2 | 7.8 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 48.1 | 14.4 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 9-4 | 69.2 | 48.0 | 21.2 | +4.21 | 32.4 | 0.77 | 61.5 | keep collecting (13/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.4 | -5.5 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.3 | 10.7 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 52.2 | 7.8 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 13-11 | 54.2 | 48.8 | 5.4 | +0.71 | 3.0 | 0.96 | 41.7 | keep collecting (24/30) |
| money_moving+sharp_gap | spread | 9-3 | 75.0 | 48.8 | 26.2 | +5.13 | 42.7 | 0.42 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 48.8 | 17.9 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 8-8 | 50.0 | 47.2 | 2.8 | -1.18 | -7.4 | 0.94 | 43.8 | keep collecting (16/30) |
| consensus_gap+sharp_gap | spread | 3-3 | 50.0 | 46.3 | 3.7 | -0.43 | -7.1 | 2.17 | 66.7 | keep collecting (6/30) |
| follow_move+money_level | spread | 11-7 | 61.1 | 47.5 | 13.6 | +3.04 | 16.9 | 0.78 | 44.4 | keep collecting (18/30) |
| follow_move+pin_value | spread | 11-7 | 61.1 | 48.3 | 12.8 | +2.56 | 14.2 | 0.33 | 33.3 | keep collecting (18/30) |
| follow_move+money_moving | spread | 9-1 | 90.0 | 47.0 | 43.0 | +7.22 | 72.2 | 0.2 | 40.0 | keep collecting (10/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 53.7 | 12.9 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 53.7 | -53.7 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 16-9 | 64.0 | 49.2 | 14.8 | +5.58 | 22.3 | 0.08 | 32.0 | keep collecting (25/30) |
| money_level+sharp_gap | total | 22-14 | 61.1 | 49.9 | 11.3 | +6.06 | 16.8 | 0.14 | 33.3 | no edge shown yet |
| money_moving+sharp_gap | total | 17-8 | 68.0 | 50.3 | 17.7 | +7.42 | 29.7 | 0.12 | 24.0 | keep collecting (25/30) |
| money_level+pin_value | total | 7-4 | 63.6 | 51.2 | 12.4 | +2.32 | 21.1 | 0.36 | 36.4 | keep collecting (11/30) |
| money_moving+pin_value | total | 4-3 | 57.1 | 50.4 | 6.8 | +0.56 | 8.0 | 0.29 | 28.6 | keep collecting (7/30) |
| pin_value+sharp_gap | total | 10-5 | 66.7 | 50.5 | 16.1 | +4.01 | 26.7 | 0.0 | 33.3 | keep collecting (15/30) |
| follow_move+money_level | total | 15-12 | 55.6 | 48.9 | 6.6 | +1.63 | 6.0 | 0.15 | 37.0 | keep collecting (27/30) |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.5 | -2.8 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 4-2 | 66.7 | 51.8 | 14.9 | +1.68 | 28.0 | -0.17 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 15-9 | 62.5 | 50.0 | 12.5 | +4.66 | 19.4 | 0.21 | 37.5 | keep collecting (24/30) |
| money_level+rlm_ratio | total | 4-0 | 100.0 | 52.7 | 47.3 | +3.68 | 92.0 | 0.25 | 25.0 | keep collecting (4/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 50.9 | 15.8 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 4-2 | 66.7 | 51.8 | 14.9 | +1.68 | 28.0 | -0.17 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 9-8 | 52.9 | 49.5 | 3.4 | +0.2 | 1.2 | 0.06 | 35.3 | keep collecting (17/30) |
| consensus_gap+money_level | total | 3-3 | 50.0 | 49.1 | 0.9 | -0.34 | -5.7 | -0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 48.4 | 31.6 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-13 | 35.0 | 49.5 | -14.5 | -6.83 | -34.2 | 0.55 | 50.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | total | 3-6 | 33.3 | 50.3 | -17.0 | -3.35 | -37.2 | -0.11 | 22.2 | keep collecting (9/30) |
| money_moving+rlm_ratio | total | 2-1 | 66.7 | 50.9 | 15.8 | +0.86 | 28.7 | -1.0 | 0.0 | keep collecting (3/30) |
| consensus_gap+follow_move | total | 7-7 | 50.0 | 49.2 | 0.8 | -0.67 | -4.8 | 1.21 | 64.3 | keep collecting (14/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 52.7 | -52.7 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 52.7 | -52.7 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 0-1 | 0.0 | 52.7 | -52.7 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |

## CLOSE

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 82-87 | 48.5 | 43.1 | 5.4 | +22.83 | 13.5 |  |  | no edge shown yet |
| follow_move | both | 352-361 | 49.4 | 49.3 | 0.1 | -41.95 | -5.9 |  |  | DROP: below break-even |
| rlm_ratio | both | 100-81 | 55.2 | 51.0 | 4.2 | +10.13 | 5.6 |  |  | no edge shown yet |
| money_level | both | 658-512 | 56.2 | 55.7 | 0.6 | -75.37 | -6.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 502-626 | 44.5 | 47.1 | -2.6 | -99.79 | -8.8 |  |  | DROP: below break-even |
| money_moving | both | 499-629 | 44.2 | 47.3 | -3.1 | -111.99 | -9.9 |  |  | DROP: below break-even |
| pin_value | both | 231-223 | 50.9 | 47.4 | 3.5 | +7.6 | 1.7 |  |  | no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 51.2 | 15.4 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 232-337 | 40.8 | 45.8 | -5.0 | -69.05 | -12.1 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 57-50 | 53.3 | 47.6 | 5.7 | -0.71 | -0.7 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 98-185 | 34.6 | 42.7 | -8.1 | -26.32 | -9.3 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 16-26 | 38.1 | 37.1 | 0.9 | +13.34 | 31.8 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 98-114 | 46.2 | 44.6 | 1.7 | -3.36 | -1.6 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | both | 14-11 | 56.0 | 48.8 | 7.2 | +1.2 | 4.8 |  |  | keep collecting (25/30) |
| consensus_gap+sharp_gap | both | 99-189 | 34.4 | 42.4 | -8.0 | -27.15 | -9.4 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 224-254 | 46.9 | 49.4 | -2.5 | -51.59 | -10.8 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 54-43 | 55.7 | 51.5 | 4.1 | +6.51 | 6.7 |  |  | no edge shown yet |
| follow_move+pin_value | both | 87-74 | 54.0 | 48.7 | 5.3 | +2.92 | 1.8 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 100-81 | 55.2 | 51.0 | 4.2 | +10.13 | 5.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 228-250 | 47.7 | 49.4 | -1.7 | -43.73 | -9.1 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 79-87 | 47.6 | 42.9 | 4.7 | +20.09 | 12.1 |  |  | no edge shown yet |
| money_moving+pin_value | both | 94-118 | 44.3 | 46.1 | -1.7 | -12.19 | -5.8 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 97-80 | 54.8 | 50.9 | 3.9 | +8.29 | 4.7 |  |  | no edge shown yet |
| money_moving+sharp_gap | both | 481-606 | 44.3 | 47.1 | -2.9 | -101.45 | -9.3 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 25-23 | 52.1 | 45.9 | 6.1 | +13.07 | 27.2 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 54-43 | 55.7 | 51.5 | 4.1 | +6.51 | 6.7 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 82-87 | 48.5 | 43.1 | 5.4 | +22.83 | 13.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 24-19 | 55.8 | 50.3 | 5.6 | +2.49 | 5.8 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 96-118 | 44.9 | 46.1 | -1.3 | -10.44 | -4.9 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 100-81 | 55.2 | 51.0 | 4.2 | +10.13 | 5.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+money_moving | both | 345-345 | 50.0 | 52.1 | -2.1 | -62.41 | -9.0 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 345-342 | 50.2 | 52.0 | -1.7 | -54.24 | -7.9 |  |  | no edge shown yet |
| follow_move+money_level | both | 205-227 | 47.5 | 48.5 | -1.1 | -42.43 | -9.8 |  |  | DROP: below break-even |
| money_level+rlm_ratio | both | 49-43 | 53.3 | 50.6 | 2.7 | +1.35 | 1.5 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 141-122 | 53.6 | 56.6 | -2.9 | -18.69 | -7.1 |  |  | no edge shown yet |
| money_level+pin_value | both | 105-108 | 49.3 | 48.7 | 0.6 | -17.3 | -8.1 |  |  | no edge shown yet |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | both | 34-27 | 55.7 | 48.8 | 7.0 | +5.69 | 9.3 |  |  | no edge shown yet |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 52.7 | 47.3 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 20-38 | 34.5 | 26.7 | 7.8 | +15.21 | 26.2 |  |  | DROP: below break-even |
| pin_rlm | spread | 16-16 | 50.0 | 51.6 | -1.6 | -1.45 | -4.5 |  |  | no edge shown yet |
| pin_rlm | total | 46-33 | 58.2 | 51.7 | 6.6 | +9.06 | 11.5 |  |  | no edge shown yet |
| follow_move | spread | 165-166 | 49.8 | 48.6 | 1.2 | -17.27 | -5.2 |  |  | no edge shown yet |
| follow_move | total | 187-195 | 49.0 | 49.9 | -0.9 | -24.68 | -6.5 |  |  | no edge shown yet |
| rlm_ratio | spread | 28-29 | 49.1 | 50.5 | -1.3 | -3.51 | -6.1 |  |  | no edge shown yet |
| rlm_ratio | total | 72-52 | 58.1 | 51.3 | 6.8 | +13.63 | 11.0 |  |  | no edge shown yet |
| money_level | moneyline | 262-89 | 74.6 | 71.4 | 3.3 | -9.69 | -2.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 196-203 | 49.1 | 48.5 | 0.6 | -27.11 | -6.8 |  |  | no edge shown yet |
| money_level | total | 200-220 | 47.6 | 49.3 | -1.7 | -38.57 | -9.2 |  |  | DROP: below break-even |
| sharp_gap | moneyline | 109-212 | 34.0 | 40.1 | -6.1 | -41.89 | -13.1 |  |  | DROP: below break-even |
| sharp_gap | spread | 200-193 | 50.9 | 49.4 | 1.5 | -12.91 | -3.3 |  |  | no edge shown yet |
| sharp_gap | total | 193-221 | 46.6 | 50.4 | -3.8 | -44.98 | -10.9 |  |  | DROP: below break-even |
| money_moving | moneyline | 114-205 | 35.7 | 41.0 | -5.2 | -36.65 | -11.5 |  |  | DROP: below break-even |
| money_moving | spread | 197-196 | 50.1 | 49.3 | 0.8 | -18.78 | -4.8 |  |  | no edge shown yet |
| money_moving | total | 188-228 | 45.2 | 50.3 | -5.1 | -56.56 | -13.6 |  |  | DROP: below break-even |
| pin_value | moneyline | 10-35 | 22.2 | 28.3 | -6.1 | -0.66 | -1.5 |  |  | DROP: below break-even |
| pin_value | spread | 111-87 | 56.1 | 49.4 | 6.6 | +10.47 | 5.3 |  |  | no edge shown yet |
| pin_value | total | 110-101 | 52.1 | 49.6 | 2.6 | -2.21 | -1.0 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 53.7 | 46.3 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 89-197 | 31.1 | 43.0 | -11.9 | -53.64 | -18.8 |  |  | DROP: below break-even |
| consensus_gap | spread | 70-55 | 56.0 | 48.6 | 7.4 | +4.81 | 3.8 |  |  | no edge shown yet |
| consensus_gap | total | 73-85 | 46.2 | 48.5 | -2.3 | -20.23 | -12.8 |  |  | DROP: below break-even |
| money_level+money_moving | moneyline | 78-47 | 62.4 | 65.4 | -3.0 | -5.12 | -4.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 73-47 | 60.8 | 65.0 | -4.2 | -4.53 | -3.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 102-198 | 34.0 | 40.0 | -6.0 | -36.7 | -12.2 |  |  | DROP: below break-even |
| consensus_gap+money_level | moneyline | 62-40 | 60.8 | 70.2 | -9.4 | -5.36 | -5.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 31-115 | 21.2 | 37.3 | -16.1 | -14.4 | -9.9 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+sharp_gap | moneyline | 32-120 | 21.1 | 36.8 | -15.8 | -16.24 | -10.7 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_rlm | moneyline | 8-17 | 32.0 | 28.9 | 3.1 | +15.43 | 61.7 |  |  | keep collecting (25/30) |
| money_moving+pin_rlm | moneyline | 20-38 | 34.5 | 26.7 | 7.8 | +15.21 | 26.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 20-38 | 34.5 | 26.7 | 7.8 | +15.21 | 26.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 10-32 | 23.8 | 28.5 | -4.7 | +2.34 | 5.6 |  |  | DROP: below break-even |
| money_moving+pin_value | moneyline | 5-23 | 17.9 | 24.9 | -7.1 | +4.55 | 16.3 |  |  | keep collecting (28/30) |
| pin_rlm+pin_value | moneyline | 3-6 | 33.3 | 24.9 | 8.4 | +10.35 | 115.0 |  |  | keep collecting (9/30) |
| pin_value+sharp_gap | moneyline | 5-24 | 17.2 | 24.9 | -7.7 | +3.55 | 12.2 |  |  | keep collecting (29/30) |
| money_level+pin_rlm | moneyline | 5-3 | 62.5 | 31.2 | 31.3 | +3.4 | 42.5 |  |  | keep collecting (8/30) |
| money_level+pin_value | moneyline | 3-1 | 75.0 | 62.5 | 12.5 | +0.31 | 7.8 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 31-19 | 62.0 | 47.2 | 14.8 | +7.4 | 14.8 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 38-29 | 56.7 | 48.5 | 8.2 | +3.48 | 5.2 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 48-33 | 59.3 | 48.6 | 10.7 | +7.86 | 9.7 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.33 | -38.9 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | spread | 37-29 | 56.1 | 48.9 | 7.2 | +2.59 | 3.9 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 103-105 | 49.5 | 48.3 | 1.2 | -12.63 | -6.1 |  |  | no edge shown yet |
| follow_move+pin_rlm | spread | 14-15 | 48.3 | 51.4 | -3.1 | -2.21 | -7.6 |  |  | keep collecting (29/30) |
| follow_move+pin_value | spread | 45-33 | 57.7 | 48.0 | 9.7 | +6.3 | 8.1 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 28-29 | 49.1 | 50.5 | -1.3 | -3.51 | -6.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 104-104 | 50.0 | 48.5 | 1.5 | -10.49 | -5.0 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 14-16 | 46.7 | 51.5 | -4.8 | -3.28 | -10.9 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 51-46 | 52.6 | 48.8 | 3.8 | -1.83 | -1.9 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 26-28 | 48.1 | 50.3 | -2.1 | -4.44 | -8.2 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 192-188 | 50.5 | 49.3 | 1.2 | -15.28 | -4.0 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 6-7 | 46.2 | 50.3 | -4.1 | -1.79 | -13.8 |  |  | keep collecting (13/30) |
| pin_rlm+rlm_ratio | spread | 14-15 | 48.3 | 51.4 | -3.1 | -2.21 | -7.6 |  |  | keep collecting (29/30) |
| pin_rlm+sharp_gap | spread | 16-16 | 50.0 | 51.6 | -1.6 | -1.45 | -4.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 4-6 | 40.0 | 49.3 | -9.3 | -2.55 | -25.5 |  |  | keep collecting (10/30) |
| pin_value+sharp_gap | spread | 51-46 | 52.6 | 49.0 | 3.5 | -1.89 | -2.0 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 28-29 | 49.1 | 50.5 | -1.3 | -3.51 | -6.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 104-105 | 49.8 | 47.8 | 2.0 | -11.95 | -5.7 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 14-14 | 50.0 | 49.7 | 0.3 | -1.43 | -5.1 |  |  | keep collecting (28/30) |
| money_level+sharp_gap | spread | 150-147 | 50.5 | 48.7 | 1.9 | -12.58 | -4.2 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 46-35 | 56.8 | 48.0 | 8.8 | +4.45 | 5.5 |  |  | no edge shown yet |
| money_level+money_moving | spread | 149-148 | 50.2 | 48.6 | 1.6 | -14.49 | -4.9 |  |  | no edge shown yet |
| money_level+pin_value | spread | 57-53 | 51.8 | 48.3 | 3.5 | -3.69 | -3.4 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 8-6 | 57.1 | 50.5 | 6.6 | +1.1 | 7.9 |  |  | keep collecting (14/30) |
| money_level+money_moving | total | 118-150 | 44.0 | 49.7 | -5.7 | -42.8 | -16.0 |  |  | DROP: below break-even |
| money_level+sharp_gap | total | 122-148 | 45.2 | 49.8 | -4.6 | -37.13 | -13.8 |  |  | DROP: below break-even |
| money_moving+sharp_gap | total | 187-220 | 45.9 | 50.4 | -4.4 | -49.47 | -12.2 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 33-47 | 41.2 | 47.9 | -6.6 | -17.78 | -22.2 |  |  | DROP: below break-even |
| consensus_gap+pin_value | total | 40-49 | 44.9 | 48.5 | -3.5 | -13.56 | -15.2 |  |  | no edge shown yet |
| follow_move+money_moving | total | 121-149 | 44.8 | 50.1 | -5.3 | -38.97 | -14.4 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 124-146 | 45.9 | 50.2 | -4.2 | -33.24 | -12.3 |  |  | DROP: below break-even |
| money_level+pin_value | total | 45-54 | 45.5 | 48.6 | -3.1 | -13.92 | -14.1 |  |  | no edge shown yet |
| follow_move+money_level | total | 101-122 | 45.3 | 49.3 | -4.0 | -30.48 | -13.7 |  |  | DROP: below break-even |
| follow_move+pin_value | total | 42-41 | 50.6 | 49.4 | 1.2 | -3.38 | -4.1 |  |  | no edge shown yet |
| money_moving+pin_value | total | 38-49 | 43.7 | 49.8 | -6.2 | -14.91 | -17.1 |  |  | DROP: below break-even |
| pin_value+sharp_gap | total | 40-48 | 45.5 | 49.9 | -4.5 | -12.09 | -13.7 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 29-41 | 41.4 | 48.5 | -7.0 | -15.41 | -22.0 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | total | 30-40 | 42.9 | 48.5 | -5.7 | -13.5 | -19.3 |  |  | DROP: below break-even |
| consensus_gap+follow_move | total | 26-31 | 45.6 | 48.0 | -2.4 | -8.12 | -14.2 |  |  | no edge shown yet |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pin_rlm | total | 5-6 | 45.5 | 48.8 | -3.3 | -1.6 | -14.6 |  |  | keep collecting (11/30) |
| consensus_gap+rlm_ratio | total | 12-7 | 63.2 | 48.4 | 14.7 | +3.53 | 18.6 |  |  | keep collecting (19/30) |
| follow_move+pin_rlm | total | 40-28 | 58.8 | 51.6 | 7.2 | +8.71 | 12.8 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 72-52 | 58.1 | 51.3 | 6.8 | +13.63 | 11.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 21-18 | 53.8 | 51.7 | 2.1 | +1.19 | 3.1 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 35-29 | 54.7 | 50.9 | 3.8 | +2.77 | 4.3 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 45-33 | 57.7 | 51.6 | 6.0 | +8.15 | 10.5 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 71-52 | 57.7 | 51.2 | 6.5 | +12.72 | 10.3 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 16-10 | 61.5 | 51.0 | 10.5 | +4.51 | 17.3 |  |  | keep collecting (26/30) |
| pin_rlm+rlm_ratio | total | 40-28 | 58.8 | 51.6 | 7.2 | +8.71 | 12.8 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 46-33 | 58.2 | 51.7 | 6.6 | +9.06 | 11.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 20-13 | 60.6 | 50.6 | 10.0 | +5.03 | 15.3 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 72-52 | 58.1 | 51.3 | 6.8 | +13.63 | 11.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 52.7 | 47.3 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_rlm | close | 1-3k bets | 49-56 | 46.7 | 3.0 | 13.6 |  |
| pin_rlm | close | 3k+ bets | 20-21 | 48.8 | 7.5 | 8.7 |  |
| pin_rlm | close | <1k bets | 13-10 | 56.5 | 13.0 | 21.7 |  |
| pin_rlm | close | pin $1-2k | 40-31 | 56.3 | 11.4 | 33.2 |  |
| pin_rlm | close | pin $2k+ | 14-41 | 25.5 | -9.5 | -36.9 |  |
| pin_rlm | close | pin limit <$1k | 28-15 | 65.1 | 14.7 | 45.4 |  |
| follow_move | close | 1-3k bets | 236-227 | 51.0 | 1.6 | -2.8 |  |
| follow_move | close | 3k+ bets | 78-88 | 47.0 | -2.3 | -10.4 |  |
| follow_move | close | <1k bets | 38-46 | 45.2 | -3.8 | -13.9 |  |
| follow_move | close | pin $1-2k | 112-146 | 43.4 | -5.6 | -17.3 |  |
| follow_move | close | pin $2k+ | 64-64 | 50.0 | 0.5 | -4.6 |  |
| follow_move | close | pin limit <$1k | 75-67 | 52.8 | 2.9 | 0.9 |  |
| rlm_ratio | close | 1-3k bets | 69-59 | 53.9 | 3.0 | 2.9 |  |
| rlm_ratio | close | 3k+ bets | 24-16 | 60.0 | 8.8 | 14.9 |  |
| rlm_ratio | close | <1k bets | 7-6 | 53.8 | 3.0 | 3.3 |  |
| rlm_ratio | close | pin $1-2k | 35-31 | 53.0 | 2.7 | 1.0 |  |
| rlm_ratio | close | pin $2k+ | 11-14 | 44.0 | -7.9 | -15.9 |  |
| rlm_ratio | close | pin limit <$1k | 28-18 | 60.9 | 9.2 | 16.9 |  |
| money_level | close | 1-3k bets | 438-303 | 59.1 | 3.4 | -1.5 |  |
| money_level | close | 3k+ bets | 149-130 | 53.4 | -2.2 | -9.2 |  |
| money_level | close | <1k bets | 71-78 | 47.7 | -8.0 | -25.2 |  |
| money_level | close | pin $1-2k | 186-176 | 51.4 | -2.5 | -9.3 |  |
| money_level | close | pin $2k+ | 157-127 | 55.3 | -2.4 | -10.0 |  |
| money_level | close | pin limit <$1k | 75-87 | 46.3 | -3.3 | -12.3 |  |
| sharp_gap | close | 1-3k bets | 312-402 | 43.7 | -3.4 | -11.3 |  |
| sharp_gap | close | 3k+ bets | 129-145 | 47.1 | 0.3 | 2.2 |  |
| sharp_gap | close | <1k bets | 61-78 | 43.9 | -4.1 | -17.3 |  |
| sharp_gap | close | pin $1-2k | 166-187 | 47.0 | -1.7 | -4.8 |  |
| sharp_gap | close | pin $2k+ | 112-162 | 40.9 | -5.2 | -17.6 |  |
| sharp_gap | close | pin limit <$1k | 75-81 | 48.1 | -2.4 | -2.3 |  |
| money_moving | close | 1-3k bets | 310-402 | 43.5 | -3.7 | -12.3 |  |
| money_moving | close | 3k+ bets | 128-148 | 46.4 | -0.9 | -0.6 |  |
| money_moving | close | <1k bets | 61-78 | 43.9 | -4.1 | -15.5 |  |
| money_moving | close | pin $1-2k | 160-193 | 45.3 | -3.0 | -7.4 |  |
| money_moving | close | pin $2k+ | 115-158 | 42.1 | -4.0 | -15.6 |  |
| money_moving | close | pin limit <$1k | 73-84 | 46.5 | -3.7 | -5.3 |  |
| pin_value | close | 1-3k bets | 140-143 | 49.5 | 1.9 | -0.9 |  |
| pin_value | close | 3k+ bets | 51-56 | 47.7 | 0.5 | -4.2 |  |
| pin_value | close | <1k bets | 40-24 | 62.5 | 15.8 | 22.9 |  |
| pin_value | close | pin $1-2k | 109-109 | 50.0 | 2.2 | -1.6 |  |
| pin_value | close | pin $2k+ | 62-66 | 48.4 | 3.0 | 0.8 |  |
| pin_value | close | pin limit <$1k | 60-48 | 55.6 | 6.8 | 9.3 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 46.3 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 46.3 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 147-209 | 41.3 | -4.9 | -13.5 |  |
| consensus_gap | close | 3k+ bets | 57-75 | 43.2 | -3.4 | 1.1 |  |
| consensus_gap | close | <1k bets | 28-52 | 35.0 | -7.9 | -26.8 |  |
| consensus_gap | close | pin $1-2k | 74-90 | 45.1 | -2.5 | -1.2 |  |
| consensus_gap | close | pin $2k+ | 58-69 | 45.7 | -4.0 | -13.8 |  |
| consensus_gap | close | pin limit <$1k | 37-36 | 50.7 | 2.4 | 0.5 |  |
| consensus_gap+follow_move | close | 1-3k bets | 41-30 | 57.7 | 10.1 | 7.9 |  |
| consensus_gap+money_level | close | 1-3k bets | 98-68 | 59.0 | 1.8 | 3.9 |  |
| consensus_gap+money_moving | close | 1-3k bets | 65-118 | 35.5 | -7.5 | -11.2 |  |
| consensus_gap+pin_value | close | 1-3k bets | 61-75 | 44.9 | -0.1 | -4.2 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 65-121 | 34.9 | -7.8 | -12.5 |  |
| follow_move+money_level | close | 1-3k bets | 146-143 | 50.5 | 1.9 | -3.9 |  |
| follow_move+money_moving | close | 1-3k bets | 159-168 | 48.6 | -0.8 | -7.4 |  |
| follow_move+pin_value | close | 1-3k bets | 52-44 | 54.2 | 5.5 | 2.0 |  |
| follow_move+sharp_gap | close | 1-3k bets | 159-166 | 48.9 | -0.6 | -6.8 |  |
| money_level+money_moving | close | 1-3k bets | 223-209 | 51.6 | -0.4 | -4.6 |  |
| money_level+pin_value | close | 1-3k bets | 69-65 | 51.5 | 2.8 | -3.6 |  |
| money_level+sharp_gap | close | 1-3k bets | 223-209 | 51.6 | -0.4 | -3.8 |  |
| money_moving+pin_value | close | 1-3k bets | 61-78 | 43.9 | -2.3 | -7.9 |  |
| money_moving+sharp_gap | close | 1-3k bets | 300-390 | 43.5 | -3.6 | -11.6 |  |
| pin_value+sharp_gap | close | 1-3k bets | 63-80 | 44.1 | -2.2 | -7.9 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 11-18 | 37.9 | 0.3 | 37.1 |  |
| money_level+pin_rlm | close | 1-3k bets | 23-18 | 56.1 | 4.8 | 7.2 |  |
| pin_rlm+pin_value | close | 1-3k bets | 16-16 | 50.0 | 5.1 | 37.2 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 49-56 | 46.7 | 3.0 | 13.6 |  |
| money_moving+pin_rlm | close | 1-3k bets | 47-56 | 45.6 | 2.1 | 12.1 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 13-7 | 65.0 | 16.1 | 21.6 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 69-59 | 53.9 | 3.0 | 2.9 |  |
| money_level+rlm_ratio | close | 1-3k bets | 35-31 | 53.0 | 2.5 | 1.1 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 68-59 | 53.5 | 2.6 | 2.2 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 69-59 | 53.9 | 3.0 | 2.9 |  |
| follow_move+pin_rlm | close | 1-3k bets | 33-29 | 53.2 | 1.7 | 1.8 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 33-29 | 53.2 | 1.7 | 1.8 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 16-13 | 55.2 | 5.2 | 4.3 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 47.3 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 13-13 | 50.0 | 2.1 | -7.0 |  |
| consensus_gap+money_moving | close | 3k+ bets | 22-43 | 33.8 | -8.5 | 8.4 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-5 | 37.5 | -2.9 | 19.3 |  |
| consensus_gap+pin_value | close | 3k+ bets | 27-29 | 48.2 | 3.7 | 1.4 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 1-3 | 25.0 | -23.9 | -53.2 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 23-43 | 34.8 | -7.4 | 12.6 |  |
| follow_move+money_moving | close | 3k+ bets | 49-56 | 46.7 | -2.6 | -11.2 |  |
| follow_move+pin_rlm | close | 3k+ bets | 14-10 | 58.3 | 6.6 | 12.4 |  |
| follow_move+pin_value | close | 3k+ bets | 20-23 | 46.5 | -2.3 | -12.8 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 24-16 | 60.0 | 8.8 | 14.9 |  |
| follow_move+sharp_gap | close | 3k+ bets | 53-55 | 49.1 | -0.4 | -6.5 |  |
| money_moving+pin_rlm | close | 3k+ bets | 19-21 | 47.5 | 6.5 | 6.5 |  |
| money_moving+pin_value | close | 3k+ bets | 24-31 | 43.6 | -1.9 | -5.0 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 22-15 | 59.5 | 8.5 | 13.6 |  |
| money_moving+sharp_gap | close | 3k+ bets | 121-138 | 46.7 | -0.2 | 1.4 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-6 | 45.5 | -1.0 | -13.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 14-10 | 58.3 | 6.6 | 12.4 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 20-21 | 48.8 | 7.5 | 8.7 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 5-5 | 50.0 | -0.9 | -5.2 |  |
| pin_value+sharp_gap | close | 3k+ bets | 24-29 | 45.3 | -0.3 | -1.4 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 24-16 | 60.0 | 8.8 | 14.9 |  |
| money_level+money_moving | close | 3k+ bets | 85-85 | 50.0 | -2.0 | -8.8 |  |
| money_level+sharp_gap | close | 3k+ bets | 84-82 | 50.6 | -1.1 | -6.6 |  |
| follow_move+money_level | close | 3k+ bets | 46-51 | 47.4 | -1.0 | -9.9 |  |
| money_level+rlm_ratio | close | 3k+ bets | 13-7 | 65.0 | 14.3 | 23.6 |  |
| consensus_gap+money_level | close | 3k+ bets | 31-33 | 48.4 | -7.6 | -17.8 |  |
| money_level+pin_value | close | 3k+ bets | 24-31 | 43.6 | -4.8 | -19.5 |  |
| money_level+pin_rlm | close | 3k+ bets | 8-6 | 57.1 | 13.3 | 17.5 |  |
| money_level+money_moving | close | <1k bets | 37-50 | 42.5 | -10.1 | -30.7 |  |
| money_level+sharp_gap | close | <1k bets | 38-50 | 43.2 | -9.5 | -29.3 |  |
| money_moving+sharp_gap | close | <1k bets | 60-77 | 43.8 | -4.4 | -17.5 |  |
| consensus_gap+money_level | close | <1k bets | 12-21 | 36.4 | -17.9 | -41.9 |  |
| consensus_gap+money_moving | close | <1k bets | 11-24 | 31.4 | -10.1 | -32.1 |  |
| consensus_gap+pin_value | close | <1k bets | 10-10 | 50.0 | 7.7 | 7.8 |  |
| consensus_gap+sharp_gap | close | <1k bets | 11-25 | 30.6 | -10.5 | -34.0 |  |
| money_level+pin_value | close | <1k bets | 12-12 | 50.0 | 0.9 | -7.2 |  |
| money_moving+pin_value | close | <1k bets | 9-9 | 50.0 | 3.4 | 8.6 |  |
| pin_value+sharp_gap | close | <1k bets | 9-9 | 50.0 | 3.4 | 8.6 |  |
| follow_move+money_moving | close | <1k bets | 16-30 | 34.8 | -14.0 | -33.8 |  |
| follow_move+sharp_gap | close | <1k bets | 16-29 | 35.6 | -13.3 | -32.4 |  |
| follow_move+money_level | close | <1k bets | 13-33 | 28.3 | -20.0 | -46.6 |  |
| consensus_gap+pin_rlm | close | <1k bets | 2-3 | 40.0 | 10.6 | 20.4 |  |
| money_moving+pin_rlm | close | <1k bets | 13-10 | 56.5 | 13.0 | 21.7 |  |
| pin_rlm+sharp_gap | close | <1k bets | 13-10 | 56.5 | 13.0 | 21.7 |  |
| consensus_gap+follow_move | close | <1k bets | 3-7 | 30.0 | -16.5 | -44.9 |  |
| follow_move+pin_rlm | close | <1k bets | 7-4 | 63.6 | 12.5 | 22.1 |  |
| follow_move+pin_value | close | <1k bets | 15-7 | 68.2 | 19.5 | 29.5 |  |
| follow_move+rlm_ratio | close | <1k bets | 7-6 | 53.8 | 3.0 | 3.3 |  |
| money_moving+rlm_ratio | close | <1k bets | 7-6 | 53.8 | 3.0 | 3.3 |  |
| pin_rlm+pin_value | close | <1k bets | 4-1 | 80.0 | 28.6 | 53.3 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 7-4 | 63.6 | 12.5 | 22.1 |  |
| pin_value+rlm_ratio | close | <1k bets | 3-1 | 75.0 | 23.9 | 43.9 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 7-6 | 53.8 | 3.0 | 3.3 |  |
| money_level+rlm_ratio | close | <1k bets | 1-5 | 16.7 | -34.1 | -68.5 |  |
| money_level+pin_rlm | close | <1k bets | 3-3 | 50.0 | 7.5 | 4.6 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 0-1 | 0.0 | -47.3 | -100.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 20-20 | 50.0 | 2.4 | -6.8 |  |
| consensus_gap+money_moving | close | pin $1-2k | 37-51 | 42.0 | -4.6 | -4.9 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 11-13 | 45.8 | 5.6 | 46.6 |  |
| consensus_gap+pin_value | close | pin $1-2k | 45-54 | 45.5 | 0.6 | -6.3 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 8-6 | 57.1 | 8.8 | 6.4 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 37-48 | 43.5 | -2.9 | -1.5 |  |
| follow_move+money_moving | close | pin $1-2k | 77-107 | 41.8 | -7.2 | -20.4 |  |
| follow_move+pin_rlm | close | pin $1-2k | 26-19 | 57.8 | 6.7 | 10.5 |  |
| follow_move+pin_value | close | pin $1-2k | 40-43 | 48.2 | -0.7 | -9.4 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 35-31 | 53.0 | 2.7 | 1.0 |  |
| follow_move+sharp_gap | close | pin $1-2k | 79-105 | 42.9 | -6.2 | -18.3 |  |
| money_moving+pin_rlm | close | pin $1-2k | 38-31 | 55.1 | 10.4 | 31.6 |  |
| money_moving+pin_value | close | pin $1-2k | 41-58 | 41.4 | -5.3 | -16.9 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 34-30 | 53.1 | 2.9 | 1.1 |  |
| money_moving+sharp_gap | close | pin $1-2k | 158-185 | 46.1 | -2.4 | -6.5 |  |
| pin_rlm+pin_value | close | pin $1-2k | 10-14 | 41.7 | -6.6 | -9.3 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 26-19 | 57.8 | 6.7 | 10.5 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 40-31 | 56.3 | 11.4 | 33.2 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 12-13 | 48.0 | -1.5 | -9.9 |  |
| pin_value+sharp_gap | close | pin $1-2k | 41-56 | 42.3 | -4.5 | -15.2 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 35-31 | 53.0 | 2.7 | 1.0 |  |
| follow_move+money_level | close | pin $1-2k | 75-98 | 43.4 | -5.2 | -17.6 |  |
| money_level+rlm_ratio | close | pin $1-2k | 21-17 | 55.3 | 5.6 | 4.7 |  |
| money_level+sharp_gap | close | pin $1-2k | 121-129 | 48.4 | -3.1 | -10.1 |  |
| money_level+money_moving | close | pin $1-2k | 117-131 | 47.2 | -4.1 | -12.2 |  |
| consensus_gap+money_level | close | pin $1-2k | 42-42 | 50.0 | -5.6 | -11.6 |  |
| money_level+pin_value | close | pin $1-2k | 45-50 | 47.4 | -1.7 | -11.5 |  |
| money_level+pin_rlm | close | pin $1-2k | 20-12 | 62.5 | 14.0 | 24.1 |  |
| follow_move+money_level | close | pin $2k+ | 35-35 | 50.0 | 1.7 | -5.0 |  |
| follow_move+money_moving | close | pin $2k+ | 39-40 | 49.4 | -0.2 | -6.0 |  |
| follow_move+sharp_gap | close | pin $2k+ | 40-40 | 50.0 | 0.5 | -4.8 |  |
| money_level+money_moving | close | pin $2k+ | 74-80 | 48.1 | -5.0 | -13.0 |  |
| money_level+sharp_gap | close | pin $2k+ | 73-82 | 47.1 | -5.9 | -13.9 |  |
| money_moving+sharp_gap | close | pin $2k+ | 110-157 | 41.2 | -4.8 | -16.7 |  |
| consensus_gap+money_moving | close | pin $2k+ | 19-42 | 31.1 | -11.5 | -22.5 |  |
| consensus_gap+pin_value | close | pin $2k+ | 28-31 | 47.5 | 6.3 | 9.3 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 20-45 | 30.8 | -13.1 | -25.2 |  |
| money_moving+pin_value | close | pin $2k+ | 30-38 | 44.1 | 0.6 | 2.2 |  |
| pin_value+sharp_gap | close | pin $2k+ | 30-39 | 43.5 | 0.2 | 0.7 |  |
| consensus_gap+follow_move | close | pin $2k+ | 8-4 | 66.7 | 19.0 | 23.4 |  |
| follow_move+pin_value | close | pin $2k+ | 21-14 | 60.0 | 11.6 | 13.0 |  |
| follow_move+pin_rlm | close | pin $2k+ | 6-13 | 31.6 | -20.9 | -39.5 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 11-14 | 44.0 | -7.9 | -15.9 |  |
| money_level+pin_rlm | close | pin $2k+ | 4-7 | 36.4 | -8.1 | -28.9 |  |
| money_level+pin_value | close | pin $2k+ | 31-30 | 50.8 | 2.1 | -6.5 |  |
| money_level+rlm_ratio | close | pin $2k+ | 5-6 | 45.5 | -6.2 | -13.1 |  |
| money_moving+pin_rlm | close | pin $2k+ | 14-41 | 25.5 | -9.5 | -36.9 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 11-14 | 44.0 | -7.9 | -15.9 |  |
| pin_rlm+pin_value | close | pin $2k+ | 3-7 | 30.0 | -6.3 | 19.5 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 6-13 | 31.6 | -20.9 | -39.5 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 14-41 | 25.5 | -9.5 | -36.9 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 1-2 | 33.3 | -20.4 | -37.4 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 11-14 | 44.0 | -7.9 | -15.9 |  |
| consensus_gap+money_level | close | pin $2k+ | 41-28 | 59.4 | -3.0 | -8.2 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 2-11 | 15.4 | -13.9 | -22.5 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -53.7 | -100.0 |  |
| money_level+money_moving | close | pin limit <$1k | 37-50 | 42.5 | -7.2 | -18.8 |  |
| money_level+sharp_gap | close | pin limit <$1k | 39-50 | 43.8 | -6.1 | -16.3 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 69-76 | 47.6 | -2.8 | -2.8 |  |
| consensus_gap+money_level | close | pin limit <$1k | 19-21 | 47.5 | -1.1 | -12.5 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 25-29 | 46.3 | -1.5 | -4.8 |  |
| follow_move+money_moving | close | pin limit <$1k | 45-49 | 47.9 | -2.6 | -8.4 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 46-48 | 48.9 | -1.6 | -6.3 |  |
| money_level+pin_value | close | pin limit <$1k | 29-28 | 50.9 | 2.8 | -4.1 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 12-10 | 54.5 | 7.1 | 2.0 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 15-14 | 51.7 | 4.6 | 12.7 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 16-15 | 51.6 | 3.9 | 11.4 |  |
| follow_move+money_level | close | pin limit <$1k | 35-40 | 46.7 | -2.4 | -11.1 |  |
| follow_move+pin_value | close | pin limit <$1k | 26-17 | 60.5 | 11.8 | 14.4 |  |
| money_moving+pin_value | close | pin limit <$1k | 23-22 | 51.1 | 2.6 | 6.7 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 25-23 | 52.1 | 3.2 | 7.9 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 3-2 | 60.0 | 17.2 | 101.6 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 27-15 | 64.3 | 13.9 | 44.3 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 12-2 | 85.7 | 36.9 | 95.2 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 28-15 | 65.1 | 14.7 | 45.4 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 22-11 | 66.7 | 15.1 | 28.1 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 28-18 | 60.9 | 9.2 | 16.9 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 27-18 | 60.0 | 8.4 | 15.3 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 22-11 | 66.7 | 15.1 | 28.1 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 28-18 | 60.9 | 9.2 | 16.9 |  |
| money_level+pin_rlm | close | pin limit <$1k | 10-8 | 55.6 | 3.8 | 6.4 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 10-10 | 50.0 | -1.6 | -3.9 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 11-4 | 73.3 | 22.4 | 40.5 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 3-3 | 50.0 | 1.8 | -5.2 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 47.3 | 87.7 |  |
| pin_rlm | early | <1k bets | 1-1 | 50.0 | 25.1 | -3.7 | -2.15 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -24.9 | -100.0 | -4.8 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 75.1 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 15-16 | 48.4 | -0.5 | -7.7 | -0.1 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -50.5 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 135-136 | 49.8 | 0.7 | -4.6 | 0.19 |
| follow_move | early | pin $1-2k | 10-8 | 55.6 | 5.6 | 5.0 | -0.06 |
| follow_move | early | pin limit <$1k | 33-29 | 53.2 | 4.3 | 1.1 | -0.35 |
| rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 14.4 | 29.2 | -0.5 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.7 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 3-1 | 75.0 | 23.9 | 44.2 | 0.0 |
| rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -3.7 | -1.0 | -0.5 |
| rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 28.4 | 53.6 | -0.4 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 0.0 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 42.0 | 59.7 | 0.33 |
| money_level | early | <1k bets | 71-42 | 62.8 | 3.7 | 0.3 | 0.27 |
| money_level | early | pin $1-2k | 14-8 | 63.6 | -0.7 | -3.2 | 0.01 |
| money_level | early | pin limit <$1k | 22-24 | 47.8 | -6.1 | -12.1 | 0.31 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.1 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 6.2 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 58-46 | 55.8 | 7.2 | 11.7 | 0.53 |
| sharp_gap | early | pin $1-2k | 11-9 | 55.0 | 3.2 | 13.8 | -0.57 |
| sharp_gap | early | pin limit <$1k | 27-16 | 62.8 | 14.1 | 30.8 | 0.2 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.3 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.5 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 38-26 | 59.4 | 6.8 | 3.0 | 0.16 |
| money_moving | early | pin $1-2k | 6-6 | 50.0 | -11.9 | -26.9 | 0.35 |
| money_moving | early | pin limit <$1k | 20-9 | 69.0 | 19.9 | 47.8 | 0.36 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.8 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.7 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 30-32 | 48.4 | 0.9 | -8.3 | 0.21 |
| pin_value | early | pin $1-2k | 11-14 | 44.0 | 0.2 | -16.7 | 0.17 |
| pin_value | early | pin limit <$1k | 32-27 | 54.2 | 4.9 | 2.5 | 0.15 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -47.3 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -28.5 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -10.4 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 14.4 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 106-154 | 40.8 | -5.6 | -17.5 | 0.33 |
| consensus_gap | early | pin $1-2k | 10-16 | 38.5 | -7.1 | -24.8 | 0.47 |
| consensus_gap | early | pin limit <$1k | 17-32 | 34.7 | -15.5 | -27.7 | 0.33 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 16.1 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 3.5 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 3.1 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.5 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.1 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 15.8 | 26.0 | -0.25 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 5.0 | -6.9 | 0.3 |
| consensus_gap+follow_move | early | 1-3k bets | 4-4 | 50.0 | 3.6 | -6.9 | 0.25 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.5 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -1.5 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 10-10 | 50.0 | 0.6 | -4.1 | 0.05 |
| follow_move+pin_value | early | 1-3k bets | 7-5 | 58.3 | 9.8 | 9.2 | -0.42 |
| follow_move+sharp_gap | early | 1-3k bets | 9-8 | 52.9 | 2.9 | 1.2 | -0.18 |
| follow_move+rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 14.4 | 29.2 | -0.5 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 26.7 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 4-2 | 66.7 | 14.4 | 29.2 | -0.5 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 18.6 | 56.1 | 0.15 |
| follow_move+money_moving | early | 1-3k bets | 9-4 | 69.2 | 20.2 | 32.1 | 0.08 |
| money_moving+rlm_ratio | early | 1-3k bets | 2-1 | 66.7 | 15.4 | 28.7 | -1.0 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 53.7 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 53.7 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.7 | 83.3 | 1.0 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.7 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.7 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.5 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.7 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.7 | 83.3 | 1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.7 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 36.1 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 47.3 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 11-11 | 50.0 | 1.2 | -5.9 | 1.36 |
| consensus_gap+money_level | early | <1k bets | 15-14 | 51.7 | -13.1 | -20.4 | 0.18 |
| consensus_gap+sharp_gap | early | <1k bets | 10-22 | 31.2 | -16.0 | -12.2 | 0.57 |
| follow_move+money_level | early | <1k bets | 16-9 | 64.0 | 16.5 | 21.9 | 0.68 |
| follow_move+sharp_gap | early | <1k bets | 16-6 | 72.7 | 24.3 | 38.8 | 0.86 |
| money_level+sharp_gap | early | <1k bets | 41-21 | 66.1 | 10.4 | 12.1 | 0.71 |
| money_level+money_moving | early | <1k bets | 25-15 | 62.5 | 5.1 | -1.1 | -0.05 |
| money_moving+sharp_gap | early | <1k bets | 25-15 | 62.5 | 11.9 | 8.7 | 0.31 |
| consensus_gap+money_moving | early | <1k bets | 6-10 | 37.5 | -10.4 | -37.6 | -0.27 |
| follow_move+pin_value | early | <1k bets | 11-10 | 52.4 | 3.4 | -1.5 | 0.29 |
| follow_move+money_moving | early | <1k bets | 9-5 | 64.3 | 16.1 | 23.3 | 0.14 |
| consensus_gap+pin_value | early | <1k bets | 11-21 | 34.4 | -11.0 | -35.3 | 0.5 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -24.9 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -24.9 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | <1k bets | 1-1 | 50.0 | 25.1 | -3.7 | -2.15 |
| pin_value+sharp_gap | early | <1k bets | 4-3 | 57.1 | 11.6 | 9.1 | 0.03 |
| money_level+pin_value | early | <1k bets | 3-3 | 50.0 | 0.9 | -4.5 | 1.33 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -53.2 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -52.7 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 0-2 | 0.0 | -50.5 | -100.0 | 2.5 |
| follow_move+rlm_ratio | early | <1k bets | 3-1 | 75.0 | 23.9 | 44.2 | 0.0 |
| money_level+rlm_ratio | early | <1k bets | 2-0 | 100.0 | 47.3 | 93.0 | 0.5 |
| money_moving+rlm_ratio | early | <1k bets | 2-0 | 100.0 | 50.5 | 93.0 | -1.0 |
| rlm_ratio+sharp_gap | early | <1k bets | 3-1 | 75.0 | 23.9 | 44.2 | 0.0 |
| consensus_gap+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -52.7 | -100.0 | 1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 47.3 | 90.9 | 1.0 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 75.1 | 92.6 | 0.5 |
| consensus_gap+money_level | early | pin $1-2k | 4-4 | 50.0 | -14.3 | -22.9 | 0.44 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -32.1 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 4-9 | 30.8 | -7.9 | -42.5 | 0.4 |
| follow_move+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -3.7 | -1.0 | -0.5 |
| follow_move+sharp_gap | early | pin $1-2k | 3-1 | 75.0 | 25.0 | 45.0 | -0.25 |
| money_level+money_moving | early | pin $1-2k | 6-5 | 54.5 | -10.7 | -20.3 | 0.02 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -7.8 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 1-1 | 50.0 | -3.7 | -1.0 | -0.5 |
| money_level+sharp_gap | early | pin $1-2k | 8-4 | 66.7 | 4.1 | 8.4 | -0.41 |
| money_moving+sharp_gap | early | pin $1-2k | 3-5 | 37.5 | -21.4 | -45.3 | -0.06 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.3 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 2-2 | 50.0 | 0.0 | -8.4 | 0.75 |
| follow_move+money_level | early | pin $1-2k | 3-2 | 60.0 | 12.2 | 16.0 | 0.2 |
| follow_move+pin_value | early | pin $1-2k | 4-3 | 57.1 | 7.7 | 6.9 | 0.29 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 46.3 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 1-0 | 100.0 | 53.7 | 90.9 | 0.0 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -24.9 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -25.0 | -62.8 | -0.72 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -24.9 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -24.9 | -100.0 | -4.8 |
| money_level+money_moving | early | pin limit <$1k | 11-7 | 61.1 | 8.1 | 12.1 | 0.53 |
| money_level+sharp_gap | early | pin limit <$1k | 18-14 | 56.2 | 5.1 | 2.3 | 0.25 |
| money_moving+sharp_gap | early | pin limit <$1k | 16-5 | 76.2 | 28.2 | 68.0 | 0.39 |
| money_level+pin_value | early | pin limit <$1k | 8-5 | 61.5 | 10.5 | 16.6 | 0.46 |
| money_moving+pin_value | early | pin limit <$1k | 6-4 | 60.0 | 10.1 | 13.0 | 0.3 |
| pin_value+sharp_gap | early | pin limit <$1k | 11-5 | 68.8 | 18.5 | 30.3 | 0.06 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-7 | 46.2 | -1.0 | -14.2 | 0.46 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -27.0 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 13-17 | 43.3 | -4.9 | -18.8 | 0.49 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.8 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 8-7 | 53.3 | 3.8 | 1.9 | 0.07 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 5.2 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 9-7 | 56.2 | 6.4 | 6.9 | -0.31 |
| follow_move+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 28.4 | 53.6 | -0.4 |
| money_level+rlm_ratio | early | pin limit <$1k | 4-0 | 100.0 | 47.3 | 92.0 | 0.25 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.8 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 4-1 | 80.0 | 28.4 | 53.6 | -0.4 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 23.5 | 72.3 | 0.54 |
| follow_move+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 20.9 | 33.3 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.8 | 28.7 | -1.0 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -52.7 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -52.7 | -100.0 | 1.0 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 75.1 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 75.1 | 92.6 | 0.5 |
