# CBB scorecard

Generated 2026-11-21 11:50 UTC. 721 graded games (18 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**685 games before 2026-11-21 (fit) · 36 on or after it (forward).**

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
sample ran **47.9% favourites** (n=720) and **50.2% overs** (n=721) and **73.1% moneyline favourites** (n=614).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-21. Nothing in the engine was chosen using these. n=36 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 3-4 | 42.9 | 35.1 | 7.8 | -0.3 | -4.3 | -1.27 | 28.6 | keep collecting (7/30) |
| follow_move | both | 12-19 | 38.7 | 47.1 | -8.4 | -5.78 | -18.6 | -0.29 | 25.8 | DROP: below break-even |
| rlm_ratio | both | 2-3 | 40.0 | 40.3 | -0.3 | -1.18 | -23.6 | -0.06 | 40.0 | keep collecting (5/30) |
| money_level | both | 9-7 | 56.2 | 63.5 | -7.2 | -1.56 | -9.7 | 1.07 | 50.0 | keep collecting (16/30) |
| sharp_gap | both | 6-6 | 50.0 | 47.5 | 2.5 | -1.01 | -8.4 | 0.52 | 41.7 | keep collecting (12/30) |
| money_moving | both | 7-4 | 63.6 | 53.5 | 10.2 | +2.07 | 18.8 | 1.12 | 54.5 | keep collecting (11/30) |
| pin_value | both | 0-1 | 0.0 | 47.2 | -47.2 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap | both | 9-3 | 75.0 | 56.7 | 18.3 | +3.21 | 26.7 | 0.53 | 58.3 | keep collecting (12/30) |
| follow_move+money_level | both | 2-3 | 40.0 | 60.8 | -20.8 | -1.98 | -39.6 | 0.36 | 20.0 | keep collecting (5/30) |
| follow_move+sharp_gap | both | 3-4 | 42.9 | 46.3 | -3.4 | -1.27 | -18.2 | -0.19 | 28.6 | keep collecting (7/30) |
| money_level+sharp_gap | both | 3-2 | 60.0 | 62.1 | -2.1 | +0.26 | 5.3 | 1.9 | 60.0 | keep collecting (5/30) |
| follow_move+money_moving | both | 4-3 | 57.1 | 50.4 | 6.7 | +0.81 | 11.6 | 0.4 | 42.9 | keep collecting (7/30) |
| money_level+money_moving | both | 4-3 | 57.1 | 62.8 | -5.6 | -0.62 | -8.9 | 1.61 | 57.1 | keep collecting (7/30) |
| consensus_gap+money_level | both | 3-1 | 75.0 | 67.7 | 7.3 | -0.02 | -0.5 | 1.17 | 75.0 | keep collecting (4/30) |
| follow_move+rlm_quiet | both | 3-4 | 42.9 | 35.1 | 7.8 | -0.3 | -4.3 | -1.27 | 28.6 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 2-3 | 40.0 | 40.3 | -0.3 | -1.18 | -23.6 | -0.06 | 40.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | both | 2-2 | 50.0 | 37.2 | 12.8 | -0.18 | -4.5 | -1.32 | 25.0 | keep collecting (4/30) |
| rlm_quiet+sharp_gap | both | 2-2 | 50.0 | 37.2 | 12.8 | -0.18 | -4.5 | -1.32 | 25.0 | keep collecting (4/30) |
| rlm_ratio+sharp_gap | both | 2-3 | 40.0 | 40.3 | -0.3 | -1.18 | -23.6 | -0.06 | 40.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 2-1 | 66.7 | 58.1 | 8.5 | +0.02 | 0.7 | -0.83 | 33.3 | keep collecting (3/30) |
| money_moving+rlm_quiet | both | 3-0 | 100.0 | 36.7 | 63.3 | +3.7 | 123.3 | 0.33 | 66.7 | keep collecting (3/30) |
| money_moving+rlm_ratio | both | 2-1 | 66.7 | 43.5 | 23.1 | +0.82 | 27.3 | 1.33 | 66.7 | keep collecting (3/30) |
| money_moving+sharp_gap | both | 4-2 | 66.7 | 54.5 | 12.1 | +1.17 | 19.6 | 1.42 | 66.7 | keep collecting (6/30) |
| consensus_gap+money_moving | both | 2-0 | 100.0 | 67.7 | 32.3 | +0.84 | 42.0 | 0.15 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | both | 1-0 | 100.0 | 67.7 | 32.3 | +0.73 | 73.0 | 2.5 | 100.0 | keep collecting (1/30) |
| money_level+rlm_ratio | both | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 1-3 | 25.0 | 32.3 | -7.3 | -1.12 | -28.0 | -0.97 | 25.0 | keep collecting (4/30) |
| rlm_quiet | total | 2-1 | 66.7 | 38.9 | 27.8 | +0.82 | 27.3 | -1.67 | 33.3 | keep collecting (3/30) |
| follow_move | moneyline | 6-4 | 60.0 | 42.9 | 17.1 | +3.76 | 37.6 | -1.51 | 20.0 | keep collecting (10/30) |
| follow_move | spread | 1-8 | 11.1 | 52.8 | -41.7 | -7.09 | -78.8 | 0.33 | 22.2 | keep collecting (9/30) |
| follow_move | total | 5-7 | 41.7 | 46.3 | -4.6 | -2.46 | -20.5 | 0.25 | 33.3 | keep collecting (12/30) |
| rlm_ratio | moneyline | 0-1 | 0.0 | 32.3 | -32.3 | -1.0 | -100.0 | -0.3 | 0.0 | keep collecting (1/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| rlm_ratio | total | 2-1 | 66.7 | 38.9 | 27.8 | +0.82 | 27.3 | -1.67 | 33.3 | keep collecting (3/30) |
| money_level | moneyline | 5-2 | 71.4 | 67.7 | 3.7 | -0.19 | -2.8 | 0.89 | 57.1 | keep collecting (7/30) |
| money_level | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level | total | 4-4 | 50.0 | 61.1 | -11.1 | -0.36 | -4.5 | 0.75 | 37.5 | keep collecting (8/30) |
| sharp_gap | moneyline | 2-2 | 50.0 | 50.0 | 0.0 | -0.65 | -16.1 | 1.8 | 75.0 | keep collecting (4/30) |
| sharp_gap | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| sharp_gap | total | 4-3 | 57.1 | 45.2 | 11.9 | +0.64 | 9.1 | -0.86 | 14.3 | keep collecting (7/30) |
| money_moving | moneyline | 4-0 | 100.0 | 58.9 | 41.1 | +3.35 | 83.7 | 1.32 | 75.0 | keep collecting (4/30) |
| money_moving | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.27 | -4.5 | 0.33 | 33.3 | keep collecting (6/30) |
| pin_value | spread | 0-1 | 0.0 | 47.2 | -47.2 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap | moneyline | 3-2 | 60.0 | 67.7 | -7.7 | -1.02 | -20.4 | 0.28 | 60.0 | keep collecting (5/30) |
| consensus_gap | spread | 3-0 | 100.0 | 47.2 | 52.8 | +2.58 | 85.8 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.65 | 41.2 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+money_level | moneyline | 3-1 | 75.0 | 67.7 | 7.3 | -0.02 | -0.5 | 1.17 | 75.0 | keep collecting (4/30) |
| follow_move+rlm_quiet | moneyline | 1-3 | 25.0 | 32.3 | -7.3 | -1.12 | -28.0 | -0.97 | 25.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 0-1 | 0.0 | 32.3 | -32.3 | -1.0 | -100.0 | -0.3 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 0-1 | 0.0 | 32.3 | -32.3 | -1.0 | -100.0 | -0.3 | 0.0 | keep collecting (1/30) |
| rlm_quiet+rlm_ratio | moneyline | 0-1 | 0.0 | 32.3 | -32.3 | -1.0 | -100.0 | -0.3 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | moneyline | 0-1 | 0.0 | 32.3 | -32.3 | -1.0 | -100.0 | -0.3 | 0.0 | keep collecting (1/30) |
| rlm_ratio+sharp_gap | moneyline | 0-1 | 0.0 | 32.3 | -32.3 | -1.0 | -100.0 | -0.3 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 1-1 | 50.0 | 67.7 | -17.7 | -0.89 | -44.5 | -2.75 | 0.0 | keep collecting (2/30) |
| consensus_gap+money_moving | moneyline | 2-0 | 100.0 | 67.7 | 32.3 | +0.84 | 42.0 | 0.15 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 1-0 | 100.0 | 67.7 | 32.3 | +0.73 | 73.0 | 2.5 | 100.0 | keep collecting (1/30) |
| money_level+money_moving | moneyline | 3-0 | 100.0 | 67.7 | 32.3 | +1.47 | 48.9 | 1.1 | 66.7 | keep collecting (3/30) |
| money_level+sharp_gap | moneyline | 2-0 | 100.0 | 67.7 | 32.3 | +1.35 | 67.8 | 2.75 | 100.0 | keep collecting (2/30) |
| money_moving+sharp_gap | moneyline | 2-0 | 100.0 | 67.7 | 32.3 | +1.35 | 67.8 | 2.75 | 100.0 | keep collecting (2/30) |
| follow_move+money_level | moneyline | 1-0 | 100.0 | 67.7 | 32.3 | +0.11 | 11.1 | -2.2 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.99 | 99.5 | -0.1 | 50.0 | keep collecting (2/30) |
| money_moving+rlm_quiet | moneyline | 1-0 | 100.0 | 32.3 | 67.7 | +1.88 | 188.0 | 2.0 | 100.0 | keep collecting (1/30) |
| follow_move+money_level | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| follow_move+money_moving | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to sharp_gap alone, not independent confirmation |
| money_level+money_moving | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+rlm_ratio | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+sharp_gap | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| money_moving+sharp_gap | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | total | 1-2 | 33.3 | 61.1 | -27.8 | -1.09 | -36.4 | -0.33 | 0.0 | keep collecting (3/30) |
| follow_move+sharp_gap | total | 3-2 | 60.0 | 47.8 | 12.2 | +0.73 | 14.5 | -1.2 | 20.0 | keep collecting (5/30) |
| money_level+sharp_gap | total | 1-1 | 50.0 | 61.1 | -11.1 | -0.09 | -4.5 | -0.5 | 0.0 | keep collecting (2/30) |
| follow_move+money_moving | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.18 | -4.5 | -0.5 | 25.0 | keep collecting (4/30) |
| money_level+money_moving | total | 1-2 | 33.3 | 61.1 | -27.8 | -1.09 | -36.4 | 1.0 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | total | 2-1 | 66.7 | 38.9 | 27.8 | +0.82 | 27.3 | -1.67 | 33.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 2-1 | 66.7 | 38.9 | 27.8 | +0.82 | 27.3 | -1.67 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 2-1 | 66.7 | 38.9 | 27.8 | +0.82 | 27.3 | -1.67 | 33.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | total | 2-1 | 66.7 | 38.9 | 27.8 | +0.82 | 27.3 | -1.67 | 33.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_ratio+sharp_gap | total | 2-1 | 66.7 | 38.9 | 27.8 | +0.82 | 27.3 | -1.67 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | total | 2-0 | 100.0 | 38.9 | 61.1 | +1.82 | 90.9 | -0.5 | 50.0 | keep collecting (2/30) |
| money_moving+rlm_ratio | total | 2-0 | 100.0 | 38.9 | 61.1 | +1.82 | 90.9 | -0.5 | 50.0 | keep collecting (2/30) |
| money_moving+sharp_gap | total | 2-1 | 66.7 | 46.3 | 20.4 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| consensus_gap+follow_move | total | 1-0 | 100.0 | 38.9 | 61.1 | +0.91 | 90.9 | 3.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 13-25 | 34.2 | 39.4 | -5.2 | -1.31 | -3.5 |  |  | DROP: below break-even |
| pin_move | both | 23-23 | 50.0 | 49.0 | 1.0 | -2.94 | -6.4 |  |  | no edge shown yet |
| money_delta | both | 14-15 | 48.3 | 41.2 | 7.1 | -1.51 | -5.2 |  |  | keep collecting (29/30) |
| pin_rlm | both | 3-5 | 37.5 | 40.0 | -2.5 | -1.71 | -21.3 |  |  | keep collecting (8/30) |
| follow_move | both | 40-46 | 46.5 | 48.9 | -2.4 | -2.06 | -2.4 |  |  | no edge shown yet |
| rlm_ratio | both | 7-14 | 33.3 | 37.9 | -4.6 | -7.07 | -33.7 |  |  | keep collecting (21/30) |
| money_level | both | 52-40 | 56.5 | 58.3 | -1.8 | -4.34 | -4.7 |  |  | no edge shown yet |
| sharp_gap | both | 30-48 | 38.5 | 48.7 | -10.2 | -22.12 | -28.4 |  |  | DROP: below break-even |
| money_moving | both | 33-48 | 40.7 | 49.7 | -9.0 | -20.98 | -25.9 |  |  | DROP: below break-even |
| pin_value | both | 22-14 | 61.1 | 50.5 | 10.6 | +17.18 | 47.7 |  |  | no edge shown yet |
| consensus_gap | both | 25-18 | 58.1 | 55.0 | 3.1 | +0.04 | 0.1 |  |  | no edge shown yet |
| follow_move+pin_move | both | 16-19 | 45.7 | 49.0 | -3.3 | -5.15 | -14.7 |  |  | no edge shown yet |
| money_delta+money_moving | both | 10-9 | 52.6 | 40.4 | 12.2 | +0.7 | 3.7 |  |  | keep collecting (19/30) |
| money_delta+sharp_gap | both | 10-8 | 55.6 | 40.5 | 15.0 | +1.7 | 9.4 |  |  | keep collecting (18/30) |
| money_moving+sharp_gap | both | 29-46 | 38.7 | 48.9 | -10.3 | -21.03 | -28.0 |  |  | DROP: below break-even |
| consensus_gap+money_level | both | 16-11 | 59.3 | 63.2 | -4.0 | -0.92 | -3.4 |  |  | keep collecting (27/30) |
| follow_move+rlm_quiet | both | 13-25 | 34.2 | 39.4 | -5.2 | -1.31 | -3.5 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | both | 6-10 | 37.5 | 41.2 | -3.7 | -3.86 | -24.1 |  |  | keep collecting (16/30) |
| consensus_gap+follow_move | both | 9-8 | 52.9 | 53.6 | -0.6 | -1.48 | -8.7 |  |  | keep collecting (17/30) |
| follow_move+money_level | both | 19-15 | 55.9 | 59.0 | -3.2 | -2.33 | -6.9 |  |  | no edge shown yet |
| money_level+money_moving | both | 25-27 | 48.1 | 55.5 | -7.5 | -8.21 | -15.8 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 22-26 | 45.8 | 54.8 | -9.0 | -8.35 | -17.4 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 7-14 | 33.3 | 54.4 | -21.1 | -9.09 | -43.3 |  |  | keep collecting (21/30) |
| consensus_gap+pin_move | both | 5-3 | 62.5 | 51.9 | 10.6 | +1.07 | 13.4 |  |  | keep collecting (8/30) |
| consensus_gap+pin_value | both | 11-6 | 64.7 | 51.7 | 13.0 | +3.61 | 21.2 |  |  | keep collecting (17/30) |
| consensus_gap+sharp_gap | both | 6-14 | 30.0 | 52.3 | -22.3 | -9.23 | -46.1 |  |  | keep collecting (20/30) |
| follow_move+money_moving | both | 14-22 | 38.9 | 48.4 | -9.5 | -11.02 | -30.6 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 6-4 | 60.0 | 50.7 | 9.3 | +11.03 | 110.3 |  |  | keep collecting (10/30) |
| follow_move+sharp_gap | both | 15-23 | 39.5 | 47.6 | -8.1 | -11.11 | -29.2 |  |  | DROP: below break-even |
| money_level+pin_move | both | 11-9 | 55.0 | 55.4 | -0.4 | -0.37 | -1.8 |  |  | keep collecting (20/30) |
| money_level+pin_value | both | 8-8 | 50.0 | 54.7 | -4.7 | -0.92 | -5.8 |  |  | keep collecting (16/30) |
| money_moving+pin_move | both | 8-10 | 44.4 | 50.8 | -6.4 | -3.14 | -17.5 |  |  | keep collecting (18/30) |
| money_moving+pin_value | both | 5-11 | 31.2 | 51.9 | -20.7 | -6.57 | -41.1 |  |  | keep collecting (16/30) |
| pin_move+pin_value | both | 7-5 | 58.3 | 50.7 | 7.6 | +1.06 | 8.8 |  |  | keep collecting (12/30) |
| pin_move+sharp_gap | both | 6-11 | 35.3 | 48.5 | -13.2 | -5.92 | -34.8 |  |  | keep collecting (17/30) |
| pin_value+sharp_gap | both | 4-10 | 28.6 | 50.6 | -22.0 | -6.48 | -46.3 |  |  | keep collecting (14/30) |
| follow_move+money_delta | both | 8-11 | 42.1 | 41.4 | 0.8 | -3.5 | -18.4 |  |  | keep collecting (19/30) |
| money_delta+pin_move | both | 4-4 | 50.0 | 38.1 | 11.9 | -0.14 | -1.8 |  |  | keep collecting (8/30) |
| money_delta+rlm_quiet | both | 4-9 | 30.8 | 38.4 | -7.7 | -5.19 | -39.9 |  |  | keep collecting (13/30) |
| follow_move+rlm_ratio | both | 7-14 | 33.3 | 37.9 | -4.6 | -7.07 | -33.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | both | 2-10 | 16.7 | 35.0 | -18.4 | -8.09 | -67.4 |  |  | keep collecting (12/30) |
| money_moving+rlm_ratio | both | 7-12 | 36.8 | 38.5 | -1.7 | -5.07 | -26.7 |  |  | keep collecting (19/30) |
| rlm_quiet+rlm_ratio | both | 2-11 | 15.4 | 34.3 | -18.9 | -9.09 | -69.9 |  |  | keep collecting (13/30) |
| rlm_quiet+sharp_gap | both | 2-12 | 14.3 | 34.6 | -20.3 | -10.09 | -72.1 |  |  | keep collecting (14/30) |
| rlm_ratio+sharp_gap | both | 7-14 | 33.3 | 37.9 | -4.6 | -7.07 | -33.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | both | 4-1 | 80.0 | 45.0 | 35.0 | +2.72 | 54.4 |  |  | keep collecting (5/30) |
| consensus_gap+rlm_quiet | both | 3-4 | 42.9 | 37.1 | 5.8 | -1.18 | -16.9 |  |  | keep collecting (7/30) |
| consensus_gap+rlm_ratio | both | 2-3 | 40.0 | 33.6 | 6.4 | -1.09 | -21.8 |  |  | keep collecting (5/30) |
| money_delta+rlm_ratio | both | 6-6 | 50.0 | 41.6 | 8.4 | -0.41 | -3.4 |  |  | keep collecting (12/30) |
| consensus_gap+pin_rlm | both | 1-2 | 33.3 | 46.3 | -13.0 | -1.0 | -33.3 |  |  | keep collecting (3/30) |
| money_level+pin_rlm | both | 1-2 | 33.3 | 48.5 | -15.2 | -1.05 | -34.9 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | both | 3-4 | 42.9 | 41.1 | 1.7 | -0.71 | -10.1 |  |  | keep collecting (7/30) |
| pin_rlm+sharp_gap | both | 3-5 | 37.5 | 40.0 | -2.5 | -1.71 | -21.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | both | 3-2 | 60.0 | 42.0 | 18.0 | +0.81 | 16.3 |  |  | keep collecting (5/30) |
| consensus_gap+money_delta | both | 2-1 | 66.7 | 34.5 | 32.2 | +0.91 | 30.3 |  |  | keep collecting (3/30) |
| follow_move+pin_rlm | both | 3-3 | 50.0 | 35.6 | 14.4 | +0.29 | 4.9 |  |  | keep collecting (6/30) |
| money_delta+pin_rlm | both | 2-1 | 66.7 | 36.7 | 30.0 | +0.95 | 31.7 |  |  | keep collecting (3/30) |
| pin_move+pin_rlm | both | 2-4 | 33.3 | 36.7 | -3.3 | -2.05 | -34.1 |  |  | keep collecting (6/30) |
| pin_move+rlm_ratio | both | 2-3 | 40.0 | 36.2 | 3.8 | -1.05 | -21.0 |  |  | keep collecting (5/30) |
| pin_rlm+rlm_quiet | both | 1-2 | 33.3 | 34.5 | -1.1 | -1.0 | -33.3 |  |  | keep collecting (3/30) |
| pin_rlm+rlm_ratio | both | 3-3 | 50.0 | 35.6 | 14.4 | +0.29 | 4.9 |  |  | keep collecting (6/30) |
| money_delta+pin_value | both | 2-1 | 66.7 | 46.3 | 20.4 | +0.78 | 26.0 |  |  | keep collecting (3/30) |
| pin_value+rlm_quiet | both | 3-1 | 75.0 | 40.7 | 34.3 | +11.42 | 285.5 |  |  | keep collecting (4/30) |
| pin_value+rlm_ratio | both | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 |  |  | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 38.9 | -38.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 5-9 | 35.7 | 32.3 | 3.5 | +7.24 | 51.7 |  |  | keep collecting (14/30) |
| rlm_quiet | spread | 3-4 | 42.9 | 52.0 | -9.1 | -1.19 | -16.9 |  |  | keep collecting (7/30) |
| rlm_quiet | total | 5-12 | 29.4 | 40.2 | -10.8 | -7.37 | -43.3 |  |  | keep collecting (17/30) |
| pin_move | moneyline | 6-2 | 75.0 | 50.0 | 25.0 | +2.71 | 33.9 |  |  | keep collecting (8/30) |
| pin_move | spread | 10-8 | 55.6 | 51.2 | 4.3 | +0.89 | 5.0 |  |  | keep collecting (18/30) |
| pin_move | total | 7-13 | 35.0 | 46.7 | -11.7 | -6.55 | -32.7 |  |  | keep collecting (20/30) |
| money_delta | moneyline | 2-4 | 33.3 | 32.3 | 1.1 | -1.62 | -27.0 |  |  | keep collecting (6/30) |
| money_delta | spread | 3-3 | 50.0 | 49.1 | 0.9 | -0.2 | -3.4 |  |  | keep collecting (6/30) |
| money_delta | total | 9-8 | 52.9 | 41.5 | 11.4 | +0.31 | 1.8 |  |  | keep collecting (17/30) |
| pin_rlm | moneyline | 2-2 | 50.0 | 41.1 | 8.9 | +0.34 | 8.5 |  |  | keep collecting (4/30) |
| pin_rlm | total | 1-3 | 25.0 | 38.9 | -13.9 | -2.05 | -51.2 |  |  | keep collecting (4/30) |
| follow_move | moneyline | 17-13 | 56.7 | 47.6 | 9.0 | +9.84 | 32.8 |  |  | no edge shown yet |
| follow_move | spread | 9-14 | 39.1 | 51.3 | -12.2 | -5.75 | -25.0 |  |  | keep collecting (23/30) |
| follow_move | total | 14-19 | 42.4 | 48.3 | -5.9 | -6.14 | -18.6 |  |  | no edge shown yet |
| rlm_ratio | moneyline | 2-9 | 18.2 | 32.3 | -14.1 | -6.66 | -60.5 |  |  | keep collecting (11/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 47.2 | -47.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_ratio | total | 5-4 | 55.6 | 43.8 | 11.7 | +0.59 | 6.6 |  |  | keep collecting (9/30) |
| money_level | moneyline | 20-11 | 64.5 | 66.6 | -2.1 | -4.35 | -14.0 |  |  | no edge shown yet |
| money_level | spread | 12-13 | 48.0 | 49.2 | -1.2 | -2.16 | -8.6 |  |  | keep collecting (25/30) |
| money_level | total | 20-16 | 55.6 | 57.4 | -1.9 | +2.17 | 6.0 |  |  | no edge shown yet |
| sharp_gap | moneyline | 8-17 | 32.0 | 45.0 | -13.0 | -11.05 | -44.2 |  |  | keep collecting (25/30) |
| sharp_gap | spread | 9-16 | 36.0 | 49.0 | -13.0 | -8.01 | -32.0 |  |  | keep collecting (25/30) |
| sharp_gap | total | 13-15 | 46.4 | 51.6 | -5.2 | -3.07 | -10.9 |  |  | keep collecting (28/30) |
| money_moving | moneyline | 10-15 | 40.0 | 47.9 | -7.9 | -8.78 | -35.1 |  |  | keep collecting (25/30) |
| money_moving | spread | 9-16 | 36.0 | 49.0 | -13.0 | -8.01 | -32.0 |  |  | keep collecting (25/30) |
| money_moving | total | 14-17 | 45.2 | 51.8 | -6.6 | -4.2 | -13.5 |  |  | no edge shown yet |
| pin_value | moneyline | 3-0 | 100.0 | 44.1 | 55.9 | +14.59 | 486.2 |  |  | keep collecting (3/30) |
| pin_value | spread | 11-4 | 73.3 | 49.4 | 23.9 | +5.45 | 36.3 |  |  | keep collecting (15/30) |
| pin_value | total | 8-10 | 44.4 | 52.5 | -8.0 | -2.85 | -15.9 |  |  | keep collecting (18/30) |
| consensus_gap | moneyline | 11-10 | 52.4 | 57.6 | -5.2 | -4.27 | -20.4 |  |  | keep collecting (21/30) |
| consensus_gap | spread | 6-2 | 75.0 | 48.6 | 26.4 | +3.13 | 39.1 |  |  | keep collecting (8/30) |
| consensus_gap | total | 8-6 | 57.1 | 54.8 | 2.4 | +1.18 | 8.5 |  |  | keep collecting (14/30) |
| consensus_gap+money_level | moneyline | 9-5 | 64.3 | 67.7 | -3.5 | -1.16 | -8.3 |  |  | keep collecting (14/30) |
| follow_move+pin_move | moneyline | 6-2 | 75.0 | 50.0 | 25.0 | +2.71 | 33.9 |  |  | redundant -- identical record to pin_move alone, not independent confirmation |
| follow_move+rlm_quiet | moneyline | 5-9 | 35.7 | 32.3 | 3.5 | +7.24 | 51.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | moneyline | 2-2 | 50.0 | 32.3 | 17.7 | +0.42 | 10.5 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | moneyline | 6-4 | 60.0 | 53.5 | 6.5 | -0.21 | -2.1 |  |  | keep collecting (10/30) |
| follow_move+money_level | moneyline | 10-4 | 71.4 | 65.2 | 6.2 | +0.35 | 2.5 |  |  | keep collecting (14/30) |
| money_moving+sharp_gap | moneyline | 8-15 | 34.8 | 46.1 | -11.4 | -9.05 | -39.4 |  |  | keep collecting (23/30) |
| follow_move+money_moving | moneyline | 7-7 | 50.0 | 44.9 | 5.1 | -2.43 | -17.4 |  |  | keep collecting (14/30) |
| follow_move+sharp_gap | moneyline | 7-9 | 43.8 | 43.3 | 0.4 | -4.43 | -27.7 |  |  | keep collecting (16/30) |
| money_level+money_moving | moneyline | 7-5 | 58.3 | 64.8 | -6.5 | -2.5 | -20.8 |  |  | keep collecting (12/30) |
| money_level+sharp_gap | moneyline | 5-5 | 50.0 | 64.2 | -14.2 | -2.77 | -27.7 |  |  | keep collecting (10/30) |
| follow_move+rlm_ratio | moneyline | 2-9 | 18.2 | 32.3 | -14.1 | -6.66 | -60.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | moneyline | 1-6 | 14.3 | 32.3 | -18.0 | -5.0 | -71.4 |  |  | keep collecting (7/30) |
| money_moving+rlm_ratio | moneyline | 2-7 | 22.2 | 32.3 | -10.0 | -4.66 | -51.8 |  |  | keep collecting (9/30) |
| rlm_quiet+rlm_ratio | moneyline | 1-8 | 11.1 | 32.3 | -21.1 | -7.0 | -77.8 |  |  | keep collecting (9/30) |
| rlm_quiet+sharp_gap | moneyline | 1-8 | 11.1 | 32.3 | -21.1 | -7.0 | -77.8 |  |  | keep collecting (9/30) |
| rlm_ratio+sharp_gap | moneyline | 2-9 | 18.2 | 32.3 | -14.1 | -6.66 | -60.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 4-7 | 36.4 | 54.8 | -18.5 | -4.81 | -43.8 |  |  | keep collecting (11/30) |
| consensus_gap+rlm_quiet | moneyline | 1-3 | 25.0 | 32.3 | -7.3 | -2.0 | -50.0 |  |  | keep collecting (4/30) |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 32.3 | -7.3 | -2.0 | -50.0 |  |  | keep collecting (4/30) |
| consensus_gap+sharp_gap | moneyline | 3-8 | 27.3 | 51.6 | -24.3 | -5.95 | -54.1 |  |  | keep collecting (11/30) |
| consensus_gap+pin_rlm | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | +0.0 | 0.0 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 67.7 | -67.7 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 2-1 | 66.7 | 44.1 | 22.6 | +1.34 | 44.7 |  |  | keep collecting (3/30) |
| pin_rlm+sharp_gap | moneyline | 2-2 | 50.0 | 41.1 | 8.9 | +0.34 | 8.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 1-0 | 100.0 | 67.7 | 32.3 | +0.89 | 88.5 |  |  | keep collecting (1/30) |
| money_level+rlm_ratio | moneyline | 0-1 | 0.0 | 32.3 | -32.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+pin_move | moneyline | 3-0 | 100.0 | 55.9 | 44.1 | +2.33 | 77.5 |  |  | keep collecting (3/30) |
| money_level+pin_move | moneyline | 4-0 | 100.0 | 67.7 | 32.3 | +2.29 | 57.2 |  |  | keep collecting (4/30) |
| consensus_gap+money_delta | moneyline | 1-1 | 50.0 | 32.3 | 17.7 | +0.0 | 0.0 |  |  | keep collecting (2/30) |
| follow_move+money_delta | moneyline | 1-2 | 33.3 | 32.3 | 1.1 | -1.0 | -33.3 |  |  | keep collecting (3/30) |
| follow_move+pin_rlm | moneyline | 2-1 | 66.7 | 32.3 | 34.4 | +1.34 | 44.7 |  |  | keep collecting (3/30) |
| money_delta+money_moving | moneyline | 2-4 | 33.3 | 32.3 | 1.1 | -1.62 | -27.0 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_move | moneyline | 1-0 | 100.0 | 32.3 | 67.7 | +1.0 | 100.0 |  |  | keep collecting (1/30) |
| money_delta+pin_rlm | moneyline | 1-0 | 100.0 | 32.3 | 67.7 | +1.0 | 100.0 |  |  | keep collecting (1/30) |
| money_delta+rlm_quiet | moneyline | 1-2 | 33.3 | 32.3 | 1.1 | -1.0 | -33.3 |  |  | keep collecting (3/30) |
| money_delta+rlm_ratio | moneyline | 1-2 | 33.3 | 32.3 | 1.1 | -1.0 | -33.3 |  |  | keep collecting (3/30) |
| money_delta+sharp_gap | moneyline | 2-4 | 33.3 | 32.3 | 1.1 | -1.62 | -27.0 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| money_moving+pin_move | moneyline | 3-0 | 100.0 | 55.9 | 44.1 | +2.38 | 79.4 |  |  | keep collecting (3/30) |
| pin_move+pin_rlm | moneyline | 1-1 | 50.0 | 32.3 | 17.7 | +0.0 | 0.0 |  |  | keep collecting (2/30) |
| pin_move+rlm_ratio | moneyline | 1-1 | 50.0 | 32.3 | 17.7 | +0.0 | 0.0 |  |  | keep collecting (2/30) |
| pin_move+sharp_gap | moneyline | 3-1 | 75.0 | 50.0 | 25.0 | +1.38 | 34.6 |  |  | keep collecting (4/30) |
| pin_rlm+rlm_quiet | moneyline | 1-1 | 50.0 | 32.3 | 17.7 | +0.0 | 0.0 |  |  | keep collecting (2/30) |
| pin_rlm+rlm_ratio | moneyline | 2-1 | 66.7 | 32.3 | 34.4 | +1.34 | 44.7 |  |  | keep collecting (3/30) |
| follow_move+pin_value | moneyline | 1-0 | 100.0 | 32.3 | 67.7 | +10.6 | 1060.0 |  |  | keep collecting (1/30) |
| pin_value+rlm_quiet | moneyline | 1-0 | 100.0 | 32.3 | 67.7 | +10.6 | 1060.0 |  |  | keep collecting (1/30) |
| follow_move+pin_move | spread | 5-7 | 41.7 | 51.9 | -10.2 | -2.53 | -21.1 |  |  | keep collecting (12/30) |
| money_moving+sharp_gap | spread | 9-16 | 36.0 | 49.0 | -13.0 | -8.01 | -32.0 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 3-4 | 42.9 | 52.0 | -9.1 | -1.19 | -16.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | spread | 7-11 | 38.9 | 48.8 | -9.9 | -4.82 | -26.8 |  |  | keep collecting (18/30) |
| money_level+sharp_gap | spread | 7-11 | 38.9 | 48.8 | -9.9 | -4.82 | -26.8 |  |  | keep collecting (18/30) |
| pin_move+rlm_quiet | spread | 1-2 | 33.3 | 52.8 | -19.4 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| consensus_gap+pin_value | spread | 6-2 | 75.0 | 48.6 | 26.4 | +3.13 | 39.1 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| follow_move+money_level | spread | 2-4 | 33.3 | 50.9 | -17.6 | -2.13 | -35.5 |  |  | keep collecting (6/30) |
| follow_move+money_moving | spread | 0-5 | 0.0 | 50.6 | -50.6 | -5.0 | -100.0 |  |  | keep collecting (5/30) |
| follow_move+sharp_gap | spread | 0-5 | 0.0 | 50.6 | -50.6 | -5.0 | -100.0 |  |  | keep collecting (5/30) |
| money_level+pin_move | spread | 3-4 | 42.9 | 50.4 | -7.5 | -1.3 | -18.5 |  |  | keep collecting (7/30) |
| money_moving+pin_move | spread | 1-4 | 20.0 | 49.4 | -29.4 | -3.17 | -63.3 |  |  | keep collecting (5/30) |
| pin_move+sharp_gap | spread | 1-4 | 20.0 | 49.4 | -29.4 | -3.17 | -63.3 |  |  | keep collecting (5/30) |
| money_delta+money_level | spread | 1-0 | 100.0 | 47.2 | 52.8 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+money_moving | spread | 2-1 | 66.7 | 47.2 | 19.4 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| money_delta+sharp_gap | spread | 2-1 | 66.7 | 47.2 | 19.4 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| consensus_gap+money_level | spread | 1-2 | 33.3 | 49.1 | -15.7 | -1.12 | -37.4 |  |  | keep collecting (3/30) |
| consensus_gap+money_moving | spread | 0-2 | 0.0 | 47.2 | -47.2 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+sharp_gap | spread | 0-2 | 0.0 | 47.2 | -47.2 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+pin_value | spread | 3-2 | 60.0 | 49.4 | 10.6 | +0.62 | 12.4 |  |  | keep collecting (5/30) |
| money_moving+pin_value | spread | 1-4 | 20.0 | 49.4 | -29.4 | -3.17 | -63.3 |  |  | keep collecting (5/30) |
| pin_value+sharp_gap | spread | 1-4 | 20.0 | 49.4 | -29.4 | -3.17 | -63.3 |  |  | keep collecting (5/30) |
| follow_move+money_delta | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 47.2 | -47.2 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | spread | 0-1 | 0.0 | 47.2 | -47.2 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 47.2 | -47.2 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 47.2 | -47.2 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 3-0 | 100.0 | 50.9 | 49.1 | +2.65 | 88.4 |  |  | keep collecting (3/30) |
| pin_move+pin_value | spread | 6-1 | 85.7 | 49.6 | 36.1 | +4.15 | 59.3 |  |  | keep collecting (7/30) |
| consensus_gap+pin_move | spread | 2-1 | 66.7 | 49.1 | 17.6 | +0.74 | 24.7 |  |  | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 1-0 | 100.0 | 52.8 | 47.2 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 52.8 | 47.2 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| pin_value+rlm_quiet | spread | 1-0 | 100.0 | 52.8 | 47.2 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+rlm_quiet | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta+money_moving | total | 6-4 | 60.0 | 43.3 | 16.7 | +1.5 | 15.0 |  |  | keep collecting (10/30) |
| money_delta+sharp_gap | total | 6-3 | 66.7 | 43.8 | 22.8 | +2.5 | 27.8 |  |  | keep collecting (9/30) |
| money_moving+sharp_gap | total | 12-15 | 44.4 | 51.2 | -6.8 | -3.97 | -14.7 |  |  | keep collecting (27/30) |
| follow_move+rlm_quiet | total | 5-12 | 29.4 | 40.2 | -10.8 | -7.37 | -43.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+follow_move | total | 2-4 | 33.3 | 53.7 | -20.4 | -2.18 | -36.4 |  |  | keep collecting (6/30) |
| consensus_gap+money_level | total | 6-4 | 60.0 | 61.1 | -1.1 | +1.37 | 13.7 |  |  | keep collecting (10/30) |
| consensus_gap+money_moving | total | 3-5 | 37.5 | 55.6 | -18.1 | -2.27 | -28.4 |  |  | keep collecting (8/30) |
| consensus_gap+pin_move | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+pin_value | total | 4-4 | 50.0 | 52.8 | -2.8 | -0.41 | -5.2 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | total | 3-4 | 42.9 | 54.8 | -11.9 | -1.27 | -18.2 |  |  | keep collecting (7/30) |
| follow_move+money_level | total | 7-7 | 50.0 | 56.3 | -6.3 | -0.55 | -3.9 |  |  | keep collecting (14/30) |
| follow_move+money_moving | total | 7-10 | 41.2 | 50.7 | -9.5 | -3.59 | -21.1 |  |  | keep collecting (17/30) |
| follow_move+pin_move | total | 5-10 | 33.3 | 46.3 | -13.0 | -5.33 | -35.5 |  |  | keep collecting (15/30) |
| follow_move+pin_value | total | 2-4 | 33.3 | 53.7 | -20.4 | -2.22 | -37.0 |  |  | keep collecting (6/30) |
| follow_move+sharp_gap | total | 8-9 | 47.1 | 50.7 | -3.6 | -1.68 | -9.9 |  |  | keep collecting (17/30) |
| money_level+money_moving | total | 11-11 | 50.0 | 56.1 | -6.1 | -0.88 | -4.0 |  |  | keep collecting (22/30) |
| money_level+pin_move | total | 4-5 | 44.4 | 53.7 | -9.3 | -1.36 | -15.1 |  |  | keep collecting (9/30) |
| money_level+pin_value | total | 5-6 | 45.5 | 57.1 | -11.6 | -1.54 | -14.0 |  |  | keep collecting (11/30) |
| money_level+sharp_gap | total | 10-10 | 50.0 | 55.6 | -5.6 | -0.75 | -3.8 |  |  | keep collecting (20/30) |
| money_moving+pin_move | total | 4-6 | 40.0 | 50.0 | -10.0 | -2.36 | -23.6 |  |  | keep collecting (10/30) |
| money_moving+pin_value | total | 4-7 | 36.4 | 53.0 | -16.7 | -3.4 | -30.9 |  |  | keep collecting (11/30) |
| pin_move+pin_value | total | 1-4 | 20.0 | 52.2 | -32.2 | -3.09 | -61.8 |  |  | keep collecting (5/30) |
| pin_move+sharp_gap | total | 2-6 | 25.0 | 47.2 | -22.2 | -4.14 | -51.7 |  |  | keep collecting (8/30) |
| pin_value+sharp_gap | total | 3-6 | 33.3 | 51.2 | -17.9 | -3.31 | -36.8 |  |  | keep collecting (9/30) |
| follow_move+money_delta | total | 7-7 | 50.0 | 42.1 | 7.9 | -0.5 | -3.6 |  |  | keep collecting (14/30) |
| money_delta+pin_move | total | 3-4 | 42.9 | 38.9 | 4.0 | -1.14 | -16.3 |  |  | keep collecting (7/30) |
| money_delta+rlm_quiet | total | 3-6 | 33.3 | 38.9 | -5.6 | -3.19 | -35.4 |  |  | keep collecting (9/30) |
| pin_move+rlm_quiet | total | 3-6 | 33.3 | 41.4 | -8.0 | -3.19 | -35.4 |  |  | keep collecting (9/30) |
| follow_move+rlm_ratio | total | 5-4 | 55.6 | 43.8 | 11.7 | +0.59 | 6.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | total | 5-3 | 62.5 | 44.4 | 18.1 | +1.59 | 19.9 |  |  | keep collecting (8/30) |
| money_moving+rlm_quiet | total | 1-4 | 20.0 | 38.9 | -18.9 | -3.09 | -61.8 |  |  | keep collecting (5/30) |
| money_moving+rlm_ratio | total | 5-4 | 55.6 | 43.8 | 11.7 | +0.59 | 6.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 1-3 | 25.0 | 38.9 | -13.9 | -2.09 | -52.3 |  |  | keep collecting (4/30) |
| rlm_quiet+sharp_gap | total | 1-4 | 20.0 | 38.9 | -18.9 | -3.09 | -61.8 |  |  | keep collecting (5/30) |
| rlm_ratio+sharp_gap | total | 5-4 | 55.6 | 43.8 | 11.7 | +0.59 | 6.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | total | 1-0 | 100.0 | 38.9 | 61.1 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| consensus_gap+rlm_quiet | total | 1-1 | 50.0 | 38.9 | 11.1 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| consensus_gap+rlm_ratio | total | 1-0 | 100.0 | 38.9 | 61.1 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+pin_value | total | 2-1 | 66.7 | 46.3 | 20.4 | +0.78 | 26.0 |  |  | keep collecting (3/30) |
| pin_value+rlm_quiet | total | 1-1 | 50.0 | 38.9 | 11.1 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| pin_value+rlm_ratio | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 |  |  | keep collecting (2/30) |
| follow_move+pin_rlm | total | 1-2 | 33.3 | 38.9 | -5.6 | -1.05 | -34.9 |  |  | keep collecting (3/30) |
| money_delta+money_level | total | 3-1 | 75.0 | 44.4 | 30.6 | +1.81 | 45.3 |  |  | keep collecting (4/30) |
| money_delta+pin_rlm | total | 1-1 | 50.0 | 38.9 | 11.1 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | total | 1-1 | 50.0 | 38.9 | 11.1 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | total | 3-1 | 75.0 | 44.4 | 30.6 | +1.81 | 45.3 |  |  | keep collecting (4/30) |
| money_moving+pin_rlm | total | 1-3 | 25.0 | 38.9 | -13.9 | -2.05 | -51.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | total | 1-3 | 25.0 | 38.9 | -13.9 | -2.05 | -51.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 1-2 | 33.3 | 38.9 | -5.6 | -1.05 | -34.9 |  |  | keep collecting (3/30) |
| pin_rlm+rlm_ratio | total | 1-2 | 33.3 | 38.9 | -5.6 | -1.05 | -34.9 |  |  | keep collecting (3/30) |
| pin_rlm+sharp_gap | total | 1-3 | 25.0 | 38.9 | -13.9 | -2.05 | -51.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | total | 0-1 | 0.0 | 38.9 | -38.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+pin_rlm | total | 0-1 | 0.0 | 38.9 | -38.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+pin_value | total | 0-1 | 0.0 | 38.9 | -38.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |

# FIT (in-sample — this is the hypothesis)

Games before 2026-11-21. The engine was built by looking at these, so a strong record here is expected and proves nothing. n=685 games.

## EARLY  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 31-37 | 45.6 | 35.9 | 9.7 | +10.5 | 15.4 | 0.15 | 42.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move | both | 5-9 | 35.7 | 48.2 | -12.5 | -5.1 | -36.4 | 0.22 | 50.0 | keep collecting (14/30) |
| money_delta | both | 10-7 | 58.8 | 41.8 | 17.0 | +4.43 | 26.1 | -0.22 | 29.4 | keep collecting (17/30) |
| pin_rlm | both | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | both | 475-404 | 54.0 | 52.4 | 1.6 | -45.57 | -5.2 | 0.19 | 41.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | both | 30-18 | 62.5 | 38.5 | 24.0 | +20.45 | 42.6 | 0.37 | 50.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | both | 170-110 | 60.7 | 59.0 | 1.7 | -12.24 | -4.4 | -0.11 | 39.6 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 144-121 | 54.3 | 48.3 | 6.0 | +19.0 | 7.2 | 0.28 | 43.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | both | 102-82 | 55.4 | 51.2 | 4.3 | -0.81 | -0.4 | 0.04 | 41.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | both | 49-48 | 50.5 | 48.3 | 2.2 | -4.43 | -4.6 | 0.1 | 38.1 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.2 | -31.2 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 220-290 | 43.1 | 47.2 | -4.1 | -61.37 | -12.0 | 0.39 | 45.1 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | both | 33-28 | 54.1 | 63.8 | -9.7 | -9.61 | -15.8 | 0.35 | 49.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | both | 17-23 | 42.5 | 46.7 | -4.2 | -6.42 | -16.1 | 0.25 | 42.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_value | both | 19-28 | 40.4 | 46.5 | -6.1 | -11.54 | -24.5 | 0.39 | 48.9 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_quiet | both | 31-37 | 45.6 | 35.9 | 9.7 | +10.5 | 15.4 | 0.15 | 42.6 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 30-18 | 62.5 | 38.5 | 24.0 | +20.45 | 42.6 | 0.37 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 76-38 | 66.7 | 49.9 | 16.8 | +25.22 | 22.1 | 0.35 | 47.4 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 64-40 | 61.5 | 58.1 | 3.4 | -0.87 | -0.8 | -0.16 | 47.1 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 11-9 | 55.0 | 49.8 | 5.2 | +0.81 | 4.0 | 0.4 | 45.0 | keep collecting (20/30) |
| money_moving+pin_value | both | 8-5 | 61.5 | 49.9 | 11.6 | +2.04 | 15.7 | 0.31 | 38.5 | keep collecting (13/30) |
| rlm_quiet+rlm_ratio | both | 17-11 | 60.7 | 35.9 | 24.8 | +14.16 | 50.6 | -0.12 | 46.4 | keep collecting (28/30) |
| rlm_quiet+sharp_gap | both | 19-14 | 57.6 | 35.9 | 21.7 | +12.97 | 39.3 | -0.13 | 45.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | both | 30-18 | 62.5 | 38.5 | 24.0 | +20.45 | 42.6 | 0.37 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 97-60 | 61.8 | 55.7 | 6.1 | +4.17 | 2.7 | 0.14 | 43.3 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 60-48 | 55.6 | 48.6 | 6.9 | +5.0 | 4.6 | 0.18 | 44.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_level | both | 3-2 | 60.0 | 45.8 | 14.2 | +1.46 | 29.2 | 1.16 | 60.0 | keep collecting (5/30) |
| money_delta+money_moving | both | 9-7 | 56.2 | 41.3 | 14.9 | +3.53 | 22.0 | -0.23 | 31.2 | keep collecting (16/30) |
| money_delta+pin_value | both | 3-1 | 75.0 | 50.0 | 25.0 | +1.61 | 40.3 | 0.0 | 25.0 | keep collecting (4/30) |
| money_delta+sharp_gap | both | 7-5 | 58.3 | 40.5 | 17.9 | +3.78 | 31.5 | -0.31 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | both | 13-8 | 61.9 | 48.8 | 13.1 | +3.66 | 17.4 | -0.18 | 33.3 | keep collecting (21/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 32-41 | 43.8 | 51.2 | -7.4 | -15.02 | -20.6 | 0.72 | 54.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_quiet | both | 4-7 | 36.4 | 37.2 | -0.8 | -2.99 | -27.1 | 0.95 | 72.7 | keep collecting (11/30) |
| follow_move+pin_value | both | 20-17 | 54.1 | 48.8 | 5.2 | +0.41 | 1.1 | -0.12 | 29.7 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 42.2 | -25.5 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 26-45 | 36.6 | 45.5 | -8.9 | -10.29 | -14.5 | 0.88 | 49.3 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | both | 91-44 | 67.4 | 60.2 | 7.2 | +1.24 | 0.9 | 0.0 | 43.7 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 11-7 | 61.1 | 41.4 | 19.8 | +4.43 | 24.6 | 1.22 | 61.1 | keep collecting (18/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 44.2 | 5.8 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 53-29 | 64.6 | 52.9 | 11.7 | +9.8 | 12.0 | 0.29 | 51.2 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 3-0 | 100.0 | 49.1 | 50.9 | +2.61 | 87.1 | 0.0 | 0.0 | keep collecting (3/30) |
| follow_move+money_delta | both | 5-3 | 62.5 | 41.1 | 21.4 | +3.95 | 49.4 | 0.05 | 37.5 | keep collecting (8/30) |
| money_delta+rlm_quiet | both | 2-2 | 50.0 | 37.9 | 12.1 | +1.53 | 38.3 | -2.1 | 0.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | both | 11-11 | 50.0 | 36.1 | 13.9 | +3.87 | 17.6 | 0.26 | 40.9 | keep collecting (22/30) |
| money_moving+rlm_ratio | both | 12-8 | 60.0 | 40.7 | 19.3 | +6.66 | 33.3 | 0.16 | 45.0 | keep collecting (20/30) |
| consensus_gap+rlm_ratio | both | 4-4 | 50.0 | 38.5 | 11.5 | +0.09 | 1.1 | 0.69 | 62.5 | keep collecting (8/30) |
| pin_move+pin_value | both | 1-4 | 20.0 | 49.1 | -29.1 | -3.09 | -61.8 | 0.2 | 20.0 | keep collecting (5/30) |
| follow_move+pin_move | both | 5-3 | 62.5 | 52.3 | 10.2 | +0.9 | 11.2 | 0.42 | 62.5 | keep collecting (8/30) |
| consensus_gap+pin_move | both | 0-5 | 0.0 | 44.5 | -44.5 | -5.0 | -100.0 | 0.26 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | both | 2-2 | 50.0 | 55.8 | -5.8 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 26.6 | 23.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 26.6 | 23.4 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | both | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.2 | -51.2 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-1 | 66.7 | 49.9 | 16.8 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 2-1 | 66.7 | 34.5 | 32.2 | +3.34 | 111.3 | 0.87 | 66.7 | keep collecting (3/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 16-25 | 39.0 | 26.6 | 12.4 | +8.89 | 21.7 | -0.07 | 43.9 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 12-10 | 54.5 | 50.2 | 4.3 | +0.95 | 4.3 | 0.77 | 50.0 | keep collecting (22/30) |
| pin_move | moneyline | 2-3 | 40.0 | 45.3 | -5.3 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-4 | 20.0 | 49.6 | -29.6 | -3.09 | -61.8 | 0.4 | 40.0 | keep collecting (5/30) |
| pin_move | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.14 | -3.5 | 0.25 | 50.0 | keep collecting (4/30) |
| money_delta | moneyline | 2-4 | 33.3 | 26.6 | 6.7 | +0.34 | 5.7 | -1.45 | 33.3 | keep collecting (6/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 7-2 | 77.8 | 50.2 | 27.6 | +4.26 | 47.4 | 0.44 | 22.2 | keep collecting (9/30) |
| pin_rlm | moneyline | 1-2 | 33.3 | 26.6 | 6.7 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | moneyline | 195-127 | 60.6 | 56.8 | 3.7 | -25.09 | -7.8 | 0.19 | 46.0 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 128-141 | 47.6 | 49.7 | -2.1 | -23.21 | -8.6 | 0.02 | 34.2 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | total | 152-136 | 52.8 | 50.0 | 2.8 | +2.73 | 0.9 | 0.34 | 44.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | moneyline | 13-11 | 54.2 | 26.6 | 27.6 | +11.71 | 48.8 | 0.4 | 58.3 | keep collecting (24/30) |
| rlm_ratio | spread | 3-2 | 60.0 | 51.2 | 8.8 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 14-5 | 73.7 | 50.3 | 23.4 | +7.9 | 41.6 | 0.58 | 52.6 | keep collecting (19/30) |
| money_level | moneyline | 97-39 | 71.3 | 68.9 | 2.4 | -7.41 | -5.4 | -0.24 | 44.9 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-17 | 50.0 | 49.3 | 0.7 | -1.69 | -5.0 | 0.88 | 50.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | total | 56-54 | 50.9 | 49.8 | 1.1 | -3.14 | -2.9 | -0.26 | 30.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 61-62 | 49.6 | 46.4 | 3.2 | +2.59 | 2.1 | 0.32 | 49.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | spread | 20-14 | 58.8 | 49.8 | 9.1 | +4.0 | 11.8 | 0.65 | 38.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 63-45 | 58.3 | 50.1 | 8.3 | +12.4 | 11.5 | 0.12 | 37.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | moneyline | 44-42 | 51.2 | 52.7 | -1.6 | -13.4 | -15.6 | -0.15 | 46.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | spread | 18-5 | 78.3 | 49.2 | 29.1 | +11.18 | 48.6 | 0.3 | 43.5 | keep collecting (23/30) |
| money_moving | total | 40-35 | 53.3 | 50.0 | 3.3 | +1.41 | 1.9 | 0.19 | 36.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | moneyline | 2-6 | 25.0 | 32.4 | -7.4 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| pin_value | spread | 24-20 | 54.5 | 49.5 | 5.0 | +1.16 | 2.6 | 0.25 | 38.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 23-22 | 51.1 | 50.0 | 1.1 | -1.28 | -2.9 | -0.02 | 35.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.0 | -18.7 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 90-164 | 35.4 | 44.8 | -9.4 | -50.5 | -19.9 | 0.15 | 42.5 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 64-61 | 51.2 | 49.2 | 2.0 | -5.08 | -4.1 | 0.34 | 40.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap | total | 66-65 | 50.4 | 50.0 | 0.4 | -5.78 | -4.4 | 0.91 | 55.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | moneyline | 46-19 | 70.8 | 64.0 | 6.7 | -1.1 | -1.7 | 0.04 | 53.8 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+follow_move | moneyline | 11-22 | 33.3 | 53.5 | -20.2 | -14.69 | -44.5 | 0.2 | 54.5 | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 32.4 | -7.4 | -4.31 | -53.8 | -0.08 | 50.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| consensus_gap+rlm_quiet | moneyline | 1-5 | 16.7 | 26.6 | -9.9 | -3.68 | -61.3 | 1.07 | 83.3 | keep collecting (6/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.2 | -8.9 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 16-25 | 39.0 | 26.6 | 12.4 | +8.89 | 21.7 | -0.07 | 43.9 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 30-13 | 69.8 | 70.1 | -0.4 | -4.91 | -11.4 | -0.67 | 51.2 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 26.6 | -26.6 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 15-36 | 29.4 | 44.0 | -14.6 | -11.03 | -21.6 | 0.91 | 51.0 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | moneyline | 58-16 | 78.4 | 69.0 | 9.4 | -0.74 | -1.0 | -0.27 | 45.9 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 28-13 | 68.3 | 56.3 | 12.0 | +2.92 | 7.1 | 0.07 | 53.7 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 24-19 | 55.8 | 70.1 | -14.3 | -8.46 | -19.7 | 0.12 | 48.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+sharp_gap | moneyline | 36-18 | 66.7 | 50.0 | 16.7 | +8.81 | 16.3 | 0.23 | 53.7 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 22-26 | 45.8 | 47.1 | -1.2 | -7.54 | -15.7 | 0.02 | 52.1 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | moneyline | 8-21 | 27.6 | 46.0 | -18.4 | -12.26 | -42.3 | 0.24 | 48.3 | keep collecting (29/30) |
| follow_move+rlm_ratio | moneyline | 13-11 | 54.2 | 26.6 | 27.6 | +11.71 | 48.8 | 0.4 | 58.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 9-8 | 52.9 | 26.6 | 26.4 | +9.84 | 57.9 | -0.25 | 47.1 | keep collecting (17/30) |
| rlm_quiet+sharp_gap | moneyline | 9-11 | 45.0 | 26.6 | 18.4 | +6.84 | 34.2 | -0.41 | 45.0 | keep collecting (20/30) |
| rlm_ratio+sharp_gap | moneyline | 13-11 | 54.2 | 26.6 | 27.6 | +11.71 | 48.8 | 0.4 | 58.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 26.6 | -1.6 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 5-8 | 38.5 | 26.6 | 11.9 | +1.49 | 11.5 | 0.36 | 46.2 | keep collecting (13/30) |
| money_moving+rlm_ratio | moneyline | 4-4 | 50.0 | 26.6 | 23.4 | +3.22 | 40.2 | 0.16 | 50.0 | keep collecting (8/30) |
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
| money_level+rlm_ratio | moneyline | 4-3 | 57.1 | 26.6 | 30.6 | +1.87 | 26.7 | 2.0 | 85.7 | keep collecting (7/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 1-0 | 100.0 | 26.6 | 73.4 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 26.6 | 40.1 | +3.34 | 111.3 | -1.53 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 1-1 | 50.0 | 26.6 | 23.4 | +1.7 | 85.0 | -4.2 | 0.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 26.6 | 73.4 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 26.6 | -26.6 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-0 | 100.0 | 26.6 | 73.4 | +1.64 | 164.0 | 3.8 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 48.0 | -2.5 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 48.0 | 35.4 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 10-8 | 55.6 | 48.9 | 6.7 | +0.6 | 3.3 | 0.5 | 50.0 | keep collecting (18/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.2 | 8.8 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 49.0 | 13.5 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 10-5 | 66.7 | 48.8 | 17.9 | +4.12 | 27.5 | 0.93 | 66.7 | keep collecting (15/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 49.1 | -6.3 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 51.2 | 8.8 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 52.0 | -52.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 52.0 | -52.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-11 | 56.0 | 49.3 | 6.7 | +1.62 | 6.5 | 1.0 | 44.0 | keep collecting (25/30) |
| money_moving+sharp_gap | spread | 10-3 | 76.9 | 49.2 | 27.7 | +6.04 | 46.4 | 0.54 | 46.2 | keep collecting (13/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.3 | 17.3 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-11 | 45.0 | 48.6 | -3.6 | -3.2 | -16.0 | 0.85 | 45.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 48.0 | 14.5 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 11-9 | 55.0 | 48.8 | 6.2 | +1.04 | 5.2 | 0.7 | 45.0 | keep collecting (20/30) |
| follow_move+pin_value | spread | 12-7 | 63.2 | 49.0 | 14.1 | +3.45 | 18.2 | 0.26 | 31.6 | keep collecting (19/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 48.0 | 52.0 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 48.0 | 52.0 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 48.0 | 52.0 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-2 | 81.8 | 48.3 | 33.5 | +6.22 | 56.6 | 0.36 | 45.5 | keep collecting (11/30) |
| money_delta+rlm_quiet | spread | 1-0 | 100.0 | 48.0 | 52.0 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 2-0 | 100.0 | 48.0 | 52.0 | +1.74 | 87.1 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 52.0 | 14.6 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | spread | 1-3 | 25.0 | 49.0 | -24.0 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 48.0 | -48.0 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-2 | 33.3 | 48.0 | -14.6 | -1.09 | -36.4 | 0.33 | 33.3 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.0 | -52.0 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 12-10 | 54.5 | 50.2 | 4.3 | +0.95 | 4.3 | 0.77 | 50.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 24-22 | 52.2 | 49.9 | 2.3 | -0.08 | -0.2 | -0.04 | 37.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | total | 37-30 | 55.2 | 49.9 | 5.3 | +3.65 | 5.4 | -0.09 | 32.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | total | 28-19 | 59.6 | 50.1 | 9.5 | +6.5 | 13.8 | 0.26 | 36.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 8-5 | 61.5 | 50.1 | 11.4 | +2.23 | 17.2 | 0.23 | 30.8 | keep collecting (13/30) |
| money_moving+pin_value | total | 5-3 | 62.5 | 50.1 | 12.4 | +1.47 | 18.3 | 0.12 | 25.0 | keep collecting (8/30) |
| pin_value+sharp_gap | total | 11-6 | 64.7 | 50.1 | 14.6 | +3.92 | 23.1 | -0.06 | 29.4 | keep collecting (17/30) |
| follow_move+money_level | total | 22-19 | 53.7 | 49.8 | 3.8 | +0.94 | 2.3 | 0.15 | 39.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.9 | -3.3 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 14-5 | 73.7 | 50.3 | 23.4 | +7.9 | 41.6 | 0.58 | 52.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 30-14 | 68.2 | 50.0 | 18.1 | +13.33 | 30.3 | 0.41 | 43.2 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 5-3 | 62.5 | 50.3 | 12.2 | +1.63 | 20.4 | 1.0 | 62.5 | keep collecting (8/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 50.1 | 16.5 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 14-5 | 73.7 | 50.3 | 23.4 | +7.9 | 41.6 | 0.58 | 52.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 16-14 | 53.3 | 50.0 | 3.3 | +0.65 | 2.2 | 0.57 | 50.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | total | 4-3 | 57.1 | 49.8 | 7.3 | +0.53 | 7.5 | -0.43 | 14.3 | keep collecting (7/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 49.8 | 30.2 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 49.9 | -16.6 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 6-6 | 50.0 | 50.1 | -0.1 | -0.58 | -4.8 | -0.08 | 25.0 | keep collecting (12/30) |
| money_moving+rlm_ratio | total | 6-4 | 60.0 | 50.2 | 9.8 | +1.58 | 15.8 | 0.4 | 50.0 | keep collecting (10/30) |
| consensus_gap+follow_move | total | 12-8 | 60.0 | 50.0 | 10.0 | +2.88 | 14.4 | 1.45 | 65.0 | keep collecting (20/30) |
| consensus_gap+money_delta | total | 2-0 | 100.0 | 49.6 | 50.4 | +1.78 | 88.9 | 0.0 | 0.0 | keep collecting (2/30) |
| follow_move+money_delta | total | 2-2 | 50.0 | 50.2 | -0.2 | -0.22 | -5.5 | 1.25 | 50.0 | keep collecting (4/30) |
| money_delta+money_moving | total | 6-2 | 75.0 | 50.2 | 24.8 | +3.35 | 41.9 | 0.5 | 25.0 | keep collecting (8/30) |
| money_delta+pin_value | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 | -0.5 | 0.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 5-1 | 83.3 | 50.1 | 33.2 | +3.44 | 57.4 | 0.67 | 33.3 | keep collecting (6/30) |
| money_moving+rlm_quiet | total | 4-3 | 57.1 | 50.3 | 6.9 | +0.64 | 9.1 | 0.43 | 42.9 | keep collecting (7/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 7-2 | 77.8 | 50.3 | 27.5 | +4.41 | 49.0 | 0.44 | 55.6 | keep collecting (9/30) |
| rlm_quiet+sharp_gap | total | 9-2 | 81.8 | 50.3 | 31.5 | +6.22 | 56.6 | 0.64 | 54.5 | keep collecting (11/30) |
| follow_move+pin_move | total | 2-0 | 100.0 | 50.4 | 49.6 | +1.86 | 93.0 | 1.0 | 100.0 | keep collecting (2/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 2-1 | 66.7 | 50.1 | 16.5 | +0.82 | 27.3 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 50.4 | -0.4 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 3-1 | 75.0 | 50.4 | 24.6 | +1.77 | 44.2 | 0.25 | 50.0 | keep collecting (4/30) |
| money_level+pin_move | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_value | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 182-257 | 41.5 | 41.9 | -0.4 | -34.92 | -8.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move | both | 495-494 | 50.1 | 50.0 | 0.1 | -28.51 | -2.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | both | 316-423 | 42.8 | 44.0 | -1.2 | -58.17 | -7.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm | both | 140-157 | 47.1 | 42.2 | 4.9 | +31.28 | 10.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | both | 857-764 | 52.9 | 51.9 | 0.9 | -90.52 | -5.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | both | 200-225 | 47.1 | 44.6 | 2.5 | +1.15 | 0.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level | both | 1084-805 | 57.4 | 55.5 | 1.8 | -66.92 | -3.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 847-976 | 46.5 | 47.5 | -1.0 | -117.8 | -6.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | both | 847-977 | 46.4 | 47.8 | -1.3 | -127.36 | -7.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | both | 351-357 | 49.6 | 47.8 | 1.7 | +3.28 | 0.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 331-449 | 42.4 | 47.1 | -4.6 | -87.77 | -11.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+follow_move | both | 127-127 | 50.0 | 51.2 | -1.2 | -15.22 | -6.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | both | 148-242 | 37.9 | 44.3 | -6.3 | -31.97 | -8.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_move | both | 80-83 | 49.1 | 51.0 | -1.9 | +2.16 | 1.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | both | 23-39 | 37.1 | 37.1 | -0.1 | +10.03 | 16.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_value | both | 132-146 | 47.5 | 45.4 | 2.1 | +3.7 | 1.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | both | 25-43 | 36.8 | 39.6 | -2.9 | -1.66 | -2.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | both | 147-246 | 37.4 | 43.7 | -6.3 | -32.96 | -8.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_moving | both | 457-486 | 48.5 | 49.4 | -0.9 | -66.32 | -7.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_move | both | 355-351 | 50.3 | 50.3 | -0.0 | -29.59 | -4.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_rlm | both | 108-111 | 49.3 | 44.4 | 5.0 | +7.57 | 3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | both | 123-118 | 51.0 | 48.9 | 2.1 | -8.43 | -3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | both | 200-225 | 47.1 | 44.6 | 2.5 | +1.15 | 0.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 462-483 | 48.9 | 49.2 | -0.3 | -56.21 | -5.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_move | both | 298-325 | 47.8 | 48.7 | -0.9 | -22.93 | -3.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_rlm | both | 134-153 | 46.7 | 42.2 | 4.5 | +29.32 | 10.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_value | both | 155-183 | 45.9 | 47.1 | -1.3 | -13.9 | -4.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | both | 192-218 | 46.8 | 44.6 | 2.2 | +0.23 | 0.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+sharp_gap | both | 812-938 | 46.4 | 47.5 | -1.1 | -110.39 | -6.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_rlm | both | 129-130 | 49.8 | 44.3 | 5.5 | +25.5 | 9.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_value | both | 156-155 | 50.2 | 49.0 | 1.1 | -4.95 | -1.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_ratio | both | 116-109 | 51.6 | 45.7 | 5.8 | +16.25 | 7.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | both | 305-325 | 48.4 | 48.6 | -0.2 | -16.69 | -2.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+pin_value | both | 40-41 | 49.4 | 45.6 | 3.8 | +12.58 | 15.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_ratio | both | 108-111 | 49.3 | 44.4 | 5.0 | +7.57 | 3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | both | 140-157 | 47.1 | 42.2 | 4.9 | +31.28 | 10.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 38-31 | 55.1 | 48.6 | 6.4 | +3.73 | 5.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | both | 157-185 | 45.9 | 47.1 | -1.1 | -14.1 | -4.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio+sharp_gap | both | 200-225 | 47.1 | 44.6 | 2.5 | +1.15 | 0.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 151-176 | 46.2 | 46.0 | 0.2 | -22.47 | -6.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+money_moving | both | 597-532 | 52.9 | 52.4 | 0.5 | -46.48 | -4.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | both | 588-522 | 53.0 | 52.2 | 0.8 | -38.02 | -3.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | both | 565-401 | 58.5 | 56.6 | 1.9 | -44.51 | -4.6 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 95-81 | 54.0 | 48.5 | 5.5 | +10.68 | 6.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | both | 203-165 | 55.2 | 57.9 | -2.7 | -22.75 | -6.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | both | 293-268 | 52.2 | 53.1 | -0.9 | -27.8 | -5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | both | 172-158 | 52.1 | 49.8 | 2.3 | -8.55 | -2.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_quiet | both | 19-47 | 28.8 | 36.2 | -7.4 | -9.07 | -13.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_quiet | both | 182-257 | 41.5 | 41.9 | -0.4 | -34.92 | -8.0 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 98-149 | 39.7 | 41.9 | -2.2 | -20.73 | -8.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_moving | both | 226-331 | 40.6 | 42.4 | -1.8 | -49.17 | -8.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_delta | both | 41-110 | 27.2 | 36.6 | -9.4 | -31.68 | -21.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_level | both | 117-111 | 51.3 | 46.9 | 4.4 | +11.59 | 5.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | both | 68-71 | 48.9 | 46.9 | 2.1 | -5.57 | -4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+sharp_gap | both | 223-326 | 40.6 | 42.4 | -1.8 | -47.34 | -8.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
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
| money_level+pin_rlm | both | 63-43 | 59.4 | 46.7 | 12.7 | +19.25 | 18.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_rlm | both | 82-94 | 46.6 | 42.2 | 4.4 | +12.43 | 7.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+rlm_ratio | both | 110-116 | 48.7 | 45.0 | 3.6 | -0.1 | -0.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+rlm_quiet | both | 24-35 | 40.7 | 47.2 | -6.5 | -12.58 | -21.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 50.4 | 49.6 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 52-110 | 32.1 | 27.5 | 4.6 | -7.46 | -4.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet | spread | 45-45 | 50.0 | 50.6 | -0.6 | -3.33 | -3.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_quiet | total | 85-102 | 45.5 | 50.2 | -4.7 | -24.13 | -12.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move | moneyline | 103-101 | 50.5 | 49.5 | 0.9 | +6.99 | 3.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move | spread | 194-205 | 48.6 | 50.1 | -1.5 | -28.3 | -7.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move | total | 198-188 | 51.3 | 50.1 | 1.2 | -7.21 | -1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | moneyline | 49-166 | 22.8 | 28.1 | -5.3 | -44.92 | -20.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta | spread | 122-125 | 49.4 | 50.7 | -1.3 | -13.91 | -5.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | total | 145-132 | 52.3 | 50.2 | 2.2 | +0.66 | 0.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm | moneyline | 38-72 | 34.5 | 28.3 | 6.3 | +22.97 | 20.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm | spread | 25-22 | 53.2 | 50.8 | 2.4 | +0.79 | 1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm | total | 77-63 | 55.0 | 50.2 | 4.8 | +7.52 | 5.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | moneyline | 314-205 | 60.5 | 56.5 | 4.0 | -25.77 | -5.0 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 247-262 | 48.5 | 49.6 | -1.1 | -37.75 | -7.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | total | 296-297 | 49.9 | 50.0 | -0.1 | -27.0 | -4.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | moneyline | 37-80 | 31.6 | 29.8 | 1.8 | -2.78 | -2.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio | spread | 41-43 | 48.8 | 50.1 | -1.3 | -5.76 | -6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | total | 122-102 | 54.5 | 50.2 | 4.3 | +9.69 | 4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | moneyline | 417-157 | 72.6 | 69.1 | 3.6 | -22.7 | -4.0 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 316-326 | 49.2 | 49.3 | -0.1 | -41.01 | -6.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level | total | 351-322 | 52.2 | 49.9 | 2.2 | -3.21 | -0.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 201-327 | 38.1 | 41.6 | -3.5 | -55.15 | -10.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| sharp_gap | spread | 324-310 | 51.1 | 49.6 | 1.5 | -17.72 | -2.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 322-339 | 48.7 | 50.1 | -1.4 | -44.93 | -6.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | moneyline | 209-317 | 39.7 | 42.6 | -2.9 | -46.1 | -8.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | spread | 321-313 | 50.6 | 49.6 | 1.0 | -23.6 | -3.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | total | 317-347 | 47.7 | 50.1 | -2.3 | -57.67 | -8.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | moneyline | 18-54 | 25.0 | 30.5 | -5.5 | +10.87 | 15.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | spread | 158-147 | 51.8 | 49.6 | 2.2 | -9.11 | -3.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 175-156 | 52.9 | 49.9 | 2.9 | +1.52 | 0.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.0 | 48.0 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 140-273 | 33.9 | 44.8 | -10.9 | -78.34 | -19.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 86-75 | 53.4 | 49.3 | 4.1 | -1.7 | -1.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap | total | 105-101 | 51.0 | 49.8 | 1.2 | -7.73 | -3.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | moneyline | 145-83 | 63.6 | 63.1 | 0.5 | -6.7 | -2.9 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 136-81 | 62.7 | 62.6 | 0.0 | -6.32 | -2.9 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 187-303 | 38.2 | 41.5 | -3.3 | -42.39 | -8.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+follow_move | moneyline | 52-67 | 43.7 | 53.3 | -9.6 | -20.43 | -17.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 7-36 | 16.3 | 28.8 | -12.5 | -8.64 | -20.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 52-110 | 32.1 | 27.5 | 4.6 | -7.46 | -4.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 95-65 | 59.4 | 69.0 | -9.6 | -16.77 | -10.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 55-154 | 26.3 | 39.8 | -13.5 | -24.75 | -11.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | moneyline | 246-79 | 75.7 | 70.5 | 5.2 | -11.67 | -3.6 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 101-109 | 48.1 | 48.2 | -0.1 | -12.65 | -6.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_moving | moneyline | 46-149 | 23.6 | 27.8 | -4.2 | -30.89 | -15.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+sharp_gap | moneyline | 44-148 | 22.9 | 27.8 | -4.9 | -32.08 | -16.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 53-159 | 25.0 | 38.7 | -13.7 | -27.63 | -13.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+sharp_gap | moneyline | 98-108 | 47.6 | 47.3 | 0.3 | -12.08 | -5.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_quiet | moneyline | 23-67 | 25.6 | 27.6 | -2.1 | -5.91 | -6.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 24-68 | 26.1 | 27.6 | -1.5 | -7.45 | -8.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_move | moneyline | 28-35 | 44.4 | 53.3 | -8.9 | +4.93 | 7.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 10-28 | 26.3 | 29.1 | -2.7 | +9.65 | 25.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 4-30 | 11.8 | 29.3 | -17.6 | -7.04 | -20.7 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 83-67 | 55.3 | 51.6 | 3.8 | +6.35 | 4.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_rlm | moneyline | 24-39 | 38.1 | 29.6 | 8.5 | +2.46 | 3.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 37-80 | 31.6 | 29.8 | 1.8 | -2.78 | -2.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 46-62 | 42.6 | 42.6 | -0.0 | +10.69 | 9.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_rlm | moneyline | 37-70 | 34.6 | 28.3 | 6.2 | +23.57 | 22.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 36-76 | 32.1 | 29.9 | 2.2 | -0.18 | -0.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_rlm | moneyline | 27-45 | 37.5 | 28.5 | 9.0 | +17.19 | 23.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 23-32 | 41.8 | 28.3 | 13.5 | +9.87 | 17.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 21-30 | 41.2 | 30.3 | 10.9 | +8.28 | 16.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+sharp_gap | moneyline | 46-63 | 42.2 | 42.1 | 0.1 | +9.51 | 8.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 14-32 | 30.4 | 28.6 | 1.8 | -4.18 | -9.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 24-39 | 38.1 | 29.6 | 8.5 | +2.46 | 3.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 38-72 | 34.5 | 28.3 | 6.3 | +22.97 | 20.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 23-65 | 26.1 | 27.7 | -1.5 | -5.91 | -6.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 37-80 | 31.6 | 29.8 | 1.8 | -2.78 | -2.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 11-82 | 11.8 | 28.1 | -16.3 | -29.62 | -31.8 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 13-45 | 22.4 | 29.8 | -7.4 | +1.38 | 2.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_move | moneyline | 16-35 | 31.4 | 30.3 | 1.1 | +0.84 | 1.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_rlm | moneyline | 22-44 | 33.3 | 28.7 | 4.6 | +7.63 | 11.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_value | moneyline | 2-18 | 10.0 | 26.6 | -16.6 | -11.18 | -55.9 |  |  | keep collecting (20/30) |
| money_moving+pin_value | moneyline | 10-33 | 23.3 | 29.9 | -6.6 | +8.44 | 19.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_value | moneyline | 6-9 | 40.0 | 32.8 | 7.2 | +7.27 | 48.5 |  |  | keep collecting (15/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 26.6 | 4.7 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 10-35 | 22.2 | 29.7 | -7.5 | +6.44 | 14.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_delta | moneyline | 23-47 | 32.9 | 30.6 | 2.3 | -10.09 | -14.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_level | moneyline | 14-23 | 37.8 | 30.4 | 7.5 | +6.11 | 16.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+rlm_ratio | moneyline | 21-38 | 35.6 | 30.6 | 5.0 | -3.0 | -5.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_move | moneyline | 67-42 | 61.5 | 67.0 | -5.5 | -6.77 | -6.2 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 11-9 | 55.0 | 31.3 | 23.7 | +5.77 | 28.8 |  |  | keep collecting (20/30) |
| money_level+rlm_ratio | moneyline | 13-11 | 54.2 | 38.3 | 15.9 | +6.1 | 25.4 |  |  | keep collecting (24/30) |
| money_delta+rlm_quiet | moneyline | 15-35 | 30.0 | 29.4 | 0.6 | -9.95 | -19.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_value | moneyline | 5-2 | 71.4 | 66.7 | 4.7 | +0.68 | 9.7 |  |  | keep collecting (7/30) |
| follow_move+pin_value | moneyline | 2-7 | 22.2 | 31.8 | -9.6 | -4.79 | -53.3 |  |  | keep collecting (9/30) |
| pin_value+rlm_quiet | moneyline | 1-6 | 14.3 | 26.6 | -12.3 | -4.48 | -64.0 |  |  | keep collecting (7/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 26.6 | -1.6 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 34-27 | 55.7 | 48.7 | 7.0 | +1.9 | 3.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | spread | 48-42 | 53.3 | 49.1 | 4.2 | -1.14 | -1.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_move | spread | 25-27 | 48.1 | 49.2 | -1.1 | -5.73 | -11.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 60-44 | 57.7 | 49.2 | 8.5 | +6.95 | 6.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_ratio | spread | 4-4 | 50.0 | 50.0 | 0.0 | -0.67 | -8.3 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | spread | 47-42 | 52.8 | 49.2 | 3.6 | -2.03 | -2.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | spread | 157-160 | 49.5 | 49.3 | 0.2 | -18.11 | -5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_move | spread | 122-135 | 47.5 | 49.9 | -2.4 | -23.93 | -9.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_rlm | spread | 19-18 | 51.4 | 50.6 | 0.7 | -0.65 | -1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | spread | 56-50 | 52.8 | 49.1 | 3.8 | -1.23 | -1.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | spread | 41-43 | 48.8 | 50.1 | -1.3 | -5.76 | -6.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 158-159 | 49.8 | 49.4 | 0.5 | -15.97 | -5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_move | spread | 117-123 | 48.8 | 49.8 | -1.1 | -17.0 | -7.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | spread | 23-22 | 51.1 | 50.8 | 0.3 | -1.04 | -2.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | spread | 79-79 | 50.0 | 49.3 | 0.7 | -10.83 | -6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_ratio | spread | 39-42 | 48.1 | 50.1 | -1.9 | -6.69 | -8.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | spread | 316-305 | 50.9 | 49.6 | 1.3 | -20.1 | -3.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_rlm | spread | 25-22 | 53.2 | 50.8 | 2.4 | +0.79 | 1.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 73-79 | 48.0 | 49.7 | -1.7 | -14.7 | -9.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_ratio | spread | 22-24 | 47.8 | 50.4 | -2.6 | -3.94 | -8.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | spread | 120-123 | 49.4 | 49.8 | -0.4 | -14.27 | -5.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+pin_value | spread | 7-10 | 41.2 | 50.6 | -9.4 | -3.88 | -22.8 |  |  | keep collecting (17/30) |
| pin_rlm+rlm_ratio | spread | 19-18 | 51.4 | 50.6 | 0.7 | -0.65 | -1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | spread | 25-22 | 53.2 | 50.8 | 2.4 | +0.79 | 1.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 7-7 | 50.0 | 49.4 | 0.6 | -1.01 | -7.2 |  |  | keep collecting (14/30) |
| pin_value+sharp_gap | spread | 79-79 | 50.0 | 49.4 | 0.6 | -10.89 | -6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | spread | 41-43 | 48.8 | 50.1 | -1.3 | -5.76 | -6.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 152-164 | 48.1 | 49.1 | -1.0 | -26.69 | -8.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+rlm_ratio | spread | 21-28 | 42.9 | 49.9 | -7.0 | -9.13 | -18.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | spread | 249-243 | 50.6 | 49.4 | 1.3 | -18.72 | -3.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | spread | 57-46 | 55.3 | 48.9 | 6.4 | +2.72 | 2.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | spread | 248-244 | 50.4 | 49.3 | 1.1 | -20.64 | -4.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | spread | 107-124 | 46.3 | 49.6 | -3.3 | -27.49 | -11.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_value | spread | 86-86 | 50.0 | 49.1 | 0.9 | -11.81 | -6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_delta | spread | 14-14 | 50.0 | 50.4 | -0.4 | -2.09 | -7.5 |  |  | keep collecting (28/30) |
| follow_move+money_delta | spread | 38-47 | 44.7 | 50.2 | -5.5 | -12.62 | -14.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_level | spread | 40-40 | 50.0 | 50.1 | -0.1 | -3.96 | -4.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_moving | spread | 68-74 | 47.9 | 50.4 | -2.5 | -12.64 | -8.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | spread | 32-26 | 55.2 | 50.4 | 4.7 | +1.88 | 3.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+sharp_gap | spread | 67-72 | 48.2 | 50.4 | -2.2 | -11.62 | -8.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_quiet | spread | 45-45 | 50.0 | 50.6 | -0.6 | -3.33 | -3.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 14-4 | 77.8 | 50.7 | 27.1 | +8.78 | 48.8 |  |  | keep collecting (18/30) |
| rlm_quiet+sharp_gap | spread | 21-10 | 67.7 | 50.9 | 16.9 | +9.22 | 29.7 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+pin_rlm | spread | 14-10 | 58.3 | 50.3 | 8.0 | +2.58 | 10.7 |  |  | keep collecting (24/30) |
| money_delta+rlm_ratio | spread | 16-26 | 38.1 | 50.0 | -11.9 | -11.78 | -28.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 52.0 | 48.0 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_move | spread | 36-42 | 46.2 | 50.8 | -4.6 | -9.09 | -11.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_rlm | spread | 13-15 | 46.4 | 50.6 | -4.2 | -3.31 | -11.8 |  |  | keep collecting (28/30) |
| money_delta+rlm_quiet | spread | 14-17 | 45.2 | 51.0 | -5.8 | -4.07 | -13.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_quiet | spread | 20-10 | 66.7 | 50.8 | 15.8 | +8.27 | 27.6 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| pin_move+rlm_quiet | spread | 25-21 | 54.3 | 51.0 | 3.4 | +2.17 | 4.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-2 | 75.0 | 51.5 | 23.5 | +3.56 | 44.5 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_quiet | spread | 2-3 | 40.0 | 50.4 | -10.4 | -1.33 | -26.7 |  |  | keep collecting (5/30) |
| pin_value+rlm_quiet | spread | 4-4 | 50.0 | 49.0 | 1.0 | -0.52 | -6.5 |  |  | keep collecting (8/30) |
| follow_move+money_delta | total | 90-82 | 52.3 | 50.2 | 2.1 | +0.24 | 0.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | total | 204-205 | 49.9 | 50.0 | -0.1 | -19.14 | -4.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | total | 203-198 | 50.6 | 50.0 | 0.6 | -12.98 | -3.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | total | 309-330 | 48.4 | 50.1 | -1.7 | -47.91 | -7.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | total | 51-54 | 48.6 | 49.7 | -1.2 | -8.7 | -8.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_move | total | 27-21 | 56.2 | 49.8 | 6.4 | +2.96 | 6.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_value | total | 59-57 | 50.9 | 49.8 | 1.1 | -4.63 | -4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | total | 199-217 | 47.8 | 50.1 | -2.2 | -35.56 | -8.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+sharp_gap | total | 206-216 | 48.8 | 50.1 | -1.3 | -28.16 | -6.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | total | 119-102 | 53.8 | 50.0 | 3.8 | +6.46 | 2.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | total | 81-70 | 53.6 | 49.8 | 3.8 | +2.58 | 1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_value | total | 77-67 | 53.5 | 50.0 | 3.5 | +2.49 | 1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_quiet | total | 85-102 | 45.5 | 50.2 | -4.7 | -24.13 | -12.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 135-140 | 49.1 | 50.1 | -1.0 | -16.62 | -6.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_quiet+sharp_gap | total | 53-71 | 42.7 | 50.2 | -7.5 | -22.49 | -18.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_moving | total | 112-108 | 50.9 | 50.2 | 0.7 | -5.64 | -2.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | total | 167-158 | 51.4 | 49.9 | 1.4 | -6.16 | -1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 65-61 | 51.6 | 50.0 | 1.6 | -2.4 | -1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | total | 66-71 | 48.2 | 50.0 | -1.8 | -11.51 | -8.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | total | 68-71 | 48.9 | 50.0 | -1.1 | -9.65 | -6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | total | 45-46 | 49.5 | 49.8 | -0.4 | -6.08 | -6.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+sharp_gap | total | 47-45 | 51.1 | 49.8 | 1.2 | -3.3 | -3.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+follow_move | total | 41-33 | 55.4 | 49.8 | 5.6 | +3.3 | 4.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_delta | total | 16-14 | 53.3 | 50.0 | 3.4 | +0.03 | 0.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_quiet | total | 10-8 | 55.6 | 50.0 | 5.5 | +0.9 | 5.0 |  |  | keep collecting (18/30) |
| money_delta+rlm_quiet | total | 20-35 | 36.4 | 50.3 | -13.9 | -16.76 | -30.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+sharp_gap | total | 112-106 | 51.4 | 50.2 | 1.2 | -3.64 | -1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_quiet | total | 47-69 | 40.5 | 50.2 | -9.7 | -25.99 | -22.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 63-48 | 56.8 | 50.2 | 6.6 | +9.44 | 8.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_move | total | 66-58 | 53.2 | 50.2 | 3.0 | +2.32 | 1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | total | 139-139 | 50.0 | 50.1 | -0.1 | -11.93 | -4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_move | total | 150-149 | 50.2 | 50.1 | 0.1 | -12.02 | -4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+rlm_quiet | total | 19-25 | 43.2 | 50.2 | -7.0 | -7.58 | -17.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | total | 10-8 | 55.6 | 50.0 | 5.6 | +0.87 | 4.8 |  |  | keep collecting (18/30) |
| consensus_gap+rlm_ratio | total | 17-9 | 65.4 | 49.9 | 15.5 | +6.04 | 23.2 |  |  | keep collecting (26/30) |
| follow_move+pin_rlm | total | 65-54 | 54.6 | 50.2 | 4.4 | +5.75 | 4.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | total | 122-102 | 54.5 | 50.2 | 4.3 | +9.69 | 4.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 38-24 | 61.3 | 50.2 | 11.0 | +10.91 | 17.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+rlm_ratio | total | 61-42 | 59.2 | 50.2 | 9.1 | +13.72 | 13.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | total | 74-61 | 54.8 | 50.2 | 4.6 | +6.79 | 5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_ratio | total | 117-100 | 53.9 | 50.2 | 3.7 | +7.11 | 3.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_rlm | total | 77-63 | 55.0 | 50.2 | 4.8 | +7.52 | 5.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 73-55 | 57.0 | 50.2 | 6.8 | +11.92 | 9.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+pin_value | total | 28-20 | 58.3 | 50.2 | 8.2 | +5.4 | 11.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_ratio | total | 65-54 | 54.6 | 50.2 | 4.4 | +5.75 | 4.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | total | 77-63 | 55.0 | 50.2 | 4.8 | +7.52 | 5.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 30-21 | 58.8 | 50.2 | 8.7 | +6.22 | 12.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | total | 122-102 | 54.5 | 50.2 | 4.3 | +9.69 | 4.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 47-35 | 57.3 | 50.3 | 7.0 | +8.11 | 9.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+rlm_ratio | total | 73-52 | 58.4 | 50.2 | 8.2 | +14.68 | 11.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | total | 34-27 | 55.7 | 50.1 | 5.6 | +3.73 | 6.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_quiet | total | 39-52 | 42.9 | 50.2 | -7.3 | -16.27 | -17.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_quiet | total | 22-28 | 44.0 | 50.3 | -6.3 | -7.86 | -15.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_quiet+rlm_ratio | total | 42-53 | 44.2 | 50.3 | -6.1 | -14.5 | -15.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 50.4 | 49.6 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

# Pooled (fit + forward together)

Kept for continuity. **Contaminated** — it mixes the games the engine was built
on with the games testing it. Use the forward table for any decision.

## EARLY  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 34-41 | 45.3 | 36.0 | 9.3 | +10.19 | 13.6 | 0.02 | 41.3 | no edge shown yet |
| pin_move | both | 5-9 | 35.7 | 48.2 | -12.5 | -5.1 | -36.4 | 0.22 | 50.0 | keep collecting (14/30) |
| money_delta | both | 10-7 | 58.8 | 41.8 | 17.0 | +4.43 | 26.1 | -0.22 | 29.4 | keep collecting (17/30) |
| pin_rlm | both | 1-2 | 33.3 | 26.9 | 6.5 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | both | 487-423 | 53.5 | 52.2 | 1.3 | -51.35 | -5.6 | 0.17 | 41.3 | no edge shown yet |
| rlm_ratio | both | 32-21 | 60.4 | 39.2 | 21.2 | +19.26 | 36.3 | 0.33 | 49.1 | no edge shown yet |
| money_level | both | 179-117 | 60.5 | 59.1 | 1.4 | -13.79 | -4.7 | -0.05 | 40.2 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 150-127 | 54.2 | 48.4 | 5.8 | +17.99 | 6.5 | 0.29 | 43.0 | no edge shown yet |
| money_moving | both | 109-86 | 55.9 | 51.3 | 4.6 | +1.26 | 0.6 | 0.1 | 42.6 | no edge shown yet |
| pin_value | both | 49-49 | 50.0 | 48.4 | 1.6 | -5.43 | -5.5 | 0.1 | 37.8 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.2 | -31.2 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 229-293 | 43.9 | 47.5 | -3.7 | -58.16 | -11.1 | 0.4 | 45.4 | DROP: below break-even |
| consensus_gap+money_level | both | 36-29 | 55.4 | 64.2 | -8.9 | -9.63 | -14.8 | 0.4 | 50.8 | no edge shown yet |
| consensus_gap+money_moving | both | 19-23 | 45.2 | 48.1 | -2.8 | -5.58 | -13.3 | 0.25 | 42.9 | no edge shown yet |
| consensus_gap+pin_value | both | 19-28 | 40.4 | 46.6 | -6.2 | -11.54 | -24.5 | 0.39 | 48.9 | DROP: below break-even |
| follow_move+rlm_quiet | both | 34-41 | 45.3 | 36.0 | 9.3 | +10.19 | 13.6 | 0.02 | 41.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 32-21 | 60.4 | 39.2 | 21.2 | +19.26 | 36.3 | 0.33 | 49.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 79-42 | 65.3 | 49.7 | 15.6 | +23.95 | 19.8 | 0.32 | 46.3 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 68-43 | 61.3 | 58.2 | 3.0 | -1.49 | -1.3 | -0.05 | 47.7 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 11-9 | 55.0 | 49.6 | 5.4 | +0.81 | 4.0 | 0.4 | 45.0 | keep collecting (20/30) |
| money_moving+pin_value | both | 8-5 | 61.5 | 49.8 | 11.7 | +2.04 | 15.7 | 0.31 | 38.5 | keep collecting (13/30) |
| rlm_quiet+rlm_ratio | both | 19-13 | 59.4 | 36.9 | 22.4 | +13.97 | 43.7 | -0.27 | 43.8 | no edge shown yet |
| rlm_quiet+sharp_gap | both | 21-16 | 56.8 | 36.8 | 20.0 | +12.79 | 34.6 | -0.26 | 43.2 | no edge shown yet |
| rlm_ratio+sharp_gap | both | 32-21 | 60.4 | 39.2 | 21.2 | +19.26 | 36.3 | 0.33 | 49.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 100-62 | 61.7 | 55.8 | 6.0 | +4.43 | 2.7 | 0.19 | 43.8 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 64-50 | 56.1 | 49.1 | 7.0 | +6.18 | 5.4 | 0.25 | 45.6 | no edge shown yet |
| money_delta+money_level | both | 3-2 | 60.0 | 45.7 | 14.3 | +1.46 | 29.2 | 1.16 | 60.0 | keep collecting (5/30) |
| money_delta+money_moving | both | 9-7 | 56.2 | 41.3 | 15.0 | +3.53 | 22.0 | -0.23 | 31.2 | keep collecting (16/30) |
| money_delta+pin_value | both | 3-1 | 75.0 | 50.0 | 25.0 | +1.61 | 40.3 | 0.0 | 25.0 | keep collecting (4/30) |
| money_delta+sharp_gap | both | 7-5 | 58.3 | 40.5 | 17.8 | +3.78 | 31.5 | -0.31 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | both | 13-8 | 61.9 | 48.8 | 13.1 | +3.66 | 17.4 | -0.18 | 33.3 | keep collecting (21/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 50.2 | -50.2 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 34-42 | 44.7 | 51.7 | -7.0 | -15.0 | -19.7 | 0.66 | 53.9 | no edge shown yet |
| consensus_gap+rlm_quiet | both | 4-7 | 36.4 | 37.1 | -0.8 | -2.99 | -27.1 | 0.95 | 72.7 | keep collecting (11/30) |
| follow_move+pin_value | both | 20-17 | 54.1 | 48.9 | 5.2 | +0.41 | 1.1 | -0.12 | 29.7 | no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 42.3 | -25.6 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 27-45 | 37.5 | 45.9 | -8.4 | -9.56 | -13.3 | 0.9 | 50.0 | DROP: below break-even |
| follow_move+money_level | both | 93-47 | 66.4 | 59.9 | 6.5 | -0.74 | -0.5 | 0.01 | 42.9 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 11-8 | 57.9 | 41.9 | 16.0 | +3.43 | 18.0 | 1.42 | 63.2 | keep collecting (19/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 44.2 | 5.8 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 57-32 | 64.0 | 52.7 | 11.4 | +10.61 | 11.9 | 0.3 | 50.6 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 3-0 | 100.0 | 49.4 | 50.6 | +2.61 | 87.1 | 0.0 | 0.0 | keep collecting (3/30) |
| follow_move+money_delta | both | 5-3 | 62.5 | 41.0 | 21.5 | +3.95 | 49.4 | 0.05 | 37.5 | keep collecting (8/30) |
| money_delta+rlm_quiet | both | 2-2 | 50.0 | 37.9 | 12.1 | +1.53 | 38.3 | -2.1 | 0.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | both | 14-11 | 56.0 | 36.8 | 19.2 | +7.57 | 30.3 | 0.27 | 44.0 | keep collecting (25/30) |
| money_moving+rlm_ratio | both | 14-9 | 60.9 | 42.0 | 18.9 | +7.48 | 32.5 | 0.32 | 47.8 | keep collecting (23/30) |
| consensus_gap+rlm_ratio | both | 4-4 | 50.0 | 38.3 | 11.7 | +0.09 | 1.1 | 0.69 | 62.5 | keep collecting (8/30) |
| pin_move+pin_value | both | 1-4 | 20.0 | 49.2 | -29.2 | -3.09 | -61.8 | 0.2 | 20.0 | keep collecting (5/30) |
| follow_move+pin_move | both | 5-3 | 62.5 | 52.1 | 10.4 | +0.9 | 11.2 | 0.42 | 62.5 | keep collecting (8/30) |
| consensus_gap+pin_move | both | 0-5 | 0.0 | 44.5 | -44.5 | -5.0 | -100.0 | 0.26 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | both | 2-2 | 50.0 | 55.8 | -5.8 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 26.9 | -26.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 26.9 | 23.1 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 26.9 | -26.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 26.9 | -26.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 26.9 | 23.1 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | both | 1-2 | 33.3 | 26.9 | 6.5 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 50.9 | -50.9 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 49.8 | -49.8 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-1 | 66.7 | 50.1 | 16.6 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 26.9 | 73.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 26.9 | 73.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 26.9 | 73.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 2-1 | 66.7 | 34.5 | 32.2 | +3.34 | 111.3 | 0.87 | 66.7 | keep collecting (3/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 26.9 | -26.9 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 17-28 | 37.8 | 26.9 | 10.9 | +7.77 | 17.3 | -0.15 | 42.2 | DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 14-11 | 56.0 | 49.9 | 6.1 | +1.77 | 7.1 | 0.48 | 48.0 | keep collecting (25/30) |
| pin_move | moneyline | 2-3 | 40.0 | 45.4 | -5.4 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-4 | 20.0 | 49.6 | -29.6 | -3.09 | -61.8 | 0.4 | 40.0 | keep collecting (5/30) |
| pin_move | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.14 | -3.5 | 0.25 | 50.0 | keep collecting (4/30) |
| money_delta | moneyline | 2-4 | 33.3 | 26.9 | 6.5 | +0.34 | 5.7 | -1.45 | 33.3 | keep collecting (6/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 7-2 | 77.8 | 49.9 | 27.9 | +4.26 | 47.4 | 0.44 | 22.2 | keep collecting (9/30) |
| pin_rlm | moneyline | 1-2 | 33.3 | 26.9 | 6.5 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | moneyline | 201-131 | 60.5 | 56.3 | 4.3 | -21.32 | -6.4 | 0.14 | 45.2 | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 129-149 | 46.4 | 49.8 | -3.4 | -30.3 | -10.9 | 0.03 | 33.8 | DROP: below break-even |
| follow_move | total | 157-143 | 52.3 | 50.0 | 2.3 | +0.27 | 0.1 | 0.34 | 44.0 | no edge shown yet |
| rlm_ratio | moneyline | 13-12 | 52.0 | 26.9 | 25.1 | +10.71 | 42.8 | 0.38 | 56.0 | keep collecting (25/30) |
| rlm_ratio | spread | 3-3 | 50.0 | 51.4 | -1.4 | -0.16 | -2.7 | 0.33 | 16.7 | keep collecting (6/30) |
| rlm_ratio | total | 16-6 | 72.7 | 49.8 | 22.9 | +8.72 | 39.6 | 0.27 | 50.0 | keep collecting (22/30) |
| money_level | moneyline | 102-41 | 71.3 | 68.9 | 2.4 | -7.6 | -5.3 | -0.18 | 45.5 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-18 | 48.6 | 49.3 | -0.8 | -2.69 | -7.7 | 1.0 | 51.4 | no edge shown yet |
| money_level | total | 60-58 | 50.8 | 50.1 | 0.7 | -3.5 | -3.0 | -0.19 | 30.5 | no edge shown yet |
| sharp_gap | moneyline | 63-64 | 49.6 | 46.5 | 3.1 | +1.95 | 1.5 | 0.36 | 50.4 | no edge shown yet |
| sharp_gap | spread | 20-15 | 57.1 | 49.8 | 7.3 | +3.0 | 8.6 | 0.77 | 40.0 | no edge shown yet |
| sharp_gap | total | 67-48 | 58.3 | 50.0 | 8.3 | +13.04 | 11.3 | 0.06 | 35.7 | no edge shown yet |
| money_moving | moneyline | 48-42 | 53.3 | 53.1 | 0.2 | -10.05 | -11.2 | -0.09 | 47.8 | no edge shown yet |
| money_moving | spread | 18-6 | 75.0 | 49.3 | 25.7 | +10.18 | 42.4 | 0.5 | 45.8 | keep collecting (24/30) |
| money_moving | total | 43-38 | 53.1 | 50.0 | 3.1 | +1.14 | 1.4 | 0.2 | 35.8 | no edge shown yet |
| pin_value | moneyline | 2-6 | 25.0 | 32.7 | -7.7 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| pin_value | spread | 24-21 | 53.3 | 49.5 | 3.8 | +0.16 | 0.3 | 0.24 | 37.8 | no edge shown yet |
| pin_value | total | 23-22 | 51.1 | 50.0 | 1.1 | -1.28 | -2.9 | -0.02 | 35.6 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.1 | -18.7 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 93-166 | 35.9 | 45.4 | -9.5 | -51.52 | -19.9 | 0.15 | 42.9 | DROP: below break-even |
| consensus_gap | spread | 67-61 | 52.3 | 49.2 | 3.2 | -2.51 | -2.0 | 0.34 | 39.8 | no edge shown yet |
| consensus_gap | total | 69-66 | 51.1 | 50.0 | 1.1 | -4.13 | -3.1 | 0.91 | 55.6 | no edge shown yet |
| money_level+sharp_gap | moneyline | 48-19 | 71.6 | 64.2 | 7.5 | +0.26 | 0.4 | 0.12 | 55.2 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+follow_move | moneyline | 12-23 | 34.3 | 54.6 | -20.3 | -15.58 | -44.5 | 0.03 | 51.4 | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 32.7 | -7.7 | -4.31 | -53.8 | -0.08 | 50.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| consensus_gap+rlm_quiet | moneyline | 1-5 | 16.7 | 26.9 | -10.2 | -3.68 | -61.3 | 1.07 | 83.3 | keep collecting (6/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.3 | -9.0 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 17-28 | 37.8 | 26.9 | 10.9 | +7.77 | 17.3 | -0.15 | 42.2 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 33-13 | 71.7 | 70.1 | 1.6 | -3.44 | -7.5 | -0.55 | 52.2 | beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 26.9 | -26.9 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 16-36 | 30.8 | 44.7 | -13.9 | -10.3 | -19.8 | 0.94 | 51.9 | DROP: below break-even |
| follow_move+money_level | moneyline | 59-16 | 78.7 | 68.8 | 9.9 | -0.63 | -0.8 | -0.29 | 45.3 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 30-13 | 69.8 | 55.9 | 13.9 | +4.92 | 11.4 | 0.06 | 53.5 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 27-20 | 57.4 | 70.2 | -12.7 | -8.47 | -18.0 | 0.21 | 51.1 | no edge shown yet |
| follow_move+sharp_gap | moneyline | 36-19 | 65.5 | 49.6 | 15.9 | +7.81 | 14.2 | 0.22 | 52.7 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 24-26 | 48.0 | 48.1 | -0.1 | -6.18 | -12.4 | 0.13 | 54.0 | no edge shown yet |
| consensus_gap+money_moving | moneyline | 10-21 | 32.3 | 47.8 | -15.5 | -11.42 | -36.9 | 0.24 | 48.4 | INVERT candidate: wrong well beyond its base rate |
| follow_move+rlm_ratio | moneyline | 13-12 | 52.0 | 26.9 | 25.1 | +10.71 | 42.8 | 0.38 | 56.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 9-9 | 50.0 | 26.9 | 23.1 | +8.84 | 49.1 | -0.26 | 44.4 | keep collecting (18/30) |
| rlm_quiet+sharp_gap | moneyline | 9-12 | 42.9 | 26.9 | 16.0 | +5.84 | 27.8 | -0.4 | 42.9 | keep collecting (21/30) |
| rlm_ratio+sharp_gap | moneyline | 13-12 | 52.0 | 26.9 | 25.1 | +10.71 | 42.8 | 0.38 | 56.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 26.9 | -1.9 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 6-8 | 42.9 | 26.9 | 16.0 | +3.37 | 24.1 | 0.48 | 50.0 | keep collecting (14/30) |
| money_moving+rlm_ratio | moneyline | 4-4 | 50.0 | 26.9 | 23.1 | +3.22 | 40.2 | 0.16 | 50.0 | keep collecting (8/30) |
| money_delta+money_moving | moneyline | 2-4 | 33.3 | 26.9 | 6.5 | +0.34 | 5.7 | -1.45 | 33.3 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-3 | 40.0 | 26.9 | 13.1 | +1.34 | 26.8 | -1.74 | 40.0 | keep collecting (5/30) |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 42.3 | -42.3 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-1 | 66.7 | 57.7 | 9.0 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | moneyline | 2-1 | 66.7 | 57.7 | 9.0 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 26.9 | -26.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-1 | 50.0 | 26.9 | 23.1 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 26.9 | -26.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 26.9 | -26.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-1 | 50.0 | 26.9 | 23.1 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | moneyline | 1-2 | 33.3 | 26.9 | 6.5 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 26.9 | -26.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 26.9 | -26.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.13 | 56.5 | -0.1 | 50.0 | keep collecting (2/30) |
| money_level+rlm_ratio | moneyline | 4-3 | 57.1 | 26.9 | 30.3 | +1.87 | 26.7 | 2.0 | 85.7 | keep collecting (7/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 26.9 | 73.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 1-0 | 100.0 | 26.9 | 73.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 1-0 | 100.0 | 26.9 | 73.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 26.9 | 39.8 | +3.34 | 111.3 | -1.53 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 1-1 | 50.0 | 26.9 | 23.1 | +1.7 | 85.0 | -4.2 | 0.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 26.9 | 73.1 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 26.9 | -26.9 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-0 | 100.0 | 26.9 | 73.1 | +1.64 | 164.0 | 3.8 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 47.9 | -2.5 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 47.9 | 35.4 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 10-8 | 55.6 | 48.8 | 6.7 | +0.6 | 3.3 | 0.5 | 50.0 | keep collecting (18/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-3 | 50.0 | 51.4 | -1.4 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-7 | 58.8 | 49.1 | 9.7 | +2.09 | 12.3 | 0.88 | 41.2 | keep collecting (17/30) |
| money_level+money_moving | spread | 10-6 | 62.5 | 49.0 | 13.5 | +3.12 | 19.5 | 1.19 | 68.8 | keep collecting (16/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 49.1 | -6.2 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 3-3 | 50.0 | 51.4 | -1.4 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 52.1 | -52.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 52.1 | -52.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-12 | 53.8 | 49.4 | 4.5 | +0.62 | 2.4 | 1.15 | 46.2 | keep collecting (26/30) |
| money_moving+sharp_gap | spread | 10-4 | 71.4 | 49.4 | 22.0 | +5.04 | 36.0 | 0.86 | 50.0 | keep collecting (14/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.3 | 17.4 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-11 | 45.0 | 48.5 | -3.5 | -3.2 | -16.0 | 0.85 | 45.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 47.9 | 14.6 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 11-10 | 52.4 | 48.9 | 3.5 | +0.04 | 0.2 | 0.9 | 47.6 | keep collecting (21/30) |
| follow_move+pin_value | spread | 12-7 | 63.2 | 49.0 | 14.1 | +3.45 | 18.2 | 0.26 | 31.6 | keep collecting (19/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 47.9 | 52.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 47.9 | 52.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 47.9 | 52.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-3 | 75.0 | 48.6 | 26.4 | +5.22 | 43.5 | 0.75 | 50.0 | keep collecting (12/30) |
| money_delta+rlm_quiet | spread | 1-0 | 100.0 | 47.9 | 52.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 2-0 | 100.0 | 47.9 | 52.1 | +1.74 | 87.1 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 2-2 | 50.0 | 52.1 | -2.1 | -0.07 | -1.7 | 1.25 | 25.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | spread | 2-1 | 66.7 | 50.7 | 16.0 | +0.86 | 28.7 | 1.0 | 33.3 | keep collecting (3/30) |
| pin_move+pin_value | spread | 1-3 | 25.0 | 49.0 | -24.0 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 47.9 | -47.9 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-2 | 33.3 | 47.9 | -14.6 | -1.09 | -36.4 | 0.33 | 33.3 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.1 | -52.1 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 14-11 | 56.0 | 49.9 | 6.1 | +1.77 | 7.1 | 0.48 | 48.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 25-24 | 51.0 | 50.1 | 0.9 | -1.17 | -2.4 | 0.02 | 36.7 | no edge shown yet |
| money_level+sharp_gap | total | 38-31 | 55.1 | 50.0 | 5.0 | +3.55 | 5.2 | -0.1 | 31.9 | no edge shown yet |
| money_moving+sharp_gap | total | 30-20 | 60.0 | 50.0 | 10.0 | +7.32 | 14.6 | 0.2 | 36.0 | no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 50.2 | -50.2 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 8-5 | 61.5 | 49.9 | 11.6 | +2.23 | 17.2 | 0.23 | 30.8 | keep collecting (13/30) |
| money_moving+pin_value | total | 5-3 | 62.5 | 49.9 | 12.6 | +1.47 | 18.3 | 0.12 | 25.0 | keep collecting (8/30) |
| pin_value+sharp_gap | total | 11-6 | 64.7 | 50.0 | 14.7 | +3.92 | 23.1 | -0.06 | 29.4 | keep collecting (17/30) |
| follow_move+money_level | total | 23-21 | 52.3 | 50.1 | 2.2 | -0.15 | -0.3 | 0.11 | 36.4 | no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 50.0 | -3.4 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 16-6 | 72.7 | 49.8 | 22.9 | +8.72 | 39.6 | 0.27 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 33-16 | 67.3 | 50.0 | 17.4 | +14.05 | 28.7 | 0.24 | 40.8 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 5-3 | 62.5 | 49.8 | 12.7 | +1.63 | 20.4 | 1.0 | 62.5 | keep collecting (8/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 49.9 | 16.7 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 16-6 | 72.7 | 49.8 | 22.9 | +8.72 | 39.6 | 0.27 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 18-16 | 52.9 | 50.0 | 3.0 | +0.47 | 1.4 | 0.44 | 47.1 | no edge shown yet |
| consensus_gap+money_level | total | 4-3 | 57.1 | 50.1 | 7.1 | +0.53 | 7.5 | -0.43 | 14.3 | keep collecting (7/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 50.1 | 29.9 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 50.0 | -16.7 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 6-6 | 50.0 | 49.9 | 0.1 | -0.58 | -4.8 | -0.08 | 25.0 | keep collecting (12/30) |
| money_moving+rlm_ratio | total | 8-4 | 66.7 | 49.9 | 16.8 | +3.4 | 28.3 | 0.25 | 50.0 | keep collecting (12/30) |
| consensus_gap+follow_move | total | 13-8 | 61.9 | 50.0 | 11.9 | +3.79 | 18.0 | 1.52 | 66.7 | keep collecting (21/30) |
| consensus_gap+money_delta | total | 2-0 | 100.0 | 50.2 | 49.8 | +1.78 | 88.9 | 0.0 | 0.0 | keep collecting (2/30) |
| follow_move+money_delta | total | 2-2 | 50.0 | 49.9 | 0.1 | -0.22 | -5.5 | 1.25 | 50.0 | keep collecting (4/30) |
| money_delta+money_moving | total | 6-2 | 75.0 | 49.9 | 25.1 | +3.35 | 41.9 | 0.5 | 25.0 | keep collecting (8/30) |
| money_delta+pin_value | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 | -0.5 | 0.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 5-1 | 83.3 | 49.9 | 33.4 | +3.44 | 57.4 | 0.67 | 33.3 | keep collecting (6/30) |
| money_moving+rlm_quiet | total | 6-3 | 66.7 | 49.8 | 16.8 | +2.45 | 27.3 | 0.22 | 44.4 | keep collecting (9/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 9-3 | 75.0 | 49.8 | 25.2 | +5.22 | 43.5 | -0.08 | 50.0 | keep collecting (12/30) |
| rlm_quiet+sharp_gap | total | 11-3 | 78.6 | 49.8 | 28.7 | +7.04 | 50.3 | 0.14 | 50.0 | keep collecting (14/30) |
| follow_move+pin_move | total | 2-0 | 100.0 | 49.8 | 50.2 | +1.86 | 93.0 | 1.0 | 100.0 | keep collecting (2/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 49.8 | -49.8 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 49.8 | -49.8 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 2-1 | 66.7 | 49.9 | 16.7 | +0.82 | 27.3 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 49.8 | 0.2 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 3-1 | 75.0 | 49.8 | 25.2 | +1.77 | 44.2 | 0.25 | 50.0 | keep collecting (4/30) |
| money_level+pin_move | total | 0-1 | 0.0 | 50.2 | -50.2 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_value | total | 0-1 | 0.0 | 50.2 | -50.2 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 50.2 | -50.2 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 49.8 | -49.8 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 0-1 | 0.0 | 49.8 | -49.8 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 195-282 | 40.9 | 41.9 | -1.0 | -36.23 | -7.6 |  |  | DROP: below break-even |
| pin_move | both | 518-517 | 50.0 | 50.0 | 0.1 | -31.46 | -3.0 |  |  | DROP: below break-even |
| money_delta | both | 330-438 | 43.0 | 44.0 | -1.0 | -59.68 | -7.8 |  |  | DROP: below break-even |
| pin_rlm | both | 143-162 | 46.9 | 42.2 | 4.7 | +29.58 | 9.7 |  |  | DROP: below break-even |
| follow_move | both | 897-810 | 52.5 | 51.8 | 0.8 | -92.58 | -5.4 |  |  | no edge shown yet |
| rlm_ratio | both | 207-239 | 46.4 | 44.2 | 2.3 | -5.92 | -1.3 |  |  | DROP: below break-even |
| money_level | both | 1136-845 | 57.3 | 55.6 | 1.8 | -71.26 | -3.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 877-1024 | 46.1 | 47.5 | -1.3 | -139.93 | -7.4 |  |  | DROP: below break-even |
| money_moving | both | 880-1025 | 46.2 | 47.8 | -1.6 | -148.35 | -7.8 |  |  | DROP: below break-even |
| pin_value | both | 373-371 | 50.1 | 48.0 | 2.2 | +20.46 | 2.8 |  |  | no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 356-467 | 43.3 | 47.6 | -4.3 | -87.73 | -10.7 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 136-135 | 50.2 | 51.4 | -1.2 | -16.71 | -6.2 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 155-256 | 37.7 | 44.9 | -7.1 | -41.06 | -10.0 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 85-86 | 49.7 | 51.1 | -1.4 | +3.23 | 1.9 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 24-41 | 36.9 | 37.9 | -1.0 | +9.03 | 13.9 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 143-152 | 48.5 | 45.9 | 2.6 | +7.31 | 2.5 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | both | 27-46 | 37.0 | 39.2 | -2.3 | -2.75 | -3.8 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 153-260 | 37.0 | 44.2 | -7.1 | -42.18 | -10.2 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 471-508 | 48.1 | 49.3 | -1.2 | -77.34 | -7.9 |  |  | DROP: below break-even |
| follow_move+pin_move | both | 371-370 | 50.1 | 50.3 | -0.2 | -34.74 | -4.7 |  |  | no edge shown yet |
| follow_move+pin_rlm | both | 111-114 | 49.3 | 44.1 | 5.3 | +7.86 | 3.5 |  |  | no edge shown yet |
| follow_move+pin_value | both | 129-122 | 51.4 | 48.9 | 2.5 | +2.6 | 1.0 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 207-239 | 46.4 | 44.2 | 2.3 | -5.92 | -1.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 477-506 | 48.5 | 49.1 | -0.5 | -67.32 | -6.8 |  |  | DROP: below break-even |
| money_moving+pin_move | both | 306-335 | 47.7 | 48.7 | -1.0 | -26.07 | -4.1 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 137-157 | 46.6 | 42.2 | 4.4 | +28.61 | 9.7 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 160-194 | 45.2 | 47.3 | -2.1 | -20.47 | -5.8 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 199-230 | 46.4 | 44.3 | 2.1 | -4.83 | -1.1 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 841-984 | 46.1 | 47.5 | -1.4 | -131.42 | -7.2 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 131-134 | 49.4 | 44.1 | 5.3 | +23.45 | 8.8 |  |  | no edge shown yet |
| pin_move+pin_value | both | 163-160 | 50.5 | 49.1 | 1.4 | -3.89 | -1.2 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 118-112 | 51.3 | 45.5 | 5.8 | +15.2 | 6.6 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 311-336 | 48.1 | 48.6 | -0.5 | -22.61 | -3.5 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 40-42 | 48.8 | 45.6 | 3.2 | +11.58 | 14.1 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 111-114 | 49.3 | 44.1 | 5.3 | +7.86 | 3.5 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 143-162 | 46.9 | 42.2 | 4.7 | +29.58 | 9.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 40-31 | 56.3 | 48.5 | 7.8 | +5.51 | 7.8 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 161-195 | 45.2 | 47.2 | -2.0 | -20.58 | -5.8 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 207-239 | 46.4 | 44.2 | 2.3 | -5.92 | -1.3 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 159-187 | 46.0 | 45.9 | 0.0 | -25.97 | -7.5 |  |  | DROP: below break-even |
| money_level+money_moving | both | 622-559 | 52.7 | 52.4 | 0.3 | -54.69 | -4.6 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 610-548 | 52.7 | 52.2 | 0.5 | -46.37 | -4.0 |  |  | no edge shown yet |
| follow_move+money_level | both | 584-416 | 58.4 | 56.6 | 1.8 | -46.84 | -4.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 98-83 | 54.1 | 48.3 | 5.9 | +11.5 | 6.4 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 219-176 | 55.4 | 58.2 | -2.7 | -23.67 | -6.0 |  |  | no edge shown yet |
| money_level+pin_move | both | 304-277 | 52.3 | 53.1 | -0.8 | -28.17 | -4.8 |  |  | no edge shown yet |
| money_level+pin_value | both | 180-166 | 52.0 | 49.9 | 2.1 | -9.47 | -2.7 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 22-51 | 30.1 | 36.4 | -6.3 | -10.25 | -14.0 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | both | 195-282 | 40.9 | 41.9 | -1.0 | -36.23 | -7.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 100-161 | 38.3 | 41.4 | -3.1 | -30.82 | -11.8 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 236-340 | 41.0 | 42.4 | -1.4 | -48.47 | -8.4 |  |  | DROP: below break-even |
| consensus_gap+money_delta | both | 43-111 | 27.9 | 36.7 | -8.8 | -30.77 | -20.0 |  |  | DROP: below break-even |
| money_delta+money_level | both | 121-112 | 51.9 | 46.9 | 5.0 | +14.31 | 6.1 |  |  | no edge shown yet |
| money_delta+pin_value | both | 70-72 | 49.3 | 46.9 | 2.4 | -4.79 | -3.4 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 233-334 | 41.1 | 42.4 | -1.3 | -45.64 | -8.0 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 81-133 | 37.9 | 39.9 | -2.1 | -20.73 | -9.7 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | both | 92-156 | 37.1 | 41.4 | -4.3 | -31.72 | -12.8 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 53-96 | 35.6 | 42.9 | -7.3 | -35.98 | -24.1 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | both | 93-115 | 44.7 | 44.1 | 0.6 | -8.09 | -3.9 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 43-64 | 40.2 | 40.5 | -0.3 | -9.48 | -8.9 |  |  | DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 122-139 | 46.7 | 46.3 | 0.5 | -6.08 | -2.3 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 64-45 | 58.7 | 46.8 | 11.9 | +18.2 | 16.7 |  |  | no edge shown yet |
| money_delta+pin_rlm | both | 84-95 | 46.9 | 42.1 | 4.8 | +13.39 | 7.5 |  |  | no edge shown yet |
| money_delta+rlm_ratio | both | 116-122 | 48.7 | 44.9 | 3.9 | -0.51 | -0.2 |  |  | no edge shown yet |
| pin_value+rlm_quiet | both | 27-36 | 42.9 | 46.9 | -4.0 | -1.16 | -1.8 |  |  | DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 49.8 | 50.2 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 57-119 | 32.4 | 27.7 | 4.7 | -0.22 | -0.1 |  |  | DROP: below break-even |
| rlm_quiet | spread | 48-49 | 49.5 | 50.7 | -1.2 | -4.51 | -4.6 |  |  | no edge shown yet |
| rlm_quiet | total | 90-114 | 44.1 | 49.9 | -5.8 | -31.5 | -15.4 |  |  | DROP: below break-even |
| pin_move | moneyline | 109-103 | 51.4 | 49.6 | 1.9 | +9.7 | 4.6 |  |  | no edge shown yet |
| pin_move | spread | 204-213 | 48.9 | 50.2 | -1.2 | -27.4 | -6.6 |  |  | no edge shown yet |
| pin_move | total | 205-201 | 50.5 | 50.0 | 0.5 | -13.76 | -3.4 |  |  | no edge shown yet |
| money_delta | moneyline | 51-170 | 23.1 | 28.3 | -5.3 | -46.54 | -21.1 |  |  | DROP: below break-even |
| money_delta | spread | 125-128 | 49.4 | 50.7 | -1.3 | -14.11 | -5.6 |  |  | no edge shown yet |
| money_delta | total | 154-140 | 52.4 | 49.9 | 2.5 | +0.98 | 0.3 |  |  | no edge shown yet |
| pin_rlm | moneyline | 40-74 | 35.1 | 28.9 | 6.2 | +23.31 | 20.4 |  |  | DROP: below break-even |
| pin_rlm | spread | 25-22 | 53.2 | 50.8 | 2.3 | +0.79 | 1.7 |  |  | no edge shown yet |
| pin_rlm | total | 78-66 | 54.2 | 49.9 | 4.3 | +5.47 | 3.8 |  |  | no edge shown yet |
| follow_move | moneyline | 331-218 | 60.3 | 55.9 | 4.4 | -15.93 | -2.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 256-276 | 48.1 | 49.6 | -1.5 | -43.5 | -8.2 |  |  | DROP: below break-even |
| follow_move | total | 310-316 | 49.5 | 50.0 | -0.5 | -33.14 | -5.3 |  |  | no edge shown yet |
| rlm_ratio | moneyline | 39-89 | 30.5 | 29.8 | 0.7 | -9.44 | -7.4 |  |  | DROP: below break-even |
| rlm_ratio | spread | 41-44 | 48.2 | 50.1 | -1.9 | -6.76 | -8.0 |  |  | no edge shown yet |
| rlm_ratio | total | 127-106 | 54.5 | 49.9 | 4.6 | +10.28 | 4.4 |  |  | no edge shown yet |
| money_level | moneyline | 437-168 | 72.2 | 69.0 | 3.2 | -27.05 | -4.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 328-339 | 49.2 | 49.3 | -0.1 | -43.17 | -6.5 |  |  | DROP: below break-even |
| money_level | total | 371-338 | 52.3 | 50.0 | 2.3 | -1.04 | -0.1 |  |  | no edge shown yet |
| sharp_gap | moneyline | 209-344 | 37.8 | 41.8 | -4.0 | -66.2 | -12.0 |  |  | DROP: below break-even |
| sharp_gap | spread | 333-326 | 50.5 | 49.6 | 0.9 | -25.73 | -3.9 |  |  | no edge shown yet |
| sharp_gap | total | 335-354 | 48.6 | 50.0 | -1.3 | -48.0 | -7.0 |  |  | DROP: below break-even |
| money_moving | moneyline | 219-332 | 39.7 | 42.9 | -3.2 | -54.88 | -10.0 |  |  | DROP: below break-even |
| money_moving | spread | 330-329 | 50.1 | 49.6 | 0.5 | -31.6 | -4.8 |  |  | no edge shown yet |
| money_moving | total | 331-364 | 47.6 | 50.0 | -2.3 | -61.86 | -8.9 |  |  | DROP: below break-even |
| pin_value | moneyline | 21-54 | 28.0 | 31.2 | -3.2 | +25.46 | 33.9 |  |  | DROP: below break-even |
| pin_value | spread | 169-151 | 52.8 | 49.6 | 3.2 | -3.66 | -1.1 |  |  | no edge shown yet |
| pin_value | total | 183-166 | 52.4 | 50.0 | 2.4 | -1.33 | -0.4 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.1 | 47.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 151-283 | 34.8 | 45.6 | -10.8 | -82.61 | -19.0 |  |  | DROP: below break-even |
| consensus_gap | spread | 92-77 | 54.4 | 49.2 | 5.2 | +1.43 | 0.8 |  |  | no edge shown yet |
| consensus_gap | total | 113-107 | 51.4 | 50.1 | 1.3 | -6.55 | -3.0 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 152-88 | 63.3 | 63.3 | 0.0 | -9.2 | -3.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 141-86 | 62.1 | 62.7 | -0.6 | -9.09 | -4.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 195-318 | 38.0 | 41.8 | -3.7 | -51.44 | -10.0 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 58-71 | 45.0 | 53.4 | -8.4 | -20.64 | -16.0 |  |  | DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 8-39 | 17.0 | 28.8 | -11.8 | -10.64 | -22.6 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 57-119 | 32.4 | 27.7 | 4.7 | -0.22 | -0.1 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 104-70 | 59.8 | 69.1 | -9.4 | -17.93 | -10.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 59-161 | 26.8 | 40.7 | -13.9 | -29.56 | -13.4 |  |  | DROP: below break-even |
| follow_move+money_level | moneyline | 256-83 | 75.5 | 70.3 | 5.3 | -11.32 | -3.3 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 108-116 | 48.2 | 47.9 | 0.3 | -15.09 | -6.7 |  |  | no edge shown yet |
| money_delta+money_moving | moneyline | 48-153 | 23.9 | 28.0 | -4.1 | -32.51 | -16.2 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 46-152 | 23.2 | 28.0 | -4.8 | -33.7 | -17.0 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 56-167 | 25.1 | 39.5 | -14.4 | -33.58 | -15.1 |  |  | DROP: below break-even |
| follow_move+sharp_gap | moneyline | 105-117 | 47.3 | 46.9 | 0.4 | -16.51 | -7.4 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | moneyline | 24-73 | 24.7 | 27.8 | -3.1 | -10.91 | -11.3 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 25-76 | 24.8 | 27.8 | -3.0 | -14.45 | -14.3 |  |  | DROP: below break-even |
| consensus_gap+pin_move | moneyline | 31-35 | 47.0 | 53.5 | -6.5 | +7.25 | 11.0 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 11-29 | 27.5 | 30.3 | -2.8 | +9.65 | 24.1 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 5-33 | 13.2 | 29.3 | -16.1 | -9.04 | -23.8 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 89-69 | 56.3 | 51.5 | 4.9 | +9.06 | 5.7 |  |  | no edge shown yet |
| follow_move+pin_rlm | moneyline | 26-40 | 39.4 | 29.7 | 9.7 | +3.8 | 5.8 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 39-89 | 30.5 | 29.8 | 0.7 | -9.44 | -7.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 49-62 | 44.1 | 43.1 | 1.0 | +13.07 | 11.8 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 39-71 | 35.5 | 29.0 | 6.5 | +24.91 | 22.6 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 38-83 | 31.4 | 29.9 | 1.5 | -4.84 | -4.0 |  |  | DROP: below break-even |
| pin_move+pin_rlm | moneyline | 28-46 | 37.8 | 28.7 | 9.1 | +17.19 | 23.2 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 25-34 | 42.4 | 28.4 | 13.9 | +10.29 | 17.4 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 22-31 | 41.5 | 30.4 | 11.1 | +8.28 | 15.6 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 49-64 | 43.4 | 42.4 | 0.9 | +10.89 | 9.6 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 15-33 | 31.2 | 28.8 | 2.4 | -4.18 | -8.7 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 26-40 | 39.4 | 29.7 | 9.7 | +3.8 | 5.8 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 40-74 | 35.1 | 28.9 | 6.2 | +23.31 | 20.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 24-73 | 24.7 | 27.8 | -3.1 | -12.91 | -13.3 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 39-89 | 30.5 | 29.8 | 0.7 | -9.44 | -7.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 12-83 | 12.6 | 28.3 | -15.7 | -29.62 | -31.2 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 14-45 | 23.7 | 30.8 | -7.1 | +2.27 | 3.8 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 17-35 | 32.7 | 30.4 | 2.3 | +1.84 | 3.5 |  |  | DROP: below break-even |
| money_delta+pin_rlm | moneyline | 23-44 | 34.3 | 28.9 | 5.4 | +8.63 | 12.9 |  |  | DROP: below break-even |
| money_delta+pin_value | moneyline | 2-18 | 10.0 | 26.9 | -16.9 | -11.18 | -55.9 |  |  | keep collecting (20/30) |
| money_moving+pin_value | moneyline | 10-33 | 23.3 | 30.1 | -6.8 | +8.44 | 19.6 |  |  | DROP: below break-even |
| pin_move+pin_value | moneyline | 6-9 | 40.0 | 33.0 | 7.0 | +7.27 | 48.5 |  |  | keep collecting (15/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 26.9 | 4.4 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 10-35 | 22.2 | 30.0 | -7.7 | +6.44 | 14.3 |  |  | DROP: below break-even |
| follow_move+money_delta | moneyline | 24-49 | 32.9 | 30.7 | 2.2 | -11.09 | -15.2 |  |  | DROP: below break-even |
| money_delta+money_level | moneyline | 14-23 | 37.8 | 30.6 | 7.2 | +6.11 | 16.5 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | moneyline | 22-40 | 35.5 | 30.6 | 4.9 | -4.0 | -6.4 |  |  | DROP: below break-even |
| money_level+pin_move | moneyline | 71-42 | 62.8 | 67.0 | -4.2 | -4.48 | -4.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 11-10 | 52.4 | 33.5 | 18.9 | +4.77 | 22.7 |  |  | keep collecting (21/30) |
| money_level+rlm_ratio | moneyline | 13-12 | 52.0 | 38.0 | 14.0 | +5.1 | 20.4 |  |  | keep collecting (25/30) |
| money_delta+rlm_quiet | moneyline | 16-37 | 30.2 | 29.5 | 0.7 | -10.95 | -20.7 |  |  | DROP: below break-even |
| money_level+pin_value | moneyline | 5-2 | 71.4 | 66.5 | 4.9 | +0.68 | 9.7 |  |  | keep collecting (7/30) |
| follow_move+pin_value | moneyline | 3-7 | 30.0 | 31.5 | -1.5 | +5.8 | 58.0 |  |  | keep collecting (10/30) |
| pin_value+rlm_quiet | moneyline | 2-6 | 25.0 | 26.9 | -1.9 | +6.12 | 76.5 |  |  | keep collecting (8/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 26.9 | -1.9 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 35-27 | 56.5 | 48.7 | 7.7 | +2.81 | 4.5 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 48-44 | 52.2 | 49.0 | 3.1 | -3.14 | -3.4 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 27-28 | 49.1 | 49.2 | -0.1 | -4.99 | -9.1 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 66-46 | 58.9 | 49.2 | 9.7 | +10.08 | 9.0 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 4-4 | 50.0 | 50.0 | 0.0 | -0.67 | -8.3 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | spread | 47-44 | 51.6 | 49.2 | 2.4 | -4.03 | -4.4 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 157-165 | 48.8 | 49.3 | -0.6 | -23.11 | -7.2 |  |  | no edge shown yet |
| follow_move+pin_move | spread | 127-142 | 47.2 | 49.9 | -2.7 | -26.46 | -9.8 |  |  | DROP: below break-even |
| follow_move+pin_rlm | spread | 19-18 | 51.4 | 50.6 | 0.7 | -0.65 | -1.7 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 59-50 | 54.1 | 49.1 | 5.0 | +1.42 | 1.3 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 41-44 | 48.2 | 50.1 | -1.9 | -6.76 | -8.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 158-164 | 49.1 | 49.4 | -0.3 | -20.97 | -6.5 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 118-127 | 48.2 | 49.8 | -1.6 | -20.16 | -8.2 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 23-22 | 51.1 | 50.8 | 0.3 | -1.04 | -2.3 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 80-83 | 49.1 | 49.3 | -0.2 | -14.0 | -8.6 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 39-43 | 47.6 | 50.1 | -2.5 | -7.69 | -9.4 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 325-321 | 50.3 | 49.6 | 0.7 | -28.1 | -4.4 |  |  | no edge shown yet |
| pin_move+pin_rlm | spread | 25-22 | 53.2 | 50.8 | 2.3 | +0.79 | 1.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 79-80 | 49.7 | 49.7 | -0.0 | -10.55 | -6.6 |  |  | no edge shown yet |
| pin_move+rlm_ratio | spread | 22-24 | 47.8 | 50.5 | -2.6 | -3.94 | -8.6 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 121-127 | 48.8 | 49.8 | -1.0 | -17.43 | -7.0 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 7-10 | 41.2 | 50.6 | -9.4 | -3.88 | -22.8 |  |  | keep collecting (17/30) |
| pin_rlm+rlm_ratio | spread | 19-18 | 51.4 | 50.6 | 0.7 | -0.65 | -1.7 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 25-22 | 53.2 | 50.8 | 2.3 | +0.79 | 1.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 7-7 | 50.0 | 49.4 | 0.6 | -1.01 | -7.2 |  |  | keep collecting (14/30) |
| pin_value+sharp_gap | spread | 80-83 | 49.1 | 49.4 | -0.3 | -14.06 | -8.6 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 41-44 | 48.2 | 50.1 | -1.9 | -6.76 | -8.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 154-168 | 47.8 | 49.1 | -1.3 | -28.82 | -8.9 |  |  | DROP: below break-even |
| money_level+rlm_ratio | spread | 21-28 | 42.9 | 49.9 | -7.0 | -9.13 | -18.6 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 256-254 | 50.2 | 49.3 | 0.9 | -23.55 | -4.6 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 58-48 | 54.7 | 48.9 | 5.8 | +1.6 | 1.5 |  |  | no edge shown yet |
| money_level+money_moving | spread | 255-255 | 50.0 | 49.3 | 0.7 | -25.46 | -5.0 |  |  | no edge shown yet |
| money_level+pin_move | spread | 110-128 | 46.2 | 49.6 | -3.4 | -28.78 | -12.1 |  |  | DROP: below break-even |
| money_level+pin_value | spread | 89-88 | 50.3 | 49.1 | 1.1 | -11.19 | -6.3 |  |  | no edge shown yet |
| consensus_gap+money_delta | spread | 14-14 | 50.0 | 50.4 | -0.4 | -2.09 | -7.5 |  |  | keep collecting (28/30) |
| follow_move+money_delta | spread | 38-49 | 43.7 | 50.2 | -6.5 | -14.62 | -16.8 |  |  | DROP: below break-even |
| money_delta+money_level | spread | 41-40 | 50.6 | 50.0 | 0.6 | -3.05 | -3.8 |  |  | no edge shown yet |
| money_delta+money_moving | spread | 70-75 | 48.3 | 50.4 | -2.1 | -11.82 | -8.2 |  |  | no edge shown yet |
| money_delta+pin_value | spread | 32-26 | 55.2 | 50.4 | 4.7 | +1.88 | 3.2 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 69-73 | 48.6 | 50.4 | -1.8 | -10.8 | -7.6 |  |  | no edge shown yet |
| follow_move+rlm_quiet | spread | 48-49 | 49.5 | 50.7 | -1.2 | -4.51 | -4.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 14-4 | 77.8 | 50.7 | 27.1 | +8.78 | 48.8 |  |  | keep collecting (18/30) |
| rlm_quiet+sharp_gap | spread | 21-10 | 67.7 | 50.9 | 16.9 | +9.22 | 29.7 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+pin_rlm | spread | 14-10 | 58.3 | 50.3 | 8.0 | +2.58 | 10.7 |  |  | keep collecting (24/30) |
| money_delta+rlm_ratio | spread | 16-27 | 37.2 | 50.0 | -12.7 | -12.78 | -29.7 |  |  | DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 52.1 | 47.9 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_move | spread | 36-42 | 46.2 | 50.8 | -4.6 | -9.09 | -11.7 |  |  | no edge shown yet |
| money_delta+pin_rlm | spread | 13-15 | 46.4 | 50.6 | -4.2 | -3.31 | -11.8 |  |  | keep collecting (28/30) |
| money_delta+rlm_quiet | spread | 14-18 | 43.8 | 51.0 | -7.3 | -5.07 | -15.8 |  |  | no edge shown yet |
| money_moving+rlm_quiet | spread | 20-10 | 66.7 | 50.8 | 15.8 | +8.27 | 27.6 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_move+rlm_quiet | spread | 26-23 | 53.1 | 51.1 | 2.0 | +1.08 | 2.2 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-2 | 75.0 | 51.6 | 23.4 | +3.56 | 44.5 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_quiet | spread | 3-3 | 50.0 | 50.7 | -0.7 | -0.42 | -7.1 |  |  | keep collecting (6/30) |
| pin_value+rlm_quiet | spread | 5-4 | 55.6 | 49.3 | 6.2 | +0.39 | 4.4 |  |  | keep collecting (9/30) |
| follow_move+money_delta | total | 97-89 | 52.2 | 49.9 | 2.3 | -0.26 | -0.1 |  |  | no edge shown yet |
| money_level+money_moving | total | 215-216 | 49.9 | 50.0 | -0.1 | -20.02 | -4.6 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 213-208 | 50.6 | 50.0 | 0.6 | -13.73 | -3.3 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 321-345 | 48.2 | 50.0 | -1.8 | -51.88 | -7.8 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 57-58 | 49.6 | 50.2 | -0.6 | -7.33 | -6.4 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 27-23 | 54.0 | 50.1 | 3.9 | +0.96 | 1.9 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 63-61 | 50.8 | 50.1 | 0.7 | -5.04 | -4.1 |  |  | no edge shown yet |
| follow_move+money_moving | total | 206-227 | 47.6 | 50.0 | -2.4 | -39.15 | -9.0 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 214-225 | 48.7 | 50.0 | -1.2 | -29.84 | -6.8 |  |  | DROP: below break-even |
| money_level+pin_move | total | 123-107 | 53.5 | 50.0 | 3.5 | +5.1 | 2.2 |  |  | no edge shown yet |
| money_level+pin_value | total | 86-76 | 53.1 | 50.1 | 3.0 | +1.04 | 0.6 |  |  | no edge shown yet |
| pin_move+pin_value | total | 78-71 | 52.3 | 50.0 | 2.4 | -0.6 | -0.4 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 90-114 | 44.1 | 49.9 | -5.8 | -31.5 | -15.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 139-146 | 48.8 | 49.9 | -1.2 | -18.98 | -6.7 |  |  | no edge shown yet |
| rlm_quiet+sharp_gap | total | 54-75 | 41.9 | 49.9 | -8.0 | -25.59 | -19.8 |  |  | DROP: below break-even |
| money_delta+money_moving | total | 118-112 | 51.3 | 49.9 | 1.4 | -4.14 | -1.8 |  |  | no edge shown yet |
| follow_move+money_level | total | 174-165 | 51.3 | 50.0 | 1.3 | -6.71 | -2.0 |  |  | no edge shown yet |
| follow_move+pin_value | total | 67-65 | 50.8 | 50.0 | 0.7 | -4.62 | -3.5 |  |  | no edge shown yet |
| money_moving+pin_value | total | 70-78 | 47.3 | 50.0 | -2.7 | -14.91 | -10.1 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 71-77 | 48.0 | 50.0 | -2.0 | -12.96 | -8.8 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 48-51 | 48.5 | 50.1 | -1.6 | -8.36 | -8.4 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 50-49 | 50.5 | 50.1 | 0.4 | -4.57 | -4.6 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 43-37 | 53.8 | 50.1 | 3.6 | +1.12 | 1.4 |  |  | no edge shown yet |
| consensus_gap+money_delta | total | 17-14 | 54.8 | 50.0 | 4.8 | +0.94 | 3.0 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | total | 11-9 | 55.0 | 50.0 | 5.0 | +0.81 | 4.1 |  |  | keep collecting (20/30) |
| money_delta+rlm_quiet | total | 23-41 | 35.9 | 49.8 | -13.9 | -19.95 | -31.2 |  |  | DROP: below break-even |
| money_delta+sharp_gap | total | 118-109 | 52.0 | 49.9 | 2.1 | -1.14 | -0.5 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 48-73 | 39.7 | 49.9 | -10.2 | -29.08 | -24.0 |  |  | DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 66-49 | 57.4 | 49.9 | 7.5 | +11.25 | 9.8 |  |  | no edge shown yet |
| money_delta+pin_move | total | 69-62 | 52.7 | 49.9 | 2.8 | +1.18 | 0.9 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 141-145 | 49.3 | 49.9 | -0.6 | -16.07 | -5.6 |  |  | no edge shown yet |
| follow_move+pin_move | total | 155-159 | 49.4 | 50.0 | -0.6 | -17.34 | -5.5 |  |  | no edge shown yet |
| pin_value+rlm_quiet | total | 20-26 | 43.5 | 49.9 | -6.4 | -7.67 | -16.7 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | total | 10-9 | 52.6 | 50.0 | 2.6 | -0.13 | -0.7 |  |  | keep collecting (19/30) |
| consensus_gap+rlm_ratio | total | 18-9 | 66.7 | 50.1 | 16.6 | +6.95 | 25.8 |  |  | keep collecting (27/30) |
| follow_move+pin_rlm | total | 66-56 | 54.1 | 49.9 | 4.2 | +4.71 | 3.9 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 127-106 | 54.5 | 49.9 | 4.6 | +10.28 | 4.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 39-25 | 60.9 | 49.9 | 11.1 | +10.86 | 17.0 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 64-43 | 59.8 | 49.9 | 9.9 | +15.53 | 14.5 |  |  | PROMOTE: beats break-even and its own base rate |
| money_moving+pin_rlm | total | 75-64 | 54.0 | 49.9 | 4.1 | +4.74 | 3.4 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 122-104 | 54.0 | 49.9 | 4.1 | +7.7 | 3.4 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 78-66 | 54.2 | 49.9 | 4.3 | +5.47 | 3.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 74-57 | 56.5 | 49.9 | 6.6 | +10.87 | 8.3 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 28-21 | 57.1 | 49.9 | 7.2 | +4.4 | 9.0 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 66-56 | 54.1 | 49.9 | 4.2 | +4.71 | 3.9 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 78-66 | 54.2 | 49.9 | 4.3 | +5.47 | 3.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 32-21 | 60.4 | 49.9 | 10.5 | +8.0 | 15.1 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 127-106 | 54.5 | 49.9 | 4.6 | +10.28 | 4.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 48-36 | 57.1 | 49.8 | 7.3 | +8.06 | 9.6 |  |  | no edge shown yet |
| money_delta+rlm_ratio | total | 78-55 | 58.6 | 49.9 | 8.8 | +16.27 | 12.2 |  |  | no edge shown yet |
| money_delta+pin_value | total | 36-28 | 56.2 | 49.9 | 6.3 | +4.51 | 7.0 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 42-58 | 42.0 | 49.9 | -7.9 | -19.45 | -19.5 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | total | 22-29 | 43.1 | 49.8 | -6.7 | -8.86 | -17.4 |  |  | no edge shown yet |
| rlm_quiet+rlm_ratio | total | 43-56 | 43.4 | 49.8 | -6.4 | -16.59 | -16.8 |  |  | DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 49.8 | 50.2 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| rlm_quiet | close | 1-3k bets | 128-189 | 40.4 | -1.3 | -6.7 |  |
| rlm_quiet | close | 3k+ bets | 45-65 | 40.9 | -1.6 | -11.0 |  |
| rlm_quiet | close | <1k bets | 22-28 | 44.0 | 2.5 | -6.0 |  |
| rlm_quiet | close | pin $1-2k | 50-88 | 36.2 | -7.1 | -17.8 |  |
| rlm_quiet | close | pin $2k+ | 55-66 | 45.5 | 7.5 | 5.9 |  |
| rlm_quiet | close | pin limit <$1k | 39-38 | 50.6 | 1.3 | -2.9 |  |
| pin_move | close | 1-3k bets | 327-324 | 50.2 | 0.3 | -2.5 |  |
| pin_move | close | 3k+ bets | 124-125 | 49.8 | 0.1 | -3.7 |  |
| pin_move | close | <1k bets | 67-68 | 49.6 | -0.9 | -4.6 |  |
| pin_move | close | pin $1-2k | 242-238 | 50.4 | 0.1 | -1.3 |  |
| pin_move | close | pin $2k+ | 184-189 | 49.3 | -0.4 | -6.4 |  |
| pin_move | close | pin limit <$1k | 92-90 | 50.5 | 1.0 | -0.9 |  |
| money_delta | close | 1-3k bets | 209-265 | 44.1 | -0.6 | -6.9 |  |
| money_delta | close | 3k+ bets | 83-111 | 42.8 | -0.4 | -2.1 |  |
| money_delta | close | <1k bets | 38-62 | 38.0 | -4.0 | -22.9 |  |
| money_delta | close | pin $1-2k | 117-121 | 49.2 | 3.4 | 2.6 |  |
| money_delta | close | pin $2k+ | 83-113 | 42.3 | 1.3 | -9.7 |  |
| money_delta | close | pin limit <$1k | 53-55 | 49.1 | -0.2 | -1.9 |  |
| pin_rlm | close | 1-3k bets | 88-97 | 47.6 | 4.9 | 15.5 |  |
| pin_rlm | close | 3k+ bets | 34-44 | 43.6 | 1.6 | -4.8 |  |
| pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.6 | 11.0 |  |
| pin_rlm | close | pin $1-2k | 62-66 | 48.4 | 4.8 | 11.5 |  |
| pin_rlm | close | pin $2k+ | 39-65 | 37.5 | 1.7 | -1.6 |  |
| pin_rlm | close | pin limit <$1k | 42-31 | 57.5 | 8.9 | 22.5 |  |
| follow_move | close | 1-3k bets | 579-518 | 52.8 | 1.3 | -4.3 |  |
| follow_move | close | 3k+ bets | 198-184 | 51.8 | -0.1 | -5.1 |  |
| follow_move | close | <1k bets | 120-108 | 52.6 | -0.5 | -11.2 |  |
| follow_move | close | pin $1-2k | 270-294 | 47.9 | -3.2 | -10.6 |  |
| follow_move | close | pin $2k+ | 231-190 | 54.9 | 2.9 | -0.8 |  |
| follow_move | close | pin limit <$1k | 111-109 | 50.5 | 0.6 | -3.7 |  |
| rlm_ratio | close | 1-3k bets | 130-167 | 43.8 | -0.5 | -6.2 |  |
| rlm_ratio | close | 3k+ bets | 51-46 | 52.6 | 8.1 | 12.4 |  |
| rlm_ratio | close | <1k bets | 26-26 | 50.0 | 7.0 | 0.8 |  |
| rlm_ratio | close | pin $1-2k | 72-73 | 49.7 | 3.3 | 3.8 |  |
| rlm_ratio | close | pin $2k+ | 39-53 | 42.4 | 4.3 | -6.1 |  |
| rlm_ratio | close | pin limit <$1k | 47-35 | 57.3 | 8.3 | 10.7 |  |
| money_level | close | 1-3k bets | 736-525 | 58.4 | 2.7 | -2.1 |  |
| money_level | close | 3k+ bets | 255-201 | 55.9 | 0.7 | -2.9 |  |
| money_level | close | <1k bets | 145-118 | 55.1 | -0.8 | -11.5 |  |
| money_level | close | pin $1-2k | 333-287 | 53.7 | -0.3 | -4.4 |  |
| money_level | close | pin $2k+ | 287-224 | 56.2 | -1.2 | -7.3 |  |
| money_level | close | pin limit <$1k | 129-128 | 50.2 | -0.1 | -4.6 |  |
| sharp_gap | close | 1-3k bets | 545-657 | 45.3 | -2.0 | -9.4 |  |
| sharp_gap | close | 3k+ bets | 218-229 | 48.8 | 1.3 | 2.4 |  |
| sharp_gap | close | <1k bets | 114-137 | 45.4 | -2.4 | -14.6 |  |
| sharp_gap | close | pin $1-2k | 284-315 | 47.4 | -1.3 | -5.5 |  |
| sharp_gap | close | pin $2k+ | 227-264 | 46.2 | -0.2 | -3.8 |  |
| sharp_gap | close | pin limit <$1k | 118-127 | 48.2 | -1.3 | -4.0 |  |
| money_moving | close | 1-3k bets | 551-656 | 45.7 | -2.2 | -9.8 |  |
| money_moving | close | 3k+ bets | 217-231 | 48.4 | 0.7 | 0.9 |  |
| money_moving | close | <1k bets | 112-137 | 45.0 | -2.4 | -13.5 |  |
| money_moving | close | pin $1-2k | 282-318 | 47.0 | -2.0 | -6.2 |  |
| money_moving | close | pin $2k+ | 228-262 | 46.5 | 0.0 | -3.8 |  |
| money_moving | close | pin limit <$1k | 115-134 | 46.2 | -3.3 | -7.8 |  |
| pin_value | close | 1-3k bets | 237-240 | 49.7 | 1.8 | 3.9 |  |
| pin_value | close | 3k+ bets | 82-87 | 48.5 | -0.1 | -5.0 |  |
| pin_value | close | <1k bets | 54-44 | 55.1 | 7.9 | 10.6 |  |
| pin_value | close | pin $1-2k | 171-189 | 47.5 | -0.8 | -3.5 |  |
| pin_value | close | pin $2k+ | 106-115 | 48.0 | 1.9 | 4.3 |  |
| pin_value | close | pin limit <$1k | 96-67 | 58.9 | 9.0 | 14.4 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.9 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.9 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 233-291 | 44.5 | -4.0 | -11.2 |  |
| consensus_gap | close | 3k+ bets | 83-97 | 46.1 | -1.6 | 4.6 |  |
| consensus_gap | close | <1k bets | 40-78 | 33.9 | -9.8 | -30.7 |  |
| consensus_gap | close | pin $1-2k | 114-124 | 47.9 | -1.6 | -1.4 |  |
| consensus_gap | close | pin $2k+ | 94-106 | 47.0 | -2.9 | -2.8 |  |
| consensus_gap | close | pin limit <$1k | 51-45 | 53.1 | 2.9 | 3.8 |  |
| consensus_gap+follow_move | close | 1-3k bets | 96-88 | 52.2 | 0.3 | -2.2 |  |
| consensus_gap+money_level | close | 1-3k bets | 155-104 | 59.8 | 0.8 | 2.2 |  |
| consensus_gap+money_moving | close | 1-3k bets | 104-162 | 39.1 | -6.5 | -11.9 |  |
| consensus_gap+pin_move | close | 1-3k bets | 58-54 | 51.8 | 0.2 | 5.1 |  |
| consensus_gap+pin_value | close | 1-3k bets | 94-105 | 47.2 | 1.1 | -0.4 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 101-165 | 38.0 | -6.7 | -13.1 |  |
| follow_move+money_level | close | 1-3k bets | 385-266 | 59.1 | 2.8 | -3.3 |  |
| follow_move+money_moving | close | 1-3k bets | 311-336 | 48.1 | -1.2 | -8.3 |  |
| follow_move+pin_move | close | 1-3k bets | 235-237 | 49.8 | -0.4 | -5.6 |  |
| follow_move+pin_value | close | 1-3k bets | 79-78 | 50.3 | 1.8 | 1.5 |  |
| follow_move+sharp_gap | close | 1-3k bets | 313-335 | 48.3 | -0.6 | -7.0 |  |
| money_level+money_moving | close | 1-3k bets | 398-354 | 52.9 | 0.4 | -4.0 |  |
| money_level+pin_move | close | 1-3k bets | 202-181 | 52.7 | -0.1 | -3.8 |  |
| money_level+pin_value | close | 1-3k bets | 116-105 | 52.5 | 2.8 | -1.5 |  |
| money_level+sharp_gap | close | 1-3k bets | 384-346 | 52.6 | 0.4 | -3.6 |  |
| money_moving+pin_move | close | 1-3k bets | 198-213 | 48.2 | -0.9 | -3.1 |  |
| money_moving+pin_value | close | 1-3k bets | 103-128 | 44.6 | -2.8 | -7.6 |  |
| money_moving+sharp_gap | close | 1-3k bets | 521-627 | 45.4 | -2.1 | -9.0 |  |
| pin_move+pin_value | close | 1-3k bets | 106-101 | 51.2 | 2.1 | 0.5 |  |
| pin_move+sharp_gap | close | 1-3k bets | 203-213 | 48.8 | -0.0 | -1.5 |  |
| pin_value+sharp_gap | close | 1-3k bets | 104-131 | 44.3 | -2.9 | -8.3 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 128-189 | 40.4 | -1.3 | -6.7 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 64-113 | 36.2 | -5.0 | -14.3 |  |
| consensus_gap+money_delta | close | 1-3k bets | 27-66 | 29.0 | -8.4 | -22.4 |  |
| follow_move+money_delta | close | 1-3k bets | 101-118 | 46.1 | -0.6 | -8.5 |  |
| money_delta+money_level | close | 1-3k bets | 76-73 | 51.0 | 3.1 | 5.5 |  |
| money_delta+money_moving | close | 1-3k bets | 146-210 | 41.0 | -2.0 | -10.1 |  |
| money_delta+pin_value | close | 1-3k bets | 46-45 | 50.5 | 3.1 | 1.1 |  |
| money_delta+sharp_gap | close | 1-3k bets | 145-207 | 41.2 | -1.8 | -9.6 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 73-80 | 47.7 | 0.4 | 2.0 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 18-28 | 39.1 | 0.2 | 15.8 |  |
| money_level+pin_rlm | close | 1-3k bets | 39-30 | 56.5 | 8.0 | 8.8 |  |
| pin_move+pin_rlm | close | 1-3k bets | 80-80 | 50.0 | 5.5 | 11.4 |  |
| pin_rlm+pin_value | close | 1-3k bets | 29-25 | 53.7 | 7.6 | 28.3 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 88-97 | 47.6 | 4.9 | 15.5 |  |
| money_delta+pin_rlm | close | 1-3k bets | 50-54 | 48.1 | 4.8 | 15.0 |  |
| money_moving+pin_rlm | close | 1-3k bets | 83-93 | 47.2 | 4.4 | 15.8 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 21-33 | 38.9 | -0.8 | 1.7 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 130-167 | 43.8 | -0.5 | -6.2 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 70-82 | 46.1 | 0.4 | -7.3 |  |
| money_level+rlm_ratio | close | 1-3k bets | 60-58 | 50.8 | 1.5 | -1.9 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 124-160 | 43.7 | -0.8 | -6.1 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 130-167 | 43.8 | -0.5 | -6.2 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 15-34 | 30.6 | -5.3 | -8.6 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 57-110 | 34.1 | -7.1 | -17.8 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 52-97 | 34.9 | -4.7 | -14.0 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 57-74 | 43.5 | -0.6 | -7.5 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 35-60 | 36.8 | -6.6 | -22.4 |  |
| follow_move+pin_rlm | close | 1-3k bets | 63-73 | 46.3 | 2.0 | -3.9 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 68-68 | 50.0 | 4.3 | 3.1 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 25-43 | 36.8 | -3.0 | -15.5 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 63-73 | 46.3 | 2.0 | -3.9 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 27-21 | 56.2 | 8.4 | 8.0 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 17-21 | 44.7 | -0.4 | 12.3 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 50.2 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 31-27 | 53.4 | 3.2 | 3.8 |  |
| consensus_gap+money_moving | close | 3k+ bets | 34-54 | 38.6 | -6.0 | 12.1 |  |
| consensus_gap+pin_move | close | 3k+ bets | 21-19 | 52.5 | 2.1 | 6.4 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-6 | 33.3 | -6.7 | 6.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 35-33 | 51.5 | 4.8 | 5.6 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -1.0 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 35-54 | 39.3 | -5.1 | 15.1 |  |
| follow_move+money_moving | close | 3k+ bets | 106-109 | 49.3 | 0.1 | -3.4 |  |
| follow_move+pin_move | close | 3k+ bets | 94-91 | 50.8 | 0.8 | -1.2 |  |
| follow_move+pin_rlm | close | 3k+ bets | 32-30 | 51.6 | 7.6 | 13.7 |  |
| follow_move+pin_value | close | 3k+ bets | 32-32 | 50.0 | 0.1 | -6.2 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 51-46 | 52.6 | 8.1 | 12.4 |  |
| follow_move+sharp_gap | close | 3k+ bets | 108-108 | 50.0 | 1.2 | -1.4 |  |
| money_moving+pin_move | close | 3k+ bets | 72-81 | 47.1 | -1.2 | -6.6 |  |
| money_moving+pin_rlm | close | 3k+ bets | 33-43 | 43.4 | 1.7 | -4.9 |  |
| money_moving+pin_value | close | 3k+ bets | 40-50 | 44.4 | -3.2 | -8.8 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 49-44 | 52.7 | 8.3 | 13.0 |  |
| money_moving+sharp_gap | close | 3k+ bets | 210-221 | 48.7 | 1.2 | 2.2 |  |
| pin_move+pin_rlm | close | 3k+ bets | 32-38 | 45.7 | 2.0 | -0.1 |  |
| pin_move+pin_value | close | 3k+ bets | 32-39 | 45.1 | -4.3 | -15.2 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 34-31 | 52.3 | 6.9 | 13.3 |  |
| pin_move+sharp_gap | close | 3k+ bets | 72-81 | 47.1 | -0.9 | -5.9 |  |
| pin_rlm+pin_value | close | 3k+ bets | 6-14 | 30.0 | -15.8 | -42.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 32-30 | 51.6 | 7.6 | 13.7 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 34-44 | 43.6 | 1.6 | -4.8 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 9-9 | 50.0 | -0.2 | -5.1 |  |
| pin_value+sharp_gap | close | 3k+ bets | 40-49 | 44.9 | -2.7 | -7.8 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 51-46 | 52.6 | 8.1 | 12.4 |  |
| follow_move+money_delta | close | 3k+ bets | 40-49 | 44.9 | -0.4 | -7.0 |  |
| money_level+money_moving | close | 3k+ bets | 148-127 | 53.8 | 1.5 | -0.5 |  |
| money_level+sharp_gap | close | 3k+ bets | 147-124 | 54.2 | 2.2 | 1.0 |  |
| follow_move+money_level | close | 3k+ bets | 124-91 | 57.7 | 1.1 | -2.5 |  |
| money_level+rlm_ratio | close | 3k+ bets | 25-12 | 67.6 | 20.5 | 38.4 |  |
| consensus_gap+money_level | close | 3k+ bets | 46-45 | 50.5 | -6.4 | -12.7 |  |
| money_level+pin_move | close | 3k+ bets | 68-61 | 52.7 | -0.8 | -3.2 |  |
| money_level+pin_value | close | 3k+ bets | 46-44 | 51.1 | 0.7 | -5.2 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 7-12 | 36.8 | -1.0 | -5.4 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 45-65 | 40.9 | -1.6 | -11.0 |  |
| money_delta+money_moving | close | 3k+ bets | 63-84 | 42.9 | 0.7 | 2.9 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 19-26 | 42.2 | 0.9 | -2.3 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 23-35 | 39.7 | -2.5 | -10.9 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 21-34 | 38.2 | -3.9 | -13.1 |  |
| consensus_gap+money_delta | close | 3k+ bets | 12-23 | 34.3 | -4.1 | 18.4 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 10-26 | 27.8 | -15.1 | -38.6 |  |
| money_delta+sharp_gap | close | 3k+ bets | 61-81 | 43.0 | 0.9 | 3.6 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 26-31 | 45.6 | 2.0 | -0.4 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 11-16 | 40.7 | -0.9 | -3.2 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 7-11 | 38.9 | -10.8 | -25.7 |  |
| money_delta+money_level | close | 3k+ bets | 33-22 | 60.0 | 14.0 | 21.2 |  |
| money_level+pin_rlm | close | 3k+ bets | 16-9 | 64.0 | 19.2 | 37.0 |  |
| money_delta+pin_value | close | 3k+ bets | 18-19 | 48.6 | 2.8 | -8.3 |  |
| money_delta+pin_move | close | 3k+ bets | 36-42 | 46.2 | 1.0 | -5.7 |  |
| money_delta+pin_rlm | close | 3k+ bets | 22-27 | 44.9 | 3.1 | -4.5 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 30-25 | 54.5 | 9.9 | 15.6 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 47.9 | 87.7 |  |
| money_level+money_moving | close | <1k bets | 76-77 | 49.7 | -2.7 | -14.4 |  |
| money_level+sharp_gap | close | <1k bets | 79-77 | 50.6 | -2.1 | -13.9 |  |
| money_moving+sharp_gap | close | <1k bets | 110-135 | 44.9 | -2.6 | -14.7 |  |
| consensus_gap+money_level | close | <1k bets | 18-27 | 40.0 | -15.9 | -39.4 |  |
| consensus_gap+money_moving | close | <1k bets | 17-40 | 29.8 | -11.8 | -34.9 |  |
| consensus_gap+pin_move | close | <1k bets | 6-13 | 31.6 | -18.2 | -26.5 |  |
| consensus_gap+pin_value | close | <1k bets | 14-14 | 50.0 | 7.9 | 15.4 |  |
| consensus_gap+sharp_gap | close | <1k bets | 17-41 | 29.3 | -12.1 | -36.0 |  |
| money_level+pin_move | close | <1k bets | 34-35 | 49.3 | -5.0 | -13.5 |  |
| money_level+pin_value | close | <1k bets | 18-17 | 51.4 | 1.1 | -4.2 |  |
| money_moving+pin_move | close | <1k bets | 36-41 | 46.8 | -1.0 | -4.2 |  |
| money_moving+pin_value | close | <1k bets | 17-16 | 51.5 | 6.2 | 14.9 |  |
| pin_move+pin_value | close | <1k bets | 25-20 | 55.6 | 7.3 | 12.9 |  |
| pin_move+sharp_gap | close | <1k bets | 36-42 | 46.2 | -2.2 | -9.5 |  |
| pin_value+sharp_gap | close | <1k bets | 17-15 | 53.1 | 7.2 | 18.5 |  |
| follow_move+money_delta | close | <1k bets | 18-20 | 47.4 | 5.0 | -3.2 |  |
| follow_move+money_moving | close | <1k bets | 54-63 | 46.2 | -3.4 | -13.8 |  |
| follow_move+pin_move | close | <1k bets | 42-42 | 50.0 | -1.2 | -7.2 |  |
| follow_move+sharp_gap | close | <1k bets | 56-63 | 47.1 | -3.3 | -16.1 |  |
| money_delta+money_moving | close | <1k bets | 27-46 | 37.0 | -2.9 | -23.1 |  |
| money_delta+pin_move | close | <1k bets | 13-17 | 43.3 | -0.4 | -15.5 |  |
| money_delta+sharp_gap | close | <1k bets | 27-46 | 37.0 | -2.9 | -23.1 |  |
| follow_move+rlm_quiet | close | <1k bets | 22-28 | 44.0 | 2.5 | -6.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 26-26 | 50.0 | 7.0 | 0.8 |  |
| money_delta+rlm_quiet | close | <1k bets | 8-10 | 44.4 | 4.9 | -4.3 |  |
| money_delta+rlm_ratio | close | <1k bets | 16-15 | 51.6 | 10.1 | 6.3 |  |
| money_moving+rlm_quiet | close | <1k bets | 14-12 | 53.8 | 13.0 | 20.2 |  |
| money_moving+rlm_ratio | close | <1k bets | 26-26 | 50.0 | 7.0 | 0.8 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 10-10 | 50.0 | 10.5 | 5.6 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 13-13 | 50.0 | 8.3 | 3.3 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 26-26 | 50.0 | 7.0 | 0.8 |  |
| follow_move+money_level | close | <1k bets | 75-59 | 56.0 | -2.2 | -15.1 |  |
| consensus_gap+money_delta | close | <1k bets | 4-22 | 15.4 | -16.6 | -63.0 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -1.5 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 12-14 | 46.2 | 7.9 | -0.2 |  |
| money_moving+pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.6 | 11.0 |  |
| pin_rlm+sharp_gap | close | <1k bets | 21-21 | 50.0 | 9.6 | 11.0 |  |
| money_delta+pin_value | close | <1k bets | 6-8 | 42.9 | -3.3 | -19.4 |  |
| consensus_gap+follow_move | close | <1k bets | 9-20 | 31.0 | -19.1 | -51.4 |  |
| follow_move+pin_rlm | close | <1k bets | 16-11 | 59.3 | 16.4 | 17.3 |  |
| follow_move+pin_value | close | <1k bets | 18-12 | 60.0 | 11.2 | 13.8 |  |
| pin_move+pin_rlm | close | <1k bets | 19-16 | 54.3 | 11.1 | 15.0 |  |
| pin_move+rlm_quiet | close | <1k bets | 10-10 | 50.0 | 4.9 | 9.6 |  |
| pin_move+rlm_ratio | close | <1k bets | 16-13 | 55.2 | 10.3 | 7.8 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 21.5 | 60.8 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 7-5 | 58.3 | 16.1 | 15.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 16-11 | 59.3 | 16.4 | 17.3 |  |
| pin_value+rlm_quiet | close | <1k bets | 3-4 | 42.9 | -6.5 | -17.6 |  |
| pin_value+rlm_ratio | close | <1k bets | 4-1 | 80.0 | 31.0 | 51.7 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 2-7 | 22.2 | -12.1 | -57.2 |  |
| money_delta+money_level | close | <1k bets | 12-17 | 41.4 | -1.9 | -18.9 |  |
| money_level+rlm_ratio | close | <1k bets | 13-13 | 50.0 | 4.9 | -1.9 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 17.8 | 19.0 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 0-5 | 0.0 | -35.7 | -100.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 44-48 | 47.8 | -4.9 | -8.6 |  |
| consensus_gap+money_moving | close | pin $1-2k | 56-68 | 45.2 | -3.6 | -4.9 |  |
| consensus_gap+pin_move | close | pin $1-2k | 44-44 | 50.0 | -2.5 | 5.3 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-18 | 41.9 | 1.0 | 25.8 |  |
| consensus_gap+pin_value | close | pin $1-2k | 67-72 | 48.2 | 2.0 | -3.5 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-14 | 50.0 | 4.3 | 9.0 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 53-66 | 44.5 | -2.9 | -4.1 |  |
| follow_move+money_moving | close | pin $1-2k | 156-187 | 45.5 | -4.4 | -10.8 |  |
| follow_move+pin_move | close | pin $1-2k | 170-180 | 48.6 | -2.0 | -6.7 |  |
| follow_move+pin_rlm | close | pin $1-2k | 50-50 | 50.0 | 4.3 | 5.3 |  |
| follow_move+pin_value | close | pin $1-2k | 57-67 | 46.0 | -3.5 | -13.3 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 72-73 | 49.7 | 3.3 | 3.8 |  |
| follow_move+sharp_gap | close | pin $1-2k | 159-186 | 46.1 | -3.6 | -10.0 |  |
| money_moving+pin_move | close | pin $1-2k | 148-164 | 47.4 | -1.8 | -3.6 |  |
| money_moving+pin_rlm | close | pin $1-2k | 59-63 | 48.4 | 4.3 | 11.9 |  |
| money_moving+pin_value | close | pin $1-2k | 68-99 | 40.7 | -7.2 | -20.4 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 70-69 | 50.4 | 3.5 | 5.1 |  |
| money_moving+sharp_gap | close | pin $1-2k | 273-306 | 47.2 | -1.6 | -5.7 |  |
| pin_move+pin_rlm | close | pin $1-2k | 59-60 | 49.6 | 4.6 | 11.6 |  |
| pin_move+pin_value | close | pin $1-2k | 74-88 | 45.7 | -3.9 | -11.9 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 58-54 | 51.8 | 5.0 | 7.2 |  |
| pin_move+sharp_gap | close | pin $1-2k | 151-164 | 47.9 | -1.0 | -3.1 |  |
| pin_rlm+pin_value | close | pin $1-2k | 15-24 | 38.5 | -9.7 | -19.7 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 50-50 | 50.0 | 4.3 | 5.3 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 62-66 | 48.4 | 4.8 | 11.5 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 18-20 | 47.4 | -2.3 | -10.6 |  |
| pin_value+sharp_gap | close | pin $1-2k | 68-97 | 41.2 | -6.6 | -19.4 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 72-73 | 49.7 | 3.3 | 3.8 |  |
| follow_move+money_level | close | pin $1-2k | 186-173 | 51.8 | -2.6 | -9.1 |  |
| money_level+rlm_ratio | close | pin $1-2k | 42-32 | 56.8 | 8.2 | 10.7 |  |
| money_level+sharp_gap | close | pin $1-2k | 205-199 | 50.7 | -1.0 | -5.6 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 4-11 | 26.7 | -15.9 | -23.4 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 50-88 | 36.2 | -7.1 | -17.8 |  |
| money_level+money_moving | close | pin $1-2k | 206-203 | 50.4 | -1.6 | -6.6 |  |
| consensus_gap+money_level | close | pin $1-2k | 68-60 | 53.1 | -4.0 | -6.4 |  |
| money_level+pin_value | close | pin $1-2k | 78-80 | 49.4 | -0.6 | -7.6 |  |
| money_level+pin_move | close | pin $1-2k | 148-136 | 52.1 | -0.6 | -4.7 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 23-38 | 37.7 | -6.2 | -6.4 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 36-50 | 41.9 | -3.5 | -5.5 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 15-27 | 35.7 | -8.1 | -12.8 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 20-33 | 37.7 | -5.2 | -6.9 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 24-40 | 37.5 | -5.9 | -10.1 |  |
| money_level+pin_rlm | close | pin $1-2k | 30-22 | 57.7 | 11.2 | 13.4 |  |
| follow_move+money_delta | close | pin $1-2k | 58-60 | 49.2 | 2.8 | 1.1 |  |
| money_delta+money_moving | close | pin $1-2k | 80-93 | 46.2 | 2.0 | 0.1 |  |
| money_delta+pin_move | close | pin $1-2k | 61-64 | 48.8 | 1.5 | 3.3 |  |
| money_delta+pin_rlm | close | pin $1-2k | 38-41 | 48.1 | 4.6 | 11.0 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 44-40 | 52.4 | 6.4 | 10.0 |  |
| money_delta+sharp_gap | close | pin $1-2k | 80-91 | 46.8 | 2.5 | 1.2 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 47.9 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 44-36 | 55.0 | 7.1 | 7.1 |  |
| consensus_gap+money_delta | close | pin $1-2k | 16-26 | 38.1 | -2.6 | -10.1 |  |
| money_delta+pin_value | close | pin $1-2k | 37-43 | 46.2 | -2.1 | -12.6 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 14-29 | 32.6 | -11.0 | -22.0 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 9-22 | 29.0 | -20.1 | -44.3 |  |
| follow_move+money_level | close | pin $2k+ | 143-90 | 61.4 | 2.0 | -2.1 |  |
| follow_move+money_moving | close | pin $2k+ | 110-108 | 50.5 | 2.4 | -3.8 |  |
| follow_move+pin_move | close | pin $2k+ | 139-127 | 52.3 | 2.0 | -1.9 |  |
| follow_move+sharp_gap | close | pin $2k+ | 111-109 | 50.5 | 2.5 | -3.5 |  |
| money_level+money_moving | close | pin $2k+ | 154-140 | 52.4 | -0.4 | -5.2 |  |
| money_level+pin_move | close | pin $2k+ | 104-90 | 53.6 | -1.8 | -5.7 |  |
| money_level+sharp_gap | close | pin $2k+ | 154-141 | 52.2 | -0.6 | -5.1 |  |
| money_moving+pin_move | close | pin $2k+ | 97-106 | 47.8 | 0.3 | -4.9 |  |
| money_moving+sharp_gap | close | pin $2k+ | 222-258 | 46.2 | -0.1 | -3.7 |  |
| pin_move+sharp_gap | close | pin $2k+ | 97-107 | 47.5 | 0.1 | -4.9 |  |
| consensus_gap+money_delta | close | pin $2k+ | 7-25 | 21.9 | -10.1 | -56.9 |  |
| consensus_gap+money_moving | close | pin $2k+ | 32-62 | 34.0 | -10.1 | -9.4 |  |
| consensus_gap+pin_value | close | pin $2k+ | 40-47 | 46.0 | 3.5 | 10.3 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 34-65 | 34.3 | -10.3 | -8.8 |  |
| money_delta+money_moving | close | pin $2k+ | 57-81 | 41.3 | 2.8 | -8.2 |  |
| money_delta+pin_value | close | pin $2k+ | 18-21 | 46.2 | 3.5 | -11.8 |  |
| money_delta+sharp_gap | close | pin $2k+ | 55-80 | 40.7 | 2.2 | -9.2 |  |
| money_moving+pin_value | close | pin $2k+ | 54-66 | 45.0 | -0.1 | 3.3 |  |
| pin_value+sharp_gap | close | pin $2k+ | 54-67 | 44.6 | -0.3 | 2.5 |  |
| consensus_gap+pin_move | close | pin $2k+ | 26-31 | 45.6 | -4.7 | -14.3 |  |
| money_delta+pin_move | close | pin $2k+ | 31-44 | 41.3 | -1.1 | -14.8 |  |
| consensus_gap+follow_move | close | pin $2k+ | 29-26 | 52.7 | 0.0 | -12.1 |  |
| follow_move+pin_value | close | pin $2k+ | 34-30 | 53.1 | 6.3 | 15.6 |  |
| pin_move+pin_value | close | pin $2k+ | 47-45 | 51.1 | 3.4 | 0.2 |  |
| follow_move+money_delta | close | pin $2k+ | 31-39 | 44.3 | 2.4 | -8.0 |  |
| follow_move+pin_rlm | close | pin $2k+ | 28-41 | 40.6 | 3.0 | -7.3 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 39-53 | 42.4 | 4.3 | -6.1 |  |
| money_delta+money_level | close | pin $2k+ | 25-20 | 55.6 | 11.8 | 12.4 |  |
| money_delta+pin_rlm | close | pin $2k+ | 21-36 | 36.8 | 1.2 | -8.3 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 19-24 | 44.2 | 5.5 | -4.0 |  |
| money_level+pin_rlm | close | pin $2k+ | 15-10 | 60.0 | 16.3 | 27.1 |  |
| money_level+pin_value | close | pin $2k+ | 55-51 | 51.9 | 2.0 | -4.1 |  |
| money_level+rlm_ratio | close | pin $2k+ | 14-12 | 53.8 | 8.3 | 13.1 |  |
| money_moving+pin_rlm | close | pin $2k+ | 39-65 | 37.5 | 1.7 | -1.6 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 39-52 | 42.9 | 4.7 | -5.0 |  |
| pin_move+pin_rlm | close | pin $2k+ | 31-43 | 41.9 | 3.7 | -1.9 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 27-35 | 43.5 | 3.6 | -0.6 |  |
| pin_rlm+pin_value | close | pin $2k+ | 6-13 | 31.6 | -4.3 | 13.6 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 28-41 | 40.6 | 3.0 | -7.3 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 39-65 | 37.5 | 1.7 | -1.6 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 4-6 | 40.0 | -0.9 | -19.0 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 39-53 | 42.4 | 4.3 | -6.1 |  |
| consensus_gap+money_level | close | pin $2k+ | 60-48 | 55.6 | -7.3 | -13.2 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 55-66 | 45.5 | 7.5 | 5.9 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 16-21 | 43.2 | 4.7 | -10.0 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 26-37 | 41.3 | 5.7 | -7.2 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 13-27 | 32.5 | 0.2 | -20.0 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 20-33 | 37.7 | 5.1 | -11.5 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 26-38 | 40.6 | 5.2 | -8.6 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-20 | 16.7 | -14.1 | -27.9 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 4-12 | 25.0 | -3.2 | -46.7 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-11 | 0.0 | -29.2 | -100.0 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 35-43 | 44.9 | 5.0 | -2.0 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 5-7 | 41.7 | 5.5 | 64.1 |  |
| follow_move+money_delta | close | pin limit <$1k | 34-38 | 47.2 | -2.0 | -9.4 |  |
| money_level+money_moving | close | pin limit <$1k | 70-81 | 46.4 | -3.4 | -11.1 |  |
| money_level+sharp_gap | close | pin limit <$1k | 67-74 | 47.5 | -2.2 | -8.8 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 106-118 | 47.3 | -2.1 | -5.2 |  |
| consensus_gap+money_level | close | pin limit <$1k | 27-26 | 50.9 | 0.2 | -5.9 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 15-11 | 57.7 | 9.5 | 25.7 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 36-33 | 52.2 | 2.6 | 4.6 |  |
| follow_move+money_moving | close | pin limit <$1k | 67-76 | 46.9 | -2.5 | -9.9 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 72-75 | 49.0 | -0.4 | -5.9 |  |
| money_level+pin_move | close | pin limit <$1k | 52-51 | 50.5 | 0.6 | -3.6 |  |
| money_level+pin_value | close | pin limit <$1k | 47-35 | 57.3 | 7.3 | 8.5 |  |
| pin_move+pin_value | close | pin limit <$1k | 42-27 | 60.9 | 11.2 | 22.1 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 19-11 | 63.3 | 13.8 | 16.9 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 23-19 | 54.8 | 6.0 | 14.3 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 25-19 | 56.8 | 7.9 | 17.6 |  |
| follow_move+money_level | close | pin limit <$1k | 55-57 | 49.1 | -1.1 | -6.5 |  |
| follow_move+pin_move | close | pin limit <$1k | 62-63 | 49.6 | 0.1 | -5.0 |  |
| follow_move+pin_value | close | pin limit <$1k | 38-25 | 60.3 | 10.5 | 14.4 |  |
| money_moving+pin_move | close | pin limit <$1k | 61-65 | 48.4 | -1.0 | -3.8 |  |
| money_moving+pin_value | close | pin limit <$1k | 38-29 | 56.7 | 7.1 | 14.3 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 63-65 | 49.2 | -0.1 | -2.3 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 39-31 | 55.7 | 6.1 | 12.1 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 39-38 | 50.6 | 1.3 | -2.9 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 27-26 | 50.9 | 1.9 | -2.2 |  |
| money_delta+money_moving | close | pin limit <$1k | 46-46 | 50.0 | 0.8 | 0.6 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 9-6 | 60.0 | 13.2 | 43.2 |  |
| money_delta+money_level | close | pin limit <$1k | 25-20 | 55.6 | 5.7 | 6.4 |  |
| money_delta+pin_value | close | pin limit <$1k | 15-8 | 65.2 | 16.2 | 42.9 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 45-44 | 50.6 | 1.4 | 1.7 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 30-31 | 49.2 | 0.3 | 1.6 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 7-3 | 70.0 | 24.6 | 77.3 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 25-18 | 58.1 | 9.8 | 21.9 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 39-29 | 57.4 | 8.8 | 23.1 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 41-31 | 56.9 | 8.0 | 15.3 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-5 | 79.2 | 30.2 | 69.5 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 42-31 | 57.5 | 8.9 | 22.5 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 6-1 | 85.7 | 39.1 | 63.9 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 13-7 | 65.0 | 15.1 | 24.4 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 11-17 | 39.3 | -9.0 | -24.5 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 22-22 | 50.0 | 1.1 | -3.9 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 33-23 | 58.9 | 9.9 | 13.5 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 47-35 | 57.3 | 8.3 | 10.7 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 28-22 | 56.0 | 7.0 | 7.7 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 21-25 | 45.7 | -3.3 | -12.2 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 43-33 | 56.6 | 7.6 | 9.4 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 33-23 | 58.9 | 9.9 | 13.5 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 15-10 | 60.0 | 11.9 | 15.5 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 33-23 | 58.9 | 9.9 | 13.5 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 23-18 | 56.1 | 7.3 | 7.7 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 47-35 | 57.3 | 8.3 | 10.7 |  |
| money_level+pin_rlm | close | pin limit <$1k | 19-13 | 59.4 | 9.5 | 13.9 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 21-15 | 58.3 | 9.1 | 13.5 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 18-5 | 78.3 | 28.3 | 49.8 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 7-3 | 70.0 | 22.3 | 33.8 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 50.2 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -3.7 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -51.1 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 31-33 | 48.4 | 13.0 | 17.9 | 0.04 |
| rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -14.4 | -3.3 | -0.95 |
| rlm_quiet | early | pin limit <$1k | 5-7 | 41.7 | -2.4 | -15.0 | 0.27 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.2 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 5-8 | 38.5 | -9.6 | -31.5 | 0.32 |
| pin_move | early | pin $1-2k | 0-3 | 0.0 | -35.3 | -100.0 | 0.23 |
| pin_move | early | pin limit <$1k | 5-6 | 45.5 | -6.3 | -19.1 | 0.22 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.6 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 8-6 | 57.1 | 17.1 | 26.7 | -0.34 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -39.5 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 4-0 | 100.0 | 50.6 | 88.0 | -0.25 |
| pin_rlm | early | <1k bets | 1-2 | 33.3 | 6.5 | -35.8 | -1.0 |
| pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -26.9 | -100.0 | -1.75 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.1 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.3 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -51.1 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 407-340 | 54.5 | 2.4 | -4.8 | 0.16 |
| follow_move | early | pin $1-2k | 28-16 | 63.6 | 10.0 | 14.9 | -0.34 |
| follow_move | early | pin limit <$1k | 47-39 | 54.7 | 4.4 | 1.9 | -0.11 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 26-17 | 60.5 | 22.4 | 31.7 | 0.46 |
| rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.0 | 55.6 | -1.52 |
| rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 1.1 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 43.1 | 59.7 | 0.33 |
| money_level | early | <1k bets | 150-97 | 60.7 | 0.9 | -5.0 | -0.07 |
| money_level | early | pin $1-2k | 20-8 | 71.4 | 6.0 | 4.1 | 0.01 |
| money_level | early | pin limit <$1k | 24-26 | 48.0 | -5.2 | -11.4 | 0.22 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.5 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.3 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 123-105 | 53.9 | 5.4 | 3.8 | 0.35 |
| sharp_gap | early | pin $1-2k | 15-11 | 57.7 | 4.8 | 6.7 | -0.39 |
| sharp_gap | early | pin limit <$1k | 29-18 | 61.7 | 13.1 | 27.9 | 0.12 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.5 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 51.1 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 85-75 | 53.1 | 1.3 | -7.1 | 0.09 |
| money_moving | early | pin $1-2k | 8-8 | 50.0 | -8.4 | -31.4 | 0.21 |
| money_moving | early | pin limit <$1k | 23-9 | 71.9 | 22.7 | 52.0 | 0.42 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.8 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 36-40 | 47.4 | -1.0 | -10.4 | 0.12 |
| pin_value | early | pin $1-2k | 13-19 | 40.6 | -5.2 | -23.6 | 0.12 |
| pin_value | early | pin limit <$1k | 36-30 | 54.5 | 4.9 | 3.2 | 0.09 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -50.2 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -26.5 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.3 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.6 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 184-239 | 43.5 | -4.3 | -13.8 | 0.38 |
| consensus_gap | early | pin $1-2k | 12-20 | 37.5 | -7.9 | -28.2 | 0.51 |
| consensus_gap | early | pin limit <$1k | 18-34 | 34.6 | -15.6 | -28.2 | 0.28 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.6 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.6 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -1.1 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.3 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 5.1 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.2 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.9 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.5 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.7 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.2 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -1.1 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 3.5 | -6.9 | 0.3 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -0.6 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-6 | 53.8 | 6.6 | 0.8 | -0.31 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -3.7 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.3 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.1 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.5 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 2.9 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.6 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.8 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.1 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 50.9 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.6 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 50.9 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 52.1 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 12.0 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 18.8 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 17.3 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 17.3 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -26.9 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| follow_move+rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -51.1 | -100.0 | -0.5 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 51.1 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| rlm_quiet+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| rlm_quiet+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 38.5 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 50.2 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 28-34 | 45.2 | -7.2 | -18.5 | 0.76 |
| consensus_gap+money_level | early | <1k bets | 31-22 | 58.5 | -7.5 | -10.1 | 0.44 |
| consensus_gap+sharp_gap | early | <1k bets | 23-38 | 37.7 | -9.5 | -17.1 | 1.02 |
| follow_move+money_level | early | <1k bets | 78-36 | 68.4 | 7.3 | 0.9 | 0.01 |
| follow_move+sharp_gap | early | <1k bets | 67-32 | 67.7 | 17.6 | 20.0 | 0.41 |
| money_level+sharp_gap | early | <1k bets | 82-49 | 62.6 | 5.8 | 2.1 | 0.22 |
| follow_move+money_moving | early | <1k bets | 45-27 | 62.5 | 9.1 | 8.8 | 0.33 |
| money_level+money_moving | early | <1k bets | 53-38 | 58.2 | -0.8 | -8.3 | -0.13 |
| money_moving+sharp_gap | early | <1k bets | 50-43 | 53.8 | 3.9 | -3.5 | 0.25 |
| consensus_gap+money_moving | early | <1k bets | 12-19 | 38.7 | -11.2 | -38.8 | 0.25 |
| follow_move+pin_value | early | <1k bets | 13-11 | 54.2 | 4.4 | 1.3 | -0.01 |
| follow_move+rlm_quiet | early | <1k bets | 31-33 | 48.4 | 13.0 | 17.9 | 0.04 |
| money_moving+rlm_quiet | early | <1k bets | 12-9 | 57.1 | 20.5 | 36.4 | 0.38 |
| rlm_quiet+sharp_gap | early | <1k bets | 19-13 | 59.4 | 22.5 | 31.0 | -0.23 |
| follow_move+rlm_ratio | early | <1k bets | 26-17 | 60.5 | 22.4 | 31.7 | 0.46 |
| rlm_quiet+rlm_ratio | early | <1k bets | 17-10 | 63.0 | 26.0 | 41.1 | -0.24 |
| rlm_ratio+sharp_gap | early | <1k bets | 26-17 | 60.5 | 22.4 | 31.7 | 0.46 |
| pin_move+pin_value | early | <1k bets | 1-4 | 20.0 | -29.2 | -61.8 | 0.2 |
| follow_move+pin_move | early | <1k bets | 5-3 | 62.5 | 10.4 | 11.2 | 0.42 |
| consensus_gap+pin_value | early | <1k bets | 13-23 | 36.1 | -10.5 | -32.5 | 0.4 |
| pin_value+rlm_quiet | early | <1k bets | 0-3 | 0.0 | -42.9 | -100.0 | -0.6 |
| money_delta+money_moving | early | <1k bets | 7-6 | 53.8 | 14.6 | 21.7 | -0.36 |
| money_delta+sharp_gap | early | <1k bets | 6-4 | 60.0 | 21.6 | 39.1 | -0.47 |
| consensus_gap+pin_move | early | <1k bets | 0-5 | 0.0 | -44.5 | -100.0 | 0.26 |
| money_level+pin_move | early | <1k bets | 2-2 | 50.0 | -5.8 | -21.8 | 0.1 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -26.9 | -100.0 | -4.8 |
| consensus_gap+rlm_quiet | early | <1k bets | 3-5 | 37.5 | -0.8 | -22.7 | 1.01 |
| consensus_gap+rlm_ratio | early | <1k bets | 4-3 | 57.1 | 17.2 | 15.6 | 0.6 |
| follow_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 23.1 | -3.7 | -2.15 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -26.9 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | <1k bets | 0-1 | 0.0 | -26.9 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 23.1 | -3.7 | -2.15 |
| pin_rlm+sharp_gap | early | <1k bets | 1-2 | 33.3 | 6.5 | -35.8 | -1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 11.7 | -4.5 | -1.9 |
| pin_value+sharp_gap | early | <1k bets | 5-4 | 55.6 | 8.3 | 6.1 | -0.09 |
| money_level+pin_value | early | <1k bets | 4-4 | 50.0 | -0.1 | -4.5 | 0.88 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -50.9 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -49.8 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 1-2 | 33.3 | -17.4 | -36.4 | 1.33 |
| money_level+rlm_ratio | early | <1k bets | 7-7 | 50.0 | 11.5 | 4.8 | 1.93 |
| money_moving+rlm_ratio | early | <1k bets | 11-7 | 61.1 | 18.9 | 36.3 | 0.47 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 49.8 | 90.9 | 0.0 |
| money_delta+money_level | early | <1k bets | 3-1 | 75.0 | 30.8 | 61.5 | 1.2 |
| pin_move+sharp_gap | early | <1k bets | 2-1 | 66.7 | 16.6 | 4.3 | -0.07 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 73.1 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 73.1 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 73.1 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 3-3 | 50.0 | 11.7 | 37.5 | 0.07 |
| money_delta+rlm_quiet | early | <1k bets | 1-2 | 33.3 | -1.2 | 23.3 | -2.8 |
| money_delta+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 32.2 | 111.3 | 0.87 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 50.2 | 90.9 | -1.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -26.9 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 5-4 | 55.6 | -9.2 | -12.6 | 0.71 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -31.4 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 5-10 | 33.3 | -8.1 | -38.7 | 0.31 |
| follow_move+rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -14.4 | -3.3 | -0.95 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.0 | 55.6 | -1.52 |
| follow_move+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 13.9 | 37.5 | -0.83 |
| money_level+money_moving | early | pin $1-2k | 8-5 | 61.5 | -4.2 | -15.6 | 0.07 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.8 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -8.2 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -8.2 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-3 | 40.0 | 3.0 | 55.6 | -1.52 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -39.5 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -39.5 | -100.0 | 2.5 |
| money_level+sharp_gap | early | pin $1-2k | 12-4 | 75.0 | 10.5 | 12.5 | -0.26 |
| money_moving+sharp_gap | early | pin $1-2k | 4-6 | 40.0 | -16.7 | -45.4 | 0.08 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -9.0 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 4-6 | 40.0 | -10.0 | -31.3 | 0.34 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 0-3 | 0.0 | -26.9 | -100.0 | -0.97 |
| follow_move+pin_value | early | pin $1-2k | 6-5 | 54.5 | 7.0 | 0.8 | -0.3 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -26.9 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 11-4 | 73.3 | 8.3 | 6.6 | -0.07 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 47.9 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 4-1 | 80.0 | 11.9 | 6.9 | -0.18 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.9 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -26.9 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -16.7 | -46.8 | -0.12 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.9 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -26.9 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | pin $1-2k | 0-1 | 0.0 | -26.9 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -26.9 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -26.9 | -100.0 | -1.75 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -26.9 | -100.0 | -4.8 |
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -26.9 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.9 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin limit <$1k | 5-7 | 41.7 | -2.4 | -15.0 | 0.27 |
| money_level+money_moving | early | pin limit <$1k | 13-7 | 65.0 | 12.8 | 20.2 | 0.48 |
| money_level+sharp_gap | early | pin limit <$1k | 20-16 | 55.6 | 5.0 | 1.6 | 0.14 |
| money_moving+sharp_gap | early | pin limit <$1k | 18-5 | 78.3 | 30.3 | 70.1 | 0.35 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -50.2 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 9-6 | 60.0 | 10.1 | 13.8 | 0.33 |
| money_moving+pin_value | early | pin limit <$1k | 7-4 | 63.6 | 13.9 | 20.1 | 0.18 |
| pin_value+sharp_gap | early | pin limit <$1k | 12-6 | 66.7 | 16.8 | 26.4 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-9 | 40.0 | -12.2 | -25.7 | 0.53 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -26.5 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 14-18 | 43.8 | -5.3 | -17.9 | 0.43 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.0 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 11-11 | 50.0 | -3.8 | -7.4 | -0.04 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 4.4 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 13-7 | 65.0 | 16.5 | 24.2 | -0.07 |
| follow_move+rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level+rlm_ratio | early | pin limit <$1k | 6-0 | 100.0 | 54.0 | 92.6 | 0.42 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 16.7 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| consensus_gap+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 50.9 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 22.7 | 72.3 | 0.54 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 1.1 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 50.9 | 85.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 9-3 | 75.0 | 25.5 | 43.3 | 0.33 |
| money_delta+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_delta+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 52.1 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 3-1 | 75.0 | 25.6 | 41.3 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.0 | 45.3 | -0.5 |
| money_delta+sharp_gap | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 | -0.5 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 11.5 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 24.4 | 51.6 | -0.07 |
| pin_move+pin_value | early | pin limit <$1k | 1-4 | 20.0 | -29.2 | -61.8 | 0.2 |
| follow_move+pin_move | early | pin limit <$1k | 5-3 | 62.5 | 10.4 | 11.2 | 0.42 |
| consensus_gap+pin_move | early | pin limit <$1k | 0-3 | 0.0 | -56.3 | -100.0 | 0.53 |
| money_level+pin_move | early | pin limit <$1k | 2-2 | 50.0 | -5.8 | -21.8 | 0.1 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -49.8 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -49.8 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 16.6 | 4.3 | -0.07 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.1 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.1 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.1 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 73.1 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 73.1 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 73.1 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 50.2 | 90.9 | -1.0 |
| rlm_quiet | close | 1-3k bets | 116-169 | 40.7 | -1.0 | -8.2 |  |
| rlm_quiet | close | 3k+ bets | 44-60 | 42.3 | -0.3 | -8.1 |  |
| rlm_quiet | close | <1k bets | 22-28 | 44.0 | 2.4 | -6.0 |  |
| rlm_quiet | close | pin $1-2k | 46-80 | 36.5 | -6.5 | -16.7 |  |
| rlm_quiet | close | pin $2k+ | 51-62 | 45.1 | 7.4 | -2.5 |  |
| rlm_quiet | close | pin limit <$1k | 36-36 | 50.0 | 0.1 | -4.2 |  |
| pin_move | close | 1-3k bets | 308-303 | 50.4 | 0.5 | -1.8 |  |
| pin_move | close | 3k+ bets | 120-123 | 49.4 | -0.3 | -4.6 |  |
| pin_move | close | <1k bets | 67-68 | 49.6 | -1.0 | -4.6 |  |
| pin_move | close | pin $1-2k | 234-226 | 50.9 | 0.5 | -0.3 |  |
| pin_move | close | pin $2k+ | 174-183 | 48.7 | -0.8 | -7.2 |  |
| pin_move | close | pin limit <$1k | 87-85 | 50.6 | 0.8 | -0.7 |  |
| money_delta | close | 1-3k bets | 199-252 | 44.1 | -0.6 | -6.4 |  |
| money_delta | close | 3k+ bets | 79-109 | 42.0 | -1.1 | -3.3 |  |
| money_delta | close | <1k bets | 38-62 | 38.0 | -4.1 | -22.9 |  |
| money_delta | close | pin $1-2k | 112-115 | 49.3 | 3.6 | 3.3 |  |
| money_delta | close | pin $2k+ | 82-110 | 42.7 | 1.7 | -8.9 |  |
| money_delta | close | pin limit <$1k | 50-54 | 48.1 | -1.7 | -3.7 |  |
| pin_rlm | close | 1-3k bets | 87-92 | 48.6 | 6.0 | 18.3 |  |
| pin_rlm | close | 3k+ bets | 32-44 | 42.1 | -0.0 | -7.9 |  |
| pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| pin_rlm | close | pin $1-2k | 61-64 | 48.8 | 5.0 | 12.7 |  |
| pin_rlm | close | pin $2k+ | 38-64 | 37.3 | 1.9 | -1.9 |  |
| pin_rlm | close | pin limit <$1k | 41-29 | 58.6 | 9.3 | 24.9 |  |
| follow_move | close | 1-3k bets | 547-479 | 53.3 | 1.7 | -4.5 |  |
| follow_move | close | 3k+ bets | 190-177 | 51.8 | -0.2 | -5.2 |  |
| follow_move | close | <1k bets | 120-108 | 52.6 | -0.6 | -11.2 |  |
| follow_move | close | pin $1-2k | 259-280 | 48.1 | -3.1 | -10.5 |  |
| follow_move | close | pin $2k+ | 217-181 | 54.5 | 2.3 | -3.9 |  |
| follow_move | close | pin limit <$1k | 105-104 | 50.2 | 0.2 | -4.1 |  |
| rlm_ratio | close | 1-3k bets | 126-155 | 44.8 | 0.0 | -3.6 |  |
| rlm_ratio | close | 3k+ bets | 48-44 | 52.2 | 7.5 | 11.8 |  |
| rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.9 | 0.8 |  |
| rlm_ratio | close | pin $1-2k | 70-71 | 49.6 | 3.1 | 4.0 |  |
| rlm_ratio | close | pin $2k+ | 38-50 | 43.2 | 5.0 | -4.4 |  |
| rlm_ratio | close | pin limit <$1k | 44-34 | 56.4 | 6.7 | 8.9 |  |
| money_level | close | 1-3k bets | 695-493 | 58.5 | 2.9 | -1.9 |  |
| money_level | close | 3k+ bets | 244-193 | 55.8 | 0.7 | -3.1 |  |
| money_level | close | <1k bets | 145-118 | 55.1 | -0.8 | -11.5 |  |
| money_level | close | pin $1-2k | 317-276 | 53.5 | -0.6 | -4.9 |  |
| money_level | close | pin $2k+ | 275-213 | 56.4 | -1.0 | -7.0 |  |
| money_level | close | pin limit <$1k | 124-121 | 50.6 | 0.5 | -3.8 |  |
| sharp_gap | close | 1-3k bets | 523-620 | 45.8 | -1.7 | -8.3 |  |
| sharp_gap | close | 3k+ bets | 210-218 | 49.1 | 1.7 | 3.4 |  |
| sharp_gap | close | <1k bets | 114-137 | 45.4 | -2.4 | -14.6 |  |
| sharp_gap | close | pin $1-2k | 275-302 | 47.7 | -1.1 | -4.8 |  |
| sharp_gap | close | pin $2k+ | 221-250 | 46.9 | 0.7 | -2.0 |  |
| sharp_gap | close | pin limit <$1k | 115-122 | 48.5 | -1.2 | -3.2 |  |
| money_moving | close | 1-3k bets | 526-619 | 45.9 | -1.9 | -8.8 |  |
| money_moving | close | 3k+ bets | 209-220 | 48.7 | 1.0 | 1.8 |  |
| money_moving | close | <1k bets | 112-137 | 45.0 | -2.5 | -13.5 |  |
| money_moving | close | pin $1-2k | 272-306 | 47.1 | -1.9 | -5.8 |  |
| money_moving | close | pin $2k+ | 222-248 | 47.2 | 1.0 | -2.0 |  |
| money_moving | close | pin limit <$1k | 110-128 | 46.2 | -3.5 | -7.6 |  |
| pin_value | close | 1-3k bets | 217-228 | 48.8 | 1.0 | 0.3 |  |
| pin_value | close | 3k+ bets | 80-85 | 48.5 | -0.0 | -5.0 |  |
| pin_value | close | <1k bets | 54-44 | 55.1 | 8.0 | 10.6 |  |
| pin_value | close | pin $1-2k | 162-182 | 47.1 | -1.1 | -4.5 |  |
| pin_value | close | pin $2k+ | 97-112 | 46.4 | 0.6 | -2.4 |  |
| pin_value | close | pin limit <$1k | 92-63 | 59.4 | 9.7 | 15.4 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 48.0 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 48.0 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 210-275 | 43.3 | -4.5 | -12.3 |  |
| consensus_gap | close | 3k+ bets | 81-95 | 46.0 | -1.4 | 5.1 |  |
| consensus_gap | close | <1k bets | 40-78 | 33.9 | -9.7 | -30.7 |  |
| consensus_gap | close | pin $1-2k | 107-120 | 47.1 | -1.8 | -2.0 |  |
| consensus_gap | close | pin $2k+ | 82-102 | 44.6 | -4.4 | -5.5 |  |
| consensus_gap | close | pin limit <$1k | 49-43 | 53.3 | 3.1 | 4.1 |  |
| consensus_gap+follow_move | close | 1-3k bets | 88-80 | 52.4 | 0.5 | -1.3 |  |
| consensus_gap+money_level | close | 1-3k bets | 141-94 | 60.0 | 1.2 | 2.9 |  |
| consensus_gap+money_moving | close | 1-3k bets | 98-150 | 39.5 | -5.5 | -9.8 |  |
| consensus_gap+pin_move | close | 1-3k bets | 53-51 | 51.0 | -0.5 | 4.5 |  |
| consensus_gap+pin_value | close | 1-3k bets | 84-99 | 45.9 | 0.3 | -1.9 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 96-153 | 38.6 | -5.7 | -10.9 |  |
| follow_move+money_level | close | 1-3k bets | 371-252 | 59.6 | 3.2 | -2.8 |  |
| follow_move+money_moving | close | 1-3k bets | 302-317 | 48.8 | -0.7 | -6.7 |  |
| follow_move+pin_move | close | 1-3k bets | 222-220 | 50.2 | 0.0 | -4.6 |  |
| follow_move+pin_value | close | 1-3k bets | 73-74 | 49.7 | 1.2 | -5.9 |  |
| follow_move+sharp_gap | close | 1-3k bets | 303-315 | 49.0 | -0.1 | -5.3 |  |
| money_level+money_moving | close | 1-3k bets | 379-333 | 53.2 | 0.8 | -3.3 |  |
| money_level+pin_move | close | 1-3k bets | 193-172 | 52.9 | 0.1 | -3.5 |  |
| money_level+pin_value | close | 1-3k bets | 110-98 | 52.9 | 3.3 | -0.8 |  |
| money_level+sharp_gap | close | 1-3k bets | 368-326 | 53.0 | 0.9 | -2.8 |  |
| money_moving+pin_move | close | 1-3k bets | 192-204 | 48.5 | -0.6 | -2.3 |  |
| money_moving+pin_value | close | 1-3k bets | 99-119 | 45.4 | -1.8 | -5.5 |  |
| money_moving+sharp_gap | close | 1-3k bets | 500-592 | 45.8 | -1.7 | -7.9 |  |
| pin_move+pin_value | close | 1-3k bets | 99-96 | 50.8 | 1.7 | 0.0 |  |
| pin_move+sharp_gap | close | 1-3k bets | 199-203 | 49.5 | 0.6 | 0.1 |  |
| pin_value+sharp_gap | close | 1-3k bets | 101-123 | 45.1 | -2.0 | -6.3 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 116-169 | 40.7 | -1.0 | -8.2 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 62-104 | 37.3 | -4.4 | -11.0 |  |
| consensus_gap+money_delta | close | 1-3k bets | 25-65 | 27.8 | -9.5 | -24.2 |  |
| follow_move+money_delta | close | 1-3k bets | 95-109 | 46.6 | -0.4 | -7.4 |  |
| money_delta+money_level | close | 1-3k bets | 74-72 | 50.7 | 2.7 | 5.0 |  |
| money_delta+money_moving | close | 1-3k bets | 139-202 | 40.8 | -2.3 | -10.1 |  |
| money_delta+pin_value | close | 1-3k bets | 44-44 | 50.0 | 2.6 | 0.2 |  |
| money_delta+sharp_gap | close | 1-3k bets | 138-200 | 40.8 | -2.3 | -9.9 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 70-77 | 47.6 | 0.1 | 2.1 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 17-26 | 39.5 | 1.6 | 19.2 |  |
| money_level+pin_rlm | close | 1-3k bets | 39-28 | 58.2 | 9.8 | 12.1 |  |
| pin_move+pin_rlm | close | 1-3k bets | 79-76 | 51.0 | 6.2 | 13.7 |  |
| pin_rlm+pin_value | close | 1-3k bets | 29-24 | 54.7 | 8.6 | 30.7 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 87-92 | 48.6 | 6.0 | 18.3 |  |
| money_delta+pin_rlm | close | 1-3k bets | 49-53 | 48.0 | 4.5 | 15.3 |  |
| money_moving+pin_rlm | close | 1-3k bets | 82-89 | 48.0 | 5.3 | 18.0 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 19-30 | 38.8 | -1.6 | 4.1 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 126-155 | 44.8 | 0.0 | -3.6 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 66-77 | 46.2 | 0.1 | -6.8 |  |
| money_level+rlm_ratio | close | 1-3k bets | 59-56 | 51.3 | 1.7 | -1.0 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 120-150 | 44.4 | -0.5 | -4.1 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 126-155 | 44.8 | 0.0 | -3.6 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 12-30 | 28.6 | -7.0 | -7.2 |  |
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
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 49.6 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 30-27 | 52.6 | 2.9 | 3.3 |  |
| consensus_gap+money_moving | close | 3k+ bets | 33-52 | 38.8 | -5.2 | 14.5 |  |
| consensus_gap+pin_move | close | 3k+ bets | 21-19 | 52.5 | 2.2 | 6.4 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-6 | 33.3 | -6.4 | 6.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 34-33 | 50.7 | 4.3 | 4.3 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -0.7 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 34-52 | 39.5 | -4.3 | 17.6 |  |
| follow_move+money_moving | close | 3k+ bets | 101-106 | 48.8 | -0.4 | -4.1 |  |
| follow_move+pin_move | close | 3k+ bets | 91-89 | 50.6 | 0.5 | -1.8 |  |
| follow_move+pin_rlm | close | 3k+ bets | 30-30 | 50.0 | 5.8 | 10.3 |  |
| follow_move+pin_value | close | 3k+ bets | 32-32 | 50.0 | 0.1 | -6.2 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 48-44 | 52.2 | 7.5 | 11.8 |  |
| follow_move+sharp_gap | close | 3k+ bets | 103-105 | 49.5 | 0.8 | -2.0 |  |
| money_moving+pin_move | close | 3k+ bets | 70-80 | 46.7 | -1.5 | -7.1 |  |
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
| money_level+pin_move | close | 3k+ bets | 66-61 | 52.0 | -1.5 | -4.5 |  |
| money_level+pin_value | close | 3k+ bets | 44-43 | 50.6 | 0.3 | -6.3 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 7-12 | 36.8 | -0.8 | -5.4 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 44-60 | 42.3 | -0.3 | -8.1 |  |
| money_delta+money_moving | close | 3k+ bets | 60-83 | 42.0 | -0.2 | 1.4 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 19-24 | 44.2 | 2.7 | 2.2 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 23-32 | 41.8 | -0.3 | -6.0 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 21-31 | 40.4 | -1.7 | -8.0 |  |
| consensus_gap+money_delta | close | 3k+ bets | 12-23 | 34.3 | -3.9 | 18.4 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 10-24 | 29.4 | -13.2 | -34.9 |  |
| money_delta+sharp_gap | close | 3k+ bets | 58-80 | 42.0 | 0.0 | 2.1 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 25-29 | 46.3 | 2.5 | 0.7 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 11-16 | 40.7 | -0.9 | -3.2 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 7-11 | 38.9 | -11.1 | -25.7 |  |
| money_delta+money_level | close | 3k+ bets | 31-22 | 58.5 | 12.6 | 18.5 |  |
| money_level+pin_rlm | close | 3k+ bets | 15-9 | 62.5 | 17.9 | 34.6 |  |
| money_delta+pin_value | close | 3k+ bets | 18-19 | 48.6 | 2.8 | -8.3 |  |
| money_delta+pin_move | close | 3k+ bets | 35-41 | 46.1 | 0.9 | -5.8 |  |
| money_delta+pin_rlm | close | 3k+ bets | 21-27 | 43.8 | 2.1 | -6.6 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 28-24 | 53.8 | 9.4 | 14.8 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 48.0 | 87.7 |  |
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
| pin_move+sharp_gap | close | <1k bets | 36-42 | 46.2 | -2.4 | -9.5 |  |
| pin_value+sharp_gap | close | <1k bets | 17-15 | 53.1 | 7.2 | 18.5 |  |
| follow_move+money_delta | close | <1k bets | 18-20 | 47.4 | 4.8 | -3.2 |  |
| follow_move+money_moving | close | <1k bets | 54-63 | 46.2 | -3.5 | -13.8 |  |
| follow_move+pin_move | close | <1k bets | 42-42 | 50.0 | -1.4 | -7.2 |  |
| follow_move+sharp_gap | close | <1k bets | 56-63 | 47.1 | -3.4 | -16.1 |  |
| money_delta+money_moving | close | <1k bets | 27-46 | 37.0 | -3.0 | -23.1 |  |
| money_delta+pin_move | close | <1k bets | 13-17 | 43.3 | -0.6 | -15.5 |  |
| money_delta+sharp_gap | close | <1k bets | 27-46 | 37.0 | -3.0 | -23.1 |  |
| follow_move+rlm_quiet | close | <1k bets | 22-28 | 44.0 | 2.4 | -6.0 |  |
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
| pin_move+rlm_quiet | close | <1k bets | 10-10 | 50.0 | 4.7 | 9.6 |  |
| pin_move+rlm_ratio | close | <1k bets | 16-13 | 55.2 | 10.1 | 7.8 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 21.4 | 60.8 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 7-5 | 58.3 | 16.0 | 15.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 16-11 | 59.3 | 16.2 | 17.3 |  |
| pin_value+rlm_quiet | close | <1k bets | 3-4 | 42.9 | -6.6 | -17.6 |  |
| pin_value+rlm_ratio | close | <1k bets | 4-1 | 80.0 | 30.6 | 51.7 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 2-7 | 22.2 | -11.9 | -57.2 |  |
| money_delta+money_level | close | <1k bets | 12-17 | 41.4 | -2.1 | -18.9 |  |
| money_level+rlm_ratio | close | <1k bets | 13-13 | 50.0 | 4.6 | -1.9 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 17.6 | 19.0 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 0-5 | 0.0 | -35.6 | -100.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 41-46 | 47.1 | -5.1 | -9.7 |  |
| consensus_gap+money_moving | close | pin $1-2k | 54-65 | 45.4 | -2.9 | -3.4 |  |
| consensus_gap+pin_move | close | pin $1-2k | 43-43 | 50.0 | -2.5 | 5.6 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-18 | 41.9 | 1.1 | 25.8 |  |
| consensus_gap+pin_value | close | pin $1-2k | 64-70 | 47.8 | 1.9 | -4.1 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-14 | 50.0 | 4.5 | 9.0 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 52-63 | 45.2 | -1.8 | -2.5 |  |
| follow_move+money_moving | close | pin $1-2k | 152-183 | 45.4 | -4.5 | -11.0 |  |
| follow_move+pin_move | close | pin $1-2k | 165-169 | 49.4 | -1.3 | -5.1 |  |
| follow_move+pin_rlm | close | pin $1-2k | 49-48 | 50.5 | 4.5 | 6.6 |  |
| follow_move+pin_value | close | pin $1-2k | 56-65 | 46.3 | -3.2 | -12.7 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 70-71 | 49.6 | 3.1 | 4.0 |  |
| follow_move+sharp_gap | close | pin $1-2k | 155-181 | 46.1 | -3.6 | -9.9 |  |
| money_moving+pin_move | close | pin $1-2k | 145-160 | 47.5 | -1.8 | -3.3 |  |
| money_moving+pin_rlm | close | pin $1-2k | 58-62 | 48.3 | 4.2 | 12.2 |  |
| money_moving+pin_value | close | pin $1-2k | 66-95 | 41.0 | -6.9 | -19.7 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 68-68 | 50.0 | 3.1 | 4.6 |  |
| money_moving+sharp_gap | close | pin $1-2k | 264-294 | 47.3 | -1.4 | -5.2 |  |
| pin_move+pin_rlm | close | pin $1-2k | 58-58 | 50.0 | 4.8 | 12.8 |  |
| pin_move+pin_value | close | pin $1-2k | 71-86 | 45.2 | -4.4 | -12.7 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 57-52 | 52.3 | 5.2 | 8.4 |  |
| pin_move+sharp_gap | close | pin $1-2k | 148-159 | 48.2 | -0.9 | -2.4 |  |
| pin_rlm+pin_value | close | pin $1-2k | 15-24 | 38.5 | -9.9 | -19.7 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 49-48 | 50.5 | 4.5 | 6.6 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 61-64 | 48.8 | 5.0 | 12.7 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 18-20 | 47.4 | -2.5 | -10.6 |  |
| pin_value+sharp_gap | close | pin $1-2k | 66-93 | 41.5 | -6.2 | -18.7 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 70-71 | 49.6 | 3.1 | 4.0 |  |
| follow_move+money_level | close | pin $1-2k | 180-168 | 51.7 | -2.7 | -9.4 |  |
| money_level+rlm_ratio | close | pin $1-2k | 40-32 | 55.6 | 7.0 | 8.4 |  |
| money_level+sharp_gap | close | pin $1-2k | 197-191 | 50.8 | -1.0 | -5.7 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 3-11 | 21.4 | -20.4 | -31.6 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 46-80 | 36.5 | -6.5 | -16.7 |  |
| money_level+money_moving | close | pin $1-2k | 197-195 | 50.3 | -1.7 | -6.7 |  |
| consensus_gap+money_level | close | pin $1-2k | 63-56 | 52.9 | -3.9 | -6.4 |  |
| money_level+pin_value | close | pin $1-2k | 74-77 | 49.0 | -0.9 | -8.3 |  |
| money_level+pin_move | close | pin $1-2k | 144-132 | 52.2 | -0.7 | -4.7 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 23-37 | 38.3 | -5.6 | -4.8 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 33-44 | 42.9 | -2.4 | -2.1 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 15-25 | 37.5 | -6.8 | -8.4 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 20-31 | 39.2 | -4.1 | -3.2 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 24-38 | 38.7 | -5.1 | -7.2 |  |
| money_level+pin_rlm | close | pin $1-2k | 29-22 | 56.9 | 10.3 | 11.8 |  |
| follow_move+money_delta | close | pin $1-2k | 54-55 | 49.5 | 3.4 | 2.3 |  |
| money_delta+money_moving | close | pin $1-2k | 77-92 | 45.6 | 1.2 | -1.0 |  |
| money_delta+pin_move | close | pin $1-2k | 58-61 | 48.7 | 1.4 | 3.6 |  |
| money_delta+pin_rlm | close | pin $1-2k | 37-41 | 47.4 | 3.9 | 9.9 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 42-40 | 51.2 | 5.2 | 7.9 |  |
| money_delta+sharp_gap | close | pin $1-2k | 77-90 | 46.1 | 1.7 | 0.2 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 48.0 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 42-36 | 53.8 | 5.9 | 4.8 |  |
| consensus_gap+money_delta | close | pin $1-2k | 16-26 | 38.1 | -2.5 | -10.1 |  |
| money_delta+pin_value | close | pin $1-2k | 37-42 | 46.8 | -1.6 | -11.5 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 12-24 | 33.3 | -9.1 | -17.6 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 8-21 | 27.6 | -21.6 | -47.0 |  |
| follow_move+money_level | close | pin $2k+ | 138-87 | 61.3 | 1.9 | -2.0 |  |
| follow_move+money_moving | close | pin $2k+ | 106-102 | 51.0 | 3.1 | -2.5 |  |
| follow_move+pin_move | close | pin $2k+ | 131-122 | 51.8 | 1.8 | -2.5 |  |
| follow_move+sharp_gap | close | pin $2k+ | 107-103 | 51.0 | 3.2 | -2.2 |  |
| money_level+money_moving | close | pin $2k+ | 149-131 | 53.2 | 0.5 | -3.4 |  |
| money_level+pin_move | close | pin $2k+ | 100-88 | 53.2 | -2.0 | -6.0 |  |
| money_level+sharp_gap | close | pin $2k+ | 149-132 | 53.0 | 0.3 | -3.4 |  |
| money_moving+pin_move | close | pin $2k+ | 95-103 | 48.0 | 0.8 | -4.2 |  |
| money_moving+sharp_gap | close | pin $2k+ | 216-244 | 47.0 | 0.8 | -1.9 |  |
| pin_move+sharp_gap | close | pin $2k+ | 95-104 | 47.7 | 0.6 | -4.2 |  |
| consensus_gap+money_delta | close | pin $2k+ | 7-25 | 21.9 | -9.9 | -56.9 |  |
| consensus_gap+money_moving | close | pin $2k+ | 30-58 | 34.1 | -8.5 | -6.7 |  |
| consensus_gap+pin_value | close | pin $2k+ | 33-45 | 42.3 | 1.0 | 6.4 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 32-61 | 34.4 | -8.8 | -6.2 |  |
| money_delta+money_moving | close | pin $2k+ | 56-78 | 41.8 | 3.4 | -6.8 |  |
| money_delta+pin_value | close | pin $2k+ | 18-21 | 46.2 | 3.6 | -11.8 |  |
| money_delta+sharp_gap | close | pin $2k+ | 54-77 | 41.2 | 2.8 | -7.9 |  |
| money_moving+pin_value | close | pin $2k+ | 54-63 | 46.2 | 1.2 | 6.0 |  |
| pin_value+sharp_gap | close | pin $2k+ | 54-64 | 45.8 | 1.0 | 5.1 |  |
| consensus_gap+pin_move | close | pin $2k+ | 23-30 | 43.4 | -6.2 | -17.5 |  |
| money_delta+pin_move | close | pin $2k+ | 31-44 | 41.3 | -1.1 | -14.8 |  |
| consensus_gap+follow_move | close | pin $2k+ | 26-26 | 50.0 | -1.6 | -15.9 |  |
| follow_move+pin_value | close | pin $2k+ | 32-30 | 51.6 | 4.5 | -2.3 |  |
| pin_move+pin_value | close | pin $2k+ | 45-44 | 50.6 | 2.9 | -0.6 |  |
| follow_move+money_delta | close | pin $2k+ | 31-37 | 45.6 | 3.7 | -5.3 |  |
| follow_move+pin_rlm | close | pin $2k+ | 27-41 | 39.7 | 2.1 | -9.3 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 38-50 | 43.2 | 5.0 | -4.4 |  |
| money_delta+money_level | close | pin $2k+ | 24-20 | 54.5 | 11.0 | 10.6 |  |
| money_delta+pin_rlm | close | pin $2k+ | 21-36 | 36.8 | 1.4 | -8.3 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 19-22 | 46.3 | 7.7 | 0.7 |  |
| money_level+pin_rlm | close | pin $2k+ | 15-9 | 62.5 | 20.1 | 32.4 |  |
| money_level+pin_value | close | pin $2k+ | 53-49 | 52.0 | 2.1 | -4.0 |  |
| money_level+rlm_ratio | close | pin $2k+ | 14-11 | 56.0 | 9.7 | 17.6 |  |
| money_moving+pin_rlm | close | pin $2k+ | 38-64 | 37.3 | 1.9 | -1.9 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 38-49 | 43.7 | 5.3 | -3.3 |  |
| pin_move+pin_rlm | close | pin $2k+ | 31-43 | 41.9 | 3.9 | -1.9 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 27-35 | 43.5 | 3.7 | -0.6 |  |
| pin_rlm+pin_value | close | pin $2k+ | 6-13 | 31.6 | -4.2 | 13.6 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 27-41 | 39.7 | 2.1 | -9.3 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 38-64 | 37.3 | 1.9 | -1.9 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 4-6 | 40.0 | -0.9 | -19.0 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 38-50 | 43.2 | 5.0 | -4.4 |  |
| consensus_gap+money_level | close | pin $2k+ | 53-44 | 54.6 | -8.2 | -15.0 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 51-62 | 45.1 | 7.4 | -2.5 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 16-20 | 44.4 | 5.7 | -7.5 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 26-35 | 42.6 | 7.3 | -4.2 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 13-27 | 32.5 | 0.4 | -20.0 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 20-32 | 38.5 | 5.9 | -9.7 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 26-36 | 41.9 | 6.7 | -5.7 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-19 | 17.4 | -11.3 | -24.8 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 4-12 | 25.0 | -2.9 | -46.7 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-11 | 0.0 | -28.9 | -100.0 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 34-40 | 45.9 | 6.1 | -0.0 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 4-7 | 36.4 | -0.5 | -26.4 |  |
| follow_move+money_delta | close | pin limit <$1k | 31-37 | 45.6 | -4.3 | -12.5 |  |
| money_level+money_moving | close | pin limit <$1k | 68-77 | 46.9 | -2.9 | -10.0 |  |
| money_level+sharp_gap | close | pin limit <$1k | 67-71 | 48.6 | -1.3 | -6.8 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 103-113 | 47.7 | -2.0 | -4.4 |  |
| consensus_gap+money_level | close | pin limit <$1k | 27-25 | 51.9 | 1.4 | -4.1 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 14-10 | 58.3 | 9.7 | 27.8 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 35-31 | 53.0 | 3.8 | 6.4 |  |
| follow_move+money_moving | close | pin limit <$1k | 64-73 | 46.7 | -3.0 | -10.2 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 69-73 | 48.6 | -1.1 | -6.6 |  |
| money_level+pin_move | close | pin limit <$1k | 49-48 | 50.5 | 0.6 | -3.5 |  |
| money_level+pin_value | close | pin limit <$1k | 45-32 | 58.4 | 8.8 | 10.6 |  |
| pin_move+pin_value | close | pin limit <$1k | 40-25 | 61.5 | 12.0 | 23.8 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 17-10 | 63.0 | 12.7 | 15.4 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 21-17 | 55.3 | 6.2 | 16.0 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 23-18 | 56.1 | 6.9 | 16.7 |  |
| follow_move+money_level | close | pin limit <$1k | 53-54 | 49.5 | -0.7 | -5.7 |  |
| follow_move+pin_move | close | pin limit <$1k | 59-60 | 49.6 | -0.3 | -5.1 |  |
| follow_move+pin_value | close | pin limit <$1k | 35-23 | 60.3 | 10.7 | 14.5 |  |
| money_moving+pin_move | close | pin limit <$1k | 58-62 | 48.3 | -1.4 | -3.8 |  |
| money_moving+pin_value | close | pin limit <$1k | 35-25 | 58.3 | 9.0 | 18.1 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 62-62 | 50.0 | 0.2 | -0.8 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 37-28 | 56.9 | 7.4 | 14.9 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 36-36 | 50.0 | 0.1 | -4.2 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 25-26 | 49.0 | -0.8 | -6.1 |  |
| money_delta+money_moving | close | pin limit <$1k | 43-45 | 48.9 | -0.8 | -1.4 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 7-6 | 53.8 | 5.8 | 35.2 |  |
| money_delta+money_level | close | pin limit <$1k | 25-19 | 56.8 | 6.7 | 8.8 |  |
| money_delta+pin_value | close | pin limit <$1k | 13-8 | 61.9 | 13.0 | 38.5 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 42-43 | 49.4 | -0.3 | -0.3 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 29-30 | 49.2 | -0.4 | 1.6 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 6-2 | 75.0 | 28.1 | 96.7 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 24-17 | 58.5 | 9.4 | 23.0 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 38-27 | 58.5 | 9.3 | 25.7 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 40-29 | 58.0 | 8.4 | 17.5 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-4 | 82.6 | 33.5 | 76.8 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 41-29 | 58.6 | 9.3 | 24.9 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 4-1 | 80.0 | 29.9 | 51.3 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 12-7 | 63.2 | 13.0 | 20.9 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 9-17 | 34.6 | -14.9 | -33.8 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 20-21 | 48.8 | -0.9 | -6.4 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 32-22 | 59.3 | 9.4 | 14.0 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 44-34 | 56.4 | 6.7 | 8.9 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 25-21 | 54.3 | 4.5 | 4.4 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 19-25 | 43.2 | -6.7 | -17.1 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 40-32 | 55.6 | 5.9 | 7.4 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 32-22 | 59.3 | 9.4 | 14.0 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 14-10 | 58.3 | 9.0 | 11.9 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 32-22 | 59.3 | 9.4 | 14.0 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 21-18 | 53.8 | 4.1 | 3.2 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 44-34 | 56.4 | 6.7 | 8.9 |  |
| money_level+pin_rlm | close | pin limit <$1k | 19-12 | 61.3 | 11.0 | 17.6 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 21-14 | 60.0 | 10.4 | 16.8 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 16-5 | 76.2 | 26.0 | 46.1 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 5-3 | 62.5 | 12.6 | 18.4 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 49.6 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -3.3 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -50.8 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 28-29 | 49.1 | 13.8 | 20.7 | 0.2 |
| rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -14.2 | -3.3 | -0.95 |
| rlm_quiet | early | pin limit <$1k | 5-7 | 41.7 | -2.3 | -15.0 | 0.27 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -49.6 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 5-8 | 38.5 | -9.6 | -31.5 | 0.32 |
| pin_move | early | pin $1-2k | 0-3 | 0.0 | -35.1 | -100.0 | 0.23 |
| pin_move | early | pin limit <$1k | 5-6 | 45.5 | -6.3 | -19.1 | 0.22 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.8 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 8-6 | 57.1 | 17.0 | 26.7 | -0.34 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -39.3 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 4-0 | 100.0 | 50.4 | 88.0 | -0.25 |
| pin_rlm | early | <1k bets | 1-2 | 33.3 | 6.7 | -35.8 | -1.0 |
| pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -26.6 | -100.0 | -1.75 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.3 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -50.8 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 395-325 | 54.9 | 2.6 | -4.8 | 0.2 |
| follow_move | early | pin $1-2k | 27-16 | 62.8 | 8.5 | 11.9 | -0.35 |
| follow_move | early | pin limit <$1k | 47-39 | 54.7 | 4.4 | 1.9 | -0.11 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.0 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 24-14 | 63.2 | 26.0 | 39.0 | 0.52 |
| rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.2 | 55.6 | -1.52 |
| rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 0.9 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 42.8 | 59.7 | 0.33 |
| money_level | early | <1k bets | 141-90 | 61.0 | 1.3 | -4.7 | -0.15 |
| money_level | early | pin $1-2k | 20-8 | 71.4 | 5.8 | 4.1 | 0.01 |
| money_level | early | pin limit <$1k | 24-26 | 48.0 | -5.3 | -11.4 | 0.22 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.5 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.1 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 117-99 | 54.2 | 5.7 | 4.5 | 0.34 |
| sharp_gap | early | pin $1-2k | 15-11 | 57.7 | 4.8 | 6.7 | -0.39 |
| sharp_gap | early | pin limit <$1k | 29-18 | 61.7 | 13.1 | 27.9 | 0.12 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.5 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.8 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 78-71 | 52.3 | 0.7 | -9.0 | 0.01 |
| money_moving | early | pin $1-2k | 8-8 | 50.0 | -8.5 | -31.4 | 0.21 |
| money_moving | early | pin limit <$1k | 23-9 | 71.9 | 22.7 | 52.0 | 0.42 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.7 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 36-39 | 48.0 | -0.3 | -9.2 | 0.13 |
| pin_value | early | pin $1-2k | 13-18 | 41.9 | -3.8 | -21.1 | 0.12 |
| pin_value | early | pin limit <$1k | 36-30 | 54.5 | 5.0 | 3.2 | 0.09 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -49.6 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -26.6 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.3 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.7 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 176-236 | 42.7 | -4.7 | -14.8 | 0.37 |
| consensus_gap | early | pin $1-2k | 12-20 | 37.5 | -7.9 | -28.2 | 0.51 |
| consensus_gap | early | pin limit <$1k | 18-34 | 34.6 | -15.5 | -28.2 | 0.28 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -52.0 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.8 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.8 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -0.8 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.0 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 4.7 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.0 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.8 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.4 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.5 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -49.6 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -1.1 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 3.6 | -6.9 | 0.3 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -0.4 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-6 | 53.8 | 6.5 | 0.8 | -0.31 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -3.3 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.1 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.3 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.5 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 2.7 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.5 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.6 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.0 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.6 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 52.0 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 12.3 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 19.0 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 17.7 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 17.7 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| follow_move+rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -50.8 | -100.0 | -0.5 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.0 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.0 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.8 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| rlm_quiet+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.0 | -100.0 | -1.0 |
| rlm_quiet+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.0 | -100.0 | -1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.0 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 38.1 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 49.6 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 26-33 | 44.1 | -7.7 | -19.4 | 0.84 |
| consensus_gap+money_level | early | <1k bets | 28-21 | 57.1 | -8.4 | -10.9 | 0.38 |
| consensus_gap+sharp_gap | early | <1k bets | 22-38 | 36.7 | -10.1 | -18.6 | 1.0 |
| follow_move+money_level | early | <1k bets | 76-33 | 69.7 | 8.3 | 2.7 | -0.01 |
| follow_move+sharp_gap | early | <1k bets | 64-28 | 69.6 | 19.2 | 23.0 | 0.46 |
| money_level+sharp_gap | early | <1k bets | 79-47 | 62.7 | 6.1 | 2.0 | 0.15 |
| follow_move+money_moving | early | <1k bets | 41-24 | 63.1 | 9.3 | 8.5 | 0.32 |
| money_level+money_moving | early | <1k bets | 49-35 | 58.3 | -0.6 | -8.2 | -0.27 |
| money_moving+sharp_gap | early | <1k bets | 46-41 | 52.9 | 3.6 | -5.0 | 0.17 |
| consensus_gap+money_moving | early | <1k bets | 10-19 | 34.5 | -13.7 | -44.4 | 0.26 |
| follow_move+pin_value | early | <1k bets | 13-11 | 54.2 | 4.5 | 1.3 | -0.01 |
| follow_move+rlm_quiet | early | <1k bets | 28-29 | 49.1 | 13.8 | 20.7 | 0.2 |
| money_moving+rlm_quiet | early | <1k bets | 9-9 | 50.0 | 14.3 | 22.0 | 0.38 |
| rlm_quiet+sharp_gap | early | <1k bets | 17-11 | 60.7 | 24.9 | 36.0 | -0.07 |
| follow_move+rlm_ratio | early | <1k bets | 24-14 | 63.2 | 26.0 | 39.0 | 0.52 |
| rlm_quiet+rlm_ratio | early | <1k bets | 15-8 | 65.2 | 29.4 | 49.0 | -0.05 |
| rlm_ratio+sharp_gap | early | <1k bets | 24-14 | 63.2 | 26.0 | 39.0 | 0.52 |
| pin_move+pin_value | early | <1k bets | 1-4 | 20.0 | -29.1 | -61.8 | 0.2 |
| follow_move+pin_move | early | <1k bets | 5-3 | 62.5 | 10.2 | 11.2 | 0.42 |
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
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -50.4 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 1-2 | 33.3 | -17.3 | -36.4 | 1.33 |
| money_level+rlm_ratio | early | <1k bets | 7-6 | 53.8 | 16.3 | 12.9 | 1.69 |
| money_moving+rlm_ratio | early | <1k bets | 9-6 | 60.0 | 19.4 | 38.2 | 0.3 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 50.4 | 90.9 | 0.0 |
| money_delta+money_level | early | <1k bets | 3-1 | 75.0 | 30.8 | 61.5 | 1.2 |
| pin_move+sharp_gap | early | <1k bets | 2-1 | 66.7 | 16.8 | 4.3 | -0.07 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 3-3 | 50.0 | 11.5 | 37.5 | 0.07 |
| money_delta+rlm_quiet | early | <1k bets | 1-2 | 33.3 | -1.2 | 23.3 | -2.8 |
| money_delta+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 32.2 | 111.3 | 0.87 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 49.6 | 90.9 | -1.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -26.6 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 5-4 | 55.6 | -9.4 | -12.6 | 0.71 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -31.6 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 5-10 | 33.3 | -8.0 | -38.7 | 0.31 |
| follow_move+rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -14.2 | -3.3 | -0.95 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.2 | 55.6 | -1.52 |
| follow_move+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 13.8 | 37.5 | -0.83 |
| money_level+money_moving | early | pin $1-2k | 8-5 | 61.5 | -4.4 | -15.6 | 0.07 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.8 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -8.0 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -8.0 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-3 | 40.0 | 3.2 | 55.6 | -1.52 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -52.0 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -39.3 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -52.0 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -39.3 | -100.0 | 2.5 |
| money_level+sharp_gap | early | pin $1-2k | 12-4 | 75.0 | 10.4 | 12.5 | -0.26 |
| money_moving+sharp_gap | early | pin $1-2k | 4-6 | 40.0 | -16.8 | -45.4 | 0.08 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.9 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 4-6 | 40.0 | -10.0 | -31.3 | 0.34 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 0-3 | 0.0 | -26.6 | -100.0 | -0.97 |
| follow_move+pin_value | early | pin $1-2k | 6-5 | 54.5 | 7.0 | 0.8 | -0.3 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -26.6 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 11-4 | 73.3 | 8.1 | 6.6 | -0.07 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 48.0 | 98.0 | 0.0 |
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
| money_moving+sharp_gap | early | pin limit <$1k | 18-5 | 78.3 | 30.2 | 70.1 | 0.35 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -49.6 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 9-6 | 60.0 | 9.9 | 13.8 | 0.33 |
| money_moving+pin_value | early | pin limit <$1k | 7-4 | 63.6 | 13.8 | 20.1 | 0.18 |
| pin_value+sharp_gap | early | pin limit <$1k | 12-6 | 66.7 | 16.7 | 26.4 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-9 | 40.0 | -12.1 | -25.7 | 0.53 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -26.7 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 14-18 | 43.8 | -5.2 | -17.9 | 0.43 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.1 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 11-11 | 50.0 | -3.9 | -7.4 | -0.04 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 4.4 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 13-7 | 65.0 | 16.4 | 24.2 | -0.07 |
| follow_move+rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level+rlm_ratio | early | pin limit <$1k | 6-0 | 100.0 | 53.7 | 92.6 | 0.42 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 16.5 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| consensus_gap+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 22.8 | 72.3 | 0.54 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 0.8 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 9-3 | 75.0 | 25.5 | 43.3 | 0.33 |
| money_delta+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_delta+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 52.0 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 3-1 | 75.0 | 25.4 | 41.3 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.0 | 45.3 | -0.5 |
| money_delta+sharp_gap | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 | -0.5 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 11.9 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 24.5 | 51.6 | -0.07 |
| pin_move+pin_value | early | pin limit <$1k | 1-4 | 20.0 | -29.1 | -61.8 | 0.2 |
| follow_move+pin_move | early | pin limit <$1k | 5-3 | 62.5 | 10.2 | 11.2 | 0.42 |
| consensus_gap+pin_move | early | pin limit <$1k | 0-3 | 0.0 | -56.4 | -100.0 | 0.53 |
| money_level+pin_move | early | pin limit <$1k | 2-2 | 50.0 | -5.8 | -21.8 | 0.1 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -50.4 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -50.4 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 16.8 | 4.3 | -0.07 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 73.4 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 49.6 | 90.9 | -1.0 |
| rlm_quiet | close | 1-3k bets | 12-20 | 37.5 | -2.2 | 7.1 |  |
| rlm_quiet | close | 3k+ bets | 1-5 | 16.7 | -21.4 | -59.7 |  |
| rlm_quiet | close | pin $1-2k | 4-8 | 33.3 | -7.9 | -28.9 |  |
| rlm_quiet | close | pin $2k+ | 4-4 | 50.0 | 9.2 | 124.1 |  |
| rlm_quiet | close | pin limit <$1k | 3-2 | 60.0 | 18.0 | 16.4 |  |
| pin_move | close | 1-3k bets | 19-21 | 47.5 | -2.2 | -12.3 |  |
| pin_move | close | 3k+ bets | 4-2 | 66.7 | 21.8 | 32.6 |  |
| pin_move | close | pin $1-2k | 8-12 | 40.0 | -6.9 | -23.5 |  |
| pin_move | close | pin $2k+ | 10-6 | 62.5 | 10.5 | 13.5 |  |
| pin_move | close | pin limit <$1k | 5-5 | 50.0 | 1.5 | -4.0 |  |
| money_delta | close | 1-3k bets | 10-13 | 43.5 | 3.0 | -16.2 |  |
| money_delta | close | 3k+ bets | 4-2 | 66.7 | 22.9 | 37.0 |  |
| money_delta | close | pin $1-2k | 5-6 | 45.5 | 5.9 | -11.7 |  |
| money_delta | close | pin $2k+ | 1-3 | 25.0 | -14.7 | -52.3 |  |
| money_delta | close | pin limit <$1k | 3-1 | 75.0 | 32.2 | 44.5 |  |
| pin_rlm | close | 1-3k bets | 1-5 | 16.7 | -24.8 | -66.7 |  |
| pin_rlm | close | 3k+ bets | 2-0 | 100.0 | 64.4 | 114.6 |  |
| pin_rlm | close | pin $1-2k | 1-2 | 33.3 | -3.3 | -34.9 |  |
| pin_rlm | close | pin $2k+ | 1-1 | 50.0 | 0.0 | 17.0 |  |
| pin_rlm | close | pin limit <$1k | 1-2 | 33.3 | -3.3 | -33.3 |  |
| follow_move | close | 1-3k bets | 32-39 | 45.1 | -3.6 | -2.2 |  |
| follow_move | close | 3k+ bets | 8-7 | 53.3 | 3.6 | -3.4 |  |
| follow_move | close | pin $1-2k | 11-14 | 44.0 | -4.6 | -12.9 |  |
| follow_move | close | pin $2k+ | 14-9 | 60.9 | 12.2 | 53.9 |  |
| follow_move | close | pin limit <$1k | 6-5 | 54.5 | 4.9 | 4.6 |  |
| rlm_ratio | close | 1-3k bets | 4-12 | 25.0 | -12.1 | -51.7 |  |
| rlm_ratio | close | 3k+ bets | 3-2 | 60.0 | 19.3 | 24.0 |  |
| rlm_ratio | close | pin $1-2k | 2-2 | 50.0 | 12.8 | -2.4 |  |
| rlm_ratio | close | pin $2k+ | 1-3 | 25.0 | -11.0 | -41.5 |  |
| rlm_ratio | close | pin limit <$1k | 3-1 | 75.0 | 32.2 | 44.5 |  |
| money_level | close | 1-3k bets | 41-32 | 56.2 | -2.2 | -6.2 |  |
| money_level | close | 3k+ bets | 11-8 | 57.9 | 0.0 | 1.1 |  |
| money_level | close | pin $1-2k | 16-11 | 59.3 | 2.6 | 6.5 |  |
| money_level | close | pin $2k+ | 12-11 | 52.2 | -5.5 | -13.3 |  |
| money_level | close | pin limit <$1k | 5-7 | 41.7 | -13.7 | -20.8 |  |
| sharp_gap | close | 1-3k bets | 22-37 | 37.3 | -11.5 | -31.2 |  |
| sharp_gap | close | 3k+ bets | 8-11 | 42.1 | -6.2 | -19.4 |  |
| sharp_gap | close | pin $1-2k | 9-13 | 40.9 | -8.9 | -22.1 |  |
| sharp_gap | close | pin $2k+ | 6-14 | 30.0 | -19.8 | -46.2 |  |
| sharp_gap | close | pin limit <$1k | 3-5 | 37.5 | -7.2 | -27.8 |  |
| money_moving | close | 1-3k bets | 25-37 | 40.3 | -9.8 | -27.9 |  |
| money_moving | close | 3k+ bets | 8-11 | 42.1 | -6.2 | -19.4 |  |
| money_moving | close | pin $1-2k | 10-12 | 45.5 | -6.0 | -17.0 |  |
| money_moving | close | pin $2k+ | 6-14 | 30.0 | -19.8 | -46.2 |  |
| money_moving | close | pin limit <$1k | 5-6 | 45.5 | -3.7 | -13.1 |  |
| pin_value | close | 1-3k bets | 20-12 | 62.5 | 12.4 | 54.3 |  |
| pin_value | close | 3k+ bets | 2-2 | 50.0 | -3.5 | -4.9 |  |
| pin_value | close | pin $1-2k | 9-7 | 56.2 | 5.8 | 19.7 |  |
| pin_value | close | pin $2k+ | 9-3 | 75.0 | 25.2 | 120.3 |  |
| pin_value | close | pin limit <$1k | 4-4 | 50.0 | -1.7 | -5.0 |  |
| consensus_gap | close | 1-3k bets | 23-16 | 59.0 | 4.2 | 2.2 |  |
| consensus_gap | close | 3k+ bets | 2-2 | 50.0 | -7.2 | -20.4 |  |
| consensus_gap | close | pin $1-2k | 7-4 | 63.6 | 2.9 | 11.6 |  |
| consensus_gap | close | pin $2k+ | 12-4 | 75.0 | 16.3 | 28.2 |  |
| consensus_gap | close | pin limit <$1k | 2-2 | 50.0 | 7.2 | -2.3 |  |
| follow_move+pin_move | close | 1-3k bets | 13-17 | 43.3 | -6.7 | -20.5 |  |
| money_delta+money_moving | close | 1-3k bets | 7-8 | 46.7 | 6.8 | -10.3 |  |
| money_delta+sharp_gap | close | 1-3k bets | 7-7 | 50.0 | 10.1 | -3.9 |  |
| money_moving+sharp_gap | close | 1-3k bets | 21-35 | 37.5 | -11.6 | -31.0 |  |
| consensus_gap+money_level | close | 1-3k bets | 14-10 | 58.3 | -4.6 | -4.6 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 12-20 | 37.5 | -2.2 | 7.1 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 5-8 | 38.5 | -3.8 | -25.2 |  |
| consensus_gap+follow_move | close | 1-3k bets | 8-8 | 50.0 | -2.7 | -11.1 |  |
| follow_move+money_level | close | 1-3k bets | 14-14 | 50.0 | -8.4 | -14.8 |  |
| money_level+money_moving | close | 1-3k bets | 19-21 | 47.5 | -8.2 | -17.0 |  |
| money_level+sharp_gap | close | 1-3k bets | 16-20 | 44.4 | -10.3 | -19.3 |  |
| consensus_gap+money_moving | close | 1-3k bets | 6-12 | 33.3 | -20.8 | -41.0 |  |
| consensus_gap+pin_move | close | 1-3k bets | 5-3 | 62.5 | 10.6 | 13.4 |  |
| consensus_gap+pin_value | close | 1-3k bets | 10-6 | 62.5 | 11.4 | 16.9 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 5-12 | 29.4 | -22.2 | -44.2 |  |
| follow_move+money_moving | close | 1-3k bets | 9-19 | 32.1 | -16.6 | -43.4 |  |
| follow_move+pin_value | close | 1-3k bets | 6-4 | 60.0 | 9.3 | 110.3 |  |
| follow_move+sharp_gap | close | 1-3k bets | 10-20 | 33.3 | -14.3 | -40.8 |  |
| money_level+pin_move | close | 1-3k bets | 9-9 | 50.0 | -5.6 | -10.8 |  |
| money_level+pin_value | close | 1-3k bets | 6-7 | 46.2 | -8.8 | -13.3 |  |
| money_moving+pin_move | close | 1-3k bets | 6-9 | 40.0 | -11.3 | -24.8 |  |
| money_moving+pin_value | close | 1-3k bets | 4-9 | 30.8 | -21.4 | -42.1 |  |
| pin_move+pin_value | close | 1-3k bets | 7-5 | 58.3 | 7.6 | 8.8 |  |
| pin_move+sharp_gap | close | 1-3k bets | 4-10 | 28.6 | -20.0 | -46.4 |  |
| pin_value+sharp_gap | close | 1-3k bets | 3-8 | 27.3 | -23.2 | -49.0 |  |
| follow_move+money_delta | close | 1-3k bets | 6-9 | 40.0 | -0.5 | -22.4 |  |
| money_delta+pin_move | close | 1-3k bets | 3-3 | 50.0 | 12.2 | -1.6 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 4-7 | 36.4 | -2.0 | -29.0 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 4-12 | 25.0 | -12.1 | -51.7 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 2-7 | 22.2 | -12.2 | -56.6 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 4-10 | 28.6 | -9.2 | -44.8 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 2-9 | 18.2 | -15.9 | -64.5 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 2-9 | 18.2 | -15.9 | -64.5 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 4-12 | 25.0 | -12.1 | -51.7 |  |
| money_delta+money_level | close | 1-3k bets | 2-1 | 66.7 | 25.0 | 28.7 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 3-4 | 42.9 | 5.8 | -16.9 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 2-3 | 40.0 | 6.4 | -21.8 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 4-5 | 44.4 | 4.4 | -14.1 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 1-2 | 33.3 | -13.0 | -33.3 |  |
| money_level+pin_rlm | close | 1-3k bets | 0-2 | 0.0 | -53.3 | -100.0 |  |
| money_moving+pin_rlm | close | 1-3k bets | 1-4 | 20.0 | -23.3 | -60.0 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 1-5 | 16.7 | -24.8 | -66.7 |  |
| money_level+rlm_ratio | close | 1-3k bets | 1-2 | 33.3 | -3.3 | -34.9 |  |
| consensus_gap+money_delta | close | 1-3k bets | 2-1 | 66.7 | 32.2 | 30.3 |  |
| follow_move+pin_rlm | close | 1-3k bets | 1-3 | 25.0 | -10.6 | -50.0 |  |
| money_delta+pin_rlm | close | 1-3k bets | 1-1 | 50.0 | 14.4 | 0.0 |  |
| pin_move+pin_rlm | close | 1-3k bets | 1-4 | 20.0 | -16.2 | -60.0 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 1-3 | 25.0 | -10.6 | -50.0 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 1-2 | 33.3 | -1.1 | -33.3 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 1-3 | 25.0 | -10.6 | -50.0 |  |
| money_delta+pin_value | close | 1-3k bets | 2-1 | 66.7 | 20.4 | 26.0 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 3-1 | 75.0 | 34.3 | 285.5 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 2-0 | 100.0 | 50.0 | 88.9 |  |
| pin_rlm+pin_value | close | 1-3k bets | 0-1 | 0.0 | -38.9 | -100.0 |  |
| money_level+money_moving | close | 3k+ bets | 6-6 | 50.0 | -4.9 | -11.7 |  |
| money_level+sharp_gap | close | 3k+ bets | 6-6 | 50.0 | -4.9 | -11.7 |  |
| money_moving+sharp_gap | close | 3k+ bets | 8-11 | 42.1 | -6.2 | -19.4 |  |
| follow_move+money_delta | close | 3k+ bets | 2-2 | 50.0 | 5.6 | -3.5 |  |
| follow_move+money_level | close | 3k+ bets | 5-1 | 83.3 | 21.5 | 30.3 |  |
| follow_move+money_moving | close | 3k+ bets | 5-3 | 62.5 | 15.3 | 13.9 |  |
| follow_move+pin_move | close | 3k+ bets | 3-2 | 60.0 | 16.7 | 19.9 |  |
| follow_move+pin_rlm | close | 3k+ bets | 2-0 | 100.0 | 64.4 | 114.6 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 3-2 | 60.0 | 19.3 | 24.0 |  |
| follow_move+sharp_gap | close | 3k+ bets | 5-3 | 62.5 | 15.3 | 13.9 |  |
| money_delta+money_level | close | 3k+ bets | 2-0 | 100.0 | 50.0 | 93.0 |  |
| money_delta+money_moving | close | 3k+ bets | 3-1 | 75.0 | 32.2 | 56.0 |  |
| money_delta+pin_move | close | 3k+ bets | 1-1 | 50.0 | 11.1 | -2.4 |  |
| money_delta+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 61.1 | 95.2 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 2-1 | 66.7 | 20.4 | 28.7 |  |
| money_delta+sharp_gap | close | 3k+ bets | 3-1 | 75.0 | 32.2 | 56.0 |  |
| money_level+pin_move | close | 3k+ bets | 2-0 | 100.0 | 46.7 | 78.8 |  |
| money_level+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 61.1 | 95.2 |  |
| money_level+rlm_ratio | close | 3k+ bets | 2-0 | 100.0 | 50.0 | 93.0 |  |
| money_moving+pin_move | close | 3k+ bets | 2-1 | 66.7 | 18.2 | 19.2 |  |
| money_moving+pin_rlm | close | 3k+ bets | 2-0 | 100.0 | 64.4 | 114.6 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 3-2 | 60.0 | 19.3 | 24.0 |  |
| pin_move+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 61.1 | 95.2 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 1-0 | 100.0 | 61.1 | 95.2 |  |
| pin_move+sharp_gap | close | 3k+ bets | 2-1 | 66.7 | 18.2 | 19.2 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 2-0 | 100.0 | 64.4 | 114.6 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 2-0 | 100.0 | 64.4 | 114.6 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 3-2 | 60.0 | 19.3 | 24.0 |  |
| consensus_gap+money_level | close | 3k+ bets | 2-1 | 66.7 | 1.1 | 6.1 |  |
| consensus_gap+money_moving | close | 3k+ bets | 1-2 | 33.3 | -22.6 | -57.0 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 1-2 | 33.3 | -22.6 | -57.0 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 1-5 | 16.7 | -21.4 | -59.7 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 1-2 | 33.3 | -3.3 | -19.3 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 0-2 | 0.0 | -38.9 | -100.0 |  |
| money_level+pin_value | close | 3k+ bets | 2-1 | 66.7 | 13.0 | 26.7 |  |
| money_moving+pin_value | close | 3k+ bets | 1-2 | 33.3 | -17.6 | -36.4 |  |
| pin_value+sharp_gap | close | 3k+ bets | 1-2 | 33.3 | -17.6 | -36.4 |  |
| consensus_gap+follow_move | close | 3k+ bets | 1-0 | 100.0 | 32.3 | 29.0 |  |
| consensus_gap+pin_value | close | 3k+ bets | 1-0 | 100.0 | 38.9 | 89.3 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 0-3 | 0.0 | -36.7 | -100.0 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 0-3 | 0.0 | -36.7 | -100.0 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 0-2 | 0.0 | -35.6 | -100.0 |  |
| money_delta+money_moving | close | pin $1-2k | 3-1 | 75.0 | 37.8 | 45.3 |  |
| money_delta+sharp_gap | close | pin $1-2k | 3-1 | 75.0 | 37.8 | 45.3 |  |
| money_moving+sharp_gap | close | pin $1-2k | 9-12 | 42.9 | -7.8 | -18.4 |  |
| consensus_gap+follow_move | close | pin $1-2k | 3-2 | 60.0 | -2.1 | 9.5 |  |
| consensus_gap+money_level | close | pin $1-2k | 5-4 | 55.6 | -8.5 | -6.1 |  |
| consensus_gap+money_moving | close | pin $1-2k | 2-3 | 40.0 | -23.8 | -39.0 |  |
| consensus_gap+pin_move | close | pin $1-2k | 1-1 | 50.0 | -6.9 | -4.5 |  |
| consensus_gap+pin_value | close | pin $1-2k | 3-2 | 60.0 | 5.0 | 13.9 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 1-3 | 25.0 | -37.8 | -52.3 |  |
| follow_move+money_level | close | pin $1-2k | 6-5 | 54.5 | -0.4 | 3.1 |  |
| follow_move+money_moving | close | pin $1-2k | 4-4 | 50.0 | 0.0 | -3.5 |  |
| follow_move+pin_move | close | pin $1-2k | 5-11 | 31.2 | -15.4 | -39.5 |  |
| follow_move+pin_value | close | pin $1-2k | 1-2 | 33.3 | -17.6 | -36.4 |  |
| follow_move+sharp_gap | close | pin $1-2k | 4-5 | 44.4 | -3.6 | -14.2 |  |
| money_level+money_moving | close | pin $1-2k | 9-8 | 52.9 | -1.3 | -3.8 |  |
| money_level+pin_move | close | pin $1-2k | 4-4 | 50.0 | -2.8 | -4.3 |  |
| money_level+pin_value | close | pin $1-2k | 4-3 | 57.1 | 1.2 | 7.0 |  |
| money_level+sharp_gap | close | pin $1-2k | 8-8 | 50.0 | -3.4 | -4.9 |  |
| money_moving+pin_move | close | pin $1-2k | 3-4 | 42.9 | -6.7 | -18.7 |  |
| money_moving+pin_value | close | pin $1-2k | 2-4 | 33.3 | -20.4 | -37.6 |  |
| pin_move+pin_value | close | pin $1-2k | 3-2 | 60.0 | 9.4 | 11.5 |  |
| pin_move+sharp_gap | close | pin $1-2k | 3-5 | 37.5 | -9.9 | -28.8 |  |
| pin_value+sharp_gap | close | pin $1-2k | 2-4 | 33.3 | -20.4 | -37.6 |  |
| follow_move+money_delta | close | pin $1-2k | 4-5 | 44.4 | 4.0 | -13.2 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 4-8 | 33.3 | -7.9 | -28.9 |  |
| money_delta+pin_move | close | pin $1-2k | 3-3 | 50.0 | 11.1 | -2.4 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 2-5 | 28.6 | -12.3 | -44.2 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 3-6 | 33.3 | -7.9 | -35.4 |  |
| follow_move+pin_rlm | close | pin $1-2k | 1-2 | 33.3 | -3.3 | -34.9 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 2-2 | 50.0 | 12.8 | -2.4 |  |
| pin_move+pin_rlm | close | pin $1-2k | 1-2 | 33.3 | -3.3 | -34.9 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 1-2 | 33.3 | -3.3 | -34.9 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 0-2 | 0.0 | -35.6 | -100.0 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 1-2 | 33.3 | -3.3 | -34.9 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 1-2 | 33.3 | -3.3 | -34.9 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 0-2 | 0.0 | -35.6 | -100.0 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 0-2 | 0.0 | -35.6 | -100.0 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 2-2 | 50.0 | 12.8 | -2.4 |  |
| money_delta+money_level | close | pin $1-2k | 2-0 | 100.0 | 61.1 | 95.2 |  |
| money_delta+pin_rlm | close | pin $1-2k | 1-0 | 100.0 | 61.1 | 95.2 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 2-0 | 100.0 | 61.1 | 95.2 |  |
| money_level+pin_rlm | close | pin $1-2k | 1-0 | 100.0 | 61.1 | 95.2 |  |
| money_level+rlm_ratio | close | pin $1-2k | 2-0 | 100.0 | 61.1 | 95.2 |  |
| money_moving+pin_rlm | close | pin $1-2k | 1-1 | 50.0 | 11.1 | -2.4 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 2-1 | 66.7 | 27.8 | 30.1 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 0-1 | 0.0 | -38.9 | -100.0 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 1-0 | 100.0 | 47.2 | 90.9 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 1-1 | 50.0 | 4.2 | -4.5 |  |
| money_delta+pin_value | close | pin $1-2k | 0-1 | 0.0 | -38.9 | -100.0 |  |
| follow_move+pin_move | close | pin $2k+ | 8-5 | 61.5 | 8.8 | 10.5 |  |
| consensus_gap+money_level | close | pin $2k+ | 7-4 | 63.6 | 1.6 | 2.5 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 4-4 | 50.0 | 9.2 | 124.1 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 1-3 | 25.0 | -14.0 | -39.5 |  |
| money_level+money_moving | close | pin $2k+ | 5-9 | 35.7 | -18.6 | -39.8 |  |
| money_level+sharp_gap | close | pin $2k+ | 5-9 | 35.7 | -18.6 | -39.8 |  |
| money_moving+sharp_gap | close | pin $2k+ | 6-14 | 30.0 | -19.8 | -46.2 |  |
| consensus_gap+pin_value | close | pin $2k+ | 7-2 | 77.8 | 26.1 | 44.5 |  |
| follow_move+money_level | close | pin $2k+ | 5-3 | 62.5 | 2.9 | -5.2 |  |
| follow_move+money_moving | close | pin $2k+ | 4-6 | 40.0 | -9.2 | -29.9 |  |
| follow_move+sharp_gap | close | pin $2k+ | 4-6 | 40.0 | -9.2 | -29.9 |  |
| money_level+pin_move | close | pin $2k+ | 4-2 | 66.7 | 4.8 | 4.8 |  |
| money_moving+pin_move | close | pin $2k+ | 2-3 | 40.0 | -14.9 | -32.3 |  |
| pin_move+sharp_gap | close | pin $2k+ | 2-3 | 40.0 | -14.9 | -32.3 |  |
| money_delta+money_level | close | pin $2k+ | 1-0 | 100.0 | 52.8 | 90.9 |  |
| money_delta+money_moving | close | pin $2k+ | 1-3 | 25.0 | -14.7 | -52.3 |  |
| money_delta+sharp_gap | close | pin $2k+ | 1-3 | 25.0 | -14.7 | -52.3 |  |
| consensus_gap+money_moving | close | pin $2k+ | 2-4 | 33.3 | -27.6 | -49.2 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 2-4 | 33.3 | -27.6 | -49.2 |  |
| money_level+pin_value | close | pin $2k+ | 2-2 | 50.0 | -2.1 | -5.8 |  |
| money_moving+pin_value | close | pin $2k+ | 0-3 | 0.0 | -49.1 | -100.0 |  |
| pin_value+sharp_gap | close | pin $2k+ | 0-3 | 0.0 | -49.1 | -100.0 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -67.7 | -100.0 |  |
| money_level+pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -67.7 | -100.0 |  |
| money_moving+pin_rlm | close | pin $2k+ | 1-1 | 50.0 | 0.0 | 17.0 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 1-1 | 50.0 | 0.0 | 17.0 |  |
| follow_move+money_delta | close | pin $2k+ | 0-2 | 0.0 | -39.7 | -100.0 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 1-3 | 25.0 | -11.0 | -41.5 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 0-2 | 0.0 | -39.7 | -100.0 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 1-3 | 25.0 | -11.0 | -41.5 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 1-3 | 25.0 | -11.0 | -41.5 |  |
| money_level+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -32.3 | -100.0 |  |
| consensus_gap+follow_move | close | pin $2k+ | 3-0 | 100.0 | 32.3 | 53.9 |  |
| consensus_gap+pin_move | close | pin $2k+ | 3-1 | 75.0 | 17.5 | 29.0 |  |
| follow_move+pin_value | close | pin $2k+ | 2-0 | 100.0 | 60.3 | 571.6 |  |
| pin_move+pin_value | close | pin $2k+ | 2-1 | 66.7 | 19.4 | 22.2 |  |
| follow_move+pin_rlm | close | pin $2k+ | 1-0 | 100.0 | 67.7 | 134.0 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 1-0 | 100.0 | 67.7 | 134.0 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 1-0 | 100.0 | 67.7 | 1060.0 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 0-2 | 0.0 | -35.6 | -100.0 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 0-2 | 0.0 | -35.6 | -100.0 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 0-1 | 0.0 | -32.3 | -100.0 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -32.3 | -100.0 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 2-1 | 66.7 | 22.6 | 30.3 |  |
| consensus_gap+money_level | close | pin limit <$1k | 0-1 | 0.0 | -61.1 | -100.0 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 2-2 | 50.0 | 7.2 | -2.3 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 1-2 | 33.3 | -13.0 | -36.4 |  |
| follow_move+money_level | close | pin limit <$1k | 2-3 | 40.0 | -15.0 | -23.6 |  |
| follow_move+money_moving | close | pin limit <$1k | 3-3 | 50.0 | 1.1 | -3.7 |  |
| follow_move+pin_value | close | pin limit <$1k | 3-2 | 60.0 | 5.0 | 13.8 |  |
| money_level+money_moving | close | pin limit <$1k | 2-4 | 33.3 | -20.4 | -37.0 |  |
| money_level+pin_value | close | pin limit <$1k | 2-3 | 40.0 | -15.0 | -23.6 |  |
| money_moving+pin_value | close | pin limit <$1k | 3-4 | 42.9 | -8.7 | -18.7 |  |
| follow_move+pin_move | close | pin limit <$1k | 3-3 | 50.0 | 2.5 | -3.0 |  |
| money_level+pin_move | close | pin limit <$1k | 3-3 | 50.0 | -2.3 | -5.2 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 3-5 | 37.5 | -7.2 | -27.8 |  |
| pin_move+pin_value | close | pin limit <$1k | 2-2 | 50.0 | -3.5 | -4.5 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 3-2 | 60.0 | 18.0 | 16.4 |  |
| money_moving+pin_move | close | pin limit <$1k | 3-3 | 50.0 | 1.1 | -3.7 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 2-0 | 100.0 | 64.4 | 95.5 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 14.4 | 0.0 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 1-1 | 50.0 | 14.4 | 0.0 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 2-0 | 100.0 | 64.4 | 95.5 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 2-0 | 100.0 | 64.4 | 95.5 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 2-1 | 66.7 | 30.0 | 30.3 |  |
| follow_move+money_delta | close | pin limit <$1k | 3-1 | 75.0 | 32.2 | 44.5 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 1-1 | 50.0 | 14.4 | 0.0 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 3-1 | 75.0 | 32.2 | 44.5 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 3-2 | 60.0 | 13.5 | 15.6 |  |
| money_delta+money_moving | close | pin limit <$1k | 3-1 | 75.0 | 32.2 | 44.5 |  |
| money_delta+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 14.4 | 0.0 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 1-1 | 50.0 | 14.4 | 0.0 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 2-0 | 100.0 | 64.4 | 95.5 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 3-1 | 75.0 | 32.2 | 44.5 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 3-1 | 75.0 | 32.2 | 44.5 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 1-2 | 33.3 | -3.3 | -33.3 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 2-0 | 100.0 | 64.4 | 95.5 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 3-1 | 75.0 | 32.2 | 44.5 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 1-2 | 33.3 | -3.3 | -33.3 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 2-1 | 66.7 | 22.6 | 30.3 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 1-1 | 50.0 | 14.4 | 0.0 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 1-3 | 25.0 | -17.8 | -50.0 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 1-0 | 100.0 | 67.7 | 100.0 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 1-1 | 50.0 | 14.4 | 0.0 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 1-2 | 33.3 | -3.3 | -33.3 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 2-0 | 100.0 | 64.4 | 95.5 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 2-0 | 100.0 | 64.4 | 95.5 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 3-1 | 75.0 | 32.2 | 44.5 |  |
| money_delta+pin_value | close | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 1-0 | 100.0 | 61.1 | 90.9 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 2-3 | 40.0 | -7.8 | -24.4 |  |
| money_level+sharp_gap | close | pin limit <$1k | 0-3 | 0.0 | -46.3 | -100.0 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 0-1 | 0.0 | -38.9 | -100.0 |  |
| money_delta+money_level | close | pin limit <$1k | 0-1 | 0.0 | -38.9 | -100.0 |  |
| money_level+pin_rlm | close | pin limit <$1k | 0-1 | 0.0 | -38.9 | -100.0 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 0-1 | 0.0 | -38.9 | -100.0 |  |
| rlm_quiet | early | <1k bets | 3-4 | 42.9 | 7.8 | -4.3 | -1.27 |
| follow_move | early | <1k bets | 12-15 | 44.4 | -2.8 | -6.6 | -0.71 |
| follow_move | early | pin $1-2k | 1-0 | 100.0 | 67.7 | 142.0 | 0.0 |
| rlm_ratio | early | <1k bets | 2-3 | 40.0 | -0.3 | -23.6 | -0.06 |
| money_level | early | <1k bets | 9-7 | 56.2 | -7.2 | -9.7 | 1.07 |
| sharp_gap | early | <1k bets | 6-6 | 50.0 | 2.5 | -8.4 | 0.52 |
| money_moving | early | <1k bets | 7-4 | 63.6 | 10.2 | 18.8 | 1.12 |
| pin_value | early | <1k bets | 0-1 | 0.0 | -47.2 | -100.0 | 0.0 |
| pin_value | early | pin $1-2k | 0-1 | 0.0 | -47.2 | -100.0 | 0.0 |
| consensus_gap | early | <1k bets | 8-3 | 72.7 | 16.4 | 21.2 | 0.85 |
| follow_move+money_level | early | <1k bets | 2-3 | 40.0 | -20.8 | -39.6 | 0.36 |
| follow_move+sharp_gap | early | <1k bets | 3-4 | 42.9 | -3.4 | -18.2 | -0.19 |
| money_level+sharp_gap | early | <1k bets | 3-2 | 60.0 | -2.1 | 5.3 | 1.9 |
| follow_move+money_moving | early | <1k bets | 4-3 | 57.1 | 6.7 | 11.6 | 0.4 |
| money_level+money_moving | early | <1k bets | 4-3 | 57.1 | -5.6 | -8.9 | 1.61 |
| consensus_gap+money_level | early | <1k bets | 3-1 | 75.0 | 7.3 | -0.5 | 1.17 |
| follow_move+rlm_quiet | early | <1k bets | 3-4 | 42.9 | 7.8 | -4.3 | -1.27 |
| follow_move+rlm_ratio | early | <1k bets | 2-3 | 40.0 | -0.3 | -23.6 | -0.06 |
| rlm_quiet+rlm_ratio | early | <1k bets | 2-2 | 50.0 | 12.8 | -4.5 | -1.32 |
| rlm_quiet+sharp_gap | early | <1k bets | 2-2 | 50.0 | 12.8 | -4.5 | -1.32 |
| rlm_ratio+sharp_gap | early | <1k bets | 2-3 | 40.0 | -0.3 | -23.6 | -0.06 |
| consensus_gap+follow_move | early | <1k bets | 2-1 | 66.7 | 8.5 | 0.7 | -0.83 |
| money_moving+rlm_quiet | early | <1k bets | 3-0 | 100.0 | 63.3 | 123.3 | 0.33 |
| money_moving+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 23.1 | 27.3 | 1.33 |
| money_moving+sharp_gap | early | <1k bets | 4-2 | 66.7 | 12.1 | 19.6 | 1.42 |
| consensus_gap+money_moving | early | <1k bets | 2-0 | 100.0 | 32.3 | 42.0 | 0.15 |
| consensus_gap+sharp_gap | early | <1k bets | 1-0 | 100.0 | 32.3 | 73.0 | 2.5 |
| money_level+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -52.8 | -100.0 | 5.0 |
