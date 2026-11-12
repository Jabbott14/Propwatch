# NFL scorecard

Generated 2026-11-12 18:22 UTC. 28 graded games (0 finished games had no final score and are not graded).

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before kickoff. Break-even at -110 is 52.4%. CLV = points of
closing-line value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured on
this sample. `edge` is hit% minus that. A signal that is structurally long dogs or
unders will beat 50% in any week dogs or unders run, which is not an edge --
this sample ran **67.9% favourites** (n=28)
**50.0% overs** (n=28) and **82.1% moneyline favourites** (n=28) and **44.6% team-total overs** (n=56).

Moneyline has no handicap, so its `follow_move` reads price, its CLV is
percentage points of implied probability, and `pin_value` is a pure price
comparison against Pinnacle's no-vig fair -- no half-points involved.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

**Gate B is these signals. Gate A is the Pinnacle columns on the board — a price
floor, never a veto.** EV against Pinnacle can essentially never be positive,
because Pinnacle is the fair-value definition. Using it as a veto rejects every
signal this system exists to find. See fault 4 in propwatch-news-vs-coherence.md.

## EARLY

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 0-2 | 0.0 | 17.9 | -17.9 | -2.0 | -100.0 | -4.4 | 50.0 | keep collecting (2/30) |
| follow_move | both | 24-9 | 72.7 | 70.6 | 2.2 | +3.92 | 11.9 | -0.17 | 30.3 | beats break-even but not its base rate -- directional bias, not signal |
| rlm | both | 0-2 | 0.0 | 32.1 | -32.1 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| rlm_ratio | both | 0-1 | 0.0 | 32.1 | -32.1 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level | both | 37-21 | 63.8 | 61.0 | 2.8 | +4.26 | 7.3 | -0.81 | 15.5 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 30-29 | 50.8 | 51.3 | -0.5 | -5.24 | -8.9 | -0.1 | 28.8 | no edge shown yet |
| money_moving | both | 10-6 | 62.5 | 57.4 | 5.1 | +1.61 | 10.1 | -0.23 | 25.0 | keep collecting (16/30) |
| pin_value | both | 20-16 | 55.6 | 47.7 | 7.9 | +1.4 | 3.9 | 0.33 | 30.6 | no edge shown yet |
| book_lag | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | -0.75 | 50.0 | keep collecting (2/30) |
| consensus_gap | both | 10-19 | 34.5 | 31.7 | 2.8 | -10.09 | -34.8 | 0.24 | 44.8 | keep collecting (29/30) |
| follow_move+rlm | both | 0-2 | 0.0 | 32.1 | -32.1 | -2.0 | -100.0 | 0.5 | 50.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | both | 0-1 | 0.0 | 32.1 | -32.1 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 14-5 | 73.7 | 67.1 | 6.6 | +3.35 | 17.6 | -0.09 | 21.1 | keep collecting (19/30) |
| rlm+rlm_ratio | both | 0-1 | 0.0 | 32.1 | -32.1 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 0-1 | 0.0 | 32.1 | -32.1 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| rlm_ratio+sharp_gap | both | 0-1 | 0.0 | 32.1 | -32.1 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_value | both | 6-2 | 75.0 | 58.9 | 16.1 | +3.46 | 43.3 | -0.44 | 0.0 | keep collecting (8/30) |
| money_level+sharp_gap | both | 24-16 | 60.0 | 59.6 | 0.4 | +1.54 | 3.9 | -0.59 | 15.0 | no edge shown yet |
| pin_value+sharp_gap | both | 7-5 | 58.3 | 46.4 | 11.9 | +1.3 | 10.8 | 0.47 | 25.0 | keep collecting (12/30) |
| follow_move+money_level | both | 21-6 | 77.8 | 74.1 | 3.7 | +4.56 | 16.9 | -0.74 | 25.9 | keep collecting (27/30) |
| consensus_gap+pin_value | both | 2-4 | 33.3 | 28.6 | 4.8 | -2.4 | -40.0 | 1.58 | 66.7 | keep collecting (6/30) |
| follow_move+pin_value | both | 4-0 | 100.0 | 58.9 | 41.1 | +3.47 | 86.7 | 0.0 | 0.0 | keep collecting (4/30) |
| consensus_gap+follow_move | both | 3-0 | 100.0 | 77.4 | 22.6 | +1.75 | 58.5 | -0.23 | 33.3 | keep collecting (3/30) |
| consensus_gap+money_level | both | 4-1 | 80.0 | 63.6 | 16.4 | +1.62 | 32.5 | -2.26 | 20.0 | keep collecting (5/30) |
| consensus_gap+sharp_gap | both | 6-10 | 37.5 | 35.3 | 2.2 | -4.63 | -29.0 | 0.12 | 50.0 | keep collecting (16/30) |
| follow_move+money_moving | both | 6-1 | 85.7 | 76.0 | 9.7 | +2.83 | 40.4 | -0.44 | 28.6 | keep collecting (7/30) |
| money_level+money_moving | both | 8-3 | 72.7 | 64.9 | 7.8 | +2.83 | 25.7 | -0.74 | 18.2 | keep collecting (11/30) |
| money_moving+pin_value | both | 4-2 | 66.7 | 50.6 | 16.1 | +1.69 | 28.2 | 1.0 | 33.3 | keep collecting (6/30) |
| money_moving+sharp_gap | both | 4-3 | 57.1 | 57.7 | -0.5 | +0.25 | 3.6 | -0.09 | 14.3 | keep collecting (7/30) |
| book_lag+consensus_gap | both | 0-1 | 0.0 | 32.1 | -32.1 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+pin_rlm | both | 0-2 | 0.0 | 17.9 | -17.9 | -2.0 | -100.0 | -4.4 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-1 | 0.0 | 17.9 | -17.9 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | both | 0-2 | 0.0 | 17.9 | -17.9 | -2.0 | -100.0 | -4.4 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+money_level | both | 0-1 | 0.0 | 67.9 | -67.9 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+money_moving | both | 0-1 | 0.0 | 67.9 | -67.9 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+sharp_gap | both | 0-1 | 0.0 | 67.9 | -67.9 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+money_moving | both | 0-1 | 0.0 | 17.9 | -17.9 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 17.9 | -17.9 | -1.0 | -100.0 | 1.8 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 0-2 | 0.0 | 17.9 | -17.9 | -2.0 | -100.0 | -4.4 | 50.0 | keep collecting (2/30) |
| follow_move | moneyline | 17-3 | 85.0 | 82.1 | 2.9 | +3.68 | 18.4 | -0.28 | 35.0 | keep collecting (20/30) |
| follow_move | spread | 7-5 | 58.3 | 53.0 | 5.4 | +1.24 | 10.3 | 0.25 | 25.0 | keep collecting (12/30) |
| follow_move | total | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | -3.0 | 0.0 | keep collecting (1/30) |
| rlm | spread | 0-2 | 0.0 | 32.1 | -32.1 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 32.1 | -32.1 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level | moneyline | 16-3 | 84.2 | 78.8 | 5.5 | +2.98 | 15.7 | -1.55 | 26.3 | keep collecting (19/30) |
| money_level | spread | 12-7 | 63.2 | 54.7 | 8.5 | +4.08 | 21.5 | -0.24 | 10.5 | keep collecting (19/30) |
| money_level | total | 9-11 | 45.0 | 50.0 | -5.0 | -2.81 | -14.0 | -0.65 | 10.0 | keep collecting (20/30) |
| sharp_gap | moneyline | 10-10 | 50.0 | 46.8 | 3.2 | -4.32 | -21.6 | -0.07 | 40.0 | keep collecting (20/30) |
| sharp_gap | spread | 9-11 | 45.0 | 57.1 | -12.1 | -2.89 | -14.5 | 0.07 | 25.0 | keep collecting (20/30) |
| sharp_gap | total | 11-8 | 57.9 | 50.0 | 7.9 | +1.97 | 10.4 | -0.32 | 21.1 | keep collecting (19/30) |
| money_moving | moneyline | 4-2 | 66.7 | 60.7 | 6.0 | +0.02 | 0.3 | 0.07 | 50.0 | keep collecting (6/30) |
| money_moving | spread | 4-3 | 57.1 | 57.7 | -0.5 | +0.72 | 10.2 | -0.43 | 14.3 | keep collecting (7/30) |
| money_moving | total | 2-1 | 66.7 | 50.0 | 16.7 | +0.88 | 29.3 | -0.33 | 0.0 | keep collecting (3/30) |
| pin_value | moneyline | 0-5 | 0.0 | 17.9 | -17.9 | -5.0 | -100.0 | 2.28 | 100.0 | keep collecting (5/30) |
| pin_value | spread | 9-1 | 90.0 | 57.1 | 32.9 | +6.94 | 69.4 | -0.25 | 10.0 | keep collecting (10/30) |
| pin_value | total | 3-5 | 37.5 | 50.0 | -12.5 | -2.26 | -28.2 | -0.25 | 12.5 | keep collecting (8/30) |
| pin_value | tt_away | 3-3 | 50.0 | 50.0 | -0.0 | -0.47 | -7.8 | 0.33 | 33.3 | keep collecting (6/30) |
| pin_value | tt_home | 5-2 | 71.4 | 50.8 | 20.7 | +2.18 | 31.2 | 0.43 | 28.6 | keep collecting (7/30) |
| book_lag | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | -0.75 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 5-15 | 25.0 | 24.3 | 0.7 | -10.36 | -51.8 | 0.3 | 55.0 | keep collecting (20/30) |
| consensus_gap | spread | 5-4 | 55.6 | 48.0 | 7.5 | +0.27 | 3.0 | 0.11 | 22.2 | keep collecting (9/30) |
| follow_move+money_level | moneyline | 16-2 | 88.9 | 82.1 | 6.7 | +3.98 | 22.1 | -1.05 | 27.8 | keep collecting (18/30) |
| follow_move+sharp_gap | moneyline | 8-1 | 88.9 | 82.1 | 6.7 | +1.94 | 21.6 | -0.41 | 22.2 | keep collecting (9/30) |
| money_level+sharp_gap | moneyline | 8-2 | 80.0 | 75.7 | 4.3 | +0.94 | 9.4 | -1.43 | 20.0 | keep collecting (10/30) |
| consensus_gap+sharp_gap | moneyline | 4-9 | 30.8 | 27.7 | 3.0 | -5.33 | -41.0 | 0.12 | 53.8 | keep collecting (13/30) |
| follow_move+money_moving | moneyline | 4-0 | 100.0 | 82.1 | 17.9 | +2.02 | 50.4 | -0.78 | 50.0 | keep collecting (4/30) |
| money_level+money_moving | moneyline | 4-0 | 100.0 | 82.1 | 17.9 | +2.02 | 50.4 | -0.78 | 50.0 | keep collecting (4/30) |
| consensus_gap+follow_move | moneyline | 2-0 | 100.0 | 82.1 | 17.9 | +0.94 | 46.8 | -0.35 | 50.0 | keep collecting (2/30) |
| consensus_gap+money_level | moneyline | 2-1 | 66.7 | 60.7 | 6.0 | -0.06 | -2.2 | -3.77 | 33.3 | keep collecting (3/30) |
| consensus_gap+pin_value | moneyline | 0-4 | 0.0 | 17.9 | -17.9 | -4.0 | -100.0 | 2.38 | 100.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | moneyline | 0-2 | 0.0 | 17.9 | -17.9 | -2.0 | -100.0 | -4.4 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 17.9 | -17.9 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | moneyline | 0-2 | 0.0 | 17.9 | -17.9 | -2.0 | -100.0 | -4.4 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.61 | -30.4 | 0.7 | 50.0 | keep collecting (2/30) |
| pin_value+sharp_gap | moneyline | 0-3 | 0.0 | 17.9 | -17.9 | -3.0 | -100.0 | 3.03 | 100.0 | keep collecting (3/30) |
| consensus_gap+money_moving | moneyline | 0-1 | 0.0 | 17.9 | -17.9 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 17.9 | -17.9 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 17.9 | -17.9 | -1.0 | -100.0 | 1.8 | 100.0 | keep collecting (1/30) |
| follow_move+rlm | spread | 0-2 | 0.0 | 32.1 | -32.1 | -2.0 | -100.0 | 0.5 | 50.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 32.1 | -32.1 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 6-4 | 60.0 | 53.6 | 6.4 | +1.41 | 14.1 | 0.2 | 20.0 | keep collecting (10/30) |
| rlm+rlm_ratio | spread | 0-1 | 0.0 | 32.1 | -32.1 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 0-1 | 0.0 | 32.1 | -32.1 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 32.1 | -32.1 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+pin_value | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.6 | 80.0 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+sharp_gap | spread | 8-7 | 53.3 | 58.3 | -5.0 | +0.27 | 1.8 | -0.1 | 13.3 | keep collecting (15/30) |
| follow_move+pin_value | spread | 4-0 | 100.0 | 58.9 | 41.1 | +3.47 | 86.7 | 0.0 | 0.0 | keep collecting (4/30) |
| pin_value+sharp_gap | spread | 5-0 | 100.0 | 60.7 | 39.3 | +4.46 | 89.2 | -0.3 | 0.0 | keep collecting (5/30) |
| consensus_gap+follow_move | spread | 1-0 | 100.0 | 67.9 | 32.1 | +0.82 | 82.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 2-0 | 100.0 | 67.9 | 32.1 | +1.69 | 84.5 | 0.0 | 0.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | spread | 2-1 | 66.7 | 67.9 | -1.2 | +0.69 | 23.0 | 0.17 | 33.3 | keep collecting (3/30) |
| follow_move+money_level | spread | 5-3 | 62.5 | 58.9 | 3.6 | +1.57 | 19.7 | 0.25 | 25.0 | keep collecting (8/30) |
| money_level+pin_value | spread | 4-0 | 100.0 | 67.9 | 32.1 | +3.63 | 90.7 | -0.38 | 0.0 | keep collecting (4/30) |
| follow_move+money_moving | spread | 2-1 | 66.7 | 67.9 | -1.2 | +0.81 | 27.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_level+money_moving | spread | 2-2 | 50.0 | 58.9 | -8.9 | -0.07 | -1.7 | -1.0 | 0.0 | keep collecting (4/30) |
| money_moving+pin_value | spread | 3-1 | 75.0 | 58.9 | 16.1 | +1.76 | 44.1 | 0.25 | 25.0 | keep collecting (4/30) |
| money_moving+sharp_gap | spread | 1-2 | 33.3 | 67.9 | -34.5 | -1.02 | -34.0 | -0.67 | 0.0 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 32.1 | -32.1 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| book_lag+money_level | spread | 0-1 | 0.0 | 67.9 | -67.9 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+money_moving | spread | 0-1 | 0.0 | 67.9 | -67.9 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+sharp_gap | spread | 0-1 | 0.0 | 67.9 | -67.9 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.16 | -4.1 | -0.5 | 0.0 | keep collecting (4/30) |
| money_level+sharp_gap | total | 8-7 | 53.3 | 50.0 | 3.3 | +0.32 | 2.2 | -0.53 | 13.3 | keep collecting (15/30) |
| pin_value+sharp_gap | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.16 | -4.1 | -0.5 | 0.0 | keep collecting (4/30) |
| follow_move+money_level | total | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | -3.0 | 0.0 | redundant -- identical record to follow_move alone, not independent confirmation |
| money_level+money_moving | total | 2-1 | 66.7 | 50.0 | 16.7 | +0.88 | 29.3 | -0.33 | 0.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| money_moving+sharp_gap | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.88 | 93.9 | 0.0 | 0.0 | keep collecting (2/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 50.0 | 50.0 | +0.93 | 92.6 | 0.0 | 0.0 | keep collecting (1/30) |

## CLOSE

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 3-8 | 27.3 | 35.4 | -8.1 | -5.31 | -48.3 |  |  | keep collecting (11/30) |
| follow_move | both | 48-32 | 60.0 | 63.2 | -3.2 | -0.21 | -0.3 |  |  | no edge shown yet |
| rlm | both | 4-12 | 25.0 | 50.9 | -25.9 | -8.44 | -52.8 |  |  | keep collecting (16/30) |
| rlm_ratio | both | 3-6 | 33.3 | 53.6 | -20.2 | -3.31 | -36.8 |  |  | keep collecting (9/30) |
| money_level | both | 54-30 | 64.3 | 60.5 | 3.7 | +8.81 | 10.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 36-45 | 44.4 | 49.2 | -4.7 | -15.76 | -19.5 |  |  | no edge shown yet |
| money_moving | both | 24-31 | 43.6 | 43.0 | 0.6 | -11.31 | -20.6 |  |  | no edge shown yet |
| pin_value | both | 37-29 | 56.1 | 48.5 | 7.5 | +2.45 | 3.7 |  |  | no edge shown yet |
| book_lag | both | 4-0 | 100.0 | 58.9 | 41.1 | +3.29 | 82.4 |  |  | keep collecting (4/30) |
| consensus_gap | both | 12-23 | 34.3 | 30.3 | 4.0 | -10.23 | -29.2 |  |  | DROP: below break-even |
| follow_move+rlm | both | 4-12 | 25.0 | 50.9 | -25.9 | -8.44 | -52.8 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | both | 3-6 | 33.3 | 53.6 | -20.2 | -3.31 | -36.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 19-15 | 55.9 | 63.7 | -7.8 | -3.51 | -10.3 |  |  | no edge shown yet |
| money_level+pin_value | both | 9-4 | 69.2 | 58.0 | 11.3 | +3.61 | 27.8 |  |  | keep collecting (13/30) |
| rlm+rlm_ratio | both | 3-6 | 33.3 | 53.6 | -20.2 | -3.31 | -36.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 3-10 | 23.1 | 48.4 | -25.3 | -7.31 | -56.2 |  |  | keep collecting (13/30) |
| rlm_ratio+sharp_gap | both | 3-6 | 33.3 | 53.6 | -20.2 | -3.31 | -36.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 26-19 | 57.8 | 58.6 | -0.8 | -0.69 | -1.5 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 6-1 | 85.7 | 52.6 | 33.2 | +3.93 | 56.1 |  |  | keep collecting (7/30) |
| follow_move+money_level | both | 30-10 | 75.0 | 73.7 | 1.3 | +6.35 | 15.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+sharp_gap | both | 4-9 | 30.8 | 28.8 | 1.9 | -3.74 | -28.8 |  |  | keep collecting (13/30) |
| follow_move+pin_value | both | 8-3 | 72.7 | 59.9 | 12.8 | +3.61 | 32.8 |  |  | keep collecting (11/30) |
| pin_value+rlm | both | 2-2 | 50.0 | 54.5 | -4.5 | -0.26 | -6.5 |  |  | keep collecting (4/30) |
| pin_value+sharp_gap | both | 10-7 | 58.8 | 47.3 | 11.6 | +1.22 | 7.2 |  |  | keep collecting (17/30) |
| consensus_gap+pin_value | both | 2-5 | 28.6 | 19.9 | 8.7 | -3.26 | -46.5 |  |  | keep collecting (7/30) |
| book_lag+consensus_gap | both | 3-0 | 100.0 | 56.0 | 44.0 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| book_lag+money_moving | both | 1-0 | 100.0 | 32.1 | 67.9 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | both | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | both | 3-8 | 27.3 | 19.2 | 8.1 | -4.8 | -43.6 |  |  | keep collecting (11/30) |
| money_moving+pin_value | both | 10-6 | 62.5 | 44.0 | 18.5 | +2.34 | 14.6 |  |  | keep collecting (16/30) |
| money_moving+sharp_gap | both | 16-24 | 40.0 | 43.6 | -3.6 | -10.72 | -26.8 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 3-1 | 75.0 | 78.6 | -3.6 | +0.54 | 13.4 |  |  | keep collecting (4/30) |
| money_level+money_moving | both | 16-8 | 66.7 | 55.4 | 11.3 | +4.65 | 19.4 |  |  | keep collecting (24/30) |
| consensus_gap+pin_rlm | both | 0-4 | 0.0 | 17.9 | -17.9 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| money_level+pin_rlm | both | 0-3 | 0.0 | 39.3 | -39.3 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | both | 3-8 | 27.3 | 35.4 | -8.1 | -5.31 | -48.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 3-8 | 27.3 | 35.4 | -8.1 | -5.31 | -48.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+money_moving | both | 9-9 | 50.0 | 59.7 | -9.7 | -3.22 | -17.9 |  |  | keep collecting (18/30) |
| follow_move+pin_rlm | both | 3-3 | 50.0 | 50.0 | 0.0 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| money_moving+rlm | both | 3-7 | 30.0 | 46.4 | -16.4 | -4.31 | -43.1 |  |  | keep collecting (10/30) |
| money_moving+rlm_ratio | both | 3-3 | 50.0 | 50.0 | 0.0 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| pin_rlm+pin_value | both | 1-3 | 25.0 | 33.9 | -8.9 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| pin_rlm+rlm | both | 3-3 | 50.0 | 50.0 | 0.0 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| pin_rlm+rlm_ratio | both | 3-3 | 50.0 | 50.0 | 0.0 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| pin_value+rlm_ratio | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| money_level+rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+rlm | both | 0-1 | 0.0 | 67.9 | -67.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| book_lag+money_level | both | 1-0 | 100.0 | 67.9 | 32.1 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 0-5 | 0.0 | 17.9 | -17.9 | -5.0 | -100.0 |  |  | keep collecting (5/30) |
| pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| follow_move | moneyline | 23-5 | 82.1 | 82.1 | -0.0 | +4.45 | 15.9 |  |  | keep collecting (28/30) |
| follow_move | spread | 9-14 | 39.1 | 55.4 | -16.3 | -5.79 | -25.2 |  |  | keep collecting (23/30) |
| follow_move | total | 5-4 | 55.6 | 50.0 | 5.6 | +0.47 | 5.2 |  |  | keep collecting (9/30) |
| follow_move | tt_away | 6-4 | 60.0 | 52.1 | 7.9 | +1.33 | 13.3 |  |  | keep collecting (10/30) |
| follow_move | tt_home | 5-5 | 50.0 | 51.1 | -1.1 | -0.66 | -6.6 |  |  | keep collecting (10/30) |
| rlm | moneyline | 0-1 | 0.0 | 82.1 | -82.1 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm | spread | 1-8 | 11.1 | 48.0 | -36.9 | -7.13 | -79.2 |  |  | keep collecting (9/30) |
| rlm | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| rlm_ratio | moneyline | 0-1 | 0.0 | 82.1 | -82.1 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_ratio | spread | 0-4 | 0.0 | 50.0 | -50.0 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| rlm_ratio | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| money_level | moneyline | 24-4 | 85.7 | 75.3 | 10.5 | +7.6 | 27.1 |  |  | keep collecting (28/30) |
| money_level | spread | 16-12 | 57.1 | 56.4 | 0.8 | +2.55 | 9.1 |  |  | keep collecting (28/30) |
| money_level | total | 14-14 | 50.0 | 50.0 | 0.0 | -1.34 | -4.8 |  |  | keep collecting (28/30) |
| sharp_gap | moneyline | 14-12 | 53.8 | 54.9 | -1.1 | -2.45 | -9.4 |  |  | keep collecting (26/30) |
| sharp_gap | spread | 9-18 | 33.3 | 42.7 | -9.4 | -10.0 | -37.0 |  |  | keep collecting (27/30) |
| sharp_gap | total | 13-15 | 46.4 | 50.0 | -3.6 | -3.31 | -11.8 |  |  | keep collecting (28/30) |
| money_moving | moneyline | 7-12 | 36.8 | 38.2 | -1.3 | -7.4 | -38.9 |  |  | keep collecting (19/30) |
| money_moving | spread | 7-10 | 41.2 | 40.5 | 0.6 | -3.87 | -22.7 |  |  | keep collecting (17/30) |
| money_moving | total | 10-9 | 52.6 | 50.0 | 2.6 | -0.04 | -0.2 |  |  | keep collecting (19/30) |
| pin_value | moneyline | 2-5 | 28.6 | 27.0 | 1.5 | -3.59 | -51.3 |  |  | keep collecting (7/30) |
| pin_value | spread | 10-1 | 90.9 | 54.9 | 36.0 | +7.72 | 70.2 |  |  | keep collecting (11/30) |
| pin_value | total | 7-5 | 58.3 | 50.0 | 8.3 | +1.02 | 8.5 |  |  | keep collecting (12/30) |
| pin_value | tt_away | 8-9 | 47.1 | 49.1 | -2.0 | -2.07 | -12.2 |  |  | keep collecting (17/30) |
| pin_value | tt_home | 10-9 | 52.6 | 51.4 | 1.2 | -0.63 | -3.3 |  |  | keep collecting (19/30) |
| book_lag | spread | 4-0 | 100.0 | 58.9 | 41.1 | +3.29 | 82.4 |  |  | keep collecting (4/30) |
| consensus_gap | moneyline | 8-20 | 28.6 | 24.7 | 3.8 | -10.52 | -37.6 |  |  | keep collecting (28/30) |
| consensus_gap | spread | 4-3 | 57.1 | 52.6 | 4.6 | +0.29 | 4.2 |  |  | keep collecting (7/30) |
| consensus_gap+money_level | moneyline | 5-1 | 83.3 | 50.0 | 33.3 | +3.1 | 51.6 |  |  | keep collecting (6/30) |
| follow_move+rlm | moneyline | 0-1 | 0.0 | 82.1 | -82.1 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 0-1 | 0.0 | 82.1 | -82.1 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 12-3 | 80.0 | 82.1 | -2.1 | +2.19 | 14.6 |  |  | keep collecting (15/30) |
| rlm+rlm_ratio | moneyline | 0-1 | 0.0 | 82.1 | -82.1 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+sharp_gap | moneyline | 0-1 | 0.0 | 82.1 | -82.1 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 0-1 | 0.0 | 82.1 | -82.1 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+sharp_gap | moneyline | 4-8 | 33.3 | 28.6 | 4.8 | -2.74 | -22.9 |  |  | keep collecting (12/30) |
| follow_move+money_level | moneyline | 22-3 | 88.0 | 82.1 | 5.9 | +6.04 | 24.2 |  |  | keep collecting (25/30) |
| money_level+sharp_gap | moneyline | 13-3 | 81.2 | 74.1 | 7.1 | +3.65 | 22.8 |  |  | keep collecting (16/30) |
| consensus_gap+pin_value | moneyline | 1-5 | 16.7 | 17.9 | -1.2 | -4.04 | -67.3 |  |  | keep collecting (6/30) |
| pin_value+sharp_gap | moneyline | 1-3 | 25.0 | 33.9 | -8.9 | -2.56 | -63.9 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | moneyline | 3-0 | 100.0 | 82.1 | 17.9 | +1.54 | 51.2 |  |  | keep collecting (3/30) |
| consensus_gap+money_moving | moneyline | 2-8 | 20.0 | 17.9 | 2.1 | -5.58 | -55.8 |  |  | keep collecting (10/30) |
| money_moving+pin_value | moneyline | 2-3 | 40.0 | 30.7 | 9.3 | -1.59 | -31.9 |  |  | keep collecting (5/30) |
| consensus_gap+pin_rlm | moneyline | 0-4 | 0.0 | 17.9 | -17.9 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| money_level+money_moving | moneyline | 6-2 | 75.0 | 66.1 | 8.9 | +1.64 | 20.5 |  |  | keep collecting (8/30) |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 17.9 | -17.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 0-5 | 0.0 | 17.9 | -17.9 | -5.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | moneyline | 5-8 | 38.5 | 42.6 | -4.1 | -4.56 | -35.1 |  |  | keep collecting (13/30) |
| pin_rlm+sharp_gap | moneyline | 0-5 | 0.0 | 17.9 | -17.9 | -5.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+money_moving | moneyline | 5-1 | 83.3 | 82.1 | 1.2 | +1.18 | 19.7 |  |  | keep collecting (6/30) |
| pin_rlm+pin_value | moneyline | 0-2 | 0.0 | 17.9 | -17.9 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| follow_move+pin_value | moneyline | 1-0 | 100.0 | 82.1 | 17.9 | +0.44 | 44.4 |  |  | keep collecting (1/30) |
| money_level+pin_value | moneyline | 1-0 | 100.0 | 82.1 | 17.9 | +0.44 | 44.4 |  |  | keep collecting (1/30) |
| follow_move+rlm | spread | 1-8 | 11.1 | 48.0 | -36.9 | -7.13 | -79.2 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-4 | 0.0 | 50.0 | -50.0 | -4.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 4-9 | 30.8 | 48.6 | -17.9 | -5.39 | -41.4 |  |  | keep collecting (13/30) |
| money_level+pin_value | spread | 5-1 | 83.3 | 61.9 | 21.4 | +3.57 | 59.5 |  |  | keep collecting (6/30) |
| rlm+rlm_ratio | spread | 0-4 | 0.0 | 50.0 | -50.0 | -4.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 0-7 | 0.0 | 42.3 | -42.3 | -7.0 | -100.0 |  |  | keep collecting (7/30) |
| rlm_ratio+sharp_gap | spread | 0-4 | 0.0 | 50.0 | -50.0 | -4.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 6-6 | 50.0 | 61.9 | -11.9 | -0.47 | -3.9 |  |  | keep collecting (12/30) |
| follow_move+pin_value | spread | 5-1 | 83.3 | 61.9 | 21.4 | +3.41 | 56.9 |  |  | keep collecting (6/30) |
| pin_value+rlm | spread | 1-0 | 100.0 | 67.9 | 32.1 | +0.87 | 87.0 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | spread | 5-7 | 41.7 | 50.0 | -8.3 | -2.5 | -20.8 |  |  | keep collecting (12/30) |
| consensus_gap+sharp_gap | spread | 0-1 | 0.0 | 32.1 | -32.1 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| book_lag+consensus_gap | spread | 3-0 | 100.0 | 56.0 | 44.0 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| pin_value+sharp_gap | spread | 4-1 | 80.0 | 53.6 | 26.4 | +2.47 | 49.4 |  |  | keep collecting (5/30) |
| book_lag+money_moving | spread | 1-0 | 100.0 | 32.1 | 67.9 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | spread | 1-0 | 100.0 | 32.1 | 67.9 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| consensus_gap+pin_value | spread | 1-0 | 100.0 | 32.1 | 67.9 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| money_moving+pin_value | spread | 4-0 | 100.0 | 50.0 | 50.0 | +3.43 | 85.8 |  |  | keep collecting (4/30) |
| money_level+money_moving | spread | 5-3 | 62.5 | 50.0 | 12.5 | +1.52 | 19.0 |  |  | keep collecting (8/30) |
| money_moving+sharp_gap | spread | 4-9 | 30.8 | 37.6 | -6.9 | -5.42 | -41.7 |  |  | keep collecting (13/30) |
| follow_move+money_moving | spread | 1-4 | 20.0 | 46.4 | -26.4 | -3.09 | -61.8 |  |  | keep collecting (5/30) |
| money_moving+rlm | spread | 0-4 | 0.0 | 41.1 | -41.1 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| follow_move+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_moving+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm+rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+follow_move | spread | 0-1 | 0.0 | 67.9 | -67.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+rlm | spread | 0-1 | 0.0 | 67.9 | -67.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| book_lag+money_level | spread | 1-0 | 100.0 | 67.9 | 32.1 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| consensus_gap+money_level | spread | 1-0 | 100.0 | 67.9 | 32.1 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | total | 8-9 | 47.1 | 50.0 | -2.9 | -1.84 | -10.8 |  |  | keep collecting (17/30) |
| pin_value+sharp_gap | total | 5-3 | 62.5 | 50.0 | 12.5 | +1.31 | 16.4 |  |  | keep collecting (8/30) |
| money_level+pin_value | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.4 | -6.7 |  |  | keep collecting (6/30) |
| money_moving+sharp_gap | total | 7-7 | 50.0 | 50.0 | 0.0 | -0.73 | -5.2 |  |  | keep collecting (14/30) |
| money_level+money_moving | total | 5-3 | 62.5 | 50.0 | 12.5 | +1.49 | 18.6 |  |  | keep collecting (8/30) |
| money_moving+pin_value | total | 4-3 | 57.1 | 50.0 | 7.1 | +0.5 | 7.2 |  |  | keep collecting (7/30) |
| follow_move+money_moving | total | 3-4 | 42.9 | 50.0 | -7.1 | -1.31 | -18.7 |  |  | keep collecting (7/30) |
| follow_move+pin_rlm | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+pin_value | total | 1-2 | 33.3 | 50.0 | -16.7 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| follow_move+rlm | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.31 | -5.2 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| money_moving+pin_rlm | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.31 | -5.2 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| money_moving+rlm_ratio | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+pin_value | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| pin_rlm+rlm | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm | total | 1-2 | 33.3 | 50.0 | -16.7 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| pin_value+rlm_ratio | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| rlm+rlm_ratio | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | total | 3-2 | 60.0 | 50.0 | 10.0 | +0.69 | 13.8 |  |  | keep collecting (5/30) |
| rlm_ratio+sharp_gap | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | total | 2-1 | 66.7 | 50.0 | 16.7 | +0.78 | 26.0 |  |  | keep collecting (3/30) |
| follow_move+pin_value | tt_home | 1-0 | 100.0 | 55.4 | 44.6 | +0.89 | 88.5 |  |  | keep collecting (1/30) |

## By ticket volume and Pinnacle limit (both markets)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_rlm | close | 40k+ bets | 3-8 | 27.3 | -8.1 | -48.3 |  |
| pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 16.4 | 13.8 |  |
| pin_rlm | close | pin $50k+ | 0-6 | 0.0 | -28.6 | -100.0 |  |
| follow_move | close | 40k+ bets | 48-32 | 60.0 | -3.2 | -0.3 |  |
| follow_move | close | pin $10-50k | 10-4 | 71.4 | 9.9 | 13.0 |  |
| follow_move | close | pin $50k+ | 27-19 | 58.7 | -10.1 | -5.9 |  |
| follow_move | close | pin limit <$10k | 11-9 | 55.0 | 3.4 | 3.3 |  |
| rlm | close | 40k+ bets | 4-12 | 25.0 | -25.9 | -52.8 |  |
| rlm | close | pin $10-50k | 3-3 | 50.0 | 0.0 | -5.2 |  |
| rlm | close | pin $50k+ | 1-9 | 10.0 | -41.4 | -81.3 |  |
| rlm_ratio | close | 40k+ bets | 3-6 | 33.3 | -20.2 | -36.8 |  |
| rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 25.0 | 42.2 |  |
| rlm_ratio | close | pin $50k+ | 0-5 | 0.0 | -56.4 | -100.0 |  |
| money_level | close | 40k+ bets | 54-30 | 64.3 | 3.7 | 10.5 |  |
| money_level | close | pin $10-50k | 18-14 | 56.2 | 1.2 | -2.8 |  |
| money_level | close | pin $50k+ | 36-16 | 69.2 | 5.3 | 18.7 |  |
| sharp_gap | close | 40k+ bets | 36-45 | 44.4 | -4.7 | -19.5 |  |
| sharp_gap | close | pin $10-50k | 15-16 | 48.4 | -3.7 | -13.8 |  |
| sharp_gap | close | pin $50k+ | 21-29 | 42.0 | -5.4 | -23.0 |  |
| money_moving | close | 40k+ bets | 24-31 | 43.6 | 0.6 | -20.6 |  |
| money_moving | close | pin $10-50k | 11-11 | 50.0 | 0.0 | -9.9 |  |
| money_moving | close | pin $50k+ | 13-20 | 39.4 | 1.1 | -27.6 |  |
| pin_value | close | 40k+ bets | 37-29 | 56.1 | 7.5 | 3.7 |  |
| pin_value | close | pin $10-50k | 7-7 | 50.0 | 4.6 | -7.0 |  |
| pin_value | close | pin $50k+ | 12-4 | 75.0 | 27.7 | 38.3 |  |
| pin_value | close | pin limit <$10k | 18-18 | 50.0 | -0.3 | -7.5 |  |
| book_lag | close | 40k+ bets | 4-0 | 100.0 | 41.1 | 82.4 |  |
| book_lag | close | pin $50k+ | 4-0 | 100.0 | 41.1 | 82.4 |  |
| consensus_gap | close | 40k+ bets | 12-23 | 34.3 | 4.0 | -29.2 |  |
| consensus_gap | close | pin $10-50k | 1-4 | 20.0 | -10.7 | -74.3 |  |
| consensus_gap | close | pin $50k+ | 11-19 | 36.7 | 6.4 | -21.7 |  |
| follow_move+rlm | close | 40k+ bets | 4-12 | 25.0 | -25.9 | -52.8 |  |
| follow_move+rlm_ratio | close | 40k+ bets | 3-6 | 33.3 | -20.2 | -36.8 |  |
| follow_move+sharp_gap | close | 40k+ bets | 19-15 | 55.9 | -7.8 | -10.3 |  |
| money_level+pin_value | close | 40k+ bets | 9-4 | 69.2 | 11.3 | 27.8 |  |
| rlm+rlm_ratio | close | 40k+ bets | 3-6 | 33.3 | -20.2 | -36.8 |  |
| rlm+sharp_gap | close | 40k+ bets | 3-10 | 23.1 | -25.3 | -56.2 |  |
| rlm_ratio+sharp_gap | close | 40k+ bets | 3-6 | 33.3 | -20.2 | -36.8 |  |
| money_level+sharp_gap | close | 40k+ bets | 26-19 | 57.8 | -0.8 | -1.5 |  |
| consensus_gap+money_level | close | 40k+ bets | 6-1 | 85.7 | 33.2 | 56.1 |  |
| follow_move+money_level | close | 40k+ bets | 30-10 | 75.0 | 1.3 | 15.9 |  |
| consensus_gap+sharp_gap | close | 40k+ bets | 4-9 | 30.8 | 1.9 | -28.8 |  |
| follow_move+pin_value | close | 40k+ bets | 8-3 | 72.7 | 12.8 | 32.8 |  |
| pin_value+rlm | close | 40k+ bets | 2-2 | 50.0 | -4.5 | -6.5 |  |
| pin_value+sharp_gap | close | 40k+ bets | 10-7 | 58.8 | 11.6 | 7.2 |  |
| consensus_gap+pin_value | close | 40k+ bets | 2-5 | 28.6 | 8.7 | -46.5 |  |
| book_lag+consensus_gap | close | 40k+ bets | 3-0 | 100.0 | 44.0 | 82.0 |  |
| book_lag+money_moving | close | 40k+ bets | 1-0 | 100.0 | 67.9 | 78.1 |  |
| book_lag+pin_value | close | 40k+ bets | 2-0 | 100.0 | 50.0 | 80.7 |  |
| consensus_gap+money_moving | close | 40k+ bets | 3-8 | 27.3 | 8.1 | -43.6 |  |
| money_moving+pin_value | close | 40k+ bets | 10-6 | 62.5 | 18.5 | 14.6 |  |
| money_moving+sharp_gap | close | 40k+ bets | 16-24 | 40.0 | -3.6 | -26.8 |  |
| consensus_gap+follow_move | close | 40k+ bets | 3-1 | 75.0 | -3.6 | 13.4 |  |
| money_level+money_moving | close | 40k+ bets | 16-8 | 66.7 | 11.3 | 19.4 |  |
| consensus_gap+pin_rlm | close | 40k+ bets | 0-4 | 0.0 | -17.9 | -100.0 |  |
| money_level+pin_rlm | close | 40k+ bets | 0-3 | 0.0 | -39.3 | -100.0 |  |
| money_moving+pin_rlm | close | 40k+ bets | 3-8 | 27.3 | -8.1 | -48.3 |  |
| pin_rlm+sharp_gap | close | 40k+ bets | 3-8 | 27.3 | -8.1 | -48.3 |  |
| follow_move+money_moving | close | 40k+ bets | 9-9 | 50.0 | -9.7 | -17.9 |  |
| follow_move+pin_rlm | close | 40k+ bets | 3-3 | 50.0 | 0.0 | -5.2 |  |
| money_moving+rlm | close | 40k+ bets | 3-7 | 30.0 | -16.4 | -43.1 |  |
| money_moving+rlm_ratio | close | 40k+ bets | 3-3 | 50.0 | 0.0 | -5.2 |  |
| pin_rlm+pin_value | close | 40k+ bets | 1-3 | 25.0 | -8.9 | -53.2 |  |
| pin_rlm+rlm | close | 40k+ bets | 3-3 | 50.0 | 0.0 | -5.2 |  |
| pin_rlm+rlm_ratio | close | 40k+ bets | 3-3 | 50.0 | 0.0 | -5.2 |  |
| pin_value+rlm_ratio | close | 40k+ bets | 1-1 | 50.0 | 0.0 | -6.5 |  |
| money_level+rlm | close | 40k+ bets | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_level+rlm_ratio | close | 40k+ bets | 0-2 | 0.0 | -50.0 | -100.0 |  |
| consensus_gap+rlm | close | 40k+ bets | 0-1 | 0.0 | -67.9 | -100.0 |  |
| book_lag+money_level | close | 40k+ bets | 1-0 | 100.0 | 32.1 | 83.3 |  |
| money_level+sharp_gap | close | pin $10-50k | 10-9 | 52.6 | -2.4 | -9.5 |  |
| pin_value+sharp_gap | close | pin $10-50k | 5-4 | 55.6 | 9.1 | 3.5 |  |
| money_level+pin_value | close | pin $10-50k | 3-3 | 50.0 | 0.0 | -6.7 |  |
| consensus_gap+pin_value | close | pin $10-50k | 0-2 | 0.0 | -17.9 | -100.0 |  |
| follow_move+money_level | close | pin $10-50k | 7-1 | 87.5 | 17.4 | 26.7 |  |
| follow_move+sharp_gap | close | pin $10-50k | 6-3 | 66.7 | 6.0 | 7.0 |  |
| money_moving+sharp_gap | close | pin $10-50k | 7-8 | 46.7 | -3.3 | -13.9 |  |
| consensus_gap+follow_move | close | pin $10-50k | 1-0 | 100.0 | 17.9 | 28.6 |  |
| consensus_gap+money_level | close | pin $10-50k | 1-0 | 100.0 | 17.9 | 28.6 |  |
| consensus_gap+sharp_gap | close | pin $10-50k | 1-1 | 50.0 | 0.0 | -35.7 |  |
| money_level+money_moving | close | pin $10-50k | 6-3 | 66.7 | 9.5 | 15.0 |  |
| money_moving+pin_value | close | pin $10-50k | 4-4 | 50.0 | 4.0 | -6.2 |  |
| follow_move+money_moving | close | pin $10-50k | 5-4 | 55.6 | -1.6 | -6.1 |  |
| follow_move+pin_rlm | close | pin $10-50k | 3-1 | 75.0 | 25.0 | 42.2 |  |
| follow_move+pin_value | close | pin $10-50k | 1-2 | 33.3 | -16.7 | -37.7 |  |
| follow_move+rlm | close | pin $10-50k | 3-3 | 50.0 | 0.0 | -5.2 |  |
| follow_move+rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 25.0 | 42.2 |  |
| money_moving+pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 16.4 | 13.8 |  |
| money_moving+rlm | close | pin $10-50k | 3-3 | 50.0 | 0.0 | -5.2 |  |
| money_moving+rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 25.0 | 42.2 |  |
| pin_rlm+pin_value | close | pin $10-50k | 1-2 | 33.3 | -6.0 | -37.7 |  |
| pin_rlm+rlm | close | pin $10-50k | 3-1 | 75.0 | 25.0 | 42.2 |  |
| pin_rlm+rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 25.0 | 42.2 |  |
| pin_rlm+sharp_gap | close | pin $10-50k | 3-2 | 60.0 | 16.4 | 13.8 |  |
| pin_value+rlm | close | pin $10-50k | 1-2 | 33.3 | -16.7 | -37.7 |  |
| pin_value+rlm_ratio | close | pin $10-50k | 1-1 | 50.0 | 0.0 | -6.5 |  |
| rlm+rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 25.0 | 42.2 |  |
| rlm+sharp_gap | close | pin $10-50k | 3-2 | 60.0 | 10.0 | 13.8 |  |
| rlm_ratio+sharp_gap | close | pin $10-50k | 3-1 | 75.0 | 25.0 | 42.2 |  |
| consensus_gap+money_moving | close | pin $10-50k | 0-1 | 0.0 | -17.9 | -100.0 |  |
| consensus_gap+pin_rlm | close | pin $10-50k | 0-1 | 0.0 | -17.9 | -100.0 |  |
| follow_move+rlm | close | pin $50k+ | 1-9 | 10.0 | -41.4 | -81.3 |  |
| follow_move+rlm_ratio | close | pin $50k+ | 0-5 | 0.0 | -56.4 | -100.0 |  |
| follow_move+sharp_gap | close | pin $50k+ | 13-12 | 52.0 | -12.7 | -16.5 |  |
| money_level+pin_value | close | pin $50k+ | 6-1 | 85.7 | 20.9 | 57.4 |  |
| rlm+rlm_ratio | close | pin $50k+ | 0-5 | 0.0 | -56.4 | -100.0 |  |
| rlm+sharp_gap | close | pin $50k+ | 0-8 | 0.0 | -47.3 | -100.0 |  |
| rlm_ratio+sharp_gap | close | pin $50k+ | 0-5 | 0.0 | -56.4 | -100.0 |  |
| consensus_gap+money_level | close | pin $50k+ | 5-1 | 83.3 | 35.7 | 60.7 |  |
| follow_move+money_level | close | pin $50k+ | 23-9 | 71.9 | -2.7 | 13.2 |  |
| consensus_gap+sharp_gap | close | pin $50k+ | 3-8 | 27.3 | 2.3 | -27.5 |  |
| follow_move+pin_value | close | pin $50k+ | 6-1 | 85.7 | 20.9 | 55.1 |  |
| pin_value+rlm | close | pin $50k+ | 1-0 | 100.0 | 32.1 | 87.0 |  |
| money_level+sharp_gap | close | pin $50k+ | 16-10 | 61.5 | 0.4 | 4.3 |  |
| consensus_gap+pin_value | close | pin $50k+ | 2-3 | 40.0 | 19.3 | -25.1 |  |
| pin_value+sharp_gap | close | pin $50k+ | 5-3 | 62.5 | 14.3 | 11.4 |  |
| book_lag+consensus_gap | close | pin $50k+ | 3-0 | 100.0 | 44.0 | 82.0 |  |
| book_lag+money_moving | close | pin $50k+ | 1-0 | 100.0 | 67.9 | 78.1 |  |
| book_lag+pin_value | close | pin $50k+ | 2-0 | 100.0 | 50.0 | 80.7 |  |
| consensus_gap+money_moving | close | pin $50k+ | 3-7 | 30.0 | 10.7 | -38.0 |  |
| money_moving+pin_value | close | pin $50k+ | 6-2 | 75.0 | 33.0 | 35.5 |  |
| consensus_gap+pin_rlm | close | pin $50k+ | 0-3 | 0.0 | -17.9 | -100.0 |  |
| money_level+money_moving | close | pin $50k+ | 10-5 | 66.7 | 12.4 | 22.0 |  |
| money_level+pin_rlm | close | pin $50k+ | 0-3 | 0.0 | -39.3 | -100.0 |  |
| money_moving+pin_rlm | close | pin $50k+ | 0-6 | 0.0 | -28.6 | -100.0 |  |
| money_moving+sharp_gap | close | pin $50k+ | 9-16 | 36.0 | -3.7 | -34.6 |  |
| pin_rlm+sharp_gap | close | pin $50k+ | 0-6 | 0.0 | -28.6 | -100.0 |  |
| follow_move+money_moving | close | pin $50k+ | 4-5 | 44.4 | -17.9 | -29.7 |  |
| pin_rlm+pin_value | close | pin $50k+ | 0-1 | 0.0 | -17.9 | -100.0 |  |
| consensus_gap+follow_move | close | pin $50k+ | 2-1 | 66.7 | -10.7 | 8.4 |  |
| money_moving+rlm | close | pin $50k+ | 0-4 | 0.0 | -41.1 | -100.0 |  |
| follow_move+pin_rlm | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_level+rlm | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_level+rlm_ratio | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_moving+rlm_ratio | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| pin_rlm+rlm | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| pin_rlm+rlm_ratio | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| consensus_gap+rlm | close | pin $50k+ | 0-1 | 0.0 | -67.9 | -100.0 |  |
| book_lag+money_level | close | pin $50k+ | 1-0 | 100.0 | 32.1 | 83.3 |  |
| follow_move+pin_value | close | pin limit <$10k | 1-0 | 100.0 | 44.6 | 88.5 |  |
| pin_rlm | early | <10k bets | 0-2 | 0.0 | -17.9 | -100.0 | -4.4 |
| pin_rlm | early | pin limit <$10k | 0-2 | 0.0 | -17.9 | -100.0 | -4.4 |
| follow_move | early | 10-40k bets | 2-1 | 66.7 | -10.7 | 6.3 | -0.4 |
| follow_move | early | 40k+ bets | 3-2 | 60.0 | -2.1 | -10.9 | -0.1 |
| follow_move | early | <10k bets | 19-6 | 76.0 | 4.6 | 17.1 | -0.15 |
| follow_move | early | pin $10-50k | 6-4 | 60.0 | 0.0 | 8.7 | 0.33 |
| follow_move | early | pin $50k+ | 4-2 | 66.7 | 3.6 | 6.1 | -0.33 |
| follow_move | early | pin limit <$10k | 14-3 | 82.4 | 2.9 | 15.8 | -0.4 |
| rlm | early | 40k+ bets | 0-1 | 0.0 | -32.1 | -100.0 | 0.0 |
| rlm | early | <10k bets | 0-1 | 0.0 | -32.1 | -100.0 | 1.0 |
| rlm | early | pin $10-50k | 0-1 | 0.0 | -32.1 | -100.0 | 1.0 |
| rlm | early | pin $50k+ | 0-1 | 0.0 | -32.1 | -100.0 | 0.0 |
| rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -32.1 | -100.0 | 0.0 |
| rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -32.1 | -100.0 | 0.0 |
| money_level | early | 10-40k bets | 3-3 | 50.0 | -10.7 | -13.8 | -0.28 |
| money_level | early | 40k+ bets | 4-4 | 50.0 | -16.5 | -19.9 | -0.06 |
| money_level | early | <10k bets | 30-14 | 68.2 | 8.2 | 15.2 | -1.02 |
| money_level | early | pin $10-50k | 11-9 | 55.0 | 0.0 | 2.8 | -0.18 |
| money_level | early | pin $50k+ | 5-2 | 71.4 | 2.6 | 20.1 | -0.36 |
| money_level | early | pin limit <$10k | 21-10 | 67.7 | 4.7 | 7.4 | -1.32 |
| sharp_gap | early | 10-40k bets | 3-3 | 50.0 | 4.8 | 3.1 | 0.27 |
| sharp_gap | early | 40k+ bets | 4-5 | 44.4 | -14.3 | -29.5 | -0.06 |
| sharp_gap | early | <10k bets | 23-21 | 52.3 | 1.6 | -6.3 | -0.16 |
| sharp_gap | early | pin $10-50k | 10-10 | 50.0 | -5.4 | -4.6 | -0.03 |
| sharp_gap | early | pin $50k+ | 3-5 | 37.5 | -18.8 | -37.5 | 0.33 |
| sharp_gap | early | pin limit <$10k | 17-14 | 54.8 | 7.4 | -4.3 | -0.26 |
| money_moving | early | <10k bets | 10-6 | 62.5 | 5.1 | 10.1 | -0.23 |
| money_moving | early | pin $10-50k | 4-2 | 66.7 | 10.7 | 28.6 | -0.5 |
| money_moving | early | pin limit <$10k | 6-4 | 60.0 | 1.8 | -1.1 | -0.06 |
| pin_value | early | 10-40k bets | 1-2 | 33.3 | -22.6 | -39.3 | 0.0 |
| pin_value | early | 40k+ bets | 4-2 | 66.7 | 23.5 | 22.5 | 0.0 |
| pin_value | early | <10k bets | 15-12 | 55.6 | 7.8 | 4.5 | 0.44 |
| pin_value | early | pin $10-50k | 6-2 | 75.0 | 13.8 | 43.8 | -0.31 |
| pin_value | early | pin $50k+ | 3-0 | 100.0 | 56.0 | 81.1 | 0.0 |
| pin_value | early | pin limit <$10k | 11-14 | 44.0 | 0.2 | -18.2 | 0.58 |
| book_lag | early | <10k bets | 0-2 | 0.0 | -50.0 | -100.0 | -0.75 |
| book_lag | early | pin $10-50k | 0-2 | 0.0 | -50.0 | -100.0 | -0.75 |
| consensus_gap | early | 10-40k bets | 2-2 | 50.0 | 7.1 | 7.0 | 0.4 |
| consensus_gap | early | 40k+ bets | 2-2 | 50.0 | 28.6 | -6.4 | 0.17 |
| consensus_gap | early | <10k bets | 6-15 | 28.6 | -2.9 | -48.2 | 0.22 |
| consensus_gap | early | pin $10-50k | 3-4 | 42.9 | 4.6 | -10.9 | 0.03 |
| consensus_gap | early | pin $50k+ | 3-3 | 50.0 | 13.1 | -7.3 | 0.43 |
| consensus_gap | early | pin limit <$10k | 4-12 | 25.0 | -1.8 | -55.6 | 0.26 |
| consensus_gap+follow_move | early | 10-40k bets | 1-0 | 100.0 | 32.1 | 82.0 | 0.0 |
| consensus_gap+money_level | early | 10-40k bets | 1-0 | 100.0 | 32.1 | 82.0 | 0.0 |
| consensus_gap+pin_value | early | 10-40k bets | 1-0 | 100.0 | 32.1 | 82.0 | 0.0 |
| consensus_gap+sharp_gap | early | 10-40k bets | 2-2 | 50.0 | 7.1 | 7.0 | 0.4 |
| follow_move+money_level | early | 10-40k bets | 2-1 | 66.7 | -10.7 | 6.3 | -0.4 |
| follow_move+pin_value | early | 10-40k bets | 1-0 | 100.0 | 32.1 | 82.0 | 0.0 |
| follow_move+sharp_gap | early | 10-40k bets | 1-0 | 100.0 | 32.1 | 82.0 | 0.0 |
| money_level+pin_value | early | 10-40k bets | 1-0 | 100.0 | 32.1 | 82.0 | 0.0 |
| money_level+sharp_gap | early | 10-40k bets | 1-1 | 50.0 | -8.9 | -9.0 | 0.0 |
| pin_value+sharp_gap | early | 10-40k bets | 1-0 | 100.0 | 32.1 | 82.0 | 0.0 |
| follow_move+rlm | early | 40k+ bets | 0-1 | 0.0 | -32.1 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -32.1 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | 40k+ bets | 3-2 | 60.0 | -2.1 | -10.9 | -0.1 |
| rlm+rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -32.1 | -100.0 | 0.0 |
| rlm+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -32.1 | -100.0 | 0.0 |
| rlm_ratio+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -32.1 | -100.0 | 0.0 |
| money_level+pin_value | early | 40k+ bets | 0-1 | 0.0 | -50.0 | -100.0 | 0.0 |
| money_level+sharp_gap | early | 40k+ bets | 3-4 | 42.9 | -23.5 | -35.5 | -0.07 |
| pin_value+sharp_gap | early | 40k+ bets | 1-1 | 50.0 | 8.9 | -8.4 | 0.0 |
| follow_move+money_level | early | 40k+ bets | 2-1 | 66.7 | -15.5 | -12.6 | -0.17 |
| consensus_gap+pin_value | early | 40k+ bets | 1-0 | 100.0 | 67.9 | 78.1 | 0.0 |
| follow_move+pin_value | early | 40k+ bets | 1-0 | 100.0 | 67.9 | 83.3 | 0.0 |
| follow_move+money_level | early | <10k bets | 17-4 | 81.0 | 8.5 | 22.6 | -0.87 |
| follow_move+money_moving | early | <10k bets | 6-1 | 85.7 | 9.7 | 40.4 | -0.44 |
| follow_move+pin_value | early | <10k bets | 2-0 | 100.0 | 32.1 | 90.6 | 0.0 |
| follow_move+sharp_gap | early | <10k bets | 10-3 | 76.9 | 8.0 | 23.7 | -0.09 |
| money_level+money_moving | early | <10k bets | 8-3 | 72.7 | 7.8 | 25.7 | -0.74 |
| money_level+pin_value | early | <10k bets | 5-1 | 83.3 | 24.4 | 60.7 | -0.58 |
| money_level+sharp_gap | early | <10k bets | 20-11 | 64.5 | 6.5 | 13.6 | -0.75 |
| money_moving+pin_value | early | <10k bets | 4-2 | 66.7 | 16.1 | 28.2 | 1.0 |
| money_moving+sharp_gap | early | <10k bets | 4-3 | 57.1 | -0.5 | 3.6 | -0.09 |
| pin_value+sharp_gap | early | <10k bets | 5-4 | 55.6 | 10.3 | 7.2 | 0.62 |
| consensus_gap+sharp_gap | early | <10k bets | 4-8 | 33.3 | 0.6 | -41.0 | 0.03 |
| consensus_gap+follow_move | early | <10k bets | 2-0 | 100.0 | 17.9 | 46.8 | -0.35 |
| consensus_gap+money_level | early | <10k bets | 3-1 | 75.0 | 12.5 | 20.1 | -2.83 |
| book_lag+consensus_gap | early | <10k bets | 0-1 | 0.0 | -32.1 | -100.0 | 0.5 |
| consensus_gap+pin_value | early | <10k bets | 0-4 | 0.0 | -17.9 | -100.0 | 2.38 |
| consensus_gap+pin_rlm | early | <10k bets | 0-2 | 0.0 | -17.9 | -100.0 | -4.4 |
| money_level+pin_rlm | early | <10k bets | 0-1 | 0.0 | -17.9 | -100.0 | -10.6 |
| pin_rlm+sharp_gap | early | <10k bets | 0-2 | 0.0 | -17.9 | -100.0 | -4.4 |
| follow_move+rlm | early | <10k bets | 0-1 | 0.0 | -32.1 | -100.0 | 1.0 |
| book_lag+money_level | early | <10k bets | 0-1 | 0.0 | -67.9 | -100.0 | -2.0 |
| book_lag+money_moving | early | <10k bets | 0-1 | 0.0 | -67.9 | -100.0 | -2.0 |
| book_lag+sharp_gap | early | <10k bets | 0-1 | 0.0 | -67.9 | -100.0 | -2.0 |
| consensus_gap+money_moving | early | <10k bets | 0-1 | 0.0 | -17.9 | -100.0 | 5.0 |
| pin_rlm+pin_value | early | <10k bets | 0-1 | 0.0 | -17.9 | -100.0 | 1.8 |
| money_level+pin_value | early | pin $10-50k | 3-1 | 75.0 | 11.6 | 45.2 | -0.38 |
| money_level+sharp_gap | early | pin $10-50k | 9-8 | 52.9 | -3.2 | -2.2 | -0.12 |
| pin_value+sharp_gap | early | pin $10-50k | 3-1 | 75.0 | 11.6 | 45.2 | -0.38 |
| follow_move+money_level | early | pin $10-50k | 5-3 | 62.5 | 0.0 | 12.9 | 0.29 |
| follow_move+sharp_gap | early | pin $10-50k | 5-2 | 71.4 | 11.7 | 29.0 | 0.21 |
| consensus_gap+sharp_gap | early | pin $10-50k | 2-0 | 100.0 | 57.1 | 116.5 | -0.5 |
| follow_move+money_moving | early | pin $10-50k | 2-0 | 100.0 | 32.1 | 90.6 | 0.0 |
| follow_move+pin_value | early | pin $10-50k | 2-0 | 100.0 | 32.1 | 90.6 | 0.0 |
| money_level+money_moving | early | pin $10-50k | 2-1 | 66.7 | 10.7 | 31.1 | -1.33 |
| money_moving+pin_value | early | pin $10-50k | 3-1 | 75.0 | 16.1 | 44.1 | 0.25 |
| money_moving+sharp_gap | early | pin $10-50k | 1-1 | 50.0 | -17.9 | -1.0 | -1.0 |
| book_lag+consensus_gap | early | pin $10-50k | 0-1 | 0.0 | -32.1 | -100.0 | 0.5 |
| follow_move+rlm | early | pin $10-50k | 0-1 | 0.0 | -32.1 | -100.0 | 1.0 |
| book_lag+money_level | early | pin $10-50k | 0-1 | 0.0 | -67.9 | -100.0 | -2.0 |
| book_lag+money_moving | early | pin $10-50k | 0-1 | 0.0 | -67.9 | -100.0 | -2.0 |
| book_lag+sharp_gap | early | pin $10-50k | 0-1 | 0.0 | -67.9 | -100.0 | -2.0 |
| consensus_gap+money_level | early | pin $10-50k | 1-0 | 100.0 | 32.1 | 87.0 | 0.0 |
| follow_move+rlm | early | pin $50k+ | 0-1 | 0.0 | -32.1 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -32.1 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | pin $50k+ | 3-2 | 60.0 | 0.7 | -0.0 | 0.0 |
| rlm+rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -32.1 | -100.0 | 0.0 |
| rlm+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -32.1 | -100.0 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -32.1 | -100.0 | 0.0 |
| follow_move+money_level | early | pin $50k+ | 3-1 | 75.0 | -3.6 | 13.4 | -0.5 |
| money_level+sharp_gap | early | pin $50k+ | 2-2 | 50.0 | -25.0 | -20.9 | 0.0 |
| consensus_gap+pin_value | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 80.0 | 0.0 |
| follow_move+pin_value | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 82.7 | 0.0 |
| pin_value+sharp_gap | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 82.7 | 0.0 |
| consensus_gap+follow_move | early | pin $50k+ | 1-0 | 100.0 | 32.1 | 82.0 | 0.0 |
| consensus_gap+money_level | early | pin $50k+ | 1-0 | 100.0 | 32.1 | 82.0 | 0.0 |
| consensus_gap+sharp_gap | early | pin $50k+ | 1-2 | 33.3 | -17.9 | -39.3 | 0.87 |
| money_level+pin_value | early | pin $50k+ | 1-0 | 100.0 | 32.1 | 82.0 | 0.0 |
| money_level+pin_value | early | pin limit <$10k | 2-1 | 66.7 | 16.7 | 27.8 | -0.67 |
| money_level+sharp_gap | early | pin limit <$10k | 13-6 | 68.4 | 9.0 | 14.5 | -1.15 |
| pin_value+sharp_gap | early | pin limit <$10k | 2-4 | 33.3 | -0.6 | -36.1 | 1.18 |
| follow_move+money_level | early | pin limit <$10k | 13-2 | 86.7 | 7.6 | 19.9 | -1.35 |
| follow_move+sharp_gap | early | pin limit <$10k | 6-1 | 85.7 | 5.6 | 18.9 | -0.46 |
| consensus_gap+sharp_gap | early | pin limit <$10k | 3-8 | 27.3 | -2.3 | -52.6 | 0.04 |
| follow_move+money_moving | early | pin limit <$10k | 4-1 | 80.0 | 0.7 | 20.3 | -0.62 |
| money_level+money_moving | early | pin limit <$10k | 6-2 | 75.0 | 6.7 | 23.7 | -0.51 |
| consensus_gap+follow_move | early | pin limit <$10k | 2-0 | 100.0 | 17.9 | 46.8 | -0.35 |
| consensus_gap+money_level | early | pin limit <$10k | 2-1 | 66.7 | 6.0 | -2.2 | -3.77 |
| consensus_gap+pin_value | early | pin limit <$10k | 0-4 | 0.0 | -17.9 | -100.0 | 2.38 |
| money_moving+sharp_gap | early | pin limit <$10k | 3-2 | 60.0 | 6.4 | 5.4 | 0.28 |
| consensus_gap+pin_rlm | early | pin limit <$10k | 0-2 | 0.0 | -17.9 | -100.0 | -4.4 |
| money_level+pin_rlm | early | pin limit <$10k | 0-1 | 0.0 | -17.9 | -100.0 | -10.6 |
| pin_rlm+sharp_gap | early | pin limit <$10k | 0-2 | 0.0 | -17.9 | -100.0 | -4.4 |
| money_moving+pin_value | early | pin limit <$10k | 1-1 | 50.0 | 16.1 | -3.7 | 2.5 |
| consensus_gap+money_moving | early | pin limit <$10k | 0-1 | 0.0 | -17.9 | -100.0 | 5.0 |
| pin_rlm+pin_value | early | pin limit <$10k | 0-1 | 0.0 | -17.9 | -100.0 | 1.8 |
