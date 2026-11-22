# CBB scorecard

Generated 2026-11-22 01:38 UTC. 752 graded games (36 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**684 games before 2026-11-21 (fit) · 68 on or after it (forward).**

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
sample ran **47.7% favourites** (n=751) and **50.7% overs** (n=752) and **72.5% moneyline favourites** (n=644).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-21. Nothing in the engine was chosen using these. n=68 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 6-7 | 46.2 | 37.1 | 9.0 | +0.24 | 1.8 | 0.5 | 46.2 | keep collecting (13/30) |
| money_delta | both | 0-1 | 0.0 | 39.7 | -39.7 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| follow_move | both | 37-48 | 43.5 | 47.6 | -4.1 | -11.73 | -13.8 | 0.31 | 38.8 | DROP: below break-even |
| rlm_ratio | both | 4-6 | 40.0 | 39.5 | 0.5 | -1.51 | -15.1 | 0.73 | 50.0 | keep collecting (10/30) |
| money_level | both | 13-15 | 46.4 | 60.6 | -14.1 | -7.64 | -27.3 | 0.03 | 35.7 | keep collecting (28/30) |
| sharp_gap | both | 11-13 | 45.8 | 45.3 | 0.6 | -2.05 | -8.6 | 0.47 | 50.0 | keep collecting (24/30) |
| money_moving | both | 12-10 | 54.5 | 48.6 | 5.9 | +1.83 | 8.3 | 0.59 | 50.0 | keep collecting (22/30) |
| pin_value | both | 2-1 | 66.7 | 43.6 | 23.0 | +0.78 | 26.0 | -0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap | both | 24-20 | 54.5 | 51.6 | 3.0 | -0.16 | -0.4 | 0.27 | 47.7 | no edge shown yet |
| follow_move+money_level | both | 2-7 | 22.2 | 58.8 | -36.5 | -5.98 | -66.4 | 0.33 | 33.3 | keep collecting (9/30) |
| follow_move+sharp_gap | both | 5-8 | 38.5 | 44.3 | -5.8 | -2.6 | -20.0 | 0.64 | 46.2 | keep collecting (13/30) |
| money_level+sharp_gap | both | 4-6 | 40.0 | 56.4 | -16.4 | -3.33 | -33.3 | 0.42 | 50.0 | keep collecting (10/30) |
| follow_move+money_moving | both | 6-6 | 50.0 | 47.4 | 2.6 | +0.48 | 4.0 | 0.67 | 50.0 | keep collecting (12/30) |
| money_level+money_moving | both | 5-7 | 41.7 | 57.8 | -16.1 | -4.21 | -35.1 | 0.5 | 41.7 | keep collecting (12/30) |
| consensus_gap+money_level | both | 5-4 | 55.6 | 60.8 | -5.3 | -2.19 | -24.4 | 0.09 | 44.4 | keep collecting (9/30) |
| follow_move+rlm_quiet | both | 6-7 | 46.2 | 37.1 | 9.0 | +0.24 | 1.8 | 0.5 | 46.2 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 4-6 | 40.0 | 39.5 | 0.5 | -1.51 | -15.1 | 0.73 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | both | 4-4 | 50.0 | 37.6 | 12.4 | +0.49 | 6.1 | 0.04 | 37.5 | keep collecting (8/30) |
| rlm_quiet+sharp_gap | both | 4-4 | 50.0 | 37.6 | 12.4 | +0.49 | 6.1 | 0.04 | 37.5 | keep collecting (8/30) |
| rlm_ratio+sharp_gap | both | 4-6 | 40.0 | 39.5 | 0.5 | -1.51 | -15.1 | 0.73 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 3-4 | 42.9 | 53.3 | -10.4 | -2.29 | -32.8 | 1.01 | 71.4 | keep collecting (7/30) |
| money_moving+rlm_quiet | both | 5-1 | 83.3 | 37.6 | 45.7 | +5.37 | 89.4 | 1.1 | 66.7 | keep collecting (6/30) |
| money_moving+rlm_ratio | both | 4-3 | 57.1 | 40.6 | 16.5 | +1.49 | 21.2 | 1.66 | 71.4 | keep collecting (7/30) |
| money_moving+sharp_gap | both | 7-7 | 50.0 | 45.7 | 4.3 | +0.6 | 4.3 | 0.96 | 64.3 | keep collecting (14/30) |
| consensus_gap+money_moving | both | 3-1 | 75.0 | 57.3 | 17.7 | +0.26 | 6.5 | 0.07 | 25.0 | keep collecting (4/30) |
| consensus_gap+sharp_gap | both | 3-2 | 60.0 | 52.1 | 7.9 | +0.26 | 5.2 | 0.5 | 60.0 | keep collecting (5/30) |
| money_level+rlm_ratio | both | 0-2 | 0.0 | 47.1 | -47.1 | -2.0 | -100.0 | 3.5 | 100.0 | keep collecting (2/30) |
| follow_move+money_delta | both | 0-1 | 0.0 | 39.7 | -39.7 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_level | both | 0-1 | 0.0 | 39.7 | -39.7 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_moving | both | 0-1 | 0.0 | 39.7 | -39.7 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | both | 0-1 | 0.0 | 39.7 | -39.7 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | both | 0-1 | 0.0 | 39.7 | -39.7 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| follow_move+pin_value | both | 1-0 | 100.0 | 39.7 | 60.3 | +0.91 | 90.9 | -2.0 | 0.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 2-6 | 25.0 | 35.5 | -10.5 | -2.36 | -29.5 | 0.31 | 37.5 | keep collecting (8/30) |
| rlm_quiet | total | 4-1 | 80.0 | 39.7 | 40.3 | +2.6 | 51.9 | 0.8 | 60.0 | keep collecting (5/30) |
| money_delta | total | 0-1 | 0.0 | 39.7 | -39.7 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| follow_move | moneyline | 15-12 | 55.6 | 47.3 | 8.2 | +4.15 | 15.4 | -0.54 | 29.6 | keep collecting (27/30) |
| follow_move | spread | 7-17 | 29.2 | 51.5 | -22.3 | -10.56 | -44.0 | -0.25 | 20.8 | keep collecting (24/30) |
| follow_move | total | 15-19 | 44.1 | 45.2 | -1.0 | -5.32 | -15.6 | 1.38 | 58.8 | no edge shown yet |
| rlm_ratio | moneyline | 1-3 | 25.0 | 35.5 | -10.5 | -1.24 | -31.0 | 0.33 | 25.0 | keep collecting (4/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| rlm_ratio | total | 3-2 | 60.0 | 39.7 | 20.3 | +0.73 | 14.5 | 0.2 | 60.0 | keep collecting (5/30) |
| money_level | moneyline | 9-6 | 60.0 | 62.6 | -2.6 | -2.27 | -15.2 | -0.35 | 26.7 | keep collecting (15/30) |
| money_level | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level | total | 4-8 | 33.3 | 58.6 | -25.2 | -4.36 | -36.4 | 0.08 | 41.7 | keep collecting (12/30) |
| sharp_gap | moneyline | 6-6 | 50.0 | 42.7 | 7.3 | +0.4 | 3.4 | 0.77 | 58.3 | keep collecting (12/30) |
| sharp_gap | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| sharp_gap | total | 5-6 | 45.5 | 47.2 | -1.7 | -1.45 | -13.2 | -0.27 | 36.4 | keep collecting (11/30) |
| money_moving | moneyline | 7-4 | 63.6 | 48.7 | 15.0 | +3.28 | 29.8 | 0.64 | 54.5 | keep collecting (11/30) |
| money_moving | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving | total | 5-5 | 50.0 | 47.9 | 2.1 | -0.45 | -4.5 | 0.1 | 40.0 | keep collecting (10/30) |
| pin_value | spread | 1-1 | 50.0 | 45.6 | 4.4 | -0.13 | -6.5 | 0.5 | 50.0 | keep collecting (2/30) |
| pin_value | total | 1-0 | 100.0 | 39.7 | 60.3 | +0.91 | 90.9 | -2.0 | 0.0 | keep collecting (1/30) |
| consensus_gap | moneyline | 10-10 | 50.0 | 54.4 | -4.4 | -2.58 | -12.9 | -0.45 | 40.0 | keep collecting (20/30) |
| consensus_gap | spread | 6-2 | 75.0 | 47.8 | 27.2 | +3.23 | 40.4 | 0.5 | 37.5 | keep collecting (8/30) |
| consensus_gap | total | 8-8 | 50.0 | 50.0 | -0.0 | -0.81 | -5.0 | 1.06 | 62.5 | keep collecting (16/30) |
| consensus_gap+money_level | moneyline | 5-3 | 62.5 | 60.9 | 1.6 | -1.19 | -14.9 | -0.15 | 37.5 | keep collecting (8/30) |
| follow_move+rlm_quiet | moneyline | 2-6 | 25.0 | 35.5 | -10.5 | -2.36 | -29.5 | 0.31 | 37.5 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 1-3 | 25.0 | 35.5 | -10.5 | -1.24 | -31.0 | 0.33 | 25.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 1-3 | 25.0 | 35.5 | -10.5 | -1.24 | -31.0 | 0.33 | 25.0 | keep collecting (4/30) |
| rlm_quiet+rlm_ratio | moneyline | 1-3 | 25.0 | 35.5 | -10.5 | -1.24 | -31.0 | 0.33 | 25.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | moneyline | 1-3 | 25.0 | 35.5 | -10.5 | -1.24 | -31.0 | 0.33 | 25.0 | keep collecting (4/30) |
| rlm_ratio+sharp_gap | moneyline | 1-3 | 25.0 | 35.5 | -10.5 | -1.24 | -31.0 | 0.33 | 25.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 2-1 | 66.7 | 64.5 | 2.2 | -0.2 | -6.8 | -0.63 | 33.3 | keep collecting (3/30) |
| consensus_gap+money_moving | moneyline | 3-1 | 75.0 | 57.3 | 17.7 | +0.26 | 6.5 | 0.07 | 25.0 | keep collecting (4/30) |
| consensus_gap+sharp_gap | moneyline | 3-1 | 75.0 | 50.0 | 25.0 | +1.26 | 31.4 | 0.12 | 50.0 | keep collecting (4/30) |
| money_level+money_moving | moneyline | 4-2 | 66.7 | 59.7 | 7.0 | -0.12 | -1.9 | 0.17 | 33.3 | keep collecting (6/30) |
| money_level+sharp_gap | moneyline | 3-1 | 75.0 | 57.3 | 17.7 | +0.76 | 19.1 | 0.3 | 50.0 | keep collecting (4/30) |
| money_moving+sharp_gap | moneyline | 4-3 | 57.1 | 43.8 | 13.4 | +1.88 | 26.8 | 1.36 | 71.4 | keep collecting (7/30) |
| follow_move+money_level | moneyline | 1-2 | 33.3 | 64.5 | -31.2 | -1.89 | -63.0 | -1.67 | 0.0 | keep collecting (3/30) |
| follow_move+money_moving | moneyline | 3-2 | 60.0 | 47.1 | 12.9 | +1.75 | 35.0 | -0.18 | 40.0 | keep collecting (5/30) |
| money_moving+rlm_quiet | moneyline | 2-1 | 66.7 | 35.5 | 31.2 | +2.64 | 88.0 | 1.2 | 66.7 | keep collecting (3/30) |
| money_moving+rlm_ratio | moneyline | 1-1 | 50.0 | 35.5 | 14.5 | +0.76 | 38.0 | 0.8 | 50.0 | keep collecting (2/30) |
| follow_move+money_level | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| follow_move+money_moving | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to sharp_gap alone, not independent confirmation |
| money_level+money_moving | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+rlm_ratio | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+sharp_gap | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| money_moving+sharp_gap | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | total | 1-4 | 20.0 | 56.2 | -36.2 | -3.09 | -61.8 | 0.6 | 40.0 | keep collecting (5/30) |
| follow_move+sharp_gap | total | 4-4 | 50.0 | 47.4 | 2.6 | -0.36 | -4.5 | 0.25 | 50.0 | keep collecting (8/30) |
| money_level+sharp_gap | total | 1-4 | 20.0 | 56.2 | -36.2 | -3.09 | -61.8 | -0.4 | 40.0 | keep collecting (5/30) |
| follow_move+money_moving | total | 3-3 | 50.0 | 46.6 | 3.4 | -0.27 | -4.5 | 0.67 | 50.0 | keep collecting (6/30) |
| money_level+money_moving | total | 1-4 | 20.0 | 56.2 | -36.2 | -3.09 | -61.8 | 0.0 | 40.0 | keep collecting (5/30) |
| follow_move+rlm_quiet | total | 4-1 | 80.0 | 39.7 | 40.3 | +2.6 | 51.9 | 0.8 | 60.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 3-2 | 60.0 | 39.7 | 20.3 | +0.73 | 14.5 | 0.2 | 60.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 3-1 | 75.0 | 39.7 | 35.3 | +1.73 | 43.2 | -0.25 | 50.0 | keep collecting (4/30) |
| rlm_quiet+sharp_gap | total | 3-1 | 75.0 | 39.7 | 35.3 | +1.73 | 43.2 | -0.25 | 50.0 | keep collecting (4/30) |
| rlm_ratio+sharp_gap | total | 3-2 | 60.0 | 39.7 | 20.3 | +0.73 | 14.5 | 0.2 | 60.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | total | 3-0 | 100.0 | 39.7 | 60.3 | +2.73 | 90.9 | 1.0 | 66.7 | keep collecting (3/30) |
| money_moving+rlm_ratio | total | 3-1 | 75.0 | 39.7 | 35.3 | +1.73 | 43.2 | 1.25 | 75.0 | keep collecting (4/30) |
| money_moving+sharp_gap | total | 3-3 | 50.0 | 46.6 | 3.4 | -0.27 | -4.5 | -0.17 | 50.0 | keep collecting (6/30) |
| consensus_gap+follow_move | total | 1-3 | 25.0 | 44.9 | -19.9 | -2.09 | -52.3 | 2.25 | 100.0 | keep collecting (4/30) |
| consensus_gap+money_level | total | 0-1 | 0.0 | 60.3 | -60.3 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+sharp_gap | total | 0-1 | 0.0 | 60.3 | -60.3 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | total | 0-1 | 0.0 | 39.7 | -39.7 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_level | total | 0-1 | 0.0 | 39.7 | -39.7 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_moving | total | 0-1 | 0.0 | 39.7 | -39.7 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | total | 0-1 | 0.0 | 39.7 | -39.7 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | total | 0-1 | 0.0 | 39.7 | -39.7 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+rlm_ratio | total | 0-1 | 0.0 | 39.7 | -39.7 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| follow_move+pin_value | total | 1-0 | 100.0 | 39.7 | 60.3 | +0.91 | 90.9 | -2.0 | 0.0 | redundant -- identical record to pin_value alone, not independent confirmation |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 22-47 | 31.9 | 40.3 | -8.4 | -13.05 | -18.9 |  |  | DROP: below break-even |
| pin_move | both | 42-51 | 45.2 | 48.7 | -3.5 | -13.07 | -14.1 |  |  | no edge shown yet |
| money_delta | both | 25-29 | 46.3 | 40.0 | 6.3 | +0.07 | 0.1 |  |  | no edge shown yet |
| pin_rlm | both | 7-13 | 35.0 | 39.7 | -4.7 | -5.92 | -29.6 |  |  | keep collecting (20/30) |
| follow_move | both | 70-95 | 42.4 | 48.7 | -6.3 | -24.92 | -15.1 |  |  | DROP: below break-even |
| rlm_ratio | both | 14-30 | 31.8 | 39.9 | -8.0 | -16.55 | -37.6 |  |  | DROP: below break-even |
| money_level | both | 95-66 | 59.0 | 57.2 | 1.9 | +2.34 | 1.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 60-84 | 41.7 | 47.9 | -6.2 | -27.64 | -19.2 |  |  | DROP: below break-even |
| money_moving | both | 64-83 | 43.5 | 48.6 | -5.1 | -25.08 | -17.1 |  |  | DROP: below break-even |
| pin_value | both | 42-26 | 61.8 | 51.6 | 10.1 | +26.46 | 38.9 |  |  | PROMOTE: beats break-even and its own base rate |
| consensus_gap | both | 39-26 | 60.0 | 53.6 | 6.4 | +5.74 | 8.8 |  |  | no edge shown yet |
| follow_move+pin_move | both | 30-43 | 41.1 | 47.9 | -6.8 | -15.35 | -21.0 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 20-21 | 48.8 | 39.3 | 9.5 | +3.37 | 8.2 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 20-20 | 50.0 | 39.3 | 10.7 | +4.37 | 10.9 |  |  | no edge shown yet |
| money_moving+sharp_gap | both | 59-81 | 42.1 | 48.1 | -5.9 | -25.55 | -18.3 |  |  | DROP: below break-even |
| consensus_gap+money_level | both | 28-12 | 70.0 | 60.3 | 9.7 | +6.43 | 16.1 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+rlm_quiet | both | 22-47 | 31.9 | 40.3 | -8.4 | -13.05 | -18.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | both | 12-20 | 37.5 | 40.9 | -3.4 | -6.77 | -21.2 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 14-11 | 56.0 | 52.9 | 3.1 | -1.0 | -4.0 |  |  | keep collecting (25/30) |
| follow_move+money_level | both | 34-29 | 54.0 | 57.2 | -3.2 | -5.94 | -9.4 |  |  | no edge shown yet |
| money_level+money_moving | both | 46-43 | 51.7 | 54.3 | -2.6 | -7.53 | -8.5 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 42-42 | 50.0 | 53.8 | -3.8 | -8.09 | -9.6 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 13-16 | 44.8 | 52.1 | -7.3 | -2.99 | -10.3 |  |  | keep collecting (29/30) |
| consensus_gap+pin_move | both | 7-5 | 58.3 | 52.4 | 5.9 | +0.17 | 1.4 |  |  | keep collecting (12/30) |
| consensus_gap+pin_value | both | 16-9 | 64.0 | 50.8 | 13.2 | +8.64 | 34.6 |  |  | keep collecting (25/30) |
| consensus_gap+sharp_gap | both | 12-16 | 42.9 | 50.8 | -7.9 | -3.13 | -11.2 |  |  | keep collecting (28/30) |
| follow_move+money_moving | both | 29-45 | 39.2 | 47.6 | -8.4 | -21.91 | -29.6 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 11-8 | 57.9 | 52.6 | 5.3 | +11.52 | 60.6 |  |  | keep collecting (19/30) |
| follow_move+sharp_gap | both | 30-47 | 39.0 | 47.1 | -8.2 | -23.0 | -29.9 |  |  | DROP: below break-even |
| money_level+pin_move | both | 19-20 | 48.7 | 54.7 | -6.0 | -5.16 | -13.2 |  |  | no edge shown yet |
| money_level+pin_value | both | 16-13 | 55.2 | 56.1 | -0.9 | +1.29 | 4.4 |  |  | keep collecting (29/30) |
| money_moving+pin_move | both | 14-23 | 37.8 | 47.3 | -9.4 | -10.49 | -28.4 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 11-15 | 42.3 | 51.1 | -8.8 | -1.6 | -6.1 |  |  | keep collecting (26/30) |
| pin_move+pin_value | both | 11-10 | 52.4 | 52.4 | 0.0 | -0.3 | -1.4 |  |  | keep collecting (21/30) |
| pin_move+sharp_gap | both | 12-25 | 32.4 | 45.9 | -13.5 | -14.27 | -38.6 |  |  | DROP: below break-even |
| pin_value+sharp_gap | both | 10-14 | 41.7 | 50.3 | -8.6 | -1.51 | -6.3 |  |  | keep collecting (24/30) |
| follow_move+money_delta | both | 13-22 | 37.1 | 40.4 | -3.2 | -9.82 | -28.1 |  |  | DROP: below break-even |
| money_delta+pin_move | both | 7-10 | 41.2 | 38.7 | 2.5 | -3.26 | -19.2 |  |  | keep collecting (17/30) |
| money_delta+rlm_quiet | both | 7-16 | 30.4 | 39.2 | -8.8 | -9.42 | -40.9 |  |  | keep collecting (23/30) |
| follow_move+rlm_ratio | both | 14-30 | 31.8 | 39.9 | -8.0 | -16.55 | -37.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | both | 7-22 | 24.1 | 38.6 | -14.5 | -15.05 | -51.9 |  |  | keep collecting (29/30) |
| money_moving+rlm_ratio | both | 14-28 | 33.3 | 40.1 | -6.7 | -14.55 | -34.6 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 5-22 | 18.5 | 38.4 | -19.9 | -17.32 | -64.2 |  |  | keep collecting (27/30) |
| rlm_quiet+sharp_gap | both | 7-25 | 21.9 | 38.3 | -16.4 | -18.05 | -56.4 |  |  | INVERT candidate: wrong well beyond its base rate |
| rlm_ratio+sharp_gap | both | 14-30 | 31.8 | 39.9 | -8.0 | -16.55 | -37.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | both | 7-4 | 63.6 | 41.0 | 22.7 | +3.35 | 30.5 |  |  | keep collecting (11/30) |
| consensus_gap+rlm_quiet | both | 3-6 | 33.3 | 38.5 | -5.2 | -3.18 | -35.4 |  |  | keep collecting (9/30) |
| consensus_gap+rlm_ratio | both | 3-4 | 42.9 | 36.7 | 6.2 | -1.2 | -17.1 |  |  | keep collecting (7/30) |
| money_delta+rlm_ratio | both | 11-16 | 40.7 | 40.0 | 0.7 | -5.73 | -21.2 |  |  | keep collecting (27/30) |
| consensus_gap+pin_rlm | both | 1-2 | 33.3 | 46.6 | -13.2 | -1.0 | -33.3 |  |  | keep collecting (3/30) |
| money_level+pin_rlm | both | 3-5 | 37.5 | 41.8 | -4.3 | -2.12 | -26.5 |  |  | keep collecting (8/30) |
| money_moving+pin_rlm | both | 7-12 | 36.8 | 39.9 | -3.1 | -4.92 | -25.9 |  |  | keep collecting (19/30) |
| pin_rlm+sharp_gap | both | 7-13 | 35.0 | 39.7 | -4.7 | -5.92 | -29.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | both | 7-6 | 53.8 | 41.6 | 12.3 | +0.56 | 4.3 |  |  | keep collecting (13/30) |
| consensus_gap+money_delta | both | 4-2 | 66.7 | 36.9 | 29.8 | +5.3 | 88.4 |  |  | keep collecting (6/30) |
| follow_move+pin_rlm | both | 7-11 | 38.9 | 38.3 | 0.6 | -3.92 | -21.8 |  |  | keep collecting (18/30) |
| money_delta+pin_rlm | both | 5-7 | 41.7 | 38.3 | 3.4 | -2.17 | -18.1 |  |  | keep collecting (12/30) |
| pin_move+pin_rlm | both | 6-12 | 33.3 | 38.5 | -5.2 | -6.26 | -34.8 |  |  | keep collecting (18/30) |
| pin_move+rlm_ratio | both | 6-11 | 35.3 | 38.5 | -3.2 | -5.26 | -30.9 |  |  | keep collecting (17/30) |
| pin_rlm+rlm_quiet | both | 3-6 | 33.3 | 38.8 | -5.4 | -3.14 | -34.9 |  |  | keep collecting (9/30) |
| pin_rlm+rlm_ratio | both | 7-11 | 38.9 | 38.3 | 0.6 | -3.92 | -21.8 |  |  | keep collecting (18/30) |
| money_delta+pin_value | both | 5-2 | 71.4 | 42.0 | 29.4 | +6.1 | 87.1 |  |  | keep collecting (7/30) |
| pin_value+rlm_quiet | both | 4-2 | 66.7 | 41.5 | 25.2 | +11.33 | 188.8 |  |  | keep collecting (6/30) |
| pin_value+rlm_ratio | both | 3-0 | 100.0 | 46.6 | 53.4 | +2.69 | 89.6 |  |  | keep collecting (3/30) |
| pin_rlm+pin_value | both | 1-1 | 50.0 | 39.7 | 10.3 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| rlm_quiet | moneyline | 8-17 | 32.0 | 35.5 | -3.5 | +3.88 | 15.5 |  |  | keep collecting (25/30) |
| rlm_quiet | spread | 3-6 | 33.3 | 53.4 | -20.1 | -3.19 | -35.4 |  |  | keep collecting (9/30) |
| rlm_quiet | total | 11-24 | 31.4 | 40.3 | -8.9 | -13.74 | -39.3 |  |  | DROP: below break-even |
| pin_move | moneyline | 12-11 | 52.2 | 48.1 | 4.1 | -0.44 | -1.9 |  |  | keep collecting (23/30) |
| pin_move | spread | 15-17 | 46.9 | 51.4 | -4.5 | -3.53 | -11.0 |  |  | no edge shown yet |
| pin_move | total | 15-23 | 39.5 | 46.7 | -7.3 | -9.1 | -24.0 |  |  | DROP: below break-even |
| money_delta | moneyline | 8-10 | 44.4 | 35.5 | 9.0 | +3.39 | 18.8 |  |  | keep collecting (18/30) |
| money_delta | spread | 3-3 | 50.0 | 48.5 | 1.5 | -0.2 | -3.4 |  |  | keep collecting (6/30) |
| money_delta | total | 14-16 | 46.7 | 41.1 | 5.6 | -3.11 | -10.4 |  |  | no edge shown yet |
| pin_rlm | moneyline | 3-4 | 42.9 | 39.6 | 3.2 | -0.64 | -9.1 |  |  | keep collecting (7/30) |
| pin_rlm | total | 4-9 | 30.8 | 39.7 | -8.9 | -5.28 | -40.6 |  |  | keep collecting (13/30) |
| follow_move | moneyline | 29-29 | 50.0 | 48.5 | 1.5 | +3.43 | 5.9 |  |  | no edge shown yet |
| follow_move | spread | 15-28 | 34.9 | 51.3 | -16.5 | -14.28 | -33.2 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move | total | 26-38 | 40.6 | 47.1 | -6.5 | -14.07 | -22.0 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 4-14 | 22.2 | 35.5 | -13.3 | -9.71 | -54.0 |  |  | keep collecting (18/30) |
| rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| rlm_ratio | total | 10-14 | 41.7 | 42.3 | -0.6 | -4.84 | -20.2 |  |  | keep collecting (24/30) |
| money_level | moneyline | 41-21 | 66.1 | 61.2 | 4.9 | -1.44 | -2.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 15-16 | 48.4 | 48.7 | -0.3 | -2.54 | -8.2 |  |  | no edge shown yet |
| money_level | total | 39-29 | 57.4 | 57.3 | 0.1 | +6.32 | 9.3 |  |  | no edge shown yet |
| sharp_gap | moneyline | 25-29 | 46.3 | 45.7 | 0.6 | -4.39 | -8.1 |  |  | no edge shown yet |
| sharp_gap | spread | 11-20 | 35.5 | 48.7 | -13.2 | -10.22 | -33.0 |  |  | DROP: below break-even |
| sharp_gap | total | 24-35 | 40.7 | 49.5 | -8.8 | -13.04 | -22.1 |  |  | DROP: below break-even |
| money_moving | moneyline | 28-26 | 51.9 | 47.3 | 4.5 | -0.7 | -1.3 |  |  | no edge shown yet |
| money_moving | spread | 11-20 | 35.5 | 48.7 | -13.2 | -10.22 | -33.0 |  |  | DROP: below break-even |
| money_moving | total | 25-37 | 40.3 | 49.7 | -9.3 | -14.17 | -22.8 |  |  | DROP: below break-even |
| pin_value | moneyline | 4-1 | 80.0 | 47.1 | 32.9 | +18.09 | 361.7 |  |  | keep collecting (5/30) |
| pin_value | spread | 19-9 | 67.9 | 49.7 | 18.2 | +7.32 | 26.1 |  |  | keep collecting (28/30) |
| pin_value | total | 19-16 | 54.3 | 53.8 | 0.5 | +1.05 | 3.0 |  |  | no edge shown yet |
| consensus_gap | moneyline | 18-14 | 56.2 | 55.4 | 0.8 | -0.68 | -2.1 |  |  | no edge shown yet |
| consensus_gap | spread | 9-4 | 69.2 | 48.3 | 20.9 | +3.69 | 28.4 |  |  | keep collecting (13/30) |
| consensus_gap | total | 12-8 | 60.0 | 54.1 | 5.9 | +2.73 | 13.7 |  |  | keep collecting (20/30) |
| consensus_gap+money_level | moneyline | 15-5 | 75.0 | 64.5 | 10.5 | +1.93 | 9.7 |  |  | keep collecting (20/30) |
| follow_move+pin_move | moneyline | 11-11 | 50.0 | 47.4 | 2.6 | -0.85 | -3.9 |  |  | keep collecting (22/30) |
| follow_move+rlm_quiet | moneyline | 8-17 | 32.0 | 35.5 | -3.5 | +3.88 | 15.5 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | moneyline | 4-6 | 40.0 | 35.5 | 4.5 | -0.26 | -2.6 |  |  | keep collecting (10/30) |
| consensus_gap+follow_move | moneyline | 9-6 | 60.0 | 52.9 | 7.1 | -0.49 | -3.3 |  |  | keep collecting (15/30) |
| follow_move+money_level | moneyline | 19-10 | 65.5 | 60.5 | 5.0 | -0.7 | -2.4 |  |  | keep collecting (29/30) |
| money_moving+sharp_gap | moneyline | 25-26 | 49.0 | 46.3 | 2.7 | -1.39 | -2.7 |  |  | no edge shown yet |
| follow_move+money_moving | moneyline | 14-13 | 51.9 | 46.2 | 5.6 | -3.62 | -13.4 |  |  | keep collecting (27/30) |
| follow_move+sharp_gap | moneyline | 14-16 | 46.7 | 45.2 | 1.5 | -6.62 | -22.1 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 20-9 | 69.0 | 57.5 | 11.5 | +2.99 | 10.3 |  |  | keep collecting (29/30) |
| money_level+sharp_gap | moneyline | 17-9 | 65.4 | 56.7 | 8.7 | +2.3 | 8.9 |  |  | keep collecting (26/30) |
| follow_move+rlm_ratio | moneyline | 4-14 | 22.2 | 35.5 | -13.3 | -9.71 | -54.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | moneyline | 2-9 | 18.2 | 35.5 | -17.3 | -6.68 | -60.7 |  |  | keep collecting (11/30) |
| money_moving+rlm_ratio | moneyline | 4-12 | 25.0 | 35.5 | -10.5 | -7.71 | -48.2 |  |  | keep collecting (16/30) |
| rlm_quiet+rlm_ratio | moneyline | 1-11 | 8.3 | 35.5 | -27.2 | -10.0 | -83.3 |  |  | keep collecting (12/30) |
| rlm_quiet+sharp_gap | moneyline | 2-12 | 14.3 | 35.5 | -21.2 | -9.68 | -69.1 |  |  | keep collecting (14/30) |
| rlm_ratio+sharp_gap | moneyline | 4-14 | 22.2 | 35.5 | -13.3 | -9.71 | -54.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 7-8 | 46.7 | 52.9 | -6.2 | -0.36 | -2.4 |  |  | keep collecting (15/30) |
| consensus_gap+rlm_quiet | moneyline | 1-5 | 16.7 | 35.5 | -18.8 | -4.0 | -66.7 |  |  | keep collecting (6/30) |
| consensus_gap+rlm_ratio | moneyline | 1-4 | 20.0 | 35.5 | -15.5 | -3.0 | -60.0 |  |  | keep collecting (5/30) |
| consensus_gap+sharp_gap | moneyline | 6-9 | 40.0 | 51.0 | -11.0 | -1.5 | -10.0 |  |  | keep collecting (15/30) |
| consensus_gap+pin_rlm | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | +0.0 | 0.0 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | moneyline | 1-2 | 33.3 | 45.2 | -11.8 | -0.98 | -32.7 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | moneyline | 3-3 | 50.0 | 40.3 | 9.7 | +0.36 | 6.0 |  |  | keep collecting (6/30) |
| pin_rlm+sharp_gap | moneyline | 3-4 | 42.9 | 39.6 | 3.2 | -0.64 | -9.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +5.38 | 269.2 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | moneyline | 2-2 | 50.0 | 35.5 | 14.5 | -0.05 | -1.3 |  |  | keep collecting (4/30) |
| consensus_gap+pin_move | moneyline | 5-1 | 83.3 | 54.8 | 28.5 | +2.43 | 40.5 |  |  | keep collecting (6/30) |
| money_level+pin_move | moneyline | 8-4 | 66.7 | 59.7 | 7.0 | +0.82 | 6.8 |  |  | keep collecting (12/30) |
| consensus_gap+money_delta | moneyline | 2-2 | 50.0 | 35.5 | 14.5 | +3.5 | 87.5 |  |  | keep collecting (4/30) |
| follow_move+money_delta | moneyline | 2-7 | 22.2 | 35.5 | -13.3 | -4.98 | -55.3 |  |  | keep collecting (9/30) |
| follow_move+pin_rlm | moneyline | 3-3 | 50.0 | 35.5 | 14.5 | +0.36 | 6.0 |  |  | keep collecting (6/30) |
| money_delta+money_moving | moneyline | 8-10 | 44.4 | 35.5 | 9.0 | +3.39 | 18.8 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_move | moneyline | 2-2 | 50.0 | 35.5 | 14.5 | +0.02 | 0.5 |  |  | keep collecting (4/30) |
| money_delta+pin_rlm | moneyline | 2-2 | 50.0 | 35.5 | 14.5 | +0.02 | 0.5 |  |  | keep collecting (4/30) |
| money_delta+rlm_quiet | moneyline | 1-5 | 16.7 | 35.5 | -18.8 | -4.0 | -66.7 |  |  | keep collecting (6/30) |
| money_delta+rlm_ratio | moneyline | 2-7 | 22.2 | 35.5 | -13.3 | -4.98 | -55.3 |  |  | keep collecting (9/30) |
| money_delta+sharp_gap | moneyline | 8-10 | 44.4 | 35.5 | 9.0 | +3.39 | 18.8 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| money_moving+pin_move | moneyline | 4-2 | 66.7 | 45.2 | 21.5 | +1.4 | 23.4 |  |  | keep collecting (6/30) |
| pin_move+pin_rlm | moneyline | 2-3 | 40.0 | 35.5 | 4.5 | -0.98 | -19.6 |  |  | keep collecting (5/30) |
| pin_move+rlm_ratio | moneyline | 2-3 | 40.0 | 35.5 | 4.5 | -0.98 | -19.6 |  |  | keep collecting (5/30) |
| pin_move+sharp_gap | moneyline | 4-4 | 50.0 | 42.7 | 7.3 | -0.6 | -7.5 |  |  | keep collecting (8/30) |
| pin_rlm+rlm_quiet | moneyline | 1-1 | 50.0 | 35.5 | 14.5 | +0.0 | 0.0 |  |  | keep collecting (2/30) |
| pin_rlm+rlm_ratio | moneyline | 3-3 | 50.0 | 35.5 | 14.5 | +0.36 | 6.0 |  |  | keep collecting (6/30) |
| follow_move+pin_value | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | +9.6 | 480.0 |  |  | keep collecting (2/30) |
| pin_value+rlm_quiet | moneyline | 1-0 | 100.0 | 35.5 | 64.5 | +10.6 | 1060.0 |  |  | keep collecting (1/30) |
| money_delta+money_level | moneyline | 2-1 | 66.7 | 35.5 | 31.2 | +1.74 | 58.0 |  |  | keep collecting (3/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 64.5 | -64.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_move+pin_value | moneyline | 0-1 | 0.0 | 64.5 | -64.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta+pin_value | moneyline | 1-0 | 100.0 | 35.5 | 64.5 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 1-0 | 100.0 | 35.5 | 64.5 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 1-0 | 100.0 | 35.5 | 64.5 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| follow_move+pin_move | spread | 7-13 | 35.0 | 51.8 | -16.8 | -6.71 | -33.6 |  |  | keep collecting (20/30) |
| money_moving+sharp_gap | spread | 11-20 | 35.5 | 48.7 | -13.2 | -10.22 | -33.0 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 3-6 | 33.3 | 53.4 | -20.1 | -3.19 | -35.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | spread | 8-14 | 36.4 | 48.0 | -11.6 | -6.95 | -31.6 |  |  | keep collecting (22/30) |
| money_level+sharp_gap | spread | 8-14 | 36.4 | 48.0 | -11.6 | -6.95 | -31.6 |  |  | keep collecting (22/30) |
| pin_move+rlm_quiet | spread | 1-3 | 25.0 | 54.4 | -29.4 | -2.09 | -52.3 |  |  | keep collecting (4/30) |
| consensus_gap+pin_value | spread | 7-4 | 63.6 | 48.0 | 15.6 | +2.01 | 18.3 |  |  | keep collecting (11/30) |
| follow_move+money_level | spread | 2-5 | 28.6 | 51.9 | -23.3 | -3.13 | -44.7 |  |  | keep collecting (7/30) |
| follow_move+money_moving | spread | 1-7 | 12.5 | 52.2 | -39.7 | -6.09 | -76.1 |  |  | keep collecting (8/30) |
| follow_move+sharp_gap | spread | 1-7 | 12.5 | 52.2 | -39.7 | -6.09 | -76.1 |  |  | keep collecting (8/30) |
| money_level+pin_move | spread | 3-6 | 33.3 | 50.5 | -17.2 | -3.3 | -36.6 |  |  | keep collecting (9/30) |
| money_moving+pin_move | spread | 2-6 | 25.0 | 50.0 | -25.0 | -4.26 | -53.2 |  |  | keep collecting (8/30) |
| pin_move+sharp_gap | spread | 2-6 | 25.0 | 50.0 | -25.0 | -4.26 | -53.2 |  |  | keep collecting (8/30) |
| money_delta+money_level | spread | 1-0 | 100.0 | 45.6 | 54.4 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+money_moving | spread | 2-1 | 66.7 | 45.6 | 21.1 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| money_delta+sharp_gap | spread | 2-1 | 66.7 | 45.6 | 21.1 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| consensus_gap+money_level | spread | 3-2 | 60.0 | 47.4 | 12.6 | +0.59 | 11.7 |  |  | keep collecting (5/30) |
| consensus_gap+money_moving | spread | 1-2 | 33.3 | 45.6 | -12.3 | -1.12 | -37.4 |  |  | keep collecting (3/30) |
| consensus_gap+sharp_gap | spread | 1-2 | 33.3 | 45.6 | -12.3 | -1.12 | -37.4 |  |  | keep collecting (3/30) |
| money_level+pin_value | spread | 4-3 | 57.1 | 48.1 | 9.0 | +0.5 | 7.1 |  |  | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-5 | 37.5 | 48.9 | -11.4 | -2.38 | -29.8 |  |  | keep collecting (8/30) |
| pin_value+sharp_gap | spread | 3-5 | 37.5 | 48.9 | -11.4 | -2.38 | -29.8 |  |  | keep collecting (8/30) |
| follow_move+money_delta | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| follow_move+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | spread | 0-1 | 0.0 | 45.6 | -45.6 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 5-1 | 83.3 | 52.9 | 30.4 | +3.41 | 56.8 |  |  | keep collecting (6/30) |
| pin_move+pin_value | spread | 8-3 | 72.7 | 50.4 | 22.3 | +3.93 | 35.7 |  |  | keep collecting (11/30) |
| consensus_gap+pin_move | spread | 2-2 | 50.0 | 50.0 | 0.0 | -0.26 | -6.5 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 1-1 | 50.0 | 54.4 | -4.4 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 54.4 | 45.6 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| pin_value+rlm_quiet | spread | 1-0 | 100.0 | 54.4 | 45.6 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+rlm_quiet | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_quiet+rlm_ratio | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_quiet+sharp_gap | spread | 0-1 | 0.0 | 54.4 | -54.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta+money_moving | total | 10-10 | 50.0 | 41.8 | 8.2 | -0.84 | -4.2 |  |  | keep collecting (20/30) |
| money_delta+sharp_gap | total | 10-9 | 52.6 | 41.9 | 10.8 | +0.16 | 0.9 |  |  | keep collecting (19/30) |
| money_moving+sharp_gap | total | 23-35 | 39.7 | 49.3 | -9.6 | -13.94 | -24.0 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | total | 11-24 | 31.4 | 40.3 | -8.9 | -13.74 | -39.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+follow_move | total | 4-4 | 50.0 | 52.6 | -2.6 | -0.42 | -5.2 |  |  | keep collecting (8/30) |
| consensus_gap+money_level | total | 10-5 | 66.7 | 58.9 | 7.7 | +3.92 | 26.1 |  |  | keep collecting (15/30) |
| consensus_gap+money_moving | total | 5-6 | 45.5 | 52.8 | -7.4 | -1.51 | -13.7 |  |  | keep collecting (11/30) |
| consensus_gap+pin_move | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+pin_value | total | 7-5 | 58.3 | 53.4 | 4.9 | +1.24 | 10.4 |  |  | keep collecting (12/30) |
| consensus_gap+sharp_gap | total | 5-5 | 50.0 | 52.1 | -2.1 | -0.51 | -5.1 |  |  | keep collecting (10/30) |
| follow_move+money_level | total | 13-14 | 48.1 | 55.0 | -6.8 | -2.11 | -7.8 |  |  | keep collecting (27/30) |
| follow_move+money_moving | total | 14-25 | 35.9 | 47.6 | -11.7 | -12.2 | -31.3 |  |  | DROP: below break-even |
| follow_move+pin_move | total | 12-19 | 38.7 | 45.7 | -7.0 | -7.79 | -25.1 |  |  | DROP: below break-even |
| follow_move+pin_value | total | 5-6 | 45.5 | 52.8 | -7.4 | -1.49 | -13.5 |  |  | keep collecting (11/30) |
| follow_move+sharp_gap | total | 15-24 | 38.5 | 47.6 | -9.2 | -10.29 | -26.4 |  |  | DROP: below break-even |
| money_level+money_moving | total | 18-20 | 47.4 | 55.4 | -8.0 | -3.58 | -9.4 |  |  | no edge shown yet |
| money_level+pin_move | total | 8-10 | 44.4 | 53.4 | -9.0 | -2.68 | -14.9 |  |  | keep collecting (18/30) |
| money_level+pin_value | total | 12-9 | 57.1 | 58.3 | -1.2 | +1.79 | 8.5 |  |  | keep collecting (21/30) |
| money_level+sharp_gap | total | 17-19 | 47.2 | 55.1 | -7.9 | -3.45 | -9.6 |  |  | no edge shown yet |
| money_moving+pin_move | total | 8-15 | 34.8 | 46.9 | -12.1 | -7.64 | -33.2 |  |  | keep collecting (23/30) |
| money_moving+pin_value | total | 7-10 | 41.2 | 53.0 | -11.9 | -3.72 | -21.9 |  |  | keep collecting (17/30) |
| pin_move+pin_value | total | 3-6 | 33.3 | 53.4 | -20.1 | -3.23 | -35.9 |  |  | keep collecting (9/30) |
| pin_move+sharp_gap | total | 6-15 | 28.6 | 45.6 | -17.0 | -9.42 | -44.8 |  |  | keep collecting (21/30) |
| pin_value+sharp_gap | total | 6-9 | 40.0 | 52.1 | -12.1 | -3.62 | -24.2 |  |  | keep collecting (15/30) |
| follow_move+money_delta | total | 11-13 | 45.8 | 41.4 | 4.4 | -2.84 | -11.8 |  |  | keep collecting (24/30) |
| money_delta+pin_move | total | 5-8 | 38.5 | 39.7 | -1.2 | -3.28 | -25.3 |  |  | keep collecting (13/30) |
| money_delta+rlm_quiet | total | 6-10 | 37.5 | 39.7 | -2.2 | -4.42 | -27.6 |  |  | keep collecting (16/30) |
| pin_move+rlm_quiet | total | 7-11 | 38.9 | 40.8 | -2.0 | -4.42 | -24.6 |  |  | keep collecting (18/30) |
| follow_move+rlm_ratio | total | 10-14 | 41.7 | 42.3 | -0.6 | -4.84 | -20.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | total | 9-8 | 52.9 | 42.1 | 10.8 | +0.25 | 1.5 |  |  | keep collecting (17/30) |
| money_moving+rlm_quiet | total | 5-12 | 29.4 | 39.7 | -10.3 | -7.37 | -43.3 |  |  | keep collecting (17/30) |
| money_moving+rlm_ratio | total | 10-14 | 41.7 | 42.3 | -0.6 | -4.84 | -20.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 4-10 | 28.6 | 39.7 | -11.1 | -6.32 | -45.1 |  |  | keep collecting (14/30) |
| rlm_quiet+sharp_gap | total | 5-12 | 29.4 | 39.7 | -10.3 | -7.37 | -43.3 |  |  | keep collecting (17/30) |
| rlm_ratio+sharp_gap | total | 10-14 | 41.7 | 42.3 | -0.6 | -4.84 | -20.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | total | 2-0 | 100.0 | 39.7 | 60.3 | +1.8 | 90.1 |  |  | keep collecting (2/30) |
| consensus_gap+rlm_quiet | total | 1-1 | 50.0 | 39.7 | 10.3 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| consensus_gap+rlm_ratio | total | 2-0 | 100.0 | 39.7 | 60.3 | +1.8 | 90.1 |  |  | keep collecting (2/30) |
| money_delta+pin_value | total | 4-2 | 66.7 | 43.1 | 23.5 | +1.6 | 26.6 |  |  | keep collecting (6/30) |
| pin_value+rlm_quiet | total | 2-2 | 50.0 | 39.7 | 10.3 | -0.18 | -4.5 |  |  | keep collecting (4/30) |
| pin_value+rlm_ratio | total | 3-0 | 100.0 | 46.6 | 53.4 | +2.69 | 89.6 |  |  | keep collecting (3/30) |
| follow_move+pin_rlm | total | 4-8 | 33.3 | 39.7 | -6.4 | -4.28 | -35.7 |  |  | keep collecting (12/30) |
| money_delta+money_level | total | 4-3 | 57.1 | 42.6 | 14.5 | +0.71 | 10.1 |  |  | keep collecting (7/30) |
| money_delta+pin_rlm | total | 3-5 | 37.5 | 39.7 | -2.2 | -2.19 | -27.3 |  |  | keep collecting (8/30) |
| money_level+pin_rlm | total | 2-3 | 40.0 | 39.7 | 0.3 | -1.14 | -22.8 |  |  | keep collecting (5/30) |
| money_level+rlm_ratio | total | 5-4 | 55.6 | 44.3 | 11.3 | +0.62 | 6.8 |  |  | keep collecting (9/30) |
| money_moving+pin_rlm | total | 4-9 | 30.8 | 39.7 | -8.9 | -5.28 | -40.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | total | 4-9 | 30.8 | 39.7 | -8.9 | -5.28 | -40.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 4-8 | 33.3 | 39.7 | -6.4 | -4.28 | -35.7 |  |  | keep collecting (12/30) |
| pin_rlm+rlm_ratio | total | 4-8 | 33.3 | 39.7 | -6.4 | -4.28 | -35.7 |  |  | keep collecting (12/30) |
| pin_rlm+sharp_gap | total | 4-9 | 30.8 | 39.7 | -8.9 | -5.28 | -40.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | total | 2-5 | 28.6 | 39.7 | -11.1 | -3.14 | -44.8 |  |  | keep collecting (7/30) |
| consensus_gap+pin_rlm | total | 0-1 | 0.0 | 39.7 | -39.7 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+pin_value | total | 1-1 | 50.0 | 39.7 | 10.3 | -0.09 | -4.5 |  |  | keep collecting (2/30) |

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
| pin_value | both | 49-48 | 50.5 | 48.3 | 2.2 | -4.43 | -4.6 | 0.1 | 38.1 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.3 | -31.3 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 219-290 | 43.0 | 47.2 | -4.2 | -61.46 | -12.1 | 0.39 | 45.0 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | both | 32-28 | 53.3 | 63.6 | -10.3 | -9.71 | -16.2 | 0.33 | 48.3 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | both | 17-23 | 42.5 | 46.7 | -4.2 | -6.42 | -16.1 | 0.25 | 42.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_value | both | 19-28 | 40.4 | 46.5 | -6.1 | -11.54 | -24.5 | 0.39 | 48.9 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_quiet | both | 30-36 | 45.5 | 35.9 | 9.6 | +10.59 | 16.0 | 0.18 | 43.9 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 29-17 | 63.0 | 38.5 | 24.5 | +20.54 | 44.6 | 0.42 | 52.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 75-37 | 67.0 | 50.1 | 16.9 | +25.31 | 22.6 | 0.37 | 48.2 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 64-39 | 62.1 | 58.2 | 4.0 | +0.13 | 0.1 | -0.17 | 46.6 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 11-9 | 55.0 | 49.8 | 5.2 | +0.81 | 4.0 | 0.4 | 45.0 | keep collecting (20/30) |
| money_moving+pin_value | both | 8-5 | 61.5 | 49.9 | 11.7 | +2.04 | 15.7 | 0.31 | 38.5 | keep collecting (13/30) |
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
| follow_move+pin_value | both | 20-17 | 54.1 | 48.8 | 5.2 | +0.41 | 1.1 | -0.12 | 29.7 | HYPOTHESIS (in-sample) -- no edge shown yet |
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
| pin_value | spread | 24-20 | 54.5 | 49.5 | 5.0 | +1.16 | 2.6 | 0.25 | 38.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 23-22 | 51.1 | 50.0 | 1.1 | -1.28 | -2.9 | -0.02 | 35.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
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
| consensus_gap+pin_value | spread | 10-8 | 55.6 | 48.8 | 6.7 | +0.6 | 3.3 | 0.5 | 50.0 | keep collecting (18/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.3 | 8.7 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 48.9 | 13.6 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 10-5 | 66.7 | 48.7 | 17.9 | +4.12 | 27.5 | 0.93 | 66.7 | keep collecting (15/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 49.1 | -6.2 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
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
| money_moving+pin_value | total | 5-3 | 62.5 | 50.1 | 12.4 | +1.47 | 18.3 | 0.12 | 25.0 | keep collecting (8/30) |
| pin_value+sharp_gap | total | 11-6 | 64.7 | 50.1 | 14.7 | +3.92 | 23.1 | -0.06 | 29.4 | keep collecting (17/30) |
| follow_move+money_level | total | 22-19 | 53.7 | 49.9 | 3.8 | +0.94 | 2.3 | 0.15 | 39.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.9 | -3.3 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
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
| pin_move | both | 494-493 | 50.1 | 50.0 | 0.1 | -28.35 | -2.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | both | 316-422 | 42.8 | 44.0 | -1.2 | -57.17 | -7.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm | both | 140-157 | 47.1 | 42.2 | 4.9 | +31.28 | 10.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | both | 856-763 | 52.9 | 51.9 | 1.0 | -89.6 | -5.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | both | 200-225 | 47.1 | 44.6 | 2.5 | +1.15 | 0.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level | both | 1082-804 | 57.4 | 55.5 | 1.8 | -66.84 | -3.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 845-975 | 46.4 | 47.5 | -1.0 | -118.59 | -6.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | both | 846-975 | 46.5 | 47.8 | -1.3 | -126.2 | -6.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | both | 350-357 | 49.5 | 47.8 | 1.7 | +2.45 | 0.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 330-448 | 42.4 | 47.1 | -4.7 | -87.6 | -11.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+follow_move | both | 127-127 | 50.0 | 51.2 | -1.2 | -15.22 | -6.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | both | 147-241 | 37.9 | 44.3 | -6.4 | -31.8 | -8.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_move | both | 79-83 | 48.8 | 51.0 | -2.2 | +1.33 | 0.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | both | 23-39 | 37.1 | 37.2 | -0.1 | +10.03 | 16.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_value | both | 131-146 | 47.3 | 45.4 | 1.9 | +2.87 | 1.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | both | 25-43 | 36.8 | 39.7 | -2.9 | -1.66 | -2.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | both | 146-245 | 37.3 | 43.8 | -6.4 | -32.79 | -8.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_moving | both | 457-486 | 48.5 | 49.4 | -0.9 | -66.32 | -7.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_move | both | 355-351 | 50.3 | 50.3 | -0.0 | -29.59 | -4.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_rlm | both | 108-111 | 49.3 | 44.3 | 5.0 | +7.57 | 3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | both | 123-118 | 51.0 | 48.9 | 2.1 | -8.43 | -3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | both | 200-225 | 47.1 | 44.6 | 2.5 | +1.15 | 0.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 462-483 | 48.9 | 49.2 | -0.3 | -56.21 | -5.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_move | both | 297-324 | 47.8 | 48.7 | -0.9 | -22.76 | -3.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_rlm | both | 134-153 | 46.7 | 42.2 | 4.5 | +29.32 | 10.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_value | both | 154-183 | 45.7 | 47.1 | -1.4 | -14.73 | -4.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | both | 192-218 | 46.8 | 44.6 | 2.2 | +0.23 | 0.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+sharp_gap | both | 811-937 | 46.4 | 47.5 | -1.1 | -110.22 | -6.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_rlm | both | 129-130 | 49.8 | 44.3 | 5.5 | +25.5 | 9.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_value | both | 155-155 | 50.0 | 49.0 | 1.0 | -5.78 | -1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_ratio | both | 116-109 | 51.6 | 45.7 | 5.8 | +16.25 | 7.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | both | 304-325 | 48.3 | 48.6 | -0.3 | -17.52 | -2.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+pin_value | both | 40-41 | 49.4 | 45.6 | 3.8 | +12.58 | 15.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_ratio | both | 108-111 | 49.3 | 44.3 | 5.0 | +7.57 | 3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | both | 140-157 | 47.1 | 42.2 | 4.9 | +31.28 | 10.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 38-31 | 55.1 | 48.6 | 6.5 | +3.73 | 5.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | both | 156-185 | 45.7 | 47.0 | -1.3 | -14.93 | -4.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio+sharp_gap | both | 200-225 | 47.1 | 44.6 | 2.5 | +1.15 | 0.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 151-176 | 46.2 | 46.0 | 0.2 | -22.47 | -6.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+money_moving | both | 596-531 | 52.9 | 52.4 | 0.5 | -46.31 | -4.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | both | 587-522 | 52.9 | 52.2 | 0.8 | -38.85 | -3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | both | 564-401 | 58.4 | 56.6 | 1.9 | -44.59 | -4.6 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 95-81 | 54.0 | 48.4 | 5.5 | +10.68 | 6.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | both | 202-165 | 55.0 | 57.9 | -2.9 | -23.58 | -6.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | both | 292-267 | 52.2 | 53.1 | -0.9 | -27.63 | -4.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | both | 171-158 | 52.0 | 49.8 | 2.1 | -9.38 | -2.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_quiet | both | 19-47 | 28.8 | 36.2 | -7.4 | -9.07 | -13.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_quiet | both | 182-256 | 41.6 | 41.9 | -0.3 | -33.92 | -7.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 98-149 | 39.7 | 41.9 | -2.2 | -20.73 | -8.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_moving | both | 226-330 | 40.6 | 42.4 | -1.8 | -48.17 | -8.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_delta | both | 41-109 | 27.3 | 36.7 | -9.3 | -30.68 | -20.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_level | both | 117-111 | 51.3 | 46.9 | 4.4 | +11.59 | 5.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | both | 68-71 | 48.9 | 46.9 | 2.1 | -5.57 | -4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+sharp_gap | both | 223-325 | 40.7 | 42.5 | -1.8 | -46.34 | -8.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 79-122 | 39.3 | 40.4 | -1.1 | -11.64 | -5.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_quiet | both | 90-146 | 38.1 | 41.7 | -3.5 | -23.63 | -10.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+rlm_quiet | both | 49-87 | 36.0 | 42.8 | -6.7 | -30.79 | -22.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+rlm_quiet | both | 87-105 | 45.3 | 44.1 | 1.2 | -4.23 | -2.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_quiet | both | 42-62 | 40.4 | 40.8 | -0.4 | -8.48 | -8.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 118-135 | 46.6 | 46.4 | 0.3 | -5.93 | -2.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_rlm | both | 63-43 | 59.4 | 46.7 | 12.8 | +19.25 | 18.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_rlm | both | 82-94 | 46.6 | 42.2 | 4.4 | +12.43 | 7.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+rlm_ratio | both | 110-116 | 48.7 | 45.0 | 3.6 | -0.1 | -0.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+rlm_quiet | both | 24-35 | 40.7 | 47.2 | -6.5 | -12.58 | -21.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 50.3 | 49.7 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 52-110 | 32.1 | 27.5 | 4.6 | -7.46 | -4.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet | spread | 45-44 | 50.6 | 50.6 | -0.1 | -2.33 | -2.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_quiet | total | 85-102 | 45.5 | 50.1 | -4.7 | -24.13 | -12.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move | moneyline | 103-101 | 50.5 | 49.5 | 0.9 | +6.99 | 3.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move | spread | 193-205 | 48.5 | 50.1 | -1.6 | -29.13 | -7.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move | total | 198-187 | 51.4 | 50.1 | 1.4 | -6.21 | -1.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | moneyline | 49-165 | 22.9 | 28.2 | -5.3 | -43.92 | -20.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta | spread | 122-125 | 49.4 | 50.8 | -1.4 | -13.91 | -5.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | total | 145-132 | 52.3 | 50.2 | 2.2 | +0.66 | 0.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm | moneyline | 38-72 | 34.5 | 28.3 | 6.2 | +22.97 | 20.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm | spread | 25-22 | 53.2 | 50.9 | 2.3 | +0.79 | 1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm | total | 77-63 | 55.0 | 50.2 | 4.8 | +7.52 | 5.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
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
| pin_value | spread | 157-147 | 51.6 | 49.6 | 2.0 | -9.94 | -3.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 175-156 | 52.9 | 50.0 | 2.9 | +1.52 | 0.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
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
| consensus_gap+money_moving | moneyline | 55-153 | 26.4 | 39.9 | -13.4 | -23.75 | -11.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | moneyline | 245-79 | 75.6 | 70.5 | 5.1 | -11.75 | -3.6 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 101-109 | 48.1 | 48.2 | -0.1 | -12.65 | -6.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_moving | moneyline | 46-148 | 23.7 | 27.8 | -4.1 | -29.89 | -15.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+sharp_gap | moneyline | 44-147 | 23.0 | 27.9 | -4.8 | -31.08 | -16.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 53-158 | 25.1 | 38.8 | -13.7 | -26.63 | -12.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+sharp_gap | moneyline | 98-108 | 47.6 | 47.3 | 0.3 | -12.08 | -5.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_quiet | moneyline | 23-67 | 25.6 | 27.7 | -2.1 | -5.91 | -6.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 24-68 | 26.1 | 27.6 | -1.6 | -7.45 | -8.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_move | moneyline | 28-35 | 44.4 | 53.3 | -8.9 | +4.93 | 7.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 10-28 | 26.3 | 29.1 | -2.8 | +9.65 | 25.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 4-30 | 11.8 | 29.4 | -17.6 | -7.04 | -20.7 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 83-67 | 55.3 | 51.6 | 3.8 | +6.35 | 4.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_rlm | moneyline | 24-39 | 38.1 | 29.6 | 8.5 | +2.46 | 3.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 37-80 | 31.6 | 29.8 | 1.8 | -2.78 | -2.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 46-62 | 42.6 | 42.6 | -0.1 | +10.69 | 9.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_rlm | moneyline | 37-70 | 34.6 | 28.4 | 6.2 | +23.57 | 22.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 36-76 | 32.1 | 30.0 | 2.2 | -0.18 | -0.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_rlm | moneyline | 27-45 | 37.5 | 28.6 | 8.9 | +17.19 | 23.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 23-32 | 41.8 | 28.3 | 13.5 | +9.87 | 17.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 21-30 | 41.2 | 30.3 | 10.9 | +8.28 | 16.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+sharp_gap | moneyline | 46-63 | 42.2 | 42.1 | 0.1 | +9.51 | 8.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 14-32 | 30.4 | 28.7 | 1.8 | -4.18 | -9.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 24-39 | 38.1 | 29.6 | 8.5 | +2.46 | 3.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 38-72 | 34.5 | 28.3 | 6.2 | +22.97 | 20.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
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
| consensus_gap+pin_move | spread | 24-27 | 47.1 | 49.2 | -2.2 | -6.56 | -12.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 59-44 | 57.3 | 49.2 | 8.1 | +6.11 | 5.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_ratio | spread | 4-4 | 50.0 | 50.0 | 0.0 | -0.67 | -8.3 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | spread | 46-42 | 52.3 | 49.2 | 3.0 | -2.86 | -3.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | spread | 157-160 | 49.5 | 49.3 | 0.2 | -18.11 | -5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_move | spread | 122-135 | 47.5 | 49.9 | -2.4 | -23.93 | -9.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_rlm | spread | 19-18 | 51.4 | 50.6 | 0.7 | -0.65 | -1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | spread | 56-50 | 52.8 | 49.0 | 3.8 | -1.23 | -1.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | spread | 41-43 | 48.8 | 50.2 | -1.3 | -5.76 | -6.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 158-159 | 49.8 | 49.4 | 0.5 | -15.97 | -5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_move | spread | 116-123 | 48.5 | 49.8 | -1.3 | -17.83 | -7.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | spread | 23-22 | 51.1 | 50.8 | 0.3 | -1.04 | -2.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | spread | 78-79 | 49.7 | 49.3 | 0.4 | -11.66 | -7.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_ratio | spread | 39-42 | 48.1 | 50.1 | -1.9 | -6.69 | -8.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | spread | 315-305 | 50.8 | 49.6 | 1.2 | -20.93 | -3.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_rlm | spread | 25-22 | 53.2 | 50.9 | 2.3 | +0.79 | 1.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 72-79 | 47.7 | 49.7 | -2.0 | -15.54 | -10.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_ratio | spread | 22-24 | 47.8 | 50.5 | -2.6 | -3.94 | -8.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | spread | 119-123 | 49.2 | 49.8 | -0.7 | -15.1 | -6.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+pin_value | spread | 7-10 | 41.2 | 50.6 | -9.4 | -3.88 | -22.8 |  |  | keep collecting (17/30) |
| pin_rlm+rlm_ratio | spread | 19-18 | 51.4 | 50.6 | 0.7 | -0.65 | -1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | spread | 25-22 | 53.2 | 50.9 | 2.3 | +0.79 | 1.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 7-7 | 50.0 | 49.4 | 0.6 | -1.01 | -7.2 |  |  | keep collecting (14/30) |
| pin_value+sharp_gap | spread | 78-79 | 49.7 | 49.4 | 0.3 | -11.73 | -7.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | spread | 41-43 | 48.8 | 50.2 | -1.3 | -5.76 | -6.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 152-164 | 48.1 | 49.1 | -1.0 | -26.69 | -8.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+rlm_ratio | spread | 21-28 | 42.9 | 49.9 | -7.0 | -9.13 | -18.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | spread | 248-243 | 50.5 | 49.3 | 1.2 | -19.56 | -4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | spread | 56-46 | 54.9 | 48.9 | 6.0 | +1.89 | 1.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | spread | 247-244 | 50.3 | 49.3 | 1.0 | -21.47 | -4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | spread | 106-124 | 46.1 | 49.6 | -3.5 | -28.32 | -12.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_value | spread | 85-86 | 49.7 | 49.1 | 0.6 | -12.64 | -7.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_delta | spread | 14-14 | 50.0 | 50.5 | -0.5 | -2.09 | -7.5 |  |  | keep collecting (28/30) |
| follow_move+money_delta | spread | 38-47 | 44.7 | 50.2 | -5.5 | -12.62 | -14.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_level | spread | 40-40 | 50.0 | 50.1 | -0.1 | -3.96 | -4.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_moving | spread | 68-74 | 47.9 | 50.4 | -2.6 | -12.64 | -8.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | spread | 32-26 | 55.2 | 50.4 | 4.7 | +1.88 | 3.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+sharp_gap | spread | 67-72 | 48.2 | 50.4 | -2.2 | -11.62 | -8.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_quiet | spread | 45-44 | 50.6 | 50.6 | -0.1 | -2.33 | -2.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 14-4 | 77.8 | 50.7 | 27.1 | +8.78 | 48.8 |  |  | keep collecting (18/30) |
| rlm_quiet+sharp_gap | spread | 21-10 | 67.7 | 50.9 | 16.9 | +9.22 | 29.7 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+pin_rlm | spread | 14-10 | 58.3 | 50.4 | 8.0 | +2.58 | 10.7 |  |  | keep collecting (24/30) |
| money_delta+rlm_ratio | spread | 16-26 | 38.1 | 50.0 | -11.9 | -11.78 | -28.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 52.1 | 47.9 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_move | spread | 36-42 | 46.2 | 50.8 | -4.7 | -9.09 | -11.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_rlm | spread | 13-15 | 46.4 | 50.6 | -4.2 | -3.31 | -11.8 |  |  | keep collecting (28/30) |
| money_delta+rlm_quiet | spread | 14-17 | 45.2 | 51.0 | -5.9 | -4.07 | -13.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_quiet | spread | 20-10 | 66.7 | 50.8 | 15.8 | +8.27 | 27.6 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| pin_move+rlm_quiet | spread | 25-21 | 54.3 | 51.0 | 3.3 | +2.17 | 4.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-2 | 75.0 | 51.6 | 23.4 | +3.56 | 44.5 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_quiet | spread | 2-3 | 40.0 | 50.4 | -10.4 | -1.33 | -26.7 |  |  | keep collecting (5/30) |
| pin_value+rlm_quiet | spread | 4-4 | 50.0 | 48.9 | 1.1 | -0.52 | -6.5 |  |  | keep collecting (8/30) |
| follow_move+money_delta | total | 90-82 | 52.3 | 50.1 | 2.2 | +0.24 | 0.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | total | 204-204 | 50.0 | 50.0 | 0.0 | -18.14 | -4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | total | 203-198 | 50.6 | 50.0 | 0.6 | -12.98 | -3.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | total | 309-330 | 48.4 | 50.1 | -1.7 | -47.91 | -7.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | total | 51-54 | 48.6 | 49.8 | -1.2 | -8.7 | -8.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_move | total | 27-21 | 56.2 | 49.9 | 6.4 | +2.96 | 6.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_value | total | 59-57 | 50.9 | 49.8 | 1.0 | -4.63 | -4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | total | 199-217 | 47.8 | 50.1 | -2.2 | -35.56 | -8.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+sharp_gap | total | 206-216 | 48.8 | 50.1 | -1.2 | -28.16 | -6.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | total | 119-101 | 54.1 | 50.0 | 4.1 | +7.46 | 3.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | total | 81-70 | 53.6 | 49.9 | 3.8 | +2.58 | 1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_value | total | 77-67 | 53.5 | 50.0 | 3.5 | +2.49 | 1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_quiet | total | 85-102 | 45.5 | 50.1 | -4.7 | -24.13 | -12.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 135-139 | 49.3 | 50.1 | -0.8 | -15.62 | -5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_quiet+sharp_gap | total | 53-71 | 42.7 | 50.2 | -7.4 | -22.49 | -18.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_moving | total | 112-108 | 50.9 | 50.2 | 0.7 | -5.64 | -2.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | total | 167-158 | 51.4 | 50.0 | 1.4 | -6.16 | -1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 65-61 | 51.6 | 50.0 | 1.6 | -2.4 | -1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | total | 66-71 | 48.2 | 50.0 | -1.8 | -11.51 | -8.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | total | 68-71 | 48.9 | 50.0 | -1.1 | -9.65 | -6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
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
| money_delta+pin_move | total | 66-58 | 53.2 | 50.2 | 3.0 | +2.32 | 1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | total | 139-139 | 50.0 | 50.1 | -0.1 | -11.93 | -4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_move | total | 150-149 | 50.2 | 50.1 | 0.1 | -12.02 | -4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+rlm_quiet | total | 19-25 | 43.2 | 50.1 | -7.0 | -7.58 | -17.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | total | 10-8 | 55.6 | 50.0 | 5.6 | +0.87 | 4.8 |  |  | keep collecting (18/30) |
| consensus_gap+rlm_ratio | total | 17-9 | 65.4 | 49.9 | 15.5 | +6.04 | 23.2 |  |  | keep collecting (26/30) |
| follow_move+pin_rlm | total | 65-54 | 54.6 | 50.2 | 4.4 | +5.75 | 4.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | total | 122-102 | 54.5 | 50.2 | 4.3 | +9.69 | 4.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 38-24 | 61.3 | 50.2 | 11.1 | +10.91 | 17.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+rlm_ratio | total | 61-42 | 59.2 | 50.1 | 9.1 | +13.72 | 13.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | total | 74-61 | 54.8 | 50.2 | 4.6 | +6.79 | 5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_ratio | total | 117-100 | 53.9 | 50.2 | 3.8 | +7.11 | 3.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_rlm | total | 77-63 | 55.0 | 50.2 | 4.8 | +7.52 | 5.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 73-55 | 57.0 | 50.2 | 6.9 | +11.92 | 9.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+pin_value | total | 28-20 | 58.3 | 50.1 | 8.2 | +5.4 | 11.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_ratio | total | 65-54 | 54.6 | 50.2 | 4.4 | +5.75 | 4.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | total | 77-63 | 55.0 | 50.2 | 4.8 | +7.52 | 5.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 30-21 | 58.8 | 50.1 | 8.7 | +6.22 | 12.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | total | 122-102 | 54.5 | 50.2 | 4.3 | +9.69 | 4.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 47-35 | 57.3 | 50.2 | 7.1 | +8.11 | 9.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+rlm_ratio | total | 73-52 | 58.4 | 50.2 | 8.2 | +14.68 | 11.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | total | 34-27 | 55.7 | 50.1 | 5.6 | +3.73 | 6.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_quiet | total | 39-52 | 42.9 | 50.2 | -7.3 | -16.27 | -17.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_quiet | total | 22-28 | 44.0 | 50.2 | -6.2 | -7.86 | -15.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_quiet+rlm_ratio | total | 42-53 | 44.2 | 50.2 | -6.0 | -14.5 | -15.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 50.3 | 49.7 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

# Pooled (fit + forward together)

Kept for continuity. **Contaminated** — it mixes the games the engine was built
on with the games testing it. Use the forward table for any decision.

## EARLY  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 36-43 | 45.6 | 36.1 | 9.4 | +10.82 | 13.7 | 0.23 | 44.3 | no edge shown yet |
| pin_move | both | 5-9 | 35.7 | 48.2 | -12.5 | -5.1 | -36.4 | 0.22 | 50.0 | keep collecting (14/30) |
| money_delta | both | 10-8 | 55.6 | 42.3 | 13.3 | +3.43 | 19.1 | -0.09 | 33.3 | keep collecting (18/30) |
| pin_rlm | both | 1-2 | 33.3 | 27.5 | 5.8 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | both | 511-450 | 53.2 | 52.0 | 1.1 | -56.21 | -5.8 | 0.2 | 41.7 | no edge shown yet |
| rlm_ratio | both | 33-23 | 58.9 | 39.1 | 19.8 | +19.02 | 34.0 | 0.47 | 51.8 | no edge shown yet |
| money_level | both | 182-124 | 59.5 | 59.0 | 0.5 | -18.97 | -6.2 | -0.11 | 38.9 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 154-133 | 53.7 | 48.0 | 5.6 | +17.04 | 5.9 | 0.3 | 43.9 | no edge shown yet |
| money_moving | both | 114-90 | 55.9 | 51.0 | 4.9 | +3.02 | 1.5 | 0.1 | 42.6 | no edge shown yet |
| pin_value | both | 51-49 | 51.0 | 48.4 | 2.6 | -3.66 | -3.7 | 0.08 | 38.0 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.4 | -31.4 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 243-310 | 43.9 | 47.7 | -3.8 | -61.62 | -11.1 | 0.38 | 45.2 | DROP: below break-even |
| consensus_gap+money_level | both | 37-32 | 53.6 | 63.4 | -9.7 | -11.9 | -17.2 | 0.3 | 47.8 | no edge shown yet |
| consensus_gap+money_moving | both | 20-24 | 45.5 | 48.2 | -2.7 | -6.16 | -14.0 | 0.23 | 40.9 | no edge shown yet |
| consensus_gap+pin_value | both | 19-28 | 40.4 | 46.7 | -6.3 | -11.54 | -24.5 | 0.39 | 48.9 | DROP: below break-even |
| follow_move+rlm_quiet | both | 36-43 | 45.6 | 36.1 | 9.4 | +10.82 | 13.7 | 0.23 | 44.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 33-23 | 58.9 | 39.1 | 19.8 | +19.02 | 34.0 | 0.47 | 51.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 80-45 | 64.0 | 49.3 | 14.7 | +22.71 | 18.2 | 0.4 | 48.0 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 69-46 | 60.0 | 58.0 | 2.0 | -4.07 | -3.5 | -0.1 | 46.1 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 11-9 | 55.0 | 49.5 | 5.5 | +0.81 | 4.0 | 0.4 | 45.0 | keep collecting (20/30) |
| money_moving+pin_value | both | 8-5 | 61.5 | 49.7 | 11.8 | +2.04 | 15.7 | 0.31 | 38.5 | keep collecting (13/30) |
| rlm_quiet+rlm_ratio | both | 20-14 | 58.8 | 36.6 | 22.3 | +14.73 | 43.3 | -0.04 | 47.1 | no edge shown yet |
| rlm_quiet+sharp_gap | both | 22-17 | 56.4 | 36.5 | 19.9 | +13.55 | 34.7 | -0.06 | 46.2 | no edge shown yet |
| rlm_ratio+sharp_gap | both | 33-23 | 58.9 | 39.1 | 19.8 | +19.02 | 34.0 | 0.47 | 51.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 101-66 | 60.5 | 55.5 | 5.0 | +0.84 | 0.5 | 0.16 | 43.7 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 67-54 | 55.4 | 48.4 | 7.0 | +6.6 | 5.5 | 0.28 | 47.1 | no edge shown yet |
| money_delta+money_level | both | 3-3 | 50.0 | 46.4 | 3.6 | +0.46 | 7.6 | 1.3 | 66.7 | keep collecting (6/30) |
| money_delta+money_moving | both | 9-8 | 52.9 | 41.9 | 11.1 | +2.53 | 14.9 | -0.1 | 35.3 | keep collecting (17/30) |
| money_delta+pin_value | both | 3-1 | 75.0 | 50.0 | 25.0 | +1.61 | 40.3 | 0.0 | 25.0 | keep collecting (4/30) |
| money_delta+sharp_gap | both | 7-6 | 53.8 | 41.4 | 12.5 | +2.78 | 21.4 | -0.13 | 46.2 | keep collecting (13/30) |
| pin_value+sharp_gap | both | 13-8 | 61.9 | 48.7 | 13.2 | +3.66 | 17.4 | -0.18 | 33.3 | keep collecting (21/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 50.7 | -50.7 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 35-45 | 43.8 | 51.8 | -8.1 | -17.31 | -21.6 | 0.75 | 56.2 | DROP: below break-even |
| consensus_gap+rlm_quiet | both | 4-7 | 36.4 | 37.3 | -0.9 | -2.99 | -27.1 | 0.95 | 72.7 | keep collecting (11/30) |
| follow_move+pin_value | both | 21-17 | 55.3 | 48.9 | 6.4 | +1.32 | 3.5 | -0.17 | 28.9 | no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 42.5 | -25.8 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 29-47 | 38.2 | 45.9 | -7.7 | -10.04 | -13.2 | 0.86 | 50.0 | DROP: below break-even |
| follow_move+money_level | both | 93-51 | 64.6 | 59.8 | 4.8 | -4.74 | -3.3 | 0.02 | 43.1 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 11-9 | 55.0 | 42.4 | 12.6 | +2.43 | 12.1 | 1.45 | 65.0 | keep collecting (20/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 44.2 | 5.8 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 59-34 | 63.4 | 52.4 | 11.0 | +11.28 | 12.1 | 0.35 | 51.6 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 3-0 | 100.0 | 49.7 | 50.3 | +2.61 | 87.1 | 0.0 | 0.0 | keep collecting (3/30) |
| follow_move+money_delta | both | 5-4 | 55.6 | 42.0 | 13.5 | +2.95 | 32.8 | 0.27 | 44.4 | keep collecting (9/30) |
| money_delta+rlm_quiet | both | 2-2 | 50.0 | 38.0 | 12.0 | +1.53 | 38.3 | -2.1 | 0.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | both | 16-11 | 59.3 | 37.1 | 22.1 | +10.23 | 37.9 | 0.48 | 48.1 | keep collecting (27/30) |
| money_moving+rlm_ratio | both | 16-10 | 61.5 | 42.0 | 19.5 | +9.15 | 35.2 | 0.6 | 53.8 | keep collecting (26/30) |
| consensus_gap+rlm_ratio | both | 4-4 | 50.0 | 38.4 | 11.6 | +0.09 | 1.1 | 0.69 | 62.5 | keep collecting (8/30) |
| pin_move+pin_value | both | 1-4 | 20.0 | 49.2 | -29.2 | -3.09 | -61.8 | 0.2 | 20.0 | keep collecting (5/30) |
| follow_move+pin_move | both | 5-3 | 62.5 | 51.8 | 10.7 | +0.9 | 11.2 | 0.42 | 62.5 | keep collecting (8/30) |
| consensus_gap+pin_move | both | 0-5 | 0.0 | 44.6 | -44.6 | -5.0 | -100.0 | 0.26 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | both | 2-2 | 50.0 | 55.8 | -5.8 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 27.5 | -27.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 27.5 | 22.5 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 27.5 | -27.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 27.5 | -27.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 27.5 | 22.5 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | both | 1-2 | 33.3 | 27.5 | 5.8 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 50.8 | -50.8 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 49.3 | -49.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-1 | 66.7 | 50.2 | 16.4 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 27.5 | 72.5 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 27.5 | 72.5 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 27.5 | 72.5 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 2-2 | 50.0 | 38.4 | 11.6 | +2.34 | 58.5 | 1.15 | 75.0 | keep collecting (4/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 27.5 | -27.5 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 18-30 | 37.5 | 27.5 | 10.0 | +7.53 | 15.7 | 0.01 | 43.8 | DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.5 | 10.5 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 15-11 | 57.7 | 49.5 | 8.2 | +2.64 | 10.1 | 0.85 | 53.8 | keep collecting (26/30) |
| pin_move | moneyline | 2-3 | 40.0 | 45.5 | -5.5 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-4 | 20.0 | 49.5 | -29.5 | -3.09 | -61.8 | 0.4 | 40.0 | keep collecting (5/30) |
| pin_move | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.14 | -3.5 | 0.25 | 50.0 | keep collecting (4/30) |
| money_delta | moneyline | 2-4 | 33.3 | 27.5 | 5.8 | +0.34 | 5.7 | -1.45 | 33.3 | keep collecting (6/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 7-3 | 70.0 | 49.6 | 20.4 | +3.26 | 32.6 | 0.6 | 30.0 | keep collecting (10/30) |
| pin_rlm | moneyline | 1-2 | 33.3 | 27.5 | 5.8 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | moneyline | 210-138 | 60.3 | 55.8 | 4.5 | -19.94 | -5.7 | 0.13 | 44.8 | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 135-157 | 46.2 | 49.8 | -3.5 | -32.77 | -11.2 | 0.0 | 33.2 | DROP: below break-even |
| follow_move | total | 166-155 | 51.7 | 50.0 | 1.7 | -3.5 | -1.1 | 0.45 | 46.1 | no edge shown yet |
| rlm_ratio | moneyline | 14-13 | 51.9 | 27.5 | 24.4 | +11.47 | 42.5 | 0.43 | 55.6 | keep collecting (27/30) |
| rlm_ratio | spread | 3-3 | 50.0 | 51.6 | -1.6 | -0.16 | -2.7 | 0.33 | 16.7 | keep collecting (6/30) |
| rlm_ratio | total | 16-7 | 69.6 | 49.5 | 20.1 | +7.72 | 33.5 | 0.57 | 56.5 | keep collecting (23/30) |
| money_level | moneyline | 105-45 | 70.0 | 68.3 | 1.7 | -9.78 | -6.5 | -0.26 | 42.7 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-18 | 48.6 | 49.3 | -0.7 | -2.69 | -7.7 | 1.0 | 51.4 | no edge shown yet |
| money_level | total | 60-61 | 49.6 | 50.3 | -0.7 | -6.5 | -5.4 | -0.24 | 30.6 | no edge shown yet |
| sharp_gap | moneyline | 67-67 | 50.0 | 46.0 | 4.0 | +3.99 | 3.0 | 0.36 | 50.7 | no edge shown yet |
| sharp_gap | spread | 20-15 | 57.1 | 49.8 | 7.3 | +3.0 | 8.6 | 0.77 | 40.0 | no edge shown yet |
| sharp_gap | total | 67-51 | 56.8 | 49.9 | 6.9 | +10.04 | 8.5 | 0.09 | 37.3 | no edge shown yet |
| money_moving | moneyline | 51-45 | 53.1 | 52.3 | 0.8 | -9.12 | -9.5 | -0.06 | 47.9 | no edge shown yet |
| money_moving | spread | 18-6 | 75.0 | 49.2 | 25.8 | +10.18 | 42.4 | 0.5 | 45.8 | keep collecting (24/30) |
| money_moving | total | 45-39 | 53.6 | 50.0 | 3.6 | +1.96 | 2.3 | 0.17 | 35.7 | no edge shown yet |
| pin_value | moneyline | 2-6 | 25.0 | 33.1 | -8.1 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| pin_value | spread | 25-21 | 54.3 | 49.4 | 5.0 | +1.03 | 2.2 | 0.26 | 39.1 | no edge shown yet |
| pin_value | total | 24-22 | 52.2 | 50.0 | 2.1 | -0.38 | -0.8 | -0.07 | 34.8 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.3 | -19.0 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 99-174 | 36.3 | 45.8 | -9.5 | -53.18 | -19.5 | 0.1 | 42.1 | DROP: below break-even |
| consensus_gap | spread | 70-63 | 52.6 | 49.1 | 3.5 | -1.85 | -1.4 | 0.35 | 39.8 | no edge shown yet |
| consensus_gap | total | 74-73 | 50.3 | 50.1 | 0.3 | -6.59 | -4.5 | 0.93 | 55.8 | no edge shown yet |
| money_level+sharp_gap | moneyline | 49-20 | 71.0 | 63.4 | 7.6 | -0.34 | -0.5 | 0.06 | 53.6 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+follow_move | moneyline | 13-23 | 36.1 | 55.0 | -18.9 | -14.89 | -41.4 | 0.13 | 52.8 | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 33.1 | -8.1 | -4.31 | -53.8 | -0.08 | 50.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| consensus_gap+rlm_quiet | moneyline | 1-5 | 16.7 | 27.5 | -10.8 | -3.68 | -61.3 | 1.07 | 83.3 | keep collecting (6/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.5 | -9.2 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 18-30 | 37.5 | 27.5 | 10.0 | +7.53 | 15.7 | 0.01 | 43.8 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 34-15 | 69.4 | 68.8 | 0.5 | -5.03 | -10.3 | -0.57 | 49.0 | beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 27.5 | -27.5 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 18-37 | 32.7 | 44.7 | -12.0 | -9.77 | -17.8 | 0.85 | 50.9 | DROP: below break-even |
| follow_move+money_level | moneyline | 59-18 | 76.6 | 68.4 | 8.2 | -2.63 | -3.4 | -0.32 | 44.2 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 31-14 | 68.9 | 55.5 | 13.4 | +5.67 | 12.6 | 0.06 | 53.3 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 28-22 | 56.0 | 68.9 | -12.9 | -9.74 | -19.5 | 0.05 | 46.0 | no edge shown yet |
| follow_move+sharp_gap | moneyline | 37-20 | 64.9 | 48.8 | 16.1 | +8.57 | 15.0 | 0.25 | 52.6 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 26-28 | 48.1 | 46.7 | 1.5 | -4.66 | -8.6 | 0.2 | 55.6 | no edge shown yet |
| consensus_gap+money_moving | moneyline | 11-22 | 33.3 | 48.0 | -14.6 | -12.01 | -36.4 | 0.22 | 45.5 | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 14-13 | 51.9 | 27.5 | 24.4 | +11.47 | 42.5 | 0.43 | 55.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 10-10 | 50.0 | 27.5 | 22.5 | +9.6 | 48.0 | -0.12 | 45.0 | keep collecting (20/30) |
| rlm_quiet+sharp_gap | moneyline | 10-13 | 43.5 | 27.5 | 16.0 | +6.6 | 28.7 | -0.27 | 43.5 | keep collecting (23/30) |
| rlm_ratio+sharp_gap | moneyline | 14-13 | 51.9 | 27.5 | 24.4 | +11.47 | 42.5 | 0.43 | 55.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 27.5 | -2.5 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 7-8 | 46.7 | 27.5 | 19.2 | +5.13 | 34.2 | 0.59 | 53.3 | keep collecting (15/30) |
| money_moving+rlm_ratio | moneyline | 5-4 | 55.6 | 27.5 | 28.1 | +4.98 | 55.3 | 0.39 | 55.6 | keep collecting (9/30) |
| money_delta+money_moving | moneyline | 2-4 | 33.3 | 27.5 | 5.8 | +0.34 | 5.7 | -1.45 | 33.3 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-3 | 40.0 | 27.5 | 12.5 | +1.34 | 26.8 | -1.74 | 40.0 | keep collecting (5/30) |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 42.5 | -42.5 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-1 | 66.7 | 57.5 | 9.2 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | moneyline | 2-1 | 66.7 | 57.5 | 9.2 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 27.5 | -27.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-1 | 50.0 | 27.5 | 22.5 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 27.5 | -27.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 27.5 | -27.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-1 | 50.0 | 27.5 | 22.5 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | moneyline | 1-2 | 33.3 | 27.5 | 5.8 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 27.5 | -27.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 27.5 | -27.5 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.13 | 56.5 | -0.1 | 50.0 | keep collecting (2/30) |
| money_level+rlm_ratio | moneyline | 4-3 | 57.1 | 27.5 | 29.7 | +1.87 | 26.7 | 2.0 | 85.7 | keep collecting (7/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 27.5 | 72.5 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 1-0 | 100.0 | 27.5 | 72.5 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 1-0 | 100.0 | 27.5 | 72.5 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 27.5 | 39.2 | +3.34 | 111.3 | -1.53 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 1-1 | 50.0 | 27.5 | 22.5 | +1.7 | 85.0 | -4.2 | 0.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 27.5 | 72.5 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 27.5 | -27.5 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-0 | 100.0 | 27.5 | 72.5 | +1.64 | 164.0 | 3.8 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 47.7 | -2.2 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 47.7 | 35.7 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 10-8 | 55.6 | 48.7 | 6.9 | +0.6 | 3.3 | 0.5 | 50.0 | keep collecting (18/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.5 | 10.5 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-3 | 50.0 | 51.6 | -1.6 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-7 | 58.8 | 49.0 | 9.8 | +2.09 | 12.3 | 0.88 | 41.2 | keep collecting (17/30) |
| money_level+money_moving | spread | 10-6 | 62.5 | 48.8 | 13.7 | +3.12 | 19.5 | 1.19 | 68.8 | keep collecting (16/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 49.0 | -6.1 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.5 | 10.5 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 3-3 | 50.0 | 51.6 | -1.6 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 52.3 | -52.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 52.3 | -52.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-12 | 53.8 | 49.3 | 4.6 | +0.62 | 2.4 | 1.15 | 46.2 | keep collecting (26/30) |
| money_moving+sharp_gap | spread | 10-4 | 71.4 | 49.3 | 22.1 | +5.04 | 36.0 | 0.86 | 50.0 | keep collecting (14/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.2 | 17.4 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-11 | 45.0 | 48.4 | -3.4 | -3.2 | -16.0 | 0.85 | 45.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 47.7 | 14.8 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 11-10 | 52.4 | 48.8 | 3.6 | +0.04 | 0.2 | 0.9 | 47.6 | keep collecting (21/30) |
| follow_move+pin_value | spread | 12-7 | 63.2 | 48.9 | 14.3 | +3.45 | 18.2 | 0.26 | 31.6 | keep collecting (19/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 47.7 | 52.3 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 47.7 | 52.3 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 47.7 | 52.3 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-3 | 75.0 | 48.4 | 26.6 | +5.22 | 43.5 | 0.75 | 50.0 | keep collecting (12/30) |
| money_delta+rlm_quiet | spread | 1-0 | 100.0 | 47.7 | 52.3 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 2-0 | 100.0 | 47.7 | 52.3 | +1.74 | 87.1 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 2-2 | 50.0 | 52.3 | -2.3 | -0.07 | -1.7 | 1.25 | 25.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | spread | 2-1 | 66.7 | 50.8 | 15.9 | +0.86 | 28.7 | 1.0 | 33.3 | keep collecting (3/30) |
| pin_move+pin_value | spread | 1-3 | 25.0 | 48.8 | -23.8 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 47.7 | -47.7 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-2 | 33.3 | 47.7 | -14.3 | -1.09 | -36.4 | 0.33 | 33.3 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.3 | -52.3 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 15-11 | 57.7 | 49.5 | 8.2 | +2.64 | 10.1 | 0.85 | 53.8 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 25-25 | 50.0 | 50.2 | -0.2 | -2.17 | -4.3 | -0.06 | 36.0 | no edge shown yet |
| money_level+sharp_gap | total | 38-34 | 52.8 | 50.1 | 2.6 | +0.55 | 0.8 | -0.11 | 33.3 | no edge shown yet |
| money_moving+sharp_gap | total | 31-22 | 58.5 | 49.8 | 8.7 | +6.23 | 11.8 | 0.21 | 37.7 | no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 50.7 | -50.7 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 8-5 | 61.5 | 49.7 | 11.8 | +2.23 | 17.2 | 0.23 | 30.8 | keep collecting (13/30) |
| money_moving+pin_value | total | 5-3 | 62.5 | 49.8 | 12.7 | +1.47 | 18.3 | 0.12 | 25.0 | keep collecting (8/30) |
| pin_value+sharp_gap | total | 11-6 | 64.7 | 49.9 | 14.8 | +3.92 | 23.1 | -0.06 | 29.4 | keep collecting (17/30) |
| follow_move+money_level | total | 23-23 | 50.0 | 50.3 | -0.3 | -2.15 | -4.7 | 0.2 | 39.1 | no edge shown yet |
| follow_move+pin_value | total | 8-8 | 50.0 | 50.1 | -0.1 | -0.84 | -5.3 | -0.44 | 25.0 | keep collecting (16/30) |
| follow_move+rlm_ratio | total | 16-7 | 69.6 | 49.5 | 20.1 | +7.72 | 33.5 | 0.57 | 56.5 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 33-18 | 64.7 | 49.9 | 14.8 | +12.05 | 23.6 | 0.41 | 45.1 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 5-4 | 55.6 | 49.5 | 6.1 | +0.63 | 7.0 | 1.11 | 66.7 | keep collecting (9/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 49.8 | 16.9 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 16-7 | 69.6 | 49.5 | 20.1 | +7.72 | 33.5 | 0.57 | 56.5 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 19-17 | 52.8 | 49.9 | 2.9 | +0.38 | 1.1 | 0.58 | 50.0 | no edge shown yet |
| consensus_gap+money_level | total | 4-4 | 50.0 | 50.3 | -0.3 | -0.47 | -5.9 | -0.12 | 25.0 | keep collecting (8/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 50.4 | 29.6 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 50.2 | -16.8 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 6-7 | 46.2 | 49.8 | -3.7 | -1.58 | -12.2 | 0.08 | 30.8 | keep collecting (13/30) |
| money_moving+rlm_ratio | total | 9-5 | 64.3 | 49.5 | 14.8 | +3.31 | 23.6 | 0.64 | 57.1 | keep collecting (14/30) |
| consensus_gap+follow_move | total | 13-11 | 54.2 | 50.0 | 4.2 | +0.79 | 3.3 | 1.58 | 70.8 | keep collecting (24/30) |
| consensus_gap+money_delta | total | 2-0 | 100.0 | 50.7 | 49.3 | +1.78 | 88.9 | 0.0 | 0.0 | keep collecting (2/30) |
| follow_move+money_delta | total | 2-3 | 40.0 | 49.6 | -9.6 | -1.22 | -24.4 | 1.4 | 60.0 | keep collecting (5/30) |
| money_delta+money_moving | total | 6-3 | 66.7 | 49.6 | 17.0 | +2.35 | 26.1 | 0.67 | 33.3 | keep collecting (9/30) |
| money_delta+pin_value | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 | -0.5 | 0.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 5-2 | 71.4 | 49.7 | 21.7 | +2.44 | 34.9 | 0.86 | 42.9 | keep collecting (7/30) |
| money_moving+rlm_quiet | total | 7-3 | 70.0 | 49.5 | 20.5 | +3.36 | 33.6 | 0.6 | 50.0 | keep collecting (10/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 9-3 | 75.0 | 49.4 | 25.6 | +5.22 | 43.5 | 0.33 | 58.3 | keep collecting (12/30) |
| rlm_quiet+sharp_gap | total | 11-3 | 78.6 | 49.4 | 29.1 | +7.04 | 50.3 | 0.5 | 57.1 | keep collecting (14/30) |
| follow_move+pin_move | total | 2-0 | 100.0 | 49.3 | 50.7 | +1.86 | 93.0 | 1.0 | 100.0 | keep collecting (2/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 49.3 | -49.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 49.3 | -49.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 2-2 | 50.0 | 49.7 | 0.3 | -0.18 | -4.5 | 0.75 | 50.0 | keep collecting (4/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 49.3 | 0.7 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 3-1 | 75.0 | 49.3 | 25.7 | +1.77 | 44.2 | 0.25 | 50.0 | keep collecting (4/30) |
| money_level+pin_move | total | 0-1 | 0.0 | 50.7 | -50.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_value | total | 0-1 | 0.0 | 50.7 | -50.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 50.7 | -50.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 49.3 | -49.3 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 0-2 | 0.0 | 49.3 | -49.3 | -2.0 | -100.0 | 2.0 | 100.0 | keep collecting (2/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 204-303 | 40.2 | 42.0 | -1.7 | -46.96 | -9.3 |  |  | DROP: below break-even |
| pin_move | both | 536-544 | 49.6 | 49.9 | -0.2 | -41.41 | -3.8 |  |  | DROP: below break-even |
| money_delta | both | 341-451 | 43.1 | 43.9 | -0.9 | -57.1 | -7.2 |  |  | DROP: below break-even |
| pin_rlm | both | 147-170 | 46.4 | 42.3 | 4.1 | +25.37 | 8.0 |  |  | DROP: below break-even |
| follow_move | both | 926-858 | 51.9 | 51.6 | 0.3 | -114.52 | -6.4 |  |  | no edge shown yet |
| rlm_ratio | both | 214-255 | 45.6 | 44.1 | 1.5 | -15.4 | -3.3 |  |  | DROP: below break-even |
| money_level | both | 1177-870 | 57.5 | 55.5 | 2.0 | -64.5 | -3.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 905-1059 | 46.1 | 47.5 | -1.4 | -146.23 | -7.4 |  |  | DROP: below break-even |
| money_moving | both | 910-1058 | 46.2 | 47.8 | -1.6 | -151.28 | -7.7 |  |  | DROP: below break-even |
| pin_value | both | 392-383 | 50.6 | 48.1 | 2.5 | +28.91 | 3.7 |  |  | no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 50.8 | 15.9 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 369-474 | 43.8 | 47.8 | -4.1 | -81.86 | -9.7 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 141-138 | 50.5 | 51.4 | -0.9 | -16.23 | -5.8 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 160-257 | 38.4 | 45.1 | -6.8 | -34.79 | -8.3 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 86-88 | 49.4 | 51.3 | -1.8 | +1.5 | 0.9 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 24-41 | 36.9 | 38.2 | -1.3 | +9.03 | 13.9 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 147-155 | 48.7 | 46.1 | 2.6 | +11.51 | 3.8 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | both | 28-47 | 37.3 | 39.5 | -2.2 | -2.86 | -3.8 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 158-261 | 37.7 | 44.5 | -6.8 | -35.92 | -8.6 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 486-531 | 47.8 | 49.2 | -1.4 | -88.23 | -8.7 |  |  | DROP: below break-even |
| follow_move+pin_move | both | 385-394 | 49.4 | 50.1 | -0.7 | -44.95 | -5.8 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 115-122 | 48.5 | 44.1 | 4.5 | +3.65 | 1.5 |  |  | no edge shown yet |
| follow_move+pin_value | both | 134-126 | 51.5 | 49.0 | 2.5 | +3.09 | 1.2 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 214-255 | 45.6 | 44.1 | 1.5 | -15.4 | -3.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 492-530 | 48.1 | 49.0 | -0.8 | -79.21 | -7.8 |  |  | DROP: below break-even |
| money_moving+pin_move | both | 311-347 | 47.3 | 48.6 | -1.3 | -33.25 | -5.1 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 141-165 | 46.1 | 42.3 | 3.8 | +24.4 | 8.0 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 165-198 | 45.5 | 47.3 | -1.8 | -16.33 | -4.5 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 206-246 | 45.6 | 44.2 | 1.3 | -14.32 | -3.2 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 870-1018 | 46.1 | 47.5 | -1.4 | -135.77 | -7.2 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 135-142 | 48.7 | 44.1 | 4.6 | +19.24 | 6.9 |  |  | no edge shown yet |
| pin_move+pin_value | both | 166-165 | 50.2 | 49.2 | 1.0 | -6.08 | -1.8 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 122-120 | 50.4 | 45.4 | 5.0 | +10.99 | 4.5 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 316-350 | 47.4 | 48.4 | -1.0 | -31.79 | -4.8 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 41-42 | 49.4 | 45.6 | 3.8 | +12.49 | 15.1 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 115-122 | 48.5 | 44.1 | 4.5 | +3.65 | 1.5 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 147-170 | 46.4 | 42.3 | 4.1 | +25.37 | 8.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 41-31 | 56.9 | 48.4 | 8.5 | +6.42 | 8.9 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 166-199 | 45.5 | 47.2 | -1.7 | -16.44 | -4.5 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 214-255 | 45.6 | 44.1 | 1.5 | -15.4 | -3.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 164-198 | 45.3 | 45.7 | -0.4 | -32.29 | -8.9 |  |  | DROP: below break-even |
| money_level+money_moving | both | 642-574 | 52.8 | 52.3 | 0.5 | -53.84 | -4.4 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 629-564 | 52.7 | 52.1 | 0.6 | -46.94 | -3.9 |  |  | no edge shown yet |
| follow_move+money_level | both | 598-430 | 58.2 | 56.4 | 1.7 | -50.53 | -4.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 102-87 | 54.0 | 47.9 | 6.1 | +11.24 | 5.9 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 230-177 | 56.5 | 58.1 | -1.6 | -17.15 | -4.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_move | both | 311-287 | 52.0 | 53.1 | -1.1 | -32.79 | -5.5 |  |  | no edge shown yet |
| money_level+pin_value | both | 187-171 | 52.2 | 50.1 | 2.2 | -8.09 | -2.3 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 22-53 | 29.3 | 36.5 | -7.2 | -12.25 | -16.3 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | both | 204-303 | 40.2 | 42.0 | -1.7 | -46.96 | -9.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 105-174 | 37.6 | 41.7 | -4.0 | -38.78 | -13.9 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 246-351 | 41.2 | 42.3 | -1.1 | -44.8 | -7.5 |  |  | DROP: below break-even |
| consensus_gap+money_delta | both | 45-111 | 28.8 | 37.1 | -8.3 | -25.38 | -16.3 |  |  | DROP: below break-even |
| money_delta+money_level | both | 124-115 | 51.9 | 46.7 | 5.2 | +14.94 | 6.3 |  |  | no edge shown yet |
| money_delta+pin_value | both | 73-73 | 50.0 | 46.8 | 3.2 | +0.53 | 0.4 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 243-345 | 41.3 | 42.3 | -1.0 | -41.97 | -7.1 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 84-144 | 36.8 | 40.3 | -3.5 | -28.96 | -12.7 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | both | 97-168 | 36.6 | 41.6 | -5.0 | -38.68 | -14.6 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 56-103 | 35.2 | 42.9 | -7.7 | -40.21 | -25.3 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | both | 99-125 | 44.2 | 44.0 | 0.2 | -11.0 | -4.9 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 45-68 | 39.8 | 41.1 | -1.3 | -11.62 | -10.3 |  |  | DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 50.8 | 15.9 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 125-145 | 46.3 | 46.1 | 0.2 | -9.19 | -3.4 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 66-48 | 57.9 | 46.5 | 11.4 | +17.13 | 15.0 |  |  | no edge shown yet |
| money_delta+pin_rlm | both | 87-101 | 46.3 | 42.2 | 4.1 | +10.27 | 5.5 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | both | 121-132 | 47.8 | 44.6 | 3.2 | -5.82 | -2.3 |  |  | no edge shown yet |
| pin_value+rlm_quiet | both | 28-37 | 43.1 | 46.9 | -3.8 | -1.25 | -1.9 |  |  | DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 49.3 | 50.7 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 60-127 | 32.1 | 28.2 | 3.9 | -3.58 | -1.9 |  |  | DROP: below break-even |
| rlm_quiet | spread | 48-50 | 49.0 | 50.8 | -1.8 | -5.51 | -5.6 |  |  | no edge shown yet |
| rlm_quiet | total | 96-126 | 43.2 | 49.7 | -6.4 | -37.88 | -17.1 |  |  | DROP: below break-even |
| pin_move | moneyline | 115-112 | 50.7 | 49.3 | 1.4 | +6.55 | 2.9 |  |  | no edge shown yet |
| pin_move | spread | 208-222 | 48.4 | 50.2 | -1.8 | -32.65 | -7.6 |  |  | DROP: below break-even |
| pin_move | total | 213-210 | 50.4 | 49.8 | 0.5 | -15.31 | -3.6 |  |  | no edge shown yet |
| money_delta | moneyline | 57-175 | 24.6 | 28.8 | -4.3 | -40.53 | -17.5 |  |  | DROP: below break-even |
| money_delta | spread | 125-128 | 49.4 | 50.8 | -1.4 | -14.11 | -5.6 |  |  | no edge shown yet |
| money_delta | total | 159-148 | 51.8 | 49.6 | 2.2 | -2.45 | -0.8 |  |  | no edge shown yet |
| pin_rlm | moneyline | 41-76 | 35.0 | 29.4 | 5.6 | +22.33 | 19.1 |  |  | DROP: below break-even |
| pin_rlm | spread | 25-22 | 53.2 | 50.9 | 2.2 | +0.79 | 1.7 |  |  | no edge shown yet |
| pin_rlm | total | 81-72 | 52.9 | 49.5 | 3.4 | +2.24 | 1.5 |  |  | no edge shown yet |
| follow_move | moneyline | 342-234 | 59.4 | 55.3 | 4.1 | -22.42 | -3.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 262-289 | 47.5 | 49.6 | -2.1 | -51.03 | -9.3 |  |  | DROP: below break-even |
| follow_move | total | 322-335 | 49.0 | 50.0 | -0.9 | -41.08 | -6.3 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 41-94 | 30.4 | 30.2 | 0.2 | -12.49 | -9.3 |  |  | DROP: below break-even |
| rlm_ratio | spread | 41-45 | 47.7 | 50.2 | -2.5 | -7.76 | -9.0 |  |  | no edge shown yet |
| rlm_ratio | total | 132-116 | 53.2 | 49.6 | 3.6 | +4.85 | 2.0 |  |  | no edge shown yet |
| money_level | moneyline | 457-178 | 72.0 | 68.3 | 3.7 | -24.23 | -3.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 330-342 | 49.1 | 49.2 | -0.1 | -44.39 | -6.6 |  |  | DROP: below break-even |
| money_level | total | 390-350 | 52.7 | 50.2 | 2.5 | +4.11 | 0.6 |  |  | no edge shown yet |
| sharp_gap | moneyline | 226-355 | 38.9 | 42.1 | -3.2 | -58.54 | -10.1 |  |  | DROP: below break-even |
| sharp_gap | spread | 334-330 | 50.3 | 49.6 | 0.7 | -28.78 | -4.3 |  |  | no edge shown yet |
| sharp_gap | total | 345-374 | 48.0 | 49.9 | -1.9 | -58.92 | -8.2 |  |  | DROP: below break-even |
| money_moving | moneyline | 237-342 | 40.9 | 43.2 | -2.3 | -45.8 | -7.9 |  |  | DROP: below break-even |
| money_moving | spread | 331-333 | 49.8 | 49.5 | 0.3 | -34.65 | -5.2 |  |  | no edge shown yet |
| money_moving | total | 342-383 | 47.2 | 49.9 | -2.7 | -70.83 | -9.8 |  |  | DROP: below break-even |
| pin_value | moneyline | 22-55 | 28.6 | 32.2 | -3.6 | +28.96 | 37.6 |  |  | DROP: below break-even |
| pin_value | spread | 176-156 | 53.0 | 49.6 | 3.4 | -2.62 | -0.8 |  |  | no edge shown yet |
| pin_value | total | 194-172 | 53.0 | 50.1 | 2.9 | +2.57 | 0.7 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.3 | 47.7 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 158-286 | 35.6 | 46.0 | -10.5 | -78.02 | -17.6 |  |  | DROP: below break-even |
| consensus_gap | spread | 94-79 | 54.3 | 49.2 | 5.2 | +1.16 | 0.7 |  |  | no edge shown yet |
| consensus_gap | total | 117-109 | 51.8 | 50.3 | 1.4 | -5.0 | -2.2 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 165-92 | 64.2 | 62.5 | 1.7 | -3.71 | -1.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 153-90 | 63.0 | 62.0 | 1.0 | -4.02 | -1.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 212-328 | 39.3 | 42.1 | -2.8 | -42.78 | -7.9 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 61-73 | 45.5 | 53.4 | -7.8 | -20.92 | -15.6 |  |  | DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 8-41 | 16.3 | 29.3 | -13.0 | -12.64 | -25.8 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 60-127 | 32.1 | 28.2 | 3.9 | -3.58 | -1.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 110-70 | 61.1 | 68.8 | -7.7 | -14.84 | -8.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 62-161 | 27.8 | 41.2 | -13.4 | -24.11 | -10.8 |  |  | DROP: below break-even |
| follow_move+money_level | moneyline | 264-89 | 74.8 | 69.5 | 5.3 | -12.44 | -3.5 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 115-122 | 48.5 | 47.8 | 0.7 | -16.28 | -6.9 |  |  | no edge shown yet |
| money_delta+money_moving | moneyline | 54-158 | 25.5 | 28.5 | -3.1 | -26.5 | -12.5 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 52-157 | 24.9 | 28.6 | -3.7 | -27.69 | -13.2 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 59-167 | 26.1 | 40.0 | -13.9 | -28.12 | -12.4 |  |  | DROP: below break-even |
| follow_move+sharp_gap | moneyline | 112-124 | 47.5 | 46.8 | 0.7 | -18.7 | -7.9 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | moneyline | 25-76 | 24.8 | 28.4 | -3.6 | -12.59 | -12.5 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 26-80 | 24.5 | 28.3 | -3.8 | -17.13 | -16.2 |  |  | DROP: below break-even |
| consensus_gap+pin_move | moneyline | 33-36 | 47.8 | 53.6 | -5.8 | +7.36 | 10.7 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 11-29 | 27.5 | 30.9 | -3.4 | +9.65 | 24.1 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 5-34 | 12.8 | 29.8 | -17.0 | -10.04 | -25.7 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 94-78 | 54.7 | 50.8 | 3.9 | +5.5 | 3.2 |  |  | no edge shown yet |
| follow_move+pin_rlm | moneyline | 27-42 | 39.1 | 30.1 | 9.0 | +2.82 | 4.1 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 41-94 | 30.4 | 30.2 | 0.2 | -12.49 | -9.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 50-64 | 43.9 | 42.9 | 1.0 | +12.09 | 10.6 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 40-73 | 35.4 | 29.5 | 5.9 | +23.93 | 21.2 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 40-88 | 31.2 | 30.3 | 1.0 | -7.89 | -6.2 |  |  | DROP: below break-even |
| pin_move+pin_rlm | moneyline | 29-48 | 37.7 | 29.2 | 8.4 | +16.21 | 21.0 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 27-38 | 41.5 | 28.9 | 12.7 | +9.61 | 14.8 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 23-33 | 41.1 | 30.7 | 10.4 | +7.3 | 13.0 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 50-67 | 42.7 | 42.1 | 0.6 | +8.91 | 7.6 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 15-33 | 31.2 | 29.4 | 1.9 | -4.18 | -8.7 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 27-42 | 39.1 | 30.1 | 9.0 | +2.82 | 4.1 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 41-76 | 35.0 | 29.4 | 5.6 | +22.33 | 19.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 24-76 | 24.0 | 28.4 | -4.4 | -15.91 | -15.9 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 41-94 | 30.4 | 30.2 | 0.2 | -12.49 | -9.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 13-83 | 13.5 | 28.9 | -15.4 | -25.12 | -26.2 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 15-45 | 25.0 | 31.2 | -6.2 | +6.77 | 11.3 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 18-37 | 32.7 | 30.8 | 2.0 | +0.86 | 1.6 |  |  | DROP: below break-even |
| money_delta+pin_rlm | moneyline | 24-46 | 34.3 | 29.4 | 4.9 | +7.65 | 10.9 |  |  | DROP: below break-even |
| money_delta+pin_value | moneyline | 3-18 | 14.3 | 27.5 | -13.2 | -6.68 | -31.8 |  |  | keep collecting (21/30) |
| money_moving+pin_value | moneyline | 11-33 | 25.0 | 30.6 | -5.6 | +12.94 | 29.4 |  |  | DROP: below break-even |
| pin_move+pin_value | moneyline | 6-10 | 37.5 | 35.9 | 1.6 | +6.27 | 39.2 |  |  | keep collecting (16/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 27.5 | 3.8 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 11-35 | 23.9 | 30.4 | -6.5 | +10.94 | 23.8 |  |  | DROP: below break-even |
| follow_move+money_delta | moneyline | 25-54 | 31.6 | 30.9 | 0.7 | -15.07 | -19.1 |  |  | DROP: below break-even |
| money_delta+money_level | moneyline | 16-24 | 40.0 | 30.9 | 9.1 | +7.85 | 19.6 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | moneyline | 23-45 | 33.8 | 30.8 | 3.0 | -7.98 | -11.7 |  |  | DROP: below break-even |
| money_level+pin_move | moneyline | 75-46 | 62.0 | 66.2 | -4.2 | -5.95 | -4.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 12-11 | 52.2 | 33.4 | 18.8 | +4.79 | 20.8 |  |  | keep collecting (23/30) |
| money_level+rlm_ratio | moneyline | 15-13 | 53.6 | 37.1 | 16.4 | +6.04 | 21.6 |  |  | keep collecting (28/30) |
| money_delta+rlm_quiet | moneyline | 16-40 | 28.6 | 29.9 | -1.3 | -13.95 | -24.9 |  |  | DROP: below break-even |
| money_level+pin_value | moneyline | 5-3 | 62.5 | 66.9 | -4.4 | -0.32 | -4.0 |  |  | keep collecting (8/30) |
| follow_move+pin_value | moneyline | 3-8 | 27.3 | 35.7 | -8.4 | +4.8 | 43.7 |  |  | keep collecting (11/30) |
| pin_value+rlm_quiet | moneyline | 2-6 | 25.0 | 27.5 | -2.5 | +6.12 | 76.5 |  |  | keep collecting (8/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 27.5 | -2.5 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 35-28 | 55.6 | 48.6 | 6.9 | +1.81 | 2.9 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 48-44 | 52.2 | 48.9 | 3.2 | -3.09 | -3.4 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 26-29 | 47.3 | 49.2 | -1.9 | -6.82 | -12.4 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | -0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 66-48 | 57.9 | 49.1 | 8.8 | +8.12 | 7.1 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 4-4 | 50.0 | 50.0 | -0.0 | -0.67 | -8.3 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | spread | 47-44 | 51.6 | 49.1 | 2.5 | -3.99 | -4.4 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 158-167 | 48.6 | 49.3 | -0.7 | -24.2 | -7.4 |  |  | no edge shown yet |
| follow_move+pin_move | spread | 129-148 | 46.6 | 49.9 | -3.4 | -30.64 | -11.1 |  |  | DROP: below break-even |
| follow_move+pin_rlm | spread | 19-18 | 51.4 | 50.7 | 0.7 | -0.65 | -1.7 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 61-51 | 54.5 | 49.1 | 5.4 | +2.18 | 1.9 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 41-45 | 47.7 | 50.2 | -2.5 | -7.76 | -9.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 159-166 | 48.9 | 49.3 | -0.4 | -22.06 | -6.8 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 118-129 | 47.8 | 49.8 | -2.0 | -22.09 | -8.9 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 23-22 | 51.1 | 50.9 | 0.2 | -1.04 | -2.3 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 81-84 | 49.1 | 49.2 | -0.1 | -14.05 | -8.5 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 39-44 | 47.0 | 50.1 | -3.1 | -8.69 | -10.5 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 326-325 | 50.1 | 49.6 | 0.5 | -31.15 | -4.8 |  |  | no edge shown yet |
| pin_move+pin_rlm | spread | 25-22 | 53.2 | 50.9 | 2.2 | +0.79 | 1.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 80-82 | 49.4 | 49.7 | -0.3 | -11.61 | -7.2 |  |  | no edge shown yet |
| pin_move+rlm_ratio | spread | 22-24 | 47.8 | 50.5 | -2.7 | -3.94 | -8.6 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 121-129 | 48.4 | 49.8 | -1.4 | -19.36 | -7.7 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 7-10 | 41.2 | 50.7 | -9.5 | -3.88 | -22.8 |  |  | keep collecting (17/30) |
| pin_rlm+rlm_ratio | spread | 19-18 | 51.4 | 50.7 | 0.7 | -0.65 | -1.7 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 25-22 | 53.2 | 50.9 | 2.2 | +0.79 | 1.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 7-7 | 50.0 | 49.3 | 0.7 | -1.01 | -7.2 |  |  | keep collecting (14/30) |
| pin_value+sharp_gap | spread | 81-84 | 49.1 | 49.3 | -0.2 | -14.11 | -8.6 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 41-45 | 47.7 | 50.2 | -2.5 | -7.76 | -9.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 154-169 | 47.7 | 49.1 | -1.4 | -29.82 | -9.2 |  |  | DROP: below break-even |
| money_level+rlm_ratio | spread | 21-28 | 42.9 | 49.9 | -7.0 | -9.13 | -18.6 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 256-257 | 49.9 | 49.3 | 0.7 | -26.5 | -5.2 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 59-48 | 55.1 | 48.8 | 6.4 | +2.47 | 2.3 |  |  | no edge shown yet |
| money_level+money_moving | spread | 255-258 | 49.7 | 49.2 | 0.5 | -28.42 | -5.5 |  |  | no edge shown yet |
| money_level+pin_move | spread | 109-130 | 45.6 | 49.6 | -4.0 | -31.62 | -13.2 |  |  | DROP: below break-even |
| money_level+pin_value | spread | 89-89 | 50.0 | 49.0 | 1.0 | -12.15 | -6.8 |  |  | no edge shown yet |
| consensus_gap+money_delta | spread | 14-14 | 50.0 | 50.5 | -0.5 | -2.09 | -7.5 |  |  | keep collecting (28/30) |
| follow_move+money_delta | spread | 38-49 | 43.7 | 50.2 | -6.6 | -14.62 | -16.8 |  |  | DROP: below break-even |
| money_delta+money_level | spread | 41-40 | 50.6 | 50.0 | 0.6 | -3.05 | -3.8 |  |  | no edge shown yet |
| money_delta+money_moving | spread | 70-75 | 48.3 | 50.4 | -2.2 | -11.82 | -8.2 |  |  | no edge shown yet |
| money_delta+pin_value | spread | 32-26 | 55.2 | 50.5 | 4.7 | +1.88 | 3.2 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 69-73 | 48.6 | 50.4 | -1.8 | -10.8 | -7.6 |  |  | no edge shown yet |
| follow_move+rlm_quiet | spread | 48-50 | 49.0 | 50.8 | -1.8 | -5.51 | -5.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 14-5 | 73.7 | 50.9 | 22.8 | +7.78 | 40.9 |  |  | keep collecting (19/30) |
| rlm_quiet+sharp_gap | spread | 21-11 | 65.6 | 51.0 | 14.6 | +8.22 | 25.7 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 14-10 | 58.3 | 50.4 | 7.9 | +2.58 | 10.7 |  |  | keep collecting (24/30) |
| money_delta+rlm_ratio | spread | 16-27 | 37.2 | 49.9 | -12.7 | -12.78 | -29.7 |  |  | DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 52.3 | 47.7 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_move | spread | 36-42 | 46.2 | 50.9 | -4.7 | -9.09 | -11.7 |  |  | no edge shown yet |
| money_delta+pin_rlm | spread | 13-15 | 46.4 | 50.7 | -4.2 | -3.31 | -11.8 |  |  | keep collecting (28/30) |
| money_delta+rlm_quiet | spread | 14-18 | 43.8 | 51.2 | -7.4 | -5.07 | -15.8 |  |  | no edge shown yet |
| money_moving+rlm_quiet | spread | 20-11 | 64.5 | 51.0 | 13.5 | +7.27 | 23.4 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 26-24 | 52.0 | 51.2 | 0.8 | +0.08 | 0.2 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-2 | 75.0 | 51.7 | 23.3 | +3.56 | 44.5 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_quiet | spread | 3-3 | 50.0 | 50.8 | -0.8 | -0.42 | -7.1 |  |  | keep collecting (6/30) |
| pin_value+rlm_quiet | spread | 5-4 | 55.6 | 49.2 | 6.3 | +0.39 | 4.4 |  |  | keep collecting (9/30) |
| follow_move+money_delta | total | 101-95 | 51.5 | 49.6 | 1.9 | -2.6 | -1.3 |  |  | no edge shown yet |
| money_level+money_moving | total | 222-224 | 49.8 | 50.0 | -0.3 | -21.71 | -4.9 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 220-217 | 50.3 | 50.0 | 0.3 | -16.43 | -3.8 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 332-365 | 47.6 | 49.9 | -2.2 | -61.85 | -8.9 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 61-59 | 50.8 | 50.5 | 0.3 | -4.78 | -4.0 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 27-23 | 54.0 | 50.3 | 3.7 | +0.96 | 1.9 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 66-62 | 51.6 | 50.3 | 1.2 | -3.38 | -2.6 |  |  | no edge shown yet |
| follow_move+money_moving | total | 213-242 | 46.8 | 49.9 | -3.1 | -47.76 | -10.5 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 221-240 | 47.9 | 49.9 | -1.9 | -38.45 | -8.3 |  |  | DROP: below break-even |
| money_level+pin_move | total | 127-111 | 53.4 | 50.0 | 3.4 | +4.77 | 2.0 |  |  | no edge shown yet |
| money_level+pin_value | total | 93-79 | 54.1 | 50.3 | 3.7 | +4.37 | 2.5 |  |  | no edge shown yet |
| pin_move+pin_value | total | 80-73 | 52.3 | 50.0 | 2.3 | -0.74 | -0.5 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 96-126 | 43.2 | 49.7 | -6.4 | -37.88 | -17.1 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 143-154 | 48.1 | 49.8 | -1.6 | -23.26 | -7.8 |  |  | no edge shown yet |
| rlm_quiet+sharp_gap | total | 58-83 | 41.1 | 49.6 | -8.4 | -29.86 | -21.2 |  |  | DROP: below break-even |
| money_delta+money_moving | total | 122-118 | 50.8 | 49.6 | 1.2 | -6.48 | -2.7 |  |  | no edge shown yet |
| follow_move+money_level | total | 180-172 | 51.1 | 50.1 | 1.0 | -8.27 | -2.3 |  |  | no edge shown yet |
| follow_move+pin_value | total | 70-67 | 51.1 | 50.1 | 1.0 | -3.89 | -2.8 |  |  | no edge shown yet |
| money_moving+pin_value | total | 73-81 | 47.4 | 50.0 | -2.6 | -15.22 | -9.9 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 74-80 | 48.1 | 50.0 | -1.9 | -13.27 | -8.6 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 50-52 | 49.0 | 50.3 | -1.3 | -7.59 | -7.4 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 52-50 | 51.0 | 50.3 | 0.7 | -3.81 | -3.7 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 45-37 | 54.9 | 50.4 | 4.5 | +2.88 | 3.5 |  |  | no edge shown yet |
| consensus_gap+money_delta | total | 18-14 | 56.2 | 50.0 | 6.2 | +1.83 | 5.7 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | total | 11-9 | 55.0 | 49.9 | 5.1 | +0.81 | 4.1 |  |  | keep collecting (20/30) |
| money_delta+rlm_quiet | total | 26-45 | 36.6 | 49.5 | -12.8 | -21.18 | -29.8 |  |  | DROP: below break-even |
| money_delta+sharp_gap | total | 122-115 | 51.5 | 49.6 | 1.9 | -3.48 | -1.5 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 52-81 | 39.1 | 49.6 | -10.5 | -33.36 | -25.1 |  |  | DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 67-51 | 56.8 | 49.7 | 7.1 | +10.15 | 8.6 |  |  | no edge shown yet |
| money_delta+pin_move | total | 71-66 | 51.8 | 49.5 | 2.3 | -0.96 | -0.7 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 145-154 | 48.5 | 49.8 | -1.3 | -21.35 | -7.1 |  |  | no edge shown yet |
| follow_move+pin_move | total | 162-168 | 49.1 | 49.9 | -0.8 | -19.81 | -6.0 |  |  | no edge shown yet |
| pin_value+rlm_quiet | total | 21-27 | 43.8 | 49.6 | -5.9 | -7.76 | -16.2 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | total | 10-9 | 52.6 | 50.0 | 2.6 | -0.13 | -0.7 |  |  | keep collecting (19/30) |
| consensus_gap+rlm_ratio | total | 19-9 | 67.9 | 50.1 | 17.7 | +7.85 | 28.0 |  |  | keep collecting (28/30) |
| follow_move+pin_rlm | total | 69-62 | 52.7 | 49.5 | 3.1 | +1.48 | 1.1 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 132-116 | 53.2 | 49.6 | 3.6 | +4.85 | 2.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 40-27 | 59.7 | 49.5 | 10.2 | +9.77 | 14.6 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 66-46 | 58.9 | 49.7 | 9.2 | +14.33 | 12.8 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 78-70 | 52.7 | 49.5 | 3.2 | +1.51 | 1.0 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 127-114 | 52.7 | 49.6 | 3.1 | +2.27 | 0.9 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 81-72 | 52.9 | 49.5 | 3.4 | +2.24 | 1.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 77-63 | 55.0 | 49.6 | 5.4 | +7.64 | 5.5 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 29-21 | 58.0 | 49.7 | 8.3 | +5.3 | 10.6 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 69-62 | 52.7 | 49.5 | 3.1 | +1.48 | 1.1 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 81-72 | 52.9 | 49.5 | 3.4 | +2.24 | 1.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 33-21 | 61.1 | 49.7 | 11.4 | +8.91 | 16.5 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 132-116 | 53.2 | 49.6 | 3.6 | +4.85 | 2.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 50-40 | 55.6 | 49.5 | 6.1 | +5.92 | 6.6 |  |  | no edge shown yet |
| money_delta+rlm_ratio | total | 82-60 | 57.7 | 49.6 | 8.2 | +14.93 | 10.5 |  |  | no edge shown yet |
| money_delta+pin_value | total | 38-29 | 56.7 | 49.7 | 7.0 | +5.33 | 8.0 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 46-63 | 42.2 | 49.6 | -7.4 | -20.69 | -19.0 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | total | 24-33 | 42.1 | 49.5 | -7.4 | -11.0 | -19.3 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | total | 46-63 | 42.2 | 49.5 | -7.3 | -20.82 | -19.1 |  |  | DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 49.3 | 50.7 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| rlm_quiet | close | 1-3k bets | 135-201 | 40.2 | -1.6 | -7.4 |  |
| rlm_quiet | close | 3k+ bets | 46-65 | 41.4 | -1.2 | -10.0 |  |
| rlm_quiet | close | <1k bets | 23-37 | 38.3 | -3.5 | -18.5 |  |
| rlm_quiet | close | pin $1-2k | 55-93 | 37.2 | -6.0 | -16.3 |  |
| rlm_quiet | close | pin $2k+ | 57-69 | 45.2 | 7.2 | 5.6 |  |
| rlm_quiet | close | pin limit <$1k | 40-43 | 48.2 | -1.0 | -7.6 |  |
| pin_move | close | 1-3k bets | 339-340 | 49.9 | 0.1 | -3.0 |  |
| pin_move | close | 3k+ bets | 125-127 | 49.6 | -0.1 | -4.1 |  |
| pin_move | close | <1k bets | 72-77 | 48.3 | -2.1 | -7.4 |  |
| pin_move | close | pin $1-2k | 254-250 | 50.4 | 0.3 | -1.3 |  |
| pin_move | close | pin $2k+ | 189-198 | 48.8 | -0.9 | -7.3 |  |
| pin_move | close | pin limit <$1k | 93-96 | 49.2 | -0.3 | -3.5 |  |
| money_delta | close | 1-3k bets | 215-272 | 44.1 | -0.5 | -6.8 |  |
| money_delta | close | 3k+ bets | 84-111 | 43.1 | -0.2 | -1.5 |  |
| money_delta | close | <1k bets | 42-68 | 38.2 | -3.6 | -19.0 |  |
| money_delta | close | pin $1-2k | 122-123 | 49.8 | 4.2 | 5.1 |  |
| money_delta | close | pin $2k+ | 85-115 | 42.5 | 1.4 | -9.4 |  |
| money_delta | close | pin limit <$1k | 53-61 | 46.5 | -2.6 | -7.0 |  |
| pin_rlm | close | 1-3k bets | 91-101 | 47.4 | 4.7 | 14.4 |  |
| pin_rlm | close | 3k+ bets | 34-44 | 43.6 | 1.4 | -4.8 |  |
| pin_rlm | close | <1k bets | 22-25 | 46.8 | 5.9 | 3.2 |  |
| pin_rlm | close | pin $1-2k | 66-67 | 49.6 | 6.1 | 13.2 |  |
| pin_rlm | close | pin $2k+ | 39-66 | 37.1 | 1.0 | -2.5 |  |
| pin_rlm | close | pin limit <$1k | 42-37 | 53.2 | 4.7 | 13.2 |  |
| follow_move | close | 1-3k bets | 599-548 | 52.2 | 1.0 | -5.1 |  |
| follow_move | close | 3k+ bets | 199-185 | 51.8 | -0.0 | -5.1 |  |
| follow_move | close | <1k bets | 128-125 | 50.6 | -2.2 | -14.6 |  |
| follow_move | close | pin $1-2k | 283-308 | 47.9 | -3.0 | -10.4 |  |
| follow_move | close | pin $2k+ | 240-199 | 54.7 | 2.8 | -0.8 |  |
| follow_move | close | pin limit <$1k | 114-118 | 49.1 | -0.7 | -6.2 |  |
| rlm_ratio | close | 1-3k bets | 135-178 | 43.1 | -1.1 | -7.9 |  |
| rlm_ratio | close | 3k+ bets | 51-46 | 52.6 | 8.1 | 12.4 |  |
| rlm_ratio | close | <1k bets | 28-31 | 47.5 | 4.5 | -4.7 |  |
| rlm_ratio | close | pin $1-2k | 77-75 | 50.7 | 4.8 | 5.4 |  |
| rlm_ratio | close | pin $2k+ | 39-54 | 41.9 | 3.7 | -7.1 |  |
| rlm_ratio | close | pin limit <$1k | 47-42 | 52.8 | 4.0 | 2.0 |  |
| money_level | close | 1-3k bets | 760-542 | 58.4 | 2.8 | -2.0 |  |
| money_level | close | 3k+ bets | 255-204 | 55.6 | 0.4 | -3.6 |  |
| money_level | close | <1k bets | 162-123 | 56.8 | 1.2 | -7.4 |  |
| money_level | close | pin $1-2k | 344-297 | 53.7 | -0.3 | -4.5 |  |
| money_level | close | pin $2k+ | 295-230 | 56.2 | -1.2 | -7.4 |  |
| money_level | close | pin limit <$1k | 136-132 | 50.7 | 0.4 | -3.5 |  |
| sharp_gap | close | 1-3k bets | 561-681 | 45.2 | -2.2 | -9.9 |  |
| sharp_gap | close | 3k+ bets | 219-231 | 48.7 | 1.2 | 2.2 |  |
| sharp_gap | close | <1k bets | 125-146 | 46.1 | -1.5 | -11.7 |  |
| sharp_gap | close | pin $1-2k | 295-324 | 47.7 | -0.9 | -4.7 |  |
| sharp_gap | close | pin $2k+ | 234-270 | 46.4 | -0.1 | -3.7 |  |
| sharp_gap | close | pin limit <$1k | 118-138 | 46.1 | -3.2 | -8.1 |  |
| money_moving | close | 1-3k bets | 569-678 | 45.6 | -2.3 | -10.0 |  |
| money_moving | close | 3k+ bets | 218-233 | 48.3 | 0.5 | 0.7 |  |
| money_moving | close | <1k bets | 123-146 | 45.7 | -1.6 | -10.7 |  |
| money_moving | close | pin $1-2k | 294-326 | 47.4 | -1.5 | -5.2 |  |
| money_moving | close | pin $2k+ | 235-268 | 46.7 | 0.2 | -3.6 |  |
| money_moving | close | pin limit <$1k | 116-144 | 44.6 | -4.7 | -11.0 |  |
| pin_value | close | 1-3k bets | 248-249 | 49.9 | 1.8 | 3.9 |  |
| pin_value | close | 3k+ bets | 82-89 | 48.0 | -0.8 | -6.1 |  |
| pin_value | close | <1k bets | 62-45 | 57.9 | 10.6 | 18.8 |  |
| pin_value | close | pin $1-2k | 180-196 | 47.9 | -0.5 | -2.1 |  |
| pin_value | close | pin $2k+ | 108-119 | 47.6 | 1.3 | 3.2 |  |
| pin_value | close | pin limit <$1k | 104-68 | 60.5 | 10.4 | 17.2 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.7 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.7 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 240-297 | 44.7 | -4.0 | -11.2 |  |
| consensus_gap | close | 3k+ bets | 83-97 | 46.1 | -1.7 | 4.6 |  |
| consensus_gap | close | <1k bets | 46-79 | 36.8 | -7.4 | -23.3 |  |
| consensus_gap | close | pin $1-2k | 114-128 | 47.1 | -2.4 | -1.5 |  |
| consensus_gap | close | pin $2k+ | 100-107 | 48.3 | -2.1 | -1.5 |  |
| consensus_gap | close | pin limit <$1k | 54-45 | 54.5 | 4.2 | 6.4 |  |
| consensus_gap+follow_move | close | 1-3k bets | 99-91 | 52.1 | 0.2 | -2.6 |  |
| consensus_gap+money_level | close | 1-3k bets | 162-105 | 60.7 | 1.7 | 3.5 |  |
| consensus_gap+money_moving | close | 1-3k bets | 106-163 | 39.4 | -6.6 | -11.8 |  |
| consensus_gap+pin_move | close | 1-3k bets | 58-56 | 50.9 | -0.7 | 3.1 |  |
| consensus_gap+pin_value | close | 1-3k bets | 96-108 | 47.1 | 0.6 | -1.0 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 103-166 | 38.3 | -6.8 | -12.9 |  |
| follow_move+money_level | close | 1-3k bets | 394-276 | 58.8 | 2.7 | -3.6 |  |
| follow_move+money_moving | close | 1-3k bets | 322-353 | 47.7 | -1.5 | -9.1 |  |
| follow_move+pin_move | close | 1-3k bets | 245-252 | 49.3 | -0.6 | -6.2 |  |
| follow_move+pin_value | close | 1-3k bets | 82-81 | 50.3 | 1.7 | 1.2 |  |
| follow_move+sharp_gap | close | 1-3k bets | 324-353 | 47.9 | -1.0 | -7.9 |  |
| money_level+money_moving | close | 1-3k bets | 409-364 | 52.9 | 0.4 | -4.3 |  |
| money_level+pin_move | close | 1-3k bets | 206-186 | 52.6 | -0.2 | -4.3 |  |
| money_level+pin_value | close | 1-3k bets | 120-108 | 52.6 | 2.9 | -1.2 |  |
| money_level+sharp_gap | close | 1-3k bets | 394-357 | 52.5 | 0.3 | -4.1 |  |
| money_moving+pin_move | close | 1-3k bets | 202-220 | 47.9 | -1.1 | -3.8 |  |
| money_moving+pin_value | close | 1-3k bets | 105-131 | 44.5 | -3.0 | -7.9 |  |
| money_moving+sharp_gap | close | 1-3k bets | 538-650 | 45.3 | -2.3 | -9.4 |  |
| pin_move+pin_value | close | 1-3k bets | 106-104 | 50.5 | 1.3 | -0.9 |  |
| pin_move+sharp_gap | close | 1-3k bets | 207-222 | 48.3 | -0.4 | -2.6 |  |
| pin_value+sharp_gap | close | 1-3k bets | 106-134 | 44.2 | -3.1 | -8.6 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 135-201 | 40.2 | -1.6 | -7.4 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 68-122 | 35.8 | -5.6 | -15.9 |  |
| consensus_gap+money_delta | close | 1-3k bets | 27-66 | 29.0 | -8.7 | -22.4 |  |
| follow_move+money_delta | close | 1-3k bets | 104-125 | 45.4 | -1.1 | -9.9 |  |
| money_delta+money_level | close | 1-3k bets | 77-74 | 51.0 | 3.3 | 5.4 |  |
| money_delta+money_moving | close | 1-3k bets | 151-215 | 41.3 | -1.7 | -9.6 |  |
| money_delta+pin_value | close | 1-3k bets | 47-46 | 50.5 | 3.1 | 1.0 |  |
| money_delta+sharp_gap | close | 1-3k bets | 150-212 | 41.4 | -1.5 | -9.2 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 75-83 | 47.5 | 0.4 | 1.2 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 18-28 | 39.1 | -0.0 | 15.8 |  |
| money_level+pin_rlm | close | 1-3k bets | 41-31 | 56.9 | 8.8 | 9.8 |  |
| pin_move+pin_rlm | close | 1-3k bets | 83-84 | 49.7 | 5.2 | 10.3 |  |
| pin_rlm+pin_value | close | 1-3k bets | 29-25 | 53.7 | 7.6 | 28.3 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 91-101 | 47.4 | 4.7 | 14.4 |  |
| money_delta+pin_rlm | close | 1-3k bets | 52-57 | 47.7 | 4.5 | 13.4 |  |
| money_moving+pin_rlm | close | 1-3k bets | 86-97 | 47.0 | 4.2 | 14.5 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 21-34 | 38.2 | -1.6 | -0.2 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 135-178 | 43.1 | -1.1 | -7.9 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 73-88 | 45.3 | 0.1 | -8.8 |  |
| money_level+rlm_ratio | close | 1-3k bets | 63-60 | 51.2 | 2.4 | -1.1 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 129-171 | 43.0 | -1.4 | -7.9 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 135-178 | 43.1 | -1.1 | -7.9 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 15-36 | 29.4 | -6.5 | -12.2 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 61-118 | 34.1 | -7.4 | -18.8 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 54-105 | 34.0 | -6.1 | -16.9 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 61-80 | 43.3 | -0.6 | -7.5 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 37-65 | 36.3 | -7.2 | -24.0 |  |
| follow_move+pin_rlm | close | 1-3k bets | 66-77 | 46.2 | 1.9 | -4.5 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 71-72 | 49.7 | 4.2 | 2.2 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 26-45 | 36.6 | -3.7 | -16.3 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 66-77 | 46.2 | 1.9 | -4.5 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 27-21 | 56.2 | 8.5 | 8.0 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 17-22 | 43.6 | -1.6 | 9.5 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 50.7 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 31-27 | 53.4 | 3.2 | 3.8 |  |
| consensus_gap+money_moving | close | 3k+ bets | 34-54 | 38.6 | -6.2 | 12.1 |  |
| consensus_gap+pin_move | close | 3k+ bets | 21-19 | 52.5 | 2.1 | 6.4 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-6 | 33.3 | -7.1 | 6.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 35-33 | 51.5 | 4.6 | 5.6 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -1.4 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 35-54 | 39.3 | -5.3 | 15.1 |  |
| follow_move+money_moving | close | 3k+ bets | 106-109 | 49.3 | 0.1 | -3.4 |  |
| follow_move+pin_move | close | 3k+ bets | 95-92 | 50.8 | 0.7 | -1.2 |  |
| follow_move+pin_rlm | close | 3k+ bets | 32-30 | 51.6 | 7.5 | 13.7 |  |
| follow_move+pin_value | close | 3k+ bets | 32-33 | 49.2 | -0.9 | -7.6 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 51-46 | 52.6 | 8.1 | 12.4 |  |
| follow_move+sharp_gap | close | 3k+ bets | 108-108 | 50.0 | 1.2 | -1.4 |  |
| money_moving+pin_move | close | 3k+ bets | 72-82 | 46.8 | -1.5 | -7.2 |  |
| money_moving+pin_rlm | close | 3k+ bets | 33-43 | 43.4 | 1.5 | -4.9 |  |
| money_moving+pin_value | close | 3k+ bets | 40-51 | 44.0 | -3.7 | -9.8 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 49-44 | 52.7 | 8.2 | 13.0 |  |
| money_moving+sharp_gap | close | 3k+ bets | 211-223 | 48.6 | 1.1 | 1.9 |  |
| pin_move+pin_rlm | close | 3k+ bets | 32-38 | 45.7 | 1.9 | -0.1 |  |
| pin_move+pin_value | close | 3k+ bets | 32-41 | 43.8 | -5.8 | -17.6 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 34-31 | 52.3 | 6.9 | 13.3 |  |
| pin_move+sharp_gap | close | 3k+ bets | 72-82 | 46.8 | -1.2 | -6.5 |  |
| pin_rlm+pin_value | close | 3k+ bets | 6-14 | 30.0 | -15.9 | -42.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 32-30 | 51.6 | 7.5 | 13.7 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 34-44 | 43.6 | 1.4 | -4.8 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 9-9 | 50.0 | -0.1 | -5.1 |  |
| pin_value+sharp_gap | close | 3k+ bets | 40-50 | 44.4 | -3.2 | -8.8 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 51-46 | 52.6 | 8.1 | 12.4 |  |
| follow_move+money_delta | close | 3k+ bets | 40-49 | 44.9 | -0.4 | -7.0 |  |
| money_level+money_moving | close | 3k+ bets | 148-129 | 53.4 | 1.2 | -1.2 |  |
| money_level+sharp_gap | close | 3k+ bets | 147-126 | 53.8 | 1.8 | 0.2 |  |
| follow_move+money_level | close | 3k+ bets | 124-92 | 57.4 | 1.0 | -2.9 |  |
| money_level+rlm_ratio | close | 3k+ bets | 25-12 | 67.6 | 20.4 | 38.4 |  |
| consensus_gap+money_level | close | 3k+ bets | 46-45 | 50.5 | -6.3 | -12.7 |  |
| money_level+pin_move | close | 3k+ bets | 68-63 | 51.9 | -1.6 | -4.7 |  |
| money_level+pin_value | close | 3k+ bets | 46-46 | 50.0 | -0.7 | -7.3 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 7-12 | 36.8 | -1.3 | -5.4 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 46-65 | 41.4 | -1.2 | -10.0 |  |
| money_delta+money_moving | close | 3k+ bets | 64-84 | 43.2 | 1.0 | 3.6 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 19-26 | 42.2 | 0.8 | -2.3 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 23-35 | 39.7 | -2.6 | -10.9 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 21-34 | 38.2 | -4.0 | -13.1 |  |
| consensus_gap+money_delta | close | 3k+ bets | 12-23 | 34.3 | -4.5 | 18.4 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 10-26 | 27.8 | -15.1 | -38.6 |  |
| money_delta+sharp_gap | close | 3k+ bets | 62-81 | 43.4 | 1.2 | 4.3 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 27-31 | 46.6 | 2.8 | 1.3 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 11-16 | 40.7 | -1.0 | -3.2 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 7-11 | 38.9 | -10.5 | -25.7 |  |
| money_delta+money_level | close | 3k+ bets | 33-22 | 60.0 | 13.9 | 21.2 |  |
| money_level+pin_rlm | close | 3k+ bets | 16-9 | 64.0 | 19.1 | 37.0 |  |
| money_delta+pin_value | close | 3k+ bets | 18-19 | 48.6 | 2.7 | -8.3 |  |
| money_delta+pin_move | close | 3k+ bets | 36-42 | 46.2 | 1.0 | -5.7 |  |
| money_delta+pin_rlm | close | 3k+ bets | 22-27 | 44.9 | 3.0 | -4.5 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 30-25 | 54.5 | 9.9 | 15.6 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 47.7 | 87.7 |  |
| money_level+money_moving | close | <1k bets | 85-80 | 51.5 | -0.5 | -10.0 |  |
| money_level+sharp_gap | close | <1k bets | 88-80 | 52.4 | -0.0 | -9.6 |  |
| money_moving+sharp_gap | close | <1k bets | 121-144 | 45.7 | -1.7 | -11.7 |  |
| consensus_gap+money_level | close | <1k bets | 22-27 | 44.9 | -11.2 | -30.5 |  |
| consensus_gap+money_moving | close | <1k bets | 20-40 | 33.3 | -8.5 | -22.7 |  |
| consensus_gap+pin_move | close | <1k bets | 7-13 | 35.0 | -15.9 | -22.6 |  |
| consensus_gap+pin_value | close | <1k bets | 16-14 | 53.3 | 11.4 | 32.3 |  |
| consensus_gap+sharp_gap | close | <1k bets | 20-41 | 32.8 | -8.8 | -24.0 |  |
| money_level+pin_move | close | <1k bets | 37-38 | 49.3 | -4.7 | -13.3 |  |
| money_level+pin_value | close | <1k bets | 21-17 | 55.3 | 4.9 | 3.4 |  |
| money_moving+pin_move | close | <1k bets | 37-45 | 45.1 | -2.3 | -7.7 |  |
| money_moving+pin_value | close | <1k bets | 20-16 | 55.6 | 10.5 | 31.1 |  |
| pin_move+pin_value | close | <1k bets | 28-20 | 58.3 | 9.9 | 17.8 |  |
| pin_move+sharp_gap | close | <1k bets | 37-46 | 44.6 | -3.4 | -12.7 |  |
| pin_value+sharp_gap | close | <1k bets | 20-15 | 57.1 | 11.6 | 34.9 |  |
| follow_move+money_delta | close | <1k bets | 20-24 | 45.5 | 3.1 | -7.8 |  |
| follow_move+money_moving | close | <1k bets | 58-69 | 45.7 | -3.8 | -15.6 |  |
| follow_move+pin_move | close | <1k bets | 45-50 | 47.4 | -3.6 | -12.3 |  |
| follow_move+sharp_gap | close | <1k bets | 60-69 | 46.5 | -3.6 | -17.7 |  |
| money_delta+money_moving | close | <1k bets | 31-52 | 37.3 | -2.5 | -17.9 |  |
| money_delta+pin_move | close | <1k bets | 14-20 | 41.2 | -2.6 | -19.8 |  |
| money_delta+sharp_gap | close | <1k bets | 31-52 | 37.3 | -2.5 | -17.9 |  |
| follow_move+rlm_quiet | close | <1k bets | 23-37 | 38.3 | -3.5 | -18.5 |  |
| follow_move+rlm_ratio | close | <1k bets | 28-31 | 47.5 | 4.5 | -4.7 |  |
| money_delta+rlm_quiet | close | <1k bets | 9-12 | 42.9 | 2.8 | -8.9 |  |
| money_delta+rlm_ratio | close | <1k bets | 18-19 | 48.6 | 7.1 | -0.6 |  |
| money_moving+rlm_quiet | close | <1k bets | 15-16 | 48.4 | 6.8 | 7.0 |  |
| money_moving+rlm_ratio | close | <1k bets | 28-31 | 47.5 | 4.5 | -4.7 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 11-13 | 45.8 | 5.5 | -4.0 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 14-17 | 45.2 | 2.9 | -7.2 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 28-31 | 47.5 | 4.5 | -4.7 |  |
| follow_move+money_level | close | <1k bets | 80-62 | 56.3 | -1.6 | -14.3 |  |
| consensus_gap+money_delta | close | <1k bets | 6-22 | 21.4 | -11.4 | -39.3 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -2.0 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 13-17 | 43.3 | 4.3 | -7.1 |  |
| money_moving+pin_rlm | close | <1k bets | 22-25 | 46.8 | 5.9 | 3.2 |  |
| pin_rlm+sharp_gap | close | <1k bets | 22-25 | 46.8 | 5.9 | 3.2 |  |
| money_delta+pin_value | close | <1k bets | 8-8 | 50.0 | 4.7 | 16.9 |  |
| consensus_gap+follow_move | close | <1k bets | 11-20 | 35.5 | -15.3 | -43.6 |  |
| follow_move+pin_rlm | close | <1k bets | 17-15 | 53.1 | 10.0 | 5.0 |  |
| follow_move+pin_value | close | <1k bets | 20-12 | 62.5 | 13.6 | 18.7 |  |
| pin_move+pin_rlm | close | <1k bets | 20-20 | 50.0 | 6.7 | 5.4 |  |
| pin_move+rlm_quiet | close | <1k bets | 11-14 | 44.0 | -1.1 | -4.7 |  |
| pin_move+rlm_ratio | close | <1k bets | 17-17 | 50.0 | 5.2 | -2.4 |  |
| pin_rlm+pin_value | close | <1k bets | 6-3 | 66.7 | 24.8 | 64.1 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 8-7 | 53.3 | 9.7 | 5.4 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 17-15 | 53.1 | 10.0 | 5.0 |  |
| pin_value+rlm_quiet | close | <1k bets | 4-4 | 50.0 | 0.7 | -4.0 |  |
| pin_value+rlm_ratio | close | <1k bets | 5-1 | 83.3 | 34.6 | 58.3 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -6.2 | -42.5 |  |
| money_delta+money_level | close | <1k bets | 14-19 | 42.4 | -0.2 | -14.7 |  |
| money_level+rlm_ratio | close | <1k bets | 14-15 | 48.3 | 3.6 | -5.5 |  |
| money_level+pin_rlm | close | <1k bets | 9-8 | 52.9 | 11.2 | 5.0 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 0-5 | 0.0 | -35.9 | -100.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 44-51 | 46.3 | -5.9 | -11.5 |  |
| consensus_gap+money_moving | close | pin $1-2k | 56-69 | 44.8 | -3.9 | -2.7 |  |
| consensus_gap+pin_move | close | pin $1-2k | 43-46 | 48.3 | -3.9 | 2.1 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-18 | 41.9 | 0.7 | 25.8 |  |
| consensus_gap+pin_value | close | pin $1-2k | 67-74 | 47.5 | 1.2 | -2.3 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-15 | 48.3 | 3.0 | 5.2 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 53-67 | 44.2 | -3.2 | -1.9 |  |
| follow_move+money_moving | close | pin $1-2k | 164-192 | 46.1 | -3.6 | -9.9 |  |
| follow_move+pin_move | close | pin $1-2k | 178-190 | 48.4 | -1.9 | -6.9 |  |
| follow_move+pin_rlm | close | pin $1-2k | 54-51 | 51.4 | 6.0 | 7.7 |  |
| follow_move+pin_value | close | pin $1-2k | 59-70 | 45.7 | -3.7 | -13.7 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 77-75 | 50.7 | 4.8 | 5.4 |  |
| follow_move+sharp_gap | close | pin $1-2k | 167-192 | 46.5 | -2.9 | -9.5 |  |
| money_moving+pin_move | close | pin $1-2k | 152-167 | 47.6 | -1.4 | -3.3 |  |
| money_moving+pin_rlm | close | pin $1-2k | 63-64 | 49.6 | 5.7 | 13.7 |  |
| money_moving+pin_value | close | pin $1-2k | 70-101 | 40.9 | -6.9 | -17.8 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 75-71 | 51.4 | 5.1 | 6.7 |  |
| money_moving+sharp_gap | close | pin $1-2k | 284-314 | 47.5 | -1.2 | -4.7 |  |
| pin_move+pin_rlm | close | pin $1-2k | 63-61 | 50.8 | 6.1 | 13.4 |  |
| pin_move+pin_value | close | pin $1-2k | 75-90 | 45.5 | -4.1 | -12.3 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 62-55 | 53.0 | 6.6 | 9.3 |  |
| pin_move+sharp_gap | close | pin $1-2k | 155-168 | 48.0 | -0.7 | -3.0 |  |
| pin_rlm+pin_value | close | pin $1-2k | 16-24 | 40.0 | -8.0 | -16.9 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 54-51 | 51.4 | 6.0 | 7.7 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 66-67 | 49.6 | 6.1 | 13.2 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 19-20 | 48.7 | -0.8 | -8.0 |  |
| pin_value+sharp_gap | close | pin $1-2k | 70-99 | 41.4 | -6.3 | -16.9 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 77-75 | 50.7 | 4.8 | 5.4 |  |
| follow_move+money_level | close | pin $1-2k | 192-177 | 52.0 | -2.1 | -8.5 |  |
| money_level+rlm_ratio | close | pin $1-2k | 45-33 | 57.7 | 10.0 | 12.6 |  |
| money_level+sharp_gap | close | pin $1-2k | 212-204 | 51.0 | -0.7 | -5.3 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 4-13 | 23.5 | -17.4 | -32.4 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 55-93 | 37.2 | -6.0 | -16.3 |  |
| money_level+money_moving | close | pin $1-2k | 214-208 | 50.7 | -1.1 | -6.1 |  |
| consensus_gap+money_level | close | pin $1-2k | 67-60 | 52.8 | -4.3 | -7.1 |  |
| money_level+pin_value | close | pin $1-2k | 78-82 | 48.8 | -1.3 | -8.8 |  |
| money_level+pin_move | close | pin $1-2k | 152-140 | 52.1 | -0.6 | -4.8 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 26-40 | 39.4 | -4.5 | -4.7 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 41-53 | 43.6 | -1.4 | -2.5 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 17-27 | 38.6 | -5.4 | -8.0 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 22-34 | 39.3 | -3.5 | -5.0 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 27-43 | 38.6 | -4.7 | -9.5 |  |
| money_level+pin_rlm | close | pin $1-2k | 32-23 | 58.2 | 12.4 | 14.4 |  |
| follow_move+money_delta | close | pin $1-2k | 61-63 | 49.2 | 3.3 | 1.0 |  |
| money_delta+money_moving | close | pin $1-2k | 84-94 | 47.2 | 3.1 | 3.7 |  |
| money_delta+pin_move | close | pin $1-2k | 64-65 | 49.6 | 2.7 | 4.6 |  |
| money_delta+pin_rlm | close | pin $1-2k | 41-42 | 49.4 | 6.2 | 12.8 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 47-42 | 52.8 | 7.4 | 10.4 |  |
| money_delta+sharp_gap | close | pin $1-2k | 84-92 | 47.7 | 3.6 | 4.8 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 47.7 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 45-37 | 54.9 | 7.5 | 6.9 |  |
| consensus_gap+money_delta | close | pin $1-2k | 17-26 | 39.5 | -1.2 | 0.6 |  |
| money_delta+pin_value | close | pin $1-2k | 40-44 | 47.6 | -0.5 | -5.6 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 16-31 | 34.0 | -9.5 | -20.4 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 10-23 | 30.3 | -18.6 | -41.9 |  |
| follow_move+money_level | close | pin $2k+ | 146-93 | 61.1 | 1.7 | -2.6 |  |
| follow_move+money_moving | close | pin $2k+ | 113-110 | 50.7 | 2.6 | -3.3 |  |
| follow_move+pin_move | close | pin $2k+ | 144-135 | 51.6 | 1.4 | -3.0 |  |
| follow_move+sharp_gap | close | pin $2k+ | 114-111 | 50.7 | 2.7 | -3.0 |  |
| money_level+money_moving | close | pin $2k+ | 157-143 | 52.3 | -0.5 | -5.4 |  |
| money_level+pin_move | close | pin $2k+ | 106-94 | 53.0 | -2.6 | -7.0 |  |
| money_level+sharp_gap | close | pin $2k+ | 157-144 | 52.2 | -0.7 | -5.4 |  |
| money_moving+pin_move | close | pin $2k+ | 98-109 | 47.3 | -0.1 | -5.8 |  |
| money_moving+sharp_gap | close | pin $2k+ | 229-264 | 46.5 | 0.0 | -3.6 |  |
| pin_move+sharp_gap | close | pin $2k+ | 98-110 | 47.1 | -0.4 | -5.8 |  |
| consensus_gap+money_delta | close | pin $2k+ | 7-25 | 21.9 | -10.6 | -56.9 |  |
| consensus_gap+money_moving | close | pin $2k+ | 35-62 | 36.1 | -8.8 | -7.3 |  |
| consensus_gap+pin_value | close | pin $2k+ | 41-48 | 46.1 | 3.4 | 10.0 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 37-65 | 36.3 | -9.0 | -6.7 |  |
| money_delta+money_moving | close | pin $2k+ | 59-83 | 41.5 | 3.1 | -7.8 |  |
| money_delta+pin_value | close | pin $2k+ | 18-21 | 46.2 | 3.3 | -11.8 |  |
| money_delta+sharp_gap | close | pin $2k+ | 57-82 | 41.0 | 2.5 | -8.8 |  |
| money_moving+pin_value | close | pin $2k+ | 56-67 | 45.5 | 0.3 | 3.9 |  |
| pin_value+sharp_gap | close | pin $2k+ | 56-68 | 45.2 | 0.1 | 3.0 |  |
| consensus_gap+pin_move | close | pin $2k+ | 28-31 | 47.5 | -3.6 | -11.9 |  |
| money_delta+pin_move | close | pin $2k+ | 31-45 | 40.8 | -1.7 | -16.0 |  |
| consensus_gap+follow_move | close | pin $2k+ | 32-26 | 55.2 | 1.5 | -8.5 |  |
| follow_move+pin_value | close | pin $2k+ | 35-31 | 53.0 | 5.7 | 15.0 |  |
| pin_move+pin_value | close | pin $2k+ | 48-47 | 50.5 | 2.6 | -1.0 |  |
| follow_move+money_delta | close | pin $2k+ | 31-40 | 43.7 | 1.8 | -9.3 |  |
| follow_move+pin_rlm | close | pin $2k+ | 28-42 | 40.0 | 2.2 | -8.6 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 39-54 | 41.9 | 3.7 | -7.1 |  |
| money_delta+money_level | close | pin $2k+ | 25-20 | 55.6 | 11.7 | 12.4 |  |
| money_delta+pin_rlm | close | pin $2k+ | 21-37 | 36.2 | 0.3 | -9.9 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 19-25 | 43.2 | 4.5 | -6.2 |  |
| money_level+pin_rlm | close | pin $2k+ | 15-10 | 60.0 | 16.2 | 27.1 |  |
| money_level+pin_value | close | pin $2k+ | 56-53 | 51.4 | 1.5 | -5.0 |  |
| money_level+rlm_ratio | close | pin $2k+ | 14-12 | 53.8 | 8.2 | 13.1 |  |
| money_moving+pin_rlm | close | pin $2k+ | 39-66 | 37.1 | 1.0 | -2.5 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 39-53 | 42.4 | 4.0 | -6.1 |  |
| pin_move+pin_rlm | close | pin $2k+ | 31-44 | 41.3 | 3.0 | -3.2 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 27-36 | 42.9 | 2.8 | -2.2 |  |
| pin_rlm+pin_value | close | pin $2k+ | 6-13 | 31.6 | -4.7 | 13.6 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 28-42 | 40.0 | 2.2 | -8.6 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 39-66 | 37.1 | 1.0 | -2.5 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 4-6 | 40.0 | -1.2 | -19.0 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 39-54 | 41.9 | 3.7 | -7.1 |  |
| consensus_gap+money_level | close | pin $2k+ | 66-48 | 57.9 | -4.9 | -9.4 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 57-69 | 45.2 | 7.2 | 5.6 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 16-21 | 43.2 | 4.4 | -10.0 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 27-37 | 42.2 | 6.3 | -5.0 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 13-27 | 32.5 | -0.3 | -20.0 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 20-33 | 37.7 | 4.6 | -11.5 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 27-38 | 41.5 | 5.8 | -6.5 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-20 | 16.7 | -14.6 | -27.9 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 4-12 | 25.0 | -3.7 | -46.7 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-11 | 0.0 | -29.7 | -100.0 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 36-46 | 43.9 | 4.0 | -3.6 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 5-7 | 41.7 | 5.2 | 64.1 |  |
| follow_move+money_delta | close | pin limit <$1k | 34-42 | 44.7 | -4.3 | -14.1 |  |
| money_level+money_moving | close | pin limit <$1k | 71-85 | 45.5 | -4.2 | -12.7 |  |
| money_level+sharp_gap | close | pin limit <$1k | 68-79 | 46.3 | -3.4 | -11.2 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 107-129 | 45.3 | -3.9 | -9.2 |  |
| consensus_gap+money_level | close | pin limit <$1k | 30-26 | 53.6 | 2.6 | -0.9 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 15-11 | 57.7 | 9.3 | 25.7 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 39-33 | 54.2 | 4.4 | 8.1 |  |
| follow_move+money_moving | close | pin limit <$1k | 68-85 | 44.4 | -4.8 | -14.6 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 73-84 | 46.5 | -2.8 | -10.7 |  |
| money_level+pin_move | close | pin limit <$1k | 53-53 | 50.0 | 0.1 | -4.5 |  |
| money_level+pin_value | close | pin limit <$1k | 53-36 | 59.6 | 9.3 | 12.8 |  |
| pin_move+pin_value | close | pin limit <$1k | 43-28 | 60.6 | 10.7 | 21.4 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 20-11 | 64.5 | 14.8 | 19.2 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 24-19 | 55.8 | 6.8 | 16.0 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 26-19 | 57.8 | 8.7 | 19.1 |  |
| follow_move+money_level | close | pin limit <$1k | 57-61 | 48.3 | -1.9 | -8.0 |  |
| follow_move+pin_move | close | pin limit <$1k | 63-69 | 47.7 | -1.7 | -8.5 |  |
| follow_move+pin_value | close | pin limit <$1k | 40-25 | 61.5 | 11.7 | 16.8 |  |
| money_moving+pin_move | close | pin limit <$1k | 61-71 | 46.2 | -3.0 | -8.2 |  |
| money_moving+pin_value | close | pin limit <$1k | 39-30 | 56.5 | 6.8 | 13.7 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 63-72 | 46.7 | -2.5 | -7.4 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 40-32 | 55.6 | 5.8 | 11.6 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 40-43 | 48.2 | -1.0 | -7.6 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 27-31 | 46.6 | -2.3 | -10.7 |  |
| money_delta+money_moving | close | pin limit <$1k | 46-51 | 47.4 | -1.6 | -4.6 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 9-6 | 60.0 | 13.2 | 43.2 |  |
| money_delta+money_level | close | pin limit <$1k | 25-22 | 53.2 | 3.6 | 1.9 |  |
| money_delta+pin_value | close | pin limit <$1k | 15-8 | 65.2 | 16.2 | 42.9 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 45-49 | 47.9 | -1.0 | -3.7 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 30-35 | 46.2 | -2.5 | -4.7 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 7-3 | 70.0 | 24.4 | 77.3 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 25-22 | 53.2 | 5.0 | 11.5 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 39-35 | 52.7 | 4.3 | 13.1 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 41-37 | 52.6 | 3.8 | 6.5 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-5 | 79.2 | 30.3 | 69.5 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 42-37 | 53.2 | 4.7 | 13.2 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 6-1 | 85.7 | 39.1 | 63.9 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 13-7 | 65.0 | 15.3 | 24.4 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 11-19 | 36.7 | -11.5 | -29.6 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 22-26 | 45.8 | -3.0 | -11.9 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 33-29 | 53.2 | 4.4 | 2.5 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 47-42 | 52.8 | 4.0 | 2.0 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 28-26 | 51.9 | 3.1 | -0.3 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 21-30 | 41.2 | -7.5 | -20.8 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 43-40 | 51.8 | 3.0 | 0.1 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 33-29 | 53.2 | 4.4 | 2.5 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 15-14 | 51.7 | 3.7 | -0.5 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 33-29 | 53.2 | 4.4 | 2.5 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 23-23 | 50.0 | 1.4 | -4.0 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 47-42 | 52.8 | 4.0 | 2.0 |  |
| money_level+pin_rlm | close | pin limit <$1k | 19-15 | 55.9 | 6.4 | 7.2 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 21-17 | 55.3 | 6.3 | 7.5 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 18-5 | 78.3 | 28.5 | 49.8 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 7-3 | 70.0 | 22.2 | 33.8 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 50.7 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.1 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -51.5 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 33-35 | 48.5 | 13.0 | 17.8 | 0.29 |
| rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -15.0 | -3.3 | -0.95 |
| rlm_quiet | early | pin limit <$1k | 5-7 | 41.7 | -2.5 | -15.0 | 0.27 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.7 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 5-8 | 38.5 | -9.6 | -31.5 | 0.32 |
| pin_move | early | pin $1-2k | 0-3 | 0.0 | -35.8 | -100.0 | 0.23 |
| pin_move | early | pin limit <$1k | 5-6 | 45.5 | -6.2 | -19.1 | 0.22 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.4 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 8-7 | 53.3 | 12.6 | 18.2 | -0.18 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -39.9 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 4-0 | 100.0 | 50.7 | 88.0 | -0.25 |
| pin_rlm | early | <1k bets | 1-2 | 33.3 | 5.8 | -35.8 | -1.0 |
| pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -27.5 | -100.0 | -1.75 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.5 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.4 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -51.5 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 428-365 | 54.0 | 2.0 | -5.3 | 0.19 |
| follow_move | early | pin $1-2k | 28-17 | 62.2 | 9.3 | 12.3 | -0.38 |
| follow_move | early | pin limit <$1k | 48-39 | 55.2 | 4.9 | 2.9 | -0.14 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.5 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.3 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 27-19 | 58.7 | 20.7 | 29.1 | 0.63 |
| rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 2.6 | 55.6 | -1.52 |
| rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 1.3 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 43.5 | 59.7 | 0.33 |
| money_level | early | <1k bets | 153-104 | 59.5 | -0.2 | -6.9 | -0.14 |
| money_level | early | pin $1-2k | 20-8 | 71.4 | 6.4 | 4.1 | 0.01 |
| money_level | early | pin limit <$1k | 24-26 | 48.0 | -5.1 | -11.4 | 0.22 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.5 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.6 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 127-111 | 53.4 | 5.2 | 3.2 | 0.36 |
| sharp_gap | early | pin $1-2k | 15-11 | 57.7 | 4.8 | 6.7 | -0.39 |
| sharp_gap | early | pin limit <$1k | 29-18 | 61.7 | 13.1 | 27.9 | 0.12 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.6 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 51.5 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 90-79 | 53.3 | 1.9 | -5.6 | 0.09 |
| money_moving | early | pin $1-2k | 8-8 | 50.0 | -8.2 | -31.4 | 0.21 |
| money_moving | early | pin limit <$1k | 23-9 | 71.9 | 22.8 | 52.0 | 0.42 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.9 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.3 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 38-40 | 48.7 | 0.3 | -7.8 | 0.11 |
| pin_value | early | pin $1-2k | 14-19 | 42.4 | -3.5 | -20.3 | 0.14 |
| pin_value | early | pin limit <$1k | 37-30 | 55.2 | 5.6 | 4.5 | 0.06 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -50.7 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -26.6 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.3 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.4 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 197-251 | 44.0 | -4.0 | -12.9 | 0.36 |
| consensus_gap | early | pin $1-2k | 12-20 | 37.5 | -8.0 | -28.2 | 0.51 |
| consensus_gap | early | pin limit <$1k | 18-34 | 34.6 | -15.6 | -28.2 | 0.28 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -52.3 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.4 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.4 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -1.5 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.5 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 5.4 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.4 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 17.1 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.4 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.9 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.7 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -1.1 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 3.6 | -6.9 | 0.3 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -0.9 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-6 | 53.8 | 6.8 | 0.8 | -0.31 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.1 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.6 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -20.6 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.7 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 3.1 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.6 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.5 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.9 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.5 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.2 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 50.8 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.5 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 50.8 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 52.3 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 11.7 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 18.5 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 16.7 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 16.7 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -27.5 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.3 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.3 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.3 | 83.3 | 1.0 |
| follow_move+rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -51.5 | -100.0 | -0.5 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.3 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.3 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 51.5 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.3 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.3 | 83.3 | 1.0 |
| rlm_quiet+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.3 | -100.0 | -1.0 |
| rlm_quiet+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.3 | -100.0 | -1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.3 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 39.1 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 50.7 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 29-37 | 43.9 | -8.5 | -20.8 | 0.86 |
| consensus_gap+money_level | early | <1k bets | 32-25 | 56.1 | -8.7 | -13.4 | 0.32 |
| consensus_gap+sharp_gap | early | <1k bets | 25-40 | 38.5 | -8.6 | -16.8 | 0.96 |
| follow_move+money_level | early | <1k bets | 78-40 | 66.1 | 5.2 | -2.6 | 0.02 |
| follow_move+sharp_gap | early | <1k bets | 68-35 | 66.0 | 16.4 | 18.1 | 0.51 |
| money_level+sharp_gap | early | <1k bets | 83-53 | 61.0 | 4.6 | -0.6 | 0.17 |
| follow_move+money_moving | early | <1k bets | 47-29 | 61.8 | 8.7 | 9.2 | 0.39 |
| money_level+money_moving | early | <1k bets | 54-41 | 56.8 | -1.9 | -10.7 | -0.19 |
| money_moving+sharp_gap | early | <1k bets | 53-47 | 53.0 | 4.1 | -2.8 | 0.29 |
| consensus_gap+money_moving | early | <1k bets | 13-20 | 39.4 | -10.5 | -38.2 | 0.24 |
| follow_move+pin_value | early | <1k bets | 14-11 | 56.0 | 6.2 | 4.8 | -0.09 |
| follow_move+rlm_quiet | early | <1k bets | 33-35 | 48.5 | 13.0 | 17.8 | 0.29 |
| money_moving+rlm_quiet | early | <1k bets | 14-9 | 60.9 | 24.0 | 44.9 | 0.61 |
| rlm_quiet+sharp_gap | early | <1k bets | 20-14 | 58.8 | 22.4 | 31.4 | -0.0 |
| follow_move+rlm_ratio | early | <1k bets | 27-19 | 58.7 | 20.7 | 29.1 | 0.63 |
| rlm_quiet+rlm_ratio | early | <1k bets | 18-11 | 62.1 | 25.6 | 40.9 | 0.03 |
| rlm_ratio+sharp_gap | early | <1k bets | 27-19 | 58.7 | 20.7 | 29.1 | 0.63 |
| pin_move+pin_value | early | <1k bets | 1-4 | 20.0 | -29.2 | -61.8 | 0.2 |
| follow_move+pin_move | early | <1k bets | 5-3 | 62.5 | 10.7 | 11.2 | 0.42 |
| consensus_gap+pin_value | early | <1k bets | 13-23 | 36.1 | -10.6 | -32.5 | 0.4 |
| pin_value+rlm_quiet | early | <1k bets | 0-3 | 0.0 | -43.0 | -100.0 | -0.6 |
| money_delta+money_moving | early | <1k bets | 7-7 | 50.0 | 9.9 | 13.0 | -0.19 |
| money_delta+sharp_gap | early | <1k bets | 6-5 | 54.5 | 15.0 | 26.5 | -0.25 |
| consensus_gap+pin_move | early | <1k bets | 0-5 | 0.0 | -44.6 | -100.0 | 0.26 |
| money_level+pin_move | early | <1k bets | 2-2 | 50.0 | -5.8 | -21.8 | 0.1 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -27.5 | -100.0 | -4.8 |
| consensus_gap+rlm_quiet | early | <1k bets | 3-5 | 37.5 | -0.9 | -22.7 | 1.01 |
| consensus_gap+rlm_ratio | early | <1k bets | 4-3 | 57.1 | 17.2 | 15.6 | 0.6 |
| follow_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 22.5 | -3.7 | -2.15 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -27.5 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | <1k bets | 0-1 | 0.0 | -27.5 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 22.5 | -3.7 | -2.15 |
| pin_rlm+sharp_gap | early | <1k bets | 1-2 | 33.3 | 5.8 | -35.8 | -1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 11.6 | -4.5 | -1.9 |
| pin_value+sharp_gap | early | <1k bets | 5-4 | 55.6 | 8.2 | 6.1 | -0.09 |
| money_level+pin_value | early | <1k bets | 4-4 | 50.0 | -0.2 | -4.5 | 0.88 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -50.8 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -49.3 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 1-2 | 33.3 | -17.4 | -36.4 | 1.33 |
| money_level+rlm_ratio | early | <1k bets | 7-8 | 46.7 | 7.2 | -2.1 | 1.93 |
| money_moving+rlm_ratio | early | <1k bets | 13-8 | 61.9 | 19.7 | 39.1 | 0.8 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 49.3 | 90.9 | 0.0 |
| money_delta+money_level | early | <1k bets | 3-2 | 60.0 | 14.8 | 29.2 | 1.36 |
| pin_move+sharp_gap | early | <1k bets | 2-1 | 66.7 | 16.4 | 4.3 | -0.07 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 72.5 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 72.5 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 72.5 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 3-4 | 42.9 | 2.9 | 17.8 | 0.34 |
| money_delta+rlm_quiet | early | <1k bets | 1-2 | 33.3 | -1.4 | 23.3 | -2.8 |
| money_delta+rlm_ratio | early | <1k bets | 2-2 | 50.0 | 11.6 | 58.5 | 1.15 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 50.7 | 90.9 | -1.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -27.5 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 5-4 | 55.6 | -8.7 | -12.6 | 0.71 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -30.9 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 5-10 | 33.3 | -8.2 | -38.7 | 0.31 |
| follow_move+rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -15.0 | -3.3 | -0.95 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 2.6 | 55.6 | -1.52 |
| follow_move+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 14.0 | 37.5 | -0.83 |
| money_level+money_moving | early | pin $1-2k | 8-5 | 61.5 | -3.7 | -15.6 | 0.07 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.6 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -8.7 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -8.7 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-3 | 40.0 | 2.6 | 55.6 | -1.52 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -52.3 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -39.9 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -52.3 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -39.9 | -100.0 | 2.5 |
| money_level+sharp_gap | early | pin $1-2k | 12-4 | 75.0 | 10.9 | 12.5 | -0.26 |
| money_moving+sharp_gap | early | pin $1-2k | 4-6 | 40.0 | -16.5 | -45.4 | 0.08 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -9.2 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 4-6 | 40.0 | -10.0 | -31.3 | 0.34 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 0-3 | 0.0 | -27.5 | -100.0 | -0.97 |
| follow_move+pin_value | early | pin $1-2k | 6-5 | 54.5 | 7.0 | 0.8 | -0.3 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -27.5 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 11-4 | 73.3 | 8.8 | 6.6 | -0.07 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 47.7 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 4-1 | 80.0 | 12.5 | 6.9 | -0.18 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -27.5 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -27.5 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -16.7 | -46.8 | -0.12 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -27.5 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -27.5 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | pin $1-2k | 0-1 | 0.0 | -27.5 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -27.5 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -27.5 | -100.0 | -1.75 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -27.5 | -100.0 | -4.8 |
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -27.5 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -27.5 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin limit <$1k | 5-7 | 41.7 | -2.5 | -15.0 | 0.27 |
| money_level+money_moving | early | pin limit <$1k | 13-7 | 65.0 | 13.0 | 20.2 | 0.48 |
| money_level+sharp_gap | early | pin limit <$1k | 20-16 | 55.6 | 5.1 | 1.6 | 0.14 |
| money_moving+sharp_gap | early | pin limit <$1k | 18-5 | 78.3 | 30.3 | 70.1 | 0.35 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -50.7 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 9-6 | 60.0 | 10.2 | 13.8 | 0.33 |
| money_moving+pin_value | early | pin limit <$1k | 7-4 | 63.6 | 14.0 | 20.1 | 0.18 |
| pin_value+sharp_gap | early | pin limit <$1k | 12-6 | 66.7 | 16.9 | 26.4 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-9 | 40.0 | -12.1 | -25.7 | 0.53 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -26.2 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 14-18 | 43.8 | -5.4 | -17.9 | 0.43 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.0 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 11-11 | 50.0 | -3.6 | -7.4 | -0.04 |
| follow_move+pin_value | early | pin limit <$1k | 15-12 | 55.6 | 6.1 | 4.5 | -0.11 |
| follow_move+sharp_gap | early | pin limit <$1k | 13-7 | 65.0 | 16.5 | 24.2 | -0.07 |
| follow_move+rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level+rlm_ratio | early | pin limit <$1k | 6-0 | 100.0 | 54.1 | 92.6 | 0.42 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 16.9 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| consensus_gap+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 50.8 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 22.7 | 72.3 | 0.54 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 1.5 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 50.8 | 85.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 9-3 | 75.0 | 25.6 | 43.3 | 0.33 |
| money_delta+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 50.8 | 87.1 | -0.33 |
| money_delta+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 50.8 | 87.1 | -0.33 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 52.3 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 3-1 | 75.0 | 25.7 | 41.3 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.0 | 45.3 | -0.5 |
| money_delta+sharp_gap | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 | -0.5 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 10.9 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 24.2 | 51.6 | -0.07 |
| pin_move+pin_value | early | pin limit <$1k | 1-4 | 20.0 | -29.2 | -61.8 | 0.2 |
| follow_move+pin_move | early | pin limit <$1k | 5-3 | 62.5 | 10.7 | 11.2 | 0.42 |
| consensus_gap+pin_move | early | pin limit <$1k | 0-3 | 0.0 | -56.0 | -100.0 | 0.53 |
| money_level+pin_move | early | pin limit <$1k | 2-2 | 50.0 | -5.8 | -21.8 | 0.1 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -49.3 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -49.3 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 16.4 | 4.3 | -0.07 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.5 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.5 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.5 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 72.5 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 72.5 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 72.5 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 50.7 | 90.9 | -1.0 |
| rlm_quiet | close | 1-3k bets | 116-168 | 40.8 | -0.8 | -7.9 |  |
| rlm_quiet | close | 3k+ bets | 44-60 | 42.3 | -0.3 | -8.1 |  |
| rlm_quiet | close | <1k bets | 22-28 | 44.0 | 2.5 | -6.0 |  |
| rlm_quiet | close | pin $1-2k | 46-79 | 36.8 | -6.1 | -16.0 |  |
| rlm_quiet | close | pin $2k+ | 51-62 | 45.1 | 7.4 | -2.5 |  |
| rlm_quiet | close | pin limit <$1k | 36-36 | 50.0 | 0.1 | -4.2 |  |
| pin_move | close | 1-3k bets | 307-302 | 50.4 | 0.5 | -1.8 |  |
| pin_move | close | 3k+ bets | 120-123 | 49.4 | -0.3 | -4.6 |  |
| pin_move | close | <1k bets | 67-68 | 49.6 | -1.0 | -4.6 |  |
| pin_move | close | pin $1-2k | 233-226 | 50.8 | 0.4 | -0.5 |  |
| pin_move | close | pin $2k+ | 174-183 | 48.7 | -0.8 | -7.2 |  |
| pin_move | close | pin limit <$1k | 87-84 | 50.9 | 1.1 | -0.1 |  |
| money_delta | close | 1-3k bets | 199-251 | 44.2 | -0.5 | -6.2 |  |
| money_delta | close | 3k+ bets | 79-109 | 42.0 | -1.1 | -3.3 |  |
| money_delta | close | <1k bets | 38-62 | 38.0 | -4.1 | -22.9 |  |
| money_delta | close | pin $1-2k | 112-114 | 49.6 | 3.7 | 3.7 |  |
| money_delta | close | pin $2k+ | 82-110 | 42.7 | 1.6 | -8.9 |  |
| money_delta | close | pin limit <$1k | 50-54 | 48.1 | -1.7 | -3.7 |  |
| pin_rlm | close | 1-3k bets | 87-92 | 48.6 | 6.0 | 18.3 |  |
| pin_rlm | close | 3k+ bets | 32-44 | 42.1 | -0.0 | -7.9 |  |
| pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| pin_rlm | close | pin $1-2k | 61-64 | 48.8 | 5.0 | 12.7 |  |
| pin_rlm | close | pin $2k+ | 38-64 | 37.3 | 1.9 | -1.9 |  |
| pin_rlm | close | pin limit <$1k | 41-29 | 58.6 | 9.4 | 24.9 |  |
| follow_move | close | 1-3k bets | 546-478 | 53.3 | 1.7 | -4.4 |  |
| follow_move | close | 3k+ bets | 190-177 | 51.8 | -0.2 | -5.2 |  |
| follow_move | close | <1k bets | 120-108 | 52.6 | -0.6 | -11.2 |  |
| follow_move | close | pin $1-2k | 258-279 | 48.0 | -3.1 | -10.3 |  |
| follow_move | close | pin $2k+ | 217-181 | 54.5 | 2.3 | -3.9 |  |
| follow_move | close | pin limit <$1k | 105-104 | 50.2 | 0.2 | -4.1 |  |
| rlm_ratio | close | 1-3k bets | 126-155 | 44.8 | 0.0 | -3.6 |  |
| rlm_ratio | close | 3k+ bets | 48-44 | 52.2 | 7.5 | 11.8 |  |
| rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.9 | 0.8 |  |
| rlm_ratio | close | pin $1-2k | 70-71 | 49.6 | 3.1 | 4.0 |  |
| rlm_ratio | close | pin $2k+ | 38-50 | 43.2 | 5.0 | -4.4 |  |
| rlm_ratio | close | pin limit <$1k | 44-34 | 56.4 | 6.8 | 8.9 |  |
| money_level | close | 1-3k bets | 693-492 | 58.5 | 2.9 | -1.9 |  |
| money_level | close | 3k+ bets | 244-193 | 55.8 | 0.7 | -3.1 |  |
| money_level | close | <1k bets | 145-118 | 55.1 | -0.8 | -11.5 |  |
| money_level | close | pin $1-2k | 315-276 | 53.3 | -0.7 | -5.1 |  |
| money_level | close | pin $2k+ | 275-213 | 56.4 | -0.9 | -7.0 |  |
| money_level | close | pin limit <$1k | 124-120 | 50.8 | 0.7 | -3.4 |  |
| sharp_gap | close | 1-3k bets | 521-619 | 45.7 | -1.7 | -8.4 |  |
| sharp_gap | close | 3k+ bets | 210-218 | 49.1 | 1.7 | 3.4 |  |
| sharp_gap | close | <1k bets | 114-137 | 45.4 | -2.4 | -14.6 |  |
| sharp_gap | close | pin $1-2k | 274-301 | 47.7 | -1.1 | -4.8 |  |
| sharp_gap | close | pin $2k+ | 221-250 | 46.9 | 0.7 | -2.0 |  |
| sharp_gap | close | pin limit <$1k | 114-122 | 48.3 | -1.4 | -3.6 |  |
| money_moving | close | 1-3k bets | 525-617 | 46.0 | -1.9 | -8.7 |  |
| money_moving | close | 3k+ bets | 209-220 | 48.7 | 1.0 | 1.8 |  |
| money_moving | close | <1k bets | 112-137 | 45.0 | -2.5 | -13.5 |  |
| money_moving | close | pin $1-2k | 271-305 | 47.0 | -1.9 | -5.8 |  |
| money_moving | close | pin $2k+ | 222-248 | 47.2 | 1.0 | -2.0 |  |
| money_moving | close | pin limit <$1k | 110-127 | 46.4 | -3.2 | -7.2 |  |
| pin_value | close | 1-3k bets | 216-228 | 48.6 | 0.9 | 0.1 |  |
| pin_value | close | 3k+ bets | 80-85 | 48.5 | -0.0 | -5.0 |  |
| pin_value | close | <1k bets | 54-44 | 55.1 | 8.0 | 10.6 |  |
| pin_value | close | pin $1-2k | 161-182 | 46.9 | -1.3 | -4.8 |  |
| pin_value | close | pin $2k+ | 97-112 | 46.4 | 0.6 | -2.4 |  |
| pin_value | close | pin limit <$1k | 92-63 | 59.4 | 9.7 | 15.4 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.9 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.9 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 209-274 | 43.3 | -4.6 | -12.3 |  |
| consensus_gap | close | 3k+ bets | 81-95 | 46.0 | -1.4 | 5.1 |  |
| consensus_gap | close | <1k bets | 40-78 | 33.9 | -9.7 | -30.7 |  |
| consensus_gap | close | pin $1-2k | 106-119 | 47.1 | -2.0 | -1.9 |  |
| consensus_gap | close | pin $2k+ | 82-102 | 44.6 | -4.4 | -5.5 |  |
| consensus_gap | close | pin limit <$1k | 49-43 | 53.3 | 3.0 | 4.1 |  |
| consensus_gap+follow_move | close | 1-3k bets | 88-80 | 52.4 | 0.5 | -1.3 |  |
| consensus_gap+money_level | close | 1-3k bets | 140-94 | 59.8 | 1.0 | 2.5 |  |
| consensus_gap+money_moving | close | 1-3k bets | 97-149 | 39.4 | -5.7 | -9.9 |  |
| consensus_gap+pin_move | close | 1-3k bets | 52-51 | 50.5 | -1.0 | 3.7 |  |
| consensus_gap+pin_value | close | 1-3k bets | 83-99 | 45.6 | 0.0 | -2.4 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 95-152 | 38.5 | -5.8 | -11.0 |  |
| follow_move+money_level | close | 1-3k bets | 370-252 | 59.5 | 3.2 | -2.8 |  |
| follow_move+money_moving | close | 1-3k bets | 302-317 | 48.8 | -0.6 | -6.7 |  |
| follow_move+pin_move | close | 1-3k bets | 222-220 | 50.2 | 0.0 | -4.6 |  |
| follow_move+pin_value | close | 1-3k bets | 73-74 | 49.7 | 1.2 | -5.9 |  |
| follow_move+sharp_gap | close | 1-3k bets | 303-315 | 49.0 | -0.1 | -5.3 |  |
| money_level+money_moving | close | 1-3k bets | 378-332 | 53.2 | 0.8 | -3.3 |  |
| money_level+pin_move | close | 1-3k bets | 192-171 | 52.9 | 0.1 | -3.5 |  |
| money_level+pin_value | close | 1-3k bets | 109-98 | 52.7 | 3.1 | -1.2 |  |
| money_level+sharp_gap | close | 1-3k bets | 367-326 | 53.0 | 0.8 | -2.9 |  |
| money_moving+pin_move | close | 1-3k bets | 191-203 | 48.5 | -0.6 | -2.3 |  |
| money_moving+pin_value | close | 1-3k bets | 98-119 | 45.2 | -2.1 | -5.9 |  |
| money_moving+sharp_gap | close | 1-3k bets | 499-591 | 45.8 | -1.8 | -7.9 |  |
| pin_move+pin_value | close | 1-3k bets | 98-96 | 50.5 | 1.5 | -0.4 |  |
| pin_move+sharp_gap | close | 1-3k bets | 198-203 | 49.4 | 0.5 | -0.1 |  |
| pin_value+sharp_gap | close | 1-3k bets | 100-123 | 44.8 | -2.2 | -6.7 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 116-168 | 40.8 | -0.8 | -7.9 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 62-104 | 37.3 | -4.4 | -11.0 |  |
| consensus_gap+money_delta | close | 1-3k bets | 25-64 | 28.1 | -9.4 | -23.3 |  |
| follow_move+money_delta | close | 1-3k bets | 95-109 | 46.6 | -0.4 | -7.4 |  |
| money_delta+money_level | close | 1-3k bets | 74-72 | 50.7 | 2.7 | 5.0 |  |
| money_delta+money_moving | close | 1-3k bets | 139-201 | 40.9 | -2.2 | -9.8 |  |
| money_delta+pin_value | close | 1-3k bets | 44-44 | 50.0 | 2.6 | 0.2 |  |
| money_delta+sharp_gap | close | 1-3k bets | 138-199 | 40.9 | -2.2 | -9.6 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 70-77 | 47.6 | 0.1 | 2.1 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 17-26 | 39.5 | 1.5 | 19.2 |  |
| money_level+pin_rlm | close | 1-3k bets | 39-28 | 58.2 | 9.9 | 12.1 |  |
| pin_move+pin_rlm | close | 1-3k bets | 79-76 | 51.0 | 6.2 | 13.7 |  |
| pin_rlm+pin_value | close | 1-3k bets | 29-24 | 54.7 | 8.6 | 30.7 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 87-92 | 48.6 | 6.0 | 18.3 |  |
| money_delta+pin_rlm | close | 1-3k bets | 49-53 | 48.0 | 4.5 | 15.3 |  |
| money_moving+pin_rlm | close | 1-3k bets | 82-89 | 48.0 | 5.3 | 18.0 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 19-30 | 38.8 | -1.7 | 4.1 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 126-155 | 44.8 | 0.0 | -3.6 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 66-77 | 46.2 | 0.2 | -6.8 |  |
| money_level+rlm_ratio | close | 1-3k bets | 59-56 | 51.3 | 1.7 | -1.0 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 120-150 | 44.4 | -0.5 | -4.1 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 126-155 | 44.8 | 0.0 | -3.6 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 12-30 | 28.6 | -7.1 | -7.2 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 55-103 | 34.8 | -6.8 | -15.6 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 50-88 | 36.2 | -3.9 | -9.9 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 52-66 | 44.1 | 0.0 | -5.5 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 31-53 | 36.9 | -6.6 | -21.6 |  |
| follow_move+pin_rlm | close | 1-3k bets | 62-70 | 47.0 | 2.3 | -2.5 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 67-65 | 50.8 | 4.7 | 4.7 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 24-41 | 36.9 | -3.2 | -14.6 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 62-70 | 47.0 | 2.3 | -2.5 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 25-21 | 54.3 | 6.5 | 4.5 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 14-20 | 41.2 | -4.1 | -19.8 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 49.7 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 30-27 | 52.6 | 2.9 | 3.3 |  |
| consensus_gap+money_moving | close | 3k+ bets | 33-52 | 38.8 | -5.2 | 14.5 |  |
| consensus_gap+pin_move | close | 3k+ bets | 21-19 | 52.5 | 2.2 | 6.4 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-6 | 33.3 | -6.5 | 6.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 34-33 | 50.7 | 4.3 | 4.3 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -0.8 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 34-52 | 39.5 | -4.3 | 17.6 |  |
| follow_move+money_moving | close | 3k+ bets | 101-106 | 48.8 | -0.4 | -4.1 |  |
| follow_move+pin_move | close | 3k+ bets | 91-89 | 50.6 | 0.5 | -1.8 |  |
| follow_move+pin_rlm | close | 3k+ bets | 30-30 | 50.0 | 5.8 | 10.3 |  |
| follow_move+pin_value | close | 3k+ bets | 32-32 | 50.0 | 0.1 | -6.2 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 48-44 | 52.2 | 7.5 | 11.8 |  |
| follow_move+sharp_gap | close | 3k+ bets | 103-105 | 49.5 | 0.8 | -2.0 |  |
| money_moving+pin_move | close | 3k+ bets | 70-80 | 46.7 | -1.4 | -7.1 |  |
| money_moving+pin_rlm | close | 3k+ bets | 31-43 | 41.9 | 0.0 | -8.1 |  |
| money_moving+pin_value | close | 3k+ bets | 39-48 | 44.8 | -2.6 | -7.9 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 46-42 | 52.3 | 7.6 | 12.4 |  |
| money_moving+sharp_gap | close | 3k+ bets | 202-210 | 49.0 | 1.6 | 3.2 |  |
| pin_move+pin_rlm | close | 3k+ bets | 31-38 | 44.9 | 1.2 | -1.5 |  |
| pin_move+pin_value | close | 3k+ bets | 32-39 | 45.1 | -4.4 | -15.2 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 33-31 | 51.6 | 6.2 | 12.1 |  |
| pin_move+sharp_gap | close | 3k+ bets | 70-80 | 46.7 | -1.1 | -6.4 |  |
| pin_rlm+pin_value | close | 3k+ bets | 6-14 | 30.0 | -15.9 | -42.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 30-30 | 50.0 | 5.8 | 10.3 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 32-44 | 42.1 | -0.0 | -7.9 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 9-9 | 50.0 | -0.3 | -5.1 |  |
| pin_value+sharp_gap | close | 3k+ bets | 39-47 | 45.3 | -2.1 | -6.8 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 48-44 | 52.2 | 7.5 | 11.8 |  |
| follow_move+money_delta | close | 3k+ bets | 38-47 | 44.7 | -0.5 | -7.2 |  |
| money_level+money_moving | close | 3k+ bets | 142-121 | 54.0 | 1.9 | 0.0 |  |
| money_level+sharp_gap | close | 3k+ bets | 141-118 | 54.4 | 2.5 | 1.5 |  |
| follow_move+money_level | close | 3k+ bets | 119-90 | 56.9 | 0.6 | -3.4 |  |
| money_level+rlm_ratio | close | 3k+ bets | 23-12 | 65.7 | 18.8 | 35.2 |  |
| consensus_gap+money_level | close | 3k+ bets | 44-44 | 50.0 | -6.5 | -13.3 |  |
| money_level+pin_move | close | 3k+ bets | 66-61 | 52.0 | -1.4 | -4.5 |  |
| money_level+pin_value | close | 3k+ bets | 44-43 | 50.6 | 0.3 | -6.3 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 7-12 | 36.8 | -0.8 | -5.4 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 44-60 | 42.3 | -0.3 | -8.1 |  |
| money_delta+money_moving | close | 3k+ bets | 60-83 | 42.0 | -0.2 | 1.4 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 19-24 | 44.2 | 2.7 | 2.2 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 23-32 | 41.8 | -0.3 | -6.0 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 21-31 | 40.4 | -1.7 | -8.0 |  |
| consensus_gap+money_delta | close | 3k+ bets | 12-23 | 34.3 | -4.0 | 18.4 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 10-24 | 29.4 | -13.2 | -34.9 |  |
| money_delta+sharp_gap | close | 3k+ bets | 58-80 | 42.0 | 0.0 | 2.1 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 25-29 | 46.3 | 2.5 | 0.7 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 11-16 | 40.7 | -0.9 | -3.2 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 7-11 | 38.9 | -11.0 | -25.7 |  |
| money_delta+money_level | close | 3k+ bets | 31-22 | 58.5 | 12.6 | 18.5 |  |
| money_level+pin_rlm | close | 3k+ bets | 15-9 | 62.5 | 17.8 | 34.6 |  |
| money_delta+pin_value | close | 3k+ bets | 18-19 | 48.6 | 2.7 | -8.3 |  |
| money_delta+pin_move | close | 3k+ bets | 35-41 | 46.1 | 0.9 | -5.8 |  |
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
| consensus_gap+pin_value | close | pin $1-2k | 63-70 | 47.4 | 1.5 | -4.8 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-14 | 50.0 | 4.5 | 9.0 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 51-62 | 45.1 | -2.1 | -2.4 |  |
| follow_move+money_moving | close | pin $1-2k | 152-183 | 45.4 | -4.5 | -11.0 |  |
| follow_move+pin_move | close | pin $1-2k | 165-169 | 49.4 | -1.3 | -5.1 |  |
| follow_move+pin_rlm | close | pin $1-2k | 49-48 | 50.5 | 4.5 | 6.6 |  |
| follow_move+pin_value | close | pin $1-2k | 56-65 | 46.3 | -3.1 | -12.7 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 70-71 | 49.6 | 3.1 | 4.0 |  |
| follow_move+sharp_gap | close | pin $1-2k | 155-181 | 46.1 | -3.6 | -9.9 |  |
| money_moving+pin_move | close | pin $1-2k | 144-160 | 47.4 | -1.9 | -3.6 |  |
| money_moving+pin_rlm | close | pin $1-2k | 58-62 | 48.3 | 4.2 | 12.2 |  |
| money_moving+pin_value | close | pin $1-2k | 65-95 | 40.6 | -7.2 | -20.4 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 68-68 | 50.0 | 3.1 | 4.6 |  |
| money_moving+sharp_gap | close | pin $1-2k | 263-293 | 47.3 | -1.5 | -5.2 |  |
| pin_move+pin_rlm | close | pin $1-2k | 58-58 | 50.0 | 4.8 | 12.8 |  |
| pin_move+pin_value | close | pin $1-2k | 70-86 | 44.9 | -4.8 | -13.3 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 57-52 | 52.3 | 5.2 | 8.4 |  |
| pin_move+sharp_gap | close | pin $1-2k | 147-159 | 48.0 | -1.1 | -2.7 |  |
| pin_rlm+pin_value | close | pin $1-2k | 15-24 | 38.5 | -9.9 | -19.7 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 49-48 | 50.5 | 4.5 | 6.6 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 61-64 | 48.8 | 5.0 | 12.7 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 18-20 | 47.4 | -2.4 | -10.6 |  |
| pin_value+sharp_gap | close | pin $1-2k | 65-93 | 41.1 | -6.6 | -19.4 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 70-71 | 49.6 | 3.1 | 4.0 |  |
| follow_move+money_level | close | pin $1-2k | 179-168 | 51.6 | -2.8 | -9.5 |  |
| money_level+rlm_ratio | close | pin $1-2k | 40-32 | 55.6 | 7.0 | 8.4 |  |
| money_level+sharp_gap | close | pin $1-2k | 196-191 | 50.6 | -1.2 | -5.9 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 3-11 | 21.4 | -20.4 | -31.6 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 46-79 | 36.8 | -6.1 | -16.0 |  |
| money_level+money_moving | close | pin $1-2k | 196-195 | 50.1 | -1.8 | -6.9 |  |
| consensus_gap+money_level | close | pin $1-2k | 62-56 | 52.5 | -4.4 | -7.1 |  |
| money_level+pin_value | close | pin $1-2k | 73-77 | 48.7 | -1.2 | -8.9 |  |
| money_level+pin_move | close | pin $1-2k | 143-132 | 52.0 | -0.9 | -5.0 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 23-37 | 38.3 | -5.6 | -4.8 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 33-44 | 42.9 | -2.3 | -2.1 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 15-25 | 37.5 | -6.8 | -8.4 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 20-31 | 39.2 | -4.1 | -3.2 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 24-38 | 38.7 | -5.1 | -7.2 |  |
| money_level+pin_rlm | close | pin $1-2k | 29-22 | 56.9 | 10.3 | 11.8 |  |
| follow_move+money_delta | close | pin $1-2k | 54-55 | 49.5 | 3.4 | 2.3 |  |
| money_delta+money_moving | close | pin $1-2k | 77-91 | 45.8 | 1.4 | -0.4 |  |
| money_delta+pin_move | close | pin $1-2k | 58-61 | 48.7 | 1.4 | 3.6 |  |
| money_delta+pin_rlm | close | pin $1-2k | 37-41 | 47.4 | 3.9 | 9.9 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 42-40 | 51.2 | 5.2 | 7.9 |  |
| money_delta+sharp_gap | close | pin $1-2k | 77-89 | 46.4 | 1.9 | 0.8 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 47.9 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 42-36 | 53.8 | 5.9 | 4.8 |  |
| consensus_gap+money_delta | close | pin $1-2k | 16-25 | 39.0 | -2.0 | -7.9 |  |
| money_delta+pin_value | close | pin $1-2k | 37-42 | 46.8 | -1.6 | -11.5 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 12-24 | 33.3 | -9.1 | -17.6 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 8-21 | 27.6 | -21.6 | -47.0 |  |
| follow_move+money_level | close | pin $2k+ | 138-87 | 61.3 | 1.9 | -2.0 |  |
| follow_move+money_moving | close | pin $2k+ | 106-102 | 51.0 | 3.1 | -2.5 |  |
| follow_move+pin_move | close | pin $2k+ | 131-122 | 51.8 | 1.8 | -2.5 |  |
| follow_move+sharp_gap | close | pin $2k+ | 107-103 | 51.0 | 3.2 | -2.2 |  |
| money_level+money_moving | close | pin $2k+ | 149-131 | 53.2 | 0.5 | -3.4 |  |
| money_level+pin_move | close | pin $2k+ | 100-88 | 53.2 | -2.0 | -6.0 |  |
| money_level+sharp_gap | close | pin $2k+ | 149-132 | 53.0 | 0.4 | -3.4 |  |
| money_moving+pin_move | close | pin $2k+ | 95-103 | 48.0 | 0.8 | -4.2 |  |
| money_moving+sharp_gap | close | pin $2k+ | 216-244 | 47.0 | 0.8 | -1.9 |  |
| pin_move+sharp_gap | close | pin $2k+ | 95-104 | 47.7 | 0.6 | -4.2 |  |
| consensus_gap+money_delta | close | pin $2k+ | 7-25 | 21.9 | -9.9 | -56.9 |  |
| consensus_gap+money_moving | close | pin $2k+ | 30-58 | 34.1 | -8.5 | -6.7 |  |
| consensus_gap+pin_value | close | pin $2k+ | 33-45 | 42.3 | 1.0 | 6.4 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 32-61 | 34.4 | -8.9 | -6.2 |  |
| money_delta+money_moving | close | pin $2k+ | 56-78 | 41.8 | 3.4 | -6.8 |  |
| money_delta+pin_value | close | pin $2k+ | 18-21 | 46.2 | 3.6 | -11.8 |  |
| money_delta+sharp_gap | close | pin $2k+ | 54-77 | 41.2 | 2.8 | -7.9 |  |
| money_moving+pin_value | close | pin $2k+ | 54-63 | 46.2 | 1.2 | 6.0 |  |
| pin_value+sharp_gap | close | pin $2k+ | 54-64 | 45.8 | 1.0 | 5.1 |  |
| consensus_gap+pin_move | close | pin $2k+ | 23-30 | 43.4 | -6.2 | -17.5 |  |
| money_delta+pin_move | close | pin $2k+ | 31-44 | 41.3 | -1.1 | -14.8 |  |
| consensus_gap+follow_move | close | pin $2k+ | 26-26 | 50.0 | -1.5 | -15.9 |  |
| follow_move+pin_value | close | pin $2k+ | 32-30 | 51.6 | 4.5 | -2.3 |  |
| pin_move+pin_value | close | pin $2k+ | 45-44 | 50.6 | 2.9 | -0.6 |  |
| follow_move+money_delta | close | pin $2k+ | 31-37 | 45.6 | 3.6 | -5.3 |  |
| follow_move+pin_rlm | close | pin $2k+ | 27-41 | 39.7 | 2.1 | -9.3 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 38-50 | 43.2 | 5.0 | -4.4 |  |
| money_delta+money_level | close | pin $2k+ | 24-20 | 54.5 | 11.0 | 10.6 |  |
| money_delta+pin_rlm | close | pin $2k+ | 21-36 | 36.8 | 1.3 | -8.3 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 19-22 | 46.3 | 7.7 | 0.7 |  |
| money_level+pin_rlm | close | pin $2k+ | 15-9 | 62.5 | 20.1 | 32.4 |  |
| money_level+pin_value | close | pin $2k+ | 53-49 | 52.0 | 2.1 | -4.0 |  |
| money_level+rlm_ratio | close | pin $2k+ | 14-11 | 56.0 | 9.7 | 17.6 |  |
| money_moving+pin_rlm | close | pin $2k+ | 38-64 | 37.3 | 1.9 | -1.9 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 38-49 | 43.7 | 5.3 | -3.3 |  |
| pin_move+pin_rlm | close | pin $2k+ | 31-43 | 41.9 | 3.8 | -1.9 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 27-35 | 43.5 | 3.7 | -0.6 |  |
| pin_rlm+pin_value | close | pin $2k+ | 6-13 | 31.6 | -4.3 | 13.6 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 27-41 | 39.7 | 2.1 | -9.3 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 38-64 | 37.3 | 1.9 | -1.9 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 4-6 | 40.0 | -0.9 | -19.0 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 38-50 | 43.2 | 5.0 | -4.4 |  |
| consensus_gap+money_level | close | pin $2k+ | 53-44 | 54.6 | -8.1 | -15.0 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 51-62 | 45.1 | 7.4 | -2.5 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 16-20 | 44.4 | 5.7 | -7.5 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 26-35 | 42.6 | 7.2 | -4.2 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 13-27 | 32.5 | 0.3 | -20.0 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 20-32 | 38.5 | 5.9 | -9.7 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 26-36 | 41.9 | 6.7 | -5.7 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-19 | 17.4 | -11.4 | -24.8 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 4-12 | 25.0 | -3.0 | -46.7 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-11 | 0.0 | -28.9 | -100.0 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 34-40 | 45.9 | 6.1 | -0.0 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 4-7 | 36.4 | -0.5 | -26.4 |  |
| follow_move+money_delta | close | pin limit <$1k | 31-37 | 45.6 | -4.3 | -12.5 |  |
| money_level+money_moving | close | pin limit <$1k | 68-76 | 47.2 | -2.6 | -9.4 |  |
| money_level+sharp_gap | close | pin limit <$1k | 67-71 | 48.6 | -1.2 | -6.8 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 103-113 | 47.7 | -2.0 | -4.4 |  |
| consensus_gap+money_level | close | pin limit <$1k | 27-25 | 51.9 | 1.4 | -4.1 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 14-10 | 58.3 | 9.6 | 27.8 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 35-31 | 53.0 | 3.7 | 6.4 |  |
| follow_move+money_moving | close | pin limit <$1k | 64-73 | 46.7 | -3.0 | -10.2 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 69-73 | 48.6 | -1.1 | -6.6 |  |
| money_level+pin_move | close | pin limit <$1k | 49-47 | 51.0 | 1.1 | -2.5 |  |
| money_level+pin_value | close | pin limit <$1k | 45-32 | 58.4 | 8.8 | 10.6 |  |
| pin_move+pin_value | close | pin limit <$1k | 40-25 | 61.5 | 12.0 | 23.8 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 17-10 | 63.0 | 12.7 | 15.4 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 21-17 | 55.3 | 6.2 | 16.0 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 23-18 | 56.1 | 6.9 | 16.7 |  |
| follow_move+money_level | close | pin limit <$1k | 53-54 | 49.5 | -0.7 | -5.7 |  |
| follow_move+pin_move | close | pin limit <$1k | 59-60 | 49.6 | -0.2 | -5.1 |  |
| follow_move+pin_value | close | pin limit <$1k | 35-23 | 60.3 | 10.7 | 14.5 |  |
| money_moving+pin_move | close | pin limit <$1k | 58-61 | 48.7 | -1.0 | -3.0 |  |
| money_moving+pin_value | close | pin limit <$1k | 35-25 | 58.3 | 8.9 | 18.1 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 62-62 | 50.0 | 0.3 | -0.8 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 37-28 | 56.9 | 7.4 | 14.9 |  |
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
| follow_move | early | pin $1-2k | 27-16 | 62.8 | 8.5 | 11.9 | -0.35 |
| follow_move | early | pin limit <$1k | 47-39 | 54.7 | 4.4 | 1.9 | -0.11 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 23-13 | 63.9 | 26.8 | 41.4 | 0.6 |
| rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.2 | 55.6 | -1.52 |
| rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 0.9 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 42.8 | 59.7 | 0.33 |
| money_level | early | <1k bets | 140-89 | 61.1 | 1.4 | -4.4 | -0.16 |
| money_level | early | pin $1-2k | 20-8 | 71.4 | 5.8 | 4.1 | 0.01 |
| money_level | early | pin limit <$1k | 24-26 | 48.0 | -5.2 | -11.4 | 0.22 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.5 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.1 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 116-98 | 54.2 | 5.6 | 4.5 | 0.35 |
| sharp_gap | early | pin $1-2k | 15-11 | 57.7 | 4.8 | 6.7 | -0.39 |
| sharp_gap | early | pin limit <$1k | 29-18 | 61.7 | 13.1 | 27.9 | 0.12 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.5 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.9 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 78-69 | 53.1 | 1.2 | -7.7 | 0.01 |
| money_moving | early | pin $1-2k | 8-8 | 50.0 | -8.5 | -31.4 | 0.21 |
| money_moving | early | pin limit <$1k | 23-9 | 71.9 | 22.7 | 52.0 | 0.42 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.7 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 36-39 | 48.0 | -0.3 | -9.2 | 0.13 |
| pin_value | early | pin $1-2k | 13-18 | 41.9 | -3.7 | -21.1 | 0.12 |
| pin_value | early | pin limit <$1k | 36-30 | 54.5 | 5.0 | 3.2 | 0.09 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -49.7 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -26.7 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.3 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.7 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 175-236 | 42.6 | -4.8 | -14.8 | 0.36 |
| consensus_gap | early | pin $1-2k | 12-20 | 37.5 | -7.9 | -28.2 | 0.51 |
| consensus_gap | early | pin limit <$1k | 18-34 | 34.6 | -15.5 | -28.2 | 0.28 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.8 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.8 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -0.9 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.1 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 4.7 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.1 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.8 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.4 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.6 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -49.7 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -1.0 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 3.6 | -6.9 | 0.3 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -0.4 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-6 | 53.8 | 6.6 | 0.8 | -0.31 |
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
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -8.0 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -8.0 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-3 | 40.0 | 3.2 | 55.6 | -1.52 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -39.4 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -39.4 | -100.0 | 2.5 |
| money_level+sharp_gap | early | pin $1-2k | 12-4 | 75.0 | 10.4 | 12.5 | -0.26 |
| money_moving+sharp_gap | early | pin $1-2k | 4-6 | 40.0 | -16.8 | -45.4 | 0.08 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.9 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 4-6 | 40.0 | -10.0 | -31.3 | 0.34 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 0-3 | 0.0 | -26.6 | -100.0 | -0.97 |
| follow_move+pin_value | early | pin $1-2k | 6-5 | 54.5 | 7.1 | 0.8 | -0.3 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -26.6 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 11-4 | 73.3 | 8.2 | 6.6 | -0.07 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 47.9 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 4-1 | 80.0 | 11.7 | 6.9 | -0.18 |
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
| rlm_quiet | close | 1-3k bets | 19-33 | 36.5 | -3.9 | -4.5 |  |
| rlm_quiet | close | 3k+ bets | 2-5 | 28.6 | -10.8 | -37.5 |  |
| rlm_quiet | close | <1k bets | 1-9 | 10.0 | -29.9 | -80.9 |  |
| rlm_quiet | close | pin $1-2k | 9-14 | 39.1 | -1.4 | -17.7 |  |
| rlm_quiet | close | pin $2k+ | 6-7 | 46.2 | 4.5 | 76.4 |  |
| rlm_quiet | close | pin limit <$1k | 4-7 | 36.4 | -4.8 | -29.4 |  |
| pin_move | close | 1-3k bets | 32-38 | 45.7 | -3.1 | -13.0 |  |
| pin_move | close | 3k+ bets | 5-4 | 55.6 | 8.5 | 10.1 |  |
| pin_move | close | <1k bets | 5-9 | 35.7 | -13.4 | -34.7 |  |
| pin_move | close | pin $1-2k | 21-24 | 46.7 | -1.0 | -9.7 |  |
| pin_move | close | pin $2k+ | 15-15 | 50.0 | -1.1 | -7.5 |  |
| pin_move | close | pin limit <$1k | 6-12 | 33.3 | -13.8 | -35.8 |  |
| money_delta | close | 1-3k bets | 16-21 | 43.2 | 3.2 | -14.1 |  |
| money_delta | close | 3k+ bets | 5-2 | 71.4 | 27.9 | 46.6 |  |
| money_delta | close | <1k bets | 4-6 | 40.0 | 2.4 | 20.2 |  |
| money_delta | close | pin $1-2k | 10-9 | 52.6 | 13.3 | 21.1 |  |
| money_delta | close | pin $2k+ | 3-5 | 37.5 | -0.5 | -23.4 |  |
| money_delta | close | pin limit <$1k | 3-7 | 30.0 | -11.3 | -42.2 |  |
| pin_rlm | close | 1-3k bets | 4-9 | 30.8 | -9.5 | -39.4 |  |
| pin_rlm | close | 3k+ bets | 2-0 | 100.0 | 62.4 | 114.6 |  |
| pin_rlm | close | <1k bets | 1-4 | 20.0 | -18.9 | -61.8 |  |
| pin_rlm | close | pin $1-2k | 5-3 | 62.5 | 24.4 | 21.8 |  |
| pin_rlm | close | pin $2k+ | 1-2 | 33.3 | -11.8 | -22.0 |  |
| pin_rlm | close | pin limit <$1k | 1-8 | 11.1 | -28.1 | -77.8 |  |
| follow_move | close | 1-3k bets | 53-70 | 43.1 | -5.8 | -10.6 |  |
| follow_move | close | 3k+ bets | 9-8 | 52.9 | 3.1 | -3.3 |  |
| follow_move | close | <1k bets | 8-17 | 32.0 | -15.2 | -45.3 |  |
| follow_move | close | pin $1-2k | 25-29 | 46.3 | -1.3 | -11.2 |  |
| follow_move | close | pin $2k+ | 23-18 | 56.1 | 6.2 | 29.0 |  |
| follow_move | close | pin limit <$1k | 9-14 | 39.1 | -9.1 | -24.9 |  |
| rlm_ratio | close | 1-3k bets | 9-23 | 28.1 | -11.7 | -45.5 |  |
| rlm_ratio | close | 3k+ bets | 3-2 | 60.0 | 17.9 | 24.0 |  |
| rlm_ratio | close | <1k bets | 2-5 | 28.6 | -9.9 | -45.7 |  |
| rlm_ratio | close | pin $1-2k | 7-4 | 63.6 | 25.8 | 23.8 |  |
| rlm_ratio | close | pin $2k+ | 1-4 | 20.0 | -17.5 | -53.2 |  |
| rlm_ratio | close | pin limit <$1k | 3-8 | 27.3 | -13.9 | -47.5 |  |
| money_level | close | 1-3k bets | 67-50 | 57.3 | -0.4 | -3.5 |  |
| money_level | close | 3k+ bets | 11-11 | 50.0 | -6.3 | -12.7 |  |
| money_level | close | <1k bets | 17-5 | 77.3 | 22.2 | 41.7 |  |
| money_level | close | pin $1-2k | 29-21 | 58.0 | 1.7 | 2.5 |  |
| money_level | close | pin $2k+ | 20-17 | 54.1 | -3.6 | -12.4 |  |
| money_level | close | pin limit <$1k | 12-12 | 50.0 | -5.9 | -5.0 |  |
| sharp_gap | close | 1-3k bets | 40-62 | 39.2 | -9.2 | -27.4 |  |
| sharp_gap | close | 3k+ bets | 9-13 | 40.9 | -7.4 | -21.1 |  |
| sharp_gap | close | <1k bets | 11-9 | 55.0 | 10.2 | 24.8 |  |
| sharp_gap | close | pin $1-2k | 21-23 | 47.7 | -0.5 | -2.5 |  |
| sharp_gap | close | pin $2k+ | 13-20 | 39.4 | -8.9 | -27.1 |  |
| sharp_gap | close | pin limit <$1k | 4-16 | 20.0 | -26.0 | -61.8 |  |
| money_moving | close | 1-3k bets | 44-61 | 41.9 | -7.5 | -24.2 |  |
| money_moving | close | 3k+ bets | 9-13 | 40.9 | -7.4 | -21.1 |  |
| money_moving | close | <1k bets | 11-9 | 55.0 | 10.2 | 24.8 |  |
| money_moving | close | pin $1-2k | 23-21 | 52.3 | 2.8 | 3.3 |  |
| money_moving | close | pin $2k+ | 13-20 | 39.4 | -8.9 | -27.1 |  |
| money_moving | close | pin limit <$1k | 6-17 | 26.1 | -21.7 | -50.3 |  |
| pin_value | close | 1-3k bets | 32-21 | 60.4 | 8.9 | 35.7 |  |
| pin_value | close | 3k+ bets | 2-4 | 33.3 | -20.8 | -36.6 |  |
| pin_value | close | <1k bets | 8-1 | 88.9 | 38.2 | 108.1 |  |
| pin_value | close | pin $1-2k | 19-14 | 57.6 | 7.4 | 25.6 |  |
| pin_value | close | pin $2k+ | 11-7 | 61.1 | 11.2 | 67.9 |  |
| pin_value | close | pin limit <$1k | 12-5 | 70.6 | 14.3 | 34.0 |  |
| consensus_gap | close | 1-3k bets | 31-23 | 57.4 | 3.3 | -1.0 |  |
| consensus_gap | close | 3k+ bets | 2-2 | 50.0 | -6.2 | -20.4 |  |
| consensus_gap | close | <1k bets | 6-1 | 85.7 | 37.2 | 101.7 |  |
| consensus_gap | close | pin $1-2k | 8-9 | 47.1 | -7.0 | 4.5 |  |
| consensus_gap | close | pin $2k+ | 18-5 | 78.3 | 21.0 | 30.3 |  |
| consensus_gap | close | pin limit <$1k | 5-2 | 71.4 | 20.6 | 36.6 |  |
| follow_move+pin_move | close | 1-3k bets | 23-32 | 41.8 | -6.4 | -19.4 |  |
| money_delta+money_moving | close | 1-3k bets | 12-14 | 46.2 | 6.8 | -7.4 |  |
| money_delta+sharp_gap | close | 1-3k bets | 12-13 | 48.0 | 8.6 | -3.7 |  |
| money_moving+sharp_gap | close | 1-3k bets | 39-59 | 39.8 | -8.9 | -26.4 |  |
| consensus_gap+money_level | close | 1-3k bets | 22-11 | 66.7 | 5.8 | 10.5 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 19-33 | 36.5 | -3.9 | -4.5 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 9-14 | 39.1 | -1.9 | -17.6 |  |
| consensus_gap+follow_move | close | 1-3k bets | 11-11 | 50.0 | -2.5 | -12.2 |  |
| follow_move+money_level | close | 1-3k bets | 24-24 | 50.0 | -7.2 | -13.9 |  |
| money_level+money_moving | close | 1-3k bets | 31-32 | 49.2 | -6.1 | -15.4 |  |
| money_level+sharp_gap | close | 1-3k bets | 27-31 | 46.6 | -8.2 | -17.6 |  |
| consensus_gap+money_moving | close | 1-3k bets | 9-14 | 39.1 | -14.2 | -32.8 |  |
| consensus_gap+pin_move | close | 1-3k bets | 6-5 | 54.5 | 3.2 | -3.0 |  |
| consensus_gap+pin_value | close | 1-3k bets | 13-9 | 59.1 | 7.8 | 10.8 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 8-14 | 36.4 | -15.3 | -34.9 |  |
| follow_move+money_moving | close | 1-3k bets | 20-36 | 35.7 | -12.6 | -34.7 |  |
| follow_move+pin_value | close | 1-3k bets | 9-7 | 56.2 | 4.1 | 66.6 |  |
| follow_move+sharp_gap | close | 1-3k bets | 21-38 | 35.6 | -12.1 | -34.8 |  |
| money_level+pin_move | close | 1-3k bets | 14-15 | 48.3 | -6.7 | -14.1 |  |
| money_level+pin_value | close | 1-3k bets | 11-10 | 52.4 | -4.3 | -1.2 |  |
| money_moving+pin_move | close | 1-3k bets | 11-17 | 39.3 | -9.5 | -24.9 |  |
| money_moving+pin_value | close | 1-3k bets | 7-12 | 36.8 | -16.2 | -30.5 |  |
| pin_move+pin_value | close | 1-3k bets | 8-8 | 50.0 | -2.2 | -6.5 |  |
| pin_move+sharp_gap | close | 1-3k bets | 9-19 | 32.1 | -14.8 | -38.4 |  |
| pin_value+sharp_gap | close | 1-3k bets | 6-11 | 35.3 | -16.9 | -33.5 |  |
| follow_move+money_delta | close | 1-3k bets | 9-16 | 36.0 | -4.2 | -29.9 |  |
| money_delta+pin_move | close | 1-3k bets | 5-6 | 45.5 | 6.9 | -10.2 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 6-12 | 33.3 | -6.0 | -35.1 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 9-23 | 28.1 | -11.7 | -45.5 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 6-15 | 28.6 | -10.0 | -42.7 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 9-21 | 30.0 | -10.1 | -41.8 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 4-17 | 19.0 | -19.3 | -63.0 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 6-18 | 25.0 | -13.2 | -49.8 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 9-23 | 28.1 | -11.7 | -45.5 |  |
| money_delta+money_level | close | 1-3k bets | 3-2 | 60.0 | 20.0 | 17.6 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 3-6 | 33.3 | -5.2 | -35.4 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 2-4 | 33.3 | -2.9 | -34.9 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 7-11 | 38.9 | -0.6 | -24.4 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 1-2 | 33.3 | -13.2 | -33.3 |  |
| money_level+pin_rlm | close | 1-3k bets | 2-3 | 40.0 | -3.8 | -21.4 |  |
| money_moving+pin_rlm | close | 1-3k bets | 4-8 | 33.3 | -7.4 | -34.3 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 4-9 | 30.8 | -9.5 | -39.4 |  |
| money_level+rlm_ratio | close | 1-3k bets | 4-4 | 50.0 | 9.3 | -2.4 |  |
| consensus_gap+money_delta | close | 1-3k bets | 2-2 | 50.0 | 13.5 | -2.3 |  |
| follow_move+pin_rlm | close | 1-3k bets | 4-7 | 36.4 | -1.8 | -28.4 |  |
| money_delta+pin_rlm | close | 1-3k bets | 3-4 | 42.9 | 5.0 | -14.7 |  |
| pin_move+pin_rlm | close | 1-3k bets | 4-8 | 33.3 | -5.0 | -34.3 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 4-7 | 36.4 | -1.8 | -28.4 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 2-4 | 33.3 | -5.0 | -34.1 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 4-7 | 36.4 | -1.8 | -28.4 |  |
| money_delta+pin_value | close | 1-3k bets | 3-2 | 60.0 | 16.2 | 13.8 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 3-2 | 60.0 | 18.2 | 208.4 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 2-0 | 100.0 | 50.0 | 88.9 |  |
| pin_rlm+pin_value | close | 1-3k bets | 0-1 | 0.0 | -39.7 | -100.0 |  |
| money_level+money_moving | close | 3k+ bets | 6-8 | 42.9 | -10.8 | -24.3 |  |
| money_level+sharp_gap | close | 3k+ bets | 6-8 | 42.9 | -10.8 | -24.3 |  |
| money_moving+sharp_gap | close | 3k+ bets | 9-13 | 40.9 | -7.4 | -21.1 |  |
| follow_move+money_delta | close | 3k+ bets | 2-2 | 50.0 | 5.1 | -3.5 |  |
| follow_move+money_level | close | 3k+ bets | 5-2 | 71.4 | 11.1 | 11.7 |  |
| follow_move+money_moving | close | 3k+ bets | 5-3 | 62.5 | 15.1 | 13.9 |  |
| follow_move+pin_move | close | 3k+ bets | 4-3 | 57.1 | 11.0 | 13.6 |  |
| follow_move+pin_rlm | close | 3k+ bets | 2-0 | 100.0 | 62.4 | 114.6 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 3-2 | 60.0 | 17.9 | 24.0 |  |
| follow_move+sharp_gap | close | 3k+ bets | 5-3 | 62.5 | 15.1 | 13.9 |  |
| money_delta+money_level | close | 3k+ bets | 2-0 | 100.0 | 50.0 | 93.0 |  |
| money_delta+money_moving | close | 3k+ bets | 4-1 | 80.0 | 37.9 | 65.6 |  |
| money_delta+pin_move | close | 3k+ bets | 1-1 | 50.0 | 10.3 | -2.4 |  |
| money_delta+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 60.3 | 95.2 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 2-1 | 66.7 | 20.1 | 28.7 |  |
| money_delta+sharp_gap | close | 3k+ bets | 4-1 | 80.0 | 37.9 | 65.6 |  |
| money_level+pin_move | close | 3k+ bets | 2-2 | 50.0 | -3.6 | -10.6 |  |
| money_level+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 60.3 | 95.2 |  |
| money_level+rlm_ratio | close | 3k+ bets | 2-0 | 100.0 | 50.0 | 93.0 |  |
| money_moving+pin_move | close | 3k+ bets | 2-2 | 50.0 | 2.6 | -10.6 |  |
| money_moving+pin_rlm | close | 3k+ bets | 2-0 | 100.0 | 62.4 | 114.6 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 3-2 | 60.0 | 17.9 | 24.0 |  |
| pin_move+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 60.3 | 95.2 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 1-0 | 100.0 | 60.3 | 95.2 |  |
| pin_move+sharp_gap | close | 3k+ bets | 2-2 | 50.0 | 2.6 | -10.6 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 2-0 | 100.0 | 62.4 | 114.6 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 2-0 | 100.0 | 62.4 | 114.6 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 3-2 | 60.0 | 17.9 | 24.0 |  |
| consensus_gap+money_level | close | 3k+ bets | 2-1 | 66.7 | 3.6 | 6.1 |  |
| consensus_gap+money_moving | close | 3k+ bets | 1-2 | 33.3 | -21.5 | -57.0 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 1-2 | 33.3 | -21.5 | -57.0 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 2-5 | 28.6 | -10.8 | -37.5 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 2-2 | 50.0 | 11.3 | 9.3 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 0-2 | 0.0 | -39.7 | -100.0 |  |
| money_level+pin_value | close | 3k+ bets | 2-3 | 40.0 | -14.1 | -24.0 |  |
| money_moving+pin_value | close | 3k+ bets | 1-3 | 25.0 | -25.0 | -52.3 |  |
| pin_value+sharp_gap | close | 3k+ bets | 1-3 | 25.0 | -25.0 | -52.3 |  |
| consensus_gap+follow_move | close | 3k+ bets | 1-0 | 100.0 | 35.5 | 29.0 |  |
| consensus_gap+pin_value | close | 3k+ bets | 1-0 | 100.0 | 39.7 | 89.3 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 0-3 | 0.0 | -38.3 | -100.0 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 0-3 | 0.0 | -38.3 | -100.0 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 0-2 | 0.0 | -37.6 | -100.0 |  |
| pin_move+pin_value | close | 3k+ bets | 0-2 | 0.0 | -55.1 | -100.0 |  |
| follow_move+pin_value | close | 3k+ bets | 0-1 | 0.0 | -64.5 | -100.0 |  |
| consensus_gap+money_level | close | <1k bets | 4-0 | 100.0 | 46.4 | 69.2 |  |
| consensus_gap+money_moving | close | <1k bets | 3-0 | 100.0 | 59.7 | 209.0 |  |
| consensus_gap+pin_value | close | <1k bets | 2-0 | 100.0 | 59.5 | 268.8 |  |
| consensus_gap+sharp_gap | close | <1k bets | 3-0 | 100.0 | 59.7 | 209.0 |  |
| follow_move+pin_move | close | <1k bets | 3-8 | 27.3 | -19.9 | -51.3 |  |
| follow_move+rlm_quiet | close | <1k bets | 1-9 | 10.0 | -29.9 | -80.9 |  |
| money_level+money_moving | close | <1k bets | 9-3 | 75.0 | 25.7 | 46.2 |  |
| money_level+pin_value | close | <1k bets | 3-0 | 100.0 | 44.6 | 91.3 |  |
| money_level+sharp_gap | close | <1k bets | 9-3 | 75.0 | 25.7 | 46.2 |  |
| money_moving+pin_value | close | <1k bets | 3-0 | 100.0 | 59.7 | 209.5 |  |
| money_moving+sharp_gap | close | <1k bets | 11-9 | 55.0 | 10.2 | 24.8 |  |
| pin_move+rlm_quiet | close | <1k bets | 1-4 | 20.0 | -21.8 | -61.8 |  |
| pin_value+sharp_gap | close | <1k bets | 3-0 | 100.0 | 59.7 | 209.5 |  |
| follow_move+money_moving | close | <1k bets | 4-6 | 40.0 | -3.8 | -36.0 |  |
| follow_move+sharp_gap | close | <1k bets | 4-6 | 40.0 | -3.8 | -36.0 |  |
| money_level+pin_move | close | <1k bets | 3-3 | 50.0 | -4.1 | -10.7 |  |
| money_moving+rlm_quiet | close | <1k bets | 1-4 | 20.0 | -18.9 | -61.8 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 1-4 | 20.0 | -18.9 | -61.8 |  |
| follow_move+money_delta | close | <1k bets | 2-4 | 33.3 | -5.0 | -36.6 |  |
| follow_move+pin_rlm | close | <1k bets | 1-4 | 20.0 | -18.9 | -61.8 |  |
| follow_move+pin_value | close | <1k bets | 2-0 | 100.0 | 50.0 | 93.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 2-5 | 28.6 | -9.9 | -45.7 |  |
| money_delta+money_moving | close | <1k bets | 4-6 | 40.0 | 2.4 | 20.2 |  |
| money_delta+pin_move | close | <1k bets | 1-3 | 25.0 | -13.7 | -52.3 |  |
| money_delta+pin_rlm | close | <1k bets | 1-3 | 25.0 | -13.7 | -52.3 |  |
| money_delta+pin_value | close | <1k bets | 2-0 | 100.0 | 62.4 | 270.4 |  |
| money_delta+rlm_quiet | close | <1k bets | 1-2 | 33.3 | -5.0 | -36.4 |  |
| money_delta+rlm_ratio | close | <1k bets | 2-4 | 33.3 | -5.0 | -36.6 |  |
| money_delta+sharp_gap | close | <1k bets | 4-6 | 40.0 | 2.4 | 20.2 |  |
| money_moving+pin_move | close | <1k bets | 1-4 | 20.0 | -18.9 | -61.8 |  |
| money_moving+pin_rlm | close | <1k bets | 1-4 | 20.0 | -18.9 | -61.8 |  |
| money_moving+rlm_ratio | close | <1k bets | 2-5 | 28.6 | -9.9 | -45.7 |  |
| pin_move+pin_rlm | close | <1k bets | 1-4 | 20.0 | -18.9 | -61.8 |  |
| pin_move+pin_value | close | <1k bets | 3-0 | 100.0 | 48.5 | 91.0 |  |
| pin_move+rlm_ratio | close | <1k bets | 1-4 | 20.0 | -18.9 | -61.8 |  |
| pin_move+sharp_gap | close | <1k bets | 1-4 | 20.0 | -18.9 | -61.8 |  |
| pin_rlm+pin_value | close | <1k bets | 1-0 | 100.0 | 60.3 | 90.9 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 1-2 | 33.3 | -6.4 | -36.4 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 1-4 | 20.0 | -18.9 | -61.8 |  |
| pin_rlm+sharp_gap | close | <1k bets | 1-4 | 20.0 | -18.9 | -61.8 |  |
| pin_value+rlm_quiet | close | <1k bets | 1-0 | 100.0 | 60.3 | 90.9 |  |
| pin_value+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 60.3 | 90.9 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 1-3 | 25.0 | -13.7 | -52.3 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 2-5 | 28.6 | -9.9 | -45.7 |  |
| consensus_gap+follow_move | close | <1k bets | 2-0 | 100.0 | 47.9 | 69.7 |  |
| consensus_gap+pin_move | close | <1k bets | 1-0 | 100.0 | 35.5 | 50.0 |  |
| follow_move+money_level | close | <1k bets | 5-3 | 62.5 | 8.3 | -0.8 |  |
| money_delta+money_level | close | <1k bets | 2-2 | 50.0 | 12.4 | 15.3 |  |
| money_level+pin_rlm | close | <1k bets | 0-2 | 0.0 | -37.6 | -100.0 |  |
| money_level+rlm_ratio | close | <1k bets | 1-2 | 33.3 | -5.0 | -36.9 |  |
| consensus_gap+money_delta | close | <1k bets | 2-0 | 100.0 | 62.4 | 269.6 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 60.3 | 89.3 |  |
| money_delta+money_moving | close | pin $1-2k | 7-3 | 70.0 | 32.4 | 71.9 |  |
| money_delta+sharp_gap | close | pin $1-2k | 7-3 | 70.0 | 32.4 | 71.9 |  |
| money_moving+sharp_gap | close | pin $1-2k | 21-21 | 50.0 | 1.2 | 2.2 |  |
| consensus_gap+follow_move | close | pin $1-2k | 3-5 | 37.5 | -16.2 | -31.6 |  |
| consensus_gap+money_level | close | pin $1-2k | 5-4 | 55.6 | -6.6 | -6.1 |  |
| consensus_gap+money_moving | close | pin $1-2k | 3-5 | 37.5 | -15.1 | 6.9 |  |
| consensus_gap+pin_move | close | pin $1-2k | 1-3 | 25.0 | -26.2 | -52.3 |  |
| consensus_gap+pin_value | close | pin $1-2k | 4-4 | 50.0 | -0.6 | 39.9 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 2-5 | 28.6 | -22.3 | 5.8 |  |
| follow_move+money_level | close | pin $1-2k | 13-9 | 59.1 | 5.4 | 6.3 |  |
| follow_move+money_moving | close | pin $1-2k | 12-9 | 57.1 | 10.0 | 6.2 |  |
| follow_move+pin_move | close | pin $1-2k | 13-21 | 38.2 | -7.8 | -23.8 |  |
| follow_move+pin_value | close | pin $1-2k | 3-5 | 37.5 | -12.9 | -29.2 |  |
| follow_move+sharp_gap | close | pin $1-2k | 12-11 | 52.2 | 6.0 | -3.0 |  |
| money_level+money_moving | close | pin $1-2k | 18-13 | 58.1 | 4.6 | 4.0 |  |
| money_level+pin_move | close | pin $1-2k | 9-8 | 52.9 | -0.1 | -1.1 |  |
| money_level+pin_value | close | pin $1-2k | 5-5 | 50.0 | -6.8 | -6.0 |  |
| money_level+sharp_gap | close | pin $1-2k | 16-13 | 55.2 | 2.4 | 2.4 |  |
| money_moving+pin_move | close | pin $1-2k | 8-7 | 53.3 | 6.9 | 2.9 |  |
| money_moving+pin_value | close | pin $1-2k | 5-6 | 45.5 | -5.1 | 18.7 |  |
| pin_move+pin_value | close | pin $1-2k | 5-4 | 55.6 | 4.1 | 3.9 |  |
| pin_move+sharp_gap | close | pin $1-2k | 8-9 | 47.1 | 1.9 | -9.2 |  |
| pin_value+sharp_gap | close | pin $1-2k | 5-6 | 45.5 | -5.1 | 18.7 |  |
| follow_move+money_delta | close | pin $1-2k | 7-8 | 46.7 | 6.8 | -8.7 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 9-14 | 39.1 | -1.4 | -17.7 |  |
| money_delta+pin_move | close | pin $1-2k | 6-4 | 60.0 | 21.1 | 17.4 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 4-7 | 36.4 | -4.3 | -29.4 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 8-9 | 47.1 | 6.6 | -4.6 |  |
| follow_move+pin_rlm | close | pin $1-2k | 5-3 | 62.5 | 24.4 | 21.8 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 7-4 | 63.6 | 25.8 | 23.8 |  |
| pin_move+pin_rlm | close | pin $1-2k | 5-3 | 62.5 | 24.4 | 21.8 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 5-3 | 62.5 | 24.4 | 21.8 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 2-2 | 50.0 | 11.3 | -3.5 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 5-3 | 62.5 | 24.4 | 21.8 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 5-3 | 62.5 | 24.4 | 21.8 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 2-3 | 40.0 | 2.0 | -22.8 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 3-5 | 37.5 | -0.6 | -27.3 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 7-4 | 63.6 | 25.8 | 23.8 |  |
| money_delta+money_level | close | pin $1-2k | 3-1 | 75.0 | 37.4 | 48.1 |  |
| money_delta+pin_rlm | close | pin $1-2k | 4-1 | 80.0 | 42.0 | 56.7 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 5-2 | 71.4 | 33.5 | 39.8 |  |
| money_level+pin_rlm | close | pin $1-2k | 3-1 | 75.0 | 37.4 | 47.0 |  |
| money_level+rlm_ratio | close | pin $1-2k | 5-1 | 83.3 | 45.7 | 62.7 |  |
| money_moving+pin_rlm | close | pin $1-2k | 5-2 | 71.4 | 32.9 | 39.2 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 7-3 | 70.0 | 32.0 | 36.2 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 3-3 | 50.0 | 11.0 | -3.1 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 1-2 | 33.3 | -8.5 | -36.4 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 2-2 | 50.0 | 6.6 | -4.5 |  |
| money_delta+pin_value | close | pin $1-2k | 3-2 | 60.0 | 21.1 | 86.4 |  |
| consensus_gap+money_delta | close | pin $1-2k | 1-1 | 50.0 | 14.5 | 175.0 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 0-1 | 0.0 | -35.5 | -100.0 |  |
| pin_rlm+pin_value | close | pin $1-2k | 1-0 | 100.0 | 60.3 | 90.9 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 1-0 | 100.0 | 60.3 | 90.9 |  |
| follow_move+pin_move | close | pin $2k+ | 13-13 | 50.0 | -1.6 | -7.8 |  |
| consensus_gap+money_level | close | pin $2k+ | 13-4 | 76.5 | 16.1 | 22.0 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 6-7 | 46.2 | 4.5 | 76.4 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 2-6 | 25.0 | -15.7 | -36.3 |  |
| money_level+money_moving | close | pin $2k+ | 8-12 | 40.0 | -14.0 | -33.7 |  |
| money_level+sharp_gap | close | pin $2k+ | 8-12 | 40.0 | -14.0 | -33.7 |  |
| money_moving+sharp_gap | close | pin $2k+ | 13-20 | 39.4 | -8.9 | -27.1 |  |
| consensus_gap+pin_value | close | pin $2k+ | 8-3 | 72.7 | 23.3 | 35.3 |  |
| follow_move+money_level | close | pin $2k+ | 8-6 | 57.1 | -3.1 | -12.2 |  |
| follow_move+money_moving | close | pin $2k+ | 7-8 | 46.7 | -2.6 | -14.3 |  |
| follow_move+sharp_gap | close | pin $2k+ | 7-8 | 46.7 | -2.6 | -14.3 |  |
| money_level+pin_move | close | pin $2k+ | 6-6 | 50.0 | -9.7 | -21.7 |  |
| money_moving+pin_move | close | pin $2k+ | 3-6 | 33.3 | -17.6 | -41.2 |  |
| pin_move+sharp_gap | close | pin $2k+ | 3-6 | 33.3 | -17.6 | -41.2 |  |
| money_delta+money_level | close | pin $2k+ | 1-0 | 100.0 | 54.4 | 90.9 |  |
| money_delta+money_moving | close | pin $2k+ | 3-5 | 37.5 | -0.5 | -23.4 |  |
| money_delta+sharp_gap | close | pin $2k+ | 3-5 | 37.5 | -0.5 | -23.4 |  |
| consensus_gap+money_moving | close | pin $2k+ | 5-4 | 55.6 | -2.7 | -12.4 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 5-4 | 55.6 | -2.7 | -12.4 |  |
| money_level+pin_value | close | pin $2k+ | 3-4 | 42.9 | -8.8 | -19.3 |  |
| money_moving+pin_value | close | pin $2k+ | 2-4 | 33.3 | -15.2 | -36.9 |  |
| pin_value+sharp_gap | close | pin $2k+ | 2-4 | 33.3 | -15.2 | -36.9 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -64.5 | -100.0 |  |
| money_level+pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -64.5 | -100.0 |  |
| money_moving+pin_rlm | close | pin $2k+ | 1-2 | 33.3 | -11.8 | -22.0 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 1-2 | 33.3 | -11.8 | -22.0 |  |
| follow_move+money_delta | close | pin $2k+ | 0-3 | 0.0 | -38.9 | -100.0 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 1-4 | 20.0 | -17.5 | -53.2 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 0-3 | 0.0 | -38.9 | -100.0 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 1-4 | 20.0 | -17.5 | -53.2 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 1-4 | 20.0 | -17.5 | -53.2 |  |
| money_level+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -35.5 | -100.0 |  |
| consensus_gap+follow_move | close | pin $2k+ | 6-0 | 100.0 | 35.5 | 55.6 |  |
| consensus_gap+pin_move | close | pin $2k+ | 5-1 | 83.3 | 25.1 | 37.7 |  |
| follow_move+pin_value | close | pin $2k+ | 3-1 | 75.0 | 25.0 | 283.6 |  |
| pin_move+pin_value | close | pin $2k+ | 3-3 | 50.0 | -0.2 | -7.1 |  |
| follow_move+pin_rlm | close | pin $2k+ | 1-1 | 50.0 | 14.5 | 17.0 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 1-1 | 50.0 | 14.5 | 17.0 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 1-0 | 100.0 | 64.5 | 1060.0 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 1-2 | 33.3 | -3.6 | -22.7 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 1-2 | 33.3 | -3.6 | -22.7 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 0-1 | 0.0 | -35.5 | -100.0 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -35.5 | -100.0 |  |
| money_delta+pin_move | close | pin $2k+ | 0-1 | 0.0 | -35.5 | -100.0 |  |
| money_delta+pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -35.5 | -100.0 |  |
| pin_move+pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -35.5 | -100.0 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -35.5 | -100.0 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 3-1 | 75.0 | 26.1 | 44.5 |  |
| consensus_gap+money_level | close | pin limit <$1k | 3-1 | 75.0 | 14.7 | 41.4 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 3-2 | 60.0 | 12.9 | 15.6 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 4-2 | 66.7 | 13.2 | 26.1 |  |
| follow_move+money_level | close | pin limit <$1k | 4-7 | 36.4 | -17.8 | -30.5 |  |
| follow_move+money_moving | close | pin limit <$1k | 4-12 | 25.0 | -22.2 | -52.2 |  |
| follow_move+pin_value | close | pin limit <$1k | 5-2 | 71.4 | 14.9 | 35.9 |  |
| money_level+money_moving | close | pin limit <$1k | 3-9 | 25.0 | -28.4 | -52.9 |  |
| money_level+pin_value | close | pin limit <$1k | 8-4 | 66.7 | 8.6 | 27.0 |  |
| money_moving+pin_value | close | pin limit <$1k | 4-5 | 44.4 | -9.0 | -16.0 |  |
| follow_move+pin_move | close | pin limit <$1k | 4-9 | 30.8 | -14.5 | -40.2 |  |
| money_level+pin_move | close | pin limit <$1k | 4-6 | 40.0 | -11.5 | -23.6 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 4-16 | 20.0 | -26.0 | -61.8 |  |
| pin_move+pin_value | close | pin limit <$1k | 3-3 | 50.0 | -5.9 | -3.8 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 4-7 | 36.4 | -4.8 | -29.4 |  |
| money_moving+pin_move | close | pin limit <$1k | 3-10 | 23.1 | -22.6 | -55.5 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 2-0 | 100.0 | 62.4 | 95.5 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 12.4 | 0.0 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 1-1 | 50.0 | 12.4 | 0.0 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 2-0 | 100.0 | 62.4 | 95.5 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 2-0 | 100.0 | 62.4 | 95.5 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 3-1 | 75.0 | 31.2 | 44.5 |  |
| follow_move+money_delta | close | pin limit <$1k | 3-5 | 37.5 | -4.3 | -27.8 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 1-7 | 12.5 | -26.7 | -75.0 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 3-8 | 27.3 | -13.9 | -47.5 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 4-11 | 26.7 | -19.6 | -49.0 |  |
| money_delta+money_moving | close | pin limit <$1k | 3-6 | 33.3 | -8.2 | -35.8 |  |
| money_delta+pin_move | close | pin limit <$1k | 1-5 | 16.7 | -22.3 | -66.7 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 1-5 | 16.7 | -22.3 | -66.7 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 2-2 | 50.0 | 11.3 | -2.3 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 3-5 | 37.5 | -4.3 | -27.8 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 3-6 | 33.3 | -8.2 | -35.8 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 1-8 | 11.1 | -28.1 | -77.8 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 2-5 | 28.6 | -10.5 | -44.2 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 3-8 | 27.3 | -13.9 | -47.5 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 1-8 | 11.1 | -28.1 | -77.8 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 2-5 | 28.6 | -13.5 | -44.2 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 1-7 | 12.5 | -26.7 | -75.0 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 1-10 | 9.1 | -34.0 | -81.8 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 1-4 | 20.0 | -18.9 | -60.0 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 1-7 | 12.5 | -26.7 | -75.0 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 1-8 | 11.1 | -28.1 | -77.8 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 2-5 | 28.6 | -10.5 | -44.2 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 2-5 | 28.6 | -10.5 | -44.2 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 3-8 | 27.3 | -13.9 | -47.5 |  |
| money_delta+pin_value | close | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 1-0 | 100.0 | 60.3 | 90.9 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 3-4 | 42.9 | -8.6 | -19.3 |  |
| money_level+sharp_gap | close | pin limit <$1k | 1-8 | 11.1 | -40.0 | -79.2 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 0-1 | 0.0 | -39.7 | -100.0 |  |
| money_delta+money_level | close | pin limit <$1k | 0-3 | 0.0 | -39.7 | -100.0 |  |
| money_level+pin_rlm | close | pin limit <$1k | 0-3 | 0.0 | -39.7 | -100.0 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 0-3 | 0.0 | -39.7 | -100.0 |  |
| rlm_quiet | early | <1k bets | 6-7 | 46.2 | 9.0 | 1.8 | 0.5 |
| money_delta | early | <1k bets | 0-1 | 0.0 | -39.7 | -100.0 | 2.0 |
| follow_move | early | <1k bets | 34-42 | 44.7 | -3.2 | -11.8 | 0.09 |
| follow_move | early | pin $1-2k | 1-1 | 50.0 | 14.5 | 21.0 | -1.2 |
| follow_move | early | pin limit <$1k | 1-0 | 100.0 | 60.3 | 90.9 | -2.0 |
| rlm_ratio | early | <1k bets | 4-6 | 40.0 | 0.5 | -15.1 | 0.73 |
| money_level | early | <1k bets | 13-15 | 46.4 | -14.1 | -27.3 | 0.03 |
| sharp_gap | early | <1k bets | 11-13 | 45.8 | 0.6 | -8.6 | 0.47 |
| money_moving | early | <1k bets | 12-10 | 54.5 | 5.9 | 8.3 | 0.59 |
| pin_value | early | <1k bets | 2-1 | 66.7 | 23.0 | 26.0 | -0.33 |
| pin_value | early | pin $1-2k | 1-1 | 50.0 | 4.4 | -6.5 | 0.5 |
| pin_value | early | pin limit <$1k | 1-0 | 100.0 | 60.3 | 90.9 | -2.0 |
| consensus_gap | early | <1k bets | 22-15 | 59.5 | 7.7 | 8.3 | 0.36 |
| follow_move+money_level | early | <1k bets | 2-7 | 22.2 | -36.5 | -66.4 | 0.33 |
| follow_move+sharp_gap | early | <1k bets | 5-8 | 38.5 | -5.8 | -20.0 | 0.64 |
| money_level+sharp_gap | early | <1k bets | 4-6 | 40.0 | -16.4 | -33.3 | 0.42 |
| follow_move+money_moving | early | <1k bets | 6-6 | 50.0 | 2.6 | 4.0 | 0.67 |
| money_level+money_moving | early | <1k bets | 5-7 | 41.7 | -16.1 | -35.1 | 0.5 |
| consensus_gap+money_level | early | <1k bets | 5-4 | 55.6 | -5.3 | -24.4 | 0.09 |
| follow_move+rlm_quiet | early | <1k bets | 6-7 | 46.2 | 9.0 | 1.8 | 0.5 |
| follow_move+rlm_ratio | early | <1k bets | 4-6 | 40.0 | 0.5 | -15.1 | 0.73 |
| rlm_quiet+rlm_ratio | early | <1k bets | 4-4 | 50.0 | 12.4 | 6.1 | 0.04 |
| rlm_quiet+sharp_gap | early | <1k bets | 4-4 | 50.0 | 12.4 | 6.1 | 0.04 |
| rlm_ratio+sharp_gap | early | <1k bets | 4-6 | 40.0 | 0.5 | -15.1 | 0.73 |
| consensus_gap+follow_move | early | <1k bets | 3-4 | 42.9 | -10.4 | -32.8 | 1.01 |
| money_moving+rlm_quiet | early | <1k bets | 5-1 | 83.3 | 45.7 | 89.4 | 1.1 |
| money_moving+rlm_ratio | early | <1k bets | 4-3 | 57.1 | 16.5 | 21.2 | 1.66 |
| money_moving+sharp_gap | early | <1k bets | 7-7 | 50.0 | 4.3 | 4.3 | 0.96 |
| consensus_gap+money_moving | early | <1k bets | 3-1 | 75.0 | 17.7 | 6.5 | 0.07 |
| consensus_gap+sharp_gap | early | <1k bets | 3-2 | 60.0 | 7.9 | 5.2 | 0.5 |
| money_level+rlm_ratio | early | <1k bets | 0-2 | 0.0 | -47.1 | -100.0 | 3.5 |
| follow_move+money_delta | early | <1k bets | 0-1 | 0.0 | -39.7 | -100.0 | 2.0 |
| money_delta+money_level | early | <1k bets | 0-1 | 0.0 | -39.7 | -100.0 | 2.0 |
| money_delta+money_moving | early | <1k bets | 0-1 | 0.0 | -39.7 | -100.0 | 2.0 |
| money_delta+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -39.7 | -100.0 | 2.0 |
| money_delta+sharp_gap | early | <1k bets | 0-1 | 0.0 | -39.7 | -100.0 | 2.0 |
| follow_move+pin_value | early | <1k bets | 1-0 | 100.0 | 60.3 | 90.9 | -2.0 |
| follow_move+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 60.3 | 90.9 | -2.0 |
