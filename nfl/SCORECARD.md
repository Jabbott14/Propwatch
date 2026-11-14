# NFL scorecard

Generated 2026-11-14 06:56 UTC. 29 graded games (0 finished games had no final score and are not graded).

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before kickoff. Break-even at -110 is 52.4%. CLV = points of
closing-line value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured on
this sample. `edge` is hit% minus that. A signal that is structurally long dogs or
unders will beat 50% in any week dogs or unders run, which is not an edge --
this sample ran **65.5% favourites** (n=29)
**51.7% overs** (n=29) and **79.3% moneyline favourites** (n=29) and **46.6% team-total overs** (n=58).

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
| pin_rlm | both | 1-2 | 33.3 | 20.7 | 12.6 | -0.92 | -30.7 | -2.3 | 66.7 | keep collecting (3/30) |
| follow_move | both | 24-10 | 70.6 | 69.1 | 1.5 | +2.92 | 8.6 | -0.21 | 29.4 | beats break-even but not its base rate -- directional bias, not signal |
| rlm | both | 0-2 | 0.0 | 34.5 | -34.5 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| rlm_ratio | both | 0-1 | 0.0 | 34.5 | -34.5 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level | both | 39-22 | 63.9 | 59.9 | 4.0 | +5.07 | 8.3 | -0.83 | 14.8 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 33-29 | 53.2 | 50.6 | 2.7 | -2.34 | -3.8 | -0.1 | 29.0 | no edge shown yet |
| money_moving | both | 11-6 | 64.7 | 54.6 | 10.1 | +2.69 | 15.8 | -0.1 | 29.4 | keep collecting (17/30) |
| pin_value | both | 20-17 | 54.1 | 48.2 | 5.8 | +0.4 | 1.1 | 0.32 | 29.7 | no edge shown yet |
| book_lag | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | -0.75 | 50.0 | keep collecting (2/30) |
| consensus_gap | both | 11-20 | 35.5 | 33.9 | 1.6 | -10.01 | -32.3 | 0.29 | 45.2 | DROP: below break-even |
| follow_move+rlm | both | 0-2 | 0.0 | 34.5 | -34.5 | -2.0 | -100.0 | 0.5 | 50.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | both | 0-1 | 0.0 | 34.5 | -34.5 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 14-5 | 73.7 | 65.5 | 8.2 | +3.35 | 17.6 | -0.09 | 21.1 | keep collecting (19/30) |
| rlm+rlm_ratio | both | 0-1 | 0.0 | 34.5 | -34.5 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 0-1 | 0.0 | 34.5 | -34.5 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| rlm_ratio+sharp_gap | both | 0-1 | 0.0 | 34.5 | -34.5 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_value | both | 6-2 | 75.0 | 58.2 | 16.8 | +3.46 | 43.3 | -0.44 | 0.0 | keep collecting (8/30) |
| money_level+sharp_gap | both | 26-16 | 61.9 | 58.1 | 3.8 | +3.36 | 8.0 | -0.61 | 14.3 | no edge shown yet |
| pin_value+sharp_gap | both | 7-5 | 58.3 | 46.8 | 11.5 | +1.3 | 10.8 | 0.47 | 25.0 | keep collecting (12/30) |
| follow_move+money_level | both | 21-7 | 75.0 | 72.2 | 2.8 | +3.56 | 12.7 | -0.77 | 25.0 | keep collecting (28/30) |
| consensus_gap+pin_value | both | 2-5 | 28.6 | 35.5 | -6.9 | -3.4 | -48.6 | 1.36 | 57.1 | keep collecting (7/30) |
| follow_move+pin_value | both | 4-0 | 100.0 | 57.8 | 42.2 | +3.47 | 86.7 | 0.0 | 0.0 | keep collecting (4/30) |
| consensus_gap+follow_move | both | 3-0 | 100.0 | 74.7 | 25.3 | +1.75 | 58.5 | -0.23 | 33.3 | keep collecting (3/30) |
| consensus_gap+money_level | both | 4-1 | 80.0 | 62.1 | 17.9 | +1.62 | 32.5 | -2.26 | 20.0 | keep collecting (5/30) |
| consensus_gap+sharp_gap | both | 7-10 | 41.2 | 35.5 | 5.7 | -3.55 | -20.9 | 0.23 | 52.9 | keep collecting (17/30) |
| follow_move+money_moving | both | 6-1 | 85.7 | 73.4 | 12.3 | +2.83 | 40.4 | -0.44 | 28.6 | keep collecting (7/30) |
| money_level+money_moving | both | 8-3 | 72.7 | 63.6 | 9.1 | +2.83 | 25.7 | -0.74 | 18.2 | keep collecting (11/30) |
| money_moving+pin_value | both | 4-2 | 66.7 | 50.0 | 16.7 | +1.69 | 28.2 | 1.0 | 33.3 | keep collecting (6/30) |
| money_moving+sharp_gap | both | 5-3 | 62.5 | 52.2 | 10.3 | +1.33 | 16.6 | 0.16 | 25.0 | keep collecting (8/30) |
| book_lag+consensus_gap | both | 0-1 | 0.0 | 34.5 | -34.5 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+pin_rlm | both | 1-2 | 33.3 | 20.7 | 12.6 | -0.92 | -30.7 | -2.3 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-1 | 0.0 | 20.7 | -20.7 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | both | 1-2 | 33.3 | 20.7 | 12.6 | -0.92 | -30.7 | -2.3 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+money_level | both | 0-1 | 0.0 | 65.5 | -65.5 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+money_moving | both | 0-1 | 0.0 | 65.5 | -65.5 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+sharp_gap | both | 0-1 | 0.0 | 65.5 | -65.5 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+money_moving | both | 1-1 | 50.0 | 20.7 | 29.3 | +0.08 | 4.0 | 3.45 | 100.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 20.7 | -20.7 | -1.0 | -100.0 | 1.8 | 100.0 | keep collecting (1/30) |
| money_moving+pin_rlm | both | 1-0 | 100.0 | 20.7 | 79.3 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-2 | 33.3 | 20.7 | 12.6 | -0.92 | -30.7 | -2.3 | 66.7 | keep collecting (3/30) |
| follow_move | moneyline | 17-4 | 81.0 | 79.3 | 1.6 | +2.68 | 12.8 | -0.34 | 33.3 | keep collecting (21/30) |
| follow_move | spread | 7-5 | 58.3 | 52.6 | 5.7 | +1.24 | 10.3 | 0.25 | 25.0 | keep collecting (12/30) |
| follow_move | total | 0-1 | 0.0 | 51.7 | -51.7 | -1.0 | -100.0 | -3.0 | 0.0 | keep collecting (1/30) |
| rlm | spread | 0-2 | 0.0 | 34.5 | -34.5 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 34.5 | -34.5 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level | moneyline | 16-4 | 80.0 | 76.4 | 3.6 | +1.98 | 9.9 | -1.56 | 25.0 | keep collecting (20/30) |
| money_level | spread | 13-7 | 65.0 | 53.1 | 11.9 | +4.99 | 24.9 | -0.23 | 10.0 | keep collecting (20/30) |
| money_level | total | 10-11 | 47.6 | 50.7 | -3.1 | -1.9 | -9.0 | -0.71 | 9.5 | keep collecting (21/30) |
| sharp_gap | moneyline | 11-10 | 52.4 | 45.8 | 6.6 | -3.24 | -15.4 | 0.02 | 42.9 | keep collecting (21/30) |
| sharp_gap | spread | 10-11 | 47.6 | 55.2 | -7.6 | -1.98 | -9.4 | 0.07 | 23.8 | keep collecting (21/30) |
| sharp_gap | total | 12-8 | 60.0 | 50.7 | 9.3 | +2.88 | 14.4 | -0.4 | 20.0 | keep collecting (20/30) |
| money_moving | moneyline | 5-2 | 71.4 | 54.2 | 17.2 | +1.1 | 15.6 | 0.33 | 57.1 | keep collecting (7/30) |
| money_moving | spread | 4-3 | 57.1 | 56.7 | 0.5 | +0.72 | 10.2 | -0.43 | 14.3 | keep collecting (7/30) |
| money_moving | total | 2-1 | 66.7 | 50.6 | 16.1 | +0.88 | 29.3 | -0.33 | 0.0 | keep collecting (3/30) |
| pin_value | moneyline | 0-5 | 0.0 | 20.7 | -20.7 | -5.0 | -100.0 | 2.28 | 100.0 | keep collecting (5/30) |
| pin_value | spread | 9-2 | 81.8 | 57.1 | 24.8 | +5.94 | 54.0 | -0.23 | 9.1 | keep collecting (11/30) |
| pin_value | total | 3-5 | 37.5 | 50.0 | -12.5 | -2.26 | -28.2 | -0.25 | 12.5 | keep collecting (8/30) |
| pin_value | tt_away | 3-3 | 50.0 | 50.0 | 0.0 | -0.47 | -7.8 | 0.33 | 33.3 | keep collecting (6/30) |
| pin_value | tt_home | 5-2 | 71.4 | 50.5 | 20.9 | +2.18 | 31.2 | 0.43 | 28.6 | keep collecting (7/30) |
| book_lag | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | -0.75 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 6-15 | 28.6 | 26.3 | 2.3 | -9.28 | -44.2 | 0.38 | 57.1 | keep collecting (21/30) |
| consensus_gap | spread | 5-5 | 50.0 | 50.0 | 0.0 | -0.73 | -7.3 | 0.1 | 20.0 | keep collecting (10/30) |
| follow_move+money_level | moneyline | 16-3 | 84.2 | 79.3 | 4.9 | +2.98 | 15.7 | -1.08 | 26.3 | keep collecting (19/30) |
| follow_move+sharp_gap | moneyline | 8-1 | 88.9 | 79.3 | 9.6 | +1.94 | 21.6 | -0.41 | 22.2 | keep collecting (9/30) |
| money_level+sharp_gap | moneyline | 8-2 | 80.0 | 73.4 | 6.6 | +0.94 | 9.4 | -1.43 | 20.0 | keep collecting (10/30) |
| consensus_gap+sharp_gap | moneyline | 5-9 | 35.7 | 29.1 | 6.7 | -4.25 | -30.3 | 0.24 | 57.1 | keep collecting (14/30) |
| follow_move+money_moving | moneyline | 4-0 | 100.0 | 79.3 | 20.7 | +2.02 | 50.4 | -0.78 | 50.0 | keep collecting (4/30) |
| money_level+money_moving | moneyline | 4-0 | 100.0 | 79.3 | 20.7 | +2.02 | 50.4 | -0.78 | 50.0 | keep collecting (4/30) |
| consensus_gap+follow_move | moneyline | 2-0 | 100.0 | 79.3 | 20.7 | +0.94 | 46.8 | -0.35 | 50.0 | keep collecting (2/30) |
| consensus_gap+money_level | moneyline | 2-1 | 66.7 | 59.8 | 6.9 | -0.06 | -2.2 | -3.77 | 33.3 | keep collecting (3/30) |
| consensus_gap+pin_value | moneyline | 0-4 | 0.0 | 20.7 | -20.7 | -4.0 | -100.0 | 2.38 | 100.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | moneyline | 1-2 | 33.3 | 20.7 | 12.6 | -0.92 | -30.7 | -2.3 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 20.7 | -20.7 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | moneyline | 1-2 | 33.3 | 20.7 | 12.6 | -0.92 | -30.7 | -2.3 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | moneyline | 2-1 | 66.7 | 40.2 | 26.4 | +0.47 | 15.7 | 1.1 | 66.7 | keep collecting (3/30) |
| pin_value+sharp_gap | moneyline | 0-3 | 0.0 | 20.7 | -20.7 | -3.0 | -100.0 | 3.03 | 100.0 | keep collecting (3/30) |
| consensus_gap+money_moving | moneyline | 1-1 | 50.0 | 20.7 | 29.3 | +0.08 | 4.0 | 3.45 | 100.0 | keep collecting (2/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 20.7 | -20.7 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 20.7 | -20.7 | -1.0 | -100.0 | 1.8 | 100.0 | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 1-0 | 100.0 | 20.7 | 79.3 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| follow_move+rlm | spread | 0-2 | 0.0 | 34.5 | -34.5 | -2.0 | -100.0 | 0.5 | 50.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 34.5 | -34.5 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 6-4 | 60.0 | 53.1 | 6.9 | +1.41 | 14.1 | 0.2 | 20.0 | keep collecting (10/30) |
| rlm+rlm_ratio | spread | 0-1 | 0.0 | 34.5 | -34.5 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 0-1 | 0.0 | 34.5 | -34.5 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 34.5 | -34.5 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+pin_value | spread | 2-1 | 66.7 | 55.2 | 11.5 | +0.6 | 20.0 | 0.0 | 0.0 | keep collecting (3/30) |
| money_level+sharp_gap | spread | 9-7 | 56.2 | 55.8 | 0.4 | +1.18 | 7.4 | -0.09 | 12.5 | keep collecting (16/30) |
| follow_move+pin_value | spread | 4-0 | 100.0 | 57.8 | 42.2 | +3.47 | 86.7 | 0.0 | 0.0 | keep collecting (4/30) |
| pin_value+sharp_gap | spread | 5-0 | 100.0 | 59.3 | 40.7 | +4.46 | 89.2 | -0.3 | 0.0 | keep collecting (5/30) |
| consensus_gap+follow_move | spread | 1-0 | 100.0 | 65.5 | 34.5 | +0.82 | 82.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 2-0 | 100.0 | 65.5 | 34.5 | +1.69 | 84.5 | 0.0 | 0.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | spread | 2-1 | 66.7 | 65.5 | 1.1 | +0.69 | 23.0 | 0.17 | 33.3 | keep collecting (3/30) |
| follow_move+money_level | spread | 5-3 | 62.5 | 57.8 | 4.7 | +1.57 | 19.7 | 0.25 | 25.0 | keep collecting (8/30) |
| money_level+pin_value | spread | 4-0 | 100.0 | 65.5 | 34.5 | +3.63 | 90.7 | -0.38 | 0.0 | keep collecting (4/30) |
| follow_move+money_moving | spread | 2-1 | 66.7 | 65.5 | 1.1 | +0.81 | 27.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_level+money_moving | spread | 2-2 | 50.0 | 57.8 | -7.8 | -0.07 | -1.7 | -1.0 | 0.0 | keep collecting (4/30) |
| money_moving+pin_value | spread | 3-1 | 75.0 | 57.8 | 17.2 | +1.76 | 44.1 | 0.25 | 25.0 | keep collecting (4/30) |
| money_moving+sharp_gap | spread | 1-2 | 33.3 | 65.5 | -32.2 | -1.02 | -34.0 | -0.67 | 0.0 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 34.5 | -34.5 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| book_lag+money_level | spread | 0-1 | 0.0 | 65.5 | -65.5 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+money_moving | spread | 0-1 | 0.0 | 65.5 | -65.5 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+sharp_gap | spread | 0-1 | 0.0 | 65.5 | -65.5 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 2-2 | 50.0 | 50.9 | -0.9 | -0.16 | -4.1 | -0.5 | 0.0 | keep collecting (4/30) |
| money_level+sharp_gap | total | 9-7 | 56.2 | 50.9 | 5.4 | +1.23 | 7.7 | -0.62 | 12.5 | keep collecting (16/30) |
| pin_value+sharp_gap | total | 2-2 | 50.0 | 50.9 | -0.9 | -0.16 | -4.1 | -0.5 | 0.0 | keep collecting (4/30) |
| follow_move+money_level | total | 0-1 | 0.0 | 51.7 | -51.7 | -1.0 | -100.0 | -3.0 | 0.0 | redundant -- identical record to follow_move alone, not independent confirmation |
| money_level+money_moving | total | 2-1 | 66.7 | 50.6 | 16.1 | +0.88 | 29.3 | -0.33 | 0.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| money_moving+sharp_gap | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.88 | 93.9 | 0.0 | 0.0 | keep collecting (2/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 48.3 | 51.7 | +0.93 | 92.6 | 0.0 | 0.0 | keep collecting (1/30) |

## CLOSE

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 4-8 | 33.3 | 34.8 | -1.4 | -4.31 | -35.9 |  |  | keep collecting (12/30) |
| follow_move | both | 48-36 | 57.1 | 61.7 | -4.6 | -4.21 | -5.0 |  |  | no edge shown yet |
| rlm | both | 4-12 | 25.0 | 50.4 | -25.4 | -8.44 | -52.8 |  |  | keep collecting (16/30) |
| rlm_ratio | both | 3-6 | 33.3 | 52.5 | -19.2 | -3.31 | -36.8 |  |  | keep collecting (9/30) |
| money_level | both | 55-30 | 64.7 | 59.7 | 5.0 | +9.68 | 11.4 |  |  | PROMOTE: beats break-even and its own base rate |
| sharp_gap | both | 38-46 | 45.2 | 48.9 | -3.6 | -14.89 | -17.7 |  |  | no edge shown yet |
| money_moving | both | 26-32 | 44.8 | 43.2 | 1.6 | -10.44 | -18.0 |  |  | no edge shown yet |
| pin_value | both | 39-30 | 56.5 | 48.8 | 7.7 | +3.15 | 4.6 |  |  | no edge shown yet |
| book_lag | both | 4-0 | 100.0 | 57.8 | 42.2 | +3.29 | 82.4 |  |  | keep collecting (4/30) |
| consensus_gap | both | 13-23 | 36.1 | 31.7 | 4.4 | -9.23 | -25.6 |  |  | DROP: below break-even |
| follow_move+rlm | both | 4-12 | 25.0 | 50.4 | -25.4 | -8.44 | -52.8 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | both | 3-6 | 33.3 | 52.5 | -19.2 | -3.31 | -36.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 19-16 | 54.3 | 61.9 | -7.6 | -4.51 | -12.9 |  |  | no edge shown yet |
| money_level+pin_value | both | 9-4 | 69.2 | 57.8 | 11.4 | +3.61 | 27.8 |  |  | keep collecting (13/30) |
| rlm+rlm_ratio | both | 3-6 | 33.3 | 52.5 | -19.2 | -3.31 | -36.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 3-10 | 23.1 | 48.0 | -24.9 | -7.31 | -56.2 |  |  | keep collecting (13/30) |
| rlm_ratio+sharp_gap | both | 3-6 | 33.3 | 52.5 | -19.2 | -3.31 | -36.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 27-19 | 58.7 | 57.8 | 0.9 | +0.18 | 0.4 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 6-1 | 85.7 | 52.2 | 33.5 | +3.93 | 56.1 |  |  | keep collecting (7/30) |
| follow_move+money_level | both | 30-10 | 75.0 | 71.6 | 3.4 | +6.35 | 15.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+sharp_gap | both | 5-9 | 35.7 | 30.0 | 5.7 | -2.74 | -19.6 |  |  | keep collecting (14/30) |
| follow_move+pin_value | both | 8-3 | 72.7 | 58.5 | 14.3 | +3.61 | 32.8 |  |  | keep collecting (11/30) |
| pin_value+rlm | both | 2-2 | 50.0 | 53.4 | -3.4 | -0.26 | -6.5 |  |  | keep collecting (4/30) |
| pin_value+sharp_gap | both | 10-7 | 58.8 | 47.7 | 11.2 | +1.22 | 7.2 |  |  | keep collecting (17/30) |
| consensus_gap+pin_value | both | 2-5 | 28.6 | 22.7 | 5.9 | -3.26 | -46.5 |  |  | keep collecting (7/30) |
| book_lag+consensus_gap | both | 3-0 | 100.0 | 55.2 | 44.8 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| book_lag+money_moving | both | 1-0 | 100.0 | 34.5 | 65.5 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | both | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | both | 4-8 | 33.3 | 21.8 | 11.5 | -3.8 | -31.6 |  |  | keep collecting (12/30) |
| money_moving+pin_value | both | 10-6 | 62.5 | 44.6 | 17.9 | +2.34 | 14.6 |  |  | keep collecting (16/30) |
| money_moving+sharp_gap | both | 18-25 | 41.9 | 43.5 | -1.7 | -9.85 | -22.9 |  |  | no edge shown yet |
| consensus_gap+follow_move | both | 3-1 | 75.0 | 75.9 | -0.9 | +0.54 | 13.4 |  |  | keep collecting (4/30) |
| money_level+money_moving | both | 17-8 | 68.0 | 54.6 | 13.4 | +5.52 | 22.1 |  |  | keep collecting (25/30) |
| consensus_gap+pin_rlm | both | 1-4 | 20.0 | 20.7 | -0.7 | -3.0 | -60.0 |  |  | keep collecting (5/30) |
| money_level+pin_rlm | both | 0-3 | 0.0 | 40.2 | -40.2 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | both | 4-8 | 33.3 | 34.8 | -1.4 | -4.31 | -35.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 4-8 | 33.3 | 34.8 | -1.4 | -4.31 | -35.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+money_moving | both | 9-10 | 47.4 | 58.1 | -10.7 | -4.22 | -22.2 |  |  | keep collecting (19/30) |
| follow_move+pin_rlm | both | 3-3 | 50.0 | 48.9 | 1.1 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| money_moving+rlm | both | 3-7 | 30.0 | 46.2 | -16.2 | -4.31 | -43.1 |  |  | keep collecting (10/30) |
| money_moving+rlm_ratio | both | 3-3 | 50.0 | 48.9 | 1.1 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| pin_rlm+pin_value | both | 1-3 | 25.0 | 34.5 | -9.5 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| pin_rlm+rlm | both | 3-3 | 50.0 | 48.9 | 1.1 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| pin_rlm+rlm_ratio | both | 3-3 | 50.0 | 48.9 | 1.1 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| pin_value+rlm_ratio | both | 1-1 | 50.0 | 48.3 | 1.7 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| money_level+rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+rlm | both | 0-1 | 0.0 | 65.5 | -65.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| book_lag+money_level | both | 1-0 | 100.0 | 65.5 | 34.5 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 1-5 | 16.7 | 20.7 | -4.0 | -4.0 | -66.7 |  |  | keep collecting (6/30) |
| pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm | total | 3-1 | 75.0 | 48.3 | 26.7 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| follow_move | moneyline | 23-6 | 79.3 | 79.3 | 0.0 | +3.45 | 11.9 |  |  | keep collecting (29/30) |
| follow_move | spread | 9-14 | 39.1 | 54.7 | -15.6 | -5.79 | -25.2 |  |  | keep collecting (23/30) |
| follow_move | total | 5-5 | 50.0 | 49.7 | 0.3 | -0.53 | -5.3 |  |  | keep collecting (10/30) |
| follow_move | tt_away | 6-5 | 54.5 | 51.6 | 3.0 | +0.33 | 3.0 |  |  | keep collecting (11/30) |
| follow_move | tt_home | 5-6 | 45.5 | 50.9 | -5.5 | -1.66 | -15.1 |  |  | keep collecting (11/30) |
| rlm | moneyline | 0-1 | 0.0 | 79.3 | -79.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm | spread | 1-8 | 11.1 | 48.3 | -37.2 | -7.13 | -79.2 |  |  | keep collecting (9/30) |
| rlm | total | 3-3 | 50.0 | 48.9 | 1.1 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| rlm_ratio | moneyline | 0-1 | 0.0 | 79.3 | -79.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_ratio | spread | 0-4 | 0.0 | 50.0 | -50.0 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| rlm_ratio | total | 3-1 | 75.0 | 48.3 | 26.7 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| money_level | moneyline | 24-4 | 85.7 | 73.0 | 12.7 | +7.6 | 27.1 |  |  | keep collecting (28/30) |
| money_level | spread | 17-12 | 58.6 | 54.8 | 3.8 | +3.42 | 11.8 |  |  | keep collecting (29/30) |
| money_level | total | 14-14 | 50.0 | 51.5 | -1.5 | -1.34 | -4.8 |  |  | keep collecting (28/30) |
| sharp_gap | moneyline | 15-12 | 55.6 | 53.3 | 2.3 | -1.45 | -5.4 |  |  | keep collecting (27/30) |
| sharp_gap | spread | 10-18 | 35.7 | 43.3 | -7.6 | -9.13 | -32.6 |  |  | keep collecting (28/30) |
| sharp_gap | total | 13-16 | 44.8 | 50.1 | -5.2 | -4.31 | -14.9 |  |  | keep collecting (29/30) |
| money_moving | moneyline | 8-12 | 40.0 | 38.3 | 1.7 | -6.4 | -32.0 |  |  | keep collecting (20/30) |
| money_moving | spread | 8-10 | 44.4 | 41.4 | 3.1 | -3.0 | -16.6 |  |  | keep collecting (18/30) |
| money_moving | total | 10-10 | 50.0 | 49.8 | 0.2 | -1.04 | -5.2 |  |  | keep collecting (20/30) |
| pin_value | moneyline | 2-5 | 28.6 | 29.1 | -0.5 | -3.59 | -51.3 |  |  | keep collecting (7/30) |
| pin_value | spread | 10-2 | 83.3 | 55.2 | 28.2 | +6.72 | 56.0 |  |  | keep collecting (12/30) |
| pin_value | total | 7-5 | 58.3 | 50.3 | 8.0 | +1.02 | 8.5 |  |  | keep collecting (12/30) |
| pin_value | tt_away | 9-9 | 50.0 | 49.2 | 0.8 | -1.31 | -7.3 |  |  | keep collecting (18/30) |
| pin_value | tt_home | 11-9 | 55.0 | 50.7 | 4.3 | +0.32 | 1.6 |  |  | keep collecting (20/30) |
| book_lag | spread | 4-0 | 100.0 | 57.8 | 42.2 | +3.29 | 82.4 |  |  | keep collecting (4/30) |
| consensus_gap | moneyline | 9-20 | 31.0 | 26.8 | 4.3 | -9.52 | -32.8 |  |  | keep collecting (29/30) |
| consensus_gap | spread | 4-3 | 57.1 | 52.2 | 4.9 | +0.29 | 4.2 |  |  | keep collecting (7/30) |
| consensus_gap+money_level | moneyline | 5-1 | 83.3 | 50.0 | 33.3 | +3.1 | 51.6 |  |  | keep collecting (6/30) |
| follow_move+rlm | moneyline | 0-1 | 0.0 | 79.3 | -79.3 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 0-1 | 0.0 | 79.3 | -79.3 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 12-3 | 80.0 | 79.3 | 0.7 | +2.19 | 14.6 |  |  | keep collecting (15/30) |
| rlm+rlm_ratio | moneyline | 0-1 | 0.0 | 79.3 | -79.3 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+sharp_gap | moneyline | 0-1 | 0.0 | 79.3 | -79.3 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 0-1 | 0.0 | 79.3 | -79.3 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+sharp_gap | moneyline | 5-8 | 38.5 | 29.7 | 8.8 | -1.74 | -13.4 |  |  | keep collecting (13/30) |
| follow_move+money_level | moneyline | 22-3 | 88.0 | 79.3 | 8.7 | +6.04 | 24.2 |  |  | keep collecting (25/30) |
| money_level+sharp_gap | moneyline | 13-3 | 81.2 | 72.0 | 9.3 | +3.65 | 22.8 |  |  | keep collecting (16/30) |
| consensus_gap+pin_value | moneyline | 1-5 | 16.7 | 20.7 | -4.0 | -4.04 | -67.3 |  |  | keep collecting (6/30) |
| pin_value+sharp_gap | moneyline | 1-3 | 25.0 | 35.3 | -10.3 | -2.56 | -63.9 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | moneyline | 3-0 | 100.0 | 79.3 | 20.7 | +1.54 | 51.2 |  |  | keep collecting (3/30) |
| consensus_gap+money_moving | moneyline | 3-8 | 27.3 | 20.7 | 6.6 | -4.58 | -41.6 |  |  | keep collecting (11/30) |
| money_moving+pin_value | moneyline | 2-3 | 40.0 | 32.4 | 7.6 | -1.59 | -31.9 |  |  | keep collecting (5/30) |
| consensus_gap+pin_rlm | moneyline | 1-4 | 20.0 | 20.7 | -0.7 | -3.0 | -60.0 |  |  | keep collecting (5/30) |
| money_level+money_moving | moneyline | 6-2 | 75.0 | 64.7 | 10.3 | +1.64 | 20.5 |  |  | keep collecting (8/30) |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 20.7 | -20.7 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 1-5 | 16.7 | 20.7 | -4.0 | -4.0 | -66.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | moneyline | 6-8 | 42.9 | 41.6 | 1.2 | -3.56 | -25.5 |  |  | keep collecting (14/30) |
| pin_rlm+sharp_gap | moneyline | 1-5 | 16.7 | 20.7 | -4.0 | -4.0 | -66.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+money_moving | moneyline | 5-1 | 83.3 | 79.3 | 4.0 | +1.18 | 19.7 |  |  | keep collecting (6/30) |
| pin_rlm+pin_value | moneyline | 0-2 | 0.0 | 20.7 | -20.7 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| follow_move+pin_value | moneyline | 1-0 | 100.0 | 79.3 | 20.7 | +0.44 | 44.4 |  |  | keep collecting (1/30) |
| money_level+pin_value | moneyline | 1-0 | 100.0 | 79.3 | 20.7 | +0.44 | 44.4 |  |  | keep collecting (1/30) |
| follow_move+rlm | spread | 1-8 | 11.1 | 48.3 | -37.2 | -7.13 | -79.2 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-4 | 0.0 | 50.0 | -50.0 | -4.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 4-9 | 30.8 | 48.8 | -18.0 | -5.39 | -41.4 |  |  | keep collecting (13/30) |
| money_level+pin_value | spread | 5-1 | 83.3 | 60.3 | 23.0 | +3.57 | 59.5 |  |  | keep collecting (6/30) |
| rlm+rlm_ratio | spread | 0-4 | 0.0 | 50.0 | -50.0 | -4.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 0-7 | 0.0 | 43.3 | -43.3 | -7.0 | -100.0 |  |  | keep collecting (7/30) |
| rlm_ratio+sharp_gap | spread | 0-4 | 0.0 | 50.0 | -50.0 | -4.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 6-6 | 50.0 | 60.3 | -10.3 | -0.47 | -3.9 |  |  | keep collecting (12/30) |
| follow_move+pin_value | spread | 5-1 | 83.3 | 60.3 | 23.0 | +3.41 | 56.9 |  |  | keep collecting (6/30) |
| pin_value+rlm | spread | 1-0 | 100.0 | 65.5 | 34.5 | +0.87 | 87.0 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | spread | 6-7 | 46.2 | 48.8 | -2.7 | -1.62 | -12.5 |  |  | keep collecting (13/30) |
| consensus_gap+sharp_gap | spread | 0-1 | 0.0 | 34.5 | -34.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| book_lag+consensus_gap | spread | 3-0 | 100.0 | 55.2 | 44.8 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| pin_value+sharp_gap | spread | 4-1 | 80.0 | 53.1 | 26.9 | +2.47 | 49.4 |  |  | keep collecting (5/30) |
| book_lag+money_moving | spread | 1-0 | 100.0 | 34.5 | 65.5 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | spread | 1-0 | 100.0 | 34.5 | 65.5 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| consensus_gap+pin_value | spread | 1-0 | 100.0 | 34.5 | 65.5 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| money_moving+pin_value | spread | 4-0 | 100.0 | 50.0 | 50.0 | +3.43 | 85.8 |  |  | keep collecting (4/30) |
| money_level+money_moving | spread | 6-3 | 66.7 | 48.3 | 18.4 | +2.39 | 26.6 |  |  | keep collecting (9/30) |
| money_moving+sharp_gap | spread | 5-9 | 35.7 | 38.9 | -3.2 | -4.55 | -32.5 |  |  | keep collecting (14/30) |
| follow_move+money_moving | spread | 1-4 | 20.0 | 46.9 | -26.9 | -3.09 | -61.8 |  |  | keep collecting (5/30) |
| money_moving+rlm | spread | 0-4 | 0.0 | 42.2 | -42.2 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| follow_move+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_moving+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm+rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+follow_move | spread | 0-1 | 0.0 | 65.5 | -65.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+rlm | spread | 0-1 | 0.0 | 65.5 | -65.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| book_lag+money_level | spread | 1-0 | 100.0 | 65.5 | 34.5 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| consensus_gap+money_level | spread | 1-0 | 100.0 | 65.5 | 34.5 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | total | 8-9 | 47.1 | 51.3 | -4.3 | -1.84 | -10.8 |  |  | keep collecting (17/30) |
| pin_value+sharp_gap | total | 5-3 | 62.5 | 50.4 | 12.1 | +1.31 | 16.4 |  |  | keep collecting (8/30) |
| money_level+pin_value | total | 3-3 | 50.0 | 51.7 | -1.7 | -0.4 | -6.7 |  |  | keep collecting (6/30) |
| money_moving+sharp_gap | total | 7-8 | 46.7 | 49.7 | -3.0 | -1.73 | -11.5 |  |  | keep collecting (15/30) |
| money_level+money_moving | total | 5-3 | 62.5 | 51.7 | 10.8 | +1.49 | 18.6 |  |  | keep collecting (8/30) |
| money_moving+pin_value | total | 4-3 | 57.1 | 50.2 | 6.9 | +0.5 | 7.2 |  |  | keep collecting (7/30) |
| follow_move+money_moving | total | 3-5 | 37.5 | 49.1 | -11.6 | -2.31 | -28.9 |  |  | keep collecting (8/30) |
| follow_move+pin_rlm | total | 3-1 | 75.0 | 48.3 | 26.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+pin_value | total | 1-2 | 33.3 | 49.4 | -16.1 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| follow_move+rlm | total | 3-3 | 50.0 | 48.9 | 1.1 | -0.31 | -5.2 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | total | 3-1 | 75.0 | 48.3 | 26.7 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 3-4 | 42.9 | 48.8 | -5.9 | -1.31 | -18.7 |  |  | keep collecting (7/30) |
| money_moving+pin_rlm | total | 3-1 | 75.0 | 48.3 | 26.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm | total | 3-3 | 50.0 | 48.9 | 1.1 | -0.31 | -5.2 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| money_moving+rlm_ratio | total | 3-1 | 75.0 | 48.3 | 26.7 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+pin_value | total | 1-1 | 50.0 | 48.3 | 1.7 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| pin_rlm+rlm | total | 3-1 | 75.0 | 48.3 | 26.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | total | 3-1 | 75.0 | 48.3 | 26.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | total | 3-1 | 75.0 | 48.3 | 26.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm | total | 1-2 | 33.3 | 49.4 | -16.1 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| pin_value+rlm_ratio | total | 1-1 | 50.0 | 48.3 | 1.7 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| rlm+rlm_ratio | total | 3-1 | 75.0 | 48.3 | 26.7 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | total | 3-2 | 60.0 | 48.3 | 11.7 | +0.69 | 13.8 |  |  | keep collecting (5/30) |
| rlm_ratio+sharp_gap | total | 3-1 | 75.0 | 48.3 | 26.7 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | total | 2-1 | 66.7 | 51.7 | 14.9 | +0.78 | 26.0 |  |  | keep collecting (3/30) |
| follow_move+pin_value | tt_home | 1-0 | 100.0 | 53.4 | 46.6 | +0.89 | 88.5 |  |  | keep collecting (1/30) |

## By ticket volume and Pinnacle limit (both markets)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_rlm | close | 40k+ bets | 4-8 | 33.3 | -1.4 | -35.9 |  |
| pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 17.2 | 13.8 |  |
| pin_rlm | close | pin $50k+ | 1-6 | 14.3 | -14.8 | -71.4 |  |
| follow_move | close | 40k+ bets | 48-36 | 57.1 | -4.6 | -5.0 |  |
| follow_move | close | pin $10-50k | 10-5 | 66.7 | 7.1 | 5.5 |  |
| follow_move | close | pin $50k+ | 27-20 | 57.4 | -9.8 | -7.9 |  |
| follow_move | close | pin limit <$10k | 11-11 | 50.0 | -1.3 | -6.1 |  |
| rlm | close | 40k+ bets | 4-12 | 25.0 | -25.4 | -52.8 |  |
| rlm | close | pin $10-50k | 3-3 | 50.0 | 1.1 | -5.2 |  |
| rlm | close | pin $50k+ | 1-9 | 10.0 | -41.4 | -81.3 |  |
| rlm_ratio | close | 40k+ bets | 3-6 | 33.3 | -19.2 | -36.8 |  |
| rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 26.7 | 42.2 |  |
| rlm_ratio | close | pin $50k+ | 0-5 | 0.0 | -55.9 | -100.0 |  |
| money_level | close | 40k+ bets | 55-30 | 64.7 | 5.0 | 11.4 |  |
| money_level | close | pin $10-50k | 18-14 | 56.2 | 0.4 | -2.8 |  |
| money_level | close | pin $50k+ | 37-16 | 69.8 | 7.7 | 19.9 |  |
| sharp_gap | close | 40k+ bets | 38-46 | 45.2 | -3.6 | -17.7 |  |
| sharp_gap | close | pin $10-50k | 15-17 | 46.9 | -5.0 | -16.5 |  |
| sharp_gap | close | pin $50k+ | 23-29 | 44.2 | -2.8 | -18.5 |  |
| money_moving | close | 40k+ bets | 26-32 | 44.8 | 1.6 | -18.0 |  |
| money_moving | close | pin $10-50k | 11-12 | 47.8 | -1.9 | -13.9 |  |
| money_moving | close | pin $50k+ | 15-20 | 42.9 | 3.9 | -20.7 |  |
| pin_value | close | 40k+ bets | 39-30 | 56.5 | 7.7 | 4.6 |  |
| pin_value | close | pin $10-50k | 7-7 | 50.0 | 3.9 | -7.0 |  |
| pin_value | close | pin $50k+ | 12-5 | 70.6 | 22.1 | 30.2 |  |
| pin_value | close | pin limit <$10k | 20-18 | 52.6 | 2.6 | -2.6 |  |
| book_lag | close | 40k+ bets | 4-0 | 100.0 | 42.2 | 82.4 |  |
| book_lag | close | pin $50k+ | 4-0 | 100.0 | 42.2 | 82.4 |  |
| consensus_gap | close | 40k+ bets | 13-23 | 36.1 | 4.4 | -25.6 |  |
| consensus_gap | close | pin $10-50k | 1-4 | 20.0 | -12.4 | -74.3 |  |
| consensus_gap | close | pin $50k+ | 12-19 | 38.7 | 7.1 | -17.8 |  |
| follow_move+rlm | close | 40k+ bets | 4-12 | 25.0 | -25.4 | -52.8 |  |
| follow_move+rlm_ratio | close | 40k+ bets | 3-6 | 33.3 | -19.2 | -36.8 |  |
| follow_move+sharp_gap | close | 40k+ bets | 19-16 | 54.3 | -7.6 | -12.9 |  |
| money_level+pin_value | close | 40k+ bets | 9-4 | 69.2 | 11.4 | 27.8 |  |
| rlm+rlm_ratio | close | 40k+ bets | 3-6 | 33.3 | -19.2 | -36.8 |  |
| rlm+sharp_gap | close | 40k+ bets | 3-10 | 23.1 | -24.9 | -56.2 |  |
| rlm_ratio+sharp_gap | close | 40k+ bets | 3-6 | 33.3 | -19.2 | -36.8 |  |
| money_level+sharp_gap | close | 40k+ bets | 27-19 | 58.7 | 0.9 | 0.4 |  |
| consensus_gap+money_level | close | 40k+ bets | 6-1 | 85.7 | 33.5 | 56.1 |  |
| follow_move+money_level | close | 40k+ bets | 30-10 | 75.0 | 3.4 | 15.9 |  |
| consensus_gap+sharp_gap | close | 40k+ bets | 5-9 | 35.7 | 5.7 | -19.6 |  |
| follow_move+pin_value | close | 40k+ bets | 8-3 | 72.7 | 14.3 | 32.8 |  |
| pin_value+rlm | close | 40k+ bets | 2-2 | 50.0 | -3.4 | -6.5 |  |
| pin_value+sharp_gap | close | 40k+ bets | 10-7 | 58.8 | 11.2 | 7.2 |  |
| consensus_gap+pin_value | close | 40k+ bets | 2-5 | 28.6 | 5.9 | -46.5 |  |
| book_lag+consensus_gap | close | 40k+ bets | 3-0 | 100.0 | 44.8 | 82.0 |  |
| book_lag+money_moving | close | 40k+ bets | 1-0 | 100.0 | 65.5 | 78.1 |  |
| book_lag+pin_value | close | 40k+ bets | 2-0 | 100.0 | 50.0 | 80.7 |  |
| consensus_gap+money_moving | close | 40k+ bets | 4-8 | 33.3 | 11.5 | -31.6 |  |
| money_moving+pin_value | close | 40k+ bets | 10-6 | 62.5 | 17.9 | 14.6 |  |
| money_moving+sharp_gap | close | 40k+ bets | 18-25 | 41.9 | -1.7 | -22.9 |  |
| consensus_gap+follow_move | close | 40k+ bets | 3-1 | 75.0 | -0.9 | 13.4 |  |
| money_level+money_moving | close | 40k+ bets | 17-8 | 68.0 | 13.4 | 22.1 |  |
| consensus_gap+pin_rlm | close | 40k+ bets | 1-4 | 20.0 | -0.7 | -60.0 |  |
| money_level+pin_rlm | close | 40k+ bets | 0-3 | 0.0 | -40.2 | -100.0 |  |
| money_moving+pin_rlm | close | 40k+ bets | 4-8 | 33.3 | -1.4 | -35.9 |  |
| pin_rlm+sharp_gap | close | 40k+ bets | 4-8 | 33.3 | -1.4 | -35.9 |  |
| follow_move+money_moving | close | 40k+ bets | 9-10 | 47.4 | -10.7 | -22.2 |  |
| follow_move+pin_rlm | close | 40k+ bets | 3-3 | 50.0 | 1.1 | -5.2 |  |
| money_moving+rlm | close | 40k+ bets | 3-7 | 30.0 | -16.2 | -43.1 |  |
| money_moving+rlm_ratio | close | 40k+ bets | 3-3 | 50.0 | 1.1 | -5.2 |  |
| pin_rlm+pin_value | close | 40k+ bets | 1-3 | 25.0 | -9.5 | -53.2 |  |
| pin_rlm+rlm | close | 40k+ bets | 3-3 | 50.0 | 1.1 | -5.2 |  |
| pin_rlm+rlm_ratio | close | 40k+ bets | 3-3 | 50.0 | 1.1 | -5.2 |  |
| pin_value+rlm_ratio | close | 40k+ bets | 1-1 | 50.0 | 1.7 | -6.5 |  |
| money_level+rlm | close | 40k+ bets | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_level+rlm_ratio | close | 40k+ bets | 0-2 | 0.0 | -50.0 | -100.0 |  |
| consensus_gap+rlm | close | 40k+ bets | 0-1 | 0.0 | -65.5 | -100.0 |  |
| book_lag+money_level | close | 40k+ bets | 1-0 | 100.0 | 34.5 | 83.3 |  |
| money_level+sharp_gap | close | pin $10-50k | 10-9 | 52.6 | -3.1 | -9.5 |  |
| pin_value+sharp_gap | close | pin $10-50k | 5-4 | 55.6 | 8.4 | 3.5 |  |
| money_level+pin_value | close | pin $10-50k | 3-3 | 50.0 | -1.7 | -6.7 |  |
| consensus_gap+pin_value | close | pin $10-50k | 0-2 | 0.0 | -20.7 | -100.0 |  |
| follow_move+money_level | close | pin $10-50k | 7-1 | 87.5 | 18.5 | 26.7 |  |
| follow_move+sharp_gap | close | pin $10-50k | 6-4 | 60.0 | 2.1 | -3.7 |  |
| money_moving+sharp_gap | close | pin $10-50k | 7-9 | 43.8 | -5.8 | -19.2 |  |
| consensus_gap+follow_move | close | pin $10-50k | 1-0 | 100.0 | 20.7 | 28.6 |  |
| consensus_gap+money_level | close | pin $10-50k | 1-0 | 100.0 | 20.7 | 28.6 |  |
| consensus_gap+sharp_gap | close | pin $10-50k | 1-1 | 50.0 | 0.0 | -35.7 |  |
| money_level+money_moving | close | pin $10-50k | 6-3 | 66.7 | 8.8 | 15.0 |  |
| money_moving+pin_value | close | pin $10-50k | 4-4 | 50.0 | 3.4 | -6.2 |  |
| follow_move+money_moving | close | pin $10-50k | 5-5 | 50.0 | -5.2 | -15.5 |  |
| follow_move+pin_rlm | close | pin $10-50k | 3-1 | 75.0 | 26.7 | 42.2 |  |
| follow_move+pin_value | close | pin $10-50k | 1-2 | 33.3 | -16.1 | -37.7 |  |
| follow_move+rlm | close | pin $10-50k | 3-3 | 50.0 | 1.1 | -5.2 |  |
| follow_move+rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 26.7 | 42.2 |  |
| money_moving+pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 17.2 | 13.8 |  |
| money_moving+rlm | close | pin $10-50k | 3-3 | 50.0 | 1.1 | -5.2 |  |
| money_moving+rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 26.7 | 42.2 |  |
| pin_rlm+pin_value | close | pin $10-50k | 1-2 | 33.3 | -5.7 | -37.7 |  |
| pin_rlm+rlm | close | pin $10-50k | 3-1 | 75.0 | 26.7 | 42.2 |  |
| pin_rlm+rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 26.7 | 42.2 |  |
| pin_rlm+sharp_gap | close | pin $10-50k | 3-2 | 60.0 | 17.2 | 13.8 |  |
| pin_value+rlm | close | pin $10-50k | 1-2 | 33.3 | -16.1 | -37.7 |  |
| pin_value+rlm_ratio | close | pin $10-50k | 1-1 | 50.0 | 1.7 | -6.5 |  |
| rlm+rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 26.7 | 42.2 |  |
| rlm+sharp_gap | close | pin $10-50k | 3-2 | 60.0 | 11.7 | 13.8 |  |
| rlm_ratio+sharp_gap | close | pin $10-50k | 3-1 | 75.0 | 26.7 | 42.2 |  |
| consensus_gap+money_moving | close | pin $10-50k | 0-1 | 0.0 | -20.7 | -100.0 |  |
| consensus_gap+pin_rlm | close | pin $10-50k | 0-1 | 0.0 | -20.7 | -100.0 |  |
| follow_move+rlm | close | pin $50k+ | 1-9 | 10.0 | -41.4 | -81.3 |  |
| follow_move+rlm_ratio | close | pin $50k+ | 0-5 | 0.0 | -55.9 | -100.0 |  |
| follow_move+sharp_gap | close | pin $50k+ | 13-12 | 52.0 | -11.4 | -16.5 |  |
| money_level+pin_value | close | pin $50k+ | 6-1 | 85.7 | 22.7 | 57.4 |  |
| rlm+rlm_ratio | close | pin $50k+ | 0-5 | 0.0 | -55.9 | -100.0 |  |
| rlm+sharp_gap | close | pin $50k+ | 0-8 | 0.0 | -47.8 | -100.0 |  |
| rlm_ratio+sharp_gap | close | pin $50k+ | 0-5 | 0.0 | -55.9 | -100.0 |  |
| consensus_gap+money_level | close | pin $50k+ | 5-1 | 83.3 | 35.6 | 60.7 |  |
| follow_move+money_level | close | pin $50k+ | 23-9 | 71.9 | -0.3 | 13.2 |  |
| consensus_gap+sharp_gap | close | pin $50k+ | 4-8 | 33.3 | 6.6 | -16.9 |  |
| follow_move+pin_value | close | pin $50k+ | 6-1 | 85.7 | 22.7 | 55.1 |  |
| pin_value+rlm | close | pin $50k+ | 1-0 | 100.0 | 34.5 | 87.0 |  |
| money_level+sharp_gap | close | pin $50k+ | 17-10 | 63.0 | 3.7 | 7.4 |  |
| consensus_gap+pin_value | close | pin $50k+ | 2-3 | 40.0 | 16.6 | -25.1 |  |
| pin_value+sharp_gap | close | pin $50k+ | 5-3 | 62.5 | 14.2 | 11.4 |  |
| book_lag+consensus_gap | close | pin $50k+ | 3-0 | 100.0 | 44.8 | 82.0 |  |
| book_lag+money_moving | close | pin $50k+ | 1-0 | 100.0 | 65.5 | 78.1 |  |
| book_lag+pin_value | close | pin $50k+ | 2-0 | 100.0 | 50.0 | 80.7 |  |
| consensus_gap+money_moving | close | pin $50k+ | 4-7 | 36.4 | 14.4 | -25.4 |  |
| money_moving+pin_value | close | pin $50k+ | 6-2 | 75.0 | 32.3 | 35.5 |  |
| consensus_gap+pin_rlm | close | pin $50k+ | 1-3 | 25.0 | 4.3 | -50.0 |  |
| money_level+money_moving | close | pin $50k+ | 11-5 | 68.8 | 15.9 | 26.1 |  |
| money_level+pin_rlm | close | pin $50k+ | 0-3 | 0.0 | -40.2 | -100.0 |  |
| money_moving+pin_rlm | close | pin $50k+ | 1-6 | 14.3 | -14.8 | -71.4 |  |
| money_moving+sharp_gap | close | pin $50k+ | 11-16 | 40.7 | 0.8 | -25.1 |  |
| pin_rlm+sharp_gap | close | pin $50k+ | 1-6 | 14.3 | -14.8 | -71.4 |  |
| follow_move+money_moving | close | pin $50k+ | 4-5 | 44.4 | -16.9 | -29.7 |  |
| pin_rlm+pin_value | close | pin $50k+ | 0-1 | 0.0 | -20.7 | -100.0 |  |
| consensus_gap+follow_move | close | pin $50k+ | 2-1 | 66.7 | -8.0 | 8.4 |  |
| money_moving+rlm | close | pin $50k+ | 0-4 | 0.0 | -42.2 | -100.0 |  |
| follow_move+pin_rlm | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_level+rlm | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_level+rlm_ratio | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_moving+rlm_ratio | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| pin_rlm+rlm | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| pin_rlm+rlm_ratio | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| consensus_gap+rlm | close | pin $50k+ | 0-1 | 0.0 | -65.5 | -100.0 |  |
| book_lag+money_level | close | pin $50k+ | 1-0 | 100.0 | 34.5 | 83.3 |  |
| follow_move+pin_value | close | pin limit <$10k | 1-0 | 100.0 | 46.6 | 88.5 |  |
| pin_rlm | early | <10k bets | 1-2 | 33.3 | 12.6 | -30.7 | -2.3 |
| pin_rlm | early | pin $10-50k | 1-0 | 100.0 | 79.3 | 108.0 | 1.9 |
| pin_rlm | early | pin limit <$10k | 0-2 | 0.0 | -20.7 | -100.0 | -4.4 |
| follow_move | early | 10-40k bets | 2-1 | 66.7 | -8.0 | 6.3 | -0.4 |
| follow_move | early | 40k+ bets | 3-2 | 60.0 | -1.4 | -10.9 | -0.1 |
| follow_move | early | <10k bets | 19-7 | 73.1 | 3.2 | 12.6 | -0.21 |
| follow_move | early | pin $10-50k | 6-5 | 54.5 | -6.3 | -1.2 | 0.15 |
| follow_move | early | pin $50k+ | 4-2 | 66.7 | 4.6 | 6.1 | -0.33 |
| follow_move | early | pin limit <$10k | 14-3 | 82.4 | 5.5 | 15.8 | -0.4 |
| rlm | early | 40k+ bets | 0-1 | 0.0 | -34.5 | -100.0 | 0.0 |
| rlm | early | <10k bets | 0-1 | 0.0 | -34.5 | -100.0 | 1.0 |
| rlm | early | pin $10-50k | 0-1 | 0.0 | -34.5 | -100.0 | 1.0 |
| rlm | early | pin $50k+ | 0-1 | 0.0 | -34.5 | -100.0 | 0.0 |
| rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -34.5 | -100.0 | 0.0 |
| rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -34.5 | -100.0 | 0.0 |
| money_level | early | 10-40k bets | 3-3 | 50.0 | -9.8 | -13.8 | -0.28 |
| money_level | early | 40k+ bets | 4-4 | 50.0 | -15.1 | -19.9 | -0.06 |
| money_level | early | <10k bets | 32-15 | 68.1 | 9.0 | 15.9 | -1.03 |
| money_level | early | pin $10-50k | 12-10 | 54.5 | -0.3 | 2.1 | -0.24 |
| money_level | early | pin $50k+ | 5-2 | 71.4 | 4.4 | 20.1 | -0.36 |
| money_level | early | pin limit <$10k | 22-10 | 68.8 | 6.9 | 10.0 | -1.34 |
| sharp_gap | early | 10-40k bets | 3-3 | 50.0 | 4.0 | 3.1 | 0.27 |
| sharp_gap | early | 40k+ bets | 4-5 | 44.4 | -13.8 | -29.5 | -0.06 |
| sharp_gap | early | <10k bets | 26-21 | 55.3 | 5.6 | 0.3 | -0.15 |
| sharp_gap | early | pin $10-50k | 12-10 | 54.5 | 2.2 | 4.9 | 0.06 |
| sharp_gap | early | pin $50k+ | 3-5 | 37.5 | -18.1 | -37.5 | 0.33 |
| sharp_gap | early | pin limit <$10k | 18-14 | 56.2 | 8.2 | -1.3 | -0.32 |
| money_moving | early | <10k bets | 11-6 | 64.7 | 10.1 | 15.8 | -0.1 |
| money_moving | early | pin $10-50k | 5-2 | 71.4 | 21.2 | 40.0 | -0.16 |
| money_moving | early | pin limit <$10k | 6-4 | 60.0 | 2.4 | -1.1 | -0.06 |
| pin_value | early | 10-40k bets | 1-2 | 33.3 | -21.8 | -39.3 | 0.0 |
| pin_value | early | 40k+ bets | 4-2 | 66.7 | 22.1 | 22.5 | 0.0 |
| pin_value | early | <10k bets | 15-13 | 53.6 | 5.3 | 0.8 | 0.42 |
| pin_value | early | pin $10-50k | 6-3 | 66.7 | 6.1 | 27.8 | -0.28 |
| pin_value | early | pin $50k+ | 3-0 | 100.0 | 55.2 | 81.1 | 0.0 |
| pin_value | early | pin limit <$10k | 11-14 | 44.0 | -0.2 | -18.2 | 0.58 |
| book_lag | early | <10k bets | 0-2 | 0.0 | -50.0 | -100.0 | -0.75 |
| book_lag | early | pin $10-50k | 0-2 | 0.0 | -50.0 | -100.0 | -0.75 |
| consensus_gap | early | 10-40k bets | 2-2 | 50.0 | 6.9 | 7.0 | 0.4 |
| consensus_gap | early | 40k+ bets | 2-2 | 50.0 | 25.9 | -6.4 | 0.17 |
| consensus_gap | early | <10k bets | 7-16 | 30.4 | -3.6 | -43.6 | 0.29 |
| consensus_gap | early | pin $10-50k | 4-5 | 44.4 | 4.2 | -7.6 | 0.23 |
| consensus_gap | early | pin $50k+ | 3-3 | 50.0 | 12.1 | -7.3 | 0.43 |
| consensus_gap | early | pin limit <$10k | 4-12 | 25.0 | -3.9 | -55.6 | 0.26 |
| consensus_gap+follow_move | early | 10-40k bets | 1-0 | 100.0 | 34.5 | 82.0 | 0.0 |
| consensus_gap+money_level | early | 10-40k bets | 1-0 | 100.0 | 34.5 | 82.0 | 0.0 |
| consensus_gap+pin_value | early | 10-40k bets | 1-0 | 100.0 | 34.5 | 82.0 | 0.0 |
| consensus_gap+sharp_gap | early | 10-40k bets | 2-2 | 50.0 | 6.9 | 7.0 | 0.4 |
| follow_move+money_level | early | 10-40k bets | 2-1 | 66.7 | -8.0 | 6.3 | -0.4 |
| follow_move+pin_value | early | 10-40k bets | 1-0 | 100.0 | 34.5 | 82.0 | 0.0 |
| follow_move+sharp_gap | early | 10-40k bets | 1-0 | 100.0 | 34.5 | 82.0 | 0.0 |
| money_level+pin_value | early | 10-40k bets | 1-0 | 100.0 | 34.5 | 82.0 | 0.0 |
| money_level+sharp_gap | early | 10-40k bets | 1-1 | 50.0 | -8.6 | -9.0 | 0.0 |
| pin_value+sharp_gap | early | 10-40k bets | 1-0 | 100.0 | 34.5 | 82.0 | 0.0 |
| follow_move+rlm | early | 40k+ bets | 0-1 | 0.0 | -34.5 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -34.5 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | 40k+ bets | 3-2 | 60.0 | -1.4 | -10.9 | -0.1 |
| rlm+rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -34.5 | -100.0 | 0.0 |
| rlm+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -34.5 | -100.0 | 0.0 |
| rlm_ratio+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -34.5 | -100.0 | 0.0 |
| money_level+pin_value | early | 40k+ bets | 0-1 | 0.0 | -51.7 | -100.0 | 0.0 |
| money_level+sharp_gap | early | 40k+ bets | 3-4 | 42.9 | -22.2 | -35.5 | -0.07 |
| pin_value+sharp_gap | early | 40k+ bets | 1-1 | 50.0 | 6.9 | -8.4 | 0.0 |
| follow_move+money_level | early | 40k+ bets | 2-1 | 66.7 | -12.6 | -12.6 | -0.17 |
| consensus_gap+pin_value | early | 40k+ bets | 1-0 | 100.0 | 65.5 | 78.1 | 0.0 |
| follow_move+pin_value | early | 40k+ bets | 1-0 | 100.0 | 65.5 | 83.3 | 0.0 |
| follow_move+money_level | early | <10k bets | 17-5 | 77.3 | 6.4 | 17.0 | -0.9 |
| follow_move+money_moving | early | <10k bets | 6-1 | 85.7 | 12.3 | 40.4 | -0.44 |
| follow_move+pin_value | early | <10k bets | 2-0 | 100.0 | 34.5 | 90.6 | 0.0 |
| follow_move+sharp_gap | early | <10k bets | 10-3 | 76.9 | 9.8 | 23.7 | -0.09 |
| money_level+money_moving | early | <10k bets | 8-3 | 72.7 | 9.1 | 25.7 | -0.74 |
| money_level+pin_value | early | <10k bets | 5-1 | 83.3 | 25.3 | 60.7 | -0.58 |
| money_level+sharp_gap | early | <10k bets | 22-11 | 66.7 | 10.0 | 18.3 | -0.77 |
| money_moving+pin_value | early | <10k bets | 4-2 | 66.7 | 16.7 | 28.2 | 1.0 |
| money_moving+sharp_gap | early | <10k bets | 5-3 | 62.5 | 10.3 | 16.6 | 0.16 |
| pin_value+sharp_gap | early | <10k bets | 5-4 | 55.6 | 10.0 | 7.2 | 0.62 |
| consensus_gap+sharp_gap | early | <10k bets | 5-8 | 38.5 | 5.3 | -29.5 | 0.18 |
| consensus_gap+follow_move | early | <10k bets | 2-0 | 100.0 | 20.7 | 46.8 | -0.35 |
| consensus_gap+money_level | early | <10k bets | 3-1 | 75.0 | 13.8 | 20.1 | -2.83 |
| book_lag+consensus_gap | early | <10k bets | 0-1 | 0.0 | -34.5 | -100.0 | 0.5 |
| consensus_gap+pin_value | early | <10k bets | 0-5 | 0.0 | -29.7 | -100.0 | 1.9 |
| consensus_gap+pin_rlm | early | <10k bets | 1-2 | 33.3 | 12.6 | -30.7 | -2.3 |
| money_level+pin_rlm | early | <10k bets | 0-1 | 0.0 | -20.7 | -100.0 | -10.6 |
| pin_rlm+sharp_gap | early | <10k bets | 1-2 | 33.3 | 12.6 | -30.7 | -2.3 |
| follow_move+rlm | early | <10k bets | 0-1 | 0.0 | -34.5 | -100.0 | 1.0 |
| book_lag+money_level | early | <10k bets | 0-1 | 0.0 | -65.5 | -100.0 | -2.0 |
| book_lag+money_moving | early | <10k bets | 0-1 | 0.0 | -65.5 | -100.0 | -2.0 |
| book_lag+sharp_gap | early | <10k bets | 0-1 | 0.0 | -65.5 | -100.0 | -2.0 |
| consensus_gap+money_moving | early | <10k bets | 1-1 | 50.0 | 29.3 | 4.0 | 3.45 |
| pin_rlm+pin_value | early | <10k bets | 0-1 | 0.0 | -20.7 | -100.0 | 1.8 |
| money_moving+pin_rlm | early | <10k bets | 1-0 | 100.0 | 79.3 | 108.0 | 1.9 |
| money_level+pin_value | early | pin $10-50k | 3-1 | 75.0 | 12.9 | 45.2 | -0.38 |
| money_level+sharp_gap | early | pin $10-50k | 10-8 | 55.6 | 1.1 | 3.0 | -0.11 |
| pin_value+sharp_gap | early | pin $10-50k | 3-1 | 75.0 | 12.9 | 45.2 | -0.38 |
| follow_move+money_level | early | pin $10-50k | 5-4 | 55.6 | -7.7 | 0.4 | 0.08 |
| follow_move+sharp_gap | early | pin $10-50k | 5-2 | 71.4 | 12.8 | 29.0 | 0.21 |
| consensus_gap+sharp_gap | early | pin $10-50k | 3-0 | 100.0 | 64.4 | 113.7 | 0.3 |
| follow_move+money_moving | early | pin $10-50k | 2-0 | 100.0 | 34.5 | 90.6 | 0.0 |
| follow_move+pin_value | early | pin $10-50k | 2-0 | 100.0 | 34.5 | 90.6 | 0.0 |
| money_level+money_moving | early | pin $10-50k | 2-1 | 66.7 | 11.5 | 31.1 | -1.33 |
| money_moving+pin_value | early | pin $10-50k | 3-1 | 75.0 | 17.2 | 44.1 | 0.25 |
| money_moving+sharp_gap | early | pin $10-50k | 2-1 | 66.7 | 16.1 | 35.3 | -0.03 |
| book_lag+consensus_gap | early | pin $10-50k | 0-1 | 0.0 | -34.5 | -100.0 | 0.5 |
| follow_move+rlm | early | pin $10-50k | 0-1 | 0.0 | -34.5 | -100.0 | 1.0 |
| book_lag+money_level | early | pin $10-50k | 0-1 | 0.0 | -65.5 | -100.0 | -2.0 |
| book_lag+money_moving | early | pin $10-50k | 0-1 | 0.0 | -65.5 | -100.0 | -2.0 |
| book_lag+sharp_gap | early | pin $10-50k | 0-1 | 0.0 | -65.5 | -100.0 | -2.0 |
| consensus_gap+money_level | early | pin $10-50k | 1-0 | 100.0 | 34.5 | 87.0 | 0.0 |
| consensus_gap+pin_value | early | pin $10-50k | 0-1 | 0.0 | -65.5 | -100.0 | 0.0 |
| consensus_gap+money_moving | early | pin $10-50k | 1-0 | 100.0 | 79.3 | 108.0 | 1.9 |
| consensus_gap+pin_rlm | early | pin $10-50k | 1-0 | 100.0 | 79.3 | 108.0 | 1.9 |
| money_moving+pin_rlm | early | pin $10-50k | 1-0 | 100.0 | 79.3 | 108.0 | 1.9 |
| pin_rlm+sharp_gap | early | pin $10-50k | 1-0 | 100.0 | 79.3 | 108.0 | 1.9 |
| follow_move+rlm | early | pin $50k+ | 0-1 | 0.0 | -34.5 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -34.5 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | pin $50k+ | 3-2 | 60.0 | 1.4 | -0.0 | 0.0 |
| rlm+rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -34.5 | -100.0 | 0.0 |
| rlm+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -34.5 | -100.0 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -34.5 | -100.0 | 0.0 |
| follow_move+money_level | early | pin $50k+ | 3-1 | 75.0 | -0.9 | 13.4 | -0.5 |
| money_level+sharp_gap | early | pin $50k+ | 2-2 | 50.0 | -22.4 | -20.9 | 0.0 |
| consensus_gap+pin_value | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 80.0 | 0.0 |
| follow_move+pin_value | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 82.7 | 0.0 |
| pin_value+sharp_gap | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 82.7 | 0.0 |
| consensus_gap+follow_move | early | pin $50k+ | 1-0 | 100.0 | 34.5 | 82.0 | 0.0 |
| consensus_gap+money_level | early | pin $50k+ | 1-0 | 100.0 | 34.5 | 82.0 | 0.0 |
| consensus_gap+sharp_gap | early | pin $50k+ | 1-2 | 33.3 | -17.2 | -39.3 | 0.87 |
| money_level+pin_value | early | pin $50k+ | 1-0 | 100.0 | 34.5 | 82.0 | 0.0 |
| money_level+pin_value | early | pin limit <$10k | 2-1 | 66.7 | 16.1 | 27.8 | -0.67 |
| money_level+sharp_gap | early | pin limit <$10k | 14-6 | 70.0 | 11.4 | 18.3 | -1.19 |
| pin_value+sharp_gap | early | pin limit <$10k | 2-4 | 33.3 | -2.3 | -36.1 | 1.18 |
| follow_move+money_level | early | pin limit <$10k | 13-2 | 86.7 | 10.1 | 19.9 | -1.35 |
| follow_move+sharp_gap | early | pin limit <$10k | 6-1 | 85.7 | 8.4 | 18.9 | -0.46 |
| consensus_gap+sharp_gap | early | pin limit <$10k | 3-8 | 27.3 | -4.1 | -52.6 | 0.04 |
| follow_move+money_moving | early | pin limit <$10k | 4-1 | 80.0 | 3.4 | 20.3 | -0.62 |
| money_level+money_moving | early | pin limit <$10k | 6-2 | 75.0 | 8.2 | 23.7 | -0.51 |
| consensus_gap+follow_move | early | pin limit <$10k | 2-0 | 100.0 | 20.7 | 46.8 | -0.35 |
| consensus_gap+money_level | early | pin limit <$10k | 2-1 | 66.7 | 6.9 | -2.2 | -3.77 |
| consensus_gap+pin_value | early | pin limit <$10k | 0-4 | 0.0 | -20.7 | -100.0 | 2.38 |
| money_moving+sharp_gap | early | pin limit <$10k | 3-2 | 60.0 | 6.9 | 5.4 | 0.28 |
| consensus_gap+pin_rlm | early | pin limit <$10k | 0-2 | 0.0 | -20.7 | -100.0 | -4.4 |
| money_level+pin_rlm | early | pin limit <$10k | 0-1 | 0.0 | -20.7 | -100.0 | -10.6 |
| pin_rlm+sharp_gap | early | pin limit <$10k | 0-2 | 0.0 | -20.7 | -100.0 | -4.4 |
| money_moving+pin_value | early | pin limit <$10k | 1-1 | 50.0 | 15.5 | -3.7 | 2.5 |
| consensus_gap+money_moving | early | pin limit <$10k | 0-1 | 0.0 | -20.7 | -100.0 | 5.0 |
| pin_rlm+pin_value | early | pin limit <$10k | 0-1 | 0.0 | -20.7 | -100.0 | 1.8 |
