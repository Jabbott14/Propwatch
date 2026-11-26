# CBB scorecard

Generated 2026-11-26 03:48 UTC. 958 graded games (37 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**684 games before 2026-11-21 (fit) · 274 on or after it (forward).**

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
sample ran **47.0% favourites** (n=957) and **50.4% overs** (n=958) and **71.4% moneyline favourites** (n=837).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-21. Nothing in the engine was chosen using these. n=274 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 26-32 | 44.8 | 38.6 | 6.2 | +4.11 | 7.1 | 0.82 | 48.3 | no edge shown yet |
| pin_move | both | 6-11 | 35.3 | 48.7 | -13.4 | -5.47 | -32.2 | 0.18 | 29.4 | keep collecting (17/30) |
| money_delta | both | 4-5 | 44.4 | 37.9 | 6.5 | +1.47 | 16.3 | 3.02 | 100.0 | keep collecting (9/30) |
| pin_rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | keep collecting (2/30) |
| follow_move | both | 219-240 | 47.7 | 48.8 | -1.1 | -41.74 | -9.1 | 0.01 | 37.5 | DROP: below break-even |
| rlm_ratio | both | 10-16 | 38.5 | 41.4 | -2.9 | -1.99 | -7.6 | 0.4 | 53.8 | keep collecting (26/30) |
| money_level | both | 72-61 | 54.1 | 57.5 | -3.3 | -17.44 | -13.1 | -0.39 | 36.1 | no edge shown yet |
| sharp_gap | both | 55-63 | 46.6 | 50.2 | -3.6 | -13.3 | -11.3 | 0.25 | 46.6 | no edge shown yet |
| money_moving | both | 45-43 | 51.1 | 49.1 | 2.0 | -2.65 | -3.0 | 0.62 | 51.1 | no edge shown yet |
| pin_value | both | 21-18 | 53.8 | 49.6 | 4.2 | +0.67 | 1.7 | 0.04 | 33.3 | no edge shown yet |
| consensus_gap | both | 135-118 | 53.4 | 52.9 | 0.4 | -17.24 | -6.8 | 0.54 | 49.8 | no edge shown yet |
| follow_move+money_level | both | 26-18 | 59.1 | 57.0 | 2.1 | -4.93 | -11.2 | 0.11 | 36.4 | no edge shown yet |
| follow_move+sharp_gap | both | 24-26 | 48.0 | 48.0 | -0.0 | -2.98 | -6.0 | 0.62 | 46.0 | no edge shown yet |
| money_level+sharp_gap | both | 37-37 | 50.0 | 55.8 | -5.8 | -12.24 | -16.5 | -0.17 | 41.9 | no edge shown yet |
| follow_move+money_moving | both | 19-19 | 50.0 | 47.7 | 2.3 | +0.13 | 0.4 | 0.67 | 44.7 | no edge shown yet |
| money_level+money_moving | both | 21-17 | 55.3 | 55.3 | 0.0 | -1.84 | -4.8 | 0.49 | 50.0 | no edge shown yet |
| consensus_gap+money_level | both | 24-17 | 58.5 | 61.6 | -3.0 | -5.2 | -12.7 | -0.54 | 31.7 | no edge shown yet |
| follow_move+rlm_quiet | both | 26-32 | 44.8 | 38.6 | 6.2 | +4.11 | 7.1 | 0.82 | 48.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 10-16 | 38.5 | 41.4 | -2.9 | -1.99 | -7.6 | 0.4 | 53.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | both | 9-10 | 47.4 | 39.2 | 8.2 | +3.1 | 16.3 | 0.32 | 47.4 | keep collecting (19/30) |
| rlm_quiet+sharp_gap | both | 10-12 | 45.5 | 40.4 | 5.1 | +2.01 | 9.2 | 0.5 | 45.5 | keep collecting (22/30) |
| rlm_ratio+sharp_gap | both | 10-16 | 38.5 | 41.4 | -2.9 | -1.99 | -7.6 | 0.4 | 53.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 17-19 | 47.2 | 55.1 | -7.9 | -7.68 | -21.3 | 0.82 | 58.3 | no edge shown yet |
| money_moving+rlm_quiet | both | 9-10 | 47.4 | 39.2 | 8.2 | +2.99 | 15.7 | 0.91 | 47.4 | keep collecting (19/30) |
| money_moving+rlm_ratio | both | 7-6 | 53.8 | 40.4 | 13.5 | +4.05 | 31.1 | 1.58 | 69.2 | keep collecting (13/30) |
| money_moving+sharp_gap | both | 24-28 | 46.2 | 47.0 | -0.9 | -2.41 | -4.6 | 0.93 | 57.7 | no edge shown yet |
| consensus_gap+money_moving | both | 10-5 | 66.7 | 55.1 | 11.6 | +0.97 | 6.5 | 1.23 | 60.0 | keep collecting (15/30) |
| consensus_gap+sharp_gap | both | 15-15 | 50.0 | 57.0 | -7.0 | -6.39 | -21.3 | -0.38 | 36.7 | no edge shown yet |
| money_level+rlm_ratio | both | 1-6 | 14.3 | 47.4 | -33.1 | -5.09 | -72.7 | 0.64 | 71.4 | keep collecting (7/30) |
| follow_move+pin_move | both | 2-6 | 25.0 | 46.3 | -21.3 | -4.15 | -51.9 | 0.12 | 25.0 | keep collecting (8/30) |
| follow_move+money_delta | both | 3-2 | 60.0 | 38.9 | 21.1 | +3.56 | 71.2 | 2.74 | 100.0 | keep collecting (5/30) |
| money_delta+money_level | both | 1-3 | 25.0 | 40.4 | -15.4 | -2.09 | -52.3 | 1.68 | 100.0 | keep collecting (4/30) |
| money_delta+money_moving | both | 4-5 | 44.4 | 37.9 | 6.5 | +1.47 | 16.3 | 3.02 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | both | 3-2 | 60.0 | 38.9 | 21.1 | +3.56 | 71.2 | 2.74 | 100.0 | keep collecting (5/30) |
| money_delta+sharp_gap | both | 4-5 | 44.4 | 37.9 | 6.5 | +1.47 | 16.3 | 3.02 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| follow_move+pin_value | both | 4-4 | 50.0 | 48.7 | 1.3 | -0.36 | -4.5 | -0.62 | 25.0 | keep collecting (8/30) |
| consensus_gap+pin_move | both | 2-1 | 66.7 | 51.7 | 15.0 | +0.86 | 28.7 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+pin_value | both | 10-3 | 76.9 | 49.2 | 27.8 | +5.9 | 45.4 | -0.15 | 30.8 | keep collecting (13/30) |
| money_level+pin_move | both | 2-4 | 33.3 | 47.8 | -14.4 | -2.15 | -35.8 | 0.17 | 16.7 | keep collecting (6/30) |
| money_level+pin_value | both | 3-3 | 50.0 | 53.9 | -3.9 | -0.27 | -4.5 | 0.78 | 50.0 | keep collecting (6/30) |
| pin_move+pin_value | both | 3-6 | 33.3 | 49.6 | -16.3 | -3.23 | -35.9 | 0.44 | 33.3 | keep collecting (9/30) |
| money_moving+pin_value | both | 3-2 | 60.0 | 53.1 | 6.9 | +0.77 | 15.4 | 1.14 | 100.0 | keep collecting (5/30) |
| pin_value+sharp_gap | both | 1-4 | 20.0 | 54.9 | -34.9 | -3.09 | -61.8 | 1.34 | 80.0 | keep collecting (5/30) |
| consensus_gap+money_delta | both | 1-0 | 100.0 | 47.8 | 52.2 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 1-0 | 100.0 | 47.8 | 52.2 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | both | 1-0 | 100.0 | 47.8 | 52.2 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+rlm_ratio | both | 1-0 | 100.0 | 47.8 | 52.2 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+sharp_gap | both | 0-3 | 0.0 | 45.8 | -45.8 | -3.0 | -100.0 | 1.0 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | both | 2-1 | 66.7 | 32.9 | 33.7 | +3.65 | 121.7 | 3.57 | 100.0 | keep collecting (3/30) |
| consensus_gap+rlm_quiet | both | 1-1 | 50.0 | 32.9 | 17.1 | +0.6 | 30.0 | 1.1 | 100.0 | keep collecting (2/30) |
| money_moving+pin_move | both | 1-1 | 50.0 | 47.8 | 2.2 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+pin_rlm | both | 0-1 | 0.0 | 32.9 | -32.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 0-1 | 0.0 | 32.9 | -32.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 15-21 | 41.7 | 32.9 | 8.7 | +5.11 | 14.2 | 0.87 | 44.4 | no edge shown yet |
| rlm_quiet | total | 11-11 | 50.0 | 47.8 | 2.2 | -1.0 | -4.5 | 0.73 | 54.5 | keep collecting (22/30) |
| pin_move | moneyline | 0-1 | 0.0 | 32.9 | -32.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move | spread | 1-3 | 25.0 | 47.4 | -22.4 | -2.06 | -51.4 | -0.25 | 0.0 | keep collecting (4/30) |
| pin_move | total | 5-7 | 41.7 | 50.4 | -8.7 | -2.41 | -20.1 | 0.33 | 41.7 | keep collecting (12/30) |
| money_delta | moneyline | 2-4 | 33.3 | 32.9 | 0.4 | +0.65 | 10.8 | 2.7 | 100.0 | keep collecting (6/30) |
| money_delta | total | 2-1 | 66.7 | 47.8 | 18.9 | +0.82 | 27.3 | 3.67 | 100.0 | keep collecting (3/30) |
| pin_rlm | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | keep collecting (2/30) |
| follow_move | moneyline | 92-83 | 52.6 | 47.0 | 5.6 | -1.43 | -0.8 | -0.3 | 34.3 | no edge shown yet |
| follow_move | spread | 49-63 | 43.8 | 50.6 | -6.9 | -17.56 | -15.7 | 0.03 | 29.5 | DROP: below break-even |
| follow_move | total | 78-94 | 45.3 | 49.5 | -4.2 | -22.76 | -13.2 | 0.31 | 45.9 | DROP: below break-even |
| rlm_ratio | moneyline | 4-10 | 28.6 | 35.4 | -6.8 | -1.44 | -10.3 | -0.25 | 35.7 | keep collecting (14/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 55.1 | -55.1 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| rlm_ratio | total | 6-5 | 54.5 | 47.8 | 6.7 | +0.45 | 4.1 | 0.82 | 72.7 | keep collecting (11/30) |
| money_level | moneyline | 37-31 | 54.4 | 63.0 | -8.6 | -19.29 | -28.4 | -0.48 | 35.3 | no edge shown yet |
| money_level | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.06 | -2.9 | 2.0 | 50.0 | keep collecting (2/30) |
| money_level | total | 34-29 | 54.0 | 51.7 | 2.3 | +1.9 | 3.0 | -0.37 | 36.5 | no edge shown yet |
| sharp_gap | moneyline | 24-35 | 40.7 | 50.3 | -9.6 | -13.48 | -22.9 | -0.03 | 47.5 | DROP: below break-even |
| sharp_gap | spread | 0-2 | 0.0 | 55.1 | -55.1 | -2.0 | -100.0 | 3.0 | 100.0 | keep collecting (2/30) |
| sharp_gap | total | 31-26 | 54.4 | 50.0 | 4.4 | +2.18 | 3.8 | 0.44 | 43.9 | no edge shown yet |
| money_moving | moneyline | 19-21 | 47.5 | 48.3 | -0.8 | -4.4 | -11.0 | 0.94 | 60.0 | no edge shown yet |
| money_moving | spread | 0-2 | 0.0 | 55.1 | -55.1 | -2.0 | -100.0 | 3.0 | 100.0 | keep collecting (2/30) |
| money_moving | total | 26-20 | 56.5 | 49.5 | 7.0 | +3.75 | 8.2 | 0.24 | 41.3 | no edge shown yet |
| pin_value | moneyline | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| pin_value | spread | 11-9 | 55.0 | 48.0 | 7.0 | +0.58 | 2.9 | 0.05 | 25.0 | keep collecting (20/30) |
| pin_value | total | 10-8 | 55.6 | 50.5 | 5.1 | +1.09 | 6.1 | -0.06 | 38.9 | keep collecting (18/30) |
| consensus_gap | moneyline | 66-57 | 53.7 | 56.8 | -3.1 | -17.52 | -14.2 | 0.44 | 49.6 | no edge shown yet |
| consensus_gap | spread | 29-18 | 61.7 | 48.2 | 13.6 | +7.18 | 15.3 | 0.23 | 34.0 | no edge shown yet |
| consensus_gap | total | 40-43 | 48.2 | 49.9 | -1.7 | -6.9 | -8.3 | 0.87 | 59.0 | no edge shown yet |
| consensus_gap+money_level | moneyline | 19-14 | 57.6 | 64.0 | -6.4 | -6.71 | -20.3 | -0.58 | 33.3 | no edge shown yet |
| follow_move+rlm_quiet | moneyline | 15-21 | 41.7 | 32.9 | 8.7 | +5.11 | 14.2 | 0.87 | 44.4 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 4-10 | 28.6 | 35.4 | -6.8 | -1.44 | -10.3 | -0.25 | 35.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 9-12 | 42.9 | 45.9 | -3.1 | -2.66 | -12.7 | 0.24 | 33.3 | keep collecting (21/30) |
| rlm_quiet+rlm_ratio | moneyline | 4-7 | 36.4 | 32.9 | 3.4 | +1.56 | 14.2 | 0.09 | 36.4 | keep collecting (11/30) |
| rlm_quiet+sharp_gap | moneyline | 4-7 | 36.4 | 32.9 | 3.4 | +1.56 | 14.2 | 0.09 | 36.4 | keep collecting (11/30) |
| rlm_ratio+sharp_gap | moneyline | 4-10 | 28.6 | 35.4 | -6.8 | -1.44 | -10.3 | -0.25 | 35.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 11-7 | 61.1 | 61.4 | -0.3 | -1.14 | -6.3 | 0.14 | 44.4 | keep collecting (18/30) |
| consensus_gap+money_moving | moneyline | 7-4 | 63.6 | 57.8 | 5.9 | -0.8 | -7.3 | 1.5 | 54.5 | keep collecting (11/30) |
| consensus_gap+sharp_gap | moneyline | 12-10 | 54.5 | 59.3 | -4.8 | -4.08 | -18.5 | -0.47 | 36.4 | keep collecting (22/30) |
| money_level+money_moving | moneyline | 8-8 | 50.0 | 60.7 | -10.7 | -4.74 | -29.6 | 1.11 | 56.2 | keep collecting (16/30) |
| money_level+sharp_gap | moneyline | 17-21 | 44.7 | 59.9 | -15.1 | -14.42 | -38.0 | -0.48 | 39.5 | INVERT candidate: wrong well beyond its base rate |
| money_moving+sharp_gap | moneyline | 7-16 | 30.4 | 43.3 | -12.9 | -5.94 | -25.8 | 1.45 | 73.9 | keep collecting (23/30) |
| follow_move+money_level | moneyline | 14-7 | 66.7 | 63.8 | 2.9 | -4.91 | -23.4 | -0.4 | 19.0 | keep collecting (21/30) |
| follow_move+money_moving | moneyline | 10-8 | 55.6 | 46.2 | 9.3 | +2.91 | 16.2 | 0.46 | 38.9 | keep collecting (18/30) |
| money_moving+rlm_quiet | moneyline | 5-6 | 45.5 | 32.9 | 12.5 | +3.35 | 30.5 | 1.3 | 54.5 | keep collecting (11/30) |
| money_moving+rlm_ratio | moneyline | 3-4 | 42.9 | 32.9 | 9.9 | +2.41 | 34.4 | 1.37 | 57.1 | keep collecting (7/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 67.1 | -67.1 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_rlm | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | moneyline | 0-3 | 0.0 | 44.3 | -44.3 | -3.0 | -100.0 | -1.5 | 33.3 | keep collecting (3/30) |
| pin_rlm+rlm_ratio | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+money_moving | moneyline | 2-4 | 33.3 | 32.9 | 0.4 | +0.65 | 10.8 | 2.7 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-4 | 33.3 | 32.9 | 0.4 | +0.65 | 10.8 | 2.7 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_level | moneyline | 0-2 | 0.0 | 32.9 | -32.9 | -2.0 | -100.0 | 1.85 | 100.0 | keep collecting (2/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 32.9 | 33.7 | +3.65 | 121.7 | 3.57 | 100.0 | keep collecting (3/30) |
| money_delta+rlm_quiet | moneyline | 2-1 | 66.7 | 32.9 | 33.7 | +3.65 | 121.7 | 3.57 | 100.0 | keep collecting (3/30) |
| money_delta+rlm_ratio | moneyline | 2-1 | 66.7 | 32.9 | 33.7 | +3.65 | 121.7 | 3.57 | 100.0 | keep collecting (3/30) |
| consensus_gap+rlm_quiet | moneyline | 1-1 | 50.0 | 32.9 | 17.1 | +0.6 | 30.0 | 1.1 | 100.0 | keep collecting (2/30) |
| follow_move+pin_move | moneyline | 0-1 | 0.0 | 32.9 | -32.9 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| money_level+pin_move | moneyline | 0-1 | 0.0 | 32.9 | -32.9 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| pin_move+pin_rlm | moneyline | 0-1 | 0.0 | 32.9 | -32.9 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| pin_move+rlm_ratio | moneyline | 0-1 | 0.0 | 32.9 | -32.9 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| pin_move+sharp_gap | moneyline | 0-1 | 0.0 | 32.9 | -32.9 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| follow_move+money_level | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.06 | -2.9 | 2.0 | 50.0 | redundant -- identical record to money_level alone, not independent confirmation |
| follow_move+money_moving | spread | 0-1 | 0.0 | 55.1 | -55.1 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 55.1 | -55.1 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 0-1 | 0.0 | 55.1 | -55.1 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level+money_moving | spread | 0-1 | 0.0 | 55.1 | -55.1 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level+rlm_ratio | spread | 0-1 | 0.0 | 55.1 | -55.1 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 0-1 | 0.0 | 55.1 | -55.1 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 55.1 | -55.1 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+sharp_gap | spread | 0-2 | 0.0 | 55.1 | -55.1 | -2.0 | -100.0 | 3.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 55.1 | -55.1 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 1-1 | 50.0 | 44.9 | 5.1 | -0.09 | -4.5 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | spread | 0-2 | 0.0 | 44.9 | -44.9 | -2.0 | -100.0 | 0.0 | 0.0 | keep collecting (2/30) |
| consensus_gap+pin_value | spread | 4-1 | 80.0 | 46.9 | 33.1 | +2.41 | 48.1 | -0.4 | 0.0 | keep collecting (5/30) |
| follow_move+pin_move | spread | 1-1 | 50.0 | 44.9 | 5.1 | -0.06 | -2.9 | -0.5 | 0.0 | keep collecting (2/30) |
| consensus_gap+pin_move | spread | 0-1 | 0.0 | 55.1 | -55.1 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | spread | 0-1 | 0.0 | 44.9 | -44.9 | -1.0 | -100.0 | 4.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_move | spread | 1-0 | 100.0 | 44.9 | 55.1 | +0.94 | 94.3 | -1.0 | 0.0 | keep collecting (1/30) |
| money_moving+pin_value | spread | 0-1 | 0.0 | 55.1 | -55.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | spread | 0-1 | 0.0 | 55.1 | -55.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| follow_move+money_level | total | 11-10 | 52.4 | 50.9 | 1.4 | +0.04 | 0.2 | 0.43 | 52.4 | keep collecting (21/30) |
| follow_move+sharp_gap | total | 15-13 | 53.6 | 49.4 | 4.2 | +0.68 | 2.4 | 0.75 | 53.6 | keep collecting (28/30) |
| money_level+sharp_gap | total | 20-15 | 57.1 | 51.3 | 5.8 | +3.18 | 9.1 | 0.03 | 42.9 | no edge shown yet |
| follow_move+money_moving | total | 9-10 | 47.4 | 48.7 | -1.4 | -1.78 | -9.3 | 0.63 | 47.4 | keep collecting (19/30) |
| money_level+money_moving | total | 13-8 | 61.9 | 51.1 | 10.8 | +3.89 | 18.5 | -0.19 | 42.9 | keep collecting (21/30) |
| follow_move+rlm_quiet | total | 11-11 | 50.0 | 47.8 | 2.2 | -1.0 | -4.5 | 0.73 | 54.5 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 6-5 | 54.5 | 47.8 | 6.7 | +0.45 | 4.1 | 0.82 | 72.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 5-3 | 62.5 | 47.8 | 14.7 | +1.55 | 19.3 | 0.62 | 62.5 | keep collecting (8/30) |
| rlm_quiet+sharp_gap | total | 6-5 | 54.5 | 47.8 | 6.7 | +0.45 | 4.1 | 0.91 | 54.5 | keep collecting (11/30) |
| rlm_ratio+sharp_gap | total | 6-5 | 54.5 | 47.8 | 6.7 | +0.45 | 4.1 | 0.82 | 72.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | total | 4-4 | 50.0 | 47.8 | 2.2 | -0.36 | -4.5 | 0.38 | 37.5 | keep collecting (8/30) |
| money_moving+rlm_ratio | total | 4-1 | 80.0 | 47.8 | 32.2 | +2.64 | 52.7 | 1.2 | 80.0 | keep collecting (5/30) |
| money_moving+sharp_gap | total | 17-10 | 63.0 | 49.6 | 13.4 | +5.53 | 20.5 | 0.33 | 40.7 | keep collecting (27/30) |
| follow_move+pin_move | total | 1-4 | 20.0 | 49.6 | -29.6 | -3.09 | -61.8 | 0.4 | 40.0 | keep collecting (5/30) |
| consensus_gap+follow_move | total | 6-11 | 35.3 | 49.1 | -13.8 | -5.55 | -32.6 | 1.35 | 70.6 | keep collecting (17/30) |
| consensus_gap+money_level | total | 5-3 | 62.5 | 51.6 | 10.9 | +1.51 | 18.8 | -0.38 | 25.0 | keep collecting (8/30) |
| consensus_gap+sharp_gap | total | 3-5 | 37.5 | 50.5 | -13.0 | -2.31 | -28.9 | -0.12 | 37.5 | keep collecting (8/30) |
| follow_move+money_delta | total | 1-1 | 50.0 | 47.8 | 2.2 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+money_level | total | 1-1 | 50.0 | 47.8 | 2.2 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+money_moving | total | 2-1 | 66.7 | 47.8 | 18.9 | +0.82 | 27.3 | 3.67 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | total | 1-1 | 50.0 | 47.8 | 2.2 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 2-1 | 66.7 | 47.8 | 18.9 | +0.82 | 27.3 | 3.67 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+rlm_ratio | total | 1-2 | 33.3 | 47.8 | -14.5 | -1.09 | -36.4 | 1.33 | 100.0 | keep collecting (3/30) |
| follow_move+pin_value | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.27 | -4.5 | -0.67 | 33.3 | keep collecting (6/30) |
| consensus_gap+pin_move | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | 0.5 | 50.0 | keep collecting (2/30) |
| consensus_gap+pin_value | total | 6-2 | 75.0 | 50.5 | 24.5 | +3.5 | 43.7 | 0.0 | 50.0 | keep collecting (8/30) |
| money_level+pin_move | total | 1-3 | 25.0 | 52.2 | -27.2 | -2.09 | -52.3 | 0.5 | 25.0 | keep collecting (4/30) |
| money_level+pin_value | total | 3-2 | 60.0 | 51.3 | 8.7 | +0.73 | 14.5 | 0.6 | 40.0 | keep collecting (5/30) |
| pin_move+pin_value | total | 3-4 | 42.9 | 50.9 | -8.1 | -1.23 | -17.6 | 0.57 | 42.9 | keep collecting (7/30) |
| consensus_gap+money_delta | total | 1-0 | 100.0 | 47.8 | 52.2 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_moving | total | 3-1 | 75.0 | 47.8 | 27.2 | +1.77 | 44.2 | 0.5 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 1-0 | 100.0 | 47.8 | 52.2 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | total | 1-0 | 100.0 | 47.8 | 52.2 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | total | 3-0 | 100.0 | 47.8 | 52.2 | +2.77 | 92.3 | 1.0 | 100.0 | keep collecting (3/30) |
| pin_value+rlm_ratio | total | 1-0 | 100.0 | 47.8 | 52.2 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | total | 1-2 | 33.3 | 50.7 | -17.4 | -1.09 | -36.4 | 1.33 | 66.7 | keep collecting (3/30) |
| pin_move+sharp_gap | total | 0-2 | 0.0 | 52.2 | -52.2 | -2.0 | -100.0 | 1.5 | 50.0 | keep collecting (2/30) |
| money_moving+pin_move | total | 1-1 | 50.0 | 47.8 | 2.2 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 108-167 | 39.3 | 43.0 | -3.7 | -36.94 | -13.4 |  |  | DROP: below break-even |
| pin_move | both | 195-212 | 47.9 | 49.5 | -1.5 | -23.83 | -5.9 |  |  | DROP: below break-even |
| money_delta | both | 99-115 | 46.3 | 44.4 | 1.9 | -11.51 | -5.4 |  |  | DROP: below break-even |
| pin_rlm | both | 41-60 | 40.6 | 42.3 | -1.7 | -14.28 | -14.1 |  |  | DROP: below break-even |
| follow_move | both | 313-348 | 47.4 | 49.2 | -1.9 | -64.0 | -9.7 |  |  | DROP: below break-even |
| rlm_ratio | both | 69-107 | 39.2 | 42.6 | -3.4 | -31.71 | -18.0 |  |  | DROP: below break-even |
| money_level | both | 404-314 | 56.3 | 55.0 | 1.3 | -31.89 | -4.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 312-360 | 46.4 | 48.5 | -2.1 | -75.57 | -11.2 |  |  | DROP: below break-even |
| money_moving | both | 325-351 | 48.1 | 48.9 | -0.8 | -60.06 | -8.9 |  |  | DROP: below break-even |
| pin_value | both | 149-146 | 50.5 | 49.7 | 0.8 | +1.6 | 0.5 |  |  | no edge shown yet |
| consensus_gap | both | 130-103 | 55.8 | 52.5 | 3.3 | +2.4 | 1.0 |  |  | no edge shown yet |
| follow_move+pin_move | both | 131-168 | 43.8 | 49.0 | -5.2 | -45.38 | -15.2 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 74-88 | 45.7 | 42.9 | 2.7 | -7.57 | -4.7 |  |  | DROP: below break-even |
| money_delta+sharp_gap | both | 74-87 | 46.0 | 42.9 | 3.1 | -6.57 | -4.1 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 303-339 | 47.2 | 48.6 | -1.4 | -60.46 | -9.4 |  |  | DROP: below break-even |
| consensus_gap+money_level | both | 85-53 | 61.6 | 58.3 | 3.3 | -2.56 | -1.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+rlm_quiet | both | 108-167 | 39.3 | 43.0 | -3.7 | -36.94 | -13.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | both | 52-78 | 40.0 | 44.2 | -4.2 | -18.14 | -14.0 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 35-35 | 50.0 | 51.0 | -1.0 | -7.91 | -11.3 |  |  | no edge shown yet |
| follow_move+money_level | both | 152-125 | 54.9 | 55.2 | -0.3 | -19.41 | -7.0 |  |  | no edge shown yet |
| money_level+money_moving | both | 220-196 | 52.9 | 52.8 | 0.1 | -23.7 | -5.7 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 208-197 | 51.4 | 52.5 | -1.2 | -30.66 | -7.6 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 44-52 | 45.8 | 50.6 | -4.7 | -12.1 | -12.6 |  |  | no edge shown yet |
| consensus_gap+pin_move | both | 37-23 | 61.7 | 50.4 | 11.3 | +14.92 | 24.9 |  |  | no edge shown yet |
| consensus_gap+pin_value | both | 43-40 | 51.8 | 49.4 | 2.4 | +2.09 | 2.5 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | both | 44-56 | 44.0 | 50.0 | -6.0 | -15.96 | -16.0 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 162-187 | 46.4 | 48.5 | -2.0 | -40.9 | -11.7 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 48-45 | 51.6 | 50.1 | 1.5 | +7.78 | 8.4 |  |  | no edge shown yet |
| follow_move+sharp_gap | both | 158-190 | 45.4 | 48.2 | -2.8 | -43.61 | -12.5 |  |  | DROP: below break-even |
| money_level+pin_move | both | 89-83 | 51.7 | 53.6 | -1.8 | -13.59 | -7.9 |  |  | no edge shown yet |
| money_level+pin_value | both | 67-66 | 50.4 | 50.6 | -0.3 | -7.39 | -5.6 |  |  | no edge shown yet |
| money_moving+pin_move | both | 93-103 | 47.4 | 48.6 | -1.1 | -16.36 | -8.3 |  |  | no edge shown yet |
| money_moving+pin_value | both | 57-67 | 46.0 | 49.7 | -3.8 | -12.85 | -10.4 |  |  | no edge shown yet |
| pin_move+pin_value | both | 61-65 | 48.4 | 50.9 | -2.5 | -10.41 | -8.3 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 88-109 | 44.7 | 48.1 | -3.5 | -25.48 | -12.9 |  |  | DROP: below break-even |
| pin_value+sharp_gap | both | 56-71 | 44.1 | 50.0 | -5.9 | -17.75 | -14.0 |  |  | DROP: below break-even |
| follow_move+money_delta | both | 51-73 | 41.1 | 44.4 | -3.3 | -21.85 | -17.6 |  |  | DROP: below break-even |
| money_delta+pin_move | both | 31-39 | 44.3 | 44.8 | -0.5 | -9.01 | -12.9 |  |  | no edge shown yet |
| money_delta+rlm_quiet | both | 29-49 | 37.2 | 42.2 | -5.0 | -18.07 | -23.2 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | both | 69-107 | 39.2 | 42.6 | -3.4 | -31.71 | -18.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | both | 50-85 | 37.0 | 41.9 | -4.9 | -27.7 | -20.5 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 67-101 | 39.9 | 42.8 | -2.9 | -28.34 | -16.9 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 36-76 | 32.1 | 40.6 | -8.5 | -32.22 | -28.8 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | both | 50-87 | 36.5 | 41.9 | -5.4 | -29.6 | -21.6 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 69-107 | 39.2 | 42.6 | -3.4 | -31.71 | -18.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | both | 26-24 | 52.0 | 47.6 | 4.4 | +1.44 | 2.9 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 9-17 | 34.6 | 40.0 | -5.3 | -6.72 | -25.9 |  |  | keep collecting (26/30) |
| consensus_gap+rlm_ratio | both | 8-11 | 42.1 | 40.4 | 1.7 | -1.75 | -9.2 |  |  | keep collecting (19/30) |
| money_delta+rlm_ratio | both | 34-55 | 38.2 | 42.5 | -4.3 | -19.44 | -21.8 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 7-7 | 50.0 | 44.0 | 6.0 | +1.58 | 11.3 |  |  | keep collecting (14/30) |
| money_level+pin_rlm | both | 13-15 | 46.4 | 46.4 | 0.0 | -2.66 | -9.5 |  |  | keep collecting (28/30) |
| money_moving+pin_rlm | both | 41-54 | 43.2 | 42.8 | 0.4 | -8.28 | -8.7 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 41-60 | 40.6 | 42.3 | -1.7 | -14.28 | -14.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | both | 26-24 | 52.0 | 46.8 | 5.2 | +0.34 | 0.7 |  |  | no edge shown yet |
| consensus_gap+money_delta | both | 14-9 | 60.9 | 43.5 | 17.4 | +7.9 | 34.3 |  |  | keep collecting (23/30) |
| follow_move+pin_rlm | both | 34-52 | 39.5 | 42.0 | -2.5 | -13.35 | -15.5 |  |  | DROP: below break-even |
| money_delta+pin_rlm | both | 21-30 | 41.2 | 42.4 | -1.2 | -8.67 | -17.0 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 38-52 | 42.2 | 43.1 | -0.9 | -10.36 | -11.5 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | both | 34-49 | 41.0 | 43.4 | -2.4 | -11.82 | -14.2 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 19-38 | 33.3 | 40.4 | -7.1 | -13.8 | -24.2 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | both | 34-52 | 39.5 | 42.0 | -2.5 | -13.35 | -15.5 |  |  | DROP: below break-even |
| money_delta+pin_value | both | 21-10 | 67.7 | 48.5 | 19.3 | +13.02 | 42.0 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_value+rlm_quiet | both | 13-16 | 44.8 | 47.9 | -3.1 | +6.0 | 20.7 |  |  | keep collecting (29/30) |
| pin_value+rlm_ratio | both | 7-7 | 50.0 | 48.2 | 1.8 | -0.31 | -2.2 |  |  | keep collecting (14/30) |
| pin_rlm+pin_value | both | 8-9 | 47.1 | 49.2 | -2.1 | -1.33 | -7.8 |  |  | keep collecting (17/30) |
| rlm_quiet | moneyline | 39-76 | 33.9 | 33.5 | 0.4 | -10.38 | -9.0 |  |  | DROP: below break-even |
| rlm_quiet | spread | 22-26 | 45.8 | 53.6 | -7.8 | -5.32 | -11.1 |  |  | no edge shown yet |
| rlm_quiet | total | 47-65 | 42.0 | 48.1 | -6.1 | -21.24 | -19.0 |  |  | DROP: below break-even |
| pin_move | moneyline | 58-50 | 53.7 | 46.5 | 7.2 | +13.45 | 12.5 |  |  | no edge shown yet |
| pin_move | spread | 65-72 | 47.4 | 51.5 | -4.0 | -13.16 | -9.6 |  |  | no edge shown yet |
| pin_move | total | 72-90 | 44.4 | 49.7 | -5.3 | -24.12 | -14.9 |  |  | DROP: below break-even |
| money_delta | moneyline | 27-46 | 37.0 | 35.7 | 1.2 | -8.77 | -12.0 |  |  | DROP: below break-even |
| money_delta | spread | 19-17 | 52.8 | 50.9 | 1.9 | +0.46 | 1.3 |  |  | no edge shown yet |
| money_delta | total | 53-52 | 50.5 | 48.1 | 2.3 | -3.2 | -3.0 |  |  | no edge shown yet |
| pin_rlm | moneyline | 16-30 | 34.8 | 34.4 | 0.4 | -7.12 | -15.5 |  |  | DROP: below break-even |
| pin_rlm | spread | 5-3 | 62.5 | 51.3 | 11.2 | +1.51 | 18.9 |  |  | keep collecting (8/30) |
| pin_rlm | total | 20-27 | 42.6 | 48.6 | -6.0 | -8.68 | -18.5 |  |  | no edge shown yet |
| follow_move | moneyline | 112-120 | 48.3 | 47.6 | 0.6 | -20.51 | -8.8 |  |  | no edge shown yet |
| follow_move | spread | 88-95 | 48.1 | 50.9 | -2.8 | -14.13 | -7.7 |  |  | no edge shown yet |
| follow_move | total | 113-133 | 45.9 | 49.5 | -3.5 | -29.36 | -11.9 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 24-52 | 31.6 | 33.8 | -2.3 | -17.8 | -23.4 |  |  | DROP: below break-even |
| rlm_ratio | spread | 11-9 | 55.0 | 52.0 | 3.0 | +0.89 | 4.4 |  |  | keep collecting (20/30) |
| rlm_ratio | total | 34-46 | 42.5 | 48.6 | -6.1 | -14.79 | -18.5 |  |  | DROP: below break-even |
| money_level | moneyline | 163-90 | 64.4 | 63.8 | 0.6 | -24.74 | -9.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 100-93 | 51.8 | 48.6 | 3.2 | -3.3 | -1.7 |  |  | no edge shown yet |
| money_level | total | 141-131 | 51.8 | 51.3 | 0.5 | -3.85 | -1.4 |  |  | no edge shown yet |
| sharp_gap | moneyline | 96-129 | 42.7 | 45.7 | -3.0 | -40.3 | -17.9 |  |  | DROP: below break-even |
| sharp_gap | spread | 98-95 | 50.8 | 49.5 | 1.2 | -6.69 | -3.5 |  |  | no edge shown yet |
| sharp_gap | total | 118-136 | 46.5 | 50.2 | -3.7 | -28.57 | -11.2 |  |  | DROP: below break-even |
| money_moving | moneyline | 105-118 | 47.1 | 46.9 | 0.2 | -26.4 | -11.8 |  |  | DROP: below break-even |
| money_moving | spread | 98-95 | 50.8 | 49.5 | 1.2 | -6.69 | -3.5 |  |  | no edge shown yet |
| money_moving | total | 122-138 | 46.9 | 50.2 | -3.3 | -26.97 | -10.4 |  |  | DROP: below break-even |
| pin_value | moneyline | 7-13 | 35.0 | 44.9 | -9.9 | +9.11 | 45.6 |  |  | keep collecting (20/30) |
| pin_value | spread | 71-61 | 53.8 | 49.6 | 4.2 | +0.48 | 0.4 |  |  | no edge shown yet |
| pin_value | total | 71-72 | 49.7 | 50.4 | -0.8 | -8.0 | -5.6 |  |  | no edge shown yet |
| consensus_gap | moneyline | 68-52 | 56.7 | 54.8 | 1.8 | -1.16 | -1.0 |  |  | no edge shown yet |
| consensus_gap | spread | 27-21 | 56.2 | 48.9 | 7.3 | +2.38 | 5.0 |  |  | no edge shown yet |
| consensus_gap | total | 35-30 | 53.8 | 50.9 | 2.9 | +1.18 | 1.8 |  |  | no edge shown yet |
| consensus_gap+money_level | moneyline | 52-23 | 69.3 | 64.8 | 4.5 | -1.5 | -2.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+pin_move | moneyline | 42-45 | 48.3 | 45.9 | 2.4 | -3.91 | -4.5 |  |  | no edge shown yet |
| follow_move+rlm_quiet | moneyline | 39-76 | 33.9 | 33.5 | 0.4 | -10.38 | -9.0 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | moneyline | 19-29 | 39.6 | 33.7 | 5.9 | +0.03 | 0.1 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 20-18 | 52.6 | 51.8 | 0.8 | -4.36 | -11.5 |  |  | no edge shown yet |
| follow_move+money_level | moneyline | 64-39 | 62.1 | 63.1 | -0.9 | -13.39 | -13.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 91-113 | 44.6 | 45.8 | -1.2 | -26.52 | -13.0 |  |  | DROP: below break-even |
| follow_move+money_moving | moneyline | 57-68 | 45.6 | 45.5 | 0.1 | -17.75 | -14.2 |  |  | DROP: below break-even |
| follow_move+sharp_gap | moneyline | 52-71 | 42.3 | 44.6 | -2.3 | -21.36 | -17.4 |  |  | DROP: below break-even |
| money_level+money_moving | moneyline | 67-44 | 60.4 | 60.3 | 0.1 | -9.47 | -8.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 59-47 | 55.7 | 59.7 | -4.0 | -14.87 | -14.0 |  |  | no edge shown yet |
| follow_move+rlm_ratio | moneyline | 24-52 | 31.6 | 33.8 | -2.3 | -17.8 | -23.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | moneyline | 20-42 | 32.3 | 32.9 | -0.7 | -12.48 | -20.1 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 23-48 | 32.4 | 33.9 | -1.5 | -15.52 | -21.9 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | moneyline | 17-41 | 29.3 | 32.9 | -3.6 | -14.72 | -25.4 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 20-43 | 31.7 | 32.9 | -1.2 | -13.34 | -21.2 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 24-52 | 31.6 | 33.8 | -2.3 | -17.8 | -23.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 21-25 | 45.7 | 50.7 | -5.1 | -5.48 | -11.9 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | moneyline | 3-12 | 20.0 | 32.9 | -12.9 | -7.22 | -48.1 |  |  | keep collecting (15/30) |
| consensus_gap+rlm_ratio | moneyline | 3-7 | 30.0 | 32.9 | -2.9 | -2.22 | -22.2 |  |  | keep collecting (10/30) |
| consensus_gap+sharp_gap | moneyline | 21-28 | 42.9 | 49.7 | -6.8 | -8.34 | -17.0 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 4-3 | 57.1 | 37.8 | 19.3 | +2.88 | 41.1 |  |  | keep collecting (7/30) |
| money_level+pin_rlm | moneyline | 3-5 | 37.5 | 41.5 | -4.0 | -1.8 | -22.5 |  |  | keep collecting (8/30) |
| money_moving+pin_rlm | moneyline | 16-25 | 39.0 | 34.6 | 4.4 | -2.12 | -5.2 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 16-30 | 34.8 | 34.4 | 0.4 | -7.12 | -15.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 4-6 | 40.0 | 43.2 | -3.2 | +1.84 | 18.4 |  |  | keep collecting (10/30) |
| money_level+rlm_ratio | moneyline | 4-9 | 30.8 | 38.2 | -7.4 | -4.66 | -35.9 |  |  | keep collecting (13/30) |
| consensus_gap+pin_move | moneyline | 21-5 | 80.8 | 50.0 | 30.8 | +18.81 | 72.4 |  |  | keep collecting (26/30) |
| money_level+pin_move | moneyline | 28-16 | 63.6 | 62.4 | 1.2 | -1.29 | -2.9 |  |  | no edge shown yet |
| consensus_gap+money_delta | moneyline | 5-6 | 45.5 | 36.0 | 9.4 | +2.83 | 25.7 |  |  | keep collecting (11/30) |
| follow_move+money_delta | moneyline | 15-30 | 33.3 | 36.7 | -3.4 | -11.89 | -26.4 |  |  | DROP: below break-even |
| follow_move+pin_rlm | moneyline | 13-25 | 34.2 | 33.8 | 0.4 | -5.58 | -14.7 |  |  | DROP: below break-even |
| money_delta+money_moving | moneyline | 25-43 | 36.8 | 34.9 | 1.8 | -7.51 | -11.0 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 9-11 | 45.0 | 34.6 | 10.4 | -1.14 | -5.7 |  |  | keep collecting (20/30) |
| money_delta+pin_rlm | moneyline | 9-14 | 39.1 | 34.4 | 4.7 | -3.72 | -16.2 |  |  | keep collecting (23/30) |
| money_delta+rlm_quiet | moneyline | 9-24 | 27.3 | 32.9 | -5.7 | -11.69 | -35.4 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | moneyline | 11-28 | 28.2 | 34.7 | -6.5 | -13.47 | -34.5 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 25-43 | 36.8 | 34.9 | 1.8 | -7.51 | -11.0 |  |  | DROP: below break-even |
| money_moving+pin_move | moneyline | 24-23 | 51.1 | 43.1 | 8.0 | +1.35 | 2.9 |  |  | no edge shown yet |
| pin_move+pin_rlm | moneyline | 13-22 | 37.1 | 33.9 | 3.2 | -3.2 | -9.1 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 10-21 | 32.3 | 34.0 | -1.8 | -5.66 | -18.3 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 22-28 | 44.0 | 41.8 | 2.2 | -4.04 | -8.1 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | moneyline | 10-20 | 33.3 | 32.9 | 0.4 | -4.08 | -13.6 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 13-25 | 34.2 | 33.8 | 0.4 | -5.58 | -14.7 |  |  | DROP: below break-even |
| follow_move+pin_value | moneyline | 3-3 | 50.0 | 50.0 | 0.0 | +9.55 | 159.1 |  |  | keep collecting (6/30) |
| pin_value+rlm_quiet | moneyline | 2-1 | 66.7 | 32.9 | 33.7 | +10.98 | 366.0 |  |  | keep collecting (3/30) |
| money_delta+money_level | moneyline | 7-4 | 63.6 | 45.3 | 18.3 | +4.11 | 37.4 |  |  | keep collecting (11/30) |
| money_level+pin_value | moneyline | 1-6 | 14.3 | 62.2 | -47.9 | -5.43 | -77.6 |  |  | keep collecting (7/30) |
| pin_move+pin_value | moneyline | 3-4 | 42.9 | 52.4 | -9.6 | -0.97 | -13.9 |  |  | keep collecting (7/30) |
| money_delta+pin_value | moneyline | 2-0 | 100.0 | 32.9 | 67.1 | +5.88 | 294.0 |  |  | keep collecting (2/30) |
| money_moving+pin_value | moneyline | 3-4 | 42.9 | 42.7 | 0.2 | +2.45 | 35.0 |  |  | keep collecting (7/30) |
| pin_value+sharp_gap | moneyline | 3-6 | 33.3 | 48.1 | -14.8 | +0.45 | 5.0 |  |  | keep collecting (9/30) |
| pin_rlm+pin_value | moneyline | 1-0 | 100.0 | 32.9 | 67.1 | +1.38 | 138.0 |  |  | keep collecting (1/30) |
| pin_value+rlm_ratio | moneyline | 1-0 | 100.0 | 32.9 | 67.1 | +1.38 | 138.0 |  |  | keep collecting (1/30) |
| follow_move+pin_move | spread | 38-51 | 42.7 | 51.3 | -8.6 | -16.29 | -18.3 |  |  | DROP: below break-even |
| money_moving+sharp_gap | spread | 98-95 | 50.8 | 49.5 | 1.2 | -6.69 | -3.5 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 22-26 | 45.8 | 53.6 | -7.8 | -5.32 | -11.1 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | spread | 73-68 | 51.8 | 48.7 | 3.0 | -2.55 | -1.8 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 73-68 | 51.8 | 48.7 | 3.0 | -2.55 | -1.8 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 12-18 | 40.0 | 53.7 | -13.7 | -6.75 | -22.5 |  |  | no edge shown yet |
| consensus_gap+pin_value | spread | 20-15 | 57.1 | 49.6 | 7.6 | +2.37 | 6.8 |  |  | no edge shown yet |
| follow_move+money_level | spread | 32-28 | 53.3 | 50.0 | 3.3 | +1.12 | 1.9 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 38-36 | 51.4 | 51.0 | 0.4 | -1.37 | -1.8 |  |  | no edge shown yet |
| follow_move+sharp_gap | spread | 38-36 | 51.4 | 51.0 | 0.4 | -1.37 | -1.8 |  |  | no edge shown yet |
| money_level+pin_move | spread | 23-25 | 47.9 | 50.0 | -2.1 | -4.67 | -9.7 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 29-29 | 50.0 | 50.9 | -0.9 | -3.14 | -5.4 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 29-29 | 50.0 | 50.9 | -0.9 | -3.14 | -5.4 |  |  | no edge shown yet |
| money_delta+money_level | spread | 7-5 | 58.3 | 47.4 | 10.9 | +1.27 | 10.6 |  |  | keep collecting (12/30) |
| money_delta+money_moving | spread | 13-12 | 52.0 | 49.8 | 2.2 | -0.24 | -1.0 |  |  | keep collecting (25/30) |
| money_delta+sharp_gap | spread | 13-12 | 52.0 | 49.8 | 2.2 | -0.24 | -1.0 |  |  | keep collecting (25/30) |
| consensus_gap+money_level | spread | 9-12 | 42.9 | 47.8 | -5.0 | -4.24 | -20.2 |  |  | keep collecting (21/30) |
| consensus_gap+money_moving | spread | 7-9 | 43.8 | 49.4 | -5.6 | -2.92 | -18.2 |  |  | keep collecting (16/30) |
| consensus_gap+sharp_gap | spread | 7-9 | 43.8 | 49.4 | -5.6 | -2.92 | -18.2 |  |  | keep collecting (16/30) |
| money_level+pin_value | spread | 28-25 | 52.8 | 48.0 | 4.9 | -0.96 | -1.8 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 26-29 | 47.3 | 49.5 | -2.3 | -6.52 | -11.9 |  |  | no edge shown yet |
| pin_value+sharp_gap | spread | 26-29 | 47.3 | 49.5 | -2.3 | -6.52 | -11.9 |  |  | no edge shown yet |
| follow_move+money_delta | spread | 8-6 | 57.1 | 52.2 | 5.0 | +1.21 | 8.7 |  |  | keep collecting (14/30) |
| follow_move+rlm_ratio | spread | 11-9 | 55.0 | 52.0 | 3.0 | +0.89 | 4.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | spread | 3-4 | 42.9 | 50.7 | -7.9 | -1.4 | -20.0 |  |  | keep collecting (7/30) |
| money_moving+rlm_ratio | spread | 11-9 | 55.0 | 52.0 | 3.0 | +0.89 | 4.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 11-9 | 55.0 | 52.0 | 3.0 | +0.89 | 4.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 18-15 | 54.5 | 50.5 | 4.1 | +0.79 | 2.4 |  |  | no edge shown yet |
| pin_move+pin_value | spread | 31-27 | 53.4 | 51.6 | 1.9 | +0.16 | 0.3 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 9-10 | 47.4 | 50.8 | -3.4 | -2.14 | -11.3 |  |  | keep collecting (19/30) |
| consensus_gap+follow_move | spread | 5-5 | 50.0 | 50.0 | -0.0 | -0.52 | -5.2 |  |  | keep collecting (10/30) |
| consensus_gap+rlm_quiet | spread | 2-0 | 100.0 | 55.1 | 44.9 | +1.82 | 90.9 |  |  | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 3-3 | 50.0 | 55.1 | -5.1 | -0.33 | -5.6 |  |  | keep collecting (6/30) |
| money_delta+rlm_quiet | spread | 4-3 | 57.1 | 55.1 | 2.0 | +0.78 | 11.1 |  |  | keep collecting (7/30) |
| money_moving+rlm_quiet | spread | 8-8 | 50.0 | 54.5 | -4.5 | -0.62 | -3.9 |  |  | keep collecting (16/30) |
| rlm_quiet+rlm_ratio | spread | 1-4 | 20.0 | 55.1 | -35.1 | -3.13 | -62.6 |  |  | keep collecting (5/30) |
| rlm_quiet+sharp_gap | spread | 8-8 | 50.0 | 54.5 | -4.5 | -0.62 | -3.9 |  |  | keep collecting (16/30) |
| consensus_gap+money_delta | spread | 3-1 | 75.0 | 55.1 | 19.9 | +1.63 | 40.8 |  |  | keep collecting (4/30) |
| money_delta+pin_move | spread | 7-4 | 63.6 | 52.3 | 11.3 | +2.19 | 19.9 |  |  | keep collecting (11/30) |
| money_delta+pin_value | spread | 6-3 | 66.7 | 52.8 | 13.8 | +2.32 | 25.8 |  |  | keep collecting (9/30) |
| money_moving+pin_rlm | spread | 5-3 | 62.5 | 51.3 | 11.2 | +1.51 | 18.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | spread | 5-3 | 62.5 | 51.3 | 11.2 | +1.51 | 18.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | spread | 3-1 | 75.0 | 55.1 | 19.9 | +1.7 | 42.4 |  |  | keep collecting (4/30) |
| pin_rlm+sharp_gap | spread | 5-3 | 62.5 | 51.3 | 11.2 | +1.51 | 18.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.76 | 87.8 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 9-2 | 81.8 | 51.4 | 30.4 | +6.11 | 55.5 |  |  | keep collecting (11/30) |
| pin_move+rlm_ratio | spread | 5-2 | 71.4 | 50.7 | 20.7 | +2.42 | 34.6 |  |  | keep collecting (7/30) |
| pin_value+rlm_ratio | spread | 1-0 | 100.0 | 55.1 | 44.9 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| follow_move+pin_rlm | spread | 2-2 | 50.0 | 47.4 | 2.6 | -0.18 | -4.5 |  |  | keep collecting (4/30) |
| money_delta+pin_rlm | spread | 3-2 | 60.0 | 53.1 | 6.9 | +0.7 | 13.9 |  |  | keep collecting (5/30) |
| pin_rlm+rlm_quiet | spread | 0-1 | 0.0 | 55.1 | -55.1 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+rlm_ratio | spread | 2-2 | 50.0 | 47.4 | 2.6 | -0.18 | -4.5 |  |  | keep collecting (4/30) |
| money_level+pin_rlm | spread | 2-2 | 50.0 | 47.4 | 2.6 | -0.18 | -4.5 |  |  | keep collecting (4/30) |
| consensus_gap+pin_rlm | spread | 2-1 | 66.7 | 51.7 | 15.0 | +0.79 | 26.2 |  |  | keep collecting (3/30) |
| money_delta+money_moving | total | 36-33 | 52.2 | 48.3 | 3.9 | +0.18 | 0.3 |  |  | no edge shown yet |
| money_delta+sharp_gap | total | 36-32 | 52.9 | 48.3 | 4.6 | +1.18 | 1.7 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 114-131 | 46.5 | 50.2 | -3.7 | -27.24 | -11.1 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | total | 47-65 | 42.0 | 48.1 | -6.1 | -21.24 | -19.0 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+follow_move | total | 10-12 | 45.5 | 50.2 | -4.7 | -3.04 | -13.8 |  |  | keep collecting (22/30) |
| consensus_gap+money_level | total | 24-18 | 57.1 | 52.1 | 5.1 | +3.17 | 7.6 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 16-18 | 47.1 | 50.9 | -3.8 | -3.7 | -10.9 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 7-8 | 46.7 | 50.4 | -3.8 | -1.75 | -11.7 |  |  | keep collecting (15/30) |
| consensus_gap+pin_value | total | 19-19 | 50.0 | 50.8 | -0.8 | -2.12 | -5.6 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 16-19 | 45.7 | 50.8 | -5.1 | -4.7 | -13.4 |  |  | no edge shown yet |
| follow_move+money_level | total | 56-58 | 49.1 | 50.8 | -1.6 | -7.14 | -6.3 |  |  | no edge shown yet |
| follow_move+money_moving | total | 67-83 | 44.7 | 49.7 | -5.0 | -21.78 | -14.5 |  |  | DROP: below break-even |
| follow_move+pin_move | total | 51-72 | 41.5 | 49.6 | -8.2 | -25.19 | -20.5 |  |  | DROP: below break-even |
| follow_move+pin_value | total | 27-27 | 50.0 | 49.9 | 0.1 | -2.56 | -4.7 |  |  | no edge shown yet |
| follow_move+sharp_gap | total | 68-83 | 45.0 | 49.7 | -4.7 | -20.88 | -13.8 |  |  | DROP: below break-even |
| money_level+money_moving | total | 80-84 | 48.8 | 51.1 | -2.4 | -11.68 | -7.1 |  |  | no edge shown yet |
| money_level+pin_move | total | 38-42 | 47.5 | 50.9 | -3.4 | -7.64 | -9.6 |  |  | no edge shown yet |
| money_level+pin_value | total | 38-35 | 52.1 | 51.5 | 0.6 | -1.0 | -1.4 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 76-82 | 48.1 | 51.2 | -3.1 | -13.24 | -8.4 |  |  | no edge shown yet |
| money_moving+pin_move | total | 40-51 | 44.0 | 49.9 | -6.0 | -14.57 | -16.0 |  |  | DROP: below break-even |
| money_moving+pin_value | total | 28-34 | 45.2 | 50.7 | -5.5 | -8.78 | -14.2 |  |  | no edge shown yet |
| pin_move+pin_value | total | 27-34 | 44.3 | 50.1 | -5.8 | -9.59 | -15.7 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 37-52 | 41.6 | 49.9 | -8.3 | -18.3 | -20.6 |  |  | DROP: below break-even |
| pin_value+sharp_gap | total | 27-36 | 42.9 | 50.7 | -7.8 | -11.68 | -18.5 |  |  | DROP: below break-even |
| follow_move+money_delta | total | 28-37 | 43.1 | 48.1 | -5.0 | -11.17 | -17.2 |  |  | DROP: below break-even |
| money_delta+pin_move | total | 15-24 | 38.5 | 47.9 | -9.5 | -10.06 | -25.8 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | total | 16-22 | 42.1 | 47.8 | -5.7 | -7.16 | -18.8 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 21-31 | 40.4 | 48.3 | -7.9 | -11.43 | -22.0 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | total | 34-46 | 42.5 | 48.6 | -6.1 | -14.79 | -18.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | total | 20-23 | 46.5 | 48.2 | -1.7 | -4.57 | -10.6 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 22-35 | 38.6 | 48.2 | -9.6 | -14.6 | -25.6 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | total | 33-44 | 42.9 | 48.7 | -5.8 | -13.7 | -17.8 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | total | 18-31 | 36.7 | 48.3 | -11.5 | -14.37 | -29.3 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | total | 22-36 | 37.9 | 48.2 | -10.3 | -15.65 | -27.0 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | total | 34-46 | 42.5 | 48.6 | -6.1 | -14.79 | -18.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | total | 6-2 | 75.0 | 47.8 | 27.2 | +3.44 | 43.0 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_quiet | total | 4-5 | 44.4 | 48.3 | -3.9 | -1.32 | -14.7 |  |  | keep collecting (9/30) |
| consensus_gap+rlm_ratio | total | 3-4 | 42.9 | 48.4 | -5.6 | -1.29 | -18.4 |  |  | keep collecting (7/30) |
| money_delta+pin_value | total | 13-7 | 65.0 | 48.0 | 17.0 | +4.82 | 24.1 |  |  | keep collecting (20/30) |
| pin_value+rlm_quiet | total | 8-12 | 40.0 | 48.0 | -8.0 | -4.64 | -23.2 |  |  | keep collecting (20/30) |
| pin_value+rlm_ratio | total | 5-7 | 41.7 | 48.9 | -7.2 | -2.53 | -21.1 |  |  | keep collecting (12/30) |
| follow_move+pin_rlm | total | 19-25 | 43.2 | 48.6 | -5.4 | -7.58 | -17.2 |  |  | no edge shown yet |
| money_delta+money_level | total | 12-15 | 44.4 | 48.6 | -4.2 | -3.94 | -14.6 |  |  | keep collecting (27/30) |
| money_delta+pin_rlm | total | 9-14 | 39.1 | 48.0 | -8.9 | -5.65 | -24.6 |  |  | keep collecting (23/30) |
| money_level+pin_rlm | total | 8-8 | 50.0 | 48.6 | 1.4 | -0.68 | -4.3 |  |  | keep collecting (16/30) |
| money_level+rlm_ratio | total | 13-13 | 50.0 | 49.2 | 0.8 | -1.11 | -4.3 |  |  | keep collecting (26/30) |
| money_moving+pin_rlm | total | 20-26 | 43.5 | 48.6 | -5.1 | -7.68 | -16.7 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 20-27 | 42.6 | 48.6 | -6.0 | -8.68 | -18.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 19-26 | 42.2 | 48.7 | -6.5 | -8.58 | -19.1 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 19-25 | 43.2 | 48.6 | -5.4 | -7.58 | -17.2 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 20-27 | 42.6 | 48.6 | -6.0 | -8.68 | -18.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | total | 9-17 | 34.6 | 48.5 | -13.9 | -8.72 | -33.5 |  |  | keep collecting (26/30) |
| consensus_gap+pin_rlm | total | 1-3 | 25.0 | 48.9 | -23.9 | -2.09 | -52.3 |  |  | keep collecting (4/30) |
| pin_rlm+pin_value | total | 4-8 | 33.3 | 48.5 | -15.2 | -4.4 | -36.7 |  |  | keep collecting (12/30) |

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
| rlm_quiet | both | 56-68 | 45.2 | 36.7 | 8.4 | +14.7 | 11.9 | 0.48 | 46.0 | DROP: below break-even |
| pin_move | both | 11-20 | 35.5 | 48.4 | -12.9 | -10.57 | -34.1 | 0.2 | 38.7 | DROP: below break-even |
| money_delta | both | 14-12 | 53.8 | 40.0 | 13.9 | +5.9 | 22.7 | 0.9 | 53.8 | keep collecting (26/30) |
| pin_rlm | both | 1-4 | 20.0 | 37.1 | -17.1 | -3.07 | -61.5 | -0.3 | 60.0 | keep collecting (5/30) |
| follow_move | both | 693-642 | 51.9 | 51.0 | 0.9 | -86.22 | -6.5 | 0.13 | 40.4 | no edge shown yet |
| rlm_ratio | both | 39-33 | 54.2 | 39.6 | 14.6 | +18.55 | 25.8 | 0.41 | 52.8 | no edge shown yet |
| money_level | both | 241-170 | 58.6 | 58.4 | 0.2 | -28.78 | -7.0 | -0.21 | 38.2 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 198-183 | 52.0 | 49.0 | 3.0 | +5.79 | 1.5 | 0.27 | 44.4 | no edge shown yet |
| money_moving | both | 147-123 | 54.4 | 50.5 | 4.0 | -1.46 | -0.5 | 0.23 | 44.8 | no edge shown yet |
| pin_value | both | 71-67 | 51.4 | 48.8 | 2.6 | -3.93 | -2.8 | 0.08 | 36.2 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.8 | -31.8 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 354-408 | 46.5 | 49.5 | -3.1 | -78.7 | -10.3 | 0.44 | 46.6 | DROP: below break-even |
| consensus_gap+money_level | both | 56-45 | 55.4 | 63.1 | -7.6 | -14.91 | -14.8 | -0.02 | 41.6 | no edge shown yet |
| consensus_gap+money_moving | both | 27-28 | 49.1 | 49.7 | -0.6 | -5.45 | -9.9 | 0.52 | 47.3 | no edge shown yet |
| consensus_gap+pin_value | both | 30-31 | 49.2 | 47.3 | 1.9 | -4.8 | -7.9 | 0.27 | 44.3 | no edge shown yet |
| follow_move+rlm_quiet | both | 56-68 | 45.2 | 36.7 | 8.4 | +14.7 | 11.9 | 0.48 | 46.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 39-33 | 54.2 | 39.6 | 14.6 | +18.55 | 25.8 | 0.41 | 52.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 99-63 | 61.1 | 49.3 | 11.8 | +22.33 | 13.8 | 0.45 | 47.5 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 85-56 | 60.3 | 57.1 | 3.2 | -1.71 | -1.2 | 0.01 | 47.5 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 14-12 | 53.8 | 50.4 | 3.4 | +0.54 | 2.1 | 0.49 | 46.2 | keep collecting (26/30) |
| money_moving+pin_value | both | 12-8 | 60.0 | 50.8 | 9.2 | +2.65 | 13.2 | 0.48 | 50.0 | keep collecting (20/30) |
| rlm_quiet+rlm_ratio | both | 25-20 | 55.6 | 37.0 | 18.6 | +17.35 | 38.6 | 0.1 | 48.9 | no edge shown yet |
| rlm_quiet+sharp_gap | both | 28-25 | 52.8 | 37.7 | 15.1 | +15.08 | 28.4 | 0.16 | 47.2 | no edge shown yet |
| rlm_ratio+sharp_gap | both | 39-33 | 54.2 | 39.6 | 14.6 | +18.55 | 25.8 | 0.41 | 52.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 134-97 | 58.0 | 55.6 | 2.4 | -8.08 | -3.5 | 0.04 | 42.9 | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | both | 84-75 | 52.8 | 48.0 | 4.8 | +3.59 | 2.3 | 0.43 | 49.1 | no edge shown yet |
| money_delta+money_level | both | 4-5 | 44.4 | 43.0 | 1.4 | -0.63 | -7.0 | 1.39 | 77.8 | keep collecting (9/30) |
| money_delta+money_moving | both | 13-12 | 52.0 | 39.6 | 12.4 | +4.99 | 20.0 | 0.94 | 56.0 | keep collecting (25/30) |
| money_delta+pin_value | both | 4-1 | 80.0 | 49.9 | 30.1 | +2.52 | 50.4 | 0.2 | 40.0 | keep collecting (5/30) |
| money_delta+sharp_gap | both | 11-10 | 52.4 | 38.8 | 13.6 | +5.25 | 25.0 | 1.12 | 66.7 | keep collecting (21/30) |
| pin_value+sharp_gap | both | 14-12 | 53.8 | 50.0 | 3.9 | +0.57 | 2.2 | 0.11 | 42.3 | keep collecting (26/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 49-60 | 45.0 | 52.9 | -8.0 | -22.7 | -20.8 | 0.76 | 56.0 | DROP: below break-even |
| consensus_gap+rlm_quiet | both | 5-8 | 38.5 | 36.4 | 2.0 | -2.39 | -18.4 | 0.97 | 76.9 | keep collecting (13/30) |
| follow_move+pin_value | both | 24-22 | 52.2 | 48.8 | 3.3 | -0.95 | -2.1 | -0.2 | 28.3 | no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 42.9 | -26.2 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 41-60 | 40.6 | 49.5 | -8.9 | -16.69 | -16.5 | 0.51 | 45.5 | DROP: below break-even |
| follow_move+money_level | both | 117-62 | 65.4 | 59.1 | 6.3 | -3.69 | -2.1 | 0.03 | 41.9 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 12-13 | 48.0 | 43.5 | 4.5 | -0.66 | -2.6 | 1.06 | 64.0 | keep collecting (25/30) |
| pin_value+rlm_ratio | both | 3-2 | 60.0 | 45.5 | 14.5 | +0.73 | 14.5 | -1.16 | 40.0 | keep collecting (5/30) |
| follow_move+money_moving | both | 72-47 | 60.5 | 51.2 | 9.3 | +10.93 | 9.2 | 0.42 | 49.6 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 4-0 | 100.0 | 49.4 | 50.6 | +3.52 | 88.0 | 0.25 | 25.0 | keep collecting (4/30) |
| follow_move+money_delta | both | 8-5 | 61.5 | 39.7 | 21.8 | +7.51 | 57.8 | 1.08 | 61.5 | keep collecting (13/30) |
| money_delta+rlm_quiet | both | 4-3 | 57.1 | 34.2 | 22.9 | +5.18 | 74.0 | 0.33 | 42.9 | keep collecting (7/30) |
| money_moving+rlm_quiet | both | 20-20 | 50.0 | 37.4 | 12.6 | +7.85 | 19.6 | 0.59 | 45.0 | no edge shown yet |
| money_moving+rlm_ratio | both | 19-13 | 59.4 | 40.6 | 18.8 | +11.71 | 36.6 | 0.77 | 56.2 | no edge shown yet |
| consensus_gap+rlm_ratio | both | 5-4 | 55.6 | 40.2 | 15.3 | +1.0 | 11.1 | 0.72 | 66.7 | keep collecting (9/30) |
| pin_move+pin_value | both | 4-10 | 28.6 | 49.3 | -20.7 | -6.32 | -45.1 | 0.36 | 28.6 | keep collecting (14/30) |
| follow_move+pin_move | both | 7-9 | 43.8 | 49.0 | -5.2 | -3.25 | -20.3 | 0.28 | 43.8 | keep collecting (16/30) |
| consensus_gap+pin_move | both | 2-6 | 25.0 | 46.9 | -21.9 | -4.14 | -51.7 | 0.29 | 50.0 | keep collecting (8/30) |
| money_level+pin_move | both | 4-6 | 40.0 | 49.9 | -9.9 | -3.02 | -30.2 | 0.14 | 30.0 | keep collecting (10/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-3 | 25.0 | 39.3 | -14.3 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-3 | 25.0 | 39.3 | -14.3 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+sharp_gap | both | 1-4 | 20.0 | 37.1 | -17.1 | -3.07 | -61.5 | -0.3 | 60.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.3 | -51.3 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-4 | 33.3 | 46.6 | -13.3 | -2.87 | -47.8 | 0.47 | 33.3 | keep collecting (6/30) |
| money_level+pin_rlm | both | 1-2 | 33.3 | 42.9 | -9.5 | -1.07 | -35.8 | 0.67 | 66.7 | keep collecting (3/30) |
| pin_move+pin_rlm | both | 1-1 | 50.0 | 28.6 | 21.4 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| pin_move+rlm_ratio | both | 1-1 | 50.0 | 28.6 | 21.4 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | both | 5-3 | 62.5 | 36.4 | 26.1 | +6.9 | 86.2 | 2.04 | 87.5 | keep collecting (8/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_moving+pin_move | both | 1-1 | 50.0 | 49.6 | 0.4 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |
| rlm_quiet | moneyline | 31-45 | 40.8 | 28.6 | 12.2 | +15.0 | 19.7 | 0.39 | 44.7 | DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.4 | 10.6 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 22-21 | 51.2 | 49.7 | 1.5 | -0.96 | -2.2 | 0.79 | 53.5 | no edge shown yet |
| pin_move | moneyline | 2-4 | 33.3 | 42.9 | -9.5 | -2.87 | -47.8 | 0.02 | 50.0 | keep collecting (6/30) |
| pin_move | spread | 2-7 | 22.2 | 49.0 | -26.8 | -5.15 | -57.2 | 0.11 | 22.2 | keep collecting (9/30) |
| pin_move | total | 7-9 | 43.8 | 50.1 | -6.3 | -2.55 | -15.9 | 0.31 | 43.8 | keep collecting (16/30) |
| money_delta | moneyline | 4-8 | 33.3 | 28.6 | 4.8 | +0.99 | 8.2 | 0.62 | 66.7 | keep collecting (12/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 9-3 | 75.0 | 49.7 | 25.3 | +5.08 | 42.3 | 1.25 | 41.7 | keep collecting (12/30) |
| pin_rlm | moneyline | 1-4 | 20.0 | 37.1 | -17.1 | -3.07 | -61.5 | -0.3 | 60.0 | keep collecting (5/30) |
| follow_move | moneyline | 287-209 | 57.9 | 52.8 | 5.1 | -25.52 | -5.1 | 0.02 | 41.9 | PROMOTE: beats break-even and its own base rate |
| follow_move | spread | 177-203 | 46.6 | 49.8 | -3.2 | -39.76 | -10.5 | 0.02 | 32.9 | DROP: below break-even |
| follow_move | total | 229-230 | 49.9 | 50.0 | -0.1 | -20.94 | -4.6 | 0.33 | 45.1 | no edge shown yet |
| rlm_ratio | moneyline | 17-20 | 45.9 | 29.7 | 16.2 | +11.27 | 30.4 | 0.18 | 51.4 | no edge shown yet |
| rlm_ratio | spread | 3-3 | 50.0 | 52.0 | -2.0 | -0.16 | -2.7 | 0.33 | 16.7 | keep collecting (6/30) |
| rlm_ratio | total | 19-10 | 65.5 | 49.6 | 15.9 | +7.44 | 25.7 | 0.72 | 62.1 | keep collecting (29/30) |
| money_level | moneyline | 133-70 | 65.5 | 67.0 | -1.5 | -26.8 | -13.2 | -0.33 | 41.4 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 18-18 | 50.0 | 49.0 | 1.0 | -1.75 | -4.8 | 0.94 | 50.0 | no edge shown yet |
| money_level | total | 90-82 | 52.3 | 50.2 | 2.1 | -0.23 | -0.1 | -0.31 | 32.0 | no edge shown yet |
| sharp_gap | moneyline | 85-96 | 47.0 | 48.0 | -1.0 | -9.89 | -5.5 | 0.21 | 49.2 | no edge shown yet |
| sharp_gap | spread | 20-16 | 55.6 | 49.8 | 5.7 | +2.0 | 5.6 | 0.78 | 41.7 | no edge shown yet |
| sharp_gap | total | 93-71 | 56.7 | 49.9 | 6.8 | +13.67 | 8.3 | 0.24 | 39.6 | no edge shown yet |
| money_moving | moneyline | 63-62 | 50.4 | 51.2 | -0.8 | -16.8 | -13.4 | 0.2 | 51.2 | no edge shown yet |
| money_moving | spread | 18-7 | 72.0 | 49.2 | 22.8 | +9.18 | 36.7 | 0.52 | 48.0 | keep collecting (25/30) |
| money_moving | total | 66-54 | 55.0 | 50.0 | 5.0 | +6.17 | 5.1 | 0.2 | 37.5 | no edge shown yet |
| pin_value | moneyline | 2-7 | 22.2 | 38.1 | -15.9 | -5.31 | -59.0 | 0.12 | 55.6 | keep collecting (9/30) |
| pin_value | spread | 36-29 | 55.4 | 49.1 | 6.3 | +2.57 | 3.9 | 0.18 | 33.8 | no edge shown yet |
| pin_value | total | 33-31 | 51.6 | 50.0 | 1.5 | -1.19 | -1.9 | -0.03 | 35.9 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 53.0 | -19.6 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 155-221 | 41.2 | 49.5 | -8.3 | -68.12 | -18.1 | 0.24 | 44.7 | DROP: below break-even |
| consensus_gap | spread | 93-79 | 54.1 | 48.9 | 5.2 | +2.1 | 1.2 | 0.31 | 38.4 | no edge shown yet |
| consensus_gap | total | 106-108 | 49.5 | 50.0 | -0.5 | -12.68 | -5.9 | 0.89 | 56.5 | no edge shown yet |
| money_level+sharp_gap | moneyline | 63-40 | 61.2 | 62.7 | -1.5 | -15.52 | -15.1 | -0.15 | 48.5 | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+follow_move | moneyline | 22-29 | 43.1 | 57.1 | -14.0 | -15.83 | -31.0 | 0.18 | 51.0 | no edge shown yet |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 33.9 | -8.9 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| consensus_gap+rlm_quiet | moneyline | 2-6 | 25.0 | 28.6 | -3.6 | -3.08 | -38.5 | 1.07 | 87.5 | keep collecting (8/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.9 | -9.5 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 31-45 | 40.8 | 28.6 | 12.2 | +15.0 | 19.7 | 0.39 | 44.7 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 38-21 | 64.4 | 67.1 | -2.7 | -9.64 | -16.3 | -0.19 | 52.5 | beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 27-46 | 37.0 | 49.7 | -12.7 | -15.11 | -20.7 | 0.5 | 46.6 | DROP: below break-even |
| follow_move+money_level | moneyline | 72-23 | 75.8 | 67.4 | 8.4 | -5.65 | -6.0 | -0.29 | 40.0 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 38-20 | 65.5 | 53.0 | 12.6 | +6.83 | 11.8 | 0.2 | 50.0 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 42-33 | 56.0 | 68.0 | -12.0 | -15.26 | -20.3 | -0.21 | 41.3 | no edge shown yet |
| follow_move+sharp_gap | moneyline | 45-29 | 60.8 | 48.8 | 12.0 | +7.15 | 9.7 | 0.24 | 48.6 | no edge shown yet |
| money_moving+sharp_gap | moneyline | 29-41 | 41.4 | 45.7 | -4.3 | -12.48 | -17.8 | 0.5 | 60.0 | DROP: below break-even |
| consensus_gap+money_moving | moneyline | 15-25 | 37.5 | 50.0 | -12.5 | -13.06 | -32.7 | 0.59 | 50.0 | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 17-20 | 45.9 | 29.7 | 16.2 | +11.27 | 30.4 | 0.18 | 51.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 13-14 | 48.1 | 28.6 | 19.6 | +12.4 | 45.9 | -0.1 | 44.4 | keep collecting (27/30) |
| rlm_quiet+sharp_gap | moneyline | 13-17 | 43.3 | 28.6 | 14.8 | +9.4 | 31.3 | -0.22 | 43.3 | no edge shown yet |
| rlm_ratio+sharp_gap | moneyline | 17-20 | 45.9 | 29.7 | 16.2 | +11.27 | 30.4 | 0.18 | 51.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 28.6 | -3.6 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 10-13 | 43.5 | 28.6 | 14.9 | +5.84 | 25.4 | 0.85 | 52.2 | keep collecting (23/30) |
| money_moving+rlm_ratio | moneyline | 7-7 | 50.0 | 28.6 | 21.4 | +6.63 | 47.4 | 0.82 | 57.1 | keep collecting (14/30) |
| money_delta+money_moving | moneyline | 4-8 | 33.3 | 28.6 | 4.8 | +0.99 | 8.2 | 0.62 | 66.7 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 4-7 | 36.4 | 28.6 | 7.8 | +1.99 | 18.1 | 0.68 | 72.7 | keep collecting (11/30) |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 42.9 | -42.9 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-2 | 50.0 | 50.0 | 0.0 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| money_level+pin_move | moneyline | 2-2 | 50.0 | 50.0 | 0.0 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-3 | 25.0 | 39.3 | -14.3 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-3 | 25.0 | 39.3 | -14.3 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+sharp_gap | moneyline | 1-4 | 20.0 | 37.1 | -17.1 | -3.07 | -61.5 | -0.3 | 60.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | -1.55 | 50.0 | keep collecting (2/30) |
| pin_move+sharp_gap | moneyline | 2-1 | 66.7 | 42.9 | 23.8 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+rlm_ratio | moneyline | 4-6 | 40.0 | 32.8 | 7.2 | -1.13 | -11.3 | 0.95 | 70.0 | keep collecting (10/30) |
| money_level+pin_rlm | moneyline | 1-2 | 33.3 | 42.9 | -9.5 | -1.07 | -35.8 | 0.67 | 66.7 | keep collecting (3/30) |
| pin_move+pin_rlm | moneyline | 1-1 | 50.0 | 28.6 | 21.4 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| pin_move+rlm_ratio | moneyline | 1-1 | 50.0 | 28.6 | 21.4 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| follow_move+money_delta | moneyline | 4-2 | 66.7 | 28.6 | 38.1 | +6.99 | 116.5 | 1.02 | 66.7 | keep collecting (6/30) |
| money_delta+rlm_quiet | moneyline | 3-2 | 60.0 | 28.6 | 31.4 | +5.35 | 107.0 | 0.46 | 60.0 | keep collecting (5/30) |
| money_delta+rlm_ratio | moneyline | 4-1 | 80.0 | 28.6 | 51.4 | +7.99 | 159.8 | 2.26 | 80.0 | keep collecting (5/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 28.6 | -28.6 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-2 | 33.3 | 28.6 | 4.8 | -0.36 | -12.0 | 2.5 | 100.0 | keep collecting (3/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 71.4 | -71.4 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 71.4 | -71.4 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 47.0 | -1.6 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 47.0 | 36.3 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 15-9 | 62.5 | 48.3 | 14.2 | +3.84 | 16.0 | 0.29 | 37.5 | keep collecting (24/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.4 | 10.6 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-3 | 50.0 | 52.0 | -2.0 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-7 | 58.8 | 48.8 | 10.0 | +2.09 | 12.3 | 0.88 | 41.2 | keep collecting (17/30) |
| money_level+money_moving | spread | 10-6 | 62.5 | 48.5 | 14.0 | +3.12 | 19.5 | 1.19 | 68.8 | keep collecting (16/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.7 | -5.9 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 4-3 | 57.1 | 49.6 | 7.6 | +0.41 | 5.8 | 0.57 | 57.1 | keep collecting (7/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 3-3 | 50.0 | 52.0 | -2.0 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 53.0 | -53.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 53.0 | -53.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-12 | 53.8 | 49.1 | 4.8 | +0.62 | 2.4 | 1.15 | 46.2 | keep collecting (26/30) |
| money_moving+sharp_gap | spread | 10-5 | 66.7 | 49.4 | 17.3 | +4.04 | 26.9 | 0.87 | 53.3 | keep collecting (15/30) |
| pin_value+sharp_gap | spread | 2-2 | 50.0 | 50.0 | 0.0 | -0.26 | -6.5 | 0.75 | 75.0 | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 9-12 | 42.9 | 47.9 | -5.0 | -4.2 | -20.0 | 1.0 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 47.0 | 15.5 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 12-10 | 54.5 | 48.4 | 6.2 | +0.98 | 4.5 | 0.82 | 45.5 | keep collecting (22/30) |
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
| consensus_gap+pin_move | spread | 0-3 | 0.0 | 49.0 | -49.0 | -3.0 | -100.0 | 0.33 | 33.3 | keep collecting (3/30) |
| follow_move+pin_move | spread | 2-3 | 40.0 | 47.0 | -7.0 | -1.15 | -23.0 | 0.0 | 20.0 | keep collecting (5/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 53.0 | -53.0 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_move | spread | 1-0 | 100.0 | 47.0 | 53.0 | +0.94 | 94.3 | -1.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 22-21 | 51.2 | 49.7 | 1.5 | -0.96 | -2.2 | 0.79 | 53.5 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 37-29 | 56.1 | 50.2 | 5.9 | +4.82 | 7.3 | -0.11 | 37.9 | no edge shown yet |
| money_level+sharp_gap | total | 57-45 | 55.9 | 50.1 | 5.8 | +6.82 | 6.7 | -0.05 | 36.3 | no edge shown yet |
| money_moving+sharp_gap | total | 45-29 | 60.8 | 49.9 | 10.9 | +12.03 | 16.3 | 0.28 | 37.8 | no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 11-7 | 61.1 | 50.0 | 11.2 | +2.96 | 16.4 | 0.33 | 33.3 | keep collecting (18/30) |
| money_moving+pin_value | total | 8-4 | 66.7 | 49.8 | 16.9 | +3.24 | 27.0 | 0.33 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | total | 12-8 | 60.0 | 50.0 | 10.0 | +2.83 | 14.1 | 0.15 | 35.0 | keep collecting (20/30) |
| follow_move+money_level | total | 33-29 | 53.2 | 50.2 | 3.1 | +0.99 | 1.6 | 0.24 | 43.5 | no edge shown yet |
| follow_move+pin_value | total | 10-12 | 45.5 | 50.0 | -4.6 | -3.03 | -13.8 | -0.41 | 27.3 | keep collecting (22/30) |
| follow_move+rlm_ratio | total | 19-10 | 65.5 | 49.6 | 15.9 | +7.44 | 25.7 | 0.72 | 62.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 44-27 | 62.0 | 49.9 | 12.0 | +13.1 | 18.4 | 0.56 | 47.9 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 6-5 | 54.5 | 49.7 | 4.9 | +0.54 | 4.9 | 1.09 | 72.7 | keep collecting (11/30) |
| pin_value+rlm_ratio | total | 3-1 | 75.0 | 49.8 | 25.2 | +1.73 | 43.2 | -0.25 | 50.0 | keep collecting (4/30) |
| rlm_ratio+sharp_gap | total | 19-10 | 65.5 | 49.6 | 15.9 | +7.44 | 25.7 | 0.72 | 62.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 25-24 | 51.0 | 49.9 | 1.1 | -1.12 | -2.3 | 0.59 | 49.0 | no edge shown yet |
| consensus_gap+money_level | total | 9-6 | 60.0 | 50.3 | 9.7 | +2.03 | 13.5 | -0.4 | 20.0 | keep collecting (15/30) |
| consensus_gap+money_moving | total | 7-2 | 77.8 | 50.0 | 27.8 | +4.3 | 47.7 | 0.0 | 33.3 | keep collecting (9/30) |
| consensus_gap+pin_value | total | 13-16 | 44.8 | 50.1 | -5.3 | -4.34 | -14.9 | 0.34 | 48.3 | keep collecting (29/30) |
| consensus_gap+sharp_gap | total | 9-11 | 45.0 | 50.0 | -5.0 | -2.89 | -14.5 | -0.1 | 30.0 | keep collecting (20/30) |
| money_moving+rlm_ratio | total | 10-5 | 66.7 | 49.7 | 17.0 | +4.22 | 28.1 | 0.67 | 60.0 | keep collecting (15/30) |
| consensus_gap+follow_move | total | 18-19 | 48.6 | 49.9 | -1.3 | -2.67 | -7.2 | 1.41 | 67.6 | no edge shown yet |
| consensus_gap+money_delta | total | 3-0 | 100.0 | 50.1 | 49.9 | +2.69 | 89.6 | 0.33 | 33.3 | keep collecting (3/30) |
| follow_move+money_delta | total | 3-3 | 50.0 | 49.7 | 0.3 | -0.31 | -5.2 | 1.33 | 66.7 | keep collecting (6/30) |
| money_delta+money_moving | total | 8-3 | 72.7 | 49.7 | 23.0 | +4.17 | 37.9 | 1.36 | 45.5 | keep collecting (11/30) |
| money_delta+pin_value | total | 3-0 | 100.0 | 49.9 | 50.1 | +2.69 | 89.6 | 0.0 | 33.3 | keep collecting (3/30) |
| money_delta+sharp_gap | total | 7-2 | 77.8 | 49.8 | 28.0 | +4.26 | 47.4 | 1.67 | 55.6 | keep collecting (9/30) |
| money_moving+rlm_quiet | total | 8-7 | 53.3 | 49.6 | 3.7 | +0.27 | 1.8 | 0.4 | 40.0 | keep collecting (15/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 11-5 | 68.8 | 49.6 | 19.1 | +5.04 | 31.5 | 0.62 | 62.5 | keep collecting (16/30) |
| rlm_quiet+sharp_gap | total | 14-7 | 66.7 | 49.6 | 17.0 | +5.77 | 27.5 | 0.86 | 57.1 | keep collecting (21/30) |
| follow_move+pin_move | total | 3-4 | 42.9 | 49.8 | -7.0 | -1.23 | -17.6 | 0.57 | 57.1 | keep collecting (7/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 3-2 | 60.0 | 49.7 | 10.3 | +0.73 | 14.5 | 0.8 | 60.0 | keep collecting (5/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 49.6 | 0.4 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 4-1 | 80.0 | 49.6 | 30.4 | +2.68 | 53.6 | 0.4 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | total | 1-4 | 20.0 | 50.4 | -30.4 | -3.09 | -61.8 | 0.4 | 20.0 | keep collecting (5/30) |
| pin_move+pin_value | total | 3-5 | 37.5 | 50.2 | -12.7 | -2.23 | -27.9 | 0.5 | 37.5 | keep collecting (8/30) |
| pin_move+sharp_gap | total | 0-3 | 0.0 | 50.4 | -50.4 | -3.0 | -100.0 | 1.0 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 49.6 | -49.6 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 1-2 | 33.3 | 49.6 | -16.2 | -1.09 | -36.4 | 1.67 | 100.0 | keep collecting (3/30) |
| consensus_gap+pin_move | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | 0.5 | 50.0 | keep collecting (2/30) |
| money_moving+pin_move | total | 1-1 | 50.0 | 49.6 | 0.4 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 290-423 | 40.7 | 42.1 | -1.4 | -70.86 | -9.9 |  |  | DROP: below break-even |
| pin_move | both | 691-712 | 49.3 | 49.7 | -0.4 | -57.33 | -4.1 |  |  | DROP: below break-even |
| money_delta | both | 415-537 | 43.6 | 44.3 | -0.7 | -68.68 | -7.2 |  |  | DROP: below break-even |
| pin_rlm | both | 181-221 | 45.0 | 42.2 | 2.8 | +13.0 | 3.2 |  |  | DROP: below break-even |
| follow_move | both | 1169-1111 | 51.3 | 50.9 | 0.3 | -153.6 | -6.7 |  |  | no edge shown yet |
| rlm_ratio | both | 269-332 | 44.8 | 43.8 | 1.0 | -30.56 | -5.1 |  |  | DROP: below break-even |
| money_level | both | 1486-1118 | 57.1 | 55.3 | 1.8 | -98.73 | -3.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 1157-1335 | 46.4 | 47.7 | -1.3 | -194.16 | -7.8 |  |  | DROP: below break-even |
| money_moving | both | 1171-1326 | 46.9 | 48.0 | -1.1 | -186.26 | -7.5 |  |  | DROP: below break-even |
| pin_value | both | 504-506 | 49.9 | 48.4 | 1.5 | +5.37 | 0.5 |  |  | DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 51.0 | 15.7 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 460-551 | 45.5 | 48.7 | -3.2 | -85.21 | -8.4 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 162-162 | 50.0 | 51.1 | -1.1 | -23.14 | -7.1 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 191-293 | 39.5 | 45.9 | -6.4 | -43.9 | -9.1 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 118-108 | 52.2 | 50.6 | 1.6 | +16.03 | 7.1 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 30-47 | 39.0 | 38.9 | 0.1 | +10.61 | 13.8 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 178-187 | 48.8 | 46.6 | 2.2 | +7.44 | 2.0 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | both | 33-54 | 37.9 | 40.2 | -2.2 | -3.42 | -3.9 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 190-301 | 38.7 | 45.4 | -6.7 | -48.75 | -9.9 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 619-673 | 47.9 | 49.0 | -1.0 | -107.22 | -8.3 |  |  | DROP: below break-even |
| follow_move+pin_move | both | 488-524 | 48.2 | 49.7 | -1.5 | -78.12 | -7.7 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 142-166 | 46.1 | 43.5 | 2.6 | -8.78 | -2.8 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 173-166 | 51.0 | 49.2 | 1.9 | -1.87 | -0.6 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 269-332 | 44.8 | 43.8 | 1.0 | -30.56 | -5.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 620-673 | 48.0 | 48.7 | -0.8 | -99.81 | -7.7 |  |  | DROP: below break-even |
| money_moving+pin_move | both | 392-434 | 47.5 | 48.5 | -1.0 | -44.34 | -5.4 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 175-211 | 45.3 | 42.4 | 3.0 | +17.04 | 4.4 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 214-253 | 45.8 | 47.8 | -2.0 | -27.97 | -6.0 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 259-319 | 44.8 | 43.9 | 0.9 | -28.1 | -4.9 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 1114-1276 | 46.6 | 47.8 | -1.2 | -170.68 | -7.1 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 167-186 | 47.3 | 43.9 | 3.4 | +11.13 | 3.2 |  |  | DROP: below break-even |
| pin_move+pin_value | both | 218-222 | 49.5 | 49.5 | 0.0 | -16.41 | -3.7 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 150-162 | 48.1 | 45.0 | 3.1 | +0.43 | 0.1 |  |  | DROP: below break-even |
| pin_move+sharp_gap | both | 394-441 | 47.2 | 48.3 | -1.1 | -48.22 | -5.8 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 48-51 | 48.5 | 46.5 | 2.0 | +10.26 | 10.4 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 142-166 | 46.1 | 43.5 | 2.6 | -8.78 | -2.8 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 181-221 | 45.0 | 42.2 | 2.8 | +13.0 | 3.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 45-40 | 52.9 | 48.5 | 4.4 | +1.43 | 1.7 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 215-258 | 45.5 | 47.9 | -2.4 | -32.08 | -6.8 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 269-332 | 44.8 | 43.8 | 1.0 | -30.56 | -5.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 202-249 | 44.8 | 45.5 | -0.8 | -44.32 | -9.8 |  |  | DROP: below break-even |
| money_level+money_moving | both | 816-727 | 52.9 | 52.4 | 0.5 | -70.01 | -4.5 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 795-719 | 52.5 | 52.2 | 0.4 | -69.51 | -4.6 |  |  | no edge shown yet |
| follow_move+money_level | both | 716-526 | 57.6 | 56.0 | 1.7 | -64.0 | -5.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 121-105 | 53.5 | 47.9 | 5.6 | +11.02 | 4.9 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 287-218 | 56.8 | 58.0 | -1.2 | -26.15 | -5.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_move | both | 382-352 | 52.0 | 53.1 | -1.0 | -42.36 | -5.8 |  |  | no edge shown yet |
| money_level+pin_value | both | 241-225 | 51.7 | 50.0 | 1.7 | -15.12 | -3.2 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 28-64 | 30.4 | 37.5 | -7.0 | -15.79 | -17.2 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | both | 290-423 | 40.7 | 42.1 | -1.4 | -70.86 | -9.9 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 148-236 | 38.5 | 41.6 | -3.1 | -50.33 | -13.1 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 300-418 | 41.8 | 42.7 | -0.9 | -55.74 | -7.8 |  |  | DROP: below break-even |
| consensus_gap+money_delta | both | 55-118 | 31.8 | 38.4 | -6.6 | -22.78 | -13.2 |  |  | DROP: below break-even |
| money_delta+money_level | both | 143-135 | 51.4 | 47.2 | 4.2 | +13.03 | 4.7 |  |  | no edge shown yet |
| money_delta+pin_value | both | 89-82 | 52.0 | 47.5 | 4.6 | +6.45 | 3.8 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 297-412 | 41.9 | 42.7 | -0.8 | -52.91 | -7.5 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 115-198 | 36.7 | 40.2 | -3.5 | -43.85 | -14.0 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | both | 140-231 | 37.7 | 41.5 | -3.8 | -51.33 | -13.8 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 78-136 | 36.4 | 42.4 | -6.0 | -48.86 | -22.8 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | both | 140-186 | 42.9 | 43.9 | -0.9 | -24.39 | -7.5 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 61-102 | 37.4 | 40.4 | -3.0 | -24.29 | -14.9 |  |  | DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 51.0 | 15.7 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 149-178 | 45.6 | 46.2 | -0.6 | -18.94 | -5.8 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 76-59 | 56.3 | 46.7 | 9.6 | +15.58 | 11.5 |  |  | no edge shown yet |
| money_delta+pin_rlm | both | 103-125 | 45.2 | 42.4 | 2.8 | +2.76 | 1.2 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | both | 144-171 | 45.7 | 44.1 | 1.6 | -19.54 | -6.2 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | both | 37-52 | 41.6 | 47.5 | -5.9 | -7.57 | -8.5 |  |  | DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 49.6 | 50.4 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 91-186 | 32.9 | 29.3 | 3.5 | -17.84 | -6.4 |  |  | DROP: below break-even |
| rlm_quiet | spread | 67-70 | 48.9 | 51.3 | -2.4 | -7.64 | -5.6 |  |  | no edge shown yet |
| rlm_quiet | total | 132-167 | 44.1 | 49.7 | -5.6 | -45.38 | -15.2 |  |  | DROP: below break-even |
| pin_move | moneyline | 161-153 | 51.3 | 48.1 | 3.2 | +18.44 | 5.9 |  |  | no edge shown yet |
| pin_move | spread | 259-280 | 48.1 | 50.4 | -2.3 | -44.31 | -8.2 |  |  | DROP: below break-even |
| pin_move | total | 271-279 | 49.3 | 49.9 | -0.6 | -31.46 | -5.7 |  |  | no edge shown yet |
| money_delta | moneyline | 76-211 | 26.5 | 30.5 | -4.0 | -52.7 | -18.4 |  |  | DROP: below break-even |
| money_delta | spread | 141-142 | 49.8 | 51.0 | -1.2 | -13.45 | -4.8 |  |  | no edge shown yet |
| money_delta | total | 198-184 | 51.8 | 49.7 | 2.1 | -2.53 | -0.7 |  |  | no edge shown yet |
| pin_rlm | moneyline | 54-104 | 34.2 | 30.2 | 4.0 | +13.85 | 8.8 |  |  | DROP: below break-even |
| pin_rlm | spread | 30-26 | 53.6 | 51.2 | 2.4 | +1.3 | 2.3 |  |  | no edge shown yet |
| pin_rlm | total | 97-91 | 51.6 | 49.7 | 1.9 | -2.15 | -1.1 |  |  | no edge shown yet |
| follow_move | moneyline | 425-325 | 56.7 | 53.1 | 3.5 | -46.35 | -6.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 335-356 | 48.5 | 49.7 | -1.2 | -50.88 | -7.4 |  |  | DROP: below break-even |
| follow_move | total | 409-430 | 48.7 | 50.0 | -1.2 | -56.37 | -6.7 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 61-132 | 31.6 | 30.8 | 0.8 | -20.58 | -10.7 |  |  | DROP: below break-even |
| rlm_ratio | spread | 52-52 | 50.0 | 50.4 | -0.4 | -4.87 | -4.7 |  |  | no edge shown yet |
| rlm_ratio | total | 156-148 | 51.3 | 49.8 | 1.6 | -5.1 | -1.7 |  |  | no edge shown yet |
| money_level | moneyline | 579-247 | 70.1 | 67.4 | 2.6 | -47.52 | -5.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 415-419 | 49.8 | 49.1 | 0.7 | -45.15 | -5.4 |  |  | DROP: below break-even |
| money_level | total | 492-452 | 52.1 | 50.1 | 2.0 | -6.06 | -0.6 |  |  | no edge shown yet |
| sharp_gap | moneyline | 297-455 | 39.5 | 43.0 | -3.5 | -94.45 | -12.6 |  |  | DROP: below break-even |
| sharp_gap | spread | 421-405 | 51.0 | 49.5 | 1.4 | -25.25 | -3.1 |  |  | no edge shown yet |
| sharp_gap | total | 439-475 | 48.0 | 49.9 | -1.9 | -74.46 | -8.1 |  |  | DROP: below break-even |
| money_moving | moneyline | 314-434 | 42.0 | 44.1 | -2.1 | -71.51 | -9.6 |  |  | DROP: below break-even |
| money_moving | spread | 418-408 | 50.6 | 49.5 | 1.1 | -31.12 | -3.8 |  |  | no edge shown yet |
| money_moving | total | 439-484 | 47.6 | 49.9 | -2.4 | -83.63 | -9.1 |  |  | DROP: below break-even |
| pin_value | moneyline | 25-67 | 27.2 | 34.6 | -7.4 | +19.98 | 21.7 |  |  | DROP: below break-even |
| pin_value | spread | 230-209 | 52.4 | 49.6 | 2.8 | -8.79 | -2.0 |  |  | no edge shown yet |
| pin_value | total | 249-230 | 52.0 | 50.1 | 1.9 | -5.83 | -1.2 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 53.0 | 47.0 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 208-324 | 39.1 | 47.7 | -8.6 | -78.5 | -14.8 |  |  | DROP: below break-even |
| consensus_gap | spread | 112-96 | 53.8 | 49.1 | 4.8 | -0.16 | -0.1 |  |  | no edge shown yet |
| consensus_gap | total | 140-131 | 51.7 | 50.2 | 1.5 | -6.55 | -2.4 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 212-127 | 62.5 | 62.3 | 0.2 | -16.17 | -4.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 195-128 | 60.4 | 61.8 | -1.4 | -21.19 | -6.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 278-415 | 40.1 | 43.0 | -2.9 | -67.91 | -9.8 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 72-85 | 45.9 | 52.9 | -7.0 | -24.78 | -15.8 |  |  | DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 10-48 | 17.2 | 30.0 | -12.8 | -15.86 | -27.3 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 91-186 | 32.9 | 29.3 | 3.5 | -17.84 | -6.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 147-88 | 62.6 | 67.8 | -5.2 | -18.27 | -7.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 76-178 | 29.9 | 42.6 | -12.6 | -29.23 | -11.5 |  |  | !! CHECK: consensus_gap+money_moving close moneyline all sits -12.6 pts from its base (42.6%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+money_level | moneyline | 309-118 | 72.4 | 68.2 | 4.1 | -25.14 | -5.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+money_moving | moneyline | 158-177 | 47.2 | 46.9 | 0.3 | -30.41 | -9.1 |  |  | DROP: below break-even |
| money_delta+money_moving | moneyline | 71-191 | 27.1 | 30.0 | -2.9 | -37.4 | -14.3 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 69-190 | 26.6 | 30.0 | -3.4 | -38.59 | -14.9 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 74-186 | 28.5 | 41.6 | -13.1 | -34.97 | -13.4 |  |  | !! CHECK: consensus_gap+sharp_gap close moneyline all sits -13.1 pts from its base (41.6%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+sharp_gap | moneyline | 150-179 | 45.6 | 45.9 | -0.3 | -33.44 | -10.2 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | moneyline | 43-109 | 28.3 | 29.1 | -0.8 | -18.39 | -12.1 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 44-111 | 28.4 | 29.1 | -0.7 | -20.79 | -13.4 |  |  | DROP: below break-even |
| consensus_gap+pin_move | moneyline | 49-41 | 54.4 | 51.9 | 2.5 | +22.74 | 25.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 14-32 | 30.4 | 31.4 | -0.9 | +11.53 | 25.1 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 7-37 | 15.9 | 30.5 | -14.6 | -9.26 | -21.0 |  |  | DROP: below break-even |
| follow_move+pin_move | moneyline | 125-113 | 52.5 | 48.9 | 3.6 | +1.45 | 0.6 |  |  | no edge shown yet |
| follow_move+pin_rlm | moneyline | 37-65 | 36.3 | 30.7 | 5.6 | -4.12 | -4.0 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 61-132 | 31.6 | 30.8 | 0.8 | -20.58 | -10.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 70-87 | 44.6 | 42.5 | 2.1 | +10.04 | 6.4 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 53-97 | 35.3 | 30.3 | 5.1 | +19.45 | 13.0 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 59-124 | 32.2 | 30.9 | 1.3 | -15.7 | -8.6 |  |  | DROP: below break-even |
| pin_move+pin_rlm | moneyline | 40-69 | 36.7 | 30.1 | 6.6 | +11.99 | 11.0 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 42-62 | 40.4 | 29.8 | 10.6 | +8.9 | 8.6 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 31-52 | 37.3 | 31.1 | 6.2 | +1.62 | 1.9 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 68-93 | 42.2 | 41.6 | 0.6 | +3.47 | 2.2 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 24-53 | 31.2 | 29.7 | 1.5 | -9.26 | -12.0 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 37-65 | 36.3 | 30.7 | 5.6 | -4.12 | -4.0 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 54-104 | 34.2 | 30.2 | 4.0 | +13.85 | 8.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 40-106 | 27.4 | 29.1 | -1.7 | -20.63 | -14.1 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 61-132 | 31.6 | 30.8 | 0.8 | -20.58 | -10.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 16-87 | 15.5 | 30.2 | -14.7 | -25.79 | -25.0 |  |  | DROP: below break-even |
| consensus_gap+pin_value | moneyline | 17-51 | 25.0 | 33.0 | -8.0 | +3.23 | 4.7 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 25-46 | 35.2 | 31.6 | 3.6 | -0.3 | -0.4 |  |  | DROP: below break-even |
| money_delta+pin_rlm | moneyline | 31-58 | 34.8 | 30.5 | 4.3 | +3.91 | 4.4 |  |  | DROP: below break-even |
| money_delta+pin_value | moneyline | 4-18 | 18.2 | 28.6 | -10.4 | -5.3 | -24.1 |  |  | keep collecting (22/30) |
| money_moving+pin_value | moneyline | 13-37 | 26.0 | 32.8 | -6.8 | +10.89 | 21.8 |  |  | DROP: below break-even |
| pin_move+pin_value | moneyline | 9-13 | 40.9 | 40.3 | 0.7 | +6.3 | 28.6 |  |  | keep collecting (22/30) |
| pin_rlm+pin_value | moneyline | 6-11 | 35.3 | 28.6 | 6.7 | +12.45 | 73.2 |  |  | keep collecting (17/30) |
| pin_value+sharp_gap | moneyline | 13-41 | 24.1 | 34.1 | -10.0 | +6.89 | 12.8 |  |  | DROP: below break-even |
| follow_move+money_delta | moneyline | 38-77 | 33.0 | 32.7 | 0.4 | -21.98 | -19.1 |  |  | DROP: below break-even |
| money_delta+money_level | moneyline | 21-27 | 43.8 | 34.8 | 8.9 | +10.22 | 21.3 |  |  | no edge shown yet |
| money_delta+rlm_ratio | moneyline | 32-66 | 32.7 | 31.6 | 1.0 | -16.47 | -16.8 |  |  | DROP: below break-even |
| money_level+pin_move | moneyline | 95-58 | 62.1 | 65.6 | -3.5 | -8.05 | -5.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 14-14 | 50.0 | 34.7 | 15.3 | +3.97 | 14.2 |  |  | keep collecting (28/30) |
| money_level+rlm_ratio | moneyline | 17-20 | 45.9 | 37.8 | 8.1 | +1.43 | 3.9 |  |  | no edge shown yet |
| money_delta+rlm_quiet | moneyline | 24-59 | 28.9 | 30.1 | -1.2 | -21.64 | -26.1 |  |  | DROP: below break-even |
| money_level+pin_value | moneyline | 6-8 | 42.9 | 65.3 | -22.5 | -4.75 | -33.9 |  |  | keep collecting (14/30) |
| follow_move+pin_value | moneyline | 5-10 | 33.3 | 40.0 | -6.7 | +4.75 | 31.7 |  |  | keep collecting (15/30) |
| pin_value+rlm_quiet | moneyline | 3-7 | 30.0 | 28.6 | 1.4 | +6.5 | 65.0 |  |  | keep collecting (10/30) |
| pin_value+rlm_ratio | moneyline | 2-3 | 40.0 | 28.6 | 11.4 | -0.1 | -2.0 |  |  | keep collecting (5/30) |
| consensus_gap+follow_move | spread | 39-32 | 54.9 | 48.4 | 6.6 | +1.39 | 2.0 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 54-51 | 51.4 | 48.8 | 2.6 | -4.88 | -4.7 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 33-38 | 46.5 | 49.4 | -2.9 | -9.7 | -13.7 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 5-4 | 55.6 | 50.3 | 5.2 | +0.3 | 3.3 |  |  | keep collecting (9/30) |
| consensus_gap+pin_value | spread | 80-60 | 57.1 | 49.1 | 8.1 | +8.31 | 5.9 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 6-4 | 60.0 | 50.0 | 10.0 | +1.09 | 10.9 |  |  | keep collecting (10/30) |
| consensus_gap+sharp_gap | spread | 53-51 | 51.0 | 49.0 | 1.9 | -5.78 | -5.6 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 195-196 | 49.9 | 49.3 | 0.5 | -19.47 | -5.0 |  |  | no edge shown yet |
| follow_move+pin_move | spread | 161-188 | 46.1 | 50.1 | -4.0 | -41.24 | -11.8 |  |  | DROP: below break-even |
| follow_move+pin_rlm | spread | 21-21 | 50.0 | 50.7 | -0.7 | -1.83 | -4.4 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 74-66 | 52.9 | 49.1 | 3.8 | -1.44 | -1.0 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 52-52 | 50.0 | 50.4 | -0.4 | -4.87 | -4.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 196-195 | 50.1 | 49.4 | 0.8 | -17.34 | -4.4 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 145-155 | 48.3 | 49.9 | -1.6 | -23.97 | -8.0 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 28-26 | 51.9 | 51.1 | 0.7 | -0.53 | -1.0 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 105-109 | 49.1 | 49.2 | -0.1 | -18.35 | -8.6 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 50-51 | 49.5 | 50.3 | -0.8 | -5.81 | -5.7 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 413-400 | 50.8 | 49.5 | 1.3 | -27.62 | -3.4 |  |  | no edge shown yet |
| pin_move+pin_rlm | spread | 30-26 | 53.6 | 51.2 | 2.4 | +1.3 | 2.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 103-107 | 49.0 | 50.0 | -0.9 | -16.38 | -7.8 |  |  | no edge shown yet |
| pin_move+rlm_ratio | spread | 27-28 | 49.1 | 50.7 | -1.6 | -3.52 | -6.4 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 148-155 | 48.8 | 49.9 | -1.1 | -21.24 | -7.0 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 10-11 | 47.6 | 51.3 | -3.7 | -2.19 | -10.4 |  |  | keep collecting (21/30) |
| pin_rlm+rlm_ratio | spread | 21-21 | 50.0 | 50.7 | -0.7 | -1.83 | -4.4 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 30-26 | 53.6 | 51.2 | 2.4 | +1.3 | 2.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 8-8 | 50.0 | 49.6 | 0.4 | -1.17 | -7.3 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | spread | 105-109 | 49.1 | 49.3 | -0.2 | -18.41 | -8.6 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 52-52 | 50.0 | 50.4 | -0.4 | -4.87 | -4.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 184-192 | 48.9 | 48.9 | -0.0 | -25.57 | -6.8 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 30-30 | 50.0 | 50.0 | 0.0 | -3.02 | -5.0 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 321-311 | 50.8 | 49.1 | 1.7 | -22.1 | -3.5 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 65-58 | 52.8 | 48.5 | 4.4 | -2.35 | -1.9 |  |  | no edge shown yet |
| money_level+money_moving | spread | 320-312 | 50.6 | 49.1 | 1.6 | -24.02 | -3.8 |  |  | no edge shown yet |
| money_level+pin_move | spread | 129-151 | 46.1 | 49.6 | -3.5 | -34.99 | -12.5 |  |  | DROP: below break-even |
| money_level+pin_value | spread | 113-112 | 50.2 | 48.8 | 1.5 | -14.6 | -6.5 |  |  | no edge shown yet |
| consensus_gap+money_delta | spread | 17-15 | 53.1 | 50.9 | 2.2 | -0.46 | -1.4 |  |  | no edge shown yet |
| follow_move+money_delta | spread | 46-53 | 46.5 | 50.5 | -4.0 | -11.4 | -11.5 |  |  | no edge shown yet |
| money_delta+money_level | spread | 47-45 | 51.1 | 49.9 | 1.2 | -2.69 | -2.9 |  |  | no edge shown yet |
| money_delta+money_moving | spread | 81-86 | 48.5 | 50.5 | -2.0 | -12.88 | -7.7 |  |  | no edge shown yet |
| money_delta+pin_value | spread | 38-30 | 55.9 | 50.8 | 5.1 | +3.19 | 4.7 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 80-84 | 48.8 | 50.5 | -1.7 | -11.86 | -7.2 |  |  | no edge shown yet |
| follow_move+rlm_quiet | spread | 67-70 | 48.9 | 51.3 | -2.4 | -7.64 | -5.6 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 15-8 | 65.2 | 51.4 | 13.8 | +5.65 | 24.5 |  |  | keep collecting (23/30) |
| rlm_quiet+sharp_gap | spread | 29-18 | 61.7 | 51.7 | 10.0 | +8.6 | 18.3 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 16-13 | 55.2 | 50.3 | 4.9 | +1.39 | 4.8 |  |  | keep collecting (29/30) |
| money_delta+pin_move | spread | 43-49 | 46.7 | 51.2 | -4.5 | -9.9 | -10.8 |  |  | no edge shown yet |
| money_delta+rlm_ratio | spread | 19-30 | 38.8 | 50.1 | -11.3 | -13.18 | -26.9 |  |  | DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 53.0 | 47.0 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_rlm | spread | 16-18 | 47.1 | 51.1 | -4.0 | -3.61 | -10.6 |  |  | no edge shown yet |
| money_delta+rlm_quiet | spread | 18-20 | 47.4 | 51.7 | -4.4 | -3.29 | -8.7 |  |  | no edge shown yet |
| money_moving+rlm_quiet | spread | 28-18 | 60.9 | 51.7 | 9.2 | +7.65 | 16.6 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 38-39 | 49.4 | 51.7 | -2.4 | -3.59 | -4.7 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-3 | 66.7 | 52.3 | 14.4 | +2.56 | 28.4 |  |  | keep collecting (9/30) |
| consensus_gap+rlm_quiet | spread | 4-3 | 57.1 | 51.3 | 5.9 | +0.48 | 6.9 |  |  | keep collecting (7/30) |
| pin_value+rlm_quiet | spread | 7-7 | 50.0 | 50.4 | -0.4 | -0.85 | -6.1 |  |  | keep collecting (14/30) |
| follow_move+money_delta | total | 118-119 | 49.8 | 49.7 | 0.0 | -10.93 | -4.6 |  |  | no edge shown yet |
| money_level+money_moving | total | 284-288 | 49.7 | 50.1 | -0.4 | -29.82 | -5.2 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 279-280 | 49.9 | 50.1 | -0.1 | -26.22 | -4.7 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 423-461 | 47.9 | 49.9 | -2.1 | -75.15 | -8.5 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 75-72 | 51.0 | 50.3 | 0.7 | -5.53 | -3.8 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 36-29 | 55.4 | 50.2 | 5.2 | +2.99 | 4.6 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 81-76 | 51.6 | 50.2 | 1.4 | -4.1 | -2.6 |  |  | no edge shown yet |
| follow_move+money_moving | total | 266-300 | 47.0 | 49.9 | -2.9 | -57.34 | -10.1 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 274-299 | 47.8 | 49.9 | -2.1 | -49.04 | -8.6 |  |  | DROP: below break-even |
| money_level+pin_move | total | 158-143 | 52.5 | 50.0 | 2.5 | +0.68 | 0.2 |  |  | no edge shown yet |
| money_level+pin_value | total | 122-105 | 53.7 | 50.2 | 3.5 | +4.23 | 1.9 |  |  | no edge shown yet |
| pin_move+pin_value | total | 106-102 | 51.0 | 50.0 | 1.0 | -6.33 | -3.0 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 132-167 | 44.1 | 49.7 | -5.6 | -45.38 | -15.2 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 177-192 | 48.0 | 49.9 | -1.9 | -30.41 | -8.2 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | total | 75-107 | 41.2 | 49.7 | -8.5 | -38.14 | -21.0 |  |  | DROP: below break-even |
| money_delta+money_moving | total | 148-141 | 51.2 | 49.7 | 1.5 | -5.46 | -1.9 |  |  | no edge shown yet |
| follow_move+money_level | total | 223-216 | 50.8 | 50.1 | 0.7 | -13.29 | -3.0 |  |  | no edge shown yet |
| follow_move+pin_value | total | 94-90 | 51.1 | 50.0 | 1.1 | -5.18 | -2.8 |  |  | no edge shown yet |
| money_moving+pin_value | total | 96-107 | 47.3 | 50.0 | -2.8 | -20.5 | -10.1 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 97-108 | 47.3 | 50.0 | -2.7 | -20.55 | -10.0 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 61-64 | 48.8 | 50.2 | -1.4 | -9.79 | -7.8 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 63-64 | 49.6 | 50.2 | -0.6 | -8.0 | -6.3 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 51-45 | 53.1 | 50.2 | 2.9 | +0.26 | 0.3 |  |  | no edge shown yet |
| consensus_gap+money_delta | total | 22-16 | 57.9 | 50.0 | 7.9 | +3.47 | 9.1 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | total | 14-13 | 51.9 | 49.9 | 2.0 | -0.42 | -1.6 |  |  | keep collecting (27/30) |
| money_delta+rlm_quiet | total | 36-57 | 38.7 | 49.6 | -10.9 | -23.92 | -25.7 |  |  | DROP: below break-even |
| money_delta+sharp_gap | total | 148-138 | 51.7 | 49.7 | 2.0 | -2.46 | -0.9 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 69-104 | 39.9 | 49.7 | -9.8 | -40.59 | -23.5 |  |  | !! IMPLAUSIBLE: money_moving+rlm_quiet close total all 39.9% on n=173. A -110 market outside 40-60% at this sample is a measurement bug until proven otherwise. Recompute from source.  ||  DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 75-63 | 54.3 | 49.8 | 4.5 | +5.5 | 4.0 |  |  | no edge shown yet |
| money_delta+pin_move | total | 81-83 | 49.4 | 49.7 | -0.3 | -8.74 | -5.3 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 178-193 | 48.0 | 49.9 | -1.9 | -30.45 | -8.2 |  |  | DROP: below break-even |
| follow_move+pin_move | total | 202-223 | 47.5 | 49.9 | -2.4 | -38.33 | -9.0 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | total | 27-38 | 41.5 | 49.7 | -8.2 | -13.22 | -20.3 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | total | 11-11 | 50.0 | 50.0 | 0.0 | -1.22 | -5.5 |  |  | keep collecting (22/30) |
| consensus_gap+rlm_ratio | total | 20-13 | 60.6 | 50.0 | 10.6 | +4.76 | 14.4 |  |  | no edge shown yet |
| follow_move+pin_rlm | total | 84-80 | 51.2 | 49.7 | 1.5 | -2.83 | -1.7 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 156-148 | 51.3 | 49.8 | 1.6 | -5.1 | -1.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 46-32 | 59.0 | 49.7 | 9.3 | +10.22 | 13.1 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 74-55 | 57.4 | 49.8 | 7.5 | +12.61 | 9.8 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 94-88 | 51.6 | 49.7 | 1.9 | -1.89 | -1.0 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 150-144 | 51.0 | 49.8 | 1.3 | -6.59 | -2.2 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 97-91 | 51.6 | 49.7 | 1.9 | -2.15 | -1.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 92-82 | 52.9 | 49.8 | 3.1 | +2.33 | 1.3 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 32-29 | 52.5 | 49.8 | 2.7 | -0.01 | -0.0 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 84-80 | 51.2 | 49.7 | 1.5 | -2.83 | -1.7 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 97-91 | 51.6 | 49.7 | 1.9 | -2.15 | -1.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 35-29 | 54.7 | 49.8 | 4.9 | +2.69 | 4.2 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 156-148 | 51.3 | 49.8 | 1.6 | -5.1 | -1.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 56-49 | 53.3 | 49.7 | 3.7 | +2.46 | 2.3 |  |  | no edge shown yet |
| money_delta+rlm_ratio | total | 93-75 | 55.4 | 49.7 | 5.6 | +10.1 | 6.0 |  |  | no edge shown yet |
| money_delta+pin_value | total | 47-34 | 58.0 | 49.8 | 8.2 | +8.55 | 10.6 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 60-85 | 41.4 | 49.8 | -8.4 | -29.7 | -20.5 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | total | 31-46 | 40.3 | 49.7 | -9.4 | -17.58 | -22.8 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | total | 60-84 | 41.7 | 49.7 | -8.0 | -28.87 | -20.0 |  |  | DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 49.6 | 50.4 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| rlm_quiet | close | 1-3k bets | 184-274 | 40.2 | -1.9 | -8.7 |  |
| rlm_quiet | close | 3k+ bets | 74-102 | 42.0 | -0.3 | -10.3 |  |
| rlm_quiet | close | <1k bets | 32-47 | 40.5 | -1.5 | -16.0 |  |
| rlm_quiet | close | pin $1-2k | 77-131 | 37.0 | -6.7 | -18.6 |  |
| rlm_quiet | close | pin $2k+ | 91-110 | 45.3 | 7.0 | 3.5 |  |
| rlm_quiet | close | pin limit <$1k | 50-54 | 48.1 | -1.3 | -7.7 |  |
| pin_move | close | 1-3k bets | 434-443 | 49.5 | -0.1 | -2.8 |  |
| pin_move | close | 3k+ bets | 170-182 | 48.3 | -1.3 | -7.2 |  |
| pin_move | close | <1k bets | 87-87 | 50.0 | -0.3 | -4.3 |  |
| pin_move | close | pin $1-2k | 311-331 | 48.4 | -1.6 | -5.0 |  |
| pin_move | close | pin $2k+ | 258-264 | 49.4 | 0.1 | -4.5 |  |
| pin_move | close | pin limit <$1k | 122-117 | 51.0 | 1.4 | -0.5 |  |
| money_delta | close | 1-3k bets | 257-326 | 44.1 | -0.7 | -7.4 |  |
| money_delta | close | 3k+ bets | 106-135 | 44.0 | 0.1 | -2.4 |  |
| money_delta | close | <1k bets | 52-76 | 40.6 | -2.4 | -15.4 |  |
| money_delta | close | pin $1-2k | 151-148 | 50.5 | 4.3 | 5.3 |  |
| money_delta | close | pin $2k+ | 106-138 | 43.4 | 1.9 | -8.3 |  |
| money_delta | close | pin limit <$1k | 62-72 | 46.3 | -3.1 | -8.0 |  |
| pin_rlm | close | 1-3k bets | 113-133 | 45.9 | 3.6 | 9.0 |  |
| pin_rlm | close | 3k+ bets | 42-62 | 40.4 | -1.5 | -12.8 |  |
| pin_rlm | close | <1k bets | 26-26 | 50.0 | 7.7 | 7.9 |  |
| pin_rlm | close | pin $1-2k | 78-91 | 46.2 | 2.0 | 4.4 |  |
| pin_rlm | close | pin $2k+ | 54-89 | 37.8 | 1.9 | -5.1 |  |
| pin_rlm | close | pin limit <$1k | 49-41 | 54.4 | 5.6 | 14.3 |  |
| follow_move | close | 1-3k bets | 741-707 | 51.2 | 0.5 | -6.0 |  |
| follow_move | close | 3k+ bets | 264-250 | 51.4 | 0.4 | -5.6 |  |
| follow_move | close | <1k bets | 164-154 | 51.6 | -0.5 | -11.8 |  |
| follow_move | close | pin $1-2k | 348-405 | 46.2 | -4.2 | -13.4 |  |
| follow_move | close | pin $2k+ | 317-276 | 53.5 | 2.7 | -1.6 |  |
| follow_move | close | pin limit <$1k | 147-144 | 50.5 | 0.6 | -3.8 |  |
| rlm_ratio | close | 1-3k bets | 170-225 | 43.0 | -0.8 | -7.6 |  |
| rlm_ratio | close | 3k+ bets | 63-69 | 47.7 | 4.0 | 1.5 |  |
| rlm_ratio | close | <1k bets | 36-38 | 48.6 | 5.2 | -3.3 |  |
| rlm_ratio | close | pin $1-2k | 94-104 | 47.5 | 1.7 | -0.9 |  |
| rlm_ratio | close | pin $2k+ | 53-77 | 40.8 | 2.9 | -9.8 |  |
| rlm_ratio | close | pin limit <$1k | 54-50 | 51.9 | 2.8 | 0.1 |  |
| money_level | close | 1-3k bets | 949-691 | 57.9 | 2.5 | -2.5 |  |
| money_level | close | 3k+ bets | 332-277 | 54.5 | -0.5 | -5.7 |  |
| money_level | close | <1k bets | 205-149 | 57.9 | 2.5 | -6.2 |  |
| money_level | close | pin $1-2k | 438-388 | 53.0 | -0.7 | -5.9 |  |
| money_level | close | pin $2k+ | 385-312 | 55.2 | -2.0 | -8.8 |  |
| money_level | close | pin limit <$1k | 176-156 | 53.0 | 2.7 | 0.6 |  |
| sharp_gap | close | 1-3k bets | 719-846 | 45.9 | -1.7 | -9.0 |  |
| sharp_gap | close | 3k+ bets | 278-312 | 47.1 | -0.5 | -2.6 |  |
| sharp_gap | close | <1k bets | 160-176 | 47.6 | -0.6 | -11.1 |  |
| sharp_gap | close | pin $1-2k | 378-415 | 47.7 | -1.0 | -5.6 |  |
| sharp_gap | close | pin $2k+ | 308-361 | 46.0 | -0.7 | -5.4 |  |
| sharp_gap | close | pin limit <$1k | 150-168 | 47.2 | -2.3 | -6.8 |  |
| money_moving | close | 1-3k bets | 733-839 | 46.6 | -1.4 | -8.4 |  |
| money_moving | close | 3k+ bets | 280-312 | 47.3 | -0.8 | -3.5 |  |
| money_moving | close | <1k bets | 158-174 | 47.6 | -0.4 | -9.8 |  |
| money_moving | close | pin $1-2k | 379-416 | 47.7 | -1.3 | -5.8 |  |
| money_moving | close | pin $2k+ | 313-356 | 46.8 | 0.0 | -4.6 |  |
| money_moving | close | pin limit <$1k | 150-174 | 46.3 | -3.2 | -8.6 |  |
| pin_value | close | 1-3k bets | 327-319 | 50.6 | 2.2 | 3.0 |  |
| pin_value | close | 3k+ bets | 105-129 | 44.9 | -4.1 | -12.7 |  |
| pin_value | close | <1k bets | 72-58 | 55.4 | 8.0 | 12.3 |  |
| pin_value | close | pin $1-2k | 233-251 | 48.1 | -0.5 | -3.3 |  |
| pin_value | close | pin $2k+ | 143-163 | 46.7 | -0.4 | -2.0 |  |
| pin_value | close | pin limit <$1k | 128-92 | 58.2 | 8.3 | 12.4 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.0 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.0 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 292-343 | 46.0 | -3.3 | -9.3 |  |
| consensus_gap | close | 3k+ bets | 110-120 | 47.8 | -1.5 | 1.8 |  |
| consensus_gap | close | <1k bets | 58-86 | 40.3 | -5.1 | -19.8 |  |
| consensus_gap | close | pin $1-2k | 138-146 | 48.6 | -1.1 | 0.5 |  |
| consensus_gap | close | pin $2k+ | 140-133 | 51.3 | -0.4 | 1.8 |  |
| consensus_gap | close | pin limit <$1k | 59-56 | 51.3 | 1.3 | -0.2 |  |
| consensus_gap+follow_move | close | 1-3k bets | 108-106 | 50.5 | -0.8 | -5.2 |  |
| consensus_gap+money_level | close | 1-3k bets | 191-131 | 59.3 | 0.8 | -0.4 |  |
| consensus_gap+money_moving | close | 1-3k bets | 122-184 | 39.9 | -6.4 | -11.8 |  |
| consensus_gap+pin_move | close | 1-3k bets | 76-67 | 53.1 | 2.6 | 11.4 |  |
| consensus_gap+pin_value | close | 1-3k bets | 115-127 | 47.5 | 0.8 | -1.6 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 120-189 | 38.8 | -6.9 | -13.3 |  |
| follow_move+money_level | close | 1-3k bets | 466-337 | 58.0 | 2.3 | -4.0 |  |
| follow_move+money_moving | close | 1-3k bets | 402-440 | 47.7 | -1.2 | -8.2 |  |
| follow_move+pin_move | close | 1-3k bets | 303-335 | 47.5 | -2.1 | -9.0 |  |
| follow_move+pin_value | close | 1-3k bets | 107-103 | 51.0 | 2.0 | 1.2 |  |
| follow_move+sharp_gap | close | 1-3k bets | 403-441 | 47.7 | -0.9 | -7.6 |  |
| money_level+money_moving | close | 1-3k bets | 524-460 | 53.3 | 0.9 | -3.5 |  |
| money_level+pin_move | close | 1-3k bets | 250-223 | 52.9 | 0.1 | -4.0 |  |
| money_level+pin_value | close | 1-3k bets | 157-137 | 53.4 | 3.7 | 0.2 |  |
| money_level+sharp_gap | close | 1-3k bets | 505-454 | 52.7 | 0.6 | -3.8 |  |
| money_moving+pin_move | close | 1-3k bets | 252-269 | 48.4 | -0.3 | -3.1 |  |
| money_moving+pin_value | close | 1-3k bets | 139-161 | 46.3 | -1.5 | -6.2 |  |
| money_moving+sharp_gap | close | 1-3k bets | 691-804 | 46.2 | -1.6 | -8.1 |  |
| pin_move+pin_value | close | 1-3k bets | 138-136 | 50.4 | 0.7 | -1.8 |  |
| pin_move+sharp_gap | close | 1-3k bets | 256-275 | 48.2 | -0.3 | -3.1 |  |
| pin_value+sharp_gap | close | 1-3k bets | 140-167 | 45.6 | -2.2 | -7.7 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 184-274 | 40.2 | -1.9 | -8.7 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 90-159 | 36.1 | -5.2 | -15.4 |  |
| consensus_gap+money_delta | close | 1-3k bets | 33-70 | 32.0 | -6.6 | -18.2 |  |
| follow_move+money_delta | close | 1-3k bets | 126-157 | 44.5 | -1.6 | -11.0 |  |
| money_delta+money_level | close | 1-3k bets | 92-86 | 51.7 | 3.6 | 6.0 |  |
| money_delta+money_moving | close | 1-3k bets | 186-256 | 42.1 | -1.1 | -8.7 |  |
| money_delta+pin_value | close | 1-3k bets | 57-52 | 52.3 | 4.5 | 4.0 |  |
| money_delta+sharp_gap | close | 1-3k bets | 185-253 | 42.2 | -0.9 | -8.3 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 91-105 | 46.4 | -0.4 | -2.2 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 22-30 | 42.3 | 3.2 | 21.3 |  |
| money_level+pin_rlm | close | 1-3k bets | 49-39 | 55.7 | 7.9 | 7.6 |  |
| pin_move+pin_rlm | close | 1-3k bets | 104-111 | 48.4 | 4.4 | 7.2 |  |
| pin_rlm+pin_value | close | 1-3k bets | 33-30 | 52.4 | 5.8 | 22.8 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 113-133 | 45.9 | 3.6 | 9.0 |  |
| money_delta+pin_rlm | close | 1-3k bets | 63-74 | 46.0 | 3.1 | 6.5 |  |
| money_moving+pin_rlm | close | 1-3k bets | 108-125 | 46.4 | 3.8 | 10.8 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 25-38 | 39.7 | -0.8 | 2.3 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 170-225 | 43.0 | -0.8 | -7.6 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 88-115 | 43.3 | -1.2 | -11.8 |  |
| money_level+rlm_ratio | close | 1-3k bets | 78-73 | 51.7 | 3.0 | -0.1 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 163-214 | 43.2 | -0.8 | -6.9 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 89-98 | 47.6 | 2.7 | -0.6 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 30-27 | 52.6 | 4.7 | 1.6 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 170-225 | 43.0 | -0.8 | -7.6 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 17-42 | 28.8 | -7.8 | -14.3 |  |
| follow_move+pin_rlm | close | 1-3k bets | 83-105 | 44.1 | 0.6 | -7.0 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 84-155 | 35.1 | -6.1 | -16.8 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 83-119 | 41.1 | -2.8 | -10.9 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 35-66 | 34.7 | -5.1 | -18.6 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 83-105 | 44.1 | 0.6 | -7.0 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 71-136 | 34.3 | -5.7 | -16.3 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 47-87 | 35.1 | -7.8 | -25.4 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 21-30 | 41.2 | -5.0 | -0.2 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 50.4 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 40-35 | 53.3 | 2.8 | 0.3 |  |
| consensus_gap+money_moving | close | 3k+ bets | 44-68 | 39.3 | -6.7 | 4.2 |  |
| consensus_gap+pin_move | close | 3k+ bets | 34-28 | 54.8 | 4.1 | 5.5 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 5-10 | 33.3 | -8.7 | -11.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 44-44 | 50.0 | 2.3 | 1.1 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 5-9 | 35.7 | -5.4 | -4.3 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 44-69 | 38.9 | -6.6 | 5.7 |  |
| follow_move+money_moving | close | 3k+ bets | 141-152 | 48.1 | -0.7 | -6.9 |  |
| follow_move+pin_move | close | 3k+ bets | 129-132 | 49.4 | -0.2 | -4.5 |  |
| follow_move+pin_rlm | close | 3k+ bets | 39-45 | 46.4 | 3.2 | 1.3 |  |
| follow_move+pin_value | close | 3k+ bets | 43-48 | 47.3 | -2.6 | -11.1 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 63-69 | 47.7 | 4.0 | 1.5 |  |
| follow_move+sharp_gap | close | 3k+ bets | 140-150 | 48.3 | 0.1 | -4.8 |  |
| money_moving+pin_move | close | 3k+ bets | 93-115 | 44.7 | -3.6 | -12.4 |  |
| money_moving+pin_rlm | close | 3k+ bets | 41-60 | 40.6 | -1.3 | -12.1 |  |
| money_moving+pin_value | close | 3k+ bets | 52-71 | 42.3 | -6.3 | -15.0 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 60-67 | 47.2 | 3.5 | 0.3 |  |
| money_moving+sharp_gap | close | 3k+ bets | 269-300 | 47.3 | -0.4 | -2.5 |  |
| pin_move+pin_rlm | close | 3k+ bets | 39-54 | 41.9 | -1.6 | -9.7 |  |
| pin_move+pin_value | close | 3k+ bets | 48-62 | 43.6 | -6.0 | -17.7 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 41-46 | 47.1 | 2.4 | 0.9 |  |
| pin_move+sharp_gap | close | 3k+ bets | 91-115 | 44.2 | -3.7 | -12.2 |  |
| pin_rlm+pin_value | close | 3k+ bets | 8-18 | 30.8 | -16.7 | -41.4 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 39-45 | 46.4 | 3.2 | 1.3 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 42-62 | 40.4 | -1.5 | -12.8 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 10-12 | 45.5 | -4.7 | -13.7 |  |
| pin_value+sharp_gap | close | 3k+ bets | 52-71 | 42.3 | -6.5 | -14.9 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 63-69 | 47.7 | 4.0 | 1.5 |  |
| follow_move+money_delta | close | 3k+ bets | 50-63 | 44.2 | -0.7 | -9.1 |  |
| money_level+money_moving | close | 3k+ bets | 182-171 | 51.6 | -0.8 | -5.1 |  |
| money_level+sharp_gap | close | 3k+ bets | 177-168 | 51.3 | -0.7 | -4.3 |  |
| follow_move+money_level | close | 3k+ bets | 151-117 | 56.3 | 0.2 | -5.3 |  |
| money_level+rlm_ratio | close | 3k+ bets | 26-15 | 63.4 | 15.7 | 29.5 |  |
| consensus_gap+money_level | close | 3k+ bets | 65-59 | 52.4 | -5.1 | -11.2 |  |
| money_level+pin_move | close | 3k+ bets | 84-85 | 49.7 | -4.3 | -10.3 |  |
| money_level+pin_value | close | 3k+ bets | 58-67 | 46.4 | -4.3 | -13.7 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 10-16 | 38.5 | -0.9 | -8.7 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 74-102 | 42.0 | -0.3 | -10.3 |  |
| money_delta+money_moving | close | 3k+ bets | 78-105 | 42.6 | -0.1 | -1.1 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 29-46 | 38.7 | -2.0 | -13.2 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 40-57 | 41.2 | -0.8 | -11.0 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 37-57 | 39.4 | -2.9 | -15.1 |  |
| consensus_gap+money_delta | close | 3k+ bets | 15-26 | 36.6 | -3.5 | 15.0 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 18-35 | 34.0 | -8.0 | -27.8 |  |
| money_delta+sharp_gap | close | 3k+ bets | 76-102 | 42.7 | 0.1 | -0.6 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 44-53 | 45.4 | 2.2 | -3.0 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 17-30 | 36.2 | -4.4 | -17.4 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 10-18 | 35.7 | -13.6 | -32.0 |  |
| money_delta+money_level | close | 3k+ bets | 36-29 | 55.4 | 8.5 | 11.5 |  |
| money_level+pin_rlm | close | 3k+ bets | 16-11 | 59.3 | 13.5 | 26.8 |  |
| money_delta+pin_value | close | 3k+ bets | 22-22 | 50.0 | 2.8 | -5.5 |  |
| money_delta+pin_move | close | 3k+ bets | 44-53 | 45.4 | -0.1 | -8.1 |  |
| money_delta+pin_rlm | close | 3k+ bets | 27-34 | 44.3 | 1.9 | -6.5 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 35-34 | 50.7 | 6.8 | 7.0 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 47.0 | 87.7 |  |
| money_level+money_moving | close | <1k bets | 110-95 | 53.7 | 1.2 | -8.2 |  |
| money_level+sharp_gap | close | <1k bets | 113-96 | 54.1 | 1.3 | -8.3 |  |
| money_moving+sharp_gap | close | <1k bets | 154-171 | 47.4 | -0.6 | -10.5 |  |
| consensus_gap+money_level | close | <1k bets | 31-28 | 52.5 | -3.9 | -18.5 |  |
| consensus_gap+money_moving | close | <1k bets | 25-41 | 37.9 | -5.9 | -19.1 |  |
| consensus_gap+pin_move | close | <1k bets | 8-13 | 38.1 | -12.6 | -17.2 |  |
| consensus_gap+pin_value | close | <1k bets | 19-16 | 54.3 | 11.8 | 29.5 |  |
| consensus_gap+sharp_gap | close | <1k bets | 26-43 | 37.7 | -6.1 | -20.5 |  |
| money_level+pin_move | close | <1k bets | 48-44 | 52.2 | -0.8 | -6.6 |  |
| money_level+pin_value | close | <1k bets | 26-21 | 55.3 | 5.5 | 3.3 |  |
| money_moving+pin_move | close | <1k bets | 47-50 | 48.5 | 0.6 | -2.4 |  |
| money_moving+pin_value | close | <1k bets | 23-21 | 52.3 | 6.9 | 20.2 |  |
| pin_move+pin_value | close | <1k bets | 32-24 | 57.1 | 8.5 | 14.5 |  |
| pin_move+sharp_gap | close | <1k bets | 47-51 | 48.0 | -0.4 | -6.7 |  |
| pin_value+sharp_gap | close | <1k bets | 23-20 | 53.5 | 7.7 | 23.0 |  |
| follow_move+money_delta | close | <1k bets | 26-29 | 47.3 | 3.5 | -5.4 |  |
| follow_move+money_moving | close | <1k bets | 76-81 | 48.4 | -1.0 | -11.2 |  |
| follow_move+pin_move | close | <1k bets | 56-57 | 49.6 | -1.2 | -7.7 |  |
| follow_move+sharp_gap | close | <1k bets | 77-82 | 48.4 | -1.5 | -13.6 |  |
| money_delta+money_moving | close | <1k bets | 36-57 | 38.7 | -2.1 | -16.4 |  |
| money_delta+pin_move | close | <1k bets | 14-20 | 41.2 | -3.6 | -19.8 |  |
| money_delta+sharp_gap | close | <1k bets | 36-57 | 38.7 | -2.1 | -16.4 |  |
| follow_move+rlm_quiet | close | <1k bets | 32-47 | 40.5 | -1.5 | -16.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 36-38 | 48.6 | 5.2 | -3.3 |  |
| money_delta+rlm_quiet | close | <1k bets | 13-14 | 48.1 | 7.0 | -0.5 |  |
| money_delta+rlm_ratio | close | <1k bets | 21-22 | 48.8 | 6.3 | -1.2 |  |
| money_moving+rlm_quiet | close | <1k bets | 19-19 | 50.0 | 8.2 | 7.8 |  |
| money_moving+rlm_ratio | close | <1k bets | 36-38 | 48.6 | 5.2 | -3.3 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 15-16 | 48.4 | 7.6 | -0.6 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 18-20 | 47.4 | 5.0 | -3.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 36-38 | 48.6 | 5.2 | -3.3 |  |
| follow_move+money_level | close | <1k bets | 99-72 | 57.9 | 0.8 | -10.3 |  |
| consensus_gap+money_delta | close | <1k bets | 7-22 | 24.1 | -10.8 | -35.0 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -2.8 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 13-17 | 43.3 | 3.0 | -7.1 |  |
| money_moving+pin_rlm | close | <1k bets | 26-26 | 50.0 | 7.7 | 7.9 |  |
| pin_rlm+sharp_gap | close | <1k bets | 26-26 | 50.0 | 7.7 | 7.9 |  |
| money_delta+pin_value | close | <1k bets | 10-8 | 55.6 | 9.8 | 25.3 |  |
| consensus_gap+follow_move | close | <1k bets | 14-21 | 40.0 | -11.1 | -35.2 |  |
| follow_move+pin_rlm | close | <1k bets | 20-16 | 55.6 | 11.3 | 9.1 |  |
| follow_move+pin_value | close | <1k bets | 23-15 | 60.5 | 11.6 | 15.1 |  |
| pin_move+pin_rlm | close | <1k bets | 24-21 | 53.3 | 8.9 | 10.6 |  |
| pin_move+rlm_quiet | close | <1k bets | 13-14 | 48.1 | 2.3 | 2.3 |  |
| pin_move+rlm_ratio | close | <1k bets | 20-18 | 52.6 | 7.0 | 2.3 |  |
| pin_rlm+pin_value | close | <1k bets | 7-3 | 70.0 | 27.0 | 66.8 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 9-6 | 60.0 | 15.9 | 17.9 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 20-16 | 55.6 | 11.3 | 9.1 |  |
| pin_value+rlm_quiet | close | <1k bets | 6-4 | 60.0 | 10.8 | 15.0 |  |
| pin_value+rlm_ratio | close | <1k bets | 5-1 | 83.3 | 34.6 | 58.3 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -6.8 | -42.5 |  |
| money_delta+money_level | close | <1k bets | 15-20 | 42.9 | -0.5 | -14.3 |  |
| money_level+rlm_ratio | close | <1k bets | 17-17 | 50.0 | 5.0 | -2.7 |  |
| money_level+pin_rlm | close | <1k bets | 11-9 | 55.0 | 11.6 | 8.4 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-6 | 14.3 | -22.9 | -72.7 |  |
| consensus_gap+follow_move | close | pin $1-2k | 50-57 | 46.7 | -4.9 | -10.9 |  |
| consensus_gap+money_moving | close | pin $1-2k | 61-76 | 44.5 | -3.8 | -4.5 |  |
| consensus_gap+pin_move | close | pin $1-2k | 53-54 | 49.5 | -1.8 | 5.9 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 14-19 | 42.4 | 1.0 | 25.4 |  |
| consensus_gap+pin_value | close | pin $1-2k | 81-84 | 49.1 | 2.5 | -0.3 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 15-16 | 48.4 | 3.4 | 6.1 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 59-74 | 44.4 | -3.1 | -3.5 |  |
| follow_move+money_moving | close | pin $1-2k | 204-249 | 45.0 | -4.4 | -12.2 |  |
| follow_move+pin_move | close | pin $1-2k | 211-256 | 45.2 | -4.9 | -13.0 |  |
| follow_move+pin_rlm | close | pin $1-2k | 64-72 | 47.1 | 1.3 | -0.7 |  |
| follow_move+pin_value | close | pin $1-2k | 81-93 | 46.6 | -3.0 | -12.0 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 94-104 | 47.5 | 1.7 | -0.9 |  |
| follow_move+sharp_gap | close | pin $1-2k | 208-249 | 45.5 | -3.8 | -11.5 |  |
| money_moving+pin_move | close | pin $1-2k | 186-210 | 47.0 | -2.4 | -5.6 |  |
| money_moving+pin_rlm | close | pin $1-2k | 75-84 | 47.2 | 2.5 | 7.0 |  |
| money_moving+pin_value | close | pin $1-2k | 90-121 | 42.7 | -5.4 | -15.5 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 92-97 | 48.7 | 2.5 | 1.5 |  |
| money_moving+sharp_gap | close | pin $1-2k | 363-398 | 47.7 | -1.1 | -5.2 |  |
| pin_move+pin_rlm | close | pin $1-2k | 75-82 | 47.8 | 2.5 | 6.0 |  |
| pin_move+pin_value | close | pin $1-2k | 97-120 | 44.7 | -5.1 | -14.1 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 72-75 | 49.0 | 2.2 | 1.9 |  |
| pin_move+sharp_gap | close | pin $1-2k | 188-215 | 46.7 | -2.3 | -6.4 |  |
| pin_rlm+pin_value | close | pin $1-2k | 19-30 | 38.8 | -9.4 | -19.6 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 64-72 | 47.1 | 1.3 | -0.7 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 78-91 | 46.2 | 2.0 | 4.4 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 21-25 | 45.7 | -3.4 | -12.8 |  |
| pin_value+sharp_gap | close | pin $1-2k | 90-118 | 43.3 | -4.7 | -14.3 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 94-104 | 47.5 | 1.7 | -0.9 |  |
| follow_move+money_level | close | pin $1-2k | 223-219 | 50.5 | -3.4 | -11.4 |  |
| money_level+rlm_ratio | close | pin $1-2k | 49-42 | 53.8 | 5.9 | 4.8 |  |
| money_level+sharp_gap | close | pin $1-2k | 267-262 | 50.5 | -1.1 | -6.7 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 5-15 | 25.0 | -15.6 | -30.7 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 77-131 | 37.0 | -6.7 | -18.6 |  |
| money_level+money_moving | close | pin $1-2k | 271-265 | 50.6 | -1.2 | -6.9 |  |
| consensus_gap+money_level | close | pin $1-2k | 79-70 | 53.0 | -3.2 | -7.1 |  |
| money_level+pin_value | close | pin $1-2k | 105-105 | 50.0 | 0.1 | -6.5 |  |
| money_level+pin_move | close | pin $1-2k | 179-179 | 50.0 | -2.4 | -8.9 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 40-61 | 39.6 | -4.3 | -8.1 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 54-78 | 40.9 | -4.6 | -9.5 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 25-42 | 37.3 | -7.0 | -12.6 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 33-52 | 38.8 | -4.5 | -9.0 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 41-63 | 39.4 | -4.5 | -10.3 |  |
| money_level+pin_rlm | close | pin $1-2k | 35-30 | 53.8 | 7.5 | 5.7 |  |
| follow_move+money_delta | close | pin $1-2k | 73-81 | 47.4 | 0.8 | -3.4 |  |
| money_delta+money_moving | close | pin $1-2k | 101-112 | 47.4 | 2.8 | 2.7 |  |
| money_delta+pin_move | close | pin $1-2k | 72-79 | 47.7 | 0.3 | -0.1 |  |
| money_delta+pin_rlm | close | pin $1-2k | 46-53 | 46.5 | 2.5 | 4.8 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 53-54 | 49.5 | 3.8 | 3.2 |  |
| money_delta+sharp_gap | close | pin $1-2k | 101-110 | 47.9 | 3.2 | 3.7 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 47.0 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 53-46 | 53.5 | 5.4 | 4.1 |  |
| consensus_gap+money_delta | close | pin $1-2k | 20-26 | 43.5 | 1.7 | 7.4 |  |
| money_delta+pin_value | close | pin $1-2k | 46-47 | 49.5 | 1.3 | -2.0 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 23-40 | 36.5 | -7.6 | -18.4 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 14-32 | 30.4 | -18.4 | -40.5 |  |
| consensus_gap+follow_move | close | pin $2k+ | 44-35 | 55.7 | 2.5 | -5.6 |  |
| consensus_gap+money_delta | close | pin $2k+ | 12-28 | 30.0 | -6.0 | -41.4 |  |
| consensus_gap+money_level | close | pin $2k+ | 92-67 | 57.9 | -4.4 | -9.9 |  |
| consensus_gap+money_moving | close | pin $2k+ | 50-79 | 38.8 | -7.5 | -6.0 |  |
| consensus_gap+pin_move | close | pin $2k+ | 47-40 | 54.0 | 3.6 | 3.8 |  |
| consensus_gap+pin_value | close | pin $2k+ | 54-60 | 47.4 | 3.1 | 7.5 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 4-15 | 21.1 | -13.4 | -52.3 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 51-83 | 38.1 | -8.5 | -6.5 |  |
| follow_move+money_delta | close | pin $2k+ | 42-53 | 44.2 | 2.7 | -8.9 |  |
| follow_move+money_level | close | pin $2k+ | 178-120 | 59.7 | 0.8 | -4.2 |  |
| follow_move+money_moving | close | pin $2k+ | 150-154 | 49.3 | 1.8 | -5.5 |  |
| follow_move+pin_move | close | pin $2k+ | 195-186 | 51.2 | 1.8 | -2.8 |  |
| follow_move+pin_value | close | pin $2k+ | 44-42 | 51.2 | 3.3 | 8.0 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 53-77 | 40.8 | 2.9 | -9.8 |  |
| follow_move+sharp_gap | close | pin $2k+ | 147-154 | 48.8 | 1.4 | -5.8 |  |
| money_delta+money_level | close | pin $2k+ | 30-24 | 55.6 | 10.8 | 12.7 |  |
| money_delta+money_moving | close | pin $2k+ | 76-106 | 41.8 | 2.5 | -8.9 |  |
| money_delta+pin_move | close | pin $2k+ | 44-59 | 42.7 | 0.3 | -13.1 |  |
| money_delta+pin_value | close | pin $2k+ | 24-25 | 49.0 | 3.9 | -6.5 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 26-38 | 40.6 | 2.2 | -13.0 |  |
| money_delta+sharp_gap | close | pin $2k+ | 74-105 | 41.3 | 2.1 | -9.7 |  |
| money_level+money_moving | close | pin $2k+ | 205-193 | 51.5 | -1.5 | -6.8 |  |
| money_level+pin_move | close | pin $2k+ | 131-112 | 53.9 | -1.9 | -6.1 |  |
| money_level+pin_value | close | pin $2k+ | 70-75 | 48.3 | -1.8 | -10.6 |  |
| money_level+rlm_ratio | close | pin $2k+ | 19-17 | 52.8 | 6.8 | 8.5 |  |
| money_level+sharp_gap | close | pin $2k+ | 202-196 | 50.8 | -2.2 | -7.4 |  |
| money_moving+pin_move | close | pin $2k+ | 129-144 | 47.3 | 0.5 | -6.1 |  |
| money_moving+pin_value | close | pin $2k+ | 73-90 | 44.8 | -1.8 | -2.1 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 53-76 | 41.1 | 3.2 | -9.1 |  |
| money_moving+sharp_gap | close | pin $2k+ | 303-351 | 46.3 | -0.3 | -4.8 |  |
| pin_move+pin_value | close | pin $2k+ | 66-65 | 50.4 | 1.7 | -2.2 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 39-54 | 41.9 | 3.0 | -5.7 |  |
| pin_move+sharp_gap | close | pin $2k+ | 128-146 | 46.7 | -0.0 | -6.6 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 6-7 | 46.2 | 2.1 | -8.8 |  |
| pin_value+sharp_gap | close | pin $2k+ | 73-93 | 44.0 | -2.8 | -3.9 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 53-77 | 40.8 | 2.9 | -9.8 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 9-24 | 27.3 | -6.6 | -13.7 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 7-16 | 30.4 | -0.9 | -31.5 |  |
| follow_move+pin_rlm | close | pin $2k+ | 39-61 | 39.0 | 2.5 | -10.8 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 91-110 | 45.3 | 7.0 | 3.5 |  |
| money_moving+pin_rlm | close | pin $2k+ | 54-88 | 38.0 | 2.1 | -4.4 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 41-59 | 41.0 | 5.1 | -7.7 |  |
| pin_move+pin_rlm | close | pin $2k+ | 44-63 | 41.1 | 3.5 | -5.4 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 60-77 | 43.8 | 3.8 | -3.5 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 21-44 | 32.3 | -0.1 | -21.1 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 39-61 | 39.0 | 2.5 | -10.8 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 54-89 | 37.8 | 1.9 | -5.1 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 28-51 | 35.4 | 2.7 | -16.2 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 40-59 | 40.4 | 4.4 | -9.4 |  |
| money_delta+pin_rlm | close | pin $2k+ | 30-48 | 38.5 | 2.1 | -9.3 |  |
| money_level+pin_rlm | close | pin $2k+ | 17-13 | 56.7 | 13.0 | 19.4 |  |
| pin_rlm+pin_value | close | pin $2k+ | 9-14 | 39.1 | -0.7 | 18.6 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 23-32 | 41.8 | 3.7 | -13.4 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 8-10 | 44.4 | 3.7 | 40.9 |  |
| follow_move+money_delta | close | pin limit <$1k | 37-48 | 43.5 | -5.7 | -16.5 |  |
| money_level+money_moving | close | pin limit <$1k | 98-103 | 48.8 | -1.1 | -6.7 |  |
| money_level+sharp_gap | close | pin limit <$1k | 93-97 | 48.9 | -0.9 | -6.3 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 138-156 | 46.9 | -2.5 | -7.0 |  |
| consensus_gap+money_level | close | pin limit <$1k | 33-31 | 51.6 | 0.9 | -4.4 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 18-14 | 56.2 | 7.6 | 19.9 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 43-43 | 50.0 | 0.5 | -0.7 |  |
| follow_move+money_moving | close | pin limit <$1k | 86-100 | 46.2 | -3.2 | -11.2 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 90-99 | 47.6 | -1.8 | -8.6 |  |
| money_level+pin_move | close | pin limit <$1k | 72-61 | 54.1 | 4.2 | 3.3 |  |
| money_level+pin_value | close | pin limit <$1k | 66-45 | 59.5 | 9.3 | 12.6 |  |
| pin_move+pin_value | close | pin limit <$1k | 55-37 | 59.8 | 9.9 | 18.5 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 22-15 | 59.5 | 9.9 | 10.1 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 27-27 | 50.0 | 1.3 | 2.9 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 29-29 | 50.0 | 1.1 | 2.2 |  |
| follow_move+money_level | close | pin limit <$1k | 78-72 | 52.0 | 1.7 | -1.5 |  |
| follow_move+pin_move | close | pin limit <$1k | 82-82 | 50.0 | 0.4 | -4.2 |  |
| follow_move+pin_value | close | pin limit <$1k | 48-31 | 60.8 | 10.9 | 15.4 |  |
| money_moving+pin_move | close | pin limit <$1k | 77-80 | 49.0 | -0.4 | -3.4 |  |
| money_moving+pin_value | close | pin limit <$1k | 51-42 | 54.8 | 5.3 | 8.9 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 78-80 | 49.4 | -0.0 | -2.8 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 52-47 | 52.5 | 2.9 | 4.2 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 50-54 | 48.1 | -1.3 | -7.7 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 28-36 | 43.8 | -5.4 | -16.1 |  |
| money_delta+money_moving | close | pin limit <$1k | 52-58 | 47.3 | -1.9 | -5.4 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 10-8 | 55.6 | 8.2 | 30.0 |  |
| money_delta+money_level | close | pin limit <$1k | 26-25 | 51.0 | 1.3 | -2.3 |  |
| money_delta+pin_value | close | pin limit <$1k | 19-10 | 65.5 | 16.3 | 39.8 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 51-56 | 47.7 | -1.5 | -4.6 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 33-40 | 45.2 | -3.7 | -7.2 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 7-4 | 63.6 | 17.5 | 61.2 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 27-24 | 52.9 | 4.4 | 10.3 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 46-39 | 54.1 | 5.4 | 14.3 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 48-41 | 53.9 | 4.9 | 8.4 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 20-7 | 74.1 | 25.0 | 57.7 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 49-41 | 54.4 | 5.6 | 14.3 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 7-4 | 63.6 | 15.8 | 21.7 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 15-10 | 60.0 | 10.2 | 14.8 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 12-21 | 36.4 | -12.2 | -30.2 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 26-31 | 45.6 | -3.5 | -12.2 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 39-33 | 54.2 | 5.0 | 4.2 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 54-50 | 51.9 | 2.8 | 0.1 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 30-31 | 49.2 | 0.1 | -5.4 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 22-35 | 38.6 | -10.4 | -25.8 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 49-47 | 51.0 | 2.0 | -1.5 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 39-33 | 54.2 | 5.0 | 4.2 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 15-16 | 48.4 | -0.1 | -6.9 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 39-33 | 54.2 | 5.0 | 4.2 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 24-28 | 46.2 | -2.8 | -11.4 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 54-50 | 51.9 | 2.8 | 0.1 |  |
| money_level+pin_rlm | close | pin limit <$1k | 24-16 | 60.0 | 10.3 | 15.1 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 26-19 | 57.8 | 8.5 | 12.1 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 18-8 | 69.2 | 19.4 | 32.5 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 7-6 | 53.8 | 5.6 | 2.9 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 50.4 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.6 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -51.7 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 53-60 | 46.9 | 10.5 | 14.1 | 0.54 |
| rlm_quiet | early | pin $1-2k | 3-7 | 30.0 | -1.0 | 7.2 | -0.12 |
| rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.6 | -100.0 | 1.3 |
| rlm_quiet | early | pin limit <$1k | 6-8 | 42.9 | -2.3 | -13.5 | 0.23 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.4 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 11-19 | 36.7 | -11.6 | -31.9 | 0.24 |
| pin_move | early | pin $1-2k | 1-5 | 16.7 | -25.2 | -67.6 | -0.05 |
| pin_move | early | pin limit <$1k | 10-15 | 40.0 | -9.9 | -26.0 | 0.26 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 12-11 | 52.2 | 13.5 | 22.6 | 0.98 |
| money_delta | early | pin $1-2k | 0-3 | 0.0 | -36.7 | -100.0 | 2.17 |
| money_delta | early | pin limit <$1k | 5-0 | 100.0 | 50.8 | 88.6 | 0.0 |
| pin_rlm | early | <1k bets | 1-4 | 20.0 | -17.1 | -61.5 | -0.3 |
| pin_rlm | early | pin $1-2k | 0-3 | 0.0 | -42.9 | -100.0 | -0.67 |
| pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 21.4 | -3.7 | 0.25 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.6 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -51.7 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 586-533 | 52.4 | 1.5 | -6.2 | 0.14 |
| follow_move | early | pin $1-2k | 40-29 | 58.0 | 7.4 | 7.3 | -0.33 |
| follow_move | early | pin $2k+ | 0-2 | 0.0 | -40.8 | -100.0 | 0.65 |
| follow_move | early | pin limit <$1k | 58-59 | 49.6 | -0.4 | -6.8 | -0.13 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 22.9 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.0 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 33-29 | 53.2 | 14.5 | 20.8 | 0.52 |
| rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.5 | 29.7 | -1.02 |
| rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.8 | -100.0 | 0.65 |
| rlm_ratio | early | pin limit <$1k | 8-2 | 80.0 | 36.6 | 61.1 | 0.33 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 1.5 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 44.0 | 59.7 | 0.33 |
| money_level | early | <1k bets | 212-150 | 58.6 | -0.3 | -7.6 | -0.24 |
| money_level | early | pin $1-2k | 24-13 | 64.9 | 1.3 | -2.9 | -0.05 |
| money_level | early | pin $2k+ | 1-1 | 50.0 | -12.2 | -47.2 | -0.7 |
| money_level | early | pin limit <$1k | 31-32 | 49.2 | -2.8 | -8.4 | 0.26 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.2 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.7 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 171-161 | 51.5 | 2.3 | -1.1 | 0.31 |
| sharp_gap | early | pin $1-2k | 18-17 | 51.4 | -3.8 | -6.9 | -0.3 |
| sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.8 | -100.0 | 0.65 |
| sharp_gap | early | pin limit <$1k | 35-23 | 60.3 | 11.8 | 23.4 | 0.18 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.5 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 51.7 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 123-112 | 52.3 | 1.7 | -6.0 | 0.24 |
| money_moving | early | pin $1-2k | 8-13 | 38.1 | -18.9 | -47.8 | 0.36 |
| money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.2 | -8.4 | 0.65 |
| money_moving | early | pin limit <$1k | 32-11 | 74.4 | 24.6 | 52.7 | 0.41 |
| pin_value | early | 1-3k bets | 13-10 | 56.5 | 8.3 | 6.3 | -0.04 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.0 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 57-57 | 50.0 | 1.0 | -5.4 | 0.1 |
| pin_value | early | pin $1-2k | 19-28 | 40.4 | -6.9 | -24.0 | 0.16 |
| pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.0 | 83.3 | 0.0 |
| pin_value | early | pin limit <$1k | 51-39 | 56.7 | 7.0 | 7.3 | 0.04 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -50.4 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -27.1 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.1 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.2 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 285-333 | 46.1 | -3.5 | -12.3 | 0.44 |
| consensus_gap | early | pin $1-2k | 22-25 | 46.8 | -0.5 | -11.9 | 0.29 |
| consensus_gap | early | pin $2k+ | 1-1 | 50.0 | 12.2 | -8.4 | 0.65 |
| consensus_gap | early | pin limit <$1k | 26-38 | 40.6 | -9.5 | -17.9 | 0.24 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -53.0 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -1.7 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.7 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 5.4 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.3 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 7-4 | 63.6 | 14.3 | 19.4 | -0.09 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.1 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.8 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.4 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -0.7 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 6-5 | 54.5 | 8.4 | 1.3 | 0.27 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -1.4 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-7 | 50.0 | 2.9 | -6.4 | -0.29 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.6 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.7 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -20.0 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -3.0 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 3.5 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.5 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 22.9 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.4 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 22.9 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.3 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.3 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.3 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.3 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 53.0 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 11.4 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 18.0 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 16.0 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 16.0 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -28.6 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 53.0 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 53.0 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.0 | 83.3 | 1.0 |
| follow_move+rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -51.7 | -100.0 | -0.5 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.0 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.0 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 51.7 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.0 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 53.0 | 83.3 | 1.0 |
| rlm_quiet+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -53.0 | -100.0 | -1.0 |
| rlm_quiet+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.0 | -100.0 | -1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -53.0 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 39.5 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 50.4 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 41-52 | 44.1 | -9.3 | -21.9 | 0.87 |
| consensus_gap+money_level | early | <1k bets | 51-38 | 57.3 | -6.8 | -12.0 | -0.06 |
| consensus_gap+sharp_gap | early | <1k bets | 37-53 | 41.1 | -9.7 | -19.5 | 0.54 |
| follow_move+money_level | early | <1k bets | 102-51 | 66.7 | 6.7 | -1.3 | 0.03 |
| follow_move+sharp_gap | early | <1k bets | 87-53 | 62.1 | 12.6 | 13.0 | 0.53 |
| money_level+sharp_gap | early | <1k bets | 116-84 | 58.0 | 1.7 | -4.9 | 0.04 |
| follow_move+money_moving | early | <1k bets | 60-42 | 58.8 | 7.3 | 6.5 | 0.46 |
| money_level+money_moving | early | <1k bets | 70-51 | 57.9 | 0.3 | -6.4 | -0.04 |
| money_moving+sharp_gap | early | <1k bets | 70-68 | 50.7 | 2.4 | -4.2 | 0.46 |
| consensus_gap+money_moving | early | <1k bets | 20-24 | 45.5 | -5.9 | -27.0 | 0.59 |
| follow_move+pin_value | early | <1k bets | 17-15 | 53.1 | 3.5 | -0.2 | -0.17 |
| follow_move+rlm_quiet | early | <1k bets | 53-60 | 46.9 | 10.5 | 14.1 | 0.54 |
| money_moving+rlm_quiet | early | <1k bets | 18-18 | 50.0 | 12.8 | 22.1 | 0.69 |
| rlm_quiet+sharp_gap | early | <1k bets | 26-22 | 54.2 | 16.5 | 25.4 | 0.22 |
| follow_move+rlm_ratio | early | <1k bets | 33-29 | 53.2 | 14.5 | 20.8 | 0.52 |
| rlm_quiet+rlm_ratio | early | <1k bets | 23-17 | 57.5 | 20.6 | 36.2 | 0.16 |
| rlm_ratio+sharp_gap | early | <1k bets | 33-29 | 53.2 | 14.5 | 20.8 | 0.52 |
| pin_move+pin_value | early | <1k bets | 4-10 | 28.6 | -20.7 | -45.1 | 0.36 |
| follow_move+pin_move | early | <1k bets | 7-9 | 43.8 | -5.2 | -20.3 | 0.28 |
| consensus_gap+pin_value | early | <1k bets | 23-26 | 46.9 | -0.6 | -11.8 | 0.25 |
| pin_value+rlm_quiet | early | <1k bets | 0-3 | 0.0 | -43.7 | -100.0 | -0.6 |
| money_delta+money_moving | early | <1k bets | 11-11 | 50.0 | 11.8 | 19.5 | 1.02 |
| money_delta+sharp_gap | early | <1k bets | 10-9 | 52.6 | 15.2 | 28.3 | 1.18 |
| consensus_gap+pin_move | early | <1k bets | 2-6 | 25.0 | -21.9 | -51.7 | 0.29 |
| money_level+pin_move | early | <1k bets | 4-6 | 40.0 | -9.9 | -30.2 | 0.14 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -28.6 | -100.0 | -4.8 |
| consensus_gap+rlm_quiet | early | <1k bets | 4-6 | 40.0 | 3.0 | -12.2 | 1.03 |
| consensus_gap+rlm_ratio | early | <1k bets | 5-3 | 62.5 | 20.8 | 25.0 | 0.65 |
| follow_move+pin_rlm | early | <1k bets | 1-3 | 25.0 | -14.3 | -51.8 | -0.7 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -28.6 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | <1k bets | 0-1 | 0.0 | -28.6 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-3 | 25.0 | -14.3 | -51.8 | -0.7 |
| pin_rlm+sharp_gap | early | <1k bets | 1-4 | 20.0 | -17.1 | -61.5 | -0.3 |
| pin_value+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 24.1 | 27.3 | -0.93 |
| pin_value+sharp_gap | early | <1k bets | 6-8 | 42.9 | -7.2 | -18.2 | 0.42 |
| money_level+pin_value | early | <1k bets | 7-7 | 50.0 | -1.7 | -4.5 | 0.84 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -51.3 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -49.6 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 4-4 | 50.0 | -3.3 | -4.0 | 1.21 |
| money_level+rlm_ratio | early | <1k bets | 8-12 | 40.0 | -1.4 | -17.1 | 1.32 |
| money_moving+rlm_ratio | early | <1k bets | 16-11 | 59.3 | 19.0 | 39.9 | 0.95 |
| consensus_gap+money_delta | early | <1k bets | 2-0 | 100.0 | 50.0 | 90.9 | 0.5 |
| money_delta+money_level | early | <1k bets | 4-4 | 50.0 | 8.2 | 4.6 | 1.44 |
| pin_move+sharp_gap | early | <1k bets | 2-4 | 33.3 | -13.3 | -47.8 | 0.47 |
| money_level+pin_rlm | early | <1k bets | 1-2 | 33.3 | -9.5 | -35.8 | 0.67 |
| pin_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 21.4 | -3.7 | 0.25 |
| pin_move+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 21.4 | -3.7 | 0.25 |
| follow_move+money_delta | early | <1k bets | 6-5 | 54.5 | 16.4 | 52.8 | 1.28 |
| money_delta+rlm_quiet | early | <1k bets | 3-3 | 50.0 | 17.9 | 72.5 | 0.38 |
| money_delta+rlm_ratio | early | <1k bets | 5-3 | 62.5 | 26.1 | 86.2 | 2.04 |
| money_delta+pin_value | early | <1k bets | 2-0 | 100.0 | 50.4 | 90.9 | 0.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -28.6 | -100.0 | 1.3 |
| money_moving+pin_move | early | <1k bets | 1-1 | 50.0 | 0.4 | -2.4 | 1.0 |
| consensus_gap+money_level | early | pin $1-2k | 7-5 | 58.3 | -7.0 | -9.8 | 0.07 |
| consensus_gap+money_moving | early | pin $1-2k | 1-3 | 25.0 | -40.3 | -54.2 | 0.95 |
| consensus_gap+pin_value | early | pin $1-2k | 8-11 | 42.1 | -1.0 | -22.3 | 0.14 |
| follow_move+rlm_quiet | early | pin $1-2k | 3-7 | 30.0 | -1.0 | 7.2 | -0.12 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.5 | 29.7 | -1.02 |
| follow_move+sharp_gap | early | pin $1-2k | 9-6 | 60.0 | 2.9 | 19.2 | -0.62 |
| money_level+money_moving | early | pin $1-2k | 8-8 | 50.0 | -13.0 | -31.4 | 0.26 |
| money_level+pin_value | early | pin $1-2k | 2-4 | 33.3 | -18.8 | -37.6 | 0.78 |
| money_moving+pin_value | early | pin $1-2k | 1-4 | 20.0 | -34.8 | -63.3 | 0.94 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -9.7 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -9.7 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -10.5 | 29.7 | -1.02 |
| money_delta+money_level | early | pin $1-2k | 0-2 | 0.0 | -40.8 | -100.0 | 1.25 |
| money_delta+money_moving | early | pin $1-2k | 0-3 | 0.0 | -36.7 | -100.0 | 2.17 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -53.0 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-3 | 0.0 | -36.7 | -100.0 | 2.17 |
| money_level+sharp_gap | early | pin $1-2k | 15-9 | 62.5 | -0.9 | -4.8 | -0.23 |
| money_moving+sharp_gap | early | pin $1-2k | 4-10 | 28.6 | -27.6 | -61.0 | 0.36 |
| pin_value+sharp_gap | early | pin $1-2k | 1-4 | 20.0 | -30.6 | -61.8 | -0.22 |
| consensus_gap+follow_move | early | pin $1-2k | 6-7 | 46.2 | -2.2 | -11.3 | 0.4 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 1-3 | 25.0 | -3.6 | -35.0 | -0.65 |
| follow_move+pin_value | early | pin $1-2k | 6-7 | 46.2 | -1.5 | -14.7 | -0.25 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -28.6 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 12-6 | 66.7 | 3.0 | -0.4 | -0.03 |
| money_level+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -12.2 | -1.0 | 0.75 |
| follow_move+money_moving | early | pin $1-2k | 4-3 | 57.1 | -7.7 | -23.6 | -0.13 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -28.6 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -28.6 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 4-5 | 44.4 | -12.7 | -31.7 | -0.69 |
| follow_move+pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -28.6 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | pin $1-2k | 0-1 | 0.0 | -28.6 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-3 | 0.0 | -42.9 | -100.0 | -0.67 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -28.6 | -100.0 | -4.8 |
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -28.6 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -28.6 | -100.0 | 1.3 |
| pin_move+pin_value | early | pin $1-2k | 0-2 | 0.0 | -47.0 | -100.0 | 0.0 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -71.4 | -100.0 | 1.5 |
| follow_move+pin_move | early | pin $1-2k | 1-1 | 50.0 | 3.0 | -2.9 | -0.5 |
| money_level+pin_move | early | pin $1-2k | 1-0 | 100.0 | 53.0 | 94.3 | -1.0 |
| consensus_gap+money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.2 | -8.4 | 0.65 |
| consensus_gap+pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.0 | 83.3 | 0.0 |
| follow_move+money_level | early | pin $2k+ | 0-1 | 0.0 | -53.0 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.8 | -100.0 | 0.65 |
| follow_move+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.8 | -100.0 | 0.65 |
| money_level+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -53.0 | -100.0 | 0.0 |
| money_level+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -53.0 | -100.0 | 0.0 |
| money_moving+pin_value | early | pin $2k+ | 1-0 | 100.0 | 53.0 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.8 | -100.0 | 0.65 |
| consensus_gap+follow_move | early | pin $2k+ | 0-1 | 0.0 | -28.6 | -100.0 | 1.3 |
| consensus_gap+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.6 | -100.0 | 1.3 |
| consensus_gap+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.6 | -100.0 | 1.3 |
| consensus_gap+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.6 | -100.0 | 1.3 |
| follow_move+money_moving | early | pin $2k+ | 0-1 | 0.0 | -28.6 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.6 | -100.0 | 1.3 |
| money_moving+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.6 | -100.0 | 1.3 |
| money_moving+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.6 | -100.0 | 1.3 |
| money_moving+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.6 | -100.0 | 1.3 |
| rlm_quiet+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.6 | -100.0 | 1.3 |
| rlm_quiet+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.6 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin limit <$1k | 6-8 | 42.9 | -2.3 | -13.5 | 0.23 |
| money_level+money_moving | early | pin limit <$1k | 17-7 | 70.8 | 19.2 | 32.1 | 0.48 |
| money_level+sharp_gap | early | pin limit <$1k | 25-20 | 55.6 | 5.6 | 2.6 | 0.24 |
| money_moving+sharp_gap | early | pin limit <$1k | 23-6 | 79.3 | 30.9 | 68.0 | 0.31 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -50.4 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 12-8 | 60.0 | 10.0 | 14.0 | 0.4 |
| money_moving+pin_value | early | pin limit <$1k | 10-4 | 71.4 | 21.8 | 35.6 | 0.36 |
| pin_value+sharp_gap | early | pin limit <$1k | 13-8 | 61.9 | 12.1 | 17.4 | 0.19 |
| consensus_gap+follow_move | early | pin limit <$1k | 7-10 | 41.2 | -10.2 | -23.2 | 0.41 |
| consensus_gap+money_level | early | pin limit <$1k | 6-7 | 46.2 | -8.3 | -19.0 | 0.31 |
| consensus_gap+pin_value | early | pin limit <$1k | 21-20 | 51.2 | 2.0 | -3.4 | 0.33 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 7-4 | 63.6 | 18.1 | 56.6 | 0.91 |
| follow_move+money_level | early | pin limit <$1k | 14-14 | 50.0 | -1.9 | -6.7 | -0.03 |
| follow_move+pin_value | early | pin limit <$1k | 18-15 | 54.5 | 5.2 | 2.9 | -0.18 |
| follow_move+sharp_gap | early | pin limit <$1k | 16-10 | 61.5 | 13.6 | 17.7 | -0.02 |
| follow_move+rlm_ratio | early | pin limit <$1k | 8-2 | 80.0 | 36.6 | 61.1 | 0.33 |
| money_level+rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.1 | 68.3 | 0.44 |
| pin_value+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.2 | 43.2 | -0.25 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 8-2 | 80.0 | 36.6 | 61.1 | 0.33 |
| consensus_gap+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 51.0 | 87.1 | 0.33 |
| consensus_gap+money_moving | early | pin limit <$1k | 10-3 | 76.9 | 29.1 | 76.9 | 0.65 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 1.7 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 51.0 | 87.1 | 0.33 |
| follow_move+money_moving | early | pin limit <$1k | 13-5 | 72.2 | 22.8 | 38.2 | 0.39 |
| money_delta+money_moving | early | pin limit <$1k | 4-0 | 100.0 | 50.8 | 88.0 | 0.0 |
| money_delta+pin_value | early | pin limit <$1k | 4-0 | 100.0 | 50.8 | 88.0 | 0.0 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 53.0 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 4-2 | 66.7 | 17.4 | 26.0 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 30.1 | 54.4 | -0.2 |
| money_delta+sharp_gap | early | pin limit <$1k | 3-0 | 100.0 | 50.1 | 89.6 | 0.0 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 10.5 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | 5.5 | 13.7 | -0.05 |
| pin_move+pin_value | early | pin limit <$1k | 4-8 | 33.3 | -16.3 | -36.0 | 0.42 |
| follow_move+pin_move | early | pin limit <$1k | 6-8 | 42.9 | -6.4 | -22.8 | 0.39 |
| consensus_gap+pin_move | early | pin limit <$1k | 2-4 | 33.3 | -19.7 | -35.7 | 0.43 |
| money_level+pin_move | early | pin limit <$1k | 3-6 | 33.3 | -16.9 | -44.0 | 0.27 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -49.6 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -49.6 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-4 | 33.3 | -13.3 | -47.8 | 0.47 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 21.4 | -3.7 | 0.25 |
| money_level+pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 21.4 | -3.7 | 0.25 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 21.4 | -3.7 | 0.25 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 21.4 | -3.7 | 0.25 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 21.4 | -3.7 | 0.25 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 21.4 | -3.7 | 0.25 |
| money_delta+money_level | early | pin limit <$1k | 2-0 | 100.0 | 50.4 | 90.9 | 0.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 50.4 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 50.4 | 90.9 | 1.0 |
| money_moving+pin_move | early | pin limit <$1k | 1-1 | 50.0 | 0.4 | -2.4 | 1.0 |
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
| rlm_quiet | close | 1-3k bets | 68-106 | 39.1 | -4.0 | -10.1 |  |
| rlm_quiet | close | 3k+ bets | 30-42 | 41.7 | -1.1 | -13.5 |  |
| rlm_quiet | close | <1k bets | 10-19 | 34.5 | -8.6 | -33.2 |  |
| rlm_quiet | close | pin $1-2k | 31-50 | 38.3 | -6.4 | -20.5 |  |
| rlm_quiet | close | pin $2k+ | 38-47 | 44.7 | 4.1 | 10.6 |  |
| rlm_quiet | close | pin limit <$1k | 14-18 | 43.8 | -4.0 | -15.4 |  |
| pin_move | close | 1-3k bets | 126-137 | 47.9 | -1.3 | -4.0 |  |
| pin_move | close | 3k+ bets | 49-56 | 46.7 | -3.4 | -11.4 |  |
| pin_move | close | <1k bets | 20-19 | 51.3 | 1.6 | -3.3 |  |
| pin_move | close | pin $1-2k | 79-102 | 43.6 | -5.8 | -14.5 |  |
| pin_move | close | pin $2k+ | 82-77 | 51.6 | 2.1 | 2.7 |  |
| pin_move | close | pin limit <$1k | 34-33 | 50.7 | 1.3 | -2.8 |  |
| money_delta | close | 1-3k bets | 58-75 | 43.6 | -0.5 | -11.3 |  |
| money_delta | close | 3k+ bets | 27-26 | 50.9 | 6.0 | 0.7 |  |
| money_delta | close | <1k bets | 14-14 | 50.0 | 5.3 | 11.4 |  |
| money_delta | close | pin $1-2k | 39-33 | 54.2 | 7.7 | 11.5 |  |
| money_delta | close | pin $2k+ | 24-26 | 48.0 | 6.4 | -2.7 |  |
| money_delta | close | pin limit <$1k | 12-18 | 40.0 | -7.5 | -23.0 |  |
| pin_rlm | close | 1-3k bets | 26-39 | 40.0 | -1.8 | -13.1 |  |
| pin_rlm | close | 3k+ bets | 10-16 | 38.5 | -3.3 | -20.2 |  |
| pin_rlm | close | <1k bets | 5-5 | 50.0 | 2.4 | -4.9 |  |
| pin_rlm | close | pin $1-2k | 17-25 | 40.5 | -3.7 | -15.3 |  |
| pin_rlm | close | pin $2k+ | 16-23 | 41.0 | 3.4 | -8.3 |  |
| pin_rlm | close | pin limit <$1k | 8-12 | 40.0 | -7.7 | -23.0 |  |
| follow_move | close | 1-3k bets | 195-229 | 46.0 | -3.2 | -10.0 |  |
| follow_move | close | 3k+ bets | 74-73 | 50.3 | 1.3 | -6.7 |  |
| follow_move | close | <1k bets | 44-46 | 48.9 | -1.0 | -13.1 |  |
| follow_move | close | pin $1-2k | 91-122 | 42.7 | -6.5 | -18.9 |  |
| follow_move | close | pin $2k+ | 97-93 | 51.1 | 2.2 | 2.8 |  |
| follow_move | close | pin limit <$1k | 41-40 | 50.6 | 0.9 | -4.1 |  |
| rlm_ratio | close | 1-3k bets | 44-70 | 38.6 | -3.8 | -17.6 |  |
| rlm_ratio | close | 3k+ bets | 15-25 | 37.5 | -4.9 | -22.0 |  |
| rlm_ratio | close | <1k bets | 10-12 | 45.5 | 1.0 | -12.8 |  |
| rlm_ratio | close | pin $1-2k | 24-31 | 43.6 | -0.6 | -9.9 |  |
| rlm_ratio | close | pin $2k+ | 15-24 | 38.5 | 0.9 | -15.0 |  |
| rlm_ratio | close | pin limit <$1k | 10-16 | 38.5 | -9.5 | -26.2 |  |
| money_level | close | 1-3k bets | 256-199 | 56.3 | 1.2 | -4.2 |  |
| money_level | close | 3k+ bets | 88-84 | 51.2 | -3.6 | -12.3 |  |
| money_level | close | <1k bets | 60-31 | 65.9 | 11.1 | 9.2 |  |
| money_level | close | pin $1-2k | 120-111 | 51.9 | -1.5 | -8.7 |  |
| money_level | close | pin $2k+ | 106-96 | 52.5 | -4.2 | -13.1 |  |
| money_level | close | pin limit <$1k | 51-36 | 58.6 | 7.0 | 10.7 |  |
| sharp_gap | close | 1-3k bets | 198-227 | 46.6 | -1.9 | -10.6 |  |
| sharp_gap | close | 3k+ bets | 68-94 | 42.0 | -6.2 | -18.4 |  |
| sharp_gap | close | <1k bets | 46-39 | 54.1 | 4.8 | -0.8 |  |
| sharp_gap | close | pin $1-2k | 103-111 | 48.1 | -0.6 | -6.9 |  |
| sharp_gap | close | pin $2k+ | 85-106 | 44.5 | -3.2 | -12.2 |  |
| sharp_gap | close | pin limit <$1k | 35-46 | 43.2 | -6.4 | -17.5 |  |
| money_moving | close | 1-3k bets | 208-222 | 48.4 | -0.4 | -7.6 |  |
| money_moving | close | 3k+ bets | 71-92 | 43.6 | -5.4 | -17.6 |  |
| money_moving | close | <1k bets | 46-37 | 55.4 | 5.9 | 1.5 |  |
| money_moving | close | pin $1-2k | 108-107 | 50.2 | 1.0 | -4.1 |  |
| money_moving | close | pin $2k+ | 89-103 | 46.4 | -1.5 | -9.4 |  |
| money_moving | close | pin limit <$1k | 39-47 | 45.3 | -4.3 | -13.4 |  |
| pin_value | close | 1-3k bets | 107-89 | 54.6 | 4.8 | 8.9 |  |
| pin_value | close | 3k+ bets | 24-43 | 35.8 | -14.8 | -32.0 |  |
| pin_value | close | <1k bets | 18-14 | 56.2 | 8.9 | 17.6 |  |
| pin_value | close | pin $1-2k | 70-67 | 51.1 | 1.6 | 0.6 |  |
| pin_value | close | pin $2k+ | 44-50 | 46.8 | -2.6 | -1.9 |  |
| pin_value | close | pin limit <$1k | 35-29 | 54.7 | 4.2 | 4.0 |  |
| consensus_gap | close | 1-3k bets | 83-69 | 54.6 | 2.3 | 0.4 |  |
| consensus_gap | close | 3k+ bets | 29-25 | 53.7 | -0.8 | -9.2 |  |
| consensus_gap | close | <1k bets | 18-8 | 69.2 | 18.4 | 29.9 |  |
| consensus_gap | close | pin $1-2k | 30-27 | 52.6 | 0.8 | 7.0 |  |
| consensus_gap | close | pin $2k+ | 57-28 | 67.1 | 10.8 | 20.1 |  |
| consensus_gap | close | pin limit <$1k | 9-13 | 40.9 | -7.9 | -22.0 |  |
| follow_move+pin_move | close | 1-3k bets | 80-111 | 41.9 | -6.9 | -17.9 |  |
| money_delta+money_moving | close | 1-3k bets | 47-55 | 46.1 | 3.3 | -5.1 |  |
| money_delta+sharp_gap | close | 1-3k bets | 47-54 | 46.5 | 3.8 | -4.1 |  |
| money_moving+sharp_gap | close | 1-3k bets | 192-213 | 47.4 | -1.2 | -8.6 |  |
| consensus_gap+money_level | close | 1-3k bets | 51-37 | 58.0 | 0.0 | -8.1 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 68-106 | 39.1 | -4.0 | -10.1 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 31-51 | 37.8 | -6.4 | -16.6 |  |
| consensus_gap+follow_move | close | 1-3k bets | 20-26 | 43.5 | -6.5 | -19.2 |  |
| follow_move+money_level | close | 1-3k bets | 96-85 | 53.0 | -1.9 | -8.2 |  |
| money_level+money_moving | close | 1-3k bets | 146-128 | 53.3 | 0.6 | -4.0 |  |
| money_level+sharp_gap | close | 1-3k bets | 138-128 | 51.9 | -0.6 | -6.1 |  |
| consensus_gap+money_moving | close | 1-3k bets | 25-35 | 41.7 | -8.2 | -19.7 |  |
| consensus_gap+pin_move | close | 1-3k bets | 23-14 | 62.2 | 13.1 | 36.6 |  |
| consensus_gap+pin_value | close | 1-3k bets | 29-27 | 51.8 | 2.6 | -1.8 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 25-37 | 40.3 | -9.2 | -22.4 |  |
| follow_move+money_moving | close | 1-3k bets | 100-123 | 44.8 | -3.4 | -12.4 |  |
| follow_move+pin_value | close | 1-3k bets | 33-27 | 55.0 | 5.0 | 20.4 |  |
| follow_move+sharp_gap | close | 1-3k bets | 100-126 | 44.2 | -4.0 | -13.9 |  |
| money_level+pin_move | close | 1-3k bets | 57-50 | 53.3 | -0.0 | -4.9 |  |
| money_level+pin_value | close | 1-3k bets | 46-38 | 54.8 | 4.4 | 2.6 |  |
| money_moving+pin_move | close | 1-3k bets | 60-62 | 49.2 | 1.0 | -3.4 |  |
| money_moving+pin_value | close | 1-3k bets | 39-40 | 49.4 | -0.2 | -6.8 |  |
| pin_move+pin_value | close | 1-3k bets | 39-39 | 50.0 | -1.1 | -5.3 |  |
| pin_move+sharp_gap | close | 1-3k bets | 57-68 | 45.6 | -2.2 | -10.3 |  |
| pin_value+sharp_gap | close | 1-3k bets | 38-43 | 46.9 | -2.8 | -11.5 |  |
| follow_move+money_delta | close | 1-3k bets | 31-48 | 39.2 | -5.0 | -20.2 |  |
| money_delta+pin_move | close | 1-3k bets | 21-25 | 45.7 | 1.7 | -9.6 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 16-34 | 32.0 | -10.0 | -31.8 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 44-70 | 38.6 | -3.8 | -17.6 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 29-52 | 35.8 | -5.2 | -19.0 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 43-64 | 40.2 | -2.4 | -14.0 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 21-48 | 30.4 | -9.7 | -29.1 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 28-55 | 33.7 | -7.4 | -24.1 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 44-70 | 38.6 | -3.8 | -17.6 |  |
| money_delta+money_level | close | 1-3k bets | 18-14 | 56.2 | 8.2 | 10.4 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 5-12 | 29.4 | -9.2 | -31.8 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 6-8 | 42.9 | 3.2 | -4.0 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 22-38 | 36.7 | -5.5 | -23.5 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 5-3 | 62.5 | 20.1 | 47.4 |  |
| money_level+pin_rlm | close | 1-3k bets | 10-10 | 50.0 | 4.2 | -2.2 |  |
| money_moving+pin_rlm | close | 1-3k bets | 26-34 | 43.3 | 1.1 | -5.9 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 26-39 | 40.0 | -1.8 | -13.1 |  |
| money_level+rlm_ratio | close | 1-3k bets | 19-17 | 52.8 | 6.2 | 2.8 |  |
| consensus_gap+money_delta | close | 1-3k bets | 8-6 | 57.1 | 16.2 | 14.0 |  |
| follow_move+pin_rlm | close | 1-3k bets | 21-33 | 38.9 | -2.7 | -14.5 |  |
| money_delta+pin_rlm | close | 1-3k bets | 14-20 | 41.2 | 0.1 | -16.9 |  |
| pin_move+pin_rlm | close | 1-3k bets | 25-33 | 43.1 | 0.9 | -6.7 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 22-30 | 42.3 | -0.4 | -8.6 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 11-24 | 31.4 | -8.4 | -23.6 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 21-33 | 38.9 | -2.7 | -14.5 |  |
| money_delta+pin_value | close | 1-3k bets | 13-7 | 65.0 | 17.3 | 25.6 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 7-10 | 41.2 | -5.7 | 38.9 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 5-5 | 50.0 | 2.1 | -1.2 |  |
| pin_rlm+pin_value | close | 1-3k bets | 4-6 | 40.0 | -8.2 | -19.3 |  |
| money_level+money_moving | close | 3k+ bets | 40-50 | 44.4 | -8.5 | -19.9 |  |
| money_level+sharp_gap | close | 3k+ bets | 36-50 | 41.9 | -10.5 | -21.7 |  |
| money_moving+sharp_gap | close | 3k+ bets | 67-90 | 42.7 | -5.7 | -17.6 |  |
| follow_move+money_delta | close | 3k+ bets | 12-16 | 42.9 | -1.3 | -14.9 |  |
| follow_move+money_level | close | 3k+ bets | 32-27 | 54.2 | -1.7 | -12.2 |  |
| follow_move+money_moving | close | 3k+ bets | 40-46 | 46.5 | -2.1 | -13.7 |  |
| follow_move+pin_move | close | 3k+ bets | 37-42 | 46.8 | -2.4 | -10.8 |  |
| follow_move+pin_rlm | close | 3k+ bets | 9-14 | 39.1 | -1.8 | -18.0 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 15-25 | 37.5 | -4.9 | -22.0 |  |
| follow_move+sharp_gap | close | 3k+ bets | 37-45 | 45.1 | -2.4 | -12.1 |  |
| money_delta+money_level | close | 3k+ bets | 5-7 | 41.7 | -7.4 | -19.5 |  |
| money_delta+money_moving | close | 3k+ bets | 18-22 | 45.0 | 1.4 | -10.1 |  |
| money_delta+pin_move | close | 3k+ bets | 9-11 | 45.0 | -1.1 | -12.4 |  |
| money_delta+pin_rlm | close | 3k+ bets | 6-7 | 46.2 | 2.0 | -6.4 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 7-10 | 41.2 | -1.5 | -16.8 |  |
| money_delta+sharp_gap | close | 3k+ bets | 18-22 | 45.0 | 1.4 | -10.1 |  |
| money_level+pin_move | close | 3k+ bets | 18-24 | 42.9 | -13.2 | -27.7 |  |
| money_level+pin_rlm | close | 3k+ bets | 1-2 | 33.3 | -16.9 | -34.9 |  |
| money_level+rlm_ratio | close | 3k+ bets | 3-3 | 50.0 | -0.5 | -3.8 |  |
| money_moving+pin_move | close | 3k+ bets | 22-32 | 40.7 | -9.0 | -24.2 |  |
| money_moving+pin_rlm | close | 3k+ bets | 10-15 | 40.0 | -2.1 | -17.0 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 14-25 | 35.9 | -6.7 | -27.0 |  |
| pin_move+pin_rlm | close | 3k+ bets | 8-14 | 36.4 | -7.0 | -27.3 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 8-14 | 36.4 | -6.8 | -27.2 |  |
| pin_move+sharp_gap | close | 3k+ bets | 20-32 | 38.5 | -10.6 | -25.9 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 9-14 | 39.1 | -1.8 | -18.0 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 10-16 | 38.5 | -3.3 | -20.2 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 15-25 | 37.5 | -4.9 | -22.0 |  |
| consensus_gap+money_level | close | 3k+ bets | 21-15 | 58.3 | -1.2 | -6.1 |  |
| consensus_gap+money_moving | close | 3k+ bets | 11-16 | 40.7 | -10.5 | -28.1 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 10-17 | 37.0 | -13.0 | -32.4 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 30-42 | 41.7 | -1.1 | -13.5 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 18-23 | 43.9 | 0.7 | -7.9 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 8-11 | 42.1 | 0.2 | -15.0 |  |
| money_level+pin_value | close | 3k+ bets | 13-24 | 35.1 | -16.8 | -33.9 |  |
| money_moving+pin_value | close | 3k+ bets | 12-22 | 35.3 | -16.4 | -33.7 |  |
| pin_value+sharp_gap | close | 3k+ bets | 12-23 | 34.3 | -17.9 | -35.6 |  |
| consensus_gap+follow_move | close | 3k+ bets | 10-8 | 55.6 | 3.1 | -9.2 |  |
| consensus_gap+pin_value | close | 3k+ bets | 9-11 | 45.0 | -7.0 | -14.4 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 16-26 | 38.1 | -5.3 | -23.9 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 17-25 | 40.5 | -2.6 | -17.5 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 6-13 | 31.6 | -8.5 | -33.3 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 10-22 | 31.2 | -9.6 | -33.9 |  |
| pin_move+pin_value | close | 3k+ bets | 15-22 | 40.5 | -10.5 | -23.1 |  |
| follow_move+pin_value | close | 3k+ bets | 10-15 | 40.0 | -10.5 | -24.2 |  |
| consensus_gap+money_delta | close | 3k+ bets | 3-3 | 50.0 | 3.5 | -5.1 |  |
| consensus_gap+pin_move | close | 3k+ bets | 12-9 | 57.1 | 5.1 | -0.2 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 3-4 | 42.9 | -0.2 | -17.6 |  |
| money_delta+pin_value | close | 3k+ bets | 4-3 | 57.1 | 4.1 | 9.1 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 3-6 | 33.3 | -16.6 | -37.1 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 2-4 | 33.3 | -12.7 | -36.9 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 1-3 | 25.0 | -16.5 | -52.3 |  |
| pin_rlm+pin_value | close | 3k+ bets | 2-3 | 40.0 | -11.6 | -24.3 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 1-2 | 33.3 | -15.9 | -36.4 |  |
| consensus_gap+money_level | close | <1k bets | 13-1 | 92.9 | 35.1 | 48.5 |  |
| consensus_gap+money_moving | close | <1k bets | 8-1 | 88.9 | 35.7 | 81.0 |  |
| consensus_gap+pin_value | close | <1k bets | 5-2 | 71.4 | 28.5 | 85.8 |  |
| consensus_gap+sharp_gap | close | <1k bets | 9-2 | 81.8 | 29.2 | 60.9 |  |
| follow_move+pin_move | close | <1k bets | 14-15 | 48.3 | -1.8 | -9.0 |  |
| follow_move+rlm_quiet | close | <1k bets | 10-19 | 34.5 | -8.6 | -33.2 |  |
| money_level+money_moving | close | <1k bets | 34-18 | 65.4 | 12.3 | 10.0 |  |
| money_level+pin_value | close | <1k bets | 8-4 | 66.7 | 18.2 | 24.9 |  |
| money_level+sharp_gap | close | <1k bets | 34-19 | 64.2 | 10.8 | 8.1 |  |
| money_moving+pin_value | close | <1k bets | 6-5 | 54.5 | 9.4 | 36.2 |  |
| money_moving+sharp_gap | close | <1k bets | 44-36 | 55.0 | 5.9 | 2.4 |  |
| pin_move+rlm_quiet | close | <1k bets | 3-4 | 42.9 | -5.5 | -18.6 |  |
| pin_value+sharp_gap | close | <1k bets | 6-5 | 54.5 | 9.4 | 36.2 |  |
| follow_move+money_moving | close | <1k bets | 22-18 | 55.0 | 5.7 | -3.6 |  |
| follow_move+sharp_gap | close | <1k bets | 21-19 | 52.5 | 3.2 | -5.9 |  |
| money_level+pin_move | close | <1k bets | 14-9 | 60.9 | 10.4 | 14.1 |  |
| money_moving+rlm_quiet | close | <1k bets | 5-7 | 41.7 | -1.6 | -19.1 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 5-7 | 41.7 | -1.6 | -19.1 |  |
| follow_move+money_delta | close | <1k bets | 8-9 | 47.1 | 1.4 | -10.3 |  |
| follow_move+pin_rlm | close | <1k bets | 4-5 | 44.4 | -3.2 | -15.5 |  |
| follow_move+pin_value | close | <1k bets | 5-3 | 62.5 | 13.0 | 19.9 |  |
| follow_move+rlm_ratio | close | <1k bets | 10-12 | 45.5 | 1.0 | -12.8 |  |
| money_delta+money_moving | close | <1k bets | 9-11 | 45.0 | 2.5 | 8.2 |  |
| money_delta+pin_move | close | <1k bets | 1-3 | 25.0 | -22.8 | -52.3 |  |
| money_delta+pin_rlm | close | <1k bets | 1-3 | 25.0 | -22.8 | -52.3 |  |
| money_delta+pin_value | close | <1k bets | 4-0 | 100.0 | 55.9 | 181.8 |  |
| money_delta+rlm_quiet | close | <1k bets | 5-4 | 55.6 | 11.9 | 7.3 |  |
| money_delta+rlm_ratio | close | <1k bets | 5-7 | 41.7 | -2.2 | -20.7 |  |
| money_delta+sharp_gap | close | <1k bets | 9-11 | 45.0 | 2.5 | 8.2 |  |
| money_moving+pin_move | close | <1k bets | 11-9 | 55.0 | 7.0 | 4.3 |  |
| money_moving+pin_rlm | close | <1k bets | 5-5 | 50.0 | 2.4 | -4.9 |  |
| money_moving+rlm_ratio | close | <1k bets | 10-12 | 45.5 | 1.0 | -12.8 |  |
| pin_move+pin_rlm | close | <1k bets | 5-5 | 50.0 | 2.4 | -4.9 |  |
| pin_move+pin_value | close | <1k bets | 7-4 | 63.6 | 14.2 | 20.8 |  |
| pin_move+rlm_ratio | close | <1k bets | 4-5 | 44.4 | -3.2 | -15.5 |  |
| pin_move+sharp_gap | close | <1k bets | 11-9 | 55.0 | 7.0 | 4.3 |  |
| pin_rlm+pin_value | close | <1k bets | 2-0 | 100.0 | 52.2 | 90.9 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 2-1 | 66.7 | 17.4 | 26.2 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 4-5 | 44.4 | -3.2 | -15.5 |  |
| pin_rlm+sharp_gap | close | <1k bets | 5-5 | 50.0 | 2.4 | -4.9 |  |
| pin_value+rlm_quiet | close | <1k bets | 3-0 | 100.0 | 52.2 | 90.9 |  |
| pin_value+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 52.2 | 90.9 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 5-6 | 45.5 | 2.7 | -11.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 10-12 | 45.5 | 1.0 | -12.8 |  |
| consensus_gap+follow_move | close | <1k bets | 5-1 | 83.3 | 28.4 | 42.8 |  |
| consensus_gap+pin_move | close | <1k bets | 2-0 | 100.0 | 42.6 | 70.5 |  |
| follow_move+money_level | close | <1k bets | 24-13 | 64.9 | 9.8 | 7.3 |  |
| money_delta+money_level | close | <1k bets | 3-3 | 50.0 | 7.6 | 7.7 |  |
| money_level+pin_rlm | close | <1k bets | 2-3 | 40.0 | -6.6 | -23.6 |  |
| money_level+rlm_ratio | close | <1k bets | 4-4 | 50.0 | 5.2 | -5.5 |  |
| consensus_gap+money_delta | close | <1k bets | 3-0 | 100.0 | 50.7 | 208.0 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 52.2 | 89.3 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-1 | 50.0 | 9.6 | -4.5 |  |
| money_delta+money_moving | close | pin $1-2k | 24-20 | 54.5 | 10.2 | 16.9 |  |
| money_delta+sharp_gap | close | pin $1-2k | 24-20 | 54.5 | 10.2 | 16.9 |  |
| money_moving+sharp_gap | close | pin $1-2k | 100-102 | 49.5 | 0.5 | -4.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 9-11 | 45.0 | -5.7 | -16.3 |  |
| consensus_gap+money_level | close | pin $1-2k | 16-14 | 53.3 | -2.2 | -10.1 |  |
| consensus_gap+money_moving | close | pin $1-2k | 8-12 | 40.0 | -8.7 | -11.1 |  |
| consensus_gap+pin_move | close | pin $1-2k | 11-11 | 50.0 | 1.5 | 10.9 |  |
| consensus_gap+pin_value | close | pin $1-2k | 16-14 | 53.3 | 4.5 | 14.0 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 8-12 | 40.0 | -8.7 | -9.8 |  |
| follow_move+money_level | close | pin $1-2k | 45-50 | 47.4 | -5.8 | -16.3 |  |
| follow_move+money_moving | close | pin $1-2k | 52-62 | 45.6 | -3.2 | -12.6 |  |
| follow_move+pin_move | close | pin $1-2k | 47-84 | 35.9 | -13.0 | -30.2 |  |
| follow_move+pin_value | close | pin $1-2k | 25-26 | 49.0 | -0.7 | -6.9 |  |
| follow_move+sharp_gap | close | pin $1-2k | 53-65 | 44.9 | -3.9 | -13.7 |  |
| money_level+money_moving | close | pin $1-2k | 75-69 | 52.1 | 0.3 | -6.3 |  |
| money_level+pin_move | close | pin $1-2k | 37-46 | 44.6 | -7.2 | -19.4 |  |
| money_level+pin_value | close | pin $1-2k | 31-28 | 52.5 | 2.6 | -2.0 |  |
| money_level+sharp_gap | close | pin $1-2k | 70-70 | 50.0 | -1.4 | -8.8 |  |
| money_moving+pin_move | close | pin $1-2k | 42-47 | 47.2 | -2.3 | -9.4 |  |
| money_moving+pin_value | close | pin $1-2k | 25-24 | 51.0 | 2.2 | 3.7 |  |
| pin_move+pin_value | close | pin $1-2k | 27-33 | 45.0 | -5.8 | -14.8 |  |
| pin_move+sharp_gap | close | pin $1-2k | 41-53 | 43.6 | -5.0 | -15.5 |  |
| pin_value+sharp_gap | close | pin $1-2k | 25-24 | 51.0 | 2.2 | 3.7 |  |
| follow_move+money_delta | close | pin $1-2k | 19-24 | 44.2 | -2.6 | -13.4 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 31-50 | 38.3 | -6.4 | -20.5 |  |
| money_delta+pin_move | close | pin $1-2k | 14-16 | 46.7 | 0.4 | -7.9 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 11-15 | 42.3 | -3.2 | -16.3 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 21-32 | 39.6 | -6.1 | -17.0 |  |
| follow_move+pin_rlm | close | pin $1-2k | 15-22 | 40.5 | -4.2 | -14.6 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 24-31 | 43.6 | -0.6 | -9.9 |  |
| pin_move+pin_rlm | close | pin $1-2k | 17-22 | 43.6 | -1.5 | -8.8 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 15-21 | 41.7 | -3.9 | -12.2 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 10-16 | 38.5 | -5.9 | -15.6 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 15-22 | 40.5 | -4.2 | -14.6 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 17-25 | 40.5 | -3.7 | -15.3 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 13-20 | 39.4 | -4.1 | -15.3 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 17-23 | 42.5 | -1.5 | -10.7 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 24-31 | 43.6 | -0.6 | -9.9 |  |
| money_delta+money_level | close | pin $1-2k | 11-9 | 55.0 | 7.3 | 6.8 |  |
| money_delta+pin_rlm | close | pin $1-2k | 9-11 | 45.0 | 0.8 | -9.9 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 11-13 | 45.8 | 1.2 | -8.7 |  |
| money_level+pin_rlm | close | pin $1-2k | 6-7 | 46.2 | 1.3 | -10.0 |  |
| money_level+rlm_ratio | close | pin $1-2k | 9-9 | 50.0 | 4.3 | -3.6 |  |
| money_moving+pin_rlm | close | pin $1-2k | 17-20 | 45.9 | 0.6 | -3.9 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 24-27 | 47.1 | 2.2 | -2.8 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 17-22 | 43.6 | -0.4 | -8.4 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 2-4 | 33.3 | -6.5 | -28.5 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 6-10 | 37.5 | -10.6 | -24.9 |  |
| money_delta+pin_value | close | pin $1-2k | 9-5 | 64.3 | 18.8 | 51.2 |  |
| consensus_gap+money_delta | close | pin $1-2k | 4-1 | 80.0 | 37.3 | 132.7 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 1-2 | 33.3 | -6.0 | -20.7 |  |
| pin_rlm+pin_value | close | pin $1-2k | 4-5 | 44.4 | -3.5 | -10.4 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 3-4 | 42.9 | -4.1 | -12.0 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 1-1 | 50.0 | 7.4 | 19.0 |  |
| follow_move+pin_move | close | pin $2k+ | 62-62 | 50.0 | 0.9 | -3.4 |  |
| consensus_gap+money_level | close | pin $2k+ | 38-21 | 64.4 | 3.6 | -0.1 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 38-47 | 44.7 | 4.1 | 10.6 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 25-36 | 41.0 | -0.9 | -7.9 |  |
| money_level+money_moving | close | pin $2k+ | 55-60 | 47.8 | -5.3 | -14.2 |  |
| money_level+sharp_gap | close | pin $2k+ | 52-62 | 45.6 | -7.4 | -16.6 |  |
| money_moving+sharp_gap | close | pin $2k+ | 85-102 | 45.5 | -2.2 | -10.3 |  |
| consensus_gap+pin_value | close | pin $2k+ | 20-14 | 58.8 | 9.1 | 10.7 |  |
| follow_move+money_level | close | pin $2k+ | 39-32 | 54.9 | -3.2 | -11.1 |  |
| follow_move+money_moving | close | pin $2k+ | 43-50 | 46.2 | -1.3 | -11.2 |  |
| follow_move+sharp_gap | close | pin $2k+ | 39-49 | 44.3 | -2.9 | -13.2 |  |
| money_level+pin_move | close | pin $2k+ | 30-23 | 56.6 | -1.9 | -6.6 |  |
| money_moving+pin_move | close | pin $2k+ | 33-37 | 47.1 | 0.1 | -7.8 |  |
| pin_move+sharp_gap | close | pin $2k+ | 32-38 | 45.7 | -1.3 | -9.4 |  |
| money_delta+money_level | close | pin $2k+ | 6-3 | 66.7 | 20.7 | 35.6 |  |
| money_delta+money_moving | close | pin $2k+ | 20-26 | 43.5 | 3.1 | -11.0 |  |
| money_delta+sharp_gap | close | pin $2k+ | 20-26 | 43.5 | 3.1 | -11.0 |  |
| consensus_gap+money_moving | close | pin $2k+ | 19-18 | 51.4 | -1.4 | 0.8 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 18-19 | 48.6 | -4.1 | -2.4 |  |
| money_level+pin_value | close | pin $2k+ | 16-25 | 39.0 | -11.7 | -27.3 |  |
| money_moving+pin_value | close | pin $2k+ | 17-26 | 39.5 | -10.9 | -26.0 |  |
| pin_value+sharp_gap | close | pin $2k+ | 17-28 | 37.8 | -13.4 | -29.3 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 5-4 | 55.6 | 10.9 | 24.4 |  |
| money_level+pin_rlm | close | pin $2k+ | 2-4 | 33.3 | -13.0 | -32.5 |  |
| money_moving+pin_rlm | close | pin $2k+ | 16-22 | 42.1 | 4.4 | -5.9 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 16-23 | 41.0 | 3.4 | -8.3 |  |
| follow_move+money_delta | close | pin $2k+ | 11-15 | 42.3 | 1.9 | -14.9 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 15-24 | 38.5 | 0.9 | -15.0 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 7-14 | 33.3 | -5.0 | -31.4 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 15-24 | 38.5 | 0.9 | -15.0 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 15-24 | 38.5 | 0.9 | -15.0 |  |
| money_level+rlm_ratio | close | pin $2k+ | 5-4 | 55.6 | 10.1 | 7.2 |  |
| consensus_gap+follow_move | close | pin $2k+ | 17-7 | 70.8 | 14.1 | 20.6 |  |
| consensus_gap+pin_move | close | pin $2k+ | 23-8 | 74.2 | 21.7 | 44.2 |  |
| follow_move+pin_value | close | pin $2k+ | 11-11 | 50.0 | -0.5 | 38.2 |  |
| pin_move+pin_value | close | pin $2k+ | 20-20 | 50.0 | -1.5 | -5.6 |  |
| follow_move+pin_rlm | close | pin $2k+ | 12-19 | 38.7 | 3.2 | -11.1 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 12-19 | 38.7 | 3.2 | -11.1 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 4-3 | 57.1 | 9.4 | 146.6 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 15-23 | 39.5 | 1.1 | -11.1 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 14-22 | 38.9 | 0.2 | -13.3 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 7-12 | 36.8 | -1.5 | -24.6 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 8-18 | 30.8 | -3.6 | -26.0 |  |
| money_delta+pin_move | close | pin $2k+ | 13-13 | 50.0 | 7.9 | -1.5 |  |
| money_delta+pin_rlm | close | pin $2k+ | 9-12 | 42.9 | 4.1 | -12.2 |  |
| pin_move+pin_rlm | close | pin $2k+ | 13-18 | 41.9 | 4.3 | -7.5 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 12-17 | 41.4 | 3.4 | -10.1 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 8-16 | 33.3 | -1.2 | -19.8 |  |
| consensus_gap+money_delta | close | pin $2k+ | 5-2 | 71.4 | 23.7 | 37.7 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 3-3 | 50.0 | 10.9 | 20.3 |  |
| money_delta+pin_value | close | pin $2k+ | 6-3 | 66.7 | 13.5 | 26.6 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 4-2 | 66.7 | 25.6 | 51.1 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 2-0 | 100.0 | 48.5 | 87.8 |  |
| pin_rlm+pin_value | close | pin $2k+ | 3-1 | 75.0 | 21.7 | 42.4 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 4-5 | 44.4 | -3.2 | -14.6 |  |
| consensus_gap+money_level | close | pin limit <$1k | 5-6 | 45.5 | -6.7 | -14.2 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 5-10 | 33.3 | -14.8 | -36.0 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 7-12 | 36.8 | -12.7 | -30.2 |  |
| follow_move+money_level | close | pin limit <$1k | 24-18 | 57.1 | 6.0 | 7.1 |  |
| follow_move+money_moving | close | pin limit <$1k | 21-27 | 43.8 | -5.7 | -16.2 |  |
| follow_move+pin_value | close | pin limit <$1k | 12-8 | 60.0 | 9.2 | 14.3 |  |
| money_level+money_moving | close | pin limit <$1k | 29-27 | 51.8 | 0.8 | -1.4 |  |
| money_level+pin_value | close | pin limit <$1k | 20-13 | 60.6 | 8.9 | 15.1 |  |
| money_moving+pin_value | close | pin limit <$1k | 15-17 | 46.9 | -3.3 | -10.9 |  |
| follow_move+pin_move | close | pin limit <$1k | 22-22 | 50.0 | 0.7 | -3.9 |  |
| money_level+pin_move | close | pin limit <$1k | 22-14 | 61.1 | 10.5 | 16.6 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 34-43 | 44.2 | -5.4 | -15.7 |  |
| pin_move+pin_value | close | pin limit <$1k | 14-12 | 53.8 | 3.6 | 2.8 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 14-18 | 43.8 | -4.0 | -15.4 |  |
| money_moving+pin_move | close | pin limit <$1k | 18-19 | 48.6 | -0.6 | -6.9 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 3-2 | 60.0 | 15.2 | 16.4 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 3-4 | 42.9 | -4.1 | -16.9 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 1-2 | 33.3 | -9.5 | -33.3 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 3-3 | 50.0 | 4.7 | -3.0 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 2-3 | 40.0 | -4.8 | -21.8 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 5-11 | 31.2 | -16.9 | -40.0 |  |
| follow_move+money_delta | close | pin limit <$1k | 6-11 | 35.3 | -11.9 | -32.1 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 7-11 | 38.9 | -8.8 | -25.0 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 10-16 | 38.5 | -9.5 | -26.2 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 20-26 | 43.5 | -5.9 | -16.8 |  |
| money_delta+money_moving | close | pin limit <$1k | 9-13 | 40.9 | -6.4 | -21.1 |  |
| money_delta+pin_move | close | pin limit <$1k | 4-10 | 28.6 | -18.2 | -44.5 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 3-7 | 30.0 | -16.3 | -41.4 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 3-4 | 42.9 | -2.8 | -16.9 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 5-10 | 33.3 | -13.8 | -35.7 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 9-13 | 40.9 | -6.4 | -21.1 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 8-12 | 40.0 | -7.7 | -23.0 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 3-10 | 23.1 | -23.9 | -54.9 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 9-15 | 37.5 | -10.4 | -28.0 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 8-12 | 40.0 | -7.7 | -23.0 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 6-10 | 37.5 | -10.2 | -27.0 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 7-11 | 38.9 | -8.8 | -25.0 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 15-18 | 45.5 | -3.5 | -13.0 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 1-6 | 14.3 | -32.0 | -71.4 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 7-11 | 38.9 | -8.8 | -25.0 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 8-12 | 40.0 | -7.7 | -23.0 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 3-10 | 23.1 | -23.9 | -55.2 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 3-10 | 23.1 | -23.9 | -55.2 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 10-16 | 38.5 | -9.5 | -26.2 |  |
| money_delta+pin_value | close | pin limit <$1k | 6-2 | 75.0 | 26.6 | 43.2 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 3-3 | 50.0 | 2.2 | -4.5 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 2-3 | 40.0 | -8.7 | -24.4 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 14-19 | 42.4 | -7.7 | -19.4 |  |
| money_level+sharp_gap | close | pin limit <$1k | 25-26 | 49.0 | -1.9 | -6.7 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 1-3 | 25.0 | -22.8 | -52.3 |  |
| money_delta+money_level | close | pin limit <$1k | 1-6 | 14.3 | -33.5 | -72.1 |  |
| money_level+pin_rlm | close | pin limit <$1k | 5-4 | 55.6 | 6.8 | 6.5 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 5-5 | 50.0 | 1.3 | -4.1 |  |
| rlm_quiet | early | <1k bets | 26-32 | 44.8 | 6.2 | 7.1 | 0.82 |
| rlm_quiet | early | pin $1-2k | 2-2 | 50.0 | 17.1 | 23.0 | 1.12 |
| rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 2.2 | -4.5 | 0.0 |
| pin_move | early | <1k bets | 6-11 | 35.3 | -13.4 | -32.2 | 0.18 |
| pin_move | early | pin $1-2k | 1-2 | 33.3 | -11.6 | -35.2 | -0.33 |
| pin_move | early | pin limit <$1k | 5-9 | 35.7 | -13.7 | -31.5 | 0.29 |
| money_delta | early | <1k bets | 4-5 | 44.4 | 6.5 | 16.3 | 3.02 |
| money_delta | early | pin $1-2k | 0-1 | 0.0 | -32.9 | -100.0 | 1.5 |
| money_delta | early | pin limit <$1k | 1-0 | 100.0 | 52.2 | 90.9 | 1.0 |
| pin_rlm | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -32.9 | -100.0 | 0.0 |
| follow_move | early | <1k bets | 192-210 | 47.8 | -1.2 | -8.8 | 0.03 |
| follow_move | early | pin $1-2k | 13-12 | 52.0 | 5.9 | 3.6 | -0.32 |
| follow_move | early | pin limit <$1k | 11-20 | 35.5 | -13.5 | -30.8 | -0.18 |
| rlm_ratio | early | <1k bets | 10-16 | 38.5 | -2.9 | -7.6 | 0.4 |
| rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 9.6 | -4.5 | 0.5 |
| money_level | early | <1k bets | 72-61 | 54.1 | -3.3 | -13.1 | -0.39 |
| money_level | early | pin $1-2k | 3-5 | 37.5 | -22.5 | -38.8 | -0.29 |
| money_level | early | pin limit <$1k | 7-6 | 53.8 | 3.8 | 3.1 | 0.38 |
| sharp_gap | early | <1k bets | 55-63 | 46.6 | -3.6 | -11.3 | 0.25 |
| sharp_gap | early | pin $1-2k | 2-6 | 25.0 | -36.3 | -63.1 | -0.04 |
| sharp_gap | early | pin limit <$1k | 6-5 | 54.5 | 5.7 | 4.5 | 0.45 |
| money_moving | early | <1k bets | 45-43 | 51.1 | 2.0 | -3.0 | 0.62 |
| money_moving | early | pin $1-2k | 0-4 | 0.0 | -55.5 | -100.0 | 1.05 |
| money_moving | early | pin limit <$1k | 9-2 | 81.8 | 31.5 | 54.5 | 0.36 |
| pin_value | early | <1k bets | 21-18 | 53.8 | 4.2 | 1.7 | 0.04 |
| pin_value | early | pin $1-2k | 6-9 | 40.0 | -9.1 | -24.9 | 0.25 |
| pin_value | early | pin limit <$1k | 15-9 | 62.5 | 12.6 | 18.4 | -0.08 |
| consensus_gap | early | <1k bets | 110-97 | 53.1 | 0.3 | -7.1 | 0.59 |
| consensus_gap | early | pin $1-2k | 10-5 | 66.7 | 16.2 | 23.1 | -0.17 |
| consensus_gap | early | pin limit <$1k | 8-4 | 66.7 | 16.3 | 26.7 | 0.08 |
| follow_move+money_level | early | <1k bets | 26-18 | 59.1 | 2.1 | -11.2 | 0.11 |
| follow_move+sharp_gap | early | <1k bets | 24-26 | 48.0 | -0.0 | -6.0 | 0.62 |
| money_level+sharp_gap | early | <1k bets | 37-37 | 50.0 | -5.8 | -16.5 | -0.17 |
| follow_move+money_moving | early | <1k bets | 19-19 | 50.0 | 2.3 | 0.4 | 0.67 |
| money_level+money_moving | early | <1k bets | 21-17 | 55.3 | 0.0 | -4.8 | 0.49 |
| consensus_gap+money_level | early | <1k bets | 24-17 | 58.5 | -3.0 | -12.7 | -0.54 |
| follow_move+rlm_quiet | early | <1k bets | 26-32 | 44.8 | 6.2 | 7.1 | 0.82 |
| follow_move+rlm_ratio | early | <1k bets | 10-16 | 38.5 | -2.9 | -7.6 | 0.4 |
| rlm_quiet+rlm_ratio | early | <1k bets | 9-10 | 47.4 | 8.2 | 16.3 | 0.32 |
| rlm_quiet+sharp_gap | early | <1k bets | 10-12 | 45.5 | 5.1 | 9.2 | 0.5 |
| rlm_ratio+sharp_gap | early | <1k bets | 10-16 | 38.5 | -2.9 | -7.6 | 0.4 |
| consensus_gap+follow_move | early | <1k bets | 15-19 | 44.1 | -10.9 | -26.3 | 0.91 |
| money_moving+rlm_quiet | early | <1k bets | 9-10 | 47.4 | 8.2 | 15.7 | 0.91 |
| money_moving+rlm_ratio | early | <1k bets | 7-6 | 53.8 | 13.5 | 31.1 | 1.58 |
| money_moving+sharp_gap | early | <1k bets | 24-28 | 46.2 | -0.9 | -4.6 | 0.93 |
| consensus_gap+money_moving | early | <1k bets | 10-5 | 66.7 | 11.6 | 6.5 | 1.23 |
| consensus_gap+sharp_gap | early | <1k bets | 15-15 | 50.0 | -7.0 | -21.3 | -0.38 |
| money_level+rlm_ratio | early | <1k bets | 1-6 | 14.3 | -33.1 | -72.7 | 0.64 |
| follow_move+pin_move | early | <1k bets | 2-6 | 25.0 | -21.3 | -51.9 | 0.12 |
| follow_move+money_delta | early | <1k bets | 3-2 | 60.0 | 21.1 | 71.2 | 2.74 |
| money_delta+money_level | early | <1k bets | 1-3 | 25.0 | -15.4 | -52.3 | 1.68 |
| money_delta+money_moving | early | <1k bets | 4-5 | 44.4 | 6.5 | 16.3 | 3.02 |
| money_delta+rlm_ratio | early | <1k bets | 3-2 | 60.0 | 21.1 | 71.2 | 2.74 |
| money_delta+sharp_gap | early | <1k bets | 4-5 | 44.4 | 6.5 | 16.3 | 3.02 |
| follow_move+pin_value | early | <1k bets | 4-4 | 50.0 | 1.3 | -4.5 | -0.62 |
| consensus_gap+pin_move | early | <1k bets | 2-1 | 66.7 | 15.0 | 28.7 | 0.33 |
| consensus_gap+pin_value | early | <1k bets | 10-3 | 76.9 | 27.8 | 45.4 | -0.15 |
| money_level+pin_move | early | <1k bets | 2-4 | 33.3 | -14.4 | -35.8 | 0.17 |
| money_level+pin_value | early | <1k bets | 3-3 | 50.0 | -3.9 | -4.5 | 0.78 |
| pin_move+pin_value | early | <1k bets | 3-6 | 33.3 | -16.3 | -35.9 | 0.44 |
| money_moving+pin_value | early | <1k bets | 3-2 | 60.0 | 6.9 | 15.4 | 1.14 |
| pin_value+sharp_gap | early | <1k bets | 1-4 | 20.0 | -34.9 | -61.8 | 1.34 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 52.2 | 90.9 | 1.0 |
| consensus_gap+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 52.2 | 90.9 | 1.0 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 52.2 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 52.2 | 90.9 | 1.0 |
| follow_move+pin_rlm | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| money_level+pin_rlm | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_rlm+rlm_ratio | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_rlm+sharp_gap | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_move+sharp_gap | early | <1k bets | 0-3 | 0.0 | -45.8 | -100.0 | 1.0 |
| money_delta+rlm_quiet | early | <1k bets | 2-1 | 66.7 | 33.7 | 121.7 | 3.57 |
| consensus_gap+rlm_quiet | early | <1k bets | 1-1 | 50.0 | 17.1 | 30.0 | 1.1 |
| money_moving+pin_move | early | <1k bets | 1-1 | 50.0 | 2.2 | -2.4 | 1.0 |
| pin_move+pin_rlm | early | <1k bets | 0-1 | 0.0 | -32.9 | -100.0 | 0.0 |
| pin_move+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -32.9 | -100.0 | 0.0 |
| pin_move+pin_value | early | pin $1-2k | 0-2 | 0.0 | -44.9 | -100.0 | 0.0 |
| follow_move+rlm_quiet | early | pin $1-2k | 2-2 | 50.0 | 17.1 | 23.0 | 1.12 |
| money_level+money_moving | early | pin $1-2k | 0-3 | 0.0 | -55.7 | -100.0 | 1.07 |
| money_level+pin_value | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.7 |
| money_level+sharp_gap | early | pin $1-2k | 2-5 | 28.6 | -33.6 | -57.8 | -0.19 |
| money_moving+pin_value | early | pin $1-2k | 0-2 | 0.0 | -61.1 | -100.0 | 1.35 |
| money_moving+sharp_gap | early | pin $1-2k | 0-4 | 0.0 | -55.5 | -100.0 | 1.05 |
| pin_value+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -61.1 | -100.0 | 1.35 |
| consensus_gap+pin_value | early | pin $1-2k | 3-1 | 75.0 | 27.6 | 39.3 | -0.5 |
| follow_move+money_level | early | pin $1-2k | 1-2 | 33.3 | -26.3 | -35.2 | 0.17 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| follow_move+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| follow_move+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -67.1 | -100.0 | 0.75 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| money_level+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 1.5 |
| consensus_gap+follow_move | early | pin $1-2k | 2-1 | 66.7 | 22.4 | 55.3 | 0.6 |
| follow_move+pin_move | early | pin $1-2k | 1-1 | 50.0 | 5.1 | -2.9 | -0.5 |
| follow_move+pin_value | early | pin $1-2k | 0-1 | 0.0 | -44.9 | -100.0 | 0.0 |
| consensus_gap+money_level | early | pin $1-2k | 2-1 | 66.7 | -0.4 | -1.6 | -1.83 |
| consensus_gap+sharp_gap | early | pin $1-2k | 2-1 | 66.7 | -0.4 | -1.6 | -1.83 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 1-0 | 100.0 | 67.1 | 160.0 | 0.3 |
| consensus_gap+money_moving | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 0-1 | 0.0 | -67.1 | -100.0 | 0.0 |
| money_level+pin_move | early | pin $1-2k | 1-0 | 100.0 | 55.1 | 94.3 | -1.0 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -32.9 | -100.0 | 1.5 |
| money_delta+money_moving | early | pin $1-2k | 0-1 | 0.0 | -32.9 | -100.0 | 1.5 |
| money_delta+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -32.9 | -100.0 | 1.5 |
| follow_move+pin_move | early | pin limit <$1k | 1-5 | 16.7 | -30.1 | -68.2 | 0.33 |
| follow_move+pin_value | early | pin limit <$1k | 4-3 | 57.1 | 7.9 | 9.1 | -0.71 |
| consensus_gap+money_level | early | pin limit <$1k | 3-0 | 100.0 | 49.3 | 90.9 | 0.0 |
| consensus_gap+pin_move | early | pin limit <$1k | 2-1 | 66.7 | 15.0 | 28.7 | 0.33 |
| consensus_gap+pin_value | early | pin limit <$1k | 7-2 | 77.8 | 27.9 | 48.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 4-2 | 66.7 | 18.1 | 28.0 | 0.5 |
| follow_move+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 2.2 | -4.5 | 0.0 |
| follow_move+sharp_gap | early | pin limit <$1k | 3-3 | 50.0 | 3.2 | -3.8 | 0.17 |
| money_level+pin_move | early | pin limit <$1k | 1-4 | 20.0 | -28.3 | -61.8 | 0.4 |
| money_level+pin_value | early | pin limit <$1k | 3-2 | 60.0 | 8.7 | 14.5 | 0.6 |
| money_moving+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 2.2 | -4.5 | 0.0 |
| money_moving+sharp_gap | early | pin limit <$1k | 5-1 | 83.3 | 34.1 | 59.8 | 0.17 |
| pin_move+pin_value | early | pin limit <$1k | 3-4 | 42.9 | -8.1 | -17.6 | 0.57 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -47.8 | -100.0 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 | -0.5 |
| consensus_gap+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 52.2 | 90.9 | 1.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 52.2 | 92.3 | 1.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.2 | 90.9 | 1.0 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 52.2 | 90.9 | 1.0 |
| follow_move+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 52.2 | 90.9 | 1.0 |
| follow_move+money_level | early | pin limit <$1k | 3-3 | 50.0 | 2.5 | -3.8 | 0.0 |
| follow_move+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 9.6 | -4.5 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 52.2 | 90.9 | 1.0 |
| money_delta+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 52.2 | 90.9 | 1.0 |
| money_delta+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 52.2 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.2 | 90.9 | 1.0 |
| money_delta+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 52.2 | 90.9 | 1.0 |
| money_level+money_moving | early | pin limit <$1k | 4-0 | 100.0 | 50.0 | 92.0 | 0.5 |
| money_level+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 9.6 | -4.5 | 0.5 |
| money_level+sharp_gap | early | pin limit <$1k | 5-4 | 55.6 | 6.5 | 6.5 | 0.67 |
| money_moving+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 52.2 | 92.3 | 1.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.2 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 52.2 | 90.9 | 1.0 |
| pin_value+sharp_gap | early | pin limit <$1k | 1-2 | 33.3 | -17.4 | -36.4 | 1.33 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 9.6 | -4.5 | 0.5 |
| pin_move+sharp_gap | early | pin limit <$1k | 0-3 | 0.0 | -45.8 | -100.0 | 1.0 |
| money_moving+pin_move | early | pin limit <$1k | 1-1 | 50.0 | 2.2 | -2.4 | 1.0 |
| follow_move+pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -32.9 | -100.0 | 0.0 |
| money_level+pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -32.9 | -100.0 | 0.0 |
| pin_move+pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -32.9 | -100.0 | 0.0 |
| pin_move+rlm_ratio | early | pin limit <$1k | 0-1 | 0.0 | -32.9 | -100.0 | 0.0 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 0-1 | 0.0 | -32.9 | -100.0 | 0.0 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -32.9 | -100.0 | 0.0 |
