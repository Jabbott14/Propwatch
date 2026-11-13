# CBB scorecard

Generated 2026-11-13 17:23 UTC. 362 graded games (8 finished games had no final score matched and are not graded).

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before tip. Break-even at -110 is 52.4%. CLV = points of closing-line
value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured
on this sample. `edge` is hit% minus that. A signal that is structurally long
favourites or overs beats 50% whenever those run, which is not an edge -- this
sample ran **48.9% favourites** (n=362) and **48.9% overs** (n=362) and **76.5% moneyline favourites** (n=306).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

## EARLY

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 1-1 | 50.0 | 23.5 | 26.5 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | both | 147-148 | 49.8 | 49.8 | 0.0 | -13.68 | -4.6 | 0.22 | 40.3 | no edge shown yet |
| rlm_ratio | both | 6-4 | 60.0 | 50.9 | 9.1 | +1.61 | 16.1 | -0.2 | 20.0 | keep collecting (10/30) |
| money_level | both | 87-50 | 63.5 | 59.5 | 4.0 | +3.49 | 2.5 | 0.39 | 43.8 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 71-56 | 55.9 | 48.2 | 7.7 | +21.43 | 16.9 | 0.44 | 41.7 | no edge shown yet |
| money_moving | both | 53-33 | 61.6 | 51.4 | 10.2 | +9.53 | 11.1 | 0.1 | 41.9 | PROMOTE: beats break-even and its own base rate |
| pin_value | both | 43-41 | 51.2 | 48.0 | 3.2 | -2.68 | -3.2 | 0.15 | 41.7 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 50.7 | -30.7 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 123-171 | 41.8 | 45.9 | -4.1 | -44.09 | -15.0 | 0.35 | 47.3 | DROP: below break-even |
| consensus_gap+money_level | both | 17-18 | 48.6 | 62.5 | -14.0 | -9.16 | -26.2 | 0.6 | 51.4 | no edge shown yet |
| consensus_gap+money_moving | both | 12-13 | 48.0 | 44.4 | 3.6 | +0.55 | 2.2 | 0.24 | 40.0 | keep collecting (25/30) |
| consensus_gap+pin_value | both | 17-26 | 39.5 | 45.9 | -6.4 | -11.16 | -26.0 | 0.46 | 53.5 | DROP: below break-even |
| follow_move+rlm_ratio | both | 6-4 | 60.0 | 50.9 | 9.1 | +1.61 | 16.1 | -0.2 | 20.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 22-14 | 61.1 | 49.8 | 11.3 | +5.98 | 16.6 | 0.39 | 36.1 | no edge shown yet |
| money_level+money_moving | both | 37-18 | 67.3 | 58.0 | 9.3 | +5.7 | 10.4 | 0.03 | 45.5 | PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | both | 10-8 | 55.6 | 50.1 | 5.4 | +0.9 | 5.0 | 0.5 | 50.0 | keep collecting (18/30) |
| money_moving+pin_value | both | 7-5 | 58.3 | 50.0 | 8.3 | +1.13 | 9.4 | 0.42 | 41.7 | keep collecting (12/30) |
| rlm_ratio+sharp_gap | both | 6-4 | 60.0 | 50.9 | 9.1 | +1.61 | 16.1 | -0.2 | 20.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 53-29 | 64.6 | 55.0 | 9.6 | +9.31 | 11.4 | 0.7 | 47.6 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 33-21 | 61.1 | 48.5 | 12.6 | +9.27 | 17.2 | 0.25 | 42.6 | no edge shown yet |
| pin_value+sharp_gap | both | 12-7 | 63.2 | 48.7 | 14.4 | +3.75 | 19.8 | -0.15 | 36.8 | keep collecting (19/30) |
| consensus_gap+follow_move | both | 13-13 | 50.0 | 49.4 | 0.6 | -1.67 | -6.4 | 1.0 | 50.0 | keep collecting (26/30) |
| consensus_gap+sharp_gap | both | 13-24 | 35.1 | 42.7 | -7.6 | +1.39 | 3.8 | 0.86 | 48.6 | DROP: below break-even |
| follow_move+money_level | both | 24-15 | 61.5 | 49.5 | 12.0 | +6.82 | 17.5 | 0.49 | 41.0 | no edge shown yet |
| follow_move+pin_value | both | 18-15 | 54.5 | 49.6 | 4.9 | +0.8 | 2.4 | 0.03 | 30.3 | no edge shown yet |
| money_level+rlm_ratio | both | 6-1 | 85.7 | 51.1 | 34.6 | +4.61 | 65.9 | 0.14 | 14.3 | keep collecting (7/30) |
| pin_value+rlm_ratio | both | 2-1 | 66.7 | 50.4 | 16.3 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| follow_move+money_moving | both | 15-7 | 68.2 | 49.6 | 18.6 | +6.67 | 30.3 | 0.05 | 31.8 | keep collecting (22/30) |
| money_moving+rlm_ratio | both | 3-1 | 75.0 | 50.6 | 24.4 | +1.81 | 45.3 | -0.75 | 0.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 23.5 | -23.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 23.5 | -23.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | both | 1-1 | 50.0 | 23.5 | 26.5 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.1 | -51.1 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 23.5 | 76.5 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-1 | 50.0 | 23.5 | 26.5 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | spread | 71-77 | 48.0 | 49.7 | -1.7 | -12.18 | -8.2 | 0.09 | 36.5 | no edge shown yet |
| follow_move | total | 76-71 | 51.7 | 49.9 | 1.8 | -1.5 | -1.0 | 0.35 | 44.2 | no edge shown yet |
| rlm_ratio | spread | 2-2 | 50.0 | 51.1 | -1.1 | -0.07 | -1.7 | -0.25 | 0.0 | keep collecting (4/30) |
| rlm_ratio | total | 4-2 | 66.7 | 50.7 | 15.9 | +1.68 | 28.0 | -0.17 | 33.3 | keep collecting (6/30) |
| money_level | moneyline | 41-19 | 68.3 | 72.1 | -3.7 | -7.2 | -12.0 | 0.31 | 50.0 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 15-14 | 51.7 | 49.6 | 2.1 | -0.54 | -1.9 | 0.86 | 44.8 | keep collecting (29/30) |
| money_level | total | 31-17 | 64.6 | 49.7 | 14.9 | +11.22 | 23.4 | 0.21 | 35.4 | PROMOTE: beats break-even and its own base rate |
| sharp_gap | moneyline | 28-23 | 54.9 | 45.3 | 9.6 | +15.41 | 30.2 | 0.5 | 52.9 | no edge shown yet |
| sharp_gap | spread | 16-14 | 53.3 | 50.0 | 3.3 | +0.41 | 1.4 | 0.63 | 33.3 | no edge shown yet |
| sharp_gap | total | 27-19 | 58.7 | 50.1 | 8.6 | +5.61 | 12.2 | 0.24 | 34.8 | no edge shown yet |
| money_moving | moneyline | 20-17 | 54.1 | 53.6 | 0.5 | -4.28 | -11.6 | 0.13 | 56.8 | no edge shown yet |
| money_moving | spread | 15-4 | 78.9 | 49.7 | 29.2 | +9.42 | 49.6 | 0.21 | 36.8 | keep collecting (19/30) |
| money_moving | total | 18-12 | 60.0 | 49.9 | 10.1 | +4.39 | 14.6 | 0.0 | 26.7 | no edge shown yet |
| pin_value | moneyline | 1-5 | 16.7 | 23.5 | -6.9 | -4.02 | -67.0 | -0.02 | 66.7 | keep collecting (6/30) |
| pin_value | spread | 22-17 | 56.4 | 49.7 | 6.7 | +2.35 | 6.0 | 0.28 | 41.0 | no edge shown yet |
| pin_value | total | 20-19 | 51.3 | 50.0 | 1.3 | -1.01 | -2.6 | 0.05 | 38.5 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 51.1 | -17.8 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 46-92 | 33.3 | 41.6 | -8.2 | -33.11 | -24.0 | 0.06 | 43.5 | DROP: below break-even |
| consensus_gap | spread | 42-35 | 54.5 | 49.7 | 4.9 | +1.57 | 2.0 | 0.51 | 48.1 | no edge shown yet |
| consensus_gap | total | 35-44 | 44.3 | 49.8 | -5.5 | -12.55 | -15.9 | 0.68 | 53.2 | no edge shown yet |
| money_level+sharp_gap | moneyline | 20-6 | 76.9 | 66.3 | 10.6 | +2.39 | 9.2 | 0.88 | 69.2 | keep collecting (26/30) |
| consensus_gap+pin_value | moneyline | 1-5 | 16.7 | 23.5 | -6.9 | -4.02 | -67.0 | -0.02 | 66.7 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_level+money_moving | moneyline | 14-7 | 66.7 | 71.4 | -4.8 | -4.27 | -20.3 | -0.53 | 52.4 | keep collecting (21/30) |
| consensus_gap+sharp_gap | moneyline | 7-15 | 31.8 | 38.0 | -6.1 | +5.17 | 23.5 | 0.9 | 54.5 | keep collecting (22/30) |
| consensus_gap+money_level | moneyline | 11-10 | 52.4 | 71.4 | -19.0 | -6.35 | -30.2 | 0.23 | 52.4 | keep collecting (21/30) |
| money_moving+sharp_gap | moneyline | 12-11 | 52.2 | 46.5 | 5.6 | +0.24 | 1.0 | 0.28 | 60.9 | keep collecting (23/30) |
| consensus_gap+money_moving | moneyline | 5-12 | 29.4 | 42.2 | -12.8 | -4.5 | -26.5 | 0.3 | 52.9 | keep collecting (17/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 23.5 | -23.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 23.5 | -23.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | moneyline | 1-1 | 50.0 | 23.5 | 26.5 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 23.5 | -23.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 23.5 | 76.5 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 4-5 | 44.4 | 48.9 | -4.5 | -1.59 | -17.7 | 1.67 | 66.7 | keep collecting (9/30) |
| consensus_gap+money_moving | spread | 4-0 | 100.0 | 48.9 | 51.1 | +3.41 | 85.2 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_value | spread | 9-8 | 52.9 | 49.3 | 3.7 | -0.31 | -1.8 | 0.53 | 52.9 | keep collecting (17/30) |
| follow_move+rlm_ratio | spread | 2-2 | 50.0 | 51.1 | -1.1 | -0.07 | -1.7 | -0.25 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 8-6 | 57.1 | 49.5 | 7.6 | +1.23 | 8.8 | 0.79 | 35.7 | keep collecting (14/30) |
| money_level+money_moving | spread | 8-4 | 66.7 | 49.4 | 17.2 | +3.27 | 27.2 | 0.75 | 58.3 | keep collecting (12/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 49.5 | -6.7 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.8 | 10.2 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | spread | 2-2 | 50.0 | 51.1 | -1.1 | -0.07 | -1.7 | -0.25 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 12-11 | 52.2 | 49.7 | 2.5 | -0.23 | -1.0 | 0.96 | 39.1 | keep collecting (23/30) |
| money_moving+sharp_gap | spread | 7-3 | 70.0 | 49.8 | 20.2 | +3.27 | 32.7 | 0.6 | 40.0 | keep collecting (10/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.6 | 17.0 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 8-7 | 53.3 | 49.2 | 4.1 | -0.18 | -1.2 | 0.87 | 40.0 | keep collecting (15/30) |
| consensus_gap+sharp_gap | spread | 3-3 | 50.0 | 48.9 | 1.1 | -0.43 | -7.1 | 2.17 | 66.7 | keep collecting (6/30) |
| follow_move+money_level | spread | 10-7 | 58.8 | 49.3 | 9.5 | +2.1 | 12.3 | 0.76 | 41.2 | keep collecting (17/30) |
| follow_move+pin_value | spread | 11-7 | 61.1 | 49.5 | 11.6 | +2.56 | 14.2 | 0.33 | 33.3 | keep collecting (18/30) |
| follow_move+money_moving | spread | 7-1 | 87.5 | 49.2 | 38.3 | +5.37 | 67.2 | 0.38 | 37.5 | keep collecting (8/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 51.1 | 15.6 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 1-0 | 100.0 | 51.1 | 48.9 | +0.95 | 95.2 | 0.0 | 0.0 | keep collecting (1/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 15-7 | 68.2 | 49.8 | 18.4 | +6.7 | 30.4 | 0.18 | 31.8 | keep collecting (22/30) |
| money_level+sharp_gap | total | 21-12 | 63.6 | 49.9 | 13.7 | +7.15 | 21.7 | 0.39 | 36.4 | no edge shown yet |
| money_moving+sharp_gap | total | 14-7 | 66.7 | 50.1 | 16.6 | +5.75 | 27.4 | 0.05 | 23.8 | keep collecting (21/30) |
| money_level+pin_value | total | 7-4 | 63.6 | 50.5 | 13.1 | +2.32 | 21.1 | 0.36 | 36.4 | keep collecting (11/30) |
| money_moving+pin_value | total | 4-3 | 57.1 | 50.2 | 7.0 | +0.56 | 8.0 | 0.29 | 28.6 | keep collecting (7/30) |
| pin_value+sharp_gap | total | 10-5 | 66.7 | 50.2 | 16.4 | +4.01 | 26.7 | 0.0 | 33.3 | keep collecting (15/30) |
| follow_move+money_level | total | 14-8 | 63.6 | 49.7 | 13.9 | +4.72 | 21.5 | 0.27 | 40.9 | keep collecting (22/30) |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.8 | -3.1 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 4-2 | 66.7 | 50.7 | 15.9 | +1.68 | 28.0 | -0.17 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 14-8 | 63.6 | 50.0 | 13.6 | +4.75 | 21.6 | 0.14 | 36.4 | keep collecting (22/30) |
| money_level+rlm_ratio | total | 4-0 | 100.0 | 51.1 | 48.9 | +3.68 | 92.0 | 0.25 | 25.0 | keep collecting (4/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 50.4 | 16.3 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 4-2 | 66.7 | 50.7 | 15.9 | +1.68 | 28.0 | -0.17 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 8-6 | 57.1 | 49.8 | 7.3 | +1.29 | 9.2 | -0.14 | 28.6 | keep collecting (14/30) |
| consensus_gap+money_level | total | 2-3 | 40.0 | 49.8 | -9.8 | -1.22 | -24.4 | 0.2 | 20.0 | keep collecting (5/30) |
| consensus_gap+money_moving | total | 3-1 | 75.0 | 49.4 | 25.6 | +1.65 | 41.2 | 0.0 | 0.0 | keep collecting (4/30) |
| consensus_gap+pin_value | total | 7-13 | 35.0 | 49.8 | -14.8 | -6.83 | -34.2 | 0.55 | 50.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | total | 3-6 | 33.3 | 50.1 | -16.8 | -3.35 | -37.2 | -0.11 | 22.2 | keep collecting (9/30) |
| money_moving+rlm_ratio | total | 2-1 | 66.7 | 50.4 | 16.3 | +0.86 | 28.7 | -1.0 | 0.0 | keep collecting (3/30) |
| consensus_gap+follow_move | total | 5-6 | 45.5 | 49.7 | -4.2 | -1.49 | -13.5 | 1.18 | 63.6 | keep collecting (11/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |

## CLOSE

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 67-70 | 48.9 | 41.7 | 7.2 | +25.4 | 18.5 |  |  | no edge shown yet |
| follow_move | both | 299-304 | 49.6 | 49.8 | -0.2 | -33.48 | -5.6 |  |  | no edge shown yet |
| rlm_ratio | both | 86-67 | 56.2 | 50.4 | 5.8 | +11.13 | 7.3 |  |  | no edge shown yet |
| money_level | both | 560-431 | 56.5 | 56.4 | 0.1 | -61.77 | -6.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 418-534 | 43.9 | 46.5 | -2.6 | -79.99 | -8.4 |  |  | DROP: below break-even |
| money_moving | both | 415-537 | 43.6 | 46.9 | -3.3 | -93.39 | -9.8 |  |  | DROP: below break-even |
| pin_value | both | 201-186 | 51.9 | 47.6 | 4.4 | +17.72 | 4.6 |  |  | no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 50.4 | 16.3 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 219-313 | 41.2 | 46.2 | -5.0 | -58.01 | -10.9 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 53-47 | 53.0 | 49.1 | 3.9 | -1.21 | -1.2 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 91-174 | 34.3 | 42.7 | -8.4 | -20.78 | -7.8 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 16-24 | 40.0 | 36.7 | 3.3 | +15.34 | 38.3 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 93-105 | 47.0 | 45.2 | 1.8 | +1.38 | 0.7 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | both | 14-10 | 58.3 | 49.5 | 8.8 | +2.2 | 9.2 |  |  | keep collecting (24/30) |
| consensus_gap+sharp_gap | both | 92-178 | 34.1 | 42.3 | -8.2 | -21.61 | -8.0 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 194-222 | 46.6 | 49.8 | -3.2 | -47.14 | -11.3 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 43-33 | 56.6 | 50.6 | 6.0 | +6.27 | 8.2 |  |  | no edge shown yet |
| follow_move+pin_value | both | 74-58 | 56.1 | 49.5 | 6.5 | +7.12 | 5.4 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 86-67 | 56.2 | 50.4 | 5.8 | +11.13 | 7.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 198-219 | 47.5 | 49.8 | -2.3 | -40.28 | -9.7 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 64-70 | 47.8 | 41.5 | 6.2 | +22.66 | 16.9 |  |  | no edge shown yet |
| money_moving+pin_value | both | 83-101 | 45.1 | 46.1 | -1.0 | -4.86 | -2.6 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 83-66 | 55.7 | 50.4 | 5.3 | +9.29 | 6.2 |  |  | no edge shown yet |
| money_moving+sharp_gap | both | 400-517 | 43.6 | 46.6 | -3.0 | -82.35 | -9.0 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 22-19 | 53.7 | 44.5 | 9.1 | +14.38 | 35.1 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 43-33 | 56.6 | 50.6 | 6.0 | +6.27 | 8.2 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 67-70 | 48.9 | 41.7 | 7.2 | +25.4 | 18.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 22-15 | 59.5 | 50.1 | 9.3 | +4.67 | 12.6 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 85-101 | 45.7 | 46.0 | -0.3 | -3.11 | -1.7 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 86-67 | 56.2 | 50.4 | 5.8 | +11.13 | 7.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+money_moving | both | 288-294 | 49.5 | 52.3 | -2.8 | -53.78 | -9.2 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 287-290 | 49.7 | 52.1 | -2.3 | -46.81 | -8.1 |  |  | no edge shown yet |
| follow_move+money_level | both | 174-194 | 47.3 | 49.5 | -2.2 | -37.76 | -10.3 |  |  | DROP: below break-even |
| money_level+rlm_ratio | both | 38-34 | 52.8 | 50.2 | 2.6 | +0.15 | 0.2 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 134-113 | 54.3 | 57.9 | -3.6 | -15.06 | -6.1 |  |  | no edge shown yet |
| money_level+pin_value | both | 92-89 | 50.8 | 49.7 | 1.1 | -9.72 | -5.4 |  |  | no edge shown yet |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | both | 26-20 | 56.5 | 47.0 | 9.5 | +5.25 | 11.4 |  |  | no edge shown yet |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 51.1 | 48.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 18-31 | 36.7 | 25.7 | 11.0 | +19.8 | 40.4 |  |  | DROP: below break-even |
| pin_rlm | spread | 14-13 | 51.9 | 50.5 | 1.3 | -0.37 | -1.4 |  |  | keep collecting (27/30) |
| pin_rlm | total | 35-26 | 57.4 | 50.7 | 6.6 | +5.97 | 9.8 |  |  | no edge shown yet |
| follow_move | spread | 136-143 | 48.7 | 49.5 | -0.8 | -20.76 | -7.4 |  |  | no edge shown yet |
| follow_move | total | 163-161 | 50.3 | 50.0 | 0.3 | -12.72 | -3.9 |  |  | no edge shown yet |
| rlm_ratio | spread | 24-24 | 50.0 | 50.1 | -0.1 | -2.28 | -4.7 |  |  | no edge shown yet |
| rlm_ratio | total | 62-43 | 59.0 | 50.5 | 8.5 | +13.41 | 12.8 |  |  | no edge shown yet |
| money_level | moneyline | 228-72 | 76.0 | 72.2 | 3.8 | -1.72 | -0.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 162-175 | 48.1 | 49.5 | -1.4 | -30.0 | -8.9 |  |  | DROP: below break-even |
| money_level | total | 170-184 | 48.0 | 49.7 | -1.6 | -30.05 | -8.5 |  |  | DROP: below break-even |
| sharp_gap | moneyline | 88-184 | 32.4 | 37.9 | -5.6 | -28.42 | -10.4 |  |  | DROP: below break-even |
| sharp_gap | spread | 168-164 | 50.6 | 49.8 | 0.8 | -13.13 | -4.0 |  |  | no edge shown yet |
| sharp_gap | total | 162-186 | 46.6 | 50.1 | -3.6 | -38.45 | -11.0 |  |  | DROP: below break-even |
| money_moving | moneyline | 92-178 | 34.1 | 39.2 | -5.1 | -26.31 | -9.7 |  |  | DROP: below break-even |
| money_moving | spread | 165-167 | 49.7 | 49.8 | -0.1 | -19.0 | -5.7 |  |  | no edge shown yet |
| money_moving | total | 158-192 | 45.1 | 50.1 | -5.0 | -48.08 | -13.7 |  |  | DROP: below break-even |
| pin_value | moneyline | 10-30 | 25.0 | 27.5 | -2.5 | +4.34 | 10.9 |  |  | DROP: below break-even |
| pin_value | spread | 96-67 | 58.9 | 49.9 | 9.0 | +17.04 | 10.5 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_value | total | 95-89 | 51.6 | 49.8 | 1.8 | -3.67 | -2.0 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 51.1 | 48.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 84-183 | 31.5 | 43.0 | -11.5 | -45.64 | -17.1 |  |  | DROP: below break-even |
| consensus_gap | spread | 65-50 | 56.5 | 49.6 | 6.9 | +5.48 | 4.8 |  |  | no edge shown yet |
| consensus_gap | total | 70-80 | 46.7 | 49.4 | -2.7 | -17.85 | -11.9 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 63-38 | 62.4 | 64.9 | -2.6 | -0.18 | -0.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 58-37 | 61.1 | 64.2 | -3.2 | +0.14 | 0.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 83-173 | 32.4 | 38.0 | -5.6 | -24.86 | -9.7 |  |  | DROP: below break-even |
| consensus_gap+money_level | moneyline | 60-36 | 62.5 | 71.5 | -9.0 | -2.4 | -2.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 28-106 | 20.9 | 36.2 | -15.3 | -7.4 | -5.5 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+sharp_gap | moneyline | 29-111 | 20.7 | 35.6 | -14.9 | -9.25 | -6.6 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | moneyline | 8-16 | 33.3 | 27.9 | 5.4 | +16.43 | 68.5 |  |  | keep collecting (24/30) |
| money_moving+pin_rlm | moneyline | 18-31 | 36.7 | 25.7 | 11.0 | +19.8 | 40.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 18-31 | 36.7 | 25.7 | 11.0 | +19.8 | 40.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 10-29 | 25.6 | 27.6 | -2.0 | +5.34 | 13.7 |  |  | DROP: below break-even |
| money_moving+pin_value | moneyline | 5-21 | 19.2 | 23.5 | -4.3 | +6.55 | 25.2 |  |  | keep collecting (26/30) |
| pin_rlm+pin_value | moneyline | 3-6 | 33.3 | 23.5 | 9.8 | +10.35 | 115.0 |  |  | keep collecting (9/30) |
| pin_value+sharp_gap | moneyline | 5-22 | 18.5 | 23.5 | -5.0 | +5.55 | 20.6 |  |  | keep collecting (27/30) |
| money_level+pin_rlm | moneyline | 5-3 | 62.5 | 30.1 | 32.4 | +3.4 | 42.5 |  |  | keep collecting (8/30) |
| money_level+pin_value | moneyline | 3-1 | 75.0 | 63.2 | 11.8 | +0.31 | 7.8 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 27-19 | 58.7 | 49.1 | 9.6 | +3.91 | 8.5 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 35-29 | 54.7 | 49.5 | 5.2 | +0.87 | 1.4 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 45-29 | 60.8 | 49.6 | 11.2 | +9.31 | 12.6 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.33 | -38.9 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | spread | 34-29 | 54.0 | 49.6 | 4.3 | -0.02 | -0.0 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 88-94 | 48.4 | 49.4 | -1.1 | -15.4 | -8.5 |  |  | no edge shown yet |
| follow_move+pin_rlm | spread | 12-12 | 50.0 | 50.5 | -0.5 | -1.13 | -4.7 |  |  | keep collecting (24/30) |
| follow_move+pin_value | spread | 35-22 | 61.4 | 49.2 | 12.2 | +8.23 | 14.4 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 24-24 | 50.0 | 50.1 | -0.1 | -2.28 | -4.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 89-93 | 48.9 | 49.5 | -0.6 | -13.26 | -7.3 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 12-13 | 48.0 | 50.5 | -2.5 | -2.2 | -8.8 |  |  | keep collecting (25/30) |
| money_moving+pin_value | spread | 44-37 | 54.3 | 49.7 | 4.7 | +1.03 | 1.3 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 22-23 | 48.9 | 50.1 | -1.2 | -3.21 | -7.1 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 160-159 | 50.2 | 49.8 | 0.4 | -15.5 | -4.9 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 6-4 | 60.0 | 50.2 | 9.8 | +1.21 | 12.1 |  |  | keep collecting (10/30) |
| pin_rlm+rlm_ratio | spread | 12-12 | 50.0 | 50.5 | -0.5 | -1.13 | -4.7 |  |  | keep collecting (24/30) |
| pin_rlm+sharp_gap | spread | 14-13 | 51.9 | 50.5 | 1.3 | -0.37 | -1.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 4-3 | 57.1 | 49.8 | 7.3 | +0.45 | 6.5 |  |  | keep collecting (7/30) |
| pin_value+sharp_gap | spread | 44-37 | 54.3 | 49.7 | 4.6 | +0.97 | 1.2 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 24-24 | 50.0 | 50.1 | -0.1 | -2.28 | -4.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 87-93 | 48.3 | 49.2 | -0.9 | -15.41 | -8.6 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 11-12 | 47.8 | 50.0 | -2.1 | -2.22 | -9.7 |  |  | keep collecting (23/30) |
| money_level+sharp_gap | spread | 127-129 | 49.6 | 49.5 | 0.1 | -15.4 | -6.0 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 42-33 | 56.0 | 49.4 | 6.6 | +2.96 | 4.0 |  |  | no edge shown yet |
| money_level+money_moving | spread | 126-130 | 49.2 | 49.5 | -0.3 | -17.32 | -6.8 |  |  | no edge shown yet |
| money_level+pin_value | spread | 48-42 | 53.3 | 49.5 | 3.8 | -0.62 | -0.7 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 7-5 | 58.3 | 50.2 | 8.1 | +1.16 | 9.7 |  |  | keep collecting (12/30) |
| money_level+money_moving | total | 99-126 | 44.0 | 49.8 | -5.8 | -36.28 | -16.1 |  |  | DROP: below break-even |
| money_level+sharp_gap | total | 102-124 | 45.1 | 49.8 | -4.7 | -31.55 | -14.0 |  |  | DROP: below break-even |
| money_moving+sharp_gap | total | 157-185 | 45.9 | 50.1 | -4.2 | -41.99 | -12.3 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 32-44 | 42.1 | 49.1 | -7.0 | -15.62 | -20.6 |  |  | DROP: below break-even |
| consensus_gap+pin_value | total | 38-47 | 44.7 | 49.3 | -4.6 | -13.28 | -15.6 |  |  | no edge shown yet |
| follow_move+money_moving | total | 106-128 | 45.3 | 50.1 | -4.8 | -31.74 | -13.6 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 109-126 | 46.4 | 50.1 | -3.7 | -27.01 | -11.5 |  |  | DROP: below break-even |
| money_level+pin_value | total | 41-46 | 47.1 | 49.4 | -2.3 | -9.42 | -10.8 |  |  | no edge shown yet |
| follow_move+money_level | total | 87-101 | 46.3 | 49.7 | -3.4 | -22.34 | -11.9 |  |  | DROP: below break-even |
| follow_move+pin_value | total | 39-36 | 52.0 | 49.7 | 2.3 | -1.11 | -1.5 |  |  | no edge shown yet |
| money_moving+pin_value | total | 34-43 | 44.2 | 50.0 | -5.8 | -12.45 | -16.2 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 36-42 | 46.2 | 50.0 | -3.8 | -9.63 | -12.3 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 28-39 | 41.8 | 49.4 | -7.6 | -14.25 | -21.3 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | total | 29-38 | 43.3 | 49.4 | -6.1 | -12.34 | -18.4 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 26-28 | 48.1 | 49.2 | -1.0 | -5.12 | -9.5 |  |  | no edge shown yet |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pin_rlm | total | 5-5 | 50.0 | 49.6 | 0.4 | -0.6 | -6.0 |  |  | keep collecting (10/30) |
| consensus_gap+rlm_ratio | total | 12-6 | 66.7 | 49.4 | 17.3 | +4.53 | 25.2 |  |  | keep collecting (18/30) |
| follow_move+pin_rlm | total | 31-21 | 59.6 | 50.7 | 8.9 | +7.39 | 14.2 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 62-43 | 59.0 | 50.5 | 8.5 | +13.41 | 12.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 14-12 | 53.8 | 50.7 | 3.2 | +0.69 | 2.7 |  |  | keep collecting (26/30) |
| money_level+rlm_ratio | total | 27-22 | 55.1 | 50.3 | 4.8 | +2.37 | 4.8 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 34-26 | 56.7 | 50.7 | 5.9 | +5.06 | 8.4 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 61-43 | 58.7 | 50.5 | 8.1 | +12.5 | 12.0 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 13-9 | 59.1 | 50.5 | 8.6 | +2.82 | 12.8 |  |  | keep collecting (22/30) |
| pin_rlm+rlm_ratio | total | 31-21 | 59.6 | 50.7 | 8.9 | +7.39 | 14.2 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 35-26 | 57.4 | 50.7 | 6.6 | +5.97 | 9.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 18-12 | 60.0 | 50.2 | 9.8 | +4.22 | 14.1 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 62-43 | 59.0 | 50.5 | 8.5 | +13.41 | 12.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 51.1 | 48.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_rlm | close | 1-3k bets | 37-45 | 45.1 | 2.4 | 17.1 |  |
| pin_rlm | close | 3k+ bets | 19-18 | 51.4 | 11.7 | 15.2 |  |
| pin_rlm | close | <1k bets | 11-7 | 61.1 | 19.3 | 31.8 |  |
| pin_rlm | close | pin $1-2k | 32-25 | 56.1 | 12.3 | 38.0 |  |
| pin_rlm | close | pin $2k+ | 13-34 | 27.7 | -6.3 | -30.5 |  |
| pin_rlm | close | pin limit <$1k | 22-11 | 66.7 | 17.5 | 54.8 |  |
| follow_move | close | 1-3k bets | 196-194 | 50.3 | 0.5 | -4.3 |  |
| follow_move | close | 3k+ bets | 70-77 | 47.6 | -2.2 | -9.2 |  |
| follow_move | close | <1k bets | 33-33 | 50.0 | 0.2 | -4.9 |  |
| follow_move | close | pin $1-2k | 94-125 | 42.9 | -6.7 | -18.4 |  |
| follow_move | close | pin $2k+ | 51-54 | 48.6 | -1.2 | -7.6 |  |
| follow_move | close | pin limit <$1k | 68-55 | 55.3 | 5.2 | 5.7 |  |
| rlm_ratio | close | 1-3k bets | 58-51 | 53.2 | 2.9 | 1.4 |  |
| rlm_ratio | close | 3k+ bets | 21-14 | 60.0 | 9.5 | 14.9 |  |
| rlm_ratio | close | <1k bets | 7-2 | 77.8 | 26.9 | 49.3 |  |
| rlm_ratio | close | pin $1-2k | 28-27 | 50.9 | 0.8 | -3.5 |  |
| rlm_ratio | close | pin $2k+ | 10-12 | 45.5 | -5.2 | -13.1 |  |
| rlm_ratio | close | pin limit <$1k | 24-14 | 63.2 | 12.4 | 21.4 |  |
| money_level | close | 1-3k bets | 376-250 | 60.1 | 3.4 | 0.0 |  |
| money_level | close | 3k+ bets | 128-118 | 52.0 | -4.0 | -12.2 |  |
| money_level | close | <1k bets | 56-62 | 47.5 | -8.9 | -26.1 |  |
| money_level | close | pin $1-2k | 156-149 | 51.1 | -3.2 | -9.6 |  |
| money_level | close | pin $2k+ | 133-104 | 56.1 | -2.3 | -9.2 |  |
| money_level | close | pin limit <$1k | 67-71 | 48.6 | -1.7 | -8.1 |  |
| sharp_gap | close | 1-3k bets | 259-343 | 43.0 | -3.6 | -11.2 |  |
| sharp_gap | close | 3k+ bets | 110-129 | 46.0 | -0.2 | 1.8 |  |
| sharp_gap | close | <1k bets | 49-61 | 44.5 | -2.5 | -14.4 |  |
| sharp_gap | close | pin $1-2k | 139-159 | 46.6 | -1.6 | -4.1 |  |
| sharp_gap | close | pin $2k+ | 88-138 | 38.9 | -6.3 | -20.3 |  |
| sharp_gap | close | pin limit <$1k | 64-68 | 48.5 | -1.4 | -0.4 |  |
| money_moving | close | 1-3k bets | 257-344 | 42.8 | -4.1 | -12.4 |  |
| money_moving | close | 3k+ bets | 109-132 | 45.2 | -1.7 | -1.4 |  |
| money_moving | close | <1k bets | 49-60 | 45.0 | -2.3 | -13.6 |  |
| money_moving | close | pin $1-2k | 134-164 | 45.0 | -3.4 | -7.5 |  |
| money_moving | close | pin $2k+ | 91-134 | 40.4 | -4.9 | -17.9 |  |
| money_moving | close | pin limit <$1k | 63-70 | 47.4 | -2.4 | -2.5 |  |
| pin_value | close | 1-3k bets | 122-124 | 49.6 | 2.1 | 0.1 |  |
| pin_value | close | 3k+ bets | 46-48 | 48.9 | 1.4 | -1.0 |  |
| pin_value | close | <1k bets | 33-14 | 70.2 | 22.6 | 39.1 |  |
| pin_value | close | pin $1-2k | 99-88 | 52.9 | 5.1 | 4.6 |  |
| pin_value | close | pin $2k+ | 52-55 | 48.6 | 3.2 | 2.9 |  |
| pin_value | close | pin limit <$1k | 50-43 | 53.8 | 4.4 | 6.6 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 48.9 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 48.9 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 138-193 | 41.7 | -4.9 | -12.0 |  |
| consensus_gap | close | 3k+ bets | 55-72 | 43.3 | -3.9 | 2.2 |  |
| consensus_gap | close | <1k bets | 26-47 | 35.6 | -7.3 | -27.3 |  |
| consensus_gap | close | pin $1-2k | 71-82 | 46.4 | -1.6 | 1.2 |  |
| consensus_gap | close | pin $2k+ | 54-67 | 44.6 | -6.3 | -16.2 |  |
| consensus_gap | close | pin limit <$1k | 34-32 | 51.5 | 2.2 | 2.7 |  |
| consensus_gap+follow_move | close | 1-3k bets | 38-28 | 57.6 | 8.4 | 7.5 |  |
| consensus_gap+money_level | close | 1-3k bets | 92-62 | 59.7 | 1.1 | 5.2 |  |
| consensus_gap+money_moving | close | 1-3k bets | 59-110 | 34.9 | -8.0 | -10.2 |  |
| consensus_gap+pin_value | close | 1-3k bets | 59-70 | 45.7 | 0.4 | -1.9 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 59-113 | 34.3 | -8.2 | -11.5 |  |
| follow_move+money_level | close | 1-3k bets | 123-121 | 50.4 | 1.0 | -4.3 |  |
| follow_move+money_moving | close | 1-3k bets | 135-147 | 47.9 | -1.9 | -9.0 |  |
| follow_move+pin_value | close | 1-3k bets | 44-37 | 54.3 | 4.9 | 2.0 |  |
| follow_move+sharp_gap | close | 1-3k bets | 135-145 | 48.2 | -1.6 | -8.3 |  |
| money_level+money_moving | close | 1-3k bets | 186-175 | 51.5 | -0.9 | -3.7 |  |
| money_level+pin_value | close | 1-3k bets | 62-53 | 53.9 | 4.2 | 0.9 |  |
| money_level+sharp_gap | close | 1-3k bets | 186-174 | 51.7 | -0.6 | -2.9 |  |
| money_moving+pin_value | close | 1-3k bets | 53-67 | 44.2 | -2.1 | -5.9 |  |
| money_moving+sharp_gap | close | 1-3k bets | 249-334 | 42.7 | -3.9 | -11.7 |  |
| pin_value+sharp_gap | close | 1-3k bets | 55-69 | 44.4 | -1.8 | -5.9 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 11-17 | 39.3 | 1.7 | 42.0 |  |
| money_level+pin_rlm | close | 1-3k bets | 16-13 | 55.2 | 4.7 | 5.1 |  |
| pin_rlm+pin_value | close | 1-3k bets | 13-14 | 48.1 | 4.8 | 41.6 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 37-45 | 45.1 | 2.4 | 17.1 |  |
| money_moving+pin_rlm | close | 1-3k bets | 35-45 | 43.8 | 1.3 | 15.4 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 13-7 | 65.0 | 15.4 | 21.6 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 58-51 | 53.2 | 2.9 | 1.4 |  |
| money_level+rlm_ratio | close | 1-3k bets | 27-25 | 51.9 | 1.8 | -1.4 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 57-51 | 52.8 | 2.4 | 0.5 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 58-51 | 53.2 | 2.9 | 1.4 |  |
| follow_move+pin_rlm | close | 1-3k bets | 23-24 | 48.9 | -1.7 | -6.8 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 23-24 | 48.9 | -1.7 | -6.8 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 14-11 | 56.0 | 6.0 | 5.7 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 48.9 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 13-13 | 50.0 | 0.8 | -7.0 |  |
| consensus_gap+money_moving | close | 3k+ bets | 21-41 | 33.9 | -9.0 | 10.7 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-5 | 37.5 | -2.4 | 19.3 |  |
| consensus_gap+pin_value | close | 3k+ bets | 25-27 | 48.1 | 2.7 | 2.1 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 1-3 | 25.0 | -24.4 | -53.2 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 22-41 | 34.9 | -7.8 | 15.0 |  |
| follow_move+money_moving | close | 3k+ bets | 43-52 | 45.3 | -4.5 | -13.9 |  |
| follow_move+pin_rlm | close | 3k+ bets | 13-8 | 61.9 | 11.3 | 19.2 |  |
| follow_move+pin_value | close | 3k+ bets | 19-19 | 50.0 | 0.4 | -6.3 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 21-14 | 60.0 | 9.5 | 14.9 |  |
| follow_move+sharp_gap | close | 3k+ bets | 47-51 | 48.0 | -1.9 | -8.6 |  |
| money_moving+pin_rlm | close | 3k+ bets | 18-18 | 50.0 | 10.7 | 12.9 |  |
| money_moving+pin_value | close | 3k+ bets | 21-29 | 42.0 | -3.6 | -6.7 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 19-13 | 59.4 | 9.0 | 13.4 |  |
| money_moving+sharp_gap | close | 3k+ bets | 102-122 | 45.5 | -0.8 | 0.9 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-5 | 50.0 | 5.1 | -5.2 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 13-8 | 61.9 | 11.3 | 19.2 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 19-18 | 51.4 | 11.7 | 15.2 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 5-4 | 55.6 | 5.4 | 5.3 |  |
| pin_value+sharp_gap | close | 3k+ bets | 21-27 | 43.8 | -1.8 | -2.8 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 21-14 | 60.0 | 9.5 | 14.9 |  |
| money_level+money_moving | close | 3k+ bets | 71-78 | 47.7 | -4.4 | -13.4 |  |
| money_level+sharp_gap | close | 3k+ bets | 70-75 | 48.3 | -3.3 | -11.0 |  |
| follow_move+money_level | close | 3k+ bets | 40-48 | 45.5 | -4.0 | -13.8 |  |
| money_level+rlm_ratio | close | 3k+ bets | 10-7 | 58.8 | 8.5 | 11.7 |  |
| consensus_gap+money_level | close | 3k+ bets | 30-33 | 47.6 | -9.9 | -19.4 |  |
| money_level+pin_value | close | 3k+ bets | 21-29 | 42.0 | -7.5 | -22.7 |  |
| money_level+pin_rlm | close | 3k+ bets | 7-6 | 53.8 | 11.7 | 11.5 |  |
| money_level+money_moving | close | <1k bets | 31-40 | 43.7 | -9.0 | -27.5 |  |
| money_level+sharp_gap | close | <1k bets | 31-40 | 43.7 | -9.0 | -27.5 |  |
| money_moving+sharp_gap | close | <1k bets | 49-60 | 45.0 | -2.3 | -13.6 |  |
| consensus_gap+money_level | close | <1k bets | 12-18 | 40.0 | -15.0 | -36.1 |  |
| consensus_gap+money_moving | close | <1k bets | 11-23 | 32.4 | -8.9 | -30.1 |  |
| consensus_gap+pin_value | close | <1k bets | 9-8 | 52.9 | 9.6 | 15.9 |  |
| consensus_gap+sharp_gap | close | <1k bets | 11-24 | 31.4 | -9.3 | -32.1 |  |
| money_level+pin_value | close | <1k bets | 9-7 | 56.2 | 5.2 | 3.6 |  |
| money_moving+pin_value | close | <1k bets | 9-5 | 64.3 | 17.9 | 39.6 |  |
| pin_value+sharp_gap | close | <1k bets | 9-5 | 64.3 | 17.9 | 39.6 |  |
| follow_move+money_moving | close | <1k bets | 16-23 | 41.0 | -8.7 | -22.0 |  |
| follow_move+sharp_gap | close | <1k bets | 16-23 | 41.0 | -8.7 | -22.0 |  |
| follow_move+money_level | close | <1k bets | 11-25 | 30.6 | -18.8 | -42.3 |  |
| consensus_gap+pin_rlm | close | <1k bets | 2-2 | 50.0 | 26.5 | 50.5 |  |
| money_moving+pin_rlm | close | <1k bets | 11-7 | 61.1 | 19.3 | 31.8 |  |
| pin_rlm+sharp_gap | close | <1k bets | 11-7 | 61.1 | 19.3 | 31.8 |  |
| consensus_gap+follow_move | close | <1k bets | 2-6 | 25.0 | -23.9 | -54.2 |  |
| follow_move+pin_rlm | close | <1k bets | 7-1 | 87.5 | 36.7 | 67.9 |  |
| follow_move+pin_value | close | <1k bets | 11-2 | 84.6 | 34.9 | 60.9 |  |
| follow_move+rlm_ratio | close | <1k bets | 7-2 | 77.8 | 26.9 | 49.3 |  |
| money_moving+rlm_ratio | close | <1k bets | 7-2 | 77.8 | 26.9 | 49.3 |  |
| pin_rlm+pin_value | close | <1k bets | 4-0 | 100.0 | 48.9 | 91.6 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 7-1 | 87.5 | 36.7 | 67.9 |  |
| pin_value+rlm_ratio | close | <1k bets | 3-0 | 100.0 | 48.9 | 91.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 7-2 | 77.8 | 26.9 | 49.3 |  |
| money_level+rlm_ratio | close | <1k bets | 1-2 | 33.3 | -17.8 | -36.9 |  |
| money_level+pin_rlm | close | <1k bets | 3-1 | 75.0 | 37.7 | 56.8 |  |
| consensus_gap+follow_move | close | pin $1-2k | 20-20 | 50.0 | 0.8 | -6.8 |  |
| consensus_gap+money_moving | close | pin $1-2k | 36-48 | 42.9 | -4.0 | -2.3 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 11-12 | 47.8 | 7.2 | 53.0 |  |
| consensus_gap+pin_value | close | pin $1-2k | 44-49 | 47.3 | 1.9 | -2.3 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 8-6 | 57.1 | 7.8 | 6.4 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 36-45 | 44.4 | -2.1 | 1.3 |  |
| follow_move+money_moving | close | pin $1-2k | 65-94 | 40.9 | -8.8 | -22.4 |  |
| follow_move+pin_rlm | close | pin $1-2k | 19-15 | 55.9 | 5.5 | 6.3 |  |
| follow_move+pin_value | close | pin $1-2k | 35-33 | 51.5 | 1.9 | -3.4 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 28-27 | 50.9 | 0.8 | -3.5 |  |
| follow_move+sharp_gap | close | pin $1-2k | 67-92 | 42.1 | -7.6 | -20.0 |  |
| money_moving+pin_rlm | close | pin $1-2k | 30-25 | 54.5 | 11.0 | 36.0 |  |
| money_moving+pin_value | close | pin $1-2k | 39-47 | 45.3 | -1.5 | -8.6 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 27-26 | 50.9 | 0.9 | -3.6 |  |
| money_moving+sharp_gap | close | pin $1-2k | 133-158 | 45.7 | -2.6 | -6.0 |  |
| pin_rlm+pin_value | close | pin $1-2k | 9-11 | 45.0 | -2.6 | -0.7 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 19-15 | 55.9 | 5.5 | 6.3 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 32-25 | 56.1 | 12.3 | 38.0 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 11-10 | 52.4 | 2.5 | -1.8 |  |
| pin_value+sharp_gap | close | pin $1-2k | 39-45 | 46.4 | -0.4 | -6.5 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 28-27 | 50.9 | 0.8 | -3.5 |  |
| follow_move+money_level | close | pin $1-2k | 63-86 | 42.3 | -7.2 | -19.9 |  |
| money_level+rlm_ratio | close | pin $1-2k | 16-14 | 53.3 | 3.6 | 0.3 |  |
| money_level+sharp_gap | close | pin $1-2k | 99-108 | 47.8 | -3.8 | -10.8 |  |
| money_level+money_moving | close | pin $1-2k | 97-111 | 46.6 | -5.1 | -13.0 |  |
| consensus_gap+money_level | close | pin $1-2k | 41-38 | 51.9 | -4.3 | -8.1 |  |
| money_level+pin_value | close | pin $1-2k | 42-39 | 51.9 | 2.0 | -3.3 |  |
| money_level+pin_rlm | close | pin $1-2k | 15-9 | 62.5 | 15.6 | 25.1 |  |
| follow_move+money_level | close | pin $2k+ | 29-31 | 48.3 | -1.1 | -8.2 |  |
| follow_move+money_moving | close | pin $2k+ | 31-36 | 46.3 | -3.5 | -12.0 |  |
| follow_move+sharp_gap | close | pin $2k+ | 32-36 | 47.1 | -2.7 | -10.5 |  |
| money_level+money_moving | close | pin $2k+ | 61-69 | 46.9 | -5.9 | -14.8 |  |
| money_level+sharp_gap | close | pin $2k+ | 60-71 | 45.8 | -7.0 | -15.9 |  |
| money_moving+sharp_gap | close | pin $2k+ | 86-133 | 39.3 | -5.9 | -19.3 |  |
| consensus_gap+money_moving | close | pin $2k+ | 16-41 | 28.1 | -14.8 | -27.0 |  |
| consensus_gap+pin_value | close | pin $2k+ | 26-29 | 47.3 | 5.8 | 10.6 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 17-44 | 27.9 | -16.4 | -29.6 |  |
| money_moving+pin_value | close | pin $2k+ | 24-34 | 41.4 | -1.6 | 0.3 |  |
| pin_value+sharp_gap | close | pin $2k+ | 24-35 | 40.7 | -2.0 | -1.4 |  |
| consensus_gap+follow_move | close | pin $2k+ | 7-4 | 63.6 | 14.5 | 17.6 |  |
| follow_move+pin_value | close | pin $2k+ | 16-10 | 61.5 | 12.2 | 15.1 |  |
| follow_move+pin_rlm | close | pin $2k+ | 6-11 | 35.3 | -15.6 | -32.4 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 10-12 | 45.5 | -5.2 | -13.1 |  |
| money_level+pin_rlm | close | pin $2k+ | 4-7 | 36.4 | -6.8 | -28.9 |  |
| money_level+pin_value | close | pin $2k+ | 25-26 | 49.0 | -1.0 | -10.2 |  |
| money_level+rlm_ratio | close | pin $2k+ | 4-6 | 40.0 | -10.7 | -23.5 |  |
| money_moving+pin_rlm | close | pin $2k+ | 13-34 | 27.7 | -6.3 | -30.5 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 10-12 | 45.5 | -5.2 | -13.1 |  |
| pin_rlm+pin_value | close | pin $2k+ | 3-6 | 33.3 | 0.6 | 32.8 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 6-11 | 35.3 | -15.6 | -32.4 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 13-34 | 27.7 | -6.3 | -30.5 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 1-1 | 50.0 | -1.1 | -6.2 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 10-12 | 45.5 | -5.2 | -13.1 |  |
| consensus_gap+money_level | close | pin $2k+ | 39-28 | 58.2 | -6.1 | -11.0 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 2-11 | 15.4 | -12.4 | -22.5 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -51.1 | -100.0 |  |
| money_level+money_moving | close | pin limit <$1k | 33-40 | 45.2 | -4.7 | -13.6 |  |
| money_level+sharp_gap | close | pin limit <$1k | 34-40 | 45.9 | -4.0 | -12.2 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 59-63 | 48.4 | -1.5 | -0.1 |  |
| consensus_gap+money_level | close | pin limit <$1k | 18-19 | 48.6 | -1.2 | -10.4 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 23-27 | 46.0 | -2.7 | -4.6 |  |
| follow_move+money_moving | close | pin limit <$1k | 41-41 | 50.0 | -0.2 | -4.3 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 42-41 | 50.6 | 0.3 | -3.1 |  |
| money_level+pin_value | close | pin limit <$1k | 25-24 | 51.0 | 1.8 | -3.7 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 11-8 | 57.9 | 8.8 | 8.4 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 14-13 | 51.9 | 3.7 | 14.2 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 15-14 | 51.7 | 3.2 | 12.7 |  |
| follow_move+money_level | close | pin limit <$1k | 31-30 | 50.8 | 1.2 | -3.2 |  |
| follow_move+pin_value | close | pin limit <$1k | 23-15 | 60.5 | 10.9 | 14.5 |  |
| money_moving+pin_value | close | pin limit <$1k | 20-20 | 50.0 | 1.0 | 6.0 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 22-21 | 51.2 | 1.9 | 7.4 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 3-1 | 75.0 | 32.4 | 152.0 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 21-11 | 65.6 | 16.5 | 53.7 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 10-2 | 83.3 | 35.1 | 96.3 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 22-11 | 66.7 | 17.5 | 54.8 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 18-7 | 72.0 | 21.2 | 38.4 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 24-14 | 63.2 | 12.4 | 21.4 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 23-14 | 62.2 | 11.4 | 19.5 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 18-7 | 72.0 | 21.2 | 38.4 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 24-14 | 63.2 | 12.4 | 21.4 |  |
| money_level+pin_rlm | close | pin limit <$1k | 7-4 | 63.6 | 12.7 | 21.9 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 7-6 | 53.8 | 3.1 | 3.7 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 10-4 | 71.4 | 21.0 | 36.9 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 3-2 | 60.0 | 10.7 | 13.8 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 48.9 | 87.7 |  |
| pin_rlm | early | <1k bets | 1-1 | 50.0 | 26.5 | -3.7 | -2.15 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -23.5 | -100.0 | -4.8 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 76.5 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 15-16 | 48.4 | -1.3 | -7.7 | -0.1 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -50.0 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 119-113 | 51.3 | 1.6 | -1.8 | 0.27 |
| follow_move | early | pin $1-2k | 10-8 | 55.6 | 5.6 | 5.0 | -0.06 |
| follow_move | early | pin limit <$1k | 33-29 | 53.2 | 3.6 | 1.1 | -0.35 |
| rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 15.9 | 29.2 | -0.5 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -51.1 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 2-1 | 66.7 | 15.6 | 28.7 | 0.67 |
| rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -1.1 | -1.0 | -0.5 |
| rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 29.3 | 53.6 | -0.4 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | -0.0 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 41.2 | 59.7 | 0.33 |
| money_level | early | <1k bets | 58-30 | 65.9 | 4.9 | 5.5 | 0.57 |
| money_level | early | pin $1-2k | 14-8 | 63.6 | -1.9 | -3.2 | 0.01 |
| money_level | early | pin limit <$1k | 22-24 | 47.8 | -6.3 | -12.1 | 0.31 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 8.0 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 7.1 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 44-34 | 56.4 | 7.6 | 15.5 | 0.71 |
| sharp_gap | early | pin $1-2k | 11-9 | 55.0 | 3.5 | 13.8 | -0.57 |
| sharp_gap | early | pin limit <$1k | 27-16 | 62.8 | 14.5 | 30.8 | 0.2 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.4 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.0 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 29-22 | 56.9 | 3.9 | -5.9 | 0.05 |
| money_moving | early | pin $1-2k | 6-6 | 50.0 | -13.1 | -26.9 | 0.35 |
| money_moving | early | pin limit <$1k | 20-9 | 69.0 | 19.9 | 47.8 | 0.36 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.5 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 51.1 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 30-32 | 48.4 | 0.7 | -8.3 | 0.21 |
| pin_value | early | pin $1-2k | 11-14 | 44.0 | -0.4 | -16.7 | 0.17 |
| pin_value | early | pin limit <$1k | 32-27 | 54.2 | 4.8 | 2.5 | 0.15 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -48.9 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -26.1 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.4 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 13.8 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 98-136 | 41.9 | -4.0 | -15.2 | 0.36 |
| consensus_gap | early | pin $1-2k | 10-16 | 38.5 | -7.3 | -24.8 | 0.47 |
| consensus_gap | early | pin limit <$1k | 17-32 | 34.7 | -16.1 | -27.7 | 0.33 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 16.1 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 4.0 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 3.8 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.5 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 20.0 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.3 | 26.0 | -0.25 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 3.4 | -6.9 | 0.3 |
| consensus_gap+follow_move | early | 1-3k bets | 4-4 | 50.0 | 1.1 | -6.9 | 0.25 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -23.0 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -1.4 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 10-10 | 50.0 | 0.1 | -4.1 | 0.05 |
| follow_move+pin_value | early | 1-3k bets | 7-5 | 58.3 | 8.7 | 9.2 | -0.42 |
| follow_move+sharp_gap | early | 1-3k bets | 9-8 | 52.9 | 2.9 | 1.2 | -0.18 |
| follow_move+rlm_ratio | early | 1-3k bets | 4-2 | 66.7 | 15.9 | 29.2 | -0.5 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.9 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 4-2 | 66.7 | 15.9 | 29.2 | -0.5 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 18.3 | 56.1 | 0.15 |
| follow_move+money_moving | early | 1-3k bets | 9-4 | 69.2 | 19.5 | 32.1 | 0.08 |
| money_moving+rlm_ratio | early | 1-3k bets | 2-1 | 66.7 | 16.3 | 28.7 | -1.0 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 51.1 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 51.1 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 51.1 | 83.3 | 1.0 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -51.1 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -51.1 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.0 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 51.1 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 51.1 | 83.3 | 1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -51.1 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 36.2 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 48.9 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 9-9 | 50.0 | 0.4 | -6.2 | 1.33 |
| consensus_gap+money_level | early | <1k bets | 12-11 | 52.2 | -12.5 | -21.3 | 0.8 |
| consensus_gap+sharp_gap | early | <1k bets | 9-17 | 34.6 | -10.2 | 2.0 | 1.13 |
| follow_move+money_level | early | <1k bets | 14-5 | 73.7 | 24.6 | 40.2 | 0.95 |
| follow_move+sharp_gap | early | <1k bets | 13-5 | 72.2 | 22.7 | 37.7 | 1.0 |
| money_level+sharp_gap | early | <1k bets | 35-16 | 68.6 | 11.9 | 15.1 | 1.09 |
| money_level+money_moving | early | <1k bets | 22-13 | 62.9 | 3.5 | -1.0 | -0.12 |
| money_moving+sharp_gap | early | <1k bets | 19-14 | 57.6 | 7.0 | -0.4 | 0.25 |
| consensus_gap+money_moving | early | <1k bets | 5-9 | 35.7 | -10.3 | -42.1 | 0.26 |
| follow_move+pin_value | early | <1k bets | 11-10 | 52.4 | 2.7 | -1.5 | 0.29 |
| follow_move+money_moving | early | <1k bets | 6-3 | 66.7 | 17.3 | 27.7 | 0.0 |
| consensus_gap+pin_value | early | <1k bets | 11-21 | 34.4 | -11.2 | -35.3 | 0.5 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -23.5 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -23.5 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | <1k bets | 1-1 | 50.0 | 26.5 | -3.7 | -2.15 |
| pin_value+sharp_gap | early | <1k bets | 4-3 | 57.1 | 11.2 | 9.1 | 0.03 |
| money_level+pin_value | early | <1k bets | 3-3 | 50.0 | 0.4 | -4.5 | 1.33 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -51.1 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -51.1 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 2.5 |
| follow_move+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 15.6 | 28.7 | 0.67 |
| money_level+rlm_ratio | early | <1k bets | 2-0 | 100.0 | 48.9 | 93.0 | 0.5 |
| money_moving+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 48.9 | 95.2 | 0.0 |
| rlm_ratio+sharp_gap | early | <1k bets | 2-1 | 66.7 | 15.6 | 28.7 | 0.67 |
| consensus_gap+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -51.1 | -100.0 | 1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 48.9 | 90.9 | 1.0 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 76.5 | 92.6 | 0.5 |
| consensus_gap+money_level | early | pin $1-2k | 4-4 | 50.0 | -16.1 | -22.9 | 0.44 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -33.9 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 4-9 | 30.8 | -8.5 | -42.5 | 0.4 |
| follow_move+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -1.1 | -1.0 | -0.5 |
| follow_move+sharp_gap | early | pin $1-2k | 3-1 | 75.0 | 25.0 | 45.0 | -0.25 |
| money_level+money_moving | early | pin $1-2k | 6-5 | 54.5 | -12.1 | -20.3 | 0.02 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -9.3 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 1-1 | 50.0 | -1.1 | -1.0 | -0.5 |
| money_level+sharp_gap | early | pin $1-2k | 8-4 | 66.7 | 3.4 | 8.4 | -0.41 |
| money_moving+sharp_gap | early | pin $1-2k | 3-5 | 37.5 | -22.3 | -45.3 | -0.06 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -7.8 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 2-2 | 50.0 | 0.0 | -8.4 | 0.75 |
| follow_move+money_level | early | pin $1-2k | 3-2 | 60.0 | 10.7 | 16.0 | 0.2 |
| follow_move+pin_value | early | pin $1-2k | 4-3 | 57.1 | 7.3 | 6.9 | 0.29 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 48.9 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 1-0 | 100.0 | 51.1 | 90.9 | 0.0 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -23.5 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -25.0 | -62.8 | -0.72 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -23.5 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -23.5 | -100.0 | -4.8 |
| money_level+money_moving | early | pin limit <$1k | 11-7 | 61.1 | 8.0 | 12.1 | 0.53 |
| money_level+sharp_gap | early | pin limit <$1k | 18-14 | 56.2 | 5.3 | 2.3 | 0.25 |
| money_moving+sharp_gap | early | pin limit <$1k | 16-5 | 76.2 | 28.6 | 68.0 | 0.39 |
| money_level+pin_value | early | pin limit <$1k | 8-5 | 61.5 | 11.1 | 16.6 | 0.46 |
| money_moving+pin_value | early | pin limit <$1k | 6-4 | 60.0 | 10.0 | 13.0 | 0.3 |
| pin_value+sharp_gap | early | pin limit <$1k | 11-5 | 68.8 | 18.6 | 30.3 | 0.06 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-7 | 46.2 | -2.9 | -14.2 | 0.46 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -27.8 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 13-17 | 43.3 | -5.5 | -18.8 | 0.49 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.5 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 8-7 | 53.3 | 3.4 | 1.9 | 0.07 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 4.3 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 9-7 | 56.2 | 6.2 | 6.9 | -0.31 |
| follow_move+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 29.3 | 53.6 | -0.4 |
| money_level+rlm_ratio | early | pin limit <$1k | 4-0 | 100.0 | 48.9 | 92.0 | 0.25 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 16.3 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 4-1 | 80.0 | 29.3 | 53.6 | -0.4 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 23.0 | 72.3 | 0.54 |
| follow_move+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 20.2 | 33.3 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 16.3 | 28.7 | -1.0 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -51.1 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -51.1 | -100.0 | 1.0 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 76.5 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 76.5 | 92.6 | 0.5 |
