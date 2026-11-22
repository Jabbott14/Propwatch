# CBB scorecard

Generated 2026-11-22 19:59 UTC. 772 graded games (33 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**684 games before 2026-11-21 (fit) · 88 on or after it (forward).**

Every signal, threshold and PROMOTE/DROP label here was chosen while looking at
the games before 2026-11-21. `pin_value` went 108-68 in first halves --
fitted and scored on the same 176 games, never tested on one it did not help
choose. So every record appears twice:

- **FIT** — in-sample. A label here is a **hypothesis**.
- **FORWARD** — out-of-sample. A label here is **evidence**.

Base rates are measured separately in each period, so the forward test is not
scored against the fit window's own favourite rate.

The board weights a signal by its FIT edge until it has
30 decided forward outcomes, then by its FORWARD edge. Changing any
threshold moves the holdout date and restarts the forward test.

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before tip. Break-even at -110 is 52.4%. CLV = points of closing-line
value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured
on this sample. `edge` is hit% minus that. A signal that is structurally long
favourites or overs beats 50% whenever those run, which is not an edge -- this
sample ran **47.3% favourites** (n=771) and **50.5% overs** (n=772) and **72.7% moneyline favourites** (n=663).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-21. Nothing in the engine was chosen using these. n=88 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 6-8 | 42.9 | 36.8 | 6.0 | -0.76 | -5.4 | 0.46 | 42.9 | keep collecting (14/30) |
| pin_move | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | 0.0 | 0.0 | keep collecting (2/30) |
| money_delta | both | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| follow_move | both | 51-63 | 44.7 | 48.3 | -3.6 | -16.55 | -14.5 | 0.1 | 33.3 | DROP: below break-even |
| rlm_ratio | both | 4-6 | 40.0 | 40.1 | -0.1 | -1.51 | -15.1 | 0.73 | 50.0 | keep collecting (10/30) |
| money_level | both | 14-15 | 48.3 | 60.8 | -12.6 | -6.73 | -23.2 | 0.02 | 34.5 | keep collecting (29/30) |
| sharp_gap | both | 11-14 | 44.0 | 44.9 | -0.9 | -3.05 | -12.2 | 0.45 | 48.0 | keep collecting (25/30) |
| money_moving | both | 12-11 | 52.2 | 48.6 | 3.5 | +0.83 | 3.6 | 0.57 | 47.8 | keep collecting (23/30) |
| pin_value | both | 4-2 | 66.7 | 45.5 | 21.2 | +1.6 | 26.6 | -0.83 | 16.7 | keep collecting (6/30) |
| consensus_gap | both | 37-28 | 56.9 | 51.9 | 5.0 | +3.12 | 4.8 | 0.4 | 47.7 | no edge shown yet |
| follow_move+money_level | both | 2-7 | 22.2 | 59.0 | -36.8 | -5.98 | -66.4 | 0.33 | 33.3 | keep collecting (9/30) |
| follow_move+sharp_gap | both | 5-9 | 35.7 | 43.9 | -8.2 | -3.6 | -25.7 | 0.59 | 42.9 | keep collecting (14/30) |
| money_level+sharp_gap | both | 4-6 | 40.0 | 56.3 | -16.3 | -3.33 | -33.3 | 0.42 | 50.0 | keep collecting (10/30) |
| follow_move+money_moving | both | 6-7 | 46.2 | 47.6 | -1.4 | -0.52 | -4.0 | 0.62 | 46.2 | keep collecting (13/30) |
| money_level+money_moving | both | 5-7 | 41.7 | 58.2 | -16.6 | -4.21 | -35.1 | 0.5 | 41.7 | keep collecting (12/30) |
| consensus_gap+money_level | both | 6-4 | 60.0 | 62.1 | -2.1 | -1.28 | -12.8 | 0.08 | 40.0 | keep collecting (10/30) |
| follow_move+rlm_quiet | both | 6-8 | 42.9 | 36.8 | 6.0 | -0.76 | -5.4 | 0.46 | 42.9 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 4-6 | 40.0 | 40.1 | -0.1 | -1.51 | -15.1 | 0.73 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | both | 4-4 | 50.0 | 37.6 | 12.4 | +0.49 | 6.1 | 0.04 | 37.5 | keep collecting (8/30) |
| rlm_quiet+sharp_gap | both | 4-5 | 44.4 | 38.3 | 6.2 | -0.51 | -5.7 | 0.03 | 33.3 | keep collecting (9/30) |
| rlm_ratio+sharp_gap | both | 4-6 | 40.0 | 40.1 | -0.1 | -1.51 | -15.1 | 0.73 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 3-5 | 37.5 | 54.2 | -16.7 | -3.29 | -41.2 | 0.89 | 62.5 | keep collecting (8/30) |
| money_moving+rlm_quiet | both | 5-2 | 71.4 | 38.4 | 33.0 | +4.37 | 62.4 | 0.94 | 57.1 | keep collecting (7/30) |
| money_moving+rlm_ratio | both | 4-3 | 57.1 | 42.0 | 15.2 | +1.49 | 21.2 | 1.66 | 71.4 | keep collecting (7/30) |
| money_moving+sharp_gap | both | 7-8 | 46.7 | 45.5 | 1.2 | -0.4 | -2.7 | 0.9 | 60.0 | keep collecting (15/30) |
| consensus_gap+money_moving | both | 3-1 | 75.0 | 59.0 | 16.0 | +0.26 | 6.5 | 0.07 | 25.0 | keep collecting (4/30) |
| consensus_gap+sharp_gap | both | 3-2 | 60.0 | 51.4 | 8.6 | +0.26 | 5.2 | 0.5 | 60.0 | keep collecting (5/30) |
| money_level+rlm_ratio | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 3.5 | 100.0 | keep collecting (2/30) |
| follow_move+pin_move | both | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | both | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_level | both | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_moving | both | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | both | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | both | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| follow_move+pin_value | both | 2-1 | 66.7 | 43.2 | 23.5 | +0.82 | 27.3 | -2.0 | 0.0 | keep collecting (3/30) |
| consensus_gap+pin_move | both | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+pin_value | both | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_move | both | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | both | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_value | both | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 2-6 | 25.0 | 32.1 | -7.1 | -2.36 | -29.5 | 0.31 | 37.5 | keep collecting (8/30) |
| rlm_quiet | total | 4-2 | 66.7 | 43.2 | 23.5 | +1.6 | 26.6 | 0.67 | 50.0 | keep collecting (6/30) |
| pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | 0.0 | 0.0 | keep collecting (2/30) |
| money_delta | total | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| follow_move | moneyline | 20-17 | 54.1 | 47.6 | 6.5 | +1.09 | 2.9 | -0.77 | 24.3 | no edge shown yet |
| follow_move | spread | 12-20 | 37.5 | 51.7 | -14.2 | -9.0 | -28.1 | -0.34 | 18.8 | DROP: below break-even |
| follow_move | total | 19-26 | 42.2 | 46.5 | -4.3 | -8.64 | -19.2 | 1.13 | 51.1 | no edge shown yet |
| rlm_ratio | moneyline | 1-3 | 25.0 | 32.1 | -7.1 | -1.24 | -31.0 | 0.33 | 25.0 | keep collecting (4/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| rlm_ratio | total | 3-2 | 60.0 | 43.2 | 16.8 | +0.73 | 14.5 | 0.2 | 60.0 | keep collecting (5/30) |
| money_level | moneyline | 9-6 | 60.0 | 65.5 | -5.5 | -2.27 | -15.2 | -0.35 | 26.7 | keep collecting (15/30) |
| money_level | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level | total | 5-8 | 38.5 | 55.8 | -17.3 | -3.46 | -26.6 | 0.08 | 38.5 | keep collecting (13/30) |
| sharp_gap | moneyline | 6-6 | 50.0 | 41.0 | 9.0 | +0.4 | 3.4 | 0.77 | 58.3 | keep collecting (12/30) |
| sharp_gap | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| sharp_gap | total | 5-7 | 41.7 | 47.7 | -6.1 | -2.46 | -20.5 | -0.25 | 33.3 | keep collecting (12/30) |
| money_moving | moneyline | 7-4 | 63.6 | 48.4 | 15.3 | +3.28 | 29.8 | 0.64 | 54.5 | keep collecting (11/30) |
| money_moving | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving | total | 5-6 | 45.5 | 48.1 | -2.7 | -1.45 | -13.2 | 0.09 | 36.4 | keep collecting (11/30) |
| pin_value | spread | 2-1 | 66.7 | 43.2 | 23.5 | +0.78 | 26.0 | 0.0 | 33.3 | keep collecting (3/30) |
| pin_value | total | 2-1 | 66.7 | 47.7 | 18.9 | +0.82 | 27.3 | -1.67 | 0.0 | keep collecting (3/30) |
| consensus_gap | moneyline | 15-14 | 51.7 | 54.3 | -2.6 | -2.53 | -8.7 | -0.0 | 41.4 | keep collecting (29/30) |
| consensus_gap | spread | 10-4 | 71.4 | 50.0 | 21.4 | +4.9 | 35.0 | 0.57 | 50.0 | keep collecting (14/30) |
| consensus_gap | total | 12-10 | 54.5 | 50.0 | 4.5 | +0.75 | 3.4 | 0.82 | 54.5 | keep collecting (22/30) |
| consensus_gap+money_level | moneyline | 5-3 | 62.5 | 63.4 | -0.9 | -1.19 | -14.9 | -0.15 | 37.5 | keep collecting (8/30) |
| follow_move+rlm_quiet | moneyline | 2-6 | 25.0 | 32.1 | -7.1 | -2.36 | -29.5 | 0.31 | 37.5 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 1-3 | 25.0 | 32.1 | -7.1 | -1.24 | -31.0 | 0.33 | 25.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 1-3 | 25.0 | 32.1 | -7.1 | -1.24 | -31.0 | 0.33 | 25.0 | keep collecting (4/30) |
| rlm_quiet+rlm_ratio | moneyline | 1-3 | 25.0 | 32.1 | -7.1 | -1.24 | -31.0 | 0.33 | 25.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | moneyline | 1-3 | 25.0 | 32.1 | -7.1 | -1.24 | -31.0 | 0.33 | 25.0 | keep collecting (4/30) |
| rlm_ratio+sharp_gap | moneyline | 1-3 | 25.0 | 32.1 | -7.1 | -1.24 | -31.0 | 0.33 | 25.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 2-1 | 66.7 | 67.9 | -1.2 | -0.2 | -6.8 | -0.63 | 33.3 | keep collecting (3/30) |
| consensus_gap+money_moving | moneyline | 3-1 | 75.0 | 59.0 | 16.0 | +0.26 | 6.5 | 0.07 | 25.0 | keep collecting (4/30) |
| consensus_gap+sharp_gap | moneyline | 3-1 | 75.0 | 50.0 | 25.0 | +1.26 | 31.4 | 0.12 | 50.0 | keep collecting (4/30) |
| money_level+money_moving | moneyline | 4-2 | 66.7 | 61.9 | 4.7 | -0.12 | -1.9 | 0.17 | 33.3 | keep collecting (6/30) |
| money_level+sharp_gap | moneyline | 3-1 | 75.0 | 59.0 | 16.0 | +0.76 | 19.1 | 0.3 | 50.0 | keep collecting (4/30) |
| money_moving+sharp_gap | moneyline | 4-3 | 57.1 | 42.3 | 14.8 | +1.88 | 26.8 | 1.36 | 71.4 | keep collecting (7/30) |
| follow_move+money_level | moneyline | 1-2 | 33.3 | 67.9 | -34.6 | -1.89 | -63.0 | -1.67 | 0.0 | keep collecting (3/30) |
| follow_move+money_moving | moneyline | 3-2 | 60.0 | 46.4 | 13.6 | +1.75 | 35.0 | -0.18 | 40.0 | keep collecting (5/30) |
| money_moving+rlm_quiet | moneyline | 2-1 | 66.7 | 32.1 | 34.6 | +2.64 | 88.0 | 1.2 | 66.7 | keep collecting (3/30) |
| money_moving+rlm_ratio | moneyline | 1-1 | 50.0 | 32.1 | 17.9 | +0.76 | 38.0 | 0.8 | 50.0 | keep collecting (2/30) |
| follow_move+money_level | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| follow_move+money_moving | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to sharp_gap alone, not independent confirmation |
| money_level+money_moving | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+rlm_ratio | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+sharp_gap | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| money_moving+sharp_gap | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 1-0 | 100.0 | 43.2 | 56.8 | +0.91 | 90.9 | -1.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_level | total | 1-4 | 20.0 | 54.1 | -34.1 | -3.09 | -61.8 | 0.6 | 40.0 | keep collecting (5/30) |
| follow_move+sharp_gap | total | 4-5 | 44.4 | 47.7 | -3.3 | -1.36 | -15.2 | 0.22 | 44.4 | keep collecting (9/30) |
| money_level+sharp_gap | total | 1-4 | 20.0 | 54.1 | -34.1 | -3.09 | -61.8 | -0.4 | 40.0 | keep collecting (5/30) |
| follow_move+money_moving | total | 3-4 | 42.9 | 47.1 | -4.2 | -1.27 | -18.2 | 0.57 | 42.9 | keep collecting (7/30) |
| money_level+money_moving | total | 1-4 | 20.0 | 54.1 | -34.1 | -3.09 | -61.8 | 0.0 | 40.0 | keep collecting (5/30) |
| follow_move+rlm_quiet | total | 4-2 | 66.7 | 43.2 | 23.5 | +1.6 | 26.6 | 0.67 | 50.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 3-2 | 60.0 | 43.2 | 16.8 | +0.73 | 14.5 | 0.2 | 60.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 3-1 | 75.0 | 43.2 | 31.8 | +1.73 | 43.2 | -0.25 | 50.0 | keep collecting (4/30) |
| rlm_quiet+sharp_gap | total | 3-2 | 60.0 | 43.2 | 16.8 | +0.73 | 14.5 | -0.2 | 40.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | total | 3-2 | 60.0 | 43.2 | 16.8 | +0.73 | 14.5 | 0.2 | 60.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | total | 3-1 | 75.0 | 43.2 | 31.8 | +1.73 | 43.2 | 0.75 | 50.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | total | 3-1 | 75.0 | 43.2 | 31.8 | +1.73 | 43.2 | 1.25 | 75.0 | keep collecting (4/30) |
| money_moving+sharp_gap | total | 3-4 | 42.9 | 47.1 | -4.2 | -1.27 | -18.2 | -0.14 | 42.9 | keep collecting (7/30) |
| follow_move+pin_move | total | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | total | 1-4 | 20.0 | 45.9 | -25.9 | -3.09 | -61.8 | 1.8 | 80.0 | keep collecting (5/30) |
| consensus_gap+money_level | total | 1-1 | 50.0 | 56.8 | -6.8 | -0.09 | -4.5 | 1.0 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | total | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | total | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_level | total | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_moving | total | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | total | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | total | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+rlm_ratio | total | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| follow_move+pin_value | total | 1-1 | 50.0 | 43.2 | 6.8 | -0.09 | -4.5 | -2.5 | 0.0 | keep collecting (2/30) |
| consensus_gap+pin_move | total | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+pin_value | total | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_move | total | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_value | total | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 24-62 | 27.9 | 40.4 | -12.5 | -26.23 | -30.5 |  |  | DROP: below break-even |
| pin_move | both | 55-67 | 45.1 | 49.3 | -4.2 | -15.52 | -12.7 |  |  | DROP: below break-even |
| money_delta | both | 34-41 | 45.3 | 41.2 | 4.1 | -3.72 | -5.0 |  |  | no edge shown yet |
| pin_rlm | both | 9-19 | 32.1 | 39.7 | -7.6 | -10.06 | -35.9 |  |  | keep collecting (28/30) |
| follow_move | both | 86-125 | 40.8 | 49.3 | -8.5 | -41.94 | -19.9 |  |  | DROP: below break-even |
| rlm_ratio | both | 17-38 | 30.9 | 40.2 | -9.3 | -21.78 | -39.6 |  |  | DROP: below break-even |
| money_level | both | 128-87 | 59.5 | 57.1 | 2.5 | +2.42 | 1.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 85-112 | 43.1 | 47.9 | -4.7 | -35.53 | -18.0 |  |  | DROP: below break-even |
| money_moving | both | 89-111 | 44.5 | 48.5 | -4.0 | -32.97 | -16.5 |  |  | DROP: below break-even |
| pin_value | both | 53-34 | 60.9 | 50.6 | 10.3 | +28.34 | 32.6 |  |  | PROMOTE: beats break-even and its own base rate |
| consensus_gap | both | 48-28 | 63.2 | 54.1 | 9.0 | +10.52 | 13.8 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+pin_move | both | 36-57 | 38.7 | 48.7 | -10.0 | -23.79 | -25.6 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 25-29 | 46.3 | 39.7 | 6.6 | +0.0 | 0.0 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 25-28 | 47.2 | 39.6 | 7.6 | +1.0 | 1.9 |  |  | no edge shown yet |
| money_moving+sharp_gap | both | 84-109 | 43.5 | 48.1 | -4.6 | -33.44 | -17.3 |  |  | DROP: below break-even |
| consensus_gap+money_level | both | 34-13 | 72.3 | 61.0 | 11.4 | +7.65 | 16.3 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+rlm_quiet | both | 24-62 | 27.9 | 40.4 | -12.5 | -26.23 | -30.5 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | both | 13-26 | 33.3 | 41.9 | -8.5 | -11.86 | -30.4 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 16-11 | 59.3 | 53.9 | 5.3 | +0.75 | 2.8 |  |  | keep collecting (27/30) |
| follow_move+money_level | both | 42-41 | 50.6 | 57.6 | -7.0 | -11.87 | -14.3 |  |  | no edge shown yet |
| money_level+money_moving | both | 64-56 | 53.3 | 54.2 | -0.9 | -6.82 | -5.7 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 60-55 | 52.2 | 53.8 | -1.6 | -7.38 | -6.4 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 17-17 | 50.0 | 53.2 | -3.2 | -1.95 | -5.7 |  |  | no edge shown yet |
| consensus_gap+pin_move | both | 9-5 | 64.3 | 51.8 | 12.5 | +3.88 | 27.7 |  |  | keep collecting (14/30) |
| consensus_gap+pin_value | both | 18-10 | 64.3 | 50.0 | 14.3 | +9.42 | 33.6 |  |  | keep collecting (28/30) |
| consensus_gap+sharp_gap | both | 16-17 | 48.5 | 52.0 | -3.5 | -2.09 | -6.3 |  |  | no edge shown yet |
| follow_move+money_moving | both | 37-63 | 37.0 | 48.3 | -11.3 | -33.3 | -33.3 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 14-10 | 58.3 | 52.3 | 6.1 | +12.24 | 51.0 |  |  | keep collecting (24/30) |
| follow_move+sharp_gap | both | 38-65 | 36.9 | 47.8 | -10.9 | -34.39 | -33.4 |  |  | DROP: below break-even |
| money_level+pin_move | both | 25-27 | 48.1 | 55.0 | -6.9 | -7.1 | -13.7 |  |  | no edge shown yet |
| money_level+pin_value | both | 20-15 | 57.1 | 53.2 | 3.9 | +2.7 | 7.7 |  |  | no edge shown yet |
| money_moving+pin_move | both | 22-29 | 43.1 | 48.1 | -5.0 | -9.62 | -18.9 |  |  | no edge shown yet |
| money_moving+pin_value | both | 17-18 | 48.6 | 49.5 | -0.9 | +0.71 | 2.0 |  |  | no edge shown yet |
| pin_move+pin_value | both | 16-13 | 55.2 | 52.5 | 2.7 | +1.2 | 4.1 |  |  | keep collecting (29/30) |
| pin_move+sharp_gap | both | 20-31 | 39.2 | 47.2 | -8.0 | -13.4 | -26.3 |  |  | DROP: below break-even |
| pin_value+sharp_gap | both | 16-17 | 48.5 | 49.0 | -0.6 | +0.8 | 2.4 |  |  | no edge shown yet |
| follow_move+money_delta | both | 17-30 | 36.2 | 42.3 | -6.2 | -14.2 | -30.2 |  |  | DROP: below break-even |
| money_delta+pin_move | both | 9-15 | 37.5 | 41.0 | -3.5 | -6.4 | -26.7 |  |  | keep collecting (24/30) |
| money_delta+rlm_quiet | both | 9-22 | 29.0 | 40.5 | -11.5 | -13.6 | -43.9 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | both | 17-38 | 30.9 | 40.2 | -9.3 | -21.78 | -39.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | both | 9-30 | 23.1 | 39.3 | -16.3 | -21.23 | -54.4 |  |  | INVERT candidate: wrong well beyond its base rate |
| money_moving+rlm_ratio | both | 17-36 | 32.1 | 40.5 | -8.5 | -19.78 | -37.3 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 6-28 | 17.6 | 38.0 | -20.4 | -22.41 | -65.9 |  |  | INVERT candidate: wrong well beyond its base rate |
| rlm_quiet+sharp_gap | both | 9-33 | 21.4 | 38.8 | -17.4 | -24.23 | -57.7 |  |  | INVERT candidate: wrong well beyond its base rate |
| rlm_ratio+sharp_gap | both | 17-38 | 30.9 | 40.2 | -9.3 | -21.78 | -39.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | both | 8-5 | 61.5 | 43.6 | 18.0 | +3.31 | 25.4 |  |  | keep collecting (13/30) |
| consensus_gap+rlm_quiet | both | 4-6 | 40.0 | 39.3 | 0.7 | -2.27 | -22.7 |  |  | keep collecting (10/30) |
| consensus_gap+rlm_ratio | both | 3-4 | 42.9 | 35.3 | 7.6 | -1.2 | -17.1 |  |  | keep collecting (7/30) |
| money_delta+rlm_ratio | both | 13-21 | 38.2 | 40.8 | -2.6 | -8.86 | -26.1 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 1-2 | 33.3 | 47.7 | -14.4 | -1.0 | -33.3 |  |  | keep collecting (3/30) |
| money_level+pin_rlm | both | 5-5 | 50.0 | 43.4 | 6.6 | -0.26 | -2.6 |  |  | keep collecting (10/30) |
| money_moving+pin_rlm | both | 9-18 | 33.3 | 40.0 | -6.7 | -9.06 | -33.5 |  |  | keep collecting (27/30) |
| pin_rlm+sharp_gap | both | 9-19 | 32.1 | 39.7 | -7.6 | -10.06 | -35.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | both | 9-8 | 52.9 | 44.4 | 8.5 | +0.42 | 2.5 |  |  | keep collecting (17/30) |
| consensus_gap+money_delta | both | 6-2 | 75.0 | 42.4 | 32.6 | +7.06 | 88.2 |  |  | keep collecting (8/30) |
| follow_move+pin_rlm | both | 9-16 | 36.0 | 38.7 | -2.7 | -7.06 | -28.2 |  |  | keep collecting (25/30) |
| money_delta+pin_rlm | both | 6-12 | 33.3 | 38.3 | -4.9 | -6.21 | -34.5 |  |  | keep collecting (18/30) |
| pin_move+pin_rlm | both | 8-15 | 34.8 | 39.8 | -5.0 | -7.4 | -32.2 |  |  | keep collecting (23/30) |
| pin_move+rlm_ratio | both | 8-14 | 36.4 | 39.7 | -3.3 | -6.4 | -29.1 |  |  | keep collecting (22/30) |
| pin_rlm+rlm_quiet | both | 3-11 | 21.4 | 38.4 | -17.0 | -8.14 | -58.1 |  |  | keep collecting (14/30) |
| pin_rlm+rlm_ratio | both | 9-16 | 36.0 | 38.7 | -2.7 | -7.06 | -28.2 |  |  | keep collecting (25/30) |
| money_delta+pin_value | both | 10-2 | 83.3 | 44.5 | 38.8 | +10.69 | 89.0 |  |  | keep collecting (12/30) |
| pin_value+rlm_quiet | both | 5-3 | 62.5 | 45.2 | 17.3 | +11.24 | 140.5 |  |  | keep collecting (8/30) |
| pin_value+rlm_ratio | both | 3-0 | 100.0 | 47.7 | 52.3 | +2.69 | 89.6 |  |  | keep collecting (3/30) |
| pin_rlm+pin_value | both | 1-1 | 50.0 | 43.2 | 6.8 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| rlm_quiet | moneyline | 8-26 | 23.5 | 32.1 | -8.6 | -5.12 | -15.1 |  |  | DROP: below break-even |
| rlm_quiet | spread | 4-7 | 36.4 | 54.3 | -18.0 | -3.28 | -29.8 |  |  | keep collecting (11/30) |
| rlm_quiet | total | 12-29 | 29.3 | 43.5 | -14.2 | -17.83 | -43.5 |  |  | DROP: below break-even |
| pin_move | moneyline | 15-14 | 51.7 | 46.9 | 4.8 | +0.89 | 3.1 |  |  | keep collecting (29/30) |
| pin_move | spread | 22-19 | 53.7 | 52.2 | 1.5 | +0.96 | 2.3 |  |  | no edge shown yet |
| pin_move | total | 18-34 | 34.6 | 48.4 | -13.8 | -17.37 | -33.4 |  |  | DROP: below break-even |
| money_delta | moneyline | 9-17 | 34.6 | 34.9 | -0.2 | -2.76 | -10.6 |  |  | keep collecting (26/30) |
| money_delta | spread | 4-3 | 57.1 | 49.0 | 8.1 | +0.71 | 10.1 |  |  | keep collecting (7/30) |
| money_delta | total | 21-21 | 50.0 | 43.8 | 6.2 | -1.67 | -4.0 |  |  | no edge shown yet |
| pin_rlm | moneyline | 3-9 | 25.0 | 35.1 | -10.1 | -5.64 | -47.0 |  |  | keep collecting (12/30) |
| pin_rlm | total | 6-10 | 37.5 | 43.2 | -5.7 | -4.42 | -27.6 |  |  | keep collecting (16/30) |
| follow_move | moneyline | 33-42 | 44.0 | 48.3 | -4.3 | -7.61 | -10.2 |  |  | no edge shown yet |
| follow_move | spread | 22-31 | 41.5 | 52.2 | -10.7 | -10.84 | -20.5 |  |  | DROP: below break-even |
| follow_move | total | 31-52 | 37.3 | 48.3 | -10.9 | -23.49 | -28.3 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 4-20 | 16.7 | 33.6 | -16.9 | -15.71 | -65.5 |  |  | keep collecting (24/30) |
| rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| rlm_ratio | total | 13-16 | 44.8 | 45.1 | -0.2 | -4.07 | -14.0 |  |  | keep collecting (29/30) |
| money_level | moneyline | 54-27 | 66.7 | 63.9 | 2.7 | -4.34 | -5.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 23-23 | 50.0 | 49.4 | 0.6 | -2.4 | -5.2 |  |  | no edge shown yet |
| money_level | total | 51-37 | 58.0 | 54.8 | 3.2 | +9.15 | 10.4 |  |  | no edge shown yet |
| sharp_gap | moneyline | 30-42 | 41.7 | 46.0 | -4.4 | -15.44 | -21.4 |  |  | DROP: below break-even |
| sharp_gap | spread | 19-28 | 40.4 | 47.5 | -7.1 | -11.01 | -23.4 |  |  | DROP: below break-even |
| sharp_gap | total | 36-42 | 46.2 | 49.8 | -3.7 | -9.08 | -11.6 |  |  | no edge shown yet |
| money_moving | moneyline | 33-39 | 45.8 | 47.5 | -1.7 | -11.75 | -16.3 |  |  | no edge shown yet |
| money_moving | spread | 19-28 | 40.4 | 47.5 | -7.1 | -11.01 | -23.4 |  |  | DROP: below break-even |
| money_moving | total | 37-44 | 45.7 | 49.9 | -4.2 | -10.21 | -12.6 |  |  | no edge shown yet |
| pin_value | moneyline | 4-1 | 80.0 | 46.4 | 33.6 | +18.09 | 361.7 |  |  | keep collecting (5/30) |
| pin_value | spread | 24-12 | 66.7 | 49.2 | 17.4 | +8.79 | 24.4 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_value | total | 25-21 | 54.3 | 52.1 | 2.3 | +1.47 | 3.2 |  |  | no edge shown yet |
| consensus_gap | moneyline | 25-15 | 62.5 | 57.2 | 5.3 | +3.31 | 8.3 |  |  | no edge shown yet |
| consensus_gap | spread | 10-5 | 66.7 | 47.7 | 18.9 | +3.6 | 24.0 |  |  | keep collecting (15/30) |
| consensus_gap | total | 13-8 | 61.9 | 52.9 | 9.0 | +3.6 | 17.2 |  |  | keep collecting (21/30) |
| consensus_gap+money_level | moneyline | 20-5 | 80.0 | 67.9 | 12.1 | +3.28 | 13.1 |  |  | keep collecting (25/30) |
| follow_move+pin_move | moneyline | 11-14 | 44.0 | 46.4 | -2.4 | -3.85 | -15.4 |  |  | keep collecting (25/30) |
| follow_move+rlm_quiet | moneyline | 8-26 | 23.5 | 32.1 | -8.6 | -5.12 | -15.1 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | moneyline | 4-8 | 33.3 | 32.1 | 1.2 | -2.26 | -18.8 |  |  | keep collecting (12/30) |
| consensus_gap+follow_move | moneyline | 10-6 | 62.5 | 54.5 | 8.0 | +0.35 | 2.2 |  |  | keep collecting (16/30) |
| follow_move+money_level | moneyline | 21-14 | 60.0 | 63.8 | -3.8 | -4.12 | -11.8 |  |  | no edge shown yet |
| money_moving+sharp_gap | moneyline | 30-39 | 43.5 | 46.6 | -3.1 | -12.44 | -18.0 |  |  | no edge shown yet |
| follow_move+money_moving | moneyline | 15-22 | 40.5 | 46.6 | -6.1 | -12.34 | -33.3 |  |  | no edge shown yet |
| follow_move+sharp_gap | moneyline | 15-25 | 37.5 | 45.5 | -8.0 | -15.34 | -38.3 |  |  | DROP: below break-even |
| money_level+money_moving | moneyline | 25-15 | 62.5 | 59.8 | 2.7 | -1.06 | -2.6 |  |  | no edge shown yet |
| money_level+sharp_gap | moneyline | 22-15 | 59.5 | 59.2 | 0.3 | -1.75 | -4.7 |  |  | no edge shown yet |
| follow_move+rlm_ratio | moneyline | 4-20 | 16.7 | 33.6 | -16.9 | -15.71 | -65.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | moneyline | 2-14 | 12.5 | 32.1 | -19.6 | -11.68 | -73.0 |  |  | keep collecting (16/30) |
| money_moving+rlm_ratio | moneyline | 4-18 | 18.2 | 33.7 | -15.5 | -13.71 | -62.3 |  |  | keep collecting (22/30) |
| rlm_quiet+rlm_ratio | moneyline | 1-16 | 5.9 | 32.1 | -26.2 | -15.0 | -88.2 |  |  | keep collecting (17/30) |
| rlm_quiet+sharp_gap | moneyline | 2-17 | 10.5 | 32.1 | -21.6 | -14.68 | -77.3 |  |  | keep collecting (19/30) |
| rlm_ratio+sharp_gap | moneyline | 4-20 | 16.7 | 33.6 | -16.9 | -15.71 | -65.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 10-8 | 55.6 | 56.0 | -0.4 | +0.78 | 4.3 |  |  | keep collecting (18/30) |
| consensus_gap+rlm_quiet | moneyline | 1-5 | 16.7 | 32.1 | -15.4 | -4.0 | -66.7 |  |  | keep collecting (6/30) |
| consensus_gap+rlm_ratio | moneyline | 1-4 | 20.0 | 32.1 | -12.1 | -3.0 | -60.0 |  |  | keep collecting (5/30) |
| consensus_gap+sharp_gap | moneyline | 9-9 | 50.0 | 54.0 | -4.0 | -0.36 | -2.0 |  |  | keep collecting (18/30) |
| consensus_gap+pin_rlm | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | +0.0 | 0.0 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | moneyline | 1-2 | 33.3 | 44.0 | -10.7 | -0.98 | -32.7 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | moneyline | 3-8 | 27.3 | 35.4 | -8.1 | -4.64 | -42.2 |  |  | keep collecting (11/30) |
| pin_rlm+sharp_gap | moneyline | 3-9 | 25.0 | 35.1 | -10.1 | -5.64 | -47.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +5.38 | 269.2 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | moneyline | 2-3 | 40.0 | 39.3 | 0.7 | -1.05 | -21.1 |  |  | keep collecting (5/30) |
| consensus_gap+pin_move | moneyline | 6-1 | 85.7 | 52.6 | 33.2 | +5.23 | 74.7 |  |  | keep collecting (7/30) |
| money_level+pin_move | moneyline | 9-5 | 64.3 | 62.8 | 1.5 | +0.35 | 2.5 |  |  | keep collecting (14/30) |
| consensus_gap+money_delta | moneyline | 3-2 | 60.0 | 39.3 | 20.7 | +4.35 | 86.9 |  |  | keep collecting (5/30) |
| follow_move+money_delta | moneyline | 3-12 | 20.0 | 36.9 | -16.9 | -9.13 | -60.9 |  |  | keep collecting (15/30) |
| follow_move+pin_rlm | moneyline | 3-7 | 30.0 | 32.1 | -2.1 | -3.64 | -36.4 |  |  | keep collecting (10/30) |
| money_delta+money_moving | moneyline | 8-16 | 33.3 | 33.6 | -0.3 | -2.61 | -10.9 |  |  | keep collecting (24/30) |
| money_delta+pin_move | moneyline | 2-4 | 33.3 | 32.1 | 1.2 | -1.98 | -33.0 |  |  | keep collecting (6/30) |
| money_delta+pin_rlm | moneyline | 2-6 | 25.0 | 32.1 | -7.1 | -3.98 | -49.8 |  |  | keep collecting (8/30) |
| money_delta+rlm_quiet | moneyline | 1-9 | 10.0 | 32.1 | -22.1 | -8.0 | -80.0 |  |  | keep collecting (10/30) |
| money_delta+rlm_ratio | moneyline | 2-11 | 15.4 | 34.9 | -19.5 | -8.98 | -69.1 |  |  | keep collecting (13/30) |
| money_delta+sharp_gap | moneyline | 8-16 | 33.3 | 33.6 | -0.3 | -2.61 | -10.9 |  |  | keep collecting (24/30) |
| money_moving+pin_move | moneyline | 5-4 | 55.6 | 44.0 | 11.5 | -0.06 | -0.7 |  |  | keep collecting (9/30) |
| pin_move+pin_rlm | moneyline | 2-5 | 28.6 | 32.1 | -3.5 | -2.98 | -42.6 |  |  | keep collecting (7/30) |
| pin_move+rlm_ratio | moneyline | 2-5 | 28.6 | 32.1 | -3.5 | -2.98 | -42.6 |  |  | keep collecting (7/30) |
| pin_move+sharp_gap | moneyline | 5-6 | 45.5 | 41.9 | 3.6 | -2.06 | -18.8 |  |  | keep collecting (11/30) |
| pin_rlm+rlm_quiet | moneyline | 1-5 | 16.7 | 32.1 | -15.4 | -4.0 | -66.7 |  |  | keep collecting (6/30) |
| pin_rlm+rlm_ratio | moneyline | 3-7 | 30.0 | 32.1 | -2.1 | -3.64 | -36.4 |  |  | keep collecting (10/30) |
| follow_move+pin_value | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | +9.6 | 480.0 |  |  | keep collecting (2/30) |
| pin_value+rlm_quiet | moneyline | 1-0 | 100.0 | 32.1 | 67.9 | +10.6 | 1060.0 |  |  | keep collecting (1/30) |
| money_delta+money_level | moneyline | 2-2 | 50.0 | 41.0 | 9.0 | +0.74 | 18.5 |  |  | keep collecting (4/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 67.9 | -67.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_move+pin_value | moneyline | 0-1 | 0.0 | 67.9 | -67.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta+pin_value | moneyline | 1-0 | 100.0 | 32.1 | 67.9 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 1-0 | 100.0 | 32.1 | 67.9 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 1-0 | 100.0 | 32.1 | 67.9 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| follow_move+pin_move | spread | 11-15 | 42.3 | 52.6 | -10.3 | -5.01 | -19.3 |  |  | keep collecting (26/30) |
| money_moving+sharp_gap | spread | 19-28 | 40.4 | 47.5 | -7.1 | -11.01 | -23.4 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 4-7 | 36.4 | 54.3 | -18.0 | -3.28 | -29.8 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | spread | 12-17 | 41.4 | 47.4 | -6.0 | -6.38 | -22.0 |  |  | keep collecting (29/30) |
| money_level+sharp_gap | spread | 12-17 | 41.4 | 47.4 | -6.0 | -6.38 | -22.0 |  |  | keep collecting (29/30) |
| pin_move+rlm_quiet | spread | 2-4 | 33.3 | 54.5 | -21.2 | -2.18 | -36.4 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 8-5 | 61.5 | 47.4 | 14.2 | +1.92 | 14.8 |  |  | keep collecting (13/30) |
| follow_move+money_level | spread | 4-6 | 40.0 | 52.7 | -12.7 | -2.32 | -23.2 |  |  | keep collecting (10/30) |
| follow_move+money_moving | spread | 3-9 | 25.0 | 52.3 | -27.3 | -6.35 | -52.9 |  |  | keep collecting (12/30) |
| follow_move+sharp_gap | spread | 3-9 | 25.0 | 52.3 | -27.3 | -6.35 | -52.9 |  |  | keep collecting (12/30) |
| money_level+pin_move | spread | 5-7 | 41.7 | 51.1 | -9.5 | -2.5 | -20.8 |  |  | keep collecting (12/30) |
| money_moving+pin_move | spread | 6-7 | 46.2 | 50.5 | -4.4 | -1.65 | -12.7 |  |  | keep collecting (13/30) |
| pin_move+sharp_gap | spread | 6-7 | 46.2 | 50.5 | -4.4 | -1.65 | -12.7 |  |  | keep collecting (13/30) |
| money_delta+money_level | spread | 1-0 | 100.0 | 43.2 | 56.8 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+money_moving | spread | 3-1 | 75.0 | 46.6 | 28.4 | +1.73 | 43.2 |  |  | keep collecting (4/30) |
| money_delta+sharp_gap | spread | 3-1 | 75.0 | 46.6 | 28.4 | +1.73 | 43.2 |  |  | keep collecting (4/30) |
| consensus_gap+money_level | spread | 3-3 | 50.0 | 45.5 | 4.5 | -0.41 | -6.9 |  |  | keep collecting (6/30) |
| consensus_gap+money_moving | spread | 2-3 | 40.0 | 45.9 | -5.9 | -1.21 | -24.3 |  |  | keep collecting (5/30) |
| consensus_gap+sharp_gap | spread | 2-3 | 40.0 | 45.9 | -5.9 | -1.21 | -24.3 |  |  | keep collecting (5/30) |
| money_level+pin_value | spread | 6-4 | 60.0 | 45.9 | 14.1 | +1.16 | 11.6 |  |  | keep collecting (10/30) |
| money_moving+pin_value | spread | 6-7 | 46.2 | 47.4 | -1.2 | -1.81 | -13.9 |  |  | keep collecting (13/30) |
| pin_value+sharp_gap | spread | 6-7 | 46.2 | 47.4 | -1.2 | -1.81 | -13.9 |  |  | keep collecting (13/30) |
| follow_move+money_delta | spread | 1-2 | 33.3 | 52.3 | -18.9 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| follow_move+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | spread | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 8-1 | 88.9 | 53.8 | 35.1 | +6.13 | 68.1 |  |  | keep collecting (9/30) |
| pin_move+pin_value | spread | 12-3 | 80.0 | 51.4 | 28.6 | +7.56 | 50.4 |  |  | keep collecting (15/30) |
| consensus_gap+pin_move | spread | 3-2 | 60.0 | 51.4 | 8.6 | +0.65 | 13.0 |  |  | keep collecting (5/30) |
| consensus_gap+follow_move | spread | 2-1 | 66.7 | 56.8 | 9.8 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| consensus_gap+rlm_quiet | spread | 2-0 | 100.0 | 56.8 | 43.2 | +1.82 | 90.9 |  |  | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 2-0 | 100.0 | 56.8 | 43.2 | +1.82 | 90.9 |  |  | keep collecting (2/30) |
| money_delta+rlm_quiet | spread | 1-1 | 50.0 | 56.8 | -6.8 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_moving+rlm_quiet | spread | 1-2 | 33.3 | 52.3 | -18.9 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| rlm_quiet+rlm_ratio | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_quiet+sharp_gap | spread | 1-2 | 33.3 | 52.3 | -18.9 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+pin_move | spread | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+pin_value | spread | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+money_moving | total | 14-12 | 53.8 | 44.2 | 9.6 | +0.89 | 3.4 |  |  | keep collecting (26/30) |
| money_delta+sharp_gap | total | 14-11 | 56.0 | 44.3 | 11.7 | +1.89 | 7.5 |  |  | keep collecting (25/30) |
| money_moving+sharp_gap | total | 35-42 | 45.5 | 49.7 | -4.3 | -9.99 | -13.0 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 12-29 | 29.3 | 43.5 | -14.2 | -17.83 | -43.5 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+follow_move | total | 4-4 | 50.0 | 51.7 | -1.7 | -0.42 | -5.2 |  |  | keep collecting (8/30) |
| consensus_gap+money_level | total | 11-5 | 68.8 | 56.0 | 12.8 | +4.79 | 29.9 |  |  | keep collecting (16/30) |
| consensus_gap+money_moving | total | 5-6 | 45.5 | 51.9 | -6.4 | -1.51 | -13.7 |  |  | keep collecting (11/30) |
| consensus_gap+pin_move | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+pin_value | total | 8-5 | 61.5 | 52.6 | 8.9 | +2.11 | 16.3 |  |  | keep collecting (13/30) |
| consensus_gap+sharp_gap | total | 5-5 | 50.0 | 51.4 | -1.4 | -0.51 | -5.1 |  |  | keep collecting (10/30) |
| follow_move+money_level | total | 17-21 | 44.7 | 53.2 | -8.5 | -5.43 | -14.3 |  |  | no edge shown yet |
| follow_move+money_moving | total | 19-32 | 37.3 | 48.5 | -11.3 | -14.61 | -28.6 |  |  | DROP: below break-even |
| follow_move+pin_move | total | 14-28 | 33.3 | 47.7 | -14.4 | -14.93 | -35.5 |  |  | DROP: below break-even |
| follow_move+pin_value | total | 5-8 | 38.5 | 51.6 | -13.1 | -3.49 | -26.8 |  |  | keep collecting (13/30) |
| follow_move+sharp_gap | total | 20-31 | 39.2 | 48.5 | -9.3 | -12.7 | -24.9 |  |  | DROP: below break-even |
| money_level+money_moving | total | 27-24 | 52.9 | 53.6 | -0.7 | +0.61 | 1.2 |  |  | no edge shown yet |
| money_level+pin_move | total | 11-15 | 42.3 | 52.6 | -10.3 | -4.95 | -19.0 |  |  | keep collecting (26/30) |
| money_level+pin_value | total | 14-10 | 58.3 | 55.7 | 2.7 | +2.53 | 10.6 |  |  | keep collecting (24/30) |
| money_level+sharp_gap | total | 26-23 | 53.1 | 53.5 | -0.4 | +0.74 | 1.5 |  |  | no edge shown yet |
| money_moving+pin_move | total | 11-18 | 37.9 | 48.4 | -10.4 | -7.91 | -27.3 |  |  | keep collecting (29/30) |
| money_moving+pin_value | total | 10-11 | 47.6 | 51.6 | -4.0 | -1.98 | -9.4 |  |  | keep collecting (21/30) |
| pin_move+pin_value | total | 4-9 | 30.8 | 52.6 | -21.9 | -5.36 | -41.2 |  |  | keep collecting (13/30) |
| pin_move+sharp_gap | total | 9-18 | 33.3 | 47.7 | -14.4 | -9.69 | -35.9 |  |  | keep collecting (27/30) |
| pin_value+sharp_gap | total | 9-10 | 47.4 | 51.1 | -3.7 | -1.89 | -10.0 |  |  | keep collecting (19/30) |
| follow_move+money_delta | total | 13-16 | 44.8 | 44.1 | 0.7 | -3.98 | -13.7 |  |  | keep collecting (29/30) |
| money_delta+pin_move | total | 6-11 | 35.3 | 43.2 | -7.9 | -5.33 | -31.4 |  |  | keep collecting (17/30) |
| money_delta+rlm_quiet | total | 7-12 | 36.8 | 43.2 | -6.3 | -5.51 | -29.0 |  |  | keep collecting (19/30) |
| pin_move+rlm_quiet | total | 7-14 | 33.3 | 43.8 | -10.5 | -7.42 | -35.3 |  |  | keep collecting (21/30) |
| follow_move+rlm_ratio | total | 13-16 | 44.8 | 45.1 | -0.2 | -4.07 | -14.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | total | 11-9 | 55.0 | 44.5 | 10.5 | +1.12 | 5.6 |  |  | keep collecting (20/30) |
| money_moving+rlm_quiet | total | 6-14 | 30.0 | 43.2 | -13.2 | -8.46 | -42.3 |  |  | keep collecting (20/30) |
| money_moving+rlm_ratio | total | 13-16 | 44.8 | 45.1 | -0.2 | -4.07 | -14.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 5-11 | 31.2 | 43.2 | -11.9 | -6.41 | -40.1 |  |  | keep collecting (16/30) |
| rlm_quiet+sharp_gap | total | 6-14 | 30.0 | 43.2 | -13.2 | -8.46 | -42.3 |  |  | keep collecting (20/30) |
| rlm_ratio+sharp_gap | total | 13-16 | 44.8 | 45.1 | -0.2 | -4.07 | -14.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | total | 2-0 | 100.0 | 43.2 | 56.8 | +1.8 | 90.1 |  |  | keep collecting (2/30) |
| consensus_gap+rlm_quiet | total | 1-1 | 50.0 | 43.2 | 6.8 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| consensus_gap+rlm_ratio | total | 2-0 | 100.0 | 43.2 | 56.8 | +1.8 | 90.1 |  |  | keep collecting (2/30) |
| money_delta+pin_value | total | 8-2 | 80.0 | 44.5 | 35.5 | +5.28 | 52.8 |  |  | keep collecting (10/30) |
| pin_value+rlm_quiet | total | 2-3 | 40.0 | 43.2 | -3.2 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| pin_value+rlm_ratio | total | 3-0 | 100.0 | 47.7 | 52.3 | +2.69 | 89.6 |  |  | keep collecting (3/30) |
| follow_move+pin_rlm | total | 6-9 | 40.0 | 43.2 | -3.2 | -3.42 | -22.8 |  |  | keep collecting (15/30) |
| money_delta+money_level | total | 5-3 | 62.5 | 44.9 | 17.6 | +1.66 | 20.7 |  |  | keep collecting (8/30) |
| money_delta+pin_rlm | total | 4-6 | 40.0 | 43.2 | -3.2 | -2.24 | -22.4 |  |  | keep collecting (10/30) |
| money_level+pin_rlm | total | 4-3 | 57.1 | 43.2 | 14.0 | +0.72 | 10.3 |  |  | keep collecting (7/30) |
| money_level+rlm_ratio | total | 7-5 | 58.3 | 46.6 | 11.7 | +1.48 | 12.3 |  |  | keep collecting (12/30) |
| money_moving+pin_rlm | total | 6-10 | 37.5 | 43.2 | -5.7 | -4.42 | -27.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | total | 6-10 | 37.5 | 43.2 | -5.7 | -4.42 | -27.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 6-9 | 40.0 | 43.2 | -3.2 | -3.42 | -22.8 |  |  | keep collecting (15/30) |
| pin_rlm+rlm_ratio | total | 6-9 | 40.0 | 43.2 | -3.2 | -3.42 | -22.8 |  |  | keep collecting (15/30) |
| pin_rlm+sharp_gap | total | 6-10 | 37.5 | 43.2 | -5.7 | -4.42 | -27.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | total | 2-6 | 25.0 | 43.2 | -18.2 | -4.14 | -51.7 |  |  | keep collecting (8/30) |
| consensus_gap+pin_rlm | total | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+pin_value | total | 1-1 | 50.0 | 43.2 | 6.8 | -0.09 | -4.5 |  |  | keep collecting (2/30) |

# FIT (in-sample — this is the hypothesis)

Games before 2026-11-21. The engine was built by looking at these, so a strong record here is expected and proves nothing. n=684 games.

## EARLY  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 30-36 | 45.5 | 35.9 | 9.6 | +10.59 | 16.0 | 0.18 | 43.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move | both | 5-9 | 35.7 | 48.2 | -12.5 | -5.1 | -36.4 | 0.22 | 50.0 | keep collecting (14/30) |
| money_delta | both | 10-7 | 58.8 | 41.8 | 17.0 | +4.43 | 26.1 | -0.22 | 29.4 | keep collecting (17/30) |
| pin_rlm | both | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | both | 474-402 | 54.1 | 52.4 | 1.7 | -44.48 | -5.1 | 0.19 | 42.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | both | 29-17 | 63.0 | 38.5 | 24.5 | +20.54 | 44.6 | 0.42 | 52.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | both | 169-109 | 60.8 | 59.0 | 1.8 | -11.33 | -4.1 | -0.12 | 39.2 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 143-120 | 54.4 | 48.4 | 6.0 | +19.09 | 7.3 | 0.29 | 43.3 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | both | 102-80 | 56.0 | 51.3 | 4.7 | +1.19 | 0.7 | 0.04 | 41.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | both | 50-49 | 50.5 | 48.3 | 2.2 | -4.6 | -4.6 | 0.09 | 37.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.3 | -31.3 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 219-290 | 43.0 | 47.2 | -4.2 | -61.46 | -12.1 | 0.39 | 45.0 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | both | 32-28 | 53.3 | 63.6 | -10.3 | -9.71 | -16.2 | 0.33 | 48.3 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | both | 17-23 | 42.5 | 46.7 | -4.2 | -6.42 | -16.1 | 0.25 | 42.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_value | both | 20-28 | 41.7 | 46.6 | -4.9 | -10.7 | -22.3 | 0.38 | 47.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_quiet | both | 30-36 | 45.5 | 35.9 | 9.6 | +10.59 | 16.0 | 0.18 | 43.9 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 29-17 | 63.0 | 38.5 | 24.5 | +20.54 | 44.6 | 0.42 | 52.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 75-37 | 67.0 | 50.1 | 16.9 | +25.31 | 22.6 | 0.37 | 48.2 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 64-39 | 62.1 | 58.2 | 4.0 | +0.13 | 0.1 | -0.17 | 46.6 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 11-9 | 55.0 | 49.8 | 5.2 | +0.81 | 4.0 | 0.4 | 45.0 | keep collecting (20/30) |
| money_moving+pin_value | both | 9-6 | 60.0 | 49.8 | 10.2 | +1.88 | 12.5 | 0.27 | 33.3 | keep collecting (15/30) |
| rlm_quiet+rlm_ratio | both | 16-10 | 61.5 | 35.7 | 25.9 | +14.25 | 54.8 | -0.07 | 50.0 | keep collecting (26/30) |
| rlm_quiet+sharp_gap | both | 18-13 | 58.1 | 35.8 | 22.3 | +13.06 | 42.1 | -0.08 | 48.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | both | 29-17 | 63.0 | 38.5 | 24.5 | +20.54 | 44.6 | 0.42 | 52.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 97-60 | 61.8 | 55.7 | 6.1 | +4.17 | 2.7 | 0.14 | 43.3 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 60-47 | 56.1 | 48.8 | 7.2 | +6.0 | 5.6 | 0.19 | 44.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_level | both | 3-2 | 60.0 | 45.8 | 14.2 | +1.46 | 29.2 | 1.16 | 60.0 | keep collecting (5/30) |
| money_delta+money_moving | both | 9-7 | 56.2 | 41.3 | 14.9 | +3.53 | 22.0 | -0.23 | 31.2 | keep collecting (16/30) |
| money_delta+pin_value | both | 3-1 | 75.0 | 50.0 | 25.0 | +1.61 | 40.3 | 0.0 | 25.0 | keep collecting (4/30) |
| money_delta+sharp_gap | both | 7-5 | 58.3 | 40.5 | 17.8 | +3.78 | 31.5 | -0.31 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | both | 13-8 | 61.9 | 48.8 | 13.1 | +3.66 | 17.4 | -0.18 | 33.3 | keep collecting (21/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 49.7 | -49.7 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 32-41 | 43.8 | 51.2 | -7.3 | -15.02 | -20.6 | 0.72 | 54.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_quiet | both | 4-7 | 36.4 | 37.2 | -0.8 | -2.99 | -27.1 | 0.95 | 72.7 | keep collecting (11/30) |
| follow_move+pin_value | both | 20-18 | 52.6 | 48.9 | 3.8 | -0.59 | -1.6 | -0.11 | 28.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 42.2 | -25.5 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 26-45 | 36.6 | 45.5 | -8.9 | -10.29 | -14.5 | 0.88 | 49.3 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | both | 91-44 | 67.4 | 60.2 | 7.2 | +1.24 | 0.9 | 0.0 | 43.7 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 11-7 | 61.1 | 41.4 | 19.7 | +4.43 | 24.6 | 1.22 | 61.1 | keep collecting (18/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 44.2 | 5.8 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 53-28 | 65.4 | 53.2 | 12.2 | +10.8 | 13.3 | 0.3 | 51.9 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 3-0 | 100.0 | 49.1 | 50.9 | +2.61 | 87.1 | 0.0 | 0.0 | keep collecting (3/30) |
| follow_move+money_delta | both | 5-3 | 62.5 | 41.0 | 21.5 | +3.95 | 49.4 | 0.05 | 37.5 | keep collecting (8/30) |
| money_delta+rlm_quiet | both | 2-2 | 50.0 | 37.9 | 12.1 | +1.53 | 38.3 | -2.1 | 0.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | both | 11-10 | 52.4 | 36.5 | 15.9 | +4.87 | 23.2 | 0.3 | 42.9 | keep collecting (21/30) |
| money_moving+rlm_ratio | both | 12-7 | 63.2 | 41.5 | 21.7 | +7.66 | 40.3 | 0.21 | 47.4 | keep collecting (19/30) |
| consensus_gap+rlm_ratio | both | 4-4 | 50.0 | 38.5 | 11.5 | +0.09 | 1.1 | 0.69 | 62.5 | keep collecting (8/30) |
| pin_move+pin_value | both | 1-4 | 20.0 | 49.1 | -29.1 | -3.09 | -61.8 | 0.2 | 20.0 | keep collecting (5/30) |
| follow_move+pin_move | both | 5-3 | 62.5 | 52.2 | 10.3 | +0.9 | 11.2 | 0.42 | 62.5 | keep collecting (8/30) |
| consensus_gap+pin_move | both | 0-5 | 0.0 | 44.5 | -44.5 | -5.0 | -100.0 | 0.26 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | both | 2-2 | 50.0 | 55.8 | -5.8 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 26.6 | 23.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 26.6 | 23.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | both | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.2 | -51.2 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 50.3 | -50.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-1 | 66.7 | 49.9 | 16.8 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 2-1 | 66.7 | 34.5 | 32.1 | +3.34 | 111.3 | 0.87 | 66.7 | keep collecting (3/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 16-24 | 40.0 | 26.6 | 13.4 | +9.89 | 24.7 | -0.05 | 45.0 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 11-10 | 52.4 | 50.2 | 2.2 | +0.04 | 0.2 | 0.86 | 52.4 | keep collecting (21/30) |
| pin_move | moneyline | 2-3 | 40.0 | 45.3 | -5.3 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-4 | 20.0 | 49.6 | -29.6 | -3.09 | -61.8 | 0.4 | 40.0 | keep collecting (5/30) |
| pin_move | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.14 | -3.5 | 0.25 | 50.0 | keep collecting (4/30) |
| money_delta | moneyline | 2-4 | 33.3 | 26.6 | 6.7 | +0.34 | 5.7 | -1.45 | 33.3 | keep collecting (6/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 7-2 | 77.8 | 50.2 | 27.6 | +4.26 | 47.4 | 0.44 | 22.2 | keep collecting (9/30) |
| pin_rlm | moneyline | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | moneyline | 195-126 | 60.7 | 56.9 | 3.8 | -24.09 | -7.5 | 0.19 | 46.1 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 128-140 | 47.8 | 49.7 | -1.9 | -22.21 | -8.3 | 0.02 | 34.3 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | total | 151-136 | 52.6 | 50.0 | 2.6 | +1.82 | 0.6 | 0.34 | 44.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | moneyline | 13-10 | 56.5 | 26.6 | 29.9 | +12.71 | 55.2 | 0.45 | 60.9 | keep collecting (23/30) |
| rlm_ratio | spread | 3-2 | 60.0 | 51.3 | 8.7 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 13-5 | 72.2 | 50.2 | 22.0 | +6.99 | 38.8 | 0.67 | 55.6 | keep collecting (18/30) |
| money_level | moneyline | 96-39 | 71.1 | 68.9 | 2.2 | -7.5 | -5.6 | -0.25 | 44.4 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-17 | 50.0 | 49.3 | 0.7 | -1.69 | -5.0 | 0.88 | 50.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | total | 56-53 | 51.4 | 49.9 | 1.5 | -2.14 | -2.0 | -0.28 | 29.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 61-61 | 50.0 | 46.6 | 3.4 | +3.59 | 2.9 | 0.32 | 50.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | spread | 20-14 | 58.8 | 49.8 | 9.1 | +4.0 | 11.8 | 0.65 | 38.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 62-45 | 57.9 | 50.1 | 7.9 | +11.5 | 10.7 | 0.13 | 37.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | moneyline | 44-41 | 51.8 | 53.0 | -1.3 | -12.4 | -14.6 | -0.15 | 47.1 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | spread | 18-5 | 78.3 | 49.2 | 29.1 | +11.18 | 48.6 | 0.3 | 43.5 | keep collecting (23/30) |
| money_moving | total | 40-34 | 54.1 | 50.0 | 4.0 | +2.41 | 3.3 | 0.18 | 35.1 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | moneyline | 2-6 | 25.0 | 32.5 | -7.5 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| pin_value | spread | 25-20 | 55.6 | 49.5 | 6.1 | +1.99 | 4.4 | 0.24 | 37.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 23-23 | 50.0 | 50.0 | 0.0 | -2.28 | -5.0 | -0.02 | 34.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.1 | -18.8 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 89-164 | 35.2 | 44.7 | -9.6 | -50.6 | -20.0 | 0.15 | 42.3 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 64-61 | 51.2 | 49.2 | 2.0 | -5.08 | -4.1 | 0.34 | 40.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap | total | 66-65 | 50.4 | 50.0 | 0.4 | -5.78 | -4.4 | 0.91 | 55.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | moneyline | 46-19 | 70.8 | 64.0 | 6.7 | -1.1 | -1.7 | 0.04 | 53.8 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+follow_move | moneyline | 11-22 | 33.3 | 53.5 | -20.2 | -14.69 | -44.5 | 0.2 | 54.5 | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 32.5 | -7.5 | -4.31 | -53.8 | -0.08 | 50.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| consensus_gap+rlm_quiet | moneyline | 1-5 | 16.7 | 26.6 | -10.0 | -3.68 | -61.3 | 1.07 | 83.3 | keep collecting (6/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.2 | -8.9 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 16-24 | 40.0 | 26.6 | 13.4 | +9.89 | 24.7 | -0.05 | 45.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 30-13 | 69.8 | 70.1 | -0.3 | -4.91 | -11.4 | -0.67 | 51.2 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 26.6 | -26.6 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 15-36 | 29.4 | 44.0 | -14.6 | -11.03 | -21.6 | 0.91 | 51.0 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | moneyline | 58-16 | 78.4 | 68.9 | 9.4 | -0.74 | -1.0 | -0.27 | 45.9 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 28-12 | 70.0 | 57.0 | 13.0 | +3.92 | 9.8 | 0.08 | 55.0 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 23-19 | 54.8 | 70.0 | -15.3 | -8.55 | -20.4 | 0.09 | 47.6 | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+sharp_gap | moneyline | 36-17 | 67.9 | 50.4 | 17.5 | +9.81 | 18.5 | 0.24 | 54.7 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 22-25 | 46.8 | 47.5 | -0.7 | -6.54 | -13.9 | 0.03 | 53.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | moneyline | 8-21 | 27.6 | 46.0 | -18.4 | -12.26 | -42.3 | 0.24 | 48.3 | keep collecting (29/30) |
| follow_move+rlm_ratio | moneyline | 13-10 | 56.5 | 26.6 | 29.9 | +12.71 | 55.2 | 0.45 | 60.9 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 9-7 | 56.2 | 26.6 | 29.6 | +10.84 | 67.8 | -0.23 | 50.0 | keep collecting (16/30) |
| rlm_quiet+sharp_gap | moneyline | 9-10 | 47.4 | 26.6 | 20.7 | +7.84 | 41.3 | -0.4 | 47.4 | keep collecting (19/30) |
| rlm_ratio+sharp_gap | moneyline | 13-10 | 56.5 | 26.6 | 29.9 | +12.71 | 55.2 | 0.45 | 60.9 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 26.6 | -1.6 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 5-7 | 41.7 | 26.6 | 15.0 | +2.49 | 20.8 | 0.44 | 50.0 | keep collecting (12/30) |
| money_moving+rlm_ratio | moneyline | 4-3 | 57.1 | 26.6 | 30.5 | +4.22 | 60.3 | 0.27 | 57.1 | keep collecting (7/30) |
| money_delta+money_moving | moneyline | 2-4 | 33.3 | 26.6 | 6.7 | +0.34 | 5.7 | -1.45 | 33.3 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-3 | 40.0 | 26.6 | 13.4 | +1.34 | 26.8 | -1.74 | 40.0 | keep collecting (5/30) |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 42.2 | -42.2 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-1 | 66.7 | 57.8 | 8.9 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | moneyline | 2-1 | 66.7 | 57.8 | 8.9 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-1 | 50.0 | 26.6 | 23.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-1 | 50.0 | 26.6 | 23.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | moneyline | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.13 | 56.5 | -0.1 | 50.0 | keep collecting (2/30) |
| money_level+rlm_ratio | moneyline | 4-3 | 57.1 | 26.6 | 30.5 | +1.87 | 26.7 | 2.0 | 85.7 | keep collecting (7/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 26.6 | 40.0 | +3.34 | 111.3 | -1.53 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 1-1 | 50.0 | 26.6 | 23.4 | +1.7 | 85.0 | -4.2 | 0.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 26.6 | 73.4 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-0 | 100.0 | 26.6 | 73.4 | +1.64 | 164.0 | 3.8 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 47.9 | -2.4 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 47.9 | 35.5 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 11-8 | 57.9 | 48.8 | 9.1 | +1.43 | 7.6 | 0.47 | 47.4 | keep collecting (19/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.3 | 8.7 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 48.9 | 13.6 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 10-5 | 66.7 | 48.7 | 17.9 | +4.12 | 27.5 | 0.93 | 66.7 | keep collecting (15/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 49.1 | -6.2 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 4-2 | 66.7 | 49.3 | 17.4 | +1.41 | 23.5 | 0.5 | 50.0 | keep collecting (6/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 51.3 | 8.7 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 52.1 | -52.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 52.1 | -52.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-11 | 56.0 | 49.2 | 6.8 | +1.62 | 6.5 | 1.0 | 44.0 | keep collecting (25/30) |
| money_moving+sharp_gap | spread | 10-3 | 76.9 | 49.2 | 27.7 | +6.04 | 46.4 | 0.54 | 46.2 | keep collecting (13/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.3 | 17.4 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-11 | 45.0 | 48.5 | -3.5 | -3.2 | -16.0 | 0.85 | 45.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 47.9 | 14.6 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 11-9 | 55.0 | 48.7 | 6.3 | +1.04 | 5.2 | 0.7 | 45.0 | keep collecting (20/30) |
| follow_move+pin_value | spread | 12-7 | 63.2 | 49.0 | 14.2 | +3.45 | 18.2 | 0.26 | 31.6 | keep collecting (19/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 47.9 | 52.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 47.9 | 52.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 47.9 | 52.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-2 | 81.8 | 48.3 | 33.6 | +6.22 | 56.6 | 0.36 | 45.5 | keep collecting (11/30) |
| money_delta+rlm_quiet | spread | 1-0 | 100.0 | 47.9 | 52.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 2-0 | 100.0 | 47.9 | 52.1 | +1.74 | 87.1 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 52.1 | 14.5 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | spread | 1-3 | 25.0 | 48.9 | -23.9 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 47.9 | -47.9 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-2 | 33.3 | 47.9 | -14.5 | -1.09 | -36.4 | 0.33 | 33.3 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.1 | -52.1 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 11-10 | 52.4 | 50.2 | 2.2 | +0.04 | 0.2 | 0.86 | 52.4 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 24-21 | 53.3 | 49.9 | 3.4 | +0.92 | 2.1 | -0.07 | 35.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | total | 37-30 | 55.2 | 50.0 | 5.3 | +3.65 | 5.4 | -0.09 | 32.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | total | 28-19 | 59.6 | 50.1 | 9.5 | +6.5 | 13.8 | 0.26 | 36.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 49.7 | -49.7 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 8-5 | 61.5 | 50.1 | 11.4 | +2.23 | 17.2 | 0.23 | 30.8 | keep collecting (13/30) |
| money_moving+pin_value | total | 5-4 | 55.6 | 50.1 | 5.5 | +0.47 | 5.2 | 0.11 | 22.2 | keep collecting (9/30) |
| pin_value+sharp_gap | total | 11-6 | 64.7 | 50.1 | 14.7 | +3.92 | 23.1 | -0.06 | 29.4 | keep collecting (17/30) |
| follow_move+money_level | total | 22-19 | 53.7 | 49.9 | 3.8 | +0.94 | 2.3 | 0.15 | 39.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 7-9 | 43.8 | 50.0 | -6.2 | -2.75 | -17.2 | -0.31 | 25.0 | keep collecting (16/30) |
| follow_move+rlm_ratio | total | 13-5 | 72.2 | 50.2 | 22.0 | +6.99 | 38.8 | 0.67 | 55.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 29-14 | 67.4 | 50.0 | 17.4 | +12.42 | 28.9 | 0.44 | 44.2 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 5-3 | 62.5 | 50.2 | 12.3 | +1.63 | 20.4 | 1.0 | 62.5 | keep collecting (8/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 50.1 | 16.6 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 13-5 | 72.2 | 50.2 | 22.0 | +6.99 | 38.8 | 0.67 | 55.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 16-14 | 53.3 | 50.0 | 3.3 | +0.65 | 2.2 | 0.57 | 50.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | total | 4-3 | 57.1 | 49.9 | 7.3 | +0.53 | 7.5 | -0.43 | 14.3 | keep collecting (7/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 49.8 | 30.2 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 49.9 | -16.6 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 6-6 | 50.0 | 50.1 | -0.1 | -0.58 | -4.8 | -0.08 | 25.0 | keep collecting (12/30) |
| money_moving+rlm_ratio | total | 6-4 | 60.0 | 50.2 | 9.8 | +1.58 | 15.8 | 0.4 | 50.0 | keep collecting (10/30) |
| consensus_gap+follow_move | total | 12-8 | 60.0 | 50.0 | 10.0 | +2.88 | 14.4 | 1.45 | 65.0 | keep collecting (20/30) |
| consensus_gap+money_delta | total | 2-0 | 100.0 | 49.7 | 50.3 | +1.78 | 88.9 | 0.0 | 0.0 | keep collecting (2/30) |
| follow_move+money_delta | total | 2-2 | 50.0 | 50.1 | -0.1 | -0.22 | -5.5 | 1.25 | 50.0 | keep collecting (4/30) |
| money_delta+money_moving | total | 6-2 | 75.0 | 50.1 | 24.9 | +3.35 | 41.9 | 0.5 | 25.0 | keep collecting (8/30) |
| money_delta+pin_value | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 | -0.5 | 0.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 5-1 | 83.3 | 50.1 | 33.2 | +3.44 | 57.4 | 0.67 | 33.3 | keep collecting (6/30) |
| money_moving+rlm_quiet | total | 4-3 | 57.1 | 50.2 | 6.9 | +0.64 | 9.1 | 0.43 | 42.9 | keep collecting (7/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 6-2 | 75.0 | 50.2 | 24.8 | +3.5 | 43.7 | 0.62 | 62.5 | keep collecting (8/30) |
| rlm_quiet+sharp_gap | total | 8-2 | 80.0 | 50.2 | 29.8 | +5.31 | 53.1 | 0.8 | 60.0 | keep collecting (10/30) |
| follow_move+pin_move | total | 2-0 | 100.0 | 50.3 | 49.7 | +1.86 | 93.0 | 1.0 | 100.0 | keep collecting (2/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 50.3 | -50.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 50.3 | -50.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 2-1 | 66.7 | 50.1 | 16.6 | +0.82 | 27.3 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 50.3 | -0.3 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 3-1 | 75.0 | 50.3 | 24.7 | +1.77 | 44.2 | 0.25 | 50.0 | keep collecting (4/30) |
| money_level+pin_move | total | 0-1 | 0.0 | 49.7 | -49.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_value | total | 0-1 | 0.0 | 49.7 | -49.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 49.7 | -49.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 50.3 | -50.3 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 0-1 | 0.0 | 50.3 | -50.3 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 182-256 | 41.6 | 41.9 | -0.3 | -33.92 | -7.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move | both | 496-500 | 49.8 | 49.9 | -0.1 | -33.5 | -3.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta | both | 316-422 | 42.8 | 44.0 | -1.2 | -57.17 | -7.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm | both | 140-161 | 46.5 | 42.2 | 4.4 | +27.28 | 9.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | both | 856-763 | 52.9 | 51.9 | 1.0 | -89.6 | -5.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | both | 200-225 | 47.1 | 44.6 | 2.5 | +1.15 | 0.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level | both | 1082-804 | 57.4 | 55.5 | 1.8 | -66.84 | -3.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 845-975 | 46.4 | 47.5 | -1.0 | -118.59 | -6.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | both | 846-975 | 46.5 | 47.8 | -1.3 | -126.2 | -6.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | both | 355-360 | 49.7 | 47.9 | 1.8 | +3.77 | 0.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 330-448 | 42.4 | 47.1 | -4.7 | -87.6 | -11.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+follow_move | both | 127-127 | 50.0 | 51.2 | -1.2 | -15.22 | -6.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | both | 147-241 | 37.9 | 44.3 | -6.4 | -31.8 | -8.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_move | both | 81-85 | 48.8 | 50.9 | -2.1 | +1.11 | 0.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | both | 23-40 | 36.5 | 37.0 | -0.5 | +9.03 | 14.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_value | both | 135-147 | 47.9 | 45.5 | 2.4 | +5.35 | 1.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | both | 25-43 | 36.8 | 39.7 | -2.9 | -1.66 | -2.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | both | 146-245 | 37.3 | 43.8 | -6.4 | -32.79 | -8.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_moving | both | 457-486 | 48.5 | 49.4 | -0.9 | -66.32 | -7.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_move | both | 357-356 | 50.1 | 50.3 | -0.2 | -32.74 | -4.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_rlm | both | 108-114 | 48.6 | 44.3 | 4.3 | +4.57 | 2.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | both | 125-121 | 50.8 | 48.9 | 1.9 | -9.65 | -3.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | both | 200-225 | 47.1 | 44.6 | 2.5 | +1.15 | 0.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 462-483 | 48.9 | 49.2 | -0.3 | -56.21 | -5.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_move | both | 299-331 | 47.5 | 48.6 | -1.2 | -27.98 | -4.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_rlm | both | 134-157 | 46.0 | 42.1 | 3.9 | +25.32 | 8.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_value | both | 157-186 | 45.8 | 47.2 | -1.4 | -15.12 | -4.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | both | 192-218 | 46.8 | 44.6 | 2.2 | +0.23 | 0.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+sharp_gap | both | 811-937 | 46.4 | 47.5 | -1.1 | -110.22 | -6.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_rlm | both | 129-134 | 49.0 | 44.2 | 4.8 | +21.5 | 8.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_value | both | 157-157 | 50.0 | 49.0 | 1.0 | -6.0 | -1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_ratio | both | 116-113 | 50.7 | 45.7 | 4.9 | +12.25 | 5.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | both | 306-332 | 48.0 | 48.6 | -0.6 | -22.74 | -3.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+pin_value | both | 40-42 | 48.8 | 45.7 | 3.1 | +11.58 | 14.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_ratio | both | 108-114 | 48.6 | 44.3 | 4.3 | +4.57 | 2.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | both | 140-161 | 46.5 | 42.2 | 4.4 | +27.28 | 9.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 38-33 | 53.5 | 48.7 | 4.8 | +1.73 | 2.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | both | 159-187 | 46.0 | 47.1 | -1.1 | -14.32 | -4.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio+sharp_gap | both | 200-225 | 47.1 | 44.6 | 2.5 | +1.15 | 0.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 151-176 | 46.2 | 46.0 | 0.2 | -22.47 | -6.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+money_moving | both | 596-531 | 52.9 | 52.4 | 0.5 | -46.31 | -4.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | both | 587-522 | 52.9 | 52.2 | 0.8 | -38.85 | -3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | both | 564-401 | 58.4 | 56.6 | 1.9 | -44.59 | -4.6 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 95-81 | 54.0 | 48.4 | 5.5 | +10.68 | 6.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | both | 202-165 | 55.0 | 57.9 | -2.9 | -23.58 | -6.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | both | 293-269 | 52.1 | 53.1 | -1.0 | -28.76 | -5.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | both | 174-159 | 52.3 | 49.8 | 2.4 | -7.73 | -2.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_quiet | both | 19-47 | 28.8 | 36.2 | -7.4 | -9.07 | -13.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_quiet | both | 182-256 | 41.6 | 41.9 | -0.3 | -33.92 | -7.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 98-149 | 39.7 | 41.9 | -2.2 | -20.73 | -8.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_moving | both | 226-330 | 40.6 | 42.4 | -1.8 | -48.17 | -8.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_delta | both | 41-109 | 27.3 | 36.7 | -9.3 | -30.68 | -20.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_level | both | 117-111 | 51.3 | 46.9 | 4.4 | +11.59 | 5.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | both | 68-72 | 48.6 | 46.9 | 1.7 | -6.57 | -4.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+sharp_gap | both | 223-325 | 40.7 | 42.5 | -1.8 | -46.34 | -8.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 79-122 | 39.3 | 40.4 | -1.1 | -11.64 | -5.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_quiet | both | 90-146 | 38.1 | 41.7 | -3.5 | -23.63 | -10.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+rlm_quiet | both | 49-87 | 36.0 | 42.8 | -6.7 | -30.79 | -22.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+rlm_quiet | both | 88-108 | 44.9 | 44.1 | 0.8 | -6.25 | -3.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_quiet | both | 42-64 | 39.6 | 40.7 | -1.1 | -10.48 | -9.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 118-139 | 45.9 | 46.5 | -0.5 | -9.93 | -3.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_rlm | both | 63-44 | 58.9 | 46.7 | 12.2 | +18.25 | 17.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_rlm | both | 82-95 | 46.3 | 42.3 | 4.0 | +11.43 | 6.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+rlm_ratio | both | 110-116 | 48.7 | 45.0 | 3.6 | -0.1 | -0.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+rlm_quiet | both | 24-36 | 40.0 | 47.2 | -7.2 | -13.58 | -22.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 50.3 | 49.7 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 52-110 | 32.1 | 27.5 | 4.6 | -7.46 | -4.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet | spread | 45-44 | 50.6 | 50.6 | -0.1 | -2.33 | -2.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_quiet | total | 85-102 | 45.5 | 50.1 | -4.7 | -24.13 | -12.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move | moneyline | 103-103 | 50.0 | 49.3 | 0.7 | +4.99 | 2.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move | spread | 194-208 | 48.3 | 50.2 | -1.9 | -31.15 | -7.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move | total | 199-189 | 51.3 | 50.1 | 1.2 | -7.34 | -1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | moneyline | 49-165 | 22.9 | 28.2 | -5.3 | -43.92 | -20.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta | spread | 122-125 | 49.4 | 50.8 | -1.4 | -13.91 | -5.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | total | 145-132 | 52.3 | 50.2 | 2.2 | +0.66 | 0.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm | moneyline | 38-74 | 33.9 | 28.3 | 5.6 | +20.97 | 18.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm | spread | 25-23 | 52.1 | 50.9 | 1.2 | -0.21 | -0.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm | total | 77-64 | 54.6 | 50.2 | 4.4 | +6.52 | 4.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | moneyline | 313-205 | 60.4 | 56.4 | 4.0 | -25.85 | -5.0 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 247-261 | 48.6 | 49.6 | -0.9 | -36.75 | -7.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | total | 296-297 | 49.9 | 50.0 | -0.1 | -27.0 | -4.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | moneyline | 37-80 | 31.6 | 29.8 | 1.8 | -2.78 | -2.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio | spread | 41-43 | 48.8 | 50.2 | -1.3 | -5.76 | -6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | total | 122-102 | 54.5 | 50.2 | 4.3 | +9.69 | 4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | moneyline | 416-157 | 72.6 | 69.0 | 3.6 | -22.78 | -4.0 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 315-326 | 49.1 | 49.3 | -0.2 | -41.85 | -6.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level | total | 351-321 | 52.2 | 49.9 | 2.3 | -2.21 | -0.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 201-326 | 38.1 | 41.6 | -3.5 | -54.15 | -10.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| sharp_gap | spread | 323-310 | 51.0 | 49.6 | 1.4 | -18.56 | -2.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 321-339 | 48.6 | 50.1 | -1.4 | -45.88 | -7.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | moneyline | 209-316 | 39.8 | 42.7 | -2.8 | -45.1 | -8.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | spread | 320-313 | 50.6 | 49.6 | 1.0 | -24.43 | -3.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | total | 317-346 | 47.8 | 50.1 | -2.2 | -56.67 | -8.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | moneyline | 18-54 | 25.0 | 30.5 | -5.5 | +10.87 | 15.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | spread | 159-148 | 51.8 | 49.6 | 2.2 | -9.27 | -3.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 178-158 | 53.0 | 50.0 | 3.0 | +2.17 | 0.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.1 | 47.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 140-272 | 34.0 | 44.9 | -10.9 | -77.34 | -18.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 85-75 | 53.1 | 49.3 | 3.9 | -2.53 | -1.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap | total | 105-101 | 51.0 | 49.8 | 1.1 | -7.73 | -3.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | moneyline | 145-83 | 63.6 | 63.1 | 0.5 | -6.7 | -2.9 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 136-81 | 62.7 | 62.6 | 0.1 | -6.32 | -2.9 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 187-302 | 38.2 | 41.5 | -3.3 | -41.39 | -8.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+follow_move | moneyline | 52-67 | 43.7 | 53.3 | -9.6 | -20.43 | -17.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 7-36 | 16.3 | 28.8 | -12.5 | -8.64 | -20.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 52-110 | 32.1 | 27.5 | 4.6 | -7.46 | -4.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 95-65 | 59.4 | 69.0 | -9.6 | -16.77 | -10.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 55-153 | 26.4 | 39.9 | -13.4 | -23.75 | -11.4 |  |  | !! CHECK: consensus_gap+money_moving close moneyline all sits -13.4 pts from its base (39.9%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | moneyline | 245-79 | 75.6 | 70.5 | 5.1 | -11.75 | -3.6 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 101-109 | 48.1 | 48.2 | -0.1 | -12.65 | -6.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_moving | moneyline | 46-148 | 23.7 | 27.8 | -4.1 | -29.89 | -15.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+sharp_gap | moneyline | 44-147 | 23.0 | 27.9 | -4.8 | -31.08 | -16.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 53-158 | 25.1 | 38.8 | -13.7 | -26.63 | -12.6 |  |  | !! CHECK: consensus_gap+sharp_gap close moneyline all sits -13.7 pts from its base (38.8%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+sharp_gap | moneyline | 98-108 | 47.6 | 47.3 | 0.3 | -12.08 | -5.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_quiet | moneyline | 23-67 | 25.6 | 27.7 | -2.1 | -5.91 | -6.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 24-68 | 26.1 | 27.6 | -1.6 | -7.45 | -8.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_move | moneyline | 28-36 | 43.8 | 52.9 | -9.2 | +3.93 | 6.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 10-29 | 25.6 | 29.0 | -3.4 | +8.65 | 22.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 4-30 | 11.8 | 29.4 | -17.6 | -7.04 | -20.7 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 83-68 | 55.0 | 51.4 | 3.6 | +5.35 | 3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_rlm | moneyline | 24-40 | 37.5 | 29.6 | 7.9 | +1.46 | 2.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 37-80 | 31.6 | 29.8 | 1.8 | -2.78 | -2.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 46-64 | 41.8 | 42.4 | -0.5 | +8.69 | 7.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_rlm | moneyline | 37-72 | 33.9 | 28.3 | 5.6 | +21.57 | 19.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 36-76 | 32.1 | 30.0 | 2.2 | -0.18 | -0.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_rlm | moneyline | 27-47 | 36.5 | 28.5 | 8.0 | +15.19 | 20.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 23-33 | 41.1 | 28.3 | 12.8 | +8.87 | 15.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 21-31 | 40.4 | 30.2 | 10.2 | +7.28 | 14.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+sharp_gap | moneyline | 46-65 | 41.4 | 41.8 | -0.3 | +7.51 | 6.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 14-33 | 29.8 | 28.6 | 1.2 | -5.18 | -11.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 24-40 | 37.5 | 29.6 | 7.9 | +1.46 | 2.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 38-74 | 33.9 | 28.3 | 5.6 | +20.97 | 18.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 23-65 | 26.1 | 27.7 | -1.6 | -5.91 | -6.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 37-80 | 31.6 | 29.8 | 1.8 | -2.78 | -2.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 11-81 | 12.0 | 28.2 | -16.2 | -28.62 | -31.1 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 13-45 | 22.4 | 29.9 | -7.4 | +1.38 | 2.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_move | moneyline | 16-35 | 31.4 | 30.3 | 1.1 | +0.84 | 1.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_rlm | moneyline | 22-44 | 33.3 | 28.8 | 4.6 | +7.63 | 11.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_value | moneyline | 2-18 | 10.0 | 26.6 | -16.6 | -11.18 | -55.9 |  |  | keep collecting (20/30) |
| money_moving+pin_value | moneyline | 10-33 | 23.3 | 29.9 | -6.6 | +8.44 | 19.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_value | moneyline | 6-9 | 40.0 | 32.9 | 7.1 | +7.27 | 48.5 |  |  | keep collecting (15/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 26.6 | 4.6 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 10-35 | 22.2 | 29.7 | -7.5 | +6.44 | 14.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_delta | moneyline | 23-47 | 32.9 | 30.6 | 2.2 | -10.09 | -14.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_level | moneyline | 14-23 | 37.8 | 30.4 | 7.4 | +6.11 | 16.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+rlm_ratio | moneyline | 21-38 | 35.6 | 30.6 | 5.0 | -3.0 | -5.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_move | moneyline | 67-42 | 61.5 | 66.9 | -5.5 | -6.77 | -6.2 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 11-9 | 55.0 | 31.3 | 23.7 | +5.77 | 28.8 |  |  | keep collecting (20/30) |
| money_level+rlm_ratio | moneyline | 13-11 | 54.2 | 38.3 | 15.9 | +6.1 | 25.4 |  |  | keep collecting (24/30) |
| money_delta+rlm_quiet | moneyline | 15-35 | 30.0 | 29.4 | 0.6 | -9.95 | -19.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_value | moneyline | 5-2 | 71.4 | 66.7 | 4.7 | +0.68 | 9.7 |  |  | keep collecting (7/30) |
| follow_move+pin_value | moneyline | 2-7 | 22.2 | 31.8 | -9.6 | -4.79 | -53.3 |  |  | keep collecting (9/30) |
| pin_value+rlm_quiet | moneyline | 1-6 | 14.3 | 26.6 | -12.3 | -4.48 | -64.0 |  |  | keep collecting (7/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 26.6 | -1.6 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 34-27 | 55.7 | 48.6 | 7.1 | +1.9 | 3.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | spread | 47-42 | 52.8 | 49.1 | 3.7 | -1.97 | -2.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_move | spread | 24-28 | 46.2 | 49.3 | -3.1 | -7.56 | -14.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 60-45 | 57.1 | 49.2 | 8.0 | +5.95 | 5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_ratio | spread | 4-4 | 50.0 | 50.0 | 0.0 | -0.67 | -8.3 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | spread | 46-42 | 52.3 | 49.2 | 3.0 | -2.86 | -3.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | spread | 157-160 | 49.5 | 49.3 | 0.2 | -18.11 | -5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_move | spread | 123-137 | 47.3 | 49.9 | -2.6 | -24.95 | -9.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_rlm | spread | 19-19 | 50.0 | 50.7 | -0.7 | -1.65 | -4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | spread | 56-51 | 52.3 | 49.1 | 3.3 | -2.23 | -2.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | spread | 41-43 | 48.8 | 50.2 | -1.3 | -5.76 | -6.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 158-159 | 49.8 | 49.4 | 0.5 | -15.97 | -5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_move | spread | 116-126 | 47.9 | 49.8 | -1.9 | -20.83 | -8.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | spread | 23-23 | 50.0 | 50.8 | -0.8 | -2.04 | -4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | spread | 79-80 | 49.7 | 49.3 | 0.4 | -11.83 | -7.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_ratio | spread | 39-42 | 48.1 | 50.1 | -1.9 | -6.69 | -8.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | spread | 315-305 | 50.8 | 49.6 | 1.2 | -20.93 | -3.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_rlm | spread | 25-23 | 52.1 | 50.9 | 1.2 | -0.21 | -0.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 72-80 | 47.4 | 49.7 | -2.4 | -16.54 | -10.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_ratio | spread | 22-26 | 45.8 | 50.5 | -4.7 | -5.94 | -12.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | spread | 119-126 | 48.6 | 49.9 | -1.3 | -18.1 | -7.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+pin_value | spread | 7-10 | 41.2 | 50.6 | -9.4 | -3.88 | -22.8 |  |  | keep collecting (17/30) |
| pin_rlm+rlm_ratio | spread | 19-19 | 50.0 | 50.7 | -0.7 | -1.65 | -4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | spread | 25-23 | 52.1 | 50.9 | 1.2 | -0.21 | -0.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 7-8 | 46.7 | 49.6 | -2.9 | -2.01 | -13.4 |  |  | keep collecting (15/30) |
| pin_value+sharp_gap | spread | 79-80 | 49.7 | 49.4 | 0.3 | -11.89 | -7.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | spread | 41-43 | 48.8 | 50.2 | -1.3 | -5.76 | -6.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 152-164 | 48.1 | 49.1 | -1.0 | -26.69 | -8.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+rlm_ratio | spread | 21-28 | 42.9 | 49.9 | -7.0 | -9.13 | -18.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | spread | 248-243 | 50.5 | 49.3 | 1.2 | -19.56 | -4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | spread | 56-46 | 54.9 | 48.9 | 6.0 | +1.89 | 1.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | spread | 247-244 | 50.3 | 49.3 | 1.0 | -21.47 | -4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | spread | 106-126 | 45.7 | 49.6 | -3.9 | -30.32 | -13.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_value | spread | 85-87 | 49.4 | 49.1 | 0.3 | -13.64 | -7.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_delta | spread | 14-14 | 50.0 | 50.5 | -0.5 | -2.09 | -7.5 |  |  | keep collecting (28/30) |
| follow_move+money_delta | spread | 38-47 | 44.7 | 50.2 | -5.5 | -12.62 | -14.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_level | spread | 40-40 | 50.0 | 50.1 | -0.1 | -3.96 | -4.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_moving | spread | 68-74 | 47.9 | 50.4 | -2.6 | -12.64 | -8.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | spread | 32-27 | 54.2 | 50.5 | 3.8 | +0.88 | 1.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+sharp_gap | spread | 67-72 | 48.2 | 50.4 | -2.2 | -11.62 | -8.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_quiet | spread | 45-44 | 50.6 | 50.6 | -0.1 | -2.33 | -2.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 14-4 | 77.8 | 50.7 | 27.1 | +8.78 | 48.8 |  |  | keep collecting (18/30) |
| rlm_quiet+sharp_gap | spread | 21-10 | 67.7 | 50.9 | 16.9 | +9.22 | 29.7 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+pin_rlm | spread | 14-11 | 56.0 | 50.4 | 5.6 | +1.57 | 6.3 |  |  | keep collecting (25/30) |
| money_delta+pin_move | spread | 36-45 | 44.4 | 50.9 | -6.4 | -12.09 | -14.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+rlm_ratio | spread | 16-26 | 38.1 | 50.0 | -11.9 | -11.78 | -28.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 52.1 | 47.9 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_rlm | spread | 13-16 | 44.8 | 50.7 | -5.8 | -4.31 | -14.8 |  |  | keep collecting (29/30) |
| money_delta+rlm_quiet | spread | 14-17 | 45.2 | 51.0 | -5.9 | -4.07 | -13.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_quiet | spread | 20-10 | 66.7 | 50.8 | 15.8 | +8.27 | 27.6 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| pin_move+rlm_quiet | spread | 26-21 | 55.3 | 51.0 | 4.3 | +3.15 | 6.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-2 | 75.0 | 51.6 | 23.4 | +3.56 | 44.5 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_quiet | spread | 2-3 | 40.0 | 50.4 | -10.4 | -1.33 | -26.7 |  |  | keep collecting (5/30) |
| pin_value+rlm_quiet | spread | 4-4 | 50.0 | 48.9 | 1.1 | -0.52 | -6.5 |  |  | keep collecting (8/30) |
| follow_move+money_delta | total | 90-82 | 52.3 | 50.1 | 2.2 | +0.24 | 0.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | total | 204-204 | 50.0 | 50.0 | 0.0 | -18.14 | -4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | total | 203-198 | 50.6 | 50.0 | 0.6 | -12.98 | -3.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | total | 309-330 | 48.4 | 50.1 | -1.7 | -47.91 | -7.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | total | 51-54 | 48.6 | 49.8 | -1.2 | -8.7 | -8.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_move | total | 29-21 | 58.0 | 49.9 | 8.1 | +4.74 | 9.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_value | total | 62-57 | 52.1 | 49.8 | 2.3 | -1.98 | -1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | total | 199-217 | 47.8 | 50.1 | -2.2 | -35.56 | -8.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+sharp_gap | total | 206-216 | 48.8 | 50.1 | -1.2 | -28.16 | -6.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | total | 120-101 | 54.3 | 50.0 | 4.3 | +8.33 | 3.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | total | 84-70 | 54.5 | 49.9 | 4.7 | +5.23 | 3.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_value | total | 79-68 | 53.7 | 50.0 | 3.7 | +3.27 | 2.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_quiet | total | 85-102 | 45.5 | 50.1 | -4.7 | -24.13 | -12.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 137-141 | 49.3 | 50.1 | -0.8 | -15.84 | -5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_quiet+sharp_gap | total | 53-71 | 42.7 | 50.2 | -7.4 | -22.49 | -18.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_moving | total | 112-108 | 50.9 | 50.2 | 0.7 | -5.64 | -2.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | total | 167-158 | 51.4 | 50.0 | 1.4 | -6.16 | -1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 67-63 | 51.5 | 50.0 | 1.6 | -2.62 | -2.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | total | 68-73 | 48.2 | 50.0 | -1.8 | -11.73 | -8.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | total | 70-72 | 49.3 | 50.0 | -0.7 | -8.87 | -6.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | total | 45-46 | 49.5 | 49.9 | -0.4 | -6.08 | -6.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+sharp_gap | total | 47-45 | 51.1 | 49.9 | 1.2 | -3.3 | -3.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+follow_move | total | 41-33 | 55.4 | 49.8 | 5.6 | +3.3 | 4.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_delta | total | 16-14 | 53.3 | 50.0 | 3.4 | +0.03 | 0.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_quiet | total | 10-8 | 55.6 | 50.0 | 5.5 | +0.9 | 5.0 |  |  | keep collecting (18/30) |
| money_delta+rlm_quiet | total | 20-35 | 36.4 | 50.2 | -13.9 | -16.76 | -30.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+sharp_gap | total | 112-106 | 51.4 | 50.2 | 1.2 | -3.64 | -1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_quiet | total | 47-69 | 40.5 | 50.2 | -9.7 | -25.99 | -22.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 63-48 | 56.8 | 50.1 | 6.6 | +9.44 | 8.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_move | total | 66-59 | 52.8 | 50.2 | 2.6 | +1.32 | 1.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | total | 141-141 | 50.0 | 50.1 | -0.1 | -12.15 | -4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_move | total | 151-151 | 50.0 | 50.1 | -0.1 | -13.15 | -4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+rlm_quiet | total | 19-26 | 42.2 | 50.1 | -7.9 | -8.58 | -19.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | total | 10-8 | 55.6 | 50.0 | 5.6 | +0.87 | 4.8 |  |  | keep collecting (18/30) |
| consensus_gap+rlm_ratio | total | 17-9 | 65.4 | 49.9 | 15.5 | +6.04 | 23.2 |  |  | keep collecting (26/30) |
| follow_move+pin_rlm | total | 65-55 | 54.2 | 50.2 | 4.0 | +4.75 | 4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | total | 122-102 | 54.5 | 50.2 | 4.3 | +9.69 | 4.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 38-24 | 61.3 | 50.2 | 11.1 | +10.91 | 17.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+rlm_ratio | total | 61-42 | 59.2 | 50.1 | 9.1 | +13.72 | 13.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | total | 74-62 | 54.4 | 50.2 | 4.2 | +5.79 | 4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_ratio | total | 117-100 | 53.9 | 50.2 | 3.8 | +7.11 | 3.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_rlm | total | 77-64 | 54.6 | 50.2 | 4.4 | +6.52 | 4.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 73-56 | 56.6 | 50.2 | 6.4 | +10.92 | 8.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+pin_value | total | 28-21 | 57.1 | 50.1 | 7.0 | +4.4 | 9.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_ratio | total | 65-55 | 54.2 | 50.2 | 4.0 | +4.75 | 4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | total | 77-64 | 54.6 | 50.2 | 4.4 | +6.52 | 4.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 30-22 | 57.7 | 50.1 | 7.6 | +5.22 | 10.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | total | 122-102 | 54.5 | 50.2 | 4.3 | +9.69 | 4.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 47-35 | 57.3 | 50.2 | 7.1 | +8.11 | 9.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+rlm_ratio | total | 73-52 | 58.4 | 50.2 | 8.2 | +14.68 | 11.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | total | 34-27 | 55.7 | 50.1 | 5.6 | +3.73 | 6.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_quiet | total | 39-54 | 41.9 | 50.1 | -8.2 | -18.27 | -19.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_quiet | total | 22-29 | 43.1 | 50.2 | -7.1 | -8.86 | -17.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_quiet+rlm_ratio | total | 42-53 | 44.2 | 50.2 | -6.0 | -14.5 | -15.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 50.3 | 49.7 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

# Pooled (fit + forward together)

Kept for continuity. **Contaminated** — it mixes the games the engine was built
on with the games testing it. Use the forward table for any decision.

## EARLY  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 36-44 | 45.0 | 36.2 | 8.8 | +9.82 | 12.3 | 0.23 | 43.8 | no edge shown yet |
| pin_move | both | 6-10 | 37.5 | 48.4 | -10.9 | -5.19 | -32.4 | 0.19 | 43.8 | keep collecting (16/30) |
| money_delta | both | 10-8 | 55.6 | 42.3 | 13.3 | +3.43 | 19.1 | -0.09 | 33.3 | keep collecting (18/30) |
| pin_rlm | both | 1-2 | 33.3 | 27.3 | 6.0 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | both | 525-465 | 53.0 | 52.0 | 1.1 | -61.03 | -6.2 | 0.18 | 41.0 | no edge shown yet |
| rlm_ratio | both | 33-23 | 58.9 | 39.1 | 19.9 | +19.02 | 34.0 | 0.47 | 51.8 | no edge shown yet |
| money_level | both | 183-124 | 59.6 | 59.0 | 0.6 | -18.06 | -5.9 | -0.11 | 38.8 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 154-134 | 53.5 | 48.0 | 5.4 | +16.04 | 5.6 | 0.3 | 43.8 | no edge shown yet |
| money_moving | both | 114-91 | 55.6 | 51.0 | 4.6 | +2.02 | 1.0 | 0.1 | 42.4 | no edge shown yet |
| pin_value | both | 54-51 | 51.4 | 48.4 | 3.1 | -3.0 | -2.9 | 0.04 | 36.2 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.6 | -31.6 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 256-318 | 44.6 | 47.8 | -3.2 | -58.34 | -10.2 | 0.39 | 45.3 | DROP: below break-even |
| consensus_gap+money_level | both | 38-32 | 54.3 | 63.2 | -9.0 | -10.99 | -15.7 | 0.29 | 47.1 | no edge shown yet |
| consensus_gap+money_moving | both | 20-24 | 45.5 | 48.1 | -2.7 | -6.16 | -14.0 | 0.23 | 40.9 | no edge shown yet |
| consensus_gap+pin_value | both | 21-28 | 42.9 | 46.7 | -3.8 | -9.79 | -20.0 | 0.38 | 46.9 | no edge shown yet |
| follow_move+rlm_quiet | both | 36-44 | 45.0 | 36.2 | 8.8 | +9.82 | 12.3 | 0.23 | 43.8 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 33-23 | 58.9 | 39.1 | 19.9 | +19.02 | 34.0 | 0.47 | 51.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 80-46 | 63.5 | 49.3 | 14.2 | +21.71 | 17.2 | 0.4 | 47.6 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 69-46 | 60.0 | 58.0 | 2.0 | -4.07 | -3.5 | -0.1 | 46.1 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 12-9 | 57.1 | 49.5 | 7.6 | +1.72 | 8.2 | 0.38 | 42.9 | keep collecting (21/30) |
| money_moving+pin_value | both | 9-6 | 60.0 | 49.5 | 10.5 | +1.88 | 12.5 | 0.27 | 33.3 | keep collecting (15/30) |
| rlm_quiet+rlm_ratio | both | 20-14 | 58.8 | 36.5 | 22.3 | +14.73 | 43.3 | -0.04 | 47.1 | no edge shown yet |
| rlm_quiet+sharp_gap | both | 22-18 | 55.0 | 36.8 | 18.2 | +12.55 | 31.4 | -0.06 | 45.0 | no edge shown yet |
| rlm_ratio+sharp_gap | both | 33-23 | 58.9 | 39.1 | 19.9 | +19.02 | 34.0 | 0.47 | 51.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 101-66 | 60.5 | 55.5 | 5.0 | +0.84 | 0.5 | 0.16 | 43.7 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 67-55 | 54.9 | 48.4 | 6.6 | +5.6 | 4.6 | 0.28 | 46.7 | no edge shown yet |
| money_delta+money_level | both | 3-3 | 50.0 | 46.5 | 3.5 | +0.46 | 7.6 | 1.3 | 66.7 | keep collecting (6/30) |
| money_delta+money_moving | both | 9-8 | 52.9 | 41.8 | 11.1 | +2.53 | 14.9 | -0.1 | 35.3 | keep collecting (17/30) |
| money_delta+pin_value | both | 3-1 | 75.0 | 50.0 | 25.0 | +1.61 | 40.3 | 0.0 | 25.0 | keep collecting (4/30) |
| money_delta+sharp_gap | both | 7-6 | 53.8 | 41.4 | 12.5 | +2.78 | 21.4 | -0.13 | 46.2 | keep collecting (13/30) |
| pin_value+sharp_gap | both | 13-8 | 61.9 | 48.7 | 13.2 | +3.66 | 17.4 | -0.18 | 33.3 | keep collecting (21/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 50.5 | -50.5 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 35-46 | 43.2 | 51.8 | -8.6 | -18.31 | -22.6 | 0.74 | 55.6 | DROP: below break-even |
| consensus_gap+rlm_quiet | both | 4-7 | 36.4 | 37.2 | -0.8 | -2.99 | -27.1 | 0.95 | 72.7 | keep collecting (11/30) |
| follow_move+pin_value | both | 22-19 | 53.7 | 48.8 | 4.9 | +0.23 | 0.6 | -0.25 | 26.8 | no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 42.4 | -25.8 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 29-47 | 38.2 | 45.8 | -7.7 | -10.04 | -13.2 | 0.86 | 50.0 | DROP: below break-even |
| follow_move+money_level | both | 93-51 | 64.6 | 59.8 | 4.8 | -4.74 | -3.3 | 0.02 | 43.1 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 11-9 | 55.0 | 42.4 | 12.6 | +2.43 | 12.1 | 1.45 | 65.0 | keep collecting (20/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 44.2 | 5.8 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 59-35 | 62.8 | 52.4 | 10.4 | +10.28 | 10.9 | 0.35 | 51.1 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 3-0 | 100.0 | 49.5 | 50.5 | +2.61 | 87.1 | 0.0 | 0.0 | keep collecting (3/30) |
| follow_move+money_delta | both | 5-4 | 55.6 | 42.0 | 13.6 | +2.95 | 32.8 | 0.27 | 44.4 | keep collecting (9/30) |
| money_delta+rlm_quiet | both | 2-2 | 50.0 | 37.9 | 12.1 | +1.53 | 38.3 | -2.1 | 0.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | both | 16-12 | 57.1 | 37.5 | 19.7 | +9.23 | 33.0 | 0.46 | 46.4 | keep collecting (28/30) |
| money_moving+rlm_ratio | both | 16-10 | 61.5 | 42.0 | 19.5 | +9.15 | 35.2 | 0.6 | 53.8 | keep collecting (26/30) |
| consensus_gap+rlm_ratio | both | 4-4 | 50.0 | 38.4 | 11.6 | +0.09 | 1.1 | 0.69 | 62.5 | keep collecting (8/30) |
| pin_move+pin_value | both | 2-4 | 33.3 | 49.3 | -16.0 | -2.18 | -36.4 | 0.17 | 16.7 | keep collecting (6/30) |
| follow_move+pin_move | both | 5-4 | 55.6 | 51.5 | 4.1 | -0.1 | -1.1 | 0.38 | 55.6 | keep collecting (9/30) |
| consensus_gap+pin_move | both | 1-5 | 16.7 | 45.4 | -28.8 | -4.09 | -68.2 | 0.22 | 50.0 | keep collecting (6/30) |
| money_level+pin_move | both | 3-2 | 60.0 | 54.7 | 5.3 | +0.04 | 0.8 | 0.08 | 40.0 | keep collecting (5/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 27.3 | -27.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 27.3 | 22.7 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 27.3 | -27.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 27.3 | -27.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 27.3 | 22.7 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | both | 1-2 | 33.3 | 27.3 | 6.0 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.1 | -51.1 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 49.5 | -49.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-1 | 66.7 | 50.2 | 16.5 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 27.3 | 72.7 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 27.3 | 72.7 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 27.3 | 72.7 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 2-2 | 50.0 | 38.4 | 11.6 | +2.34 | 58.5 | 1.15 | 75.0 | keep collecting (4/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 27.3 | -27.3 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 18-30 | 37.5 | 27.3 | 10.2 | +7.53 | 15.7 | 0.01 | 43.8 | DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.5 | 10.5 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 15-12 | 55.6 | 49.6 | 5.9 | +1.64 | 6.1 | 0.81 | 51.9 | keep collecting (27/30) |
| pin_move | moneyline | 2-3 | 40.0 | 45.5 | -5.5 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-4 | 20.0 | 49.5 | -29.5 | -3.09 | -61.8 | 0.4 | 40.0 | keep collecting (5/30) |
| pin_move | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.23 | -3.8 | 0.17 | 33.3 | keep collecting (6/30) |
| money_delta | moneyline | 2-4 | 33.3 | 27.3 | 6.0 | +0.34 | 5.7 | -1.45 | 33.3 | keep collecting (6/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 7-3 | 70.0 | 49.7 | 20.3 | +3.26 | 32.6 | 0.6 | 30.0 | keep collecting (10/30) |
| pin_rlm | moneyline | 1-2 | 33.3 | 27.3 | 6.0 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | moneyline | 215-143 | 60.1 | 55.7 | 4.3 | -23.0 | -6.4 | 0.09 | 43.9 | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 140-160 | 46.7 | 49.7 | -3.1 | -31.21 | -10.4 | -0.02 | 32.7 | DROP: below break-even |
| follow_move | total | 170-162 | 51.2 | 50.0 | 1.2 | -6.82 | -2.1 | 0.45 | 45.5 | no edge shown yet |
| rlm_ratio | moneyline | 14-13 | 51.9 | 27.3 | 24.6 | +11.47 | 42.5 | 0.43 | 55.6 | keep collecting (27/30) |
| rlm_ratio | spread | 3-3 | 50.0 | 51.8 | -1.8 | -0.16 | -2.7 | 0.33 | 16.7 | keep collecting (6/30) |
| rlm_ratio | total | 16-7 | 69.6 | 49.6 | 20.0 | +7.72 | 33.5 | 0.57 | 56.5 | keep collecting (23/30) |
| money_level | moneyline | 105-45 | 70.0 | 68.5 | 1.5 | -9.78 | -6.5 | -0.26 | 42.7 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-18 | 48.6 | 49.2 | -0.6 | -2.69 | -7.7 | 1.0 | 51.4 | no edge shown yet |
| money_level | total | 61-61 | 50.0 | 50.2 | -0.2 | -5.59 | -4.6 | -0.24 | 30.3 | no edge shown yet |
| sharp_gap | moneyline | 67-67 | 50.0 | 45.9 | 4.1 | +3.99 | 3.0 | 0.36 | 50.7 | no edge shown yet |
| sharp_gap | spread | 20-15 | 57.1 | 49.8 | 7.4 | +3.0 | 8.6 | 0.77 | 40.0 | no edge shown yet |
| sharp_gap | total | 67-52 | 56.3 | 49.9 | 6.4 | +9.04 | 7.6 | 0.09 | 37.0 | no edge shown yet |
| money_moving | moneyline | 51-45 | 53.1 | 52.4 | 0.8 | -9.12 | -9.5 | -0.06 | 47.9 | no edge shown yet |
| money_moving | spread | 18-6 | 75.0 | 49.1 | 25.9 | +10.18 | 42.4 | 0.5 | 45.8 | keep collecting (24/30) |
| money_moving | total | 45-40 | 52.9 | 50.0 | 3.0 | +0.96 | 1.1 | 0.16 | 35.3 | no edge shown yet |
| pin_value | moneyline | 2-6 | 25.0 | 33.0 | -8.0 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| pin_value | spread | 27-21 | 56.2 | 49.2 | 7.0 | +2.77 | 5.8 | 0.23 | 37.5 | no edge shown yet |
| pin_value | total | 25-24 | 51.0 | 50.0 | 1.0 | -1.47 | -3.0 | -0.12 | 32.7 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.7 | -19.3 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 104-178 | 36.9 | 46.0 | -9.1 | -53.13 | -18.8 | 0.13 | 42.2 | DROP: below break-even |
| consensus_gap | spread | 74-65 | 53.2 | 49.1 | 4.1 | -0.18 | -0.1 | 0.37 | 41.0 | no edge shown yet |
| consensus_gap | total | 78-75 | 51.0 | 50.1 | 0.9 | -5.03 | -3.3 | 0.9 | 54.9 | no edge shown yet |
| money_level+sharp_gap | moneyline | 49-20 | 71.0 | 63.5 | 7.5 | -0.34 | -0.5 | 0.06 | 53.6 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+follow_move | moneyline | 13-23 | 36.1 | 55.0 | -18.9 | -14.89 | -41.4 | 0.13 | 52.8 | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 33.0 | -8.0 | -4.31 | -53.8 | -0.08 | 50.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| consensus_gap+rlm_quiet | moneyline | 1-5 | 16.7 | 27.3 | -10.6 | -3.68 | -61.3 | 1.07 | 83.3 | keep collecting (6/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.4 | -9.1 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 18-30 | 37.5 | 27.3 | 10.2 | +7.53 | 15.7 | 0.01 | 43.8 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 34-15 | 69.4 | 69.0 | 0.4 | -5.03 | -10.3 | -0.57 | 49.0 | beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 27.3 | -27.3 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 18-37 | 32.7 | 44.6 | -11.9 | -9.77 | -17.8 | 0.85 | 50.9 | DROP: below break-even |
| follow_move+money_level | moneyline | 59-18 | 76.6 | 68.6 | 8.1 | -2.63 | -3.4 | -0.32 | 44.2 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 31-14 | 68.9 | 55.5 | 13.3 | +5.67 | 12.6 | 0.06 | 53.3 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 28-22 | 56.0 | 69.1 | -13.1 | -9.74 | -19.5 | 0.05 | 46.0 | no edge shown yet |
| follow_move+sharp_gap | moneyline | 37-20 | 64.9 | 48.8 | 16.1 | +8.57 | 15.0 | 0.25 | 52.6 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 26-28 | 48.1 | 46.6 | 1.5 | -4.66 | -8.6 | 0.2 | 55.6 | no edge shown yet |
| consensus_gap+money_moving | moneyline | 11-22 | 33.3 | 47.9 | -14.6 | -12.01 | -36.4 | 0.22 | 45.5 | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 14-13 | 51.9 | 27.3 | 24.6 | +11.47 | 42.5 | 0.43 | 55.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 10-10 | 50.0 | 27.3 | 22.7 | +9.6 | 48.0 | -0.12 | 45.0 | keep collecting (20/30) |
| rlm_quiet+sharp_gap | moneyline | 10-13 | 43.5 | 27.3 | 16.2 | +6.6 | 28.7 | -0.27 | 43.5 | keep collecting (23/30) |
| rlm_ratio+sharp_gap | moneyline | 14-13 | 51.9 | 27.3 | 24.6 | +11.47 | 42.5 | 0.43 | 55.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 27.3 | -2.3 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 7-8 | 46.7 | 27.3 | 19.4 | +5.13 | 34.2 | 0.59 | 53.3 | keep collecting (15/30) |
| money_moving+rlm_ratio | moneyline | 5-4 | 55.6 | 27.3 | 28.3 | +4.98 | 55.3 | 0.39 | 55.6 | keep collecting (9/30) |
| money_delta+money_moving | moneyline | 2-4 | 33.3 | 27.3 | 6.0 | +0.34 | 5.7 | -1.45 | 33.3 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-3 | 40.0 | 27.3 | 12.7 | +1.34 | 26.8 | -1.74 | 40.0 | keep collecting (5/30) |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 42.4 | -42.4 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-1 | 66.7 | 57.6 | 9.1 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | moneyline | 2-1 | 66.7 | 57.6 | 9.1 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 27.3 | -27.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-1 | 50.0 | 27.3 | 22.7 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 27.3 | -27.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 27.3 | -27.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-1 | 50.0 | 27.3 | 22.7 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | moneyline | 1-2 | 33.3 | 27.3 | 6.0 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 27.3 | -27.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 27.3 | -27.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.13 | 56.5 | -0.1 | 50.0 | keep collecting (2/30) |
| money_level+rlm_ratio | moneyline | 4-3 | 57.1 | 27.3 | 29.8 | +1.87 | 26.7 | 2.0 | 85.7 | keep collecting (7/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 27.3 | 72.7 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 1-0 | 100.0 | 27.3 | 72.7 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 1-0 | 100.0 | 27.3 | 72.7 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 27.3 | 39.4 | +3.34 | 111.3 | -1.53 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 1-1 | 50.0 | 27.3 | 22.7 | +1.7 | 85.0 | -4.2 | 0.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 27.3 | 72.7 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 27.3 | -27.3 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-0 | 100.0 | 27.3 | 72.7 | +1.64 | 164.0 | 3.8 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 47.3 | -1.9 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 47.3 | 36.0 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 11-8 | 57.9 | 48.5 | 9.4 | +1.43 | 7.6 | 0.47 | 47.4 | keep collecting (19/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.5 | 10.5 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-3 | 50.0 | 51.8 | -1.8 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-7 | 58.8 | 48.9 | 9.9 | +2.09 | 12.3 | 0.88 | 41.2 | keep collecting (17/30) |
| money_level+money_moving | spread | 10-6 | 62.5 | 48.7 | 13.8 | +3.12 | 19.5 | 1.19 | 68.8 | keep collecting (16/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.9 | -6.0 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 4-2 | 66.7 | 49.1 | 17.6 | +1.41 | 23.5 | 0.5 | 50.0 | keep collecting (6/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 3-3 | 50.0 | 51.8 | -1.8 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 52.7 | -52.7 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 52.7 | -52.7 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-12 | 53.8 | 49.2 | 4.7 | +0.62 | 2.4 | 1.15 | 46.2 | keep collecting (26/30) |
| money_moving+sharp_gap | spread | 10-4 | 71.4 | 49.2 | 22.2 | +5.04 | 36.0 | 0.86 | 50.0 | keep collecting (14/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.1 | 17.6 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-11 | 45.0 | 48.1 | -3.1 | -3.2 | -16.0 | 0.85 | 45.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 47.3 | 15.2 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 11-10 | 52.4 | 48.6 | 3.8 | +0.04 | 0.2 | 0.9 | 47.6 | keep collecting (21/30) |
| follow_move+pin_value | spread | 13-7 | 65.0 | 48.7 | 16.3 | +4.36 | 21.8 | 0.2 | 30.0 | keep collecting (20/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 47.3 | 52.7 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 47.3 | 52.7 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 47.3 | 52.7 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-3 | 75.0 | 48.2 | 26.8 | +5.22 | 43.5 | 0.75 | 50.0 | keep collecting (12/30) |
| money_delta+rlm_quiet | spread | 1-0 | 100.0 | 47.3 | 52.7 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 2-0 | 100.0 | 47.3 | 52.7 | +1.74 | 87.1 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 2-2 | 50.0 | 52.7 | -2.7 | -0.07 | -1.7 | 1.25 | 25.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | spread | 2-1 | 66.7 | 50.9 | 15.8 | +0.86 | 28.7 | 1.0 | 33.3 | keep collecting (3/30) |
| pin_move+pin_value | spread | 1-3 | 25.0 | 48.7 | -23.7 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 47.3 | -47.3 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-2 | 33.3 | 47.3 | -14.0 | -1.09 | -36.4 | 0.33 | 33.3 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.7 | -52.7 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 15-12 | 55.6 | 49.6 | 5.9 | +1.64 | 6.1 | 0.81 | 51.9 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 25-25 | 50.0 | 50.2 | -0.2 | -2.17 | -4.3 | -0.06 | 36.0 | no edge shown yet |
| money_level+sharp_gap | total | 38-34 | 52.8 | 50.1 | 2.7 | +0.55 | 0.8 | -0.11 | 33.3 | no edge shown yet |
| money_moving+sharp_gap | total | 31-23 | 57.4 | 49.9 | 7.5 | +5.23 | 9.7 | 0.2 | 37.0 | no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 50.5 | -50.5 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 9-5 | 64.3 | 49.9 | 14.4 | +3.14 | 22.4 | 0.21 | 28.6 | keep collecting (14/30) |
| money_moving+pin_value | total | 5-4 | 55.6 | 49.8 | 5.7 | +0.47 | 5.2 | 0.11 | 22.2 | keep collecting (9/30) |
| pin_value+sharp_gap | total | 11-6 | 64.7 | 49.9 | 14.8 | +3.92 | 23.1 | -0.06 | 29.4 | keep collecting (17/30) |
| follow_move+money_level | total | 23-23 | 50.0 | 50.2 | -0.2 | -2.15 | -4.7 | 0.2 | 39.1 | no edge shown yet |
| follow_move+pin_value | total | 8-10 | 44.4 | 50.0 | -5.6 | -2.84 | -15.8 | -0.56 | 22.2 | keep collecting (18/30) |
| follow_move+rlm_ratio | total | 16-7 | 69.6 | 49.6 | 20.0 | +7.72 | 33.5 | 0.57 | 56.5 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 33-19 | 63.5 | 49.9 | 13.5 | +11.05 | 21.3 | 0.4 | 44.2 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 5-4 | 55.6 | 49.6 | 6.0 | +0.63 | 7.0 | 1.11 | 66.7 | keep collecting (9/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 49.8 | 16.8 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 16-7 | 69.6 | 49.6 | 20.0 | +7.72 | 33.5 | 0.57 | 56.5 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 19-18 | 51.4 | 49.9 | 1.4 | -0.62 | -1.7 | 0.57 | 48.6 | no edge shown yet |
| consensus_gap+money_level | total | 5-4 | 55.6 | 50.3 | 5.3 | +0.44 | 4.8 | -0.11 | 22.2 | keep collecting (9/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 50.3 | 29.7 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 8-14 | 36.4 | 50.1 | -13.8 | -6.92 | -31.5 | 0.45 | 45.5 | keep collecting (22/30) |
| consensus_gap+sharp_gap | total | 6-7 | 46.2 | 49.9 | -3.7 | -1.58 | -12.2 | 0.08 | 30.8 | keep collecting (13/30) |
| money_moving+rlm_ratio | total | 9-5 | 64.3 | 49.6 | 14.7 | +3.31 | 23.6 | 0.64 | 57.1 | keep collecting (14/30) |
| consensus_gap+follow_move | total | 13-12 | 52.0 | 50.0 | 2.0 | -0.21 | -0.9 | 1.52 | 68.0 | keep collecting (25/30) |
| consensus_gap+money_delta | total | 2-0 | 100.0 | 50.5 | 49.5 | +1.78 | 88.9 | 0.0 | 0.0 | keep collecting (2/30) |
| follow_move+money_delta | total | 2-3 | 40.0 | 49.7 | -9.7 | -1.22 | -24.4 | 1.4 | 60.0 | keep collecting (5/30) |
| money_delta+money_moving | total | 6-3 | 66.7 | 49.7 | 17.0 | +2.35 | 26.1 | 0.67 | 33.3 | keep collecting (9/30) |
| money_delta+pin_value | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 | -0.5 | 0.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 5-2 | 71.4 | 49.8 | 21.7 | +2.44 | 34.9 | 0.86 | 42.9 | keep collecting (7/30) |
| money_moving+rlm_quiet | total | 7-4 | 63.6 | 49.6 | 14.1 | +2.36 | 21.5 | 0.55 | 45.5 | keep collecting (11/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 9-3 | 75.0 | 49.6 | 25.4 | +5.22 | 43.5 | 0.33 | 58.3 | keep collecting (12/30) |
| rlm_quiet+sharp_gap | total | 11-4 | 73.3 | 49.6 | 23.8 | +6.04 | 40.3 | 0.47 | 53.3 | keep collecting (15/30) |
| follow_move+pin_move | total | 2-1 | 66.7 | 49.5 | 17.2 | +0.86 | 28.7 | 0.67 | 66.7 | keep collecting (3/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 49.5 | -49.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 49.5 | -49.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 2-2 | 50.0 | 49.7 | 0.3 | -0.18 | -4.5 | 0.75 | 50.0 | keep collecting (4/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 49.5 | 0.5 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 3-1 | 75.0 | 49.5 | 25.5 | +1.77 | 44.2 | 0.25 | 50.0 | keep collecting (4/30) |
| money_level+pin_move | total | 1-1 | 50.0 | 50.5 | -0.5 | -0.09 | -4.5 | 0.0 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | total | 1-1 | 50.0 | 50.5 | -0.5 | -0.09 | -4.5 | 0.0 | 0.0 | keep collecting (2/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 50.5 | -50.5 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 49.5 | -49.5 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 0-2 | 0.0 | 49.5 | -49.5 | -2.0 | -100.0 | 2.0 | 100.0 | keep collecting (2/30) |
| consensus_gap+pin_move | total | 1-0 | 100.0 | 50.5 | 49.5 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 206-318 | 39.3 | 41.8 | -2.5 | -60.15 | -11.5 |  |  | DROP: below break-even |
| pin_move | both | 551-567 | 49.3 | 49.8 | -0.5 | -49.02 | -4.4 |  |  | DROP: below break-even |
| money_delta | both | 350-463 | 43.1 | 44.0 | -0.9 | -60.89 | -7.5 |  |  | DROP: below break-even |
| pin_rlm | both | 149-180 | 45.3 | 42.1 | 3.2 | +17.23 | 5.2 |  |  | DROP: below break-even |
| follow_move | both | 942-888 | 51.5 | 51.5 | -0.1 | -131.54 | -7.2 |  |  | no edge shown yet |
| rlm_ratio | both | 217-263 | 45.2 | 44.1 | 1.2 | -20.63 | -4.3 |  |  | DROP: below break-even |
| money_level | both | 1210-891 | 57.6 | 55.5 | 2.1 | -64.42 | -3.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 930-1087 | 46.1 | 47.5 | -1.4 | -154.12 | -7.6 |  |  | DROP: below break-even |
| money_moving | both | 935-1086 | 46.3 | 47.8 | -1.6 | -159.17 | -7.9 |  |  | DROP: below break-even |
| pin_value | both | 408-394 | 50.9 | 48.1 | 2.8 | +32.11 | 4.0 |  |  | no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 50.9 | 15.8 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 378-476 | 44.3 | 47.9 | -3.7 | -77.09 | -9.0 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 143-138 | 50.9 | 51.4 | -0.6 | -14.47 | -5.1 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 164-258 | 38.9 | 45.3 | -6.4 | -33.75 | -8.0 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 90-90 | 50.0 | 51.0 | -1.0 | +4.99 | 2.8 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 24-42 | 36.4 | 38.0 | -1.6 | +8.03 | 12.2 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 153-157 | 49.4 | 46.1 | 3.3 | +14.77 | 4.8 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | both | 28-47 | 37.3 | 39.4 | -2.1 | -2.86 | -3.8 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 162-262 | 38.2 | 44.6 | -6.4 | -34.88 | -8.2 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 494-549 | 47.4 | 49.2 | -1.8 | -99.62 | -9.6 |  |  | DROP: below break-even |
| follow_move+pin_move | both | 393-413 | 48.8 | 50.1 | -1.3 | -56.53 | -7.0 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 117-130 | 47.4 | 43.9 | 3.5 | -2.49 | -1.0 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 139-131 | 51.5 | 49.0 | 2.5 | +2.59 | 1.0 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 217-263 | 45.2 | 44.1 | 1.2 | -20.63 | -4.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 500-548 | 47.7 | 49.0 | -1.3 | -90.59 | -8.6 |  |  | DROP: below break-even |
| money_moving+pin_move | both | 321-360 | 47.1 | 48.6 | -1.4 | -37.6 | -5.5 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 143-175 | 45.0 | 42.1 | 2.8 | +16.26 | 5.1 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 174-204 | 46.0 | 47.3 | -1.3 | -14.41 | -3.8 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 209-254 | 45.1 | 44.2 | 1.0 | -19.55 | -4.2 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 895-1046 | 46.1 | 47.6 | -1.4 | -143.66 | -7.4 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 137-149 | 47.9 | 44.0 | 3.9 | +14.1 | 4.9 |  |  | DROP: below break-even |
| pin_move+pin_value | both | 173-170 | 50.4 | 49.2 | 1.2 | -4.8 | -1.4 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 124-127 | 49.4 | 45.3 | 4.1 | +5.86 | 2.3 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 326-363 | 47.3 | 48.4 | -1.1 | -36.14 | -5.2 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 41-43 | 48.8 | 45.7 | 3.1 | +11.49 | 13.7 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 117-130 | 47.4 | 43.9 | 3.5 | -2.49 | -1.0 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 149-180 | 45.3 | 42.1 | 3.2 | +17.23 | 5.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 41-33 | 55.4 | 48.5 | 6.9 | +4.42 | 6.0 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 175-204 | 46.2 | 47.2 | -1.1 | -13.52 | -3.6 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 217-263 | 45.2 | 44.1 | 1.2 | -20.63 | -4.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 168-206 | 44.9 | 45.7 | -0.8 | -36.67 | -9.8 |  |  | DROP: below break-even |
| money_level+money_moving | both | 660-587 | 52.9 | 52.4 | 0.6 | -53.14 | -4.3 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 647-577 | 52.9 | 52.2 | 0.7 | -46.24 | -3.8 |  |  | no edge shown yet |
| follow_move+money_level | both | 606-442 | 57.8 | 56.4 | 1.4 | -56.46 | -5.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 104-89 | 53.9 | 48.1 | 5.8 | +11.11 | 5.8 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 236-178 | 57.0 | 58.2 | -1.2 | -15.93 | -3.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_move | both | 318-296 | 51.8 | 53.1 | -1.3 | -35.86 | -5.8 |  |  | no edge shown yet |
| money_level+pin_value | both | 194-174 | 52.7 | 49.9 | 2.8 | -5.04 | -1.4 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 23-53 | 30.3 | 36.6 | -6.4 | -11.34 | -14.9 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | both | 206-318 | 39.3 | 41.8 | -2.5 | -60.15 | -11.5 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 107-182 | 37.0 | 41.6 | -4.5 | -44.96 | -15.6 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 251-359 | 41.1 | 42.3 | -1.2 | -48.17 | -7.9 |  |  | DROP: below break-even |
| consensus_gap+money_delta | both | 47-111 | 29.7 | 37.3 | -7.6 | -23.62 | -14.9 |  |  | DROP: below break-even |
| money_delta+money_level | both | 125-116 | 51.9 | 46.8 | 5.1 | +14.9 | 6.2 |  |  | no edge shown yet |
| money_delta+pin_value | both | 78-74 | 51.3 | 47.0 | 4.3 | +4.11 | 2.7 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 248-353 | 41.3 | 42.3 | -1.1 | -45.34 | -7.5 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 85-150 | 36.2 | 40.1 | -4.0 | -34.05 | -14.5 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | both | 99-176 | 36.0 | 41.5 | -5.5 | -44.86 | -16.3 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 58-109 | 34.7 | 42.7 | -8.0 | -44.39 | -26.6 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | both | 101-134 | 43.0 | 44.0 | -1.0 | -18.11 | -7.7 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 45-75 | 37.5 | 40.7 | -3.2 | -18.62 | -15.5 |  |  | DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 50.9 | 15.8 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 127-154 | 45.2 | 46.2 | -1.0 | -16.33 | -5.8 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 68-49 | 58.1 | 46.6 | 11.5 | +17.99 | 15.4 |  |  | no edge shown yet |
| money_delta+pin_rlm | both | 88-107 | 45.1 | 42.0 | 3.1 | +5.22 | 2.7 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | both | 123-137 | 47.3 | 44.6 | 2.7 | -8.96 | -3.4 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | both | 29-39 | 42.6 | 47.1 | -4.4 | -2.34 | -3.4 |  |  | DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 49.5 | 50.5 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 60-136 | 30.6 | 28.0 | 2.6 | -12.58 | -6.4 |  |  | DROP: below break-even |
| rlm_quiet | spread | 49-51 | 49.0 | 50.9 | -1.9 | -5.6 | -5.6 |  |  | no edge shown yet |
| rlm_quiet | total | 97-131 | 42.5 | 49.7 | -7.2 | -41.97 | -18.4 |  |  | DROP: below break-even |
| pin_move | moneyline | 118-117 | 50.2 | 48.9 | 1.3 | +5.89 | 2.5 |  |  | no edge shown yet |
| pin_move | spread | 216-227 | 48.8 | 50.3 | -1.5 | -30.19 | -6.8 |  |  | DROP: below break-even |
| pin_move | total | 217-223 | 49.3 | 49.9 | -0.6 | -24.71 | -5.6 |  |  | no edge shown yet |
| money_delta | moneyline | 58-182 | 24.2 | 29.0 | -4.8 | -46.69 | -19.5 |  |  | DROP: below break-even |
| money_delta | spread | 126-128 | 49.6 | 50.9 | -1.3 | -13.2 | -5.2 |  |  | no edge shown yet |
| money_delta | total | 166-153 | 52.0 | 49.7 | 2.3 | -1.0 | -0.3 |  |  | no edge shown yet |
| pin_rlm | moneyline | 41-83 | 33.1 | 29.1 | 3.9 | +15.33 | 12.4 |  |  | DROP: below break-even |
| pin_rlm | spread | 25-23 | 52.1 | 51.1 | 1.0 | -0.21 | -0.4 |  |  | no edge shown yet |
| pin_rlm | total | 83-74 | 52.9 | 49.6 | 3.2 | +2.11 | 1.3 |  |  | no edge shown yet |
| follow_move | moneyline | 346-247 | 58.3 | 55.2 | 3.2 | -33.46 | -5.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 269-292 | 48.0 | 49.6 | -1.6 | -47.59 | -8.5 |  |  | DROP: below break-even |
| follow_move | total | 327-349 | 48.4 | 50.0 | -1.6 | -50.49 | -7.5 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 41-100 | 29.1 | 30.2 | -1.1 | -18.49 | -13.1 |  |  | DROP: below break-even |
| rlm_ratio | spread | 41-45 | 47.7 | 50.2 | -2.5 | -7.76 | -9.0 |  |  | no edge shown yet |
| rlm_ratio | total | 135-118 | 53.4 | 49.7 | 3.7 | +5.62 | 2.2 |  |  | no edge shown yet |
| money_level | moneyline | 470-184 | 71.9 | 68.4 | 3.5 | -27.12 | -4.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 338-349 | 49.2 | 49.2 | 0.0 | -44.25 | -6.4 |  |  | DROP: below break-even |
| money_level | total | 402-358 | 52.9 | 50.1 | 2.8 | +6.95 | 0.9 |  |  | no edge shown yet |
| sharp_gap | moneyline | 231-368 | 38.6 | 42.2 | -3.7 | -69.59 | -11.6 |  |  | DROP: below break-even |
| sharp_gap | spread | 342-338 | 50.3 | 49.5 | 0.8 | -29.57 | -4.3 |  |  | no edge shown yet |
| sharp_gap | total | 357-381 | 48.4 | 49.9 | -1.5 | -54.96 | -7.4 |  |  | DROP: below break-even |
| money_moving | moneyline | 242-355 | 40.5 | 43.3 | -2.8 | -56.85 | -9.5 |  |  | DROP: below break-even |
| money_moving | spread | 339-341 | 49.9 | 49.5 | 0.4 | -35.44 | -5.2 |  |  | no edge shown yet |
| money_moving | total | 354-390 | 47.6 | 49.9 | -2.3 | -66.88 | -9.0 |  |  | DROP: below break-even |
| pin_value | moneyline | 22-55 | 28.6 | 32.0 | -3.4 | +28.96 | 37.6 |  |  | DROP: below break-even |
| pin_value | spread | 183-160 | 53.4 | 49.5 | 3.8 | -0.49 | -0.1 |  |  | no edge shown yet |
| pin_value | total | 203-179 | 53.1 | 50.1 | 3.1 | +3.64 | 1.0 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.7 | 47.3 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 165-287 | 36.5 | 46.3 | -9.8 | -74.03 | -16.4 |  |  | DROP: below break-even |
| consensus_gap | spread | 95-80 | 54.3 | 49.1 | 5.2 | +1.06 | 0.6 |  |  | no edge shown yet |
| consensus_gap | total | 118-109 | 52.0 | 50.3 | 1.7 | -4.13 | -1.8 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 170-98 | 63.4 | 62.7 | 0.7 | -7.76 | -2.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 158-96 | 62.2 | 62.2 | 0.1 | -8.07 | -3.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 217-341 | 38.9 | 42.3 | -3.4 | -53.82 | -9.6 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 62-73 | 45.9 | 53.5 | -7.6 | -20.07 | -14.9 |  |  | DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 8-41 | 16.3 | 29.2 | -12.8 | -12.64 | -25.8 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 60-136 | 30.6 | 28.0 | 2.6 | -12.58 | -6.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 115-70 | 62.2 | 69.0 | -6.9 | -13.49 | -7.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 65-161 | 28.8 | 41.6 | -12.8 | -22.97 | -10.2 |  |  | !! CHECK: consensus_gap+money_moving close moneyline all sits -12.8 pts from its base (41.6%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+money_level | moneyline | 266-93 | 74.1 | 69.7 | 4.4 | -15.87 | -4.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+money_moving | moneyline | 116-131 | 47.0 | 47.9 | -0.9 | -24.99 | -10.1 |  |  | DROP: below break-even |
| money_delta+money_moving | moneyline | 54-164 | 24.8 | 28.5 | -3.8 | -32.5 | -14.9 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 52-163 | 24.2 | 28.6 | -4.4 | -33.69 | -15.7 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 62-167 | 27.1 | 40.4 | -13.3 | -26.99 | -11.8 |  |  | !! CHECK: consensus_gap+sharp_gap close moneyline all sits -13.3 pts from its base (40.4%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+sharp_gap | moneyline | 113-133 | 45.9 | 46.9 | -0.9 | -27.41 | -11.1 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | moneyline | 25-81 | 23.6 | 28.2 | -4.6 | -17.59 | -16.6 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 26-85 | 23.4 | 28.1 | -4.7 | -22.13 | -19.9 |  |  | DROP: below break-even |
| consensus_gap+pin_move | moneyline | 34-37 | 47.9 | 52.9 | -5.0 | +9.16 | 12.9 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 11-30 | 26.8 | 30.6 | -3.8 | +8.65 | 21.1 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 5-34 | 12.8 | 29.6 | -16.8 | -10.04 | -25.7 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 94-82 | 53.4 | 50.5 | 2.9 | +1.5 | 0.9 |  |  | no edge shown yet |
| follow_move+pin_rlm | moneyline | 27-47 | 36.5 | 29.8 | 6.7 | -2.18 | -2.9 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 41-100 | 29.1 | 30.2 | -1.1 | -18.49 | -13.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 51-68 | 42.9 | 42.6 | 0.3 | +8.62 | 7.2 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 40-80 | 33.3 | 29.2 | 4.1 | +16.93 | 14.1 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 40-94 | 29.9 | 30.3 | -0.5 | -13.89 | -10.4 |  |  | DROP: below break-even |
| pin_move+pin_rlm | moneyline | 29-52 | 35.8 | 29.0 | 6.8 | +12.21 | 15.1 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 27-41 | 39.7 | 28.6 | 11.1 | +6.61 | 9.7 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 23-36 | 39.0 | 30.4 | 8.6 | +4.3 | 7.3 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 51-71 | 41.8 | 41.8 | -0.0 | +5.45 | 4.5 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 15-38 | 28.3 | 29.0 | -0.7 | -9.18 | -17.3 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 27-47 | 36.5 | 29.8 | 6.7 | -2.18 | -2.9 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 41-83 | 33.1 | 29.1 | 3.9 | +15.33 | 12.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 24-81 | 22.9 | 28.2 | -5.3 | -20.91 | -19.9 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 41-100 | 29.1 | 30.2 | -1.1 | -18.49 | -13.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 14-83 | 14.4 | 29.2 | -14.7 | -24.27 | -25.0 |  |  | DROP: below break-even |
| consensus_gap+pin_value | moneyline | 15-45 | 25.0 | 31.1 | -6.1 | +6.77 | 11.3 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 18-39 | 31.6 | 30.5 | 1.1 | -1.14 | -2.0 |  |  | DROP: below break-even |
| money_delta+pin_rlm | moneyline | 24-50 | 32.4 | 29.1 | 3.3 | +3.65 | 4.9 |  |  | DROP: below break-even |
| money_delta+pin_value | moneyline | 3-18 | 14.3 | 27.3 | -13.0 | -6.68 | -31.8 |  |  | keep collecting (21/30) |
| money_moving+pin_value | moneyline | 11-33 | 25.0 | 30.4 | -5.4 | +12.94 | 29.4 |  |  | DROP: below break-even |
| pin_move+pin_value | moneyline | 6-10 | 37.5 | 35.8 | 1.7 | +6.27 | 39.2 |  |  | keep collecting (16/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 27.3 | 3.9 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 11-35 | 23.9 | 30.3 | -6.3 | +10.94 | 23.8 |  |  | DROP: below break-even |
| follow_move+money_delta | moneyline | 26-59 | 30.6 | 31.6 | -1.0 | -19.22 | -22.6 |  |  | DROP: below break-even |
| money_delta+money_level | moneyline | 16-25 | 39.0 | 31.7 | 7.3 | +6.85 | 16.7 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | moneyline | 23-49 | 31.9 | 31.1 | 0.9 | -11.98 | -16.6 |  |  | DROP: below break-even |
| money_level+pin_move | moneyline | 76-47 | 61.8 | 66.4 | -4.6 | -6.42 | -5.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 12-11 | 52.2 | 33.2 | 19.0 | +4.79 | 20.8 |  |  | keep collecting (23/30) |
| money_level+rlm_ratio | moneyline | 15-14 | 51.7 | 38.3 | 13.5 | +5.04 | 17.4 |  |  | keep collecting (29/30) |
| money_delta+rlm_quiet | moneyline | 16-44 | 26.7 | 29.6 | -2.9 | -17.95 | -29.9 |  |  | DROP: below break-even |
| money_level+pin_value | moneyline | 5-3 | 62.5 | 67.0 | -4.5 | -0.32 | -4.0 |  |  | keep collecting (8/30) |
| follow_move+pin_value | moneyline | 3-8 | 27.3 | 35.6 | -8.3 | +4.8 | 43.7 |  |  | keep collecting (11/30) |
| pin_value+rlm_quiet | moneyline | 2-6 | 25.0 | 27.3 | -2.3 | +6.12 | 76.5 |  |  | keep collecting (8/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 27.3 | -2.3 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 36-28 | 56.2 | 48.5 | 7.7 | +2.72 | 4.3 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 49-45 | 52.1 | 48.8 | 3.3 | -3.18 | -3.4 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 27-30 | 47.4 | 49.2 | -1.8 | -6.91 | -12.1 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | -0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 68-50 | 57.6 | 49.0 | 8.7 | +7.87 | 6.7 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 4-4 | 50.0 | 50.0 | 0.0 | -0.67 | -8.3 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | spread | 48-45 | 51.6 | 49.0 | 2.6 | -4.08 | -4.4 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 160-169 | 48.6 | 49.2 | -0.6 | -24.45 | -7.4 |  |  | no edge shown yet |
| follow_move+pin_move | spread | 134-152 | 46.9 | 50.0 | -3.1 | -29.96 | -10.5 |  |  | DROP: below break-even |
| follow_move+pin_rlm | spread | 19-19 | 50.0 | 50.8 | -0.8 | -1.65 | -4.3 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 64-52 | 55.2 | 49.0 | 6.1 | +3.9 | 3.4 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 41-45 | 47.7 | 50.2 | -2.5 | -7.76 | -9.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 161-168 | 48.9 | 49.2 | -0.3 | -22.32 | -6.8 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 122-133 | 47.8 | 49.8 | -2.0 | -22.48 | -8.8 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 23-23 | 50.0 | 51.0 | -1.0 | -2.04 | -4.4 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 85-87 | 49.4 | 49.1 | 0.3 | -13.64 | -7.9 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 39-44 | 47.0 | 50.1 | -3.1 | -8.69 | -10.5 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 334-333 | 50.1 | 49.5 | 0.6 | -31.94 | -4.8 |  |  | no edge shown yet |
| pin_move+pin_rlm | spread | 25-23 | 52.1 | 51.1 | 1.0 | -0.21 | -0.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 84-83 | 50.3 | 49.7 | 0.6 | -8.98 | -5.4 |  |  | no edge shown yet |
| pin_move+rlm_ratio | spread | 22-26 | 45.8 | 50.7 | -4.8 | -5.94 | -12.4 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 125-133 | 48.4 | 49.8 | -1.4 | -19.74 | -7.7 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 7-10 | 41.2 | 50.8 | -9.6 | -3.88 | -22.8 |  |  | keep collecting (17/30) |
| pin_rlm+rlm_ratio | spread | 19-19 | 50.0 | 50.8 | -0.8 | -1.65 | -4.3 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 25-23 | 52.1 | 51.1 | 1.0 | -0.21 | -0.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 7-8 | 46.7 | 49.5 | -2.8 | -2.01 | -13.4 |  |  | keep collecting (15/30) |
| pin_value+sharp_gap | spread | 85-87 | 49.4 | 49.2 | 0.2 | -13.7 | -8.0 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 41-45 | 47.7 | 50.2 | -2.5 | -7.76 | -9.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 156-170 | 47.9 | 48.9 | -1.1 | -29.0 | -8.9 |  |  | DROP: below break-even |
| money_level+rlm_ratio | spread | 21-28 | 42.9 | 49.8 | -7.0 | -9.13 | -18.6 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 260-260 | 50.0 | 49.2 | 0.8 | -25.93 | -5.0 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 59-49 | 54.6 | 48.6 | 6.1 | +1.47 | 1.4 |  |  | no edge shown yet |
| money_level+money_moving | spread | 259-261 | 49.8 | 49.1 | 0.7 | -27.85 | -5.4 |  |  | no edge shown yet |
| money_level+pin_move | spread | 111-133 | 45.5 | 49.6 | -4.1 | -32.82 | -13.5 |  |  | DROP: below break-even |
| money_level+pin_value | spread | 91-91 | 50.0 | 48.9 | 1.1 | -12.48 | -6.9 |  |  | no edge shown yet |
| consensus_gap+money_delta | spread | 15-14 | 51.7 | 50.6 | 1.1 | -1.18 | -4.1 |  |  | keep collecting (29/30) |
| follow_move+money_delta | spread | 39-49 | 44.3 | 50.3 | -6.0 | -13.71 | -15.6 |  |  | DROP: below break-even |
| money_delta+money_level | spread | 41-40 | 50.6 | 50.0 | 0.6 | -3.05 | -3.8 |  |  | no edge shown yet |
| money_delta+money_moving | spread | 71-75 | 48.6 | 50.5 | -1.9 | -10.91 | -7.5 |  |  | no edge shown yet |
| money_delta+pin_value | spread | 33-27 | 55.0 | 50.6 | 4.4 | +1.79 | 3.0 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 70-73 | 49.0 | 50.5 | -1.5 | -9.89 | -6.9 |  |  | no edge shown yet |
| follow_move+rlm_quiet | spread | 49-51 | 49.0 | 50.9 | -1.9 | -5.6 | -5.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 14-5 | 73.7 | 51.0 | 22.7 | +7.78 | 40.9 |  |  | keep collecting (19/30) |
| rlm_quiet+sharp_gap | spread | 22-12 | 64.7 | 51.1 | 13.6 | +8.13 | 23.9 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 14-11 | 56.0 | 50.5 | 5.5 | +1.57 | 6.3 |  |  | keep collecting (25/30) |
| money_delta+pin_move | spread | 37-45 | 45.1 | 51.1 | -6.0 | -11.18 | -13.6 |  |  | no edge shown yet |
| money_delta+rlm_ratio | spread | 16-27 | 37.2 | 49.9 | -12.7 | -12.78 | -29.7 |  |  | DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 52.7 | 47.3 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_rlm | spread | 13-16 | 44.8 | 50.8 | -6.0 | -4.31 | -14.8 |  |  | keep collecting (29/30) |
| money_delta+rlm_quiet | spread | 15-18 | 45.5 | 51.4 | -5.9 | -4.16 | -12.6 |  |  | no edge shown yet |
| money_moving+rlm_quiet | spread | 21-12 | 63.6 | 51.0 | 12.6 | +7.18 | 21.7 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 28-25 | 52.8 | 51.4 | 1.5 | +0.97 | 1.8 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-2 | 75.0 | 52.0 | 23.0 | +3.56 | 44.5 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_quiet | spread | 4-3 | 57.1 | 51.1 | 6.0 | +0.48 | 6.9 |  |  | keep collecting (7/30) |
| pin_value+rlm_quiet | spread | 6-4 | 60.0 | 49.5 | 10.5 | +1.3 | 13.0 |  |  | keep collecting (10/30) |
| follow_move+money_delta | total | 103-98 | 51.2 | 49.7 | 1.5 | -3.74 | -1.9 |  |  | no edge shown yet |
| money_level+money_moving | total | 231-228 | 50.3 | 50.0 | 0.3 | -17.53 | -3.8 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 229-221 | 50.9 | 50.0 | 0.9 | -12.24 | -2.7 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 344-372 | 48.0 | 49.9 | -1.8 | -57.9 | -8.1 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 62-59 | 51.2 | 50.4 | 0.8 | -3.91 | -3.2 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 29-23 | 55.8 | 50.2 | 5.5 | +2.74 | 5.3 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 70-62 | 53.0 | 50.3 | 2.8 | +0.14 | 0.1 |  |  | no edge shown yet |
| follow_move+money_moving | total | 218-249 | 46.7 | 49.9 | -3.2 | -50.17 | -10.7 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 226-247 | 47.8 | 49.9 | -2.1 | -40.86 | -8.6 |  |  | DROP: below break-even |
| money_level+pin_move | total | 131-116 | 53.0 | 50.0 | 3.0 | +3.38 | 1.4 |  |  | no edge shown yet |
| money_level+pin_value | total | 98-80 | 55.1 | 50.3 | 4.8 | +7.76 | 4.4 |  |  | no edge shown yet |
| pin_move+pin_value | total | 83-77 | 51.9 | 50.0 | 1.9 | -2.09 | -1.3 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 97-131 | 42.5 | 49.7 | -7.2 | -41.97 | -18.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 148-159 | 48.2 | 49.8 | -1.6 | -23.75 | -7.7 |  |  | no edge shown yet |
| rlm_quiet+sharp_gap | total | 59-85 | 41.0 | 49.7 | -8.7 | -30.95 | -21.5 |  |  | DROP: below break-even |
| money_delta+money_moving | total | 126-120 | 51.2 | 49.7 | 1.5 | -4.76 | -1.9 |  |  | no edge shown yet |
| follow_move+money_level | total | 184-179 | 50.7 | 50.1 | 0.6 | -11.59 | -3.2 |  |  | no edge shown yet |
| follow_move+pin_value | total | 72-71 | 50.3 | 50.0 | 0.3 | -6.11 | -4.3 |  |  | no edge shown yet |
| money_moving+pin_value | total | 78-84 | 48.1 | 50.0 | -1.9 | -13.71 | -8.5 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 79-82 | 49.1 | 50.0 | -0.9 | -10.76 | -6.7 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 50-52 | 49.0 | 50.2 | -1.2 | -7.59 | -7.4 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 52-50 | 51.0 | 50.2 | 0.8 | -3.81 | -3.7 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 45-37 | 54.9 | 50.3 | 4.6 | +2.88 | 3.5 |  |  | no edge shown yet |
| consensus_gap+money_delta | total | 18-14 | 56.2 | 50.0 | 6.2 | +1.83 | 5.7 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | total | 11-9 | 55.0 | 49.9 | 5.1 | +0.81 | 4.1 |  |  | keep collecting (20/30) |
| money_delta+rlm_quiet | total | 27-47 | 36.5 | 49.6 | -13.1 | -22.27 | -30.1 |  |  | DROP: below break-even |
| money_delta+sharp_gap | total | 126-117 | 51.9 | 49.7 | 2.2 | -1.76 | -0.7 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 53-83 | 39.0 | 49.6 | -10.7 | -34.45 | -25.3 |  |  | DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 68-51 | 57.1 | 49.8 | 7.4 | +11.1 | 9.3 |  |  | no edge shown yet |
| money_delta+pin_move | total | 72-70 | 50.7 | 49.6 | 1.1 | -4.01 | -2.8 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 150-159 | 48.5 | 49.8 | -1.3 | -21.84 | -7.1 |  |  | no edge shown yet |
| follow_move+pin_move | total | 165-179 | 48.0 | 49.9 | -1.9 | -28.08 | -8.2 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | total | 21-29 | 42.0 | 49.7 | -7.7 | -9.76 | -19.5 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | total | 10-9 | 52.6 | 50.0 | 2.6 | -0.13 | -0.7 |  |  | keep collecting (19/30) |
| consensus_gap+rlm_ratio | total | 19-9 | 67.9 | 50.1 | 17.7 | +7.85 | 28.0 |  |  | keep collecting (28/30) |
| follow_move+pin_rlm | total | 71-64 | 52.6 | 49.6 | 2.9 | +1.34 | 1.0 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 135-118 | 53.4 | 49.7 | 3.7 | +5.62 | 2.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 42-27 | 60.9 | 49.6 | 11.2 | +11.63 | 16.9 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 68-47 | 59.1 | 49.8 | 9.4 | +15.19 | 13.2 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 80-72 | 52.6 | 49.6 | 3.0 | +1.37 | 0.9 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 130-116 | 52.8 | 49.7 | 3.1 | +3.04 | 1.2 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 83-74 | 52.9 | 49.6 | 3.2 | +2.11 | 1.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 79-65 | 54.9 | 49.7 | 5.2 | +7.5 | 5.2 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 29-22 | 56.9 | 49.7 | 7.1 | +4.3 | 8.4 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 71-64 | 52.6 | 49.6 | 2.9 | +1.34 | 1.0 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 83-74 | 52.9 | 49.6 | 3.2 | +2.11 | 1.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 33-22 | 60.0 | 49.8 | 10.2 | +7.91 | 14.4 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 135-118 | 53.4 | 49.7 | 3.7 | +5.62 | 2.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 51-41 | 55.4 | 49.6 | 5.8 | +5.87 | 6.4 |  |  | no edge shown yet |
| money_delta+rlm_ratio | total | 84-61 | 57.9 | 49.7 | 8.3 | +15.79 | 10.9 |  |  | no edge shown yet |
| money_delta+pin_value | total | 42-29 | 59.2 | 49.8 | 9.4 | +9.01 | 12.7 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 46-68 | 40.4 | 49.7 | -9.4 | -25.69 | -22.5 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | total | 24-35 | 40.7 | 49.6 | -8.9 | -13.0 | -22.0 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | total | 47-64 | 42.3 | 49.6 | -7.3 | -20.91 | -18.8 |  |  | DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 49.5 | 50.5 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| rlm_quiet | close | 1-3k bets | 135-211 | 39.0 | -2.6 | -10.0 |  |
| rlm_quiet | close | 3k+ bets | 47-65 | 42.0 | -0.8 | -9.1 |  |
| rlm_quiet | close | <1k bets | 24-42 | 36.4 | -4.8 | -23.0 |  |
| rlm_quiet | close | pin $1-2k | 55-101 | 35.3 | -7.8 | -20.6 |  |
| rlm_quiet | close | pin $2k+ | 60-74 | 44.8 | 6.9 | 3.7 |  |
| rlm_quiet | close | pin limit <$1k | 40-44 | 47.6 | -1.6 | -8.7 |  |
| pin_move | close | 1-3k bets | 351-354 | 49.8 | 0.1 | -3.1 |  |
| pin_move | close | 3k+ bets | 127-135 | 48.5 | -1.3 | -6.3 |  |
| pin_move | close | <1k bets | 73-78 | 48.3 | -2.2 | -7.3 |  |
| pin_move | close | pin $1-2k | 261-260 | 50.1 | -0.0 | -1.7 |  |
| pin_move | close | pin $2k+ | 193-208 | 48.1 | -1.5 | -8.6 |  |
| pin_move | close | pin limit <$1k | 97-99 | 49.5 | -0.0 | -3.1 |  |
| money_delta | close | 1-3k bets | 219-280 | 43.9 | -0.7 | -7.5 |  |
| money_delta | close | 3k+ bets | 85-111 | 43.4 | 0.0 | -1.0 |  |
| money_delta | close | <1k bets | 46-72 | 39.0 | -3.3 | -18.0 |  |
| money_delta | close | pin $1-2k | 125-127 | 49.6 | 3.8 | 4.4 |  |
| money_delta | close | pin $2k+ | 87-120 | 42.0 | 1.0 | -10.4 |  |
| money_delta | close | pin limit <$1k | 57-63 | 47.5 | -1.7 | -5.3 |  |
| pin_rlm | close | 1-3k bets | 93-108 | 46.3 | 3.9 | 11.2 |  |
| pin_rlm | close | 3k+ bets | 34-47 | 42.0 | -0.2 | -8.3 |  |
| pin_rlm | close | <1k bets | 22-25 | 46.8 | 5.9 | 3.2 |  |
| pin_rlm | close | pin $1-2k | 66-71 | 48.2 | 4.5 | 9.9 |  |
| pin_rlm | close | pin $2k+ | 39-72 | 35.1 | -0.4 | -7.8 |  |
| pin_rlm | close | pin limit <$1k | 44-37 | 54.3 | 5.8 | 15.2 |  |
| follow_move | close | 1-3k bets | 606-568 | 51.6 | 0.4 | -6.2 |  |
| follow_move | close | 3k+ bets | 201-187 | 51.8 | -0.1 | -5.1 |  |
| follow_move | close | <1k bets | 135-133 | 50.4 | -2.0 | -14.4 |  |
| follow_move | close | pin $1-2k | 289-325 | 47.1 | -3.8 | -12.0 |  |
| follow_move | close | pin $2k+ | 246-208 | 54.2 | 2.4 | -1.7 |  |
| follow_move | close | pin limit <$1k | 117-123 | 48.8 | -1.1 | -6.9 |  |
| rlm_ratio | close | 1-3k bets | 137-184 | 42.7 | -1.5 | -9.0 |  |
| rlm_ratio | close | 3k+ bets | 51-46 | 52.6 | 8.0 | 12.4 |  |
| rlm_ratio | close | <1k bets | 29-33 | 46.8 | 3.9 | -6.3 |  |
| rlm_ratio | close | pin $1-2k | 77-79 | 49.4 | 3.5 | 2.7 |  |
| rlm_ratio | close | pin $2k+ | 39-60 | 39.4 | 1.4 | -12.7 |  |
| rlm_ratio | close | pin limit <$1k | 49-42 | 53.8 | 4.9 | 4.0 |  |
| money_level | close | 1-3k bets | 780-556 | 58.4 | 2.8 | -2.1 |  |
| money_level | close | 3k+ bets | 259-206 | 55.7 | 0.6 | -3.4 |  |
| money_level | close | <1k bets | 171-128 | 57.2 | 1.5 | -6.8 |  |
| money_level | close | pin $1-2k | 358-305 | 54.0 | 0.0 | -4.0 |  |
| money_level | close | pin $2k+ | 307-241 | 56.0 | -1.4 | -7.9 |  |
| money_level | close | pin limit <$1k | 142-135 | 51.3 | 0.9 | -2.5 |  |
| sharp_gap | close | 1-3k bets | 575-701 | 45.1 | -2.3 | -10.3 |  |
| sharp_gap | close | 3k+ bets | 223-232 | 49.0 | 1.4 | 2.7 |  |
| sharp_gap | close | <1k bets | 132-153 | 46.3 | -1.4 | -11.9 |  |
| sharp_gap | close | pin $1-2k | 305-336 | 47.6 | -1.1 | -5.2 |  |
| sharp_gap | close | pin $2k+ | 243-284 | 46.1 | -0.3 | -4.5 |  |
| sharp_gap | close | pin limit <$1k | 125-140 | 47.2 | -2.2 | -6.2 |  |
| money_moving | close | 1-3k bets | 583-698 | 45.5 | -2.4 | -10.4 |  |
| money_moving | close | 3k+ bets | 222-234 | 48.7 | 0.8 | 1.3 |  |
| money_moving | close | <1k bets | 130-153 | 45.9 | -1.5 | -10.9 |  |
| money_moving | close | pin $1-2k | 303-339 | 47.2 | -1.8 | -6.0 |  |
| money_moving | close | pin $2k+ | 244-282 | 46.4 | -0.0 | -4.5 |  |
| money_moving | close | pin limit <$1k | 123-146 | 45.7 | -3.7 | -9.0 |  |
| pin_value | close | 1-3k bets | 260-256 | 50.4 | 2.3 | 4.4 |  |
| pin_value | close | 3k+ bets | 84-91 | 48.0 | -0.7 | -6.1 |  |
| pin_value | close | <1k bets | 64-47 | 57.7 | 10.3 | 18.0 |  |
| pin_value | close | pin $1-2k | 188-202 | 48.2 | -0.1 | -1.8 |  |
| pin_value | close | pin $2k+ | 111-122 | 47.6 | 1.3 | 3.0 |  |
| pin_value | close | pin limit <$1k | 109-70 | 60.9 | 10.9 | 17.9 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.3 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.3 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 243-298 | 44.9 | -3.8 | -10.7 |  |
| consensus_gap | close | 3k+ bets | 84-98 | 46.2 | -1.5 | 4.5 |  |
| consensus_gap | close | <1k bets | 51-79 | 39.2 | -5.8 | -20.2 |  |
| consensus_gap | close | pin $1-2k | 119-128 | 48.2 | -1.4 | 0.8 |  |
| consensus_gap | close | pin $2k+ | 104-111 | 48.4 | -2.2 | -2.4 |  |
| consensus_gap | close | pin limit <$1k | 56-45 | 55.4 | 5.1 | 8.0 |  |
| consensus_gap+follow_move | close | 1-3k bets | 99-91 | 52.1 | 0.3 | -2.6 |  |
| consensus_gap+money_level | close | 1-3k bets | 164-106 | 60.7 | 1.7 | 3.2 |  |
| consensus_gap+money_moving | close | 1-3k bets | 106-164 | 39.3 | -6.7 | -12.1 |  |
| consensus_gap+pin_move | close | 1-3k bets | 60-58 | 50.8 | -0.3 | 4.4 |  |
| consensus_gap+pin_value | close | 1-3k bets | 99-110 | 47.4 | 1.0 | -0.7 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 103-167 | 38.1 | -6.9 | -13.2 |  |
| follow_move+money_level | close | 1-3k bets | 399-285 | 58.3 | 2.2 | -4.3 |  |
| follow_move+money_moving | close | 1-3k bets | 326-366 | 47.1 | -2.1 | -10.3 |  |
| follow_move+pin_move | close | 1-3k bets | 250-265 | 48.5 | -1.3 | -7.7 |  |
| follow_move+pin_value | close | 1-3k bets | 85-85 | 50.0 | 1.4 | 0.4 |  |
| follow_move+sharp_gap | close | 1-3k bets | 328-366 | 47.3 | -1.6 | -9.1 |  |
| money_level+money_moving | close | 1-3k bets | 420-374 | 52.9 | 0.4 | -4.3 |  |
| money_level+pin_move | close | 1-3k bets | 213-193 | 52.5 | -0.3 | -4.4 |  |
| money_level+pin_value | close | 1-3k bets | 125-111 | 53.0 | 3.3 | -0.6 |  |
| money_level+sharp_gap | close | 1-3k bets | 405-367 | 52.5 | 0.3 | -4.1 |  |
| money_moving+pin_move | close | 1-3k bets | 210-229 | 47.8 | -1.1 | -4.1 |  |
| money_moving+pin_value | close | 1-3k bets | 111-135 | 45.1 | -2.4 | -7.1 |  |
| money_moving+sharp_gap | close | 1-3k bets | 552-670 | 45.2 | -2.4 | -9.9 |  |
| pin_move+pin_value | close | 1-3k bets | 111-107 | 50.9 | 1.7 | -0.2 |  |
| pin_move+sharp_gap | close | 1-3k bets | 215-231 | 48.2 | -0.5 | -3.0 |  |
| pin_value+sharp_gap | close | 1-3k bets | 112-137 | 45.0 | -2.3 | -7.5 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 135-211 | 39.0 | -2.6 | -10.0 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 68-128 | 34.7 | -6.5 | -18.5 |  |
| consensus_gap+money_delta | close | 1-3k bets | 27-66 | 29.0 | -8.6 | -22.4 |  |
| follow_move+money_delta | close | 1-3k bets | 105-130 | 44.7 | -1.7 | -11.4 |  |
| money_delta+money_level | close | 1-3k bets | 78-75 | 51.0 | 3.1 | 5.3 |  |
| money_delta+money_moving | close | 1-3k bets | 153-221 | 40.9 | -1.9 | -10.5 |  |
| money_delta+pin_value | close | 1-3k bets | 50-47 | 51.5 | 3.9 | 2.7 |  |
| money_delta+sharp_gap | close | 1-3k bets | 152-218 | 41.1 | -1.8 | -10.1 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 76-90 | 45.8 | -1.2 | -2.5 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 18-29 | 38.3 | -0.5 | 13.3 |  |
| money_level+pin_rlm | close | 1-3k bets | 43-32 | 57.3 | 9.1 | 10.5 |  |
| pin_move+pin_rlm | close | 1-3k bets | 85-88 | 49.1 | 4.8 | 8.7 |  |
| pin_rlm+pin_value | close | 1-3k bets | 29-25 | 53.7 | 7.6 | 28.3 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 93-108 | 46.3 | 3.9 | 11.2 |  |
| money_delta+pin_rlm | close | 1-3k bets | 53-62 | 46.1 | 3.3 | 9.2 |  |
| money_moving+pin_rlm | close | 1-3k bets | 88-104 | 45.8 | 3.4 | 11.2 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 21-34 | 38.2 | -1.5 | -0.2 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 137-184 | 42.7 | -1.5 | -9.0 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 74-92 | 44.6 | -0.6 | -10.4 |  |
| money_level+rlm_ratio | close | 1-3k bets | 65-62 | 51.2 | 2.1 | -1.2 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 131-177 | 42.5 | -1.8 | -9.0 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 73-77 | 48.7 | 3.4 | 0.0 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 27-22 | 55.1 | 7.3 | 5.8 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 137-184 | 42.7 | -1.5 | -9.0 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 15-36 | 29.4 | -6.5 | -12.2 |  |
| follow_move+pin_rlm | close | 1-3k bets | 68-83 | 45.0 | 1.2 | -7.0 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 61-124 | 33.0 | -8.3 | -21.4 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 61-86 | 41.5 | -2.1 | -11.3 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 26-50 | 34.2 | -5.2 | -21.8 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 68-83 | 45.0 | 1.2 | -7.0 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 54-109 | 33.1 | -6.6 | -19.0 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 37-69 | 34.9 | -8.2 | -26.8 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 17-23 | 42.5 | -2.8 | 6.7 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 50.5 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 32-27 | 54.2 | 4.0 | 5.2 |  |
| consensus_gap+money_moving | close | 3k+ bets | 35-54 | 39.3 | -5.5 | 12.9 |  |
| consensus_gap+pin_move | close | 3k+ bets | 23-19 | 54.8 | 4.4 | 10.4 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-6 | 33.3 | -7.0 | 6.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 37-33 | 52.9 | 6.0 | 8.0 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -1.3 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 36-54 | 40.0 | -4.6 | 16.0 |  |
| follow_move+money_moving | close | 3k+ bets | 108-110 | 49.5 | 0.3 | -3.0 |  |
| follow_move+pin_move | close | 3k+ bets | 97-97 | 50.0 | -0.2 | -2.8 |  |
| follow_move+pin_rlm | close | 3k+ bets | 32-32 | 50.0 | 5.7 | 10.1 |  |
| follow_move+pin_value | close | 3k+ bets | 34-34 | 50.0 | -0.1 | -6.1 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 51-46 | 52.6 | 8.0 | 12.4 |  |
| follow_move+sharp_gap | close | 3k+ bets | 110-109 | 50.2 | 1.3 | -1.0 |  |
| money_moving+pin_move | close | 3k+ bets | 74-86 | 46.2 | -2.0 | -8.3 |  |
| money_moving+pin_rlm | close | 3k+ bets | 33-46 | 41.8 | -0.2 | -8.5 |  |
| money_moving+pin_value | close | 3k+ bets | 42-52 | 44.7 | -3.0 | -8.6 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 49-44 | 52.7 | 8.2 | 13.0 |  |
| money_moving+sharp_gap | close | 3k+ bets | 215-224 | 49.0 | 1.3 | 2.5 |  |
| pin_move+pin_rlm | close | 3k+ bets | 32-41 | 43.8 | 0.0 | -4.2 |  |
| pin_move+pin_value | close | 3k+ bets | 34-43 | 44.2 | -5.5 | -16.9 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 34-33 | 50.7 | 5.1 | 10.0 |  |
| pin_move+sharp_gap | close | 3k+ bets | 74-86 | 46.2 | -1.7 | -7.6 |  |
| pin_rlm+pin_value | close | 3k+ bets | 6-15 | 28.6 | -17.6 | -45.5 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 32-32 | 50.0 | 5.7 | 10.1 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 34-47 | 42.0 | -0.2 | -8.3 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 9-10 | 47.4 | -2.8 | -10.1 |  |
| pin_value+sharp_gap | close | 3k+ bets | 42-51 | 45.2 | -2.5 | -7.6 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 51-46 | 52.6 | 8.0 | 12.4 |  |
| follow_move+money_delta | close | 3k+ bets | 41-49 | 45.6 | 0.1 | -5.9 |  |
| money_level+money_moving | close | 3k+ bets | 151-130 | 53.7 | 1.5 | -0.6 |  |
| money_level+sharp_gap | close | 3k+ bets | 150-127 | 54.2 | 2.1 | 0.8 |  |
| follow_move+money_level | close | 3k+ bets | 125-93 | 57.3 | 0.9 | -2.9 |  |
| money_level+rlm_ratio | close | 3k+ bets | 25-12 | 67.6 | 20.4 | 38.4 |  |
| consensus_gap+money_level | close | 3k+ bets | 46-45 | 50.5 | -6.2 | -12.7 |  |
| money_level+pin_move | close | 3k+ bets | 68-64 | 51.5 | -2.1 | -5.4 |  |
| money_level+pin_value | close | 3k+ bets | 47-46 | 50.5 | -0.0 | -6.2 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 8-12 | 40.0 | 1.2 | -0.6 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 47-65 | 42.0 | -0.8 | -9.1 |  |
| money_delta+money_moving | close | 3k+ bets | 65-84 | 43.6 | 1.3 | 4.2 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 19-26 | 42.2 | 0.8 | -2.3 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 24-35 | 40.7 | -1.7 | -9.2 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 22-34 | 39.3 | -3.0 | -11.2 |  |
| consensus_gap+money_delta | close | 3k+ bets | 13-23 | 36.1 | -3.0 | 20.4 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 11-26 | 29.7 | -13.5 | -35.1 |  |
| money_delta+sharp_gap | close | 3k+ bets | 63-81 | 43.8 | 1.6 | 4.9 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 29-34 | 46.0 | 1.7 | -0.6 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 11-18 | 37.9 | -4.4 | -9.9 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 8-12 | 40.0 | -9.6 | -23.6 |  |
| money_delta+money_level | close | 3k+ bets | 33-22 | 60.0 | 13.9 | 21.2 |  |
| money_level+pin_rlm | close | 3k+ bets | 16-9 | 64.0 | 19.0 | 37.0 |  |
| money_delta+pin_value | close | 3k+ bets | 19-19 | 50.0 | 3.8 | -5.7 |  |
| money_delta+pin_move | close | 3k+ bets | 37-44 | 45.7 | 0.2 | -6.8 |  |
| money_delta+pin_rlm | close | 3k+ bets | 22-28 | 44.0 | 1.9 | -6.4 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 30-25 | 54.5 | 9.9 | 15.6 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 47.3 | 87.7 |  |
| money_level+money_moving | close | <1k bets | 89-82 | 52.0 | -0.2 | -9.6 |  |
| money_level+sharp_gap | close | <1k bets | 92-82 | 52.9 | 0.3 | -9.2 |  |
| money_moving+sharp_gap | close | <1k bets | 128-151 | 45.9 | -1.7 | -11.9 |  |
| consensus_gap+money_level | close | <1k bets | 26-27 | 49.1 | -7.9 | -24.4 |  |
| consensus_gap+money_moving | close | <1k bets | 23-40 | 36.5 | -6.7 | -19.8 |  |
| consensus_gap+pin_move | close | <1k bets | 7-13 | 35.0 | -15.8 | -22.6 |  |
| consensus_gap+pin_value | close | <1k bets | 17-14 | 54.8 | 12.8 | 34.1 |  |
| consensus_gap+sharp_gap | close | <1k bets | 23-41 | 35.9 | -7.0 | -21.1 |  |
| money_level+pin_move | close | <1k bets | 37-39 | 48.7 | -5.3 | -14.4 |  |
| money_level+pin_value | close | <1k bets | 22-17 | 56.4 | 6.2 | 5.5 |  |
| money_moving+pin_move | close | <1k bets | 37-45 | 45.1 | -2.3 | -7.7 |  |
| money_moving+pin_value | close | <1k bets | 21-17 | 55.3 | 10.2 | 29.4 |  |
| pin_move+pin_value | close | <1k bets | 28-20 | 58.3 | 9.9 | 17.8 |  |
| pin_move+sharp_gap | close | <1k bets | 37-46 | 44.6 | -3.4 | -12.7 |  |
| pin_value+sharp_gap | close | <1k bets | 21-16 | 56.8 | 11.2 | 32.9 |  |
| follow_move+money_delta | close | <1k bets | 22-27 | 44.9 | 1.8 | -9.5 |  |
| follow_move+money_moving | close | <1k bets | 60-73 | 45.1 | -4.2 | -16.5 |  |
| follow_move+pin_move | close | <1k bets | 46-51 | 47.4 | -3.6 | -12.1 |  |
| follow_move+sharp_gap | close | <1k bets | 62-73 | 45.9 | -4.0 | -18.5 |  |
| money_delta+money_moving | close | <1k bets | 33-54 | 37.9 | -2.3 | -17.2 |  |
| money_delta+pin_move | close | <1k bets | 14-20 | 41.2 | -2.6 | -19.8 |  |
| money_delta+sharp_gap | close | <1k bets | 33-54 | 37.9 | -2.3 | -17.2 |  |
| follow_move+rlm_quiet | close | <1k bets | 24-42 | 36.4 | -4.8 | -23.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 29-33 | 46.8 | 3.9 | -6.3 |  |
| money_delta+rlm_quiet | close | <1k bets | 10-14 | 41.7 | 1.4 | -12.4 |  |
| money_delta+rlm_ratio | close | <1k bets | 19-20 | 48.7 | 6.7 | -0.8 |  |
| money_moving+rlm_quiet | close | <1k bets | 16-18 | 47.1 | 5.5 | 3.1 |  |
| money_moving+rlm_ratio | close | <1k bets | 29-33 | 46.8 | 3.9 | -6.3 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 12-15 | 44.4 | 4.0 | -7.6 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 15-19 | 44.1 | 1.9 | -9.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 29-33 | 46.8 | 3.9 | -6.3 |  |
| follow_move+money_level | close | <1k bets | 82-64 | 56.2 | -1.6 | -14.0 |  |
| consensus_gap+money_delta | close | <1k bets | 7-22 | 24.1 | -10.0 | -35.0 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -1.8 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 13-17 | 43.3 | 4.3 | -7.1 |  |
| money_moving+pin_rlm | close | <1k bets | 22-25 | 46.8 | 5.9 | 3.2 |  |
| pin_rlm+sharp_gap | close | <1k bets | 22-25 | 46.8 | 5.9 | 3.2 |  |
| money_delta+pin_value | close | <1k bets | 9-8 | 52.9 | 7.5 | 21.5 |  |
| consensus_gap+follow_move | close | <1k bets | 12-20 | 37.5 | -13.9 | -39.6 |  |
| follow_move+pin_rlm | close | <1k bets | 17-15 | 53.1 | 10.0 | 5.0 |  |
| follow_move+pin_value | close | <1k bets | 20-12 | 62.5 | 13.7 | 18.7 |  |
| pin_move+pin_rlm | close | <1k bets | 20-20 | 50.0 | 6.7 | 5.4 |  |
| pin_move+rlm_quiet | close | <1k bets | 11-14 | 44.0 | -1.1 | -4.7 |  |
| pin_move+rlm_ratio | close | <1k bets | 17-17 | 50.0 | 5.2 | -2.4 |  |
| pin_rlm+pin_value | close | <1k bets | 6-3 | 66.7 | 24.8 | 64.1 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 8-7 | 53.3 | 9.7 | 5.4 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 17-15 | 53.1 | 10.0 | 5.0 |  |
| pin_value+rlm_quiet | close | <1k bets | 4-4 | 50.0 | 0.8 | -4.0 |  |
| pin_value+rlm_ratio | close | <1k bets | 5-1 | 83.3 | 34.6 | 58.3 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -6.1 | -42.5 |  |
| money_delta+money_level | close | <1k bets | 14-19 | 42.4 | -0.2 | -14.7 |  |
| money_level+rlm_ratio | close | <1k bets | 14-15 | 48.3 | 3.6 | -5.5 |  |
| money_level+pin_rlm | close | <1k bets | 9-8 | 52.9 | 11.2 | 5.0 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 0-5 | 0.0 | -35.7 | -100.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 45-51 | 46.9 | -5.5 | -10.5 |  |
| consensus_gap+money_moving | close | pin $1-2k | 57-69 | 45.2 | -3.5 | -2.5 |  |
| consensus_gap+pin_move | close | pin $1-2k | 44-46 | 48.9 | -3.1 | 5.2 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-18 | 41.9 | 0.8 | 25.8 |  |
| consensus_gap+pin_value | close | pin $1-2k | 69-74 | 48.3 | 2.0 | -1.0 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-15 | 48.3 | 3.1 | 5.2 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 54-67 | 44.6 | -2.9 | -1.7 |  |
| follow_move+money_moving | close | pin $1-2k | 166-202 | 45.1 | -4.6 | -12.0 |  |
| follow_move+pin_move | close | pin $1-2k | 180-200 | 47.4 | -2.9 | -8.8 |  |
| follow_move+pin_rlm | close | pin $1-2k | 54-55 | 49.5 | 4.1 | 3.8 |  |
| follow_move+pin_value | close | pin $1-2k | 61-74 | 45.2 | -4.3 | -14.7 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 77-79 | 49.4 | 3.5 | 2.7 |  |
| follow_move+sharp_gap | close | pin $1-2k | 169-201 | 45.7 | -3.9 | -11.3 |  |
| money_moving+pin_move | close | pin $1-2k | 155-173 | 47.3 | -1.9 | -4.3 |  |
| money_moving+pin_rlm | close | pin $1-2k | 63-68 | 48.1 | 4.1 | 10.2 |  |
| money_moving+pin_value | close | pin $1-2k | 72-105 | 40.7 | -7.1 | -18.6 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 75-75 | 50.0 | 3.8 | 3.9 |  |
| money_moving+sharp_gap | close | pin $1-2k | 293-326 | 47.3 | -1.5 | -5.4 |  |
| pin_move+pin_rlm | close | pin $1-2k | 63-64 | 49.6 | 4.7 | 10.7 |  |
| pin_move+pin_value | close | pin $1-2k | 78-93 | 45.6 | -4.0 | -12.1 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 62-58 | 51.7 | 5.1 | 6.5 |  |
| pin_move+sharp_gap | close | pin $1-2k | 158-174 | 47.6 | -1.2 | -4.1 |  |
| pin_rlm+pin_value | close | pin $1-2k | 16-25 | 39.0 | -9.1 | -18.9 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 54-55 | 49.5 | 4.1 | 3.8 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 66-71 | 48.2 | 4.5 | 9.9 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 19-21 | 47.5 | -2.0 | -10.3 |  |
| pin_value+sharp_gap | close | pin $1-2k | 72-102 | 41.4 | -6.3 | -17.2 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 77-79 | 49.4 | 3.5 | 2.7 |  |
| follow_move+money_level | close | pin $1-2k | 194-183 | 51.5 | -2.8 | -9.6 |  |
| money_level+rlm_ratio | close | pin $1-2k | 45-34 | 57.0 | 9.2 | 11.1 |  |
| money_level+sharp_gap | close | pin $1-2k | 221-210 | 51.3 | -0.5 | -5.1 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 4-13 | 23.5 | -17.4 | -32.4 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 55-101 | 35.3 | -7.8 | -20.6 |  |
| money_level+money_moving | close | pin $1-2k | 222-214 | 50.9 | -1.0 | -6.0 |  |
| consensus_gap+money_level | close | pin $1-2k | 69-60 | 53.5 | -3.6 | -6.1 |  |
| money_level+pin_value | close | pin $1-2k | 81-83 | 49.4 | -0.5 | -7.6 |  |
| money_level+pin_move | close | pin $1-2k | 153-144 | 51.5 | -1.1 | -5.9 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 26-44 | 37.1 | -6.8 | -10.1 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 41-58 | 41.4 | -3.8 | -7.4 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 17-30 | 36.2 | -7.8 | -13.8 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 22-37 | 37.3 | -5.5 | -9.8 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 27-47 | 36.5 | -6.9 | -14.4 |  |
| money_level+pin_rlm | close | pin $1-2k | 32-24 | 57.1 | 11.2 | 12.3 |  |
| follow_move+money_delta | close | pin $1-2k | 62-68 | 47.7 | 1.5 | -2.3 |  |
| money_delta+money_moving | close | pin $1-2k | 84-97 | 46.4 | 2.4 | 1.9 |  |
| money_delta+pin_move | close | pin $1-2k | 64-69 | 48.1 | 1.0 | 1.5 |  |
| money_delta+pin_rlm | close | pin $1-2k | 41-45 | 47.7 | 4.5 | 8.8 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 47-45 | 51.1 | 5.8 | 6.8 |  |
| money_delta+sharp_gap | close | pin $1-2k | 84-95 | 46.9 | 2.8 | 3.1 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 47.3 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 45-38 | 54.2 | 6.7 | 5.6 |  |
| consensus_gap+money_delta | close | pin $1-2k | 18-26 | 40.9 | -0.5 | 2.5 |  |
| money_delta+pin_value | close | pin $1-2k | 42-44 | 48.8 | 0.7 | -3.4 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 16-35 | 31.4 | -12.2 | -26.6 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 10-25 | 28.6 | -20.5 | -45.2 |  |
| consensus_gap+follow_move | close | pin $2k+ | 34-28 | 54.8 | 1.7 | -8.3 |  |
| consensus_gap+money_delta | close | pin $2k+ | 8-26 | 23.5 | -10.0 | -53.8 |  |
| consensus_gap+money_level | close | pin $2k+ | 69-51 | 57.5 | -5.2 | -10.5 |  |
| consensus_gap+money_moving | close | pin $2k+ | 37-66 | 35.9 | -9.1 | -8.9 |  |
| consensus_gap+pin_move | close | pin $2k+ | 30-33 | 47.6 | -3.0 | -11.4 |  |
| consensus_gap+pin_value | close | pin $2k+ | 43-50 | 46.2 | 3.4 | 9.3 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-13 | 0.0 | -31.2 | -100.0 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 39-69 | 36.1 | -9.4 | -8.4 |  |
| follow_move+money_delta | close | pin $2k+ | 32-43 | 42.7 | 0.6 | -11.6 |  |
| follow_move+money_level | close | pin $2k+ | 148-97 | 60.4 | 0.9 | -3.4 |  |
| follow_move+money_moving | close | pin $2k+ | 116-117 | 49.8 | 1.9 | -5.0 |  |
| follow_move+pin_move | close | pin $2k+ | 147-142 | 50.9 | 0.7 | -4.4 |  |
| follow_move+pin_value | close | pin $2k+ | 37-32 | 53.6 | 6.2 | 15.5 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 39-60 | 39.4 | 1.4 | -12.7 |  |
| follow_move+sharp_gap | close | pin $2k+ | 117-118 | 49.8 | 2.0 | -4.7 |  |
| money_delta+money_level | close | pin $2k+ | 25-21 | 54.3 | 9.9 | 9.9 |  |
| money_delta+money_moving | close | pin $2k+ | 61-88 | 40.9 | 2.4 | -9.2 |  |
| money_delta+pin_move | close | pin $2k+ | 32-49 | 39.5 | -3.0 | -18.8 |  |
| money_delta+pin_value | close | pin $2k+ | 19-22 | 46.3 | 3.0 | -11.4 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 19-29 | 39.6 | 1.0 | -14.0 |  |
| money_delta+sharp_gap | close | pin $2k+ | 59-87 | 40.4 | 1.8 | -10.2 |  |
| money_level+money_moving | close | pin $2k+ | 162-150 | 51.9 | -0.9 | -6.0 |  |
| money_level+pin_move | close | pin $2k+ | 108-97 | 52.7 | -2.9 | -7.4 |  |
| money_level+pin_value | close | pin $2k+ | 57-55 | 50.9 | 1.1 | -5.9 |  |
| money_level+rlm_ratio | close | pin $2k+ | 14-14 | 50.0 | 4.1 | 5.0 |  |
| money_level+sharp_gap | close | pin $2k+ | 162-151 | 51.8 | -1.1 | -5.9 |  |
| money_moving+pin_move | close | pin $2k+ | 101-116 | 46.5 | -0.7 | -7.5 |  |
| money_moving+pin_value | close | pin $2k+ | 59-69 | 46.1 | 0.8 | 4.2 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 39-59 | 39.8 | 1.7 | -11.8 |  |
| money_moving+sharp_gap | close | pin $2k+ | 238-278 | 46.1 | -0.2 | -4.4 |  |
| pin_move+pin_value | close | pin $2k+ | 50-49 | 50.5 | 2.5 | -1.1 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 27-40 | 40.3 | 0.7 | -8.0 |  |
| pin_move+sharp_gap | close | pin $2k+ | 101-117 | 46.3 | -0.9 | -7.5 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 4-7 | 36.4 | -5.8 | -26.4 |  |
| pin_value+sharp_gap | close | pin $2k+ | 59-70 | 45.7 | 0.6 | 3.4 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 39-60 | 39.4 | 1.4 | -12.7 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-21 | 16.0 | -15.0 | -30.8 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 5-13 | 27.8 | -2.0 | -42.0 |  |
| follow_move+pin_rlm | close | pin $2k+ | 28-46 | 37.8 | 0.7 | -13.5 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 60-74 | 44.8 | 6.9 | 3.7 |  |
| money_moving+pin_rlm | close | pin $2k+ | 39-72 | 35.1 | -0.4 | -7.8 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 28-41 | 40.6 | 5.0 | -9.1 |  |
| pin_move+pin_rlm | close | pin $2k+ | 31-48 | 39.2 | 1.5 | -8.1 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 38-50 | 43.2 | 3.3 | -5.7 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 13-31 | 29.5 | -2.7 | -27.2 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 28-46 | 37.8 | 0.7 | -13.5 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 39-72 | 35.1 | -0.4 | -7.8 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 20-37 | 35.1 | 2.5 | -17.7 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 28-42 | 40.0 | 4.6 | -10.4 |  |
| money_delta+pin_rlm | close | pin $2k+ | 21-40 | 34.4 | -1.0 | -14.3 |  |
| money_level+pin_rlm | close | pin $2k+ | 15-10 | 60.0 | 16.2 | 27.1 |  |
| pin_rlm+pin_value | close | pin $2k+ | 6-13 | 31.6 | -4.7 | 13.6 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 17-23 | 42.5 | 3.9 | -12.0 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 6-7 | 46.2 | 8.6 | 66.2 |  |
| follow_move+money_delta | close | pin limit <$1k | 35-43 | 44.9 | -4.3 | -13.8 |  |
| money_level+money_moving | close | pin limit <$1k | 76-86 | 46.9 | -2.8 | -10.1 |  |
| money_level+sharp_gap | close | pin limit <$1k | 73-80 | 47.7 | -2.0 | -8.5 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 114-131 | 46.5 | -2.8 | -7.1 |  |
| consensus_gap+money_level | close | pin limit <$1k | 32-26 | 55.2 | 4.3 | 2.2 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 16-11 | 59.3 | 10.9 | 27.9 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 41-33 | 55.4 | 5.7 | 10.2 |  |
| follow_move+money_moving | close | pin limit <$1k | 71-87 | 44.9 | -4.4 | -13.6 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 76-86 | 46.9 | -2.4 | -9.9 |  |
| money_level+pin_move | close | pin limit <$1k | 57-55 | 50.9 | 1.0 | -2.8 |  |
| money_level+pin_value | close | pin limit <$1k | 56-36 | 60.9 | 10.7 | 15.2 |  |
| pin_move+pin_value | close | pin limit <$1k | 45-28 | 61.6 | 11.8 | 23.2 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 21-11 | 65.6 | 16.0 | 21.3 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 25-19 | 56.8 | 7.9 | 17.6 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 27-19 | 58.7 | 9.7 | 20.6 |  |
| follow_move+money_level | close | pin limit <$1k | 60-64 | 48.4 | -1.8 | -7.8 |  |
| follow_move+pin_move | close | pin limit <$1k | 66-71 | 48.2 | -1.3 | -7.7 |  |
| follow_move+pin_value | close | pin limit <$1k | 41-25 | 62.1 | 12.3 | 17.9 |  |
| money_moving+pin_move | close | pin limit <$1k | 65-71 | 47.8 | -1.5 | -5.3 |  |
| money_moving+pin_value | close | pin limit <$1k | 43-30 | 58.9 | 9.2 | 17.8 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 67-72 | 48.2 | -1.1 | -4.6 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 44-32 | 57.9 | 8.2 | 15.7 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 40-44 | 47.6 | -1.6 | -8.7 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 27-31 | 46.6 | -2.4 | -10.7 |  |
| money_delta+money_moving | close | pin limit <$1k | 49-52 | 48.5 | -0.6 | -2.6 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 9-6 | 60.0 | 13.2 | 43.2 |  |
| money_delta+money_level | close | pin limit <$1k | 26-22 | 54.2 | 4.5 | 3.8 |  |
| money_delta+pin_value | close | pin limit <$1k | 17-8 | 68.0 | 18.9 | 46.9 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 48-50 | 49.0 | -0.0 | -1.7 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 31-36 | 46.3 | -2.5 | -4.6 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 7-3 | 70.0 | 24.4 | 77.3 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 26-22 | 54.2 | 5.9 | 13.3 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 41-35 | 53.9 | 5.5 | 15.2 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 43-37 | 53.8 | 4.9 | 8.6 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-5 | 79.2 | 30.3 | 69.5 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 44-37 | 54.3 | 5.8 | 15.2 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 6-1 | 85.7 | 39.1 | 63.9 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 13-7 | 65.0 | 15.2 | 24.4 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 11-19 | 36.7 | -11.6 | -29.6 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 22-26 | 45.8 | -3.1 | -11.9 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 35-29 | 54.7 | 5.7 | 5.3 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 49-42 | 53.8 | 4.9 | 4.0 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 29-26 | 52.7 | 3.9 | 1.4 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 21-30 | 41.2 | -7.6 | -20.8 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 45-40 | 52.9 | 4.1 | 2.3 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 35-29 | 54.7 | 5.7 | 5.3 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 15-14 | 51.7 | 3.6 | -0.5 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 35-29 | 54.7 | 5.7 | 5.3 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 23-23 | 50.0 | 1.3 | -4.0 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 49-42 | 53.8 | 4.9 | 4.0 |  |
| money_level+pin_rlm | close | pin limit <$1k | 21-15 | 58.3 | 8.7 | 12.0 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 23-17 | 57.5 | 8.4 | 11.8 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 18-5 | 78.3 | 28.5 | 49.8 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 7-3 | 70.0 | 22.2 | 33.8 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 50.5 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -3.9 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -51.6 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 33-36 | 47.8 | 12.2 | 16.1 | 0.28 |
| rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -14.9 | -3.3 | -0.95 |
| rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -27.3 | -100.0 | 1.3 |
| rlm_quiet | early | pin limit <$1k | 5-8 | 38.5 | -6.1 | -21.5 | 0.25 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.5 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 6-9 | 40.0 | -8.3 | -27.9 | 0.27 |
| pin_move | early | pin $1-2k | 0-3 | 0.0 | -35.8 | -100.0 | 0.23 |
| pin_move | early | pin limit <$1k | 6-7 | 46.2 | -5.2 | -16.9 | 0.18 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 8-7 | 53.3 | 12.7 | 18.2 | -0.18 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -40.0 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 4-0 | 100.0 | 50.8 | 88.0 | -0.25 |
| pin_rlm | early | <1k bets | 1-2 | 33.3 | 6.0 | -35.8 | -1.0 |
| pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -27.3 | -100.0 | -1.75 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.7 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.5 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -51.6 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 442-380 | 53.8 | 1.9 | -5.7 | 0.16 |
| follow_move | early | pin $1-2k | 30-18 | 62.5 | 9.7 | 12.9 | -0.46 |
| follow_move | early | pin $2k+ | 0-2 | 0.0 | -40.0 | -100.0 | 0.65 |
| follow_move | early | pin limit <$1k | 50-42 | 54.3 | 4.0 | 0.6 | -0.19 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.4 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.7 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 27-19 | 58.7 | 20.7 | 29.1 | 0.63 |
| rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 2.6 | 55.6 | -1.52 |
| rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.0 | -100.0 | 0.65 |
| rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 1.3 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 43.5 | 59.7 | 0.33 |
| money_level | early | <1k bets | 154-104 | 59.7 | -0.0 | -6.5 | -0.14 |
| money_level | early | pin $1-2k | 21-8 | 72.4 | 7.8 | 7.1 | 0.01 |
| money_level | early | pin $2k+ | 1-1 | 50.0 | -12.7 | -47.2 | -0.7 |
| money_level | early | pin limit <$1k | 25-26 | 49.0 | -4.0 | -9.4 | 0.22 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.4 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.4 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 127-112 | 53.1 | 5.0 | 2.8 | 0.36 |
| sharp_gap | early | pin $1-2k | 16-11 | 59.3 | 6.4 | 9.8 | -0.37 |
| sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.0 | -100.0 | 0.65 |
| sharp_gap | early | pin limit <$1k | 29-19 | 60.4 | 11.8 | 25.2 | 0.12 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.6 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 51.6 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 90-80 | 52.9 | 1.6 | -6.2 | 0.08 |
| money_moving | early | pin $1-2k | 8-9 | 47.1 | -10.6 | -35.5 | 0.2 |
| money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.7 | -8.4 | 0.65 |
| money_moving | early | pin limit <$1k | 23-10 | 69.7 | 20.6 | 47.4 | 0.41 |
| pin_value | early | 1-3k bets | 13-10 | 56.5 | 8.3 | 6.3 | -0.04 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.7 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 40-41 | 49.4 | 1.0 | -6.5 | 0.05 |
| pin_value | early | pin $1-2k | 14-20 | 41.2 | -4.7 | -22.6 | 0.14 |
| pin_value | early | pin $2k+ | 1-0 | 100.0 | 52.7 | 83.3 | 0.0 |
| pin_value | early | pin limit <$1k | 39-31 | 55.7 | 6.1 | 5.5 | -0.0 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -50.5 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -26.9 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.1 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.7 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 208-258 | 44.6 | -3.5 | -11.9 | 0.39 |
| consensus_gap | early | pin $1-2k | 12-21 | 36.4 | -8.5 | -30.4 | 0.49 |
| consensus_gap | early | pin $2k+ | 1-1 | 50.0 | 12.7 | -8.4 | 0.65 |
| consensus_gap | early | pin limit <$1k | 19-34 | 35.8 | -14.4 | -25.9 | 0.28 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -52.7 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -1.6 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.5 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 5.4 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.3 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 7-4 | 63.6 | 14.3 | 19.4 | -0.09 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.4 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.8 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.5 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -0.8 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 6-5 | 54.5 | 8.3 | 1.3 | 0.27 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -0.6 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-7 | 50.0 | 2.9 | -6.4 | -0.29 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -3.9 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.4 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -20.6 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.5 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 3.1 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.6 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.4 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.6 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.4 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.2 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.1 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.6 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.1 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 52.7 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 11.9 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 18.5 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 16.9 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 16.9 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -27.3 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.7 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.7 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.7 | 83.3 | 1.0 |
| follow_move+rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -51.6 | -100.0 | -0.5 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.7 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.7 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 51.6 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.7 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.7 | 83.3 | 1.0 |
| rlm_quiet+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.7 | -100.0 | -1.0 |
| rlm_quiet+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.7 | -100.0 | -1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.7 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 38.9 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 50.5 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 29-38 | 43.3 | -9.1 | -22.0 | 0.85 |
| consensus_gap+money_level | early | <1k bets | 33-25 | 56.9 | -7.8 | -11.6 | 0.31 |
| consensus_gap+sharp_gap | early | <1k bets | 25-40 | 38.5 | -8.5 | -16.8 | 0.96 |
| follow_move+money_level | early | <1k bets | 78-40 | 66.1 | 5.1 | -2.6 | 0.02 |
| follow_move+sharp_gap | early | <1k bets | 68-36 | 65.4 | 15.8 | 16.9 | 0.5 |
| money_level+sharp_gap | early | <1k bets | 83-53 | 61.0 | 4.6 | -0.6 | 0.17 |
| follow_move+money_moving | early | <1k bets | 47-30 | 61.0 | 8.0 | 7.8 | 0.38 |
| money_level+money_moving | early | <1k bets | 54-41 | 56.8 | -2.0 | -10.7 | -0.19 |
| money_moving+sharp_gap | early | <1k bets | 53-48 | 52.5 | 3.6 | -3.7 | 0.28 |
| consensus_gap+money_moving | early | <1k bets | 13-20 | 39.4 | -10.5 | -38.2 | 0.24 |
| follow_move+pin_value | early | <1k bets | 15-12 | 55.6 | 5.9 | 4.1 | -0.23 |
| follow_move+rlm_quiet | early | <1k bets | 33-36 | 47.8 | 12.2 | 16.1 | 0.28 |
| money_moving+rlm_quiet | early | <1k bets | 14-10 | 58.3 | 21.0 | 38.8 | 0.59 |
| rlm_quiet+sharp_gap | early | <1k bets | 20-15 | 57.1 | 20.4 | 27.6 | -0.0 |
| follow_move+rlm_ratio | early | <1k bets | 27-19 | 58.7 | 20.7 | 29.1 | 0.63 |
| rlm_quiet+rlm_ratio | early | <1k bets | 18-11 | 62.1 | 25.7 | 40.9 | 0.03 |
| rlm_ratio+sharp_gap | early | <1k bets | 27-19 | 58.7 | 20.7 | 29.1 | 0.63 |
| pin_move+pin_value | early | <1k bets | 2-4 | 33.3 | -16.0 | -36.4 | 0.17 |
| follow_move+pin_move | early | <1k bets | 5-4 | 55.6 | 4.1 | -1.1 | 0.38 |
| consensus_gap+pin_value | early | <1k bets | 14-23 | 37.8 | -8.9 | -29.1 | 0.39 |
| pin_value+rlm_quiet | early | <1k bets | 0-3 | 0.0 | -43.1 | -100.0 | -0.6 |
| money_delta+money_moving | early | <1k bets | 7-7 | 50.0 | 10.0 | 13.0 | -0.19 |
| money_delta+sharp_gap | early | <1k bets | 6-5 | 54.5 | 15.1 | 26.5 | -0.25 |
| consensus_gap+pin_move | early | <1k bets | 1-5 | 16.7 | -28.8 | -68.2 | 0.22 |
| money_level+pin_move | early | <1k bets | 3-2 | 60.0 | 5.3 | 0.8 | 0.08 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -27.3 | -100.0 | -4.8 |
| consensus_gap+rlm_quiet | early | <1k bets | 3-5 | 37.5 | -0.9 | -22.7 | 1.01 |
| consensus_gap+rlm_ratio | early | <1k bets | 4-3 | 57.1 | 17.2 | 15.6 | 0.6 |
| follow_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 22.7 | -3.7 | -2.15 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -27.3 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | <1k bets | 0-1 | 0.0 | -27.3 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 22.7 | -3.7 | -2.15 |
| pin_rlm+sharp_gap | early | <1k bets | 1-2 | 33.3 | 6.0 | -35.8 | -1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 11.6 | -4.5 | -1.9 |
| pin_value+sharp_gap | early | <1k bets | 5-4 | 55.6 | 8.3 | 6.1 | -0.09 |
| money_level+pin_value | early | <1k bets | 5-4 | 55.6 | 5.4 | 6.1 | 0.78 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -51.1 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -49.5 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 1-2 | 33.3 | -17.6 | -36.4 | 1.33 |
| money_level+rlm_ratio | early | <1k bets | 7-8 | 46.7 | 7.3 | -2.1 | 1.93 |
| money_moving+rlm_ratio | early | <1k bets | 13-8 | 61.9 | 19.7 | 39.1 | 0.8 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 49.5 | 90.9 | 0.0 |
| money_delta+money_level | early | <1k bets | 3-2 | 60.0 | 14.7 | 29.2 | 1.36 |
| pin_move+sharp_gap | early | <1k bets | 2-1 | 66.7 | 16.5 | 4.3 | -0.07 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 72.7 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 72.7 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 72.7 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 3-4 | 42.9 | 2.9 | 17.8 | 0.34 |
| money_delta+rlm_quiet | early | <1k bets | 1-2 | 33.3 | -1.4 | 23.3 | -2.8 |
| money_delta+rlm_ratio | early | <1k bets | 2-2 | 50.0 | 11.6 | 58.5 | 1.15 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 50.5 | 90.9 | -1.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -27.3 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 5-4 | 55.6 | -8.7 | -12.6 | 0.71 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -30.9 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 5-10 | 33.3 | -8.0 | -38.7 | 0.31 |
| follow_move+rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -14.9 | -3.3 | -0.95 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 2.6 | 55.6 | -1.52 |
| follow_move+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 14.0 | 37.5 | -0.83 |
| money_level+money_moving | early | pin $1-2k | 8-5 | 61.5 | -3.8 | -15.6 | 0.07 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.4 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-2 | 33.3 | -16.5 | -38.9 | 0.67 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -8.6 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -8.6 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-3 | 40.0 | 2.6 | 55.6 | -1.52 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -52.7 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -40.0 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -52.7 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -40.0 | -100.0 | 2.5 |
| money_level+sharp_gap | early | pin $1-2k | 13-4 | 76.5 | 13.1 | 17.1 | -0.25 |
| money_moving+sharp_gap | early | pin $1-2k | 4-6 | 40.0 | -16.5 | -45.4 | 0.08 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -9.1 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 4-6 | 40.0 | -10.0 | -31.3 | 0.34 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 0-3 | 0.0 | -27.3 | -100.0 | -0.97 |
| follow_move+pin_value | early | pin $1-2k | 6-6 | 50.0 | 2.4 | -7.6 | -0.27 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -27.3 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 11-4 | 73.3 | 8.7 | 6.6 | -0.07 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 47.3 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 4-2 | 66.7 | 2.1 | -10.9 | -0.15 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -27.3 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -27.3 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -16.7 | -46.8 | -0.12 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -27.3 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -27.3 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | pin $1-2k | 0-1 | 0.0 | -27.3 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -27.3 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -27.3 | -100.0 | -1.75 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -27.3 | -100.0 | -4.8 |
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -27.3 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -27.3 | -100.0 | 1.3 |
| consensus_gap+money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.7 | -8.4 | 0.65 |
| consensus_gap+pin_value | early | pin $2k+ | 1-0 | 100.0 | 52.7 | 83.3 | 0.0 |
| follow_move+money_level | early | pin $2k+ | 0-1 | 0.0 | -52.7 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.0 | -100.0 | 0.65 |
| follow_move+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.0 | -100.0 | 0.65 |
| money_level+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -52.7 | -100.0 | 0.0 |
| money_level+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -52.7 | -100.0 | 0.0 |
| money_moving+pin_value | early | pin $2k+ | 1-0 | 100.0 | 52.7 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.0 | -100.0 | 0.65 |
| consensus_gap+follow_move | early | pin $2k+ | 0-1 | 0.0 | -27.3 | -100.0 | 1.3 |
| consensus_gap+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -27.3 | -100.0 | 1.3 |
| consensus_gap+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -27.3 | -100.0 | 1.3 |
| consensus_gap+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -27.3 | -100.0 | 1.3 |
| follow_move+money_moving | early | pin $2k+ | 0-1 | 0.0 | -27.3 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -27.3 | -100.0 | 1.3 |
| money_moving+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -27.3 | -100.0 | 1.3 |
| money_moving+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -27.3 | -100.0 | 1.3 |
| money_moving+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -27.3 | -100.0 | 1.3 |
| rlm_quiet+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -27.3 | -100.0 | 1.3 |
| rlm_quiet+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -27.3 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin limit <$1k | 5-8 | 38.5 | -6.1 | -21.5 | 0.25 |
| money_level+money_moving | early | pin limit <$1k | 13-7 | 65.0 | 12.9 | 20.2 | 0.48 |
| money_level+sharp_gap | early | pin limit <$1k | 20-16 | 55.6 | 5.1 | 1.6 | 0.14 |
| money_moving+sharp_gap | early | pin limit <$1k | 18-6 | 75.0 | 27.0 | 63.1 | 0.34 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -50.5 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 10-6 | 62.5 | 12.6 | 18.6 | 0.31 |
| money_moving+pin_value | early | pin limit <$1k | 7-4 | 63.6 | 14.0 | 20.1 | 0.18 |
| pin_value+sharp_gap | early | pin limit <$1k | 12-6 | 66.7 | 16.9 | 26.4 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-9 | 40.0 | -11.9 | -25.7 | 0.53 |
| consensus_gap+money_level | early | pin limit <$1k | 4-7 | 36.4 | -19.3 | -38.9 | 0.36 |
| consensus_gap+pin_value | early | pin limit <$1k | 15-18 | 45.5 | -3.6 | -14.6 | 0.42 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.1 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 11-11 | 50.0 | -3.6 | -7.4 | -0.04 |
| follow_move+pin_value | early | pin limit <$1k | 16-13 | 55.2 | 5.9 | 3.9 | -0.24 |
| follow_move+sharp_gap | early | pin limit <$1k | 13-8 | 61.9 | 13.4 | 18.2 | -0.07 |
| follow_move+rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level+rlm_ratio | early | pin limit <$1k | 6-0 | 100.0 | 54.0 | 92.6 | 0.42 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 16.8 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| consensus_gap+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.1 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 22.7 | 72.3 | 0.54 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 1.6 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.1 | 85.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 9-4 | 69.2 | 19.9 | 32.3 | 0.31 |
| money_delta+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 50.9 | 87.1 | -0.33 |
| money_delta+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 50.9 | 87.1 | -0.33 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 3-2 | 60.0 | 10.7 | 13.0 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.0 | 45.3 | -0.5 |
| money_delta+sharp_gap | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 | -0.5 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 11.1 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | 5.8 | 13.7 | -0.05 |
| pin_move+pin_value | early | pin limit <$1k | 2-4 | 33.3 | -16.0 | -36.4 | 0.17 |
| follow_move+pin_move | early | pin limit <$1k | 5-4 | 55.6 | 4.1 | -1.1 | 0.38 |
| consensus_gap+pin_move | early | pin limit <$1k | 1-3 | 25.0 | -29.5 | -52.3 | 0.4 |
| money_level+pin_move | early | pin limit <$1k | 3-2 | 60.0 | 5.3 | 0.8 | 0.08 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -49.5 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -49.5 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 16.5 | 4.3 | -0.07 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.7 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.7 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.7 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 72.7 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 72.7 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 72.7 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 50.5 | 90.9 | -1.0 |
| rlm_quiet | close | 1-3k bets | 116-168 | 40.8 | -0.8 | -7.9 |  |
| rlm_quiet | close | 3k+ bets | 44-60 | 42.3 | -0.3 | -8.1 |  |
| rlm_quiet | close | <1k bets | 22-28 | 44.0 | 2.5 | -6.0 |  |
| rlm_quiet | close | pin $1-2k | 46-81 | 36.2 | -6.8 | -17.4 |  |
| rlm_quiet | close | pin $2k+ | 53-63 | 45.7 | 8.0 | -1.7 |  |
| rlm_quiet | close | pin limit <$1k | 36-36 | 50.0 | 0.1 | -4.2 |  |
| pin_move | close | 1-3k bets | 308-306 | 50.2 | 0.2 | -2.3 |  |
| pin_move | close | 3k+ bets | 121-126 | 49.0 | -0.6 | -5.4 |  |
| pin_move | close | <1k bets | 67-68 | 49.6 | -1.0 | -4.6 |  |
| pin_move | close | pin $1-2k | 232-229 | 50.3 | -0.1 | -1.3 |  |
| pin_move | close | pin $2k+ | 176-187 | 48.5 | -1.0 | -7.7 |  |
| pin_move | close | pin limit <$1k | 88-84 | 51.2 | 1.4 | 0.4 |  |
| money_delta | close | 1-3k bets | 199-251 | 44.2 | -0.5 | -6.2 |  |
| money_delta | close | 3k+ bets | 79-109 | 42.0 | -1.1 | -3.3 |  |
| money_delta | close | <1k bets | 38-62 | 38.0 | -4.1 | -22.9 |  |
| money_delta | close | pin $1-2k | 112-115 | 49.3 | 3.5 | 3.3 |  |
| money_delta | close | pin $2k+ | 82-112 | 42.3 | 1.0 | -9.8 |  |
| money_delta | close | pin limit <$1k | 50-54 | 48.1 | -1.7 | -3.7 |  |
| pin_rlm | close | 1-3k bets | 87-94 | 48.1 | 5.5 | 17.0 |  |
| pin_rlm | close | 3k+ bets | 32-46 | 41.0 | -1.0 | -10.3 |  |
| pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| pin_rlm | close | pin $1-2k | 61-66 | 48.0 | 4.1 | 10.9 |  |
| pin_rlm | close | pin $2k+ | 38-66 | 36.5 | 1.3 | -3.8 |  |
| pin_rlm | close | pin limit <$1k | 41-29 | 58.6 | 9.4 | 24.9 |  |
| follow_move | close | 1-3k bets | 546-478 | 53.3 | 1.7 | -4.4 |  |
| follow_move | close | 3k+ bets | 190-177 | 51.8 | -0.2 | -5.2 |  |
| follow_move | close | <1k bets | 120-108 | 52.6 | -0.6 | -11.2 |  |
| follow_move | close | pin $1-2k | 257-283 | 47.6 | -3.5 | -11.2 |  |
| follow_move | close | pin $2k+ | 220-183 | 54.6 | 2.5 | -3.7 |  |
| follow_move | close | pin limit <$1k | 106-104 | 50.5 | 0.4 | -3.7 |  |
| rlm_ratio | close | 1-3k bets | 126-155 | 44.8 | 0.0 | -3.6 |  |
| rlm_ratio | close | 3k+ bets | 48-44 | 52.2 | 7.5 | 11.8 |  |
| rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.9 | 0.8 |  |
| rlm_ratio | close | pin $1-2k | 70-73 | 49.0 | 2.4 | 2.5 |  |
| rlm_ratio | close | pin $2k+ | 38-53 | 41.8 | 3.4 | -7.6 |  |
| rlm_ratio | close | pin limit <$1k | 44-34 | 56.4 | 6.8 | 8.9 |  |
| money_level | close | 1-3k bets | 693-492 | 58.5 | 2.9 | -1.9 |  |
| money_level | close | 3k+ bets | 244-193 | 55.8 | 0.7 | -3.1 |  |
| money_level | close | <1k bets | 145-118 | 55.1 | -0.8 | -11.5 |  |
| money_level | close | pin $1-2k | 318-277 | 53.4 | -0.5 | -4.8 |  |
| money_level | close | pin $2k+ | 279-216 | 56.4 | -1.0 | -7.0 |  |
| money_level | close | pin limit <$1k | 125-120 | 51.0 | 0.9 | -3.0 |  |
| sharp_gap | close | 1-3k bets | 521-619 | 45.7 | -1.7 | -8.4 |  |
| sharp_gap | close | 3k+ bets | 210-218 | 49.1 | 1.7 | 3.4 |  |
| sharp_gap | close | <1k bets | 114-137 | 45.4 | -2.4 | -14.6 |  |
| sharp_gap | close | pin $1-2k | 275-304 | 47.5 | -1.3 | -5.2 |  |
| sharp_gap | close | pin $2k+ | 223-255 | 46.7 | 0.4 | -2.7 |  |
| sharp_gap | close | pin limit <$1k | 115-122 | 48.5 | -1.2 | -3.2 |  |
| money_moving | close | 1-3k bets | 525-617 | 46.0 | -1.9 | -8.7 |  |
| money_moving | close | 3k+ bets | 209-220 | 48.7 | 1.0 | 1.8 |  |
| money_moving | close | <1k bets | 112-137 | 45.0 | -2.5 | -13.5 |  |
| money_moving | close | pin $1-2k | 271-309 | 46.7 | -2.3 | -6.5 |  |
| money_moving | close | pin $2k+ | 224-253 | 47.0 | 0.6 | -2.7 |  |
| money_moving | close | pin limit <$1k | 111-127 | 46.6 | -3.0 | -6.8 |  |
| pin_value | close | 1-3k bets | 220-230 | 48.9 | 1.1 | 0.4 |  |
| pin_value | close | 3k+ bets | 81-86 | 48.5 | 0.0 | -5.0 |  |
| pin_value | close | <1k bets | 54-44 | 55.1 | 8.0 | 10.6 |  |
| pin_value | close | pin $1-2k | 163-184 | 47.0 | -1.3 | -4.8 |  |
| pin_value | close | pin $2k+ | 99-113 | 46.7 | 0.8 | -2.0 |  |
| pin_value | close | pin limit <$1k | 93-63 | 59.6 | 9.9 | 15.9 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.9 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.9 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 209-274 | 43.3 | -4.6 | -12.3 |  |
| consensus_gap | close | 3k+ bets | 81-95 | 46.0 | -1.4 | 5.1 |  |
| consensus_gap | close | <1k bets | 40-78 | 33.9 | -9.7 | -30.7 |  |
| consensus_gap | close | pin $1-2k | 108-119 | 47.6 | -1.5 | -1.2 |  |
| consensus_gap | close | pin $2k+ | 83-105 | 44.1 | -4.8 | -6.5 |  |
| consensus_gap | close | pin limit <$1k | 50-43 | 53.8 | 3.5 | 5.0 |  |
| consensus_gap+follow_move | close | 1-3k bets | 88-80 | 52.4 | 0.5 | -1.3 |  |
| consensus_gap+money_level | close | 1-3k bets | 140-94 | 59.8 | 1.0 | 2.5 |  |
| consensus_gap+money_moving | close | 1-3k bets | 97-149 | 39.4 | -5.7 | -9.9 |  |
| consensus_gap+pin_move | close | 1-3k bets | 53-53 | 50.0 | -1.3 | 2.5 |  |
| consensus_gap+pin_value | close | 1-3k bets | 86-100 | 46.2 | 0.6 | -1.5 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 95-152 | 38.5 | -5.8 | -11.0 |  |
| follow_move+money_level | close | 1-3k bets | 370-252 | 59.5 | 3.2 | -2.8 |  |
| follow_move+money_moving | close | 1-3k bets | 302-317 | 48.8 | -0.6 | -6.7 |  |
| follow_move+pin_move | close | 1-3k bets | 223-224 | 49.9 | -0.3 | -5.2 |  |
| follow_move+pin_value | close | 1-3k bets | 74-76 | 49.3 | 0.8 | -6.5 |  |
| follow_move+sharp_gap | close | 1-3k bets | 303-315 | 49.0 | -0.1 | -5.3 |  |
| money_level+money_moving | close | 1-3k bets | 378-332 | 53.2 | 0.8 | -3.3 |  |
| money_level+pin_move | close | 1-3k bets | 193-173 | 52.7 | -0.1 | -3.8 |  |
| money_level+pin_value | close | 1-3k bets | 111-99 | 52.9 | 3.3 | -0.8 |  |
| money_level+sharp_gap | close | 1-3k bets | 367-326 | 53.0 | 0.8 | -2.9 |  |
| money_moving+pin_move | close | 1-3k bets | 192-207 | 48.1 | -0.9 | -3.0 |  |
| money_moving+pin_value | close | 1-3k bets | 100-121 | 45.2 | -2.1 | -5.9 |  |
| money_moving+sharp_gap | close | 1-3k bets | 499-591 | 45.8 | -1.8 | -7.9 |  |
| pin_move+pin_value | close | 1-3k bets | 99-97 | 50.5 | 1.4 | -0.5 |  |
| pin_move+sharp_gap | close | 1-3k bets | 199-207 | 49.0 | 0.1 | -0.9 |  |
| pin_value+sharp_gap | close | 1-3k bets | 102-124 | 45.1 | -2.0 | -6.3 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 116-168 | 40.8 | -0.8 | -7.9 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 62-104 | 37.3 | -4.4 | -11.0 |  |
| consensus_gap+money_delta | close | 1-3k bets | 25-64 | 28.1 | -9.4 | -23.3 |  |
| follow_move+money_delta | close | 1-3k bets | 95-109 | 46.6 | -0.4 | -7.4 |  |
| money_delta+money_level | close | 1-3k bets | 74-72 | 50.7 | 2.7 | 5.0 |  |
| money_delta+money_moving | close | 1-3k bets | 139-201 | 40.9 | -2.2 | -9.8 |  |
| money_delta+pin_value | close | 1-3k bets | 44-45 | 49.4 | 2.0 | -0.9 |  |
| money_delta+sharp_gap | close | 1-3k bets | 138-199 | 40.9 | -2.2 | -9.6 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 70-80 | 46.7 | -0.9 | 0.1 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 17-27 | 38.6 | 0.9 | 16.5 |  |
| money_level+pin_rlm | close | 1-3k bets | 39-29 | 57.4 | 8.9 | 10.4 |  |
| pin_move+pin_rlm | close | 1-3k bets | 79-78 | 50.3 | 5.6 | 12.3 |  |
| pin_rlm+pin_value | close | 1-3k bets | 29-24 | 54.7 | 8.6 | 30.7 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 87-94 | 48.1 | 5.5 | 17.0 |  |
| money_delta+pin_rlm | close | 1-3k bets | 49-54 | 47.6 | 4.0 | 14.2 |  |
| money_moving+pin_rlm | close | 1-3k bets | 82-91 | 47.4 | 4.8 | 16.6 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 19-30 | 38.8 | -1.7 | 4.1 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 126-155 | 44.8 | 0.0 | -3.6 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 66-77 | 46.2 | 0.2 | -6.8 |  |
| money_level+rlm_ratio | close | 1-3k bets | 59-56 | 51.3 | 1.7 | -1.0 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 120-150 | 44.4 | -0.5 | -4.1 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 67-68 | 49.6 | 3.6 | 2.4 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 25-22 | 53.2 | 5.2 | 2.3 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 126-155 | 44.8 | 0.0 | -3.6 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 12-30 | 28.6 | -7.1 | -7.2 |  |
| follow_move+pin_rlm | close | 1-3k bets | 62-72 | 46.3 | 1.7 | -4.0 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 55-103 | 34.8 | -6.8 | -15.6 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 52-68 | 43.3 | -0.6 | -7.1 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 24-42 | 36.4 | -3.6 | -15.9 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 62-72 | 46.3 | 1.7 | -4.0 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 50-88 | 36.2 | -3.9 | -9.9 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 31-53 | 36.9 | -6.6 | -21.6 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 14-20 | 41.2 | -4.1 | -19.8 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 49.7 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 30-27 | 52.6 | 2.9 | 3.3 |  |
| consensus_gap+money_moving | close | 3k+ bets | 33-52 | 38.8 | -5.2 | 14.5 |  |
| consensus_gap+pin_move | close | 3k+ bets | 22-19 | 53.7 | 3.4 | 8.4 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-6 | 33.3 | -6.5 | 6.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 35-33 | 51.5 | 5.0 | 5.6 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -0.8 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 34-52 | 39.5 | -4.3 | 17.6 |  |
| follow_move+money_moving | close | 3k+ bets | 101-106 | 48.8 | -0.4 | -4.1 |  |
| follow_move+pin_move | close | 3k+ bets | 92-90 | 50.5 | 0.5 | -1.8 |  |
| follow_move+pin_rlm | close | 3k+ bets | 30-31 | 49.2 | 4.9 | 8.5 |  |
| follow_move+pin_value | close | 3k+ bets | 33-33 | 50.0 | 0.1 | -6.1 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 48-44 | 52.2 | 7.5 | 11.8 |  |
| follow_move+sharp_gap | close | 3k+ bets | 103-105 | 49.5 | 0.8 | -2.0 |  |
| money_moving+pin_move | close | 3k+ bets | 71-83 | 46.1 | -1.9 | -8.2 |  |
| money_moving+pin_rlm | close | 3k+ bets | 31-45 | 40.8 | -1.0 | -10.5 |  |
| money_moving+pin_value | close | 3k+ bets | 40-49 | 44.9 | -2.5 | -7.8 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 46-42 | 52.3 | 7.6 | 12.4 |  |
| money_moving+sharp_gap | close | 3k+ bets | 202-210 | 49.0 | 1.6 | 3.2 |  |
| pin_move+pin_rlm | close | 3k+ bets | 31-40 | 43.7 | 0.1 | -4.2 |  |
| pin_move+pin_value | close | 3k+ bets | 33-40 | 45.2 | -4.2 | -14.9 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 33-32 | 50.8 | 5.4 | 10.3 |  |
| pin_move+sharp_gap | close | 3k+ bets | 71-83 | 46.1 | -1.6 | -7.6 |  |
| pin_rlm+pin_value | close | 3k+ bets | 6-15 | 28.6 | -17.5 | -45.5 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 30-31 | 49.2 | 4.9 | 8.5 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 32-46 | 41.0 | -1.0 | -10.3 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 9-10 | 47.4 | -2.9 | -10.1 |  |
| pin_value+sharp_gap | close | 3k+ bets | 40-48 | 45.5 | -2.0 | -6.7 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 48-44 | 52.2 | 7.5 | 11.8 |  |
| follow_move+money_delta | close | 3k+ bets | 38-47 | 44.7 | -0.5 | -7.2 |  |
| money_level+money_moving | close | 3k+ bets | 142-121 | 54.0 | 1.9 | 0.0 |  |
| money_level+sharp_gap | close | 3k+ bets | 141-118 | 54.4 | 2.5 | 1.5 |  |
| follow_move+money_level | close | 3k+ bets | 119-90 | 56.9 | 0.6 | -3.4 |  |
| money_level+rlm_ratio | close | 3k+ bets | 23-12 | 65.7 | 18.8 | 35.2 |  |
| consensus_gap+money_level | close | 3k+ bets | 44-44 | 50.0 | -6.5 | -13.3 |  |
| money_level+pin_move | close | 3k+ bets | 66-61 | 52.0 | -1.4 | -4.5 |  |
| money_level+pin_value | close | 3k+ bets | 45-43 | 51.1 | 0.9 | -5.2 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 7-12 | 36.8 | -0.8 | -5.4 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 44-60 | 42.3 | -0.3 | -8.1 |  |
| money_delta+money_moving | close | 3k+ bets | 60-83 | 42.0 | -0.2 | 1.4 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 19-24 | 44.2 | 2.7 | 2.2 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 23-32 | 41.8 | -0.3 | -6.0 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 21-31 | 40.4 | -1.7 | -8.0 |  |
| consensus_gap+money_delta | close | 3k+ bets | 12-23 | 34.3 | -4.0 | 18.4 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 10-24 | 29.4 | -13.2 | -34.9 |  |
| money_delta+sharp_gap | close | 3k+ bets | 58-80 | 42.0 | 0.0 | 2.1 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 26-30 | 46.4 | 2.4 | 0.6 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 11-17 | 39.3 | -2.7 | -6.7 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 7-12 | 36.8 | -13.1 | -29.6 |  |
| money_delta+money_level | close | 3k+ bets | 31-22 | 58.5 | 12.6 | 18.5 |  |
| money_level+pin_rlm | close | 3k+ bets | 15-9 | 62.5 | 17.8 | 34.6 |  |
| money_delta+pin_value | close | 3k+ bets | 18-19 | 48.6 | 2.7 | -8.3 |  |
| money_delta+pin_move | close | 3k+ bets | 35-42 | 45.5 | 0.2 | -7.0 |  |
| money_delta+pin_rlm | close | 3k+ bets | 21-27 | 43.8 | 2.1 | -6.6 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 28-24 | 53.8 | 9.4 | 14.8 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 47.9 | 87.7 |  |
| money_level+money_moving | close | <1k bets | 76-77 | 49.7 | -2.8 | -14.4 |  |
| money_level+sharp_gap | close | <1k bets | 79-77 | 50.6 | -2.2 | -13.9 |  |
| money_moving+sharp_gap | close | <1k bets | 110-135 | 44.9 | -2.7 | -14.7 |  |
| consensus_gap+money_level | close | <1k bets | 18-27 | 40.0 | -15.9 | -39.4 |  |
| consensus_gap+money_moving | close | <1k bets | 17-40 | 29.8 | -11.7 | -34.9 |  |
| consensus_gap+pin_move | close | <1k bets | 6-13 | 31.6 | -18.2 | -26.5 |  |
| consensus_gap+pin_value | close | <1k bets | 14-14 | 50.0 | 8.1 | 15.4 |  |
| consensus_gap+sharp_gap | close | <1k bets | 17-41 | 29.3 | -12.0 | -36.0 |  |
| money_level+pin_move | close | <1k bets | 34-35 | 49.3 | -5.1 | -13.5 |  |
| money_level+pin_value | close | <1k bets | 18-17 | 51.4 | 1.2 | -4.2 |  |
| money_moving+pin_move | close | <1k bets | 36-41 | 46.8 | -1.1 | -4.2 |  |
| money_moving+pin_value | close | <1k bets | 17-16 | 51.5 | 6.2 | 14.9 |  |
| pin_move+pin_value | close | <1k bets | 25-20 | 55.6 | 7.3 | 12.9 |  |
| pin_move+sharp_gap | close | <1k bets | 36-42 | 46.2 | -2.3 | -9.5 |  |
| pin_value+sharp_gap | close | <1k bets | 17-15 | 53.1 | 7.2 | 18.5 |  |
| follow_move+money_delta | close | <1k bets | 18-20 | 47.4 | 4.9 | -3.2 |  |
| follow_move+money_moving | close | <1k bets | 54-63 | 46.2 | -3.5 | -13.8 |  |
| follow_move+pin_move | close | <1k bets | 42-42 | 50.0 | -1.3 | -7.2 |  |
| follow_move+sharp_gap | close | <1k bets | 56-63 | 47.1 | -3.4 | -16.1 |  |
| money_delta+money_moving | close | <1k bets | 27-46 | 37.0 | -3.0 | -23.1 |  |
| money_delta+pin_move | close | <1k bets | 13-17 | 43.3 | -0.6 | -15.5 |  |
| money_delta+sharp_gap | close | <1k bets | 27-46 | 37.0 | -3.0 | -23.1 |  |
| follow_move+rlm_quiet | close | <1k bets | 22-28 | 44.0 | 2.5 | -6.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.9 | 0.8 |  |
| money_delta+rlm_quiet | close | <1k bets | 8-10 | 44.4 | 4.9 | -4.3 |  |
| money_delta+rlm_ratio | close | <1k bets | 16-15 | 51.6 | 10.0 | 6.3 |  |
| money_moving+rlm_quiet | close | <1k bets | 14-12 | 53.8 | 12.9 | 20.2 |  |
| money_moving+rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.9 | 0.8 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 10-10 | 50.0 | 10.4 | 5.6 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 13-13 | 50.0 | 8.1 | 3.3 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 26-26 | 50.0 | 6.9 | 0.8 |  |
| follow_move+money_level | close | <1k bets | 75-59 | 56.0 | -2.3 | -15.1 |  |
| consensus_gap+money_delta | close | <1k bets | 4-22 | 15.4 | -16.5 | -63.0 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -1.3 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 12-14 | 46.2 | 7.9 | -0.2 |  |
| money_moving+pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| pin_rlm+sharp_gap | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| money_delta+pin_value | close | <1k bets | 6-8 | 42.9 | -3.1 | -19.4 |  |
| consensus_gap+follow_move | close | <1k bets | 9-20 | 31.0 | -19.1 | -51.4 |  |
| follow_move+pin_rlm | close | <1k bets | 16-11 | 59.3 | 16.2 | 17.3 |  |
| follow_move+pin_value | close | <1k bets | 18-12 | 60.0 | 11.2 | 13.8 |  |
| pin_move+pin_rlm | close | <1k bets | 19-16 | 54.3 | 10.9 | 15.0 |  |
| pin_move+rlm_quiet | close | <1k bets | 10-10 | 50.0 | 4.8 | 9.6 |  |
| pin_move+rlm_ratio | close | <1k bets | 16-13 | 55.2 | 10.1 | 7.8 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 21.4 | 60.8 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 7-5 | 58.3 | 16.0 | 15.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 16-11 | 59.3 | 16.2 | 17.3 |  |
| pin_value+rlm_quiet | close | <1k bets | 3-4 | 42.9 | -6.6 | -17.6 |  |
| pin_value+rlm_ratio | close | <1k bets | 4-1 | 80.0 | 30.7 | 51.7 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 2-7 | 22.2 | -12.0 | -57.2 |  |
| money_delta+money_level | close | <1k bets | 12-17 | 41.4 | -2.1 | -18.9 |  |
| money_level+rlm_ratio | close | <1k bets | 13-13 | 50.0 | 4.7 | -1.9 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 17.6 | 19.0 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 0-5 | 0.0 | -35.6 | -100.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 41-46 | 47.1 | -5.1 | -9.7 |  |
| consensus_gap+money_moving | close | pin $1-2k | 53-64 | 45.3 | -3.1 | -3.4 |  |
| consensus_gap+pin_move | close | pin $1-2k | 42-43 | 49.4 | -3.2 | 4.6 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-18 | 41.9 | 1.0 | 25.8 |  |
| consensus_gap+pin_value | close | pin $1-2k | 65-70 | 48.1 | 2.2 | -3.5 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-14 | 50.0 | 4.5 | 9.0 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 51-62 | 45.1 | -2.1 | -2.4 |  |
| follow_move+money_moving | close | pin $1-2k | 152-187 | 44.8 | -5.0 | -12.0 |  |
| follow_move+pin_move | close | pin $1-2k | 164-172 | 48.8 | -1.9 | -6.3 |  |
| follow_move+pin_rlm | close | pin $1-2k | 49-50 | 49.5 | 3.4 | 4.4 |  |
| follow_move+pin_value | close | pin $1-2k | 56-67 | 45.5 | -3.9 | -14.1 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 70-73 | 49.0 | 2.4 | 2.5 |  |
| follow_move+sharp_gap | close | pin $1-2k | 155-184 | 45.7 | -4.0 | -10.7 |  |
| money_moving+pin_move | close | pin $1-2k | 144-163 | 46.9 | -2.4 | -4.5 |  |
| money_moving+pin_rlm | close | pin $1-2k | 58-64 | 47.5 | 3.3 | 10.3 |  |
| money_moving+pin_value | close | pin $1-2k | 65-97 | 40.1 | -7.7 | -21.3 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 68-70 | 49.3 | 2.3 | 3.1 |  |
| money_moving+sharp_gap | close | pin $1-2k | 263-296 | 47.0 | -1.7 | -5.7 |  |
| pin_move+pin_rlm | close | pin $1-2k | 58-60 | 49.2 | 3.9 | 10.9 |  |
| pin_move+pin_value | close | pin $1-2k | 70-87 | 44.6 | -5.0 | -13.8 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 57-54 | 51.4 | 4.2 | 6.4 |  |
| pin_move+sharp_gap | close | pin $1-2k | 147-162 | 47.6 | -1.5 | -3.6 |  |
| pin_rlm+pin_value | close | pin $1-2k | 15-25 | 37.5 | -10.9 | -21.7 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 49-50 | 49.5 | 3.4 | 4.4 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 61-66 | 48.0 | 4.1 | 10.9 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 18-21 | 46.2 | -3.6 | -12.9 |  |
| pin_value+sharp_gap | close | pin $1-2k | 65-94 | 40.9 | -6.8 | -19.9 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 70-73 | 49.0 | 2.4 | 2.5 |  |
| follow_move+money_level | close | pin $1-2k | 178-169 | 51.3 | -3.1 | -10.0 |  |
| money_level+rlm_ratio | close | pin $1-2k | 40-33 | 54.8 | 6.2 | 6.9 |  |
| money_level+sharp_gap | close | pin $1-2k | 197-192 | 50.6 | -1.1 | -5.9 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 3-11 | 21.4 | -20.4 | -31.6 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 46-81 | 36.2 | -6.8 | -17.4 |  |
| money_level+money_moving | close | pin $1-2k | 196-196 | 50.0 | -1.9 | -7.2 |  |
| consensus_gap+money_level | close | pin $1-2k | 63-56 | 52.9 | -3.9 | -6.3 |  |
| money_level+pin_value | close | pin $1-2k | 74-77 | 49.0 | -0.9 | -8.3 |  |
| money_level+pin_move | close | pin $1-2k | 142-133 | 51.6 | -1.3 | -5.7 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 23-39 | 37.1 | -7.0 | -7.9 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 33-46 | 41.8 | -3.5 | -4.5 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 15-26 | 36.6 | -7.9 | -10.6 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 20-32 | 38.5 | -4.9 | -5.1 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 24-40 | 37.5 | -6.5 | -10.1 |  |
| money_level+pin_rlm | close | pin $1-2k | 29-23 | 55.8 | 9.1 | 9.7 |  |
| follow_move+money_delta | close | pin $1-2k | 54-57 | 48.6 | 2.4 | 0.4 |  |
| money_delta+money_moving | close | pin $1-2k | 77-92 | 45.6 | 1.1 | -1.0 |  |
| money_delta+pin_move | close | pin $1-2k | 58-63 | 47.9 | 0.6 | 1.8 |  |
| money_delta+pin_rlm | close | pin $1-2k | 37-42 | 46.8 | 3.2 | 8.6 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 42-41 | 50.6 | 4.5 | 6.6 |  |
| money_delta+sharp_gap | close | pin $1-2k | 77-90 | 46.1 | 1.6 | 0.2 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 47.9 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 42-37 | 53.2 | 5.2 | 3.5 |  |
| consensus_gap+money_delta | close | pin $1-2k | 16-25 | 39.0 | -2.0 | -7.9 |  |
| money_delta+pin_value | close | pin $1-2k | 37-42 | 46.8 | -1.6 | -11.5 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 12-25 | 32.4 | -10.2 | -19.9 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 8-22 | 26.7 | -22.5 | -48.8 |  |
| consensus_gap+follow_move | close | pin $2k+ | 27-28 | 49.1 | -2.0 | -17.0 |  |
| consensus_gap+money_delta | close | pin $2k+ | 7-26 | 21.2 | -11.2 | -58.2 |  |
| consensus_gap+money_level | close | pin $2k+ | 54-46 | 54.0 | -8.6 | -15.6 |  |
| consensus_gap+money_moving | close | pin $2k+ | 31-61 | 33.7 | -9.2 | -8.7 |  |
| consensus_gap+pin_move | close | pin $2k+ | 24-32 | 42.9 | -6.3 | -18.5 |  |
| consensus_gap+pin_value | close | pin $2k+ | 34-46 | 42.5 | 1.0 | 6.1 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-13 | 0.0 | -30.6 | -100.0 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 33-64 | 34.0 | -9.5 | -8.1 |  |
| follow_move+money_delta | close | pin $2k+ | 31-38 | 44.9 | 2.5 | -6.6 |  |
| follow_move+money_level | close | pin $2k+ | 139-88 | 61.2 | 1.8 | -2.0 |  |
| follow_move+money_moving | close | pin $2k+ | 107-104 | 50.7 | 2.8 | -3.0 |  |
| follow_move+pin_move | close | pin $2k+ | 133-124 | 51.8 | 1.8 | -2.5 |  |
| follow_move+pin_value | close | pin $2k+ | 33-31 | 51.6 | 4.3 | -2.4 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 38-53 | 41.8 | 3.4 | -7.6 |  |
| follow_move+sharp_gap | close | pin $2k+ | 108-105 | 50.7 | 2.9 | -2.7 |  |
| money_delta+money_level | close | pin $2k+ | 24-21 | 53.3 | 9.1 | 8.1 |  |
| money_delta+money_moving | close | pin $2k+ | 56-80 | 41.2 | 2.4 | -8.2 |  |
| money_delta+pin_move | close | pin $2k+ | 31-46 | 40.3 | -2.4 | -17.0 |  |
| money_delta+pin_value | close | pin $2k+ | 18-22 | 45.0 | 2.2 | -14.0 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 19-24 | 44.2 | 5.0 | -4.0 |  |
| money_delta+sharp_gap | close | pin $2k+ | 54-79 | 40.6 | 1.8 | -9.3 |  |
| money_level+money_moving | close | pin $2k+ | 150-133 | 53.0 | 0.2 | -3.8 |  |
| money_level+pin_move | close | pin $2k+ | 101-89 | 53.2 | -1.9 | -6.0 |  |
| money_level+pin_value | close | pin $2k+ | 54-50 | 51.9 | 2.1 | -4.0 |  |
| money_level+rlm_ratio | close | pin $2k+ | 14-13 | 51.9 | 5.3 | 8.9 |  |
| money_level+sharp_gap | close | pin $2k+ | 150-134 | 52.8 | 0.0 | -3.7 |  |
| money_moving+pin_move | close | pin $2k+ | 96-107 | 47.3 | 0.3 | -5.6 |  |
| money_moving+pin_value | close | pin $2k+ | 56-64 | 46.7 | 1.6 | 6.4 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 38-52 | 42.2 | 3.7 | -6.6 |  |
| money_moving+sharp_gap | close | pin $2k+ | 218-249 | 46.7 | 0.5 | -2.5 |  |
| pin_move+pin_value | close | pin $2k+ | 46-45 | 50.5 | 2.9 | -0.7 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 27-37 | 42.2 | 2.4 | -3.7 |  |
| pin_move+sharp_gap | close | pin $2k+ | 96-108 | 47.1 | 0.0 | -5.6 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 4-7 | 36.4 | -5.6 | -26.4 |  |
| pin_value+sharp_gap | close | pin $2k+ | 56-65 | 46.3 | 1.4 | 5.5 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 38-53 | 41.8 | 3.4 | -7.6 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-20 | 16.7 | -12.0 | -27.9 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 4-13 | 23.5 | -4.4 | -49.8 |  |
| follow_move+pin_rlm | close | pin $2k+ | 27-42 | 39.1 | 1.7 | -10.6 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 53-63 | 45.7 | 8.0 | -1.7 |  |
| money_moving+pin_rlm | close | pin $2k+ | 38-66 | 36.5 | 1.3 | -3.8 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 26-36 | 41.9 | 6.7 | -5.7 |  |
| pin_move+pin_rlm | close | pin $2k+ | 31-45 | 40.8 | 3.0 | -4.5 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 35-41 | 46.1 | 6.2 | -0.0 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 13-28 | 31.7 | -0.3 | -21.9 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 27-42 | 39.1 | 1.7 | -10.6 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 38-66 | 36.5 | 1.3 | -3.8 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 20-33 | 37.7 | 5.2 | -11.5 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 26-37 | 41.3 | 6.2 | -7.2 |  |
| money_delta+pin_rlm | close | pin $2k+ | 21-36 | 36.8 | 1.3 | -8.3 |  |
| money_level+pin_rlm | close | pin $2k+ | 15-9 | 62.5 | 20.1 | 32.4 |  |
| pin_rlm+pin_value | close | pin $2k+ | 6-13 | 31.6 | -4.3 | 13.6 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 16-20 | 44.4 | 5.7 | -7.5 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 4-7 | 36.4 | -0.5 | -26.4 |  |
| follow_move+money_delta | close | pin limit <$1k | 31-37 | 45.6 | -4.3 | -12.5 |  |
| money_level+money_moving | close | pin limit <$1k | 69-76 | 47.6 | -2.2 | -8.7 |  |
| money_level+sharp_gap | close | pin limit <$1k | 68-71 | 48.9 | -0.9 | -6.1 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 104-113 | 47.9 | -1.7 | -4.0 |  |
| consensus_gap+money_level | close | pin limit <$1k | 28-25 | 52.8 | 2.3 | -2.4 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 15-10 | 60.0 | 11.3 | 30.2 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 36-31 | 53.7 | 4.4 | 7.6 |  |
| follow_move+money_moving | close | pin limit <$1k | 65-73 | 47.1 | -2.6 | -9.5 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 70-73 | 49.0 | -0.8 | -6.0 |  |
| money_level+pin_move | close | pin limit <$1k | 50-47 | 51.5 | 1.6 | -1.6 |  |
| money_level+pin_value | close | pin limit <$1k | 46-32 | 59.0 | 9.3 | 11.5 |  |
| pin_move+pin_value | close | pin limit <$1k | 41-25 | 62.1 | 12.6 | 24.7 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 18-10 | 64.3 | 14.1 | 18.0 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 22-17 | 56.4 | 7.3 | 17.8 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 24-18 | 57.1 | 7.9 | 18.4 |  |
| follow_move+money_level | close | pin limit <$1k | 54-54 | 50.0 | -0.2 | -4.8 |  |
| follow_move+pin_move | close | pin limit <$1k | 60-60 | 50.0 | 0.2 | -4.3 |  |
| follow_move+pin_value | close | pin limit <$1k | 36-23 | 61.0 | 11.3 | 15.7 |  |
| money_moving+pin_move | close | pin limit <$1k | 59-61 | 49.2 | -0.5 | -2.3 |  |
| money_moving+pin_value | close | pin limit <$1k | 36-25 | 59.0 | 9.6 | 19.2 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 63-62 | 50.4 | 0.7 | -0.1 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 38-28 | 57.6 | 8.0 | 16.0 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 36-36 | 50.0 | 0.1 | -4.2 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 25-26 | 49.0 | -0.8 | -6.1 |  |
| money_delta+money_moving | close | pin limit <$1k | 43-45 | 48.9 | -0.8 | -1.4 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 7-6 | 53.8 | 5.8 | 35.2 |  |
| money_delta+money_level | close | pin limit <$1k | 25-19 | 56.8 | 6.7 | 8.8 |  |
| money_delta+pin_value | close | pin limit <$1k | 13-8 | 61.9 | 13.0 | 38.5 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 42-43 | 49.4 | -0.2 | -0.3 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 29-30 | 49.2 | -0.4 | 1.6 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 6-2 | 75.0 | 28.0 | 96.7 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 24-17 | 58.5 | 9.4 | 23.0 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 38-27 | 58.5 | 9.3 | 25.7 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 40-29 | 58.0 | 8.4 | 17.5 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-4 | 82.6 | 33.5 | 76.8 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 41-29 | 58.6 | 9.4 | 24.9 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 4-1 | 80.0 | 29.9 | 51.3 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 12-7 | 63.2 | 13.1 | 20.9 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 9-17 | 34.6 | -14.9 | -33.8 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 20-21 | 48.8 | -0.9 | -6.4 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 32-22 | 59.3 | 9.5 | 14.0 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 44-34 | 56.4 | 6.8 | 8.9 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 25-21 | 54.3 | 4.6 | 4.4 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 19-25 | 43.2 | -6.6 | -17.1 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 40-32 | 55.6 | 6.0 | 7.4 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 32-22 | 59.3 | 9.5 | 14.0 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 14-10 | 58.3 | 9.0 | 11.9 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 32-22 | 59.3 | 9.5 | 14.0 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 21-18 | 53.8 | 4.2 | 3.2 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 44-34 | 56.4 | 6.8 | 8.9 |  |
| money_level+pin_rlm | close | pin limit <$1k | 19-12 | 61.3 | 11.1 | 17.6 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 21-14 | 60.0 | 10.5 | 16.8 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 16-5 | 76.2 | 26.1 | 46.1 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 5-3 | 62.5 | 12.6 | 18.4 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 49.7 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -3.4 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -50.9 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 27-28 | 49.1 | 13.9 | 21.6 | 0.24 |
| rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -14.2 | -3.3 | -0.95 |
| rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| rlm_quiet | early | pin limit <$1k | 5-7 | 41.7 | -2.3 | -15.0 | 0.27 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -49.7 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 5-8 | 38.5 | -9.6 | -31.5 | 0.32 |
| pin_move | early | pin $1-2k | 0-3 | 0.0 | -35.1 | -100.0 | 0.23 |
| pin_move | early | pin limit <$1k | 5-6 | 45.5 | -6.3 | -19.1 | 0.22 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.8 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 8-6 | 57.1 | 17.0 | 26.7 | -0.34 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -39.4 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 4-0 | 100.0 | 50.5 | 88.0 | -0.25 |
| pin_rlm | early | <1k bets | 1-2 | 33.3 | 6.7 | -35.8 | -1.0 |
| pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -26.6 | -100.0 | -1.75 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.3 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -50.9 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 394-323 | 55.0 | 2.6 | -4.6 | 0.2 |
| follow_move | early | pin $1-2k | 27-17 | 61.4 | 7.2 | 9.4 | -0.34 |
| follow_move | early | pin $2k+ | 0-2 | 0.0 | -39.4 | -100.0 | 0.65 |
| follow_move | early | pin limit <$1k | 47-39 | 54.7 | 4.4 | 1.9 | -0.11 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 23-13 | 63.9 | 26.8 | 41.4 | 0.6 |
| rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.2 | 55.6 | -1.52 |
| rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -39.4 | -100.0 | 0.65 |
| rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 0.9 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 42.8 | 59.7 | 0.33 |
| money_level | early | <1k bets | 140-89 | 61.1 | 1.4 | -4.4 | -0.16 |
| money_level | early | pin $1-2k | 21-8 | 72.4 | 7.3 | 7.1 | 0.01 |
| money_level | early | pin $2k+ | 1-1 | 50.0 | -12.7 | -47.2 | -0.7 |
| money_level | early | pin limit <$1k | 24-26 | 48.0 | -5.2 | -11.4 | 0.22 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.5 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.1 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 116-98 | 54.2 | 5.6 | 4.5 | 0.35 |
| sharp_gap | early | pin $1-2k | 16-11 | 59.3 | 6.4 | 9.8 | -0.37 |
| sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -39.4 | -100.0 | 0.65 |
| sharp_gap | early | pin limit <$1k | 29-18 | 61.7 | 13.1 | 27.9 | 0.12 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.5 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.9 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 78-69 | 53.1 | 1.2 | -7.7 | 0.01 |
| money_moving | early | pin $1-2k | 8-9 | 47.1 | -11.0 | -35.5 | 0.2 |
| money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.7 | -8.4 | 0.65 |
| money_moving | early | pin limit <$1k | 23-9 | 71.9 | 22.7 | 52.0 | 0.42 |
| pin_value | early | 1-3k bets | 13-10 | 56.5 | 8.0 | 6.3 | -0.04 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 36-39 | 48.0 | -0.3 | -9.2 | 0.13 |
| pin_value | early | pin $1-2k | 13-19 | 40.6 | -5.2 | -23.6 | 0.12 |
| pin_value | early | pin $2k+ | 1-0 | 100.0 | 52.1 | 83.3 | 0.0 |
| pin_value | early | pin limit <$1k | 36-30 | 54.5 | 5.0 | 3.2 | 0.09 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -49.7 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -26.7 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.3 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.7 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 175-236 | 42.6 | -4.8 | -14.8 | 0.36 |
| consensus_gap | early | pin $1-2k | 12-20 | 37.5 | -7.9 | -28.2 | 0.51 |
| consensus_gap | early | pin $2k+ | 1-1 | 50.0 | 12.7 | -8.4 | 0.65 |
| consensus_gap | early | pin limit <$1k | 18-34 | 34.6 | -15.5 | -28.2 | 0.28 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.8 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.8 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -0.9 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.1 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 4.7 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.1 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 7-4 | 63.6 | 13.9 | 19.4 | -0.09 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.4 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.6 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -49.7 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -1.0 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 6-5 | 54.5 | 8.0 | 1.3 | 0.27 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -0.4 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-7 | 50.0 | 2.5 | -6.4 | -0.29 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -3.4 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.1 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.2 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.5 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 2.7 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.5 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.6 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.1 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.6 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 52.1 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 12.3 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 18.9 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 17.6 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 17.6 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| follow_move+rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -50.9 | -100.0 | -0.5 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.9 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| rlm_quiet+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| rlm_quiet+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 38.2 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 49.7 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 26-33 | 44.1 | -7.7 | -19.4 | 0.84 |
| consensus_gap+money_level | early | <1k bets | 27-21 | 56.2 | -9.1 | -11.4 | 0.36 |
| consensus_gap+sharp_gap | early | <1k bets | 22-38 | 36.7 | -10.1 | -18.6 | 1.0 |
| follow_move+money_level | early | <1k bets | 76-33 | 69.7 | 8.3 | 2.7 | -0.01 |
| follow_move+sharp_gap | early | <1k bets | 63-27 | 70.0 | 19.4 | 23.6 | 0.49 |
| money_level+sharp_gap | early | <1k bets | 79-47 | 62.7 | 6.1 | 2.0 | 0.15 |
| follow_move+money_moving | early | <1k bets | 41-23 | 64.1 | 9.8 | 10.2 | 0.33 |
| money_level+money_moving | early | <1k bets | 49-34 | 59.0 | -0.0 | -7.1 | -0.29 |
| money_moving+sharp_gap | early | <1k bets | 46-40 | 53.5 | 3.9 | -3.9 | 0.18 |
| consensus_gap+money_moving | early | <1k bets | 10-19 | 34.5 | -13.7 | -44.4 | 0.26 |
| follow_move+pin_value | early | <1k bets | 13-11 | 54.2 | 4.5 | 1.3 | -0.01 |
| follow_move+rlm_quiet | early | <1k bets | 27-28 | 49.1 | 13.9 | 21.6 | 0.24 |
| money_moving+rlm_quiet | early | <1k bets | 9-8 | 52.9 | 16.7 | 29.1 | 0.44 |
| rlm_quiet+sharp_gap | early | <1k bets | 16-10 | 61.5 | 25.9 | 39.2 | -0.02 |
| follow_move+rlm_ratio | early | <1k bets | 23-13 | 63.9 | 26.8 | 41.4 | 0.6 |
| rlm_quiet+rlm_ratio | early | <1k bets | 14-7 | 66.7 | 31.1 | 54.1 | 0.02 |
| rlm_ratio+sharp_gap | early | <1k bets | 23-13 | 63.9 | 26.8 | 41.4 | 0.6 |
| pin_move+pin_value | early | <1k bets | 1-4 | 20.0 | -29.1 | -61.8 | 0.2 |
| follow_move+pin_move | early | <1k bets | 5-3 | 62.5 | 10.3 | 11.2 | 0.42 |
| consensus_gap+pin_value | early | <1k bets | 13-23 | 36.1 | -10.4 | -32.5 | 0.4 |
| pin_value+rlm_quiet | early | <1k bets | 0-3 | 0.0 | -43.0 | -100.0 | -0.6 |
| money_delta+money_moving | early | <1k bets | 7-6 | 53.8 | 14.5 | 21.7 | -0.36 |
| money_delta+sharp_gap | early | <1k bets | 6-4 | 60.0 | 21.6 | 39.1 | -0.47 |
| consensus_gap+pin_move | early | <1k bets | 0-5 | 0.0 | -44.5 | -100.0 | 0.26 |
| money_level+pin_move | early | <1k bets | 2-2 | 50.0 | -5.8 | -21.8 | 0.1 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| consensus_gap+rlm_quiet | early | <1k bets | 3-5 | 37.5 | -1.0 | -22.7 | 1.01 |
| consensus_gap+rlm_ratio | early | <1k bets | 4-3 | 57.1 | 17.0 | 15.6 | 0.6 |
| follow_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 23.4 | -3.7 | -2.15 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | <1k bets | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 23.4 | -3.7 | -2.15 |
| pin_rlm+sharp_gap | early | <1k bets | 1-2 | 33.3 | 6.7 | -35.8 | -1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 11.5 | -4.5 | -1.9 |
| pin_value+sharp_gap | early | <1k bets | 5-4 | 55.6 | 8.4 | 6.1 | -0.09 |
| money_level+pin_value | early | <1k bets | 4-4 | 50.0 | 0.1 | -4.5 | 0.88 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -51.2 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -50.3 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 1-2 | 33.3 | -17.4 | -36.4 | 1.33 |
| money_level+rlm_ratio | early | <1k bets | 7-6 | 53.8 | 16.3 | 12.9 | 1.69 |
| money_moving+rlm_ratio | early | <1k bets | 9-5 | 64.3 | 22.7 | 48.0 | 0.36 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 50.3 | 90.9 | 0.0 |
| money_delta+money_level | early | <1k bets | 3-1 | 75.0 | 30.8 | 61.5 | 1.2 |
| pin_move+sharp_gap | early | <1k bets | 2-1 | 66.7 | 16.8 | 4.3 | -0.07 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 3-3 | 50.0 | 11.5 | 37.5 | 0.07 |
| money_delta+rlm_quiet | early | <1k bets | 1-2 | 33.3 | -1.2 | 23.3 | -2.8 |
| money_delta+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 32.1 | 111.3 | 0.87 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 49.7 | 90.9 | -1.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 5-4 | 55.6 | -9.3 | -12.6 | 0.71 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -31.5 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 5-10 | 33.3 | -8.0 | -38.7 | 0.31 |
| follow_move+rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -14.2 | -3.3 | -0.95 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.2 | 55.6 | -1.52 |
| follow_move+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 13.8 | 37.5 | -0.83 |
| money_level+money_moving | early | pin $1-2k | 8-5 | 61.5 | -4.3 | -15.6 | 0.07 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.7 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-2 | 33.3 | -16.8 | -38.9 | 0.67 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -8.0 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -8.0 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-3 | 40.0 | 3.2 | 55.6 | -1.52 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -39.4 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -39.4 | -100.0 | 2.5 |
| money_level+sharp_gap | early | pin $1-2k | 13-4 | 76.5 | 12.7 | 17.1 | -0.25 |
| money_moving+sharp_gap | early | pin $1-2k | 4-6 | 40.0 | -16.8 | -45.4 | 0.08 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.9 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 4-6 | 40.0 | -10.0 | -31.3 | 0.34 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 0-3 | 0.0 | -26.6 | -100.0 | -0.97 |
| follow_move+pin_value | early | pin $1-2k | 6-6 | 50.0 | 2.3 | -7.6 | -0.27 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -26.6 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 11-4 | 73.3 | 8.2 | 6.6 | -0.07 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 47.9 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 4-2 | 66.7 | 1.4 | -10.9 | -0.15 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -16.7 | -46.8 | -0.12 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -26.6 | -100.0 | -1.75 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | -4.8 |
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -26.6 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.7 | -8.4 | 0.65 |
| consensus_gap+pin_value | early | pin $2k+ | 1-0 | 100.0 | 52.1 | 83.3 | 0.0 |
| follow_move+money_level | early | pin $2k+ | 0-1 | 0.0 | -52.1 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -39.4 | -100.0 | 0.65 |
| follow_move+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -39.4 | -100.0 | 0.65 |
| money_level+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -52.1 | -100.0 | 0.0 |
| money_level+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -52.1 | -100.0 | 0.0 |
| money_moving+pin_value | early | pin $2k+ | 1-0 | 100.0 | 52.1 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -39.4 | -100.0 | 0.65 |
| consensus_gap+follow_move | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| follow_move+money_moving | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| money_moving+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| money_moving+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| money_moving+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| rlm_quiet+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| rlm_quiet+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin limit <$1k | 5-7 | 41.7 | -2.3 | -15.0 | 0.27 |
| money_level+money_moving | early | pin limit <$1k | 13-7 | 65.0 | 12.7 | 20.2 | 0.48 |
| money_level+sharp_gap | early | pin limit <$1k | 20-16 | 55.6 | 4.9 | 1.6 | 0.14 |
| money_moving+sharp_gap | early | pin limit <$1k | 18-5 | 78.3 | 30.3 | 70.1 | 0.35 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -49.7 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 9-6 | 60.0 | 9.9 | 13.8 | 0.33 |
| money_moving+pin_value | early | pin limit <$1k | 7-4 | 63.6 | 13.8 | 20.1 | 0.18 |
| pin_value+sharp_gap | early | pin limit <$1k | 12-6 | 66.7 | 16.7 | 26.4 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-9 | 40.0 | -12.0 | -25.7 | 0.53 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -26.6 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 14-18 | 43.8 | -5.2 | -17.9 | 0.43 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.1 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 11-11 | 50.0 | -3.9 | -7.4 | -0.04 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 4.5 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 13-7 | 65.0 | 16.5 | 24.2 | -0.07 |
| follow_move+rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level+rlm_ratio | early | pin limit <$1k | 6-0 | 100.0 | 53.7 | 92.6 | 0.42 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 16.6 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| consensus_gap+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 22.8 | 72.3 | 0.54 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 0.9 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 9-3 | 75.0 | 25.5 | 43.3 | 0.33 |
| money_delta+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_delta+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 52.1 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 3-1 | 75.0 | 25.5 | 41.3 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.0 | 45.3 | -0.5 |
| money_delta+sharp_gap | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 | -0.5 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 11.8 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 24.5 | 51.6 | -0.07 |
| pin_move+pin_value | early | pin limit <$1k | 1-4 | 20.0 | -29.1 | -61.8 | 0.2 |
| follow_move+pin_move | early | pin limit <$1k | 5-3 | 62.5 | 10.3 | 11.2 | 0.42 |
| consensus_gap+pin_move | early | pin limit <$1k | 0-3 | 0.0 | -56.4 | -100.0 | 0.53 |
| money_level+pin_move | early | pin limit <$1k | 2-2 | 50.0 | -5.8 | -21.8 | 0.1 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -50.3 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -50.3 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 16.8 | 4.3 | -0.07 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 49.7 | 90.9 | -1.0 |
| rlm_quiet | close | 1-3k bets | 19-43 | 30.6 | -9.8 | -19.9 |  |
| rlm_quiet | close | 3k+ bets | 3-5 | 37.5 | -4.6 | -21.5 |  |
| rlm_quiet | close | <1k bets | 2-14 | 12.5 | -26.7 | -76.1 |  |
| rlm_quiet | close | pin $1-2k | 9-20 | 31.0 | -10.1 | -34.7 |  |
| rlm_quiet | close | pin $2k+ | 7-11 | 38.9 | -1.3 | 38.0 |  |
| rlm_quiet | close | pin limit <$1k | 4-8 | 33.3 | -10.1 | -35.3 |  |
| pin_move | close | 1-3k bets | 43-48 | 47.3 | -1.7 | -8.2 |  |
| pin_move | close | 3k+ bets | 6-9 | 40.0 | -10.1 | -21.2 |  |
| pin_move | close | <1k bets | 6-10 | 37.5 | -13.4 | -30.5 |  |
| pin_move | close | pin $1-2k | 29-31 | 48.3 | -0.1 | -4.1 |  |
| pin_move | close | pin $2k+ | 17-21 | 44.7 | -6.6 | -16.8 |  |
| pin_move | close | pin limit <$1k | 9-15 | 37.5 | -10.9 | -28.0 |  |
| money_delta | close | 1-3k bets | 20-29 | 40.8 | 0.2 | -19.4 |  |
| money_delta | close | 3k+ bets | 6-2 | 75.0 | 29.5 | 52.1 |  |
| money_delta | close | <1k bets | 8-10 | 44.4 | 3.6 | 9.1 |  |
| money_delta | close | pin $1-2k | 13-12 | 52.0 | 9.9 | 14.7 |  |
| money_delta | close | pin $2k+ | 5-8 | 38.5 | 2.8 | -19.9 |  |
| money_delta | close | pin limit <$1k | 7-9 | 43.8 | 0.4 | -15.6 |  |
| pin_rlm | close | 1-3k bets | 6-14 | 30.0 | -9.4 | -41.3 |  |
| pin_rlm | close | 3k+ bets | 2-1 | 66.7 | 27.2 | 43.1 |  |
| pin_rlm | close | <1k bets | 1-4 | 20.0 | -21.0 | -61.8 |  |
| pin_rlm | close | pin $1-2k | 5-5 | 50.0 | 11.3 | -2.6 |  |
| pin_rlm | close | pin $2k+ | 1-6 | 14.3 | -22.9 | -66.6 |  |
| pin_rlm | close | pin limit <$1k | 3-8 | 27.3 | -14.9 | -46.7 |  |
| follow_move | close | 1-3k bets | 60-90 | 40.0 | -9.4 | -18.8 |  |
| follow_move | close | 3k+ bets | 11-10 | 52.4 | 1.1 | -3.5 |  |
| follow_move | close | <1k bets | 15-25 | 37.5 | -10.2 | -32.4 |  |
| follow_move | close | pin $1-2k | 32-42 | 43.2 | -5.7 | -17.9 |  |
| follow_move | close | pin $2k+ | 26-25 | 51.0 | 0.7 | 14.2 |  |
| follow_move | close | pin limit <$1k | 11-19 | 36.7 | -12.1 | -29.5 |  |
| rlm_ratio | close | 1-3k bets | 11-29 | 27.5 | -12.7 | -46.7 |  |
| rlm_ratio | close | 3k+ bets | 3-2 | 60.0 | 18.5 | 24.0 |  |
| rlm_ratio | close | <1k bets | 3-7 | 30.0 | -9.9 | -42.9 |  |
| rlm_ratio | close | pin $1-2k | 7-6 | 53.8 | 15.8 | 4.8 |  |
| rlm_ratio | close | pin $2k+ | 1-7 | 12.5 | -21.0 | -70.8 |  |
| rlm_ratio | close | pin limit <$1k | 5-8 | 38.5 | -4.9 | -25.8 |  |
| money_level | close | 1-3k bets | 87-64 | 57.6 | 0.1 | -3.7 |  |
| money_level | close | 3k+ bets | 15-13 | 53.6 | -2.8 | -7.2 |  |
| money_level | close | <1k bets | 26-10 | 72.2 | 16.3 | 27.8 |  |
| money_level | close | pin $1-2k | 40-28 | 58.8 | 2.8 | 2.5 |  |
| money_level | close | pin $2k+ | 28-25 | 52.8 | -5.4 | -15.6 |  |
| money_level | close | pin limit <$1k | 17-15 | 53.1 | -1.1 | 1.0 |  |
| sharp_gap | close | 1-3k bets | 54-82 | 39.7 | -8.2 | -26.7 |  |
| sharp_gap | close | 3k+ bets | 13-14 | 48.1 | -1.2 | -7.3 |  |
| sharp_gap | close | <1k bets | 18-16 | 52.9 | 6.4 | 8.1 |  |
| sharp_gap | close | pin $1-2k | 30-32 | 48.4 | -0.6 | -6.0 |  |
| sharp_gap | close | pin $2k+ | 20-29 | 40.8 | -6.1 | -22.5 |  |
| sharp_gap | close | pin limit <$1k | 10-18 | 35.7 | -11.5 | -31.6 |  |
| money_moving | close | 1-3k bets | 58-81 | 41.7 | -7.1 | -24.3 |  |
| money_moving | close | 3k+ bets | 13-14 | 48.1 | -1.2 | -7.3 |  |
| money_moving | close | <1k bets | 18-16 | 52.9 | 6.4 | 8.1 |  |
| money_moving | close | pin $1-2k | 32-30 | 51.6 | 1.5 | -1.9 |  |
| money_moving | close | pin $2k+ | 20-29 | 40.8 | -6.1 | -22.5 |  |
| money_moving | close | pin limit <$1k | 12-19 | 38.7 | -9.4 | -26.0 |  |
| pin_value | close | 1-3k bets | 40-26 | 60.6 | 10.2 | 31.9 |  |
| pin_value | close | 3k+ bets | 3-5 | 37.5 | -17.3 | -28.6 |  |
| pin_value | close | <1k bets | 10-3 | 76.9 | 28.3 | 73.5 |  |
| pin_value | close | pin $1-2k | 25-18 | 58.1 | 8.8 | 22.9 |  |
| pin_value | close | pin $2k+ | 12-9 | 57.1 | 7.6 | 53.0 |  |
| pin_value | close | pin limit <$1k | 16-7 | 69.6 | 15.7 | 32.1 |  |
| consensus_gap | close | 1-3k bets | 34-24 | 58.6 | 4.7 | 2.5 |  |
| consensus_gap | close | 3k+ bets | 3-3 | 50.0 | -2.3 | -15.1 |  |
| consensus_gap | close | <1k bets | 11-1 | 91.7 | 35.7 | 83.1 |  |
| consensus_gap | close | pin $1-2k | 11-9 | 55.0 | 0.6 | 23.3 |  |
| consensus_gap | close | pin $2k+ | 21-6 | 77.8 | 19.3 | 26.3 |  |
| consensus_gap | close | pin limit <$1k | 6-2 | 75.0 | 24.7 | 42.9 |  |
| follow_move+pin_move | close | 1-3k bets | 27-41 | 39.7 | -8.8 | -23.5 |  |
| money_delta+money_moving | close | 1-3k bets | 14-20 | 41.2 | 2.1 | -17.9 |  |
| money_delta+sharp_gap | close | 1-3k bets | 14-19 | 42.4 | 3.5 | -15.4 |  |
| money_moving+sharp_gap | close | 1-3k bets | 53-79 | 40.2 | -8.1 | -25.9 |  |
| consensus_gap+money_level | close | 1-3k bets | 24-12 | 66.7 | 5.8 | 7.5 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 19-43 | 30.6 | -9.8 | -19.9 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 9-18 | 33.3 | -7.8 | -29.8 |  |
| consensus_gap+follow_move | close | 1-3k bets | 11-11 | 50.0 | -2.4 | -12.2 |  |
| follow_move+money_level | close | 1-3k bets | 29-33 | 46.8 | -10.6 | -20.0 |  |
| money_level+money_moving | close | 1-3k bets | 42-42 | 50.0 | -4.7 | -12.8 |  |
| money_level+sharp_gap | close | 1-3k bets | 38-41 | 48.1 | -6.1 | -14.3 |  |
| consensus_gap+money_moving | close | 1-3k bets | 9-15 | 37.5 | -15.0 | -35.6 |  |
| consensus_gap+pin_move | close | 1-3k bets | 7-5 | 58.3 | 8.3 | 20.6 |  |
| consensus_gap+pin_value | close | 1-3k bets | 13-10 | 56.5 | 6.3 | 5.9 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 8-15 | 34.8 | -16.0 | -37.8 |  |
| follow_move+money_moving | close | 1-3k bets | 24-49 | 32.9 | -15.6 | -40.3 |  |
| follow_move+pin_value | close | 1-3k bets | 11-9 | 55.0 | 3.5 | 52.3 |  |
| follow_move+sharp_gap | close | 1-3k bets | 25-51 | 32.9 | -14.9 | -40.2 |  |
| money_level+pin_move | close | 1-3k bets | 20-20 | 50.0 | -4.7 | -10.1 |  |
| money_level+pin_value | close | 1-3k bets | 14-12 | 53.8 | 0.7 | 1.1 |  |
| money_moving+pin_move | close | 1-3k bets | 18-22 | 45.0 | -3.8 | -15.0 |  |
| money_moving+pin_value | close | 1-3k bets | 11-14 | 44.0 | -6.8 | -17.4 |  |
| pin_move+pin_value | close | 1-3k bets | 12-10 | 54.5 | 2.7 | 2.5 |  |
| pin_move+sharp_gap | close | 1-3k bets | 16-24 | 40.0 | -7.6 | -24.5 |  |
| pin_value+sharp_gap | close | 1-3k bets | 10-13 | 43.5 | -6.8 | -18.5 |  |
| follow_move+money_delta | close | 1-3k bets | 10-21 | 32.3 | -9.0 | -37.2 |  |
| money_delta+pin_move | close | 1-3k bets | 6-10 | 37.5 | -2.2 | -26.1 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 6-16 | 27.3 | -12.5 | -46.9 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 11-29 | 27.5 | -12.7 | -46.7 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 6-21 | 22.2 | -16.1 | -55.4 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 11-27 | 28.9 | -11.7 | -43.9 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 4-21 | 16.0 | -21.5 | -68.9 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 6-24 | 20.0 | -17.7 | -59.9 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 11-29 | 27.5 | -12.7 | -46.7 |  |
| money_delta+money_level | close | 1-3k bets | 4-3 | 57.1 | 12.0 | 11.9 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 3-6 | 33.3 | -4.0 | -35.4 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 2-4 | 33.3 | -0.6 | -34.9 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 8-15 | 34.8 | -5.2 | -32.3 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 1-2 | 33.3 | -14.4 | -33.3 |  |
| money_level+pin_rlm | close | 1-3k bets | 4-3 | 57.1 | 12.0 | 11.3 |  |
| money_moving+pin_rlm | close | 1-3k bets | 6-13 | 31.6 | -8.2 | -38.2 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 6-14 | 30.0 | -9.4 | -41.3 |  |
| money_level+rlm_ratio | close | 1-3k bets | 6-6 | 50.0 | 5.3 | -2.8 |  |
| consensus_gap+money_delta | close | 1-3k bets | 2-2 | 50.0 | 15.1 | -2.3 |  |
| follow_move+pin_rlm | close | 1-3k bets | 6-11 | 35.3 | -2.7 | -30.9 |  |
| money_delta+pin_rlm | close | 1-3k bets | 4-8 | 33.3 | -3.4 | -34.0 |  |
| pin_move+pin_rlm | close | 1-3k bets | 6-10 | 37.5 | -1.5 | -26.6 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 6-9 | 40.0 | 1.3 | -21.7 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 2-8 | 20.0 | -16.5 | -60.5 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 6-11 | 35.3 | -2.7 | -30.9 |  |
| money_delta+pin_value | close | 1-3k bets | 6-2 | 75.0 | 30.1 | 42.7 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 3-3 | 50.0 | 6.4 | 157.0 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 2-0 | 100.0 | 50.0 | 88.9 |  |
| pin_rlm+pin_value | close | 1-3k bets | 0-1 | 0.0 | -43.2 | -100.0 |  |
| money_level+money_moving | close | 3k+ bets | 9-9 | 50.0 | -4.0 | -9.1 |  |
| money_level+sharp_gap | close | 3k+ bets | 9-9 | 50.0 | -4.0 | -9.1 |  |
| money_moving+sharp_gap | close | 3k+ bets | 13-14 | 48.1 | -1.2 | -7.3 |  |
| follow_move+money_delta | close | 3k+ bets | 3-2 | 60.0 | 11.4 | 15.4 |  |
| follow_move+money_level | close | 3k+ bets | 6-3 | 66.7 | 5.5 | 8.1 |  |
| follow_move+money_moving | close | 3k+ bets | 7-4 | 63.6 | 13.2 | 17.6 |  |
| follow_move+pin_move | close | 3k+ bets | 5-7 | 41.7 | -7.9 | -17.9 |  |
| follow_move+pin_rlm | close | 3k+ bets | 2-1 | 66.7 | 27.2 | 43.1 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 3-2 | 60.0 | 18.5 | 24.0 |  |
| follow_move+sharp_gap | close | 3k+ bets | 7-4 | 63.6 | 13.2 | 17.6 |  |
| money_delta+money_level | close | 3k+ bets | 2-0 | 100.0 | 50.0 | 93.0 |  |
| money_delta+money_moving | close | 3k+ bets | 5-1 | 83.3 | 39.3 | 69.8 |  |
| money_delta+pin_move | close | 3k+ bets | 2-2 | 50.0 | 3.4 | -3.5 |  |
| money_delta+pin_rlm | close | 3k+ bets | 1-1 | 50.0 | 6.8 | -2.4 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 2-1 | 66.7 | 18.9 | 28.7 |  |
| money_delta+sharp_gap | close | 3k+ bets | 5-1 | 83.3 | 39.3 | 69.8 |  |
| money_level+pin_move | close | 3k+ bets | 2-3 | 40.0 | -18.0 | -28.5 |  |
| money_level+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 56.8 | 95.2 |  |
| money_level+rlm_ratio | close | 3k+ bets | 2-0 | 100.0 | 50.0 | 93.0 |  |
| money_moving+pin_move | close | 3k+ bets | 3-3 | 50.0 | 0.4 | -8.6 |  |
| money_moving+pin_rlm | close | 3k+ bets | 2-1 | 66.7 | 27.2 | 43.1 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 3-2 | 60.0 | 18.5 | 24.0 |  |
| pin_move+pin_rlm | close | 3k+ bets | 1-1 | 50.0 | 6.8 | -2.4 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 1-1 | 50.0 | 6.8 | -2.4 |  |
| pin_move+sharp_gap | close | 3k+ bets | 3-3 | 50.0 | 0.4 | -8.6 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 2-1 | 66.7 | 27.2 | 43.1 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 2-1 | 66.7 | 27.2 | 43.1 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 3-2 | 60.0 | 18.5 | 24.0 |  |
| consensus_gap+money_level | close | 3k+ bets | 2-1 | 66.7 | 2.5 | 6.1 |  |
| consensus_gap+money_moving | close | 3k+ bets | 2-2 | 50.0 | -6.2 | -20.0 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 2-2 | 50.0 | -6.2 | -20.0 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 3-5 | 37.5 | -4.6 | -21.5 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 3-4 | 42.9 | -0.7 | -10.3 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 1-2 | 33.3 | -14.4 | -36.4 |  |
| money_level+pin_value | close | 3k+ bets | 2-3 | 40.0 | -13.6 | -24.0 |  |
| money_moving+pin_value | close | 3k+ bets | 2-3 | 40.0 | -11.4 | -23.6 |  |
| pin_value+sharp_gap | close | 3k+ bets | 2-3 | 40.0 | -11.4 | -23.6 |  |
| consensus_gap+follow_move | close | 3k+ bets | 2-0 | 100.0 | 37.6 | 60.0 |  |
| consensus_gap+pin_value | close | 3k+ bets | 2-0 | 100.0 | 43.2 | 90.1 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 1-3 | 25.0 | -18.8 | -52.3 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 1-3 | 25.0 | -18.8 | -52.3 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 0-1 | 0.0 | -43.2 | -100.0 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 0-2 | 0.0 | -37.6 | -100.0 |  |
| pin_move+pin_value | close | 3k+ bets | 1-3 | 25.0 | -31.2 | -52.3 |  |
| follow_move+pin_value | close | 3k+ bets | 1-1 | 50.0 | -12.4 | -4.5 |  |
| consensus_gap+money_delta | close | 3k+ bets | 1-0 | 100.0 | 43.2 | 90.9 |  |
| consensus_gap+pin_move | close | 3k+ bets | 1-0 | 100.0 | 43.2 | 90.9 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 1-0 | 100.0 | 43.2 | 90.9 |  |
| money_delta+pin_value | close | 3k+ bets | 1-0 | 100.0 | 43.2 | 90.9 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 1-0 | 100.0 | 43.2 | 90.9 |  |
| consensus_gap+money_level | close | <1k bets | 8-0 | 100.0 | 39.7 | 59.7 |  |
| consensus_gap+money_moving | close | <1k bets | 6-0 | 100.0 | 46.3 | 123.4 |  |
| consensus_gap+pin_value | close | <1k bets | 3-0 | 100.0 | 56.0 | 208.2 |  |
| consensus_gap+sharp_gap | close | <1k bets | 6-0 | 100.0 | 46.3 | 123.4 |  |
| follow_move+pin_move | close | <1k bets | 4-9 | 30.8 | -18.7 | -43.5 |  |
| follow_move+rlm_quiet | close | <1k bets | 2-14 | 12.5 | -26.7 | -76.1 |  |
| money_level+money_moving | close | <1k bets | 13-5 | 72.2 | 20.2 | 31.1 |  |
| money_level+pin_value | close | <1k bets | 4-0 | 100.0 | 46.6 | 90.2 |  |
| money_level+sharp_gap | close | <1k bets | 13-5 | 72.2 | 20.2 | 31.1 |  |
| money_moving+pin_value | close | <1k bets | 4-1 | 80.0 | 39.0 | 124.8 |  |
| money_moving+sharp_gap | close | <1k bets | 18-16 | 52.9 | 6.4 | 8.1 |  |
| pin_move+rlm_quiet | close | <1k bets | 1-4 | 20.0 | -23.7 | -61.8 |  |
| pin_value+sharp_gap | close | <1k bets | 4-1 | 80.0 | 39.0 | 124.8 |  |
| follow_move+money_moving | close | <1k bets | 6-10 | 37.5 | -8.4 | -36.2 |  |
| follow_move+sharp_gap | close | <1k bets | 6-10 | 37.5 | -8.4 | -36.2 |  |
| money_level+pin_move | close | <1k bets | 3-4 | 42.9 | -11.6 | -23.4 |  |
| money_moving+rlm_quiet | close | <1k bets | 2-6 | 25.0 | -15.4 | -52.3 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 2-6 | 25.0 | -15.4 | -52.3 |  |
| follow_move+money_delta | close | <1k bets | 4-7 | 36.4 | -6.0 | -31.3 |  |
| follow_move+pin_rlm | close | <1k bets | 1-4 | 20.0 | -21.0 | -61.8 |  |
| follow_move+pin_value | close | <1k bets | 2-0 | 100.0 | 50.0 | 93.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -9.9 | -42.9 |  |
| money_delta+money_moving | close | <1k bets | 6-8 | 42.9 | 3.6 | 13.5 |  |
| money_delta+pin_move | close | <1k bets | 1-3 | 25.0 | -15.4 | -52.3 |  |
| money_delta+pin_rlm | close | <1k bets | 1-3 | 25.0 | -15.4 | -52.3 |  |
| money_delta+pin_value | close | <1k bets | 3-0 | 100.0 | 60.5 | 212.0 |  |
| money_delta+rlm_quiet | close | <1k bets | 2-4 | 33.3 | -6.2 | -36.4 |  |
| money_delta+rlm_ratio | close | <1k bets | 3-5 | 37.5 | -2.9 | -28.6 |  |
| money_delta+sharp_gap | close | <1k bets | 6-8 | 42.9 | 3.6 | 13.5 |  |
| money_moving+pin_move | close | <1k bets | 1-4 | 20.0 | -21.0 | -61.8 |  |
| money_moving+pin_rlm | close | <1k bets | 1-4 | 20.0 | -21.0 | -61.8 |  |
| money_moving+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -9.9 | -42.9 |  |
| pin_move+pin_rlm | close | <1k bets | 1-4 | 20.0 | -21.0 | -61.8 |  |
| pin_move+pin_value | close | <1k bets | 3-0 | 100.0 | 47.7 | 91.0 |  |
| pin_move+rlm_ratio | close | <1k bets | 1-4 | 20.0 | -21.0 | -61.8 |  |
| pin_move+sharp_gap | close | <1k bets | 1-4 | 20.0 | -21.0 | -61.8 |  |
| pin_rlm+pin_value | close | <1k bets | 1-0 | 100.0 | 56.8 | 90.9 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 1-2 | 33.3 | -9.8 | -36.4 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 1-4 | 20.0 | -21.0 | -61.8 |  |
| pin_rlm+sharp_gap | close | <1k bets | 1-4 | 20.0 | -21.0 | -61.8 |  |
| pin_value+rlm_quiet | close | <1k bets | 1-0 | 100.0 | 56.8 | 90.9 |  |
| pin_value+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 56.8 | 90.9 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 2-5 | 28.6 | -11.4 | -45.5 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 3-7 | 30.0 | -9.9 | -42.9 |  |
| consensus_gap+follow_move | close | <1k bets | 3-0 | 100.0 | 40.3 | 74.7 |  |
| consensus_gap+pin_move | close | <1k bets | 1-0 | 100.0 | 32.1 | 50.0 |  |
| follow_move+money_level | close | <1k bets | 7-5 | 58.3 | 2.2 | -1.4 |  |
| money_delta+money_level | close | <1k bets | 2-2 | 50.0 | 12.4 | 15.3 |  |
| money_level+pin_rlm | close | <1k bets | 0-2 | 0.0 | -37.6 | -100.0 |  |
| money_level+rlm_ratio | close | <1k bets | 1-2 | 33.3 | -6.2 | -36.9 |  |
| consensus_gap+money_delta | close | <1k bets | 3-0 | 100.0 | 52.3 | 208.0 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 56.8 | 89.3 |  |
| money_delta+money_moving | close | pin $1-2k | 7-5 | 58.3 | 20.7 | 43.3 |  |
| money_delta+sharp_gap | close | pin $1-2k | 7-5 | 58.3 | 20.7 | 43.3 |  |
| money_moving+sharp_gap | close | pin $1-2k | 30-30 | 50.0 | 0.5 | -2.9 |  |
| consensus_gap+follow_move | close | pin $1-2k | 4-5 | 44.4 | -10.6 | -18.6 |  |
| consensus_gap+money_level | close | pin $1-2k | 6-4 | 60.0 | -2.4 | -3.1 |  |
| consensus_gap+money_moving | close | pin $1-2k | 4-5 | 44.4 | -9.1 | 8.7 |  |
| consensus_gap+pin_move | close | pin $1-2k | 2-3 | 40.0 | -6.9 | 14.2 |  |
| consensus_gap+pin_value | close | pin $1-2k | 4-4 | 50.0 | -0.3 | 39.9 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 3-5 | 37.5 | -14.2 | 8.0 |  |
| follow_move+money_level | close | pin $1-2k | 16-14 | 53.3 | -1.6 | -5.0 |  |
| follow_move+money_moving | close | pin $1-2k | 14-15 | 48.3 | -1.0 | -12.3 |  |
| follow_move+pin_move | close | pin $1-2k | 16-28 | 36.4 | -10.8 | -27.9 |  |
| follow_move+pin_value | close | pin $1-2k | 5-7 | 41.7 | -9.5 | -21.0 |  |
| follow_move+sharp_gap | close | pin $1-2k | 14-17 | 45.2 | -3.0 | -18.0 |  |
| money_level+money_moving | close | pin $1-2k | 26-18 | 59.1 | 5.2 | 3.8 |  |
| money_level+pin_move | close | pin $1-2k | 11-11 | 50.0 | -3.0 | -8.3 |  |
| money_level+pin_value | close | pin $1-2k | 7-6 | 53.8 | 1.2 | 0.5 |  |
| money_level+sharp_gap | close | pin $1-2k | 24-18 | 57.1 | 3.9 | 2.7 |  |
| money_moving+pin_move | close | pin $1-2k | 11-10 | 52.4 | 4.5 | -1.4 |  |
| money_moving+pin_value | close | pin $1-2k | 7-8 | 46.7 | -2.1 | 11.5 |  |
| pin_move+pin_value | close | pin $1-2k | 8-6 | 57.1 | 5.2 | 7.7 |  |
| pin_move+sharp_gap | close | pin $1-2k | 11-12 | 47.8 | 1.3 | -10.0 |  |
| pin_value+sharp_gap | close | pin $1-2k | 7-8 | 46.7 | -2.1 | 11.5 |  |
| follow_move+money_delta | close | pin $1-2k | 8-11 | 42.1 | -0.8 | -18.2 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 9-20 | 31.0 | -10.1 | -34.7 |  |
| money_delta+pin_move | close | pin $1-2k | 6-6 | 50.0 | 8.7 | -2.2 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 4-10 | 28.6 | -14.0 | -44.5 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 8-12 | 40.0 | -2.3 | -18.9 |  |
| follow_move+pin_rlm | close | pin $1-2k | 5-5 | 50.0 | 11.3 | -2.6 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 7-6 | 53.8 | 15.8 | 4.8 |  |
| pin_move+pin_rlm | close | pin $1-2k | 5-4 | 55.6 | 16.1 | 8.2 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 5-4 | 55.6 | 16.1 | 8.2 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 2-4 | 33.3 | -6.2 | -35.7 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 5-5 | 50.0 | 11.3 | -2.6 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 5-5 | 50.0 | 11.3 | -2.6 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 2-5 | 28.6 | -9.9 | -44.8 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 3-7 | 30.0 | -8.7 | -41.9 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 7-6 | 53.8 | 15.8 | 4.8 |  |
| money_delta+money_level | close | pin $1-2k | 3-1 | 75.0 | 37.4 | 48.1 |  |
| money_delta+pin_rlm | close | pin $1-2k | 4-3 | 57.1 | 18.7 | 11.9 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 5-4 | 55.6 | 17.3 | 8.7 |  |
| money_level+pin_rlm | close | pin $1-2k | 3-1 | 75.0 | 37.4 | 47.0 |  |
| money_level+rlm_ratio | close | pin $1-2k | 5-1 | 83.3 | 45.7 | 62.7 |  |
| money_moving+pin_rlm | close | pin $1-2k | 5-4 | 55.6 | 16.1 | 8.2 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 7-5 | 58.3 | 19.8 | 13.5 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 3-5 | 37.5 | -2.9 | -27.3 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 1-2 | 33.3 | -7.0 | -36.4 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 2-3 | 40.0 | -5.9 | -23.6 |  |
| money_delta+pin_value | close | pin $1-2k | 5-2 | 71.4 | 29.8 | 87.7 |  |
| consensus_gap+money_delta | close | pin $1-2k | 2-1 | 66.7 | 22.6 | 144.9 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 0-1 | 0.0 | -32.1 | -100.0 |  |
| pin_rlm+pin_value | close | pin $1-2k | 1-0 | 100.0 | 56.8 | 90.9 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 1-0 | 100.0 | 56.8 | 90.9 |  |
| follow_move+pin_move | close | pin $2k+ | 14-18 | 43.8 | -7.9 | -19.2 |  |
| consensus_gap+money_level | close | pin $2k+ | 15-5 | 75.0 | 13.2 | 14.8 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 7-11 | 38.9 | -1.3 | 38.0 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 3-9 | 25.0 | -15.1 | -41.6 |  |
| money_level+money_moving | close | pin $2k+ | 12-17 | 41.4 | -12.0 | -27.6 |  |
| money_level+sharp_gap | close | pin $2k+ | 12-17 | 41.4 | -12.0 | -27.6 |  |
| money_moving+sharp_gap | close | pin $2k+ | 20-29 | 40.8 | -6.1 | -22.5 |  |
| consensus_gap+pin_value | close | pin $2k+ | 9-4 | 69.2 | 21.0 | 29.1 |  |
| follow_move+money_level | close | pin $2k+ | 9-9 | 50.0 | -12.1 | -21.1 |  |
| follow_move+money_moving | close | pin $2k+ | 9-13 | 40.9 | -7.6 | -24.2 |  |
| follow_move+sharp_gap | close | pin $2k+ | 9-13 | 40.9 | -7.6 | -24.2 |  |
| money_level+pin_move | close | pin $2k+ | 7-8 | 46.7 | -15.0 | -24.3 |  |
| money_moving+pin_move | close | pin $2k+ | 5-9 | 35.7 | -14.5 | -34.6 |  |
| pin_move+sharp_gap | close | pin $2k+ | 5-9 | 35.7 | -14.5 | -34.6 |  |
| money_delta+money_level | close | pin $2k+ | 1-0 | 100.0 | 56.8 | 90.9 |  |
| money_delta+money_moving | close | pin $2k+ | 5-8 | 38.5 | 2.8 | -19.9 |  |
| money_delta+sharp_gap | close | pin $2k+ | 5-8 | 38.5 | 2.8 | -19.9 |  |
| consensus_gap+money_moving | close | pin $2k+ | 6-5 | 54.5 | -3.4 | -11.0 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 6-5 | 54.5 | -3.4 | -11.0 |  |
| money_level+pin_value | close | pin $2k+ | 3-5 | 37.5 | -12.2 | -29.4 |  |
| money_moving+pin_value | close | pin $2k+ | 3-5 | 37.5 | -10.8 | -28.8 |  |
| pin_value+sharp_gap | close | pin $2k+ | 3-5 | 37.5 | -10.8 | -28.8 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -67.9 | -100.0 |  |
| money_level+pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -67.9 | -100.0 |  |
| money_moving+pin_rlm | close | pin $2k+ | 1-6 | 14.3 | -22.9 | -66.6 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 1-6 | 14.3 | -22.9 | -66.6 |  |
| follow_move+money_delta | close | pin $2k+ | 1-5 | 16.7 | -21.4 | -68.2 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 1-7 | 12.5 | -21.0 | -70.8 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 0-5 | 0.0 | -34.3 | -100.0 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 1-7 | 12.5 | -21.0 | -70.8 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 1-7 | 12.5 | -21.0 | -70.8 |  |
| money_level+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -32.1 | -100.0 |  |
| consensus_gap+follow_move | close | pin $2k+ | 7-0 | 100.0 | 33.7 | 60.6 |  |
| consensus_gap+pin_move | close | pin $2k+ | 6-1 | 85.7 | 26.5 | 45.3 |  |
| follow_move+pin_value | close | pin $2k+ | 4-1 | 80.0 | 28.6 | 245.0 |  |
| pin_move+pin_value | close | pin $2k+ | 4-4 | 50.0 | -1.4 | -6.5 |  |
| follow_move+pin_rlm | close | pin $2k+ | 1-4 | 20.0 | -12.1 | -53.2 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 1-4 | 20.0 | -12.1 | -53.2 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 2-0 | 100.0 | 55.5 | 575.5 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 2-5 | 28.6 | -8.6 | -39.6 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 2-5 | 28.6 | -8.6 | -39.6 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 1-3 | 25.0 | -13.3 | -52.3 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 0-4 | 0.0 | -32.1 | -100.0 |  |
| money_delta+pin_move | close | pin $2k+ | 1-3 | 25.0 | -13.3 | -52.3 |  |
| money_delta+pin_rlm | close | pin $2k+ | 0-4 | 0.0 | -32.1 | -100.0 |  |
| pin_move+pin_rlm | close | pin $2k+ | 0-3 | 0.0 | -32.1 | -100.0 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 0-3 | 0.0 | -32.1 | -100.0 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 0-3 | 0.0 | -32.1 | -100.0 |  |
| consensus_gap+money_delta | close | pin $2k+ | 1-0 | 100.0 | 43.2 | 90.9 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 1-0 | 100.0 | 43.2 | 90.9 |  |
| money_delta+pin_value | close | pin $2k+ | 1-0 | 100.0 | 43.2 | 90.9 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 3-1 | 75.0 | 27.8 | 44.5 |  |
| consensus_gap+money_level | close | pin limit <$1k | 4-1 | 80.0 | 23.2 | 50.5 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 3-2 | 60.0 | 13.6 | 15.6 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 5-2 | 71.4 | 18.5 | 34.8 |  |
| follow_move+money_level | close | pin limit <$1k | 6-10 | 37.5 | -15.1 | -28.1 |  |
| follow_move+money_moving | close | pin limit <$1k | 6-14 | 30.0 | -17.4 | -42.4 |  |
| follow_move+pin_value | close | pin limit <$1k | 5-2 | 71.4 | 16.6 | 35.9 |  |
| money_level+money_moving | close | pin limit <$1k | 7-10 | 41.2 | -10.8 | -21.8 |  |
| money_level+pin_value | close | pin limit <$1k | 10-4 | 71.4 | 15.6 | 35.6 |  |
| money_moving+pin_value | close | pin limit <$1k | 7-5 | 58.3 | 7.2 | 10.7 |  |
| follow_move+pin_move | close | pin limit <$1k | 6-11 | 35.3 | -12.0 | -31.6 |  |
| money_level+pin_move | close | pin limit <$1k | 7-8 | 46.7 | -4.7 | -10.9 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 10-18 | 35.7 | -11.5 | -31.6 |  |
| pin_move+pin_value | close | pin limit <$1k | 4-3 | 57.1 | 2.3 | 9.1 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 4-8 | 33.3 | -10.1 | -35.3 |  |
| money_moving+pin_move | close | pin limit <$1k | 6-10 | 37.5 | -9.3 | -28.1 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 2-0 | 100.0 | 62.4 | 95.5 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 12.4 | 0.0 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 1-1 | 50.0 | 12.4 | 0.0 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 2-0 | 100.0 | 62.4 | 95.5 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 2-0 | 100.0 | 62.4 | 95.5 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 3-1 | 75.0 | 31.2 | 44.5 |  |
| follow_move+money_delta | close | pin limit <$1k | 4-6 | 40.0 | -3.4 | -22.7 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 3-7 | 30.0 | -12.1 | -41.4 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 5-8 | 38.5 | -4.9 | -25.8 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 6-13 | 31.6 | -15.3 | -39.4 |  |
| money_delta+money_moving | close | pin limit <$1k | 6-7 | 46.2 | 2.8 | -10.8 |  |
| money_delta+pin_move | close | pin limit <$1k | 2-6 | 25.0 | -16.8 | -50.6 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 2-5 | 28.6 | -13.0 | -43.5 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 2-2 | 50.0 | 9.6 | -2.3 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 4-5 | 44.4 | 1.0 | -14.1 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 6-7 | 46.2 | 2.8 | -10.8 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 3-8 | 27.3 | -14.9 | -46.7 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 2-5 | 28.6 | -13.0 | -44.2 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 5-8 | 38.5 | -4.9 | -25.8 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 3-8 | 27.3 | -14.9 | -46.7 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 2-5 | 28.6 | -15.0 | -44.2 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 3-7 | 30.0 | -12.1 | -41.4 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 4-10 | 28.6 | -16.7 | -44.8 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 1-4 | 20.0 | -21.0 | -60.0 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 3-7 | 30.0 | -12.1 | -41.4 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 3-8 | 27.3 | -14.9 | -46.7 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 2-5 | 28.6 | -13.0 | -44.2 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 2-5 | 28.6 | -13.0 | -44.2 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 5-8 | 38.5 | -4.9 | -25.8 |  |
| money_delta+pin_value | close | pin limit <$1k | 4-0 | 100.0 | 53.4 | 91.0 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 1-0 | 100.0 | 56.8 | 90.9 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 6-4 | 60.0 | 10.0 | 13.8 |  |
| money_level+sharp_gap | close | pin limit <$1k | 5-9 | 35.7 | -15.3 | -32.1 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 0-1 | 0.0 | -43.2 | -100.0 |  |
| money_delta+money_level | close | pin limit <$1k | 1-3 | 25.0 | -18.2 | -51.2 |  |
| money_level+pin_rlm | close | pin limit <$1k | 2-3 | 40.0 | -3.2 | -22.8 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 2-3 | 40.0 | -3.2 | -22.8 |  |
| rlm_quiet | early | <1k bets | 6-8 | 42.9 | 6.0 | -5.4 | 0.46 |
| rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -43.2 | -100.0 | 0.0 |
| pin_move | early | <1k bets | 1-1 | 50.0 | 0.0 | -4.5 | 0.0 |
| pin_move | early | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 | 0.0 |
| money_delta | early | <1k bets | 0-1 | 0.0 | -43.2 | -100.0 | 2.0 |
| follow_move | early | <1k bets | 48-57 | 45.7 | -2.8 | -13.1 | -0.08 |
| follow_move | early | pin $1-2k | 3-1 | 75.0 | 34.0 | 52.3 | -1.77 |
| follow_move | early | pin limit <$1k | 3-3 | 50.0 | 2.7 | -18.0 | -1.33 |
| rlm_ratio | early | <1k bets | 4-6 | 40.0 | -0.1 | -15.1 | 0.73 |
| money_level | early | <1k bets | 14-15 | 48.3 | -12.6 | -23.2 | 0.02 |
| money_level | early | pin limit <$1k | 1-0 | 100.0 | 43.2 | 90.9 | 0.0 |
| sharp_gap | early | <1k bets | 11-14 | 44.0 | -0.9 | -12.2 | 0.45 |
| sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -43.2 | -100.0 | 0.0 |
| money_moving | early | <1k bets | 12-11 | 52.2 | 3.5 | 3.6 | 0.57 |
| money_moving | early | pin limit <$1k | 0-1 | 0.0 | -43.2 | -100.0 | 0.0 |
| pin_value | early | <1k bets | 4-2 | 66.7 | 21.2 | 26.6 | -0.83 |
| pin_value | early | pin $1-2k | 1-1 | 50.0 | 6.8 | -6.5 | 0.5 |
| pin_value | early | pin limit <$1k | 3-1 | 75.0 | 28.4 | 43.2 | -1.5 |
| consensus_gap | early | <1k bets | 33-22 | 60.0 | 7.8 | 10.1 | 0.59 |
| consensus_gap | early | pin $1-2k | 0-1 | 0.0 | -32.1 | -100.0 | 0.0 |
| consensus_gap | early | pin limit <$1k | 1-0 | 100.0 | 43.2 | 90.9 | 0.0 |
| follow_move+money_level | early | <1k bets | 2-7 | 22.2 | -36.8 | -66.4 | 0.33 |
| follow_move+sharp_gap | early | <1k bets | 5-9 | 35.7 | -8.2 | -25.7 | 0.59 |
| money_level+sharp_gap | early | <1k bets | 4-6 | 40.0 | -16.3 | -33.3 | 0.42 |
| follow_move+money_moving | early | <1k bets | 6-7 | 46.2 | -1.4 | -4.0 | 0.62 |
| money_level+money_moving | early | <1k bets | 5-7 | 41.7 | -16.6 | -35.1 | 0.5 |
| consensus_gap+money_level | early | <1k bets | 6-4 | 60.0 | -2.1 | -12.8 | 0.08 |
| follow_move+rlm_quiet | early | <1k bets | 6-8 | 42.9 | 6.0 | -5.4 | 0.46 |
| follow_move+rlm_ratio | early | <1k bets | 4-6 | 40.0 | -0.1 | -15.1 | 0.73 |
| rlm_quiet+rlm_ratio | early | <1k bets | 4-4 | 50.0 | 12.4 | 6.1 | 0.04 |
| rlm_quiet+sharp_gap | early | <1k bets | 4-5 | 44.4 | 6.2 | -5.7 | 0.03 |
| rlm_ratio+sharp_gap | early | <1k bets | 4-6 | 40.0 | -0.1 | -15.1 | 0.73 |
| consensus_gap+follow_move | early | <1k bets | 3-5 | 37.5 | -16.7 | -41.2 | 0.89 |
| money_moving+rlm_quiet | early | <1k bets | 5-2 | 71.4 | 33.0 | 62.4 | 0.94 |
| money_moving+rlm_ratio | early | <1k bets | 4-3 | 57.1 | 15.2 | 21.2 | 1.66 |
| money_moving+sharp_gap | early | <1k bets | 7-8 | 46.7 | 1.2 | -2.7 | 0.9 |
| consensus_gap+money_moving | early | <1k bets | 3-1 | 75.0 | 16.0 | 6.5 | 0.07 |
| consensus_gap+sharp_gap | early | <1k bets | 3-2 | 60.0 | 8.6 | 5.2 | 0.5 |
| money_level+rlm_ratio | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 3.5 |
| follow_move+pin_move | early | <1k bets | 0-1 | 0.0 | -43.2 | -100.0 | 0.0 |
| follow_move+money_delta | early | <1k bets | 0-1 | 0.0 | -43.2 | -100.0 | 2.0 |
| money_delta+money_level | early | <1k bets | 0-1 | 0.0 | -43.2 | -100.0 | 2.0 |
| money_delta+money_moving | early | <1k bets | 0-1 | 0.0 | -43.2 | -100.0 | 2.0 |
| money_delta+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -43.2 | -100.0 | 2.0 |
| money_delta+sharp_gap | early | <1k bets | 0-1 | 0.0 | -43.2 | -100.0 | 2.0 |
| follow_move+pin_value | early | <1k bets | 2-1 | 66.7 | 23.5 | 27.3 | -2.0 |
| consensus_gap+pin_move | early | <1k bets | 1-0 | 100.0 | 43.2 | 90.9 | 0.0 |
| consensus_gap+pin_value | early | <1k bets | 1-0 | 100.0 | 43.2 | 90.9 | 0.0 |
| money_level+pin_move | early | <1k bets | 1-0 | 100.0 | 43.2 | 90.9 | 0.0 |
| money_level+pin_value | early | <1k bets | 1-0 | 100.0 | 43.2 | 90.9 | 0.0 |
| pin_move+pin_value | early | <1k bets | 1-0 | 100.0 | 43.2 | 90.9 | 0.0 |
| follow_move+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -43.2 | -100.0 | 0.0 |
| follow_move+pin_value | early | pin limit <$1k | 2-1 | 66.7 | 23.5 | 27.3 | -2.0 |
| consensus_gap+money_level | early | pin limit <$1k | 1-0 | 100.0 | 43.2 | 90.9 | 0.0 |
| consensus_gap+pin_move | early | pin limit <$1k | 1-0 | 100.0 | 43.2 | 90.9 | 0.0 |
| consensus_gap+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 43.2 | 90.9 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 0-1 | 0.0 | -43.2 | -100.0 | 0.0 |
| follow_move+rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -43.2 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -43.2 | -100.0 | 0.0 |
| money_level+pin_move | early | pin limit <$1k | 1-0 | 100.0 | 43.2 | 90.9 | 0.0 |
| money_level+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 43.2 | 90.9 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -43.2 | -100.0 | 0.0 |
| money_moving+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -43.2 | -100.0 | 0.0 |
| pin_move+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 43.2 | 90.9 | 0.0 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -43.2 | -100.0 | 0.0 |
