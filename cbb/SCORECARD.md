# CBB scorecard

Generated 2026-11-16 07:20 UTC. 508 graded games (13 finished games had no final score matched and are not graded).

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before tip. Break-even at -110 is 52.4%. CLV = points of closing-line
value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured
on this sample. `edge` is hit% minus that. A signal that is structurally long
favourites or overs beats 50% whenever those run, which is not an edge -- this
sample ran **47.1% favourites** (n=507) and **45.9% overs** (n=508) and **74.2% moneyline favourites** (n=431).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

## EARLY

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 1-1 | 50.0 | 25.8 | 24.2 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | both | 188-208 | 47.5 | 49.3 | -1.8 | -35.89 | -9.1 | 0.13 | 39.1 | DROP: below break-even |
| rlm_ratio | both | 7-6 | 53.8 | 52.6 | 1.3 | +0.52 | 4.0 | 0.0 | 30.8 | keep collecting (13/30) |
| money_level | both | 118-74 | 61.5 | 58.5 | 3.0 | -6.07 | -3.2 | 0.23 | 42.2 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 103-79 | 56.6 | 49.3 | 7.3 | +22.23 | 12.2 | 0.35 | 42.9 | no edge shown yet |
| money_moving | both | 70-48 | 59.3 | 51.2 | 8.1 | +11.37 | 9.6 | 0.2 | 43.2 | PROMOTE: beats break-even and its own base rate |
| pin_value | both | 43-42 | 50.6 | 47.8 | 2.8 | -3.68 | -4.3 | 0.14 | 41.2 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.7 | -31.7 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 156-221 | 41.4 | 46.6 | -5.2 | -65.15 | -17.3 | 0.31 | 45.9 | DROP: below break-even |
| consensus_gap+money_level | both | 23-22 | 51.1 | 63.3 | -12.1 | -10.62 | -23.6 | 0.25 | 46.7 | no edge shown yet |
| consensus_gap+money_moving | both | 15-18 | 45.5 | 46.3 | -0.9 | -2.69 | -8.2 | 0.18 | 39.4 | no edge shown yet |
| consensus_gap+pin_value | both | 17-27 | 38.6 | 45.5 | -6.9 | -12.16 | -27.6 | 0.43 | 52.3 | DROP: below break-even |
| follow_move+rlm_ratio | both | 7-6 | 53.8 | 52.6 | 1.3 | +0.52 | 4.0 | 0.0 | 30.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 26-18 | 59.1 | 49.7 | 9.4 | +5.63 | 12.8 | 0.52 | 40.9 | no edge shown yet |
| money_level+money_moving | both | 45-26 | 63.4 | 56.9 | 6.5 | +3.08 | 4.3 | 0.16 | 49.3 | PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | both | 10-8 | 55.6 | 50.7 | 4.9 | +0.9 | 5.0 | 0.5 | 50.0 | keep collecting (18/30) |
| money_moving+pin_value | both | 7-5 | 58.3 | 50.1 | 8.2 | +1.13 | 9.4 | 0.42 | 41.7 | keep collecting (12/30) |
| rlm_ratio+sharp_gap | both | 7-6 | 53.8 | 52.6 | 1.3 | +0.52 | 4.0 | 0.0 | 30.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 72-41 | 63.7 | 55.6 | 8.1 | +7.11 | 6.3 | 0.49 | 46.0 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 44-28 | 61.1 | 49.5 | 11.6 | +12.34 | 17.1 | 0.44 | 45.8 | no edge shown yet |
| pin_value+sharp_gap | both | 12-7 | 63.2 | 49.2 | 13.9 | +3.75 | 19.8 | -0.15 | 36.8 | keep collecting (19/30) |
| consensus_gap+follow_move | both | 15-16 | 48.4 | 48.2 | 0.2 | -2.86 | -9.2 | 1.13 | 54.8 | no edge shown yet |
| consensus_gap+sharp_gap | both | 17-33 | 34.0 | 46.3 | -12.3 | -6.48 | -13.0 | 0.62 | 46.0 | DROP: below break-even |
| follow_move+money_level | both | 27-23 | 54.0 | 48.5 | 5.5 | +1.56 | 3.1 | 0.52 | 42.0 | no edge shown yet |
| follow_move+pin_value | both | 18-15 | 54.5 | 48.9 | 5.6 | +0.8 | 2.4 | 0.03 | 30.3 | no edge shown yet |
| money_level+rlm_ratio | both | 6-3 | 66.7 | 53.7 | 13.0 | +2.61 | 29.0 | 0.56 | 33.3 | keep collecting (9/30) |
| pin_value+rlm_ratio | both | 2-1 | 66.7 | 51.4 | 15.3 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| follow_move+money_moving | both | 18-12 | 60.0 | 49.0 | 11.0 | +4.43 | 14.8 | 0.37 | 43.3 | no edge shown yet |
| money_moving+rlm_ratio | both | 4-3 | 57.1 | 51.8 | 5.4 | +0.72 | 10.3 | -0.14 | 28.6 | keep collecting (7/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | both | 1-1 | 50.0 | 25.8 | 24.2 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 53.5 | -53.5 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 54.1 | -54.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 0-1 | 0.0 | 54.1 | -54.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 25.8 | 74.2 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-1 | 50.0 | 25.8 | 24.2 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | spread | 93-108 | 46.3 | 49.2 | -2.9 | -22.69 | -11.3 | -0.0 | 33.8 | DROP: below break-even |
| follow_move | total | 95-100 | 48.7 | 49.4 | -0.7 | -13.2 | -6.8 | 0.28 | 44.6 | no edge shown yet |
| rlm_ratio | spread | 3-2 | 60.0 | 51.7 | 8.3 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 4-4 | 50.0 | 53.1 | -3.1 | -0.32 | -4.0 | 0.38 | 50.0 | keep collecting (8/30) |
| money_level | moneyline | 63-27 | 70.0 | 69.4 | 0.6 | -8.96 | -10.0 | 0.18 | 46.7 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 16-15 | 51.6 | 49.0 | 2.6 | -0.6 | -1.9 | 0.9 | 48.4 | no edge shown yet |
| money_level | total | 39-32 | 54.9 | 48.8 | 6.2 | +3.48 | 4.9 | -0.01 | 33.8 | no edge shown yet |
| sharp_gap | moneyline | 43-37 | 53.8 | 47.6 | 6.2 | +9.7 | 12.1 | 0.39 | 50.0 | no edge shown yet |
| sharp_gap | spread | 18-14 | 56.2 | 49.8 | 6.4 | +2.26 | 7.1 | 0.56 | 34.4 | no edge shown yet |
| sharp_gap | total | 42-28 | 60.0 | 51.1 | 8.9 | +10.26 | 14.7 | 0.21 | 38.6 | no edge shown yet |
| money_moving | moneyline | 26-25 | 51.0 | 53.3 | -2.3 | -5.41 | -10.6 | 0.24 | 54.9 | no edge shown yet |
| money_moving | spread | 17-4 | 81.0 | 49.0 | 31.9 | +11.27 | 53.7 | 0.14 | 38.1 | keep collecting (21/30) |
| money_moving | total | 27-19 | 58.7 | 49.8 | 8.9 | +5.51 | 12.0 | 0.17 | 32.6 | no edge shown yet |
| pin_value | moneyline | 1-5 | 16.7 | 25.8 | -9.1 | -4.02 | -67.0 | -0.02 | 66.7 | keep collecting (6/30) |
| pin_value | spread | 22-17 | 56.4 | 49.2 | 7.2 | +2.35 | 6.0 | 0.28 | 41.0 | no edge shown yet |
| pin_value | total | 20-20 | 50.0 | 49.8 | 0.2 | -2.01 | -5.0 | 0.03 | 37.5 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.9 | -19.5 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 63-120 | 34.4 | 43.8 | -9.3 | -46.49 | -25.4 | -0.03 | 42.6 | DROP: below break-even |
| consensus_gap | spread | 50-48 | 51.0 | 49.1 | 1.9 | -4.35 | -4.4 | 0.48 | 44.9 | no edge shown yet |
| consensus_gap | total | 43-53 | 44.8 | 49.3 | -4.5 | -14.3 | -14.9 | 0.77 | 53.1 | no edge shown yet |
| money_level+sharp_gap | moneyline | 33-12 | 73.3 | 64.5 | 8.8 | +0.72 | 1.6 | 0.53 | 57.8 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+pin_value | moneyline | 1-5 | 16.7 | 25.8 | -9.1 | -4.02 | -67.0 | -0.02 | 66.7 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_level+money_moving | moneyline | 17-9 | 65.4 | 70.5 | -5.1 | -5.47 | -21.0 | -0.07 | 57.7 | keep collecting (26/30) |
| consensus_gap+sharp_gap | moneyline | 11-24 | 31.4 | 45.2 | -13.7 | -2.71 | -7.7 | 0.55 | 48.6 | DROP: below break-even |
| consensus_gap+money_level | moneyline | 16-14 | 53.3 | 71.0 | -17.7 | -8.68 | -28.9 | -0.09 | 46.7 | INVERT candidate: wrong well beyond its base rate |
| money_moving+sharp_gap | moneyline | 15-13 | 53.6 | 48.3 | 5.3 | +1.07 | 3.8 | 0.67 | 64.3 | keep collecting (28/30) |
| consensus_gap+money_moving | moneyline | 7-17 | 29.2 | 46.0 | -16.8 | -8.63 | -36.0 | 0.28 | 50.0 | keep collecting (24/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | moneyline | 1-1 | 50.0 | 25.8 | 24.2 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 25.8 | 74.2 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 4-5 | 44.4 | 47.1 | -2.7 | -1.59 | -17.7 | 1.67 | 66.7 | keep collecting (9/30) |
| consensus_gap+money_moving | spread | 4-0 | 100.0 | 47.1 | 52.9 | +3.41 | 85.2 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_value | spread | 9-8 | 52.9 | 48.1 | 4.8 | -0.31 | -1.8 | 0.53 | 52.9 | keep collecting (17/30) |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.7 | 8.3 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 48.6 | 13.9 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 9-4 | 69.2 | 48.5 | 20.8 | +4.21 | 32.4 | 0.77 | 61.5 | keep collecting (13/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.8 | -5.9 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.4 | 10.6 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 51.7 | 8.3 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 13-11 | 54.2 | 49.0 | 5.1 | +0.71 | 3.0 | 0.96 | 41.7 | keep collecting (24/30) |
| money_moving+sharp_gap | spread | 9-3 | 75.0 | 49.0 | 26.0 | +5.13 | 42.7 | 0.42 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.0 | 17.6 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 8-8 | 50.0 | 47.9 | 2.1 | -1.18 | -7.4 | 0.94 | 43.8 | keep collecting (16/30) |
| consensus_gap+sharp_gap | spread | 3-3 | 50.0 | 47.1 | 2.9 | -0.43 | -7.1 | 2.17 | 66.7 | keep collecting (6/30) |
| follow_move+money_level | spread | 11-7 | 61.1 | 48.1 | 13.0 | +3.04 | 16.9 | 0.78 | 44.4 | keep collecting (18/30) |
| follow_move+pin_value | spread | 11-7 | 61.1 | 48.7 | 12.4 | +2.56 | 14.2 | 0.33 | 33.3 | keep collecting (18/30) |
| follow_move+money_moving | spread | 9-1 | 90.0 | 47.7 | 42.3 | +7.22 | 72.2 | 0.2 | 40.0 | keep collecting (10/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 52.9 | 13.8 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.9 | -52.9 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 19-13 | 59.4 | 49.2 | 10.2 | +4.34 | 13.6 | 0.09 | 37.5 | no edge shown yet |
| money_level+sharp_gap | total | 26-18 | 59.1 | 50.0 | 9.1 | +5.68 | 12.9 | 0.18 | 36.4 | no edge shown yet |
| money_moving+sharp_gap | total | 20-12 | 62.5 | 50.8 | 11.7 | +6.14 | 19.2 | 0.25 | 31.2 | no edge shown yet |
| money_level+pin_value | total | 7-4 | 63.6 | 51.9 | 11.8 | +2.32 | 21.1 | 0.36 | 36.4 | keep collecting (11/30) |
| money_moving+pin_value | total | 4-3 | 57.1 | 50.6 | 6.6 | +0.56 | 8.0 | 0.29 | 28.6 | keep collecting (7/30) |
| pin_value+sharp_gap | total | 10-5 | 66.7 | 50.8 | 15.8 | +4.01 | 26.7 | 0.0 | 33.3 | keep collecting (15/30) |
| follow_move+money_level | total | 16-16 | 50.0 | 48.7 | 1.3 | -1.47 | -4.6 | 0.38 | 40.6 | no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.2 | -2.5 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 4-4 | 50.0 | 53.1 | -3.1 | -0.32 | -4.0 | 0.38 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 16-12 | 57.1 | 50.3 | 6.8 | +2.55 | 9.1 | 0.46 | 42.9 | keep collecting (28/30) |
| money_level+rlm_ratio | total | 4-2 | 66.7 | 54.1 | 12.5 | +1.68 | 28.0 | 0.83 | 50.0 | keep collecting (6/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 51.4 | 15.3 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 4-4 | 50.0 | 53.1 | -3.1 | -0.32 | -4.0 | 0.38 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 9-11 | 45.0 | 49.6 | -4.6 | -2.8 | -14.0 | 0.45 | 45.0 | keep collecting (20/30) |
| consensus_gap+money_level | total | 3-3 | 50.0 | 48.6 | 1.4 | -0.34 | -5.7 | -0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 47.5 | 32.5 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 49.0 | -15.7 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 3-6 | 33.3 | 50.5 | -17.1 | -3.35 | -37.2 | -0.11 | 22.2 | keep collecting (9/30) |
| money_moving+rlm_ratio | total | 2-3 | 40.0 | 52.5 | -12.5 | -1.14 | -22.8 | 0.2 | 40.0 | keep collecting (5/30) |
| consensus_gap+follow_move | total | 7-8 | 46.7 | 48.6 | -2.0 | -1.67 | -11.1 | 1.33 | 66.7 | keep collecting (15/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 54.1 | -54.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 54.1 | -54.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 0-1 | 0.0 | 54.1 | -54.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |

## CLOSE

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 100-106 | 48.5 | 42.8 | 5.7 | +26.73 | 13.0 |  |  | no edge shown yet |
| follow_move | both | 411-423 | 49.3 | 49.6 | -0.3 | -49.63 | -6.0 |  |  | DROP: below break-even |
| rlm_ratio | both | 123-97 | 55.9 | 51.6 | 4.3 | +15.44 | 7.0 |  |  | no edge shown yet |
| money_level | both | 791-600 | 56.9 | 55.5 | 1.4 | -67.46 | -4.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 615-730 | 45.7 | 47.3 | -1.5 | -93.88 | -7.0 |  |  | DROP: below break-even |
| money_moving | both | 612-734 | 45.5 | 47.4 | -2.0 | -105.09 | -7.8 |  |  | DROP: below break-even |
| pin_value | both | 264-273 | 49.2 | 47.1 | 2.0 | -8.88 | -1.7 |  |  | DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 51.0 | 15.7 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 255-380 | 40.2 | 45.9 | -5.8 | -88.63 | -14.0 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 61-56 | 52.1 | 47.5 | 4.6 | -3.15 | -2.7 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 109-206 | 34.6 | 42.7 | -8.1 | -31.46 | -10.0 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 18-32 | 36.0 | 36.1 | -0.1 | +12.56 | 25.1 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 104-130 | 44.4 | 44.1 | 0.4 | -10.63 | -4.5 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | both | 15-12 | 55.6 | 48.3 | 7.2 | +1.11 | 4.1 |  |  | keep collecting (27/30) |
| consensus_gap+sharp_gap | both | 110-210 | 34.4 | 42.3 | -7.9 | -32.29 | -10.1 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 272-293 | 48.1 | 49.8 | -1.7 | -46.49 | -8.2 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 65-46 | 58.6 | 52.2 | 6.4 | +13.73 | 12.4 |  |  | no edge shown yet |
| follow_move+pin_value | both | 96-84 | 53.3 | 48.9 | 4.4 | +1.0 | 0.6 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 123-97 | 55.9 | 51.6 | 4.3 | +15.44 | 7.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 276-289 | 48.8 | 49.9 | -1.0 | -38.63 | -6.8 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 97-105 | 48.0 | 42.8 | 5.3 | +24.99 | 12.4 |  |  | no edge shown yet |
| money_moving+pin_value | both | 113-137 | 45.2 | 46.2 | -1.0 | -10.31 | -4.1 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 120-96 | 55.6 | 51.5 | 4.0 | +13.6 | 6.3 |  |  | no edge shown yet |
| money_moving+sharp_gap | both | 591-707 | 45.5 | 47.3 | -1.7 | -92.89 | -7.2 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 28-26 | 51.9 | 45.1 | 6.7 | +16.74 | 31.0 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 65-46 | 58.6 | 52.2 | 6.4 | +13.73 | 12.4 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 100-106 | 48.5 | 42.8 | 5.7 | +26.73 | 13.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 27-19 | 58.7 | 50.6 | 8.1 | +5.18 | 11.3 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 115-136 | 45.8 | 46.3 | -0.5 | -7.55 | -3.0 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 123-97 | 55.9 | 51.6 | 4.3 | +15.44 | 7.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+money_moving | both | 431-405 | 51.6 | 52.0 | -0.5 | -48.14 | -5.8 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 431-401 | 51.8 | 51.9 | -0.1 | -40.96 | -4.9 |  |  | no edge shown yet |
| follow_move+money_level | both | 245-259 | 48.6 | 49.0 | -0.3 | -37.41 | -7.4 |  |  | DROP: below break-even |
| money_level+rlm_ratio | both | 68-54 | 55.7 | 51.2 | 4.5 | +7.94 | 6.5 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 156-139 | 52.9 | 56.4 | -3.5 | -26.12 | -8.9 |  |  | no edge shown yet |
| money_level+pin_value | both | 123-124 | 49.8 | 48.7 | 1.1 | -17.15 | -6.9 |  |  | no edge shown yet |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | both | 47-31 | 60.3 | 48.4 | 11.9 | +13.99 | 17.9 |  |  | no edge shown yet |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 54.1 | 45.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 26-53 | 32.9 | 27.6 | 5.3 | +11.98 | 15.2 |  |  | DROP: below break-even |
| pin_rlm | spread | 17-16 | 51.5 | 51.1 | 0.4 | -0.62 | -1.9 |  |  | no edge shown yet |
| pin_rlm | total | 57-37 | 60.6 | 52.7 | 7.9 | +15.36 | 16.3 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move | spread | 189-193 | 49.5 | 49.1 | 0.4 | -22.24 | -5.8 |  |  | no edge shown yet |
| follow_move | total | 222-230 | 49.1 | 50.0 | -0.9 | -27.39 | -6.1 |  |  | no edge shown yet |
| rlm_ratio | spread | 33-34 | 49.3 | 50.0 | -0.8 | -3.97 | -5.9 |  |  | no edge shown yet |
| rlm_ratio | total | 90-63 | 58.8 | 52.2 | 6.6 | +19.41 | 12.7 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level | moneyline | 311-112 | 73.5 | 69.9 | 3.6 | -13.89 | -3.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 228-244 | 48.3 | 49.0 | -0.7 | -38.65 | -8.2 |  |  | DROP: below break-even |
| money_level | total | 252-244 | 50.8 | 49.3 | 1.5 | -14.93 | -3.0 |  |  | no edge shown yet |
| sharp_gap | moneyline | 138-252 | 35.4 | 40.1 | -4.7 | -49.15 | -12.6 |  |  | DROP: below break-even |
| sharp_gap | spread | 236-230 | 50.6 | 49.5 | 1.1 | -16.95 | -3.6 |  |  | no edge shown yet |
| sharp_gap | total | 241-248 | 49.3 | 50.9 | -1.6 | -27.79 | -5.7 |  |  | no edge shown yet |
| money_moving | moneyline | 142-246 | 36.6 | 40.8 | -4.2 | -43.82 | -11.3 |  |  | DROP: below break-even |
| money_moving | spread | 233-233 | 50.0 | 49.4 | 0.6 | -22.82 | -4.9 |  |  | no edge shown yet |
| money_moving | total | 237-255 | 48.2 | 50.8 | -2.6 | -38.46 | -7.8 |  |  | DROP: below break-even |
| pin_value | moneyline | 13-44 | 22.8 | 28.3 | -5.5 | -2.9 | -5.1 |  |  | DROP: below break-even |
| pin_value | spread | 124-109 | 53.2 | 49.6 | 3.6 | -0.24 | -0.1 |  |  | no edge shown yet |
| pin_value | total | 127-120 | 51.4 | 49.2 | 2.2 | -5.73 | -2.3 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.9 | 47.1 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 103-224 | 31.5 | 43.7 | -12.2 | -65.15 | -19.9 |  |  | DROP: below break-even |
| consensus_gap | spread | 72-65 | 52.6 | 49.0 | 3.6 | -3.46 | -2.5 |  |  | no edge shown yet |
| consensus_gap | total | 80-91 | 46.8 | 47.8 | -1.0 | -20.01 | -11.7 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 95-60 | 61.3 | 63.0 | -1.7 | -7.33 | -4.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 91-59 | 60.7 | 62.6 | -1.9 | -6.83 | -4.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 128-236 | 35.2 | 39.7 | -4.6 | -42.29 | -11.6 |  |  | DROP: below break-even |
| consensus_gap+money_level | moneyline | 70-50 | 58.3 | 69.0 | -10.7 | -11.95 | -10.0 |  |  | no edge shown yet |
| consensus_gap+money_moving | moneyline | 36-128 | 22.0 | 37.6 | -15.6 | -16.8 | -10.2 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+sharp_gap | moneyline | 37-133 | 21.8 | 36.9 | -15.1 | -18.65 | -11.0 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_rlm | moneyline | 10-22 | 31.2 | 28.8 | 2.5 | +15.65 | 48.9 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 26-52 | 33.3 | 27.6 | 5.7 | +12.98 | 16.6 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 26-53 | 32.9 | 27.6 | 5.3 | +11.98 | 15.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 12-38 | 24.0 | 28.7 | -4.7 | +1.58 | 3.2 |  |  | DROP: below break-even |
| money_moving+pin_value | moneyline | 7-28 | 20.0 | 25.8 | -5.8 | +5.27 | 15.1 |  |  | DROP: below break-even |
| pin_rlm+pin_value | moneyline | 5-8 | 38.5 | 25.8 | 12.7 | +14.07 | 108.2 |  |  | keep collecting (13/30) |
| pin_value+sharp_gap | moneyline | 7-28 | 20.0 | 25.8 | -5.8 | +5.27 | 15.1 |  |  | DROP: below break-even |
| money_level+pin_rlm | moneyline | 8-7 | 53.3 | 32.2 | 21.1 | +2.35 | 15.6 |  |  | keep collecting (15/30) |
| money_level+pin_value | moneyline | 3-1 | 75.0 | 62.1 | 12.9 | +0.31 | 7.8 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 31-24 | 56.4 | 48.1 | 8.3 | +2.4 | 4.4 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 39-35 | 52.7 | 48.8 | 3.9 | -1.68 | -2.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 49-40 | 55.1 | 48.9 | 6.1 | +1.7 | 1.9 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.33 | -38.9 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | spread | 38-35 | 52.1 | 49.1 | 3.0 | -2.58 | -3.5 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 121-125 | 49.2 | 48.9 | 0.3 | -16.18 | -6.6 |  |  | no edge shown yet |
| follow_move+pin_rlm | spread | 15-15 | 50.0 | 51.0 | -1.0 | -1.37 | -4.6 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 48-39 | 55.2 | 48.7 | 6.5 | +2.87 | 3.3 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 33-34 | 49.3 | 50.0 | -0.8 | -3.97 | -5.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 122-124 | 49.6 | 48.9 | 0.7 | -14.04 | -5.7 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 15-16 | 48.4 | 51.0 | -2.6 | -2.44 | -7.9 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 58-56 | 50.9 | 49.1 | 1.8 | -5.77 | -5.1 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 31-33 | 48.4 | 49.9 | -1.5 | -4.9 | -7.7 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 228-225 | 50.3 | 49.5 | 0.9 | -19.32 | -4.3 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 6-7 | 46.2 | 50.2 | -4.1 | -1.79 | -13.8 |  |  | keep collecting (13/30) |
| pin_rlm+rlm_ratio | spread | 15-15 | 50.0 | 51.0 | -1.0 | -1.37 | -4.6 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 17-16 | 51.5 | 51.1 | 0.4 | -0.62 | -1.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 5-6 | 45.5 | 49.2 | -3.8 | -1.72 | -15.6 |  |  | keep collecting (11/30) |
| pin_value+sharp_gap | spread | 58-56 | 50.9 | 49.2 | 1.6 | -5.84 | -5.1 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 33-34 | 49.3 | 50.0 | -0.8 | -3.97 | -5.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 116-124 | 48.3 | 48.5 | -0.2 | -19.73 | -8.2 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 17-19 | 47.2 | 49.5 | -2.3 | -3.71 | -10.3 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 177-178 | 49.9 | 49.1 | 0.8 | -18.68 | -5.3 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 48-40 | 54.5 | 48.6 | 6.0 | +1.17 | 1.3 |  |  | no edge shown yet |
| money_level+money_moving | spread | 176-179 | 49.6 | 49.0 | 0.6 | -20.6 | -5.8 |  |  | no edge shown yet |
| money_level+pin_value | spread | 62-64 | 49.2 | 48.8 | 0.4 | -10.37 | -8.2 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 8-6 | 57.1 | 50.4 | 6.7 | +1.1 | 7.9 |  |  | keep collecting (14/30) |
| money_level+money_moving | total | 160-166 | 49.1 | 50.1 | -1.0 | -20.22 | -6.2 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 163-164 | 49.8 | 50.1 | -0.3 | -15.46 | -4.7 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 235-246 | 48.9 | 50.9 | -2.0 | -31.28 | -6.5 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 38-49 | 43.7 | 46.8 | -3.1 | -15.34 | -17.6 |  |  | DROP: below break-even |
| consensus_gap+pin_value | total | 43-52 | 45.3 | 47.6 | -2.3 | -13.91 | -14.6 |  |  | no edge shown yet |
| follow_move+money_moving | total | 151-168 | 47.3 | 50.6 | -3.2 | -30.31 | -9.5 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 154-165 | 48.3 | 50.6 | -2.3 | -24.59 | -7.7 |  |  | no edge shown yet |
| money_level+pin_value | total | 58-59 | 49.6 | 48.1 | 1.4 | -7.09 | -6.1 |  |  | no edge shown yet |
| follow_move+money_level | total | 129-135 | 48.9 | 49.4 | -0.5 | -17.68 | -6.7 |  |  | no edge shown yet |
| follow_move+pin_value | total | 48-45 | 51.6 | 49.2 | 2.5 | -1.87 | -2.0 |  |  | no edge shown yet |
| money_moving+pin_value | total | 48-53 | 47.5 | 50.0 | -2.4 | -9.81 | -9.7 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 50-52 | 49.0 | 50.1 | -1.1 | -6.99 | -6.9 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 34-43 | 44.2 | 47.8 | -3.6 | -12.97 | -16.8 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 35-42 | 45.5 | 47.9 | -2.5 | -11.06 | -14.4 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 30-32 | 48.4 | 47.1 | 1.3 | -5.55 | -9.0 |  |  | no edge shown yet |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pin_rlm | total | 5-7 | 41.7 | 48.6 | -7.0 | -2.6 | -21.7 |  |  | keep collecting (12/30) |
| consensus_gap+rlm_ratio | total | 13-8 | 61.9 | 47.8 | 14.1 | +3.44 | 16.4 |  |  | keep collecting (21/30) |
| follow_move+pin_rlm | total | 50-31 | 61.7 | 52.6 | 9.1 | +15.1 | 18.6 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+rlm_ratio | total | 90-63 | 58.8 | 52.2 | 6.6 | +19.41 | 12.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 31-18 | 63.3 | 52.8 | 10.5 | +10.54 | 21.5 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 51-35 | 59.3 | 51.9 | 7.4 | +11.65 | 13.5 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 56-37 | 60.2 | 52.7 | 7.5 | +14.45 | 15.5 |  |  | PROMOTE: beats break-even and its own base rate |
| money_moving+rlm_ratio | total | 89-63 | 58.6 | 52.2 | 6.3 | +18.5 | 12.2 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_rlm+pin_value | total | 17-11 | 60.7 | 51.8 | 8.9 | +4.46 | 15.9 |  |  | keep collecting (28/30) |
| pin_rlm+rlm_ratio | total | 50-31 | 61.7 | 52.6 | 9.1 | +15.1 | 18.6 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_rlm+sharp_gap | total | 57-37 | 60.6 | 52.7 | 7.9 | +15.36 | 16.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 22-13 | 62.9 | 51.1 | 11.8 | +6.89 | 19.7 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 90-63 | 58.8 | 52.2 | 6.6 | +19.41 | 12.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 54.1 | 45.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_rlm | close | 1-3k bets | 59-64 | 48.0 | 4.4 | 15.1 |  |
| pin_rlm | close | 3k+ bets | 20-22 | 47.6 | 6.5 | 6.1 |  |
| pin_rlm | close | <1k bets | 21-20 | 51.2 | 8.9 | 13.7 |  |
| pin_rlm | close | pin $1-2k | 44-41 | 51.8 | 7.2 | 20.4 |  |
| pin_rlm | close | pin $2k+ | 21-49 | 30.0 | -4.3 | -22.4 |  |
| pin_rlm | close | pin limit <$1k | 35-16 | 68.6 | 16.9 | 49.1 |  |
| follow_move | close | 1-3k bets | 264-259 | 50.5 | 0.9 | -3.7 |  |
| follow_move | close | 3k+ bets | 87-92 | 48.6 | -0.8 | -7.4 |  |
| follow_move | close | <1k bets | 60-72 | 45.5 | -4.3 | -13.1 |  |
| follow_move | close | pin $1-2k | 136-168 | 44.7 | -4.5 | -14.6 |  |
| follow_move | close | pin $2k+ | 75-77 | 49.3 | -0.2 | -5.9 |  |
| follow_move | close | pin limit <$1k | 87-77 | 53.0 | 2.6 | 1.5 |  |
| rlm_ratio | close | 1-3k bets | 78-67 | 53.8 | 2.1 | 2.9 |  |
| rlm_ratio | close | 3k+ bets | 26-17 | 60.5 | 9.6 | 15.6 |  |
| rlm_ratio | close | <1k bets | 19-13 | 59.4 | 7.3 | 14.4 |  |
| rlm_ratio | close | pin $1-2k | 43-36 | 54.4 | 3.5 | 4.0 |  |
| rlm_ratio | close | pin $2k+ | 13-16 | 44.8 | -6.1 | -14.9 |  |
| rlm_ratio | close | pin limit <$1k | 36-20 | 64.3 | 11.5 | 23.7 |  |
| money_level | close | 1-3k bets | 502-345 | 59.3 | 3.8 | -0.5 |  |
| money_level | close | 3k+ bets | 161-141 | 53.3 | -2.0 | -9.1 |  |
| money_level | close | <1k bets | 128-113 | 53.1 | -2.7 | -14.3 |  |
| money_level | close | pin $1-2k | 232-207 | 52.8 | -0.9 | -6.3 |  |
| money_level | close | pin $2k+ | 193-154 | 55.6 | -2.0 | -9.6 |  |
| money_level | close | pin limit <$1k | 94-95 | 49.7 | 0.3 | -5.4 |  |
| sharp_gap | close | 1-3k bets | 365-450 | 44.8 | -2.4 | -9.5 |  |
| sharp_gap | close | 3k+ bets | 144-153 | 48.5 | 1.9 | 5.5 |  |
| sharp_gap | close | <1k bets | 106-126 | 45.7 | -2.7 | -13.7 |  |
| sharp_gap | close | pin $1-2k | 208-220 | 48.6 | -0.2 | -2.5 |  |
| sharp_gap | close | pin $2k+ | 146-189 | 43.6 | -2.1 | -10.8 |  |
| sharp_gap | close | pin limit <$1k | 91-91 | 50.0 | -0.9 | 0.9 |  |
| money_moving | close | 1-3k bets | 365-451 | 44.7 | -2.8 | -10.3 |  |
| money_moving | close | 3k+ bets | 143-156 | 47.8 | 0.8 | 3.0 |  |
| money_moving | close | <1k bets | 104-126 | 45.2 | -2.7 | -12.5 |  |
| money_moving | close | pin $1-2k | 203-226 | 47.3 | -1.2 | -4.2 |  |
| money_moving | close | pin $2k+ | 148-186 | 44.3 | -1.3 | -9.5 |  |
| money_moving | close | pin limit <$1k | 89-95 | 48.4 | -2.3 | -2.2 |  |
| pin_value | close | 1-3k bets | 160-168 | 48.8 | 1.4 | -2.7 |  |
| pin_value | close | 3k+ bets | 55-61 | 47.4 | 0.2 | -5.2 |  |
| pin_value | close | <1k bets | 49-44 | 52.7 | 6.5 | 6.4 |  |
| pin_value | close | pin $1-2k | 124-137 | 47.5 | -0.3 | -6.8 |  |
| pin_value | close | pin $2k+ | 73-81 | 47.4 | 2.3 | -0.3 |  |
| pin_value | close | pin limit <$1k | 67-55 | 54.9 | 6.6 | 7.7 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.1 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.1 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 158-230 | 40.7 | -5.6 | -15.7 |  |
| consensus_gap | close | 3k+ bets | 60-78 | 43.5 | -3.2 | 3.0 |  |
| consensus_gap | close | <1k bets | 37-71 | 34.3 | -9.3 | -28.7 |  |
| consensus_gap | close | pin $1-2k | 81-104 | 43.8 | -3.9 | -5.0 |  |
| consensus_gap | close | pin $2k+ | 65-82 | 44.2 | -5.2 | -13.2 |  |
| consensus_gap | close | pin limit <$1k | 39-39 | 50.0 | 2.0 | -1.1 |  |
| consensus_gap+follow_move | close | 1-3k bets | 43-34 | 55.8 | 8.3 | 4.4 |  |
| consensus_gap+money_level | close | 1-3k bets | 107-78 | 57.8 | 1.1 | 1.6 |  |
| consensus_gap+money_moving | close | 1-3k bets | 69-126 | 35.4 | -7.7 | -12.8 |  |
| consensus_gap+pin_value | close | 1-3k bets | 64-86 | 42.7 | -1.9 | -9.2 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 69-129 | 34.8 | -7.7 | -13.9 |  |
| follow_move+money_level | close | 1-3k bets | 167-163 | 50.6 | 1.6 | -3.6 |  |
| follow_move+money_moving | close | 1-3k bets | 183-191 | 48.9 | -1.0 | -6.7 |  |
| follow_move+pin_value | close | 1-3k bets | 57-50 | 53.3 | 4.4 | 0.4 |  |
| follow_move+sharp_gap | close | 1-3k bets | 183-188 | 49.3 | -0.6 | -5.9 |  |
| money_level+money_moving | close | 1-3k bets | 268-240 | 52.8 | 0.7 | -2.3 |  |
| money_level+pin_value | close | 1-3k bets | 80-74 | 51.9 | 3.2 | -2.5 |  |
| money_level+sharp_gap | close | 1-3k bets | 266-239 | 52.7 | 0.9 | -1.7 |  |
| money_moving+pin_value | close | 1-3k bets | 72-87 | 45.3 | -1.3 | -5.9 |  |
| money_moving+sharp_gap | close | 1-3k bets | 353-436 | 44.7 | -2.5 | -9.5 |  |
| pin_value+sharp_gap | close | 1-3k bets | 74-89 | 45.4 | -1.3 | -6.0 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 12-20 | 37.5 | 0.7 | 30.6 |  |
| money_level+pin_rlm | close | 1-3k bets | 30-19 | 61.2 | 10.2 | 17.7 |  |
| pin_rlm+pin_value | close | 1-3k bets | 18-17 | 51.4 | 6.1 | 38.3 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 59-64 | 48.0 | 4.4 | 15.1 |  |
| money_moving+pin_rlm | close | 1-3k bets | 57-63 | 47.5 | 3.9 | 14.8 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 13-7 | 65.0 | 16.6 | 21.6 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 78-67 | 53.8 | 2.1 | 2.9 |  |
| money_level+rlm_ratio | close | 1-3k bets | 43-37 | 53.8 | 2.4 | 2.7 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 77-67 | 53.5 | 1.8 | 2.2 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 78-67 | 53.8 | 2.1 | 2.9 |  |
| follow_move+pin_rlm | close | 1-3k bets | 38-30 | 55.9 | 3.6 | 7.1 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 38-30 | 55.9 | 3.6 | 7.1 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 18-13 | 58.1 | 7.5 | 10.0 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 45.9 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 15-13 | 53.6 | 6.2 | -0.2 |  |
| consensus_gap+money_moving | close | 3k+ bets | 25-44 | 36.2 | -6.5 | 14.7 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-5 | 37.5 | -2.7 | 19.3 |  |
| consensus_gap+pin_value | close | 3k+ bets | 28-30 | 48.3 | 3.9 | 1.1 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 2-3 | 40.0 | -7.3 | -24.4 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 26-44 | 37.1 | -5.6 | 18.5 |  |
| follow_move+money_moving | close | 3k+ bets | 56-58 | 49.1 | -0.2 | -6.7 |  |
| follow_move+pin_rlm | close | 3k+ bets | 14-10 | 58.3 | 6.8 | 12.4 |  |
| follow_move+pin_value | close | 3k+ bets | 23-23 | 50.0 | 1.1 | -6.2 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 26-17 | 60.5 | 9.6 | 15.6 |  |
| follow_move+sharp_gap | close | 3k+ bets | 60-57 | 51.3 | 1.9 | -2.4 |  |
| money_moving+pin_rlm | close | 3k+ bets | 19-22 | 46.3 | 5.5 | 3.9 |  |
| money_moving+pin_value | close | 3k+ bets | 26-34 | 43.3 | -2.0 | -6.8 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 24-16 | 60.0 | 9.3 | 14.4 |  |
| money_moving+sharp_gap | close | 3k+ bets | 136-146 | 48.2 | 1.6 | 5.0 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-6 | 45.5 | -0.9 | -13.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 14-10 | 58.3 | 6.8 | 12.4 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 20-22 | 47.6 | 6.5 | 6.1 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 6-5 | 54.5 | 4.4 | 2.8 |  |
| pin_value+sharp_gap | close | 3k+ bets | 26-32 | 44.8 | -0.6 | -3.5 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 26-17 | 60.5 | 9.6 | 15.6 |  |
| money_level+money_moving | close | 3k+ bets | 93-89 | 51.1 | -0.6 | -6.3 |  |
| money_level+sharp_gap | close | 3k+ bets | 92-86 | 51.7 | 0.3 | -4.2 |  |
| follow_move+money_level | close | 3k+ bets | 51-53 | 49.0 | 0.5 | -6.9 |  |
| money_level+rlm_ratio | close | 3k+ bets | 15-8 | 65.2 | 15.1 | 23.7 |  |
| consensus_gap+money_level | close | 3k+ bets | 33-35 | 48.5 | -7.3 | -17.0 |  |
| money_level+pin_value | close | 3k+ bets | 26-33 | 44.1 | -4.2 | -18.7 |  |
| money_level+pin_rlm | close | 3k+ bets | 8-6 | 57.1 | 13.2 | 17.5 |  |
| money_level+money_moving | close | <1k bets | 70-75 | 48.3 | -4.4 | -16.7 |  |
| money_level+sharp_gap | close | <1k bets | 73-75 | 49.3 | -3.9 | -16.1 |  |
| money_moving+sharp_gap | close | <1k bets | 102-124 | 45.1 | -3.0 | -13.7 |  |
| consensus_gap+money_level | close | <1k bets | 16-26 | 38.1 | -17.6 | -41.8 |  |
| consensus_gap+money_moving | close | <1k bets | 15-36 | 29.4 | -11.8 | -32.8 |  |
| consensus_gap+pin_value | close | <1k bets | 12-14 | 46.2 | 5.7 | 9.9 |  |
| consensus_gap+sharp_gap | close | <1k bets | 15-37 | 28.8 | -12.0 | -34.1 |  |
| money_level+pin_value | close | <1k bets | 17-17 | 50.0 | 0.7 | -6.7 |  |
| money_moving+pin_value | close | <1k bets | 15-16 | 48.4 | 3.0 | 10.3 |  |
| pin_value+sharp_gap | close | <1k bets | 15-15 | 50.0 | 3.9 | 13.9 |  |
| follow_move+money_moving | close | <1k bets | 33-44 | 42.9 | -7.3 | -17.8 |  |
| follow_move+sharp_gap | close | <1k bets | 33-44 | 42.9 | -7.4 | -17.8 |  |
| follow_move+money_level | close | <1k bets | 27-43 | 38.6 | -10.9 | -26.2 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -0.6 | 12.2 |  |
| money_moving+pin_rlm | close | <1k bets | 21-20 | 51.2 | 8.9 | 13.7 |  |
| pin_rlm+sharp_gap | close | <1k bets | 21-20 | 51.2 | 8.9 | 13.7 |  |
| consensus_gap+follow_move | close | <1k bets | 3-9 | 25.0 | -23.0 | -54.1 |  |
| follow_move+pin_rlm | close | <1k bets | 13-6 | 68.4 | 15.9 | 31.3 |  |
| follow_move+pin_value | close | <1k bets | 16-11 | 59.3 | 10.1 | 12.6 |  |
| follow_move+rlm_ratio | close | <1k bets | 19-13 | 59.4 | 7.3 | 14.4 |  |
| money_moving+rlm_ratio | close | <1k bets | 19-13 | 59.4 | 7.3 | 14.4 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 19.9 | 60.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 13-6 | 68.4 | 15.9 | 31.3 |  |
| pin_value+rlm_ratio | close | <1k bets | 3-1 | 75.0 | 22.6 | 43.9 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 19-13 | 59.4 | 7.3 | 14.4 |  |
| money_level+rlm_ratio | close | <1k bets | 10-9 | 52.6 | 0.4 | 1.6 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 15.9 | 19.0 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 23-24 | 48.9 | 1.3 | -8.6 |  |
| consensus_gap+money_moving | close | pin $1-2k | 42-57 | 42.4 | -4.5 | -5.4 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 11-16 | 40.7 | 0.9 | 30.3 |  |
| consensus_gap+pin_value | close | pin $1-2k | 48-62 | 43.6 | -0.8 | -10.5 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 9-7 | 56.2 | 8.2 | 5.1 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 42-54 | 43.8 | -2.5 | -2.4 |  |
| follow_move+money_moving | close | pin $1-2k | 94-117 | 44.5 | -4.9 | -15.1 |  |
| follow_move+pin_rlm | close | pin $1-2k | 30-21 | 58.8 | 6.9 | 12.8 |  |
| follow_move+pin_value | close | pin $1-2k | 44-48 | 47.8 | -1.3 | -9.9 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 43-36 | 54.4 | 3.5 | 4.0 |  |
| follow_move+sharp_gap | close | pin $1-2k | 96-116 | 45.3 | -4.3 | -13.7 |  |
| money_moving+pin_rlm | close | pin $1-2k | 42-40 | 51.2 | 6.6 | 20.2 |  |
| money_moving+pin_value | close | pin $1-2k | 49-67 | 42.2 | -4.9 | -16.0 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 42-35 | 54.5 | 3.7 | 4.1 |  |
| money_moving+sharp_gap | close | pin $1-2k | 199-216 | 48.0 | -0.6 | -3.4 |  |
| pin_rlm+pin_value | close | pin $1-2k | 10-16 | 38.5 | -9.6 | -16.2 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 30-21 | 58.8 | 6.9 | 12.8 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 44-41 | 51.8 | 7.2 | 20.4 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 13-13 | 50.0 | 0.1 | -6.0 |  |
| pin_value+sharp_gap | close | pin $1-2k | 49-65 | 43.0 | -4.2 | -14.5 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 43-36 | 54.4 | 3.5 | 4.0 |  |
| follow_move+money_level | close | pin $1-2k | 92-106 | 46.5 | -2.3 | -11.5 |  |
| money_level+rlm_ratio | close | pin $1-2k | 28-19 | 59.6 | 9.4 | 13.4 |  |
| money_level+sharp_gap | close | pin $1-2k | 154-148 | 51.0 | -0.5 | -5.1 |  |
| money_level+money_moving | close | pin $1-2k | 151-151 | 50.0 | -1.4 | -6.6 |  |
| consensus_gap+money_level | close | pin $1-2k | 46-49 | 48.4 | -6.9 | -13.9 |  |
| money_level+pin_value | close | pin $1-2k | 54-58 | 48.2 | -0.9 | -9.7 |  |
| money_level+pin_rlm | close | pin $1-2k | 23-15 | 60.5 | 13.0 | 19.8 |  |
| follow_move+money_level | close | pin $2k+ | 41-46 | 47.1 | -1.8 | -10.3 |  |
| follow_move+money_moving | close | pin $2k+ | 48-50 | 49.0 | -0.6 | -6.8 |  |
| follow_move+sharp_gap | close | pin $2k+ | 49-50 | 49.5 | -0.0 | -5.8 |  |
| money_level+money_moving | close | pin $2k+ | 96-96 | 50.0 | -2.5 | -9.2 |  |
| money_level+sharp_gap | close | pin $2k+ | 96-98 | 49.5 | -3.1 | -9.8 |  |
| money_moving+sharp_gap | close | pin $2k+ | 143-184 | 43.7 | -1.7 | -10.0 |  |
| consensus_gap+money_moving | close | pin $2k+ | 22-48 | 31.4 | -10.3 | -15.2 |  |
| consensus_gap+pin_value | close | pin $2k+ | 29-38 | 43.3 | 2.5 | 4.0 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 23-51 | 31.1 | -11.8 | -17.9 |  |
| money_moving+pin_value | close | pin $2k+ | 37-46 | 44.6 | 1.2 | 4.2 |  |
| pin_value+sharp_gap | close | pin $2k+ | 37-46 | 44.6 | 1.2 | 4.2 |  |
| consensus_gap+follow_move | close | pin $2k+ | 8-6 | 57.1 | 9.0 | 5.7 |  |
| follow_move+pin_value | close | pin $2k+ | 24-17 | 58.5 | 9.6 | 10.0 |  |
| follow_move+pin_rlm | close | pin $2k+ | 7-13 | 35.0 | -16.8 | -33.3 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 13-16 | 44.8 | -6.1 | -14.9 |  |
| money_level+pin_rlm | close | pin $2k+ | 7-8 | 46.7 | 3.9 | -8.2 |  |
| money_level+pin_value | close | pin $2k+ | 35-36 | 49.3 | 0.2 | -9.2 |  |
| money_level+rlm_ratio | close | pin $2k+ | 6-8 | 42.9 | -7.6 | -18.7 |  |
| money_moving+pin_rlm | close | pin $2k+ | 21-49 | 30.0 | -4.3 | -22.4 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 13-16 | 44.8 | -6.1 | -14.9 |  |
| pin_rlm+pin_value | close | pin $2k+ | 5-8 | 38.5 | 4.3 | 51.3 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 7-13 | 35.0 | -16.8 | -33.3 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 21-49 | 30.0 | -4.3 | -22.4 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 2-2 | 50.0 | -1.4 | -7.3 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 13-16 | 44.8 | -6.1 | -14.9 |  |
| consensus_gap+money_level | close | pin $2k+ | 45-34 | 57.0 | -5.1 | -11.8 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-14 | 22.2 | -6.6 | -3.9 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -52.9 | -100.0 |  |
| money_level+money_moving | close | pin limit <$1k | 52-57 | 47.7 | -2.3 | -8.3 |  |
| money_level+sharp_gap | close | pin limit <$1k | 54-57 | 48.6 | -1.6 | -6.5 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 85-86 | 49.7 | -1.2 | 0.7 |  |
| consensus_gap+money_level | close | pin limit <$1k | 21-22 | 48.8 | 0.8 | -9.8 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 27-30 | 47.4 | 0.1 | -3.2 |  |
| follow_move+money_moving | close | pin limit <$1k | 55-56 | 49.5 | -1.7 | -5.0 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 56-54 | 50.9 | -0.4 | -2.4 |  |
| money_level+pin_value | close | pin limit <$1k | 34-30 | 53.1 | 5.6 | 0.4 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 13-10 | 56.5 | 9.2 | 5.9 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 17-15 | 53.1 | 6.2 | 13.9 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 18-16 | 52.9 | 5.4 | 12.7 |  |
| follow_move+money_level | close | pin limit <$1k | 45-44 | 50.6 | 1.0 | -3.4 |  |
| follow_move+pin_value | close | pin limit <$1k | 28-19 | 59.6 | 11.0 | 12.8 |  |
| money_moving+pin_value | close | pin limit <$1k | 27-24 | 52.9 | 4.5 | 9.2 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 29-25 | 53.7 | 4.8 | 10.1 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 3-2 | 60.0 | 18.2 | 101.6 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 34-16 | 68.0 | 16.3 | 48.3 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 13-2 | 86.7 | 37.2 | 95.2 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 35-16 | 68.6 | 16.9 | 49.1 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 28-12 | 70.0 | 17.3 | 34.7 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 36-20 | 64.3 | 11.5 | 23.7 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 35-20 | 63.6 | 10.9 | 22.5 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 28-12 | 70.0 | 17.3 | 34.7 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 36-20 | 64.3 | 11.5 | 23.7 |  |
| money_level+pin_rlm | close | pin limit <$1k | 17-8 | 68.0 | 14.9 | 30.7 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 18-11 | 62.1 | 9.1 | 19.7 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 12-4 | 75.0 | 23.4 | 43.9 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 3-3 | 50.0 | 2.8 | -5.2 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 45.9 | 87.7 |  |
| pin_rlm | early | <1k bets | 1-1 | 50.0 | 24.2 | -3.7 | -2.15 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 15-16 | 48.4 | -0.8 | -7.7 | -0.1 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -49.4 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 147-164 | 47.3 | -2.0 | -9.4 | 0.18 |
| follow_move | early | pin $1-2k | 10-9 | 52.6 | 2.5 | -0.6 | 0.0 |
| follow_move | early | pin limit <$1k | 34-29 | 54.0 | 5.0 | 2.6 | -0.33 |
| rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 14.5 | 29.2 | -0.5 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.9 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 3-3 | 50.0 | -3.0 | -3.8 | 0.67 |
| rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -2.9 | -1.0 | -0.5 |
| rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 27.5 | 53.6 | -0.4 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | -0.1 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 41.5 | 59.7 | 0.33 |
| money_level | early | <1k bets | 89-54 | 62.2 | 3.2 | -3.3 | 0.28 |
| money_level | early | pin $1-2k | 15-8 | 65.2 | 0.8 | -2.7 | -0.03 |
| money_level | early | pin limit <$1k | 22-24 | 47.8 | -6.2 | -12.1 | 0.31 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 6.9 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 6.3 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 76-57 | 57.1 | 7.4 | 9.7 | 0.48 |
| sharp_gap | early | pin $1-2k | 12-9 | 57.1 | 4.4 | 13.4 | -0.59 |
| sharp_gap | early | pin limit <$1k | 27-16 | 62.8 | 13.9 | 30.8 | 0.2 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.1 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.4 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 46-37 | 55.4 | 3.6 | -1.4 | 0.2 |
| money_moving | early | pin $1-2k | 6-6 | 50.0 | -11.6 | -26.9 | 0.35 |
| money_moving | early | pin limit <$1k | 20-9 | 69.0 | 19.7 | 47.8 | 0.36 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.4 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.9 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 30-33 | 47.6 | 0.1 | -9.7 | 0.19 |
| pin_value | early | pin $1-2k | 11-14 | 44.0 | -0.2 | -16.7 | 0.17 |
| pin_value | early | pin limit <$1k | 32-28 | 53.3 | 4.0 | 0.8 | 0.13 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -45.9 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -28.2 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -10.8 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 13.6 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 123-173 | 41.6 | -5.4 | -18.3 | 0.3 |
| consensus_gap | early | pin $1-2k | 10-17 | 37.0 | -8.0 | -27.6 | 0.49 |
| consensus_gap | early | pin limit <$1k | 17-33 | 34.0 | -16.0 | -29.1 | 0.31 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 15.8 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 2.4 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 2.8 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.1 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 18.7 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 15.3 | 26.0 | -0.25 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 4.6 | -6.9 | 0.3 |
| consensus_gap+follow_move | early | 1-3k bets | 4-4 | 50.0 | 3.0 | -6.9 | 0.25 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.9 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.2 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 10-10 | 50.0 | 0.0 | -4.1 | 0.05 |
| follow_move+pin_value | early | 1-3k bets | 7-5 | 58.3 | 9.1 | 9.2 | -0.42 |
| follow_move+sharp_gap | early | 1-3k bets | 9-8 | 52.9 | 2.5 | 1.2 | -0.18 |
| follow_move+rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 14.5 | 29.2 | -0.5 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 26.6 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 4-2 | 66.7 | 14.5 | 29.2 | -0.5 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 18.1 | 56.1 | 0.15 |
| follow_move+money_moving | early | 1-3k bets | 9-4 | 69.2 | 19.8 | 32.1 | 0.08 |
| money_moving+rlm_ratio | early | 1-3k bets | 2-1 | 66.7 | 15.7 | 28.7 | -1.0 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.9 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.9 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.9 | 83.3 | 1.0 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.9 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.9 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.4 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.9 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.9 | 83.3 | 1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.9 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 35.8 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 45.9 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 11-12 | 47.8 | -0.8 | -10.0 | 1.43 |
| consensus_gap+money_level | early | <1k bets | 18-15 | 54.5 | -10.9 | -19.3 | 0.26 |
| consensus_gap+sharp_gap | early | <1k bets | 13-26 | 33.3 | -15.2 | -18.9 | 0.74 |
| follow_move+money_level | early | <1k bets | 17-13 | 56.7 | 9.2 | 7.9 | 0.83 |
| follow_move+sharp_gap | early | <1k bets | 17-9 | 65.4 | 16.3 | 24.8 | 1.04 |
| money_level+sharp_gap | early | <1k bets | 54-28 | 65.9 | 9.3 | 6.7 | 0.64 |
| money_level+money_moving | early | <1k bets | 30-21 | 58.8 | 1.5 | -5.8 | 0.1 |
| money_moving+sharp_gap | early | <1k bets | 30-21 | 58.8 | 8.1 | 5.8 | 0.52 |
| consensus_gap+money_moving | early | <1k bets | 8-14 | 36.4 | -12.0 | -41.6 | 0.15 |
| follow_move+pin_value | early | <1k bets | 11-10 | 52.4 | 3.6 | -1.5 | 0.29 |
| follow_move+money_moving | early | <1k bets | 9-8 | 52.9 | 4.3 | 1.5 | 0.59 |
| consensus_gap+pin_value | early | <1k bets | 11-22 | 33.3 | -12.1 | -37.3 | 0.45 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | <1k bets | 1-1 | 50.0 | 24.2 | -3.7 | -2.15 |
| pin_value+sharp_gap | early | <1k bets | 4-3 | 57.1 | 11.6 | 9.1 | 0.03 |
| money_level+pin_value | early | <1k bets | 3-3 | 50.0 | 1.4 | -4.5 | 1.33 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -53.5 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -54.1 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 0-2 | 0.0 | -49.4 | -100.0 | 2.5 |
| follow_move+rlm_ratio | early | <1k bets | 3-3 | 50.0 | -3.0 | -3.8 | 0.67 |
| money_level+rlm_ratio | early | <1k bets | 2-2 | 50.0 | -4.1 | -3.5 | 1.25 |
| money_moving+rlm_ratio | early | <1k bets | 2-2 | 50.0 | -2.4 | -3.5 | 0.5 |
| rlm_ratio+sharp_gap | early | <1k bets | 3-3 | 50.0 | -3.0 | -3.8 | 0.67 |
| consensus_gap+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -54.1 | -100.0 | 1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 45.9 | 90.9 | 1.0 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| consensus_gap+money_level | early | pin $1-2k | 4-4 | 50.0 | -14.1 | -22.9 | 0.44 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -31.9 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 4-9 | 30.8 | -8.6 | -42.5 | 0.4 |
| follow_move+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -2.9 | -1.0 | -0.5 |
| follow_move+sharp_gap | early | pin $1-2k | 3-1 | 75.0 | 25.0 | 45.0 | -0.25 |
| money_level+money_moving | early | pin $1-2k | 6-5 | 54.5 | -10.4 | -20.3 | 0.02 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.3 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 1-1 | 50.0 | -2.9 | -1.0 | -0.5 |
| money_level+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 6.2 | 8.3 | -0.45 |
| money_moving+sharp_gap | early | pin $1-2k | 3-5 | 37.5 | -21.2 | -45.3 | -0.06 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.6 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 2-2 | 50.0 | 0.0 | -8.4 | 0.75 |
| follow_move+money_level | early | pin $1-2k | 3-2 | 60.0 | 11.7 | 16.0 | 0.2 |
| follow_move+pin_value | early | pin $1-2k | 4-3 | 57.1 | 7.6 | 6.9 | 0.29 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 47.1 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 1-0 | 100.0 | 52.9 | 90.9 | 0.0 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -25.0 | -62.8 | -0.72 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| money_level+money_moving | early | pin limit <$1k | 11-7 | 61.1 | 7.9 | 12.1 | 0.53 |
| money_level+sharp_gap | early | pin limit <$1k | 18-14 | 56.2 | 4.8 | 2.3 | 0.25 |
| money_moving+sharp_gap | early | pin limit <$1k | 16-5 | 76.2 | 27.9 | 68.0 | 0.39 |
| money_level+pin_value | early | pin limit <$1k | 8-5 | 61.5 | 9.9 | 16.6 | 0.46 |
| money_moving+pin_value | early | pin limit <$1k | 6-4 | 60.0 | 9.9 | 13.0 | 0.3 |
| pin_value+sharp_gap | early | pin limit <$1k | 11-5 | 68.8 | 18.2 | 30.3 | 0.06 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-7 | 46.2 | -1.0 | -14.2 | 0.46 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -27.1 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 13-18 | 41.9 | -6.2 | -21.4 | 0.44 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.4 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 8-7 | 53.3 | 3.3 | 1.9 | 0.07 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 5.1 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 9-7 | 56.2 | 6.0 | 6.9 | -0.31 |
| follow_move+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 27.5 | 53.6 | -0.4 |
| money_level+rlm_ratio | early | pin limit <$1k | 4-0 | 100.0 | 45.9 | 92.0 | 0.25 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.3 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 4-1 | 80.0 | 27.5 | 53.6 | -0.4 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 23.4 | 72.3 | 0.54 |
| follow_move+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 20.4 | 33.3 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.3 | 28.7 | -1.0 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -54.1 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -54.1 | -100.0 | 1.0 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
