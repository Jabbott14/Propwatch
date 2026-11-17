# CBB scorecard

Generated 2026-11-17 04:12 UTC. 523 graded games (20 finished games had no final score matched and are not graded).

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before tip. Break-even at -110 is 52.4%. CLV = points of closing-line
value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured
on this sample. `edge` is hit% minus that. A signal that is structurally long
favourites or overs beats 50% whenever those run, which is not an edge -- this
sample ran **47.5% favourites** (n=522) and **45.9% overs** (n=523) and **73.8% moneyline favourites** (n=443).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

## EARLY

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 1-1 | 50.0 | 26.2 | 23.8 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | both | 196-217 | 47.5 | 49.4 | -2.0 | -37.35 | -9.0 | 0.15 | 39.5 | DROP: below break-even |
| rlm_ratio | both | 8-6 | 57.1 | 52.6 | 4.6 | +1.43 | 10.2 | 0.0 | 28.6 | keep collecting (14/30) |
| money_level | both | 120-76 | 61.2 | 58.4 | 2.8 | -7.35 | -3.7 | 0.18 | 41.3 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 106-79 | 57.3 | 49.5 | 7.8 | +24.67 | 13.3 | 0.32 | 42.7 | no edge shown yet |
| money_moving | both | 71-50 | 58.7 | 51.1 | 7.5 | +10.07 | 8.3 | 0.14 | 42.1 | no edge shown yet |
| pin_value | both | 43-42 | 50.6 | 47.9 | 2.7 | -3.68 | -4.3 | 0.14 | 41.2 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.5 | -31.5 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 163-223 | 42.2 | 46.5 | -4.3 | -52.48 | -13.6 | 0.31 | 45.6 | DROP: below break-even |
| consensus_gap+money_level | both | 23-22 | 51.1 | 63.1 | -12.0 | -10.62 | -23.6 | 0.25 | 46.7 | no edge shown yet |
| consensus_gap+money_moving | both | 15-19 | 44.1 | 45.8 | -1.7 | -3.69 | -10.9 | 0.17 | 38.2 | no edge shown yet |
| consensus_gap+pin_value | both | 17-27 | 38.6 | 45.7 | -7.0 | -12.16 | -27.6 | 0.43 | 52.3 | DROP: below break-even |
| follow_move+rlm_ratio | both | 8-6 | 57.1 | 52.6 | 4.6 | +1.43 | 10.2 | 0.0 | 28.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 27-18 | 60.0 | 49.8 | 10.2 | +6.54 | 14.5 | 0.51 | 40.0 | no edge shown yet |
| money_level+money_moving | both | 46-27 | 63.0 | 56.9 | 6.1 | +2.78 | 3.8 | 0.06 | 47.9 | PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | both | 10-8 | 55.6 | 50.7 | 4.8 | +0.9 | 5.0 | 0.5 | 50.0 | keep collecting (18/30) |
| money_moving+pin_value | both | 7-5 | 58.3 | 50.1 | 8.2 | +1.13 | 9.4 | 0.42 | 41.7 | keep collecting (12/30) |
| rlm_ratio+sharp_gap | both | 8-6 | 57.1 | 52.6 | 4.6 | +1.43 | 10.2 | 0.0 | 28.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 73-41 | 64.0 | 55.7 | 8.4 | +7.81 | 6.9 | 0.42 | 45.6 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 45-28 | 61.6 | 49.9 | 11.8 | +13.05 | 17.9 | 0.34 | 45.2 | PROMOTE: beats break-even and its own base rate |
| pin_value+sharp_gap | both | 12-7 | 63.2 | 49.3 | 13.9 | +3.75 | 19.8 | -0.15 | 36.8 | keep collecting (19/30) |
| consensus_gap+follow_move | both | 16-16 | 50.0 | 48.6 | 1.4 | -1.95 | -6.1 | 1.09 | 53.1 | no edge shown yet |
| consensus_gap+sharp_gap | both | 19-33 | 36.5 | 46.6 | -10.1 | -4.74 | -9.1 | 0.64 | 46.2 | DROP: below break-even |
| follow_move+money_level | both | 27-24 | 52.9 | 48.7 | 4.3 | +0.56 | 1.1 | 0.47 | 41.2 | no edge shown yet |
| follow_move+pin_value | both | 18-15 | 54.5 | 49.0 | 5.5 | +0.8 | 2.4 | 0.03 | 30.3 | no edge shown yet |
| money_level+rlm_ratio | both | 6-3 | 66.7 | 53.6 | 13.1 | +2.61 | 29.0 | 0.56 | 33.3 | keep collecting (9/30) |
| pin_value+rlm_ratio | both | 2-1 | 66.7 | 51.4 | 15.3 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| follow_move+money_moving | both | 18-12 | 60.0 | 49.1 | 10.9 | +4.43 | 14.8 | 0.37 | 43.3 | no edge shown yet |
| money_moving+rlm_ratio | both | 4-3 | 57.1 | 51.8 | 5.4 | +0.72 | 10.3 | -0.14 | 28.6 | keep collecting (7/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 26.2 | -26.2 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 26.2 | -26.2 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | both | 1-1 | 50.0 | 26.2 | 23.8 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 53.3 | -53.3 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 54.1 | -54.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 1-1 | 50.0 | 54.1 | -4.1 | -0.09 | -4.5 | 0.5 | 50.0 | keep collecting (2/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 26.2 | 73.8 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-1 | 50.0 | 26.2 | 23.8 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | spread | 97-113 | 46.2 | 49.4 | -3.2 | -23.79 | -11.3 | -0.01 | 33.8 | DROP: below break-even |
| follow_move | total | 99-104 | 48.8 | 49.5 | -0.7 | -13.56 | -6.7 | 0.31 | 45.3 | no edge shown yet |
| rlm_ratio | spread | 3-2 | 60.0 | 51.5 | 8.5 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 5-4 | 55.6 | 53.2 | 2.4 | +0.59 | 6.5 | 0.33 | 44.4 | keep collecting (9/30) |
| money_level | moneyline | 65-27 | 70.7 | 69.2 | 1.5 | -8.23 | -8.9 | 0.1 | 45.7 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 16-16 | 50.0 | 49.2 | 0.8 | -1.6 | -5.0 | 0.81 | 46.9 | no edge shown yet |
| money_level | total | 39-33 | 54.2 | 48.7 | 5.4 | +2.48 | 3.4 | -0.01 | 33.3 | no edge shown yet |
| sharp_gap | moneyline | 44-37 | 54.3 | 47.9 | 6.4 | +10.4 | 12.8 | 0.3 | 49.4 | no edge shown yet |
| sharp_gap | spread | 19-14 | 57.6 | 49.8 | 7.8 | +3.09 | 9.4 | 0.61 | 36.4 | no edge shown yet |
| sharp_gap | total | 43-28 | 60.6 | 51.1 | 9.5 | +11.17 | 15.7 | 0.21 | 38.0 | no edge shown yet |
| money_moving | moneyline | 27-26 | 50.9 | 53.1 | -2.2 | -5.7 | -10.8 | 0.1 | 52.8 | no edge shown yet |
| money_moving | spread | 17-4 | 81.0 | 49.2 | 31.8 | +11.27 | 53.7 | 0.14 | 38.1 | keep collecting (21/30) |
| money_moving | total | 27-20 | 57.4 | 49.7 | 7.7 | +4.51 | 9.6 | 0.17 | 31.9 | no edge shown yet |
| pin_value | moneyline | 1-5 | 16.7 | 26.2 | -9.5 | -4.02 | -67.0 | -0.02 | 66.7 | keep collecting (6/30) |
| pin_value | spread | 22-17 | 56.4 | 49.3 | 7.1 | +2.35 | 6.0 | 0.28 | 41.0 | no edge shown yet |
| pin_value | total | 20-20 | 50.0 | 49.8 | 0.2 | -2.01 | -5.0 | 0.03 | 37.5 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.5 | -19.2 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 65-121 | 34.9 | 43.6 | -8.7 | -37.19 | -20.0 | -0.01 | 42.5 | DROP: below break-even |
| consensus_gap | spread | 53-49 | 52.0 | 49.2 | 2.8 | -2.76 | -2.7 | 0.45 | 44.1 | no edge shown yet |
| consensus_gap | total | 45-53 | 45.9 | 49.3 | -3.4 | -12.52 | -12.8 | 0.77 | 53.1 | no edge shown yet |
| money_level+sharp_gap | moneyline | 34-12 | 73.9 | 64.5 | 9.4 | +1.42 | 3.1 | 0.37 | 56.5 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+pin_value | moneyline | 1-5 | 16.7 | 26.2 | -9.5 | -4.02 | -67.0 | -0.02 | 66.7 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_level+money_moving | moneyline | 18-9 | 66.7 | 70.3 | -3.6 | -4.76 | -17.6 | -0.31 | 55.6 | keep collecting (27/30) |
| consensus_gap+sharp_gap | moneyline | 11-24 | 31.4 | 45.2 | -13.8 | -2.71 | -7.7 | 0.55 | 48.6 | DROP: below break-even |
| consensus_gap+money_level | moneyline | 16-14 | 53.3 | 70.6 | -17.3 | -8.68 | -28.9 | -0.09 | 46.7 | INVERT candidate: wrong well beyond its base rate |
| money_moving+sharp_gap | moneyline | 16-13 | 55.2 | 49.2 | 6.0 | +1.78 | 6.1 | 0.42 | 62.1 | keep collecting (29/30) |
| consensus_gap+money_moving | moneyline | 7-18 | 28.0 | 45.2 | -17.2 | -9.63 | -38.5 | 0.27 | 48.0 | keep collecting (25/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 26.2 | -26.2 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 26.2 | -26.2 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | moneyline | 1-1 | 50.0 | 26.2 | 23.8 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 26.2 | -26.2 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 26.2 | 73.8 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 4-5 | 44.4 | 47.5 | -3.1 | -1.59 | -17.7 | 1.67 | 66.7 | keep collecting (9/30) |
| consensus_gap+money_moving | spread | 4-0 | 100.0 | 47.5 | 52.5 | +3.41 | 85.2 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_value | spread | 9-8 | 52.9 | 48.4 | 4.6 | -0.31 | -1.8 | 0.53 | 52.9 | keep collecting (17/30) |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.5 | 8.5 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 48.8 | 13.7 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 9-4 | 69.2 | 48.7 | 20.6 | +4.21 | 32.4 | 0.77 | 61.5 | keep collecting (13/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.9 | -6.1 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.5 | 10.5 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 51.5 | 8.5 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 13-11 | 54.2 | 49.2 | 5.0 | +0.71 | 3.0 | 0.96 | 41.7 | keep collecting (24/30) |
| money_moving+sharp_gap | spread | 9-3 | 75.0 | 49.2 | 25.8 | +5.13 | 42.7 | 0.42 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.2 | 17.5 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 8-8 | 50.0 | 48.1 | 1.9 | -1.18 | -7.4 | 0.94 | 43.8 | keep collecting (16/30) |
| consensus_gap+sharp_gap | spread | 4-3 | 57.1 | 47.5 | 9.6 | +0.41 | 5.8 | 2.14 | 71.4 | keep collecting (7/30) |
| follow_move+money_level | spread | 11-8 | 57.9 | 48.6 | 9.3 | +2.04 | 10.7 | 0.63 | 42.1 | keep collecting (19/30) |
| follow_move+pin_value | spread | 11-7 | 61.1 | 48.9 | 12.2 | +2.56 | 14.2 | 0.33 | 33.3 | keep collecting (18/30) |
| follow_move+money_moving | spread | 9-1 | 90.0 | 48.0 | 42.0 | +7.22 | 72.2 | 0.2 | 40.0 | keep collecting (10/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 52.5 | 14.2 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.5 | -52.5 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 19-14 | 57.6 | 49.1 | 8.4 | +3.34 | 10.1 | 0.09 | 36.4 | no edge shown yet |
| money_level+sharp_gap | total | 26-18 | 59.1 | 50.0 | 9.1 | +5.68 | 12.9 | 0.18 | 36.4 | no edge shown yet |
| money_moving+sharp_gap | total | 20-12 | 62.5 | 50.8 | 11.7 | +6.14 | 19.2 | 0.25 | 31.2 | no edge shown yet |
| money_level+pin_value | total | 7-4 | 63.6 | 51.9 | 11.8 | +2.32 | 21.1 | 0.36 | 36.4 | keep collecting (11/30) |
| money_moving+pin_value | total | 4-3 | 57.1 | 50.6 | 6.6 | +0.56 | 8.0 | 0.29 | 28.6 | keep collecting (7/30) |
| pin_value+sharp_gap | total | 10-5 | 66.7 | 50.8 | 15.8 | +4.01 | 26.7 | 0.0 | 33.3 | keep collecting (15/30) |
| follow_move+money_level | total | 16-16 | 50.0 | 48.7 | 1.3 | -1.47 | -4.6 | 0.38 | 40.6 | no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.2 | -2.5 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 5-4 | 55.6 | 53.2 | 2.4 | +0.59 | 6.5 | 0.33 | 44.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 17-12 | 58.6 | 50.4 | 8.2 | +3.46 | 11.9 | 0.45 | 41.4 | keep collecting (29/30) |
| money_level+rlm_ratio | total | 4-2 | 66.7 | 54.1 | 12.6 | +1.68 | 28.0 | 0.83 | 50.0 | keep collecting (6/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 51.4 | 15.3 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 5-4 | 55.6 | 53.2 | 2.4 | +0.59 | 6.5 | 0.33 | 44.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 9-11 | 45.0 | 49.6 | -4.6 | -2.8 | -14.0 | 0.45 | 45.0 | keep collecting (20/30) |
| consensus_gap+money_level | total | 3-3 | 50.0 | 48.6 | 1.4 | -0.34 | -5.7 | -0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 47.5 | 32.5 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 49.0 | -15.7 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 4-6 | 40.0 | 50.8 | -10.8 | -2.44 | -24.4 | -0.1 | 20.0 | keep collecting (10/30) |
| money_moving+rlm_ratio | total | 2-3 | 40.0 | 52.5 | -12.5 | -1.14 | -22.8 | 0.2 | 40.0 | keep collecting (5/30) |
| consensus_gap+follow_move | total | 8-8 | 50.0 | 49.0 | 1.0 | -0.76 | -4.8 | 1.25 | 62.5 | keep collecting (16/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 54.1 | -54.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 54.1 | -54.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 1-1 | 50.0 | 54.1 | -4.1 | -0.09 | -4.5 | 0.5 | 50.0 | keep collecting (2/30) |

## CLOSE

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 105-107 | 49.5 | 42.8 | 6.7 | +35.25 | 16.6 |  |  | no edge shown yet |
| follow_move | both | 424-435 | 49.4 | 49.7 | -0.3 | -49.63 | -5.8 |  |  | DROP: below break-even |
| rlm_ratio | both | 126-97 | 56.5 | 51.6 | 4.9 | +18.15 | 8.1 |  |  | no edge shown yet |
| money_level | both | 817-616 | 57.0 | 55.4 | 1.7 | -63.08 | -4.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 640-745 | 46.2 | 47.4 | -1.2 | -83.38 | -6.0 |  |  | DROP: below break-even |
| money_moving | both | 636-750 | 45.9 | 47.5 | -1.6 | -96.49 | -7.0 |  |  | DROP: below break-even |
| pin_value | both | 271-282 | 49.0 | 47.3 | 1.7 | -11.65 | -2.1 |  |  | DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 50.8 | 15.8 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 262-390 | 40.2 | 45.9 | -5.7 | -87.18 | -13.4 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 62-57 | 52.1 | 47.8 | 4.3 | -3.24 | -2.7 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 113-209 | 35.1 | 42.9 | -7.8 | -30.97 | -9.6 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 19-33 | 36.5 | 36.5 | 0.1 | +12.47 | 24.0 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 107-132 | 44.8 | 44.3 | 0.5 | -9.98 | -4.2 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | both | 16-12 | 57.1 | 48.5 | 8.6 | +2.02 | 7.2 |  |  | keep collecting (28/30) |
| consensus_gap+sharp_gap | both | 114-213 | 34.9 | 42.5 | -7.6 | -31.81 | -9.7 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 278-296 | 48.4 | 49.9 | -1.5 | -43.97 | -7.7 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 66-46 | 58.9 | 52.1 | 6.9 | +14.64 | 13.1 |  |  | no edge shown yet |
| follow_move+pin_value | both | 97-85 | 53.3 | 49.0 | 4.3 | +0.91 | 0.5 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 126-97 | 56.5 | 51.6 | 4.9 | +18.15 | 8.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 283-292 | 49.2 | 50.0 | -0.8 | -35.21 | -6.1 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 102-106 | 49.0 | 42.7 | 6.3 | +33.52 | 16.1 |  |  | no edge shown yet |
| money_moving+pin_value | both | 117-140 | 45.5 | 46.4 | -0.8 | -9.81 | -3.8 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 122-96 | 56.0 | 51.5 | 4.4 | +15.42 | 7.1 |  |  | no edge shown yet |
| money_moving+sharp_gap | both | 615-722 | 46.0 | 47.4 | -1.4 | -83.28 | -6.2 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 29-26 | 52.7 | 45.4 | 7.3 | +17.65 | 32.1 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 66-46 | 58.9 | 52.1 | 6.9 | +14.64 | 13.1 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 105-107 | 49.5 | 42.8 | 6.7 | +35.25 | 16.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 27-19 | 58.7 | 50.6 | 8.1 | +5.18 | 11.3 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 119-139 | 46.1 | 46.5 | -0.4 | -7.06 | -2.7 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 126-97 | 56.5 | 51.6 | 4.9 | +18.15 | 8.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+money_moving | both | 449-413 | 52.1 | 52.0 | 0.1 | -39.48 | -4.6 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 449-408 | 52.4 | 51.9 | 0.5 | -31.3 | -3.7 |  |  | no edge shown yet |
| follow_move+money_level | both | 251-264 | 48.7 | 49.1 | -0.3 | -36.88 | -7.2 |  |  | DROP: below break-even |
| money_level+rlm_ratio | both | 69-54 | 56.1 | 51.2 | 4.9 | +8.85 | 7.2 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 159-141 | 53.0 | 56.2 | -3.2 | -25.54 | -8.5 |  |  | no edge shown yet |
| money_level+pin_value | both | 127-129 | 49.6 | 48.8 | 0.8 | -18.65 | -7.3 |  |  | no edge shown yet |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | both | 50-31 | 61.7 | 48.1 | 13.6 | +19.11 | 23.6 |  |  | PROMOTE: beats break-even and its own base rate |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 54.1 | 45.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 28-54 | 34.1 | 27.9 | 6.2 | +17.78 | 21.7 |  |  | DROP: below break-even |
| pin_rlm | spread | 18-16 | 52.9 | 50.9 | 2.1 | +0.29 | 0.9 |  |  | no edge shown yet |
| pin_rlm | total | 59-37 | 61.5 | 52.7 | 8.8 | +17.18 | 17.9 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move | spread | 195-199 | 49.5 | 49.3 | 0.2 | -22.59 | -5.7 |  |  | no edge shown yet |
| follow_move | total | 229-236 | 49.2 | 50.0 | -0.8 | -27.04 | -5.8 |  |  | no edge shown yet |
| rlm_ratio | spread | 33-34 | 49.3 | 50.0 | -0.8 | -3.97 | -5.9 |  |  | no edge shown yet |
| rlm_ratio | total | 93-63 | 59.6 | 52.2 | 7.4 | +22.12 | 14.2 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level | moneyline | 320-115 | 73.6 | 69.4 | 4.1 | -12.04 | -2.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 239-248 | 49.1 | 49.2 | -0.1 | -32.57 | -6.7 |  |  | no edge shown yet |
| money_level | total | 258-253 | 50.5 | 49.3 | 1.2 | -18.47 | -3.6 |  |  | no edge shown yet |
| sharp_gap | moneyline | 144-257 | 35.9 | 40.3 | -4.4 | -45.92 | -11.5 |  |  | DROP: below break-even |
| sharp_gap | spread | 248-233 | 51.6 | 49.5 | 2.0 | -9.06 | -1.9 |  |  | no edge shown yet |
| sharp_gap | total | 248-255 | 49.3 | 50.9 | -1.6 | -28.4 | -5.6 |  |  | no edge shown yet |
| money_moving | moneyline | 148-251 | 37.1 | 41.0 | -3.9 | -40.59 | -10.2 |  |  | DROP: below break-even |
| money_moving | spread | 245-236 | 50.9 | 49.5 | 1.4 | -14.94 | -3.1 |  |  | no edge shown yet |
| money_moving | total | 243-263 | 48.0 | 50.8 | -2.8 | -40.96 | -8.1 |  |  | DROP: below break-even |
| pin_value | moneyline | 13-44 | 22.8 | 28.7 | -5.9 | -2.9 | -5.1 |  |  | DROP: below break-even |
| pin_value | spread | 127-114 | 52.7 | 49.6 | 3.1 | -2.65 | -1.1 |  |  | no edge shown yet |
| pin_value | total | 131-124 | 51.4 | 49.2 | 2.2 | -6.1 | -2.4 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.5 | 47.5 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 105-231 | 31.2 | 43.6 | -12.4 | -65.09 | -19.4 |  |  | DROP: below break-even |
| consensus_gap | spread | 74-67 | 52.5 | 49.1 | 3.4 | -3.8 | -2.7 |  |  | no edge shown yet |
| consensus_gap | total | 83-92 | 47.4 | 47.8 | -0.4 | -18.29 | -10.4 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 100-61 | 62.1 | 62.6 | -0.5 | -3.6 | -2.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 96-60 | 61.5 | 62.2 | -0.7 | -3.1 | -2.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 134-241 | 35.7 | 40.0 | -4.3 | -39.07 | -10.4 |  |  | DROP: below break-even |
| consensus_gap+money_level | moneyline | 70-51 | 57.9 | 68.7 | -10.8 | -12.95 | -10.7 |  |  | no edge shown yet |
| consensus_gap+money_moving | moneyline | 36-130 | 21.7 | 37.7 | -16.0 | -18.8 | -11.3 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+sharp_gap | moneyline | 37-135 | 21.5 | 37.0 | -15.5 | -20.65 | -12.0 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_rlm | moneyline | 10-23 | 30.3 | 29.1 | 1.2 | +14.65 | 44.4 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 28-53 | 34.6 | 27.9 | 6.6 | +18.78 | 23.2 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 28-54 | 34.1 | 27.9 | 6.2 | +17.78 | 21.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 12-38 | 24.0 | 29.0 | -5.0 | +1.58 | 3.2 |  |  | DROP: below break-even |
| money_moving+pin_value | moneyline | 7-28 | 20.0 | 26.2 | -6.2 | +5.27 | 15.1 |  |  | DROP: below break-even |
| pin_rlm+pin_value | moneyline | 5-8 | 38.5 | 26.2 | 12.3 | +14.07 | 108.2 |  |  | keep collecting (13/30) |
| pin_value+sharp_gap | moneyline | 7-28 | 20.0 | 26.2 | -6.2 | +5.27 | 15.1 |  |  | DROP: below break-even |
| money_level+pin_rlm | moneyline | 9-7 | 56.2 | 32.1 | 24.1 | +5.65 | 35.3 |  |  | keep collecting (16/30) |
| money_level+pin_value | moneyline | 3-1 | 75.0 | 61.9 | 13.1 | +0.31 | 7.8 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 31-25 | 55.4 | 48.4 | 7.0 | +1.4 | 2.5 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 41-36 | 53.2 | 48.9 | 4.3 | -1.02 | -1.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 50-41 | 54.9 | 49.0 | 5.9 | +1.53 | 1.7 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.33 | -38.9 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | spread | 40-36 | 52.6 | 49.1 | 3.5 | -1.91 | -2.5 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 124-125 | 49.8 | 49.0 | 0.8 | -13.38 | -5.4 |  |  | no edge shown yet |
| follow_move+pin_rlm | spread | 15-15 | 50.0 | 50.8 | -0.8 | -1.37 | -4.6 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 49-40 | 55.1 | 48.9 | 6.1 | +2.78 | 3.1 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 33-34 | 49.3 | 50.0 | -0.8 | -3.97 | -5.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 125-124 | 50.2 | 49.1 | 1.1 | -11.25 | -4.5 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 16-16 | 50.0 | 50.8 | -0.8 | -1.53 | -4.8 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 60-58 | 50.8 | 49.2 | 1.7 | -6.09 | -5.2 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 31-33 | 48.4 | 49.9 | -1.5 | -4.9 | -7.7 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 240-228 | 51.3 | 49.5 | 1.8 | -11.44 | -2.4 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 6-7 | 46.2 | 50.2 | -4.0 | -1.79 | -13.8 |  |  | keep collecting (13/30) |
| pin_rlm+rlm_ratio | spread | 15-15 | 50.0 | 50.8 | -0.8 | -1.37 | -4.6 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 18-16 | 52.9 | 50.9 | 2.1 | +0.29 | 0.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 5-6 | 45.5 | 49.3 | -3.9 | -1.72 | -15.6 |  |  | keep collecting (11/30) |
| pin_value+sharp_gap | spread | 60-58 | 50.8 | 49.3 | 1.6 | -6.16 | -5.2 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 33-34 | 49.3 | 50.0 | -0.8 | -3.97 | -5.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 120-126 | 48.8 | 48.7 | 0.0 | -18.02 | -7.3 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 17-19 | 47.2 | 49.6 | -2.4 | -3.71 | -10.3 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 187-180 | 51.0 | 49.2 | 1.8 | -11.51 | -3.1 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 50-41 | 54.9 | 48.7 | 6.2 | +1.84 | 2.0 |  |  | no edge shown yet |
| money_level+money_moving | spread | 186-181 | 50.7 | 49.1 | 1.5 | -13.42 | -3.7 |  |  | no edge shown yet |
| money_level+pin_value | spread | 65-67 | 49.2 | 49.0 | 0.3 | -10.78 | -8.2 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 9-6 | 60.0 | 50.2 | 9.8 | +2.01 | 13.4 |  |  | keep collecting (15/30) |
| money_level+money_moving | total | 163-171 | 48.8 | 50.1 | -1.3 | -22.45 | -6.7 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 166-168 | 49.7 | 50.2 | -0.5 | -16.69 | -5.0 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 241-253 | 48.8 | 50.9 | -2.1 | -32.78 | -6.6 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 39-49 | 44.3 | 46.8 | -2.5 | -14.43 | -16.4 |  |  | DROP: below break-even |
| consensus_gap+pin_value | total | 45-53 | 45.9 | 47.7 | -1.7 | -13.09 | -13.4 |  |  | no edge shown yet |
| follow_move+money_moving | total | 154-171 | 47.4 | 50.6 | -3.2 | -30.59 | -9.4 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 158-168 | 48.5 | 50.7 | -2.2 | -23.97 | -7.4 |  |  | no edge shown yet |
| money_level+pin_value | total | 59-61 | 49.2 | 48.1 | 1.1 | -8.18 | -6.8 |  |  | no edge shown yet |
| follow_move+money_level | total | 131-138 | 48.7 | 49.4 | -0.7 | -18.86 | -7.0 |  |  | no edge shown yet |
| follow_move+pin_value | total | 48-45 | 51.6 | 49.2 | 2.5 | -1.87 | -2.0 |  |  | no edge shown yet |
| money_moving+pin_value | total | 50-54 | 48.1 | 50.0 | -1.9 | -8.99 | -8.6 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 52-53 | 49.5 | 50.1 | -0.6 | -6.17 | -5.9 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 36-43 | 45.6 | 48.0 | -2.4 | -11.15 | -14.1 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 37-42 | 46.8 | 48.1 | -1.2 | -9.24 | -11.7 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 31-32 | 49.2 | 47.2 | 2.0 | -4.64 | -7.4 |  |  | no edge shown yet |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pin_rlm | total | 6-7 | 46.2 | 49.1 | -2.9 | -1.7 | -13.0 |  |  | keep collecting (13/30) |
| consensus_gap+rlm_ratio | total | 14-8 | 63.6 | 48.1 | 15.5 | +4.35 | 19.8 |  |  | keep collecting (22/30) |
| follow_move+pin_rlm | total | 51-31 | 62.2 | 52.5 | 9.7 | +16.01 | 19.5 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+rlm_ratio | total | 93-63 | 59.6 | 52.2 | 7.4 | +22.12 | 14.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 32-18 | 64.0 | 52.6 | 11.4 | +11.45 | 22.9 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 52-35 | 59.8 | 51.8 | 7.9 | +12.56 | 14.4 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 58-37 | 61.1 | 52.6 | 8.4 | +16.27 | 17.1 |  |  | PROMOTE: beats break-even and its own base rate |
| money_moving+rlm_ratio | total | 91-63 | 59.1 | 52.2 | 6.9 | +20.32 | 13.2 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_rlm+pin_value | total | 18-11 | 62.1 | 51.8 | 10.2 | +5.37 | 18.5 |  |  | keep collecting (29/30) |
| pin_rlm+rlm_ratio | total | 51-31 | 62.2 | 52.5 | 9.7 | +16.01 | 19.5 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_rlm+sharp_gap | total | 59-37 | 61.5 | 52.7 | 8.8 | +17.18 | 17.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 22-13 | 62.9 | 51.1 | 11.8 | +6.89 | 19.7 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 93-63 | 59.6 | 52.2 | 7.4 | +22.12 | 14.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 54.1 | 45.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_rlm | close | 1-3k bets | 63-65 | 49.2 | 5.7 | 18.6 |  |
| pin_rlm | close | 3k+ bets | 21-22 | 48.8 | 7.9 | 13.7 |  |
| pin_rlm | close | <1k bets | 21-20 | 51.2 | 8.7 | 13.7 |  |
| pin_rlm | close | pin $1-2k | 46-41 | 52.9 | 8.1 | 22.1 |  |
| pin_rlm | close | pin $2k+ | 24-50 | 32.4 | -1.9 | -12.2 |  |
| pin_rlm | close | pin limit <$1k | 35-16 | 68.6 | 16.9 | 49.1 |  |
| follow_move | close | 1-3k bets | 274-267 | 50.6 | 1.0 | -3.3 |  |
| follow_move | close | 3k+ bets | 90-96 | 48.4 | -1.2 | -7.7 |  |
| follow_move | close | <1k bets | 60-72 | 45.5 | -4.3 | -13.1 |  |
| follow_move | close | pin $1-2k | 142-173 | 45.1 | -4.3 | -14.0 |  |
| follow_move | close | pin $2k+ | 78-81 | 49.1 | -0.7 | -6.4 |  |
| follow_move | close | pin limit <$1k | 90-78 | 53.6 | 3.2 | 2.5 |  |
| rlm_ratio | close | 1-3k bets | 80-67 | 54.4 | 2.8 | 4.0 |  |
| rlm_ratio | close | 3k+ bets | 27-17 | 61.4 | 10.5 | 17.3 |  |
| rlm_ratio | close | <1k bets | 19-13 | 59.4 | 7.2 | 14.4 |  |
| rlm_ratio | close | pin $1-2k | 44-36 | 55.0 | 4.1 | 5.0 |  |
| rlm_ratio | close | pin $2k+ | 13-16 | 44.8 | -5.9 | -14.9 |  |
| rlm_ratio | close | pin limit <$1k | 37-20 | 64.9 | 12.1 | 24.8 |  |
| money_level | close | 1-3k bets | 517-357 | 59.2 | 3.7 | -0.9 |  |
| money_level | close | 3k+ bets | 172-145 | 54.3 | -0.8 | -6.4 |  |
| money_level | close | <1k bets | 128-113 | 53.1 | -2.6 | -14.3 |  |
| money_level | close | pin $1-2k | 238-213 | 52.8 | -0.8 | -6.2 |  |
| money_level | close | pin $2k+ | 203-159 | 56.1 | -1.4 | -8.0 |  |
| money_level | close | pin limit <$1k | 96-98 | 49.5 | 0.0 | -5.8 |  |
| sharp_gap | close | 1-3k bets | 380-461 | 45.2 | -2.1 | -8.7 |  |
| sharp_gap | close | 3k+ bets | 154-157 | 49.5 | 2.6 | 7.3 |  |
| sharp_gap | close | <1k bets | 106-126 | 45.7 | -2.8 | -13.7 |  |
| sharp_gap | close | pin $1-2k | 214-225 | 48.7 | -0.1 | -2.3 |  |
| sharp_gap | close | pin $2k+ | 157-192 | 45.0 | -0.8 | -7.4 |  |
| sharp_gap | close | pin limit <$1k | 94-93 | 50.3 | -0.7 | 1.3 |  |
| money_moving | close | 1-3k bets | 379-463 | 45.0 | -2.5 | -9.7 |  |
| money_moving | close | 3k+ bets | 153-160 | 48.9 | 1.6 | 4.9 |  |
| money_moving | close | <1k bets | 104-126 | 45.2 | -2.8 | -12.5 |  |
| money_moving | close | pin $1-2k | 209-231 | 47.5 | -1.2 | -4.0 |  |
| money_moving | close | pin $2k+ | 159-189 | 45.7 | -0.0 | -6.1 |  |
| money_moving | close | pin limit <$1k | 91-98 | 48.1 | -2.6 | -2.8 |  |
| pin_value | close | 1-3k bets | 165-175 | 48.5 | 1.0 | -3.3 |  |
| pin_value | close | 3k+ bets | 57-63 | 47.5 | 0.2 | -5.3 |  |
| pin_value | close | <1k bets | 49-44 | 52.7 | 6.4 | 6.4 |  |
| pin_value | close | pin $1-2k | 127-143 | 47.0 | -0.8 | -7.8 |  |
| pin_value | close | pin $2k+ | 76-84 | 47.5 | 2.1 | -0.5 |  |
| pin_value | close | pin limit <$1k | 68-55 | 55.3 | 6.9 | 8.4 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.5 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.5 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 161-236 | 40.6 | -5.8 | -14.9 |  |
| consensus_gap | close | 3k+ bets | 64-82 | 43.8 | -2.8 | 2.8 |  |
| consensus_gap | close | <1k bets | 37-71 | 34.3 | -9.4 | -28.7 |  |
| consensus_gap | close | pin $1-2k | 84-105 | 44.4 | -3.3 | -4.0 |  |
| consensus_gap | close | pin $2k+ | 67-87 | 43.5 | -5.5 | -11.6 |  |
| consensus_gap | close | pin limit <$1k | 39-39 | 50.0 | 1.9 | -1.1 |  |
| consensus_gap+follow_move | close | 1-3k bets | 43-34 | 55.8 | 8.2 | 4.4 |  |
| consensus_gap+money_level | close | 1-3k bets | 108-80 | 57.4 | 0.8 | 1.0 |  |
| consensus_gap+money_moving | close | 1-3k bets | 71-129 | 35.5 | -7.7 | -13.1 |  |
| consensus_gap+pin_value | close | 1-3k bets | 65-88 | 42.5 | -2.3 | -9.8 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 71-132 | 35.0 | -7.7 | -14.2 |  |
| follow_move+money_level | close | 1-3k bets | 172-167 | 50.7 | 1.6 | -3.4 |  |
| follow_move+money_moving | close | 1-3k bets | 187-192 | 49.3 | -0.6 | -5.9 |  |
| follow_move+pin_value | close | 1-3k bets | 58-51 | 53.2 | 4.2 | 0.3 |  |
| follow_move+sharp_gap | close | 1-3k bets | 188-189 | 49.9 | -0.1 | -4.9 |  |
| money_level+money_moving | close | 1-3k bets | 277-246 | 53.0 | 1.0 | -2.0 |  |
| money_level+pin_value | close | 1-3k bets | 82-78 | 51.2 | 2.4 | -3.8 |  |
| money_level+sharp_gap | close | 1-3k bets | 275-244 | 53.0 | 1.2 | -1.3 |  |
| money_moving+pin_value | close | 1-3k bets | 75-90 | 45.5 | -1.4 | -5.9 |  |
| money_moving+sharp_gap | close | 1-3k bets | 367-447 | 45.1 | -2.2 | -8.8 |  |
| pin_value+sharp_gap | close | 1-3k bets | 77-92 | 45.6 | -1.3 | -5.9 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 13-21 | 38.2 | 1.0 | 28.5 |  |
| money_level+pin_rlm | close | 1-3k bets | 32-19 | 62.7 | 11.9 | 20.6 |  |
| pin_rlm+pin_value | close | 1-3k bets | 19-17 | 52.8 | 7.1 | 39.7 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 63-65 | 49.2 | 5.7 | 18.6 |  |
| money_moving+pin_rlm | close | 1-3k bets | 61-64 | 48.8 | 5.3 | 18.4 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 13-7 | 65.0 | 16.6 | 21.6 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 80-67 | 54.4 | 2.8 | 4.0 |  |
| money_level+rlm_ratio | close | 1-3k bets | 44-37 | 54.3 | 3.1 | 3.8 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 78-67 | 53.8 | 2.2 | 2.9 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 80-67 | 54.4 | 2.8 | 4.0 |  |
| follow_move+pin_rlm | close | 1-3k bets | 39-30 | 56.5 | 4.4 | 8.3 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 39-30 | 56.5 | 4.4 | 8.3 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 18-13 | 58.1 | 7.5 | 10.0 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 45.9 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 16-14 | 53.3 | 5.5 | -0.4 |  |
| consensus_gap+money_moving | close | 3k+ bets | 27-44 | 38.0 | -5.1 | 16.7 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-5 | 37.5 | -2.9 | 19.3 |  |
| consensus_gap+pin_value | close | 3k+ bets | 30-30 | 50.0 | 5.4 | 4.0 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 3-3 | 50.0 | 1.6 | -5.2 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 28-44 | 38.9 | -4.2 | 20.4 |  |
| follow_move+money_moving | close | 3k+ bets | 58-60 | 49.2 | -0.4 | -6.6 |  |
| follow_move+pin_rlm | close | 3k+ bets | 14-10 | 58.3 | 7.0 | 12.4 |  |
| follow_move+pin_value | close | 3k+ bets | 23-23 | 50.0 | 1.0 | -6.2 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 27-17 | 61.4 | 10.5 | 17.3 |  |
| follow_move+sharp_gap | close | 3k+ bets | 62-59 | 51.2 | 1.6 | -2.5 |  |
| money_moving+pin_rlm | close | 3k+ bets | 20-22 | 47.6 | 7.0 | 11.7 |  |
| money_moving+pin_value | close | 3k+ bets | 27-34 | 44.3 | -1.3 | -5.3 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 25-16 | 61.0 | 10.3 | 16.3 |  |
| money_moving+sharp_gap | close | 3k+ bets | 146-150 | 49.3 | 2.3 | 6.9 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-6 | 45.5 | -0.9 | -13.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 14-10 | 58.3 | 7.0 | 12.4 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 21-22 | 48.8 | 7.9 | 13.7 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 6-5 | 54.5 | 4.5 | 2.8 |  |
| pin_value+sharp_gap | close | 3k+ bets | 27-32 | 45.8 | 0.2 | -2.0 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 27-17 | 61.4 | 10.5 | 17.3 |  |
| money_level+money_moving | close | 3k+ bets | 102-91 | 52.8 | 1.1 | -2.1 |  |
| money_level+sharp_gap | close | 3k+ bets | 101-88 | 53.4 | 2.0 | 0.0 |  |
| follow_move+money_level | close | 3k+ bets | 52-54 | 49.1 | 0.3 | -6.8 |  |
| money_level+rlm_ratio | close | 3k+ bets | 15-8 | 65.2 | 15.2 | 23.7 |  |
| consensus_gap+money_level | close | 3k+ bets | 35-35 | 50.0 | -5.5 | -14.1 |  |
| money_level+pin_value | close | 3k+ bets | 28-34 | 45.2 | -3.1 | -16.6 |  |
| money_level+pin_rlm | close | 3k+ bets | 9-6 | 60.0 | 17.2 | 38.3 |  |
| money_level+money_moving | close | <1k bets | 70-75 | 48.3 | -4.4 | -16.7 |  |
| money_level+sharp_gap | close | <1k bets | 73-75 | 49.3 | -3.9 | -16.1 |  |
| money_moving+sharp_gap | close | <1k bets | 102-124 | 45.1 | -3.1 | -13.7 |  |
| consensus_gap+money_level | close | <1k bets | 16-26 | 38.1 | -17.5 | -41.8 |  |
| consensus_gap+money_moving | close | <1k bets | 15-36 | 29.4 | -11.9 | -32.8 |  |
| consensus_gap+pin_value | close | <1k bets | 12-14 | 46.2 | 5.5 | 9.9 |  |
| consensus_gap+sharp_gap | close | <1k bets | 15-37 | 28.8 | -12.2 | -34.1 |  |
| money_level+pin_value | close | <1k bets | 17-17 | 50.0 | 0.6 | -6.7 |  |
| money_moving+pin_value | close | <1k bets | 15-16 | 48.4 | 2.8 | 10.3 |  |
| pin_value+sharp_gap | close | <1k bets | 15-15 | 50.0 | 3.8 | 13.9 |  |
| follow_move+money_moving | close | <1k bets | 33-44 | 42.9 | -7.4 | -17.8 |  |
| follow_move+sharp_gap | close | <1k bets | 33-44 | 42.9 | -7.5 | -17.8 |  |
| follow_move+money_level | close | <1k bets | 27-43 | 38.6 | -10.9 | -26.2 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -0.9 | 12.2 |  |
| money_moving+pin_rlm | close | <1k bets | 21-20 | 51.2 | 8.7 | 13.7 |  |
| pin_rlm+sharp_gap | close | <1k bets | 21-20 | 51.2 | 8.7 | 13.7 |  |
| consensus_gap+follow_move | close | <1k bets | 3-9 | 25.0 | -23.2 | -54.1 |  |
| follow_move+pin_rlm | close | <1k bets | 13-6 | 68.4 | 15.9 | 31.3 |  |
| follow_move+pin_value | close | <1k bets | 16-11 | 59.3 | 10.0 | 12.6 |  |
| follow_move+rlm_ratio | close | <1k bets | 19-13 | 59.4 | 7.2 | 14.4 |  |
| money_moving+rlm_ratio | close | <1k bets | 19-13 | 59.4 | 7.2 | 14.4 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 19.7 | 60.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 13-6 | 68.4 | 15.9 | 31.3 |  |
| pin_value+rlm_ratio | close | <1k bets | 3-1 | 75.0 | 22.5 | 43.9 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 19-13 | 59.4 | 7.2 | 14.4 |  |
| money_level+rlm_ratio | close | <1k bets | 10-9 | 52.6 | 0.3 | 1.6 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 15.7 | 19.0 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 23-24 | 48.9 | 1.2 | -8.6 |  |
| consensus_gap+money_moving | close | pin $1-2k | 44-57 | 43.6 | -3.5 | -3.5 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 12-16 | 42.9 | 2.3 | 32.5 |  |
| consensus_gap+pin_value | close | pin $1-2k | 50-63 | 44.2 | -0.4 | -9.5 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 9-7 | 56.2 | 8.1 | 5.1 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 44-54 | 44.9 | -1.5 | -0.6 |  |
| follow_move+money_moving | close | pin $1-2k | 97-119 | 44.9 | -4.7 | -14.4 |  |
| follow_move+pin_rlm | close | pin $1-2k | 31-21 | 59.6 | 7.8 | 14.3 |  |
| follow_move+pin_value | close | pin $1-2k | 44-48 | 47.8 | -1.3 | -9.9 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 44-36 | 55.0 | 4.1 | 5.0 |  |
| follow_move+sharp_gap | close | pin $1-2k | 99-118 | 45.6 | -4.0 | -13.0 |  |
| money_moving+pin_rlm | close | pin $1-2k | 44-40 | 52.4 | 7.6 | 21.9 |  |
| money_moving+pin_value | close | pin $1-2k | 51-69 | 42.5 | -4.9 | -15.6 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 43-35 | 55.1 | 4.3 | 5.2 |  |
| money_moving+sharp_gap | close | pin $1-2k | 205-221 | 48.1 | -0.6 | -3.2 |  |
| pin_rlm+pin_value | close | pin $1-2k | 11-16 | 40.7 | -7.6 | -12.3 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 31-21 | 59.6 | 7.8 | 14.3 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 46-41 | 52.9 | 8.1 | 22.1 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 13-13 | 50.0 | 0.0 | -6.0 |  |
| pin_value+sharp_gap | close | pin $1-2k | 51-67 | 43.2 | -4.2 | -14.2 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 44-36 | 55.0 | 4.1 | 5.0 |  |
| follow_move+money_level | close | pin $1-2k | 95-109 | 46.6 | -2.3 | -11.3 |  |
| money_level+rlm_ratio | close | pin $1-2k | 29-19 | 60.4 | 10.3 | 15.0 |  |
| money_level+sharp_gap | close | pin $1-2k | 158-151 | 51.1 | -0.3 | -4.8 |  |
| money_level+money_moving | close | pin $1-2k | 155-154 | 50.2 | -1.2 | -6.3 |  |
| consensus_gap+money_level | close | pin $1-2k | 48-49 | 49.5 | -5.6 | -11.9 |  |
| money_level+pin_value | close | pin $1-2k | 55-61 | 47.4 | -1.7 | -11.2 |  |
| money_level+pin_rlm | close | pin $1-2k | 24-15 | 61.5 | 14.0 | 21.7 |  |
| follow_move+money_level | close | pin $2k+ | 43-48 | 47.3 | -2.0 | -9.9 |  |
| follow_move+money_moving | close | pin $2k+ | 49-50 | 49.5 | -0.1 | -5.8 |  |
| follow_move+sharp_gap | close | pin $2k+ | 50-50 | 50.0 | 0.4 | -4.8 |  |
| money_level+money_moving | close | pin $2k+ | 104-97 | 51.7 | -0.7 | -5.1 |  |
| money_level+sharp_gap | close | pin $2k+ | 104-99 | 51.2 | -1.3 | -5.8 |  |
| money_moving+sharp_gap | close | pin $2k+ | 154-187 | 45.2 | -0.5 | -6.5 |  |
| consensus_gap+money_moving | close | pin $2k+ | 23-50 | 31.5 | -10.4 | -16.2 |  |
| consensus_gap+pin_value | close | pin $2k+ | 30-39 | 43.5 | 2.2 | 3.7 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 24-53 | 31.2 | -11.7 | -18.7 |  |
| money_moving+pin_value | close | pin $2k+ | 39-47 | 45.3 | 1.6 | 4.9 |  |
| pin_value+sharp_gap | close | pin $2k+ | 39-47 | 45.3 | 1.6 | 4.9 |  |
| consensus_gap+follow_move | close | pin $2k+ | 8-6 | 57.1 | 8.8 | 5.7 |  |
| follow_move+pin_value | close | pin $2k+ | 25-18 | 58.1 | 8.9 | 9.4 |  |
| follow_move+pin_rlm | close | pin $2k+ | 7-13 | 35.0 | -16.6 | -33.3 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 13-16 | 44.8 | -5.9 | -14.9 |  |
| money_level+pin_rlm | close | pin $2k+ | 9-8 | 52.9 | 10.8 | 17.5 |  |
| money_level+pin_value | close | pin $2k+ | 38-38 | 50.0 | 0.7 | -7.8 |  |
| money_level+rlm_ratio | close | pin $2k+ | 6-8 | 42.9 | -7.5 | -18.7 |  |
| money_moving+pin_rlm | close | pin $2k+ | 24-50 | 32.4 | -1.9 | -12.2 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 13-16 | 44.8 | -5.9 | -14.9 |  |
| pin_rlm+pin_value | close | pin $2k+ | 5-8 | 38.5 | 4.1 | 51.3 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 7-13 | 35.0 | -16.6 | -33.3 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 24-50 | 32.4 | -1.9 | -12.2 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 2-2 | 50.0 | -1.2 | -7.3 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 13-16 | 44.8 | -5.9 | -14.9 |  |
| consensus_gap+money_level | close | pin $2k+ | 46-36 | 56.1 | -5.7 | -12.8 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-15 | 21.1 | -8.0 | -9.0 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -52.5 | -100.0 |  |
| money_level+money_moving | close | pin limit <$1k | 54-60 | 47.4 | -2.7 | -8.9 |  |
| money_level+sharp_gap | close | pin limit <$1k | 56-59 | 48.7 | -1.6 | -6.4 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 87-88 | 49.7 | -1.2 | 0.6 |  |
| consensus_gap+money_level | close | pin limit <$1k | 21-22 | 48.8 | 0.8 | -9.8 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 27-30 | 47.4 | 0.1 | -3.2 |  |
| follow_move+money_moving | close | pin limit <$1k | 56-56 | 50.0 | -1.2 | -4.1 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 58-54 | 51.8 | 0.5 | -0.7 |  |
| money_level+pin_value | close | pin limit <$1k | 34-30 | 53.1 | 5.5 | 0.4 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 13-10 | 56.5 | 9.1 | 5.9 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 17-15 | 53.1 | 6.1 | 13.9 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 18-16 | 52.9 | 5.4 | 12.7 |  |
| follow_move+money_level | close | pin limit <$1k | 46-44 | 51.1 | 1.6 | -2.3 |  |
| follow_move+pin_value | close | pin limit <$1k | 28-19 | 59.6 | 11.0 | 12.8 |  |
| money_moving+pin_value | close | pin limit <$1k | 27-24 | 52.9 | 4.4 | 9.2 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 29-25 | 53.7 | 4.8 | 10.1 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 3-2 | 60.0 | 18.1 | 101.6 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 34-16 | 68.0 | 16.4 | 48.3 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 13-2 | 86.7 | 37.2 | 95.2 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 35-16 | 68.6 | 16.9 | 49.1 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 28-12 | 70.0 | 17.4 | 34.7 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 37-20 | 64.9 | 12.1 | 24.8 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 35-20 | 63.6 | 10.9 | 22.5 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 28-12 | 70.0 | 17.4 | 34.7 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 37-20 | 64.9 | 12.1 | 24.8 |  |
| money_level+pin_rlm | close | pin limit <$1k | 17-8 | 68.0 | 14.9 | 30.7 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 18-11 | 62.1 | 9.1 | 19.7 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 12-4 | 75.0 | 23.5 | 43.9 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 3-3 | 50.0 | 2.7 | -5.2 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 45.9 | 87.7 |  |
| pin_rlm | early | <1k bets | 1-1 | 50.0 | 23.8 | -3.7 | -2.15 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.2 | -100.0 | -4.8 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.8 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 15-16 | 48.4 | -0.9 | -7.7 | -0.1 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -49.2 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 152-170 | 47.2 | -2.2 | -9.5 | 0.17 |
| follow_move | early | pin $1-2k | 10-9 | 52.6 | 2.5 | -0.6 | 0.0 |
| follow_move | early | pin limit <$1k | 34-29 | 54.0 | 4.9 | 2.6 | -0.33 |
| rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 14.7 | 29.2 | -0.5 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.5 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 4-3 | 57.1 | 4.0 | 9.7 | 0.57 |
| rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -2.5 | -1.0 | -0.5 |
| rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 27.5 | 53.6 | -0.4 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | -0.0 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 41.5 | 59.7 | 0.33 |
| money_level | early | <1k bets | 91-56 | 61.9 | 2.9 | -4.1 | 0.21 |
| money_level | early | pin $1-2k | 15-8 | 65.2 | 1.0 | -2.7 | -0.03 |
| money_level | early | pin limit <$1k | 22-24 | 47.8 | -6.1 | -12.1 | 0.31 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 6.9 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 6.5 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 79-57 | 58.1 | 8.2 | 11.3 | 0.44 |
| sharp_gap | early | pin $1-2k | 12-9 | 57.1 | 4.5 | 13.4 | -0.59 |
| sharp_gap | early | pin limit <$1k | 27-16 | 62.8 | 13.9 | 30.8 | 0.2 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.0 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.2 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 47-39 | 54.7 | 2.9 | -2.9 | 0.12 |
| money_moving | early | pin $1-2k | 6-6 | 50.0 | -11.5 | -26.9 | 0.35 |
| money_moving | early | pin limit <$1k | 20-9 | 69.0 | 19.7 | 47.8 | 0.36 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.3 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.5 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 30-33 | 47.6 | 0.0 | -9.7 | 0.19 |
| pin_value | early | pin $1-2k | 11-14 | 44.0 | -0.4 | -16.7 | 0.17 |
| pin_value | early | pin limit <$1k | 32-28 | 53.3 | 4.0 | 0.8 | 0.13 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -45.9 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -27.9 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -10.9 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 13.2 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 127-175 | 42.1 | -4.9 | -17.4 | 0.3 |
| consensus_gap | early | pin $1-2k | 10-17 | 37.0 | -8.2 | -27.6 | 0.49 |
| consensus_gap | early | pin limit <$1k | 17-33 | 34.0 | -16.0 | -29.1 | 0.31 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 15.9 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 2.4 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 2.8 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.0 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 18.7 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 15.3 | 26.0 | -0.25 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 4.3 | -6.9 | 0.3 |
| consensus_gap+follow_move | early | 1-3k bets | 4-4 | 50.0 | 2.7 | -6.9 | 0.25 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.9 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.5 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 10-10 | 50.0 | -0.1 | -4.1 | 0.05 |
| follow_move+pin_value | early | 1-3k bets | 7-5 | 58.3 | 8.9 | 9.2 | -0.42 |
| follow_move+sharp_gap | early | 1-3k bets | 9-8 | 52.9 | 2.5 | 1.2 | -0.18 |
| follow_move+rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 14.7 | 29.2 | -0.5 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 26.9 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 4-2 | 66.7 | 14.7 | 29.2 | -0.5 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.9 | 56.1 | 0.15 |
| follow_move+money_moving | early | 1-3k bets | 9-4 | 69.2 | 19.7 | 32.1 | 0.08 |
| money_moving+rlm_ratio | early | 1-3k bets | 2-1 | 66.7 | 15.8 | 28.7 | -1.0 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.5 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.5 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.5 | 83.3 | 1.0 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.5 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.5 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.2 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.5 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.5 | 83.3 | 1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.5 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 36.0 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 45.9 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 12-12 | 50.0 | 1.0 | -5.8 | 1.38 |
| consensus_gap+money_level | early | <1k bets | 18-15 | 54.5 | -10.6 | -19.3 | 0.26 |
| consensus_gap+sharp_gap | early | <1k bets | 15-26 | 36.6 | -12.1 | -13.7 | 0.75 |
| follow_move+money_level | early | <1k bets | 17-14 | 54.8 | 7.1 | 4.4 | 0.74 |
| follow_move+sharp_gap | early | <1k bets | 18-9 | 66.7 | 17.3 | 27.2 | 1.0 |
| money_level+sharp_gap | early | <1k bets | 55-28 | 66.3 | 9.6 | 7.4 | 0.55 |
| money_level+money_moving | early | <1k bets | 31-22 | 58.5 | 1.2 | -6.2 | -0.03 |
| money_moving+sharp_gap | early | <1k bets | 31-21 | 59.6 | 8.4 | 7.0 | 0.38 |
| consensus_gap+money_moving | early | <1k bets | 8-15 | 34.8 | -12.6 | -44.1 | 0.14 |
| follow_move+pin_value | early | <1k bets | 11-10 | 52.4 | 3.6 | -1.5 | 0.29 |
| follow_move+money_moving | early | <1k bets | 9-8 | 52.9 | 4.3 | 1.5 | 0.59 |
| consensus_gap+pin_value | early | <1k bets | 11-22 | 33.3 | -12.3 | -37.3 | 0.45 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -26.2 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -26.2 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | <1k bets | 1-1 | 50.0 | 23.8 | -3.7 | -2.15 |
| pin_value+sharp_gap | early | <1k bets | 4-3 | 57.1 | 11.5 | 9.1 | 0.03 |
| money_level+pin_value | early | <1k bets | 3-3 | 50.0 | 1.4 | -4.5 | 1.33 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -53.3 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -54.1 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 0-2 | 0.0 | -49.2 | -100.0 | 2.5 |
| follow_move+rlm_ratio | early | <1k bets | 4-3 | 57.1 | 4.0 | 9.7 | 0.57 |
| money_level+rlm_ratio | early | <1k bets | 2-2 | 50.0 | -4.1 | -3.5 | 1.25 |
| money_moving+rlm_ratio | early | <1k bets | 2-2 | 50.0 | -2.5 | -3.5 | 0.5 |
| rlm_ratio+sharp_gap | early | <1k bets | 4-3 | 57.1 | 4.0 | 9.7 | 0.57 |
| consensus_gap+rlm_ratio | early | <1k bets | 1-1 | 50.0 | -4.1 | -4.5 | 0.5 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 45.9 | 90.9 | 1.0 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 73.8 | 92.6 | 0.5 |
| consensus_gap+money_level | early | pin $1-2k | 4-4 | 50.0 | -14.0 | -22.9 | 0.44 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -31.7 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 4-9 | 30.8 | -8.9 | -42.5 | 0.4 |
| follow_move+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -2.5 | -1.0 | -0.5 |
| follow_move+sharp_gap | early | pin $1-2k | 3-1 | 75.0 | 25.0 | 45.0 | -0.25 |
| money_level+money_moving | early | pin $1-2k | 6-5 | 54.5 | -10.2 | -20.3 | 0.02 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.5 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 1-1 | 50.0 | -2.5 | -1.0 | -0.5 |
| money_level+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 6.4 | 8.3 | -0.45 |
| money_moving+sharp_gap | early | pin $1-2k | 3-5 | 37.5 | -21.1 | -45.3 | -0.06 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.7 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 2-2 | 50.0 | 0.0 | -8.4 | 0.75 |
| follow_move+money_level | early | pin $1-2k | 3-2 | 60.0 | 11.5 | 16.0 | 0.2 |
| follow_move+pin_value | early | pin $1-2k | 4-3 | 57.1 | 7.5 | 6.9 | 0.29 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 47.5 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 1-0 | 100.0 | 52.5 | 90.9 | 0.0 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.2 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -25.0 | -62.8 | -0.72 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -26.2 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -26.2 | -100.0 | -4.8 |
| money_level+money_moving | early | pin limit <$1k | 11-7 | 61.1 | 7.9 | 12.1 | 0.53 |
| money_level+sharp_gap | early | pin limit <$1k | 18-14 | 56.2 | 4.8 | 2.3 | 0.25 |
| money_moving+sharp_gap | early | pin limit <$1k | 16-5 | 76.2 | 27.9 | 68.0 | 0.39 |
| money_level+pin_value | early | pin limit <$1k | 8-5 | 61.5 | 10.0 | 16.6 | 0.46 |
| money_moving+pin_value | early | pin limit <$1k | 6-4 | 60.0 | 9.8 | 13.0 | 0.3 |
| pin_value+sharp_gap | early | pin limit <$1k | 11-5 | 68.8 | 18.1 | 30.3 | 0.06 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-7 | 46.2 | -1.2 | -14.2 | 0.46 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -27.1 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 13-18 | 41.9 | -6.2 | -21.4 | 0.44 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.3 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 8-7 | 53.3 | 3.2 | 1.9 | 0.07 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 5.0 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 9-7 | 56.2 | 5.9 | 6.9 | -0.31 |
| follow_move+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 27.5 | 53.6 | -0.4 |
| money_level+rlm_ratio | early | pin limit <$1k | 4-0 | 100.0 | 45.9 | 92.0 | 0.25 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.3 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 4-1 | 80.0 | 27.5 | 53.6 | -0.4 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 23.3 | 72.3 | 0.54 |
| follow_move+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 20.3 | 33.3 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.3 | 28.7 | -1.0 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -54.1 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -54.1 | -100.0 | 1.0 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.8 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 73.8 | 92.6 | 0.5 |
