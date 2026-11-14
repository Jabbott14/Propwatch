# CBB scorecard

Generated 2026-11-14 16:08 UTC. 416 graded games (10 finished games had no final score matched and are not graded).

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before tip. Break-even at -110 is 52.4%. CLV = points of closing-line
value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured
on this sample. `edge` is hit% minus that. A signal that is structurally long
favourites or overs beats 50% whenever those run, which is not an edge -- this
sample ran **47.2% favourites** (n=415) and **47.4% overs** (n=416) and **75.7% moneyline favourites** (n=346).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

## EARLY

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 1-1 | 50.0 | 24.3 | 25.7 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | both | 159-165 | 49.1 | 49.5 | -0.4 | -19.68 | -6.1 | 0.18 | 39.8 | no edge shown yet |
| rlm_ratio | both | 6-4 | 60.0 | 52.2 | 7.8 | +1.61 | 16.1 | -0.2 | 20.0 | keep collecting (10/30) |
| money_level | both | 94-52 | 64.4 | 59.0 | 5.4 | +4.46 | 3.1 | 0.42 | 43.8 | PROMOTE: beats break-even and its own base rate |
| sharp_gap | both | 76-61 | 55.5 | 47.6 | 7.8 | +20.57 | 15.0 | 0.43 | 42.3 | no edge shown yet |
| money_moving | both | 57-35 | 62.0 | 51.7 | 10.2 | +10.36 | 11.3 | 0.16 | 42.4 | PROMOTE: beats break-even and its own base rate |
| pin_value | both | 43-41 | 51.2 | 47.8 | 3.4 | -2.68 | -3.2 | 0.15 | 41.7 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.7 | -31.7 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 130-183 | 41.5 | 45.8 | -4.3 | -48.49 | -15.5 | 0.4 | 47.6 | DROP: below break-even |
| consensus_gap+money_level | both | 18-18 | 50.0 | 62.1 | -12.1 | -8.62 | -23.9 | 0.68 | 52.8 | no edge shown yet |
| consensus_gap+money_moving | both | 12-13 | 48.0 | 44.2 | 3.8 | +0.55 | 2.2 | 0.24 | 40.0 | keep collecting (25/30) |
| consensus_gap+pin_value | both | 17-26 | 39.5 | 45.5 | -5.9 | -11.16 | -26.0 | 0.46 | 53.5 | DROP: below break-even |
| follow_move+rlm_ratio | both | 6-4 | 60.0 | 52.2 | 7.8 | +1.61 | 16.1 | -0.2 | 20.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 24-15 | 61.5 | 49.5 | 12.0 | +6.83 | 17.5 | 0.44 | 38.5 | no edge shown yet |
| money_level+money_moving | both | 39-19 | 67.2 | 57.4 | 9.8 | +5.72 | 9.9 | 0.09 | 46.6 | PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | both | 10-8 | 55.6 | 50.3 | 5.3 | +0.9 | 5.0 | 0.5 | 50.0 | keep collecting (18/30) |
| money_moving+pin_value | both | 7-5 | 58.3 | 50.0 | 8.3 | +1.13 | 9.4 | 0.42 | 41.7 | keep collecting (12/30) |
| rlm_ratio+sharp_gap | both | 6-4 | 60.0 | 52.2 | 7.8 | +1.61 | 16.1 | -0.2 | 20.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 56-30 | 65.1 | 54.4 | 10.7 | +10.63 | 12.4 | 0.72 | 48.8 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 37-22 | 62.7 | 49.1 | 13.6 | +11.11 | 18.8 | 0.34 | 44.1 | PROMOTE: beats break-even and its own base rate |
| pin_value+sharp_gap | both | 12-7 | 63.2 | 48.9 | 14.2 | +3.75 | 19.8 | -0.15 | 36.8 | keep collecting (19/30) |
| consensus_gap+follow_move | both | 15-15 | 50.0 | 48.5 | 1.5 | -1.86 | -6.2 | 1.07 | 53.3 | no edge shown yet |
| consensus_gap+sharp_gap | both | 13-25 | 34.2 | 42.2 | -8.0 | +0.39 | 1.0 | 0.84 | 47.4 | DROP: below break-even |
| follow_move+money_level | both | 25-17 | 59.5 | 48.7 | 10.8 | +5.76 | 13.7 | 0.45 | 40.5 | no edge shown yet |
| follow_move+pin_value | both | 18-15 | 54.5 | 49.1 | 5.5 | +0.8 | 2.4 | 0.03 | 30.3 | no edge shown yet |
| money_level+rlm_ratio | both | 6-1 | 85.7 | 52.7 | 33.0 | +4.61 | 65.9 | 0.14 | 14.3 | keep collecting (7/30) |
| pin_value+rlm_ratio | both | 2-1 | 66.7 | 50.9 | 15.8 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| follow_move+money_moving | both | 17-8 | 68.0 | 49.0 | 19.0 | +7.52 | 30.1 | 0.16 | 36.0 | keep collecting (25/30) |
| money_moving+rlm_ratio | both | 3-1 | 75.0 | 51.4 | 23.6 | +1.81 | 45.3 | -0.75 | 0.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 24.3 | -24.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 24.3 | -24.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | both | 1-1 | 50.0 | 24.3 | 25.7 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 52.7 | -52.7 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 52.6 | -52.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 0-1 | 0.0 | 52.6 | -52.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 24.3 | 75.7 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-1 | 50.0 | 24.3 | 25.7 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | spread | 77-86 | 47.2 | 49.2 | -2.0 | -15.68 | -9.6 | 0.06 | 35.6 | no edge shown yet |
| follow_move | total | 82-79 | 50.9 | 49.7 | 1.2 | -4.0 | -2.5 | 0.3 | 44.1 | no edge shown yet |
| rlm_ratio | spread | 2-2 | 50.0 | 52.8 | -2.8 | -0.07 | -1.7 | -0.25 | 0.0 | keep collecting (4/30) |
| rlm_ratio | total | 4-2 | 66.7 | 51.8 | 14.9 | +1.68 | 28.0 | -0.17 | 33.3 | keep collecting (6/30) |
| money_level | moneyline | 47-19 | 71.2 | 71.0 | 0.2 | -5.17 | -7.8 | 0.39 | 50.0 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 16-14 | 53.3 | 48.9 | 4.4 | +0.4 | 1.3 | 0.87 | 46.7 | no edge shown yet |
| money_level | total | 31-19 | 62.0 | 49.2 | 12.8 | +9.22 | 18.4 | 0.18 | 34.0 | no edge shown yet |
| sharp_gap | moneyline | 30-27 | 52.6 | 44.1 | 8.5 | +12.79 | 22.4 | 0.46 | 52.6 | no edge shown yet |
| sharp_gap | spread | 17-14 | 54.8 | 49.9 | 4.9 | +1.35 | 4.4 | 0.65 | 35.5 | no edge shown yet |
| sharp_gap | total | 29-20 | 59.2 | 50.3 | 8.9 | +6.43 | 13.1 | 0.27 | 34.7 | no edge shown yet |
| money_moving | moneyline | 21-18 | 53.8 | 54.6 | -0.8 | -5.2 | -13.3 | 0.19 | 56.4 | no edge shown yet |
| money_moving | spread | 16-4 | 80.0 | 49.2 | 30.8 | +10.36 | 51.8 | 0.25 | 40.0 | keep collecting (20/30) |
| money_moving | total | 20-13 | 60.6 | 49.9 | 10.7 | +5.2 | 15.8 | 0.06 | 27.3 | no edge shown yet |
| pin_value | moneyline | 1-5 | 16.7 | 24.3 | -7.6 | -4.02 | -67.0 | -0.02 | 66.7 | keep collecting (6/30) |
| pin_value | spread | 22-17 | 56.4 | 49.2 | 7.2 | +2.35 | 6.0 | 0.28 | 41.0 | no edge shown yet |
| pin_value | total | 20-19 | 51.3 | 49.9 | 1.3 | -1.01 | -2.6 | 0.05 | 38.5 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.8 | -19.4 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 49-96 | 33.8 | 41.7 | -7.9 | -33.19 | -22.9 | 0.09 | 43.4 | DROP: below break-even |
| consensus_gap | spread | 43-40 | 51.8 | 49.2 | 2.6 | -2.52 | -3.0 | 0.57 | 48.2 | no edge shown yet |
| consensus_gap | total | 38-47 | 44.7 | 49.7 | -5.0 | -12.78 | -15.0 | 0.78 | 54.1 | no edge shown yet |
| money_level+sharp_gap | moneyline | 22-6 | 78.6 | 64.7 | 13.9 | +3.77 | 13.5 | 0.96 | 71.4 | keep collecting (28/30) |
| consensus_gap+pin_value | moneyline | 1-5 | 16.7 | 24.3 | -7.6 | -4.02 | -67.0 | -0.02 | 66.7 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_level+money_moving | moneyline | 15-7 | 68.2 | 71.0 | -2.9 | -4.19 | -19.0 | -0.35 | 54.5 | keep collecting (22/30) |
| consensus_gap+sharp_gap | moneyline | 7-16 | 30.4 | 37.7 | -7.3 | +4.17 | 18.1 | 0.86 | 52.2 | keep collecting (23/30) |
| consensus_gap+money_level | moneyline | 12-10 | 54.5 | 71.0 | -16.5 | -5.8 | -26.4 | 0.38 | 54.5 | keep collecting (22/30) |
| money_moving+sharp_gap | moneyline | 13-11 | 54.2 | 47.9 | 6.3 | +0.32 | 1.3 | 0.41 | 62.5 | keep collecting (24/30) |
| consensus_gap+money_moving | moneyline | 5-12 | 29.4 | 42.4 | -13.0 | -4.5 | -26.5 | 0.3 | 52.9 | keep collecting (17/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 24.3 | -24.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 24.3 | -24.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | moneyline | 1-1 | 50.0 | 24.3 | 25.7 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 24.3 | -24.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 24.3 | 75.7 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 4-5 | 44.4 | 47.2 | -2.8 | -1.59 | -17.7 | 1.67 | 66.7 | keep collecting (9/30) |
| consensus_gap+money_moving | spread | 4-0 | 100.0 | 47.2 | 52.8 | +3.41 | 85.2 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_value | spread | 9-8 | 52.9 | 48.2 | 4.7 | -0.31 | -1.8 | 0.53 | 52.9 | keep collecting (17/30) |
| follow_move+rlm_ratio | spread | 2-2 | 50.0 | 52.8 | -2.8 | -0.07 | -1.7 | -0.25 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 9-6 | 60.0 | 48.7 | 11.3 | +2.18 | 14.5 | 0.8 | 40.0 | keep collecting (15/30) |
| money_level+money_moving | spread | 9-4 | 69.2 | 48.5 | 20.7 | +4.21 | 32.4 | 0.77 | 61.5 | keep collecting (13/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.8 | -6.0 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.4 | 10.6 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | spread | 2-2 | 50.0 | 52.8 | -2.8 | -0.07 | -1.7 | -0.25 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 13-11 | 54.2 | 49.1 | 5.1 | +0.71 | 3.0 | 0.96 | 41.7 | keep collecting (24/30) |
| money_moving+sharp_gap | spread | 8-3 | 72.7 | 49.2 | 23.5 | +4.22 | 38.3 | 0.64 | 45.5 | keep collecting (11/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.1 | 17.6 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 8-8 | 50.0 | 47.9 | 2.1 | -1.18 | -7.4 | 0.94 | 43.8 | keep collecting (16/30) |
| consensus_gap+sharp_gap | spread | 3-3 | 50.0 | 47.2 | 2.8 | -0.43 | -7.1 | 2.17 | 66.7 | keep collecting (6/30) |
| follow_move+money_level | spread | 11-7 | 61.1 | 48.2 | 13.0 | +3.04 | 16.9 | 0.78 | 44.4 | keep collecting (18/30) |
| follow_move+pin_value | spread | 11-7 | 61.1 | 48.8 | 12.3 | +2.56 | 14.2 | 0.33 | 33.3 | keep collecting (18/30) |
| follow_move+money_moving | spread | 8-1 | 88.9 | 47.8 | 41.0 | +6.32 | 70.2 | 0.44 | 44.4 | keep collecting (9/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 52.8 | 13.9 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 1-0 | 100.0 | 52.8 | 47.2 | +0.95 | 95.2 | 0.0 | 0.0 | keep collecting (1/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 15-8 | 65.2 | 49.4 | 15.8 | +5.7 | 24.8 | 0.13 | 30.4 | keep collecting (23/30) |
| money_level+sharp_gap | total | 21-13 | 61.8 | 49.7 | 12.1 | +6.15 | 18.1 | 0.35 | 35.3 | no edge shown yet |
| money_moving+sharp_gap | total | 16-8 | 66.7 | 50.2 | 16.4 | +6.57 | 27.4 | 0.12 | 25.0 | keep collecting (24/30) |
| money_level+pin_value | total | 7-4 | 63.6 | 51.2 | 12.4 | +2.32 | 21.1 | 0.36 | 36.4 | keep collecting (11/30) |
| money_moving+pin_value | total | 4-3 | 57.1 | 50.4 | 6.8 | +0.56 | 8.0 | 0.29 | 28.6 | keep collecting (7/30) |
| pin_value+sharp_gap | total | 10-5 | 66.7 | 50.5 | 16.1 | +4.01 | 26.7 | 0.0 | 33.3 | keep collecting (15/30) |
| follow_move+money_level | total | 14-10 | 58.3 | 49.1 | 9.2 | +2.72 | 11.3 | 0.21 | 37.5 | keep collecting (24/30) |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.5 | -2.8 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 4-2 | 66.7 | 51.8 | 14.9 | +1.68 | 28.0 | -0.17 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 15-9 | 62.5 | 50.0 | 12.5 | +4.66 | 19.4 | 0.21 | 37.5 | keep collecting (24/30) |
| money_level+rlm_ratio | total | 4-0 | 100.0 | 52.6 | 47.4 | +3.68 | 92.0 | 0.25 | 25.0 | keep collecting (4/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 50.9 | 15.8 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 4-2 | 66.7 | 51.8 | 14.9 | +1.68 | 28.0 | -0.17 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 9-7 | 56.2 | 49.7 | 6.6 | +1.2 | 7.5 | 0.0 | 31.2 | keep collecting (16/30) |
| consensus_gap+money_level | total | 2-3 | 40.0 | 49.5 | -9.5 | -1.22 | -24.4 | 0.2 | 20.0 | keep collecting (5/30) |
| consensus_gap+money_moving | total | 3-1 | 75.0 | 48.7 | 26.3 | +1.65 | 41.2 | 0.0 | 0.0 | keep collecting (4/30) |
| consensus_gap+pin_value | total | 7-13 | 35.0 | 49.5 | -14.5 | -6.83 | -34.2 | 0.55 | 50.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | total | 3-6 | 33.3 | 50.3 | -17.0 | -3.35 | -37.2 | -0.11 | 22.2 | keep collecting (9/30) |
| money_moving+rlm_ratio | total | 2-1 | 66.7 | 50.9 | 15.8 | +0.86 | 28.7 | -1.0 | 0.0 | keep collecting (3/30) |
| consensus_gap+follow_move | total | 7-7 | 50.0 | 49.2 | 0.8 | -0.67 | -4.8 | 1.21 | 64.3 | keep collecting (14/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 52.6 | -52.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 52.6 | -52.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 0-1 | 0.0 | 52.6 | -52.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |

## CLOSE

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 78-84 | 48.1 | 42.7 | 5.4 | +21.65 | 13.4 |  |  | no edge shown yet |
| follow_move | both | 342-350 | 49.4 | 49.5 | -0.0 | -40.04 | -5.8 |  |  | DROP: below break-even |
| rlm_ratio | both | 97-79 | 55.1 | 50.9 | 4.2 | +9.24 | 5.3 |  |  | no edge shown yet |
| money_level | both | 640-493 | 56.5 | 55.9 | 0.6 | -69.29 | -6.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 483-609 | 44.2 | 46.8 | -2.6 | -97.77 | -9.0 |  |  | DROP: below break-even |
| money_moving | both | 482-610 | 44.1 | 47.2 | -3.1 | -109.06 | -10.0 |  |  | DROP: below break-even |
| pin_value | both | 221-214 | 50.8 | 47.4 | 3.4 | +7.7 | 1.8 |  |  | no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 50.9 | 15.7 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 229-329 | 41.0 | 45.7 | -4.6 | -63.62 | -11.4 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 55-50 | 52.4 | 47.9 | 4.5 | -2.43 | -2.3 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 96-184 | 34.3 | 42.4 | -8.2 | -27.04 | -9.7 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 16-26 | 38.1 | 36.8 | 1.3 | +13.34 | 31.8 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 95-111 | 46.1 | 44.4 | 1.7 | -2.92 | -1.4 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | both | 14-11 | 56.0 | 48.8 | 7.2 | +1.2 | 4.8 |  |  | keep collecting (25/30) |
| consensus_gap+sharp_gap | both | 97-188 | 34.0 | 42.1 | -8.1 | -27.87 | -9.8 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 218-247 | 46.9 | 49.5 | -2.6 | -50.09 | -10.8 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 52-41 | 55.9 | 51.4 | 4.5 | +6.6 | 7.1 |  |  | no edge shown yet |
| follow_move+pin_value | both | 83-70 | 54.2 | 48.9 | 5.3 | +3.4 | 2.2 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 97-79 | 55.1 | 50.9 | 4.2 | +9.24 | 5.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 222-244 | 47.6 | 49.6 | -1.9 | -43.23 | -9.3 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 75-84 | 47.2 | 42.5 | 4.6 | +18.91 | 11.9 |  |  | no edge shown yet |
| money_moving+pin_value | both | 91-116 | 44.0 | 46.0 | -2.1 | -12.74 | -6.2 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 94-78 | 54.7 | 50.9 | 3.8 | +7.4 | 4.3 |  |  | no edge shown yet |
| money_moving+sharp_gap | both | 465-590 | 44.1 | 46.9 | -2.9 | -98.12 | -9.3 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 25-23 | 52.1 | 45.8 | 6.3 | +13.07 | 27.2 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 52-41 | 55.9 | 51.4 | 4.5 | +6.6 | 7.1 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 78-84 | 48.1 | 42.7 | 5.4 | +21.65 | 13.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 24-19 | 55.8 | 50.3 | 5.5 | +2.49 | 5.8 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 93-116 | 44.5 | 46.1 | -1.6 | -10.99 | -5.3 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 97-79 | 55.1 | 50.9 | 4.2 | +9.24 | 5.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+money_moving | both | 335-334 | 50.1 | 52.2 | -2.1 | -57.97 | -8.7 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 332-330 | 50.2 | 51.9 | -1.8 | -51.1 | -7.7 |  |  | no edge shown yet |
| follow_move+money_level | both | 198-219 | 47.5 | 48.8 | -1.3 | -40.82 | -9.8 |  |  | DROP: below break-even |
| money_level+rlm_ratio | both | 47-41 | 53.4 | 50.5 | 2.9 | +1.44 | 1.6 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 139-118 | 54.1 | 56.9 | -2.8 | -16.41 | -6.4 |  |  | no edge shown yet |
| money_level+pin_value | both | 100-102 | 49.5 | 48.9 | 0.6 | -15.68 | -7.8 |  |  | no edge shown yet |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | both | 33-25 | 56.9 | 48.5 | 8.4 | +6.77 | 11.7 |  |  | no edge shown yet |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 52.6 | 47.4 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 19-37 | 33.9 | 26.1 | 7.8 | +14.85 | 26.5 |  |  | DROP: below break-even |
| pin_rlm | spread | 15-16 | 48.4 | 51.2 | -2.8 | -2.43 | -7.8 |  |  | no edge shown yet |
| pin_rlm | total | 44-31 | 58.7 | 51.7 | 7.0 | +9.23 | 12.3 |  |  | no edge shown yet |
| follow_move | spread | 158-163 | 49.2 | 49.0 | 0.3 | -20.62 | -6.4 |  |  | no edge shown yet |
| follow_move | total | 184-187 | 49.6 | 49.9 | -0.3 | -19.42 | -5.2 |  |  | no edge shown yet |
| rlm_ratio | spread | 26-29 | 47.3 | 50.3 | -3.0 | -5.47 | -9.9 |  |  | no edge shown yet |
| rlm_ratio | total | 71-50 | 58.7 | 51.2 | 7.4 | +14.71 | 12.2 |  |  | no edge shown yet |
| money_level | moneyline | 256-84 | 75.3 | 71.8 | 3.5 | -6.7 | -2.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 190-196 | 49.2 | 48.8 | 0.4 | -25.62 | -6.6 |  |  | no edge shown yet |
| money_level | total | 194-213 | 47.7 | 49.3 | -1.7 | -36.98 | -9.1 |  |  | DROP: below break-even |
| sharp_gap | moneyline | 103-208 | 33.1 | 39.0 | -5.9 | -40.9 | -13.2 |  |  | DROP: below break-even |
| sharp_gap | spread | 193-187 | 50.8 | 49.5 | 1.3 | -13.44 | -3.5 |  |  | no edge shown yet |
| sharp_gap | total | 187-214 | 46.6 | 50.3 | -3.7 | -43.43 | -10.8 |  |  | DROP: below break-even |
| money_moving | moneyline | 109-200 | 35.3 | 40.4 | -5.2 | -36.69 | -11.9 |  |  | DROP: below break-even |
| money_moving | spread | 190-190 | 50.0 | 49.4 | 0.6 | -19.31 | -5.1 |  |  | no edge shown yet |
| money_moving | total | 183-220 | 45.4 | 50.3 | -4.9 | -53.06 | -13.2 |  |  | DROP: below break-even |
| pin_value | moneyline | 10-34 | 22.7 | 27.8 | -5.1 | +0.34 | 0.8 |  |  | DROP: below break-even |
| pin_value | spread | 107-81 | 56.9 | 49.6 | 7.3 | +12.96 | 6.9 |  |  | no edge shown yet |
| pin_value | total | 104-99 | 51.2 | 49.5 | 1.7 | -5.6 | -2.8 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.8 | 47.2 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 89-193 | 31.6 | 42.7 | -11.1 | -49.64 | -17.6 |  |  | DROP: below break-even |
| consensus_gap | spread | 68-52 | 56.7 | 49.0 | 7.7 | +6.09 | 5.1 |  |  | no edge shown yet |
| consensus_gap | total | 72-84 | 46.2 | 48.5 | -2.3 | -20.07 | -12.9 |  |  | DROP: below break-even |
| money_level+money_moving | moneyline | 75-45 | 62.5 | 65.4 | -2.9 | -3.39 | -2.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 68-44 | 60.7 | 64.7 | -4.0 | -3.17 | -2.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 98-195 | 33.4 | 39.2 | -5.8 | -35.34 | -12.1 |  |  | DROP: below break-even |
| consensus_gap+money_level | moneyline | 62-38 | 62.0 | 70.6 | -8.6 | -3.36 | -3.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 31-114 | 21.4 | 36.7 | -15.3 | -13.4 | -9.2 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+sharp_gap | moneyline | 32-119 | 21.2 | 36.2 | -15.0 | -15.24 | -10.1 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_rlm | moneyline | 8-17 | 32.0 | 28.4 | 3.6 | +15.43 | 61.7 |  |  | keep collecting (25/30) |
| money_moving+pin_rlm | moneyline | 19-37 | 33.9 | 26.1 | 7.8 | +14.85 | 26.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 19-37 | 33.9 | 26.1 | 7.8 | +14.85 | 26.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 10-32 | 23.8 | 28.0 | -4.1 | +2.34 | 5.6 |  |  | DROP: below break-even |
| money_moving+pin_value | moneyline | 5-23 | 17.9 | 24.3 | -6.4 | +4.55 | 16.3 |  |  | keep collecting (28/30) |
| pin_rlm+pin_value | moneyline | 3-6 | 33.3 | 24.3 | 9.1 | +10.35 | 115.0 |  |  | keep collecting (9/30) |
| pin_value+sharp_gap | moneyline | 5-24 | 17.2 | 24.3 | -7.0 | +3.55 | 12.2 |  |  | keep collecting (29/30) |
| money_level+pin_rlm | moneyline | 5-3 | 62.5 | 30.7 | 31.8 | +3.4 | 42.5 |  |  | keep collecting (8/30) |
| money_level+pin_value | moneyline | 3-1 | 75.0 | 62.9 | 12.1 | +0.31 | 7.8 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 29-19 | 60.4 | 47.8 | 12.6 | +5.69 | 11.8 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 37-29 | 56.1 | 48.8 | 7.2 | +2.61 | 4.0 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 46-31 | 59.7 | 49.0 | 10.8 | +8.15 | 10.6 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.33 | -38.9 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | spread | 36-29 | 55.4 | 49.1 | 6.3 | +1.72 | 2.6 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 99-104 | 48.8 | 48.7 | 0.1 | -15.29 | -7.5 |  |  | no edge shown yet |
| follow_move+pin_rlm | spread | 13-15 | 46.4 | 51.0 | -4.6 | -3.19 | -11.4 |  |  | keep collecting (28/30) |
| follow_move+pin_value | spread | 41-30 | 57.7 | 48.4 | 9.3 | +5.79 | 8.1 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 26-29 | 47.3 | 50.3 | -3.0 | -5.47 | -9.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 100-103 | 49.3 | 48.8 | 0.5 | -13.16 | -6.5 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 13-16 | 44.8 | 51.1 | -6.2 | -4.26 | -14.7 |  |  | keep collecting (29/30) |
| money_moving+pin_value | spread | 49-44 | 52.7 | 49.1 | 3.6 | -1.54 | -1.7 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 24-28 | 46.2 | 50.1 | -4.0 | -6.4 | -12.3 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 185-182 | 50.4 | 49.4 | 1.0 | -15.81 | -4.3 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 6-7 | 46.2 | 50.2 | -4.1 | -1.79 | -13.8 |  |  | keep collecting (13/30) |
| pin_rlm+rlm_ratio | spread | 13-15 | 46.4 | 51.0 | -4.6 | -3.19 | -11.4 |  |  | keep collecting (28/30) |
| pin_rlm+sharp_gap | spread | 15-16 | 48.4 | 51.2 | -2.8 | -2.43 | -7.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 4-6 | 40.0 | 49.4 | -9.4 | -2.55 | -25.5 |  |  | keep collecting (10/30) |
| pin_value+sharp_gap | spread | 49-44 | 52.7 | 49.3 | 3.4 | -1.6 | -1.7 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 26-29 | 47.3 | 50.3 | -3.0 | -5.47 | -9.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 100-103 | 49.3 | 48.3 | 1.0 | -13.6 | -6.7 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 13-14 | 48.1 | 49.7 | -1.5 | -2.41 | -8.9 |  |  | keep collecting (27/30) |
| money_level+sharp_gap | spread | 146-143 | 50.5 | 48.9 | 1.6 | -12.17 | -4.2 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 45-33 | 57.7 | 48.5 | 9.2 | +5.58 | 7.1 |  |  | no edge shown yet |
| money_level+money_moving | spread | 145-144 | 50.2 | 48.9 | 1.3 | -14.09 | -4.9 |  |  | no edge shown yet |
| money_level+pin_value | spread | 54-48 | 52.9 | 48.7 | 4.2 | -1.35 | -1.3 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 8-6 | 57.1 | 50.4 | 6.7 | +1.1 | 7.9 |  |  | keep collecting (14/30) |
| money_level+money_moving | total | 115-145 | 44.2 | 49.7 | -5.5 | -40.49 | -15.6 |  |  | DROP: below break-even |
| money_level+sharp_gap | total | 118-143 | 45.2 | 49.7 | -4.5 | -35.76 | -13.7 |  |  | DROP: below break-even |
| money_moving+sharp_gap | total | 182-213 | 46.1 | 50.3 | -4.3 | -46.97 | -11.9 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 32-47 | 40.5 | 47.8 | -7.3 | -18.62 | -23.6 |  |  | DROP: below break-even |
| consensus_gap+pin_value | total | 39-48 | 44.8 | 48.4 | -3.6 | -13.41 | -15.4 |  |  | no edge shown yet |
| follow_move+money_moving | total | 119-143 | 45.4 | 50.1 | -4.7 | -34.8 | -13.3 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 122-141 | 46.4 | 50.2 | -3.8 | -30.08 | -11.4 |  |  | DROP: below break-even |
| money_level+pin_value | total | 43-53 | 44.8 | 48.6 | -3.8 | -14.64 | -15.2 |  |  | no edge shown yet |
| follow_move+money_level | total | 98-116 | 45.8 | 49.3 | -3.5 | -27.22 | -12.7 |  |  | DROP: below break-even |
| follow_move+pin_value | total | 42-40 | 51.2 | 49.4 | 1.8 | -2.38 | -2.9 |  |  | no edge shown yet |
| money_moving+pin_value | total | 37-49 | 43.0 | 49.8 | -6.8 | -15.76 | -18.3 |  |  | DROP: below break-even |
| pin_value+sharp_gap | total | 39-48 | 44.8 | 49.9 | -5.1 | -12.94 | -14.9 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 28-41 | 40.6 | 48.4 | -7.8 | -16.25 | -23.6 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | total | 29-40 | 42.0 | 48.5 | -6.5 | -14.34 | -20.8 |  |  | DROP: below break-even |
| consensus_gap+follow_move | total | 26-31 | 45.6 | 48.0 | -2.4 | -8.12 | -14.2 |  |  | no edge shown yet |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pin_rlm | total | 5-6 | 45.5 | 48.8 | -3.3 | -1.6 | -14.6 |  |  | keep collecting (11/30) |
| consensus_gap+rlm_ratio | total | 12-7 | 63.2 | 48.5 | 14.7 | +3.53 | 18.6 |  |  | keep collecting (19/30) |
| follow_move+pin_rlm | total | 39-26 | 60.0 | 51.6 | 8.4 | +9.79 | 15.1 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 71-50 | 58.7 | 51.2 | 7.4 | +14.71 | 12.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 20-16 | 55.6 | 51.8 | 3.8 | +2.26 | 6.3 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 34-27 | 55.7 | 50.9 | 4.8 | +3.85 | 6.3 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 43-31 | 58.1 | 51.6 | 6.5 | +8.32 | 11.2 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 70-50 | 58.3 | 51.2 | 7.1 | +13.8 | 11.5 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 16-10 | 61.5 | 51.0 | 10.5 | +4.51 | 17.3 |  |  | keep collecting (26/30) |
| pin_rlm+rlm_ratio | total | 39-26 | 60.0 | 51.6 | 8.4 | +9.79 | 15.1 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 44-31 | 58.7 | 51.7 | 7.0 | +9.23 | 12.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 20-13 | 60.6 | 50.6 | 10.0 | +5.03 | 15.3 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 71-50 | 58.7 | 51.2 | 7.4 | +14.71 | 12.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 52.6 | 47.4 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_rlm | close | 1-3k bets | 47-54 | 46.5 | 3.1 | 14.2 |  |
| pin_rlm | close | 3k+ bets | 20-21 | 48.8 | 7.9 | 8.7 |  |
| pin_rlm | close | <1k bets | 11-9 | 55.0 | 11.7 | 18.6 |  |
| pin_rlm | close | pin $1-2k | 38-30 | 55.9 | 10.7 | 32.7 |  |
| pin_rlm | close | pin $2k+ | 14-41 | 25.5 | -8.9 | -36.9 |  |
| pin_rlm | close | pin limit <$1k | 26-13 | 66.7 | 16.4 | 50.5 |  |
| follow_move | close | 1-3k bets | 227-222 | 50.6 | 1.1 | -3.6 |  |
| follow_move | close | 3k+ bets | 78-88 | 47.0 | -2.4 | -10.4 |  |
| follow_move | close | <1k bets | 37-40 | 48.1 | -1.3 | -8.5 |  |
| follow_move | close | pin $1-2k | 108-142 | 43.2 | -6.1 | -17.7 |  |
| follow_move | close | pin $2k+ | 63-63 | 50.0 | 0.4 | -4.6 |  |
| follow_move | close | pin limit <$1k | 73-61 | 54.5 | 4.4 | 4.1 |  |
| rlm_ratio | close | 1-3k bets | 66-58 | 53.2 | 2.3 | 1.5 |  |
| rlm_ratio | close | 3k+ bets | 24-16 | 60.0 | 9.0 | 14.9 |  |
| rlm_ratio | close | <1k bets | 7-5 | 58.3 | 7.5 | 11.9 |  |
| rlm_ratio | close | pin $1-2k | 34-31 | 52.3 | 2.0 | -0.5 |  |
| rlm_ratio | close | pin $2k+ | 11-14 | 44.0 | -7.4 | -15.9 |  |
| rlm_ratio | close | pin limit <$1k | 27-16 | 62.8 | 11.1 | 20.6 |  |
| money_level | close | 1-3k bets | 423-294 | 59.0 | 3.0 | -1.8 |  |
| money_level | close | 3k+ bets | 149-130 | 53.4 | -2.5 | -9.2 |  |
| money_level | close | <1k bets | 68-68 | 50.0 | -5.9 | -21.6 |  |
| money_level | close | pin $1-2k | 180-166 | 52.0 | -1.9 | -8.1 |  |
| money_level | close | pin $2k+ | 155-125 | 55.4 | -2.6 | -9.8 |  |
| money_level | close | pin limit <$1k | 71-81 | 46.7 | -2.9 | -11.6 |  |
| sharp_gap | close | 1-3k bets | 300-390 | 43.5 | -3.2 | -11.3 |  |
| sharp_gap | close | 3k+ bets | 129-145 | 47.1 | 0.4 | 2.2 |  |
| sharp_gap | close | <1k bets | 54-73 | 42.5 | -5.3 | -19.7 |  |
| sharp_gap | close | pin $1-2k | 159-179 | 47.0 | -1.6 | -4.6 |  |
| sharp_gap | close | pin $2k+ | 109-161 | 40.4 | -5.3 | -18.2 |  |
| sharp_gap | close | pin limit <$1k | 70-76 | 47.9 | -2.4 | -2.1 |  |
| money_moving | close | 1-3k bets | 300-389 | 43.5 | -3.5 | -12.0 |  |
| money_moving | close | 3k+ bets | 128-148 | 46.4 | -0.8 | -0.6 |  |
| money_moving | close | <1k bets | 54-72 | 42.9 | -5.1 | -19.1 |  |
| money_moving | close | pin $1-2k | 154-184 | 45.6 | -3.2 | -7.6 |  |
| money_moving | close | pin $2k+ | 112-157 | 41.6 | -4.2 | -16.2 |  |
| money_moving | close | pin limit <$1k | 69-78 | 46.9 | -3.2 | -4.0 |  |
| pin_value | close | 1-3k bets | 133-139 | 48.9 | 1.4 | -1.7 |  |
| pin_value | close | 3k+ bets | 51-56 | 47.7 | 0.4 | -4.2 |  |
| pin_value | close | <1k bets | 37-19 | 66.1 | 19.3 | 30.3 |  |
| pin_value | close | pin $1-2k | 105-104 | 50.2 | 2.5 | -1.0 |  |
| pin_value | close | pin $2k+ | 61-64 | 48.8 | 3.2 | 1.7 |  |
| pin_value | close | pin limit <$1k | 55-46 | 54.5 | 5.6 | 7.5 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.2 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.2 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 145-204 | 41.5 | -4.5 | -12.8 |  |
| consensus_gap | close | 3k+ bets | 57-75 | 43.2 | -3.4 | 1.1 |  |
| consensus_gap | close | <1k bets | 27-49 | 35.5 | -7.0 | -25.4 |  |
| consensus_gap | close | pin $1-2k | 74-87 | 46.0 | -1.5 | 0.6 |  |
| consensus_gap | close | pin $2k+ | 57-69 | 45.2 | -4.6 | -14.6 |  |
| consensus_gap | close | pin limit <$1k | 35-35 | 50.0 | 1.7 | -0.4 |  |
| consensus_gap+follow_move | close | 1-3k bets | 40-30 | 57.1 | 9.2 | 6.8 |  |
| consensus_gap+money_level | close | 1-3k bets | 96-66 | 59.3 | 1.7 | 4.2 |  |
| consensus_gap+money_moving | close | 1-3k bets | 63-117 | 35.0 | -7.7 | -11.8 |  |
| consensus_gap+pin_value | close | 1-3k bets | 59-73 | 44.7 | -0.0 | -4.1 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 63-120 | 34.4 | -7.9 | -13.1 |  |
| follow_move+money_level | close | 1-3k bets | 139-139 | 50.0 | 1.2 | -4.9 |  |
| follow_move+money_moving | close | 1-3k bets | 153-164 | 48.3 | -1.3 | -8.1 |  |
| follow_move+pin_value | close | 1-3k bets | 49-43 | 53.3 | 4.4 | 0.3 |  |
| follow_move+sharp_gap | close | 1-3k bets | 153-162 | 48.6 | -1.0 | -7.5 |  |
| money_level+money_moving | close | 1-3k bets | 215-203 | 51.4 | -0.7 | -4.6 |  |
| money_level+pin_value | close | 1-3k bets | 64-63 | 50.4 | 1.5 | -5.7 |  |
| money_level+sharp_gap | close | 1-3k bets | 213-202 | 51.3 | -0.5 | -4.0 |  |
| money_moving+pin_value | close | 1-3k bets | 58-78 | 42.6 | -3.5 | -9.9 |  |
| money_moving+sharp_gap | close | 1-3k bets | 290-379 | 43.3 | -3.5 | -11.5 |  |
| pin_value+sharp_gap | close | 1-3k bets | 60-80 | 42.9 | -3.3 | -9.9 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 11-18 | 37.9 | 0.6 | 37.1 |  |
| money_level+pin_rlm | close | 1-3k bets | 22-17 | 56.4 | 5.0 | 7.8 |  |
| pin_rlm+pin_value | close | 1-3k bets | 16-16 | 50.0 | 5.2 | 37.2 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 47-54 | 46.5 | 3.1 | 14.2 |  |
| money_moving+pin_rlm | close | 1-3k bets | 45-54 | 45.5 | 2.3 | 12.7 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 13-7 | 65.0 | 16.1 | 21.6 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 66-58 | 53.2 | 2.3 | 1.5 |  |
| money_level+rlm_ratio | close | 1-3k bets | 33-30 | 52.4 | 1.8 | -0.3 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 65-58 | 52.8 | 1.9 | 0.8 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 66-58 | 53.2 | 2.3 | 1.5 |  |
| follow_move+pin_rlm | close | 1-3k bets | 31-28 | 52.5 | 1.1 | 0.3 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 31-28 | 52.5 | 1.1 | 0.3 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 16-13 | 55.2 | 5.1 | 4.3 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 47.4 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 13-13 | 50.0 | 1.9 | -7.0 |  |
| consensus_gap+money_moving | close | 3k+ bets | 22-43 | 33.8 | -8.4 | 8.4 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-5 | 37.5 | -2.5 | 19.3 |  |
| consensus_gap+pin_value | close | 3k+ bets | 27-29 | 48.2 | 3.6 | 1.4 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 1-3 | 25.0 | -23.7 | -53.2 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 23-43 | 34.8 | -7.3 | 12.6 |  |
| follow_move+money_moving | close | 3k+ bets | 49-56 | 46.7 | -2.8 | -11.2 |  |
| follow_move+pin_rlm | close | 3k+ bets | 14-10 | 58.3 | 7.0 | 12.4 |  |
| follow_move+pin_value | close | 3k+ bets | 20-23 | 46.5 | -2.5 | -12.8 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 24-16 | 60.0 | 9.0 | 14.9 |  |
| follow_move+sharp_gap | close | 3k+ bets | 53-55 | 49.1 | -0.5 | -6.5 |  |
| money_moving+pin_rlm | close | 3k+ bets | 19-21 | 47.5 | 7.0 | 6.5 |  |
| money_moving+pin_value | close | 3k+ bets | 24-31 | 43.6 | -1.9 | -5.0 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 22-15 | 59.5 | 8.6 | 13.6 |  |
| money_moving+sharp_gap | close | 3k+ bets | 121-138 | 46.7 | -0.1 | 1.4 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-6 | 45.5 | -0.6 | -13.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 14-10 | 58.3 | 7.0 | 12.4 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 20-21 | 48.8 | 7.9 | 8.7 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 5-5 | 50.0 | -0.6 | -5.2 |  |
| pin_value+sharp_gap | close | 3k+ bets | 24-29 | 45.3 | -0.2 | -1.4 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 24-16 | 60.0 | 9.0 | 14.9 |  |
| money_level+money_moving | close | 3k+ bets | 85-85 | 50.0 | -2.2 | -8.8 |  |
| money_level+sharp_gap | close | 3k+ bets | 84-82 | 50.6 | -1.2 | -6.6 |  |
| follow_move+money_level | close | 3k+ bets | 46-51 | 47.4 | -1.3 | -9.9 |  |
| money_level+rlm_ratio | close | 3k+ bets | 13-7 | 65.0 | 14.4 | 23.6 |  |
| consensus_gap+money_level | close | 3k+ bets | 31-33 | 48.4 | -8.0 | -17.8 |  |
| money_level+pin_value | close | 3k+ bets | 24-31 | 43.6 | -5.0 | -19.5 |  |
| money_level+pin_rlm | close | 3k+ bets | 8-6 | 57.1 | 13.7 | 17.5 |  |
| money_level+money_moving | close | <1k bets | 35-45 | 43.8 | -9.1 | -28.3 |  |
| money_level+sharp_gap | close | <1k bets | 35-45 | 43.8 | -9.1 | -28.3 |  |
| money_moving+sharp_gap | close | <1k bets | 54-72 | 42.9 | -5.1 | -19.1 |  |
| consensus_gap+money_level | close | <1k bets | 12-19 | 38.7 | -15.5 | -38.2 |  |
| consensus_gap+money_moving | close | <1k bets | 11-24 | 31.4 | -10.0 | -32.1 |  |
| consensus_gap+pin_value | close | <1k bets | 9-9 | 50.0 | 8.2 | 9.5 |  |
| consensus_gap+sharp_gap | close | <1k bets | 11-25 | 30.6 | -10.4 | -34.0 |  |
| money_level+pin_value | close | <1k bets | 12-8 | 60.0 | 10.2 | 11.4 |  |
| money_moving+pin_value | close | <1k bets | 9-7 | 56.2 | 9.5 | 22.1 |  |
| pin_value+sharp_gap | close | <1k bets | 9-7 | 56.2 | 9.5 | 22.1 |  |
| follow_move+money_moving | close | <1k bets | 16-27 | 37.2 | -11.9 | -29.2 |  |
| follow_move+sharp_gap | close | <1k bets | 16-27 | 37.2 | -11.9 | -29.2 |  |
| follow_move+money_level | close | <1k bets | 13-29 | 31.0 | -17.6 | -41.5 |  |
| consensus_gap+pin_rlm | close | <1k bets | 2-3 | 40.0 | 11.1 | 20.4 |  |
| money_moving+pin_rlm | close | <1k bets | 11-9 | 55.0 | 11.7 | 18.6 |  |
| pin_rlm+sharp_gap | close | <1k bets | 11-9 | 55.0 | 11.7 | 18.6 |  |
| consensus_gap+follow_move | close | <1k bets | 2-7 | 22.2 | -25.0 | -59.3 |  |
| follow_move+pin_rlm | close | <1k bets | 7-3 | 70.0 | 19.0 | 34.3 |  |
| follow_move+pin_value | close | <1k bets | 14-4 | 77.8 | 28.4 | 48.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 7-5 | 58.3 | 7.5 | 11.9 |  |
| money_moving+rlm_ratio | close | <1k bets | 7-5 | 58.3 | 7.5 | 11.9 |  |
| pin_rlm+pin_value | close | <1k bets | 4-1 | 80.0 | 28.4 | 53.3 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 7-3 | 70.0 | 19.0 | 34.3 |  |
| pin_value+rlm_ratio | close | <1k bets | 3-1 | 75.0 | 23.7 | 43.9 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 7-5 | 58.3 | 7.5 | 11.9 |  |
| money_level+rlm_ratio | close | <1k bets | 1-4 | 20.0 | -30.5 | -62.1 |  |
| money_level+pin_rlm | close | <1k bets | 3-2 | 60.0 | 19.8 | 25.5 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 0-1 | 0.0 | -47.4 | -100.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 20-20 | 50.0 | 2.0 | -6.8 |  |
| consensus_gap+money_moving | close | pin $1-2k | 37-51 | 42.0 | -4.7 | -4.9 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 11-13 | 45.8 | 5.8 | 46.6 |  |
| consensus_gap+pin_value | close | pin $1-2k | 45-52 | 46.4 | 1.7 | -4.4 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 8-6 | 57.1 | 8.7 | 6.4 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 37-48 | 43.5 | -2.9 | -1.5 |  |
| follow_move+money_moving | close | pin $1-2k | 75-104 | 41.9 | -7.4 | -20.3 |  |
| follow_move+pin_rlm | close | pin $1-2k | 25-19 | 56.8 | 5.7 | 8.6 |  |
| follow_move+pin_value | close | pin $1-2k | 38-41 | 48.1 | -1.0 | -9.6 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 34-31 | 52.3 | 2.0 | -0.5 |  |
| follow_move+sharp_gap | close | pin $1-2k | 77-102 | 43.0 | -6.3 | -18.1 |  |
| money_moving+pin_rlm | close | pin $1-2k | 36-30 | 54.5 | 9.6 | 31.0 |  |
| money_moving+pin_value | close | pin $1-2k | 40-56 | 41.7 | -5.1 | -16.2 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 33-30 | 52.4 | 2.1 | -0.5 |  |
| money_moving+sharp_gap | close | pin $1-2k | 153-178 | 46.2 | -2.4 | -6.2 |  |
| pin_rlm+pin_value | close | pin $1-2k | 10-14 | 41.7 | -6.6 | -9.3 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 25-19 | 56.8 | 5.7 | 8.6 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 38-30 | 55.9 | 10.7 | 32.7 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 12-13 | 48.0 | -1.7 | -9.9 |  |
| pin_value+sharp_gap | close | pin $1-2k | 40-54 | 42.6 | -4.2 | -14.4 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 34-31 | 52.3 | 2.0 | -0.5 |  |
| follow_move+money_level | close | pin $1-2k | 73-95 | 43.5 | -5.3 | -17.4 |  |
| money_level+rlm_ratio | close | pin $1-2k | 21-17 | 55.3 | 5.4 | 4.7 |  |
| money_level+sharp_gap | close | pin $1-2k | 117-123 | 48.8 | -2.8 | -9.3 |  |
| money_level+money_moving | close | pin $1-2k | 115-126 | 47.7 | -3.9 | -11.2 |  |
| consensus_gap+money_level | close | pin $1-2k | 42-39 | 51.9 | -4.0 | -8.3 |  |
| money_level+pin_value | close | pin $1-2k | 43-46 | 48.3 | -0.9 | -9.8 |  |
| money_level+pin_rlm | close | pin $1-2k | 20-12 | 62.5 | 14.0 | 24.1 |  |
| follow_move+money_level | close | pin $2k+ | 34-34 | 50.0 | 1.3 | -5.0 |  |
| follow_move+money_moving | close | pin $2k+ | 38-40 | 48.7 | -0.9 | -7.2 |  |
| follow_move+sharp_gap | close | pin $2k+ | 39-40 | 49.4 | -0.2 | -5.9 |  |
| money_level+money_moving | close | pin $2k+ | 72-79 | 47.7 | -5.3 | -13.2 |  |
| money_level+sharp_gap | close | pin $2k+ | 71-81 | 46.7 | -6.2 | -14.2 |  |
| money_moving+sharp_gap | close | pin $2k+ | 107-156 | 40.7 | -4.9 | -17.3 |  |
| consensus_gap+money_moving | close | pin $2k+ | 18-42 | 30.0 | -12.4 | -24.4 |  |
| consensus_gap+pin_value | close | pin $2k+ | 27-31 | 46.6 | 5.5 | 8.0 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 19-45 | 29.7 | -14.0 | -26.9 |  |
| money_moving+pin_value | close | pin $2k+ | 29-38 | 43.3 | -0.1 | 0.9 |  |
| pin_value+sharp_gap | close | pin $2k+ | 29-39 | 42.6 | -0.5 | -0.6 |  |
| consensus_gap+follow_move | close | pin $2k+ | 7-4 | 63.6 | 15.9 | 17.6 |  |
| follow_move+pin_value | close | pin $2k+ | 20-13 | 60.6 | 11.9 | 14.1 |  |
| follow_move+pin_rlm | close | pin $2k+ | 6-13 | 31.6 | -20.3 | -39.5 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 11-14 | 44.0 | -7.4 | -15.9 |  |
| money_level+pin_rlm | close | pin $2k+ | 4-7 | 36.4 | -7.6 | -28.9 |  |
| money_level+pin_value | close | pin $2k+ | 30-29 | 50.8 | 1.7 | -6.5 |  |
| money_level+rlm_ratio | close | pin $2k+ | 5-6 | 45.5 | -5.8 | -13.1 |  |
| money_moving+pin_rlm | close | pin $2k+ | 14-41 | 25.5 | -8.9 | -36.9 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 11-14 | 44.0 | -7.4 | -15.9 |  |
| pin_rlm+pin_value | close | pin $2k+ | 3-7 | 30.0 | -5.7 | 19.5 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 6-13 | 31.6 | -20.3 | -39.5 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 14-41 | 25.5 | -8.9 | -36.9 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 1-2 | 33.3 | -19.4 | -37.4 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 11-14 | 44.0 | -7.4 | -15.9 |  |
| consensus_gap+money_level | close | pin $2k+ | 40-28 | 58.8 | -4.3 | -9.6 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 2-11 | 15.4 | -13.3 | -22.5 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -52.8 | -100.0 |  |
| money_level+money_moving | close | pin limit <$1k | 35-46 | 43.2 | -6.4 | -17.4 |  |
| money_level+sharp_gap | close | pin limit <$1k | 36-46 | 43.9 | -5.9 | -16.1 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 65-71 | 47.8 | -2.4 | -1.9 |  |
| consensus_gap+money_level | close | pin limit <$1k | 18-21 | 46.2 | -2.5 | -15.0 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 23-28 | 45.1 | -2.6 | -6.5 |  |
| follow_move+money_moving | close | pin limit <$1k | 44-45 | 49.4 | -1.1 | -5.4 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 45-45 | 50.0 | -0.6 | -4.3 |  |
| money_level+pin_value | close | pin limit <$1k | 27-27 | 50.0 | 1.9 | -5.7 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 11-10 | 52.4 | 4.6 | -1.9 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 14-14 | 50.0 | 2.9 | 10.1 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 15-15 | 50.0 | 2.4 | 9.0 |  |
| follow_move+money_level | close | pin limit <$1k | 34-36 | 48.6 | -0.6 | -7.5 |  |
| follow_move+pin_value | close | pin limit <$1k | 25-16 | 61.0 | 12.1 | 15.4 |  |
| money_moving+pin_value | close | pin limit <$1k | 22-22 | 50.0 | 1.5 | 4.9 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 24-23 | 51.1 | 2.2 | 6.3 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 3-2 | 60.0 | 17.3 | 101.6 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 25-13 | 65.8 | 15.6 | 49.4 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 12-2 | 85.7 | 37.0 | 95.2 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 26-13 | 66.7 | 16.4 | 50.5 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 21-9 | 70.0 | 18.4 | 34.5 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 27-16 | 62.8 | 11.1 | 20.6 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 26-16 | 61.9 | 10.3 | 18.9 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 21-9 | 70.0 | 18.4 | 34.5 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 27-16 | 62.8 | 11.1 | 20.6 |  |
| money_level+pin_rlm | close | pin limit <$1k | 9-6 | 60.0 | 8.1 | 14.8 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 9-8 | 52.9 | 1.2 | 1.8 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 11-4 | 73.3 | 22.5 | 40.5 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 3-3 | 50.0 | 1.8 | -5.2 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 47.4 | 87.7 |  |
| pin_rlm | early | <1k bets | 1-1 | 50.0 | 25.7 | -3.7 | -2.15 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -24.3 | -100.0 | -4.8 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 75.7 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 15-16 | 48.4 | -0.8 | -7.7 | -0.1 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -50.1 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 130-129 | 50.2 | 0.9 | -3.9 | 0.23 |
| follow_move | early | pin $1-2k | 10-8 | 55.6 | 5.6 | 5.0 | -0.06 |
| follow_move | early | pin limit <$1k | 33-29 | 53.2 | 4.1 | 1.1 | -0.35 |
| rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 14.8 | 29.2 | -0.5 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.8 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 2-1 | 66.7 | 14.0 | 28.7 | 0.67 |
| rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -2.8 | -1.0 | -0.5 |
| rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 28.4 | 53.6 | -0.4 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | -0.1 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 41.5 | 59.7 | 0.33 |
| money_level | early | <1k bets | 65-32 | 67.0 | 6.9 | 6.0 | 0.59 |
| money_level | early | pin $1-2k | 14-8 | 63.6 | -1.2 | -3.2 | 0.01 |
| money_level | early | pin limit <$1k | 22-24 | 47.8 | -6.3 | -12.1 | 0.31 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.4 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 6.3 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 49-39 | 55.7 | 8.1 | 12.7 | 0.67 |
| sharp_gap | early | pin $1-2k | 11-9 | 55.0 | 3.3 | 13.8 | -0.57 |
| sharp_gap | early | pin limit <$1k | 27-16 | 62.8 | 14.2 | 30.8 | 0.2 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.3 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.1 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 33-24 | 57.9 | 4.7 | -3.8 | 0.15 |
| money_moving | early | pin $1-2k | 6-6 | 50.0 | -12.4 | -26.9 | 0.35 |
| money_moving | early | pin limit <$1k | 20-9 | 69.0 | 19.9 | 47.8 | 0.36 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.6 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 30-32 | 48.4 | 0.9 | -8.3 | 0.21 |
| pin_value | early | pin $1-2k | 11-14 | 44.0 | 0.0 | -16.7 | 0.17 |
| pin_value | early | pin limit <$1k | 32-27 | 54.2 | 4.9 | 2.5 | 0.15 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -47.4 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -27.7 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -10.7 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 14.2 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 104-147 | 41.4 | -4.4 | -15.9 | 0.42 |
| consensus_gap | early | pin $1-2k | 10-16 | 38.5 | -7.2 | -24.8 | 0.47 |
| consensus_gap | early | pin limit <$1k | 17-32 | 34.7 | -15.6 | -27.7 | 0.33 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 15.9 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 3.4 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 3.2 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.4 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.3 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 15.8 | 26.0 | -0.25 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 4.5 | -6.9 | 0.3 |
| consensus_gap+follow_move | early | 1-3k bets | 4-4 | 50.0 | 2.8 | -6.9 | 0.25 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -22.2 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -1.4 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 10-10 | 50.0 | 0.3 | -4.1 | 0.05 |
| follow_move+pin_value | early | 1-3k bets | 7-5 | 58.3 | 9.3 | 9.2 | -0.42 |
| follow_move+sharp_gap | early | 1-3k bets | 9-8 | 52.9 | 2.8 | 1.2 | -0.18 |
| follow_move+rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 14.8 | 29.2 | -0.5 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 27.3 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 4-2 | 66.7 | 14.8 | 29.2 | -0.5 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 18.5 | 56.1 | 0.15 |
| follow_move+money_moving | early | 1-3k bets | 9-4 | 69.2 | 19.9 | 32.1 | 0.08 |
| money_moving+rlm_ratio | early | 1-3k bets | 2-1 | 66.7 | 15.7 | 28.7 | -1.0 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.8 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.8 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.1 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.8 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 35.8 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 47.4 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 11-11 | 50.0 | 1.0 | -5.9 | 1.36 |
| consensus_gap+money_level | early | <1k bets | 13-11 | 54.2 | -10.2 | -18.2 | 0.91 |
| consensus_gap+sharp_gap | early | <1k bets | 9-18 | 33.3 | -10.6 | -1.8 | 1.09 |
| follow_move+money_level | early | <1k bets | 15-7 | 68.2 | 20.4 | 29.9 | 0.82 |
| follow_move+sharp_gap | early | <1k bets | 15-6 | 71.4 | 22.6 | 36.4 | 1.0 |
| money_level+sharp_gap | early | <1k bets | 38-17 | 69.1 | 13.8 | 16.4 | 1.08 |
| money_level+money_moving | early | <1k bets | 24-14 | 63.2 | 4.8 | -0.9 | -0.03 |
| money_moving+sharp_gap | early | <1k bets | 23-15 | 60.5 | 9.7 | 4.5 | 0.38 |
| consensus_gap+money_moving | early | <1k bets | 5-9 | 35.7 | -10.2 | -42.1 | 0.26 |
| follow_move+pin_value | early | <1k bets | 11-10 | 52.4 | 3.3 | -1.5 | 0.29 |
| follow_move+money_moving | early | <1k bets | 8-4 | 66.7 | 18.0 | 27.9 | 0.25 |
| consensus_gap+pin_value | early | <1k bets | 11-21 | 34.4 | -11.0 | -35.3 | 0.5 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -24.3 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -24.3 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | <1k bets | 1-1 | 50.0 | 25.7 | -3.7 | -2.15 |
| pin_value+sharp_gap | early | <1k bets | 4-3 | 57.1 | 11.6 | 9.1 | 0.03 |
| money_level+pin_value | early | <1k bets | 3-3 | 50.0 | 0.9 | -4.5 | 1.33 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -52.7 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -52.6 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 0-2 | 0.0 | -50.1 | -100.0 | 2.5 |
| follow_move+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 14.0 | 28.7 | 0.67 |
| money_level+rlm_ratio | early | <1k bets | 2-0 | 100.0 | 47.4 | 93.0 | 0.5 |
| money_moving+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 47.4 | 95.2 | 0.0 |
| rlm_ratio+sharp_gap | early | <1k bets | 2-1 | 66.7 | 14.0 | 28.7 | 0.67 |
| consensus_gap+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -52.6 | -100.0 | 1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 47.4 | 90.9 | 1.0 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 75.7 | 92.6 | 0.5 |
| consensus_gap+money_level | early | pin $1-2k | 4-4 | 50.0 | -15.0 | -22.9 | 0.44 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -32.9 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 4-9 | 30.8 | -8.1 | -42.5 | 0.4 |
| follow_move+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -2.8 | -1.0 | -0.5 |
| follow_move+sharp_gap | early | pin $1-2k | 3-1 | 75.0 | 25.0 | 45.0 | -0.25 |
| money_level+money_moving | early | pin $1-2k | 6-5 | 54.5 | -11.3 | -20.3 | 0.02 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.3 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 1-1 | 50.0 | -2.8 | -1.0 | -0.5 |
| money_level+sharp_gap | early | pin $1-2k | 8-4 | 66.7 | 3.8 | 8.4 | -0.41 |
| money_moving+sharp_gap | early | pin $1-2k | 3-5 | 37.5 | -21.8 | -45.3 | -0.06 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.1 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 2-2 | 50.0 | 0.0 | -8.4 | 0.75 |
| follow_move+money_level | early | pin $1-2k | 3-2 | 60.0 | 11.7 | 16.0 | 0.2 |
| follow_move+pin_value | early | pin $1-2k | 4-3 | 57.1 | 7.5 | 6.9 | 0.29 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 47.2 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 1-0 | 100.0 | 52.8 | 90.9 | 0.0 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -24.3 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -25.0 | -62.8 | -0.72 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -24.3 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -24.3 | -100.0 | -4.8 |
| money_level+money_moving | early | pin limit <$1k | 11-7 | 61.1 | 8.0 | 12.1 | 0.53 |
| money_level+sharp_gap | early | pin limit <$1k | 18-14 | 56.2 | 5.0 | 2.3 | 0.25 |
| money_moving+sharp_gap | early | pin limit <$1k | 16-5 | 76.2 | 28.3 | 68.0 | 0.39 |
| money_level+pin_value | early | pin limit <$1k | 8-5 | 61.5 | 10.5 | 16.6 | 0.46 |
| money_moving+pin_value | early | pin limit <$1k | 6-4 | 60.0 | 10.0 | 13.0 | 0.3 |
| pin_value+sharp_gap | early | pin limit <$1k | 11-5 | 68.8 | 18.4 | 30.3 | 0.06 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-7 | 46.2 | -1.5 | -14.2 | 0.46 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -27.4 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 13-17 | 43.3 | -5.0 | -18.8 | 0.49 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.7 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 8-7 | 53.3 | 3.5 | 1.9 | 0.07 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 4.9 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 9-7 | 56.2 | 6.3 | 6.9 | -0.31 |
| follow_move+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 28.4 | 53.6 | -0.4 |
| money_level+rlm_ratio | early | pin limit <$1k | 4-0 | 100.0 | 47.4 | 92.0 | 0.25 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.8 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 4-1 | 80.0 | 28.4 | 53.6 | -0.4 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 23.4 | 72.3 | 0.54 |
| follow_move+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 20.6 | 33.3 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.8 | 28.7 | -1.0 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -52.6 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -52.6 | -100.0 | 1.0 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 75.7 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 75.7 | 92.6 | 0.5 |
