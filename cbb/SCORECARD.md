# CBB scorecard

Generated 2026-11-24 14:18 UTC. 839 graded games (23 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**684 games before 2026-11-21 (fit) · 155 on or after it (forward).**

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
sample ran **47.0% favourites** (n=838) and **50.8% overs** (n=839) and **72.1% moneyline favourites** (n=723).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-21. Nothing in the engine was chosen using these. n=155 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 9-18 | 33.3 | 38.3 | -5.0 | -6.59 | -24.4 | 0.86 | 48.1 | keep collecting (27/30) |
| pin_move | both | 4-6 | 40.0 | 49.7 | -9.7 | -2.36 | -23.6 | 0.3 | 30.0 | keep collecting (10/30) |
| money_delta | both | 2-3 | 40.0 | 40.0 | -0.0 | -1.18 | -23.6 | 3.0 | 100.0 | keep collecting (5/30) |
| pin_rlm | both | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 | 1.5 | 100.0 | keep collecting (1/30) |
| follow_move | both | 104-121 | 46.2 | 48.7 | -2.4 | -27.66 | -12.3 | 0.18 | 37.8 | DROP: below break-even |
| rlm_ratio | both | 5-11 | 31.2 | 42.5 | -11.2 | -5.6 | -35.0 | 0.82 | 56.2 | keep collecting (16/30) |
| money_level | both | 39-30 | 56.5 | 59.1 | -2.6 | -6.78 | -9.8 | -0.24 | 39.1 | no edge shown yet |
| sharp_gap | both | 25-36 | 41.0 | 47.4 | -6.4 | -11.23 | -18.4 | 0.67 | 54.1 | DROP: below break-even |
| money_moving | both | 24-28 | 46.2 | 47.7 | -1.5 | -7.36 | -14.1 | 0.35 | 48.1 | no edge shown yet |
| pin_value | both | 11-12 | 47.8 | 48.9 | -1.1 | -2.27 | -9.9 | -0.01 | 34.8 | keep collecting (23/30) |
| consensus_gap | both | 67-50 | 57.3 | 52.1 | 5.2 | +2.23 | 1.9 | 0.32 | 48.7 | no edge shown yet |
| follow_move+money_level | both | 14-10 | 58.3 | 60.7 | -2.3 | -3.69 | -15.4 | 0.53 | 41.7 | keep collecting (24/30) |
| follow_move+sharp_gap | both | 11-17 | 39.3 | 48.5 | -9.2 | -7.44 | -26.6 | 1.05 | 53.6 | keep collecting (28/30) |
| money_level+sharp_gap | both | 15-17 | 46.9 | 55.6 | -8.7 | -5.83 | -18.2 | 0.33 | 53.1 | no edge shown yet |
| follow_move+money_moving | both | 11-12 | 47.8 | 48.4 | -0.6 | -3.1 | -13.5 | 0.49 | 43.5 | keep collecting (23/30) |
| money_level+money_moving | both | 13-11 | 54.2 | 56.0 | -1.9 | -1.64 | -6.8 | 0.2 | 41.7 | keep collecting (24/30) |
| consensus_gap+money_level | both | 12-7 | 63.2 | 59.1 | 4.1 | -1.65 | -8.7 | -0.22 | 42.1 | keep collecting (19/30) |
| follow_move+rlm_quiet | both | 9-18 | 33.3 | 38.3 | -5.0 | -6.59 | -24.4 | 0.86 | 48.1 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 5-11 | 31.2 | 42.5 | -11.2 | -5.6 | -35.0 | 0.82 | 56.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | both | 4-8 | 33.3 | 38.9 | -5.6 | -3.51 | -29.3 | 0.3 | 41.7 | keep collecting (12/30) |
| rlm_quiet+sharp_gap | both | 4-9 | 30.8 | 39.4 | -8.6 | -4.51 | -34.7 | 0.28 | 38.5 | keep collecting (13/30) |
| rlm_ratio+sharp_gap | both | 5-11 | 31.2 | 42.5 | -11.2 | -5.6 | -35.0 | 0.82 | 56.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 8-5 | 61.5 | 53.0 | 8.5 | -0.09 | -0.7 | 0.64 | 61.5 | keep collecting (13/30) |
| money_moving+rlm_quiet | both | 5-6 | 45.5 | 38.4 | 7.0 | +0.37 | 3.3 | 0.55 | 45.5 | keep collecting (11/30) |
| money_moving+rlm_ratio | both | 5-5 | 50.0 | 41.3 | 8.7 | +0.4 | 4.0 | 0.99 | 60.0 | keep collecting (10/30) |
| money_moving+sharp_gap | both | 15-19 | 44.1 | 45.8 | -1.7 | -4.09 | -12.0 | 0.76 | 55.9 | no edge shown yet |
| consensus_gap+money_moving | both | 4-3 | 57.1 | 49.2 | 7.9 | -0.83 | -11.9 | 0.74 | 57.1 | keep collecting (7/30) |
| consensus_gap+sharp_gap | both | 6-5 | 54.5 | 48.5 | 6.1 | -1.15 | -10.5 | 0.05 | 54.5 | keep collecting (11/30) |
| money_level+rlm_ratio | both | 1-3 | 25.0 | 53.1 | -28.1 | -2.09 | -52.3 | 2.38 | 100.0 | keep collecting (4/30) |
| follow_move+pin_move | both | 1-3 | 25.0 | 46.9 | -21.9 | -2.09 | -52.3 | 0.5 | 25.0 | keep collecting (4/30) |
| follow_move+money_delta | both | 1-1 | 50.0 | 44.5 | 5.5 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+money_level | both | 1-2 | 33.3 | 40.8 | -7.5 | -1.09 | -36.4 | 1.73 | 100.0 | keep collecting (3/30) |
| money_delta+money_moving | both | 2-3 | 40.0 | 40.0 | -0.0 | -1.18 | -23.6 | 3.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | both | 1-1 | 50.0 | 44.5 | 5.5 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+sharp_gap | both | 2-3 | 40.0 | 40.0 | -0.0 | -1.18 | -23.6 | 3.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| follow_move+pin_value | both | 3-3 | 50.0 | 45.9 | 4.1 | -0.27 | -4.5 | -0.83 | 16.7 | keep collecting (6/30) |
| consensus_gap+pin_move | both | 1-0 | 100.0 | 55.5 | 44.5 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+pin_value | both | 5-1 | 83.3 | 49.8 | 33.5 | +3.47 | 57.8 | 0.0 | 33.3 | keep collecting (6/30) |
| money_level+pin_move | both | 1-1 | 50.0 | 55.5 | -5.5 | -0.09 | -4.5 | 1.5 | 50.0 | keep collecting (2/30) |
| money_level+pin_value | both | 2-2 | 50.0 | 55.5 | -5.5 | -0.18 | -4.5 | 1.43 | 75.0 | keep collecting (4/30) |
| pin_move+pin_value | both | 2-5 | 28.6 | 50.4 | -21.8 | -3.18 | -45.5 | 0.43 | 28.6 | keep collecting (7/30) |
| money_moving+pin_value | both | 1-1 | 50.0 | 55.6 | -5.6 | -0.09 | -4.5 | 1.35 | 100.0 | keep collecting (2/30) |
| pin_value+sharp_gap | both | 1-2 | 33.3 | 55.6 | -22.2 | -1.09 | -36.4 | 1.9 | 100.0 | keep collecting (3/30) |
| consensus_gap+money_delta | both | 1-0 | 100.0 | 44.5 | 55.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 1-0 | 100.0 | 44.5 | 55.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | both | 1-0 | 100.0 | 44.5 | 55.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+rlm_ratio | both | 1-0 | 100.0 | 44.5 | 55.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | both | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+sharp_gap | both | 0-1 | 0.0 | 55.5 | -55.5 | -1.0 | -100.0 | 3.0 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 5-10 | 33.3 | 33.3 | 0.0 | -2.19 | -14.6 | 0.89 | 40.0 | keep collecting (15/30) |
| rlm_quiet | total | 4-8 | 33.3 | 44.5 | -11.2 | -4.4 | -36.7 | 0.83 | 58.3 | keep collecting (12/30) |
| pin_move | spread | 0-2 | 0.0 | 43.2 | -43.2 | -2.0 | -100.0 | 0.0 | 0.0 | keep collecting (2/30) |
| pin_move | total | 4-4 | 50.0 | 51.4 | -1.4 | -0.36 | -4.5 | 0.38 | 37.5 | keep collecting (8/30) |
| money_delta | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 | 2.0 | 100.0 | keep collecting (2/30) |
| money_delta | total | 2-1 | 66.7 | 44.5 | 22.2 | +0.82 | 27.3 | 3.67 | 100.0 | keep collecting (3/30) |
| pin_rlm | moneyline | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 | 1.5 | 100.0 | keep collecting (1/30) |
| follow_move | moneyline | 46-36 | 56.1 | 47.2 | 8.9 | +3.83 | 4.7 | -0.07 | 32.9 | no edge shown yet |
| follow_move | spread | 24-38 | 38.7 | 51.3 | -12.6 | -15.61 | -25.2 | -0.11 | 29.0 | DROP: below break-even |
| follow_move | total | 34-47 | 42.0 | 48.2 | -6.2 | -15.87 | -19.6 | 0.67 | 49.4 | DROP: below break-even |
| rlm_ratio | moneyline | 1-6 | 14.3 | 38.1 | -23.8 | -4.24 | -60.6 | 0.01 | 28.6 | keep collecting (7/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| rlm_ratio | total | 4-4 | 50.0 | 44.5 | 5.5 | -0.36 | -4.5 | 1.0 | 75.0 | keep collecting (8/30) |
| money_level | moneyline | 21-16 | 56.8 | 63.1 | -6.3 | -9.18 | -24.8 | -0.2 | 35.1 | no edge shown yet |
| money_level | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level | total | 18-13 | 58.1 | 54.4 | 3.6 | +3.4 | 11.0 | -0.45 | 41.9 | no edge shown yet |
| sharp_gap | moneyline | 10-21 | 32.3 | 45.2 | -12.9 | -9.9 | -31.9 | 0.67 | 58.1 | DROP: below break-even |
| sharp_gap | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| sharp_gap | total | 15-14 | 51.7 | 49.4 | 2.3 | -0.33 | -1.1 | 0.52 | 48.3 | keep collecting (29/30) |
| money_moving | moneyline | 10-16 | 38.5 | 46.2 | -7.7 | -8.12 | -31.2 | 0.43 | 57.7 | keep collecting (26/30) |
| money_moving | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving | total | 14-11 | 56.0 | 48.9 | 7.1 | +1.76 | 7.0 | 0.08 | 36.0 | keep collecting (25/30) |
| pin_value | moneyline | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| pin_value | spread | 6-7 | 46.2 | 46.4 | -0.2 | -1.81 | -14.0 | -0.15 | 23.1 | keep collecting (13/30) |
| pin_value | total | 5-4 | 55.6 | 50.6 | 4.9 | +0.54 | 6.1 | 0.0 | 44.4 | keep collecting (9/30) |
| consensus_gap | moneyline | 32-24 | 57.1 | 55.4 | 1.8 | -3.02 | -5.4 | -0.12 | 44.6 | no edge shown yet |
| consensus_gap | spread | 14-11 | 56.0 | 48.1 | 7.9 | +1.31 | 5.2 | 0.2 | 36.0 | keep collecting (25/30) |
| consensus_gap | total | 21-15 | 58.3 | 49.7 | 8.6 | +3.94 | 10.9 | 1.08 | 63.9 | no edge shown yet |
| consensus_gap+money_level | moneyline | 10-6 | 62.5 | 60.4 | 2.1 | -2.47 | -15.5 | -0.45 | 37.5 | keep collecting (16/30) |
| follow_move+rlm_quiet | moneyline | 5-10 | 33.3 | 33.3 | 0.0 | -2.19 | -14.6 | 0.89 | 40.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 1-6 | 14.3 | 38.1 | -23.8 | -4.24 | -60.6 | 0.01 | 28.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 3-7 | 30.0 | 46.7 | -16.7 | -4.71 | -47.1 | 1.23 | 40.0 | keep collecting (10/30) |
| rlm_quiet+rlm_ratio | moneyline | 1-5 | 16.7 | 33.3 | -16.7 | -3.24 | -54.0 | -0.23 | 16.7 | keep collecting (6/30) |
| rlm_quiet+sharp_gap | moneyline | 1-5 | 16.7 | 33.3 | -16.7 | -3.24 | -54.0 | -0.23 | 16.7 | keep collecting (6/30) |
| rlm_ratio+sharp_gap | moneyline | 1-6 | 14.3 | 38.1 | -23.8 | -4.24 | -60.6 | 0.01 | 28.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 5-1 | 83.3 | 61.1 | 22.2 | +1.18 | 19.7 | -0.62 | 33.3 | keep collecting (6/30) |
| consensus_gap+money_moving | moneyline | 3-3 | 50.0 | 50.0 | -0.0 | -1.74 | -29.0 | 0.7 | 50.0 | keep collecting (6/30) |
| consensus_gap+sharp_gap | moneyline | 5-4 | 55.6 | 48.1 | 7.4 | -1.06 | -11.8 | -0.27 | 44.4 | keep collecting (9/30) |
| money_level+money_moving | moneyline | 5-5 | 50.0 | 60.0 | -10.0 | -2.95 | -29.4 | 0.49 | 40.0 | keep collecting (10/30) |
| money_level+sharp_gap | moneyline | 6-9 | 40.0 | 57.8 | -17.8 | -6.04 | -40.3 | 0.45 | 53.3 | keep collecting (15/30) |
| money_moving+sharp_gap | moneyline | 4-12 | 25.0 | 41.7 | -16.7 | -7.12 | -44.5 | 1.11 | 68.8 | keep collecting (16/30) |
| follow_move+money_level | moneyline | 9-4 | 69.2 | 66.7 | 2.6 | -2.23 | -17.2 | 0.06 | 23.1 | keep collecting (13/30) |
| follow_move+money_moving | moneyline | 6-5 | 54.5 | 48.5 | 6.1 | -0.65 | -5.9 | 0.02 | 36.4 | keep collecting (11/30) |
| money_moving+rlm_quiet | moneyline | 2-4 | 33.3 | 33.3 | -0.0 | -0.36 | -6.0 | 0.67 | 50.0 | keep collecting (6/30) |
| money_moving+rlm_ratio | moneyline | 1-3 | 25.0 | 33.3 | -8.3 | -1.24 | -31.0 | -0.28 | 25.0 | keep collecting (4/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_rlm | moneyline | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | moneyline | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 | 1.5 | 100.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+money_moving | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_level | moneyline | 0-1 | 0.0 | 33.3 | -33.3 | -1.0 | -100.0 | 2.2 | 100.0 | keep collecting (1/30) |
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
| follow_move+pin_value | spread | 1-1 | 50.0 | 43.2 | 6.8 | -0.09 | -4.5 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | spread | 0-2 | 0.0 | 43.2 | -43.2 | -2.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| consensus_gap+pin_value | spread | 2-1 | 66.7 | 47.7 | 18.9 | +0.74 | 24.7 | -0.67 | 0.0 | keep collecting (3/30) |
| follow_move+pin_move | spread | 0-1 | 0.0 | 43.2 | -43.2 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_level | total | 5-5 | 50.0 | 53.3 | -3.3 | -0.46 | -4.6 | 0.7 | 60.0 | keep collecting (10/30) |
| follow_move+sharp_gap | total | 8-9 | 47.1 | 49.0 | -2.0 | -1.73 | -10.2 | 0.71 | 58.8 | keep collecting (17/30) |
| money_level+sharp_gap | total | 9-7 | 56.2 | 53.4 | 2.8 | +1.21 | 7.6 | -0.06 | 50.0 | keep collecting (16/30) |
| follow_move+money_moving | total | 5-6 | 45.5 | 47.5 | -2.1 | -1.45 | -13.2 | 0.55 | 45.5 | keep collecting (11/30) |
| money_level+money_moving | total | 8-5 | 61.5 | 53.0 | 8.6 | +2.31 | 17.7 | -0.38 | 38.5 | keep collecting (13/30) |
| follow_move+rlm_quiet | total | 4-8 | 33.3 | 44.5 | -11.2 | -4.4 | -36.7 | 0.83 | 58.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 4-4 | 50.0 | 44.5 | 5.5 | -0.36 | -4.5 | 1.0 | 75.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 3-3 | 50.0 | 44.5 | 5.5 | -0.27 | -4.5 | 0.83 | 66.7 | keep collecting (6/30) |
| rlm_quiet+sharp_gap | total | 3-4 | 42.9 | 44.5 | -1.7 | -1.27 | -18.2 | 0.71 | 57.1 | keep collecting (7/30) |
| rlm_ratio+sharp_gap | total | 4-4 | 50.0 | 44.5 | 5.5 | -0.36 | -4.5 | 1.0 | 75.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | total | 3-2 | 60.0 | 44.5 | 15.5 | +0.73 | 14.5 | 0.4 | 40.0 | keep collecting (5/30) |
| money_moving+rlm_ratio | total | 4-1 | 80.0 | 44.5 | 35.5 | +2.64 | 52.7 | 1.2 | 80.0 | keep collecting (5/30) |
| money_moving+sharp_gap | total | 11-6 | 64.7 | 49.0 | 15.7 | +4.03 | 23.7 | 0.18 | 41.2 | keep collecting (17/30) |
| follow_move+pin_move | total | 1-2 | 33.3 | 48.2 | -14.8 | -1.09 | -36.4 | 0.67 | 33.3 | keep collecting (3/30) |
| consensus_gap+follow_move | total | 3-4 | 42.9 | 46.1 | -3.2 | -1.27 | -18.2 | 1.71 | 85.7 | keep collecting (7/30) |
| consensus_gap+money_level | total | 2-1 | 66.7 | 51.8 | 14.8 | +0.82 | 27.3 | 1.0 | 66.7 | keep collecting (3/30) |
| consensus_gap+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| follow_move+money_delta | total | 1-1 | 50.0 | 44.5 | 5.5 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+money_level | total | 1-1 | 50.0 | 44.5 | 5.5 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+money_moving | total | 2-1 | 66.7 | 44.5 | 22.2 | +0.82 | 27.3 | 3.67 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | total | 1-1 | 50.0 | 44.5 | 5.5 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 2-1 | 66.7 | 44.5 | 22.2 | +0.82 | 27.3 | 3.67 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+rlm_ratio | total | 1-1 | 50.0 | 44.5 | 5.5 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| follow_move+pin_value | total | 2-2 | 50.0 | 47.3 | 2.7 | -0.18 | -4.5 | -1.0 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | total | 1-0 | 100.0 | 55.5 | 44.5 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+pin_value | total | 3-0 | 100.0 | 51.8 | 48.2 | +2.73 | 90.9 | 0.67 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | total | 1-1 | 50.0 | 55.5 | -5.5 | -0.09 | -4.5 | 1.5 | 50.0 | keep collecting (2/30) |
| money_level+pin_value | total | 2-1 | 66.7 | 51.8 | 14.8 | +0.82 | 27.3 | 1.33 | 66.7 | keep collecting (3/30) |
| pin_move+pin_value | total | 2-3 | 40.0 | 53.3 | -13.3 | -1.18 | -23.6 | 0.6 | 40.0 | keep collecting (5/30) |
| consensus_gap+money_delta | total | 1-0 | 100.0 | 44.5 | 55.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_moving | total | 1-0 | 100.0 | 44.5 | 55.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 1-0 | 100.0 | 44.5 | 55.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | total | 1-0 | 100.0 | 44.5 | 55.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 44.5 | 55.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+rlm_ratio | total | 1-0 | 100.0 | 44.5 | 55.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | 2.0 | 100.0 | keep collecting (2/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 55.5 | -55.5 | -1.0 | -100.0 | 3.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 52-106 | 32.9 | 42.0 | -9.1 | -38.5 | -24.4 |  |  | DROP: below break-even |
| pin_move | both | 101-120 | 45.7 | 49.5 | -3.8 | -24.16 | -10.9 |  |  | DROP: below break-even |
| money_delta | both | 56-68 | 45.2 | 42.7 | 2.5 | -8.73 | -7.0 |  |  | DROP: below break-even |
| pin_rlm | both | 18-34 | 34.6 | 40.7 | -6.0 | -12.28 | -23.6 |  |  | DROP: below break-even |
| follow_move | both | 163-209 | 43.8 | 49.5 | -5.6 | -55.95 | -15.0 |  |  | DROP: below break-even |
| rlm_ratio | both | 31-63 | 33.0 | 40.8 | -7.8 | -29.13 | -31.0 |  |  | DROP: below break-even |
| money_level | both | 230-162 | 58.7 | 56.2 | 2.5 | +1.47 | 0.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 167-200 | 45.5 | 48.0 | -2.5 | -43.8 | -11.9 |  |  | DROP: below break-even |
| money_moving | both | 175-195 | 47.3 | 48.7 | -1.4 | -35.43 | -9.6 |  |  | DROP: below break-even |
| pin_value | both | 89-73 | 54.9 | 49.9 | 5.1 | +21.11 | 13.0 |  |  | no edge shown yet |
| consensus_gap | both | 83-52 | 61.5 | 53.7 | 7.8 | +14.09 | 10.4 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+pin_move | both | 68-105 | 39.3 | 49.3 | -10.0 | -40.06 | -23.2 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 44-50 | 46.8 | 41.6 | 5.2 | -1.81 | -1.9 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 44-49 | 47.3 | 41.6 | 5.7 | -0.81 | -0.9 |  |  | no edge shown yet |
| money_moving+sharp_gap | both | 163-190 | 46.2 | 48.3 | -2.1 | -36.11 | -10.2 |  |  | DROP: below break-even |
| consensus_gap+money_level | both | 58-27 | 68.2 | 59.9 | 8.3 | +7.31 | 8.6 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+rlm_quiet | both | 52-106 | 32.9 | 42.0 | -9.1 | -38.5 | -24.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | both | 27-54 | 33.3 | 43.7 | -10.4 | -22.68 | -28.0 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 25-21 | 54.3 | 52.7 | 1.6 | -1.45 | -3.1 |  |  | no edge shown yet |
| follow_move+money_level | both | 81-69 | 54.0 | 57.1 | -3.1 | -11.06 | -7.4 |  |  | no edge shown yet |
| money_level+money_moving | both | 120-99 | 54.8 | 53.9 | 0.9 | -4.38 | -2.0 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 113-98 | 53.6 | 53.4 | 0.1 | -5.84 | -2.8 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 29-27 | 51.8 | 52.1 | -0.3 | +1.03 | 1.8 |  |  | no edge shown yet |
| consensus_gap+pin_move | both | 21-11 | 65.6 | 50.8 | 14.9 | +9.17 | 28.6 |  |  | no edge shown yet |
| consensus_gap+pin_value | both | 30-18 | 62.5 | 49.4 | 13.1 | +12.05 | 25.1 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | both | 30-28 | 51.7 | 51.7 | 0.1 | +0.35 | 0.6 |  |  | no edge shown yet |
| follow_move+money_moving | both | 76-104 | 42.2 | 48.5 | -6.3 | -36.08 | -20.0 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 27-24 | 52.9 | 51.2 | 1.7 | +9.84 | 19.3 |  |  | no edge shown yet |
| follow_move+sharp_gap | both | 77-108 | 41.6 | 48.0 | -6.4 | -38.15 | -20.6 |  |  | DROP: below break-even |
| money_level+pin_move | both | 46-41 | 52.9 | 55.1 | -2.2 | -4.4 | -5.1 |  |  | no edge shown yet |
| money_level+pin_value | both | 39-28 | 58.2 | 51.7 | 6.6 | +6.17 | 9.2 |  |  | no edge shown yet |
| money_moving+pin_move | both | 42-53 | 44.2 | 47.9 | -3.7 | -11.67 | -12.3 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 31-34 | 47.7 | 49.6 | -1.9 | -2.97 | -4.6 |  |  | no edge shown yet |
| pin_move+pin_value | both | 34-29 | 54.0 | 51.1 | 2.8 | +1.13 | 1.8 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 40-57 | 41.2 | 47.2 | -6.0 | -17.45 | -18.0 |  |  | DROP: below break-even |
| pin_value+sharp_gap | both | 30-33 | 47.6 | 49.3 | -1.6 | -2.88 | -4.6 |  |  | no edge shown yet |
| follow_move+money_delta | both | 30-46 | 39.5 | 43.8 | -4.4 | -17.62 | -23.2 |  |  | DROP: below break-even |
| money_delta+pin_move | both | 16-22 | 42.1 | 42.8 | -0.7 | -6.66 | -17.5 |  |  | no edge shown yet |
| money_delta+rlm_quiet | both | 17-35 | 32.7 | 41.8 | -9.1 | -18.65 | -35.9 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | both | 31-63 | 33.0 | 40.8 | -7.8 | -29.13 | -31.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | both | 20-52 | 27.8 | 40.1 | -12.3 | -28.56 | -39.7 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 31-59 | 34.4 | 41.0 | -6.6 | -25.13 | -27.9 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 15-48 | 23.8 | 38.8 | -15.0 | -29.71 | -47.2 |  |  | INVERT candidate: wrong well beyond its base rate |
| rlm_quiet+sharp_gap | both | 20-57 | 26.0 | 39.8 | -13.8 | -33.56 | -43.6 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 31-63 | 33.0 | 40.8 | -7.8 | -29.13 | -31.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | both | 15-7 | 68.2 | 46.9 | 21.3 | +8.34 | 37.9 |  |  | keep collecting (22/30) |
| consensus_gap+rlm_quiet | both | 6-12 | 33.3 | 39.7 | -6.3 | -4.96 | -27.6 |  |  | keep collecting (18/30) |
| consensus_gap+rlm_ratio | both | 5-7 | 41.7 | 39.9 | 1.7 | -0.95 | -7.9 |  |  | keep collecting (12/30) |
| money_delta+rlm_ratio | both | 21-32 | 39.6 | 41.3 | -1.7 | -11.81 | -22.3 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 2-5 | 28.6 | 44.5 | -15.9 | -1.6 | -22.9 |  |  | keep collecting (7/30) |
| money_level+pin_rlm | both | 7-4 | 63.6 | 45.5 | 18.1 | +2.75 | 25.0 |  |  | keep collecting (11/30) |
| money_moving+pin_rlm | both | 18-30 | 37.5 | 41.0 | -3.5 | -8.28 | -17.2 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 18-34 | 34.6 | 40.7 | -6.0 | -12.28 | -23.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | both | 13-11 | 54.2 | 46.4 | 7.8 | +1.19 | 4.9 |  |  | keep collecting (24/30) |
| consensus_gap+money_delta | both | 8-4 | 66.7 | 43.7 | 22.9 | +6.81 | 56.8 |  |  | keep collecting (12/30) |
| follow_move+pin_rlm | both | 16-30 | 34.8 | 40.1 | -5.3 | -10.51 | -22.8 |  |  | DROP: below break-even |
| money_delta+pin_rlm | both | 10-16 | 38.5 | 39.4 | -0.9 | -6.13 | -23.6 |  |  | keep collecting (26/30) |
| pin_move+pin_rlm | both | 17-29 | 37.0 | 40.9 | -3.9 | -8.62 | -18.7 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | both | 16-28 | 36.4 | 41.5 | -5.1 | -9.0 | -20.5 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 8-25 | 24.2 | 39.4 | -15.2 | -13.6 | -41.2 |  |  | INVERT candidate: wrong well beyond its base rate |
| pin_rlm+rlm_ratio | both | 16-30 | 34.8 | 40.1 | -5.3 | -10.51 | -22.8 |  |  | DROP: below break-even |
| money_delta+pin_value | both | 12-6 | 66.7 | 46.5 | 20.2 | +8.44 | 46.9 |  |  | keep collecting (18/30) |
| pin_value+rlm_quiet | both | 8-12 | 40.0 | 46.5 | -6.5 | +5.01 | 25.0 |  |  | keep collecting (20/30) |
| pin_value+rlm_ratio | both | 5-4 | 55.6 | 48.3 | 7.2 | +0.4 | 4.5 |  |  | keep collecting (9/30) |
| pin_rlm+pin_value | both | 3-5 | 37.5 | 47.4 | -9.9 | -2.31 | -28.9 |  |  | keep collecting (8/30) |
| rlm_quiet | moneyline | 18-47 | 27.7 | 33.8 | -6.2 | -11.31 | -17.4 |  |  | DROP: below break-even |
| rlm_quiet | spread | 11-15 | 42.3 | 55.2 | -12.9 | -4.6 | -17.7 |  |  | keep collecting (26/30) |
| rlm_quiet | total | 23-44 | 34.3 | 44.8 | -10.5 | -22.58 | -33.7 |  |  | DROP: below break-even |
| pin_move | moneyline | 29-28 | 50.9 | 46.2 | 4.7 | +2.44 | 4.3 |  |  | no edge shown yet |
| pin_move | spread | 37-36 | 50.7 | 52.1 | -1.4 | -2.58 | -3.5 |  |  | no edge shown yet |
| pin_move | total | 35-56 | 38.5 | 49.3 | -10.9 | -24.02 | -26.4 |  |  | DROP: below break-even |
| money_delta | moneyline | 16-28 | 36.4 | 36.4 | -0.0 | -5.67 | -12.9 |  |  | DROP: below break-even |
| money_delta | spread | 9-8 | 52.9 | 50.4 | 2.5 | +0.29 | 1.7 |  |  | keep collecting (17/30) |
| money_delta | total | 31-32 | 49.2 | 45.0 | 4.2 | -3.36 | -5.3 |  |  | no edge shown yet |
| pin_rlm | moneyline | 8-16 | 33.3 | 34.7 | -1.4 | -3.5 | -14.6 |  |  | keep collecting (24/30) |
| pin_rlm | spread | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| pin_rlm | total | 9-18 | 33.3 | 45.3 | -12.0 | -9.69 | -35.9 |  |  | keep collecting (27/30) |
| follow_move | moneyline | 61-71 | 46.2 | 48.0 | -1.8 | -11.83 | -9.0 |  |  | no edge shown yet |
| follow_move | spread | 45-53 | 45.9 | 52.2 | -6.3 | -11.45 | -11.7 |  |  | no edge shown yet |
| follow_move | total | 57-85 | 40.1 | 48.9 | -8.8 | -32.67 | -23.0 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 11-33 | 25.0 | 34.1 | -9.1 | -17.45 | -39.7 |  |  | DROP: below break-even |
| rlm_ratio | spread | 1-2 | 33.3 | 52.3 | -18.9 | -1.15 | -38.4 |  |  | keep collecting (3/30) |
| rlm_ratio | total | 19-28 | 40.4 | 46.4 | -6.0 | -10.52 | -22.4 |  |  | DROP: below break-even |
| money_level | moneyline | 96-45 | 68.1 | 63.8 | 4.3 | -2.11 | -1.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 50-47 | 51.5 | 48.8 | 2.7 | -2.13 | -2.2 |  |  | no edge shown yet |
| money_level | total | 84-70 | 54.5 | 53.9 | 0.6 | +5.71 | 3.7 |  |  | no edge shown yet |
| sharp_gap | moneyline | 56-73 | 43.4 | 45.2 | -1.8 | -17.79 | -13.8 |  |  | DROP: below break-even |
| sharp_gap | spread | 44-53 | 45.4 | 48.8 | -3.5 | -13.13 | -13.5 |  |  | no edge shown yet |
| sharp_gap | total | 67-74 | 47.5 | 50.0 | -2.5 | -12.88 | -9.1 |  |  | no edge shown yet |
| money_moving | moneyline | 62-65 | 48.8 | 47.0 | 1.8 | -8.17 | -6.4 |  |  | no edge shown yet |
| money_moving | spread | 44-53 | 45.4 | 48.8 | -3.5 | -13.13 | -13.5 |  |  | no edge shown yet |
| money_moving | total | 69-77 | 47.3 | 50.2 | -3.0 | -14.13 | -9.7 |  |  | no edge shown yet |
| pin_value | moneyline | 5-4 | 55.6 | 40.7 | 14.8 | +16.16 | 179.6 |  |  | keep collecting (9/30) |
| pin_value | spread | 40-33 | 54.8 | 49.5 | 5.3 | +1.47 | 2.0 |  |  | no edge shown yet |
| pin_value | total | 44-36 | 55.0 | 51.2 | 3.8 | +3.48 | 4.3 |  |  | no edge shown yet |
| consensus_gap | moneyline | 45-28 | 61.6 | 56.2 | 5.5 | +4.86 | 6.7 |  |  | PROMOTE: beats break-even and its own base rate |
| consensus_gap | spread | 17-10 | 63.0 | 48.2 | 14.7 | +4.59 | 17.0 |  |  | keep collecting (27/30) |
| consensus_gap | total | 21-14 | 60.0 | 52.7 | 7.3 | +4.64 | 13.3 |  |  | no edge shown yet |
| consensus_gap+money_level | moneyline | 36-11 | 76.6 | 66.0 | 10.6 | +4.04 | 8.6 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+pin_move | moneyline | 21-27 | 43.8 | 45.8 | -2.1 | -5.17 | -10.8 |  |  | no edge shown yet |
| follow_move+rlm_quiet | moneyline | 18-47 | 27.7 | 33.8 | -6.2 | -11.31 | -17.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | moneyline | 9-19 | 32.1 | 34.5 | -2.4 | -4.53 | -16.2 |  |  | keep collecting (28/30) |
| consensus_gap+follow_move | moneyline | 15-12 | 55.6 | 53.1 | 2.5 | -1.34 | -5.0 |  |  | keep collecting (27/30) |
| follow_move+money_level | moneyline | 38-20 | 65.5 | 63.8 | 1.7 | -1.32 | -2.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 54-64 | 45.8 | 45.8 | -0.0 | -9.24 | -7.8 |  |  | no edge shown yet |
| follow_move+money_moving | moneyline | 31-38 | 44.9 | 45.9 | -1.0 | -11.28 | -16.3 |  |  | no edge shown yet |
| follow_move+sharp_gap | moneyline | 30-42 | 41.7 | 44.9 | -3.2 | -15.21 | -21.1 |  |  | DROP: below break-even |
| money_level+money_moving | moneyline | 43-21 | 67.2 | 60.4 | 6.8 | +4.08 | 6.4 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+sharp_gap | moneyline | 37-21 | 63.8 | 59.8 | 4.0 | +2.46 | 4.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+rlm_ratio | moneyline | 11-33 | 25.0 | 34.1 | -9.1 | -17.45 | -39.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | moneyline | 8-26 | 23.5 | 33.3 | -9.8 | -13.68 | -40.2 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 11-30 | 26.8 | 34.1 | -7.3 | -14.45 | -35.3 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | moneyline | 6-28 | 17.6 | 33.3 | -15.7 | -18.06 | -53.1 |  |  | INVERT candidate: wrong well beyond its base rate |
| rlm_quiet+sharp_gap | moneyline | 8-30 | 21.1 | 33.3 | -12.3 | -17.68 | -46.5 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 11-33 | 25.0 | 34.1 | -9.1 | -17.45 | -39.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 16-12 | 57.1 | 53.6 | 3.6 | +4.56 | 16.3 |  |  | keep collecting (28/30) |
| consensus_gap+rlm_quiet | moneyline | 2-9 | 18.2 | 33.3 | -15.2 | -5.6 | -50.9 |  |  | keep collecting (11/30) |
| consensus_gap+rlm_ratio | moneyline | 2-5 | 28.6 | 33.3 | -4.8 | -1.6 | -22.9 |  |  | keep collecting (7/30) |
| consensus_gap+sharp_gap | moneyline | 17-14 | 54.8 | 52.7 | 2.2 | +2.87 | 9.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 2-2 | 50.0 | 41.7 | 8.3 | +1.4 | 35.0 |  |  | keep collecting (4/30) |
| money_level+pin_rlm | moneyline | 2-1 | 66.7 | 44.4 | 22.2 | +1.16 | 38.7 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | moneyline | 8-13 | 38.1 | 34.9 | 3.2 | -0.5 | -2.4 |  |  | keep collecting (21/30) |
| pin_rlm+sharp_gap | moneyline | 8-16 | 33.3 | 34.7 | -1.4 | -3.5 | -14.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 3-2 | 60.0 | 40.0 | 20.0 | +4.46 | 89.3 |  |  | keep collecting (5/30) |
| money_level+rlm_ratio | moneyline | 3-3 | 50.0 | 38.9 | 11.1 | +0.09 | 1.4 |  |  | keep collecting (6/30) |
| consensus_gap+pin_move | moneyline | 12-4 | 75.0 | 50.0 | 25.0 | +8.35 | 52.2 |  |  | keep collecting (16/30) |
| money_level+pin_move | moneyline | 15-6 | 71.4 | 63.5 | 7.9 | +2.87 | 13.7 |  |  | keep collecting (21/30) |
| consensus_gap+money_delta | moneyline | 3-3 | 50.0 | 38.9 | 11.1 | +3.35 | 55.8 |  |  | keep collecting (6/30) |
| follow_move+money_delta | moneyline | 8-18 | 30.8 | 38.5 | -7.7 | -9.92 | -38.1 |  |  | keep collecting (26/30) |
| follow_move+pin_rlm | moneyline | 7-13 | 35.0 | 33.3 | 1.7 | -1.82 | -9.1 |  |  | keep collecting (20/30) |
| money_delta+money_moving | moneyline | 15-26 | 36.6 | 35.8 | 0.8 | -4.52 | -11.0 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 4-6 | 40.0 | 33.3 | 6.7 | -1.76 | -17.6 |  |  | keep collecting (10/30) |
| money_delta+pin_rlm | moneyline | 4-8 | 33.3 | 33.3 | -0.0 | -3.76 | -31.3 |  |  | keep collecting (12/30) |
| money_delta+rlm_quiet | moneyline | 3-15 | 16.7 | 33.3 | -16.7 | -11.66 | -64.8 |  |  | keep collecting (18/30) |
| money_delta+rlm_ratio | moneyline | 5-17 | 22.7 | 34.8 | -12.1 | -11.5 | -52.3 |  |  | keep collecting (22/30) |
| money_delta+sharp_gap | moneyline | 15-26 | 36.6 | 35.8 | 0.8 | -4.52 | -11.0 |  |  | DROP: below break-even |
| money_moving+pin_move | moneyline | 11-9 | 55.0 | 40.0 | 15.0 | +4.41 | 22.1 |  |  | keep collecting (20/30) |
| pin_move+pin_rlm | moneyline | 7-11 | 38.9 | 33.3 | 5.6 | +0.16 | 0.9 |  |  | keep collecting (18/30) |
| pin_move+rlm_ratio | moneyline | 6-10 | 37.5 | 33.3 | 4.2 | -0.16 | -1.0 |  |  | keep collecting (16/30) |
| pin_move+sharp_gap | moneyline | 11-12 | 47.8 | 39.1 | 8.7 | +1.41 | 6.1 |  |  | keep collecting (23/30) |
| pin_rlm+rlm_quiet | moneyline | 4-12 | 25.0 | 33.3 | -8.3 | -4.32 | -27.0 |  |  | keep collecting (16/30) |
| pin_rlm+rlm_ratio | moneyline | 7-13 | 35.0 | 33.3 | 1.7 | -1.82 | -9.1 |  |  | keep collecting (20/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 44.4 | -11.1 | +8.6 | 286.7 |  |  | keep collecting (3/30) |
| pin_value+rlm_quiet | moneyline | 1-1 | 50.0 | 33.3 | 16.7 | +9.6 | 480.0 |  |  | keep collecting (2/30) |
| money_delta+money_level | moneyline | 6-1 | 85.7 | 47.6 | 38.1 | +6.07 | 86.8 |  |  | keep collecting (7/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_move+pin_value | moneyline | 1-2 | 33.3 | 44.4 | -11.1 | -0.92 | -30.7 |  |  | keep collecting (3/30) |
| money_delta+pin_value | moneyline | 1-0 | 100.0 | 33.3 | 66.7 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 1-1 | 50.0 | 33.3 | 16.7 | +3.5 | 175.0 |  |  | keep collecting (2/30) |
| pin_value+sharp_gap | moneyline | 1-1 | 50.0 | 33.3 | 16.7 | +3.5 | 175.0 |  |  | keep collecting (2/30) |
| follow_move+pin_move | spread | 21-30 | 41.2 | 52.8 | -11.6 | -10.78 | -21.1 |  |  | DROP: below break-even |
| money_moving+sharp_gap | spread | 44-53 | 45.4 | 48.8 | -3.5 | -13.13 | -13.5 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 11-15 | 42.3 | 55.2 | -12.9 | -4.6 | -17.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | spread | 32-35 | 47.8 | 48.3 | -0.5 | -6.17 | -9.2 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 32-35 | 47.8 | 48.3 | -0.5 | -6.17 | -9.2 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 6-12 | 33.3 | 55.3 | -21.9 | -6.35 | -35.3 |  |  | keep collecting (18/30) |
| consensus_gap+pin_value | spread | 14-8 | 63.6 | 48.8 | 14.9 | +4.08 | 18.6 |  |  | keep collecting (22/30) |
| follow_move+money_level | spread | 13-12 | 52.0 | 53.0 | -1.0 | -0.04 | -0.2 |  |  | keep collecting (25/30) |
| follow_move+money_moving | spread | 12-15 | 44.4 | 52.8 | -8.3 | -4.0 | -14.8 |  |  | keep collecting (27/30) |
| follow_move+sharp_gap | spread | 12-15 | 44.4 | 52.8 | -8.3 | -4.0 | -14.8 |  |  | keep collecting (27/30) |
| money_level+pin_move | spread | 11-10 | 52.4 | 51.0 | 1.4 | -0.3 | -1.4 |  |  | keep collecting (21/30) |
| money_moving+pin_move | spread | 11-12 | 47.8 | 50.9 | -3.1 | -2.28 | -9.9 |  |  | keep collecting (23/30) |
| pin_move+sharp_gap | spread | 11-12 | 47.8 | 50.9 | -3.1 | -2.28 | -9.9 |  |  | keep collecting (23/30) |
| money_delta+money_level | spread | 3-1 | 75.0 | 46.6 | 28.4 | +1.7 | 42.5 |  |  | keep collecting (4/30) |
| money_delta+money_moving | spread | 6-6 | 50.0 | 48.9 | 1.1 | -0.57 | -4.8 |  |  | keep collecting (12/30) |
| money_delta+sharp_gap | spread | 6-6 | 50.0 | 48.9 | 1.1 | -0.57 | -4.8 |  |  | keep collecting (12/30) |
| consensus_gap+money_level | spread | 5-7 | 41.7 | 46.6 | -4.9 | -2.73 | -22.8 |  |  | keep collecting (12/30) |
| consensus_gap+money_moving | spread | 4-5 | 44.4 | 47.7 | -3.3 | -1.53 | -17.0 |  |  | keep collecting (9/30) |
| consensus_gap+sharp_gap | spread | 4-5 | 44.4 | 47.7 | -3.3 | -1.53 | -17.0 |  |  | keep collecting (9/30) |
| money_level+pin_value | spread | 15-11 | 57.7 | 46.9 | 10.8 | +1.79 | 6.9 |  |  | keep collecting (26/30) |
| money_moving+pin_value | spread | 13-15 | 46.4 | 48.5 | -2.1 | -3.77 | -13.5 |  |  | keep collecting (28/30) |
| pin_value+sharp_gap | spread | 13-15 | 46.4 | 48.5 | -2.1 | -3.77 | -13.5 |  |  | keep collecting (28/30) |
| follow_move+money_delta | spread | 4-3 | 57.1 | 54.8 | 2.3 | +0.65 | 9.2 |  |  | keep collecting (7/30) |
| follow_move+rlm_ratio | spread | 1-2 | 33.3 | 52.3 | -18.9 | -1.15 | -38.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.15 | -7.7 |  |  | keep collecting (2/30) |
| money_moving+rlm_ratio | spread | 1-2 | 33.3 | 52.3 | -18.9 | -1.15 | -38.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 1-2 | 33.3 | 52.3 | -18.9 | -1.15 | -38.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 10-7 | 58.8 | 53.6 | 5.2 | +1.85 | 10.9 |  |  | keep collecting (17/30) |
| pin_move+pin_value | spread | 19-10 | 65.5 | 52.1 | 13.4 | +6.52 | 22.5 |  |  | keep collecting (29/30) |
| consensus_gap+pin_move | spread | 6-2 | 75.0 | 51.7 | 23.3 | +3.16 | 39.5 |  |  | keep collecting (8/30) |
| consensus_gap+follow_move | spread | 3-2 | 60.0 | 54.1 | 5.9 | +0.67 | 13.3 |  |  | keep collecting (5/30) |
| consensus_gap+rlm_quiet | spread | 2-0 | 100.0 | 56.8 | 43.2 | +1.82 | 90.9 |  |  | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 2-3 | 40.0 | 56.8 | -16.8 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| money_delta+rlm_quiet | spread | 3-2 | 60.0 | 56.8 | 3.2 | +0.8 | 16.0 |  |  | keep collecting (5/30) |
| money_moving+rlm_quiet | spread | 1-4 | 20.0 | 54.1 | -34.1 | -3.09 | -61.8 |  |  | keep collecting (5/30) |
| rlm_quiet+rlm_ratio | spread | 0-1 | 0.0 | 56.8 | -56.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_quiet+sharp_gap | spread | 1-4 | 20.0 | 54.1 | -34.1 | -3.09 | -61.8 |  |  | keep collecting (5/30) |
| consensus_gap+money_delta | spread | 2-0 | 100.0 | 56.8 | 43.2 | +1.76 | 87.8 |  |  | keep collecting (2/30) |
| money_delta+pin_move | spread | 3-2 | 60.0 | 54.1 | 5.9 | +0.67 | 13.3 |  |  | keep collecting (5/30) |
| money_delta+pin_value | spread | 2-2 | 50.0 | 53.4 | -3.4 | -0.24 | -6.1 |  |  | keep collecting (4/30) |
| money_moving+pin_rlm | spread | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | spread | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | spread | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 1-0 | 100.0 | 56.8 | 43.2 | +0.91 | 90.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+rlm_ratio | spread | 1-0 | 100.0 | 56.8 | 43.2 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| money_level+rlm_ratio | spread | 1-0 | 100.0 | 56.8 | 43.2 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| pin_move+rlm_ratio | spread | 1-0 | 100.0 | 56.8 | 43.2 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| pin_value+rlm_ratio | spread | 1-0 | 100.0 | 56.8 | 43.2 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| money_delta+money_moving | total | 23-18 | 56.1 | 45.3 | 10.8 | +3.28 | 8.0 |  |  | no edge shown yet |
| money_delta+sharp_gap | total | 23-17 | 57.5 | 45.3 | 12.2 | +4.28 | 10.7 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 65-73 | 47.1 | 50.1 | -3.0 | -13.73 | -9.9 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 23-44 | 34.3 | 44.8 | -10.5 | -22.58 | -33.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+follow_move | total | 7-7 | 50.0 | 51.6 | -1.6 | -0.77 | -5.5 |  |  | keep collecting (14/30) |
| consensus_gap+money_level | total | 17-9 | 65.4 | 55.1 | 10.3 | +6.01 | 23.1 |  |  | keep collecting (26/30) |
| consensus_gap+money_moving | total | 9-10 | 47.4 | 52.0 | -4.7 | -1.99 | -10.5 |  |  | keep collecting (19/30) |
| consensus_gap+pin_move | total | 3-5 | 37.5 | 51.4 | -13.9 | -2.35 | -29.4 |  |  | keep collecting (8/30) |
| consensus_gap+pin_value | total | 13-8 | 61.9 | 52.4 | 9.6 | +3.5 | 16.7 |  |  | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 9-9 | 50.0 | 51.8 | -1.8 | -0.99 | -5.5 |  |  | keep collecting (18/30) |
| follow_move+money_level | total | 30-37 | 44.8 | 52.9 | -8.1 | -9.7 | -14.5 |  |  | no edge shown yet |
| follow_move+money_moving | total | 33-51 | 39.3 | 49.2 | -9.9 | -20.79 | -24.8 |  |  | DROP: below break-even |
| follow_move+pin_move | total | 26-48 | 35.1 | 49.1 | -14.0 | -24.1 | -32.6 |  |  | DROP: below break-even |
| follow_move+pin_value | total | 16-15 | 51.6 | 50.5 | 1.1 | -0.6 | -2.0 |  |  | no edge shown yet |
| follow_move+sharp_gap | total | 35-51 | 40.7 | 49.1 | -8.4 | -18.94 | -22.0 |  |  | DROP: below break-even |
| money_level+money_moving | total | 45-43 | 51.1 | 53.4 | -2.2 | -2.3 | -2.6 |  |  | no edge shown yet |
| money_level+pin_move | total | 20-25 | 44.4 | 53.0 | -8.6 | -6.97 | -15.5 |  |  | no edge shown yet |
| money_level+pin_value | total | 24-16 | 60.0 | 54.4 | 5.6 | +5.39 | 13.5 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 44-42 | 51.2 | 53.2 | -2.0 | -2.14 | -2.5 |  |  | no edge shown yet |
| money_moving+pin_move | total | 20-32 | 38.5 | 49.6 | -11.1 | -13.81 | -26.5 |  |  | DROP: below break-even |
| money_moving+pin_value | total | 17-18 | 48.6 | 51.4 | -2.8 | -2.7 | -7.7 |  |  | no edge shown yet |
| pin_move+pin_value | total | 14-17 | 45.2 | 50.9 | -5.7 | -4.46 | -14.4 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 18-33 | 35.3 | 49.2 | -14.0 | -16.58 | -32.5 |  |  | DROP: below break-even |
| pin_value+sharp_gap | total | 16-17 | 48.5 | 50.8 | -2.3 | -2.61 | -7.9 |  |  | no edge shown yet |
| follow_move+money_delta | total | 18-25 | 41.9 | 45.3 | -3.4 | -8.35 | -19.4 |  |  | no edge shown yet |
| money_delta+pin_move | total | 9-14 | 39.1 | 44.5 | -5.4 | -5.56 | -24.2 |  |  | keep collecting (23/30) |
| money_delta+rlm_quiet | total | 11-18 | 37.9 | 44.5 | -6.6 | -7.79 | -26.8 |  |  | keep collecting (29/30) |
| pin_move+rlm_quiet | total | 12-23 | 34.3 | 45.1 | -10.9 | -11.79 | -33.7 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | total | 19-28 | 40.4 | 46.4 | -6.0 | -10.52 | -22.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | total | 15-14 | 51.7 | 45.7 | 6.1 | -0.16 | -0.6 |  |  | keep collecting (29/30) |
| money_moving+rlm_quiet | total | 11-22 | 33.3 | 44.8 | -11.5 | -11.79 | -35.7 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | total | 19-27 | 41.3 | 46.4 | -5.1 | -9.52 | -20.7 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | total | 9-19 | 32.1 | 44.9 | -12.8 | -10.65 | -38.0 |  |  | keep collecting (28/30) |
| rlm_quiet+sharp_gap | total | 11-23 | 32.4 | 44.8 | -12.5 | -12.79 | -37.6 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | total | 19-28 | 40.4 | 46.4 | -6.0 | -10.52 | -22.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | total | 3-1 | 75.0 | 44.5 | 30.5 | +1.71 | 42.8 |  |  | keep collecting (4/30) |
| consensus_gap+rlm_quiet | total | 2-3 | 40.0 | 46.7 | -6.7 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| consensus_gap+rlm_ratio | total | 2-2 | 50.0 | 47.3 | 2.7 | -0.2 | -4.9 |  |  | keep collecting (4/30) |
| money_delta+pin_value | total | 9-4 | 69.2 | 45.4 | 23.9 | +4.18 | 32.2 |  |  | keep collecting (13/30) |
| pin_value+rlm_quiet | total | 5-8 | 38.5 | 44.5 | -6.1 | -3.41 | -26.2 |  |  | keep collecting (13/30) |
| pin_value+rlm_ratio | total | 4-4 | 50.0 | 47.3 | 2.7 | -0.44 | -5.5 |  |  | keep collecting (8/30) |
| follow_move+pin_rlm | total | 9-17 | 34.6 | 45.4 | -10.7 | -8.69 | -33.4 |  |  | keep collecting (26/30) |
| money_delta+money_level | total | 6-5 | 54.5 | 46.5 | 8.0 | +0.57 | 5.2 |  |  | keep collecting (11/30) |
| money_delta+pin_rlm | total | 6-8 | 42.9 | 44.5 | -1.7 | -2.37 | -17.0 |  |  | keep collecting (14/30) |
| money_level+pin_rlm | total | 5-3 | 62.5 | 45.9 | 16.6 | +1.59 | 19.9 |  |  | keep collecting (8/30) |
| money_level+rlm_ratio | total | 9-8 | 52.9 | 48.4 | 4.6 | +0.25 | 1.5 |  |  | keep collecting (17/30) |
| money_moving+pin_rlm | total | 9-17 | 34.6 | 45.4 | -10.7 | -8.69 | -33.4 |  |  | keep collecting (26/30) |
| pin_move+pin_rlm | total | 9-18 | 33.3 | 45.3 | -12.0 | -9.69 | -35.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 9-18 | 33.3 | 45.7 | -12.4 | -9.69 | -35.9 |  |  | keep collecting (27/30) |
| pin_rlm+rlm_ratio | total | 9-17 | 34.6 | 45.4 | -10.7 | -8.69 | -33.4 |  |  | keep collecting (26/30) |
| pin_rlm+sharp_gap | total | 9-18 | 33.3 | 45.3 | -12.0 | -9.69 | -35.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | total | 4-13 | 23.5 | 45.2 | -21.6 | -9.28 | -54.6 |  |  | keep collecting (17/30) |
| consensus_gap+pin_rlm | total | 0-3 | 0.0 | 48.2 | -48.2 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_rlm+pin_value | total | 2-5 | 28.6 | 46.1 | -17.5 | -3.22 | -46.0 |  |  | keep collecting (7/30) |

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
| rlm_quiet | both | 39-54 | 41.9 | 36.7 | 5.2 | +3.99 | 4.3 | 0.38 | 45.2 | DROP: below break-even |
| pin_move | both | 9-15 | 37.5 | 48.8 | -11.3 | -7.46 | -31.1 | 0.25 | 41.7 | keep collecting (24/30) |
| money_delta | both | 12-10 | 54.5 | 41.7 | 12.8 | +3.25 | 14.8 | 0.51 | 45.5 | keep collecting (22/30) |
| pin_rlm | both | 1-3 | 25.0 | 39.0 | -14.0 | -2.07 | -51.8 | -0.37 | 75.0 | keep collecting (4/30) |
| follow_move | both | 578-523 | 52.5 | 51.5 | 1.0 | -72.13 | -6.6 | 0.19 | 41.1 | no edge shown yet |
| rlm_ratio | both | 34-28 | 54.8 | 40.0 | 14.9 | +14.93 | 24.1 | 0.52 | 53.2 | no edge shown yet |
| money_level | both | 208-139 | 59.9 | 58.8 | 1.1 | -18.11 | -5.2 | -0.14 | 39.2 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 168-156 | 51.9 | 48.1 | 3.8 | +7.86 | 2.4 | 0.36 | 45.4 | no edge shown yet |
| money_moving | both | 126-108 | 53.8 | 50.3 | 3.5 | -6.17 | -2.6 | 0.11 | 43.2 | no edge shown yet |
| pin_value | both | 61-61 | 50.0 | 48.7 | 1.3 | -6.87 | -5.6 | 0.07 | 36.9 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.8 | -31.8 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 286-340 | 45.7 | 48.4 | -2.7 | -59.24 | -9.5 | 0.38 | 45.7 | DROP: below break-even |
| consensus_gap+money_level | both | 44-35 | 55.7 | 62.5 | -6.8 | -11.36 | -14.4 | 0.2 | 46.8 | no edge shown yet |
| consensus_gap+money_moving | both | 21-26 | 44.7 | 47.3 | -2.6 | -7.26 | -15.4 | 0.32 | 44.7 | no edge shown yet |
| consensus_gap+pin_value | both | 25-29 | 46.3 | 47.0 | -0.7 | -7.24 | -13.4 | 0.34 | 46.3 | no edge shown yet |
| follow_move+rlm_quiet | both | 39-54 | 41.9 | 36.7 | 5.2 | +3.99 | 4.3 | 0.38 | 45.2 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 34-28 | 54.8 | 40.0 | 14.9 | +14.93 | 24.1 | 0.52 | 53.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 86-54 | 61.4 | 49.6 | 11.8 | +17.87 | 12.8 | 0.51 | 49.3 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 77-50 | 60.6 | 57.4 | 3.2 | -1.51 | -1.2 | -0.1 | 45.7 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 13-11 | 54.2 | 50.4 | 3.7 | +0.63 | 2.6 | 0.57 | 50.0 | keep collecting (24/30) |
| money_moving+pin_value | both | 10-7 | 58.8 | 50.8 | 8.1 | +1.78 | 10.5 | 0.39 | 41.2 | keep collecting (17/30) |
| rlm_quiet+rlm_ratio | both | 20-18 | 52.6 | 37.0 | 15.6 | +10.73 | 28.2 | 0.05 | 47.4 | no edge shown yet |
| rlm_quiet+sharp_gap | both | 22-22 | 50.0 | 37.2 | 12.8 | +8.55 | 19.4 | 0.02 | 45.5 | no edge shown yet |
| rlm_ratio+sharp_gap | both | 34-28 | 54.8 | 40.0 | 14.9 | +14.93 | 24.1 | 0.52 | 53.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 112-77 | 59.3 | 55.3 | 3.9 | -1.66 | -0.9 | 0.17 | 45.0 | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | both | 75-66 | 53.2 | 47.8 | 5.4 | +1.91 | 1.4 | 0.33 | 47.5 | no edge shown yet |
| money_delta+money_level | both | 4-4 | 50.0 | 44.6 | 5.4 | +0.37 | 4.6 | 1.38 | 75.0 | keep collecting (8/30) |
| money_delta+money_moving | both | 11-10 | 52.4 | 41.3 | 11.0 | +2.34 | 11.2 | 0.54 | 47.6 | keep collecting (21/30) |
| money_delta+pin_value | both | 4-1 | 80.0 | 49.8 | 30.2 | +2.52 | 50.4 | 0.2 | 40.0 | keep collecting (5/30) |
| money_delta+sharp_gap | both | 9-8 | 52.9 | 40.9 | 12.1 | +2.6 | 15.3 | 0.66 | 58.8 | keep collecting (17/30) |
| pin_value+sharp_gap | both | 14-10 | 58.3 | 49.8 | 8.6 | +2.57 | 10.7 | 0.08 | 41.7 | keep collecting (24/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 50.8 | -50.8 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 40-46 | 46.5 | 51.8 | -5.3 | -15.11 | -17.6 | 0.71 | 55.8 | no edge shown yet |
| consensus_gap+rlm_quiet | both | 4-7 | 36.4 | 37.4 | -1.1 | -2.99 | -27.1 | 0.95 | 72.7 | keep collecting (11/30) |
| follow_move+pin_value | both | 23-21 | 52.3 | 48.8 | 3.5 | -0.86 | -2.0 | -0.21 | 27.3 | no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 42.6 | -26.0 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 32-50 | 39.0 | 45.9 | -6.9 | -11.45 | -14.0 | 0.77 | 50.0 | DROP: below break-even |
| follow_move+money_level | both | 105-54 | 66.0 | 60.0 | 6.0 | -2.45 | -1.5 | 0.08 | 43.4 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 12-10 | 54.5 | 44.2 | 10.3 | +2.34 | 10.6 | 1.43 | 68.2 | keep collecting (22/30) |
| pin_value+rlm_ratio | both | 3-2 | 60.0 | 45.3 | 14.7 | +0.73 | 14.5 | -1.16 | 40.0 | keep collecting (5/30) |
| follow_move+money_moving | both | 64-40 | 61.5 | 52.1 | 9.5 | +7.7 | 7.4 | 0.34 | 50.0 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 4-0 | 100.0 | 49.4 | 50.6 | +3.52 | 88.0 | 0.25 | 25.0 | keep collecting (4/30) |
| follow_move+money_delta | both | 6-4 | 60.0 | 42.8 | 17.2 | +3.86 | 38.6 | 0.34 | 50.0 | keep collecting (10/30) |
| money_delta+rlm_quiet | both | 2-2 | 50.0 | 38.0 | 12.0 | +1.53 | 38.3 | -2.1 | 0.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | both | 16-16 | 50.0 | 37.2 | 12.8 | +5.23 | 16.4 | 0.38 | 43.8 | no edge shown yet |
| money_moving+rlm_ratio | both | 17-12 | 58.6 | 41.4 | 17.2 | +8.06 | 27.8 | 0.48 | 51.7 | keep collecting (29/30) |
| consensus_gap+rlm_ratio | both | 5-4 | 55.6 | 39.8 | 15.8 | +1.0 | 11.1 | 0.72 | 66.7 | keep collecting (9/30) |
| pin_move+pin_value | both | 3-9 | 25.0 | 49.3 | -24.3 | -6.27 | -52.3 | 0.33 | 25.0 | keep collecting (12/30) |
| follow_move+pin_move | both | 6-6 | 50.0 | 50.7 | -0.7 | -1.19 | -9.9 | 0.45 | 50.0 | keep collecting (12/30) |
| consensus_gap+pin_move | both | 1-5 | 16.7 | 45.5 | -28.8 | -4.09 | -68.2 | 0.22 | 50.0 | keep collecting (6/30) |
| money_level+pin_move | both | 3-3 | 50.0 | 54.1 | -4.1 | -0.96 | -16.0 | 0.57 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 27.9 | -27.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-2 | 33.3 | 42.6 | -9.3 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 27.9 | -27.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 27.9 | -27.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-2 | 33.3 | 42.6 | -9.3 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+sharp_gap | both | 1-3 | 25.0 | 39.0 | -14.0 | -2.07 | -51.8 | -0.37 | 75.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.1 | -51.1 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 49.2 | -49.2 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-2 | 50.0 | 50.4 | -0.4 | -0.87 | -21.7 | 0.7 | 50.0 | keep collecting (4/30) |
| money_level+pin_rlm | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.07 | -3.7 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 27.9 | 72.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 27.9 | 72.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 3-2 | 60.0 | 40.7 | 19.3 | +3.25 | 65.0 | 1.12 | 80.0 | keep collecting (5/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 27.9 | -27.9 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 21-34 | 38.2 | 27.9 | 10.2 | +7.7 | 14.0 | 0.2 | 43.6 | DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.4 | 10.6 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 15-18 | 45.5 | 49.4 | -4.0 | -4.36 | -13.2 | 0.85 | 54.5 | no edge shown yet |
| pin_move | moneyline | 2-3 | 40.0 | 45.6 | -5.6 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-6 | 14.3 | 48.7 | -34.4 | -5.09 | -72.7 | 0.29 | 28.6 | keep collecting (7/30) |
| pin_move | total | 6-6 | 50.0 | 50.1 | -0.1 | -0.5 | -4.2 | 0.33 | 41.7 | keep collecting (12/30) |
| money_delta | moneyline | 2-6 | 25.0 | 27.9 | -2.9 | -1.66 | -20.8 | -0.59 | 50.0 | keep collecting (8/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 9-3 | 75.0 | 49.5 | 25.5 | +5.08 | 42.3 | 1.25 | 41.7 | keep collecting (12/30) |
| pin_rlm | moneyline | 1-3 | 25.0 | 39.0 | -14.0 | -2.07 | -51.8 | -0.37 | 75.0 | keep collecting (4/30) |
| follow_move | moneyline | 241-162 | 59.8 | 54.4 | 5.4 | -20.26 | -5.0 | 0.14 | 43.4 | PROMOTE: beats break-even and its own base rate |
| follow_move | spread | 152-178 | 46.1 | 49.8 | -3.7 | -37.82 | -11.5 | -0.0 | 33.3 | DROP: below break-even |
| follow_move | total | 185-183 | 50.3 | 50.0 | 0.3 | -14.05 | -3.8 | 0.42 | 45.7 | no edge shown yet |
| rlm_ratio | moneyline | 14-16 | 46.7 | 29.4 | 17.3 | +8.47 | 28.2 | 0.35 | 53.3 | no edge shown yet |
| rlm_ratio | spread | 3-3 | 50.0 | 52.0 | -2.0 | -0.16 | -2.7 | 0.33 | 16.7 | keep collecting (6/30) |
| rlm_ratio | total | 17-9 | 65.4 | 49.3 | 16.0 | +6.62 | 25.5 | 0.77 | 61.5 | keep collecting (26/30) |
| money_level | moneyline | 117-55 | 68.0 | 67.7 | 0.3 | -16.68 | -9.7 | -0.24 | 42.4 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-18 | 48.6 | 49.1 | -0.5 | -2.69 | -7.7 | 1.0 | 51.4 | no edge shown yet |
| money_level | total | 74-66 | 52.9 | 50.4 | 2.5 | +1.26 | 0.9 | -0.31 | 32.1 | no edge shown yet |
| sharp_gap | moneyline | 71-82 | 46.4 | 46.1 | 0.3 | -6.31 | -4.1 | 0.39 | 51.6 | no edge shown yet |
| sharp_gap | spread | 20-15 | 57.1 | 49.7 | 7.4 | +3.0 | 8.6 | 0.77 | 40.0 | no edge shown yet |
| sharp_gap | total | 77-59 | 56.6 | 49.9 | 6.8 | +11.16 | 8.2 | 0.21 | 39.7 | no edge shown yet |
| money_moving | moneyline | 54-57 | 48.6 | 51.0 | -2.3 | -20.51 | -18.5 | -0.01 | 49.5 | no edge shown yet |
| money_moving | spread | 18-6 | 75.0 | 49.0 | 26.0 | +10.18 | 42.4 | 0.5 | 45.8 | keep collecting (24/30) |
| money_moving | total | 54-45 | 54.5 | 49.9 | 4.6 | +4.17 | 4.2 | 0.15 | 35.4 | no edge shown yet |
| pin_value | moneyline | 2-7 | 22.2 | 37.7 | -15.5 | -5.31 | -59.0 | 0.12 | 55.6 | keep collecting (9/30) |
| pin_value | spread | 31-27 | 53.4 | 49.1 | 4.4 | +0.17 | 0.3 | 0.16 | 34.5 | no edge shown yet |
| pin_value | total | 28-27 | 50.9 | 50.0 | 0.9 | -1.74 | -3.2 | -0.02 | 36.4 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 53.0 | -19.6 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 121-188 | 39.2 | 47.2 | -8.1 | -53.61 | -17.4 | 0.1 | 42.7 | DROP: below break-even |
| consensus_gap | spread | 78-72 | 52.0 | 48.9 | 3.1 | -3.78 | -2.5 | 0.32 | 39.3 | no edge shown yet |
| consensus_gap | total | 87-80 | 52.1 | 50.1 | 2.0 | -1.85 | -1.1 | 0.95 | 56.9 | no edge shown yet |
| money_level+sharp_gap | moneyline | 52-28 | 65.0 | 62.7 | 2.3 | -7.14 | -8.9 | 0.12 | 53.8 | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+follow_move | moneyline | 16-23 | 41.0 | 55.1 | -14.1 | -13.51 | -34.6 | 0.08 | 51.3 | no edge shown yet |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 33.5 | -8.5 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| consensus_gap+rlm_quiet | moneyline | 1-5 | 16.7 | 27.9 | -11.3 | -3.68 | -61.3 | 1.07 | 83.3 | keep collecting (6/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.6 | -9.3 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 21-34 | 38.2 | 27.9 | 10.2 | +7.7 | 14.0 | 0.2 | 43.6 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 35-18 | 66.0 | 67.9 | -1.9 | -7.85 | -14.8 | -0.45 | 49.1 | beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 27.9 | -27.9 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 20-40 | 33.3 | 44.9 | -11.5 | -12.09 | -20.2 | 0.73 | 50.0 | DROP: below break-even |
| follow_move+money_level | moneyline | 67-20 | 77.0 | 68.5 | 8.5 | -2.97 | -3.4 | -0.22 | 42.5 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 34-17 | 66.7 | 54.8 | 11.9 | +3.28 | 6.4 | 0.07 | 51.0 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 33-25 | 56.9 | 67.5 | -10.6 | -11.02 | -19.0 | -0.06 | 44.8 | no edge shown yet |
| follow_move+sharp_gap | moneyline | 39-24 | 61.9 | 49.6 | 12.3 | +5.1 | 8.1 | 0.4 | 52.4 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 26-37 | 41.3 | 45.4 | -4.2 | -13.66 | -21.7 | 0.31 | 57.1 | DROP: below break-even |
| consensus_gap+money_moving | moneyline | 11-24 | 31.4 | 46.8 | -15.4 | -14.01 | -40.0 | 0.32 | 48.6 | INVERT candidate: wrong well beyond its base rate |
| follow_move+rlm_ratio | moneyline | 14-16 | 46.7 | 29.4 | 17.3 | +8.47 | 28.2 | 0.35 | 53.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 10-12 | 45.5 | 27.9 | 17.5 | +7.6 | 34.5 | -0.23 | 40.9 | keep collecting (22/30) |
| rlm_quiet+sharp_gap | moneyline | 10-15 | 40.0 | 27.9 | 12.1 | +4.6 | 18.4 | -0.36 | 40.0 | keep collecting (25/30) |
| rlm_ratio+sharp_gap | moneyline | 14-16 | 46.7 | 29.4 | 17.3 | +8.47 | 28.2 | 0.35 | 53.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 27.9 | -2.9 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 7-11 | 38.9 | 27.9 | 10.9 | +2.13 | 11.8 | 0.52 | 50.0 | keep collecting (18/30) |
| money_moving+rlm_ratio | moneyline | 5-6 | 45.5 | 27.9 | 17.5 | +2.98 | 27.1 | 0.07 | 45.5 | keep collecting (11/30) |
| money_delta+money_moving | moneyline | 2-6 | 25.0 | 27.9 | -2.9 | -1.66 | -20.8 | -0.59 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-5 | 28.6 | 27.9 | 0.6 | -0.66 | -9.4 | -0.67 | 57.1 | keep collecting (7/30) |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 42.6 | -42.6 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-1 | 66.7 | 57.4 | 9.3 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | moneyline | 2-1 | 66.7 | 57.4 | 9.3 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 27.9 | -27.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-2 | 33.3 | 42.6 | -9.3 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 27.9 | -27.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 27.9 | -27.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-2 | 33.3 | 42.6 | -9.3 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+sharp_gap | moneyline | 1-3 | 25.0 | 39.0 | -14.0 | -2.07 | -51.8 | -0.37 | 75.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 27.9 | -27.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | -1.55 | 50.0 | keep collecting (2/30) |
| pin_move+sharp_gap | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.13 | 56.5 | -0.1 | 50.0 | keep collecting (2/30) |
| money_level+rlm_ratio | moneyline | 4-4 | 50.0 | 33.5 | 16.5 | +0.87 | 10.8 | 1.94 | 87.5 | keep collecting (8/30) |
| money_level+pin_rlm | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.07 | -3.7 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+pin_rlm | moneyline | 1-0 | 100.0 | 27.9 | 72.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 1-0 | 100.0 | 27.9 | 72.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 27.9 | 38.7 | +3.34 | 111.3 | -1.53 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 1-1 | 50.0 | 27.9 | 22.1 | +1.7 | 85.0 | -4.2 | 0.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 27.9 | 72.1 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 27.9 | -27.9 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-1 | 50.0 | 27.9 | 22.1 | +0.64 | 32.0 | 3.0 | 100.0 | keep collecting (2/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 72.1 | -72.1 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 72.1 | -72.1 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 47.0 | -1.6 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 47.0 | 36.3 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 13-9 | 59.1 | 48.4 | 10.7 | +2.17 | 9.9 | 0.32 | 40.9 | keep collecting (22/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.4 | 10.6 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-3 | 50.0 | 52.0 | -2.0 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-7 | 58.8 | 48.8 | 10.1 | +2.09 | 12.3 | 0.88 | 41.2 | keep collecting (17/30) |
| money_level+money_moving | spread | 10-6 | 62.5 | 48.5 | 14.0 | +3.12 | 19.5 | 1.19 | 68.8 | keep collecting (16/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.7 | -5.9 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 4-2 | 66.7 | 49.0 | 17.7 | +1.41 | 23.5 | 0.5 | 50.0 | keep collecting (6/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 3-3 | 50.0 | 52.0 | -2.0 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 53.0 | -53.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 53.0 | -53.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-12 | 53.8 | 49.1 | 4.8 | +0.62 | 2.4 | 1.15 | 46.2 | keep collecting (26/30) |
| money_moving+sharp_gap | spread | 10-4 | 71.4 | 49.1 | 22.3 | +5.04 | 36.0 | 0.86 | 50.0 | keep collecting (14/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.0 | 17.7 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-11 | 45.0 | 47.9 | -2.9 | -3.2 | -16.0 | 0.85 | 45.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 47.0 | 15.5 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 11-10 | 52.4 | 48.4 | 3.9 | +0.04 | 0.2 | 0.9 | 47.6 | keep collecting (21/30) |
| follow_move+pin_value | spread | 13-8 | 61.9 | 48.4 | 13.5 | +3.36 | 16.0 | 0.19 | 28.6 | keep collecting (21/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 47.0 | 53.0 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 47.0 | 53.0 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 47.0 | 53.0 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-3 | 75.0 | 48.0 | 27.0 | +5.22 | 43.5 | 0.75 | 50.0 | keep collecting (12/30) |
| money_delta+rlm_quiet | spread | 1-0 | 100.0 | 47.0 | 53.0 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 2-0 | 100.0 | 47.0 | 53.0 | +1.74 | 87.1 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 2-2 | 50.0 | 53.0 | -3.0 | -0.07 | -1.7 | 1.25 | 25.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | spread | 2-1 | 66.7 | 51.0 | 15.7 | +0.86 | 28.7 | 1.0 | 33.3 | keep collecting (3/30) |
| pin_move+pin_value | spread | 1-5 | 16.7 | 48.0 | -31.3 | -4.09 | -68.2 | 0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 47.0 | -47.0 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-3 | 25.0 | 47.0 | -22.0 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 53.0 | -53.0 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 15-18 | 45.5 | 49.4 | -4.0 | -4.36 | -13.2 | 0.85 | 54.5 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 32-26 | 55.2 | 50.3 | 4.9 | +3.23 | 5.6 | -0.14 | 36.2 | no edge shown yet |
| money_level+sharp_gap | total | 46-37 | 55.4 | 50.2 | 5.2 | +4.86 | 5.9 | -0.08 | 36.1 | no edge shown yet |
| money_moving+sharp_gap | total | 39-25 | 60.9 | 49.8 | 11.1 | +10.53 | 16.5 | 0.23 | 37.5 | no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 50.8 | -50.8 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 10-6 | 62.5 | 49.8 | 12.7 | +3.05 | 19.1 | 0.44 | 37.5 | keep collecting (16/30) |
| money_moving+pin_value | total | 6-4 | 60.0 | 49.7 | 10.3 | +1.38 | 13.8 | 0.2 | 30.0 | keep collecting (10/30) |
| pin_value+sharp_gap | total | 12-7 | 63.2 | 49.9 | 13.3 | +3.83 | 20.2 | 0.16 | 36.8 | keep collecting (19/30) |
| follow_move+money_level | total | 27-24 | 52.9 | 50.3 | 2.6 | +0.49 | 1.0 | 0.25 | 43.1 | no edge shown yet |
| follow_move+pin_value | total | 9-11 | 45.0 | 50.0 | -5.0 | -2.94 | -14.7 | -0.45 | 25.0 | keep collecting (20/30) |
| follow_move+rlm_ratio | total | 17-9 | 65.4 | 49.3 | 16.0 | +6.62 | 25.5 | 0.77 | 61.5 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 37-23 | 61.7 | 49.9 | 11.8 | +10.69 | 17.8 | 0.52 | 48.3 | no edge shown yet |
| money_level+rlm_ratio | total | 6-4 | 60.0 | 49.4 | 10.6 | +1.54 | 15.4 | 1.1 | 70.0 | keep collecting (10/30) |
| pin_value+rlm_ratio | total | 3-1 | 75.0 | 49.6 | 25.4 | +1.73 | 43.2 | -0.25 | 50.0 | keep collecting (4/30) |
| rlm_ratio+sharp_gap | total | 17-9 | 65.4 | 49.3 | 16.0 | +6.62 | 25.5 | 0.77 | 61.5 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 21-20 | 51.2 | 49.9 | 1.4 | -0.8 | -2.0 | 0.56 | 48.8 | no edge shown yet |
| consensus_gap+money_level | total | 6-4 | 60.0 | 50.3 | 9.7 | +1.34 | 13.4 | 0.0 | 30.0 | keep collecting (10/30) |
| consensus_gap+money_moving | total | 5-1 | 83.3 | 50.3 | 33.1 | +3.43 | 57.2 | -0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+pin_value | total | 10-14 | 41.7 | 50.2 | -8.5 | -5.11 | -21.3 | 0.5 | 50.0 | keep collecting (24/30) |
| consensus_gap+sharp_gap | total | 7-7 | 50.0 | 49.8 | 0.2 | -0.67 | -4.8 | 0.14 | 35.7 | keep collecting (14/30) |
| money_moving+rlm_ratio | total | 10-5 | 66.7 | 49.4 | 17.2 | +4.22 | 28.1 | 0.67 | 60.0 | keep collecting (15/30) |
| consensus_gap+follow_move | total | 15-12 | 55.6 | 49.9 | 5.6 | +1.6 | 5.9 | 1.52 | 70.4 | keep collecting (27/30) |
| consensus_gap+money_delta | total | 3-0 | 100.0 | 50.3 | 49.7 | +2.69 | 89.6 | 0.33 | 33.3 | keep collecting (3/30) |
| follow_move+money_delta | total | 3-3 | 50.0 | 49.5 | 0.5 | -0.31 | -5.2 | 1.33 | 66.7 | keep collecting (6/30) |
| money_delta+money_moving | total | 8-3 | 72.7 | 49.5 | 23.2 | +4.17 | 37.9 | 1.36 | 45.5 | keep collecting (11/30) |
| money_delta+pin_value | total | 3-0 | 100.0 | 49.7 | 50.3 | +2.69 | 89.6 | 0.0 | 33.3 | keep collecting (3/30) |
| money_delta+sharp_gap | total | 7-2 | 77.8 | 49.6 | 28.2 | +4.26 | 47.4 | 1.67 | 55.6 | keep collecting (9/30) |
| money_moving+rlm_quiet | total | 7-5 | 58.3 | 49.4 | 9.0 | +1.36 | 11.4 | 0.42 | 41.7 | keep collecting (12/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 9-5 | 64.3 | 49.3 | 14.9 | +3.22 | 23.0 | 0.71 | 64.3 | keep collecting (14/30) |
| rlm_quiet+sharp_gap | total | 11-6 | 64.7 | 49.3 | 15.4 | +4.04 | 23.8 | 0.76 | 58.8 | keep collecting (17/30) |
| follow_move+pin_move | total | 3-2 | 60.0 | 49.5 | 10.5 | +0.77 | 15.4 | 0.8 | 60.0 | keep collecting (5/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 49.2 | -49.2 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 49.2 | -49.2 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 3-2 | 60.0 | 49.5 | 10.5 | +0.73 | 14.5 | 0.8 | 60.0 | keep collecting (5/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 49.2 | 0.8 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 4-1 | 80.0 | 49.2 | 30.8 | +2.68 | 53.6 | 0.4 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | total | 1-2 | 33.3 | 50.8 | -17.4 | -1.09 | -36.4 | 1.0 | 33.3 | keep collecting (3/30) |
| pin_move+pin_value | total | 2-4 | 33.3 | 50.5 | -17.2 | -2.18 | -36.4 | 0.5 | 33.3 | keep collecting (6/30) |
| pin_move+sharp_gap | total | 0-2 | 0.0 | 50.8 | -50.8 | -2.0 | -100.0 | 1.5 | 50.0 | keep collecting (2/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 49.2 | -49.2 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 1-2 | 33.3 | 49.2 | -15.9 | -1.09 | -36.4 | 1.67 | 100.0 | keep collecting (3/30) |
| consensus_gap+pin_move | total | 1-0 | 100.0 | 50.8 | 49.2 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 234-362 | 39.3 | 41.9 | -2.7 | -72.41 | -12.1 |  |  | DROP: below break-even |
| pin_move | both | 597-620 | 49.1 | 49.7 | -0.7 | -57.65 | -4.7 |  |  | DROP: below break-even |
| money_delta | both | 372-490 | 43.2 | 44.1 | -0.9 | -65.91 | -7.6 |  |  | DROP: below break-even |
| pin_rlm | both | 158-195 | 44.8 | 42.0 | 2.7 | +15.01 | 4.3 |  |  | DROP: below break-even |
| follow_move | both | 1019-972 | 51.2 | 51.3 | -0.1 | -145.55 | -7.3 |  |  | no edge shown yet |
| rlm_ratio | both | 231-288 | 44.5 | 43.7 | 0.8 | -27.98 | -5.4 |  |  | DROP: below break-even |
| money_level | both | 1312-966 | 57.6 | 55.4 | 2.1 | -65.36 | -2.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 1012-1175 | 46.3 | 47.5 | -1.2 | -162.39 | -7.4 |  |  | DROP: below break-even |
| money_moving | both | 1021-1170 | 46.6 | 47.9 | -1.3 | -161.63 | -7.4 |  |  | DROP: below break-even |
| pin_value | both | 444-433 | 50.6 | 48.2 | 2.4 | +24.88 | 2.8 |  |  | no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 51.0 | 15.7 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 413-500 | 45.2 | 48.4 | -3.1 | -73.51 | -8.1 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 152-148 | 50.7 | 51.4 | -0.7 | -16.67 | -5.6 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 176-268 | 39.6 | 45.6 | -6.0 | -30.77 | -6.9 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 102-96 | 51.5 | 50.8 | 0.8 | +10.28 | 5.2 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 25-45 | 35.7 | 38.4 | -2.6 | +7.43 | 10.6 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 165-165 | 50.0 | 46.2 | 3.8 | +17.4 | 5.3 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | both | 30-50 | 37.5 | 39.9 | -2.4 | -2.61 | -3.3 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 176-273 | 39.2 | 45.1 | -5.9 | -32.44 | -7.2 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 533-590 | 47.5 | 49.0 | -1.6 | -102.4 | -9.1 |  |  | DROP: below break-even |
| follow_move+pin_move | both | 425-461 | 48.0 | 49.9 | -1.9 | -72.8 | -8.2 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 124-144 | 46.3 | 43.6 | 2.7 | -5.94 | -2.2 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 152-145 | 51.2 | 49.1 | 2.1 | +0.19 | 0.1 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 231-288 | 44.5 | 43.7 | 0.8 | -27.98 | -5.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 539-591 | 47.7 | 48.8 | -1.1 | -94.36 | -8.4 |  |  | DROP: below break-even |
| money_moving+pin_move | both | 341-384 | 47.0 | 48.4 | -1.3 | -39.65 | -5.5 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 152-187 | 44.8 | 42.1 | 2.7 | +17.04 | 5.0 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 188-220 | 46.1 | 47.5 | -1.4 | -18.09 | -4.4 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 223-277 | 44.6 | 43.8 | 0.8 | -24.89 | -5.0 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 974-1127 | 46.4 | 47.6 | -1.2 | -146.33 | -7.0 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 146-163 | 47.2 | 43.8 | 3.5 | +12.88 | 4.2 |  |  | DROP: below break-even |
| pin_move+pin_value | both | 191-186 | 50.7 | 49.2 | 1.4 | -4.87 | -1.3 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 132-141 | 48.4 | 45.0 | 3.3 | +3.25 | 1.2 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 346-389 | 47.1 | 48.2 | -1.1 | -40.19 | -5.5 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 43-47 | 47.8 | 46.0 | 1.7 | +9.27 | 10.3 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 124-144 | 46.3 | 43.6 | 2.7 | -5.94 | -2.2 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 158-195 | 44.8 | 42.0 | 2.7 | +15.01 | 4.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 43-37 | 53.8 | 48.6 | 5.2 | +2.14 | 2.7 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 189-220 | 46.2 | 47.4 | -1.2 | -17.2 | -4.2 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 231-288 | 44.5 | 43.7 | 0.8 | -27.98 | -5.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 181-222 | 44.9 | 45.7 | -0.8 | -40.09 | -9.9 |  |  | DROP: below break-even |
| money_level+money_moving | both | 716-630 | 53.2 | 52.4 | 0.8 | -50.7 | -3.8 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 700-620 | 53.0 | 52.2 | 0.9 | -44.7 | -3.4 |  |  | no edge shown yet |
| follow_move+money_level | both | 645-470 | 57.8 | 56.3 | 1.5 | -55.65 | -5.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 108-92 | 54.0 | 48.0 | 6.0 | +11.87 | 5.9 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 260-192 | 57.5 | 58.3 | -0.8 | -16.28 | -3.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_move | both | 339-310 | 52.2 | 53.1 | -0.9 | -33.16 | -5.1 |  |  | no edge shown yet |
| money_level+pin_value | both | 213-187 | 53.2 | 49.9 | 3.3 | -1.56 | -0.4 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 25-59 | 29.8 | 36.9 | -7.2 | -14.04 | -16.7 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | both | 234-362 | 39.3 | 41.9 | -2.7 | -72.41 | -12.1 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 118-206 | 36.4 | 41.3 | -4.9 | -54.29 | -16.8 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 270-380 | 41.5 | 42.5 | -1.0 | -49.98 | -7.7 |  |  | DROP: below break-even |
| consensus_gap+money_delta | both | 49-113 | 30.2 | 37.9 | -7.6 | -23.86 | -14.7 |  |  | DROP: below break-even |
| money_delta+money_level | both | 132-118 | 52.8 | 47.0 | 5.8 | +19.93 | 8.0 |  |  | no edge shown yet |
| money_delta+pin_value | both | 80-78 | 50.6 | 47.2 | 3.4 | +1.87 | 1.2 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 267-374 | 41.7 | 42.5 | -0.8 | -47.15 | -7.4 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 94-170 | 35.6 | 39.9 | -4.3 | -41.34 | -15.7 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | both | 110-198 | 35.7 | 41.3 | -5.6 | -52.19 | -16.9 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 66-122 | 35.1 | 42.8 | -7.6 | -49.44 | -26.3 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | both | 115-162 | 41.5 | 44.0 | -2.5 | -28.92 | -10.4 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 50-89 | 36.0 | 40.5 | -4.5 | -24.08 | -17.3 |  |  | DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 51.0 | 15.7 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 134-161 | 45.4 | 46.1 | -0.7 | -16.59 | -5.6 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 70-48 | 59.3 | 46.6 | 12.7 | +21.0 | 17.8 |  |  | PROMOTE: beats break-even and its own base rate |
| money_delta+pin_rlm | both | 92-111 | 45.3 | 42.0 | 3.3 | +5.3 | 2.6 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | both | 131-148 | 47.0 | 44.3 | 2.7 | -11.91 | -4.3 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | both | 32-48 | 40.0 | 47.2 | -7.2 | -8.57 | -10.7 |  |  | DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 49.2 | 50.8 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 70-157 | 30.8 | 28.7 | 2.1 | -18.77 | -8.3 |  |  | DROP: below break-even |
| rlm_quiet | spread | 56-59 | 48.7 | 51.2 | -2.5 | -6.93 | -6.0 |  |  | no edge shown yet |
| rlm_quiet | total | 108-146 | 42.5 | 49.6 | -7.0 | -46.71 | -18.4 |  |  | DROP: below break-even |
| pin_move | moneyline | 132-131 | 50.2 | 48.4 | 1.8 | +7.44 | 2.8 |  |  | no edge shown yet |
| pin_move | spread | 231-244 | 48.6 | 50.3 | -1.7 | -33.72 | -7.1 |  |  | DROP: below break-even |
| pin_move | total | 234-245 | 48.9 | 49.8 | -1.0 | -31.36 | -6.5 |  |  | DROP: below break-even |
| money_delta | moneyline | 65-193 | 25.2 | 29.8 | -4.6 | -49.59 | -19.2 |  |  | DROP: below break-even |
| money_delta | spread | 131-133 | 49.6 | 51.0 | -1.4 | -13.61 | -5.2 |  |  | no edge shown yet |
| money_delta | total | 176-164 | 51.8 | 49.5 | 2.2 | -2.7 | -0.8 |  |  | no edge shown yet |
| pin_rlm | moneyline | 46-90 | 33.8 | 29.6 | 4.3 | +17.47 | 12.8 |  |  | DROP: below break-even |
| pin_rlm | spread | 26-23 | 53.1 | 51.3 | 1.8 | +0.7 | 1.4 |  |  | no edge shown yet |
| pin_rlm | total | 86-82 | 51.2 | 49.5 | 1.7 | -3.16 | -1.9 |  |  | no edge shown yet |
| follow_move | moneyline | 374-276 | 57.5 | 54.3 | 3.3 | -37.68 | -5.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 292-314 | 48.2 | 49.6 | -1.5 | -48.2 | -8.0 |  |  | DROP: below break-even |
| follow_move | total | 353-382 | 48.0 | 49.9 | -1.9 | -59.68 | -8.1 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 48-113 | 29.8 | 30.4 | -0.6 | -20.23 | -12.6 |  |  | DROP: below break-even |
| rlm_ratio | spread | 42-45 | 48.3 | 50.2 | -2.0 | -6.92 | -7.9 |  |  | no edge shown yet |
| rlm_ratio | total | 141-130 | 52.0 | 49.6 | 2.5 | -0.83 | -0.3 |  |  | no edge shown yet |
| money_level | moneyline | 512-202 | 71.7 | 68.0 | 3.7 | -24.89 | -3.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 365-373 | 49.5 | 49.1 | 0.4 | -43.97 | -6.0 |  |  | DROP: below break-even |
| money_level | total | 435-391 | 52.7 | 50.2 | 2.4 | +3.5 | 0.4 |  |  | no edge shown yet |
| sharp_gap | moneyline | 257-399 | 39.2 | 42.4 | -3.2 | -71.94 | -11.0 |  |  | DROP: below break-even |
| sharp_gap | spread | 367-363 | 50.3 | 49.5 | 0.8 | -31.69 | -4.3 |  |  | no edge shown yet |
| sharp_gap | total | 388-413 | 48.4 | 49.8 | -1.4 | -58.76 | -7.3 |  |  | DROP: below break-even |
| money_moving | moneyline | 271-381 | 41.6 | 43.6 | -2.1 | -53.27 | -8.2 |  |  | DROP: below break-even |
| money_moving | spread | 364-366 | 49.9 | 49.4 | 0.4 | -37.56 | -5.1 |  |  | no edge shown yet |
| money_moving | total | 386-423 | 47.7 | 49.9 | -2.2 | -70.8 | -8.8 |  |  | DROP: below break-even |
| pin_value | moneyline | 23-58 | 28.4 | 32.3 | -3.9 | +27.04 | 33.4 |  |  | DROP: below break-even |
| pin_value | spread | 199-181 | 52.4 | 49.5 | 2.8 | -7.81 | -2.1 |  |  | no edge shown yet |
| pin_value | total | 222-194 | 53.4 | 50.1 | 3.2 | +5.65 | 1.4 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 53.0 | 47.0 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 185-300 | 38.1 | 47.1 | -9.0 | -72.48 | -14.9 |  |  | DROP: below break-even |
| consensus_gap | spread | 102-85 | 54.5 | 49.0 | 5.6 | +2.06 | 1.1 |  |  | no edge shown yet |
| consensus_gap | total | 126-115 | 52.3 | 50.4 | 1.9 | -3.09 | -1.3 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 188-104 | 64.4 | 62.7 | 1.7 | -2.62 | -0.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 173-102 | 62.9 | 62.1 | 0.8 | -3.86 | -1.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 241-366 | 39.7 | 42.5 | -2.8 | -50.63 | -8.3 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 67-79 | 45.9 | 53.3 | -7.4 | -21.77 | -14.9 |  |  | DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 9-45 | 16.7 | 29.6 | -12.9 | -14.24 | -26.4 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 70-157 | 30.8 | 28.7 | 2.1 | -18.77 | -8.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 131-76 | 63.3 | 68.7 | -5.4 | -12.74 | -6.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 71-165 | 30.1 | 42.1 | -12.1 | -19.19 | -8.1 |  |  | !! CHECK: consensus_gap+money_moving close moneyline all sits -12.1 pts from its base (42.1%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+money_level | moneyline | 283-99 | 74.1 | 69.2 | 4.9 | -13.07 | -3.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+money_moving | moneyline | 132-147 | 47.3 | 47.4 | -0.1 | -23.94 | -8.6 |  |  | DROP: below break-even |
| money_delta+money_moving | moneyline | 61-174 | 26.0 | 29.4 | -3.5 | -34.41 | -14.6 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 59-173 | 25.4 | 29.5 | -4.0 | -35.6 | -15.3 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 70-172 | 28.9 | 41.2 | -12.3 | -23.76 | -9.8 |  |  | !! CHECK: consensus_gap+sharp_gap close moneyline all sits -12.3 pts from its base (41.2%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+sharp_gap | moneyline | 128-150 | 46.0 | 46.3 | -0.3 | -27.28 | -9.8 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | moneyline | 31-93 | 25.0 | 28.7 | -3.7 | -19.59 | -15.8 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 32-98 | 24.6 | 28.6 | -4.0 | -25.13 | -19.3 |  |  | DROP: below break-even |
| consensus_gap+pin_move | moneyline | 40-40 | 50.0 | 52.2 | -2.2 | +12.28 | 15.4 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 12-31 | 27.9 | 31.0 | -3.1 | +10.05 | 23.4 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 6-35 | 14.6 | 30.1 | -15.5 | -8.64 | -21.1 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 104-95 | 52.3 | 49.7 | 2.6 | +0.18 | 0.1 |  |  | no edge shown yet |
| follow_move+pin_rlm | moneyline | 31-53 | 36.9 | 30.0 | 6.9 | -0.36 | -0.4 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 48-113 | 29.8 | 30.4 | -0.6 | -20.23 | -12.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 57-73 | 43.8 | 41.9 | 2.0 | +13.1 | 10.1 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 45-85 | 34.6 | 29.6 | 5.0 | +21.07 | 16.2 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 47-106 | 30.7 | 30.5 | 0.2 | -14.63 | -9.6 |  |  | DROP: below break-even |
| pin_move+pin_rlm | moneyline | 34-58 | 37.0 | 29.4 | 7.6 | +15.35 | 16.7 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 32-52 | 38.1 | 29.5 | 8.6 | +4.33 | 5.2 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 27-41 | 39.7 | 30.5 | 9.2 | +7.12 | 10.5 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 57-77 | 42.5 | 41.1 | 1.4 | +8.93 | 6.7 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 18-45 | 28.6 | 29.3 | -0.8 | -9.5 | -15.1 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 31-53 | 36.9 | 30.0 | 6.9 | -0.36 | -0.4 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 46-90 | 33.8 | 29.6 | 4.3 | +17.47 | 12.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 29-93 | 23.8 | 28.7 | -4.9 | -23.97 | -19.7 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 48-113 | 29.8 | 30.4 | -0.6 | -20.23 | -12.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 14-84 | 14.3 | 29.7 | -15.5 | -25.27 | -25.8 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 16-47 | 25.4 | 31.4 | -6.0 | +5.85 | 9.3 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 20-41 | 32.8 | 30.8 | 2.0 | -0.92 | -1.5 |  |  | DROP: below break-even |
| money_delta+pin_rlm | moneyline | 26-52 | 33.3 | 29.6 | 3.7 | +3.87 | 5.0 |  |  | DROP: below break-even |
| money_delta+pin_value | moneyline | 3-18 | 14.3 | 27.9 | -13.7 | -6.68 | -31.8 |  |  | keep collecting (21/30) |
| money_moving+pin_value | moneyline | 11-34 | 24.4 | 30.9 | -6.4 | +11.94 | 26.5 |  |  | DROP: below break-even |
| pin_move+pin_value | moneyline | 7-11 | 38.9 | 35.3 | 3.6 | +6.35 | 35.3 |  |  | keep collecting (18/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 27.9 | 3.3 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 11-36 | 23.4 | 30.8 | -7.4 | +9.94 | 21.1 |  |  | DROP: below break-even |
| follow_move+money_delta | moneyline | 31-65 | 32.3 | 32.5 | -0.2 | -20.01 | -20.8 |  |  | DROP: below break-even |
| money_delta+money_level | moneyline | 20-24 | 45.5 | 34.0 | 11.5 | +12.18 | 27.7 |  |  | no edge shown yet |
| money_delta+rlm_ratio | moneyline | 26-55 | 32.1 | 31.2 | 0.9 | -14.5 | -17.9 |  |  | DROP: below break-even |
| money_level+pin_move | moneyline | 82-48 | 63.1 | 66.3 | -3.2 | -3.9 | -3.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 13-10 | 56.5 | 33.7 | 22.8 | +6.93 | 30.1 |  |  | keep collecting (23/30) |
| money_level+rlm_ratio | moneyline | 16-14 | 53.3 | 38.2 | 15.1 | +6.18 | 20.6 |  |  | no edge shown yet |
| money_delta+rlm_quiet | moneyline | 18-50 | 26.5 | 29.9 | -3.4 | -21.61 | -31.8 |  |  | DROP: below break-even |
| money_level+pin_value | moneyline | 5-3 | 62.5 | 66.5 | -4.0 | -0.32 | -4.0 |  |  | keep collecting (8/30) |
| follow_move+pin_value | moneyline | 3-9 | 25.0 | 35.3 | -10.3 | +3.8 | 31.7 |  |  | keep collecting (12/30) |
| pin_value+rlm_quiet | moneyline | 2-7 | 22.2 | 27.9 | -5.7 | +5.12 | 56.9 |  |  | keep collecting (9/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 27.9 | -2.9 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 37-29 | 56.1 | 48.4 | 7.7 | +2.57 | 3.9 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 51-47 | 52.0 | 48.7 | 3.3 | -3.5 | -3.6 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 30-30 | 50.0 | 49.2 | 0.8 | -4.4 | -7.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 74-53 | 58.3 | 48.9 | 9.3 | +10.03 | 7.9 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 5-4 | 55.6 | 50.3 | 5.2 | +0.18 | 2.0 |  |  | keep collecting (9/30) |
| consensus_gap+sharp_gap | spread | 50-47 | 51.5 | 48.9 | 2.6 | -4.4 | -4.5 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 169-175 | 49.1 | 49.2 | -0.1 | -22.11 | -6.4 |  |  | no edge shown yet |
| follow_move+pin_move | spread | 144-167 | 46.3 | 50.1 | -3.8 | -35.73 | -11.5 |  |  | DROP: below break-even |
| follow_move+pin_rlm | spread | 19-19 | 50.0 | 50.9 | -0.9 | -1.65 | -4.3 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 66-58 | 53.2 | 49.1 | 4.1 | -0.38 | -0.3 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 42-45 | 48.3 | 50.2 | -2.0 | -6.92 | -7.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 170-174 | 49.4 | 49.3 | 0.2 | -19.98 | -5.8 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 127-138 | 47.9 | 49.8 | -1.9 | -23.11 | -8.7 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 24-23 | 51.1 | 51.2 | -0.1 | -1.13 | -2.4 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 92-95 | 49.2 | 49.1 | 0.1 | -15.6 | -8.3 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 40-44 | 47.6 | 50.1 | -2.5 | -7.85 | -9.3 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 359-358 | 50.1 | 49.4 | 0.6 | -34.06 | -4.8 |  |  | no edge shown yet |
| pin_move+pin_rlm | spread | 26-23 | 53.1 | 51.3 | 1.8 | +0.7 | 1.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 91-90 | 50.3 | 49.8 | 0.5 | -10.02 | -5.5 |  |  | no edge shown yet |
| pin_move+rlm_ratio | spread | 23-26 | 46.9 | 50.8 | -3.9 | -5.1 | -10.4 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 130-138 | 48.5 | 49.8 | -1.3 | -20.38 | -7.6 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 8-10 | 44.4 | 51.0 | -6.5 | -2.97 | -16.5 |  |  | keep collecting (18/30) |
| pin_rlm+rlm_ratio | spread | 19-19 | 50.0 | 50.9 | -0.9 | -1.65 | -4.3 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 26-23 | 53.1 | 51.3 | 1.8 | +0.7 | 1.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 8-8 | 50.0 | 49.6 | 0.4 | -1.17 | -7.3 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | spread | 92-95 | 49.2 | 49.2 | 0.0 | -15.67 | -8.4 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 42-45 | 48.3 | 50.2 | -2.0 | -6.92 | -7.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 165-176 | 48.4 | 48.9 | -0.5 | -26.73 | -7.8 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 22-28 | 44.0 | 49.9 | -5.9 | -8.28 | -16.6 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 280-278 | 50.2 | 49.1 | 1.1 | -25.72 | -4.6 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 61-53 | 53.5 | 48.4 | 5.1 | -0.85 | -0.7 |  |  | no edge shown yet |
| money_level+money_moving | spread | 279-279 | 50.0 | 49.0 | 1.0 | -27.64 | -5.0 |  |  | no edge shown yet |
| money_level+pin_move | spread | 117-136 | 46.2 | 49.5 | -3.3 | -30.62 | -12.1 |  |  | DROP: below break-even |
| money_level+pin_value | spread | 100-98 | 50.5 | 48.7 | 1.8 | -11.86 | -6.0 |  |  | no edge shown yet |
| consensus_gap+money_delta | spread | 16-14 | 53.3 | 50.8 | 2.5 | -0.33 | -1.1 |  |  | no edge shown yet |
| follow_move+money_delta | spread | 42-50 | 45.7 | 50.5 | -4.8 | -11.97 | -13.0 |  |  | no edge shown yet |
| money_delta+money_level | spread | 43-41 | 51.2 | 50.0 | 1.2 | -2.26 | -2.7 |  |  | no edge shown yet |
| money_delta+money_moving | spread | 74-80 | 48.1 | 50.5 | -2.5 | -13.21 | -8.6 |  |  | no edge shown yet |
| money_delta+pin_value | spread | 34-29 | 54.0 | 50.7 | 3.3 | +0.63 | 1.0 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 73-78 | 48.3 | 50.5 | -2.1 | -12.19 | -8.1 |  |  | no edge shown yet |
| follow_move+rlm_quiet | spread | 56-59 | 48.7 | 51.2 | -2.5 | -6.93 | -6.0 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 14-5 | 73.7 | 51.1 | 22.6 | +7.78 | 40.9 |  |  | keep collecting (19/30) |
| rlm_quiet+sharp_gap | spread | 22-14 | 61.1 | 51.3 | 9.8 | +6.13 | 17.0 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 14-11 | 56.0 | 50.6 | 5.4 | +1.57 | 6.3 |  |  | keep collecting (25/30) |
| money_delta+pin_move | spread | 39-47 | 45.3 | 51.2 | -5.9 | -11.42 | -13.3 |  |  | no edge shown yet |
| money_delta+rlm_ratio | spread | 17-27 | 38.6 | 50.0 | -11.4 | -11.93 | -27.1 |  |  | DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 53.0 | 47.0 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_rlm | spread | 13-16 | 44.8 | 50.9 | -6.1 | -4.31 | -14.8 |  |  | keep collecting (29/30) |
| money_delta+rlm_quiet | spread | 17-19 | 47.2 | 51.7 | -4.4 | -3.27 | -9.1 |  |  | no edge shown yet |
| money_moving+rlm_quiet | spread | 21-14 | 60.0 | 51.3 | 8.7 | +5.18 | 14.8 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 32-33 | 49.2 | 51.7 | -2.5 | -3.2 | -4.9 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-2 | 75.0 | 52.2 | 22.8 | +3.56 | 44.5 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_quiet | spread | 4-3 | 57.1 | 51.3 | 5.9 | +0.48 | 6.9 |  |  | keep collecting (7/30) |
| pin_value+rlm_quiet | spread | 6-7 | 46.2 | 50.2 | -4.1 | -1.7 | -13.1 |  |  | keep collecting (13/30) |
| follow_move+money_delta | total | 108-107 | 50.2 | 49.6 | 0.7 | -8.11 | -3.8 |  |  | no edge shown yet |
| money_level+money_moving | total | 249-247 | 50.2 | 50.1 | 0.1 | -20.44 | -4.1 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 247-240 | 50.7 | 50.1 | 0.7 | -15.12 | -3.1 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 374-403 | 48.1 | 49.9 | -1.7 | -61.64 | -7.9 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 68-63 | 51.9 | 50.6 | 1.3 | -2.69 | -2.1 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 32-26 | 55.2 | 50.3 | 4.8 | +2.39 | 4.1 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 75-65 | 53.6 | 50.4 | 3.2 | +1.52 | 1.1 |  |  | no edge shown yet |
| follow_move+money_moving | total | 232-268 | 46.4 | 49.9 | -3.5 | -56.35 | -11.3 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 241-267 | 47.4 | 49.9 | -2.4 | -47.1 | -9.3 |  |  | DROP: below break-even |
| money_level+pin_move | total | 140-126 | 52.6 | 50.1 | 2.6 | +1.36 | 0.5 |  |  | no edge shown yet |
| money_level+pin_value | total | 108-86 | 55.7 | 50.4 | 5.3 | +10.62 | 5.5 |  |  | no edge shown yet |
| pin_move+pin_value | total | 93-85 | 52.2 | 50.0 | 2.2 | -1.2 | -0.7 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 108-146 | 42.5 | 49.6 | -7.0 | -46.71 | -18.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 157-173 | 47.6 | 49.8 | -2.2 | -29.65 | -9.0 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | total | 64-94 | 40.5 | 49.5 | -9.0 | -35.28 | -22.3 |  |  | DROP: below break-even |
| money_delta+money_moving | total | 135-126 | 51.7 | 49.5 | 2.2 | -2.36 | -0.9 |  |  | no edge shown yet |
| follow_move+money_level | total | 197-195 | 50.3 | 50.2 | 0.1 | -15.85 | -4.0 |  |  | no edge shown yet |
| follow_move+pin_value | total | 83-78 | 51.6 | 50.1 | 1.5 | -3.23 | -2.0 |  |  | no edge shown yet |
| money_moving+pin_value | total | 85-91 | 48.3 | 50.0 | -1.7 | -14.43 | -8.2 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 86-89 | 49.1 | 50.0 | -0.9 | -11.48 | -6.6 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 54-56 | 49.1 | 50.4 | -1.3 | -8.08 | -7.3 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 56-54 | 50.9 | 50.3 | 0.6 | -4.29 | -3.9 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 48-40 | 54.5 | 50.4 | 4.1 | +2.53 | 2.9 |  |  | no edge shown yet |
| consensus_gap+money_delta | total | 19-15 | 55.9 | 50.0 | 5.9 | +1.74 | 5.1 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | total | 12-11 | 52.2 | 49.8 | 2.3 | -0.28 | -1.2 |  |  | keep collecting (23/30) |
| money_delta+rlm_quiet | total | 31-53 | 36.9 | 49.4 | -12.4 | -24.55 | -29.2 |  |  | DROP: below break-even |
| money_delta+sharp_gap | total | 135-123 | 52.3 | 49.5 | 2.8 | +0.64 | 0.2 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 58-91 | 38.9 | 49.5 | -10.5 | -37.77 | -25.4 |  |  | DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 69-53 | 56.6 | 49.6 | 6.9 | +10.01 | 8.2 |  |  | no edge shown yet |
| money_delta+pin_move | total | 75-73 | 50.7 | 49.5 | 1.2 | -4.24 | -2.9 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 159-174 | 47.7 | 49.8 | -2.0 | -28.74 | -8.6 |  |  | DROP: below break-even |
| follow_move+pin_move | total | 177-199 | 47.1 | 49.9 | -2.8 | -37.24 | -9.9 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | total | 24-34 | 41.4 | 49.5 | -8.2 | -11.99 | -20.7 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | total | 10-11 | 47.6 | 50.0 | -2.4 | -2.13 | -10.1 |  |  | keep collecting (21/30) |
| consensus_gap+rlm_ratio | total | 19-11 | 63.3 | 50.2 | 13.2 | +5.85 | 19.5 |  |  | no edge shown yet |
| follow_move+pin_rlm | total | 74-72 | 50.7 | 49.5 | 1.2 | -3.93 | -2.7 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 141-130 | 52.0 | 49.6 | 2.5 | -0.83 | -0.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 43-27 | 61.4 | 49.5 | 12.0 | +12.5 | 17.9 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 70-50 | 58.3 | 49.7 | 8.7 | +13.97 | 11.6 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 83-79 | 51.2 | 49.5 | 1.8 | -2.9 | -1.8 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 136-127 | 51.7 | 49.6 | 2.2 | -2.42 | -0.9 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 86-82 | 51.2 | 49.5 | 1.7 | -3.16 | -1.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 82-74 | 52.6 | 49.5 | 3.1 | +1.23 | 0.8 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 30-26 | 53.6 | 49.6 | 4.0 | +1.17 | 2.1 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 74-72 | 50.7 | 49.5 | 1.2 | -3.93 | -2.7 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 86-82 | 51.2 | 49.5 | 1.7 | -3.16 | -1.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 34-26 | 56.7 | 49.7 | 7.0 | +4.78 | 8.0 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 141-130 | 52.0 | 49.6 | 2.5 | -0.83 | -0.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 53-43 | 55.2 | 49.4 | 5.8 | +5.73 | 6.0 |  |  | no edge shown yet |
| money_delta+rlm_ratio | total | 88-66 | 57.1 | 49.5 | 7.6 | +14.51 | 9.4 |  |  | no edge shown yet |
| money_delta+pin_value | total | 43-31 | 58.1 | 49.6 | 8.5 | +7.92 | 10.7 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 51-77 | 39.8 | 49.5 | -9.7 | -30.06 | -23.5 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | total | 26-42 | 38.2 | 49.4 | -11.2 | -18.14 | -26.7 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | total | 51-72 | 41.5 | 49.4 | -7.9 | -25.14 | -20.4 |  |  | DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 49.2 | 50.8 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| rlm_quiet | close | 1-3k bets | 158-238 | 39.9 | -1.9 | -8.8 |  |
| rlm_quiet | close | 3k+ bets | 50-79 | 38.8 | -3.8 | -16.6 |  |
| rlm_quiet | close | <1k bets | 26-45 | 36.6 | -4.7 | -23.0 |  |
| rlm_quiet | close | pin $1-2k | 63-117 | 35.0 | -8.5 | -21.3 |  |
| rlm_quiet | close | pin $2k+ | 71-89 | 44.4 | 5.9 | 1.8 |  |
| rlm_quiet | close | pin limit <$1k | 42-45 | 48.3 | -0.8 | -7.4 |  |
| pin_move | close | 1-3k bets | 384-387 | 49.8 | 0.2 | -2.7 |  |
| pin_move | close | 3k+ bets | 136-154 | 46.9 | -2.6 | -9.8 |  |
| pin_move | close | <1k bets | 77-79 | 49.4 | -1.2 | -5.4 |  |
| pin_move | close | pin $1-2k | 275-284 | 49.2 | -0.8 | -3.2 |  |
| pin_move | close | pin $2k+ | 217-232 | 48.3 | -1.1 | -8.0 |  |
| pin_move | close | pin limit <$1k | 105-104 | 50.2 | 0.7 | -1.8 |  |
| money_delta | close | 1-3k bets | 235-299 | 44.0 | -0.7 | -7.6 |  |
| money_delta | close | 3k+ bets | 89-119 | 42.8 | -0.6 | -3.0 |  |
| money_delta | close | <1k bets | 48-72 | 40.0 | -2.6 | -16.1 |  |
| money_delta | close | pin $1-2k | 132-129 | 50.6 | 4.5 | 6.0 |  |
| money_delta | close | pin $2k+ | 94-131 | 41.8 | 0.6 | -11.2 |  |
| money_delta | close | pin limit <$1k | 58-66 | 46.8 | -2.3 | -6.7 |  |
| pin_rlm | close | 1-3k bets | 102-119 | 46.2 | 4.0 | 11.0 |  |
| pin_rlm | close | 3k+ bets | 34-52 | 39.5 | -2.6 | -13.7 |  |
| pin_rlm | close | <1k bets | 22-24 | 47.8 | 6.5 | 5.5 |  |
| pin_rlm | close | pin $1-2k | 71-80 | 47.0 | 3.2 | 7.6 |  |
| pin_rlm | close | pin $2k+ | 43-77 | 35.8 | 0.4 | -6.4 |  |
| pin_rlm | close | pin limit <$1k | 44-38 | 53.7 | 5.2 | 13.8 |  |
| follow_move | close | 1-3k bets | 660-623 | 51.4 | 0.5 | -5.8 |  |
| follow_move | close | 3k+ bets | 216-210 | 50.7 | -1.0 | -7.7 |  |
| follow_move | close | <1k bets | 143-139 | 50.7 | -1.6 | -13.8 |  |
| follow_move | close | pin $1-2k | 311-352 | 46.9 | -3.7 | -11.8 |  |
| follow_move | close | pin $2k+ | 272-236 | 53.5 | 2.0 | -2.4 |  |
| follow_move | close | pin limit <$1k | 122-130 | 48.4 | -1.4 | -7.5 |  |
| rlm_ratio | close | 1-3k bets | 149-201 | 42.6 | -1.2 | -8.6 |  |
| rlm_ratio | close | 3k+ bets | 53-54 | 49.5 | 5.4 | 5.6 |  |
| rlm_ratio | close | <1k bets | 29-33 | 46.8 | 3.9 | -6.3 |  |
| rlm_ratio | close | pin $1-2k | 85-89 | 48.9 | 3.2 | 2.4 |  |
| rlm_ratio | close | pin $2k+ | 43-66 | 39.4 | 1.8 | -12.0 |  |
| rlm_ratio | close | pin limit <$1k | 49-45 | 52.1 | 3.3 | 0.6 |  |
| money_level | close | 1-3k bets | 840-612 | 57.9 | 2.3 | -2.5 |  |
| money_level | close | 3k+ bets | 289-224 | 56.3 | 1.2 | -2.6 |  |
| money_level | close | <1k bets | 183-129 | 58.7 | 3.0 | -4.5 |  |
| money_level | close | pin $1-2k | 387-329 | 54.1 | 0.2 | -3.7 |  |
| money_level | close | pin $2k+ | 341-266 | 56.2 | -1.1 | -7.1 |  |
| money_level | close | pin limit <$1k | 149-141 | 51.4 | 1.0 | -2.3 |  |
| sharp_gap | close | 1-3k bets | 631-757 | 45.5 | -1.9 | -9.4 |  |
| sharp_gap | close | 3k+ bets | 242-260 | 48.2 | 0.6 | 0.3 |  |
| sharp_gap | close | <1k bets | 139-157 | 47.0 | -0.9 | -11.1 |  |
| sharp_gap | close | pin $1-2k | 334-356 | 48.4 | -0.2 | -3.6 |  |
| sharp_gap | close | pin $2k+ | 268-317 | 45.8 | -0.6 | -5.0 |  |
| sharp_gap | close | pin limit <$1k | 129-149 | 46.4 | -2.9 | -7.8 |  |
| money_moving | close | 1-3k bets | 642-751 | 46.1 | -1.8 | -9.1 |  |
| money_moving | close | 3k+ bets | 241-262 | 47.9 | 0.1 | -1.0 |  |
| money_moving | close | <1k bets | 138-156 | 46.9 | -0.8 | -9.9 |  |
| money_moving | close | pin $1-2k | 333-358 | 48.2 | -0.8 | -4.1 |  |
| money_moving | close | pin $2k+ | 269-315 | 46.1 | -0.4 | -5.0 |  |
| money_moving | close | pin limit <$1k | 127-156 | 44.9 | -4.5 | -10.8 |  |
| pin_value | close | 1-3k bets | 286-280 | 50.5 | 2.3 | 3.8 |  |
| pin_value | close | 3k+ bets | 93-102 | 47.7 | -0.9 | -7.0 |  |
| pin_value | close | <1k bets | 65-51 | 56.0 | 8.5 | 14.5 |  |
| pin_value | close | pin $1-2k | 205-220 | 48.2 | -0.3 | -2.3 |  |
| pin_value | close | pin $2k+ | 124-139 | 47.1 | 0.7 | 0.5 |  |
| pin_value | close | pin limit <$1k | 115-74 | 60.8 | 10.8 | 17.7 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.0 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.0 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 264-313 | 45.8 | -3.3 | -9.3 |  |
| consensus_gap | close | 3k+ bets | 94-105 | 47.2 | -1.2 | 3.7 |  |
| consensus_gap | close | <1k bets | 55-81 | 40.4 | -5.1 | -19.2 |  |
| consensus_gap | close | pin $1-2k | 128-134 | 48.9 | -0.9 | 1.3 |  |
| consensus_gap | close | pin $2k+ | 120-120 | 50.0 | -0.9 | 0.6 |  |
| consensus_gap | close | pin limit <$1k | 57-46 | 55.3 | 5.0 | 7.7 |  |
| consensus_gap+follow_move | close | 1-3k bets | 102-97 | 51.3 | -0.3 | -3.4 |  |
| consensus_gap+money_level | close | 1-3k bets | 176-115 | 60.5 | 1.5 | 2.3 |  |
| consensus_gap+money_moving | close | 1-3k bets | 113-169 | 40.1 | -6.0 | -10.0 |  |
| consensus_gap+pin_move | close | 1-3k bets | 66-60 | 52.4 | 1.3 | 7.6 |  |
| consensus_gap+pin_value | close | 1-3k bets | 107-114 | 48.4 | 1.8 | 0.7 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 111-172 | 39.2 | -6.2 | -11.0 |  |
| follow_move+money_level | close | 1-3k bets | 423-305 | 58.1 | 2.2 | -4.0 |  |
| follow_move+money_moving | close | 1-3k bets | 355-393 | 47.5 | -1.5 | -9.0 |  |
| follow_move+pin_move | close | 1-3k bets | 274-295 | 48.2 | -1.5 | -7.7 |  |
| follow_move+pin_value | close | 1-3k bets | 94-91 | 50.8 | 2.1 | 1.5 |  |
| follow_move+sharp_gap | close | 1-3k bets | 358-395 | 47.5 | -1.1 | -8.1 |  |
| money_level+money_moving | close | 1-3k bets | 457-406 | 53.0 | 0.5 | -4.1 |  |
| money_level+pin_move | close | 1-3k bets | 224-201 | 52.7 | -0.1 | -3.9 |  |
| money_level+pin_value | close | 1-3k bets | 136-118 | 53.5 | 3.9 | 0.5 |  |
| money_level+sharp_gap | close | 1-3k bets | 440-399 | 52.4 | 0.4 | -4.0 |  |
| money_moving+pin_move | close | 1-3k bets | 225-243 | 48.1 | -0.6 | -3.1 |  |
| money_moving+pin_value | close | 1-3k bets | 120-144 | 45.5 | -2.2 | -7.0 |  |
| money_moving+sharp_gap | close | 1-3k bets | 606-721 | 45.7 | -1.9 | -8.7 |  |
| pin_move+pin_value | close | 1-3k bets | 123-115 | 51.7 | 2.3 | 0.9 |  |
| pin_move+sharp_gap | close | 1-3k bets | 230-247 | 48.2 | -0.2 | -2.5 |  |
| pin_value+sharp_gap | close | 1-3k bets | 121-146 | 45.3 | -2.2 | -7.4 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 158-238 | 39.9 | -1.9 | -8.8 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 77-144 | 34.8 | -6.2 | -17.9 |  |
| consensus_gap+money_delta | close | 1-3k bets | 29-68 | 29.9 | -8.4 | -21.7 |  |
| follow_move+money_delta | close | 1-3k bets | 116-143 | 44.8 | -1.5 | -11.2 |  |
| money_delta+money_level | close | 1-3k bets | 84-78 | 51.9 | 3.8 | 6.9 |  |
| money_delta+money_moving | close | 1-3k bets | 167-235 | 41.5 | -1.5 | -9.7 |  |
| money_delta+pin_value | close | 1-3k bets | 52-50 | 51.0 | 3.2 | 1.4 |  |
| money_delta+sharp_gap | close | 1-3k bets | 166-232 | 41.7 | -1.3 | -9.3 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 83-96 | 46.4 | -0.4 | -1.9 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 19-30 | 38.8 | -0.3 | 15.6 |  |
| money_level+pin_rlm | close | 1-3k bets | 45-32 | 58.4 | 10.5 | 12.9 |  |
| pin_move+pin_rlm | close | 1-3k bets | 94-98 | 49.0 | 5.1 | 9.3 |  |
| pin_rlm+pin_value | close | 1-3k bets | 31-28 | 52.5 | 6.0 | 23.8 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 102-119 | 46.2 | 4.0 | 11.0 |  |
| money_delta+pin_rlm | close | 1-3k bets | 57-66 | 46.3 | 3.7 | 8.6 |  |
| money_moving+pin_rlm | close | 1-3k bets | 97-112 | 46.4 | 4.0 | 12.6 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 23-35 | 39.7 | -0.5 | 3.7 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 149-201 | 42.6 | -1.2 | -8.6 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 81-101 | 44.5 | -0.2 | -10.5 |  |
| money_level+rlm_ratio | close | 1-3k bets | 69-65 | 51.5 | 2.7 | -0.5 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 143-192 | 42.7 | -1.3 | -8.1 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 81-86 | 48.5 | 3.6 | 1.4 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 29-25 | 53.7 | 5.7 | 2.9 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 149-201 | 42.6 | -1.2 | -8.6 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 16-39 | 29.1 | -7.0 | -12.4 |  |
| follow_move+pin_rlm | close | 1-3k bets | 75-93 | 44.6 | 1.2 | -6.0 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 70-138 | 33.7 | -7.5 | -19.7 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 74-103 | 41.8 | -2.1 | -9.8 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 31-60 | 34.1 | -5.5 | -19.8 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 75-93 | 44.6 | 1.2 | -6.0 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 61-122 | 33.3 | -6.3 | -18.1 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 43-79 | 35.2 | -8.0 | -26.6 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 19-28 | 40.4 | -5.6 | -1.0 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 50.8 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 36-31 | 53.7 | 3.1 | 2.2 |  |
| consensus_gap+money_moving | close | 3k+ bets | 38-59 | 39.2 | -6.2 | 9.4 |  |
| consensus_gap+pin_move | close | 3k+ bets | 28-23 | 54.9 | 5.0 | 8.5 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-8 | 27.3 | -13.2 | -13.2 |  |
| consensus_gap+pin_value | close | 3k+ bets | 40-36 | 52.6 | 6.0 | 7.1 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-8 | 33.3 | -8.0 | -4.3 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 39-59 | 39.8 | -5.5 | 12.2 |  |
| follow_move+money_moving | close | 3k+ bets | 114-124 | 47.9 | -1.2 | -6.4 |  |
| follow_move+pin_move | close | 3k+ bets | 103-114 | 47.5 | -2.4 | -8.4 |  |
| follow_move+pin_rlm | close | 3k+ bets | 32-37 | 46.4 | 2.5 | 2.1 |  |
| follow_move+pin_value | close | 3k+ bets | 37-40 | 48.1 | -1.8 | -9.6 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 53-54 | 49.5 | 5.4 | 5.6 |  |
| follow_move+sharp_gap | close | 3k+ bets | 116-123 | 48.5 | -0.2 | -4.5 |  |
| money_moving+pin_move | close | 3k+ bets | 77-97 | 44.3 | -3.8 | -12.4 |  |
| money_moving+pin_rlm | close | 3k+ bets | 33-51 | 39.3 | -2.6 | -14.0 |  |
| money_moving+pin_value | close | 3k+ bets | 47-59 | 44.3 | -3.5 | -10.2 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 51-52 | 49.5 | 5.5 | 5.9 |  |
| money_moving+sharp_gap | close | 3k+ bets | 234-252 | 48.1 | 0.5 | 0.1 |  |
| pin_move+pin_rlm | close | 3k+ bets | 32-46 | 41.0 | -2.5 | -10.3 |  |
| pin_move+pin_value | close | 3k+ bets | 39-50 | 43.8 | -5.4 | -17.4 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 34-39 | 46.6 | 1.3 | 0.9 |  |
| pin_move+sharp_gap | close | 3k+ bets | 77-97 | 44.3 | -3.5 | -11.8 |  |
| pin_rlm+pin_value | close | 3k+ bets | 6-16 | 27.3 | -19.2 | -48.0 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 32-37 | 46.4 | 2.5 | 2.1 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 34-52 | 39.5 | -2.6 | -13.7 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 9-11 | 45.0 | -5.1 | -14.6 |  |
| pin_value+sharp_gap | close | 3k+ bets | 47-58 | 44.8 | -3.1 | -9.3 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 53-54 | 49.5 | 5.4 | 5.6 |  |
| follow_move+money_delta | close | 3k+ bets | 42-52 | 44.7 | -0.6 | -7.8 |  |
| money_level+money_moving | close | 3k+ bets | 163-141 | 53.6 | 1.3 | -0.7 |  |
| money_level+sharp_gap | close | 3k+ bets | 162-138 | 54.0 | 1.9 | 0.7 |  |
| follow_move+money_level | close | 3k+ bets | 135-102 | 57.0 | 0.4 | -4.2 |  |
| money_level+rlm_ratio | close | 3k+ bets | 25-13 | 65.8 | 18.4 | 34.7 |  |
| consensus_gap+money_level | close | 3k+ bets | 55-49 | 52.9 | -4.4 | -10.0 |  |
| money_level+pin_move | close | 3k+ bets | 75-71 | 51.4 | -2.3 | -6.3 |  |
| money_level+pin_value | close | 3k+ bets | 54-51 | 51.4 | 1.0 | -4.5 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 8-15 | 34.8 | -3.9 | -13.6 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 50-79 | 38.8 | -3.8 | -16.6 |  |
| money_delta+money_moving | close | 3k+ bets | 69-91 | 43.1 | 0.7 | 1.9 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 21-33 | 38.9 | -2.0 | -11.4 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 26-43 | 37.7 | -4.4 | -16.7 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 24-42 | 36.4 | -5.6 | -18.7 |  |
| consensus_gap+money_delta | close | 3k+ bets | 13-23 | 36.1 | -3.4 | 20.4 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 12-29 | 29.3 | -13.7 | -36.6 |  |
| money_delta+sharp_gap | close | 3k+ bets | 67-88 | 43.2 | 1.0 | 2.5 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 29-45 | 39.2 | -4.4 | -15.4 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 11-23 | 32.4 | -9.3 | -23.1 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 8-16 | 33.3 | -15.5 | -36.3 |  |
| money_delta+money_level | close | 3k+ bets | 34-22 | 60.7 | 14.5 | 22.5 |  |
| money_level+pin_rlm | close | 3k+ bets | 16-9 | 64.0 | 18.9 | 37.0 |  |
| money_delta+pin_value | close | 3k+ bets | 19-20 | 48.7 | 2.2 | -8.1 |  |
| money_delta+pin_move | close | 3k+ bets | 37-46 | 44.6 | -0.9 | -9.1 |  |
| money_delta+pin_rlm | close | 3k+ bets | 22-29 | 43.1 | 1.1 | -8.2 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 31-27 | 53.4 | 9.2 | 13.0 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 47.0 | 87.7 |  |
| money_level+money_moving | close | <1k bets | 96-82 | 53.9 | 1.4 | -7.0 |  |
| money_level+sharp_gap | close | <1k bets | 98-82 | 54.4 | 1.7 | -6.6 |  |
| money_moving+sharp_gap | close | <1k bets | 134-153 | 46.7 | -1.0 | -10.7 |  |
| consensus_gap+money_level | close | <1k bets | 29-28 | 50.9 | -6.1 | -22.2 |  |
| consensus_gap+money_moving | close | <1k bets | 25-40 | 38.5 | -5.4 | -17.8 |  |
| consensus_gap+pin_move | close | <1k bets | 8-13 | 38.1 | -12.6 | -17.2 |  |
| consensus_gap+pin_value | close | <1k bets | 18-15 | 54.5 | 12.0 | 31.8 |  |
| consensus_gap+sharp_gap | close | <1k bets | 26-42 | 38.2 | -5.6 | -19.4 |  |
| money_level+pin_move | close | <1k bets | 40-38 | 51.3 | -2.7 | -9.3 |  |
| money_level+pin_value | close | <1k bets | 23-18 | 56.1 | 6.0 | 4.7 |  |
| money_moving+pin_move | close | <1k bets | 39-44 | 47.0 | -0.7 | -4.3 |  |
| money_moving+pin_value | close | <1k bets | 21-17 | 55.3 | 10.2 | 29.4 |  |
| pin_move+pin_value | close | <1k bets | 29-21 | 58.0 | 9.5 | 16.9 |  |
| pin_move+sharp_gap | close | <1k bets | 39-45 | 46.4 | -1.8 | -9.2 |  |
| pin_value+sharp_gap | close | <1k bets | 21-16 | 56.8 | 11.2 | 32.9 |  |
| follow_move+money_delta | close | <1k bets | 23-27 | 46.0 | 2.7 | -7.4 |  |
| follow_move+money_moving | close | <1k bets | 64-73 | 46.7 | -2.8 | -14.4 |  |
| follow_move+pin_move | close | <1k bets | 48-52 | 48.0 | -3.1 | -10.9 |  |
| follow_move+sharp_gap | close | <1k bets | 65-73 | 47.1 | -2.9 | -16.4 |  |
| money_delta+money_moving | close | <1k bets | 34-54 | 38.6 | -1.8 | -15.9 |  |
| money_delta+pin_move | close | <1k bets | 14-19 | 42.4 | -1.9 | -17.4 |  |
| money_delta+sharp_gap | close | <1k bets | 34-54 | 38.6 | -1.8 | -15.9 |  |
| follow_move+rlm_quiet | close | <1k bets | 26-45 | 36.6 | -4.7 | -23.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 29-33 | 46.8 | 3.9 | -6.3 |  |
| money_delta+rlm_quiet | close | <1k bets | 11-14 | 44.0 | 3.9 | -7.9 |  |
| money_delta+rlm_ratio | close | <1k bets | 19-20 | 48.7 | 6.7 | -0.8 |  |
| money_moving+rlm_quiet | close | <1k bets | 16-18 | 47.1 | 6.0 | 3.1 |  |
| money_moving+rlm_ratio | close | <1k bets | 29-33 | 46.8 | 3.9 | -6.3 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 12-15 | 44.4 | 4.6 | -7.6 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 15-19 | 44.1 | 2.4 | -9.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 29-33 | 46.8 | 3.9 | -6.3 |  |
| follow_move+money_level | close | <1k bets | 87-63 | 58.0 | 0.1 | -11.2 |  |
| consensus_gap+money_delta | close | <1k bets | 7-22 | 24.1 | -10.4 | -35.0 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -2.4 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 13-16 | 44.8 | 5.2 | -3.9 |  |
| money_moving+pin_rlm | close | <1k bets | 22-24 | 47.8 | 6.5 | 5.5 |  |
| pin_rlm+sharp_gap | close | <1k bets | 22-24 | 47.8 | 6.5 | 5.5 |  |
| money_delta+pin_value | close | <1k bets | 9-8 | 52.9 | 7.4 | 21.5 |  |
| consensus_gap+follow_move | close | <1k bets | 14-20 | 41.2 | -10.6 | -33.3 |  |
| follow_move+pin_rlm | close | <1k bets | 17-14 | 54.8 | 11.1 | 8.4 |  |
| follow_move+pin_value | close | <1k bets | 21-14 | 60.0 | 11.2 | 14.0 |  |
| pin_move+pin_rlm | close | <1k bets | 20-19 | 51.3 | 7.5 | 8.1 |  |
| pin_move+rlm_quiet | close | <1k bets | 12-14 | 46.2 | 0.7 | -1.0 |  |
| pin_move+rlm_ratio | close | <1k bets | 17-16 | 51.5 | 6.2 | 0.5 |  |
| pin_rlm+pin_value | close | <1k bets | 6-3 | 66.7 | 24.8 | 64.1 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 8-6 | 57.1 | 13.9 | 12.9 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 17-14 | 54.8 | 11.1 | 8.4 |  |
| pin_value+rlm_quiet | close | <1k bets | 5-4 | 55.6 | 6.5 | 6.5 |  |
| pin_value+rlm_ratio | close | <1k bets | 5-1 | 83.3 | 34.8 | 58.3 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -6.4 | -42.5 |  |
| money_delta+money_level | close | <1k bets | 14-18 | 43.8 | 0.6 | -12.1 |  |
| money_level+rlm_ratio | close | <1k bets | 14-14 | 50.0 | 4.8 | -2.1 |  |
| money_level+pin_rlm | close | <1k bets | 9-7 | 56.2 | 13.6 | 11.6 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-5 | 16.7 | -21.5 | -68.2 |  |
| consensus_gap+follow_move | close | pin $1-2k | 48-54 | 47.1 | -5.1 | -10.7 |  |
| consensus_gap+money_moving | close | pin $1-2k | 59-72 | 45.0 | -3.6 | -3.4 |  |
| consensus_gap+pin_move | close | pin $1-2k | 48-49 | 49.5 | -2.4 | 5.3 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-19 | 40.6 | -1.0 | 21.9 |  |
| consensus_gap+pin_value | close | pin $1-2k | 75-77 | 49.3 | 2.7 | 0.5 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-16 | 46.7 | 1.2 | 1.7 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 57-69 | 45.2 | -2.6 | -1.5 |  |
| follow_move+money_moving | close | pin $1-2k | 181-216 | 45.6 | -3.8 | -10.6 |  |
| follow_move+pin_move | close | pin $1-2k | 190-222 | 46.1 | -4.0 | -10.7 |  |
| follow_move+pin_rlm | close | pin $1-2k | 58-63 | 47.9 | 2.4 | 1.7 |  |
| follow_move+pin_value | close | pin $1-2k | 69-81 | 46.0 | -3.5 | -13.2 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 85-89 | 48.9 | 3.2 | 2.4 |  |
| follow_move+sharp_gap | close | pin $1-2k | 186-216 | 46.3 | -3.0 | -9.7 |  |
| money_moving+pin_move | close | pin $1-2k | 165-184 | 47.3 | -1.8 | -4.0 |  |
| money_moving+pin_rlm | close | pin $1-2k | 68-74 | 47.9 | 3.5 | 10.0 |  |
| money_moving+pin_value | close | pin $1-2k | 80-110 | 42.1 | -5.8 | -16.2 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 83-83 | 50.0 | 3.9 | 4.7 |  |
| money_moving+sharp_gap | close | pin $1-2k | 320-343 | 48.3 | -0.5 | -3.5 |  |
| pin_move+pin_rlm | close | pin $1-2k | 68-72 | 48.6 | 3.5 | 8.9 |  |
| pin_move+pin_value | close | pin $1-2k | 85-99 | 46.2 | -3.5 | -11.1 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 66-66 | 50.0 | 3.3 | 4.4 |  |
| pin_move+sharp_gap | close | pin $1-2k | 168-187 | 47.3 | -1.4 | -4.3 |  |
| pin_rlm+pin_value | close | pin $1-2k | 18-28 | 39.1 | -9.2 | -19.5 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 58-63 | 47.9 | 2.4 | 1.7 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 71-80 | 47.0 | 3.2 | 7.6 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 20-24 | 45.5 | -4.0 | -14.2 |  |
| pin_value+sharp_gap | close | pin $1-2k | 80-107 | 42.8 | -5.1 | -14.9 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 85-89 | 48.9 | 3.2 | 2.4 |  |
| follow_move+money_level | close | pin $1-2k | 205-192 | 51.6 | -2.3 | -9.0 |  |
| money_level+rlm_ratio | close | pin $1-2k | 47-35 | 57.3 | 9.4 | 11.7 |  |
| money_level+sharp_gap | close | pin $1-2k | 237-220 | 51.9 | 0.2 | -3.9 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 4-15 | 21.1 | -19.9 | -39.5 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 63-117 | 35.0 | -8.5 | -21.3 |  |
| money_level+money_moving | close | pin $1-2k | 239-224 | 51.6 | -0.2 | -4.7 |  |
| consensus_gap+money_level | close | pin $1-2k | 75-64 | 54.0 | -2.8 | -5.1 |  |
| money_level+pin_value | close | pin $1-2k | 91-89 | 50.6 | 0.6 | -5.4 |  |
| money_level+pin_move | close | pin $1-2k | 159-152 | 51.1 | -1.4 | -6.5 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 32-52 | 38.1 | -5.8 | -8.5 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 45-72 | 38.5 | -7.0 | -13.2 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 20-39 | 33.9 | -10.1 | -17.7 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 27-46 | 37.0 | -6.0 | -10.6 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 33-56 | 37.1 | -6.4 | -13.2 |  |
| money_level+pin_rlm | close | pin $1-2k | 33-23 | 58.9 | 12.6 | 15.7 |  |
| follow_move+money_delta | close | pin $1-2k | 67-69 | 49.3 | 2.8 | 0.5 |  |
| money_delta+money_moving | close | pin $1-2k | 89-97 | 47.8 | 3.4 | 4.4 |  |
| money_delta+pin_move | close | pin $1-2k | 67-70 | 48.9 | 1.6 | 2.7 |  |
| money_delta+pin_rlm | close | pin $1-2k | 43-45 | 48.9 | 5.2 | 10.7 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 50-45 | 52.6 | 6.9 | 9.5 |  |
| money_delta+sharp_gap | close | pin $1-2k | 89-95 | 48.4 | 3.9 | 5.5 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 47.0 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 46-37 | 55.4 | 7.6 | 7.9 |  |
| consensus_gap+money_delta | close | pin $1-2k | 18-26 | 40.9 | -0.7 | 2.5 |  |
| money_delta+pin_value | close | pin $1-2k | 43-45 | 48.9 | 0.7 | -3.4 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 20-37 | 35.1 | -9.2 | -20.8 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 12-30 | 28.6 | -20.5 | -45.1 |  |
| consensus_gap+follow_move | close | pin $2k+ | 39-31 | 55.7 | 2.7 | -4.9 |  |
| consensus_gap+money_delta | close | pin $2k+ | 9-26 | 25.7 | -8.9 | -49.8 |  |
| consensus_gap+money_level | close | pin $2k+ | 80-57 | 58.4 | -4.1 | -8.6 |  |
| consensus_gap+money_moving | close | pin $2k+ | 43-71 | 37.7 | -7.7 | -4.2 |  |
| consensus_gap+pin_move | close | pin $2k+ | 37-35 | 51.4 | 1.2 | -3.2 |  |
| consensus_gap+pin_value | close | pin $2k+ | 48-54 | 47.1 | 4.1 | 9.0 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 2-14 | 12.5 | -20.1 | -67.2 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 45-74 | 37.8 | -8.0 | -3.9 |  |
| follow_move+money_delta | close | pin $2k+ | 36-48 | 42.9 | 1.2 | -11.5 |  |
| follow_move+money_level | close | pin $2k+ | 161-105 | 60.5 | 1.1 | -3.0 |  |
| follow_move+money_moving | close | pin $2k+ | 125-131 | 48.8 | 1.0 | -6.4 |  |
| follow_move+pin_move | close | pin $2k+ | 165-164 | 50.2 | 0.3 | -5.4 |  |
| follow_move+pin_value | close | pin $2k+ | 39-37 | 51.3 | 3.8 | 9.8 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 43-66 | 39.4 | 1.8 | -12.0 |  |
| follow_move+sharp_gap | close | pin $2k+ | 126-132 | 48.8 | 1.1 | -6.1 |  |
| money_delta+money_level | close | pin $2k+ | 29-22 | 56.9 | 12.7 | 15.6 |  |
| money_delta+money_moving | close | pin $2k+ | 67-99 | 40.4 | 1.5 | -11.1 |  |
| money_delta+pin_move | close | pin $2k+ | 36-54 | 40.0 | -2.4 | -18.0 |  |
| money_delta+pin_value | close | pin $2k+ | 20-24 | 45.5 | 1.4 | -13.3 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 22-33 | 40.0 | 2.0 | -13.9 |  |
| money_delta+sharp_gap | close | pin $2k+ | 65-98 | 39.9 | 1.0 | -12.0 |  |
| money_level+money_moving | close | pin $2k+ | 180-167 | 51.9 | -0.9 | -5.6 |  |
| money_level+pin_move | close | pin $2k+ | 119-101 | 54.1 | -1.6 | -5.1 |  |
| money_level+pin_value | close | pin $2k+ | 64-61 | 51.2 | 1.6 | -5.3 |  |
| money_level+rlm_ratio | close | pin $2k+ | 16-14 | 53.3 | 7.7 | 11.3 |  |
| money_level+sharp_gap | close | pin $2k+ | 180-168 | 51.7 | -1.1 | -5.5 |  |
| money_moving+pin_move | close | pin $2k+ | 109-126 | 46.4 | -0.4 | -7.4 |  |
| money_moving+pin_value | close | pin $2k+ | 64-78 | 45.1 | -0.6 | 0.5 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 43-65 | 39.8 | 2.1 | -11.2 |  |
| money_moving+sharp_gap | close | pin $2k+ | 263-311 | 45.8 | -0.6 | -5.0 |  |
| pin_move+pin_value | close | pin $2k+ | 56-56 | 50.0 | 2.0 | -2.5 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 31-45 | 40.8 | 1.9 | -6.5 |  |
| pin_move+sharp_gap | close | pin $2k+ | 109-127 | 46.2 | -0.6 | -7.4 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 5-7 | 41.7 | -1.7 | -17.1 |  |
| pin_value+sharp_gap | close | pin $2k+ | 64-79 | 44.8 | -0.8 | -0.2 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 43-66 | 39.4 | 1.8 | -12.0 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 5-22 | 18.5 | -12.8 | -23.3 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 6-15 | 28.6 | -1.5 | -34.1 |  |
| follow_move+pin_rlm | close | pin $2k+ | 31-51 | 37.8 | 1.2 | -12.7 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 71-89 | 44.4 | 5.9 | 1.8 |  |
| money_moving+pin_rlm | close | pin $2k+ | 43-77 | 35.8 | 0.4 | -6.4 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 30-49 | 38.0 | 2.3 | -13.7 |  |
| pin_move+pin_rlm | close | pin $2k+ | 35-53 | 39.8 | 2.7 | -6.2 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 46-64 | 41.8 | 1.6 | -8.8 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 15-36 | 29.4 | -2.7 | -26.5 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 31-51 | 37.8 | 1.2 | -12.7 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 43-77 | 35.8 | 0.4 | -6.4 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 22-43 | 33.8 | 1.4 | -19.4 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 30-50 | 37.5 | 2.0 | -14.8 |  |
| money_delta+pin_rlm | close | pin $2k+ | 23-43 | 34.8 | -0.4 | -14.4 |  |
| money_level+pin_rlm | close | pin $2k+ | 16-10 | 61.5 | 18.2 | 30.4 |  |
| pin_rlm+pin_value | close | pin $2k+ | 6-13 | 31.6 | -5.2 | 13.6 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 19-28 | 40.4 | 2.0 | -16.6 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 6-10 | 37.5 | -1.6 | 35.0 |  |
| follow_move+money_delta | close | pin limit <$1k | 35-46 | 43.2 | -5.8 | -17.0 |  |
| money_level+money_moving | close | pin limit <$1k | 79-92 | 46.2 | -3.6 | -11.5 |  |
| money_level+sharp_gap | close | pin limit <$1k | 76-86 | 46.9 | -2.8 | -10.0 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 118-140 | 45.7 | -3.6 | -8.8 |  |
| consensus_gap+money_level | close | pin limit <$1k | 32-26 | 55.2 | 4.2 | 2.2 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 17-12 | 58.6 | 10.1 | 25.7 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 42-34 | 55.3 | 5.4 | 9.8 |  |
| follow_move+money_moving | close | pin limit <$1k | 73-93 | 44.0 | -5.3 | -15.5 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 78-92 | 45.9 | -3.4 | -11.9 |  |
| money_level+pin_move | close | pin limit <$1k | 61-57 | 51.7 | 1.8 | -1.4 |  |
| money_level+pin_value | close | pin limit <$1k | 58-37 | 61.1 | 10.8 | 15.5 |  |
| pin_move+pin_value | close | pin limit <$1k | 50-31 | 61.7 | 11.8 | 22.8 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 22-12 | 64.7 | 15.1 | 19.8 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 25-20 | 55.6 | 6.5 | 15.0 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 27-20 | 57.4 | 8.3 | 18.1 |  |
| follow_move+money_level | close | pin limit <$1k | 63-68 | 48.1 | -2.1 | -8.4 |  |
| follow_move+pin_move | close | pin limit <$1k | 70-75 | 48.3 | -1.1 | -7.5 |  |
| follow_move+pin_value | close | pin limit <$1k | 44-27 | 62.0 | 12.1 | 17.6 |  |
| money_moving+pin_move | close | pin limit <$1k | 67-74 | 47.5 | -1.7 | -6.0 |  |
| money_moving+pin_value | close | pin limit <$1k | 44-32 | 57.9 | 8.1 | 15.7 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 69-75 | 47.9 | -1.3 | -5.2 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 45-34 | 57.0 | 7.2 | 13.8 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 42-45 | 48.3 | -0.8 | -7.4 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 27-32 | 45.8 | -3.1 | -12.2 |  |
| money_delta+money_moving | close | pin limit <$1k | 50-55 | 47.6 | -1.4 | -4.5 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 9-7 | 56.2 | 9.2 | 34.3 |  |
| money_delta+money_level | close | pin limit <$1k | 26-23 | 53.1 | 3.6 | 1.7 |  |
| money_delta+pin_value | close | pin limit <$1k | 17-9 | 65.4 | 16.3 | 41.2 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 49-53 | 48.0 | -0.9 | -3.6 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 31-37 | 45.6 | -3.0 | -6.0 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 7-4 | 63.6 | 17.6 | 61.2 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 26-23 | 53.1 | 4.9 | 11.0 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 41-36 | 53.2 | 4.9 | 13.7 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 43-38 | 53.1 | 4.4 | 7.3 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-6 | 76.0 | 27.1 | 62.7 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 44-38 | 53.7 | 5.2 | 13.8 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 7-2 | 77.8 | 30.6 | 48.7 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 14-8 | 63.6 | 14.0 | 21.7 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 11-20 | 35.5 | -12.7 | -31.8 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 24-26 | 48.0 | -0.8 | -7.7 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 35-30 | 53.8 | 5.0 | 3.7 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 49-45 | 52.1 | 3.3 | 0.6 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 29-29 | 50.0 | 1.3 | -3.8 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 21-31 | 40.4 | -8.3 | -22.4 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 45-43 | 51.1 | 2.4 | -1.2 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 35-30 | 53.8 | 5.0 | 3.7 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 15-14 | 51.7 | 3.7 | -0.5 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 35-30 | 53.8 | 5.0 | 3.7 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 23-24 | 48.9 | 0.4 | -6.1 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 49-45 | 52.1 | 3.3 | 0.6 |  |
| money_level+pin_rlm | close | pin limit <$1k | 21-15 | 58.3 | 8.9 | 12.0 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 23-18 | 56.1 | 7.2 | 9.1 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 18-6 | 75.0 | 25.3 | 43.5 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 7-4 | 63.6 | 15.6 | 21.7 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 50.8 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.3 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -51.9 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 36-46 | 43.9 | 7.7 | 6.4 | 0.44 |
| rlm_quiet | early | pin $1-2k | 2-6 | 25.0 | -6.1 | 1.5 | -0.43 |
| rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -27.9 | -100.0 | 1.3 |
| rlm_quiet | early | pin limit <$1k | 5-8 | 38.5 | -6.2 | -21.5 | 0.25 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.8 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 9-14 | 39.1 | -9.6 | -28.1 | 0.31 |
| pin_move | early | pin $1-2k | 0-5 | 0.0 | -40.6 | -100.0 | 0.14 |
| pin_move | early | pin limit <$1k | 9-10 | 47.4 | -3.6 | -13.0 | 0.28 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.4 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 10-9 | 52.6 | 12.3 | 13.4 | 0.54 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -40.5 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 5-0 | 100.0 | 50.9 | 88.6 | 0.0 |
| pin_rlm | early | <1k bets | 1-3 | 25.0 | -14.0 | -51.8 | -0.37 |
| pin_rlm | early | pin $1-2k | 0-3 | 0.0 | -42.6 | -100.0 | -0.67 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.1 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.6 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -51.9 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 488-432 | 53.0 | 1.5 | -6.4 | 0.17 |
| follow_move | early | pin $1-2k | 36-25 | 59.0 | 8.3 | 8.9 | -0.26 |
| follow_move | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
| follow_move | early | pin limit <$1k | 53-47 | 53.0 | 3.0 | 0.0 | -0.16 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.1 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.0 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 28-24 | 53.8 | 14.8 | 17.9 | 0.67 |
| rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.3 | 29.7 | -1.02 |
| rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
| rlm_ratio | early | pin limit <$1k | 8-1 | 88.9 | 44.0 | 79.0 | 0.37 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 1.5 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 43.9 | 59.7 | 0.33 |
| money_level | early | <1k bets | 179-119 | 60.1 | 0.6 | -5.6 | -0.18 |
| money_level | early | pin $1-2k | 22-10 | 68.8 | 3.8 | 2.2 | -0.01 |
| money_level | early | pin $2k+ | 1-1 | 50.0 | -12.5 | -47.2 | -0.7 |
| money_level | early | pin limit <$1k | 26-28 | 48.1 | -4.7 | -10.9 | 0.3 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.3 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.6 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 141-134 | 51.3 | 3.1 | -0.5 | 0.42 |
| sharp_gap | early | pin $1-2k | 17-13 | 56.7 | 1.9 | 4.4 | -0.36 |
| sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
| sharp_gap | early | pin limit <$1k | 31-20 | 60.8 | 12.1 | 25.3 | 0.17 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.6 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 51.9 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 102-97 | 51.3 | 0.7 | -9.4 | 0.1 |
| money_moving | early | pin $1-2k | 8-10 | 44.4 | -13.8 | -39.0 | 0.28 |
| money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.5 | -8.4 | 0.65 |
| money_moving | early | pin limit <$1k | 25-10 | 71.4 | 22.4 | 49.9 | 0.39 |
| pin_value | early | 1-3k bets | 13-10 | 56.5 | 8.4 | 6.3 | -0.04 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.0 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 47-51 | 48.0 | -0.9 | -9.3 | 0.09 |
| pin_value | early | pin $1-2k | 16-26 | 38.1 | -8.7 | -28.4 | 0.08 |
| pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.0 | 83.3 | 0.0 |
| pin_value | early | pin limit <$1k | 44-35 | 55.7 | 6.0 | 5.4 | 0.07 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -50.8 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -27.0 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.1 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.5 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 231-274 | 45.7 | -2.8 | -10.9 | 0.39 |
| consensus_gap | early | pin $1-2k | 18-23 | 43.9 | -2.5 | -17.8 | 0.2 |
| consensus_gap | early | pin $2k+ | 1-1 | 50.0 | 12.5 | -8.4 | 0.65 |
| consensus_gap | early | pin limit <$1k | 22-35 | 38.6 | -11.6 | -21.2 | 0.31 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -53.0 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.4 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.4 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -1.9 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.7 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 5.6 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.3 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 7-4 | 63.6 | 14.4 | 19.4 | -0.09 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.3 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.9 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.8 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -0.7 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 6-5 | 54.5 | 8.4 | 1.3 | 0.27 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -1.0 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-7 | 50.0 | 3.0 | -6.4 | -0.29 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.3 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.6 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -20.2 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.7 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 3.4 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.6 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.1 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.5 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.1 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.3 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.1 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.5 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.1 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 53.0 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 11.6 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 18.2 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 16.4 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 16.4 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -27.9 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 53.0 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 53.0 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.0 | 83.3 | 1.0 |
| follow_move+rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -51.9 | -100.0 | -0.5 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.0 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.0 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 51.9 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.0 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.0 | 83.3 | 1.0 |
| rlm_quiet+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.0 | -100.0 | -1.0 |
| rlm_quiet+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.0 | -100.0 | -1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.0 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 39.4 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 50.8 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 33-38 | 46.5 | -6.0 | -17.6 | 0.79 |
| consensus_gap+money_level | early | <1k bets | 39-28 | 58.2 | -5.5 | -10.6 | 0.19 |
| consensus_gap+sharp_gap | early | <1k bets | 28-43 | 39.4 | -7.5 | -17.4 | 0.85 |
| follow_move+money_level | early | <1k bets | 90-43 | 67.7 | 6.5 | -0.5 | 0.09 |
| follow_move+sharp_gap | early | <1k bets | 74-44 | 62.7 | 12.7 | 11.7 | 0.62 |
| money_level+sharp_gap | early | <1k bets | 94-64 | 59.5 | 3.4 | -2.1 | 0.19 |
| follow_move+money_moving | early | <1k bets | 52-35 | 59.8 | 7.2 | 3.9 | 0.37 |
| money_level+money_moving | early | <1k bets | 62-45 | 57.9 | -0.1 | -7.1 | -0.18 |
| money_moving+sharp_gap | early | <1k bets | 61-59 | 50.8 | 2.7 | -6.2 | 0.34 |
| consensus_gap+money_moving | early | <1k bets | 14-22 | 38.9 | -9.8 | -38.1 | 0.35 |
| follow_move+pin_value | early | <1k bets | 16-14 | 53.3 | 3.8 | 0.1 | -0.18 |
| follow_move+rlm_quiet | early | <1k bets | 36-46 | 43.9 | 7.7 | 6.4 | 0.44 |
| money_moving+rlm_quiet | early | <1k bets | 14-14 | 50.0 | 13.0 | 19.0 | 0.48 |
| rlm_quiet+sharp_gap | early | <1k bets | 20-19 | 51.3 | 14.1 | 14.5 | 0.08 |
| follow_move+rlm_ratio | early | <1k bets | 28-24 | 53.8 | 14.8 | 17.9 | 0.67 |
| rlm_quiet+rlm_ratio | early | <1k bets | 18-15 | 54.5 | 17.6 | 23.8 | 0.12 |
| rlm_ratio+sharp_gap | early | <1k bets | 28-24 | 53.8 | 14.8 | 17.9 | 0.67 |
| pin_move+pin_value | early | <1k bets | 3-9 | 25.0 | -24.3 | -52.3 | 0.33 |
| follow_move+pin_move | early | <1k bets | 6-6 | 50.0 | -0.7 | -9.9 | 0.45 |
| consensus_gap+pin_value | early | <1k bets | 18-24 | 42.9 | -4.3 | -19.6 | 0.34 |
| pin_value+rlm_quiet | early | <1k bets | 0-3 | 0.0 | -43.4 | -100.0 | -0.6 |
| money_delta+money_moving | early | <1k bets | 9-9 | 50.0 | 10.1 | 9.1 | 0.57 |
| money_delta+sharp_gap | early | <1k bets | 8-7 | 53.3 | 13.9 | 18.2 | 0.69 |
| consensus_gap+pin_move | early | <1k bets | 1-5 | 16.7 | -28.8 | -68.2 | 0.22 |
| money_level+pin_move | early | <1k bets | 3-3 | 50.0 | -4.1 | -16.0 | 0.57 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -27.9 | -100.0 | -4.8 |
| consensus_gap+rlm_quiet | early | <1k bets | 3-5 | 37.5 | -1.1 | -22.7 | 1.01 |
| consensus_gap+rlm_ratio | early | <1k bets | 5-3 | 62.5 | 21.3 | 25.0 | 0.65 |
| follow_move+pin_rlm | early | <1k bets | 1-2 | 33.3 | -9.3 | -35.8 | -0.93 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -27.9 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | <1k bets | 0-1 | 0.0 | -27.9 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-2 | 33.3 | -9.3 | -35.8 | -0.93 |
| pin_rlm+sharp_gap | early | <1k bets | 1-3 | 25.0 | -14.0 | -51.8 | -0.37 |
| pin_value+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 24.5 | 27.3 | -0.93 |
| pin_value+sharp_gap | early | <1k bets | 6-6 | 50.0 | 0.2 | -4.5 | 0.41 |
| money_level+pin_value | early | <1k bets | 6-6 | 50.0 | -2.0 | -4.5 | 1.06 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -51.1 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -49.2 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 2-3 | 40.0 | -14.9 | -23.6 | 1.34 |
| money_level+rlm_ratio | early | <1k bets | 8-9 | 47.1 | 4.9 | -2.4 | 1.85 |
| money_moving+rlm_ratio | early | <1k bets | 14-10 | 58.3 | 17.0 | 29.7 | 0.62 |
| consensus_gap+money_delta | early | <1k bets | 2-0 | 100.0 | 50.0 | 90.9 | 0.5 |
| money_delta+money_level | early | <1k bets | 4-3 | 57.1 | 13.8 | 19.5 | 1.43 |
| pin_move+sharp_gap | early | <1k bets | 2-2 | 50.0 | -0.4 | -21.7 | 0.7 |
| money_level+pin_rlm | early | <1k bets | 1-1 | 50.0 | 0.0 | -3.7 | 1.0 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 72.1 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 72.1 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 4-4 | 50.0 | 8.8 | 27.0 | 0.42 |
| money_delta+rlm_quiet | early | <1k bets | 1-2 | 33.3 | -1.7 | 23.3 | -2.8 |
| money_delta+rlm_ratio | early | <1k bets | 3-2 | 60.0 | 19.3 | 65.0 | 1.12 |
| money_delta+pin_value | early | <1k bets | 2-0 | 100.0 | 50.8 | 90.9 | 0.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -27.9 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 6-4 | 60.0 | -4.5 | -4.6 | 0.25 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -30.4 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 7-11 | 38.9 | -3.8 | -28.1 | 0.15 |
| follow_move+rlm_quiet | early | pin $1-2k | 2-6 | 25.0 | -6.1 | 1.5 | -0.43 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.3 | 29.7 | -1.02 |
| follow_move+sharp_gap | early | pin $1-2k | 9-5 | 64.3 | 8.0 | 27.7 | -0.66 |
| money_level+money_moving | early | pin $1-2k | 8-6 | 57.1 | -8.2 | -21.6 | 0.19 |
| money_level+pin_value | early | pin $1-2k | 2-4 | 33.3 | -18.9 | -37.6 | 0.78 |
| money_moving+pin_value | early | pin $1-2k | 1-3 | 25.0 | -30.3 | -54.2 | 0.93 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -9.2 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -9.2 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -10.3 | 29.7 | -1.02 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -53.0 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -40.5 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -53.0 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -40.5 | -100.0 | 2.5 |
| money_level+sharp_gap | early | pin $1-2k | 14-6 | 70.0 | 5.6 | 7.8 | -0.25 |
| money_moving+sharp_gap | early | pin $1-2k | 4-7 | 36.4 | -21.4 | -50.4 | 0.23 |
| pin_value+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -25.0 | -52.3 | -0.52 |
| consensus_gap+follow_move | early | pin $1-2k | 5-6 | 45.5 | -2.5 | -18.8 | 0.45 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 0-3 | 0.0 | -27.9 | -100.0 | -0.97 |
| follow_move+pin_value | early | pin $1-2k | 6-7 | 46.2 | -1.4 | -14.7 | -0.25 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -27.9 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 11-5 | 68.8 | 4.1 | -0.1 | 0.03 |
| money_level+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -12.5 | -1.0 | 0.75 |
| follow_move+money_moving | early | pin $1-2k | 4-2 | 66.7 | 2.6 | -10.9 | -0.15 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -27.9 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -27.9 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 3-4 | 42.9 | -10.3 | -30.6 | -0.66 |
| follow_move+pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -27.9 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | pin $1-2k | 0-1 | 0.0 | -27.9 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-3 | 0.0 | -42.6 | -100.0 | -0.67 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -27.9 | -100.0 | -4.8 |
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -27.9 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -27.9 | -100.0 | 1.3 |
| pin_move+pin_value | early | pin $1-2k | 0-2 | 0.0 | -47.0 | -100.0 | 0.0 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -72.1 | -100.0 | 1.5 |
| follow_move+pin_move | early | pin $1-2k | 0-1 | 0.0 | -47.0 | -100.0 | 0.0 |
| consensus_gap+money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.5 | -8.4 | 0.65 |
| consensus_gap+pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.0 | 83.3 | 0.0 |
| follow_move+money_level | early | pin $2k+ | 0-1 | 0.0 | -53.0 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
| follow_move+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
| money_level+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -53.0 | -100.0 | 0.0 |
| money_level+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -53.0 | -100.0 | 0.0 |
| money_moving+pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.0 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
| consensus_gap+follow_move | early | pin $2k+ | 0-1 | 0.0 | -27.9 | -100.0 | 1.3 |
| consensus_gap+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -27.9 | -100.0 | 1.3 |
| consensus_gap+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -27.9 | -100.0 | 1.3 |
| consensus_gap+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -27.9 | -100.0 | 1.3 |
| follow_move+money_moving | early | pin $2k+ | 0-1 | 0.0 | -27.9 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -27.9 | -100.0 | 1.3 |
| money_moving+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -27.9 | -100.0 | 1.3 |
| money_moving+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -27.9 | -100.0 | 1.3 |
| money_moving+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -27.9 | -100.0 | 1.3 |
| rlm_quiet+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -27.9 | -100.0 | 1.3 |
| rlm_quiet+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -27.9 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin limit <$1k | 5-8 | 38.5 | -6.2 | -21.5 | 0.25 |
| money_level+money_moving | early | pin limit <$1k | 14-7 | 66.7 | 14.9 | 23.6 | 0.5 |
| money_level+sharp_gap | early | pin limit <$1k | 21-17 | 55.3 | 4.8 | 1.3 | 0.24 |
| money_moving+sharp_gap | early | pin limit <$1k | 20-6 | 76.9 | 28.8 | 65.2 | 0.31 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -50.8 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 11-7 | 61.1 | 11.3 | 16.0 | 0.5 |
| money_moving+pin_value | early | pin limit <$1k | 8-4 | 66.7 | 17.1 | 26.0 | 0.25 |
| pin_value+sharp_gap | early | pin limit <$1k | 13-7 | 65.0 | 15.3 | 23.3 | 0.2 |
| consensus_gap+follow_move | early | pin limit <$1k | 7-9 | 43.8 | -7.8 | -18.4 | 0.56 |
| consensus_gap+money_level | early | pin limit <$1k | 5-7 | 41.7 | -13.3 | -28.1 | 0.42 |
| consensus_gap+pin_value | early | pin limit <$1k | 17-18 | 48.6 | -0.6 | -8.6 | 0.45 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 7-4 | 63.6 | 18.3 | 56.6 | 0.91 |
| follow_move+money_level | early | pin limit <$1k | 12-11 | 52.2 | -1.0 | -3.2 | 0.01 |
| follow_move+pin_value | early | pin limit <$1k | 17-14 | 54.8 | 5.6 | 3.4 | -0.19 |
| follow_move+sharp_gap | early | pin limit <$1k | 14-8 | 63.6 | 15.2 | 21.5 | -0.02 |
| follow_move+rlm_ratio | early | pin limit <$1k | 8-1 | 88.9 | 44.0 | 79.0 | 0.37 |
| money_level+rlm_ratio | early | pin limit <$1k | 7-0 | 100.0 | 53.6 | 92.4 | 0.5 |
| pin_value+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.4 | 43.2 | -0.25 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 8-1 | 88.9 | 44.0 | 79.0 | 0.37 |
| consensus_gap+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 51.0 | 87.1 | 0.33 |
| consensus_gap+money_moving | early | pin limit <$1k | 8-3 | 72.7 | 25.3 | 74.0 | 0.58 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 1.9 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 51.0 | 87.1 | 0.33 |
| follow_move+money_moving | early | pin limit <$1k | 10-4 | 71.4 | 22.2 | 36.5 | 0.36 |
| money_delta+money_moving | early | pin limit <$1k | 4-0 | 100.0 | 50.9 | 88.0 | 0.0 |
| money_delta+pin_value | early | pin limit <$1k | 4-0 | 100.0 | 50.9 | 88.0 | 0.0 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 53.0 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 3-2 | 60.0 | 10.9 | 13.0 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 30.2 | 54.4 | -0.2 |
| money_delta+sharp_gap | early | pin limit <$1k | 3-0 | 100.0 | 50.3 | 89.6 | 0.0 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 10.6 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | 5.7 | 13.7 | -0.05 |
| pin_move+pin_value | early | pin limit <$1k | 3-7 | 30.0 | -19.7 | -42.7 | 0.4 |
| follow_move+pin_move | early | pin limit <$1k | 6-5 | 54.5 | 3.6 | -1.7 | 0.49 |
| consensus_gap+pin_move | early | pin limit <$1k | 1-3 | 25.0 | -29.2 | -52.3 | 0.4 |
| money_level+pin_move | early | pin limit <$1k | 3-3 | 50.0 | -4.1 | -16.0 | 0.57 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -49.2 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -49.2 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | -0.4 | -21.7 | 0.7 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.1 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.1 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.1 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 72.1 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 72.1 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 72.1 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 2-0 | 100.0 | 50.8 | 90.9 | 0.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 50.8 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 50.8 | 90.9 | 1.0 |
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
| rlm_quiet | close | 1-3k bets | 42-70 | 37.5 | -4.4 | -11.0 |  |
| rlm_quiet | close | 3k+ bets | 6-19 | 24.0 | -18.9 | -51.6 |  |
| rlm_quiet | close | <1k bets | 4-17 | 19.0 | -22.4 | -63.3 |  |
| rlm_quiet | close | pin $1-2k | 17-36 | 32.1 | -11.3 | -30.6 |  |
| rlm_quiet | close | pin $2k+ | 18-26 | 40.9 | -1.3 | 11.0 |  |
| rlm_quiet | close | pin limit <$1k | 6-9 | 40.0 | -4.5 | -22.5 |  |
| pin_move | close | 1-3k bets | 76-81 | 48.4 | -0.7 | -4.2 |  |
| pin_move | close | 3k+ bets | 15-28 | 34.9 | -14.8 | -35.5 |  |
| pin_move | close | <1k bets | 10-11 | 47.6 | -3.8 | -10.9 |  |
| pin_move | close | pin $1-2k | 43-55 | 43.9 | -5.2 | -11.8 |  |
| pin_move | close | pin $2k+ | 41-45 | 47.7 | -2.2 | -9.4 |  |
| pin_move | close | pin limit <$1k | 17-20 | 45.9 | -3.3 | -12.1 |  |
| money_delta | close | 1-3k bets | 36-48 | 42.9 | 0.4 | -14.6 |  |
| money_delta | close | 3k+ bets | 10-10 | 50.0 | 6.5 | -0.2 |  |
| money_delta | close | <1k bets | 10-10 | 50.0 | 7.1 | 17.9 |  |
| money_delta | close | pin $1-2k | 20-14 | 58.8 | 14.3 | 24.1 |  |
| money_delta | close | pin $2k+ | 12-19 | 38.7 | -1.1 | -20.3 |  |
| money_delta | close | pin limit <$1k | 8-12 | 40.0 | -4.5 | -22.7 |  |
| pin_rlm | close | 1-3k bets | 15-25 | 37.5 | -2.8 | -16.2 |  |
| pin_rlm | close | 3k+ bets | 2-6 | 25.0 | -15.3 | -46.4 |  |
| pin_rlm | close | <1k bets | 1-3 | 25.0 | -19.5 | -52.3 |  |
| pin_rlm | close | pin $1-2k | 10-14 | 41.7 | -1.0 | -10.1 |  |
| pin_rlm | close | pin $2k+ | 5-11 | 31.2 | -4.2 | -23.2 |  |
| pin_rlm | close | pin limit <$1k | 3-9 | 25.0 | -18.6 | -51.2 |  |
| follow_move | close | 1-3k bets | 114-145 | 44.0 | -5.1 | -11.2 |  |
| follow_move | close | 3k+ bets | 26-33 | 44.1 | -7.3 | -22.9 |  |
| follow_move | close | <1k bets | 23-31 | 42.6 | -6.3 | -25.0 |  |
| follow_move | close | pin $1-2k | 54-69 | 43.9 | -5.3 | -14.6 |  |
| follow_move | close | pin $2k+ | 52-53 | 49.5 | -0.8 | 2.5 |  |
| follow_move | close | pin limit <$1k | 16-26 | 38.1 | -11.1 | -26.8 |  |
| rlm_ratio | close | 1-3k bets | 23-46 | 33.3 | -7.3 | -28.9 |  |
| rlm_ratio | close | 3k+ bets | 5-10 | 33.3 | -8.2 | -32.6 |  |
| rlm_ratio | close | <1k bets | 3-7 | 30.0 | -11.2 | -42.9 |  |
| rlm_ratio | close | pin $1-2k | 15-16 | 48.4 | 6.4 | 1.9 |  |
| rlm_ratio | close | pin $2k+ | 5-13 | 27.8 | -7.4 | -34.4 |  |
| rlm_ratio | close | pin limit <$1k | 5-11 | 31.2 | -13.3 | -39.8 |  |
| money_level | close | 1-3k bets | 147-120 | 55.1 | -1.3 | -5.6 |  |
| money_level | close | 3k+ bets | 45-31 | 59.2 | 3.6 | 0.5 |  |
| money_level | close | <1k bets | 38-11 | 77.6 | 21.4 | 32.8 |  |
| money_level | close | pin $1-2k | 69-52 | 57.0 | 1.9 | 1.5 |  |
| money_level | close | pin $2k+ | 62-50 | 55.4 | -1.1 | -7.7 |  |
| money_level | close | pin limit <$1k | 24-21 | 53.3 | -0.2 | 1.4 |  |
| sharp_gap | close | 1-3k bets | 110-138 | 44.4 | -3.6 | -14.0 |  |
| sharp_gap | close | 3k+ bets | 32-42 | 43.2 | -5.3 | -17.3 |  |
| sharp_gap | close | <1k bets | 25-20 | 55.6 | 7.8 | 8.4 |  |
| sharp_gap | close | pin $1-2k | 59-52 | 53.2 | 4.5 | 4.3 |  |
| sharp_gap | close | pin $2k+ | 45-62 | 42.1 | -4.8 | -15.5 |  |
| sharp_gap | close | pin limit <$1k | 14-27 | 34.1 | -14.3 | -34.6 |  |
| money_moving | close | 1-3k bets | 117-134 | 46.6 | -2.2 | -10.9 |  |
| money_moving | close | 3k+ bets | 32-42 | 43.2 | -5.3 | -17.3 |  |
| money_moving | close | <1k bets | 26-19 | 57.8 | 9.0 | 10.5 |  |
| money_moving | close | pin $1-2k | 62-49 | 55.9 | 6.1 | 8.1 |  |
| money_moving | close | pin $2k+ | 45-62 | 42.1 | -4.8 | -15.5 |  |
| money_moving | close | pin limit <$1k | 16-29 | 35.6 | -13.3 | -32.0 |  |
| pin_value | close | 1-3k bets | 66-50 | 56.9 | 6.8 | 17.1 |  |
| pin_value | close | 3k+ bets | 12-16 | 42.9 | -6.9 | -18.6 |  |
| pin_value | close | <1k bets | 11-7 | 61.1 | 12.6 | 35.7 |  |
| pin_value | close | pin $1-2k | 42-36 | 53.8 | 4.1 | 8.9 |  |
| pin_value | close | pin $2k+ | 25-26 | 49.0 | 0.6 | 10.6 |  |
| pin_value | close | pin limit <$1k | 22-11 | 66.7 | 14.1 | 26.5 |  |
| consensus_gap | close | 1-3k bets | 55-39 | 58.5 | 5.2 | 6.0 |  |
| consensus_gap | close | 3k+ bets | 13-10 | 56.5 | 1.9 | -7.4 |  |
| consensus_gap | close | <1k bets | 15-3 | 83.3 | 29.1 | 56.5 |  |
| consensus_gap | close | pin $1-2k | 20-15 | 57.1 | 2.8 | 17.3 |  |
| consensus_gap | close | pin $2k+ | 37-15 | 71.2 | 15.3 | 26.2 |  |
| consensus_gap | close | pin limit <$1k | 7-3 | 70.0 | 21.1 | 33.4 |  |
| follow_move+pin_move | close | 1-3k bets | 51-71 | 41.8 | -7.0 | -16.6 |  |
| money_delta+money_moving | close | 1-3k bets | 28-34 | 45.2 | 3.6 | -9.1 |  |
| money_delta+sharp_gap | close | 1-3k bets | 28-33 | 45.9 | 4.4 | -7.6 |  |
| money_moving+sharp_gap | close | 1-3k bets | 107-130 | 45.1 | -3.1 | -12.1 |  |
| consensus_gap+money_level | close | 1-3k bets | 36-21 | 63.2 | 3.4 | 1.6 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 42-70 | 37.5 | -4.4 | -11.0 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 22-35 | 38.6 | -4.9 | -15.4 |  |
| consensus_gap+follow_move | close | 1-3k bets | 14-17 | 45.2 | -5.8 | -14.7 |  |
| follow_move+money_level | close | 1-3k bets | 53-53 | 50.0 | -6.2 | -11.1 |  |
| money_level+money_moving | close | 1-3k bets | 79-74 | 51.6 | -2.2 | -7.8 |  |
| money_level+sharp_gap | close | 1-3k bets | 73-73 | 50.0 | -3.3 | -9.2 |  |
| consensus_gap+money_moving | close | 1-3k bets | 16-20 | 44.4 | -6.4 | -11.3 |  |
| consensus_gap+pin_move | close | 1-3k bets | 13-7 | 65.0 | 14.3 | 34.5 |  |
| consensus_gap+pin_value | close | 1-3k bets | 21-14 | 60.0 | 9.6 | 12.3 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 16-20 | 44.4 | -5.8 | -11.6 |  |
| follow_move+money_moving | close | 1-3k bets | 53-76 | 41.1 | -7.0 | -20.1 |  |
| follow_move+pin_value | close | 1-3k bets | 20-15 | 57.1 | 6.2 | 35.6 |  |
| follow_move+sharp_gap | close | 1-3k bets | 55-80 | 40.7 | -6.9 | -20.8 |  |
| money_level+pin_move | close | 1-3k bets | 31-28 | 52.5 | -2.2 | -4.9 |  |
| money_level+pin_value | close | 1-3k bets | 25-19 | 56.8 | 4.5 | 6.5 |  |
| money_moving+pin_move | close | 1-3k bets | 33-36 | 47.8 | 0.3 | -3.5 |  |
| money_moving+pin_value | close | 1-3k bets | 20-23 | 46.5 | -3.9 | -12.5 |  |
| pin_move+pin_value | close | 1-3k bets | 24-18 | 57.1 | 5.9 | 7.4 |  |
| pin_move+sharp_gap | close | 1-3k bets | 31-40 | 43.7 | -3.0 | -11.5 |  |
| pin_value+sharp_gap | close | 1-3k bets | 19-22 | 46.3 | -3.6 | -12.9 |  |
| follow_move+money_delta | close | 1-3k bets | 21-34 | 38.2 | -5.1 | -25.2 |  |
| money_delta+pin_move | close | 1-3k bets | 13-16 | 44.8 | 3.0 | -11.8 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 12-26 | 31.6 | -9.8 | -37.6 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 23-46 | 33.3 | -7.3 | -28.9 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 15-35 | 30.0 | -9.4 | -32.4 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 23-42 | 35.4 | -5.5 | -24.5 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 11-34 | 24.4 | -14.1 | -43.2 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 15-40 | 27.3 | -11.8 | -38.5 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 23-46 | 33.3 | -7.3 | -28.9 |  |
| money_delta+money_level | close | 1-3k bets | 10-6 | 62.5 | 14.6 | 24.5 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 4-9 | 30.8 | -6.9 | -29.1 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 4-5 | 44.4 | 6.0 | 1.7 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 15-24 | 38.5 | -2.6 | -23.9 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 2-3 | 40.0 | -4.5 | 8.0 |  |
| money_level+pin_rlm | close | 1-3k bets | 6-3 | 66.7 | 21.0 | 31.1 |  |
| money_moving+pin_rlm | close | 1-3k bets | 15-21 | 41.7 | 0.9 | -6.9 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 15-25 | 37.5 | -2.8 | -16.2 |  |
| money_level+rlm_ratio | close | 1-3k bets | 10-9 | 52.6 | 6.9 | 2.3 |  |
| consensus_gap+money_delta | close | 1-3k bets | 4-4 | 50.0 | 9.5 | -4.2 |  |
| follow_move+pin_rlm | close | 1-3k bets | 13-21 | 38.2 | -1.3 | -13.8 |  |
| money_delta+pin_rlm | close | 1-3k bets | 8-12 | 40.0 | 1.6 | -20.0 |  |
| pin_move+pin_rlm | close | 1-3k bets | 15-20 | 42.9 | 2.5 | -4.2 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 14-18 | 43.8 | 3.1 | -2.7 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 7-18 | 28.0 | -10.7 | -30.0 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 13-21 | 38.2 | -1.3 | -13.8 |  |
| money_delta+pin_value | close | 1-3k bets | 8-5 | 61.5 | 15.3 | 16.7 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 5-8 | 38.5 | -7.1 | 48.3 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 4-3 | 57.1 | 7.7 | 7.1 |  |
| pin_rlm+pin_value | close | 1-3k bets | 2-4 | 33.3 | -15.1 | -37.0 |  |
| money_level+money_moving | close | 3k+ bets | 21-20 | 51.2 | -2.3 | -5.0 |  |
| money_level+sharp_gap | close | 3k+ bets | 21-20 | 51.2 | -2.3 | -5.0 |  |
| money_moving+sharp_gap | close | 3k+ bets | 32-42 | 43.2 | -5.3 | -17.3 |  |
| follow_move+money_delta | close | 3k+ bets | 4-5 | 44.4 | -1.5 | -14.2 |  |
| follow_move+money_level | close | 3k+ bets | 16-12 | 57.1 | -2.8 | -9.8 |  |
| follow_move+money_moving | close | 3k+ bets | 13-18 | 41.9 | -7.7 | -21.4 |  |
| follow_move+pin_move | close | 3k+ bets | 11-24 | 31.4 | -18.9 | -42.8 |  |
| follow_move+pin_rlm | close | 3k+ bets | 2-6 | 25.0 | -15.3 | -46.4 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 5-10 | 33.3 | -8.2 | -32.6 |  |
| follow_move+sharp_gap | close | 3k+ bets | 13-18 | 41.9 | -7.7 | -21.4 |  |
| money_delta+money_level | close | 3k+ bets | 3-0 | 100.0 | 52.3 | 93.5 |  |
| money_delta+money_moving | close | 3k+ bets | 9-8 | 52.9 | 10.3 | 5.8 |  |
| money_delta+pin_move | close | 3k+ bets | 2-4 | 33.3 | -13.4 | -35.7 |  |
| money_delta+pin_rlm | close | 3k+ bets | 1-2 | 33.3 | -7.5 | -34.9 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 3-3 | 50.0 | 7.4 | -3.1 |  |
| money_delta+sharp_gap | close | 3k+ bets | 9-8 | 52.9 | 10.3 | 5.8 |  |
| money_level+pin_move | close | 3k+ bets | 9-10 | 47.4 | -8.7 | -18.7 |  |
| money_level+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 55.5 | 95.2 |  |
| money_level+rlm_ratio | close | 3k+ bets | 2-1 | 66.7 | 14.8 | 28.7 |  |
| money_moving+pin_move | close | 3k+ bets | 6-14 | 30.0 | -19.6 | -44.7 |  |
| money_moving+pin_rlm | close | 3k+ bets | 2-6 | 25.0 | -15.3 | -46.4 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 5-10 | 33.3 | -8.2 | -32.6 |  |
| pin_move+pin_rlm | close | 3k+ bets | 1-6 | 14.3 | -27.0 | -72.1 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 1-7 | 12.5 | -30.6 | -75.6 |  |
| pin_move+sharp_gap | close | 3k+ bets | 6-14 | 30.0 | -19.6 | -44.7 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 2-6 | 25.0 | -15.3 | -46.4 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 2-6 | 25.0 | -15.3 | -46.4 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 5-10 | 33.3 | -8.2 | -32.6 |  |
| consensus_gap+money_level | close | 3k+ bets | 11-5 | 68.8 | 7.7 | 8.2 |  |
| consensus_gap+money_moving | close | 3k+ bets | 5-7 | 41.7 | -12.1 | -26.6 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 5-7 | 41.7 | -12.1 | -26.6 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 6-19 | 24.0 | -18.9 | -51.6 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 3-15 | 16.7 | -26.8 | -65.1 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 2-5 | 28.6 | -16.3 | -44.8 |  |
| money_level+pin_value | close | 3k+ bets | 9-8 | 52.9 | 2.1 | -0.6 |  |
| money_moving+pin_value | close | 3k+ bets | 7-10 | 41.2 | -8.6 | -22.5 |  |
| pin_value+sharp_gap | close | 3k+ bets | 7-10 | 41.2 | -8.6 | -22.5 |  |
| consensus_gap+follow_move | close | 3k+ bets | 6-4 | 60.0 | 4.3 | -4.5 |  |
| consensus_gap+pin_value | close | 3k+ bets | 5-3 | 62.5 | 13.8 | 19.8 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 3-11 | 21.4 | -20.8 | -58.5 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 3-11 | 21.4 | -20.8 | -58.5 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 0-6 | 0.0 | -40.8 | -100.0 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 2-9 | 18.2 | -21.2 | -64.5 |  |
| pin_move+pin_value | close | 3k+ bets | 6-10 | 37.5 | -13.4 | -28.8 |  |
| follow_move+pin_value | close | 3k+ bets | 4-7 | 36.4 | -16.7 | -30.9 |  |
| consensus_gap+money_delta | close | 3k+ bets | 1-0 | 100.0 | 43.2 | 90.9 |  |
| consensus_gap+pin_move | close | 3k+ bets | 6-4 | 60.0 | 10.0 | 8.6 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 1-3 | 25.0 | -19.7 | -52.3 |  |
| money_delta+pin_value | close | 3k+ bets | 1-1 | 50.0 | -6.8 | -4.5 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 1-4 | 20.0 | -29.6 | -61.8 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 0-2 | 0.0 | -44.4 | -100.0 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 0-2 | 0.0 | -44.4 | -100.0 |  |
| pin_rlm+pin_value | close | 3k+ bets | 0-1 | 0.0 | -44.5 | -100.0 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 0-1 | 0.0 | -44.5 | -100.0 |  |
| consensus_gap+money_level | close | <1k bets | 11-1 | 91.7 | 32.6 | 42.3 |  |
| consensus_gap+money_moving | close | <1k bets | 8-0 | 100.0 | 44.6 | 103.6 |  |
| consensus_gap+pin_value | close | <1k bets | 4-1 | 80.0 | 36.0 | 123.1 |  |
| consensus_gap+sharp_gap | close | <1k bets | 9-1 | 90.0 | 35.7 | 77.0 |  |
| follow_move+pin_move | close | <1k bets | 6-10 | 37.5 | -13.3 | -30.3 |  |
| follow_move+rlm_quiet | close | <1k bets | 4-17 | 19.0 | -22.4 | -63.3 |  |
| money_level+money_moving | close | <1k bets | 20-5 | 80.0 | 25.4 | 38.3 |  |
| money_level+pin_value | close | <1k bets | 5-1 | 83.3 | 34.0 | 56.7 |  |
| money_level+sharp_gap | close | <1k bets | 19-5 | 79.2 | 25.1 | 40.2 |  |
| money_moving+pin_value | close | <1k bets | 4-1 | 80.0 | 38.2 | 124.8 |  |
| money_moving+sharp_gap | close | <1k bets | 24-18 | 57.1 | 9.1 | 12.8 |  |
| pin_move+rlm_quiet | close | <1k bets | 2-4 | 33.3 | -13.4 | -36.4 |  |
| pin_value+sharp_gap | close | <1k bets | 4-1 | 80.0 | 38.2 | 124.8 |  |
| follow_move+money_moving | close | <1k bets | 10-10 | 50.0 | 1.1 | -17.8 |  |
| follow_move+sharp_gap | close | <1k bets | 9-10 | 47.4 | -0.6 | -18.3 |  |
| money_level+pin_move | close | <1k bets | 6-3 | 66.7 | 11.3 | 22.8 |  |
| money_moving+rlm_quiet | close | <1k bets | 2-6 | 25.0 | -15.3 | -52.3 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 2-6 | 25.0 | -15.3 | -52.3 |  |
| follow_move+money_delta | close | <1k bets | 5-7 | 41.7 | -2.9 | -20.5 |  |
| follow_move+pin_rlm | close | <1k bets | 1-3 | 25.0 | -19.5 | -52.3 |  |
| follow_move+pin_value | close | <1k bets | 3-2 | 60.0 | 11.4 | 15.4 |  |
| follow_move+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -11.2 | -42.9 |  |
| money_delta+money_moving | close | <1k bets | 7-8 | 46.7 | 5.9 | 18.9 |  |
| money_delta+pin_move | close | <1k bets | 1-2 | 33.3 | -11.2 | -36.4 |  |
| money_delta+pin_rlm | close | <1k bets | 1-2 | 33.3 | -11.2 | -36.4 |  |
| money_delta+pin_value | close | <1k bets | 3-0 | 100.0 | 59.2 | 212.0 |  |
| money_delta+rlm_quiet | close | <1k bets | 3-4 | 42.9 | 1.4 | -17.2 |  |
| money_delta+rlm_ratio | close | <1k bets | 3-5 | 37.5 | -4.2 | -28.6 |  |
| money_delta+sharp_gap | close | <1k bets | 7-8 | 46.7 | 5.9 | 18.9 |  |
| money_moving+pin_move | close | <1k bets | 3-3 | 50.0 | 3.9 | -5.2 |  |
| money_moving+pin_rlm | close | <1k bets | 1-3 | 25.0 | -19.5 | -52.3 |  |
| money_moving+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -11.2 | -42.9 |  |
| pin_move+pin_rlm | close | <1k bets | 1-3 | 25.0 | -19.5 | -52.3 |  |
| pin_move+pin_value | close | <1k bets | 4-1 | 80.0 | 28.6 | 52.8 |  |
| pin_move+rlm_ratio | close | <1k bets | 1-3 | 25.0 | -19.5 | -52.3 |  |
| pin_move+sharp_gap | close | <1k bets | 3-3 | 50.0 | 3.9 | -5.2 |  |
| pin_rlm+pin_value | close | <1k bets | 1-0 | 100.0 | 55.5 | 90.9 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 1-1 | 50.0 | 5.5 | -4.5 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 1-3 | 25.0 | -19.5 | -52.3 |  |
| pin_rlm+sharp_gap | close | <1k bets | 1-3 | 25.0 | -19.5 | -52.3 |  |
| pin_value+rlm_quiet | close | <1k bets | 2-0 | 100.0 | 55.5 | 90.9 |  |
| pin_value+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 55.5 | 90.9 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 2-5 | 28.6 | -11.2 | -45.5 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 3-7 | 30.0 | -11.2 | -42.9 |  |
| consensus_gap+follow_move | close | <1k bets | 5-0 | 100.0 | 42.2 | 71.3 |  |
| consensus_gap+pin_move | close | <1k bets | 2-0 | 100.0 | 44.4 | 70.5 |  |
| follow_move+money_level | close | <1k bets | 12-4 | 75.0 | 16.6 | 21.7 |  |
| money_delta+money_level | close | <1k bets | 2-1 | 66.7 | 25.9 | 53.8 |  |
| money_level+pin_rlm | close | <1k bets | 0-1 | 0.0 | -44.5 | -100.0 |  |
| money_level+rlm_ratio | close | <1k bets | 1-1 | 50.0 | 5.5 | -5.3 |  |
| consensus_gap+money_delta | close | <1k bets | 3-0 | 100.0 | 51.8 | 208.0 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 55.5 | 89.3 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-0 | 100.0 | 55.5 | 90.9 |  |
| money_delta+money_moving | close | pin $1-2k | 12-5 | 70.6 | 28.7 | 57.8 |  |
| money_delta+sharp_gap | close | pin $1-2k | 12-5 | 70.6 | 28.7 | 57.8 |  |
| money_moving+sharp_gap | close | pin $1-2k | 57-47 | 54.8 | 5.7 | 8.1 |  |
| consensus_gap+follow_move | close | pin $1-2k | 7-8 | 46.7 | -7.5 | -16.8 |  |
| consensus_gap+money_level | close | pin $1-2k | 12-8 | 60.0 | 1.2 | 2.3 |  |
| consensus_gap+money_moving | close | pin $1-2k | 6-8 | 42.9 | -9.5 | -3.4 |  |
| consensus_gap+pin_move | close | pin $1-2k | 6-6 | 50.0 | -1.2 | 9.9 |  |
| consensus_gap+pin_value | close | pin $1-2k | 10-7 | 58.8 | 7.1 | 31.9 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 6-7 | 46.2 | -7.7 | 6.1 |  |
| follow_move+money_level | close | pin $1-2k | 27-23 | 54.0 | -0.4 | -2.0 |  |
| follow_move+money_moving | close | pin $1-2k | 29-29 | 50.0 | 1.5 | -2.1 |  |
| follow_move+pin_move | close | pin $1-2k | 26-50 | 34.2 | -14.4 | -30.3 |  |
| follow_move+pin_value | close | pin $1-2k | 13-14 | 48.1 | -2.2 | -8.7 |  |
| follow_move+sharp_gap | close | pin $1-2k | 31-32 | 49.2 | 1.1 | -4.5 |  |
| money_level+money_moving | close | pin $1-2k | 43-28 | 60.6 | 7.0 | 8.8 |  |
| money_level+pin_move | close | pin $1-2k | 17-19 | 47.2 | -6.4 | -12.6 |  |
| money_level+pin_value | close | pin $1-2k | 17-12 | 58.6 | 6.8 | 9.7 |  |
| money_level+sharp_gap | close | pin $1-2k | 40-28 | 58.8 | 6.0 | 7.5 |  |
| money_moving+pin_move | close | pin $1-2k | 21-21 | 50.0 | 1.1 | 0.0 |  |
| money_moving+pin_value | close | pin $1-2k | 15-13 | 53.6 | 3.7 | 13.6 |  |
| pin_move+pin_value | close | pin $1-2k | 15-12 | 55.6 | 3.8 | 4.5 |  |
| pin_move+sharp_gap | close | pin $1-2k | 21-25 | 45.7 | -2.1 | -8.7 |  |
| pin_value+sharp_gap | close | pin $1-2k | 15-13 | 53.6 | 4.1 | 13.6 |  |
| follow_move+money_delta | close | pin $1-2k | 13-12 | 52.0 | 6.5 | 0.8 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 17-36 | 32.1 | -11.3 | -30.6 |  |
| money_delta+pin_move | close | pin $1-2k | 9-7 | 56.2 | 12.4 | 9.4 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 8-12 | 40.0 | -4.6 | -22.4 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 12-26 | 31.6 | -12.8 | -31.1 |  |
| follow_move+pin_rlm | close | pin $1-2k | 9-13 | 40.9 | -1.6 | -10.6 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 15-16 | 48.4 | 6.4 | 1.9 |  |
| pin_move+pin_rlm | close | pin $1-2k | 10-12 | 45.5 | 1.9 | -1.9 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 9-12 | 42.9 | -1.1 | -6.3 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 5-13 | 27.8 | -14.2 | -33.8 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 9-13 | 40.9 | -1.6 | -10.6 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 10-14 | 41.7 | -1.0 | -10.1 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 7-14 | 33.3 | -8.0 | -24.4 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 9-16 | 36.0 | -5.4 | -21.1 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 15-16 | 48.4 | 6.4 | 1.9 |  |
| money_delta+money_level | close | pin $1-2k | 4-0 | 100.0 | 55.5 | 95.8 |  |
| money_delta+pin_rlm | close | pin $1-2k | 6-3 | 66.7 | 24.6 | 29.9 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 8-4 | 66.7 | 24.0 | 29.6 |  |
| money_level+pin_rlm | close | pin $1-2k | 4-0 | 100.0 | 55.5 | 93.8 |  |
| money_level+rlm_ratio | close | pin $1-2k | 7-2 | 77.8 | 33.3 | 50.4 |  |
| money_moving+pin_rlm | close | pin $1-2k | 10-10 | 50.0 | 6.0 | 7.9 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 15-13 | 53.6 | 11.1 | 12.8 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 9-13 | 40.9 | -1.1 | -10.3 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 1-4 | 20.0 | -22.5 | -61.8 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 4-8 | 33.3 | -13.2 | -36.0 |  |
| money_delta+pin_value | close | pin $1-2k | 6-3 | 66.7 | 23.4 | 67.2 |  |
| consensus_gap+money_delta | close | pin $1-2k | 2-1 | 66.7 | 22.2 | 144.9 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 0-2 | 0.0 | -44.4 | -100.0 |  |
| pin_rlm+pin_value | close | pin $1-2k | 3-3 | 50.0 | 1.6 | -5.2 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 2-3 | 40.0 | -6.7 | -24.4 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 0-1 | 0.0 | -55.5 | -100.0 |  |
| follow_move+pin_move | close | pin $2k+ | 32-40 | 44.4 | -5.8 | -15.7 |  |
| consensus_gap+money_level | close | pin $2k+ | 26-11 | 70.3 | 9.4 | 10.5 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 18-26 | 40.9 | -1.3 | 11.0 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 11-23 | 32.4 | -10.5 | -28.3 |  |
| money_level+money_moving | close | pin $2k+ | 30-34 | 46.9 | -5.3 | -13.7 |  |
| money_level+sharp_gap | close | pin $2k+ | 30-34 | 46.9 | -5.3 | -13.7 |  |
| money_moving+sharp_gap | close | pin $2k+ | 45-62 | 42.1 | -4.8 | -15.5 |  |
| consensus_gap+pin_value | close | pin $2k+ | 14-8 | 63.6 | 16.4 | 19.5 |  |
| follow_move+money_level | close | pin $2k+ | 22-17 | 56.4 | -3.9 | -8.5 |  |
| follow_move+money_moving | close | pin $2k+ | 18-27 | 40.0 | -8.4 | -22.4 |  |
| follow_move+sharp_gap | close | pin $2k+ | 18-27 | 40.0 | -8.4 | -22.4 |  |
| money_level+pin_move | close | pin $2k+ | 18-12 | 60.0 | 1.0 | 0.5 |  |
| money_moving+pin_move | close | pin $2k+ | 13-19 | 40.6 | -5.8 | -18.8 |  |
| pin_move+sharp_gap | close | pin $2k+ | 13-19 | 40.6 | -5.8 | -18.8 |  |
| money_delta+money_level | close | pin $2k+ | 5-1 | 83.3 | 41.1 | 71.6 |  |
| money_delta+money_moving | close | pin $2k+ | 11-19 | 36.7 | -2.6 | -24.0 |  |
| money_delta+sharp_gap | close | pin $2k+ | 11-19 | 36.7 | -2.6 | -24.0 |  |
| consensus_gap+money_moving | close | pin $2k+ | 12-10 | 54.5 | 1.7 | 14.6 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 12-10 | 54.5 | 1.7 | 14.6 |  |
| money_level+pin_value | close | pin $2k+ | 10-11 | 47.6 | -1.2 | -11.4 |  |
| money_moving+pin_value | close | pin $2k+ | 8-14 | 36.4 | -12.0 | -31.9 |  |
| pin_value+sharp_gap | close | pin $2k+ | 8-14 | 36.4 | -12.0 | -31.9 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 1-2 | 33.3 | -11.1 | 13.3 |  |
| money_level+pin_rlm | close | pin $2k+ | 1-1 | 50.0 | 0.0 | 7.0 |  |
| money_moving+pin_rlm | close | pin $2k+ | 5-11 | 31.2 | -4.2 | -23.2 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 5-11 | 31.2 | -4.2 | -23.2 |  |
| follow_move+money_delta | close | pin $2k+ | 5-10 | 33.3 | -6.9 | -34.1 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 5-13 | 27.8 | -7.4 | -34.4 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 3-9 | 25.0 | -11.1 | -49.4 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 5-13 | 27.8 | -7.4 | -34.4 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 5-13 | 27.8 | -7.4 | -34.4 |  |
| money_level+rlm_ratio | close | pin $2k+ | 2-1 | 66.7 | 25.5 | 32.9 |  |
| consensus_gap+follow_move | close | pin $2k+ | 12-3 | 80.0 | 21.3 | 39.8 |  |
| consensus_gap+pin_move | close | pin $2k+ | 13-3 | 81.2 | 28.5 | 50.4 |  |
| follow_move+pin_value | close | pin $2k+ | 6-6 | 50.0 | -1.4 | 74.7 |  |
| pin_move+pin_value | close | pin $2k+ | 10-11 | 47.6 | -2.2 | -10.6 |  |
| follow_move+pin_rlm | close | pin $2k+ | 4-9 | 30.8 | -2.6 | -23.4 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 4-9 | 30.8 | -2.6 | -23.4 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 2-3 | 40.0 | -7.4 | 170.2 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 4-13 | 23.5 | -14.6 | -42.9 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 4-13 | 23.5 | -14.6 | -42.9 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 3-8 | 27.3 | -12.5 | -46.4 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 2-10 | 16.7 | -16.7 | -54.3 |  |
| money_delta+pin_move | close | pin $2k+ | 5-8 | 38.5 | -2.8 | -24.0 |  |
| money_delta+pin_rlm | close | pin $2k+ | 2-7 | 22.2 | -11.1 | -53.1 |  |
| pin_move+pin_rlm | close | pin $2k+ | 4-8 | 33.3 | -0.0 | -17.2 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 4-8 | 33.3 | -2.0 | -21.1 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 2-8 | 20.0 | -13.3 | -45.2 |  |
| consensus_gap+money_delta | close | pin $2k+ | 2-0 | 100.0 | 43.2 | 87.8 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 2-2 | 50.0 | 10.8 | 32.7 |  |
| money_delta+pin_value | close | pin $2k+ | 2-2 | 50.0 | -3.4 | -6.1 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 2-1 | 66.7 | 25.5 | 74.9 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 1-0 | 100.0 | 43.2 | 84.7 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 4-2 | 66.7 | 20.4 | 28.1 |  |
| consensus_gap+money_level | close | pin limit <$1k | 4-1 | 80.0 | 24.5 | 50.5 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 3-3 | 50.0 | 3.7 | -3.7 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 6-3 | 66.7 | 16.1 | 26.0 |  |
| follow_move+money_level | close | pin limit <$1k | 9-14 | 39.1 | -13.1 | -25.1 |  |
| follow_move+money_moving | close | pin limit <$1k | 8-20 | 28.6 | -19.9 | -45.1 |  |
| follow_move+pin_value | close | pin limit <$1k | 8-4 | 66.7 | 13.8 | 26.9 |  |
| money_level+money_moving | close | pin limit <$1k | 10-16 | 38.5 | -13.6 | -26.9 |  |
| money_level+pin_value | close | pin limit <$1k | 12-5 | 70.6 | 15.7 | 33.9 |  |
| money_moving+pin_value | close | pin limit <$1k | 8-7 | 53.3 | 2.2 | 1.5 |  |
| follow_move+pin_move | close | pin limit <$1k | 10-15 | 40.0 | -8.5 | -22.8 |  |
| money_level+pin_move | close | pin limit <$1k | 11-10 | 52.4 | 0.5 | -0.2 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 14-27 | 34.1 | -14.3 | -34.6 |  |
| pin_move+pin_value | close | pin limit <$1k | 9-6 | 60.0 | 8.1 | 14.3 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 6-9 | 40.0 | -4.5 | -22.5 |  |
| money_moving+pin_move | close | pin limit <$1k | 8-13 | 38.1 | -10.1 | -27.0 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 2-1 | 66.7 | 25.9 | 30.3 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 2-2 | 50.0 | 8.3 | -2.3 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 1-2 | 33.3 | -7.5 | -33.3 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 3-1 | 75.0 | 33.3 | 45.5 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 2-1 | 66.7 | 25.9 | 30.3 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 3-2 | 60.0 | 15.5 | 15.6 |  |
| follow_move+money_delta | close | pin limit <$1k | 4-9 | 30.8 | -13.7 | -40.5 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 3-8 | 27.3 | -16.2 | -46.7 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 5-11 | 31.2 | -13.3 | -39.8 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 8-19 | 29.6 | -18.5 | -43.1 |  |
| money_delta+money_moving | close | pin limit <$1k | 7-10 | 41.2 | -3.3 | -20.3 |  |
| money_delta+pin_move | close | pin limit <$1k | 2-7 | 22.2 | -21.1 | -56.1 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 2-6 | 25.0 | -18.1 | -50.6 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 2-3 | 40.0 | -2.3 | -21.8 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 4-8 | 33.3 | -11.2 | -35.6 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 7-10 | 41.2 | -3.3 | -20.3 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 3-9 | 25.0 | -18.6 | -51.2 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 2-6 | 25.0 | -18.1 | -51.1 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 5-11 | 31.2 | -13.3 | -39.8 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 3-9 | 25.0 | -18.6 | -51.2 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 4-5 | 44.4 | -0.0 | -13.7 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 3-8 | 27.3 | -16.2 | -46.7 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 6-13 | 31.6 | -15.8 | -39.2 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 1-4 | 20.0 | -22.3 | -60.0 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 3-8 | 27.3 | -16.2 | -46.7 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 3-9 | 25.0 | -18.6 | -51.2 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 2-6 | 25.0 | -18.1 | -51.1 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 2-6 | 25.0 | -18.1 | -51.1 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 5-11 | 31.2 | -13.3 | -39.8 |  |
| money_delta+pin_value | close | pin limit <$1k | 4-1 | 80.0 | 33.3 | 52.8 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 2-1 | 66.7 | 22.2 | 27.3 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 2-1 | 66.7 | 18.5 | 26.0 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 7-6 | 53.8 | 3.4 | 2.5 |  |
| money_level+sharp_gap | close | pin limit <$1k | 8-15 | 34.8 | -16.9 | -33.8 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 0-2 | 0.0 | -44.5 | -100.0 |  |
| money_delta+money_level | close | pin limit <$1k | 1-4 | 20.0 | -24.5 | -61.0 |  |
| money_level+pin_rlm | close | pin limit <$1k | 2-3 | 40.0 | -4.5 | -22.8 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 2-4 | 33.3 | -11.2 | -35.7 |  |
| rlm_quiet | early | <1k bets | 9-18 | 33.3 | -5.0 | -24.4 | 0.86 |
| rlm_quiet | early | pin $1-2k | 1-1 | 50.0 | 16.7 | 16.0 | 1.15 |
| rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -44.5 | -100.0 | 0.0 |
| pin_move | early | <1k bets | 4-6 | 40.0 | -9.7 | -23.6 | 0.3 |
| pin_move | early | pin $1-2k | 0-2 | 0.0 | -43.2 | -100.0 | 0.0 |
| pin_move | early | pin limit <$1k | 4-4 | 50.0 | -1.4 | -4.5 | 0.38 |
| money_delta | early | <1k bets | 2-3 | 40.0 | -0.0 | -23.6 | 3.0 |
| money_delta | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| pin_rlm | early | <1k bets | 0-1 | 0.0 | -66.7 | -100.0 | 1.5 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -66.7 | -100.0 | 1.5 |
| follow_move | early | <1k bets | 94-109 | 46.3 | -2.6 | -12.6 | 0.07 |
| follow_move | early | pin $1-2k | 9-8 | 52.9 | 8.4 | 7.6 | -0.06 |
| follow_move | early | pin limit <$1k | 6-8 | 42.9 | -2.9 | -11.2 | -0.45 |
| rlm_ratio | early | <1k bets | 5-11 | 31.2 | -11.2 | -35.0 | 0.82 |
| rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -66.7 | -100.0 | 1.5 |
| rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| money_level | early | <1k bets | 39-30 | 56.5 | -2.6 | -9.8 | -0.24 |
| money_level | early | pin $1-2k | 1-2 | 33.3 | -33.3 | -44.4 | -0.23 |
| money_level | early | pin limit <$1k | 2-2 | 50.0 | -2.7 | -4.5 | 1.25 |
| sharp_gap | early | <1k bets | 25-36 | 41.0 | -6.4 | -18.4 | 0.67 |
| sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -33.3 | -44.4 | -0.23 |
| sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | 2.7 | -4.5 | 0.75 |
| money_moving | early | <1k bets | 24-28 | 46.2 | -1.5 | -14.1 | 0.35 |
| money_moving | early | pin $1-2k | 0-1 | 0.0 | -66.7 | -100.0 | 1.7 |
| money_moving | early | pin limit <$1k | 2-1 | 66.7 | 22.2 | 27.3 | 0.0 |
| pin_value | early | <1k bets | 11-12 | 47.8 | -1.1 | -9.9 | -0.01 |
| pin_value | early | pin $1-2k | 3-7 | 30.0 | -16.9 | -43.9 | -0.03 |
| pin_value | early | pin limit <$1k | 8-5 | 61.5 | 11.1 | 16.3 | 0.0 |
| consensus_gap | early | <1k bets | 56-38 | 59.6 | 7.8 | 6.2 | 0.48 |
| consensus_gap | early | pin $1-2k | 6-3 | 66.7 | 17.4 | 19.3 | -0.9 |
| consensus_gap | early | pin limit <$1k | 4-1 | 80.0 | 28.9 | 51.9 | 0.6 |
| follow_move+money_level | early | <1k bets | 14-10 | 58.3 | -2.3 | -15.4 | 0.53 |
| follow_move+sharp_gap | early | <1k bets | 11-17 | 39.3 | -9.2 | -26.6 | 1.05 |
| money_level+sharp_gap | early | <1k bets | 15-17 | 46.9 | -8.7 | -18.2 | 0.33 |
| follow_move+money_moving | early | <1k bets | 11-12 | 47.8 | -0.6 | -13.5 | 0.49 |
| money_level+money_moving | early | <1k bets | 13-11 | 54.2 | -1.9 | -6.8 | 0.2 |
| consensus_gap+money_level | early | <1k bets | 12-7 | 63.2 | 4.1 | -8.7 | -0.22 |
| follow_move+rlm_quiet | early | <1k bets | 9-18 | 33.3 | -5.0 | -24.4 | 0.86 |
| follow_move+rlm_ratio | early | <1k bets | 5-11 | 31.2 | -11.2 | -35.0 | 0.82 |
| rlm_quiet+rlm_ratio | early | <1k bets | 4-8 | 33.3 | -5.6 | -29.3 | 0.3 |
| rlm_quiet+sharp_gap | early | <1k bets | 4-9 | 30.8 | -8.6 | -34.7 | 0.28 |
| rlm_ratio+sharp_gap | early | <1k bets | 5-11 | 31.2 | -11.2 | -35.0 | 0.82 |
| consensus_gap+follow_move | early | <1k bets | 7-5 | 58.3 | 4.6 | -8.3 | 0.53 |
| money_moving+rlm_quiet | early | <1k bets | 5-6 | 45.5 | 7.0 | 3.3 | 0.55 |
| money_moving+rlm_ratio | early | <1k bets | 5-5 | 50.0 | 8.7 | 4.0 | 0.99 |
| money_moving+sharp_gap | early | <1k bets | 15-19 | 44.1 | -1.7 | -12.0 | 0.76 |
| consensus_gap+money_moving | early | <1k bets | 4-3 | 57.1 | 7.9 | -11.9 | 0.74 |
| consensus_gap+sharp_gap | early | <1k bets | 6-5 | 54.5 | 6.1 | -10.5 | 0.05 |
| money_level+rlm_ratio | early | <1k bets | 1-3 | 25.0 | -28.1 | -52.3 | 2.38 |
| follow_move+pin_move | early | <1k bets | 1-3 | 25.0 | -21.9 | -52.3 | 0.5 |
| follow_move+money_delta | early | <1k bets | 1-1 | 50.0 | 5.5 | -4.5 | 1.5 |
| money_delta+money_level | early | <1k bets | 1-2 | 33.3 | -7.5 | -36.4 | 1.73 |
| money_delta+money_moving | early | <1k bets | 2-3 | 40.0 | -0.0 | -23.6 | 3.0 |
| money_delta+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 5.5 | -4.5 | 1.5 |
| money_delta+sharp_gap | early | <1k bets | 2-3 | 40.0 | -0.0 | -23.6 | 3.0 |
| follow_move+pin_value | early | <1k bets | 3-3 | 50.0 | 4.1 | -4.5 | -0.83 |
| consensus_gap+pin_move | early | <1k bets | 1-0 | 100.0 | 44.5 | 90.9 | 0.0 |
| consensus_gap+pin_value | early | <1k bets | 5-1 | 83.3 | 33.5 | 57.8 | 0.0 |
| money_level+pin_move | early | <1k bets | 1-1 | 50.0 | -5.5 | -4.5 | 1.5 |
| money_level+pin_value | early | <1k bets | 2-2 | 50.0 | -5.5 | -4.5 | 1.43 |
| pin_move+pin_value | early | <1k bets | 2-5 | 28.6 | -21.8 | -45.5 | 0.43 |
| money_moving+pin_value | early | <1k bets | 1-1 | 50.0 | -5.6 | -4.5 | 1.35 |
| pin_value+sharp_gap | early | <1k bets | 1-2 | 33.3 | -22.2 | -36.4 | 1.9 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| consensus_gap+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| follow_move+pin_rlm | early | <1k bets | 0-1 | 0.0 | -66.7 | -100.0 | 1.5 |
| money_level+pin_rlm | early | <1k bets | 0-1 | 0.0 | -66.7 | -100.0 | 1.5 |
| pin_rlm+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -66.7 | -100.0 | 1.5 |
| pin_rlm+sharp_gap | early | <1k bets | 0-1 | 0.0 | -66.7 | -100.0 | 1.5 |
| pin_move+sharp_gap | early | <1k bets | 0-1 | 0.0 | -55.5 | -100.0 | 3.0 |
| pin_move+pin_value | early | pin $1-2k | 0-2 | 0.0 | -43.2 | -100.0 | 0.0 |
| follow_move+rlm_quiet | early | pin $1-2k | 1-1 | 50.0 | 16.7 | 16.0 | 1.15 |
| money_level+money_moving | early | pin $1-2k | 0-1 | 0.0 | -66.7 | -100.0 | 1.7 |
| money_level+pin_value | early | pin $1-2k | 0-1 | 0.0 | -66.7 | -100.0 | 1.7 |
| money_level+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -33.3 | -44.4 | -0.23 |
| money_moving+pin_value | early | pin $1-2k | 0-1 | 0.0 | -66.7 | -100.0 | 1.7 |
| money_moving+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -66.7 | -100.0 | 1.7 |
| pin_value+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -66.7 | -100.0 | 1.7 |
| consensus_gap+pin_value | early | pin $1-2k | 2-1 | 66.7 | 18.9 | 24.7 | -0.67 |
| follow_move+money_level | early | pin $1-2k | 0-1 | 0.0 | -66.7 | -100.0 | 1.5 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -66.7 | -100.0 | 1.5 |
| follow_move+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -66.7 | -100.0 | 1.5 |
| follow_move+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -66.7 | -100.0 | 1.5 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -66.7 | -100.0 | 1.5 |
| money_level+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -66.7 | -100.0 | 1.5 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -66.7 | -100.0 | 1.5 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -66.7 | -100.0 | 1.5 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -66.7 | -100.0 | 1.5 |
| consensus_gap+follow_move | early | pin $1-2k | 1-0 | 100.0 | 66.7 | 106.0 | 1.5 |
| follow_move+pin_move | early | pin $1-2k | 0-1 | 0.0 | -43.2 | -100.0 | 0.0 |
| follow_move+pin_value | early | pin $1-2k | 0-1 | 0.0 | -43.2 | -100.0 | 0.0 |
| consensus_gap+money_level | early | pin $1-2k | 1-0 | 100.0 | 33.3 | 66.7 | -3.9 |
| consensus_gap+sharp_gap | early | pin $1-2k | 1-0 | 100.0 | 33.3 | 66.7 | -3.9 |
| follow_move+pin_move | early | pin limit <$1k | 1-2 | 33.3 | -14.8 | -36.4 | 0.67 |
| follow_move+pin_value | early | pin limit <$1k | 3-2 | 60.0 | 13.5 | 14.5 | -1.0 |
| consensus_gap+money_level | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 90.9 | 0.5 |
| consensus_gap+pin_move | early | pin limit <$1k | 1-0 | 100.0 | 44.5 | 90.9 | 0.0 |
| consensus_gap+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 48.2 | 90.9 | 0.67 |
| follow_move+money_moving | early | pin limit <$1k | 1-1 | 50.0 | 5.5 | -4.5 | 0.5 |
| follow_move+rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -44.5 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 5.5 | -4.5 | 0.5 |
| money_level+pin_move | early | pin limit <$1k | 1-1 | 50.0 | -5.5 | -4.5 | 1.5 |
| money_level+pin_value | early | pin limit <$1k | 2-1 | 66.7 | 14.8 | 27.3 | 1.33 |
| money_moving+rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -44.5 | -100.0 | 0.0 |
| money_moving+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 22.2 | 27.3 | 0.0 |
| pin_move+pin_value | early | pin limit <$1k | 2-3 | 40.0 | -13.3 | -23.6 | 0.6 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -44.5 | -100.0 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| consensus_gap+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| follow_move+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| follow_move+money_level | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| follow_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| money_delta+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| money_delta+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| money_delta+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| money_level+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| money_level+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| money_level+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 | 2.0 |
| money_moving+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| pin_value+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 | 2.0 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 55.5 | 90.9 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -55.5 | -100.0 | 3.0 |
