# CBB scorecard

Generated 2026-11-24 02:36 UTC. 822 graded games (36 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**684 games before 2026-11-21 (fit) · 138 on or after it (forward).**

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
sample ran **46.9% favourites** (n=821) and **50.9% overs** (n=822) and **72.0% moneyline favourites** (n=708).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-21. Nothing in the engine was chosen using these. n=138 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 9-15 | 37.5 | 38.0 | -0.5 | -3.59 | -15.0 | 0.72 | 45.8 | keep collecting (24/30) |
| pin_move | both | 4-5 | 44.4 | 50.4 | -6.0 | -1.36 | -15.2 | 0.11 | 22.2 | keep collecting (9/30) |
| money_delta | both | 1-2 | 33.3 | 40.4 | -7.0 | -1.09 | -36.4 | 1.6 | 100.0 | keep collecting (3/30) |
| pin_rlm | both | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | 1.5 | 100.0 | keep collecting (1/30) |
| follow_move | both | 94-109 | 46.3 | 48.5 | -2.2 | -23.11 | -11.4 | 0.16 | 36.9 | DROP: below break-even |
| rlm_ratio | both | 5-8 | 38.5 | 42.7 | -4.3 | -2.6 | -20.0 | 0.55 | 53.8 | keep collecting (13/30) |
| money_level | both | 32-24 | 57.1 | 60.0 | -2.8 | -4.5 | -8.0 | -0.1 | 37.5 | no edge shown yet |
| sharp_gap | both | 20-29 | 40.8 | 48.4 | -7.6 | -10.47 | -21.4 | 0.43 | 49.0 | DROP: below break-even |
| money_moving | both | 20-24 | 45.5 | 48.3 | -2.8 | -6.3 | -14.3 | 0.33 | 50.0 | no edge shown yet |
| pin_value | both | 11-10 | 52.4 | 49.1 | 3.3 | -0.27 | -1.3 | -0.16 | 28.6 | keep collecting (21/30) |
| consensus_gap | both | 63-44 | 58.9 | 51.4 | 7.4 | +7.4 | 6.9 | 0.4 | 48.6 | no edge shown yet |
| follow_move+money_level | both | 11-9 | 55.0 | 60.4 | -5.4 | -3.64 | -18.2 | 0.67 | 40.0 | keep collecting (20/30) |
| follow_move+sharp_gap | both | 9-13 | 40.9 | 48.0 | -7.1 | -4.36 | -19.8 | 1.05 | 50.0 | keep collecting (22/30) |
| money_level+sharp_gap | both | 12-14 | 46.2 | 57.4 | -11.3 | -4.66 | -17.9 | 0.28 | 50.0 | keep collecting (26/30) |
| follow_move+money_moving | both | 10-11 | 47.6 | 48.1 | -0.5 | -2.32 | -11.0 | 0.64 | 47.6 | keep collecting (21/30) |
| money_level+money_moving | both | 11-10 | 52.4 | 57.8 | -5.5 | -2.46 | -11.7 | 0.32 | 42.9 | keep collecting (21/30) |
| consensus_gap+money_level | both | 11-5 | 68.8 | 59.3 | 9.4 | +0.33 | 2.1 | -0.45 | 37.5 | keep collecting (16/30) |
| follow_move+rlm_quiet | both | 9-15 | 37.5 | 38.0 | -0.5 | -3.59 | -15.0 | 0.72 | 45.8 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 5-8 | 38.5 | 42.7 | -4.3 | -2.6 | -20.0 | 0.55 | 53.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | both | 4-5 | 44.4 | 38.3 | 6.2 | -0.51 | -5.7 | -0.27 | 33.3 | keep collecting (9/30) |
| rlm_quiet+sharp_gap | both | 4-6 | 40.0 | 38.8 | 1.2 | -1.51 | -15.1 | -0.24 | 30.0 | keep collecting (10/30) |
| rlm_ratio+sharp_gap | both | 5-8 | 38.5 | 42.7 | -4.3 | -2.6 | -20.0 | 0.55 | 53.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 7-5 | 58.3 | 51.3 | 7.1 | -0.1 | -0.9 | 0.84 | 66.7 | keep collecting (12/30) |
| money_moving+rlm_quiet | both | 5-5 | 50.0 | 38.8 | 11.2 | +1.37 | 13.7 | 0.6 | 50.0 | keep collecting (10/30) |
| money_moving+rlm_ratio | both | 5-4 | 55.6 | 42.0 | 13.6 | +1.4 | 15.5 | 1.1 | 66.7 | keep collecting (9/30) |
| money_moving+sharp_gap | both | 13-16 | 44.8 | 47.3 | -2.5 | -2.91 | -10.0 | 0.59 | 55.2 | keep collecting (29/30) |
| consensus_gap+money_moving | both | 4-3 | 57.1 | 49.1 | 8.1 | -0.83 | -11.9 | 0.74 | 57.1 | keep collecting (7/30) |
| consensus_gap+sharp_gap | both | 5-4 | 55.6 | 48.2 | 7.3 | -0.17 | -1.8 | -0.06 | 55.6 | keep collecting (9/30) |
| money_level+rlm_ratio | both | 1-3 | 25.0 | 52.7 | -27.7 | -2.09 | -52.3 | 2.38 | 100.0 | keep collecting (4/30) |
| follow_move+pin_move | both | 1-3 | 25.0 | 46.4 | -21.4 | -2.09 | -52.3 | 0.5 | 25.0 | keep collecting (4/30) |
| follow_move+money_delta | both | 1-1 | 50.0 | 43.5 | 6.5 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+money_level | both | 1-1 | 50.0 | 43.5 | 6.5 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+money_moving | both | 1-2 | 33.3 | 40.4 | -7.0 | -1.09 | -36.4 | 1.6 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | both | 1-1 | 50.0 | 43.5 | 6.5 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+sharp_gap | both | 1-2 | 33.3 | 40.4 | -7.0 | -1.09 | -36.4 | 1.6 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| follow_move+pin_value | both | 3-3 | 50.0 | 45.2 | 4.8 | -0.27 | -4.5 | -0.83 | 16.7 | keep collecting (6/30) |
| consensus_gap+pin_move | both | 1-0 | 100.0 | 56.5 | 43.5 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+pin_value | both | 5-1 | 83.3 | 49.8 | 33.6 | +3.47 | 57.8 | 0.0 | 33.3 | keep collecting (6/30) |
| money_level+pin_move | both | 1-1 | 50.0 | 56.5 | -6.5 | -0.09 | -4.5 | 1.5 | 50.0 | keep collecting (2/30) |
| money_level+pin_value | both | 2-2 | 50.0 | 55.6 | -5.6 | -0.18 | -4.5 | 1.43 | 75.0 | keep collecting (4/30) |
| pin_move+pin_value | both | 2-4 | 33.3 | 51.7 | -18.4 | -2.18 | -36.4 | 0.17 | 16.7 | keep collecting (6/30) |
| money_moving+pin_value | both | 1-1 | 50.0 | 54.7 | -4.7 | -0.09 | -4.5 | 1.35 | 100.0 | keep collecting (2/30) |
| pin_value+sharp_gap | both | 1-2 | 33.3 | 55.3 | -22.0 | -1.09 | -36.4 | 1.9 | 100.0 | keep collecting (3/30) |
| consensus_gap+money_delta | both | 1-0 | 100.0 | 43.5 | 56.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 1-0 | 100.0 | 43.5 | 56.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | both | 1-0 | 100.0 | 43.5 | 56.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+rlm_ratio | both | 1-0 | 100.0 | 43.5 | 56.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | both | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+sharp_gap | both | 0-1 | 0.0 | 56.5 | -56.5 | -1.0 | -100.0 | 3.0 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 5-9 | 35.7 | 34.1 | 1.6 | -1.19 | -8.5 | 0.95 | 42.9 | keep collecting (14/30) |
| rlm_quiet | total | 4-6 | 40.0 | 43.5 | -3.5 | -2.4 | -24.0 | 0.4 | 50.0 | keep collecting (10/30) |
| pin_move | spread | 0-2 | 0.0 | 42.0 | -42.0 | -2.0 | -100.0 | 0.0 | 0.0 | keep collecting (2/30) |
| pin_move | total | 4-3 | 57.1 | 52.8 | 4.3 | +0.64 | 9.1 | 0.14 | 28.6 | keep collecting (7/30) |
| money_delta | moneyline | 0-1 | 0.0 | 34.1 | -34.1 | -1.0 | -100.0 | 1.8 | 100.0 | keep collecting (1/30) |
| money_delta | total | 1-1 | 50.0 | 43.5 | 6.5 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| pin_rlm | moneyline | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | 1.5 | 100.0 | keep collecting (1/30) |
| follow_move | moneyline | 40-32 | 55.6 | 47.4 | 8.2 | +4.13 | 5.7 | -0.08 | 33.3 | no edge shown yet |
| follow_move | spread | 22-36 | 37.9 | 51.4 | -13.4 | -15.5 | -26.7 | -0.16 | 27.6 | DROP: below break-even |
| follow_move | total | 32-41 | 43.8 | 47.4 | -3.6 | -11.73 | -16.1 | 0.64 | 47.9 | no edge shown yet |
| rlm_ratio | moneyline | 1-5 | 16.7 | 39.4 | -22.8 | -3.24 | -54.0 | 0.02 | 33.3 | keep collecting (6/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 58.0 | -58.0 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| rlm_ratio | total | 4-2 | 66.7 | 43.5 | 23.2 | +1.64 | 27.3 | 0.33 | 66.7 | keep collecting (6/30) |
| money_level | moneyline | 18-12 | 60.0 | 63.8 | -3.8 | -5.26 | -17.5 | -0.35 | 30.0 | no edge shown yet |
| money_level | spread | 0-1 | 0.0 | 58.0 | -58.0 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level | total | 14-11 | 56.0 | 55.5 | 0.5 | +1.76 | 7.0 | 0.0 | 44.0 | keep collecting (25/30) |
| sharp_gap | moneyline | 8-17 | 32.0 | 46.8 | -14.8 | -9.41 | -37.7 | 0.61 | 56.0 | keep collecting (25/30) |
| sharp_gap | spread | 0-1 | 0.0 | 58.0 | -58.0 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| sharp_gap | total | 12-11 | 52.2 | 49.7 | 2.5 | -0.06 | -0.3 | 0.04 | 39.1 | keep collecting (23/30) |
| money_moving | moneyline | 9-13 | 40.9 | 47.1 | -6.2 | -5.33 | -24.2 | 0.48 | 59.1 | keep collecting (22/30) |
| money_moving | spread | 0-1 | 0.0 | 58.0 | -58.0 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving | total | 11-10 | 52.4 | 49.1 | 3.3 | +0.03 | 0.2 | -0.05 | 38.1 | keep collecting (21/30) |
| pin_value | moneyline | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| pin_value | spread | 6-6 | 50.0 | 46.0 | 4.0 | -0.82 | -6.8 | -0.25 | 16.7 | keep collecting (12/30) |
| pin_value | total | 5-3 | 62.5 | 51.6 | 10.9 | +1.54 | 19.3 | -0.25 | 37.5 | keep collecting (8/30) |
| consensus_gap | moneyline | 28-20 | 58.3 | 54.6 | 3.7 | +0.16 | 0.3 | -0.05 | 43.8 | no edge shown yet |
| consensus_gap | spread | 14-10 | 58.3 | 48.0 | 10.3 | +2.31 | 9.6 | 0.29 | 37.5 | keep collecting (24/30) |
| consensus_gap | total | 21-14 | 60.0 | 49.4 | 10.6 | +4.94 | 14.1 | 1.09 | 62.9 | no edge shown yet |
| consensus_gap+money_level | moneyline | 9-4 | 69.2 | 61.0 | 8.2 | -0.49 | -3.7 | -0.78 | 30.8 | keep collecting (13/30) |
| follow_move+rlm_quiet | moneyline | 5-9 | 35.7 | 34.1 | 1.6 | -1.19 | -8.5 | 0.95 | 42.9 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 1-5 | 16.7 | 39.4 | -22.8 | -3.24 | -54.0 | 0.02 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 2-6 | 25.0 | 46.0 | -21.0 | -3.73 | -46.6 | 1.76 | 50.0 | keep collecting (8/30) |
| rlm_quiet+rlm_ratio | moneyline | 1-4 | 20.0 | 34.1 | -14.1 | -2.24 | -44.8 | -0.28 | 20.0 | keep collecting (5/30) |
| rlm_quiet+sharp_gap | moneyline | 1-4 | 20.0 | 34.1 | -14.1 | -2.24 | -44.8 | -0.28 | 20.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | moneyline | 1-5 | 16.7 | 39.4 | -22.8 | -3.24 | -54.0 | 0.02 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 4-1 | 80.0 | 59.5 | 20.5 | +1.17 | 23.4 | -0.38 | 40.0 | keep collecting (5/30) |
| consensus_gap+money_moving | moneyline | 3-3 | 50.0 | 50.0 | -0.0 | -1.74 | -29.0 | 0.7 | 50.0 | keep collecting (6/30) |
| consensus_gap+sharp_gap | moneyline | 4-3 | 57.1 | 47.7 | 9.4 | -0.07 | -1.1 | -0.5 | 42.9 | keep collecting (7/30) |
| money_level+money_moving | moneyline | 5-4 | 55.6 | 62.3 | -6.8 | -1.95 | -21.6 | 0.3 | 33.3 | keep collecting (9/30) |
| money_level+sharp_gap | moneyline | 5-7 | 41.7 | 60.6 | -18.9 | -4.05 | -33.8 | 0.28 | 50.0 | keep collecting (12/30) |
| money_moving+sharp_gap | moneyline | 4-9 | 30.8 | 43.9 | -13.1 | -4.12 | -31.7 | 1.15 | 69.2 | keep collecting (13/30) |
| follow_move+money_level | moneyline | 7-4 | 63.6 | 65.9 | -2.2 | -2.27 | -20.7 | 0.31 | 27.3 | keep collecting (11/30) |
| follow_move+money_moving | moneyline | 5-4 | 55.6 | 48.2 | 7.3 | +0.14 | 1.5 | 0.28 | 44.4 | keep collecting (9/30) |
| money_moving+rlm_quiet | moneyline | 2-3 | 40.0 | 34.1 | 5.9 | +0.64 | 12.8 | 0.8 | 60.0 | keep collecting (5/30) |
| money_moving+rlm_ratio | moneyline | 1-2 | 33.3 | 34.1 | -0.8 | -0.24 | -8.0 | -0.37 | 33.3 | keep collecting (3/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_rlm | moneyline | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | moneyline | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | 1.5 | 100.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | 1.5 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+money_moving | moneyline | 0-1 | 0.0 | 34.1 | -34.1 | -1.0 | -100.0 | 1.8 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 0-1 | 0.0 | 34.1 | -34.1 | -1.0 | -100.0 | 1.8 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| follow_move+money_level | spread | 0-1 | 0.0 | 58.0 | -58.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| follow_move+money_moving | spread | 0-1 | 0.0 | 58.0 | -58.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 58.0 | -58.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 0-1 | 0.0 | 58.0 | -58.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to sharp_gap alone, not independent confirmation |
| money_level+money_moving | spread | 0-1 | 0.0 | 58.0 | -58.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+rlm_ratio | spread | 0-1 | 0.0 | 58.0 | -58.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+sharp_gap | spread | 0-1 | 0.0 | 58.0 | -58.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 58.0 | -58.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| money_moving+sharp_gap | spread | 0-1 | 0.0 | 58.0 | -58.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 58.0 | -58.0 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 1-1 | 50.0 | 42.0 | 8.0 | -0.09 | -4.5 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | spread | 0-2 | 0.0 | 42.0 | -42.0 | -2.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| consensus_gap+pin_value | spread | 2-1 | 66.7 | 47.3 | 19.3 | +0.74 | 24.7 | -0.67 | 0.0 | keep collecting (3/30) |
| follow_move+pin_move | spread | 0-1 | 0.0 | 42.0 | -42.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_level | total | 4-4 | 50.0 | 53.3 | -3.3 | -0.36 | -4.6 | 0.62 | 50.0 | keep collecting (8/30) |
| follow_move+sharp_gap | total | 7-6 | 53.8 | 48.5 | 5.4 | +0.36 | 2.8 | 0.31 | 46.2 | keep collecting (13/30) |
| money_level+sharp_gap | total | 7-6 | 53.8 | 54.5 | -0.7 | +0.4 | 3.1 | -0.08 | 46.2 | keep collecting (13/30) |
| follow_move+money_moving | total | 5-6 | 45.5 | 47.0 | -1.6 | -1.45 | -13.2 | 0.55 | 45.5 | keep collecting (11/30) |
| money_level+money_moving | total | 6-5 | 54.5 | 54.2 | 0.4 | +0.49 | 4.4 | -0.09 | 45.5 | keep collecting (11/30) |
| follow_move+rlm_quiet | total | 4-6 | 40.0 | 43.5 | -3.5 | -2.4 | -24.0 | 0.4 | 50.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 4-2 | 66.7 | 43.5 | 23.2 | +1.64 | 27.3 | 0.33 | 66.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 3-1 | 75.0 | 43.5 | 31.5 | +1.73 | 43.2 | -0.25 | 50.0 | keep collecting (4/30) |
| rlm_quiet+sharp_gap | total | 3-2 | 60.0 | 43.5 | 16.5 | +0.73 | 14.5 | -0.2 | 40.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | total | 4-2 | 66.7 | 43.5 | 23.2 | +1.64 | 27.3 | 0.33 | 66.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | total | 3-2 | 60.0 | 43.5 | 16.5 | +0.73 | 14.5 | 0.4 | 40.0 | keep collecting (5/30) |
| money_moving+rlm_ratio | total | 4-1 | 80.0 | 43.5 | 36.5 | +2.64 | 52.7 | 1.2 | 80.0 | keep collecting (5/30) |
| money_moving+sharp_gap | total | 9-6 | 60.0 | 49.6 | 10.4 | +2.21 | 14.8 | -0.2 | 40.0 | keep collecting (15/30) |
| follow_move+pin_move | total | 1-2 | 33.3 | 47.8 | -14.5 | -1.09 | -36.4 | 0.67 | 33.3 | keep collecting (3/30) |
| consensus_gap+follow_move | total | 3-4 | 42.9 | 45.3 | -2.5 | -1.27 | -18.2 | 1.71 | 85.7 | keep collecting (7/30) |
| consensus_gap+money_level | total | 2-1 | 66.7 | 52.2 | 14.5 | +0.82 | 27.3 | 1.0 | 66.7 | keep collecting (3/30) |
| consensus_gap+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| follow_move+money_delta | total | 1-1 | 50.0 | 43.5 | 6.5 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_level | total | 1-1 | 50.0 | 43.5 | 6.5 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_moving | total | 1-1 | 50.0 | 43.5 | 6.5 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | total | 1-1 | 50.0 | 43.5 | 6.5 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | total | 1-1 | 50.0 | 43.5 | 6.5 | -0.09 | -4.5 | 1.5 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+rlm_ratio | total | 1-1 | 50.0 | 43.5 | 6.5 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| follow_move+pin_value | total | 2-2 | 50.0 | 46.7 | 3.3 | -0.18 | -4.5 | -1.0 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | total | 1-0 | 100.0 | 56.5 | 43.5 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+pin_value | total | 3-0 | 100.0 | 52.2 | 47.8 | +2.73 | 90.9 | 0.67 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | total | 1-1 | 50.0 | 56.5 | -6.5 | -0.09 | -4.5 | 1.5 | 50.0 | keep collecting (2/30) |
| money_level+pin_value | total | 2-1 | 66.7 | 52.2 | 14.5 | +0.82 | 27.3 | 1.33 | 66.7 | keep collecting (3/30) |
| pin_move+pin_value | total | 2-2 | 50.0 | 56.5 | -6.5 | -0.18 | -4.5 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+money_delta | total | 1-0 | 100.0 | 43.5 | 56.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_moving | total | 1-0 | 100.0 | 43.5 | 56.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 1-0 | 100.0 | 43.5 | 56.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | total | 1-0 | 100.0 | 43.5 | 56.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 43.5 | 56.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+rlm_ratio | total | 1-0 | 100.0 | 43.5 | 56.5 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | 2.0 | 100.0 | keep collecting (2/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 56.5 | -56.5 | -1.0 | -100.0 | 3.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 47-93 | 33.6 | 41.8 | -8.3 | -32.88 | -23.5 |  |  | DROP: below break-even |
| pin_move | both | 92-105 | 46.7 | 49.7 | -3.0 | -19.02 | -9.7 |  |  | DROP: below break-even |
| money_delta | both | 53-62 | 46.1 | 42.3 | 3.8 | -6.06 | -5.3 |  |  | no edge shown yet |
| pin_rlm | both | 17-27 | 38.6 | 40.9 | -2.2 | -8.48 | -19.3 |  |  | DROP: below break-even |
| follow_move | both | 151-186 | 44.8 | 49.4 | -4.6 | -45.13 | -13.4 |  |  | DROP: below break-even |
| rlm_ratio | both | 30-55 | 35.3 | 41.0 | -5.7 | -24.33 | -28.6 |  |  | DROP: below break-even |
| money_level | both | 203-141 | 59.0 | 56.4 | 2.6 | +3.68 | 1.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 148-170 | 46.5 | 48.0 | -1.4 | -32.04 | -10.1 |  |  | DROP: below break-even |
| money_moving | both | 154-168 | 47.8 | 48.5 | -0.7 | -27.68 | -8.6 |  |  | DROP: below break-even |
| pin_value | both | 78-62 | 55.7 | 50.5 | 5.2 | +22.56 | 16.1 |  |  | no edge shown yet |
| consensus_gap | both | 75-50 | 60.0 | 53.4 | 6.6 | +11.75 | 9.4 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+pin_move | both | 63-93 | 40.4 | 49.3 | -8.9 | -34.43 | -22.1 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 41-45 | 47.7 | 41.1 | 6.6 | -0.13 | -0.2 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 41-44 | 48.2 | 41.1 | 7.2 | +0.87 | 1.0 |  |  | no edge shown yet |
| money_moving+sharp_gap | both | 145-163 | 47.1 | 48.2 | -1.1 | -27.31 | -8.9 |  |  | DROP: below break-even |
| consensus_gap+money_level | both | 53-27 | 66.2 | 59.4 | 6.8 | +5.54 | 6.9 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+rlm_quiet | both | 47-93 | 33.6 | 41.8 | -8.3 | -32.88 | -23.5 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | both | 24-45 | 34.8 | 43.4 | -8.6 | -18.81 | -27.3 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 25-20 | 55.6 | 53.0 | 2.5 | -0.45 | -1.0 |  |  | no edge shown yet |
| follow_move+money_level | both | 74-60 | 55.2 | 57.2 | -2.0 | -6.85 | -5.1 |  |  | no edge shown yet |
| money_level+money_moving | both | 107-86 | 55.4 | 53.8 | 1.6 | -1.02 | -0.5 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 102-85 | 54.5 | 53.5 | 1.1 | -1.47 | -0.8 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 28-26 | 51.9 | 52.0 | -0.1 | +2.01 | 3.7 |  |  | no edge shown yet |
| consensus_gap+pin_move | both | 20-10 | 66.7 | 50.9 | 15.7 | +9.33 | 31.1 |  |  | PROMOTE: beats break-even and its own base rate |
| consensus_gap+pin_value | both | 26-17 | 60.5 | 49.3 | 11.1 | +9.6 | 22.3 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | both | 28-27 | 50.9 | 51.3 | -0.4 | +1.28 | 2.3 |  |  | no edge shown yet |
| follow_move+money_moving | both | 70-90 | 43.8 | 48.4 | -4.7 | -29.73 | -18.6 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 25-21 | 54.3 | 52.1 | 2.3 | +10.95 | 23.8 |  |  | no edge shown yet |
| follow_move+sharp_gap | both | 71-93 | 43.3 | 48.0 | -4.7 | -30.81 | -18.8 |  |  | DROP: below break-even |
| money_level+pin_move | both | 43-38 | 53.1 | 55.4 | -2.3 | -3.48 | -4.3 |  |  | no edge shown yet |
| money_level+pin_value | both | 32-23 | 58.2 | 52.7 | 5.4 | +5.08 | 9.2 |  |  | no edge shown yet |
| money_moving+pin_move | both | 40-45 | 47.1 | 48.3 | -1.2 | -7.81 | -9.2 |  |  | no edge shown yet |
| money_moving+pin_value | both | 27-25 | 51.9 | 50.8 | 1.1 | +2.47 | 4.7 |  |  | no edge shown yet |
| pin_move+pin_value | both | 30-25 | 54.5 | 52.1 | 2.4 | +1.65 | 3.0 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 38-47 | 44.7 | 47.8 | -3.1 | -11.59 | -13.6 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 26-24 | 52.0 | 50.3 | 1.7 | +2.56 | 5.1 |  |  | no edge shown yet |
| follow_move+money_delta | both | 30-43 | 41.1 | 43.6 | -2.5 | -14.62 | -20.0 |  |  | DROP: below break-even |
| money_delta+pin_move | both | 16-20 | 44.4 | 42.5 | 2.0 | -4.66 | -12.9 |  |  | no edge shown yet |
| money_delta+rlm_quiet | both | 17-33 | 34.0 | 41.6 | -7.6 | -16.65 | -33.3 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | both | 30-55 | 35.3 | 41.0 | -5.7 | -24.33 | -28.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | both | 19-44 | 30.2 | 39.8 | -9.6 | -23.76 | -37.7 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 30-52 | 36.6 | 41.1 | -4.6 | -21.33 | -26.0 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 14-41 | 25.5 | 38.9 | -13.4 | -25.91 | -47.1 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | both | 19-48 | 28.4 | 39.6 | -11.2 | -27.76 | -41.4 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 30-55 | 35.3 | 41.0 | -5.7 | -24.33 | -28.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | both | 14-6 | 70.0 | 47.2 | 22.8 | +7.88 | 39.4 |  |  | keep collecting (20/30) |
| consensus_gap+rlm_quiet | both | 6-11 | 35.3 | 39.9 | -4.6 | -3.96 | -23.3 |  |  | keep collecting (17/30) |
| consensus_gap+rlm_ratio | both | 5-6 | 45.5 | 40.0 | 5.4 | +0.05 | 0.4 |  |  | keep collecting (11/30) |
| money_delta+rlm_ratio | both | 21-30 | 41.2 | 41.1 | 0.1 | -9.81 | -19.2 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 2-4 | 33.3 | 44.7 | -11.4 | -0.6 | -10.0 |  |  | keep collecting (6/30) |
| money_level+pin_rlm | both | 7-4 | 63.6 | 45.0 | 18.6 | +2.75 | 25.0 |  |  | keep collecting (11/30) |
| money_moving+pin_rlm | both | 17-25 | 40.5 | 41.0 | -0.5 | -6.48 | -15.4 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 17-27 | 38.6 | 40.9 | -2.2 | -8.48 | -19.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | both | 13-10 | 56.5 | 46.5 | 10.1 | +2.19 | 9.5 |  |  | keep collecting (23/30) |
| consensus_gap+money_delta | both | 8-2 | 80.0 | 44.9 | 35.1 | +8.81 | 88.1 |  |  | keep collecting (10/30) |
| follow_move+pin_rlm | both | 15-24 | 38.5 | 40.1 | -1.6 | -7.71 | -19.8 |  |  | DROP: below break-even |
| money_delta+pin_rlm | both | 10-15 | 40.0 | 39.0 | 1.0 | -5.13 | -20.5 |  |  | keep collecting (25/30) |
| pin_move+pin_rlm | both | 16-22 | 42.1 | 41.1 | 1.0 | -4.82 | -12.7 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 15-22 | 40.5 | 41.6 | -1.1 | -6.2 | -16.8 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | both | 7-19 | 26.9 | 39.3 | -12.4 | -10.8 | -41.5 |  |  | keep collecting (26/30) |
| pin_rlm+rlm_ratio | both | 15-24 | 38.5 | 40.1 | -1.6 | -7.71 | -19.8 |  |  | DROP: below break-even |
| money_delta+pin_value | both | 12-4 | 75.0 | 46.4 | 28.6 | +10.44 | 65.3 |  |  | keep collecting (16/30) |
| pin_value+rlm_quiet | both | 8-9 | 47.1 | 46.6 | 0.4 | +8.01 | 47.1 |  |  | keep collecting (17/30) |
| pin_value+rlm_ratio | both | 5-1 | 83.3 | 50.2 | 33.1 | +3.4 | 56.7 |  |  | keep collecting (6/30) |
| pin_rlm+pin_value | both | 3-2 | 60.0 | 49.0 | 11.0 | +0.69 | 13.8 |  |  | keep collecting (5/30) |
| rlm_quiet | moneyline | 16-42 | 27.6 | 34.7 | -7.1 | -10.85 | -18.7 |  |  | DROP: below break-even |
| rlm_quiet | spread | 9-12 | 42.9 | 55.7 | -12.8 | -3.49 | -16.6 |  |  | keep collecting (21/30) |
| rlm_quiet | total | 22-39 | 36.1 | 43.9 | -7.8 | -18.53 | -30.4 |  |  | DROP: below break-even |
| pin_move | moneyline | 27-24 | 52.9 | 46.6 | 6.4 | +2.94 | 5.8 |  |  | no edge shown yet |
| pin_move | spread | 34-31 | 52.3 | 52.3 | -0.0 | -0.22 | -0.3 |  |  | no edge shown yet |
| pin_move | total | 31-50 | 38.3 | 49.6 | -11.3 | -21.75 | -26.8 |  |  | DROP: below break-even |
| money_delta | moneyline | 15-27 | 35.7 | 37.2 | -1.4 | -6.13 | -14.6 |  |  | DROP: below break-even |
| money_delta | spread | 8-6 | 57.1 | 50.0 | 7.1 | +1.39 | 9.9 |  |  | keep collecting (14/30) |
| money_delta | total | 30-29 | 50.8 | 44.1 | 6.7 | -1.31 | -2.2 |  |  | no edge shown yet |
| pin_rlm | moneyline | 7-13 | 35.0 | 35.7 | -0.7 | -3.7 | -18.5 |  |  | keep collecting (20/30) |
| pin_rlm | spread | 1-0 | 100.0 | 58.0 | 42.0 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| pin_rlm | total | 9-14 | 39.1 | 44.6 | -5.5 | -5.69 | -24.7 |  |  | keep collecting (23/30) |
| follow_move | moneyline | 55-64 | 46.2 | 48.0 | -1.8 | -11.36 | -9.5 |  |  | no edge shown yet |
| follow_move | spread | 42-47 | 47.2 | 52.2 | -5.0 | -8.25 | -9.3 |  |  | no edge shown yet |
| follow_move | total | 54-75 | 41.9 | 48.7 | -6.9 | -25.52 | -19.8 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 10-30 | 25.0 | 34.9 | -9.9 | -17.65 | -44.1 |  |  | DROP: below break-even |
| rlm_ratio | spread | 1-2 | 33.3 | 52.7 | -19.3 | -1.15 | -38.4 |  |  | keep collecting (3/30) |
| rlm_ratio | total | 19-23 | 45.2 | 46.0 | -0.7 | -5.52 | -13.1 |  |  | no edge shown yet |
| money_level | moneyline | 84-42 | 66.7 | 63.1 | 3.6 | -4.5 | -3.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 42-39 | 51.9 | 48.9 | 2.9 | -1.14 | -1.4 |  |  | no edge shown yet |
| money_level | total | 77-60 | 56.2 | 54.7 | 1.5 | +9.32 | 6.8 |  |  | no edge shown yet |
| sharp_gap | moneyline | 50-64 | 43.9 | 45.3 | -1.4 | -15.17 | -13.3 |  |  | DROP: below break-even |
| sharp_gap | spread | 38-42 | 47.5 | 48.2 | -0.7 | -7.51 | -9.4 |  |  | no edge shown yet |
| sharp_gap | total | 60-64 | 48.4 | 50.3 | -1.9 | -9.37 | -7.6 |  |  | no edge shown yet |
| money_moving | moneyline | 54-59 | 47.8 | 46.5 | 1.3 | -9.55 | -8.5 |  |  | no edge shown yet |
| money_moving | spread | 38-42 | 47.5 | 48.2 | -0.7 | -7.51 | -9.4 |  |  | no edge shown yet |
| money_moving | total | 62-67 | 48.1 | 50.6 | -2.5 | -10.62 | -8.2 |  |  | no edge shown yet |
| pin_value | moneyline | 5-3 | 62.5 | 42.1 | 20.4 | +17.16 | 214.6 |  |  | keep collecting (8/30) |
| pin_value | spread | 33-29 | 53.2 | 50.3 | 3.0 | -0.44 | -0.7 |  |  | no edge shown yet |
| pin_value | total | 40-30 | 57.1 | 51.7 | 5.5 | +5.84 | 8.3 |  |  | no edge shown yet |
| consensus_gap | moneyline | 41-27 | 60.3 | 55.6 | 4.7 | +4.96 | 7.3 |  |  | no edge shown yet |
| consensus_gap | spread | 14-10 | 58.3 | 47.3 | 11.0 | +2.02 | 8.4 |  |  | keep collecting (24/30) |
| consensus_gap | total | 20-13 | 60.6 | 53.4 | 7.2 | +4.77 | 14.5 |  |  | no edge shown yet |
| consensus_gap+money_level | moneyline | 32-11 | 74.4 | 65.1 | 9.3 | +3.14 | 7.3 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+pin_move | moneyline | 19-24 | 44.2 | 45.9 | -1.8 | -5.67 | -13.2 |  |  | no edge shown yet |
| follow_move+rlm_quiet | moneyline | 16-42 | 27.6 | 34.7 | -7.1 | -10.85 | -18.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | moneyline | 8-17 | 32.0 | 35.4 | -3.4 | -5.73 | -22.9 |  |  | keep collecting (25/30) |
| consensus_gap+follow_move | moneyline | 15-12 | 55.6 | 52.9 | 2.6 | -1.34 | -5.0 |  |  | keep collecting (27/30) |
| follow_move+money_level | moneyline | 34-19 | 64.2 | 62.9 | 1.3 | -2.31 | -4.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 49-58 | 45.8 | 45.7 | 0.1 | -9.58 | -9.0 |  |  | no edge shown yet |
| follow_move+money_moving | moneyline | 28-35 | 44.4 | 45.7 | -1.3 | -13.13 | -20.8 |  |  | no edge shown yet |
| follow_move+sharp_gap | moneyline | 27-38 | 41.5 | 44.9 | -3.3 | -16.06 | -24.7 |  |  | DROP: below break-even |
| money_level+money_moving | moneyline | 36-19 | 65.5 | 59.5 | 5.9 | +1.9 | 3.5 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+sharp_gap | moneyline | 32-19 | 62.7 | 59.0 | 3.7 | +1.28 | 2.5 |  |  | no edge shown yet |
| follow_move+rlm_ratio | moneyline | 10-30 | 25.0 | 34.9 | -9.9 | -17.65 | -44.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | moneyline | 7-24 | 22.6 | 34.1 | -11.5 | -14.88 | -48.0 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 10-28 | 26.3 | 35.0 | -8.6 | -15.65 | -41.2 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | moneyline | 5-25 | 16.7 | 34.1 | -17.5 | -18.26 | -60.9 |  |  | INVERT candidate: wrong well beyond its base rate |
| rlm_quiet+sharp_gap | moneyline | 7-27 | 20.6 | 34.1 | -13.5 | -17.88 | -52.6 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 10-30 | 25.0 | 34.9 | -9.9 | -17.65 | -44.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 15-12 | 55.6 | 52.9 | 2.6 | +4.53 | 16.8 |  |  | keep collecting (27/30) |
| consensus_gap+rlm_quiet | moneyline | 2-9 | 18.2 | 34.1 | -15.9 | -5.6 | -50.9 |  |  | keep collecting (11/30) |
| consensus_gap+rlm_ratio | moneyline | 2-5 | 28.6 | 34.1 | -5.6 | -1.6 | -22.9 |  |  | keep collecting (7/30) |
| consensus_gap+sharp_gap | moneyline | 15-14 | 51.7 | 51.6 | 0.1 | +2.81 | 9.7 |  |  | keep collecting (29/30) |
| consensus_gap+pin_rlm | moneyline | 2-2 | 50.0 | 42.1 | 7.9 | +1.4 | 35.0 |  |  | keep collecting (4/30) |
| money_level+pin_rlm | moneyline | 2-1 | 66.7 | 44.7 | 22.0 | +1.16 | 38.7 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | moneyline | 7-12 | 36.8 | 35.8 | 1.0 | -2.7 | -14.2 |  |  | keep collecting (19/30) |
| pin_rlm+sharp_gap | moneyline | 7-13 | 35.0 | 35.7 | -0.7 | -3.7 | -18.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 3-2 | 60.0 | 40.5 | 19.5 | +4.46 | 89.3 |  |  | keep collecting (5/30) |
| money_level+rlm_ratio | moneyline | 3-3 | 50.0 | 39.4 | 10.6 | +0.09 | 1.4 |  |  | keep collecting (6/30) |
| consensus_gap+pin_move | moneyline | 12-4 | 75.0 | 50.0 | 25.0 | +8.35 | 52.2 |  |  | keep collecting (16/30) |
| money_level+pin_move | moneyline | 14-6 | 70.0 | 62.7 | 7.3 | +2.57 | 12.8 |  |  | keep collecting (20/30) |
| consensus_gap+money_delta | moneyline | 3-2 | 60.0 | 40.5 | 19.5 | +4.35 | 86.9 |  |  | keep collecting (5/30) |
| follow_move+money_delta | moneyline | 8-18 | 30.8 | 39.0 | -8.2 | -9.92 | -38.1 |  |  | keep collecting (26/30) |
| follow_move+pin_rlm | moneyline | 6-11 | 35.3 | 34.1 | 1.2 | -3.02 | -17.8 |  |  | keep collecting (17/30) |
| money_delta+money_moving | moneyline | 14-26 | 35.0 | 36.5 | -1.5 | -5.98 | -14.9 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 4-6 | 40.0 | 34.1 | 5.9 | -1.76 | -17.6 |  |  | keep collecting (10/30) |
| money_delta+pin_rlm | moneyline | 4-8 | 33.3 | 34.1 | -0.8 | -3.76 | -31.3 |  |  | keep collecting (12/30) |
| money_delta+rlm_quiet | moneyline | 3-15 | 16.7 | 34.1 | -17.5 | -11.66 | -64.8 |  |  | keep collecting (18/30) |
| money_delta+rlm_ratio | moneyline | 5-17 | 22.7 | 35.6 | -12.8 | -11.5 | -52.3 |  |  | keep collecting (22/30) |
| money_delta+sharp_gap | moneyline | 14-26 | 35.0 | 36.5 | -1.5 | -5.98 | -14.9 |  |  | DROP: below break-even |
| money_moving+pin_move | moneyline | 10-8 | 55.6 | 41.2 | 14.4 | +2.21 | 12.3 |  |  | keep collecting (18/30) |
| pin_move+pin_rlm | moneyline | 6-8 | 42.9 | 34.1 | 8.7 | -0.04 | -0.3 |  |  | keep collecting (14/30) |
| pin_move+rlm_ratio | moneyline | 5-8 | 38.5 | 34.1 | 4.3 | -1.36 | -10.5 |  |  | keep collecting (13/30) |
| pin_move+sharp_gap | moneyline | 10-9 | 52.6 | 40.8 | 11.8 | +1.21 | 6.4 |  |  | keep collecting (19/30) |
| pin_rlm+rlm_quiet | moneyline | 3-10 | 23.1 | 34.1 | -11.1 | -5.52 | -42.5 |  |  | keep collecting (13/30) |
| pin_rlm+rlm_ratio | moneyline | 6-11 | 35.3 | 34.1 | 1.2 | -3.02 | -17.8 |  |  | keep collecting (17/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 44.7 | -11.4 | +8.6 | 286.7 |  |  | keep collecting (3/30) |
| pin_value+rlm_quiet | moneyline | 1-1 | 50.0 | 34.1 | 15.9 | +9.6 | 480.0 |  |  | keep collecting (2/30) |
| money_delta+money_level | moneyline | 5-1 | 83.3 | 50.0 | 33.3 | +4.61 | 76.9 |  |  | keep collecting (6/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_move+pin_value | moneyline | 1-2 | 33.3 | 44.7 | -11.4 | -0.92 | -30.7 |  |  | keep collecting (3/30) |
| money_delta+pin_value | moneyline | 1-0 | 100.0 | 34.1 | 65.9 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 1-0 | 100.0 | 34.1 | 65.9 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 1-0 | 100.0 | 34.1 | 65.9 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| follow_move+pin_move | spread | 20-26 | 43.5 | 52.8 | -9.3 | -7.76 | -16.9 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 38-42 | 47.5 | 48.2 | -0.7 | -7.51 | -9.4 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 9-12 | 42.9 | 55.7 | -12.8 | -3.49 | -16.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | spread | 28-29 | 49.1 | 47.9 | 1.2 | -3.72 | -6.5 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 28-29 | 49.1 | 47.9 | 1.2 | -3.72 | -6.5 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 5-9 | 35.7 | 55.7 | -20.0 | -4.33 | -30.9 |  |  | keep collecting (14/30) |
| consensus_gap+pin_value | spread | 11-8 | 57.9 | 47.9 | 10.0 | +1.51 | 7.9 |  |  | keep collecting (19/30) |
| follow_move+money_level | spread | 12-9 | 57.1 | 53.4 | 3.7 | +2.05 | 9.8 |  |  | keep collecting (21/30) |
| follow_move+money_moving | spread | 11-12 | 47.8 | 53.1 | -5.3 | -1.91 | -8.3 |  |  | keep collecting (23/30) |
| follow_move+sharp_gap | spread | 11-12 | 47.8 | 53.1 | -5.3 | -1.91 | -8.3 |  |  | keep collecting (23/30) |
| money_level+pin_move | spread | 10-9 | 52.6 | 51.3 | 1.4 | -0.13 | -0.7 |  |  | keep collecting (19/30) |
| money_moving+pin_move | spread | 11-10 | 52.4 | 51.1 | 1.2 | -0.28 | -1.3 |  |  | keep collecting (21/30) |
| pin_move+sharp_gap | spread | 11-10 | 52.4 | 51.1 | 1.2 | -0.28 | -1.3 |  |  | keep collecting (21/30) |
| money_delta+money_level | spread | 3-1 | 75.0 | 46.0 | 29.0 | +1.7 | 42.5 |  |  | keep collecting (4/30) |
| money_delta+money_moving | spread | 5-4 | 55.6 | 47.3 | 8.2 | +0.52 | 5.7 |  |  | keep collecting (9/30) |
| money_delta+sharp_gap | spread | 5-4 | 55.6 | 47.3 | 8.2 | +0.52 | 5.7 |  |  | keep collecting (9/30) |
| consensus_gap+money_level | spread | 5-7 | 41.7 | 46.0 | -4.3 | -2.73 | -22.8 |  |  | keep collecting (12/30) |
| consensus_gap+money_moving | spread | 4-5 | 44.4 | 47.3 | -2.9 | -1.53 | -17.0 |  |  | keep collecting (9/30) |
| consensus_gap+sharp_gap | spread | 4-5 | 44.4 | 47.3 | -2.9 | -1.53 | -17.0 |  |  | keep collecting (9/30) |
| money_level+pin_value | spread | 11-9 | 55.0 | 47.6 | 7.4 | +0.45 | 2.3 |  |  | keep collecting (20/30) |
| money_moving+pin_value | spread | 11-12 | 47.8 | 49.7 | -1.8 | -2.44 | -10.6 |  |  | keep collecting (23/30) |
| pin_value+sharp_gap | spread | 11-12 | 47.8 | 49.7 | -1.8 | -2.44 | -10.6 |  |  | keep collecting (23/30) |
| follow_move+money_delta | spread | 4-3 | 57.1 | 55.7 | 1.4 | +0.65 | 9.2 |  |  | keep collecting (7/30) |
| follow_move+rlm_ratio | spread | 1-2 | 33.3 | 52.7 | -19.3 | -1.15 | -38.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.15 | -7.7 |  |  | keep collecting (2/30) |
| money_moving+rlm_ratio | spread | 1-2 | 33.3 | 52.7 | -19.3 | -1.15 | -38.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 1-2 | 33.3 | 52.7 | -19.3 | -1.15 | -38.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 10-7 | 58.8 | 54.2 | 4.6 | +1.85 | 10.9 |  |  | keep collecting (17/30) |
| pin_move+pin_value | spread | 17-9 | 65.4 | 53.1 | 12.3 | +5.85 | 22.5 |  |  | keep collecting (26/30) |
| consensus_gap+pin_move | spread | 5-2 | 71.4 | 51.1 | 20.3 | +2.33 | 33.3 |  |  | keep collecting (7/30) |
| consensus_gap+follow_move | spread | 3-2 | 60.0 | 54.8 | 5.2 | +0.67 | 13.3 |  |  | keep collecting (5/30) |
| consensus_gap+rlm_quiet | spread | 2-0 | 100.0 | 58.0 | 42.0 | +1.82 | 90.9 |  |  | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 2-3 | 40.0 | 58.0 | -18.0 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| money_delta+rlm_quiet | spread | 3-2 | 60.0 | 58.0 | 2.0 | +0.8 | 16.0 |  |  | keep collecting (5/30) |
| money_moving+rlm_quiet | spread | 1-3 | 25.0 | 54.0 | -29.0 | -2.09 | -52.3 |  |  | keep collecting (4/30) |
| rlm_quiet+rlm_ratio | spread | 0-1 | 0.0 | 58.0 | -58.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_quiet+sharp_gap | spread | 1-3 | 25.0 | 54.0 | -29.0 | -2.09 | -52.3 |  |  | keep collecting (4/30) |
| consensus_gap+money_delta | spread | 2-0 | 100.0 | 58.0 | 42.0 | +1.76 | 87.8 |  |  | keep collecting (2/30) |
| money_delta+pin_move | spread | 3-1 | 75.0 | 58.0 | 17.0 | +1.67 | 41.6 |  |  | keep collecting (4/30) |
| money_delta+pin_value | spread | 2-1 | 66.7 | 58.0 | 8.7 | +0.76 | 25.2 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | spread | 1-0 | 100.0 | 58.0 | 42.0 | +0.91 | 90.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | spread | 1-0 | 100.0 | 58.0 | 42.0 | +0.91 | 90.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | spread | 1-0 | 100.0 | 58.0 | 42.0 | +0.91 | 90.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 1-0 | 100.0 | 58.0 | 42.0 | +0.91 | 90.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+rlm_ratio | spread | 1-0 | 100.0 | 58.0 | 42.0 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| money_level+rlm_ratio | spread | 1-0 | 100.0 | 58.0 | 42.0 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| pin_move+rlm_ratio | spread | 1-0 | 100.0 | 58.0 | 42.0 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| pin_value+rlm_ratio | spread | 1-0 | 100.0 | 58.0 | 42.0 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| money_delta+money_moving | total | 22-15 | 59.5 | 44.5 | 14.9 | +5.33 | 14.4 |  |  | no edge shown yet |
| money_delta+sharp_gap | total | 22-14 | 61.1 | 44.6 | 16.5 | +6.33 | 17.6 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 58-63 | 47.9 | 50.4 | -2.4 | -10.22 | -8.4 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 22-39 | 36.1 | 43.9 | -7.8 | -18.53 | -30.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+follow_move | total | 7-6 | 53.8 | 52.5 | 1.3 | +0.23 | 1.8 |  |  | keep collecting (13/30) |
| consensus_gap+money_level | total | 16-9 | 64.0 | 56.0 | 8.0 | +5.14 | 20.5 |  |  | keep collecting (25/30) |
| consensus_gap+money_moving | total | 9-9 | 50.0 | 52.9 | -2.9 | -0.99 | -5.5 |  |  | keep collecting (18/30) |
| consensus_gap+pin_move | total | 3-4 | 42.9 | 52.8 | -9.9 | -1.35 | -19.3 |  |  | keep collecting (7/30) |
| consensus_gap+pin_value | total | 12-7 | 63.2 | 53.1 | 10.1 | +3.63 | 19.1 |  |  | keep collecting (19/30) |
| consensus_gap+sharp_gap | total | 9-8 | 52.9 | 52.7 | 0.3 | +0.01 | 0.1 |  |  | keep collecting (17/30) |
| follow_move+money_level | total | 28-32 | 46.7 | 53.5 | -6.8 | -6.59 | -11.0 |  |  | no edge shown yet |
| follow_move+money_moving | total | 31-43 | 41.9 | 49.3 | -7.4 | -14.69 | -19.8 |  |  | DROP: below break-even |
| follow_move+pin_move | total | 24-43 | 35.8 | 49.1 | -13.3 | -20.99 | -31.3 |  |  | DROP: below break-even |
| follow_move+pin_value | total | 14-12 | 53.8 | 51.5 | 2.3 | +0.5 | 1.9 |  |  | keep collecting (26/30) |
| follow_move+sharp_gap | total | 33-43 | 43.4 | 49.1 | -5.7 | -12.84 | -16.9 |  |  | DROP: below break-even |
| money_level+money_moving | total | 43-38 | 53.1 | 54.1 | -1.0 | +0.8 | 1.0 |  |  | no edge shown yet |
| money_level+pin_move | total | 19-23 | 45.2 | 53.7 | -8.5 | -5.91 | -14.1 |  |  | no edge shown yet |
| money_level+pin_value | total | 21-13 | 61.8 | 55.4 | 6.4 | +5.62 | 16.5 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 42-37 | 53.2 | 53.9 | -0.7 | +0.97 | 1.2 |  |  | no edge shown yet |
| money_moving+pin_move | total | 19-27 | 41.3 | 49.7 | -8.4 | -9.75 | -21.2 |  |  | DROP: below break-even |
| money_moving+pin_value | total | 15-13 | 53.6 | 52.3 | 1.2 | +0.4 | 1.4 |  |  | keep collecting (28/30) |
| pin_move+pin_value | total | 12-14 | 46.2 | 52.0 | -5.9 | -3.28 | -12.6 |  |  | keep collecting (26/30) |
| pin_move+sharp_gap | total | 17-28 | 37.8 | 49.3 | -11.5 | -12.53 | -27.8 |  |  | DROP: below break-even |
| pin_value+sharp_gap | total | 14-12 | 53.8 | 51.5 | 2.3 | +0.5 | 1.9 |  |  | keep collecting (26/30) |
| follow_move+money_delta | total | 18-22 | 45.0 | 44.5 | 0.5 | -5.35 | -13.4 |  |  | no edge shown yet |
| money_delta+pin_move | total | 9-13 | 40.9 | 43.5 | -2.6 | -4.56 | -20.7 |  |  | keep collecting (22/30) |
| money_delta+rlm_quiet | total | 11-16 | 40.7 | 43.5 | -2.7 | -5.79 | -21.4 |  |  | keep collecting (27/30) |
| pin_move+rlm_quiet | total | 11-19 | 36.7 | 44.3 | -7.7 | -8.74 | -29.1 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | total | 19-23 | 45.2 | 46.0 | -0.7 | -5.52 | -13.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | total | 15-12 | 55.6 | 44.9 | 10.6 | +1.84 | 6.8 |  |  | keep collecting (27/30) |
| money_moving+rlm_quiet | total | 11-17 | 39.3 | 43.9 | -4.7 | -6.79 | -24.2 |  |  | keep collecting (28/30) |
| money_moving+rlm_ratio | total | 19-22 | 46.3 | 46.0 | 0.3 | -4.52 | -11.0 |  |  | no edge shown yet |
| rlm_quiet+rlm_ratio | total | 9-15 | 37.5 | 44.0 | -6.5 | -6.65 | -27.7 |  |  | keep collecting (24/30) |
| rlm_quiet+sharp_gap | total | 11-18 | 37.9 | 43.9 | -6.0 | -7.79 | -26.8 |  |  | keep collecting (29/30) |
| rlm_ratio+sharp_gap | total | 19-23 | 45.2 | 46.0 | -0.7 | -5.52 | -13.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | total | 3-0 | 100.0 | 43.5 | 56.5 | +2.71 | 90.4 |  |  | keep collecting (3/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 46.7 | 3.3 | -0.18 | -4.5 |  |  | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 2-1 | 66.7 | 47.8 | 18.8 | +0.8 | 26.7 |  |  | keep collecting (3/30) |
| money_delta+pin_value | total | 9-3 | 75.0 | 44.6 | 30.4 | +5.18 | 43.2 |  |  | keep collecting (12/30) |
| pin_value+rlm_quiet | total | 5-5 | 50.0 | 43.5 | 6.5 | -0.41 | -4.1 |  |  | keep collecting (10/30) |
| pin_value+rlm_ratio | total | 4-1 | 80.0 | 48.7 | 31.3 | +2.56 | 51.2 |  |  | keep collecting (5/30) |
| follow_move+pin_rlm | total | 9-13 | 40.9 | 44.7 | -3.8 | -4.69 | -21.3 |  |  | keep collecting (22/30) |
| money_delta+money_level | total | 6-4 | 60.0 | 46.1 | 13.9 | +1.57 | 15.7 |  |  | keep collecting (10/30) |
| money_delta+pin_rlm | total | 6-7 | 46.2 | 43.5 | 2.7 | -1.37 | -10.6 |  |  | keep collecting (13/30) |
| money_level+pin_rlm | total | 5-3 | 62.5 | 45.1 | 17.4 | +1.59 | 19.9 |  |  | keep collecting (8/30) |
| money_level+rlm_ratio | total | 9-7 | 56.2 | 48.4 | 7.9 | +1.25 | 7.8 |  |  | keep collecting (16/30) |
| money_moving+pin_rlm | total | 9-13 | 40.9 | 44.7 | -3.8 | -4.69 | -21.3 |  |  | keep collecting (22/30) |
| pin_move+pin_rlm | total | 9-14 | 39.1 | 44.6 | -5.5 | -5.69 | -24.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 9-14 | 39.1 | 45.2 | -6.0 | -5.69 | -24.7 |  |  | keep collecting (23/30) |
| pin_rlm+rlm_ratio | total | 9-13 | 40.9 | 44.7 | -3.8 | -4.69 | -21.3 |  |  | keep collecting (22/30) |
| pin_rlm+sharp_gap | total | 9-14 | 39.1 | 44.6 | -5.5 | -5.69 | -24.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | total | 4-9 | 30.8 | 44.5 | -13.7 | -5.28 | -40.6 |  |  | keep collecting (13/30) |
| consensus_gap+pin_rlm | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm+pin_value | total | 2-2 | 50.0 | 46.7 | 3.3 | -0.22 | -5.5 |  |  | keep collecting (4/30) |

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
| rlm_quiet | both | 39-51 | 43.3 | 36.5 | 6.8 | +6.99 | 7.8 | 0.32 | 44.4 | DROP: below break-even |
| pin_move | both | 9-14 | 39.1 | 48.7 | -9.6 | -6.46 | -28.1 | 0.18 | 39.1 | keep collecting (23/30) |
| money_delta | both | 11-9 | 55.0 | 42.0 | 13.0 | +3.34 | 16.7 | 0.05 | 40.0 | keep collecting (20/30) |
| pin_rlm | both | 1-3 | 25.0 | 39.0 | -14.0 | -2.07 | -51.8 | -0.37 | 75.0 | keep collecting (4/30) |
| follow_move | both | 568-511 | 52.6 | 51.6 | 1.0 | -67.58 | -6.3 | 0.18 | 41.1 | no edge shown yet |
| rlm_ratio | both | 34-25 | 57.6 | 39.8 | 17.8 | +17.93 | 30.4 | 0.45 | 52.5 | no edge shown yet |
| money_level | both | 201-133 | 60.2 | 59.0 | 1.2 | -15.83 | -4.7 | -0.12 | 38.9 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 163-149 | 52.2 | 48.3 | 4.0 | +8.62 | 2.8 | 0.31 | 44.2 | no edge shown yet |
| money_moving | both | 122-104 | 54.0 | 50.6 | 3.4 | -5.11 | -2.3 | 0.1 | 43.4 | no edge shown yet |
| pin_value | both | 61-59 | 50.8 | 48.7 | 2.2 | -4.87 | -4.1 | 0.05 | 35.8 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.9 | -31.9 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 282-334 | 45.8 | 48.2 | -2.4 | -54.07 | -8.8 | 0.39 | 45.6 | DROP: below break-even |
| consensus_gap+money_level | both | 43-33 | 56.6 | 62.6 | -6.1 | -9.38 | -12.3 | 0.17 | 46.1 | no edge shown yet |
| consensus_gap+money_moving | both | 21-26 | 44.7 | 47.3 | -2.6 | -7.26 | -15.4 | 0.32 | 44.7 | no edge shown yet |
| consensus_gap+pin_value | both | 25-29 | 46.3 | 47.0 | -0.7 | -7.24 | -13.4 | 0.34 | 46.3 | no edge shown yet |
| follow_move+rlm_quiet | both | 39-51 | 43.3 | 36.5 | 6.8 | +6.99 | 7.8 | 0.32 | 44.4 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 34-25 | 57.6 | 39.8 | 17.8 | +17.93 | 30.4 | 0.45 | 52.5 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 84-50 | 62.7 | 49.6 | 13.1 | +20.95 | 15.6 | 0.49 | 48.5 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 75-49 | 60.5 | 57.8 | 2.7 | -2.32 | -1.9 | -0.09 | 46.0 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 13-11 | 54.2 | 50.4 | 3.8 | +0.63 | 2.6 | 0.57 | 50.0 | keep collecting (24/30) |
| money_moving+pin_value | both | 10-7 | 58.8 | 50.7 | 8.1 | +1.78 | 10.5 | 0.39 | 41.2 | keep collecting (17/30) |
| rlm_quiet+rlm_ratio | both | 20-15 | 57.1 | 36.5 | 20.6 | +13.73 | 39.2 | -0.12 | 45.7 | no edge shown yet |
| rlm_quiet+sharp_gap | both | 22-19 | 53.7 | 36.8 | 16.8 | +11.55 | 28.2 | -0.12 | 43.9 | no edge shown yet |
| rlm_ratio+sharp_gap | both | 34-25 | 57.6 | 39.8 | 17.8 | +17.93 | 30.4 | 0.45 | 52.5 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 109-74 | 59.6 | 55.6 | 3.9 | -0.49 | -0.3 | 0.16 | 44.3 | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | both | 73-63 | 53.7 | 48.2 | 5.5 | +3.09 | 2.3 | 0.28 | 47.1 | no edge shown yet |
| money_delta+money_level | both | 4-3 | 57.1 | 46.9 | 10.2 | +1.37 | 19.5 | 1.26 | 71.4 | keep collecting (7/30) |
| money_delta+money_moving | both | 10-9 | 52.6 | 41.6 | 11.0 | +2.43 | 12.8 | 0.06 | 42.1 | keep collecting (19/30) |
| money_delta+pin_value | both | 4-1 | 80.0 | 49.8 | 30.2 | +2.52 | 50.4 | 0.2 | 40.0 | keep collecting (5/30) |
| money_delta+sharp_gap | both | 8-7 | 53.3 | 41.2 | 12.2 | +2.69 | 18.0 | 0.07 | 53.3 | keep collecting (15/30) |
| pin_value+sharp_gap | both | 14-10 | 58.3 | 49.8 | 8.6 | +2.57 | 10.7 | 0.08 | 41.7 | keep collecting (24/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 50.9 | -50.9 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 39-46 | 45.9 | 51.5 | -5.6 | -15.12 | -17.8 | 0.74 | 56.5 | no edge shown yet |
| consensus_gap+rlm_quiet | both | 4-7 | 36.4 | 37.4 | -1.0 | -2.99 | -27.1 | 0.95 | 72.7 | keep collecting (11/30) |
| follow_move+pin_value | both | 23-21 | 52.3 | 48.7 | 3.5 | -0.86 | -2.0 | -0.21 | 27.3 | no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 42.7 | -26.0 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 31-49 | 38.8 | 45.8 | -7.0 | -10.46 | -13.1 | 0.78 | 50.0 | DROP: below break-even |
| follow_move+money_level | both | 102-53 | 65.8 | 60.0 | 5.8 | -2.4 | -1.5 | 0.09 | 43.2 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 12-10 | 54.5 | 44.2 | 10.3 | +2.34 | 10.6 | 1.43 | 68.2 | keep collecting (22/30) |
| pin_value+rlm_ratio | both | 3-2 | 60.0 | 45.3 | 14.7 | +0.73 | 14.5 | -1.16 | 40.0 | keep collecting (5/30) |
| follow_move+money_moving | both | 63-39 | 61.8 | 52.1 | 9.7 | +8.48 | 8.3 | 0.37 | 51.0 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 4-0 | 100.0 | 49.4 | 50.6 | +3.52 | 88.0 | 0.25 | 25.0 | keep collecting (4/30) |
| follow_move+money_delta | both | 6-4 | 60.0 | 42.7 | 17.3 | +3.86 | 38.6 | 0.34 | 50.0 | keep collecting (10/30) |
| money_delta+rlm_quiet | both | 2-2 | 50.0 | 38.0 | 12.0 | +1.53 | 38.3 | -2.1 | 0.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | both | 16-15 | 51.6 | 37.4 | 14.2 | +6.23 | 20.1 | 0.4 | 45.2 | no edge shown yet |
| money_moving+rlm_ratio | both | 17-11 | 60.7 | 41.9 | 18.8 | +9.06 | 32.4 | 0.49 | 53.6 | keep collecting (28/30) |
| consensus_gap+rlm_ratio | both | 5-4 | 55.6 | 39.7 | 15.8 | +1.0 | 11.1 | 0.72 | 66.7 | keep collecting (9/30) |
| pin_move+pin_value | both | 3-8 | 27.3 | 49.3 | -22.0 | -5.27 | -47.9 | 0.18 | 18.2 | keep collecting (11/30) |
| follow_move+pin_move | both | 6-6 | 50.0 | 50.6 | -0.6 | -1.19 | -9.9 | 0.45 | 50.0 | keep collecting (12/30) |
| consensus_gap+pin_move | both | 1-5 | 16.7 | 45.4 | -28.8 | -4.09 | -68.2 | 0.22 | 50.0 | keep collecting (6/30) |
| money_level+pin_move | both | 3-3 | 50.0 | 54.1 | -4.1 | -0.96 | -16.0 | 0.57 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 28.0 | -28.0 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-2 | 33.3 | 42.7 | -9.3 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 28.0 | -28.0 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 28.0 | -28.0 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-2 | 33.3 | 42.7 | -9.3 | -1.07 | -35.8 | -0.93 | 66.7 | keep collecting (3/30) |
| pin_rlm+sharp_gap | both | 1-3 | 25.0 | 39.0 | -14.0 | -2.07 | -51.8 | -0.37 | 75.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.1 | -51.1 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 49.1 | -49.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-2 | 50.0 | 50.4 | -0.4 | -0.87 | -21.7 | 0.7 | 50.0 | keep collecting (4/30) |
| money_level+pin_rlm | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.07 | -3.7 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 28.0 | 72.0 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 28.0 | 72.0 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 3-2 | 60.0 | 40.7 | 19.3 | +3.25 | 65.0 | 1.12 | 80.0 | keep collecting (5/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 28.0 | -28.0 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 21-33 | 38.9 | 28.0 | 10.9 | +8.7 | 16.1 | 0.21 | 44.4 | DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.4 | 10.6 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 15-16 | 48.4 | 49.4 | -1.0 | -2.36 | -7.6 | 0.71 | 51.6 | no edge shown yet |
| pin_move | moneyline | 2-3 | 40.0 | 45.6 | -5.6 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-6 | 14.3 | 48.7 | -34.4 | -5.09 | -72.7 | 0.29 | 28.6 | keep collecting (7/30) |
| pin_move | total | 6-5 | 54.5 | 50.2 | 4.3 | +0.5 | 4.5 | 0.18 | 36.4 | keep collecting (11/30) |
| money_delta | moneyline | 2-5 | 28.6 | 28.0 | 0.6 | -0.66 | -9.4 | -0.99 | 42.9 | keep collecting (7/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 8-3 | 72.7 | 49.5 | 23.3 | +4.17 | 37.9 | 0.64 | 36.4 | keep collecting (11/30) |
| pin_rlm | moneyline | 1-3 | 25.0 | 39.0 | -14.0 | -2.07 | -51.8 | -0.37 | 75.0 | keep collecting (4/30) |
| follow_move | moneyline | 235-158 | 59.8 | 54.7 | 5.1 | -19.96 | -5.1 | 0.14 | 43.8 | PROMOTE: beats break-even and its own base rate |
| follow_move | spread | 150-176 | 46.0 | 49.7 | -3.7 | -37.71 | -11.6 | -0.01 | 33.1 | DROP: below break-even |
| follow_move | total | 183-177 | 50.8 | 50.0 | 0.9 | -9.91 | -2.8 | 0.41 | 45.3 | no edge shown yet |
| rlm_ratio | moneyline | 14-15 | 48.3 | 29.5 | 18.8 | +9.47 | 32.6 | 0.36 | 55.2 | keep collecting (29/30) |
| rlm_ratio | spread | 3-3 | 50.0 | 52.1 | -2.1 | -0.16 | -2.7 | 0.33 | 16.7 | keep collecting (6/30) |
| rlm_ratio | total | 17-7 | 70.8 | 49.3 | 21.5 | +8.62 | 35.9 | 0.58 | 58.3 | keep collecting (24/30) |
| money_level | moneyline | 114-51 | 69.1 | 68.0 | 1.1 | -12.76 | -7.7 | -0.27 | 41.8 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-18 | 48.6 | 49.0 | -0.5 | -2.69 | -7.7 | 1.0 | 51.4 | no edge shown yet |
| money_level | total | 70-64 | 52.2 | 50.4 | 1.8 | -0.38 | -0.3 | -0.22 | 32.1 | no edge shown yet |
| sharp_gap | moneyline | 69-78 | 46.9 | 46.6 | 0.4 | -5.82 | -4.0 | 0.37 | 51.0 | no edge shown yet |
| sharp_gap | spread | 20-15 | 57.1 | 49.7 | 7.4 | +3.0 | 8.6 | 0.77 | 40.0 | no edge shown yet |
| sharp_gap | total | 74-56 | 56.9 | 49.9 | 7.1 | +11.44 | 8.8 | 0.12 | 37.7 | no edge shown yet |
| money_moving | moneyline | 53-54 | 49.5 | 51.4 | -1.9 | -17.73 | -16.6 | -0.02 | 49.5 | no edge shown yet |
| money_moving | spread | 18-6 | 75.0 | 49.0 | 26.0 | +10.18 | 42.4 | 0.5 | 45.8 | keep collecting (24/30) |
| money_moving | total | 51-44 | 53.7 | 50.0 | 3.7 | +2.44 | 2.6 | 0.13 | 35.8 | no edge shown yet |
| pin_value | moneyline | 2-7 | 22.2 | 37.8 | -15.5 | -5.31 | -59.0 | 0.12 | 55.6 | keep collecting (9/30) |
| pin_value | spread | 31-26 | 54.4 | 49.1 | 5.3 | +1.17 | 2.1 | 0.14 | 33.3 | no edge shown yet |
| pin_value | total | 28-26 | 51.9 | 50.1 | 1.8 | -0.74 | -1.4 | -0.06 | 35.2 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 53.1 | -19.8 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 117-184 | 38.9 | 46.9 | -8.0 | -50.44 | -16.8 | 0.11 | 42.5 | DROP: below break-even |
| consensus_gap | spread | 78-71 | 52.3 | 48.9 | 3.5 | -2.78 | -1.9 | 0.34 | 39.6 | no edge shown yet |
| consensus_gap | total | 87-79 | 52.4 | 50.1 | 2.3 | -0.85 | -0.5 | 0.95 | 56.6 | no edge shown yet |
| money_level+sharp_gap | moneyline | 51-26 | 66.2 | 63.4 | 2.8 | -5.15 | -6.7 | 0.08 | 53.2 | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+follow_move | moneyline | 15-23 | 39.5 | 54.6 | -15.2 | -13.52 | -35.6 | 0.13 | 52.6 | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 33.5 | -8.5 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| consensus_gap+rlm_quiet | moneyline | 1-5 | 16.7 | 28.0 | -11.3 | -3.68 | -61.3 | 1.07 | 83.3 | keep collecting (6/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.7 | -9.3 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 21-33 | 38.9 | 28.0 | 10.9 | +8.7 | 16.1 | 0.21 | 44.4 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 35-17 | 67.3 | 68.6 | -1.3 | -6.85 | -13.2 | -0.5 | 48.1 | beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 28.0 | -28.0 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 19-39 | 32.8 | 44.7 | -11.9 | -11.11 | -19.1 | 0.74 | 50.0 | DROP: below break-even |
| follow_move+money_level | moneyline | 65-20 | 76.5 | 68.4 | 8.1 | -3.01 | -3.5 | -0.19 | 43.5 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 33-16 | 67.3 | 54.9 | 12.4 | +4.06 | 8.3 | 0.12 | 53.1 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 32-23 | 58.2 | 68.0 | -9.8 | -9.04 | -16.4 | -0.12 | 43.6 | no edge shown yet |
| follow_move+sharp_gap | moneyline | 38-23 | 62.3 | 49.6 | 12.7 | +6.08 | 10.0 | 0.44 | 54.1 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 26-34 | 43.3 | 46.3 | -3.0 | -10.66 | -17.8 | 0.28 | 56.7 | no edge shown yet |
| consensus_gap+money_moving | moneyline | 11-24 | 31.4 | 46.9 | -15.4 | -14.01 | -40.0 | 0.32 | 48.6 | INVERT candidate: wrong well beyond its base rate |
| follow_move+rlm_ratio | moneyline | 14-15 | 48.3 | 29.5 | 18.8 | +9.47 | 32.6 | 0.36 | 55.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 10-11 | 47.6 | 28.0 | 19.7 | +8.6 | 41.0 | -0.24 | 42.9 | keep collecting (21/30) |
| rlm_quiet+sharp_gap | moneyline | 10-14 | 41.7 | 28.0 | 13.7 | +5.6 | 23.3 | -0.38 | 41.7 | keep collecting (24/30) |
| rlm_ratio+sharp_gap | moneyline | 14-15 | 48.3 | 29.5 | 18.8 | +9.47 | 32.6 | 0.36 | 55.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 28.0 | -3.0 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 7-10 | 41.2 | 28.0 | 13.2 | +3.13 | 18.4 | 0.55 | 52.9 | keep collecting (17/30) |
| money_moving+rlm_ratio | moneyline | 5-5 | 50.0 | 28.0 | 22.0 | +3.98 | 39.8 | 0.08 | 50.0 | keep collecting (10/30) |
| money_delta+money_moving | moneyline | 2-5 | 28.6 | 28.0 | 0.6 | -0.66 | -9.4 | -0.99 | 42.9 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-4 | 33.3 | 28.0 | 5.4 | +0.34 | 5.7 | -1.15 | 50.0 | keep collecting (6/30) |
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
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 28.0 | 38.7 | +3.34 | 111.3 | -1.53 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 1-1 | 50.0 | 28.0 | 22.0 | +1.7 | 85.0 | -4.2 | 0.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 28.0 | 72.0 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 28.0 | -28.0 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-0 | 100.0 | 28.0 | 72.0 | +1.64 | 164.0 | 3.8 | 100.0 | keep collecting (1/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 72.0 | -72.0 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 72.0 | -72.0 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 46.9 | -1.4 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 46.9 | 36.4 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 13-9 | 59.1 | 48.3 | 10.8 | +2.17 | 9.9 | 0.32 | 40.9 | keep collecting (22/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.4 | 10.6 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-3 | 50.0 | 52.1 | -2.1 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-7 | 58.8 | 48.7 | 10.1 | +2.09 | 12.3 | 0.88 | 41.2 | keep collecting (17/30) |
| money_level+money_moving | spread | 10-6 | 62.5 | 48.4 | 14.1 | +3.12 | 19.5 | 1.19 | 68.8 | keep collecting (16/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.7 | -5.8 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 4-2 | 66.7 | 49.0 | 17.7 | +1.41 | 23.5 | 0.5 | 50.0 | keep collecting (6/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 3-3 | 50.0 | 52.1 | -2.1 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 53.1 | -53.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 53.1 | -53.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-12 | 53.8 | 49.0 | 4.8 | +0.62 | 2.4 | 1.15 | 46.2 | keep collecting (26/30) |
| money_moving+sharp_gap | spread | 10-4 | 71.4 | 49.1 | 22.3 | +5.04 | 36.0 | 0.86 | 50.0 | keep collecting (14/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.0 | 17.7 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-11 | 45.0 | 47.8 | -2.8 | -3.2 | -16.0 | 0.85 | 45.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 46.9 | 15.6 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 11-10 | 52.4 | 48.4 | 4.0 | +0.04 | 0.2 | 0.9 | 47.6 | keep collecting (21/30) |
| follow_move+pin_value | spread | 13-8 | 61.9 | 48.4 | 13.5 | +3.36 | 16.0 | 0.19 | 28.6 | keep collecting (21/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 46.9 | 53.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_quiet | spread | 1-0 | 100.0 | 46.9 | 53.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 46.9 | 53.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-3 | 75.0 | 47.9 | 27.1 | +5.22 | 43.5 | 0.75 | 50.0 | keep collecting (12/30) |
| money_delta+rlm_quiet | spread | 1-0 | 100.0 | 46.9 | 53.1 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+rlm_quiet | spread | 2-0 | 100.0 | 46.9 | 53.1 | +1.74 | 87.1 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 2-2 | 50.0 | 53.1 | -3.1 | -0.07 | -1.7 | 1.25 | 25.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | spread | 2-1 | 66.7 | 51.0 | 15.6 | +0.86 | 28.7 | 1.0 | 33.3 | keep collecting (3/30) |
| pin_move+pin_value | spread | 1-5 | 16.7 | 47.9 | -31.3 | -4.09 | -68.2 | 0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 46.9 | -46.9 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-3 | 25.0 | 46.9 | -21.9 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 53.1 | -53.1 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 15-16 | 48.4 | 49.4 | -1.0 | -2.36 | -7.6 | 0.71 | 51.6 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 30-26 | 53.6 | 50.3 | 3.3 | +1.41 | 2.5 | -0.07 | 37.5 | no edge shown yet |
| money_level+sharp_gap | total | 44-36 | 55.0 | 50.2 | 4.8 | +4.04 | 5.1 | -0.09 | 35.0 | no edge shown yet |
| money_moving+sharp_gap | total | 37-25 | 59.7 | 49.8 | 9.8 | +8.72 | 14.1 | 0.15 | 37.1 | no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 50.9 | -50.9 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 10-6 | 62.5 | 49.8 | 12.7 | +3.05 | 19.1 | 0.44 | 37.5 | keep collecting (16/30) |
| money_moving+pin_value | total | 6-4 | 60.0 | 49.7 | 10.3 | +1.38 | 13.8 | 0.2 | 30.0 | keep collecting (10/30) |
| pin_value+sharp_gap | total | 12-7 | 63.2 | 49.9 | 13.3 | +3.83 | 20.2 | 0.16 | 36.8 | keep collecting (19/30) |
| follow_move+money_level | total | 26-23 | 53.1 | 50.4 | 2.7 | +0.58 | 1.2 | 0.22 | 40.8 | no edge shown yet |
| follow_move+pin_value | total | 9-11 | 45.0 | 50.0 | -5.0 | -2.94 | -14.7 | -0.45 | 25.0 | keep collecting (20/30) |
| follow_move+rlm_ratio | total | 17-7 | 70.8 | 49.3 | 21.5 | +8.62 | 35.9 | 0.58 | 58.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 36-20 | 64.3 | 49.9 | 14.4 | +12.78 | 22.8 | 0.41 | 44.6 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 6-4 | 60.0 | 49.3 | 10.7 | +1.54 | 15.4 | 1.1 | 70.0 | keep collecting (10/30) |
| pin_value+rlm_ratio | total | 3-1 | 75.0 | 49.6 | 25.4 | +1.73 | 43.2 | -0.25 | 50.0 | keep collecting (4/30) |
| rlm_ratio+sharp_gap | total | 17-7 | 70.8 | 49.3 | 21.5 | +8.62 | 35.9 | 0.58 | 58.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 21-20 | 51.2 | 49.9 | 1.4 | -0.8 | -2.0 | 0.56 | 48.8 | no edge shown yet |
| consensus_gap+money_level | total | 6-4 | 60.0 | 50.3 | 9.7 | +1.34 | 13.4 | 0.0 | 30.0 | keep collecting (10/30) |
| consensus_gap+money_moving | total | 5-1 | 83.3 | 50.3 | 33.0 | +3.43 | 57.2 | -0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+pin_value | total | 10-14 | 41.7 | 50.2 | -8.5 | -5.11 | -21.3 | 0.5 | 50.0 | keep collecting (24/30) |
| consensus_gap+sharp_gap | total | 7-7 | 50.0 | 49.8 | 0.2 | -0.67 | -4.8 | 0.14 | 35.7 | keep collecting (14/30) |
| money_moving+rlm_ratio | total | 10-5 | 66.7 | 49.4 | 17.3 | +4.22 | 28.1 | 0.67 | 60.0 | keep collecting (15/30) |
| consensus_gap+follow_move | total | 15-12 | 55.6 | 49.9 | 5.7 | +1.6 | 5.9 | 1.52 | 70.4 | keep collecting (27/30) |
| consensus_gap+money_delta | total | 3-0 | 100.0 | 50.3 | 49.7 | +2.69 | 89.6 | 0.33 | 33.3 | keep collecting (3/30) |
| follow_move+money_delta | total | 3-3 | 50.0 | 49.4 | 0.6 | -0.31 | -5.2 | 1.33 | 66.7 | keep collecting (6/30) |
| money_delta+money_moving | total | 7-3 | 70.0 | 49.5 | 20.5 | +3.26 | 32.6 | 0.7 | 40.0 | keep collecting (10/30) |
| money_delta+pin_value | total | 3-0 | 100.0 | 49.7 | 50.3 | +2.69 | 89.6 | 0.0 | 33.3 | keep collecting (3/30) |
| money_delta+sharp_gap | total | 6-2 | 75.0 | 49.6 | 25.4 | +3.35 | 41.9 | 0.88 | 50.0 | keep collecting (8/30) |
| money_moving+rlm_quiet | total | 7-5 | 58.3 | 49.3 | 9.0 | +1.36 | 11.4 | 0.42 | 41.7 | keep collecting (12/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 9-3 | 75.0 | 49.3 | 25.7 | +5.22 | 43.5 | 0.33 | 58.3 | keep collecting (12/30) |
| rlm_quiet+sharp_gap | total | 11-4 | 73.3 | 49.3 | 24.1 | +6.04 | 40.3 | 0.47 | 53.3 | keep collecting (15/30) |
| follow_move+pin_move | total | 3-2 | 60.0 | 49.5 | 10.5 | +0.77 | 15.4 | 0.8 | 60.0 | keep collecting (5/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 49.1 | -49.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 49.1 | -49.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 3-2 | 60.0 | 49.5 | 10.5 | +0.73 | 14.5 | 0.8 | 60.0 | keep collecting (5/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 49.1 | 0.9 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 4-1 | 80.0 | 49.1 | 30.9 | +2.68 | 53.6 | 0.4 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | total | 1-2 | 33.3 | 50.9 | -17.5 | -1.09 | -36.4 | 1.0 | 33.3 | keep collecting (3/30) |
| pin_move+pin_value | total | 2-3 | 40.0 | 50.9 | -10.9 | -1.18 | -23.6 | 0.2 | 20.0 | keep collecting (5/30) |
| pin_move+sharp_gap | total | 0-2 | 0.0 | 50.9 | -50.9 | -2.0 | -100.0 | 1.5 | 50.0 | keep collecting (2/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 49.1 | -49.1 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 1-2 | 33.3 | 49.1 | -15.8 | -1.09 | -36.4 | 1.67 | 100.0 | keep collecting (3/30) |
| consensus_gap+pin_move | total | 1-0 | 100.0 | 50.9 | 49.1 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 229-349 | 39.6 | 41.9 | -2.3 | -66.79 | -11.6 |  |  | DROP: below break-even |
| pin_move | both | 588-605 | 49.3 | 49.7 | -0.5 | -52.52 | -4.4 |  |  | DROP: below break-even |
| money_delta | both | 369-484 | 43.3 | 44.1 | -0.8 | -63.23 | -7.4 |  |  | DROP: below break-even |
| pin_rlm | both | 157-188 | 45.5 | 42.1 | 3.4 | +18.81 | 5.5 |  |  | DROP: below break-even |
| follow_move | both | 1007-949 | 51.5 | 51.3 | 0.2 | -134.72 | -6.9 |  |  | no edge shown yet |
| rlm_ratio | both | 230-280 | 45.1 | 43.8 | 1.3 | -23.18 | -4.5 |  |  | DROP: below break-even |
| money_level | both | 1285-945 | 57.6 | 55.4 | 2.2 | -63.15 | -2.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 993-1145 | 46.4 | 47.5 | -1.0 | -150.63 | -7.0 |  |  | DROP: below break-even |
| money_moving | both | 1000-1143 | 46.7 | 47.8 | -1.1 | -153.87 | -7.2 |  |  | DROP: below break-even |
| pin_value | both | 433-422 | 50.6 | 48.2 | 2.4 | +26.33 | 3.1 |  |  | no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 51.0 | 15.6 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 405-498 | 44.9 | 48.3 | -3.4 | -75.85 | -8.4 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 152-147 | 50.8 | 51.4 | -0.6 | -15.67 | -5.2 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 175-267 | 39.6 | 45.6 | -6.0 | -29.8 | -6.7 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 101-95 | 51.5 | 50.7 | 0.8 | +10.44 | 5.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 25-44 | 36.2 | 38.2 | -2.0 | +8.43 | 12.2 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 161-164 | 49.5 | 46.2 | 3.4 | +14.95 | 4.6 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | both | 30-49 | 38.0 | 39.8 | -1.8 | -1.61 | -2.0 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 174-272 | 39.0 | 45.0 | -6.0 | -31.51 | -7.1 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 527-576 | 47.8 | 49.0 | -1.2 | -96.05 | -8.7 |  |  | DROP: below break-even |
| follow_move+pin_move | both | 420-449 | 48.3 | 49.9 | -1.6 | -67.17 | -7.7 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 123-138 | 47.1 | 43.7 | 3.5 | -3.14 | -1.2 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 150-142 | 51.4 | 49.0 | 2.3 | +1.3 | 0.4 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 230-280 | 45.1 | 43.8 | 1.3 | -23.18 | -4.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 533-576 | 48.1 | 48.8 | -0.7 | -87.02 | -7.8 |  |  | DROP: below break-even |
| money_moving+pin_move | both | 339-376 | 47.4 | 48.4 | -1.0 | -35.79 | -5.0 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 151-182 | 45.3 | 42.1 | 3.3 | +18.84 | 5.7 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 184-211 | 46.6 | 47.5 | -0.9 | -12.65 | -3.2 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 222-270 | 45.1 | 43.9 | 1.3 | -21.09 | -4.3 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 956-1100 | 46.5 | 47.5 | -1.0 | -137.53 | -6.7 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 145-156 | 48.2 | 43.9 | 4.3 | +16.68 | 5.5 |  |  | no edge shown yet |
| pin_move+pin_value | both | 187-182 | 50.7 | 49.2 | 1.5 | -4.35 | -1.2 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 131-135 | 49.2 | 45.1 | 4.1 | +6.05 | 2.3 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 344-379 | 47.6 | 48.3 | -0.7 | -34.33 | -4.7 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 43-44 | 49.4 | 45.9 | 3.5 | +12.27 | 14.1 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 123-138 | 47.1 | 43.7 | 3.5 | -3.14 | -1.2 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 157-188 | 45.5 | 42.1 | 3.4 | +18.81 | 5.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 43-34 | 55.8 | 48.5 | 7.3 | +5.14 | 6.7 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 185-211 | 46.7 | 47.4 | -0.7 | -11.76 | -3.0 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 230-280 | 45.1 | 43.8 | 1.3 | -23.18 | -4.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 181-219 | 45.2 | 45.7 | -0.4 | -37.09 | -9.3 |  |  | DROP: below break-even |
| money_level+money_moving | both | 703-617 | 53.3 | 52.3 | 1.0 | -47.33 | -3.6 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 689-607 | 53.2 | 52.1 | 1.1 | -40.32 | -3.1 |  |  | no edge shown yet |
| follow_move+money_level | both | 638-461 | 58.1 | 56.3 | 1.8 | -51.44 | -4.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 108-91 | 54.3 | 48.0 | 6.3 | +12.87 | 6.5 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 255-192 | 57.0 | 58.2 | -1.2 | -18.04 | -4.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_move | both | 336-307 | 52.3 | 53.1 | -0.8 | -32.24 | -5.0 |  |  | no edge shown yet |
| money_level+pin_value | both | 206-182 | 53.1 | 49.9 | 3.2 | -2.66 | -0.7 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 25-58 | 30.1 | 36.8 | -6.7 | -13.04 | -15.7 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | both | 229-349 | 39.6 | 41.9 | -2.3 | -66.79 | -11.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 117-197 | 37.3 | 41.3 | -4.0 | -48.49 | -15.4 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 267-375 | 41.6 | 42.4 | -0.9 | -48.3 | -7.5 |  |  | DROP: below break-even |
| consensus_gap+money_delta | both | 49-111 | 30.6 | 37.9 | -7.3 | -21.86 | -13.7 |  |  | DROP: below break-even |
| money_delta+money_level | both | 131-117 | 52.8 | 47.1 | 5.8 | +19.47 | 7.9 |  |  | no edge shown yet |
| money_delta+pin_value | both | 80-76 | 51.3 | 47.2 | 4.1 | +3.87 | 2.5 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 264-369 | 41.7 | 42.4 | -0.7 | -45.47 | -7.2 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 93-163 | 36.3 | 40.0 | -3.6 | -37.54 | -14.7 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | both | 109-190 | 36.5 | 41.2 | -4.8 | -47.39 | -15.8 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 66-120 | 35.5 | 42.7 | -7.2 | -47.44 | -25.5 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | both | 112-153 | 42.3 | 43.9 | -1.7 | -25.06 | -9.5 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 49-83 | 37.1 | 40.5 | -3.4 | -21.28 | -16.1 |  |  | DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 51.0 | 15.6 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 134-159 | 45.7 | 46.1 | -0.4 | -14.59 | -5.0 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 70-48 | 59.3 | 46.6 | 12.7 | +21.0 | 17.8 |  |  | PROMOTE: beats break-even and its own base rate |
| money_delta+pin_rlm | both | 92-110 | 45.5 | 42.0 | 3.6 | +6.3 | 3.1 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | both | 131-146 | 47.3 | 44.2 | 3.1 | -9.91 | -3.6 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | both | 32-45 | 41.6 | 47.1 | -5.6 | -5.57 | -7.2 |  |  | DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 49.1 | 50.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 68-152 | 30.9 | 28.8 | 2.1 | -18.31 | -8.3 |  |  | DROP: below break-even |
| rlm_quiet | spread | 54-56 | 49.1 | 51.2 | -2.1 | -5.82 | -5.3 |  |  | no edge shown yet |
| rlm_quiet | total | 107-141 | 43.1 | 49.5 | -6.4 | -42.66 | -17.2 |  |  | DROP: below break-even |
| pin_move | moneyline | 130-127 | 50.6 | 48.5 | 2.0 | +7.94 | 3.1 |  |  | no edge shown yet |
| pin_move | spread | 228-239 | 48.8 | 50.3 | -1.5 | -31.37 | -6.7 |  |  | DROP: below break-even |
| pin_move | total | 230-239 | 49.0 | 49.8 | -0.8 | -29.09 | -6.2 |  |  | no edge shown yet |
| money_delta | moneyline | 64-192 | 25.0 | 29.9 | -4.9 | -50.05 | -19.6 |  |  | DROP: below break-even |
| money_delta | spread | 130-131 | 49.8 | 51.1 | -1.3 | -12.52 | -4.8 |  |  | no edge shown yet |
| money_delta | total | 175-161 | 52.1 | 49.5 | 2.6 | -0.65 | -0.2 |  |  | no edge shown yet |
| pin_rlm | moneyline | 45-87 | 34.1 | 29.6 | 4.5 | +17.27 | 13.1 |  |  | DROP: below break-even |
| pin_rlm | spread | 26-23 | 53.1 | 51.3 | 1.7 | +0.7 | 1.4 |  |  | no edge shown yet |
| pin_rlm | total | 86-78 | 52.4 | 49.4 | 3.0 | +0.84 | 0.5 |  |  | no edge shown yet |
| follow_move | moneyline | 368-269 | 57.8 | 54.4 | 3.4 | -37.21 | -5.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 289-308 | 48.4 | 49.6 | -1.2 | -45.0 | -7.5 |  |  | DROP: below break-even |
| follow_move | total | 350-372 | 48.5 | 49.9 | -1.5 | -52.52 | -7.3 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 47-110 | 29.9 | 30.5 | -0.6 | -20.43 | -13.0 |  |  | DROP: below break-even |
| rlm_ratio | spread | 42-45 | 48.3 | 50.2 | -2.0 | -6.92 | -7.9 |  |  | no edge shown yet |
| rlm_ratio | total | 141-125 | 53.0 | 49.5 | 3.5 | +4.17 | 1.6 |  |  | no edge shown yet |
| money_level | moneyline | 500-199 | 71.5 | 68.0 | 3.5 | -27.28 | -3.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 357-365 | 49.4 | 49.1 | 0.4 | -42.98 | -6.0 |  |  | DROP: below break-even |
| money_level | total | 428-381 | 52.9 | 50.3 | 2.7 | +7.11 | 0.9 |  |  | no edge shown yet |
| sharp_gap | moneyline | 251-390 | 39.2 | 42.3 | -3.2 | -69.31 | -10.8 |  |  | DROP: below break-even |
| sharp_gap | spread | 361-352 | 50.6 | 49.4 | 1.2 | -26.06 | -3.7 |  |  | no edge shown yet |
| sharp_gap | total | 381-403 | 48.6 | 49.8 | -1.2 | -55.25 | -7.0 |  |  | DROP: below break-even |
| money_moving | moneyline | 263-375 | 41.2 | 43.4 | -2.2 | -54.65 | -8.6 |  |  | DROP: below break-even |
| money_moving | spread | 358-355 | 50.2 | 49.4 | 0.8 | -31.94 | -4.5 |  |  | no edge shown yet |
| money_moving | total | 379-413 | 47.9 | 49.9 | -2.0 | -67.29 | -8.5 |  |  | DROP: below break-even |
| pin_value | moneyline | 23-57 | 28.7 | 32.4 | -3.6 | +28.04 | 35.0 |  |  | DROP: below break-even |
| pin_value | spread | 192-177 | 52.0 | 49.6 | 2.5 | -9.71 | -2.6 |  |  | no edge shown yet |
| pin_value | total | 218-188 | 53.7 | 50.1 | 3.5 | +8.01 | 2.0 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 53.1 | 46.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 181-299 | 37.7 | 47.0 | -9.3 | -72.38 | -15.1 |  |  | DROP: below break-even |
| consensus_gap | spread | 99-85 | 53.8 | 48.9 | 4.9 | -0.51 | -0.3 |  |  | no edge shown yet |
| consensus_gap | total | 125-114 | 52.3 | 50.4 | 1.9 | -2.96 | -1.2 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 181-102 | 64.0 | 62.5 | 1.4 | -4.8 | -1.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 168-100 | 62.7 | 62.0 | 0.7 | -5.03 | -1.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 236-360 | 39.6 | 42.4 | -2.8 | -50.97 | -8.6 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 67-79 | 45.9 | 53.3 | -7.4 | -21.77 | -14.9 |  |  | DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 9-45 | 16.7 | 29.6 | -12.9 | -14.24 | -26.4 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 68-152 | 30.9 | 28.8 | 2.1 | -18.31 | -8.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 127-76 | 62.6 | 68.6 | -6.0 | -13.63 | -6.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 70-165 | 29.8 | 42.0 | -12.2 | -19.22 | -8.2 |  |  | !! CHECK: consensus_gap+money_moving close moneyline all sits -12.2 pts from its base (42.0%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+money_level | moneyline | 279-98 | 74.0 | 69.1 | 4.9 | -14.06 | -3.7 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+money_moving | moneyline | 129-144 | 47.3 | 47.3 | -0.1 | -25.79 | -9.4 |  |  | DROP: below break-even |
| money_delta+money_moving | moneyline | 60-174 | 25.6 | 29.5 | -3.8 | -35.87 | -15.3 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 58-173 | 25.1 | 29.5 | -4.4 | -37.06 | -16.0 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 68-172 | 28.3 | 41.0 | -12.7 | -23.82 | -9.9 |  |  | !! CHECK: consensus_gap+sharp_gap close moneyline all sits -12.7 pts from its base (41.0%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+sharp_gap | moneyline | 125-146 | 46.1 | 46.3 | -0.2 | -28.14 | -10.4 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | moneyline | 30-91 | 24.8 | 28.7 | -3.9 | -20.79 | -17.2 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 31-95 | 24.6 | 28.7 | -4.1 | -25.33 | -20.1 |  |  | DROP: below break-even |
| consensus_gap+pin_move | moneyline | 40-40 | 50.0 | 52.2 | -2.2 | +12.28 | 15.4 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 12-31 | 27.9 | 31.0 | -3.1 | +10.05 | 23.4 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 6-35 | 14.6 | 30.1 | -15.5 | -8.64 | -21.1 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 102-92 | 52.6 | 49.8 | 2.8 | -0.32 | -0.2 |  |  | no edge shown yet |
| follow_move+pin_rlm | moneyline | 30-51 | 37.0 | 30.1 | 6.9 | -1.56 | -1.9 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 47-110 | 29.9 | 30.5 | -0.6 | -20.43 | -13.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 56-72 | 43.8 | 42.1 | 1.7 | +10.9 | 8.5 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 44-84 | 34.4 | 29.7 | 4.7 | +18.87 | 14.7 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 46-104 | 30.7 | 30.6 | 0.1 | -15.83 | -10.6 |  |  | DROP: below break-even |
| pin_move+pin_rlm | moneyline | 33-55 | 37.5 | 29.5 | 8.0 | +15.15 | 17.2 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 31-50 | 38.3 | 29.6 | 8.7 | +3.13 | 3.9 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 26-39 | 40.0 | 30.7 | 9.3 | +5.92 | 9.1 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 56-74 | 43.1 | 41.5 | 1.6 | +8.73 | 6.7 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 17-43 | 28.3 | 29.4 | -1.1 | -10.7 | -17.8 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 30-51 | 37.0 | 30.1 | 6.9 | -1.56 | -1.9 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 45-87 | 34.1 | 29.6 | 4.5 | +17.27 | 13.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 28-90 | 23.7 | 28.7 | -5.0 | -24.17 | -20.5 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 47-110 | 29.9 | 30.5 | -0.6 | -20.43 | -13.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 14-83 | 14.4 | 29.8 | -15.4 | -24.27 | -25.0 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 16-47 | 25.4 | 31.5 | -6.1 | +5.85 | 9.3 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 20-41 | 32.8 | 30.9 | 1.9 | -0.92 | -1.5 |  |  | DROP: below break-even |
| money_delta+pin_rlm | moneyline | 26-52 | 33.3 | 29.7 | 3.7 | +3.87 | 5.0 |  |  | DROP: below break-even |
| money_delta+pin_value | moneyline | 3-18 | 14.3 | 28.0 | -13.7 | -6.68 | -31.8 |  |  | keep collecting (21/30) |
| money_moving+pin_value | moneyline | 11-33 | 25.0 | 31.0 | -6.0 | +12.94 | 29.4 |  |  | DROP: below break-even |
| pin_move+pin_value | moneyline | 7-11 | 38.9 | 35.3 | 3.6 | +6.35 | 35.3 |  |  | keep collecting (18/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 28.0 | 3.3 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 11-35 | 23.9 | 30.8 | -6.9 | +10.94 | 23.8 |  |  | DROP: below break-even |
| follow_move+money_delta | moneyline | 31-65 | 32.3 | 32.6 | -0.3 | -20.01 | -20.8 |  |  | DROP: below break-even |
| money_delta+money_level | moneyline | 19-24 | 44.2 | 34.1 | 10.1 | +10.72 | 24.9 |  |  | no edge shown yet |
| money_delta+rlm_ratio | moneyline | 26-55 | 32.1 | 31.2 | 0.9 | -14.5 | -17.9 |  |  | DROP: below break-even |
| money_level+pin_move | moneyline | 81-48 | 62.8 | 66.2 | -3.4 | -4.2 | -3.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 13-10 | 56.5 | 33.7 | 22.8 | +6.93 | 30.1 |  |  | keep collecting (23/30) |
| money_level+rlm_ratio | moneyline | 16-14 | 53.3 | 38.2 | 15.1 | +6.18 | 20.6 |  |  | no edge shown yet |
| money_delta+rlm_quiet | moneyline | 18-50 | 26.5 | 29.9 | -3.4 | -21.61 | -31.8 |  |  | DROP: below break-even |
| money_level+pin_value | moneyline | 5-3 | 62.5 | 66.5 | -4.0 | -0.32 | -4.0 |  |  | keep collecting (8/30) |
| follow_move+pin_value | moneyline | 3-9 | 25.0 | 35.3 | -10.3 | +3.8 | 31.7 |  |  | keep collecting (12/30) |
| pin_value+rlm_quiet | moneyline | 2-7 | 22.2 | 28.0 | -5.7 | +5.12 | 56.9 |  |  | keep collecting (9/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 28.0 | -3.0 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 37-29 | 56.1 | 48.3 | 7.8 | +2.57 | 3.9 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 51-47 | 52.0 | 48.7 | 3.4 | -3.5 | -3.6 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 29-30 | 49.2 | 49.1 | 0.0 | -5.23 | -8.9 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | -0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 71-53 | 57.3 | 48.8 | 8.4 | +7.45 | 6.0 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 5-4 | 55.6 | 50.3 | 5.2 | +0.18 | 2.0 |  |  | keep collecting (9/30) |
| consensus_gap+sharp_gap | spread | 50-47 | 51.5 | 48.9 | 2.7 | -4.4 | -4.5 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 168-172 | 49.4 | 49.1 | 0.3 | -20.02 | -5.9 |  |  | no edge shown yet |
| follow_move+pin_move | spread | 143-163 | 46.7 | 50.0 | -3.3 | -32.71 | -10.7 |  |  | DROP: below break-even |
| follow_move+pin_rlm | spread | 19-19 | 50.0 | 51.0 | -1.0 | -1.65 | -4.3 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 66-58 | 53.2 | 49.0 | 4.2 | -0.38 | -0.3 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 42-45 | 48.3 | 50.2 | -2.0 | -6.92 | -7.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 169-171 | 49.7 | 49.2 | 0.5 | -17.88 | -5.3 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 127-136 | 48.3 | 49.8 | -1.5 | -21.11 | -8.0 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 24-23 | 51.1 | 51.3 | -0.2 | -1.13 | -2.4 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 90-92 | 49.5 | 49.1 | 0.4 | -14.27 | -7.8 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 40-44 | 47.6 | 50.1 | -2.5 | -7.85 | -9.3 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 353-347 | 50.4 | 49.4 | 1.0 | -28.44 | -4.1 |  |  | no edge shown yet |
| pin_move+pin_rlm | spread | 26-23 | 53.1 | 51.3 | 1.7 | +0.7 | 1.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 89-89 | 50.0 | 49.8 | 0.2 | -10.68 | -6.0 |  |  | no edge shown yet |
| pin_move+rlm_ratio | spread | 23-26 | 46.9 | 50.8 | -3.9 | -5.1 | -10.4 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 130-136 | 48.9 | 49.8 | -1.0 | -18.38 | -6.9 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 8-10 | 44.4 | 51.0 | -6.6 | -2.97 | -16.5 |  |  | keep collecting (18/30) |
| pin_rlm+rlm_ratio | spread | 19-19 | 50.0 | 51.0 | -1.0 | -1.65 | -4.3 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 26-23 | 53.1 | 51.3 | 1.7 | +0.7 | 1.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 8-8 | 50.0 | 49.6 | 0.4 | -1.17 | -7.3 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | spread | 90-92 | 49.5 | 49.2 | 0.3 | -14.33 | -7.9 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 42-45 | 48.3 | 50.2 | -2.0 | -6.92 | -7.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 164-173 | 48.7 | 48.8 | -0.2 | -24.64 | -7.3 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 22-28 | 44.0 | 49.9 | -5.9 | -8.28 | -16.6 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 276-272 | 50.4 | 49.0 | 1.3 | -23.28 | -4.2 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 61-53 | 53.5 | 48.4 | 5.1 | -0.85 | -0.7 |  |  | no edge shown yet |
| money_level+money_moving | spread | 275-273 | 50.2 | 49.0 | 1.2 | -25.2 | -4.6 |  |  | no edge shown yet |
| money_level+pin_move | spread | 116-135 | 46.2 | 49.5 | -3.3 | -30.45 | -12.1 |  |  | DROP: below break-even |
| money_level+pin_value | spread | 96-96 | 50.0 | 48.7 | 1.3 | -13.19 | -6.9 |  |  | no edge shown yet |
| consensus_gap+money_delta | spread | 16-14 | 53.3 | 50.8 | 2.5 | -0.33 | -1.1 |  |  | no edge shown yet |
| follow_move+money_delta | spread | 42-50 | 45.7 | 50.5 | -4.8 | -11.97 | -13.0 |  |  | no edge shown yet |
| money_delta+money_level | spread | 43-41 | 51.2 | 50.0 | 1.2 | -2.26 | -2.7 |  |  | no edge shown yet |
| money_delta+money_moving | spread | 73-78 | 48.3 | 50.6 | -2.2 | -12.12 | -8.0 |  |  | no edge shown yet |
| money_delta+pin_value | spread | 34-28 | 54.8 | 50.8 | 4.0 | +1.63 | 2.6 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 72-76 | 48.6 | 50.5 | -1.9 | -11.1 | -7.5 |  |  | no edge shown yet |
| follow_move+rlm_quiet | spread | 54-56 | 49.1 | 51.2 | -2.1 | -5.82 | -5.3 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 14-5 | 73.7 | 51.1 | 22.5 | +7.78 | 40.9 |  |  | keep collecting (19/30) |
| rlm_quiet+sharp_gap | spread | 22-13 | 62.9 | 51.3 | 11.5 | +7.13 | 20.4 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 14-11 | 56.0 | 50.6 | 5.4 | +1.57 | 6.3 |  |  | keep collecting (25/30) |
| money_delta+pin_move | spread | 39-46 | 45.9 | 51.4 | -5.5 | -10.42 | -12.3 |  |  | no edge shown yet |
| money_delta+rlm_ratio | spread | 17-27 | 38.6 | 50.0 | -11.4 | -11.93 | -27.1 |  |  | DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 53.1 | 46.9 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_rlm | spread | 13-16 | 44.8 | 51.0 | -6.1 | -4.31 | -14.8 |  |  | keep collecting (29/30) |
| money_delta+rlm_quiet | spread | 17-19 | 47.2 | 51.7 | -4.5 | -3.27 | -9.1 |  |  | no edge shown yet |
| money_moving+rlm_quiet | spread | 21-13 | 61.8 | 51.3 | 10.5 | +6.18 | 18.2 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 31-30 | 50.8 | 51.7 | -0.9 | -1.18 | -1.9 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-2 | 75.0 | 52.3 | 22.7 | +3.56 | 44.5 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_quiet | spread | 4-3 | 57.1 | 51.3 | 5.8 | +0.48 | 6.9 |  |  | keep collecting (7/30) |
| pin_value+rlm_quiet | spread | 6-7 | 46.2 | 50.2 | -4.1 | -1.7 | -13.1 |  |  | keep collecting (13/30) |
| follow_move+money_delta | total | 108-104 | 50.9 | 49.5 | 1.4 | -5.11 | -2.4 |  |  | no edge shown yet |
| money_level+money_moving | total | 247-242 | 50.5 | 50.1 | 0.4 | -17.33 | -3.5 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 245-235 | 51.0 | 50.1 | 1.0 | -12.01 | -2.5 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 367-393 | 48.3 | 49.8 | -1.6 | -58.12 | -7.6 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 67-63 | 51.5 | 50.7 | 0.9 | -3.56 | -2.7 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 32-25 | 56.1 | 50.4 | 5.7 | +3.39 | 5.9 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 74-64 | 53.6 | 50.4 | 3.2 | +1.65 | 1.2 |  |  | no edge shown yet |
| follow_move+money_moving | total | 230-260 | 46.9 | 49.9 | -2.9 | -50.25 | -10.3 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 239-259 | 48.0 | 49.8 | -1.9 | -40.99 | -8.2 |  |  | DROP: below break-even |
| money_level+pin_move | total | 139-124 | 52.9 | 50.1 | 2.8 | +2.41 | 0.9 |  |  | no edge shown yet |
| money_level+pin_value | total | 105-83 | 55.9 | 50.4 | 5.4 | +10.85 | 5.8 |  |  | no edge shown yet |
| pin_move+pin_value | total | 91-82 | 52.6 | 50.0 | 2.6 | -0.02 | -0.0 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 107-141 | 43.1 | 49.5 | -6.4 | -42.66 | -17.2 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 156-168 | 48.1 | 49.8 | -1.6 | -25.59 | -7.9 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | total | 64-89 | 41.8 | 49.4 | -7.6 | -30.28 | -19.8 |  |  | DROP: below break-even |
| money_delta+money_moving | total | 134-123 | 52.1 | 49.5 | 2.6 | -0.31 | -0.1 |  |  | no edge shown yet |
| follow_move+money_level | total | 195-190 | 50.6 | 50.2 | 0.5 | -12.75 | -3.3 |  |  | no edge shown yet |
| follow_move+pin_value | total | 81-75 | 51.9 | 50.1 | 1.8 | -2.12 | -1.4 |  |  | no edge shown yet |
| money_moving+pin_value | total | 83-86 | 49.1 | 50.1 | -0.9 | -11.32 | -6.7 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 84-84 | 50.0 | 50.0 | -0.0 | -8.37 | -5.0 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 54-55 | 49.5 | 50.4 | -0.9 | -7.08 | -6.5 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 56-53 | 51.4 | 50.4 | 1.0 | -3.29 | -3.0 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 48-39 | 55.2 | 50.5 | 4.7 | +3.53 | 4.1 |  |  | no edge shown yet |
| consensus_gap+money_delta | total | 19-14 | 57.6 | 50.0 | 7.5 | +2.74 | 8.3 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | total | 12-10 | 54.5 | 49.8 | 4.7 | +0.72 | 3.3 |  |  | keep collecting (22/30) |
| money_delta+rlm_quiet | total | 31-51 | 37.8 | 49.3 | -11.5 | -22.55 | -27.5 |  |  | DROP: below break-even |
| money_delta+sharp_gap | total | 134-120 | 52.8 | 49.5 | 3.3 | +2.69 | 1.1 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 58-86 | 40.3 | 49.4 | -9.1 | -32.77 | -22.8 |  |  | DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 69-52 | 57.0 | 49.6 | 7.4 | +11.01 | 9.1 |  |  | no edge shown yet |
| money_delta+pin_move | total | 75-72 | 51.0 | 49.4 | 1.6 | -3.24 | -2.2 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 158-169 | 48.3 | 49.7 | -1.4 | -24.68 | -7.5 |  |  | no edge shown yet |
| follow_move+pin_move | total | 175-194 | 47.4 | 49.8 | -2.4 | -34.14 | -9.3 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | total | 24-31 | 43.6 | 49.5 | -5.9 | -8.99 | -16.4 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | total | 10-10 | 50.0 | 50.1 | -0.1 | -1.13 | -5.6 |  |  | keep collecting (20/30) |
| consensus_gap+rlm_ratio | total | 19-10 | 65.5 | 50.2 | 15.3 | +6.85 | 23.6 |  |  | keep collecting (29/30) |
| follow_move+pin_rlm | total | 74-68 | 52.1 | 49.4 | 2.7 | +0.07 | 0.0 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 141-125 | 53.0 | 49.5 | 3.5 | +4.17 | 1.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 43-27 | 61.4 | 49.4 | 12.0 | +12.5 | 17.9 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 70-49 | 58.8 | 49.6 | 9.2 | +14.97 | 12.6 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 83-75 | 52.5 | 49.4 | 3.1 | +1.1 | 0.7 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 136-122 | 52.7 | 49.5 | 3.2 | +2.58 | 1.0 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 86-78 | 52.4 | 49.4 | 3.0 | +0.84 | 0.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 82-70 | 53.9 | 49.5 | 4.5 | +5.23 | 3.4 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 30-23 | 56.6 | 49.6 | 7.0 | +4.17 | 7.9 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 74-68 | 52.1 | 49.4 | 2.7 | +0.07 | 0.0 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 86-78 | 52.4 | 49.4 | 3.0 | +0.84 | 0.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 34-23 | 59.6 | 49.7 | 10.0 | +7.78 | 13.7 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 141-125 | 53.0 | 49.5 | 3.5 | +4.17 | 1.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 53-42 | 55.8 | 49.3 | 6.5 | +6.73 | 7.1 |  |  | no edge shown yet |
| money_delta+rlm_ratio | total | 88-64 | 57.9 | 49.5 | 8.4 | +16.51 | 10.9 |  |  | no edge shown yet |
| money_delta+pin_value | total | 43-30 | 58.9 | 49.6 | 9.3 | +8.92 | 12.2 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 50-73 | 40.7 | 49.5 | -8.9 | -27.01 | -22.0 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | total | 26-38 | 40.6 | 49.4 | -8.7 | -14.14 | -22.1 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | total | 51-68 | 42.9 | 49.3 | -6.5 | -21.14 | -17.8 |  |  | DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 49.1 | 50.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| rlm_quiet | close | 1-3k bets | 154-229 | 40.2 | -1.6 | -8.4 |  |
| rlm_quiet | close | 3k+ bets | 49-75 | 39.5 | -3.0 | -14.8 |  |
| rlm_quiet | close | <1k bets | 26-45 | 36.6 | -4.7 | -23.0 |  |
| rlm_quiet | close | pin $1-2k | 62-112 | 35.6 | -7.9 | -20.9 |  |
| rlm_quiet | close | pin $2k+ | 68-86 | 44.2 | 5.9 | 1.8 |  |
| rlm_quiet | close | pin limit <$1k | 41-44 | 48.2 | -0.8 | -7.5 |  |
| pin_move | close | 1-3k bets | 377-376 | 50.1 | 0.4 | -2.4 |  |
| pin_move | close | 3k+ bets | 134-150 | 47.2 | -2.3 | -9.0 |  |
| pin_move | close | <1k bets | 77-79 | 49.4 | -1.2 | -5.4 |  |
| pin_move | close | pin $1-2k | 272-276 | 49.6 | -0.5 | -2.7 |  |
| pin_move | close | pin $2k+ | 214-227 | 48.5 | -0.9 | -7.5 |  |
| pin_move | close | pin limit <$1k | 102-102 | 50.0 | 0.5 | -2.2 |  |
| money_delta | close | 1-3k bets | 233-294 | 44.2 | -0.5 | -7.2 |  |
| money_delta | close | 3k+ bets | 88-118 | 42.7 | -0.7 | -3.0 |  |
| money_delta | close | <1k bets | 48-72 | 40.0 | -2.6 | -16.1 |  |
| money_delta | close | pin $1-2k | 132-129 | 50.6 | 4.5 | 6.0 |  |
| money_delta | close | pin $2k+ | 92-129 | 41.6 | 0.5 | -11.6 |  |
| money_delta | close | pin limit <$1k | 58-65 | 47.2 | -1.9 | -6.0 |  |
| pin_rlm | close | 1-3k bets | 101-114 | 47.0 | 4.7 | 12.1 |  |
| pin_rlm | close | 3k+ bets | 34-50 | 40.5 | -1.7 | -11.6 |  |
| pin_rlm | close | <1k bets | 22-24 | 47.8 | 6.5 | 5.5 |  |
| pin_rlm | close | pin $1-2k | 70-75 | 48.3 | 4.2 | 9.1 |  |
| pin_rlm | close | pin $2k+ | 43-76 | 36.1 | 0.6 | -5.6 |  |
| pin_rlm | close | pin limit <$1k | 44-37 | 54.3 | 5.9 | 15.2 |  |
| follow_move | close | 1-3k bets | 653-606 | 51.9 | 0.9 | -5.2 |  |
| follow_move | close | 3k+ bets | 211-204 | 50.8 | -0.8 | -7.2 |  |
| follow_move | close | <1k bets | 143-139 | 50.7 | -1.6 | -13.8 |  |
| follow_move | close | pin $1-2k | 309-345 | 47.2 | -3.4 | -11.5 |  |
| follow_move | close | pin $2k+ | 267-230 | 53.7 | 2.3 | -2.0 |  |
| follow_move | close | pin limit <$1k | 120-127 | 48.6 | -1.2 | -7.2 |  |
| rlm_ratio | close | 1-3k bets | 148-196 | 43.0 | -0.7 | -8.2 |  |
| rlm_ratio | close | 3k+ bets | 53-51 | 51.0 | 6.6 | 8.6 |  |
| rlm_ratio | close | <1k bets | 29-33 | 46.8 | 3.9 | -6.3 |  |
| rlm_ratio | close | pin $1-2k | 84-85 | 49.7 | 3.9 | 3.0 |  |
| rlm_ratio | close | pin $2k+ | 43-65 | 39.8 | 2.1 | -11.2 |  |
| rlm_ratio | close | pin limit <$1k | 49-44 | 52.7 | 3.9 | 1.7 |  |
| money_level | close | 1-3k bets | 824-595 | 58.1 | 2.6 | -2.2 |  |
| money_level | close | 3k+ bets | 278-220 | 55.8 | 0.7 | -3.3 |  |
| money_level | close | <1k bets | 183-129 | 58.7 | 3.0 | -4.5 |  |
| money_level | close | pin $1-2k | 379-321 | 54.1 | 0.3 | -3.6 |  |
| money_level | close | pin $2k+ | 334-260 | 56.2 | -1.1 | -7.1 |  |
| money_level | close | pin limit <$1k | 147-138 | 51.6 | 1.2 | -2.0 |  |
| sharp_gap | close | 1-3k bets | 618-736 | 45.6 | -1.7 | -9.0 |  |
| sharp_gap | close | 3k+ bets | 236-251 | 48.5 | 0.8 | 1.1 |  |
| sharp_gap | close | <1k bets | 139-157 | 47.0 | -0.8 | -11.1 |  |
| sharp_gap | close | pin $1-2k | 326-348 | 48.4 | -0.3 | -3.9 |  |
| sharp_gap | close | pin $2k+ | 265-306 | 46.4 | -0.0 | -3.8 |  |
| sharp_gap | close | pin limit <$1k | 128-145 | 46.9 | -2.4 | -6.8 |  |
| money_moving | close | 1-3k bets | 627-733 | 46.1 | -1.7 | -9.0 |  |
| money_moving | close | 3k+ bets | 235-253 | 48.2 | 0.3 | -0.3 |  |
| money_moving | close | <1k bets | 138-156 | 46.9 | -0.8 | -9.9 |  |
| money_moving | close | pin $1-2k | 323-352 | 47.9 | -1.1 | -4.9 |  |
| money_moving | close | pin $2k+ | 266-304 | 46.7 | 0.2 | -3.8 |  |
| money_moving | close | pin limit <$1k | 126-152 | 45.3 | -4.0 | -9.9 |  |
| pin_value | close | 1-3k bets | 278-272 | 50.5 | 2.3 | 4.1 |  |
| pin_value | close | 3k+ bets | 90-99 | 47.6 | -1.1 | -7.0 |  |
| pin_value | close | <1k bets | 65-51 | 56.0 | 8.5 | 14.5 |  |
| pin_value | close | pin $1-2k | 200-215 | 48.2 | -0.3 | -2.2 |  |
| pin_value | close | pin $2k+ | 120-135 | 47.1 | 0.6 | 0.7 |  |
| pin_value | close | pin limit <$1k | 113-72 | 61.1 | 11.0 | 18.2 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 46.9 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 46.9 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 258-311 | 45.3 | -3.7 | -9.7 |  |
| consensus_gap | close | 3k+ bets | 92-105 | 46.7 | -1.5 | 3.3 |  |
| consensus_gap | close | <1k bets | 55-81 | 40.4 | -5.1 | -19.2 |  |
| consensus_gap | close | pin $1-2k | 125-134 | 48.3 | -1.5 | 0.3 |  |
| consensus_gap | close | pin $2k+ | 118-120 | 49.6 | -1.2 | -0.0 |  |
| consensus_gap | close | pin limit <$1k | 57-45 | 55.9 | 5.5 | 8.8 |  |
| consensus_gap+follow_move | close | 1-3k bets | 102-96 | 51.5 | -0.1 | -2.9 |  |
| consensus_gap+money_level | close | 1-3k bets | 173-115 | 60.1 | 1.2 | 2.0 |  |
| consensus_gap+money_moving | close | 1-3k bets | 112-168 | 40.0 | -6.0 | -9.8 |  |
| consensus_gap+pin_move | close | 1-3k bets | 65-59 | 52.4 | 1.3 | 7.9 |  |
| consensus_gap+pin_value | close | 1-3k bets | 103-113 | 47.7 | 1.1 | -0.4 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 109-171 | 38.9 | -6.3 | -10.8 |  |
| follow_move+money_level | close | 1-3k bets | 420-298 | 58.5 | 2.6 | -3.4 |  |
| follow_move+money_moving | close | 1-3k bets | 351-382 | 47.9 | -1.0 | -8.5 |  |
| follow_move+pin_move | close | 1-3k bets | 270-286 | 48.6 | -1.1 | -7.3 |  |
| follow_move+pin_value | close | 1-3k bets | 93-89 | 51.1 | 2.4 | 2.1 |  |
| follow_move+sharp_gap | close | 1-3k bets | 354-383 | 48.0 | -0.5 | -7.4 |  |
| money_level+money_moving | close | 1-3k bets | 447-394 | 53.2 | 0.8 | -3.6 |  |
| money_level+pin_move | close | 1-3k bets | 223-199 | 52.8 | 0.1 | -3.7 |  |
| money_level+pin_value | close | 1-3k bets | 132-114 | 53.7 | 4.0 | 0.7 |  |
| money_level+sharp_gap | close | 1-3k bets | 432-387 | 52.7 | 0.8 | -3.4 |  |
| money_moving+pin_move | close | 1-3k bets | 223-237 | 48.5 | -0.2 | -2.7 |  |
| money_moving+pin_value | close | 1-3k bets | 118-138 | 46.1 | -1.5 | -5.6 |  |
| money_moving+sharp_gap | close | 1-3k bets | 594-703 | 45.8 | -1.7 | -8.5 |  |
| pin_move+pin_value | close | 1-3k bets | 120-112 | 51.7 | 2.4 | 1.1 |  |
| pin_move+sharp_gap | close | 1-3k bets | 228-239 | 48.8 | 0.4 | -1.7 |  |
| pin_value+sharp_gap | close | 1-3k bets | 119-140 | 45.9 | -1.5 | -5.9 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 154-229 | 40.2 | -1.6 | -8.4 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 76-138 | 35.5 | -5.4 | -17.1 |  |
| consensus_gap+money_delta | close | 1-3k bets | 29-66 | 30.5 | -7.8 | -20.1 |  |
| follow_move+money_delta | close | 1-3k bets | 116-140 | 45.3 | -1.0 | -10.2 |  |
| money_delta+money_level | close | 1-3k bets | 83-77 | 51.9 | 3.7 | 6.7 |  |
| money_delta+money_moving | close | 1-3k bets | 165-231 | 41.7 | -1.3 | -9.4 |  |
| money_delta+pin_value | close | 1-3k bets | 52-48 | 52.0 | 4.3 | 3.4 |  |
| money_delta+sharp_gap | close | 1-3k bets | 164-228 | 41.8 | -1.1 | -9.0 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 83-94 | 46.9 | 0.1 | -0.8 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 19-29 | 39.6 | 0.7 | 18.1 |  |
| money_level+pin_rlm | close | 1-3k bets | 45-32 | 58.4 | 10.5 | 12.9 |  |
| pin_move+pin_rlm | close | 1-3k bets | 93-93 | 50.0 | 6.0 | 10.5 |  |
| pin_rlm+pin_value | close | 1-3k bets | 31-26 | 54.4 | 8.0 | 28.2 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 101-114 | 47.0 | 4.7 | 12.1 |  |
| money_delta+pin_rlm | close | 1-3k bets | 57-65 | 46.7 | 4.2 | 9.5 |  |
| money_moving+pin_rlm | close | 1-3k bets | 96-109 | 46.8 | 4.5 | 12.7 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 23-34 | 40.4 | 0.3 | 5.5 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 148-196 | 43.0 | -0.7 | -8.2 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 81-99 | 45.0 | 0.3 | -9.5 |  |
| money_level+rlm_ratio | close | 1-3k bets | 69-64 | 51.9 | 3.1 | 0.2 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 142-188 | 43.0 | -0.9 | -8.0 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 80-82 | 49.4 | 4.4 | 2.0 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 29-23 | 55.8 | 7.8 | 6.8 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 148-196 | 43.0 | -0.7 | -8.2 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 16-38 | 29.6 | -6.2 | -10.8 |  |
| follow_move+pin_rlm | close | 1-3k bets | 74-89 | 45.4 | 1.9 | -5.6 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 69-133 | 34.2 | -6.8 | -19.4 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 71-97 | 42.3 | -1.6 | -9.8 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 30-56 | 34.9 | -4.6 | -20.0 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 74-89 | 45.4 | 1.9 | -5.6 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 60-118 | 33.7 | -5.9 | -18.2 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 43-77 | 35.8 | -7.3 | -25.4 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 19-26 | 42.2 | -3.6 | 3.4 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 50.9 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 36-31 | 53.7 | 3.1 | 2.2 |  |
| consensus_gap+money_moving | close | 3k+ bets | 38-59 | 39.2 | -6.2 | 9.4 |  |
| consensus_gap+pin_move | close | 3k+ bets | 28-23 | 54.9 | 5.0 | 8.5 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-8 | 27.3 | -13.2 | -13.2 |  |
| consensus_gap+pin_value | close | 3k+ bets | 40-36 | 52.6 | 6.0 | 7.1 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-8 | 33.3 | -8.0 | -4.3 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 39-59 | 39.8 | -5.5 | 12.2 |  |
| follow_move+money_moving | close | 3k+ bets | 112-121 | 48.1 | -1.1 | -6.0 |  |
| follow_move+pin_move | close | 3k+ bets | 102-111 | 47.9 | -2.0 | -7.3 |  |
| follow_move+pin_rlm | close | 3k+ bets | 32-35 | 47.8 | 3.7 | 5.2 |  |
| follow_move+pin_value | close | 3k+ bets | 36-39 | 48.0 | -1.9 | -9.8 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 53-51 | 51.0 | 6.6 | 8.6 |  |
| follow_move+sharp_gap | close | 3k+ bets | 114-120 | 48.7 | -0.1 | -4.1 |  |
| money_moving+pin_move | close | 3k+ bets | 77-95 | 44.8 | -3.4 | -11.4 |  |
| money_moving+pin_rlm | close | 3k+ bets | 33-49 | 40.2 | -1.7 | -11.9 |  |
| money_moving+pin_value | close | 3k+ bets | 45-56 | 44.6 | -3.4 | -9.5 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 51-49 | 51.0 | 6.7 | 9.0 |  |
| money_moving+sharp_gap | close | 3k+ bets | 228-243 | 48.4 | 0.7 | 0.8 |  |
| pin_move+pin_rlm | close | 3k+ bets | 32-44 | 42.1 | -1.6 | -8.0 |  |
| pin_move+pin_value | close | 3k+ bets | 38-49 | 43.7 | -5.6 | -17.6 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 34-37 | 47.9 | 2.5 | 3.8 |  |
| pin_move+sharp_gap | close | 3k+ bets | 77-95 | 44.8 | -3.1 | -10.8 |  |
| pin_rlm+pin_value | close | 3k+ bets | 6-15 | 28.6 | -17.8 | -45.5 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 32-35 | 47.8 | 3.7 | 5.2 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 34-50 | 40.5 | -1.7 | -11.6 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 9-10 | 47.4 | -2.8 | -10.1 |  |
| pin_value+sharp_gap | close | 3k+ bets | 45-55 | 45.0 | -3.0 | -8.5 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 53-51 | 51.0 | 6.6 | 8.6 |  |
| follow_move+money_delta | close | 3k+ bets | 42-52 | 44.7 | -0.6 | -7.8 |  |
| money_level+money_moving | close | 3k+ bets | 160-140 | 53.3 | 1.1 | -1.2 |  |
| money_level+sharp_gap | close | 3k+ bets | 159-137 | 53.7 | 1.6 | 0.1 |  |
| follow_move+money_level | close | 3k+ bets | 131-100 | 56.7 | 0.3 | -4.3 |  |
| money_level+rlm_ratio | close | 3k+ bets | 25-13 | 65.8 | 18.4 | 34.7 |  |
| consensus_gap+money_level | close | 3k+ bets | 53-49 | 52.0 | -5.1 | -11.0 |  |
| money_level+pin_move | close | 3k+ bets | 73-70 | 51.0 | -2.5 | -6.6 |  |
| money_level+pin_value | close | 3k+ bets | 51-50 | 50.5 | -0.1 | -6.3 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 8-15 | 34.8 | -3.9 | -13.6 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 49-75 | 39.5 | -3.0 | -14.8 |  |
| money_delta+money_moving | close | 3k+ bets | 68-90 | 43.0 | 0.7 | 1.9 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 21-30 | 41.2 | -0.1 | -6.2 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 26-40 | 39.4 | -3.0 | -12.9 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 24-39 | 38.1 | -4.2 | -14.9 |  |
| consensus_gap+money_delta | close | 3k+ bets | 13-23 | 36.1 | -3.4 | 20.4 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 12-29 | 29.3 | -13.7 | -36.6 |  |
| money_delta+sharp_gap | close | 3k+ bets | 66-87 | 43.1 | 1.0 | 2.6 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 29-42 | 40.8 | -2.8 | -11.8 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 11-21 | 34.4 | -7.5 | -18.3 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 8-15 | 34.8 | -14.1 | -33.5 |  |
| money_delta+money_level | close | 3k+ bets | 34-22 | 60.7 | 14.4 | 22.5 |  |
| money_level+pin_rlm | close | 3k+ bets | 16-9 | 64.0 | 18.9 | 37.0 |  |
| money_delta+pin_value | close | 3k+ bets | 19-20 | 48.7 | 2.2 | -8.1 |  |
| money_delta+pin_move | close | 3k+ bets | 37-46 | 44.6 | -0.9 | -9.1 |  |
| money_delta+pin_rlm | close | 3k+ bets | 22-29 | 43.1 | 1.1 | -8.2 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 31-27 | 53.4 | 9.2 | 13.0 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 46.9 | 87.7 |  |
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
| money_moving+pin_move | close | <1k bets | 39-44 | 47.0 | -0.6 | -4.3 |  |
| money_moving+pin_value | close | <1k bets | 21-17 | 55.3 | 10.2 | 29.4 |  |
| pin_move+pin_value | close | <1k bets | 29-21 | 58.0 | 9.5 | 16.9 |  |
| pin_move+sharp_gap | close | <1k bets | 39-45 | 46.4 | -1.8 | -9.2 |  |
| pin_value+sharp_gap | close | <1k bets | 21-16 | 56.8 | 11.2 | 32.9 |  |
| follow_move+money_delta | close | <1k bets | 23-27 | 46.0 | 2.7 | -7.4 |  |
| follow_move+money_moving | close | <1k bets | 64-73 | 46.7 | -2.8 | -14.4 |  |
| follow_move+pin_move | close | <1k bets | 48-52 | 48.0 | -3.1 | -10.9 |  |
| follow_move+sharp_gap | close | <1k bets | 65-73 | 47.1 | -2.8 | -16.4 |  |
| money_delta+money_moving | close | <1k bets | 34-54 | 38.6 | -1.8 | -15.9 |  |
| money_delta+pin_move | close | <1k bets | 14-19 | 42.4 | -1.8 | -17.4 |  |
| money_delta+sharp_gap | close | <1k bets | 34-54 | 38.6 | -1.8 | -15.9 |  |
| follow_move+rlm_quiet | close | <1k bets | 26-45 | 36.6 | -4.7 | -23.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 29-33 | 46.8 | 3.9 | -6.3 |  |
| money_delta+rlm_quiet | close | <1k bets | 11-14 | 44.0 | 3.9 | -7.9 |  |
| money_delta+rlm_ratio | close | <1k bets | 19-20 | 48.7 | 6.7 | -0.8 |  |
| money_moving+rlm_quiet | close | <1k bets | 16-18 | 47.1 | 6.0 | 3.1 |  |
| money_moving+rlm_ratio | close | <1k bets | 29-33 | 46.8 | 3.9 | -6.3 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 12-15 | 44.4 | 4.6 | -7.6 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 15-19 | 44.1 | 2.5 | -9.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 29-33 | 46.8 | 3.9 | -6.3 |  |
| follow_move+money_level | close | <1k bets | 87-63 | 58.0 | 0.1 | -11.2 |  |
| consensus_gap+money_delta | close | <1k bets | 7-22 | 24.1 | -10.4 | -35.0 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -2.4 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 13-16 | 44.8 | 5.3 | -3.9 |  |
| money_moving+pin_rlm | close | <1k bets | 22-24 | 47.8 | 6.5 | 5.5 |  |
| pin_rlm+sharp_gap | close | <1k bets | 22-24 | 47.8 | 6.5 | 5.5 |  |
| money_delta+pin_value | close | <1k bets | 9-8 | 52.9 | 7.5 | 21.5 |  |
| consensus_gap+follow_move | close | <1k bets | 14-20 | 41.2 | -10.6 | -33.3 |  |
| follow_move+pin_rlm | close | <1k bets | 17-14 | 54.8 | 11.2 | 8.4 |  |
| follow_move+pin_value | close | <1k bets | 21-14 | 60.0 | 11.2 | 14.0 |  |
| pin_move+pin_rlm | close | <1k bets | 20-19 | 51.3 | 7.6 | 8.1 |  |
| pin_move+rlm_quiet | close | <1k bets | 12-14 | 46.2 | 0.8 | -1.0 |  |
| pin_move+rlm_ratio | close | <1k bets | 17-16 | 51.5 | 6.3 | 0.5 |  |
| pin_rlm+pin_value | close | <1k bets | 6-3 | 66.7 | 24.8 | 64.1 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 8-6 | 57.1 | 13.9 | 12.9 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 17-14 | 54.8 | 11.2 | 8.4 |  |
| pin_value+rlm_quiet | close | <1k bets | 5-4 | 55.6 | 6.5 | 6.5 |  |
| pin_value+rlm_ratio | close | <1k bets | 5-1 | 83.3 | 34.9 | 58.3 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -6.4 | -42.5 |  |
| money_delta+money_level | close | <1k bets | 14-18 | 43.8 | 0.7 | -12.1 |  |
| money_level+rlm_ratio | close | <1k bets | 14-14 | 50.0 | 4.8 | -2.1 |  |
| money_level+pin_rlm | close | <1k bets | 9-7 | 56.2 | 13.6 | 11.6 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-5 | 16.7 | -21.5 | -68.2 |  |
| consensus_gap+follow_move | close | pin $1-2k | 48-54 | 47.1 | -5.1 | -10.7 |  |
| consensus_gap+money_moving | close | pin $1-2k | 59-72 | 45.0 | -3.6 | -3.4 |  |
| consensus_gap+pin_move | close | pin $1-2k | 47-49 | 49.0 | -2.9 | 4.5 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-19 | 40.6 | -1.0 | 21.9 |  |
| consensus_gap+pin_value | close | pin $1-2k | 72-77 | 48.3 | 1.8 | -1.3 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-16 | 46.7 | 1.2 | 1.7 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 57-69 | 45.2 | -2.6 | -1.5 |  |
| follow_move+money_moving | close | pin $1-2k | 179-212 | 45.8 | -3.7 | -10.8 |  |
| follow_move+pin_move | close | pin $1-2k | 189-216 | 46.7 | -3.5 | -10.2 |  |
| follow_move+pin_rlm | close | pin $1-2k | 57-59 | 49.1 | 3.5 | 2.5 |  |
| follow_move+pin_value | close | pin $1-2k | 68-79 | 46.3 | -3.2 | -12.7 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 84-85 | 49.7 | 3.9 | 3.0 |  |
| follow_move+sharp_gap | close | pin $1-2k | 184-211 | 46.6 | -2.8 | -9.7 |  |
| money_moving+pin_move | close | pin $1-2k | 164-181 | 47.5 | -1.6 | -4.1 |  |
| money_moving+pin_rlm | close | pin $1-2k | 67-71 | 48.6 | 4.2 | 10.1 |  |
| money_moving+pin_value | close | pin $1-2k | 78-107 | 42.2 | -5.7 | -16.0 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 82-80 | 50.6 | 4.5 | 4.7 |  |
| money_moving+sharp_gap | close | pin $1-2k | 312-337 | 48.1 | -0.6 | -4.1 |  |
| pin_move+pin_rlm | close | pin $1-2k | 67-67 | 50.0 | 4.6 | 10.6 |  |
| pin_move+pin_value | close | pin $1-2k | 84-97 | 46.4 | -3.2 | -10.7 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 65-62 | 51.2 | 4.3 | 5.2 |  |
| pin_move+sharp_gap | close | pin $1-2k | 167-182 | 47.9 | -1.1 | -3.8 |  |
| pin_rlm+pin_value | close | pin $1-2k | 18-26 | 40.9 | -7.3 | -15.9 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 57-59 | 49.1 | 3.5 | 2.5 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 70-75 | 48.3 | 4.2 | 9.1 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 20-22 | 47.6 | -1.8 | -10.1 |  |
| pin_value+sharp_gap | close | pin $1-2k | 78-104 | 42.9 | -5.0 | -14.6 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 84-85 | 49.7 | 3.9 | 3.0 |  |
| follow_move+money_level | close | pin $1-2k | 204-190 | 51.8 | -2.2 | -8.8 |  |
| money_level+rlm_ratio | close | pin $1-2k | 47-35 | 57.3 | 9.4 | 11.7 |  |
| money_level+sharp_gap | close | pin $1-2k | 234-217 | 51.9 | 0.3 | -3.9 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 4-15 | 21.1 | -20.0 | -39.5 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 62-112 | 35.6 | -7.9 | -20.9 |  |
| money_level+money_moving | close | pin $1-2k | 234-221 | 51.4 | -0.4 | -5.0 |  |
| consensus_gap+money_level | close | pin $1-2k | 74-64 | 53.6 | -3.2 | -5.8 |  |
| money_level+pin_value | close | pin $1-2k | 88-87 | 50.3 | 0.4 | -5.9 |  |
| money_level+pin_move | close | pin $1-2k | 159-150 | 51.5 | -1.1 | -5.9 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 31-49 | 38.8 | -5.1 | -9.2 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 44-67 | 39.6 | -6.0 | -12.2 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 19-35 | 35.2 | -9.1 | -17.9 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 26-42 | 38.2 | -4.9 | -10.2 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 32-52 | 38.1 | -5.5 | -13.0 |  |
| money_level+pin_rlm | close | pin $1-2k | 33-23 | 58.9 | 12.6 | 15.7 |  |
| follow_move+money_delta | close | pin $1-2k | 67-69 | 49.3 | 2.8 | 0.5 |  |
| money_delta+money_moving | close | pin $1-2k | 89-97 | 47.8 | 3.5 | 4.4 |  |
| money_delta+pin_move | close | pin $1-2k | 67-70 | 48.9 | 1.6 | 2.7 |  |
| money_delta+pin_rlm | close | pin $1-2k | 43-45 | 48.9 | 5.2 | 10.7 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 50-45 | 52.6 | 7.0 | 9.5 |  |
| money_delta+sharp_gap | close | pin $1-2k | 89-95 | 48.4 | 3.9 | 5.5 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 46.9 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 46-37 | 55.4 | 7.6 | 7.9 |  |
| consensus_gap+money_delta | close | pin $1-2k | 18-26 | 40.9 | -0.7 | 2.5 |  |
| money_delta+pin_value | close | pin $1-2k | 43-45 | 48.9 | 0.7 | -3.4 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 20-37 | 35.1 | -9.2 | -20.8 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 12-28 | 30.0 | -19.0 | -42.4 |  |
| consensus_gap+follow_move | close | pin $2k+ | 39-31 | 55.7 | 2.7 | -4.9 |  |
| consensus_gap+money_delta | close | pin $2k+ | 9-26 | 25.7 | -8.9 | -49.8 |  |
| consensus_gap+money_level | close | pin $2k+ | 79-57 | 58.1 | -4.3 | -9.1 |  |
| consensus_gap+money_moving | close | pin $2k+ | 43-71 | 37.7 | -7.7 | -4.2 |  |
| consensus_gap+pin_move | close | pin $2k+ | 37-35 | 51.4 | 1.2 | -3.2 |  |
| consensus_gap+pin_value | close | pin $2k+ | 47-54 | 46.5 | 3.7 | 8.3 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 2-14 | 12.5 | -20.2 | -67.2 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 45-74 | 37.8 | -8.0 | -3.9 |  |
| follow_move+money_delta | close | pin $2k+ | 36-48 | 42.9 | 1.2 | -11.5 |  |
| follow_move+money_level | close | pin $2k+ | 159-103 | 60.7 | 1.4 | -2.4 |  |
| follow_move+money_moving | close | pin $2k+ | 125-127 | 49.6 | 1.8 | -4.9 |  |
| follow_move+pin_move | close | pin $2k+ | 163-160 | 50.5 | 0.7 | -4.7 |  |
| follow_move+pin_value | close | pin $2k+ | 39-37 | 51.3 | 3.8 | 9.8 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 43-65 | 39.8 | 2.1 | -11.2 |  |
| follow_move+sharp_gap | close | pin $2k+ | 126-128 | 49.6 | 1.9 | -4.7 |  |
| money_delta+money_level | close | pin $2k+ | 28-22 | 56.0 | 11.5 | 13.0 |  |
| money_delta+money_moving | close | pin $2k+ | 65-97 | 40.1 | 1.4 | -11.6 |  |
| money_delta+pin_move | close | pin $2k+ | 36-53 | 40.4 | -1.9 | -17.1 |  |
| money_delta+pin_value | close | pin $2k+ | 20-23 | 46.5 | 2.5 | -11.3 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 22-33 | 40.0 | 2.0 | -13.9 |  |
| money_delta+sharp_gap | close | pin $2k+ | 63-96 | 39.6 | 0.9 | -12.5 |  |
| money_level+money_moving | close | pin $2k+ | 178-162 | 52.4 | -0.4 | -4.9 |  |
| money_level+pin_move | close | pin $2k+ | 117-101 | 53.7 | -1.9 | -5.7 |  |
| money_level+pin_value | close | pin $2k+ | 61-59 | 50.8 | 1.2 | -5.9 |  |
| money_level+rlm_ratio | close | pin $2k+ | 16-14 | 53.3 | 7.7 | 11.3 |  |
| money_level+sharp_gap | close | pin $2k+ | 178-163 | 52.2 | -0.6 | -4.9 |  |
| money_moving+pin_move | close | pin $2k+ | 109-123 | 47.0 | 0.1 | -6.2 |  |
| money_moving+pin_value | close | pin $2k+ | 63-74 | 46.0 | 0.3 | 2.8 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 43-64 | 40.2 | 2.4 | -10.4 |  |
| money_moving+sharp_gap | close | pin $2k+ | 260-300 | 46.4 | 0.1 | -3.7 |  |
| pin_move+pin_value | close | pin $2k+ | 55-55 | 50.0 | 2.0 | -2.4 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 31-44 | 41.3 | 2.3 | -5.2 |  |
| pin_move+sharp_gap | close | pin $2k+ | 109-124 | 46.8 | -0.1 | -6.2 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 5-7 | 41.7 | -1.7 | -17.1 |  |
| pin_value+sharp_gap | close | pin $2k+ | 63-75 | 45.7 | 0.1 | 2.1 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 43-65 | 39.8 | 2.1 | -11.2 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 5-22 | 18.5 | -12.8 | -23.3 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 6-15 | 28.6 | -1.5 | -34.1 |  |
| follow_move+pin_rlm | close | pin $2k+ | 31-50 | 38.3 | 1.5 | -11.6 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 68-86 | 44.2 | 5.9 | 1.8 |  |
| money_moving+pin_rlm | close | pin $2k+ | 43-76 | 36.1 | 0.6 | -5.6 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 30-47 | 39.0 | 3.4 | -11.5 |  |
| pin_move+pin_rlm | close | pin $2k+ | 35-52 | 40.2 | 3.0 | -5.1 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 45-61 | 42.5 | 2.5 | -7.2 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 15-35 | 30.0 | -2.2 | -25.0 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 31-50 | 38.3 | 1.5 | -11.6 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 43-76 | 36.1 | 0.6 | -5.6 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 22-42 | 34.4 | 1.8 | -18.1 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 30-48 | 38.5 | 3.0 | -12.6 |  |
| money_delta+pin_rlm | close | pin $2k+ | 23-43 | 34.8 | -0.4 | -14.4 |  |
| money_level+pin_rlm | close | pin $2k+ | 16-10 | 61.5 | 18.1 | 30.4 |  |
| pin_rlm+pin_value | close | pin $2k+ | 6-13 | 31.6 | -5.2 | 13.6 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 19-28 | 40.4 | 2.0 | -16.6 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 6-10 | 37.5 | -1.6 | 35.0 |  |
| follow_move+money_delta | close | pin limit <$1k | 35-45 | 43.8 | -5.2 | -16.0 |  |
| money_level+money_moving | close | pin limit <$1k | 78-89 | 46.7 | -3.0 | -10.5 |  |
| money_level+sharp_gap | close | pin limit <$1k | 75-83 | 47.5 | -2.2 | -9.0 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 117-136 | 46.2 | -3.0 | -7.8 |  |
| consensus_gap+money_level | close | pin limit <$1k | 32-26 | 55.2 | 4.2 | 2.2 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 17-11 | 60.7 | 12.1 | 30.2 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 42-33 | 56.0 | 6.1 | 11.3 |  |
| follow_move+money_moving | close | pin limit <$1k | 72-90 | 44.4 | -4.7 | -14.6 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 77-89 | 46.4 | -2.8 | -10.9 |  |
| money_level+pin_move | close | pin limit <$1k | 60-56 | 51.7 | 1.8 | -1.3 |  |
| money_level+pin_value | close | pin limit <$1k | 57-36 | 61.3 | 11.0 | 15.9 |  |
| pin_move+pin_value | close | pin limit <$1k | 48-30 | 61.5 | 11.6 | 22.6 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 22-11 | 66.7 | 17.1 | 23.4 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 25-19 | 56.8 | 7.8 | 17.6 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 27-19 | 58.7 | 9.6 | 20.6 |  |
| follow_move+money_level | close | pin limit <$1k | 62-66 | 48.4 | -1.7 | -7.8 |  |
| follow_move+pin_move | close | pin limit <$1k | 68-73 | 48.2 | -1.2 | -7.6 |  |
| follow_move+pin_value | close | pin limit <$1k | 43-26 | 62.3 | 12.5 | 18.2 |  |
| money_moving+pin_move | close | pin limit <$1k | 66-72 | 47.8 | -1.4 | -5.3 |  |
| money_moving+pin_value | close | pin limit <$1k | 43-30 | 58.9 | 9.2 | 17.8 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 68-73 | 48.2 | -1.0 | -4.6 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 44-32 | 57.9 | 8.2 | 15.7 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 41-44 | 48.2 | -0.8 | -7.5 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 27-31 | 46.6 | -2.2 | -10.7 |  |
| money_delta+money_moving | close | pin limit <$1k | 50-54 | 48.1 | -0.8 | -3.6 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 9-6 | 60.0 | 13.1 | 43.2 |  |
| money_delta+money_level | close | pin limit <$1k | 26-23 | 53.1 | 3.6 | 1.7 |  |
| money_delta+pin_value | close | pin limit <$1k | 17-8 | 68.0 | 18.9 | 46.9 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 49-52 | 48.5 | -0.3 | -2.7 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 31-36 | 46.3 | -2.3 | -4.6 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 7-3 | 70.0 | 24.2 | 77.3 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 26-22 | 54.2 | 6.1 | 13.3 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 41-35 | 53.9 | 5.6 | 15.2 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 43-37 | 53.8 | 5.1 | 8.6 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-5 | 79.2 | 30.3 | 69.5 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 44-37 | 54.3 | 5.9 | 15.2 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 7-1 | 87.5 | 40.6 | 67.3 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 14-7 | 66.7 | 17.0 | 27.5 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 11-19 | 36.7 | -11.4 | -29.6 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 23-25 | 47.9 | -0.8 | -7.9 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 35-29 | 54.7 | 5.9 | 5.3 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 49-44 | 52.7 | 3.9 | 1.7 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 29-28 | 50.9 | 2.2 | -2.1 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 21-30 | 41.2 | -7.4 | -20.8 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 45-42 | 51.7 | 3.0 | -0.0 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 35-29 | 54.7 | 5.9 | 5.3 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 15-13 | 53.6 | 5.6 | 3.1 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 35-29 | 54.7 | 5.9 | 5.3 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 23-23 | 50.0 | 1.5 | -4.0 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 49-44 | 52.7 | 3.9 | 1.7 |  |
| money_level+pin_rlm | close | pin limit <$1k | 21-15 | 58.3 | 9.0 | 12.0 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 23-18 | 56.1 | 7.3 | 9.1 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 18-5 | 78.3 | 28.6 | 49.8 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 7-3 | 70.0 | 22.1 | 33.8 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 50.9 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.4 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -52.0 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 36-43 | 45.6 | 9.6 | 10.5 | 0.38 |
| rlm_quiet | early | pin $1-2k | 2-6 | 25.0 | -6.1 | 1.5 | -0.43 |
| rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| rlm_quiet | early | pin limit <$1k | 5-8 | 38.5 | -6.1 | -21.5 | 0.25 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.9 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 9-13 | 40.9 | -7.7 | -24.8 | 0.23 |
| pin_move | early | pin $1-2k | 0-5 | 0.0 | -40.6 | -100.0 | 0.14 |
| pin_move | early | pin limit <$1k | 9-9 | 50.0 | -1.0 | -8.1 | 0.19 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.4 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 9-8 | 52.9 | 12.4 | 15.5 | 0.01 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -40.5 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 5-0 | 100.0 | 51.0 | 88.6 | 0.0 |
| pin_rlm | early | <1k bets | 1-3 | 25.0 | -14.0 | -51.8 | -0.37 |
| pin_rlm | early | pin $1-2k | 0-3 | 0.0 | -42.7 | -100.0 | -0.67 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.6 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -52.0 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 481-423 | 53.2 | 1.7 | -6.0 | 0.17 |
| follow_move | early | pin $1-2k | 36-25 | 59.0 | 8.3 | 8.9 | -0.26 |
| follow_move | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
| follow_move | early | pin limit <$1k | 53-47 | 53.0 | 3.0 | 0.0 | -0.16 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.1 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 28-21 | 57.1 | 18.3 | 25.1 | 0.58 |
| rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.4 | 29.7 | -1.02 |
| rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
| rlm_ratio | early | pin limit <$1k | 8-1 | 88.9 | 44.1 | 79.0 | 0.37 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 1.5 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 44.0 | 59.7 | 0.33 |
| money_level | early | <1k bets | 172-113 | 60.4 | 0.7 | -5.1 | -0.15 |
| money_level | early | pin $1-2k | 22-10 | 68.8 | 3.9 | 2.2 | -0.01 |
| money_level | early | pin $2k+ | 1-1 | 50.0 | -12.6 | -47.2 | -0.7 |
| money_level | early | pin limit <$1k | 26-28 | 48.1 | -4.7 | -10.9 | 0.3 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.3 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.6 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 136-127 | 51.7 | 3.3 | -0.3 | 0.37 |
| sharp_gap | early | pin $1-2k | 17-13 | 56.7 | 1.9 | 4.4 | -0.36 |
| sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
| sharp_gap | early | pin limit <$1k | 31-20 | 60.8 | 12.1 | 25.3 | 0.17 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.6 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 52.0 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 98-93 | 51.3 | 0.5 | -9.2 | 0.08 |
| money_moving | early | pin $1-2k | 8-10 | 44.4 | -13.7 | -39.0 | 0.28 |
| money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.6 | -8.4 | 0.65 |
| money_moving | early | pin limit <$1k | 25-10 | 71.4 | 22.4 | 49.9 | 0.39 |
| pin_value | early | 1-3k bets | 13-10 | 56.5 | 8.4 | 6.3 | -0.04 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 47-49 | 49.0 | 0.1 | -7.5 | 0.06 |
| pin_value | early | pin $1-2k | 16-26 | 38.1 | -8.7 | -28.4 | 0.08 |
| pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.1 | 83.3 | 0.0 |
| pin_value | early | pin limit <$1k | 44-33 | 57.1 | 7.4 | 8.1 | 0.04 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -50.9 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -27.1 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.0 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.6 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 229-272 | 45.7 | -2.7 | -10.6 | 0.38 |
| consensus_gap | early | pin $1-2k | 18-23 | 43.9 | -2.5 | -17.8 | 0.2 |
| consensus_gap | early | pin $2k+ | 1-1 | 50.0 | 12.6 | -8.4 | 0.65 |
| consensus_gap | early | pin limit <$1k | 22-35 | 38.6 | -11.6 | -21.2 | 0.31 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -53.1 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.4 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.4 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -2.0 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.7 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 5.7 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.4 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 7-4 | 63.6 | 14.4 | 19.4 | -0.09 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.3 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 17.0 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.9 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -0.6 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 6-5 | 54.5 | 8.4 | 1.3 | 0.27 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -0.9 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-7 | 50.0 | 3.1 | -6.4 | -0.29 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.4 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.6 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -20.1 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.7 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 3.5 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.7 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.1 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.5 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.1 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.4 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.1 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.5 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.1 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 53.1 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 11.6 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 18.2 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 16.3 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 16.3 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| follow_move+rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -52.0 | -100.0 | -0.5 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 52.0 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.1 | 83.3 | 1.0 |
| rlm_quiet+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| rlm_quiet+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.1 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 39.4 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 50.9 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 32-38 | 45.7 | -6.5 | -17.8 | 0.83 |
| consensus_gap+money_level | early | <1k bets | 38-26 | 59.4 | -4.6 | -8.0 | 0.16 |
| consensus_gap+sharp_gap | early | <1k bets | 27-42 | 39.1 | -7.7 | -16.4 | 0.86 |
| follow_move+money_level | early | <1k bets | 87-42 | 67.4 | 6.3 | -0.5 | 0.1 |
| follow_move+sharp_gap | early | <1k bets | 72-40 | 64.3 | 14.3 | 15.0 | 0.6 |
| money_level+sharp_gap | early | <1k bets | 91-61 | 59.9 | 3.4 | -1.4 | 0.18 |
| follow_move+money_moving | early | <1k bets | 51-34 | 60.0 | 7.4 | 4.9 | 0.41 |
| money_level+money_moving | early | <1k bets | 60-44 | 57.7 | -0.8 | -8.0 | -0.17 |
| money_moving+sharp_gap | early | <1k bets | 59-56 | 51.3 | 2.7 | -5.5 | 0.28 |
| consensus_gap+money_moving | early | <1k bets | 14-22 | 38.9 | -9.8 | -38.1 | 0.35 |
| follow_move+pin_value | early | <1k bets | 16-14 | 53.3 | 3.8 | 0.1 | -0.18 |
| follow_move+rlm_quiet | early | <1k bets | 36-43 | 45.6 | 9.6 | 10.5 | 0.38 |
| money_moving+rlm_quiet | early | <1k bets | 14-13 | 51.9 | 14.6 | 23.4 | 0.5 |
| rlm_quiet+sharp_gap | early | <1k bets | 20-16 | 55.6 | 18.8 | 24.1 | -0.08 |
| follow_move+rlm_ratio | early | <1k bets | 28-21 | 57.1 | 18.3 | 25.1 | 0.58 |
| rlm_quiet+rlm_ratio | early | <1k bets | 18-12 | 60.0 | 23.6 | 36.2 | -0.06 |
| rlm_ratio+sharp_gap | early | <1k bets | 28-21 | 57.1 | 18.3 | 25.1 | 0.58 |
| pin_move+pin_value | early | <1k bets | 3-8 | 27.3 | -22.0 | -47.9 | 0.18 |
| follow_move+pin_move | early | <1k bets | 6-6 | 50.0 | -0.6 | -9.9 | 0.45 |
| consensus_gap+pin_value | early | <1k bets | 18-24 | 42.9 | -4.3 | -19.6 | 0.34 |
| pin_value+rlm_quiet | early | <1k bets | 0-3 | 0.0 | -43.4 | -100.0 | -0.6 |
| money_delta+money_moving | early | <1k bets | 8-8 | 50.0 | 10.0 | 10.8 | 0.01 |
| money_delta+sharp_gap | early | <1k bets | 7-6 | 53.8 | 14.3 | 21.7 | 0.01 |
| consensus_gap+pin_move | early | <1k bets | 1-5 | 16.7 | -28.8 | -68.2 | 0.22 |
| money_level+pin_move | early | <1k bets | 3-3 | 50.0 | -4.1 | -16.0 | 0.57 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -28.0 | -100.0 | -4.8 |
| consensus_gap+rlm_quiet | early | <1k bets | 3-5 | 37.5 | -1.1 | -22.7 | 1.01 |
| consensus_gap+rlm_ratio | early | <1k bets | 5-3 | 62.5 | 21.3 | 25.0 | 0.65 |
| follow_move+pin_rlm | early | <1k bets | 1-2 | 33.3 | -9.3 | -35.8 | -0.93 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -28.0 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | <1k bets | 0-1 | 0.0 | -28.0 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-2 | 33.3 | -9.3 | -35.8 | -0.93 |
| pin_rlm+sharp_gap | early | <1k bets | 1-3 | 25.0 | -14.0 | -51.8 | -0.37 |
| pin_value+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 24.6 | 27.3 | -0.93 |
| pin_value+sharp_gap | early | <1k bets | 6-6 | 50.0 | 0.2 | -4.5 | 0.41 |
| money_level+pin_value | early | <1k bets | 6-6 | 50.0 | -2.0 | -4.5 | 1.06 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -51.1 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -49.1 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 2-3 | 40.0 | -14.9 | -23.6 | 1.34 |
| money_level+rlm_ratio | early | <1k bets | 8-9 | 47.1 | 5.0 | -2.4 | 1.85 |
| money_moving+rlm_ratio | early | <1k bets | 14-9 | 60.9 | 18.9 | 35.3 | 0.65 |
| consensus_gap+money_delta | early | <1k bets | 2-0 | 100.0 | 50.0 | 90.9 | 0.5 |
| money_delta+money_level | early | <1k bets | 4-2 | 66.7 | 20.8 | 39.4 | 1.3 |
| pin_move+sharp_gap | early | <1k bets | 2-2 | 50.0 | -0.4 | -21.7 | 0.7 |
| money_level+pin_rlm | early | <1k bets | 1-1 | 50.0 | 0.0 | -3.7 | 1.0 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 4-4 | 50.0 | 8.8 | 27.0 | 0.42 |
| money_delta+rlm_quiet | early | <1k bets | 1-2 | 33.3 | -1.7 | 23.3 | -2.8 |
| money_delta+rlm_ratio | early | <1k bets | 3-2 | 60.0 | 19.3 | 65.0 | 1.12 |
| money_delta+pin_value | early | <1k bets | 2-0 | 100.0 | 50.9 | 90.9 | 0.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -28.0 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 6-4 | 60.0 | -4.5 | -4.6 | 0.25 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -30.3 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 7-11 | 38.9 | -3.8 | -28.1 | 0.15 |
| follow_move+rlm_quiet | early | pin $1-2k | 2-6 | 25.0 | -6.1 | 1.5 | -0.43 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.4 | 29.7 | -1.02 |
| follow_move+sharp_gap | early | pin $1-2k | 9-5 | 64.3 | 8.0 | 27.7 | -0.66 |
| money_level+money_moving | early | pin $1-2k | 8-6 | 57.1 | -8.2 | -21.6 | 0.19 |
| money_level+pin_value | early | pin $1-2k | 2-4 | 33.3 | -18.8 | -37.6 | 0.78 |
| money_moving+pin_value | early | pin $1-2k | 1-3 | 25.0 | -30.3 | -54.2 | 0.93 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -9.3 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -9.3 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -10.4 | 29.7 | -1.02 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -53.1 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -40.5 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -53.1 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -40.5 | -100.0 | 2.5 |
| money_level+sharp_gap | early | pin $1-2k | 14-6 | 70.0 | 5.6 | 7.8 | -0.25 |
| money_moving+sharp_gap | early | pin $1-2k | 4-7 | 36.4 | -21.4 | -50.4 | 0.23 |
| pin_value+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -25.0 | -52.3 | -0.52 |
| consensus_gap+follow_move | early | pin $1-2k | 5-6 | 45.5 | -2.5 | -18.8 | 0.45 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 0-3 | 0.0 | -28.0 | -100.0 | -0.97 |
| follow_move+pin_value | early | pin $1-2k | 6-7 | 46.2 | -1.4 | -14.7 | -0.25 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -28.0 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 11-5 | 68.8 | 4.2 | -0.1 | 0.03 |
| money_level+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -12.6 | -1.0 | 0.75 |
| follow_move+money_moving | early | pin $1-2k | 4-2 | 66.7 | 2.6 | -10.9 | -0.15 |
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
| pin_move+pin_value | early | pin $1-2k | 0-2 | 0.0 | -46.9 | -100.0 | 0.0 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -72.0 | -100.0 | 1.5 |
| follow_move+pin_move | early | pin $1-2k | 0-1 | 0.0 | -46.9 | -100.0 | 0.0 |
| consensus_gap+money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.6 | -8.4 | 0.65 |
| consensus_gap+pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.1 | 83.3 | 0.0 |
| follow_move+money_level | early | pin $2k+ | 0-1 | 0.0 | -53.1 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
| follow_move+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
| money_level+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -53.1 | -100.0 | 0.0 |
| money_level+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -53.1 | -100.0 | 0.0 |
| money_moving+pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.1 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
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
| follow_move+rlm_quiet | early | pin limit <$1k | 5-8 | 38.5 | -6.1 | -21.5 | 0.25 |
| money_level+money_moving | early | pin limit <$1k | 14-7 | 66.7 | 14.9 | 23.6 | 0.5 |
| money_level+sharp_gap | early | pin limit <$1k | 21-17 | 55.3 | 4.9 | 1.3 | 0.24 |
| money_moving+sharp_gap | early | pin limit <$1k | 20-6 | 76.9 | 28.8 | 65.2 | 0.31 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -50.9 | -100.0 | -1.0 |
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
| follow_move+rlm_ratio | early | pin limit <$1k | 8-1 | 88.9 | 44.1 | 79.0 | 0.37 |
| money_level+rlm_ratio | early | pin limit <$1k | 7-0 | 100.0 | 53.6 | 92.4 | 0.5 |
| pin_value+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.4 | 43.2 | -0.25 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 8-1 | 88.9 | 44.1 | 79.0 | 0.37 |
| consensus_gap+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 51.0 | 87.1 | 0.33 |
| consensus_gap+money_moving | early | pin limit <$1k | 8-3 | 72.7 | 25.3 | 74.0 | 0.58 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 2.0 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 51.0 | 87.1 | 0.33 |
| follow_move+money_moving | early | pin limit <$1k | 10-4 | 71.4 | 22.3 | 36.5 | 0.36 |
| money_delta+money_moving | early | pin limit <$1k | 4-0 | 100.0 | 51.0 | 88.0 | 0.0 |
| money_delta+pin_value | early | pin limit <$1k | 4-0 | 100.0 | 51.0 | 88.0 | 0.0 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 53.1 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 3-2 | 60.0 | 11.0 | 13.0 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 30.2 | 54.4 | -0.2 |
| money_delta+sharp_gap | early | pin limit <$1k | 3-0 | 100.0 | 50.3 | 89.6 | 0.0 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 10.6 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | 5.7 | 13.7 | -0.05 |
| pin_move+pin_value | early | pin limit <$1k | 3-6 | 33.3 | -16.4 | -36.4 | 0.22 |
| follow_move+pin_move | early | pin limit <$1k | 6-5 | 54.5 | 3.6 | -1.7 | 0.49 |
| consensus_gap+pin_move | early | pin limit <$1k | 1-3 | 25.0 | -29.2 | -52.3 | 0.4 |
| money_level+pin_move | early | pin limit <$1k | 3-3 | 50.0 | -4.1 | -16.0 | 0.57 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -49.1 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -49.1 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | -0.4 | -21.7 | 0.7 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 72.0 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 2-0 | 100.0 | 50.9 | 90.9 | 0.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 50.9 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 50.9 | 90.9 | 1.0 |
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
| rlm_quiet | close | 1-3k bets | 38-61 | 38.4 | -3.4 | -9.9 |  |
| rlm_quiet | close | 3k+ bets | 5-15 | 25.0 | -17.5 | -49.1 |  |
| rlm_quiet | close | <1k bets | 4-17 | 19.0 | -22.5 | -63.3 |  |
| rlm_quiet | close | pin $1-2k | 16-31 | 34.0 | -9.2 | -30.7 |  |
| rlm_quiet | close | pin $2k+ | 15-23 | 39.5 | -2.4 | 12.2 |  |
| rlm_quiet | close | pin limit <$1k | 5-8 | 38.5 | -5.3 | -25.5 |  |
| pin_move | close | 1-3k bets | 69-70 | 49.6 | 0.3 | -3.1 |  |
| pin_move | close | 3k+ bets | 13-24 | 35.1 | -15.0 | -33.5 |  |
| pin_move | close | <1k bets | 10-11 | 47.6 | -3.8 | -10.9 |  |
| pin_move | close | pin $1-2k | 40-47 | 46.0 | -3.8 | -9.8 |  |
| pin_move | close | pin $2k+ | 38-40 | 48.7 | -1.1 | -6.7 |  |
| pin_move | close | pin limit <$1k | 14-18 | 43.8 | -5.6 | -16.4 |  |
| money_delta | close | 1-3k bets | 34-43 | 44.2 | 2.1 | -12.5 |  |
| money_delta | close | 3k+ bets | 9-9 | 50.0 | 7.1 | 0.1 |  |
| money_delta | close | <1k bets | 10-10 | 50.0 | 7.5 | 17.9 |  |
| money_delta | close | pin $1-2k | 20-14 | 58.8 | 14.8 | 24.1 |  |
| money_delta | close | pin $2k+ | 10-17 | 37.0 | -2.1 | -24.7 |  |
| money_delta | close | pin limit <$1k | 8-11 | 42.1 | -1.6 | -18.7 |  |
| pin_rlm | close | 1-3k bets | 14-20 | 41.2 | 0.6 | -13.8 |  |
| pin_rlm | close | 3k+ bets | 2-4 | 33.3 | -7.6 | -28.5 |  |
| pin_rlm | close | <1k bets | 1-3 | 25.0 | -18.5 | -52.3 |  |
| pin_rlm | close | pin $1-2k | 9-9 | 50.0 | 6.3 | -3.4 |  |
| pin_rlm | close | pin $2k+ | 5-10 | 33.3 | -2.9 | -18.1 |  |
| pin_rlm | close | pin limit <$1k | 3-8 | 27.3 | -15.4 | -46.7 |  |
| follow_move | close | 1-3k bets | 107-128 | 45.5 | -3.7 | -9.0 |  |
| follow_move | close | 3k+ bets | 21-27 | 43.8 | -7.3 | -21.9 |  |
| follow_move | close | <1k bets | 23-31 | 42.6 | -6.1 | -25.0 |  |
| follow_move | close | pin $1-2k | 52-62 | 45.6 | -3.8 | -13.2 |  |
| follow_move | close | pin $2k+ | 47-47 | 50.0 | -0.0 | 5.4 |  |
| follow_move | close | pin limit <$1k | 14-23 | 37.8 | -11.1 | -27.5 |  |
| rlm_ratio | close | 1-3k bets | 22-41 | 34.9 | -5.8 | -28.8 |  |
| rlm_ratio | close | 3k+ bets | 5-7 | 41.7 | -1.2 | -15.8 |  |
| rlm_ratio | close | <1k bets | 3-7 | 30.0 | -10.7 | -42.9 |  |
| rlm_ratio | close | pin $1-2k | 14-12 | 53.8 | 11.6 | 5.4 |  |
| rlm_ratio | close | pin $2k+ | 5-12 | 29.4 | -6.6 | -30.5 |  |
| rlm_ratio | close | pin limit <$1k | 5-10 | 33.3 | -10.4 | -35.7 |  |
| money_level | close | 1-3k bets | 131-103 | 56.0 | -0.6 | -4.0 |  |
| money_level | close | 3k+ bets | 34-27 | 55.7 | -0.2 | -4.8 |  |
| money_level | close | <1k bets | 38-11 | 77.6 | 21.2 | 32.8 |  |
| money_level | close | pin $1-2k | 61-44 | 58.1 | 2.7 | 3.2 |  |
| money_level | close | pin $2k+ | 55-44 | 55.6 | -1.1 | -7.7 |  |
| money_level | close | pin limit <$1k | 22-18 | 55.0 | 1.1 | 4.4 |  |
| sharp_gap | close | 1-3k bets | 97-117 | 45.3 | -2.4 | -12.5 |  |
| sharp_gap | close | 3k+ bets | 26-33 | 44.1 | -5.3 | -15.5 |  |
| sharp_gap | close | <1k bets | 25-20 | 55.6 | 8.0 | 8.4 |  |
| sharp_gap | close | pin $1-2k | 51-44 | 53.7 | 4.4 | 3.4 |  |
| sharp_gap | close | pin $2k+ | 42-51 | 45.2 | -1.7 | -9.4 |  |
| sharp_gap | close | pin limit <$1k | 13-23 | 36.1 | -11.4 | -30.9 |  |
| money_moving | close | 1-3k bets | 102-116 | 46.8 | -1.6 | -10.7 |  |
| money_moving | close | 3k+ bets | 26-33 | 44.1 | -5.3 | -15.5 |  |
| money_moving | close | <1k bets | 26-19 | 57.8 | 9.3 | 10.5 |  |
| money_moving | close | pin $1-2k | 52-43 | 54.7 | 4.9 | 4.6 |  |
| money_moving | close | pin $2k+ | 42-51 | 45.2 | -1.7 | -9.4 |  |
| money_moving | close | pin limit <$1k | 15-25 | 37.5 | -10.6 | -28.4 |  |
| pin_value | close | 1-3k bets | 58-42 | 58.0 | 7.5 | 21.0 |  |
| pin_value | close | 3k+ bets | 9-13 | 40.9 | -11.4 | -21.9 |  |
| pin_value | close | <1k bets | 11-7 | 61.1 | 12.6 | 35.7 |  |
| pin_value | close | pin $1-2k | 37-31 | 54.4 | 4.5 | 11.1 |  |
| pin_value | close | pin $2k+ | 21-22 | 48.8 | -0.5 | 14.1 |  |
| pin_value | close | pin limit <$1k | 20-9 | 69.0 | 15.5 | 30.8 |  |
| consensus_gap | close | 1-3k bets | 49-37 | 57.0 | 3.7 | 4.8 |  |
| consensus_gap | close | 3k+ bets | 11-10 | 52.4 | -1.4 | -12.1 |  |
| consensus_gap | close | <1k bets | 15-3 | 83.3 | 29.4 | 56.5 |  |
| consensus_gap | close | pin $1-2k | 17-15 | 53.1 | -1.6 | 10.8 |  |
| consensus_gap | close | pin $2k+ | 35-15 | 70.0 | 14.8 | 24.3 |  |
| consensus_gap | close | pin limit <$1k | 7-2 | 77.8 | 28.1 | 48.3 |  |
| follow_move+pin_move | close | 1-3k bets | 47-62 | 43.1 | -5.7 | -15.9 |  |
| money_delta+money_moving | close | 1-3k bets | 26-30 | 46.4 | 5.3 | -7.1 |  |
| money_delta+sharp_gap | close | 1-3k bets | 26-29 | 47.3 | 6.2 | -5.5 |  |
| money_moving+sharp_gap | close | 1-3k bets | 95-112 | 45.9 | -2.1 | -11.4 |  |
| consensus_gap+money_level | close | 1-3k bets | 33-21 | 61.1 | 1.7 | -0.0 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 38-61 | 38.4 | -3.4 | -9.9 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 19-29 | 39.6 | -3.4 | -16.5 |  |
| consensus_gap+follow_move | close | 1-3k bets | 14-16 | 46.7 | -4.7 | -11.9 |  |
| follow_move+money_level | close | 1-3k bets | 50-46 | 52.1 | -4.2 | -7.8 |  |
| money_level+money_moving | close | 1-3k bets | 69-62 | 52.7 | -1.0 | -5.3 |  |
| money_level+sharp_gap | close | 1-3k bets | 65-61 | 51.6 | -1.6 | -5.9 |  |
| consensus_gap+money_moving | close | 1-3k bets | 15-19 | 44.1 | -6.4 | -9.1 |  |
| consensus_gap+pin_move | close | 1-3k bets | 12-6 | 66.7 | 15.9 | 39.2 |  |
| consensus_gap+pin_value | close | 1-3k bets | 17-13 | 56.7 | 6.4 | 6.2 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 14-19 | 42.4 | -7.0 | -9.8 |  |
| follow_move+money_moving | close | 1-3k bets | 49-65 | 43.0 | -4.9 | -18.2 |  |
| follow_move+pin_value | close | 1-3k bets | 19-13 | 59.4 | 7.8 | 42.3 |  |
| follow_move+sharp_gap | close | 1-3k bets | 51-68 | 42.9 | -4.6 | -18.4 |  |
| money_level+pin_move | close | 1-3k bets | 30-26 | 53.6 | -1.3 | -3.3 |  |
| money_level+pin_value | close | 1-3k bets | 21-15 | 58.3 | 5.2 | 9.4 |  |
| money_moving+pin_move | close | 1-3k bets | 31-30 | 50.8 | 3.1 | -0.9 |  |
| money_moving+pin_value | close | 1-3k bets | 18-17 | 51.4 | 0.2 | -3.3 |  |
| pin_move+pin_value | close | 1-3k bets | 21-15 | 58.3 | 6.3 | 9.6 |  |
| pin_move+sharp_gap | close | 1-3k bets | 29-32 | 47.5 | 0.4 | -7.1 |  |
| pin_value+sharp_gap | close | 1-3k bets | 17-16 | 51.5 | 1.1 | -3.2 |  |
| follow_move+money_delta | close | 1-3k bets | 21-31 | 40.4 | -2.6 | -20.9 |  |
| money_delta+pin_move | close | 1-3k bets | 13-14 | 48.1 | 6.7 | -5.3 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 12-24 | 33.3 | -7.6 | -34.2 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 22-41 | 34.9 | -5.8 | -28.8 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 14-30 | 31.8 | -6.9 | -32.7 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 22-38 | 36.7 | -4.2 | -25.2 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 10-30 | 25.0 | -13.5 | -46.6 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 14-34 | 29.2 | -9.3 | -38.3 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 22-41 | 34.9 | -5.8 | -28.8 |  |
| money_delta+money_level | close | 1-3k bets | 9-5 | 64.3 | 15.6 | 24.7 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 4-8 | 33.3 | -4.3 | -23.2 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 4-4 | 50.0 | 11.7 | 14.4 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 15-22 | 40.5 | -0.3 | -19.8 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 2-2 | 50.0 | 5.6 | 35.0 |  |
| money_level+pin_rlm | close | 1-3k bets | 6-3 | 66.7 | 21.3 | 31.1 |  |
| money_moving+pin_rlm | close | 1-3k bets | 14-18 | 43.8 | 3.1 | -8.4 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 14-20 | 41.2 | 0.6 | -13.8 |  |
| money_level+rlm_ratio | close | 1-3k bets | 10-8 | 55.6 | 9.7 | 8.0 |  |
| consensus_gap+money_delta | close | 1-3k bets | 4-2 | 66.7 | 25.4 | 27.8 |  |
| follow_move+pin_rlm | close | 1-3k bets | 12-17 | 41.4 | 2.0 | -13.5 |  |
| money_delta+pin_rlm | close | 1-3k bets | 8-11 | 42.1 | 4.0 | -15.8 |  |
| pin_move+pin_rlm | close | 1-3k bets | 14-15 | 48.3 | 7.7 | 1.1 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 13-14 | 48.1 | 7.5 | -0.2 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 6-14 | 30.0 | -8.3 | -33.5 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 12-17 | 41.4 | 2.0 | -13.5 |  |
| money_delta+pin_value | close | 1-3k bets | 8-3 | 72.7 | 26.7 | 37.9 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 5-6 | 45.5 | 0.2 | 75.3 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 4-1 | 80.0 | 28.4 | 49.9 |  |
| pin_rlm+pin_value | close | 1-3k bets | 2-2 | 50.0 | -0.4 | -5.5 |  |
| money_level+money_moving | close | 3k+ bets | 18-19 | 48.6 | -5.3 | -9.9 |  |
| money_level+sharp_gap | close | 3k+ bets | 18-19 | 48.6 | -5.3 | -9.9 |  |
| money_moving+sharp_gap | close | 3k+ bets | 26-33 | 44.1 | -5.3 | -15.5 |  |
| follow_move+money_delta | close | 3k+ bets | 4-5 | 44.4 | -1.6 | -14.2 |  |
| follow_move+money_level | close | 3k+ bets | 12-10 | 54.5 | -5.6 | -13.0 |  |
| follow_move+money_moving | close | 3k+ bets | 11-15 | 42.3 | -8.6 | -20.9 |  |
| follow_move+pin_move | close | 3k+ bets | 10-21 | 32.3 | -18.2 | -39.6 |  |
| follow_move+pin_rlm | close | 3k+ bets | 2-4 | 33.3 | -7.6 | -28.5 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 5-7 | 41.7 | -1.2 | -15.8 |  |
| follow_move+sharp_gap | close | 3k+ bets | 11-15 | 42.3 | -8.6 | -20.9 |  |
| money_delta+money_level | close | 3k+ bets | 3-0 | 100.0 | 52.7 | 93.5 |  |
| money_delta+money_moving | close | 3k+ bets | 8-7 | 53.3 | 11.5 | 6.9 |  |
| money_delta+pin_move | close | 3k+ bets | 2-4 | 33.3 | -13.4 | -35.7 |  |
| money_delta+pin_rlm | close | 3k+ bets | 1-2 | 33.3 | -7.0 | -34.9 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 3-3 | 50.0 | 7.5 | -3.1 |  |
| money_delta+sharp_gap | close | 3k+ bets | 8-7 | 53.3 | 11.5 | 6.9 |  |
| money_level+pin_move | close | 3k+ bets | 7-9 | 43.8 | -13.2 | -23.0 |  |
| money_level+pin_rlm | close | 3k+ bets | 1-0 | 100.0 | 56.5 | 95.2 |  |
| money_level+rlm_ratio | close | 3k+ bets | 2-1 | 66.7 | 14.5 | 28.7 |  |
| money_moving+pin_move | close | 3k+ bets | 6-12 | 33.3 | -17.8 | -38.6 |  |
| money_moving+pin_rlm | close | 3k+ bets | 2-4 | 33.3 | -7.6 | -28.5 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 5-7 | 41.7 | -1.2 | -15.8 |  |
| pin_move+pin_rlm | close | 3k+ bets | 1-4 | 20.0 | -22.3 | -61.0 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 1-5 | 16.7 | -28.0 | -67.5 |  |
| pin_move+sharp_gap | close | 3k+ bets | 6-12 | 33.3 | -17.8 | -38.6 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 2-4 | 33.3 | -7.6 | -28.5 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 2-4 | 33.3 | -7.6 | -28.5 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 5-7 | 41.7 | -1.2 | -15.8 |  |
| consensus_gap+money_level | close | 3k+ bets | 9-5 | 64.3 | 4.0 | 3.4 |  |
| consensus_gap+money_moving | close | 3k+ bets | 5-7 | 41.7 | -12.5 | -26.6 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 5-7 | 41.7 | -12.5 | -26.6 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 5-15 | 25.0 | -17.5 | -49.1 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 3-12 | 20.0 | -23.4 | -58.1 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 2-5 | 28.6 | -16.4 | -44.8 |  |
| money_level+pin_value | close | 3k+ bets | 6-7 | 46.2 | -7.2 | -13.2 |  |
| money_moving+pin_value | close | 3k+ bets | 5-7 | 41.7 | -12.1 | -21.7 |  |
| pin_value+sharp_gap | close | 3k+ bets | 5-7 | 41.7 | -12.1 | -21.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 6-4 | 60.0 | 4.1 | -4.5 |  |
| consensus_gap+pin_value | close | 3k+ bets | 5-3 | 62.5 | 13.0 | 19.8 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 3-8 | 27.3 | -16.6 | -47.2 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 3-8 | 27.3 | -16.6 | -47.2 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 0-4 | 0.0 | -42.1 | -100.0 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 2-6 | 25.0 | -15.4 | -51.2 |  |
| pin_move+pin_value | close | 3k+ bets | 5-9 | 35.7 | -16.8 | -31.7 |  |
| follow_move+pin_value | close | 3k+ bets | 3-6 | 33.3 | -22.5 | -37.2 |  |
| consensus_gap+money_delta | close | 3k+ bets | 1-0 | 100.0 | 42.0 | 90.9 |  |
| consensus_gap+pin_move | close | 3k+ bets | 6-4 | 60.0 | 9.6 | 8.6 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 1-3 | 25.0 | -20.7 | -52.3 |  |
| money_delta+pin_value | close | 3k+ bets | 1-1 | 50.0 | -8.0 | -4.5 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 1-3 | 25.0 | -27.0 | -52.3 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 0-2 | 0.0 | -45.3 | -100.0 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 0-2 | 0.0 | -45.3 | -100.0 |  |
| consensus_gap+money_level | close | <1k bets | 11-1 | 91.7 | 33.2 | 42.3 |  |
| consensus_gap+money_moving | close | <1k bets | 8-0 | 100.0 | 45.0 | 103.6 |  |
| consensus_gap+pin_value | close | <1k bets | 4-1 | 80.0 | 36.4 | 123.1 |  |
| consensus_gap+sharp_gap | close | <1k bets | 9-1 | 90.0 | 36.0 | 77.0 |  |
| follow_move+pin_move | close | <1k bets | 6-10 | 37.5 | -13.2 | -30.3 |  |
| follow_move+rlm_quiet | close | <1k bets | 4-17 | 19.0 | -22.5 | -63.3 |  |
| money_level+money_moving | close | <1k bets | 20-5 | 80.0 | 25.5 | 38.3 |  |
| money_level+pin_value | close | <1k bets | 5-1 | 83.3 | 34.1 | 56.7 |  |
| money_level+sharp_gap | close | <1k bets | 19-5 | 79.2 | 25.2 | 40.2 |  |
| money_moving+pin_value | close | <1k bets | 4-1 | 80.0 | 39.0 | 124.8 |  |
| money_moving+sharp_gap | close | <1k bets | 24-18 | 57.1 | 9.4 | 12.8 |  |
| pin_move+rlm_quiet | close | <1k bets | 2-4 | 33.3 | -13.4 | -36.4 |  |
| pin_value+sharp_gap | close | <1k bets | 4-1 | 80.0 | 39.0 | 124.8 |  |
| follow_move+money_moving | close | <1k bets | 10-10 | 50.0 | 1.5 | -17.8 |  |
| follow_move+sharp_gap | close | <1k bets | 9-10 | 47.4 | -0.2 | -18.3 |  |
| money_level+pin_move | close | <1k bets | 6-3 | 66.7 | 11.1 | 22.8 |  |
| money_moving+rlm_quiet | close | <1k bets | 2-6 | 25.0 | -15.0 | -52.3 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 2-6 | 25.0 | -15.0 | -52.3 |  |
| follow_move+money_delta | close | <1k bets | 5-7 | 41.7 | -2.5 | -20.5 |  |
| follow_move+pin_rlm | close | <1k bets | 1-3 | 25.0 | -18.5 | -52.3 |  |
| follow_move+pin_value | close | <1k bets | 3-2 | 60.0 | 11.6 | 15.4 |  |
| follow_move+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -10.7 | -42.9 |  |
| money_delta+money_moving | close | <1k bets | 7-8 | 46.7 | 6.3 | 18.9 |  |
| money_delta+pin_move | close | <1k bets | 1-2 | 33.3 | -10.1 | -36.4 |  |
| money_delta+pin_rlm | close | <1k bets | 1-2 | 33.3 | -10.1 | -36.4 |  |
| money_delta+pin_value | close | <1k bets | 3-0 | 100.0 | 59.6 | 212.0 |  |
| money_delta+rlm_quiet | close | <1k bets | 3-4 | 42.9 | 1.3 | -17.2 |  |
| money_delta+rlm_ratio | close | <1k bets | 3-5 | 37.5 | -3.6 | -28.6 |  |
| money_delta+sharp_gap | close | <1k bets | 7-8 | 46.7 | 6.3 | 18.9 |  |
| money_moving+pin_move | close | <1k bets | 3-3 | 50.0 | 4.6 | -5.2 |  |
| money_moving+pin_rlm | close | <1k bets | 1-3 | 25.0 | -18.5 | -52.3 |  |
| money_moving+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -10.7 | -42.9 |  |
| pin_move+pin_rlm | close | <1k bets | 1-3 | 25.0 | -18.5 | -52.3 |  |
| pin_move+pin_value | close | <1k bets | 4-1 | 80.0 | 28.4 | 52.8 |  |
| pin_move+rlm_ratio | close | <1k bets | 1-3 | 25.0 | -18.5 | -52.3 |  |
| pin_move+sharp_gap | close | <1k bets | 3-3 | 50.0 | 4.6 | -5.2 |  |
| pin_rlm+pin_value | close | <1k bets | 1-0 | 100.0 | 56.5 | 90.9 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 1-1 | 50.0 | 6.5 | -4.5 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 1-3 | 25.0 | -18.5 | -52.3 |  |
| pin_rlm+sharp_gap | close | <1k bets | 1-3 | 25.0 | -18.5 | -52.3 |  |
| pin_value+rlm_quiet | close | <1k bets | 2-0 | 100.0 | 56.5 | 90.9 |  |
| pin_value+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 56.5 | 90.9 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 2-5 | 28.6 | -10.9 | -45.5 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 3-7 | 30.0 | -10.7 | -42.9 |  |
| consensus_gap+follow_move | close | <1k bets | 5-0 | 100.0 | 43.1 | 71.3 |  |
| consensus_gap+pin_move | close | <1k bets | 2-0 | 100.0 | 45.3 | 70.5 |  |
| follow_move+money_level | close | <1k bets | 12-4 | 75.0 | 16.7 | 21.7 |  |
| money_delta+money_level | close | <1k bets | 2-1 | 66.7 | 26.3 | 53.8 |  |
| money_level+pin_rlm | close | <1k bets | 0-1 | 0.0 | -43.5 | -100.0 |  |
| money_level+rlm_ratio | close | <1k bets | 1-1 | 50.0 | 6.5 | -5.3 |  |
| consensus_gap+money_delta | close | <1k bets | 3-0 | 100.0 | 52.2 | 208.0 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 56.5 | 89.3 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-0 | 100.0 | 56.5 | 90.9 |  |
| money_delta+money_moving | close | pin $1-2k | 12-5 | 70.6 | 29.1 | 57.8 |  |
| money_delta+sharp_gap | close | pin $1-2k | 12-5 | 70.6 | 29.1 | 57.8 |  |
| money_moving+sharp_gap | close | pin $1-2k | 49-41 | 54.4 | 4.9 | 5.4 |  |
| consensus_gap+follow_move | close | pin $1-2k | 7-8 | 46.7 | -8.1 | -16.8 |  |
| consensus_gap+money_level | close | pin $1-2k | 11-8 | 57.9 | -1.3 | -2.2 |  |
| consensus_gap+money_moving | close | pin $1-2k | 6-8 | 42.9 | -9.9 | -3.4 |  |
| consensus_gap+pin_move | close | pin $1-2k | 5-6 | 45.5 | -6.1 | 3.3 |  |
| consensus_gap+pin_value | close | pin $1-2k | 7-7 | 50.0 | -2.2 | 20.0 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 6-7 | 46.2 | -8.1 | 6.1 |  |
| follow_move+money_level | close | pin $1-2k | 26-21 | 55.3 | 0.5 | 0.1 |  |
| follow_move+money_moving | close | pin $1-2k | 27-25 | 51.9 | 2.9 | -2.6 |  |
| follow_move+pin_move | close | pin $1-2k | 25-44 | 36.2 | -12.9 | -29.3 |  |
| follow_move+pin_value | close | pin $1-2k | 12-12 | 50.0 | -1.3 | -5.5 |  |
| follow_move+sharp_gap | close | pin $1-2k | 29-27 | 51.8 | 2.9 | -3.6 |  |
| money_level+money_moving | close | pin $1-2k | 38-25 | 60.3 | 6.6 | 8.7 |  |
| money_level+pin_move | close | pin $1-2k | 17-17 | 50.0 | -4.3 | -7.4 |  |
| money_level+pin_value | close | pin $1-2k | 14-10 | 58.3 | 5.9 | 9.0 |  |
| money_level+sharp_gap | close | pin $1-2k | 37-25 | 59.7 | 6.4 | 8.7 |  |
| money_moving+pin_move | close | pin $1-2k | 20-18 | 52.6 | 3.0 | -0.5 |  |
| money_moving+pin_value | close | pin $1-2k | 13-10 | 56.5 | 5.6 | 21.8 |  |
| pin_move+pin_value | close | pin $1-2k | 14-10 | 58.3 | 5.8 | 9.9 |  |
| pin_move+sharp_gap | close | pin $1-2k | 20-20 | 50.0 | 0.9 | -5.5 |  |
| pin_value+sharp_gap | close | pin $1-2k | 13-10 | 56.5 | 6.2 | 21.8 |  |
| follow_move+money_delta | close | pin $1-2k | 13-12 | 52.0 | 7.1 | 0.8 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 16-31 | 34.0 | -9.2 | -30.7 |  |
| money_delta+pin_move | close | pin $1-2k | 9-7 | 56.2 | 13.4 | 9.4 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 8-12 | 40.0 | -4.0 | -22.4 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 11-21 | 34.4 | -9.9 | -31.3 |  |
| follow_move+pin_rlm | close | pin $1-2k | 8-9 | 47.1 | 4.2 | -9.0 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 14-12 | 53.8 | 11.6 | 5.4 |  |
| pin_move+pin_rlm | close | pin $1-2k | 9-7 | 56.2 | 11.4 | 8.6 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 8-8 | 50.0 | 5.2 | -3.3 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 4-9 | 30.8 | -11.6 | -40.6 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 8-9 | 47.1 | 4.2 | -9.0 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 9-9 | 50.0 | 6.3 | -3.4 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 6-10 | 37.5 | -3.9 | -27.0 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 8-12 | 40.0 | -1.3 | -22.3 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 14-12 | 53.8 | 11.6 | 5.4 |  |
| money_delta+money_level | close | pin $1-2k | 4-0 | 100.0 | 55.6 | 95.8 |  |
| money_delta+pin_rlm | close | pin $1-2k | 6-3 | 66.7 | 25.3 | 29.9 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 8-4 | 66.7 | 24.4 | 29.6 |  |
| money_level+pin_rlm | close | pin $1-2k | 4-0 | 100.0 | 55.6 | 93.8 |  |
| money_level+rlm_ratio | close | pin $1-2k | 7-2 | 77.8 | 33.1 | 50.4 |  |
| money_moving+pin_rlm | close | pin $1-2k | 9-7 | 56.2 | 12.0 | 8.6 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 14-10 | 58.3 | 15.8 | 14.1 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 8-10 | 44.4 | 2.8 | -13.7 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 1-4 | 20.0 | -23.4 | -61.8 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 4-6 | 40.0 | -6.4 | -23.2 |  |
| money_delta+pin_value | close | pin $1-2k | 6-3 | 66.7 | 24.2 | 67.2 |  |
| consensus_gap+money_delta | close | pin $1-2k | 2-1 | 66.7 | 22.0 | 144.9 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 0-2 | 0.0 | -45.3 | -100.0 |  |
| pin_rlm+pin_value | close | pin $1-2k | 3-1 | 75.0 | 24.6 | 42.2 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 2-1 | 66.7 | 18.8 | 26.0 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 0-1 | 0.0 | -56.5 | -100.0 |  |
| follow_move+pin_move | close | pin $2k+ | 30-36 | 45.5 | -4.5 | -13.1 |  |
| consensus_gap+money_level | close | pin $2k+ | 25-11 | 69.4 | 9.3 | 8.9 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 15-23 | 39.5 | -2.4 | 12.2 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 10-20 | 33.3 | -9.0 | -25.4 |  |
| money_level+money_moving | close | pin $2k+ | 28-29 | 49.1 | -3.1 | -10.6 |  |
| money_level+sharp_gap | close | pin $2k+ | 28-29 | 49.1 | -3.1 | -10.6 |  |
| money_moving+sharp_gap | close | pin $2k+ | 42-51 | 45.2 | -1.7 | -9.4 |  |
| consensus_gap+pin_value | close | pin $2k+ | 13-8 | 61.9 | 15.4 | 16.5 |  |
| follow_move+money_level | close | pin $2k+ | 20-15 | 57.1 | -2.9 | -4.7 |  |
| follow_move+money_moving | close | pin $2k+ | 18-23 | 43.9 | -4.6 | -14.9 |  |
| follow_move+sharp_gap | close | pin $2k+ | 18-23 | 43.9 | -4.6 | -14.9 |  |
| money_level+pin_move | close | pin $2k+ | 16-12 | 57.1 | -1.9 | -3.5 |  |
| money_moving+pin_move | close | pin $2k+ | 13-16 | 44.8 | -2.2 | -10.4 |  |
| pin_move+sharp_gap | close | pin $2k+ | 13-16 | 44.8 | -2.2 | -10.4 |  |
| money_delta+money_level | close | pin $2k+ | 4-1 | 80.0 | 36.4 | 56.8 |  |
| money_delta+money_moving | close | pin $2k+ | 9-17 | 34.6 | -3.8 | -29.1 |  |
| money_delta+sharp_gap | close | pin $2k+ | 9-17 | 34.6 | -3.8 | -29.1 |  |
| consensus_gap+money_moving | close | pin $2k+ | 12-10 | 54.5 | 2.0 | 14.6 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 12-10 | 54.5 | 2.0 | 14.6 |  |
| money_level+pin_value | close | pin $2k+ | 7-9 | 43.8 | -6.7 | -18.1 |  |
| money_moving+pin_value | close | pin $2k+ | 7-10 | 41.2 | -9.3 | -22.6 |  |
| pin_value+sharp_gap | close | pin $2k+ | 7-10 | 41.2 | -9.3 | -22.6 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 1-2 | 33.3 | -11.4 | 13.3 |  |
| money_level+pin_rlm | close | pin $2k+ | 1-1 | 50.0 | 0.0 | 7.0 |  |
| money_moving+pin_rlm | close | pin $2k+ | 5-10 | 33.3 | -2.9 | -18.1 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 5-10 | 33.3 | -2.9 | -18.1 |  |
| follow_move+money_delta | close | pin $2k+ | 5-10 | 33.3 | -7.7 | -34.1 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 5-12 | 29.4 | -6.6 | -30.5 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 3-9 | 25.0 | -11.8 | -49.4 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 5-12 | 29.4 | -6.6 | -30.5 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 5-12 | 29.4 | -6.6 | -30.5 |  |
| money_level+rlm_ratio | close | pin $2k+ | 2-1 | 66.7 | 24.6 | 32.9 |  |
| consensus_gap+follow_move | close | pin $2k+ | 12-3 | 80.0 | 21.5 | 39.8 |  |
| consensus_gap+pin_move | close | pin $2k+ | 13-3 | 81.2 | 28.8 | 50.4 |  |
| follow_move+pin_value | close | pin $2k+ | 6-6 | 50.0 | -2.0 | 74.7 |  |
| pin_move+pin_value | close | pin $2k+ | 9-10 | 47.4 | -3.4 | -10.8 |  |
| follow_move+pin_rlm | close | pin $2k+ | 4-8 | 33.3 | -0.8 | -17.0 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 4-8 | 33.3 | -0.8 | -17.0 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 2-3 | 40.0 | -8.4 | 170.2 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 4-11 | 26.7 | -11.3 | -35.3 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 4-11 | 26.7 | -11.3 | -35.3 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 3-8 | 27.3 | -13.4 | -46.4 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 2-9 | 18.2 | -15.9 | -50.2 |  |
| money_delta+pin_move | close | pin $2k+ | 5-7 | 41.7 | -0.4 | -17.6 |  |
| money_delta+pin_rlm | close | pin $2k+ | 2-7 | 22.2 | -11.9 | -53.1 |  |
| pin_move+pin_rlm | close | pin $2k+ | 4-7 | 36.4 | 2.2 | -9.6 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 4-7 | 36.4 | 0.1 | -13.9 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 2-7 | 22.2 | -11.9 | -39.1 |  |
| consensus_gap+money_delta | close | pin $2k+ | 2-0 | 100.0 | 42.0 | 87.8 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 2-2 | 50.0 | 9.9 | 32.7 |  |
| money_delta+pin_value | close | pin $2k+ | 2-1 | 66.7 | 8.7 | 25.2 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 2-1 | 66.7 | 24.6 | 74.9 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 1-0 | 100.0 | 42.0 | 84.7 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 4-1 | 80.0 | 33.2 | 53.8 |  |
| consensus_gap+money_level | close | pin limit <$1k | 4-1 | 80.0 | 23.5 | 50.5 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 3-2 | 60.0 | 13.2 | 15.6 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 6-2 | 75.0 | 23.4 | 41.8 |  |
| follow_move+money_level | close | pin limit <$1k | 8-12 | 40.0 | -12.0 | -23.6 |  |
| follow_move+money_moving | close | pin limit <$1k | 7-17 | 29.2 | -18.3 | -44.1 |  |
| follow_move+pin_value | close | pin limit <$1k | 7-3 | 70.0 | 15.9 | 32.9 |  |
| money_level+money_moving | close | pin limit <$1k | 9-13 | 40.9 | -10.9 | -22.4 |  |
| money_level+pin_value | close | pin limit <$1k | 11-4 | 73.3 | 17.6 | 38.8 |  |
| money_moving+pin_value | close | pin limit <$1k | 7-5 | 58.3 | 7.2 | 10.7 |  |
| follow_move+pin_move | close | pin limit <$1k | 8-13 | 38.1 | -10.0 | -26.6 |  |
| money_level+pin_move | close | pin limit <$1k | 10-9 | 52.6 | 0.8 | 0.1 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 13-23 | 36.1 | -11.4 | -30.9 |  |
| pin_move+pin_value | close | pin limit <$1k | 7-5 | 58.3 | 5.0 | 11.1 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 5-8 | 38.5 | -5.3 | -25.5 |  |
| money_moving+pin_move | close | pin limit <$1k | 7-11 | 38.9 | -8.4 | -25.7 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 2-0 | 100.0 | 61.2 | 95.5 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 2-1 | 66.7 | 26.3 | 30.3 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 1-1 | 50.0 | 11.2 | 0.0 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 3-0 | 100.0 | 59.6 | 93.9 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 2-0 | 100.0 | 61.2 | 95.5 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 3-1 | 75.0 | 30.6 | 44.5 |  |
| follow_move+money_delta | close | pin limit <$1k | 4-8 | 33.3 | -10.5 | -35.6 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 3-7 | 30.0 | -12.5 | -41.4 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 5-10 | 33.3 | -10.4 | -35.7 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 7-16 | 30.4 | -16.6 | -41.7 |  |
| money_delta+money_moving | close | pin limit <$1k | 7-9 | 43.8 | 0.0 | -15.4 |  |
| money_delta+pin_move | close | pin limit <$1k | 2-6 | 25.0 | -17.3 | -50.6 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 2-5 | 28.6 | -13.6 | -43.5 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 2-2 | 50.0 | 8.9 | -2.3 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 4-7 | 36.4 | -7.5 | -29.7 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 7-9 | 43.8 | 0.0 | -15.4 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 3-8 | 27.3 | -15.4 | -46.7 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 2-5 | 28.6 | -13.6 | -44.2 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 5-10 | 33.3 | -10.4 | -35.7 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 3-8 | 27.3 | -15.4 | -46.7 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 3-4 | 42.9 | -1.1 | -16.9 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 3-7 | 30.0 | -12.5 | -41.4 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 5-11 | 31.2 | -14.9 | -40.0 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 1-3 | 25.0 | -16.1 | -50.0 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 3-7 | 30.0 | -12.5 | -41.4 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 3-8 | 27.3 | -15.4 | -46.7 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 2-5 | 28.6 | -13.6 | -44.2 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 2-5 | 28.6 | -13.6 | -44.2 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 5-10 | 33.3 | -10.4 | -35.7 |  |
| money_delta+pin_value | close | pin limit <$1k | 4-0 | 100.0 | 53.3 | 91.0 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 2-0 | 100.0 | 56.5 | 90.9 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 6-4 | 60.0 | 10.0 | 13.8 |  |
| money_level+sharp_gap | close | pin limit <$1k | 7-12 | 36.8 | -14.2 | -30.1 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 0-1 | 0.0 | -43.5 | -100.0 |  |
| money_delta+money_level | close | pin limit <$1k | 1-4 | 20.0 | -23.5 | -61.0 |  |
| money_level+pin_rlm | close | pin limit <$1k | 2-3 | 40.0 | -3.5 | -22.8 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 2-4 | 33.3 | -10.1 | -35.7 |  |
| rlm_quiet | early | <1k bets | 9-15 | 37.5 | -0.5 | -15.0 | 0.72 |
| rlm_quiet | early | pin $1-2k | 1-1 | 50.0 | 15.9 | 16.0 | 1.15 |
| rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -43.5 | -100.0 | 0.0 |
| pin_move | early | <1k bets | 4-5 | 44.4 | -6.0 | -15.2 | 0.11 |
| pin_move | early | pin $1-2k | 0-2 | 0.0 | -42.0 | -100.0 | 0.0 |
| pin_move | early | pin limit <$1k | 4-3 | 57.1 | 4.3 | 9.1 | 0.14 |
| money_delta | early | <1k bets | 1-2 | 33.3 | -7.0 | -36.4 | 1.6 |
| money_delta | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| pin_rlm | early | <1k bets | 0-1 | 0.0 | -65.9 | -100.0 | 1.5 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -65.9 | -100.0 | 1.5 |
| follow_move | early | <1k bets | 87-100 | 46.5 | -2.0 | -11.0 | 0.05 |
| follow_move | early | pin $1-2k | 9-8 | 52.9 | 8.1 | 7.6 | -0.06 |
| follow_move | early | pin limit <$1k | 6-8 | 42.9 | -2.2 | -11.2 | -0.45 |
| rlm_ratio | early | <1k bets | 5-8 | 38.5 | -4.3 | -20.0 | 0.55 |
| rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -65.9 | -100.0 | 1.5 |
| rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| money_level | early | <1k bets | 32-24 | 57.1 | -2.8 | -8.0 | -0.1 |
| money_level | early | pin $1-2k | 1-2 | 33.3 | -32.5 | -44.4 | -0.23 |
| money_level | early | pin limit <$1k | 2-2 | 50.0 | -3.3 | -4.5 | 1.25 |
| sharp_gap | early | <1k bets | 20-29 | 40.8 | -7.6 | -21.4 | 0.43 |
| sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -32.5 | -44.4 | -0.23 |
| sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | 3.3 | -4.5 | 0.75 |
| money_moving | early | <1k bets | 20-24 | 45.5 | -2.8 | -14.3 | 0.33 |
| money_moving | early | pin $1-2k | 0-1 | 0.0 | -65.9 | -100.0 | 1.7 |
| money_moving | early | pin limit <$1k | 2-1 | 66.7 | 23.2 | 27.3 | 0.0 |
| pin_value | early | <1k bets | 11-10 | 52.4 | 3.3 | -1.3 | -0.16 |
| pin_value | early | pin $1-2k | 3-7 | 30.0 | -16.0 | -43.9 | -0.03 |
| pin_value | early | pin limit <$1k | 8-3 | 72.7 | 20.8 | 37.5 | -0.27 |
| consensus_gap | early | <1k bets | 54-36 | 60.0 | 8.7 | 8.7 | 0.48 |
| consensus_gap | early | pin $1-2k | 6-3 | 66.7 | 17.6 | 19.3 | -0.9 |
| consensus_gap | early | pin limit <$1k | 4-1 | 80.0 | 28.7 | 51.9 | 0.6 |
| follow_move+money_level | early | <1k bets | 11-9 | 55.0 | -5.4 | -18.2 | 0.67 |
| follow_move+sharp_gap | early | <1k bets | 9-13 | 40.9 | -7.1 | -19.8 | 1.05 |
| money_level+sharp_gap | early | <1k bets | 12-14 | 46.2 | -11.3 | -17.9 | 0.28 |
| follow_move+money_moving | early | <1k bets | 10-11 | 47.6 | -0.5 | -11.0 | 0.64 |
| money_level+money_moving | early | <1k bets | 11-10 | 52.4 | -5.5 | -11.7 | 0.32 |
| consensus_gap+money_level | early | <1k bets | 11-5 | 68.8 | 9.4 | 2.1 | -0.45 |
| follow_move+rlm_quiet | early | <1k bets | 9-15 | 37.5 | -0.5 | -15.0 | 0.72 |
| follow_move+rlm_ratio | early | <1k bets | 5-8 | 38.5 | -4.3 | -20.0 | 0.55 |
| rlm_quiet+rlm_ratio | early | <1k bets | 4-5 | 44.4 | 6.2 | -5.7 | -0.27 |
| rlm_quiet+sharp_gap | early | <1k bets | 4-6 | 40.0 | 1.2 | -15.1 | -0.24 |
| rlm_ratio+sharp_gap | early | <1k bets | 5-8 | 38.5 | -4.3 | -20.0 | 0.55 |
| consensus_gap+follow_move | early | <1k bets | 6-5 | 54.5 | 2.6 | -9.2 | 0.74 |
| money_moving+rlm_quiet | early | <1k bets | 5-5 | 50.0 | 11.2 | 13.7 | 0.6 |
| money_moving+rlm_ratio | early | <1k bets | 5-4 | 55.6 | 13.6 | 15.5 | 1.1 |
| money_moving+sharp_gap | early | <1k bets | 13-16 | 44.8 | -2.5 | -10.0 | 0.59 |
| consensus_gap+money_moving | early | <1k bets | 4-3 | 57.1 | 8.1 | -11.9 | 0.74 |
| consensus_gap+sharp_gap | early | <1k bets | 5-4 | 55.6 | 7.3 | -1.8 | -0.06 |
| money_level+rlm_ratio | early | <1k bets | 1-3 | 25.0 | -27.7 | -52.3 | 2.38 |
| follow_move+pin_move | early | <1k bets | 1-3 | 25.0 | -21.4 | -52.3 | 0.5 |
| follow_move+money_delta | early | <1k bets | 1-1 | 50.0 | 6.5 | -4.5 | 1.5 |
| money_delta+money_level | early | <1k bets | 1-1 | 50.0 | 6.5 | -4.5 | 1.5 |
| money_delta+money_moving | early | <1k bets | 1-2 | 33.3 | -7.0 | -36.4 | 1.6 |
| money_delta+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 6.5 | -4.5 | 1.5 |
| money_delta+sharp_gap | early | <1k bets | 1-2 | 33.3 | -7.0 | -36.4 | 1.6 |
| follow_move+pin_value | early | <1k bets | 3-3 | 50.0 | 4.8 | -4.5 | -0.83 |
| consensus_gap+pin_move | early | <1k bets | 1-0 | 100.0 | 43.5 | 90.9 | 0.0 |
| consensus_gap+pin_value | early | <1k bets | 5-1 | 83.3 | 33.6 | 57.8 | 0.0 |
| money_level+pin_move | early | <1k bets | 1-1 | 50.0 | -6.5 | -4.5 | 1.5 |
| money_level+pin_value | early | <1k bets | 2-2 | 50.0 | -5.6 | -4.5 | 1.43 |
| pin_move+pin_value | early | <1k bets | 2-4 | 33.3 | -18.4 | -36.4 | 0.17 |
| money_moving+pin_value | early | <1k bets | 1-1 | 50.0 | -4.7 | -4.5 | 1.35 |
| pin_value+sharp_gap | early | <1k bets | 1-2 | 33.3 | -22.0 | -36.4 | 1.9 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| consensus_gap+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| follow_move+pin_rlm | early | <1k bets | 0-1 | 0.0 | -65.9 | -100.0 | 1.5 |
| money_level+pin_rlm | early | <1k bets | 0-1 | 0.0 | -65.9 | -100.0 | 1.5 |
| pin_rlm+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -65.9 | -100.0 | 1.5 |
| pin_rlm+sharp_gap | early | <1k bets | 0-1 | 0.0 | -65.9 | -100.0 | 1.5 |
| pin_move+sharp_gap | early | <1k bets | 0-1 | 0.0 | -56.5 | -100.0 | 3.0 |
| pin_move+pin_value | early | pin $1-2k | 0-2 | 0.0 | -42.0 | -100.0 | 0.0 |
| follow_move+rlm_quiet | early | pin $1-2k | 1-1 | 50.0 | 15.9 | 16.0 | 1.15 |
| money_level+money_moving | early | pin $1-2k | 0-1 | 0.0 | -65.9 | -100.0 | 1.7 |
| money_level+pin_value | early | pin $1-2k | 0-1 | 0.0 | -65.9 | -100.0 | 1.7 |
| money_level+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -32.5 | -44.4 | -0.23 |
| money_moving+pin_value | early | pin $1-2k | 0-1 | 0.0 | -65.9 | -100.0 | 1.7 |
| money_moving+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -65.9 | -100.0 | 1.7 |
| pin_value+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -65.9 | -100.0 | 1.7 |
| consensus_gap+pin_value | early | pin $1-2k | 2-1 | 66.7 | 19.3 | 24.7 | -0.67 |
| follow_move+money_level | early | pin $1-2k | 0-1 | 0.0 | -65.9 | -100.0 | 1.5 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -65.9 | -100.0 | 1.5 |
| follow_move+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -65.9 | -100.0 | 1.5 |
| follow_move+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -65.9 | -100.0 | 1.5 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -65.9 | -100.0 | 1.5 |
| money_level+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -65.9 | -100.0 | 1.5 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -65.9 | -100.0 | 1.5 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -65.9 | -100.0 | 1.5 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -65.9 | -100.0 | 1.5 |
| consensus_gap+follow_move | early | pin $1-2k | 1-0 | 100.0 | 65.9 | 106.0 | 1.5 |
| follow_move+pin_move | early | pin $1-2k | 0-1 | 0.0 | -42.0 | -100.0 | 0.0 |
| follow_move+pin_value | early | pin $1-2k | 0-1 | 0.0 | -42.0 | -100.0 | 0.0 |
| consensus_gap+money_level | early | pin $1-2k | 1-0 | 100.0 | 34.1 | 66.7 | -3.9 |
| consensus_gap+sharp_gap | early | pin $1-2k | 1-0 | 100.0 | 34.1 | 66.7 | -3.9 |
| follow_move+pin_move | early | pin limit <$1k | 1-2 | 33.3 | -14.5 | -36.4 | 0.67 |
| follow_move+pin_value | early | pin limit <$1k | 3-2 | 60.0 | 14.2 | 14.5 | -1.0 |
| consensus_gap+money_level | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 90.9 | 0.5 |
| consensus_gap+pin_move | early | pin limit <$1k | 1-0 | 100.0 | 43.5 | 90.9 | 0.0 |
| consensus_gap+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 47.8 | 90.9 | 0.67 |
| follow_move+money_moving | early | pin limit <$1k | 1-1 | 50.0 | 6.5 | -4.5 | 0.5 |
| follow_move+rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -43.5 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 6.5 | -4.5 | 0.5 |
| money_level+pin_move | early | pin limit <$1k | 1-1 | 50.0 | -6.5 | -4.5 | 1.5 |
| money_level+pin_value | early | pin limit <$1k | 2-1 | 66.7 | 14.5 | 27.3 | 1.33 |
| money_moving+rlm_quiet | early | pin limit <$1k | 0-1 | 0.0 | -43.5 | -100.0 | 0.0 |
| money_moving+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 23.2 | 27.3 | 0.0 |
| pin_move+pin_value | early | pin limit <$1k | 2-2 | 50.0 | -6.5 | -4.5 | 0.25 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -43.5 | -100.0 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| consensus_gap+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| follow_move+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| follow_move+money_level | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| follow_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| money_delta+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| money_delta+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| money_delta+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| money_level+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| money_level+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| money_level+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 | 2.0 |
| money_moving+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| pin_value+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 | 2.0 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 56.5 | 90.9 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -56.5 | -100.0 | 3.0 |
