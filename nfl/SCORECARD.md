# NFL scorecard

Generated 2026-11-16 07:10 UTC. 41 graded games (0 finished games had no final score and are not graded).

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before kickoff. Break-even at -110 is 52.4%. CLV = points of
closing-line value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured on
this sample. `edge` is hit% minus that. A signal that is structurally long dogs or
unders will beat 50% in any week dogs or unders run, which is not an edge --
this sample ran **65.9% favourites** (n=41)
**53.7% overs** (n=41) and **80.5% moneyline favourites** (n=41) and **50.0% team-total overs** (n=82).

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
| pin_rlm | both | 1-4 | 20.0 | 19.5 | 0.5 | -2.92 | -58.4 | -0.8 | 80.0 | keep collecting (5/30) |
| follow_move | both | 37-18 | 67.3 | 70.4 | -3.1 | +2.76 | 5.0 | -0.02 | 29.1 | beats break-even but not its base rate -- directional bias, not signal |
| rlm | both | 1-5 | 16.7 | 52.4 | -35.8 | -4.17 | -69.5 | 0.02 | 16.7 | keep collecting (6/30) |
| rlm_ratio | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level | both | 66-31 | 68.0 | 61.1 | 7.0 | +16.72 | 17.2 | -0.4 | 23.7 | PROMOTE: beats break-even and its own base rate |
| sharp_gap | both | 56-39 | 58.9 | 50.7 | 8.3 | +8.36 | 8.8 | 0.05 | 33.7 | no edge shown yet |
| money_moving | both | 13-9 | 59.1 | 53.2 | 5.9 | +1.64 | 7.5 | -0.12 | 27.3 | keep collecting (22/30) |
| pin_value | both | 30-25 | 54.5 | 48.2 | 6.4 | +0.99 | 1.8 | 0.14 | 27.3 | no edge shown yet |
| book_lag | both | 1-2 | 33.3 | 55.3 | -22.0 | -1.13 | -37.7 | -0.17 | 66.7 | keep collecting (3/30) |
| consensus_gap | both | 15-30 | 33.3 | 30.4 | 3.0 | -14.4 | -32.0 | 0.13 | 51.1 | DROP: below break-even |
| follow_move+rlm | both | 1-5 | 16.7 | 52.4 | -35.8 | -4.17 | -69.5 | 0.02 | 16.7 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 21-8 | 72.4 | 66.9 | 5.5 | +5.53 | 19.1 | 0.16 | 24.1 | keep collecting (29/30) |
| rlm+rlm_ratio | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_value | both | 9-3 | 75.0 | 57.5 | 17.5 | +5.04 | 42.0 | -0.21 | 8.3 | keep collecting (12/30) |
| money_level+sharp_gap | both | 44-20 | 68.8 | 58.8 | 10.0 | +14.61 | 22.8 | -0.26 | 23.4 | PROMOTE: beats break-even and its own base rate |
| pin_value+sharp_gap | both | 11-5 | 68.8 | 47.7 | 21.0 | +4.74 | 29.6 | 0.54 | 31.2 | keep collecting (16/30) |
| follow_move+money_level | both | 33-11 | 75.0 | 74.1 | 0.9 | +6.57 | 14.9 | -0.33 | 29.5 | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+pin_value | both | 3-7 | 30.0 | 36.3 | -6.3 | -4.53 | -45.3 | 1.02 | 60.0 | keep collecting (10/30) |
| follow_move+pin_value | both | 4-1 | 80.0 | 59.5 | 20.5 | +2.47 | 49.3 | 0.0 | 0.0 | keep collecting (5/30) |
| consensus_gap+follow_move | both | 3-0 | 100.0 | 75.6 | 24.4 | +1.75 | 58.5 | -0.23 | 33.3 | keep collecting (3/30) |
| consensus_gap+money_level | both | 6-1 | 85.7 | 56.8 | 28.9 | +3.46 | 49.4 | -1.34 | 42.9 | keep collecting (7/30) |
| consensus_gap+sharp_gap | both | 10-14 | 41.7 | 32.3 | 9.3 | -3.88 | -16.2 | 0.38 | 62.5 | keep collecting (24/30) |
| follow_move+money_moving | both | 6-2 | 75.0 | 69.2 | 5.8 | +1.83 | 22.8 | -0.39 | 25.0 | keep collecting (8/30) |
| money_level+money_moving | both | 8-3 | 72.7 | 64.3 | 8.4 | +2.83 | 25.7 | -0.74 | 18.2 | keep collecting (11/30) |
| money_moving+pin_value | both | 4-2 | 66.7 | 49.6 | 17.1 | +1.69 | 28.2 | 1.0 | 33.3 | keep collecting (6/30) |
| money_moving+sharp_gap | both | 6-3 | 66.7 | 51.5 | 15.2 | +2.28 | 25.4 | -0.08 | 22.2 | keep collecting (9/30) |
| book_lag+consensus_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.13 | -6.5 | 0.75 | 100.0 | keep collecting (2/30) |
| consensus_gap+pin_rlm | both | 1-4 | 20.0 | 19.5 | 0.5 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | both | 1-4 | 20.0 | 19.5 | 0.5 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+money_level | both | 1-1 | 50.0 | 65.9 | -15.9 | -0.13 | -6.5 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+money_moving | both | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 65.9 | -15.9 | -0.13 | -6.5 | -0.5 | 50.0 | keep collecting (2/30) |
| consensus_gap+money_moving | both | 1-1 | 50.0 | 19.5 | 30.5 | +0.08 | 4.0 | 3.45 | 100.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 | 1.8 | 100.0 | keep collecting (1/30) |
| money_moving+pin_rlm | both | 1-0 | 100.0 | 19.5 | 80.5 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| money_moving+rlm | both | 0-1 | 0.0 | 34.1 | -34.1 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| book_lag+pin_value | both | 1-0 | 100.0 | 65.9 | 34.1 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-4 | 20.0 | 19.5 | 0.5 | -2.92 | -58.4 | -0.8 | 80.0 | keep collecting (5/30) |
| follow_move | moneyline | 26-7 | 78.8 | 80.5 | -1.7 | +3.78 | 11.5 | -0.06 | 36.4 | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 11-10 | 52.4 | 55.3 | -2.9 | -0.02 | -0.1 | 0.19 | 19.0 | keep collecting (21/30) |
| follow_move | total | 0-1 | 0.0 | 53.7 | -53.7 | -1.0 | -100.0 | -3.0 | 0.0 | keep collecting (1/30) |
| rlm | moneyline | 0-1 | 0.0 | 80.5 | -80.5 | -1.0 | -100.0 | -0.9 | 0.0 | keep collecting (1/30) |
| rlm | spread | 1-4 | 20.0 | 46.8 | -26.8 | -3.17 | -63.3 | 0.2 | 20.0 | keep collecting (5/30) |
| rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level | moneyline | 26-6 | 81.2 | 76.7 | 4.6 | +5.05 | 15.8 | -0.76 | 34.4 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 22-10 | 68.8 | 55.0 | 13.8 | +10.37 | 32.4 | -0.17 | 12.5 | PROMOTE: beats break-even and its own base rate |
| money_level | total | 18-15 | 54.5 | 51.9 | 2.7 | +1.3 | 4.0 | -0.27 | 24.2 | no edge shown yet |
| sharp_gap | moneyline | 16-15 | 51.6 | 45.1 | 6.5 | -4.0 | -12.9 | 0.33 | 51.6 | no edge shown yet |
| sharp_gap | spread | 20-13 | 60.6 | 55.3 | 5.3 | +5.27 | 16.0 | 0.02 | 21.2 | no edge shown yet |
| sharp_gap | total | 20-11 | 64.5 | 51.3 | 13.2 | +7.08 | 22.9 | -0.19 | 29.0 | no edge shown yet |
| money_moving | moneyline | 5-2 | 71.4 | 54.4 | 17.1 | +1.1 | 15.6 | 0.33 | 57.1 | keep collecting (7/30) |
| money_moving | spread | 4-5 | 44.4 | 55.3 | -10.8 | -1.28 | -14.3 | -0.11 | 22.2 | keep collecting (9/30) |
| money_moving | total | 4-2 | 66.7 | 48.8 | 17.9 | +1.83 | 30.5 | -0.67 | 0.0 | keep collecting (6/30) |
| pin_value | moneyline | 0-6 | 0.0 | 19.5 | -19.5 | -6.0 | -100.0 | 1.68 | 83.3 | keep collecting (6/30) |
| pin_value | spread | 11-4 | 73.3 | 55.3 | 18.0 | +5.64 | 37.6 | -0.03 | 20.0 | keep collecting (15/30) |
| pin_value | total | 5-6 | 45.5 | 50.3 | -4.9 | -1.52 | -13.8 | 0.0 | 18.2 | keep collecting (11/30) |
| pin_value | tt_away | 8-4 | 66.7 | 50.0 | 16.7 | +2.88 | 24.0 | 0.0 | 25.0 | keep collecting (12/30) |
| pin_value | tt_home | 6-5 | 54.5 | 50.0 | 4.5 | -0.02 | -0.1 | -0.18 | 18.2 | keep collecting (11/30) |
| book_lag | spread | 1-2 | 33.3 | 55.3 | -22.0 | -1.13 | -37.7 | -0.17 | 66.7 | keep collecting (3/30) |
| consensus_gap | moneyline | 9-24 | 27.3 | 23.2 | 4.1 | -13.54 | -41.0 | 0.09 | 57.6 | DROP: below break-even |
| consensus_gap | spread | 6-6 | 50.0 | 50.0 | 0.0 | -0.86 | -7.1 | 0.25 | 33.3 | keep collecting (12/30) |
| follow_move+money_level | moneyline | 25-5 | 83.3 | 80.5 | 2.8 | +5.09 | 17.0 | -0.48 | 33.3 | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+sharp_gap | moneyline | 11-2 | 84.6 | 80.5 | 4.1 | +2.38 | 18.3 | 0.13 | 30.8 | keep collecting (13/30) |
| money_level+sharp_gap | moneyline | 12-3 | 80.0 | 72.4 | 7.6 | +2.34 | 15.6 | -0.53 | 33.3 | keep collecting (15/30) |
| consensus_gap+sharp_gap | moneyline | 7-13 | 35.0 | 25.6 | 9.4 | -5.44 | -27.2 | 0.39 | 65.0 | keep collecting (20/30) |
| follow_move+money_moving | moneyline | 4-0 | 100.0 | 80.5 | 19.5 | +2.02 | 50.4 | -0.78 | 50.0 | keep collecting (4/30) |
| money_level+money_moving | moneyline | 4-0 | 100.0 | 80.5 | 19.5 | +2.02 | 50.4 | -0.78 | 50.0 | keep collecting (4/30) |
| consensus_gap+follow_move | moneyline | 2-0 | 100.0 | 80.5 | 19.5 | +0.94 | 46.8 | -0.35 | 50.0 | keep collecting (2/30) |
| consensus_gap+money_level | moneyline | 3-1 | 75.0 | 50.0 | 25.0 | +0.9 | 22.4 | -2.6 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_value | moneyline | 0-5 | 0.0 | 19.5 | -19.5 | -5.0 | -100.0 | 1.64 | 80.0 | keep collecting (5/30) |
| consensus_gap+pin_rlm | moneyline | 1-4 | 20.0 | 19.5 | 0.5 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+sharp_gap | moneyline | 1-4 | 20.0 | 19.5 | 0.5 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | moneyline | 2-1 | 66.7 | 39.8 | 26.8 | +0.47 | 15.7 | 1.1 | 66.7 | keep collecting (3/30) |
| pin_value+sharp_gap | moneyline | 0-3 | 0.0 | 19.5 | -19.5 | -3.0 | -100.0 | 3.03 | 100.0 | keep collecting (3/30) |
| consensus_gap+money_moving | moneyline | 1-1 | 50.0 | 19.5 | 30.5 | +0.08 | 4.0 | 3.45 | 100.0 | keep collecting (2/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 | 1.8 | 100.0 | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 1-0 | 100.0 | 19.5 | 80.5 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| follow_move+rlm | moneyline | 0-1 | 0.0 | 80.5 | -80.5 | -1.0 | -100.0 | -0.9 | 0.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm | spread | 1-4 | 20.0 | 46.8 | -26.8 | -3.17 | -63.3 | 0.2 | 20.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 55.9 | 6.6 | +3.14 | 19.7 | 0.19 | 18.8 | keep collecting (16/30) |
| rlm+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+pin_value | spread | 3-2 | 60.0 | 53.2 | 6.8 | +0.47 | 9.4 | 0.4 | 40.0 | keep collecting (5/30) |
| money_level+sharp_gap | spread | 17-8 | 68.0 | 57.0 | 11.0 | +7.65 | 30.6 | -0.1 | 16.0 | keep collecting (25/30) |
| follow_move+pin_value | spread | 4-1 | 80.0 | 59.5 | 20.5 | +2.47 | 49.3 | 0.0 | 0.0 | keep collecting (5/30) |
| pin_value+sharp_gap | spread | 7-0 | 100.0 | 56.8 | 43.2 | +6.17 | 88.1 | -0.07 | 14.3 | keep collecting (7/30) |
| consensus_gap+follow_move | spread | 1-0 | 100.0 | 65.9 | 34.1 | +0.82 | 82.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 3-0 | 100.0 | 65.9 | 34.1 | +2.56 | 85.3 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+sharp_gap | spread | 3-1 | 75.0 | 65.9 | 9.1 | +1.56 | 39.0 | 0.38 | 50.0 | keep collecting (4/30) |
| follow_move+money_level | spread | 8-5 | 61.5 | 61.0 | 0.6 | +2.48 | 19.1 | 0.23 | 23.1 | keep collecting (13/30) |
| money_level+pin_value | spread | 6-1 | 85.7 | 61.3 | 24.4 | +4.33 | 61.9 | -0.07 | 14.3 | keep collecting (7/30) |
| follow_move+money_moving | spread | 2-2 | 50.0 | 57.9 | -7.9 | -0.19 | -4.7 | 0.0 | 0.0 | keep collecting (4/30) |
| money_level+money_moving | spread | 2-2 | 50.0 | 57.9 | -7.9 | -0.07 | -1.7 | -1.0 | 0.0 | keep collecting (4/30) |
| money_moving+pin_value | spread | 3-1 | 75.0 | 57.9 | 17.1 | +1.76 | 44.1 | 0.25 | 25.0 | keep collecting (4/30) |
| money_moving+sharp_gap | spread | 1-2 | 33.3 | 65.9 | -32.5 | -1.02 | -34.0 | -0.67 | 0.0 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.13 | -6.5 | 0.75 | 100.0 | keep collecting (2/30) |
| book_lag+money_level | spread | 1-1 | 50.0 | 65.9 | -15.9 | -0.13 | -6.5 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+money_moving | spread | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+sharp_gap | spread | 1-1 | 50.0 | 65.9 | -15.9 | -0.13 | -6.5 | -0.5 | 50.0 | keep collecting (2/30) |
| money_moving+rlm | spread | 0-1 | 0.0 | 34.1 | -34.1 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| book_lag+pin_value | spread | 1-0 | 100.0 | 65.9 | 34.1 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_value | total | 3-2 | 60.0 | 52.2 | 7.8 | +0.71 | 14.1 | -0.4 | 0.0 | keep collecting (5/30) |
| money_level+sharp_gap | total | 15-9 | 62.5 | 52.1 | 10.4 | +4.61 | 19.2 | -0.25 | 25.0 | keep collecting (24/30) |
| pin_value+sharp_gap | total | 4-2 | 66.7 | 51.2 | 15.4 | +1.58 | 26.3 | 0.0 | 16.7 | keep collecting (6/30) |
| follow_move+money_level | total | 0-1 | 0.0 | 53.7 | -53.7 | -1.0 | -100.0 | -3.0 | 0.0 | redundant -- identical record to follow_move alone, not independent confirmation |
| money_level+money_moving | total | 2-1 | 66.7 | 51.2 | 15.4 | +0.88 | 29.3 | -0.33 | 0.0 | keep collecting (3/30) |
| money_moving+sharp_gap | total | 3-0 | 100.0 | 48.8 | 51.2 | +2.83 | 94.3 | -0.67 | 0.0 | keep collecting (3/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 46.3 | 53.7 | +0.93 | 92.6 | 0.0 | 0.0 | keep collecting (1/30) |

## CLOSE

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 5-10 | 33.3 | 30.7 | 2.6 | -5.07 | -33.8 |  |  | keep collecting (15/30) |
| follow_move | both | 72-53 | 57.6 | 61.2 | -3.6 | -3.84 | -3.1 |  |  | no edge shown yet |
| rlm | both | 5-17 | 22.7 | 48.8 | -26.1 | -12.57 | -57.1 |  |  | keep collecting (22/30) |
| rlm_ratio | both | 3-8 | 27.3 | 48.6 | -21.3 | -5.31 | -48.3 |  |  | keep collecting (11/30) |
| money_level | both | 80-40 | 66.7 | 61.8 | 4.9 | +18.18 | 15.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 55-64 | 46.2 | 48.6 | -2.4 | -18.31 | -15.4 |  |  | no edge shown yet |
| money_moving | both | 35-56 | 38.5 | 43.1 | -4.6 | -26.49 | -29.1 |  |  | DROP: below break-even |
| pin_value | both | 57-42 | 57.6 | 49.2 | 8.4 | +6.93 | 7.0 |  |  | no edge shown yet |
| book_lag | both | 4-0 | 100.0 | 57.9 | 42.1 | +3.29 | 82.4 |  |  | keep collecting (4/30) |
| consensus_gap | both | 17-32 | 34.7 | 29.5 | 5.2 | -13.57 | -27.7 |  |  | DROP: below break-even |
| follow_move+rlm | both | 5-17 | 22.7 | 48.8 | -26.1 | -12.57 | -57.1 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | both | 3-8 | 27.3 | 48.6 | -21.3 | -5.31 | -48.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 29-24 | 54.7 | 60.4 | -5.7 | -4.54 | -8.6 |  |  | no edge shown yet |
| money_level+pin_value | both | 15-6 | 71.4 | 57.7 | 13.7 | +6.96 | 33.1 |  |  | keep collecting (21/30) |
| rlm+rlm_ratio | both | 3-8 | 27.3 | 48.6 | -21.3 | -5.31 | -48.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 4-13 | 23.5 | 45.6 | -22.1 | -9.44 | -55.5 |  |  | keep collecting (17/30) |
| rlm_ratio+sharp_gap | both | 3-8 | 27.3 | 48.6 | -21.3 | -5.31 | -48.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 40-25 | 61.5 | 59.4 | 2.1 | +4.82 | 7.4 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 7-1 | 87.5 | 55.8 | 31.7 | +4.86 | 60.7 |  |  | keep collecting (8/30) |
| follow_move+money_level | both | 47-17 | 73.4 | 71.1 | 2.4 | +10.49 | 16.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+sharp_gap | both | 8-14 | 36.4 | 29.2 | 7.2 | -4.75 | -21.6 |  |  | keep collecting (22/30) |
| follow_move+pin_value | both | 10-4 | 71.4 | 57.6 | 13.9 | +4.43 | 31.7 |  |  | keep collecting (14/30) |
| pin_value+rlm | both | 2-3 | 40.0 | 51.7 | -11.7 | -1.26 | -25.2 |  |  | keep collecting (5/30) |
| pin_value+sharp_gap | both | 15-11 | 57.7 | 47.2 | 10.5 | +1.58 | 6.1 |  |  | keep collecting (26/30) |
| consensus_gap+pin_value | both | 3-6 | 33.3 | 22.8 | 10.6 | -3.42 | -38.0 |  |  | keep collecting (9/30) |
| book_lag+consensus_gap | both | 3-0 | 100.0 | 55.3 | 44.7 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| book_lag+money_moving | both | 1-0 | 100.0 | 34.1 | 65.9 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | both | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | both | 6-15 | 28.6 | 23.1 | 5.5 | -8.63 | -41.1 |  |  | keep collecting (21/30) |
| money_moving+pin_value | both | 10-10 | 50.0 | 44.3 | 5.7 | -1.66 | -8.3 |  |  | keep collecting (20/30) |
| money_moving+sharp_gap | both | 24-38 | 38.7 | 43.0 | -4.3 | -17.33 | -28.0 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 3-1 | 75.0 | 76.8 | -1.8 | +0.54 | 13.4 |  |  | keep collecting (4/30) |
| money_level+money_moving | both | 23-13 | 63.9 | 57.8 | 6.1 | +5.27 | 14.6 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 2-6 | 25.0 | 19.5 | 5.5 | -3.76 | -47.0 |  |  | keep collecting (8/30) |
| money_level+pin_rlm | both | 0-3 | 0.0 | 39.8 | -39.8 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | both | 5-10 | 33.3 | 30.7 | 2.6 | -5.07 | -33.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 5-10 | 33.3 | 30.7 | 2.6 | -5.07 | -33.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+money_moving | both | 14-17 | 45.2 | 57.1 | -12.0 | -7.31 | -23.6 |  |  | no edge shown yet |
| follow_move+pin_rlm | both | 3-3 | 50.0 | 47.6 | 2.4 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| money_moving+rlm | both | 3-11 | 21.4 | 45.3 | -23.9 | -8.31 | -59.4 |  |  | keep collecting (14/30) |
| money_moving+rlm_ratio | both | 3-5 | 37.5 | 44.2 | -6.7 | -2.31 | -28.9 |  |  | keep collecting (8/30) |
| pin_rlm+pin_value | both | 1-3 | 25.0 | 32.9 | -7.9 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| pin_rlm+rlm | both | 3-3 | 50.0 | 47.6 | 2.4 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| pin_rlm+rlm_ratio | both | 3-3 | 50.0 | 47.6 | 2.4 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| pin_value+rlm_ratio | both | 1-1 | 50.0 | 46.3 | 3.7 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| money_level+rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+rlm | both | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| book_lag+money_level | both | 1-0 | 100.0 | 65.9 | 34.1 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 2-7 | 22.2 | 19.5 | 2.7 | -4.76 | -52.9 |  |  | keep collecting (9/30) |
| pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| follow_move | moneyline | 32-8 | 80.0 | 80.5 | -0.5 | +5.17 | 12.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 15-20 | 42.9 | 55.0 | -12.1 | -6.23 | -17.8 |  |  | no edge shown yet |
| follow_move | total | 9-9 | 50.0 | 50.0 | 0.0 | -0.8 | -4.5 |  |  | keep collecting (18/30) |
| follow_move | tt_away | 8-7 | 53.3 | 50.0 | 3.3 | -0.0 | -0.0 |  |  | keep collecting (15/30) |
| follow_move | tt_home | 8-9 | 47.1 | 50.0 | -2.9 | -1.97 | -11.6 |  |  | keep collecting (17/30) |
| rlm | moneyline | 0-1 | 0.0 | 80.5 | -80.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm | spread | 1-11 | 8.3 | 47.4 | -39.0 | -10.13 | -84.4 |  |  | keep collecting (12/30) |
| rlm | total | 4-5 | 44.4 | 47.2 | -2.7 | -1.44 | -16.0 |  |  | keep collecting (9/30) |
| rlm_ratio | moneyline | 0-1 | 0.0 | 80.5 | -80.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_ratio | spread | 0-6 | 0.0 | 44.7 | -44.7 | -6.0 | -100.0 |  |  | keep collecting (6/30) |
| rlm_ratio | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| money_level | moneyline | 34-6 | 85.0 | 75.9 | 9.1 | +10.25 | 25.6 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level | spread | 24-16 | 60.0 | 56.3 | 3.7 | +5.72 | 14.3 |  |  | no edge shown yet |
| money_level | total | 22-18 | 55.0 | 53.1 | 1.9 | +2.21 | 5.5 |  |  | no edge shown yet |
| sharp_gap | moneyline | 20-18 | 52.6 | 51.6 | 1.0 | -3.69 | -9.7 |  |  | no edge shown yet |
| sharp_gap | spread | 16-24 | 40.0 | 43.7 | -3.7 | -9.82 | -24.5 |  |  | DROP: below break-even |
| sharp_gap | total | 19-22 | 46.3 | 50.6 | -4.3 | -4.8 | -11.7 |  |  | no edge shown yet |
| money_moving | moneyline | 12-19 | 38.7 | 37.2 | 1.5 | -10.22 | -33.0 |  |  | DROP: below break-even |
| money_moving | spread | 9-20 | 31.0 | 41.8 | -10.8 | -12.0 | -41.4 |  |  | keep collecting (29/30) |
| money_moving | total | 14-17 | 45.2 | 50.1 | -5.0 | -4.27 | -13.8 |  |  | no edge shown yet |
| pin_value | moneyline | 2-6 | 25.0 | 27.1 | -2.1 | -4.59 | -57.4 |  |  | keep collecting (8/30) |
| pin_value | spread | 15-3 | 83.3 | 55.3 | 28.0 | +10.04 | 55.8 |  |  | keep collecting (18/30) |
| pin_value | total | 11-10 | 52.4 | 50.5 | 1.9 | -0.38 | -1.8 |  |  | keep collecting (21/30) |
| pin_value | tt_away | 14-11 | 56.0 | 50.0 | 6.0 | +1.14 | 4.6 |  |  | keep collecting (25/30) |
| pin_value | tt_home | 15-12 | 55.6 | 50.0 | 5.6 | +0.73 | 2.7 |  |  | keep collecting (27/30) |
| book_lag | spread | 4-0 | 100.0 | 57.9 | 42.1 | +3.29 | 82.4 |  |  | keep collecting (4/30) |
| consensus_gap | moneyline | 12-29 | 29.3 | 25.5 | 3.8 | -14.7 | -35.8 |  |  | DROP: below break-even |
| consensus_gap | spread | 5-3 | 62.5 | 50.0 | 12.5 | +1.13 | 14.1 |  |  | keep collecting (8/30) |
| consensus_gap+money_level | moneyline | 6-1 | 85.7 | 54.4 | 31.4 | +4.02 | 57.5 |  |  | keep collecting (7/30) |
| follow_move+rlm | moneyline | 0-1 | 0.0 | 80.5 | -80.5 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 0-1 | 0.0 | 80.5 | -80.5 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 15-4 | 78.9 | 80.5 | -1.5 | +2.78 | 14.6 |  |  | keep collecting (19/30) |
| rlm+rlm_ratio | moneyline | 0-1 | 0.0 | 80.5 | -80.5 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+sharp_gap | moneyline | 0-1 | 0.0 | 80.5 | -80.5 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 0-1 | 0.0 | 80.5 | -80.5 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+sharp_gap | moneyline | 7-13 | 35.0 | 28.7 | 6.3 | -4.58 | -22.9 |  |  | keep collecting (20/30) |
| follow_move+money_level | moneyline | 31-5 | 86.1 | 80.5 | 5.6 | +7.76 | 21.6 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+sharp_gap | moneyline | 17-4 | 81.0 | 74.7 | 6.3 | +5.17 | 24.6 |  |  | keep collecting (21/30) |
| consensus_gap+pin_value | moneyline | 1-6 | 14.3 | 19.5 | -5.2 | -5.04 | -72.0 |  |  | keep collecting (7/30) |
| pin_value+sharp_gap | moneyline | 1-4 | 20.0 | 31.7 | -11.7 | -3.56 | -71.1 |  |  | keep collecting (5/30) |
| consensus_gap+follow_move | moneyline | 3-0 | 100.0 | 80.5 | 19.5 | +1.54 | 51.2 |  |  | keep collecting (3/30) |
| consensus_gap+money_moving | moneyline | 5-15 | 25.0 | 22.6 | 2.4 | -9.41 | -47.1 |  |  | keep collecting (20/30) |
| money_moving+pin_value | moneyline | 2-4 | 33.3 | 29.7 | 3.7 | -2.59 | -43.2 |  |  | keep collecting (6/30) |
| consensus_gap+pin_rlm | moneyline | 2-6 | 25.0 | 19.5 | 5.5 | -3.76 | -47.0 |  |  | keep collecting (8/30) |
| money_level+money_moving | moneyline | 9-2 | 81.8 | 69.4 | 12.4 | +3.57 | 32.5 |  |  | keep collecting (11/30) |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 2-7 | 22.2 | 19.5 | 2.7 | -4.76 | -52.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | moneyline | 9-12 | 42.9 | 39.8 | 3.0 | -4.87 | -23.2 |  |  | keep collecting (21/30) |
| pin_rlm+sharp_gap | moneyline | 2-7 | 22.2 | 19.5 | 2.7 | -4.76 | -52.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+money_moving | moneyline | 7-1 | 87.5 | 80.5 | 7.0 | +2.19 | 27.4 |  |  | keep collecting (8/30) |
| pin_rlm+pin_value | moneyline | 0-2 | 0.0 | 19.5 | -19.5 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| follow_move+pin_value | moneyline | 1-0 | 100.0 | 80.5 | 19.5 | +0.44 | 44.4 |  |  | keep collecting (1/30) |
| money_level+pin_value | moneyline | 1-0 | 100.0 | 80.5 | 19.5 | +0.44 | 44.4 |  |  | keep collecting (1/30) |
| follow_move+rlm | spread | 1-11 | 8.3 | 47.4 | -39.0 | -10.13 | -84.4 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-6 | 0.0 | 44.7 | -44.7 | -6.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 8-13 | 38.1 | 49.2 | -11.1 | -5.74 | -27.3 |  |  | keep collecting (21/30) |
| money_level+pin_value | spread | 8-2 | 80.0 | 59.5 | 20.5 | +5.18 | 51.8 |  |  | keep collecting (10/30) |
| rlm+rlm_ratio | spread | 0-6 | 0.0 | 44.7 | -44.7 | -6.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 0-9 | 0.0 | 41.2 | -41.2 | -9.0 | -100.0 |  |  | keep collecting (9/30) |
| rlm_ratio+sharp_gap | spread | 0-6 | 0.0 | 44.7 | -44.7 | -6.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 11-9 | 55.0 | 61.1 | -6.1 | +1.09 | 5.4 |  |  | keep collecting (20/30) |
| follow_move+pin_value | spread | 6-1 | 85.7 | 61.3 | 24.4 | +4.28 | 61.2 |  |  | keep collecting (7/30) |
| pin_value+rlm | spread | 1-0 | 100.0 | 65.9 | 34.1 | +0.87 | 87.0 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | spread | 10-9 | 52.6 | 50.8 | 1.8 | -0.14 | -0.8 |  |  | keep collecting (19/30) |
| consensus_gap+sharp_gap | spread | 1-1 | 50.0 | 34.1 | 15.9 | -0.17 | -8.4 |  |  | keep collecting (2/30) |
| book_lag+consensus_gap | spread | 3-0 | 100.0 | 55.3 | 44.7 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| pin_value+sharp_gap | spread | 7-1 | 87.5 | 50.0 | 37.5 | +5.0 | 62.6 |  |  | keep collecting (8/30) |
| book_lag+money_moving | spread | 1-0 | 100.0 | 34.1 | 65.9 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | spread | 1-0 | 100.0 | 34.1 | 65.9 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| consensus_gap+pin_value | spread | 2-0 | 100.0 | 34.1 | 65.9 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| money_moving+pin_value | spread | 4-0 | 100.0 | 50.0 | 50.0 | +3.43 | 85.8 |  |  | keep collecting (4/30) |
| money_level+money_moving | spread | 6-5 | 54.5 | 51.4 | 3.1 | +0.39 | 3.6 |  |  | keep collecting (11/30) |
| money_moving+sharp_gap | spread | 6-14 | 30.0 | 38.9 | -8.9 | -8.55 | -42.8 |  |  | keep collecting (20/30) |
| follow_move+money_moving | spread | 2-9 | 18.2 | 48.6 | -30.4 | -7.09 | -64.5 |  |  | keep collecting (11/30) |
| money_moving+rlm | spread | 0-7 | 0.0 | 43.2 | -43.2 | -7.0 | -100.0 |  |  | keep collecting (7/30) |
| follow_move+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_moving+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-4 | 0.0 | 42.1 | -42.1 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| pin_rlm+rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+follow_move | spread | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+rlm | spread | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| book_lag+money_level | spread | 1-0 | 100.0 | 65.9 | 34.1 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| consensus_gap+money_level | spread | 1-0 | 100.0 | 65.9 | 34.1 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | total | 13-12 | 52.0 | 53.1 | -1.1 | -0.2 | -0.8 |  |  | keep collecting (25/30) |
| pin_value+sharp_gap | total | 7-6 | 53.8 | 51.4 | 2.4 | +0.13 | 1.0 |  |  | keep collecting (13/30) |
| money_level+pin_value | total | 6-4 | 60.0 | 53.7 | 6.3 | +1.33 | 13.3 |  |  | keep collecting (10/30) |
| money_moving+sharp_gap | total | 9-12 | 42.9 | 50.2 | -7.3 | -3.91 | -18.6 |  |  | keep collecting (21/30) |
| money_level+money_moving | total | 8-6 | 57.1 | 53.7 | 3.5 | +1.31 | 9.3 |  |  | keep collecting (14/30) |
| money_moving+pin_value | total | 4-6 | 40.0 | 50.7 | -10.7 | -2.5 | -25.0 |  |  | keep collecting (10/30) |
| follow_move+money_moving | total | 5-7 | 41.7 | 49.4 | -7.7 | -2.4 | -20.0 |  |  | keep collecting (12/30) |
| follow_move+pin_rlm | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+pin_value | total | 2-3 | 40.0 | 49.3 | -9.3 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| follow_move+rlm | total | 4-5 | 44.4 | 47.2 | -2.7 | -1.44 | -16.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 6-7 | 46.2 | 49.2 | -3.0 | -1.58 | -12.2 |  |  | keep collecting (13/30) |
| money_moving+pin_rlm | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm | total | 3-4 | 42.9 | 47.4 | -4.5 | -1.31 | -18.7 |  |  | keep collecting (7/30) |
| money_moving+rlm_ratio | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+pin_value | total | 1-1 | 50.0 | 46.3 | 3.7 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| pin_rlm+rlm | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm | total | 1-3 | 25.0 | 48.2 | -23.2 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| pin_value+rlm_ratio | total | 1-1 | 50.0 | 46.3 | 3.7 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| rlm+rlm_ratio | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | total | 4-3 | 57.1 | 46.3 | 10.8 | +0.56 | 8.0 |  |  | keep collecting (7/30) |
| rlm_ratio+sharp_gap | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | total | 5-3 | 62.5 | 53.7 | 8.8 | +1.64 | 20.5 |  |  | keep collecting (8/30) |
| follow_move+pin_value | tt_home | 1-0 | 100.0 | 50.0 | 50.0 | +0.89 | 88.5 |  |  | keep collecting (1/30) |

## By ticket volume and Pinnacle limit (both markets)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_rlm | close | 40k+ bets | 5-10 | 33.3 | 2.6 | -33.8 |  |
| pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 19.0 | 13.8 |  |
| pin_rlm | close | pin $50k+ | 2-8 | 20.0 | -5.6 | -57.6 |  |
| follow_move | close | 40k+ bets | 72-53 | 57.6 | -3.6 | -3.1 |  |
| follow_move | close | pin $10-50k | 14-9 | 60.9 | 3.1 | -0.6 |  |
| follow_move | close | pin $50k+ | 42-28 | 60.0 | -7.4 | -2.5 |  |
| follow_move | close | pin limit <$10k | 16-16 | 50.0 | 0.0 | -6.2 |  |
| rlm | close | 40k+ bets | 5-17 | 22.7 | -26.1 | -57.1 |  |
| rlm | close | pin $10-50k | 4-5 | 44.4 | -2.7 | -16.0 |  |
| rlm | close | pin $50k+ | 1-12 | 7.7 | -42.2 | -85.6 |  |
| rlm_ratio | close | 40k+ bets | 3-8 | 27.3 | -21.3 | -48.3 |  |
| rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 28.7 | 42.2 |  |
| rlm_ratio | close | pin $50k+ | 0-7 | 0.0 | -49.8 | -100.0 |  |
| money_level | close | 40k+ bets | 80-40 | 66.7 | 4.9 | 15.1 |  |
| money_level | close | pin $10-50k | 26-18 | 59.1 | 2.3 | 4.5 |  |
| money_level | close | pin $50k+ | 54-22 | 71.1 | 6.4 | 21.3 |  |
| sharp_gap | close | 40k+ bets | 55-64 | 46.2 | -2.4 | -15.4 |  |
| sharp_gap | close | pin $10-50k | 20-23 | 46.5 | -5.3 | -15.5 |  |
| sharp_gap | close | pin $50k+ | 35-41 | 46.1 | -0.7 | -15.3 |  |
| money_moving | close | 40k+ bets | 35-56 | 38.5 | -4.6 | -29.1 |  |
| money_moving | close | pin $10-50k | 14-20 | 41.2 | -7.8 | -24.5 |  |
| money_moving | close | pin $50k+ | 21-36 | 36.8 | -2.7 | -31.9 |  |
| pin_value | close | 40k+ bets | 57-42 | 57.6 | 8.4 | 7.0 |  |
| pin_value | close | pin $10-50k | 11-12 | 47.8 | 0.0 | -10.4 |  |
| pin_value | close | pin $50k+ | 17-7 | 70.8 | 22.0 | 31.0 |  |
| pin_value | close | pin limit <$10k | 29-23 | 55.8 | 5.8 | 3.6 |  |
| book_lag | close | 40k+ bets | 4-0 | 100.0 | 42.1 | 82.4 |  |
| book_lag | close | pin $50k+ | 4-0 | 100.0 | 42.1 | 82.4 |  |
| consensus_gap | close | 40k+ bets | 17-32 | 34.7 | 5.2 | -27.7 |  |
| consensus_gap | close | pin $10-50k | 1-5 | 16.7 | -13.0 | -78.6 |  |
| consensus_gap | close | pin $50k+ | 16-27 | 37.2 | 7.8 | -20.6 |  |
| follow_move+rlm | close | 40k+ bets | 5-17 | 22.7 | -26.1 | -57.1 |  |
| follow_move+rlm_ratio | close | 40k+ bets | 3-8 | 27.3 | -21.3 | -48.3 |  |
| follow_move+sharp_gap | close | 40k+ bets | 29-24 | 54.7 | -5.7 | -8.6 |  |
| money_level+pin_value | close | 40k+ bets | 15-6 | 71.4 | 13.7 | 33.1 |  |
| rlm+rlm_ratio | close | 40k+ bets | 3-8 | 27.3 | -21.3 | -48.3 |  |
| rlm+sharp_gap | close | 40k+ bets | 4-13 | 23.5 | -22.1 | -55.5 |  |
| rlm_ratio+sharp_gap | close | 40k+ bets | 3-8 | 27.3 | -21.3 | -48.3 |  |
| money_level+sharp_gap | close | 40k+ bets | 40-25 | 61.5 | 2.1 | 7.4 |  |
| consensus_gap+money_level | close | 40k+ bets | 7-1 | 87.5 | 31.7 | 60.7 |  |
| follow_move+money_level | close | 40k+ bets | 47-17 | 73.4 | 2.4 | 16.4 |  |
| consensus_gap+sharp_gap | close | 40k+ bets | 8-14 | 36.4 | 7.2 | -21.6 |  |
| follow_move+pin_value | close | 40k+ bets | 10-4 | 71.4 | 13.9 | 31.7 |  |
| pin_value+rlm | close | 40k+ bets | 2-3 | 40.0 | -11.7 | -25.2 |  |
| pin_value+sharp_gap | close | 40k+ bets | 15-11 | 57.7 | 10.5 | 6.1 |  |
| consensus_gap+pin_value | close | 40k+ bets | 3-6 | 33.3 | 10.6 | -38.0 |  |
| book_lag+consensus_gap | close | 40k+ bets | 3-0 | 100.0 | 44.7 | 82.0 |  |
| book_lag+money_moving | close | 40k+ bets | 1-0 | 100.0 | 65.9 | 78.1 |  |
| book_lag+pin_value | close | 40k+ bets | 2-0 | 100.0 | 50.0 | 80.7 |  |
| consensus_gap+money_moving | close | 40k+ bets | 6-15 | 28.6 | 5.5 | -41.1 |  |
| money_moving+pin_value | close | 40k+ bets | 10-10 | 50.0 | 5.7 | -8.3 |  |
| money_moving+sharp_gap | close | 40k+ bets | 24-38 | 38.7 | -4.3 | -28.0 |  |
| consensus_gap+follow_move | close | 40k+ bets | 3-1 | 75.0 | -1.8 | 13.4 |  |
| money_level+money_moving | close | 40k+ bets | 23-13 | 63.9 | 6.1 | 14.6 |  |
| consensus_gap+pin_rlm | close | 40k+ bets | 2-6 | 25.0 | 5.5 | -47.0 |  |
| money_level+pin_rlm | close | 40k+ bets | 0-3 | 0.0 | -39.8 | -100.0 |  |
| money_moving+pin_rlm | close | 40k+ bets | 5-10 | 33.3 | 2.6 | -33.8 |  |
| pin_rlm+sharp_gap | close | 40k+ bets | 5-10 | 33.3 | 2.6 | -33.8 |  |
| follow_move+money_moving | close | 40k+ bets | 14-17 | 45.2 | -12.0 | -23.6 |  |
| follow_move+pin_rlm | close | 40k+ bets | 3-3 | 50.0 | 2.4 | -5.2 |  |
| money_moving+rlm | close | 40k+ bets | 3-11 | 21.4 | -23.9 | -59.4 |  |
| money_moving+rlm_ratio | close | 40k+ bets | 3-5 | 37.5 | -6.7 | -28.9 |  |
| pin_rlm+pin_value | close | 40k+ bets | 1-3 | 25.0 | -7.9 | -53.2 |  |
| pin_rlm+rlm | close | 40k+ bets | 3-3 | 50.0 | 2.4 | -5.2 |  |
| pin_rlm+rlm_ratio | close | 40k+ bets | 3-3 | 50.0 | 2.4 | -5.2 |  |
| pin_value+rlm_ratio | close | 40k+ bets | 1-1 | 50.0 | 3.7 | -6.5 |  |
| money_level+rlm | close | 40k+ bets | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_level+rlm_ratio | close | 40k+ bets | 0-2 | 0.0 | -50.0 | -100.0 |  |
| consensus_gap+rlm | close | 40k+ bets | 0-1 | 0.0 | -65.9 | -100.0 |  |
| book_lag+money_level | close | 40k+ bets | 1-0 | 100.0 | 34.1 | 83.3 |  |
| money_level+sharp_gap | close | pin $10-50k | 14-12 | 53.8 | -2.3 | -4.2 |  |
| pin_value+sharp_gap | close | pin $10-50k | 7-7 | 50.0 | 0.9 | -6.2 |  |
| money_level+pin_value | close | pin $10-50k | 6-4 | 60.0 | 6.3 | 13.3 |  |
| consensus_gap+pin_value | close | pin $10-50k | 0-2 | 0.0 | -19.5 | -100.0 |  |
| follow_move+money_level | close | pin $10-50k | 10-3 | 76.9 | 10.9 | 17.8 |  |
| follow_move+sharp_gap | close | pin $10-50k | 8-7 | 53.3 | -1.8 | -10.3 |  |
| money_moving+sharp_gap | close | pin $10-50k | 8-13 | 38.1 | -11.7 | -29.4 |  |
| consensus_gap+follow_move | close | pin $10-50k | 1-0 | 100.0 | 19.5 | 28.6 |  |
| consensus_gap+money_level | close | pin $10-50k | 1-0 | 100.0 | 19.5 | 28.6 |  |
| consensus_gap+sharp_gap | close | pin $10-50k | 1-1 | 50.0 | 0.0 | -35.7 |  |
| money_level+money_moving | close | pin $10-50k | 8-6 | 57.1 | -0.3 | 1.8 |  |
| money_moving+pin_value | close | pin $10-50k | 4-7 | 36.4 | -11.5 | -31.8 |  |
| follow_move+money_moving | close | pin $10-50k | 6-7 | 46.2 | -7.7 | -19.6 |  |
| follow_move+pin_rlm | close | pin $10-50k | 3-1 | 75.0 | 28.7 | 42.2 |  |
| follow_move+pin_value | close | pin $10-50k | 2-3 | 40.0 | -9.3 | -23.6 |  |
| follow_move+rlm | close | pin $10-50k | 4-5 | 44.4 | -2.7 | -16.0 |  |
| follow_move+rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 28.7 | 42.2 |  |
| money_moving+pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 19.0 | 13.8 |  |
| money_moving+rlm | close | pin $10-50k | 3-4 | 42.9 | -4.5 | -18.7 |  |
| money_moving+rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 28.7 | 42.2 |  |
| pin_rlm+pin_value | close | pin $10-50k | 1-2 | 33.3 | -4.1 | -37.7 |  |
| pin_rlm+rlm | close | pin $10-50k | 3-1 | 75.0 | 28.7 | 42.2 |  |
| pin_rlm+rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 28.7 | 42.2 |  |
| pin_rlm+sharp_gap | close | pin $10-50k | 3-2 | 60.0 | 19.0 | 13.8 |  |
| pin_value+rlm | close | pin $10-50k | 1-3 | 25.0 | -23.2 | -53.2 |  |
| pin_value+rlm_ratio | close | pin $10-50k | 1-1 | 50.0 | 3.7 | -6.5 |  |
| rlm+rlm_ratio | close | pin $10-50k | 3-1 | 75.0 | 28.7 | 42.2 |  |
| rlm+sharp_gap | close | pin $10-50k | 4-3 | 57.1 | 10.8 | 8.0 |  |
| rlm_ratio+sharp_gap | close | pin $10-50k | 3-1 | 75.0 | 28.7 | 42.2 |  |
| consensus_gap+money_moving | close | pin $10-50k | 0-2 | 0.0 | -19.5 | -100.0 |  |
| consensus_gap+pin_rlm | close | pin $10-50k | 0-1 | 0.0 | -19.5 | -100.0 |  |
| follow_move+rlm | close | pin $50k+ | 1-12 | 7.7 | -42.2 | -85.6 |  |
| follow_move+rlm_ratio | close | pin $50k+ | 0-7 | 0.0 | -49.8 | -100.0 |  |
| follow_move+sharp_gap | close | pin $50k+ | 21-17 | 55.3 | -7.3 | -7.9 |  |
| money_level+pin_value | close | pin $50k+ | 9-2 | 81.8 | 20.4 | 51.2 |  |
| rlm+rlm_ratio | close | pin $50k+ | 0-7 | 0.0 | -49.8 | -100.0 |  |
| rlm+sharp_gap | close | pin $50k+ | 0-10 | 0.0 | -45.1 | -100.0 |  |
| rlm_ratio+sharp_gap | close | pin $50k+ | 0-7 | 0.0 | -49.8 | -100.0 |  |
| consensus_gap+money_level | close | pin $50k+ | 6-1 | 85.7 | 33.4 | 65.3 |  |
| follow_move+money_level | close | pin $50k+ | 37-14 | 72.5 | 0.2 | 16.0 |  |
| consensus_gap+sharp_gap | close | pin $50k+ | 7-13 | 35.0 | 7.9 | -20.2 |  |
| follow_move+pin_value | close | pin $50k+ | 7-1 | 87.5 | 23.8 | 59.1 |  |
| pin_value+rlm | close | pin $50k+ | 1-0 | 100.0 | 34.1 | 87.0 |  |
| money_level+sharp_gap | close | pin $50k+ | 26-13 | 66.7 | 5.1 | 15.1 |  |
| consensus_gap+pin_value | close | pin $50k+ | 3-4 | 42.9 | 19.2 | -20.3 |  |
| pin_value+sharp_gap | close | pin $50k+ | 8-4 | 66.7 | 21.7 | 20.4 |  |
| book_lag+consensus_gap | close | pin $50k+ | 3-0 | 100.0 | 44.7 | 82.0 |  |
| book_lag+money_moving | close | pin $50k+ | 1-0 | 100.0 | 65.9 | 78.1 |  |
| book_lag+pin_value | close | pin $50k+ | 2-0 | 100.0 | 50.0 | 80.7 |  |
| consensus_gap+money_moving | close | pin $50k+ | 6-13 | 31.6 | 8.1 | -34.9 |  |
| money_moving+pin_value | close | pin $50k+ | 6-3 | 66.7 | 26.8 | 20.4 |  |
| consensus_gap+pin_rlm | close | pin $50k+ | 2-5 | 28.6 | 9.1 | -39.4 |  |
| money_level+money_moving | close | pin $50k+ | 15-7 | 68.2 | 10.2 | 22.8 |  |
| money_level+pin_rlm | close | pin $50k+ | 0-3 | 0.0 | -39.8 | -100.0 |  |
| money_moving+pin_rlm | close | pin $50k+ | 2-8 | 20.0 | -5.6 | -57.6 |  |
| money_moving+sharp_gap | close | pin $50k+ | 16-25 | 39.0 | -0.5 | -27.2 |  |
| pin_rlm+sharp_gap | close | pin $50k+ | 2-8 | 20.0 | -5.6 | -57.6 |  |
| follow_move+money_moving | close | pin $50k+ | 8-10 | 44.4 | -15.0 | -26.4 |  |
| pin_rlm+pin_value | close | pin $50k+ | 0-1 | 0.0 | -19.5 | -100.0 |  |
| consensus_gap+follow_move | close | pin $50k+ | 2-1 | 66.7 | -8.9 | 8.4 |  |
| money_moving+rlm | close | pin $50k+ | 0-7 | 0.0 | -43.2 | -100.0 |  |
| follow_move+pin_rlm | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_level+rlm | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_level+rlm_ratio | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| money_moving+rlm_ratio | close | pin $50k+ | 0-4 | 0.0 | -42.1 | -100.0 |  |
| pin_rlm+rlm | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| pin_rlm+rlm_ratio | close | pin $50k+ | 0-2 | 0.0 | -50.0 | -100.0 |  |
| consensus_gap+rlm | close | pin $50k+ | 0-1 | 0.0 | -65.9 | -100.0 |  |
| book_lag+money_level | close | pin $50k+ | 1-0 | 100.0 | 34.1 | 83.3 |  |
| follow_move+pin_value | close | pin limit <$10k | 1-0 | 100.0 | 50.0 | 88.5 |  |
| pin_rlm | early | <10k bets | 1-4 | 20.0 | 0.5 | -58.4 | -0.8 |
| pin_rlm | early | pin $10-50k | 1-0 | 100.0 | 80.5 | 108.0 | 1.9 |
| pin_rlm | early | pin limit <$10k | 0-4 | 0.0 | -19.5 | -100.0 | -1.47 |
| follow_move | early | 10-40k bets | 2-1 | 66.7 | -8.9 | 6.3 | -0.4 |
| follow_move | early | 40k+ bets | 3-2 | 60.0 | -2.0 | -10.9 | -0.1 |
| follow_move | early | <10k bets | 32-15 | 68.1 | -2.9 | 6.6 | 0.01 |
| follow_move | early | pin $10-50k | 7-5 | 58.3 | -3.3 | 5.8 | 0.14 |
| follow_move | early | pin $50k+ | 4-2 | 66.7 | 4.1 | 6.1 | -0.33 |
| follow_move | early | pin limit <$10k | 25-8 | 75.8 | 0.1 | 13.5 | 0.29 |
| rlm | early | 40k+ bets | 0-1 | 0.0 | -34.1 | -100.0 | 0.0 |
| rlm | early | <10k bets | 1-4 | 20.0 | -36.1 | -63.3 | 0.02 |
| rlm | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.5 |
| rlm | early | pin $50k+ | 0-1 | 0.0 | -34.1 | -100.0 | 0.0 |
| rlm | early | pin limit <$10k | 0-2 | 0.0 | -73.2 | -100.0 | -0.45 |
| rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -34.1 | -100.0 | 0.0 |
| rlm_ratio | early | <10k bets | 1-0 | 100.0 | 34.1 | 83.3 | 0.0 |
| rlm_ratio | early | pin $10-50k | 1-0 | 100.0 | 34.1 | 83.3 | 0.0 |
| rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -34.1 | -100.0 | 0.0 |
| money_level | early | 10-40k bets | 3-3 | 50.0 | -10.2 | -13.8 | -0.28 |
| money_level | early | 40k+ bets | 4-4 | 50.0 | -15.9 | -19.9 | -0.06 |
| money_level | early | <10k bets | 59-24 | 71.1 | 10.4 | 23.1 | -0.44 |
| money_level | early | pin $10-50k | 12-11 | 52.2 | -2.1 | -2.3 | -0.23 |
| money_level | early | pin $50k+ | 5-2 | 71.4 | 3.8 | 20.1 | -0.36 |
| money_level | early | pin limit <$10k | 47-14 | 77.0 | 14.7 | 30.6 | -0.37 |
| sharp_gap | early | 10-40k bets | 3-3 | 50.0 | 3.7 | 3.1 | 0.27 |
| sharp_gap | early | 40k+ bets | 4-5 | 44.4 | -14.4 | -29.5 | -0.06 |
| sharp_gap | early | <10k bets | 49-31 | 61.3 | 11.2 | 13.5 | 0.04 |
| sharp_gap | early | pin $10-50k | 13-10 | 56.5 | 3.4 | 8.3 | 0.06 |
| sharp_gap | early | pin $50k+ | 3-5 | 37.5 | -18.3 | -37.5 | 0.33 |
| sharp_gap | early | pin limit <$10k | 36-22 | 62.1 | 13.6 | 12.9 | -0.1 |
| money_moving | early | <10k bets | 13-9 | 59.1 | 5.9 | 7.5 | -0.12 |
| money_moving | early | pin $10-50k | 5-2 | 71.4 | 21.3 | 40.0 | -0.16 |
| money_moving | early | pin limit <$10k | 7-6 | 53.8 | -3.0 | -8.5 | 0.03 |
| pin_value | early | 10-40k bets | 1-2 | 33.3 | -22.0 | -39.3 | 0.0 |
| pin_value | early | 40k+ bets | 4-2 | 66.7 | 21.3 | 22.5 | 0.0 |
| pin_value | early | <10k bets | 25-21 | 54.3 | 6.3 | 1.8 | 0.17 |
| pin_value | early | pin $10-50k | 6-3 | 66.7 | 5.7 | 27.8 | -0.28 |
| pin_value | early | pin $50k+ | 3-0 | 100.0 | 55.3 | 81.1 | 0.0 |
| pin_value | early | pin limit <$10k | 21-22 | 48.8 | 3.1 | -9.2 | 0.23 |
| book_lag | early | <10k bets | 1-2 | 33.3 | -22.0 | -37.7 | -0.17 |
| book_lag | early | pin $10-50k | 0-2 | 0.0 | -50.0 | -100.0 | -0.75 |
| book_lag | early | pin limit <$10k | 1-0 | 100.0 | 34.1 | 87.0 | 1.0 |
| consensus_gap | early | 10-40k bets | 2-2 | 50.0 | 7.3 | 7.0 | 0.4 |
| consensus_gap | early | 40k+ bets | 2-2 | 50.0 | 26.8 | -6.4 | 0.17 |
| consensus_gap | early | <10k bets | 11-26 | 29.7 | -0.1 | -39.0 | 0.1 |
| consensus_gap | early | pin $10-50k | 4-5 | 44.4 | 4.6 | -7.6 | 0.23 |
| consensus_gap | early | pin $50k+ | 3-3 | 50.0 | 12.6 | -7.3 | 0.43 |
| consensus_gap | early | pin limit <$10k | 7-21 | 25.0 | -1.6 | -50.4 | -0.26 |
| consensus_gap+follow_move | early | 10-40k bets | 1-0 | 100.0 | 34.1 | 82.0 | 0.0 |
| consensus_gap+money_level | early | 10-40k bets | 1-0 | 100.0 | 34.1 | 82.0 | 0.0 |
| consensus_gap+pin_value | early | 10-40k bets | 1-0 | 100.0 | 34.1 | 82.0 | 0.0 |
| consensus_gap+sharp_gap | early | 10-40k bets | 2-2 | 50.0 | 7.3 | 7.0 | 0.4 |
| follow_move+money_level | early | 10-40k bets | 2-1 | 66.7 | -8.9 | 6.3 | -0.4 |
| follow_move+pin_value | early | 10-40k bets | 1-0 | 100.0 | 34.1 | 82.0 | 0.0 |
| follow_move+sharp_gap | early | 10-40k bets | 1-0 | 100.0 | 34.1 | 82.0 | 0.0 |
| money_level+pin_value | early | 10-40k bets | 1-0 | 100.0 | 34.1 | 82.0 | 0.0 |
| money_level+sharp_gap | early | 10-40k bets | 1-1 | 50.0 | -9.8 | -9.0 | 0.0 |
| pin_value+sharp_gap | early | 10-40k bets | 1-0 | 100.0 | 34.1 | 82.0 | 0.0 |
| follow_move+rlm | early | 40k+ bets | 0-1 | 0.0 | -34.1 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -34.1 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | 40k+ bets | 3-2 | 60.0 | -2.0 | -10.9 | -0.1 |
| rlm+rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -34.1 | -100.0 | 0.0 |
| rlm+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -34.1 | -100.0 | 0.0 |
| rlm_ratio+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -34.1 | -100.0 | 0.0 |
| money_level+pin_value | early | 40k+ bets | 0-1 | 0.0 | -53.7 | -100.0 | 0.0 |
| money_level+sharp_gap | early | 40k+ bets | 3-4 | 42.9 | -23.0 | -35.5 | -0.07 |
| pin_value+sharp_gap | early | 40k+ bets | 1-1 | 50.0 | 6.1 | -8.4 | 0.0 |
| follow_move+money_level | early | 40k+ bets | 2-1 | 66.7 | -13.8 | -12.6 | -0.17 |
| consensus_gap+pin_value | early | 40k+ bets | 1-0 | 100.0 | 65.9 | 78.1 | 0.0 |
| follow_move+pin_value | early | 40k+ bets | 1-0 | 100.0 | 65.9 | 83.3 | 0.0 |
| follow_move+money_level | early | <10k bets | 29-9 | 76.3 | 2.8 | 17.8 | -0.34 |
| follow_move+money_moving | early | <10k bets | 6-2 | 75.0 | 5.8 | 22.8 | -0.39 |
| follow_move+pin_value | early | <10k bets | 2-1 | 66.7 | 0.8 | 27.1 | 0.0 |
| follow_move+sharp_gap | early | <10k bets | 17-6 | 73.9 | 5.8 | 22.8 | 0.23 |
| money_level+money_moving | early | <10k bets | 8-3 | 72.7 | 8.4 | 25.7 | -0.74 |
| money_level+pin_value | early | <10k bets | 8-2 | 80.0 | 22.9 | 52.2 | -0.25 |
| money_level+sharp_gap | early | <10k bets | 40-15 | 72.7 | 14.9 | 31.4 | -0.29 |
| money_moving+pin_value | early | <10k bets | 4-2 | 66.7 | 17.1 | 28.2 | 1.0 |
| money_moving+sharp_gap | early | <10k bets | 6-3 | 66.7 | 15.2 | 25.4 | -0.08 |
| pin_value+sharp_gap | early | <10k bets | 9-4 | 69.2 | 22.3 | 31.4 | 0.66 |
| consensus_gap+sharp_gap | early | <10k bets | 8-12 | 40.0 | 9.8 | -20.8 | 0.38 |
| consensus_gap+follow_move | early | <10k bets | 2-0 | 100.0 | 19.5 | 46.8 | -0.35 |
| consensus_gap+money_level | early | <10k bets | 5-1 | 83.3 | 28.0 | 43.9 | -1.57 |
| book_lag+consensus_gap | early | <10k bets | 1-1 | 50.0 | 0.0 | -6.5 | 0.75 |
| consensus_gap+pin_value | early | <10k bets | 1-7 | 12.5 | -20.4 | -76.6 | 1.27 |
| consensus_gap+pin_rlm | early | <10k bets | 1-4 | 20.0 | 0.5 | -58.4 | -0.8 |
| money_level+pin_rlm | early | <10k bets | 0-1 | 0.0 | -19.5 | -100.0 | -10.6 |
| pin_rlm+sharp_gap | early | <10k bets | 1-4 | 20.0 | 0.5 | -58.4 | -0.8 |
| follow_move+rlm | early | <10k bets | 1-4 | 20.0 | -36.1 | -63.3 | 0.02 |
| book_lag+money_level | early | <10k bets | 1-1 | 50.0 | -15.9 | -6.5 | -0.5 |
| book_lag+money_moving | early | <10k bets | 0-1 | 0.0 | -65.9 | -100.0 | -2.0 |
| book_lag+sharp_gap | early | <10k bets | 1-1 | 50.0 | -15.9 | -6.5 | -0.5 |
| consensus_gap+money_moving | early | <10k bets | 1-1 | 50.0 | 30.5 | 4.0 | 3.45 |
| pin_rlm+pin_value | early | <10k bets | 0-1 | 0.0 | -19.5 | -100.0 | 1.8 |
| money_moving+pin_rlm | early | <10k bets | 1-0 | 100.0 | 80.5 | 108.0 | 1.9 |
| follow_move+rlm_ratio | early | <10k bets | 1-0 | 100.0 | 34.1 | 83.3 | 0.0 |
| rlm+rlm_ratio | early | <10k bets | 1-0 | 100.0 | 34.1 | 83.3 | 0.0 |
| rlm+sharp_gap | early | <10k bets | 1-0 | 100.0 | 34.1 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | <10k bets | 1-0 | 100.0 | 34.1 | 83.3 | 0.0 |
| money_moving+rlm | early | <10k bets | 0-1 | 0.0 | -34.1 | -100.0 | 0.0 |
| book_lag+pin_value | early | <10k bets | 1-0 | 100.0 | 34.1 | 87.0 | 1.0 |
| money_level+pin_value | early | pin $10-50k | 3-1 | 75.0 | 12.2 | 45.2 | -0.38 |
| money_level+sharp_gap | early | pin $10-50k | 10-8 | 55.6 | 0.8 | 3.0 | -0.11 |
| pin_value+sharp_gap | early | pin $10-50k | 3-1 | 75.0 | 12.2 | 45.2 | -0.38 |
| follow_move+money_level | early | pin $10-50k | 5-4 | 55.6 | -8.1 | 0.4 | 0.08 |
| follow_move+sharp_gap | early | pin $10-50k | 6-2 | 75.0 | 15.2 | 35.8 | 0.19 |
| consensus_gap+sharp_gap | early | pin $10-50k | 3-0 | 100.0 | 65.0 | 113.7 | 0.3 |
| follow_move+money_moving | early | pin $10-50k | 2-0 | 100.0 | 34.1 | 90.6 | 0.0 |
| follow_move+pin_value | early | pin $10-50k | 2-0 | 100.0 | 34.1 | 90.6 | 0.0 |
| money_level+money_moving | early | pin $10-50k | 2-1 | 66.7 | 11.4 | 31.1 | -1.33 |
| money_moving+pin_value | early | pin $10-50k | 3-1 | 75.0 | 17.1 | 44.1 | 0.25 |
| money_moving+sharp_gap | early | pin $10-50k | 2-1 | 66.7 | 16.3 | 35.3 | -0.03 |
| book_lag+consensus_gap | early | pin $10-50k | 0-1 | 0.0 | -34.1 | -100.0 | 0.5 |
| follow_move+rlm | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.5 |
| book_lag+money_level | early | pin $10-50k | 0-1 | 0.0 | -65.9 | -100.0 | -2.0 |
| book_lag+money_moving | early | pin $10-50k | 0-1 | 0.0 | -65.9 | -100.0 | -2.0 |
| book_lag+sharp_gap | early | pin $10-50k | 0-1 | 0.0 | -65.9 | -100.0 | -2.0 |
| consensus_gap+money_level | early | pin $10-50k | 1-0 | 100.0 | 34.1 | 87.0 | 0.0 |
| consensus_gap+pin_value | early | pin $10-50k | 0-1 | 0.0 | -65.9 | -100.0 | 0.0 |
| consensus_gap+money_moving | early | pin $10-50k | 1-0 | 100.0 | 80.5 | 108.0 | 1.9 |
| consensus_gap+pin_rlm | early | pin $10-50k | 1-0 | 100.0 | 80.5 | 108.0 | 1.9 |
| money_moving+pin_rlm | early | pin $10-50k | 1-0 | 100.0 | 80.5 | 108.0 | 1.9 |
| pin_rlm+sharp_gap | early | pin $10-50k | 1-0 | 100.0 | 80.5 | 108.0 | 1.9 |
| follow_move+rlm_ratio | early | pin $10-50k | 1-0 | 100.0 | 34.1 | 83.3 | 0.0 |
| rlm+rlm_ratio | early | pin $10-50k | 1-0 | 100.0 | 34.1 | 83.3 | 0.0 |
| rlm+sharp_gap | early | pin $10-50k | 1-0 | 100.0 | 34.1 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $10-50k | 1-0 | 100.0 | 34.1 | 83.3 | 0.0 |
| follow_move+rlm | early | pin $50k+ | 0-1 | 0.0 | -34.1 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -34.1 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | pin $50k+ | 3-2 | 60.0 | 1.0 | -0.0 | 0.0 |
| rlm+rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -34.1 | -100.0 | 0.0 |
| rlm+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -34.1 | -100.0 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -34.1 | -100.0 | 0.0 |
| follow_move+money_level | early | pin $50k+ | 3-1 | 75.0 | -1.8 | 13.4 | -0.5 |
| money_level+sharp_gap | early | pin $50k+ | 2-2 | 50.0 | -23.2 | -20.9 | 0.0 |
| consensus_gap+pin_value | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 80.0 | 0.0 |
| follow_move+pin_value | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 82.7 | 0.0 |
| pin_value+sharp_gap | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 82.7 | 0.0 |
| consensus_gap+follow_move | early | pin $50k+ | 1-0 | 100.0 | 34.1 | 82.0 | 0.0 |
| consensus_gap+money_level | early | pin $50k+ | 1-0 | 100.0 | 34.1 | 82.0 | 0.0 |
| consensus_gap+sharp_gap | early | pin $50k+ | 1-2 | 33.3 | -17.1 | -39.3 | 0.87 |
| money_level+pin_value | early | pin $50k+ | 1-0 | 100.0 | 34.1 | 82.0 | 0.0 |
| money_level+pin_value | early | pin limit <$10k | 5-2 | 71.4 | 18.1 | 34.4 | -0.14 |
| money_level+sharp_gap | early | pin limit <$10k | 30-8 | 78.9 | 20.6 | 41.4 | -0.36 |
| pin_value+sharp_gap | early | pin limit <$10k | 6-4 | 60.0 | 18.8 | 12.8 | 1.01 |
| follow_move+money_level | early | pin limit <$10k | 24-4 | 85.7 | 8.8 | 27.7 | -0.1 |
| follow_move+sharp_gap | early | pin limit <$10k | 11-3 | 78.6 | 5.6 | 24.5 | 0.3 |
| consensus_gap+sharp_gap | early | pin limit <$10k | 5-12 | 29.4 | -0.0 | -46.8 | -0.22 |
| follow_move+money_moving | early | pin limit <$10k | 4-1 | 80.0 | 2.4 | 20.3 | -0.62 |
| money_level+money_moving | early | pin limit <$10k | 6-2 | 75.0 | 7.3 | 23.7 | -0.51 |
| consensus_gap+follow_move | early | pin limit <$10k | 2-0 | 100.0 | 19.5 | 46.8 | -0.35 |
| consensus_gap+money_level | early | pin limit <$10k | 4-1 | 80.0 | 26.8 | 35.3 | -1.88 |
| consensus_gap+pin_value | early | pin limit <$10k | 1-6 | 14.3 | -13.9 | -73.3 | 1.46 |
| money_moving+sharp_gap | early | pin limit <$10k | 3-2 | 60.0 | 6.8 | 5.4 | 0.28 |
| consensus_gap+pin_rlm | early | pin limit <$10k | 0-4 | 0.0 | -19.5 | -100.0 | -1.47 |
| money_level+pin_rlm | early | pin limit <$10k | 0-1 | 0.0 | -19.5 | -100.0 | -10.6 |
| pin_rlm+sharp_gap | early | pin limit <$10k | 0-4 | 0.0 | -19.5 | -100.0 | -1.47 |
| money_moving+pin_value | early | pin limit <$10k | 1-1 | 50.0 | 17.1 | -3.7 | 2.5 |
| consensus_gap+money_moving | early | pin limit <$10k | 0-1 | 0.0 | -19.5 | -100.0 | 5.0 |
| pin_rlm+pin_value | early | pin limit <$10k | 0-1 | 0.0 | -19.5 | -100.0 | 1.8 |
| follow_move+pin_value | early | pin limit <$10k | 0-1 | 0.0 | -65.9 | -100.0 | 0.0 |
| follow_move+rlm | early | pin limit <$10k | 0-2 | 0.0 | -73.2 | -100.0 | -0.45 |
| book_lag+consensus_gap | early | pin limit <$10k | 1-0 | 100.0 | 34.1 | 87.0 | 1.0 |
| book_lag+money_level | early | pin limit <$10k | 1-0 | 100.0 | 34.1 | 87.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$10k | 1-0 | 100.0 | 34.1 | 87.0 | 1.0 |
| book_lag+sharp_gap | early | pin limit <$10k | 1-0 | 100.0 | 34.1 | 87.0 | 1.0 |
