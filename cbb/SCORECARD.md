# CBB scorecard

Generated 2026-11-25 00:08 UTC. 853 graded games (59 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**684 games before 2026-11-21 (fit) · 169 on or after it (forward).**

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
sample ran **47.3% favourites** (n=852) and **50.3% overs** (n=853) and **72.0% moneyline favourites** (n=737).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-21. Nothing in the engine was chosen using these. n=169 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 12-20 | 37.5 | 39.2 | -1.7 | -2.99 | -9.3 | 1.21 | 53.1 | DROP: below break-even |
| pin_move | both | 4-6 | 40.0 | 49.5 | -9.5 | -2.36 | -23.6 | 0.3 | 30.0 | keep collecting (10/30) |
| money_delta | both | 4-3 | 57.1 | 39.1 | 18.1 | +3.47 | 49.5 | 3.06 | 100.0 | keep collecting (7/30) |
| pin_rlm | both | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.5 | 100.0 | keep collecting (1/30) |
| follow_move | both | 116-136 | 46.0 | 48.8 | -2.8 | -28.87 | -11.5 | 0.13 | 38.9 | DROP: below break-even |
| rlm_ratio | both | 7-11 | 38.9 | 42.4 | -3.6 | -0.95 | -5.3 | 1.08 | 61.1 | keep collecting (18/30) |
| money_level | both | 41-33 | 55.4 | 58.4 | -3.0 | -8.44 | -11.4 | -0.42 | 37.8 | no edge shown yet |
| sharp_gap | both | 29-37 | 43.9 | 47.4 | -3.5 | -6.24 | -9.4 | 0.58 | 54.5 | no edge shown yet |
| money_moving | both | 26-29 | 47.3 | 47.3 | -0.0 | -3.71 | -6.7 | 0.46 | 50.9 | no edge shown yet |
| pin_value | both | 11-12 | 47.8 | 49.3 | -1.5 | -2.27 | -9.9 | -0.01 | 34.8 | keep collecting (23/30) |
| consensus_gap | both | 77-55 | 58.3 | 52.4 | 6.0 | +5.51 | 4.2 | 0.39 | 48.5 | no edge shown yet |
| follow_move+money_level | both | 14-10 | 58.3 | 60.1 | -1.8 | -3.69 | -15.4 | 0.53 | 41.7 | keep collecting (24/30) |
| follow_move+sharp_gap | both | 13-17 | 43.3 | 47.6 | -4.3 | -2.79 | -9.3 | 1.19 | 56.7 | no edge shown yet |
| money_level+sharp_gap | both | 17-18 | 48.6 | 55.0 | -6.4 | -5.48 | -15.7 | 0.05 | 51.4 | no edge shown yet |
| follow_move+money_moving | both | 13-13 | 50.0 | 47.6 | 2.4 | +0.55 | 2.1 | 0.72 | 50.0 | keep collecting (26/30) |
| money_level+money_moving | both | 13-11 | 54.2 | 55.3 | -1.1 | -1.64 | -6.8 | 0.2 | 41.7 | keep collecting (24/30) |
| consensus_gap+money_level | both | 13-9 | 59.1 | 59.6 | -0.5 | -2.78 | -12.7 | -0.5 | 36.4 | keep collecting (22/30) |
| follow_move+rlm_quiet | both | 12-20 | 37.5 | 39.2 | -1.7 | -2.99 | -9.3 | 1.21 | 53.1 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 7-11 | 38.9 | 42.4 | -3.6 | -0.95 | -5.3 | 1.08 | 61.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | both | 6-8 | 42.9 | 39.1 | 3.8 | +1.14 | 8.1 | 0.71 | 50.0 | keep collecting (14/30) |
| rlm_quiet+sharp_gap | both | 6-9 | 40.0 | 39.6 | 0.4 | +0.14 | 0.9 | 0.67 | 46.7 | keep collecting (15/30) |
| rlm_ratio+sharp_gap | both | 7-11 | 38.9 | 42.4 | -3.6 | -0.95 | -5.3 | 1.08 | 61.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 9-5 | 64.3 | 53.7 | 10.5 | +0.82 | 5.8 | 0.66 | 64.3 | keep collecting (14/30) |
| money_moving+rlm_quiet | both | 7-7 | 50.0 | 39.1 | 10.9 | +4.02 | 28.7 | 0.96 | 57.1 | keep collecting (14/30) |
| money_moving+rlm_ratio | both | 7-5 | 58.3 | 40.8 | 17.6 | +5.05 | 42.0 | 1.36 | 66.7 | keep collecting (12/30) |
| money_moving+sharp_gap | both | 17-19 | 47.2 | 45.2 | 2.1 | +0.56 | 1.5 | 0.89 | 58.3 | no edge shown yet |
| consensus_gap+money_moving | both | 4-3 | 57.1 | 49.6 | 7.5 | -0.83 | -11.9 | 0.74 | 57.1 | keep collecting (7/30) |
| consensus_gap+sharp_gap | both | 7-5 | 58.3 | 48.8 | 9.5 | -0.28 | -2.3 | -0.03 | 50.0 | keep collecting (12/30) |
| money_level+rlm_ratio | both | 1-3 | 25.0 | 54.2 | -29.2 | -2.09 | -52.3 | 2.38 | 100.0 | keep collecting (4/30) |
| follow_move+pin_move | both | 1-3 | 25.0 | 48.1 | -23.1 | -2.09 | -52.3 | 0.5 | 25.0 | keep collecting (4/30) |
| follow_move+money_delta | both | 3-1 | 75.0 | 40.1 | 34.9 | +4.56 | 114.0 | 2.35 | 100.0 | keep collecting (4/30) |
| money_delta+money_level | both | 1-2 | 33.3 | 42.5 | -9.2 | -1.09 | -36.4 | 1.73 | 100.0 | keep collecting (3/30) |
| money_delta+money_moving | both | 4-3 | 57.1 | 39.1 | 18.1 | +3.47 | 49.5 | 3.06 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | both | 3-1 | 75.0 | 40.1 | 34.9 | +4.56 | 114.0 | 2.35 | 100.0 | keep collecting (4/30) |
| money_delta+sharp_gap | both | 4-3 | 57.1 | 39.1 | 18.1 | +3.47 | 49.5 | 3.06 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| follow_move+pin_value | both | 3-3 | 50.0 | 47.4 | 2.6 | -0.27 | -4.5 | -0.83 | 16.7 | keep collecting (6/30) |
| consensus_gap+pin_move | both | 1-0 | 100.0 | 52.7 | 47.3 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+pin_value | both | 5-1 | 83.3 | 49.6 | 33.7 | +3.47 | 57.8 | 0.0 | 33.3 | keep collecting (6/30) |
| money_level+pin_move | both | 1-1 | 50.0 | 52.7 | -2.7 | -0.09 | -4.5 | 1.5 | 50.0 | keep collecting (2/30) |
| money_level+pin_value | both | 2-2 | 50.0 | 54.9 | -4.9 | -0.18 | -4.5 | 1.43 | 75.0 | keep collecting (4/30) |
| pin_move+pin_value | both | 2-5 | 28.6 | 49.7 | -21.1 | -3.18 | -45.5 | 0.43 | 28.6 | keep collecting (7/30) |
| money_moving+pin_value | both | 1-1 | 50.0 | 57.2 | -7.2 | -0.09 | -4.5 | 1.35 | 100.0 | keep collecting (2/30) |
| pin_value+sharp_gap | both | 1-2 | 33.3 | 55.7 | -22.4 | -1.09 | -36.4 | 1.9 | 100.0 | keep collecting (3/30) |
| consensus_gap+money_delta | both | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | both | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+rlm_ratio | both | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | both | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+sharp_gap | both | 0-1 | 0.0 | 52.7 | -52.7 | -1.0 | -100.0 | 3.0 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_quiet | both | 2-0 | 100.0 | 32.9 | 67.1 | +4.65 | 232.5 | 3.2 | 100.0 | keep collecting (2/30) |
| rlm_quiet | moneyline | 7-11 | 38.9 | 32.9 | 6.0 | +1.46 | 8.1 | 1.65 | 50.0 | keep collecting (18/30) |
| rlm_quiet | total | 5-9 | 35.7 | 47.3 | -11.6 | -4.45 | -31.8 | 0.64 | 57.1 | keep collecting (14/30) |
| pin_move | spread | 0-2 | 0.0 | 45.0 | -45.0 | -2.0 | -100.0 | 0.0 | 0.0 | keep collecting (2/30) |
| pin_move | total | 4-4 | 50.0 | 50.7 | -0.7 | -0.36 | -4.5 | 0.38 | 37.5 | keep collecting (8/30) |
| money_delta | moneyline | 2-2 | 50.0 | 32.9 | 17.1 | +2.65 | 66.2 | 2.6 | 100.0 | keep collecting (4/30) |
| money_delta | total | 2-1 | 66.7 | 47.3 | 19.3 | +0.82 | 27.3 | 3.67 | 100.0 | keep collecting (3/30) |
| pin_rlm | moneyline | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.5 | 100.0 | keep collecting (1/30) |
| follow_move | moneyline | 50-44 | 53.2 | 46.7 | 6.5 | +2.26 | 2.4 | -0.2 | 33.0 | no edge shown yet |
| follow_move | spread | 27-40 | 40.3 | 51.1 | -10.8 | -14.89 | -22.2 | -0.07 | 29.9 | DROP: below break-even |
| follow_move | total | 39-52 | 42.9 | 49.2 | -6.4 | -16.24 | -17.8 | 0.63 | 51.6 | DROP: below break-even |
| rlm_ratio | moneyline | 3-6 | 33.3 | 36.7 | -3.4 | +0.41 | 4.6 | 0.72 | 44.4 | keep collecting (9/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| rlm_ratio | total | 4-4 | 50.0 | 47.3 | 2.7 | -0.36 | -4.5 | 1.0 | 75.0 | keep collecting (8/30) |
| money_level | moneyline | 22-18 | 55.0 | 63.7 | -8.7 | -10.7 | -26.8 | -0.58 | 32.5 | no edge shown yet |
| money_level | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level | total | 19-14 | 57.6 | 52.2 | 5.4 | +3.27 | 9.9 | -0.39 | 42.4 | no edge shown yet |
| sharp_gap | moneyline | 13-21 | 38.2 | 45.0 | -6.7 | -4.77 | -14.0 | 0.51 | 58.8 | DROP: below break-even |
| sharp_gap | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| sharp_gap | total | 16-15 | 51.6 | 49.9 | 1.7 | -0.46 | -1.5 | 0.52 | 48.4 | no edge shown yet |
| money_moving | moneyline | 12-16 | 42.9 | 45.1 | -2.3 | -3.46 | -12.4 | 0.62 | 60.7 | keep collecting (28/30) |
| money_moving | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving | total | 14-12 | 53.8 | 49.4 | 4.5 | +0.76 | 2.9 | 0.12 | 38.5 | keep collecting (26/30) |
| pin_value | moneyline | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| pin_value | spread | 6-7 | 46.2 | 47.3 | -1.1 | -1.81 | -14.0 | -0.15 | 23.1 | keep collecting (13/30) |
| pin_value | total | 5-4 | 55.6 | 50.3 | 5.3 | +0.54 | 6.1 | 0.0 | 44.4 | keep collecting (9/30) |
| consensus_gap | moneyline | 37-28 | 56.9 | 55.5 | 1.4 | -3.16 | -4.9 | 0.22 | 47.7 | no edge shown yet |
| consensus_gap | spread | 15-11 | 57.7 | 48.5 | 9.2 | +2.14 | 8.2 | 0.19 | 34.6 | keep collecting (26/30) |
| consensus_gap | total | 25-16 | 61.0 | 49.8 | 11.2 | +6.53 | 15.9 | 0.8 | 58.5 | no edge shown yet |
| consensus_gap+money_level | moneyline | 10-8 | 55.6 | 61.4 | -5.8 | -4.47 | -24.8 | -0.73 | 33.3 | keep collecting (18/30) |
| follow_move+rlm_quiet | moneyline | 7-11 | 38.9 | 32.9 | 6.0 | +1.46 | 8.1 | 1.65 | 50.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 3-6 | 33.3 | 36.7 | -3.4 | +0.41 | 4.6 | 0.72 | 44.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 5-7 | 41.7 | 44.3 | -2.6 | -0.06 | -0.5 | 1.56 | 50.0 | keep collecting (12/30) |
| rlm_quiet+rlm_ratio | moneyline | 3-5 | 37.5 | 32.9 | 4.6 | +1.41 | 17.6 | 0.62 | 37.5 | keep collecting (8/30) |
| rlm_quiet+sharp_gap | moneyline | 3-5 | 37.5 | 32.9 | 4.6 | +1.41 | 17.6 | 0.62 | 37.5 | keep collecting (8/30) |
| rlm_ratio+sharp_gap | moneyline | 3-6 | 33.3 | 36.7 | -3.4 | +0.41 | 4.6 | 0.72 | 44.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 5-1 | 83.3 | 61.4 | 21.9 | +1.18 | 19.7 | -0.62 | 33.3 | keep collecting (6/30) |
| consensus_gap+money_moving | moneyline | 3-3 | 50.0 | 50.0 | -0.0 | -1.74 | -29.0 | 0.7 | 50.0 | keep collecting (6/30) |
| consensus_gap+sharp_gap | moneyline | 5-4 | 55.6 | 48.1 | 7.5 | -1.06 | -11.8 | -0.27 | 44.4 | keep collecting (9/30) |
| money_level+money_moving | moneyline | 5-5 | 50.0 | 60.3 | -10.3 | -2.95 | -29.4 | 0.49 | 40.0 | keep collecting (10/30) |
| money_level+sharp_gap | moneyline | 7-9 | 43.8 | 58.5 | -14.8 | -5.56 | -34.8 | -0.2 | 50.0 | keep collecting (16/30) |
| money_moving+sharp_gap | moneyline | 6-12 | 33.3 | 40.5 | -7.2 | -2.47 | -13.7 | 1.34 | 72.2 | keep collecting (18/30) |
| follow_move+money_level | moneyline | 9-4 | 69.2 | 67.1 | 2.1 | -2.23 | -17.2 | 0.06 | 23.1 | keep collecting (13/30) |
| follow_move+money_moving | moneyline | 8-5 | 61.5 | 46.1 | 15.5 | +4.0 | 30.8 | 0.51 | 46.2 | keep collecting (13/30) |
| money_moving+rlm_quiet | moneyline | 4-4 | 50.0 | 32.9 | 17.1 | +4.29 | 53.6 | 1.3 | 62.5 | keep collecting (8/30) |
| money_moving+rlm_ratio | moneyline | 3-3 | 50.0 | 32.9 | 17.1 | +3.41 | 56.8 | 0.88 | 50.0 | keep collecting (6/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_rlm | moneyline | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | moneyline | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.5 | 100.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+money_moving | moneyline | 2-2 | 50.0 | 32.9 | 17.1 | +2.65 | 66.2 | 2.6 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-2 | 50.0 | 32.9 | 17.1 | +2.65 | 66.2 | 2.6 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_level | moneyline | 0-1 | 0.0 | 32.9 | -32.9 | -1.0 | -100.0 | 2.2 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 2-0 | 100.0 | 32.9 | 67.1 | +4.65 | 232.5 | 3.2 | 100.0 | keep collecting (2/30) |
| money_delta+rlm_quiet | moneyline | 2-0 | 100.0 | 32.9 | 67.1 | +4.65 | 232.5 | 3.2 | 100.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 32.9 | 67.1 | +4.65 | 232.5 | 3.2 | 100.0 | keep collecting (2/30) |
| follow_move+money_level | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| follow_move+money_moving | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to sharp_gap alone, not independent confirmation |
| money_level+money_moving | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+rlm_ratio | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+sharp_gap | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| money_moving+sharp_gap | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 1-1 | 50.0 | 45.0 | 5.0 | -0.09 | -4.5 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | spread | 0-2 | 0.0 | 45.0 | -45.0 | -2.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| consensus_gap+pin_value | spread | 2-1 | 66.7 | 48.3 | 18.3 | +0.74 | 24.7 | -0.67 | 0.0 | keep collecting (3/30) |
| follow_move+pin_move | spread | 0-1 | 0.0 | 45.0 | -45.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_level | total | 5-5 | 50.0 | 51.6 | -1.6 | -0.46 | -4.6 | 0.7 | 60.0 | keep collecting (10/30) |
| follow_move+sharp_gap | total | 8-9 | 47.1 | 49.5 | -2.5 | -1.73 | -10.2 | 0.71 | 58.8 | keep collecting (17/30) |
| money_level+sharp_gap | total | 10-8 | 55.6 | 51.8 | 3.8 | +1.08 | 6.0 | 0.0 | 50.0 | keep collecting (18/30) |
| follow_move+money_moving | total | 5-7 | 41.7 | 48.7 | -7.0 | -2.46 | -20.5 | 0.58 | 50.0 | keep collecting (12/30) |
| money_level+money_moving | total | 8-5 | 61.5 | 51.4 | 10.1 | +2.31 | 17.7 | -0.38 | 38.5 | keep collecting (13/30) |
| follow_move+rlm_quiet | total | 5-9 | 35.7 | 47.3 | -11.6 | -4.45 | -31.8 | 0.64 | 57.1 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 4-4 | 50.0 | 47.3 | 2.7 | -0.36 | -4.5 | 1.0 | 75.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 3-3 | 50.0 | 47.3 | 2.7 | -0.27 | -4.5 | 0.83 | 66.7 | keep collecting (6/30) |
| rlm_quiet+sharp_gap | total | 3-4 | 42.9 | 47.3 | -4.5 | -1.27 | -18.2 | 0.71 | 57.1 | keep collecting (7/30) |
| rlm_ratio+sharp_gap | total | 4-4 | 50.0 | 47.3 | 2.7 | -0.36 | -4.5 | 1.0 | 75.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | total | 3-3 | 50.0 | 47.3 | 2.7 | -0.27 | -4.5 | 0.5 | 50.0 | keep collecting (6/30) |
| money_moving+rlm_ratio | total | 4-1 | 80.0 | 47.3 | 32.7 | +2.64 | 52.7 | 1.2 | 80.0 | keep collecting (5/30) |
| money_moving+sharp_gap | total | 11-6 | 64.7 | 49.5 | 15.2 | +4.03 | 23.7 | 0.18 | 41.2 | keep collecting (17/30) |
| follow_move+pin_move | total | 1-2 | 33.3 | 49.1 | -15.8 | -1.09 | -36.4 | 0.67 | 33.3 | keep collecting (3/30) |
| consensus_gap+follow_move | total | 4-4 | 50.0 | 48.0 | 2.0 | -0.36 | -4.6 | 1.62 | 87.5 | keep collecting (8/30) |
| consensus_gap+money_level | total | 3-1 | 75.0 | 51.3 | 23.7 | +1.69 | 42.2 | 0.5 | 50.0 | keep collecting (4/30) |
| consensus_gap+sharp_gap | total | 2-1 | 66.7 | 50.9 | 15.8 | +0.78 | 26.0 | 0.67 | 66.7 | keep collecting (3/30) |
| follow_move+money_delta | total | 1-1 | 50.0 | 47.3 | 2.7 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+money_level | total | 1-1 | 50.0 | 47.3 | 2.7 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+money_moving | total | 2-1 | 66.7 | 47.3 | 19.3 | +0.82 | 27.3 | 3.67 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | total | 1-1 | 50.0 | 47.3 | 2.7 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 2-1 | 66.7 | 47.3 | 19.3 | +0.82 | 27.3 | 3.67 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+rlm_ratio | total | 1-1 | 50.0 | 47.3 | 2.7 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| follow_move+pin_value | total | 2-2 | 50.0 | 48.7 | 1.3 | -0.18 | -4.5 | -1.0 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | total | 1-0 | 100.0 | 52.7 | 47.3 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+pin_value | total | 3-0 | 100.0 | 50.9 | 49.1 | +2.73 | 90.9 | 0.67 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | total | 1-1 | 50.0 | 52.7 | -2.7 | -0.09 | -4.5 | 1.5 | 50.0 | keep collecting (2/30) |
| money_level+pin_value | total | 2-1 | 66.7 | 50.9 | 15.8 | +0.82 | 27.3 | 1.33 | 66.7 | keep collecting (3/30) |
| pin_move+pin_value | total | 2-3 | 40.0 | 51.6 | -11.6 | -1.18 | -23.6 | 0.6 | 40.0 | keep collecting (5/30) |
| consensus_gap+money_delta | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_moving | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+rlm_ratio | total | 1-0 | 100.0 | 47.3 | 52.7 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | 2.0 | 100.0 | keep collecting (2/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 52.7 | -52.7 | -1.0 | -100.0 | 3.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 63-116 | 35.2 | 42.7 | -7.5 | -35.67 | -19.9 |  |  | DROP: below break-even |
| pin_move | both | 107-135 | 44.2 | 49.4 | -5.1 | -34.38 | -14.2 |  |  | DROP: below break-even |
| money_delta | both | 63-73 | 46.3 | 43.8 | 2.5 | -5.69 | -4.2 |  |  | no edge shown yet |
| pin_rlm | both | 18-39 | 31.6 | 41.3 | -9.7 | -17.28 | -30.3 |  |  | DROP: below break-even |
| follow_move | both | 182-226 | 44.6 | 49.3 | -4.7 | -53.31 | -13.1 |  |  | DROP: below break-even |
| rlm_ratio | both | 38-70 | 35.2 | 41.5 | -6.3 | -26.95 | -25.0 |  |  | DROP: below break-even |
| money_level | both | 245-186 | 56.8 | 55.6 | 1.2 | -11.56 | -2.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 185-218 | 45.9 | 48.1 | -2.2 | -44.03 | -10.9 |  |  | DROP: below break-even |
| money_moving | both | 192-214 | 47.3 | 48.8 | -1.5 | -38.38 | -9.5 |  |  | DROP: below break-even |
| pin_value | both | 93-81 | 53.4 | 49.6 | 3.8 | +16.72 | 9.6 |  |  | no edge shown yet |
| consensus_gap | both | 89-58 | 60.5 | 53.5 | 7.0 | +12.44 | 8.5 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+pin_move | both | 73-117 | 38.4 | 49.2 | -10.7 | -47.76 | -25.1 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 48-55 | 46.6 | 42.5 | 4.1 | -1.58 | -1.5 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 48-54 | 47.1 | 42.5 | 4.6 | -0.58 | -0.6 |  |  | no edge shown yet |
| money_moving+sharp_gap | both | 180-208 | 46.4 | 48.4 | -2.0 | -38.05 | -9.8 |  |  | DROP: below break-even |
| consensus_gap+money_level | both | 61-32 | 65.6 | 59.4 | 6.2 | +3.93 | 4.2 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+rlm_quiet | both | 63-116 | 35.2 | 42.7 | -7.5 | -35.67 | -19.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | both | 30-61 | 33.0 | 44.2 | -11.2 | -26.79 | -29.4 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 25-22 | 53.2 | 52.0 | 1.2 | -2.45 | -5.2 |  |  | no edge shown yet |
| follow_move+money_level | both | 85-76 | 52.8 | 56.3 | -3.5 | -14.87 | -9.2 |  |  | no edge shown yet |
| money_level+money_moving | both | 128-112 | 53.3 | 53.5 | -0.1 | -11.22 | -4.7 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 121-110 | 52.4 | 53.0 | -0.6 | -11.68 | -5.1 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 31-30 | 50.8 | 51.7 | -0.9 | -0.78 | -1.3 |  |  | no edge shown yet |
| consensus_gap+pin_move | both | 22-12 | 64.7 | 50.5 | 14.3 | +8.64 | 25.4 |  |  | no edge shown yet |
| consensus_gap+pin_value | both | 32-19 | 62.7 | 49.0 | 13.7 | +12.87 | 25.2 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | both | 32-30 | 51.6 | 51.1 | 0.5 | -0.47 | -0.8 |  |  | no edge shown yet |
| follow_move+money_moving | both | 87-117 | 42.6 | 48.5 | -5.8 | -37.74 | -18.5 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 28-26 | 51.9 | 50.7 | 1.2 | +8.79 | 16.3 |  |  | no edge shown yet |
| follow_move+sharp_gap | both | 89-121 | 42.4 | 48.0 | -5.6 | -38.09 | -18.1 |  |  | DROP: below break-even |
| money_level+pin_move | both | 48-48 | 50.0 | 54.4 | -4.4 | -10.39 | -10.8 |  |  | no edge shown yet |
| money_level+pin_value | both | 39-33 | 54.2 | 50.9 | 3.3 | +1.17 | 1.6 |  |  | no edge shown yet |
| money_moving+pin_move | both | 43-63 | 40.6 | 47.8 | -7.2 | -21.14 | -19.9 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 32-37 | 46.4 | 49.6 | -3.2 | -5.06 | -7.3 |  |  | no edge shown yet |
| pin_move+pin_value | both | 35-32 | 52.2 | 50.7 | 1.6 | -0.91 | -1.4 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 41-67 | 38.0 | 47.3 | -9.3 | -26.91 | -24.9 |  |  | DROP: below break-even |
| pin_value+sharp_gap | both | 31-36 | 46.3 | 49.4 | -3.2 | -4.97 | -7.4 |  |  | no edge shown yet |
| follow_move+money_delta | both | 34-51 | 40.0 | 44.7 | -4.7 | -17.35 | -20.4 |  |  | DROP: below break-even |
| money_delta+pin_move | both | 17-26 | 39.5 | 44.1 | -4.6 | -9.7 | -22.6 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 20-38 | 34.5 | 42.9 | -8.4 | -17.44 | -30.1 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | both | 38-70 | 35.2 | 41.5 | -6.3 | -26.95 | -25.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | both | 25-58 | 30.1 | 41.0 | -10.9 | -28.23 | -34.0 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 37-66 | 35.9 | 41.8 | -5.9 | -24.67 | -23.9 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 20-54 | 27.0 | 39.7 | -12.7 | -28.57 | -38.6 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | both | 26-63 | 29.2 | 40.6 | -11.4 | -31.51 | -35.4 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 38-70 | 35.2 | 41.5 | -6.3 | -26.95 | -25.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | both | 15-9 | 62.5 | 48.2 | 14.3 | +6.34 | 26.4 |  |  | keep collecting (24/30) |
| consensus_gap+rlm_quiet | both | 6-13 | 31.6 | 39.3 | -7.7 | -5.96 | -31.4 |  |  | keep collecting (19/30) |
| consensus_gap+rlm_ratio | both | 5-8 | 38.5 | 39.5 | -1.0 | -1.95 | -15.0 |  |  | keep collecting (13/30) |
| money_delta+rlm_ratio | both | 23-36 | 39.0 | 42.2 | -3.2 | -12.4 | -21.0 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 2-6 | 25.0 | 43.3 | -18.3 | -2.6 | -32.5 |  |  | keep collecting (8/30) |
| money_level+pin_rlm | both | 7-4 | 63.6 | 47.0 | 16.6 | +2.75 | 25.0 |  |  | keep collecting (11/30) |
| money_moving+pin_rlm | both | 18-35 | 34.0 | 41.7 | -7.7 | -13.28 | -25.1 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 18-39 | 31.6 | 41.3 | -9.7 | -17.28 | -30.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | both | 14-12 | 53.8 | 47.4 | 6.4 | +1.17 | 4.5 |  |  | keep collecting (26/30) |
| consensus_gap+money_delta | both | 10-5 | 66.7 | 43.9 | 22.8 | +7.63 | 50.9 |  |  | keep collecting (15/30) |
| follow_move+pin_rlm | both | 16-35 | 31.4 | 40.9 | -9.5 | -15.51 | -30.4 |  |  | DROP: below break-even |
| money_delta+pin_rlm | both | 10-19 | 34.5 | 40.6 | -6.2 | -9.13 | -31.5 |  |  | keep collecting (29/30) |
| pin_move+pin_rlm | both | 17-34 | 33.3 | 41.6 | -8.3 | -13.62 | -26.7 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | both | 16-33 | 32.7 | 42.1 | -9.4 | -14.0 | -28.6 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 8-30 | 21.1 | 40.1 | -19.0 | -18.6 | -48.9 |  |  | INVERT candidate: wrong well beyond its base rate |
| pin_rlm+rlm_ratio | both | 16-35 | 31.4 | 40.9 | -9.5 | -15.51 | -30.4 |  |  | DROP: below break-even |
| money_delta+pin_value | both | 14-6 | 70.0 | 47.9 | 22.1 | +10.26 | 51.3 |  |  | keep collecting (20/30) |
| pin_value+rlm_quiet | both | 9-13 | 40.9 | 47.8 | -6.9 | +4.96 | 22.5 |  |  | keep collecting (22/30) |
| pin_value+rlm_ratio | both | 5-4 | 55.6 | 49.4 | 6.2 | +0.4 | 4.5 |  |  | keep collecting (9/30) |
| pin_rlm+pin_value | both | 3-5 | 37.5 | 49.0 | -11.5 | -2.31 | -28.9 |  |  | keep collecting (8/30) |
| rlm_quiet | moneyline | 21-53 | 28.4 | 33.4 | -5.0 | -11.99 | -16.2 |  |  | DROP: below break-even |
| rlm_quiet | spread | 14-17 | 45.2 | 53.4 | -8.2 | -3.81 | -12.3 |  |  | no edge shown yet |
| rlm_quiet | total | 28-46 | 37.8 | 47.5 | -9.6 | -19.86 | -26.8 |  |  | DROP: below break-even |
| pin_move | moneyline | 32-33 | 49.2 | 46.1 | 3.2 | -0.67 | -1.0 |  |  | no edge shown yet |
| pin_move | spread | 38-40 | 48.7 | 51.7 | -3.0 | -5.6 | -7.2 |  |  | no edge shown yet |
| pin_move | total | 37-62 | 37.4 | 49.7 | -12.3 | -28.12 | -28.4 |  |  | DROP: below break-even |
| money_delta | moneyline | 18-30 | 37.5 | 35.8 | 1.7 | -4.26 | -8.9 |  |  | DROP: below break-even |
| money_delta | spread | 9-10 | 47.4 | 50.8 | -3.4 | -1.71 | -9.0 |  |  | keep collecting (19/30) |
| money_delta | total | 36-33 | 52.2 | 47.6 | 4.6 | +0.27 | 0.4 |  |  | no edge shown yet |
| pin_rlm | moneyline | 8-20 | 28.6 | 34.1 | -5.6 | -7.5 | -26.8 |  |  | keep collecting (28/30) |
| pin_rlm | spread | 1-1 | 50.0 | 55.0 | -5.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| pin_rlm | total | 9-18 | 33.3 | 47.7 | -14.4 | -9.69 | -35.9 |  |  | keep collecting (27/30) |
| follow_move | moneyline | 69-77 | 47.3 | 47.4 | -0.2 | -8.42 | -5.8 |  |  | no edge shown yet |
| follow_move | spread | 51-57 | 47.2 | 51.6 | -4.4 | -9.93 | -9.2 |  |  | no edge shown yet |
| follow_move | total | 62-92 | 40.3 | 49.4 | -9.2 | -34.96 | -22.7 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 15-37 | 28.8 | 33.6 | -4.7 | -15.07 | -29.0 |  |  | DROP: below break-even |
| rlm_ratio | spread | 3-4 | 42.9 | 53.6 | -10.7 | -1.3 | -18.6 |  |  | keep collecting (7/30) |
| rlm_ratio | total | 20-29 | 40.8 | 48.2 | -7.4 | -10.57 | -21.6 |  |  | DROP: below break-even |
| money_level | moneyline | 104-51 | 67.1 | 64.0 | 3.1 | -3.46 | -2.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 55-53 | 50.9 | 49.3 | 1.6 | -3.59 | -3.3 |  |  | no edge shown yet |
| money_level | total | 86-82 | 51.2 | 51.9 | -0.7 | -4.51 | -2.7 |  |  | no edge shown yet |
| sharp_gap | moneyline | 64-78 | 45.1 | 44.9 | 0.1 | -13.99 | -9.9 |  |  | DROP: below break-even |
| sharp_gap | spread | 50-58 | 46.3 | 49.4 | -3.1 | -12.83 | -11.9 |  |  | no edge shown yet |
| sharp_gap | total | 71-82 | 46.4 | 50.1 | -3.6 | -17.2 | -11.2 |  |  | no edge shown yet |
| money_moving | moneyline | 69-71 | 49.3 | 46.8 | 2.5 | -7.09 | -5.1 |  |  | no edge shown yet |
| money_moving | spread | 50-58 | 46.3 | 49.4 | -3.1 | -12.83 | -11.9 |  |  | no edge shown yet |
| money_moving | total | 73-85 | 46.2 | 50.1 | -3.9 | -18.45 | -11.7 |  |  | DROP: below break-even |
| pin_value | moneyline | 5-4 | 55.6 | 40.5 | 15.1 | +16.16 | 179.6 |  |  | keep collecting (9/30) |
| pin_value | spread | 41-38 | 51.9 | 49.7 | 2.2 | -2.7 | -3.4 |  |  | no edge shown yet |
| pin_value | total | 47-39 | 54.7 | 50.5 | 4.2 | +3.25 | 3.8 |  |  | no edge shown yet |
| consensus_gap | moneyline | 48-32 | 60.0 | 56.4 | 3.6 | +2.48 | 3.1 |  |  | no edge shown yet |
| consensus_gap | spread | 17-10 | 63.0 | 48.7 | 14.3 | +4.59 | 17.0 |  |  | keep collecting (27/30) |
| consensus_gap | total | 24-16 | 60.0 | 51.1 | 8.9 | +5.37 | 13.4 |  |  | no edge shown yet |
| consensus_gap+money_level | moneyline | 39-14 | 73.6 | 65.8 | 7.8 | +2.66 | 5.0 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+pin_move | moneyline | 23-31 | 42.6 | 45.6 | -3.0 | -7.76 | -14.4 |  |  | no edge shown yet |
| follow_move+rlm_quiet | moneyline | 21-53 | 28.4 | 33.4 | -5.0 | -11.99 | -16.2 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | moneyline | 9-23 | 28.1 | 34.0 | -5.8 | -8.53 | -26.7 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 15-13 | 53.6 | 52.4 | 1.1 | -2.34 | -8.4 |  |  | keep collecting (28/30) |
| follow_move+money_level | moneyline | 40-20 | 66.7 | 64.2 | 2.4 | +0.06 | 0.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 61-69 | 46.9 | 45.5 | 1.4 | -7.17 | -5.5 |  |  | no edge shown yet |
| follow_move+money_moving | moneyline | 37-42 | 46.8 | 45.5 | 1.4 | -8.48 | -10.7 |  |  | no edge shown yet |
| follow_move+sharp_gap | moneyline | 37-46 | 44.6 | 44.4 | 0.1 | -10.69 | -12.9 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 46-23 | 66.7 | 60.7 | 6.0 | +3.74 | 5.4 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+sharp_gap | moneyline | 40-22 | 64.5 | 59.9 | 4.6 | +3.12 | 5.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+rlm_ratio | moneyline | 15-37 | 28.8 | 33.6 | -4.7 | -15.07 | -29.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | moneyline | 10-30 | 25.0 | 32.9 | -7.9 | -14.08 | -35.2 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 14-34 | 29.2 | 33.6 | -4.4 | -13.79 | -28.7 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | moneyline | 9-32 | 22.0 | 32.9 | -11.0 | -16.74 | -40.8 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 11-34 | 24.4 | 32.9 | -8.5 | -16.36 | -36.4 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 15-37 | 28.8 | 33.6 | -4.7 | -15.07 | -29.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 17-15 | 53.1 | 53.2 | -0.1 | +1.84 | 5.7 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | moneyline | 2-10 | 16.7 | 32.9 | -16.2 | -6.6 | -55.0 |  |  | keep collecting (12/30) |
| consensus_gap+rlm_ratio | moneyline | 2-6 | 25.0 | 32.9 | -7.9 | -2.6 | -32.5 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | moneyline | 18-16 | 52.9 | 52.0 | 0.9 | +1.15 | 3.4 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 2-3 | 40.0 | 39.7 | 0.3 | +0.4 | 8.0 |  |  | keep collecting (5/30) |
| money_level+pin_rlm | moneyline | 2-1 | 66.7 | 44.3 | 22.4 | +1.16 | 38.7 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | moneyline | 8-17 | 32.0 | 34.3 | -2.3 | -4.5 | -18.0 |  |  | keep collecting (25/30) |
| pin_rlm+sharp_gap | moneyline | 8-20 | 28.6 | 34.1 | -5.6 | -7.5 | -26.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 3-2 | 60.0 | 39.7 | 20.3 | +4.46 | 89.3 |  |  | keep collecting (5/30) |
| money_level+rlm_ratio | moneyline | 3-3 | 50.0 | 38.6 | 11.4 | +0.09 | 1.4 |  |  | keep collecting (6/30) |
| consensus_gap+pin_move | moneyline | 13-5 | 72.2 | 50.0 | 22.2 | +7.83 | 43.5 |  |  | keep collecting (18/30) |
| money_level+pin_move | moneyline | 17-6 | 73.9 | 64.1 | 9.8 | +3.87 | 16.8 |  |  | keep collecting (23/30) |
| consensus_gap+money_delta | moneyline | 3-4 | 42.9 | 37.8 | 5.1 | +2.35 | 33.5 |  |  | keep collecting (7/30) |
| follow_move+money_delta | moneyline | 10-20 | 33.3 | 37.5 | -4.1 | -8.51 | -28.4 |  |  | DROP: below break-even |
| follow_move+pin_rlm | moneyline | 7-17 | 29.2 | 32.9 | -3.7 | -5.82 | -24.2 |  |  | keep collecting (24/30) |
| money_delta+money_moving | moneyline | 17-28 | 37.8 | 35.2 | 2.6 | -3.11 | -6.9 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 4-8 | 33.3 | 32.9 | 0.4 | -3.76 | -31.3 |  |  | keep collecting (12/30) |
| money_delta+pin_rlm | moneyline | 4-10 | 28.6 | 32.9 | -4.3 | -5.76 | -41.1 |  |  | keep collecting (14/30) |
| money_delta+rlm_quiet | moneyline | 4-17 | 19.0 | 32.9 | -13.9 | -11.31 | -53.9 |  |  | keep collecting (21/30) |
| money_delta+rlm_ratio | moneyline | 7-19 | 26.9 | 34.2 | -7.3 | -10.09 | -38.8 |  |  | keep collecting (26/30) |
| money_delta+sharp_gap | moneyline | 17-28 | 37.8 | 35.2 | 2.6 | -3.11 | -6.9 |  |  | DROP: below break-even |
| money_moving+pin_move | moneyline | 12-13 | 48.0 | 39.7 | 8.3 | +0.95 | 3.8 |  |  | keep collecting (25/30) |
| pin_move+pin_rlm | moneyline | 7-15 | 31.8 | 32.9 | -1.1 | -3.84 | -17.5 |  |  | keep collecting (22/30) |
| pin_move+rlm_ratio | moneyline | 6-14 | 30.0 | 32.9 | -2.9 | -4.16 | -20.8 |  |  | keep collecting (20/30) |
| pin_move+sharp_gap | moneyline | 12-16 | 42.9 | 39.0 | 3.8 | -2.05 | -7.3 |  |  | keep collecting (28/30) |
| pin_rlm+rlm_quiet | moneyline | 4-16 | 20.0 | 32.9 | -12.9 | -8.32 | -41.6 |  |  | keep collecting (20/30) |
| pin_rlm+rlm_ratio | moneyline | 7-17 | 29.2 | 32.9 | -3.7 | -5.82 | -24.2 |  |  | keep collecting (24/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 44.3 | -11.0 | +8.6 | 286.7 |  |  | keep collecting (3/30) |
| pin_value+rlm_quiet | moneyline | 1-1 | 50.0 | 32.9 | 17.1 | +9.6 | 480.0 |  |  | keep collecting (2/30) |
| money_delta+money_level | moneyline | 6-1 | 85.7 | 47.6 | 38.2 | +6.07 | 86.8 |  |  | keep collecting (7/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_move+pin_value | moneyline | 1-2 | 33.3 | 44.3 | -11.0 | -0.92 | -30.7 |  |  | keep collecting (3/30) |
| money_delta+pin_value | moneyline | 1-0 | 100.0 | 32.9 | 67.1 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 1-1 | 50.0 | 32.9 | 17.1 | +3.5 | 175.0 |  |  | keep collecting (2/30) |
| pin_value+sharp_gap | moneyline | 1-1 | 50.0 | 32.9 | 17.1 | +3.5 | 175.0 |  |  | keep collecting (2/30) |
| follow_move+pin_move | spread | 22-33 | 40.0 | 52.1 | -12.1 | -12.8 | -23.3 |  |  | DROP: below break-even |
| money_moving+sharp_gap | spread | 50-58 | 46.3 | 49.4 | -3.1 | -12.83 | -11.9 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 14-17 | 45.2 | 53.4 | -8.2 | -3.81 | -12.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | spread | 36-39 | 48.0 | 49.1 | -1.1 | -6.57 | -8.8 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 36-39 | 48.0 | 49.1 | -1.1 | -6.57 | -8.8 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 7-14 | 33.3 | 53.6 | -20.3 | -7.37 | -35.1 |  |  | keep collecting (21/30) |
| consensus_gap+pin_value | spread | 14-8 | 63.6 | 49.1 | 14.6 | +4.08 | 18.6 |  |  | keep collecting (22/30) |
| follow_move+money_level | spread | 15-14 | 51.7 | 52.3 | -0.5 | -0.23 | -0.8 |  |  | keep collecting (29/30) |
| follow_move+money_moving | spread | 15-18 | 45.5 | 52.3 | -6.8 | -4.32 | -13.1 |  |  | no edge shown yet |
| follow_move+sharp_gap | spread | 15-18 | 45.5 | 52.3 | -6.8 | -4.32 | -13.1 |  |  | no edge shown yet |
| money_level+pin_move | spread | 11-12 | 47.8 | 51.1 | -3.3 | -2.3 | -10.0 |  |  | keep collecting (23/30) |
| money_moving+pin_move | spread | 11-14 | 44.0 | 51.0 | -7.0 | -4.28 | -17.1 |  |  | keep collecting (25/30) |
| pin_move+sharp_gap | spread | 11-14 | 44.0 | 51.0 | -7.0 | -4.28 | -17.1 |  |  | keep collecting (25/30) |
| money_delta+money_level | spread | 3-2 | 60.0 | 49.0 | 11.0 | +0.7 | 14.0 |  |  | keep collecting (5/30) |
| money_delta+money_moving | spread | 6-8 | 42.9 | 50.0 | -7.1 | -2.57 | -18.4 |  |  | keep collecting (14/30) |
| money_delta+sharp_gap | spread | 6-8 | 42.9 | 50.0 | -7.1 | -2.57 | -18.4 |  |  | keep collecting (14/30) |
| consensus_gap+money_level | spread | 5-7 | 41.7 | 47.5 | -5.8 | -2.73 | -22.8 |  |  | keep collecting (12/30) |
| consensus_gap+money_moving | spread | 4-5 | 44.4 | 48.3 | -3.9 | -1.53 | -17.0 |  |  | keep collecting (9/30) |
| consensus_gap+sharp_gap | spread | 4-5 | 44.4 | 48.3 | -3.9 | -1.53 | -17.0 |  |  | keep collecting (9/30) |
| money_level+pin_value | spread | 15-14 | 51.7 | 48.4 | 3.3 | -1.21 | -4.2 |  |  | keep collecting (29/30) |
| money_moving+pin_value | spread | 13-18 | 41.9 | 49.5 | -7.6 | -6.77 | -21.8 |  |  | no edge shown yet |
| pin_value+sharp_gap | spread | 13-18 | 41.9 | 49.5 | -7.6 | -6.77 | -21.8 |  |  | no edge shown yet |
| follow_move+money_delta | spread | 4-5 | 44.4 | 53.9 | -9.5 | -1.35 | -15.1 |  |  | keep collecting (9/30) |
| follow_move+rlm_ratio | spread | 3-4 | 42.9 | 53.6 | -10.7 | -1.3 | -18.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | spread | 1-3 | 25.0 | 52.5 | -27.5 | -2.15 | -53.8 |  |  | keep collecting (4/30) |
| money_moving+rlm_ratio | spread | 3-4 | 42.9 | 53.6 | -10.7 | -1.3 | -18.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 3-4 | 42.9 | 53.6 | -10.7 | -1.3 | -18.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 10-8 | 55.6 | 52.8 | 2.8 | +0.85 | 4.7 |  |  | keep collecting (18/30) |
| pin_move+pin_value | spread | 19-11 | 63.3 | 51.7 | 11.7 | +5.52 | 18.4 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 6-2 | 75.0 | 51.3 | 23.7 | +3.16 | 39.5 |  |  | keep collecting (8/30) |
| consensus_gap+follow_move | spread | 3-2 | 60.0 | 53.0 | 7.0 | +0.67 | 13.3 |  |  | keep collecting (5/30) |
| consensus_gap+rlm_quiet | spread | 2-0 | 100.0 | 55.0 | 45.0 | +1.82 | 90.9 |  |  | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 2-3 | 40.0 | 55.0 | -15.0 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| money_delta+rlm_quiet | spread | 3-3 | 50.0 | 55.0 | -5.0 | -0.2 | -3.4 |  |  | keep collecting (6/30) |
| money_moving+rlm_quiet | spread | 2-5 | 28.6 | 53.6 | -25.0 | -3.22 | -46.0 |  |  | keep collecting (7/30) |
| rlm_quiet+rlm_ratio | spread | 1-2 | 33.3 | 55.0 | -21.7 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| rlm_quiet+sharp_gap | spread | 2-5 | 28.6 | 53.6 | -25.0 | -3.22 | -46.0 |  |  | keep collecting (7/30) |
| consensus_gap+money_delta | spread | 2-0 | 100.0 | 55.0 | 45.0 | +1.76 | 87.8 |  |  | keep collecting (2/30) |
| money_delta+pin_move | spread | 3-3 | 50.0 | 53.4 | -3.4 | -0.33 | -5.6 |  |  | keep collecting (6/30) |
| money_delta+pin_value | spread | 2-2 | 50.0 | 52.5 | -2.5 | -0.24 | -6.1 |  |  | keep collecting (4/30) |
| money_moving+pin_rlm | spread | 1-1 | 50.0 | 55.0 | -5.0 | -0.09 | -4.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | spread | 1-1 | 50.0 | 55.0 | -5.0 | -0.09 | -4.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | spread | 1-0 | 100.0 | 55.0 | 45.0 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| pin_rlm+sharp_gap | spread | 1-1 | 50.0 | 55.0 | -5.0 | -0.09 | -4.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+rlm_ratio | spread | 1-0 | 100.0 | 55.0 | 45.0 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 55.0 | 11.6 | +0.83 | 27.6 |  |  | keep collecting (3/30) |
| pin_move+rlm_ratio | spread | 1-1 | 50.0 | 55.0 | -5.0 | -0.15 | -7.7 |  |  | keep collecting (2/30) |
| pin_value+rlm_ratio | spread | 1-0 | 100.0 | 55.0 | 45.0 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| follow_move+pin_rlm | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta+pin_rlm | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+rlm_quiet | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+rlm_ratio | spread | 0-1 | 0.0 | 55.0 | -55.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta+money_moving | total | 25-19 | 56.8 | 47.7 | 9.1 | +4.1 | 9.3 |  |  | no edge shown yet |
| money_delta+sharp_gap | total | 25-18 | 58.1 | 47.7 | 10.4 | +5.1 | 11.9 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 69-81 | 46.0 | 50.1 | -4.1 | -18.05 | -12.0 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | total | 28-46 | 37.8 | 47.5 | -9.6 | -19.86 | -26.8 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+follow_move | total | 7-7 | 50.0 | 50.8 | -0.8 | -0.77 | -5.5 |  |  | keep collecting (14/30) |
| consensus_gap+money_level | total | 17-11 | 60.7 | 52.5 | 8.2 | +4.01 | 14.3 |  |  | keep collecting (28/30) |
| consensus_gap+money_moving | total | 10-10 | 50.0 | 50.8 | -0.8 | -1.08 | -5.4 |  |  | keep collecting (20/30) |
| consensus_gap+pin_move | total | 3-5 | 37.5 | 50.7 | -13.2 | -2.35 | -29.4 |  |  | keep collecting (8/30) |
| consensus_gap+pin_value | total | 15-9 | 62.5 | 50.9 | 11.6 | +4.32 | 18.0 |  |  | keep collecting (24/30) |
| consensus_gap+sharp_gap | total | 10-9 | 52.6 | 50.7 | 1.9 | -0.08 | -0.4 |  |  | keep collecting (19/30) |
| follow_move+money_level | total | 30-42 | 41.7 | 51.4 | -9.7 | -14.7 | -20.4 |  |  | DROP: below break-even |
| follow_move+money_moving | total | 35-57 | 38.0 | 49.7 | -11.6 | -24.93 | -27.1 |  |  | DROP: below break-even |
| follow_move+pin_move | total | 28-53 | 34.6 | 49.6 | -15.0 | -27.19 | -33.6 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | total | 17-16 | 51.5 | 50.1 | 1.4 | -0.65 | -2.0 |  |  | no edge shown yet |
| follow_move+sharp_gap | total | 37-57 | 39.4 | 49.6 | -10.2 | -23.08 | -24.6 |  |  | DROP: below break-even |
| money_level+money_moving | total | 46-50 | 47.9 | 51.7 | -3.7 | -8.39 | -8.7 |  |  | no edge shown yet |
| money_level+pin_move | total | 20-30 | 40.0 | 51.5 | -11.5 | -11.97 | -23.9 |  |  | DROP: below break-even |
| money_level+pin_value | total | 24-18 | 57.1 | 52.2 | 5.0 | +3.39 | 8.1 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 45-49 | 47.9 | 51.6 | -3.7 | -8.23 | -8.8 |  |  | no edge shown yet |
| money_moving+pin_move | total | 20-36 | 35.7 | 49.9 | -14.2 | -17.81 | -31.8 |  |  | DROP: below break-even |
| money_moving+pin_value | total | 18-18 | 50.0 | 50.6 | -0.6 | -1.79 | -5.0 |  |  | no edge shown yet |
| pin_move+pin_value | total | 15-19 | 44.1 | 50.3 | -6.2 | -5.51 | -16.2 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 18-37 | 32.7 | 49.8 | -17.0 | -20.58 | -37.4 |  |  | INVERT candidate: wrong well beyond its base rate |
| pin_value+sharp_gap | total | 17-17 | 50.0 | 50.3 | -0.3 | -1.7 | -5.0 |  |  | no edge shown yet |
| follow_move+money_delta | total | 20-26 | 43.5 | 47.7 | -4.2 | -7.49 | -16.3 |  |  | no edge shown yet |
| money_delta+pin_move | total | 10-15 | 40.0 | 47.3 | -7.3 | -5.61 | -22.4 |  |  | keep collecting (25/30) |
| money_delta+rlm_quiet | total | 13-18 | 41.9 | 47.3 | -5.4 | -5.93 | -19.1 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 14-24 | 36.8 | 47.6 | -10.8 | -10.89 | -28.7 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | total | 20-29 | 40.8 | 48.2 | -7.4 | -10.57 | -21.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | total | 15-14 | 51.7 | 47.9 | 3.8 | -0.16 | -0.6 |  |  | keep collecting (29/30) |
| money_moving+rlm_quiet | total | 13-23 | 36.1 | 47.5 | -11.4 | -10.93 | -30.3 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | total | 20-28 | 41.7 | 48.2 | -6.6 | -9.57 | -19.9 |  |  | no edge shown yet |
| rlm_quiet+rlm_ratio | total | 10-20 | 33.3 | 47.5 | -14.2 | -10.7 | -35.7 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | total | 13-24 | 35.1 | 47.5 | -12.3 | -11.93 | -32.2 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | total | 20-29 | 40.8 | 48.2 | -7.4 | -10.57 | -21.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | total | 5-1 | 83.3 | 47.3 | 36.0 | +3.53 | 58.8 |  |  | keep collecting (6/30) |
| consensus_gap+rlm_quiet | total | 2-3 | 40.0 | 48.4 | -8.4 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| consensus_gap+rlm_ratio | total | 2-2 | 50.0 | 48.7 | 1.3 | -0.2 | -4.9 |  |  | keep collecting (4/30) |
| money_delta+pin_value | total | 11-4 | 73.3 | 47.7 | 25.6 | +6.0 | 40.0 |  |  | keep collecting (15/30) |
| pin_value+rlm_quiet | total | 6-9 | 40.0 | 47.3 | -7.3 | -3.46 | -23.1 |  |  | keep collecting (15/30) |
| pin_value+rlm_ratio | total | 4-4 | 50.0 | 48.7 | 1.3 | -0.44 | -5.5 |  |  | keep collecting (8/30) |
| follow_move+pin_rlm | total | 9-17 | 34.6 | 47.7 | -13.1 | -8.69 | -33.4 |  |  | keep collecting (26/30) |
| money_delta+money_level | total | 6-6 | 50.0 | 48.2 | 1.8 | -0.43 | -3.6 |  |  | keep collecting (12/30) |
| money_delta+pin_rlm | total | 6-8 | 42.9 | 47.3 | -4.5 | -2.37 | -17.0 |  |  | keep collecting (14/30) |
| money_level+pin_rlm | total | 5-3 | 62.5 | 48.0 | 14.5 | +1.59 | 19.9 |  |  | keep collecting (8/30) |
| money_level+rlm_ratio | total | 9-8 | 52.9 | 49.2 | 3.7 | +0.25 | 1.5 |  |  | keep collecting (17/30) |
| money_moving+pin_rlm | total | 9-17 | 34.6 | 47.7 | -13.1 | -8.69 | -33.4 |  |  | keep collecting (26/30) |
| pin_move+pin_rlm | total | 9-18 | 33.3 | 47.7 | -14.4 | -9.69 | -35.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 9-18 | 33.3 | 47.9 | -14.6 | -9.69 | -35.9 |  |  | keep collecting (27/30) |
| pin_rlm+rlm_ratio | total | 9-17 | 34.6 | 47.7 | -13.1 | -8.69 | -33.4 |  |  | keep collecting (26/30) |
| pin_rlm+sharp_gap | total | 9-18 | 33.3 | 47.7 | -14.4 | -9.69 | -35.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | total | 4-13 | 23.5 | 47.7 | -24.1 | -9.28 | -54.6 |  |  | keep collecting (17/30) |
| consensus_gap+pin_rlm | total | 0-3 | 0.0 | 49.1 | -49.1 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_rlm+pin_value | total | 2-5 | 28.6 | 48.1 | -19.5 | -3.22 | -46.0 |  |  | keep collecting (7/30) |

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
| rlm_quiet | both | 42-56 | 42.9 | 36.8 | 6.0 | +7.6 | 7.8 | 0.52 | 46.9 | DROP: below break-even |
| pin_move | both | 9-15 | 37.5 | 48.8 | -11.3 | -7.46 | -31.1 | 0.25 | 41.7 | keep collecting (24/30) |
| money_delta | both | 14-10 | 58.3 | 40.7 | 17.6 | +7.9 | 32.9 | 0.74 | 50.0 | keep collecting (24/30) |
| pin_rlm | both | 1-3 | 25.0 | 39.0 | -14.0 | -2.07 | -51.8 | -0.37 | 75.0 | keep collecting (4/30) |
| follow_move | both | 590-538 | 52.3 | 51.4 | 0.9 | -73.34 | -6.5 | 0.18 | 41.3 | no edge shown yet |
| rlm_ratio | both | 36-28 | 56.2 | 39.7 | 16.5 | +19.58 | 30.6 | 0.61 | 54.7 | no edge shown yet |
| money_level | both | 210-142 | 59.7 | 58.8 | 0.8 | -19.77 | -5.6 | -0.18 | 38.9 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 172-157 | 52.3 | 48.1 | 4.2 | +12.86 | 3.9 | 0.35 | 45.6 | no edge shown yet |
| money_moving | both | 128-109 | 54.0 | 50.2 | 3.8 | -2.52 | -1.1 | 0.14 | 43.9 | no edge shown yet |
| pin_value | both | 61-61 | 50.0 | 48.7 | 1.3 | -6.87 | -5.6 | 0.07 | 36.9 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.6 | -31.6 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 296-345 | 46.2 | 48.5 | -2.4 | -55.96 | -8.7 | 0.39 | 45.7 | DROP: below break-even |
| consensus_gap+money_level | both | 45-37 | 54.9 | 62.6 | -7.7 | -12.49 | -15.2 | 0.11 | 45.1 | no edge shown yet |
| consensus_gap+money_moving | both | 21-26 | 44.7 | 47.3 | -2.6 | -7.26 | -15.4 | 0.32 | 44.7 | no edge shown yet |
| consensus_gap+pin_value | both | 25-29 | 46.3 | 47.0 | -0.7 | -7.24 | -13.4 | 0.34 | 46.3 | no edge shown yet |
| follow_move+rlm_quiet | both | 42-56 | 42.9 | 36.8 | 6.0 | +7.6 | 7.8 | 0.52 | 46.9 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 36-28 | 56.2 | 39.7 | 16.5 | +19.58 | 30.6 | 0.61 | 54.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 88-54 | 62.0 | 49.4 | 12.6 | +22.52 | 15.9 | 0.55 | 50.0 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 77-50 | 60.6 | 57.3 | 3.3 | -1.51 | -1.2 | -0.1 | 45.7 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 13-11 | 54.2 | 50.5 | 3.6 | +0.63 | 2.6 | 0.57 | 50.0 | keep collecting (24/30) |
| money_moving+pin_value | both | 10-7 | 58.8 | 50.9 | 7.9 | +1.78 | 10.5 | 0.39 | 41.2 | keep collecting (17/30) |
| rlm_quiet+rlm_ratio | both | 22-18 | 55.0 | 36.7 | 18.3 | +15.38 | 38.5 | 0.21 | 50.0 | no edge shown yet |
| rlm_quiet+sharp_gap | both | 24-22 | 52.2 | 37.0 | 15.2 | +13.2 | 28.7 | 0.16 | 47.8 | no edge shown yet |
| rlm_ratio+sharp_gap | both | 36-28 | 56.2 | 39.7 | 16.5 | +19.58 | 30.6 | 0.61 | 54.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 114-78 | 59.4 | 55.3 | 4.1 | -1.31 | -0.7 | 0.12 | 44.8 | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | both | 77-66 | 53.8 | 47.6 | 6.3 | +6.56 | 4.6 | 0.37 | 48.3 | no edge shown yet |
| money_delta+money_level | both | 4-4 | 50.0 | 44.7 | 5.3 | +0.37 | 4.6 | 1.38 | 75.0 | keep collecting (8/30) |
| money_delta+money_moving | both | 13-10 | 56.5 | 40.3 | 16.2 | +6.99 | 30.4 | 0.77 | 52.2 | keep collecting (23/30) |
| money_delta+pin_value | both | 4-1 | 80.0 | 49.9 | 30.1 | +2.52 | 50.4 | 0.2 | 40.0 | keep collecting (5/30) |
| money_delta+sharp_gap | both | 11-8 | 57.9 | 39.6 | 18.3 | +7.25 | 38.2 | 0.93 | 63.2 | keep collecting (19/30) |
| pin_value+sharp_gap | both | 14-10 | 58.3 | 49.9 | 8.5 | +2.57 | 10.7 | 0.08 | 41.7 | keep collecting (24/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 50.3 | -50.3 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 41-46 | 47.1 | 51.8 | -4.7 | -14.2 | -16.3 | 0.71 | 56.3 | no edge shown yet |
| consensus_gap+rlm_quiet | both | 4-7 | 36.4 | 37.6 | -1.3 | -2.99 | -27.1 | 0.95 | 72.7 | keep collecting (11/30) |
| follow_move+pin_value | both | 23-21 | 52.3 | 48.8 | 3.4 | -0.86 | -2.0 | -0.21 | 27.3 | no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 42.7 | -26.0 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 33-50 | 39.8 | 46.0 | -6.3 | -10.58 | -12.7 | 0.75 | 49.4 | DROP: below break-even |
| follow_move+money_level | both | 105-54 | 66.0 | 60.0 | 6.1 | -2.45 | -1.5 | 0.08 | 43.4 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 12-10 | 54.5 | 44.4 | 10.2 | +2.34 | 10.6 | 1.43 | 68.2 | keep collecting (22/30) |
| pin_value+rlm_ratio | both | 3-2 | 60.0 | 45.5 | 14.5 | +0.73 | 14.5 | -1.16 | 40.0 | keep collecting (5/30) |
| follow_move+money_moving | both | 66-41 | 61.7 | 51.6 | 10.1 | +11.35 | 10.6 | 0.4 | 51.4 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 4-0 | 100.0 | 49.4 | 50.6 | +3.52 | 88.0 | 0.25 | 25.0 | keep collecting (4/30) |
| follow_move+money_delta | both | 8-4 | 66.7 | 40.5 | 26.2 | +8.51 | 70.9 | 0.82 | 58.3 | keep collecting (12/30) |
| money_delta+rlm_quiet | both | 4-2 | 66.7 | 34.8 | 31.9 | +6.18 | 103.0 | -0.33 | 33.3 | keep collecting (6/30) |
| money_moving+rlm_quiet | both | 18-17 | 51.4 | 37.2 | 14.3 | +8.88 | 25.4 | 0.56 | 48.6 | no edge shown yet |
| money_moving+rlm_ratio | both | 19-12 | 61.3 | 40.7 | 20.6 | +12.71 | 41.0 | 0.65 | 54.8 | no edge shown yet |
| consensus_gap+rlm_ratio | both | 5-4 | 55.6 | 40.0 | 15.5 | +1.0 | 11.1 | 0.72 | 66.7 | keep collecting (9/30) |
| pin_move+pin_value | both | 3-9 | 25.0 | 49.2 | -24.2 | -6.27 | -52.3 | 0.33 | 25.0 | keep collecting (12/30) |
| follow_move+pin_move | both | 6-6 | 50.0 | 50.9 | -0.9 | -1.19 | -9.9 | 0.45 | 50.0 | keep collecting (12/30) |
| consensus_gap+pin_move | both | 1-5 | 16.7 | 45.5 | -28.8 | -4.09 | -68.2 | 0.22 | 50.0 | keep collecting (6/30) |
| money_level+pin_move | both | 3-3 | 50.0 | 53.8 | -3.8 | -0.96 | -16.0 | 0.57 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 28.0 | -28.0 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-2 | 33.3 | 42.7 | -9.3 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 28.0 | -28.0 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 28.0 | -28.0 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-2 | 33.3 | 42.7 | -9.3 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+sharp_gap | both | 1-3 | 25.0 | 39.0 | -14.0 | -2.07 | -51.8 | -0.37 | 75.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.2 | -51.2 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 49.7 | -49.7 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-2 | 50.0 | 50.1 | -0.1 | -0.87 | -21.7 | 0.7 | 50.0 | keep collecting (4/30) |
| money_level+pin_rlm | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.07 | -3.7 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 28.0 | 72.0 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 28.0 | 72.0 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 5-2 | 71.4 | 37.3 | 34.2 | +7.9 | 112.8 | 1.71 | 85.7 | keep collecting (7/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 28.0 | -28.0 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 23-35 | 39.7 | 28.0 | 11.7 | +11.35 | 19.6 | 0.48 | 46.6 | DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.5 | 10.5 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 16-19 | 45.7 | 49.8 | -4.1 | -4.41 | -12.6 | 0.77 | 54.3 | no edge shown yet |
| pin_move | moneyline | 2-3 | 40.0 | 45.6 | -5.6 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-6 | 14.3 | 48.8 | -34.6 | -5.09 | -72.7 | 0.29 | 28.6 | keep collecting (7/30) |
| pin_move | total | 6-6 | 50.0 | 50.0 | -0.0 | -0.5 | -4.2 | 0.33 | 41.7 | keep collecting (12/30) |
| money_delta | moneyline | 4-6 | 40.0 | 28.0 | 12.0 | +2.99 | 29.9 | 0.17 | 60.0 | keep collecting (10/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 9-3 | 75.0 | 49.8 | 25.2 | +5.08 | 42.3 | 1.25 | 41.7 | keep collecting (12/30) |
| pin_rlm | moneyline | 1-3 | 25.0 | 39.0 | -14.0 | -2.07 | -51.8 | -0.37 | 75.0 | keep collecting (4/30) |
| follow_move | moneyline | 245-170 | 59.0 | 54.1 | 4.9 | -21.83 | -5.3 | 0.1 | 43.1 | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 155-180 | 46.3 | 49.8 | -3.5 | -37.09 | -11.1 | 0.0 | 33.4 | DROP: below break-even |
| follow_move | total | 190-188 | 50.3 | 50.0 | 0.3 | -14.42 | -3.8 | 0.41 | 46.3 | no edge shown yet |
| rlm_ratio | moneyline | 16-16 | 50.0 | 29.3 | 20.7 | +13.12 | 41.0 | 0.53 | 56.2 | no edge shown yet |
| rlm_ratio | spread | 3-3 | 50.0 | 51.8 | -1.8 | -0.16 | -2.7 | 0.33 | 16.7 | keep collecting (6/30) |
| rlm_ratio | total | 17-9 | 65.4 | 49.8 | 15.6 | +6.62 | 25.5 | 0.77 | 61.5 | keep collecting (26/30) |
| money_level | moneyline | 118-57 | 67.4 | 67.8 | -0.3 | -18.21 | -10.4 | -0.32 | 41.7 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-18 | 48.6 | 49.2 | -0.6 | -2.69 | -7.7 | 1.0 | 51.4 | no edge shown yet |
| money_level | total | 75-67 | 52.8 | 50.2 | 2.7 | +1.13 | 0.8 | -0.3 | 32.4 | no edge shown yet |
| sharp_gap | moneyline | 74-82 | 47.4 | 46.0 | 1.4 | -1.18 | -0.8 | 0.36 | 51.9 | no edge shown yet |
| sharp_gap | spread | 20-15 | 57.1 | 49.8 | 7.4 | +3.0 | 8.6 | 0.77 | 40.0 | no edge shown yet |
| sharp_gap | total | 78-60 | 56.5 | 50.0 | 6.6 | +11.03 | 8.0 | 0.22 | 39.9 | no edge shown yet |
| money_moving | moneyline | 56-57 | 49.6 | 50.6 | -1.0 | -15.86 | -14.0 | 0.05 | 50.4 | no edge shown yet |
| money_moving | spread | 18-6 | 75.0 | 49.1 | 25.9 | +10.18 | 42.4 | 0.5 | 45.8 | keep collecting (24/30) |
| money_moving | total | 54-46 | 54.0 | 50.0 | 4.0 | +3.17 | 3.2 | 0.16 | 36.0 | no edge shown yet |
| pin_value | moneyline | 2-7 | 22.2 | 37.8 | -15.5 | -5.31 | -59.0 | 0.12 | 55.6 | keep collecting (9/30) |
| pin_value | spread | 31-27 | 53.4 | 49.2 | 4.3 | +0.17 | 0.3 | 0.16 | 34.5 | no edge shown yet |
| pin_value | total | 28-27 | 50.9 | 50.0 | 0.9 | -1.74 | -3.2 | -0.02 | 36.4 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.7 | -19.4 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 126-192 | 39.6 | 47.5 | -7.9 | -53.76 | -16.9 | 0.16 | 43.4 | DROP: below break-even |
| consensus_gap | spread | 79-72 | 52.3 | 49.0 | 3.3 | -2.94 | -2.0 | 0.32 | 39.1 | no edge shown yet |
| consensus_gap | total | 91-81 | 52.9 | 50.0 | 2.9 | +0.75 | 0.4 | 0.88 | 55.8 | no edge shown yet |
| money_level+sharp_gap | moneyline | 53-28 | 65.4 | 62.8 | 2.6 | -6.66 | -8.2 | -0.0 | 53.1 | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+follow_move | moneyline | 16-23 | 41.0 | 55.1 | -14.1 | -13.51 | -34.6 | 0.08 | 51.3 | no edge shown yet |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 33.5 | -8.5 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| consensus_gap+rlm_quiet | moneyline | 1-5 | 16.7 | 28.0 | -11.3 | -3.68 | -61.3 | 1.07 | 83.3 | keep collecting (6/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.7 | -9.3 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 23-35 | 39.7 | 28.0 | 11.7 | +11.35 | 19.6 | 0.48 | 46.6 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 35-18 | 66.0 | 67.9 | -1.9 | -7.85 | -14.8 | -0.45 | 49.1 | beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 28.0 | -28.0 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 20-40 | 33.3 | 44.9 | -11.5 | -12.09 | -20.2 | 0.73 | 50.0 | DROP: below break-even |
| follow_move+money_level | moneyline | 67-20 | 77.0 | 68.5 | 8.5 | -2.97 | -3.4 | -0.22 | 42.5 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 36-17 | 67.9 | 53.7 | 14.2 | +7.93 | 15.0 | 0.19 | 52.8 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 33-27 | 55.0 | 67.6 | -12.6 | -13.02 | -21.7 | -0.15 | 43.3 | no edge shown yet |
| follow_move+sharp_gap | moneyline | 41-24 | 63.1 | 49.0 | 14.1 | +9.75 | 15.0 | 0.49 | 53.8 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 28-37 | 43.1 | 44.9 | -1.8 | -9.01 | -13.9 | 0.4 | 58.5 | DROP: below break-even |
| consensus_gap+money_moving | moneyline | 11-24 | 31.4 | 46.9 | -15.4 | -14.01 | -40.0 | 0.32 | 48.6 | INVERT candidate: wrong well beyond its base rate |
| follow_move+rlm_ratio | moneyline | 16-16 | 50.0 | 29.3 | 20.7 | +13.12 | 41.0 | 0.53 | 56.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 12-12 | 50.0 | 28.0 | 22.0 | +12.25 | 51.0 | 0.05 | 45.8 | keep collecting (24/30) |
| rlm_quiet+sharp_gap | moneyline | 12-15 | 44.4 | 28.0 | 16.5 | +9.25 | 34.3 | -0.1 | 44.4 | keep collecting (27/30) |
| rlm_ratio+sharp_gap | moneyline | 16-16 | 50.0 | 29.3 | 20.7 | +13.12 | 41.0 | 0.53 | 56.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 28.0 | -3.0 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 9-11 | 45.0 | 28.0 | 17.0 | +6.78 | 33.9 | 0.78 | 55.0 | keep collecting (20/30) |
| money_moving+rlm_ratio | moneyline | 7-6 | 53.8 | 28.0 | 25.9 | +7.63 | 58.7 | 0.55 | 53.8 | keep collecting (13/30) |
| money_delta+money_moving | moneyline | 4-6 | 40.0 | 28.0 | 12.0 | +2.99 | 29.9 | 0.17 | 60.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 4-5 | 44.4 | 28.0 | 16.5 | +3.99 | 44.3 | 0.19 | 66.7 | keep collecting (9/30) |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 42.7 | -42.7 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-1 | 66.7 | 57.3 | 9.3 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | moneyline | 2-1 | 66.7 | 57.3 | 9.3 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 28.0 | -28.0 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-2 | 33.3 | 42.7 | -9.3 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 28.0 | -28.0 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 28.0 | -28.0 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-2 | 33.3 | 42.7 | -9.3 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+sharp_gap | moneyline | 1-3 | 25.0 | 39.0 | -14.0 | -2.07 | -51.8 | -0.37 | 75.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 28.0 | -28.0 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | -1.55 | 50.0 | keep collecting (2/30) |
| pin_move+sharp_gap | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.13 | 56.5 | -0.1 | 50.0 | keep collecting (2/30) |
| money_level+rlm_ratio | moneyline | 4-4 | 50.0 | 33.5 | 16.5 | +0.87 | 10.8 | 1.94 | 87.5 | keep collecting (8/30) |
| money_level+pin_rlm | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.07 | -3.7 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+pin_rlm | moneyline | 1-0 | 100.0 | 28.0 | 72.0 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 1-0 | 100.0 | 28.0 | 72.0 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 4-1 | 80.0 | 28.0 | 52.0 | +7.99 | 159.8 | 0.36 | 60.0 | keep collecting (5/30) |
| money_delta+rlm_quiet | moneyline | 3-1 | 75.0 | 28.0 | 47.0 | +6.35 | 158.8 | -0.5 | 50.0 | keep collecting (4/30) |
| money_delta+rlm_ratio | moneyline | 4-0 | 100.0 | 28.0 | 72.0 | +8.99 | 224.8 | 1.75 | 75.0 | keep collecting (4/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 28.0 | -28.0 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-1 | 50.0 | 28.0 | 22.0 | +0.64 | 32.0 | 3.0 | 100.0 | keep collecting (2/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 72.0 | -72.0 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 72.0 | -72.0 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 47.3 | -1.8 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 47.3 | 36.0 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 13-9 | 59.1 | 48.5 | 10.6 | +2.17 | 9.9 | 0.32 | 40.9 | keep collecting (22/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.5 | 10.5 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-3 | 50.0 | 51.8 | -1.8 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-7 | 58.8 | 48.9 | 9.9 | +2.09 | 12.3 | 0.88 | 41.2 | keep collecting (17/30) |
| money_level+money_moving | spread | 10-6 | 62.5 | 48.7 | 13.8 | +3.12 | 19.5 | 1.19 | 68.8 | keep collecting (16/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.8 | -6.0 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
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
| follow_move+pin_value | spread | 13-8 | 61.9 | 48.6 | 13.3 | +3.36 | 16.0 | 0.19 | 28.6 | keep collecting (21/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 47.3 | 52.7 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 47.3 | 52.7 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 47.3 | 52.7 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-3 | 75.0 | 48.2 | 26.8 | +5.22 | 43.5 | 0.75 | 50.0 | keep collecting (12/30) |
| money_delta+rlm_quiet | spread | 1-0 | 100.0 | 47.3 | 52.7 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 2-0 | 100.0 | 47.3 | 52.7 | +1.74 | 87.1 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 2-2 | 50.0 | 52.7 | -2.7 | -0.07 | -1.7 | 1.25 | 25.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | spread | 2-1 | 66.7 | 50.9 | 15.8 | +0.86 | 28.7 | 1.0 | 33.3 | keep collecting (3/30) |
| pin_move+pin_value | spread | 1-5 | 16.7 | 48.2 | -31.5 | -4.09 | -68.2 | 0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 47.3 | -47.3 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-3 | 25.0 | 47.3 | -22.3 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.7 | -52.7 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 16-19 | 45.7 | 49.8 | -4.1 | -4.41 | -12.6 | 0.77 | 54.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 32-26 | 55.2 | 50.1 | 5.1 | +3.23 | 5.6 | -0.14 | 36.2 | no edge shown yet |
| money_level+sharp_gap | total | 47-38 | 55.3 | 50.1 | 5.2 | +4.73 | 5.6 | -0.07 | 36.5 | no edge shown yet |
| money_moving+sharp_gap | total | 39-25 | 60.9 | 49.9 | 11.0 | +10.53 | 16.5 | 0.23 | 37.5 | no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 50.3 | -50.3 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 10-6 | 62.5 | 49.9 | 12.6 | +3.05 | 19.1 | 0.44 | 37.5 | keep collecting (16/30) |
| money_moving+pin_value | total | 6-4 | 60.0 | 49.9 | 10.1 | +1.38 | 13.8 | 0.2 | 30.0 | keep collecting (10/30) |
| pin_value+sharp_gap | total | 12-7 | 63.2 | 50.0 | 13.2 | +3.83 | 20.2 | 0.16 | 36.8 | keep collecting (19/30) |
| follow_move+money_level | total | 27-24 | 52.9 | 50.1 | 2.8 | +0.49 | 1.0 | 0.25 | 43.1 | no edge shown yet |
| follow_move+pin_value | total | 9-11 | 45.0 | 50.0 | -5.0 | -2.94 | -14.7 | -0.45 | 25.0 | keep collecting (20/30) |
| follow_move+rlm_ratio | total | 17-9 | 65.4 | 49.8 | 15.6 | +6.62 | 25.5 | 0.77 | 61.5 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 37-23 | 61.7 | 50.0 | 11.7 | +10.69 | 17.8 | 0.52 | 48.3 | no edge shown yet |
| money_level+rlm_ratio | total | 6-4 | 60.0 | 49.8 | 10.2 | +1.54 | 15.4 | 1.1 | 70.0 | keep collecting (10/30) |
| pin_value+rlm_ratio | total | 3-1 | 75.0 | 49.9 | 25.1 | +1.73 | 43.2 | -0.25 | 50.0 | keep collecting (4/30) |
| rlm_ratio+sharp_gap | total | 17-9 | 65.4 | 49.8 | 15.6 | +6.62 | 25.5 | 0.77 | 61.5 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 21-21 | 50.0 | 49.9 | 0.1 | -1.8 | -4.3 | 0.57 | 50.0 | no edge shown yet |
| consensus_gap+money_level | total | 7-4 | 63.6 | 50.1 | 13.5 | +2.21 | 20.1 | -0.09 | 27.3 | keep collecting (11/30) |
| consensus_gap+money_moving | total | 5-1 | 83.3 | 50.1 | 33.2 | +3.43 | 57.2 | -0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+pin_value | total | 10-14 | 41.7 | 50.1 | -8.4 | -5.11 | -21.3 | 0.5 | 50.0 | keep collecting (24/30) |
| consensus_gap+sharp_gap | total | 8-7 | 53.3 | 49.9 | 3.4 | +0.2 | 1.3 | 0.07 | 33.3 | keep collecting (15/30) |
| money_moving+rlm_ratio | total | 10-5 | 66.7 | 49.8 | 16.9 | +4.22 | 28.1 | 0.67 | 60.0 | keep collecting (15/30) |
| consensus_gap+follow_move | total | 16-12 | 57.1 | 50.0 | 7.2 | +2.51 | 9.0 | 1.5 | 71.4 | keep collecting (28/30) |
| consensus_gap+money_delta | total | 3-0 | 100.0 | 50.1 | 49.9 | +2.69 | 89.6 | 0.33 | 33.3 | keep collecting (3/30) |
| follow_move+money_delta | total | 3-3 | 50.0 | 49.8 | 0.2 | -0.31 | -5.2 | 1.33 | 66.7 | keep collecting (6/30) |
| money_delta+money_moving | total | 8-3 | 72.7 | 49.8 | 22.9 | +4.17 | 37.9 | 1.36 | 45.5 | keep collecting (11/30) |
| money_delta+pin_value | total | 3-0 | 100.0 | 49.9 | 50.1 | +2.69 | 89.6 | 0.0 | 33.3 | keep collecting (3/30) |
| money_delta+sharp_gap | total | 7-2 | 77.8 | 49.8 | 27.9 | +4.26 | 47.4 | 1.67 | 55.6 | keep collecting (9/30) |
| money_moving+rlm_quiet | total | 7-6 | 53.8 | 49.8 | 4.1 | +0.36 | 2.8 | 0.46 | 46.2 | keep collecting (13/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 9-5 | 64.3 | 49.7 | 14.5 | +3.22 | 23.0 | 0.71 | 64.3 | keep collecting (14/30) |
| rlm_quiet+sharp_gap | total | 11-6 | 64.7 | 49.7 | 15.0 | +4.04 | 23.8 | 0.76 | 58.8 | keep collecting (17/30) |
| follow_move+pin_move | total | 3-2 | 60.0 | 49.8 | 10.2 | +0.77 | 15.4 | 0.8 | 60.0 | keep collecting (5/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 49.7 | -49.7 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 49.7 | -49.7 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 3-2 | 60.0 | 49.8 | 10.2 | +0.73 | 14.5 | 0.8 | 60.0 | keep collecting (5/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 49.7 | 0.3 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 4-1 | 80.0 | 49.7 | 30.3 | +2.68 | 53.6 | 0.4 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | total | 1-2 | 33.3 | 50.3 | -17.0 | -1.09 | -36.4 | 1.0 | 33.3 | keep collecting (3/30) |
| pin_move+pin_value | total | 2-4 | 33.3 | 50.2 | -16.9 | -2.18 | -36.4 | 0.5 | 33.3 | keep collecting (6/30) |
| pin_move+sharp_gap | total | 0-2 | 0.0 | 50.3 | -50.3 | -2.0 | -100.0 | 1.5 | 50.0 | keep collecting (2/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 49.7 | -49.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 1-2 | 33.3 | 49.7 | -16.4 | -1.09 | -36.4 | 1.67 | 100.0 | keep collecting (3/30) |
| consensus_gap+pin_move | total | 1-0 | 100.0 | 50.3 | 49.7 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 245-372 | 39.7 | 42.0 | -2.3 | -69.58 | -11.3 |  |  | DROP: below break-even |
| pin_move | both | 603-635 | 48.7 | 49.7 | -1.0 | -67.87 | -5.5 |  |  | DROP: below break-even |
| money_delta | both | 379-495 | 43.4 | 44.2 | -0.8 | -62.86 | -7.2 |  |  | DROP: below break-even |
| pin_rlm | both | 158-200 | 44.1 | 42.1 | 2.1 | +10.01 | 2.8 |  |  | DROP: below break-even |
| follow_move | both | 1038-989 | 51.2 | 51.2 | 0.0 | -142.91 | -7.1 |  |  | no edge shown yet |
| rlm_ratio | both | 238-295 | 44.7 | 43.7 | 0.9 | -25.8 | -4.8 |  |  | DROP: below break-even |
| money_level | both | 1327-990 | 57.3 | 55.4 | 1.8 | -78.39 | -3.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 1030-1193 | 46.3 | 47.5 | -1.2 | -162.62 | -7.3 |  |  | DROP: below break-even |
| money_moving | both | 1038-1189 | 46.6 | 47.9 | -1.3 | -164.58 | -7.4 |  |  | DROP: below break-even |
| pin_value | both | 448-441 | 50.4 | 48.2 | 2.2 | +20.48 | 2.3 |  |  | no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 50.9 | 15.8 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 419-506 | 45.3 | 48.4 | -3.1 | -75.16 | -8.1 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 152-149 | 50.5 | 51.3 | -0.8 | -17.67 | -5.9 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 178-271 | 39.6 | 45.7 | -6.0 | -32.58 | -7.3 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 103-97 | 51.5 | 50.7 | 0.8 | +9.75 | 4.9 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 25-46 | 35.2 | 38.2 | -3.0 | +6.43 | 9.1 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 167-166 | 50.2 | 46.2 | 4.0 | +18.22 | 5.5 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | both | 30-51 | 37.0 | 39.7 | -2.7 | -3.61 | -4.5 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 178-275 | 39.3 | 45.1 | -5.8 | -33.26 | -7.3 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 544-603 | 47.4 | 49.1 | -1.6 | -104.06 | -9.1 |  |  | DROP: below break-even |
| follow_move+pin_move | both | 430-473 | 47.6 | 49.9 | -2.3 | -80.5 | -8.9 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 124-149 | 45.4 | 43.6 | 1.9 | -10.94 | -4.0 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 153-147 | 51.0 | 49.1 | 1.9 | -0.85 | -0.3 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 238-295 | 44.7 | 43.7 | 0.9 | -25.8 | -4.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 551-604 | 47.7 | 48.8 | -1.1 | -94.3 | -8.2 |  |  | DROP: below break-even |
| money_moving+pin_move | both | 342-394 | 46.5 | 48.4 | -1.9 | -49.12 | -6.7 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 152-192 | 44.2 | 42.1 | 2.1 | +12.04 | 3.5 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 189-223 | 45.9 | 47.6 | -1.7 | -20.18 | -4.9 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 229-284 | 44.6 | 43.9 | 0.8 | -24.43 | -4.8 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 991-1145 | 46.4 | 47.6 | -1.2 | -148.27 | -6.9 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 146-168 | 46.5 | 43.8 | 2.7 | +7.88 | 2.5 |  |  | DROP: below break-even |
| pin_move+pin_value | both | 192-189 | 50.4 | 49.2 | 1.2 | -6.91 | -1.8 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 132-146 | 47.5 | 45.0 | 2.5 | -1.75 | -0.6 |  |  | DROP: below break-even |
| pin_move+sharp_gap | both | 347-399 | 46.5 | 48.2 | -1.7 | -49.66 | -6.7 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 43-47 | 47.8 | 46.2 | 1.6 | +9.27 | 10.3 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 124-149 | 45.4 | 43.6 | 1.9 | -10.94 | -4.0 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 158-200 | 44.1 | 42.1 | 2.1 | +10.01 | 2.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 43-37 | 53.8 | 48.7 | 5.0 | +2.14 | 2.7 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 190-223 | 46.0 | 47.5 | -1.5 | -19.29 | -4.7 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 238-295 | 44.7 | 43.7 | 0.9 | -25.8 | -4.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 185-227 | 44.9 | 45.7 | -0.8 | -39.82 | -9.7 |  |  | DROP: below break-even |
| money_level+money_moving | both | 724-643 | 53.0 | 52.4 | 0.5 | -57.53 | -4.2 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 708-632 | 52.8 | 52.2 | 0.6 | -50.53 | -3.8 |  |  | no edge shown yet |
| follow_move+money_level | both | 649-477 | 57.6 | 56.3 | 1.4 | -59.46 | -5.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 109-93 | 54.0 | 48.2 | 5.8 | +11.85 | 5.9 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 263-197 | 57.2 | 58.3 | -1.1 | -19.65 | -4.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_move | both | 341-317 | 51.8 | 53.1 | -1.3 | -39.16 | -6.0 |  |  | no edge shown yet |
| money_level+pin_value | both | 213-192 | 52.6 | 49.9 | 2.7 | -6.56 | -1.6 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 25-60 | 29.4 | 36.8 | -7.4 | -15.04 | -17.7 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | both | 245-372 | 39.7 | 42.0 | -2.3 | -69.58 | -11.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 124-212 | 36.9 | 41.3 | -4.4 | -52.24 | -15.5 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 274-385 | 41.6 | 42.6 | -1.0 | -49.75 | -7.5 |  |  | DROP: below break-even |
| consensus_gap+money_delta | both | 51-114 | 30.9 | 38.0 | -7.1 | -23.05 | -14.0 |  |  | DROP: below break-even |
| money_delta+money_level | both | 132-120 | 52.4 | 47.1 | 5.2 | +17.93 | 7.1 |  |  | no edge shown yet |
| money_delta+pin_value | both | 82-78 | 51.2 | 47.3 | 4.0 | +3.69 | 2.3 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 271-379 | 41.7 | 42.6 | -0.9 | -46.92 | -7.2 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 99-176 | 36.0 | 40.0 | -4.0 | -40.2 | -14.6 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | both | 115-204 | 36.1 | 41.3 | -5.3 | -51.86 | -16.3 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 69-125 | 35.6 | 42.8 | -7.2 | -48.23 | -24.9 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | both | 118-169 | 41.1 | 44.0 | -2.9 | -33.04 | -11.5 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 50-94 | 34.7 | 40.4 | -5.7 | -29.08 | -20.2 |  |  | DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 50.9 | 15.8 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 135-165 | 45.0 | 46.2 | -1.2 | -19.64 | -6.5 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 70-48 | 59.3 | 46.8 | 12.5 | +21.0 | 17.8 |  |  | PROMOTE: beats break-even and its own base rate |
| money_delta+pin_rlm | both | 92-114 | 44.7 | 42.1 | 2.6 | +2.3 | 1.1 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | both | 133-152 | 46.7 | 44.3 | 2.4 | -12.5 | -4.4 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | both | 33-49 | 40.2 | 47.5 | -7.2 | -8.62 | -10.5 |  |  | DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 49.7 | 50.3 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 73-163 | 30.9 | 28.7 | 2.2 | -19.45 | -8.2 |  |  | DROP: below break-even |
| rlm_quiet | spread | 59-61 | 49.2 | 51.1 | -1.9 | -6.14 | -5.1 |  |  | no edge shown yet |
| rlm_quiet | total | 113-148 | 43.3 | 49.8 | -6.5 | -43.99 | -16.9 |  |  | DROP: below break-even |
| pin_move | moneyline | 135-136 | 49.8 | 48.3 | 1.5 | +4.33 | 1.6 |  |  | no edge shown yet |
| pin_move | spread | 232-248 | 48.3 | 50.3 | -2.0 | -36.74 | -7.7 |  |  | DROP: below break-even |
| pin_move | total | 236-251 | 48.5 | 49.9 | -1.5 | -35.46 | -7.3 |  |  | DROP: below break-even |
| money_delta | moneyline | 67-195 | 25.6 | 29.8 | -4.2 | -48.18 | -18.4 |  |  | DROP: below break-even |
| money_delta | spread | 131-135 | 49.2 | 50.9 | -1.7 | -15.61 | -5.9 |  |  | no edge shown yet |
| money_delta | total | 181-165 | 52.3 | 49.8 | 2.5 | +0.93 | 0.3 |  |  | no edge shown yet |
| pin_rlm | moneyline | 46-94 | 32.9 | 29.5 | 3.3 | +13.47 | 9.6 |  |  | DROP: below break-even |
| pin_rlm | spread | 26-24 | 52.0 | 51.2 | 0.8 | -0.3 | -0.6 |  |  | no edge shown yet |
| pin_rlm | total | 86-82 | 51.2 | 49.8 | 1.4 | -3.16 | -1.9 |  |  | no edge shown yet |
| follow_move | moneyline | 382-282 | 57.5 | 54.0 | 3.5 | -34.27 | -5.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 298-318 | 48.4 | 49.7 | -1.3 | -46.68 | -7.6 |  |  | DROP: below break-even |
| follow_move | total | 358-389 | 47.9 | 50.0 | -2.1 | -61.96 | -8.3 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 52-117 | 30.8 | 30.3 | 0.5 | -17.85 | -10.6 |  |  | DROP: below break-even |
| rlm_ratio | spread | 44-47 | 48.4 | 50.3 | -2.0 | -7.07 | -7.8 |  |  | no edge shown yet |
| rlm_ratio | total | 142-131 | 52.0 | 49.8 | 2.2 | -0.88 | -0.3 |  |  | no edge shown yet |
| money_level | moneyline | 520-208 | 71.4 | 68.0 | 3.4 | -26.24 | -3.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 370-379 | 49.4 | 49.2 | 0.2 | -45.43 | -6.1 |  |  | DROP: below break-even |
| money_level | total | 437-403 | 52.0 | 50.1 | 1.9 | -6.72 | -0.8 |  |  | no edge shown yet |
| sharp_gap | moneyline | 265-404 | 39.6 | 42.4 | -2.8 | -68.14 | -10.2 |  |  | DROP: below break-even |
| sharp_gap | spread | 373-368 | 50.3 | 49.6 | 0.8 | -31.39 | -4.2 |  |  | no edge shown yet |
| sharp_gap | total | 392-421 | 48.2 | 49.9 | -1.7 | -63.08 | -7.8 |  |  | DROP: below break-even |
| money_moving | moneyline | 278-387 | 41.8 | 43.7 | -1.9 | -52.19 | -7.8 |  |  | DROP: below break-even |
| money_moving | spread | 370-371 | 49.9 | 49.5 | 0.4 | -37.26 | -5.0 |  |  | no edge shown yet |
| money_moving | total | 390-431 | 47.5 | 50.0 | -2.5 | -75.12 | -9.1 |  |  | DROP: below break-even |
| pin_value | moneyline | 23-58 | 28.4 | 32.3 | -3.9 | +27.04 | 33.4 |  |  | DROP: below break-even |
| pin_value | spread | 200-186 | 51.8 | 49.6 | 2.2 | -11.97 | -3.1 |  |  | no edge shown yet |
| pin_value | total | 225-197 | 53.3 | 50.0 | 3.3 | +5.42 | 1.3 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.7 | 47.3 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 188-304 | 38.2 | 47.3 | -9.1 | -74.86 | -15.2 |  |  | DROP: below break-even |
| consensus_gap | spread | 102-85 | 54.5 | 49.1 | 5.5 | +2.06 | 1.1 |  |  | no edge shown yet |
| consensus_gap | total | 129-117 | 52.4 | 50.1 | 2.3 | -2.36 | -1.0 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 191-106 | 64.3 | 62.7 | 1.6 | -2.96 | -1.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 176-103 | 63.1 | 62.1 | 1.0 | -3.2 | -1.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 248-371 | 40.1 | 42.5 | -2.4 | -48.55 | -7.8 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 67-80 | 45.6 | 53.1 | -7.6 | -22.77 | -15.5 |  |  | DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 9-46 | 16.4 | 29.6 | -13.2 | -15.24 | -27.7 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 73-163 | 30.9 | 28.7 | 2.2 | -19.45 | -8.2 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 134-79 | 62.9 | 68.5 | -5.6 | -14.11 | -6.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 72-168 | 30.0 | 42.3 | -12.3 | -21.91 | -9.1 |  |  | !! CHECK: consensus_gap+money_moving close moneyline all sits -12.3 pts from its base (42.3%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+money_level | moneyline | 285-99 | 74.2 | 69.2 | 5.0 | -11.69 | -3.0 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 138-151 | 47.8 | 47.2 | 0.6 | -21.14 | -7.3 |  |  | DROP: below break-even |
| money_delta+money_moving | moneyline | 63-176 | 26.4 | 29.4 | -3.1 | -33.0 | -13.8 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 61-175 | 25.8 | 29.4 | -3.6 | -34.19 | -14.5 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 71-174 | 29.0 | 41.3 | -12.3 | -25.48 | -10.4 |  |  | !! CHECK: consensus_gap+sharp_gap close moneyline all sits -12.3 pts from its base (41.3%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+sharp_gap | moneyline | 135-154 | 46.7 | 46.1 | 0.6 | -22.77 | -7.9 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | moneyline | 33-97 | 25.4 | 28.6 | -3.2 | -19.99 | -15.4 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 35-102 | 25.5 | 28.6 | -3.0 | -23.81 | -17.4 |  |  | DROP: below break-even |
| consensus_gap+pin_move | moneyline | 41-41 | 50.0 | 52.2 | -2.2 | +11.76 | 14.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 12-32 | 27.3 | 31.0 | -3.7 | +9.05 | 20.6 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 6-36 | 14.3 | 30.1 | -15.8 | -9.64 | -23.0 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 106-99 | 51.7 | 49.5 | 2.2 | -2.41 | -1.2 |  |  | no edge shown yet |
| follow_move+pin_rlm | moneyline | 31-57 | 35.2 | 30.0 | 5.3 | -4.36 | -5.0 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 52-117 | 30.8 | 30.3 | 0.5 | -17.85 | -10.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 58-77 | 43.0 | 41.7 | 1.3 | +9.64 | 7.1 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 45-89 | 33.6 | 29.6 | 4.0 | +17.07 | 12.7 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 50-110 | 31.2 | 30.4 | 0.8 | -13.97 | -8.7 |  |  | DROP: below break-even |
| pin_move+pin_rlm | moneyline | 34-62 | 35.4 | 29.3 | 6.1 | +11.35 | 11.8 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 32-56 | 36.4 | 29.5 | 6.9 | +0.33 | 0.4 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 27-45 | 37.5 | 30.4 | 7.1 | +3.12 | 4.3 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 58-81 | 41.7 | 41.0 | 0.8 | +5.46 | 3.9 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 18-49 | 26.9 | 29.3 | -2.4 | -13.5 | -20.2 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 31-57 | 35.2 | 30.0 | 5.3 | -4.36 | -5.0 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 46-94 | 32.9 | 29.5 | 3.3 | +13.47 | 9.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 32-97 | 24.8 | 28.6 | -3.8 | -22.65 | -17.6 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 52-117 | 30.8 | 30.3 | 0.5 | -17.85 | -10.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 14-85 | 14.1 | 29.7 | -15.6 | -26.27 | -26.5 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 16-47 | 25.4 | 31.5 | -6.1 | +5.85 | 9.3 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 20-43 | 31.7 | 30.8 | 1.0 | -2.92 | -4.6 |  |  | DROP: below break-even |
| money_delta+pin_rlm | moneyline | 26-54 | 32.5 | 29.6 | 2.9 | +1.87 | 2.3 |  |  | DROP: below break-even |
| money_delta+pin_value | moneyline | 3-18 | 14.3 | 28.0 | -13.7 | -6.68 | -31.8 |  |  | keep collecting (21/30) |
| money_moving+pin_value | moneyline | 11-34 | 24.4 | 30.9 | -6.4 | +11.94 | 26.5 |  |  | DROP: below break-even |
| pin_move+pin_value | moneyline | 7-11 | 38.9 | 35.3 | 3.6 | +6.35 | 35.3 |  |  | keep collecting (18/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 28.0 | 3.3 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 11-36 | 23.4 | 30.8 | -7.4 | +9.94 | 21.1 |  |  | DROP: below break-even |
| follow_move+money_delta | moneyline | 33-67 | 33.0 | 32.4 | 0.6 | -18.6 | -18.6 |  |  | DROP: below break-even |
| money_delta+money_level | moneyline | 20-24 | 45.5 | 34.0 | 11.5 | +12.18 | 27.7 |  |  | no edge shown yet |
| money_delta+rlm_ratio | moneyline | 28-57 | 32.9 | 31.1 | 1.9 | -13.09 | -15.4 |  |  | DROP: below break-even |
| money_level+pin_move | moneyline | 84-48 | 63.6 | 66.4 | -2.7 | -2.89 | -2.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 13-10 | 56.5 | 33.7 | 22.8 | +6.93 | 30.1 |  |  | keep collecting (23/30) |
| money_level+rlm_ratio | moneyline | 16-14 | 53.3 | 38.2 | 15.1 | +6.18 | 20.6 |  |  | no edge shown yet |
| money_delta+rlm_quiet | moneyline | 19-52 | 26.8 | 29.8 | -3.1 | -21.26 | -29.9 |  |  | DROP: below break-even |
| money_level+pin_value | moneyline | 5-3 | 62.5 | 66.5 | -4.0 | -0.32 | -4.0 |  |  | keep collecting (8/30) |
| follow_move+pin_value | moneyline | 3-9 | 25.0 | 35.3 | -10.3 | +3.8 | 31.7 |  |  | keep collecting (12/30) |
| pin_value+rlm_quiet | moneyline | 2-7 | 22.2 | 28.0 | -5.7 | +5.12 | 56.9 |  |  | keep collecting (9/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 28.0 | -3.0 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 37-29 | 56.1 | 48.5 | 7.5 | +2.57 | 3.9 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 51-47 | 52.0 | 48.8 | 3.2 | -3.5 | -3.6 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 30-30 | 50.0 | 49.3 | 0.7 | -4.4 | -7.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 74-53 | 58.3 | 49.0 | 9.2 | +10.03 | 7.9 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 5-4 | 55.6 | 50.3 | 5.3 | +0.18 | 2.0 |  |  | keep collecting (9/30) |
| consensus_gap+sharp_gap | spread | 50-47 | 51.5 | 49.0 | 2.5 | -4.4 | -4.5 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 172-178 | 49.1 | 49.3 | -0.2 | -22.43 | -6.4 |  |  | no edge shown yet |
| follow_move+pin_move | spread | 145-170 | 46.0 | 50.1 | -4.1 | -37.75 | -12.0 |  |  | DROP: below break-even |
| follow_move+pin_rlm | spread | 19-20 | 48.7 | 50.9 | -2.2 | -2.65 | -6.8 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 66-59 | 52.8 | 49.2 | 3.6 | -1.38 | -1.1 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 44-47 | 48.4 | 50.3 | -2.0 | -7.07 | -7.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 173-177 | 49.4 | 49.4 | 0.1 | -20.29 | -5.8 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 127-140 | 47.6 | 49.9 | -2.3 | -25.11 | -9.4 |  |  | DROP: below break-even |
| money_moving+pin_rlm | spread | 24-24 | 50.0 | 51.1 | -1.1 | -2.13 | -4.4 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 92-98 | 48.4 | 49.2 | -0.8 | -18.6 | -9.8 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 42-46 | 47.7 | 50.2 | -2.5 | -8.0 | -9.1 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 365-363 | 50.1 | 49.5 | 0.6 | -33.76 | -4.6 |  |  | no edge shown yet |
| pin_move+pin_rlm | spread | 26-24 | 52.0 | 51.2 | 0.8 | -0.3 | -0.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 91-91 | 50.0 | 49.9 | 0.1 | -11.02 | -6.1 |  |  | no edge shown yet |
| pin_move+rlm_ratio | spread | 23-27 | 46.0 | 50.8 | -4.8 | -6.1 | -12.2 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 130-140 | 48.1 | 49.9 | -1.7 | -22.38 | -8.3 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 8-10 | 44.4 | 50.9 | -6.5 | -2.97 | -16.5 |  |  | keep collecting (18/30) |
| pin_rlm+rlm_ratio | spread | 19-20 | 48.7 | 50.9 | -2.2 | -2.65 | -6.8 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 26-24 | 52.0 | 51.2 | 0.8 | -0.3 | -0.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 8-8 | 50.0 | 49.7 | 0.3 | -1.17 | -7.3 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | spread | 92-98 | 48.4 | 49.3 | -0.9 | -18.67 | -9.8 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 44-47 | 48.4 | 50.3 | -2.0 | -7.07 | -7.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 167-178 | 48.4 | 49.1 | -0.6 | -26.92 | -7.8 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 23-29 | 44.2 | 50.0 | -5.8 | -8.3 | -16.0 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 284-282 | 50.2 | 49.2 | 1.0 | -26.12 | -4.6 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 61-53 | 53.5 | 48.6 | 4.9 | -0.85 | -0.7 |  |  | no edge shown yet |
| money_level+money_moving | spread | 283-283 | 50.0 | 49.2 | 0.8 | -28.04 | -5.0 |  |  | no edge shown yet |
| money_level+pin_move | spread | 117-138 | 45.9 | 49.6 | -3.7 | -32.62 | -12.8 |  |  | DROP: below break-even |
| money_level+pin_value | spread | 100-101 | 49.8 | 48.9 | 0.8 | -14.86 | -7.4 |  |  | no edge shown yet |
| consensus_gap+money_delta | spread | 16-14 | 53.3 | 50.7 | 2.6 | -0.33 | -1.1 |  |  | no edge shown yet |
| follow_move+money_delta | spread | 42-52 | 44.7 | 50.5 | -5.8 | -13.97 | -14.9 |  |  | no edge shown yet |
| money_delta+money_level | spread | 43-42 | 50.6 | 50.0 | 0.6 | -3.26 | -3.8 |  |  | no edge shown yet |
| money_delta+money_moving | spread | 74-82 | 47.4 | 50.5 | -3.1 | -15.21 | -9.8 |  |  | no edge shown yet |
| money_delta+pin_value | spread | 34-29 | 54.0 | 50.6 | 3.3 | +0.63 | 1.0 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 73-80 | 47.7 | 50.5 | -2.8 | -14.19 | -9.3 |  |  | no edge shown yet |
| follow_move+rlm_quiet | spread | 59-61 | 49.2 | 51.1 | -1.9 | -6.14 | -5.1 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 15-6 | 71.4 | 51.2 | 20.3 | +7.65 | 36.4 |  |  | keep collecting (21/30) |
| rlm_quiet+sharp_gap | spread | 23-15 | 60.5 | 51.3 | 9.2 | +6.0 | 15.8 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 14-11 | 56.0 | 50.5 | 5.5 | +1.57 | 6.3 |  |  | keep collecting (25/30) |
| money_delta+pin_move | spread | 39-48 | 44.8 | 51.1 | -6.3 | -12.42 | -14.3 |  |  | no edge shown yet |
| money_delta+rlm_ratio | spread | 17-29 | 37.0 | 50.1 | -13.2 | -13.93 | -30.3 |  |  | DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 52.7 | 47.3 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_rlm | spread | 13-17 | 43.3 | 50.9 | -7.6 | -5.31 | -17.7 |  |  | no edge shown yet |
| money_delta+rlm_quiet | spread | 17-20 | 45.9 | 51.5 | -5.6 | -4.27 | -11.5 |  |  | no edge shown yet |
| money_moving+rlm_quiet | spread | 22-15 | 59.5 | 51.2 | 8.2 | +5.05 | 13.6 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 33-35 | 48.5 | 51.5 | -3.0 | -4.22 | -6.2 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-3 | 66.7 | 52.1 | 14.6 | +2.56 | 28.4 |  |  | keep collecting (9/30) |
| consensus_gap+rlm_quiet | spread | 4-3 | 57.1 | 51.2 | 6.0 | +0.48 | 6.9 |  |  | keep collecting (7/30) |
| pin_value+rlm_quiet | spread | 6-7 | 46.2 | 50.2 | -4.1 | -1.7 | -13.1 |  |  | keep collecting (13/30) |
| follow_move+money_delta | total | 110-108 | 50.5 | 49.8 | 0.6 | -7.25 | -3.3 |  |  | no edge shown yet |
| money_level+money_moving | total | 250-254 | 49.6 | 50.0 | -0.4 | -26.53 | -5.3 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 248-247 | 50.1 | 50.0 | 0.1 | -21.21 | -4.3 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 378-411 | 47.9 | 49.9 | -2.0 | -65.96 | -8.4 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 68-65 | 51.1 | 50.2 | 0.9 | -4.69 | -3.5 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 32-26 | 55.2 | 50.1 | 5.0 | +2.39 | 4.1 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 77-66 | 53.8 | 50.1 | 3.7 | +2.34 | 1.6 |  |  | no edge shown yet |
| follow_move+money_moving | total | 234-274 | 46.1 | 50.0 | -3.9 | -60.49 | -11.9 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 243-273 | 47.1 | 49.9 | -2.9 | -51.24 | -9.9 |  |  | DROP: below break-even |
| money_level+pin_move | total | 140-131 | 51.7 | 50.0 | 1.6 | -3.64 | -1.3 |  |  | no edge shown yet |
| money_level+pin_value | total | 108-88 | 55.1 | 50.2 | 4.9 | +8.62 | 4.4 |  |  | no edge shown yet |
| pin_move+pin_value | total | 94-87 | 51.9 | 50.0 | 1.9 | -2.25 | -1.2 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 113-148 | 43.3 | 49.8 | -6.5 | -43.99 | -16.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 157-177 | 47.0 | 49.9 | -2.9 | -33.65 | -10.1 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | total | 66-95 | 41.0 | 49.8 | -8.8 | -34.42 | -21.4 |  |  | DROP: below break-even |
| money_delta+money_moving | total | 137-127 | 51.9 | 49.8 | 2.1 | -1.54 | -0.6 |  |  | no edge shown yet |
| follow_move+money_level | total | 197-200 | 49.6 | 50.1 | -0.4 | -20.85 | -5.3 |  |  | no edge shown yet |
| follow_move+pin_value | total | 84-79 | 51.5 | 50.0 | 1.5 | -3.28 | -2.0 |  |  | no edge shown yet |
| money_moving+pin_value | total | 86-91 | 48.6 | 50.0 | -1.4 | -13.52 | -7.6 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 87-89 | 49.4 | 50.0 | -0.6 | -10.57 | -6.0 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 55-56 | 49.5 | 50.1 | -0.6 | -7.17 | -6.5 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 57-54 | 51.4 | 50.1 | 1.2 | -3.38 | -3.0 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 48-40 | 54.5 | 50.2 | 4.4 | +2.53 | 2.9 |  |  | no edge shown yet |
| consensus_gap+money_delta | total | 21-15 | 58.3 | 50.0 | 8.3 | +3.56 | 9.9 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | total | 12-11 | 52.2 | 49.9 | 2.2 | -0.28 | -1.2 |  |  | keep collecting (23/30) |
| money_delta+rlm_quiet | total | 33-53 | 38.4 | 49.8 | -11.4 | -22.69 | -26.4 |  |  | DROP: below break-even |
| money_delta+sharp_gap | total | 137-124 | 52.5 | 49.8 | 2.7 | +1.46 | 0.6 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 60-92 | 39.5 | 49.8 | -10.3 | -36.91 | -24.3 |  |  | !! IMPLAUSIBLE: money_moving+rlm_quiet close total all 39.5% on n=152. A -110 market outside 40-60% at this sample is a measurement bug until proven otherwise. Recompute from source.  ||  DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 69-54 | 56.1 | 49.9 | 6.2 | +9.01 | 7.3 |  |  | no edge shown yet |
| money_delta+pin_move | total | 76-74 | 50.7 | 49.8 | 0.9 | -4.29 | -2.9 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 159-178 | 47.2 | 49.9 | -2.7 | -32.74 | -9.7 |  |  | DROP: below break-even |
| follow_move+pin_move | total | 179-204 | 46.7 | 49.9 | -3.2 | -40.34 | -10.5 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | total | 25-35 | 41.7 | 49.8 | -8.2 | -12.04 | -20.1 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | total | 10-11 | 47.6 | 50.0 | -2.4 | -2.13 | -10.1 |  |  | keep collecting (21/30) |
| consensus_gap+rlm_ratio | total | 19-11 | 63.3 | 50.1 | 13.3 | +5.85 | 19.5 |  |  | no edge shown yet |
| follow_move+pin_rlm | total | 74-72 | 50.7 | 49.8 | 0.9 | -3.93 | -2.7 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 142-131 | 52.0 | 49.8 | 2.2 | -0.88 | -0.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 43-27 | 61.4 | 49.8 | 11.6 | +12.5 | 17.9 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 70-50 | 58.3 | 49.9 | 8.5 | +13.97 | 11.6 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 83-79 | 51.2 | 49.8 | 1.4 | -2.9 | -1.8 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 137-128 | 51.7 | 49.8 | 1.9 | -2.46 | -0.9 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 86-82 | 51.2 | 49.8 | 1.4 | -3.16 | -1.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 82-74 | 52.6 | 49.8 | 2.7 | +1.23 | 0.8 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 30-26 | 53.6 | 49.9 | 3.7 | +1.17 | 2.1 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 74-72 | 50.7 | 49.8 | 0.9 | -3.93 | -2.7 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 86-82 | 51.2 | 49.8 | 1.4 | -3.16 | -1.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 34-26 | 56.7 | 49.9 | 6.8 | +4.78 | 8.0 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 142-131 | 52.0 | 49.8 | 2.2 | -0.88 | -0.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 53-43 | 55.2 | 49.8 | 5.4 | +5.73 | 6.0 |  |  | no edge shown yet |
| money_delta+rlm_ratio | total | 88-66 | 57.1 | 49.8 | 7.3 | +14.51 | 9.4 |  |  | no edge shown yet |
| money_delta+pin_value | total | 45-31 | 59.2 | 49.9 | 9.3 | +9.74 | 12.8 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 53-78 | 40.5 | 49.8 | -9.4 | -29.16 | -22.3 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | total | 26-42 | 38.2 | 49.8 | -11.5 | -18.14 | -26.7 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | total | 52-73 | 41.6 | 49.8 | -8.2 | -25.19 | -20.2 |  |  | DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 49.7 | 50.3 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| rlm_quiet | close | 1-3k bets | 162-239 | 40.4 | -1.5 | -7.5 |  |
| rlm_quiet | close | 3k+ bets | 57-88 | 39.3 | -3.2 | -15.9 |  |
| rlm_quiet | close | <1k bets | 26-45 | 36.6 | -4.9 | -23.0 |  |
| rlm_quiet | close | pin $1-2k | 66-118 | 35.9 | -7.9 | -19.8 |  |
| rlm_quiet | close | pin $2k+ | 73-97 | 42.9 | 4.6 | -1.8 |  |
| rlm_quiet | close | pin limit <$1k | 42-45 | 48.3 | -1.1 | -7.4 |  |
| pin_move | close | 1-3k bets | 386-388 | 49.9 | 0.2 | -2.6 |  |
| pin_move | close | 3k+ bets | 140-168 | 45.5 | -3.9 | -12.7 |  |
| pin_move | close | <1k bets | 77-79 | 49.4 | -1.3 | -5.4 |  |
| pin_move | close | pin $1-2k | 277-290 | 48.9 | -1.2 | -3.9 |  |
| pin_move | close | pin $2k+ | 221-241 | 47.8 | -1.5 | -9.1 |  |
| pin_move | close | pin limit <$1k | 105-104 | 50.2 | 0.6 | -1.8 |  |
| money_delta | close | 1-3k bets | 239-300 | 44.3 | -0.4 | -6.7 |  |
| money_delta | close | 3k+ bets | 92-123 | 42.8 | -0.7 | -3.5 |  |
| money_delta | close | <1k bets | 48-72 | 40.0 | -2.7 | -16.1 |  |
| money_delta | close | pin $1-2k | 137-130 | 51.3 | 5.1 | 7.3 |  |
| money_delta | close | pin $2k+ | 94-135 | 41.0 | -0.1 | -12.8 |  |
| money_delta | close | pin limit <$1k | 59-66 | 47.2 | -2.2 | -6.0 |  |
| pin_rlm | close | 1-3k bets | 102-119 | 46.2 | 3.8 | 11.0 |  |
| pin_rlm | close | 3k+ bets | 34-57 | 37.4 | -4.3 | -18.4 |  |
| pin_rlm | close | <1k bets | 22-24 | 47.8 | 6.2 | 5.5 |  |
| pin_rlm | close | pin $1-2k | 71-80 | 47.0 | 3.0 | 7.6 |  |
| pin_rlm | close | pin $2k+ | 43-82 | 34.4 | -0.9 | -10.2 |  |
| pin_rlm | close | pin limit <$1k | 44-38 | 53.7 | 4.9 | 13.8 |  |
| follow_move | close | 1-3k bets | 668-627 | 51.6 | 0.7 | -5.3 |  |
| follow_move | close | 3k+ bets | 227-223 | 50.4 | -1.0 | -7.8 |  |
| follow_move | close | <1k bets | 143-139 | 50.7 | -1.6 | -13.8 |  |
| follow_move | close | pin $1-2k | 315-357 | 46.9 | -3.7 | -11.8 |  |
| follow_move | close | pin $2k+ | 278-246 | 53.1 | 1.7 | -3.3 |  |
| follow_move | close | pin limit <$1k | 122-130 | 48.4 | -1.4 | -7.5 |  |
| rlm_ratio | close | 1-3k bets | 154-202 | 43.3 | -0.6 | -6.9 |  |
| rlm_ratio | close | 3k+ bets | 55-60 | 47.8 | 4.1 | 2.2 |  |
| rlm_ratio | close | <1k bets | 29-33 | 46.8 | 3.6 | -6.3 |  |
| rlm_ratio | close | pin $1-2k | 86-89 | 49.1 | 3.5 | 3.0 |  |
| rlm_ratio | close | pin $2k+ | 43-72 | 37.4 | -0.2 | -16.6 |  |
| rlm_ratio | close | pin limit <$1k | 49-45 | 52.1 | 3.0 | 0.6 |  |
| money_level | close | 1-3k bets | 844-621 | 57.6 | 2.1 | -3.0 |  |
| money_level | close | 3k+ bets | 300-239 | 55.7 | 0.6 | -3.7 |  |
| money_level | close | <1k bets | 183-129 | 58.7 | 3.0 | -4.5 |  |
| money_level | close | pin $1-2k | 388-338 | 53.4 | -0.3 | -4.8 |  |
| money_level | close | pin $2k+ | 351-272 | 56.3 | -1.1 | -6.9 |  |
| money_level | close | pin limit <$1k | 149-142 | 51.2 | 0.9 | -2.7 |  |
| sharp_gap | close | 1-3k bets | 640-761 | 45.7 | -1.8 | -8.9 |  |
| sharp_gap | close | 3k+ bets | 251-274 | 47.8 | 0.3 | -0.7 |  |
| sharp_gap | close | <1k bets | 139-157 | 47.0 | -1.0 | -11.1 |  |
| sharp_gap | close | pin $1-2k | 337-361 | 48.3 | -0.4 | -3.9 |  |
| sharp_gap | close | pin $2k+ | 273-327 | 45.5 | -1.0 | -6.0 |  |
| sharp_gap | close | pin limit <$1k | 130-149 | 46.6 | -2.9 | -7.5 |  |
| money_moving | close | 1-3k bets | 651-755 | 46.3 | -1.7 | -8.7 |  |
| money_moving | close | 3k+ bets | 249-277 | 47.3 | -0.5 | -2.5 |  |
| money_moving | close | <1k bets | 138-156 | 46.9 | -0.9 | -9.9 |  |
| money_moving | close | pin $1-2k | 336-363 | 48.1 | -0.9 | -4.4 |  |
| money_moving | close | pin $2k+ | 274-325 | 45.7 | -0.8 | -6.0 |  |
| money_moving | close | pin limit <$1k | 128-156 | 45.1 | -4.4 | -10.5 |  |
| pin_value | close | 1-3k bets | 290-281 | 50.8 | 2.6 | 4.2 |  |
| pin_value | close | 3k+ bets | 93-109 | 46.0 | -2.6 | -10.2 |  |
| pin_value | close | <1k bets | 65-51 | 56.0 | 8.6 | 14.5 |  |
| pin_value | close | pin $1-2k | 207-224 | 48.0 | -0.5 | -2.8 |  |
| pin_value | close | pin $2k+ | 125-143 | 46.6 | 0.1 | -0.7 |  |
| pin_value | close | pin limit <$1k | 116-74 | 61.1 | 11.1 | 18.1 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.3 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.3 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 268-315 | 46.0 | -3.1 | -9.1 |  |
| consensus_gap | close | 3k+ bets | 96-109 | 46.8 | -1.7 | 2.3 |  |
| consensus_gap | close | <1k bets | 55-81 | 40.4 | -5.1 | -19.2 |  |
| consensus_gap | close | pin $1-2k | 129-136 | 48.7 | -1.1 | 0.9 |  |
| consensus_gap | close | pin $2k+ | 123-122 | 50.2 | -0.8 | 0.4 |  |
| consensus_gap | close | pin limit <$1k | 58-46 | 55.8 | 5.6 | 8.5 |  |
| consensus_gap+follow_move | close | 1-3k bets | 102-97 | 51.3 | -0.3 | -3.4 |  |
| consensus_gap+money_level | close | 1-3k bets | 177-117 | 60.2 | 1.3 | 1.7 |  |
| consensus_gap+money_moving | close | 1-3k bets | 115-169 | 40.5 | -5.7 | -9.5 |  |
| consensus_gap+pin_move | close | 1-3k bets | 66-60 | 52.4 | 1.3 | 7.6 |  |
| consensus_gap+pin_value | close | 1-3k bets | 109-114 | 48.9 | 2.3 | 1.5 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 113-172 | 39.6 | -5.8 | -10.5 |  |
| follow_move+money_level | close | 1-3k bets | 425-308 | 58.0 | 2.1 | -4.2 |  |
| follow_move+money_moving | close | 1-3k bets | 361-396 | 47.7 | -1.3 | -8.4 |  |
| follow_move+pin_move | close | 1-3k bets | 276-296 | 48.3 | -1.5 | -7.5 |  |
| follow_move+pin_value | close | 1-3k bets | 95-91 | 51.1 | 2.3 | 2.0 |  |
| follow_move+sharp_gap | close | 1-3k bets | 364-398 | 47.8 | -0.9 | -7.5 |  |
| money_level+money_moving | close | 1-3k bets | 461-410 | 52.9 | 0.4 | -4.2 |  |
| money_level+pin_move | close | 1-3k bets | 225-202 | 52.7 | -0.1 | -4.0 |  |
| money_level+pin_value | close | 1-3k bets | 136-118 | 53.5 | 4.0 | 0.5 |  |
| money_level+sharp_gap | close | 1-3k bets | 444-403 | 52.4 | 0.3 | -4.1 |  |
| money_moving+pin_move | close | 1-3k bets | 226-244 | 48.1 | -0.7 | -3.2 |  |
| money_moving+pin_value | close | 1-3k bets | 121-144 | 45.7 | -2.1 | -6.6 |  |
| money_moving+sharp_gap | close | 1-3k bets | 615-725 | 45.9 | -1.7 | -8.2 |  |
| pin_move+pin_value | close | 1-3k bets | 124-115 | 51.9 | 2.5 | 1.3 |  |
| pin_move+sharp_gap | close | 1-3k bets | 231-248 | 48.2 | -0.3 | -2.6 |  |
| pin_value+sharp_gap | close | 1-3k bets | 122-146 | 45.5 | -2.0 | -7.0 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 162-239 | 40.4 | -1.5 | -7.5 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 80-144 | 35.7 | -5.4 | -15.6 |  |
| consensus_gap+money_delta | close | 1-3k bets | 31-68 | 31.3 | -7.2 | -19.4 |  |
| follow_move+money_delta | close | 1-3k bets | 118-144 | 45.0 | -1.3 | -10.2 |  |
| money_delta+money_level | close | 1-3k bets | 84-79 | 51.5 | 3.4 | 6.3 |  |
| money_delta+money_moving | close | 1-3k bets | 170-236 | 41.9 | -1.2 | -8.8 |  |
| money_delta+pin_value | close | 1-3k bets | 54-50 | 51.9 | 4.0 | 3.1 |  |
| money_delta+sharp_gap | close | 1-3k bets | 169-233 | 42.0 | -1.1 | -8.4 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 83-96 | 46.4 | -0.5 | -1.9 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 19-30 | 38.8 | -0.4 | 15.6 |  |
| money_level+pin_rlm | close | 1-3k bets | 45-32 | 58.4 | 10.3 | 12.9 |  |
| pin_move+pin_rlm | close | 1-3k bets | 94-98 | 49.0 | 4.9 | 9.3 |  |
| pin_rlm+pin_value | close | 1-3k bets | 31-28 | 52.5 | 5.9 | 23.8 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 102-119 | 46.2 | 3.8 | 11.0 |  |
| money_delta+pin_rlm | close | 1-3k bets | 57-66 | 46.3 | 3.6 | 8.6 |  |
| money_moving+pin_rlm | close | 1-3k bets | 97-112 | 46.4 | 3.9 | 12.6 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 23-35 | 39.7 | -0.5 | 3.7 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 154-202 | 43.3 | -0.6 | -6.9 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 83-102 | 44.9 | 0.1 | -9.0 |  |
| money_level+rlm_ratio | close | 1-3k bets | 70-66 | 51.5 | 2.5 | -0.6 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 148-193 | 43.4 | -0.6 | -6.3 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 81-86 | 48.5 | 3.4 | 1.4 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 29-25 | 53.7 | 5.5 | 2.9 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 154-202 | 43.3 | -0.6 | -6.9 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 16-39 | 29.1 | -7.0 | -12.4 |  |
| follow_move+pin_rlm | close | 1-3k bets | 75-93 | 44.6 | 1.0 | -6.0 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 73-138 | 34.6 | -6.6 | -17.2 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 75-103 | 42.1 | -1.9 | -9.2 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 31-60 | 34.1 | -5.7 | -19.8 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 75-93 | 44.6 | 1.0 | -6.0 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 64-122 | 34.4 | -5.4 | -15.4 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 44-79 | 35.8 | -7.5 | -24.5 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 20-28 | 41.7 | -4.6 | 1.0 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 50.3 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 36-32 | 52.9 | 2.7 | 0.7 |  |
| consensus_gap+money_moving | close | 3k+ bets | 38-62 | 38.0 | -7.3 | 6.1 |  |
| consensus_gap+pin_move | close | 3k+ bets | 29-24 | 54.7 | 4.9 | 7.2 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-9 | 25.0 | -14.3 | -20.4 |  |
| consensus_gap+pin_value | close | 3k+ bets | 40-37 | 51.9 | 5.4 | 5.7 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-9 | 30.8 | -9.4 | -11.6 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 39-61 | 39.0 | -5.9 | 10.0 |  |
| follow_move+money_moving | close | 3k+ bets | 119-134 | 47.0 | -2.0 | -8.3 |  |
| follow_move+pin_move | close | 3k+ bets | 106-125 | 45.9 | -3.8 | -11.4 |  |
| follow_move+pin_rlm | close | 3k+ bets | 32-42 | 43.2 | 0.0 | -4.8 |  |
| follow_move+pin_value | close | 3k+ bets | 37-42 | 46.8 | -3.1 | -11.9 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 55-60 | 47.8 | 4.1 | 2.2 |  |
| follow_move+sharp_gap | close | 3k+ bets | 122-133 | 47.8 | -0.8 | -5.8 |  |
| money_moving+pin_move | close | 3k+ bets | 77-106 | 42.1 | -5.7 | -16.7 |  |
| money_moving+pin_rlm | close | 3k+ bets | 33-56 | 37.1 | -4.3 | -18.8 |  |
| money_moving+pin_value | close | 3k+ bets | 47-62 | 43.1 | -4.8 | -12.6 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 52-58 | 47.3 | 3.5 | 0.8 |  |
| money_moving+sharp_gap | close | 3k+ bets | 242-266 | 47.6 | 0.0 | -1.3 |  |
| pin_move+pin_rlm | close | 3k+ bets | 32-51 | 38.6 | -4.4 | -15.7 |  |
| pin_move+pin_value | close | 3k+ bets | 39-53 | 42.4 | -7.0 | -20.1 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 34-44 | 43.6 | -0.9 | -5.5 |  |
| pin_move+sharp_gap | close | 3k+ bets | 77-106 | 42.1 | -5.4 | -16.2 |  |
| pin_rlm+pin_value | close | 3k+ bets | 6-16 | 27.3 | -19.3 | -48.0 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 32-42 | 43.2 | 0.0 | -4.8 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 34-57 | 37.4 | -4.3 | -18.4 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 9-11 | 45.0 | -5.2 | -14.6 |  |
| pin_value+sharp_gap | close | 3k+ bets | 47-61 | 43.5 | -4.4 | -11.8 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 55-60 | 47.8 | 4.1 | 2.2 |  |
| follow_move+money_delta | close | 3k+ bets | 44-56 | 44.0 | -1.2 | -9.5 |  |
| money_level+money_moving | close | 3k+ bets | 167-150 | 52.7 | 0.4 | -2.4 |  |
| money_level+sharp_gap | close | 3k+ bets | 166-146 | 53.2 | 1.2 | -0.8 |  |
| follow_move+money_level | close | 3k+ bets | 137-106 | 56.4 | -0.1 | -5.0 |  |
| money_level+rlm_ratio | close | 3k+ bets | 25-13 | 65.8 | 18.4 | 34.7 |  |
| consensus_gap+money_level | close | 3k+ bets | 57-52 | 52.3 | -5.0 | -11.1 |  |
| money_level+pin_move | close | 3k+ bets | 76-77 | 49.7 | -4.0 | -9.7 |  |
| money_level+pin_value | close | 3k+ bets | 54-56 | 49.1 | -1.3 | -8.8 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 8-16 | 33.3 | -4.9 | -17.2 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 57-88 | 39.3 | -3.2 | -15.9 |  |
| money_delta+money_moving | close | 3k+ bets | 70-95 | 42.4 | 0.0 | -0.1 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 23-39 | 37.1 | -3.4 | -15.4 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 29-49 | 37.2 | -4.5 | -18.0 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 26-48 | 35.1 | -6.7 | -22.4 |  |
| consensus_gap+money_delta | close | 3k+ bets | 13-24 | 35.1 | -4.0 | 17.2 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 14-32 | 30.4 | -12.5 | -35.1 |  |
| money_delta+sharp_gap | close | 3k+ bets | 68-92 | 42.5 | 0.2 | 0.5 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 31-52 | 37.3 | -6.0 | -19.8 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 11-28 | 28.2 | -12.4 | -33.0 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 8-17 | 32.0 | -17.1 | -38.8 |  |
| money_delta+money_level | close | 3k+ bets | 34-23 | 59.6 | 13.3 | 20.3 |  |
| money_level+pin_rlm | close | 3k+ bets | 16-9 | 64.0 | 18.8 | 37.0 |  |
| money_delta+pin_value | close | 3k+ bets | 19-20 | 48.7 | 2.2 | -8.1 |  |
| money_delta+pin_move | close | 3k+ bets | 38-50 | 43.2 | -2.1 | -12.0 |  |
| money_delta+pin_rlm | close | 3k+ bets | 22-32 | 40.7 | -1.0 | -13.3 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 31-30 | 50.8 | 6.8 | 7.4 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 47.3 | 87.7 |  |
| money_level+money_moving | close | <1k bets | 96-82 | 53.9 | 1.4 | -7.0 |  |
| money_level+sharp_gap | close | <1k bets | 98-82 | 54.4 | 1.7 | -6.6 |  |
| money_moving+sharp_gap | close | <1k bets | 134-153 | 46.7 | -1.1 | -10.7 |  |
| consensus_gap+money_level | close | <1k bets | 29-28 | 50.9 | -6.1 | -22.2 |  |
| consensus_gap+money_moving | close | <1k bets | 25-40 | 38.5 | -5.4 | -17.8 |  |
| consensus_gap+pin_move | close | <1k bets | 8-13 | 38.1 | -12.7 | -17.2 |  |
| consensus_gap+pin_value | close | <1k bets | 18-15 | 54.5 | 11.9 | 31.8 |  |
| consensus_gap+sharp_gap | close | <1k bets | 26-42 | 38.2 | -5.6 | -19.4 |  |
| money_level+pin_move | close | <1k bets | 40-38 | 51.3 | -2.8 | -9.3 |  |
| money_level+pin_value | close | <1k bets | 23-18 | 56.1 | 6.1 | 4.7 |  |
| money_moving+pin_move | close | <1k bets | 39-44 | 47.0 | -0.9 | -4.3 |  |
| money_moving+pin_value | close | <1k bets | 21-17 | 55.3 | 10.0 | 29.4 |  |
| pin_move+pin_value | close | <1k bets | 29-21 | 58.0 | 9.5 | 16.9 |  |
| pin_move+sharp_gap | close | <1k bets | 39-45 | 46.4 | -2.0 | -9.2 |  |
| pin_value+sharp_gap | close | <1k bets | 21-16 | 56.8 | 11.0 | 32.9 |  |
| follow_move+money_delta | close | <1k bets | 23-27 | 46.0 | 2.5 | -7.4 |  |
| follow_move+money_moving | close | <1k bets | 64-73 | 46.7 | -2.9 | -14.4 |  |
| follow_move+pin_move | close | <1k bets | 48-52 | 48.0 | -3.2 | -10.9 |  |
| follow_move+sharp_gap | close | <1k bets | 65-73 | 47.1 | -3.0 | -16.4 |  |
| money_delta+money_moving | close | <1k bets | 34-54 | 38.6 | -2.0 | -15.9 |  |
| money_delta+pin_move | close | <1k bets | 14-19 | 42.4 | -2.1 | -17.4 |  |
| money_delta+sharp_gap | close | <1k bets | 34-54 | 38.6 | -2.0 | -15.9 |  |
| follow_move+rlm_quiet | close | <1k bets | 26-45 | 36.6 | -4.9 | -23.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 29-33 | 46.8 | 3.6 | -6.3 |  |
| money_delta+rlm_quiet | close | <1k bets | 11-14 | 44.0 | 3.8 | -7.9 |  |
| money_delta+rlm_ratio | close | <1k bets | 19-20 | 48.7 | 6.4 | -0.8 |  |
| money_moving+rlm_quiet | close | <1k bets | 16-18 | 47.1 | 5.8 | 3.1 |  |
| money_moving+rlm_ratio | close | <1k bets | 29-33 | 46.8 | 3.6 | -6.3 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 12-15 | 44.4 | 4.4 | -7.6 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 15-19 | 44.1 | 2.2 | -9.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 29-33 | 46.8 | 3.6 | -6.3 |  |
| follow_move+money_level | close | <1k bets | 87-63 | 58.0 | 0.1 | -11.2 |  |
| consensus_gap+money_delta | close | <1k bets | 7-22 | 24.1 | -10.4 | -35.0 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -2.4 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 13-16 | 44.8 | 5.0 | -3.9 |  |
| money_moving+pin_rlm | close | <1k bets | 22-24 | 47.8 | 6.2 | 5.5 |  |
| pin_rlm+sharp_gap | close | <1k bets | 22-24 | 47.8 | 6.2 | 5.5 |  |
| money_delta+pin_value | close | <1k bets | 9-8 | 52.9 | 7.4 | 21.5 |  |
| consensus_gap+follow_move | close | <1k bets | 14-20 | 41.2 | -10.7 | -33.3 |  |
| follow_move+pin_rlm | close | <1k bets | 17-14 | 54.8 | 10.9 | 8.4 |  |
| follow_move+pin_value | close | <1k bets | 21-14 | 60.0 | 11.2 | 14.0 |  |
| pin_move+pin_rlm | close | <1k bets | 20-19 | 51.3 | 7.2 | 8.1 |  |
| pin_move+rlm_quiet | close | <1k bets | 12-14 | 46.2 | 0.5 | -1.0 |  |
| pin_move+rlm_ratio | close | <1k bets | 17-16 | 51.5 | 5.9 | 0.5 |  |
| pin_rlm+pin_value | close | <1k bets | 6-3 | 66.7 | 24.5 | 64.1 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 8-6 | 57.1 | 13.6 | 12.9 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 17-14 | 54.8 | 10.9 | 8.4 |  |
| pin_value+rlm_quiet | close | <1k bets | 5-4 | 55.6 | 6.3 | 6.5 |  |
| pin_value+rlm_ratio | close | <1k bets | 5-1 | 83.3 | 34.4 | 58.3 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -6.5 | -42.5 |  |
| money_delta+money_level | close | <1k bets | 14-18 | 43.8 | 0.4 | -12.1 |  |
| money_level+rlm_ratio | close | <1k bets | 14-14 | 50.0 | 4.5 | -2.1 |  |
| money_level+pin_rlm | close | <1k bets | 9-7 | 56.2 | 13.3 | 11.6 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-5 | 16.7 | -21.8 | -68.2 |  |
| consensus_gap+follow_move | close | pin $1-2k | 48-54 | 47.1 | -5.0 | -10.7 |  |
| consensus_gap+money_moving | close | pin $1-2k | 59-72 | 45.0 | -3.6 | -3.4 |  |
| consensus_gap+pin_move | close | pin $1-2k | 48-49 | 49.5 | -2.3 | 5.3 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-19 | 40.6 | -1.0 | 21.9 |  |
| consensus_gap+pin_value | close | pin $1-2k | 76-78 | 49.4 | 2.8 | 0.4 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-16 | 46.7 | 1.3 | 1.7 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 57-69 | 45.2 | -2.6 | -1.5 |  |
| follow_move+money_moving | close | pin $1-2k | 183-220 | 45.4 | -4.0 | -10.9 |  |
| follow_move+pin_move | close | pin $1-2k | 192-227 | 45.8 | -4.3 | -11.3 |  |
| follow_move+pin_rlm | close | pin $1-2k | 58-63 | 47.9 | 2.2 | 1.7 |  |
| follow_move+pin_value | close | pin $1-2k | 70-82 | 46.1 | -3.5 | -13.0 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 86-89 | 49.1 | 3.5 | 3.0 |  |
| follow_move+sharp_gap | close | pin $1-2k | 188-220 | 46.1 | -3.2 | -10.1 |  |
| money_moving+pin_move | close | pin $1-2k | 165-188 | 46.7 | -2.4 | -5.1 |  |
| money_moving+pin_rlm | close | pin $1-2k | 68-74 | 47.9 | 3.3 | 10.0 |  |
| money_moving+pin_value | close | pin $1-2k | 80-110 | 42.1 | -5.9 | -16.2 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 84-83 | 50.3 | 4.2 | 5.3 |  |
| money_moving+sharp_gap | close | pin $1-2k | 323-348 | 48.1 | -0.6 | -3.8 |  |
| pin_move+pin_rlm | close | pin $1-2k | 68-72 | 48.6 | 3.3 | 8.9 |  |
| pin_move+pin_value | close | pin $1-2k | 86-101 | 46.0 | -3.7 | -11.5 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 66-66 | 50.0 | 3.1 | 4.4 |  |
| pin_move+sharp_gap | close | pin $1-2k | 168-191 | 46.8 | -2.1 | -5.3 |  |
| pin_rlm+pin_value | close | pin $1-2k | 18-28 | 39.1 | -9.4 | -19.5 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 58-63 | 47.9 | 2.2 | 1.7 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 71-80 | 47.0 | 3.0 | 7.6 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 20-24 | 45.5 | -4.2 | -14.2 |  |
| pin_value+sharp_gap | close | pin $1-2k | 80-107 | 42.8 | -5.1 | -14.9 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 86-89 | 49.1 | 3.5 | 3.0 |  |
| follow_move+money_level | close | pin $1-2k | 205-196 | 51.1 | -2.8 | -9.9 |  |
| money_level+rlm_ratio | close | pin $1-2k | 47-35 | 57.3 | 9.4 | 11.7 |  |
| money_level+sharp_gap | close | pin $1-2k | 238-225 | 51.4 | -0.2 | -4.7 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 4-15 | 21.1 | -19.9 | -39.5 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 66-118 | 35.9 | -7.9 | -19.8 |  |
| money_level+money_moving | close | pin $1-2k | 240-229 | 51.2 | -0.7 | -5.5 |  |
| consensus_gap+money_level | close | pin $1-2k | 75-66 | 53.2 | -3.5 | -6.5 |  |
| money_level+pin_value | close | pin $1-2k | 91-91 | 50.0 | 0.1 | -6.4 |  |
| money_level+pin_move | close | pin $1-2k | 159-157 | 50.3 | -2.2 | -8.0 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 33-52 | 38.8 | -5.4 | -7.4 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 47-73 | 39.2 | -6.6 | -12.1 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 20-39 | 33.9 | -10.3 | -17.7 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 27-46 | 37.0 | -6.2 | -10.6 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 34-56 | 37.8 | -6.0 | -12.0 |  |
| money_level+pin_rlm | close | pin $1-2k | 33-23 | 58.9 | 12.4 | 15.7 |  |
| follow_move+money_delta | close | pin $1-2k | 70-70 | 50.0 | 3.4 | 1.9 |  |
| money_delta+money_moving | close | pin $1-2k | 91-98 | 48.1 | 3.6 | 4.8 |  |
| money_delta+pin_move | close | pin $1-2k | 68-71 | 48.9 | 1.4 | 2.7 |  |
| money_delta+pin_rlm | close | pin $1-2k | 43-45 | 48.9 | 5.0 | 10.7 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 51-45 | 53.1 | 7.4 | 10.5 |  |
| money_delta+sharp_gap | close | pin $1-2k | 91-96 | 48.7 | 4.1 | 5.9 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 47.3 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 46-38 | 54.8 | 6.9 | 6.6 |  |
| consensus_gap+money_delta | close | pin $1-2k | 19-26 | 42.2 | 0.4 | 4.5 |  |
| money_delta+pin_value | close | pin $1-2k | 44-45 | 49.4 | 1.1 | -2.4 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 22-37 | 37.3 | -7.5 | -16.9 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 13-31 | 29.5 | -19.8 | -43.2 |  |
| consensus_gap+follow_move | close | pin $2k+ | 39-32 | 54.9 | 2.2 | -6.2 |  |
| consensus_gap+money_delta | close | pin $2k+ | 9-27 | 25.0 | -9.4 | -51.2 |  |
| consensus_gap+money_level | close | pin $2k+ | 83-58 | 58.9 | -3.6 | -7.9 |  |
| consensus_gap+money_moving | close | pin $2k+ | 44-73 | 37.6 | -7.8 | -5.6 |  |
| consensus_gap+pin_move | close | pin $2k+ | 38-36 | 51.4 | 1.2 | -3.8 |  |
| consensus_gap+pin_value | close | pin $2k+ | 48-54 | 47.1 | 4.0 | 9.0 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 2-15 | 11.8 | -20.6 | -69.1 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 46-76 | 37.7 | -8.0 | -5.2 |  |
| follow_move+money_delta | close | pin $2k+ | 36-52 | 40.9 | -0.7 | -15.6 |  |
| follow_move+money_level | close | pin $2k+ | 163-107 | 60.4 | 0.9 | -3.2 |  |
| follow_move+money_moving | close | pin $2k+ | 127-138 | 47.9 | 0.1 | -8.3 |  |
| follow_move+pin_move | close | pin $2k+ | 168-171 | 49.6 | -0.2 | -6.6 |  |
| follow_move+pin_value | close | pin $2k+ | 39-38 | 50.6 | 3.0 | 8.3 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 43-72 | 37.4 | -0.2 | -16.6 |  |
| follow_move+sharp_gap | close | pin $2k+ | 128-139 | 47.9 | 0.2 | -8.0 |  |
| money_delta+money_level | close | pin $2k+ | 29-23 | 55.8 | 11.4 | 13.4 |  |
| money_delta+money_moving | close | pin $2k+ | 67-103 | 39.4 | 0.6 | -13.2 |  |
| money_delta+pin_move | close | pin $2k+ | 36-57 | 38.7 | -3.4 | -20.7 |  |
| money_delta+pin_value | close | pin $2k+ | 20-24 | 45.5 | 1.4 | -13.3 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 22-37 | 37.3 | -0.9 | -19.7 |  |
| money_delta+sharp_gap | close | pin $2k+ | 65-102 | 38.9 | 0.0 | -14.1 |  |
| money_level+money_moving | close | pin $2k+ | 184-172 | 51.7 | -1.2 | -6.1 |  |
| money_level+pin_move | close | pin $2k+ | 121-103 | 54.0 | -1.8 | -5.5 |  |
| money_level+pin_value | close | pin $2k+ | 64-64 | 50.0 | 0.3 | -7.5 |  |
| money_level+rlm_ratio | close | pin $2k+ | 16-15 | 51.6 | 5.7 | 7.7 |  |
| money_level+sharp_gap | close | pin $2k+ | 184-173 | 51.5 | -1.4 | -6.1 |  |
| money_moving+pin_move | close | pin $2k+ | 110-132 | 45.5 | -1.2 | -9.4 |  |
| money_moving+pin_value | close | pin $2k+ | 64-81 | 44.1 | -1.7 | -1.6 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 43-71 | 37.7 | 0.1 | -15.9 |  |
| money_moving+sharp_gap | close | pin $2k+ | 268-321 | 45.5 | -0.9 | -5.9 |  |
| pin_move+pin_value | close | pin $2k+ | 56-57 | 49.6 | 1.5 | -3.4 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 31-50 | 38.3 | -0.2 | -12.3 |  |
| pin_move+sharp_gap | close | pin $2k+ | 110-133 | 45.3 | -1.4 | -9.5 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 5-7 | 41.7 | -1.6 | -17.1 |  |
| pin_value+sharp_gap | close | pin $2k+ | 64-82 | 43.8 | -1.9 | -2.3 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 43-72 | 37.4 | -0.2 | -16.6 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 5-23 | 17.9 | -13.3 | -26.1 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 6-16 | 27.3 | -2.7 | -37.1 |  |
| follow_move+pin_rlm | close | pin $2k+ | 31-56 | 35.6 | -0.8 | -17.7 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 73-97 | 42.9 | 4.6 | -1.8 |  |
| money_moving+pin_rlm | close | pin $2k+ | 43-82 | 34.4 | -0.9 | -10.2 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 30-54 | 35.7 | 0.3 | -18.8 |  |
| pin_move+pin_rlm | close | pin $2k+ | 35-58 | 37.6 | 0.8 | -11.3 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 47-70 | 40.2 | 0.2 | -12.6 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 15-41 | 26.8 | -5.4 | -33.0 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 31-56 | 35.6 | -0.8 | -17.7 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 43-82 | 34.4 | -0.9 | -10.2 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 22-48 | 31.4 | -1.1 | -25.1 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 30-55 | 35.3 | -0.1 | -19.8 |  |
| money_delta+pin_rlm | close | pin $2k+ | 23-46 | 33.3 | -2.0 | -18.1 |  |
| money_level+pin_rlm | close | pin $2k+ | 16-10 | 61.5 | 18.1 | 30.4 |  |
| pin_rlm+pin_value | close | pin $2k+ | 6-13 | 31.6 | -5.2 | 13.6 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 19-31 | 38.0 | -0.2 | -21.6 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 6-10 | 37.5 | -1.6 | 35.0 |  |
| follow_move+money_delta | close | pin limit <$1k | 35-46 | 43.2 | -6.1 | -17.0 |  |
| money_level+money_moving | close | pin limit <$1k | 79-92 | 46.2 | -3.6 | -11.5 |  |
| money_level+sharp_gap | close | pin limit <$1k | 76-86 | 46.9 | -2.8 | -10.0 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 119-140 | 45.9 | -3.5 | -8.4 |  |
| consensus_gap+money_level | close | pin limit <$1k | 32-26 | 55.2 | 4.5 | 2.2 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 17-12 | 58.6 | 10.2 | 25.7 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 43-34 | 55.8 | 6.2 | 10.9 |  |
| follow_move+money_moving | close | pin limit <$1k | 73-93 | 44.0 | -5.4 | -15.5 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 78-92 | 45.9 | -3.5 | -11.9 |  |
| money_level+pin_move | close | pin limit <$1k | 61-57 | 51.7 | 1.8 | -1.4 |  |
| money_level+pin_value | close | pin limit <$1k | 58-37 | 61.1 | 11.0 | 15.5 |  |
| pin_move+pin_value | close | pin limit <$1k | 50-31 | 61.7 | 11.9 | 22.8 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 22-12 | 64.7 | 15.2 | 19.8 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 26-20 | 56.5 | 7.6 | 16.6 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 28-20 | 58.3 | 9.3 | 19.6 |  |
| follow_move+money_level | close | pin limit <$1k | 63-68 | 48.1 | -2.1 | -8.4 |  |
| follow_move+pin_move | close | pin limit <$1k | 70-75 | 48.3 | -1.3 | -7.5 |  |
| follow_move+pin_value | close | pin limit <$1k | 44-27 | 62.0 | 12.2 | 17.6 |  |
| money_moving+pin_move | close | pin limit <$1k | 67-74 | 47.5 | -1.9 | -6.0 |  |
| money_moving+pin_value | close | pin limit <$1k | 45-32 | 58.4 | 8.8 | 16.7 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 69-75 | 47.9 | -1.5 | -5.2 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 46-34 | 57.5 | 7.8 | 14.7 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 42-45 | 48.3 | -1.1 | -7.4 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 27-32 | 45.8 | -3.4 | -12.2 |  |
| money_delta+money_moving | close | pin limit <$1k | 51-55 | 48.1 | -1.1 | -3.6 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 10-7 | 58.8 | 11.6 | 37.6 |  |
| money_delta+money_level | close | pin limit <$1k | 26-23 | 53.1 | 3.3 | 1.7 |  |
| money_delta+pin_value | close | pin limit <$1k | 18-9 | 66.7 | 17.5 | 43.1 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 50-53 | 48.5 | -0.7 | -2.7 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 31-37 | 45.6 | -3.4 | -6.0 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 7-4 | 63.6 | 17.6 | 61.2 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 26-23 | 53.1 | 4.6 | 11.0 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 41-36 | 53.2 | 4.6 | 13.7 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 43-38 | 53.1 | 4.1 | 7.3 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-6 | 76.0 | 27.0 | 62.7 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 44-38 | 53.7 | 4.9 | 13.8 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 7-2 | 77.8 | 30.4 | 48.7 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 14-8 | 63.6 | 13.8 | 21.7 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 11-20 | 35.5 | -13.0 | -31.8 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 24-26 | 48.0 | -1.1 | -7.7 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 35-30 | 53.8 | 4.7 | 3.7 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 49-45 | 52.1 | 3.0 | 0.6 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 29-29 | 50.0 | 0.9 | -3.8 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 21-31 | 40.4 | -8.6 | -22.4 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 45-43 | 51.1 | 2.1 | -1.2 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 35-30 | 53.8 | 4.7 | 3.7 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 15-14 | 51.7 | 3.4 | -0.5 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 35-30 | 53.8 | 4.7 | 3.7 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 23-24 | 48.9 | 0.0 | -6.1 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 49-45 | 52.1 | 3.0 | 0.6 |  |
| money_level+pin_rlm | close | pin limit <$1k | 21-15 | 58.3 | 8.6 | 12.0 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 23-18 | 56.1 | 6.8 | 9.1 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 18-6 | 75.0 | 25.1 | 43.5 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 7-4 | 63.6 | 15.6 | 21.7 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 50.3 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.2 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -51.5 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 39-48 | 44.8 | 8.4 | 10.2 | 0.6 |
| rlm_quiet | early | pin $1-2k | 2-6 | 25.0 | -6.0 | 1.5 | -0.43 |
| rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| rlm_quiet | early | pin limit <$1k | 5-8 | 38.5 | -6.2 | -21.5 | 0.25 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.3 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 9-14 | 39.1 | -9.6 | -28.1 | 0.31 |
| pin_move | early | pin $1-2k | 0-5 | 0.0 | -40.6 | -100.0 | 0.14 |
| pin_move | early | pin limit <$1k | 9-10 | 47.4 | -3.5 | -13.0 | 0.28 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.6 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 12-9 | 57.1 | 17.8 | 34.3 | 0.8 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -40.3 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 5-0 | 100.0 | 50.7 | 88.6 | 0.0 |
| pin_rlm | early | <1k bets | 1-3 | 25.0 | -14.0 | -51.8 | -0.37 |
| pin_rlm | early | pin $1-2k | 0-3 | 0.0 | -42.7 | -100.0 | -0.67 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.5 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -51.5 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 500-447 | 52.8 | 1.4 | -6.3 | 0.16 |
| follow_move | early | pin $1-2k | 36-25 | 59.0 | 8.3 | 8.9 | -0.26 |
| follow_move | early | pin $2k+ | 0-2 | 0.0 | -40.3 | -100.0 | 0.65 |
| follow_move | early | pin limit <$1k | 53-47 | 53.0 | 3.0 | 0.0 | -0.16 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.1 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.7 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 30-24 | 55.6 | 16.7 | 25.8 | 0.76 |
| rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.2 | 29.7 | -1.02 |
| rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.3 | -100.0 | 0.65 |
| rlm_ratio | early | pin limit <$1k | 8-1 | 88.9 | 43.9 | 79.0 | 0.37 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 1.4 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 43.6 | 59.7 | 0.33 |
| money_level | early | <1k bets | 181-122 | 59.7 | 0.3 | -6.1 | -0.22 |
| money_level | early | pin $1-2k | 22-10 | 68.8 | 3.8 | 2.2 | -0.01 |
| money_level | early | pin $2k+ | 1-1 | 50.0 | -12.4 | -47.2 | -0.7 |
| money_level | early | pin limit <$1k | 26-28 | 48.1 | -4.7 | -10.9 | 0.3 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.3 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.5 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 145-135 | 51.8 | 3.6 | 1.2 | 0.4 |
| sharp_gap | early | pin $1-2k | 17-13 | 56.7 | 2.0 | 4.4 | -0.36 |
| sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.3 | -100.0 | 0.65 |
| sharp_gap | early | pin limit <$1k | 31-20 | 60.8 | 12.1 | 25.3 | 0.17 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.5 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 51.5 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 104-98 | 51.5 | 1.1 | -7.5 | 0.13 |
| money_moving | early | pin $1-2k | 8-10 | 44.4 | -13.8 | -39.0 | 0.28 |
| money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.4 | -8.4 | 0.65 |
| money_moving | early | pin limit <$1k | 25-10 | 71.4 | 22.3 | 49.9 | 0.39 |
| pin_value | early | 1-3k bets | 13-10 | 56.5 | 8.2 | 6.3 | -0.04 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.7 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 47-51 | 48.0 | -0.9 | -9.3 | 0.09 |
| pin_value | early | pin $1-2k | 16-26 | 38.1 | -8.8 | -28.4 | 0.08 |
| pin_value | early | pin $2k+ | 1-0 | 100.0 | 52.7 | 83.3 | 0.0 |
| pin_value | early | pin limit <$1k | 44-35 | 55.7 | 6.0 | 5.4 | 0.07 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -50.3 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -27.0 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.2 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.4 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 241-279 | 46.3 | -2.4 | -10.0 | 0.4 |
| consensus_gap | early | pin $1-2k | 18-23 | 43.9 | -2.5 | -17.8 | 0.2 |
| consensus_gap | early | pin $2k+ | 1-1 | 50.0 | 12.4 | -8.4 | 0.65 |
| consensus_gap | early | pin limit <$1k | 22-35 | 38.6 | -11.5 | -21.2 | 0.31 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -52.7 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.6 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.6 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -1.5 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.6 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 5.2 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.2 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 7-4 | 63.6 | 14.2 | 19.4 | -0.09 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.2 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.8 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.3 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -0.8 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 6-5 | 54.5 | 8.2 | 1.3 | 0.27 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -1.1 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-7 | 50.0 | 2.8 | -6.4 | -0.29 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.2 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.5 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -20.4 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.9 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 3.3 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.5 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.1 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.5 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.1 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.2 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.4 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 52.7 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 11.6 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 18.3 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 16.5 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 16.5 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.7 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.7 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.7 | 83.3 | 1.0 |
| follow_move+rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -51.5 | -100.0 | -0.5 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.7 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.7 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 51.5 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.7 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.7 | 83.3 | 1.0 |
| rlm_quiet+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.7 | -100.0 | -1.0 |
| rlm_quiet+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.7 | -100.0 | -1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.7 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 39.1 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 50.3 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 34-38 | 47.2 | -5.3 | -16.0 | 0.79 |
| consensus_gap+money_level | early | <1k bets | 40-30 | 57.1 | -6.6 | -11.8 | 0.09 |
| consensus_gap+sharp_gap | early | <1k bets | 29-43 | 40.3 | -6.8 | -15.9 | 0.83 |
| follow_move+money_level | early | <1k bets | 90-43 | 67.7 | 6.6 | -0.5 | 0.09 |
| follow_move+sharp_gap | early | <1k bets | 76-44 | 63.3 | 13.7 | 15.4 | 0.66 |
| money_level+sharp_gap | early | <1k bets | 96-65 | 59.6 | 3.6 | -1.8 | 0.13 |
| follow_move+money_moving | early | <1k bets | 54-36 | 60.0 | 7.9 | 7.8 | 0.44 |
| money_level+money_moving | early | <1k bets | 62-45 | 57.9 | -0.0 | -7.1 | -0.18 |
| money_moving+sharp_gap | early | <1k bets | 63-59 | 51.6 | 3.8 | -2.3 | 0.39 |
| consensus_gap+money_moving | early | <1k bets | 14-22 | 38.9 | -9.8 | -38.1 | 0.35 |
| follow_move+pin_value | early | <1k bets | 16-14 | 53.3 | 3.8 | 0.1 | -0.18 |
| follow_move+rlm_quiet | early | <1k bets | 39-48 | 44.8 | 8.4 | 10.2 | 0.6 |
| money_moving+rlm_quiet | early | <1k bets | 16-15 | 51.6 | 14.6 | 28.9 | 0.67 |
| rlm_quiet+sharp_gap | early | <1k bets | 22-19 | 53.7 | 16.7 | 25.2 | 0.23 |
| follow_move+rlm_ratio | early | <1k bets | 30-24 | 55.6 | 16.7 | 25.8 | 0.76 |
| rlm_quiet+rlm_ratio | early | <1k bets | 20-15 | 57.1 | 20.6 | 35.7 | 0.3 |
| rlm_ratio+sharp_gap | early | <1k bets | 30-24 | 55.6 | 16.7 | 25.8 | 0.76 |
| pin_move+pin_value | early | <1k bets | 3-9 | 25.0 | -24.2 | -52.3 | 0.33 |
| follow_move+pin_move | early | <1k bets | 6-6 | 50.0 | -0.9 | -9.9 | 0.45 |
| consensus_gap+pin_value | early | <1k bets | 18-24 | 42.9 | -4.3 | -19.6 | 0.34 |
| pin_value+rlm_quiet | early | <1k bets | 0-3 | 0.0 | -43.5 | -100.0 | -0.6 |
| money_delta+money_moving | early | <1k bets | 11-9 | 55.0 | 16.1 | 31.5 | 0.83 |
| money_delta+sharp_gap | early | <1k bets | 10-7 | 58.8 | 20.6 | 43.4 | 0.98 |
| consensus_gap+pin_move | early | <1k bets | 1-5 | 16.7 | -28.8 | -68.2 | 0.22 |
| money_level+pin_move | early | <1k bets | 3-3 | 50.0 | -3.8 | -16.0 | 0.57 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -28.0 | -100.0 | -4.8 |
| consensus_gap+rlm_quiet | early | <1k bets | 3-5 | 37.5 | -1.3 | -22.7 | 1.01 |
| consensus_gap+rlm_ratio | early | <1k bets | 5-3 | 62.5 | 21.0 | 25.0 | 0.65 |
| follow_move+pin_rlm | early | <1k bets | 1-2 | 33.3 | -9.3 | -35.8 | -0.93 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -28.0 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | <1k bets | 0-1 | 0.0 | -28.0 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-2 | 33.3 | -9.3 | -35.8 | -0.93 |
| pin_rlm+sharp_gap | early | <1k bets | 1-3 | 25.0 | -14.0 | -51.8 | -0.37 |
| pin_value+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 24.2 | 27.3 | -0.93 |
| pin_value+sharp_gap | early | <1k bets | 6-6 | 50.0 | 0.2 | -4.5 | 0.41 |
| money_level+pin_value | early | <1k bets | 6-6 | 50.0 | -1.9 | -4.5 | 1.06 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -51.2 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -49.7 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 2-3 | 40.0 | -14.9 | -23.6 | 1.34 |
| money_level+rlm_ratio | early | <1k bets | 8-9 | 47.1 | 4.8 | -2.4 | 1.85 |
| money_moving+rlm_ratio | early | <1k bets | 16-10 | 61.5 | 21.0 | 45.3 | 0.82 |
| consensus_gap+money_delta | early | <1k bets | 2-0 | 100.0 | 50.0 | 90.9 | 0.5 |
| money_delta+money_level | early | <1k bets | 4-3 | 57.1 | 13.6 | 19.5 | 1.43 |
| pin_move+sharp_gap | early | <1k bets | 2-2 | 50.0 | -0.1 | -21.7 | 0.7 |
| money_level+pin_rlm | early | <1k bets | 1-1 | 50.0 | 0.0 | -3.7 | 1.0 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 6-4 | 60.0 | 21.2 | 68.1 | 0.98 |
| money_delta+rlm_quiet | early | <1k bets | 3-2 | 60.0 | 27.7 | 107.0 | -0.4 |
| money_delta+rlm_ratio | early | <1k bets | 5-2 | 71.4 | 34.2 | 112.8 | 1.71 |
| money_delta+pin_value | early | <1k bets | 2-0 | 100.0 | 50.3 | 90.9 | 0.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 6-4 | 60.0 | -4.6 | -4.6 | 0.25 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -30.5 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 7-11 | 38.9 | -3.9 | -28.1 | 0.15 |
| follow_move+rlm_quiet | early | pin $1-2k | 2-6 | 25.0 | -6.0 | 1.5 | -0.43 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.2 | 29.7 | -1.02 |
| follow_move+sharp_gap | early | pin $1-2k | 9-5 | 64.3 | 8.0 | 27.7 | -0.66 |
| money_level+money_moving | early | pin $1-2k | 8-6 | 57.1 | -8.2 | -21.6 | 0.19 |
| money_level+pin_value | early | pin $1-2k | 2-4 | 33.3 | -19.0 | -37.6 | 0.78 |
| money_moving+pin_value | early | pin $1-2k | 1-3 | 25.0 | -30.4 | -54.2 | 0.93 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -9.1 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -9.1 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -10.2 | 29.7 | -1.02 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -52.7 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -40.3 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -52.7 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -40.3 | -100.0 | 2.5 |
| money_level+sharp_gap | early | pin $1-2k | 14-6 | 70.0 | 5.7 | 7.8 | -0.25 |
| money_moving+sharp_gap | early | pin $1-2k | 4-7 | 36.4 | -21.4 | -50.4 | 0.23 |
| pin_value+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -25.0 | -52.3 | -0.52 |
| consensus_gap+follow_move | early | pin $1-2k | 5-6 | 45.5 | -2.5 | -18.8 | 0.45 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 0-3 | 0.0 | -28.0 | -100.0 | -0.97 |
| follow_move+pin_value | early | pin $1-2k | 6-7 | 46.2 | -1.5 | -14.7 | -0.25 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -28.0 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 11-5 | 68.8 | 4.1 | -0.1 | 0.03 |
| money_level+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -12.4 | -1.0 | 0.75 |
| follow_move+money_moving | early | pin $1-2k | 4-2 | 66.7 | 2.5 | -10.9 | -0.15 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -28.0 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -28.0 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 3-4 | 42.9 | -10.3 | -30.6 | -0.66 |
| follow_move+pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -28.0 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | pin $1-2k | 0-1 | 0.0 | -28.0 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-3 | 0.0 | -42.7 | -100.0 | -0.67 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -28.0 | -100.0 | -4.8 |
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -28.0 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| pin_move+pin_value | early | pin $1-2k | 0-2 | 0.0 | -47.3 | -100.0 | 0.0 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -72.0 | -100.0 | 1.5 |
| follow_move+pin_move | early | pin $1-2k | 0-1 | 0.0 | -47.3 | -100.0 | 0.0 |
| consensus_gap+money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.4 | -8.4 | 0.65 |
| consensus_gap+pin_value | early | pin $2k+ | 1-0 | 100.0 | 52.7 | 83.3 | 0.0 |
| follow_move+money_level | early | pin $2k+ | 0-1 | 0.0 | -52.7 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.3 | -100.0 | 0.65 |
| follow_move+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.3 | -100.0 | 0.65 |
| money_level+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -52.7 | -100.0 | 0.0 |
| money_level+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -52.7 | -100.0 | 0.0 |
| money_moving+pin_value | early | pin $2k+ | 1-0 | 100.0 | 52.7 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.3 | -100.0 | 0.65 |
| consensus_gap+follow_move | early | pin $2k+ | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| consensus_gap+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| consensus_gap+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| consensus_gap+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| follow_move+money_moving | early | pin $2k+ | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| money_moving+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| money_moving+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| money_moving+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| rlm_quiet+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| rlm_quiet+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin limit <$1k | 5-8 | 38.5 | -6.2 | -21.5 | 0.25 |
| money_level+money_moving | early | pin limit <$1k | 14-7 | 66.7 | 14.8 | 23.6 | 0.5 |
| money_level+sharp_gap | early | pin limit <$1k | 21-17 | 55.3 | 4.8 | 1.3 | 0.24 |
| money_moving+sharp_gap | early | pin limit <$1k | 20-6 | 76.9 | 28.7 | 65.2 | 0.31 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -50.3 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 11-7 | 61.1 | 11.2 | 16.0 | 0.5 |
| money_moving+pin_value | early | pin limit <$1k | 8-4 | 66.7 | 17.0 | 26.0 | 0.25 |
| pin_value+sharp_gap | early | pin limit <$1k | 13-7 | 65.0 | 15.2 | 23.3 | 0.2 |
| consensus_gap+follow_move | early | pin limit <$1k | 7-9 | 43.8 | -7.9 | -18.4 | 0.56 |
| consensus_gap+money_level | early | pin limit <$1k | 5-7 | 41.7 | -13.4 | -28.1 | 0.42 |
| consensus_gap+pin_value | early | pin limit <$1k | 17-18 | 48.6 | -0.5 | -8.6 | 0.45 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 7-4 | 63.6 | 18.2 | 56.6 | 0.91 |
| follow_move+money_level | early | pin limit <$1k | 12-11 | 52.2 | -1.2 | -3.2 | 0.01 |
| follow_move+pin_value | early | pin limit <$1k | 17-14 | 54.8 | 5.5 | 3.4 | -0.19 |
| follow_move+sharp_gap | early | pin limit <$1k | 14-8 | 63.6 | 15.1 | 21.5 | -0.02 |
| follow_move+rlm_ratio | early | pin limit <$1k | 8-1 | 88.9 | 43.9 | 79.0 | 0.37 |
| money_level+rlm_ratio | early | pin limit <$1k | 7-0 | 100.0 | 53.3 | 92.4 | 0.5 |
| pin_value+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.1 | 43.2 | -0.25 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 8-1 | 88.9 | 43.9 | 79.0 | 0.37 |
| consensus_gap+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 50.9 | 87.1 | 0.33 |
| consensus_gap+money_moving | early | pin limit <$1k | 8-3 | 72.7 | 25.2 | 74.0 | 0.58 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 1.5 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 50.9 | 87.1 | 0.33 |
| follow_move+money_moving | early | pin limit <$1k | 10-4 | 71.4 | 22.1 | 36.5 | 0.36 |
| money_delta+money_moving | early | pin limit <$1k | 4-0 | 100.0 | 50.7 | 88.0 | 0.0 |
| money_delta+pin_value | early | pin limit <$1k | 4-0 | 100.0 | 50.7 | 88.0 | 0.0 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 3-2 | 60.0 | 10.7 | 13.0 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 30.1 | 54.4 | -0.2 |
| money_delta+sharp_gap | early | pin limit <$1k | 3-0 | 100.0 | 50.1 | 89.6 | 0.0 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 10.9 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | 5.6 | 13.7 | -0.05 |
| pin_move+pin_value | early | pin limit <$1k | 3-7 | 30.0 | -19.6 | -42.7 | 0.4 |
| follow_move+pin_move | early | pin limit <$1k | 6-5 | 54.5 | 3.4 | -1.7 | 0.49 |
| consensus_gap+pin_move | early | pin limit <$1k | 1-3 | 25.0 | -29.2 | -52.3 | 0.4 |
| money_level+pin_move | early | pin limit <$1k | 3-3 | 50.0 | -3.8 | -16.0 | 0.57 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -49.7 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -49.7 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | -0.1 | -21.7 | 0.7 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 2-0 | 100.0 | 50.3 | 90.9 | 0.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 50.3 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 50.3 | 90.9 | 1.0 |
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
| rlm_quiet | close | 1-3k bets | 46-71 | 39.3 | -3.3 | -6.7 |  |
| rlm_quiet | close | 3k+ bets | 13-28 | 31.7 | -11.5 | -35.6 |  |
| rlm_quiet | close | <1k bets | 4-17 | 19.0 | -23.2 | -63.3 |  |
| rlm_quiet | close | pin $1-2k | 20-37 | 35.1 | -9.7 | -25.3 |  |
| rlm_quiet | close | pin $2k+ | 20-34 | 37.0 | -4.2 | -2.3 |  |
| rlm_quiet | close | pin limit <$1k | 6-9 | 40.0 | -6.7 | -22.5 |  |
| pin_move | close | 1-3k bets | 78-82 | 48.8 | -0.5 | -3.8 |  |
| pin_move | close | 3k+ bets | 19-42 | 31.1 | -17.9 | -42.6 |  |
| pin_move | close | <1k bets | 10-11 | 47.6 | -3.6 | -10.9 |  |
| pin_move | close | pin $1-2k | 45-61 | 42.5 | -6.7 | -14.8 |  |
| pin_move | close | pin $2k+ | 45-54 | 45.5 | -4.0 | -14.4 |  |
| pin_move | close | pin limit <$1k | 17-20 | 45.9 | -3.5 | -12.1 |  |
| money_delta | close | 1-3k bets | 40-49 | 44.9 | 1.3 | -9.0 |  |
| money_delta | close | 3k+ bets | 13-14 | 48.1 | 4.1 | -4.5 |  |
| money_delta | close | <1k bets | 10-10 | 50.0 | 5.6 | 17.9 |  |
| money_delta | close | pin $1-2k | 25-15 | 62.5 | 16.3 | 29.9 |  |
| money_delta | close | pin $2k+ | 12-23 | 34.3 | -5.7 | -29.4 |  |
| money_delta | close | pin limit <$1k | 9-12 | 42.9 | -4.0 | -17.3 |  |
| pin_rlm | close | 1-3k bets | 15-25 | 37.5 | -3.8 | -16.2 |  |
| pin_rlm | close | 3k+ bets | 2-11 | 15.4 | -24.1 | -67.0 |  |
| pin_rlm | close | <1k bets | 1-3 | 25.0 | -22.3 | -52.3 |  |
| pin_rlm | close | pin $1-2k | 10-14 | 41.7 | -2.2 | -10.1 |  |
| pin_rlm | close | pin $2k+ | 5-16 | 23.8 | -11.8 | -41.5 |  |
| pin_rlm | close | pin limit <$1k | 3-9 | 25.0 | -21.1 | -51.2 |  |
| follow_move | close | 1-3k bets | 122-149 | 45.0 | -4.0 | -8.8 |  |
| follow_move | close | 3k+ bets | 37-46 | 44.6 | -5.7 | -19.1 |  |
| follow_move | close | <1k bets | 23-31 | 42.6 | -6.8 | -25.0 |  |
| follow_move | close | pin $1-2k | 58-74 | 43.9 | -5.2 | -14.4 |  |
| follow_move | close | pin $2k+ | 58-63 | 47.9 | -1.8 | -1.9 |  |
| follow_move | close | pin limit <$1k | 16-26 | 38.1 | -11.4 | -26.8 |  |
| rlm_ratio | close | 1-3k bets | 28-47 | 37.3 | -4.1 | -19.1 |  |
| rlm_ratio | close | 3k+ bets | 7-16 | 30.4 | -10.7 | -36.1 |  |
| rlm_ratio | close | <1k bets | 3-7 | 30.0 | -13.0 | -42.9 |  |
| rlm_ratio | close | pin $1-2k | 16-16 | 50.0 | 7.4 | 5.2 |  |
| rlm_ratio | close | pin $2k+ | 5-19 | 20.8 | -15.3 | -50.8 |  |
| rlm_ratio | close | pin limit <$1k | 5-11 | 31.2 | -15.5 | -39.8 |  |
| money_level | close | 1-3k bets | 151-129 | 53.9 | -1.9 | -7.6 |  |
| money_level | close | 3k+ bets | 56-46 | 54.9 | -0.3 | -6.2 |  |
| money_level | close | <1k bets | 38-11 | 77.6 | 22.2 | 32.8 |  |
| money_level | close | pin $1-2k | 70-61 | 53.4 | -0.6 | -4.8 |  |
| money_level | close | pin $2k+ | 72-56 | 56.2 | -0.9 | -6.3 |  |
| money_level | close | pin limit <$1k | 24-22 | 52.2 | 0.2 | -0.8 |  |
| sharp_gap | close | 1-3k bets | 119-142 | 45.6 | -2.4 | -11.4 |  |
| sharp_gap | close | 3k+ bets | 41-56 | 42.3 | -5.9 | -18.7 |  |
| sharp_gap | close | <1k bets | 25-20 | 55.6 | 7.2 | 8.4 |  |
| sharp_gap | close | pin $1-2k | 62-57 | 52.1 | 3.5 | 2.3 |  |
| sharp_gap | close | pin $2k+ | 50-72 | 41.0 | -6.2 | -19.0 |  |
| sharp_gap | close | pin limit <$1k | 15-27 | 35.7 | -13.3 | -31.6 |  |
| money_moving | close | 1-3k bets | 126-138 | 47.7 | -1.1 | -8.4 |  |
| money_moving | close | 3k+ bets | 40-57 | 41.2 | -7.3 | -21.5 |  |
| money_moving | close | <1k bets | 26-19 | 57.8 | 8.4 | 10.5 |  |
| money_moving | close | pin $1-2k | 65-54 | 54.6 | 5.0 | 5.7 |  |
| money_moving | close | pin $2k+ | 50-72 | 41.0 | -6.2 | -19.0 |  |
| money_moving | close | pin limit <$1k | 17-29 | 37.0 | -12.2 | -29.3 |  |
| pin_value | close | 1-3k bets | 70-51 | 57.9 | 8.2 | 18.6 |  |
| pin_value | close | 3k+ bets | 12-23 | 34.3 | -15.6 | -34.9 |  |
| pin_value | close | <1k bets | 11-7 | 61.1 | 12.6 | 35.7 |  |
| pin_value | close | pin $1-2k | 44-40 | 52.4 | 2.8 | 5.7 |  |
| pin_value | close | pin $2k+ | 26-30 | 46.4 | -2.3 | 4.0 |  |
| pin_value | close | pin limit <$1k | 23-11 | 67.6 | 16.5 | 28.4 |  |
| consensus_gap | close | 1-3k bets | 59-41 | 59.0 | 5.7 | 6.6 |  |
| consensus_gap | close | 3k+ bets | 15-14 | 51.7 | -2.0 | -15.0 |  |
| consensus_gap | close | <1k bets | 15-3 | 83.3 | 28.9 | 56.5 |  |
| consensus_gap | close | pin $1-2k | 21-17 | 55.3 | 1.7 | 13.1 |  |
| consensus_gap | close | pin $2k+ | 40-17 | 70.2 | 14.3 | 23.3 |  |
| consensus_gap | close | pin limit <$1k | 8-3 | 72.7 | 24.3 | 38.7 |  |
| follow_move+pin_move | close | 1-3k bets | 53-72 | 42.4 | -6.5 | -15.8 |  |
| money_delta+money_moving | close | 1-3k bets | 31-35 | 47.0 | 4.6 | -3.5 |  |
| money_delta+sharp_gap | close | 1-3k bets | 31-34 | 47.7 | 5.4 | -2.0 |  |
| money_moving+sharp_gap | close | 1-3k bets | 116-134 | 46.4 | -1.9 | -9.4 |  |
| consensus_gap+money_level | close | 1-3k bets | 37-23 | 61.7 | 2.3 | -1.3 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 46-71 | 39.3 | -3.3 | -6.7 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 23-35 | 39.7 | -4.7 | -13.5 |  |
| consensus_gap+follow_move | close | 1-3k bets | 14-17 | 45.2 | -5.4 | -14.7 |  |
| follow_move+money_level | close | 1-3k bets | 55-56 | 49.5 | -5.9 | -12.0 |  |
| money_level+money_moving | close | 1-3k bets | 83-78 | 51.6 | -1.9 | -8.3 |  |
| money_level+sharp_gap | close | 1-3k bets | 77-77 | 50.0 | -3.0 | -9.6 |  |
| consensus_gap+money_moving | close | 1-3k bets | 18-20 | 47.4 | -3.7 | -7.5 |  |
| consensus_gap+pin_move | close | 1-3k bets | 13-7 | 65.0 | 14.5 | 34.5 |  |
| consensus_gap+pin_value | close | 1-3k bets | 23-14 | 62.2 | 12.3 | 16.6 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 18-20 | 47.4 | -3.2 | -7.8 |  |
| follow_move+money_moving | close | 1-3k bets | 59-79 | 42.8 | -5.3 | -15.8 |  |
| follow_move+pin_value | close | 1-3k bets | 21-15 | 58.3 | 8.0 | 37.3 |  |
| follow_move+sharp_gap | close | 1-3k bets | 61-83 | 42.4 | -5.2 | -16.6 |  |
| money_level+pin_move | close | 1-3k bets | 32-29 | 52.5 | -1.5 | -5.5 |  |
| money_level+pin_value | close | 1-3k bets | 25-19 | 56.8 | 6.0 | 6.5 |  |
| money_moving+pin_move | close | 1-3k bets | 34-37 | 47.9 | -0.0 | -4.1 |  |
| money_moving+pin_value | close | 1-3k bets | 21-23 | 47.7 | -2.2 | -10.2 |  |
| pin_move+pin_value | close | 1-3k bets | 25-18 | 58.1 | 7.4 | 9.4 |  |
| pin_move+sharp_gap | close | 1-3k bets | 32-41 | 43.8 | -3.3 | -11.9 |  |
| pin_value+sharp_gap | close | 1-3k bets | 20-22 | 47.6 | -2.0 | -10.4 |  |
| follow_move+money_delta | close | 1-3k bets | 23-35 | 39.7 | -4.6 | -19.8 |  |
| money_delta+pin_move | close | 1-3k bets | 13-16 | 44.8 | 1.5 | -11.8 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 13-26 | 33.3 | -9.2 | -30.7 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 28-47 | 37.3 | -4.1 | -19.1 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 18-35 | 34.0 | -6.3 | -22.0 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 28-43 | 39.4 | -2.2 | -14.6 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 14-34 | 29.2 | -10.2 | -31.0 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 18-40 | 31.0 | -8.8 | -28.7 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 28-47 | 37.3 | -4.1 | -19.1 |  |
| money_delta+money_level | close | 1-3k bets | 10-7 | 58.8 | 9.6 | 17.2 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 4-9 | 30.8 | -7.2 | -29.1 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 4-5 | 44.4 | 5.9 | 1.7 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 17-25 | 40.5 | -1.4 | -16.5 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 2-3 | 40.0 | -5.5 | 8.0 |  |
| money_level+pin_rlm | close | 1-3k bets | 6-3 | 66.7 | 19.7 | 31.1 |  |
| money_moving+pin_rlm | close | 1-3k bets | 15-21 | 41.7 | -0.2 | -6.9 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 15-25 | 37.5 | -3.8 | -16.2 |  |
| money_level+rlm_ratio | close | 1-3k bets | 11-10 | 52.4 | 5.4 | 2.0 |  |
| consensus_gap+money_delta | close | 1-3k bets | 6-4 | 60.0 | 17.7 | 14.8 |  |
| follow_move+pin_rlm | close | 1-3k bets | 13-21 | 38.2 | -2.5 | -13.8 |  |
| money_delta+pin_rlm | close | 1-3k bets | 8-12 | 40.0 | 0.6 | -20.0 |  |
| pin_move+pin_rlm | close | 1-3k bets | 15-20 | 42.9 | 1.3 | -4.2 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 14-18 | 43.8 | 1.9 | -2.7 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 7-18 | 28.0 | -11.8 | -30.0 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 13-21 | 38.2 | -2.5 | -13.8 |  |
| money_delta+pin_value | close | 1-3k bets | 10-5 | 66.7 | 18.6 | 26.6 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 6-8 | 42.9 | -4.5 | 51.7 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 4-3 | 57.1 | 7.2 | 7.1 |  |
| pin_rlm+pin_value | close | 1-3k bets | 2-4 | 33.3 | -16.2 | -37.0 |  |
| money_level+money_moving | close | 3k+ bets | 25-29 | 46.3 | -6.7 | -13.9 |  |
| money_level+sharp_gap | close | 3k+ bets | 25-28 | 47.2 | -5.6 | -12.2 |  |
| money_moving+sharp_gap | close | 3k+ bets | 40-56 | 41.7 | -6.7 | -20.7 |  |
| follow_move+money_delta | close | 3k+ bets | 6-9 | 40.0 | -5.4 | -22.8 |  |
| follow_move+money_level | close | 3k+ bets | 18-16 | 52.9 | -5.4 | -14.9 |  |
| follow_move+money_moving | close | 3k+ bets | 18-28 | 39.1 | -9.9 | -27.0 |  |
| follow_move+pin_move | close | 3k+ bets | 14-35 | 28.6 | -20.6 | -47.3 |  |
| follow_move+pin_rlm | close | 3k+ bets | 2-11 | 15.4 | -24.1 | -67.0 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 7-16 | 30.4 | -10.7 | -36.1 |  |
| follow_move+sharp_gap | close | 3k+ bets | 19-28 | 40.4 | -8.3 | -22.8 |  |
| money_delta+money_level | close | 3k+ bets | 3-1 | 75.0 | 26.9 | 45.1 |  |
| money_delta+money_moving | close | 3k+ bets | 10-12 | 45.5 | 2.5 | -9.6 |  |
| money_delta+pin_move | close | 3k+ bets | 3-8 | 27.3 | -18.2 | -47.2 |  |
| money_delta+pin_rlm | close | 3k+ bets | 1-5 | 16.7 | -24.7 | -67.5 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 3-6 | 33.3 | -9.0 | -35.4 |  |
| money_delta+sharp_gap | close | 3k+ bets | 10-12 | 45.5 | 2.5 | -9.6 |  |
| money_level+pin_move | close | 3k+ bets | 10-16 | 38.5 | -16.9 | -34.9 |  |
| money_level+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 52.7 | 95.2 |  |
| money_level+rlm_ratio | close | 3k+ bets | 2-1 | 66.7 | 15.8 | 28.7 |  |
| money_moving+pin_move | close | 3k+ bets | 6-23 | 20.7 | -26.7 | -61.9 |  |
| money_moving+pin_rlm | close | 3k+ bets | 2-11 | 15.4 | -24.1 | -67.0 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 6-16 | 27.3 | -14.3 | -45.6 |  |
| pin_move+pin_rlm | close | 3k+ bets | 1-11 | 8.3 | -31.7 | -83.7 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 1-12 | 7.7 | -33.3 | -85.0 |  |
| pin_move+sharp_gap | close | 3k+ bets | 6-23 | 20.7 | -26.7 | -61.9 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 2-11 | 15.4 | -24.1 | -67.0 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 2-11 | 15.4 | -24.1 | -67.0 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 7-16 | 30.4 | -10.7 | -36.1 |  |
| consensus_gap+money_level | close | 3k+ bets | 13-8 | 61.9 | 2.2 | -1.6 |  |
| consensus_gap+money_moving | close | 3k+ bets | 5-10 | 33.3 | -17.7 | -41.3 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 5-9 | 35.7 | -14.2 | -37.1 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 13-28 | 31.7 | -11.5 | -35.6 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 5-22 | 18.5 | -24.7 | -62.2 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 4-8 | 33.3 | -11.1 | -35.7 |  |
| money_level+pin_value | close | 3k+ bets | 9-13 | 40.9 | -10.6 | -23.2 |  |
| money_moving+pin_value | close | 3k+ bets | 7-13 | 35.0 | -15.4 | -34.1 |  |
| pin_value+sharp_gap | close | 3k+ bets | 7-13 | 35.0 | -15.4 | -34.1 |  |
| consensus_gap+follow_move | close | 3k+ bets | 6-5 | 54.5 | 1.8 | -13.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 5-4 | 55.6 | 7.6 | 6.5 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 5-17 | 22.7 | -19.7 | -56.4 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 6-17 | 26.1 | -15.9 | -46.5 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 0-11 | 0.0 | -39.3 | -100.0 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 4-15 | 21.1 | -19.0 | -55.3 |  |
| pin_move+pin_value | close | 3k+ bets | 6-13 | 31.6 | -18.9 | -40.0 |  |
| follow_move+pin_value | close | 3k+ bets | 4-9 | 30.8 | -21.3 | -41.5 |  |
| consensus_gap+money_delta | close | 3k+ bets | 1-1 | 50.0 | 6.0 | -4.5 |  |
| consensus_gap+pin_move | close | 3k+ bets | 7-5 | 58.3 | 9.1 | 2.8 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 1-4 | 20.0 | -21.3 | -61.8 |  |
| money_delta+pin_value | close | 3k+ bets | 1-1 | 50.0 | -5.0 | -4.5 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 1-5 | 16.7 | -32.1 | -68.2 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 0-3 | 0.0 | -39.5 | -100.0 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 0-3 | 0.0 | -39.5 | -100.0 |  |
| pin_rlm+pin_value | close | 3k+ bets | 0-1 | 0.0 | -47.3 | -100.0 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 0-1 | 0.0 | -47.3 | -100.0 |  |
| consensus_gap+money_level | close | <1k bets | 11-1 | 91.7 | 32.3 | 42.3 |  |
| consensus_gap+money_moving | close | <1k bets | 8-0 | 100.0 | 44.2 | 103.6 |  |
| consensus_gap+pin_value | close | <1k bets | 4-1 | 80.0 | 35.4 | 123.1 |  |
| consensus_gap+sharp_gap | close | <1k bets | 9-1 | 90.0 | 35.4 | 77.0 |  |
| follow_move+pin_move | close | <1k bets | 6-10 | 37.5 | -13.6 | -30.3 |  |
| follow_move+rlm_quiet | close | <1k bets | 4-17 | 19.0 | -23.2 | -63.3 |  |
| money_level+money_moving | close | <1k bets | 20-5 | 80.0 | 25.8 | 38.3 |  |
| money_level+pin_value | close | <1k bets | 5-1 | 83.3 | 34.5 | 56.7 |  |
| money_level+sharp_gap | close | <1k bets | 19-5 | 79.2 | 25.5 | 40.2 |  |
| money_moving+pin_value | close | <1k bets | 4-1 | 80.0 | 36.5 | 124.8 |  |
| money_moving+sharp_gap | close | <1k bets | 24-18 | 57.1 | 8.5 | 12.8 |  |
| pin_move+rlm_quiet | close | <1k bets | 2-4 | 33.3 | -14.2 | -36.4 |  |
| pin_value+sharp_gap | close | <1k bets | 4-1 | 80.0 | 36.5 | 124.8 |  |
| follow_move+money_moving | close | <1k bets | 10-10 | 50.0 | 0.1 | -17.8 |  |
| follow_move+sharp_gap | close | <1k bets | 9-10 | 47.4 | -1.7 | -18.3 |  |
| money_level+pin_move | close | <1k bets | 6-3 | 66.7 | 12.2 | 22.8 |  |
| money_moving+rlm_quiet | close | <1k bets | 2-6 | 25.0 | -16.9 | -52.3 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 2-6 | 25.0 | -16.9 | -52.3 |  |
| follow_move+money_delta | close | <1k bets | 5-7 | 41.7 | -4.3 | -20.5 |  |
| follow_move+pin_rlm | close | <1k bets | 1-3 | 25.0 | -22.3 | -52.3 |  |
| follow_move+pin_value | close | <1k bets | 3-2 | 60.0 | 11.0 | 15.4 |  |
| follow_move+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -13.0 | -42.9 |  |
| money_delta+money_moving | close | <1k bets | 7-8 | 46.7 | 4.1 | 18.9 |  |
| money_delta+pin_move | close | <1k bets | 1-2 | 33.3 | -14.0 | -36.4 |  |
| money_delta+pin_rlm | close | <1k bets | 1-2 | 33.3 | -14.0 | -36.4 |  |
| money_delta+pin_value | close | <1k bets | 3-0 | 100.0 | 57.5 | 212.0 |  |
| money_delta+rlm_quiet | close | <1k bets | 3-4 | 42.9 | 0.6 | -17.2 |  |
| money_delta+rlm_ratio | close | <1k bets | 3-5 | 37.5 | -6.2 | -28.6 |  |
| money_delta+sharp_gap | close | <1k bets | 7-8 | 46.7 | 4.1 | 18.9 |  |
| money_moving+pin_move | close | <1k bets | 3-3 | 50.0 | 2.2 | -5.2 |  |
| money_moving+pin_rlm | close | <1k bets | 1-3 | 25.0 | -22.3 | -52.3 |  |
| money_moving+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -13.0 | -42.9 |  |
| pin_move+pin_rlm | close | <1k bets | 1-3 | 25.0 | -22.3 | -52.3 |  |
| pin_move+pin_value | close | <1k bets | 4-1 | 80.0 | 29.0 | 52.8 |  |
| pin_move+rlm_ratio | close | <1k bets | 1-3 | 25.0 | -22.3 | -52.3 |  |
| pin_move+sharp_gap | close | <1k bets | 3-3 | 50.0 | 2.2 | -5.2 |  |
| pin_rlm+pin_value | close | <1k bets | 1-0 | 100.0 | 52.7 | 90.9 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 1-1 | 50.0 | 2.7 | -4.5 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 1-3 | 25.0 | -22.3 | -52.3 |  |
| pin_rlm+sharp_gap | close | <1k bets | 1-3 | 25.0 | -22.3 | -52.3 |  |
| pin_value+rlm_quiet | close | <1k bets | 2-0 | 100.0 | 52.7 | 90.9 |  |
| pin_value+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 52.7 | 90.9 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 2-5 | 28.6 | -12.6 | -45.5 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 3-7 | 30.0 | -13.0 | -42.9 |  |
| consensus_gap+follow_move | close | <1k bets | 5-0 | 100.0 | 40.8 | 71.3 |  |
| consensus_gap+pin_move | close | <1k bets | 2-0 | 100.0 | 42.8 | 70.5 |  |
| follow_move+money_level | close | <1k bets | 12-4 | 75.0 | 16.9 | 21.7 |  |
| money_delta+money_level | close | <1k bets | 2-1 | 66.7 | 24.1 | 53.8 |  |
| money_level+pin_rlm | close | <1k bets | 0-1 | 0.0 | -47.3 | -100.0 |  |
| money_level+rlm_ratio | close | <1k bets | 1-1 | 50.0 | 2.7 | -5.3 |  |
| consensus_gap+money_delta | close | <1k bets | 3-0 | 100.0 | 50.9 | 208.0 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 52.7 | 89.3 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-0 | 100.0 | 52.7 | 90.9 |  |
| money_delta+money_moving | close | pin $1-2k | 14-6 | 70.0 | 26.7 | 54.0 |  |
| money_delta+sharp_gap | close | pin $1-2k | 14-6 | 70.0 | 26.7 | 54.0 |  |
| money_moving+sharp_gap | close | pin $1-2k | 60-52 | 53.6 | 4.5 | 5.7 |  |
| consensus_gap+follow_move | close | pin $1-2k | 7-8 | 46.7 | -6.2 | -16.8 |  |
| consensus_gap+money_level | close | pin $1-2k | 12-10 | 54.5 | -3.0 | -7.0 |  |
| consensus_gap+money_moving | close | pin $1-2k | 6-8 | 42.9 | -8.3 | -3.4 |  |
| consensus_gap+pin_move | close | pin $1-2k | 6-6 | 50.0 | 0.5 | 9.9 |  |
| consensus_gap+pin_value | close | pin $1-2k | 11-8 | 57.9 | 7.5 | 28.0 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 6-7 | 46.2 | -6.4 | 6.1 |  |
| follow_move+money_level | close | pin $1-2k | 27-27 | 50.0 | -3.3 | -9.3 |  |
| follow_move+money_moving | close | pin $1-2k | 31-33 | 48.4 | 0.0 | -5.0 |  |
| follow_move+pin_move | close | pin $1-2k | 28-55 | 33.7 | -15.0 | -31.5 |  |
| follow_move+pin_value | close | pin $1-2k | 14-15 | 48.3 | -1.9 | -8.3 |  |
| follow_move+sharp_gap | close | pin $1-2k | 33-36 | 47.8 | -0.4 | -7.1 |  |
| money_level+money_moving | close | pin $1-2k | 44-33 | 57.1 | 4.5 | 2.8 |  |
| money_level+pin_move | close | pin $1-2k | 17-24 | 41.5 | -10.7 | -23.2 |  |
| money_level+pin_value | close | pin $1-2k | 17-14 | 54.8 | 4.2 | 2.6 |  |
| money_level+sharp_gap | close | pin $1-2k | 41-33 | 55.4 | 3.5 | 1.4 |  |
| money_moving+pin_move | close | pin $1-2k | 21-25 | 45.7 | -3.5 | -8.7 |  |
| money_moving+pin_value | close | pin $1-2k | 15-13 | 53.6 | 4.2 | 13.6 |  |
| pin_move+pin_value | close | pin $1-2k | 16-14 | 53.3 | 2.2 | 0.5 |  |
| pin_move+sharp_gap | close | pin $1-2k | 21-29 | 42.0 | -6.1 | -16.0 |  |
| pin_value+sharp_gap | close | pin $1-2k | 15-13 | 53.6 | 4.3 | 13.6 |  |
| follow_move+money_delta | close | pin $1-2k | 16-13 | 55.2 | 8.4 | 7.3 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 20-37 | 35.1 | -9.7 | -25.3 |  |
| money_delta+pin_move | close | pin $1-2k | 10-8 | 55.6 | 9.0 | 8.1 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 10-12 | 45.5 | -1.3 | -11.9 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 14-27 | 34.1 | -11.8 | -26.6 |  |
| follow_move+pin_rlm | close | pin $1-2k | 9-13 | 40.9 | -3.0 | -10.6 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 16-16 | 50.0 | 7.4 | 5.2 |  |
| pin_move+pin_rlm | close | pin $1-2k | 10-12 | 45.5 | 0.6 | -1.9 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 9-12 | 42.9 | -2.5 | -6.3 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 5-13 | 27.8 | -15.8 | -33.8 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 9-13 | 40.9 | -3.0 | -10.6 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 10-14 | 41.7 | -2.2 | -10.1 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 7-14 | 33.3 | -9.4 | -24.4 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 10-16 | 38.5 | -4.6 | -16.8 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 16-16 | 50.0 | 7.4 | 5.2 |  |
| money_delta+money_level | close | pin $1-2k | 4-1 | 80.0 | 34.5 | 56.7 |  |
| money_delta+pin_rlm | close | pin $1-2k | 6-3 | 66.7 | 22.5 | 29.9 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 9-4 | 69.2 | 25.9 | 35.5 |  |
| money_level+pin_rlm | close | pin $1-2k | 4-0 | 100.0 | 54.9 | 93.8 |  |
| money_level+rlm_ratio | close | pin $1-2k | 7-2 | 77.8 | 33.5 | 50.4 |  |
| money_moving+pin_rlm | close | pin $1-2k | 10-10 | 50.0 | 4.6 | 7.9 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 16-13 | 55.2 | 12.1 | 16.0 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 10-13 | 43.5 | -0.3 | -5.9 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 1-4 | 20.0 | -21.3 | -61.8 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 5-9 | 35.7 | -12.7 | -31.2 |  |
| money_delta+pin_value | close | pin $1-2k | 7-3 | 70.0 | 24.1 | 69.5 |  |
| consensus_gap+money_delta | close | pin $1-2k | 3-1 | 75.0 | 29.9 | 131.4 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 0-2 | 0.0 | -42.8 | -100.0 |  |
| pin_rlm+pin_value | close | pin $1-2k | 3-3 | 50.0 | 0.5 | -5.2 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 2-3 | 40.0 | -8.4 | -24.4 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 0-1 | 0.0 | -52.7 | -100.0 |  |
| follow_move+pin_move | close | pin $2k+ | 35-47 | 42.7 | -7.0 | -19.4 |  |
| consensus_gap+money_level | close | pin $2k+ | 29-12 | 70.7 | 9.8 | 11.0 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 20-34 | 37.0 | -4.2 | -2.3 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 12-29 | 29.3 | -12.7 | -35.7 |  |
| money_level+money_moving | close | pin $2k+ | 34-39 | 46.6 | -6.4 | -15.3 |  |
| money_level+sharp_gap | close | pin $2k+ | 34-39 | 46.6 | -6.4 | -15.3 |  |
| money_moving+sharp_gap | close | pin $2k+ | 50-72 | 41.0 | -6.2 | -19.0 |  |
| consensus_gap+pin_value | close | pin $2k+ | 14-8 | 63.6 | 16.2 | 19.5 |  |
| follow_move+money_level | close | pin $2k+ | 24-19 | 55.8 | -4.6 | -9.1 |  |
| follow_move+money_moving | close | pin $2k+ | 20-34 | 37.0 | -11.0 | -29.1 |  |
| follow_move+sharp_gap | close | pin $2k+ | 20-34 | 37.0 | -11.0 | -29.1 |  |
| money_level+pin_move | close | pin $2k+ | 20-14 | 58.8 | -0.5 | -2.4 |  |
| money_moving+pin_move | close | pin $2k+ | 14-25 | 35.9 | -9.8 | -29.4 |  |
| pin_move+sharp_gap | close | pin $2k+ | 14-25 | 35.9 | -9.8 | -29.4 |  |
| money_delta+money_level | close | pin $2k+ | 5-2 | 71.4 | 27.0 | 47.1 |  |
| money_delta+money_moving | close | pin $2k+ | 11-23 | 32.4 | -7.2 | -33.0 |  |
| money_delta+sharp_gap | close | pin $2k+ | 11-23 | 32.4 | -7.2 | -33.0 |  |
| consensus_gap+money_moving | close | pin $2k+ | 13-12 | 52.0 | -0.1 | 6.0 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 13-12 | 52.0 | -0.1 | 6.0 |  |
| money_level+pin_value | close | pin $2k+ | 10-14 | 41.7 | -8.3 | -22.5 |  |
| money_moving+pin_value | close | pin $2k+ | 8-17 | 32.0 | -17.3 | -40.1 |  |
| pin_value+sharp_gap | close | pin $2k+ | 8-17 | 32.0 | -17.3 | -40.1 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 1-3 | 25.0 | -16.5 | -15.0 |  |
| money_level+pin_rlm | close | pin $2k+ | 1-1 | 50.0 | 0.0 | 7.0 |  |
| money_moving+pin_rlm | close | pin $2k+ | 5-16 | 23.8 | -11.8 | -41.5 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 5-16 | 23.8 | -11.8 | -41.5 |  |
| follow_move+money_delta | close | pin $2k+ | 5-14 | 26.3 | -14.2 | -48.0 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 5-19 | 20.8 | -15.3 | -50.8 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 3-13 | 18.8 | -19.1 | -62.1 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 5-19 | 20.8 | -15.3 | -50.8 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 5-19 | 20.8 | -15.3 | -50.8 |  |
| money_level+rlm_ratio | close | pin $2k+ | 2-2 | 50.0 | 6.0 | -0.3 |  |
| consensus_gap+follow_move | close | pin $2k+ | 12-4 | 75.0 | 18.0 | 31.1 |  |
| consensus_gap+pin_move | close | pin $2k+ | 14-4 | 77.8 | 25.2 | 41.9 |  |
| follow_move+pin_value | close | pin $2k+ | 6-7 | 46.2 | -4.9 | 61.3 |  |
| pin_move+pin_value | close | pin $2k+ | 10-12 | 45.5 | -4.3 | -14.6 |  |
| follow_move+pin_rlm | close | pin $2k+ | 4-14 | 22.2 | -11.9 | -44.7 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 4-14 | 22.2 | -11.9 | -44.7 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 2-3 | 40.0 | -6.2 | 170.2 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 4-18 | 18.2 | -19.4 | -55.9 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 4-18 | 18.2 | -19.4 | -55.9 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 3-11 | 21.4 | -17.8 | -57.9 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 2-15 | 11.8 | -22.4 | -67.8 |  |
| money_delta+pin_move | close | pin $2k+ | 5-11 | 31.2 | -9.3 | -38.2 |  |
| money_delta+pin_rlm | close | pin $2k+ | 2-10 | 16.7 | -18.1 | -64.8 |  |
| pin_move+pin_rlm | close | pin $2k+ | 4-13 | 23.5 | -10.7 | -41.5 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 4-13 | 23.5 | -12.0 | -44.3 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 2-13 | 13.3 | -21.0 | -63.5 |  |
| consensus_gap+money_delta | close | pin $2k+ | 2-1 | 66.7 | 19.0 | 25.2 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 2-3 | 40.0 | 2.7 | 6.2 |  |
| money_delta+pin_value | close | pin $2k+ | 2-2 | 50.0 | -2.5 | -6.1 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 2-2 | 50.0 | 11.6 | 31.2 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 1-0 | 100.0 | 45.0 | 84.7 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 4-2 | 66.7 | 20.0 | 28.1 |  |
| consensus_gap+money_level | close | pin limit <$1k | 4-1 | 80.0 | 27.3 | 50.5 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 4-3 | 57.1 | 10.3 | 9.8 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 7-3 | 70.0 | 20.0 | 32.5 |  |
| follow_move+money_level | close | pin limit <$1k | 9-14 | 39.1 | -12.0 | -25.1 |  |
| follow_move+money_moving | close | pin limit <$1k | 8-20 | 28.6 | -20.3 | -45.1 |  |
| follow_move+pin_value | close | pin limit <$1k | 8-4 | 66.7 | 15.1 | 26.9 |  |
| money_level+money_moving | close | pin limit <$1k | 10-16 | 38.5 | -12.6 | -26.9 |  |
| money_level+pin_value | close | pin limit <$1k | 12-5 | 70.6 | 18.1 | 33.9 |  |
| money_moving+pin_value | close | pin limit <$1k | 9-7 | 56.2 | 5.9 | 7.1 |  |
| follow_move+pin_move | close | pin limit <$1k | 10-15 | 40.0 | -9.0 | -22.8 |  |
| money_level+pin_move | close | pin limit <$1k | 11-10 | 52.4 | 1.4 | -0.2 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 15-27 | 35.7 | -13.3 | -31.6 |  |
| pin_move+pin_value | close | pin limit <$1k | 9-6 | 60.0 | 9.0 | 14.3 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 6-9 | 40.0 | -6.7 | -22.5 |  |
| money_moving+pin_move | close | pin limit <$1k | 8-13 | 38.1 | -10.6 | -27.0 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 3-1 | 75.0 | 31.3 | 45.5 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 2-2 | 50.0 | 6.3 | -2.3 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 1-2 | 33.3 | -9.2 | -33.3 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 3-1 | 75.0 | 31.3 | 45.5 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 2-1 | 66.7 | 24.1 | 30.3 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 4-2 | 66.7 | 20.8 | 28.1 |  |
| follow_move+money_delta | close | pin limit <$1k | 4-9 | 30.8 | -15.9 | -40.5 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 3-8 | 27.3 | -18.8 | -46.7 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 5-11 | 31.2 | -15.5 | -39.8 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 8-19 | 29.6 | -19.1 | -43.1 |  |
| money_delta+money_moving | close | pin limit <$1k | 8-10 | 44.4 | -2.4 | -14.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 2-7 | 22.2 | -23.5 | -56.1 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 2-6 | 25.0 | -20.5 | -50.6 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 2-3 | 40.0 | -4.5 | -21.8 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 4-8 | 33.3 | -13.2 | -35.6 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 8-10 | 44.4 | -2.4 | -14.2 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 3-9 | 25.0 | -21.1 | -51.2 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 2-6 | 25.0 | -20.5 | -51.1 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 5-11 | 31.2 | -15.5 | -39.8 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 3-9 | 25.0 | -21.1 | -51.2 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 4-5 | 44.4 | -1.9 | -13.7 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 3-8 | 27.3 | -18.8 | -46.7 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 6-13 | 31.6 | -16.7 | -39.2 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 1-4 | 20.0 | -24.5 | -60.0 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 3-8 | 27.3 | -18.8 | -46.7 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 3-9 | 25.0 | -21.1 | -51.2 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 2-6 | 25.0 | -20.5 | -51.1 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 2-6 | 25.0 | -20.5 | -51.1 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 5-11 | 31.2 | -15.5 | -39.8 |  |
| money_delta+pin_value | close | pin limit <$1k | 5-1 | 83.3 | 35.1 | 59.1 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 2-1 | 66.7 | 19.3 | 27.3 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 2-1 | 66.7 | 17.6 | 26.0 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 8-6 | 57.1 | 7.1 | 8.8 |  |
| money_level+sharp_gap | close | pin limit <$1k | 8-15 | 34.8 | -16.0 | -33.8 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 0-2 | 0.0 | -47.3 | -100.0 |  |
| money_delta+money_level | close | pin limit <$1k | 1-4 | 20.0 | -27.3 | -61.0 |  |
| money_level+pin_rlm | close | pin limit <$1k | 2-3 | 40.0 | -7.3 | -22.8 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 2-4 | 33.3 | -14.0 | -35.7 |  |
| rlm_quiet | early | <1k bets | 12-20 | 37.5 | -1.7 | -9.3 | 1.21 |
| rlm_quiet | early | pin $1-2k | 1-1 | 50.0 | 17.1 | 16.0 | 1.15 |
| rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -47.3 | -100.0 | 0.0 |
| pin_move | early | <1k bets | 4-6 | 40.0 | -9.5 | -23.6 | 0.3 |
| pin_move | early | pin $1-2k | 0-2 | 0.0 | -45.0 | -100.0 | 0.0 |
| pin_move | early | pin limit <$1k | 4-4 | 50.0 | -0.7 | -4.5 | 0.38 |
| money_delta | early | <1k bets | 4-3 | 57.1 | 18.1 | 49.5 | 3.06 |
| money_delta | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| pin_rlm | early | <1k bets | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| follow_move | early | <1k bets | 106-124 | 46.1 | -2.9 | -11.6 | 0.02 |
| follow_move | early | pin $1-2k | 9-8 | 52.9 | 8.7 | 7.6 | -0.06 |
| follow_move | early | pin limit <$1k | 6-8 | 42.9 | -4.7 | -11.2 | -0.45 |
| rlm_ratio | early | <1k bets | 7-11 | 38.9 | -3.6 | -5.3 | 1.08 |
| rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| money_level | early | <1k bets | 41-33 | 55.4 | -3.0 | -11.4 | -0.42 |
| money_level | early | pin $1-2k | 1-2 | 33.3 | -33.8 | -44.4 | -0.23 |
| money_level | early | pin limit <$1k | 2-2 | 50.0 | -1.3 | -4.5 | 1.25 |
| sharp_gap | early | <1k bets | 29-37 | 43.9 | -3.5 | -9.4 | 0.58 |
| sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -33.8 | -44.4 | -0.23 |
| sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | 1.3 | -4.5 | 0.75 |
| money_moving | early | <1k bets | 26-29 | 47.3 | -0.0 | -6.7 | 0.46 |
| money_moving | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.7 |
| money_moving | early | pin limit <$1k | 2-1 | 66.7 | 19.3 | 27.3 | 0.0 |
| pin_value | early | <1k bets | 11-12 | 47.8 | -1.5 | -9.9 | -0.01 |
| pin_value | early | pin $1-2k | 3-7 | 30.0 | -18.2 | -43.9 | -0.03 |
| pin_value | early | pin limit <$1k | 8-5 | 61.5 | 11.3 | 16.3 | 0.0 |
| consensus_gap | early | <1k bets | 66-43 | 60.6 | 8.4 | 8.4 | 0.55 |
| consensus_gap | early | pin $1-2k | 6-3 | 66.7 | 17.2 | 19.3 | -0.9 |
| consensus_gap | early | pin limit <$1k | 4-1 | 80.0 | 29.5 | 51.9 | 0.6 |
| follow_move+money_level | early | <1k bets | 14-10 | 58.3 | -1.8 | -15.4 | 0.53 |
| follow_move+sharp_gap | early | <1k bets | 13-17 | 43.3 | -4.3 | -9.3 | 1.19 |
| money_level+sharp_gap | early | <1k bets | 17-18 | 48.6 | -6.4 | -15.7 | 0.05 |
| follow_move+money_moving | early | <1k bets | 13-13 | 50.0 | 2.4 | 2.1 | 0.72 |
| money_level+money_moving | early | <1k bets | 13-11 | 54.2 | -1.1 | -6.8 | 0.2 |
| consensus_gap+money_level | early | <1k bets | 13-9 | 59.1 | -0.5 | -12.7 | -0.5 |
| follow_move+rlm_quiet | early | <1k bets | 12-20 | 37.5 | -1.7 | -9.3 | 1.21 |
| follow_move+rlm_ratio | early | <1k bets | 7-11 | 38.9 | -3.6 | -5.3 | 1.08 |
| rlm_quiet+rlm_ratio | early | <1k bets | 6-8 | 42.9 | 3.8 | 8.1 | 0.71 |
| rlm_quiet+sharp_gap | early | <1k bets | 6-9 | 40.0 | 0.4 | 0.9 | 0.67 |
| rlm_ratio+sharp_gap | early | <1k bets | 7-11 | 38.9 | -3.6 | -5.3 | 1.08 |
| consensus_gap+follow_move | early | <1k bets | 8-5 | 61.5 | 7.3 | -0.7 | 0.56 |
| money_moving+rlm_quiet | early | <1k bets | 7-7 | 50.0 | 10.9 | 28.7 | 0.96 |
| money_moving+rlm_ratio | early | <1k bets | 7-5 | 58.3 | 17.6 | 42.0 | 1.36 |
| money_moving+sharp_gap | early | <1k bets | 17-19 | 47.2 | 2.1 | 1.5 | 0.89 |
| consensus_gap+money_moving | early | <1k bets | 4-3 | 57.1 | 7.5 | -11.9 | 0.74 |
| consensus_gap+sharp_gap | early | <1k bets | 7-5 | 58.3 | 9.5 | -2.3 | -0.03 |
| money_level+rlm_ratio | early | <1k bets | 1-3 | 25.0 | -29.2 | -52.3 | 2.38 |
| follow_move+pin_move | early | <1k bets | 1-3 | 25.0 | -23.1 | -52.3 | 0.5 |
| follow_move+money_delta | early | <1k bets | 3-1 | 75.0 | 34.9 | 114.0 | 2.35 |
| money_delta+money_level | early | <1k bets | 1-2 | 33.3 | -9.2 | -36.4 | 1.73 |
| money_delta+money_moving | early | <1k bets | 4-3 | 57.1 | 18.1 | 49.5 | 3.06 |
| money_delta+rlm_ratio | early | <1k bets | 3-1 | 75.0 | 34.9 | 114.0 | 2.35 |
| money_delta+sharp_gap | early | <1k bets | 4-3 | 57.1 | 18.1 | 49.5 | 3.06 |
| follow_move+pin_value | early | <1k bets | 3-3 | 50.0 | 2.6 | -4.5 | -0.83 |
| consensus_gap+pin_move | early | <1k bets | 1-0 | 100.0 | 47.3 | 90.9 | 0.0 |
| consensus_gap+pin_value | early | <1k bets | 5-1 | 83.3 | 33.7 | 57.8 | 0.0 |
| money_level+pin_move | early | <1k bets | 1-1 | 50.0 | -2.7 | -4.5 | 1.5 |
| money_level+pin_value | early | <1k bets | 2-2 | 50.0 | -4.9 | -4.5 | 1.43 |
| pin_move+pin_value | early | <1k bets | 2-5 | 28.6 | -21.1 | -45.5 | 0.43 |
| money_moving+pin_value | early | <1k bets | 1-1 | 50.0 | -7.2 | -4.5 | 1.35 |
| pin_value+sharp_gap | early | <1k bets | 1-2 | 33.3 | -22.4 | -36.4 | 1.9 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| consensus_gap+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| follow_move+pin_rlm | early | <1k bets | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| money_level+pin_rlm | early | <1k bets | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| pin_rlm+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| pin_rlm+sharp_gap | early | <1k bets | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| pin_move+sharp_gap | early | <1k bets | 0-1 | 0.0 | -52.7 | -100.0 | 3.0 |
| money_delta+rlm_quiet | early | <1k bets | 2-0 | 100.0 | 67.1 | 232.5 | 3.2 |
| pin_move+pin_value | early | pin $1-2k | 0-2 | 0.0 | -45.0 | -100.0 | 0.0 |
| follow_move+rlm_quiet | early | pin $1-2k | 1-1 | 50.0 | 17.1 | 16.0 | 1.15 |
| money_level+money_moving | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.7 |
| money_level+pin_value | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.7 |
| money_level+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -33.8 | -44.4 | -0.23 |
| money_moving+pin_value | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.7 |
| money_moving+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.7 |
| pin_value+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.7 |
| consensus_gap+pin_value | early | pin $1-2k | 2-1 | 66.7 | 18.3 | 24.7 | -0.67 |
| follow_move+money_level | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| follow_move+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| follow_move+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| money_level+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| consensus_gap+follow_move | early | pin $1-2k | 1-0 | 100.0 | 67.1 | 106.0 | 1.5 |
| follow_move+pin_move | early | pin $1-2k | 0-1 | 0.0 | -45.0 | -100.0 | 0.0 |
| follow_move+pin_value | early | pin $1-2k | 0-1 | 0.0 | -45.0 | -100.0 | 0.0 |
| consensus_gap+money_level | early | pin $1-2k | 1-0 | 100.0 | 32.9 | 66.7 | -3.9 |
| consensus_gap+sharp_gap | early | pin $1-2k | 1-0 | 100.0 | 32.9 | 66.7 | -3.9 |
| follow_move+pin_move | early | pin limit <$1k | 1-2 | 33.3 | -15.8 | -36.4 | 0.67 |
| follow_move+pin_value | early | pin limit <$1k | 3-2 | 60.0 | 12.1 | 14.5 | -1.0 |
| consensus_gap+money_level | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 90.9 | 0.5 |
| consensus_gap+pin_move | early | pin limit <$1k | 1-0 | 100.0 | 47.3 | 90.9 | 0.0 |
| consensus_gap+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 49.1 | 90.9 | 0.67 |
| follow_move+money_moving | early | pin limit <$1k | 1-1 | 50.0 | 2.7 | -4.5 | 0.5 |
| follow_move+rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -47.3 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 2.7 | -4.5 | 0.5 |
| money_level+pin_move | early | pin limit <$1k | 1-1 | 50.0 | -2.7 | -4.5 | 1.5 |
| money_level+pin_value | early | pin limit <$1k | 2-1 | 66.7 | 15.8 | 27.3 | 1.33 |
| money_moving+rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -47.3 | -100.0 | 0.0 |
| money_moving+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 19.3 | 27.3 | 0.0 |
| pin_move+pin_value | early | pin limit <$1k | 2-3 | 40.0 | -11.6 | -23.6 | 0.6 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -47.3 | -100.0 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| consensus_gap+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| follow_move+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| follow_move+money_level | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| follow_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| money_delta+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| money_delta+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| money_delta+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| money_level+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| money_level+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| money_level+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 | 2.0 |
| money_moving+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| pin_value+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 | 2.0 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 90.9 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -52.7 | -100.0 | 3.0 |
