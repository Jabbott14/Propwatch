# CBB scorecard

Generated 2026-11-15 23:11 UTC. 489 graded games (27 finished games had no final score matched and are not graded).

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before tip. Break-even at -110 is 52.4%. CLV = points of closing-line
value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured
on this sample. `edge` is hit% minus that. A signal that is structurally long
favourites or overs beats 50% whenever those run, which is not an edge -- this
sample ran **46.9% favourites** (n=488) and **46.4% overs** (n=489) and **73.9% moneyline favourites** (n=414).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

## EARLY

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 1-1 | 50.0 | 26.1 | 23.9 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | both | 183-196 | 48.3 | 49.3 | -1.0 | -28.52 | -7.5 | 0.13 | 39.3 | DROP: below break-even |
| rlm_ratio | both | 7-4 | 63.6 | 52.1 | 11.5 | +2.52 | 22.9 | -0.36 | 18.2 | keep collecting (11/30) |
| money_level | both | 115-69 | 62.5 | 58.3 | 4.2 | -1.51 | -0.8 | 0.24 | 42.4 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 99-75 | 56.9 | 49.4 | 7.5 | +23.66 | 13.6 | 0.33 | 42.5 | no edge shown yet |
| money_moving | both | 70-43 | 61.9 | 51.4 | 10.6 | +16.37 | 14.5 | 0.12 | 42.5 | PROMOTE: beats break-even and its own base rate |
| pin_value | both | 43-41 | 51.2 | 47.8 | 3.3 | -2.68 | -3.2 | 0.15 | 41.7 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.8 | -31.8 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 152-212 | 41.8 | 46.8 | -5.1 | -58.95 | -16.2 | 0.28 | 45.9 | DROP: below break-even |
| consensus_gap+money_level | both | 23-22 | 51.1 | 63.0 | -11.9 | -10.62 | -23.6 | 0.25 | 46.7 | no edge shown yet |
| consensus_gap+money_moving | both | 15-16 | 48.4 | 47.7 | 0.7 | -0.69 | -2.2 | -0.04 | 38.7 | no edge shown yet |
| consensus_gap+pin_value | both | 17-26 | 39.5 | 45.5 | -6.0 | -11.16 | -26.0 | 0.46 | 53.5 | DROP: below break-even |
| follow_move+rlm_ratio | both | 7-4 | 63.6 | 52.1 | 11.5 | +2.52 | 22.9 | -0.36 | 18.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 26-16 | 61.9 | 49.4 | 12.5 | +7.63 | 18.2 | 0.45 | 38.1 | no edge shown yet |
| money_level+money_moving | both | 45-23 | 66.2 | 56.6 | 9.5 | +6.08 | 8.9 | 0.12 | 48.5 | PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | both | 10-8 | 55.6 | 50.5 | 5.1 | +0.9 | 5.0 | 0.5 | 50.0 | keep collecting (18/30) |
| money_moving+pin_value | both | 7-5 | 58.3 | 50.0 | 8.3 | +1.13 | 9.4 | 0.42 | 41.7 | keep collecting (12/30) |
| rlm_ratio+sharp_gap | both | 7-4 | 63.6 | 52.1 | 11.5 | +2.52 | 22.9 | -0.36 | 18.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 70-38 | 64.8 | 55.5 | 9.4 | +9.72 | 9.0 | 0.48 | 46.3 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 44-25 | 63.8 | 49.7 | 14.1 | +15.34 | 22.2 | 0.3 | 43.5 | PROMOTE: beats break-even and its own base rate |
| pin_value+sharp_gap | both | 12-7 | 63.2 | 49.1 | 14.0 | +3.75 | 19.8 | -0.15 | 36.8 | keep collecting (19/30) |
| consensus_gap+follow_move | both | 15-15 | 50.0 | 48.3 | 1.7 | -1.86 | -6.2 | 1.07 | 53.3 | no edge shown yet |
| consensus_gap+sharp_gap | both | 17-32 | 34.7 | 46.8 | -12.1 | -5.48 | -11.2 | 0.49 | 44.9 | DROP: below break-even |
| follow_move+money_level | both | 27-21 | 56.2 | 48.3 | 7.9 | +3.56 | 7.4 | 0.46 | 39.6 | no edge shown yet |
| follow_move+pin_value | both | 18-15 | 54.5 | 48.9 | 5.6 | +0.8 | 2.4 | 0.03 | 30.3 | no edge shown yet |
| money_level+rlm_ratio | both | 6-1 | 85.7 | 53.4 | 32.4 | +4.61 | 65.9 | 0.14 | 14.3 | keep collecting (7/30) |
| pin_value+rlm_ratio | both | 2-1 | 66.7 | 51.2 | 15.5 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| follow_move+money_moving | both | 18-10 | 64.3 | 48.6 | 15.7 | +6.43 | 23.0 | 0.25 | 39.3 | keep collecting (28/30) |
| money_moving+rlm_ratio | both | 4-1 | 80.0 | 50.7 | 29.3 | +2.72 | 54.4 | -1.0 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 26.1 | -26.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 26.1 | -26.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | both | 1-1 | 50.0 | 26.1 | 23.9 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 53.3 | -53.3 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 53.6 | -53.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 0-1 | 0.0 | 53.6 | -53.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 26.1 | 73.9 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-1 | 50.0 | 26.1 | 23.9 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | spread | 90-101 | 47.1 | 49.1 | -1.9 | -18.46 | -9.7 | -0.01 | 34.6 | no edge shown yet |
| follow_move | total | 93-95 | 49.5 | 49.5 | 0.0 | -10.06 | -5.4 | 0.28 | 44.1 | no edge shown yet |
| rlm_ratio | spread | 3-2 | 60.0 | 51.8 | 8.2 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 4-2 | 66.7 | 52.4 | 14.3 | +1.68 | 28.0 | -0.17 | 33.3 | keep collecting (6/30) |
| money_level | moneyline | 60-25 | 70.6 | 69.4 | 1.2 | -7.39 | -8.7 | 0.3 | 49.4 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 16-15 | 51.6 | 48.9 | 2.7 | -0.6 | -1.9 | 0.9 | 48.4 | no edge shown yet |
| money_level | total | 39-29 | 57.4 | 48.7 | 8.6 | +6.48 | 9.5 | -0.13 | 30.9 | no edge shown yet |
| sharp_gap | moneyline | 40-35 | 53.3 | 47.8 | 5.6 | +10.05 | 13.4 | 0.33 | 50.7 | no edge shown yet |
| sharp_gap | spread | 18-14 | 56.2 | 49.8 | 6.4 | +2.26 | 7.1 | 0.56 | 34.4 | no edge shown yet |
| sharp_gap | total | 41-26 | 61.2 | 50.9 | 10.3 | +11.36 | 16.9 | 0.22 | 37.3 | no edge shown yet |
| money_moving | moneyline | 26-22 | 54.2 | 54.0 | 0.2 | -2.41 | -5.0 | 0.13 | 56.2 | no edge shown yet |
| money_moving | spread | 17-4 | 81.0 | 49.0 | 32.0 | +11.27 | 53.7 | 0.14 | 38.1 | keep collecting (21/30) |
| money_moving | total | 27-17 | 61.4 | 49.7 | 11.7 | +7.51 | 17.1 | 0.09 | 29.5 | no edge shown yet |
| pin_value | moneyline | 1-5 | 16.7 | 26.1 | -9.4 | -4.02 | -67.0 | -0.02 | 66.7 | keep collecting (6/30) |
| pin_value | spread | 22-17 | 56.4 | 49.1 | 7.3 | +2.35 | 6.0 | 0.28 | 41.0 | no edge shown yet |
| pin_value | total | 20-19 | 51.3 | 49.9 | 1.4 | -1.01 | -2.6 | 0.05 | 38.5 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 53.1 | -19.7 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 62-115 | 35.0 | 44.2 | -9.2 | -41.61 | -23.5 | -0.06 | 42.4 | DROP: below break-even |
| consensus_gap | spread | 48-47 | 50.5 | 49.1 | 1.4 | -5.13 | -5.4 | 0.46 | 45.3 | no edge shown yet |
| consensus_gap | total | 42-50 | 45.7 | 49.5 | -3.8 | -12.21 | -13.3 | 0.74 | 53.3 | no edge shown yet |
| money_level+sharp_gap | moneyline | 31-11 | 73.8 | 64.8 | 9.0 | +1.33 | 3.2 | 0.6 | 61.9 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+pin_value | moneyline | 1-5 | 16.7 | 26.1 | -9.4 | -4.02 | -67.0 | -0.02 | 66.7 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_level+money_moving | moneyline | 17-8 | 68.0 | 70.1 | -2.1 | -4.47 | -17.9 | -0.03 | 60.0 | keep collecting (25/30) |
| consensus_gap+sharp_gap | moneyline | 11-23 | 32.4 | 45.8 | -13.4 | -1.71 | -5.0 | 0.36 | 47.1 | DROP: below break-even |
| consensus_gap+money_level | moneyline | 16-14 | 53.3 | 70.7 | -17.4 | -8.68 | -28.9 | -0.09 | 46.7 | INVERT candidate: wrong well beyond its base rate |
| money_moving+sharp_gap | moneyline | 15-12 | 55.6 | 49.1 | 6.4 | +2.07 | 7.7 | 0.44 | 63.0 | keep collecting (27/30) |
| consensus_gap+money_moving | moneyline | 7-15 | 31.8 | 47.8 | -16.0 | -6.63 | -30.1 | -0.01 | 50.0 | keep collecting (22/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 26.1 | -26.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 26.1 | -26.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | moneyline | 1-1 | 50.0 | 26.1 | 23.9 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 26.1 | -26.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 26.1 | 73.9 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 4-5 | 44.4 | 46.9 | -2.5 | -1.59 | -17.7 | 1.67 | 66.7 | keep collecting (9/30) |
| consensus_gap+money_moving | spread | 4-0 | 100.0 | 46.9 | 53.1 | +3.41 | 85.2 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_value | spread | 9-8 | 52.9 | 48.0 | 4.9 | -0.31 | -1.8 | 0.53 | 52.9 | keep collecting (17/30) |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.8 | 8.2 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 48.5 | 14.0 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 9-4 | 69.2 | 48.3 | 20.9 | +4.21 | 32.4 | 0.77 | 61.5 | keep collecting (13/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.7 | -5.8 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.4 | 10.6 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 51.8 | 8.2 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 13-11 | 54.2 | 49.0 | 5.2 | +0.71 | 3.0 | 0.96 | 41.7 | keep collecting (24/30) |
| money_moving+sharp_gap | spread | 9-3 | 75.0 | 49.0 | 26.0 | +5.13 | 42.7 | 0.42 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.0 | 17.7 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 8-8 | 50.0 | 47.7 | 2.3 | -1.18 | -7.4 | 0.94 | 43.8 | keep collecting (16/30) |
| consensus_gap+sharp_gap | spread | 3-3 | 50.0 | 46.9 | 3.1 | -0.43 | -7.1 | 2.17 | 66.7 | keep collecting (6/30) |
| follow_move+money_level | spread | 11-7 | 61.1 | 48.0 | 13.2 | +3.04 | 16.9 | 0.78 | 44.4 | keep collecting (18/30) |
| follow_move+pin_value | spread | 11-7 | 61.1 | 48.6 | 12.5 | +2.56 | 14.2 | 0.33 | 33.3 | keep collecting (18/30) |
| follow_move+money_moving | spread | 9-1 | 90.0 | 47.5 | 42.5 | +7.22 | 72.2 | 0.2 | 40.0 | keep collecting (10/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 53.1 | 13.6 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 53.1 | -53.1 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 19-11 | 63.3 | 49.0 | 14.3 | +6.34 | 21.1 | -0.03 | 33.3 | no edge shown yet |
| money_level+sharp_gap | total | 26-16 | 61.9 | 49.8 | 12.1 | +7.68 | 18.3 | 0.1 | 33.3 | no edge shown yet |
| money_moving+sharp_gap | total | 20-10 | 66.7 | 50.5 | 16.2 | +8.14 | 27.1 | 0.13 | 26.7 | PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | total | 7-4 | 63.6 | 51.6 | 12.0 | +2.32 | 21.1 | 0.36 | 36.4 | keep collecting (11/30) |
| money_moving+pin_value | total | 4-3 | 57.1 | 50.5 | 6.6 | +0.56 | 8.0 | 0.29 | 28.6 | keep collecting (7/30) |
| pin_value+sharp_gap | total | 10-5 | 66.7 | 50.7 | 16.0 | +4.01 | 26.7 | 0.0 | 33.3 | keep collecting (15/30) |
| follow_move+money_level | total | 16-14 | 53.3 | 48.6 | 4.8 | +0.53 | 1.8 | 0.27 | 36.7 | no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.3 | -2.6 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 4-2 | 66.7 | 52.4 | 14.3 | +1.68 | 28.0 | -0.17 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 16-10 | 61.5 | 50.0 | 11.5 | +4.55 | 17.5 | 0.35 | 38.5 | keep collecting (26/30) |
| money_level+rlm_ratio | total | 4-0 | 100.0 | 53.6 | 46.4 | +3.68 | 92.0 | 0.25 | 25.0 | keep collecting (4/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 51.2 | 15.5 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 4-2 | 66.7 | 52.4 | 14.3 | +1.68 | 28.0 | -0.17 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 9-9 | 50.0 | 49.2 | 0.8 | -0.8 | -4.4 | 0.28 | 38.9 | keep collecting (18/30) |
| consensus_gap+money_level | total | 3-3 | 50.0 | 48.8 | 1.2 | -0.34 | -5.7 | -0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 47.9 | 32.1 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-13 | 35.0 | 49.3 | -14.3 | -6.83 | -34.2 | 0.55 | 50.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | total | 3-6 | 33.3 | 50.4 | -17.1 | -3.35 | -37.2 | -0.11 | 22.2 | keep collecting (9/30) |
| money_moving+rlm_ratio | total | 2-1 | 66.7 | 51.2 | 15.5 | +0.86 | 28.7 | -1.0 | 0.0 | keep collecting (3/30) |
| consensus_gap+follow_move | total | 7-7 | 50.0 | 49.0 | 1.0 | -0.67 | -4.8 | 1.21 | 64.3 | keep collecting (14/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 53.6 | -53.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 53.6 | -53.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 0-1 | 0.0 | 53.6 | -53.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |

## CLOSE

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 98-103 | 48.8 | 42.9 | 5.8 | +27.82 | 13.8 |  |  | no edge shown yet |
| follow_move | both | 396-409 | 49.2 | 49.5 | -0.3 | -49.53 | -6.2 |  |  | DROP: below break-even |
| rlm_ratio | both | 120-93 | 56.3 | 51.3 | 5.0 | +16.7 | 7.8 |  |  | no edge shown yet |
| money_level | both | 766-576 | 57.1 | 55.4 | 1.7 | -59.33 | -4.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 595-704 | 45.8 | 47.4 | -1.5 | -87.12 | -6.7 |  |  | DROP: below break-even |
| money_moving | both | 591-709 | 45.5 | 47.5 | -2.0 | -99.91 | -7.7 |  |  | DROP: below break-even |
| pin_value | both | 256-263 | 49.3 | 47.3 | 2.0 | -6.09 | -1.2 |  |  | no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 51.0 | 15.6 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 253-369 | 40.7 | 46.1 | -5.4 | -79.41 | -12.8 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 61-56 | 52.1 | 47.7 | 4.5 | -3.15 | -2.7 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 109-202 | 35.0 | 43.1 | -8.0 | -27.46 | -8.8 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 18-31 | 36.7 | 36.5 | 0.2 | +13.56 | 27.7 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 104-127 | 45.0 | 44.4 | 0.6 | -7.63 | -3.3 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | both | 15-12 | 55.6 | 48.5 | 7.0 | +1.11 | 4.1 |  |  | keep collecting (27/30) |
| consensus_gap+sharp_gap | both | 110-206 | 34.8 | 42.7 | -7.9 | -28.29 | -9.0 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 261-283 | 48.0 | 49.7 | -1.7 | -46.66 | -8.6 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 63-46 | 57.8 | 51.9 | 5.9 | +11.83 | 10.9 |  |  | no edge shown yet |
| follow_move+pin_value | both | 93-84 | 52.5 | 48.9 | 3.7 | -1.69 | -1.0 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 120-93 | 56.3 | 51.3 | 5.0 | +16.7 | 7.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 265-279 | 48.7 | 49.7 | -1.0 | -38.8 | -7.1 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 95-102 | 48.2 | 42.9 | 5.4 | +26.09 | 13.2 |  |  | no edge shown yet |
| money_moving+pin_value | both | 109-133 | 45.0 | 46.2 | -1.1 | -9.91 | -4.1 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 117-92 | 56.0 | 51.3 | 4.7 | +14.86 | 7.1 |  |  | no edge shown yet |
| money_moving+sharp_gap | both | 571-682 | 45.6 | 47.3 | -1.8 | -87.13 | -7.0 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 28-26 | 51.9 | 45.1 | 6.8 | +16.74 | 31.0 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 63-46 | 57.8 | 51.9 | 5.9 | +11.83 | 10.9 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 98-103 | 48.8 | 42.9 | 5.8 | +27.82 | 13.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 26-19 | 57.8 | 50.6 | 7.2 | +4.35 | 9.7 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 111-132 | 45.7 | 46.3 | -0.6 | -7.16 | -2.9 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 120-93 | 56.3 | 51.3 | 5.0 | +16.7 | 7.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+money_moving | both | 415-389 | 51.6 | 52.0 | -0.4 | -44.89 | -5.6 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 416-385 | 51.9 | 51.9 | 0.0 | -37.13 | -4.6 |  |  | no edge shown yet |
| follow_move+money_level | both | 234-249 | 48.4 | 48.8 | -0.4 | -37.58 | -7.8 |  |  | DROP: below break-even |
| money_level+rlm_ratio | both | 65-50 | 56.5 | 50.9 | 5.6 | +9.2 | 8.0 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 156-134 | 53.8 | 56.4 | -2.6 | -21.12 | -7.3 |  |  | no edge shown yet |
| money_level+pin_value | both | 119-120 | 49.8 | 48.8 | 1.0 | -16.75 | -7.0 |  |  | no edge shown yet |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | both | 45-30 | 60.0 | 48.4 | 11.6 | +13.08 | 17.4 |  |  | no edge shown yet |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 53.6 | 46.4 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 26-50 | 34.2 | 28.0 | 6.2 | +14.98 | 19.7 |  |  | DROP: below break-even |
| pin_rlm | spread | 17-16 | 51.5 | 51.2 | 0.3 | -0.62 | -1.9 |  |  | no edge shown yet |
| pin_rlm | total | 55-37 | 59.8 | 52.3 | 7.4 | +13.46 | 14.6 |  |  | no edge shown yet |
| follow_move | spread | 182-186 | 49.5 | 49.0 | 0.5 | -21.7 | -5.9 |  |  | no edge shown yet |
| follow_move | total | 214-223 | 49.0 | 49.9 | -1.0 | -27.84 | -6.4 |  |  | no edge shown yet |
| rlm_ratio | spread | 32-32 | 50.0 | 50.0 | 0.0 | -2.8 | -4.4 |  |  | no edge shown yet |
| rlm_ratio | total | 88-61 | 59.1 | 51.9 | 7.2 | +19.51 | 13.1 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level | moneyline | 301-106 | 74.0 | 69.8 | 4.2 | -9.84 | -2.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 222-234 | 48.7 | 48.9 | -0.2 | -34.21 | -7.5 |  |  | DROP: below break-even |
| money_level | total | 243-236 | 50.7 | 49.3 | 1.4 | -15.28 | -3.2 |  |  | no edge shown yet |
| sharp_gap | moneyline | 133-241 | 35.6 | 40.5 | -5.0 | -43.43 | -11.6 |  |  | DROP: below break-even |
| sharp_gap | spread | 230-222 | 50.9 | 49.5 | 1.4 | -14.51 | -3.2 |  |  | no edge shown yet |
| sharp_gap | total | 232-241 | 49.0 | 50.7 | -1.7 | -29.19 | -6.2 |  |  | no edge shown yet |
| money_moving | moneyline | 136-236 | 36.6 | 41.1 | -4.6 | -39.68 | -10.7 |  |  | DROP: below break-even |
| money_moving | spread | 227-225 | 50.2 | 49.4 | 0.8 | -20.38 | -4.5 |  |  | no edge shown yet |
| money_moving | total | 228-248 | 47.9 | 50.6 | -2.7 | -39.86 | -8.4 |  |  | DROP: below break-even |
| pin_value | moneyline | 13-41 | 24.1 | 28.7 | -4.7 | +0.1 | 0.2 |  |  | DROP: below break-even |
| pin_value | spread | 120-106 | 53.1 | 49.6 | 3.5 | -0.73 | -0.3 |  |  | no edge shown yet |
| pin_value | total | 123-116 | 51.5 | 49.3 | 2.2 | -5.46 | -2.3 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 53.1 | 46.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 103-215 | 32.4 | 43.8 | -11.4 | -56.15 | -17.7 |  |  | DROP: below break-even |
| consensus_gap | spread | 72-63 | 53.3 | 48.9 | 4.4 | -1.46 | -1.1 |  |  | no edge shown yet |
| consensus_gap | total | 78-91 | 46.2 | 48.0 | -1.9 | -21.79 | -12.9 |  |  | DROP: below break-even |
| money_level+money_moving | moneyline | 92-57 | 61.7 | 63.3 | -1.6 | -5.02 | -3.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 89-56 | 61.4 | 63.0 | -1.6 | -3.94 | -2.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 123-226 | 35.2 | 40.2 | -5.0 | -37.57 | -10.8 |  |  | DROP: below break-even |
| consensus_gap+money_level | moneyline | 70-45 | 60.9 | 69.3 | -8.5 | -6.95 | -6.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 36-124 | 22.5 | 38.0 | -15.5 | -12.8 | -8.0 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+sharp_gap | moneyline | 37-129 | 22.3 | 37.3 | -15.0 | -14.65 | -8.8 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_rlm | moneyline | 10-21 | 32.3 | 29.2 | 3.1 | +16.65 | 53.7 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 26-49 | 34.7 | 28.0 | 6.7 | +15.98 | 21.3 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 26-50 | 34.2 | 28.0 | 6.2 | +14.98 | 19.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 12-36 | 25.0 | 29.1 | -4.1 | +3.58 | 7.5 |  |  | DROP: below break-even |
| money_moving+pin_value | moneyline | 7-27 | 20.6 | 26.1 | -5.5 | +6.27 | 18.4 |  |  | DROP: below break-even |
| pin_rlm+pin_value | moneyline | 5-8 | 38.5 | 26.1 | 12.4 | +14.07 | 108.2 |  |  | keep collecting (13/30) |
| pin_value+sharp_gap | moneyline | 7-27 | 20.6 | 26.1 | -5.5 | +6.27 | 18.4 |  |  | DROP: below break-even |
| money_level+pin_rlm | moneyline | 8-6 | 57.1 | 32.9 | 24.2 | +3.35 | 23.9 |  |  | keep collecting (14/30) |
| money_level+pin_value | moneyline | 3-1 | 75.0 | 62.0 | 13.0 | +0.31 | 7.8 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 31-24 | 56.4 | 47.9 | 8.4 | +2.4 | 4.4 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 39-35 | 52.7 | 48.8 | 3.9 | -1.68 | -2.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | -0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 49-39 | 55.7 | 48.9 | 6.8 | +2.7 | 3.1 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.33 | -38.9 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | spread | 38-35 | 52.1 | 49.0 | 3.0 | -2.58 | -3.5 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 117-121 | 49.2 | 48.7 | 0.4 | -15.85 | -6.7 |  |  | no edge shown yet |
| follow_move+pin_rlm | spread | 15-15 | 50.0 | 51.0 | -1.0 | -1.37 | -4.6 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 47-39 | 54.7 | 48.6 | 6.1 | +2.04 | 2.4 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 32-32 | 50.0 | 50.0 | 0.0 | -2.8 | -4.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 118-120 | 49.6 | 48.8 | 0.8 | -13.72 | -5.8 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 15-16 | 48.4 | 51.1 | -2.7 | -2.44 | -7.9 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 56-54 | 50.9 | 49.0 | 1.9 | -5.52 | -5.0 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 30-31 | 49.2 | 49.8 | -0.7 | -3.74 | -6.1 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 222-217 | 50.6 | 49.4 | 1.2 | -16.88 | -3.8 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 6-7 | 46.2 | 50.2 | -4.1 | -1.79 | -13.8 |  |  | keep collecting (13/30) |
| pin_rlm+rlm_ratio | spread | 15-15 | 50.0 | 51.0 | -1.0 | -1.37 | -4.6 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 17-16 | 51.5 | 51.2 | 0.3 | -0.62 | -1.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 4-6 | 40.0 | 49.4 | -9.4 | -2.55 | -25.5 |  |  | keep collecting (10/30) |
| pin_value+sharp_gap | spread | 56-54 | 50.9 | 49.2 | 1.7 | -5.58 | -5.1 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 32-32 | 50.0 | 50.0 | 0.0 | -2.8 | -4.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 112-119 | 48.5 | 48.3 | 0.2 | -18.4 | -8.0 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 16-17 | 48.5 | 49.3 | -0.9 | -2.54 | -7.7 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 172-171 | 50.1 | 49.0 | 1.2 | -16.29 | -4.7 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 48-40 | 54.5 | 48.5 | 6.1 | +1.17 | 1.3 |  |  | no edge shown yet |
| money_level+money_moving | spread | 171-172 | 49.9 | 48.9 | 0.9 | -18.21 | -5.3 |  |  | no edge shown yet |
| money_level+pin_value | spread | 60-62 | 49.2 | 48.7 | 0.4 | -10.11 | -8.3 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 8-6 | 57.1 | 50.4 | 6.7 | +1.1 | 7.9 |  |  | keep collecting (14/30) |
| money_level+money_moving | total | 152-160 | 48.7 | 50.0 | -1.3 | -21.66 | -6.9 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 155-158 | 49.5 | 50.0 | -0.5 | -16.9 | -5.4 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 226-239 | 48.6 | 50.7 | -2.1 | -32.67 | -7.0 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 38-49 | 43.7 | 47.2 | -3.6 | -15.34 | -17.6 |  |  | DROP: below break-even |
| consensus_gap+pin_value | total | 43-52 | 45.3 | 47.9 | -2.7 | -13.91 | -14.6 |  |  | no edge shown yet |
| follow_move+money_moving | total | 144-162 | 47.1 | 50.4 | -3.4 | -30.8 | -10.1 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 147-159 | 48.0 | 50.4 | -2.4 | -25.08 | -8.2 |  |  | DROP: below break-even |
| money_level+pin_value | total | 56-57 | 49.6 | 48.3 | 1.2 | -6.95 | -6.1 |  |  | no edge shown yet |
| follow_move+money_level | total | 122-130 | 48.4 | 49.3 | -0.9 | -19.17 | -7.6 |  |  | no edge shown yet |
| follow_move+pin_value | total | 46-45 | 50.5 | 49.2 | 1.4 | -3.73 | -4.1 |  |  | no edge shown yet |
| money_moving+pin_value | total | 46-52 | 46.9 | 49.9 | -3.0 | -10.67 | -10.9 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 48-51 | 48.5 | 50.0 | -1.6 | -7.85 | -7.9 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 34-43 | 44.2 | 48.1 | -3.9 | -12.97 | -16.8 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 35-42 | 45.5 | 48.2 | -2.7 | -11.06 | -14.4 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 30-32 | 48.4 | 47.5 | 0.9 | -5.55 | -9.0 |  |  | no edge shown yet |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pin_rlm | total | 5-7 | 41.7 | 48.8 | -7.1 | -2.6 | -21.7 |  |  | keep collecting (12/30) |
| consensus_gap+rlm_ratio | total | 13-8 | 61.9 | 48.1 | 13.8 | +3.44 | 16.4 |  |  | keep collecting (21/30) |
| follow_move+pin_rlm | total | 48-31 | 60.8 | 52.2 | 8.5 | +13.2 | 16.7 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 88-61 | 59.1 | 51.9 | 7.2 | +19.51 | 13.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 29-18 | 61.7 | 52.4 | 9.3 | +8.63 | 18.4 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 49-33 | 59.8 | 51.6 | 8.2 | +11.74 | 14.3 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 54-37 | 59.3 | 52.3 | 7.0 | +12.55 | 13.8 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 87-61 | 58.8 | 51.9 | 6.9 | +18.6 | 12.6 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_rlm+pin_value | total | 17-11 | 60.7 | 51.5 | 9.2 | +4.46 | 15.9 |  |  | keep collecting (28/30) |
| pin_rlm+rlm_ratio | total | 48-31 | 60.8 | 52.2 | 8.5 | +13.2 | 16.7 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 55-37 | 59.8 | 52.3 | 7.4 | +13.46 | 14.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 22-13 | 62.9 | 50.9 | 11.9 | +6.89 | 19.7 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 88-61 | 59.1 | 51.9 | 7.2 | +19.51 | 13.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 53.6 | 46.4 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_rlm | close | 1-3k bets | 57-63 | 47.5 | 4.0 | 14.7 |  |
| pin_rlm | close | 3k+ bets | 20-21 | 48.8 | 7.1 | 8.7 |  |
| pin_rlm | close | <1k bets | 21-19 | 52.5 | 9.9 | 16.5 |  |
| pin_rlm | close | pin $1-2k | 43-40 | 51.8 | 7.2 | 21.0 |  |
| pin_rlm | close | pin $2k+ | 21-47 | 30.9 | -3.9 | -20.2 |  |
| pin_rlm | close | pin limit <$1k | 34-16 | 68.0 | 16.7 | 48.2 |  |
| follow_move | close | 1-3k bets | 255-251 | 50.4 | 0.9 | -3.9 |  |
| follow_move | close | 3k+ bets | 83-92 | 47.4 | -1.9 | -9.6 |  |
| follow_move | close | <1k bets | 58-66 | 46.8 | -2.7 | -10.6 |  |
| follow_move | close | pin $1-2k | 129-166 | 43.7 | -5.5 | -16.6 |  |
| follow_move | close | pin $2k+ | 73-74 | 49.7 | 0.1 | -5.3 |  |
| follow_move | close | pin limit <$1k | 85-75 | 53.1 | 2.9 | 1.6 |  |
| rlm_ratio | close | 1-3k bets | 76-64 | 54.3 | 2.9 | 3.7 |  |
| rlm_ratio | close | 3k+ bets | 25-17 | 59.5 | 8.6 | 14.0 |  |
| rlm_ratio | close | <1k bets | 19-12 | 61.3 | 9.7 | 18.1 |  |
| rlm_ratio | close | pin $1-2k | 42-36 | 53.8 | 3.1 | 2.8 |  |
| rlm_ratio | close | pin $2k+ | 12-16 | 42.9 | -8.2 | -18.4 |  |
| rlm_ratio | close | pin limit <$1k | 35-20 | 63.6 | 11.2 | 22.4 |  |
| money_level | close | 1-3k bets | 487-332 | 59.5 | 4.1 | -0.2 |  |
| money_level | close | 3k+ bets | 156-137 | 53.2 | -1.9 | -9.2 |  |
| money_level | close | <1k bets | 123-106 | 53.7 | -2.1 | -13.2 |  |
| money_level | close | pin $1-2k | 226-197 | 53.4 | -0.3 | -5.3 |  |
| money_level | close | pin $2k+ | 186-150 | 55.4 | -2.0 | -9.7 |  |
| money_level | close | pin limit <$1k | 90-93 | 49.2 | -0.3 | -6.5 |  |
| sharp_gap | close | 1-3k bets | 353-435 | 44.8 | -2.5 | -9.3 |  |
| sharp_gap | close | 3k+ bets | 139-150 | 48.1 | 1.3 | 4.6 |  |
| sharp_gap | close | <1k bets | 103-118 | 46.6 | -1.9 | -11.7 |  |
| sharp_gap | close | pin $1-2k | 201-213 | 48.6 | -0.4 | -2.9 |  |
| sharp_gap | close | pin $2k+ | 141-184 | 43.4 | -2.4 | -11.0 |  |
| sharp_gap | close | pin limit <$1k | 88-88 | 50.0 | -0.7 | 1.0 |  |
| money_moving | close | 1-3k bets | 352-437 | 44.6 | -2.9 | -10.4 |  |
| money_moving | close | 3k+ bets | 138-153 | 47.4 | 0.2 | 2.0 |  |
| money_moving | close | <1k bets | 101-118 | 46.1 | -1.9 | -10.4 |  |
| money_moving | close | pin $1-2k | 196-219 | 47.2 | -1.4 | -4.7 |  |
| money_moving | close | pin $2k+ | 143-181 | 44.1 | -1.6 | -9.6 |  |
| money_moving | close | pin limit <$1k | 86-92 | 48.3 | -2.2 | -2.2 |  |
| pin_value | close | 1-3k bets | 157-161 | 49.4 | 1.8 | -1.4 |  |
| pin_value | close | 3k+ bets | 53-59 | 47.3 | 0.1 | -5.2 |  |
| pin_value | close | <1k bets | 46-43 | 51.7 | 5.3 | 4.8 |  |
| pin_value | close | pin $1-2k | 121-132 | 47.8 | -0.0 | -6.1 |  |
| pin_value | close | pin $2k+ | 70-78 | 47.3 | 1.9 | -0.1 |  |
| pin_value | close | pin limit <$1k | 65-53 | 55.1 | 6.6 | 8.1 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 46.9 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 46.9 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 158-226 | 41.1 | -5.4 | -14.8 |  |
| consensus_gap | close | 3k+ bets | 60-76 | 44.1 | -2.5 | 4.5 |  |
| consensus_gap | close | <1k bets | 35-66 | 34.7 | -9.0 | -27.5 |  |
| consensus_gap | close | pin $1-2k | 81-101 | 44.5 | -3.0 | -3.4 |  |
| consensus_gap | close | pin $2k+ | 65-78 | 45.5 | -4.2 | -10.8 |  |
| consensus_gap | close | pin limit <$1k | 39-39 | 50.0 | 1.7 | -1.1 |  |
| consensus_gap+follow_move | close | 1-3k bets | 43-34 | 55.8 | 8.2 | 4.4 |  |
| consensus_gap+money_level | close | 1-3k bets | 107-76 | 58.5 | 1.7 | 2.7 |  |
| consensus_gap+money_moving | close | 1-3k bets | 69-124 | 35.8 | -7.7 | -11.8 |  |
| consensus_gap+pin_value | close | 1-3k bets | 64-85 | 43.0 | -1.9 | -8.6 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 69-127 | 35.2 | -7.7 | -13.0 |  |
| follow_move+money_level | close | 1-3k bets | 159-155 | 50.6 | 1.8 | -3.6 |  |
| follow_move+money_moving | close | 1-3k bets | 175-184 | 48.7 | -1.0 | -7.1 |  |
| follow_move+pin_value | close | 1-3k bets | 56-50 | 52.8 | 4.0 | -0.4 |  |
| follow_move+sharp_gap | close | 1-3k bets | 175-181 | 49.2 | -0.6 | -6.3 |  |
| money_level+money_moving | close | 1-3k bets | 257-230 | 52.8 | 0.8 | -2.2 |  |
| money_level+pin_value | close | 1-3k bets | 78-71 | 52.3 | 3.6 | -1.8 |  |
| money_level+sharp_gap | close | 1-3k bets | 256-229 | 52.8 | 1.0 | -1.5 |  |
| money_moving+pin_value | close | 1-3k bets | 70-84 | 45.5 | -1.2 | -5.4 |  |
| money_moving+sharp_gap | close | 1-3k bets | 341-422 | 44.7 | -2.6 | -9.4 |  |
| pin_value+sharp_gap | close | 1-3k bets | 72-86 | 45.6 | -1.1 | -5.4 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 12-19 | 38.7 | 1.4 | 34.8 |  |
| money_level+pin_rlm | close | 1-3k bets | 28-19 | 59.6 | 9.0 | 14.4 |  |
| pin_rlm+pin_value | close | 1-3k bets | 18-17 | 51.4 | 6.2 | 38.3 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 57-63 | 47.5 | 4.0 | 14.7 |  |
| money_moving+pin_rlm | close | 1-3k bets | 55-62 | 47.0 | 3.5 | 14.4 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 13-7 | 65.0 | 16.4 | 21.6 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 76-64 | 54.3 | 2.9 | 3.7 |  |
| money_level+rlm_ratio | close | 1-3k bets | 41-34 | 54.7 | 3.7 | 4.4 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 75-64 | 54.0 | 2.6 | 3.1 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 76-64 | 54.3 | 2.9 | 3.7 |  |
| follow_move+pin_rlm | close | 1-3k bets | 36-30 | 54.5 | 2.6 | 4.4 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 36-30 | 54.5 | 2.6 | 4.4 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 18-13 | 58.1 | 7.7 | 10.0 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 46.4 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 15-13 | 53.6 | 6.0 | -0.2 |  |
| consensus_gap+money_moving | close | 3k+ bets | 25-44 | 36.2 | -6.7 | 14.7 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-5 | 37.5 | -3.0 | 19.3 |  |
| consensus_gap+pin_value | close | 3k+ bets | 28-29 | 49.1 | 4.6 | 2.9 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 2-3 | 40.0 | -7.8 | -24.4 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 26-44 | 37.1 | -5.7 | 18.5 |  |
| follow_move+money_moving | close | 3k+ bets | 53-58 | 47.7 | -1.5 | -9.3 |  |
| follow_move+pin_rlm | close | 3k+ bets | 14-10 | 58.3 | 6.8 | 12.4 |  |
| follow_move+pin_value | close | 3k+ bets | 21-23 | 47.7 | -1.1 | -10.5 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 25-17 | 59.5 | 8.6 | 14.0 |  |
| follow_move+sharp_gap | close | 3k+ bets | 57-57 | 50.0 | 0.6 | -4.9 |  |
| money_moving+pin_rlm | close | 3k+ bets | 19-21 | 47.5 | 6.1 | 6.5 |  |
| money_moving+pin_value | close | 3k+ bets | 25-33 | 43.1 | -2.3 | -6.7 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 23-16 | 59.0 | 8.2 | 12.6 |  |
| money_moving+sharp_gap | close | 3k+ bets | 131-143 | 47.8 | 1.0 | 4.0 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-6 | 45.5 | -1.0 | -13.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 14-10 | 58.3 | 6.8 | 12.4 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 20-21 | 48.8 | 7.1 | 8.7 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 5-5 | 50.0 | -0.6 | -5.2 |  |
| pin_value+sharp_gap | close | 3k+ bets | 25-31 | 44.6 | -0.8 | -3.3 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 25-17 | 59.5 | 8.6 | 14.0 |  |
| money_level+money_moving | close | 3k+ bets | 90-88 | 50.6 | -1.1 | -7.4 |  |
| money_level+sharp_gap | close | 3k+ bets | 89-85 | 51.1 | -0.3 | -5.3 |  |
| follow_move+money_level | close | 3k+ bets | 49-53 | 48.0 | -0.4 | -8.7 |  |
| money_level+rlm_ratio | close | 3k+ bets | 14-8 | 63.6 | 13.4 | 21.0 |  |
| consensus_gap+money_level | close | 3k+ bets | 33-34 | 49.3 | -6.3 | -15.8 |  |
| money_level+pin_value | close | 3k+ bets | 25-32 | 43.9 | -4.6 | -19.0 |  |
| money_level+pin_rlm | close | 3k+ bets | 8-6 | 57.1 | 13.1 | 17.5 |  |
| money_level+money_moving | close | <1k bets | 68-70 | 49.3 | -3.5 | -14.6 |  |
| money_level+sharp_gap | close | <1k bets | 71-70 | 50.4 | -2.9 | -14.0 |  |
| money_moving+sharp_gap | close | <1k bets | 99-116 | 46.0 | -2.2 | -11.7 |  |
| consensus_gap+money_level | close | <1k bets | 16-24 | 40.0 | -15.8 | -38.9 |  |
| consensus_gap+money_moving | close | <1k bets | 15-34 | 30.6 | -11.3 | -30.1 |  |
| consensus_gap+pin_value | close | <1k bets | 12-13 | 48.0 | 6.8 | 14.3 |  |
| consensus_gap+sharp_gap | close | <1k bets | 15-35 | 30.0 | -11.6 | -31.5 |  |
| money_level+pin_value | close | <1k bets | 16-17 | 48.5 | -0.8 | -9.8 |  |
| money_moving+pin_value | close | <1k bets | 14-16 | 46.7 | 1.6 | 7.4 |  |
| pin_value+sharp_gap | close | <1k bets | 14-15 | 48.3 | 2.5 | 11.1 |  |
| follow_move+money_moving | close | <1k bets | 33-41 | 44.6 | -5.3 | -14.5 |  |
| follow_move+sharp_gap | close | <1k bets | 33-41 | 44.6 | -5.3 | -14.5 |  |
| follow_move+money_level | close | <1k bets | 26-41 | 38.8 | -10.4 | -25.8 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -0.9 | 12.2 |  |
| money_moving+pin_rlm | close | <1k bets | 21-19 | 52.5 | 9.9 | 16.5 |  |
| pin_rlm+sharp_gap | close | <1k bets | 21-19 | 52.5 | 9.9 | 16.5 |  |
| consensus_gap+follow_move | close | <1k bets | 3-9 | 25.0 | -22.9 | -54.1 |  |
| follow_move+pin_rlm | close | <1k bets | 13-6 | 68.4 | 16.3 | 31.3 |  |
| follow_move+pin_value | close | <1k bets | 16-11 | 59.3 | 10.1 | 12.6 |  |
| follow_move+rlm_ratio | close | <1k bets | 19-12 | 61.3 | 9.7 | 18.1 |  |
| money_moving+rlm_ratio | close | <1k bets | 19-12 | 61.3 | 9.7 | 18.1 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 20.1 | 60.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 13-6 | 68.4 | 16.3 | 31.3 |  |
| pin_value+rlm_ratio | close | <1k bets | 3-1 | 75.0 | 23.1 | 43.9 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 19-12 | 61.3 | 9.7 | 18.1 |  |
| money_level+rlm_ratio | close | <1k bets | 10-8 | 55.6 | 3.9 | 7.2 |  |
| money_level+pin_rlm | close | <1k bets | 9-5 | 64.3 | 19.1 | 27.5 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 23-24 | 48.9 | 1.2 | -8.6 |  |
| consensus_gap+money_moving | close | pin $1-2k | 42-57 | 42.4 | -4.6 | -5.4 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 11-16 | 40.7 | 0.7 | 30.3 |  |
| consensus_gap+pin_value | close | pin $1-2k | 48-61 | 44.0 | -0.5 | -9.6 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 9-7 | 56.2 | 8.0 | 5.1 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 42-54 | 43.8 | -2.6 | -2.4 |  |
| follow_move+money_moving | close | pin $1-2k | 91-115 | 44.2 | -5.2 | -15.9 |  |
| follow_move+pin_rlm | close | pin $1-2k | 29-21 | 58.0 | 6.4 | 11.1 |  |
| follow_move+pin_value | close | pin $1-2k | 42-48 | 46.7 | -2.3 | -12.2 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 42-36 | 53.8 | 3.1 | 2.8 |  |
| follow_move+sharp_gap | close | pin $1-2k | 93-114 | 44.9 | -4.5 | -14.4 |  |
| money_moving+pin_rlm | close | pin $1-2k | 41-39 | 51.2 | 6.7 | 20.7 |  |
| money_moving+pin_value | close | pin $1-2k | 48-65 | 42.5 | -4.7 | -15.4 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 41-35 | 53.9 | 3.3 | 2.9 |  |
| money_moving+sharp_gap | close | pin $1-2k | 192-209 | 47.9 | -0.8 | -3.9 |  |
| pin_rlm+pin_value | close | pin $1-2k | 10-16 | 38.5 | -9.5 | -16.2 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 29-21 | 58.0 | 6.4 | 11.1 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 43-40 | 51.8 | 7.2 | 21.0 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 13-13 | 50.0 | 0.2 | -6.0 |  |
| pin_value+sharp_gap | close | pin $1-2k | 48-63 | 43.2 | -4.0 | -13.9 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 42-36 | 53.8 | 3.1 | 2.8 |  |
| follow_move+money_level | close | pin $1-2k | 88-104 | 45.8 | -2.9 | -12.8 |  |
| money_level+rlm_ratio | close | pin $1-2k | 27-19 | 58.7 | 8.8 | 11.6 |  |
| money_level+sharp_gap | close | pin $1-2k | 150-143 | 51.2 | -0.3 | -4.9 |  |
| money_level+money_moving | close | pin $1-2k | 147-146 | 50.2 | -1.2 | -6.4 |  |
| consensus_gap+money_level | close | pin $1-2k | 46-47 | 49.5 | -5.5 | -12.1 |  |
| money_level+pin_value | close | pin $1-2k | 53-56 | 48.6 | -0.5 | -9.0 |  |
| money_level+pin_rlm | close | pin $1-2k | 22-14 | 61.1 | 13.3 | 21.1 |  |
| follow_move+money_level | close | pin $2k+ | 39-44 | 47.0 | -1.8 | -10.5 |  |
| follow_move+money_moving | close | pin $2k+ | 46-49 | 48.4 | -1.1 | -7.9 |  |
| follow_move+sharp_gap | close | pin $2k+ | 47-49 | 49.0 | -0.6 | -6.8 |  |
| money_level+money_moving | close | pin $2k+ | 92-94 | 49.5 | -2.9 | -9.9 |  |
| money_level+sharp_gap | close | pin $2k+ | 92-96 | 48.9 | -3.6 | -10.6 |  |
| money_moving+sharp_gap | close | pin $2k+ | 138-179 | 43.5 | -2.1 | -10.1 |  |
| consensus_gap+money_moving | close | pin $2k+ | 22-47 | 31.9 | -10.2 | -13.9 |  |
| consensus_gap+pin_value | close | pin $2k+ | 29-36 | 44.6 | 3.3 | 7.3 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 23-50 | 31.5 | -11.6 | -16.8 |  |
| money_moving+pin_value | close | pin $2k+ | 35-45 | 43.8 | 0.4 | 3.5 |  |
| pin_value+sharp_gap | close | pin $2k+ | 35-45 | 43.8 | 0.4 | 3.5 |  |
| consensus_gap+follow_move | close | pin $2k+ | 8-6 | 57.1 | 9.0 | 5.7 |  |
| follow_move+pin_value | close | pin $2k+ | 23-17 | 57.5 | 8.6 | 8.2 |  |
| follow_move+pin_rlm | close | pin $2k+ | 7-13 | 35.0 | -16.9 | -33.3 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 12-16 | 42.9 | -8.2 | -18.4 |  |
| money_level+pin_rlm | close | pin $2k+ | 7-8 | 46.7 | 3.8 | -8.2 |  |
| money_level+pin_value | close | pin $2k+ | 33-35 | 48.5 | -0.6 | -10.7 |  |
| money_level+rlm_ratio | close | pin $2k+ | 5-8 | 38.5 | -12.2 | -26.5 |  |
| money_moving+pin_rlm | close | pin $2k+ | 21-47 | 30.9 | -3.9 | -20.2 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 12-16 | 42.9 | -8.2 | -18.4 |  |
| pin_rlm+pin_value | close | pin $2k+ | 5-8 | 38.5 | 4.0 | 51.3 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 7-13 | 35.0 | -16.9 | -33.3 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 21-47 | 30.9 | -3.9 | -20.2 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 1-2 | 33.3 | -19.7 | -37.4 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 12-16 | 42.9 | -8.2 | -18.4 |  |
| consensus_gap+money_level | close | pin $2k+ | 45-33 | 57.7 | -4.0 | -10.6 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-13 | 23.5 | -5.8 | 1.7 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -53.1 | -100.0 |  |
| money_level+money_moving | close | pin limit <$1k | 49-55 | 47.1 | -2.7 | -9.5 |  |
| money_level+sharp_gap | close | pin limit <$1k | 51-55 | 48.1 | -1.9 | -7.6 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 82-83 | 49.7 | -1.0 | 0.8 |  |
| consensus_gap+money_level | close | pin limit <$1k | 21-22 | 48.8 | 0.6 | -9.8 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 27-30 | 47.4 | -0.1 | -3.2 |  |
| follow_move+money_moving | close | pin limit <$1k | 53-54 | 49.5 | -1.4 | -5.1 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 54-52 | 50.9 | -0.1 | -2.4 |  |
| money_level+pin_value | close | pin limit <$1k | 33-29 | 53.2 | 5.5 | 0.5 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 13-10 | 56.5 | 9.0 | 5.9 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 17-15 | 53.1 | 5.9 | 13.9 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 18-16 | 52.9 | 5.2 | 12.7 |  |
| follow_move+money_level | close | pin limit <$1k | 43-43 | 50.0 | 0.6 | -4.5 |  |
| follow_move+pin_value | close | pin limit <$1k | 28-19 | 59.6 | 10.9 | 12.8 |  |
| money_moving+pin_value | close | pin limit <$1k | 26-23 | 53.1 | 4.5 | 9.7 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 28-24 | 53.8 | 4.9 | 10.6 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 3-2 | 60.0 | 17.6 | 101.6 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 33-16 | 67.3 | 16.1 | 47.3 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 13-2 | 86.7 | 37.3 | 95.2 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 34-16 | 68.0 | 16.7 | 48.2 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 27-12 | 69.2 | 16.9 | 33.2 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 35-20 | 63.6 | 11.2 | 22.4 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 34-20 | 63.0 | 10.6 | 21.1 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 27-12 | 69.2 | 16.9 | 33.2 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 35-20 | 63.6 | 11.2 | 22.4 |  |
| money_level+pin_rlm | close | pin limit <$1k | 16-8 | 66.7 | 14.0 | 28.0 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 17-11 | 60.7 | 8.2 | 17.0 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 12-4 | 75.0 | 23.7 | 43.9 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 3-3 | 50.0 | 2.4 | -5.2 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 46.4 | 87.7 |  |
| pin_rlm | early | <1k bets | 1-1 | 50.0 | 23.9 | -3.7 | -2.15 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.1 | -100.0 | -4.8 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.9 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 15-16 | 48.4 | -0.7 | -7.7 | -0.1 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -49.7 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 142-152 | 48.3 | -0.9 | -7.5 | 0.18 |
| follow_move | early | pin $1-2k | 10-8 | 55.6 | 5.6 | 5.0 | -0.06 |
| follow_move | early | pin limit <$1k | 33-29 | 53.2 | 4.3 | 1.1 | -0.35 |
| rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 14.5 | 29.2 | -0.5 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 3-1 | 75.0 | 23.1 | 44.2 | 0.0 |
| rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -3.1 | -1.0 | -0.5 |
| rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 27.9 | 53.6 | -0.4 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 0.1 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 41.9 | 59.7 | 0.33 |
| money_level | early | <1k bets | 86-49 | 63.7 | 4.7 | -0.1 | 0.3 |
| money_level | early | pin $1-2k | 14-8 | 63.6 | -0.1 | -3.2 | 0.01 |
| money_level | early | pin limit <$1k | 22-24 | 47.8 | -6.1 | -12.1 | 0.31 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 6.9 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 6.5 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 72-53 | 57.6 | 7.8 | 11.4 | 0.46 |
| sharp_gap | early | pin $1-2k | 11-9 | 55.0 | 3.3 | 13.8 | -0.57 |
| sharp_gap | early | pin limit <$1k | 27-16 | 62.8 | 14.0 | 30.8 | 0.2 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.1 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.7 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 46-32 | 59.0 | 6.8 | 4.9 | 0.09 |
| money_moving | early | pin $1-2k | 6-6 | 50.0 | -11.4 | -26.9 | 0.35 |
| money_moving | early | pin limit <$1k | 20-9 | 69.0 | 19.8 | 47.8 | 0.36 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.5 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 30-32 | 48.4 | 0.8 | -8.3 | 0.21 |
| pin_value | early | pin $1-2k | 11-14 | 44.0 | -0.2 | -16.7 | 0.17 |
| pin_value | early | pin limit <$1k | 32-27 | 54.2 | 4.9 | 2.5 | 0.15 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -46.4 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -28.2 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -10.7 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 13.5 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 120-165 | 42.1 | -5.0 | -16.9 | 0.26 |
| consensus_gap | early | pin $1-2k | 10-16 | 38.5 | -7.4 | -24.8 | 0.47 |
| consensus_gap | early | pin limit <$1k | 17-32 | 34.7 | -15.4 | -27.7 | 0.33 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 16.1 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 2.8 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 2.9 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.2 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 18.8 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 15.5 | 26.0 | -0.25 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 4.6 | -6.9 | 0.3 |
| consensus_gap+follow_move | early | 1-3k bets | 4-4 | 50.0 | 3.1 | -6.9 | 0.25 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.6 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.3 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 10-10 | 50.0 | 0.2 | -4.1 | 0.05 |
| follow_move+pin_value | early | 1-3k bets | 7-5 | 58.3 | 9.3 | 9.2 | -0.42 |
| follow_move+sharp_gap | early | 1-3k bets | 9-8 | 52.9 | 2.7 | 1.2 | -0.18 |
| follow_move+rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 14.5 | 29.2 | -0.5 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 26.7 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 4-2 | 66.7 | 14.5 | 29.2 | -0.5 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 18.1 | 56.1 | 0.15 |
| follow_move+money_moving | early | 1-3k bets | 9-4 | 69.2 | 19.9 | 32.1 | 0.08 |
| money_moving+rlm_ratio | early | 1-3k bets | 2-1 | 66.7 | 15.6 | 28.7 | -1.0 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.7 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 36.3 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 46.4 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 11-11 | 50.0 | 1.2 | -5.9 | 1.36 |
| consensus_gap+money_level | early | <1k bets | 18-15 | 54.5 | -10.7 | -19.3 | 0.26 |
| consensus_gap+sharp_gap | early | <1k bets | 13-25 | 34.2 | -14.9 | -16.7 | 0.57 |
| follow_move+money_level | early | <1k bets | 17-11 | 60.7 | 13.4 | 15.6 | 0.75 |
| follow_move+sharp_gap | early | <1k bets | 17-7 | 70.8 | 22.2 | 35.2 | 0.96 |
| money_level+sharp_gap | early | <1k bets | 52-25 | 67.5 | 11.1 | 10.5 | 0.65 |
| money_level+money_moving | early | <1k bets | 30-18 | 62.5 | 5.4 | 0.1 | 0.04 |
| money_moving+sharp_gap | early | <1k bets | 30-18 | 62.5 | 11.5 | 12.4 | 0.33 |
| consensus_gap+money_moving | early | <1k bets | 8-12 | 40.0 | -10.7 | -35.7 | -0.18 |
| follow_move+pin_value | early | <1k bets | 11-10 | 52.4 | 3.5 | -1.5 | 0.29 |
| follow_move+money_moving | early | <1k bets | 9-6 | 60.0 | 12.0 | 15.1 | 0.4 |
| consensus_gap+pin_value | early | <1k bets | 11-21 | 34.4 | -11.2 | -35.3 | 0.5 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -26.1 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -26.1 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | <1k bets | 1-1 | 50.0 | 23.9 | -3.7 | -2.15 |
| pin_value+sharp_gap | early | <1k bets | 4-3 | 57.1 | 11.5 | 9.1 | 0.03 |
| money_level+pin_value | early | <1k bets | 3-3 | 50.0 | 1.2 | -4.5 | 1.33 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -53.3 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -53.6 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 0-2 | 0.0 | -49.7 | -100.0 | 2.5 |
| follow_move+rlm_ratio | early | <1k bets | 3-1 | 75.0 | 23.1 | 44.2 | 0.0 |
| money_level+rlm_ratio | early | <1k bets | 2-0 | 100.0 | 46.4 | 93.0 | 0.5 |
| money_moving+rlm_ratio | early | <1k bets | 2-0 | 100.0 | 49.7 | 93.0 | -1.0 |
| rlm_ratio+sharp_gap | early | <1k bets | 3-1 | 75.0 | 23.1 | 44.2 | 0.0 |
| consensus_gap+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -53.6 | -100.0 | 1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 46.4 | 90.9 | 1.0 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 73.9 | 92.6 | 0.5 |
| consensus_gap+money_level | early | pin $1-2k | 4-4 | 50.0 | -13.8 | -22.9 | 0.44 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -31.6 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 4-9 | 30.8 | -8.6 | -42.5 | 0.4 |
| follow_move+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -3.1 | -1.0 | -0.5 |
| follow_move+sharp_gap | early | pin $1-2k | 3-1 | 75.0 | 25.0 | 45.0 | -0.25 |
| money_level+money_moving | early | pin $1-2k | 6-5 | 54.5 | -10.1 | -20.3 | 0.02 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.2 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 1-1 | 50.0 | -3.1 | -1.0 | -0.5 |
| money_level+sharp_gap | early | pin $1-2k | 8-4 | 66.7 | 4.7 | 8.4 | -0.41 |
| money_moving+sharp_gap | early | pin $1-2k | 3-5 | 37.5 | -21.1 | -45.3 | -0.06 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.7 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 2-2 | 50.0 | 0.0 | -8.4 | 0.75 |
| follow_move+money_level | early | pin $1-2k | 3-2 | 60.0 | 11.8 | 16.0 | 0.2 |
| follow_move+pin_value | early | pin $1-2k | 4-3 | 57.1 | 7.6 | 6.9 | 0.29 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 46.9 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 1-0 | 100.0 | 53.1 | 90.9 | 0.0 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.1 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -25.0 | -62.8 | -0.72 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -26.1 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -26.1 | -100.0 | -4.8 |
| money_level+money_moving | early | pin limit <$1k | 11-7 | 61.1 | 8.0 | 12.1 | 0.53 |
| money_level+sharp_gap | early | pin limit <$1k | 18-14 | 56.2 | 4.9 | 2.3 | 0.25 |
| money_moving+sharp_gap | early | pin limit <$1k | 16-5 | 76.2 | 28.0 | 68.0 | 0.39 |
| money_level+pin_value | early | pin limit <$1k | 8-5 | 61.5 | 10.2 | 16.6 | 0.46 |
| money_moving+pin_value | early | pin limit <$1k | 6-4 | 60.0 | 9.9 | 13.0 | 0.3 |
| pin_value+sharp_gap | early | pin limit <$1k | 11-5 | 68.8 | 18.3 | 30.3 | 0.06 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-7 | 46.2 | -1.1 | -14.2 | 0.46 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -26.9 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 13-17 | 43.3 | -4.9 | -18.8 | 0.49 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.4 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 8-7 | 53.3 | 3.4 | 1.9 | 0.07 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 5.1 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 9-7 | 56.2 | 6.2 | 6.9 | -0.31 |
| follow_move+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 27.9 | 53.6 | -0.4 |
| money_level+rlm_ratio | early | pin limit <$1k | 4-0 | 100.0 | 46.4 | 92.0 | 0.25 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.5 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 4-1 | 80.0 | 27.9 | 53.6 | -0.4 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 23.4 | 72.3 | 0.54 |
| follow_move+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 20.6 | 33.3 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.5 | 28.7 | -1.0 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -53.6 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -53.6 | -100.0 | 1.0 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.9 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 73.9 | 92.6 | 0.5 |
