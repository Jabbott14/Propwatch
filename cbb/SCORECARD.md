# CBB scorecard

Generated 2026-11-17 16:30 UTC. 528 graded games (15 finished games had no final score matched and are not graded).

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before tip. Break-even at -110 is 52.4%. CLV = points of closing-line
value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured
on this sample. `edge` is hit% minus that. A signal that is structurally long
favourites or overs beats 50% whenever those run, which is not an edge -- this
sample ran **47.4% favourites** (n=527) and **46.2% overs** (n=528) and **74.0% moneyline favourites** (n=447).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

## EARLY

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 1-1 | 50.0 | 26.0 | 24.0 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | both | 198-219 | 47.5 | 49.5 | -2.0 | -37.53 | -9.0 | 0.17 | 39.8 | DROP: below break-even |
| rlm_ratio | both | 8-6 | 57.1 | 52.4 | 4.7 | +1.43 | 10.2 | 0.0 | 28.6 | keep collecting (14/30) |
| money_level | both | 122-76 | 61.6 | 58.7 | 2.9 | -7.28 | -3.7 | 0.18 | 41.4 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 106-81 | 56.7 | 49.2 | 7.5 | +22.67 | 12.1 | 0.31 | 42.2 | no edge shown yet |
| money_moving | both | 72-51 | 58.5 | 51.1 | 7.4 | +9.1 | 7.4 | 0.14 | 42.3 | no edge shown yet |
| pin_value | both | 43-42 | 50.6 | 47.9 | 2.7 | -3.68 | -4.3 | 0.14 | 41.2 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.5 | -31.5 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 166-227 | 42.2 | 46.4 | -4.2 | -54.37 | -13.8 | 0.29 | 44.8 | DROP: below break-even |
| consensus_gap+money_level | both | 23-22 | 51.1 | 63.2 | -12.1 | -10.62 | -23.6 | 0.25 | 46.7 | no edge shown yet |
| consensus_gap+money_moving | both | 15-20 | 42.9 | 45.3 | -2.4 | -4.7 | -13.4 | 0.17 | 37.1 | no edge shown yet |
| consensus_gap+pin_value | both | 17-27 | 38.6 | 45.6 | -7.0 | -12.16 | -27.6 | 0.43 | 52.3 | DROP: below break-even |
| follow_move+rlm_ratio | both | 8-6 | 57.1 | 52.4 | 4.7 | +1.43 | 10.2 | 0.0 | 28.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 27-18 | 60.0 | 49.8 | 10.2 | +6.54 | 14.5 | 0.51 | 40.0 | no edge shown yet |
| money_level+money_moving | both | 47-27 | 63.5 | 57.2 | 6.3 | +2.81 | 3.8 | 0.06 | 48.6 | PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | both | 10-8 | 55.6 | 50.6 | 4.9 | +0.9 | 5.0 | 0.5 | 50.0 | keep collecting (18/30) |
| money_moving+pin_value | both | 7-5 | 58.3 | 50.1 | 8.2 | +1.13 | 9.4 | 0.42 | 41.7 | keep collecting (12/30) |
| rlm_ratio+sharp_gap | both | 8-6 | 57.1 | 52.4 | 4.7 | +1.43 | 10.2 | 0.0 | 28.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 73-41 | 64.0 | 55.7 | 8.3 | +7.81 | 6.9 | 0.42 | 45.6 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 45-29 | 60.8 | 49.5 | 11.3 | +12.05 | 16.3 | 0.34 | 44.6 | no edge shown yet |
| pin_value+sharp_gap | both | 12-7 | 63.2 | 49.2 | 14.0 | +3.75 | 19.8 | -0.15 | 36.8 | keep collecting (19/30) |
| consensus_gap+follow_move | both | 16-16 | 50.0 | 48.6 | 1.4 | -1.95 | -6.1 | 1.09 | 53.1 | no edge shown yet |
| consensus_gap+sharp_gap | both | 19-35 | 35.2 | 45.8 | -10.6 | -6.74 | -12.5 | 0.6 | 44.4 | DROP: below break-even |
| follow_move+money_level | both | 27-24 | 52.9 | 48.7 | 4.2 | +0.56 | 1.1 | 0.47 | 41.2 | no edge shown yet |
| follow_move+pin_value | both | 18-15 | 54.5 | 49.0 | 5.5 | +0.8 | 2.4 | 0.03 | 30.3 | no edge shown yet |
| money_level+rlm_ratio | both | 6-3 | 66.7 | 53.4 | 13.3 | +2.61 | 29.0 | 0.56 | 33.3 | keep collecting (9/30) |
| pin_value+rlm_ratio | both | 2-1 | 66.7 | 51.3 | 15.4 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| follow_move+money_moving | both | 18-12 | 60.0 | 49.1 | 10.9 | +4.43 | 14.8 | 0.37 | 43.3 | no edge shown yet |
| money_moving+rlm_ratio | both | 4-3 | 57.1 | 51.6 | 5.5 | +0.72 | 10.3 | -0.14 | 28.6 | keep collecting (7/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 26.0 | -26.0 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 26.0 | -26.0 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | both | 1-1 | 50.0 | 26.0 | 24.0 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 53.2 | -53.2 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 1-1 | 50.0 | 53.8 | -3.8 | -0.09 | -4.5 | 0.5 | 50.0 | keep collecting (2/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 26.0 | 74.0 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-1 | 50.0 | 26.0 | 24.0 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | spread | 97-115 | 45.8 | 49.4 | -3.7 | -25.79 | -12.2 | -0.0 | 34.0 | DROP: below break-even |
| follow_move | total | 101-104 | 49.3 | 49.5 | -0.3 | -11.74 | -5.7 | 0.34 | 45.9 | no edge shown yet |
| rlm_ratio | spread | 3-2 | 60.0 | 51.5 | 8.5 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 5-4 | 55.6 | 52.9 | 2.6 | +0.59 | 6.5 | 0.33 | 44.4 | keep collecting (9/30) |
| money_level | moneyline | 67-27 | 71.3 | 69.4 | 1.8 | -8.17 | -8.7 | 0.1 | 45.7 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 16-16 | 50.0 | 49.2 | 0.8 | -1.6 | -5.0 | 0.81 | 46.9 | no edge shown yet |
| money_level | total | 39-33 | 54.2 | 48.8 | 5.3 | +2.48 | 3.4 | -0.01 | 33.3 | no edge shown yet |
| sharp_gap | moneyline | 44-39 | 53.0 | 47.4 | 5.6 | +8.4 | 10.1 | 0.29 | 48.2 | no edge shown yet |
| sharp_gap | spread | 19-14 | 57.6 | 49.8 | 7.8 | +3.09 | 9.4 | 0.61 | 36.4 | no edge shown yet |
| sharp_gap | total | 43-28 | 60.6 | 51.0 | 9.5 | +11.17 | 15.7 | 0.21 | 38.0 | no edge shown yet |
| money_moving | moneyline | 28-27 | 50.9 | 53.1 | -2.2 | -6.68 | -12.1 | 0.1 | 52.7 | no edge shown yet |
| money_moving | spread | 17-4 | 81.0 | 49.1 | 31.8 | +11.27 | 53.7 | 0.14 | 38.1 | keep collecting (21/30) |
| money_moving | total | 27-20 | 57.4 | 49.8 | 7.7 | +4.51 | 9.6 | 0.17 | 31.9 | no edge shown yet |
| pin_value | moneyline | 1-5 | 16.7 | 26.0 | -9.3 | -4.02 | -67.0 | -0.02 | 66.7 | keep collecting (6/30) |
| pin_value | spread | 22-17 | 56.4 | 49.3 | 7.1 | +2.35 | 6.0 | 0.28 | 41.0 | no edge shown yet |
| pin_value | total | 20-20 | 50.0 | 49.8 | 0.2 | -2.01 | -5.0 | 0.03 | 37.5 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.6 | -19.2 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 66-124 | 34.7 | 43.4 | -8.7 | -39.86 | -21.0 | -0.04 | 41.6 | DROP: below break-even |
| consensus_gap | spread | 54-50 | 51.9 | 49.1 | 2.8 | -2.85 | -2.7 | 0.44 | 43.3 | no edge shown yet |
| consensus_gap | total | 46-53 | 46.5 | 49.3 | -2.9 | -11.65 | -11.8 | 0.76 | 52.5 | no edge shown yet |
| money_level+sharp_gap | moneyline | 34-12 | 73.9 | 64.6 | 9.3 | +1.42 | 3.1 | 0.37 | 56.5 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+pin_value | moneyline | 1-5 | 16.7 | 26.0 | -9.3 | -4.02 | -67.0 | -0.02 | 66.7 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_level+money_moving | moneyline | 19-9 | 67.9 | 70.6 | -2.8 | -4.74 | -16.9 | -0.29 | 57.1 | keep collecting (28/30) |
| consensus_gap+sharp_gap | moneyline | 11-26 | 29.7 | 44.2 | -14.4 | -4.71 | -12.7 | 0.5 | 45.9 | DROP: below break-even |
| consensus_gap+money_level | moneyline | 16-14 | 53.3 | 70.8 | -17.5 | -8.68 | -28.9 | -0.09 | 46.7 | INVERT candidate: wrong well beyond its base rate |
| money_moving+sharp_gap | moneyline | 16-14 | 53.3 | 48.4 | 4.9 | +0.78 | 2.6 | 0.4 | 60.0 | no edge shown yet |
| consensus_gap+money_moving | moneyline | 7-19 | 26.9 | 44.5 | -17.5 | -10.63 | -40.9 | 0.26 | 46.2 | keep collecting (26/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 26.0 | -26.0 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 26.0 | -26.0 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | moneyline | 1-1 | 50.0 | 26.0 | 24.0 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 26.0 | -26.0 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 26.0 | 74.0 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 4-5 | 44.4 | 47.4 | -3.0 | -1.59 | -17.7 | 1.67 | 66.7 | keep collecting (9/30) |
| consensus_gap+money_moving | spread | 4-0 | 100.0 | 47.4 | 52.6 | +3.41 | 85.2 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_value | spread | 9-8 | 52.9 | 48.3 | 4.6 | -0.31 | -1.8 | 0.53 | 52.9 | keep collecting (17/30) |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.5 | 8.5 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 48.7 | 13.8 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 9-4 | 69.2 | 48.6 | 20.6 | +4.21 | 32.4 | 0.77 | 61.5 | keep collecting (13/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.9 | -6.0 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.5 | 10.5 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 51.5 | 8.5 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 13-11 | 54.2 | 49.1 | 5.0 | +0.71 | 3.0 | 0.96 | 41.7 | keep collecting (24/30) |
| money_moving+sharp_gap | spread | 9-3 | 75.0 | 49.1 | 25.9 | +5.13 | 42.7 | 0.42 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.1 | 17.5 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 8-8 | 50.0 | 48.1 | 1.9 | -1.18 | -7.4 | 0.94 | 43.8 | keep collecting (16/30) |
| consensus_gap+sharp_gap | spread | 4-3 | 57.1 | 47.4 | 9.7 | +0.41 | 5.8 | 2.14 | 71.4 | keep collecting (7/30) |
| follow_move+money_level | spread | 11-8 | 57.9 | 48.5 | 9.4 | +2.04 | 10.7 | 0.63 | 42.1 | keep collecting (19/30) |
| follow_move+pin_value | spread | 11-7 | 61.1 | 48.9 | 12.2 | +2.56 | 14.2 | 0.33 | 33.3 | keep collecting (18/30) |
| follow_move+money_moving | spread | 9-1 | 90.0 | 48.0 | 42.0 | +7.22 | 72.2 | 0.2 | 40.0 | keep collecting (10/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 52.6 | 14.1 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.6 | -52.6 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 19-14 | 57.6 | 49.2 | 8.4 | +3.34 | 10.1 | 0.09 | 36.4 | no edge shown yet |
| money_level+sharp_gap | total | 26-18 | 59.1 | 50.0 | 9.1 | +5.68 | 12.9 | 0.18 | 36.4 | no edge shown yet |
| money_moving+sharp_gap | total | 20-12 | 62.5 | 50.7 | 11.8 | +6.14 | 19.2 | 0.25 | 31.2 | no edge shown yet |
| money_level+pin_value | total | 7-4 | 63.6 | 51.7 | 11.9 | +2.32 | 21.1 | 0.36 | 36.4 | keep collecting (11/30) |
| money_moving+pin_value | total | 4-3 | 57.1 | 50.5 | 6.6 | +0.56 | 8.0 | 0.29 | 28.6 | keep collecting (7/30) |
| pin_value+sharp_gap | total | 10-5 | 66.7 | 50.8 | 15.9 | +4.01 | 26.7 | 0.0 | 33.3 | keep collecting (15/30) |
| follow_move+money_level | total | 16-16 | 50.0 | 48.8 | 1.2 | -1.47 | -4.6 | 0.38 | 40.6 | no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.2 | -2.6 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 5-4 | 55.6 | 52.9 | 2.6 | +0.59 | 6.5 | 0.33 | 44.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 17-12 | 58.6 | 50.4 | 8.2 | +3.46 | 11.9 | 0.45 | 41.4 | keep collecting (29/30) |
| money_level+rlm_ratio | total | 4-2 | 66.7 | 53.8 | 12.9 | +1.68 | 28.0 | 0.83 | 50.0 | keep collecting (6/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 51.3 | 15.4 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 5-4 | 55.6 | 52.9 | 2.6 | +0.59 | 6.5 | 0.33 | 44.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 9-11 | 45.0 | 49.6 | -4.6 | -2.8 | -14.0 | 0.45 | 45.0 | keep collecting (20/30) |
| consensus_gap+money_level | total | 3-3 | 50.0 | 48.7 | 1.3 | -0.34 | -5.7 | -0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 47.7 | 32.3 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 49.1 | -15.8 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 4-6 | 40.0 | 50.8 | -10.8 | -2.44 | -24.4 | -0.1 | 20.0 | keep collecting (10/30) |
| money_moving+rlm_ratio | total | 2-3 | 40.0 | 52.3 | -12.3 | -1.14 | -22.8 | 0.2 | 40.0 | keep collecting (5/30) |
| consensus_gap+follow_move | total | 8-8 | 50.0 | 49.1 | 0.9 | -0.76 | -4.8 | 1.25 | 62.5 | keep collecting (16/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 1-1 | 50.0 | 53.8 | -3.8 | -0.09 | -4.5 | 0.5 | 50.0 | keep collecting (2/30) |

## CLOSE

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 107-108 | 49.8 | 42.6 | 7.1 | +36.03 | 16.8 |  |  | no edge shown yet |
| follow_move | both | 427-438 | 49.4 | 49.7 | -0.3 | -49.9 | -5.8 |  |  | DROP: below break-even |
| rlm_ratio | both | 129-98 | 56.8 | 51.4 | 5.4 | +19.88 | 8.8 |  |  | no edge shown yet |
| money_level | both | 825-622 | 57.0 | 55.4 | 1.6 | -64.97 | -4.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 646-753 | 46.2 | 47.3 | -1.1 | -86.01 | -6.1 |  |  | DROP: below break-even |
| money_moving | both | 643-757 | 45.9 | 47.5 | -1.5 | -98.09 | -7.0 |  |  | DROP: below break-even |
| pin_value | both | 272-285 | 48.8 | 47.3 | 1.6 | -13.78 | -2.5 |  |  | DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 50.9 | 15.8 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 264-392 | 40.2 | 45.9 | -5.7 | -87.88 | -13.4 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 62-57 | 52.1 | 47.9 | 4.2 | -3.24 | -2.7 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 114-211 | 35.1 | 42.8 | -7.7 | -32.1 | -9.9 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 19-33 | 36.5 | 36.4 | 0.2 | +12.47 | 24.0 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 107-133 | 44.6 | 44.2 | 0.3 | -10.98 | -4.6 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | both | 16-12 | 57.1 | 48.6 | 8.5 | +2.02 | 7.2 |  |  | keep collecting (28/30) |
| consensus_gap+sharp_gap | both | 115-215 | 34.8 | 42.4 | -7.5 | -32.94 | -10.0 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 281-298 | 48.5 | 49.9 | -1.3 | -43.24 | -7.5 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 67-46 | 59.3 | 51.9 | 7.4 | +15.55 | 13.8 |  |  | no edge shown yet |
| follow_move+pin_value | both | 97-86 | 53.0 | 49.1 | 3.9 | -0.09 | -0.0 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 129-98 | 56.8 | 51.4 | 5.4 | +19.88 | 8.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 286-294 | 49.3 | 49.9 | -0.6 | -34.49 | -5.9 |  |  | no edge shown yet |
| money_moving+pin_rlm | both | 104-107 | 49.3 | 42.6 | 6.7 | +34.3 | 16.3 |  |  | no edge shown yet |
| money_moving+pin_value | both | 118-142 | 45.4 | 46.3 | -0.9 | -10.94 | -4.2 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 125-97 | 56.3 | 51.3 | 5.0 | +17.14 | 7.7 |  |  | no edge shown yet |
| money_moving+sharp_gap | both | 621-729 | 46.0 | 47.3 | -1.3 | -84.91 | -6.3 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 30-26 | 53.6 | 45.3 | 8.3 | +18.52 | 33.1 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 67-46 | 59.3 | 51.9 | 7.4 | +15.55 | 13.8 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 107-108 | 49.8 | 42.6 | 7.1 | +36.03 | 16.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 27-19 | 58.7 | 50.6 | 8.1 | +5.18 | 11.3 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 120-141 | 46.0 | 46.4 | -0.4 | -8.19 | -3.1 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 129-98 | 56.8 | 51.4 | 5.4 | +19.88 | 8.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+money_moving | both | 454-417 | 52.1 | 52.0 | 0.1 | -39.86 | -4.6 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 453-412 | 52.4 | 51.9 | 0.5 | -31.7 | -3.7 |  |  | no edge shown yet |
| follow_move+money_level | both | 254-267 | 48.8 | 49.1 | -0.3 | -37.16 | -7.1 |  |  | DROP: below break-even |
| money_level+rlm_ratio | both | 72-55 | 56.7 | 51.0 | 5.7 | +10.58 | 8.3 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 160-141 | 53.2 | 56.4 | -3.3 | -25.12 | -8.3 |  |  | no edge shown yet |
| money_level+pin_value | both | 128-130 | 49.6 | 48.8 | 0.8 | -18.78 | -7.3 |  |  | no edge shown yet |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | both | 52-31 | 62.7 | 48.0 | 14.6 | +20.89 | 25.2 |  |  | PROMOTE: beats break-even and its own base rate |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 53.8 | 46.2 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 28-55 | 33.7 | 27.7 | 6.0 | +16.78 | 20.2 |  |  | DROP: below break-even |
| pin_rlm | spread | 18-16 | 52.9 | 50.9 | 2.0 | +0.29 | 0.9 |  |  | no edge shown yet |
| pin_rlm | total | 61-37 | 62.2 | 52.4 | 9.8 | +18.96 | 19.3 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move | spread | 195-202 | 49.1 | 49.3 | -0.2 | -25.59 | -6.4 |  |  | no edge shown yet |
| follow_move | total | 232-236 | 49.6 | 50.0 | -0.4 | -24.31 | -5.2 |  |  | no edge shown yet |
| rlm_ratio | spread | 33-35 | 48.5 | 50.0 | -1.5 | -4.97 | -7.3 |  |  | no edge shown yet |
| rlm_ratio | total | 96-63 | 60.4 | 52.0 | 8.4 | +24.85 | 15.6 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level | moneyline | 324-115 | 73.8 | 69.7 | 4.1 | -11.54 | -2.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 239-253 | 48.6 | 49.1 | -0.6 | -37.57 | -7.6 |  |  | DROP: below break-even |
| money_level | total | 262-254 | 50.8 | 49.3 | 1.5 | -15.87 | -3.1 |  |  | no edge shown yet |
| sharp_gap | moneyline | 144-261 | 35.6 | 40.1 | -4.5 | -49.92 | -12.3 |  |  | DROP: below break-even |
| sharp_gap | spread | 249-237 | 51.2 | 49.5 | 1.7 | -12.16 | -2.5 |  |  | no edge shown yet |
| sharp_gap | total | 253-255 | 49.8 | 50.8 | -1.0 | -23.93 | -4.7 |  |  | no edge shown yet |
| money_moving | moneyline | 149-254 | 37.0 | 40.9 | -3.9 | -43.57 | -10.8 |  |  | DROP: below break-even |
| money_moving | spread | 246-240 | 50.6 | 49.5 | 1.2 | -18.03 | -3.7 |  |  | no edge shown yet |
| money_moving | total | 248-263 | 48.5 | 50.7 | -2.2 | -36.5 | -7.1 |  |  | DROP: below break-even |
| pin_value | moneyline | 13-45 | 22.4 | 28.4 | -6.0 | -3.9 | -6.7 |  |  | DROP: below break-even |
| pin_value | spread | 127-115 | 52.5 | 49.6 | 2.8 | -3.65 | -1.5 |  |  | no edge shown yet |
| pin_value | total | 132-125 | 51.4 | 49.2 | 2.1 | -6.23 | -2.4 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.6 | 47.4 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 106-233 | 31.3 | 43.5 | -12.3 | -66.67 | -19.7 |  |  | DROP: below break-even |
| consensus_gap | spread | 74-67 | 52.5 | 49.1 | 3.4 | -3.8 | -2.7 |  |  | no edge shown yet |
| consensus_gap | total | 84-92 | 47.7 | 48.0 | -0.2 | -17.42 | -9.9 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 101-61 | 62.3 | 62.8 | -0.4 | -3.58 | -2.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 96-60 | 61.5 | 62.3 | -0.8 | -3.1 | -2.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 134-244 | 35.4 | 39.8 | -4.4 | -42.07 | -11.1 |  |  | DROP: below break-even |
| consensus_gap+money_level | moneyline | 71-51 | 58.2 | 68.9 | -10.7 | -12.52 | -10.3 |  |  | no edge shown yet |
| consensus_gap+money_moving | moneyline | 36-132 | 21.4 | 37.4 | -16.0 | -20.8 | -12.4 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+sharp_gap | moneyline | 37-137 | 21.3 | 36.7 | -15.5 | -22.65 | -13.0 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_rlm | moneyline | 10-23 | 30.3 | 28.9 | 1.4 | +14.65 | 44.4 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 28-54 | 34.1 | 27.7 | 6.4 | +17.78 | 21.7 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 28-55 | 33.7 | 27.7 | 6.0 | +16.78 | 20.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 12-39 | 23.5 | 28.8 | -5.3 | +0.58 | 1.1 |  |  | DROP: below break-even |
| money_moving+pin_value | moneyline | 7-29 | 19.4 | 26.0 | -6.5 | +4.27 | 11.9 |  |  | DROP: below break-even |
| pin_rlm+pin_value | moneyline | 5-8 | 38.5 | 26.0 | 12.5 | +14.07 | 108.2 |  |  | keep collecting (13/30) |
| pin_value+sharp_gap | moneyline | 7-29 | 19.4 | 26.0 | -6.5 | +4.27 | 11.9 |  |  | DROP: below break-even |
| money_level+pin_rlm | moneyline | 9-7 | 56.2 | 32.0 | 24.3 | +5.65 | 35.3 |  |  | keep collecting (16/30) |
| money_level+pin_value | moneyline | 3-1 | 75.0 | 62.0 | 13.0 | +0.31 | 7.8 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 31-25 | 55.4 | 48.4 | 7.0 | +1.4 | 2.5 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 41-36 | 53.2 | 48.9 | 4.3 | -1.02 | -1.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 50-41 | 54.9 | 49.0 | 5.9 | +1.53 | 1.7 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.33 | -38.9 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | spread | 40-36 | 52.6 | 49.1 | 3.5 | -1.91 | -2.5 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 124-127 | 49.4 | 49.0 | 0.4 | -15.38 | -6.1 |  |  | no edge shown yet |
| follow_move+pin_rlm | spread | 15-15 | 50.0 | 50.9 | -0.9 | -1.37 | -4.6 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 49-41 | 54.4 | 48.9 | 5.5 | +1.78 | 2.0 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 33-35 | 48.5 | 50.0 | -1.5 | -4.97 | -7.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 125-126 | 49.8 | 49.1 | 0.7 | -13.25 | -5.3 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 16-16 | 50.0 | 50.8 | -0.8 | -1.53 | -4.8 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 60-59 | 50.4 | 49.2 | 1.3 | -7.09 | -6.0 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 31-34 | 47.7 | 49.9 | -2.2 | -5.9 | -9.1 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 241-232 | 51.0 | 49.5 | 1.5 | -14.53 | -3.1 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 6-7 | 46.2 | 50.2 | -4.0 | -1.79 | -13.8 |  |  | keep collecting (13/30) |
| pin_rlm+rlm_ratio | spread | 15-15 | 50.0 | 50.9 | -0.9 | -1.37 | -4.6 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 18-16 | 52.9 | 50.9 | 2.0 | +0.29 | 0.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 5-6 | 45.5 | 49.3 | -3.8 | -1.72 | -15.6 |  |  | keep collecting (11/30) |
| pin_value+sharp_gap | spread | 60-59 | 50.4 | 49.3 | 1.1 | -7.16 | -6.0 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 33-35 | 48.5 | 50.0 | -1.5 | -4.97 | -7.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 120-129 | 48.2 | 48.7 | -0.5 | -21.02 | -8.4 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 17-20 | 45.9 | 49.5 | -3.6 | -4.71 | -12.7 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 187-184 | 50.4 | 49.2 | 1.3 | -15.51 | -4.2 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 50-41 | 54.9 | 48.7 | 6.3 | +1.84 | 2.0 |  |  | no edge shown yet |
| money_level+money_moving | spread | 186-185 | 50.1 | 49.1 | 1.0 | -17.42 | -4.7 |  |  | no edge shown yet |
| money_level+pin_value | spread | 65-68 | 48.9 | 49.0 | -0.1 | -11.78 | -8.9 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 9-6 | 60.0 | 50.2 | 9.8 | +2.01 | 13.4 |  |  | keep collecting (15/30) |
| money_level+money_moving | total | 167-171 | 49.4 | 50.1 | -0.7 | -18.85 | -5.6 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 170-168 | 50.3 | 50.1 | 0.2 | -13.09 | -3.9 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 246-253 | 49.3 | 50.8 | -1.5 | -28.31 | -5.7 |  |  | no edge shown yet |
| consensus_gap+money_level | total | 39-49 | 44.3 | 47.1 | -2.8 | -14.43 | -16.4 |  |  | DROP: below break-even |
| consensus_gap+pin_value | total | 45-53 | 45.9 | 47.8 | -1.9 | -13.09 | -13.4 |  |  | no edge shown yet |
| follow_move+money_moving | total | 157-171 | 47.9 | 50.6 | -2.7 | -27.86 | -8.5 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 161-168 | 48.9 | 50.6 | -1.7 | -21.24 | -6.5 |  |  | no edge shown yet |
| money_level+pin_value | total | 60-61 | 49.6 | 48.2 | 1.4 | -7.31 | -6.0 |  |  | no edge shown yet |
| follow_move+money_level | total | 134-138 | 49.3 | 49.4 | -0.2 | -16.14 | -5.9 |  |  | no edge shown yet |
| follow_move+pin_value | total | 48-45 | 51.6 | 49.2 | 2.4 | -1.87 | -2.0 |  |  | no edge shown yet |
| money_moving+pin_value | total | 51-54 | 48.6 | 50.0 | -1.4 | -8.12 | -7.7 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 53-53 | 50.0 | 50.1 | -0.1 | -5.3 | -5.0 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 37-43 | 46.2 | 48.1 | -1.9 | -10.28 | -12.9 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 38-42 | 47.5 | 48.2 | -0.7 | -8.37 | -10.5 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 31-32 | 49.2 | 47.4 | 1.8 | -4.64 | -7.4 |  |  | no edge shown yet |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pin_rlm | total | 6-7 | 46.2 | 49.1 | -3.0 | -1.7 | -13.0 |  |  | keep collecting (13/30) |
| consensus_gap+rlm_ratio | total | 14-8 | 63.6 | 48.3 | 15.4 | +4.35 | 19.8 |  |  | keep collecting (22/30) |
| follow_move+pin_rlm | total | 52-31 | 62.7 | 52.3 | 10.3 | +16.92 | 20.4 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+rlm_ratio | total | 96-63 | 60.4 | 52.0 | 8.4 | +24.85 | 15.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 34-18 | 65.4 | 52.3 | 13.1 | +13.23 | 25.4 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 55-35 | 61.1 | 51.6 | 9.5 | +15.28 | 17.0 |  |  | PROMOTE: beats break-even and its own base rate |
| money_moving+pin_rlm | total | 60-37 | 61.9 | 52.4 | 9.5 | +18.05 | 18.6 |  |  | PROMOTE: beats break-even and its own base rate |
| money_moving+rlm_ratio | total | 94-63 | 59.9 | 52.0 | 7.9 | +23.05 | 14.7 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_rlm+pin_value | total | 19-11 | 63.3 | 51.5 | 11.8 | +6.24 | 20.8 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 52-31 | 62.7 | 52.3 | 10.3 | +16.92 | 20.4 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_rlm+sharp_gap | total | 61-37 | 62.2 | 52.4 | 9.8 | +18.96 | 19.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 22-13 | 62.9 | 51.0 | 11.9 | +6.89 | 19.7 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 96-63 | 60.4 | 52.0 | 8.4 | +24.85 | 15.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 53.8 | 46.2 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_rlm | close | 1-3k bets | 64-65 | 49.6 | 6.2 | 19.1 |  |
| pin_rlm | close | 3k+ bets | 22-23 | 48.9 | 8.1 | 12.9 |  |
| pin_rlm | close | <1k bets | 21-20 | 51.2 | 9.0 | 13.7 |  |
| pin_rlm | close | pin $1-2k | 47-41 | 53.4 | 8.7 | 22.8 |  |
| pin_rlm | close | pin $2k+ | 24-51 | 32.0 | -2.1 | -13.3 |  |
| pin_rlm | close | pin limit <$1k | 36-16 | 69.2 | 17.8 | 49.9 |  |
| follow_move | close | 1-3k bets | 276-269 | 50.6 | 1.0 | -3.3 |  |
| follow_move | close | 3k+ bets | 91-97 | 48.4 | -1.2 | -7.7 |  |
| follow_move | close | <1k bets | 60-72 | 45.5 | -4.3 | -13.1 |  |
| follow_move | close | pin $1-2k | 143-174 | 45.1 | -4.3 | -13.9 |  |
| follow_move | close | pin $2k+ | 78-82 | 48.8 | -1.0 | -7.0 |  |
| follow_move | close | pin limit <$1k | 91-78 | 53.8 | 3.5 | 3.0 |  |
| rlm_ratio | close | 1-3k bets | 82-68 | 54.7 | 3.2 | 4.5 |  |
| rlm_ratio | close | 3k+ bets | 28-17 | 62.2 | 11.3 | 18.9 |  |
| rlm_ratio | close | <1k bets | 19-13 | 59.4 | 7.4 | 14.4 |  |
| rlm_ratio | close | pin $1-2k | 45-36 | 55.6 | 4.7 | 6.1 |  |
| rlm_ratio | close | pin $2k+ | 13-16 | 44.8 | -6.0 | -14.9 |  |
| rlm_ratio | close | pin limit <$1k | 38-20 | 65.5 | 13.1 | 26.0 |  |
| money_level | close | 1-3k bets | 523-362 | 59.1 | 3.6 | -1.1 |  |
| money_level | close | 3k+ bets | 174-146 | 54.4 | -0.8 | -6.2 |  |
| money_level | close | <1k bets | 128-113 | 53.1 | -2.6 | -14.3 |  |
| money_level | close | pin $1-2k | 240-215 | 52.7 | -0.9 | -6.4 |  |
| money_level | close | pin $2k+ | 204-160 | 56.0 | -1.6 | -8.1 |  |
| money_level | close | pin limit <$1k | 98-98 | 50.0 | 0.5 | -4.8 |  |
| sharp_gap | close | 1-3k bets | 385-467 | 45.2 | -1.9 | -8.8 |  |
| sharp_gap | close | 3k+ bets | 155-159 | 49.4 | 2.5 | 6.9 |  |
| sharp_gap | close | <1k bets | 106-126 | 45.7 | -2.7 | -13.7 |  |
| sharp_gap | close | pin $1-2k | 216-227 | 48.8 | -0.0 | -2.3 |  |
| sharp_gap | close | pin $2k+ | 157-194 | 44.7 | -1.0 | -7.9 |  |
| sharp_gap | close | pin limit <$1k | 96-93 | 50.8 | -0.0 | 2.2 |  |
| money_moving | close | 1-3k bets | 385-468 | 45.1 | -2.3 | -9.7 |  |
| money_moving | close | 3k+ bets | 154-162 | 48.7 | 1.5 | 4.5 |  |
| money_moving | close | <1k bets | 104-126 | 45.2 | -2.7 | -12.5 |  |
| money_moving | close | pin $1-2k | 211-233 | 47.5 | -1.0 | -4.0 |  |
| money_moving | close | pin $2k+ | 159-191 | 45.4 | -0.2 | -6.6 |  |
| money_moving | close | pin limit <$1k | 93-98 | 48.7 | -1.9 | -1.8 |  |
| pin_value | close | 1-3k bets | 166-177 | 48.4 | 0.9 | -3.6 |  |
| pin_value | close | 3k+ bets | 57-64 | 47.1 | -0.2 | -6.0 |  |
| pin_value | close | <1k bets | 49-44 | 52.7 | 6.4 | 6.4 |  |
| pin_value | close | pin $1-2k | 127-144 | 46.9 | -0.9 | -8.2 |  |
| pin_value | close | pin $2k+ | 76-85 | 47.2 | 1.8 | -1.2 |  |
| pin_value | close | pin limit <$1k | 69-56 | 55.2 | 6.7 | 8.1 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.4 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.4 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 162-238 | 40.5 | -5.7 | -15.1 |  |
| consensus_gap | close | 3k+ bets | 65-82 | 44.2 | -2.6 | 3.0 |  |
| consensus_gap | close | <1k bets | 37-71 | 34.3 | -9.4 | -28.7 |  |
| consensus_gap | close | pin $1-2k | 84-106 | 44.2 | -3.4 | -4.5 |  |
| consensus_gap | close | pin $2k+ | 68-87 | 43.9 | -5.2 | -11.2 |  |
| consensus_gap | close | pin limit <$1k | 39-39 | 50.0 | 1.8 | -1.1 |  |
| consensus_gap+follow_move | close | 1-3k bets | 43-34 | 55.8 | 8.1 | 4.4 |  |
| consensus_gap+money_level | close | 1-3k bets | 108-80 | 57.4 | 0.7 | 1.0 |  |
| consensus_gap+money_moving | close | 1-3k bets | 72-131 | 35.5 | -7.6 | -13.4 |  |
| consensus_gap+pin_value | close | 1-3k bets | 65-89 | 42.2 | -2.5 | -10.4 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 72-134 | 35.0 | -7.5 | -14.5 |  |
| follow_move+money_level | close | 1-3k bets | 174-169 | 50.7 | 1.6 | -3.4 |  |
| follow_move+money_moving | close | 1-3k bets | 189-193 | 49.5 | -0.4 | -5.7 |  |
| follow_move+pin_value | close | 1-3k bets | 58-51 | 53.2 | 4.2 | 0.3 |  |
| follow_move+sharp_gap | close | 1-3k bets | 190-190 | 50.0 | 0.1 | -4.7 |  |
| money_level+money_moving | close | 1-3k bets | 281-249 | 53.0 | 1.0 | -2.0 |  |
| money_level+pin_value | close | 1-3k bets | 83-78 | 51.6 | 2.7 | -3.2 |  |
| money_level+sharp_gap | close | 1-3k bets | 278-247 | 53.0 | 1.2 | -1.3 |  |
| money_moving+pin_value | close | 1-3k bets | 76-91 | 45.5 | -1.2 | -5.9 |  |
| money_moving+sharp_gap | close | 1-3k bets | 372-452 | 45.1 | -2.0 | -8.8 |  |
| pin_value+sharp_gap | close | 1-3k bets | 78-93 | 45.6 | -1.1 | -6.0 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 13-21 | 38.2 | 1.2 | 28.5 |  |
| money_level+pin_rlm | close | 1-3k bets | 33-19 | 63.5 | 12.9 | 21.9 |  |
| pin_rlm+pin_value | close | 1-3k bets | 20-17 | 54.1 | 8.5 | 41.0 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 64-65 | 49.6 | 6.2 | 19.1 |  |
| money_moving+pin_rlm | close | 1-3k bets | 62-64 | 49.2 | 5.8 | 19.0 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 13-7 | 65.0 | 16.5 | 21.6 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 82-68 | 54.7 | 3.2 | 4.5 |  |
| money_level+rlm_ratio | close | 1-3k bets | 46-38 | 54.8 | 3.8 | 4.7 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 80-68 | 54.1 | 2.7 | 3.4 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 82-68 | 54.7 | 3.2 | 4.5 |  |
| follow_move+pin_rlm | close | 1-3k bets | 39-30 | 56.5 | 4.5 | 8.3 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 39-30 | 56.5 | 4.5 | 8.3 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 18-13 | 58.1 | 7.5 | 10.0 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 46.2 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 16-14 | 53.3 | 5.4 | -0.4 |  |
| consensus_gap+money_moving | close | 3k+ bets | 27-44 | 38.0 | -5.1 | 16.7 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-5 | 37.5 | -2.9 | 19.3 |  |
| consensus_gap+pin_value | close | 3k+ bets | 30-30 | 50.0 | 5.3 | 4.0 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 3-3 | 50.0 | 1.5 | -5.2 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 28-44 | 38.9 | -4.1 | 20.4 |  |
| follow_move+money_moving | close | 3k+ bets | 59-61 | 49.2 | -0.4 | -6.5 |  |
| follow_move+pin_rlm | close | 3k+ bets | 15-10 | 60.0 | 8.5 | 15.5 |  |
| follow_move+pin_value | close | 3k+ bets | 23-24 | 48.9 | -0.1 | -8.2 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 28-17 | 62.2 | 11.3 | 18.9 |  |
| follow_move+sharp_gap | close | 3k+ bets | 63-60 | 51.2 | 1.6 | -2.5 |  |
| money_moving+pin_rlm | close | 3k+ bets | 21-23 | 47.7 | 7.2 | 10.9 |  |
| money_moving+pin_value | close | 3k+ bets | 27-35 | 43.5 | -2.1 | -6.8 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 26-16 | 61.9 | 11.1 | 18.0 |  |
| money_moving+sharp_gap | close | 3k+ bets | 147-152 | 49.2 | 2.2 | 6.5 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-6 | 45.5 | -0.9 | -13.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 15-10 | 60.0 | 8.5 | 15.5 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 22-23 | 48.9 | 8.1 | 12.9 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 6-5 | 54.5 | 4.4 | 2.8 |  |
| pin_value+sharp_gap | close | 3k+ bets | 27-33 | 45.0 | -0.7 | -3.6 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 28-17 | 62.2 | 11.3 | 18.9 |  |
| money_level+money_moving | close | 3k+ bets | 103-92 | 52.8 | 1.0 | -2.1 |  |
| money_level+sharp_gap | close | 3k+ bets | 102-89 | 53.4 | 1.9 | -0.0 |  |
| follow_move+money_level | close | 3k+ bets | 53-55 | 49.1 | 0.3 | -6.7 |  |
| money_level+rlm_ratio | close | 3k+ bets | 16-8 | 66.7 | 16.5 | 26.5 |  |
| consensus_gap+money_level | close | 3k+ bets | 36-35 | 50.7 | -5.2 | -13.3 |  |
| money_level+pin_value | close | 3k+ bets | 28-35 | 44.4 | -4.0 | -17.9 |  |
| money_level+pin_rlm | close | 3k+ bets | 10-6 | 62.5 | 19.1 | 41.6 |  |
| money_level+money_moving | close | <1k bets | 70-75 | 48.3 | -4.4 | -16.7 |  |
| money_level+sharp_gap | close | <1k bets | 73-75 | 49.3 | -3.9 | -16.1 |  |
| money_moving+sharp_gap | close | <1k bets | 102-124 | 45.1 | -3.0 | -13.7 |  |
| consensus_gap+money_level | close | <1k bets | 16-26 | 38.1 | -17.6 | -41.8 |  |
| consensus_gap+money_moving | close | <1k bets | 15-36 | 29.4 | -11.8 | -32.8 |  |
| consensus_gap+pin_value | close | <1k bets | 12-14 | 46.2 | 5.6 | 9.9 |  |
| consensus_gap+sharp_gap | close | <1k bets | 15-37 | 28.8 | -12.1 | -34.1 |  |
| money_level+pin_value | close | <1k bets | 17-17 | 50.0 | 0.6 | -6.7 |  |
| money_moving+pin_value | close | <1k bets | 15-16 | 48.4 | 2.9 | 10.3 |  |
| pin_value+sharp_gap | close | <1k bets | 15-15 | 50.0 | 3.9 | 13.9 |  |
| follow_move+money_moving | close | <1k bets | 33-44 | 42.9 | -7.3 | -17.8 |  |
| follow_move+sharp_gap | close | <1k bets | 33-44 | 42.9 | -7.4 | -17.8 |  |
| follow_move+money_level | close | <1k bets | 27-43 | 38.6 | -10.9 | -26.2 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -0.8 | 12.2 |  |
| money_moving+pin_rlm | close | <1k bets | 21-20 | 51.2 | 9.0 | 13.7 |  |
| pin_rlm+sharp_gap | close | <1k bets | 21-20 | 51.2 | 9.0 | 13.7 |  |
| consensus_gap+follow_move | close | <1k bets | 3-9 | 25.0 | -23.2 | -54.1 |  |
| follow_move+pin_rlm | close | <1k bets | 13-6 | 68.4 | 16.1 | 31.3 |  |
| follow_move+pin_value | close | <1k bets | 16-11 | 59.3 | 10.0 | 12.6 |  |
| follow_move+rlm_ratio | close | <1k bets | 19-13 | 59.4 | 7.4 | 14.4 |  |
| money_moving+rlm_ratio | close | <1k bets | 19-13 | 59.4 | 7.4 | 14.4 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 19.9 | 60.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 13-6 | 68.4 | 16.1 | 31.3 |  |
| pin_value+rlm_ratio | close | <1k bets | 3-1 | 75.0 | 22.8 | 43.9 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 19-13 | 59.4 | 7.4 | 14.4 |  |
| money_level+rlm_ratio | close | <1k bets | 10-9 | 52.6 | 0.6 | 1.6 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 16.0 | 19.0 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 23-24 | 48.9 | 1.1 | -8.6 |  |
| consensus_gap+money_moving | close | pin $1-2k | 44-58 | 43.1 | -3.8 | -4.5 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 12-16 | 42.9 | 2.4 | 32.5 |  |
| consensus_gap+pin_value | close | pin $1-2k | 50-64 | 43.9 | -0.6 | -10.3 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 9-7 | 56.2 | 8.0 | 5.1 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 44-55 | 44.4 | -1.7 | -1.6 |  |
| follow_move+money_moving | close | pin $1-2k | 98-119 | 45.2 | -4.4 | -13.9 |  |
| follow_move+pin_rlm | close | pin $1-2k | 32-21 | 60.4 | 8.7 | 15.7 |  |
| follow_move+pin_value | close | pin $1-2k | 44-48 | 47.8 | -1.4 | -9.9 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 45-36 | 55.6 | 4.7 | 6.1 |  |
| follow_move+sharp_gap | close | pin $1-2k | 100-118 | 45.9 | -3.8 | -12.5 |  |
| money_moving+pin_rlm | close | pin $1-2k | 45-40 | 52.9 | 8.2 | 22.7 |  |
| money_moving+pin_value | close | pin $1-2k | 51-70 | 42.1 | -5.0 | -16.3 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 44-35 | 55.7 | 4.9 | 6.3 |  |
| money_moving+sharp_gap | close | pin $1-2k | 207-223 | 48.1 | -0.5 | -3.2 |  |
| pin_rlm+pin_value | close | pin $1-2k | 11-16 | 40.7 | -7.5 | -12.3 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 32-21 | 60.4 | 8.7 | 15.7 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 47-41 | 53.4 | 8.7 | 22.8 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 13-13 | 50.0 | 0.1 | -6.0 |  |
| pin_value+sharp_gap | close | pin $1-2k | 51-68 | 42.9 | -4.3 | -14.9 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 45-36 | 55.6 | 4.7 | 6.1 |  |
| follow_move+money_level | close | pin $1-2k | 96-110 | 46.6 | -2.3 | -11.2 |  |
| money_level+rlm_ratio | close | pin $1-2k | 30-19 | 61.2 | 11.1 | 16.6 |  |
| money_level+sharp_gap | close | pin $1-2k | 159-152 | 51.1 | -0.3 | -4.8 |  |
| money_level+money_moving | close | pin $1-2k | 156-155 | 50.2 | -1.2 | -6.3 |  |
| consensus_gap+money_level | close | pin $1-2k | 48-49 | 49.5 | -5.8 | -11.9 |  |
| money_level+pin_value | close | pin $1-2k | 55-61 | 47.4 | -1.7 | -11.2 |  |
| money_level+pin_rlm | close | pin $1-2k | 25-15 | 62.5 | 14.9 | 23.4 |  |
| follow_move+money_level | close | pin $2k+ | 43-49 | 46.7 | -2.5 | -10.9 |  |
| follow_move+money_moving | close | pin $2k+ | 49-51 | 49.0 | -0.6 | -6.7 |  |
| follow_move+sharp_gap | close | pin $2k+ | 50-51 | 49.5 | -0.1 | -5.7 |  |
| money_level+money_moving | close | pin $2k+ | 104-98 | 51.5 | -1.0 | -5.6 |  |
| money_level+sharp_gap | close | pin $2k+ | 104-100 | 51.0 | -1.6 | -6.2 |  |
| money_moving+sharp_gap | close | pin $2k+ | 154-189 | 44.9 | -0.7 | -7.1 |  |
| consensus_gap+money_moving | close | pin $2k+ | 23-50 | 31.5 | -10.3 | -16.2 |  |
| consensus_gap+pin_value | close | pin $2k+ | 30-39 | 43.5 | 2.3 | 3.7 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 24-53 | 31.2 | -11.7 | -18.7 |  |
| money_moving+pin_value | close | pin $2k+ | 39-48 | 44.8 | 1.1 | 3.7 |  |
| pin_value+sharp_gap | close | pin $2k+ | 39-48 | 44.8 | 1.1 | 3.7 |  |
| consensus_gap+follow_move | close | pin $2k+ | 8-6 | 57.1 | 8.8 | 5.7 |  |
| follow_move+pin_value | close | pin $2k+ | 25-19 | 56.8 | 7.5 | 6.9 |  |
| follow_move+pin_rlm | close | pin $2k+ | 7-13 | 35.0 | -16.6 | -33.3 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 13-16 | 44.8 | -6.0 | -14.9 |  |
| money_level+pin_rlm | close | pin $2k+ | 9-8 | 52.9 | 10.9 | 17.5 |  |
| money_level+pin_value | close | pin $2k+ | 38-39 | 49.4 | 0.1 | -9.0 |  |
| money_level+rlm_ratio | close | pin $2k+ | 6-8 | 42.9 | -7.5 | -18.7 |  |
| money_moving+pin_rlm | close | pin $2k+ | 24-51 | 32.0 | -2.1 | -13.3 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 13-16 | 44.8 | -6.0 | -14.9 |  |
| pin_rlm+pin_value | close | pin $2k+ | 5-8 | 38.5 | 4.2 | 51.3 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 7-13 | 35.0 | -16.6 | -33.3 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 24-51 | 32.0 | -2.1 | -13.3 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 2-2 | 50.0 | -1.3 | -7.3 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 13-16 | 44.8 | -6.0 | -14.9 |  |
| consensus_gap+money_level | close | pin $2k+ | 47-36 | 56.6 | -5.4 | -12.1 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-15 | 21.1 | -7.8 | -9.0 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -52.6 | -100.0 |  |
| money_level+money_moving | close | pin limit <$1k | 56-60 | 48.3 | -1.7 | -7.2 |  |
| money_level+sharp_gap | close | pin limit <$1k | 58-59 | 49.6 | -0.6 | -4.8 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 89-88 | 50.3 | -0.5 | 1.6 |  |
| consensus_gap+money_level | close | pin limit <$1k | 21-22 | 48.8 | 0.6 | -9.8 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 27-30 | 47.4 | -0.1 | -3.2 |  |
| follow_move+money_moving | close | pin limit <$1k | 57-56 | 50.4 | -0.6 | -3.3 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 59-54 | 52.2 | 1.0 | 0.1 |  |
| money_level+pin_value | close | pin limit <$1k | 35-30 | 53.8 | 6.1 | 1.7 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 13-10 | 56.5 | 8.9 | 5.9 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 17-15 | 53.1 | 6.0 | 13.9 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 18-16 | 52.9 | 5.2 | 12.7 |  |
| follow_move+money_level | close | pin limit <$1k | 47-44 | 51.6 | 2.1 | -1.3 |  |
| follow_move+pin_value | close | pin limit <$1k | 28-19 | 59.6 | 10.9 | 12.8 |  |
| money_moving+pin_value | close | pin limit <$1k | 28-24 | 53.8 | 5.3 | 10.7 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 30-25 | 54.5 | 5.6 | 11.5 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 3-2 | 60.0 | 17.8 | 101.6 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 35-16 | 68.6 | 17.3 | 49.1 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 14-2 | 87.5 | 38.3 | 94.7 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 36-16 | 69.2 | 17.8 | 49.9 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 28-12 | 70.0 | 17.6 | 34.7 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 38-20 | 65.5 | 13.1 | 26.0 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 36-20 | 64.3 | 11.9 | 23.7 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 28-12 | 70.0 | 17.6 | 34.7 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 38-20 | 65.5 | 13.1 | 26.0 |  |
| money_level+pin_rlm | close | pin limit <$1k | 18-8 | 69.2 | 16.6 | 32.9 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 19-11 | 63.3 | 10.8 | 22.1 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 12-4 | 75.0 | 23.6 | 43.9 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 3-3 | 50.0 | 2.5 | -5.2 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 46.2 | 87.7 |  |
| pin_rlm | early | <1k bets | 1-1 | 50.0 | 24.0 | -3.7 | -2.15 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.0 | -100.0 | -4.8 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.0 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 15-16 | 48.4 | -0.9 | -7.7 | -0.1 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -49.4 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 154-172 | 47.2 | -2.2 | -9.5 | 0.19 |
| follow_move | early | pin $1-2k | 10-9 | 52.6 | 2.5 | -0.6 | 0.0 |
| follow_move | early | pin limit <$1k | 34-29 | 54.0 | 4.9 | 2.6 | -0.33 |
| rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 14.8 | 29.2 | -0.5 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.6 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 4-3 | 57.1 | 4.3 | 9.7 | 0.57 |
| rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -2.6 | -1.0 | -0.5 |
| rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 27.7 | 53.6 | -0.4 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 0.0 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 41.6 | 59.7 | 0.33 |
| money_level | early | <1k bets | 93-56 | 62.4 | 3.1 | -4.0 | 0.21 |
| money_level | early | pin $1-2k | 15-8 | 65.2 | 0.9 | -2.7 | -0.03 |
| money_level | early | pin limit <$1k | 22-24 | 47.8 | -6.1 | -12.1 | 0.31 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.0 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 6.5 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 79-59 | 57.2 | 7.7 | 9.6 | 0.42 |
| sharp_gap | early | pin $1-2k | 12-9 | 57.1 | 4.5 | 13.4 | -0.59 |
| sharp_gap | early | pin limit <$1k | 27-16 | 62.8 | 14.0 | 30.8 | 0.2 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.1 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.4 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 48-40 | 54.5 | 2.8 | -3.9 | 0.12 |
| money_moving | early | pin $1-2k | 6-6 | 50.0 | -11.6 | -26.9 | 0.35 |
| money_moving | early | pin limit <$1k | 20-9 | 69.0 | 19.7 | 47.8 | 0.36 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.4 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.6 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 30-33 | 47.6 | 0.0 | -9.7 | 0.19 |
| pin_value | early | pin $1-2k | 11-14 | 44.0 | -0.4 | -16.7 | 0.17 |
| pin_value | early | pin limit <$1k | 32-28 | 53.3 | 4.0 | 0.8 | 0.13 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -46.2 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -27.9 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -10.9 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 13.3 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 130-178 | 42.2 | -4.7 | -17.4 | 0.28 |
| consensus_gap | early | pin $1-2k | 10-17 | 37.0 | -8.1 | -27.6 | 0.49 |
| consensus_gap | early | pin limit <$1k | 17-33 | 34.0 | -16.1 | -29.1 | 0.31 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 16.0 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 2.6 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 2.9 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.1 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 18.8 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 15.4 | 26.0 | -0.25 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 4.3 | -6.9 | 0.3 |
| consensus_gap+follow_move | early | 1-3k bets | 4-4 | 50.0 | 2.7 | -6.9 | 0.25 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.9 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.4 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 10-10 | 50.0 | 0.0 | -4.1 | 0.05 |
| follow_move+pin_value | early | 1-3k bets | 7-5 | 58.3 | 9.0 | 9.2 | -0.42 |
| follow_move+sharp_gap | early | 1-3k bets | 9-8 | 52.9 | 2.6 | 1.2 | -0.18 |
| follow_move+rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 14.8 | 29.2 | -0.5 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 26.9 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 4-2 | 66.7 | 14.8 | 29.2 | -0.5 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 18.0 | 56.1 | 0.15 |
| follow_move+money_moving | early | 1-3k bets | 9-4 | 69.2 | 19.7 | 32.1 | 0.08 |
| money_moving+rlm_ratio | early | 1-3k bets | 2-1 | 66.7 | 15.8 | 28.7 | -1.0 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.6 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.6 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.6 | 83.3 | 1.0 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.6 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.6 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.4 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.6 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.6 | 83.3 | 1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.6 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 36.1 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 46.2 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 12-12 | 50.0 | 1.0 | -5.8 | 1.38 |
| consensus_gap+money_level | early | <1k bets | 18-15 | 54.5 | -10.8 | -19.3 | 0.26 |
| consensus_gap+sharp_gap | early | <1k bets | 15-28 | 34.9 | -12.7 | -17.7 | 0.7 |
| follow_move+money_level | early | <1k bets | 17-14 | 54.8 | 7.0 | 4.4 | 0.74 |
| follow_move+sharp_gap | early | <1k bets | 18-9 | 66.7 | 17.3 | 27.2 | 1.0 |
| money_level+sharp_gap | early | <1k bets | 55-28 | 66.3 | 9.5 | 7.4 | 0.55 |
| money_level+money_moving | early | <1k bets | 32-22 | 59.3 | 1.5 | -6.0 | -0.03 |
| money_moving+sharp_gap | early | <1k bets | 31-22 | 58.5 | 7.8 | 5.0 | 0.37 |
| consensus_gap+money_moving | early | <1k bets | 8-16 | 33.3 | -13.2 | -46.4 | 0.14 |
| follow_move+pin_value | early | <1k bets | 11-10 | 52.4 | 3.5 | -1.5 | 0.29 |
| follow_move+money_moving | early | <1k bets | 9-8 | 52.9 | 4.2 | 1.5 | 0.59 |
| consensus_gap+pin_value | early | <1k bets | 11-22 | 33.3 | -12.3 | -37.3 | 0.45 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -26.0 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -26.0 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | <1k bets | 1-1 | 50.0 | 24.0 | -3.7 | -2.15 |
| pin_value+sharp_gap | early | <1k bets | 4-3 | 57.1 | 11.5 | 9.1 | 0.03 |
| money_level+pin_value | early | <1k bets | 3-3 | 50.0 | 1.3 | -4.5 | 1.33 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -53.2 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -53.8 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 0-2 | 0.0 | -49.4 | -100.0 | 2.5 |
| follow_move+rlm_ratio | early | <1k bets | 4-3 | 57.1 | 4.3 | 9.7 | 0.57 |
| money_level+rlm_ratio | early | <1k bets | 2-2 | 50.0 | -3.8 | -3.5 | 1.25 |
| money_moving+rlm_ratio | early | <1k bets | 2-2 | 50.0 | -2.2 | -3.5 | 0.5 |
| rlm_ratio+sharp_gap | early | <1k bets | 4-3 | 57.1 | 4.3 | 9.7 | 0.57 |
| consensus_gap+rlm_ratio | early | <1k bets | 1-1 | 50.0 | -3.8 | -4.5 | 0.5 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 46.2 | 90.9 | 1.0 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 74.0 | 92.6 | 0.5 |
| consensus_gap+money_level | early | pin $1-2k | 4-4 | 50.0 | -14.1 | -22.9 | 0.44 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -31.8 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 4-9 | 30.8 | -8.8 | -42.5 | 0.4 |
| follow_move+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -2.6 | -1.0 | -0.5 |
| follow_move+sharp_gap | early | pin $1-2k | 3-1 | 75.0 | 25.0 | 45.0 | -0.25 |
| money_level+money_moving | early | pin $1-2k | 6-5 | 54.5 | -10.3 | -20.3 | 0.02 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.5 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 1-1 | 50.0 | -2.6 | -1.0 | -0.5 |
| money_level+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 6.3 | 8.3 | -0.45 |
| money_moving+sharp_gap | early | pin $1-2k | 3-5 | 37.5 | -21.2 | -45.3 | -0.06 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.7 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 2-2 | 50.0 | 0.0 | -8.4 | 0.75 |
| follow_move+money_level | early | pin $1-2k | 3-2 | 60.0 | 11.5 | 16.0 | 0.2 |
| follow_move+pin_value | early | pin $1-2k | 4-3 | 57.1 | 7.5 | 6.9 | 0.29 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 47.4 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 1-0 | 100.0 | 52.6 | 90.9 | 0.0 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.0 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -25.0 | -62.8 | -0.72 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -26.0 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -26.0 | -100.0 | -4.8 |
| money_level+money_moving | early | pin limit <$1k | 11-7 | 61.1 | 7.9 | 12.1 | 0.53 |
| money_level+sharp_gap | early | pin limit <$1k | 18-14 | 56.2 | 4.9 | 2.3 | 0.25 |
| money_moving+sharp_gap | early | pin limit <$1k | 16-5 | 76.2 | 27.9 | 68.0 | 0.39 |
| money_level+pin_value | early | pin limit <$1k | 8-5 | 61.5 | 10.1 | 16.6 | 0.46 |
| money_moving+pin_value | early | pin limit <$1k | 6-4 | 60.0 | 9.9 | 13.0 | 0.3 |
| pin_value+sharp_gap | early | pin limit <$1k | 11-5 | 68.8 | 18.2 | 30.3 | 0.06 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-7 | 46.2 | -1.3 | -14.2 | 0.46 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -27.1 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 13-18 | 41.9 | -6.3 | -21.4 | 0.44 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.3 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 8-7 | 53.3 | 3.3 | 1.9 | 0.07 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 5.0 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 9-7 | 56.2 | 6.0 | 6.9 | -0.31 |
| follow_move+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 27.7 | 53.6 | -0.4 |
| money_level+rlm_ratio | early | pin limit <$1k | 4-0 | 100.0 | 46.2 | 92.0 | 0.25 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.4 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 4-1 | 80.0 | 27.7 | 53.6 | -0.4 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 23.3 | 72.3 | 0.54 |
| follow_move+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 20.4 | 33.3 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.4 | 28.7 | -1.0 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -53.8 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -53.8 | -100.0 | 1.0 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.0 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 74.0 | 92.6 | 0.5 |
