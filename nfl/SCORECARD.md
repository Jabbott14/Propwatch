# NFL scorecard

Generated 2026-11-15 23:06 UTC. 37 graded games (3 finished games had no final score and are not graded).

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before kickoff. Break-even at -110 is 52.4%. CLV = points of
closing-line value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured on
this sample. `edge` is hit% minus that. A signal that is structurally long dogs or
unders will beat 50% in any week dogs or unders run, which is not an edge --
this sample ran **62.2% favourites** (n=37)
**51.4% overs** (n=37) and **78.4% moneyline favourites** (n=37) and **50.0% team-total overs** (n=74).

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
| pin_rlm | both | 1-3 | 25.0 | 21.6 | 3.4 | -1.92 | -48.0 | -1.47 | 75.0 | keep collecting (4/30) |
| follow_move | both | 32-17 | 65.3 | 68.6 | -3.3 | +1.05 | 2.1 | -0.29 | 26.5 | beats break-even but not its base rate -- directional bias, not signal |
| rlm | both | 1-5 | 16.7 | 52.7 | -36.0 | -4.17 | -69.5 | 0.02 | 16.7 | keep collecting (6/30) |
| rlm_ratio | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level | both | 55-30 | 64.7 | 59.1 | 5.6 | +9.58 | 11.3 | -0.63 | 20.0 | PROMOTE: beats break-even and its own base rate |
| sharp_gap | both | 48-36 | 57.1 | 50.1 | 7.0 | +4.46 | 5.3 | -0.22 | 28.6 | no edge shown yet |
| money_moving | both | 13-8 | 61.9 | 53.0 | 8.9 | +2.64 | 12.6 | -0.13 | 28.6 | keep collecting (21/30) |
| pin_value | both | 25-22 | 53.2 | 47.7 | 5.5 | -0.39 | -0.8 | 0.16 | 25.5 | no edge shown yet |
| book_lag | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | -0.75 | 50.0 | keep collecting (2/30) |
| consensus_gap | both | 14-25 | 35.9 | 31.8 | 4.1 | -10.27 | -26.3 | 0.35 | 48.7 | DROP: below break-even |
| follow_move+rlm | both | 1-5 | 16.7 | 52.7 | -36.0 | -4.17 | -69.5 | 0.02 | 16.7 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 19-7 | 73.1 | 65.9 | 7.2 | +5.02 | 19.3 | -0.35 | 19.2 | keep collecting (26/30) |
| rlm+rlm_ratio | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_value | both | 7-3 | 70.0 | 55.1 | 14.9 | +3.3 | 33.0 | -0.35 | 0.0 | keep collecting (10/30) |
| money_level+sharp_gap | both | 37-20 | 64.9 | 57.0 | 7.9 | +8.58 | 15.1 | -0.6 | 17.5 | PROMOTE: beats break-even and its own base rate |
| pin_value+sharp_gap | both | 8-5 | 61.5 | 45.5 | 16.0 | +2.13 | 16.4 | 0.43 | 23.1 | keep collecting (13/30) |
| follow_move+money_level | both | 28-11 | 71.8 | 71.4 | 0.3 | +3.86 | 9.9 | -0.71 | 25.6 | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+pin_value | both | 2-6 | 25.0 | 33.8 | -8.8 | -4.4 | -55.0 | 1.02 | 50.0 | keep collecting (8/30) |
| follow_move+pin_value | both | 4-1 | 80.0 | 57.3 | 22.7 | +2.47 | 49.3 | 0.0 | 0.0 | keep collecting (5/30) |
| consensus_gap+follow_move | both | 3-0 | 100.0 | 73.0 | 27.0 | +1.75 | 58.5 | -0.23 | 33.3 | keep collecting (3/30) |
| consensus_gap+money_level | both | 5-1 | 83.3 | 54.1 | 29.3 | +2.59 | 43.1 | -1.73 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 9-12 | 42.9 | 32.8 | 10.0 | -2.75 | -13.1 | 0.24 | 57.1 | keep collecting (21/30) |
| follow_move+money_moving | both | 6-2 | 75.0 | 67.2 | 7.8 | +1.83 | 22.8 | -0.39 | 25.0 | keep collecting (8/30) |
| money_level+money_moving | both | 8-3 | 72.7 | 62.7 | 10.1 | +2.83 | 25.7 | -0.74 | 18.2 | keep collecting (11/30) |
| money_moving+pin_value | both | 4-2 | 66.7 | 49.1 | 17.6 | +1.69 | 28.2 | 1.0 | 33.3 | keep collecting (6/30) |
| money_moving+sharp_gap | both | 6-3 | 66.7 | 50.8 | 15.9 | +2.28 | 25.4 | -0.08 | 22.2 | keep collecting (9/30) |
| book_lag+consensus_gap | both | 0-1 | 0.0 | 37.8 | -37.8 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+pin_rlm | both | 1-3 | 25.0 | 21.6 | 3.4 | -1.92 | -48.0 | -1.47 | 75.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-1 | 0.0 | 21.6 | -21.6 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | both | 1-3 | 25.0 | 21.6 | 3.4 | -1.92 | -48.0 | -1.47 | 75.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+money_level | both | 0-1 | 0.0 | 62.2 | -62.2 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+money_moving | both | 0-1 | 0.0 | 62.2 | -62.2 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+sharp_gap | both | 0-1 | 0.0 | 62.2 | -62.2 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+money_moving | both | 1-1 | 50.0 | 21.6 | 28.4 | +0.08 | 4.0 | 3.45 | 100.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 21.6 | -21.6 | -1.0 | -100.0 | 1.8 | 100.0 | keep collecting (1/30) |
| money_moving+pin_rlm | both | 1-0 | 100.0 | 21.6 | 78.4 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| money_moving+rlm | both | 0-1 | 0.0 | 37.8 | -37.8 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-3 | 25.0 | 21.6 | 3.4 | -1.92 | -48.0 | -1.47 | 75.0 | keep collecting (4/30) |
| follow_move | moneyline | 22-7 | 75.9 | 78.4 | -2.5 | +2.03 | 7.0 | -0.42 | 34.5 | keep collecting (29/30) |
| follow_move | spread | 10-9 | 52.6 | 54.5 | -1.8 | +0.03 | 0.1 | 0.05 | 15.8 | keep collecting (19/30) |
| follow_move | total | 0-1 | 0.0 | 51.4 | -51.4 | -1.0 | -100.0 | -3.0 | 0.0 | keep collecting (1/30) |
| rlm | moneyline | 0-1 | 0.0 | 78.4 | -78.4 | -1.0 | -100.0 | -0.9 | 0.0 | keep collecting (1/30) |
| rlm | spread | 1-4 | 20.0 | 47.6 | -27.6 | -3.17 | -63.3 | 0.2 | 20.0 | keep collecting (5/30) |
| rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level | moneyline | 22-6 | 78.6 | 74.3 | 4.2 | +3.29 | 11.8 | -1.23 | 32.1 | keep collecting (28/30) |
| money_level | spread | 18-10 | 64.3 | 52.6 | 11.7 | +6.63 | 23.7 | -0.3 | 7.1 | keep collecting (28/30) |
| money_level | total | 15-14 | 51.7 | 50.7 | 1.0 | -0.34 | -1.2 | -0.38 | 20.7 | keep collecting (29/30) |
| sharp_gap | moneyline | 15-13 | 53.6 | 45.9 | 7.6 | -2.55 | -9.1 | -0.13 | 46.4 | keep collecting (28/30) |
| sharp_gap | spread | 17-12 | 58.6 | 53.8 | 4.8 | +3.45 | 11.9 | -0.09 | 17.2 | keep collecting (29/30) |
| sharp_gap | total | 16-11 | 59.3 | 50.6 | 8.7 | +3.56 | 13.2 | -0.44 | 22.2 | keep collecting (27/30) |
| money_moving | moneyline | 5-2 | 71.4 | 54.1 | 17.4 | +1.1 | 15.6 | 0.33 | 57.1 | keep collecting (7/30) |
| money_moving | spread | 4-5 | 44.4 | 54.1 | -9.6 | -1.28 | -14.3 | -0.11 | 22.2 | keep collecting (9/30) |
| money_moving | total | 4-1 | 80.0 | 49.7 | 30.3 | +2.83 | 56.6 | -0.8 | 0.0 | keep collecting (5/30) |
| pin_value | moneyline | 0-6 | 0.0 | 21.6 | -21.6 | -6.0 | -100.0 | 1.68 | 83.3 | keep collecting (6/30) |
| pin_value | spread | 10-3 | 76.9 | 54.7 | 22.2 | +5.77 | 44.4 | -0.19 | 7.7 | keep collecting (13/30) |
| pin_value | total | 3-6 | 33.3 | 50.2 | -16.8 | -3.26 | -36.2 | -0.22 | 11.1 | keep collecting (9/30) |
| pin_value | tt_away | 6-4 | 60.0 | 50.0 | 10.0 | +1.11 | 11.1 | 0.0 | 30.0 | keep collecting (10/30) |
| pin_value | tt_home | 6-3 | 66.7 | 50.0 | 16.7 | +1.98 | 22.1 | 0.22 | 22.2 | keep collecting (9/30) |
| book_lag | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | -0.75 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 9-20 | 31.0 | 25.5 | 5.5 | -9.54 | -32.9 | 0.44 | 58.6 | keep collecting (29/30) |
| consensus_gap | spread | 5-5 | 50.0 | 50.0 | -0.0 | -0.73 | -7.3 | 0.1 | 20.0 | keep collecting (10/30) |
| follow_move+money_level | moneyline | 21-5 | 80.8 | 78.4 | 2.4 | +3.33 | 12.8 | -0.95 | 30.8 | keep collecting (26/30) |
| follow_move+sharp_gap | moneyline | 10-2 | 83.3 | 78.4 | 5.0 | +1.83 | 15.2 | -0.75 | 25.0 | keep collecting (12/30) |
| money_level+sharp_gap | moneyline | 11-3 | 78.6 | 70.3 | 8.3 | +1.79 | 12.8 | -1.34 | 28.6 | keep collecting (14/30) |
| consensus_gap+sharp_gap | moneyline | 7-11 | 38.9 | 27.9 | 11.0 | -3.44 | -19.1 | 0.26 | 61.1 | keep collecting (18/30) |
| follow_move+money_moving | moneyline | 4-0 | 100.0 | 78.4 | 21.6 | +2.02 | 50.4 | -0.78 | 50.0 | keep collecting (4/30) |
| money_level+money_moving | moneyline | 4-0 | 100.0 | 78.4 | 21.6 | +2.02 | 50.4 | -0.78 | 50.0 | keep collecting (4/30) |
| consensus_gap+follow_move | moneyline | 2-0 | 100.0 | 78.4 | 21.6 | +0.94 | 46.8 | -0.35 | 50.0 | keep collecting (2/30) |
| consensus_gap+money_level | moneyline | 3-1 | 75.0 | 50.0 | 25.0 | +0.9 | 22.4 | -2.6 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_value | moneyline | 0-5 | 0.0 | 21.6 | -21.6 | -5.0 | -100.0 | 1.64 | 80.0 | keep collecting (5/30) |
| consensus_gap+pin_rlm | moneyline | 1-3 | 25.0 | 21.6 | 3.4 | -1.92 | -48.0 | -1.47 | 75.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 21.6 | -21.6 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | moneyline | 1-3 | 25.0 | 21.6 | 3.4 | -1.92 | -48.0 | -1.47 | 75.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | moneyline | 2-1 | 66.7 | 40.5 | 26.1 | +0.47 | 15.7 | 1.1 | 66.7 | keep collecting (3/30) |
| pin_value+sharp_gap | moneyline | 0-3 | 0.0 | 21.6 | -21.6 | -3.0 | -100.0 | 3.03 | 100.0 | keep collecting (3/30) |
| consensus_gap+money_moving | moneyline | 1-1 | 50.0 | 21.6 | 28.4 | +0.08 | 4.0 | 3.45 | 100.0 | keep collecting (2/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 21.6 | -21.6 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 21.6 | -21.6 | -1.0 | -100.0 | 1.8 | 100.0 | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 1-0 | 100.0 | 21.6 | 78.4 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| follow_move+rlm | moneyline | 0-1 | 0.0 | 78.4 | -78.4 | -1.0 | -100.0 | -0.9 | 0.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm | spread | 1-4 | 20.0 | 47.6 | -27.6 | -3.17 | -63.3 | 0.2 | 20.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 9-5 | 64.3 | 55.2 | 9.1 | +3.19 | 22.8 | 0.0 | 14.3 | keep collecting (14/30) |
| rlm+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+pin_value | spread | 2-1 | 66.7 | 54.1 | 12.6 | +0.6 | 20.0 | 0.0 | 0.0 | keep collecting (3/30) |
| money_level+sharp_gap | spread | 14-8 | 63.6 | 54.4 | 9.2 | +4.83 | 21.9 | -0.25 | 9.1 | keep collecting (22/30) |
| follow_move+pin_value | spread | 4-1 | 80.0 | 57.3 | 22.7 | +2.47 | 49.3 | 0.0 | 0.0 | keep collecting (5/30) |
| pin_value+sharp_gap | spread | 6-0 | 100.0 | 54.1 | 45.9 | +5.29 | 88.2 | -0.25 | 0.0 | keep collecting (6/30) |
| consensus_gap+follow_move | spread | 1-0 | 100.0 | 62.2 | 37.8 | +0.82 | 82.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 2-0 | 100.0 | 62.2 | 37.8 | +1.69 | 84.5 | 0.0 | 0.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | spread | 2-1 | 66.7 | 62.2 | 4.5 | +0.69 | 23.0 | 0.17 | 33.3 | keep collecting (3/30) |
| follow_move+money_level | spread | 7-5 | 58.3 | 58.1 | 0.2 | +1.53 | 12.7 | 0.0 | 16.7 | keep collecting (12/30) |
| money_level+pin_value | spread | 5-1 | 83.3 | 58.1 | 25.2 | +3.46 | 57.7 | -0.25 | 0.0 | keep collecting (6/30) |
| follow_move+money_moving | spread | 2-2 | 50.0 | 56.1 | -6.1 | -0.19 | -4.7 | 0.0 | 0.0 | keep collecting (4/30) |
| money_level+money_moving | spread | 2-2 | 50.0 | 56.1 | -6.1 | -0.07 | -1.7 | -1.0 | 0.0 | keep collecting (4/30) |
| money_moving+pin_value | spread | 3-1 | 75.0 | 56.1 | 18.9 | +1.76 | 44.1 | 0.25 | 25.0 | keep collecting (4/30) |
| money_moving+sharp_gap | spread | 1-2 | 33.3 | 62.2 | -28.8 | -1.02 | -34.0 | -0.67 | 0.0 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 37.8 | -37.8 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| book_lag+money_level | spread | 0-1 | 0.0 | 62.2 | -62.2 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+money_moving | spread | 0-1 | 0.0 | 62.2 | -62.2 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+sharp_gap | spread | 0-1 | 0.0 | 62.2 | -62.2 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm | spread | 0-1 | 0.0 | 37.8 | -37.8 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 2-2 | 50.0 | 50.7 | -0.7 | -0.16 | -4.1 | -0.5 | 0.0 | keep collecting (4/30) |
| money_level+sharp_gap | total | 12-9 | 57.1 | 50.8 | 6.3 | +1.96 | 9.4 | -0.48 | 19.0 | keep collecting (21/30) |
| pin_value+sharp_gap | total | 2-2 | 50.0 | 50.7 | -0.7 | -0.16 | -4.1 | -0.5 | 0.0 | keep collecting (4/30) |
| follow_move+money_level | total | 0-1 | 0.0 | 51.4 | -51.4 | -1.0 | -100.0 | -3.0 | 0.0 | redundant -- identical record to follow_move alone, not independent confirmation |
| money_level+money_moving | total | 2-1 | 66.7 | 50.5 | 16.2 | +0.88 | 29.3 | -0.33 | 0.0 | keep collecting (3/30) |
| money_moving+sharp_gap | total | 3-0 | 100.0 | 49.5 | 50.5 | +2.83 | 94.3 | -0.67 | 0.0 | keep collecting (3/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 48.6 | 51.4 | +0.93 | 92.6 | 0.0 | 0.0 | keep collecting (1/30) |

## CLOSE

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 5-9 | 35.7 | 33.4 | 2.3 | -4.07 | -29.1 |  |  | keep collecting (14/30) |
| follow_move | both | 62-50 | 55.4 | 60.3 | -5.0 | -7.85 | -7.0 |  |  | no edge shown yet |
| rlm | both | 4-15 | 21.1 | 50.5 | -29.4 | -11.44 | -60.2 |  |  | keep collecting (19/30) |
| rlm_ratio | both | 3-7 | 30.0 | 51.1 | -21.1 | -4.31 | -43.1 |  |  | keep collecting (10/30) |
| money_level | both | 71-38 | 65.1 | 59.9 | 5.3 | +14.1 | 12.9 |  |  | PROMOTE: beats break-even and its own base rate |
| sharp_gap | both | 47-60 | 43.9 | 48.8 | -4.8 | -20.55 | -19.2 |  |  | DROP: below break-even |
| money_moving | both | 33-48 | 40.7 | 44.3 | -3.6 | -19.93 | -24.6 |  |  | DROP: below break-even |
| pin_value | both | 51-39 | 56.7 | 48.7 | 8.0 | +4.43 | 4.9 |  |  | no edge shown yet |
| book_lag | both | 4-0 | 100.0 | 56.1 | 43.9 | +3.29 | 82.4 |  |  | keep collecting (4/30) |
| consensus_gap | both | 17-28 | 37.8 | 31.7 | 6.1 | -9.57 | -21.3 |  |  | DROP: below break-even |
| follow_move+rlm | both | 4-15 | 21.1 | 50.5 | -29.4 | -11.44 | -60.2 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | both | 3-7 | 30.0 | 51.1 | -21.1 | -4.31 | -43.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 23-22 | 51.1 | 60.4 | -9.2 | -7.0 | -15.6 |  |  | no edge shown yet |
| money_level+pin_value | both | 12-6 | 66.7 | 55.6 | 11.1 | +4.26 | 23.7 |  |  | keep collecting (18/30) |
| rlm+rlm_ratio | both | 3-7 | 30.0 | 51.1 | -21.1 | -4.31 | -43.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 3-12 | 20.0 | 48.1 | -28.1 | -9.31 | -62.1 |  |  | keep collecting (15/30) |
| rlm_ratio+sharp_gap | both | 3-7 | 30.0 | 51.1 | -21.1 | -4.31 | -43.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 33-24 | 57.9 | 57.9 | 0.0 | +0.45 | 0.8 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 7-1 | 87.5 | 55.1 | 32.4 | +4.86 | 60.7 |  |  | keep collecting (8/30) |
| follow_move+money_level | both | 40-16 | 71.4 | 69.2 | 2.2 | +7.19 | 12.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+sharp_gap | both | 8-12 | 40.0 | 31.8 | 8.2 | -2.75 | -13.7 |  |  | keep collecting (20/30) |
| follow_move+pin_value | both | 8-3 | 72.7 | 56.9 | 15.8 | +3.61 | 32.8 |  |  | keep collecting (11/30) |
| pin_value+rlm | both | 2-2 | 50.0 | 52.7 | -2.7 | -0.26 | -6.5 |  |  | keep collecting (4/30) |
| pin_value+sharp_gap | both | 12-11 | 52.2 | 45.9 | 6.2 | -1.11 | -4.8 |  |  | keep collecting (23/30) |
| consensus_gap+pin_value | both | 3-6 | 33.3 | 25.2 | 8.1 | -3.42 | -38.0 |  |  | keep collecting (9/30) |
| book_lag+consensus_gap | both | 3-0 | 100.0 | 54.1 | 45.9 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| book_lag+money_moving | both | 1-0 | 100.0 | 37.8 | 62.2 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | both | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | both | 6-12 | 33.3 | 25.7 | 7.7 | -5.63 | -31.3 |  |  | keep collecting (18/30) |
| money_moving+pin_value | both | 10-10 | 50.0 | 44.5 | 5.5 | -1.66 | -8.3 |  |  | keep collecting (20/30) |
| money_moving+sharp_gap | both | 22-35 | 38.6 | 44.2 | -5.6 | -15.77 | -27.7 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 3-1 | 75.0 | 74.3 | 0.7 | +0.54 | 13.4 |  |  | keep collecting (4/30) |
| money_level+money_moving | both | 21-12 | 63.6 | 56.0 | 7.6 | +4.83 | 14.6 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 2-5 | 28.6 | 21.6 | 6.9 | -2.76 | -39.4 |  |  | keep collecting (7/30) |
| money_level+pin_rlm | both | 0-3 | 0.0 | 40.5 | -40.5 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | both | 5-9 | 35.7 | 33.4 | 2.3 | -4.07 | -29.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 5-9 | 35.7 | 33.4 | 2.3 | -4.07 | -29.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+money_moving | both | 13-16 | 44.8 | 56.8 | -11.9 | -6.84 | -23.6 |  |  | keep collecting (29/30) |
| follow_move+pin_rlm | both | 3-3 | 50.0 | 49.1 | 0.9 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| money_moving+rlm | both | 3-10 | 23.1 | 47.6 | -24.5 | -7.31 | -56.2 |  |  | keep collecting (13/30) |
| money_moving+rlm_ratio | both | 3-4 | 42.9 | 47.5 | -4.6 | -1.31 | -18.7 |  |  | keep collecting (7/30) |
| pin_rlm+pin_value | both | 1-3 | 25.0 | 35.1 | -10.1 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| pin_rlm+rlm | both | 3-3 | 50.0 | 49.1 | 0.9 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| pin_rlm+rlm_ratio | both | 3-3 | 50.0 | 49.1 | 0.9 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| pin_value+rlm_ratio | both | 1-1 | 50.0 | 48.6 | 1.4 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| money_level+rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+rlm | both | 0-1 | 0.0 | 62.2 | -62.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| book_lag+money_level | both | 1-0 | 100.0 | 62.2 | 37.8 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 2-6 | 25.0 | 21.6 | 3.4 | -3.76 | -47.0 |  |  | keep collecting (8/30) |
| pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm | total | 3-1 | 75.0 | 48.6 | 26.4 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| follow_move | moneyline | 28-8 | 77.8 | 78.4 | -0.6 | +3.6 | 10.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 13-18 | 41.9 | 54.3 | -12.4 | -6.01 | -19.4 |  |  | no edge shown yet |
| follow_move | total | 7-8 | 46.7 | 50.1 | -3.4 | -1.62 | -10.8 |  |  | keep collecting (15/30) |
| follow_move | tt_away | 8-7 | 53.3 | 50.0 | 3.3 | -0.0 | -0.0 |  |  | keep collecting (15/30) |
| follow_move | tt_home | 6-9 | 40.0 | 50.0 | -10.0 | -3.81 | -25.4 |  |  | keep collecting (15/30) |
| rlm | moneyline | 0-1 | 0.0 | 78.4 | -78.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm | spread | 1-10 | 9.1 | 48.9 | -39.8 | -9.13 | -83.0 |  |  | keep collecting (11/30) |
| rlm | total | 3-4 | 42.9 | 49.0 | -6.2 | -1.31 | -18.7 |  |  | keep collecting (7/30) |
| rlm_ratio | moneyline | 0-1 | 0.0 | 78.4 | -78.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_ratio | spread | 0-5 | 0.0 | 47.6 | -47.6 | -5.0 | -100.0 |  |  | keep collecting (5/30) |
| rlm_ratio | total | 3-1 | 75.0 | 48.6 | 26.4 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| money_level | moneyline | 30-6 | 83.3 | 73.6 | 9.7 | +8.68 | 24.1 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level | spread | 22-15 | 59.5 | 54.9 | 4.5 | +4.94 | 13.4 |  |  | no edge shown yet |
| money_level | total | 19-17 | 52.8 | 51.1 | 1.7 | +0.48 | 1.3 |  |  | no edge shown yet |
| sharp_gap | moneyline | 18-16 | 52.9 | 51.7 | 1.3 | -2.56 | -7.5 |  |  | no edge shown yet |
| sharp_gap | spread | 14-22 | 38.9 | 44.6 | -5.7 | -9.6 | -26.7 |  |  | DROP: below break-even |
| sharp_gap | total | 15-22 | 40.5 | 50.2 | -9.6 | -8.4 | -22.7 |  |  | no edge shown yet |
| money_moving | moneyline | 11-16 | 40.7 | 38.4 | 2.3 | -7.76 | -28.7 |  |  | keep collecting (27/30) |
| money_moving | spread | 9-17 | 34.6 | 44.4 | -9.8 | -9.0 | -34.6 |  |  | keep collecting (26/30) |
| money_moving | total | 13-15 | 46.4 | 50.0 | -3.6 | -3.18 | -11.4 |  |  | keep collecting (28/30) |
| pin_value | moneyline | 2-6 | 25.0 | 28.7 | -3.7 | -4.59 | -57.4 |  |  | keep collecting (8/30) |
| pin_value | spread | 13-3 | 81.2 | 53.0 | 28.2 | +8.3 | 51.9 |  |  | keep collecting (16/30) |
| pin_value | total | 9-9 | 50.0 | 50.2 | -0.2 | -1.21 | -6.7 |  |  | keep collecting (18/30) |
| pin_value | tt_away | 12-11 | 52.2 | 50.0 | 2.2 | -0.8 | -3.5 |  |  | keep collecting (23/30) |
| pin_value | tt_home | 15-10 | 60.0 | 50.0 | 10.0 | +2.73 | 10.9 |  |  | keep collecting (25/30) |
| book_lag | spread | 4-0 | 100.0 | 56.1 | 43.9 | +3.29 | 82.4 |  |  | keep collecting (4/30) |
| consensus_gap | moneyline | 12-25 | 32.4 | 27.8 | 4.7 | -10.7 | -28.9 |  |  | DROP: below break-even |
| consensus_gap | spread | 5-3 | 62.5 | 50.0 | 12.5 | +1.13 | 14.1 |  |  | keep collecting (8/30) |
| consensus_gap+money_level | moneyline | 6-1 | 85.7 | 54.1 | 31.7 | +4.02 | 57.5 |  |  | keep collecting (7/30) |
| follow_move+rlm | moneyline | 0-1 | 0.0 | 78.4 | -78.4 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 0-1 | 0.0 | 78.4 | -78.4 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 13-4 | 76.5 | 78.4 | -1.9 | +1.92 | 11.3 |  |  | keep collecting (17/30) |
| rlm+rlm_ratio | moneyline | 0-1 | 0.0 | 78.4 | -78.4 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+sharp_gap | moneyline | 0-1 | 0.0 | 78.4 | -78.4 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 0-1 | 0.0 | 78.4 | -78.4 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+sharp_gap | moneyline | 7-11 | 38.9 | 31.1 | 7.8 | -2.58 | -14.3 |  |  | keep collecting (18/30) |
| follow_move+money_level | moneyline | 27-5 | 84.4 | 78.4 | 6.0 | +6.19 | 19.4 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+sharp_gap | moneyline | 15-4 | 78.9 | 72.4 | 6.5 | +4.3 | 22.6 |  |  | keep collecting (19/30) |
| consensus_gap+pin_value | moneyline | 1-6 | 14.3 | 21.6 | -7.3 | -5.04 | -72.0 |  |  | keep collecting (7/30) |
| pin_value+sharp_gap | moneyline | 1-4 | 20.0 | 33.0 | -13.0 | -3.56 | -71.1 |  |  | keep collecting (5/30) |
| consensus_gap+follow_move | moneyline | 3-0 | 100.0 | 78.4 | 21.6 | +1.54 | 51.2 |  |  | keep collecting (3/30) |
| consensus_gap+money_moving | moneyline | 5-12 | 29.4 | 25.0 | 4.5 | -6.41 | -37.7 |  |  | keep collecting (17/30) |
| money_moving+pin_value | moneyline | 2-4 | 33.3 | 31.1 | 2.3 | -2.59 | -43.2 |  |  | keep collecting (6/30) |
| consensus_gap+pin_rlm | moneyline | 2-5 | 28.6 | 21.6 | 6.9 | -2.76 | -39.4 |  |  | keep collecting (7/30) |
| money_level+money_moving | moneyline | 8-2 | 80.0 | 67.0 | 13.0 | +3.04 | 30.4 |  |  | keep collecting (10/30) |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 21.6 | -21.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 2-6 | 25.0 | 21.6 | 3.4 | -3.76 | -47.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | moneyline | 8-10 | 44.4 | 40.5 | 3.9 | -3.4 | -18.9 |  |  | keep collecting (18/30) |
| pin_rlm+sharp_gap | moneyline | 2-6 | 25.0 | 21.6 | 3.4 | -3.76 | -47.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+money_moving | moneyline | 6-1 | 85.7 | 78.4 | 7.3 | +1.66 | 23.7 |  |  | keep collecting (7/30) |
| pin_rlm+pin_value | moneyline | 0-2 | 0.0 | 21.6 | -21.6 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| follow_move+pin_value | moneyline | 1-0 | 100.0 | 78.4 | 21.6 | +0.44 | 44.4 |  |  | keep collecting (1/30) |
| money_level+pin_value | moneyline | 1-0 | 100.0 | 78.4 | 21.6 | +0.44 | 44.4 |  |  | keep collecting (1/30) |
| follow_move+rlm | spread | 1-10 | 9.1 | 48.9 | -39.8 | -9.13 | -83.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-5 | 0.0 | 47.6 | -47.6 | -5.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 6-11 | 35.3 | 49.3 | -14.0 | -5.52 | -32.4 |  |  | keep collecting (17/30) |
| money_level+pin_value | spread | 7-2 | 77.8 | 56.8 | 21.0 | +4.31 | 47.9 |  |  | keep collecting (9/30) |
| rlm+rlm_ratio | spread | 0-5 | 0.0 | 47.6 | -47.6 | -5.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 0-8 | 0.0 | 43.9 | -43.9 | -8.0 | -100.0 |  |  | keep collecting (8/30) |
| rlm_ratio+sharp_gap | spread | 0-5 | 0.0 | 47.6 | -47.6 | -5.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 9-8 | 52.9 | 59.3 | -6.4 | +0.31 | 1.8 |  |  | keep collecting (17/30) |
| follow_move+pin_value | spread | 5-1 | 83.3 | 58.1 | 25.2 | +3.41 | 56.9 |  |  | keep collecting (6/30) |
| pin_value+rlm | spread | 1-0 | 100.0 | 62.2 | 37.8 | +0.87 | 87.0 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | spread | 8-8 | 50.0 | 50.0 | 0.0 | -0.92 | -5.8 |  |  | keep collecting (16/30) |
| consensus_gap+sharp_gap | spread | 1-1 | 50.0 | 37.8 | 12.2 | -0.17 | -8.4 |  |  | keep collecting (2/30) |
| book_lag+consensus_gap | spread | 3-0 | 100.0 | 54.1 | 45.9 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| pin_value+sharp_gap | spread | 6-1 | 85.7 | 48.3 | 37.5 | +4.13 | 59.1 |  |  | keep collecting (7/30) |
| book_lag+money_moving | spread | 1-0 | 100.0 | 37.8 | 62.2 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | spread | 1-0 | 100.0 | 37.8 | 62.2 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| consensus_gap+pin_value | spread | 2-0 | 100.0 | 37.8 | 62.2 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| money_moving+pin_value | spread | 4-0 | 100.0 | 50.0 | 50.0 | +3.43 | 85.8 |  |  | keep collecting (4/30) |
| money_level+money_moving | spread | 6-5 | 54.5 | 51.1 | 3.4 | +0.39 | 3.6 |  |  | keep collecting (11/30) |
| money_moving+sharp_gap | spread | 6-13 | 31.6 | 41.7 | -10.1 | -7.55 | -39.8 |  |  | keep collecting (19/30) |
| follow_move+money_moving | spread | 2-8 | 20.0 | 50.0 | -30.0 | -6.09 | -60.9 |  |  | keep collecting (10/30) |
| money_moving+rlm | spread | 0-6 | 0.0 | 45.9 | -45.9 | -6.0 | -100.0 |  |  | keep collecting (6/30) |
| follow_move+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_moving+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-3 | 0.0 | 45.9 | -45.9 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_rlm+rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+follow_move | spread | 0-1 | 0.0 | 62.2 | -62.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+rlm | spread | 0-1 | 0.0 | 62.2 | -62.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| book_lag+money_level | spread | 1-0 | 100.0 | 62.2 | 37.8 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| consensus_gap+money_level | spread | 1-0 | 100.0 | 62.2 | 37.8 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | total | 10-12 | 45.5 | 51.1 | -5.7 | -2.93 | -13.3 |  |  | keep collecting (22/30) |
| pin_value+sharp_gap | total | 5-6 | 45.5 | 50.4 | -4.9 | -1.69 | -15.3 |  |  | keep collecting (11/30) |
| money_level+pin_value | total | 4-4 | 50.0 | 51.4 | -1.4 | -0.49 | -6.2 |  |  | keep collecting (8/30) |
| money_moving+sharp_gap | total | 8-12 | 40.0 | 50.0 | -10.0 | -4.82 | -24.1 |  |  | keep collecting (20/30) |
| money_level+money_moving | total | 7-5 | 58.3 | 51.4 | 7.0 | +1.4 | 11.7 |  |  | keep collecting (12/30) |
| money_moving+pin_value | total | 4-6 | 40.0 | 50.3 | -10.3 | -2.5 | -25.0 |  |  | keep collecting (10/30) |
| follow_move+money_moving | total | 5-7 | 41.7 | 49.8 | -8.1 | -2.4 | -20.0 |  |  | keep collecting (12/30) |
| follow_move+pin_rlm | total | 3-1 | 75.0 | 48.6 | 26.4 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+pin_value | total | 1-2 | 33.3 | 49.5 | -16.2 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| follow_move+rlm | total | 3-4 | 42.9 | 49.0 | -6.2 | -1.31 | -18.7 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | total | 3-1 | 75.0 | 48.6 | 26.4 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 4-7 | 36.4 | 49.6 | -13.3 | -3.4 | -30.9 |  |  | keep collecting (11/30) |
| money_moving+pin_rlm | total | 3-1 | 75.0 | 48.6 | 26.4 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm | total | 3-4 | 42.9 | 49.0 | -6.2 | -1.31 | -18.7 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| money_moving+rlm_ratio | total | 3-1 | 75.0 | 48.6 | 26.4 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+pin_value | total | 1-1 | 50.0 | 48.6 | 1.4 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| pin_rlm+rlm | total | 3-1 | 75.0 | 48.6 | 26.4 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | total | 3-1 | 75.0 | 48.6 | 26.4 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | total | 3-1 | 75.0 | 48.6 | 26.4 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm | total | 1-2 | 33.3 | 49.5 | -16.2 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| pin_value+rlm_ratio | total | 1-1 | 50.0 | 48.6 | 1.4 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| rlm+rlm_ratio | total | 3-1 | 75.0 | 48.6 | 26.4 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | total | 3-3 | 50.0 | 48.6 | 1.4 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| rlm_ratio+sharp_gap | total | 3-1 | 75.0 | 48.6 | 26.4 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | total | 4-3 | 57.1 | 51.4 | 5.8 | +0.69 | 9.8 |  |  | keep collecting (7/30) |
| follow_move+pin_value | tt_home | 1-0 | 100.0 | 50.0 | 50.0 | +0.89 | 88.5 |  |  | keep collecting (1/30) |

## By ticket volume and Pinnacle limit (both markets)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_rlm | close | 40k+ bets | 5-9 | 35.7 | 2.3 | -29.1 |  |
| pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 16.8 | 13.8 |  |
| pin_rlm | close | pin $50k+ | 2-7 | 22.2 | -5.7 | -52.9 |  |
| follow_move | close | 40k+ bets | 62-50 | 55.4 | -5.0 | -7.0 |  |
| follow_move | close | pin $10-50k | 12-8 | 60.0 | 1.5 | -4.8 |  |
| follow_move | close | pin $50k+ | 36-26 | 58.1 | -7.8 | -5.0 |  |
| follow_move | close | pin limit <$10k | 14-16 | 46.7 | -3.3 | -12.7 |  |
| rlm | close | 40k+ bets | 4-15 | 21.1 | -29.4 | -60.2 |  |
| rlm | close | pin $10-50k | 3-4 | 42.9 | -6.2 | -18.7 |  |
| rlm | close | pin $50k+ | 1-11 | 8.3 | -43.0 | -84.4 |  |
| rlm_ratio | close | 40k+ bets | 3-7 | 30.0 | -21.1 | -43.1 |  |
| rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 26.4 | 42.2 |  |
| rlm_ratio | close | pin $50k+ | 0-6 | 0.0 | -52.7 | -100.0 |  |
| money_level | close | 40k+ bets | 71-38 | 65.1 | 5.3 | 12.9 |  |
| money_level | close | pin $10-50k | 23-17 | 57.5 | 2.3 | 0.6 |  |
| money_level | close | pin $50k+ | 48-21 | 69.6 | 7.0 | 20.1 |  |
| sharp_gap | close | 40k+ bets | 47-60 | 43.9 | -4.8 | -19.2 |  |
| sharp_gap | close | pin $10-50k | 16-23 | 41.0 | -10.5 | -26.4 |  |
| sharp_gap | close | pin $50k+ | 31-37 | 45.6 | -1.6 | -15.1 |  |
| money_moving | close | 40k+ bets | 33-48 | 40.7 | -3.6 | -24.6 |  |
| money_moving | close | pin $10-50k | 13-18 | 41.9 | -7.1 | -23.3 |  |
| money_moving | close | pin $50k+ | 20-30 | 40.0 | -1.5 | -25.4 |  |
| pin_value | close | 40k+ bets | 51-39 | 56.7 | 8.0 | 4.9 |  |
| pin_value | close | pin $10-50k | 9-11 | 45.0 | -2.3 | -16.0 |  |
| pin_value | close | pin $50k+ | 15-7 | 68.2 | 21.1 | 25.9 |  |
| pin_value | close | pin limit <$10k | 27-21 | 56.2 | 6.2 | 4.0 |  |
| book_lag | close | 40k+ bets | 4-0 | 100.0 | 43.9 | 82.4 |  |
| book_lag | close | pin $50k+ | 4-0 | 100.0 | 43.9 | 82.4 |  |
| consensus_gap | close | 40k+ bets | 17-28 | 37.8 | 6.1 | -21.3 |  |
| consensus_gap | close | pin $10-50k | 1-5 | 16.7 | -14.4 | -78.6 |  |
| consensus_gap | close | pin $50k+ | 16-23 | 41.0 | 9.2 | -12.4 |  |
| follow_move+rlm | close | 40k+ bets | 4-15 | 21.1 | -29.4 | -60.2 |  |
| follow_move+rlm_ratio | close | 40k+ bets | 3-7 | 30.0 | -21.1 | -43.1 |  |
| follow_move+sharp_gap | close | 40k+ bets | 23-22 | 51.1 | -9.2 | -15.6 |  |
| money_level+pin_value | close | 40k+ bets | 12-6 | 66.7 | 11.1 | 23.7 |  |
| rlm+rlm_ratio | close | 40k+ bets | 3-7 | 30.0 | -21.1 | -43.1 |  |
| rlm+sharp_gap | close | 40k+ bets | 3-12 | 20.0 | -28.1 | -62.1 |  |
| rlm_ratio+sharp_gap | close | 40k+ bets | 3-7 | 30.0 | -21.1 | -43.1 |  |
| money_level+sharp_gap | close | 40k+ bets | 33-24 | 57.9 | 0.0 | 0.8 |  |
| consensus_gap+money_level | close | 40k+ bets | 7-1 | 87.5 | 32.4 | 60.7 |  |
| follow_move+money_level | close | 40k+ bets | 40-16 | 71.4 | 2.2 | 12.8 |  |
| consensus_gap+sharp_gap | close | 40k+ bets | 8-12 | 40.0 | 8.2 | -13.7 |  |
| follow_move+pin_value | close | 40k+ bets | 8-3 | 72.7 | 15.8 | 32.8 |  |
| pin_value+rlm | close | 40k+ bets | 2-2 | 50.0 | -2.7 | -6.5 |  |
| pin_value+sharp_gap | close | 40k+ bets | 12-11 | 52.2 | 6.2 | -4.8 |  |
| consensus_gap+pin_value | close | 40k+ bets | 3-6 | 33.3 | 8.1 | -38.0 |  |
| book_lag+consensus_gap | close | 40k+ bets | 3-0 | 100.0 | 45.9 | 82.0 |  |
| book_lag+money_moving | close | 40k+ bets | 1-0 | 100.0 | 62.2 | 78.1 |  |
| book_lag+pin_value | close | 40k+ bets | 2-0 | 100.0 | 50.0 | 80.7 |  |
| consensus_gap+money_moving | close | 40k+ bets | 6-12 | 33.3 | 7.7 | -31.3 |  |
| money_moving+pin_value | close | 40k+ bets | 10-10 | 50.0 | 5.5 | -8.3 |  |
| money_moving+sharp_gap | close | 40k+ bets | 22-35 | 38.6 | -5.6 | -27.7 |  |
| consensus_gap+follow_move | close | 40k+ bets | 3-1 | 75.0 | 0.7 | 13.4 |  |
| money_level+money_moving | close | 40k+ bets | 21-12 | 63.6 | 7.6 | 14.6 |  |
| consensus_gap+pin_rlm | close | 40k+ bets | 2-5 | 28.6 | 6.9 | -39.4 |  |
| money_level+pin_rlm | close | 40k+ bets | 0-3 | 0.0 | -40.5 | -100.0 |  |
| money_moving+pin_rlm | close | 40k+ bets | 5-9 | 35.7 | 2.3 | -29.1 |  |
| pin_rlm+sharp_gap | close | 40k+ bets | 5-9 | 35.7 | 2.3 | -29.1 |  |
| follow_move+money_moving | close | 40k+ bets | 13-16 | 44.8 | -11.9 | -23.6 |  |
| follow_move+pin_rlm | close | 40k+ bets | 3-3 | 50.0 | 0.9 | -5.2 |  |
| money_moving+rlm | close | 40k+ bets | 3-10 | 23.1 | -24.5 | -56.2 |  |
| money_moving+rlm_ratio | close | 40k+ bets | 3-4 | 42.9 | -4.6 | -18.7 |  |
| pin_rlm+pin_value | close | 40k+ bets | 1-3 | 25.0 | -10.1 | -53.2 |  |
| pin_rlm+rlm | close | 40k+ bets | 3-3 | 50.0 | 0.9 | -5.2 |  |
| pin_rlm+rlm_ratio | close | 40k+ bets | 3-3 | 50.0 | 0.9 | -5.2 |  |
| pin_value+rlm_ratio | close | 40k+ bets | 1-1 | 50.0 | 1.4 | -6.5 |  |
| money_level+rlm | close | 40k+ bets | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_level+rlm_ratio | close | 40k+ bets | 0-2 | 0.0 | -50.0 | -100.0 |  |
| consensus_gap+rlm | close | 40k+ bets | 0-1 | 0.0 | -62.2 | -100.0 |  |
| book_lag+money_level | close | 40k+ bets | 1-0 | 100.0 | 37.8 | 83.3 |  |
| money_level+sharp_gap | close | pin $10-50k | 11-12 | 47.8 | -6.8 | -16.6 |  |
| pin_value+sharp_gap | close | pin $10-50k | 5-7 | 41.7 | -6.3 | -22.4 |  |
| money_level+pin_value | close | pin $10-50k | 4-4 | 50.0 | -1.4 | -6.2 |  |
| consensus_gap+pin_value | close | pin $10-50k | 0-2 | 0.0 | -21.6 | -100.0 |  |
| follow_move+money_level | close | pin $10-50k | 9-3 | 75.0 | 10.1 | 11.3 |  |
| follow_move+sharp_gap | close | pin $10-50k | 6-7 | 46.2 | -10.0 | -25.9 |  |
| money_moving+sharp_gap | close | pin $10-50k | 7-13 | 35.0 | -14.9 | -35.4 |  |
| consensus_gap+follow_move | close | pin $10-50k | 1-0 | 100.0 | 21.6 | 28.6 |  |
| consensus_gap+money_level | close | pin $10-50k | 1-0 | 100.0 | 21.6 | 28.6 |  |
| consensus_gap+sharp_gap | close | pin $10-50k | 1-1 | 50.0 | 0.0 | -35.7 |  |
| money_level+money_moving | close | pin $10-50k | 7-5 | 58.3 | 2.5 | 2.9 |  |
| money_moving+pin_value | close | pin $10-50k | 4-7 | 36.4 | -11.3 | -31.8 |  |
| follow_move+money_moving | close | pin $10-50k | 6-7 | 46.2 | -7.9 | -19.6 |  |
| follow_move+pin_rlm | close | pin $10-50k | 3-1 | 75.0 | 26.4 | 42.2 |  |
| follow_move+pin_value | close | pin $10-50k | 1-2 | 33.3 | -16.2 | -37.7 |  |
| follow_move+rlm | close | pin $10-50k | 3-4 | 42.9 | -6.2 | -18.7 |  |
| follow_move+rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 26.4 | 42.2 |  |
| money_moving+pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 16.8 | 13.8 |  |
| money_moving+rlm | close | pin $10-50k | 3-4 | 42.9 | -6.2 | -18.7 |  |
| money_moving+rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 26.4 | 42.2 |  |
| pin_rlm+pin_value | close | pin $10-50k | 1-2 | 33.3 | -6.3 | -37.7 |  |
| pin_rlm+rlm | close | pin $10-50k | 3-1 | 75.0 | 26.4 | 42.2 |  |
| pin_rlm+rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 26.4 | 42.2 |  |
| pin_rlm+sharp_gap | close | pin $10-50k | 3-2 | 60.0 | 16.8 | 13.8 |  |
| pin_value+rlm | close | pin $10-50k | 1-2 | 33.3 | -16.2 | -37.7 |  |
| pin_value+rlm_ratio | close | pin $10-50k | 1-1 | 50.0 | 1.4 | -6.5 |  |
| rlm+rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 26.4 | 42.2 |  |
| rlm+sharp_gap | close | pin $10-50k | 3-3 | 50.0 | 1.4 | -5.2 |  |
| rlm_ratio+sharp_gap | close | pin $10-50k | 3-1 | 75.0 | 26.4 | 42.2 |  |
| consensus_gap+money_moving | close | pin $10-50k | 0-2 | 0.0 | -21.6 | -100.0 |  |
| consensus_gap+pin_rlm | close | pin $10-50k | 0-1 | 0.0 | -21.6 | -100.0 |  |
| follow_move+rlm | close | pin $50k+ | 1-11 | 8.3 | -43.0 | -84.4 |  |
| follow_move+rlm_ratio | close | pin $50k+ | 0-6 | 0.0 | -52.7 | -100.0 |  |
| follow_move+sharp_gap | close | pin $50k+ | 17-15 | 53.1 | -9.0 | -11.3 |  |
| money_level+pin_value | close | pin $50k+ | 8-2 | 80.0 | 21.1 | 47.6 |  |
| rlm+rlm_ratio | close | pin $50k+ | 0-6 | 0.0 | -52.7 | -100.0 |  |
| rlm+sharp_gap | close | pin $50k+ | 0-9 | 0.0 | -47.7 | -100.0 |  |
| rlm_ratio+sharp_gap | close | pin $50k+ | 0-6 | 0.0 | -52.7 | -100.0 |  |
| consensus_gap+money_level | close | pin $50k+ | 6-1 | 85.7 | 34.0 | 65.3 |  |
| follow_move+money_level | close | pin $50k+ | 31-13 | 70.5 | 0.1 | 13.3 |  |
| consensus_gap+sharp_gap | close | pin $50k+ | 7-11 | 38.9 | 9.2 | -11.3 |  |
| follow_move+pin_value | close | pin $50k+ | 6-1 | 85.7 | 24.7 | 55.1 |  |
| pin_value+rlm | close | pin $50k+ | 1-0 | 100.0 | 37.8 | 87.0 |  |
| money_level+sharp_gap | close | pin $50k+ | 22-12 | 64.7 | 4.6 | 12.5 |  |
| consensus_gap+pin_value | close | pin $50k+ | 3-4 | 42.9 | 16.6 | -20.3 |  |
| pin_value+sharp_gap | close | pin $50k+ | 7-4 | 63.6 | 19.9 | 14.3 |  |
| book_lag+consensus_gap | close | pin $50k+ | 3-0 | 100.0 | 45.9 | 82.0 |  |
| book_lag+money_moving | close | pin $50k+ | 1-0 | 100.0 | 62.2 | 78.1 |  |
| book_lag+pin_value | close | pin $50k+ | 2-0 | 100.0 | 50.0 | 80.7 |  |
| consensus_gap+money_moving | close | pin $50k+ | 6-10 | 37.5 | 11.3 | -22.7 |  |
| money_moving+pin_value | close | pin $50k+ | 6-3 | 66.7 | 26.1 | 20.4 |  |
| consensus_gap+pin_rlm | close | pin $50k+ | 2-4 | 33.3 | 11.7 | -29.3 |  |
| money_level+money_moving | close | pin $50k+ | 14-7 | 66.7 | 10.6 | 21.4 |  |
| money_level+pin_rlm | close | pin $50k+ | 0-3 | 0.0 | -40.5 | -100.0 |  |
| money_moving+pin_rlm | close | pin $50k+ | 2-7 | 22.2 | -5.7 | -52.9 |  |
| money_moving+sharp_gap | close | pin $50k+ | 15-22 | 40.5 | -0.7 | -23.5 |  |
| pin_rlm+sharp_gap | close | pin $50k+ | 2-7 | 22.2 | -5.7 | -52.9 |  |
| follow_move+money_moving | close | pin $50k+ | 7-9 | 43.8 | -15.2 | -26.8 |  |
| pin_rlm+pin_value | close | pin $50k+ | 0-1 | 0.0 | -21.6 | -100.0 |  |
| consensus_gap+follow_move | close | pin $50k+ | 2-1 | 66.7 | -6.3 | 8.4 |  |
| money_moving+rlm | close | pin $50k+ | 0-6 | 0.0 | -45.9 | -100.0 |  |
| follow_move+pin_rlm | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_level+rlm | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_level+rlm_ratio | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_moving+rlm_ratio | close | pin $50k+ | 0-3 | 0.0 | -45.9 | -100.0 |  |
| pin_rlm+rlm | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| pin_rlm+rlm_ratio | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| consensus_gap+rlm | close | pin $50k+ | 0-1 | 0.0 | -62.2 | -100.0 |  |
| book_lag+money_level | close | pin $50k+ | 1-0 | 100.0 | 37.8 | 83.3 |  |
| follow_move+pin_value | close | pin limit <$10k | 1-0 | 100.0 | 50.0 | 88.5 |  |
| pin_rlm | early | <10k bets | 1-3 | 25.0 | 3.4 | -48.0 | -1.47 |
| pin_rlm | early | pin $10-50k | 1-0 | 100.0 | 78.4 | 108.0 | 1.9 |
| pin_rlm | early | pin limit <$10k | 0-3 | 0.0 | -21.6 | -100.0 | -2.6 |
| follow_move | early | 10-40k bets | 2-1 | 66.7 | -6.3 | 6.3 | -0.4 |
| follow_move | early | 40k+ bets | 3-2 | 60.0 | -2.2 | -10.9 | -0.1 |
| follow_move | early | <10k bets | 27-14 | 65.9 | -3.2 | 3.4 | -0.3 |
| follow_move | early | pin $10-50k | 7-5 | 58.3 | -1.8 | 5.8 | 0.14 |
| follow_move | early | pin $50k+ | 4-2 | 66.7 | 4.5 | 6.1 | -0.33 |
| follow_move | early | pin limit <$10k | 20-7 | 74.1 | -0.3 | 10.2 | -0.13 |
| rlm | early | 40k+ bets | 0-1 | 0.0 | -37.8 | -100.0 | 0.0 |
| rlm | early | <10k bets | 1-4 | 20.0 | -35.7 | -63.3 | 0.02 |
| rlm | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.5 |
| rlm | early | pin $50k+ | 0-1 | 0.0 | -37.8 | -100.0 | 0.0 |
| rlm | early | pin limit <$10k | 0-2 | 0.0 | -70.3 | -100.0 | -0.45 |
| rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -37.8 | -100.0 | 0.0 |
| rlm_ratio | early | <10k bets | 1-0 | 100.0 | 37.8 | 83.3 | 0.0 |
| rlm_ratio | early | pin $10-50k | 1-0 | 100.0 | 37.8 | 83.3 | 0.0 |
| rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -37.8 | -100.0 | 0.0 |
| money_level | early | 10-40k bets | 3-3 | 50.0 | -9.5 | -13.8 | -0.28 |
| money_level | early | 40k+ bets | 4-4 | 50.0 | -13.9 | -19.9 | -0.06 |
| money_level | early | <10k bets | 48-23 | 67.6 | 9.1 | 16.9 | -0.73 |
| money_level | early | pin $10-50k | 12-11 | 52.2 | -1.6 | -2.3 | -0.23 |
| money_level | early | pin $50k+ | 5-2 | 71.4 | 5.8 | 20.1 | -0.36 |
| money_level | early | pin limit <$10k | 36-13 | 73.5 | 13.4 | 23.5 | -0.77 |
| sharp_gap | early | 10-40k bets | 3-3 | 50.0 | 5.0 | 3.1 | 0.27 |
| sharp_gap | early | 40k+ bets | 4-5 | 44.4 | -13.8 | -29.5 | -0.06 |
| sharp_gap | early | <10k bets | 41-28 | 59.4 | 9.9 | 10.0 | -0.28 |
| sharp_gap | early | pin $10-50k | 13-10 | 56.5 | 4.5 | 8.3 | 0.06 |
| sharp_gap | early | pin $50k+ | 3-5 | 37.5 | -17.6 | -37.5 | 0.33 |
| sharp_gap | early | pin limit <$10k | 28-19 | 59.6 | 11.7 | 7.6 | -0.61 |
| money_moving | early | <10k bets | 13-8 | 61.9 | 8.9 | 12.6 | -0.13 |
| money_moving | early | pin $10-50k | 5-2 | 71.4 | 22.0 | 40.0 | -0.16 |
| money_moving | early | pin limit <$10k | 7-5 | 58.3 | 1.6 | -0.9 | 0.03 |
| pin_value | early | 10-40k bets | 1-2 | 33.3 | -20.7 | -39.3 | 0.0 |
| pin_value | early | 40k+ bets | 4-2 | 66.7 | 20.5 | 22.5 | 0.0 |
| pin_value | early | <10k bets | 20-18 | 52.6 | 5.2 | -1.5 | 0.2 |
| pin_value | early | pin $10-50k | 6-3 | 66.7 | 8.4 | 27.8 | -0.28 |
| pin_value | early | pin $50k+ | 3-0 | 100.0 | 54.1 | 81.1 | 0.0 |
| pin_value | early | pin limit <$10k | 16-19 | 45.7 | 0.6 | -15.2 | 0.29 |
| book_lag | early | <10k bets | 0-2 | 0.0 | -50.0 | -100.0 | -0.75 |
| book_lag | early | pin $10-50k | 0-2 | 0.0 | -50.0 | -100.0 | -0.75 |
| consensus_gap | early | 10-40k bets | 2-2 | 50.0 | 8.1 | 7.0 | 0.4 |
| consensus_gap | early | 40k+ bets | 2-2 | 50.0 | 24.3 | -6.4 | 0.17 |
| consensus_gap | early | <10k bets | 10-21 | 32.3 | 1.0 | -33.2 | 0.37 |
| consensus_gap | early | pin $10-50k | 4-5 | 44.4 | 3.9 | -7.6 | 0.23 |
| consensus_gap | early | pin $50k+ | 3-3 | 50.0 | 12.2 | -7.3 | 0.43 |
| consensus_gap | early | pin limit <$10k | 6-16 | 27.3 | -0.2 | -45.4 | 0.03 |
| consensus_gap+follow_move | early | 10-40k bets | 1-0 | 100.0 | 37.8 | 82.0 | 0.0 |
| consensus_gap+money_level | early | 10-40k bets | 1-0 | 100.0 | 37.8 | 82.0 | 0.0 |
| consensus_gap+pin_value | early | 10-40k bets | 1-0 | 100.0 | 37.8 | 82.0 | 0.0 |
| consensus_gap+sharp_gap | early | 10-40k bets | 2-2 | 50.0 | 8.1 | 7.0 | 0.4 |
| follow_move+money_level | early | 10-40k bets | 2-1 | 66.7 | -6.3 | 6.3 | -0.4 |
| follow_move+pin_value | early | 10-40k bets | 1-0 | 100.0 | 37.8 | 82.0 | 0.0 |
| follow_move+sharp_gap | early | 10-40k bets | 1-0 | 100.0 | 37.8 | 82.0 | 0.0 |
| money_level+pin_value | early | 10-40k bets | 1-0 | 100.0 | 37.8 | 82.0 | 0.0 |
| money_level+sharp_gap | early | 10-40k bets | 1-1 | 50.0 | -6.8 | -9.0 | 0.0 |
| pin_value+sharp_gap | early | 10-40k bets | 1-0 | 100.0 | 37.8 | 82.0 | 0.0 |
| follow_move+rlm | early | 40k+ bets | 0-1 | 0.0 | -37.8 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -37.8 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | 40k+ bets | 3-2 | 60.0 | -2.2 | -10.9 | -0.1 |
| rlm+rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -37.8 | -100.0 | 0.0 |
| rlm+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -37.8 | -100.0 | 0.0 |
| rlm_ratio+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -37.8 | -100.0 | 0.0 |
| money_level+pin_value | early | 40k+ bets | 0-1 | 0.0 | -51.4 | -100.0 | 0.0 |
| money_level+sharp_gap | early | 40k+ bets | 3-4 | 42.9 | -21.2 | -35.5 | -0.07 |
| pin_value+sharp_gap | early | 40k+ bets | 1-1 | 50.0 | 5.4 | -8.4 | 0.0 |
| follow_move+money_level | early | 40k+ bets | 2-1 | 66.7 | -11.7 | -12.6 | -0.17 |
| consensus_gap+pin_value | early | 40k+ bets | 1-0 | 100.0 | 62.2 | 78.1 | 0.0 |
| follow_move+pin_value | early | 40k+ bets | 1-0 | 100.0 | 62.2 | 83.3 | 0.0 |
| follow_move+money_level | early | <10k bets | 24-9 | 72.7 | 2.0 | 12.3 | -0.79 |
| follow_move+money_moving | early | <10k bets | 6-2 | 75.0 | 7.8 | 22.8 | -0.39 |
| follow_move+pin_value | early | <10k bets | 2-1 | 66.7 | 4.5 | 27.1 | 0.0 |
| follow_move+sharp_gap | early | <10k bets | 15-5 | 75.0 | 8.0 | 23.7 | -0.42 |
| money_level+money_moving | early | <10k bets | 8-3 | 72.7 | 10.1 | 25.7 | -0.74 |
| money_level+pin_value | early | <10k bets | 6-2 | 75.0 | 20.3 | 43.5 | -0.44 |
| money_level+sharp_gap | early | <10k bets | 33-15 | 68.8 | 12.8 | 23.4 | -0.7 |
| money_moving+pin_value | early | <10k bets | 4-2 | 66.7 | 17.6 | 28.2 | 1.0 |
| money_moving+sharp_gap | early | <10k bets | 6-3 | 66.7 | 15.9 | 25.4 | -0.08 |
| pin_value+sharp_gap | early | <10k bets | 6-4 | 60.0 | 15.9 | 14.8 | 0.56 |
| consensus_gap+sharp_gap | early | <10k bets | 7-10 | 41.2 | 10.5 | -17.8 | 0.21 |
| consensus_gap+follow_move | early | <10k bets | 2-0 | 100.0 | 21.6 | 46.8 | -0.35 |
| consensus_gap+money_level | early | <10k bets | 4-1 | 80.0 | 27.6 | 35.3 | -2.08 |
| book_lag+consensus_gap | early | <10k bets | 0-1 | 0.0 | -37.8 | -100.0 | 0.5 |
| consensus_gap+pin_value | early | <10k bets | 0-6 | 0.0 | -28.4 | -100.0 | 1.37 |
| consensus_gap+pin_rlm | early | <10k bets | 1-3 | 25.0 | 3.4 | -48.0 | -1.47 |
| money_level+pin_rlm | early | <10k bets | 0-1 | 0.0 | -21.6 | -100.0 | -10.6 |
| pin_rlm+sharp_gap | early | <10k bets | 1-3 | 25.0 | 3.4 | -48.0 | -1.47 |
| follow_move+rlm | early | <10k bets | 1-4 | 20.0 | -35.7 | -63.3 | 0.02 |
| book_lag+money_level | early | <10k bets | 0-1 | 0.0 | -62.2 | -100.0 | -2.0 |
| book_lag+money_moving | early | <10k bets | 0-1 | 0.0 | -62.2 | -100.0 | -2.0 |
| book_lag+sharp_gap | early | <10k bets | 0-1 | 0.0 | -62.2 | -100.0 | -2.0 |
| consensus_gap+money_moving | early | <10k bets | 1-1 | 50.0 | 28.4 | 4.0 | 3.45 |
| pin_rlm+pin_value | early | <10k bets | 0-1 | 0.0 | -21.6 | -100.0 | 1.8 |
| money_moving+pin_rlm | early | <10k bets | 1-0 | 100.0 | 78.4 | 108.0 | 1.9 |
| follow_move+rlm_ratio | early | <10k bets | 1-0 | 100.0 | 37.8 | 83.3 | 0.0 |
| rlm+rlm_ratio | early | <10k bets | 1-0 | 100.0 | 37.8 | 83.3 | 0.0 |
| rlm+sharp_gap | early | <10k bets | 1-0 | 100.0 | 37.8 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | <10k bets | 1-0 | 100.0 | 37.8 | 83.3 | 0.0 |
| money_moving+rlm | early | <10k bets | 0-1 | 0.0 | -37.8 | -100.0 | 0.0 |
| money_level+pin_value | early | pin $10-50k | 3-1 | 75.0 | 15.5 | 45.2 | -0.38 |
| money_level+sharp_gap | early | pin $10-50k | 10-8 | 55.6 | 1.8 | 3.0 | -0.11 |
| pin_value+sharp_gap | early | pin $10-50k | 3-1 | 75.0 | 15.5 | 45.2 | -0.38 |
| follow_move+money_level | early | pin $10-50k | 5-4 | 55.6 | -6.6 | 0.4 | 0.08 |
| follow_move+sharp_gap | early | pin $10-50k | 6-2 | 75.0 | 16.9 | 35.8 | 0.19 |
| consensus_gap+sharp_gap | early | pin $10-50k | 3-0 | 100.0 | 64.9 | 113.7 | 0.3 |
| follow_move+money_moving | early | pin $10-50k | 2-0 | 100.0 | 37.8 | 90.6 | 0.0 |
| follow_move+pin_value | early | pin $10-50k | 2-0 | 100.0 | 37.8 | 90.6 | 0.0 |
| money_level+money_moving | early | pin $10-50k | 2-1 | 66.7 | 12.6 | 31.1 | -1.33 |
| money_moving+pin_value | early | pin $10-50k | 3-1 | 75.0 | 18.9 | 44.1 | 0.25 |
| money_moving+sharp_gap | early | pin $10-50k | 2-1 | 66.7 | 18.0 | 35.3 | -0.03 |
| book_lag+consensus_gap | early | pin $10-50k | 0-1 | 0.0 | -37.8 | -100.0 | 0.5 |
| follow_move+rlm | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.5 |
| book_lag+money_level | early | pin $10-50k | 0-1 | 0.0 | -62.2 | -100.0 | -2.0 |
| book_lag+money_moving | early | pin $10-50k | 0-1 | 0.0 | -62.2 | -100.0 | -2.0 |
| book_lag+sharp_gap | early | pin $10-50k | 0-1 | 0.0 | -62.2 | -100.0 | -2.0 |
| consensus_gap+money_level | early | pin $10-50k | 1-0 | 100.0 | 37.8 | 87.0 | 0.0 |
| consensus_gap+pin_value | early | pin $10-50k | 0-1 | 0.0 | -62.2 | -100.0 | 0.0 |
| consensus_gap+money_moving | early | pin $10-50k | 1-0 | 100.0 | 78.4 | 108.0 | 1.9 |
| consensus_gap+pin_rlm | early | pin $10-50k | 1-0 | 100.0 | 78.4 | 108.0 | 1.9 |
| money_moving+pin_rlm | early | pin $10-50k | 1-0 | 100.0 | 78.4 | 108.0 | 1.9 |
| pin_rlm+sharp_gap | early | pin $10-50k | 1-0 | 100.0 | 78.4 | 108.0 | 1.9 |
| follow_move+rlm_ratio | early | pin $10-50k | 1-0 | 100.0 | 37.8 | 83.3 | 0.0 |
| rlm+rlm_ratio | early | pin $10-50k | 1-0 | 100.0 | 37.8 | 83.3 | 0.0 |
| rlm+sharp_gap | early | pin $10-50k | 1-0 | 100.0 | 37.8 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $10-50k | 1-0 | 100.0 | 37.8 | 83.3 | 0.0 |
| follow_move+rlm | early | pin $50k+ | 0-1 | 0.0 | -37.8 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -37.8 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | pin $50k+ | 3-2 | 60.0 | 1.1 | -0.0 | 0.0 |
| rlm+rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -37.8 | -100.0 | 0.0 |
| rlm+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -37.8 | -100.0 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -37.8 | -100.0 | 0.0 |
| follow_move+money_level | early | pin $50k+ | 3-1 | 75.0 | 0.7 | 13.4 | -0.5 |
| money_level+sharp_gap | early | pin $50k+ | 2-2 | 50.0 | -20.3 | -20.9 | 0.0 |
| consensus_gap+pin_value | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 80.0 | 0.0 |
| follow_move+pin_value | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 82.7 | 0.0 |
| pin_value+sharp_gap | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 82.7 | 0.0 |
| consensus_gap+follow_move | early | pin $50k+ | 1-0 | 100.0 | 37.8 | 82.0 | 0.0 |
| consensus_gap+money_level | early | pin $50k+ | 1-0 | 100.0 | 37.8 | 82.0 | 0.0 |
| consensus_gap+sharp_gap | early | pin $50k+ | 1-2 | 33.3 | -15.3 | -39.3 | 0.87 |
| money_level+pin_value | early | pin $50k+ | 1-0 | 100.0 | 37.8 | 82.0 | 0.0 |
| money_level+pin_value | early | pin limit <$10k | 3-2 | 60.0 | 9.7 | 13.4 | -0.4 |
| money_level+sharp_gap | early | pin limit <$10k | 23-8 | 74.2 | 17.9 | 31.3 | -1.01 |
| pin_value+sharp_gap | early | pin limit <$10k | 3-4 | 42.9 | 6.6 | -19.0 | 1.01 |
| follow_move+money_level | early | pin limit <$10k | 19-4 | 82.6 | 8.2 | 22.0 | -0.7 |
| follow_move+sharp_gap | early | pin limit <$10k | 9-2 | 81.8 | 7.9 | 26.6 | -0.86 |
| consensus_gap+sharp_gap | early | pin limit <$10k | 4-10 | 28.6 | -1.2 | -48.7 | -0.56 |
| follow_move+money_moving | early | pin limit <$10k | 4-1 | 80.0 | 4.9 | 20.3 | -0.62 |
| money_level+money_moving | early | pin limit <$10k | 6-2 | 75.0 | 9.1 | 23.7 | -0.51 |
| consensus_gap+follow_move | early | pin limit <$10k | 2-0 | 100.0 | 21.6 | 46.8 | -0.35 |
| consensus_gap+money_level | early | pin limit <$10k | 3-1 | 75.0 | 25.0 | 22.4 | -2.6 |
| consensus_gap+pin_value | early | pin limit <$10k | 0-5 | 0.0 | -21.6 | -100.0 | 1.64 |
| money_moving+sharp_gap | early | pin limit <$10k | 3-2 | 60.0 | 7.6 | 5.4 | 0.28 |
| consensus_gap+pin_rlm | early | pin limit <$10k | 0-3 | 0.0 | -21.6 | -100.0 | -2.6 |
| money_level+pin_rlm | early | pin limit <$10k | 0-1 | 0.0 | -21.6 | -100.0 | -10.6 |
| pin_rlm+sharp_gap | early | pin limit <$10k | 0-3 | 0.0 | -21.6 | -100.0 | -2.6 |
| money_moving+pin_value | early | pin limit <$10k | 1-1 | 50.0 | 14.9 | -3.7 | 2.5 |
| consensus_gap+money_moving | early | pin limit <$10k | 0-1 | 0.0 | -21.6 | -100.0 | 5.0 |
| pin_rlm+pin_value | early | pin limit <$10k | 0-1 | 0.0 | -21.6 | -100.0 | 1.8 |
| follow_move+pin_value | early | pin limit <$10k | 0-1 | 0.0 | -62.2 | -100.0 | 0.0 |
| follow_move+rlm | early | pin limit <$10k | 0-2 | 0.0 | -70.3 | -100.0 | -0.45 |
