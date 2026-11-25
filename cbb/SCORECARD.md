# CBB scorecard

Generated 2026-11-25 19:36 UTC. 918 graded games (39 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**684 games before 2026-11-21 (fit) · 234 on or after it (forward).**

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
sample ran **47.3% favourites** (n=917) and **50.5% overs** (n=918) and **71.7% moneyline favourites** (n=799).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-21. Nothing in the engine was chosen using these. n=234 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 19-26 | 42.2 | 38.1 | 4.1 | +1.89 | 4.2 | 1.01 | 51.1 | no edge shown yet |
| pin_move | both | 6-11 | 35.3 | 48.8 | -13.5 | -5.47 | -32.2 | 0.18 | 29.4 | keep collecting (17/30) |
| money_delta | both | 4-4 | 50.0 | 38.1 | 11.9 | +2.47 | 30.9 | 2.86 | 100.0 | keep collecting (8/30) |
| pin_rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | keep collecting (2/30) |
| follow_move | both | 175-201 | 46.5 | 48.9 | -2.3 | -43.97 | -11.7 | 0.03 | 37.2 | DROP: below break-even |
| rlm_ratio | both | 7-15 | 31.8 | 41.1 | -9.3 | -4.95 | -22.5 | 0.41 | 54.5 | keep collecting (22/30) |
| money_level | both | 61-51 | 54.5 | 57.5 | -3.1 | -13.09 | -11.7 | -0.45 | 36.6 | no edge shown yet |
| sharp_gap | both | 44-56 | 44.0 | 49.7 | -5.7 | -14.96 | -15.0 | 0.2 | 49.0 | DROP: below break-even |
| money_moving | both | 41-37 | 52.6 | 49.0 | 3.5 | +0.05 | 0.1 | 0.63 | 51.3 | no edge shown yet |
| pin_value | both | 21-18 | 53.8 | 49.9 | 4.0 | +0.67 | 1.7 | 0.04 | 33.3 | no edge shown yet |
| consensus_gap | both | 113-90 | 55.7 | 52.6 | 3.0 | -4.25 | -2.1 | 0.59 | 50.2 | no edge shown yet |
| follow_move+money_level | both | 23-17 | 57.5 | 57.2 | 0.3 | -4.99 | -12.5 | 0.02 | 35.0 | no edge shown yet |
| follow_move+sharp_gap | both | 19-23 | 45.2 | 48.2 | -3.0 | -5.0 | -11.9 | 0.52 | 45.2 | no edge shown yet |
| money_level+sharp_gap | both | 31-33 | 48.4 | 55.3 | -6.8 | -11.12 | -17.4 | -0.25 | 43.8 | no edge shown yet |
| follow_move+money_moving | both | 18-16 | 52.9 | 48.3 | 4.6 | +2.07 | 6.1 | 0.53 | 44.1 | no edge shown yet |
| money_level+money_moving | both | 18-14 | 56.2 | 55.7 | 0.5 | -1.08 | -3.4 | 0.52 | 46.9 | no edge shown yet |
| consensus_gap+money_level | both | 20-15 | 57.1 | 60.9 | -3.7 | -4.73 | -13.5 | -0.61 | 34.3 | no edge shown yet |
| follow_move+rlm_quiet | both | 19-26 | 42.2 | 38.1 | 4.1 | +1.89 | 4.2 | 1.01 | 51.1 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 7-15 | 31.8 | 41.1 | -9.3 | -4.95 | -22.5 | 0.41 | 54.5 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | both | 6-9 | 40.0 | 38.4 | 1.6 | +0.14 | 0.9 | 0.3 | 46.7 | keep collecting (15/30) |
| rlm_quiet+sharp_gap | both | 6-10 | 37.5 | 39.0 | -1.5 | -0.86 | -5.4 | 0.28 | 43.8 | keep collecting (16/30) |
| rlm_ratio+sharp_gap | both | 7-15 | 31.8 | 41.1 | -9.3 | -4.95 | -22.5 | 0.41 | 54.5 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 15-13 | 53.6 | 55.0 | -1.4 | -2.16 | -7.7 | 0.97 | 60.7 | keep collecting (28/30) |
| money_moving+rlm_quiet | both | 8-8 | 50.0 | 39.0 | 11.0 | +3.93 | 24.5 | 0.81 | 50.0 | keep collecting (16/30) |
| money_moving+rlm_ratio | both | 7-5 | 58.3 | 40.5 | 17.9 | +5.05 | 42.0 | 1.36 | 66.7 | keep collecting (12/30) |
| money_moving+sharp_gap | both | 22-24 | 47.8 | 46.9 | 0.9 | -0.23 | -0.5 | 0.89 | 58.7 | no edge shown yet |
| consensus_gap+money_moving | both | 10-4 | 71.4 | 55.5 | 15.9 | +1.97 | 14.1 | 1.39 | 64.3 | keep collecting (14/30) |
| consensus_gap+sharp_gap | both | 12-12 | 50.0 | 55.4 | -5.4 | -4.4 | -18.3 | -0.56 | 41.7 | keep collecting (24/30) |
| money_level+rlm_ratio | both | 1-6 | 14.3 | 46.9 | -32.6 | -5.09 | -72.7 | 0.64 | 71.4 | keep collecting (7/30) |
| follow_move+pin_move | both | 2-6 | 25.0 | 46.4 | -21.4 | -4.15 | -51.9 | 0.12 | 25.0 | keep collecting (8/30) |
| follow_move+money_delta | both | 3-1 | 75.0 | 39.9 | 35.1 | +4.56 | 114.0 | 2.35 | 100.0 | keep collecting (4/30) |
| money_delta+money_level | both | 1-3 | 25.0 | 39.9 | -14.9 | -2.09 | -52.3 | 1.68 | 100.0 | keep collecting (4/30) |
| money_delta+money_moving | both | 4-4 | 50.0 | 38.1 | 11.9 | +2.47 | 30.9 | 2.86 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | both | 3-1 | 75.0 | 39.9 | 35.1 | +4.56 | 114.0 | 2.35 | 100.0 | keep collecting (4/30) |
| money_delta+sharp_gap | both | 4-4 | 50.0 | 38.1 | 11.9 | +2.47 | 30.9 | 2.86 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| follow_move+pin_value | both | 4-4 | 50.0 | 48.9 | 1.1 | -0.36 | -4.5 | -0.62 | 25.0 | keep collecting (8/30) |
| consensus_gap+pin_move | both | 2-1 | 66.7 | 51.4 | 15.2 | +0.86 | 28.7 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+pin_value | both | 10-3 | 76.9 | 49.5 | 27.4 | +5.9 | 45.4 | -0.15 | 30.8 | keep collecting (13/30) |
| money_level+pin_move | both | 2-4 | 33.3 | 48.4 | -15.1 | -2.15 | -35.8 | 0.17 | 16.7 | keep collecting (6/30) |
| money_level+pin_value | both | 3-3 | 50.0 | 54.4 | -4.4 | -0.27 | -4.5 | 0.78 | 50.0 | keep collecting (6/30) |
| pin_move+pin_value | both | 3-6 | 33.3 | 50.0 | -16.7 | -3.23 | -35.9 | 0.44 | 33.3 | keep collecting (9/30) |
| money_moving+pin_value | both | 3-2 | 60.0 | 52.5 | 7.5 | +0.77 | 15.4 | 1.14 | 100.0 | keep collecting (5/30) |
| pin_value+sharp_gap | both | 1-4 | 20.0 | 54.9 | -34.9 | -3.09 | -61.8 | 1.34 | 80.0 | keep collecting (5/30) |
| consensus_gap+money_delta | both | 1-0 | 100.0 | 47.0 | 53.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | both | 1-0 | 100.0 | 47.0 | 53.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | both | 1-0 | 100.0 | 47.0 | 53.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+rlm_ratio | both | 1-0 | 100.0 | 47.0 | 53.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+sharp_gap | both | 0-3 | 0.0 | 46.2 | -46.2 | -3.0 | -100.0 | 1.0 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | both | 2-0 | 100.0 | 32.7 | 67.3 | +4.65 | 232.5 | 3.2 | 100.0 | keep collecting (2/30) |
| consensus_gap+rlm_quiet | both | 1-0 | 100.0 | 32.7 | 67.3 | +1.6 | 160.0 | 0.3 | 100.0 | keep collecting (1/30) |
| money_moving+pin_move | both | 1-1 | 50.0 | 47.0 | 3.0 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_move+pin_rlm | both | 0-1 | 0.0 | 32.7 | -32.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 0-1 | 0.0 | 32.7 | -32.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| rlm_quiet | moneyline | 12-16 | 42.9 | 32.7 | 10.1 | +5.52 | 19.7 | 1.22 | 46.4 | keep collecting (28/30) |
| rlm_quiet | total | 7-10 | 41.2 | 47.0 | -5.8 | -3.63 | -21.4 | 0.65 | 58.8 | keep collecting (17/30) |
| pin_move | moneyline | 0-1 | 0.0 | 32.7 | -32.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move | spread | 1-3 | 25.0 | 47.9 | -22.9 | -2.06 | -51.4 | -0.25 | 0.0 | keep collecting (4/30) |
| pin_move | total | 5-7 | 41.7 | 50.5 | -8.8 | -2.41 | -20.1 | 0.33 | 41.7 | keep collecting (12/30) |
| money_delta | moneyline | 2-3 | 40.0 | 32.7 | 7.3 | +1.65 | 33.0 | 2.38 | 100.0 | keep collecting (5/30) |
| money_delta | total | 2-1 | 66.7 | 47.0 | 19.7 | +0.82 | 27.3 | 3.67 | 100.0 | keep collecting (3/30) |
| pin_rlm | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | keep collecting (2/30) |
| follow_move | moneyline | 74-68 | 52.1 | 47.1 | 5.0 | -3.8 | -2.7 | -0.41 | 31.7 | no edge shown yet |
| follow_move | spread | 39-54 | 41.9 | 50.8 | -8.8 | -17.77 | -19.1 | 0.0 | 28.0 | DROP: below break-even |
| follow_move | total | 62-79 | 44.0 | 49.4 | -5.5 | -22.4 | -15.9 | 0.5 | 48.9 | DROP: below break-even |
| rlm_ratio | moneyline | 3-9 | 25.0 | 35.6 | -10.6 | -2.59 | -21.6 | -0.42 | 33.3 | keep collecting (12/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| rlm_ratio | total | 4-5 | 44.4 | 47.0 | -2.6 | -1.36 | -15.2 | 1.0 | 77.8 | keep collecting (9/30) |
| money_level | moneyline | 30-28 | 51.7 | 62.5 | -10.8 | -18.3 | -31.6 | -0.57 | 36.2 | no edge shown yet |
| money_level | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.06 | -2.9 | 2.0 | 50.0 | keep collecting (2/30) |
| money_level | total | 30-22 | 57.7 | 52.3 | 5.4 | +5.27 | 10.1 | -0.4 | 36.5 | no edge shown yet |
| sharp_gap | moneyline | 19-32 | 37.3 | 49.0 | -11.7 | -13.69 | -26.8 | -0.09 | 51.0 | DROP: below break-even |
| sharp_gap | spread | 0-2 | 0.0 | 54.3 | -54.3 | -2.0 | -100.0 | 3.0 | 100.0 | keep collecting (2/30) |
| sharp_gap | total | 25-22 | 53.2 | 50.2 | 3.0 | +0.72 | 1.5 | 0.4 | 44.7 | no edge shown yet |
| money_moving | moneyline | 17-20 | 45.9 | 48.6 | -2.7 | -4.88 | -13.2 | 0.85 | 59.5 | no edge shown yet |
| money_moving | spread | 0-2 | 0.0 | 54.3 | -54.3 | -2.0 | -100.0 | 3.0 | 100.0 | keep collecting (2/30) |
| money_moving | total | 24-15 | 61.5 | 49.2 | 12.4 | +6.94 | 17.8 | 0.31 | 41.0 | no edge shown yet |
| pin_value | moneyline | 0-1 | 0.0 | 67.3 | -67.3 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| pin_value | spread | 11-9 | 55.0 | 48.3 | 6.7 | +0.58 | 2.9 | 0.05 | 25.0 | keep collecting (20/30) |
| pin_value | total | 10-8 | 55.6 | 50.7 | 4.9 | +1.09 | 6.1 | -0.06 | 38.9 | keep collecting (18/30) |
| consensus_gap | moneyline | 57-45 | 55.9 | 56.1 | -0.2 | -8.98 | -8.8 | 0.57 | 52.0 | no edge shown yet |
| consensus_gap | spread | 23-17 | 57.5 | 47.9 | 9.6 | +2.88 | 7.2 | 0.25 | 32.5 | no edge shown yet |
| consensus_gap | total | 33-28 | 54.1 | 50.0 | 4.1 | +1.85 | 3.0 | 0.84 | 59.0 | no edge shown yet |
| consensus_gap+money_level | moneyline | 15-12 | 55.6 | 63.4 | -7.9 | -6.24 | -23.1 | -0.68 | 37.0 | keep collecting (27/30) |
| follow_move+rlm_quiet | moneyline | 12-16 | 42.9 | 32.7 | 10.1 | +5.52 | 19.7 | 1.22 | 46.4 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 3-9 | 25.0 | 35.6 | -10.6 | -2.59 | -21.6 | -0.42 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 7-11 | 38.9 | 46.2 | -7.3 | -3.95 | -21.9 | 0.21 | 33.3 | keep collecting (18/30) |
| rlm_quiet+rlm_ratio | moneyline | 3-6 | 33.3 | 32.7 | 0.6 | +0.41 | 4.6 | -0.06 | 33.3 | keep collecting (9/30) |
| rlm_quiet+sharp_gap | moneyline | 3-6 | 33.3 | 32.7 | 0.6 | +0.41 | 4.6 | -0.06 | 33.3 | keep collecting (9/30) |
| rlm_ratio+sharp_gap | moneyline | 3-9 | 25.0 | 35.6 | -10.6 | -2.59 | -21.6 | -0.42 | 33.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 9-4 | 69.2 | 62.0 | 7.3 | +1.38 | 10.6 | 0.17 | 46.2 | keep collecting (13/30) |
| consensus_gap+money_moving | moneyline | 7-4 | 63.6 | 57.9 | 5.8 | -0.8 | -7.3 | 1.5 | 54.5 | keep collecting (11/30) |
| consensus_gap+sharp_gap | moneyline | 9-8 | 52.9 | 57.1 | -4.2 | -3.09 | -18.2 | -0.79 | 41.2 | keep collecting (17/30) |
| money_level+money_moving | moneyline | 7-8 | 46.7 | 60.4 | -13.7 | -5.15 | -34.4 | 1.05 | 53.3 | keep collecting (15/30) |
| money_level+sharp_gap | moneyline | 13-19 | 40.6 | 58.6 | -18.0 | -13.48 | -42.1 | -0.62 | 43.8 | INVERT candidate: wrong well beyond its base rate |
| money_moving+sharp_gap | moneyline | 7-15 | 31.8 | 43.7 | -11.9 | -4.94 | -22.5 | 1.32 | 72.7 | keep collecting (22/30) |
| follow_move+money_level | moneyline | 12-7 | 63.2 | 63.6 | -0.5 | -5.07 | -26.7 | -0.43 | 21.1 | keep collecting (19/30) |
| follow_move+money_moving | moneyline | 9-7 | 56.2 | 47.8 | 8.4 | +2.85 | 17.8 | 0.25 | 37.5 | keep collecting (16/30) |
| money_moving+rlm_quiet | moneyline | 4-5 | 44.4 | 32.7 | 11.7 | +3.29 | 36.6 | 1.11 | 55.6 | keep collecting (9/30) |
| money_moving+rlm_ratio | moneyline | 3-3 | 50.0 | 32.7 | 17.3 | +3.41 | 56.8 | 0.88 | 50.0 | keep collecting (6/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 67.3 | -67.3 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 67.3 | -67.3 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 67.3 | -67.3 | -1.0 | -100.0 | 1.7 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_rlm | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | moneyline | 0-3 | 0.0 | 44.2 | -44.2 | -3.0 | -100.0 | -1.5 | 33.3 | keep collecting (3/30) |
| pin_rlm+rlm_ratio | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.75 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+money_moving | moneyline | 2-3 | 40.0 | 32.7 | 7.3 | +1.65 | 33.0 | 2.38 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-3 | 40.0 | 32.7 | 7.3 | +1.65 | 33.0 | 2.38 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_level | moneyline | 0-2 | 0.0 | 32.7 | -32.7 | -2.0 | -100.0 | 1.85 | 100.0 | keep collecting (2/30) |
| follow_move+money_delta | moneyline | 2-0 | 100.0 | 32.7 | 67.3 | +4.65 | 232.5 | 3.2 | 100.0 | keep collecting (2/30) |
| money_delta+rlm_quiet | moneyline | 2-0 | 100.0 | 32.7 | 67.3 | +4.65 | 232.5 | 3.2 | 100.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 32.7 | 67.3 | +4.65 | 232.5 | 3.2 | 100.0 | keep collecting (2/30) |
| consensus_gap+rlm_quiet | moneyline | 1-0 | 100.0 | 32.7 | 67.3 | +1.6 | 160.0 | 0.3 | 100.0 | keep collecting (1/30) |
| follow_move+pin_move | moneyline | 0-1 | 0.0 | 32.7 | -32.7 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| money_level+pin_move | moneyline | 0-1 | 0.0 | 32.7 | -32.7 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| pin_move+pin_rlm | moneyline | 0-1 | 0.0 | 32.7 | -32.7 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| pin_move+rlm_ratio | moneyline | 0-1 | 0.0 | 32.7 | -32.7 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| pin_move+sharp_gap | moneyline | 0-1 | 0.0 | 32.7 | -32.7 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to pin_move alone, not independent confirmation |
| follow_move+money_level | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.06 | -2.9 | 2.0 | 50.0 | redundant -- identical record to money_level alone, not independent confirmation |
| follow_move+money_moving | spread | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level+money_moving | spread | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_level+rlm_ratio | spread | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+sharp_gap | spread | 0-2 | 0.0 | 54.3 | -54.3 | -2.0 | -100.0 | 3.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 5.0 | 100.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 1-1 | 50.0 | 45.7 | 4.3 | -0.09 | -4.5 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | spread | 0-2 | 0.0 | 45.7 | -45.7 | -2.0 | -100.0 | 0.0 | 0.0 | keep collecting (2/30) |
| consensus_gap+pin_value | spread | 4-1 | 80.0 | 47.4 | 32.6 | +2.41 | 48.1 | -0.4 | 0.0 | keep collecting (5/30) |
| follow_move+pin_move | spread | 1-1 | 50.0 | 45.7 | 4.3 | -0.06 | -2.9 | -0.5 | 0.0 | keep collecting (2/30) |
| consensus_gap+pin_move | spread | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | spread | 0-1 | 0.0 | 45.7 | -45.7 | -1.0 | -100.0 | 4.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_move | spread | 1-0 | 100.0 | 45.7 | 54.3 | +0.94 | 94.3 | -1.0 | 0.0 | keep collecting (1/30) |
| money_moving+pin_value | spread | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | spread | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| follow_move+money_level | total | 10-9 | 52.6 | 51.4 | 1.2 | +0.13 | 0.7 | 0.26 | 47.4 | keep collecting (19/30) |
| follow_move+sharp_gap | total | 12-11 | 52.2 | 49.6 | 2.6 | -0.05 | -0.2 | 0.57 | 52.2 | keep collecting (23/30) |
| money_level+sharp_gap | total | 18-13 | 58.1 | 51.8 | 6.2 | +3.36 | 10.8 | -0.03 | 41.9 | no edge shown yet |
| follow_move+money_moving | total | 9-8 | 52.9 | 48.4 | 4.5 | +0.22 | 1.3 | 0.53 | 47.1 | keep collecting (17/30) |
| money_level+money_moving | total | 11-5 | 68.8 | 51.5 | 17.3 | +5.08 | 31.7 | -0.25 | 37.5 | keep collecting (16/30) |
| follow_move+rlm_quiet | total | 7-10 | 41.2 | 47.0 | -5.8 | -3.63 | -21.4 | 0.65 | 58.8 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | total | 4-5 | 44.4 | 47.0 | -2.6 | -1.36 | -15.2 | 1.0 | 77.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | total | 3-3 | 50.0 | 47.0 | 3.0 | -0.27 | -4.5 | 0.83 | 66.7 | keep collecting (6/30) |
| rlm_quiet+sharp_gap | total | 3-4 | 42.9 | 47.0 | -4.2 | -1.27 | -18.2 | 0.71 | 57.1 | keep collecting (7/30) |
| rlm_ratio+sharp_gap | total | 4-5 | 44.4 | 47.0 | -2.6 | -1.36 | -15.2 | 1.0 | 77.8 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | total | 4-3 | 57.1 | 47.0 | 10.1 | +0.64 | 9.1 | 0.43 | 42.9 | keep collecting (7/30) |
| money_moving+rlm_ratio | total | 4-1 | 80.0 | 47.0 | 33.0 | +2.64 | 52.7 | 1.2 | 80.0 | keep collecting (5/30) |
| money_moving+sharp_gap | total | 15-7 | 68.2 | 49.5 | 18.7 | +6.71 | 30.5 | 0.27 | 40.9 | keep collecting (22/30) |
| follow_move+pin_move | total | 1-4 | 20.0 | 49.4 | -29.4 | -3.09 | -61.8 | 0.4 | 40.0 | keep collecting (5/30) |
| consensus_gap+follow_move | total | 6-8 | 42.9 | 49.1 | -6.3 | -2.55 | -18.2 | 1.5 | 71.4 | keep collecting (14/30) |
| consensus_gap+money_level | total | 5-3 | 62.5 | 52.2 | 10.3 | +1.51 | 18.8 | -0.38 | 25.0 | keep collecting (8/30) |
| consensus_gap+sharp_gap | total | 3-4 | 42.9 | 51.3 | -8.4 | -1.31 | -18.7 | 0.0 | 42.9 | keep collecting (7/30) |
| follow_move+money_delta | total | 1-1 | 50.0 | 47.0 | 3.0 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+money_level | total | 1-1 | 50.0 | 47.0 | 3.0 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+money_moving | total | 2-1 | 66.7 | 47.0 | 19.7 | +0.82 | 27.3 | 3.67 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | total | 1-1 | 50.0 | 47.0 | 3.0 | -0.09 | -4.5 | 1.5 | 100.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 2-1 | 66.7 | 47.0 | 19.7 | +0.82 | 27.3 | 3.67 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+rlm_ratio | total | 1-2 | 33.3 | 47.0 | -13.7 | -1.09 | -36.4 | 1.33 | 100.0 | keep collecting (3/30) |
| follow_move+pin_value | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.27 | -4.5 | -0.67 | 33.3 | keep collecting (6/30) |
| consensus_gap+pin_move | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | 0.5 | 50.0 | keep collecting (2/30) |
| consensus_gap+pin_value | total | 6-2 | 75.0 | 50.7 | 24.3 | +3.5 | 43.7 | 0.0 | 50.0 | keep collecting (8/30) |
| money_level+pin_move | total | 1-3 | 25.0 | 53.0 | -28.0 | -2.09 | -52.3 | 0.5 | 25.0 | keep collecting (4/30) |
| money_level+pin_value | total | 3-2 | 60.0 | 51.8 | 8.2 | +0.73 | 14.5 | 0.6 | 40.0 | keep collecting (5/30) |
| pin_move+pin_value | total | 3-4 | 42.9 | 51.3 | -8.4 | -1.23 | -17.6 | 0.57 | 42.9 | keep collecting (7/30) |
| consensus_gap+money_delta | total | 1-0 | 100.0 | 47.0 | 53.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_moving | total | 3-0 | 100.0 | 47.0 | 53.0 | +2.77 | 92.3 | 1.0 | 100.0 | keep collecting (3/30) |
| consensus_gap+rlm_ratio | total | 1-0 | 100.0 | 47.0 | 53.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+pin_value | total | 1-0 | 100.0 | 47.0 | 53.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | total | 3-0 | 100.0 | 47.0 | 53.0 | +2.77 | 92.3 | 1.0 | 100.0 | keep collecting (3/30) |
| pin_value+rlm_ratio | total | 1-0 | 100.0 | 47.0 | 53.0 | +0.91 | 90.9 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | total | 1-2 | 33.3 | 51.0 | -17.7 | -1.09 | -36.4 | 1.33 | 66.7 | keep collecting (3/30) |
| pin_move+sharp_gap | total | 0-2 | 0.0 | 53.0 | -53.0 | -2.0 | -100.0 | 1.5 | 50.0 | keep collecting (2/30) |
| money_moving+pin_move | total | 1-1 | 50.0 | 47.0 | 3.0 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 88-143 | 38.1 | 42.4 | -4.3 | -35.78 | -15.5 |  |  | DROP: below break-even |
| pin_move | both | 153-188 | 44.9 | 49.6 | -4.7 | -41.94 | -12.3 |  |  | DROP: below break-even |
| money_delta | both | 86-101 | 46.0 | 44.2 | 1.8 | -10.2 | -5.5 |  |  | DROP: below break-even |
| pin_rlm | both | 27-52 | 34.2 | 42.4 | -8.3 | -21.42 | -27.1 |  |  | DROP: below break-even |
| follow_move | both | 261-306 | 46.0 | 49.3 | -3.3 | -67.92 | -12.0 |  |  | DROP: below break-even |
| rlm_ratio | both | 52-89 | 36.9 | 42.1 | -5.3 | -31.72 | -22.5 |  |  | DROP: below break-even |
| money_level | both | 335-267 | 55.6 | 55.6 | 0.0 | -35.08 | -5.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 251-310 | 44.7 | 48.7 | -4.0 | -80.63 | -14.4 |  |  | DROP: below break-even |
| money_moving | both | 263-301 | 46.6 | 49.2 | -2.6 | -66.45 | -11.8 |  |  | DROP: below break-even |
| pin_value | both | 128-127 | 50.2 | 50.0 | 0.2 | +1.32 | 0.5 |  |  | no edge shown yet |
| consensus_gap | both | 108-91 | 54.3 | 52.8 | 1.5 | -4.22 | -2.1 |  |  | no edge shown yet |
| follow_move+pin_move | both | 104-152 | 40.6 | 49.3 | -8.7 | -56.33 | -22.0 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 62-77 | 44.6 | 42.8 | 1.8 | -8.35 | -6.0 |  |  | DROP: below break-even |
| money_delta+sharp_gap | both | 62-76 | 44.9 | 42.8 | 2.2 | -7.35 | -5.3 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 244-291 | 45.6 | 48.9 | -3.3 | -66.6 | -12.4 |  |  | DROP: below break-even |
| consensus_gap+money_level | both | 71-48 | 59.7 | 58.8 | 0.9 | -7.0 | -5.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+rlm_quiet | both | 88-143 | 38.1 | 42.4 | -4.3 | -35.78 | -15.5 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | both | 40-70 | 36.4 | 43.9 | -7.5 | -25.1 | -22.8 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 29-33 | 46.8 | 51.7 | -4.9 | -11.15 | -18.0 |  |  | no edge shown yet |
| follow_move+money_level | both | 124-111 | 52.8 | 56.0 | -3.2 | -24.86 | -10.6 |  |  | no edge shown yet |
| money_level+money_moving | both | 181-172 | 51.3 | 53.5 | -2.3 | -32.43 | -9.2 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 170-173 | 49.6 | 53.3 | -3.7 | -38.11 | -11.1 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 35-47 | 42.7 | 51.4 | -8.8 | -15.03 | -18.3 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 28-21 | 57.1 | 50.8 | 6.3 | +7.57 | 15.4 |  |  | no edge shown yet |
| consensus_gap+pin_value | both | 38-35 | 52.1 | 49.9 | 2.2 | +2.17 | 3.0 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | both | 35-50 | 41.2 | 50.8 | -9.6 | -17.89 | -21.0 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 126-161 | 43.9 | 48.8 | -4.9 | -48.89 | -17.0 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 40-40 | 50.0 | 50.6 | -0.6 | +5.15 | 6.4 |  |  | no edge shown yet |
| follow_move+sharp_gap | both | 123-164 | 42.9 | 48.5 | -5.6 | -51.18 | -17.8 |  |  | DROP: below break-even |
| money_level+pin_move | both | 68-73 | 48.2 | 54.5 | -6.2 | -20.76 | -14.7 |  |  | no edge shown yet |
| money_level+pin_value | both | 54-60 | 47.4 | 51.2 | -3.9 | -12.88 | -11.3 |  |  | no edge shown yet |
| money_moving+pin_move | both | 62-89 | 41.1 | 48.9 | -7.9 | -32.57 | -21.6 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 44-60 | 42.3 | 50.0 | -7.7 | -17.94 | -17.3 |  |  | DROP: below break-even |
| pin_move+pin_value | both | 51-56 | 47.7 | 50.9 | -3.2 | -10.82 | -10.1 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 58-96 | 37.7 | 48.3 | -10.7 | -41.74 | -27.1 |  |  | DROP: below break-even |
| pin_value+sharp_gap | both | 43-62 | 41.0 | 50.3 | -9.4 | -20.85 | -19.9 |  |  | DROP: below break-even |
| follow_move+money_delta | both | 42-66 | 38.9 | 44.2 | -5.3 | -23.52 | -21.8 |  |  | DROP: below break-even |
| money_delta+pin_move | both | 21-38 | 35.6 | 44.5 | -8.9 | -17.91 | -30.4 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 25-45 | 35.7 | 42.0 | -6.3 | -18.26 | -26.1 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | both | 52-89 | 36.9 | 42.1 | -5.3 | -31.72 | -22.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | both | 35-72 | 32.7 | 41.2 | -8.4 | -30.89 | -28.9 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 51-84 | 37.8 | 42.5 | -4.7 | -28.44 | -21.1 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 27-65 | 29.3 | 40.1 | -10.8 | -31.64 | -34.4 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | both | 35-74 | 32.1 | 41.0 | -8.9 | -32.75 | -30.0 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 52-89 | 36.9 | 42.1 | -5.3 | -31.72 | -22.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | both | 21-20 | 51.2 | 48.3 | 2.9 | +0.77 | 1.9 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 6-16 | 27.3 | 38.8 | -11.6 | -8.96 | -40.7 |  |  | keep collecting (22/30) |
| consensus_gap+rlm_ratio | both | 5-9 | 35.7 | 39.8 | -4.1 | -2.95 | -21.1 |  |  | keep collecting (14/30) |
| money_delta+rlm_ratio | both | 30-49 | 38.0 | 42.0 | -4.0 | -17.55 | -22.2 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 3-7 | 30.0 | 45.4 | -15.4 | -2.72 | -27.2 |  |  | keep collecting (10/30) |
| money_level+pin_rlm | both | 10-11 | 47.6 | 48.0 | -0.4 | -1.52 | -7.2 |  |  | keep collecting (21/30) |
| money_moving+pin_rlm | both | 27-46 | 37.0 | 43.0 | -6.1 | -15.42 | -21.1 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 27-52 | 34.2 | 42.4 | -8.3 | -21.42 | -27.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | both | 20-19 | 51.3 | 47.4 | 3.9 | -0.44 | -1.1 |  |  | no edge shown yet |
| consensus_gap+money_delta | both | 11-7 | 61.1 | 45.0 | 16.1 | +6.51 | 36.2 |  |  | keep collecting (18/30) |
| follow_move+pin_rlm | both | 24-45 | 34.8 | 42.0 | -7.2 | -17.52 | -25.4 |  |  | DROP: below break-even |
| money_delta+pin_rlm | both | 14-28 | 33.3 | 41.9 | -8.5 | -13.83 | -32.9 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 25-46 | 35.2 | 43.0 | -7.8 | -18.18 | -25.6 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | both | 24-43 | 35.8 | 43.2 | -7.4 | -16.53 | -24.7 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 13-35 | 27.1 | 40.5 | -13.4 | -18.34 | -38.2 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | both | 24-45 | 34.8 | 42.0 | -7.2 | -17.52 | -25.4 |  |  | DROP: below break-even |
| money_delta+pin_value | both | 16-10 | 61.5 | 48.3 | 13.2 | +8.08 | 31.1 |  |  | keep collecting (26/30) |
| pin_value+rlm_quiet | both | 10-14 | 41.7 | 47.9 | -6.2 | +4.81 | 20.0 |  |  | keep collecting (24/30) |
| pin_value+rlm_ratio | both | 5-5 | 50.0 | 49.5 | 0.5 | -0.6 | -6.0 |  |  | keep collecting (10/30) |
| pin_rlm+pin_value | both | 4-8 | 33.3 | 49.8 | -16.5 | -4.43 | -37.0 |  |  | keep collecting (12/30) |
| rlm_quiet | moneyline | 31-66 | 32.0 | 33.4 | -1.5 | -12.08 | -12.5 |  |  | DROP: below break-even |
| rlm_quiet | spread | 18-22 | 45.0 | 52.8 | -7.8 | -5.1 | -12.7 |  |  | no edge shown yet |
| rlm_quiet | total | 39-55 | 41.5 | 47.3 | -5.8 | -18.6 | -19.8 |  |  | DROP: below break-even |
| pin_move | moneyline | 46-44 | 51.1 | 47.7 | 3.4 | +4.58 | 5.1 |  |  | no edge shown yet |
| pin_move | spread | 52-61 | 46.0 | 51.2 | -5.2 | -13.99 | -12.4 |  |  | no edge shown yet |
| pin_move | total | 55-83 | 39.9 | 49.6 | -9.7 | -32.54 | -23.6 |  |  | DROP: below break-even |
| money_delta | moneyline | 23-39 | 37.1 | 36.1 | 1.0 | -6.29 | -10.2 |  |  | DROP: below break-even |
| money_delta | spread | 16-12 | 57.1 | 50.9 | 6.2 | +2.74 | 9.8 |  |  | keep collecting (28/30) |
| money_delta | total | 47-50 | 48.5 | 47.4 | 1.0 | -6.65 | -6.9 |  |  | no edge shown yet |
| pin_rlm | moneyline | 10-25 | 28.6 | 34.7 | -6.1 | -9.98 | -28.5 |  |  | DROP: below break-even |
| pin_rlm | spread | 3-2 | 60.0 | 52.6 | 7.4 | +0.7 | 13.9 |  |  | keep collecting (5/30) |
| pin_rlm | total | 14-25 | 35.9 | 48.1 | -12.2 | -12.13 | -31.1 |  |  | DROP: below break-even |
| follow_move | moneyline | 95-104 | 47.7 | 48.2 | -0.4 | -18.58 | -9.3 |  |  | no edge shown yet |
| follow_move | spread | 73-84 | 46.5 | 50.7 | -4.2 | -16.75 | -10.7 |  |  | no edge shown yet |
| follow_move | total | 93-118 | 44.1 | 49.4 | -5.3 | -32.59 | -15.4 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 18-44 | 29.0 | 33.8 | -4.8 | -17.83 | -28.8 |  |  | DROP: below break-even |
| rlm_ratio | spread | 7-5 | 58.3 | 51.4 | 6.9 | +1.27 | 10.6 |  |  | keep collecting (12/30) |
| rlm_ratio | total | 27-40 | 40.3 | 48.2 | -7.9 | -15.15 | -22.6 |  |  | DROP: below break-even |
| money_level | moneyline | 140-76 | 64.8 | 64.2 | 0.6 | -19.47 | -9.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 76-77 | 49.7 | 49.2 | 0.5 | -8.99 | -5.9 |  |  | no edge shown yet |
| money_level | total | 119-114 | 51.1 | 51.9 | -0.8 | -6.62 | -2.8 |  |  | no edge shown yet |
| sharp_gap | moneyline | 82-112 | 42.3 | 46.3 | -4.0 | -35.74 | -18.4 |  |  | DROP: below break-even |
| sharp_gap | spread | 74-79 | 48.4 | 49.5 | -1.2 | -12.53 | -8.2 |  |  | no edge shown yet |
| sharp_gap | total | 95-119 | 44.4 | 50.4 | -6.0 | -32.37 | -15.1 |  |  | DROP: below break-even |
| money_moving | moneyline | 91-100 | 47.6 | 47.7 | -0.1 | -21.2 | -11.1 |  |  | no edge shown yet |
| money_moving | spread | 74-79 | 48.4 | 49.5 | -1.2 | -12.53 | -8.2 |  |  | no edge shown yet |
| money_moving | total | 98-122 | 44.5 | 50.3 | -5.8 | -32.71 | -14.9 |  |  | DROP: below break-even |
| pin_value | moneyline | 6-9 | 40.0 | 46.5 | -6.5 | +11.73 | 78.2 |  |  | keep collecting (15/30) |
| pin_value | spread | 62-53 | 53.9 | 49.7 | 4.2 | +0.47 | 0.4 |  |  | no edge shown yet |
| pin_value | total | 60-65 | 48.0 | 50.6 | -2.6 | -10.88 | -8.7 |  |  | no edge shown yet |
| consensus_gap | moneyline | 56-44 | 56.0 | 55.2 | 0.8 | -2.84 | -2.8 |  |  | no edge shown yet |
| consensus_gap | spread | 23-20 | 53.5 | 49.3 | 4.2 | -0.14 | -0.3 |  |  | no edge shown yet |
| consensus_gap | total | 29-27 | 51.8 | 51.3 | 0.5 | -1.24 | -2.2 |  |  | no edge shown yet |
| consensus_gap+money_level | moneyline | 45-19 | 70.3 | 65.1 | 5.2 | -0.72 | -1.1 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+pin_move | moneyline | 34-39 | 46.6 | 46.9 | -0.3 | -7.58 | -10.4 |  |  | no edge shown yet |
| follow_move+rlm_quiet | moneyline | 31-66 | 32.0 | 33.4 | -1.5 | -12.08 | -12.5 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| pin_move+rlm_quiet | moneyline | 13-26 | 33.3 | 33.6 | -0.3 | -6.29 | -16.1 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 18-17 | 51.4 | 52.5 | -1.0 | -4.96 | -14.2 |  |  | no edge shown yet |
| follow_move+money_level | moneyline | 55-33 | 62.5 | 64.1 | -1.6 | -9.77 | -11.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 78-96 | 44.8 | 46.6 | -1.8 | -21.95 | -12.6 |  |  | DROP: below break-even |
| follow_move+money_moving | moneyline | 48-57 | 45.7 | 46.5 | -0.8 | -16.16 | -15.4 |  |  | no edge shown yet |
| follow_move+sharp_gap | moneyline | 44-61 | 41.9 | 45.6 | -3.7 | -20.4 | -19.4 |  |  | DROP: below break-even |
| money_level+money_moving | moneyline | 60-38 | 61.2 | 61.3 | -0.1 | -7.39 | -7.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 52-41 | 55.9 | 60.6 | -4.7 | -12.42 | -13.4 |  |  | no edge shown yet |
| follow_move+rlm_ratio | moneyline | 18-44 | 29.0 | 33.8 | -4.8 | -17.83 | -28.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_quiet | moneyline | 14-36 | 28.0 | 32.7 | -4.7 | -14.26 | -28.5 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 17-40 | 29.8 | 33.9 | -4.1 | -15.55 | -27.3 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | moneyline | 12-36 | 25.0 | 32.7 | -7.7 | -16.5 | -34.4 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 14-38 | 26.9 | 32.7 | -5.8 | -16.12 | -31.0 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 18-44 | 29.0 | 33.8 | -4.8 | -17.83 | -28.8 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 18-21 | 46.2 | 52.2 | -6.1 | -3.99 | -10.2 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | moneyline | 2-12 | 14.3 | 32.7 | -18.4 | -8.6 | -61.4 |  |  | keep collecting (14/30) |
| consensus_gap+rlm_ratio | moneyline | 2-6 | 25.0 | 32.7 | -7.7 | -2.6 | -32.5 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | moneyline | 18-24 | 42.9 | 50.8 | -8.0 | -6.85 | -16.3 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 2-3 | 40.0 | 39.6 | 0.4 | +0.4 | 8.0 |  |  | keep collecting (5/30) |
| money_level+pin_rlm | moneyline | 2-3 | 40.0 | 46.5 | -6.5 | -0.84 | -16.8 |  |  | keep collecting (5/30) |
| money_moving+pin_rlm | moneyline | 10-20 | 33.3 | 35.0 | -1.7 | -4.98 | -16.6 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 10-25 | 28.6 | 34.7 | -6.1 | -9.98 | -28.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 3-4 | 42.9 | 42.6 | 0.3 | +2.46 | 35.2 |  |  | keep collecting (7/30) |
| money_level+rlm_ratio | moneyline | 3-6 | 33.3 | 40.4 | -7.1 | -2.91 | -32.4 |  |  | keep collecting (9/30) |
| consensus_gap+pin_move | moneyline | 16-5 | 76.2 | 50.8 | 25.4 | +13.06 | 62.2 |  |  | keep collecting (21/30) |
| money_level+pin_move | moneyline | 24-13 | 64.9 | 64.5 | 0.4 | -0.28 | -0.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_delta | moneyline | 3-4 | 42.9 | 37.7 | 5.2 | +2.35 | 33.5 |  |  | keep collecting (7/30) |
| follow_move+money_delta | moneyline | 13-26 | 33.3 | 37.1 | -3.8 | -10.27 | -26.3 |  |  | DROP: below break-even |
| follow_move+pin_rlm | moneyline | 9-21 | 30.0 | 33.9 | -3.9 | -7.3 | -24.3 |  |  | DROP: below break-even |
| money_delta+money_moving | moneyline | 21-37 | 36.2 | 35.1 | 1.1 | -6.03 | -10.4 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 5-11 | 31.2 | 34.9 | -3.6 | -5.66 | -35.4 |  |  | keep collecting (16/30) |
| money_delta+pin_rlm | moneyline | 6-13 | 31.6 | 34.5 | -3.0 | -6.24 | -32.8 |  |  | keep collecting (19/30) |
| money_delta+rlm_quiet | moneyline | 7-21 | 25.0 | 32.7 | -7.7 | -11.07 | -39.5 |  |  | keep collecting (28/30) |
| money_delta+rlm_ratio | moneyline | 10-25 | 28.6 | 34.7 | -6.1 | -11.85 | -33.9 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 21-37 | 36.2 | 35.1 | 1.1 | -6.03 | -10.4 |  |  | DROP: below break-even |
| money_moving+pin_move | moneyline | 18-19 | 48.6 | 44.9 | 3.8 | -2.19 | -5.9 |  |  | no edge shown yet |
| pin_move+pin_rlm | moneyline | 8-19 | 29.6 | 34.0 | -4.4 | -6.74 | -25.0 |  |  | keep collecting (27/30) |
| pin_move+rlm_ratio | moneyline | 7-18 | 28.0 | 34.1 | -6.1 | -7.06 | -28.2 |  |  | keep collecting (25/30) |
| pin_move+sharp_gap | moneyline | 16-24 | 40.0 | 43.1 | -3.1 | -7.58 | -18.9 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 6-18 | 25.0 | 32.7 | -7.7 | -7.8 | -32.5 |  |  | keep collecting (24/30) |
| pin_rlm+rlm_ratio | moneyline | 9-21 | 30.0 | 33.9 | -3.9 | -7.3 | -24.3 |  |  | DROP: below break-even |
| follow_move+pin_value | moneyline | 2-3 | 40.0 | 53.5 | -13.5 | +8.17 | 163.4 |  |  | keep collecting (5/30) |
| pin_value+rlm_quiet | moneyline | 1-1 | 50.0 | 32.7 | 17.3 | +9.6 | 480.0 |  |  | keep collecting (2/30) |
| money_delta+money_level | moneyline | 6-3 | 66.7 | 48.1 | 18.6 | +4.07 | 45.3 |  |  | keep collecting (9/30) |
| money_level+pin_value | moneyline | 1-5 | 16.7 | 61.5 | -44.9 | -4.43 | -73.9 |  |  | keep collecting (6/30) |
| pin_move+pin_value | moneyline | 2-4 | 33.3 | 55.8 | -22.4 | -2.35 | -39.2 |  |  | keep collecting (6/30) |
| money_delta+pin_value | moneyline | 1-0 | 100.0 | 32.7 | 67.3 | +4.5 | 450.0 |  |  | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 2-2 | 50.0 | 41.4 | 8.6 | +3.07 | 76.7 |  |  | keep collecting (4/30) |
| pin_value+sharp_gap | moneyline | 2-4 | 33.3 | 50.0 | -16.7 | +1.07 | 17.8 |  |  | keep collecting (6/30) |
| follow_move+pin_move | spread | 31-46 | 40.3 | 51.3 | -11.0 | -17.65 | -22.9 |  |  | DROP: below break-even |
| money_moving+sharp_gap | spread | 74-79 | 48.4 | 49.5 | -1.2 | -12.53 | -8.2 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+rlm_quiet | spread | 18-22 | 45.0 | 52.8 | -7.8 | -5.1 | -12.7 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | spread | 55-58 | 48.7 | 49.1 | -0.5 | -8.79 | -7.8 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 55-58 | 48.7 | 49.1 | -0.5 | -8.79 | -7.8 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 9-16 | 36.0 | 52.9 | -16.9 | -7.62 | -30.5 |  |  | keep collecting (25/30) |
| consensus_gap+pin_value | spread | 18-14 | 56.2 | 50.0 | 6.2 | +1.61 | 5.0 |  |  | no edge shown yet |
| follow_move+money_level | spread | 23-24 | 48.9 | 50.6 | -1.7 | -2.9 | -6.2 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 25-28 | 47.2 | 51.0 | -3.9 | -5.17 | -9.8 |  |  | no edge shown yet |
| follow_move+sharp_gap | spread | 25-28 | 47.2 | 51.0 | -3.9 | -5.17 | -9.8 |  |  | no edge shown yet |
| money_level+pin_move | spread | 16-21 | 43.2 | 50.3 | -7.1 | -6.83 | -18.5 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 17-23 | 42.5 | 50.6 | -8.1 | -7.99 | -20.0 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 17-23 | 42.5 | 50.6 | -8.1 | -7.99 | -20.0 |  |  | no edge shown yet |
| money_delta+money_level | spread | 5-3 | 62.5 | 48.9 | 13.6 | +1.46 | 18.2 |  |  | keep collecting (8/30) |
| money_delta+money_moving | spread | 10-9 | 52.6 | 50.2 | 2.4 | +0.04 | 0.2 |  |  | keep collecting (19/30) |
| money_delta+sharp_gap | spread | 10-9 | 52.6 | 50.2 | 2.4 | +0.04 | 0.2 |  |  | keep collecting (19/30) |
| consensus_gap+money_level | spread | 6-12 | 33.3 | 48.6 | -15.2 | -6.9 | -38.3 |  |  | keep collecting (18/30) |
| consensus_gap+money_moving | spread | 6-9 | 40.0 | 49.7 | -9.7 | -3.82 | -25.5 |  |  | keep collecting (15/30) |
| consensus_gap+sharp_gap | spread | 6-9 | 40.0 | 49.7 | -9.7 | -3.82 | -25.5 |  |  | keep collecting (15/30) |
| money_level+pin_value | spread | 21-22 | 48.8 | 48.7 | 0.1 | -4.15 | -9.7 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 20-26 | 43.5 | 49.6 | -6.2 | -8.9 | -19.3 |  |  | no edge shown yet |
| pin_value+sharp_gap | spread | 20-26 | 43.5 | 49.6 | -6.2 | -8.9 | -19.3 |  |  | no edge shown yet |
| follow_move+money_delta | spread | 7-5 | 58.3 | 52.1 | 6.2 | +1.38 | 11.5 |  |  | keep collecting (12/30) |
| follow_move+rlm_ratio | spread | 7-5 | 58.3 | 51.4 | 6.9 | +1.27 | 10.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | spread | 3-3 | 50.0 | 50.0 | -0.0 | -0.4 | -6.6 |  |  | keep collecting (6/30) |
| money_moving+rlm_ratio | spread | 7-5 | 58.3 | 51.4 | 6.9 | +1.27 | 10.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 7-5 | 58.3 | 51.4 | 6.9 | +1.27 | 10.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | spread | 16-13 | 55.2 | 51.0 | 4.1 | +1.05 | 3.6 |  |  | keep collecting (29/30) |
| pin_move+pin_value | spread | 27-21 | 56.2 | 51.2 | 5.0 | +2.6 | 5.4 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 8-9 | 47.1 | 51.3 | -4.2 | -2.05 | -12.1 |  |  | keep collecting (17/30) |
| consensus_gap+follow_move | spread | 4-5 | 44.4 | 50.5 | -6.0 | -1.43 | -15.8 |  |  | keep collecting (9/30) |
| consensus_gap+rlm_quiet | spread | 2-0 | 100.0 | 54.3 | 45.7 | +1.82 | 90.9 |  |  | keep collecting (2/30) |
| pin_value+rlm_quiet | spread | 3-3 | 50.0 | 54.3 | -4.3 | -0.33 | -5.6 |  |  | keep collecting (6/30) |
| money_delta+rlm_quiet | spread | 4-3 | 57.1 | 54.3 | 2.9 | +0.78 | 11.1 |  |  | keep collecting (7/30) |
| money_moving+rlm_quiet | spread | 4-6 | 40.0 | 53.4 | -13.4 | -2.39 | -23.9 |  |  | keep collecting (10/30) |
| rlm_quiet+rlm_ratio | spread | 1-3 | 25.0 | 54.3 | -29.3 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| rlm_quiet+sharp_gap | spread | 4-6 | 40.0 | 53.4 | -13.4 | -2.39 | -23.9 |  |  | keep collecting (10/30) |
| consensus_gap+money_delta | spread | 3-1 | 75.0 | 54.3 | 20.7 | +1.63 | 40.8 |  |  | keep collecting (4/30) |
| money_delta+pin_move | spread | 5-4 | 55.6 | 52.4 | 3.2 | +0.45 | 5.0 |  |  | keep collecting (9/30) |
| money_delta+pin_value | spread | 4-3 | 57.1 | 53.1 | 4.1 | +0.58 | 8.2 |  |  | keep collecting (7/30) |
| money_moving+pin_rlm | spread | 3-2 | 60.0 | 52.6 | 7.4 | +0.7 | 13.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | spread | 3-2 | 60.0 | 52.6 | 7.4 | +0.7 | 13.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | spread | 2-1 | 66.7 | 54.3 | 12.4 | +0.79 | 26.2 |  |  | keep collecting (3/30) |
| pin_rlm+sharp_gap | spread | 3-2 | 60.0 | 52.6 | 7.4 | +0.7 | 13.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+rlm_ratio | spread | 1-0 | 100.0 | 54.3 | 45.7 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| money_level+rlm_ratio | spread | 5-1 | 83.3 | 51.4 | 31.9 | +3.49 | 58.2 |  |  | keep collecting (6/30) |
| pin_move+rlm_ratio | spread | 3-1 | 75.0 | 52.1 | 22.9 | +1.67 | 41.6 |  |  | keep collecting (4/30) |
| pin_value+rlm_ratio | spread | 1-0 | 100.0 | 54.3 | 45.7 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| follow_move+pin_rlm | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_delta+pin_rlm | spread | 2-2 | 50.0 | 52.1 | -2.1 | -0.21 | -5.3 |  |  | keep collecting (4/30) |
| pin_rlm+rlm_quiet | spread | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_rlm+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| consensus_gap+pin_rlm | spread | 1-1 | 50.0 | 54.3 | -4.3 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+money_moving | total | 31-31 | 50.0 | 47.7 | 2.3 | -2.37 | -3.8 |  |  | no edge shown yet |
| money_delta+sharp_gap | total | 31-30 | 50.8 | 47.7 | 3.1 | -1.37 | -2.2 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 92-116 | 44.2 | 50.3 | -6.1 | -32.13 | -15.4 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | total | 39-55 | 41.5 | 47.3 | -5.8 | -18.6 | -19.8 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+follow_move | total | 7-11 | 38.9 | 50.7 | -11.8 | -4.77 | -26.5 |  |  | keep collecting (18/30) |
| consensus_gap+money_level | total | 20-17 | 54.1 | 52.8 | 1.2 | +0.62 | 1.7 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 11-17 | 39.3 | 51.3 | -12.0 | -7.21 | -25.8 |  |  | keep collecting (28/30) |
| consensus_gap+pin_move | total | 4-7 | 36.4 | 50.3 | -13.9 | -3.44 | -31.3 |  |  | keep collecting (11/30) |
| consensus_gap+pin_value | total | 17-17 | 50.0 | 51.2 | -1.2 | -1.9 | -5.6 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 11-17 | 39.3 | 51.3 | -12.0 | -7.21 | -25.8 |  |  | keep collecting (28/30) |
| follow_move+money_level | total | 46-54 | 46.0 | 51.3 | -5.3 | -12.19 | -12.2 |  |  | no edge shown yet |
| follow_move+money_moving | total | 53-76 | 41.1 | 49.7 | -8.7 | -27.55 | -21.4 |  |  | DROP: below break-even |
| follow_move+pin_move | total | 39-67 | 36.8 | 49.5 | -12.7 | -31.1 | -29.3 |  |  | DROP: below break-even |
| follow_move+pin_value | total | 22-24 | 47.8 | 50.0 | -2.2 | -4.07 | -8.8 |  |  | no edge shown yet |
| follow_move+sharp_gap | total | 54-75 | 41.9 | 49.8 | -7.9 | -25.61 | -19.9 |  |  | DROP: below break-even |
| money_level+money_moving | total | 66-76 | 46.5 | 51.7 | -5.2 | -16.25 | -11.4 |  |  | no edge shown yet |
| money_level+pin_move | total | 28-39 | 41.8 | 51.2 | -9.4 | -13.65 | -20.4 |  |  | DROP: below break-even |
| money_level+pin_value | total | 32-33 | 49.2 | 52.0 | -2.7 | -4.29 | -6.6 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 63-74 | 46.0 | 51.7 | -5.7 | -16.9 | -12.3 |  |  | DROP: below break-even |
| money_moving+pin_move | total | 27-47 | 36.5 | 50.0 | -13.5 | -22.39 | -30.3 |  |  | DROP: below break-even |
| money_moving+pin_value | total | 22-32 | 40.7 | 51.0 | -10.3 | -12.11 | -22.4 |  |  | DROP: below break-even |
| pin_move+pin_value | total | 22-31 | 41.5 | 50.1 | -8.5 | -11.06 | -20.9 |  |  | DROP: below break-even |
| pin_move+sharp_gap | total | 25-49 | 33.8 | 49.9 | -16.1 | -26.17 | -35.4 |  |  | INVERT candidate: wrong well beyond its base rate |
| pin_value+sharp_gap | total | 21-32 | 39.6 | 51.0 | -11.3 | -13.02 | -24.6 |  |  | DROP: below break-even |
| follow_move+money_delta | total | 22-35 | 38.6 | 47.3 | -8.7 | -14.63 | -25.7 |  |  | DROP: below break-even |
| money_delta+pin_move | total | 11-23 | 32.4 | 47.0 | -14.7 | -12.7 | -37.4 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | total | 14-21 | 40.0 | 47.0 | -7.0 | -7.97 | -22.8 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 18-28 | 39.1 | 47.7 | -8.5 | -11.2 | -24.3 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | total | 27-40 | 40.3 | 48.2 | -7.9 | -15.15 | -22.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+rlm_ratio | total | 17-21 | 44.7 | 47.5 | -2.7 | -5.3 | -14.0 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 17-30 | 36.2 | 47.5 | -11.3 | -14.23 | -30.3 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | total | 27-39 | 40.9 | 48.2 | -7.3 | -14.15 | -21.4 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | total | 14-26 | 35.0 | 47.6 | -12.6 | -13.01 | -32.5 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | total | 17-30 | 36.2 | 47.5 | -11.3 | -14.23 | -30.3 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | total | 27-40 | 40.3 | 48.2 | -7.9 | -15.15 | -22.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | total | 5-2 | 71.4 | 47.0 | 24.4 | +2.53 | 36.1 |  |  | keep collecting (7/30) |
| consensus_gap+rlm_quiet | total | 2-4 | 33.3 | 48.0 | -14.7 | -2.18 | -36.4 |  |  | keep collecting (6/30) |
| consensus_gap+rlm_ratio | total | 2-3 | 40.0 | 48.2 | -8.2 | -1.2 | -24.0 |  |  | keep collecting (5/30) |
| money_delta+pin_value | total | 11-7 | 61.1 | 47.3 | 13.8 | +3.0 | 16.7 |  |  | keep collecting (18/30) |
| pin_value+rlm_quiet | total | 6-10 | 37.5 | 47.4 | -9.9 | -4.46 | -27.9 |  |  | keep collecting (16/30) |
| pin_value+rlm_ratio | total | 4-5 | 44.4 | 49.0 | -4.6 | -1.44 | -16.0 |  |  | keep collecting (9/30) |
| follow_move+pin_rlm | total | 14-23 | 37.8 | 48.1 | -10.3 | -10.13 | -27.4 |  |  | DROP: below break-even |
| money_delta+money_level | total | 10-14 | 41.7 | 48.3 | -6.6 | -4.76 | -19.8 |  |  | keep collecting (24/30) |
| money_delta+pin_rlm | total | 6-13 | 31.6 | 47.0 | -15.4 | -7.37 | -38.8 |  |  | keep collecting (19/30) |
| money_level+pin_rlm | total | 7-7 | 50.0 | 48.3 | 1.7 | -0.59 | -4.2 |  |  | keep collecting (14/30) |
| money_level+rlm_ratio | total | 12-12 | 50.0 | 49.0 | 1.0 | -1.02 | -4.2 |  |  | keep collecting (24/30) |
| money_moving+pin_rlm | total | 14-24 | 36.8 | 48.1 | -11.3 | -11.13 | -29.3 |  |  | DROP: below break-even |
| pin_move+pin_rlm | total | 14-25 | 35.9 | 48.1 | -12.2 | -12.13 | -31.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 14-24 | 36.8 | 48.3 | -11.4 | -11.13 | -29.3 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | total | 14-23 | 37.8 | 48.1 | -10.3 | -10.13 | -27.4 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | total | 14-25 | 35.9 | 48.1 | -12.2 | -12.13 | -31.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_quiet | total | 7-16 | 30.4 | 48.0 | -17.6 | -9.54 | -41.5 |  |  | keep collecting (23/30) |
| consensus_gap+pin_rlm | total | 0-3 | 0.0 | 49.0 | -49.0 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_rlm+pin_value | total | 2-7 | 22.2 | 48.3 | -26.1 | -5.22 | -58.0 |  |  | keep collecting (9/30) |

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
| rlm_quiet | both | 49-62 | 44.1 | 36.5 | 7.6 | +12.47 | 11.2 | 0.52 | 46.8 | DROP: below break-even |
| pin_move | both | 11-20 | 35.5 | 48.4 | -12.9 | -10.57 | -34.1 | 0.2 | 38.7 | DROP: below break-even |
| money_delta | both | 14-11 | 56.0 | 40.3 | 15.7 | +6.9 | 27.6 | 0.77 | 52.0 | keep collecting (25/30) |
| pin_rlm | both | 1-4 | 20.0 | 37.0 | -17.0 | -3.07 | -61.5 | -0.3 | 60.0 | keep collecting (5/30) |
| follow_move | both | 649-603 | 51.8 | 51.2 | 0.7 | -88.44 | -7.1 | 0.14 | 40.6 | no edge shown yet |
| rlm_ratio | both | 36-32 | 52.9 | 39.4 | 13.5 | +15.58 | 22.9 | 0.42 | 52.9 | no edge shown yet |
| money_level | both | 230-160 | 59.0 | 58.4 | 0.5 | -24.42 | -6.3 | -0.21 | 38.5 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 187-176 | 51.5 | 48.7 | 2.8 | +4.13 | 1.1 | 0.26 | 44.9 | no edge shown yet |
| money_moving | both | 143-117 | 55.0 | 50.6 | 4.4 | +1.24 | 0.5 | 0.22 | 44.6 | no edge shown yet |
| pin_value | both | 71-67 | 51.4 | 48.9 | 2.6 | -3.93 | -2.8 | 0.08 | 36.2 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.6 | -31.6 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 332-380 | 46.6 | 49.1 | -2.5 | -65.71 | -9.2 | 0.45 | 46.5 | DROP: below break-even |
| consensus_gap+money_level | both | 52-43 | 54.7 | 62.8 | -8.0 | -14.44 | -15.2 | -0.02 | 43.2 | no edge shown yet |
| consensus_gap+money_moving | both | 27-27 | 50.0 | 49.7 | 0.3 | -4.45 | -8.2 | 0.55 | 48.1 | no edge shown yet |
| consensus_gap+pin_value | both | 30-31 | 49.2 | 47.3 | 1.9 | -4.8 | -7.9 | 0.27 | 44.3 | no edge shown yet |
| follow_move+rlm_quiet | both | 49-62 | 44.1 | 36.5 | 7.6 | +12.47 | 11.2 | 0.52 | 46.8 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | both | 36-32 | 52.9 | 39.4 | 13.5 | +15.58 | 22.9 | 0.42 | 52.9 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 94-60 | 61.0 | 49.4 | 11.6 | +20.31 | 13.2 | 0.41 | 47.4 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 82-53 | 60.7 | 57.3 | 3.4 | -0.94 | -0.7 | -0.01 | 46.7 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 14-12 | 53.8 | 50.5 | 3.4 | +0.54 | 2.1 | 0.49 | 46.2 | keep collecting (26/30) |
| money_moving+pin_value | both | 12-8 | 60.0 | 50.8 | 9.2 | +2.65 | 13.2 | 0.48 | 50.0 | keep collecting (20/30) |
| rlm_quiet+rlm_ratio | both | 22-19 | 53.7 | 36.6 | 17.1 | +14.38 | 35.1 | 0.07 | 48.8 | no edge shown yet |
| rlm_quiet+sharp_gap | both | 24-23 | 51.1 | 36.9 | 14.2 | +12.2 | 26.0 | 0.04 | 46.8 | no edge shown yet |
| rlm_ratio+sharp_gap | both | 36-32 | 52.9 | 39.4 | 13.5 | +15.58 | 22.9 | 0.42 | 52.9 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 128-93 | 57.9 | 55.4 | 2.5 | -6.95 | -3.1 | 0.03 | 43.4 | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | both | 82-71 | 53.6 | 48.0 | 5.5 | +5.77 | 3.8 | 0.4 | 49.0 | no edge shown yet |
| money_delta+money_level | both | 4-5 | 44.4 | 42.9 | 1.6 | -0.63 | -7.0 | 1.39 | 77.8 | keep collecting (9/30) |
| money_delta+money_moving | both | 13-11 | 54.2 | 39.9 | 14.3 | +5.99 | 25.0 | 0.8 | 54.2 | keep collecting (24/30) |
| money_delta+pin_value | both | 4-1 | 80.0 | 49.9 | 30.1 | +2.52 | 50.4 | 0.2 | 40.0 | keep collecting (5/30) |
| money_delta+sharp_gap | both | 11-9 | 55.0 | 39.1 | 15.9 | +6.25 | 31.3 | 0.96 | 65.0 | keep collecting (20/30) |
| pin_value+sharp_gap | both | 14-12 | 53.8 | 50.0 | 3.9 | +0.57 | 2.2 | 0.11 | 42.3 | keep collecting (26/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 50.5 | -50.5 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 47-54 | 46.5 | 52.6 | -6.1 | -17.18 | -17.0 | 0.79 | 56.4 | no edge shown yet |
| consensus_gap+rlm_quiet | both | 5-7 | 41.7 | 36.9 | 4.7 | -1.39 | -11.5 | 0.89 | 75.0 | keep collecting (12/30) |
| follow_move+pin_value | both | 24-22 | 52.2 | 48.9 | 3.3 | -0.95 | -2.1 | -0.2 | 28.3 | no edge shown yet |
| pin_value+rlm_quiet | both | 1-5 | 16.7 | 42.8 | -26.1 | -4.17 | -69.5 | -0.63 | 33.3 | keep collecting (6/30) |
| consensus_gap+sharp_gap | both | 38-57 | 40.0 | 48.4 | -8.4 | -14.69 | -15.5 | 0.52 | 47.4 | DROP: below break-even |
| follow_move+money_level | both | 114-61 | 65.1 | 59.2 | 5.9 | -3.75 | -2.1 | 0.01 | 41.7 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 12-13 | 48.0 | 43.3 | 4.7 | -0.66 | -2.6 | 1.06 | 64.0 | keep collecting (25/30) |
| pin_value+rlm_ratio | both | 3-2 | 60.0 | 45.4 | 14.6 | +0.73 | 14.5 | -1.16 | 40.0 | keep collecting (5/30) |
| follow_move+money_moving | both | 71-44 | 61.7 | 51.7 | 10.1 | +12.87 | 11.2 | 0.37 | 49.6 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 4-0 | 100.0 | 49.5 | 50.5 | +3.52 | 88.0 | 0.25 | 25.0 | keep collecting (4/30) |
| follow_move+money_delta | both | 8-4 | 66.7 | 40.5 | 26.1 | +8.51 | 70.9 | 0.82 | 58.3 | keep collecting (12/30) |
| money_delta+rlm_quiet | both | 4-2 | 66.7 | 35.0 | 31.7 | +6.18 | 103.0 | -0.33 | 33.3 | keep collecting (6/30) |
| money_moving+rlm_quiet | both | 19-18 | 51.4 | 37.4 | 14.0 | +8.79 | 23.8 | 0.52 | 45.9 | no edge shown yet |
| money_moving+rlm_ratio | both | 19-12 | 61.3 | 40.8 | 20.5 | +12.71 | 41.0 | 0.65 | 54.8 | no edge shown yet |
| consensus_gap+rlm_ratio | both | 5-4 | 55.6 | 40.0 | 15.5 | +1.0 | 11.1 | 0.72 | 66.7 | keep collecting (9/30) |
| pin_move+pin_value | both | 4-10 | 28.6 | 49.4 | -20.8 | -6.32 | -45.1 | 0.36 | 28.6 | keep collecting (14/30) |
| follow_move+pin_move | both | 7-9 | 43.8 | 49.1 | -5.3 | -3.25 | -20.3 | 0.28 | 43.8 | keep collecting (16/30) |
| consensus_gap+pin_move | both | 2-6 | 25.0 | 47.0 | -22.0 | -4.14 | -51.7 | 0.29 | 50.0 | keep collecting (8/30) |
| money_level+pin_move | both | 4-6 | 40.0 | 50.0 | -10.0 | -3.02 | -30.2 | 0.14 | 30.0 | keep collecting (10/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 28.3 | -28.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-3 | 25.0 | 39.1 | -14.1 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 28.3 | -28.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | both | 0-1 | 0.0 | 28.3 | -28.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-3 | 25.0 | 39.1 | -14.1 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+sharp_gap | both | 1-4 | 20.0 | 37.0 | -17.0 | -3.07 | -61.5 | -0.3 | 60.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.1 | -51.1 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 49.5 | -49.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-4 | 33.3 | 46.7 | -13.3 | -2.87 | -47.8 | 0.47 | 33.3 | keep collecting (6/30) |
| money_level+pin_rlm | both | 1-2 | 33.3 | 42.8 | -9.4 | -1.07 | -35.8 | 0.67 | 66.7 | keep collecting (3/30) |
| pin_move+pin_rlm | both | 1-1 | 50.0 | 28.3 | 21.7 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| pin_move+rlm_ratio | both | 1-1 | 50.0 | 28.3 | 21.7 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| money_delta+rlm_ratio | both | 5-2 | 71.4 | 37.4 | 34.1 | +7.9 | 112.8 | 1.71 | 85.7 | keep collecting (7/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 28.3 | -28.3 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_moving+pin_move | both | 1-1 | 50.0 | 49.5 | 0.5 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |
| rlm_quiet | moneyline | 28-40 | 41.2 | 28.3 | 12.9 | +15.41 | 22.7 | 0.47 | 45.6 | DROP: below break-even |
| rlm_quiet | spread | 3-2 | 60.0 | 49.5 | 10.5 | +0.65 | 13.0 | -0.8 | 0.0 | keep collecting (5/30) |
| rlm_quiet | total | 18-20 | 47.4 | 49.6 | -2.2 | -3.59 | -9.5 | 0.76 | 55.3 | no edge shown yet |
| pin_move | moneyline | 2-4 | 33.3 | 42.8 | -9.4 | -2.87 | -47.8 | 0.02 | 50.0 | keep collecting (6/30) |
| pin_move | spread | 2-7 | 22.2 | 49.1 | -26.9 | -5.15 | -57.2 | 0.11 | 22.2 | keep collecting (9/30) |
| pin_move | total | 7-9 | 43.8 | 50.1 | -6.3 | -2.55 | -15.9 | 0.31 | 43.8 | keep collecting (16/30) |
| money_delta | moneyline | 4-7 | 36.4 | 28.3 | 8.1 | +1.99 | 18.1 | 0.29 | 63.6 | keep collecting (11/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 9-3 | 75.0 | 49.6 | 25.4 | +5.08 | 42.3 | 1.25 | 41.7 | keep collecting (12/30) |
| pin_rlm | moneyline | 1-4 | 20.0 | 37.0 | -17.0 | -3.07 | -61.5 | -0.3 | 60.0 | keep collecting (5/30) |
| follow_move | moneyline | 269-194 | 58.1 | 53.3 | 4.8 | -27.89 | -6.0 | 0.01 | 41.7 | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 167-194 | 46.3 | 49.8 | -3.6 | -39.98 | -11.1 | 0.02 | 32.7 | DROP: below break-even |
| follow_move | total | 213-215 | 49.8 | 50.0 | -0.2 | -20.58 | -4.8 | 0.39 | 46.0 | no edge shown yet |
| rlm_ratio | moneyline | 16-19 | 45.7 | 29.5 | 16.2 | +10.12 | 28.9 | 0.15 | 51.4 | no edge shown yet |
| rlm_ratio | spread | 3-3 | 50.0 | 51.8 | -1.8 | -0.16 | -2.7 | 0.33 | 16.7 | keep collecting (6/30) |
| rlm_ratio | total | 17-10 | 63.0 | 49.5 | 13.4 | +5.62 | 20.8 | 0.78 | 63.0 | keep collecting (27/30) |
| money_level | moneyline | 126-67 | 65.3 | 67.0 | -1.7 | -25.8 | -13.4 | -0.35 | 42.0 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 18-18 | 50.0 | 49.1 | 0.9 | -1.75 | -4.8 | 0.94 | 50.0 | no edge shown yet |
| money_level | total | 86-75 | 53.4 | 50.3 | 3.1 | +3.13 | 1.9 | -0.32 | 31.7 | no edge shown yet |
| sharp_gap | moneyline | 80-93 | 46.2 | 47.4 | -1.1 | -10.1 | -5.8 | 0.2 | 50.3 | DROP: below break-even |
| sharp_gap | spread | 20-16 | 55.6 | 49.9 | 5.7 | +2.0 | 5.6 | 0.78 | 41.7 | no edge shown yet |
| sharp_gap | total | 87-67 | 56.5 | 49.9 | 6.6 | +12.22 | 7.9 | 0.21 | 39.6 | no edge shown yet |
| money_moving | moneyline | 61-61 | 50.0 | 51.4 | -1.4 | -17.28 | -14.2 | 0.15 | 50.8 | no edge shown yet |
| money_moving | spread | 18-7 | 72.0 | 49.3 | 22.7 | +9.18 | 36.7 | 0.52 | 48.0 | keep collecting (25/30) |
| money_moving | total | 64-49 | 56.6 | 49.9 | 6.7 | +9.35 | 8.3 | 0.22 | 37.2 | no edge shown yet |
| pin_value | moneyline | 2-7 | 22.2 | 37.9 | -15.7 | -5.31 | -59.0 | 0.12 | 55.6 | keep collecting (9/30) |
| pin_value | spread | 36-29 | 55.4 | 49.2 | 6.2 | +2.57 | 3.9 | 0.18 | 33.8 | no edge shown yet |
| pin_value | total | 33-31 | 51.6 | 50.1 | 1.5 | -1.19 | -1.9 | -0.03 | 35.9 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.7 | -19.3 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 146-209 | 41.1 | 48.7 | -7.6 | -59.57 | -16.8 | 0.27 | 45.1 | DROP: below break-even |
| consensus_gap | spread | 87-78 | 52.7 | 48.9 | 3.8 | -2.2 | -1.3 | 0.32 | 38.2 | no edge shown yet |
| consensus_gap | total | 99-93 | 51.6 | 50.0 | 1.5 | -3.93 | -2.0 | 0.89 | 56.2 | no edge shown yet |
| money_level+sharp_gap | moneyline | 59-38 | 60.8 | 62.3 | -1.5 | -14.58 | -15.0 | -0.17 | 50.5 | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+follow_move | moneyline | 20-26 | 43.5 | 56.6 | -13.1 | -13.31 | -28.9 | 0.19 | 52.2 | no edge shown yet |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 33.7 | -8.7 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| consensus_gap+rlm_quiet | moneyline | 2-5 | 28.6 | 28.3 | 0.3 | -2.08 | -29.7 | 0.96 | 85.7 | keep collecting (7/30) |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.8 | -9.4 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| follow_move+rlm_quiet | moneyline | 28-40 | 41.2 | 28.3 | 12.9 | +15.41 | 22.7 | 0.47 | 45.6 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | moneyline | 37-21 | 63.8 | 67.2 | -3.4 | -10.06 | -17.3 | -0.23 | 51.7 | beats break-even but not its base rate -- directional bias, not signal |
| pin_value+rlm_quiet | moneyline | 0-2 | 0.0 | 28.3 | -28.3 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| consensus_gap+sharp_gap | moneyline | 24-44 | 35.3 | 48.1 | -12.8 | -14.12 | -20.8 | 0.49 | 48.5 | DROP: below break-even |
| follow_move+money_level | moneyline | 70-23 | 75.3 | 67.5 | 7.8 | -5.81 | -6.2 | -0.3 | 40.9 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 37-19 | 66.1 | 53.9 | 12.2 | +6.77 | 12.1 | 0.13 | 50.0 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 38-31 | 55.1 | 67.9 | -12.9 | -14.79 | -21.4 | -0.21 | 43.5 | no edge shown yet |
| follow_move+sharp_gap | moneyline | 43-28 | 60.6 | 49.1 | 11.5 | +5.86 | 8.3 | 0.24 | 49.3 | no edge shown yet |
| money_moving+sharp_gap | moneyline | 29-40 | 42.0 | 45.9 | -3.9 | -11.48 | -16.6 | 0.44 | 59.4 | DROP: below break-even |
| consensus_gap+money_moving | moneyline | 15-25 | 37.5 | 50.0 | -12.5 | -13.06 | -32.7 | 0.59 | 50.0 | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 16-19 | 45.7 | 29.5 | 16.2 | +10.12 | 28.9 | 0.15 | 51.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 12-13 | 48.0 | 28.3 | 19.7 | +11.25 | 45.0 | -0.17 | 44.0 | keep collecting (25/30) |
| rlm_quiet+sharp_gap | moneyline | 12-16 | 42.9 | 28.3 | 14.6 | +8.25 | 29.5 | -0.29 | 42.9 | keep collecting (28/30) |
| rlm_ratio+sharp_gap | moneyline | 16-19 | 45.7 | 29.5 | 16.2 | +10.12 | 28.9 | 0.15 | 51.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 28.3 | -3.3 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_quiet | moneyline | 9-12 | 42.9 | 28.3 | 14.6 | +5.78 | 27.5 | 0.73 | 52.4 | keep collecting (21/30) |
| money_moving+rlm_ratio | moneyline | 7-6 | 53.8 | 28.3 | 25.6 | +7.63 | 58.7 | 0.55 | 53.8 | keep collecting (13/30) |
| money_delta+money_moving | moneyline | 4-7 | 36.4 | 28.3 | 8.1 | +1.99 | 18.1 | 0.29 | 63.6 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 4-6 | 40.0 | 28.3 | 11.7 | +2.99 | 29.9 | 0.32 | 70.0 | keep collecting (10/30) |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 42.8 | -42.8 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-2 | 50.0 | 50.0 | 0.0 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| money_level+pin_move | moneyline | 2-2 | 50.0 | 50.0 | 0.0 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 28.3 | -28.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-3 | 25.0 | 39.1 | -14.1 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 28.3 | -28.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_quiet | moneyline | 0-1 | 0.0 | 28.3 | -28.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-3 | 25.0 | 39.1 | -14.1 | -2.07 | -51.8 | -0.7 | 50.0 | keep collecting (4/30) |
| pin_rlm+sharp_gap | moneyline | 1-4 | 20.0 | 37.0 | -17.0 | -3.07 | -61.5 | -0.3 | 60.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 28.3 | -28.3 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | -1.55 | 50.0 | keep collecting (2/30) |
| pin_move+sharp_gap | moneyline | 2-1 | 66.7 | 42.8 | 23.9 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+rlm_ratio | moneyline | 4-6 | 40.0 | 32.6 | 7.4 | -1.13 | -11.3 | 0.95 | 70.0 | keep collecting (10/30) |
| money_level+pin_rlm | moneyline | 1-2 | 33.3 | 42.8 | -9.4 | -1.07 | -35.8 | 0.67 | 66.7 | keep collecting (3/30) |
| pin_move+pin_rlm | moneyline | 1-1 | 50.0 | 28.3 | 21.7 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| pin_move+rlm_ratio | moneyline | 1-1 | 50.0 | 28.3 | 21.7 | -0.07 | -3.7 | 0.25 | 50.0 | keep collecting (2/30) |
| follow_move+money_delta | moneyline | 4-1 | 80.0 | 28.3 | 51.7 | +7.99 | 159.8 | 0.36 | 60.0 | keep collecting (5/30) |
| money_delta+rlm_quiet | moneyline | 3-1 | 75.0 | 28.3 | 46.7 | +6.35 | 158.8 | -0.5 | 50.0 | keep collecting (4/30) |
| money_delta+rlm_ratio | moneyline | 4-0 | 100.0 | 28.3 | 71.7 | +8.99 | 224.8 | 1.75 | 75.0 | keep collecting (4/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 28.3 | -28.3 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-2 | 33.3 | 28.3 | 5.0 | -0.36 | -12.0 | 2.5 | 100.0 | keep collecting (3/30) |
| money_level+pin_value | moneyline | 0-1 | 0.0 | 71.7 | -71.7 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 71.7 | -71.7 | -1.0 | -100.0 | 1.7 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 47.3 | -1.9 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 47.3 | 36.0 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 15-9 | 62.5 | 48.4 | 14.1 | +3.84 | 16.0 | 0.29 | 37.5 | keep collecting (24/30) |
| follow_move+rlm_quiet | spread | 3-2 | 60.0 | 49.5 | 10.5 | +0.65 | 13.0 | -0.8 | 0.0 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 3-3 | 50.0 | 51.8 | -1.8 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-7 | 58.8 | 48.9 | 9.9 | +2.09 | 12.3 | 0.88 | 41.2 | keep collecting (17/30) |
| money_level+money_moving | spread | 10-6 | 62.5 | 48.7 | 13.8 | +3.12 | 19.5 | 1.19 | 68.8 | keep collecting (16/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.9 | -6.0 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 4-3 | 57.1 | 49.6 | 7.5 | +0.41 | 5.8 | 0.57 | 57.1 | keep collecting (7/30) |
| rlm_quiet+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_quiet+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -1.5 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 3-3 | 50.0 | 51.8 | -1.8 | -0.16 | -2.7 | 0.33 | 16.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 52.7 | -52.7 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 52.7 | -52.7 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-12 | 53.8 | 49.2 | 4.7 | +0.62 | 2.4 | 1.15 | 46.2 | keep collecting (26/30) |
| money_moving+sharp_gap | spread | 10-5 | 66.7 | 49.5 | 17.2 | +4.04 | 26.9 | 0.87 | 53.3 | keep collecting (15/30) |
| pin_value+sharp_gap | spread | 2-2 | 50.0 | 50.0 | 0.0 | -0.26 | -6.5 | 0.75 | 75.0 | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 9-12 | 42.9 | 48.1 | -5.2 | -4.2 | -20.0 | 1.0 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 47.3 | 15.2 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 12-10 | 54.5 | 48.5 | 6.0 | +0.98 | 4.5 | 0.82 | 45.5 | keep collecting (22/30) |
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
| pin_move+pin_value | spread | 1-5 | 16.7 | 48.2 | -31.6 | -4.09 | -68.2 | 0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+pin_move | spread | 0-3 | 0.0 | 49.1 | -49.1 | -3.0 | -100.0 | 0.33 | 33.3 | keep collecting (3/30) |
| follow_move+pin_move | spread | 2-3 | 40.0 | 47.3 | -7.3 | -1.15 | -23.0 | 0.0 | 20.0 | keep collecting (5/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.7 | -52.7 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_move | spread | 1-0 | 100.0 | 47.3 | 52.7 | +0.94 | 94.3 | -1.0 | 0.0 | keep collecting (1/30) |
| follow_move+rlm_quiet | total | 18-20 | 47.4 | 49.6 | -2.2 | -3.59 | -9.5 | 0.76 | 55.3 | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_level+money_moving | total | 35-26 | 57.4 | 50.2 | 7.2 | +6.0 | 9.8 | -0.11 | 36.1 | no edge shown yet |
| money_level+sharp_gap | total | 55-43 | 56.1 | 50.2 | 6.0 | +7.01 | 7.1 | -0.07 | 35.7 | no edge shown yet |
| money_moving+sharp_gap | total | 43-26 | 62.3 | 49.9 | 12.4 | +13.21 | 19.1 | 0.26 | 37.7 | PROMOTE: beats break-even and its own base rate |
| book_lag+pin_move | total | 0-1 | 0.0 | 50.5 | -50.5 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 11-7 | 61.1 | 49.9 | 11.2 | +2.96 | 16.4 | 0.33 | 33.3 | keep collecting (18/30) |
| money_moving+pin_value | total | 8-4 | 66.7 | 49.7 | 16.9 | +3.24 | 27.0 | 0.33 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | total | 12-8 | 60.0 | 49.9 | 10.1 | +2.83 | 14.1 | 0.15 | 35.0 | keep collecting (20/30) |
| follow_move+money_level | total | 32-28 | 53.3 | 50.2 | 3.1 | +1.08 | 1.8 | 0.18 | 41.7 | no edge shown yet |
| follow_move+pin_value | total | 10-12 | 45.5 | 50.0 | -4.6 | -3.03 | -13.8 | -0.41 | 27.3 | keep collecting (22/30) |
| follow_move+rlm_ratio | total | 17-10 | 63.0 | 49.5 | 13.4 | +5.62 | 20.8 | 0.78 | 63.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 41-25 | 62.1 | 49.9 | 12.2 | +12.37 | 18.7 | 0.48 | 47.0 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 6-5 | 54.5 | 49.6 | 5.0 | +0.54 | 4.9 | 1.09 | 72.7 | keep collecting (11/30) |
| pin_value+rlm_ratio | total | 3-1 | 75.0 | 49.7 | 25.3 | +1.73 | 43.2 | -0.25 | 50.0 | keep collecting (4/30) |
| rlm_ratio+sharp_gap | total | 17-10 | 63.0 | 49.5 | 13.4 | +5.62 | 20.8 | 0.78 | 63.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 25-22 | 53.2 | 49.9 | 3.3 | +0.88 | 1.9 | 0.55 | 48.9 | no edge shown yet |
| consensus_gap+money_level | total | 9-6 | 60.0 | 50.3 | 9.7 | +2.03 | 13.5 | -0.4 | 20.0 | keep collecting (15/30) |
| consensus_gap+money_moving | total | 7-1 | 87.5 | 50.0 | 37.5 | +5.3 | 66.2 | 0.12 | 37.5 | keep collecting (8/30) |
| consensus_gap+pin_value | total | 13-16 | 44.8 | 50.1 | -5.3 | -4.34 | -14.9 | 0.34 | 48.3 | keep collecting (29/30) |
| consensus_gap+sharp_gap | total | 9-10 | 47.4 | 50.0 | -2.6 | -1.89 | -10.0 | -0.05 | 31.6 | keep collecting (19/30) |
| money_moving+rlm_ratio | total | 10-5 | 66.7 | 49.6 | 17.1 | +4.22 | 28.1 | 0.67 | 60.0 | keep collecting (15/30) |
| consensus_gap+follow_move | total | 18-16 | 52.9 | 50.0 | 3.0 | +0.33 | 1.0 | 1.47 | 67.6 | no edge shown yet |
| consensus_gap+money_delta | total | 3-0 | 100.0 | 50.2 | 49.8 | +2.69 | 89.6 | 0.33 | 33.3 | keep collecting (3/30) |
| follow_move+money_delta | total | 3-3 | 50.0 | 49.6 | 0.4 | -0.31 | -5.2 | 1.33 | 66.7 | keep collecting (6/30) |
| money_delta+money_moving | total | 8-3 | 72.7 | 49.7 | 23.1 | +4.17 | 37.9 | 1.36 | 45.5 | keep collecting (11/30) |
| money_delta+pin_value | total | 3-0 | 100.0 | 49.8 | 50.2 | +2.69 | 89.6 | 0.0 | 33.3 | keep collecting (3/30) |
| money_delta+sharp_gap | total | 7-2 | 77.8 | 49.7 | 28.1 | +4.26 | 47.4 | 1.67 | 55.6 | keep collecting (9/30) |
| money_moving+rlm_quiet | total | 8-6 | 57.1 | 49.5 | 7.6 | +1.27 | 9.1 | 0.43 | 42.9 | keep collecting (14/30) |
| pin_value+rlm_quiet | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| rlm_quiet+rlm_ratio | total | 9-5 | 64.3 | 49.5 | 14.8 | +3.22 | 23.0 | 0.71 | 64.3 | keep collecting (14/30) |
| rlm_quiet+sharp_gap | total | 11-6 | 64.7 | 49.5 | 15.2 | +4.04 | 23.8 | 0.76 | 58.8 | keep collecting (17/30) |
| follow_move+pin_move | total | 3-4 | 42.9 | 49.8 | -6.9 | -1.23 | -17.6 | 0.57 | 57.1 | keep collecting (7/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 49.5 | -49.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 49.5 | -49.5 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 3-2 | 60.0 | 49.7 | 10.3 | +0.73 | 14.5 | 0.8 | 60.0 | keep collecting (5/30) |
| consensus_gap+rlm_quiet | total | 2-2 | 50.0 | 49.5 | 0.5 | -0.14 | -3.5 | 1.0 | 75.0 | keep collecting (4/30) |
| consensus_gap+rlm_ratio | total | 4-1 | 80.0 | 49.5 | 30.5 | +2.68 | 53.6 | 0.4 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | total | 1-4 | 20.0 | 50.5 | -30.5 | -3.09 | -61.8 | 0.4 | 20.0 | keep collecting (5/30) |
| pin_move+pin_value | total | 3-5 | 37.5 | 50.3 | -12.8 | -2.23 | -27.9 | 0.5 | 37.5 | keep collecting (8/30) |
| pin_move+sharp_gap | total | 0-3 | 0.0 | 50.5 | -50.5 | -3.0 | -100.0 | 1.0 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_quiet | total | 0-1 | 0.0 | 49.5 | -49.5 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 1-2 | 33.3 | 49.5 | -16.1 | -1.09 | -36.4 | 1.67 | 100.0 | keep collecting (3/30) |
| consensus_gap+pin_move | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | 0.5 | 50.0 | keep collecting (2/30) |
| money_moving+pin_move | total | 1-1 | 50.0 | 49.5 | 0.5 | -0.05 | -2.4 | 1.0 | 100.0 | keep collecting (2/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| rlm_quiet | both | 270-399 | 40.4 | 42.0 | -1.6 | -69.69 | -10.4 |  |  | DROP: below break-even |
| pin_move | both | 649-688 | 48.5 | 49.8 | -1.2 | -75.44 | -5.6 |  |  | DROP: below break-even |
| money_delta | both | 402-523 | 43.5 | 44.3 | -0.8 | -67.37 | -7.3 |  |  | DROP: below break-even |
| pin_rlm | both | 167-213 | 43.9 | 42.3 | 1.7 | +5.87 | 1.5 |  |  | DROP: below break-even |
| follow_move | both | 1117-1069 | 51.1 | 51.1 | 0.0 | -157.52 | -7.2 |  |  | no edge shown yet |
| rlm_ratio | both | 252-314 | 44.5 | 43.8 | 0.7 | -30.57 | -5.4 |  |  | DROP: below break-even |
| money_level | both | 1417-1071 | 57.0 | 55.4 | 1.5 | -101.92 | -4.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 1096-1285 | 46.0 | 47.7 | -1.7 | -199.22 | -8.4 |  |  | DROP: below break-even |
| money_moving | both | 1109-1276 | 46.5 | 48.1 | -1.6 | -192.64 | -8.1 |  |  | DROP: below break-even |
| pin_value | both | 483-487 | 49.8 | 48.5 | 1.3 | +5.09 | 0.5 |  |  | DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 50.9 | 15.8 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 438-539 | 44.8 | 48.6 | -3.7 | -91.82 | -9.4 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 156-160 | 49.4 | 51.3 | -1.9 | -26.38 | -8.3 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 182-288 | 38.7 | 45.9 | -7.2 | -46.83 | -10.0 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 109-106 | 50.7 | 50.8 | -0.1 | +8.68 | 4.0 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 26-47 | 35.6 | 38.8 | -3.2 | +6.31 | 8.6 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 173-182 | 48.7 | 46.6 | 2.2 | +7.52 | 2.1 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | both | 30-52 | 36.6 | 40.0 | -3.4 | -4.61 | -5.6 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 181-295 | 38.0 | 45.4 | -7.3 | -50.68 | -10.6 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 583-647 | 47.4 | 49.1 | -1.7 | -115.2 | -9.4 |  |  | DROP: below break-even |
| follow_move+pin_move | both | 461-508 | 47.6 | 49.9 | -2.3 | -89.07 | -9.2 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 132-159 | 45.4 | 43.7 | 1.7 | -12.95 | -4.5 |  |  | DROP: below break-even |
| follow_move+pin_value | both | 165-161 | 50.6 | 49.3 | 1.3 | -4.5 | -1.4 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 252-314 | 44.5 | 43.8 | 0.7 | -30.57 | -5.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 585-647 | 47.5 | 48.9 | -1.4 | -107.38 | -8.7 |  |  | DROP: below break-even |
| money_moving+pin_move | both | 361-420 | 46.2 | 48.6 | -2.4 | -60.55 | -7.8 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 161-203 | 44.2 | 42.4 | 1.8 | +9.9 | 2.7 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 201-246 | 45.0 | 47.8 | -2.8 | -33.06 | -7.4 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 243-302 | 44.6 | 43.9 | 0.7 | -28.2 | -5.2 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 1055-1228 | 46.2 | 47.8 | -1.6 | -176.82 | -7.7 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 154-180 | 46.1 | 43.9 | 2.2 | +3.32 | 1.0 |  |  | DROP: below break-even |
| pin_move+pin_value | both | 208-213 | 49.4 | 49.5 | -0.1 | -16.82 | -4.0 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 140-156 | 47.3 | 45.0 | 2.3 | -4.27 | -1.4 |  |  | DROP: below break-even |
| pin_move+sharp_gap | both | 364-428 | 46.0 | 48.4 | -2.4 | -64.48 | -8.1 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 44-50 | 46.8 | 46.4 | 0.4 | +7.15 | 7.6 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 132-159 | 45.4 | 43.7 | 1.7 | -12.95 | -4.5 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | both | 167-213 | 43.9 | 42.3 | 1.7 | +5.87 | 1.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 43-38 | 53.1 | 48.7 | 4.4 | +1.14 | 1.4 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 202-249 | 44.8 | 47.8 | -3.0 | -35.17 | -7.8 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 252-314 | 44.5 | 43.8 | 0.7 | -30.57 | -5.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 193-242 | 44.4 | 45.6 | -1.2 | -45.98 | -10.6 |  |  | DROP: below break-even |
| money_level+money_moving | both | 777-703 | 52.5 | 52.5 | -0.0 | -78.74 | -5.3 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 757-695 | 52.1 | 52.3 | -0.2 | -76.97 | -5.3 |  |  | no edge shown yet |
| follow_move+money_level | both | 688-512 | 57.3 | 56.2 | 1.1 | -69.45 | -5.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 115-100 | 53.5 | 48.1 | 5.4 | +10.24 | 4.8 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 273-213 | 56.2 | 58.1 | -1.9 | -30.59 | -6.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_move | both | 361-342 | 51.4 | 53.3 | -1.9 | -49.53 | -7.0 |  |  | no edge shown yet |
| money_level+pin_value | both | 228-219 | 51.0 | 50.1 | 0.9 | -20.61 | -4.6 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | both | 25-63 | 28.4 | 37.0 | -8.6 | -18.04 | -20.5 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | both | 270-399 | 40.4 | 42.0 | -1.6 | -69.69 | -10.4 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+sharp_gap | both | 133-223 | 37.4 | 41.4 | -4.1 | -53.48 | -15.0 |  |  | DROP: below break-even |
| money_delta+money_moving | both | 288-407 | 41.4 | 42.7 | -1.2 | -56.52 | -8.1 |  |  | DROP: below break-even |
| consensus_gap+money_delta | both | 52-116 | 31.0 | 38.4 | -7.4 | -24.17 | -14.4 |  |  | DROP: below break-even |
| money_delta+money_level | both | 138-131 | 51.3 | 47.3 | 4.0 | +12.36 | 4.6 |  |  | no edge shown yet |
| money_delta+pin_value | both | 84-82 | 50.6 | 47.4 | 3.2 | +1.51 | 0.9 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 285-401 | 41.5 | 42.7 | -1.1 | -53.69 | -7.8 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | both | 106-187 | 36.2 | 40.1 | -3.9 | -43.27 | -14.8 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | both | 125-218 | 36.4 | 41.4 | -4.9 | -54.52 | -15.9 |  |  | DROP: below break-even |
| money_delta+rlm_quiet | both | 74-132 | 35.9 | 42.5 | -6.6 | -49.05 | -23.8 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | both | 128-178 | 41.8 | 43.9 | -2.1 | -31.35 | -10.2 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | both | 55-99 | 35.7 | 40.5 | -4.8 | -28.82 | -18.7 |  |  | DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 50.9 | 15.8 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 139-177 | 44.0 | 46.2 | -2.2 | -27.84 | -8.8 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 73-55 | 57.0 | 47.0 | 10.0 | +16.73 | 13.1 |  |  | no edge shown yet |
| money_delta+pin_rlm | both | 96-123 | 43.8 | 42.3 | 1.5 | -2.39 | -1.1 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | both | 140-165 | 45.9 | 44.1 | 1.8 | -17.65 | -5.8 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | both | 34-50 | 40.5 | 47.5 | -7.0 | -8.77 | -10.4 |  |  | DROP: below break-even |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 49.5 | 50.5 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| rlm_quiet | moneyline | 83-176 | 32.0 | 29.1 | 2.9 | -19.54 | -7.5 |  |  | DROP: below break-even |
| rlm_quiet | spread | 63-66 | 48.8 | 51.1 | -2.3 | -7.42 | -5.8 |  |  | no edge shown yet |
| rlm_quiet | total | 124-157 | 44.1 | 49.7 | -5.5 | -42.73 | -15.2 |  |  | DROP: below break-even |
| pin_move | moneyline | 149-147 | 50.3 | 48.7 | 1.7 | +9.58 | 3.2 |  |  | no edge shown yet |
| pin_move | spread | 246-269 | 47.8 | 50.3 | -2.5 | -45.14 | -8.8 |  |  | DROP: below break-even |
| pin_move | total | 254-272 | 48.3 | 49.9 | -1.6 | -39.88 | -7.6 |  |  | DROP: below break-even |
| money_delta | moneyline | 72-204 | 26.1 | 30.3 | -4.2 | -50.22 | -18.2 |  |  | DROP: below break-even |
| money_delta | spread | 138-137 | 50.2 | 50.9 | -0.7 | -11.17 | -4.1 |  |  | no edge shown yet |
| money_delta | total | 192-182 | 51.3 | 49.7 | 1.7 | -5.99 | -1.6 |  |  | no edge shown yet |
| pin_rlm | moneyline | 48-99 | 32.7 | 30.1 | 2.6 | +10.99 | 7.5 |  |  | DROP: below break-even |
| pin_rlm | spread | 28-25 | 52.8 | 51.2 | 1.7 | +0.48 | 0.9 |  |  | no edge shown yet |
| pin_rlm | total | 91-89 | 50.6 | 49.6 | 0.9 | -5.61 | -3.1 |  |  | no edge shown yet |
| follow_move | moneyline | 408-309 | 56.9 | 53.7 | 3.2 | -44.43 | -6.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 320-345 | 48.1 | 49.7 | -1.6 | -53.5 | -8.0 |  |  | DROP: below break-even |
| follow_move | total | 389-415 | 48.4 | 49.9 | -1.6 | -59.59 | -7.4 |  |  | DROP: below break-even |
| rlm_ratio | moneyline | 55-124 | 30.7 | 30.7 | 0.0 | -20.61 | -11.5 |  |  | DROP: below break-even |
| rlm_ratio | spread | 48-48 | 50.0 | 50.3 | -0.3 | -4.49 | -4.7 |  |  | no edge shown yet |
| rlm_ratio | total | 149-142 | 51.2 | 49.7 | 1.5 | -5.46 | -1.9 |  |  | no edge shown yet |
| money_level | moneyline | 556-233 | 70.5 | 67.8 | 2.7 | -42.26 | -5.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 391-403 | 49.2 | 49.2 | 0.0 | -50.83 | -6.4 |  |  | DROP: below break-even |
| money_level | total | 470-435 | 51.9 | 50.2 | 1.8 | -8.83 | -1.0 |  |  | no edge shown yet |
| sharp_gap | moneyline | 283-438 | 39.3 | 43.0 | -3.8 | -89.89 | -12.5 |  |  | DROP: below break-even |
| sharp_gap | spread | 397-389 | 50.5 | 49.6 | 0.9 | -31.09 | -4.0 |  |  | no edge shown yet |
| sharp_gap | total | 416-458 | 47.6 | 49.9 | -2.3 | -78.25 | -9.0 |  |  | DROP: below break-even |
| money_moving | moneyline | 300-416 | 41.9 | 44.2 | -2.3 | -66.31 | -9.3 |  |  | DROP: below break-even |
| money_moving | spread | 394-392 | 50.1 | 49.5 | 0.6 | -36.96 | -4.7 |  |  | no edge shown yet |
| money_moving | total | 415-468 | 47.0 | 49.9 | -2.9 | -89.38 | -10.1 |  |  | DROP: below break-even |
| pin_value | moneyline | 24-63 | 27.6 | 34.3 | -6.7 | +22.6 | 26.0 |  |  | DROP: below break-even |
| pin_value | spread | 221-201 | 52.4 | 49.6 | 2.8 | -8.8 | -2.1 |  |  | no edge shown yet |
| pin_value | total | 238-223 | 51.6 | 50.1 | 1.5 | -8.71 | -1.9 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.7 | 47.3 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 196-316 | 38.3 | 47.5 | -9.2 | -80.18 | -15.7 |  |  | DROP: below break-even |
| consensus_gap | spread | 108-95 | 53.2 | 49.2 | 4.0 | -2.67 | -1.3 |  |  | no edge shown yet |
| consensus_gap | total | 134-128 | 51.1 | 50.3 | 0.9 | -8.97 | -3.4 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 205-121 | 62.9 | 62.8 | 0.1 | -14.1 | -4.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 188-122 | 60.6 | 62.2 | -1.5 | -18.74 | -6.0 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 265-398 | 40.0 | 43.1 | -3.1 | -63.33 | -9.6 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 70-84 | 45.5 | 53.1 | -7.6 | -25.38 | -16.5 |  |  | DROP: below break-even |
| consensus_gap+rlm_quiet | moneyline | 9-48 | 15.8 | 29.8 | -14.0 | -17.24 | -30.2 |  |  | DROP: below break-even |
| follow_move+rlm_quiet | moneyline | 83-176 | 32.0 | 29.1 | 2.9 | -19.54 | -7.5 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 140-84 | 62.5 | 68.0 | -5.5 | -17.49 | -7.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 73-174 | 29.6 | 42.5 | -13.0 | -27.74 | -11.2 |  |  | !! CHECK: consensus_gap+money_moving close moneyline all sits -13.0 pts from its base (42.5%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+money_level | moneyline | 300-112 | 72.8 | 68.8 | 4.1 | -21.51 | -5.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+money_moving | moneyline | 149-166 | 47.3 | 47.4 | -0.1 | -28.82 | -9.1 |  |  | DROP: below break-even |
| money_delta+money_moving | moneyline | 67-185 | 26.6 | 29.8 | -3.2 | -35.92 | -14.3 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 65-184 | 26.1 | 29.9 | -3.8 | -37.11 | -14.9 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 71-182 | 28.1 | 41.5 | -13.4 | -33.48 | -13.2 |  |  | !! CHECK: consensus_gap+sharp_gap close moneyline all sits -13.4 pts from its base (41.5%). Verify the base is the right comparison and the sample is not a composition artifact.  ||  DROP: below break-even |
| follow_move+sharp_gap | moneyline | 142-169 | 45.7 | 46.4 | -0.8 | -32.47 | -10.4 |  |  | DROP: below break-even |
| money_moving+rlm_quiet | moneyline | 37-103 | 26.4 | 28.9 | -2.5 | -20.17 | -14.4 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | moneyline | 38-106 | 26.4 | 28.9 | -2.5 | -23.57 | -16.4 |  |  | DROP: below break-even |
| consensus_gap+pin_move | moneyline | 44-41 | 51.8 | 52.3 | -0.5 | +16.99 | 20.0 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 12-32 | 27.3 | 31.2 | -4.0 | +9.05 | 20.6 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 6-36 | 14.3 | 30.4 | -16.1 | -9.64 | -23.0 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 117-107 | 52.2 | 49.6 | 2.6 | -2.22 | -1.0 |  |  | no edge shown yet |
| follow_move+pin_rlm | moneyline | 33-61 | 35.1 | 30.6 | 4.5 | -5.84 | -6.2 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 55-124 | 30.7 | 30.7 | 0.0 | -20.61 | -11.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 64-83 | 43.5 | 43.1 | 0.5 | +6.5 | 4.4 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 47-92 | 33.8 | 30.2 | 3.7 | +16.59 | 11.9 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 53-116 | 31.4 | 30.9 | 0.5 | -15.73 | -9.3 |  |  | DROP: below break-even |
| pin_move+pin_rlm | moneyline | 35-66 | 34.7 | 30.0 | 4.6 | +8.45 | 8.4 |  |  | DROP: below break-even |
| pin_move+rlm_quiet | moneyline | 36-59 | 37.9 | 29.7 | 8.2 | +2.58 | 2.7 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 28-49 | 36.4 | 31.1 | 5.3 | +0.22 | 0.3 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 62-89 | 41.1 | 42.1 | -1.0 | -0.07 | -0.0 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | moneyline | 20-51 | 28.2 | 29.5 | -1.3 | -12.98 | -18.3 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 33-61 | 35.1 | 30.6 | 4.5 | -5.84 | -6.2 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 48-99 | 32.7 | 30.1 | 2.6 | +10.99 | 7.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_quiet+rlm_ratio | moneyline | 35-101 | 25.7 | 28.9 | -3.2 | -22.41 | -16.5 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | moneyline | 55-124 | 30.7 | 30.7 | 0.0 | -20.61 | -11.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 14-85 | 14.1 | 30.0 | -15.9 | -26.27 | -26.5 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 16-49 | 24.6 | 32.3 | -7.7 | +3.85 | 5.9 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 21-46 | 31.3 | 31.5 | -0.2 | -4.82 | -7.2 |  |  | DROP: below break-even |
| money_delta+pin_rlm | moneyline | 28-57 | 32.9 | 30.3 | 2.6 | +1.39 | 1.6 |  |  | DROP: below break-even |
| money_delta+pin_value | moneyline | 3-18 | 14.3 | 28.3 | -14.0 | -6.68 | -31.8 |  |  | keep collecting (21/30) |
| money_moving+pin_value | moneyline | 12-35 | 25.5 | 32.0 | -6.4 | +11.51 | 24.5 |  |  | DROP: below break-even |
| pin_move+pin_value | moneyline | 8-13 | 38.1 | 40.7 | -2.6 | +4.92 | 23.4 |  |  | keep collecting (21/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 28.3 | 3.0 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 12-39 | 23.5 | 33.4 | -9.9 | +7.51 | 14.7 |  |  | DROP: below break-even |
| follow_move+money_delta | moneyline | 36-73 | 33.0 | 32.7 | 0.4 | -20.36 | -18.7 |  |  | DROP: below break-even |
| money_delta+money_level | moneyline | 20-26 | 43.5 | 34.9 | 8.6 | +10.18 | 22.1 |  |  | no edge shown yet |
| money_delta+rlm_ratio | moneyline | 31-63 | 33.0 | 31.5 | 1.5 | -14.85 | -15.8 |  |  | DROP: below break-even |
| money_level+pin_move | moneyline | 91-55 | 62.3 | 66.4 | -4.0 | -7.05 | -4.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 13-12 | 52.0 | 35.2 | 16.8 | +4.93 | 19.7 |  |  | keep collecting (25/30) |
| money_level+rlm_ratio | moneyline | 16-17 | 48.5 | 38.8 | 9.7 | +3.18 | 9.6 |  |  | no edge shown yet |
| money_delta+rlm_quiet | moneyline | 22-56 | 28.2 | 30.0 | -1.8 | -21.02 | -27.0 |  |  | DROP: below break-even |
| money_level+pin_value | moneyline | 6-7 | 46.2 | 65.0 | -18.9 | -3.75 | -28.9 |  |  | keep collecting (13/30) |
| follow_move+pin_value | moneyline | 4-10 | 28.6 | 40.7 | -12.1 | +3.37 | 24.1 |  |  | keep collecting (14/30) |
| pin_value+rlm_quiet | moneyline | 2-7 | 22.2 | 28.3 | -6.1 | +5.12 | 56.9 |  |  | keep collecting (9/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 28.3 | -3.3 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 38-32 | 54.3 | 48.5 | 5.7 | +0.48 | 0.7 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 53-51 | 51.0 | 49.0 | 2.0 | -5.79 | -5.6 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 32-37 | 46.4 | 49.5 | -3.1 | -9.61 | -13.9 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 4-4 | 50.0 | 50.7 | -0.7 | -0.61 | -7.6 |  |  | keep collecting (8/30) |
| consensus_gap+pin_value | spread | 78-59 | 56.9 | 49.2 | 7.7 | +7.56 | 5.5 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 5-4 | 55.6 | 50.3 | 5.3 | +0.18 | 2.0 |  |  | keep collecting (9/30) |
| consensus_gap+sharp_gap | spread | 52-51 | 50.5 | 49.1 | 1.3 | -6.69 | -6.5 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 182-188 | 49.2 | 49.4 | -0.2 | -23.27 | -6.3 |  |  | no edge shown yet |
| follow_move+pin_move | spread | 154-183 | 45.7 | 50.1 | -4.4 | -42.6 | -12.6 |  |  | DROP: below break-even |
| follow_move+pin_rlm | spread | 20-20 | 50.0 | 50.8 | -0.8 | -1.74 | -4.3 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 72-64 | 52.9 | 49.2 | 3.7 | -1.18 | -0.9 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 48-48 | 50.0 | 50.3 | -0.3 | -4.49 | -4.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 183-187 | 49.5 | 49.4 | 0.1 | -21.14 | -5.7 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 133-149 | 47.2 | 49.9 | -2.7 | -28.82 | -10.2 |  |  | DROP: below break-even |
| money_moving+pin_rlm | spread | 26-25 | 51.0 | 51.1 | -0.1 | -1.34 | -2.6 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 99-106 | 48.3 | 49.3 | -1.0 | -20.73 | -10.1 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 46-47 | 49.5 | 50.2 | -0.7 | -5.42 | -5.8 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 389-384 | 50.3 | 49.5 | 0.8 | -33.46 | -4.3 |  |  | no edge shown yet |
| pin_move+pin_rlm | spread | 28-25 | 52.8 | 51.2 | 1.7 | +0.48 | 0.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 99-101 | 49.5 | 49.9 | -0.4 | -13.94 | -7.0 |  |  | no edge shown yet |
| pin_move+rlm_ratio | spread | 25-27 | 48.1 | 50.7 | -2.6 | -4.28 | -8.2 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 136-149 | 47.7 | 49.9 | -2.2 | -26.09 | -9.2 |  |  | DROP: below break-even |
| pin_rlm+pin_value | spread | 9-11 | 45.0 | 51.1 | -6.1 | -3.1 | -15.5 |  |  | keep collecting (20/30) |
| pin_rlm+rlm_ratio | spread | 20-20 | 50.0 | 50.8 | -0.8 | -1.74 | -4.3 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 28-25 | 52.8 | 51.2 | 1.7 | +0.48 | 0.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 8-8 | 50.0 | 49.7 | 0.3 | -1.17 | -7.3 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | spread | 99-106 | 48.3 | 49.3 | -1.0 | -20.79 | -10.1 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 48-48 | 50.0 | 50.3 | -0.3 | -4.49 | -4.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 175-188 | 48.2 | 49.1 | -0.9 | -29.59 | -8.2 |  |  | DROP: below break-even |
| money_level+rlm_ratio | spread | 26-29 | 47.3 | 50.0 | -2.7 | -5.64 | -10.2 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 303-301 | 50.2 | 49.2 | 1.0 | -28.34 | -4.7 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 62-58 | 51.7 | 48.7 | 3.0 | -5.01 | -4.2 |  |  | no edge shown yet |
| money_level+money_moving | spread | 302-302 | 50.0 | 49.2 | 0.8 | -30.26 | -5.0 |  |  | no edge shown yet |
| money_level+pin_move | spread | 122-147 | 45.4 | 49.6 | -4.3 | -37.15 | -13.8 |  |  | DROP: below break-even |
| money_level+pin_value | spread | 106-109 | 49.3 | 48.9 | 0.4 | -17.8 | -8.3 |  |  | no edge shown yet |
| consensus_gap+money_delta | spread | 17-15 | 53.1 | 50.8 | 2.3 | -0.46 | -1.4 |  |  | no edge shown yet |
| follow_move+money_delta | spread | 45-52 | 46.4 | 50.4 | -4.0 | -11.24 | -11.6 |  |  | no edge shown yet |
| money_delta+money_level | spread | 45-43 | 51.1 | 50.0 | 1.1 | -2.5 | -2.8 |  |  | no edge shown yet |
| money_delta+money_moving | spread | 78-83 | 48.4 | 50.5 | -2.1 | -12.6 | -7.8 |  |  | no edge shown yet |
| money_delta+pin_value | spread | 36-30 | 54.5 | 50.7 | 3.8 | +1.45 | 2.2 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 77-81 | 48.7 | 50.5 | -1.7 | -11.58 | -7.3 |  |  | no edge shown yet |
| follow_move+rlm_quiet | spread | 63-66 | 48.8 | 51.1 | -2.3 | -7.42 | -5.8 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| rlm_quiet+rlm_ratio | spread | 15-7 | 68.2 | 51.2 | 17.0 | +6.65 | 30.2 |  |  | keep collecting (22/30) |
| rlm_quiet+sharp_gap | spread | 25-16 | 61.0 | 51.4 | 9.6 | +6.83 | 16.6 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 15-12 | 55.6 | 50.5 | 5.1 | +1.48 | 5.5 |  |  | keep collecting (27/30) |
| money_delta+pin_move | spread | 41-49 | 45.6 | 51.1 | -5.6 | -11.64 | -12.9 |  |  | no edge shown yet |
| money_delta+rlm_ratio | spread | 19-29 | 39.6 | 50.0 | -10.4 | -12.18 | -25.4 |  |  | DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 52.7 | 47.3 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_rlm | spread | 15-18 | 45.5 | 50.9 | -5.4 | -4.52 | -13.7 |  |  | no edge shown yet |
| money_delta+rlm_quiet | spread | 18-20 | 47.4 | 51.5 | -4.2 | -3.29 | -8.7 |  |  | no edge shown yet |
| money_moving+rlm_quiet | spread | 24-16 | 60.0 | 51.3 | 8.7 | +5.87 | 14.7 |  |  | no edge shown yet |
| pin_move+rlm_quiet | spread | 35-37 | 48.6 | 51.5 | -2.9 | -4.46 | -6.2 |  |  | no edge shown yet |
| pin_rlm+rlm_quiet | spread | 6-3 | 66.7 | 52.1 | 14.6 | +2.56 | 28.4 |  |  | keep collecting (9/30) |
| consensus_gap+rlm_quiet | spread | 4-3 | 57.1 | 51.1 | 6.0 | +0.48 | 6.9 |  |  | keep collecting (7/30) |
| pin_value+rlm_quiet | spread | 7-7 | 50.0 | 50.4 | -0.4 | -0.85 | -6.1 |  |  | keep collecting (14/30) |
| follow_move+money_delta | total | 112-117 | 48.9 | 49.7 | -0.8 | -14.38 | -6.3 |  |  | no edge shown yet |
| money_level+money_moving | total | 270-280 | 49.1 | 50.1 | -1.0 | -34.39 | -6.3 |  |  | DROP: below break-even |
| money_level+sharp_gap | total | 266-272 | 49.4 | 50.1 | -0.6 | -29.88 | -5.6 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 401-446 | 47.3 | 49.9 | -2.6 | -80.03 | -9.4 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 71-71 | 50.0 | 50.4 | -0.4 | -8.08 | -5.7 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 33-28 | 54.1 | 50.2 | 3.9 | +1.3 | 2.1 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 79-74 | 51.6 | 50.3 | 1.4 | -3.88 | -2.5 |  |  | no edge shown yet |
| follow_move+money_moving | total | 252-293 | 46.2 | 49.9 | -3.7 | -63.11 | -11.6 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 260-291 | 47.2 | 49.9 | -2.7 | -53.77 | -9.8 |  |  | DROP: below break-even |
| money_level+pin_move | total | 148-140 | 51.4 | 50.0 | 1.3 | -5.33 | -1.9 |  |  | no edge shown yet |
| money_level+pin_value | total | 116-103 | 53.0 | 50.3 | 2.7 | +0.93 | 0.4 |  |  | no edge shown yet |
| pin_move+pin_value | total | 101-99 | 50.5 | 50.0 | 0.5 | -7.8 | -3.9 |  |  | no edge shown yet |
| follow_move+rlm_quiet | total | 124-157 | 44.1 | 49.7 | -5.5 | -42.73 | -15.2 |  |  | redundant -- identical record to rlm_quiet alone, not independent confirmation |
| money_moving+pin_move | total | 164-188 | 46.6 | 49.9 | -3.3 | -38.23 | -10.9 |  |  | DROP: below break-even |
| rlm_quiet+sharp_gap | total | 70-101 | 40.9 | 49.6 | -8.7 | -36.73 | -21.5 |  |  | DROP: below break-even |
| money_delta+money_moving | total | 143-139 | 50.7 | 49.7 | 1.0 | -8.01 | -2.8 |  |  | no edge shown yet |
| follow_move+money_level | total | 213-212 | 50.1 | 50.1 | 0.0 | -18.35 | -4.3 |  |  | no edge shown yet |
| follow_move+pin_value | total | 89-87 | 50.6 | 50.0 | 0.5 | -6.69 | -3.8 |  |  | no edge shown yet |
| money_moving+pin_value | total | 90-105 | 46.2 | 50.1 | -3.9 | -23.84 | -12.2 |  |  | DROP: below break-even |
| pin_value+sharp_gap | total | 91-104 | 46.7 | 50.0 | -3.4 | -21.89 | -11.2 |  |  | DROP: below break-even |
| consensus_gap+money_moving | total | 56-63 | 47.1 | 50.3 | -3.2 | -13.3 | -11.2 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 58-62 | 48.3 | 50.2 | -1.9 | -10.51 | -8.8 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 48-44 | 52.2 | 50.3 | 1.9 | -1.47 | -1.6 |  |  | no edge shown yet |
| consensus_gap+money_delta | total | 21-16 | 56.8 | 50.0 | 6.8 | +2.56 | 6.9 |  |  | no edge shown yet |
| consensus_gap+rlm_quiet | total | 12-12 | 50.0 | 49.9 | 0.1 | -1.28 | -5.3 |  |  | keep collecting (24/30) |
| money_delta+rlm_quiet | total | 34-56 | 37.8 | 49.5 | -11.8 | -24.74 | -27.5 |  |  | DROP: below break-even |
| money_delta+sharp_gap | total | 143-136 | 51.3 | 49.7 | 1.6 | -5.01 | -1.8 |  |  | no edge shown yet |
| money_moving+rlm_quiet | total | 64-99 | 39.3 | 49.6 | -10.4 | -40.22 | -24.7 |  |  | !! IMPLAUSIBLE: money_moving+rlm_quiet close total all 39.3% on n=163. A -110 market outside 40-60% at this sample is a measurement bug until proven otherwise. Recompute from source.  ||  DROP: below break-even |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 73-62 | 54.1 | 49.7 | 4.3 | +4.68 | 3.5 |  |  | no edge shown yet |
| money_delta+pin_move | total | 77-82 | 48.4 | 49.6 | -1.2 | -11.38 | -7.2 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 166-190 | 46.6 | 49.9 | -3.2 | -38.32 | -10.8 |  |  | DROP: below break-even |
| follow_move+pin_move | total | 190-218 | 46.6 | 49.9 | -3.3 | -44.24 | -10.8 |  |  | DROP: below break-even |
| pin_value+rlm_quiet | total | 25-36 | 41.0 | 49.7 | -8.7 | -13.04 | -21.4 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | total | 10-11 | 47.6 | 50.0 | -2.4 | -2.13 | -10.1 |  |  | keep collecting (21/30) |
| consensus_gap+rlm_ratio | total | 19-12 | 61.3 | 50.1 | 11.2 | +4.85 | 15.6 |  |  | no edge shown yet |
| follow_move+pin_rlm | total | 79-78 | 50.3 | 49.6 | 0.7 | -5.38 | -3.4 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 149-142 | 51.2 | 49.7 | 1.5 | -5.46 | -1.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 45-31 | 59.2 | 49.6 | 9.6 | +10.32 | 13.6 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 73-54 | 57.5 | 49.8 | 7.7 | +12.7 | 10.0 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 88-86 | 50.6 | 49.6 | 0.9 | -5.35 | -3.1 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 144-139 | 50.9 | 49.7 | 1.2 | -7.05 | -2.5 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 91-89 | 50.6 | 49.6 | 0.9 | -5.61 | -3.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 87-80 | 52.1 | 49.7 | 2.4 | -0.21 | -0.1 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 30-28 | 51.7 | 49.7 | 2.0 | -0.83 | -1.4 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 79-78 | 50.3 | 49.6 | 0.7 | -5.38 | -3.4 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 91-89 | 50.6 | 49.6 | 0.9 | -5.61 | -3.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 34-27 | 55.7 | 49.8 | 5.9 | +3.78 | 6.2 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 149-142 | 51.2 | 49.7 | 1.5 | -5.46 | -1.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 53-48 | 52.5 | 49.6 | 2.9 | +0.73 | 0.7 |  |  | no edge shown yet |
| money_delta+rlm_ratio | total | 90-73 | 55.2 | 49.6 | 5.6 | +9.38 | 5.8 |  |  | no edge shown yet |
| money_delta+pin_value | total | 45-34 | 57.0 | 49.7 | 7.2 | +6.74 | 8.5 |  |  | no edge shown yet |
| pin_move+rlm_quiet | total | 57-82 | 41.0 | 49.7 | -8.7 | -29.47 | -21.2 |  |  | DROP: below break-even |
| pin_rlm+rlm_quiet | total | 29-45 | 39.2 | 49.6 | -10.4 | -18.4 | -24.9 |  |  | DROP: below break-even |
| rlm_quiet+rlm_ratio | total | 56-79 | 41.5 | 49.6 | -8.1 | -27.5 | -20.4 |  |  | DROP: below break-even |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 49.5 | 50.5 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| rlm_quiet | close | 1-3k bets | 173-259 | 40.0 | -1.8 | -8.9 |  |
| rlm_quiet | close | 3k+ bets | 67-93 | 41.9 | -0.4 | -10.4 |  |
| rlm_quiet | close | <1k bets | 30-47 | 39.0 | -3.0 | -19.0 |  |
| rlm_quiet | close | pin $1-2k | 73-125 | 36.9 | -7.0 | -18.7 |  |
| rlm_quiet | close | pin $2k+ | 82-106 | 43.6 | 5.5 | -0.5 |  |
| rlm_quiet | close | pin limit <$1k | 46-49 | 48.4 | -0.9 | -7.0 |  |
| pin_move | close | 1-3k bets | 406-423 | 49.0 | -0.7 | -4.0 |  |
| pin_move | close | 3k+ bets | 160-180 | 47.1 | -2.7 | -9.9 |  |
| pin_move | close | <1k bets | 83-85 | 49.4 | -1.1 | -5.4 |  |
| pin_move | close | pin $1-2k | 294-320 | 47.9 | -2.3 | -6.3 |  |
| pin_move | close | pin $2k+ | 240-257 | 48.3 | -1.1 | -7.1 |  |
| pin_move | close | pin limit <$1k | 115-111 | 50.9 | 1.3 | -0.7 |  |
| money_delta | close | 1-3k bets | 249-318 | 43.9 | -0.9 | -7.6 |  |
| money_delta | close | 3k+ bets | 102-130 | 44.0 | 0.1 | -2.0 |  |
| money_delta | close | <1k bets | 51-75 | 40.5 | -2.3 | -15.6 |  |
| money_delta | close | pin $1-2k | 147-142 | 50.9 | 4.6 | 6.1 |  |
| money_delta | close | pin $2k+ | 100-138 | 42.0 | 0.6 | -11.0 |  |
| money_delta | close | pin limit <$1k | 60-72 | 45.5 | -3.8 | -9.5 |  |
| pin_rlm | close | 1-3k bets | 103-127 | 44.8 | 2.3 | 7.5 |  |
| pin_rlm | close | 3k+ bets | 39-61 | 39.0 | -2.9 | -15.5 |  |
| pin_rlm | close | <1k bets | 25-25 | 50.0 | 7.7 | 8.4 |  |
| pin_rlm | close | pin $1-2k | 75-88 | 46.0 | 1.7 | 4.3 |  |
| pin_rlm | close | pin $2k+ | 46-85 | 35.1 | -0.4 | -9.4 |  |
| pin_rlm | close | pin limit <$1k | 46-40 | 53.5 | 4.8 | 12.9 |  |
| follow_move | close | 1-3k bets | 710-677 | 51.2 | 0.4 | -6.1 |  |
| follow_move | close | 3k+ bets | 249-241 | 50.8 | -0.4 | -6.8 |  |
| follow_move | close | <1k bets | 158-151 | 51.1 | -1.1 | -12.7 |  |
| follow_move | close | pin $1-2k | 335-391 | 46.1 | -4.5 | -13.5 |  |
| follow_move | close | pin $2k+ | 300-267 | 52.9 | 1.9 | -3.1 |  |
| follow_move | close | pin limit <$1k | 138-137 | 50.2 | 0.4 | -4.1 |  |
| rlm_ratio | close | 1-3k bets | 157-215 | 42.2 | -1.6 | -9.1 |  |
| rlm_ratio | close | 3k+ bets | 60-63 | 48.8 | 5.0 | 3.9 |  |
| rlm_ratio | close | <1k bets | 35-36 | 49.3 | 5.7 | -2.1 |  |
| rlm_ratio | close | pin $1-2k | 90-98 | 47.9 | 2.0 | -0.0 |  |
| rlm_ratio | close | pin $2k+ | 46-73 | 38.7 | 1.0 | -14.0 |  |
| rlm_ratio | close | pin limit <$1k | 51-48 | 51.5 | 2.5 | -0.6 |  |
| money_level | close | 1-3k bets | 902-659 | 57.8 | 2.2 | -2.7 |  |
| money_level | close | 3k+ bets | 316-267 | 54.2 | -0.9 | -6.3 |  |
| money_level | close | <1k bets | 199-144 | 58.0 | 2.4 | -6.3 |  |
| money_level | close | pin $1-2k | 415-371 | 52.8 | -1.0 | -6.4 |  |
| money_level | close | pin $2k+ | 371-297 | 55.5 | -1.9 | -8.3 |  |
| money_level | close | pin limit <$1k | 165-150 | 52.4 | 2.1 | -0.4 |  |
| sharp_gap | close | 1-3k bets | 675-815 | 45.3 | -2.3 | -9.9 |  |
| sharp_gap | close | 3k+ bets | 266-299 | 47.1 | -0.5 | -2.5 |  |
| sharp_gap | close | <1k bets | 155-170 | 47.7 | -0.7 | -11.1 |  |
| sharp_gap | close | pin $1-2k | 358-396 | 47.5 | -1.2 | -5.9 |  |
| sharp_gap | close | pin $2k+ | 290-352 | 45.2 | -1.6 | -7.1 |  |
| sharp_gap | close | pin limit <$1k | 140-161 | 46.5 | -3.0 | -7.9 |  |
| money_moving | close | 1-3k bets | 689-808 | 46.0 | -2.1 | -9.4 |  |
| money_moving | close | 3k+ bets | 267-299 | 47.2 | -0.9 | -3.5 |  |
| money_moving | close | <1k bets | 153-168 | 47.7 | -0.5 | -9.7 |  |
| money_moving | close | pin $1-2k | 359-396 | 47.5 | -1.5 | -5.9 |  |
| money_moving | close | pin $2k+ | 294-347 | 45.9 | -1.0 | -6.3 |  |
| money_moving | close | pin limit <$1k | 139-168 | 45.3 | -4.2 | -10.3 |  |
| pin_value | close | 1-3k bets | 312-307 | 50.4 | 1.9 | 2.8 |  |
| pin_value | close | 3k+ bets | 102-123 | 45.3 | -3.6 | -11.8 |  |
| pin_value | close | <1k bets | 69-57 | 54.8 | 7.3 | 11.4 |  |
| pin_value | close | pin $1-2k | 221-247 | 47.2 | -1.4 | -4.9 |  |
| pin_value | close | pin $2k+ | 138-155 | 47.1 | 0.0 | -0.9 |  |
| pin_value | close | pin limit <$1k | 124-85 | 59.3 | 9.3 | 14.7 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.3 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.3 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 281-336 | 45.5 | -3.7 | -10.0 |  |
| consensus_gap | close | 3k+ bets | 101-117 | 46.3 | -2.5 | 0.1 |  |
| consensus_gap | close | <1k bets | 56-85 | 39.7 | -5.6 | -20.7 |  |
| consensus_gap | close | pin $1-2k | 132-144 | 47.8 | -1.9 | -1.3 |  |
| consensus_gap | close | pin $2k+ | 133-130 | 50.6 | -0.9 | 1.0 |  |
| consensus_gap | close | pin limit <$1k | 58-53 | 52.3 | 2.0 | 1.7 |  |
| consensus_gap+follow_move | close | 1-3k bets | 104-104 | 50.0 | -1.5 | -6.0 |  |
| consensus_gap+money_level | close | 1-3k bets | 184-128 | 59.0 | 0.2 | -0.9 |  |
| consensus_gap+money_moving | close | 1-3k bets | 116-182 | 38.9 | -7.4 | -13.2 |  |
| consensus_gap+pin_move | close | 1-3k bets | 68-65 | 51.1 | 0.3 | 7.4 |  |
| consensus_gap+pin_value | close | 1-3k bets | 112-124 | 47.5 | 0.7 | -1.7 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 114-186 | 38.0 | -7.7 | -14.4 |  |
| follow_move+money_level | close | 1-3k bets | 448-325 | 58.0 | 2.1 | -4.2 |  |
| follow_move+money_moving | close | 1-3k bets | 380-423 | 47.3 | -1.7 | -9.1 |  |
| follow_move+pin_move | close | 1-3k bets | 287-320 | 47.3 | -2.4 | -9.6 |  |
| follow_move+pin_value | close | 1-3k bets | 102-98 | 51.0 | 1.9 | 1.3 |  |
| follow_move+sharp_gap | close | 1-3k bets | 381-424 | 47.3 | -1.4 | -8.5 |  |
| money_level+money_moving | close | 1-3k bets | 493-442 | 52.7 | 0.2 | -4.5 |  |
| money_level+pin_move | close | 1-3k bets | 234-215 | 52.1 | -0.8 | -5.2 |  |
| money_level+pin_value | close | 1-3k bets | 146-133 | 52.3 | 2.5 | -1.9 |  |
| money_level+sharp_gap | close | 1-3k bets | 474-436 | 52.1 | -0.1 | -4.8 |  |
| money_moving+pin_move | close | 1-3k bets | 232-258 | 47.3 | -1.5 | -5.1 |  |
| money_moving+pin_value | close | 1-3k bets | 129-157 | 45.1 | -2.8 | -8.3 |  |
| money_moving+sharp_gap | close | 1-3k bets | 649-775 | 45.6 | -2.2 | -9.1 |  |
| pin_move+pin_value | close | 1-3k bets | 131-129 | 50.4 | 0.7 | -1.8 |  |
| pin_move+sharp_gap | close | 1-3k bets | 237-265 | 47.2 | -1.4 | -5.0 |  |
| pin_value+sharp_gap | close | 1-3k bets | 130-161 | 44.7 | -3.1 | -9.3 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 173-259 | 40.0 | -1.8 | -8.9 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 82-153 | 34.9 | -6.2 | -17.5 |  |
| consensus_gap+money_delta | close | 1-3k bets | 31-69 | 31.0 | -7.8 | -20.3 |  |
| follow_move+money_delta | close | 1-3k bets | 122-153 | 44.4 | -1.8 | -11.3 |  |
| money_delta+money_level | close | 1-3k bets | 88-83 | 51.5 | 3.1 | 5.8 |  |
| money_delta+money_moving | close | 1-3k bets | 178-249 | 41.7 | -1.5 | -9.3 |  |
| money_delta+pin_value | close | 1-3k bets | 54-52 | 50.9 | 3.1 | 1.1 |  |
| money_delta+sharp_gap | close | 1-3k bets | 177-246 | 41.8 | -1.3 | -8.9 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 85-104 | 45.0 | -1.9 | -5.0 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 19-30 | 38.8 | -0.5 | 15.6 |  |
| money_level+pin_rlm | close | 1-3k bets | 46-36 | 56.1 | 8.0 | 8.3 |  |
| pin_move+pin_rlm | close | 1-3k bets | 95-106 | 47.3 | 3.2 | 5.3 |  |
| pin_rlm+pin_value | close | 1-3k bets | 31-29 | 51.7 | 5.0 | 21.8 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 103-127 | 44.8 | 2.3 | 7.5 |  |
| money_delta+pin_rlm | close | 1-3k bets | 58-72 | 44.6 | 1.6 | 4.3 |  |
| money_moving+pin_rlm | close | 1-3k bets | 98-119 | 45.2 | 2.5 | 9.3 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 23-36 | 39.0 | -1.5 | 2.0 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 157-215 | 42.2 | -1.6 | -9.1 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 86-111 | 43.7 | -1.0 | -11.2 |  |
| money_level+rlm_ratio | close | 1-3k bets | 72-69 | 51.1 | 2.1 | -1.4 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 151-205 | 42.4 | -1.6 | -8.4 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 82-93 | 46.9 | 1.9 | -2.1 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 29-25 | 53.7 | 5.6 | 2.9 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 157-215 | 42.2 | -1.6 | -9.1 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 16-41 | 28.1 | -8.3 | -15.5 |  |
| follow_move+pin_rlm | close | 1-3k bets | 76-100 | 43.2 | -0.5 | -9.1 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 76-149 | 33.8 | -7.2 | -19.1 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 77-111 | 41.0 | -3.0 | -11.9 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 31-64 | 32.6 | -7.2 | -23.2 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 76-100 | 43.2 | -0.5 | -9.1 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 65-131 | 33.2 | -6.6 | -18.3 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 46-86 | 34.8 | -8.1 | -26.0 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 20-28 | 41.7 | -4.6 | 1.0 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 50.5 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 38-35 | 52.1 | 1.5 | -2.2 |  |
| consensus_gap+money_moving | close | 3k+ bets | 41-66 | 38.3 | -7.5 | 3.7 |  |
| consensus_gap+pin_move | close | 3k+ bets | 33-28 | 54.1 | 3.3 | 4.1 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 4-10 | 28.6 | -12.8 | -18.4 |  |
| consensus_gap+pin_value | close | 3k+ bets | 43-43 | 50.0 | 2.5 | 1.2 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-9 | 30.8 | -9.6 | -11.6 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 41-67 | 38.0 | -7.3 | 5.3 |  |
| follow_move+money_moving | close | 3k+ bets | 130-145 | 47.3 | -1.8 | -8.5 |  |
| follow_move+pin_move | close | 3k+ bets | 121-132 | 47.8 | -2.0 | -8.0 |  |
| follow_move+pin_rlm | close | 3k+ bets | 36-44 | 45.0 | 1.8 | -1.4 |  |
| follow_move+pin_value | close | 3k+ bets | 41-48 | 46.1 | -3.9 | -13.4 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 60-63 | 48.8 | 5.0 | 3.9 |  |
| follow_move+sharp_gap | close | 3k+ bets | 130-143 | 47.6 | -0.9 | -6.1 |  |
| money_moving+pin_move | close | 3k+ bets | 85-114 | 42.7 | -5.6 | -16.4 |  |
| money_moving+pin_rlm | close | 3k+ bets | 38-59 | 39.2 | -2.6 | -14.9 |  |
| money_moving+pin_value | close | 3k+ bets | 50-69 | 42.0 | -6.2 | -15.3 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 57-61 | 48.3 | 4.5 | 2.7 |  |
| money_moving+sharp_gap | close | 3k+ bets | 257-287 | 47.2 | -0.5 | -2.4 |  |
| pin_move+pin_rlm | close | 3k+ bets | 36-54 | 40.0 | -3.4 | -13.6 |  |
| pin_move+pin_value | close | 3k+ bets | 46-60 | 43.4 | -6.1 | -18.2 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 38-46 | 45.2 | 0.6 | -2.9 |  |
| pin_move+sharp_gap | close | 3k+ bets | 83-114 | 42.1 | -5.7 | -16.2 |  |
| pin_rlm+pin_value | close | 3k+ bets | 7-18 | 28.0 | -19.2 | -46.7 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 36-44 | 45.0 | 1.8 | -1.4 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 39-61 | 39.0 | -2.9 | -15.5 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 9-12 | 42.9 | -7.3 | -18.6 |  |
| pin_value+sharp_gap | close | 3k+ bets | 50-69 | 42.0 | -6.4 | -15.3 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 60-63 | 48.8 | 5.0 | 3.9 |  |
| follow_move+money_delta | close | 3k+ bets | 46-60 | 43.4 | -1.7 | -10.4 |  |
| money_level+money_moving | close | 3k+ bets | 177-168 | 51.3 | -1.1 | -5.4 |  |
| money_level+sharp_gap | close | 3k+ bets | 173-165 | 51.2 | -0.9 | -4.5 |  |
| follow_move+money_level | close | 3k+ bets | 145-117 | 55.3 | -0.9 | -7.1 |  |
| money_level+rlm_ratio | close | 3k+ bets | 26-15 | 63.4 | 15.8 | 29.5 |  |
| consensus_gap+money_level | close | 3k+ bets | 59-57 | 50.9 | -6.2 | -13.9 |  |
| money_level+pin_move | close | 3k+ bets | 82-85 | 49.1 | -5.0 | -11.5 |  |
| money_level+pin_value | close | 3k+ bets | 57-65 | 46.7 | -3.9 | -13.2 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 8-16 | 33.3 | -5.1 | -17.2 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 67-93 | 41.9 | -0.4 | -10.4 |  |
| money_delta+money_moving | close | 3k+ bets | 74-101 | 42.3 | -0.3 | -1.0 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 27-40 | 40.3 | -0.3 | -9.2 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 34-50 | 40.5 | -1.4 | -11.6 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 31-50 | 38.3 | -3.8 | -16.5 |  |
| consensus_gap+money_delta | close | 3k+ bets | 14-25 | 35.9 | -4.1 | 16.0 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 16-32 | 33.3 | -9.0 | -28.4 |  |
| money_delta+sharp_gap | close | 3k+ bets | 72-98 | 42.4 | -0.1 | -0.5 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 38-53 | 41.8 | -1.5 | -10.4 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 15-29 | 34.1 | -6.7 | -21.5 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 9-18 | 33.3 | -15.9 | -36.5 |  |
| money_delta+money_level | close | 3k+ bets | 35-28 | 55.6 | 8.8 | 12.0 |  |
| money_level+pin_rlm | close | 3k+ bets | 16-11 | 59.3 | 13.6 | 26.8 |  |
| money_delta+pin_value | close | 3k+ bets | 21-22 | 48.8 | 1.8 | -7.8 |  |
| money_delta+pin_move | close | 3k+ bets | 40-53 | 43.0 | -2.4 | -12.5 |  |
| money_delta+pin_rlm | close | 3k+ bets | 25-34 | 42.4 | 0.5 | -9.8 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 33-32 | 50.8 | 7.1 | 7.8 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 47.3 | 87.7 |  |
| money_level+money_moving | close | <1k bets | 107-92 | 53.8 | 1.1 | -8.3 |  |
| money_level+sharp_gap | close | <1k bets | 110-93 | 54.2 | 1.1 | -8.4 |  |
| money_moving+sharp_gap | close | <1k bets | 149-165 | 47.5 | -0.6 | -10.5 |  |
| consensus_gap+money_level | close | <1k bets | 30-28 | 51.7 | -5.0 | -20.3 |  |
| consensus_gap+money_moving | close | <1k bets | 25-40 | 38.5 | -5.5 | -17.8 |  |
| consensus_gap+pin_move | close | <1k bets | 8-13 | 38.1 | -12.6 | -17.2 |  |
| consensus_gap+pin_value | close | <1k bets | 18-15 | 54.5 | 11.8 | 31.8 |  |
| consensus_gap+sharp_gap | close | <1k bets | 26-42 | 38.2 | -5.7 | -19.4 |  |
| money_level+pin_move | close | <1k bets | 45-42 | 51.7 | -1.8 | -7.8 |  |
| money_level+pin_value | close | <1k bets | 25-21 | 54.3 | 4.3 | 1.5 |  |
| money_moving+pin_move | close | <1k bets | 44-48 | 47.8 | -0.2 | -3.4 |  |
| money_moving+pin_value | close | <1k bets | 22-20 | 52.4 | 6.7 | 21.4 |  |
| pin_move+pin_value | close | <1k bets | 31-24 | 56.4 | 7.8 | 13.1 |  |
| pin_move+sharp_gap | close | <1k bets | 44-49 | 47.3 | -1.2 | -7.9 |  |
| pin_value+sharp_gap | close | <1k bets | 22-19 | 53.7 | 7.6 | 24.4 |  |
| follow_move+money_delta | close | <1k bets | 25-29 | 46.3 | 2.8 | -7.2 |  |
| follow_move+money_moving | close | <1k bets | 73-79 | 48.0 | -1.6 | -12.2 |  |
| follow_move+pin_move | close | <1k bets | 53-56 | 48.6 | -2.4 | -9.5 |  |
| follow_move+sharp_gap | close | <1k bets | 74-80 | 48.1 | -2.2 | -14.6 |  |
| money_delta+money_moving | close | <1k bets | 36-57 | 38.7 | -2.0 | -16.4 |  |
| money_delta+pin_move | close | <1k bets | 14-20 | 41.2 | -3.5 | -19.8 |  |
| money_delta+sharp_gap | close | <1k bets | 36-57 | 38.7 | -2.0 | -16.4 |  |
| follow_move+rlm_quiet | close | <1k bets | 30-47 | 39.0 | -3.0 | -19.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 35-36 | 49.3 | 5.7 | -2.1 |  |
| money_delta+rlm_quiet | close | <1k bets | 12-14 | 46.2 | 5.5 | -4.0 |  |
| money_delta+rlm_ratio | close | <1k bets | 21-22 | 48.8 | 6.4 | -1.2 |  |
| money_moving+rlm_quiet | close | <1k bets | 18-19 | 48.6 | 6.7 | 5.1 |  |
| money_moving+rlm_ratio | close | <1k bets | 35-36 | 49.3 | 5.7 | -2.1 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 14-16 | 46.7 | 5.6 | -4.1 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 17-20 | 45.9 | 3.4 | -6.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 35-36 | 49.3 | 5.7 | -2.1 |  |
| follow_move+money_level | close | <1k bets | 95-70 | 57.6 | 0.0 | -11.1 |  |
| consensus_gap+money_delta | close | <1k bets | 7-22 | 24.1 | -10.6 | -35.0 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -2.6 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 13-17 | 43.3 | 3.2 | -7.1 |  |
| money_moving+pin_rlm | close | <1k bets | 25-25 | 50.0 | 7.7 | 8.4 |  |
| pin_rlm+sharp_gap | close | <1k bets | 25-25 | 50.0 | 7.7 | 8.4 |  |
| money_delta+pin_value | close | <1k bets | 9-8 | 52.9 | 7.3 | 21.5 |  |
| consensus_gap+follow_move | close | <1k bets | 14-21 | 40.0 | -11.2 | -35.2 |  |
| follow_move+pin_rlm | close | <1k bets | 20-15 | 57.1 | 12.5 | 12.2 |  |
| follow_move+pin_value | close | <1k bets | 22-15 | 59.5 | 10.5 | 13.0 |  |
| pin_move+pin_rlm | close | <1k bets | 23-20 | 53.5 | 8.9 | 11.3 |  |
| pin_move+rlm_quiet | close | <1k bets | 13-14 | 48.1 | 2.4 | 2.3 |  |
| pin_move+rlm_ratio | close | <1k bets | 20-17 | 54.1 | 8.0 | 5.1 |  |
| pin_rlm+pin_value | close | <1k bets | 6-3 | 66.7 | 24.5 | 64.1 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 9-6 | 60.0 | 16.0 | 17.9 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 20-15 | 57.1 | 12.5 | 12.2 |  |
| pin_value+rlm_quiet | close | <1k bets | 5-4 | 55.6 | 6.3 | 6.5 |  |
| pin_value+rlm_ratio | close | <1k bets | 5-1 | 83.3 | 34.6 | 58.3 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 3-7 | 30.0 | -6.6 | -42.5 |  |
| money_delta+money_level | close | <1k bets | 15-20 | 42.9 | -0.4 | -14.3 |  |
| money_level+rlm_ratio | close | <1k bets | 17-16 | 51.5 | 6.1 | 0.2 |  |
| money_level+pin_rlm | close | <1k bets | 11-8 | 57.9 | 13.8 | 14.1 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-6 | 14.3 | -22.8 | -72.7 |  |
| consensus_gap+follow_move | close | pin $1-2k | 48-57 | 45.7 | -6.3 | -13.3 |  |
| consensus_gap+money_moving | close | pin $1-2k | 59-76 | 43.7 | -4.8 | -6.2 |  |
| consensus_gap+pin_move | close | pin $1-2k | 49-53 | 48.0 | -3.6 | 2.0 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-19 | 40.6 | -1.2 | 21.9 |  |
| consensus_gap+pin_value | close | pin $1-2k | 78-83 | 48.4 | 1.8 | -1.6 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-16 | 46.7 | 1.1 | 1.7 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 57-74 | 43.5 | -4.1 | -5.2 |  |
| follow_move+money_moving | close | pin $1-2k | 193-237 | 44.9 | -4.7 | -12.5 |  |
| follow_move+pin_move | close | pin $1-2k | 203-249 | 44.9 | -5.3 | -13.6 |  |
| follow_move+pin_rlm | close | pin $1-2k | 62-70 | 47.0 | 1.1 | -1.0 |  |
| follow_move+pin_value | close | pin $1-2k | 75-92 | 44.9 | -4.8 | -15.4 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 90-98 | 47.9 | 2.0 | -0.0 |  |
| follow_move+sharp_gap | close | pin $1-2k | 197-238 | 45.3 | -4.2 | -12.0 |  |
| money_moving+pin_move | close | pin $1-2k | 175-204 | 46.2 | -3.3 | -7.1 |  |
| money_moving+pin_rlm | close | pin $1-2k | 72-81 | 47.1 | 2.2 | 7.1 |  |
| money_moving+pin_value | close | pin $1-2k | 84-120 | 41.2 | -6.9 | -18.4 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 88-91 | 49.2 | 2.8 | 2.5 |  |
| money_moving+sharp_gap | close | pin $1-2k | 343-379 | 47.5 | -1.3 | -5.5 |  |
| pin_move+pin_rlm | close | pin $1-2k | 72-80 | 47.4 | 1.9 | 5.3 |  |
| pin_move+pin_value | close | pin $1-2k | 91-116 | 44.0 | -5.9 | -15.6 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 70-73 | 49.0 | 2.1 | 1.7 |  |
| pin_move+sharp_gap | close | pin $1-2k | 177-209 | 45.9 | -3.1 | -7.9 |  |
| pin_rlm+pin_value | close | pin $1-2k | 18-30 | 37.5 | -11.0 | -22.9 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 62-70 | 47.0 | 1.1 | -1.0 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 75-88 | 46.0 | 1.7 | 4.3 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 20-25 | 44.4 | -5.1 | -16.1 |  |
| pin_value+sharp_gap | close | pin $1-2k | 84-117 | 41.8 | -6.2 | -17.2 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 90-98 | 47.9 | 2.0 | -0.0 |  |
| follow_move+money_level | close | pin $1-2k | 214-213 | 50.1 | -3.9 | -12.1 |  |
| money_level+rlm_ratio | close | pin $1-2k | 48-40 | 54.5 | 6.5 | 6.2 |  |
| money_level+sharp_gap | close | pin $1-2k | 252-250 | 50.2 | -1.4 | -7.3 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 4-15 | 21.1 | -20.1 | -39.5 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 73-125 | 36.9 | -7.0 | -18.7 |  |
| money_level+money_moving | close | pin $1-2k | 256-253 | 50.3 | -1.6 | -7.5 |  |
| consensus_gap+money_level | close | pin $1-2k | 76-70 | 52.1 | -4.4 | -8.8 |  |
| money_level+pin_value | close | pin $1-2k | 96-104 | 48.0 | -2.0 | -10.3 |  |
| money_level+pin_move | close | pin $1-2k | 168-173 | 49.3 | -3.4 | -10.4 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 36-57 | 38.7 | -5.5 | -9.2 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 51-76 | 40.2 | -5.6 | -10.9 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 23-42 | 35.4 | -9.0 | -16.5 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 30-50 | 37.5 | -6.0 | -11.3 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 37-60 | 38.1 | -5.8 | -12.4 |  |
| money_level+pin_rlm | close | pin $1-2k | 34-28 | 54.8 | 8.1 | 7.5 |  |
| follow_move+money_delta | close | pin $1-2k | 71-78 | 47.7 | 0.9 | -3.0 |  |
| money_delta+money_moving | close | pin $1-2k | 97-108 | 47.3 | 2.6 | 2.7 |  |
| money_delta+pin_move | close | pin $1-2k | 69-78 | 46.9 | -0.6 | -1.6 |  |
| money_delta+pin_rlm | close | pin $1-2k | 44-51 | 46.3 | 2.0 | 4.6 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 52-51 | 50.5 | 4.6 | 4.9 |  |
| money_delta+sharp_gap | close | pin $1-2k | 97-106 | 47.8 | 3.0 | 3.7 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 47.3 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 50-45 | 52.6 | 4.3 | 2.4 |  |
| consensus_gap+money_delta | close | pin $1-2k | 19-26 | 42.2 | 0.3 | 4.5 |  |
| money_delta+pin_value | close | pin $1-2k | 44-47 | 48.4 | 0.0 | -4.5 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 22-39 | 36.1 | -8.4 | -19.6 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 13-32 | 28.9 | -20.3 | -44.5 |  |
| consensus_gap+follow_move | close | pin $2k+ | 41-35 | 53.9 | 0.9 | -8.5 |  |
| consensus_gap+money_delta | close | pin $2k+ | 10-28 | 26.3 | -9.2 | -48.9 |  |
| consensus_gap+money_level | close | pin $2k+ | 88-64 | 57.9 | -4.4 | -10.1 |  |
| consensus_gap+money_moving | close | pin $2k+ | 47-78 | 37.6 | -8.6 | -7.7 |  |
| consensus_gap+pin_move | close | pin $2k+ | 43-40 | 51.8 | 1.2 | 0.2 |  |
| consensus_gap+pin_value | close | pin $2k+ | 52-59 | 46.8 | 2.9 | 7.0 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 2-15 | 11.8 | -20.8 | -69.1 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 48-82 | 36.9 | -9.6 | -8.2 |  |
| follow_move+money_delta | close | pin $2k+ | 38-53 | 41.8 | 0.5 | -13.4 |  |
| follow_move+money_level | close | pin $2k+ | 171-116 | 59.6 | 0.4 | -4.4 |  |
| follow_move+money_moving | close | pin $2k+ | 137-148 | 48.1 | 0.2 | -8.3 |  |
| follow_move+pin_move | close | pin $2k+ | 181-181 | 50.0 | 0.4 | -5.6 |  |
| follow_move+pin_value | close | pin $2k+ | 43-41 | 51.2 | 3.3 | 8.3 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 46-73 | 38.7 | 1.0 | -14.0 |  |
| follow_move+sharp_gap | close | pin $2k+ | 135-148 | 47.7 | -0.0 | -8.5 |  |
| money_delta+money_level | close | pin $2k+ | 29-24 | 54.7 | 10.1 | 11.3 |  |
| money_delta+money_moving | close | pin $2k+ | 70-106 | 39.8 | 0.8 | -12.5 |  |
| money_delta+pin_move | close | pin $2k+ | 38-59 | 39.2 | -3.0 | -19.9 |  |
| money_delta+pin_value | close | pin $2k+ | 22-25 | 46.8 | 2.1 | -10.7 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 24-38 | 38.7 | 0.9 | -16.3 |  |
| money_delta+sharp_gap | close | pin $2k+ | 68-105 | 39.3 | 0.3 | -13.4 |  |
| money_level+money_moving | close | pin $2k+ | 197-189 | 51.0 | -2.1 | -7.6 |  |
| money_level+pin_move | close | pin $2k+ | 125-110 | 53.2 | -2.8 | -7.1 |  |
| money_level+pin_value | close | pin $2k+ | 68-72 | 48.6 | -1.5 | -10.1 |  |
| money_level+rlm_ratio | close | pin $2k+ | 17-15 | 53.1 | 7.0 | 10.3 |  |
| money_level+sharp_gap | close | pin $2k+ | 195-192 | 50.4 | -2.7 | -8.2 |  |
| money_moving+pin_move | close | pin $2k+ | 115-139 | 45.3 | -1.6 | -10.2 |  |
| money_moving+pin_value | close | pin $2k+ | 69-87 | 44.2 | -2.0 | -2.6 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 46-72 | 39.0 | 1.3 | -13.3 |  |
| money_moving+sharp_gap | close | pin $2k+ | 285-342 | 45.5 | -1.3 | -6.4 |  |
| pin_move+pin_value | close | pin $2k+ | 63-63 | 50.0 | 1.4 | -2.8 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 33-51 | 39.3 | 0.7 | -10.6 |  |
| pin_move+sharp_gap | close | pin $2k+ | 114-141 | 44.7 | -2.2 | -10.7 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 5-7 | 41.7 | -1.7 | -17.1 |  |
| pin_value+sharp_gap | close | pin $2k+ | 69-90 | 43.4 | -3.1 | -4.5 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 46-73 | 38.7 | 1.0 | -14.0 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 6-24 | 20.0 | -12.9 | -24.8 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 6-16 | 27.3 | -3.0 | -37.1 |  |
| follow_move+pin_rlm | close | pin $2k+ | 33-57 | 36.7 | 0.4 | -15.4 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 82-106 | 43.6 | 5.5 | -0.5 |  |
| money_moving+pin_rlm | close | pin $2k+ | 46-84 | 35.4 | -0.2 | -8.7 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 34-56 | 37.8 | 2.3 | -14.3 |  |
| pin_move+pin_rlm | close | pin $2k+ | 37-60 | 38.1 | 0.9 | -10.8 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 52-74 | 41.3 | 1.4 | -10.0 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 17-42 | 28.8 | -3.4 | -28.8 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 33-57 | 36.7 | 0.4 | -15.4 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 46-85 | 35.1 | -0.4 | -9.4 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 24-49 | 32.9 | 0.3 | -22.0 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 33-56 | 37.1 | 1.6 | -16.2 |  |
| money_delta+pin_rlm | close | pin $2k+ | 26-48 | 35.1 | -0.5 | -15.0 |  |
| money_level+pin_rlm | close | pin $2k+ | 16-11 | 59.3 | 15.4 | 25.6 |  |
| pin_rlm+pin_value | close | pin $2k+ | 7-14 | 33.3 | -5.1 | 11.7 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 21-32 | 39.6 | 1.8 | -17.5 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 7-10 | 41.2 | 1.1 | 37.9 |  |
| follow_move+money_delta | close | pin limit <$1k | 35-48 | 42.2 | -7.0 | -19.0 |  |
| money_level+money_moving | close | pin limit <$1k | 90-100 | 47.4 | -2.4 | -9.3 |  |
| money_level+sharp_gap | close | pin limit <$1k | 86-94 | 47.8 | -2.0 | -8.4 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 129-151 | 46.1 | -3.4 | -8.5 |  |
| consensus_gap+money_level | close | pin limit <$1k | 32-30 | 51.6 | 0.8 | -4.4 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 17-13 | 56.7 | 8.1 | 21.5 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 43-40 | 51.8 | 2.0 | 2.9 |  |
| follow_move+money_moving | close | pin limit <$1k | 82-99 | 45.3 | -4.1 | -13.0 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 86-97 | 47.0 | -2.4 | -9.8 |  |
| money_level+pin_move | close | pin limit <$1k | 68-59 | 53.5 | 3.6 | 2.2 |  |
| money_level+pin_value | close | pin limit <$1k | 64-43 | 59.8 | 9.6 | 13.3 |  |
| pin_move+pin_value | close | pin limit <$1k | 54-34 | 61.4 | 11.5 | 21.7 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 22-14 | 61.1 | 11.5 | 13.1 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 26-25 | 51.0 | 1.9 | 5.2 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 28-26 | 51.9 | 2.6 | 6.3 |  |
| follow_move+money_level | close | pin limit <$1k | 74-71 | 51.0 | 0.9 | -2.8 |  |
| follow_move+pin_move | close | pin limit <$1k | 77-78 | 49.7 | 0.2 | -4.8 |  |
| follow_move+pin_value | close | pin limit <$1k | 47-28 | 62.7 | 12.8 | 19.0 |  |
| money_moving+pin_move | close | pin limit <$1k | 71-77 | 48.0 | -1.4 | -5.3 |  |
| money_moving+pin_value | close | pin limit <$1k | 48-39 | 55.2 | 5.4 | 9.9 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 73-78 | 48.3 | -1.0 | -4.6 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 49-42 | 53.8 | 4.0 | 7.2 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 46-49 | 48.4 | -0.9 | -7.0 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 27-34 | 44.3 | -4.7 | -15.1 |  |
| money_delta+money_moving | close | pin limit <$1k | 51-58 | 46.8 | -2.3 | -6.2 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 10-8 | 55.6 | 8.2 | 30.0 |  |
| money_delta+money_level | close | pin limit <$1k | 26-25 | 51.0 | 1.4 | -2.3 |  |
| money_delta+pin_value | close | pin limit <$1k | 18-10 | 64.3 | 15.2 | 38.0 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 50-56 | 47.2 | -1.9 | -5.5 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 32-40 | 44.4 | -4.4 | -8.6 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 7-4 | 63.6 | 17.5 | 61.2 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 26-24 | 52.0 | 3.6 | 8.7 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 43-38 | 53.1 | 4.5 | 12.8 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 45-40 | 52.9 | 4.0 | 6.7 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-6 | 76.0 | 27.0 | 62.7 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 46-40 | 53.5 | 4.8 | 12.9 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 7-3 | 70.0 | 22.4 | 33.8 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 14-8 | 63.6 | 13.9 | 21.7 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 11-21 | 34.4 | -14.0 | -34.0 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 25-28 | 47.2 | -1.8 | -9.3 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 37-32 | 53.6 | 4.6 | 3.2 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 51-48 | 51.5 | 2.5 | -0.6 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 29-31 | 48.3 | -0.6 | -7.0 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 21-34 | 38.2 | -10.7 | -26.6 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 47-46 | 50.5 | 1.6 | -2.4 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 37-32 | 53.6 | 4.6 | 3.2 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 15-15 | 50.0 | 1.7 | -3.8 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 37-32 | 53.6 | 4.6 | 3.2 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 23-26 | 46.9 | -1.9 | -9.9 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 51-48 | 51.5 | 2.5 | -0.6 |  |
| money_level+pin_rlm | close | pin limit <$1k | 23-16 | 59.0 | 9.4 | 13.2 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 25-19 | 56.8 | 7.7 | 10.3 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 18-6 | 75.0 | 25.2 | 43.5 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 7-5 | 58.3 | 10.2 | 11.5 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 50.5 | 87.7 |  |
| rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.5 | 7.9 | -0.02 |
| rlm_quiet | early | 3k+ bets | 0-2 | 0.0 | -51.6 | -100.0 | -0.5 |
| rlm_quiet | early | <1k bets | 46-54 | 46.0 | 9.9 | 13.8 | 0.58 |
| rlm_quiet | early | pin $1-2k | 3-7 | 30.0 | -0.7 | 7.2 | -0.12 |
| rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.3 | -100.0 | 1.3 |
| rlm_quiet | early | pin limit <$1k | 6-8 | 42.9 | -2.2 | -13.5 | 0.23 |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.5 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 11-19 | 36.7 | -11.6 | -31.9 | 0.24 |
| pin_move | early | pin $1-2k | 1-5 | 16.7 | -25.2 | -67.6 | -0.05 |
| pin_move | early | pin limit <$1k | 10-15 | 40.0 | -9.9 | -26.0 | 0.26 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 12-10 | 54.5 | 15.6 | 28.2 | 0.83 |
| money_delta | early | pin $1-2k | 0-3 | 0.0 | -36.4 | -100.0 | 2.17 |
| money_delta | early | pin limit <$1k | 5-0 | 100.0 | 50.8 | 88.6 | 0.0 |
| pin_rlm | early | <1k bets | 1-4 | 20.0 | -17.0 | -61.5 | -0.3 |
| pin_rlm | early | pin $1-2k | 0-3 | 0.0 | -42.8 | -100.0 | -0.67 |
| pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 21.7 | -3.7 | 0.25 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.5 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -51.6 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 549-507 | 52.0 | 0.9 | -7.4 | 0.13 |
| follow_move | early | pin $1-2k | 40-29 | 58.0 | 7.3 | 7.3 | -0.33 |
| follow_move | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
| follow_move | early | pin limit <$1k | 58-59 | 49.6 | -0.5 | -6.8 | -0.13 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.1 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.7 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 30-28 | 51.7 | 13.2 | 17.2 | 0.53 |
| rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.3 | 29.7 | -1.02 |
| rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
| rlm_ratio | early | pin limit <$1k | 8-2 | 80.0 | 36.7 | 61.1 | 0.33 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 1.5 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 43.8 | 59.7 | 0.33 |
| money_level | early | <1k bets | 201-140 | 58.9 | 0.0 | -6.8 | -0.26 |
| money_level | early | pin $1-2k | 24-13 | 64.9 | 1.1 | -2.9 | -0.05 |
| money_level | early | pin $2k+ | 1-1 | 50.0 | -12.2 | -47.2 | -0.7 |
| money_level | early | pin limit <$1k | 31-32 | 49.2 | -2.9 | -8.4 | 0.26 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.3 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 8.7 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 160-154 | 51.0 | 2.1 | -1.7 | 0.3 |
| sharp_gap | early | pin $1-2k | 18-17 | 51.4 | -3.9 | -6.9 | -0.3 |
| sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
| sharp_gap | early | pin limit <$1k | 35-23 | 60.3 | 11.8 | 23.4 | 0.18 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.6 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 51.6 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 119-106 | 52.9 | 2.1 | -5.0 | 0.23 |
| money_moving | early | pin $1-2k | 8-13 | 38.1 | -19.0 | -47.8 | 0.36 |
| money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.2 | -8.4 | 0.65 |
| money_moving | early | pin limit <$1k | 32-11 | 74.4 | 24.7 | 52.7 | 0.41 |
| pin_value | early | 1-3k bets | 13-10 | 56.5 | 8.3 | 6.3 | -0.04 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.7 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 57-57 | 50.0 | 1.0 | -5.4 | 0.1 |
| pin_value | early | pin $1-2k | 19-28 | 40.4 | -6.9 | -24.0 | 0.16 |
| pin_value | early | pin $2k+ | 1-0 | 100.0 | 52.7 | 83.3 | 0.0 |
| pin_value | early | pin limit <$1k | 51-39 | 56.7 | 7.0 | 7.3 | 0.04 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -50.5 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -26.9 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.2 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 12.2 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 272-308 | 46.9 | -2.4 | -10.3 | 0.45 |
| consensus_gap | early | pin $1-2k | 22-25 | 46.8 | -0.5 | -11.9 | 0.29 |
| consensus_gap | early | pin $2k+ | 1-1 | 50.0 | 12.2 | -8.4 | 0.65 |
| consensus_gap | early | pin limit <$1k | 26-38 | 40.6 | -9.5 | -17.9 | 0.24 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -52.7 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.5 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -1.6 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 17.7 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 5.4 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.3 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 7-4 | 63.6 | 14.3 | 19.4 | -0.09 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.2 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.8 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -50.5 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -0.9 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 6-5 | 54.5 | 8.2 | 1.3 | 0.27 |
| consensus_gap+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -1.3 | -38.9 | 0.77 |
| follow_move+pin_value | early | 1-3k bets | 7-7 | 50.0 | 2.8 | -6.4 | -0.29 |
| follow_move+rlm_quiet | early | 1-3k bets | 3-6 | 33.3 | -4.5 | 7.9 | -0.02 |
| pin_value+rlm_quiet | early | 1-3k bets | 1-2 | 33.3 | -8.7 | -38.9 | -0.67 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -20.2 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -3.0 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 3.4 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.5 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.1 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.6 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.1 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.2 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.1 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.3 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.1 | 85.1 | 0.0 |
| money_delta+rlm_quiet | early | 1-3k bets | 1-0 | 100.0 | 52.7 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | 1-3k bets | 2-2 | 50.0 | 11.4 | -2.2 | -0.3 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 18.2 | 18.8 | -0.24 |
| rlm_quiet+rlm_ratio | early | 1-3k bets | 2-2 | 50.0 | 16.1 | 97.0 | -0.3 |
| rlm_quiet+sharp_gap | early | 1-3k bets | 2-2 | 50.0 | 16.1 | 97.0 | -0.3 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -28.3 | -100.0 | 1.3 |
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
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 39.4 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 50.5 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 40-46 | 46.5 | -6.8 | -16.9 | 0.87 |
| consensus_gap+money_level | early | <1k bets | 47-36 | 56.6 | -7.2 | -12.3 | -0.05 |
| consensus_gap+sharp_gap | early | <1k bets | 34-50 | 40.5 | -9.1 | -18.5 | 0.55 |
| follow_move+money_level | early | <1k bets | 99-50 | 66.4 | 6.4 | -1.4 | 0.0 |
| follow_move+sharp_gap | early | <1k bets | 82-50 | 62.1 | 12.4 | 12.3 | 0.5 |
| money_level+sharp_gap | early | <1k bets | 110-80 | 57.9 | 1.9 | -4.5 | 0.02 |
| follow_move+money_moving | early | <1k bets | 59-39 | 60.2 | 8.2 | 8.8 | 0.4 |
| money_level+money_moving | early | <1k bets | 67-48 | 58.3 | 0.3 | -6.1 | -0.06 |
| money_moving+sharp_gap | early | <1k bets | 68-64 | 51.5 | 3.1 | -2.7 | 0.43 |
| consensus_gap+money_moving | early | <1k bets | 20-23 | 46.5 | -4.9 | -25.3 | 0.63 |
| follow_move+pin_value | early | <1k bets | 17-15 | 53.1 | 3.5 | -0.2 | -0.17 |
| follow_move+rlm_quiet | early | <1k bets | 46-54 | 46.0 | 9.9 | 13.8 | 0.58 |
| money_moving+rlm_quiet | early | <1k bets | 17-16 | 51.5 | 14.3 | 26.9 | 0.62 |
| rlm_quiet+sharp_gap | early | <1k bets | 22-20 | 52.4 | 15.6 | 22.2 | 0.1 |
| follow_move+rlm_ratio | early | <1k bets | 30-28 | 51.7 | 13.2 | 17.2 | 0.53 |
| rlm_quiet+rlm_ratio | early | <1k bets | 20-16 | 55.6 | 19.1 | 32.0 | 0.14 |
| rlm_ratio+sharp_gap | early | <1k bets | 30-28 | 51.7 | 13.2 | 17.2 | 0.53 |
| pin_move+pin_value | early | <1k bets | 4-10 | 28.6 | -20.8 | -45.1 | 0.36 |
| follow_move+pin_move | early | <1k bets | 7-9 | 43.8 | -5.3 | -20.3 | 0.28 |
| consensus_gap+pin_value | early | <1k bets | 23-26 | 46.9 | -0.6 | -11.8 | 0.25 |
| pin_value+rlm_quiet | early | <1k bets | 0-3 | 0.0 | -43.5 | -100.0 | -0.6 |
| money_delta+money_moving | early | <1k bets | 11-10 | 52.4 | 14.0 | 25.2 | 0.87 |
| money_delta+sharp_gap | early | <1k bets | 10-8 | 55.6 | 17.8 | 35.5 | 1.01 |
| consensus_gap+pin_move | early | <1k bets | 2-6 | 25.0 | -22.0 | -51.7 | 0.29 |
| money_level+pin_move | early | <1k bets | 4-6 | 40.0 | -10.0 | -30.2 | 0.14 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -28.3 | -100.0 | -4.8 |
| consensus_gap+rlm_quiet | early | <1k bets | 4-5 | 44.4 | 6.8 | -2.4 | 0.93 |
| consensus_gap+rlm_ratio | early | <1k bets | 5-3 | 62.5 | 21.0 | 25.0 | 0.65 |
| follow_move+pin_rlm | early | <1k bets | 1-3 | 25.0 | -14.1 | -51.8 | -0.7 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -28.3 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | <1k bets | 0-1 | 0.0 | -28.3 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-3 | 25.0 | -14.1 | -51.8 | -0.7 |
| pin_rlm+sharp_gap | early | <1k bets | 1-4 | 20.0 | -17.0 | -61.5 | -0.3 |
| pin_value+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 24.3 | 27.3 | -0.93 |
| pin_value+sharp_gap | early | <1k bets | 6-8 | 42.9 | -7.2 | -18.2 | 0.42 |
| money_level+pin_value | early | <1k bets | 7-7 | 50.0 | -1.7 | -4.5 | 0.84 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -51.1 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -49.5 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 4-4 | 50.0 | -3.2 | -4.0 | 1.21 |
| money_level+rlm_ratio | early | <1k bets | 8-12 | 40.0 | -1.3 | -17.1 | 1.32 |
| money_moving+rlm_ratio | early | <1k bets | 16-10 | 61.5 | 21.0 | 45.3 | 0.82 |
| consensus_gap+money_delta | early | <1k bets | 2-0 | 100.0 | 50.0 | 90.9 | 0.5 |
| money_delta+money_level | early | <1k bets | 4-4 | 50.0 | 8.3 | 4.6 | 1.44 |
| pin_move+sharp_gap | early | <1k bets | 2-4 | 33.3 | -13.3 | -47.8 | 0.47 |
| money_level+pin_rlm | early | <1k bets | 1-2 | 33.3 | -9.4 | -35.8 | 0.67 |
| pin_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 21.7 | -3.7 | 0.25 |
| pin_move+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 21.7 | -3.7 | 0.25 |
| follow_move+money_delta | early | <1k bets | 6-4 | 60.0 | 21.1 | 68.1 | 0.98 |
| money_delta+rlm_quiet | early | <1k bets | 3-2 | 60.0 | 27.5 | 107.0 | -0.4 |
| money_delta+rlm_ratio | early | <1k bets | 5-2 | 71.4 | 34.1 | 112.8 | 1.71 |
| money_delta+pin_value | early | <1k bets | 2-0 | 100.0 | 50.5 | 90.9 | 0.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -28.3 | -100.0 | 1.3 |
| money_moving+pin_move | early | <1k bets | 1-1 | 50.0 | 0.5 | -2.4 | 1.0 |
| consensus_gap+money_level | early | pin $1-2k | 7-5 | 58.3 | -7.3 | -9.8 | 0.07 |
| consensus_gap+money_moving | early | pin $1-2k | 1-3 | 25.0 | -40.6 | -54.2 | 0.95 |
| consensus_gap+pin_value | early | pin $1-2k | 8-11 | 42.1 | -1.1 | -22.3 | 0.14 |
| follow_move+rlm_quiet | early | pin $1-2k | 3-7 | 30.0 | -0.7 | 7.2 | -0.12 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-4 | 33.3 | -10.3 | 29.7 | -1.02 |
| follow_move+sharp_gap | early | pin $1-2k | 9-6 | 60.0 | 2.8 | 19.2 | -0.62 |
| money_level+money_moving | early | pin $1-2k | 8-8 | 50.0 | -13.2 | -31.4 | 0.26 |
| money_level+pin_value | early | pin $1-2k | 2-4 | 33.3 | -18.9 | -37.6 | 0.78 |
| money_moving+pin_value | early | pin $1-2k | 1-4 | 20.0 | -34.8 | -63.3 | 0.94 |
| rlm_quiet+rlm_ratio | early | pin $1-2k | 1-3 | 25.0 | -9.4 | 45.0 | -1.9 |
| rlm_quiet+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -9.4 | 45.0 | -1.9 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -10.3 | 29.7 | -1.02 |
| money_delta+money_level | early | pin $1-2k | 0-2 | 0.0 | -40.5 | -100.0 | 1.25 |
| money_delta+money_moving | early | pin $1-2k | 0-3 | 0.0 | -36.4 | -100.0 | 2.17 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -52.7 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-3 | 0.0 | -36.4 | -100.0 | 2.17 |
| money_level+sharp_gap | early | pin $1-2k | 15-9 | 62.5 | -1.1 | -4.8 | -0.23 |
| money_moving+sharp_gap | early | pin $1-2k | 4-10 | 28.6 | -27.6 | -61.0 | 0.36 |
| pin_value+sharp_gap | early | pin $1-2k | 1-4 | 20.0 | -30.5 | -61.8 | -0.22 |
| consensus_gap+follow_move | early | pin $1-2k | 6-7 | 46.2 | -2.2 | -11.3 | 0.4 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 1-3 | 25.0 | -3.3 | -35.0 | -0.65 |
| follow_move+pin_value | early | pin $1-2k | 6-7 | 46.2 | -1.5 | -14.7 | -0.25 |
| pin_value+rlm_quiet | early | pin $1-2k | 0-2 | 0.0 | -28.3 | -100.0 | -1.9 |
| follow_move+money_level | early | pin $1-2k | 12-6 | 66.7 | 2.8 | -0.4 | -0.03 |
| money_level+rlm_ratio | early | pin $1-2k | 1-1 | 50.0 | -12.2 | -1.0 | 0.75 |
| follow_move+money_moving | early | pin $1-2k | 4-3 | 57.1 | -7.9 | -23.6 | -0.13 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -28.3 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -28.3 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 4-5 | 44.4 | -12.8 | -31.7 | -0.69 |
| follow_move+pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -28.3 | -100.0 | -4.8 |
| pin_rlm+rlm_quiet | early | pin $1-2k | 0-1 | 0.0 | -28.3 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-2 | 0.0 | -50.0 | -100.0 | -1.65 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-3 | 0.0 | -42.8 | -100.0 | -0.67 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -28.3 | -100.0 | -4.8 |
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -28.3 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -28.3 | -100.0 | 1.3 |
| pin_move+pin_value | early | pin $1-2k | 0-2 | 0.0 | -47.3 | -100.0 | 0.0 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -71.7 | -100.0 | 1.5 |
| follow_move+pin_move | early | pin $1-2k | 1-1 | 50.0 | 2.7 | -2.9 | -0.5 |
| money_level+pin_move | early | pin $1-2k | 1-0 | 100.0 | 52.7 | 94.3 | -1.0 |
| consensus_gap+money_moving | early | pin $2k+ | 1-1 | 50.0 | 12.2 | -8.4 | 0.65 |
| consensus_gap+pin_value | early | pin $2k+ | 1-0 | 100.0 | 52.7 | 83.3 | 0.0 |
| follow_move+money_level | early | pin $2k+ | 0-1 | 0.0 | -52.7 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
| follow_move+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
| money_level+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -52.7 | -100.0 | 0.0 |
| money_level+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -52.7 | -100.0 | 0.0 |
| money_moving+pin_value | early | pin $2k+ | 1-0 | 100.0 | 52.7 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $2k+ | 0-2 | 0.0 | -40.5 | -100.0 | 0.65 |
| consensus_gap+follow_move | early | pin $2k+ | 0-1 | 0.0 | -28.3 | -100.0 | 1.3 |
| consensus_gap+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.3 | -100.0 | 1.3 |
| consensus_gap+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.3 | -100.0 | 1.3 |
| consensus_gap+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.3 | -100.0 | 1.3 |
| follow_move+money_moving | early | pin $2k+ | 0-1 | 0.0 | -28.3 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.3 | -100.0 | 1.3 |
| money_moving+rlm_quiet | early | pin $2k+ | 0-1 | 0.0 | -28.3 | -100.0 | 1.3 |
| money_moving+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.3 | -100.0 | 1.3 |
| money_moving+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.3 | -100.0 | 1.3 |
| rlm_quiet+rlm_ratio | early | pin $2k+ | 0-1 | 0.0 | -28.3 | -100.0 | 1.3 |
| rlm_quiet+sharp_gap | early | pin $2k+ | 0-1 | 0.0 | -28.3 | -100.0 | 1.3 |
| follow_move+rlm_quiet | early | pin limit <$1k | 6-8 | 42.9 | -2.2 | -13.5 | 0.23 |
| money_level+money_moving | early | pin limit <$1k | 17-7 | 70.8 | 19.2 | 32.1 | 0.48 |
| money_level+sharp_gap | early | pin limit <$1k | 25-20 | 55.6 | 5.6 | 2.6 | 0.24 |
| money_moving+sharp_gap | early | pin limit <$1k | 23-6 | 79.3 | 30.9 | 68.0 | 0.31 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -50.5 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 12-8 | 60.0 | 10.1 | 14.0 | 0.4 |
| money_moving+pin_value | early | pin limit <$1k | 10-4 | 71.4 | 21.8 | 35.6 | 0.36 |
| pin_value+sharp_gap | early | pin limit <$1k | 13-8 | 61.9 | 12.1 | 17.4 | 0.19 |
| consensus_gap+follow_move | early | pin limit <$1k | 7-10 | 41.2 | -10.4 | -23.2 | 0.41 |
| consensus_gap+money_level | early | pin limit <$1k | 6-7 | 46.2 | -8.4 | -19.0 | 0.31 |
| consensus_gap+pin_value | early | pin limit <$1k | 21-20 | 51.2 | 2.0 | -3.4 | 0.33 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 7-4 | 63.6 | 18.1 | 56.6 | 0.91 |
| follow_move+money_level | early | pin limit <$1k | 14-14 | 50.0 | -1.9 | -6.7 | -0.03 |
| follow_move+pin_value | early | pin limit <$1k | 18-15 | 54.5 | 5.1 | 2.9 | -0.18 |
| follow_move+sharp_gap | early | pin limit <$1k | 16-10 | 61.5 | 13.6 | 17.7 | -0.02 |
| follow_move+rlm_ratio | early | pin limit <$1k | 8-2 | 80.0 | 36.7 | 61.1 | 0.33 |
| money_level+rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.2 | 68.3 | 0.44 |
| pin_value+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.3 | 43.2 | -0.25 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 8-2 | 80.0 | 36.7 | 61.1 | 0.33 |
| consensus_gap+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 50.9 | 87.1 | 0.33 |
| consensus_gap+money_moving | early | pin limit <$1k | 10-3 | 76.9 | 29.1 | 76.9 | 0.65 |
| consensus_gap+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 1.6 | -8.4 | 1.5 |
| follow_move+money_delta | early | pin limit <$1k | 3-0 | 100.0 | 50.9 | 87.1 | 0.33 |
| follow_move+money_moving | early | pin limit <$1k | 13-5 | 72.2 | 22.8 | 38.2 | 0.39 |
| money_delta+money_moving | early | pin limit <$1k | 4-0 | 100.0 | 50.8 | 88.0 | 0.0 |
| money_delta+pin_value | early | pin limit <$1k | 4-0 | 100.0 | 50.8 | 88.0 | 0.0 |
| money_delta+rlm_quiet | early | pin limit <$1k | 1-0 | 100.0 | 52.7 | 83.3 | 0.0 |
| money_moving+rlm_quiet | early | pin limit <$1k | 4-2 | 66.7 | 17.4 | 26.0 | 0.0 |
| pin_value+rlm_quiet | early | pin limit <$1k | 1-3 | 25.0 | -25.0 | -54.2 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 4-1 | 80.0 | 30.1 | 54.4 | -0.2 |
| money_delta+sharp_gap | early | pin limit <$1k | 3-0 | 100.0 | 50.2 | 89.6 | 0.0 |
| rlm_quiet+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 10.6 | 32.0 | -0.1 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | 5.6 | 13.7 | -0.05 |
| pin_move+pin_value | early | pin limit <$1k | 4-8 | 33.3 | -16.4 | -36.0 | 0.42 |
| follow_move+pin_move | early | pin limit <$1k | 6-8 | 42.9 | -6.5 | -22.8 | 0.39 |
| consensus_gap+pin_move | early | pin limit <$1k | 2-4 | 33.3 | -19.8 | -35.7 | 0.43 |
| money_level+pin_move | early | pin limit <$1k | 3-6 | 33.3 | -17.0 | -44.0 | 0.27 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -49.5 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -49.5 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-4 | 33.3 | -13.3 | -47.8 | 0.47 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 21.7 | -3.7 | 0.25 |
| money_level+pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 21.7 | -3.7 | 0.25 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-1 | 50.0 | 21.7 | -3.7 | 0.25 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 21.7 | -3.7 | 0.25 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 21.7 | -3.7 | 0.25 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 21.7 | -3.7 | 0.25 |
| money_delta+money_level | early | pin limit <$1k | 2-0 | 100.0 | 50.5 | 90.9 | 0.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 50.5 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 50.5 | 90.9 | 1.0 |
| money_moving+pin_move | early | pin limit <$1k | 1-1 | 50.0 | 0.5 | -2.4 | 1.0 |
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
| rlm_quiet | close | 1-3k bets | 57-91 | 38.5 | -3.9 | -10.8 |  |
| rlm_quiet | close | 3k+ bets | 23-33 | 41.1 | -1.3 | -14.7 |  |
| rlm_quiet | close | <1k bets | 8-19 | 29.6 | -13.1 | -43.0 |  |
| rlm_quiet | close | pin $1-2k | 27-44 | 38.0 | -6.8 | -21.0 |  |
| rlm_quiet | close | pin $2k+ | 29-43 | 40.3 | -0.0 | 1.3 |  |
| rlm_quiet | close | pin limit <$1k | 10-13 | 43.5 | -3.4 | -15.7 |  |
| pin_move | close | 1-3k bets | 98-117 | 45.6 | -3.6 | -8.7 |  |
| pin_move | close | 3k+ bets | 39-54 | 41.9 | -8.3 | -21.8 |  |
| pin_move | close | <1k bets | 16-17 | 48.5 | -2.0 | -8.9 |  |
| pin_move | close | pin $1-2k | 62-91 | 40.5 | -9.1 | -21.3 |  |
| pin_move | close | pin $2k+ | 64-70 | 47.8 | -1.9 | -5.3 |  |
| pin_move | close | pin limit <$1k | 27-27 | 50.0 | 0.8 | -4.3 |  |
| money_delta | close | 1-3k bets | 50-67 | 42.7 | -1.2 | -12.9 |  |
| money_delta | close | 3k+ bets | 23-21 | 52.3 | 7.0 | 3.8 |  |
| money_delta | close | <1k bets | 13-13 | 50.0 | 6.4 | 12.6 |  |
| money_delta | close | pin $1-2k | 35-27 | 56.5 | 10.1 | 16.2 |  |
| money_delta | close | pin $2k+ | 18-26 | 40.9 | -0.1 | -16.1 |  |
| money_delta | close | pin limit <$1k | 10-18 | 35.7 | -11.0 | -31.2 |  |
| pin_rlm | close | 1-3k bets | 16-33 | 32.7 | -9.1 | -27.7 |  |
| pin_rlm | close | 3k+ bets | 7-15 | 31.8 | -9.6 | -33.9 |  |
| pin_rlm | close | <1k bets | 4-4 | 50.0 | 0.7 | -5.0 |  |
| pin_rlm | close | pin $1-2k | 14-22 | 38.9 | -5.9 | -18.8 |  |
| pin_rlm | close | pin $2k+ | 8-19 | 29.6 | -6.8 | -30.8 |  |
| pin_rlm | close | pin limit <$1k | 5-11 | 31.2 | -16.0 | -39.5 |  |
| follow_move | close | 1-3k bets | 164-199 | 45.2 | -4.0 | -11.0 |  |
| follow_move | close | 3k+ bets | 59-64 | 48.0 | -1.5 | -11.6 |  |
| follow_move | close | <1k bets | 38-43 | 46.9 | -3.0 | -16.7 |  |
| follow_move | close | pin $1-2k | 78-108 | 41.9 | -7.5 | -20.4 |  |
| follow_move | close | pin $2k+ | 80-84 | 48.8 | -0.3 | -1.7 |  |
| follow_move | close | pin limit <$1k | 32-33 | 49.2 | -0.3 | -5.6 |  |
| rlm_ratio | close | 1-3k bets | 31-60 | 34.1 | -7.6 | -26.2 |  |
| rlm_ratio | close | 3k+ bets | 12-19 | 38.7 | -3.3 | -19.4 |  |
| rlm_ratio | close | <1k bets | 9-10 | 47.4 | 2.6 | -9.9 |  |
| rlm_ratio | close | pin $1-2k | 20-25 | 44.4 | 0.5 | -8.2 |  |
| rlm_ratio | close | pin $2k+ | 8-20 | 28.6 | -7.7 | -34.9 |  |
| rlm_ratio | close | pin limit <$1k | 7-14 | 33.3 | -14.1 | -35.9 |  |
| money_level | close | 1-3k bets | 209-167 | 55.6 | -0.3 | -5.5 |  |
| money_level | close | 3k+ bets | 72-74 | 49.3 | -5.8 | -15.8 |  |
| money_level | close | <1k bets | 54-26 | 67.5 | 11.9 | 11.0 |  |
| money_level | close | pin $1-2k | 97-94 | 50.8 | -3.2 | -11.2 |  |
| money_level | close | pin $2k+ | 92-81 | 53.2 | -4.0 | -12.1 |  |
| money_level | close | pin limit <$1k | 40-30 | 57.1 | 5.3 | 8.9 |  |
| sharp_gap | close | 1-3k bets | 154-196 | 44.0 | -4.6 | -15.1 |  |
| sharp_gap | close | 3k+ bets | 56-81 | 40.9 | -7.5 | -20.7 |  |
| sharp_gap | close | <1k bets | 41-33 | 55.4 | 5.4 | 0.8 |  |
| sharp_gap | close | pin $1-2k | 83-92 | 47.4 | -1.4 | -8.2 |  |
| sharp_gap | close | pin $2k+ | 67-97 | 40.9 | -7.2 | -19.7 |  |
| sharp_gap | close | pin limit <$1k | 25-39 | 39.1 | -10.9 | -25.3 |  |
| money_moving | close | 1-3k bets | 164-191 | 46.2 | -2.8 | -11.6 |  |
| money_moving | close | 3k+ bets | 58-79 | 42.3 | -6.9 | -20.2 |  |
| money_moving | close | <1k bets | 41-31 | 56.9 | 6.7 | 3.5 |  |
| money_moving | close | pin $1-2k | 88-87 | 50.3 | 0.6 | -4.2 |  |
| money_moving | close | pin $2k+ | 70-94 | 42.7 | -5.4 | -16.8 |  |
| money_moving | close | pin limit <$1k | 28-41 | 40.6 | -9.3 | -22.4 |  |
| pin_value | close | 1-3k bets | 92-77 | 54.4 | 4.4 | 9.2 |  |
| pin_value | close | 3k+ bets | 21-37 | 36.2 | -14.3 | -31.4 |  |
| pin_value | close | <1k bets | 15-13 | 53.6 | 5.5 | 14.2 |  |
| pin_value | close | pin $1-2k | 58-63 | 47.9 | -1.8 | -5.3 |  |
| pin_value | close | pin $2k+ | 39-42 | 48.1 | -1.5 | 2.0 |  |
| pin_value | close | pin limit <$1k | 31-22 | 58.5 | 7.4 | 11.4 |  |
| consensus_gap | close | 1-3k bets | 72-62 | 53.7 | 0.9 | -1.8 |  |
| consensus_gap | close | 3k+ bets | 20-22 | 47.6 | -6.0 | -21.0 |  |
| consensus_gap | close | <1k bets | 16-7 | 69.6 | 18.3 | 30.6 |  |
| consensus_gap | close | pin $1-2k | 24-25 | 49.0 | -3.5 | -2.1 |  |
| consensus_gap | close | pin $2k+ | 50-25 | 66.7 | 10.5 | 19.8 |  |
| consensus_gap | close | pin limit <$1k | 8-10 | 44.4 | -5.1 | -15.3 |  |
| follow_move+pin_move | close | 1-3k bets | 64-96 | 40.0 | -8.9 | -21.9 |  |
| money_delta+money_moving | close | 1-3k bets | 39-48 | 44.8 | 2.1 | -7.2 |  |
| money_delta+sharp_gap | close | 1-3k bets | 39-47 | 45.3 | 2.7 | -6.1 |  |
| money_moving+sharp_gap | close | 1-3k bets | 150-184 | 44.9 | -3.9 | -13.1 |  |
| consensus_gap+money_level | close | 1-3k bets | 44-34 | 56.4 | -2.4 | -11.0 |  |
| follow_move+rlm_quiet | close | 1-3k bets | 57-91 | 38.5 | -3.9 | -10.8 |  |
| pin_move+rlm_quiet | close | 1-3k bets | 25-43 | 36.8 | -7.1 | -20.5 |  |
| consensus_gap+follow_move | close | 1-3k bets | 16-24 | 40.0 | -10.6 | -25.5 |  |
| follow_move+money_level | close | 1-3k bets | 78-73 | 51.7 | -4.1 | -10.2 |  |
| money_level+money_moving | close | 1-3k bets | 115-110 | 51.1 | -2.4 | -8.5 |  |
| money_level+sharp_gap | close | 1-3k bets | 107-110 | 49.3 | -3.9 | -10.8 |  |
| consensus_gap+money_moving | close | 1-3k bets | 19-33 | 36.5 | -14.1 | -28.8 |  |
| consensus_gap+pin_move | close | 1-3k bets | 15-12 | 55.6 | 6.1 | 26.3 |  |
| consensus_gap+pin_value | close | 1-3k bets | 26-24 | 52.0 | 2.1 | -2.4 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 19-34 | 35.8 | -14.5 | -30.4 |  |
| follow_move+money_moving | close | 1-3k bets | 78-106 | 42.4 | -6.1 | -17.2 |  |
| follow_move+pin_value | close | 1-3k bets | 28-22 | 56.0 | 5.2 | 24.7 |  |
| follow_move+sharp_gap | close | 1-3k bets | 78-109 | 41.7 | -6.6 | -18.9 |  |
| money_level+pin_move | close | 1-3k bets | 41-42 | 49.4 | -4.6 | -11.9 |  |
| money_level+pin_value | close | 1-3k bets | 35-34 | 50.7 | -0.5 | -5.2 |  |
| money_moving+pin_move | close | 1-3k bets | 40-51 | 44.0 | -4.4 | -14.0 |  |
| money_moving+pin_value | close | 1-3k bets | 29-36 | 44.6 | -5.5 | -16.5 |  |
| pin_move+pin_value | close | 1-3k bets | 32-32 | 50.0 | -1.3 | -6.0 |  |
| pin_move+sharp_gap | close | 1-3k bets | 38-58 | 39.6 | -8.3 | -22.4 |  |
| pin_value+sharp_gap | close | 1-3k bets | 28-37 | 43.1 | -7.3 | -19.5 |  |
| follow_move+money_delta | close | 1-3k bets | 27-44 | 38.0 | -5.9 | -22.5 |  |
| money_delta+pin_move | close | 1-3k bets | 15-24 | 38.5 | -5.3 | -24.6 |  |
| money_delta+rlm_quiet | close | 1-3k bets | 15-33 | 31.2 | -10.6 | -33.9 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 31-60 | 34.1 | -7.6 | -26.2 |  |
| money_moving+rlm_quiet | close | 1-3k bets | 21-46 | 31.3 | -8.7 | -27.4 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 31-55 | 36.0 | -5.9 | -21.9 |  |
| rlm_quiet+rlm_ratio | close | 1-3k bets | 15-43 | 25.9 | -13.6 | -38.2 |  |
| rlm_quiet+sharp_gap | close | 1-3k bets | 20-49 | 29.0 | -11.1 | -33.2 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 31-60 | 34.1 | -7.6 | -26.2 |  |
| money_delta+money_level | close | 1-3k bets | 14-11 | 56.0 | 6.6 | 10.3 |  |
| consensus_gap+rlm_quiet | close | 1-3k bets | 4-11 | 26.7 | -11.3 | -38.5 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 4-6 | 40.0 | 0.8 | -8.4 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 20-34 | 37.0 | -4.8 | -22.9 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 2-3 | 40.0 | -5.3 | 8.0 |  |
| money_level+pin_rlm | close | 1-3k bets | 7-7 | 50.0 | 2.8 | -2.1 |  |
| money_moving+pin_rlm | close | 1-3k bets | 16-28 | 36.4 | -6.1 | -19.5 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 16-33 | 32.7 | -9.1 | -27.7 |  |
| money_level+rlm_ratio | close | 1-3k bets | 13-13 | 50.0 | 3.0 | -3.0 |  |
| consensus_gap+money_delta | close | 1-3k bets | 6-5 | 54.5 | 12.1 | 4.4 |  |
| follow_move+pin_rlm | close | 1-3k bets | 14-28 | 33.3 | -7.9 | -25.7 |  |
| money_delta+pin_rlm | close | 1-3k bets | 9-18 | 33.3 | -7.5 | -33.7 |  |
| pin_move+pin_rlm | close | 1-3k bets | 16-28 | 36.4 | -5.7 | -19.5 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 15-25 | 37.5 | -4.7 | -17.4 |  |
| pin_rlm+rlm_quiet | close | 1-3k bets | 7-22 | 24.1 | -15.7 | -39.7 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 14-28 | 33.3 | -7.9 | -25.7 |  |
| money_delta+pin_value | close | 1-3k bets | 10-7 | 58.8 | 11.1 | 11.7 |  |
| pin_value+rlm_quiet | close | 1-3k bets | 6-8 | 42.9 | -4.2 | 51.7 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 4-3 | 57.1 | 7.4 | 7.1 |  |
| pin_rlm+pin_value | close | 1-3k bets | 2-5 | 28.6 | -20.3 | -46.0 |  |
| money_level+money_moving | close | 3k+ bets | 35-47 | 42.7 | -10.6 | -22.9 |  |
| money_level+sharp_gap | close | 3k+ bets | 32-47 | 40.5 | -12.2 | -24.4 |  |
| money_moving+sharp_gap | close | 3k+ bets | 55-77 | 41.7 | -7.0 | -19.8 |  |
| follow_move+money_delta | close | 3k+ bets | 8-13 | 38.1 | -6.2 | -23.3 |  |
| follow_move+money_level | close | 3k+ bets | 26-27 | 49.1 | -7.4 | -21.4 |  |
| follow_move+money_moving | close | 3k+ bets | 29-39 | 42.6 | -6.5 | -21.9 |  |
| follow_move+pin_move | close | 3k+ bets | 29-42 | 40.8 | -8.8 | -23.9 |  |
| follow_move+pin_rlm | close | 3k+ bets | 6-13 | 31.6 | -8.9 | -33.3 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 12-19 | 38.7 | -3.3 | -19.4 |  |
| follow_move+sharp_gap | close | 3k+ bets | 27-38 | 41.5 | -6.5 | -19.4 |  |
| money_delta+money_level | close | 3k+ bets | 4-6 | 40.0 | -9.4 | -22.5 |  |
| money_delta+money_moving | close | 3k+ bets | 14-18 | 43.8 | 0.2 | -11.8 |  |
| money_delta+pin_move | close | 3k+ bets | 5-11 | 31.2 | -14.5 | -38.8 |  |
| money_delta+pin_rlm | close | 3k+ bets | 4-7 | 36.4 | -6.1 | -24.1 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 5-8 | 38.5 | -3.0 | -20.5 |  |
| money_delta+sharp_gap | close | 3k+ bets | 14-18 | 43.8 | 0.2 | -11.8 |  |
| money_level+pin_move | close | 3k+ bets | 16-24 | 40.0 | -16.5 | -33.6 |  |
| money_level+pin_rlm | close | 3k+ bets | 1-2 | 33.3 | -16.1 | -34.9 |  |
| money_level+rlm_ratio | close | 3k+ bets | 3-3 | 50.0 | -0.2 | -3.8 |  |
| money_moving+pin_move | close | 3k+ bets | 14-31 | 31.1 | -18.8 | -44.4 |  |
| money_moving+pin_rlm | close | 3k+ bets | 7-14 | 33.3 | -8.5 | -30.7 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 11-19 | 36.7 | -5.7 | -25.8 |  |
| pin_move+pin_rlm | close | 3k+ bets | 5-14 | 26.3 | -16.5 | -48.5 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 5-14 | 26.3 | -16.4 | -48.3 |  |
| pin_move+sharp_gap | close | 3k+ bets | 12-31 | 27.9 | -21.2 | -47.3 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 6-13 | 31.6 | -8.9 | -33.3 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 7-15 | 31.8 | -9.6 | -33.9 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 12-19 | 38.7 | -3.3 | -19.4 |  |
| consensus_gap+money_level | close | 3k+ bets | 15-13 | 53.6 | -5.0 | -15.5 |  |
| consensus_gap+money_moving | close | 3k+ bets | 8-14 | 36.4 | -15.3 | -37.8 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 7-15 | 31.8 | -18.3 | -43.1 |  |
| follow_move+rlm_quiet | close | 3k+ bets | 23-33 | 41.1 | -1.3 | -14.7 |  |
| pin_move+rlm_quiet | close | 3k+ bets | 12-23 | 34.3 | -8.7 | -28.1 |  |
| money_delta+rlm_quiet | close | 3k+ bets | 6-8 | 42.9 | 0.4 | -12.6 |  |
| money_level+pin_value | close | 3k+ bets | 12-22 | 35.3 | -16.7 | -33.7 |  |
| money_moving+pin_value | close | 3k+ bets | 10-20 | 33.3 | -17.6 | -37.6 |  |
| pin_value+sharp_gap | close | 3k+ bets | 10-21 | 32.3 | -19.2 | -39.6 |  |
| consensus_gap+follow_move | close | 3k+ bets | 8-8 | 50.0 | -3.1 | -22.0 |  |
| consensus_gap+pin_value | close | 3k+ bets | 8-10 | 44.4 | -6.9 | -15.5 |  |
| money_moving+rlm_quiet | close | 3k+ bets | 10-19 | 34.5 | -8.3 | -31.7 |  |
| rlm_quiet+sharp_gap | close | 3k+ bets | 11-18 | 37.9 | -4.3 | -22.3 |  |
| pin_rlm+rlm_quiet | close | 3k+ bets | 4-12 | 25.0 | -15.2 | -47.6 |  |
| rlm_quiet+rlm_ratio | close | 3k+ bets | 8-16 | 33.3 | -7.0 | -29.7 |  |
| pin_move+pin_value | close | 3k+ bets | 13-20 | 39.4 | -11.3 | -25.4 |  |
| follow_move+pin_value | close | 3k+ bets | 8-15 | 34.8 | -15.6 | -34.2 |  |
| consensus_gap+money_delta | close | 3k+ bets | 2-2 | 50.0 | 1.1 | -5.3 |  |
| consensus_gap+pin_move | close | 3k+ bets | 11-9 | 55.0 | 2.8 | -4.7 |  |
| consensus_gap+rlm_quiet | close | 3k+ bets | 1-4 | 20.0 | -21.1 | -61.8 |  |
| money_delta+pin_value | close | 3k+ bets | 3-3 | 50.0 | -3.1 | -4.5 |  |
| pin_value+rlm_quiet | close | 3k+ bets | 2-6 | 25.0 | -24.6 | -53.0 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 1-4 | 20.0 | -25.4 | -62.5 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 0-3 | 0.0 | -39.5 | -100.0 |  |
| pin_rlm+pin_value | close | 3k+ bets | 1-3 | 25.0 | -27.1 | -53.1 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 0-2 | 0.0 | -50.0 | -100.0 |  |
| consensus_gap+money_level | close | <1k bets | 12-1 | 92.3 | 33.2 | 45.7 |  |
| consensus_gap+money_moving | close | <1k bets | 8-0 | 100.0 | 44.1 | 103.6 |  |
| consensus_gap+pin_value | close | <1k bets | 4-1 | 80.0 | 35.2 | 123.1 |  |
| consensus_gap+sharp_gap | close | <1k bets | 9-1 | 90.0 | 35.2 | 77.0 |  |
| follow_move+pin_move | close | <1k bets | 11-14 | 44.0 | -6.7 | -17.3 |  |
| follow_move+rlm_quiet | close | <1k bets | 8-19 | 29.6 | -13.1 | -43.0 |  |
| money_level+money_moving | close | <1k bets | 31-15 | 67.4 | 13.2 | 11.8 |  |
| money_level+pin_value | close | <1k bets | 7-4 | 63.6 | 14.4 | 19.5 |  |
| money_level+sharp_gap | close | <1k bets | 31-16 | 66.0 | 11.5 | 9.7 |  |
| money_moving+pin_value | close | <1k bets | 5-4 | 55.6 | 9.2 | 45.2 |  |
| money_moving+sharp_gap | close | <1k bets | 39-30 | 56.5 | 6.7 | 4.6 |  |
| pin_move+rlm_quiet | close | <1k bets | 3-4 | 42.9 | -5.0 | -18.6 |  |
| pin_value+sharp_gap | close | <1k bets | 5-4 | 55.6 | 9.2 | 45.2 |  |
| follow_move+money_moving | close | <1k bets | 19-16 | 54.3 | 4.3 | -6.7 |  |
| follow_move+sharp_gap | close | <1k bets | 18-17 | 51.4 | 1.4 | -9.3 |  |
| money_level+pin_move | close | <1k bets | 11-7 | 61.1 | 9.0 | 14.0 |  |
| money_moving+rlm_quiet | close | <1k bets | 4-7 | 36.4 | -7.3 | -30.5 |  |
| rlm_quiet+sharp_gap | close | <1k bets | 4-7 | 36.4 | -7.3 | -30.5 |  |
| follow_move+money_delta | close | <1k bets | 7-9 | 43.8 | -1.3 | -16.6 |  |
| follow_move+pin_rlm | close | <1k bets | 4-4 | 50.0 | 0.7 | -5.0 |  |
| follow_move+pin_value | close | <1k bets | 4-3 | 57.1 | 7.6 | 9.7 |  |
| follow_move+rlm_ratio | close | <1k bets | 9-10 | 47.4 | 2.6 | -9.9 |  |
| money_delta+money_moving | close | <1k bets | 9-11 | 45.0 | 3.1 | 8.2 |  |
| money_delta+pin_move | close | <1k bets | 1-3 | 25.0 | -22.0 | -52.3 |  |
| money_delta+pin_rlm | close | <1k bets | 1-3 | 25.0 | -22.0 | -52.3 |  |
| money_delta+pin_value | close | <1k bets | 3-0 | 100.0 | 57.8 | 212.0 |  |
| money_delta+rlm_quiet | close | <1k bets | 4-4 | 50.0 | 7.4 | -3.1 |  |
| money_delta+rlm_ratio | close | <1k bets | 5-7 | 41.7 | -1.7 | -20.7 |  |
| money_delta+sharp_gap | close | <1k bets | 9-11 | 45.0 | 3.1 | 8.2 |  |
| money_moving+pin_move | close | <1k bets | 8-7 | 53.3 | 4.1 | 0.8 |  |
| money_moving+pin_rlm | close | <1k bets | 4-4 | 50.0 | 0.7 | -5.0 |  |
| money_moving+rlm_ratio | close | <1k bets | 9-10 | 47.4 | 2.6 | -9.9 |  |
| pin_move+pin_rlm | close | <1k bets | 4-4 | 50.0 | 0.7 | -5.0 |  |
| pin_move+pin_value | close | <1k bets | 6-4 | 60.0 | 10.6 | 13.8 |  |
| pin_move+rlm_ratio | close | <1k bets | 4-4 | 50.0 | 0.7 | -5.0 |  |
| pin_move+sharp_gap | close | <1k bets | 8-7 | 53.3 | 4.1 | 0.8 |  |
| pin_rlm+pin_value | close | <1k bets | 1-0 | 100.0 | 53.0 | 90.9 |  |
| pin_rlm+rlm_quiet | close | <1k bets | 2-1 | 66.7 | 17.7 | 26.2 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 4-4 | 50.0 | 0.7 | -5.0 |  |
| pin_rlm+sharp_gap | close | <1k bets | 4-4 | 50.0 | 0.7 | -5.0 |  |
| pin_value+rlm_quiet | close | <1k bets | 2-0 | 100.0 | 53.0 | 90.9 |  |
| pin_value+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 53.0 | 90.9 |  |
| rlm_quiet+rlm_ratio | close | <1k bets | 4-6 | 40.0 | -3.3 | -23.5 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 9-10 | 47.4 | 2.6 | -9.9 |  |
| consensus_gap+follow_move | close | <1k bets | 5-1 | 83.3 | 28.6 | 42.8 |  |
| consensus_gap+pin_move | close | <1k bets | 2-0 | 100.0 | 42.9 | 70.5 |  |
| follow_move+money_level | close | <1k bets | 20-11 | 64.5 | 8.4 | 6.2 |  |
| money_delta+money_level | close | <1k bets | 3-3 | 50.0 | 8.0 | 7.7 |  |
| money_level+pin_rlm | close | <1k bets | 2-2 | 50.0 | 0.0 | -4.5 |  |
| money_level+rlm_ratio | close | <1k bets | 4-3 | 57.1 | 10.6 | 8.0 |  |
| consensus_gap+money_delta | close | <1k bets | 3-0 | 100.0 | 51.0 | 208.0 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 53.0 | 89.3 |  |
| consensus_gap+rlm_quiet | close | <1k bets | 1-1 | 50.0 | 10.1 | -4.5 |  |
| money_delta+money_moving | close | pin $1-2k | 20-16 | 55.6 | 10.8 | 20.0 |  |
| money_delta+sharp_gap | close | pin $1-2k | 20-16 | 55.6 | 10.8 | 20.0 |  |
| money_moving+sharp_gap | close | pin $1-2k | 80-83 | 49.1 | -0.1 | -4.6 |  |
| consensus_gap+follow_move | close | pin $1-2k | 7-11 | 38.9 | -12.9 | -30.7 |  |
| consensus_gap+money_level | close | pin $1-2k | 13-14 | 48.1 | -8.0 | -19.8 |  |
| consensus_gap+money_moving | close | pin $1-2k | 6-12 | 33.3 | -16.4 | -24.9 |  |
| consensus_gap+pin_move | close | pin $1-2k | 7-10 | 41.2 | -8.2 | -11.2 |  |
| consensus_gap+pin_value | close | pin $1-2k | 13-13 | 50.0 | 0.1 | 8.1 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 6-12 | 33.3 | -16.4 | -23.3 |  |
| follow_move+money_level | close | pin $1-2k | 36-44 | 45.0 | -8.9 | -21.0 |  |
| follow_move+money_moving | close | pin $1-2k | 41-50 | 45.1 | -4.1 | -14.2 |  |
| follow_move+pin_move | close | pin $1-2k | 39-77 | 33.6 | -15.6 | -34.7 |  |
| follow_move+pin_value | close | pin $1-2k | 19-25 | 43.2 | -7.0 | -18.9 |  |
| follow_move+sharp_gap | close | pin $1-2k | 42-54 | 43.8 | -5.3 | -16.4 |  |
| money_level+money_moving | close | pin $1-2k | 60-57 | 51.3 | -1.2 | -8.8 |  |
| money_level+pin_move | close | pin $1-2k | 26-40 | 39.4 | -13.3 | -29.9 |  |
| money_level+pin_value | close | pin $1-2k | 22-27 | 44.9 | -5.9 | -16.6 |  |
| money_level+sharp_gap | close | pin $1-2k | 55-58 | 48.7 | -3.3 | -12.0 |  |
| money_moving+pin_move | close | pin $1-2k | 31-41 | 43.1 | -7.1 | -18.0 |  |
| money_moving+pin_value | close | pin $1-2k | 19-23 | 45.2 | -4.2 | -7.2 |  |
| pin_move+pin_value | close | pin $1-2k | 21-29 | 42.0 | -9.1 | -21.3 |  |
| pin_move+sharp_gap | close | pin $1-2k | 30-47 | 39.0 | -10.1 | -24.9 |  |
| pin_value+sharp_gap | close | pin $1-2k | 19-23 | 45.2 | -4.2 | -7.2 |  |
| follow_move+money_delta | close | pin $1-2k | 17-21 | 44.7 | -2.0 | -13.1 |  |
| follow_move+rlm_quiet | close | pin $1-2k | 27-44 | 38.0 | -6.8 | -21.0 |  |
| money_delta+pin_move | close | pin $1-2k | 11-15 | 42.3 | -4.3 | -17.8 |  |
| money_delta+rlm_quiet | close | pin $1-2k | 10-14 | 41.7 | -4.2 | -19.3 |  |
| pin_move+rlm_quiet | close | pin $1-2k | 18-30 | 37.5 | -8.2 | -21.4 |  |
| follow_move+pin_rlm | close | pin $1-2k | 13-20 | 39.4 | -5.5 | -17.2 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 20-25 | 44.4 | 0.5 | -8.2 |  |
| pin_move+pin_rlm | close | pin $1-2k | 14-20 | 41.2 | -4.4 | -14.0 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 13-19 | 40.6 | -5.2 | -14.6 |  |
| pin_rlm+rlm_quiet | close | pin $1-2k | 8-16 | 33.3 | -10.9 | -26.4 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 13-20 | 39.4 | -5.5 | -17.2 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 14-22 | 38.9 | -5.9 | -18.8 |  |
| rlm_quiet+rlm_ratio | close | pin $1-2k | 10-18 | 35.7 | -8.1 | -22.8 |  |
| rlm_quiet+sharp_gap | close | pin $1-2k | 13-20 | 39.4 | -4.5 | -17.0 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 20-25 | 44.4 | 0.5 | -8.2 |  |
| money_delta+money_level | close | pin $1-2k | 8-8 | 50.0 | 1.2 | -3.1 |  |
| money_delta+pin_rlm | close | pin $1-2k | 7-9 | 43.8 | -1.8 | -15.0 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 10-10 | 50.0 | 5.3 | -2.4 |  |
| money_level+pin_rlm | close | pin $1-2k | 5-5 | 50.0 | 3.4 | -3.4 |  |
| money_level+rlm_ratio | close | pin $1-2k | 8-7 | 53.3 | 7.7 | 3.0 |  |
| money_moving+pin_rlm | close | pin $1-2k | 14-17 | 45.2 | -1.2 | -5.7 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 20-21 | 48.8 | 4.1 | 0.7 |  |
| money_moving+rlm_quiet | close | pin $1-2k | 13-18 | 41.9 | -2.2 | -11.7 |  |
| consensus_gap+rlm_quiet | close | pin $1-2k | 1-4 | 20.0 | -21.1 | -61.8 |  |
| pin_value+rlm_quiet | close | pin $1-2k | 5-10 | 33.3 | -15.0 | -35.8 |  |
| money_delta+pin_value | close | pin $1-2k | 7-5 | 58.3 | 12.5 | 41.3 |  |
| consensus_gap+money_delta | close | pin $1-2k | 3-1 | 75.0 | 30.1 | 131.4 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 0-2 | 0.0 | -42.9 | -100.0 |  |
| pin_rlm+pin_value | close | pin $1-2k | 3-5 | 37.5 | -11.9 | -28.9 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 2-4 | 33.3 | -15.7 | -37.0 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 0-1 | 0.0 | -53.0 | -100.0 |  |
| follow_move+pin_move | close | pin $2k+ | 48-57 | 45.7 | -3.7 | -13.2 |  |
| consensus_gap+money_level | close | pin $2k+ | 34-18 | 65.4 | 4.4 | 0.6 |  |
| follow_move+rlm_quiet | close | pin $2k+ | 29-43 | 40.3 | -0.0 | 1.3 |  |
| pin_move+rlm_quiet | close | pin $2k+ | 17-33 | 34.0 | -7.4 | -25.1 |  |
| money_level+money_moving | close | pin $2k+ | 47-56 | 45.6 | -8.0 | -18.3 |  |
| money_level+sharp_gap | close | pin $2k+ | 45-58 | 43.7 | -9.9 | -20.5 |  |
| money_moving+sharp_gap | close | pin $2k+ | 67-93 | 41.9 | -6.1 | -17.7 |  |
| consensus_gap+pin_value | close | pin $2k+ | 18-13 | 58.1 | 8.7 | 9.1 |  |
| follow_move+money_level | close | pin $2k+ | 32-28 | 53.3 | -5.8 | -13.5 |  |
| follow_move+money_moving | close | pin $2k+ | 30-44 | 40.5 | -7.6 | -23.5 |  |
| follow_move+sharp_gap | close | pin $2k+ | 27-43 | 38.6 | -9.4 | -25.9 |  |
| money_level+pin_move | close | pin $2k+ | 24-21 | 53.3 | -6.3 | -11.8 |  |
| money_moving+pin_move | close | pin $2k+ | 19-32 | 37.3 | -9.8 | -28.6 |  |
| pin_move+sharp_gap | close | pin $2k+ | 18-33 | 35.3 | -11.8 | -30.9 |  |
| money_delta+money_level | close | pin $2k+ | 5-3 | 62.5 | 16.8 | 28.7 |  |
| money_delta+money_moving | close | pin $2k+ | 14-26 | 35.0 | -4.5 | -27.0 |  |
| money_delta+sharp_gap | close | pin $2k+ | 14-26 | 35.0 | -4.5 | -27.0 |  |
| consensus_gap+money_moving | close | pin $2k+ | 16-17 | 48.5 | -4.8 | -4.9 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 15-18 | 45.5 | -7.8 | -8.5 |  |
| money_level+pin_value | close | pin $2k+ | 14-22 | 38.9 | -12.2 | -27.8 |  |
| money_moving+pin_value | close | pin $2k+ | 13-23 | 36.1 | -13.8 | -32.8 |  |
| pin_value+sharp_gap | close | pin $2k+ | 13-25 | 34.2 | -16.6 | -36.3 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 2-4 | 33.3 | -12.3 | -12.1 |  |
| money_level+pin_rlm | close | pin $2k+ | 1-2 | 33.3 | -18.1 | -28.7 |  |
| money_moving+pin_rlm | close | pin $2k+ | 8-18 | 30.8 | -5.8 | -28.2 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 8-19 | 29.6 | -6.8 | -30.8 |  |
| follow_move+money_delta | close | pin $2k+ | 7-15 | 31.8 | -7.4 | -34.5 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 8-20 | 28.6 | -7.7 | -34.9 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 5-14 | 26.3 | -10.5 | -44.3 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 8-20 | 28.6 | -7.7 | -34.9 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 8-20 | 28.6 | -7.7 | -34.9 |  |
| money_level+rlm_ratio | close | pin $2k+ | 3-2 | 60.0 | 14.3 | 17.9 |  |
| consensus_gap+follow_move | close | pin $2k+ | 14-7 | 66.7 | 9.5 | 13.8 |  |
| consensus_gap+pin_move | close | pin $2k+ | 19-8 | 70.4 | 17.3 | 39.1 |  |
| follow_move+pin_value | close | pin $2k+ | 10-10 | 50.0 | -0.6 | 42.5 |  |
| pin_move+pin_value | close | pin $2k+ | 17-18 | 48.6 | -2.5 | -8.5 |  |
| follow_move+pin_rlm | close | pin $2k+ | 6-15 | 28.6 | -5.2 | -31.0 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 6-15 | 28.6 | -5.2 | -31.0 |  |
| pin_value+rlm_quiet | close | pin $2k+ | 3-3 | 50.0 | 2.9 | 155.9 |  |
| money_moving+rlm_quiet | close | pin $2k+ | 8-20 | 28.6 | -8.5 | -33.4 |  |
| rlm_quiet+sharp_gap | close | pin $2k+ | 7-19 | 26.9 | -10.5 | -38.2 |  |
| money_delta+rlm_quiet | close | pin $2k+ | 5-12 | 29.4 | -8.4 | -38.7 |  |
| rlm_quiet+rlm_ratio | close | pin $2k+ | 4-16 | 20.0 | -13.8 | -50.0 |  |
| money_delta+pin_move | close | pin $2k+ | 7-13 | 35.0 | -5.9 | -30.7 |  |
| money_delta+pin_rlm | close | pin $2k+ | 5-12 | 29.4 | -7.1 | -37.5 |  |
| pin_move+pin_rlm | close | pin $2k+ | 6-15 | 28.6 | -7.2 | -33.7 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 6-14 | 30.0 | -6.0 | -32.6 |  |
| pin_rlm+rlm_quiet | close | pin $2k+ | 4-14 | 22.2 | -11.7 | -44.4 |  |
| consensus_gap+money_delta | close | pin $2k+ | 3-2 | 60.0 | 10.0 | 12.7 |  |
| consensus_gap+rlm_quiet | close | pin $2k+ | 2-3 | 40.0 | 3.0 | 6.2 |  |
| money_delta+pin_value | close | pin $2k+ | 4-3 | 57.1 | 4.1 | 8.2 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 2-2 | 50.0 | 11.9 | 31.2 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 1-0 | 100.0 | 45.7 | 84.7 |  |
| pin_rlm+pin_value | close | pin $2k+ | 1-1 | 50.0 | -4.3 | -6.2 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 4-4 | 50.0 | 2.5 | -3.9 |  |
| consensus_gap+money_level | close | pin limit <$1k | 4-5 | 44.4 | -8.5 | -16.4 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 4-8 | 33.3 | -15.5 | -35.9 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 7-9 | 43.8 | -7.0 | -17.2 |  |
| follow_move+money_level | close | pin limit <$1k | 20-17 | 54.1 | 3.0 | 3.3 |  |
| follow_move+money_moving | close | pin limit <$1k | 17-26 | 39.5 | -10.0 | -24.3 |  |
| follow_move+pin_value | close | pin limit <$1k | 11-5 | 68.8 | 17.2 | 31.0 |  |
| money_level+money_moving | close | pin limit <$1k | 21-24 | 46.7 | -4.7 | -11.1 |  |
| money_level+pin_value | close | pin limit <$1k | 18-11 | 62.1 | 9.9 | 18.1 |  |
| money_moving+pin_value | close | pin limit <$1k | 12-14 | 46.2 | -5.0 | -12.0 |  |
| follow_move+pin_move | close | pin limit <$1k | 17-18 | 48.6 | -0.4 | -6.5 |  |
| money_level+pin_move | close | pin limit <$1k | 18-12 | 60.0 | 9.4 | 14.4 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 25-38 | 39.7 | -10.2 | -24.1 |  |
| pin_move+pin_value | close | pin limit <$1k | 13-9 | 59.1 | 8.8 | 12.8 |  |
| follow_move+rlm_quiet | close | pin limit <$1k | 10-13 | 43.5 | -3.4 | -15.7 |  |
| money_moving+pin_move | close | pin limit <$1k | 12-16 | 42.9 | -6.2 | -18.0 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 3-2 | 60.0 | 15.8 | 16.4 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 2-3 | 40.0 | -4.2 | -21.8 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 1-2 | 33.3 | -8.9 | -33.3 |  |
| consensus_gap+rlm_quiet | close | pin limit <$1k | 3-2 | 60.0 | 15.8 | 16.4 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 2-2 | 50.0 | 6.6 | -2.3 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 4-8 | 33.3 | -15.5 | -35.9 |  |
| follow_move+money_delta | close | pin limit <$1k | 4-11 | 26.7 | -19.8 | -48.5 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 5-10 | 33.3 | -13.9 | -35.5 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 7-14 | 33.3 | -14.1 | -35.9 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 16-24 | 40.0 | -9.6 | -23.4 |  |
| money_delta+money_moving | close | pin limit <$1k | 8-13 | 38.1 | -8.5 | -26.4 |  |
| money_delta+pin_move | close | pin limit <$1k | 3-10 | 23.1 | -22.8 | -54.9 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 2-7 | 22.2 | -23.2 | -56.1 |  |
| money_delta+rlm_quiet | close | pin limit <$1k | 2-4 | 33.3 | -11.3 | -34.9 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 4-10 | 28.6 | -17.8 | -44.8 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 8-13 | 38.1 | -8.5 | -26.4 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 5-11 | 31.2 | -16.0 | -39.5 |  |
| money_moving+rlm_quiet | close | pin limit <$1k | 2-9 | 18.2 | -28.1 | -64.5 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 7-14 | 33.3 | -14.1 | -35.9 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 5-11 | 31.2 | -16.0 | -39.5 |  |
| pin_move+rlm_quiet | close | pin limit <$1k | 5-7 | 41.7 | -5.1 | -19.0 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 5-10 | 33.3 | -13.9 | -35.5 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 10-16 | 38.5 | -10.2 | -26.2 |  |
| pin_rlm+rlm_quiet | close | pin limit <$1k | 1-5 | 16.7 | -29.0 | -66.7 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 5-10 | 33.3 | -13.9 | -35.5 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 5-11 | 31.2 | -16.0 | -39.5 |  |
| rlm_quiet+rlm_ratio | close | pin limit <$1k | 2-8 | 20.0 | -26.2 | -60.9 |  |
| rlm_quiet+sharp_gap | close | pin limit <$1k | 2-8 | 20.0 | -26.2 | -60.9 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 7-14 | 33.3 | -14.1 | -35.9 |  |
| money_delta+pin_value | close | pin limit <$1k | 5-2 | 71.4 | 23.6 | 36.4 |  |
| pin_value+rlm_quiet | close | pin limit <$1k | 2-1 | 66.7 | 19.7 | 27.3 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 2-1 | 66.7 | 17.7 | 26.0 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 11-14 | 44.0 | -7.1 | -16.2 |  |
| money_level+sharp_gap | close | pin limit <$1k | 18-23 | 43.9 | -7.5 | -16.3 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 0-2 | 0.0 | -47.0 | -100.0 |  |
| money_delta+money_level | close | pin limit <$1k | 1-6 | 14.3 | -32.7 | -72.1 |  |
| money_level+pin_rlm | close | pin limit <$1k | 4-4 | 50.0 | 1.5 | -4.0 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 4-5 | 44.4 | -3.9 | -14.7 |  |
| rlm_quiet | early | <1k bets | 19-26 | 42.2 | 4.1 | 4.2 | 1.01 |
| rlm_quiet | early | pin $1-2k | 2-2 | 50.0 | 17.3 | 23.0 | 1.12 |
| rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 3.0 | -4.5 | 0.0 |
| pin_move | early | <1k bets | 6-11 | 35.3 | -13.5 | -32.2 | 0.18 |
| pin_move | early | pin $1-2k | 1-2 | 33.3 | -12.4 | -35.2 | -0.33 |
| pin_move | early | pin limit <$1k | 5-9 | 35.7 | -13.8 | -31.5 | 0.29 |
| money_delta | early | <1k bets | 4-4 | 50.0 | 11.9 | 30.9 | 2.86 |
| money_delta | early | pin $1-2k | 0-1 | 0.0 | -32.7 | -100.0 | 1.5 |
| money_delta | early | pin limit <$1k | 1-0 | 100.0 | 53.0 | 90.9 | 1.0 |
| pin_rlm | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
| follow_move | early | <1k bets | 155-184 | 45.7 | -3.3 | -13.3 | -0.01 |
| follow_move | early | pin $1-2k | 13-12 | 52.0 | 6.0 | 3.6 | -0.32 |
| follow_move | early | pin limit <$1k | 11-20 | 35.5 | -13.3 | -30.8 | -0.18 |
| rlm_ratio | early | <1k bets | 7-15 | 31.8 | -9.3 | -22.5 | 0.41 |
| rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 10.1 | -4.5 | 0.5 |
| money_level | early | <1k bets | 61-51 | 54.5 | -3.1 | -11.7 | -0.45 |
| money_level | early | pin $1-2k | 3-5 | 37.5 | -22.8 | -38.8 | -0.29 |
| money_level | early | pin limit <$1k | 7-6 | 53.8 | 3.3 | 3.1 | 0.38 |
| sharp_gap | early | <1k bets | 44-56 | 44.0 | -5.7 | -15.0 | 0.2 |
| sharp_gap | early | pin $1-2k | 2-6 | 25.0 | -36.3 | -63.1 | -0.04 |
| sharp_gap | early | pin limit <$1k | 6-5 | 54.5 | 5.6 | 4.5 | 0.45 |
| money_moving | early | <1k bets | 41-37 | 52.6 | 3.5 | 0.1 | 0.63 |
| money_moving | early | pin $1-2k | 0-4 | 0.0 | -55.4 | -100.0 | 1.05 |
| money_moving | early | pin limit <$1k | 9-2 | 81.8 | 31.9 | 54.5 | 0.36 |
| pin_value | early | <1k bets | 21-18 | 53.8 | 4.0 | 1.7 | 0.04 |
| pin_value | early | pin $1-2k | 6-9 | 40.0 | -9.4 | -24.9 | 0.25 |
| pin_value | early | pin limit <$1k | 15-9 | 62.5 | 12.4 | 18.4 | -0.08 |
| consensus_gap | early | <1k bets | 97-72 | 57.4 | 4.7 | 0.8 | 0.65 |
| consensus_gap | early | pin $1-2k | 10-5 | 66.7 | 16.1 | 23.1 | -0.17 |
| consensus_gap | early | pin limit <$1k | 8-4 | 66.7 | 16.2 | 26.7 | 0.08 |
| follow_move+money_level | early | <1k bets | 23-17 | 57.5 | 0.3 | -12.5 | 0.02 |
| follow_move+sharp_gap | early | <1k bets | 19-23 | 45.2 | -3.0 | -11.9 | 0.52 |
| money_level+sharp_gap | early | <1k bets | 31-33 | 48.4 | -6.8 | -17.4 | -0.25 |
| follow_move+money_moving | early | <1k bets | 18-16 | 52.9 | 4.6 | 6.1 | 0.53 |
| money_level+money_moving | early | <1k bets | 18-14 | 56.2 | 0.5 | -3.4 | 0.52 |
| consensus_gap+money_level | early | <1k bets | 20-15 | 57.1 | -3.7 | -13.5 | -0.61 |
| follow_move+rlm_quiet | early | <1k bets | 19-26 | 42.2 | 4.1 | 4.2 | 1.01 |
| follow_move+rlm_ratio | early | <1k bets | 7-15 | 31.8 | -9.3 | -22.5 | 0.41 |
| rlm_quiet+rlm_ratio | early | <1k bets | 6-9 | 40.0 | 1.6 | 0.9 | 0.3 |
| rlm_quiet+sharp_gap | early | <1k bets | 6-10 | 37.5 | -1.5 | -5.4 | 0.28 |
| rlm_ratio+sharp_gap | early | <1k bets | 7-15 | 31.8 | -9.3 | -22.5 | 0.41 |
| consensus_gap+follow_move | early | <1k bets | 14-13 | 51.9 | -3.4 | -11.4 | 0.93 |
| money_moving+rlm_quiet | early | <1k bets | 8-8 | 50.0 | 11.0 | 24.5 | 0.81 |
| money_moving+rlm_ratio | early | <1k bets | 7-5 | 58.3 | 17.9 | 42.0 | 1.36 |
| money_moving+sharp_gap | early | <1k bets | 22-24 | 47.8 | 0.9 | -0.5 | 0.89 |
| consensus_gap+money_moving | early | <1k bets | 10-4 | 71.4 | 15.9 | 14.1 | 1.39 |
| consensus_gap+sharp_gap | early | <1k bets | 12-12 | 50.0 | -5.4 | -18.3 | -0.56 |
| money_level+rlm_ratio | early | <1k bets | 1-6 | 14.3 | -32.6 | -72.7 | 0.64 |
| follow_move+pin_move | early | <1k bets | 2-6 | 25.0 | -21.4 | -51.9 | 0.12 |
| follow_move+money_delta | early | <1k bets | 3-1 | 75.0 | 35.1 | 114.0 | 2.35 |
| money_delta+money_level | early | <1k bets | 1-3 | 25.0 | -14.9 | -52.3 | 1.68 |
| money_delta+money_moving | early | <1k bets | 4-4 | 50.0 | 11.9 | 30.9 | 2.86 |
| money_delta+rlm_ratio | early | <1k bets | 3-1 | 75.0 | 35.1 | 114.0 | 2.35 |
| money_delta+sharp_gap | early | <1k bets | 4-4 | 50.0 | 11.9 | 30.9 | 2.86 |
| follow_move+pin_value | early | <1k bets | 4-4 | 50.0 | 1.1 | -4.5 | -0.62 |
| consensus_gap+pin_move | early | <1k bets | 2-1 | 66.7 | 15.2 | 28.7 | 0.33 |
| consensus_gap+pin_value | early | <1k bets | 10-3 | 76.9 | 27.4 | 45.4 | -0.15 |
| money_level+pin_move | early | <1k bets | 2-4 | 33.3 | -15.1 | -35.8 | 0.17 |
| money_level+pin_value | early | <1k bets | 3-3 | 50.0 | -4.4 | -4.5 | 0.78 |
| pin_move+pin_value | early | <1k bets | 3-6 | 33.3 | -16.7 | -35.9 | 0.44 |
| money_moving+pin_value | early | <1k bets | 3-2 | 60.0 | 7.5 | 15.4 | 1.14 |
| pin_value+sharp_gap | early | <1k bets | 1-4 | 20.0 | -34.9 | -61.8 | 1.34 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 53.0 | 90.9 | 1.0 |
| consensus_gap+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 53.0 | 90.9 | 1.0 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 53.0 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 53.0 | 90.9 | 1.0 |
| follow_move+pin_rlm | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| money_level+pin_rlm | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_rlm+rlm_ratio | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_rlm+sharp_gap | early | <1k bets | 0-2 | 0.0 | -50.0 | -100.0 | 0.75 |
| pin_move+sharp_gap | early | <1k bets | 0-3 | 0.0 | -46.2 | -100.0 | 1.0 |
| money_delta+rlm_quiet | early | <1k bets | 2-0 | 100.0 | 67.3 | 232.5 | 3.2 |
| consensus_gap+rlm_quiet | early | <1k bets | 1-0 | 100.0 | 67.3 | 160.0 | 0.3 |
| money_moving+pin_move | early | <1k bets | 1-1 | 50.0 | 3.0 | -2.4 | 1.0 |
| pin_move+pin_rlm | early | <1k bets | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
| pin_move+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
| pin_move+pin_value | early | pin $1-2k | 0-2 | 0.0 | -45.7 | -100.0 | 0.0 |
| follow_move+rlm_quiet | early | pin $1-2k | 2-2 | 50.0 | 17.3 | 23.0 | 1.12 |
| money_level+money_moving | early | pin $1-2k | 0-3 | 0.0 | -55.8 | -100.0 | 1.07 |
| money_level+pin_value | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.7 |
| money_level+sharp_gap | early | pin $1-2k | 2-5 | 28.6 | -33.8 | -57.8 | -0.19 |
| money_moving+pin_value | early | pin $1-2k | 0-2 | 0.0 | -60.8 | -100.0 | 1.35 |
| money_moving+sharp_gap | early | pin $1-2k | 0-4 | 0.0 | -55.4 | -100.0 | 1.05 |
| pin_value+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -60.8 | -100.0 | 1.35 |
| consensus_gap+pin_value | early | pin $1-2k | 3-1 | 75.0 | 27.1 | 39.3 | -0.5 |
| follow_move+money_level | early | pin $1-2k | 1-2 | 33.3 | -26.8 | -35.2 | 0.17 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| follow_move+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| follow_move+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -67.3 | -100.0 | 0.75 |
| money_level+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| money_level+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 1.5 |
| consensus_gap+follow_move | early | pin $1-2k | 2-1 | 66.7 | 22.4 | 55.3 | 0.6 |
| follow_move+pin_move | early | pin $1-2k | 1-1 | 50.0 | 4.3 | -2.9 | -0.5 |
| follow_move+pin_value | early | pin $1-2k | 0-1 | 0.0 | -45.7 | -100.0 | 0.0 |
| consensus_gap+money_level | early | pin $1-2k | 2-1 | 66.7 | -0.6 | -1.6 | -1.83 |
| consensus_gap+sharp_gap | early | pin $1-2k | 2-1 | 66.7 | -0.6 | -1.6 | -1.83 |
| consensus_gap+rlm_quiet | early | pin $1-2k | 1-0 | 100.0 | 67.3 | 160.0 | 0.3 |
| consensus_gap+money_moving | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 0-1 | 0.0 | -67.3 | -100.0 | 0.0 |
| money_level+pin_move | early | pin $1-2k | 1-0 | 100.0 | 54.3 | 94.3 | -1.0 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -32.7 | -100.0 | 1.5 |
| money_delta+money_moving | early | pin $1-2k | 0-1 | 0.0 | -32.7 | -100.0 | 1.5 |
| money_delta+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -32.7 | -100.0 | 1.5 |
| follow_move+pin_move | early | pin limit <$1k | 1-5 | 16.7 | -30.0 | -68.2 | 0.33 |
| follow_move+pin_value | early | pin limit <$1k | 4-3 | 57.1 | 7.8 | 9.1 | -0.71 |
| consensus_gap+money_level | early | pin limit <$1k | 3-0 | 100.0 | 49.0 | 90.9 | 0.0 |
| consensus_gap+pin_move | early | pin limit <$1k | 2-1 | 66.7 | 15.2 | 28.7 | 0.33 |
| consensus_gap+pin_value | early | pin limit <$1k | 7-2 | 77.8 | 27.6 | 48.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 4-2 | 66.7 | 18.7 | 28.0 | 0.5 |
| follow_move+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 3.0 | -4.5 | 0.0 |
| follow_move+sharp_gap | early | pin limit <$1k | 3-3 | 50.0 | 3.4 | -3.8 | 0.17 |
| money_level+pin_move | early | pin limit <$1k | 1-4 | 20.0 | -28.9 | -61.8 | 0.4 |
| money_level+pin_value | early | pin limit <$1k | 3-2 | 60.0 | 8.2 | 14.5 | 0.6 |
| money_moving+rlm_quiet | early | pin limit <$1k | 1-1 | 50.0 | 3.0 | -4.5 | 0.0 |
| money_moving+sharp_gap | early | pin limit <$1k | 5-1 | 83.3 | 34.3 | 59.8 | 0.17 |
| pin_move+pin_value | early | pin limit <$1k | 3-4 | 42.9 | -8.4 | -17.6 | 0.57 |
| rlm_quiet+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -47.0 | -100.0 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 | -0.5 |
| consensus_gap+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 53.0 | 90.9 | 1.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 53.0 | 92.3 | 1.0 |
| consensus_gap+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 53.0 | 90.9 | 1.0 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 53.0 | 90.9 | 1.0 |
| follow_move+money_delta | early | pin limit <$1k | 1-0 | 100.0 | 53.0 | 90.9 | 1.0 |
| follow_move+money_level | early | pin limit <$1k | 3-3 | 50.0 | 2.4 | -3.8 | 0.0 |
| follow_move+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 10.1 | -4.5 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 53.0 | 90.9 | 1.0 |
| money_delta+money_moving | early | pin limit <$1k | 1-0 | 100.0 | 53.0 | 90.9 | 1.0 |
| money_delta+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 53.0 | 90.9 | 1.0 |
| money_delta+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 53.0 | 90.9 | 1.0 |
| money_delta+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 53.0 | 90.9 | 1.0 |
| money_level+money_moving | early | pin limit <$1k | 4-0 | 100.0 | 50.0 | 92.0 | 0.5 |
| money_level+rlm_ratio | early | pin limit <$1k | 1-1 | 50.0 | 10.1 | -4.5 | 0.5 |
| money_level+sharp_gap | early | pin limit <$1k | 5-4 | 55.6 | 6.1 | 6.5 | 0.67 |
| money_moving+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 53.0 | 92.3 | 1.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 53.0 | 90.9 | 1.0 |
| pin_value+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 53.0 | 90.9 | 1.0 |
| pin_value+sharp_gap | early | pin limit <$1k | 1-2 | 33.3 | -17.7 | -36.4 | 1.33 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 10.1 | -4.5 | 0.5 |
| pin_move+sharp_gap | early | pin limit <$1k | 0-3 | 0.0 | -46.2 | -100.0 | 1.0 |
| money_moving+pin_move | early | pin limit <$1k | 1-1 | 50.0 | 3.0 | -2.4 | 1.0 |
| follow_move+pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
| money_level+pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
| pin_move+pin_rlm | early | pin limit <$1k | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
| pin_move+rlm_ratio | early | pin limit <$1k | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 0-1 | 0.0 | -32.7 | -100.0 | 0.0 |
