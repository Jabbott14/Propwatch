# CBB scorecard

Generated 2026-11-27 00:02 UTC. 978 graded games (35 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**684 games before 2026-11-21 (fit) · 294 on or after it (forward).**

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
sample ran **46.6% favourites** (n=977) and **50.6% overs** (n=978) and **71.1% moneyline favourites** (n=856).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-21. Nothing in the engine was chosen using these. n=294 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 26-35 | 42.6 | 39.0 | 3.7 | +1.11 | 1.8 | 0.9 | 50.8 | DROP: below break-even |
| pin_move | both | 9-16 | 36.0 | 49.8 | -13.8 | -8.09 | -32.4 | 0.49 | 40.0 | keep collecting (25/30) |
| money_delta | both | 4-5 | 44.4 | 38.1 | 6.3 | +1.47 | 16.3 | 3.02 | 100.0 | keep collecting (9/30) |
| pin_rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | keep collecting (2/30) |
| follow_move | both | 239-261 | 47.8 | 48.8 | -1.0 | -43.7 | -8.7 | 0.04 | 37.8 | DROP: below break-even |
| rlm_ratio | both | 10-16 | 38.5 | 41.5 | -3.1 | -1.99 | -7.6 | 0.4 | 53.8 | keep collecting (26/30) |
| money_level | both | 75-63 | 54.3 | 57.5 | -3.1 | -17.04 | -12.3 | -0.37 | 35.5 | no edge shown yet |
| sharp_gap | both | 58-65 | 47.2 | 50.0 | -2.9 | -12.22 | -9.9 | 0.2 | 45.5 | no edge shown yet |
| money_moving | both | 48-44 | 52.2 | 49.0 | 3.1 | -0.57 | -0.6 | 0.49 | 48.9 | no edge shown yet |
| pin_value | both | 23-20 | 53.5 | 49.4 | 4.1 | +0.49 | 1.1 | 0.11 | 34.9 | no edge shown yet |
| consensus_gap | both | 141-129 | 52.2 | 52.8 | -0.6 | -23.83 | -8.8 | 0.53 | 49.3 | no edge shown yet |
| follow_move+money_level | both | 26-19 | 57.8 | 57.1 | 0.7 | -5.93 | -13.2 | 0.28 | 37.8 | no edge shown yet |
| follow_move+sharp_gap | both | 24-27 | 47.1 | 47.8 | -0.7 | -3.98 | -7.8 | 0.71 | 47.1 | no edge shown yet |
| money_level+sharp_gap | both | 39-38 | 50.6 | 55.6 | -5.0 | -11.5 | -14.9 | -0.19 | 40.3 | no edge shown yet |
| follow_move+money_moving | both | 19-19 | 50.0 | 47.7 | 2.3 | +0.13 | 0.4 | 0.67 | 44.7 | no edge shown yet |
| money_level+money_moving | both | 23-18 | 56.1 | 55.1 | 1.0 | -1.1 | -2.7 | 0.41 | 46.3 | no edge shown yet |
| consensus_gap+money_level | both | 25-19 | 56.8 | 61.3 | -4.4 | -6.54 | -14.9 | -0.45 | 31.8 | no edge shown yet |
| follow_move+rlm_quiet | both | 26-35 | 42.6 | 39.0 | 3.7 | +1.11 | 1.8 | 0.9 | 50.8 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 10-16 | 38.5 | 41.5 | -3.1 | -1.99 | -7.6 | 0.4 | 53.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | both | 9-10 | 47.4 | 39.3 | 8.0 | +3.1 | 16.3 | 0.32 | 47.4 | keep collecting (19/30) |
| rlm_quiet+sharp_gap | both | 10-13 | 43.5 | 40.1 | 3.3 | +1.01 | 4.4 | 0.71 | 47.8 | keep collecting (23/30) |
| rlm_ratio+sharp_gap | both | 10-16 | 38.5 | 41.5 | -3.1 | -1.99 | -7.6 | 0.4 | 53.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 18-21 | 46.2 | 55.2 | -9.0 | -9.16 | -23.5 | 0.97 | 59.0 | no edge shown yet |
| money_moving+rlm_quiet | both | 9-10 | 47.4 | 39.3 | 8.0 | +2.99 | 15.7 | 0.91 | 47.4 | keep collecting (19/30) |
| money_moving+rlm_ratio | both | 7-6 | 53.8 | 40.6 | 13.2 | +4.05 | 31.1 | 1.58 | 69.2 | keep collecting (13/30) |
| money_moving+sharp_gap | both | 27-29 | 48.2 | 47.2 | 1.0 | -0.33 | -0.6 | 0.69 | 53.6 | no edge shown yet |
| consensus_gap+money_moving | both | 10-6 | 62.5 | 54.6 | 7.9 | -0.03 | -0.2 | 1.16 | 56.2 | keep collecting (16/30) |
| consensus_gap+sharp_gap | both | 15-16 | 48.4 | 56.6 | -8.2 | -7.39 | -23.8 | -0.36 | 35.5 | no edge shown yet |
| money_level+rlm_ratio | both | 1-6 | 14.3 | 47.4 | -33.1 | -5.09 | -72.7 | 0.64 | 71.4 | keep collecting (7/30) |
| follow_move+pin_move | both | 4-8 | 33.3 | 47.2 | -13.9 | -4.29 | -35.7 | 0.58 | 41.7 | keep collecting (12/30) |
| follow_move+money_delta | both | 3-2 | 60.0 | 39.1 | 20.9 | +3.56 | 71.2 | 2.74 | 100.0 | keep collecting (5/30) |
| money_delta+money_level | both | 1-3 | 25.0 | 40.4 | -15.4 | -2.09 | -52.3 | 1.68 | 100.0 | keep collecting (4/30) |
| money_delta+money_moving | both | 4-5 | 44.4 | 38.1 | 6.3 | +1.47 | 16.3 | 3.02 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | both | 3-2 | 60.0 | 39.1 | 20.9 | +3.56 | 71.2 | 2.74 | 100.0 | keep collecting (5/30) |
| money_delta+sharp_gap | both | 4-5 | 44.4 | 38.1 | 6.3 | +1.47 | 16.3 | 3.02 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| follow_move+pin_value | both | 5-5 | 50.0 | 49.1 | 0.9 | -0.41 | -4.1 | -0.3 | 30.0 | keep collecting (10/30) |
| consensus_gap+pin_move | both | 2-1 | 66.7 | 52.2 | 14.5 | +0.86 | 28.7 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+pin_value | both | 10-3 | 76.9 | 48.9 | 28.0 | +5.9 | 45.4 | -0.15 | 30.8 | keep collecting (13/30) |
| money_level+pin_move | both | 2-4 | 33.3 | 48.0 | -14.7 | -2.15 | -35.8 | 0.17 | 16.7 | keep collecting (6/30) |
| money_level+pin_value | both | 4-3 | 57.1 | 53.9 | 3.2 | +0.6 | 8.5 | 0.53 | 42.9 | keep collecting (7/30) |
| pin_move+pin_value | both | 4-8 | 33.3 | 49.4 | -16.0 | -4.28 | -35.7 | 0.67 | 41.7 | keep collecting (12/30) |
| money_moving+pin_value | both | 4-2 | 66.7 | 52.9 | 13.8 | +1.64 | 27.3 | 0.78 | 83.3 | keep collecting (6/30) |
| pin_value+sharp_gap | both | 2-4 | 33.3 | 54.7 | -21.4 | -2.22 | -37.0 | 0.95 | 66.7 | keep collecting (6/30) |
| consensus_gap+money_delta | both | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | both | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+rlm_ratio | both | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+sharp_gap | both | 0-3 | 0.0 | 46.3 | -46.3 | -3.0 | -100.0 | 1.0 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | both | 2-1 | 66.7 | 33.6 | 33.1 | +3.65 | 121.7 | 3.57 | 100.0 | keep collecting (3/30) |
| consensus_gap+rlm_quiet | both | 1-1 | 50.0 | 33.6 | 16.4 | +0.6 | 30.0 | 1.1 | 100.0 | keep collecting (2/30) |
| money_moving+pin_move | both | 1-1 | 50.0 | 47.3 | 2.7 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+pin_rlm | both | 0-1 | 0.0 | 33.6 | -33.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 0-1 | 0.0 | 33.6 | -33.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+rlm_quiet | both | 0-1 | 0.0 | 47.3 | -47.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 15-22 | 40.5 | 33.6 | 7.0 | +4.11 | 11.1 | 0.99 | 45.9 | no edge shown yet |
| rlm_quiet | total | 11-13 | 45.8 | 47.3 | -1.4 | -3.0 | -12.5 | 0.75 | 58.3 | keep collecting (24/30) |
| pin_move | moneyline | 1-2 | 33.3 | 55.5 | -22.1 | -1.48 | -49.5 | 0.77 | 33.3 | keep collecting (3/30) |
| pin_move | spread | 1-6 | 14.3 | 47.2 | -32.9 | -5.06 | -72.2 | 0.0 | 14.3 | keep collecting (7/30) |
| pin_move | total | 7-8 | 46.7 | 49.8 | -3.2 | -1.55 | -10.3 | 0.67 | 53.3 | keep collecting (15/30) |
| money_delta | moneyline | 2-4 | 33.3 | 33.6 | -0.2 | +0.65 | 10.8 | 2.7 | 100.0 | keep collecting (6/30) |
| money_delta | total | 2-1 | 66.7 | 47.3 | 19.4 | +0.82 | 27.3 | 3.67 | 100.0 | keep collecting (3/30) |
| pin_rlm | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | keep collecting (2/30) |
| follow_move | moneyline | 101-91 | 52.6 | 46.9 | 5.7 | -0.59 | -0.3 | -0.21 | 35.9 | no edge shown yet |
| follow_move | spread | 51-69 | 42.5 | 50.9 | -8.4 | -21.67 | -18.1 | 0.03 | 28.3 | DROP: below break-even |
| follow_move | total | 87-101 | 46.3 | 49.4 | -3.1 | -21.45 | -11.4 | 0.31 | 45.7 | DROP: below break-even |
| rlm_ratio | moneyline | 4-10 | 28.6 | 35.9 | -7.4 | -1.44 | -10.3 | -0.25 | 35.7 | keep collecting (14/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 56.5 | -56.5 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| rlm_ratio | total | 6-5 | 54.5 | 47.3 | 7.3 | +0.45 | 4.1 | 0.82 | 72.7 | keep collecting (11/30) |
| money_level | moneyline | 38-32 | 54.3 | 62.7 | -8.4 | -19.63 | -28.0 | -0.42 | 35.7 | no edge shown yet |
| money_level | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.06 | -2.9 | 2.0 | 50.0 | keep collecting (2/30) |
| money_level | total | 36-30 | 54.5 | 52.1 | 2.4 | +2.64 | 4.0 | -0.38 | 34.8 | no edge shown yet |
| sharp_gap | moneyline | 25-36 | 41.0 | 49.7 | -8.7 | -13.14 | -21.5 | -0.07 | 47.5 | DROP: below break-even |
| sharp_gap | spread | 0-2 | 0.0 | 56.5 | -56.5 | -2.0 | -100.0 | 3.0 | 100.0 | keep collecting (2/30) |
| sharp_gap | total | 33-27 | 55.0 | 50.1 | 4.9 | +2.92 | 4.9 | 0.38 | 41.7 | no edge shown yet |
| money_moving | moneyline | 20-21 | 48.8 | 48.0 | 0.8 | -3.06 | -7.5 | 0.73 | 58.5 | no edge shown yet |
| money_moving | spread | 0-2 | 0.0 | 56.5 | -56.5 | -2.0 | -100.0 | 3.0 | 100.0 | keep collecting (2/30) |
| money_moving | total | 28-21 | 57.1 | 49.6 | 7.5 | +4.49 | 9.2 | 0.18 | 38.8 | no edge shown yet |
| pin_value | moneyline | 0-1 | 0.0 | 66.4 | -66.4 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| pin_value | spread | 11-11 | 50.0 | 47.6 | 2.4 | -1.42 | -6.5 | 0.14 | 27.3 | keep collecting (22/30) |
| pin_value | total | 12-8 | 60.0 | 50.5 | 9.5 | +2.92 | 14.6 | 0.0 | 40.0 | keep collecting (20/30) |
| consensus_gap | moneyline | 69-63 | 52.3 | 56.7 | -4.4 | -21.76 | -16.5 | 0.45 | 49.2 | no edge shown yet |
| consensus_gap | spread | 31-19 | 62.0 | 47.7 | 14.3 | +7.92 | 15.8 | 0.28 | 36.0 | no edge shown yet |
| consensus_gap | total | 41-47 | 46.6 | 49.9 | -3.3 | -9.99 | -11.4 | 0.8 | 56.8 | no edge shown yet |
| consensus_gap+money_level | moneyline | 20-15 | 57.1 | 63.6 | -6.5 | -7.04 | -20.1 | -0.47 | 34.3 | no edge shown yet |
| follow_move+rlm_quiet | moneyline | 15-22 | 40.5 | 33.6 | 7.0 | +4.11 | 11.1 | 0.99 | 45.9 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 4-10 | 28.6 | 35.9 | -7.4 | -1.44 | -10.3 | -0.25 | 35.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 9-13 | 40.9 | 45.5 | -4.6 | -3.66 | -16.6 | 0.47 | 36.4 | keep collecting (22/30) |
| rlm_quiet+rlm_ratio | moneyline | 4-7 | 36.4 | 33.6 | 2.8 | +1.56 | 14.2 | 0.09 | 36.4 | keep collecting (11/30) |
| rlm_quiet+sharp_gap | moneyline | 4-8 | 33.3 | 33.6 | -0.2 | +0.56 | 4.7 | 0.53 | 41.7 | keep collecting (12/30) |
| rlm_ratio+sharp_gap | moneyline | 4-10 | 28.6 | 35.9 | -7.4 | -1.44 | -10.3 | -0.25 | 35.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 12-8 | 60.0 | 61.5 | -1.5 | -1.62 | -8.1 | 0.49 | 45.0 | keep collecting (20/30) |
| consensus_gap+money_moving | moneyline | 7-4 | 63.6 | 57.5 | 6.2 | -0.8 | -7.3 | 1.5 | 54.5 | keep collecting (11/30) |
| consensus_gap+sharp_gap | moneyline | 12-10 | 54.5 | 59.0 | -4.4 | -4.08 | -18.5 | -0.47 | 36.4 | keep collecting (22/30) |
| money_level+money_moving | moneyline | 8-8 | 50.0 | 60.3 | -10.3 | -4.74 | -29.6 | 1.11 | 56.2 | keep collecting (16/30) |
| money_level+sharp_gap | moneyline | 17-21 | 44.7 | 59.5 | -14.8 | -14.42 | -38.0 | -0.48 | 39.5 | no edge shown yet |
| money_moving+sharp_gap | moneyline | 8-16 | 33.3 | 43.2 | -9.8 | -4.6 | -19.2 | 1.08 | 70.8 | keep collecting (24/30) |
| follow_move+money_level | moneyline | 14-8 | 63.6 | 63.4 | 0.2 | -5.91 | -26.9 | -0.03 | 22.7 | keep collecting (22/30) |
| follow_move+money_moving | moneyline | 10-8 | 55.6 | 46.4 | 9.2 | +2.91 | 16.2 | 0.46 | 38.9 | keep collecting (18/30) |
| money_moving+rlm_quiet | moneyline | 5-6 | 45.5 | 33.6 | 11.9 | +3.35 | 30.5 | 1.3 | 54.5 | keep collecting (11/30) |
| money_moving+rlm_ratio | moneyline | 3-4 | 42.9 | 33.6 | 9.3 | +2.41 | 34.4 | 1.37 | 57.1 | keep collecting (7/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 66.4 | -66.4 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 66.4 | -66.4 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 66.4 | -66.4 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_rlm | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | moneyline | 0-3 | 0.0 | 44.5 | -44.5 | -3.0 | -100.0 | -1.5 | 33.3 | keep collecting (3/30) |
| pin_rlm+rlm_ratio | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+money_moving | moneyline | 2-4 | 33.3 | 33.6 | -0.2 | +0.65 | 10.8 | 2.7 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-4 | 33.3 | 33.6 | -0.2 | +0.65 | 10.8 | 2.7 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_level | moneyline | 0-2 | 0.0 | 33.6 | -33.6 | -2.0 | -100.0 | 1.85 | 100.0 | keep collecting (2/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 33.6 | 33.1 | +3.65 | 121.7 | 3.57 | 100.0 | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 2-1 | 66.7 | 33.6 | 33.1 | +3.65 | 121.7 | 3.57 | 100.0 | keep collecting (3/30) |
| money_delta+rlm_ratio | moneyline | 2-1 | 66.7 | 33.6 | 33.1 | +3.65 | 121.7 | 3.57 | 100.0 | keep collecting (3/30) |
| consensus_gap+rlm_quiet | moneyline | 1-1 | 50.0 | 33.6 | 16.4 | +0.6 | 30.0 | 1.1 | 100.0 | keep collecting (2/30) |
| follow_move+pin_move | moneyline | 0-1 | 0.0 | 33.6 | -33.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_move | moneyline | 0-1 | 0.0 | 33.6 | -33.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 0-1 | 0.0 | 33.6 | -33.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 0-1 | 0.0 | 33.6 | -33.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | moneyline | 0-1 | 0.0 | 33.6 | -33.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_level | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.06 | -2.9 | 2.0 | 50.0 | redundant -- identical record to money_level alone, not independent confirmation |
| follow_move+money_moving | spread | 0-1 | 0.0 | 56.5 | -56.5 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 56.5 | -56.5 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 0-1 | 0.0 | 56.5 | -56.5 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level+money_moving | spread | 0-1 | 0.0 | 56.5 | -56.5 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level+rlm_ratio | spread | 0-1 | 0.0 | 56.5 | -56.5 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 0-1 | 0.0 | 56.5 | -56.5 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 56.5 | -56.5 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+sharp_gap | spread | 0-2 | 0.0 | 56.5 | -56.5 | -2.0 | -100.0 | 3.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 56.5 | -56.5 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 1-2 | 33.3 | 47.8 | -14.5 | -1.09 | -36.4 | -0.33 | 0.0 | keep collecting (3/30) |
| pin_move+pin_value | spread | 0-4 | 0.0 | 46.8 | -46.8 | -4.0 | -100.0 | 0.5 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_value | spread | 4-1 | 80.0 | 46.1 | 33.9 | +2.41 | 48.1 | -0.4 | 0.0 | keep collecting (5/30) |
| follow_move+pin_move | spread | 1-2 | 33.3 | 47.8 | -14.5 | -1.06 | -35.2 | -0.33 | 0.0 | keep collecting (3/30) |
| consensus_gap+pin_move | spread | 0-1 | 0.0 | 56.5 | -56.5 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | spread | 0-1 | 0.0 | 43.5 | -43.5 | -1.0 | -100.0 | 4.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_move | spread | 1-0 | 100.0 | 43.5 | 56.5 | +0.94 | 94.3 | -1.0 | 0.0 | keep collecting (1/30) |
| money_moving+pin_value | spread | 0-1 | 0.0 | 56.5 | -56.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | spread | 0-1 | 0.0 | 56.5 | -56.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| follow_move+money_level | total | 11-10 | 52.4 | 51.2 | 1.2 | +0.04 | 0.2 | 0.43 | 52.4 | keep collecting (21/30) |
| follow_move+sharp_gap | total | 15-13 | 53.6 | 49.2 | 4.3 | +0.68 | 2.4 | 0.75 | 53.6 | keep collecting (28/30) |
| money_level+sharp_gap | total | 22-16 | 57.9 | 51.7 | 6.2 | +3.92 | 10.3 | -0.03 | 39.5 | no edge shown yet |
| follow_move+money_moving | total | 9-10 | 47.4 | 48.4 | -1.1 | -1.78 | -9.3 | 0.63 | 47.4 | keep collecting (19/30) |
| money_level+money_moving | total | 15-9 | 62.5 | 51.6 | 10.9 | +4.63 | 19.3 | -0.25 | 37.5 | keep collecting (24/30) |
| follow_move+rlm_quiet | total | 11-13 | 45.8 | 47.3 | -1.4 | -3.0 | -12.5 | 0.75 | 58.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 6-5 | 54.5 | 47.3 | 7.3 | +0.45 | 4.1 | 0.82 | 72.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 5-3 | 62.5 | 47.3 | 15.2 | +1.55 | 19.3 | 0.62 | 62.5 | keep collecting (8/30) |
| rlm_quiet+sharp_gap | total | 6-5 | 54.5 | 47.3 | 7.3 | +0.45 | 4.1 | 0.91 | 54.5 | keep collecting (11/30) |
| rlm_ratio+sharp_gap | total | 6-5 | 54.5 | 47.3 | 7.3 | +0.45 | 4.1 | 0.82 | 72.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | total | 4-4 | 50.0 | 47.3 | 2.7 | -0.36 | -4.5 | 0.38 | 37.5 | keep collecting (8/30) |
| money_moving+rlm_ratio | total | 4-1 | 80.0 | 47.3 | 32.7 | +2.64 | 52.7 | 1.2 | 80.0 | keep collecting (5/30) |
| money_moving+sharp_gap | total | 19-11 | 63.3 | 49.8 | 13.5 | +6.27 | 20.9 | 0.23 | 36.7 | no edge shown yet |
| follow_move+pin_move | total | 3-5 | 37.5 | 48.6 | -11.1 | -2.23 | -27.9 | 1.0 | 62.5 | keep collecting (8/30) |
| consensus_gap+follow_move | total | 6-12 | 33.3 | 48.8 | -15.5 | -6.55 | -36.4 | 1.33 | 72.2 | keep collecting (18/30) |
| consensus_gap+money_level | total | 5-4 | 55.6 | 52.1 | 3.4 | +0.51 | 5.6 | -0.33 | 22.2 | keep collecting (9/30) |
| consensus_gap+sharp_gap | total | 3-6 | 33.3 | 50.9 | -17.6 | -3.31 | -36.8 | -0.11 | 33.3 | keep collecting (9/30) |
| follow_move+money_delta | total | 1-1 | 50.0 | 47.3 | 2.7 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+money_level | total | 1-1 | 50.0 | 47.3 | 2.7 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+money_moving | total | 2-1 | 66.7 | 47.3 | 19.4 | +0.82 | 27.3 | 3.67 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | total | 1-1 | 50.0 | 47.3 | 2.7 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 2-1 | 66.7 | 47.3 | 19.4 | +0.82 | 27.3 | 3.67 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+rlm_ratio | total | 1-2 | 33.3 | 47.3 | -13.9 | -1.09 | -36.4 | 1.33 | 100.0 | keep collecting (3/30) |
| follow_move+pin_value | total | 4-3 | 57.1 | 49.6 | 7.5 | +0.68 | 9.7 | -0.29 | 42.9 | keep collecting (7/30) |
| consensus_gap+pin_move | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | 0.5 | 50.0 | keep collecting (2/30) |
| consensus_gap+pin_value | total | 6-2 | 75.0 | 50.7 | 24.3 | +3.5 | 43.7 | 0.0 | 50.0 | keep collecting (8/30) |
| money_level+pin_move | total | 1-3 | 25.0 | 52.7 | -27.7 | -2.09 | -52.3 | 0.5 | 25.0 | keep collecting (4/30) |
| money_level+pin_value | total | 4-2 | 66.7 | 51.8 | 14.9 | +1.6 | 26.6 | 0.33 | 33.3 | keep collecting (6/30) |
| pin_move+pin_value | total | 4-4 | 50.0 | 50.7 | -0.7 | -0.28 | -3.5 | 0.75 | 50.0 | keep collecting (8/30) |
| consensus_gap+money_delta | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_moving | total | 3-2 | 60.0 | 48.4 | 11.6 | +0.77 | 15.4 | 0.4 | 60.0 | keep collecting (5/30) |
| consensus_gap+rlm_ratio | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | total | 4-0 | 100.0 | 48.6 | 51.4 | +3.64 | 91.0 | 0.5 | 75.0 | keep collecting (4/30) |
| pin_value+rlm_ratio | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | total | 2-2 | 50.0 | 51.4 | -1.4 | -0.22 | -5.5 | 0.75 | 50.0 | keep collecting (4/30) |
| pin_move+sharp_gap | total | 0-2 | 0.0 | 52.7 | -52.7 | -2.0 | -100.0 | 1.5 | 50.0 | keep collecting (2/30) |
| money_moving+pin_move | total | 1-1 | 50.0 | 47.3 | 2.7 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+rlm_quiet | total | 0-1 | 0.0 | 47.3 | -47.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 117-181 | 39.3 | 43.1 | -3.8 | -37.8 | -12.7 |  |  | DROP: below break-even |
| pin_move | both | 208-225 | 48.0 | 49.5 | -1.5 | -24.13 | -5.6 |  |  | DROP: below break-even |
| money_delta | both | 109-135 | 44.7 | 44.2 | 0.5 | -16.81 | -6.9 |  |  | DROP: below break-even |
| pin_rlm | both | 43-64 | 40.2 | 42.4 | -2.2 | -16.42 | -15.3 |  |  | DROP: below break-even |
| follow_move | both | 341-375 | 47.6 | 49.2 | -1.6 | -62.72 | -8.8 |  |  | DROP: below break-even |
| rlm_ratio | both | 75-121 | 38.3 | 42.7 | -4.5 | -36.99 | -18.9 |  |  | DROP: below break-even |
| money_level | both | 436-340 | 56.2 | 54.7 | 1.5 | -31.65 | -4.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 335-395 | 45.9 | 48.5 | -2.6 | -86.9 | -11.9 |  |  | DROP: below break-even |
| money_moving | both | 348-386 | 47.4 | 48.9 | -1.5 | -71.39 | -9.7 |  |  | DROP: below break-even |
| pin_value | both | 156-158 | 49.7 | 49.6 | 0.0 | -3.38 | -1.1 |  |  | no edge shown yet |
| consensus_gap | both | 141-112 | 55.7 | 52.8 | 2.9 | +2.38 | 0.9 |  |  | no edge shown yet |
| follow_move+pin_move | both | 143-179 | 44.4 | 49.1 | -4.7 | -44.62 | -13.9 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 82-104 | 44.1 | 42.9 | 1.1 | -11.38 | -6.1 |  |  | DROP: below break-even |
| money_delta+sharp_gap | both | 82-103 | 44.3 | 42.9 | 1.4 | -10.38 | -5.6 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 326-374 | 46.6 | 48.6 | -2.0 | -71.79 | -10.3 |  |  | DROP: below break-even |
| consensus_gap+money_level | both | 93-58 | 61.6 | 58.3 | 3.3 | -1.16 | -0.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+rlm_quiet | both | 117-181 | 39.3 | 43.1 | -3.8 | -37.8 | -12.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | both | 54-82 | 39.7 | 44.1 | -4.4 | -19.34 | -14.2 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 40-37 | 51.9 | 51.4 | 0.6 | -6.0 | -7.8 |  |  | no edge shown yet |
| follow_move+money_level | both | 164-134 | 55.0 | 54.9 | 0.2 | -19.49 | -6.5 |  |  | no edge shown yet |
| money_level+money_moving | both | 236-216 | 52.2 | 52.5 | -0.3 | -29.61 | -6.6 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 224-217 | 50.8 | 52.3 | -1.5 | -36.57 | -8.3 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 49-58 | 45.8 | 51.0 | -5.2 | -13.08 | -12.2 |  |  | no edge shown yet |
| consensus_gap+pin_move | both | 39-24 | 61.9 | 50.9 | 11.0 | +15.55 | 24.7 |  |  | PROMOTE: beats break-even and its own base rate |
| consensus_gap+pin_value | both | 45-41 | 52.3 | 49.3 | 3.0 | +2.95 | 3.4 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | both | 49-62 | 44.1 | 50.5 | -6.4 | -16.94 | -15.3 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 178-208 | 46.1 | 48.4 | -2.3 | -46.17 | -12.0 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 51-50 | 50.5 | 50.1 | 0.4 | +5.39 | 5.3 |  |  | no edge shown yet |
| follow_move+sharp_gap | both | 174-211 | 45.2 | 48.2 | -3.0 | -48.88 | -12.7 |  |  | DROP: below break-even |
| money_level+pin_move | both | 94-89 | 51.4 | 53.3 | -2.0 | -15.0 | -8.2 |  |  | no edge shown yet |
| money_level+pin_value | both | 69-74 | 48.3 | 50.5 | -2.3 | -13.57 | -9.5 |  |  | no edge shown yet |
| money_moving+pin_move | both | 101-112 | 47.4 | 48.6 | -1.2 | -18.07 | -8.5 |  |  | no edge shown yet |
| money_moving+pin_value | both | 60-75 | 44.4 | 49.8 | -5.3 | -18.23 | -13.5 |  |  | DROP: below break-even |
| pin_move+pin_value | both | 63-69 | 47.7 | 51.1 | -3.3 | -12.67 | -9.6 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 96-118 | 44.9 | 48.2 | -3.3 | -27.19 | -12.7 |  |  | DROP: below break-even |
| pin_value+sharp_gap | both | 59-79 | 42.8 | 50.0 | -7.2 | -23.14 | -16.8 |  |  | DROP: below break-even |
| follow_move+money_delta | both | 58-87 | 40.0 | 44.1 | -4.1 | -25.52 | -17.6 |  |  | DROP: below break-even |
| money_delta+pin_move | both | 33-43 | 43.4 | 44.7 | -1.3 | -11.15 | -14.7 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 33-59 | 35.9 | 42.0 | -6.2 | -20.45 | -22.2 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | both | 75-121 | 38.3 | 42.7 | -4.5 | -36.99 | -18.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | both | 54-96 | 36.0 | 42.2 | -6.2 | -31.81 | -21.2 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 73-115 | 38.8 | 42.9 | -4.1 | -33.62 | -17.9 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 39-86 | 31.2 | 40.8 | -9.6 | -36.2 | -29.0 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | both | 54-98 | 35.5 | 42.1 | -6.6 | -33.72 | -22.2 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 75-121 | 38.3 | 42.7 | -4.5 | -36.99 | -18.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | both | 30-28 | 51.7 | 47.1 | 4.6 | +2.66 | 4.6 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 10-17 | 37.0 | 40.5 | -3.5 | -5.81 | -21.5 |  |  | keep collecting (27/30) |
| consensus_gap+rlm_ratio | both | 10-12 | 45.5 | 41.3 | 4.1 | -1.01 | -4.6 |  |  | keep collecting (22/30) |
| money_delta+rlm_ratio | both | 38-65 | 36.9 | 42.1 | -5.2 | -22.47 | -21.8 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 7-7 | 50.0 | 44.2 | 5.8 | +1.58 | 11.3 |  |  | keep collecting (14/30) |
| money_level+pin_rlm | both | 13-16 | 44.8 | 46.6 | -1.7 | -3.66 | -12.6 |  |  | keep collecting (29/30) |
| money_moving+pin_rlm | both | 43-58 | 42.6 | 42.8 | -0.3 | -10.42 | -10.3 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 43-64 | 40.2 | 42.4 | -2.2 | -16.42 | -15.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | both | 27-27 | 50.0 | 46.8 | 3.2 | -1.83 | -3.4 |  |  | no edge shown yet |
| consensus_gap+money_delta | both | 16-10 | 61.5 | 43.1 | 18.4 | +9.65 | 37.1 |  |  | keep collecting (26/30) |
| follow_move+pin_rlm | both | 36-55 | 39.6 | 41.9 | -2.4 | -14.49 | -15.9 |  |  | DROP: below break-even |
| money_delta+pin_rlm | both | 23-34 | 40.4 | 42.4 | -2.1 | -10.81 | -19.0 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 40-55 | 42.1 | 43.2 | -1.1 | -11.5 | -12.1 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | both | 36-52 | 40.9 | 43.3 | -2.4 | -12.96 | -14.7 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 19-41 | 31.7 | 40.3 | -8.6 | -16.8 | -28.0 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | both | 36-55 | 39.6 | 41.9 | -2.4 | -14.49 | -15.9 |  |  | DROP: below break-even |
| money_delta+pin_value | both | 21-13 | 61.8 | 48.7 | 13.0 | +10.02 | 29.5 |  |  | no edge shown yet |
| pin_value+rlm_quiet | both | 14-18 | 43.8 | 48.1 | -4.3 | +4.87 | 15.2 |  |  | no edge shown yet |
| pin_value+rlm_ratio | both | 7-8 | 46.7 | 48.1 | -1.4 | -1.31 | -8.7 |  |  | keep collecting (15/30) |
| pin_rlm+pin_value | both | 8-10 | 44.4 | 49.7 | -5.2 | -2.33 | -12.9 |  |  | keep collecting (18/30) |
| rlm_quiet | moneyline | 44-81 | 35.2 | 34.1 | 1.1 | -5.84 | -4.7 |  |  | DROP: below break-even |
| rlm_quiet | spread | 23-29 | 44.2 | 54.2 | -10.0 | -7.41 | -14.2 |  |  | no edge shown yet |
| rlm_quiet | total | 50-71 | 41.3 | 47.6 | -6.3 | -24.56 | -20.3 |  |  | DROP: below break-even |
| pin_move | moneyline | 61-56 | 52.1 | 46.8 | 5.4 | +10.97 | 9.4 |  |  | no edge shown yet |
| pin_move | spread | 69-77 | 47.3 | 51.7 | -4.4 | -14.52 | -9.9 |  |  | no edge shown yet |
| pin_move | total | 78-92 | 45.9 | 49.6 | -3.7 | -20.58 | -12.1 |  |  | DROP: below break-even |
| money_delta | moneyline | 31-54 | 36.5 | 35.9 | 0.6 | -7.51 | -8.8 |  |  | DROP: below break-even |
| money_delta | spread | 22-22 | 50.0 | 51.2 | -1.2 | -1.87 | -4.3 |  |  | no edge shown yet |
| money_delta | total | 56-59 | 48.7 | 47.7 | 1.0 | -7.43 | -6.5 |  |  | no edge shown yet |
| pin_rlm | moneyline | 16-33 | 32.7 | 34.9 | -2.3 | -10.12 | -20.7 |  |  | DROP: below break-even |
| pin_rlm | spread | 5-4 | 55.6 | 52.2 | 3.4 | +0.51 | 5.7 |  |  | keep collecting (9/30) |
| pin_rlm | total | 22-27 | 44.9 | 48.2 | -3.3 | -6.81 | -13.9 |  |  | no edge shown yet |
| follow_move | moneyline | 121-130 | 48.2 | 47.6 | 0.6 | -19.41 | -7.7 |  |  | no edge shown yet |
| follow_move | spread | 95-104 | 47.7 | 51.1 | -3.4 | -16.94 | -8.5 |  |  | no edge shown yet |
| follow_move | total | 125-141 | 47.0 | 49.3 | -2.3 | -26.36 | -9.9 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 25-59 | 29.8 | 34.4 | -4.6 | -20.6 | -24.5 |  |  | DROP: below break-even |
| rlm_ratio | spread | 12-10 | 54.5 | 52.4 | 2.2 | +0.72 | 3.3 |  |  | keep collecting (22/30) |
| rlm_ratio | total | 38-52 | 42.2 | 48.2 | -6.0 | -17.11 | -19.0 |  |  | DROP: below break-even |
| money_level | moneyline | 174-98 | 64.0 | 63.0 | 0.9 | -25.33 | -9.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 109-103 | 51.4 | 48.3 | 3.1 | -5.34 | -2.5 |  |  | no edge shown yet |
| money_level | total | 153-139 | 52.4 | 51.6 | 0.8 | -0.98 | -0.3 |  |  | no edge shown yet |
| sharp_gap | moneyline | 102-142 | 41.8 | 46.0 | -4.2 | -44.81 | -18.4 |  |  | DROP: below break-even |
| sharp_gap | spread | 107-106 | 50.2 | 49.4 | 0.9 | -9.79 | -4.6 |  |  | no edge shown yet |
| sharp_gap | total | 126-147 | 46.2 | 50.1 | -4.0 | -32.29 | -11.8 |  |  | DROP: below break-even |
| money_moving | moneyline | 111-131 | 45.9 | 47.0 | -1.1 | -30.91 | -12.8 |  |  | DROP: below break-even |
| money_moving | spread | 107-106 | 50.2 | 49.4 | 0.9 | -9.79 | -4.6 |  |  | no edge shown yet |
| money_moving | total | 130-149 | 46.6 | 50.1 | -3.5 | -30.69 | -11.0 |  |  | DROP: below break-even |
| pin_value | moneyline | 8-14 | 36.4 | 44.0 | -7.7 | +9.75 | 44.3 |  |  | keep collecting (22/30) |
| pin_value | spread | 74-66 | 52.9 | 49.6 | 3.2 | -1.82 | -1.3 |  |  | no edge shown yet |
| pin_value | total | 74-78 | 48.7 | 50.5 | -1.8 | -11.31 | -7.4 |  |  | no edge shown yet |
| consensus_gap | moneyline | 74-60 | 55.2 | 55.1 | 0.1 | -4.65 | -3.5 |  |  | no edge shown yet |
| consensus_gap | spread | 29-21 | 58.0 | 49.0 | 9.0 | +4.16 | 8.3 |  |  | no edge shown yet |
| consensus_gap | total | 38-31 | 55.1 | 51.1 | 4.0 | +2.86 | 4.2 |  |  | no edge shown yet |
| consensus_gap+money_level | moneyline | 57-28 | 67.1 | 64.1 | 3.0 | -2.72 | -3.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+pin_move | moneyline | 45-50 | 47.4 | 46.4 | 1.0 | -5.38 | -5.7 |  |  | no edge shown yet |
| follow_move+rlm_quiet | moneyline | 44-81 | 35.2 | 34.1 | 1.1 | -5.84 | -4.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | moneyline | 21-31 | 40.4 | 34.2 | 6.2 | +0.83 | 1.6 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 22-20 | 52.4 | 52.3 | 0.0 | -5.1 | -12.1 |  |  | no edge shown yet |
| follow_move+money_level | moneyline | 67-41 | 62.0 | 62.5 | -0.4 | -14.57 | -13.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 97-126 | 43.5 | 46.1 | -2.6 | -31.03 | -13.9 |  |  | DROP: below break-even |
| follow_move+money_moving | moneyline | 61-76 | 44.5 | 45.6 | -1.0 | -20.72 | -15.1 |  |  | DROP: below break-even |
| follow_move+sharp_gap | moneyline | 56-79 | 41.5 | 44.8 | -3.3 | -24.34 | -18.0 |  |  | DROP: below break-even |
| money_level+money_moving | moneyline | 72-51 | 58.5 | 59.5 | -0.9 | -12.18 | -9.9 |  |  | no edge shown yet |
| money_level+sharp_gap | moneyline | 64-54 | 54.2 | 58.9 | -4.7 | -17.58 | -14.9 |  |  | no edge shown yet |
| follow_move+rlm_ratio | moneyline | 25-59 | 29.8 | 34.4 | -4.6 | -20.6 | -24.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | moneyline | 21-47 | 30.9 | 33.6 | -2.7 | -13.28 | -19.5 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 24-55 | 30.4 | 34.4 | -4.0 | -18.32 | -23.2 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | moneyline | 18-46 | 28.1 | 33.6 | -5.5 | -15.52 | -24.2 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 21-48 | 30.4 | 33.6 | -3.1 | -14.14 | -20.5 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 25-59 | 29.8 | 34.4 | -4.6 | -20.6 | -24.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 23-30 | 43.4 | 51.5 | -8.2 | -8.11 | -15.3 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | moneyline | 3-12 | 20.0 | 33.6 | -13.6 | -7.22 | -48.1 |  |  | keep collecting (15/30) |
| consensus_gap+rlm_ratio | moneyline | 3-8 | 27.3 | 33.6 | -6.3 | -3.22 | -29.3 |  |  | keep collecting (11/30) |
| consensus_gap+sharp_gap | moneyline | 23-33 | 41.1 | 50.6 | -9.5 | -10.97 | -19.6 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | moneyline | 4-3 | 57.1 | 38.3 | 18.9 | +2.88 | 41.1 |  |  | keep collecting (7/30) |
| money_level+pin_rlm | moneyline | 3-5 | 37.5 | 41.8 | -4.3 | -1.8 | -22.5 |  |  | keep collecting (8/30) |
| money_moving+pin_rlm | moneyline | 16-28 | 36.4 | 35.1 | 1.3 | -5.12 | -11.6 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 16-33 | 32.7 | 34.9 | -2.3 | -10.12 | -20.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 4-7 | 36.4 | 42.5 | -6.2 | +0.84 | 7.7 |  |  | keep collecting (11/30) |
| money_level+rlm_ratio | moneyline | 4-10 | 28.6 | 38.3 | -9.7 | -5.66 | -40.5 |  |  | keep collecting (14/30) |
| consensus_gap+pin_move | moneyline | 22-6 | 78.6 | 51.2 | 27.4 | +18.54 | 66.2 |  |  | keep collecting (28/30) |
| money_level+pin_move | moneyline | 28-17 | 62.2 | 62.0 | 0.2 | -2.29 | -5.1 |  |  | no edge shown yet |
| consensus_gap+money_delta | moneyline | 6-7 | 46.2 | 36.1 | 10.1 | +3.67 | 28.2 |  |  | keep collecting (13/30) |
| follow_move+money_delta | moneyline | 17-37 | 31.5 | 36.6 | -5.1 | -13.09 | -24.2 |  |  | DROP: below break-even |
| follow_move+pin_rlm | moneyline | 13-28 | 31.7 | 34.4 | -2.7 | -8.58 | -20.9 |  |  | DROP: below break-even |
| money_delta+money_moving | moneyline | 28-50 | 35.9 | 35.3 | 0.6 | -6.85 | -8.8 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 9-13 | 40.9 | 35.1 | 5.8 | -3.14 | -14.3 |  |  | keep collecting (22/30) |
| money_delta+pin_rlm | moneyline | 9-17 | 34.6 | 34.8 | -0.2 | -6.72 | -25.8 |  |  | keep collecting (26/30) |
| money_delta+rlm_quiet | moneyline | 11-29 | 27.5 | 33.6 | -6.1 | -10.89 | -27.2 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | moneyline | 12-35 | 25.5 | 35.0 | -9.4 | -16.27 | -34.6 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 28-50 | 35.9 | 35.3 | 0.6 | -6.85 | -8.8 |  |  | DROP: below break-even |
| money_moving+pin_move | moneyline | 24-26 | 48.0 | 43.4 | 4.6 | -1.65 | -3.3 |  |  | no edge shown yet |
| pin_move+pin_rlm | moneyline | 13-24 | 35.1 | 34.5 | 0.7 | -5.2 | -14.1 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 10-23 | 30.3 | 34.6 | -4.3 | -7.66 | -23.2 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 22-31 | 41.5 | 42.3 | -0.7 | -7.04 | -13.3 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 10-23 | 30.3 | 33.6 | -3.3 | -7.08 | -21.5 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 13-28 | 31.7 | 34.4 | -2.7 | -8.58 | -20.9 |  |  | DROP: below break-even |
| follow_move+pin_value | moneyline | 3-3 | 50.0 | 50.0 | 0.0 | +9.55 | 159.1 |  |  | keep collecting (6/30) |
| pin_value+rlm_quiet | moneyline | 2-1 | 66.7 | 33.6 | 33.1 | +10.98 | 366.0 |  |  | keep collecting (3/30) |
| money_delta+money_level | moneyline | 9-5 | 64.3 | 43.0 | 21.3 | +6.57 | 47.0 |  |  | keep collecting (14/30) |
| money_level+pin_value | moneyline | 1-6 | 14.3 | 61.7 | -47.4 | -5.43 | -77.6 |  |  | keep collecting (7/30) |
| pin_move+pin_value | moneyline | 3-4 | 42.9 | 52.3 | -9.5 | -0.97 | -13.9 |  |  | keep collecting (7/30) |
| money_delta+pin_value | moneyline | 2-0 | 100.0 | 33.6 | 66.4 | +5.88 | 294.0 |  |  | keep collecting (2/30) |
| money_moving+pin_value | moneyline | 3-4 | 42.9 | 43.0 | -0.1 | +2.45 | 35.0 |  |  | keep collecting (7/30) |
| pin_value+sharp_gap | moneyline | 3-6 | 33.3 | 48.2 | -14.8 | +0.45 | 5.0 |  |  | keep collecting (9/30) |
| pin_rlm+pin_value | moneyline | 1-0 | 100.0 | 33.6 | 66.4 | +1.38 | 138.0 |  |  | keep collecting (1/30) |
| pin_value+rlm_ratio | moneyline | 1-0 | 100.0 | 33.6 | 66.4 | +1.38 | 138.0 |  |  | keep collecting (1/30) |
| follow_move+pin_move | spread | 41-55 | 42.7 | 51.5 | -8.8 | -17.6 | -18.3 |  |  | DROP: below break-even |
| money_moving+sharp_gap | spread | 107-106 | 50.2 | 49.4 | 0.9 | -9.79 | -4.6 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 23-29 | 44.2 | 54.2 | -10.0 | -7.41 | -14.2 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | spread | 81-78 | 50.9 | 48.4 | 2.5 | -5.48 | -3.4 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 81-78 | 50.9 | 48.4 | 2.5 | -5.48 | -3.4 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 12-19 | 38.7 | 54.4 | -15.7 | -7.75 | -25.0 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | spread | 21-15 | 58.3 | 49.6 | 8.7 | +3.32 | 9.2 |  |  | no edge shown yet |
| follow_move+money_level | spread | 35-33 | 51.5 | 50.0 | 1.5 | -1.29 | -1.9 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 42-42 | 50.0 | 51.1 | -1.1 | -3.95 | -4.7 |  |  | no edge shown yet |
| follow_move+sharp_gap | spread | 42-42 | 50.0 | 51.1 | -1.1 | -3.95 | -4.7 |  |  | no edge shown yet |
| money_level+pin_move | spread | 25-29 | 46.3 | 49.8 | -3.5 | -6.8 | -12.6 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 32-34 | 48.5 | 50.8 | -2.3 | -5.45 | -8.3 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 32-34 | 48.5 | 50.8 | -2.3 | -5.45 | -8.3 |  |  | no edge shown yet |
| money_delta+money_level | spread | 9-7 | 56.2 | 48.4 | 7.9 | +1.02 | 6.4 |  |  | keep collecting (16/30) |
| money_delta+money_moving | spread | 15-15 | 50.0 | 50.0 | 0.0 | -1.48 | -4.9 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 15-15 | 50.0 | 50.0 | 0.0 | -1.48 | -4.9 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 10-12 | 45.5 | 47.6 | -2.2 | -3.4 | -15.5 |  |  | keep collecting (22/30) |
| consensus_gap+money_moving | spread | 8-9 | 47.1 | 49.6 | -2.6 | -2.08 | -12.2 |  |  | keep collecting (17/30) |
| consensus_gap+sharp_gap | spread | 8-9 | 47.1 | 49.6 | -2.6 | -2.08 | -12.2 |  |  | keep collecting (17/30) |
| money_level+pin_value | spread | 28-30 | 48.3 | 47.5 | 0.7 | -5.96 | -10.3 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 27-34 | 44.3 | 49.5 | -5.2 | -10.69 | -17.5 |  |  | no edge shown yet |
| pin_value+sharp_gap | spread | 27-34 | 44.3 | 49.5 | -5.2 | -10.69 | -17.5 |  |  | no edge shown yet |
| follow_move+money_delta | spread | 10-10 | 50.0 | 51.9 | -1.9 | -1.03 | -5.2 |  |  | keep collecting (20/30) |
| follow_move+rlm_ratio | spread | 12-10 | 54.5 | 52.4 | 2.2 | +0.72 | 3.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | spread | 3-4 | 42.9 | 50.9 | -8.1 | -1.4 | -20.0 |  |  | keep collecting (7/30) |
| money_moving+rlm_ratio | spread | 12-10 | 54.5 | 52.4 | 2.2 | +0.72 | 3.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 12-10 | 54.5 | 52.4 | 2.2 | +0.72 | 3.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 19-17 | 52.8 | 50.7 | 2.1 | -0.38 | -1.0 |  |  | no edge shown yet |
| pin_move+pin_value | spread | 32-29 | 52.5 | 52.0 | 0.4 | -1.01 | -1.7 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 9-10 | 47.4 | 51.0 | -3.7 | -2.14 | -11.3 |  |  | keep collecting (19/30) |
| consensus_gap+follow_move | spread | 6-5 | 54.5 | 50.6 | 4.0 | +0.32 | 2.9 |  |  | keep collecting (11/30) |
| consensus_gap+rlm_quiet | spread | 2-0 | 100.0 | 56.5 | 43.5 | +1.82 | 90.9 |  |  | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 3-3 | 50.0 | 56.5 | -6.5 | -0.33 | -5.6 |  |  | keep collecting (6/30) |
| money_delta+rlm_quiet | spread | 5-5 | 50.0 | 53.9 | -3.9 | -0.31 | -3.1 |  |  | keep collecting (10/30) |
| money_moving+rlm_quiet | spread | 8-9 | 47.1 | 54.9 | -7.9 | -1.62 | -9.5 |  |  | keep collecting (17/30) |
| rlm_quiet+rlm_ratio | spread | 1-4 | 20.0 | 56.5 | -36.5 | -3.13 | -62.6 |  |  | keep collecting (5/30) |
| rlm_quiet+sharp_gap | spread | 8-9 | 47.1 | 54.9 | -7.9 | -1.62 | -9.5 |  |  | keep collecting (17/30) |
| consensus_gap+money_delta | spread | 3-1 | 75.0 | 56.5 | 18.5 | +1.63 | 40.8 |  |  | keep collecting (4/30) |
| money_delta+pin_move | spread | 7-6 | 53.8 | 52.5 | 1.4 | +0.19 | 1.5 |  |  | keep collecting (13/30) |
| money_delta+pin_value | spread | 6-4 | 60.0 | 53.9 | 6.1 | +1.32 | 13.2 |  |  | keep collecting (10/30) |
| money_moving+pin_rlm | spread | 5-4 | 55.6 | 52.2 | 3.4 | +0.51 | 5.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | spread | 5-4 | 55.6 | 52.2 | 3.4 | +0.51 | 5.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | spread | 3-2 | 60.0 | 56.5 | 3.5 | +0.7 | 13.9 |  |  | keep collecting (5/30) |
| pin_rlm+sharp_gap | spread | 5-4 | 55.6 | 52.2 | 3.4 | +0.51 | 5.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+rlm_ratio | spread | 3-0 | 100.0 | 52.2 | 47.8 | +2.59 | 86.3 |  |  | keep collecting (3/30) |
| money_level+rlm_ratio | spread | 10-3 | 76.9 | 51.5 | 25.4 | +5.94 | 45.7 |  |  | keep collecting (13/30) |
| pin_move+rlm_ratio | spread | 5-3 | 62.5 | 50.0 | 12.5 | +1.42 | 17.8 |  |  | keep collecting (8/30) |
| pin_value+rlm_ratio | spread | 1-0 | 100.0 | 56.5 | 43.5 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| follow_move+pin_rlm | spread | 2-2 | 50.0 | 46.8 | 3.2 | -0.18 | -4.5 |  |  | keep collecting (4/30) |
| money_delta+pin_rlm | spread | 3-3 | 50.0 | 54.3 | -4.3 | -0.3 | -5.1 |  |  | keep collecting (6/30) |
| pin_rlm+rlm_quiet | spread | 0-1 | 0.0 | 56.5 | -56.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+rlm_ratio | spread | 2-2 | 50.0 | 46.8 | 3.2 | -0.18 | -4.5 |  |  | keep collecting (4/30) |
| money_level+pin_rlm | spread | 2-3 | 40.0 | 48.7 | -8.7 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| consensus_gap+pin_rlm | spread | 2-1 | 66.7 | 52.2 | 14.5 | +0.79 | 26.2 |  |  | keep collecting (3/30) |
| money_delta+money_moving | total | 39-39 | 50.0 | 47.9 | 2.1 | -3.05 | -3.9 |  |  | no edge shown yet |
| money_delta+sharp_gap | total | 39-38 | 50.6 | 47.9 | 2.7 | -2.05 | -2.7 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 122-142 | 46.2 | 50.1 | -3.9 | -30.96 | -11.7 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | total | 50-71 | 41.3 | 47.6 | -6.3 | -24.56 | -20.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+follow_move | total | 12-12 | 50.0 | 50.0 | 0.0 | -1.22 | -5.1 |  |  | keep collecting (24/30) |
| consensus_gap+money_level | total | 26-18 | 59.1 | 52.5 | 6.6 | +4.95 | 11.3 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 18-19 | 48.6 | 51.0 | -2.3 | -2.88 | -7.8 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 8-8 | 50.0 | 50.3 | -0.3 | -0.84 | -5.3 |  |  | keep collecting (16/30) |
| consensus_gap+pin_value | total | 20-19 | 51.3 | 50.9 | 0.4 | -1.21 | -3.1 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 18-20 | 47.4 | 50.9 | -3.5 | -3.88 | -10.2 |  |  | no edge shown yet |
| follow_move+money_level | total | 62-60 | 50.8 | 50.8 | -0.0 | -3.64 | -3.0 |  |  | no edge shown yet |
| follow_move+money_moving | total | 75-90 | 45.5 | 49.5 | -4.0 | -21.5 | -13.0 |  |  | DROP: below break-even |
| follow_move+pin_move | total | 57-74 | 43.5 | 49.4 | -5.9 | -21.64 | -16.5 |  |  | DROP: below break-even |
| follow_move+pin_value | total | 29-30 | 49.2 | 49.8 | -0.6 | -3.78 | -6.4 |  |  | no edge shown yet |
| follow_move+sharp_gap | total | 76-90 | 45.8 | 49.5 | -3.7 | -20.6 | -12.4 |  |  | DROP: below break-even |
| money_level+money_moving | total | 83-87 | 48.8 | 51.3 | -2.5 | -11.95 | -7.0 |  |  | no edge shown yet |
| money_level+pin_move | total | 41-43 | 48.8 | 51.0 | -2.2 | -5.91 | -7.0 |  |  | no edge shown yet |
| money_level+pin_value | total | 40-38 | 51.3 | 51.7 | -0.5 | -2.18 | -2.8 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 79-85 | 48.2 | 51.4 | -3.2 | -13.51 | -8.2 |  |  | no edge shown yet |
| money_moving+pin_move | total | 45-52 | 46.4 | 49.8 | -3.4 | -10.98 | -11.3 |  |  | no edge shown yet |
| money_moving+pin_value | total | 30-37 | 44.8 | 50.8 | -6.0 | -10.0 | -14.9 |  |  | no edge shown yet |
| pin_move+pin_value | total | 28-36 | 43.8 | 50.0 | -6.2 | -10.69 | -16.7 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 42-53 | 44.2 | 49.7 | -5.5 | -14.71 | -15.5 |  |  | DROP: below break-even |
| pin_value+sharp_gap | total | 29-39 | 42.6 | 50.7 | -8.1 | -12.91 | -19.0 |  |  | DROP: below break-even |
| follow_move+money_delta | total | 31-40 | 43.7 | 47.6 | -3.9 | -11.4 | -16.1 |  |  | no edge shown yet |
| money_delta+pin_move | total | 17-24 | 41.5 | 47.4 | -5.9 | -8.2 | -20.0 |  |  | no edge shown yet |
| money_delta+rlm_quiet | total | 17-25 | 40.5 | 47.3 | -6.8 | -9.25 | -22.0 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | total | 21-32 | 39.6 | 47.9 | -8.3 | -12.43 | -23.4 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | total | 38-52 | 42.2 | 48.2 | -6.0 | -17.11 | -19.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | total | 23-26 | 46.9 | 47.7 | -0.8 | -4.8 | -9.8 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 25-40 | 38.5 | 47.8 | -9.3 | -16.92 | -26.0 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | total | 37-50 | 42.5 | 48.2 | -5.7 | -16.02 | -18.4 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | total | 20-36 | 35.7 | 47.8 | -12.1 | -17.55 | -31.3 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | total | 25-41 | 37.9 | 47.8 | -9.9 | -17.96 | -27.2 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | total | 38-52 | 42.2 | 48.2 | -6.0 | -17.11 | -19.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | total | 7-2 | 77.8 | 47.3 | 30.5 | +4.35 | 48.3 |  |  | keep collecting (9/30) |
| consensus_gap+rlm_quiet | total | 5-5 | 50.0 | 47.8 | 2.2 | -0.41 | -4.1 |  |  | keep collecting (10/30) |
| consensus_gap+rlm_ratio | total | 4-4 | 50.0 | 48.0 | 2.0 | -0.38 | -4.7 |  |  | keep collecting (8/30) |
| money_delta+pin_value | total | 13-9 | 59.1 | 47.8 | 11.3 | +2.82 | 12.8 |  |  | keep collecting (22/30) |
| pin_value+rlm_quiet | total | 9-14 | 39.1 | 47.8 | -8.6 | -5.77 | -25.1 |  |  | keep collecting (23/30) |
| pin_value+rlm_ratio | total | 5-8 | 38.5 | 48.5 | -10.1 | -3.53 | -27.2 |  |  | keep collecting (13/30) |
| follow_move+pin_rlm | total | 21-25 | 45.7 | 48.2 | -2.6 | -5.72 | -12.4 |  |  | no edge shown yet |
| money_delta+money_level | total | 12-16 | 42.9 | 48.4 | -5.6 | -4.94 | -17.6 |  |  | keep collecting (28/30) |
| money_delta+pin_rlm | total | 11-14 | 44.0 | 47.5 | -3.5 | -3.79 | -15.1 |  |  | keep collecting (25/30) |
| money_level+pin_rlm | total | 8-8 | 50.0 | 48.3 | 1.7 | -0.68 | -4.3 |  |  | keep collecting (16/30) |
| money_level+rlm_ratio | total | 13-14 | 48.1 | 48.9 | -0.7 | -2.11 | -7.8 |  |  | keep collecting (27/30) |
| money_moving+pin_rlm | total | 22-26 | 45.8 | 48.2 | -2.4 | -5.81 | -12.1 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 22-27 | 44.9 | 48.2 | -3.3 | -6.81 | -13.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 21-26 | 44.7 | 48.3 | -3.6 | -6.72 | -14.3 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 21-25 | 45.7 | 48.2 | -2.6 | -5.72 | -12.4 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 22-27 | 44.9 | 48.2 | -3.3 | -6.81 | -13.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | total | 9-17 | 34.6 | 48.1 | -13.5 | -8.72 | -33.5 |  |  | keep collecting (26/30) |
| consensus_gap+pin_rlm | total | 1-3 | 25.0 | 48.6 | -23.6 | -2.09 | -52.3 |  |  | keep collecting (4/30) |
| pin_rlm+pin_value | total | 4-8 | 33.3 | 48.2 | -14.9 | -4.4 | -36.7 |  |  | keep collecting (12/30) |

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
| rlm_quiet | both | 56-71 | 44.1 | 37.0 | 7.1 | +11.7 | 9.2 | 0.52 | 47.2 | DROP: below break-even |
| pin_move | both | 14-25 | 35.9 | 49.6 | -13.7 | -13.19 | -33.8 | 0.39 | 43.6 | DROP: below break-even |
| money_delta | both | 14-12 | 53.8 | 40.1 | 13.8 | +5.9 | 22.7 | 0.9 | 53.8 | keep collecting (26/30) |
| pin_rlm | both | 1-4 | 20.0 | 37.3 | -17.3 | -3.07 | -61.5 | -0.3 | 60.0 | keep collecting (5/30) |
| follow_move | both | 713-663 | 51.8 | 50.8 | 1.0 | -88.18 | -6.4 | 0.14 | 40.5 | no edge shown yet |
| rlm_ratio | both | 39-33 | 54.2 | 39.7 | 14.5 | +18.55 | 25.8 | 0.41 | 52.8 | no edge shown yet |
| money_level | both | 244-172 | 58.7 | 58.3 | 0.3 | -28.37 | -6.8 | -0.2 | 38.0 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 201-185 | 52.1 | 48.9 | 3.2 | +6.87 | 1.8 | 0.26 | 44.0 | no edge shown yet |
| money_moving | both | 150-124 | 54.7 | 50.4 | 4.4 | +0.62 | 0.2 | 0.19 | 44.2 | no edge shown yet |
| pin_value | both | 73-69 | 51.4 | 48.8 | 2.6 | -4.11 | -2.9 | 0.1 | 36.6 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 52.1 | -32.1 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 360-419 | 46.2 | 49.6 | -3.4 | -85.29 | -10.9 | 0.44 | 46.5 | DROP: below break-even |
| consensus_gap+money_level | both | 57-47 | 54.8 | 62.9 | -8.1 | -16.24 | -15.6 | 0.0 | 41.3 | no edge shown yet |
| consensus_gap+money_moving | both | 27-29 | 48.2 | 49.6 | -1.4 | -6.45 | -11.5 | 0.51 | 46.4 | no edge shown yet |
| consensus_gap+pin_value | both | 30-31 | 49.2 | 47.2 | 2.0 | -4.8 | -7.9 | 0.27 | 44.3 | no edge shown yet |
| follow_move+rlm_quiet | both | 56-71 | 44.1 | 37.0 | 7.1 | +11.7 | 9.2 | 0.52 | 47.2 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 39-33 | 54.2 | 39.7 | 14.5 | +18.55 | 25.8 | 0.41 | 52.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 99-64 | 60.7 | 49.2 | 11.6 | +21.33 | 13.1 | 0.48 | 47.9 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 87-57 | 60.4 | 56.8 | 3.6 | -0.97 | -0.7 | -0.01 | 46.5 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 15-12 | 55.6 | 50.4 | 5.2 | +1.41 | 5.2 | 0.43 | 44.4 | keep collecting (27/30) |
| money_moving+pin_value | both | 13-8 | 61.9 | 50.7 | 11.2 | +3.52 | 16.7 | 0.41 | 47.6 | keep collecting (21/30) |
| rlm_quiet+rlm_ratio | both | 25-20 | 55.6 | 37.1 | 18.4 | +17.35 | 38.6 | 0.1 | 48.9 | no edge shown yet |
| rlm_quiet+sharp_gap | both | 28-26 | 51.9 | 37.6 | 14.2 | +14.08 | 26.1 | 0.25 | 48.1 | no edge shown yet |
| rlm_ratio+sharp_gap | both | 39-33 | 54.2 | 39.7 | 14.5 | +18.55 | 25.8 | 0.41 | 52.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 136-98 | 58.1 | 55.5 | 2.6 | -7.34 | -3.1 | 0.03 | 42.3 | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | both | 87-76 | 53.4 | 47.9 | 5.4 | +5.67 | 3.5 | 0.36 | 47.9 | no edge shown yet |
| money_delta+money_level | both | 4-5 | 44.4 | 43.1 | 1.3 | -0.63 | -7.0 | 1.39 | 77.8 | keep collecting (9/30) |
| money_delta+money_moving | both | 13-12 | 52.0 | 39.7 | 12.3 | +4.99 | 20.0 | 0.94 | 56.0 | keep collecting (25/30) |
| money_delta+pin_value | both | 4-1 | 80.0 | 49.9 | 30.1 | +2.52 | 50.4 | 0.2 | 40.0 | keep collecting (5/30) |
| money_delta+sharp_gap | both | 11-10 | 52.4 | 38.9 | 13.4 | +5.25 | 25.0 | 1.12 | 66.7 | keep collecting (21/30) |
| pin_value+sharp_gap | both | 15-12 | 55.6 | 50.0 | 5.6 | +1.44 | 5.3 | 0.07 | 40.7 | keep collecting (27/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 50.6 | -50.6 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 50-62 | 44.6 | 53.1 | -8.5 | -24.18 | -21.6 | 0.81 | 56.2 | DROP: below break-even |
| consensus_gap+rlm_quiet | both | 5-8 | 38.5 | 36.5 | 1.9 | -2.39 | -18.4 | 0.97 | 76.9 | keep collecting (13/30) |
| follow_move+pin_value | both | 25-23 | 52.1 | 48.9 | 3.2 | -1.0 | -2.1 | -0.15 | 29.2 | no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 43.0 | -26.3 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 41-61 | 40.2 | 49.5 | -9.3 | -17.69 | -17.3 | 0.5 | 45.1 | DROP: below break-even |
| follow_move+money_level | both | 117-63 | 65.0 | 59.0 | 6.0 | -4.69 | -2.6 | 0.07 | 42.2 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 12-13 | 48.0 | 43.6 | 4.4 | -0.66 | -2.6 | 1.06 | 64.0 | keep collecting (25/30) |
| pin_value+rlm_ratio | both | 3-2 | 60.0 | 45.5 | 14.5 | +0.73 | 14.5 | -1.16 | 40.0 | keep collecting (5/30) |
| follow_move+money_moving | both | 72-47 | 60.5 | 51.1 | 9.4 | +10.93 | 9.2 | 0.42 | 49.6 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 4-0 | 100.0 | 49.3 | 50.7 | +3.52 | 88.0 | 0.25 | 25.0 | keep collecting (4/30) |
| follow_move+money_delta | both | 8-5 | 61.5 | 39.8 | 21.8 | +7.51 | 57.8 | 1.08 | 61.5 | keep collecting (13/30) |
| money_delta+rlm_quiet | both | 4-3 | 57.1 | 34.3 | 22.8 | +5.18 | 74.0 | 0.33 | 42.9 | keep collecting (7/30) |
| money_moving+rlm_quiet | both | 20-20 | 50.0 | 37.5 | 12.5 | +7.85 | 19.6 | 0.59 | 45.0 | no edge shown yet |
| money_moving+rlm_ratio | both | 19-13 | 59.4 | 40.6 | 18.7 | +11.71 | 36.6 | 0.77 | 56.2 | no edge shown yet |
| consensus_gap+rlm_ratio | both | 5-4 | 55.6 | 40.3 | 15.3 | +1.0 | 11.1 | 0.72 | 66.7 | keep collecting (9/30) |
| pin_move+pin_value | both | 5-12 | 29.4 | 49.3 | -19.9 | -7.37 | -43.3 | 0.53 | 35.3 | keep collecting (17/30) |
| follow_move+pin_move | both | 9-11 | 45.0 | 49.1 | -4.1 | -3.39 | -16.9 | 0.52 | 50.0 | keep collecting (20/30) |
| consensus_gap+pin_move | both | 2-6 | 25.0 | 46.9 | -21.9 | -4.14 | -51.7 | 0.29 | 50.0 | keep collecting (8/30) |
| money_level+pin_move | both | 4-6 | 40.0 | 50.0 | -10.0 | -3.02 | -30.2 | 0.14 | 30.0 | keep collecting (10/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 28.9 | -28.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-3 | 25.0 | 39.4 | -14.4 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 28.9 | -28.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 28.9 | -28.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-3 | 25.0 | 39.4 | -14.4 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+sharp_gap | both | 1-4 | 20.0 | 37.3 | -17.3 | -3.07 | -61.5 | -0.3 | 60.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.4 | -51.4 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 49.4 | -49.4 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-4 | 33.3 | 46.8 | -13.4 | -2.87 | -47.8 | 0.47 | 33.3 | keep collecting (6/30) |
| money_level+pin_rlm | both | 1-2 | 33.3 | 43.0 | -9.6 | -1.07 | -35.8 | 0.67 | 66.7 | keep collecting (3/30) |
| pin_move+pin_rlm | both | 1-1 | 50.0 | 28.9 | 21.1 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| pin_move+rlm_ratio | both | 1-1 | 50.0 | 28.9 | 21.1 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | both | 5-3 | 62.5 | 36.6 | 25.9 | +6.9 | 86.2 | 2.04 | 87.5 | keep collecting (8/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 28.9 | -28.9 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_moving+pin_move | both | 1-1 | 50.0 | 49.4 | 0.6 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+rlm_quiet | both | 0-1 | 0.0 | 49.4 | -49.4 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 31-46 | 40.3 | 28.9 | 11.4 | +14.0 | 18.2 | 0.45 | 45.5 | DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.3 | 10.7 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 22-23 | 48.9 | 49.5 | -0.6 | -2.96 | -6.6 | 0.8 | 55.6 | no edge shown yet |
| pin_move | moneyline | 3-5 | 37.5 | 50.0 | -12.5 | -3.35 | -41.9 | 0.3 | 50.0 | keep collecting (8/30) |
| pin_move | spread | 2-10 | 16.7 | 48.9 | -32.2 | -8.15 | -67.9 | 0.17 | 25.0 | keep collecting (12/30) |
| pin_move | total | 9-10 | 47.4 | 50.0 | -2.6 | -1.69 | -8.9 | 0.58 | 52.6 | keep collecting (19/30) |
| money_delta | moneyline | 4-8 | 33.3 | 28.9 | 4.5 | +0.99 | 8.2 | 0.62 | 66.7 | keep collecting (12/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 9-3 | 75.0 | 49.6 | 25.4 | +5.08 | 42.3 | 1.25 | 41.7 | keep collecting (12/30) |
| pin_rlm | moneyline | 1-4 | 20.0 | 37.3 | -17.3 | -3.07 | -61.5 | -0.3 | 60.0 | keep collecting (5/30) |
| follow_move | moneyline | 296-217 | 57.7 | 52.4 | 5.3 | -24.68 | -4.8 | 0.04 | 42.3 | PROMOTE: beats break-even and its own base rate |
| follow_move | spread | 179-209 | 46.1 | 49.8 | -3.7 | -43.87 | -11.3 | 0.02 | 32.5 | DROP: below break-even |
| follow_move | total | 238-237 | 50.1 | 50.0 | 0.1 | -19.63 | -4.1 | 0.33 | 45.1 | no edge shown yet |
| rlm_ratio | moneyline | 17-20 | 45.9 | 30.0 | 15.9 | +11.27 | 30.4 | 0.18 | 51.4 | no edge shown yet |
| rlm_ratio | spread | 3-3 | 50.0 | 52.3 | -2.3 | -0.16 | -2.7 | 0.33 | 16.7 | keep collecting (6/30) |
| rlm_ratio | total | 19-10 | 65.5 | 49.5 | 16.0 | +7.44 | 25.7 | 0.72 | 62.1 | keep collecting (29/30) |
| money_level | moneyline | 134-71 | 65.4 | 66.8 | -1.4 | -27.13 | -13.2 | -0.31 | 41.5 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 18-18 | 50.0 | 48.9 | 1.1 | -1.75 | -4.8 | 0.94 | 50.0 | no edge shown yet |
| money_level | total | 92-83 | 52.6 | 50.3 | 2.2 | +0.51 | 0.3 | -0.31 | 31.4 | no edge shown yet |
| sharp_gap | moneyline | 86-97 | 47.0 | 47.8 | -0.8 | -9.55 | -5.2 | 0.19 | 49.2 | no edge shown yet |
| sharp_gap | spread | 20-16 | 55.6 | 49.8 | 5.7 | +2.0 | 5.6 | 0.78 | 41.7 | no edge shown yet |
| sharp_gap | total | 95-72 | 56.9 | 49.9 | 7.0 | +14.41 | 8.6 | 0.22 | 38.9 | no edge shown yet |
| money_moving | moneyline | 64-62 | 50.8 | 51.0 | -0.2 | -15.46 | -12.3 | 0.14 | 50.8 | no edge shown yet |
| money_moving | spread | 18-7 | 72.0 | 49.0 | 23.0 | +9.18 | 36.7 | 0.52 | 48.0 | keep collecting (25/30) |
| money_moving | total | 68-55 | 55.3 | 50.0 | 5.3 | +6.91 | 5.6 | 0.18 | 36.6 | no edge shown yet |
| pin_value | moneyline | 2-7 | 22.2 | 38.3 | -16.0 | -5.31 | -59.0 | 0.12 | 55.6 | keep collecting (9/30) |
| pin_value | spread | 36-31 | 53.7 | 49.0 | 4.7 | +0.57 | 0.8 | 0.21 | 34.3 | no edge shown yet |
| pin_value | total | 35-31 | 53.0 | 50.1 | 3.0 | +0.63 | 1.0 | -0.02 | 36.4 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 53.4 | -20.1 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 158-227 | 41.0 | 49.8 | -8.8 | -72.36 | -18.8 | 0.25 | 44.7 | DROP: below break-even |
| consensus_gap | spread | 95-80 | 54.3 | 48.7 | 5.6 | +2.84 | 1.6 | 0.33 | 38.9 | no edge shown yet |
| consensus_gap | total | 107-112 | 48.9 | 50.0 | -1.2 | -15.77 | -7.2 | 0.86 | 55.7 | no edge shown yet |
| money_level+sharp_gap | moneyline | 63-40 | 61.2 | 62.5 | -1.4 | -15.52 | -15.1 | -0.15 | 48.5 | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+follow_move | moneyline | 23-30 | 43.4 | 57.6 | -14.2 | -16.31 | -30.8 | 0.31 | 50.9 | no edge shown yet |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 34.1 | -9.1 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| consensus_gap+rlm_quiet | moneyline | 2-6 | 25.0 | 28.9 | -3.9 | -3.08 | -38.5 | 1.07 | 87.5 | keep collecting (8/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 43.0 | -9.6 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 31-46 | 40.3 | 28.9 | 11.4 | +14.0 | 18.2 | 0.45 | 45.5 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 38-21 | 64.4 | 66.8 | -2.4 | -9.64 | -16.3 | -0.19 | 52.5 | beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 28.9 | -28.9 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 27-46 | 37.0 | 49.7 | -12.7 | -15.11 | -20.7 | 0.5 | 46.6 | DROP: below break-even |
| follow_move+money_level | moneyline | 72-24 | 75.0 | 67.2 | 7.8 | -6.65 | -6.9 | -0.21 | 40.6 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 38-20 | 65.5 | 52.9 | 12.6 | +6.83 | 11.8 | 0.2 | 50.0 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 43-34 | 55.8 | 67.8 | -12.0 | -15.59 | -20.3 | -0.17 | 41.6 | no edge shown yet |
| follow_move+sharp_gap | moneyline | 45-30 | 60.0 | 48.6 | 11.4 | +6.15 | 8.2 | 0.31 | 49.3 | no edge shown yet |
| money_moving+sharp_gap | moneyline | 30-41 | 42.3 | 45.5 | -3.3 | -11.14 | -15.7 | 0.39 | 59.2 | DROP: below break-even |
| consensus_gap+money_moving | moneyline | 15-25 | 37.5 | 50.0 | -12.5 | -13.06 | -32.7 | 0.59 | 50.0 | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 17-20 | 45.9 | 30.0 | 15.9 | +11.27 | 30.4 | 0.18 | 51.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 13-14 | 48.1 | 28.9 | 19.3 | +12.4 | 45.9 | -0.1 | 44.4 | keep collecting (27/30) |
| rlm_quiet+sharp_gap | moneyline | 13-18 | 41.9 | 28.9 | 13.1 | +8.4 | 27.1 | -0.04 | 45.2 | no edge shown yet |
| rlm_ratio+sharp_gap | moneyline | 17-20 | 45.9 | 30.0 | 15.9 | +11.27 | 30.4 | 0.18 | 51.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 28.9 | -3.9 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 10-13 | 43.5 | 28.9 | 14.6 | +5.84 | 25.4 | 0.85 | 52.2 | keep collecting (23/30) |
| money_moving+rlm_ratio | moneyline | 7-7 | 50.0 | 28.9 | 21.1 | +6.63 | 47.4 | 0.82 | 57.1 | keep collecting (14/30) |
| money_delta+money_moving | moneyline | 4-8 | 33.3 | 28.9 | 4.5 | +0.99 | 8.2 | 0.62 | 66.7 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 4-7 | 36.4 | 28.9 | 7.5 | +1.99 | 18.1 | 0.68 | 72.7 | keep collecting (11/30) |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 43.0 | -43.0 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-2 | 50.0 | 50.0 | 0.0 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| money_level+pin_move | moneyline | 2-2 | 50.0 | 50.0 | 0.0 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 28.9 | -28.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-3 | 25.0 | 39.4 | -14.4 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 28.9 | -28.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 28.9 | -28.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-3 | 25.0 | 39.4 | -14.4 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+sharp_gap | moneyline | 1-4 | 20.0 | 37.3 | -17.3 | -3.07 | -61.5 | -0.3 | 60.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 28.9 | -28.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | -1.55 | 50.0 | keep collecting (2/30) |
| pin_move+sharp_gap | moneyline | 2-1 | 66.7 | 43.0 | 23.7 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+rlm_ratio | moneyline | 4-6 | 40.0 | 33.1 | 6.9 | -1.13 | -11.3 | 0.95 | 70.0 | keep collecting (10/30) |
| money_level+pin_rlm | moneyline | 1-2 | 33.3 | 43.0 | -9.6 | -1.07 | -35.8 | 0.67 | 66.7 | keep collecting (3/30) |
| pin_move+pin_rlm | moneyline | 1-1 | 50.0 | 28.9 | 21.1 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| pin_move+rlm_ratio | moneyline | 1-1 | 50.0 | 28.9 | 21.1 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| follow_move+money_delta | moneyline | 4-2 | 66.7 | 28.9 | 37.8 | +6.99 | 116.5 | 1.02 | 66.7 | keep collecting (6/30) |
| money_delta+rlm_quiet | moneyline | 3-2 | 60.0 | 28.9 | 31.1 | +5.35 | 107.0 | 0.46 | 60.0 | keep collecting (5/30) |
| money_delta+rlm_ratio | moneyline | 4-1 | 80.0 | 28.9 | 51.1 | +7.99 | 159.8 | 2.26 | 80.0 | keep collecting (5/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 28.9 | -28.9 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-2 | 33.3 | 28.9 | 4.5 | -0.36 | -12.0 | 2.5 | 100.0 | keep collecting (3/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 71.1 | -71.1 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 71.1 | -71.1 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 46.6 | -1.1 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 46.6 | 36.8 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 15-9 | 62.5 | 48.0 | 14.5 | +3.84 | 16.0 | 0.29 | 37.5 | keep collecting (24/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.3 | 10.7 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-3 | 50.0 | 52.3 | -2.3 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-7 | 58.8 | 48.6 | 10.2 | +2.09 | 12.3 | 0.88 | 41.2 | keep collecting (17/30) |
| money_level+money_moving | spread | 10-6 | 62.5 | 48.3 | 14.2 | +3.12 | 19.5 | 1.19 | 68.8 | keep collecting (16/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.5 | -5.7 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 4-3 | 57.1 | 49.5 | 7.6 | +0.41 | 5.8 | 0.57 | 57.1 | keep collecting (7/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 3-3 | 50.0 | 52.3 | -2.3 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 53.4 | -53.4 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 53.4 | -53.4 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-12 | 53.8 | 48.9 | 4.9 | +0.62 | 2.4 | 1.15 | 46.2 | keep collecting (26/30) |
| money_moving+sharp_gap | spread | 10-5 | 66.7 | 49.3 | 17.4 | +4.04 | 26.9 | 0.87 | 53.3 | keep collecting (15/30) |
| pin_value+sharp_gap | spread | 2-2 | 50.0 | 50.0 | 0.0 | -0.26 | -6.5 | 0.75 | 75.0 | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 9-12 | 42.9 | 47.6 | -4.7 | -4.2 | -20.0 | 1.0 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 46.6 | 15.9 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 12-10 | 54.5 | 48.1 | 6.4 | +0.98 | 4.5 | 0.82 | 45.5 | keep collecting (22/30) |
| follow_move+pin_value | spread | 13-9 | 59.1 | 48.4 | 10.6 | +2.36 | 10.7 | 0.18 | 27.3 | keep collecting (22/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 46.6 | 53.4 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 46.6 | 53.4 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 46.6 | 53.4 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-3 | 75.0 | 47.7 | 27.3 | +5.22 | 43.5 | 0.75 | 50.0 | keep collecting (12/30) |
| money_delta+rlm_quiet | spread | 1-0 | 100.0 | 46.6 | 53.4 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 2-0 | 100.0 | 46.6 | 53.4 | +1.74 | 87.1 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 2-2 | 50.0 | 53.4 | -3.4 | -0.07 | -1.7 | 1.25 | 25.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | spread | 2-1 | 66.7 | 51.1 | 15.5 | +0.86 | 28.7 | 1.0 | 33.3 | keep collecting (3/30) |
| pin_move+pin_value | spread | 1-7 | 12.5 | 48.3 | -35.8 | -6.09 | -76.1 | 0.38 | 25.0 | keep collecting (8/30) |
| consensus_gap+pin_move | spread | 0-3 | 0.0 | 48.9 | -48.9 | -3.0 | -100.0 | 0.33 | 33.3 | keep collecting (3/30) |
| follow_move+pin_move | spread | 2-4 | 33.3 | 47.7 | -14.4 | -2.15 | -35.8 | 0.0 | 16.7 | keep collecting (6/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 53.4 | -53.4 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_move | spread | 1-0 | 100.0 | 46.6 | 53.4 | +0.94 | 94.3 | -1.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 22-23 | 48.9 | 49.5 | -0.6 | -2.96 | -6.6 | 0.8 | 55.6 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 39-30 | 56.5 | 50.2 | 6.3 | +5.56 | 8.1 | -0.13 | 36.2 | no edge shown yet |
| money_level+sharp_gap | total | 59-46 | 56.2 | 50.2 | 6.0 | +7.56 | 7.2 | -0.07 | 35.2 | no edge shown yet |
| money_moving+sharp_gap | total | 47-30 | 61.0 | 49.9 | 11.1 | +12.77 | 16.6 | 0.25 | 36.4 | PROMOTE: beats break-even and its own base rate |
| book_lag+pin_move | total | 0-1 | 0.0 | 50.6 | -50.6 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 12-7 | 63.2 | 50.0 | 13.2 | +3.83 | 20.2 | 0.26 | 31.6 | keep collecting (19/30) |
| money_moving+pin_value | total | 9-4 | 69.2 | 49.8 | 19.5 | +4.11 | 31.6 | 0.23 | 38.5 | keep collecting (13/30) |
| pin_value+sharp_gap | total | 13-8 | 61.9 | 50.0 | 11.9 | +3.7 | 17.6 | 0.1 | 33.3 | keep collecting (21/30) |
| follow_move+money_level | total | 33-29 | 53.2 | 50.3 | 3.0 | +0.99 | 1.6 | 0.24 | 43.5 | no edge shown yet |
| follow_move+pin_value | total | 11-12 | 47.8 | 50.0 | -2.2 | -2.08 | -9.0 | -0.3 | 30.4 | keep collecting (23/30) |
| follow_move+rlm_ratio | total | 19-10 | 65.5 | 49.5 | 16.0 | +7.44 | 25.7 | 0.72 | 62.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 44-27 | 62.0 | 49.9 | 12.1 | +13.1 | 18.4 | 0.56 | 47.9 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 6-5 | 54.5 | 49.5 | 5.0 | +0.54 | 4.9 | 1.09 | 72.7 | keep collecting (11/30) |
| pin_value+rlm_ratio | total | 3-1 | 75.0 | 49.7 | 25.3 | +1.73 | 43.2 | -0.25 | 50.0 | keep collecting (4/30) |
| rlm_ratio+sharp_gap | total | 19-10 | 65.5 | 49.5 | 16.0 | +7.44 | 25.7 | 0.72 | 62.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 25-24 | 51.0 | 49.8 | 1.2 | -1.12 | -2.3 | 0.59 | 49.0 | no edge shown yet |
| consensus_gap+money_level | total | 9-7 | 56.2 | 50.4 | 5.9 | +1.03 | 6.5 | -0.38 | 18.8 | keep collecting (16/30) |
| consensus_gap+money_moving | total | 7-3 | 70.0 | 50.0 | 20.0 | +3.3 | 33.0 | 0.0 | 30.0 | keep collecting (10/30) |
| consensus_gap+pin_value | total | 13-16 | 44.8 | 50.1 | -5.3 | -4.34 | -14.9 | 0.34 | 48.3 | keep collecting (29/30) |
| consensus_gap+sharp_gap | total | 9-12 | 42.9 | 50.0 | -7.1 | -3.89 | -18.5 | -0.1 | 28.6 | keep collecting (21/30) |
| money_moving+rlm_ratio | total | 10-5 | 66.7 | 49.6 | 17.1 | +4.22 | 28.1 | 0.67 | 60.0 | keep collecting (15/30) |
| consensus_gap+follow_move | total | 18-20 | 47.4 | 49.9 | -2.5 | -3.67 | -9.7 | 1.39 | 68.4 | no edge shown yet |
| consensus_gap+money_delta | total | 3-0 | 100.0 | 50.2 | 49.8 | +2.69 | 89.6 | 0.33 | 33.3 | keep collecting (3/30) |
| follow_move+money_delta | total | 3-3 | 50.0 | 49.6 | 0.4 | -0.31 | -5.2 | 1.33 | 66.7 | keep collecting (6/30) |
| money_delta+money_moving | total | 8-3 | 72.7 | 49.6 | 23.1 | +4.17 | 37.9 | 1.36 | 45.5 | keep collecting (11/30) |
| money_delta+pin_value | total | 3-0 | 100.0 | 49.8 | 50.2 | +2.69 | 89.6 | 0.0 | 33.3 | keep collecting (3/30) |
| money_delta+sharp_gap | total | 7-2 | 77.8 | 49.7 | 28.1 | +4.26 | 47.4 | 1.67 | 55.6 | keep collecting (9/30) |
| money_moving+rlm_quiet | total | 8-7 | 53.3 | 49.5 | 3.9 | +0.27 | 1.8 | 0.4 | 40.0 | keep collecting (15/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 11-5 | 68.8 | 49.5 | 19.3 | +5.04 | 31.5 | 0.62 | 62.5 | keep collecting (16/30) |
| rlm_quiet+sharp_gap | total | 14-7 | 66.7 | 49.4 | 17.2 | +5.77 | 27.5 | 0.86 | 57.1 | keep collecting (21/30) |
| follow_move+pin_move | total | 5-5 | 50.0 | 49.6 | 0.4 | -0.37 | -3.7 | 1.0 | 70.0 | keep collecting (10/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 49.4 | -49.4 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 49.4 | -49.4 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 3-2 | 60.0 | 49.6 | 10.4 | +0.73 | 14.5 | 0.8 | 60.0 | keep collecting (5/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 49.4 | 0.6 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 4-1 | 80.0 | 49.4 | 30.6 | +2.68 | 53.6 | 0.4 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | total | 1-4 | 20.0 | 50.6 | -30.6 | -3.09 | -61.8 | 0.4 | 20.0 | keep collecting (5/30) |
| pin_move+pin_value | total | 4-5 | 44.4 | 50.2 | -5.8 | -1.28 | -14.2 | 0.67 | 44.4 | keep collecting (9/30) |
| pin_move+sharp_gap | total | 0-3 | 0.0 | 50.6 | -50.6 | -3.0 | -100.0 | 1.0 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 49.4 | -49.4 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 1-2 | 33.3 | 49.4 | -16.1 | -1.09 | -36.4 | 1.67 | 100.0 | keep collecting (3/30) |
| consensus_gap+pin_move | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | 0.5 | 50.0 | keep collecting (2/30) |
| money_moving+pin_move | total | 1-1 | 50.0 | 49.4 | 0.6 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+rlm_quiet | total | 0-1 | 0.0 | 49.4 | -49.4 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 299-437 | 40.6 | 42.2 | -1.5 | -71.72 | -9.7 |  |  | DROP: below break-even |
| pin_move | both | 704-725 | 49.3 | 49.7 | -0.4 | -57.62 | -4.0 |  |  | DROP: below break-even |
| money_delta | both | 425-557 | 43.3 | 44.3 | -1.0 | -73.98 | -7.5 |  |  | DROP: below break-even |
| pin_rlm | both | 183-225 | 44.9 | 42.3 | 2.6 | +10.86 | 2.7 |  |  | DROP: below break-even |
| follow_move | both | 1197-1138 | 51.3 | 50.8 | 0.4 | -152.32 | -6.5 |  |  | no edge shown yet |
| rlm_ratio | both | 275-346 | 44.3 | 43.7 | 0.6 | -35.84 | -5.8 |  |  | DROP: below break-even |
| money_level | both | 1518-1144 | 57.0 | 55.2 | 1.9 | -98.48 | -3.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 1180-1370 | 46.3 | 47.7 | -1.4 | -205.49 | -8.1 |  |  | DROP: below break-even |
| money_moving | both | 1194-1361 | 46.7 | 48.0 | -1.3 | -197.59 | -7.7 |  |  | DROP: below break-even |
| pin_value | both | 511-518 | 49.7 | 48.4 | 1.2 | +0.39 | 0.0 |  |  | DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 51.1 | 15.5 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 471-560 | 45.7 | 48.9 | -3.2 | -85.22 | -8.3 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 167-164 | 50.5 | 51.2 | -0.7 | -21.23 | -6.4 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 196-299 | 39.6 | 46.2 | -6.6 | -44.88 | -9.1 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 120-109 | 52.4 | 50.8 | 1.6 | +16.66 | 7.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 30-47 | 39.0 | 39.1 | -0.1 | +10.61 | 13.8 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 180-188 | 48.9 | 46.6 | 2.3 | +8.3 | 2.3 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | both | 35-55 | 38.9 | 40.4 | -1.5 | -2.67 | -3.0 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 195-307 | 38.8 | 45.7 | -6.8 | -49.73 | -9.9 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 635-694 | 47.8 | 48.9 | -1.1 | -112.49 | -8.5 |  |  | DROP: below break-even |
| follow_move+pin_move | both | 500-535 | 48.3 | 49.7 | -1.4 | -77.36 | -7.5 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 144-169 | 46.0 | 43.5 | 2.5 | -9.92 | -3.2 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 176-171 | 50.7 | 49.2 | 1.6 | -4.26 | -1.2 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 275-346 | 44.3 | 43.7 | 0.6 | -35.84 | -5.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 636-694 | 47.8 | 48.7 | -0.9 | -105.08 | -7.9 |  |  | DROP: below break-even |
| money_moving+pin_move | both | 400-443 | 47.4 | 48.5 | -1.0 | -46.05 | -5.5 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 177-215 | 45.2 | 42.4 | 2.8 | +14.9 | 3.8 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 217-261 | 45.4 | 47.8 | -2.4 | -33.35 | -7.0 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 265-333 | 44.3 | 43.8 | 0.5 | -33.39 | -5.6 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 1137-1311 | 46.4 | 47.8 | -1.3 | -182.01 | -7.4 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 169-189 | 47.2 | 43.9 | 3.3 | +9.99 | 2.8 |  |  | DROP: below break-even |
| pin_move+pin_value | both | 220-226 | 49.3 | 49.5 | -0.2 | -18.67 | -4.2 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 152-165 | 47.9 | 44.9 | 3.0 | -0.71 | -0.2 |  |  | DROP: below break-even |
| pin_move+sharp_gap | both | 402-450 | 47.2 | 48.3 | -1.1 | -49.93 | -5.9 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 48-52 | 48.0 | 46.6 | 1.4 | +9.26 | 9.3 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 144-169 | 46.0 | 43.5 | 2.5 | -9.92 | -3.2 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 183-225 | 44.9 | 42.3 | 2.6 | +10.86 | 2.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 45-41 | 52.3 | 48.5 | 3.8 | +0.43 | 0.5 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 218-266 | 45.0 | 47.9 | -2.9 | -37.46 | -7.7 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 275-346 | 44.3 | 43.7 | 0.6 | -35.84 | -5.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 209-263 | 44.3 | 45.3 | -1.1 | -47.99 | -10.2 |  |  | DROP: below break-even |
| money_level+money_moving | both | 832-747 | 52.7 | 52.3 | 0.4 | -75.92 | -4.8 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 811-739 | 52.3 | 52.1 | 0.3 | -75.42 | -4.9 |  |  | no edge shown yet |
| follow_move+money_level | both | 728-535 | 57.6 | 55.8 | 1.8 | -64.08 | -5.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 122-108 | 53.0 | 47.8 | 5.2 | +8.85 | 3.8 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 295-223 | 56.9 | 58.0 | -1.1 | -24.75 | -4.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_move | both | 387-358 | 51.9 | 53.0 | -1.1 | -43.76 | -5.9 |  |  | no edge shown yet |
| money_level+pin_value | both | 243-233 | 51.1 | 49.9 | 1.1 | -21.3 | -4.5 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 29-64 | 31.2 | 37.8 | -6.6 | -14.89 | -16.0 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | both | 299-437 | 40.6 | 42.2 | -1.5 | -71.72 | -9.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 152-247 | 38.1 | 41.7 | -3.6 | -54.44 | -13.6 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 308-434 | 41.5 | 42.7 | -1.2 | -59.55 | -8.0 |  |  | DROP: below break-even |
| consensus_gap+money_delta | both | 57-119 | 32.4 | 38.5 | -6.1 | -21.03 | -12.0 |  |  | DROP: below break-even |
| money_delta+money_level | both | 147-139 | 51.4 | 47.1 | 4.3 | +14.25 | 5.0 |  |  | no edge shown yet |
| money_delta+pin_value | both | 89-85 | 51.1 | 47.6 | 3.6 | +3.45 | 2.0 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 305-428 | 41.6 | 42.7 | -1.1 | -56.72 | -7.7 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 118-208 | 36.2 | 40.3 | -4.1 | -47.84 | -14.7 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | both | 144-242 | 37.3 | 41.6 | -4.3 | -55.45 | -14.4 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 82-146 | 36.0 | 42.3 | -6.3 | -51.24 | -22.5 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | both | 142-190 | 42.8 | 43.8 | -1.0 | -25.59 | -7.7 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 61-105 | 36.7 | 40.3 | -3.5 | -27.29 | -16.4 |  |  | DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 51.1 | 15.5 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 151-182 | 45.3 | 46.2 | -0.8 | -21.08 | -6.3 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 76-60 | 55.9 | 46.8 | 9.1 | +14.58 | 10.7 |  |  | no edge shown yet |
| money_delta+pin_rlm | both | 105-129 | 44.9 | 42.4 | 2.5 | +0.62 | 0.3 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | both | 148-181 | 45.0 | 43.9 | 1.1 | -22.57 | -6.9 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | both | 38-54 | 41.3 | 47.5 | -6.2 | -8.7 | -9.5 |  |  | DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 49.4 | 50.6 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 96-191 | 33.4 | 29.6 | 3.9 | -13.3 | -4.6 |  |  | DROP: below break-even |
| rlm_quiet | spread | 68-73 | 48.2 | 51.5 | -3.3 | -9.73 | -6.9 |  |  | no edge shown yet |
| rlm_quiet | total | 135-173 | 43.8 | 49.6 | -5.8 | -48.69 | -15.8 |  |  | DROP: below break-even |
| pin_move | moneyline | 164-159 | 50.8 | 48.1 | 2.7 | +15.97 | 4.9 |  |  | no edge shown yet |
| pin_move | spread | 263-285 | 48.0 | 50.4 | -2.4 | -45.67 | -8.3 |  |  | DROP: below break-even |
| pin_move | total | 277-281 | 49.6 | 49.9 | -0.2 | -27.92 | -5.0 |  |  | no edge shown yet |
| money_delta | moneyline | 80-219 | 26.8 | 30.7 | -3.9 | -51.44 | -17.2 |  |  | DROP: below break-even |
| money_delta | spread | 144-147 | 49.5 | 51.1 | -1.7 | -15.78 | -5.4 |  |  | no edge shown yet |
| money_delta | total | 201-191 | 51.3 | 49.6 | 1.7 | -6.76 | -1.7 |  |  | no edge shown yet |
| pin_rlm | moneyline | 54-107 | 33.5 | 30.4 | 3.1 | +10.85 | 6.7 |  |  | DROP: below break-even |
| pin_rlm | spread | 30-27 | 52.6 | 51.4 | 1.2 | +0.3 | 0.5 |  |  | no edge shown yet |
| pin_rlm | total | 99-91 | 52.1 | 49.6 | 2.5 | -0.29 | -0.2 |  |  | no edge shown yet |
| follow_move | moneyline | 434-335 | 56.4 | 52.9 | 3.5 | -45.26 | -5.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 342-365 | 48.4 | 49.7 | -1.3 | -53.69 | -7.6 |  |  | DROP: below break-even |
| follow_move | total | 421-438 | 49.0 | 49.9 | -0.9 | -53.36 | -6.2 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 62-139 | 30.8 | 31.0 | -0.1 | -23.38 | -11.6 |  |  | DROP: below break-even |
| rlm_ratio | spread | 53-53 | 50.0 | 50.5 | -0.5 | -5.04 | -4.8 |  |  | no edge shown yet |
| rlm_ratio | total | 160-154 | 51.0 | 49.6 | 1.3 | -7.42 | -2.4 |  |  | no edge shown yet |
| money_level | moneyline | 590-255 | 69.8 | 67.1 | 2.7 | -48.11 | -5.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 424-429 | 49.7 | 48.9 | 0.8 | -47.19 | -5.5 |  |  | DROP: below break-even |
| money_level | total | 504-460 | 52.3 | 50.2 | 2.1 | -3.18 | -0.3 |  |  | no edge shown yet |
| sharp_gap | moneyline | 303-468 | 39.3 | 43.2 | -3.9 | -98.96 | -12.8 |  |  | DROP: below break-even |
| sharp_gap | spread | 430-416 | 50.8 | 49.5 | 1.4 | -28.35 | -3.4 |  |  | no edge shown yet |
| sharp_gap | total | 447-486 | 47.9 | 49.9 | -2.0 | -78.18 | -8.4 |  |  | DROP: below break-even |
| money_moving | moneyline | 320-447 | 41.7 | 44.2 | -2.5 | -76.02 | -9.9 |  |  | DROP: below break-even |
| money_moving | spread | 427-419 | 50.5 | 49.4 | 1.1 | -34.22 | -4.0 |  |  | no edge shown yet |
| money_moving | total | 447-495 | 47.5 | 49.9 | -2.5 | -87.35 | -9.3 |  |  | DROP: below break-even |
| pin_value | moneyline | 26-68 | 27.7 | 34.7 | -7.0 | +20.62 | 21.9 |  |  | DROP: below break-even |
| pin_value | spread | 233-214 | 52.1 | 49.5 | 2.6 | -11.1 | -2.5 |  |  | no edge shown yet |
| pin_value | total | 252-236 | 51.6 | 50.1 | 1.5 | -9.14 | -1.9 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 53.4 | 46.6 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 214-332 | 39.2 | 48.1 | -8.9 | -81.98 | -15.0 |  |  | DROP: below break-even |
| consensus_gap | spread | 114-96 | 54.3 | 49.0 | 5.3 | +1.63 | 0.8 |  |  | no edge shown yet |
| consensus_gap | total | 143-132 | 52.0 | 50.3 | 1.7 | -4.87 | -1.8 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 217-134 | 61.8 | 62.0 | -0.2 | -18.88 | -5.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 200-135 | 59.7 | 61.4 | -1.7 | -23.9 | -7.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 284-428 | 39.9 | 43.2 | -3.3 | -72.42 | -10.2 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 74-87 | 46.0 | 53.0 | -7.1 | -25.52 | -15.9 |  |  | DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 10-48 | 17.2 | 30.3 | -13.1 | -15.86 | -27.3 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 96-191 | 33.4 | 29.6 | 3.9 | -13.3 | -4.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 152-93 | 62.0 | 67.5 | -5.5 | -19.49 | -8.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 78-183 | 29.9 | 43.1 | -13.2 | -31.86 | -12.2 |  |  | !! CHECK: consensus_gap+money_moving close moneyline all sits -13.2 pts from its base (43.1%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+money_level | moneyline | 312-120 | 72.2 | 67.9 | 4.3 | -26.31 | -6.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+money_moving | moneyline | 162-185 | 46.7 | 46.8 | -0.1 | -33.38 | -9.6 |  |  | DROP: below break-even |
| money_delta+money_moving | moneyline | 74-198 | 27.2 | 30.3 | -3.0 | -36.74 | -13.5 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 72-197 | 26.8 | 30.3 | -3.5 | -37.93 | -14.1 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 76-191 | 28.5 | 42.2 | -13.7 | -37.6 | -14.1 |  |  | !! CHECK: consensus_gap+sharp_gap close moneyline all sits -13.7 pts from its base (42.2%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+sharp_gap | moneyline | 154-187 | 45.2 | 45.8 | -0.7 | -36.41 | -10.7 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | moneyline | 44-114 | 27.8 | 29.4 | -1.5 | -19.19 | -12.1 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 45-116 | 28.0 | 29.4 | -1.4 | -21.59 | -13.4 |  |  | DROP: below break-even |
| consensus_gap+pin_move | moneyline | 50-42 | 54.3 | 52.3 | 2.0 | +22.47 | 24.4 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 14-32 | 30.4 | 31.6 | -1.2 | +11.53 | 25.1 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 7-38 | 15.6 | 30.7 | -15.2 | -10.26 | -22.8 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 128-118 | 52.0 | 49.0 | 3.1 | -0.03 | -0.0 |  |  | no edge shown yet |
| follow_move+pin_rlm | moneyline | 37-68 | 35.2 | 30.9 | 4.4 | -7.12 | -6.8 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 62-139 | 30.8 | 31.0 | -0.1 | -23.38 | -11.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 70-90 | 43.8 | 42.6 | 1.2 | +7.04 | 4.4 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 53-100 | 34.6 | 30.5 | 4.1 | +16.45 | 10.8 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 60-131 | 31.4 | 31.1 | 0.3 | -18.5 | -9.7 |  |  | DROP: below break-even |
| pin_move+pin_rlm | moneyline | 40-71 | 36.0 | 30.4 | 5.7 | +9.99 | 9.0 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 44-64 | 40.7 | 30.0 | 10.7 | +9.7 | 9.0 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 31-54 | 36.5 | 31.3 | 5.1 | -0.38 | -0.5 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 68-96 | 41.5 | 41.7 | -0.3 | +0.47 | 0.3 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 24-56 | 30.0 | 29.9 | 0.1 | -12.26 | -15.3 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 37-68 | 35.2 | 30.9 | 4.4 | -7.12 | -6.8 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 54-107 | 33.5 | 30.4 | 3.1 | +10.85 | 6.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 41-111 | 27.0 | 29.4 | -2.4 | -21.43 | -14.1 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 62-139 | 30.8 | 31.0 | -0.1 | -23.38 | -11.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 17-88 | 16.2 | 30.5 | -14.3 | -24.95 | -23.8 |  |  | DROP: below break-even |
| consensus_gap+pin_value | moneyline | 17-52 | 24.6 | 33.1 | -8.5 | +2.23 | 3.2 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 25-48 | 34.2 | 31.8 | 2.5 | -2.3 | -3.2 |  |  | DROP: below break-even |
| money_delta+pin_rlm | moneyline | 31-61 | 33.7 | 30.7 | 3.0 | +0.91 | 1.0 |  |  | DROP: below break-even |
| money_delta+pin_value | moneyline | 4-18 | 18.2 | 28.9 | -10.7 | -5.3 | -24.1 |  |  | keep collecting (22/30) |
| money_moving+pin_value | moneyline | 13-37 | 26.0 | 33.1 | -7.1 | +10.89 | 21.8 |  |  | DROP: below break-even |
| pin_move+pin_value | moneyline | 9-13 | 40.9 | 40.4 | 0.5 | +6.3 | 28.6 |  |  | keep collecting (22/30) |
| pin_rlm+pin_value | moneyline | 6-11 | 35.3 | 28.9 | 6.4 | +12.45 | 73.2 |  |  | keep collecting (17/30) |
| pin_value+sharp_gap | moneyline | 13-41 | 24.1 | 34.3 | -10.3 | +6.89 | 12.8 |  |  | DROP: below break-even |
| follow_move+money_delta | moneyline | 40-84 | 32.3 | 32.6 | -0.3 | -23.18 | -18.7 |  |  | DROP: below break-even |
| money_delta+money_level | moneyline | 23-28 | 45.1 | 34.7 | 10.4 | +12.68 | 24.9 |  |  | no edge shown yet |
| money_delta+rlm_ratio | moneyline | 33-73 | 31.1 | 31.6 | -0.5 | -19.27 | -18.2 |  |  | DROP: below break-even |
| money_level+pin_move | moneyline | 95-59 | 61.7 | 65.4 | -3.7 | -9.05 | -5.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 14-14 | 50.0 | 34.9 | 15.1 | +3.97 | 14.2 |  |  | keep collecting (28/30) |
| money_level+rlm_ratio | moneyline | 17-21 | 44.7 | 37.8 | 7.0 | +0.43 | 1.1 |  |  | no edge shown yet |
| money_delta+rlm_quiet | moneyline | 26-64 | 28.9 | 30.3 | -1.4 | -20.84 | -23.2 |  |  | DROP: below break-even |
| money_level+pin_value | moneyline | 6-8 | 42.9 | 65.1 | -22.2 | -4.75 | -33.9 |  |  | keep collecting (14/30) |
| follow_move+pin_value | moneyline | 5-10 | 33.3 | 40.1 | -6.8 | +4.75 | 31.7 |  |  | keep collecting (15/30) |
| pin_value+rlm_quiet | moneyline | 3-7 | 30.0 | 28.9 | 1.1 | +6.5 | 65.0 |  |  | keep collecting (10/30) |
| pin_value+rlm_ratio | moneyline | 2-3 | 40.0 | 28.9 | 11.1 | -0.1 | -2.0 |  |  | keep collecting (5/30) |
| consensus_gap+follow_move | spread | 40-32 | 55.6 | 48.2 | 7.4 | +2.22 | 3.1 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 55-51 | 51.9 | 48.7 | 3.2 | -4.05 | -3.8 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 33-38 | 46.5 | 49.3 | -2.8 | -9.7 | -13.7 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 5-4 | 55.6 | 50.4 | 5.2 | +0.3 | 3.3 |  |  | keep collecting (9/30) |
| consensus_gap+pin_value | spread | 81-60 | 57.4 | 49.0 | 8.5 | +9.27 | 6.6 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 7-4 | 63.6 | 50.3 | 13.3 | +1.92 | 17.5 |  |  | keep collecting (11/30) |
| consensus_gap+sharp_gap | spread | 54-51 | 51.4 | 48.9 | 2.5 | -4.95 | -4.7 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 199-202 | 49.6 | 49.2 | 0.4 | -22.05 | -5.5 |  |  | no edge shown yet |
| follow_move+pin_move | spread | 164-192 | 46.1 | 50.1 | -4.0 | -42.55 | -12.0 |  |  | DROP: below break-even |
| follow_move+pin_rlm | spread | 21-21 | 50.0 | 50.8 | -0.8 | -1.83 | -4.4 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 75-68 | 52.4 | 49.0 | 3.5 | -2.61 | -1.8 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 53-53 | 50.0 | 50.5 | -0.5 | -5.04 | -4.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 200-201 | 49.9 | 49.3 | 0.6 | -19.92 | -5.0 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 148-160 | 48.1 | 49.9 | -1.8 | -26.28 | -8.5 |  |  | DROP: below break-even |
| money_moving+pin_rlm | spread | 28-27 | 50.9 | 51.3 | -0.4 | -1.53 | -2.8 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 106-114 | 48.2 | 49.1 | -0.9 | -22.52 | -10.2 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 51-52 | 49.5 | 50.4 | -0.9 | -5.97 | -5.8 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 422-411 | 50.7 | 49.4 | 1.2 | -30.72 | -3.7 |  |  | no edge shown yet |
| pin_move+pin_rlm | spread | 30-27 | 52.6 | 51.4 | 1.2 | +0.3 | 0.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 104-109 | 48.8 | 50.0 | -1.2 | -17.54 | -8.2 |  |  | no edge shown yet |
| pin_move+rlm_ratio | spread | 27-29 | 48.2 | 50.7 | -2.5 | -4.52 | -8.1 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 151-160 | 48.6 | 49.9 | -1.3 | -23.55 | -7.6 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 10-12 | 45.5 | 51.6 | -6.1 | -3.19 | -14.5 |  |  | keep collecting (22/30) |
| pin_rlm+rlm_ratio | spread | 21-21 | 50.0 | 50.8 | -0.8 | -1.83 | -4.4 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 30-27 | 52.6 | 51.4 | 1.2 | +0.3 | 0.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 8-8 | 50.0 | 49.6 | 0.4 | -1.17 | -7.3 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | spread | 106-114 | 48.2 | 49.2 | -1.0 | -22.58 | -10.3 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 53-53 | 50.0 | 50.5 | -0.5 | -5.04 | -4.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 187-197 | 48.7 | 48.8 | -0.1 | -27.98 | -7.3 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 31-31 | 50.0 | 50.0 | 0.0 | -3.19 | -5.1 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 329-321 | 50.6 | 49.0 | 1.6 | -25.04 | -3.9 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 66-58 | 53.2 | 48.3 | 4.9 | -1.52 | -1.2 |  |  | no edge shown yet |
| money_level+money_moving | spread | 328-322 | 50.5 | 48.9 | 1.5 | -26.95 | -4.1 |  |  | no edge shown yet |
| money_level+pin_move | spread | 131-155 | 45.8 | 49.5 | -3.7 | -37.13 | -13.0 |  |  | DROP: below break-even |
| money_level+pin_value | spread | 113-117 | 49.1 | 48.6 | 0.5 | -19.6 | -8.5 |  |  | no edge shown yet |
| consensus_gap+money_delta | spread | 17-15 | 53.1 | 51.1 | 2.1 | -0.46 | -1.4 |  |  | no edge shown yet |
| follow_move+money_delta | spread | 48-57 | 45.7 | 50.5 | -4.8 | -13.65 | -13.0 |  |  | no edge shown yet |
| money_delta+money_level | spread | 49-47 | 51.0 | 49.9 | 1.1 | -2.93 | -3.1 |  |  | no edge shown yet |
| money_delta+money_moving | spread | 83-89 | 48.3 | 50.6 | -2.3 | -14.12 | -8.2 |  |  | no edge shown yet |
| money_delta+pin_value | spread | 38-31 | 55.1 | 50.9 | 4.1 | +2.19 | 3.2 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 82-87 | 48.5 | 50.5 | -2.0 | -13.1 | -7.8 |  |  | no edge shown yet |
| follow_move+rlm_quiet | spread | 68-73 | 48.2 | 51.5 | -3.3 | -9.73 | -6.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 15-8 | 65.2 | 51.6 | 13.6 | +5.65 | 24.5 |  |  | keep collecting (23/30) |
| rlm_quiet+sharp_gap | spread | 29-19 | 60.4 | 51.9 | 8.6 | +7.6 | 15.8 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 16-14 | 53.3 | 50.5 | 2.9 | +0.39 | 1.3 |  |  | no edge shown yet |
| money_delta+pin_move | spread | 43-51 | 45.7 | 51.4 | -5.6 | -11.9 | -12.7 |  |  | no edge shown yet |
| money_delta+rlm_ratio | spread | 19-30 | 38.8 | 50.1 | -11.3 | -13.18 | -26.9 |  |  | DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 53.4 | 46.6 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_rlm | spread | 16-19 | 45.7 | 51.3 | -5.6 | -4.61 | -13.2 |  |  | no edge shown yet |
| money_delta+rlm_quiet | spread | 19-22 | 46.3 | 51.8 | -5.4 | -4.38 | -10.7 |  |  | no edge shown yet |
| money_moving+rlm_quiet | spread | 28-19 | 59.6 | 51.8 | 7.8 | +6.65 | 14.2 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 38-40 | 48.7 | 51.9 | -3.2 | -4.59 | -5.9 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-3 | 66.7 | 52.7 | 14.0 | +2.56 | 28.4 |  |  | keep collecting (9/30) |
| consensus_gap+rlm_quiet | spread | 4-3 | 57.1 | 51.5 | 5.7 | +0.48 | 6.9 |  |  | keep collecting (7/30) |
| pin_value+rlm_quiet | spread | 7-7 | 50.0 | 50.5 | -0.5 | -0.85 | -6.1 |  |  | keep collecting (14/30) |
| follow_move+money_delta | total | 121-122 | 49.8 | 49.6 | 0.2 | -11.16 | -4.6 |  |  | no edge shown yet |
| money_level+money_moving | total | 287-291 | 49.7 | 50.1 | -0.4 | -30.09 | -5.2 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 282-283 | 49.9 | 50.1 | -0.2 | -26.49 | -4.7 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 431-472 | 47.7 | 49.9 | -2.2 | -78.87 | -8.7 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 77-72 | 51.7 | 50.5 | 1.2 | -3.75 | -2.5 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 37-29 | 56.1 | 50.2 | 5.8 | +3.9 | 5.9 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 82-76 | 51.9 | 50.3 | 1.6 | -3.19 | -2.0 |  |  | no edge shown yet |
| follow_move+money_moving | total | 274-307 | 47.2 | 49.9 | -2.7 | -57.06 | -9.8 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 282-306 | 48.0 | 49.9 | -1.9 | -48.76 | -8.3 |  |  | DROP: below break-even |
| money_level+pin_move | total | 161-144 | 52.8 | 50.1 | 2.7 | +2.41 | 0.8 |  |  | no edge shown yet |
| money_level+pin_value | total | 124-108 | 53.4 | 50.3 | 3.1 | +3.05 | 1.3 |  |  | no edge shown yet |
| pin_move+pin_value | total | 107-104 | 50.7 | 50.0 | 0.7 | -7.42 | -3.5 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 135-173 | 43.8 | 49.6 | -5.8 | -48.69 | -15.8 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 182-193 | 48.5 | 49.8 | -1.3 | -26.82 | -7.2 |  |  | no edge shown yet |
| rlm_quiet+sharp_gap | total | 78-112 | 41.1 | 49.6 | -8.5 | -40.45 | -21.3 |  |  | DROP: below break-even |
| money_delta+money_moving | total | 151-147 | 50.7 | 49.6 | 1.0 | -8.69 | -2.9 |  |  | no edge shown yet |
| follow_move+money_level | total | 229-218 | 51.2 | 50.1 | 1.1 | -9.79 | -2.2 |  |  | no edge shown yet |
| follow_move+pin_value | total | 96-93 | 50.8 | 50.0 | 0.8 | -6.4 | -3.4 |  |  | no edge shown yet |
| money_moving+pin_value | total | 98-110 | 47.1 | 50.1 | -2.9 | -21.72 | -10.4 |  |  | DROP: below break-even |
| pin_value+sharp_gap | total | 99-111 | 47.1 | 50.0 | -2.9 | -21.77 | -10.4 |  |  | DROP: below break-even |
| consensus_gap+money_moving | total | 63-65 | 49.2 | 50.3 | -1.0 | -8.97 | -7.0 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 65-65 | 50.0 | 50.2 | -0.2 | -7.18 | -5.5 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 53-45 | 54.1 | 50.3 | 3.8 | +2.08 | 2.1 |  |  | no edge shown yet |
| consensus_gap+money_delta | total | 23-16 | 59.0 | 49.9 | 9.1 | +4.38 | 11.2 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | total | 15-13 | 53.6 | 49.8 | 3.8 | +0.49 | 1.8 |  |  | keep collecting (28/30) |
| money_delta+rlm_quiet | total | 37-60 | 38.1 | 49.5 | -11.3 | -26.01 | -26.8 |  |  | DROP: below break-even |
| money_delta+sharp_gap | total | 151-144 | 51.2 | 49.6 | 1.6 | -5.69 | -1.9 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 72-109 | 39.8 | 49.6 | -9.8 | -42.9 | -23.7 |  |  | !! IMPLAUSIBLE: money_moving+rlm_quiet close total all 39.8% on n=181. A -110 market outside 40-60% at this sample is a measurement bug until proven otherwise. Recompute from source.  ||  DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 75-64 | 54.0 | 49.7 | 4.2 | +4.5 | 3.2 |  |  | no edge shown yet |
| money_delta+pin_move | total | 83-83 | 50.0 | 49.6 | 0.4 | -6.88 | -4.1 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 183-194 | 48.5 | 49.8 | -1.3 | -26.86 | -7.1 |  |  | no edge shown yet |
| follow_move+pin_move | total | 208-225 | 48.0 | 49.9 | -1.8 | -34.79 | -8.0 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | total | 28-40 | 41.2 | 49.6 | -8.5 | -14.35 | -21.1 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | total | 11-11 | 50.0 | 50.0 | -0.0 | -1.22 | -5.5 |  |  | keep collecting (22/30) |
| consensus_gap+rlm_ratio | total | 21-13 | 61.8 | 50.0 | 11.7 | +5.66 | 16.7 |  |  | no edge shown yet |
| follow_move+pin_rlm | total | 86-80 | 51.8 | 49.6 | 2.2 | -0.97 | -0.6 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 160-154 | 51.0 | 49.6 | 1.3 | -7.42 | -2.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 46-32 | 59.0 | 49.6 | 9.4 | +10.22 | 13.1 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 74-56 | 56.9 | 49.7 | 7.2 | +11.61 | 8.9 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 96-88 | 52.2 | 49.6 | 2.6 | -0.03 | -0.0 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 154-150 | 50.7 | 49.6 | 1.0 | -8.91 | -2.9 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 99-91 | 52.1 | 49.6 | 2.5 | -0.29 | -0.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 94-82 | 53.4 | 49.6 | 3.8 | +4.2 | 2.4 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 32-29 | 52.5 | 49.7 | 2.8 | -0.01 | -0.0 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 86-80 | 51.8 | 49.6 | 2.2 | -0.97 | -0.6 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 99-91 | 52.1 | 49.6 | 2.5 | -0.29 | -0.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 35-30 | 53.8 | 49.7 | 4.1 | +1.69 | 2.6 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 160-154 | 51.0 | 49.6 | 1.3 | -7.42 | -2.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 58-49 | 54.2 | 49.5 | 4.7 | +4.32 | 4.0 |  |  | no edge shown yet |
| money_delta+rlm_ratio | total | 96-78 | 55.2 | 49.6 | 5.6 | +9.87 | 5.7 |  |  | no edge shown yet |
| money_delta+pin_value | total | 47-36 | 56.6 | 49.7 | 6.9 | +6.55 | 7.9 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 60-86 | 41.1 | 49.6 | -8.5 | -30.7 | -21.0 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | total | 31-46 | 40.3 | 49.6 | -9.3 | -17.58 | -22.8 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | total | 62-89 | 41.1 | 49.5 | -8.5 | -32.05 | -21.2 |  |  | DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 49.4 | 50.6 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| rlm_quiet | close | 1-3k bets | 189-280 | 40.3 | -1.8 | -8.0 |  |
| rlm_quiet | close | 3k+ bets | 78-110 | 41.5 | -0.8 | -11.3 |  |
| rlm_quiet | close | <1k bets | 32-47 | 40.5 | -1.5 | -16.0 |  |
| rlm_quiet | close | pin $1-2k | 79-135 | 36.9 | -6.8 | -18.9 |  |
| rlm_quiet | close | pin $2k+ | 93-113 | 45.1 | 6.8 | 3.4 |  |
| rlm_quiet | close | pin limit <$1k | 51-55 | 48.1 | -1.2 | -7.6 |  |
| pin_move | close | 1-3k bets | 440-445 | 49.7 | 0.2 | -2.3 |  |
| pin_move | close | 3k+ bets | 177-190 | 48.2 | -1.4 | -7.2 |  |
| pin_move | close | <1k bets | 87-87 | 50.0 | -0.3 | -4.3 |  |
| pin_move | close | pin $1-2k | 318-334 | 48.8 | -1.2 | -4.4 |  |
| pin_move | close | pin $2k+ | 262-274 | 48.9 | -0.5 | -5.6 |  |
| pin_move | close | pin limit <$1k | 124-117 | 51.5 | 1.9 | 0.3 |  |
| money_delta | close | 1-3k bets | 261-335 | 43.8 | -1.0 | -7.6 |  |
| money_delta | close | 3k+ bets | 112-146 | 43.4 | -0.4 | -3.5 |  |
| money_delta | close | <1k bets | 52-76 | 40.6 | -2.4 | -15.4 |  |
| money_delta | close | pin $1-2k | 153-154 | 49.8 | 3.5 | 3.8 |  |
| money_delta | close | pin $2k+ | 110-143 | 43.5 | 1.9 | -7.7 |  |
| money_delta | close | pin limit <$1k | 62-73 | 45.9 | -3.3 | -8.7 |  |
| pin_rlm | close | 1-3k bets | 114-135 | 45.8 | 3.4 | 8.5 |  |
| pin_rlm | close | 3k+ bets | 43-64 | 40.2 | -1.9 | -13.4 |  |
| pin_rlm | close | <1k bets | 26-26 | 50.0 | 7.7 | 7.9 |  |
| pin_rlm | close | pin $1-2k | 80-92 | 46.5 | 2.4 | 4.8 |  |
| pin_rlm | close | pin $2k+ | 54-92 | 37.0 | 0.8 | -7.0 |  |
| pin_rlm | close | pin limit <$1k | 49-41 | 54.4 | 5.7 | 14.3 |  |
| follow_move | close | 1-3k bets | 753-716 | 51.3 | 0.7 | -5.6 |  |
| follow_move | close | 3k+ bets | 280-265 | 51.4 | 0.6 | -5.4 |  |
| follow_move | close | <1k bets | 164-154 | 51.6 | -0.4 | -11.8 |  |
| follow_move | close | pin $1-2k | 358-411 | 46.6 | -3.8 | -12.7 |  |
| follow_move | close | pin $2k+ | 323-287 | 53.0 | 2.2 | -2.4 |  |
| follow_move | close | pin limit <$1k | 150-145 | 50.8 | 1.0 | -3.1 |  |
| rlm_ratio | close | 1-3k bets | 174-232 | 42.9 | -0.9 | -7.5 |  |
| rlm_ratio | close | 3k+ bets | 65-76 | 46.1 | 2.4 | -2.2 |  |
| rlm_ratio | close | <1k bets | 36-38 | 48.6 | 5.3 | -3.3 |  |
| rlm_ratio | close | pin $1-2k | 97-107 | 47.5 | 1.8 | -1.0 |  |
| rlm_ratio | close | pin $2k+ | 53-81 | 39.6 | 1.7 | -12.5 |  |
| rlm_ratio | close | pin limit <$1k | 54-51 | 51.4 | 2.4 | -0.8 |  |
| money_level | close | 1-3k bets | 961-701 | 57.8 | 2.6 | -2.6 |  |
| money_level | close | 3k+ bets | 352-290 | 54.8 | -0.0 | -4.7 |  |
| money_level | close | <1k bets | 205-149 | 57.9 | 2.6 | -6.2 |  |
| money_level | close | pin $1-2k | 446-397 | 52.9 | -0.7 | -6.1 |  |
| money_level | close | pin $2k+ | 393-323 | 54.9 | -2.1 | -9.1 |  |
| money_level | close | pin limit <$1k | 179-157 | 53.3 | 2.9 | 1.1 |  |
| sharp_gap | close | 1-3k bets | 729-859 | 45.9 | -1.7 | -8.9 |  |
| sharp_gap | close | 3k+ bets | 291-331 | 46.8 | -0.9 | -3.6 |  |
| sharp_gap | close | <1k bets | 160-176 | 47.6 | -0.5 | -11.1 |  |
| sharp_gap | close | pin $1-2k | 384-425 | 47.5 | -1.2 | -6.2 |  |
| sharp_gap | close | pin $2k+ | 314-375 | 45.6 | -1.2 | -6.4 |  |
| sharp_gap | close | pin limit <$1k | 153-169 | 47.5 | -1.9 | -6.2 |  |
| money_moving | close | 1-3k bets | 743-852 | 46.6 | -1.4 | -8.4 |  |
| money_moving | close | 3k+ bets | 293-331 | 47.0 | -1.2 | -4.4 |  |
| money_moving | close | <1k bets | 158-174 | 47.6 | -0.4 | -9.8 |  |
| money_moving | close | pin $1-2k | 385-426 | 47.5 | -1.5 | -6.4 |  |
| money_moving | close | pin $2k+ | 319-370 | 46.3 | -0.5 | -5.6 |  |
| money_moving | close | pin limit <$1k | 153-175 | 46.6 | -2.8 | -7.9 |  |
| pin_value | close | 1-3k bets | 331-323 | 50.6 | 2.2 | 2.9 |  |
| pin_value | close | 3k+ bets | 106-136 | 43.8 | -5.2 | -14.8 |  |
| pin_value | close | <1k bets | 72-58 | 55.4 | 8.0 | 12.3 |  |
| pin_value | close | pin $1-2k | 235-259 | 47.6 | -1.1 | -4.5 |  |
| pin_value | close | pin $2k+ | 146-167 | 46.6 | -0.5 | -2.1 |  |
| pin_value | close | pin limit <$1k | 130-92 | 58.6 | 8.6 | 13.1 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 46.6 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 46.6 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 296-346 | 46.1 | -3.3 | -9.2 |  |
| consensus_gap | close | 3k+ bets | 116-126 | 47.9 | -1.9 | 1.5 |  |
| consensus_gap | close | <1k bets | 58-86 | 40.3 | -5.1 | -19.8 |  |
| consensus_gap | close | pin $1-2k | 139-148 | 48.4 | -1.3 | -0.2 |  |
| consensus_gap | close | pin $2k+ | 144-136 | 51.4 | -0.5 | 2.1 |  |
| consensus_gap | close | pin limit <$1k | 60-56 | 51.7 | 1.6 | 0.6 |  |
| consensus_gap+follow_move | close | 1-3k bets | 110-106 | 50.9 | -0.3 | -4.3 |  |
| consensus_gap+money_level | close | 1-3k bets | 194-133 | 59.3 | 0.8 | -0.5 |  |
| consensus_gap+money_moving | close | 1-3k bets | 124-185 | 40.1 | -6.3 | -11.4 |  |
| consensus_gap+pin_move | close | 1-3k bets | 76-67 | 53.1 | 2.6 | 11.4 |  |
| consensus_gap+pin_value | close | 1-3k bets | 115-128 | 47.3 | 0.6 | -2.0 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 122-190 | 39.1 | -6.8 | -12.9 |  |
| follow_move+money_level | close | 1-3k bets | 471-340 | 58.1 | 2.5 | -3.9 |  |
| follow_move+money_moving | close | 1-3k bets | 411-449 | 47.8 | -1.0 | -7.9 |  |
| follow_move+pin_move | close | 1-3k bets | 308-337 | 47.8 | -1.8 | -8.5 |  |
| follow_move+pin_value | close | 1-3k bets | 109-104 | 51.2 | 2.2 | 1.5 |  |
| follow_move+sharp_gap | close | 1-3k bets | 412-450 | 47.8 | -0.8 | -7.3 |  |
| money_level+money_moving | close | 1-3k bets | 529-466 | 53.2 | 0.9 | -3.7 |  |
| money_level+pin_move | close | 1-3k bets | 253-223 | 53.2 | 0.4 | -3.4 |  |
| money_level+pin_value | close | 1-3k bets | 158-140 | 53.0 | 3.4 | -0.5 |  |
| money_level+sharp_gap | close | 1-3k bets | 510-460 | 52.6 | 0.6 | -4.0 |  |
| money_moving+pin_move | close | 1-3k bets | 257-271 | 48.7 | 0.0 | -2.6 |  |
| money_moving+pin_value | close | 1-3k bets | 141-163 | 46.4 | -1.5 | -6.2 |  |
| money_moving+sharp_gap | close | 1-3k bets | 701-817 | 46.2 | -1.6 | -8.1 |  |
| pin_move+pin_value | close | 1-3k bets | 139-136 | 50.5 | 0.9 | -1.5 |  |
| pin_move+sharp_gap | close | 1-3k bets | 261-277 | 48.5 | 0.1 | -2.6 |  |
| pin_value+sharp_gap | close | 1-3k bets | 142-169 | 45.7 | -2.2 | -7.7 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 189-280 | 40.3 | -1.8 | -8.0 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 93-165 | 36.0 | -5.4 | -14.8 |  |
| consensus_gap+money_delta | close | 1-3k bets | 34-70 | 32.7 | -6.2 | -17.2 |  |
| follow_move+money_delta | close | 1-3k bets | 130-165 | 44.1 | -1.9 | -10.9 |  |
| money_delta+money_level | close | 1-3k bets | 92-88 | 51.1 | 3.1 | 4.8 |  |
| money_delta+money_moving | close | 1-3k bets | 189-265 | 41.6 | -1.5 | -9.1 |  |
| money_delta+pin_value | close | 1-3k bets | 57-52 | 52.3 | 4.4 | 4.0 |  |
| money_delta+sharp_gap | close | 1-3k bets | 188-262 | 41.8 | -1.4 | -8.8 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 92-107 | 46.2 | -0.4 | -2.7 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 22-30 | 42.3 | 3.0 | 21.3 |  |
| money_level+pin_rlm | close | 1-3k bets | 49-39 | 55.7 | 8.0 | 7.6 |  |
| pin_move+pin_rlm | close | 1-3k bets | 105-113 | 48.2 | 4.3 | 6.6 |  |
| pin_rlm+pin_value | close | 1-3k bets | 33-30 | 52.4 | 5.8 | 22.8 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 114-135 | 45.8 | 3.4 | 8.5 |  |
| money_delta+pin_rlm | close | 1-3k bets | 64-76 | 45.7 | 3.0 | 5.6 |  |
| money_moving+pin_rlm | close | 1-3k bets | 109-127 | 46.2 | 3.6 | 10.2 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 27-38 | 41.5 | 0.6 | 4.9 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 174-232 | 42.9 | -0.9 | -7.5 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 91-122 | 42.7 | -1.6 | -11.6 |  |
| money_level+rlm_ratio | close | 1-3k bets | 79-74 | 51.6 | 3.1 | -0.2 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 167-221 | 43.0 | -0.9 | -6.7 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 90-100 | 47.4 | 2.6 | -1.2 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 30-27 | 52.6 | 4.8 | 1.6 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 174-232 | 42.9 | -0.9 | -7.5 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 18-42 | 30.0 | -7.1 | -12.6 |  |
| follow_move+pin_rlm | close | 1-3k bets | 84-107 | 44.0 | 0.5 | -7.4 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 87-161 | 35.1 | -6.2 | -16.2 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 84-121 | 41.0 | -2.8 | -11.1 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 35-68 | 34.0 | -5.6 | -20.2 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 84-107 | 44.0 | 0.5 | -7.4 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 73-142 | 34.0 | -6.1 | -16.1 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 50-93 | 35.0 | -7.9 | -23.8 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 22-30 | 42.3 | -3.9 | 1.4 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 50.6 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 43-37 | 53.8 | 2.8 | 0.5 |  |
| consensus_gap+money_moving | close | 3k+ bets | 47-73 | 39.2 | -7.5 | 2.5 |  |
| consensus_gap+pin_move | close | 3k+ bets | 36-29 | 55.4 | 4.0 | 6.2 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 5-10 | 33.3 | -9.0 | -11.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 45-44 | 50.6 | 2.8 | 2.1 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 5-10 | 33.3 | -7.2 | -10.7 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 47-74 | 38.8 | -7.4 | 3.9 |  |
| follow_move+money_moving | close | 3k+ bets | 148-161 | 47.9 | -0.9 | -7.8 |  |
| follow_move+pin_move | close | 3k+ bets | 136-138 | 49.6 | -0.1 | -4.1 |  |
| follow_move+pin_rlm | close | 3k+ bets | 40-46 | 46.5 | 3.3 | 1.1 |  |
| follow_move+pin_value | close | 3k+ bets | 44-51 | 46.3 | -3.5 | -12.8 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 65-76 | 46.1 | 2.4 | -2.2 |  |
| follow_move+sharp_gap | close | 3k+ bets | 147-159 | 48.0 | -0.2 | -5.8 |  |
| money_moving+pin_move | close | 3k+ bets | 96-119 | 44.7 | -3.7 | -12.6 |  |
| money_moving+pin_rlm | close | 3k+ bets | 42-62 | 40.4 | -1.7 | -12.8 |  |
| money_moving+pin_value | close | 3k+ bets | 53-76 | 41.1 | -7.5 | -17.4 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 62-74 | 45.6 | 1.9 | -3.5 |  |
| money_moving+sharp_gap | close | 3k+ bets | 282-319 | 46.9 | -0.9 | -3.5 |  |
| pin_move+pin_rlm | close | 3k+ bets | 40-55 | 42.1 | -1.7 | -9.6 |  |
| pin_move+pin_value | close | 3k+ bets | 49-65 | 43.0 | -6.6 | -18.9 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 42-47 | 47.2 | 2.3 | 0.7 |  |
| pin_move+sharp_gap | close | 3k+ bets | 94-119 | 44.1 | -3.8 | -12.4 |  |
| pin_rlm+pin_value | close | 3k+ bets | 8-19 | 29.6 | -18.1 | -43.6 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 40-46 | 46.5 | 3.3 | 1.1 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 43-64 | 40.2 | -1.9 | -13.4 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 10-13 | 43.5 | -6.7 | -17.4 |  |
| pin_value+sharp_gap | close | 3k+ bets | 53-76 | 41.1 | -7.7 | -17.4 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 65-76 | 46.1 | 2.4 | -2.2 |  |
| follow_move+money_delta | close | 3k+ bets | 53-69 | 43.4 | -1.2 | -10.6 |  |
| money_level+money_moving | close | 3k+ bets | 193-182 | 51.5 | -0.8 | -4.9 |  |
| money_level+sharp_gap | close | 3k+ bets | 188-179 | 51.2 | -0.7 | -4.2 |  |
| follow_move+money_level | close | 3k+ bets | 158-120 | 56.8 | 0.9 | -4.3 |  |
| money_level+rlm_ratio | close | 3k+ bets | 26-17 | 60.5 | 12.7 | 23.5 |  |
| consensus_gap+money_level | close | 3k+ bets | 70-62 | 53.0 | -4.6 | -9.2 |  |
| money_level+pin_move | close | 3k+ bets | 86-88 | 49.4 | -4.4 | -10.7 |  |
| money_level+pin_value | close | 3k+ bets | 59-71 | 45.4 | -5.2 | -15.6 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 10-16 | 38.5 | -1.1 | -8.7 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 78-110 | 41.5 | -0.8 | -11.3 |  |
| money_delta+money_moving | close | 3k+ bets | 83-112 | 42.6 | -0.2 | -1.5 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 30-50 | 37.5 | -3.3 | -16.2 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 41-62 | 39.8 | -2.4 | -14.3 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 38-62 | 38.0 | -4.3 | -18.3 |  |
| consensus_gap+money_delta | close | 3k+ bets | 16-27 | 37.2 | -2.6 | 16.2 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 19-39 | 32.8 | -8.8 | -29.5 |  |
| money_delta+sharp_gap | close | 3k+ bets | 81-109 | 42.6 | 0.0 | -1.1 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 45-55 | 45.0 | 1.7 | -3.5 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 17-31 | 35.4 | -5.0 | -19.1 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 10-20 | 33.3 | -15.9 | -36.5 |  |
| money_delta+money_level | close | 3k+ bets | 40-31 | 56.3 | 9.6 | 15.0 |  |
| money_level+pin_rlm | close | 3k+ bets | 16-12 | 57.1 | 11.0 | 22.3 |  |
| money_delta+pin_value | close | 3k+ bets | 22-25 | 46.8 | -0.8 | -11.6 |  |
| money_delta+pin_move | close | 3k+ bets | 45-55 | 45.0 | -0.7 | -9.0 |  |
| money_delta+pin_rlm | close | 3k+ bets | 28-36 | 43.8 | 1.2 | -7.9 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 36-37 | 49.3 | 5.9 | 3.8 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 46.6 | 87.7 |  |
| money_level+money_moving | close | <1k bets | 110-95 | 53.7 | 1.3 | -8.2 |  |
| money_level+sharp_gap | close | <1k bets | 113-96 | 54.1 | 1.4 | -8.3 |  |
| money_moving+sharp_gap | close | <1k bets | 154-171 | 47.4 | -0.5 | -10.5 |  |
| consensus_gap+money_level | close | <1k bets | 31-28 | 52.5 | -3.7 | -18.5 |  |
| consensus_gap+money_moving | close | <1k bets | 25-41 | 37.9 | -5.9 | -19.1 |  |
| consensus_gap+pin_move | close | <1k bets | 8-13 | 38.1 | -12.5 | -17.2 |  |
| consensus_gap+pin_value | close | <1k bets | 19-16 | 54.3 | 11.8 | 29.5 |  |
| consensus_gap+sharp_gap | close | <1k bets | 26-43 | 37.7 | -6.1 | -20.5 |  |
| money_level+pin_move | close | <1k bets | 48-44 | 52.2 | -0.7 | -6.6 |  |
| money_level+pin_value | close | <1k bets | 26-21 | 55.3 | 5.5 | 3.3 |  |
| money_moving+pin_move | close | <1k bets | 47-50 | 48.5 | 0.7 | -2.4 |  |
| money_moving+pin_value | close | <1k bets | 23-21 | 52.3 | 7.0 | 20.2 |  |
| pin_move+pin_value | close | <1k bets | 32-24 | 57.1 | 8.6 | 14.5 |  |
| pin_move+sharp_gap | close | <1k bets | 47-51 | 48.0 | -0.3 | -6.7 |  |
| pin_value+sharp_gap | close | <1k bets | 23-20 | 53.5 | 7.8 | 23.0 |  |
| follow_move+money_delta | close | <1k bets | 26-29 | 47.3 | 3.6 | -5.4 |  |
| follow_move+money_moving | close | <1k bets | 76-81 | 48.4 | -0.9 | -11.2 |  |
| follow_move+pin_move | close | <1k bets | 56-57 | 49.6 | -1.2 | -7.7 |  |
| follow_move+sharp_gap | close | <1k bets | 77-82 | 48.4 | -1.4 | -13.6 |  |
| money_delta+money_moving | close | <1k bets | 36-57 | 38.7 | -2.1 | -16.4 |  |
| money_delta+pin_move | close | <1k bets | 14-20 | 41.2 | -3.6 | -19.8 |  |
| money_delta+sharp_gap | close | <1k bets | 36-57 | 38.7 | -2.1 | -16.4 |  |
| follow_move+rlm_quiet | close | <1k bets | 32-47 | 40.5 | -1.5 | -16.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 36-38 | 48.6 | 5.3 | -3.3 |  |
| money_delta+rlm_quiet | close | <1k bets | 13-14 | 48.1 | 6.9 | -0.5 |  |
| money_delta+rlm_ratio | close | <1k bets | 21-22 | 48.8 | 6.3 | -1.2 |  |
| money_moving+rlm_quiet | close | <1k bets | 19-19 | 50.0 | 8.2 | 7.8 |  |
| money_moving+rlm_ratio | close | <1k bets | 36-38 | 48.6 | 5.3 | -3.3 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 15-16 | 48.4 | 7.5 | -0.6 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 18-20 | 47.4 | 5.1 | -3.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 36-38 | 48.6 | 5.3 | -3.3 |  |
| follow_move+money_level | close | <1k bets | 99-72 | 57.9 | 0.9 | -10.3 |  |
| consensus_gap+money_delta | close | <1k bets | 7-22 | 24.1 | -11.0 | -35.0 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -3.1 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 13-17 | 43.3 | 3.0 | -7.1 |  |
| money_moving+pin_rlm | close | <1k bets | 26-26 | 50.0 | 7.7 | 7.9 |  |
| pin_rlm+sharp_gap | close | <1k bets | 26-26 | 50.0 | 7.7 | 7.9 |  |
| money_delta+pin_value | close | <1k bets | 10-8 | 55.6 | 9.8 | 25.3 |  |
| consensus_gap+follow_move | close | <1k bets | 14-21 | 40.0 | -10.9 | -35.2 |  |
| follow_move+pin_rlm | close | <1k bets | 20-16 | 55.6 | 11.3 | 9.1 |  |
| follow_move+pin_value | close | <1k bets | 23-15 | 60.5 | 11.6 | 15.1 |  |
| pin_move+pin_rlm | close | <1k bets | 24-21 | 53.3 | 9.0 | 10.6 |  |
| pin_move+rlm_quiet | close | <1k bets | 13-14 | 48.1 | 2.3 | 2.3 |  |
| pin_move+rlm_ratio | close | <1k bets | 20-18 | 52.6 | 7.1 | 2.3 |  |
| pin_rlm+pin_value | close | <1k bets | 7-3 | 70.0 | 27.1 | 66.8 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 9-6 | 60.0 | 15.9 | 17.9 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 20-16 | 55.6 | 11.3 | 9.1 |  |
| pin_value+rlm_quiet | close | <1k bets | 6-4 | 60.0 | 10.9 | 15.0 |  |
| pin_value+rlm_ratio | close | <1k bets | 5-1 | 83.3 | 34.9 | 58.3 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -6.9 | -42.5 |  |
| money_delta+money_level | close | <1k bets | 15-20 | 42.9 | -0.4 | -14.3 |  |
| money_level+rlm_ratio | close | <1k bets | 17-17 | 50.0 | 5.1 | -2.7 |  |
| money_level+pin_rlm | close | <1k bets | 11-9 | 55.0 | 11.6 | 8.4 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-6 | 14.3 | -23.0 | -72.7 |  |
| consensus_gap+follow_move | close | pin $1-2k | 50-57 | 46.7 | -4.9 | -10.9 |  |
| consensus_gap+money_moving | close | pin $1-2k | 61-77 | 44.2 | -4.3 | -5.2 |  |
| consensus_gap+pin_move | close | pin $1-2k | 53-54 | 49.5 | -1.8 | 5.9 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 14-19 | 42.4 | 0.8 | 25.4 |  |
| consensus_gap+pin_value | close | pin $1-2k | 81-85 | 48.8 | 2.3 | -0.9 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 15-16 | 48.4 | 3.4 | 6.1 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 59-75 | 44.0 | -3.6 | -4.2 |  |
| follow_move+money_moving | close | pin $1-2k | 210-254 | 45.3 | -4.1 | -12.0 |  |
| follow_move+pin_move | close | pin $1-2k | 218-259 | 45.7 | -4.2 | -11.9 |  |
| follow_move+pin_rlm | close | pin $1-2k | 66-73 | 47.5 | 1.8 | -0.1 |  |
| follow_move+pin_value | close | pin $1-2k | 81-96 | 45.8 | -3.7 | -13.5 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 97-107 | 47.5 | 1.8 | -1.0 |  |
| follow_move+sharp_gap | close | pin $1-2k | 214-254 | 45.7 | -3.6 | -11.3 |  |
| money_moving+pin_move | close | pin $1-2k | 190-212 | 47.3 | -2.0 | -5.1 |  |
| money_moving+pin_rlm | close | pin $1-2k | 77-85 | 47.5 | 2.9 | 7.4 |  |
| money_moving+pin_value | close | pin $1-2k | 90-125 | 41.9 | -6.1 | -17.1 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 95-100 | 48.7 | 2.6 | 1.3 |  |
| money_moving+sharp_gap | close | pin $1-2k | 369-408 | 47.5 | -1.3 | -5.8 |  |
| pin_move+pin_rlm | close | pin $1-2k | 77-83 | 48.1 | 2.9 | 6.4 |  |
| pin_move+pin_value | close | pin $1-2k | 97-122 | 44.3 | -5.5 | -14.9 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 74-76 | 49.3 | 2.7 | 2.4 |  |
| pin_move+sharp_gap | close | pin $1-2k | 192-217 | 46.9 | -1.9 | -5.9 |  |
| pin_rlm+pin_value | close | pin $1-2k | 19-30 | 38.8 | -9.3 | -19.6 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 66-73 | 47.5 | 1.8 | -0.1 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 80-92 | 46.5 | 2.4 | 4.8 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 21-26 | 44.7 | -4.3 | -14.6 |  |
| pin_value+sharp_gap | close | pin $1-2k | 90-122 | 42.5 | -5.5 | -15.9 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 97-107 | 47.5 | 1.8 | -1.0 |  |
| follow_move+money_level | close | pin $1-2k | 227-221 | 50.7 | -3.1 | -11.1 |  |
| money_level+rlm_ratio | close | pin $1-2k | 49-42 | 53.8 | 5.9 | 4.8 |  |
| money_level+sharp_gap | close | pin $1-2k | 270-268 | 50.2 | -1.3 | -7.3 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 5-15 | 25.0 | -15.8 | -30.7 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 79-135 | 36.9 | -6.8 | -18.9 |  |
| money_level+money_moving | close | pin $1-2k | 274-271 | 50.3 | -1.4 | -7.6 |  |
| consensus_gap+money_level | close | pin $1-2k | 80-71 | 53.0 | -3.4 | -7.5 |  |
| money_level+pin_value | close | pin $1-2k | 106-109 | 49.3 | -0.5 | -7.8 |  |
| money_level+pin_move | close | pin $1-2k | 181-180 | 50.1 | -2.2 | -8.6 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 41-64 | 39.0 | -4.9 | -9.8 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 55-80 | 40.7 | -4.6 | -9.8 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 25-43 | 36.8 | -7.3 | -13.8 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 34-55 | 38.2 | -5.1 | -11.0 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 42-66 | 38.9 | -5.0 | -11.9 |  |
| money_level+pin_rlm | close | pin $1-2k | 35-30 | 53.8 | 7.5 | 5.7 |  |
| follow_move+money_delta | close | pin $1-2k | 75-84 | 47.2 | 0.6 | -4.0 |  |
| money_delta+money_moving | close | pin $1-2k | 103-117 | 46.8 | 2.2 | 1.2 |  |
| money_delta+pin_move | close | pin $1-2k | 74-80 | 48.1 | 0.7 | 0.5 |  |
| money_delta+pin_rlm | close | pin $1-2k | 48-54 | 47.1 | 3.1 | 5.5 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 55-56 | 49.5 | 3.9 | 2.9 |  |
| money_delta+sharp_gap | close | pin $1-2k | 103-115 | 47.2 | 2.5 | 2.1 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 46.6 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 53-48 | 52.5 | 4.3 | 2.1 |  |
| consensus_gap+money_delta | close | pin $1-2k | 20-26 | 43.5 | 1.6 | 7.4 |  |
| money_delta+pin_value | close | pin $1-2k | 46-49 | 48.4 | 0.2 | -4.1 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 23-42 | 35.4 | -8.6 | -20.9 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 14-34 | 29.2 | -19.6 | -43.0 |  |
| consensus_gap+follow_move | close | pin $2k+ | 45-36 | 55.6 | 2.0 | -5.8 |  |
| consensus_gap+money_delta | close | pin $2k+ | 13-28 | 31.7 | -4.3 | -35.9 |  |
| consensus_gap+money_level | close | pin $2k+ | 94-69 | 57.7 | -4.3 | -9.3 |  |
| consensus_gap+money_moving | close | pin $2k+ | 51-81 | 38.6 | -7.9 | -6.0 |  |
| consensus_gap+pin_move | close | pin $2k+ | 48-41 | 53.9 | 3.1 | 3.4 |  |
| consensus_gap+pin_value | close | pin $2k+ | 55-60 | 47.8 | 3.5 | 8.3 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 4-15 | 21.1 | -13.7 | -52.3 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 52-85 | 38.0 | -8.9 | -6.5 |  |
| follow_move+money_delta | close | pin $2k+ | 43-57 | 43.0 | 1.8 | -10.9 |  |
| follow_move+money_level | close | pin $2k+ | 179-126 | 58.7 | 0.1 | -6.0 |  |
| follow_move+money_moving | close | pin $2k+ | 152-163 | 48.3 | 0.6 | -7.8 |  |
| follow_move+pin_move | close | pin $2k+ | 198-194 | 50.5 | 0.9 | -4.0 |  |
| follow_move+pin_value | close | pin $2k+ | 45-44 | 50.6 | 2.6 | 6.4 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 53-81 | 39.6 | 1.7 | -12.5 |  |
| follow_move+sharp_gap | close | pin $2k+ | 149-163 | 47.8 | 0.3 | -8.1 |  |
| money_delta+money_level | close | pin $2k+ | 33-26 | 55.9 | 11.6 | 15.7 |  |
| money_delta+money_moving | close | pin $2k+ | 79-111 | 41.6 | 2.2 | -8.9 |  |
| money_delta+pin_move | close | pin $2k+ | 44-62 | 41.5 | -1.2 | -15.6 |  |
| money_delta+pin_value | close | pin $2k+ | 24-26 | 48.0 | 2.5 | -8.4 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 26-41 | 38.8 | 0.7 | -16.9 |  |
| money_delta+sharp_gap | close | pin $2k+ | 77-110 | 41.2 | 1.8 | -9.7 |  |
| money_level+money_moving | close | pin $2k+ | 210-204 | 50.7 | -2.0 | -7.8 |  |
| money_level+pin_move | close | pin $2k+ | 132-117 | 53.0 | -2.6 | -7.6 |  |
| money_level+pin_value | close | pin $2k+ | 70-79 | 47.0 | -2.9 | -13.0 |  |
| money_level+rlm_ratio | close | pin $2k+ | 19-19 | 50.0 | 4.4 | 2.8 |  |
| money_level+sharp_gap | close | pin $2k+ | 207-207 | 50.0 | -2.7 | -8.4 |  |
| money_moving+pin_move | close | pin $2k+ | 131-151 | 46.5 | -0.4 | -7.8 |  |
| money_moving+pin_value | close | pin $2k+ | 74-94 | 44.0 | -2.6 | -3.9 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 53-80 | 39.8 | 1.9 | -11.8 |  |
| money_moving+sharp_gap | close | pin $2k+ | 309-365 | 45.8 | -0.8 | -5.7 |  |
| pin_move+pin_value | close | pin $2k+ | 67-67 | 50.0 | 1.2 | -3.0 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 39-56 | 41.1 | 2.0 | -7.7 |  |
| pin_move+sharp_gap | close | pin $2k+ | 130-153 | 45.9 | -1.0 | -8.2 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 6-7 | 46.2 | 2.0 | -8.8 |  |
| pin_value+sharp_gap | close | pin $2k+ | 74-97 | 43.3 | -3.6 | -5.6 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 53-81 | 39.6 | 1.7 | -12.5 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 9-24 | 27.3 | -6.9 | -13.7 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 7-16 | 30.4 | -1.2 | -31.5 |  |
| follow_move+pin_rlm | close | pin $2k+ | 39-63 | 38.2 | 1.6 | -12.5 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 93-113 | 45.1 | 6.8 | 3.4 |  |
| money_moving+pin_rlm | close | pin $2k+ | 54-91 | 37.2 | 1.0 | -6.4 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 41-62 | 39.8 | 3.7 | -10.4 |  |
| pin_move+pin_rlm | close | pin $2k+ | 44-65 | 40.4 | 2.5 | -7.1 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 61-79 | 43.6 | 3.4 | -3.9 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 21-46 | 31.3 | -1.3 | -23.5 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 39-63 | 38.2 | 1.6 | -12.5 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 54-92 | 37.0 | 0.8 | -7.0 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 28-53 | 34.6 | 1.7 | -18.3 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 40-62 | 39.2 | 3.0 | -12.1 |  |
| money_delta+pin_rlm | close | pin $2k+ | 30-51 | 37.0 | 0.4 | -12.7 |  |
| money_level+pin_rlm | close | pin $2k+ | 17-14 | 54.8 | 10.8 | 15.5 |  |
| pin_rlm+pin_value | close | pin $2k+ | 9-15 | 37.5 | -3.1 | 13.7 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 24-35 | 40.7 | 2.7 | -14.9 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 8-10 | 44.4 | 3.5 | 40.9 |  |
| follow_move+money_delta | close | pin limit <$1k | 37-49 | 43.0 | -6.1 | -17.4 |  |
| money_level+money_moving | close | pin limit <$1k | 100-103 | 49.3 | -0.6 | -5.7 |  |
| money_level+sharp_gap | close | pin limit <$1k | 95-97 | 49.5 | -0.3 | -5.2 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 141-157 | 47.3 | -2.1 | -6.4 |  |
| consensus_gap+money_level | close | pin limit <$1k | 34-31 | 52.3 | 1.6 | -3.0 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 19-14 | 57.6 | 8.9 | 22.0 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 44-43 | 50.6 | 1.0 | 0.3 |  |
| follow_move+money_moving | close | pin limit <$1k | 89-101 | 46.8 | -2.5 | -10.1 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 93-100 | 48.2 | -1.2 | -7.5 |  |
| money_level+pin_move | close | pin limit <$1k | 74-61 | 54.8 | 4.9 | 4.6 |  |
| money_level+pin_value | close | pin limit <$1k | 67-45 | 59.8 | 9.6 | 13.3 |  |
| pin_move+pin_value | close | pin limit <$1k | 56-37 | 60.2 | 10.3 | 19.3 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 23-15 | 60.5 | 11.0 | 12.2 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 28-27 | 50.9 | 2.1 | 4.5 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 30-29 | 50.8 | 1.9 | 3.8 |  |
| follow_move+money_level | close | pin limit <$1k | 80-72 | 52.6 | 2.4 | -0.2 |  |
| follow_move+pin_move | close | pin limit <$1k | 84-82 | 50.6 | 1.1 | -3.0 |  |
| follow_move+pin_value | close | pin limit <$1k | 50-31 | 61.7 | 11.9 | 17.2 |  |
| money_moving+pin_move | close | pin limit <$1k | 79-80 | 49.7 | 0.3 | -2.2 |  |
| money_moving+pin_value | close | pin limit <$1k | 53-42 | 55.8 | 6.2 | 10.6 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 80-80 | 50.0 | 0.7 | -1.6 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 54-47 | 53.5 | 3.8 | 5.9 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 51-55 | 48.1 | -1.2 | -7.6 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 29-37 | 43.9 | -5.1 | -15.8 |  |
| money_delta+money_moving | close | pin limit <$1k | 52-59 | 46.8 | -2.3 | -6.2 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 10-8 | 55.6 | 8.2 | 30.0 |  |
| money_delta+money_level | close | pin limit <$1k | 26-25 | 51.0 | 1.4 | -2.3 |  |
| money_delta+pin_value | close | pin limit <$1k | 19-10 | 65.5 | 16.4 | 39.8 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 51-57 | 47.2 | -1.8 | -5.4 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 33-40 | 45.2 | -3.6 | -7.2 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 7-4 | 63.6 | 17.4 | 61.2 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 27-24 | 52.9 | 4.6 | 10.3 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 46-39 | 54.1 | 5.5 | 14.3 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 48-41 | 53.9 | 5.0 | 8.4 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 20-7 | 74.1 | 25.1 | 57.7 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 49-41 | 54.4 | 5.7 | 14.3 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 7-4 | 63.6 | 15.9 | 21.7 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 16-10 | 61.5 | 11.8 | 17.5 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 12-22 | 35.3 | -13.2 | -32.2 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 26-31 | 45.6 | -3.4 | -12.2 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 39-33 | 54.2 | 5.1 | 4.2 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 54-51 | 51.4 | 2.4 | -0.8 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 30-32 | 48.4 | -0.5 | -7.0 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 23-36 | 39.0 | -10.0 | -25.1 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 49-48 | 50.5 | 1.5 | -2.5 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 39-33 | 54.2 | 5.1 | 4.2 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 15-16 | 48.4 | 0.0 | -6.9 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 39-33 | 54.2 | 5.1 | 4.2 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 24-29 | 45.3 | -3.5 | -13.1 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 54-51 | 51.4 | 2.4 | -0.8 |  |
| money_level+pin_rlm | close | pin limit <$1k | 24-16 | 60.0 | 10.4 | 15.1 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 26-19 | 57.8 | 8.7 | 12.1 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 18-8 | 69.2 | 19.5 | 32.5 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 7-6 | 53.8 | 5.6 | 2.9 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 50.6 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.7 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -52.0 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 53-62 | 46.1 | 9.6 | 12.2 | 0.58 |
| rlm_quiet | early | pin $1-2k | 3-7 | 30.0 | -1.3 | 7.2 | -0.12 |
| rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.9 | -100.0 | 1.3 |
| rlm_quiet | early | pin limit <$1k | 6-9 | 40.0 | -5.4 | -19.3 | 0.28 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.6 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 14-21 | 40.0 | -9.1 | -26.3 | 0.19 |
| pin_move | early | pin $1-2k | 2-9 | 18.2 | -30.9 | -68.6 | 0.27 |
| pin_move | early | pin limit <$1k | 12-16 | 42.9 | -7.0 | -20.2 | 0.44 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 12-11 | 52.2 | 13.4 | 22.6 | 0.98 |
| money_delta | early | pin $1-2k | 0-3 | 0.0 | -37.0 | -100.0 | 2.17 |
| money_delta | early | pin limit <$1k | 5-0 | 100.0 | 50.9 | 88.6 | 0.0 |
| pin_rlm | early | <1k bets | 1-4 | 20.0 | -17.3 | -61.5 | -0.3 |
| pin_rlm | early | pin $1-2k | 0-3 | 0.0 | -43.0 | -100.0 | -0.67 |
| pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 21.1 | -3.7 | 0.25 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.7 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -52.0 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 604-551 | 52.3 | 1.5 | -6.1 | 0.15 |
| follow_move | early | pin $1-2k | 41-32 | 56.2 | 6.4 | 4.5 | -0.34 |
| follow_move | early | pin $2k+ | 0-2 | 0.0 | -41.1 | -100.0 | 0.65 |
| follow_move | early | pin limit <$1k | 60-60 | 50.0 | 0.1 | -5.9 | -0.08 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 22.6 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.4 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 33-29 | 53.2 | 14.4 | 20.8 | 0.52 |
| rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.8 | 29.7 | -1.02 |
| rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -41.1 | -100.0 | 0.65 |
| rlm_ratio | early | pin limit <$1k | 8-2 | 80.0 | 36.5 | 61.1 | 0.33 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 1.7 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 44.3 | 59.7 | 0.33 |
| money_level | early | <1k bets | 214-152 | 58.5 | -0.3 | -7.6 | -0.24 |
| money_level | early | pin $1-2k | 24-13 | 64.9 | 1.5 | -2.9 | -0.05 |
| money_level | early | pin $2k+ | 1-1 | 50.0 | -12.3 | -47.2 | -0.7 |
| money_level | early | pin limit <$1k | 32-32 | 50.0 | -2.0 | -6.9 | 0.24 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.1 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.7 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 173-163 | 51.5 | 2.4 | -1.0 | 0.3 |
| sharp_gap | early | pin $1-2k | 18-17 | 51.4 | -3.8 | -6.9 | -0.3 |
| sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -41.1 | -100.0 | 0.65 |
| sharp_gap | early | pin limit <$1k | 36-23 | 61.0 | 12.4 | 24.5 | 0.16 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.6 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 52.0 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 125-113 | 52.5 | 2.0 | -5.4 | 0.2 |
| money_moving | early | pin $1-2k | 8-13 | 38.1 | -18.8 | -47.8 | 0.36 |
| money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.3 | -8.4 | 0.65 |
| money_moving | early | pin limit <$1k | 33-11 | 75.0 | 25.3 | 53.4 | 0.38 |
| pin_value | early | 1-3k bets | 13-10 | 56.5 | 8.4 | 6.3 | -0.04 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.4 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 58-58 | 50.0 | 1.0 | -5.4 | 0.11 |
| pin_value | early | pin $1-2k | 19-30 | 38.8 | -8.5 | -27.1 | 0.19 |
| pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.4 | 83.3 | 0.0 |
| pin_value | early | pin limit <$1k | 53-39 | 57.6 | 7.9 | 9.1 | 0.05 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -50.6 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -27.4 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.0 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.3 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 291-343 | 45.9 | -3.9 | -12.8 | 0.44 |
| consensus_gap | early | pin $1-2k | 22-25 | 46.8 | -0.5 | -11.9 | 0.29 |
| consensus_gap | early | pin $2k+ | 1-1 | 50.0 | 12.3 | -8.4 | 0.65 |
| consensus_gap | early | pin limit <$1k | 26-38 | 40.6 | -9.5 | -17.9 | 0.24 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -53.4 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -2.0 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.9 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 5.6 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.3 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 7-4 | 63.6 | 14.4 | 19.4 | -0.09 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.0 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.9 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.6 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -0.5 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 6-5 | 54.5 | 8.6 | 1.3 | 0.27 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -1.4 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-7 | 50.0 | 3.1 | -6.4 | -0.29 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.7 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.7 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -19.7 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -3.0 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 3.7 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.6 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 22.6 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.2 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 22.6 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.4 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.4 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.4 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.4 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 53.4 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 11.3 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 17.8 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 15.7 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 15.7 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -28.9 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 53.4 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 53.4 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.4 | 83.3 | 1.0 |
| follow_move+rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -52.0 | -100.0 | -0.5 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.4 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.4 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 52.0 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.4 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.4 | 83.3 | 1.0 |
| rlm_quiet+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.4 | -100.0 | -1.0 |
| rlm_quiet+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.4 | -100.0 | -1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.4 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 39.7 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 50.6 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 42-54 | 43.8 | -9.9 | -22.8 | 0.92 |
| consensus_gap+money_level | early | <1k bets | 52-40 | 56.5 | -7.4 | -13.0 | -0.03 |
| consensus_gap+sharp_gap | early | <1k bets | 37-54 | 40.7 | -10.1 | -20.4 | 0.54 |
| follow_move+money_level | early | <1k bets | 102-52 | 66.2 | 6.4 | -1.9 | 0.08 |
| follow_move+sharp_gap | early | <1k bets | 87-54 | 61.7 | 12.3 | 12.2 | 0.57 |
| money_level+sharp_gap | early | <1k bets | 117-85 | 57.9 | 1.8 | -4.9 | 0.03 |
| follow_move+money_moving | early | <1k bets | 60-42 | 58.8 | 7.4 | 6.5 | 0.46 |
| money_level+money_moving | early | <1k bets | 71-52 | 57.7 | 0.3 | -6.4 | -0.05 |
| money_moving+sharp_gap | early | <1k bets | 72-69 | 51.1 | 2.9 | -3.3 | 0.39 |
| consensus_gap+money_moving | early | <1k bets | 20-25 | 44.4 | -6.8 | -28.7 | 0.58 |
| follow_move+pin_value | early | <1k bets | 18-16 | 52.9 | 3.3 | -0.3 | -0.1 |
| follow_move+rlm_quiet | early | <1k bets | 53-62 | 46.1 | 9.6 | 12.2 | 0.58 |
| money_moving+rlm_quiet | early | <1k bets | 18-18 | 50.0 | 12.7 | 22.1 | 0.69 |
| rlm_quiet+sharp_gap | early | <1k bets | 26-23 | 53.1 | 15.5 | 22.9 | 0.32 |
| follow_move+rlm_ratio | early | <1k bets | 33-29 | 53.2 | 14.4 | 20.8 | 0.52 |
| rlm_quiet+rlm_ratio | early | <1k bets | 23-17 | 57.5 | 20.5 | 36.2 | 0.16 |
| rlm_ratio+sharp_gap | early | <1k bets | 33-29 | 53.2 | 14.4 | 20.8 | 0.52 |
| pin_move+pin_value | early | <1k bets | 5-11 | 31.2 | -18.2 | -39.8 | 0.44 |
| follow_move+pin_move | early | <1k bets | 9-10 | 47.4 | -1.7 | -12.6 | 0.49 |
| consensus_gap+pin_value | early | <1k bets | 23-26 | 46.9 | -0.6 | -11.8 | 0.25 |
| pin_value+rlm_quiet | early | <1k bets | 0-3 | 0.0 | -43.9 | -100.0 | -0.6 |
| money_delta+money_moving | early | <1k bets | 11-11 | 50.0 | 11.8 | 19.5 | 1.02 |
| money_delta+sharp_gap | early | <1k bets | 10-9 | 52.6 | 15.1 | 28.3 | 1.18 |
| consensus_gap+pin_move | early | <1k bets | 2-6 | 25.0 | -21.9 | -51.7 | 0.29 |
| money_level+pin_move | early | <1k bets | 4-6 | 40.0 | -10.0 | -30.2 | 0.14 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -28.9 | -100.0 | -4.8 |
| consensus_gap+rlm_quiet | early | <1k bets | 4-6 | 40.0 | 2.9 | -12.2 | 1.03 |
| consensus_gap+rlm_ratio | early | <1k bets | 5-3 | 62.5 | 20.8 | 25.0 | 0.65 |
| follow_move+pin_rlm | early | <1k bets | 1-3 | 25.0 | -14.4 | -51.8 | -0.7 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -28.9 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | <1k bets | 0-1 | 0.0 | -28.9 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-3 | 25.0 | -14.4 | -51.8 | -0.7 |
| pin_rlm+sharp_gap | early | <1k bets | 1-4 | 20.0 | -17.3 | -61.5 | -0.3 |
| pin_value+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 24.1 | 27.3 | -0.93 |
| pin_value+sharp_gap | early | <1k bets | 6-8 | 42.9 | -7.2 | -18.2 | 0.42 |
| money_level+pin_value | early | <1k bets | 7-7 | 50.0 | -1.7 | -4.5 | 0.84 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -51.4 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -49.4 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 4-4 | 50.0 | -3.3 | -4.0 | 1.21 |
| money_level+rlm_ratio | early | <1k bets | 8-12 | 40.0 | -1.5 | -17.1 | 1.32 |
| money_moving+rlm_ratio | early | <1k bets | 16-11 | 59.3 | 18.9 | 39.9 | 0.95 |
| consensus_gap+money_delta | early | <1k bets | 2-0 | 100.0 | 50.0 | 90.9 | 0.5 |
| money_delta+money_level | early | <1k bets | 4-4 | 50.0 | 8.2 | 4.6 | 1.44 |
| pin_move+sharp_gap | early | <1k bets | 2-4 | 33.3 | -13.4 | -47.8 | 0.47 |
| money_level+pin_rlm | early | <1k bets | 1-2 | 33.3 | -9.6 | -35.8 | 0.67 |
| pin_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 21.1 | -3.7 | 0.25 |
| pin_move+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 21.1 | -3.7 | 0.25 |
| follow_move+money_delta | early | <1k bets | 6-5 | 54.5 | 16.4 | 52.8 | 1.28 |
| money_delta+rlm_quiet | early | <1k bets | 3-3 | 50.0 | 17.7 | 72.5 | 0.38 |
| money_delta+rlm_ratio | early | <1k bets | 5-3 | 62.5 | 25.9 | 86.2 | 2.04 |
| money_delta+pin_value | early | <1k bets | 2-0 | 100.0 | 50.6 | 90.9 | 0.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -28.9 | -100.0 | 1.3 |
| money_moving+pin_move | early | <1k bets | 1-1 | 50.0 | 0.6 | -2.4 | 1.0 |
| consensus_gap+money_level | early | pin $1-2k | 7-5 | 58.3 | -6.7 | -9.8 | 0.07 |
| consensus_gap+money_moving | early | pin $1-2k | 1-3 | 25.0 | -40.0 | -54.2 | 0.95 |
| consensus_gap+pin_value | early | pin $1-2k | 8-11 | 42.1 | -0.9 | -22.3 | 0.14 |
| follow_move+rlm_quiet | early | pin $1-2k | 3-7 | 30.0 | -1.3 | 7.2 | -0.12 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.8 | 29.7 | -1.02 |
| follow_move+sharp_gap | early | pin $1-2k | 9-6 | 60.0 | 3.0 | 19.2 | -0.62 |
| money_level+money_moving | early | pin $1-2k | 8-8 | 50.0 | -12.8 | -31.4 | 0.26 |
| money_level+pin_value | early | pin $1-2k | 2-4 | 33.3 | -18.5 | -37.6 | 0.78 |
| money_moving+pin_value | early | pin $1-2k | 1-4 | 20.0 | -34.8 | -63.3 | 0.94 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -10.0 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -10.0 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -10.8 | 29.7 | -1.02 |
| money_delta+money_level | early | pin $1-2k | 0-2 | 0.0 | -41.1 | -100.0 | 1.25 |
| money_delta+money_moving | early | pin $1-2k | 0-3 | 0.0 | -37.0 | -100.0 | 2.17 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -53.4 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-3 | 0.0 | -37.0 | -100.0 | 2.17 |
| money_level+sharp_gap | early | pin $1-2k | 15-9 | 62.5 | -0.7 | -4.8 | -0.23 |
| money_moving+sharp_gap | early | pin $1-2k | 4-10 | 28.6 | -27.5 | -61.0 | 0.36 |
| pin_value+sharp_gap | early | pin $1-2k | 1-4 | 20.0 | -30.7 | -61.8 | -0.22 |
| consensus_gap+follow_move | early | pin $1-2k | 6-7 | 46.2 | -2.2 | -11.3 | 0.4 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 1-3 | 25.0 | -3.9 | -35.0 | -0.65 |
| follow_move+pin_value | early | pin $1-2k | 6-8 | 42.9 | -5.1 | -20.8 | -0.24 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -28.9 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 12-6 | 66.7 | 3.3 | -0.4 | -0.03 |
| money_level+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -12.3 | -1.0 | 0.75 |
| follow_move+money_moving | early | pin $1-2k | 4-3 | 57.1 | -7.4 | -23.6 | -0.13 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -28.9 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -28.9 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 4-5 | 44.4 | -12.6 | -31.7 | -0.69 |
| follow_move+pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -28.9 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | pin $1-2k | 0-1 | 0.0 | -28.9 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-3 | 0.0 | -43.0 | -100.0 | -0.67 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -28.9 | -100.0 | -4.8 |
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -28.9 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -28.9 | -100.0 | 1.3 |
| pin_move+pin_value | early | pin $1-2k | 0-4 | 0.0 | -48.3 | -100.0 | 0.5 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -71.1 | -100.0 | 1.5 |
| follow_move+pin_move | early | pin $1-2k | 1-2 | 33.3 | -15.5 | -35.2 | -0.33 |
| money_level+pin_move | early | pin $1-2k | 1-0 | 100.0 | 53.4 | 94.3 | -1.0 |
| consensus_gap+money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.3 | -8.4 | 0.65 |
| consensus_gap+pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.4 | 83.3 | 0.0 |
| follow_move+money_level | early | pin $2k+ | 0-1 | 0.0 | -53.4 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -41.1 | -100.0 | 0.65 |
| follow_move+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -41.1 | -100.0 | 0.65 |
| money_level+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -53.4 | -100.0 | 0.0 |
| money_level+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -53.4 | -100.0 | 0.0 |
| money_moving+pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.4 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -41.1 | -100.0 | 0.65 |
| consensus_gap+follow_move | early | pin $2k+ | 0-1 | 0.0 | -28.9 | -100.0 | 1.3 |
| consensus_gap+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.9 | -100.0 | 1.3 |
| consensus_gap+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.9 | -100.0 | 1.3 |
| consensus_gap+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.9 | -100.0 | 1.3 |
| follow_move+money_moving | early | pin $2k+ | 0-1 | 0.0 | -28.9 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.9 | -100.0 | 1.3 |
| money_moving+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.9 | -100.0 | 1.3 |
| money_moving+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.9 | -100.0 | 1.3 |
| money_moving+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.9 | -100.0 | 1.3 |
| rlm_quiet+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.9 | -100.0 | 1.3 |
| rlm_quiet+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.9 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin limit <$1k | 6-9 | 40.0 | -5.4 | -19.3 | 0.28 |
| money_level+money_moving | early | pin limit <$1k | 18-7 | 72.0 | 20.5 | 34.3 | 0.42 |
| money_level+sharp_gap | early | pin limit <$1k | 26-20 | 56.5 | 6.6 | 4.5 | 0.22 |
| money_moving+sharp_gap | early | pin limit <$1k | 24-6 | 80.0 | 31.5 | 68.6 | 0.27 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -50.6 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 13-8 | 61.9 | 11.9 | 17.4 | 0.33 |
| money_moving+pin_value | early | pin limit <$1k | 11-4 | 73.3 | 23.7 | 39.0 | 0.27 |
| pin_value+sharp_gap | early | pin limit <$1k | 14-8 | 63.6 | 13.8 | 20.6 | 0.14 |
| consensus_gap+follow_move | early | pin limit <$1k | 7-10 | 41.2 | -10.0 | -23.2 | 0.41 |
| consensus_gap+money_level | early | pin limit <$1k | 6-7 | 46.2 | -8.2 | -19.0 | 0.31 |
| consensus_gap+pin_value | early | pin limit <$1k | 21-20 | 51.2 | 2.0 | -3.4 | 0.33 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 7-4 | 63.6 | 18.2 | 56.6 | 0.91 |
| follow_move+money_level | early | pin limit <$1k | 14-14 | 50.0 | -1.8 | -6.7 | -0.03 |
| follow_move+pin_value | early | pin limit <$1k | 19-15 | 55.9 | 6.7 | 5.6 | -0.12 |
| follow_move+sharp_gap | early | pin limit <$1k | 16-10 | 61.5 | 13.6 | 17.7 | -0.02 |
| follow_move+rlm_ratio | early | pin limit <$1k | 8-2 | 80.0 | 36.5 | 61.1 | 0.33 |
| money_level+rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.1 | 68.3 | 0.44 |
| pin_value+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.3 | 43.2 | -0.25 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 8-2 | 80.0 | 36.5 | 61.1 | 0.33 |
| consensus_gap+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 51.1 | 87.1 | 0.33 |
| consensus_gap+money_moving | early | pin limit <$1k | 10-3 | 76.9 | 29.2 | 76.9 | 0.65 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 2.0 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 51.1 | 87.1 | 0.33 |
| follow_move+money_moving | early | pin limit <$1k | 13-5 | 72.2 | 23.0 | 38.2 | 0.39 |
| money_delta+money_moving | early | pin limit <$1k | 4-0 | 100.0 | 51.0 | 88.0 | 0.0 |
| money_delta+pin_value | early | pin limit <$1k | 4-0 | 100.0 | 51.0 | 88.0 | 0.0 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 53.4 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 4-2 | 66.7 | 17.5 | 26.0 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 30.1 | 54.4 | -0.2 |
| money_delta+sharp_gap | early | pin limit <$1k | 3-0 | 100.0 | 50.2 | 89.6 | 0.0 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 10.3 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | 5.4 | 13.7 | -0.05 |
| pin_move+pin_value | early | pin limit <$1k | 5-8 | 38.5 | -11.2 | -25.9 | 0.54 |
| follow_move+pin_move | early | pin limit <$1k | 8-9 | 47.1 | -2.1 | -13.7 | 0.67 |
| consensus_gap+pin_move | early | pin limit <$1k | 2-4 | 33.3 | -19.6 | -35.7 | 0.43 |
| money_level+pin_move | early | pin limit <$1k | 3-6 | 33.3 | -17.0 | -44.0 | 0.27 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -49.4 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -49.4 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-4 | 33.3 | -13.4 | -47.8 | 0.47 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 21.1 | -3.7 | 0.25 |
| money_level+pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 21.1 | -3.7 | 0.25 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 21.1 | -3.7 | 0.25 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 21.1 | -3.7 | 0.25 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 21.1 | -3.7 | 0.25 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 21.1 | -3.7 | 0.25 |
| money_delta+money_level | early | pin limit <$1k | 2-0 | 100.0 | 50.6 | 90.9 | 0.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 50.6 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 50.6 | 90.9 | 1.0 |
| money_moving+pin_move | early | pin limit <$1k | 1-1 | 50.0 | 0.6 | -2.4 | 1.0 |
| pin_move+rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -49.4 | -100.0 | 1.0 |
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
| rlm_quiet | close | 1-3k bets | 73-112 | 39.5 | -3.8 | -8.3 |  |
| rlm_quiet | close | 3k+ bets | 34-50 | 40.5 | -2.3 | -15.3 |  |
| rlm_quiet | close | <1k bets | 10-19 | 34.5 | -8.7 | -33.2 |  |
| rlm_quiet | close | pin $1-2k | 33-54 | 37.9 | -6.7 | -21.1 |  |
| rlm_quiet | close | pin $2k+ | 40-50 | 44.4 | 3.4 | 10.0 |  |
| rlm_quiet | close | pin limit <$1k | 15-19 | 44.1 | -3.4 | -14.9 |  |
| pin_move | close | 1-3k bets | 132-139 | 48.7 | -0.4 | -2.4 |  |
| pin_move | close | 3k+ bets | 56-64 | 46.7 | -3.6 | -11.1 |  |
| pin_move | close | <1k bets | 20-19 | 51.3 | 1.6 | -3.3 |  |
| pin_move | close | pin $1-2k | 86-105 | 45.0 | -4.3 | -11.7 |  |
| pin_move | close | pin $2k+ | 86-87 | 49.7 | -0.1 | -1.0 |  |
| pin_move | close | pin limit <$1k | 36-33 | 52.2 | 2.8 | -0.1 |  |
| money_delta | close | 1-3k bets | 62-84 | 42.5 | -1.4 | -11.7 |  |
| money_delta | close | 3k+ bets | 33-37 | 47.1 | 2.4 | -4.1 |  |
| money_delta | close | <1k bets | 14-14 | 50.0 | 5.4 | 11.4 |  |
| money_delta | close | pin $1-2k | 41-39 | 51.2 | 5.0 | 5.2 |  |
| money_delta | close | pin $2k+ | 28-31 | 47.5 | 5.8 | -0.7 |  |
| money_delta | close | pin limit <$1k | 12-19 | 38.7 | -8.3 | -25.5 |  |
| pin_rlm | close | 1-3k bets | 27-41 | 39.7 | -2.0 | -14.1 |  |
| pin_rlm | close | 3k+ bets | 11-18 | 37.9 | -4.6 | -21.9 |  |
| pin_rlm | close | <1k bets | 5-5 | 50.0 | 2.5 | -4.9 |  |
| pin_rlm | close | pin $1-2k | 19-26 | 42.2 | -1.8 | -12.4 |  |
| pin_rlm | close | pin $2k+ | 16-26 | 38.1 | -0.2 | -14.9 |  |
| pin_rlm | close | pin limit <$1k | 8-12 | 40.0 | -7.4 | -23.0 |  |
| follow_move | close | 1-3k bets | 207-238 | 46.5 | -2.6 | -8.5 |  |
| follow_move | close | 3k+ bets | 90-88 | 50.6 | 1.6 | -5.8 |  |
| follow_move | close | <1k bets | 44-46 | 48.9 | -0.9 | -13.1 |  |
| follow_move | close | pin $1-2k | 101-128 | 44.1 | -5.0 | -16.4 |  |
| follow_move | close | pin $2k+ | 103-104 | 49.8 | 0.6 | 0.1 |  |
| follow_move | close | pin limit <$1k | 44-41 | 51.8 | 2.1 | -1.8 |  |
| rlm_ratio | close | 1-3k bets | 48-77 | 38.4 | -4.1 | -16.1 |  |
| rlm_ratio | close | 3k+ bets | 17-32 | 34.7 | -7.9 | -28.6 |  |
| rlm_ratio | close | <1k bets | 10-12 | 45.5 | 1.1 | -12.8 |  |
| rlm_ratio | close | pin $1-2k | 27-34 | 44.3 | -0.1 | -9.3 |  |
| rlm_ratio | close | pin $2k+ | 15-28 | 34.9 | -3.0 | -22.9 |  |
| rlm_ratio | close | pin limit <$1k | 10-17 | 37.0 | -10.5 | -28.9 |  |
| money_level | close | 1-3k bets | 268-209 | 56.2 | 1.3 | -4.3 |  |
| money_level | close | 3k+ bets | 108-97 | 52.7 | -1.5 | -8.0 |  |
| money_level | close | <1k bets | 60-31 | 65.9 | 11.2 | 9.2 |  |
| money_level | close | pin $1-2k | 128-120 | 51.6 | -1.7 | -9.4 |  |
| money_level | close | pin $2k+ | 114-107 | 51.6 | -4.3 | -13.6 |  |
| money_level | close | pin limit <$1k | 54-37 | 59.3 | 7.6 | 12.1 |  |
| sharp_gap | close | 1-3k bets | 208-240 | 46.4 | -2.0 | -10.4 |  |
| sharp_gap | close | 3k+ bets | 81-113 | 41.8 | -6.6 | -18.9 |  |
| sharp_gap | close | <1k bets | 46-39 | 54.1 | 4.9 | -0.8 |  |
| sharp_gap | close | pin $1-2k | 109-121 | 47.4 | -1.3 | -8.8 |  |
| sharp_gap | close | pin $2k+ | 91-120 | 43.1 | -4.6 | -14.6 |  |
| sharp_gap | close | pin limit <$1k | 38-47 | 44.7 | -4.9 | -14.6 |  |
| money_moving | close | 1-3k bets | 218-235 | 48.1 | -0.6 | -7.5 |  |
| money_moving | close | 3k+ bets | 84-111 | 43.1 | -5.9 | -18.2 |  |
| money_moving | close | <1k bets | 46-37 | 55.4 | 6.0 | 1.5 |  |
| money_moving | close | pin $1-2k | 114-117 | 49.4 | 0.1 | -6.2 |  |
| money_moving | close | pin $2k+ | 95-117 | 44.8 | -3.0 | -12.1 |  |
| money_moving | close | pin limit <$1k | 42-48 | 46.7 | -2.9 | -10.9 |  |
| pin_value | close | 1-3k bets | 111-93 | 54.4 | 4.6 | 8.3 |  |
| pin_value | close | 3k+ bets | 25-50 | 33.3 | -17.2 | -36.7 |  |
| pin_value | close | <1k bets | 18-14 | 56.2 | 9.1 | 17.6 |  |
| pin_value | close | pin $1-2k | 72-75 | 49.0 | -0.4 | -3.7 |  |
| pin_value | close | pin $2k+ | 47-54 | 46.5 | -2.8 | -2.3 |  |
| pin_value | close | pin limit <$1k | 37-29 | 56.1 | 5.4 | 6.6 |  |
| consensus_gap | close | 1-3k bets | 87-72 | 54.7 | 2.4 | 0.1 |  |
| consensus_gap | close | 3k+ bets | 35-31 | 53.0 | -2.0 | -8.3 |  |
| consensus_gap | close | <1k bets | 18-8 | 69.2 | 18.6 | 29.9 |  |
| consensus_gap | close | pin $1-2k | 31-29 | 51.7 | -0.3 | 3.6 |  |
| consensus_gap | close | pin $2k+ | 61-31 | 66.3 | 10.0 | 19.8 |  |
| consensus_gap | close | pin limit <$1k | 10-13 | 43.5 | -5.4 | -17.1 |  |
| follow_move+pin_move | close | 1-3k bets | 85-113 | 42.9 | -5.8 | -15.7 |  |
| money_delta+money_moving | close | 1-3k bets | 50-64 | 43.9 | 1.2 | -7.1 |  |
| money_delta+sharp_gap | close | 1-3k bets | 50-63 | 44.2 | 1.7 | -6.3 |  |
| money_moving+sharp_gap | close | 1-3k bets | 202-226 | 47.2 | -1.3 | -8.5 |  |
| consensus_gap+money_level | close | 1-3k bets | 54-39 | 58.1 | 0.0 | -8.1 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 73-112 | 39.5 | -3.8 | -8.3 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 32-53 | 37.6 | -6.5 | -16.7 |  |
| consensus_gap+follow_move | close | 1-3k bets | 22-26 | 45.8 | -4.2 | -14.8 |  |
| follow_move+money_level | close | 1-3k bets | 101-88 | 53.4 | -1.3 | -7.5 |  |
| money_level+money_moving | close | 1-3k bets | 151-134 | 53.0 | 0.5 | -4.7 |  |
| money_level+sharp_gap | close | 1-3k bets | 143-134 | 51.6 | -0.7 | -6.7 |  |
| consensus_gap+money_moving | close | 1-3k bets | 27-36 | 42.9 | -7.3 | -17.6 |  |
| consensus_gap+pin_move | close | 1-3k bets | 23-14 | 62.2 | 13.1 | 36.6 |  |
| consensus_gap+pin_value | close | 1-3k bets | 29-28 | 50.9 | 1.9 | -3.6 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 27-38 | 41.5 | -8.3 | -20.3 |  |
| follow_move+money_moving | close | 1-3k bets | 109-132 | 45.2 | -3.0 | -10.8 |  |
| follow_move+pin_value | close | 1-3k bets | 35-28 | 55.6 | 5.3 | 20.5 |  |
| follow_move+sharp_gap | close | 1-3k bets | 109-135 | 44.7 | -3.5 | -12.2 |  |
| money_level+pin_move | close | 1-3k bets | 60-50 | 54.5 | 1.4 | -2.2 |  |
| money_level+pin_value | close | 1-3k bets | 47-41 | 53.4 | 3.0 | 0.1 |  |
| money_moving+pin_move | close | 1-3k bets | 65-64 | 50.4 | 2.3 | -1.2 |  |
| money_moving+pin_value | close | 1-3k bets | 41-42 | 49.4 | -0.2 | -6.8 |  |
| pin_move+pin_value | close | 1-3k bets | 40-39 | 50.6 | -0.7 | -4.2 |  |
| pin_move+sharp_gap | close | 1-3k bets | 62-70 | 47.0 | -0.7 | -7.8 |  |
| pin_value+sharp_gap | close | 1-3k bets | 40-45 | 47.1 | -2.7 | -11.3 |  |
| follow_move+money_delta | close | 1-3k bets | 35-56 | 38.5 | -5.5 | -18.6 |  |
| money_delta+pin_move | close | 1-3k bets | 22-27 | 44.9 | 1.4 | -11.2 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 19-40 | 32.2 | -9.9 | -26.9 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 48-77 | 38.4 | -4.1 | -16.1 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 32-58 | 35.6 | -5.7 | -17.1 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 47-71 | 39.8 | -2.8 | -12.8 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 23-54 | 29.9 | -10.5 | -27.2 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 31-61 | 33.7 | -7.7 | -21.7 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 48-77 | 38.4 | -4.1 | -16.1 |  |
| money_delta+money_level | close | 1-3k bets | 18-16 | 52.9 | 5.7 | 3.9 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 6-12 | 33.3 | -6.1 | -25.0 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 8-8 | 50.0 | 8.7 | 7.4 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 25-45 | 35.7 | -6.3 | -21.5 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 5-3 | 62.5 | 20.1 | 47.4 |  |
| money_level+pin_rlm | close | 1-3k bets | 10-10 | 50.0 | 4.5 | -2.2 |  |
| money_moving+pin_rlm | close | 1-3k bets | 27-36 | 42.9 | 0.8 | -7.3 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 27-41 | 39.7 | -2.0 | -14.1 |  |
| money_level+rlm_ratio | close | 1-3k bets | 20-18 | 52.6 | 6.0 | 2.2 |  |
| consensus_gap+money_delta | close | 1-3k bets | 9-6 | 60.0 | 18.5 | 19.1 |  |
| follow_move+pin_rlm | close | 1-3k bets | 22-35 | 38.6 | -2.8 | -15.6 |  |
| money_delta+pin_rlm | close | 1-3k bets | 15-22 | 40.5 | -0.4 | -18.4 |  |
| pin_move+pin_rlm | close | 1-3k bets | 26-35 | 42.6 | 0.6 | -8.1 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 23-32 | 41.8 | -0.7 | -10.0 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 11-26 | 29.7 | -9.9 | -27.7 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 22-35 | 38.6 | -2.8 | -15.6 |  |
| money_delta+pin_value | close | 1-3k bets | 13-7 | 65.0 | 17.6 | 25.6 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 8-10 | 44.4 | -2.6 | 41.6 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 5-5 | 50.0 | 2.1 | -1.2 |  |
| pin_rlm+pin_value | close | 1-3k bets | 4-6 | 40.0 | -8.3 | -19.3 |  |
| money_level+money_moving | close | 3k+ bets | 51-61 | 45.5 | -6.9 | -16.5 |  |
| money_level+sharp_gap | close | 3k+ bets | 47-61 | 43.5 | -8.4 | -17.9 |  |
| money_moving+sharp_gap | close | 3k+ bets | 80-109 | 42.3 | -6.2 | -18.2 |  |
| follow_move+money_delta | close | 3k+ bets | 15-22 | 40.5 | -3.3 | -18.4 |  |
| follow_move+money_level | close | 3k+ bets | 39-30 | 56.5 | 1.3 | -7.1 |  |
| follow_move+money_moving | close | 3k+ bets | 47-55 | 46.1 | -2.4 | -15.3 |  |
| follow_move+pin_move | close | 3k+ bets | 44-48 | 47.8 | -1.8 | -8.6 |  |
| follow_move+pin_rlm | close | 3k+ bets | 10-15 | 40.0 | -1.2 | -16.9 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 17-32 | 34.7 | -7.9 | -28.6 |  |
| follow_move+sharp_gap | close | 3k+ bets | 44-54 | 44.9 | -2.7 | -14.0 |  |
| money_delta+money_level | close | 3k+ bets | 9-9 | 50.0 | 1.4 | 4.8 |  |
| money_delta+money_moving | close | 3k+ bets | 23-29 | 44.2 | 0.3 | -9.4 |  |
| money_delta+pin_move | close | 3k+ bets | 10-13 | 43.5 | -3.3 | -15.5 |  |
| money_delta+pin_rlm | close | 3k+ bets | 7-9 | 43.8 | -1.0 | -12.0 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 8-13 | 38.1 | -3.6 | -23.5 |  |
| money_delta+sharp_gap | close | 3k+ bets | 23-29 | 44.2 | 0.3 | -9.4 |  |
| money_level+pin_move | close | 3k+ bets | 20-27 | 42.6 | -12.7 | -27.3 |  |
| money_level+pin_rlm | close | 3k+ bets | 1-3 | 25.0 | -26.9 | -51.2 |  |
| money_level+rlm_ratio | close | 3k+ bets | 3-5 | 37.5 | -11.8 | -27.9 |  |
| money_moving+pin_move | close | 3k+ bets | 25-36 | 41.0 | -8.9 | -23.6 |  |
| money_moving+pin_rlm | close | 3k+ bets | 11-17 | 39.3 | -3.5 | -19.1 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 16-32 | 33.3 | -9.5 | -32.7 |  |
| pin_move+pin_rlm | close | 3k+ bets | 9-15 | 37.5 | -6.9 | -25.4 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 9-15 | 37.5 | -6.2 | -25.3 |  |
| pin_move+sharp_gap | close | 3k+ bets | 23-36 | 39.0 | -10.3 | -25.0 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 10-15 | 40.0 | -1.2 | -16.9 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 11-18 | 37.9 | -4.6 | -21.9 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 17-32 | 34.7 | -7.9 | -28.6 |  |
| consensus_gap+money_level | close | 3k+ bets | 26-18 | 59.1 | -0.1 | -1.0 |  |
| consensus_gap+money_moving | close | 3k+ bets | 14-21 | 40.0 | -12.2 | -26.6 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 13-22 | 37.1 | -14.1 | -29.9 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 34-50 | 40.5 | -2.3 | -15.3 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 19-25 | 43.2 | -0.3 | -8.8 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 9-15 | 37.5 | -3.8 | -21.9 |  |
| money_level+pin_value | close | 3k+ bets | 14-28 | 33.3 | -18.3 | -37.2 |  |
| money_moving+pin_value | close | 3k+ bets | 13-27 | 32.5 | -19.1 | -38.8 |  |
| pin_value+sharp_gap | close | 3k+ bets | 13-28 | 31.7 | -20.3 | -40.3 |  |
| consensus_gap+follow_move | close | 3k+ bets | 13-10 | 56.5 | 3.2 | -6.5 |  |
| consensus_gap+pin_value | close | 3k+ bets | 10-11 | 47.6 | -4.6 | -9.4 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 17-31 | 35.4 | -8.1 | -29.5 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 18-30 | 37.5 | -5.7 | -23.8 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 6-14 | 30.0 | -10.1 | -36.6 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 11-26 | 29.7 | -11.6 | -37.6 |  |
| pin_move+pin_value | close | 3k+ bets | 16-25 | 39.0 | -12.2 | -26.0 |  |
| follow_move+pin_value | close | 3k+ bets | 11-18 | 37.9 | -12.1 | -28.1 |  |
| consensus_gap+money_delta | close | 3k+ bets | 4-4 | 50.0 | 6.1 | 6.7 |  |
| consensus_gap+pin_move | close | 3k+ bets | 14-10 | 58.3 | 5.1 | 2.5 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 3-4 | 42.9 | -0.6 | -17.6 |  |
| money_delta+pin_value | close | 3k+ bets | 4-6 | 40.0 | -13.3 | -23.6 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 3-8 | 27.3 | -22.6 | -48.5 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 2-4 | 33.3 | -13.3 | -36.9 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 1-4 | 20.0 | -20.1 | -61.8 |  |
| pin_rlm+pin_value | close | 3k+ bets | 2-4 | 33.3 | -19.4 | -36.9 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 1-3 | 25.0 | -23.6 | -52.3 |  |
| consensus_gap+money_level | close | <1k bets | 13-1 | 92.9 | 35.6 | 48.5 |  |
| consensus_gap+money_moving | close | <1k bets | 8-1 | 88.9 | 36.0 | 81.0 |  |
| consensus_gap+pin_value | close | <1k bets | 5-2 | 71.4 | 28.9 | 85.8 |  |
| consensus_gap+sharp_gap | close | <1k bets | 9-2 | 81.8 | 29.4 | 60.9 |  |
| follow_move+pin_move | close | <1k bets | 14-15 | 48.3 | -1.8 | -9.0 |  |
| follow_move+rlm_quiet | close | <1k bets | 10-19 | 34.5 | -8.7 | -33.2 |  |
| money_level+money_moving | close | <1k bets | 34-18 | 65.4 | 12.4 | 10.0 |  |
| money_level+pin_value | close | <1k bets | 8-4 | 66.7 | 18.7 | 24.9 |  |
| money_level+sharp_gap | close | <1k bets | 34-19 | 64.2 | 10.9 | 8.1 |  |
| money_moving+pin_value | close | <1k bets | 6-5 | 54.5 | 9.8 | 36.2 |  |
| money_moving+sharp_gap | close | <1k bets | 44-36 | 55.0 | 6.0 | 2.4 |  |
| pin_move+rlm_quiet | close | <1k bets | 3-4 | 42.9 | -5.9 | -18.6 |  |
| pin_value+sharp_gap | close | <1k bets | 6-5 | 54.5 | 9.8 | 36.2 |  |
| follow_move+money_moving | close | <1k bets | 22-18 | 55.0 | 5.8 | -3.6 |  |
| follow_move+sharp_gap | close | <1k bets | 21-19 | 52.5 | 3.3 | -5.9 |  |
| money_level+pin_move | close | <1k bets | 14-9 | 60.9 | 10.6 | 14.1 |  |
| money_moving+rlm_quiet | close | <1k bets | 5-7 | 41.7 | -1.5 | -19.1 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 5-7 | 41.7 | -1.5 | -19.1 |  |
| follow_move+money_delta | close | <1k bets | 8-9 | 47.1 | 1.6 | -10.3 |  |
| follow_move+pin_rlm | close | <1k bets | 4-5 | 44.4 | -3.1 | -15.5 |  |
| follow_move+pin_value | close | <1k bets | 5-3 | 62.5 | 13.2 | 19.9 |  |
| follow_move+rlm_ratio | close | <1k bets | 10-12 | 45.5 | 1.1 | -12.8 |  |
| money_delta+money_moving | close | <1k bets | 9-11 | 45.0 | 2.7 | 8.2 |  |
| money_delta+pin_move | close | <1k bets | 1-3 | 25.0 | -22.3 | -52.3 |  |
| money_delta+pin_rlm | close | <1k bets | 1-3 | 25.0 | -22.3 | -52.3 |  |
| money_delta+pin_value | close | <1k bets | 4-0 | 100.0 | 56.1 | 181.8 |  |
| money_delta+rlm_quiet | close | <1k bets | 5-4 | 55.6 | 11.8 | 7.3 |  |
| money_delta+rlm_ratio | close | <1k bets | 5-7 | 41.7 | -1.9 | -20.7 |  |
| money_delta+sharp_gap | close | <1k bets | 9-11 | 45.0 | 2.7 | 8.2 |  |
| money_moving+pin_move | close | <1k bets | 11-9 | 55.0 | 7.2 | 4.3 |  |
| money_moving+pin_rlm | close | <1k bets | 5-5 | 50.0 | 2.5 | -4.9 |  |
| money_moving+rlm_ratio | close | <1k bets | 10-12 | 45.5 | 1.1 | -12.8 |  |
| pin_move+pin_rlm | close | <1k bets | 5-5 | 50.0 | 2.5 | -4.9 |  |
| pin_move+pin_value | close | <1k bets | 7-4 | 63.6 | 14.4 | 20.8 |  |
| pin_move+rlm_ratio | close | <1k bets | 4-5 | 44.4 | -3.1 | -15.5 |  |
| pin_move+sharp_gap | close | <1k bets | 11-9 | 55.0 | 7.2 | 4.3 |  |
| pin_rlm+pin_value | close | <1k bets | 2-0 | 100.0 | 52.7 | 90.9 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 2-1 | 66.7 | 17.6 | 26.2 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 4-5 | 44.4 | -3.1 | -15.5 |  |
| pin_rlm+sharp_gap | close | <1k bets | 5-5 | 50.0 | 2.5 | -4.9 |  |
| pin_value+rlm_quiet | close | <1k bets | 3-0 | 100.0 | 52.7 | 90.9 |  |
| pin_value+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 52.7 | 90.9 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 5-6 | 45.5 | 2.7 | -11.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 10-12 | 45.5 | 1.1 | -12.8 |  |
| consensus_gap+follow_move | close | <1k bets | 5-1 | 83.3 | 28.8 | 42.8 |  |
| consensus_gap+pin_move | close | <1k bets | 2-0 | 100.0 | 43.1 | 70.5 |  |
| follow_move+money_level | close | <1k bets | 24-13 | 64.9 | 9.8 | 7.3 |  |
| money_delta+money_level | close | <1k bets | 3-3 | 50.0 | 7.9 | 7.7 |  |
| money_level+pin_rlm | close | <1k bets | 2-3 | 40.0 | -6.7 | -23.6 |  |
| money_level+rlm_ratio | close | <1k bets | 4-4 | 50.0 | 5.3 | -5.5 |  |
| consensus_gap+money_delta | close | <1k bets | 3-0 | 100.0 | 50.9 | 208.0 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 52.7 | 89.3 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-1 | 50.0 | 9.6 | -4.5 |  |
| money_delta+money_moving | close | pin $1-2k | 26-25 | 51.0 | 6.6 | 8.5 |  |
| money_delta+sharp_gap | close | pin $1-2k | 26-25 | 51.0 | 6.6 | 8.5 |  |
| money_moving+sharp_gap | close | pin $1-2k | 106-112 | 48.6 | -0.3 | -6.2 |  |
| consensus_gap+follow_move | close | pin $1-2k | 9-11 | 45.0 | -5.8 | -16.3 |  |
| consensus_gap+money_level | close | pin $1-2k | 17-15 | 53.1 | -3.0 | -11.9 |  |
| consensus_gap+money_moving | close | pin $1-2k | 8-13 | 38.1 | -11.5 | -15.4 |  |
| consensus_gap+pin_move | close | pin $1-2k | 11-11 | 50.0 | 1.2 | 10.9 |  |
| consensus_gap+pin_value | close | pin $1-2k | 16-15 | 51.6 | 3.1 | 10.3 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 8-13 | 38.1 | -11.5 | -14.1 |  |
| follow_move+money_level | close | pin $1-2k | 49-52 | 48.5 | -4.6 | -14.7 |  |
| follow_move+money_moving | close | pin $1-2k | 58-67 | 46.4 | -2.4 | -11.8 |  |
| follow_move+pin_move | close | pin $1-2k | 54-87 | 38.3 | -10.4 | -25.2 |  |
| follow_move+pin_value | close | pin $1-2k | 25-29 | 46.3 | -3.1 | -12.0 |  |
| follow_move+sharp_gap | close | pin $1-2k | 59-70 | 45.7 | -3.1 | -12.9 |  |
| money_level+money_moving | close | pin $1-2k | 78-75 | 51.0 | -0.8 | -8.7 |  |
| money_level+pin_move | close | pin $1-2k | 39-47 | 45.3 | -6.4 | -17.8 |  |
| money_level+pin_value | close | pin $1-2k | 32-32 | 50.0 | 0.2 | -6.7 |  |
| money_level+sharp_gap | close | pin $1-2k | 73-76 | 49.0 | -2.3 | -11.1 |  |
| money_moving+pin_move | close | pin $1-2k | 46-49 | 48.4 | -0.9 | -7.1 |  |
| money_moving+pin_value | close | pin $1-2k | 25-28 | 47.2 | -1.5 | -4.1 |  |
| pin_move+pin_value | close | pin $1-2k | 27-35 | 43.5 | -7.2 | -17.6 |  |
| pin_move+sharp_gap | close | pin $1-2k | 45-55 | 45.0 | -3.5 | -13.0 |  |
| pin_value+sharp_gap | close | pin $1-2k | 25-28 | 47.2 | -1.5 | -4.1 |  |
| follow_move+money_delta | close | pin $1-2k | 21-27 | 43.8 | -2.5 | -14.4 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 33-54 | 37.9 | -6.7 | -21.1 |  |
| money_delta+pin_move | close | pin $1-2k | 16-17 | 48.5 | 2.9 | -4.6 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 11-17 | 39.3 | -5.7 | -22.3 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 22-34 | 39.3 | -6.0 | -17.2 |  |
| follow_move+pin_rlm | close | pin $1-2k | 17-23 | 42.5 | -1.9 | -11.3 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 27-34 | 44.3 | -0.1 | -9.3 |  |
| pin_move+pin_rlm | close | pin $1-2k | 19-23 | 45.2 | 0.4 | -6.1 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 17-22 | 43.6 | -1.6 | -9.1 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 10-17 | 37.0 | -6.8 | -18.7 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 17-23 | 42.5 | -1.9 | -11.3 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 19-26 | 42.2 | -1.8 | -12.4 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 14-23 | 37.8 | -5.7 | -19.3 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 18-26 | 40.9 | -3.1 | -14.5 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 27-34 | 44.3 | -0.1 | -9.3 |  |
| money_delta+money_level | close | pin $1-2k | 11-11 | 50.0 | 2.5 | -2.9 |  |
| money_delta+pin_rlm | close | pin $1-2k | 11-12 | 47.8 | 4.0 | -4.9 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 13-15 | 46.4 | 2.0 | -8.0 |  |
| money_level+pin_rlm | close | pin $1-2k | 6-7 | 46.2 | 1.5 | -10.0 |  |
| money_level+rlm_ratio | close | pin $1-2k | 9-9 | 50.0 | 4.3 | -3.6 |  |
| money_moving+pin_rlm | close | pin $1-2k | 19-21 | 47.5 | 2.5 | -1.5 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 27-30 | 47.4 | 2.4 | -2.9 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 18-25 | 41.9 | -2.1 | -12.5 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 2-4 | 33.3 | -7.2 | -28.5 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 6-12 | 33.3 | -14.5 | -33.3 |  |
| money_delta+pin_value | close | pin $1-2k | 9-7 | 56.2 | 10.6 | 32.3 |  |
| consensus_gap+money_delta | close | pin $1-2k | 4-1 | 80.0 | 37.1 | 132.7 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 1-2 | 33.3 | -6.6 | -20.7 |  |
| pin_rlm+pin_value | close | pin $1-2k | 4-5 | 44.4 | -3.5 | -10.4 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 3-5 | 37.5 | -9.4 | -23.0 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 1-1 | 50.0 | 6.9 | 19.0 |  |
| follow_move+pin_move | close | pin $2k+ | 65-70 | 48.1 | -1.5 | -6.8 |  |
| consensus_gap+money_level | close | pin $2k+ | 40-23 | 63.5 | 3.2 | 0.6 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 40-50 | 44.4 | 3.4 | 10.0 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 26-38 | 40.6 | -1.7 | -8.4 |  |
| money_level+money_moving | close | pin $2k+ | 60-71 | 45.8 | -6.6 | -16.6 |  |
| money_level+sharp_gap | close | pin $2k+ | 57-73 | 43.8 | -8.4 | -18.7 |  |
| money_moving+sharp_gap | close | pin $2k+ | 91-116 | 44.0 | -3.8 | -13.0 |  |
| consensus_gap+pin_value | close | pin $2k+ | 21-14 | 60.0 | 10.2 | 13.1 |  |
| follow_move+money_level | close | pin $2k+ | 40-38 | 51.3 | -6.0 | -17.4 |  |
| follow_move+money_moving | close | pin $2k+ | 45-59 | 43.3 | -4.5 | -17.6 |  |
| follow_move+sharp_gap | close | pin $2k+ | 41-58 | 41.4 | -6.1 | -19.7 |  |
| money_level+pin_move | close | pin $2k+ | 31-28 | 52.5 | -4.9 | -12.8 |  |
| money_moving+pin_move | close | pin $2k+ | 35-44 | 44.3 | -3.3 | -13.5 |  |
| pin_move+sharp_gap | close | pin $2k+ | 34-45 | 43.0 | -4.5 | -15.0 |  |
| money_delta+money_level | close | pin $2k+ | 9-5 | 64.3 | 19.4 | 39.8 |  |
| money_delta+money_moving | close | pin $2k+ | 23-31 | 42.6 | 1.8 | -10.6 |  |
| money_delta+sharp_gap | close | pin $2k+ | 23-31 | 42.6 | 1.8 | -10.6 |  |
| consensus_gap+money_moving | close | pin $2k+ | 20-20 | 50.0 | -2.8 | 0.3 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 19-21 | 47.5 | -5.3 | -2.6 |  |
| money_level+pin_value | close | pin $2k+ | 16-29 | 35.6 | -14.8 | -33.7 |  |
| money_moving+pin_value | close | pin $2k+ | 18-30 | 37.5 | -13.1 | -29.9 |  |
| pin_value+sharp_gap | close | pin $2k+ | 18-32 | 36.0 | -15.2 | -32.7 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 5-4 | 55.6 | 10.6 | 24.4 |  |
| money_level+pin_rlm | close | pin $2k+ | 2-5 | 28.6 | -19.1 | -42.2 |  |
| money_moving+pin_rlm | close | pin $2k+ | 16-25 | 39.0 | 0.6 | -12.8 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 16-26 | 38.1 | -0.2 | -14.9 |  |
| follow_move+money_delta | close | pin $2k+ | 12-19 | 38.7 | -1.4 | -20.2 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 15-28 | 34.9 | -3.0 | -22.9 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 7-17 | 29.2 | -9.1 | -40.0 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 15-28 | 34.9 | -3.0 | -22.9 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 15-28 | 34.9 | -3.0 | -22.9 |  |
| money_level+rlm_ratio | close | pin $2k+ | 5-6 | 45.5 | 0.8 | -12.3 |  |
| consensus_gap+follow_move | close | pin $2k+ | 18-8 | 69.2 | 11.9 | 18.0 |  |
| consensus_gap+pin_move | close | pin $2k+ | 24-9 | 72.7 | 19.4 | 40.7 |  |
| follow_move+pin_value | close | pin $2k+ | 12-13 | 48.0 | -3.0 | 29.0 |  |
| pin_move+pin_value | close | pin $2k+ | 21-22 | 48.8 | -3.1 | -7.9 |  |
| follow_move+pin_rlm | close | pin $2k+ | 12-21 | 36.4 | 0.5 | -16.5 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 12-21 | 36.4 | 0.5 | -16.5 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 4-3 | 57.1 | 8.5 | 146.6 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 15-26 | 36.6 | -2.4 | -17.6 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 14-25 | 35.9 | -3.3 | -20.0 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 8-15 | 34.8 | -3.8 | -26.4 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 8-20 | 28.6 | -6.3 | -31.3 |  |
| money_delta+pin_move | close | pin $2k+ | 13-16 | 44.8 | 1.9 | -11.7 |  |
| money_delta+pin_rlm | close | pin $2k+ | 9-15 | 37.5 | -2.2 | -23.2 |  |
| pin_move+pin_rlm | close | pin $2k+ | 13-20 | 39.4 | 0.8 | -13.1 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 12-19 | 38.7 | 0.2 | -15.9 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 8-18 | 30.8 | -4.2 | -26.0 |  |
| consensus_gap+money_delta | close | pin $2k+ | 6-2 | 75.0 | 28.3 | 56.0 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 3-3 | 50.0 | 10.3 | 20.3 |  |
| money_delta+pin_value | close | pin $2k+ | 6-4 | 60.0 | 5.7 | 13.9 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 4-2 | 66.7 | 25.3 | 51.1 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 2-0 | 100.0 | 48.1 | 87.8 |  |
| pin_rlm+pin_value | close | pin $2k+ | 3-2 | 60.0 | 5.4 | 13.9 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 5-5 | 50.0 | 2.5 | -4.0 |  |
| consensus_gap+money_level | close | pin limit <$1k | 6-6 | 50.0 | -2.3 | -5.5 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 6-10 | 37.5 | -10.8 | -28.1 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 8-12 | 40.0 | -9.6 | -24.2 |  |
| follow_move+money_level | close | pin limit <$1k | 26-18 | 59.1 | 7.9 | 11.0 |  |
| follow_move+money_moving | close | pin limit <$1k | 24-28 | 46.2 | -3.2 | -11.6 |  |
| follow_move+pin_value | close | pin limit <$1k | 14-8 | 63.6 | 12.7 | 21.1 |  |
| money_level+money_moving | close | pin limit <$1k | 31-27 | 53.4 | 2.4 | 1.8 |  |
| money_level+pin_value | close | pin limit <$1k | 21-13 | 61.8 | 9.7 | 17.4 |  |
| money_moving+pin_value | close | pin limit <$1k | 17-17 | 50.0 | -0.4 | -5.0 |  |
| follow_move+pin_move | close | pin limit <$1k | 24-22 | 52.2 | 3.1 | 0.3 |  |
| money_level+pin_move | close | pin limit <$1k | 24-14 | 63.2 | 12.6 | 20.6 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 37-44 | 45.7 | -3.9 | -12.8 |  |
| pin_move+pin_value | close | pin limit <$1k | 15-12 | 55.6 | 5.3 | 6.1 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 15-19 | 44.1 | -3.4 | -14.9 |  |
| money_moving+pin_move | close | pin limit <$1k | 20-19 | 51.3 | 2.2 | -1.8 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 3-2 | 60.0 | 15.5 | 16.4 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 4-4 | 50.0 | 3.1 | -3.4 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 1-2 | 33.3 | -9.4 | -33.3 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 3-3 | 50.0 | 5.0 | -3.0 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 2-3 | 40.0 | -4.5 | -21.8 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 6-11 | 35.3 | -12.9 | -32.3 |  |
| follow_move+money_delta | close | pin limit <$1k | 6-12 | 33.3 | -13.5 | -35.8 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 7-11 | 38.9 | -8.5 | -25.0 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 10-17 | 37.0 | -10.5 | -28.9 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 23-27 | 46.0 | -3.3 | -12.0 |  |
| money_delta+money_moving | close | pin limit <$1k | 9-14 | 39.1 | -7.8 | -24.5 |  |
| money_delta+pin_move | close | pin limit <$1k | 4-10 | 28.6 | -17.7 | -44.5 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 3-7 | 30.0 | -15.9 | -41.4 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 3-5 | 37.5 | -8.1 | -27.3 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 5-11 | 31.2 | -15.5 | -39.8 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 9-14 | 39.1 | -7.8 | -24.5 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 8-12 | 40.0 | -7.4 | -23.0 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 4-11 | 26.7 | -20.4 | -48.5 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 9-16 | 36.0 | -11.6 | -30.9 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 8-12 | 40.0 | -7.4 | -23.0 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 6-10 | 37.5 | -9.9 | -27.0 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 7-11 | 38.9 | -8.5 | -25.0 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 17-18 | 48.6 | -0.2 | -6.9 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 1-6 | 14.3 | -31.8 | -71.4 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 7-11 | 38.9 | -8.5 | -25.0 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 8-12 | 40.0 | -7.4 | -23.0 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 3-11 | 21.4 | -25.3 | -58.4 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 4-11 | 26.7 | -20.4 | -48.7 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 10-17 | 37.0 | -10.5 | -28.9 |  |
| money_delta+pin_value | close | pin limit <$1k | 6-2 | 75.0 | 27.0 | 43.2 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 4-3 | 57.1 | 9.1 | 8.5 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 2-3 | 40.0 | -8.4 | -24.4 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 16-19 | 45.7 | -4.6 | -13.2 |  |
| money_level+sharp_gap | close | pin limit <$1k | 27-26 | 50.9 | -0.1 | -2.9 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 1-3 | 25.0 | -22.3 | -52.3 |  |
| money_delta+money_level | close | pin limit <$1k | 1-6 | 14.3 | -33.0 | -72.1 |  |
| money_level+pin_rlm | close | pin limit <$1k | 5-4 | 55.6 | 7.1 | 6.5 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 5-5 | 50.0 | 1.6 | -4.1 |  |
| rlm_quiet | early | <1k bets | 26-34 | 43.3 | 4.5 | 3.5 | 0.9 |
| rlm_quiet | early | pin $1-2k | 2-2 | 50.0 | 16.4 | 23.0 | 1.12 |
| rlm_quiet | early | pin limit <$1k | 1-2 | 33.3 | -13.9 | -36.4 | 0.33 |
| pin_move | early | <1k bets | 9-13 | 40.9 | -8.5 | -23.2 | 0.12 |
| pin_move | early | pin $1-2k | 2-6 | 25.0 | -25.9 | -56.8 | 0.29 |
| pin_move | early | pin limit <$1k | 7-10 | 41.2 | -8.1 | -20.9 | 0.59 |
| money_delta | early | <1k bets | 4-5 | 44.4 | 6.3 | 16.3 | 3.02 |
| money_delta | early | pin $1-2k | 0-1 | 0.0 | -33.6 | -100.0 | 1.5 |
| money_delta | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| pin_rlm | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -66.4 | -100.0 | 1.5 |
| pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -33.6 | -100.0 | 0.0 |
| follow_move | early | <1k bets | 210-228 | 47.9 | -0.9 | -8.4 | 0.08 |
| follow_move | early | pin $1-2k | 14-15 | 48.3 | 2.9 | -2.9 | -0.35 |
| follow_move | early | pin limit <$1k | 13-21 | 38.2 | -10.3 | -25.6 | 0.01 |
| rlm_ratio | early | <1k bets | 10-16 | 38.5 | -3.1 | -7.6 | 0.4 |
| rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -66.4 | -100.0 | 1.5 |
| rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 9.6 | -4.5 | 0.5 |
| money_level | early | <1k bets | 74-63 | 54.0 | -3.5 | -13.1 | -0.36 |
| money_level | early | pin $1-2k | 3-5 | 37.5 | -22.0 | -38.8 | -0.29 |
| money_level | early | pin limit <$1k | 8-6 | 57.1 | 6.6 | 9.1 | 0.29 |
| sharp_gap | early | <1k bets | 57-65 | 46.7 | -3.3 | -10.7 | 0.21 |
| sharp_gap | early | pin $1-2k | 2-6 | 25.0 | -36.1 | -63.1 | -0.04 |
| sharp_gap | early | pin limit <$1k | 7-5 | 58.3 | 9.0 | 11.4 | 0.33 |
| money_moving | early | <1k bets | 47-44 | 51.6 | 2.6 | -1.6 | 0.51 |
| money_moving | early | pin $1-2k | 0-4 | 0.0 | -55.7 | -100.0 | 1.05 |
| money_moving | early | pin limit <$1k | 10-2 | 83.3 | 33.1 | 57.2 | 0.25 |
| pin_value | early | <1k bets | 22-19 | 53.7 | 4.2 | 1.5 | 0.09 |
| pin_value | early | pin $1-2k | 6-11 | 35.3 | -13.4 | -33.8 | 0.34 |
| pin_value | early | pin limit <$1k | 17-9 | 65.4 | 15.5 | 24.0 | -0.04 |
| consensus_gap | early | <1k bets | 116-107 | 52.0 | -0.8 | -9.1 | 0.57 |
| consensus_gap | early | pin $1-2k | 10-5 | 66.7 | 16.4 | 23.1 | -0.17 |
| consensus_gap | early | pin limit <$1k | 8-4 | 66.7 | 16.2 | 26.7 | 0.08 |
| follow_move+money_level | early | <1k bets | 26-19 | 57.8 | 0.7 | -13.2 | 0.28 |
| follow_move+sharp_gap | early | <1k bets | 24-27 | 47.1 | -0.7 | -7.8 | 0.71 |
| money_level+sharp_gap | early | <1k bets | 38-38 | 50.0 | -5.7 | -16.3 | -0.18 |
| follow_move+money_moving | early | <1k bets | 19-19 | 50.0 | 2.3 | 0.4 | 0.67 |
| money_level+money_moving | early | <1k bets | 22-18 | 55.0 | -0.2 | -4.9 | 0.44 |
| consensus_gap+money_level | early | <1k bets | 25-19 | 56.8 | -4.4 | -14.9 | -0.45 |
| follow_move+rlm_quiet | early | <1k bets | 26-34 | 43.3 | 4.5 | 3.5 | 0.9 |
| follow_move+rlm_ratio | early | <1k bets | 10-16 | 38.5 | -3.1 | -7.6 | 0.4 |
| rlm_quiet+rlm_ratio | early | <1k bets | 9-10 | 47.4 | 8.0 | 16.3 | 0.32 |
| rlm_quiet+sharp_gap | early | <1k bets | 10-13 | 43.5 | 3.3 | 4.4 | 0.71 |
| rlm_ratio+sharp_gap | early | <1k bets | 10-16 | 38.5 | -3.1 | -7.6 | 0.4 |
| consensus_gap+follow_move | early | <1k bets | 16-21 | 43.2 | -11.8 | -28.1 | 1.06 |
| money_moving+rlm_quiet | early | <1k bets | 9-10 | 47.4 | 8.0 | 15.7 | 0.91 |
| money_moving+rlm_ratio | early | <1k bets | 7-6 | 53.8 | 13.2 | 31.1 | 1.58 |
| money_moving+sharp_gap | early | <1k bets | 26-29 | 47.3 | 0.2 | -2.2 | 0.73 |
| consensus_gap+money_moving | early | <1k bets | 10-6 | 62.5 | 7.9 | -0.2 | 1.16 |
| consensus_gap+sharp_gap | early | <1k bets | 15-16 | 48.4 | -8.2 | -23.8 | -0.36 |
| money_level+rlm_ratio | early | <1k bets | 1-6 | 14.3 | -33.1 | -72.7 | 0.64 |
| follow_move+pin_move | early | <1k bets | 4-7 | 36.4 | -10.8 | -29.9 | 0.55 |
| follow_move+money_delta | early | <1k bets | 3-2 | 60.0 | 20.9 | 71.2 | 2.74 |
| money_delta+money_level | early | <1k bets | 1-3 | 25.0 | -15.4 | -52.3 | 1.68 |
| money_delta+money_moving | early | <1k bets | 4-5 | 44.4 | 6.3 | 16.3 | 3.02 |
| money_delta+rlm_ratio | early | <1k bets | 3-2 | 60.0 | 20.9 | 71.2 | 2.74 |
| money_delta+sharp_gap | early | <1k bets | 4-5 | 44.4 | 6.3 | 16.3 | 3.02 |
| follow_move+pin_value | early | <1k bets | 5-5 | 50.0 | 0.9 | -4.1 | -0.3 |
| consensus_gap+pin_move | early | <1k bets | 2-1 | 66.7 | 14.5 | 28.7 | 0.33 |
| consensus_gap+pin_value | early | <1k bets | 10-3 | 76.9 | 28.0 | 45.4 | -0.15 |
| money_level+pin_move | early | <1k bets | 2-4 | 33.3 | -14.7 | -35.8 | 0.17 |
| money_level+pin_value | early | <1k bets | 3-3 | 50.0 | -4.1 | -4.5 | 0.78 |
| pin_move+pin_value | early | <1k bets | 4-7 | 36.4 | -13.5 | -29.8 | 0.55 |
| money_moving+pin_value | early | <1k bets | 3-2 | 60.0 | 7.1 | 15.4 | 1.14 |
| pin_value+sharp_gap | early | <1k bets | 1-4 | 20.0 | -35.1 | -61.8 | 1.34 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| consensus_gap+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| follow_move+pin_rlm | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| money_level+pin_rlm | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_rlm+rlm_ratio | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_rlm+sharp_gap | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_move+sharp_gap | early | <1k bets | 0-3 | 0.0 | -46.3 | -100.0 | 1.0 |
| money_delta+rlm_quiet | early | <1k bets | 2-1 | 66.7 | 33.1 | 121.7 | 3.57 |
| consensus_gap+rlm_quiet | early | <1k bets | 1-1 | 50.0 | 16.4 | 30.0 | 1.1 |
| money_moving+pin_move | early | <1k bets | 1-1 | 50.0 | 2.7 | -2.4 | 1.0 |
| pin_move+pin_rlm | early | <1k bets | 0-1 | 0.0 | -33.6 | -100.0 | 0.0 |
| pin_move+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -33.6 | -100.0 | 0.0 |
| pin_move+pin_value | early | pin $1-2k | 0-4 | 0.0 | -46.8 | -100.0 | 0.5 |
| follow_move+rlm_quiet | early | pin $1-2k | 2-2 | 50.0 | 16.4 | 23.0 | 1.12 |
| money_level+money_moving | early | pin $1-2k | 0-3 | 0.0 | -55.5 | -100.0 | 1.07 |
| money_level+pin_value | early | pin $1-2k | 0-1 | 0.0 | -66.4 | -100.0 | 1.7 |
| money_level+sharp_gap | early | pin $1-2k | 2-5 | 28.6 | -33.2 | -57.8 | -0.19 |
| money_moving+pin_value | early | pin $1-2k | 0-2 | 0.0 | -61.4 | -100.0 | 1.35 |
| money_moving+sharp_gap | early | pin $1-2k | 0-4 | 0.0 | -55.7 | -100.0 | 1.05 |
| pin_value+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -61.4 | -100.0 | 1.35 |
| consensus_gap+pin_value | early | pin $1-2k | 3-1 | 75.0 | 28.2 | 39.3 | -0.5 |
| follow_move+money_level | early | pin $1-2k | 1-2 | 33.3 | -25.5 | -35.2 | 0.17 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -66.4 | -100.0 | 1.5 |
| follow_move+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -66.4 | -100.0 | 1.5 |
| follow_move+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -66.4 | -100.0 | 0.75 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -66.4 | -100.0 | 1.5 |
| money_level+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -66.4 | -100.0 | 1.5 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -66.4 | -100.0 | 1.5 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -66.4 | -100.0 | 1.5 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -66.4 | -100.0 | 1.5 |
| consensus_gap+follow_move | early | pin $1-2k | 2-1 | 66.7 | 22.1 | 55.3 | 0.6 |
| follow_move+pin_move | early | pin $1-2k | 1-2 | 33.3 | -14.5 | -35.2 | -0.33 |
| follow_move+pin_value | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap+money_level | early | pin $1-2k | 2-1 | 66.7 | 0.2 | -1.6 | -1.83 |
| consensus_gap+sharp_gap | early | pin $1-2k | 2-1 | 66.7 | 0.2 | -1.6 | -1.83 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 1-0 | 100.0 | 66.4 | 160.0 | 0.3 |
| consensus_gap+money_moving | early | pin $1-2k | 0-1 | 0.0 | -66.4 | -100.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 0-1 | 0.0 | -66.4 | -100.0 | 0.0 |
| money_level+pin_move | early | pin $1-2k | 1-0 | 100.0 | 56.5 | 94.3 | -1.0 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -33.6 | -100.0 | 1.5 |
| money_delta+money_moving | early | pin $1-2k | 0-1 | 0.0 | -33.6 | -100.0 | 1.5 |
| money_delta+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -33.6 | -100.0 | 1.5 |
| follow_move+pin_move | early | pin limit <$1k | 3-6 | 33.3 | -13.6 | -35.9 | 0.89 |
| follow_move+pin_value | early | pin limit <$1k | 5-3 | 62.5 | 13.6 | 19.9 | -0.38 |
| consensus_gap+money_level | early | pin limit <$1k | 3-0 | 100.0 | 49.1 | 90.9 | 0.0 |
| consensus_gap+pin_move | early | pin limit <$1k | 2-1 | 66.7 | 14.5 | 28.7 | 0.33 |
| consensus_gap+pin_value | early | pin limit <$1k | 7-2 | 77.8 | 27.9 | 48.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 4-2 | 66.7 | 18.5 | 28.0 | 0.5 |
| follow_move+rlm_quiet | early | pin limit <$1k | 1-2 | 33.3 | -13.9 | -36.4 | 0.33 |
| follow_move+sharp_gap | early | pin limit <$1k | 3-3 | 50.0 | 3.2 | -3.8 | 0.17 |
| money_level+pin_move | early | pin limit <$1k | 1-4 | 20.0 | -28.9 | -61.8 | 0.4 |
| money_level+pin_value | early | pin limit <$1k | 4-2 | 66.7 | 14.9 | 26.6 | 0.33 |
| money_moving+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 2.7 | -4.5 | 0.0 |
| money_moving+sharp_gap | early | pin limit <$1k | 6-1 | 85.7 | 36.1 | 63.7 | 0.0 |
| pin_move+pin_value | early | pin limit <$1k | 4-4 | 50.0 | -0.7 | -3.5 | 0.75 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -47.3 | -100.0 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 | -0.5 |
| consensus_gap+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 52.7 | 92.3 | 1.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| follow_move+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| follow_move+money_level | early | pin limit <$1k | 3-3 | 50.0 | 2.3 | -3.8 | 0.0 |
| follow_move+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 9.6 | -4.5 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| money_delta+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| money_delta+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| money_delta+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| money_level+money_moving | early | pin limit <$1k | 5-0 | 100.0 | 49.5 | 91.0 | 0.2 |
| money_level+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 9.6 | -4.5 | 0.5 |
| money_level+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 10.3 | 14.6 | 0.5 |
| money_moving+pin_value | early | pin limit <$1k | 4-0 | 100.0 | 51.4 | 91.0 | 0.5 |
| money_moving+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| pin_value+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | -1.4 | -5.5 | 0.75 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 9.6 | -4.5 | 0.5 |
| pin_move+sharp_gap | early | pin limit <$1k | 0-3 | 0.0 | -46.3 | -100.0 | 1.0 |
| money_moving+pin_move | early | pin limit <$1k | 1-1 | 50.0 | 2.7 | -2.4 | 1.0 |
| follow_move+pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -33.6 | -100.0 | 0.0 |
| money_level+pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -33.6 | -100.0 | 0.0 |
| pin_move+pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -33.6 | -100.0 | 0.0 |
| pin_move+rlm_ratio | early | pin limit <$1k | 0-1 | 0.0 | -33.6 | -100.0 | 0.0 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 0-1 | 0.0 | -33.6 | -100.0 | 0.0 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -33.6 | -100.0 | 0.0 |
| pin_move+rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -47.3 | -100.0 | 1.0 |
