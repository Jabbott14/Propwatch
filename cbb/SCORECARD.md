# CBB scorecard

Generated 2026-11-23 01:59 UTC. 798 graded games (28 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**684 games before 2026-11-21 (fit) · 114 on or after it (forward).**

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
sample ran **46.9% favourites** (n=797) and **51.1% overs** (n=798) and **71.9% moneyline favourites** (n=686).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-21. Nothing in the engine was chosen using these. n=114 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 8-12 | 40.0 | 38.3 | 1.7 | -2.19 | -11.0 | 0.33 | 40.0 | keep collecting (20/30) |
| pin_move | both | 3-4 | 42.9 | 48.9 | -6.0 | -1.27 | -18.2 | 0.0 | 14.3 | keep collecting (7/30) |
| money_delta | both | 1-1 | 50.0 | 40.4 | 9.6 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| pin_rlm | both | 0-1 | 0.0 | 63.5 | -63.5 | -1.0 | -100.0 | 1.5 | 100.0 | keep collecting (1/30) |
| follow_move | both | 74-90 | 45.1 | 48.0 | -2.9 | -23.33 | -14.2 | 0.11 | 34.8 | DROP: below break-even |
| rlm_ratio | both | 5-7 | 41.7 | 42.5 | -0.9 | -1.6 | -13.4 | 0.82 | 58.3 | keep collecting (12/30) |
| money_level | both | 21-20 | 51.2 | 59.4 | -8.2 | -7.12 | -17.4 | 0.01 | 39.0 | no edge shown yet |
| sharp_gap | both | 15-19 | 44.1 | 47.1 | -3.0 | -4.38 | -12.9 | 0.33 | 47.1 | no edge shown yet |
| money_moving | both | 18-16 | 52.9 | 49.5 | 3.4 | -0.12 | -0.3 | 0.61 | 50.0 | no edge shown yet |
| pin_value | both | 8-8 | 50.0 | 48.1 | 1.9 | -0.88 | -5.5 | -0.08 | 31.2 | keep collecting (16/30) |
| consensus_gap | both | 50-39 | 56.2 | 50.7 | 5.5 | +3.86 | 4.3 | 0.36 | 48.3 | no edge shown yet |
| follow_move+money_level | both | 5-8 | 38.5 | 58.4 | -19.9 | -5.49 | -42.2 | 0.39 | 38.5 | keep collecting (13/30) |
| follow_move+sharp_gap | both | 6-10 | 37.5 | 45.6 | -8.1 | -3.69 | -23.1 | 0.68 | 50.0 | keep collecting (16/30) |
| money_level+sharp_gap | both | 7-10 | 41.2 | 56.0 | -14.8 | -4.57 | -26.9 | 0.31 | 52.9 | keep collecting (17/30) |
| follow_move+money_moving | both | 9-9 | 50.0 | 47.8 | 2.2 | -1.23 | -6.8 | 0.79 | 50.0 | keep collecting (18/30) |
| money_level+money_moving | both | 9-9 | 50.0 | 57.9 | -7.9 | -3.28 | -18.2 | 0.48 | 44.4 | keep collecting (18/30) |
| consensus_gap+money_level | both | 8-5 | 61.5 | 57.0 | 4.6 | -1.01 | -7.8 | -0.32 | 38.5 | keep collecting (13/30) |
| follow_move+rlm_quiet | both | 8-12 | 40.0 | 38.3 | 1.7 | -2.19 | -11.0 | 0.33 | 40.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 5-7 | 41.7 | 42.5 | -0.9 | -1.6 | -13.4 | 0.82 | 58.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | both | 4-4 | 50.0 | 38.4 | 11.6 | +0.49 | 6.1 | 0.04 | 37.5 | keep collecting (8/30) |
| rlm_quiet+sharp_gap | both | 4-5 | 44.4 | 38.7 | 5.8 | -0.51 | -5.7 | 0.03 | 33.3 | keep collecting (9/30) |
| rlm_ratio+sharp_gap | both | 5-7 | 41.7 | 42.5 | -0.9 | -1.6 | -13.4 | 0.82 | 58.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 5-5 | 50.0 | 48.8 | 1.2 | -1.33 | -13.3 | 0.96 | 70.0 | keep collecting (10/30) |
| money_moving+rlm_quiet | both | 5-4 | 55.6 | 38.7 | 16.9 | +2.37 | 26.3 | 0.97 | 55.6 | keep collecting (9/30) |
| money_moving+rlm_ratio | both | 5-3 | 62.5 | 41.7 | 20.8 | +2.4 | 29.9 | 1.57 | 75.0 | keep collecting (8/30) |
| money_moving+sharp_gap | both | 11-10 | 52.4 | 48.4 | 4.0 | +1.27 | 6.1 | 0.72 | 57.1 | keep collecting (21/30) |
| consensus_gap+money_moving | both | 4-2 | 66.7 | 50.6 | 16.0 | +0.17 | 2.8 | 0.35 | 50.0 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 4-3 | 57.1 | 48.1 | 9.1 | +0.17 | 2.4 | 0.04 | 57.1 | keep collecting (7/30) |
| money_level+rlm_ratio | both | 1-3 | 25.0 | 50.7 | -25.7 | -2.09 | -52.3 | 2.38 | 100.0 | keep collecting (4/30) |
| follow_move+pin_move | both | 1-3 | 25.0 | 45.4 | -20.4 | -2.09 | -52.3 | 0.5 | 25.0 | keep collecting (4/30) |
| follow_move+money_delta | both | 1-1 | 50.0 | 40.4 | 9.6 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_level | both | 1-1 | 50.0 | 40.4 | 9.6 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_moving | both | 1-1 | 50.0 | 40.4 | 9.6 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | both | 1-1 | 50.0 | 40.4 | 9.6 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | both | 1-1 | 50.0 | 40.4 | 9.6 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| follow_move+pin_value | both | 3-3 | 50.0 | 43.9 | 6.1 | -0.27 | -4.5 | -0.83 | 16.7 | keep collecting (6/30) |
| consensus_gap+pin_move | both | 1-0 | 100.0 | 59.6 | 40.4 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+pin_value | both | 4-0 | 100.0 | 54.6 | 45.4 | +3.6 | 89.9 | 0.5 | 50.0 | keep collecting (4/30) |
| money_level+pin_move | both | 1-0 | 100.0 | 59.6 | 40.4 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | both | 2-1 | 66.7 | 54.5 | 12.2 | +0.82 | 27.3 | 0.9 | 66.7 | keep collecting (3/30) |
| pin_move+pin_value | both | 1-3 | 25.0 | 50.4 | -25.4 | -2.09 | -52.3 | 0.0 | 0.0 | keep collecting (4/30) |
| money_moving+pin_value | both | 1-1 | 50.0 | 51.9 | -1.9 | -0.09 | -4.5 | 1.35 | 100.0 | keep collecting (2/30) |
| pin_value+sharp_gap | both | 1-1 | 50.0 | 51.9 | -1.9 | -0.09 | -4.5 | 1.35 | 100.0 | keep collecting (2/30) |
| consensus_gap+money_delta | both | 1-0 | 100.0 | 40.4 | 59.6 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 1-0 | 100.0 | 40.4 | 59.6 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | both | 1-0 | 100.0 | 40.4 | 59.6 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+rlm_ratio | both | 1-0 | 100.0 | 40.4 | 59.6 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 0-1 | 0.0 | 63.5 | -63.5 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-1 | 0.0 | 63.5 | -63.5 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | both | 0-1 | 0.0 | 63.5 | -63.5 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 0-1 | 0.0 | 63.5 | -63.5 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet | moneyline | 4-7 | 36.4 | 36.5 | -0.2 | -0.79 | -7.2 | 0.33 | 36.4 | keep collecting (11/30) |
| rlm_quiet | total | 4-5 | 44.4 | 40.4 | 4.1 | -1.4 | -15.6 | 0.33 | 44.4 | keep collecting (9/30) |
| pin_move | spread | 0-2 | 0.0 | 41.2 | -41.2 | -2.0 | -100.0 | 0.0 | 0.0 | keep collecting (2/30) |
| pin_move | total | 3-2 | 60.0 | 51.9 | 8.1 | +0.73 | 14.5 | 0.0 | 20.0 | keep collecting (5/30) |
| money_delta | total | 1-1 | 50.0 | 40.4 | 9.6 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| pin_rlm | moneyline | 0-1 | 0.0 | 63.5 | -63.5 | -1.0 | -100.0 | 1.5 | 100.0 | keep collecting (1/30) |
| follow_move | moneyline | 30-25 | 54.5 | 47.3 | 7.2 | +1.18 | 2.2 | -0.3 | 30.9 | no edge shown yet |
| follow_move | spread | 19-29 | 39.6 | 51.8 | -12.2 | -11.37 | -23.7 | -0.15 | 25.0 | DROP: below break-even |
| follow_move | total | 25-36 | 41.0 | 45.7 | -4.7 | -13.14 | -21.5 | 0.67 | 45.9 | DROP: below break-even |
| rlm_ratio | moneyline | 1-4 | 20.0 | 41.9 | -21.9 | -2.24 | -44.8 | 0.56 | 40.0 | keep collecting (5/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 58.8 | -58.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| rlm_ratio | total | 4-2 | 66.7 | 40.4 | 26.3 | +1.64 | 27.3 | 0.33 | 66.7 | keep collecting (6/30) |
| money_level | moneyline | 12-10 | 54.5 | 61.0 | -6.5 | -5.33 | -24.2 | -0.38 | 27.3 | keep collecting (22/30) |
| money_level | spread | 0-1 | 0.0 | 58.8 | -58.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level | total | 9-9 | 50.0 | 57.5 | -7.5 | -0.79 | -4.4 | 0.22 | 50.0 | keep collecting (18/30) |
| sharp_gap | moneyline | 6-11 | 35.3 | 46.0 | -10.7 | -4.6 | -27.0 | 0.54 | 52.9 | keep collecting (17/30) |
| sharp_gap | spread | 0-1 | 0.0 | 58.8 | -58.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| sharp_gap | total | 9-7 | 56.2 | 47.6 | 8.7 | +1.21 | 7.6 | -0.19 | 37.5 | keep collecting (16/30) |
| money_moving | moneyline | 9-8 | 52.9 | 50.8 | 2.1 | -0.33 | -1.9 | 0.92 | 58.8 | keep collecting (17/30) |
| money_moving | spread | 0-1 | 0.0 | 58.8 | -58.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving | total | 9-7 | 56.2 | 47.6 | 8.7 | +1.22 | 7.6 | 0.0 | 37.5 | keep collecting (16/30) |
| pin_value | moneyline | 0-1 | 0.0 | 63.5 | -63.5 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| pin_value | spread | 4-5 | 44.4 | 45.1 | -0.7 | -1.52 | -16.9 | 0.0 | 22.2 | keep collecting (9/30) |
| pin_value | total | 4-2 | 66.7 | 50.0 | 16.7 | +1.64 | 27.3 | -0.5 | 33.3 | keep collecting (6/30) |
| consensus_gap | moneyline | 20-19 | 51.3 | 52.4 | -1.1 | -2.96 | -7.6 | -0.09 | 43.6 | no edge shown yet |
| consensus_gap | spread | 12-9 | 57.1 | 48.7 | 8.4 | +1.6 | 7.6 | 0.43 | 42.9 | keep collecting (21/30) |
| consensus_gap | total | 18-11 | 62.1 | 49.7 | 12.4 | +5.21 | 18.0 | 0.93 | 58.6 | keep collecting (29/30) |
| consensus_gap+money_level | moneyline | 6-4 | 60.0 | 58.1 | 1.9 | -1.83 | -18.3 | -0.71 | 30.0 | keep collecting (10/30) |
| follow_move+rlm_quiet | moneyline | 4-7 | 36.4 | 36.5 | -0.2 | -0.79 | -7.2 | 0.33 | 36.4 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 1-4 | 20.0 | 41.9 | -21.9 | -2.24 | -44.8 | 0.56 | 40.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 1-4 | 20.0 | 41.9 | -21.9 | -2.24 | -44.8 | 0.56 | 40.0 | keep collecting (5/30) |
| rlm_quiet+rlm_ratio | moneyline | 1-3 | 25.0 | 36.5 | -11.5 | -1.24 | -31.0 | 0.33 | 25.0 | keep collecting (4/30) |
| rlm_quiet+sharp_gap | moneyline | 1-3 | 25.0 | 36.5 | -11.5 | -1.24 | -31.0 | 0.33 | 25.0 | keep collecting (4/30) |
| rlm_ratio+sharp_gap | moneyline | 1-4 | 20.0 | 41.9 | -21.9 | -2.24 | -44.8 | 0.56 | 40.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 3-1 | 75.0 | 56.7 | 18.3 | +0.86 | 21.4 | -0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+money_moving | moneyline | 3-2 | 60.0 | 52.7 | 7.3 | -0.74 | -14.8 | 0.22 | 40.0 | keep collecting (5/30) |
| consensus_gap+sharp_gap | moneyline | 3-2 | 60.0 | 47.3 | 12.7 | +0.26 | 5.2 | -0.54 | 40.0 | keep collecting (5/30) |
| money_level+money_moving | moneyline | 5-4 | 55.6 | 60.5 | -4.9 | -1.95 | -21.6 | 0.3 | 33.3 | keep collecting (9/30) |
| money_level+sharp_gap | moneyline | 3-5 | 37.5 | 56.7 | -19.2 | -3.24 | -40.5 | 0.15 | 50.0 | keep collecting (8/30) |
| money_moving+sharp_gap | moneyline | 4-5 | 44.4 | 48.5 | -4.1 | -0.12 | -1.4 | 1.24 | 66.7 | keep collecting (9/30) |
| follow_move+money_level | moneyline | 3-3 | 50.0 | 63.5 | -13.5 | -2.31 | -38.5 | -0.65 | 16.7 | keep collecting (6/30) |
| follow_move+money_moving | moneyline | 5-3 | 62.5 | 50.0 | 12.5 | +1.14 | 14.2 | 0.65 | 50.0 | keep collecting (8/30) |
| money_moving+rlm_quiet | moneyline | 2-2 | 50.0 | 36.5 | 13.5 | +1.64 | 41.0 | 1.68 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | moneyline | 1-1 | 50.0 | 36.5 | 13.5 | +0.76 | 38.0 | 0.8 | 50.0 | keep collecting (2/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 63.5 | -63.5 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 63.5 | -63.5 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 63.5 | -63.5 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_rlm | moneyline | 0-1 | 0.0 | 63.5 | -63.5 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 63.5 | -63.5 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | moneyline | 0-1 | 0.0 | 63.5 | -63.5 | -1.0 | -100.0 | 1.5 | 100.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 0-1 | 0.0 | 63.5 | -63.5 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 0-1 | 0.0 | 63.5 | -63.5 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+money_level | spread | 0-1 | 0.0 | 58.8 | -58.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| follow_move+money_moving | spread | 0-1 | 0.0 | 58.8 | -58.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 58.8 | -58.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 0-1 | 0.0 | 58.8 | -58.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to sharp_gap alone, not independent confirmation |
| money_level+money_moving | spread | 0-1 | 0.0 | 58.8 | -58.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+rlm_ratio | spread | 0-1 | 0.0 | 58.8 | -58.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+sharp_gap | spread | 0-1 | 0.0 | 58.8 | -58.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 58.8 | -58.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| money_moving+sharp_gap | spread | 0-1 | 0.0 | 58.8 | -58.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 58.8 | -58.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 1-1 | 50.0 | 41.2 | 8.8 | -0.09 | -4.5 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | spread | 0-2 | 0.0 | 41.2 | -41.2 | -2.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| consensus_gap+pin_value | spread | 1-0 | 100.0 | 58.8 | 41.2 | +0.87 | 87.0 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+pin_move | spread | 0-1 | 0.0 | 41.2 | -41.2 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_level | total | 2-4 | 33.3 | 53.2 | -19.9 | -2.18 | -36.4 | 0.67 | 50.0 | keep collecting (6/30) |
| follow_move+sharp_gap | total | 5-5 | 50.0 | 46.1 | 3.9 | -0.45 | -4.5 | 0.3 | 50.0 | keep collecting (10/30) |
| money_level+sharp_gap | total | 4-4 | 50.0 | 54.8 | -4.8 | -0.33 | -4.1 | -0.12 | 50.0 | keep collecting (8/30) |
| follow_move+money_moving | total | 4-5 | 44.4 | 44.6 | -0.2 | -1.36 | -15.2 | 0.44 | 44.4 | keep collecting (9/30) |
| money_level+money_moving | total | 4-4 | 50.0 | 54.8 | -4.8 | -0.33 | -4.1 | 0.12 | 50.0 | keep collecting (8/30) |
| follow_move+rlm_quiet | total | 4-5 | 44.4 | 40.4 | 4.1 | -1.4 | -15.6 | 0.33 | 44.4 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 4-2 | 66.7 | 40.4 | 26.3 | +1.64 | 27.3 | 0.33 | 66.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 3-1 | 75.0 | 40.4 | 34.6 | +1.73 | 43.2 | -0.25 | 50.0 | keep collecting (4/30) |
| rlm_quiet+sharp_gap | total | 3-2 | 60.0 | 40.4 | 19.6 | +0.73 | 14.5 | -0.2 | 40.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | total | 4-2 | 66.7 | 40.4 | 26.3 | +1.64 | 27.3 | 0.33 | 66.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | total | 3-2 | 60.0 | 40.4 | 19.6 | +0.73 | 14.5 | 0.4 | 40.0 | keep collecting (5/30) |
| money_moving+rlm_ratio | total | 4-1 | 80.0 | 40.4 | 39.6 | +2.64 | 52.7 | 1.2 | 80.0 | keep collecting (5/30) |
| money_moving+sharp_gap | total | 7-4 | 63.6 | 47.4 | 16.3 | +2.4 | 21.8 | -0.09 | 45.5 | keep collecting (11/30) |
| follow_move+pin_move | total | 1-2 | 33.3 | 46.8 | -13.5 | -1.09 | -36.4 | 0.67 | 33.3 | keep collecting (3/30) |
| consensus_gap+follow_move | total | 2-4 | 33.3 | 43.6 | -10.2 | -2.18 | -36.4 | 1.67 | 83.3 | keep collecting (6/30) |
| consensus_gap+money_level | total | 2-1 | 66.7 | 53.2 | 13.5 | +0.82 | 27.3 | 1.0 | 66.7 | keep collecting (3/30) |
| consensus_gap+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| follow_move+money_delta | total | 1-1 | 50.0 | 40.4 | 9.6 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_level | total | 1-1 | 50.0 | 40.4 | 9.6 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_moving | total | 1-1 | 50.0 | 40.4 | 9.6 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | total | 1-1 | 50.0 | 40.4 | 9.6 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | total | 1-1 | 50.0 | 40.4 | 9.6 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+rlm_ratio | total | 1-1 | 50.0 | 40.4 | 9.6 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| follow_move+pin_value | total | 2-2 | 50.0 | 45.2 | 4.8 | -0.18 | -4.5 | -1.0 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | total | 1-0 | 100.0 | 59.6 | 40.4 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+pin_value | total | 3-0 | 100.0 | 53.2 | 46.8 | +2.73 | 90.9 | 0.67 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | total | 1-0 | 100.0 | 59.6 | 40.4 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.82 | 90.9 | 0.5 | 50.0 | keep collecting (2/30) |
| pin_move+pin_value | total | 1-1 | 50.0 | 59.6 | -9.6 | -0.09 | -4.5 | 0.0 | 0.0 | keep collecting (2/30) |
| consensus_gap+money_delta | total | 1-0 | 100.0 | 40.4 | 59.6 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_moving | total | 1-0 | 100.0 | 40.4 | 59.6 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 1-0 | 100.0 | 40.4 | 59.6 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | total | 1-0 | 100.0 | 40.4 | 59.6 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 40.4 | 59.6 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+rlm_ratio | total | 1-0 | 100.0 | 40.4 | 59.6 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | total | 1-0 | 100.0 | 40.4 | 59.6 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 37-78 | 32.2 | 41.6 | -9.4 | -28.89 | -25.1 |  |  | DROP: below break-even |
| pin_move | both | 75-84 | 47.2 | 49.7 | -2.5 | -14.03 | -8.8 |  |  | no edge shown yet |
| money_delta | both | 44-50 | 46.8 | 41.6 | 5.2 | -3.03 | -3.2 |  |  | no edge shown yet |
| pin_rlm | both | 13-21 | 38.2 | 40.0 | -1.8 | -7.8 | -22.9 |  |  | DROP: below break-even |
| follow_move | both | 118-156 | 43.1 | 49.2 | -6.2 | -44.3 | -16.2 |  |  | DROP: below break-even |
| rlm_ratio | both | 23-45 | 33.8 | 40.7 | -6.8 | -22.4 | -32.9 |  |  | DROP: below break-even |
| money_level | both | 165-112 | 59.6 | 56.5 | 3.0 | +5.16 | 1.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 120-135 | 47.1 | 48.1 | -1.0 | -26.6 | -10.4 |  |  | DROP: below break-even |
| money_moving | both | 124-135 | 47.9 | 48.6 | -0.7 | -26.06 | -10.1 |  |  | no edge shown yet |
| pin_value | both | 68-49 | 58.1 | 50.9 | 7.3 | +26.81 | 22.9 |  |  | no edge shown yet |
| consensus_gap | both | 58-38 | 60.4 | 53.6 | 6.9 | +7.4 | 7.7 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+pin_move | both | 47-73 | 39.2 | 49.1 | -9.9 | -29.61 | -24.7 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 32-35 | 47.8 | 40.7 | 7.1 | +0.9 | 1.3 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 32-34 | 48.5 | 40.7 | 7.8 | +1.9 | 2.9 |  |  | no edge shown yet |
| money_moving+sharp_gap | both | 117-130 | 47.4 | 48.3 | -0.9 | -23.87 | -9.7 |  |  | DROP: below break-even |
| consensus_gap+money_level | both | 41-21 | 66.1 | 59.0 | 7.2 | +3.64 | 5.9 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+rlm_quiet | both | 37-78 | 32.2 | 41.6 | -9.4 | -28.89 | -25.1 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | both | 20-34 | 37.0 | 43.5 | -6.4 | -13.2 | -24.4 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 19-13 | 59.4 | 53.5 | 5.8 | +0.95 | 3.0 |  |  | no edge shown yet |
| follow_move+money_level | both | 57-48 | 54.3 | 57.0 | -2.7 | -7.48 | -7.1 |  |  | no edge shown yet |
| money_level+money_moving | both | 87-68 | 56.1 | 54.0 | 2.2 | -0.62 | -0.4 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 83-67 | 55.3 | 53.6 | 1.8 | -0.16 | -0.1 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 21-21 | 50.0 | 52.6 | -2.6 | -3.15 | -7.5 |  |  | no edge shown yet |
| consensus_gap+pin_move | both | 14-6 | 70.0 | 51.1 | 18.9 | +7.21 | 36.1 |  |  | keep collecting (20/30) |
| consensus_gap+pin_value | both | 21-13 | 61.8 | 49.5 | 12.3 | +9.28 | 27.3 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | both | 21-21 | 50.0 | 52.0 | -2.0 | -2.88 | -6.8 |  |  | no edge shown yet |
| follow_move+money_moving | both | 55-75 | 42.3 | 48.3 | -6.0 | -29.6 | -22.8 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 20-16 | 55.6 | 52.0 | 3.5 | +11.62 | 32.3 |  |  | no edge shown yet |
| follow_move+sharp_gap | both | 56-76 | 42.4 | 48.0 | -5.5 | -28.68 | -21.7 |  |  | DROP: below break-even |
| money_level+pin_move | both | 32-30 | 51.6 | 55.5 | -3.8 | -4.23 | -6.8 |  |  | no edge shown yet |
| money_level+pin_value | both | 25-18 | 58.1 | 54.1 | 4.1 | +4.01 | 9.3 |  |  | no edge shown yet |
| money_moving+pin_move | both | 31-33 | 48.4 | 47.8 | 0.6 | -4.93 | -7.7 |  |  | no edge shown yet |
| money_moving+pin_value | both | 22-20 | 52.4 | 50.5 | 1.9 | +3.18 | 7.6 |  |  | no edge shown yet |
| pin_move+pin_value | both | 25-19 | 56.8 | 52.5 | 4.3 | +3.36 | 7.6 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 29-34 | 46.0 | 47.3 | -1.2 | -7.71 | -12.2 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 21-18 | 53.8 | 49.7 | 4.1 | +4.27 | 10.9 |  |  | no edge shown yet |
| follow_move+money_delta | both | 25-37 | 40.3 | 42.6 | -2.2 | -13.37 | -21.6 |  |  | DROP: below break-even |
| money_delta+pin_move | both | 13-17 | 43.3 | 40.7 | 2.6 | -4.55 | -15.2 |  |  | no edge shown yet |
| money_delta+rlm_quiet | both | 15-28 | 34.9 | 40.7 | -5.9 | -13.51 | -31.4 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | both | 23-45 | 33.8 | 40.7 | -6.8 | -22.4 | -32.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | both | 15-36 | 29.4 | 39.2 | -9.8 | -20.97 | -41.1 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 23-43 | 34.8 | 40.8 | -5.9 | -20.4 | -30.9 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 10-33 | 23.3 | 38.7 | -15.4 | -23.12 | -53.8 |  |  | INVERT candidate: wrong well beyond its base rate |
| rlm_quiet+sharp_gap | both | 15-38 | 28.3 | 39.1 | -10.8 | -22.97 | -43.3 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 23-45 | 33.8 | 40.7 | -6.8 | -22.4 | -32.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | both | 10-6 | 62.5 | 45.3 | 17.2 | +4.05 | 25.3 |  |  | keep collecting (16/30) |
| consensus_gap+rlm_quiet | both | 5-7 | 41.7 | 41.2 | 0.5 | -2.36 | -19.7 |  |  | keep collecting (12/30) |
| consensus_gap+rlm_ratio | both | 3-4 | 42.9 | 37.6 | 5.2 | -1.2 | -17.1 |  |  | keep collecting (7/30) |
| money_delta+rlm_ratio | both | 17-26 | 39.5 | 40.8 | -1.3 | -9.66 | -22.5 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 1-2 | 33.3 | 46.8 | -13.5 | -1.0 | -33.3 |  |  | keep collecting (3/30) |
| money_level+pin_rlm | both | 5-4 | 55.6 | 42.5 | 13.1 | +0.74 | 8.2 |  |  | keep collecting (9/30) |
| money_moving+pin_rlm | both | 13-20 | 39.4 | 40.1 | -0.7 | -6.8 | -20.6 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 13-21 | 38.2 | 40.0 | -1.8 | -7.8 | -22.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | both | 10-9 | 52.6 | 44.8 | 7.8 | +0.33 | 1.7 |  |  | keep collecting (19/30) |
| consensus_gap+money_delta | both | 6-2 | 75.0 | 43.6 | 31.4 | +7.06 | 88.2 |  |  | keep collecting (8/30) |
| follow_move+pin_rlm | both | 11-18 | 37.9 | 38.8 | -0.8 | -7.03 | -24.2 |  |  | keep collecting (29/30) |
| money_delta+pin_rlm | both | 8-13 | 38.1 | 38.7 | -0.6 | -5.18 | -24.7 |  |  | keep collecting (21/30) |
| pin_move+pin_rlm | both | 12-16 | 42.9 | 39.8 | 3.1 | -4.14 | -14.8 |  |  | keep collecting (28/30) |
| pin_move+rlm_ratio | both | 10-15 | 40.0 | 39.1 | 0.9 | -5.37 | -21.5 |  |  | keep collecting (25/30) |
| pin_rlm+rlm_quiet | both | 5-13 | 27.8 | 38.4 | -10.7 | -8.11 | -45.0 |  |  | keep collecting (18/30) |
| pin_rlm+rlm_ratio | both | 11-18 | 37.9 | 38.8 | -0.8 | -7.03 | -24.2 |  |  | keep collecting (29/30) |
| money_delta+pin_value | both | 11-3 | 78.6 | 42.8 | 35.8 | +10.59 | 75.7 |  |  | keep collecting (14/30) |
| pin_value+rlm_quiet | both | 8-6 | 57.1 | 45.3 | 11.8 | +11.01 | 78.6 |  |  | keep collecting (14/30) |
| pin_value+rlm_ratio | both | 3-0 | 100.0 | 46.8 | 53.2 | +2.69 | 89.6 |  |  | keep collecting (3/30) |
| pin_rlm+pin_value | both | 2-1 | 66.7 | 46.5 | 20.2 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| rlm_quiet | moneyline | 14-33 | 29.8 | 37.1 | -7.3 | -5.37 | -11.4 |  |  | DROP: below break-even |
| rlm_quiet | spread | 7-11 | 38.9 | 55.8 | -17.0 | -4.41 | -24.5 |  |  | keep collecting (18/30) |
| rlm_quiet | total | 16-34 | 32.0 | 40.7 | -8.7 | -19.11 | -38.2 |  |  | DROP: below break-even |
| pin_move | moneyline | 21-17 | 55.3 | 47.9 | 7.4 | +3.77 | 9.9 |  |  | no edge shown yet |
| pin_move | spread | 27-26 | 50.9 | 52.5 | -1.5 | -1.5 | -2.8 |  |  | no edge shown yet |
| pin_move | total | 27-41 | 39.7 | 48.6 | -8.9 | -16.3 | -24.0 |  |  | DROP: below break-even |
| money_delta | moneyline | 12-19 | 38.7 | 39.1 | -0.4 | -1.59 | -5.1 |  |  | DROP: below break-even |
| money_delta | spread | 6-4 | 60.0 | 50.0 | 10.0 | +1.6 | 16.0 |  |  | keep collecting (10/30) |
| money_delta | total | 26-27 | 49.1 | 41.4 | 7.6 | -3.03 | -5.7 |  |  | no edge shown yet |
| pin_rlm | moneyline | 5-10 | 33.3 | 38.3 | -5.0 | -4.24 | -28.3 |  |  | keep collecting (15/30) |
| pin_rlm | spread | 1-0 | 100.0 | 58.8 | 41.2 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| pin_rlm | total | 7-11 | 38.9 | 40.4 | -1.5 | -4.47 | -24.8 |  |  | keep collecting (18/30) |
| follow_move | moneyline | 45-52 | 46.4 | 48.5 | -2.1 | -7.43 | -7.7 |  |  | no edge shown yet |
| follow_move | spread | 31-41 | 43.1 | 52.4 | -9.4 | -12.39 | -17.2 |  |  | DROP: below break-even |
| follow_move | total | 42-63 | 40.0 | 47.7 | -7.7 | -24.48 | -23.3 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 8-24 | 25.0 | 37.4 | -12.4 | -15.19 | -47.5 |  |  | DROP: below break-even |
| rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| rlm_ratio | total | 15-19 | 44.1 | 43.2 | 0.9 | -5.21 | -15.3 |  |  | no edge shown yet |
| money_level | moneyline | 66-38 | 63.5 | 60.9 | 2.6 | -10.05 | -9.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 31-29 | 51.7 | 48.2 | 3.4 | -1.08 | -1.8 |  |  | no edge shown yet |
| money_level | total | 68-45 | 60.2 | 56.9 | 3.3 | +16.29 | 14.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | moneyline | 42-51 | 45.2 | 46.7 | -1.5 | -13.45 | -14.5 |  |  | no edge shown yet |
| sharp_gap | spread | 28-32 | 46.7 | 47.1 | -0.4 | -6.65 | -11.1 |  |  | no edge shown yet |
| sharp_gap | total | 50-52 | 49.0 | 50.0 | -1.0 | -6.51 | -6.4 |  |  | no edge shown yet |
| money_moving | moneyline | 46-47 | 49.5 | 47.8 | 1.6 | -8.83 | -9.5 |  |  | no edge shown yet |
| money_moving | spread | 28-32 | 46.7 | 47.1 | -0.4 | -6.65 | -11.1 |  |  | no edge shown yet |
| money_moving | total | 50-56 | 47.2 | 50.2 | -3.0 | -10.58 | -10.0 |  |  | no edge shown yet |
| pin_value | moneyline | 5-1 | 83.3 | 45.5 | 37.8 | +19.16 | 319.4 |  |  | keep collecting (6/30) |
| pin_value | spread | 29-22 | 56.9 | 49.5 | 7.4 | +3.1 | 6.1 |  |  | no edge shown yet |
| pin_value | total | 34-26 | 56.7 | 52.6 | 4.1 | +4.54 | 7.6 |  |  | no edge shown yet |
| consensus_gap | moneyline | 32-22 | 59.3 | 55.5 | 3.8 | +0.54 | 1.0 |  |  | no edge shown yet |
| consensus_gap | spread | 10-7 | 58.8 | 46.4 | 12.4 | +1.6 | 9.4 |  |  | keep collecting (17/30) |
| consensus_gap | total | 16-9 | 64.0 | 54.2 | 9.8 | +5.25 | 21.0 |  |  | keep collecting (25/30) |
| consensus_gap+money_level | moneyline | 25-10 | 71.4 | 62.7 | 8.7 | +0.52 | 1.5 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+pin_move | moneyline | 13-17 | 43.3 | 47.3 | -4.0 | -4.84 | -16.1 |  |  | no edge shown yet |
| follow_move+rlm_quiet | moneyline | 14-33 | 29.8 | 37.1 | -7.3 | -5.37 | -11.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | moneyline | 6-11 | 35.3 | 38.1 | -2.8 | -3.25 | -19.1 |  |  | keep collecting (17/30) |
| consensus_gap+follow_move | moneyline | 11-8 | 57.9 | 53.5 | 4.4 | -1.23 | -6.5 |  |  | keep collecting (19/30) |
| follow_move+money_level | moneyline | 26-17 | 60.5 | 61.0 | -0.5 | -4.86 | -11.3 |  |  | no edge shown yet |
| money_moving+sharp_gap | moneyline | 41-46 | 47.1 | 47.1 | 0.1 | -8.86 | -10.2 |  |  | no edge shown yet |
| follow_move+money_moving | moneyline | 24-29 | 45.3 | 47.2 | -1.9 | -11.91 | -22.5 |  |  | no edge shown yet |
| follow_move+sharp_gap | moneyline | 23-31 | 42.6 | 46.5 | -3.9 | -13.84 | -25.6 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 31-18 | 63.3 | 58.0 | 5.3 | -1.16 | -2.4 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+sharp_gap | moneyline | 27-18 | 60.0 | 57.5 | 2.5 | -1.78 | -3.9 |  |  | no edge shown yet |
| follow_move+rlm_ratio | moneyline | 8-24 | 25.0 | 37.4 | -12.4 | -15.19 | -47.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | moneyline | 6-19 | 24.0 | 36.5 | -12.5 | -12.28 | -49.1 |  |  | keep collecting (25/30) |
| money_moving+rlm_ratio | moneyline | 8-22 | 26.7 | 37.4 | -10.8 | -13.19 | -44.0 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | moneyline | 4-20 | 16.7 | 36.5 | -19.9 | -15.66 | -65.2 |  |  | keep collecting (24/30) |
| rlm_quiet+sharp_gap | moneyline | 6-21 | 22.2 | 36.5 | -14.3 | -14.28 | -52.9 |  |  | keep collecting (27/30) |
| rlm_ratio+sharp_gap | moneyline | 8-24 | 25.0 | 37.4 | -12.4 | -15.19 | -47.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 12-11 | 52.2 | 54.1 | -1.9 | -1.17 | -5.1 |  |  | keep collecting (23/30) |
| consensus_gap+rlm_quiet | moneyline | 1-6 | 14.3 | 36.5 | -22.3 | -5.0 | -71.4 |  |  | keep collecting (7/30) |
| consensus_gap+rlm_ratio | moneyline | 1-4 | 20.0 | 36.5 | -16.5 | -3.0 | -60.0 |  |  | keep collecting (5/30) |
| consensus_gap+sharp_gap | moneyline | 12-12 | 50.0 | 53.4 | -3.4 | -1.89 | -7.9 |  |  | keep collecting (24/30) |
| consensus_gap+pin_rlm | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | +0.0 | 0.0 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | +0.02 | 1.0 |  |  | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 5-9 | 35.7 | 38.5 | -2.7 | -3.24 | -23.1 |  |  | keep collecting (14/30) |
| pin_rlm+sharp_gap | moneyline | 5-10 | 33.3 | 38.3 | -5.0 | -4.24 | -28.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 3-0 | 100.0 | 45.5 | 54.5 | +6.46 | 215.5 |  |  | keep collecting (3/30) |
| money_level+rlm_ratio | moneyline | 2-3 | 40.0 | 41.9 | -1.9 | -1.05 | -21.1 |  |  | keep collecting (5/30) |
| consensus_gap+pin_move | moneyline | 9-2 | 81.8 | 51.2 | 30.6 | +6.78 | 61.7 |  |  | keep collecting (11/30) |
| money_level+pin_move | moneyline | 10-5 | 66.7 | 61.7 | 5.0 | +0.92 | 6.1 |  |  | keep collecting (15/30) |
| consensus_gap+money_delta | moneyline | 3-2 | 60.0 | 41.9 | 18.1 | +4.35 | 86.9 |  |  | keep collecting (5/30) |
| follow_move+money_delta | moneyline | 6-14 | 30.0 | 40.6 | -10.6 | -7.96 | -39.8 |  |  | keep collecting (20/30) |
| follow_move+pin_rlm | moneyline | 4-8 | 33.3 | 36.5 | -3.2 | -3.56 | -29.7 |  |  | keep collecting (12/30) |
| money_delta+money_moving | moneyline | 11-18 | 37.9 | 38.4 | -0.5 | -1.44 | -5.0 |  |  | keep collecting (29/30) |
| money_delta+pin_move | moneyline | 3-4 | 42.9 | 36.5 | 6.3 | -0.9 | -12.9 |  |  | keep collecting (7/30) |
| money_delta+pin_rlm | moneyline | 3-6 | 33.3 | 36.5 | -3.2 | -2.9 | -32.2 |  |  | keep collecting (9/30) |
| money_delta+rlm_quiet | moneyline | 3-12 | 20.0 | 36.5 | -16.5 | -8.66 | -57.7 |  |  | keep collecting (15/30) |
| money_delta+rlm_ratio | moneyline | 4-13 | 23.5 | 38.1 | -14.6 | -8.64 | -50.8 |  |  | keep collecting (17/30) |
| money_delta+sharp_gap | moneyline | 11-18 | 37.9 | 38.4 | -0.5 | -1.44 | -5.0 |  |  | keep collecting (29/30) |
| money_moving+pin_move | moneyline | 7-5 | 58.3 | 43.3 | 15.1 | +1.33 | 11.1 |  |  | keep collecting (12/30) |
| pin_move+pin_rlm | moneyline | 4-5 | 44.4 | 36.5 | 7.9 | -0.58 | -6.4 |  |  | keep collecting (9/30) |
| pin_move+rlm_ratio | moneyline | 3-5 | 37.5 | 36.5 | 1.0 | -1.9 | -23.8 |  |  | keep collecting (8/30) |
| pin_move+sharp_gap | moneyline | 7-6 | 53.8 | 42.8 | 11.1 | +0.34 | 2.6 |  |  | keep collecting (13/30) |
| pin_rlm+rlm_quiet | moneyline | 2-7 | 22.2 | 36.5 | -14.3 | -4.92 | -54.7 |  |  | keep collecting (9/30) |
| pin_rlm+rlm_ratio | moneyline | 4-8 | 33.3 | 36.5 | -3.2 | -3.56 | -29.7 |  |  | keep collecting (12/30) |
| follow_move+pin_value | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | +9.6 | 480.0 |  |  | keep collecting (2/30) |
| pin_value+rlm_quiet | moneyline | 1-0 | 100.0 | 36.5 | 63.5 | +10.6 | 1060.0 |  |  | keep collecting (1/30) |
| money_delta+money_level | moneyline | 3-1 | 75.0 | 50.0 | 25.0 | +2.57 | 64.3 |  |  | keep collecting (4/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 63.5 | -63.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_move+pin_value | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | +0.08 | 4.0 |  |  | keep collecting (2/30) |
| money_delta+pin_value | moneyline | 1-0 | 100.0 | 36.5 | 63.5 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 1-0 | 100.0 | 36.5 | 63.5 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 1-0 | 100.0 | 36.5 | 63.5 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| follow_move+pin_move | spread | 14-22 | 38.9 | 52.9 | -14.0 | -9.21 | -25.6 |  |  | DROP: below break-even |
| money_moving+sharp_gap | spread | 28-32 | 46.7 | 47.1 | -0.4 | -6.65 | -11.1 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 7-11 | 38.9 | 55.8 | -17.0 | -4.41 | -24.5 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | spread | 19-21 | 47.5 | 46.5 | 1.0 | -3.88 | -9.7 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 19-21 | 47.5 | 46.5 | 1.0 | -3.88 | -9.7 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 4-8 | 33.3 | 55.8 | -22.5 | -4.29 | -35.8 |  |  | keep collecting (12/30) |
| consensus_gap+pin_value | spread | 8-7 | 53.3 | 45.9 | 7.4 | -0.08 | -0.5 |  |  | keep collecting (15/30) |
| follow_move+money_level | spread | 7-6 | 53.8 | 53.4 | 0.5 | +0.54 | 4.1 |  |  | keep collecting (13/30) |
| follow_move+money_moving | spread | 6-9 | 40.0 | 52.9 | -12.9 | -3.5 | -23.3 |  |  | keep collecting (15/30) |
| follow_move+sharp_gap | spread | 6-9 | 40.0 | 52.9 | -12.9 | -3.5 | -23.3 |  |  | keep collecting (15/30) |
| money_level+pin_move | spread | 6-7 | 46.2 | 50.7 | -4.5 | -1.59 | -12.2 |  |  | keep collecting (13/30) |
| money_moving+pin_move | spread | 8-7 | 53.3 | 50.6 | 2.7 | +0.17 | 1.2 |  |  | keep collecting (15/30) |
| pin_move+sharp_gap | spread | 8-7 | 53.3 | 50.6 | 2.7 | +0.17 | 1.2 |  |  | keep collecting (15/30) |
| money_delta+money_level | spread | 1-1 | 50.0 | 41.2 | 8.8 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_delta+money_moving | spread | 3-2 | 60.0 | 44.7 | 15.3 | +0.73 | 14.5 |  |  | keep collecting (5/30) |
| money_delta+sharp_gap | spread | 3-2 | 60.0 | 44.7 | 15.3 | +0.73 | 14.5 |  |  | keep collecting (5/30) |
| consensus_gap+money_level | spread | 3-5 | 37.5 | 43.4 | -5.9 | -2.41 | -30.2 |  |  | keep collecting (8/30) |
| consensus_gap+money_moving | spread | 2-4 | 33.3 | 44.2 | -10.8 | -2.21 | -36.9 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | spread | 2-4 | 33.3 | 44.2 | -10.8 | -2.21 | -36.9 |  |  | keep collecting (6/30) |
| money_level+pin_value | spread | 8-6 | 57.1 | 45.0 | 12.2 | +0.9 | 6.5 |  |  | keep collecting (14/30) |
| money_moving+pin_value | spread | 8-8 | 50.0 | 47.8 | 2.2 | -0.99 | -6.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | spread | 8-8 | 50.0 | 47.8 | 2.2 | -0.99 | -6.2 |  |  | keep collecting (16/30) |
| follow_move+money_delta | spread | 3-2 | 60.0 | 55.3 | 4.7 | +0.8 | 16.0 |  |  | keep collecting (5/30) |
| follow_move+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | spread | 0-1 | 0.0 | 41.2 | -41.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 8-5 | 61.5 | 53.4 | 8.2 | +2.13 | 16.4 |  |  | keep collecting (13/30) |
| pin_move+pin_value | spread | 14-6 | 70.0 | 52.6 | 17.4 | +6.3 | 31.5 |  |  | keep collecting (20/30) |
| consensus_gap+pin_move | spread | 3-2 | 60.0 | 51.8 | 8.2 | +0.65 | 13.0 |  |  | keep collecting (5/30) |
| consensus_gap+follow_move | spread | 2-1 | 66.7 | 58.8 | 7.9 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| consensus_gap+rlm_quiet | spread | 2-0 | 100.0 | 58.8 | 41.2 | +1.82 | 90.9 |  |  | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 2-2 | 50.0 | 58.8 | -8.8 | -0.18 | -4.5 |  |  | keep collecting (4/30) |
| money_delta+rlm_quiet | spread | 3-1 | 75.0 | 58.8 | 16.2 | +1.8 | 45.0 |  |  | keep collecting (4/30) |
| money_moving+rlm_quiet | spread | 1-2 | 33.3 | 52.9 | -19.6 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| rlm_quiet+rlm_ratio | spread | 0-1 | 0.0 | 58.8 | -58.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_quiet+sharp_gap | spread | 1-2 | 33.3 | 52.9 | -19.6 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 58.8 | 41.2 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+pin_move | spread | 2-0 | 100.0 | 58.8 | 41.2 | +1.82 | 90.9 |  |  | keep collecting (2/30) |
| money_delta+pin_value | spread | 1-0 | 100.0 | 58.8 | 41.2 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_moving+pin_rlm | spread | 1-0 | 100.0 | 58.8 | 41.2 | +0.91 | 90.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | spread | 1-0 | 100.0 | 58.8 | 41.2 | +0.91 | 90.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | spread | 1-0 | 100.0 | 58.8 | 41.2 | +0.91 | 90.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 1-0 | 100.0 | 58.8 | 41.2 | +0.91 | 90.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+money_moving | total | 18-15 | 54.5 | 42.1 | 12.4 | +1.61 | 4.9 |  |  | no edge shown yet |
| money_delta+sharp_gap | total | 18-14 | 56.2 | 42.2 | 14.1 | +2.61 | 8.1 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 48-52 | 48.0 | 50.0 | -2.0 | -8.36 | -8.4 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 16-34 | 32.0 | 40.7 | -8.7 | -19.11 | -38.2 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+follow_move | total | 6-4 | 60.0 | 51.9 | 8.1 | +1.36 | 13.6 |  |  | keep collecting (10/30) |
| consensus_gap+money_level | total | 13-6 | 68.4 | 58.6 | 9.8 | +5.53 | 29.1 |  |  | keep collecting (19/30) |
| consensus_gap+money_moving | total | 7-6 | 53.8 | 53.7 | 0.1 | +0.23 | 1.8 |  |  | keep collecting (13/30) |
| consensus_gap+pin_move | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.22 | -5.5 |  |  | keep collecting (4/30) |
| consensus_gap+pin_value | total | 10-6 | 62.5 | 53.6 | 8.9 | +2.89 | 18.1 |  |  | keep collecting (16/30) |
| consensus_gap+sharp_gap | total | 7-5 | 58.3 | 53.2 | 5.1 | +1.23 | 10.2 |  |  | keep collecting (12/30) |
| follow_move+money_level | total | 24-25 | 49.0 | 54.5 | -5.5 | -3.15 | -6.4 |  |  | no edge shown yet |
| follow_move+money_moving | total | 25-37 | 40.3 | 48.1 | -7.8 | -14.19 | -22.9 |  |  | DROP: below break-even |
| follow_move+pin_move | total | 20-34 | 37.0 | 47.5 | -10.5 | -15.55 | -28.8 |  |  | DROP: below break-even |
| follow_move+pin_value | total | 11-10 | 52.4 | 51.4 | 1.0 | -0.11 | -0.5 |  |  | keep collecting (21/30) |
| follow_move+sharp_gap | total | 27-36 | 42.9 | 48.0 | -5.2 | -11.34 | -18.0 |  |  | DROP: below break-even |
| money_level+money_moving | total | 37-29 | 56.1 | 55.6 | 0.5 | +4.43 | 6.7 |  |  | no edge shown yet |
| money_level+pin_move | total | 16-18 | 47.1 | 54.5 | -7.5 | -3.56 | -10.5 |  |  | no edge shown yet |
| money_level+pin_value | total | 17-11 | 60.7 | 58.3 | 2.4 | +4.1 | 14.7 |  |  | keep collecting (28/30) |
| money_level+sharp_gap | total | 37-28 | 56.9 | 55.2 | 1.7 | +5.5 | 8.5 |  |  | no edge shown yet |
| money_moving+pin_move | total | 16-21 | 43.2 | 48.2 | -4.9 | -6.44 | -17.4 |  |  | no edge shown yet |
| money_moving+pin_value | total | 13-12 | 52.0 | 52.7 | -0.7 | -0.34 | -1.3 |  |  | keep collecting (25/30) |
| pin_move+pin_value | total | 10-12 | 45.5 | 52.6 | -7.2 | -3.02 | -13.7 |  |  | keep collecting (22/30) |
| pin_move+sharp_gap | total | 14-21 | 40.0 | 47.5 | -7.5 | -8.22 | -23.5 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 12-10 | 54.5 | 51.8 | 2.8 | +0.76 | 3.4 |  |  | keep collecting (22/30) |
| follow_move+money_delta | total | 16-21 | 43.2 | 41.9 | 1.3 | -6.21 | -16.8 |  |  | no edge shown yet |
| money_delta+pin_move | total | 8-13 | 38.1 | 40.4 | -2.3 | -5.47 | -26.0 |  |  | keep collecting (21/30) |
| money_delta+rlm_quiet | total | 9-15 | 37.5 | 40.4 | -2.9 | -6.65 | -27.7 |  |  | keep collecting (24/30) |
| pin_move+rlm_quiet | total | 10-15 | 40.0 | 41.1 | -1.1 | -5.65 | -22.6 |  |  | keep collecting (25/30) |
| follow_move+rlm_ratio | total | 15-19 | 44.1 | 43.2 | 0.9 | -5.21 | -15.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | total | 13-12 | 52.0 | 42.7 | 9.3 | -0.02 | -0.1 |  |  | keep collecting (25/30) |
| money_moving+rlm_quiet | total | 8-15 | 34.8 | 40.4 | -5.6 | -7.6 | -33.0 |  |  | keep collecting (23/30) |
| money_moving+rlm_ratio | total | 15-19 | 44.1 | 43.2 | 0.9 | -5.21 | -15.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 6-12 | 33.3 | 40.4 | -7.0 | -6.46 | -35.9 |  |  | keep collecting (18/30) |
| rlm_quiet+sharp_gap | total | 8-15 | 34.8 | 40.4 | -5.6 | -7.6 | -33.0 |  |  | keep collecting (23/30) |
| rlm_ratio+sharp_gap | total | 15-19 | 44.1 | 43.2 | 0.9 | -5.21 | -15.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | total | 2-0 | 100.0 | 40.4 | 59.6 | +1.8 | 90.1 |  |  | keep collecting (2/30) |
| consensus_gap+rlm_quiet | total | 2-1 | 66.7 | 40.4 | 26.3 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| consensus_gap+rlm_ratio | total | 2-0 | 100.0 | 40.4 | 59.6 | +1.8 | 90.1 |  |  | keep collecting (2/30) |
| money_delta+pin_value | total | 9-3 | 75.0 | 42.0 | 33.0 | +5.18 | 43.2 |  |  | keep collecting (12/30) |
| pin_value+rlm_quiet | total | 5-4 | 55.6 | 40.4 | 15.2 | +0.59 | 6.5 |  |  | keep collecting (9/30) |
| pin_value+rlm_ratio | total | 3-0 | 100.0 | 46.8 | 53.2 | +2.69 | 89.6 |  |  | keep collecting (3/30) |
| follow_move+pin_rlm | total | 7-10 | 41.2 | 40.4 | 0.8 | -3.47 | -20.4 |  |  | keep collecting (17/30) |
| money_delta+money_level | total | 6-4 | 60.0 | 44.2 | 15.8 | +1.57 | 15.7 |  |  | keep collecting (10/30) |
| money_delta+pin_rlm | total | 5-7 | 41.7 | 40.4 | 1.3 | -2.28 | -19.0 |  |  | keep collecting (12/30) |
| money_level+pin_rlm | total | 4-3 | 57.1 | 40.4 | 16.8 | +0.72 | 10.3 |  |  | keep collecting (7/30) |
| money_level+rlm_ratio | total | 8-6 | 57.1 | 45.9 | 11.3 | +1.39 | 9.9 |  |  | keep collecting (14/30) |
| money_moving+pin_rlm | total | 7-11 | 38.9 | 40.4 | -1.5 | -4.47 | -24.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | total | 7-11 | 38.9 | 40.4 | -1.5 | -4.47 | -24.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 7-10 | 41.2 | 40.4 | 0.8 | -3.47 | -20.4 |  |  | keep collecting (17/30) |
| pin_rlm+rlm_ratio | total | 7-10 | 41.2 | 40.4 | 0.8 | -3.47 | -20.4 |  |  | keep collecting (17/30) |
| pin_rlm+sharp_gap | total | 7-11 | 38.9 | 40.4 | -1.5 | -4.47 | -24.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | total | 3-6 | 33.3 | 40.4 | -7.0 | -3.19 | -35.4 |  |  | keep collecting (9/30) |
| consensus_gap+pin_rlm | total | 0-1 | 0.0 | 40.4 | -40.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+pin_value | total | 1-1 | 50.0 | 40.4 | 9.6 | -0.09 | -4.5 |  |  | keep collecting (2/30) |

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
| rlm_quiet | both | 38-48 | 44.2 | 36.7 | 7.5 | +8.39 | 9.8 | 0.22 | 43.0 | DROP: below break-even |
| pin_move | both | 8-13 | 38.1 | 48.6 | -10.5 | -6.37 | -30.3 | 0.15 | 38.1 | keep collecting (21/30) |
| money_delta | both | 11-8 | 57.9 | 42.7 | 15.2 | +4.34 | 22.9 | -0.04 | 36.8 | keep collecting (19/30) |
| pin_rlm | both | 1-3 | 25.0 | 39.1 | -14.1 | -2.07 | -51.8 | -0.37 | 75.0 | keep collecting (4/30) |
| follow_move | both | 548-492 | 52.7 | 51.7 | 1.0 | -67.81 | -6.5 | 0.18 | 40.9 | no edge shown yet |
| rlm_ratio | both | 34-24 | 58.6 | 40.0 | 18.6 | +18.93 | 32.6 | 0.5 | 53.4 | no edge shown yet |
| money_level | both | 190-129 | 59.6 | 58.8 | 0.7 | -18.45 | -5.8 | -0.1 | 39.2 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 158-139 | 53.2 | 48.2 | 5.0 | +14.71 | 5.0 | 0.29 | 43.8 | no edge shown yet |
| money_moving | both | 120-96 | 55.6 | 51.1 | 4.5 | +1.07 | 0.5 | 0.13 | 43.1 | no edge shown yet |
| pin_value | both | 58-57 | 50.4 | 48.6 | 1.8 | -5.48 | -4.8 | 0.07 | 36.5 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.8 | -31.8 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 269-329 | 45.0 | 47.9 | -3.0 | -57.61 | -9.6 | 0.39 | 45.5 | DROP: below break-even |
| consensus_gap+money_level | both | 40-33 | 54.8 | 62.2 | -7.4 | -10.72 | -14.7 | 0.22 | 46.6 | no edge shown yet |
| consensus_gap+money_moving | both | 21-25 | 45.7 | 47.7 | -2.1 | -6.26 | -13.6 | 0.26 | 43.5 | no edge shown yet |
| consensus_gap+pin_value | both | 24-28 | 46.2 | 47.0 | -0.9 | -7.11 | -13.7 | 0.39 | 48.1 | no edge shown yet |
| follow_move+rlm_quiet | both | 38-48 | 44.2 | 36.7 | 7.5 | +8.39 | 9.8 | 0.22 | 43.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 34-24 | 58.6 | 40.0 | 18.6 | +18.93 | 32.6 | 0.5 | 53.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 81-47 | 63.3 | 49.4 | 13.9 | +21.62 | 16.9 | 0.41 | 48.4 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 73-48 | 60.3 | 57.9 | 2.4 | -3.14 | -2.6 | -0.08 | 46.3 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 13-10 | 56.5 | 50.3 | 6.2 | +1.63 | 7.1 | 0.47 | 47.8 | keep collecting (23/30) |
| money_moving+pin_value | both | 10-7 | 58.8 | 50.7 | 8.2 | +1.78 | 10.5 | 0.39 | 41.2 | keep collecting (17/30) |
| rlm_quiet+rlm_ratio | both | 20-14 | 58.8 | 36.8 | 22.0 | +14.73 | 43.3 | -0.04 | 47.1 | no edge shown yet |
| rlm_quiet+sharp_gap | both | 22-18 | 55.0 | 37.1 | 17.9 | +12.55 | 31.4 | -0.06 | 45.0 | no edge shown yet |
| rlm_ratio+sharp_gap | both | 34-24 | 58.6 | 40.0 | 18.6 | +18.93 | 32.6 | 0.5 | 53.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 104-70 | 59.8 | 55.4 | 4.4 | -0.4 | -0.2 | 0.16 | 44.3 | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | both | 71-57 | 55.5 | 48.8 | 6.7 | +7.27 | 5.7 | 0.28 | 46.9 | no edge shown yet |
| money_delta+money_level | both | 4-3 | 57.1 | 46.8 | 10.3 | +1.37 | 19.5 | 1.26 | 71.4 | keep collecting (7/30) |
| money_delta+money_moving | both | 10-8 | 55.6 | 42.3 | 13.2 | +3.43 | 19.1 | -0.04 | 38.9 | keep collecting (18/30) |
| money_delta+pin_value | both | 4-1 | 80.0 | 49.8 | 30.2 | +2.52 | 50.4 | 0.2 | 40.0 | keep collecting (5/30) |
| money_delta+sharp_gap | both | 8-6 | 57.1 | 42.1 | 15.1 | +3.69 | 26.4 | -0.05 | 50.0 | keep collecting (14/30) |
| pin_value+sharp_gap | both | 14-9 | 60.9 | 49.7 | 11.2 | +3.57 | 15.5 | -0.05 | 39.1 | keep collecting (23/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 37-46 | 44.6 | 51.3 | -6.7 | -16.34 | -19.7 | 0.75 | 56.6 | no edge shown yet |
| consensus_gap+rlm_quiet | both | 4-7 | 36.4 | 37.4 | -1.0 | -2.99 | -27.1 | 0.95 | 72.7 | keep collecting (11/30) |
| follow_move+pin_value | both | 23-21 | 52.3 | 48.7 | 3.5 | -0.86 | -2.0 | -0.21 | 27.3 | no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 42.7 | -26.0 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 30-48 | 38.5 | 45.7 | -7.2 | -10.13 | -13.0 | 0.81 | 50.0 | DROP: below break-even |
| follow_move+money_level | both | 96-52 | 64.9 | 59.7 | 5.2 | -4.25 | -2.9 | 0.04 | 43.2 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 12-10 | 54.5 | 44.2 | 10.4 | +2.34 | 10.6 | 1.43 | 68.2 | keep collecting (22/30) |
| pin_value+rlm_ratio | both | 3-2 | 60.0 | 45.2 | 14.8 | +0.73 | 14.5 | -1.16 | 40.0 | keep collecting (5/30) |
| follow_move+money_moving | both | 62-37 | 62.6 | 52.3 | 10.3 | +9.57 | 9.7 | 0.39 | 51.5 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 4-0 | 100.0 | 49.5 | 50.5 | +3.52 | 88.0 | 0.25 | 25.0 | keep collecting (4/30) |
| follow_move+money_delta | both | 6-4 | 60.0 | 42.7 | 17.3 | +3.86 | 38.6 | 0.34 | 50.0 | keep collecting (10/30) |
| money_delta+rlm_quiet | both | 2-2 | 50.0 | 38.0 | 12.0 | +1.53 | 38.3 | -2.1 | 0.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | both | 16-14 | 53.3 | 37.8 | 15.6 | +7.23 | 24.1 | 0.5 | 46.7 | no edge shown yet |
| money_moving+rlm_ratio | both | 17-10 | 63.0 | 42.4 | 20.6 | +10.06 | 37.3 | 0.61 | 55.6 | keep collecting (27/30) |
| consensus_gap+rlm_ratio | both | 5-4 | 55.6 | 39.7 | 15.9 | +1.0 | 11.1 | 0.72 | 66.7 | keep collecting (9/30) |
| pin_move+pin_value | both | 2-7 | 22.2 | 49.0 | -26.8 | -5.18 | -57.6 | 0.11 | 11.1 | keep collecting (9/30) |
| follow_move+pin_move | both | 6-6 | 50.0 | 50.5 | -0.5 | -1.19 | -9.9 | 0.45 | 50.0 | keep collecting (12/30) |
| consensus_gap+pin_move | both | 1-5 | 16.7 | 45.5 | -28.9 | -4.09 | -68.2 | 0.22 | 50.0 | keep collecting (6/30) |
| money_level+pin_move | both | 3-2 | 60.0 | 54.8 | 5.2 | +0.04 | 0.8 | 0.08 | 40.0 | keep collecting (5/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 28.1 | -28.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-2 | 33.3 | 42.7 | -9.4 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 28.1 | -28.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 28.1 | -28.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-2 | 33.3 | 42.7 | -9.4 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+sharp_gap | both | 1-3 | 25.0 | 39.1 | -14.1 | -2.07 | -51.8 | -0.37 | 75.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.0 | -51.0 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-1 | 66.7 | 50.4 | 16.3 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+pin_rlm | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.07 | -3.7 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 28.1 | 71.9 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 28.1 | 71.9 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 3-2 | 60.0 | 40.6 | 19.4 | +3.25 | 65.0 | 1.12 | 80.0 | keep collecting (5/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 28.1 | -28.1 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 20-31 | 39.2 | 28.1 | 11.1 | +9.1 | 17.8 | 0.03 | 43.1 | DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.4 | 10.6 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 15-15 | 50.0 | 49.2 | 0.8 | -1.36 | -4.5 | 0.7 | 50.0 | no edge shown yet |
| pin_move | moneyline | 2-3 | 40.0 | 45.6 | -5.6 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-6 | 14.3 | 48.7 | -34.4 | -5.09 | -72.7 | 0.29 | 28.6 | keep collecting (7/30) |
| pin_move | total | 5-4 | 55.6 | 50.1 | 5.4 | +0.59 | 6.5 | 0.11 | 33.3 | keep collecting (9/30) |
| money_delta | moneyline | 2-4 | 33.3 | 28.1 | 5.2 | +0.34 | 5.7 | -1.45 | 33.3 | keep collecting (6/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 8-3 | 72.7 | 49.3 | 23.4 | +4.17 | 37.9 | 0.64 | 36.4 | keep collecting (11/30) |
| pin_rlm | moneyline | 1-3 | 25.0 | 39.1 | -14.1 | -2.07 | -51.8 | -0.37 | 75.0 | keep collecting (4/30) |
| follow_move | moneyline | 225-151 | 59.8 | 54.9 | 5.0 | -22.91 | -6.1 | 0.12 | 43.9 | PROMOTE: beats break-even and its own base rate |
| follow_move | spread | 147-169 | 46.5 | 49.7 | -3.2 | -33.58 | -10.6 | -0.0 | 32.9 | DROP: below break-even |
| follow_move | total | 176-172 | 50.6 | 50.0 | 0.6 | -11.32 | -3.3 | 0.4 | 44.8 | no edge shown yet |
| rlm_ratio | moneyline | 14-14 | 50.0 | 29.7 | 20.3 | +10.47 | 37.4 | 0.47 | 57.1 | keep collecting (28/30) |
| rlm_ratio | spread | 3-3 | 50.0 | 52.0 | -2.0 | -0.16 | -2.7 | 0.33 | 16.7 | keep collecting (6/30) |
| rlm_ratio | total | 17-7 | 70.8 | 49.1 | 21.8 | +8.62 | 35.9 | 0.58 | 58.3 | keep collecting (24/30) |
| money_level | moneyline | 108-49 | 68.8 | 67.7 | 1.1 | -12.83 | -8.2 | -0.27 | 42.0 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-18 | 48.6 | 49.0 | -0.5 | -2.69 | -7.7 | 1.0 | 51.4 | no edge shown yet |
| money_level | total | 65-62 | 51.2 | 50.5 | 0.6 | -2.92 | -2.3 | -0.2 | 32.3 | no edge shown yet |
| sharp_gap | moneyline | 67-72 | 48.2 | 46.4 | 1.8 | -1.01 | -0.7 | 0.35 | 50.4 | no edge shown yet |
| sharp_gap | spread | 20-15 | 57.1 | 49.7 | 7.4 | +3.0 | 8.6 | 0.77 | 40.0 | no edge shown yet |
| sharp_gap | total | 71-52 | 57.7 | 49.8 | 8.0 | +12.71 | 10.3 | 0.09 | 37.4 | no edge shown yet |
| money_moving | moneyline | 53-49 | 52.0 | 52.6 | -0.6 | -12.73 | -12.5 | 0.03 | 49.0 | no edge shown yet |
| money_moving | spread | 18-6 | 75.0 | 49.0 | 26.0 | +10.18 | 42.4 | 0.5 | 45.8 | keep collecting (24/30) |
| money_moving | total | 49-41 | 54.4 | 49.9 | 4.5 | +3.63 | 4.0 | 0.14 | 35.6 | no edge shown yet |
| pin_value | moneyline | 2-7 | 22.2 | 37.9 | -15.6 | -5.31 | -59.0 | 0.12 | 55.6 | keep collecting (9/30) |
| pin_value | spread | 29-25 | 53.7 | 49.1 | 4.6 | +0.47 | 0.9 | 0.2 | 35.2 | no edge shown yet |
| pin_value | total | 27-25 | 51.9 | 50.0 | 1.9 | -0.65 | -1.2 | -0.08 | 34.6 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 53.1 | -19.7 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 109-183 | 37.3 | 46.3 | -8.9 | -53.55 | -18.3 | 0.11 | 42.5 | DROP: below break-even |
| consensus_gap | spread | 76-70 | 52.1 | 48.9 | 3.1 | -3.48 | -2.4 | 0.36 | 40.4 | no edge shown yet |
| consensus_gap | total | 84-76 | 52.5 | 50.1 | 2.4 | -0.57 | -0.4 | 0.91 | 55.6 | no edge shown yet |
| money_level+sharp_gap | moneyline | 49-24 | 67.1 | 62.9 | 4.2 | -4.34 | -5.9 | 0.05 | 53.4 | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+follow_move | moneyline | 14-23 | 37.8 | 54.1 | -16.3 | -13.83 | -37.4 | 0.17 | 54.1 | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 33.6 | -8.6 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| consensus_gap+rlm_quiet | moneyline | 1-5 | 16.7 | 28.1 | -11.5 | -3.68 | -61.3 | 1.07 | 83.3 | keep collecting (6/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.7 | -9.4 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 20-31 | 39.2 | 28.1 | 11.1 | +9.1 | 17.8 | 0.03 | 43.1 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 35-17 | 67.3 | 68.5 | -1.2 | -6.85 | -13.2 | -0.5 | 48.1 | beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 28.1 | -28.1 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 18-38 | 32.1 | 44.5 | -12.4 | -10.77 | -19.2 | 0.78 | 50.0 | DROP: below break-even |
| follow_move+money_level | moneyline | 61-19 | 76.2 | 68.0 | 8.2 | -3.05 | -3.8 | -0.3 | 43.8 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 33-15 | 68.8 | 55.5 | 13.3 | +5.06 | 10.5 | 0.18 | 54.2 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 29-23 | 55.8 | 67.7 | -11.9 | -10.38 | -20.0 | -0.06 | 44.2 | no edge shown yet |
| follow_move+sharp_gap | moneyline | 37-21 | 63.8 | 49.2 | 14.5 | +7.57 | 13.0 | 0.27 | 53.4 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 26-30 | 46.4 | 47.7 | -1.2 | -6.66 | -11.9 | 0.23 | 55.4 | no edge shown yet |
| consensus_gap+money_moving | moneyline | 11-23 | 32.4 | 47.4 | -15.1 | -13.01 | -38.3 | 0.24 | 47.1 | INVERT candidate: wrong well beyond its base rate |
| follow_move+rlm_ratio | moneyline | 14-14 | 50.0 | 29.7 | 20.3 | +10.47 | 37.4 | 0.47 | 57.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 10-10 | 50.0 | 28.1 | 21.9 | +9.6 | 48.0 | -0.12 | 45.0 | keep collecting (20/30) |
| rlm_quiet+sharp_gap | moneyline | 10-13 | 43.5 | 28.1 | 15.3 | +6.6 | 28.7 | -0.27 | 43.5 | keep collecting (23/30) |
| rlm_ratio+sharp_gap | moneyline | 14-14 | 50.0 | 29.7 | 20.3 | +10.47 | 37.4 | 0.47 | 57.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 28.1 | -3.1 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 7-9 | 43.8 | 28.1 | 15.6 | +4.13 | 25.8 | 0.75 | 56.2 | keep collecting (16/30) |
| money_moving+rlm_ratio | moneyline | 5-4 | 55.6 | 28.1 | 27.4 | +4.98 | 55.3 | 0.39 | 55.6 | keep collecting (9/30) |
| money_delta+money_moving | moneyline | 2-4 | 33.3 | 28.1 | 5.2 | +0.34 | 5.7 | -1.45 | 33.3 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-3 | 40.0 | 28.1 | 11.9 | +1.34 | 26.8 | -1.74 | 40.0 | keep collecting (5/30) |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 42.7 | -42.7 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-1 | 66.7 | 57.3 | 9.4 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | moneyline | 2-1 | 66.7 | 57.3 | 9.4 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 28.1 | -28.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-2 | 33.3 | 42.7 | -9.4 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 28.1 | -28.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 28.1 | -28.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-2 | 33.3 | 42.7 | -9.4 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+sharp_gap | moneyline | 1-3 | 25.0 | 39.1 | -14.1 | -2.07 | -51.8 | -0.37 | 75.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 28.1 | -28.1 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | -1.55 | 50.0 | keep collecting (2/30) |
| pin_move+sharp_gap | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.13 | 56.5 | -0.1 | 50.0 | keep collecting (2/30) |
| money_level+rlm_ratio | moneyline | 4-4 | 50.0 | 33.6 | 16.4 | +0.87 | 10.8 | 1.94 | 87.5 | keep collecting (8/30) |
| money_level+pin_rlm | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.07 | -3.7 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+pin_rlm | moneyline | 1-0 | 100.0 | 28.1 | 71.9 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 1-0 | 100.0 | 28.1 | 71.9 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 28.1 | 38.5 | +3.34 | 111.3 | -1.53 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 1-1 | 50.0 | 28.1 | 21.9 | +1.7 | 85.0 | -4.2 | 0.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 28.1 | 71.9 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 28.1 | -28.1 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-0 | 100.0 | 28.1 | 71.9 | +1.64 | 164.0 | 3.8 | 100.0 | keep collecting (1/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 71.9 | -71.9 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 71.9 | -71.9 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 46.9 | -1.5 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 46.9 | 36.4 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 12-8 | 60.0 | 48.5 | 11.5 | +2.3 | 11.5 | 0.45 | 45.0 | keep collecting (20/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.4 | 10.6 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-3 | 50.0 | 52.0 | -2.0 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-7 | 58.8 | 48.7 | 10.1 | +2.09 | 12.3 | 0.88 | 41.2 | keep collecting (17/30) |
| money_level+money_moving | spread | 10-6 | 62.5 | 48.5 | 14.0 | +3.12 | 19.5 | 1.19 | 68.8 | keep collecting (16/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.7 | -5.8 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 4-2 | 66.7 | 49.0 | 17.7 | +1.41 | 23.5 | 0.5 | 50.0 | keep collecting (6/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 3-3 | 50.0 | 52.0 | -2.0 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 53.1 | -53.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 53.1 | -53.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-12 | 53.8 | 49.1 | 4.8 | +0.62 | 2.4 | 1.15 | 46.2 | keep collecting (26/30) |
| money_moving+sharp_gap | spread | 10-4 | 71.4 | 49.1 | 22.3 | +5.04 | 36.0 | 0.86 | 50.0 | keep collecting (14/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.0 | 17.7 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-11 | 45.0 | 47.8 | -2.8 | -3.2 | -16.0 | 0.85 | 45.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 46.9 | 15.6 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 11-10 | 52.4 | 48.4 | 4.0 | +0.04 | 0.2 | 0.9 | 47.6 | keep collecting (21/30) |
| follow_move+pin_value | spread | 13-8 | 61.9 | 48.4 | 13.5 | +3.36 | 16.0 | 0.19 | 28.6 | keep collecting (21/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 46.9 | 53.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 46.9 | 53.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 46.9 | 53.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-3 | 75.0 | 48.0 | 27.0 | +5.22 | 43.5 | 0.75 | 50.0 | keep collecting (12/30) |
| money_delta+rlm_quiet | spread | 1-0 | 100.0 | 46.9 | 53.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 2-0 | 100.0 | 46.9 | 53.1 | +1.74 | 87.1 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 2-2 | 50.0 | 53.1 | -3.1 | -0.07 | -1.7 | 1.25 | 25.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | spread | 2-1 | 66.7 | 51.0 | 15.6 | +0.86 | 28.7 | 1.0 | 33.3 | keep collecting (3/30) |
| pin_move+pin_value | spread | 1-5 | 16.7 | 48.0 | -31.3 | -4.09 | -68.2 | 0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 46.9 | -46.9 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-3 | 25.0 | 46.9 | -21.9 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 53.1 | -53.1 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 15-15 | 50.0 | 49.2 | 0.8 | -1.36 | -4.5 | 0.7 | 50.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 28-25 | 52.8 | 50.4 | 2.5 | +0.59 | 1.1 | -0.04 | 37.7 | no edge shown yet |
| money_level+sharp_gap | total | 41-34 | 54.7 | 50.2 | 4.4 | +3.32 | 4.4 | -0.09 | 34.7 | no edge shown yet |
| money_moving+sharp_gap | total | 35-23 | 60.3 | 49.7 | 10.6 | +8.9 | 15.3 | 0.19 | 37.9 | no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 10-5 | 66.7 | 49.6 | 17.0 | +4.05 | 27.0 | 0.27 | 33.3 | keep collecting (15/30) |
| money_moving+pin_value | total | 6-4 | 60.0 | 49.5 | 10.5 | +1.38 | 13.8 | 0.2 | 30.0 | keep collecting (10/30) |
| pin_value+sharp_gap | total | 12-6 | 66.7 | 49.7 | 16.9 | +4.83 | 26.8 | 0.0 | 33.3 | keep collecting (18/30) |
| follow_move+money_level | total | 24-23 | 51.1 | 50.5 | 0.6 | -1.24 | -2.6 | 0.21 | 40.4 | no edge shown yet |
| follow_move+pin_value | total | 9-11 | 45.0 | 50.0 | -5.0 | -2.94 | -14.7 | -0.45 | 25.0 | keep collecting (20/30) |
| follow_move+rlm_ratio | total | 17-7 | 70.8 | 49.1 | 21.8 | +8.62 | 35.9 | 0.58 | 58.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 34-19 | 64.2 | 49.8 | 14.3 | +11.96 | 22.6 | 0.42 | 45.3 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 6-4 | 60.0 | 49.1 | 10.9 | +1.54 | 15.4 | 1.1 | 70.0 | keep collecting (10/30) |
| pin_value+rlm_ratio | total | 3-1 | 75.0 | 49.4 | 25.6 | +1.73 | 43.2 | -0.25 | 50.0 | keep collecting (4/30) |
| rlm_ratio+sharp_gap | total | 17-7 | 70.8 | 49.1 | 21.8 | +8.62 | 35.9 | 0.58 | 58.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 20-19 | 51.3 | 49.8 | 1.5 | -0.71 | -1.8 | 0.54 | 48.7 | no edge shown yet |
| consensus_gap+money_level | total | 6-4 | 60.0 | 50.5 | 9.5 | +1.34 | 13.4 | 0.0 | 30.0 | keep collecting (10/30) |
| consensus_gap+money_moving | total | 5-1 | 83.3 | 50.4 | 33.0 | +3.43 | 57.2 | -0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+pin_value | total | 10-14 | 41.7 | 50.3 | -8.6 | -5.11 | -21.3 | 0.5 | 50.0 | keep collecting (24/30) |
| consensus_gap+sharp_gap | total | 7-7 | 50.0 | 49.7 | 0.3 | -0.67 | -4.8 | 0.14 | 35.7 | keep collecting (14/30) |
| money_moving+rlm_ratio | total | 10-5 | 66.7 | 49.2 | 17.5 | +4.22 | 28.1 | 0.67 | 60.0 | keep collecting (15/30) |
| consensus_gap+follow_move | total | 14-12 | 53.8 | 49.9 | 3.9 | +0.69 | 2.7 | 1.5 | 69.2 | keep collecting (26/30) |
| consensus_gap+money_delta | total | 3-0 | 100.0 | 50.4 | 49.6 | +2.69 | 89.6 | 0.33 | 33.3 | keep collecting (3/30) |
| follow_move+money_delta | total | 3-3 | 50.0 | 49.2 | 0.8 | -0.31 | -5.2 | 1.33 | 66.7 | keep collecting (6/30) |
| money_delta+money_moving | total | 7-3 | 70.0 | 49.3 | 20.7 | +3.26 | 32.6 | 0.7 | 40.0 | keep collecting (10/30) |
| money_delta+pin_value | total | 3-0 | 100.0 | 49.6 | 50.4 | +2.69 | 89.6 | 0.0 | 33.3 | keep collecting (3/30) |
| money_delta+sharp_gap | total | 6-2 | 75.0 | 49.4 | 25.6 | +3.35 | 41.9 | 0.88 | 50.0 | keep collecting (8/30) |
| money_moving+rlm_quiet | total | 7-5 | 58.3 | 49.1 | 9.3 | +1.36 | 11.4 | 0.42 | 41.7 | keep collecting (12/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 9-3 | 75.0 | 49.1 | 25.9 | +5.22 | 43.5 | 0.33 | 58.3 | keep collecting (12/30) |
| rlm_quiet+sharp_gap | total | 11-4 | 73.3 | 49.0 | 24.3 | +6.04 | 40.3 | 0.47 | 53.3 | keep collecting (15/30) |
| follow_move+pin_move | total | 3-2 | 60.0 | 49.3 | 10.7 | +0.77 | 15.4 | 0.8 | 60.0 | keep collecting (5/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 3-2 | 60.0 | 49.3 | 10.7 | +0.73 | 14.5 | 0.8 | 60.0 | keep collecting (5/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 48.9 | 1.1 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 4-1 | 80.0 | 48.9 | 31.1 | +2.68 | 53.6 | 0.4 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | total | 1-1 | 50.0 | 51.1 | -1.1 | -0.09 | -4.5 | 0.0 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | total | 1-2 | 33.3 | 51.1 | -17.8 | -1.09 | -36.4 | 0.0 | 0.0 | keep collecting (3/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 1-2 | 33.3 | 48.9 | -15.5 | -1.09 | -36.4 | 1.67 | 100.0 | keep collecting (3/30) |
| consensus_gap+pin_move | total | 1-0 | 100.0 | 51.1 | 48.9 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 219-334 | 39.6 | 42.0 | -2.4 | -62.81 | -11.4 |  |  | DROP: below break-even |
| pin_move | both | 571-584 | 49.4 | 49.8 | -0.4 | -47.53 | -4.1 |  |  | DROP: below break-even |
| money_delta | both | 360-472 | 43.3 | 44.2 | -0.9 | -60.2 | -7.2 |  |  | DROP: below break-even |
| pin_rlm | both | 153-182 | 45.7 | 42.2 | 3.5 | +19.49 | 5.8 |  |  | DROP: below break-even |
| follow_move | both | 974-919 | 51.5 | 51.3 | 0.1 | -133.9 | -7.1 |  |  | no edge shown yet |
| rlm_ratio | both | 223-270 | 45.2 | 43.9 | 1.3 | -21.25 | -4.3 |  |  | DROP: below break-even |
| money_level | both | 1247-916 | 57.7 | 55.4 | 2.3 | -61.67 | -2.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 965-1110 | 46.5 | 47.5 | -1.0 | -145.19 | -7.0 |  |  | DROP: below break-even |
| money_moving | both | 970-1110 | 46.6 | 47.8 | -1.2 | -152.26 | -7.3 |  |  | DROP: below break-even |
| pin_value | both | 423-409 | 50.8 | 48.2 | 2.6 | +30.57 | 3.7 |  |  | no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 51.0 | 15.6 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 388-486 | 44.4 | 48.2 | -3.8 | -80.21 | -9.2 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 146-140 | 51.0 | 51.5 | -0.4 | -14.27 | -5.0 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 168-262 | 39.1 | 45.6 | -6.5 | -34.96 | -8.1 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 95-91 | 51.1 | 50.9 | 0.2 | +8.33 | 4.5 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 24-42 | 36.4 | 38.4 | -2.1 | +8.03 | 12.2 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 156-160 | 49.4 | 46.3 | 3.1 | +14.63 | 4.6 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | both | 28-47 | 37.3 | 39.9 | -2.6 | -2.86 | -3.8 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 167-266 | 38.6 | 45.1 | -6.5 | -35.67 | -8.2 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 512-561 | 47.7 | 49.1 | -1.4 | -95.92 | -8.9 |  |  | DROP: below break-even |
| follow_move+pin_move | both | 404-429 | 48.5 | 50.0 | -1.5 | -62.35 | -7.5 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 119-132 | 47.4 | 43.8 | 3.6 | -2.46 | -1.0 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 145-137 | 51.4 | 49.1 | 2.4 | +1.97 | 0.7 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 223-270 | 45.2 | 43.9 | 1.3 | -21.25 | -4.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 518-559 | 48.1 | 48.9 | -0.8 | -84.88 | -7.9 |  |  | DROP: below break-even |
| money_moving+pin_move | both | 330-364 | 47.6 | 48.5 | -0.9 | -32.91 | -4.7 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 147-177 | 45.4 | 42.2 | 3.2 | +18.52 | 5.7 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 179-206 | 46.5 | 47.4 | -0.9 | -11.94 | -3.1 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 215-261 | 45.2 | 44.0 | 1.2 | -20.16 | -4.2 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 928-1067 | 46.5 | 47.6 | -1.0 | -134.09 | -6.7 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 141-150 | 48.5 | 44.0 | 4.4 | +17.36 | 6.0 |  |  | no edge shown yet |
| pin_move+pin_value | both | 182-176 | 50.8 | 49.2 | 1.6 | -2.64 | -0.7 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 126-128 | 49.6 | 45.3 | 4.4 | +6.89 | 2.7 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 335-366 | 47.8 | 48.3 | -0.5 | -30.45 | -4.3 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 42-43 | 49.4 | 45.8 | 3.6 | +12.4 | 14.6 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 119-132 | 47.4 | 43.8 | 3.6 | -2.46 | -1.0 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 153-182 | 45.7 | 42.2 | 3.5 | +19.49 | 5.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 41-33 | 55.4 | 48.4 | 7.0 | +4.42 | 6.0 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 180-205 | 46.8 | 47.3 | -0.6 | -10.05 | -2.6 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 223-270 | 45.2 | 43.9 | 1.3 | -21.25 | -4.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 176-213 | 45.2 | 45.7 | -0.5 | -35.84 | -9.2 |  |  | DROP: below break-even |
| money_level+money_moving | both | 683-599 | 53.3 | 52.3 | 1.0 | -46.93 | -3.7 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 670-589 | 53.2 | 52.1 | 1.1 | -39.02 | -3.1 |  |  | no edge shown yet |
| follow_move+money_level | both | 621-449 | 58.0 | 56.2 | 1.8 | -52.07 | -4.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 105-90 | 53.8 | 48.0 | 5.9 | +11.01 | 5.6 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 243-186 | 56.6 | 58.1 | -1.5 | -19.95 | -4.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_move | both | 325-299 | 52.1 | 53.0 | -1.0 | -33.0 | -5.3 |  |  | no edge shown yet |
| money_level+pin_value | both | 199-177 | 52.9 | 50.0 | 2.9 | -3.73 | -1.0 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 24-54 | 30.8 | 37.2 | -6.4 | -11.44 | -14.7 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | both | 219-334 | 39.6 | 42.0 | -2.4 | -62.81 | -11.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 113-187 | 37.7 | 41.4 | -3.7 | -43.7 | -14.6 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 258-365 | 41.4 | 42.5 | -1.1 | -47.27 | -7.6 |  |  | DROP: below break-even |
| consensus_gap+money_delta | both | 47-111 | 29.7 | 37.8 | -8.1 | -23.62 | -14.9 |  |  | DROP: below break-even |
| money_delta+money_level | both | 127-117 | 52.0 | 47.0 | 5.1 | +15.64 | 6.4 |  |  | no edge shown yet |
| money_delta+pin_value | both | 79-75 | 51.3 | 47.1 | 4.2 | +4.02 | 2.6 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 255-359 | 41.5 | 42.5 | -1.0 | -44.44 | -7.2 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 89-155 | 36.5 | 40.0 | -3.5 | -34.76 | -14.2 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | both | 105-182 | 36.6 | 41.3 | -4.7 | -44.6 | -15.5 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 64-115 | 35.8 | 42.7 | -7.0 | -44.3 | -24.7 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | both | 108-142 | 43.2 | 44.2 | -1.0 | -19.45 | -7.8 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 47-77 | 37.9 | 40.6 | -2.7 | -18.59 | -15.0 |  |  | DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 51.0 | 15.6 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 131-156 | 45.6 | 46.2 | -0.5 | -14.48 | -5.0 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 68-48 | 58.6 | 46.6 | 12.0 | +18.99 | 16.4 |  |  | no edge shown yet |
| money_delta+pin_rlm | both | 90-108 | 45.5 | 42.1 | 3.4 | +6.25 | 3.2 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | both | 127-142 | 47.2 | 44.4 | 2.8 | -9.76 | -3.6 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | both | 32-42 | 43.2 | 47.2 | -3.9 | -2.57 | -3.5 |  |  | DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 48.9 | 51.1 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 66-143 | 31.6 | 29.0 | 2.6 | -12.83 | -6.1 |  |  | DROP: below break-even |
| rlm_quiet | spread | 52-55 | 48.6 | 51.1 | -2.5 | -6.73 | -6.3 |  |  | no edge shown yet |
| rlm_quiet | total | 101-136 | 42.6 | 49.4 | -6.8 | -43.24 | -18.2 |  |  | DROP: below break-even |
| pin_move | moneyline | 124-120 | 50.8 | 48.9 | 1.9 | +8.77 | 3.6 |  |  | no edge shown yet |
| pin_move | spread | 221-234 | 48.6 | 50.3 | -1.7 | -32.65 | -7.2 |  |  | DROP: below break-even |
| pin_move | total | 226-230 | 49.6 | 49.8 | -0.2 | -23.65 | -5.2 |  |  | no edge shown yet |
| money_delta | moneyline | 61-184 | 24.9 | 29.9 | -5.0 | -45.51 | -18.6 |  |  | DROP: below break-even |
| money_delta | spread | 128-129 | 49.8 | 51.1 | -1.3 | -12.31 | -4.8 |  |  | no edge shown yet |
| money_delta | total | 171-159 | 51.8 | 49.3 | 2.5 | -2.37 | -0.7 |  |  | no edge shown yet |
| pin_rlm | moneyline | 43-84 | 33.9 | 29.9 | 4.0 | +16.73 | 13.2 |  |  | DROP: below break-even |
| pin_rlm | spread | 26-23 | 53.1 | 51.3 | 1.7 | +0.7 | 1.4 |  |  | no edge shown yet |
| pin_rlm | total | 84-75 | 52.8 | 49.2 | 3.6 | +2.06 | 1.3 |  |  | no edge shown yet |
| follow_move | moneyline | 358-257 | 58.2 | 54.7 | 3.6 | -33.28 | -5.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 278-302 | 47.9 | 49.6 | -1.6 | -49.14 | -8.5 |  |  | DROP: below break-even |
| follow_move | total | 338-360 | 48.4 | 49.9 | -1.5 | -51.49 | -7.4 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 45-104 | 30.2 | 30.8 | -0.6 | -17.97 | -12.1 |  |  | DROP: below break-even |
| rlm_ratio | spread | 41-45 | 47.7 | 50.2 | -2.5 | -7.76 | -9.0 |  |  | no edge shown yet |
| rlm_ratio | total | 137-121 | 53.1 | 49.3 | 3.8 | +4.48 | 1.7 |  |  | no edge shown yet |
| money_level | moneyline | 482-195 | 71.2 | 67.8 | 3.4 | -32.83 | -4.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 346-355 | 49.4 | 49.0 | 0.3 | -42.92 | -6.1 |  |  | DROP: below break-even |
| money_level | total | 419-366 | 53.4 | 50.3 | 3.1 | +14.08 | 1.8 |  |  | no edge shown yet |
| sharp_gap | moneyline | 243-377 | 39.2 | 42.5 | -3.3 | -67.6 | -10.9 |  |  | DROP: below break-even |
| sharp_gap | spread | 351-342 | 50.6 | 49.4 | 1.2 | -25.21 | -3.6 |  |  | no edge shown yet |
| sharp_gap | total | 371-391 | 48.7 | 49.8 | -1.1 | -52.39 | -6.9 |  |  | DROP: below break-even |
| money_moving | moneyline | 255-363 | 41.3 | 43.6 | -2.4 | -53.93 | -8.7 |  |  | DROP: below break-even |
| money_moving | spread | 348-345 | 50.2 | 49.4 | 0.9 | -31.08 | -4.5 |  |  | no edge shown yet |
| money_moving | total | 367-402 | 47.7 | 49.8 | -2.1 | -67.25 | -8.7 |  |  | DROP: below break-even |
| pin_value | moneyline | 23-55 | 29.5 | 32.6 | -3.1 | +30.04 | 38.5 |  |  | DROP: below break-even |
| pin_value | spread | 188-170 | 52.5 | 49.5 | 3.0 | -6.17 | -1.7 |  |  | no edge shown yet |
| pin_value | total | 212-184 | 53.5 | 50.2 | 3.3 | +6.71 | 1.7 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 53.1 | 46.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 172-294 | 36.9 | 46.8 | -9.9 | -76.79 | -16.5 |  |  | DROP: below break-even |
| consensus_gap | spread | 95-82 | 53.7 | 48.9 | 4.8 | -0.94 | -0.5 |  |  | no edge shown yet |
| consensus_gap | total | 121-110 | 52.4 | 50.6 | 1.8 | -2.48 | -1.1 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 176-101 | 63.5 | 62.4 | 1.1 | -7.86 | -2.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 163-99 | 62.2 | 61.9 | 0.4 | -8.1 | -3.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 228-348 | 39.6 | 42.6 | -3.0 | -50.25 | -8.7 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 63-75 | 45.7 | 53.5 | -7.8 | -21.65 | -15.7 |  |  | DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 8-42 | 16.0 | 29.9 | -13.9 | -13.64 | -27.3 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 66-143 | 31.6 | 29.0 | 2.6 | -12.83 | -6.1 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 120-75 | 61.5 | 68.3 | -6.7 | -16.25 | -8.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 67-164 | 29.0 | 42.1 | -13.1 | -24.92 | -10.8 |  |  | !! CHECK: consensus_gap+money_moving close moneyline all sits -13.1 pts from its base (42.1%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+money_level | moneyline | 271-96 | 73.8 | 69.0 | 4.8 | -16.61 | -4.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+money_moving | moneyline | 125-138 | 47.5 | 47.8 | -0.2 | -24.57 | -9.3 |  |  | DROP: below break-even |
| money_delta+money_moving | moneyline | 57-166 | 25.6 | 29.5 | -3.9 | -31.33 | -14.0 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 55-165 | 25.0 | 29.5 | -4.5 | -32.52 | -14.8 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 65-170 | 27.7 | 41.2 | -13.5 | -28.52 | -12.1 |  |  | !! CHECK: consensus_gap+sharp_gap close moneyline all sits -13.5 pts from its base (41.2%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+sharp_gap | moneyline | 121-139 | 46.5 | 46.8 | -0.3 | -25.92 | -10.0 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | moneyline | 29-86 | 25.2 | 28.9 | -3.7 | -18.19 | -15.8 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 30-89 | 25.2 | 28.9 | -3.7 | -21.73 | -18.3 |  |  | DROP: below break-even |
| consensus_gap+pin_move | moneyline | 37-38 | 49.3 | 52.6 | -3.3 | +10.71 | 14.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 11-30 | 26.8 | 31.3 | -4.5 | +8.65 | 21.1 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 5-34 | 12.8 | 30.4 | -17.6 | -10.04 | -25.7 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 96-85 | 53.0 | 50.4 | 2.7 | +0.51 | 0.3 |  |  | no edge shown yet |
| follow_move+pin_rlm | moneyline | 28-48 | 36.8 | 30.4 | 6.4 | -2.1 | -2.8 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 45-104 | 30.2 | 30.8 | -0.6 | -17.97 | -12.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 53-69 | 43.4 | 42.5 | 1.0 | +10.02 | 8.2 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 42-81 | 34.1 | 29.9 | 4.2 | +18.33 | 14.9 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 44-98 | 31.0 | 30.9 | 0.1 | -13.37 | -9.4 |  |  | DROP: below break-even |
| pin_move+pin_rlm | moneyline | 31-52 | 37.3 | 29.7 | 7.6 | +14.61 | 17.6 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 29-44 | 39.7 | 29.9 | 9.8 | +5.61 | 7.7 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 24-36 | 40.0 | 31.0 | 9.0 | +5.38 | 9.0 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 53-71 | 42.7 | 41.9 | 0.9 | +7.85 | 6.3 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 16-40 | 28.6 | 29.7 | -1.1 | -10.1 | -18.0 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 28-48 | 36.8 | 30.4 | 6.4 | -2.1 | -2.8 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 43-84 | 33.9 | 29.9 | 4.0 | +16.73 | 13.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 27-85 | 24.1 | 28.9 | -4.8 | -21.57 | -19.3 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 45-104 | 30.2 | 30.8 | -0.6 | -17.97 | -12.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 14-83 | 14.4 | 29.9 | -15.5 | -24.27 | -25.0 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 16-45 | 26.2 | 31.7 | -5.5 | +7.85 | 12.9 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 19-39 | 32.8 | 31.2 | 1.6 | -0.06 | -0.1 |  |  | DROP: below break-even |
| money_delta+pin_rlm | moneyline | 25-50 | 33.3 | 29.9 | 3.4 | +4.73 | 6.3 |  |  | DROP: below break-even |
| money_delta+pin_value | moneyline | 3-18 | 14.3 | 28.1 | -13.8 | -6.68 | -31.8 |  |  | keep collecting (21/30) |
| money_moving+pin_value | moneyline | 11-33 | 25.0 | 31.1 | -6.1 | +12.94 | 29.4 |  |  | DROP: below break-even |
| pin_move+pin_value | moneyline | 7-10 | 41.2 | 35.9 | 5.3 | +7.35 | 43.2 |  |  | keep collecting (17/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 28.1 | 3.1 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 11-35 | 23.9 | 31.0 | -7.1 | +10.94 | 23.8 |  |  | DROP: below break-even |
| follow_move+money_delta | moneyline | 29-61 | 32.2 | 32.5 | -0.3 | -18.05 | -20.1 |  |  | DROP: below break-even |
| money_delta+money_level | moneyline | 17-24 | 41.5 | 33.5 | 8.0 | +8.68 | 21.2 |  |  | no edge shown yet |
| money_delta+rlm_ratio | moneyline | 25-51 | 32.9 | 31.6 | 1.3 | -11.64 | -15.3 |  |  | DROP: below break-even |
| money_level+pin_move | moneyline | 77-47 | 62.1 | 66.2 | -4.1 | -5.85 | -4.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 12-10 | 54.5 | 34.1 | 20.4 | +5.79 | 26.3 |  |  | keep collecting (22/30) |
| money_level+rlm_ratio | moneyline | 15-14 | 51.7 | 38.7 | 13.0 | +5.04 | 17.4 |  |  | keep collecting (29/30) |
| money_delta+rlm_quiet | moneyline | 18-47 | 27.7 | 30.2 | -2.5 | -18.61 | -28.6 |  |  | DROP: below break-even |
| money_level+pin_value | moneyline | 5-3 | 62.5 | 66.4 | -3.9 | -0.32 | -4.0 |  |  | keep collecting (8/30) |
| follow_move+pin_value | moneyline | 3-8 | 27.3 | 36.1 | -8.8 | +4.8 | 43.7 |  |  | keep collecting (11/30) |
| pin_value+rlm_quiet | moneyline | 2-6 | 25.0 | 28.1 | -3.1 | +6.12 | 76.5 |  |  | keep collecting (8/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 28.1 | -3.1 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 36-28 | 56.2 | 48.3 | 8.0 | +2.72 | 4.3 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 49-46 | 51.6 | 48.6 | 3.0 | -4.18 | -4.4 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 27-30 | 47.4 | 49.1 | -1.7 | -6.91 | -12.1 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 68-52 | 56.7 | 48.8 | 7.9 | +5.87 | 4.9 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 4-4 | 50.0 | 50.0 | 0.0 | -0.67 | -8.3 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | spread | 48-46 | 51.1 | 48.8 | 2.2 | -5.08 | -5.4 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 163-169 | 49.1 | 49.1 | 0.0 | -21.6 | -6.5 |  |  | no edge shown yet |
| follow_move+pin_move | spread | 137-159 | 46.3 | 50.0 | -3.7 | -34.16 | -11.5 |  |  | DROP: below break-even |
| follow_move+pin_rlm | spread | 19-19 | 50.0 | 51.0 | -1.0 | -1.65 | -4.3 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 64-56 | 53.3 | 48.9 | 4.4 | -0.1 | -0.1 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 41-45 | 47.7 | 50.2 | -2.5 | -7.76 | -9.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 164-168 | 49.4 | 49.1 | 0.2 | -19.47 | -5.9 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 124-133 | 48.2 | 49.8 | -1.5 | -20.66 | -8.0 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 24-23 | 51.1 | 51.2 | -0.2 | -1.13 | -2.4 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 87-88 | 49.7 | 49.0 | 0.7 | -12.82 | -7.3 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 39-44 | 47.0 | 50.1 | -3.1 | -8.69 | -10.5 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 343-337 | 50.4 | 49.4 | 1.1 | -27.58 | -4.1 |  |  | no edge shown yet |
| pin_move+pin_rlm | spread | 26-23 | 53.1 | 51.3 | 1.7 | +0.7 | 1.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 86-86 | 50.0 | 49.7 | 0.3 | -10.23 | -5.9 |  |  | no edge shown yet |
| pin_move+rlm_ratio | spread | 22-26 | 45.8 | 50.8 | -4.9 | -5.94 | -12.4 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 127-133 | 48.8 | 49.8 | -1.0 | -17.93 | -6.9 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 8-10 | 44.4 | 51.0 | -6.6 | -2.97 | -16.5 |  |  | keep collecting (18/30) |
| pin_rlm+rlm_ratio | spread | 19-19 | 50.0 | 51.0 | -1.0 | -1.65 | -4.3 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 26-23 | 53.1 | 51.3 | 1.7 | +0.7 | 1.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 7-8 | 46.7 | 49.4 | -2.7 | -2.01 | -13.4 |  |  | keep collecting (15/30) |
| pin_value+sharp_gap | spread | 87-88 | 49.7 | 49.1 | 0.6 | -12.88 | -7.4 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 41-45 | 47.7 | 50.2 | -2.5 | -7.76 | -9.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 159-170 | 48.3 | 48.8 | -0.5 | -26.15 | -7.9 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 21-28 | 42.9 | 49.8 | -7.0 | -9.13 | -18.6 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 267-264 | 50.3 | 49.0 | 1.3 | -23.44 | -4.4 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 59-51 | 53.6 | 48.3 | 5.3 | -0.53 | -0.5 |  |  | no edge shown yet |
| money_level+money_moving | spread | 266-265 | 50.1 | 49.0 | 1.1 | -25.36 | -4.8 |  |  | no edge shown yet |
| money_level+pin_move | spread | 112-133 | 45.7 | 49.5 | -3.8 | -31.91 | -13.0 |  |  | DROP: below break-even |
| money_level+pin_value | spread | 93-93 | 50.0 | 48.7 | 1.3 | -12.74 | -6.8 |  |  | no edge shown yet |
| consensus_gap+money_delta | spread | 15-14 | 51.7 | 50.7 | 1.0 | -1.18 | -4.1 |  |  | keep collecting (29/30) |
| follow_move+money_delta | spread | 41-49 | 45.6 | 50.4 | -4.9 | -11.82 | -13.1 |  |  | no edge shown yet |
| money_delta+money_level | spread | 41-41 | 50.0 | 50.0 | 0.0 | -4.05 | -4.9 |  |  | no edge shown yet |
| money_delta+money_moving | spread | 71-76 | 48.3 | 50.6 | -2.3 | -11.91 | -8.1 |  |  | no edge shown yet |
| money_delta+pin_value | spread | 33-27 | 55.0 | 50.7 | 4.3 | +1.79 | 3.0 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 70-74 | 48.6 | 50.5 | -1.9 | -10.89 | -7.6 |  |  | no edge shown yet |
| follow_move+rlm_quiet | spread | 52-55 | 48.6 | 51.1 | -2.5 | -6.73 | -6.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 14-5 | 73.7 | 51.1 | 22.6 | +7.78 | 40.9 |  |  | keep collecting (19/30) |
| rlm_quiet+sharp_gap | spread | 22-12 | 64.7 | 51.3 | 13.4 | +8.13 | 23.9 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 14-11 | 56.0 | 50.6 | 5.4 | +1.57 | 6.3 |  |  | keep collecting (25/30) |
| money_delta+pin_move | spread | 38-45 | 45.8 | 51.3 | -5.5 | -10.27 | -12.4 |  |  | no edge shown yet |
| money_delta+rlm_ratio | spread | 16-27 | 37.2 | 49.9 | -12.7 | -12.78 | -29.7 |  |  | DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 53.1 | 46.9 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_rlm | spread | 13-16 | 44.8 | 51.0 | -6.1 | -4.31 | -14.8 |  |  | keep collecting (29/30) |
| money_delta+rlm_quiet | spread | 17-18 | 48.6 | 51.7 | -3.1 | -2.27 | -6.5 |  |  | no edge shown yet |
| money_moving+rlm_quiet | spread | 21-12 | 63.6 | 51.2 | 12.4 | +7.18 | 21.7 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 30-29 | 50.8 | 51.6 | -0.8 | -1.14 | -1.9 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-2 | 75.0 | 52.3 | 22.7 | +3.56 | 44.5 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_quiet | spread | 4-3 | 57.1 | 51.3 | 5.8 | +0.48 | 6.9 |  |  | keep collecting (7/30) |
| pin_value+rlm_quiet | spread | 6-6 | 50.0 | 50.0 | 0.0 | -0.7 | -5.8 |  |  | keep collecting (12/30) |
| follow_move+money_delta | total | 106-103 | 50.7 | 49.4 | 1.3 | -5.97 | -2.9 |  |  | no edge shown yet |
| money_level+money_moving | total | 241-233 | 50.8 | 50.1 | 0.7 | -13.71 | -2.9 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 240-226 | 51.5 | 50.1 | 1.4 | -7.48 | -1.6 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 357-382 | 48.3 | 49.8 | -1.5 | -56.27 | -7.6 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 64-60 | 51.6 | 50.9 | 0.7 | -3.17 | -2.6 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 31-23 | 57.4 | 50.5 | 6.9 | +4.52 | 8.4 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 72-63 | 53.3 | 50.6 | 2.8 | +0.91 | 0.7 |  |  | no edge shown yet |
| follow_move+money_moving | total | 224-254 | 46.9 | 49.8 | -2.9 | -49.75 | -10.4 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 233-252 | 48.0 | 49.8 | -1.7 | -39.5 | -8.1 |  |  | DROP: below break-even |
| money_level+pin_move | total | 136-119 | 53.3 | 50.1 | 3.3 | +4.76 | 1.9 |  |  | no edge shown yet |
| money_level+pin_value | total | 101-81 | 55.5 | 50.6 | 4.9 | +9.33 | 5.1 |  |  | no edge shown yet |
| pin_move+pin_value | total | 89-80 | 52.7 | 50.0 | 2.6 | +0.24 | 0.1 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 101-136 | 42.6 | 49.4 | -6.8 | -43.24 | -18.2 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 153-162 | 48.6 | 49.7 | -1.1 | -22.28 | -7.1 |  |  | no edge shown yet |
| rlm_quiet+sharp_gap | total | 61-86 | 41.5 | 49.2 | -7.7 | -30.09 | -20.5 |  |  | DROP: below break-even |
| money_delta+money_moving | total | 130-123 | 51.4 | 49.3 | 2.0 | -4.04 | -1.6 |  |  | no edge shown yet |
| follow_move+money_level | total | 191-183 | 51.1 | 50.2 | 0.9 | -9.31 | -2.5 |  |  | no edge shown yet |
| follow_move+pin_value | total | 78-73 | 51.7 | 50.1 | 1.6 | -2.73 | -1.8 |  |  | no edge shown yet |
| money_moving+pin_value | total | 81-85 | 48.8 | 50.1 | -1.3 | -12.06 | -7.3 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 82-82 | 50.0 | 50.0 | -0.0 | -8.11 | -4.9 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 52-52 | 50.0 | 50.5 | -0.5 | -5.85 | -5.6 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 54-50 | 51.9 | 50.5 | 1.4 | -2.07 | -2.0 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 47-37 | 56.0 | 50.6 | 5.3 | +4.66 | 5.5 |  |  | no edge shown yet |
| consensus_gap+money_delta | total | 18-14 | 56.2 | 50.1 | 6.2 | +1.83 | 5.7 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | total | 12-9 | 57.1 | 49.7 | 7.4 | +1.72 | 8.2 |  |  | keep collecting (21/30) |
| money_delta+rlm_quiet | total | 29-50 | 36.7 | 49.1 | -12.4 | -23.41 | -29.6 |  |  | DROP: below break-even |
| money_delta+sharp_gap | total | 130-120 | 52.0 | 49.3 | 2.7 | -1.03 | -0.4 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 55-84 | 39.6 | 49.2 | -9.7 | -33.59 | -24.2 |  |  | DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 69-52 | 57.0 | 49.5 | 7.5 | +11.01 | 9.1 |  |  | no edge shown yet |
| money_delta+pin_move | total | 74-72 | 50.7 | 49.2 | 1.5 | -4.15 | -2.8 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 155-162 | 48.9 | 49.6 | -0.7 | -20.37 | -6.4 |  |  | no edge shown yet |
| follow_move+pin_move | total | 171-185 | 48.0 | 49.8 | -1.7 | -28.7 | -8.1 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | total | 24-30 | 44.4 | 49.4 | -4.9 | -7.99 | -14.8 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | total | 10-9 | 52.6 | 50.1 | 2.6 | -0.13 | -0.7 |  |  | keep collecting (19/30) |
| consensus_gap+rlm_ratio | total | 19-9 | 67.9 | 50.2 | 17.6 | +7.85 | 28.0 |  |  | keep collecting (28/30) |
| follow_move+pin_rlm | total | 72-65 | 52.6 | 49.2 | 3.3 | +1.29 | 0.9 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 137-121 | 53.1 | 49.3 | 3.8 | +4.48 | 1.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 42-27 | 60.9 | 49.2 | 11.7 | +11.63 | 16.9 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 69-48 | 59.0 | 49.5 | 9.5 | +15.1 | 12.9 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 81-73 | 52.6 | 49.2 | 3.4 | +1.32 | 0.9 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 132-119 | 52.6 | 49.3 | 3.2 | +1.9 | 0.8 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 84-75 | 52.8 | 49.2 | 3.6 | +2.06 | 1.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 80-66 | 54.8 | 49.3 | 5.5 | +7.45 | 5.1 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 29-22 | 56.9 | 49.4 | 7.4 | +4.3 | 8.4 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 72-65 | 52.6 | 49.2 | 3.3 | +1.29 | 0.9 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 84-75 | 52.8 | 49.2 | 3.6 | +2.06 | 1.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 33-22 | 60.0 | 49.6 | 10.4 | +7.91 | 14.4 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 137-121 | 53.1 | 49.3 | 3.8 | +4.48 | 1.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 52-42 | 55.3 | 49.1 | 6.2 | +5.82 | 6.2 |  |  | no edge shown yet |
| money_delta+rlm_ratio | total | 86-64 | 57.3 | 49.3 | 8.1 | +14.65 | 9.8 |  |  | no edge shown yet |
| money_delta+pin_value | total | 43-30 | 58.9 | 49.5 | 9.4 | +8.92 | 12.2 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 49-69 | 41.5 | 49.4 | -7.8 | -23.92 | -20.3 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | total | 25-35 | 41.7 | 49.1 | -7.5 | -12.04 | -20.1 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | total | 48-65 | 42.5 | 49.1 | -6.7 | -20.96 | -18.5 |  |  | DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 48.9 | 51.1 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| rlm_quiet | close | 1-3k bets | 146-221 | 39.8 | -2.1 | -9.1 |  |
| rlm_quiet | close | 3k+ bets | 47-68 | 40.9 | -2.0 | -11.5 |  |
| rlm_quiet | close | <1k bets | 26-45 | 36.6 | -4.7 | -23.0 |  |
| rlm_quiet | close | pin $1-2k | 60-108 | 35.7 | -7.5 | -20.4 |  |
| rlm_quiet | close | pin $2k+ | 65-79 | 45.1 | 6.5 | 3.6 |  |
| rlm_quiet | close | pin limit <$1k | 41-44 | 48.2 | -0.7 | -7.5 |  |
| pin_move | close | 1-3k bets | 365-368 | 49.8 | 0.1 | -3.1 |  |
| pin_move | close | 3k+ bets | 129-137 | 48.5 | -1.1 | -6.2 |  |
| pin_move | close | <1k bets | 77-79 | 49.4 | -1.1 | -5.4 |  |
| pin_move | close | pin $1-2k | 268-267 | 50.1 | 0.0 | -1.7 |  |
| pin_move | close | pin $2k+ | 201-215 | 48.3 | -1.3 | -8.1 |  |
| pin_move | close | pin limit <$1k | 102-102 | 50.0 | 0.6 | -2.2 |  |
| money_delta | close | 1-3k bets | 227-287 | 44.2 | -0.6 | -7.2 |  |
| money_delta | close | 3k+ bets | 85-113 | 42.9 | -0.6 | -2.0 |  |
| money_delta | close | <1k bets | 48-72 | 40.0 | -2.5 | -16.1 |  |
| money_delta | close | pin $1-2k | 130-129 | 50.2 | 4.2 | 5.3 |  |
| money_delta | close | pin $2k+ | 89-123 | 42.0 | 0.6 | -10.7 |  |
| money_delta | close | pin limit <$1k | 58-65 | 47.2 | -1.7 | -6.0 |  |
| pin_rlm | close | 1-3k bets | 97-110 | 46.9 | 4.5 | 11.9 |  |
| pin_rlm | close | 3k+ bets | 34-48 | 41.5 | -0.8 | -9.4 |  |
| pin_rlm | close | <1k bets | 22-24 | 47.8 | 6.6 | 5.5 |  |
| pin_rlm | close | pin $1-2k | 68-72 | 48.6 | 4.8 | 10.3 |  |
| pin_rlm | close | pin $2k+ | 41-73 | 36.0 | 0.0 | -6.4 |  |
| pin_rlm | close | pin limit <$1k | 44-37 | 54.3 | 6.1 | 15.2 |  |
| follow_move | close | 1-3k bets | 629-589 | 51.6 | 0.6 | -5.9 |  |
| follow_move | close | 3k+ bets | 202-191 | 51.4 | -0.4 | -5.9 |  |
| follow_move | close | <1k bets | 143-139 | 50.7 | -1.5 | -13.8 |  |
| follow_move | close | pin $1-2k | 303-336 | 47.4 | -3.2 | -11.2 |  |
| follow_move | close | pin $2k+ | 252-219 | 53.5 | 1.8 | -2.7 |  |
| follow_move | close | pin limit <$1k | 120-127 | 48.6 | -1.1 | -7.2 |  |
| rlm_ratio | close | 1-3k bets | 143-190 | 42.9 | -1.0 | -8.5 |  |
| rlm_ratio | close | 3k+ bets | 51-47 | 52.0 | 7.5 | 11.3 |  |
| rlm_ratio | close | <1k bets | 29-33 | 46.8 | 4.0 | -6.3 |  |
| rlm_ratio | close | pin $1-2k | 81-81 | 50.0 | 4.5 | 3.9 |  |
| rlm_ratio | close | pin $2k+ | 40-62 | 39.2 | 1.1 | -13.2 |  |
| rlm_ratio | close | pin limit <$1k | 49-44 | 52.7 | 4.1 | 1.7 |  |
| money_level | close | 1-3k bets | 801-578 | 58.1 | 2.6 | -2.3 |  |
| money_level | close | 3k+ bets | 263-208 | 55.8 | 0.9 | -3.1 |  |
| money_level | close | <1k bets | 183-129 | 58.7 | 3.0 | -4.5 |  |
| money_level | close | pin $1-2k | 372-313 | 54.3 | 0.4 | -3.4 |  |
| money_level | close | pin $2k+ | 314-253 | 55.4 | -1.8 | -8.8 |  |
| money_level | close | pin limit <$1k | 147-138 | 51.6 | 1.1 | -2.0 |  |
| sharp_gap | close | 1-3k bets | 599-718 | 45.5 | -1.9 | -9.5 |  |
| sharp_gap | close | 3k+ bets | 227-234 | 49.2 | 1.5 | 3.1 |  |
| sharp_gap | close | <1k bets | 139-157 | 47.0 | -0.8 | -11.1 |  |
| sharp_gap | close | pin $1-2k | 320-340 | 48.5 | -0.2 | -3.6 |  |
| sharp_gap | close | pin $2k+ | 252-293 | 46.2 | -0.3 | -4.4 |  |
| sharp_gap | close | pin limit <$1k | 128-145 | 46.9 | -2.3 | -6.8 |  |
| money_moving | close | 1-3k bets | 606-717 | 45.8 | -2.0 | -9.8 |  |
| money_moving | close | 3k+ bets | 226-236 | 48.9 | 1.0 | 1.6 |  |
| money_moving | close | <1k bets | 138-156 | 46.9 | -0.7 | -9.9 |  |
| money_moving | close | pin $1-2k | 316-345 | 47.8 | -1.1 | -4.9 |  |
| money_moving | close | pin $2k+ | 253-291 | 46.5 | -0.0 | -4.4 |  |
| money_moving | close | pin limit <$1k | 126-152 | 45.3 | -4.0 | -9.9 |  |
| pin_value | close | 1-3k bets | 272-266 | 50.6 | 2.3 | 4.4 |  |
| pin_value | close | 3k+ bets | 86-92 | 48.3 | -0.4 | -5.4 |  |
| pin_value | close | <1k bets | 65-51 | 56.0 | 8.5 | 14.5 |  |
| pin_value | close | pin $1-2k | 194-211 | 47.9 | -0.6 | -2.6 |  |
| pin_value | close | pin $2k+ | 116-126 | 47.9 | 1.5 | 3.1 |  |
| pin_value | close | pin limit <$1k | 113-72 | 61.1 | 10.9 | 18.2 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 46.9 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 46.9 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 246-306 | 44.6 | -4.5 | -11.5 |  |
| consensus_gap | close | 3k+ bets | 87-98 | 47.0 | -0.8 | 5.5 |  |
| consensus_gap | close | <1k bets | 55-81 | 40.4 | -5.1 | -19.2 |  |
| consensus_gap | close | pin $1-2k | 122-132 | 48.0 | -1.8 | 0.1 |  |
| consensus_gap | close | pin $2k+ | 108-116 | 48.2 | -2.6 | -3.2 |  |
| consensus_gap | close | pin limit <$1k | 57-45 | 55.9 | 5.3 | 8.8 |  |
| consensus_gap+follow_move | close | 1-3k bets | 99-93 | 51.6 | -0.2 | -3.6 |  |
| consensus_gap+money_level | close | 1-3k bets | 166-113 | 59.5 | 0.7 | 1.1 |  |
| consensus_gap+money_moving | close | 1-3k bets | 107-168 | 38.9 | -7.2 | -13.0 |  |
| consensus_gap+pin_move | close | 1-3k bets | 62-59 | 51.2 | -0.1 | 4.7 |  |
| consensus_gap+pin_value | close | 1-3k bets | 99-112 | 46.9 | 0.3 | -1.6 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 104-170 | 38.0 | -7.4 | -13.8 |  |
| follow_move+money_level | close | 1-3k bets | 408-292 | 58.3 | 2.4 | -4.1 |  |
| follow_move+money_moving | close | 1-3k bets | 339-376 | 47.4 | -1.5 | -9.6 |  |
| follow_move+pin_move | close | 1-3k bets | 258-278 | 48.1 | -1.6 | -8.4 |  |
| follow_move+pin_value | close | 1-3k bets | 89-88 | 50.3 | 1.6 | 0.7 |  |
| follow_move+sharp_gap | close | 1-3k bets | 342-375 | 47.7 | -1.0 | -8.2 |  |
| money_level+money_moving | close | 1-3k bets | 433-385 | 52.9 | 0.6 | -4.1 |  |
| money_level+pin_move | close | 1-3k bets | 216-197 | 52.3 | -0.4 | -4.7 |  |
| money_level+pin_value | close | 1-3k bets | 128-113 | 53.1 | 3.4 | -0.3 |  |
| money_level+sharp_gap | close | 1-3k bets | 419-378 | 52.6 | 0.6 | -3.8 |  |
| money_moving+pin_move | close | 1-3k bets | 216-233 | 48.1 | -0.6 | -3.6 |  |
| money_moving+pin_value | close | 1-3k bets | 115-137 | 45.6 | -2.0 | -6.3 |  |
| money_moving+sharp_gap | close | 1-3k bets | 575-687 | 45.6 | -1.9 | -9.1 |  |
| pin_move+pin_value | close | 1-3k bets | 117-111 | 51.3 | 2.0 | 0.4 |  |
| pin_move+sharp_gap | close | 1-3k bets | 221-234 | 48.6 | 0.0 | -2.3 |  |
| pin_value+sharp_gap | close | 1-3k bets | 116-138 | 45.7 | -1.7 | -6.3 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 146-221 | 39.8 | -2.1 | -9.1 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 74-132 | 35.9 | -5.2 | -16.5 |  |
| consensus_gap+money_delta | close | 1-3k bets | 27-66 | 29.0 | -9.1 | -22.4 |  |
| follow_move+money_delta | close | 1-3k bets | 112-136 | 45.2 | -1.2 | -10.4 |  |
| money_delta+money_level | close | 1-3k bets | 80-77 | 51.0 | 2.9 | 5.0 |  |
| money_delta+money_moving | close | 1-3k bets | 159-226 | 41.3 | -1.7 | -10.0 |  |
| money_delta+pin_value | close | 1-3k bets | 51-48 | 51.5 | 3.9 | 2.6 |  |
| money_delta+sharp_gap | close | 1-3k bets | 158-223 | 41.5 | -1.6 | -9.6 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 80-92 | 46.5 | -0.4 | -1.3 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 18-29 | 38.3 | -0.9 | 13.3 |  |
| money_level+pin_rlm | close | 1-3k bets | 43-32 | 57.3 | 9.3 | 10.5 |  |
| pin_move+pin_rlm | close | 1-3k bets | 89-89 | 50.0 | 5.8 | 10.3 |  |
| pin_rlm+pin_value | close | 1-3k bets | 30-25 | 54.5 | 8.3 | 29.4 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 97-110 | 46.9 | 4.5 | 11.9 |  |
| money_delta+pin_rlm | close | 1-3k bets | 55-63 | 46.6 | 3.8 | 9.8 |  |
| money_moving+pin_rlm | close | 1-3k bets | 92-106 | 46.5 | 4.0 | 12.0 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 21-34 | 38.2 | -2.0 | -0.2 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 143-190 | 42.9 | -1.0 | -8.5 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 78-96 | 44.8 | -0.1 | -9.8 |  |
| money_level+rlm_ratio | close | 1-3k bets | 66-64 | 50.8 | 2.0 | -2.0 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 137-183 | 42.8 | -1.3 | -8.6 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 75-78 | 49.0 | 3.9 | 0.7 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 27-22 | 55.1 | 7.4 | 5.8 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 143-190 | 42.9 | -1.0 | -8.5 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 15-37 | 28.8 | -7.4 | -13.9 |  |
| follow_move+pin_rlm | close | 1-3k bets | 70-85 | 45.2 | 1.5 | -6.8 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 67-129 | 34.2 | -6.9 | -19.6 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 67-92 | 42.1 | -1.9 | -10.6 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 28-52 | 35.0 | -4.6 | -20.7 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 70-85 | 45.2 | 1.5 | -6.8 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 58-113 | 33.9 | -5.8 | -17.9 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 42-74 | 36.2 | -7.0 | -24.4 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 19-25 | 43.2 | -2.5 | 5.8 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 51.1 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 33-27 | 55.0 | 4.6 | 6.6 |  |
| consensus_gap+money_moving | close | 3k+ bets | 36-54 | 40.0 | -5.1 | 13.8 |  |
| consensus_gap+pin_move | close | 3k+ bets | 25-19 | 56.8 | 6.8 | 14.3 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-6 | 33.3 | -7.5 | 6.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 39-33 | 54.2 | 7.3 | 10.5 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -1.9 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 37-54 | 40.7 | -4.3 | 16.7 |  |
| follow_move+money_moving | close | 3k+ bets | 109-112 | 49.3 | 0.1 | -3.5 |  |
| follow_move+pin_move | close | 3k+ bets | 98-99 | 49.7 | -0.3 | -3.3 |  |
| follow_move+pin_rlm | close | 3k+ bets | 32-33 | 49.2 | 5.0 | 8.4 |  |
| follow_move+pin_value | close | 3k+ bets | 35-35 | 50.0 | -0.1 | -6.1 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 51-47 | 52.0 | 7.5 | 11.3 |  |
| follow_move+sharp_gap | close | 3k+ bets | 111-111 | 50.0 | 1.1 | -1.5 |  |
| money_moving+pin_move | close | 3k+ bets | 75-87 | 46.3 | -1.8 | -8.2 |  |
| money_moving+pin_rlm | close | 3k+ bets | 33-47 | 41.2 | -0.8 | -9.6 |  |
| money_moving+pin_value | close | 3k+ bets | 43-52 | 45.3 | -2.5 | -7.6 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 49-45 | 52.1 | 7.7 | 11.8 |  |
| money_moving+sharp_gap | close | 3k+ bets | 219-226 | 49.2 | 1.5 | 2.9 |  |
| pin_move+pin_rlm | close | 3k+ bets | 32-42 | 43.2 | -0.5 | -5.5 |  |
| pin_move+pin_value | close | 3k+ bets | 36-44 | 45.0 | -4.3 | -15.1 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 34-34 | 50.0 | 4.5 | 8.3 |  |
| pin_move+sharp_gap | close | 3k+ bets | 75-87 | 46.3 | -1.5 | -7.6 |  |
| pin_rlm+pin_value | close | 3k+ bets | 6-15 | 28.6 | -17.8 | -45.5 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 32-33 | 49.2 | 5.0 | 8.4 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 34-48 | 41.5 | -0.8 | -9.4 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 9-10 | 47.4 | -2.8 | -10.1 |  |
| pin_value+sharp_gap | close | 3k+ bets | 43-51 | 45.7 | -2.1 | -6.6 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 51-47 | 52.0 | 7.5 | 11.3 |  |
| follow_move+money_delta | close | 3k+ bets | 41-50 | 45.1 | -0.2 | -6.9 |  |
| money_level+money_moving | close | 3k+ bets | 154-131 | 54.0 | 1.8 | 0.0 |  |
| money_level+sharp_gap | close | 3k+ bets | 153-128 | 54.4 | 2.4 | 1.4 |  |
| follow_move+money_level | close | 3k+ bets | 126-94 | 57.3 | 1.0 | -3.0 |  |
| money_level+rlm_ratio | close | 3k+ bets | 25-12 | 67.6 | 20.3 | 38.4 |  |
| consensus_gap+money_level | close | 3k+ bets | 48-45 | 51.6 | -5.1 | -11.3 |  |
| money_level+pin_move | close | 3k+ bets | 69-64 | 51.9 | -1.6 | -4.7 |  |
| money_level+pin_value | close | 3k+ bets | 48-46 | 51.1 | 0.5 | -5.3 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 8-12 | 40.0 | 0.7 | -0.6 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 47-68 | 40.9 | -2.0 | -11.5 |  |
| money_delta+money_moving | close | 3k+ bets | 65-85 | 43.3 | 0.8 | 3.5 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 19-27 | 41.3 | 0.1 | -4.4 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 24-36 | 40.0 | -2.3 | -10.7 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 22-35 | 38.6 | -3.6 | -12.8 |  |
| consensus_gap+money_delta | close | 3k+ bets | 13-23 | 36.1 | -3.5 | 20.4 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 11-27 | 28.9 | -13.9 | -36.8 |  |
| money_delta+sharp_gap | close | 3k+ bets | 63-82 | 43.4 | 1.1 | 4.2 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 29-36 | 44.6 | 0.3 | -3.6 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 11-19 | 36.7 | -5.3 | -12.9 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 8-13 | 38.1 | -11.4 | -27.2 |  |
| money_delta+money_level | close | 3k+ bets | 33-22 | 60.0 | 13.7 | 21.2 |  |
| money_level+pin_rlm | close | 3k+ bets | 16-9 | 64.0 | 18.9 | 37.0 |  |
| money_delta+pin_value | close | 3k+ bets | 19-19 | 50.0 | 3.7 | -5.7 |  |
| money_delta+pin_move | close | 3k+ bets | 37-45 | 45.1 | -0.2 | -8.0 |  |
| money_delta+pin_rlm | close | 3k+ bets | 22-29 | 43.1 | 1.2 | -8.2 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 30-26 | 53.6 | 9.1 | 13.5 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 46.9 | 87.7 |  |
| money_level+money_moving | close | <1k bets | 96-82 | 53.9 | 1.5 | -7.0 |  |
| money_level+sharp_gap | close | <1k bets | 98-82 | 54.4 | 1.8 | -6.6 |  |
| money_moving+sharp_gap | close | <1k bets | 134-153 | 46.7 | -0.9 | -10.7 |  |
| consensus_gap+money_level | close | <1k bets | 29-28 | 50.9 | -6.0 | -22.2 |  |
| consensus_gap+money_moving | close | <1k bets | 25-40 | 38.5 | -5.4 | -17.8 |  |
| consensus_gap+pin_move | close | <1k bets | 8-13 | 38.1 | -12.5 | -17.2 |  |
| consensus_gap+pin_value | close | <1k bets | 18-15 | 54.5 | 11.9 | 31.8 |  |
| consensus_gap+sharp_gap | close | <1k bets | 26-42 | 38.2 | -5.6 | -19.4 |  |
| money_level+pin_move | close | <1k bets | 40-38 | 51.3 | -2.7 | -9.3 |  |
| money_level+pin_value | close | <1k bets | 23-18 | 56.1 | 5.9 | 4.7 |  |
| money_moving+pin_move | close | <1k bets | 39-44 | 47.0 | -0.6 | -4.3 |  |
| money_moving+pin_value | close | <1k bets | 21-17 | 55.3 | 10.2 | 29.4 |  |
| pin_move+pin_value | close | <1k bets | 29-21 | 58.0 | 9.5 | 16.9 |  |
| pin_move+sharp_gap | close | <1k bets | 39-45 | 46.4 | -1.7 | -9.2 |  |
| pin_value+sharp_gap | close | <1k bets | 21-16 | 56.8 | 11.2 | 32.9 |  |
| follow_move+money_delta | close | <1k bets | 23-27 | 46.0 | 2.8 | -7.4 |  |
| follow_move+money_moving | close | <1k bets | 64-73 | 46.7 | -2.7 | -14.4 |  |
| follow_move+pin_move | close | <1k bets | 48-52 | 48.0 | -3.0 | -10.9 |  |
| follow_move+sharp_gap | close | <1k bets | 65-73 | 47.1 | -2.8 | -16.4 |  |
| money_delta+money_moving | close | <1k bets | 34-54 | 38.6 | -1.8 | -15.9 |  |
| money_delta+pin_move | close | <1k bets | 14-19 | 42.4 | -1.8 | -17.4 |  |
| money_delta+sharp_gap | close | <1k bets | 34-54 | 38.6 | -1.8 | -15.9 |  |
| follow_move+rlm_quiet | close | <1k bets | 26-45 | 36.6 | -4.7 | -23.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 29-33 | 46.8 | 4.0 | -6.3 |  |
| money_delta+rlm_quiet | close | <1k bets | 11-14 | 44.0 | 3.9 | -7.9 |  |
| money_delta+rlm_ratio | close | <1k bets | 19-20 | 48.7 | 6.8 | -0.8 |  |
| money_moving+rlm_quiet | close | <1k bets | 16-18 | 47.1 | 6.1 | 3.1 |  |
| money_moving+rlm_ratio | close | <1k bets | 29-33 | 46.8 | 4.0 | -6.3 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 12-15 | 44.4 | 4.7 | -7.6 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 15-19 | 44.1 | 2.5 | -9.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 29-33 | 46.8 | 4.0 | -6.3 |  |
| follow_move+money_level | close | <1k bets | 87-63 | 58.0 | 0.1 | -11.2 |  |
| consensus_gap+money_delta | close | <1k bets | 7-22 | 24.1 | -10.5 | -35.0 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -2.5 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 13-16 | 44.8 | 5.3 | -3.9 |  |
| money_moving+pin_rlm | close | <1k bets | 22-24 | 47.8 | 6.6 | 5.5 |  |
| pin_rlm+sharp_gap | close | <1k bets | 22-24 | 47.8 | 6.6 | 5.5 |  |
| money_delta+pin_value | close | <1k bets | 9-8 | 52.9 | 7.4 | 21.5 |  |
| consensus_gap+follow_move | close | <1k bets | 14-20 | 41.2 | -10.5 | -33.3 |  |
| follow_move+pin_rlm | close | <1k bets | 17-14 | 54.8 | 11.3 | 8.4 |  |
| follow_move+pin_value | close | <1k bets | 21-14 | 60.0 | 11.2 | 14.0 |  |
| pin_move+pin_rlm | close | <1k bets | 20-19 | 51.3 | 7.7 | 8.1 |  |
| pin_move+rlm_quiet | close | <1k bets | 12-14 | 46.2 | 0.8 | -1.0 |  |
| pin_move+rlm_ratio | close | <1k bets | 17-16 | 51.5 | 6.4 | 0.5 |  |
| pin_rlm+pin_value | close | <1k bets | 6-3 | 66.7 | 24.9 | 64.1 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 8-6 | 57.1 | 14.0 | 12.9 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 17-14 | 54.8 | 11.3 | 8.4 |  |
| pin_value+rlm_quiet | close | <1k bets | 5-4 | 55.6 | 6.6 | 6.5 |  |
| pin_value+rlm_ratio | close | <1k bets | 5-1 | 83.3 | 35.1 | 58.3 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -6.5 | -42.5 |  |
| money_delta+money_level | close | <1k bets | 14-18 | 43.8 | 0.8 | -12.1 |  |
| money_level+rlm_ratio | close | <1k bets | 14-14 | 50.0 | 4.9 | -2.1 |  |
| money_level+pin_rlm | close | <1k bets | 9-7 | 56.2 | 13.7 | 11.6 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-5 | 16.7 | -21.5 | -68.2 |  |
| consensus_gap+follow_move | close | pin $1-2k | 47-52 | 47.5 | -4.8 | -9.9 |  |
| consensus_gap+money_moving | close | pin $1-2k | 58-70 | 45.3 | -3.4 | -2.6 |  |
| consensus_gap+pin_move | close | pin $1-2k | 46-47 | 49.5 | -2.4 | 5.8 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-18 | 41.9 | 0.5 | 25.8 |  |
| consensus_gap+pin_value | close | pin $1-2k | 70-76 | 47.9 | 1.4 | -1.8 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-15 | 48.3 | 2.9 | 5.2 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 56-67 | 45.5 | -2.3 | -0.6 |  |
| follow_move+money_moving | close | pin $1-2k | 175-206 | 45.9 | -3.5 | -10.4 |  |
| follow_move+pin_move | close | pin $1-2k | 185-207 | 47.2 | -3.0 | -9.1 |  |
| follow_move+pin_rlm | close | pin $1-2k | 55-56 | 49.5 | 4.1 | 3.7 |  |
| follow_move+pin_value | close | pin $1-2k | 65-77 | 45.8 | -3.6 | -13.6 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 81-81 | 50.0 | 4.5 | 3.9 |  |
| follow_move+sharp_gap | close | pin $1-2k | 180-204 | 46.9 | -2.5 | -9.1 |  |
| money_moving+pin_move | close | pin $1-2k | 161-175 | 47.9 | -1.2 | -3.2 |  |
| money_moving+pin_rlm | close | pin $1-2k | 65-69 | 48.5 | 4.4 | 10.6 |  |
| money_moving+pin_value | close | pin $1-2k | 76-106 | 41.8 | -6.1 | -16.6 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 79-77 | 50.6 | 4.8 | 5.1 |  |
| money_moving+sharp_gap | close | pin $1-2k | 306-330 | 48.1 | -0.6 | -4.0 |  |
| pin_move+pin_rlm | close | pin $1-2k | 65-64 | 50.4 | 5.3 | 12.0 |  |
| pin_move+pin_value | close | pin $1-2k | 82-95 | 46.3 | -3.3 | -10.8 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 63-58 | 52.1 | 5.4 | 7.3 |  |
| pin_move+sharp_gap | close | pin $1-2k | 164-175 | 48.4 | -0.5 | -2.7 |  |
| pin_rlm+pin_value | close | pin $1-2k | 17-25 | 40.5 | -7.6 | -16.3 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 55-56 | 49.5 | 4.1 | 3.7 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 68-72 | 48.6 | 4.8 | 10.3 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 19-21 | 47.5 | -1.8 | -10.3 |  |
| pin_value+sharp_gap | close | pin $1-2k | 76-102 | 42.7 | -5.1 | -14.8 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 81-81 | 50.0 | 4.5 | 3.9 |  |
| follow_move+money_level | close | pin $1-2k | 201-185 | 52.1 | -2.0 | -8.4 |  |
| money_level+rlm_ratio | close | pin $1-2k | 46-34 | 57.5 | 9.7 | 12.1 |  |
| money_level+sharp_gap | close | pin $1-2k | 231-212 | 52.1 | 0.5 | -3.4 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 4-14 | 22.2 | -18.3 | -36.2 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 60-108 | 35.7 | -7.5 | -20.4 |  |
| money_level+money_moving | close | pin $1-2k | 230-216 | 51.6 | -0.2 | -4.7 |  |
| consensus_gap+money_level | close | pin $1-2k | 71-63 | 53.0 | -4.0 | -7.1 |  |
| money_level+pin_value | close | pin $1-2k | 84-85 | 49.7 | -0.3 | -7.0 |  |
| money_level+pin_move | close | pin $1-2k | 156-145 | 51.8 | -0.7 | -5.3 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 29-47 | 38.2 | -5.3 | -9.5 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 43-63 | 40.6 | -4.8 | -9.9 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 18-32 | 36.0 | -7.8 | -15.1 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 24-39 | 38.1 | -4.4 | -9.2 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 30-49 | 38.0 | -5.2 | -12.4 |  |
| money_level+pin_rlm | close | pin $1-2k | 32-23 | 58.2 | 12.0 | 14.4 |  |
| follow_move+money_delta | close | pin $1-2k | 66-69 | 48.9 | 2.5 | -0.2 |  |
| money_delta+money_moving | close | pin $1-2k | 87-97 | 47.3 | 3.0 | 3.4 |  |
| money_delta+pin_move | close | pin $1-2k | 66-70 | 48.5 | 1.3 | 2.1 |  |
| money_delta+pin_rlm | close | pin $1-2k | 42-45 | 48.3 | 4.8 | 9.8 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 49-45 | 52.1 | 6.6 | 8.7 |  |
| money_delta+sharp_gap | close | pin $1-2k | 87-95 | 47.8 | 3.5 | 4.6 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 46.9 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 46-37 | 55.4 | 7.7 | 7.9 |  |
| consensus_gap+money_delta | close | pin $1-2k | 18-26 | 40.9 | -0.8 | 2.5 |  |
| money_delta+pin_value | close | pin $1-2k | 43-45 | 48.9 | 0.8 | -3.4 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 19-37 | 33.9 | -10.2 | -22.8 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 12-27 | 30.8 | -18.1 | -40.9 |  |
| consensus_gap+follow_move | close | pin $2k+ | 34-29 | 54.0 | 0.6 | -9.7 |  |
| consensus_gap+money_delta | close | pin $2k+ | 8-26 | 23.5 | -10.7 | -53.8 |  |
| consensus_gap+money_level | close | pin $2k+ | 72-56 | 56.2 | -5.9 | -12.4 |  |
| consensus_gap+money_moving | close | pin $2k+ | 38-69 | 35.5 | -10.0 | -10.4 |  |
| consensus_gap+pin_move | close | pin $2k+ | 32-33 | 49.2 | -1.3 | -8.6 |  |
| consensus_gap+pin_value | close | pin $2k+ | 44-51 | 46.3 | 3.5 | 9.2 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-13 | 0.0 | -32.0 | -100.0 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 40-72 | 35.7 | -10.2 | -9.8 |  |
| follow_move+money_delta | close | pin $2k+ | 34-45 | 43.0 | 1.1 | -11.0 |  |
| follow_move+money_level | close | pin $2k+ | 149-100 | 59.8 | 0.5 | -4.3 |  |
| follow_move+money_moving | close | pin $2k+ | 118-121 | 49.4 | 1.3 | -5.8 |  |
| follow_move+pin_move | close | pin $2k+ | 151-149 | 50.3 | 0.3 | -5.3 |  |
| follow_move+pin_value | close | pin $2k+ | 37-34 | 52.1 | 4.6 | 12.3 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 40-62 | 39.2 | 1.1 | -13.2 |  |
| follow_move+sharp_gap | close | pin $2k+ | 119-122 | 49.4 | 1.4 | -5.5 |  |
| money_delta+money_level | close | pin $2k+ | 25-22 | 53.2 | 8.5 | 7.6 |  |
| money_delta+money_moving | close | pin $2k+ | 62-91 | 40.5 | 1.7 | -10.2 |  |
| money_delta+pin_move | close | pin $2k+ | 34-50 | 40.5 | -2.2 | -16.9 |  |
| money_delta+pin_value | close | pin $2k+ | 19-22 | 46.3 | 2.7 | -11.4 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 20-31 | 39.2 | 0.8 | -15.0 |  |
| money_delta+sharp_gap | close | pin $2k+ | 60-90 | 40.0 | 1.1 | -11.2 |  |
| money_level+money_moving | close | pin $2k+ | 167-157 | 51.5 | -1.2 | -6.6 |  |
| money_level+pin_move | close | pin $2k+ | 109-98 | 52.7 | -2.9 | -7.5 |  |
| money_level+pin_value | close | pin $2k+ | 58-56 | 50.9 | 1.3 | -5.8 |  |
| money_level+rlm_ratio | close | pin $2k+ | 14-14 | 50.0 | 3.9 | 5.0 |  |
| money_level+sharp_gap | close | pin $2k+ | 167-158 | 51.4 | -1.3 | -6.5 |  |
| money_moving+pin_move | close | pin $2k+ | 103-117 | 46.8 | -0.2 | -6.7 |  |
| money_moving+pin_value | close | pin $2k+ | 60-70 | 46.2 | 0.7 | 4.1 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 40-61 | 39.6 | 1.4 | -12.4 |  |
| money_moving+sharp_gap | close | pin $2k+ | 247-287 | 46.3 | -0.2 | -4.3 |  |
| pin_move+pin_value | close | pin $2k+ | 52-51 | 50.5 | 2.5 | -1.2 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 28-41 | 40.6 | 0.9 | -7.7 |  |
| pin_move+sharp_gap | close | pin $2k+ | 103-118 | 46.6 | -0.5 | -6.8 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 4-7 | 36.4 | -6.1 | -26.4 |  |
| pin_value+sharp_gap | close | pin $2k+ | 60-71 | 45.8 | 0.5 | 3.3 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 40-62 | 39.2 | 1.1 | -13.2 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-21 | 16.0 | -15.7 | -30.8 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 5-13 | 27.8 | -2.8 | -42.0 |  |
| follow_move+pin_rlm | close | pin $2k+ | 29-47 | 38.2 | 0.7 | -13.1 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 65-79 | 45.1 | 6.5 | 3.6 |  |
| money_moving+pin_rlm | close | pin $2k+ | 41-73 | 36.0 | 0.0 | -6.4 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 29-43 | 40.3 | 4.5 | -10.0 |  |
| pin_move+pin_rlm | close | pin $2k+ | 33-49 | 40.2 | 2.3 | -6.1 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 42-54 | 43.8 | 3.0 | -5.3 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 14-32 | 30.4 | -2.3 | -25.9 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 29-47 | 38.2 | 0.7 | -13.1 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 41-73 | 36.0 | 0.0 | -6.4 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 21-39 | 35.0 | 2.0 | -18.3 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 29-44 | 39.7 | 4.0 | -11.3 |  |
| money_delta+pin_rlm | close | pin $2k+ | 22-41 | 34.9 | -0.8 | -13.7 |  |
| money_level+pin_rlm | close | pin $2k+ | 15-10 | 60.0 | 16.0 | 27.1 |  |
| pin_rlm+pin_value | close | pin $2k+ | 6-13 | 31.6 | -5.3 | 13.6 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 19-25 | 43.2 | 4.5 | -10.9 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 6-8 | 42.9 | 3.9 | 54.3 |  |
| follow_move+money_delta | close | pin limit <$1k | 35-45 | 43.8 | -5.1 | -16.0 |  |
| money_level+money_moving | close | pin limit <$1k | 78-89 | 46.7 | -3.0 | -10.5 |  |
| money_level+sharp_gap | close | pin limit <$1k | 75-83 | 47.5 | -2.2 | -9.0 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 117-136 | 46.2 | -2.9 | -7.8 |  |
| consensus_gap+money_level | close | pin limit <$1k | 32-26 | 55.2 | 4.0 | 2.2 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 17-11 | 60.7 | 12.0 | 30.2 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 42-33 | 56.0 | 6.0 | 11.3 |  |
| follow_move+money_moving | close | pin limit <$1k | 72-90 | 44.4 | -4.7 | -14.6 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 77-89 | 46.4 | -2.7 | -10.9 |  |
| money_level+pin_move | close | pin limit <$1k | 60-56 | 51.7 | 1.8 | -1.3 |  |
| money_level+pin_value | close | pin limit <$1k | 57-36 | 61.3 | 10.8 | 15.9 |  |
| pin_move+pin_value | close | pin limit <$1k | 48-30 | 61.5 | 11.5 | 22.6 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 22-11 | 66.7 | 17.0 | 23.4 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 25-19 | 56.8 | 7.7 | 17.6 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 27-19 | 58.7 | 9.5 | 20.6 |  |
| follow_move+money_level | close | pin limit <$1k | 62-66 | 48.4 | -1.7 | -7.8 |  |
| follow_move+pin_move | close | pin limit <$1k | 68-73 | 48.2 | -1.1 | -7.6 |  |
| follow_move+pin_value | close | pin limit <$1k | 43-26 | 62.3 | 12.4 | 18.2 |  |
| money_moving+pin_move | close | pin limit <$1k | 66-72 | 47.8 | -1.3 | -5.3 |  |
| money_moving+pin_value | close | pin limit <$1k | 43-30 | 58.9 | 9.1 | 17.8 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 68-73 | 48.2 | -0.8 | -4.6 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 44-32 | 57.9 | 8.1 | 15.7 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 41-44 | 48.2 | -0.7 | -7.5 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 27-31 | 46.6 | -2.0 | -10.7 |  |
| money_delta+money_moving | close | pin limit <$1k | 50-54 | 48.1 | -0.7 | -3.6 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 9-6 | 60.0 | 13.1 | 43.2 |  |
| money_delta+money_level | close | pin limit <$1k | 26-23 | 53.1 | 3.8 | 1.7 |  |
| money_delta+pin_value | close | pin limit <$1k | 17-8 | 68.0 | 19.0 | 46.9 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 49-52 | 48.5 | -0.2 | -2.7 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 31-36 | 46.3 | -2.1 | -4.6 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 7-3 | 70.0 | 24.1 | 77.3 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 26-22 | 54.2 | 6.3 | 13.3 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 41-35 | 53.9 | 5.8 | 15.2 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 43-37 | 53.8 | 5.3 | 8.6 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-5 | 79.2 | 30.4 | 69.5 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 44-37 | 54.3 | 6.1 | 15.2 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 7-1 | 87.5 | 40.7 | 67.3 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 14-7 | 66.7 | 17.2 | 27.5 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 11-19 | 36.7 | -11.2 | -29.6 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 23-25 | 47.9 | -0.7 | -7.9 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 35-29 | 54.7 | 6.1 | 5.3 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 49-44 | 52.7 | 4.1 | 1.7 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 29-28 | 50.9 | 2.4 | -2.1 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 21-30 | 41.2 | -7.2 | -20.8 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 45-42 | 51.7 | 3.2 | -0.0 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 35-29 | 54.7 | 6.1 | 5.3 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 15-13 | 53.6 | 5.8 | 3.1 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 35-29 | 54.7 | 6.1 | 5.3 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 23-23 | 50.0 | 1.7 | -4.0 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 49-44 | 52.7 | 4.1 | 1.7 |  |
| money_level+pin_rlm | close | pin limit <$1k | 21-15 | 58.3 | 9.2 | 12.0 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 23-18 | 56.1 | 7.5 | 9.1 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 18-5 | 78.3 | 28.7 | 49.8 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 7-3 | 70.0 | 22.1 | 33.8 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 51.1 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.6 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -52.1 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 35-40 | 46.7 | 10.5 | 12.9 | 0.26 |
| rlm_quiet | early | pin $1-2k | 2-5 | 28.6 | -3.1 | 16.0 | -1.07 |
| rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.1 | -100.0 | 1.3 |
| rlm_quiet | early | pin limit <$1k | 5-8 | 38.5 | -6.2 | -21.5 | 0.25 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -51.1 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 8-12 | 40.0 | -8.4 | -26.9 | 0.2 |
| pin_move | early | pin $1-2k | 0-5 | 0.0 | -40.6 | -100.0 | 0.14 |
| pin_move | early | pin limit <$1k | 8-8 | 50.0 | -1.1 | -8.6 | 0.15 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.3 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 9-7 | 56.2 | 15.0 | 22.8 | -0.11 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -40.6 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 5-0 | 100.0 | 51.1 | 88.6 | 0.0 |
| pin_rlm | early | <1k bets | 1-3 | 25.0 | -14.1 | -51.8 | -0.37 |
| pin_rlm | early | pin $1-2k | 0-3 | 0.0 | -42.7 | -100.0 | -0.67 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 71.9 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.6 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -52.1 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 463-406 | 53.3 | 1.7 | -6.3 | 0.16 |
| follow_move | early | pin $1-2k | 35-23 | 60.3 | 8.9 | 11.2 | -0.42 |
| follow_move | early | pin $2k+ | 0-2 | 0.0 | -40.6 | -100.0 | 0.65 |
| follow_move | early | pin limit <$1k | 52-45 | 53.6 | 3.4 | -0.7 | -0.15 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.1 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 28-20 | 58.3 | 19.3 | 27.7 | 0.65 |
| rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.4 | 29.7 | -1.02 |
| rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.6 | -100.0 | 0.65 |
| rlm_ratio | early | pin limit <$1k | 8-1 | 88.9 | 44.1 | 79.0 | 0.37 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 1.6 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 44.1 | 59.7 | 0.33 |
| money_level | early | <1k bets | 161-109 | 59.6 | 0.1 | -6.3 | -0.13 |
| money_level | early | pin $1-2k | 21-10 | 67.7 | 3.2 | 0.1 | 0.12 |
| money_level | early | pin $2k+ | 1-1 | 50.0 | -12.5 | -47.2 | -0.7 |
| money_level | early | pin limit <$1k | 26-27 | 49.1 | -3.8 | -9.2 | 0.25 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.3 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.7 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 131-117 | 52.8 | 4.5 | 2.2 | 0.35 |
| sharp_gap | early | pin $1-2k | 16-13 | 55.2 | 1.0 | 2.2 | -0.24 |
| sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.6 | -100.0 | 0.65 |
| sharp_gap | early | pin limit <$1k | 31-19 | 62.0 | 13.4 | 27.8 | 0.11 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.7 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 52.1 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 96-85 | 53.0 | 1.6 | -6.3 | 0.12 |
| money_moving | early | pin $1-2k | 8-10 | 44.4 | -13.7 | -39.0 | 0.28 |
| money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.5 | -8.4 | 0.65 |
| money_moving | early | pin limit <$1k | 25-10 | 71.4 | 22.4 | 49.9 | 0.39 |
| pin_value | early | 1-3k bets | 13-10 | 56.5 | 8.5 | 6.3 | -0.04 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 44-47 | 48.4 | -0.5 | -8.5 | 0.09 |
| pin_value | early | pin $1-2k | 15-25 | 37.5 | -9.3 | -29.5 | 0.13 |
| pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.1 | 83.3 | 0.0 |
| pin_value | early | pin limit <$1k | 42-32 | 56.8 | 7.1 | 7.4 | 0.04 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -51.1 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -27.0 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.1 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.5 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 220-267 | 45.2 | -3.0 | -11.0 | 0.39 |
| consensus_gap | early | pin $1-2k | 15-22 | 40.5 | -4.5 | -22.0 | 0.48 |
| consensus_gap | early | pin $2k+ | 1-1 | 50.0 | 12.5 | -8.4 | 0.65 |
| consensus_gap | early | pin limit <$1k | 22-34 | 39.3 | -11.0 | -19.8 | 0.28 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -53.1 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.3 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.3 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -2.1 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.8 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 5.8 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.5 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 7-4 | 63.6 | 14.5 | 19.4 | -0.09 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.3 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 17.0 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -51.1 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -0.7 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 6-5 | 54.5 | 8.4 | 1.3 | 0.27 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -1.1 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-7 | 50.0 | 3.1 | -6.4 | -0.29 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.6 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.7 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -20.0 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.8 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 3.5 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.7 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.1 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.6 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.1 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.4 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.0 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.5 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.0 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 53.1 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 11.4 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 18.1 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 16.1 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 16.1 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -28.1 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| follow_move+rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -52.1 | -100.0 | -0.5 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 52.1 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| rlm_quiet+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| rlm_quiet+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 39.6 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 51.1 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 31-38 | 44.9 | -6.9 | -18.5 | 0.86 |
| consensus_gap+money_level | early | <1k bets | 35-26 | 57.4 | -6.1 | -10.6 | 0.21 |
| consensus_gap+sharp_gap | early | <1k bets | 26-41 | 38.8 | -8.0 | -16.4 | 0.9 |
| follow_move+money_level | early | <1k bets | 81-41 | 66.4 | 5.6 | -2.1 | 0.04 |
| follow_move+sharp_gap | early | <1k bets | 69-37 | 65.1 | 15.3 | 16.5 | 0.52 |
| money_level+sharp_gap | early | <1k bets | 86-57 | 60.1 | 3.9 | -1.4 | 0.17 |
| follow_move+money_moving | early | <1k bets | 50-32 | 61.0 | 8.0 | 6.4 | 0.43 |
| money_level+money_moving | early | <1k bets | 58-43 | 57.4 | -1.3 | -9.1 | -0.15 |
| money_moving+sharp_gap | early | <1k bets | 57-50 | 53.3 | 3.9 | -2.0 | 0.28 |
| consensus_gap+money_moving | early | <1k bets | 14-21 | 40.0 | -9.3 | -36.3 | 0.27 |
| follow_move+pin_value | early | <1k bets | 16-14 | 53.3 | 3.7 | 0.1 | -0.18 |
| follow_move+rlm_quiet | early | <1k bets | 35-40 | 46.7 | 10.5 | 12.9 | 0.26 |
| money_moving+rlm_quiet | early | <1k bets | 14-12 | 53.8 | 16.2 | 28.2 | 0.62 |
| rlm_quiet+sharp_gap | early | <1k bets | 20-15 | 57.1 | 20.2 | 27.6 | -0.0 |
| follow_move+rlm_ratio | early | <1k bets | 28-20 | 58.3 | 19.3 | 27.7 | 0.65 |
| rlm_quiet+rlm_ratio | early | <1k bets | 18-11 | 62.1 | 25.4 | 40.9 | 0.03 |
| rlm_ratio+sharp_gap | early | <1k bets | 28-20 | 58.3 | 19.3 | 27.7 | 0.65 |
| pin_move+pin_value | early | <1k bets | 2-7 | 22.2 | -26.8 | -57.6 | 0.11 |
| follow_move+pin_move | early | <1k bets | 6-6 | 50.0 | -0.5 | -9.9 | 0.45 |
| consensus_gap+pin_value | early | <1k bets | 17-23 | 42.5 | -4.8 | -20.2 | 0.41 |
| pin_value+rlm_quiet | early | <1k bets | 0-3 | 0.0 | -43.4 | -100.0 | -0.6 |
| money_delta+money_moving | early | <1k bets | 8-7 | 53.3 | 12.6 | 18.2 | -0.11 |
| money_delta+sharp_gap | early | <1k bets | 7-5 | 58.3 | 17.9 | 31.9 | -0.14 |
| consensus_gap+pin_move | early | <1k bets | 1-5 | 16.7 | -28.9 | -68.2 | 0.22 |
| money_level+pin_move | early | <1k bets | 3-2 | 60.0 | 5.2 | 0.8 | 0.08 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -28.1 | -100.0 | -4.8 |
| consensus_gap+rlm_quiet | early | <1k bets | 3-5 | 37.5 | -1.0 | -22.7 | 1.01 |
| consensus_gap+rlm_ratio | early | <1k bets | 5-3 | 62.5 | 21.4 | 25.0 | 0.65 |
| follow_move+pin_rlm | early | <1k bets | 1-2 | 33.3 | -9.4 | -35.8 | -0.93 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -28.1 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | <1k bets | 0-1 | 0.0 | -28.1 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-2 | 33.3 | -9.4 | -35.8 | -0.93 |
| pin_rlm+sharp_gap | early | <1k bets | 1-3 | 25.0 | -14.1 | -51.8 | -0.37 |
| pin_value+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 24.7 | 27.3 | -0.93 |
| pin_value+sharp_gap | early | <1k bets | 6-5 | 54.5 | 4.8 | 4.1 | 0.17 |
| money_level+pin_value | early | <1k bets | 6-5 | 54.5 | 2.4 | 4.1 | 0.88 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -51.0 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -48.9 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 2-3 | 40.0 | -14.8 | -23.6 | 1.34 |
| money_level+rlm_ratio | early | <1k bets | 8-9 | 47.1 | 5.0 | -2.4 | 1.85 |
| money_moving+rlm_ratio | early | <1k bets | 14-8 | 63.6 | 21.2 | 41.4 | 0.8 |
| consensus_gap+money_delta | early | <1k bets | 2-0 | 100.0 | 50.0 | 90.9 | 0.5 |
| money_delta+money_level | early | <1k bets | 4-2 | 66.7 | 20.9 | 39.4 | 1.3 |
| pin_move+sharp_gap | early | <1k bets | 2-1 | 66.7 | 16.3 | 4.3 | -0.07 |
| money_level+pin_rlm | early | <1k bets | 1-1 | 50.0 | 0.0 | -3.7 | 1.0 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 71.9 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 71.9 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 4-4 | 50.0 | 8.9 | 27.0 | 0.42 |
| money_delta+rlm_quiet | early | <1k bets | 1-2 | 33.3 | -1.7 | 23.3 | -2.8 |
| money_delta+rlm_ratio | early | <1k bets | 3-2 | 60.0 | 19.4 | 65.0 | 1.12 |
| money_delta+pin_value | early | <1k bets | 2-0 | 100.0 | 51.1 | 90.9 | 0.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -28.1 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 5-4 | 55.6 | -8.0 | -12.6 | 0.71 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -30.2 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 6-10 | 37.5 | -4.7 | -30.9 | 0.29 |
| follow_move+rlm_quiet | early | pin $1-2k | 2-5 | 28.6 | -3.1 | 16.0 | -1.07 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.4 | 29.7 | -1.02 |
| follow_move+sharp_gap | early | pin $1-2k | 9-5 | 64.3 | 8.0 | 27.7 | -0.66 |
| money_level+money_moving | early | pin $1-2k | 8-6 | 57.1 | -8.0 | -21.6 | 0.19 |
| money_level+pin_value | early | pin $1-2k | 2-4 | 33.3 | -18.8 | -37.6 | 0.78 |
| money_moving+pin_value | early | pin $1-2k | 1-3 | 25.0 | -30.2 | -54.2 | 0.93 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -9.4 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -9.4 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -10.4 | 29.7 | -1.02 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -53.1 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -40.6 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -53.1 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -40.6 | -100.0 | 2.5 |
| money_level+sharp_gap | early | pin $1-2k | 13-6 | 68.4 | 4.6 | 4.7 | -0.05 |
| money_moving+sharp_gap | early | pin $1-2k | 4-7 | 36.4 | -21.3 | -50.4 | 0.23 |
| pin_value+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -25.0 | -52.3 | -0.52 |
| consensus_gap+follow_move | early | pin $1-2k | 5-6 | 45.5 | -2.6 | -18.8 | 0.45 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 0-3 | 0.0 | -28.1 | -100.0 | -0.97 |
| follow_move+pin_value | early | pin $1-2k | 6-7 | 46.2 | -1.4 | -14.7 | -0.25 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -28.1 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 11-5 | 68.8 | 4.3 | -0.1 | 0.03 |
| money_level+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -12.5 | -1.0 | 0.75 |
| follow_move+money_moving | early | pin $1-2k | 4-2 | 66.7 | 2.8 | -10.9 | -0.15 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -28.1 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -28.1 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -16.7 | -46.8 | -0.12 |
| follow_move+pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -28.1 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | pin $1-2k | 0-1 | 0.0 | -28.1 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-3 | 0.0 | -42.7 | -100.0 | -0.67 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -28.1 | -100.0 | -4.8 |
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -28.1 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -28.1 | -100.0 | 1.3 |
| pin_move+pin_value | early | pin $1-2k | 0-2 | 0.0 | -46.9 | -100.0 | 0.0 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -71.9 | -100.0 | 1.5 |
| follow_move+pin_move | early | pin $1-2k | 0-1 | 0.0 | -46.9 | -100.0 | 0.0 |
| consensus_gap+money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.5 | -8.4 | 0.65 |
| consensus_gap+pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.1 | 83.3 | 0.0 |
| follow_move+money_level | early | pin $2k+ | 0-1 | 0.0 | -53.1 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.6 | -100.0 | 0.65 |
| follow_move+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.6 | -100.0 | 0.65 |
| money_level+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -53.1 | -100.0 | 0.0 |
| money_level+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -53.1 | -100.0 | 0.0 |
| money_moving+pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.1 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.6 | -100.0 | 0.65 |
| consensus_gap+follow_move | early | pin $2k+ | 0-1 | 0.0 | -28.1 | -100.0 | 1.3 |
| consensus_gap+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.1 | -100.0 | 1.3 |
| consensus_gap+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.1 | -100.0 | 1.3 |
| consensus_gap+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.1 | -100.0 | 1.3 |
| follow_move+money_moving | early | pin $2k+ | 0-1 | 0.0 | -28.1 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.1 | -100.0 | 1.3 |
| money_moving+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.1 | -100.0 | 1.3 |
| money_moving+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.1 | -100.0 | 1.3 |
| money_moving+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.1 | -100.0 | 1.3 |
| rlm_quiet+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.1 | -100.0 | 1.3 |
| rlm_quiet+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.1 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin limit <$1k | 5-8 | 38.5 | -6.2 | -21.5 | 0.25 |
| money_level+money_moving | early | pin limit <$1k | 14-7 | 66.7 | 14.9 | 23.6 | 0.5 |
| money_level+sharp_gap | early | pin limit <$1k | 21-16 | 56.8 | 6.4 | 4.1 | 0.16 |
| money_moving+sharp_gap | early | pin limit <$1k | 20-6 | 76.9 | 28.9 | 65.2 | 0.31 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -51.1 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 11-6 | 64.7 | 15.0 | 22.8 | 0.35 |
| money_moving+pin_value | early | pin limit <$1k | 8-4 | 66.7 | 17.2 | 26.0 | 0.25 |
| pin_value+sharp_gap | early | pin limit <$1k | 13-6 | 68.4 | 18.8 | 29.8 | 0.05 |
| consensus_gap+follow_move | early | pin limit <$1k | 7-9 | 43.8 | -7.8 | -18.4 | 0.56 |
| consensus_gap+money_level | early | pin limit <$1k | 5-7 | 41.7 | -13.2 | -28.1 | 0.42 |
| consensus_gap+pin_value | early | pin limit <$1k | 17-18 | 48.6 | -0.6 | -8.6 | 0.45 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 7-4 | 63.6 | 18.3 | 56.6 | 0.91 |
| follow_move+money_level | early | pin limit <$1k | 12-11 | 52.2 | -0.9 | -3.2 | 0.01 |
| follow_move+pin_value | early | pin limit <$1k | 17-14 | 54.8 | 5.6 | 3.4 | -0.19 |
| follow_move+sharp_gap | early | pin limit <$1k | 14-8 | 63.6 | 15.3 | 21.5 | -0.02 |
| follow_move+rlm_ratio | early | pin limit <$1k | 8-1 | 88.9 | 44.1 | 79.0 | 0.37 |
| money_level+rlm_ratio | early | pin limit <$1k | 7-0 | 100.0 | 53.8 | 92.4 | 0.5 |
| pin_value+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.6 | 43.2 | -0.25 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 8-1 | 88.9 | 44.1 | 79.0 | 0.37 |
| consensus_gap+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 51.0 | 87.1 | 0.33 |
| consensus_gap+money_moving | early | pin limit <$1k | 8-3 | 72.7 | 25.3 | 74.0 | 0.58 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 2.1 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 51.0 | 87.1 | 0.33 |
| follow_move+money_moving | early | pin limit <$1k | 10-4 | 71.4 | 22.3 | 36.5 | 0.36 |
| money_delta+money_moving | early | pin limit <$1k | 4-0 | 100.0 | 51.1 | 88.0 | 0.0 |
| money_delta+pin_value | early | pin limit <$1k | 4-0 | 100.0 | 51.1 | 88.0 | 0.0 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 53.1 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 3-2 | 60.0 | 11.1 | 13.0 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 30.2 | 54.4 | -0.2 |
| money_delta+sharp_gap | early | pin limit <$1k | 3-0 | 100.0 | 50.4 | 89.6 | 0.0 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 10.4 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | 5.7 | 13.7 | -0.05 |
| pin_move+pin_value | early | pin limit <$1k | 2-5 | 28.6 | -21.0 | -45.5 | 0.14 |
| follow_move+pin_move | early | pin limit <$1k | 6-5 | 54.5 | 3.7 | -1.7 | 0.49 |
| consensus_gap+pin_move | early | pin limit <$1k | 1-3 | 25.0 | -29.2 | -52.3 | 0.4 |
| money_level+pin_move | early | pin limit <$1k | 3-2 | 60.0 | 5.2 | 0.8 | 0.08 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -48.9 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -48.9 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 16.3 | 4.3 | -0.07 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 71.9 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 71.9 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 71.9 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 71.9 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 71.9 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 71.9 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 2-0 | 100.0 | 51.1 | 90.9 | 0.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 51.1 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 51.1 | 90.9 | 1.0 |
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
| rlm_quiet | close | 1-3k bets | 30-53 | 36.1 | -5.4 | -13.1 |  |
| rlm_quiet | close | 3k+ bets | 3-8 | 27.3 | -15.5 | -42.9 |  |
| rlm_quiet | close | <1k bets | 4-17 | 19.0 | -22.3 | -63.3 |  |
| rlm_quiet | close | pin $1-2k | 14-27 | 34.1 | -7.8 | -29.9 |  |
| rlm_quiet | close | pin $2k+ | 12-16 | 42.9 | -1.5 | 25.5 |  |
| rlm_quiet | close | pin limit <$1k | 5-8 | 38.5 | -3.1 | -25.5 |  |
| pin_move | close | 1-3k bets | 57-62 | 47.9 | -1.7 | -7.2 |  |
| pin_move | close | 3k+ bets | 8-11 | 42.1 | -6.3 | -17.0 |  |
| pin_move | close | <1k bets | 10-11 | 47.6 | -3.9 | -10.9 |  |
| pin_move | close | pin $1-2k | 36-38 | 48.6 | -0.5 | -4.2 |  |
| pin_move | close | pin $2k+ | 25-28 | 47.2 | -3.6 | -10.7 |  |
| pin_move | close | pin limit <$1k | 14-18 | 43.8 | -5.5 | -16.4 |  |
| money_delta | close | 1-3k bets | 28-36 | 43.8 | 2.6 | -13.7 |  |
| money_delta | close | 3k+ bets | 6-4 | 60.0 | 15.2 | 21.7 |  |
| money_delta | close | <1k bets | 10-10 | 50.0 | 8.7 | 17.9 |  |
| money_delta | close | pin $1-2k | 18-14 | 56.2 | 14.0 | 19.8 |  |
| money_delta | close | pin $2k+ | 7-11 | 38.9 | -0.9 | -20.0 |  |
| money_delta | close | pin limit <$1k | 8-11 | 42.1 | 0.9 | -18.7 |  |
| pin_rlm | close | 1-3k bets | 10-16 | 38.5 | -1.7 | -23.1 |  |
| pin_rlm | close | 3k+ bets | 2-2 | 50.0 | 11.6 | 7.3 |  |
| pin_rlm | close | <1k bets | 1-3 | 25.0 | -15.4 | -52.3 |  |
| pin_rlm | close | pin $1-2k | 7-6 | 53.8 | 13.3 | 4.6 |  |
| pin_rlm | close | pin $2k+ | 3-7 | 30.0 | -9.2 | -32.6 |  |
| pin_rlm | close | pin limit <$1k | 3-8 | 27.3 | -12.7 | -46.7 |  |
| follow_move | close | 1-3k bets | 83-111 | 42.8 | -6.6 | -13.9 |  |
| follow_move | close | 3k+ bets | 12-14 | 46.2 | -4.2 | -14.9 |  |
| follow_move | close | <1k bets | 23-31 | 42.6 | -5.7 | -25.0 |  |
| follow_move | close | pin $1-2k | 46-53 | 46.5 | -2.4 | -11.6 |  |
| follow_move | close | pin $2k+ | 32-36 | 47.1 | -3.6 | 3.3 |  |
| follow_move | close | pin limit <$1k | 14-23 | 37.8 | -10.7 | -27.5 |  |
| rlm_ratio | close | 1-3k bets | 17-35 | 32.7 | -8.1 | -35.2 |  |
| rlm_ratio | close | 3k+ bets | 3-3 | 50.0 | 8.3 | 3.3 |  |
| rlm_ratio | close | <1k bets | 3-7 | 30.0 | -9.2 | -42.9 |  |
| rlm_ratio | close | pin $1-2k | 11-8 | 57.9 | 18.3 | 14.0 |  |
| rlm_ratio | close | pin $2k+ | 2-9 | 18.2 | -18.8 | -59.8 |  |
| rlm_ratio | close | pin limit <$1k | 5-10 | 33.3 | -8.0 | -35.7 |  |
| money_level | close | 1-3k bets | 108-86 | 55.7 | -1.1 | -5.0 |  |
| money_level | close | 3k+ bets | 19-15 | 55.9 | 1.0 | -3.5 |  |
| money_level | close | <1k bets | 38-11 | 77.6 | 20.8 | 32.8 |  |
| money_level | close | pin $1-2k | 54-36 | 60.0 | 3.9 | 5.8 |  |
| money_level | close | pin $2k+ | 35-37 | 48.6 | -6.8 | -21.0 |  |
| money_level | close | pin limit <$1k | 22-18 | 55.0 | -0.4 | 4.4 |  |
| sharp_gap | close | 1-3k bets | 78-99 | 44.1 | -3.9 | -17.0 |  |
| sharp_gap | close | 3k+ bets | 17-16 | 51.5 | 1.3 | -1.1 |  |
| sharp_gap | close | <1k bets | 25-20 | 55.6 | 8.4 | 8.4 |  |
| sharp_gap | close | pin $1-2k | 45-36 | 55.6 | 6.2 | 7.2 |  |
| sharp_gap | close | pin $2k+ | 29-38 | 43.3 | -3.8 | -16.6 |  |
| sharp_gap | close | pin limit <$1k | 13-23 | 36.1 | -10.6 | -30.9 |  |
| money_moving | close | 1-3k bets | 81-100 | 44.8 | -3.8 | -16.8 |  |
| money_moving | close | 3k+ bets | 17-16 | 51.5 | 1.3 | -1.1 |  |
| money_moving | close | <1k bets | 26-19 | 57.8 | 10.0 | 10.5 |  |
| money_moving | close | pin $1-2k | 45-36 | 55.6 | 5.7 | 6.2 |  |
| money_moving | close | pin $2k+ | 29-38 | 43.3 | -3.8 | -16.6 |  |
| money_moving | close | pin limit <$1k | 15-25 | 37.5 | -10.0 | -28.4 |  |
| pin_value | close | 1-3k bets | 52-36 | 59.1 | 8.2 | 24.7 |  |
| pin_value | close | 3k+ bets | 5-6 | 45.5 | -8.8 | -12.2 |  |
| pin_value | close | <1k bets | 11-7 | 61.1 | 12.2 | 35.7 |  |
| pin_value | close | pin $1-2k | 31-27 | 53.4 | 3.6 | 10.8 |  |
| pin_value | close | pin $2k+ | 17-13 | 56.7 | 7.8 | 38.7 |  |
| pin_value | close | pin limit <$1k | 20-9 | 69.0 | 14.0 | 30.8 |  |
| consensus_gap | close | 1-3k bets | 37-32 | 53.6 | -0.1 | -5.8 |  |
| consensus_gap | close | 3k+ bets | 6-3 | 66.7 | 13.5 | 13.8 |  |
| consensus_gap | close | <1k bets | 15-3 | 83.3 | 30.1 | 56.5 |  |
| consensus_gap | close | pin $1-2k | 14-13 | 51.9 | -2.8 | 10.5 |  |
| consensus_gap | close | pin $2k+ | 25-11 | 69.4 | 14.0 | 13.9 |  |
| consensus_gap | close | pin limit <$1k | 7-2 | 77.8 | 27.1 | 48.3 |  |
| follow_move+pin_move | close | 1-3k bets | 35-54 | 39.3 | -9.7 | -24.1 |  |
| money_delta+money_moving | close | 1-3k bets | 20-25 | 44.4 | 3.7 | -11.4 |  |
| money_delta+sharp_gap | close | 1-3k bets | 20-24 | 45.5 | 4.7 | -9.4 |  |
| money_moving+sharp_gap | close | 1-3k bets | 76-96 | 44.2 | -3.9 | -16.8 |  |
| consensus_gap+money_level | close | 1-3k bets | 26-19 | 57.8 | -1.3 | -6.0 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 30-53 | 36.1 | -5.4 | -13.1 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 15-24 | 38.5 | -4.6 | -21.3 |  |
| consensus_gap+follow_move | close | 1-3k bets | 11-13 | 45.8 | -6.7 | -19.5 |  |
| follow_move+money_level | close | 1-3k bets | 38-40 | 48.7 | -8.0 | -14.8 |  |
| money_level+money_moving | close | 1-3k bets | 55-53 | 50.9 | -3.0 | -9.4 |  |
| money_level+sharp_gap | close | 1-3k bets | 52-52 | 50.0 | -3.4 | -9.4 |  |
| consensus_gap+money_moving | close | 1-3k bets | 10-19 | 34.5 | -17.0 | -39.7 |  |
| consensus_gap+pin_move | close | 1-3k bets | 9-6 | 60.0 | 9.1 | 19.6 |  |
| consensus_gap+pin_value | close | 1-3k bets | 13-12 | 52.0 | 2.0 | -2.5 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 9-18 | 33.3 | -17.4 | -39.4 |  |
| follow_move+money_moving | close | 1-3k bets | 37-59 | 38.5 | -9.7 | -28.0 |  |
| follow_move+pin_value | close | 1-3k bets | 15-12 | 55.6 | 4.0 | 41.0 |  |
| follow_move+sharp_gap | close | 1-3k bets | 39-60 | 39.4 | -8.5 | -26.3 |  |
| money_level+pin_move | close | 1-3k bets | 23-24 | 48.9 | -6.4 | -12.2 |  |
| money_level+pin_value | close | 1-3k bets | 17-14 | 54.8 | 0.1 | 3.0 |  |
| money_moving+pin_move | close | 1-3k bets | 24-26 | 48.0 | -0.3 | -7.9 |  |
| money_moving+pin_value | close | 1-3k bets | 15-16 | 48.4 | -3.3 | -8.9 |  |
| pin_move+pin_value | close | 1-3k bets | 18-14 | 56.2 | 3.9 | 5.8 |  |
| pin_move+sharp_gap | close | 1-3k bets | 22-27 | 44.9 | -2.7 | -13.8 |  |
| pin_value+sharp_gap | close | 1-3k bets | 14-14 | 50.0 | -0.8 | -5.9 |  |
| follow_move+money_delta | close | 1-3k bets | 17-27 | 38.6 | -3.4 | -24.3 |  |
| money_delta+pin_move | close | 1-3k bets | 10-12 | 45.5 | 5.3 | -10.6 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 11-21 | 34.4 | -5.8 | -31.9 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 17-35 | 32.7 | -8.1 | -35.2 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 12-26 | 31.6 | -7.3 | -36.0 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 17-33 | 34.0 | -7.0 | -32.6 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 8-25 | 24.2 | -14.5 | -51.3 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 12-28 | 30.0 | -8.7 | -39.2 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 17-35 | 32.7 | -8.1 | -35.2 |  |
| money_delta+money_level | close | 1-3k bets | 6-5 | 54.5 | 8.4 | 5.2 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 3-7 | 30.0 | -9.5 | -41.8 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 2-4 | 33.3 | -3.8 | -34.9 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 12-19 | 38.7 | -2.1 | -23.3 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 1-2 | 33.3 | -13.5 | -33.3 |  |
| money_level+pin_rlm | close | 1-3k bets | 4-3 | 57.1 | 14.0 | 11.3 |  |
| money_moving+pin_rlm | close | 1-3k bets | 10-15 | 40.0 | -0.3 | -20.0 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 10-16 | 38.5 | -1.7 | -23.1 |  |
| money_level+rlm_ratio | close | 1-3k bets | 7-8 | 46.7 | 1.9 | -9.5 |  |
| consensus_gap+money_delta | close | 1-3k bets | 2-2 | 50.0 | 12.5 | -2.3 |  |
| follow_move+pin_rlm | close | 1-3k bets | 8-13 | 38.1 | -0.4 | -24.9 |  |
| money_delta+pin_rlm | close | 1-3k bets | 6-9 | 40.0 | 1.7 | -20.3 |  |
| pin_move+pin_rlm | close | 1-3k bets | 10-11 | 47.6 | 7.8 | -4.7 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 8-10 | 44.4 | 5.6 | -12.4 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 4-10 | 28.6 | -9.6 | -43.0 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 8-13 | 38.1 | -0.4 | -24.9 |  |
| money_delta+pin_value | close | 1-3k bets | 7-3 | 70.0 | 27.7 | 33.2 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 5-5 | 50.0 | 6.3 | 92.8 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 2-0 | 100.0 | 50.0 | 88.9 |  |
| pin_rlm+pin_value | close | 1-3k bets | 1-1 | 50.0 | 0.4 | -4.5 |  |
| money_level+money_moving | close | 3k+ bets | 12-10 | 54.5 | 0.9 | 0.0 |  |
| money_level+sharp_gap | close | 3k+ bets | 12-10 | 54.5 | 0.9 | 0.0 |  |
| money_moving+sharp_gap | close | 3k+ bets | 17-16 | 51.5 | 1.3 | -1.1 |  |
| follow_move+money_delta | close | 3k+ bets | 3-3 | 50.0 | 4.0 | -3.8 |  |
| follow_move+money_level | close | 3k+ bets | 7-4 | 63.6 | 5.1 | 5.4 |  |
| follow_move+money_moving | close | 3k+ bets | 8-6 | 57.1 | 6.9 | 5.7 |  |
| follow_move+pin_move | close | 3k+ bets | 6-9 | 40.0 | -8.3 | -21.8 |  |
| follow_move+pin_rlm | close | 3k+ bets | 2-2 | 50.0 | 11.6 | 7.3 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 3-3 | 50.0 | 8.3 | 3.3 |  |
| follow_move+sharp_gap | close | 3k+ bets | 8-6 | 57.1 | 6.9 | 5.7 |  |
| money_delta+money_level | close | 3k+ bets | 2-0 | 100.0 | 50.0 | 93.0 |  |
| money_delta+money_moving | close | 3k+ bets | 5-2 | 71.4 | 27.3 | 45.6 |  |
| money_delta+pin_move | close | 3k+ bets | 2-3 | 40.0 | -3.3 | -22.8 |  |
| money_delta+pin_rlm | close | 3k+ bets | 1-2 | 33.3 | -5.7 | -34.9 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 2-2 | 50.0 | 5.8 | -3.5 |  |
| money_delta+sharp_gap | close | 3k+ bets | 5-2 | 71.4 | 27.3 | 45.6 |  |
| money_level+pin_move | close | 3k+ bets | 3-3 | 50.0 | -5.3 | -9.2 |  |
| money_level+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 59.6 | 95.2 |  |
| money_level+rlm_ratio | close | 3k+ bets | 2-0 | 100.0 | 50.0 | 93.0 |  |
| money_moving+pin_move | close | 3k+ bets | 4-4 | 50.0 | 2.4 | -8.1 |  |
| money_moving+pin_rlm | close | 3k+ bets | 2-2 | 50.0 | 11.6 | 7.3 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 3-3 | 50.0 | 8.3 | 3.3 |  |
| pin_move+pin_rlm | close | 3k+ bets | 1-2 | 33.3 | -5.7 | -34.9 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 1-2 | 33.3 | -5.7 | -34.9 |  |
| pin_move+sharp_gap | close | 3k+ bets | 4-4 | 50.0 | 2.4 | -8.1 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 2-2 | 50.0 | 11.6 | 7.3 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 2-2 | 50.0 | 11.6 | 7.3 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 3-3 | 50.0 | 8.3 | 3.3 |  |
| consensus_gap+money_level | close | 3k+ bets | 4-1 | 80.0 | 18.1 | 25.1 |  |
| consensus_gap+money_moving | close | 3k+ bets | 3-2 | 60.0 | 3.6 | 1.4 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 3-2 | 60.0 | 3.6 | 1.4 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 3-8 | 27.3 | -15.5 | -42.9 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 3-6 | 33.3 | -10.4 | -30.2 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 1-3 | 25.0 | -19.0 | -52.3 |  |
| money_level+pin_value | close | 3k+ bets | 3-3 | 50.0 | -4.0 | -5.5 |  |
| money_moving+pin_value | close | 3k+ bets | 3-3 | 50.0 | -3.1 | -5.2 |  |
| pin_value+sharp_gap | close | 3k+ bets | 3-3 | 50.0 | -3.1 | -5.2 |  |
| consensus_gap+follow_move | close | 3k+ bets | 3-0 | 100.0 | 39.4 | 69.0 |  |
| consensus_gap+pin_value | close | 3k+ bets | 4-0 | 100.0 | 46.3 | 93.8 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 1-4 | 20.0 | -22.5 | -61.8 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 1-4 | 20.0 | -22.5 | -61.8 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 0-2 | 0.0 | -38.4 | -100.0 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 0-3 | 0.0 | -37.8 | -100.0 |  |
| pin_move+pin_value | close | 3k+ bets | 3-4 | 42.9 | -11.2 | -16.3 |  |
| follow_move+pin_value | close | 3k+ bets | 2-2 | 50.0 | -10.2 | -5.5 |  |
| consensus_gap+money_delta | close | 3k+ bets | 1-0 | 100.0 | 41.2 | 90.9 |  |
| consensus_gap+pin_move | close | 3k+ bets | 3-0 | 100.0 | 48.3 | 95.3 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 1-0 | 100.0 | 41.2 | 90.9 |  |
| money_delta+pin_value | close | 3k+ bets | 1-0 | 100.0 | 41.2 | 90.9 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 1-1 | 50.0 | -8.8 | -4.5 |  |
| consensus_gap+money_level | close | <1k bets | 11-1 | 91.7 | 34.5 | 42.3 |  |
| consensus_gap+money_moving | close | <1k bets | 8-0 | 100.0 | 46.0 | 103.6 |  |
| consensus_gap+pin_value | close | <1k bets | 4-1 | 80.0 | 36.2 | 123.1 |  |
| consensus_gap+sharp_gap | close | <1k bets | 9-1 | 90.0 | 36.8 | 77.0 |  |
| follow_move+pin_move | close | <1k bets | 6-10 | 37.5 | -12.7 | -30.3 |  |
| follow_move+rlm_quiet | close | <1k bets | 4-17 | 19.0 | -22.3 | -63.3 |  |
| money_level+money_moving | close | <1k bets | 20-5 | 80.0 | 25.5 | 38.3 |  |
| money_level+pin_value | close | <1k bets | 5-1 | 83.3 | 32.9 | 56.7 |  |
| money_level+sharp_gap | close | <1k bets | 19-5 | 79.2 | 25.1 | 40.2 |  |
| money_moving+pin_value | close | <1k bets | 4-1 | 80.0 | 40.1 | 124.8 |  |
| money_moving+sharp_gap | close | <1k bets | 24-18 | 57.1 | 9.9 | 12.8 |  |
| pin_move+rlm_quiet | close | <1k bets | 2-4 | 33.3 | -12.5 | -36.4 |  |
| pin_value+sharp_gap | close | <1k bets | 4-1 | 80.0 | 40.1 | 124.8 |  |
| follow_move+money_moving | close | <1k bets | 10-10 | 50.0 | 2.7 | -17.8 |  |
| follow_move+sharp_gap | close | <1k bets | 9-10 | 47.4 | 0.9 | -18.3 |  |
| money_level+pin_move | close | <1k bets | 6-3 | 66.7 | 10.4 | 22.8 |  |
| money_moving+rlm_quiet | close | <1k bets | 2-6 | 25.0 | -13.9 | -52.3 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 2-6 | 25.0 | -13.9 | -52.3 |  |
| follow_move+money_delta | close | <1k bets | 5-7 | 41.7 | -1.2 | -20.5 |  |
| follow_move+pin_rlm | close | <1k bets | 1-3 | 25.0 | -15.4 | -52.3 |  |
| follow_move+pin_value | close | <1k bets | 3-2 | 60.0 | 11.8 | 15.4 |  |
| follow_move+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -9.2 | -42.9 |  |
| money_delta+money_moving | close | <1k bets | 7-8 | 46.7 | 7.6 | 18.9 |  |
| money_delta+pin_move | close | <1k bets | 1-2 | 33.3 | -7.0 | -36.4 |  |
| money_delta+pin_rlm | close | <1k bets | 1-2 | 33.3 | -7.0 | -36.4 |  |
| money_delta+pin_value | close | <1k bets | 3-0 | 100.0 | 60.9 | 212.0 |  |
| money_delta+rlm_quiet | close | <1k bets | 3-4 | 42.9 | 1.5 | -17.2 |  |
| money_delta+rlm_ratio | close | <1k bets | 3-5 | 37.5 | -1.9 | -28.6 |  |
| money_delta+sharp_gap | close | <1k bets | 7-8 | 46.7 | 7.6 | 18.9 |  |
| money_moving+pin_move | close | <1k bets | 3-3 | 50.0 | 6.3 | -5.2 |  |
| money_moving+pin_rlm | close | <1k bets | 1-3 | 25.0 | -15.4 | -52.3 |  |
| money_moving+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -9.2 | -42.9 |  |
| pin_move+pin_rlm | close | <1k bets | 1-3 | 25.0 | -15.4 | -52.3 |  |
| pin_move+pin_value | close | <1k bets | 4-1 | 80.0 | 28.2 | 52.8 |  |
| pin_move+rlm_ratio | close | <1k bets | 1-3 | 25.0 | -15.4 | -52.3 |  |
| pin_move+sharp_gap | close | <1k bets | 3-3 | 50.0 | 6.3 | -5.2 |  |
| pin_rlm+pin_value | close | <1k bets | 1-0 | 100.0 | 59.6 | 90.9 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 1-1 | 50.0 | 9.6 | -4.5 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 1-3 | 25.0 | -15.4 | -52.3 |  |
| pin_rlm+sharp_gap | close | <1k bets | 1-3 | 25.0 | -15.4 | -52.3 |  |
| pin_value+rlm_quiet | close | <1k bets | 2-0 | 100.0 | 59.6 | 90.9 |  |
| pin_value+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 59.6 | 90.9 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 2-5 | 28.6 | -10.1 | -45.5 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 3-7 | 30.0 | -9.2 | -42.9 |  |
| consensus_gap+follow_move | close | <1k bets | 5-0 | 100.0 | 45.8 | 71.3 |  |
| consensus_gap+pin_move | close | <1k bets | 2-0 | 100.0 | 48.1 | 70.5 |  |
| follow_move+money_level | close | <1k bets | 12-4 | 75.0 | 17.4 | 21.7 |  |
| money_delta+money_level | close | <1k bets | 2-1 | 66.7 | 27.6 | 53.8 |  |
| money_level+pin_rlm | close | <1k bets | 0-1 | 0.0 | -40.4 | -100.0 |  |
| money_level+rlm_ratio | close | <1k bets | 1-1 | 50.0 | 9.6 | -5.3 |  |
| consensus_gap+money_delta | close | <1k bets | 3-0 | 100.0 | 53.2 | 208.0 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 59.6 | 89.3 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-0 | 100.0 | 59.6 | 90.9 |  |
| money_delta+money_moving | close | pin $1-2k | 10-5 | 66.7 | 26.3 | 53.1 |  |
| money_delta+sharp_gap | close | pin $1-2k | 10-5 | 66.7 | 26.3 | 53.1 |  |
| money_moving+sharp_gap | close | pin $1-2k | 43-34 | 55.8 | 6.3 | 8.4 |  |
| consensus_gap+follow_move | close | pin $1-2k | 6-6 | 50.0 | -5.0 | -11.6 |  |
| consensus_gap+money_level | close | pin $1-2k | 8-7 | 53.3 | -6.9 | -13.5 |  |
| consensus_gap+money_moving | close | pin $1-2k | 5-6 | 45.5 | -7.2 | 5.9 |  |
| consensus_gap+pin_move | close | pin $1-2k | 4-4 | 50.0 | -1.2 | 18.6 |  |
| consensus_gap+pin_value | close | pin $1-2k | 5-6 | 45.5 | -6.8 | 18.8 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 5-5 | 50.0 | -4.2 | 19.3 |  |
| follow_move+money_level | close | pin $1-2k | 23-16 | 59.0 | 4.1 | 6.1 |  |
| follow_move+money_moving | close | pin $1-2k | 23-19 | 54.8 | 6.5 | 2.4 |  |
| follow_move+pin_move | close | pin $1-2k | 21-35 | 37.5 | -10.7 | -26.4 |  |
| follow_move+pin_value | close | pin $1-2k | 9-10 | 47.4 | -3.0 | -10.1 |  |
| follow_move+sharp_gap | close | pin $1-2k | 25-20 | 55.6 | 7.4 | 3.0 |  |
| money_level+money_moving | close | pin $1-2k | 34-20 | 63.0 | 8.8 | 12.8 |  |
| money_level+pin_move | close | pin $1-2k | 14-12 | 53.8 | -1.0 | -0.7 |  |
| money_level+pin_value | close | pin $1-2k | 10-8 | 55.6 | 2.1 | 3.5 |  |
| money_level+sharp_gap | close | pin $1-2k | 34-20 | 63.0 | 9.2 | 14.3 |  |
| money_moving+pin_move | close | pin $1-2k | 17-12 | 58.6 | 10.3 | 10.8 |  |
| money_moving+pin_value | close | pin $1-2k | 11-9 | 55.0 | 4.1 | 21.4 |  |
| pin_move+pin_value | close | pin $1-2k | 12-8 | 60.0 | 7.4 | 13.2 |  |
| pin_move+sharp_gap | close | pin $1-2k | 17-13 | 56.7 | 8.8 | 7.1 |  |
| pin_value+sharp_gap | close | pin $1-2k | 11-8 | 57.9 | 7.5 | 27.8 |  |
| follow_move+money_delta | close | pin $1-2k | 12-12 | 50.0 | 6.8 | -3.0 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 14-27 | 34.1 | -7.8 | -29.9 |  |
| money_delta+pin_move | close | pin $1-2k | 8-7 | 53.3 | 13.2 | 4.0 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 7-12 | 36.8 | -5.0 | -28.4 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 10-17 | 37.0 | -5.3 | -25.6 |  |
| follow_move+pin_rlm | close | pin $1-2k | 6-6 | 50.0 | 10.9 | -2.6 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 11-8 | 57.9 | 18.3 | 14.0 |  |
| pin_move+pin_rlm | close | pin $1-2k | 7-4 | 63.6 | 22.3 | 23.7 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 6-4 | 60.0 | 20.4 | 16.9 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 3-6 | 33.3 | -5.7 | -35.4 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 6-6 | 50.0 | 10.9 | -2.6 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 7-6 | 53.8 | 13.3 | 4.6 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 4-7 | 36.4 | -2.3 | -29.0 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 6-9 | 40.0 | 1.2 | -22.2 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 11-8 | 57.9 | 18.3 | 14.0 |  |
| money_delta+money_level | close | pin $1-2k | 4-0 | 100.0 | 55.8 | 95.8 |  |
| money_delta+pin_rlm | close | pin $1-2k | 5-3 | 62.5 | 23.1 | 22.3 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 7-4 | 63.6 | 22.6 | 24.1 |  |
| money_level+pin_rlm | close | pin $1-2k | 3-0 | 100.0 | 60.9 | 96.0 |  |
| money_level+rlm_ratio | close | pin $1-2k | 6-1 | 85.7 | 44.2 | 66.7 |  |
| money_moving+pin_rlm | close | pin $1-2k | 7-5 | 58.3 | 17.4 | 13.4 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 11-7 | 61.1 | 21.4 | 20.3 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 6-8 | 42.9 | 3.9 | -16.6 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 1-3 | 25.0 | -17.1 | -52.3 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 4-5 | 44.4 | 0.0 | -14.7 |  |
| money_delta+pin_value | close | pin $1-2k | 6-3 | 66.7 | 26.7 | 67.2 |  |
| consensus_gap+money_delta | close | pin $1-2k | 2-1 | 66.7 | 21.2 | 144.9 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 0-1 | 0.0 | -36.5 | -100.0 |  |
| pin_rlm+pin_value | close | pin $1-2k | 2-0 | 100.0 | 50.4 | 90.9 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 1-0 | 100.0 | 59.6 | 90.9 |  |
| follow_move+pin_move | close | pin $2k+ | 18-25 | 41.9 | -9.1 | -21.5 |  |
| consensus_gap+money_level | close | pin $2k+ | 18-10 | 64.3 | 6.1 | -0.8 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 12-16 | 42.9 | -1.5 | 25.5 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 7-13 | 35.0 | -10.2 | -25.5 |  |
| money_level+money_moving | close | pin $2k+ | 17-24 | 41.5 | -9.9 | -25.9 |  |
| money_level+sharp_gap | close | pin $2k+ | 17-24 | 41.5 | -9.9 | -25.9 |  |
| money_moving+sharp_gap | close | pin $2k+ | 29-38 | 43.3 | -3.8 | -16.6 |  |
| consensus_gap+pin_value | close | pin $2k+ | 10-5 | 66.7 | 20.7 | 25.8 |  |
| follow_move+money_level | close | pin $2k+ | 10-12 | 45.5 | -14.9 | -27.8 |  |
| follow_move+money_moving | close | pin $2k+ | 11-17 | 39.3 | -10.1 | -27.1 |  |
| follow_move+sharp_gap | close | pin $2k+ | 11-17 | 39.3 | -10.1 | -27.1 |  |
| money_level+pin_move | close | pin $2k+ | 8-9 | 47.1 | -12.7 | -24.0 |  |
| money_moving+pin_move | close | pin $2k+ | 7-10 | 41.2 | -7.2 | -20.2 |  |
| pin_move+sharp_gap | close | pin $2k+ | 7-10 | 41.2 | -7.2 | -20.2 |  |
| money_delta+money_level | close | pin $2k+ | 1-1 | 50.0 | 8.8 | -4.5 |  |
| money_delta+money_moving | close | pin $2k+ | 6-11 | 35.3 | -3.4 | -26.5 |  |
| money_delta+sharp_gap | close | pin $2k+ | 6-11 | 35.3 | -3.4 | -26.5 |  |
| consensus_gap+money_moving | close | pin $2k+ | 7-8 | 46.7 | -7.3 | -21.1 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 7-8 | 46.7 | -7.3 | -21.1 |  |
| money_level+pin_value | close | pin $2k+ | 4-6 | 40.0 | -8.8 | -24.4 |  |
| money_moving+pin_value | close | pin $2k+ | 4-6 | 40.0 | -8.2 | -24.0 |  |
| pin_value+sharp_gap | close | pin $2k+ | 4-6 | 40.0 | -8.2 | -24.0 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -63.5 | -100.0 |  |
| money_level+pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -63.5 | -100.0 |  |
| money_moving+pin_rlm | close | pin $2k+ | 3-7 | 30.0 | -9.2 | -32.6 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 3-7 | 30.0 | -9.2 | -32.6 |  |
| follow_move+money_delta | close | pin $2k+ | 3-7 | 30.0 | -11.5 | -41.0 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 2-9 | 18.2 | -18.8 | -59.8 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 1-7 | 12.5 | -24.6 | -74.0 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 2-9 | 18.2 | -18.8 | -59.8 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 2-9 | 18.2 | -18.8 | -59.8 |  |
| money_level+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -36.5 | -100.0 |  |
| consensus_gap+follow_move | close | pin $2k+ | 7-1 | 87.5 | 24.6 | 40.5 |  |
| consensus_gap+pin_move | close | pin $2k+ | 8-1 | 88.9 | 33.9 | 53.5 |  |
| follow_move+pin_value | close | pin $2k+ | 4-3 | 57.1 | 5.9 | 146.4 |  |
| pin_move+pin_value | close | pin $2k+ | 6-6 | 50.0 | -0.1 | -5.0 |  |
| follow_move+pin_rlm | close | pin $2k+ | 2-5 | 28.6 | -8.0 | -36.9 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 2-5 | 28.6 | -8.0 | -36.9 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 2-1 | 66.7 | 15.3 | 350.3 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 3-7 | 30.0 | -9.1 | -36.9 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 3-7 | 30.0 | -9.1 | -36.9 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 3-5 | 37.5 | -4.6 | -26.3 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 1-6 | 14.3 | -22.3 | -70.3 |  |
| money_delta+pin_move | close | pin $2k+ | 3-4 | 42.9 | -0.0 | -15.7 |  |
| money_delta+pin_rlm | close | pin $2k+ | 1-5 | 16.7 | -19.9 | -65.3 |  |
| pin_move+pin_rlm | close | pin $2k+ | 2-4 | 33.3 | -3.2 | -26.7 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 1-4 | 20.0 | -16.5 | -58.4 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 1-4 | 20.0 | -16.5 | -58.4 |  |
| consensus_gap+money_delta | close | pin $2k+ | 1-0 | 100.0 | 41.2 | 90.9 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 1-0 | 100.0 | 41.2 | 90.9 |  |
| money_delta+pin_value | close | pin $2k+ | 1-0 | 100.0 | 41.2 | 90.9 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 4-1 | 80.0 | 32.7 | 53.8 |  |
| consensus_gap+money_level | close | pin limit <$1k | 4-1 | 80.0 | 20.4 | 50.5 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 3-2 | 60.0 | 12.7 | 15.6 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 6-2 | 75.0 | 22.6 | 41.8 |  |
| follow_move+money_level | close | pin limit <$1k | 8-12 | 40.0 | -12.9 | -23.6 |  |
| follow_move+money_moving | close | pin limit <$1k | 7-17 | 29.2 | -17.5 | -44.1 |  |
| follow_move+pin_value | close | pin limit <$1k | 7-3 | 70.0 | 14.3 | 32.9 |  |
| money_level+money_moving | close | pin limit <$1k | 9-13 | 40.9 | -11.7 | -22.4 |  |
| money_level+pin_value | close | pin limit <$1k | 11-4 | 73.3 | 15.0 | 38.8 |  |
| money_moving+pin_value | close | pin limit <$1k | 7-5 | 58.3 | 6.7 | 10.7 |  |
| follow_move+pin_move | close | pin limit <$1k | 8-13 | 38.1 | -9.4 | -26.6 |  |
| money_level+pin_move | close | pin limit <$1k | 10-9 | 52.6 | 0.1 | 0.1 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 13-23 | 36.1 | -10.6 | -30.9 |  |
| pin_move+pin_value | close | pin limit <$1k | 7-5 | 58.3 | 3.6 | 11.1 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 5-8 | 38.5 | -3.1 | -25.5 |  |
| money_moving+pin_move | close | pin limit <$1k | 7-11 | 38.9 | -7.7 | -25.7 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 2-0 | 100.0 | 61.6 | 95.5 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 2-1 | 66.7 | 27.6 | 30.3 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 1-1 | 50.0 | 11.6 | 0.0 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 3-0 | 100.0 | 60.9 | 93.9 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 2-0 | 100.0 | 61.6 | 95.5 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 3-1 | 75.0 | 30.8 | 44.5 |  |
| follow_move+money_delta | close | pin limit <$1k | 4-8 | 33.3 | -8.3 | -35.6 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 3-7 | 30.0 | -10.0 | -41.4 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 5-10 | 33.3 | -8.0 | -35.7 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 7-16 | 30.4 | -15.6 | -41.7 |  |
| money_delta+money_moving | close | pin limit <$1k | 7-9 | 43.8 | 2.4 | -15.4 |  |
| money_delta+pin_move | close | pin limit <$1k | 2-6 | 25.0 | -14.9 | -50.6 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 2-5 | 28.6 | -11.2 | -43.5 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 2-2 | 50.0 | 10.6 | -2.3 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 4-7 | 36.4 | -5.4 | -29.7 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 7-9 | 43.8 | 2.4 | -15.4 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 3-8 | 27.3 | -12.7 | -46.7 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 2-5 | 28.6 | -11.2 | -44.2 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 5-10 | 33.3 | -8.0 | -35.7 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 3-8 | 27.3 | -12.7 | -46.7 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 3-4 | 42.9 | 0.3 | -16.9 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 3-7 | 30.0 | -10.0 | -41.4 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 5-11 | 31.2 | -13.7 | -40.0 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 1-3 | 25.0 | -14.4 | -50.0 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 3-7 | 30.0 | -10.0 | -41.4 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 3-8 | 27.3 | -12.7 | -46.7 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 2-5 | 28.6 | -11.2 | -44.2 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 2-5 | 28.6 | -11.2 | -44.2 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 5-10 | 33.3 | -8.0 | -35.7 |  |
| money_delta+pin_value | close | pin limit <$1k | 4-0 | 100.0 | 54.8 | 91.0 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 2-0 | 100.0 | 59.6 | 90.9 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 6-4 | 60.0 | 10.0 | 13.8 |  |
| money_level+sharp_gap | close | pin limit <$1k | 7-12 | 36.8 | -14.7 | -30.1 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 0-1 | 0.0 | -40.4 | -100.0 |  |
| money_delta+money_level | close | pin limit <$1k | 1-4 | 20.0 | -20.4 | -61.0 |  |
| money_level+pin_rlm | close | pin limit <$1k | 2-3 | 40.0 | -0.4 | -22.8 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 2-4 | 33.3 | -7.0 | -35.7 |  |
| rlm_quiet | early | <1k bets | 8-12 | 40.0 | 1.7 | -11.0 | 0.33 |
| rlm_quiet | early | pin $1-2k | 1-0 | 100.0 | 63.5 | 132.0 | -1.8 |
| rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -40.4 | -100.0 | 0.0 |
| pin_move | early | <1k bets | 3-4 | 42.9 | -6.0 | -18.2 | 0.0 |
| pin_move | early | pin $1-2k | 0-2 | 0.0 | -41.2 | -100.0 | 0.0 |
| pin_move | early | pin limit <$1k | 3-2 | 60.0 | 8.1 | 14.5 | 0.0 |
| money_delta | early | <1k bets | 1-1 | 50.0 | 9.6 | -4.5 | 1.5 |
| money_delta | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| pin_rlm | early | <1k bets | 0-1 | 0.0 | -63.5 | -100.0 | 1.5 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -63.5 | -100.0 | 1.5 |
| follow_move | early | <1k bets | 69-83 | 45.4 | -2.7 | -14.1 | -0.03 |
| follow_move | early | pin $1-2k | 8-6 | 57.1 | 11.0 | 17.1 | -0.69 |
| follow_move | early | pin limit <$1k | 5-6 | 45.5 | 1.1 | -20.6 | -0.45 |
| rlm_ratio | early | <1k bets | 5-7 | 41.7 | -0.9 | -13.4 | 0.82 |
| rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -63.5 | -100.0 | 1.5 |
| rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| money_level | early | <1k bets | 21-20 | 51.2 | -8.2 | -17.4 | 0.01 |
| money_level | early | pin $1-2k | 0-2 | 0.0 | -63.5 | -100.0 | 1.6 |
| money_level | early | pin limit <$1k | 2-1 | 66.7 | 13.5 | 27.3 | 0.67 |
| sharp_gap | early | <1k bets | 15-19 | 44.1 | -3.0 | -12.9 | 0.33 |
| sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -63.5 | -100.0 | 1.6 |
| sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 26.3 | 27.3 | 0.0 |
| money_moving | early | <1k bets | 18-16 | 52.9 | 3.4 | -0.3 | 0.61 |
| money_moving | early | pin $1-2k | 0-1 | 0.0 | -63.5 | -100.0 | 1.7 |
| money_moving | early | pin limit <$1k | 2-1 | 66.7 | 26.3 | 27.3 | 0.0 |
| pin_value | early | <1k bets | 8-8 | 50.0 | 1.9 | -5.5 | -0.08 |
| pin_value | early | pin $1-2k | 2-6 | 25.0 | -21.2 | -53.2 | 0.21 |
| pin_value | early | pin limit <$1k | 6-2 | 75.0 | 25.0 | 42.2 | -0.38 |
| consensus_gap | early | <1k bets | 45-31 | 59.2 | 8.8 | 9.8 | 0.51 |
| consensus_gap | early | pin $1-2k | 3-2 | 60.0 | 13.6 | 17.8 | 0.28 |
| consensus_gap | early | pin limit <$1k | 4-0 | 100.0 | 45.2 | 89.9 | 0.25 |
| follow_move+money_level | early | <1k bets | 5-8 | 38.5 | -19.9 | -42.2 | 0.39 |
| follow_move+sharp_gap | early | <1k bets | 6-10 | 37.5 | -8.1 | -23.1 | 0.68 |
| money_level+sharp_gap | early | <1k bets | 7-10 | 41.2 | -14.8 | -26.9 | 0.31 |
| follow_move+money_moving | early | <1k bets | 9-9 | 50.0 | 2.2 | -6.8 | 0.79 |
| money_level+money_moving | early | <1k bets | 9-9 | 50.0 | -7.9 | -18.2 | 0.48 |
| consensus_gap+money_level | early | <1k bets | 8-5 | 61.5 | 4.6 | -7.8 | -0.32 |
| follow_move+rlm_quiet | early | <1k bets | 8-12 | 40.0 | 1.7 | -11.0 | 0.33 |
| follow_move+rlm_ratio | early | <1k bets | 5-7 | 41.7 | -0.9 | -13.4 | 0.82 |
| rlm_quiet+rlm_ratio | early | <1k bets | 4-4 | 50.0 | 11.6 | 6.1 | 0.04 |
| rlm_quiet+sharp_gap | early | <1k bets | 4-5 | 44.4 | 5.8 | -5.7 | 0.03 |
| rlm_ratio+sharp_gap | early | <1k bets | 5-7 | 41.7 | -0.9 | -13.4 | 0.82 |
| consensus_gap+follow_move | early | <1k bets | 5-5 | 50.0 | 1.2 | -13.3 | 0.96 |
| money_moving+rlm_quiet | early | <1k bets | 5-4 | 55.6 | 16.9 | 26.3 | 0.97 |
| money_moving+rlm_ratio | early | <1k bets | 5-3 | 62.5 | 20.8 | 29.9 | 1.57 |
| money_moving+sharp_gap | early | <1k bets | 11-10 | 52.4 | 4.0 | 6.1 | 0.72 |
| consensus_gap+money_moving | early | <1k bets | 4-2 | 66.7 | 16.0 | 2.8 | 0.35 |
| consensus_gap+sharp_gap | early | <1k bets | 4-3 | 57.1 | 9.1 | 2.4 | 0.04 |
| money_level+rlm_ratio | early | <1k bets | 1-3 | 25.0 | -25.7 | -52.3 | 2.38 |
| follow_move+pin_move | early | <1k bets | 1-3 | 25.0 | -20.4 | -52.3 | 0.5 |
| follow_move+money_delta | early | <1k bets | 1-1 | 50.0 | 9.6 | -4.5 | 1.5 |
| money_delta+money_level | early | <1k bets | 1-1 | 50.0 | 9.6 | -4.5 | 1.5 |
| money_delta+money_moving | early | <1k bets | 1-1 | 50.0 | 9.6 | -4.5 | 1.5 |
| money_delta+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 9.6 | -4.5 | 1.5 |
| money_delta+sharp_gap | early | <1k bets | 1-1 | 50.0 | 9.6 | -4.5 | 1.5 |
| follow_move+pin_value | early | <1k bets | 3-3 | 50.0 | 6.1 | -4.5 | -0.83 |
| consensus_gap+pin_move | early | <1k bets | 1-0 | 100.0 | 40.4 | 90.9 | 0.0 |
| consensus_gap+pin_value | early | <1k bets | 4-0 | 100.0 | 45.4 | 89.9 | 0.5 |
| money_level+pin_move | early | <1k bets | 1-0 | 100.0 | 40.4 | 90.9 | 0.0 |
| money_level+pin_value | early | <1k bets | 2-1 | 66.7 | 12.2 | 27.3 | 0.9 |
| pin_move+pin_value | early | <1k bets | 1-3 | 25.0 | -25.4 | -52.3 | 0.0 |
| money_moving+pin_value | early | <1k bets | 1-1 | 50.0 | -1.9 | -4.5 | 1.35 |
| pin_value+sharp_gap | early | <1k bets | 1-1 | 50.0 | -1.9 | -4.5 | 1.35 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| consensus_gap+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| follow_move+pin_rlm | early | <1k bets | 0-1 | 0.0 | -63.5 | -100.0 | 1.5 |
| money_level+pin_rlm | early | <1k bets | 0-1 | 0.0 | -63.5 | -100.0 | 1.5 |
| pin_rlm+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -63.5 | -100.0 | 1.5 |
| pin_rlm+sharp_gap | early | <1k bets | 0-1 | 0.0 | -63.5 | -100.0 | 1.5 |
| pin_move+pin_value | early | pin $1-2k | 0-2 | 0.0 | -41.2 | -100.0 | 0.0 |
| follow_move+rlm_quiet | early | pin $1-2k | 1-0 | 100.0 | 63.5 | 132.0 | -1.8 |
| money_level+money_moving | early | pin $1-2k | 0-1 | 0.0 | -63.5 | -100.0 | 1.7 |
| money_level+pin_value | early | pin $1-2k | 0-1 | 0.0 | -63.5 | -100.0 | 1.7 |
| money_level+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -63.5 | -100.0 | 1.6 |
| money_moving+pin_value | early | pin $1-2k | 0-1 | 0.0 | -63.5 | -100.0 | 1.7 |
| money_moving+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -63.5 | -100.0 | 1.7 |
| pin_value+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -63.5 | -100.0 | 1.7 |
| consensus_gap+pin_value | early | pin $1-2k | 1-0 | 100.0 | 41.2 | 87.0 | 0.0 |
| follow_move+money_level | early | pin $1-2k | 0-1 | 0.0 | -63.5 | -100.0 | 1.5 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -63.5 | -100.0 | 1.5 |
| follow_move+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -63.5 | -100.0 | 1.5 |
| follow_move+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -63.5 | -100.0 | 1.5 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -63.5 | -100.0 | 1.5 |
| money_level+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -63.5 | -100.0 | 1.5 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -63.5 | -100.0 | 1.5 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -63.5 | -100.0 | 1.5 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -63.5 | -100.0 | 1.5 |
| consensus_gap+follow_move | early | pin $1-2k | 1-0 | 100.0 | 63.5 | 106.0 | 1.5 |
| follow_move+pin_move | early | pin $1-2k | 0-1 | 0.0 | -41.2 | -100.0 | 0.0 |
| follow_move+pin_value | early | pin $1-2k | 0-1 | 0.0 | -41.2 | -100.0 | 0.0 |
| follow_move+pin_move | early | pin limit <$1k | 1-2 | 33.3 | -13.5 | -36.4 | 0.67 |
| follow_move+pin_value | early | pin limit <$1k | 3-2 | 60.0 | 15.6 | 14.5 | -1.0 |
| consensus_gap+money_level | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 90.9 | 0.5 |
| consensus_gap+pin_move | early | pin limit <$1k | 1-0 | 100.0 | 40.4 | 90.9 | 0.0 |
| consensus_gap+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 46.8 | 90.9 | 0.67 |
| follow_move+money_moving | early | pin limit <$1k | 1-1 | 50.0 | 9.6 | -4.5 | 0.5 |
| follow_move+rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -40.4 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 9.6 | -4.5 | 0.5 |
| money_level+pin_move | early | pin limit <$1k | 1-0 | 100.0 | 40.4 | 90.9 | 0.0 |
| money_level+pin_value | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 90.9 | 0.5 |
| money_moving+rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -40.4 | -100.0 | 0.0 |
| money_moving+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 26.3 | 27.3 | 0.0 |
| pin_move+pin_value | early | pin limit <$1k | 1-1 | 50.0 | -9.6 | -4.5 | 0.0 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -40.4 | -100.0 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| consensus_gap+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| follow_move+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| follow_move+money_level | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| follow_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| money_delta+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| money_delta+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| money_delta+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| money_level+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| money_level+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| money_level+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| money_moving+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| pin_value+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 59.6 | 90.9 | 1.0 |
