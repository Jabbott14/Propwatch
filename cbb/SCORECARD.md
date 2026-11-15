# CBB scorecard

Generated 2026-11-15 16:37 UTC. 472 graded games (14 finished games had no final score matched and are not graded).

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before tip. Break-even at -110 is 52.4%. CLV = points of closing-line
value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured
on this sample. `edge` is hit% minus that. A signal that is structurally long
favourites or overs beats 50% whenever those run, which is not an edge -- this
sample ran **46.9% favourites** (n=471) and **46.2% overs** (n=472) and **74.4% moneyline favourites** (n=399).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

## EARLY

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 1-1 | 50.0 | 25.6 | 24.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | both | 177-193 | 47.8 | 49.2 | -1.4 | -30.88 | -8.3 | 0.12 | 38.9 | DROP: below break-even |
| rlm_ratio | both | 7-4 | 63.6 | 52.2 | 11.4 | +2.52 | 22.9 | -0.36 | 18.2 | keep collecting (11/30) |
| money_level | both | 113-69 | 62.1 | 58.4 | 3.7 | -3.07 | -1.7 | 0.23 | 42.3 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 98-74 | 57.0 | 49.5 | 7.5 | +23.77 | 13.8 | 0.34 | 43.0 | no edge shown yet |
| money_moving | both | 69-42 | 62.2 | 51.2 | 10.9 | +16.7 | 15.0 | 0.1 | 42.3 | PROMOTE: beats break-even and its own base rate |
| pin_value | both | 43-41 | 51.2 | 47.8 | 3.4 | -2.68 | -3.2 | 0.15 | 41.7 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.8 | -31.8 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 148-211 | 41.2 | 46.7 | -5.5 | -60.91 | -17.0 | 0.29 | 46.2 | DROP: below break-even |
| consensus_gap+money_level | both | 23-22 | 51.1 | 63.3 | -12.2 | -10.62 | -23.6 | 0.25 | 46.7 | no edge shown yet |
| consensus_gap+money_moving | both | 15-16 | 48.4 | 47.7 | 0.7 | -0.69 | -2.2 | -0.04 | 38.7 | no edge shown yet |
| consensus_gap+pin_value | both | 17-26 | 39.5 | 45.4 | -5.9 | -11.16 | -26.0 | 0.46 | 53.5 | DROP: below break-even |
| follow_move+rlm_ratio | both | 7-4 | 63.6 | 52.2 | 11.4 | +2.52 | 22.9 | -0.36 | 18.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 25-16 | 61.0 | 49.3 | 11.7 | +6.74 | 16.4 | 0.46 | 39.0 | no edge shown yet |
| money_level+money_moving | both | 44-23 | 65.7 | 56.5 | 9.2 | +5.41 | 8.1 | 0.1 | 47.8 | PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | both | 10-8 | 55.6 | 50.5 | 5.0 | +0.9 | 5.0 | 0.5 | 50.0 | keep collecting (18/30) |
| money_moving+pin_value | both | 7-5 | 58.3 | 50.1 | 8.3 | +1.13 | 9.4 | 0.42 | 41.7 | keep collecting (12/30) |
| rlm_ratio+sharp_gap | both | 7-4 | 63.6 | 52.2 | 11.4 | +2.52 | 22.9 | -0.36 | 18.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 69-38 | 64.5 | 55.6 | 8.9 | +8.82 | 8.2 | 0.49 | 46.7 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 44-25 | 63.8 | 49.7 | 14.1 | +15.34 | 22.2 | 0.3 | 43.5 | PROMOTE: beats break-even and its own base rate |
| pin_value+sharp_gap | both | 12-7 | 63.2 | 49.2 | 14.0 | +3.75 | 19.8 | -0.15 | 36.8 | keep collecting (19/30) |
| consensus_gap+follow_move | both | 15-15 | 50.0 | 48.3 | 1.7 | -1.86 | -6.2 | 1.07 | 53.3 | no edge shown yet |
| consensus_gap+sharp_gap | both | 17-31 | 35.4 | 47.1 | -11.7 | -4.48 | -9.3 | 0.54 | 45.8 | DROP: below break-even |
| follow_move+money_level | both | 26-21 | 55.3 | 48.2 | 7.2 | +2.67 | 5.7 | 0.47 | 40.4 | no edge shown yet |
| follow_move+pin_value | both | 18-15 | 54.5 | 48.9 | 5.6 | +0.8 | 2.4 | 0.03 | 30.3 | no edge shown yet |
| money_level+rlm_ratio | both | 6-1 | 85.7 | 53.5 | 32.2 | +4.61 | 65.9 | 0.14 | 14.3 | keep collecting (7/30) |
| pin_value+rlm_ratio | both | 2-1 | 66.7 | 51.3 | 15.4 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| follow_move+money_moving | both | 18-10 | 64.3 | 48.6 | 15.7 | +6.43 | 23.0 | 0.25 | 39.3 | keep collecting (28/30) |
| money_moving+rlm_ratio | both | 4-1 | 80.0 | 50.8 | 29.2 | +2.72 | 54.4 | -1.0 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 25.6 | -25.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 25.6 | -25.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | both | 1-1 | 50.0 | 25.6 | 24.4 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 53.4 | -53.4 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 25.6 | 74.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-1 | 50.0 | 25.6 | 24.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | spread | 89-100 | 47.1 | 49.1 | -2.0 | -18.37 | -9.7 | -0.03 | 33.9 | no edge shown yet |
| follow_move | total | 88-93 | 48.6 | 49.4 | -0.8 | -12.51 | -6.9 | 0.29 | 44.2 | no edge shown yet |
| rlm_ratio | spread | 3-2 | 60.0 | 51.8 | 8.2 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 4-2 | 66.7 | 52.5 | 14.1 | +1.68 | 28.0 | -0.17 | 33.3 | keep collecting (6/30) |
| money_level | moneyline | 59-25 | 70.2 | 69.8 | 0.5 | -8.06 | -9.6 | 0.28 | 48.8 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 16-15 | 51.6 | 48.9 | 2.7 | -0.6 | -1.9 | 0.9 | 48.4 | no edge shown yet |
| money_level | total | 38-29 | 56.7 | 48.6 | 8.1 | +5.59 | 8.3 | -0.13 | 31.3 | no edge shown yet |
| sharp_gap | moneyline | 40-34 | 54.1 | 48.0 | 6.0 | +11.05 | 14.9 | 0.35 | 51.4 | no edge shown yet |
| sharp_gap | spread | 18-14 | 56.2 | 49.8 | 6.4 | +2.26 | 7.1 | 0.56 | 34.4 | no edge shown yet |
| sharp_gap | total | 40-26 | 60.6 | 50.9 | 9.7 | +10.46 | 15.9 | 0.23 | 37.9 | no edge shown yet |
| money_moving | moneyline | 25-22 | 53.2 | 53.6 | -0.4 | -3.07 | -6.5 | 0.09 | 55.3 | no edge shown yet |
| money_moving | spread | 17-4 | 81.0 | 49.0 | 32.0 | +11.27 | 53.7 | 0.14 | 38.1 | keep collecting (21/30) |
| money_moving | total | 27-16 | 62.8 | 49.7 | 13.1 | +8.51 | 19.8 | 0.09 | 30.2 | no edge shown yet |
| pin_value | moneyline | 1-5 | 16.7 | 25.6 | -8.9 | -4.02 | -67.0 | -0.02 | 66.7 | keep collecting (6/30) |
| pin_value | spread | 22-17 | 56.4 | 49.1 | 7.3 | +2.35 | 6.0 | 0.28 | 41.0 | no edge shown yet |
| pin_value | total | 20-19 | 51.3 | 49.9 | 1.4 | -1.01 | -2.6 | 0.05 | 38.5 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 53.1 | -19.7 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 61-114 | 34.9 | 44.0 | -9.1 | -40.88 | -23.4 | -0.05 | 42.9 | DROP: below break-even |
| consensus_gap | spread | 47-47 | 50.0 | 49.1 | 0.9 | -6.04 | -6.4 | 0.49 | 45.7 | no edge shown yet |
| consensus_gap | total | 40-50 | 44.4 | 49.4 | -5.0 | -13.99 | -15.5 | 0.74 | 53.3 | DROP: below break-even |
| money_level+sharp_gap | moneyline | 31-11 | 73.8 | 65.1 | 8.7 | +1.33 | 3.2 | 0.6 | 61.9 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+pin_value | moneyline | 1-5 | 16.7 | 25.6 | -8.9 | -4.02 | -67.0 | -0.02 | 66.7 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_level+money_moving | moneyline | 16-8 | 66.7 | 70.4 | -3.7 | -5.13 | -21.4 | -0.1 | 58.3 | keep collecting (24/30) |
| consensus_gap+sharp_gap | moneyline | 11-22 | 33.3 | 46.3 | -13.0 | -0.71 | -2.1 | 0.42 | 48.5 | DROP: below break-even |
| consensus_gap+money_level | moneyline | 16-14 | 53.3 | 71.2 | -17.8 | -8.68 | -28.9 | -0.09 | 46.7 | INVERT candidate: wrong well beyond its base rate |
| money_moving+sharp_gap | moneyline | 15-12 | 55.6 | 49.1 | 6.5 | +2.07 | 7.7 | 0.44 | 63.0 | keep collecting (27/30) |
| consensus_gap+money_moving | moneyline | 7-15 | 31.8 | 47.8 | -16.0 | -6.63 | -30.1 | -0.01 | 50.0 | keep collecting (22/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 25.6 | -25.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 25.6 | -25.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | moneyline | 1-1 | 50.0 | 25.6 | 24.4 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 25.6 | -25.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 25.6 | 74.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
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
| follow_move+money_level | spread | 11-7 | 61.1 | 47.9 | 13.2 | +3.04 | 16.9 | 0.78 | 44.4 | keep collecting (18/30) |
| follow_move+pin_value | spread | 11-7 | 61.1 | 48.6 | 12.5 | +2.56 | 14.2 | 0.33 | 33.3 | keep collecting (18/30) |
| follow_move+money_moving | spread | 9-1 | 90.0 | 47.5 | 42.5 | +7.22 | 72.2 | 0.2 | 40.0 | keep collecting (10/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 53.1 | 13.6 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 53.1 | -53.1 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 19-11 | 63.3 | 49.0 | 14.4 | +6.34 | 21.1 | -0.03 | 33.3 | no edge shown yet |
| money_level+sharp_gap | total | 25-16 | 61.0 | 49.7 | 11.3 | +6.79 | 16.6 | 0.1 | 34.1 | no edge shown yet |
| money_moving+sharp_gap | total | 20-10 | 66.7 | 50.5 | 16.2 | +8.14 | 27.1 | 0.13 | 26.7 | PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | total | 7-4 | 63.6 | 51.7 | 11.9 | +2.32 | 21.1 | 0.36 | 36.4 | keep collecting (11/30) |
| money_moving+pin_value | total | 4-3 | 57.1 | 50.5 | 6.6 | +0.56 | 8.0 | 0.29 | 28.6 | keep collecting (7/30) |
| pin_value+sharp_gap | total | 10-5 | 66.7 | 50.8 | 15.9 | +4.01 | 26.7 | 0.0 | 33.3 | keep collecting (15/30) |
| follow_move+money_level | total | 15-14 | 51.7 | 48.3 | 3.4 | -0.37 | -1.3 | 0.28 | 37.9 | keep collecting (29/30) |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.2 | -2.6 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 4-2 | 66.7 | 52.5 | 14.1 | +1.68 | 28.0 | -0.17 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 15-10 | 60.0 | 49.8 | 10.2 | +3.66 | 14.6 | 0.36 | 40.0 | keep collecting (25/30) |
| money_level+rlm_ratio | total | 4-0 | 100.0 | 53.8 | 46.2 | +3.68 | 92.0 | 0.25 | 25.0 | keep collecting (4/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 51.3 | 15.4 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 4-2 | 66.7 | 52.5 | 14.1 | +1.68 | 28.0 | -0.17 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 9-9 | 50.0 | 49.2 | 0.8 | -0.8 | -4.4 | 0.28 | 38.9 | keep collecting (18/30) |
| consensus_gap+money_level | total | 3-3 | 50.0 | 48.7 | 1.3 | -0.34 | -5.7 | -0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 47.7 | 32.3 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-13 | 35.0 | 49.2 | -14.2 | -6.83 | -34.2 | 0.55 | 50.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | total | 3-6 | 33.3 | 50.4 | -17.1 | -3.35 | -37.2 | -0.11 | 22.2 | keep collecting (9/30) |
| money_moving+rlm_ratio | total | 2-1 | 66.7 | 51.3 | 15.4 | +0.86 | 28.7 | -1.0 | 0.0 | keep collecting (3/30) |
| consensus_gap+follow_move | total | 7-7 | 50.0 | 48.9 | 1.1 | -0.67 | -4.8 | 1.21 | 64.3 | keep collecting (14/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |

## CLOSE

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 92-99 | 48.2 | 43.0 | 5.1 | +25.6 | 13.4 |  |  | no edge shown yet |
| follow_move | both | 378-400 | 48.6 | 49.5 | -0.9 | -57.0 | -7.3 |  |  | DROP: below break-even |
| rlm_ratio | both | 113-90 | 55.7 | 51.4 | 4.3 | +13.31 | 6.6 |  |  | no edge shown yet |
| money_level | both | 730-564 | 56.4 | 55.6 | 0.8 | -76.29 | -5.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 565-685 | 45.2 | 47.4 | -2.2 | -98.83 | -7.9 |  |  | DROP: below break-even |
| money_moving | both | 561-690 | 44.8 | 47.6 | -2.7 | -111.62 | -8.9 |  |  | DROP: below break-even |
| pin_value | both | 249-256 | 49.3 | 47.3 | 2.0 | -5.99 | -1.2 |  |  | no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 51.0 | 15.6 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 243-368 | 39.8 | 45.8 | -6.1 | -88.68 | -14.5 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 58-56 | 50.9 | 47.6 | 3.2 | -5.8 | -5.1 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 102-202 | 33.6 | 42.9 | -9.3 | -35.92 | -11.8 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 17-31 | 35.4 | 36.4 | -1.0 | +12.54 | 26.1 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 102-127 | 44.5 | 44.2 | 0.3 | -9.38 | -4.1 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | both | 14-12 | 53.8 | 48.5 | 5.3 | +0.2 | 0.8 |  |  | keep collecting (26/30) |
| consensus_gap+sharp_gap | both | 103-206 | 33.3 | 42.5 | -9.1 | -36.75 | -11.9 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 246-276 | 47.1 | 49.7 | -2.6 | -53.35 | -10.2 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 59-46 | 56.2 | 52.0 | 4.2 | +8.15 | 7.8 |  |  | no edge shown yet |
| follow_move+pin_value | both | 91-84 | 52.0 | 48.8 | 3.2 | -3.48 | -2.0 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 113-90 | 55.7 | 51.4 | 4.3 | +13.31 | 6.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 250-272 | 47.9 | 49.7 | -1.8 | -45.49 | -8.7 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 89-98 | 47.6 | 43.0 | 4.6 | +23.87 | 12.8 |  |  | no edge shown yet |
| money_moving+pin_value | both | 104-130 | 44.4 | 46.2 | -1.8 | -12.0 | -5.1 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 110-89 | 55.3 | 51.4 | 3.9 | +11.47 | 5.8 |  |  | no edge shown yet |
| money_moving+sharp_gap | both | 541-663 | 44.9 | 47.4 | -2.5 | -98.84 | -8.2 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 27-25 | 51.9 | 45.2 | 6.7 | +16.22 | 31.2 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 59-46 | 56.2 | 52.0 | 4.2 | +8.15 | 7.8 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 92-99 | 48.2 | 43.0 | 5.1 | +25.6 | 13.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 25-19 | 56.8 | 50.6 | 6.3 | +3.44 | 7.8 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 106-129 | 45.1 | 46.4 | -1.2 | -9.24 | -3.9 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 113-90 | 55.7 | 51.4 | 4.3 | +13.31 | 6.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+money_moving | both | 391-383 | 50.5 | 52.2 | -1.7 | -60.55 | -7.8 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 392-379 | 50.8 | 52.1 | -1.3 | -52.79 | -6.8 |  |  | no edge shown yet |
| follow_move+money_level | both | 220-244 | 47.4 | 48.7 | -1.3 | -45.48 | -9.8 |  |  | DROP: below break-even |
| money_level+rlm_ratio | both | 58-48 | 54.7 | 51.0 | 3.7 | +4.81 | 4.5 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 147-134 | 52.3 | 56.6 | -4.3 | -27.49 | -9.8 |  |  | no edge shown yet |
| money_level+pin_value | both | 115-120 | 48.9 | 48.7 | 0.2 | -20.31 | -8.6 |  |  | no edge shown yet |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | both | 40-30 | 57.1 | 48.5 | 8.6 | +8.39 | 12.0 |  |  | no edge shown yet |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 53.8 | 46.2 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 24-47 | 33.8 | 27.6 | 6.2 | +15.44 | 21.7 |  |  | DROP: below break-even |
| pin_rlm | spread | 17-16 | 51.5 | 51.2 | 0.3 | -0.62 | -1.9 |  |  | no edge shown yet |
| pin_rlm | total | 51-36 | 58.6 | 52.5 | 6.1 | +10.78 | 12.4 |  |  | no edge shown yet |
| follow_move | spread | 176-181 | 49.3 | 49.0 | 0.3 | -22.25 | -6.2 |  |  | no edge shown yet |
| follow_move | total | 202-219 | 48.0 | 49.9 | -1.9 | -34.74 | -8.3 |  |  | DROP: below break-even |
| rlm_ratio | spread | 32-31 | 50.8 | 50.0 | 0.7 | -1.8 | -2.9 |  |  | no edge shown yet |
| rlm_ratio | total | 81-59 | 57.9 | 52.0 | 5.8 | +15.12 | 10.8 |  |  | no edge shown yet |
| money_level | moneyline | 288-104 | 73.5 | 70.6 | 2.9 | -15.68 | -4.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 213-226 | 48.5 | 48.8 | -0.3 | -34.64 | -7.9 |  |  | DROP: below break-even |
| money_level | total | 229-234 | 49.5 | 49.3 | 0.2 | -25.97 | -5.6 |  |  | no edge shown yet |
| sharp_gap | moneyline | 125-234 | 34.8 | 40.7 | -5.9 | -46.96 | -13.1 |  |  | DROP: below break-even |
| sharp_gap | spread | 219-216 | 50.3 | 49.5 | 0.8 | -18.77 | -4.3 |  |  | no edge shown yet |
| sharp_gap | total | 221-235 | 48.5 | 50.8 | -2.3 | -33.1 | -7.3 |  |  | DROP: below break-even |
| money_moving | moneyline | 128-229 | 35.9 | 41.3 | -5.5 | -43.21 | -12.1 |  |  | DROP: below break-even |
| money_moving | spread | 216-219 | 49.7 | 49.4 | 0.2 | -24.64 | -5.7 |  |  | no edge shown yet |
| money_moving | total | 217-242 | 47.3 | 50.7 | -3.4 | -43.77 | -9.5 |  |  | DROP: below break-even |
| pin_value | moneyline | 12-40 | 23.1 | 28.4 | -5.3 | -0.42 | -0.8 |  |  | DROP: below break-even |
| pin_value | spread | 119-103 | 53.6 | 49.6 | 4.0 | +1.36 | 0.6 |  |  | no edge shown yet |
| pin_value | total | 118-113 | 51.1 | 49.3 | 1.8 | -6.93 | -3.0 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 53.1 | 46.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 98-214 | 31.4 | 43.4 | -12.0 | -61.01 | -19.6 |  |  | DROP: below break-even |
| consensus_gap | spread | 71-63 | 53.0 | 48.9 | 4.1 | -2.36 | -1.8 |  |  | no edge shown yet |
| consensus_gap | total | 74-91 | 44.8 | 47.9 | -3.1 | -25.32 | -15.3 |  |  | DROP: below break-even |
| money_level+money_moving | moneyline | 86-57 | 60.1 | 64.5 | -4.4 | -10.13 | -7.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 83-56 | 59.7 | 64.2 | -4.5 | -9.05 | -6.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 115-219 | 34.4 | 40.3 | -5.9 | -41.11 | -12.3 |  |  | DROP: below break-even |
| consensus_gap+money_level | moneyline | 66-45 | 59.5 | 70.0 | -10.6 | -8.9 | -8.0 |  |  | no edge shown yet |
| consensus_gap+money_moving | moneyline | 33-124 | 21.0 | 37.7 | -16.7 | -17.74 | -11.3 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+sharp_gap | moneyline | 34-129 | 20.9 | 37.0 | -16.1 | -19.58 | -12.0 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_rlm | moneyline | 9-21 | 30.0 | 28.8 | 1.2 | +15.63 | 52.1 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 24-46 | 34.3 | 27.7 | 6.6 | +16.44 | 23.5 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 24-47 | 33.8 | 27.6 | 6.2 | +15.44 | 21.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 12-36 | 25.0 | 28.6 | -3.6 | +3.58 | 7.5 |  |  | DROP: below break-even |
| money_moving+pin_value | moneyline | 6-26 | 18.8 | 25.6 | -6.8 | +5.75 | 18.0 |  |  | DROP: below break-even |
| pin_rlm+pin_value | moneyline | 4-8 | 33.3 | 25.6 | 7.8 | +12.55 | 104.6 |  |  | keep collecting (12/30) |
| pin_value+sharp_gap | moneyline | 6-26 | 18.8 | 25.6 | -6.8 | +5.75 | 18.0 |  |  | DROP: below break-even |
| money_level+pin_rlm | moneyline | 7-6 | 53.8 | 33.1 | 20.8 | +2.33 | 17.9 |  |  | keep collecting (13/30) |
| money_level+pin_value | moneyline | 3-1 | 75.0 | 62.2 | 12.8 | +0.31 | 7.8 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 31-24 | 56.4 | 47.9 | 8.4 | +2.4 | 4.4 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 39-35 | 52.7 | 48.8 | 4.0 | -1.68 | -2.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | -0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 49-39 | 55.7 | 48.9 | 6.8 | +2.7 | 3.1 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.33 | -38.9 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | spread | 38-35 | 52.1 | 49.0 | 3.0 | -2.58 | -3.5 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 112-117 | 48.9 | 48.7 | 0.2 | -16.5 | -7.2 |  |  | no edge shown yet |
| follow_move+pin_rlm | spread | 15-15 | 50.0 | 51.0 | -1.0 | -1.37 | -4.6 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 47-39 | 54.7 | 48.6 | 6.1 | +2.04 | 2.4 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 32-31 | 50.8 | 50.0 | 0.7 | -1.8 | -2.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 113-116 | 49.3 | 48.8 | 0.5 | -14.36 | -6.3 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 15-16 | 48.4 | 51.1 | -2.7 | -2.44 | -7.9 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 55-54 | 50.5 | 49.1 | 1.4 | -6.42 | -5.9 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 30-30 | 50.0 | 49.9 | 0.1 | -2.74 | -4.6 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 211-211 | 50.0 | 49.4 | 0.6 | -21.14 | -5.0 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 6-7 | 46.2 | 50.2 | -4.1 | -1.79 | -13.8 |  |  | keep collecting (13/30) |
| pin_rlm+rlm_ratio | spread | 15-15 | 50.0 | 51.0 | -1.0 | -1.37 | -4.6 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 17-16 | 51.5 | 51.2 | 0.3 | -0.62 | -1.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 4-6 | 40.0 | 49.4 | -9.4 | -2.55 | -25.5 |  |  | keep collecting (10/30) |
| pin_value+sharp_gap | spread | 55-54 | 50.5 | 49.2 | 1.2 | -6.49 | -6.0 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 32-31 | 50.8 | 50.0 | 0.7 | -1.8 | -2.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 109-116 | 48.4 | 48.3 | 0.2 | -18.3 | -8.1 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 16-16 | 50.0 | 49.4 | 0.6 | -1.54 | -4.8 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 165-167 | 49.7 | 48.9 | 0.8 | -18.92 | -5.7 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 47-40 | 54.0 | 48.4 | 5.6 | +0.28 | 0.3 |  |  | no edge shown yet |
| money_level+money_moving | spread | 164-168 | 49.4 | 48.9 | 0.5 | -20.83 | -6.3 |  |  | no edge shown yet |
| money_level+pin_value | spread | 60-62 | 49.2 | 48.7 | 0.4 | -10.11 | -8.3 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 8-6 | 57.1 | 50.4 | 6.7 | +1.1 | 7.9 |  |  | keep collecting (14/30) |
| money_level+money_moving | total | 141-158 | 47.2 | 50.0 | -2.8 | -29.58 | -9.9 |  |  | DROP: below break-even |
| money_level+sharp_gap | total | 144-156 | 48.0 | 50.0 | -2.0 | -24.82 | -8.3 |  |  | DROP: below break-even |
| money_moving+sharp_gap | total | 215-233 | 48.0 | 50.7 | -2.8 | -36.59 | -8.2 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 34-49 | 41.0 | 47.1 | -6.1 | -18.87 | -22.7 |  |  | DROP: below break-even |
| consensus_gap+pin_value | total | 41-52 | 44.1 | 47.8 | -3.7 | -15.65 | -16.8 |  |  | DROP: below break-even |
| follow_move+money_moving | total | 134-159 | 45.7 | 50.4 | -4.7 | -36.85 | -12.6 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 137-156 | 46.8 | 50.5 | -3.7 | -31.12 | -10.6 |  |  | DROP: below break-even |
| money_level+pin_value | total | 52-57 | 47.7 | 48.2 | -0.5 | -10.51 | -9.6 |  |  | no edge shown yet |
| follow_move+money_level | total | 111-128 | 46.4 | 49.2 | -2.7 | -27.17 | -11.4 |  |  | DROP: below break-even |
| follow_move+pin_value | total | 44-45 | 49.4 | 49.1 | 0.3 | -5.52 | -6.2 |  |  | no edge shown yet |
| money_moving+pin_value | total | 43-50 | 46.2 | 50.0 | -3.7 | -11.32 | -12.2 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 45-49 | 47.9 | 50.1 | -2.2 | -8.51 | -9.0 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 30-43 | 41.1 | 48.1 | -7.0 | -16.5 | -22.6 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | total | 31-42 | 42.5 | 48.2 | -5.7 | -14.59 | -20.0 |  |  | DROP: below break-even |
| consensus_gap+follow_move | total | 27-32 | 45.8 | 47.3 | -1.6 | -8.21 | -13.9 |  |  | no edge shown yet |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pin_rlm | total | 5-7 | 41.7 | 48.7 | -7.1 | -2.6 | -21.7 |  |  | keep collecting (12/30) |
| consensus_gap+rlm_ratio | total | 12-8 | 60.0 | 48.1 | 11.9 | +2.53 | 12.7 |  |  | keep collecting (20/30) |
| follow_move+pin_rlm | total | 44-31 | 58.7 | 52.4 | 6.3 | +9.52 | 12.7 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 81-59 | 57.9 | 52.0 | 5.8 | +15.12 | 10.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 25-18 | 58.1 | 52.6 | 5.6 | +4.95 | 11.5 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 42-32 | 56.8 | 51.6 | 5.1 | +6.35 | 8.6 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 50-36 | 58.1 | 52.5 | 5.7 | +9.87 | 11.5 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 80-59 | 57.6 | 52.0 | 5.6 | +14.21 | 10.2 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 17-10 | 63.0 | 51.6 | 11.4 | +5.46 | 20.2 |  |  | keep collecting (27/30) |
| pin_rlm+rlm_ratio | total | 44-31 | 58.7 | 52.4 | 6.3 | +9.52 | 12.7 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 51-36 | 58.6 | 52.5 | 6.1 | +10.78 | 12.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 21-13 | 61.8 | 50.9 | 10.9 | +5.99 | 17.6 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 81-59 | 57.9 | 52.0 | 5.8 | +15.12 | 10.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 53.8 | 46.2 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_rlm | close | 1-3k bets | 54-61 | 47.0 | 3.2 | 14.1 |  |
| pin_rlm | close | 3k+ bets | 20-21 | 48.8 | 7.3 | 8.7 |  |
| pin_rlm | close | <1k bets | 18-17 | 51.4 | 8.9 | 16.7 |  |
| pin_rlm | close | pin $1-2k | 42-37 | 53.2 | 8.3 | 24.7 |  |
| pin_rlm | close | pin $2k+ | 19-46 | 29.2 | -5.6 | -23.4 |  |
| pin_rlm | close | pin limit <$1k | 31-16 | 66.0 | 14.7 | 45.4 |  |
| follow_move | close | 1-3k bets | 248-247 | 50.1 | 0.6 | -4.4 |  |
| follow_move | close | 3k+ bets | 79-90 | 46.7 | -2.6 | -10.9 |  |
| follow_move | close | <1k bets | 51-63 | 44.7 | -4.7 | -14.6 |  |
| follow_move | close | pin $1-2k | 120-165 | 42.1 | -7.1 | -19.7 |  |
| follow_move | close | pin $2k+ | 71-70 | 50.4 | 0.8 | -4.0 |  |
| follow_move | close | pin limit <$1k | 81-73 | 52.6 | 2.4 | 0.6 |  |
| rlm_ratio | close | 1-3k bets | 73-63 | 53.7 | 2.2 | 2.6 |  |
| rlm_ratio | close | 3k+ bets | 24-17 | 58.5 | 7.5 | 12.1 |  |
| rlm_ratio | close | <1k bets | 16-10 | 61.5 | 9.9 | 18.6 |  |
| rlm_ratio | close | pin $1-2k | 39-36 | 52.0 | 1.1 | -0.7 |  |
| rlm_ratio | close | pin $2k+ | 12-15 | 44.4 | -6.8 | -15.4 |  |
| rlm_ratio | close | pin limit <$1k | 32-19 | 62.7 | 10.3 | 20.7 |  |
| money_level | close | 1-3k bets | 472-328 | 59.0 | 3.4 | -1.3 |  |
| money_level | close | 3k+ bets | 150-134 | 52.8 | -2.5 | -10.2 |  |
| money_level | close | <1k bets | 108-101 | 51.7 | -4.1 | -17.2 |  |
| money_level | close | pin $1-2k | 212-195 | 52.1 | -1.8 | -7.9 |  |
| money_level | close | pin $2k+ | 178-144 | 55.3 | -2.4 | -10.3 |  |
| money_level | close | pin limit <$1k | 84-91 | 48.0 | -1.5 | -9.0 |  |
| sharp_gap | close | 1-3k bets | 341-427 | 44.4 | -2.9 | -10.1 |  |
| sharp_gap | close | 3k+ bets | 133-147 | 47.5 | 0.6 | 2.8 |  |
| sharp_gap | close | <1k bets | 91-110 | 45.3 | -3.3 | -13.9 |  |
| sharp_gap | close | pin $1-2k | 190-207 | 47.9 | -1.3 | -4.0 |  |
| sharp_gap | close | pin $2k+ | 133-178 | 42.8 | -3.2 | -13.2 |  |
| sharp_gap | close | pin limit <$1k | 83-85 | 49.4 | -1.5 | -0.1 |  |
| money_moving | close | 1-3k bets | 340-429 | 44.2 | -3.4 | -11.2 |  |
| money_moving | close | 3k+ bets | 132-150 | 46.8 | -0.5 | 0.0 |  |
| money_moving | close | <1k bets | 89-110 | 44.7 | -3.3 | -12.5 |  |
| money_moving | close | pin $1-2k | 185-213 | 46.5 | -2.4 | -5.9 |  |
| money_moving | close | pin $2k+ | 135-175 | 43.5 | -2.4 | -11.7 |  |
| money_moving | close | pin limit <$1k | 81-89 | 47.6 | -3.0 | -3.5 |  |
| pin_value | close | 1-3k bets | 153-160 | 48.9 | 1.3 | -2.5 |  |
| pin_value | close | 3k+ bets | 52-57 | 47.7 | 0.3 | -4.3 |  |
| pin_value | close | <1k bets | 44-39 | 53.0 | 6.9 | 7.7 |  |
| pin_value | close | pin $1-2k | 118-127 | 48.2 | 0.4 | -5.4 |  |
| pin_value | close | pin $2k+ | 69-77 | 47.3 | 1.7 | -0.4 |  |
| pin_value | close | pin limit <$1k | 62-52 | 54.4 | 5.9 | 6.9 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 46.9 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 46.9 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 152-225 | 40.3 | -6.0 | -16.0 |  |
| consensus_gap | close | 3k+ bets | 57-76 | 42.9 | -3.8 | 0.3 |  |
| consensus_gap | close | <1k bets | 34-66 | 34.0 | -9.3 | -27.8 |  |
| consensus_gap | close | pin $1-2k | 78-101 | 43.6 | -3.8 | -5.0 |  |
| consensus_gap | close | pin $2k+ | 62-78 | 44.3 | -5.5 | -14.7 |  |
| consensus_gap | close | pin limit <$1k | 38-38 | 50.0 | 2.1 | -0.9 |  |
| consensus_gap+follow_move | close | 1-3k bets | 42-34 | 55.3 | 7.7 | 3.3 |  |
| consensus_gap+money_level | close | 1-3k bets | 101-76 | 57.1 | 0.0 | 0.3 |  |
| consensus_gap+money_moving | close | 1-3k bets | 66-124 | 34.7 | -8.6 | -13.5 |  |
| consensus_gap+pin_value | close | 1-3k bets | 63-85 | 42.6 | -2.1 | -9.3 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 66-127 | 34.2 | -8.6 | -14.7 |  |
| follow_move+money_level | close | 1-3k bets | 154-153 | 50.2 | 1.4 | -4.5 |  |
| follow_move+money_moving | close | 1-3k bets | 170-181 | 48.4 | -1.3 | -7.7 |  |
| follow_move+pin_value | close | 1-3k bets | 55-50 | 52.4 | 3.6 | -1.3 |  |
| follow_move+sharp_gap | close | 1-3k bets | 170-178 | 48.9 | -0.9 | -6.9 |  |
| money_level+money_moving | close | 1-3k bets | 246-227 | 52.0 | -0.2 | -3.8 |  |
| money_level+pin_value | close | 1-3k bets | 76-71 | 51.7 | 3.0 | -3.0 |  |
| money_level+sharp_gap | close | 1-3k bets | 245-226 | 52.0 | -0.0 | -3.1 |  |
| money_moving+pin_value | close | 1-3k bets | 67-83 | 44.7 | -2.0 | -7.0 |  |
| money_moving+sharp_gap | close | 1-3k bets | 329-414 | 44.3 | -3.1 | -10.2 |  |
| pin_value+sharp_gap | close | 1-3k bets | 69-85 | 44.8 | -1.9 | -7.0 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 11-19 | 36.7 | -0.8 | 32.6 |  |
| money_level+pin_rlm | close | 1-3k bets | 26-19 | 57.8 | 6.4 | 10.8 |  |
| pin_rlm+pin_value | close | 1-3k bets | 17-16 | 51.5 | 6.0 | 39.0 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 54-61 | 47.0 | 3.2 | 14.1 |  |
| money_moving+pin_rlm | close | 1-3k bets | 52-60 | 46.4 | 2.7 | 13.8 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 13-7 | 65.0 | 16.5 | 21.6 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 73-63 | 53.7 | 2.2 | 2.6 |  |
| money_level+rlm_ratio | close | 1-3k bets | 38-33 | 53.5 | 2.5 | 2.2 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 72-63 | 53.3 | 1.9 | 1.9 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 73-63 | 53.7 | 2.2 | 2.6 |  |
| follow_move+pin_rlm | close | 1-3k bets | 35-30 | 53.8 | 1.7 | 3.1 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 35-30 | 53.8 | 1.7 | 3.1 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 17-13 | 56.7 | 6.3 | 7.4 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 46.2 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 13-13 | 50.0 | 2.4 | -7.0 |  |
| consensus_gap+money_moving | close | 3k+ bets | 22-44 | 33.3 | -9.6 | 6.7 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-5 | 37.5 | -2.8 | 19.3 |  |
| consensus_gap+pin_value | close | 3k+ bets | 27-29 | 48.2 | 3.8 | 1.4 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 1-3 | 25.0 | -22.9 | -53.2 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 23-44 | 34.3 | -8.5 | 10.9 |  |
| follow_move+money_moving | close | 3k+ bets | 50-57 | 46.7 | -2.6 | -11.2 |  |
| follow_move+pin_rlm | close | 3k+ bets | 14-10 | 58.3 | 6.7 | 12.4 |  |
| follow_move+pin_value | close | 3k+ bets | 20-23 | 46.5 | -2.3 | -12.8 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 24-17 | 58.5 | 7.5 | 12.1 |  |
| follow_move+sharp_gap | close | 3k+ bets | 54-56 | 49.1 | -0.4 | -6.5 |  |
| money_moving+pin_rlm | close | 3k+ bets | 19-21 | 47.5 | 6.3 | 6.5 |  |
| money_moving+pin_value | close | 3k+ bets | 24-31 | 43.6 | -2.0 | -5.0 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 22-16 | 57.9 | 7.0 | 10.6 |  |
| money_moving+sharp_gap | close | 3k+ bets | 125-140 | 47.2 | 0.2 | 2.0 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-6 | 45.5 | -0.9 | -13.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 14-10 | 58.3 | 6.7 | 12.4 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 20-21 | 48.8 | 7.3 | 8.7 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 5-5 | 50.0 | -0.5 | -5.2 |  |
| pin_value+sharp_gap | close | 3k+ bets | 24-29 | 45.3 | -0.5 | -1.4 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 24-17 | 58.5 | 7.5 | 12.1 |  |
| money_level+money_moving | close | 3k+ bets | 86-87 | 49.7 | -2.3 | -9.3 |  |
| money_level+sharp_gap | close | 3k+ bets | 85-84 | 50.3 | -1.4 | -7.1 |  |
| follow_move+money_level | close | 3k+ bets | 46-52 | 46.9 | -1.5 | -10.9 |  |
| money_level+rlm_ratio | close | 3k+ bets | 13-8 | 61.9 | 11.5 | 17.7 |  |
| consensus_gap+money_level | close | 3k+ bets | 31-34 | 47.7 | -8.2 | -19.0 |  |
| money_level+pin_value | close | 3k+ bets | 24-32 | 42.9 | -5.5 | -20.9 |  |
| money_level+pin_rlm | close | 3k+ bets | 8-6 | 57.1 | 13.2 | 17.5 |  |
| money_level+money_moving | close | <1k bets | 59-68 | 46.5 | -6.2 | -19.9 |  |
| money_level+sharp_gap | close | <1k bets | 62-68 | 47.7 | -5.6 | -19.2 |  |
| money_moving+sharp_gap | close | <1k bets | 87-108 | 44.6 | -3.6 | -13.9 |  |
| consensus_gap+money_level | close | <1k bets | 15-24 | 38.5 | -17.0 | -39.9 |  |
| consensus_gap+money_moving | close | <1k bets | 14-34 | 29.2 | -11.9 | -30.7 |  |
| consensus_gap+pin_value | close | <1k bets | 12-13 | 48.0 | 7.0 | 14.3 |  |
| consensus_gap+sharp_gap | close | <1k bets | 14-35 | 28.6 | -12.1 | -32.1 |  |
| money_level+pin_value | close | <1k bets | 15-17 | 46.9 | -2.5 | -13.0 |  |
| money_moving+pin_value | close | <1k bets | 13-16 | 44.8 | -0.1 | 4.5 |  |
| pin_value+sharp_gap | close | <1k bets | 13-15 | 46.4 | 0.8 | 8.3 |  |
| follow_move+money_moving | close | <1k bets | 26-38 | 40.6 | -9.1 | -22.3 |  |
| follow_move+sharp_gap | close | <1k bets | 26-38 | 40.6 | -9.2 | -22.3 |  |
| follow_move+money_level | close | <1k bets | 20-39 | 33.9 | -15.0 | -35.4 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -0.5 | 12.2 |  |
| money_moving+pin_rlm | close | <1k bets | 18-17 | 51.4 | 8.9 | 16.7 |  |
| pin_rlm+sharp_gap | close | <1k bets | 18-17 | 51.4 | 8.9 | 16.7 |  |
| consensus_gap+follow_move | close | <1k bets | 3-9 | 25.0 | -22.9 | -54.1 |  |
| follow_move+pin_rlm | close | <1k bets | 10-6 | 62.5 | 10.5 | 19.8 |  |
| follow_move+pin_value | close | <1k bets | 16-11 | 59.3 | 10.1 | 12.6 |  |
| follow_move+rlm_ratio | close | <1k bets | 16-10 | 61.5 | 9.9 | 18.6 |  |
| money_moving+rlm_ratio | close | <1k bets | 16-10 | 61.5 | 9.9 | 18.6 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 20.1 | 60.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 10-6 | 62.5 | 10.5 | 19.8 |  |
| pin_value+rlm_ratio | close | <1k bets | 3-1 | 75.0 | 22.9 | 43.9 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 16-10 | 61.5 | 9.9 | 18.6 |  |
| money_level+rlm_ratio | close | <1k bets | 7-7 | 50.0 | -1.8 | -3.4 |  |
| money_level+pin_rlm | close | <1k bets | 6-5 | 54.5 | 11.7 | 9.9 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 20-24 | 45.5 | -2.3 | -15.2 |  |
| consensus_gap+money_moving | close | pin $1-2k | 39-57 | 40.6 | -6.3 | -8.3 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 11-16 | 40.7 | 1.0 | 30.3 |  |
| consensus_gap+pin_value | close | pin $1-2k | 47-61 | 43.5 | -0.9 | -10.5 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 8-7 | 53.3 | 5.0 | -0.7 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 39-54 | 41.9 | -4.3 | -5.4 |  |
| follow_move+money_moving | close | pin $1-2k | 84-114 | 42.4 | -7.0 | -19.2 |  |
| follow_move+pin_rlm | close | pin $1-2k | 28-21 | 57.1 | 5.3 | 9.5 |  |
| follow_move+pin_value | close | pin $1-2k | 40-48 | 45.5 | -3.5 | -14.5 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 39-36 | 52.0 | 1.1 | -0.7 |  |
| follow_move+sharp_gap | close | pin $1-2k | 86-113 | 43.2 | -6.3 | -17.7 |  |
| money_moving+pin_rlm | close | pin $1-2k | 40-36 | 52.6 | 7.7 | 24.6 |  |
| money_moving+pin_value | close | pin $1-2k | 45-63 | 41.7 | -5.4 | -16.8 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 38-35 | 52.1 | 1.3 | -0.7 |  |
| money_moving+sharp_gap | close | pin $1-2k | 181-203 | 47.1 | -1.8 | -5.1 |  |
| pin_rlm+pin_value | close | pin $1-2k | 10-15 | 40.0 | -7.7 | -12.9 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 28-21 | 57.1 | 5.3 | 9.5 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 42-37 | 53.2 | 8.3 | 24.7 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 12-13 | 48.0 | -1.7 | -9.9 |  |
| pin_value+sharp_gap | close | pin $1-2k | 45-61 | 42.5 | -4.7 | -15.2 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 39-36 | 52.0 | 1.1 | -0.7 |  |
| follow_move+money_level | close | pin $1-2k | 80-103 | 43.7 | -5.0 | -16.9 |  |
| money_level+rlm_ratio | close | pin $1-2k | 24-19 | 55.8 | 5.8 | 6.1 |  |
| money_level+sharp_gap | close | pin $1-2k | 140-142 | 49.6 | -2.2 | -8.0 |  |
| money_level+money_moving | close | pin $1-2k | 137-145 | 48.6 | -3.1 | -9.5 |  |
| consensus_gap+money_level | close | pin $1-2k | 43-47 | 47.8 | -7.6 | -15.4 |  |
| money_level+pin_value | close | pin $1-2k | 51-56 | 47.7 | -1.4 | -10.8 |  |
| money_level+pin_rlm | close | pin $1-2k | 21-14 | 60.0 | 12.2 | 19.1 |  |
| follow_move+money_level | close | pin $2k+ | 38-41 | 48.1 | -0.7 | -8.5 |  |
| follow_move+money_moving | close | pin $2k+ | 44-46 | 48.9 | -0.7 | -7.0 |  |
| follow_move+sharp_gap | close | pin $2k+ | 45-46 | 49.5 | -0.1 | -5.9 |  |
| money_level+money_moving | close | pin $2k+ | 87-91 | 48.9 | -3.9 | -11.5 |  |
| money_level+sharp_gap | close | pin $2k+ | 87-93 | 48.3 | -4.6 | -12.2 |  |
| money_moving+sharp_gap | close | pin $2k+ | 130-173 | 42.9 | -2.9 | -12.3 |  |
| consensus_gap+money_moving | close | pin $2k+ | 20-47 | 29.9 | -12.5 | -21.7 |  |
| consensus_gap+pin_value | close | pin $2k+ | 29-36 | 44.6 | 3.5 | 7.3 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 21-50 | 29.6 | -13.9 | -24.2 |  |
| money_moving+pin_value | close | pin $2k+ | 34-44 | 43.6 | -0.0 | 2.9 |  |
| pin_value+sharp_gap | close | pin $2k+ | 34-44 | 43.6 | -0.0 | 2.9 |  |
| consensus_gap+follow_move | close | pin $2k+ | 8-6 | 57.1 | 9.0 | 5.7 |  |
| follow_move+pin_value | close | pin $2k+ | 23-17 | 57.5 | 8.6 | 8.2 |  |
| follow_move+pin_rlm | close | pin $2k+ | 7-13 | 35.0 | -16.9 | -33.3 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 12-15 | 44.4 | -6.8 | -15.4 |  |
| money_level+pin_rlm | close | pin $2k+ | 6-8 | 42.9 | -1.1 | -16.1 |  |
| money_level+pin_value | close | pin $2k+ | 33-35 | 48.5 | -0.6 | -10.7 |  |
| money_level+rlm_ratio | close | pin $2k+ | 5-7 | 41.7 | -9.4 | -20.4 |  |
| money_moving+pin_rlm | close | pin $2k+ | 19-46 | 29.2 | -5.6 | -23.4 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 12-15 | 44.4 | -6.8 | -15.4 |  |
| pin_rlm+pin_value | close | pin $2k+ | 4-8 | 33.3 | -1.5 | 42.9 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 7-13 | 35.0 | -16.9 | -33.3 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 19-46 | 29.2 | -5.6 | -23.4 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 1-2 | 33.3 | -19.7 | -37.4 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 12-15 | 44.4 | -6.8 | -15.4 |  |
| consensus_gap+money_level | close | pin $2k+ | 43-33 | 56.6 | -5.7 | -12.6 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 3-13 | 18.8 | -10.3 | -4.5 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -53.1 | -100.0 |  |
| money_level+money_moving | close | pin limit <$1k | 44-53 | 45.4 | -4.6 | -13.2 |  |
| money_level+sharp_gap | close | pin limit <$1k | 46-53 | 46.5 | -3.8 | -11.1 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 77-80 | 49.0 | -1.8 | -0.4 |  |
| consensus_gap+money_level | close | pin limit <$1k | 20-22 | 47.6 | -0.6 | -12.1 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 26-30 | 46.4 | -1.0 | -4.8 |  |
| follow_move+money_moving | close | pin limit <$1k | 50-53 | 48.5 | -2.4 | -7.0 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 51-51 | 50.0 | -1.0 | -4.2 |  |
| money_level+pin_value | close | pin limit <$1k | 31-29 | 51.7 | 4.0 | -2.5 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 13-10 | 56.5 | 9.1 | 5.9 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 16-15 | 51.6 | 4.5 | 11.6 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 17-16 | 51.5 | 3.8 | 10.5 |  |
| follow_move+money_level | close | pin limit <$1k | 40-42 | 48.8 | -0.4 | -6.9 |  |
| follow_move+pin_value | close | pin limit <$1k | 28-19 | 59.6 | 11.0 | 12.8 |  |
| money_moving+pin_value | close | pin limit <$1k | 25-23 | 52.1 | 3.6 | 8.1 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 27-24 | 52.9 | 4.0 | 9.1 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 3-2 | 60.0 | 17.9 | 101.6 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 30-16 | 65.2 | 14.0 | 44.4 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 13-2 | 86.7 | 37.3 | 95.2 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 31-16 | 66.0 | 14.7 | 45.4 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 24-12 | 66.7 | 14.4 | 28.2 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 32-19 | 62.7 | 10.3 | 20.7 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 31-19 | 62.0 | 9.6 | 19.3 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 24-12 | 66.7 | 14.4 | 28.2 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 32-19 | 62.7 | 10.3 | 20.7 |  |
| money_level+pin_rlm | close | pin limit <$1k | 13-8 | 61.9 | 9.2 | 18.9 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 14-10 | 58.3 | 5.8 | 12.5 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 12-4 | 75.0 | 23.6 | 43.9 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 3-3 | 50.0 | 2.5 | -5.2 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 46.2 | 87.7 |  |
| pin_rlm | early | <1k bets | 1-1 | 50.0 | 24.4 | -3.7 | -2.15 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.6 | -100.0 | -4.8 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.4 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 15-16 | 48.4 | -0.7 | -7.7 | -0.1 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -49.6 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 141-151 | 48.3 | -0.8 | -7.5 | 0.19 |
| follow_move | early | pin $1-2k | 10-8 | 55.6 | 5.6 | 5.0 | -0.06 |
| follow_move | early | pin limit <$1k | 33-29 | 53.2 | 4.3 | 1.1 | -0.35 |
| rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 14.5 | 29.2 | -0.5 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 3-1 | 75.0 | 22.9 | 44.2 | 0.0 |
| rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -3.1 | -1.0 | -0.5 |
| rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 27.7 | 53.6 | -0.4 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | -0.1 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 41.6 | 59.7 | 0.33 |
| money_level | early | <1k bets | 84-49 | 63.2 | 4.1 | -1.3 | 0.29 |
| money_level | early | pin $1-2k | 14-8 | 63.6 | -0.4 | -3.2 | 0.01 |
| money_level | early | pin limit <$1k | 22-24 | 47.8 | -6.2 | -12.1 | 0.31 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.0 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 6.2 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 71-52 | 57.7 | 7.8 | 11.7 | 0.48 |
| sharp_gap | early | pin $1-2k | 11-9 | 55.0 | 3.3 | 13.8 | -0.57 |
| sharp_gap | early | pin limit <$1k | 27-16 | 62.8 | 14.0 | 30.8 | 0.2 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.1 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.6 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 45-31 | 59.2 | 7.2 | 5.5 | 0.07 |
| money_moving | early | pin $1-2k | 6-6 | 50.0 | -11.7 | -26.9 | 0.35 |
| money_moving | early | pin limit <$1k | 20-9 | 69.0 | 19.8 | 47.8 | 0.36 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.5 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 30-32 | 48.4 | 0.9 | -8.3 | 0.21 |
| pin_value | early | pin $1-2k | 11-14 | 44.0 | -0.1 | -16.7 | 0.17 |
| pin_value | early | pin limit <$1k | 32-27 | 54.2 | 4.9 | 2.5 | 0.15 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -46.2 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -28.3 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -10.7 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 13.8 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 118-164 | 41.8 | -5.2 | -17.1 | 0.27 |
| consensus_gap | early | pin $1-2k | 10-16 | 38.5 | -7.3 | -24.8 | 0.47 |
| consensus_gap | early | pin limit <$1k | 17-32 | 34.7 | -15.4 | -27.7 | 0.33 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 15.9 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 2.7 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 2.8 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.2 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 18.8 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 15.4 | 26.0 | -0.25 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 4.7 | -6.9 | 0.3 |
| consensus_gap+follow_move | early | 1-3k bets | 4-4 | 50.0 | 3.2 | -6.9 | 0.25 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.8 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.0 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 10-10 | 50.0 | 0.2 | -4.1 | 0.05 |
| follow_move+pin_value | early | 1-3k bets | 7-5 | 58.3 | 9.2 | 9.2 | -0.42 |
| follow_move+sharp_gap | early | 1-3k bets | 9-8 | 52.9 | 2.6 | 1.2 | -0.18 |
| follow_move+rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 14.5 | 29.2 | -0.5 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 26.6 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 4-2 | 66.7 | 14.5 | 29.2 | -0.5 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 18.3 | 56.1 | 0.15 |
| follow_move+money_moving | early | 1-3k bets | 9-4 | 69.2 | 19.9 | 32.1 | 0.08 |
| money_moving+rlm_ratio | early | 1-3k bets | 2-1 | 66.7 | 15.6 | 28.7 | -1.0 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.6 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 35.9 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 46.2 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 11-11 | 50.0 | 1.2 | -5.9 | 1.36 |
| consensus_gap+money_level | early | <1k bets | 18-15 | 54.5 | -11.0 | -19.3 | 0.26 |
| consensus_gap+sharp_gap | early | <1k bets | 13-24 | 35.1 | -14.6 | -14.5 | 0.63 |
| follow_move+money_level | early | <1k bets | 16-11 | 59.3 | 12.3 | 12.9 | 0.78 |
| follow_move+sharp_gap | early | <1k bets | 16-7 | 69.6 | 21.2 | 32.8 | 1.0 |
| money_level+sharp_gap | early | <1k bets | 51-25 | 67.1 | 10.5 | 9.5 | 0.65 |
| money_level+money_moving | early | <1k bets | 29-18 | 61.7 | 4.8 | -1.3 | 0.01 |
| money_moving+sharp_gap | early | <1k bets | 30-18 | 62.5 | 11.4 | 12.4 | 0.33 |
| consensus_gap+money_moving | early | <1k bets | 8-12 | 40.0 | -10.6 | -35.7 | -0.18 |
| follow_move+pin_value | early | <1k bets | 11-10 | 52.4 | 3.6 | -1.5 | 0.29 |
| follow_move+money_moving | early | <1k bets | 9-6 | 60.0 | 12.1 | 15.1 | 0.4 |
| consensus_gap+pin_value | early | <1k bets | 11-21 | 34.4 | -11.1 | -35.3 | 0.5 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -25.6 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -25.6 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | <1k bets | 1-1 | 50.0 | 24.4 | -3.7 | -2.15 |
| pin_value+sharp_gap | early | <1k bets | 4-3 | 57.1 | 11.6 | 9.1 | 0.03 |
| money_level+pin_value | early | <1k bets | 3-3 | 50.0 | 1.3 | -4.5 | 1.33 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -53.4 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -53.8 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 0-2 | 0.0 | -49.6 | -100.0 | 2.5 |
| follow_move+rlm_ratio | early | <1k bets | 3-1 | 75.0 | 22.9 | 44.2 | 0.0 |
| money_level+rlm_ratio | early | <1k bets | 2-0 | 100.0 | 46.2 | 93.0 | 0.5 |
| money_moving+rlm_ratio | early | <1k bets | 2-0 | 100.0 | 49.6 | 93.0 | -1.0 |
| rlm_ratio+sharp_gap | early | <1k bets | 3-1 | 75.0 | 22.9 | 44.2 | 0.0 |
| consensus_gap+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -53.8 | -100.0 | 1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 46.2 | 90.9 | 1.0 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 74.4 | 92.6 | 0.5 |
| consensus_gap+money_level | early | pin $1-2k | 4-4 | 50.0 | -14.1 | -22.9 | 0.44 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -31.9 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 4-9 | 30.8 | -8.4 | -42.5 | 0.4 |
| follow_move+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -3.1 | -1.0 | -0.5 |
| follow_move+sharp_gap | early | pin $1-2k | 3-1 | 75.0 | 25.0 | 45.0 | -0.25 |
| money_level+money_moving | early | pin $1-2k | 6-5 | 54.5 | -10.4 | -20.3 | 0.02 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.2 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 1-1 | 50.0 | -3.1 | -1.0 | -0.5 |
| money_level+sharp_gap | early | pin $1-2k | 8-4 | 66.7 | 4.4 | 8.4 | -0.41 |
| money_moving+sharp_gap | early | pin $1-2k | 3-5 | 37.5 | -21.3 | -45.3 | -0.06 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.5 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 2-2 | 50.0 | 0.0 | -8.4 | 0.75 |
| follow_move+money_level | early | pin $1-2k | 3-2 | 60.0 | 11.8 | 16.0 | 0.2 |
| follow_move+pin_value | early | pin $1-2k | 4-3 | 57.1 | 7.6 | 6.9 | 0.29 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 46.9 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 1-0 | 100.0 | 53.1 | 90.9 | 0.0 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.6 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -25.0 | -62.8 | -0.72 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -25.6 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -25.6 | -100.0 | -4.8 |
| money_level+money_moving | early | pin limit <$1k | 11-7 | 61.1 | 7.9 | 12.1 | 0.53 |
| money_level+sharp_gap | early | pin limit <$1k | 18-14 | 56.2 | 4.9 | 2.3 | 0.25 |
| money_moving+sharp_gap | early | pin limit <$1k | 16-5 | 76.2 | 28.0 | 68.0 | 0.39 |
| money_level+pin_value | early | pin limit <$1k | 8-5 | 61.5 | 10.1 | 16.6 | 0.46 |
| money_moving+pin_value | early | pin limit <$1k | 6-4 | 60.0 | 9.9 | 13.0 | 0.3 |
| pin_value+sharp_gap | early | pin limit <$1k | 11-5 | 68.8 | 18.2 | 30.3 | 0.06 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-7 | 46.2 | -1.0 | -14.2 | 0.46 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -27.1 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 13-17 | 43.3 | -4.8 | -18.8 | 0.49 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.5 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 8-7 | 53.3 | 3.4 | 1.9 | 0.07 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 5.1 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 9-7 | 56.2 | 6.1 | 6.9 | -0.31 |
| follow_move+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 27.7 | 53.6 | -0.4 |
| money_level+rlm_ratio | early | pin limit <$1k | 4-0 | 100.0 | 46.2 | 92.0 | 0.25 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.4 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 4-1 | 80.0 | 27.7 | 53.6 | -0.4 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 23.4 | 72.3 | 0.54 |
| follow_move+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 20.5 | 33.3 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.4 | 28.7 | -1.0 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -53.8 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -53.8 | -100.0 | 1.0 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.4 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 74.4 | 92.6 | 0.5 |
