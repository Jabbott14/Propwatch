# CBB scorecard

Generated 2026-11-21 19:49 UTC. 724 graded games (33 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**685 games before 2026-11-21 (fit) · 39 on or after it (forward).**

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
sample ran **47.9% favourites** (n=723) and **50.4% overs** (n=724) and **73.2% moneyline favourites** (n=616).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-21. Nothing in the engine was chosen using these. n=39 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 3-4 | 42.9 | 32.7 | 10.2 | -0.3 | -4.3 | -1.27 | 28.6 | keep collecting (7/30) |
| follow_move | both | 12-23 | 34.3 | 45.9 | -11.6 | -9.78 | -27.9 | -0.17 | 28.6 | DROP: below break-even |
| rlm_ratio | both | 2-3 | 40.0 | 38.4 | 1.6 | -1.18 | -23.6 | -0.06 | 40.0 | keep collecting (5/30) |
| money_level | both | 9-7 | 56.2 | 65.9 | -9.7 | -1.56 | -9.7 | 1.07 | 50.0 | keep collecting (16/30) |
| sharp_gap | both | 6-6 | 50.0 | 46.8 | 3.2 | -1.01 | -8.4 | 0.52 | 41.7 | keep collecting (12/30) |
| money_moving | both | 7-4 | 63.6 | 53.9 | 9.7 | +2.07 | 18.8 | 1.12 | 54.5 | keep collecting (11/30) |
| pin_value | both | 0-1 | 0.0 | 46.2 | -46.2 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap | both | 12-3 | 80.0 | 57.8 | 22.2 | +5.79 | 38.6 | 0.87 | 60.0 | keep collecting (15/30) |
| follow_move+money_level | both | 2-3 | 40.0 | 63.2 | -23.2 | -1.98 | -39.6 | 0.36 | 20.0 | keep collecting (5/30) |
| follow_move+sharp_gap | both | 3-4 | 42.9 | 45.7 | -2.9 | -1.27 | -18.2 | -0.19 | 28.6 | keep collecting (7/30) |
| money_level+sharp_gap | both | 3-2 | 60.0 | 64.3 | -4.3 | +0.26 | 5.3 | 1.9 | 60.0 | keep collecting (5/30) |
| follow_move+money_moving | both | 4-3 | 57.1 | 50.5 | 6.6 | +0.81 | 11.6 | 0.4 | 42.9 | keep collecting (7/30) |
| money_level+money_moving | both | 4-3 | 57.1 | 65.0 | -7.9 | -0.62 | -8.9 | 1.61 | 57.1 | keep collecting (7/30) |
| consensus_gap+money_level | both | 3-1 | 75.0 | 69.7 | 5.3 | -0.02 | -0.5 | 1.17 | 75.0 | keep collecting (4/30) |
| follow_move+rlm_quiet | both | 3-4 | 42.9 | 32.7 | 10.2 | -0.3 | -4.3 | -1.27 | 28.6 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 2-3 | 40.0 | 38.4 | 1.6 | -1.18 | -23.6 | -0.06 | 40.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | both | 2-2 | 50.0 | 34.5 | 15.5 | -0.18 | -4.5 | -1.32 | 25.0 | keep collecting (4/30) |
| rlm_quiet+sharp_gap | both | 2-2 | 50.0 | 34.5 | 15.5 | -0.18 | -4.5 | -1.32 | 25.0 | keep collecting (4/30) |
| rlm_ratio+sharp_gap | both | 2-3 | 40.0 | 38.4 | 1.6 | -1.18 | -23.6 | -0.06 | 40.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 2-1 | 66.7 | 58.4 | 8.2 | +0.02 | 0.7 | -0.83 | 33.3 | keep collecting (3/30) |
| money_moving+rlm_quiet | both | 3-0 | 100.0 | 34.0 | 66.0 | +3.7 | 123.3 | 0.33 | 66.7 | keep collecting (3/30) |
| money_moving+rlm_ratio | both | 2-1 | 66.7 | 41.9 | 24.8 | +0.82 | 27.3 | 1.33 | 66.7 | keep collecting (3/30) |
| money_moving+sharp_gap | both | 4-2 | 66.7 | 54.9 | 11.8 | +1.17 | 19.6 | 1.42 | 66.7 | keep collecting (6/30) |
| consensus_gap+money_moving | both | 2-0 | 100.0 | 69.7 | 30.3 | +0.84 | 42.0 | 0.15 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | both | 1-0 | 100.0 | 69.7 | 30.3 | +0.73 | 73.0 | 2.5 | 100.0 | keep collecting (1/30) |
| money_level+rlm_ratio | both | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 1-3 | 25.0 | 30.3 | -5.3 | -1.12 | -28.0 | -0.97 | 25.0 | keep collecting (4/30) |
| rlm_quiet | total | 2-1 | 66.7 | 35.9 | 30.8 | +0.82 | 27.3 | -1.67 | 33.3 | keep collecting (3/30) |
| follow_move | moneyline | 6-5 | 54.5 | 41.0 | 13.5 | +2.76 | 25.1 | -1.19 | 27.3 | keep collecting (11/30) |
| follow_move | spread | 1-9 | 10.0 | 53.8 | -43.8 | -8.09 | -80.9 | 0.3 | 20.0 | keep collecting (10/30) |
| follow_move | total | 5-9 | 35.7 | 44.0 | -8.2 | -4.46 | -31.8 | 0.29 | 35.7 | keep collecting (14/30) |
| rlm_ratio | moneyline | 0-1 | 0.0 | 30.3 | -30.3 | -1.0 | -100.0 | -0.3 | 0.0 | keep collecting (1/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| rlm_ratio | total | 2-1 | 66.7 | 35.9 | 30.8 | +0.82 | 27.3 | -1.67 | 33.3 | keep collecting (3/30) |
| money_level | moneyline | 5-2 | 71.4 | 69.7 | 1.7 | -0.19 | -2.8 | 0.89 | 57.1 | keep collecting (7/30) |
| money_level | spread | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level | total | 4-4 | 50.0 | 64.1 | -14.1 | -0.36 | -4.5 | 0.75 | 37.5 | keep collecting (8/30) |
| sharp_gap | moneyline | 2-2 | 50.0 | 50.0 | 0.0 | -0.65 | -16.1 | 1.8 | 75.0 | keep collecting (4/30) |
| sharp_gap | spread | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| sharp_gap | total | 4-3 | 57.1 | 44.0 | 13.2 | +0.64 | 9.1 | -0.86 | 14.3 | keep collecting (7/30) |
| money_moving | moneyline | 4-0 | 100.0 | 59.8 | 40.2 | +3.35 | 83.7 | 1.32 | 75.0 | keep collecting (4/30) |
| money_moving | spread | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.27 | -4.5 | 0.33 | 33.3 | keep collecting (6/30) |
| pin_value | spread | 0-1 | 0.0 | 46.2 | -46.2 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap | moneyline | 4-2 | 66.7 | 69.7 | -3.0 | -0.22 | -3.7 | -0.15 | 50.0 | keep collecting (6/30) |
| consensus_gap | spread | 4-0 | 100.0 | 46.2 | 53.8 | +3.45 | 86.3 | 1.0 | 50.0 | keep collecting (4/30) |
| consensus_gap | total | 4-1 | 80.0 | 52.8 | 27.2 | +2.56 | 51.2 | 2.0 | 80.0 | keep collecting (5/30) |
| consensus_gap+money_level | moneyline | 3-1 | 75.0 | 69.7 | 5.3 | -0.02 | -0.5 | 1.17 | 75.0 | keep collecting (4/30) |
| follow_move+rlm_quiet | moneyline | 1-3 | 25.0 | 30.3 | -5.3 | -1.12 | -28.0 | -0.97 | 25.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 0-1 | 0.0 | 30.3 | -30.3 | -1.0 | -100.0 | -0.3 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 0-1 | 0.0 | 30.3 | -30.3 | -1.0 | -100.0 | -0.3 | 0.0 | keep collecting (1/30) |
| rlm_quiet+rlm_ratio | moneyline | 0-1 | 0.0 | 30.3 | -30.3 | -1.0 | -100.0 | -0.3 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+sharp_gap | moneyline | 0-1 | 0.0 | 30.3 | -30.3 | -1.0 | -100.0 | -0.3 | 0.0 | keep collecting (1/30) |
| rlm_ratio+sharp_gap | moneyline | 0-1 | 0.0 | 30.3 | -30.3 | -1.0 | -100.0 | -0.3 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 1-1 | 50.0 | 69.7 | -19.7 | -0.89 | -44.5 | -2.75 | 0.0 | keep collecting (2/30) |
| consensus_gap+money_moving | moneyline | 2-0 | 100.0 | 69.7 | 30.3 | +0.84 | 42.0 | 0.15 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 1-0 | 100.0 | 69.7 | 30.3 | +0.73 | 73.0 | 2.5 | 100.0 | keep collecting (1/30) |
| money_level+money_moving | moneyline | 3-0 | 100.0 | 69.7 | 30.3 | +1.47 | 48.9 | 1.1 | 66.7 | keep collecting (3/30) |
| money_level+sharp_gap | moneyline | 2-0 | 100.0 | 69.7 | 30.3 | +1.35 | 67.8 | 2.75 | 100.0 | keep collecting (2/30) |
| money_moving+sharp_gap | moneyline | 2-0 | 100.0 | 69.7 | 30.3 | +1.35 | 67.8 | 2.75 | 100.0 | keep collecting (2/30) |
| follow_move+money_level | moneyline | 1-0 | 100.0 | 69.7 | 30.3 | +0.11 | 11.1 | -2.2 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.99 | 99.5 | -0.1 | 50.0 | keep collecting (2/30) |
| money_moving+rlm_quiet | moneyline | 1-0 | 100.0 | 30.3 | 69.7 | +1.88 | 188.0 | 2.0 | 100.0 | keep collecting (1/30) |
| follow_move+money_level | spread | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| follow_move+money_moving | spread | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to sharp_gap alone, not independent confirmation |
| money_level+money_moving | spread | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+rlm_ratio | spread | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+sharp_gap | spread | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| money_moving+sharp_gap | spread | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | total | 1-2 | 33.3 | 64.1 | -30.8 | -1.09 | -36.4 | -0.33 | 0.0 | keep collecting (3/30) |
| follow_move+sharp_gap | total | 3-2 | 60.0 | 47.2 | 12.8 | +0.73 | 14.5 | -1.2 | 20.0 | keep collecting (5/30) |
| money_level+sharp_gap | total | 1-1 | 50.0 | 64.1 | -14.1 | -0.09 | -4.5 | -0.5 | 0.0 | keep collecting (2/30) |
| follow_move+money_moving | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.18 | -4.5 | -0.5 | 25.0 | keep collecting (4/30) |
| money_level+money_moving | total | 1-2 | 33.3 | 64.1 | -30.8 | -1.09 | -36.4 | 1.0 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | total | 2-1 | 66.7 | 35.9 | 30.8 | +0.82 | 27.3 | -1.67 | 33.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 2-1 | 66.7 | 35.9 | 30.8 | +0.82 | 27.3 | -1.67 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 2-1 | 66.7 | 35.9 | 30.8 | +0.82 | 27.3 | -1.67 | 33.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | total | 2-1 | 66.7 | 35.9 | 30.8 | +0.82 | 27.3 | -1.67 | 33.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_ratio+sharp_gap | total | 2-1 | 66.7 | 35.9 | 30.8 | +0.82 | 27.3 | -1.67 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | total | 2-0 | 100.0 | 35.9 | 64.1 | +1.82 | 90.9 | -0.5 | 50.0 | keep collecting (2/30) |
| money_moving+rlm_ratio | total | 2-0 | 100.0 | 35.9 | 64.1 | +1.82 | 90.9 | -0.5 | 50.0 | keep collecting (2/30) |
| money_moving+sharp_gap | total | 2-1 | 66.7 | 45.3 | 21.4 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| consensus_gap+follow_move | total | 1-0 | 100.0 | 35.9 | 64.1 | +0.91 | 90.9 | 3.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 13-28 | 31.7 | 37.4 | -5.7 | -4.31 | -10.5 |  |  | DROP: below break-even |
| pin_move | both | 24-26 | 48.0 | 48.4 | -0.4 | -5.04 | -10.1 |  |  | no edge shown yet |
| money_delta | both | 14-17 | 45.2 | 39.1 | 6.0 | -3.51 | -11.3 |  |  | no edge shown yet |
| pin_rlm | both | 3-6 | 33.3 | 37.8 | -4.5 | -2.71 | -30.1 |  |  | keep collecting (9/30) |
| follow_move | both | 43-51 | 45.7 | 48.8 | -3.0 | -4.95 | -5.3 |  |  | no edge shown yet |
| rlm_ratio | both | 7-15 | 31.8 | 36.1 | -4.3 | -8.07 | -36.7 |  |  | keep collecting (22/30) |
| money_level | both | 57-40 | 58.8 | 59.9 | -1.2 | -0.48 | -0.5 |  |  | no edge shown yet |
| sharp_gap | both | 35-49 | 41.7 | 49.3 | -7.6 | -19.23 | -22.9 |  |  | DROP: below break-even |
| money_moving | both | 38-49 | 43.7 | 50.4 | -6.7 | -18.09 | -20.8 |  |  | DROP: below break-even |
| pin_value | both | 26-16 | 61.9 | 51.2 | 10.7 | +18.67 | 44.5 |  |  | no edge shown yet |
| consensus_gap | both | 27-20 | 57.4 | 55.5 | 1.9 | -0.21 | -0.4 |  |  | no edge shown yet |
| follow_move+pin_move | both | 17-22 | 43.6 | 48.3 | -4.7 | -7.24 | -18.6 |  |  | no edge shown yet |
| money_delta+money_moving | both | 10-9 | 52.6 | 38.7 | 13.9 | +0.7 | 3.7 |  |  | keep collecting (19/30) |
| money_delta+sharp_gap | both | 10-8 | 55.6 | 38.9 | 16.7 | +1.7 | 9.4 |  |  | keep collecting (18/30) |
| money_moving+sharp_gap | both | 34-47 | 42.0 | 49.6 | -7.6 | -18.14 | -22.4 |  |  | DROP: below break-even |
| consensus_gap+money_level | both | 18-11 | 62.1 | 65.2 | -3.1 | +0.83 | 2.9 |  |  | keep collecting (29/30) |
| follow_move+rlm_quiet | both | 13-28 | 31.7 | 37.4 | -5.7 | -4.31 | -10.5 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | both | 6-12 | 33.3 | 38.9 | -5.6 | -5.86 | -32.5 |  |  | keep collecting (18/30) |
| consensus_gap+follow_move | both | 10-10 | 50.0 | 53.5 | -3.5 | -2.61 | -13.1 |  |  | keep collecting (20/30) |
| follow_move+money_level | both | 21-15 | 58.3 | 60.9 | -2.5 | -1.13 | -3.1 |  |  | no edge shown yet |
| money_level+money_moving | both | 29-27 | 51.8 | 57.2 | -5.4 | -5.22 | -9.3 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 26-26 | 50.0 | 56.5 | -6.5 | -5.37 | -10.3 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 8-14 | 36.4 | 55.5 | -19.2 | -8.22 | -37.3 |  |  | keep collecting (22/30) |
| consensus_gap+pin_move | both | 5-5 | 50.0 | 50.0 | 0.0 | -0.93 | -9.3 |  |  | keep collecting (10/30) |
| consensus_gap+pin_value | both | 13-7 | 65.0 | 53.2 | 11.8 | +4.35 | 21.8 |  |  | keep collecting (20/30) |
| consensus_gap+sharp_gap | both | 7-14 | 33.3 | 53.3 | -19.9 | -8.36 | -39.8 |  |  | keep collecting (21/30) |
| follow_move+money_moving | both | 17-23 | 42.5 | 49.1 | -6.6 | -9.91 | -24.8 |  |  | no edge shown yet |
| follow_move+pin_value | both | 8-6 | 57.1 | 51.4 | 5.7 | +10.81 | 77.2 |  |  | keep collecting (14/30) |
| follow_move+sharp_gap | both | 18-24 | 42.9 | 48.2 | -5.3 | -10.0 | -23.8 |  |  | no edge shown yet |
| money_level+pin_move | both | 11-9 | 55.0 | 56.2 | -1.2 | -0.37 | -1.8 |  |  | keep collecting (20/30) |
| money_level+pin_value | both | 10-8 | 55.6 | 56.8 | -1.3 | +0.82 | 4.6 |  |  | keep collecting (18/30) |
| money_moving+pin_move | both | 9-11 | 45.0 | 50.3 | -5.3 | -3.24 | -16.2 |  |  | keep collecting (20/30) |
| money_moving+pin_value | both | 7-11 | 38.9 | 53.1 | -14.2 | -4.79 | -26.6 |  |  | keep collecting (18/30) |
| pin_move+pin_value | both | 8-6 | 57.1 | 51.3 | 5.9 | +0.97 | 6.9 |  |  | keep collecting (14/30) |
| pin_move+sharp_gap | both | 7-12 | 36.8 | 47.8 | -10.9 | -6.01 | -31.7 |  |  | keep collecting (19/30) |
| pin_value+sharp_gap | both | 6-10 | 37.5 | 51.8 | -14.3 | -4.7 | -29.4 |  |  | keep collecting (16/30) |
| follow_move+money_delta | both | 8-12 | 40.0 | 39.3 | 0.7 | -4.5 | -22.5 |  |  | keep collecting (20/30) |
| money_delta+pin_move | both | 4-4 | 50.0 | 35.2 | 14.8 | -0.14 | -1.8 |  |  | keep collecting (8/30) |
| money_delta+rlm_quiet | both | 4-10 | 28.6 | 36.0 | -7.4 | -6.19 | -44.2 |  |  | keep collecting (14/30) |
| follow_move+rlm_ratio | both | 7-15 | 31.8 | 36.1 | -4.3 | -8.07 | -36.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | both | 2-11 | 15.4 | 32.9 | -17.5 | -9.09 | -69.9 |  |  | keep collecting (13/30) |
| money_moving+rlm_ratio | both | 7-13 | 35.0 | 36.7 | -1.7 | -6.07 | -30.3 |  |  | keep collecting (20/30) |
| rlm_quiet+rlm_ratio | both | 2-12 | 14.3 | 32.3 | -18.0 | -10.09 | -72.1 |  |  | keep collecting (14/30) |
| rlm_quiet+sharp_gap | both | 2-13 | 13.3 | 32.5 | -19.2 | -11.09 | -73.9 |  |  | keep collecting (15/30) |
| rlm_ratio+sharp_gap | both | 7-15 | 31.8 | 36.1 | -4.3 | -8.07 | -36.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | both | 4-1 | 80.0 | 43.6 | 36.4 | +2.72 | 54.4 |  |  | keep collecting (5/30) |
| consensus_gap+rlm_quiet | both | 3-5 | 37.5 | 34.6 | 2.9 | -2.18 | -27.3 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_ratio | both | 2-3 | 40.0 | 31.4 | 8.6 | -1.09 | -21.8 |  |  | keep collecting (5/30) |
| money_delta+rlm_ratio | both | 6-6 | 50.0 | 40.1 | 9.9 | -0.41 | -3.4 |  |  | keep collecting (12/30) |
| consensus_gap+pin_rlm | both | 1-2 | 33.3 | 45.3 | -12.0 | -1.0 | -33.3 |  |  | keep collecting (3/30) |
| money_level+pin_rlm | both | 1-2 | 33.3 | 47.2 | -13.8 | -1.05 | -34.9 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | both | 3-5 | 37.5 | 38.7 | -1.2 | -1.71 | -21.4 |  |  | keep collecting (8/30) |
| pin_rlm+sharp_gap | both | 3-6 | 33.3 | 37.8 | -4.5 | -2.71 | -30.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | both | 3-2 | 60.0 | 40.4 | 19.6 | +0.81 | 16.3 |  |  | keep collecting (5/30) |
| consensus_gap+money_delta | both | 2-1 | 66.7 | 32.2 | 34.5 | +0.91 | 30.3 |  |  | keep collecting (3/30) |
| follow_move+pin_rlm | both | 3-4 | 42.9 | 33.5 | 9.4 | -0.71 | -10.1 |  |  | keep collecting (7/30) |
| money_delta+pin_rlm | both | 2-1 | 66.7 | 34.0 | 32.6 | +0.95 | 31.7 |  |  | keep collecting (3/30) |
| pin_move+pin_rlm | both | 2-5 | 28.6 | 34.3 | -5.7 | -3.05 | -43.5 |  |  | keep collecting (7/30) |
| pin_move+rlm_ratio | both | 2-4 | 33.3 | 34.0 | -0.7 | -2.05 | -34.1 |  |  | keep collecting (6/30) |
| pin_rlm+rlm_quiet | both | 1-3 | 25.0 | 33.1 | -8.1 | -2.0 | -50.0 |  |  | keep collecting (4/30) |
| pin_rlm+rlm_ratio | both | 3-4 | 42.9 | 33.5 | 9.4 | -0.71 | -10.1 |  |  | keep collecting (7/30) |
| money_delta+pin_value | both | 2-2 | 50.0 | 42.9 | 7.1 | -0.22 | -5.5 |  |  | keep collecting (4/30) |
| pin_value+rlm_quiet | both | 3-2 | 60.0 | 38.4 | 21.6 | +10.42 | 208.4 |  |  | keep collecting (5/30) |
| pin_value+rlm_ratio | both | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 |  |  | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 35.9 | -35.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 5-10 | 33.3 | 30.3 | 3.0 | +6.24 | 41.6 |  |  | keep collecting (15/30) |
| rlm_quiet | spread | 3-4 | 42.9 | 52.7 | -9.9 | -1.19 | -16.9 |  |  | keep collecting (7/30) |
| rlm_quiet | total | 5-14 | 26.3 | 37.4 | -11.1 | -9.37 | -49.3 |  |  | keep collecting (19/30) |
| pin_move | moneyline | 6-3 | 66.7 | 47.8 | 18.9 | +1.71 | 19.0 |  |  | keep collecting (9/30) |
| pin_move | spread | 11-9 | 55.0 | 51.9 | 3.1 | +0.8 | 4.0 |  |  | keep collecting (20/30) |
| pin_move | total | 7-14 | 33.3 | 45.3 | -12.0 | -7.55 | -35.9 |  |  | keep collecting (21/30) |
| money_delta | moneyline | 2-4 | 33.3 | 30.3 | 3.0 | -1.62 | -27.0 |  |  | keep collecting (6/30) |
| money_delta | spread | 3-3 | 50.0 | 48.7 | 1.3 | -0.2 | -3.4 |  |  | keep collecting (6/30) |
| money_delta | total | 9-10 | 47.4 | 38.9 | 8.5 | -1.69 | -8.9 |  |  | keep collecting (19/30) |
| pin_rlm | moneyline | 2-2 | 50.0 | 40.2 | 9.8 | +0.34 | 8.5 |  |  | keep collecting (4/30) |
| pin_rlm | total | 1-4 | 20.0 | 35.9 | -15.9 | -3.05 | -61.0 |  |  | keep collecting (5/30) |
| follow_move | moneyline | 18-14 | 56.2 | 47.5 | 8.7 | +9.17 | 28.7 |  |  | no edge shown yet |
| follow_move | spread | 10-16 | 38.5 | 51.8 | -13.3 | -6.85 | -26.3 |  |  | keep collecting (26/30) |
| follow_move | total | 15-21 | 41.7 | 47.6 | -6.0 | -7.27 | -20.2 |  |  | no edge shown yet |
| rlm_ratio | moneyline | 2-9 | 18.2 | 30.3 | -12.1 | -6.66 | -60.5 |  |  | keep collecting (11/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 46.2 | -46.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_ratio | total | 5-5 | 50.0 | 41.5 | 8.5 | -0.41 | -4.1 |  |  | keep collecting (10/30) |
| money_level | moneyline | 22-11 | 66.7 | 68.5 | -1.8 | -3.15 | -9.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 12-13 | 48.0 | 48.9 | -0.9 | -2.16 | -8.6 |  |  | keep collecting (25/30) |
| money_level | total | 23-16 | 59.0 | 59.8 | -0.8 | +4.83 | 12.4 |  |  | no edge shown yet |
| sharp_gap | moneyline | 10-17 | 37.0 | 46.4 | -9.3 | -9.85 | -36.5 |  |  | keep collecting (27/30) |
| sharp_gap | spread | 10-16 | 38.5 | 48.8 | -10.4 | -7.1 | -27.3 |  |  | keep collecting (26/30) |
| sharp_gap | total | 15-16 | 48.4 | 52.3 | -3.9 | -2.29 | -7.4 |  |  | no edge shown yet |
| money_moving | moneyline | 12-15 | 44.4 | 49.3 | -4.8 | -7.58 | -28.1 |  |  | keep collecting (27/30) |
| money_moving | spread | 10-16 | 38.5 | 48.8 | -10.4 | -7.1 | -27.3 |  |  | keep collecting (26/30) |
| money_moving | total | 16-18 | 47.1 | 52.5 | -5.4 | -3.42 | -10.0 |  |  | no edge shown yet |
| pin_value | moneyline | 3-0 | 100.0 | 43.4 | 56.6 | +14.59 | 486.2 |  |  | keep collecting (3/30) |
| pin_value | spread | 13-5 | 72.2 | 50.0 | 22.2 | +6.19 | 34.4 |  |  | keep collecting (18/30) |
| pin_value | total | 10-11 | 47.6 | 53.4 | -5.7 | -2.11 | -10.0 |  |  | keep collecting (21/30) |
| consensus_gap | moneyline | 11-11 | 50.0 | 57.2 | -7.2 | -5.27 | -24.0 |  |  | keep collecting (22/30) |
| consensus_gap | spread | 6-3 | 66.7 | 48.7 | 17.9 | +2.13 | 23.7 |  |  | keep collecting (9/30) |
| consensus_gap | total | 10-6 | 62.5 | 57.1 | 5.4 | +2.93 | 18.3 |  |  | keep collecting (16/30) |
| consensus_gap+money_level | moneyline | 9-5 | 64.3 | 69.7 | -5.4 | -1.16 | -8.3 |  |  | keep collecting (14/30) |
| follow_move+pin_move | moneyline | 6-3 | 66.7 | 47.8 | 18.9 | +1.71 | 19.0 |  |  | redundant -- identical record to pin_move alone, not independent confirmation |
| follow_move+rlm_quiet | moneyline | 5-10 | 33.3 | 30.3 | 3.0 | +6.24 | 41.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | moneyline | 2-3 | 40.0 | 30.3 | 9.7 | -0.58 | -11.6 |  |  | keep collecting (5/30) |
| consensus_gap+follow_move | moneyline | 6-5 | 54.5 | 51.8 | 2.8 | -1.21 | -11.0 |  |  | keep collecting (11/30) |
| follow_move+money_level | moneyline | 11-4 | 73.3 | 67.1 | 6.3 | +0.68 | 4.5 |  |  | keep collecting (15/30) |
| money_moving+sharp_gap | moneyline | 10-15 | 40.0 | 47.6 | -7.6 | -7.85 | -31.4 |  |  | keep collecting (25/30) |
| follow_move+money_moving | moneyline | 8-7 | 53.3 | 46.1 | 7.3 | -2.1 | -14.0 |  |  | keep collecting (15/30) |
| follow_move+sharp_gap | moneyline | 8-9 | 47.1 | 44.2 | 2.9 | -4.1 | -24.1 |  |  | keep collecting (17/30) |
| money_level+money_moving | moneyline | 9-5 | 64.3 | 66.9 | -2.6 | -1.3 | -9.3 |  |  | keep collecting (14/30) |
| money_level+sharp_gap | moneyline | 7-5 | 58.3 | 66.4 | -8.1 | -1.57 | -13.1 |  |  | keep collecting (12/30) |
| follow_move+rlm_ratio | moneyline | 2-9 | 18.2 | 30.3 | -12.1 | -6.66 | -60.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | moneyline | 1-6 | 14.3 | 30.3 | -16.0 | -5.0 | -71.4 |  |  | keep collecting (7/30) |
| money_moving+rlm_ratio | moneyline | 2-7 | 22.2 | 30.3 | -8.1 | -4.66 | -51.8 |  |  | keep collecting (9/30) |
| rlm_quiet+rlm_ratio | moneyline | 1-8 | 11.1 | 30.3 | -19.2 | -7.0 | -77.8 |  |  | keep collecting (9/30) |
| rlm_quiet+sharp_gap | moneyline | 1-8 | 11.1 | 30.3 | -19.2 | -7.0 | -77.8 |  |  | keep collecting (9/30) |
| rlm_ratio+sharp_gap | moneyline | 2-9 | 18.2 | 30.3 | -12.1 | -6.66 | -60.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 4-7 | 36.4 | 55.4 | -19.0 | -4.81 | -43.8 |  |  | keep collecting (11/30) |
| consensus_gap+rlm_quiet | moneyline | 1-4 | 20.0 | 30.3 | -10.3 | -3.0 | -60.0 |  |  | keep collecting (5/30) |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 30.3 | -5.3 | -2.0 | -50.0 |  |  | keep collecting (4/30) |
| consensus_gap+sharp_gap | moneyline | 3-8 | 27.3 | 51.8 | -24.5 | -5.95 | -54.1 |  |  | keep collecting (11/30) |
| consensus_gap+pin_rlm | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | +0.0 | 0.0 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 69.7 | -69.7 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 2-1 | 66.7 | 43.4 | 23.2 | +1.34 | 44.7 |  |  | keep collecting (3/30) |
| pin_rlm+sharp_gap | moneyline | 2-2 | 50.0 | 40.2 | 9.8 | +0.34 | 8.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 1-0 | 100.0 | 69.7 | 30.3 | +0.89 | 88.5 |  |  | keep collecting (1/30) |
| money_level+rlm_ratio | moneyline | 0-1 | 0.0 | 30.3 | -30.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+pin_move | moneyline | 3-1 | 75.0 | 50.0 | 25.0 | +1.33 | 33.1 |  |  | keep collecting (4/30) |
| money_level+pin_move | moneyline | 4-0 | 100.0 | 69.7 | 30.3 | +2.29 | 57.2 |  |  | keep collecting (4/30) |
| consensus_gap+money_delta | moneyline | 1-1 | 50.0 | 30.3 | 19.7 | +0.0 | 0.0 |  |  | keep collecting (2/30) |
| follow_move+money_delta | moneyline | 1-2 | 33.3 | 30.3 | 3.0 | -1.0 | -33.3 |  |  | keep collecting (3/30) |
| follow_move+pin_rlm | moneyline | 2-1 | 66.7 | 30.3 | 36.4 | +1.34 | 44.7 |  |  | keep collecting (3/30) |
| money_delta+money_moving | moneyline | 2-4 | 33.3 | 30.3 | 3.0 | -1.62 | -27.0 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_move | moneyline | 1-0 | 100.0 | 30.3 | 69.7 | +1.0 | 100.0 |  |  | keep collecting (1/30) |
| money_delta+pin_rlm | moneyline | 1-0 | 100.0 | 30.3 | 69.7 | +1.0 | 100.0 |  |  | keep collecting (1/30) |
| money_delta+rlm_quiet | moneyline | 1-2 | 33.3 | 30.3 | 3.0 | -1.0 | -33.3 |  |  | keep collecting (3/30) |
| money_delta+rlm_ratio | moneyline | 1-2 | 33.3 | 30.3 | 3.0 | -1.0 | -33.3 |  |  | keep collecting (3/30) |
| money_delta+sharp_gap | moneyline | 2-4 | 33.3 | 30.3 | 3.0 | -1.62 | -27.0 |  |  | redundant -- identical record to money_delta alone, not independent confirmation |
| money_moving+pin_move | moneyline | 3-0 | 100.0 | 56.6 | 43.4 | +2.38 | 79.4 |  |  | keep collecting (3/30) |
| pin_move+pin_rlm | moneyline | 1-1 | 50.0 | 30.3 | 19.7 | +0.0 | 0.0 |  |  | keep collecting (2/30) |
| pin_move+rlm_ratio | moneyline | 1-1 | 50.0 | 30.3 | 19.7 | +0.0 | 0.0 |  |  | keep collecting (2/30) |
| pin_move+sharp_gap | moneyline | 3-1 | 75.0 | 50.0 | 25.0 | +1.38 | 34.6 |  |  | keep collecting (4/30) |
| pin_rlm+rlm_quiet | moneyline | 1-1 | 50.0 | 30.3 | 19.7 | +0.0 | 0.0 |  |  | keep collecting (2/30) |
| pin_rlm+rlm_ratio | moneyline | 2-1 | 66.7 | 30.3 | 36.4 | +1.34 | 44.7 |  |  | keep collecting (3/30) |
| follow_move+pin_value | moneyline | 1-0 | 100.0 | 30.3 | 69.7 | +10.6 | 1060.0 |  |  | keep collecting (1/30) |
| pin_value+rlm_quiet | moneyline | 1-0 | 100.0 | 30.3 | 69.7 | +10.6 | 1060.0 |  |  | keep collecting (1/30) |
| follow_move+pin_move | spread | 6-8 | 42.9 | 52.7 | -9.9 | -2.62 | -18.7 |  |  | keep collecting (14/30) |
| money_moving+sharp_gap | spread | 10-16 | 38.5 | 48.8 | -10.4 | -7.1 | -27.3 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 3-4 | 42.9 | 52.7 | -9.9 | -1.19 | -16.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | spread | 7-11 | 38.9 | 48.3 | -9.4 | -4.82 | -26.8 |  |  | keep collecting (18/30) |
| money_level+sharp_gap | spread | 7-11 | 38.9 | 48.3 | -9.4 | -4.82 | -26.8 |  |  | keep collecting (18/30) |
| pin_move+rlm_quiet | spread | 1-2 | 33.3 | 53.8 | -20.5 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| consensus_gap+pin_value | spread | 6-3 | 66.7 | 48.7 | 17.9 | +2.13 | 23.7 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| follow_move+money_level | spread | 2-4 | 33.3 | 51.3 | -17.9 | -2.13 | -35.5 |  |  | keep collecting (6/30) |
| follow_move+money_moving | spread | 1-5 | 16.7 | 51.3 | -34.6 | -4.09 | -68.2 |  |  | keep collecting (6/30) |
| follow_move+sharp_gap | spread | 1-5 | 16.7 | 51.3 | -34.6 | -4.09 | -68.2 |  |  | keep collecting (6/30) |
| money_level+pin_move | spread | 3-4 | 42.9 | 50.5 | -7.7 | -1.3 | -18.5 |  |  | keep collecting (7/30) |
| money_moving+pin_move | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.26 | -37.6 |  |  | keep collecting (6/30) |
| pin_move+sharp_gap | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.26 | -37.6 |  |  | keep collecting (6/30) |
| money_delta+money_level | spread | 1-0 | 100.0 | 46.2 | 53.8 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+money_moving | spread | 2-1 | 66.7 | 46.2 | 20.5 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| money_delta+sharp_gap | spread | 2-1 | 66.7 | 46.2 | 20.5 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| consensus_gap+money_level | spread | 1-2 | 33.3 | 48.7 | -15.4 | -1.12 | -37.4 |  |  | keep collecting (3/30) |
| consensus_gap+money_moving | spread | 0-2 | 0.0 | 46.2 | -46.2 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+sharp_gap | spread | 0-2 | 0.0 | 46.2 | -46.2 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+pin_value | spread | 3-2 | 60.0 | 49.2 | 10.8 | +0.62 | 12.4 |  |  | keep collecting (5/30) |
| money_moving+pin_value | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.26 | -37.6 |  |  | keep collecting (6/30) |
| pin_value+sharp_gap | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.26 | -37.6 |  |  | keep collecting (6/30) |
| follow_move+money_delta | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 46.2 | -46.2 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | spread | 0-1 | 0.0 | 46.2 | -46.2 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 46.2 | -46.2 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 46.2 | -46.2 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 4-1 | 80.0 | 52.3 | 27.7 | +2.56 | 51.2 |  |  | keep collecting (5/30) |
| pin_move+pin_value | spread | 7-2 | 77.8 | 50.4 | 27.4 | +4.06 | 45.1 |  |  | keep collecting (9/30) |
| consensus_gap+pin_move | spread | 2-2 | 50.0 | 50.0 | 0.0 | -0.26 | -6.5 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 1-1 | 50.0 | 53.8 | -3.8 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 53.8 | 46.2 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| pin_value+rlm_quiet | spread | 1-0 | 100.0 | 53.8 | 46.2 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+rlm_quiet | spread | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta+money_moving | total | 6-4 | 60.0 | 41.5 | 18.5 | +1.5 | 15.0 |  |  | keep collecting (10/30) |
| money_delta+sharp_gap | total | 6-3 | 66.7 | 42.2 | 24.5 | +2.5 | 27.8 |  |  | keep collecting (9/30) |
| money_moving+sharp_gap | total | 14-16 | 46.7 | 51.9 | -5.2 | -3.2 | -10.7 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 5-14 | 26.3 | 37.4 | -11.1 | -9.37 | -49.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+follow_move | total | 3-4 | 42.9 | 56.0 | -13.2 | -1.31 | -18.7 |  |  | keep collecting (7/30) |
| consensus_gap+money_level | total | 8-4 | 66.7 | 64.1 | 2.6 | +3.11 | 25.9 |  |  | keep collecting (12/30) |
| consensus_gap+money_moving | total | 4-5 | 44.4 | 57.8 | -13.4 | -1.4 | -15.6 |  |  | keep collecting (9/30) |
| consensus_gap+pin_move | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+pin_value | total | 6-4 | 60.0 | 55.6 | 4.4 | +1.33 | 13.3 |  |  | keep collecting (10/30) |
| consensus_gap+sharp_gap | total | 4-4 | 50.0 | 57.1 | -7.1 | -0.4 | -5.0 |  |  | keep collecting (8/30) |
| follow_move+money_level | total | 8-7 | 53.3 | 58.5 | -5.1 | +0.32 | 2.1 |  |  | keep collecting (15/30) |
| follow_move+money_moving | total | 8-11 | 42.1 | 50.7 | -8.6 | -3.72 | -19.6 |  |  | keep collecting (19/30) |
| follow_move+pin_move | total | 5-11 | 31.2 | 44.7 | -13.5 | -6.33 | -39.5 |  |  | keep collecting (16/30) |
| follow_move+pin_value | total | 3-5 | 37.5 | 53.5 | -16.0 | -2.35 | -29.4 |  |  | keep collecting (8/30) |
| follow_move+sharp_gap | total | 9-10 | 47.4 | 50.7 | -3.4 | -1.81 | -9.5 |  |  | keep collecting (19/30) |
| money_level+money_moving | total | 13-11 | 54.2 | 58.2 | -4.1 | +0.9 | 3.7 |  |  | keep collecting (24/30) |
| money_level+pin_move | total | 4-5 | 44.4 | 54.7 | -10.3 | -1.36 | -15.1 |  |  | keep collecting (9/30) |
| money_level+pin_value | total | 7-6 | 53.8 | 59.8 | -5.9 | +0.2 | 1.6 |  |  | keep collecting (13/30) |
| money_level+sharp_gap | total | 12-10 | 54.5 | 57.7 | -3.1 | +1.03 | 4.7 |  |  | keep collecting (22/30) |
| money_moving+pin_move | total | 4-7 | 36.4 | 48.7 | -12.4 | -3.36 | -30.5 |  |  | keep collecting (11/30) |
| money_moving+pin_value | total | 5-7 | 41.7 | 54.7 | -13.0 | -2.53 | -21.1 |  |  | keep collecting (12/30) |
| pin_move+pin_value | total | 1-4 | 20.0 | 52.8 | -32.8 | -3.09 | -61.8 |  |  | keep collecting (5/30) |
| pin_move+sharp_gap | total | 2-7 | 22.2 | 45.3 | -23.1 | -5.14 | -57.1 |  |  | keep collecting (9/30) |
| pin_value+sharp_gap | total | 4-6 | 40.0 | 52.8 | -12.8 | -2.44 | -24.4 |  |  | keep collecting (10/30) |
| follow_move+money_delta | total | 7-8 | 46.7 | 39.7 | 7.0 | -1.5 | -10.0 |  |  | keep collecting (15/30) |
| money_delta+pin_move | total | 3-4 | 42.9 | 35.9 | 7.0 | -1.14 | -16.3 |  |  | keep collecting (7/30) |
| money_delta+rlm_quiet | total | 3-7 | 30.0 | 35.9 | -5.9 | -4.19 | -41.9 |  |  | keep collecting (10/30) |
| pin_move+rlm_quiet | total | 3-7 | 30.0 | 38.7 | -8.7 | -4.19 | -41.9 |  |  | keep collecting (10/30) |
| follow_move+rlm_ratio | total | 5-5 | 50.0 | 41.5 | 8.5 | -0.41 | -4.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | total | 5-3 | 62.5 | 42.9 | 19.6 | +1.59 | 19.9 |  |  | keep collecting (8/30) |
| money_moving+rlm_quiet | total | 1-5 | 16.7 | 35.9 | -19.2 | -4.09 | -68.2 |  |  | keep collecting (6/30) |
| money_moving+rlm_ratio | total | 5-5 | 50.0 | 41.5 | 8.5 | -0.41 | -4.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 1-4 | 20.0 | 35.9 | -15.9 | -3.09 | -61.8 |  |  | keep collecting (5/30) |
| rlm_quiet+sharp_gap | total | 1-5 | 16.7 | 35.9 | -19.2 | -4.09 | -68.2 |  |  | keep collecting (6/30) |
| rlm_ratio+sharp_gap | total | 5-5 | 50.0 | 41.5 | 8.5 | -0.41 | -4.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | total | 1-0 | 100.0 | 35.9 | 64.1 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| consensus_gap+rlm_quiet | total | 1-1 | 50.0 | 35.9 | 14.1 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| consensus_gap+rlm_ratio | total | 1-0 | 100.0 | 35.9 | 64.1 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_delta+pin_value | total | 2-2 | 50.0 | 42.9 | 7.1 | -0.22 | -5.5 |  |  | keep collecting (4/30) |
| pin_value+rlm_quiet | total | 1-2 | 33.3 | 35.9 | -2.6 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| pin_value+rlm_ratio | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 |  |  | keep collecting (2/30) |
| follow_move+pin_rlm | total | 1-3 | 25.0 | 35.9 | -10.9 | -2.05 | -51.2 |  |  | keep collecting (4/30) |
| money_delta+money_level | total | 3-1 | 75.0 | 42.9 | 32.1 | +1.81 | 45.3 |  |  | keep collecting (4/30) |
| money_delta+pin_rlm | total | 1-1 | 50.0 | 35.9 | 14.1 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | total | 1-1 | 50.0 | 35.9 | 14.1 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | total | 3-1 | 75.0 | 42.9 | 32.1 | +1.81 | 45.3 |  |  | keep collecting (4/30) |
| money_moving+pin_rlm | total | 1-4 | 20.0 | 35.9 | -15.9 | -3.05 | -61.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | total | 1-4 | 20.0 | 35.9 | -15.9 | -3.05 | -61.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 1-3 | 25.0 | 35.9 | -10.9 | -2.05 | -51.2 |  |  | keep collecting (4/30) |
| pin_rlm+rlm_ratio | total | 1-3 | 25.0 | 35.9 | -10.9 | -2.05 | -51.2 |  |  | keep collecting (4/30) |
| pin_rlm+sharp_gap | total | 1-4 | 20.0 | 35.9 | -15.9 | -3.05 | -61.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | total | 0-2 | 0.0 | 35.9 | -35.9 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| consensus_gap+pin_rlm | total | 0-1 | 0.0 | 35.9 | -35.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+pin_value | total | 0-1 | 0.0 | 35.9 | -35.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |

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
| rlm_quiet | both | 34-41 | 45.3 | 35.9 | 9.4 | +10.19 | 13.6 | 0.02 | 41.3 | no edge shown yet |
| pin_move | both | 5-9 | 35.7 | 48.2 | -12.5 | -5.1 | -36.4 | 0.22 | 50.0 | keep collecting (14/30) |
| money_delta | both | 10-7 | 58.8 | 41.7 | 17.1 | +4.43 | 26.1 | -0.22 | 29.4 | keep collecting (17/30) |
| pin_rlm | both | 1-2 | 33.3 | 26.8 | 6.5 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | both | 487-427 | 53.3 | 52.2 | 1.1 | -55.35 | -6.1 | 0.17 | 41.4 | no edge shown yet |
| rlm_ratio | both | 32-21 | 60.4 | 39.1 | 21.3 | +19.26 | 36.3 | 0.33 | 49.1 | no edge shown yet |
| money_level | both | 179-117 | 60.5 | 59.2 | 1.3 | -13.79 | -4.7 | -0.05 | 40.2 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 150-127 | 54.2 | 48.3 | 5.8 | +17.99 | 6.5 | 0.29 | 43.0 | no edge shown yet |
| money_moving | both | 109-86 | 55.9 | 51.3 | 4.6 | +1.26 | 0.6 | 0.1 | 42.6 | no edge shown yet |
| pin_value | both | 49-49 | 50.0 | 48.4 | 1.6 | -5.43 | -5.5 | 0.1 | 37.8 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.3 | -31.3 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 232-293 | 44.2 | 47.6 | -3.4 | -55.58 | -10.6 | 0.41 | 45.5 | DROP: below break-even |
| consensus_gap+money_level | both | 36-29 | 55.4 | 64.3 | -8.9 | -9.63 | -14.8 | 0.4 | 50.8 | no edge shown yet |
| consensus_gap+money_moving | both | 19-23 | 45.2 | 48.1 | -2.8 | -5.58 | -13.3 | 0.25 | 42.9 | no edge shown yet |
| consensus_gap+pin_value | both | 19-28 | 40.4 | 46.6 | -6.2 | -11.54 | -24.5 | 0.39 | 48.9 | DROP: below break-even |
| follow_move+rlm_quiet | both | 34-41 | 45.3 | 35.9 | 9.4 | +10.19 | 13.6 | 0.02 | 41.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 32-21 | 60.4 | 39.1 | 21.3 | +19.26 | 36.3 | 0.33 | 49.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 79-42 | 65.3 | 49.7 | 15.6 | +23.95 | 19.8 | 0.32 | 46.3 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 68-43 | 61.3 | 58.3 | 3.0 | -1.49 | -1.3 | -0.05 | 47.7 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 11-9 | 55.0 | 49.6 | 5.4 | +0.81 | 4.0 | 0.4 | 45.0 | keep collecting (20/30) |
| money_moving+pin_value | both | 8-5 | 61.5 | 49.8 | 11.8 | +2.04 | 15.7 | 0.31 | 38.5 | keep collecting (13/30) |
| rlm_quiet+rlm_ratio | both | 19-13 | 59.4 | 36.8 | 22.6 | +13.97 | 43.7 | -0.27 | 43.8 | no edge shown yet |
| rlm_quiet+sharp_gap | both | 21-16 | 56.8 | 36.7 | 20.1 | +12.79 | 34.6 | -0.26 | 43.2 | no edge shown yet |
| rlm_ratio+sharp_gap | both | 32-21 | 60.4 | 39.1 | 21.3 | +19.26 | 36.3 | 0.33 | 49.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 100-62 | 61.7 | 55.8 | 5.9 | +4.43 | 2.7 | 0.19 | 43.8 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 64-50 | 56.1 | 49.1 | 7.1 | +6.18 | 5.4 | 0.25 | 45.6 | no edge shown yet |
| money_delta+money_level | both | 3-2 | 60.0 | 45.7 | 14.3 | +1.46 | 29.2 | 1.16 | 60.0 | keep collecting (5/30) |
| money_delta+money_moving | both | 9-7 | 56.2 | 41.2 | 15.1 | +3.53 | 22.0 | -0.23 | 31.2 | keep collecting (16/30) |
| money_delta+pin_value | both | 3-1 | 75.0 | 50.0 | 25.0 | +1.61 | 40.3 | 0.0 | 25.0 | keep collecting (4/30) |
| money_delta+sharp_gap | both | 7-5 | 58.3 | 40.4 | 17.9 | +3.78 | 31.5 | -0.31 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | both | 13-8 | 61.9 | 48.7 | 13.2 | +3.66 | 17.4 | -0.18 | 33.3 | keep collecting (21/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 34-42 | 44.7 | 51.7 | -7.0 | -15.0 | -19.7 | 0.66 | 53.9 | no edge shown yet |
| consensus_gap+rlm_quiet | both | 4-7 | 36.4 | 37.0 | -0.6 | -2.99 | -27.1 | 0.95 | 72.7 | keep collecting (11/30) |
| follow_move+pin_value | both | 20-17 | 54.1 | 48.9 | 5.2 | +0.41 | 1.1 | -0.12 | 29.7 | no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 42.3 | -25.6 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 27-45 | 37.5 | 45.9 | -8.4 | -9.56 | -13.3 | 0.9 | 50.0 | DROP: below break-even |
| follow_move+money_level | both | 93-47 | 66.4 | 60.0 | 6.4 | -0.74 | -0.5 | 0.01 | 42.9 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 11-8 | 57.9 | 41.8 | 16.1 | +3.43 | 18.0 | 1.42 | 63.2 | keep collecting (19/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 44.1 | 5.9 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 57-32 | 64.0 | 52.7 | 11.4 | +10.61 | 11.9 | 0.3 | 50.6 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 3-0 | 100.0 | 49.6 | 50.4 | +2.61 | 87.1 | 0.0 | 0.0 | keep collecting (3/30) |
| follow_move+money_delta | both | 5-3 | 62.5 | 40.9 | 21.6 | +3.95 | 49.4 | 0.05 | 37.5 | keep collecting (8/30) |
| money_delta+rlm_quiet | both | 2-2 | 50.0 | 37.8 | 12.2 | +1.53 | 38.3 | -2.1 | 0.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | both | 14-11 | 56.0 | 36.7 | 19.3 | +7.57 | 30.3 | 0.27 | 44.0 | keep collecting (25/30) |
| money_moving+rlm_ratio | both | 14-9 | 60.9 | 41.9 | 19.0 | +7.48 | 32.5 | 0.32 | 47.8 | keep collecting (23/30) |
| consensus_gap+rlm_ratio | both | 4-4 | 50.0 | 38.2 | 11.8 | +0.09 | 1.1 | 0.69 | 62.5 | keep collecting (8/30) |
| pin_move+pin_value | both | 1-4 | 20.0 | 49.2 | -29.2 | -3.09 | -61.8 | 0.2 | 20.0 | keep collecting (5/30) |
| follow_move+pin_move | both | 5-3 | 62.5 | 52.0 | 10.5 | +0.9 | 11.2 | 0.42 | 62.5 | keep collecting (8/30) |
| consensus_gap+pin_move | both | 0-5 | 0.0 | 44.5 | -44.5 | -5.0 | -100.0 | 0.26 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | both | 2-2 | 50.0 | 55.9 | -5.9 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 26.8 | -26.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 26.8 | 23.2 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 26.8 | -26.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 26.8 | -26.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 26.8 | 23.2 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | both | 1-2 | 33.3 | 26.8 | 6.5 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 50.9 | -50.9 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-1 | 66.7 | 50.1 | 16.5 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 26.8 | 73.2 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 26.8 | 73.2 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 26.8 | 73.2 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 2-1 | 66.7 | 34.4 | 32.3 | +3.34 | 111.3 | 0.87 | 66.7 | keep collecting (3/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 26.8 | -26.8 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 17-28 | 37.8 | 26.8 | 11.0 | +7.77 | 17.3 | -0.15 | 42.2 | DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 14-11 | 56.0 | 49.7 | 6.3 | +1.77 | 7.1 | 0.48 | 48.0 | keep collecting (25/30) |
| pin_move | moneyline | 2-3 | 40.0 | 45.4 | -5.4 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-4 | 20.0 | 49.6 | -29.6 | -3.09 | -61.8 | 0.4 | 40.0 | keep collecting (5/30) |
| pin_move | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.14 | -3.5 | 0.25 | 50.0 | keep collecting (4/30) |
| money_delta | moneyline | 2-4 | 33.3 | 26.8 | 6.5 | +0.34 | 5.7 | -1.45 | 33.3 | keep collecting (6/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 7-2 | 77.8 | 49.8 | 28.0 | +4.26 | 47.4 | 0.44 | 22.2 | keep collecting (9/30) |
| pin_rlm | moneyline | 1-2 | 33.3 | 26.8 | 6.5 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | moneyline | 201-132 | 60.4 | 56.2 | 4.2 | -22.32 | -6.7 | 0.14 | 45.3 | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 129-150 | 46.2 | 49.8 | -3.6 | -31.3 | -11.2 | 0.03 | 33.7 | DROP: below break-even |
| follow_move | total | 157-145 | 52.0 | 50.0 | 2.0 | -1.73 | -0.6 | 0.34 | 44.0 | no edge shown yet |
| rlm_ratio | moneyline | 13-12 | 52.0 | 26.8 | 25.2 | +10.71 | 42.8 | 0.38 | 56.0 | keep collecting (25/30) |
| rlm_ratio | spread | 3-3 | 50.0 | 51.4 | -1.4 | -0.16 | -2.7 | 0.33 | 16.7 | keep collecting (6/30) |
| rlm_ratio | total | 16-6 | 72.7 | 49.7 | 23.1 | +8.72 | 39.6 | 0.27 | 50.0 | keep collecting (22/30) |
| money_level | moneyline | 102-41 | 71.3 | 69.0 | 2.3 | -7.6 | -5.3 | -0.18 | 45.5 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-18 | 48.6 | 49.3 | -0.8 | -2.69 | -7.7 | 1.0 | 51.4 | no edge shown yet |
| money_level | total | 60-58 | 50.8 | 50.2 | 0.7 | -3.5 | -3.0 | -0.19 | 30.5 | no edge shown yet |
| sharp_gap | moneyline | 63-64 | 49.6 | 46.5 | 3.1 | +1.95 | 1.5 | 0.36 | 50.4 | no edge shown yet |
| sharp_gap | spread | 20-15 | 57.1 | 49.8 | 7.3 | +3.0 | 8.6 | 0.77 | 40.0 | no edge shown yet |
| sharp_gap | total | 67-48 | 58.3 | 49.9 | 8.4 | +13.04 | 11.3 | 0.06 | 35.7 | no edge shown yet |
| money_moving | moneyline | 48-42 | 53.3 | 53.1 | 0.2 | -10.05 | -11.2 | -0.09 | 47.8 | no edge shown yet |
| money_moving | spread | 18-6 | 75.0 | 49.3 | 25.7 | +10.18 | 42.4 | 0.5 | 45.8 | keep collecting (24/30) |
| money_moving | total | 43-38 | 53.1 | 50.0 | 3.1 | +1.14 | 1.4 | 0.2 | 35.8 | no edge shown yet |
| pin_value | moneyline | 2-6 | 25.0 | 32.6 | -7.6 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| pin_value | spread | 24-21 | 53.3 | 49.5 | 3.9 | +0.16 | 0.3 | 0.24 | 37.8 | no edge shown yet |
| pin_value | total | 23-22 | 51.1 | 50.0 | 1.1 | -1.28 | -2.9 | -0.02 | 35.6 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.1 | -18.8 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 94-166 | 36.2 | 45.5 | -9.4 | -50.73 | -19.5 | 0.14 | 42.7 | DROP: below break-even |
| consensus_gap | spread | 68-61 | 52.7 | 49.2 | 3.6 | -1.63 | -1.3 | 0.36 | 40.3 | no edge shown yet |
| consensus_gap | total | 70-66 | 51.5 | 50.1 | 1.4 | -3.22 | -2.4 | 0.95 | 55.9 | no edge shown yet |
| money_level+sharp_gap | moneyline | 48-19 | 71.6 | 64.2 | 7.4 | +0.26 | 0.4 | 0.12 | 55.2 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+follow_move | moneyline | 12-23 | 34.3 | 54.6 | -20.4 | -15.58 | -44.5 | 0.03 | 51.4 | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 32.6 | -7.6 | -4.31 | -53.8 | -0.08 | 50.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| consensus_gap+rlm_quiet | moneyline | 1-5 | 16.7 | 26.8 | -10.1 | -3.68 | -61.3 | 1.07 | 83.3 | keep collecting (6/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.3 | -8.9 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 17-28 | 37.8 | 26.8 | 11.0 | +7.77 | 17.3 | -0.15 | 42.2 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 33-13 | 71.7 | 70.2 | 1.6 | -3.44 | -7.5 | -0.55 | 52.2 | beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 26.8 | -26.8 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 16-36 | 30.8 | 44.6 | -13.9 | -10.3 | -19.8 | 0.94 | 51.9 | DROP: below break-even |
| follow_move+money_level | moneyline | 59-16 | 78.7 | 68.9 | 9.8 | -0.63 | -0.8 | -0.29 | 45.3 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 30-13 | 69.8 | 55.9 | 13.8 | +4.92 | 11.4 | 0.06 | 53.5 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 27-20 | 57.4 | 70.3 | -12.8 | -8.47 | -18.0 | 0.21 | 51.1 | no edge shown yet |
| follow_move+sharp_gap | moneyline | 36-19 | 65.5 | 49.6 | 15.9 | +7.81 | 14.2 | 0.22 | 52.7 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 24-26 | 48.0 | 48.1 | -0.1 | -6.18 | -12.4 | 0.13 | 54.0 | no edge shown yet |
| consensus_gap+money_moving | moneyline | 10-21 | 32.3 | 47.8 | -15.5 | -11.42 | -36.9 | 0.24 | 48.4 | INVERT candidate: wrong well beyond its base rate |
| follow_move+rlm_ratio | moneyline | 13-12 | 52.0 | 26.8 | 25.2 | +10.71 | 42.8 | 0.38 | 56.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 9-9 | 50.0 | 26.8 | 23.2 | +8.84 | 49.1 | -0.26 | 44.4 | keep collecting (18/30) |
| rlm_quiet+sharp_gap | moneyline | 9-12 | 42.9 | 26.8 | 16.1 | +5.84 | 27.8 | -0.4 | 42.9 | keep collecting (21/30) |
| rlm_ratio+sharp_gap | moneyline | 13-12 | 52.0 | 26.8 | 25.2 | +10.71 | 42.8 | 0.38 | 56.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 26.8 | -1.8 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 6-8 | 42.9 | 26.8 | 16.1 | +3.37 | 24.1 | 0.48 | 50.0 | keep collecting (14/30) |
| money_moving+rlm_ratio | moneyline | 4-4 | 50.0 | 26.8 | 23.2 | +3.22 | 40.2 | 0.16 | 50.0 | keep collecting (8/30) |
| money_delta+money_moving | moneyline | 2-4 | 33.3 | 26.8 | 6.5 | +0.34 | 5.7 | -1.45 | 33.3 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-3 | 40.0 | 26.8 | 13.2 | +1.34 | 26.8 | -1.74 | 40.0 | keep collecting (5/30) |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 42.3 | -42.3 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-1 | 66.7 | 57.7 | 8.9 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | moneyline | 2-1 | 66.7 | 57.7 | 8.9 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 26.8 | -26.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-1 | 50.0 | 26.8 | 23.2 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 26.8 | -26.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 26.8 | -26.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-1 | 50.0 | 26.8 | 23.2 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | moneyline | 1-2 | 33.3 | 26.8 | 6.5 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 26.8 | -26.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 26.8 | -26.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.13 | 56.5 | -0.1 | 50.0 | keep collecting (2/30) |
| money_level+rlm_ratio | moneyline | 4-3 | 57.1 | 26.8 | 30.4 | +1.87 | 26.7 | 2.0 | 85.7 | keep collecting (7/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 26.8 | 73.2 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 1-0 | 100.0 | 26.8 | 73.2 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 1-0 | 100.0 | 26.8 | 73.2 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 26.8 | 39.9 | +3.34 | 111.3 | -1.53 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 1-1 | 50.0 | 26.8 | 23.2 | +1.7 | 85.0 | -4.2 | 0.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 26.8 | 73.2 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 26.8 | -26.8 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-0 | 100.0 | 26.8 | 73.2 | +1.64 | 164.0 | 3.8 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 47.9 | -2.4 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 47.9 | 35.5 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 10-8 | 55.6 | 48.8 | 6.7 | +0.6 | 3.3 | 0.5 | 50.0 | keep collecting (18/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-3 | 50.0 | 51.4 | -1.4 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-7 | 58.8 | 49.1 | 9.7 | +2.09 | 12.3 | 0.88 | 41.2 | keep collecting (17/30) |
| money_level+money_moving | spread | 10-6 | 62.5 | 48.9 | 13.6 | +3.12 | 19.5 | 1.19 | 68.8 | keep collecting (16/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 49.1 | -6.2 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 3-3 | 50.0 | 51.4 | -1.4 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 52.1 | -52.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 52.1 | -52.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-12 | 53.8 | 49.3 | 4.5 | +0.62 | 2.4 | 1.15 | 46.2 | keep collecting (26/30) |
| money_moving+sharp_gap | spread | 10-4 | 71.4 | 49.4 | 22.0 | +5.04 | 36.0 | 0.86 | 50.0 | keep collecting (14/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.3 | 17.4 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-11 | 45.0 | 48.5 | -3.5 | -3.2 | -16.0 | 0.85 | 45.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 47.9 | 14.6 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 11-10 | 52.4 | 48.9 | 3.5 | +0.04 | 0.2 | 0.9 | 47.6 | keep collecting (21/30) |
| follow_move+pin_value | spread | 12-7 | 63.2 | 49.0 | 14.2 | +3.45 | 18.2 | 0.26 | 31.6 | keep collecting (19/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 47.9 | 52.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 47.9 | 52.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 47.9 | 52.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-3 | 75.0 | 48.6 | 26.4 | +5.22 | 43.5 | 0.75 | 50.0 | keep collecting (12/30) |
| money_delta+rlm_quiet | spread | 1-0 | 100.0 | 47.9 | 52.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 2-0 | 100.0 | 47.9 | 52.1 | +1.74 | 87.1 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 2-2 | 50.0 | 52.1 | -2.1 | -0.07 | -1.7 | 1.25 | 25.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | spread | 2-1 | 66.7 | 50.7 | 16.0 | +0.86 | 28.7 | 1.0 | 33.3 | keep collecting (3/30) |
| pin_move+pin_value | spread | 1-3 | 25.0 | 48.9 | -23.9 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 47.9 | -47.9 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-2 | 33.3 | 47.9 | -14.5 | -1.09 | -36.4 | 0.33 | 33.3 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.1 | -52.1 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 14-11 | 56.0 | 49.7 | 6.3 | +1.77 | 7.1 | 0.48 | 48.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 25-24 | 51.0 | 50.1 | 0.9 | -1.17 | -2.4 | 0.02 | 36.7 | no edge shown yet |
| money_level+sharp_gap | total | 38-31 | 55.1 | 50.1 | 5.0 | +3.55 | 5.2 | -0.1 | 31.9 | no edge shown yet |
| money_moving+sharp_gap | total | 30-20 | 60.0 | 49.9 | 10.1 | +7.32 | 14.6 | 0.2 | 36.0 | no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 8-5 | 61.5 | 49.8 | 11.7 | +2.23 | 17.2 | 0.23 | 30.8 | keep collecting (13/30) |
| money_moving+pin_value | total | 5-3 | 62.5 | 49.9 | 12.6 | +1.47 | 18.3 | 0.12 | 25.0 | keep collecting (8/30) |
| pin_value+sharp_gap | total | 11-6 | 64.7 | 49.9 | 14.8 | +3.92 | 23.1 | -0.06 | 29.4 | keep collecting (17/30) |
| follow_move+money_level | total | 23-21 | 52.3 | 50.2 | 2.1 | -0.15 | -0.3 | 0.11 | 36.4 | no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 50.1 | -3.4 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 16-6 | 72.7 | 49.7 | 23.1 | +8.72 | 39.6 | 0.27 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 33-16 | 67.3 | 49.9 | 17.4 | +14.05 | 28.7 | 0.24 | 40.8 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 5-3 | 62.5 | 49.7 | 12.8 | +1.63 | 20.4 | 1.0 | 62.5 | keep collecting (8/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 49.9 | 16.8 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 16-6 | 72.7 | 49.7 | 23.1 | +8.72 | 39.6 | 0.27 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 18-16 | 52.9 | 50.0 | 3.0 | +0.47 | 1.4 | 0.44 | 47.1 | no edge shown yet |
| consensus_gap+money_level | total | 4-3 | 57.1 | 50.2 | 7.0 | +0.53 | 7.5 | -0.43 | 14.3 | keep collecting (7/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 50.2 | 29.8 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 50.1 | -16.8 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 6-6 | 50.0 | 49.9 | 0.1 | -0.58 | -4.8 | -0.08 | 25.0 | keep collecting (12/30) |
| money_moving+rlm_ratio | total | 8-4 | 66.7 | 49.7 | 16.9 | +3.4 | 28.3 | 0.25 | 50.0 | keep collecting (12/30) |
| consensus_gap+follow_move | total | 13-8 | 61.9 | 50.0 | 11.9 | +3.79 | 18.0 | 1.52 | 66.7 | keep collecting (21/30) |
| consensus_gap+money_delta | total | 2-0 | 100.0 | 50.4 | 49.6 | +1.78 | 88.9 | 0.0 | 0.0 | keep collecting (2/30) |
| follow_move+money_delta | total | 2-2 | 50.0 | 49.8 | 0.2 | -0.22 | -5.5 | 1.25 | 50.0 | keep collecting (4/30) |
| money_delta+money_moving | total | 6-2 | 75.0 | 49.8 | 25.2 | +3.35 | 41.9 | 0.5 | 25.0 | keep collecting (8/30) |
| money_delta+pin_value | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 | -0.5 | 0.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 5-1 | 83.3 | 49.9 | 33.5 | +3.44 | 57.4 | 0.67 | 33.3 | keep collecting (6/30) |
| money_moving+rlm_quiet | total | 6-3 | 66.7 | 49.7 | 17.0 | +2.45 | 27.3 | 0.22 | 44.4 | keep collecting (9/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 9-3 | 75.0 | 49.7 | 25.3 | +5.22 | 43.5 | -0.08 | 50.0 | keep collecting (12/30) |
| rlm_quiet+sharp_gap | total | 11-3 | 78.6 | 49.6 | 28.9 | +7.04 | 50.3 | 0.14 | 50.0 | keep collecting (14/30) |
| follow_move+pin_move | total | 2-0 | 100.0 | 49.6 | 50.4 | +1.86 | 93.0 | 1.0 | 100.0 | keep collecting (2/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 2-1 | 66.7 | 49.9 | 16.8 | +0.82 | 27.3 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 49.6 | 0.4 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 3-1 | 75.0 | 49.6 | 25.4 | +1.77 | 44.2 | 0.25 | 50.0 | keep collecting (4/30) |
| money_level+pin_move | total | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_value | total | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 195-285 | 40.6 | 41.8 | -1.2 | -39.23 | -8.2 |  |  | DROP: below break-even |
| pin_move | both | 519-520 | 50.0 | 49.9 | 0.0 | -33.55 | -3.2 |  |  | DROP: below break-even |
| money_delta | both | 330-440 | 42.9 | 43.9 | -1.1 | -61.68 | -8.0 |  |  | DROP: below break-even |
| pin_rlm | both | 143-163 | 46.7 | 42.1 | 4.6 | +28.58 | 9.3 |  |  | DROP: below break-even |
| follow_move | both | 900-815 | 52.5 | 51.8 | 0.7 | -95.47 | -5.6 |  |  | no edge shown yet |
| rlm_ratio | both | 207-240 | 46.3 | 44.1 | 2.2 | -6.92 | -1.5 |  |  | DROP: below break-even |
| money_level | both | 1141-845 | 57.5 | 55.6 | 1.8 | -67.4 | -3.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 882-1025 | 46.3 | 47.5 | -1.2 | -137.04 | -7.2 |  |  | DROP: below break-even |
| money_moving | both | 885-1026 | 46.3 | 47.8 | -1.5 | -145.45 | -7.6 |  |  | DROP: below break-even |
| pin_value | both | 377-373 | 50.3 | 48.0 | 2.3 | +21.95 | 2.9 |  |  | no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 358-469 | 43.3 | 47.6 | -4.3 | -87.98 | -10.6 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 137-137 | 50.0 | 51.3 | -1.3 | -17.84 | -6.5 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 156-256 | 37.9 | 44.9 | -7.0 | -40.19 | -9.8 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 85-88 | 49.1 | 51.0 | -1.9 | +1.23 | 0.7 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 24-41 | 36.9 | 37.9 | -0.9 | +9.03 | 13.9 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 145-153 | 48.7 | 46.0 | 2.7 | +8.05 | 2.7 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | both | 27-46 | 37.0 | 39.2 | -2.2 | -2.75 | -3.8 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 154-260 | 37.2 | 44.2 | -7.0 | -41.31 | -10.0 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 474-509 | 48.2 | 49.3 | -1.1 | -76.23 | -7.8 |  |  | DROP: below break-even |
| follow_move+pin_move | both | 372-373 | 49.9 | 50.2 | -0.3 | -36.83 | -4.9 |  |  | no edge shown yet |
| follow_move+pin_rlm | both | 111-115 | 49.1 | 44.0 | 5.1 | +6.86 | 3.0 |  |  | no edge shown yet |
| follow_move+pin_value | both | 131-124 | 51.4 | 48.9 | 2.5 | +2.38 | 0.9 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 207-240 | 46.3 | 44.1 | 2.2 | -6.92 | -1.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 480-507 | 48.6 | 49.1 | -0.4 | -66.21 | -6.7 |  |  | DROP: below break-even |
| money_moving+pin_move | both | 307-336 | 47.7 | 48.7 | -0.9 | -26.16 | -4.1 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 137-158 | 46.4 | 42.1 | 4.3 | +27.61 | 9.4 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 162-194 | 45.5 | 47.3 | -1.8 | -18.69 | -5.3 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 199-231 | 46.3 | 44.2 | 2.1 | -5.83 | -1.4 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 846-985 | 46.2 | 47.5 | -1.3 | -128.53 | -7.0 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 131-135 | 49.2 | 44.1 | 5.2 | +22.45 | 8.4 |  |  | no edge shown yet |
| pin_move+pin_value | both | 164-161 | 50.5 | 49.1 | 1.4 | -3.98 | -1.2 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 118-113 | 51.1 | 45.4 | 5.7 | +14.2 | 6.1 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 312-337 | 48.1 | 48.5 | -0.5 | -22.7 | -3.5 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 40-42 | 48.8 | 45.5 | 3.3 | +11.58 | 14.1 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 111-115 | 49.1 | 44.0 | 5.1 | +6.86 | 3.0 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 143-163 | 46.7 | 42.1 | 4.6 | +28.58 | 9.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 40-31 | 56.3 | 48.4 | 7.9 | +5.51 | 7.8 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 163-195 | 45.5 | 47.2 | -1.6 | -18.8 | -5.3 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 207-240 | 46.3 | 44.1 | 2.2 | -6.92 | -1.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 159-188 | 45.8 | 45.9 | -0.0 | -26.97 | -7.8 |  |  | DROP: below break-even |
| money_level+money_moving | both | 626-559 | 52.8 | 52.4 | 0.4 | -51.71 | -4.4 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 614-548 | 52.8 | 52.2 | 0.6 | -43.39 | -3.7 |  |  | no edge shown yet |
| follow_move+money_level | both | 586-416 | 58.5 | 56.6 | 1.8 | -45.64 | -4.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 98-83 | 54.1 | 48.2 | 6.0 | +11.5 | 6.4 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 221-176 | 55.7 | 58.2 | -2.5 | -21.92 | -5.5 |  |  | no edge shown yet |
| money_level+pin_move | both | 304-277 | 52.3 | 53.2 | -0.8 | -28.17 | -4.8 |  |  | no edge shown yet |
| money_level+pin_value | both | 182-166 | 52.3 | 50.0 | 2.3 | -7.73 | -2.2 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 22-52 | 29.7 | 36.2 | -6.5 | -11.25 | -15.2 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | both | 195-285 | 40.6 | 41.8 | -1.2 | -39.23 | -8.2 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 100-162 | 38.2 | 41.4 | -3.2 | -31.82 | -12.1 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 236-340 | 41.0 | 42.3 | -1.3 | -48.47 | -8.4 |  |  | DROP: below break-even |
| consensus_gap+money_delta | both | 43-111 | 27.9 | 36.7 | -8.8 | -30.77 | -20.0 |  |  | DROP: below break-even |
| money_delta+money_level | both | 121-112 | 51.9 | 46.8 | 5.1 | +14.31 | 6.1 |  |  | no edge shown yet |
| money_delta+pin_value | both | 70-73 | 49.0 | 46.9 | 2.1 | -5.79 | -4.1 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 233-334 | 41.1 | 42.3 | -1.2 | -45.64 | -8.0 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 81-134 | 37.7 | 39.9 | -2.2 | -21.73 | -10.1 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | both | 92-157 | 36.9 | 41.3 | -4.4 | -32.72 | -13.1 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 53-97 | 35.3 | 42.8 | -7.5 | -36.98 | -24.7 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | both | 93-117 | 44.3 | 44.0 | 0.3 | -10.09 | -4.8 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 43-65 | 39.8 | 40.5 | -0.7 | -10.48 | -9.7 |  |  | DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 122-139 | 46.7 | 46.2 | 0.6 | -6.08 | -2.3 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 64-45 | 58.7 | 46.7 | 12.0 | +18.2 | 16.7 |  |  | no edge shown yet |
| money_delta+pin_rlm | both | 84-95 | 46.9 | 42.0 | 4.9 | +13.39 | 7.5 |  |  | no edge shown yet |
| money_delta+rlm_ratio | both | 116-122 | 48.7 | 44.8 | 4.0 | -0.51 | -0.2 |  |  | no edge shown yet |
| pin_value+rlm_quiet | both | 27-37 | 42.2 | 46.8 | -4.6 | -2.16 | -3.4 |  |  | DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 49.6 | 50.4 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 57-120 | 32.2 | 27.6 | 4.6 | -1.22 | -0.7 |  |  | DROP: below break-even |
| rlm_quiet | spread | 48-49 | 49.5 | 50.7 | -1.2 | -4.51 | -4.6 |  |  | no edge shown yet |
| rlm_quiet | total | 90-116 | 43.7 | 49.8 | -6.1 | -33.5 | -16.3 |  |  | DROP: below break-even |
| pin_move | moneyline | 109-104 | 51.2 | 49.5 | 1.7 | +8.7 | 4.1 |  |  | no edge shown yet |
| pin_move | spread | 205-214 | 48.9 | 50.2 | -1.3 | -27.49 | -6.6 |  |  | no edge shown yet |
| pin_move | total | 205-202 | 50.4 | 49.9 | 0.5 | -14.76 | -3.6 |  |  | no edge shown yet |
| money_delta | moneyline | 51-170 | 23.1 | 28.3 | -5.2 | -46.54 | -21.1 |  |  | DROP: below break-even |
| money_delta | spread | 125-128 | 49.4 | 50.7 | -1.3 | -14.11 | -5.6 |  |  | no edge shown yet |
| money_delta | total | 154-142 | 52.0 | 49.8 | 2.3 | -1.02 | -0.3 |  |  | no edge shown yet |
| pin_rlm | moneyline | 40-74 | 35.1 | 28.8 | 6.3 | +23.31 | 20.4 |  |  | DROP: below break-even |
| pin_rlm | spread | 25-22 | 53.2 | 50.9 | 2.3 | +0.79 | 1.7 |  |  | no edge shown yet |
| pin_rlm | total | 78-67 | 53.8 | 49.7 | 4.1 | +4.47 | 3.1 |  |  | no edge shown yet |
| follow_move | moneyline | 332-219 | 60.3 | 55.9 | 4.4 | -16.6 | -3.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 257-278 | 48.0 | 49.6 | -1.6 | -44.59 | -8.3 |  |  | DROP: below break-even |
| follow_move | total | 311-318 | 49.4 | 50.0 | -0.5 | -34.27 | -5.4 |  |  | no edge shown yet |
| rlm_ratio | moneyline | 39-89 | 30.5 | 29.7 | 0.8 | -9.44 | -7.4 |  |  | DROP: below break-even |
| rlm_ratio | spread | 41-44 | 48.2 | 50.1 | -1.9 | -6.76 | -8.0 |  |  | no edge shown yet |
| rlm_ratio | total | 127-107 | 54.3 | 49.8 | 4.5 | +9.28 | 4.0 |  |  | no edge shown yet |
| money_level | moneyline | 439-168 | 72.3 | 69.1 | 3.2 | -25.85 | -4.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 328-339 | 49.2 | 49.3 | -0.1 | -43.17 | -6.5 |  |  | DROP: below break-even |
| money_level | total | 374-338 | 52.5 | 50.1 | 2.4 | +1.62 | 0.2 |  |  | no edge shown yet |
| sharp_gap | moneyline | 211-344 | 38.0 | 41.8 | -3.8 | -65.0 | -11.7 |  |  | DROP: below break-even |
| sharp_gap | spread | 334-326 | 50.6 | 49.6 | 1.0 | -24.82 | -3.8 |  |  | no edge shown yet |
| sharp_gap | total | 337-355 | 48.7 | 49.9 | -1.2 | -47.22 | -6.8 |  |  | DROP: below break-even |
| money_moving | moneyline | 221-332 | 40.0 | 43.0 | -3.0 | -53.68 | -9.7 |  |  | DROP: below break-even |
| money_moving | spread | 331-329 | 50.2 | 49.6 | 0.6 | -30.69 | -4.7 |  |  | no edge shown yet |
| money_moving | total | 333-365 | 47.7 | 49.9 | -2.2 | -61.08 | -8.8 |  |  | DROP: below break-even |
| pin_value | moneyline | 21-54 | 28.0 | 31.1 | -3.1 | +25.46 | 33.9 |  |  | DROP: below break-even |
| pin_value | spread | 171-152 | 52.9 | 49.6 | 3.3 | -2.92 | -0.9 |  |  | no edge shown yet |
| pin_value | total | 185-167 | 52.6 | 50.1 | 2.5 | -0.59 | -0.2 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.1 | 47.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 151-284 | 34.7 | 45.6 | -10.9 | -83.61 | -19.2 |  |  | DROP: below break-even |
| consensus_gap | spread | 92-78 | 54.1 | 49.2 | 4.9 | +0.43 | 0.3 |  |  | no edge shown yet |
| consensus_gap | total | 115-107 | 51.8 | 50.2 | 1.6 | -4.8 | -2.2 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 154-88 | 63.6 | 63.4 | 0.2 | -8.0 | -3.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 143-86 | 62.4 | 62.9 | -0.4 | -7.89 | -3.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 197-318 | 38.3 | 41.8 | -3.6 | -50.24 | -9.8 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 58-72 | 44.6 | 53.2 | -8.6 | -21.64 | -16.6 |  |  | DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 8-40 | 16.7 | 28.7 | -12.1 | -11.64 | -24.2 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 57-120 | 32.2 | 27.6 | 4.6 | -1.22 | -0.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 104-70 | 59.8 | 69.2 | -9.4 | -17.93 | -10.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 59-161 | 26.8 | 40.7 | -13.9 | -29.56 | -13.4 |  |  | DROP: below break-even |
| follow_move+money_level | moneyline | 257-83 | 75.6 | 70.3 | 5.2 | -10.99 | -3.2 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 109-116 | 48.4 | 48.0 | 0.4 | -14.75 | -6.6 |  |  | no edge shown yet |
| money_delta+money_moving | moneyline | 48-153 | 23.9 | 27.9 | -4.1 | -32.51 | -16.2 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 46-152 | 23.2 | 28.0 | -4.7 | -33.7 | -17.0 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 56-167 | 25.1 | 39.5 | -14.4 | -33.58 | -15.1 |  |  | DROP: below break-even |
| follow_move+sharp_gap | moneyline | 106-117 | 47.5 | 47.0 | 0.6 | -16.18 | -7.3 |  |  | no edge shown yet |
| money_moving+rlm_quiet | moneyline | 24-73 | 24.7 | 27.7 | -3.0 | -10.91 | -11.3 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 25-76 | 24.8 | 27.7 | -3.0 | -14.45 | -14.3 |  |  | DROP: below break-even |
| consensus_gap+pin_move | moneyline | 31-36 | 46.3 | 53.1 | -6.8 | +6.25 | 9.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 11-29 | 27.5 | 30.3 | -2.8 | +9.65 | 24.1 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 5-33 | 13.2 | 29.2 | -16.1 | -9.04 | -23.8 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 89-70 | 56.0 | 51.3 | 4.7 | +8.06 | 5.1 |  |  | no edge shown yet |
| follow_move+pin_rlm | moneyline | 26-40 | 39.4 | 29.6 | 9.8 | +3.8 | 5.8 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 39-89 | 30.5 | 29.7 | 0.8 | -9.44 | -7.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 49-62 | 44.1 | 43.1 | 1.0 | +13.07 | 11.8 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 39-71 | 35.5 | 28.9 | 6.6 | +24.91 | 22.6 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 38-83 | 31.4 | 29.9 | 1.5 | -4.84 | -4.0 |  |  | DROP: below break-even |
| pin_move+pin_rlm | moneyline | 28-46 | 37.8 | 28.7 | 9.2 | +17.19 | 23.2 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 25-35 | 41.7 | 28.3 | 13.3 | +9.29 | 15.5 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 22-31 | 41.5 | 30.3 | 11.2 | +8.28 | 15.6 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 49-64 | 43.4 | 42.4 | 1.0 | +10.89 | 9.6 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 15-33 | 31.2 | 28.7 | 2.5 | -4.18 | -8.7 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 26-40 | 39.4 | 29.6 | 9.8 | +3.8 | 5.8 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 40-74 | 35.1 | 28.8 | 6.3 | +23.31 | 20.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 24-73 | 24.7 | 27.7 | -3.0 | -12.91 | -13.3 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 39-89 | 30.5 | 29.7 | 0.8 | -9.44 | -7.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 12-83 | 12.6 | 28.3 | -15.6 | -29.62 | -31.2 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 14-45 | 23.7 | 30.7 | -7.0 | +2.27 | 3.8 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 17-35 | 32.7 | 30.4 | 2.3 | +1.84 | 3.5 |  |  | DROP: below break-even |
| money_delta+pin_rlm | moneyline | 23-44 | 34.3 | 28.9 | 5.5 | +8.63 | 12.9 |  |  | DROP: below break-even |
| money_delta+pin_value | moneyline | 2-18 | 10.0 | 26.8 | -16.8 | -11.18 | -55.9 |  |  | keep collecting (20/30) |
| money_moving+pin_value | moneyline | 10-33 | 23.3 | 30.0 | -6.8 | +8.44 | 19.6 |  |  | DROP: below break-even |
| pin_move+pin_value | moneyline | 6-9 | 40.0 | 33.0 | 7.0 | +7.27 | 48.5 |  |  | keep collecting (15/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 26.8 | 4.5 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 10-35 | 22.2 | 29.9 | -7.7 | +6.44 | 14.3 |  |  | DROP: below break-even |
| follow_move+money_delta | moneyline | 24-49 | 32.9 | 30.6 | 2.3 | -11.09 | -15.2 |  |  | DROP: below break-even |
| money_delta+money_level | moneyline | 14-23 | 37.8 | 30.6 | 7.3 | +6.11 | 16.5 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | moneyline | 22-40 | 35.5 | 30.5 | 5.0 | -4.0 | -6.4 |  |  | DROP: below break-even |
| money_level+pin_move | moneyline | 71-42 | 62.8 | 67.1 | -4.2 | -4.48 | -4.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 11-10 | 52.4 | 33.4 | 19.0 | +4.77 | 22.7 |  |  | keep collecting (21/30) |
| money_level+rlm_ratio | moneyline | 13-12 | 52.0 | 37.9 | 14.1 | +5.1 | 20.4 |  |  | keep collecting (25/30) |
| money_delta+rlm_quiet | moneyline | 16-37 | 30.2 | 29.4 | 0.8 | -10.95 | -20.7 |  |  | DROP: below break-even |
| money_level+pin_value | moneyline | 5-2 | 71.4 | 66.6 | 4.8 | +0.68 | 9.7 |  |  | keep collecting (7/30) |
| follow_move+pin_value | moneyline | 3-7 | 30.0 | 31.4 | -1.4 | +5.8 | 58.0 |  |  | keep collecting (10/30) |
| pin_value+rlm_quiet | moneyline | 2-6 | 25.0 | 26.8 | -1.8 | +6.12 | 76.5 |  |  | keep collecting (8/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 26.8 | -1.8 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 35-28 | 55.6 | 48.7 | 6.8 | +1.81 | 2.9 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 48-44 | 52.2 | 49.0 | 3.2 | -3.14 | -3.4 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 27-29 | 48.2 | 49.2 | -1.0 | -5.99 | -10.7 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 66-47 | 58.4 | 49.2 | 9.2 | +9.08 | 8.0 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 4-4 | 50.0 | 50.0 | 0.0 | -0.67 | -8.3 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | spread | 47-44 | 51.6 | 49.2 | 2.5 | -4.03 | -4.4 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 158-165 | 48.9 | 49.3 | -0.4 | -22.2 | -6.9 |  |  | no edge shown yet |
| follow_move+pin_move | spread | 128-143 | 47.2 | 50.0 | -2.7 | -26.55 | -9.8 |  |  | DROP: below break-even |
| follow_move+pin_rlm | spread | 19-18 | 51.4 | 50.6 | 0.7 | -0.65 | -1.7 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 60-51 | 54.1 | 49.1 | 4.9 | +1.33 | 1.2 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 41-44 | 48.2 | 50.1 | -1.9 | -6.76 | -8.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 159-164 | 49.2 | 49.4 | -0.1 | -20.06 | -6.2 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 119-127 | 48.4 | 49.8 | -1.4 | -19.25 | -7.8 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 23-22 | 51.1 | 50.8 | 0.3 | -1.04 | -2.3 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 81-83 | 49.4 | 49.3 | 0.1 | -13.09 | -8.0 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 39-43 | 47.6 | 50.1 | -2.5 | -7.69 | -9.4 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 326-321 | 50.4 | 49.6 | 0.8 | -27.19 | -4.2 |  |  | no edge shown yet |
| pin_move+pin_rlm | spread | 25-22 | 53.2 | 50.9 | 2.3 | +0.79 | 1.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 80-81 | 49.7 | 49.7 | -0.0 | -10.64 | -6.6 |  |  | no edge shown yet |
| pin_move+rlm_ratio | spread | 22-24 | 47.8 | 50.5 | -2.6 | -3.94 | -8.6 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 122-127 | 49.0 | 49.8 | -0.8 | -16.52 | -6.6 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 7-10 | 41.2 | 50.6 | -9.5 | -3.88 | -22.8 |  |  | keep collecting (17/30) |
| pin_rlm+rlm_ratio | spread | 19-18 | 51.4 | 50.6 | 0.7 | -0.65 | -1.7 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 25-22 | 53.2 | 50.9 | 2.3 | +0.79 | 1.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 7-7 | 50.0 | 49.4 | 0.6 | -1.01 | -7.2 |  |  | keep collecting (14/30) |
| pin_value+sharp_gap | spread | 81-83 | 49.4 | 49.4 | 0.0 | -13.15 | -8.0 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 41-44 | 48.2 | 50.1 | -1.9 | -6.76 | -8.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 154-168 | 47.8 | 49.1 | -1.3 | -28.82 | -8.9 |  |  | DROP: below break-even |
| money_level+rlm_ratio | spread | 21-28 | 42.9 | 49.9 | -7.0 | -9.13 | -18.6 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 256-254 | 50.2 | 49.3 | 0.9 | -23.55 | -4.6 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 58-48 | 54.7 | 48.9 | 5.8 | +1.6 | 1.5 |  |  | no edge shown yet |
| money_level+money_moving | spread | 255-255 | 50.0 | 49.3 | 0.7 | -25.46 | -5.0 |  |  | no edge shown yet |
| money_level+pin_move | spread | 110-128 | 46.2 | 49.6 | -3.4 | -28.78 | -12.1 |  |  | DROP: below break-even |
| money_level+pin_value | spread | 89-88 | 50.3 | 49.1 | 1.2 | -11.19 | -6.3 |  |  | no edge shown yet |
| consensus_gap+money_delta | spread | 14-14 | 50.0 | 50.5 | -0.5 | -2.09 | -7.5 |  |  | keep collecting (28/30) |
| follow_move+money_delta | spread | 38-49 | 43.7 | 50.2 | -6.5 | -14.62 | -16.8 |  |  | DROP: below break-even |
| money_delta+money_level | spread | 41-40 | 50.6 | 50.0 | 0.6 | -3.05 | -3.8 |  |  | no edge shown yet |
| money_delta+money_moving | spread | 70-75 | 48.3 | 50.4 | -2.1 | -11.82 | -8.2 |  |  | no edge shown yet |
| money_delta+pin_value | spread | 32-26 | 55.2 | 50.4 | 4.7 | +1.88 | 3.2 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 69-73 | 48.6 | 50.4 | -1.8 | -10.8 | -7.6 |  |  | no edge shown yet |
| follow_move+rlm_quiet | spread | 48-49 | 49.5 | 50.7 | -1.2 | -4.51 | -4.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 14-4 | 77.8 | 50.7 | 27.1 | +8.78 | 48.8 |  |  | keep collecting (18/30) |
| rlm_quiet+sharp_gap | spread | 21-10 | 67.7 | 50.9 | 16.8 | +9.22 | 29.7 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+pin_rlm | spread | 14-10 | 58.3 | 50.4 | 8.0 | +2.58 | 10.7 |  |  | keep collecting (24/30) |
| money_delta+rlm_ratio | spread | 16-27 | 37.2 | 50.0 | -12.7 | -12.78 | -29.7 |  |  | DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 52.1 | 47.9 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_move | spread | 36-42 | 46.2 | 50.8 | -4.7 | -9.09 | -11.7 |  |  | no edge shown yet |
| money_delta+pin_rlm | spread | 13-15 | 46.4 | 50.6 | -4.2 | -3.31 | -11.8 |  |  | keep collecting (28/30) |
| money_delta+rlm_quiet | spread | 14-18 | 43.8 | 51.1 | -7.3 | -5.07 | -15.8 |  |  | no edge shown yet |
| money_moving+rlm_quiet | spread | 20-10 | 66.7 | 50.9 | 15.8 | +8.27 | 27.6 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_move+rlm_quiet | spread | 26-23 | 53.1 | 51.1 | 2.0 | +1.08 | 2.2 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-2 | 75.0 | 51.6 | 23.4 | +3.56 | 44.5 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_quiet | spread | 3-3 | 50.0 | 50.7 | -0.7 | -0.42 | -7.1 |  |  | keep collecting (6/30) |
| pin_value+rlm_quiet | spread | 5-4 | 55.6 | 49.3 | 6.3 | +0.39 | 4.4 |  |  | keep collecting (9/30) |
| follow_move+money_delta | total | 97-90 | 51.9 | 49.8 | 2.1 | -1.26 | -0.7 |  |  | no edge shown yet |
| money_level+money_moving | total | 217-216 | 50.1 | 50.0 | 0.1 | -18.24 | -4.2 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 215-208 | 50.8 | 50.0 | 0.8 | -11.95 | -2.8 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 323-346 | 48.3 | 49.9 | -1.6 | -51.1 | -7.6 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 59-58 | 50.4 | 50.3 | 0.1 | -5.59 | -4.8 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 27-23 | 54.0 | 50.2 | 3.8 | +0.96 | 1.9 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 65-61 | 51.6 | 50.2 | 1.4 | -3.29 | -2.6 |  |  | no edge shown yet |
| follow_move+money_moving | total | 207-228 | 47.6 | 49.9 | -2.3 | -39.28 | -9.0 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 215-226 | 48.8 | 49.9 | -1.2 | -29.97 | -6.8 |  |  | DROP: below break-even |
| money_level+pin_move | total | 123-107 | 53.5 | 50.0 | 3.5 | +5.1 | 2.2 |  |  | no edge shown yet |
| money_level+pin_value | total | 88-76 | 53.7 | 50.2 | 3.5 | +2.78 | 1.7 |  |  | no edge shown yet |
| pin_move+pin_value | total | 78-71 | 52.3 | 50.0 | 2.4 | -0.6 | -0.4 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 90-116 | 43.7 | 49.8 | -6.1 | -33.5 | -16.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 139-147 | 48.6 | 49.9 | -1.3 | -19.98 | -7.0 |  |  | no edge shown yet |
| rlm_quiet+sharp_gap | total | 54-76 | 41.5 | 49.7 | -8.2 | -26.59 | -20.4 |  |  | DROP: below break-even |
| money_delta+money_moving | total | 118-112 | 51.3 | 49.8 | 1.5 | -4.14 | -1.8 |  |  | no edge shown yet |
| follow_move+money_level | total | 175-165 | 51.5 | 50.1 | 1.4 | -5.84 | -1.7 |  |  | no edge shown yet |
| follow_move+pin_value | total | 68-66 | 50.7 | 50.0 | 0.7 | -4.75 | -3.5 |  |  | no edge shown yet |
| money_moving+pin_value | total | 71-78 | 47.7 | 50.0 | -2.4 | -14.04 | -9.4 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 72-77 | 48.3 | 50.0 | -1.7 | -12.09 | -8.1 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 49-51 | 49.0 | 50.2 | -1.2 | -7.49 | -7.5 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 51-49 | 51.0 | 50.2 | 0.8 | -3.7 | -3.7 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 44-37 | 54.3 | 50.3 | 4.1 | +1.99 | 2.5 |  |  | no edge shown yet |
| consensus_gap+money_delta | total | 17-14 | 54.8 | 50.0 | 4.8 | +0.94 | 3.0 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | total | 11-9 | 55.0 | 49.9 | 5.1 | +0.81 | 4.1 |  |  | keep collecting (20/30) |
| money_delta+rlm_quiet | total | 23-42 | 35.4 | 49.7 | -14.3 | -20.95 | -32.2 |  |  | DROP: below break-even |
| money_delta+sharp_gap | total | 118-109 | 52.0 | 49.8 | 2.2 | -1.14 | -0.5 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 48-74 | 39.3 | 49.7 | -10.4 | -30.08 | -24.7 |  |  | DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 66-49 | 57.4 | 49.8 | 7.6 | +11.25 | 9.8 |  |  | no edge shown yet |
| money_delta+pin_move | total | 69-62 | 52.7 | 49.7 | 3.0 | +1.18 | 0.9 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 141-146 | 49.1 | 49.9 | -0.7 | -17.07 | -5.9 |  |  | no edge shown yet |
| follow_move+pin_move | total | 155-160 | 49.2 | 49.9 | -0.7 | -18.34 | -5.8 |  |  | no edge shown yet |
| pin_value+rlm_quiet | total | 20-27 | 42.6 | 49.8 | -7.2 | -8.67 | -18.5 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | total | 10-9 | 52.6 | 50.0 | 2.6 | -0.13 | -0.7 |  |  | keep collecting (19/30) |
| consensus_gap+rlm_ratio | total | 18-9 | 66.7 | 50.1 | 16.6 | +6.95 | 25.8 |  |  | keep collecting (27/30) |
| follow_move+pin_rlm | total | 66-57 | 53.7 | 49.7 | 3.9 | +3.71 | 3.0 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 127-107 | 54.3 | 49.8 | 4.5 | +9.28 | 4.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 39-25 | 60.9 | 49.7 | 11.2 | +10.86 | 17.0 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 64-43 | 59.8 | 49.8 | 10.0 | +15.53 | 14.5 |  |  | PROMOTE: beats break-even and its own base rate |
| money_moving+pin_rlm | total | 75-65 | 53.6 | 49.7 | 3.9 | +3.74 | 2.7 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 122-105 | 53.7 | 49.8 | 4.0 | +6.7 | 3.0 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 78-67 | 53.8 | 49.7 | 4.1 | +4.47 | 3.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 74-58 | 56.1 | 49.7 | 6.3 | +9.87 | 7.5 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 28-21 | 57.1 | 49.8 | 7.4 | +4.4 | 9.0 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 66-57 | 53.7 | 49.7 | 3.9 | +3.71 | 3.0 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 78-67 | 53.8 | 49.7 | 4.1 | +4.47 | 3.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 32-21 | 60.4 | 49.8 | 10.5 | +8.0 | 15.1 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 127-107 | 54.3 | 49.8 | 4.5 | +9.28 | 4.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 48-36 | 57.1 | 49.7 | 7.5 | +8.06 | 9.6 |  |  | no edge shown yet |
| money_delta+rlm_ratio | total | 78-55 | 58.6 | 49.7 | 8.9 | +16.27 | 12.2 |  |  | no edge shown yet |
| money_delta+pin_value | total | 36-29 | 55.4 | 49.8 | 5.5 | +3.51 | 5.4 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 42-59 | 41.6 | 49.8 | -8.2 | -20.45 | -20.3 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | total | 22-30 | 42.3 | 49.7 | -7.4 | -9.86 | -19.0 |  |  | no edge shown yet |
| rlm_quiet+rlm_ratio | total | 43-57 | 43.0 | 49.7 | -6.7 | -17.59 | -17.6 |  |  | DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 49.6 | 50.4 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| rlm_quiet | close | 1-3k bets | 128-192 | 40.0 | -1.6 | -7.6 |  |
| rlm_quiet | close | 3k+ bets | 45-65 | 40.9 | -1.5 | -11.0 |  |
| rlm_quiet | close | <1k bets | 22-28 | 44.0 | 2.6 | -6.0 |  |
| rlm_quiet | close | pin $1-2k | 50-90 | 35.7 | -7.4 | -18.9 |  |
| rlm_quiet | close | pin $2k+ | 55-66 | 45.5 | 7.6 | 5.9 |  |
| rlm_quiet | close | pin limit <$1k | 39-39 | 50.0 | 0.8 | -4.1 |  |
| pin_move | close | 1-3k bets | 328-327 | 50.1 | 0.2 | -2.8 |  |
| pin_move | close | 3k+ bets | 124-125 | 49.8 | 0.1 | -3.7 |  |
| pin_move | close | <1k bets | 67-68 | 49.6 | -0.9 | -4.6 |  |
| pin_move | close | pin $1-2k | 242-240 | 50.2 | -0.0 | -1.7 |  |
| pin_move | close | pin $2k+ | 185-189 | 49.5 | -0.3 | -6.1 |  |
| pin_move | close | pin limit <$1k | 92-91 | 50.3 | 0.8 | -1.4 |  |
| money_delta | close | 1-3k bets | 209-267 | 43.9 | -0.7 | -7.3 |  |
| money_delta | close | 3k+ bets | 83-111 | 42.8 | -0.4 | -2.1 |  |
| money_delta | close | <1k bets | 38-62 | 38.0 | -4.0 | -22.9 |  |
| money_delta | close | pin $1-2k | 117-122 | 49.0 | 3.2 | 2.2 |  |
| money_delta | close | pin $2k+ | 83-113 | 42.3 | 1.3 | -9.7 |  |
| money_delta | close | pin limit <$1k | 53-56 | 48.6 | -0.6 | -2.8 |  |
| pin_rlm | close | 1-3k bets | 88-98 | 47.3 | 4.7 | 14.9 |  |
| pin_rlm | close | 3k+ bets | 34-44 | 43.6 | 1.7 | -4.8 |  |
| pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.7 | 11.0 |  |
| pin_rlm | close | pin $1-2k | 62-66 | 48.4 | 4.9 | 11.5 |  |
| pin_rlm | close | pin $2k+ | 39-65 | 37.5 | 1.8 | -1.6 |  |
| pin_rlm | close | pin limit <$1k | 42-32 | 56.8 | 8.2 | 20.9 |  |
| follow_move | close | 1-3k bets | 582-523 | 52.7 | 1.2 | -4.5 |  |
| follow_move | close | 3k+ bets | 198-184 | 51.8 | -0.1 | -5.1 |  |
| follow_move | close | <1k bets | 120-108 | 52.6 | -0.5 | -11.2 |  |
| follow_move | close | pin $1-2k | 271-298 | 47.6 | -3.5 | -11.1 |  |
| follow_move | close | pin $2k+ | 232-190 | 55.0 | 3.0 | -0.5 |  |
| follow_move | close | pin limit <$1k | 112-110 | 50.5 | 0.6 | -3.7 |  |
| rlm_ratio | close | 1-3k bets | 130-168 | 43.6 | -0.6 | -6.5 |  |
| rlm_ratio | close | 3k+ bets | 51-46 | 52.6 | 8.2 | 12.4 |  |
| rlm_ratio | close | <1k bets | 26-26 | 50.0 | 7.2 | 0.8 |  |
| rlm_ratio | close | pin $1-2k | 72-73 | 49.7 | 3.4 | 3.8 |  |
| rlm_ratio | close | pin $2k+ | 39-53 | 42.4 | 4.4 | -6.1 |  |
| rlm_ratio | close | pin limit <$1k | 47-36 | 56.6 | 7.7 | 9.3 |  |
| money_level | close | 1-3k bets | 741-525 | 58.5 | 2.8 | -1.8 |  |
| money_level | close | 3k+ bets | 255-201 | 55.9 | 0.7 | -2.9 |  |
| money_level | close | <1k bets | 145-118 | 55.1 | -0.8 | -11.5 |  |
| money_level | close | pin $1-2k | 336-287 | 53.9 | -0.2 | -4.1 |  |
| money_level | close | pin $2k+ | 287-224 | 56.2 | -1.2 | -7.3 |  |
| money_level | close | pin limit <$1k | 131-128 | 50.6 | 0.2 | -3.9 |  |
| sharp_gap | close | 1-3k bets | 550-658 | 45.5 | -1.9 | -9.1 |  |
| sharp_gap | close | 3k+ bets | 218-229 | 48.8 | 1.3 | 2.4 |  |
| sharp_gap | close | <1k bets | 114-137 | 45.4 | -2.3 | -14.6 |  |
| sharp_gap | close | pin $1-2k | 287-315 | 47.7 | -1.1 | -5.1 |  |
| sharp_gap | close | pin $2k+ | 228-264 | 46.3 | -0.1 | -3.7 |  |
| sharp_gap | close | pin limit <$1k | 119-128 | 48.2 | -1.2 | -4.0 |  |
| money_moving | close | 1-3k bets | 556-657 | 45.8 | -2.1 | -9.5 |  |
| money_moving | close | 3k+ bets | 217-231 | 48.4 | 0.7 | 0.9 |  |
| money_moving | close | <1k bets | 112-137 | 45.0 | -2.4 | -13.5 |  |
| money_moving | close | pin $1-2k | 285-318 | 47.3 | -1.8 | -5.8 |  |
| money_moving | close | pin $2k+ | 229-262 | 46.6 | 0.1 | -3.6 |  |
| money_moving | close | pin limit <$1k | 116-135 | 46.2 | -3.2 | -7.8 |  |
| pin_value | close | 1-3k bets | 241-242 | 49.9 | 2.0 | 4.1 |  |
| pin_value | close | 3k+ bets | 82-87 | 48.5 | -0.1 | -5.0 |  |
| pin_value | close | <1k bets | 54-44 | 55.1 | 7.9 | 10.6 |  |
| pin_value | close | pin $1-2k | 172-191 | 47.4 | -0.9 | -3.8 |  |
| pin_value | close | pin $2k+ | 107-115 | 48.2 | 2.1 | 4.7 |  |
| pin_value | close | pin limit <$1k | 98-67 | 59.4 | 9.5 | 15.3 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.9 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.9 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 235-293 | 44.5 | -3.9 | -11.2 |  |
| consensus_gap | close | 3k+ bets | 83-97 | 46.1 | -1.6 | 4.6 |  |
| consensus_gap | close | <1k bets | 40-78 | 33.9 | -9.8 | -30.7 |  |
| consensus_gap | close | pin $1-2k | 114-126 | 47.5 | -1.9 | -2.2 |  |
| consensus_gap | close | pin $2k+ | 94-106 | 47.0 | -2.9 | -2.8 |  |
| consensus_gap | close | pin limit <$1k | 53-45 | 54.1 | 3.8 | 5.5 |  |
| consensus_gap+follow_move | close | 1-3k bets | 97-90 | 51.9 | 0.1 | -2.7 |  |
| consensus_gap+money_level | close | 1-3k bets | 157-104 | 60.2 | 1.1 | 2.8 |  |
| consensus_gap+money_moving | close | 1-3k bets | 105-162 | 39.3 | -6.3 | -11.6 |  |
| consensus_gap+pin_move | close | 1-3k bets | 58-56 | 50.9 | -0.6 | 3.3 |  |
| consensus_gap+pin_value | close | 1-3k bets | 96-106 | 47.5 | 1.3 | -0.0 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 102-165 | 38.2 | -6.5 | -12.7 |  |
| follow_move+money_level | close | 1-3k bets | 387-266 | 59.3 | 2.9 | -3.1 |  |
| follow_move+money_moving | close | 1-3k bets | 314-337 | 48.2 | -1.1 | -8.1 |  |
| follow_move+pin_move | close | 1-3k bets | 236-240 | 49.6 | -0.6 | -6.0 |  |
| follow_move+pin_value | close | 1-3k bets | 81-80 | 50.3 | 1.8 | 1.4 |  |
| follow_move+sharp_gap | close | 1-3k bets | 316-336 | 48.5 | -0.5 | -6.7 |  |
| money_level+money_moving | close | 1-3k bets | 402-354 | 53.2 | 0.6 | -3.6 |  |
| money_level+pin_move | close | 1-3k bets | 202-181 | 52.7 | -0.1 | -3.8 |  |
| money_level+pin_value | close | 1-3k bets | 118-105 | 52.9 | 3.2 | -0.7 |  |
| money_level+sharp_gap | close | 1-3k bets | 388-346 | 52.9 | 0.7 | -3.2 |  |
| money_moving+pin_move | close | 1-3k bets | 199-214 | 48.2 | -0.8 | -3.1 |  |
| money_moving+pin_value | close | 1-3k bets | 105-128 | 45.1 | -2.4 | -6.7 |  |
| money_moving+sharp_gap | close | 1-3k bets | 526-628 | 45.6 | -2.0 | -8.7 |  |
| pin_move+pin_value | close | 1-3k bets | 107-102 | 51.2 | 2.0 | 0.5 |  |
| pin_move+sharp_gap | close | 1-3k bets | 204-214 | 48.8 | -0.0 | -1.5 |  |
| pin_value+sharp_gap | close | 1-3k bets | 106-131 | 44.7 | -2.5 | -7.5 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 128-192 | 40.0 | -1.6 | -7.6 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 64-114 | 36.0 | -5.2 | -14.8 |  |
| consensus_gap+money_delta | close | 1-3k bets | 27-66 | 29.0 | -8.3 | -22.4 |  |
| follow_move+money_delta | close | 1-3k bets | 101-119 | 45.9 | -0.8 | -8.9 |  |
| money_delta+money_level | close | 1-3k bets | 76-73 | 51.0 | 3.1 | 5.5 |  |
| money_delta+money_moving | close | 1-3k bets | 146-210 | 41.0 | -1.9 | -10.1 |  |
| money_delta+pin_value | close | 1-3k bets | 46-46 | 50.0 | 2.6 | -0.0 |  |
| money_delta+sharp_gap | close | 1-3k bets | 145-207 | 41.2 | -1.7 | -9.6 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 73-80 | 47.7 | 0.5 | 2.0 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 18-28 | 39.1 | 0.3 | 15.8 |  |
| money_level+pin_rlm | close | 1-3k bets | 39-30 | 56.5 | 8.1 | 8.8 |  |
| pin_move+pin_rlm | close | 1-3k bets | 80-81 | 49.7 | 5.2 | 10.7 |  |
| pin_rlm+pin_value | close | 1-3k bets | 29-25 | 53.7 | 7.7 | 28.3 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 88-98 | 47.3 | 4.7 | 14.9 |  |
| money_delta+pin_rlm | close | 1-3k bets | 50-54 | 48.1 | 4.9 | 15.0 |  |
| money_moving+pin_rlm | close | 1-3k bets | 83-94 | 46.9 | 4.2 | 15.1 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 21-33 | 38.9 | -0.8 | 1.7 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 130-168 | 43.6 | -0.6 | -6.5 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 70-82 | 46.1 | 0.5 | -7.3 |  |
| money_level+rlm_ratio | close | 1-3k bets | 60-58 | 50.8 | 1.6 | -1.9 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 124-161 | 43.5 | -0.9 | -6.4 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 130-168 | 43.6 | -0.6 | -6.5 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 15-35 | 30.0 | -5.7 | -10.5 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 57-111 | 33.9 | -7.2 | -18.3 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 52-98 | 34.7 | -4.9 | -14.5 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 57-76 | 42.9 | -1.1 | -8.9 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 35-61 | 36.5 | -7.0 | -23.2 |  |
| follow_move+pin_rlm | close | 1-3k bets | 63-74 | 46.0 | 1.7 | -4.6 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 68-69 | 49.6 | 4.0 | 2.4 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 25-44 | 36.2 | -3.6 | -16.7 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 63-74 | 46.0 | 1.7 | -4.6 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 27-21 | 56.2 | 8.5 | 8.0 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 17-22 | 43.6 | -1.6 | 9.5 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 50.4 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 31-27 | 53.4 | 3.2 | 3.8 |  |
| consensus_gap+money_moving | close | 3k+ bets | 34-54 | 38.6 | -6.0 | 12.1 |  |
| consensus_gap+pin_move | close | 3k+ bets | 21-19 | 52.5 | 2.1 | 6.4 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-6 | 33.3 | -6.7 | 6.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 35-33 | 51.5 | 4.7 | 5.6 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -1.1 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 35-54 | 39.3 | -5.1 | 15.1 |  |
| follow_move+money_moving | close | 3k+ bets | 106-109 | 49.3 | 0.1 | -3.4 |  |
| follow_move+pin_move | close | 3k+ bets | 94-91 | 50.8 | 0.8 | -1.2 |  |
| follow_move+pin_rlm | close | 3k+ bets | 32-30 | 51.6 | 7.7 | 13.7 |  |
| follow_move+pin_value | close | 3k+ bets | 32-32 | 50.0 | 0.2 | -6.2 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 51-46 | 52.6 | 8.2 | 12.4 |  |
| follow_move+sharp_gap | close | 3k+ bets | 108-108 | 50.0 | 1.2 | -1.4 |  |
| money_moving+pin_move | close | 3k+ bets | 72-81 | 47.1 | -1.2 | -6.6 |  |
| money_moving+pin_rlm | close | 3k+ bets | 33-43 | 43.4 | 1.7 | -4.9 |  |
| money_moving+pin_value | close | 3k+ bets | 40-50 | 44.4 | -3.2 | -8.8 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 49-44 | 52.7 | 8.4 | 13.0 |  |
| money_moving+sharp_gap | close | 3k+ bets | 210-221 | 48.7 | 1.2 | 2.2 |  |
| pin_move+pin_rlm | close | 3k+ bets | 32-38 | 45.7 | 2.0 | -0.1 |  |
| pin_move+pin_value | close | 3k+ bets | 32-39 | 45.1 | -4.3 | -15.2 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 34-31 | 52.3 | 7.0 | 13.3 |  |
| pin_move+sharp_gap | close | 3k+ bets | 72-81 | 47.1 | -0.9 | -5.9 |  |
| pin_rlm+pin_value | close | 3k+ bets | 6-14 | 30.0 | -15.8 | -42.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 32-30 | 51.6 | 7.7 | 13.7 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 34-44 | 43.6 | 1.7 | -4.8 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 9-9 | 50.0 | -0.1 | -5.1 |  |
| pin_value+sharp_gap | close | 3k+ bets | 40-49 | 44.9 | -2.7 | -7.8 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 51-46 | 52.6 | 8.2 | 12.4 |  |
| follow_move+money_delta | close | 3k+ bets | 40-49 | 44.9 | -0.3 | -7.0 |  |
| money_level+money_moving | close | 3k+ bets | 148-127 | 53.8 | 1.5 | -0.5 |  |
| money_level+sharp_gap | close | 3k+ bets | 147-124 | 54.2 | 2.1 | 1.0 |  |
| follow_move+money_level | close | 3k+ bets | 124-91 | 57.7 | 1.1 | -2.5 |  |
| money_level+rlm_ratio | close | 3k+ bets | 25-12 | 67.6 | 20.5 | 38.4 |  |
| consensus_gap+money_level | close | 3k+ bets | 46-45 | 50.5 | -6.4 | -12.7 |  |
| money_level+pin_move | close | 3k+ bets | 68-61 | 52.7 | -0.8 | -3.2 |  |
| money_level+pin_value | close | 3k+ bets | 46-44 | 51.1 | 0.6 | -5.2 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 7-12 | 36.8 | -1.0 | -5.4 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 45-65 | 40.9 | -1.5 | -11.0 |  |
| money_delta+money_moving | close | 3k+ bets | 63-84 | 42.9 | 0.7 | 2.9 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 19-26 | 42.2 | 1.0 | -2.3 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 23-35 | 39.7 | -2.4 | -10.9 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 21-34 | 38.2 | -3.8 | -13.1 |  |
| consensus_gap+money_delta | close | 3k+ bets | 12-23 | 34.3 | -4.1 | 18.4 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 10-26 | 27.8 | -15.0 | -38.6 |  |
| money_delta+sharp_gap | close | 3k+ bets | 61-81 | 43.0 | 1.0 | 3.6 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 26-31 | 45.6 | 2.1 | -0.4 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 11-16 | 40.7 | -0.8 | -3.2 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 7-11 | 38.9 | -10.6 | -25.7 |  |
| money_delta+money_level | close | 3k+ bets | 33-22 | 60.0 | 14.0 | 21.2 |  |
| money_level+pin_rlm | close | 3k+ bets | 16-9 | 64.0 | 19.2 | 37.0 |  |
| money_delta+pin_value | close | 3k+ bets | 18-19 | 48.6 | 2.8 | -8.3 |  |
| money_delta+pin_move | close | 3k+ bets | 36-42 | 46.2 | 1.1 | -5.7 |  |
| money_delta+pin_rlm | close | 3k+ bets | 22-27 | 44.9 | 3.2 | -4.5 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 30-25 | 54.5 | 10.0 | 15.6 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 47.9 | 87.7 |  |
| money_level+money_moving | close | <1k bets | 76-77 | 49.7 | -2.7 | -14.4 |  |
| money_level+sharp_gap | close | <1k bets | 79-77 | 50.6 | -2.1 | -13.9 |  |
| money_moving+sharp_gap | close | <1k bets | 110-135 | 44.9 | -2.6 | -14.7 |  |
| consensus_gap+money_level | close | <1k bets | 18-27 | 40.0 | -15.9 | -39.4 |  |
| consensus_gap+money_moving | close | <1k bets | 17-40 | 29.8 | -11.8 | -34.9 |  |
| consensus_gap+pin_move | close | <1k bets | 6-13 | 31.6 | -18.2 | -26.5 |  |
| consensus_gap+pin_value | close | <1k bets | 14-14 | 50.0 | 7.9 | 15.4 |  |
| consensus_gap+sharp_gap | close | <1k bets | 17-41 | 29.3 | -12.0 | -36.0 |  |
| money_level+pin_move | close | <1k bets | 34-35 | 49.3 | -4.9 | -13.5 |  |
| money_level+pin_value | close | <1k bets | 18-17 | 51.4 | 1.0 | -4.2 |  |
| money_moving+pin_move | close | <1k bets | 36-41 | 46.8 | -0.9 | -4.2 |  |
| money_moving+pin_value | close | <1k bets | 17-16 | 51.5 | 6.2 | 14.9 |  |
| pin_move+pin_value | close | <1k bets | 25-20 | 55.6 | 7.3 | 12.9 |  |
| pin_move+sharp_gap | close | <1k bets | 36-42 | 46.2 | -2.1 | -9.5 |  |
| pin_value+sharp_gap | close | <1k bets | 17-15 | 53.1 | 7.3 | 18.5 |  |
| follow_move+money_delta | close | <1k bets | 18-20 | 47.4 | 5.1 | -3.2 |  |
| follow_move+money_moving | close | <1k bets | 54-63 | 46.2 | -3.4 | -13.8 |  |
| follow_move+pin_move | close | <1k bets | 42-42 | 50.0 | -1.2 | -7.2 |  |
| follow_move+sharp_gap | close | <1k bets | 56-63 | 47.1 | -3.2 | -16.1 |  |
| money_delta+money_moving | close | <1k bets | 27-46 | 37.0 | -2.8 | -23.1 |  |
| money_delta+pin_move | close | <1k bets | 13-17 | 43.3 | -0.3 | -15.5 |  |
| money_delta+sharp_gap | close | <1k bets | 27-46 | 37.0 | -2.8 | -23.1 |  |
| follow_move+rlm_quiet | close | <1k bets | 22-28 | 44.0 | 2.6 | -6.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 26-26 | 50.0 | 7.2 | 0.8 |  |
| money_delta+rlm_quiet | close | <1k bets | 8-10 | 44.4 | 5.0 | -4.3 |  |
| money_delta+rlm_ratio | close | <1k bets | 16-15 | 51.6 | 10.2 | 6.3 |  |
| money_moving+rlm_quiet | close | <1k bets | 14-12 | 53.8 | 13.1 | 20.2 |  |
| money_moving+rlm_ratio | close | <1k bets | 26-26 | 50.0 | 7.2 | 0.8 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 10-10 | 50.0 | 10.6 | 5.6 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 13-13 | 50.0 | 8.4 | 3.3 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 26-26 | 50.0 | 7.2 | 0.8 |  |
| follow_move+money_level | close | <1k bets | 75-59 | 56.0 | -2.2 | -15.1 |  |
| consensus_gap+money_delta | close | <1k bets | 4-22 | 15.4 | -16.6 | -63.0 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -1.4 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 12-14 | 46.2 | 8.1 | -0.2 |  |
| money_moving+pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.7 | 11.0 |  |
| pin_rlm+sharp_gap | close | <1k bets | 21-21 | 50.0 | 9.7 | 11.0 |  |
| money_delta+pin_value | close | <1k bets | 6-8 | 42.9 | -3.3 | -19.4 |  |
| consensus_gap+follow_move | close | <1k bets | 9-20 | 31.0 | -19.1 | -51.4 |  |
| follow_move+pin_rlm | close | <1k bets | 16-11 | 59.3 | 16.5 | 17.3 |  |
| follow_move+pin_value | close | <1k bets | 18-12 | 60.0 | 11.2 | 13.8 |  |
| pin_move+pin_rlm | close | <1k bets | 19-16 | 54.3 | 11.3 | 15.0 |  |
| pin_move+rlm_quiet | close | <1k bets | 10-10 | 50.0 | 5.0 | 9.6 |  |
| pin_move+rlm_ratio | close | <1k bets | 16-13 | 55.2 | 10.4 | 7.8 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 21.7 | 60.8 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 7-5 | 58.3 | 16.3 | 15.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 16-11 | 59.3 | 16.5 | 17.3 |  |
| pin_value+rlm_quiet | close | <1k bets | 3-4 | 42.9 | -6.5 | -17.6 |  |
| pin_value+rlm_ratio | close | <1k bets | 4-1 | 80.0 | 31.1 | 51.7 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 2-7 | 22.2 | -12.1 | -57.2 |  |
| money_delta+money_level | close | <1k bets | 12-17 | 41.4 | -1.8 | -18.9 |  |
| money_level+rlm_ratio | close | <1k bets | 13-13 | 50.0 | 5.0 | -1.9 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 18.0 | 19.0 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 0-5 | 0.0 | -35.6 | -100.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 44-50 | 46.8 | -5.7 | -10.6 |  |
| consensus_gap+money_moving | close | pin $1-2k | 56-68 | 45.2 | -3.6 | -4.9 |  |
| consensus_gap+pin_move | close | pin $1-2k | 44-46 | 48.9 | -3.4 | 3.0 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-18 | 41.9 | 1.0 | 25.8 |  |
| consensus_gap+pin_value | close | pin $1-2k | 67-73 | 47.9 | 1.6 | -4.2 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-14 | 50.0 | 4.3 | 9.0 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 53-66 | 44.5 | -2.9 | -4.1 |  |
| follow_move+money_moving | close | pin $1-2k | 157-187 | 45.6 | -4.3 | -10.7 |  |
| follow_move+pin_move | close | pin $1-2k | 170-182 | 48.3 | -2.2 | -7.2 |  |
| follow_move+pin_rlm | close | pin $1-2k | 50-50 | 50.0 | 4.4 | 5.3 |  |
| follow_move+pin_value | close | pin $1-2k | 57-69 | 45.2 | -4.2 | -14.7 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 72-73 | 49.7 | 3.4 | 3.8 |  |
| follow_move+sharp_gap | close | pin $1-2k | 160-186 | 46.2 | -3.5 | -9.9 |  |
| money_moving+pin_move | close | pin $1-2k | 148-164 | 47.4 | -1.8 | -3.6 |  |
| money_moving+pin_rlm | close | pin $1-2k | 59-63 | 48.4 | 4.4 | 11.9 |  |
| money_moving+pin_value | close | pin $1-2k | 68-99 | 40.7 | -7.1 | -20.4 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 70-69 | 50.4 | 3.6 | 5.1 |  |
| money_moving+sharp_gap | close | pin $1-2k | 276-306 | 47.4 | -1.4 | -5.3 |  |
| pin_move+pin_rlm | close | pin $1-2k | 59-60 | 49.6 | 4.7 | 11.6 |  |
| pin_move+pin_value | close | pin $1-2k | 74-89 | 45.4 | -4.2 | -12.5 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 58-54 | 51.8 | 5.1 | 7.2 |  |
| pin_move+sharp_gap | close | pin $1-2k | 151-164 | 47.9 | -1.0 | -3.1 |  |
| pin_rlm+pin_value | close | pin $1-2k | 15-24 | 38.5 | -9.6 | -19.7 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 50-50 | 50.0 | 4.4 | 5.3 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 62-66 | 48.4 | 4.9 | 11.5 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 18-20 | 47.4 | -2.2 | -10.6 |  |
| pin_value+sharp_gap | close | pin $1-2k | 68-97 | 41.2 | -6.5 | -19.4 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 72-73 | 49.7 | 3.4 | 3.8 |  |
| follow_move+money_level | close | pin $1-2k | 187-173 | 51.9 | -2.5 | -8.9 |  |
| money_level+rlm_ratio | close | pin $1-2k | 42-32 | 56.8 | 8.2 | 10.7 |  |
| money_level+sharp_gap | close | pin $1-2k | 208-199 | 51.1 | -0.8 | -5.1 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 4-12 | 25.0 | -16.5 | -28.2 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 50-90 | 35.7 | -7.4 | -18.9 |  |
| money_level+money_moving | close | pin $1-2k | 209-203 | 50.7 | -1.3 | -6.0 |  |
| consensus_gap+money_level | close | pin $1-2k | 68-60 | 53.1 | -4.1 | -6.4 |  |
| money_level+pin_value | close | pin $1-2k | 78-80 | 49.4 | -0.6 | -7.6 |  |
| money_level+pin_move | close | pin $1-2k | 148-136 | 52.1 | -0.7 | -4.7 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 23-38 | 37.7 | -6.0 | -6.4 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 36-51 | 41.4 | -3.7 | -6.6 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 15-27 | 35.7 | -8.0 | -12.8 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 20-33 | 37.7 | -5.0 | -6.9 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 24-40 | 37.5 | -5.8 | -10.1 |  |
| money_level+pin_rlm | close | pin $1-2k | 30-22 | 57.7 | 11.3 | 13.4 |  |
| follow_move+money_delta | close | pin $1-2k | 58-61 | 48.7 | 2.4 | 0.3 |  |
| money_delta+money_moving | close | pin $1-2k | 80-93 | 46.2 | 2.1 | 0.1 |  |
| money_delta+pin_move | close | pin $1-2k | 61-64 | 48.8 | 1.6 | 3.3 |  |
| money_delta+pin_rlm | close | pin $1-2k | 38-41 | 48.1 | 4.7 | 11.0 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 44-40 | 52.4 | 6.5 | 10.0 |  |
| money_delta+sharp_gap | close | pin $1-2k | 80-91 | 46.8 | 2.6 | 1.2 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 47.9 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 44-36 | 55.0 | 7.1 | 7.1 |  |
| consensus_gap+money_delta | close | pin $1-2k | 16-26 | 38.1 | -2.6 | -10.1 |  |
| money_delta+pin_value | close | pin $1-2k | 37-44 | 45.7 | -2.6 | -13.6 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 14-30 | 31.8 | -11.7 | -23.7 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 9-23 | 28.1 | -20.9 | -46.0 |  |
| follow_move+money_level | close | pin $2k+ | 143-90 | 61.4 | 1.9 | -2.1 |  |
| follow_move+money_moving | close | pin $2k+ | 111-108 | 50.7 | 2.6 | -3.3 |  |
| follow_move+pin_move | close | pin $2k+ | 140-127 | 52.4 | 2.2 | -1.5 |  |
| follow_move+sharp_gap | close | pin $2k+ | 112-109 | 50.7 | 2.7 | -3.1 |  |
| money_level+money_moving | close | pin $2k+ | 154-140 | 52.4 | -0.4 | -5.2 |  |
| money_level+pin_move | close | pin $2k+ | 104-90 | 53.6 | -1.8 | -5.7 |  |
| money_level+sharp_gap | close | pin $2k+ | 154-141 | 52.2 | -0.6 | -5.1 |  |
| money_moving+pin_move | close | pin $2k+ | 98-106 | 48.0 | 0.6 | -4.4 |  |
| money_moving+sharp_gap | close | pin $2k+ | 223-258 | 46.4 | -0.0 | -3.5 |  |
| pin_move+sharp_gap | close | pin $2k+ | 98-107 | 47.8 | 0.3 | -4.4 |  |
| consensus_gap+money_delta | close | pin $2k+ | 7-25 | 21.9 | -10.1 | -56.9 |  |
| consensus_gap+money_moving | close | pin $2k+ | 32-62 | 34.0 | -10.0 | -9.4 |  |
| consensus_gap+pin_value | close | pin $2k+ | 40-47 | 46.0 | 3.6 | 10.3 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 34-65 | 34.3 | -10.3 | -8.8 |  |
| money_delta+money_moving | close | pin $2k+ | 57-81 | 41.3 | 2.9 | -8.2 |  |
| money_delta+pin_value | close | pin $2k+ | 18-21 | 46.2 | 3.6 | -11.8 |  |
| money_delta+sharp_gap | close | pin $2k+ | 55-80 | 40.7 | 2.2 | -9.2 |  |
| money_moving+pin_value | close | pin $2k+ | 55-66 | 45.5 | 0.3 | 4.0 |  |
| pin_value+sharp_gap | close | pin $2k+ | 55-67 | 45.1 | 0.1 | 3.2 |  |
| consensus_gap+pin_move | close | pin $2k+ | 26-31 | 45.6 | -4.7 | -14.3 |  |
| money_delta+pin_move | close | pin $2k+ | 31-44 | 41.3 | -1.1 | -14.8 |  |
| consensus_gap+follow_move | close | pin $2k+ | 29-26 | 52.7 | -0.0 | -12.1 |  |
| follow_move+pin_value | close | pin $2k+ | 35-30 | 53.8 | 6.9 | 16.8 |  |
| pin_move+pin_value | close | pin $2k+ | 48-45 | 51.6 | 3.9 | 1.1 |  |
| follow_move+money_delta | close | pin $2k+ | 31-39 | 44.3 | 2.4 | -8.0 |  |
| follow_move+pin_rlm | close | pin $2k+ | 28-41 | 40.6 | 3.1 | -7.3 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 39-53 | 42.4 | 4.4 | -6.1 |  |
| money_delta+money_level | close | pin $2k+ | 25-20 | 55.6 | 11.9 | 12.4 |  |
| money_delta+pin_rlm | close | pin $2k+ | 21-36 | 36.8 | 1.3 | -8.3 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 19-24 | 44.2 | 5.5 | -4.0 |  |
| money_level+pin_rlm | close | pin $2k+ | 15-10 | 60.0 | 16.4 | 27.1 |  |
| money_level+pin_value | close | pin $2k+ | 55-51 | 51.9 | 2.1 | -4.1 |  |
| money_level+rlm_ratio | close | pin $2k+ | 14-12 | 53.8 | 8.3 | 13.1 |  |
| money_moving+pin_rlm | close | pin $2k+ | 39-65 | 37.5 | 1.8 | -1.6 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 39-52 | 42.9 | 4.7 | -5.0 |  |
| pin_move+pin_rlm | close | pin $2k+ | 31-43 | 41.9 | 3.8 | -1.9 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 27-35 | 43.5 | 3.7 | -0.6 |  |
| pin_rlm+pin_value | close | pin $2k+ | 6-13 | 31.6 | -4.3 | 13.6 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 28-41 | 40.6 | 3.1 | -7.3 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 39-65 | 37.5 | 1.8 | -1.6 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 4-6 | 40.0 | -0.9 | -19.0 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 39-53 | 42.4 | 4.4 | -6.1 |  |
| consensus_gap+money_level | close | pin $2k+ | 60-48 | 55.6 | -7.3 | -13.2 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 55-66 | 45.5 | 7.6 | 5.9 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 16-21 | 43.2 | 4.8 | -10.0 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 26-37 | 41.3 | 5.7 | -7.2 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 13-27 | 32.5 | 0.2 | -20.0 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 20-33 | 37.7 | 5.2 | -11.5 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 26-38 | 40.6 | 5.2 | -8.6 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-20 | 16.7 | -14.1 | -27.9 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 4-12 | 25.0 | -3.1 | -46.7 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-11 | 0.0 | -29.1 | -100.0 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 35-43 | 44.9 | 5.0 | -2.0 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 5-7 | 41.7 | 5.6 | 64.1 |  |
| follow_move+money_delta | close | pin limit <$1k | 34-38 | 47.2 | -1.9 | -9.4 |  |
| money_level+money_moving | close | pin limit <$1k | 71-81 | 46.7 | -3.0 | -10.4 |  |
| money_level+sharp_gap | close | pin limit <$1k | 68-74 | 47.9 | -1.8 | -8.1 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 107-119 | 47.3 | -2.0 | -5.2 |  |
| consensus_gap+money_level | close | pin limit <$1k | 29-26 | 52.7 | 1.9 | -2.5 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 15-11 | 57.7 | 9.5 | 25.7 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 38-33 | 53.5 | 3.8 | 6.9 |  |
| follow_move+money_moving | close | pin limit <$1k | 68-77 | 46.9 | -2.4 | -9.9 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 73-76 | 49.0 | -0.3 | -5.9 |  |
| money_level+pin_move | close | pin limit <$1k | 52-51 | 50.5 | 0.6 | -3.6 |  |
| money_level+pin_value | close | pin limit <$1k | 49-35 | 58.3 | 8.2 | 10.4 |  |
| pin_move+pin_value | close | pin limit <$1k | 42-27 | 60.9 | 11.1 | 22.1 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 20-11 | 64.5 | 14.9 | 19.2 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 24-19 | 55.8 | 6.9 | 16.0 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 26-19 | 57.8 | 8.8 | 19.1 |  |
| follow_move+money_level | close | pin limit <$1k | 56-57 | 49.6 | -0.7 | -5.7 |  |
| follow_move+pin_move | close | pin limit <$1k | 62-64 | 49.2 | -0.3 | -5.7 |  |
| follow_move+pin_value | close | pin limit <$1k | 39-25 | 60.9 | 11.1 | 15.6 |  |
| money_moving+pin_move | close | pin limit <$1k | 61-66 | 48.0 | -1.3 | -4.6 |  |
| money_moving+pin_value | close | pin limit <$1k | 39-29 | 57.4 | 7.7 | 15.3 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 63-66 | 48.8 | -0.4 | -3.1 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 40-31 | 56.3 | 6.7 | 13.1 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 39-39 | 50.0 | 0.8 | -4.1 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 27-27 | 50.0 | 1.1 | -4.0 |  |
| money_delta+money_moving | close | pin limit <$1k | 46-46 | 50.0 | 0.9 | 0.6 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 9-6 | 60.0 | 13.2 | 43.2 |  |
| money_delta+money_level | close | pin limit <$1k | 25-20 | 55.6 | 5.8 | 6.4 |  |
| money_delta+pin_value | close | pin limit <$1k | 15-8 | 65.2 | 16.2 | 42.9 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 45-44 | 50.6 | 1.6 | 1.7 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 30-31 | 49.2 | 0.5 | 1.6 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 7-3 | 70.0 | 24.6 | 77.3 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 25-18 | 58.1 | 10.0 | 21.9 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 39-30 | 56.5 | 8.1 | 21.3 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 41-32 | 56.2 | 7.4 | 13.8 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-5 | 79.2 | 30.3 | 69.5 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 42-32 | 56.8 | 8.2 | 20.9 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 6-1 | 85.7 | 39.1 | 63.9 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 13-7 | 65.0 | 15.2 | 24.4 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 11-17 | 39.3 | -8.9 | -24.5 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 22-23 | 48.9 | 0.0 | -6.1 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 33-24 | 57.9 | 8.9 | 11.5 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 47-36 | 56.6 | 7.7 | 9.3 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 28-22 | 56.0 | 7.2 | 7.7 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 21-26 | 44.7 | -4.1 | -14.1 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 43-34 | 55.8 | 7.0 | 7.9 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 33-24 | 57.9 | 8.9 | 11.5 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 15-11 | 57.7 | 9.7 | 11.0 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 33-24 | 57.9 | 8.9 | 11.5 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 23-19 | 54.8 | 6.1 | 5.1 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 47-36 | 56.6 | 7.7 | 9.3 |  |
| money_level+pin_rlm | close | pin limit <$1k | 19-13 | 59.4 | 9.7 | 13.9 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 21-15 | 58.3 | 9.3 | 13.5 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 18-5 | 78.3 | 28.4 | 49.8 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 7-3 | 70.0 | 22.3 | 33.8 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 50.4 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -3.7 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -51.3 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 31-33 | 48.4 | 13.1 | 17.9 | 0.04 |
| rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -14.3 | -3.3 | -0.95 |
| rlm_quiet | early | pin limit <$1k | 5-7 | 41.7 | -2.4 | -15.0 | 0.27 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.4 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 5-8 | 38.5 | -9.6 | -31.5 | 0.32 |
| pin_move | early | pin $1-2k | 0-3 | 0.0 | -35.2 | -100.0 | 0.23 |
| pin_move | early | pin limit <$1k | 5-6 | 45.5 | -6.3 | -19.1 | 0.22 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 8-6 | 57.1 | 17.3 | 26.7 | -0.34 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -39.5 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 4-0 | 100.0 | 50.6 | 88.0 | -0.25 |
| pin_rlm | early | <1k bets | 1-2 | 33.3 | 6.5 | -35.8 | -1.0 |
| pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -26.8 | -100.0 | -1.75 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.2 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.3 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -51.3 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 407-343 | 54.3 | 2.2 | -5.2 | 0.17 |
| follow_move | early | pin $1-2k | 28-16 | 63.6 | 10.0 | 14.9 | -0.34 |
| follow_move | early | pin limit <$1k | 47-39 | 54.7 | 4.4 | 1.9 | -0.11 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 26-17 | 60.5 | 22.5 | 31.7 | 0.46 |
| rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.1 | 55.6 | -1.52 |
| rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.4 | 77.5 | 0.29 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 1.1 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 43.1 | 59.7 | 0.33 |
| money_level | early | <1k bets | 150-97 | 60.7 | 0.8 | -5.0 | -0.07 |
| money_level | early | pin $1-2k | 20-8 | 71.4 | 5.9 | 4.1 | 0.01 |
| money_level | early | pin limit <$1k | 24-26 | 48.0 | -5.2 | -11.4 | 0.22 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.6 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.4 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 123-105 | 53.9 | 5.4 | 3.8 | 0.35 |
| sharp_gap | early | pin $1-2k | 15-11 | 57.7 | 4.8 | 6.7 | -0.39 |
| sharp_gap | early | pin limit <$1k | 29-18 | 61.7 | 13.2 | 27.9 | 0.12 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.6 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 51.3 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 85-75 | 53.1 | 1.3 | -7.1 | 0.09 |
| money_moving | early | pin $1-2k | 8-8 | 50.0 | -8.4 | -31.4 | 0.21 |
| money_moving | early | pin limit <$1k | 23-9 | 71.9 | 22.8 | 52.0 | 0.42 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.8 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 36-40 | 47.4 | -1.0 | -10.4 | 0.12 |
| pin_value | early | pin $1-2k | 13-19 | 40.6 | -5.1 | -23.6 | 0.12 |
| pin_value | early | pin limit <$1k | 36-30 | 54.5 | 4.9 | 3.2 | 0.09 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -50.4 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -26.5 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.3 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.7 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 187-239 | 43.9 | -4.0 | -13.1 | 0.39 |
| consensus_gap | early | pin $1-2k | 12-20 | 37.5 | -7.9 | -28.2 | 0.51 |
| consensus_gap | early | pin limit <$1k | 18-34 | 34.6 | -15.6 | -28.2 | 0.28 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -1.3 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.3 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 5.2 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.3 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 17.0 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.5 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.8 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.4 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -1.1 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 3.6 | -6.9 | 0.3 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -0.5 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-6 | 53.8 | 6.7 | 0.8 | -0.31 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -3.7 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.4 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.0 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.5 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 2.9 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.6 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.9 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.7 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.1 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 50.9 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.6 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 50.9 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 52.1 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 12.0 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 18.9 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 17.3 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 17.3 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -26.8 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| follow_move+rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -51.3 | -100.0 | -0.5 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 51.3 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.1 | 83.3 | 1.0 |
| rlm_quiet+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| rlm_quiet+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.1 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 38.6 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 50.4 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 28-34 | 45.2 | -7.2 | -18.5 | 0.76 |
| consensus_gap+money_level | early | <1k bets | 31-22 | 58.5 | -7.6 | -10.1 | 0.44 |
| consensus_gap+sharp_gap | early | <1k bets | 23-38 | 37.7 | -9.4 | -17.1 | 1.02 |
| follow_move+money_level | early | <1k bets | 78-36 | 68.4 | 7.2 | 0.9 | 0.01 |
| follow_move+sharp_gap | early | <1k bets | 67-32 | 67.7 | 17.6 | 20.0 | 0.41 |
| money_level+sharp_gap | early | <1k bets | 82-49 | 62.6 | 5.8 | 2.1 | 0.22 |
| follow_move+money_moving | early | <1k bets | 45-27 | 62.5 | 9.1 | 8.8 | 0.33 |
| money_level+money_moving | early | <1k bets | 53-38 | 58.2 | -0.9 | -8.3 | -0.13 |
| money_moving+sharp_gap | early | <1k bets | 50-43 | 53.8 | 3.9 | -3.5 | 0.25 |
| consensus_gap+money_moving | early | <1k bets | 12-19 | 38.7 | -11.2 | -38.8 | 0.25 |
| follow_move+pin_value | early | <1k bets | 13-11 | 54.2 | 4.3 | 1.3 | -0.01 |
| follow_move+rlm_quiet | early | <1k bets | 31-33 | 48.4 | 13.1 | 17.9 | 0.04 |
| money_moving+rlm_quiet | early | <1k bets | 12-9 | 57.1 | 20.7 | 36.4 | 0.38 |
| rlm_quiet+sharp_gap | early | <1k bets | 19-13 | 59.4 | 22.7 | 31.0 | -0.23 |
| follow_move+rlm_ratio | early | <1k bets | 26-17 | 60.5 | 22.5 | 31.7 | 0.46 |
| rlm_quiet+rlm_ratio | early | <1k bets | 17-10 | 63.0 | 26.1 | 41.1 | -0.24 |
| rlm_ratio+sharp_gap | early | <1k bets | 26-17 | 60.5 | 22.5 | 31.7 | 0.46 |
| pin_move+pin_value | early | <1k bets | 1-4 | 20.0 | -29.2 | -61.8 | 0.2 |
| follow_move+pin_move | early | <1k bets | 5-3 | 62.5 | 10.5 | 11.2 | 0.42 |
| consensus_gap+pin_value | early | <1k bets | 13-23 | 36.1 | -10.5 | -32.5 | 0.4 |
| pin_value+rlm_quiet | early | <1k bets | 0-3 | 0.0 | -42.8 | -100.0 | -0.6 |
| money_delta+money_moving | early | <1k bets | 7-6 | 53.8 | 14.7 | 21.7 | -0.36 |
| money_delta+sharp_gap | early | <1k bets | 6-4 | 60.0 | 21.7 | 39.1 | -0.47 |
| consensus_gap+pin_move | early | <1k bets | 0-5 | 0.0 | -44.5 | -100.0 | 0.26 |
| money_level+pin_move | early | <1k bets | 2-2 | 50.0 | -5.9 | -21.8 | 0.1 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -26.8 | -100.0 | -4.8 |
| consensus_gap+rlm_quiet | early | <1k bets | 3-5 | 37.5 | -0.7 | -22.7 | 1.01 |
| consensus_gap+rlm_ratio | early | <1k bets | 4-3 | 57.1 | 17.3 | 15.6 | 0.6 |
| follow_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 23.2 | -3.7 | -2.15 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -26.8 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | <1k bets | 0-1 | 0.0 | -26.8 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 23.2 | -3.7 | -2.15 |
| pin_rlm+sharp_gap | early | <1k bets | 1-2 | 33.3 | 6.5 | -35.8 | -1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 11.8 | -4.5 | -1.9 |
| pin_value+sharp_gap | early | <1k bets | 5-4 | 55.6 | 8.3 | 6.1 | -0.09 |
| money_level+pin_value | early | <1k bets | 4-4 | 50.0 | -0.1 | -4.5 | 0.88 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -50.9 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -49.6 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 1-2 | 33.3 | -17.4 | -36.4 | 1.33 |
| money_level+rlm_ratio | early | <1k bets | 7-7 | 50.0 | 11.6 | 4.8 | 1.93 |
| money_moving+rlm_ratio | early | <1k bets | 11-7 | 61.1 | 19.0 | 36.3 | 0.47 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 49.6 | 90.9 | 0.0 |
| money_delta+money_level | early | <1k bets | 3-1 | 75.0 | 30.9 | 61.5 | 1.2 |
| pin_move+sharp_gap | early | <1k bets | 2-1 | 66.7 | 16.5 | 4.3 | -0.07 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 73.2 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 73.2 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 73.2 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 3-3 | 50.0 | 11.8 | 37.5 | 0.07 |
| money_delta+rlm_quiet | early | <1k bets | 1-2 | 33.3 | -1.1 | 23.3 | -2.8 |
| money_delta+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 32.3 | 111.3 | 0.87 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 50.4 | 90.9 | -1.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -26.8 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 5-4 | 55.6 | -9.2 | -12.6 | 0.71 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -31.4 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 5-10 | 33.3 | -8.1 | -38.7 | 0.31 |
| follow_move+rlm_quiet | early | pin $1-2k | 1-5 | 16.7 | -14.3 | -3.3 | -0.95 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.1 | 55.6 | -1.52 |
| follow_move+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 13.9 | 37.5 | -0.83 |
| money_level+money_moving | early | pin $1-2k | 8-5 | 61.5 | -4.2 | -15.6 | 0.07 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.7 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -8.1 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -8.1 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-3 | 40.0 | 3.1 | 55.6 | -1.52 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -39.5 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -52.1 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -39.5 | -100.0 | 2.5 |
| money_level+sharp_gap | early | pin $1-2k | 12-4 | 75.0 | 10.5 | 12.5 | -0.26 |
| money_moving+sharp_gap | early | pin $1-2k | 4-6 | 40.0 | -16.7 | -45.4 | 0.08 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.9 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 4-6 | 40.0 | -10.0 | -31.3 | 0.34 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 0-3 | 0.0 | -26.8 | -100.0 | -0.97 |
| follow_move+pin_value | early | pin $1-2k | 6-5 | 54.5 | 7.0 | 0.8 | -0.3 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -26.8 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 11-4 | 73.3 | 8.3 | 6.6 | -0.07 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 47.9 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 4-1 | 80.0 | 11.9 | 6.9 | -0.18 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.8 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -26.8 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -16.7 | -46.8 | -0.12 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.8 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -26.8 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | pin $1-2k | 0-1 | 0.0 | -26.8 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -26.8 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -26.8 | -100.0 | -1.75 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -26.8 | -100.0 | -4.8 |
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -26.8 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -26.8 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin limit <$1k | 5-7 | 41.7 | -2.4 | -15.0 | 0.27 |
| money_level+money_moving | early | pin limit <$1k | 13-7 | 65.0 | 12.8 | 20.2 | 0.48 |
| money_level+sharp_gap | early | pin limit <$1k | 20-16 | 55.6 | 5.0 | 1.6 | 0.14 |
| money_moving+sharp_gap | early | pin limit <$1k | 18-5 | 78.3 | 30.3 | 70.1 | 0.35 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -50.4 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 9-6 | 60.0 | 10.1 | 13.8 | 0.33 |
| money_moving+pin_value | early | pin limit <$1k | 7-4 | 63.6 | 13.9 | 20.1 | 0.18 |
| pin_value+sharp_gap | early | pin limit <$1k | 12-6 | 66.7 | 16.9 | 26.4 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-9 | 40.0 | -12.2 | -25.7 | 0.53 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -26.5 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 14-18 | 43.8 | -5.3 | -17.9 | 0.43 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.1 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 11-11 | 50.0 | -3.8 | -7.4 | -0.04 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 4.4 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 13-7 | 65.0 | 16.5 | 24.2 | -0.07 |
| follow_move+rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.4 | 77.5 | 0.29 |
| money_level+rlm_ratio | early | pin limit <$1k | 6-0 | 100.0 | 54.1 | 92.6 | 0.42 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 16.8 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 7-1 | 87.5 | 43.4 | 77.5 | 0.29 |
| consensus_gap+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 50.9 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 22.7 | 72.3 | 0.54 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 1.3 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 50.9 | 85.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 9-3 | 75.0 | 25.6 | 43.3 | 0.33 |
| money_delta+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_delta+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 52.1 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 3-1 | 75.0 | 25.6 | 41.3 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.0 | 45.3 | -0.5 |
| money_delta+sharp_gap | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 | -0.5 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 11.4 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 24.4 | 51.6 | -0.07 |
| pin_move+pin_value | early | pin limit <$1k | 1-4 | 20.0 | -29.2 | -61.8 | 0.2 |
| follow_move+pin_move | early | pin limit <$1k | 5-3 | 62.5 | 10.5 | 11.2 | 0.42 |
| consensus_gap+pin_move | early | pin limit <$1k | 0-3 | 0.0 | -56.3 | -100.0 | 0.53 |
| money_level+pin_move | early | pin limit <$1k | 2-2 | 50.0 | -5.9 | -21.8 | 0.1 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -49.6 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -49.6 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 16.5 | 4.3 | -0.07 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.2 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.2 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 73.2 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 73.2 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 73.2 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 73.2 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 50.4 | 90.9 | -1.0 |
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
| rlm_quiet | close | 1-3k bets | 12-23 | 34.3 | -3.4 | -2.1 |  |
| rlm_quiet | close | 3k+ bets | 1-5 | 16.7 | -19.1 | -59.7 |  |
| rlm_quiet | close | pin $1-2k | 4-10 | 28.6 | -10.0 | -39.1 |  |
| rlm_quiet | close | pin $2k+ | 4-4 | 50.0 | 10.2 | 124.1 |  |
| rlm_quiet | close | pin limit <$1k | 3-3 | 50.0 | 10.3 | -3.0 |  |
| pin_move | close | 1-3k bets | 20-24 | 45.5 | -3.6 | -15.9 |  |
| pin_move | close | 3k+ bets | 4-2 | 66.7 | 23.1 | 32.6 |  |
| pin_move | close | pin $1-2k | 8-14 | 36.4 | -9.5 | -30.4 |  |
| pin_move | close | pin $2k+ | 11-6 | 64.7 | 12.3 | 18.0 |  |
| pin_move | close | pin limit <$1k | 5-6 | 45.5 | -1.8 | -12.8 |  |
| money_delta | close | 1-3k bets | 10-15 | 40.0 | 1.7 | -22.9 |  |
| money_delta | close | 3k+ bets | 4-2 | 66.7 | 24.0 | 37.0 |  |
| money_delta | close | pin $1-2k | 5-7 | 41.7 | 4.7 | -19.0 |  |
| money_delta | close | pin $2k+ | 1-3 | 25.0 | -13.2 | -52.3 |  |
| money_delta | close | pin limit <$1k | 3-2 | 60.0 | 19.6 | 15.6 |  |
| pin_rlm | close | 1-3k bets | 1-6 | 14.3 | -24.8 | -71.4 |  |
| pin_rlm | close | 3k+ bets | 2-0 | 100.0 | 66.9 | 114.6 |  |
| pin_rlm | close | pin $1-2k | 1-2 | 33.3 | -0.7 | -34.9 |  |
| pin_rlm | close | pin $2k+ | 1-1 | 50.0 | 0.0 | 17.0 |  |
| pin_rlm | close | pin limit <$1k | 1-3 | 25.0 | -9.5 | -50.0 |  |
| follow_move | close | 1-3k bets | 35-44 | 44.3 | -4.3 | -5.6 |  |
| follow_move | close | 3k+ bets | 8-7 | 53.3 | 3.9 | -3.4 |  |
| follow_move | close | pin $1-2k | 12-18 | 40.0 | -8.0 | -22.9 |  |
| follow_move | close | pin $2k+ | 15-9 | 62.5 | 13.6 | 55.5 |  |
| follow_move | close | pin limit <$1k | 7-6 | 53.8 | 4.0 | 2.9 |  |
| rlm_ratio | close | 1-3k bets | 4-13 | 23.5 | -11.7 | -54.5 |  |
| rlm_ratio | close | 3k+ bets | 3-2 | 60.0 | 20.7 | 24.0 |  |
| rlm_ratio | close | pin $1-2k | 2-2 | 50.0 | 15.5 | -2.4 |  |
| rlm_ratio | close | pin $2k+ | 1-3 | 25.0 | -9.3 | -41.5 |  |
| rlm_ratio | close | pin limit <$1k | 3-2 | 60.0 | 19.6 | 15.6 |  |
| money_level | close | 1-3k bets | 46-32 | 59.0 | -1.2 | -0.9 |  |
| money_level | close | 3k+ bets | 11-8 | 57.9 | -1.0 | 1.1 |  |
| money_level | close | pin $1-2k | 19-11 | 63.3 | 4.4 | 12.9 |  |
| money_level | close | pin $2k+ | 12-11 | 52.2 | -6.3 | -13.3 |  |
| money_level | close | pin limit <$1k | 7-7 | 50.0 | -7.7 | -5.3 |  |
| sharp_gap | close | 1-3k bets | 27-38 | 41.5 | -8.1 | -23.9 |  |
| sharp_gap | close | 3k+ bets | 8-11 | 42.1 | -5.9 | -19.4 |  |
| sharp_gap | close | pin $1-2k | 12-13 | 48.0 | -4.0 | -11.0 |  |
| sharp_gap | close | pin $2k+ | 7-14 | 33.3 | -16.4 | -39.6 |  |
| sharp_gap | close | pin limit <$1k | 4-6 | 40.0 | -4.8 | -23.5 |  |
| money_moving | close | 1-3k bets | 30-38 | 44.1 | -6.9 | -21.2 |  |
| money_moving | close | 3k+ bets | 8-11 | 42.1 | -5.9 | -19.4 |  |
| money_moving | close | pin $1-2k | 13-12 | 52.0 | -1.6 | -6.5 |  |
| money_moving | close | pin $2k+ | 7-14 | 33.3 | -16.4 | -39.6 |  |
| money_moving | close | pin limit <$1k | 6-7 | 46.2 | -3.1 | -12.1 |  |
| pin_value | close | 1-3k bets | 24-14 | 63.2 | 12.3 | 49.6 |  |
| pin_value | close | 3k+ bets | 2-2 | 50.0 | -4.5 | -4.9 |  |
| pin_value | close | pin $1-2k | 10-9 | 52.6 | 2.3 | 10.4 |  |
| pin_value | close | pin $2k+ | 10-3 | 76.9 | 27.0 | 118.0 |  |
| pin_value | close | pin limit <$1k | 6-4 | 60.0 | 5.4 | 13.4 |  |
| consensus_gap | close | 1-3k bets | 25-18 | 58.1 | 2.9 | 1.4 |  |
| consensus_gap | close | 3k+ bets | 2-2 | 50.0 | -8.4 | -20.4 |  |
| consensus_gap | close | pin $1-2k | 7-6 | 53.8 | -5.6 | -5.6 |  |
| consensus_gap | close | pin $2k+ | 12-4 | 75.0 | 15.5 | 28.2 |  |
| consensus_gap | close | pin limit <$1k | 4-2 | 66.7 | 17.6 | 27.6 |  |
| follow_move+pin_move | close | 1-3k bets | 14-20 | 41.2 | -8.1 | -24.2 |  |
| money_delta+money_moving | close | 1-3k bets | 7-8 | 46.7 | 8.7 | -10.3 |  |
| money_delta+sharp_gap | close | 1-3k bets | 7-7 | 50.0 | 11.9 | -3.9 |  |
| money_moving+sharp_gap | close | 1-3k bets | 26-36 | 41.9 | -8.1 | -23.3 |  |
| consensus_gap+money_level | close | 1-3k bets | 16-10 | 61.5 | -3.4 | 2.5 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 12-23 | 34.3 | -3.4 | -2.1 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 5-10 | 33.3 | -6.5 | -35.2 |  |
| consensus_gap+follow_move | close | 1-3k bets | 9-10 | 47.4 | -5.3 | -15.3 |  |
| follow_move+money_level | close | 1-3k bets | 16-14 | 53.3 | -7.1 | -9.8 |  |
| money_level+money_moving | close | 1-3k bets | 23-21 | 52.3 | -5.4 | -8.7 |  |
| money_level+sharp_gap | close | 1-3k bets | 20-20 | 50.0 | -6.7 | -9.9 |  |
| consensus_gap+money_moving | close | 1-3k bets | 7-12 | 36.8 | -18.5 | -34.2 |  |
| consensus_gap+pin_move | close | 1-3k bets | 5-5 | 50.0 | 0.0 | -9.3 |  |
| consensus_gap+pin_value | close | 1-3k bets | 12-7 | 63.2 | 10.5 | 18.2 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 6-12 | 33.3 | -19.4 | -36.9 |  |
| follow_move+money_moving | close | 1-3k bets | 12-20 | 37.5 | -12.2 | -34.5 |  |
| follow_move+pin_value | close | 1-3k bets | 8-6 | 57.1 | 5.7 | 77.2 |  |
| follow_move+sharp_gap | close | 1-3k bets | 13-21 | 38.2 | -10.3 | -32.7 |  |
| money_level+pin_move | close | 1-3k bets | 9-9 | 50.0 | -6.6 | -10.8 |  |
| money_level+pin_value | close | 1-3k bets | 8-7 | 53.3 | -3.9 | 0.1 |  |
| money_moving+pin_move | close | 1-3k bets | 7-10 | 41.2 | -9.7 | -22.4 |  |
| money_moving+pin_value | close | 1-3k bets | 6-9 | 40.0 | -13.5 | -24.7 |  |
| pin_move+pin_value | close | 1-3k bets | 8-6 | 57.1 | 5.9 | 6.9 |  |
| pin_move+sharp_gap | close | 1-3k bets | 5-11 | 31.2 | -16.6 | -41.2 |  |
| pin_value+sharp_gap | close | 1-3k bets | 5-8 | 38.5 | -13.4 | -27.8 |  |
| follow_move+money_delta | close | 1-3k bets | 6-10 | 37.5 | -0.9 | -27.3 |  |
| money_delta+pin_move | close | 1-3k bets | 3-3 | 50.0 | 15.0 | -1.6 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 4-8 | 33.3 | -2.7 | -34.9 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 4-13 | 23.5 | -11.7 | -54.5 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 2-8 | 20.0 | -12.5 | -60.9 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 4-11 | 26.7 | -9.2 | -48.5 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 2-10 | 16.7 | -15.5 | -67.4 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 2-10 | 16.7 | -15.5 | -67.4 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 4-13 | 23.5 | -11.7 | -54.5 |  |
| money_delta+money_level | close | 1-3k bets | 2-1 | 66.7 | 27.4 | 28.7 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 3-5 | 37.5 | 2.9 | -27.3 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 2-3 | 40.0 | 8.6 | -21.8 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 4-5 | 44.4 | 6.1 | -14.1 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 1-2 | 33.3 | -12.0 | -33.3 |  |
| money_level+pin_rlm | close | 1-3k bets | 0-2 | 0.0 | -52.8 | -100.0 |  |
| money_moving+pin_rlm | close | 1-3k bets | 1-5 | 16.7 | -23.9 | -66.7 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 1-6 | 14.3 | -24.8 | -71.4 |  |
| money_level+rlm_ratio | close | 1-3k bets | 1-2 | 33.3 | -0.7 | -34.9 |  |
| consensus_gap+money_delta | close | 1-3k bets | 2-1 | 66.7 | 34.5 | 30.3 |  |
| follow_move+pin_rlm | close | 1-3k bets | 1-4 | 20.0 | -13.7 | -60.0 |  |
| money_delta+pin_rlm | close | 1-3k bets | 1-1 | 50.0 | 16.9 | 0.0 |  |
| pin_move+pin_rlm | close | 1-3k bets | 1-5 | 16.7 | -17.4 | -66.7 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 1-4 | 20.0 | -13.7 | -60.0 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 1-3 | 25.0 | -8.1 | -50.0 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 1-4 | 20.0 | -13.7 | -60.0 |  |
| money_delta+pin_value | close | 1-3k bets | 2-2 | 50.0 | 7.1 | -5.5 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 3-2 | 60.0 | 21.6 | 208.4 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 2-0 | 100.0 | 50.0 | 88.9 |  |
| pin_rlm+pin_value | close | 1-3k bets | 0-1 | 0.0 | -35.9 | -100.0 |  |
| money_level+money_moving | close | 3k+ bets | 6-6 | 50.0 | -5.5 | -11.7 |  |
| money_level+sharp_gap | close | 3k+ bets | 6-6 | 50.0 | -5.5 | -11.7 |  |
| money_moving+sharp_gap | close | 3k+ bets | 8-11 | 42.1 | -5.9 | -19.4 |  |
| follow_move+money_delta | close | 3k+ bets | 2-2 | 50.0 | 7.1 | -3.5 |  |
| follow_move+money_level | close | 3k+ bets | 5-1 | 83.3 | 20.2 | 30.3 |  |
| follow_move+money_moving | close | 3k+ bets | 5-3 | 62.5 | 16.0 | 13.9 |  |
| follow_move+pin_move | close | 3k+ bets | 3-2 | 60.0 | 18.5 | 19.9 |  |
| follow_move+pin_rlm | close | 3k+ bets | 2-0 | 100.0 | 66.9 | 114.6 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 3-2 | 60.0 | 20.7 | 24.0 |  |
| follow_move+sharp_gap | close | 3k+ bets | 5-3 | 62.5 | 16.0 | 13.9 |  |
| money_delta+money_level | close | 3k+ bets | 2-0 | 100.0 | 50.0 | 93.0 |  |
| money_delta+money_moving | close | 3k+ bets | 3-1 | 75.0 | 33.4 | 56.0 |  |
| money_delta+pin_move | close | 3k+ bets | 1-1 | 50.0 | 14.1 | -2.4 |  |
| money_delta+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 64.1 | 95.2 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 2-1 | 66.7 | 21.4 | 28.7 |  |
| money_delta+sharp_gap | close | 3k+ bets | 3-1 | 75.0 | 33.4 | 56.0 |  |
| money_level+pin_move | close | 3k+ bets | 2-0 | 100.0 | 47.2 | 78.8 |  |
| money_level+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 64.1 | 95.2 |  |
| money_level+rlm_ratio | close | 3k+ bets | 2-0 | 100.0 | 50.0 | 93.0 |  |
| money_moving+pin_move | close | 3k+ bets | 2-1 | 66.7 | 19.5 | 19.2 |  |
| money_moving+pin_rlm | close | 3k+ bets | 2-0 | 100.0 | 66.9 | 114.6 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 3-2 | 60.0 | 20.7 | 24.0 |  |
| pin_move+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 64.1 | 95.2 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 1-0 | 100.0 | 64.1 | 95.2 |  |
| pin_move+sharp_gap | close | 3k+ bets | 2-1 | 66.7 | 19.5 | 19.2 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 2-0 | 100.0 | 66.9 | 114.6 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 2-0 | 100.0 | 66.9 | 114.6 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 3-2 | 60.0 | 20.7 | 24.0 |  |
| consensus_gap+money_level | close | 3k+ bets | 2-1 | 66.7 | -1.2 | 6.1 |  |
| consensus_gap+money_moving | close | 3k+ bets | 1-2 | 33.3 | -23.2 | -57.0 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 1-2 | 33.3 | -23.2 | -57.0 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 1-5 | 16.7 | -19.1 | -59.7 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 1-2 | 33.3 | -0.7 | -19.3 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 0-2 | 0.0 | -35.9 | -100.0 |  |
| money_level+pin_value | close | 3k+ bets | 2-1 | 66.7 | 12.0 | 26.7 |  |
| money_moving+pin_value | close | 3k+ bets | 1-2 | 33.3 | -17.9 | -36.4 |  |
| pin_value+sharp_gap | close | 3k+ bets | 1-2 | 33.3 | -17.9 | -36.4 |  |
| consensus_gap+follow_move | close | 3k+ bets | 1-0 | 100.0 | 30.3 | 29.0 |  |
| consensus_gap+pin_value | close | 3k+ bets | 1-0 | 100.0 | 35.9 | 89.3 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 0-3 | 0.0 | -34.0 | -100.0 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 0-3 | 0.0 | -34.0 | -100.0 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 0-2 | 0.0 | -33.1 | -100.0 |  |
| money_delta+money_moving | close | pin $1-2k | 3-1 | 75.0 | 40.5 | 45.3 |  |
| money_delta+sharp_gap | close | pin $1-2k | 3-1 | 75.0 | 40.5 | 45.3 |  |
| money_moving+sharp_gap | close | pin $1-2k | 12-12 | 50.0 | -2.9 | -7.3 |  |
| consensus_gap+follow_move | close | pin $1-2k | 3-4 | 42.9 | -15.1 | -21.8 |  |
| consensus_gap+money_level | close | pin $1-2k | 5-4 | 55.6 | -11.0 | -6.1 |  |
| consensus_gap+money_moving | close | pin $1-2k | 2-3 | 40.0 | -26.3 | -39.0 |  |
| consensus_gap+pin_move | close | pin $1-2k | 1-3 | 25.0 | -25.5 | -52.3 |  |
| consensus_gap+pin_value | close | pin $1-2k | 3-3 | 50.0 | -6.0 | -5.1 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 1-3 | 25.0 | -40.5 | -52.3 |  |
| follow_move+money_level | close | pin $1-2k | 7-5 | 58.3 | 1.4 | 5.6 |  |
| follow_move+money_moving | close | pin $1-2k | 5-4 | 55.6 | 3.4 | 0.6 |  |
| follow_move+pin_move | close | pin $1-2k | 5-13 | 27.8 | -17.8 | -46.3 |  |
| follow_move+pin_value | close | pin $1-2k | 1-4 | 20.0 | -28.7 | -61.8 |  |
| follow_move+sharp_gap | close | pin $1-2k | 5-5 | 50.0 | 0.0 | -9.5 |  |
| money_level+money_moving | close | pin $1-2k | 12-8 | 60.0 | 3.1 | 7.4 |  |
| money_level+pin_move | close | pin $1-2k | 4-4 | 50.0 | -3.5 | -4.3 |  |
| money_level+pin_value | close | pin $1-2k | 4-3 | 57.1 | -0.4 | 7.0 |  |
| money_level+sharp_gap | close | pin $1-2k | 11-8 | 57.9 | 1.7 | 7.0 |  |
| money_moving+pin_move | close | pin $1-2k | 3-4 | 42.9 | -6.6 | -18.7 |  |
| money_moving+pin_value | close | pin $1-2k | 2-4 | 33.3 | -21.4 | -37.6 |  |
| pin_move+pin_value | close | pin $1-2k | 3-3 | 50.0 | -1.3 | -7.1 |  |
| pin_move+sharp_gap | close | pin $1-2k | 3-5 | 37.5 | -9.6 | -28.8 |  |
| pin_value+sharp_gap | close | pin $1-2k | 2-4 | 33.3 | -21.4 | -37.6 |  |
| follow_move+money_delta | close | pin $1-2k | 4-6 | 40.0 | 2.3 | -21.9 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 4-10 | 28.6 | -10.0 | -39.1 |  |
| money_delta+pin_move | close | pin $1-2k | 3-3 | 50.0 | 14.1 | -2.4 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 2-6 | 25.0 | -13.1 | -51.2 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 3-7 | 30.0 | -8.4 | -41.9 |  |
| follow_move+pin_rlm | close | pin $1-2k | 1-2 | 33.3 | -0.7 | -34.9 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 2-2 | 50.0 | 15.5 | -2.4 |  |
| pin_move+pin_rlm | close | pin $1-2k | 1-2 | 33.3 | -0.7 | -34.9 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 1-2 | 33.3 | -0.7 | -34.9 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 0-2 | 0.0 | -33.1 | -100.0 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 1-2 | 33.3 | -0.7 | -34.9 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 1-2 | 33.3 | -0.7 | -34.9 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 0-2 | 0.0 | -33.1 | -100.0 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 0-2 | 0.0 | -33.1 | -100.0 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 2-2 | 50.0 | 15.5 | -2.4 |  |
| money_delta+money_level | close | pin $1-2k | 2-0 | 100.0 | 64.1 | 95.2 |  |
| money_delta+pin_rlm | close | pin $1-2k | 1-0 | 100.0 | 64.1 | 95.2 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 2-0 | 100.0 | 64.1 | 95.2 |  |
| money_level+pin_rlm | close | pin $1-2k | 1-0 | 100.0 | 64.1 | 95.2 |  |
| money_level+rlm_ratio | close | pin $1-2k | 2-0 | 100.0 | 64.1 | 95.2 |  |
| money_moving+pin_rlm | close | pin $1-2k | 1-1 | 50.0 | 14.1 | -2.4 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 2-1 | 66.7 | 30.8 | 30.1 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 0-1 | 0.0 | -35.9 | -100.0 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 1-1 | 50.0 | 7.9 | -4.5 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 1-2 | 33.3 | -8.5 | -36.4 |  |
| money_delta+pin_value | close | pin $1-2k | 0-2 | 0.0 | -35.9 | -100.0 |  |
| follow_move+pin_move | close | pin $2k+ | 9-5 | 64.3 | 11.1 | 16.2 |  |
| consensus_gap+money_level | close | pin $2k+ | 7-4 | 63.6 | 0.2 | 2.5 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 4-4 | 50.0 | 10.2 | 124.1 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 1-3 | 25.0 | -12.6 | -39.5 |  |
| money_level+money_moving | close | pin $2k+ | 5-9 | 35.7 | -18.8 | -39.8 |  |
| money_level+sharp_gap | close | pin $2k+ | 5-9 | 35.7 | -18.8 | -39.8 |  |
| money_moving+sharp_gap | close | pin $2k+ | 7-14 | 33.3 | -16.4 | -39.6 |  |
| consensus_gap+pin_value | close | pin $2k+ | 7-2 | 77.8 | 26.2 | 44.5 |  |
| follow_move+money_level | close | pin $2k+ | 5-3 | 62.5 | 1.7 | -5.2 |  |
| follow_move+money_moving | close | pin $2k+ | 5-6 | 45.5 | -4.0 | -18.9 |  |
| follow_move+sharp_gap | close | pin $2k+ | 5-6 | 45.5 | -4.0 | -18.9 |  |
| money_level+pin_move | close | pin $2k+ | 4-2 | 66.7 | 3.5 | 4.8 |  |
| money_moving+pin_move | close | pin $2k+ | 3-3 | 50.0 | -4.9 | -11.8 |  |
| pin_move+sharp_gap | close | pin $2k+ | 3-3 | 50.0 | -4.9 | -11.8 |  |
| money_delta+money_level | close | pin $2k+ | 1-0 | 100.0 | 53.8 | 90.9 |  |
| money_delta+money_moving | close | pin $2k+ | 1-3 | 25.0 | -13.2 | -52.3 |  |
| money_delta+sharp_gap | close | pin $2k+ | 1-3 | 25.0 | -13.2 | -52.3 |  |
| consensus_gap+money_moving | close | pin $2k+ | 2-4 | 33.3 | -28.5 | -49.2 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 2-4 | 33.3 | -28.5 | -49.2 |  |
| money_level+pin_value | close | pin $2k+ | 2-2 | 50.0 | -2.6 | -5.8 |  |
| money_moving+pin_value | close | pin $2k+ | 1-3 | 25.0 | -25.0 | -52.3 |  |
| pin_value+sharp_gap | close | pin $2k+ | 1-3 | 25.0 | -25.0 | -52.3 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -69.7 | -100.0 |  |
| money_level+pin_rlm | close | pin $2k+ | 0-1 | 0.0 | -69.7 | -100.0 |  |
| money_moving+pin_rlm | close | pin $2k+ | 1-1 | 50.0 | 0.0 | 17.0 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 1-1 | 50.0 | 0.0 | 17.0 |  |
| follow_move+money_delta | close | pin $2k+ | 0-2 | 0.0 | -38.2 | -100.0 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 1-3 | 25.0 | -9.3 | -41.5 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 0-2 | 0.0 | -38.2 | -100.0 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 1-3 | 25.0 | -9.3 | -41.5 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 1-3 | 25.0 | -9.3 | -41.5 |  |
| money_level+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -30.3 | -100.0 |  |
| consensus_gap+follow_move | close | pin $2k+ | 3-0 | 100.0 | 30.3 | 53.9 |  |
| consensus_gap+pin_move | close | pin $2k+ | 3-1 | 75.0 | 17.1 | 29.0 |  |
| follow_move+pin_value | close | pin $2k+ | 3-0 | 100.0 | 56.6 | 411.4 |  |
| pin_move+pin_value | close | pin $2k+ | 3-1 | 75.0 | 26.9 | 39.4 |  |
| follow_move+pin_rlm | close | pin $2k+ | 1-0 | 100.0 | 69.7 | 134.0 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 1-0 | 100.0 | 69.7 | 134.0 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 1-0 | 100.0 | 69.7 | 1060.0 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 0-2 | 0.0 | -33.1 | -100.0 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 0-2 | 0.0 | -33.1 | -100.0 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 0-1 | 0.0 | -30.3 | -100.0 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -30.3 | -100.0 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 3-1 | 75.0 | 26.4 | 44.5 |  |
| consensus_gap+money_level | close | pin limit <$1k | 2-1 | 66.7 | 2.6 | 24.9 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 3-2 | 60.0 | 13.9 | 15.6 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 3-2 | 60.0 | 7.2 | 13.1 |  |
| follow_move+money_level | close | pin limit <$1k | 3-3 | 50.0 | -7.7 | -5.2 |  |
| follow_move+money_moving | close | pin limit <$1k | 4-4 | 50.0 | 0.7 | -4.4 |  |
| follow_move+pin_value | close | pin limit <$1k | 4-2 | 66.7 | 9.0 | 26.0 |  |
| money_level+money_moving | close | pin limit <$1k | 3-4 | 42.9 | -13.2 | -19.3 |  |
| money_level+pin_value | close | pin limit <$1k | 4-3 | 57.1 | -1.5 | 8.1 |  |
| money_moving+pin_value | close | pin limit <$1k | 4-4 | 50.0 | -3.5 | -5.5 |  |
| follow_move+pin_move | close | pin limit <$1k | 3-4 | 42.9 | -2.9 | -16.9 |  |
| money_level+pin_move | close | pin limit <$1k | 3-3 | 50.0 | -3.0 | -5.2 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 4-6 | 40.0 | -4.8 | -23.5 |  |
| pin_move+pin_value | close | pin limit <$1k | 2-2 | 50.0 | -4.5 | -4.5 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 3-3 | 50.0 | 10.3 | -3.0 |  |
| money_moving+pin_move | close | pin limit <$1k | 3-4 | 42.9 | -4.3 | -17.4 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 2-0 | 100.0 | 66.9 | 95.5 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 16.9 | 0.0 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 1-1 | 50.0 | 16.9 | 0.0 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 2-0 | 100.0 | 66.9 | 95.5 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 2-0 | 100.0 | 66.9 | 95.5 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 3-1 | 75.0 | 33.4 | 44.5 |  |
| follow_move+money_delta | close | pin limit <$1k | 3-1 | 75.0 | 33.4 | 44.5 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 1-2 | 33.3 | -0.7 | -33.3 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 3-2 | 60.0 | 19.6 | 15.6 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 4-3 | 57.1 | 10.0 | 9.3 |  |
| money_delta+money_moving | close | pin limit <$1k | 3-1 | 75.0 | 33.4 | 44.5 |  |
| money_delta+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 16.9 | 0.0 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 1-1 | 50.0 | 16.9 | 0.0 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 2-0 | 100.0 | 66.9 | 95.5 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 3-1 | 75.0 | 33.4 | 44.5 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 3-1 | 75.0 | 33.4 | 44.5 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 1-3 | 25.0 | -9.5 | -50.0 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 2-1 | 66.7 | 32.6 | 30.3 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 3-2 | 60.0 | 19.6 | 15.6 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 1-3 | 25.0 | -9.5 | -50.0 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 2-2 | 50.0 | 8.4 | -2.3 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 1-2 | 33.3 | -0.7 | -33.3 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 1-4 | 20.0 | -20.4 | -60.0 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 1-1 | 50.0 | 16.9 | 0.0 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 1-2 | 33.3 | -0.7 | -33.3 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 1-3 | 25.0 | -9.5 | -50.0 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 2-1 | 66.7 | 32.6 | 30.3 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 2-1 | 66.7 | 32.6 | 30.3 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 3-2 | 60.0 | 19.6 | 15.6 |  |
| money_delta+pin_value | close | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 1-0 | 100.0 | 64.1 | 90.9 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 3-3 | 50.0 | 0.0 | -5.9 |  |
| money_level+sharp_gap | close | pin limit <$1k | 1-3 | 25.0 | -25.0 | -53.2 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 0-1 | 0.0 | -35.9 | -100.0 |  |
| money_delta+money_level | close | pin limit <$1k | 0-1 | 0.0 | -35.9 | -100.0 |  |
| money_level+pin_rlm | close | pin limit <$1k | 0-1 | 0.0 | -35.9 | -100.0 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 0-1 | 0.0 | -35.9 | -100.0 |  |
| rlm_quiet | early | <1k bets | 3-4 | 42.9 | 10.2 | -4.3 | -1.27 |
| follow_move | early | <1k bets | 12-18 | 40.0 | -6.3 | -15.9 | -0.54 |
| follow_move | early | pin $1-2k | 1-0 | 100.0 | 69.7 | 142.0 | 0.0 |
| rlm_ratio | early | <1k bets | 2-3 | 40.0 | 1.6 | -23.6 | -0.06 |
| money_level | early | <1k bets | 9-7 | 56.2 | -9.7 | -9.7 | 1.07 |
| sharp_gap | early | <1k bets | 6-6 | 50.0 | 3.2 | -8.4 | 0.52 |
| money_moving | early | <1k bets | 7-4 | 63.6 | 9.7 | 18.8 | 1.12 |
| pin_value | early | <1k bets | 0-1 | 0.0 | -46.2 | -100.0 | 0.0 |
| pin_value | early | pin $1-2k | 0-1 | 0.0 | -46.2 | -100.0 | 0.0 |
| consensus_gap | early | <1k bets | 11-3 | 78.6 | 21.2 | 35.1 | 1.15 |
| follow_move+money_level | early | <1k bets | 2-3 | 40.0 | -23.2 | -39.6 | 0.36 |
| follow_move+sharp_gap | early | <1k bets | 3-4 | 42.9 | -2.9 | -18.2 | -0.19 |
| money_level+sharp_gap | early | <1k bets | 3-2 | 60.0 | -4.3 | 5.3 | 1.9 |
| follow_move+money_moving | early | <1k bets | 4-3 | 57.1 | 6.6 | 11.6 | 0.4 |
| money_level+money_moving | early | <1k bets | 4-3 | 57.1 | -7.9 | -8.9 | 1.61 |
| consensus_gap+money_level | early | <1k bets | 3-1 | 75.0 | 5.3 | -0.5 | 1.17 |
| follow_move+rlm_quiet | early | <1k bets | 3-4 | 42.9 | 10.2 | -4.3 | -1.27 |
| follow_move+rlm_ratio | early | <1k bets | 2-3 | 40.0 | 1.6 | -23.6 | -0.06 |
| rlm_quiet+rlm_ratio | early | <1k bets | 2-2 | 50.0 | 15.5 | -4.5 | -1.32 |
| rlm_quiet+sharp_gap | early | <1k bets | 2-2 | 50.0 | 15.5 | -4.5 | -1.32 |
| rlm_ratio+sharp_gap | early | <1k bets | 2-3 | 40.0 | 1.6 | -23.6 | -0.06 |
| consensus_gap+follow_move | early | <1k bets | 2-1 | 66.7 | 8.2 | 0.7 | -0.83 |
| money_moving+rlm_quiet | early | <1k bets | 3-0 | 100.0 | 66.0 | 123.3 | 0.33 |
| money_moving+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 24.8 | 27.3 | 1.33 |
| money_moving+sharp_gap | early | <1k bets | 4-2 | 66.7 | 11.8 | 19.6 | 1.42 |
| consensus_gap+money_moving | early | <1k bets | 2-0 | 100.0 | 30.3 | 42.0 | 0.15 |
| consensus_gap+sharp_gap | early | <1k bets | 1-0 | 100.0 | 30.3 | 73.0 | 2.5 |
| money_level+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -53.8 | -100.0 | 5.0 |
