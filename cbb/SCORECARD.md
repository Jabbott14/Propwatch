# CBB scorecard

Generated 2026-11-20 20:46 UTC. 672 graded games (23 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**645 games before 2026-11-20 (fit) · 27 on or after it (forward).**

Every signal, threshold and PROMOTE/DROP label here was chosen while looking at
the games before 2026-11-20. `pin_value` went 108-68 in first halves --
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
sample ran **48.1% favourites** (n=671) and **49.4% overs** (n=672) and **74.1% moneyline favourites** (n=571).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-20. Nothing in the engine was chosen using these. n=27 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| money_delta | both | 0-2 | 0.0 | 35.0 | -35.0 | -2.0 | -100.0 | 1.0 | 50.0 | keep collecting (2/30) |
| follow_move | both | 10-9 | 52.6 | 48.9 | 3.7 | -0.21 | -1.1 | 0.36 | 42.1 | keep collecting (19/30) |
| rlm_ratio | both | 4-2 | 66.7 | 36.9 | 29.8 | +1.91 | 31.8 | 0.7 | 50.0 | keep collecting (6/30) |
| money_level | both | 7-8 | 46.7 | 61.9 | -15.2 | -3.38 | -22.6 | -0.32 | 46.7 | keep collecting (15/30) |
| sharp_gap | both | 8-6 | 57.1 | 46.0 | 11.1 | +3.55 | 25.4 | 0.81 | 50.0 | keep collecting (14/30) |
| money_moving | both | 3-10 | 23.1 | 46.1 | -23.0 | -7.6 | -58.4 | -0.71 | 23.1 | keep collecting (13/30) |
| consensus_gap | both | 3-3 | 50.0 | 59.5 | -9.5 | -1.24 | -20.6 | 0.57 | 50.0 | keep collecting (6/30) |
| money_moving+sharp_gap | both | 2-4 | 33.3 | 43.8 | -10.5 | -2.96 | -49.3 | -0.35 | 16.7 | keep collecting (6/30) |
| follow_move+money_level | both | 4-3 | 57.1 | 60.0 | -2.8 | -0.3 | -4.2 | -0.64 | 42.9 | keep collecting (7/30) |
| follow_move+money_moving | both | 3-4 | 42.9 | 47.1 | -4.2 | -1.6 | -22.8 | -0.74 | 28.6 | keep collecting (7/30) |
| follow_move+sharp_gap | both | 7-2 | 77.8 | 46.9 | 30.9 | +3.7 | 41.2 | 0.41 | 44.4 | keep collecting (9/30) |
| money_level+money_moving | both | 1-5 | 16.7 | 58.2 | -41.5 | -4.91 | -81.8 | -0.75 | 50.0 | keep collecting (6/30) |
| money_level+sharp_gap | both | 3-2 | 60.0 | 62.5 | -2.5 | -0.21 | -4.1 | 0.52 | 60.0 | keep collecting (5/30) |
| follow_move+money_delta | both | 0-1 | 0.0 | 40.7 | -40.7 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| follow_move+rlm_ratio | both | 4-2 | 66.7 | 36.9 | 29.8 | +1.91 | 31.8 | 0.7 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | both | 0-1 | 0.0 | 40.7 | -40.7 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | both | 0-2 | 0.0 | 35.0 | -35.0 | -2.0 | -100.0 | 1.0 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | both | 0-1 | 0.0 | 40.7 | -40.7 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| money_delta+sharp_gap | both | 0-1 | 0.0 | 40.7 | -40.7 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| money_level+rlm_ratio | both | 0-1 | 0.0 | 40.7 | -40.7 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| money_moving+rlm_ratio | both | 1-2 | 33.3 | 36.9 | -3.5 | -1.05 | -34.9 | 0.13 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | both | 4-2 | 66.7 | 36.9 | 29.8 | +1.91 | 31.8 | 0.7 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 1-2 | 33.3 | 55.7 | -22.4 | -1.17 | -38.9 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+money_level | both | 2-2 | 50.0 | 65.2 | -15.2 | -1.07 | -26.8 | 1.1 | 75.0 | keep collecting (4/30) |
| consensus_gap+money_moving | both | 0-1 | 0.0 | 48.1 | -48.1 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+sharp_gap | both | 1-1 | 50.0 | 70.8 | -20.8 | -0.17 | -8.4 | 0.55 | 50.0 | keep collecting (2/30) |
| money_delta | moneyline | 0-1 | 0.0 | 29.2 | -29.2 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta | total | 0-1 | 0.0 | 40.7 | -40.7 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| follow_move | moneyline | 5-3 | 62.5 | 50.0 | 12.5 | +1.24 | 15.5 | 0.48 | 37.5 | keep collecting (8/30) |
| follow_move | spread | 0-5 | 0.0 | 49.6 | -49.6 | -5.0 | -100.0 | 0.4 | 40.0 | keep collecting (5/30) |
| follow_move | total | 5-1 | 83.3 | 46.9 | 36.4 | +3.55 | 59.1 | 0.17 | 50.0 | keep collecting (6/30) |
| rlm_ratio | moneyline | 1-1 | 50.0 | 29.2 | 20.8 | +0.14 | 7.0 | 0.6 | 50.0 | keep collecting (2/30) |
| rlm_ratio | total | 3-1 | 75.0 | 40.7 | 34.3 | +1.77 | 44.2 | 0.75 | 50.0 | keep collecting (4/30) |
| money_level | moneyline | 3-3 | 50.0 | 70.8 | -20.8 | -1.98 | -33.0 | -0.97 | 33.3 | keep collecting (6/30) |
| money_level | spread | 0-1 | 0.0 | 48.1 | -48.1 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| money_level | total | 4-4 | 50.0 | 56.9 | -6.9 | -0.4 | -5.0 | -0.12 | 50.0 | keep collecting (8/30) |
| sharp_gap | moneyline | 4-2 | 66.7 | 50.0 | 16.7 | +3.91 | 65.2 | 0.4 | 50.0 | keep collecting (6/30) |
| sharp_gap | total | 4-4 | 50.0 | 43.1 | 6.9 | -0.36 | -4.5 | 1.12 | 50.0 | keep collecting (8/30) |
| money_moving | moneyline | 2-3 | 40.0 | 45.8 | -5.8 | -1.55 | -31.0 | -1.64 | 0.0 | keep collecting (5/30) |
| money_moving | spread | 0-1 | 0.0 | 48.1 | -48.1 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| money_moving | total | 1-6 | 14.3 | 46.0 | -31.7 | -5.05 | -72.1 | -0.43 | 28.6 | keep collecting (7/30) |
| consensus_gap | moneyline | 2-1 | 66.7 | 70.8 | -4.2 | -0.07 | -2.4 | 0.8 | 66.7 | keep collecting (3/30) |
| consensus_gap | spread | 1-2 | 33.3 | 48.1 | -14.8 | -1.17 | -38.9 | 0.33 | 33.3 | keep collecting (3/30) |
| follow_move+money_level | moneyline | 2-1 | 66.7 | 70.8 | -4.2 | -0.08 | -2.5 | -2.17 | 0.0 | keep collecting (3/30) |
| follow_move+money_moving | moneyline | 2-2 | 50.0 | 50.0 | 0.0 | -0.55 | -13.7 | -2.05 | 0.0 | keep collecting (4/30) |
| follow_move+sharp_gap | moneyline | 3-1 | 75.0 | 50.0 | 25.0 | +1.06 | 26.6 | -0.32 | 25.0 | keep collecting (4/30) |
| money_level+money_moving | moneyline | 1-1 | 50.0 | 70.8 | -20.8 | -0.91 | -45.5 | -3.25 | 0.0 | keep collecting (2/30) |
| money_level+sharp_gap | moneyline | 2-1 | 66.7 | 70.8 | -4.2 | -0.08 | -2.5 | -0.47 | 33.3 | keep collecting (3/30) |
| money_moving+sharp_gap | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.91 | -45.5 | -1.55 | 0.0 | keep collecting (2/30) |
| follow_move+rlm_ratio | moneyline | 1-1 | 50.0 | 29.2 | 20.8 | +0.14 | 7.0 | 0.6 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 1-1 | 50.0 | 29.2 | 20.8 | +0.14 | 7.0 | 0.6 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_level | moneyline | 2-1 | 66.7 | 70.8 | -4.2 | -0.07 | -2.4 | 0.8 | 66.7 | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+sharp_gap | moneyline | 1-1 | 50.0 | 70.8 | -20.8 | -0.17 | -8.4 | 0.55 | 50.0 | keep collecting (2/30) |
| consensus_gap+follow_move | moneyline | 1-0 | 100.0 | 70.8 | 29.2 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+money_moving | moneyline | 0-1 | 0.0 | 29.2 | -29.2 | -1.0 | -100.0 | 0.0 | 0.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_moving+rlm_ratio | moneyline | 0-1 | 0.0 | 29.2 | -29.2 | -1.0 | -100.0 | -0.6 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | spread | 0-2 | 0.0 | 48.1 | -48.1 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| consensus_gap+money_level | spread | 0-1 | 0.0 | 48.1 | -48.1 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| consensus_gap+money_moving | spread | 0-1 | 0.0 | 48.1 | -48.1 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+money_level | spread | 0-1 | 0.0 | 48.1 | -48.1 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| follow_move+money_moving | spread | 0-1 | 0.0 | 48.1 | -48.1 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| money_level+money_moving | spread | 0-1 | 0.0 | 48.1 | -48.1 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_moving+sharp_gap | total | 1-3 | 25.0 | 40.7 | -15.7 | -2.05 | -51.2 | 0.25 | 25.0 | keep collecting (4/30) |
| follow_move+money_delta | total | 0-1 | 0.0 | 40.7 | -40.7 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| follow_move+money_level | total | 2-1 | 66.7 | 53.1 | 13.6 | +0.78 | 26.0 | 0.0 | 66.7 | keep collecting (3/30) |
| follow_move+money_moving | total | 1-1 | 50.0 | 40.7 | 9.3 | -0.05 | -2.4 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+rlm_ratio | total | 3-1 | 75.0 | 40.7 | 34.3 | +1.77 | 44.2 | 0.75 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 4-1 | 80.0 | 44.4 | 35.6 | +2.64 | 52.8 | 1.0 | 60.0 | keep collecting (5/30) |
| money_delta+money_level | total | 0-1 | 0.0 | 40.7 | -40.7 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+money_moving | total | 0-1 | 0.0 | 40.7 | -40.7 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+rlm_ratio | total | 0-1 | 0.0 | 40.7 | -40.7 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | total | 0-1 | 0.0 | 40.7 | -40.7 | -1.0 | -100.0 | 2.0 | 100.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_level+money_moving | total | 0-3 | 0.0 | 53.1 | -53.1 | -3.0 | -100.0 | 0.0 | 66.7 | keep collecting (3/30) |
| money_level+rlm_ratio | total | 0-1 | 0.0 | 40.7 | -40.7 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.13 | -6.5 | 2.0 | 100.0 | keep collecting (2/30) |
| money_moving+rlm_ratio | total | 1-1 | 50.0 | 40.7 | 9.3 | -0.05 | -2.4 | 0.5 | 50.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | total | 3-1 | 75.0 | 40.7 | 34.3 | +1.77 | 44.2 | 0.75 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_move | both | 22-16 | 57.9 | 48.4 | 9.5 | +6.3 | 16.6 |  |  | no edge shown yet |
| money_delta | both | 12-19 | 38.7 | 42.3 | -3.6 | -5.33 | -17.2 |  |  | DROP: below break-even |
| pin_rlm | both | 8-7 | 53.3 | 39.9 | 13.4 | +2.82 | 18.8 |  |  | keep collecting (15/30) |
| follow_move | both | 30-26 | 53.6 | 50.0 | 3.6 | -2.24 | -4.0 |  |  | no edge shown yet |
| rlm_ratio | both | 6-10 | 37.5 | 40.0 | -2.5 | -3.66 | -22.9 |  |  | keep collecting (16/30) |
| money_level | both | 48-30 | 61.5 | 57.1 | 4.4 | +5.37 | 6.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 35-39 | 47.3 | 45.6 | 1.7 | -6.01 | -8.1 |  |  | no edge shown yet |
| money_moving | both | 35-38 | 47.9 | 46.6 | 1.3 | -5.13 | -7.0 |  |  | no edge shown yet |
| pin_value | both | 14-7 | 66.7 | 53.1 | 13.6 | +5.2 | 24.7 |  |  | keep collecting (21/30) |
| consensus_gap | both | 8-6 | 57.1 | 51.0 | 6.1 | +0.37 | 2.6 |  |  | keep collecting (14/30) |
| consensus_gap+money_level | both | 7-3 | 70.0 | 57.5 | 12.5 | +2.25 | 22.5 |  |  | keep collecting (10/30) |
| consensus_gap+money_moving | both | 4-3 | 57.1 | 44.8 | 12.3 | -0.38 | -5.4 |  |  | keep collecting (7/30) |
| consensus_gap+pin_value | both | 5-0 | 100.0 | 54.8 | 45.2 | +4.39 | 87.8 |  |  | keep collecting (5/30) |
| consensus_gap+sharp_gap | both | 4-3 | 57.1 | 44.8 | 12.3 | -0.38 | -5.4 |  |  | keep collecting (7/30) |
| follow_move+money_delta | both | 6-7 | 46.2 | 45.0 | 1.2 | -1.33 | -10.3 |  |  | keep collecting (13/30) |
| money_level+money_moving | both | 25-18 | 58.1 | 53.0 | 5.1 | +2.47 | 5.7 |  |  | no edge shown yet |
| money_level+pin_value | both | 12-4 | 75.0 | 54.9 | 20.1 | +6.41 | 40.1 |  |  | keep collecting (16/30) |
| money_level+sharp_gap | both | 23-16 | 59.0 | 52.4 | 6.6 | +2.68 | 6.9 |  |  | no edge shown yet |
| money_moving+pin_value | both | 8-5 | 61.5 | 51.6 | 9.9 | +1.91 | 14.7 |  |  | keep collecting (13/30) |
| money_moving+sharp_gap | both | 33-36 | 47.8 | 45.9 | 1.9 | -4.92 | -7.1 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 7-6 | 53.8 | 50.2 | 3.7 | +0.03 | 0.3 |  |  | keep collecting (13/30) |
| money_delta+money_moving | both | 7-14 | 33.3 | 39.4 | -6.0 | -5.13 | -24.4 |  |  | keep collecting (21/30) |
| money_delta+sharp_gap | both | 7-14 | 33.3 | 39.4 | -6.0 | -5.13 | -24.4 |  |  | keep collecting (21/30) |
| money_level+pin_move | both | 12-7 | 63.2 | 55.7 | 7.5 | +3.45 | 18.2 |  |  | keep collecting (19/30) |
| pin_move+pin_value | both | 8-4 | 66.7 | 51.3 | 15.4 | +2.91 | 24.2 |  |  | keep collecting (12/30) |
| follow_move+money_level | both | 16-11 | 59.3 | 57.6 | 1.6 | -0.82 | -3.0 |  |  | keep collecting (27/30) |
| follow_move+money_moving | both | 13-15 | 46.4 | 46.0 | 0.4 | -2.63 | -9.4 |  |  | keep collecting (28/30) |
| follow_move+pin_move | both | 14-9 | 60.9 | 47.8 | 13.0 | +3.55 | 15.4 |  |  | keep collecting (23/30) |
| follow_move+pin_value | both | 5-4 | 55.6 | 51.5 | 4.1 | +0.26 | 2.8 |  |  | keep collecting (9/30) |
| follow_move+sharp_gap | both | 13-16 | 44.8 | 45.8 | -1.0 | -3.63 | -12.5 |  |  | keep collecting (29/30) |
| money_moving+pin_move | both | 14-11 | 56.0 | 48.5 | 7.5 | +3.74 | 15.0 |  |  | keep collecting (25/30) |
| pin_move+sharp_gap | both | 15-11 | 57.7 | 47.5 | 10.2 | +4.69 | 18.1 |  |  | keep collecting (26/30) |
| follow_move+pin_rlm | both | 5-5 | 50.0 | 40.7 | 9.3 | -0.34 | -3.4 |  |  | keep collecting (10/30) |
| follow_move+rlm_ratio | both | 6-10 | 37.5 | 40.0 | -2.5 | -3.66 | -22.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | both | 4-2 | 66.7 | 44.4 | 22.3 | +1.68 | 28.0 |  |  | keep collecting (6/30) |
| money_delta+pin_move | both | 8-5 | 61.5 | 44.7 | 16.8 | +4.85 | 37.3 |  |  | keep collecting (13/30) |
| money_delta+pin_rlm | both | 6-4 | 60.0 | 40.6 | 19.4 | +3.96 | 39.6 |  |  | keep collecting (10/30) |
| money_delta+rlm_ratio | both | 3-5 | 37.5 | 40.7 | -3.2 | -2.2 | -27.5 |  |  | keep collecting (8/30) |
| money_level+pin_rlm | both | 3-1 | 75.0 | 46.3 | 28.7 | +1.77 | 44.2 |  |  | keep collecting (4/30) |
| money_level+rlm_ratio | both | 1-1 | 50.0 | 46.3 | 3.7 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| money_moving+pin_rlm | both | 8-6 | 57.1 | 39.8 | 17.3 | +3.82 | 27.3 |  |  | keep collecting (14/30) |
| money_moving+rlm_ratio | both | 6-9 | 40.0 | 39.9 | 0.1 | -2.66 | -17.7 |  |  | keep collecting (15/30) |
| pin_move+pin_rlm | both | 7-7 | 50.0 | 40.7 | 9.3 | +1.84 | 13.1 |  |  | keep collecting (14/30) |
| pin_move+rlm_ratio | both | 4-5 | 44.4 | 42.0 | 2.5 | -1.32 | -14.7 |  |  | keep collecting (9/30) |
| pin_rlm+rlm_ratio | both | 5-5 | 50.0 | 40.7 | 9.3 | -0.34 | -3.4 |  |  | keep collecting (10/30) |
| pin_rlm+sharp_gap | both | 8-7 | 53.3 | 39.9 | 13.4 | +2.82 | 18.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | both | 6-10 | 37.5 | 40.0 | -2.5 | -3.66 | -22.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+pin_value | both | 2-2 | 50.0 | 46.3 | 3.7 | -0.14 | -3.5 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | both | 2-0 | 100.0 | 44.2 | 55.8 | +2.03 | 101.4 |  |  | keep collecting (2/30) |
| consensus_gap+pin_move | both | 3-1 | 75.0 | 51.9 | 23.1 | +1.86 | 46.6 |  |  | keep collecting (4/30) |
| money_delta+pin_value | both | 1-2 | 33.3 | 50.6 | -17.3 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| pin_value+rlm_ratio | both | 1-1 | 50.0 | 46.3 | 3.7 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| consensus_gap+money_delta | both | 0-2 | 0.0 | 29.2 | -29.2 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_move | moneyline | 4-4 | 50.0 | 50.0 | 0.0 | +1.89 | 23.6 |  |  | keep collecting (8/30) |
| pin_move | spread | 8-6 | 57.1 | 49.7 | 7.4 | +1.23 | 8.8 |  |  | keep collecting (14/30) |
| pin_move | total | 10-6 | 62.5 | 46.5 | 16.0 | +3.18 | 19.9 |  |  | keep collecting (16/30) |
| money_delta | moneyline | 2-6 | 25.0 | 29.2 | -4.2 | -1.72 | -21.5 |  |  | keep collecting (8/30) |
| money_delta | spread | 7-6 | 53.8 | 51.6 | 2.3 | +0.62 | 4.8 |  |  | keep collecting (13/30) |
| money_delta | total | 3-7 | 30.0 | 40.7 | -10.7 | -4.23 | -42.3 |  |  | keep collecting (10/30) |
| pin_rlm | moneyline | 2-1 | 66.7 | 29.2 | 37.5 | +3.28 | 109.3 |  |  | keep collecting (3/30) |
| pin_rlm | spread | 1-1 | 50.0 | 51.9 | -1.9 | -0.09 | -4.5 |  |  | keep collecting (2/30) |
| pin_rlm | total | 5-5 | 50.0 | 40.7 | 9.3 | -0.37 | -3.7 |  |  | keep collecting (10/30) |
| follow_move | moneyline | 15-5 | 75.0 | 54.2 | 20.8 | +5.11 | 25.6 |  |  | keep collecting (20/30) |
| follow_move | spread | 8-11 | 42.1 | 49.9 | -7.8 | -3.72 | -19.6 |  |  | keep collecting (19/30) |
| follow_move | total | 7-10 | 41.2 | 45.1 | -3.9 | -3.63 | -21.4 |  |  | keep collecting (17/30) |
| rlm_ratio | moneyline | 2-0 | 100.0 | 29.2 | 70.8 | +2.66 | 133.0 |  |  | keep collecting (2/30) |
| rlm_ratio | spread | 0-1 | 0.0 | 51.9 | -51.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| rlm_ratio | total | 4-9 | 30.8 | 40.7 | -10.0 | -5.32 | -40.9 |  |  | keep collecting (13/30) |
| money_level | moneyline | 14-10 | 58.3 | 65.6 | -7.3 | -5.19 | -21.6 |  |  | keep collecting (24/30) |
| money_level | spread | 15-12 | 55.6 | 49.5 | 6.0 | +1.55 | 5.8 |  |  | keep collecting (27/30) |
| money_level | total | 19-8 | 70.4 | 57.2 | 13.2 | +9.01 | 33.4 |  |  | keep collecting (27/30) |
| sharp_gap | moneyline | 10-12 | 45.5 | 44.3 | 1.1 | -1.77 | -8.0 |  |  | keep collecting (22/30) |
| sharp_gap | spread | 13-12 | 52.0 | 49.6 | 2.4 | -0.29 | -1.2 |  |  | keep collecting (25/30) |
| sharp_gap | total | 12-15 | 44.4 | 42.8 | 1.6 | -3.95 | -14.6 |  |  | keep collecting (27/30) |
| money_moving | moneyline | 10-12 | 45.5 | 44.3 | 1.1 | -1.77 | -8.0 |  |  | keep collecting (22/30) |
| money_moving | spread | 13-12 | 52.0 | 49.6 | 2.4 | -0.29 | -1.2 |  |  | keep collecting (25/30) |
| money_moving | total | 12-14 | 46.2 | 45.7 | 0.4 | -3.07 | -11.8 |  |  | keep collecting (26/30) |
| pin_value | moneyline | 1-0 | 100.0 | 70.8 | 29.2 | +0.69 | 68.5 |  |  | keep collecting (1/30) |
| pin_value | spread | 5-5 | 50.0 | 48.9 | 1.1 | -0.68 | -6.8 |  |  | keep collecting (10/30) |
| pin_value | total | 8-2 | 80.0 | 55.6 | 24.4 | +5.19 | 51.9 |  |  | keep collecting (10/30) |
| consensus_gap | moneyline | 2-5 | 28.6 | 47.0 | -18.5 | -3.87 | -55.2 |  |  | keep collecting (7/30) |
| consensus_gap | spread | 2-1 | 66.7 | 49.4 | 17.3 | +0.7 | 23.4 |  |  | keep collecting (3/30) |
| consensus_gap | total | 4-0 | 100.0 | 59.3 | 40.7 | +3.54 | 88.4 |  |  | keep collecting (4/30) |
| money_level+money_moving | moneyline | 6-5 | 54.5 | 59.5 | -4.9 | -1.77 | -16.1 |  |  | keep collecting (11/30) |
| money_level+sharp_gap | moneyline | 6-5 | 54.5 | 59.5 | -4.9 | -1.77 | -16.1 |  |  | keep collecting (11/30) |
| money_moving+sharp_gap | moneyline | 10-12 | 45.5 | 44.3 | 1.1 | -1.77 | -8.0 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+money_level | moneyline | 8-3 | 72.7 | 67.0 | 5.7 | +0.0 | 0.0 |  |  | keep collecting (11/30) |
| money_delta+money_level | moneyline | 0-1 | 0.0 | 29.2 | -29.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_delta+money_moving | moneyline | 2-5 | 28.6 | 29.2 | -0.6 | -0.72 | -10.3 |  |  | keep collecting (7/30) |
| money_delta+sharp_gap | moneyline | 2-5 | 28.6 | 29.2 | -0.6 | -0.72 | -10.3 |  |  | keep collecting (7/30) |
| money_moving+pin_move | moneyline | 3-2 | 60.0 | 54.2 | 5.8 | +2.77 | 55.3 |  |  | keep collecting (5/30) |
| money_moving+pin_rlm | moneyline | 2-1 | 66.7 | 29.2 | 37.5 | +3.28 | 109.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_rlm | moneyline | 1-1 | 50.0 | 29.2 | 20.8 | +2.3 | 115.0 |  |  | keep collecting (2/30) |
| pin_move+sharp_gap | moneyline | 3-2 | 60.0 | 54.2 | 5.8 | +2.77 | 55.3 |  |  | keep collecting (5/30) |
| pin_rlm+sharp_gap | moneyline | 2-1 | 66.7 | 29.2 | 37.5 | +3.28 | 109.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+pin_move | moneyline | 1-0 | 100.0 | 29.2 | 70.8 | +3.3 | 330.0 |  |  | keep collecting (1/30) |
| money_delta+pin_rlm | moneyline | 2-0 | 100.0 | 29.2 | 70.8 | +4.28 | 214.0 |  |  | keep collecting (2/30) |
| consensus_gap+money_level | moneyline | 1-3 | 25.0 | 60.4 | -35.4 | -2.99 | -74.7 |  |  | keep collecting (4/30) |
| consensus_gap+money_moving | moneyline | 1-3 | 25.0 | 39.6 | -14.6 | -2.99 | -74.7 |  |  | keep collecting (4/30) |
| consensus_gap+sharp_gap | moneyline | 1-3 | 25.0 | 39.6 | -14.6 | -2.99 | -74.7 |  |  | keep collecting (4/30) |
| follow_move+money_moving | moneyline | 4-1 | 80.0 | 45.8 | 34.2 | +3.13 | 62.5 |  |  | keep collecting (5/30) |
| follow_move+pin_move | moneyline | 3-1 | 75.0 | 50.0 | 25.0 | +1.59 | 39.7 |  |  | keep collecting (4/30) |
| follow_move+sharp_gap | moneyline | 4-1 | 80.0 | 45.8 | 34.2 | +3.13 | 62.5 |  |  | keep collecting (5/30) |
| money_level+pin_move | moneyline | 2-2 | 50.0 | 70.8 | -20.8 | -0.53 | -13.3 |  |  | keep collecting (4/30) |
| consensus_gap+pin_move | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | +0.12 | 6.0 |  |  | keep collecting (2/30) |
| follow_move+rlm_ratio | moneyline | 2-0 | 100.0 | 29.2 | 70.8 | +2.66 | 133.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_ratio | moneyline | 2-0 | 100.0 | 29.2 | 70.8 | +2.66 | 133.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 2-0 | 100.0 | 29.2 | 70.8 | +2.66 | 133.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 1-0 | 100.0 | 29.2 | 70.8 | +1.12 | 112.0 |  |  | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 1-0 | 100.0 | 29.2 | 70.8 | +0.98 | 98.0 |  |  | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-0 | 100.0 | 29.2 | 70.8 | +0.98 | 98.0 |  |  | keep collecting (1/30) |
| money_delta+rlm_ratio | moneyline | 1-0 | 100.0 | 29.2 | 70.8 | +0.98 | 98.0 |  |  | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-0 | 100.0 | 29.2 | 70.8 | +0.98 | 98.0 |  |  | keep collecting (1/30) |
| consensus_gap+money_delta | moneyline | 0-2 | 0.0 | 29.2 | -29.2 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| follow_move+pin_value | moneyline | 1-0 | 100.0 | 70.8 | 29.2 | +0.69 | 68.5 |  |  | redundant -- identical record to pin_value alone, not independent confirmation |
| money_level+pin_value | moneyline | 1-0 | 100.0 | 70.8 | 29.2 | +0.69 | 68.5 |  |  | redundant -- identical record to pin_value alone, not independent confirmation |
| money_moving+pin_value | moneyline | 1-0 | 100.0 | 70.8 | 29.2 | +0.69 | 68.5 |  |  | redundant -- identical record to pin_value alone, not independent confirmation |
| pin_move+pin_value | moneyline | 1-0 | 100.0 | 70.8 | 29.2 | +0.69 | 68.5 |  |  | redundant -- identical record to pin_value alone, not independent confirmation |
| pin_value+sharp_gap | moneyline | 1-0 | 100.0 | 70.8 | 29.2 | +0.69 | 68.5 |  |  | redundant -- identical record to pin_value alone, not independent confirmation |
| consensus_gap+money_level | spread | 2-0 | 100.0 | 48.1 | 51.9 | +1.7 | 85.1 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | spread | 2-0 | 100.0 | 48.1 | 51.9 | +1.7 | 85.1 |  |  | keep collecting (2/30) |
| consensus_gap+pin_value | spread | 2-0 | 100.0 | 48.1 | 51.9 | +1.7 | 85.1 |  |  | keep collecting (2/30) |
| consensus_gap+sharp_gap | spread | 2-0 | 100.0 | 48.1 | 51.9 | +1.7 | 85.1 |  |  | keep collecting (2/30) |
| follow_move+money_delta | spread | 3-3 | 50.0 | 51.9 | -1.9 | -0.13 | -2.2 |  |  | keep collecting (6/30) |
| money_level+money_moving | spread | 12-10 | 54.5 | 49.5 | 5.1 | +0.86 | 3.9 |  |  | keep collecting (22/30) |
| money_level+pin_value | spread | 4-4 | 50.0 | 49.1 | 0.9 | -0.51 | -6.4 |  |  | keep collecting (8/30) |
| money_level+sharp_gap | spread | 12-10 | 54.5 | 49.5 | 5.1 | +0.86 | 3.9 |  |  | keep collecting (22/30) |
| money_moving+pin_value | spread | 4-5 | 44.4 | 49.0 | -4.5 | -1.51 | -16.8 |  |  | keep collecting (9/30) |
| money_moving+sharp_gap | spread | 13-12 | 52.0 | 49.6 | 2.4 | -0.29 | -1.2 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| pin_value+sharp_gap | spread | 4-5 | 44.4 | 49.0 | -4.5 | -1.51 | -16.8 |  |  | keep collecting (9/30) |
| follow_move+money_level | spread | 4-7 | 36.4 | 49.2 | -12.8 | -3.42 | -31.1 |  |  | keep collecting (11/30) |
| follow_move+money_moving | spread | 3-5 | 37.5 | 49.1 | -11.6 | -2.25 | -28.2 |  |  | keep collecting (8/30) |
| follow_move+pin_move | spread | 4-4 | 50.0 | 49.5 | 0.5 | -0.4 | -5.0 |  |  | keep collecting (8/30) |
| follow_move+pin_value | spread | 2-4 | 33.3 | 48.8 | -15.4 | -2.29 | -38.2 |  |  | keep collecting (6/30) |
| follow_move+sharp_gap | spread | 3-5 | 37.5 | 49.1 | -11.6 | -2.25 | -28.2 |  |  | keep collecting (8/30) |
| money_level+pin_move | spread | 4-4 | 50.0 | 49.5 | 0.5 | -0.47 | -5.9 |  |  | keep collecting (8/30) |
| money_moving+pin_move | spread | 4-4 | 50.0 | 49.5 | 0.5 | -0.47 | -5.9 |  |  | keep collecting (8/30) |
| pin_move+pin_value | spread | 4-3 | 57.1 | 49.2 | 7.9 | +0.45 | 6.5 |  |  | keep collecting (7/30) |
| pin_move+sharp_gap | spread | 4-4 | 50.0 | 49.5 | 0.5 | -0.47 | -5.9 |  |  | keep collecting (8/30) |
| money_delta+pin_move | spread | 4-2 | 66.7 | 51.2 | 15.4 | +1.78 | 29.6 |  |  | keep collecting (6/30) |
| money_delta+money_level | spread | 2-1 | 66.7 | 51.9 | 14.8 | +0.82 | 27.3 |  |  | keep collecting (3/30) |
| money_delta+money_moving | spread | 2-3 | 40.0 | 51.1 | -11.1 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| money_delta+sharp_gap | spread | 2-3 | 40.0 | 51.1 | -11.1 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| money_delta+pin_value | spread | 1-2 | 33.3 | 50.6 | -17.3 | -1.09 | -36.4 |  |  | keep collecting (3/30) |
| follow_move+pin_rlm | spread | 0-1 | 0.0 | 51.9 | -51.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| follow_move+rlm_ratio | spread | 0-1 | 0.0 | 51.9 | -51.9 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | spread | 1-1 | 50.0 | 51.9 | -1.9 | -0.09 | -4.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_delta+rlm_ratio | spread | 0-1 | 0.0 | 51.9 | -51.9 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | spread | 1-1 | 50.0 | 51.9 | -1.9 | -0.09 | -4.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm_ratio | spread | 0-1 | 0.0 | 51.9 | -51.9 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_rlm | spread | 1-1 | 50.0 | 51.9 | -1.9 | -0.09 | -4.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-1 | 0.0 | 51.9 | -51.9 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_move+pin_rlm | spread | 1-1 | 50.0 | 51.9 | -1.9 | -0.09 | -4.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | spread | 0-1 | 0.0 | 51.9 | -51.9 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+pin_value | spread | 1-1 | 50.0 | 51.9 | -1.9 | -0.09 | -4.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | spread | 0-1 | 0.0 | 51.9 | -51.9 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 1-1 | 50.0 | 51.9 | -1.9 | -0.09 | -4.5 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 0-1 | 0.0 | 51.9 | -51.9 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 0-1 | 0.0 | 51.9 | -51.9 | -1.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+pin_move | spread | 1-0 | 100.0 | 48.1 | 51.9 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| money_delta+money_moving | total | 3-6 | 33.3 | 40.7 | -7.4 | -3.23 | -35.9 |  |  | keep collecting (9/30) |
| money_delta+sharp_gap | total | 3-6 | 33.3 | 40.7 | -7.4 | -3.23 | -35.9 |  |  | keep collecting (9/30) |
| money_level+pin_move | total | 6-1 | 85.7 | 54.0 | 31.7 | +4.46 | 63.7 |  |  | keep collecting (7/30) |
| money_level+pin_value | total | 7-0 | 100.0 | 59.3 | 40.7 | +6.24 | 89.1 |  |  | keep collecting (7/30) |
| money_moving+sharp_gap | total | 10-12 | 45.5 | 43.3 | 2.2 | -2.86 | -13.0 |  |  | keep collecting (22/30) |
| pin_move+pin_value | total | 3-1 | 75.0 | 50.0 | 25.0 | +1.77 | 44.2 |  |  | keep collecting (4/30) |
| consensus_gap+money_level | total | 4-0 | 100.0 | 59.3 | 40.7 | +3.54 | 88.4 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+pin_value | total | 3-0 | 100.0 | 59.3 | 40.7 | +2.69 | 89.6 |  |  | keep collecting (3/30) |
| follow_move+money_delta | total | 2-4 | 33.3 | 40.7 | -7.4 | -2.18 | -36.4 |  |  | keep collecting (6/30) |
| follow_move+money_level | total | 4-1 | 80.0 | 55.6 | 24.4 | +2.6 | 51.9 |  |  | keep collecting (5/30) |
| follow_move+money_moving | total | 6-9 | 40.0 | 44.4 | -4.4 | -3.5 | -23.4 |  |  | keep collecting (15/30) |
| follow_move+pin_move | total | 7-4 | 63.6 | 45.8 | 17.8 | +2.37 | 21.5 |  |  | keep collecting (11/30) |
| follow_move+pin_rlm | total | 4-4 | 50.0 | 40.7 | 9.3 | -0.32 | -4.0 |  |  | keep collecting (8/30) |
| follow_move+rlm_ratio | total | 4-9 | 30.8 | 40.7 | -10.0 | -5.32 | -40.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 6-10 | 37.5 | 44.2 | -6.7 | -4.5 | -28.1 |  |  | keep collecting (16/30) |
| money_delta+money_level | total | 2-0 | 100.0 | 40.7 | 59.3 | +1.86 | 93.0 |  |  | keep collecting (2/30) |
| money_delta+pin_move | total | 3-3 | 50.0 | 40.7 | 9.3 | -0.23 | -3.8 |  |  | keep collecting (6/30) |
| money_delta+pin_rlm | total | 3-3 | 50.0 | 40.7 | 9.3 | -0.23 | -3.8 |  |  | keep collecting (6/30) |
| money_delta+rlm_ratio | total | 2-4 | 33.3 | 40.7 | -7.4 | -2.18 | -36.4 |  |  | keep collecting (6/30) |
| money_level+money_moving | total | 7-3 | 70.0 | 53.7 | 16.3 | +3.37 | 33.7 |  |  | keep collecting (10/30) |
| money_level+pin_rlm | total | 2-0 | 100.0 | 40.7 | 59.3 | +1.86 | 93.0 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | total | 1-0 | 100.0 | 40.7 | 59.3 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | total | 5-1 | 83.3 | 50.0 | 33.3 | +3.59 | 59.8 |  |  | keep collecting (6/30) |
| money_moving+pin_move | total | 7-5 | 58.3 | 45.4 | 13.0 | +1.45 | 12.1 |  |  | keep collecting (12/30) |
| money_moving+pin_rlm | total | 5-4 | 55.6 | 40.7 | 14.8 | +0.63 | 7.0 |  |  | keep collecting (9/30) |
| money_moving+rlm_ratio | total | 4-8 | 33.3 | 40.7 | -7.4 | -4.32 | -36.0 |  |  | keep collecting (12/30) |
| pin_move+pin_rlm | total | 5-5 | 50.0 | 40.7 | 9.3 | -0.37 | -3.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 4-4 | 50.0 | 40.7 | 9.3 | -0.32 | -4.0 |  |  | keep collecting (8/30) |
| pin_move+sharp_gap | total | 8-5 | 61.5 | 43.6 | 17.9 | +2.4 | 18.5 |  |  | keep collecting (13/30) |
| pin_rlm+rlm_ratio | total | 4-4 | 50.0 | 40.7 | 9.3 | -0.32 | -4.0 |  |  | keep collecting (8/30) |
| pin_rlm+sharp_gap | total | 5-5 | 50.0 | 40.7 | 9.3 | -0.37 | -3.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | total | 4-9 | 30.8 | 40.7 | -10.0 | -5.32 | -40.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+pin_value | total | 1-1 | 50.0 | 40.7 | 9.3 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| pin_value+sharp_gap | total | 2-1 | 66.7 | 46.9 | 19.8 | +0.86 | 28.7 |  |  | keep collecting (3/30) |
| money_moving+pin_value | total | 3-0 | 100.0 | 53.1 | 46.9 | +2.74 | 91.3 |  |  | keep collecting (3/30) |
| consensus_gap+follow_move | total | 1-0 | 100.0 | 59.3 | 40.7 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| consensus_gap+money_moving | total | 1-0 | 100.0 | 59.3 | 40.7 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| consensus_gap+pin_move | total | 1-0 | 100.0 | 59.3 | 40.7 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| consensus_gap+sharp_gap | total | 1-0 | 100.0 | 59.3 | 40.7 | +0.91 | 90.9 |  |  | keep collecting (1/30) |
| follow_move+pin_value | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 |  |  | keep collecting (2/30) |
| pin_value+rlm_ratio | total | 1-0 | 100.0 | 40.7 | 59.3 | +0.95 | 95.2 |  |  | keep collecting (1/30) |

# FIT (in-sample — this is the hypothesis)

Games before 2026-11-20. The engine was built by looking at these, so a strong record here is expected and proves nothing. n=645 games.

## EARLY  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_move | both | 5-9 | 35.7 | 48.1 | -12.4 | -5.1 | -36.4 | 0.22 | 50.0 | keep collecting (14/30) |
| money_delta | both | 10-5 | 66.7 | 42.2 | 24.5 | +6.43 | 42.9 | -0.38 | 26.7 | keep collecting (15/30) |
| pin_rlm | both | 1-2 | 33.3 | 25.8 | 7.6 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | both | 459-392 | 53.9 | 52.6 | 1.3 | -47.36 | -5.6 | 0.21 | 42.3 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | both | 25-16 | 61.0 | 37.4 | 23.6 | +17.63 | 43.0 | 0.35 | 51.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | both | 162-100 | 61.8 | 59.3 | 2.5 | -7.12 | -2.7 | -0.08 | 39.3 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 135-113 | 54.4 | 48.3 | 6.2 | +16.54 | 6.7 | 0.23 | 42.7 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | both | 99-71 | 58.2 | 51.6 | 6.6 | +7.79 | 4.6 | 0.07 | 42.9 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| pin_value | both | 49-48 | 50.5 | 48.3 | 2.2 | -4.43 | -4.6 | 0.1 | 38.1 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.1 | -31.1 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 215-282 | 43.3 | 46.9 | -3.6 | -56.66 | -11.4 | 0.38 | 45.3 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | both | 31-26 | 54.4 | 64.1 | -9.7 | -8.54 | -15.0 | 0.29 | 47.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | both | 17-22 | 43.6 | 46.6 | -3.0 | -5.42 | -13.9 | 0.21 | 41.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_value | both | 19-28 | 40.4 | 46.4 | -6.0 | -11.54 | -24.5 | 0.39 | 48.9 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_ratio | both | 25-16 | 61.0 | 37.4 | 23.6 | +17.63 | 43.0 | 0.35 | 51.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 68-36 | 65.4 | 49.9 | 15.5 | +20.61 | 19.8 | 0.36 | 48.1 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 63-35 | 64.3 | 58.4 | 5.9 | +4.04 | 4.1 | -0.13 | 46.9 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | both | 11-9 | 55.0 | 50.0 | 5.0 | +0.81 | 4.0 | 0.4 | 45.0 | keep collecting (20/30) |
| money_moving+pin_value | both | 8-5 | 61.5 | 50.0 | 11.5 | +2.04 | 15.7 | 0.31 | 38.5 | keep collecting (13/30) |
| rlm_ratio+sharp_gap | both | 25-16 | 61.0 | 37.4 | 23.6 | +17.63 | 43.0 | 0.35 | 51.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 94-57 | 62.3 | 55.6 | 6.7 | +5.37 | 3.6 | 0.13 | 43.0 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 58-43 | 57.4 | 48.8 | 8.6 | +8.96 | 8.9 | 0.16 | 45.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_level | both | 3-1 | 75.0 | 44.4 | 30.6 | +2.46 | 61.5 | 0.95 | 50.0 | keep collecting (4/30) |
| money_delta+money_moving | both | 9-5 | 64.3 | 41.6 | 22.7 | +5.53 | 39.5 | -0.41 | 28.6 | keep collecting (14/30) |
| money_delta+pin_value | both | 3-1 | 75.0 | 50.0 | 25.0 | +1.61 | 40.3 | 0.0 | 25.0 | keep collecting (4/30) |
| money_delta+sharp_gap | both | 7-4 | 63.6 | 39.3 | 24.4 | +4.78 | 43.5 | -0.52 | 36.4 | keep collecting (11/30) |
| pin_value+sharp_gap | both | 13-8 | 61.9 | 48.9 | 13.0 | +3.66 | 17.4 | -0.18 | 33.3 | keep collecting (21/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 49.0 | -49.0 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 30-38 | 44.1 | 51.4 | -7.3 | -13.76 | -20.2 | 0.8 | 57.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | both | 20-17 | 54.1 | 48.8 | 5.2 | +0.41 | 1.1 | -0.12 | 29.7 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+sharp_gap | both | 24-44 | 35.3 | 44.5 | -9.2 | -11.04 | -16.2 | 0.92 | 50.0 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | both | 86-41 | 67.7 | 60.4 | 7.3 | +1.27 | 1.0 | 0.09 | 44.1 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 11-6 | 64.7 | 40.7 | 24.1 | +5.43 | 31.9 | 1.18 | 58.8 | keep collecting (17/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 44.2 | 5.8 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 50-25 | 66.7 | 53.4 | 13.3 | +11.4 | 15.2 | 0.39 | 53.3 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 3-0 | 100.0 | 48.7 | 51.3 | +2.61 | 87.1 | 0.0 | 0.0 | keep collecting (3/30) |
| follow_move+money_delta | both | 5-2 | 71.4 | 39.5 | 31.9 | +4.95 | 70.7 | -0.23 | 28.6 | keep collecting (7/30) |
| money_moving+rlm_ratio | both | 11-6 | 64.7 | 40.3 | 24.4 | +7.71 | 45.4 | 0.17 | 47.1 | keep collecting (17/30) |
| consensus_gap+rlm_ratio | both | 3-4 | 42.9 | 36.6 | 6.3 | -0.82 | -11.7 | 0.93 | 71.4 | keep collecting (7/30) |
| pin_move+pin_value | both | 1-4 | 20.0 | 49.1 | -29.1 | -3.09 | -61.8 | 0.2 | 20.0 | keep collecting (5/30) |
| follow_move+pin_move | both | 5-3 | 62.5 | 52.6 | 9.9 | +0.9 | 11.2 | 0.42 | 62.5 | keep collecting (8/30) |
| consensus_gap+pin_move | both | 0-5 | 0.0 | 44.4 | -44.4 | -5.0 | -100.0 | 0.26 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | both | 2-2 | 50.0 | 55.8 | -5.8 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 25.8 | 24.2 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 25.8 | 24.2 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | both | 1-2 | 33.3 | 25.8 | 7.6 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.4 | -51.4 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 51.0 | -51.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-1 | 66.7 | 49.7 | 17.0 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 25.8 | 74.2 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 25.8 | 74.2 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 25.8 | 74.2 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 2-0 | 100.0 | 25.8 | 74.2 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| pin_move | moneyline | 2-3 | 40.0 | 45.2 | -5.2 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-4 | 20.0 | 49.6 | -29.6 | -3.09 | -61.8 | 0.4 | 40.0 | keep collecting (5/30) |
| pin_move | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.14 | -3.5 | 0.25 | 50.0 | keep collecting (4/30) |
| money_delta | moneyline | 2-3 | 40.0 | 25.8 | 14.2 | +1.34 | 26.8 | -1.74 | 40.0 | keep collecting (5/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 7-1 | 87.5 | 50.5 | 37.0 | +5.26 | 65.8 | 0.25 | 12.5 | keep collecting (8/30) |
| pin_rlm | moneyline | 1-2 | 33.3 | 25.8 | 7.6 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | moneyline | 188-123 | 60.5 | 57.4 | 3.1 | -26.74 | -8.6 | 0.23 | 46.6 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 127-135 | 48.5 | 49.7 | -1.3 | -18.11 | -6.9 | 0.03 | 34.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | total | 144-134 | 51.8 | 49.9 | 1.9 | -2.51 | -0.9 | 0.37 | 45.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | moneyline | 12-10 | 54.5 | 25.8 | 28.8 | +11.57 | 52.6 | 0.39 | 59.1 | keep collecting (22/30) |
| rlm_ratio | spread | 3-2 | 60.0 | 51.1 | 8.9 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 10-4 | 71.4 | 50.7 | 20.7 | +5.22 | 37.3 | 0.64 | 57.1 | keep collecting (14/30) |
| money_level | moneyline | 93-36 | 72.1 | 69.3 | 2.8 | -5.69 | -4.4 | -0.16 | 45.7 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-16 | 51.5 | 49.4 | 2.1 | -0.69 | -2.1 | 0.85 | 48.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | total | 52-48 | 52.0 | 49.6 | 2.4 | -0.74 | -0.7 | -0.29 | 28.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 57-59 | 49.1 | 46.2 | 2.9 | -0.32 | -0.3 | 0.26 | 49.1 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | spread | 20-14 | 58.8 | 49.8 | 9.0 | +4.0 | 11.8 | 0.65 | 38.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 58-40 | 59.2 | 50.2 | 9.0 | +12.86 | 13.1 | 0.05 | 36.7 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | moneyline | 42-38 | 52.5 | 53.6 | -1.1 | -10.85 | -13.6 | -0.14 | 48.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | spread | 18-4 | 81.8 | 49.3 | 32.5 | +12.18 | 55.3 | 0.23 | 40.9 | keep collecting (22/30) |
| money_moving | total | 39-29 | 57.4 | 50.0 | 7.4 | +6.46 | 9.5 | 0.25 | 36.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | moneyline | 2-6 | 25.0 | 31.8 | -6.8 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| pin_value | spread | 24-20 | 54.5 | 49.6 | 5.0 | +1.16 | 2.6 | 0.25 | 38.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 23-22 | 51.1 | 49.9 | 1.2 | -1.28 | -2.9 | -0.02 | 35.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 51.9 | -18.5 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 87-161 | 35.1 | 44.1 | -9.1 | -49.06 | -19.8 | 0.13 | 42.3 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 63-57 | 52.5 | 49.3 | 3.2 | -1.92 | -1.6 | 0.35 | 40.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap | total | 65-64 | 50.4 | 49.9 | 0.5 | -5.69 | -4.4 | 0.91 | 55.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | moneyline | 44-18 | 71.0 | 64.1 | 6.9 | -1.02 | -1.6 | 0.07 | 54.8 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+follow_move | moneyline | 10-21 | 32.3 | 53.9 | -21.6 | -14.52 | -46.9 | 0.26 | 58.1 | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 31.8 | -6.8 | -4.31 | -53.8 | -0.08 | 50.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 41.9 | -8.6 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| money_level+money_moving | moneyline | 29-12 | 70.7 | 70.7 | 0.1 | -4.0 | -9.8 | -0.54 | 53.7 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+sharp_gap | moneyline | 14-35 | 28.6 | 42.6 | -14.0 | -10.86 | -22.2 | 0.93 | 51.0 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | moneyline | 55-15 | 78.6 | 69.4 | 9.2 | -0.93 | -1.3 | -0.1 | 48.6 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 26-11 | 70.3 | 57.2 | 13.1 | +3.47 | 9.4 | 0.3 | 59.5 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 22-18 | 55.0 | 70.6 | -15.6 | -8.38 | -21.0 | 0.07 | 47.5 | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+sharp_gap | moneyline | 33-17 | 66.0 | 50.0 | 16.0 | +7.74 | 15.5 | 0.27 | 56.0 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 21-24 | 46.7 | 47.3 | -0.6 | -5.63 | -12.5 | -0.05 | 53.3 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | moneyline | 8-21 | 27.6 | 45.8 | -18.2 | -12.26 | -42.3 | 0.24 | 48.3 | keep collecting (29/30) |
| follow_move+rlm_ratio | moneyline | 12-10 | 54.5 | 25.8 | 28.8 | +11.57 | 52.6 | 0.39 | 59.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 12-10 | 54.5 | 25.8 | 28.8 | +11.57 | 52.6 | 0.39 | 59.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 25.8 | -0.8 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | moneyline | 4-3 | 57.1 | 25.8 | 31.4 | +4.22 | 60.3 | 0.27 | 57.1 | keep collecting (7/30) |
| money_delta+money_moving | moneyline | 2-3 | 40.0 | 25.8 | 14.2 | +1.34 | 26.8 | -1.74 | 40.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-3 | 40.0 | 25.8 | 14.2 | +1.34 | 26.8 | -1.74 | 40.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 41.9 | -41.9 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-1 | 66.7 | 58.1 | 8.6 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | moneyline | 2-1 | 66.7 | 58.1 | 8.6 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-1 | 50.0 | 25.8 | 24.2 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-1 | 50.0 | 25.8 | 24.2 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | moneyline | 1-2 | 33.3 | 25.8 | 7.6 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.13 | 56.5 | -0.1 | 50.0 | keep collecting (2/30) |
| money_level+rlm_ratio | moneyline | 4-3 | 57.1 | 25.8 | 31.4 | +1.87 | 26.7 | 2.0 | 85.7 | keep collecting (7/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 25.8 | 74.2 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 1-0 | 100.0 | 25.8 | 74.2 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 1-0 | 100.0 | 25.8 | 74.2 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 25.8 | 40.9 | +3.34 | 111.3 | -1.53 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 25.8 | 74.2 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 25.8 | -25.8 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-0 | 100.0 | 25.8 | 74.2 | +1.64 | 164.0 | 3.8 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-5 | 50.0 | 48.1 | 1.9 | -0.68 | -6.8 | 1.7 | 70.0 | keep collecting (10/30) |
| consensus_gap+money_moving | spread | 5-0 | 100.0 | 48.1 | 51.9 | +4.32 | 86.3 | 0.6 | 40.0 | keep collecting (5/30) |
| consensus_gap+pin_value | spread | 10-8 | 55.6 | 49.0 | 6.6 | +0.6 | 3.3 | 0.5 | 50.0 | keep collecting (18/30) |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.1 | 8.9 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 49.1 | 13.4 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 10-4 | 71.4 | 48.9 | 22.5 | +5.12 | 36.6 | 0.86 | 64.3 | keep collecting (14/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 49.2 | -6.3 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 51.1 | 8.9 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 51.9 | -51.9 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 51.9 | -51.9 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-11 | 56.0 | 49.3 | 6.7 | +1.62 | 6.5 | 1.0 | 44.0 | keep collecting (25/30) |
| money_moving+sharp_gap | spread | 10-3 | 76.9 | 49.3 | 27.6 | +6.04 | 46.4 | 0.54 | 46.2 | keep collecting (13/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.4 | 17.3 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-9 | 50.0 | 48.8 | 1.2 | -1.2 | -6.7 | 0.89 | 44.4 | keep collecting (18/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 48.1 | 14.4 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 11-8 | 57.9 | 48.9 | 9.0 | +2.04 | 10.7 | 0.63 | 42.1 | keep collecting (19/30) |
| follow_move+pin_value | spread | 12-7 | 63.2 | 49.1 | 14.0 | +3.45 | 18.2 | 0.26 | 31.6 | keep collecting (19/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 48.1 | 51.9 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 48.1 | 51.9 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-1 | 90.0 | 48.5 | 41.5 | +7.22 | 72.2 | 0.2 | 40.0 | keep collecting (10/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 51.9 | 14.8 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | spread | 1-3 | 25.0 | 49.1 | -24.1 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 48.1 | -48.1 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-2 | 33.3 | 48.1 | -14.8 | -1.09 | -36.4 | 0.33 | 33.3 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 51.9 | -51.9 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 24-19 | 55.8 | 49.7 | 6.1 | +2.92 | 6.8 | -0.05 | 34.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | total | 36-28 | 56.2 | 49.8 | 6.4 | +4.78 | 7.5 | -0.16 | 31.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | total | 27-16 | 62.8 | 50.2 | 12.6 | +8.55 | 19.9 | 0.26 | 37.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 49.0 | -49.0 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 8-5 | 61.5 | 50.4 | 11.2 | +2.23 | 17.2 | 0.23 | 30.8 | keep collecting (13/30) |
| money_moving+pin_value | total | 5-3 | 62.5 | 50.3 | 12.2 | +1.47 | 18.3 | 0.12 | 25.0 | keep collecting (8/30) |
| pin_value+sharp_gap | total | 11-6 | 64.7 | 50.2 | 14.5 | +3.92 | 23.1 | -0.06 | 29.4 | keep collecting (17/30) |
| follow_move+money_level | total | 20-18 | 52.6 | 49.6 | 3.1 | +0.17 | 0.4 | 0.16 | 36.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.8 | -3.1 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 10-4 | 71.4 | 50.7 | 20.7 | +5.22 | 37.3 | 0.64 | 57.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 25-13 | 65.8 | 50.1 | 15.7 | +9.78 | 25.7 | 0.37 | 42.1 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 5-2 | 71.4 | 50.7 | 20.7 | +2.63 | 37.6 | 0.86 | 57.1 | keep collecting (7/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 50.3 | 16.3 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 10-4 | 71.4 | 50.7 | 20.7 | +5.22 | 37.3 | 0.64 | 57.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 15-13 | 53.6 | 50.0 | 3.6 | +0.7 | 2.5 | 0.57 | 50.0 | keep collecting (28/30) |
| consensus_gap+money_level | total | 4-3 | 57.1 | 49.6 | 7.6 | +0.53 | 7.5 | -0.43 | 14.3 | keep collecting (7/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 49.4 | 30.6 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 49.8 | -16.4 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 5-6 | 45.5 | 50.3 | -4.8 | -1.49 | -13.5 | 0.0 | 27.3 | keep collecting (11/30) |
| money_moving+rlm_ratio | total | 5-3 | 62.5 | 50.5 | 12.0 | +1.63 | 20.4 | 0.38 | 50.0 | keep collecting (8/30) |
| consensus_gap+follow_move | total | 11-8 | 57.9 | 49.8 | 8.1 | +1.97 | 10.4 | 1.58 | 68.4 | keep collecting (19/30) |
| consensus_gap+money_delta | total | 2-0 | 100.0 | 49.0 | 51.0 | +1.78 | 88.9 | 0.0 | 0.0 | keep collecting (2/30) |
| follow_move+money_delta | total | 2-1 | 66.7 | 50.3 | 16.3 | +0.78 | 26.0 | 1.0 | 33.3 | keep collecting (3/30) |
| money_delta+money_moving | total | 6-1 | 85.7 | 50.4 | 35.3 | +4.35 | 62.2 | 0.29 | 14.3 | keep collecting (7/30) |
| money_delta+pin_value | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 | -0.5 | 0.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 5-0 | 100.0 | 50.2 | 49.8 | +4.44 | 88.9 | 0.4 | 20.0 | keep collecting (5/30) |
| follow_move+pin_move | total | 2-0 | 100.0 | 51.0 | 49.0 | +1.86 | 93.0 | 1.0 | 100.0 | keep collecting (2/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 51.0 | -51.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 51.0 | -51.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.82 | 90.9 | -0.5 | 0.0 | keep collecting (2/30) |
| consensus_gap+rlm_ratio | total | 2-1 | 66.7 | 51.0 | 15.7 | +0.86 | 28.7 | 0.67 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | total | 0-1 | 0.0 | 49.0 | -49.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_value | total | 0-1 | 0.0 | 49.0 | -49.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 49.0 | -49.0 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |

## CLOSE  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_move | both | 463-468 | 49.7 | 50.0 | -0.2 | -33.55 | -3.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta | both | 300-395 | 43.2 | 43.9 | -0.7 | -50.01 | -7.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm | both | 130-148 | 46.8 | 42.0 | 4.8 | +28.34 | 10.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | both | 812-724 | 52.9 | 52.0 | 0.8 | -88.05 | -5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | both | 190-212 | 47.3 | 44.4 | 2.9 | +4.06 | 1.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level | both | 1021-756 | 57.5 | 55.8 | 1.7 | -65.35 | -3.7 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 793-922 | 46.2 | 47.4 | -1.2 | -115.28 | -6.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | both | 793-924 | 46.2 | 47.7 | -1.5 | -125.73 | -7.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | both | 330-345 | 48.9 | 47.6 | 1.3 | -3.24 | -0.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 50.6 | 16.0 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 319-438 | 42.1 | 46.7 | -4.5 | -86.13 | -11.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+follow_move | both | 122-124 | 49.6 | 50.9 | -1.3 | -16.61 | -6.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | both | 143-237 | 37.6 | 43.9 | -6.3 | -30.18 | -7.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_move | both | 74-79 | 48.4 | 50.4 | -2.1 | +0.94 | 0.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | both | 23-39 | 37.1 | 36.7 | 0.4 | +10.03 | 16.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_value | both | 125-144 | 46.5 | 44.9 | 1.5 | -0.47 | -0.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | both | 25-43 | 36.8 | 39.2 | -2.4 | -1.66 | -2.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | both | 142-241 | 37.1 | 43.3 | -6.2 | -31.16 | -8.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_moving | both | 437-467 | 48.3 | 49.5 | -1.1 | -65.29 | -7.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_move | both | 333-334 | 49.9 | 50.3 | -0.4 | -32.11 | -4.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_rlm | both | 102-104 | 49.5 | 44.2 | 5.3 | +8.93 | 4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | both | 114-111 | 50.7 | 48.7 | 1.9 | -9.32 | -4.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | both | 190-212 | 47.3 | 44.4 | 2.9 | +4.06 | 1.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 442-463 | 48.8 | 49.3 | -0.4 | -54.18 | -6.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_move | both | 279-311 | 47.3 | 48.6 | -1.4 | -27.9 | -4.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_rlm | both | 124-145 | 46.1 | 41.9 | 4.2 | +25.38 | 9.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_value | both | 144-174 | 45.3 | 46.7 | -1.5 | -14.54 | -4.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | both | 182-206 | 46.9 | 44.5 | 2.4 | +2.15 | 0.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+sharp_gap | both | 760-887 | 46.1 | 47.5 | -1.3 | -108.96 | -6.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_rlm | both | 121-121 | 50.0 | 44.2 | 5.8 | +24.68 | 10.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_value | both | 145-148 | 49.5 | 48.9 | 0.6 | -7.5 | -2.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_ratio | both | 111-102 | 52.1 | 45.6 | 6.5 | +18.59 | 8.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | both | 285-311 | 47.8 | 48.5 | -0.7 | -22.61 | -3.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+pin_value | both | 38-37 | 50.7 | 45.2 | 5.5 | +14.72 | 19.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_ratio | both | 102-104 | 49.5 | 44.2 | 5.3 | +8.93 | 4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | both | 130-148 | 46.8 | 42.0 | 4.8 | +28.34 | 10.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 36-28 | 56.2 | 48.6 | 7.6 | +4.83 | 7.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | both | 147-175 | 45.7 | 46.7 | -1.0 | -12.87 | -4.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio+sharp_gap | both | 190-212 | 47.3 | 44.4 | 2.9 | +4.06 | 1.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 145-166 | 46.6 | 45.9 | 0.7 | -18.13 | -5.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+money_moving | both | 563-505 | 52.7 | 52.5 | 0.2 | -46.63 | -4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | both | 556-497 | 52.8 | 52.3 | 0.5 | -38.39 | -3.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | both | 541-383 | 58.5 | 56.8 | 1.7 | -43.12 | -4.7 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 93-79 | 54.1 | 48.7 | 5.4 | +10.79 | 6.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | both | 193-157 | 55.1 | 58.0 | -2.9 | -22.36 | -6.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | both | 272-257 | 51.4 | 53.2 | -1.8 | -35.08 | -6.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | both | 156-152 | 50.6 | 49.6 | 1.0 | -16.52 | -5.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_moving | both | 215-309 | 41.0 | 42.3 | -1.3 | -42.21 | -8.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_delta | both | 41-108 | 27.5 | 36.2 | -8.7 | -29.68 | -19.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_level | both | 112-104 | 51.9 | 47.2 | 4.7 | +13.89 | 6.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | both | 67-68 | 49.6 | 46.7 | 2.9 | -3.48 | -2.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+sharp_gap | both | 212-304 | 41.1 | 42.4 | -1.3 | -40.38 | -7.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 50.6 | 16.0 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 110-129 | 46.0 | 46.3 | -0.2 | -9.78 | -4.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_rlm | both | 59-42 | 58.4 | 46.8 | 11.6 | +16.5 | 16.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_rlm | both | 75-89 | 45.7 | 42.0 | 3.7 | +8.34 | 5.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+rlm_ratio | both | 107-109 | 49.5 | 44.9 | 4.6 | +4.1 | 1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 51.0 | 49.0 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_move | moneyline | 97-94 | 50.8 | 49.1 | 1.7 | +6.55 | 3.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move | spread | 182-195 | 48.3 | 50.2 | -1.9 | -29.11 | -7.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move | total | 184-179 | 50.7 | 50.2 | 0.4 | -10.99 | -3.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | moneyline | 43-158 | 21.4 | 27.5 | -6.1 | -47.37 | -23.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta | spread | 115-117 | 49.6 | 50.6 | -1.1 | -12.53 | -5.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | total | 142-120 | 54.2 | 50.5 | 3.7 | +9.89 | 3.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm | moneyline | 34-71 | 32.4 | 27.6 | 4.8 | +17.57 | 16.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm | spread | 24-21 | 53.3 | 50.7 | 2.6 | +0.88 | 2.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm | total | 72-56 | 56.2 | 50.6 | 5.6 | +9.89 | 7.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | moneyline | 295-193 | 60.5 | 56.8 | 3.7 | -27.7 | -5.7 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 237-246 | 49.1 | 49.6 | -0.5 | -30.83 | -6.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | total | 280-285 | 49.6 | 50.0 | -0.5 | -29.52 | -5.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | moneyline | 34-80 | 29.8 | 29.2 | 0.6 | -6.42 | -5.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio | spread | 41-41 | 50.0 | 50.1 | -0.1 | -3.76 | -4.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | total | 115-91 | 55.8 | 50.5 | 5.3 | +14.24 | 6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | moneyline | 398-140 | 74.0 | 70.1 | 3.9 | -13.61 | -2.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 297-309 | 49.0 | 49.4 | -0.4 | -41.15 | -6.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level | total | 326-307 | 51.5 | 49.8 | 1.7 | -10.59 | -1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 182-312 | 36.8 | 41.2 | -4.3 | -59.79 | -12.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| sharp_gap | spread | 305-295 | 50.8 | 49.7 | 1.2 | -19.83 | -3.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 306-315 | 49.3 | 50.2 | -0.9 | -35.66 | -5.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | moneyline | 190-302 | 38.6 | 42.3 | -3.7 | -50.75 | -10.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | spread | 302-298 | 50.3 | 49.6 | 0.7 | -25.7 | -4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | total | 301-324 | 48.2 | 50.2 | -2.0 | -49.28 | -7.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | moneyline | 17-53 | 24.3 | 28.5 | -4.3 | +11.19 | 16.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | spread | 150-140 | 51.7 | 49.7 | 2.0 | -9.12 | -3.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 163-152 | 51.7 | 49.8 | 1.9 | -5.31 | -1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 51.9 | 48.1 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 136-264 | 34.0 | 44.2 | -10.2 | -71.68 | -17.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 84-73 | 53.5 | 49.3 | 4.2 | -1.4 | -0.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap | total | 99-101 | 49.5 | 49.5 | 0.0 | -13.04 | -6.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | moneyline | 134-75 | 64.1 | 64.3 | -0.1 | -5.04 | -2.4 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 125-73 | 63.1 | 63.7 | -0.6 | -4.65 | -2.3 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 168-288 | 36.8 | 41.1 | -4.2 | -47.03 | -10.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+follow_move | moneyline | 50-64 | 43.9 | 53.0 | -9.1 | -19.13 | -16.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | moneyline | 93-58 | 61.6 | 69.7 | -8.1 | -10.37 | -6.9 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 53-150 | 26.1 | 39.1 | -13.0 | -21.34 | -10.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | moneyline | 235-71 | 76.8 | 71.5 | 5.3 | -8.61 | -2.8 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 94-107 | 46.8 | 48.2 | -1.4 | -16.72 | -8.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_moving | moneyline | 40-142 | 22.0 | 27.1 | -5.1 | -34.34 | -18.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+sharp_gap | moneyline | 38-141 | 21.2 | 27.1 | -5.9 | -35.53 | -19.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 51-155 | 24.8 | 38.0 | -13.2 | -24.22 | -11.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+sharp_gap | moneyline | 91-106 | 46.2 | 47.2 | -1.0 | -16.14 | -8.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_move | moneyline | 26-31 | 45.6 | 52.1 | -6.5 | +7.23 | 12.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 10-28 | 26.3 | 28.3 | -2.0 | +9.65 | 25.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 4-30 | 11.8 | 28.6 | -16.9 | -7.04 | -20.7 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 78-63 | 55.3 | 51.2 | 4.1 | +6.21 | 4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_rlm | moneyline | 22-39 | 36.1 | 29.0 | 7.1 | +0.5 | 0.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 34-80 | 29.8 | 29.2 | 0.6 | -6.42 | -5.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 41-60 | 40.6 | 41.6 | -1.0 | +6.36 | 6.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_rlm | moneyline | 33-69 | 32.4 | 27.7 | 4.7 | +18.17 | 17.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 33-76 | 30.3 | 29.3 | 0.9 | -3.82 | -3.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_rlm | moneyline | 25-44 | 36.2 | 27.9 | 8.3 | +13.91 | 20.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 20-30 | 40.0 | 29.7 | 10.3 | +7.3 | 14.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+sharp_gap | moneyline | 41-61 | 40.2 | 41.0 | -0.8 | +5.18 | 5.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 22-39 | 36.1 | 29.0 | 7.1 | +0.5 | 0.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 34-71 | 32.4 | 27.6 | 4.8 | +17.57 | 16.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 34-80 | 29.8 | 29.2 | 0.6 | -6.42 | -5.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 11-80 | 12.1 | 27.4 | -15.3 | -27.62 | -30.3 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 13-44 | 22.8 | 28.3 | -5.5 | +2.38 | 4.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_move | moneyline | 15-35 | 30.0 | 29.7 | 0.3 | -2.46 | -4.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_rlm | moneyline | 19-44 | 30.2 | 28.1 | 2.1 | +2.21 | 3.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_value | moneyline | 2-18 | 10.0 | 25.8 | -15.8 | -11.18 | -55.9 |  |  | keep collecting (20/30) |
| money_moving+pin_value | moneyline | 9-32 | 22.0 | 27.0 | -5.0 | +8.76 | 21.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_value | moneyline | 5-9 | 35.7 | 29.2 | 6.5 | +6.58 | 47.0 |  |  | keep collecting (14/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 25.8 | 5.5 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 9-34 | 20.9 | 26.9 | -6.0 | +6.76 | 15.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_delta | moneyline | 22-46 | 32.4 | 30.1 | 2.3 | -10.07 | -14.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_level | moneyline | 13-20 | 39.4 | 30.2 | 9.2 | +8.09 | 24.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+rlm_ratio | moneyline | 20-38 | 34.5 | 30.0 | 4.5 | -3.98 | -6.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_move | moneyline | 63-37 | 63.0 | 67.4 | -4.4 | -4.79 | -4.8 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 10-9 | 52.6 | 30.9 | 21.8 | +4.79 | 25.2 |  |  | keep collecting (19/30) |
| money_level+rlm_ratio | moneyline | 12-11 | 52.2 | 38.4 | 13.8 | +5.12 | 22.2 |  |  | keep collecting (23/30) |
| money_level+pin_value | moneyline | 4-1 | 80.0 | 64.5 | 15.5 | +1.0 | 19.9 |  |  | keep collecting (5/30) |
| follow_move+pin_value | moneyline | 1-7 | 12.5 | 25.8 | -13.3 | -5.48 | -68.5 |  |  | keep collecting (8/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 25.8 | -0.8 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 34-27 | 55.7 | 48.8 | 6.9 | +1.9 | 3.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | spread | 46-41 | 52.9 | 49.2 | 3.7 | -1.84 | -2.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_move | spread | 24-27 | 47.1 | 49.3 | -2.2 | -6.56 | -12.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 58-43 | 57.4 | 49.3 | 8.1 | +6.24 | 6.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_ratio | spread | 4-4 | 50.0 | 50.0 | 0.0 | -0.67 | -8.3 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | spread | 45-41 | 52.3 | 49.3 | 3.0 | -2.73 | -3.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | spread | 153-154 | 49.8 | 49.4 | 0.5 | -15.75 | -5.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_move | spread | 116-128 | 47.5 | 49.9 | -2.4 | -22.33 | -9.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_rlm | spread | 19-17 | 52.8 | 50.5 | 2.3 | +0.35 | 1.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | spread | 54-45 | 54.5 | 49.2 | 5.4 | +2.06 | 2.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | spread | 41-41 | 50.0 | 50.1 | -0.1 | -3.76 | -4.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 154-153 | 50.2 | 49.4 | 0.7 | -13.61 | -4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_move | spread | 110-119 | 48.0 | 49.8 | -1.8 | -19.2 | -8.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | spread | 22-21 | 51.2 | 50.7 | 0.5 | -0.95 | -2.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | spread | 73-73 | 50.0 | 49.4 | 0.6 | -10.1 | -6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_ratio | spread | 39-40 | 49.4 | 50.0 | -0.7 | -4.69 | -5.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | spread | 297-290 | 50.6 | 49.6 | 1.0 | -22.21 | -3.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_rlm | spread | 24-21 | 53.3 | 50.7 | 2.6 | +0.88 | 2.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 68-75 | 47.6 | 49.8 | -2.2 | -15.02 | -10.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_ratio | spread | 22-23 | 48.9 | 50.4 | -1.5 | -2.94 | -6.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | spread | 113-119 | 48.7 | 49.9 | -1.1 | -16.47 | -7.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+pin_value | spread | 6-9 | 40.0 | 50.4 | -10.4 | -3.79 | -25.3 |  |  | keep collecting (15/30) |
| pin_rlm+rlm_ratio | spread | 19-17 | 52.8 | 50.5 | 2.3 | +0.35 | 1.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | spread | 24-21 | 53.3 | 50.7 | 2.6 | +0.88 | 2.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 7-6 | 53.8 | 49.3 | 4.6 | -0.01 | -0.1 |  |  | keep collecting (13/30) |
| pin_value+sharp_gap | spread | 73-73 | 50.0 | 49.4 | 0.6 | -10.16 | -7.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | spread | 41-41 | 50.0 | 50.1 | -0.1 | -3.76 | -4.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 147-155 | 48.7 | 49.2 | -0.5 | -22.16 | -7.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+rlm_ratio | spread | 21-26 | 44.7 | 49.8 | -5.1 | -7.13 | -15.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | spread | 233-230 | 50.3 | 49.4 | 0.9 | -20.17 | -4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | spread | 55-45 | 55.0 | 49.0 | 6.0 | +2.02 | 2.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | spread | 232-231 | 50.1 | 49.4 | 0.7 | -22.09 | -4.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | spread | 100-120 | 45.5 | 49.6 | -4.2 | -29.69 | -13.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_value | spread | 80-81 | 49.7 | 49.2 | 0.5 | -12.08 | -7.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_delta | spread | 14-14 | 50.0 | 50.4 | -0.4 | -2.09 | -7.5 |  |  | keep collecting (28/30) |
| follow_move+money_delta | spread | 35-43 | 44.9 | 50.0 | -5.2 | -11.49 | -14.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_level | spread | 38-38 | 50.0 | 50.0 | 0.0 | -3.77 | -5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_moving | spread | 66-70 | 48.5 | 50.4 | -1.8 | -10.46 | -7.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | spread | 31-24 | 56.4 | 50.4 | 6.0 | +2.97 | 5.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+sharp_gap | spread | 65-68 | 48.9 | 50.3 | -1.5 | -9.44 | -7.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_rlm | spread | 13-9 | 59.1 | 50.2 | 8.9 | +2.67 | 12.1 |  |  | keep collecting (22/30) |
| money_delta+rlm_ratio | spread | 16-24 | 40.0 | 49.9 | -9.9 | -9.78 | -24.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 51.9 | 48.1 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_move | spread | 32-40 | 44.4 | 50.7 | -6.2 | -10.87 | -15.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_rlm | spread | 12-14 | 46.2 | 50.4 | -4.3 | -3.22 | -12.4 |  |  | keep collecting (26/30) |
| follow_move+money_delta | total | 88-77 | 53.3 | 50.5 | 2.9 | +3.42 | 2.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | total | 197-199 | 49.7 | 50.0 | -0.3 | -19.51 | -4.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | total | 198-194 | 50.5 | 50.0 | 0.5 | -13.57 | -3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | total | 295-309 | 48.8 | 50.2 | -1.4 | -39.73 | -6.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | total | 45-54 | 45.5 | 49.3 | -3.8 | -14.01 | -14.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_move | total | 24-21 | 53.3 | 49.6 | 3.8 | +0.27 | 0.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_value | total | 54-57 | 48.6 | 49.5 | -0.8 | -9.09 | -8.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | total | 190-206 | 48.0 | 50.2 | -2.2 | -32.83 | -8.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+sharp_gap | total | 197-204 | 49.1 | 50.2 | -1.0 | -24.43 | -6.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | total | 109-100 | 52.2 | 50.1 | 2.1 | -0.6 | -0.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | total | 72-70 | 50.7 | 49.6 | 1.1 | -5.44 | -3.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_value | total | 72-64 | 52.9 | 50.0 | 2.9 | +0.94 | 0.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_move | total | 128-132 | 49.2 | 50.3 | -1.1 | -15.07 | -5.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_moving | total | 109-97 | 52.9 | 50.5 | 2.4 | +2.59 | 1.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | total | 159-157 | 50.3 | 49.9 | 0.5 | -12.35 | -3.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 59-59 | 50.0 | 49.9 | 0.1 | -5.9 | -5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | total | 62-69 | 47.3 | 50.0 | -2.7 | -13.2 | -10.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | total | 65-68 | 48.9 | 50.0 | -1.2 | -9.46 | -7.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | total | 44-46 | 48.9 | 49.5 | -0.6 | -6.99 | -7.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+sharp_gap | total | 46-45 | 50.5 | 49.6 | 1.0 | -4.21 | -4.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+follow_move | total | 38-33 | 53.5 | 49.4 | 4.1 | +0.61 | 0.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_delta | total | 16-14 | 53.3 | 49.9 | 3.5 | +0.03 | 0.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+sharp_gap | total | 109-95 | 53.4 | 50.5 | 2.9 | +4.59 | 2.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 61-46 | 57.0 | 50.4 | 6.6 | +9.58 | 9.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_move | total | 63-54 | 53.8 | 50.6 | 3.2 | +3.55 | 3.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | total | 131-131 | 50.0 | 50.3 | -0.3 | -11.33 | -4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_move | total | 139-143 | 49.3 | 50.2 | -0.9 | -15.98 | -5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | total | 10-8 | 55.6 | 49.9 | 5.7 | +0.87 | 4.8 |  |  | keep collecting (18/30) |
| consensus_gap+rlm_ratio | total | 17-9 | 65.4 | 49.7 | 15.7 | +6.04 | 23.2 |  |  | keep collecting (26/30) |
| follow_move+pin_rlm | total | 61-48 | 56.0 | 50.6 | 5.3 | +8.07 | 7.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | total | 115-91 | 55.8 | 50.5 | 5.3 | +14.24 | 6.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 36-24 | 60.0 | 50.7 | 9.3 | +9.04 | 15.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+rlm_ratio | total | 60-42 | 58.8 | 50.4 | 8.4 | +12.81 | 12.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | total | 69-55 | 55.6 | 50.7 | 5.0 | +8.15 | 6.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_ratio | total | 110-90 | 55.0 | 50.5 | 4.5 | +10.66 | 5.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_rlm | total | 72-56 | 56.2 | 50.6 | 5.6 | +9.89 | 7.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 69-49 | 58.5 | 50.6 | 7.9 | +14.24 | 12.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+pin_value | total | 27-17 | 61.4 | 50.5 | 10.9 | +7.44 | 16.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_ratio | total | 61-48 | 56.0 | 50.6 | 5.3 | +8.07 | 7.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | total | 72-56 | 56.2 | 50.6 | 5.6 | +9.89 | 7.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 28-19 | 59.6 | 50.4 | 9.2 | +6.32 | 13.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | total | 115-91 | 55.8 | 50.5 | 5.3 | +14.24 | 6.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 44-31 | 58.7 | 50.7 | 7.9 | +9.34 | 12.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+rlm_ratio | total | 71-47 | 60.2 | 50.6 | 9.6 | +17.86 | 15.1 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_delta+pin_value | total | 34-26 | 56.7 | 50.4 | 6.3 | +4.73 | 7.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 51.0 | 49.0 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

# Pooled (fit + forward together)

Kept for continuity. **Contaminated** — it mixes the games the engine was built
on with the games testing it. Use the forward table for any decision.

## EARLY  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_move | both | 5-9 | 35.7 | 48.1 | -12.4 | -5.1 | -36.4 | 0.22 | 50.0 | keep collecting (14/30) |
| money_delta | both | 10-7 | 58.8 | 41.7 | 17.1 | +4.43 | 26.1 | -0.22 | 29.4 | keep collecting (17/30) |
| pin_rlm | both | 1-2 | 33.3 | 25.9 | 7.4 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | both | 469-401 | 53.9 | 52.5 | 1.4 | -47.57 | -5.5 | 0.22 | 42.3 | no edge shown yet |
| rlm_ratio | both | 29-18 | 61.7 | 38.0 | 23.7 | +19.54 | 41.6 | 0.4 | 51.1 | no edge shown yet |
| money_level | both | 169-108 | 61.0 | 59.3 | 1.7 | -10.5 | -3.8 | -0.09 | 39.7 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 143-119 | 54.6 | 48.4 | 6.2 | +20.09 | 7.7 | 0.26 | 43.1 | no edge shown yet |
| money_moving | both | 102-81 | 55.7 | 51.4 | 4.4 | +0.19 | 0.1 | 0.01 | 41.5 | no edge shown yet |
| pin_value | both | 49-48 | 50.5 | 48.3 | 2.2 | -4.43 | -4.6 | 0.1 | 38.1 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.1 | -31.1 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 218-285 | 43.3 | 47.1 | -3.7 | -57.9 | -11.5 | 0.39 | 45.3 | DROP: below break-even |
| consensus_gap+money_level | both | 33-28 | 54.1 | 64.2 | -10.1 | -9.61 | -15.8 | 0.35 | 49.2 | no edge shown yet |
| consensus_gap+money_moving | both | 17-23 | 42.5 | 46.7 | -4.2 | -6.42 | -16.1 | 0.25 | 42.5 | no edge shown yet |
| consensus_gap+pin_value | both | 19-28 | 40.4 | 46.5 | -6.0 | -11.54 | -24.5 | 0.39 | 48.9 | DROP: below break-even |
| follow_move+rlm_ratio | both | 29-18 | 61.7 | 38.0 | 23.7 | +19.54 | 41.6 | 0.4 | 51.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 75-38 | 66.4 | 49.9 | 16.5 | +24.31 | 21.5 | 0.37 | 47.8 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 64-40 | 61.5 | 58.3 | 3.2 | -0.87 | -0.8 | -0.16 | 47.1 | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_value | both | 11-9 | 55.0 | 49.9 | 5.1 | +0.81 | 4.0 | 0.4 | 45.0 | keep collecting (20/30) |
| money_moving+pin_value | both | 8-5 | 61.5 | 49.9 | 11.6 | +2.04 | 15.7 | 0.31 | 38.5 | keep collecting (13/30) |
| rlm_ratio+sharp_gap | both | 29-18 | 61.7 | 38.0 | 23.7 | +19.54 | 41.6 | 0.4 | 51.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 97-59 | 62.2 | 55.9 | 6.3 | +5.17 | 3.3 | 0.14 | 43.6 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 60-47 | 56.1 | 48.8 | 7.2 | +6.0 | 5.6 | 0.13 | 43.9 | no edge shown yet |
| money_delta+money_level | both | 3-2 | 60.0 | 45.7 | 14.3 | +1.46 | 29.2 | 1.16 | 60.0 | keep collecting (5/30) |
| money_delta+money_moving | both | 9-7 | 56.2 | 41.1 | 15.1 | +3.53 | 22.0 | -0.23 | 31.2 | keep collecting (16/30) |
| money_delta+pin_value | both | 3-1 | 75.0 | 50.0 | 25.0 | +1.61 | 40.3 | 0.0 | 25.0 | keep collecting (4/30) |
| money_delta+sharp_gap | both | 7-5 | 58.3 | 40.2 | 18.1 | +3.78 | 31.5 | -0.31 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | both | 13-8 | 61.9 | 48.8 | 13.1 | +3.66 | 17.4 | -0.18 | 33.3 | keep collecting (21/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 49.4 | -49.4 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 31-40 | 43.7 | 51.6 | -8.0 | -14.93 | -21.0 | 0.78 | 56.3 | no edge shown yet |
| follow_move+pin_value | both | 20-17 | 54.1 | 48.8 | 5.2 | +0.41 | 1.1 | -0.12 | 29.7 | no edge shown yet |
| consensus_gap+sharp_gap | both | 25-45 | 35.7 | 45.3 | -9.6 | -11.2 | -16.0 | 0.91 | 50.0 | DROP: below break-even |
| follow_move+money_level | both | 90-44 | 67.2 | 60.4 | 6.8 | +0.97 | 0.7 | 0.05 | 44.0 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 11-7 | 61.1 | 41.1 | 20.0 | +4.43 | 24.6 | 1.22 | 61.1 | keep collecting (18/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 44.1 | 5.9 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 53-29 | 64.6 | 53.0 | 11.6 | +9.8 | 12.0 | 0.29 | 51.2 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 3-0 | 100.0 | 49.0 | 51.0 | +2.61 | 87.1 | 0.0 | 0.0 | keep collecting (3/30) |
| follow_move+money_delta | both | 5-3 | 62.5 | 40.9 | 21.6 | +3.95 | 49.4 | 0.05 | 37.5 | keep collecting (8/30) |
| money_moving+rlm_ratio | both | 12-8 | 60.0 | 40.5 | 19.5 | +6.66 | 33.3 | 0.16 | 45.0 | keep collecting (20/30) |
| consensus_gap+rlm_ratio | both | 3-4 | 42.9 | 36.5 | 6.4 | -0.82 | -11.7 | 0.93 | 71.4 | keep collecting (7/30) |
| pin_move+pin_value | both | 1-4 | 20.0 | 49.1 | -29.1 | -3.09 | -61.8 | 0.2 | 20.0 | keep collecting (5/30) |
| follow_move+pin_move | both | 5-3 | 62.5 | 52.5 | 10.0 | +0.9 | 11.2 | 0.42 | 62.5 | keep collecting (8/30) |
| consensus_gap+pin_move | both | 0-5 | 0.0 | 44.4 | -44.4 | -5.0 | -100.0 | 0.26 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | both | 2-2 | 50.0 | 55.9 | -5.9 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | both | 1-2 | 33.3 | 25.9 | 7.4 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.2 | -51.2 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 50.6 | -50.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-1 | 66.7 | 49.8 | 16.9 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 25.9 | 74.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 25.9 | 74.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 25.9 | 74.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 2-1 | 66.7 | 34.1 | 32.5 | +3.34 | 111.3 | 0.87 | 66.7 | keep collecting (3/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| pin_move | moneyline | 2-3 | 40.0 | 45.2 | -5.2 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-4 | 20.0 | 49.6 | -29.6 | -3.09 | -61.8 | 0.4 | 40.0 | keep collecting (5/30) |
| pin_move | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.14 | -3.5 | 0.25 | 50.0 | keep collecting (4/30) |
| money_delta | moneyline | 2-4 | 33.3 | 25.9 | 7.4 | +0.34 | 5.7 | -1.45 | 33.3 | keep collecting (6/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 7-2 | 77.8 | 50.3 | 27.4 | +4.26 | 47.4 | 0.44 | 22.2 | keep collecting (9/30) |
| pin_rlm | moneyline | 1-2 | 33.3 | 25.9 | 7.4 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | moneyline | 193-126 | 60.5 | 57.2 | 3.3 | -25.5 | -8.0 | 0.23 | 46.4 | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 127-140 | 47.6 | 49.7 | -2.2 | -23.11 | -8.7 | 0.03 | 34.5 | DROP: below break-even |
| follow_move | total | 149-135 | 52.5 | 50.0 | 2.5 | +1.04 | 0.4 | 0.37 | 45.1 | no edge shown yet |
| rlm_ratio | moneyline | 13-11 | 54.2 | 25.9 | 28.2 | +11.71 | 48.8 | 0.4 | 58.3 | keep collecting (24/30) |
| rlm_ratio | spread | 3-2 | 60.0 | 51.1 | 8.9 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 13-5 | 72.2 | 50.5 | 21.8 | +6.99 | 38.8 | 0.67 | 55.6 | keep collecting (18/30) |
| money_level | moneyline | 96-39 | 71.1 | 69.4 | 1.7 | -7.68 | -5.7 | -0.19 | 45.2 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-17 | 50.0 | 49.3 | 0.7 | -1.69 | -5.0 | 0.88 | 50.0 | no edge shown yet |
| money_level | total | 56-52 | 51.9 | 49.7 | 2.1 | -1.14 | -1.1 | -0.28 | 29.6 | no edge shown yet |
| sharp_gap | moneyline | 61-61 | 50.0 | 46.4 | 3.6 | +3.59 | 2.9 | 0.27 | 49.2 | no edge shown yet |
| sharp_gap | spread | 20-14 | 58.8 | 49.8 | 9.0 | +4.0 | 11.8 | 0.65 | 38.2 | no edge shown yet |
| sharp_gap | total | 62-44 | 58.5 | 50.1 | 8.4 | +12.5 | 11.8 | 0.13 | 37.7 | no edge shown yet |
| money_moving | moneyline | 44-41 | 51.8 | 53.1 | -1.4 | -12.4 | -14.6 | -0.22 | 45.9 | no edge shown yet |
| money_moving | spread | 18-5 | 78.3 | 49.3 | 29.0 | +11.18 | 48.6 | 0.3 | 43.5 | keep collecting (23/30) |
| money_moving | total | 40-35 | 53.3 | 50.0 | 3.3 | +1.41 | 1.9 | 0.19 | 36.0 | no edge shown yet |
| pin_value | moneyline | 2-6 | 25.0 | 31.9 | -6.9 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| pin_value | spread | 24-20 | 54.5 | 49.6 | 5.0 | +1.16 | 2.6 | 0.25 | 38.6 | no edge shown yet |
| pin_value | total | 23-22 | 51.1 | 50.0 | 1.2 | -1.28 | -2.9 | -0.02 | 35.6 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 51.9 | -18.5 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 89-162 | 35.5 | 44.5 | -9.1 | -49.13 | -19.6 | 0.13 | 42.6 | DROP: below break-even |
| consensus_gap | spread | 64-59 | 52.0 | 49.3 | 2.8 | -3.08 | -2.5 | 0.35 | 40.7 | no edge shown yet |
| consensus_gap | total | 65-64 | 50.4 | 49.9 | 0.5 | -5.69 | -4.4 | 0.91 | 55.0 | no edge shown yet |
| money_level+sharp_gap | moneyline | 46-19 | 70.8 | 64.4 | 6.3 | -1.1 | -1.7 | 0.04 | 53.8 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+follow_move | moneyline | 11-21 | 34.4 | 54.5 | -20.1 | -13.69 | -42.8 | 0.25 | 56.2 | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 31.9 | -6.9 | -4.31 | -53.8 | -0.08 | 50.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 42.0 | -8.6 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| money_level+money_moving | moneyline | 30-13 | 69.8 | 70.7 | -1.0 | -4.91 | -11.4 | -0.67 | 51.2 | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+sharp_gap | moneyline | 15-36 | 29.4 | 43.9 | -14.5 | -11.03 | -21.6 | 0.91 | 51.0 | DROP: below break-even |
| follow_move+money_level | moneyline | 57-16 | 78.1 | 69.5 | 8.6 | -1.01 | -1.4 | -0.18 | 46.6 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 28-13 | 68.3 | 56.5 | 11.8 | +2.92 | 7.1 | 0.07 | 53.7 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 24-19 | 55.8 | 70.7 | -14.9 | -8.46 | -19.7 | 0.12 | 48.8 | no edge shown yet |
| follow_move+sharp_gap | moneyline | 36-18 | 66.7 | 50.0 | 16.7 | +8.81 | 16.3 | 0.23 | 53.7 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 22-25 | 46.8 | 47.4 | -0.6 | -6.54 | -13.9 | -0.11 | 51.1 | no edge shown yet |
| consensus_gap+money_moving | moneyline | 8-21 | 27.6 | 45.8 | -18.3 | -12.26 | -42.3 | 0.24 | 48.3 | keep collecting (29/30) |
| follow_move+rlm_ratio | moneyline | 13-11 | 54.2 | 25.9 | 28.2 | +11.71 | 48.8 | 0.4 | 58.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 13-11 | 54.2 | 25.9 | 28.2 | +11.71 | 48.8 | 0.4 | 58.3 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 25.9 | -0.9 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | moneyline | 4-4 | 50.0 | 25.9 | 24.1 | +3.22 | 40.2 | 0.16 | 50.0 | keep collecting (8/30) |
| money_delta+money_moving | moneyline | 2-4 | 33.3 | 25.9 | 7.4 | +0.34 | 5.7 | -1.45 | 33.3 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-3 | 40.0 | 25.9 | 14.1 | +1.34 | 26.8 | -1.74 | 40.0 | keep collecting (5/30) |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 42.0 | -42.0 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-1 | 66.7 | 58.0 | 8.6 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | moneyline | 2-1 | 66.7 | 58.0 | 8.6 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | moneyline | 1-2 | 33.3 | 25.9 | 7.4 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.13 | 56.5 | -0.1 | 50.0 | keep collecting (2/30) |
| money_level+rlm_ratio | moneyline | 4-3 | 57.1 | 25.9 | 31.2 | +1.87 | 26.7 | 2.0 | 85.7 | keep collecting (7/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 25.9 | 74.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 1-0 | 100.0 | 25.9 | 74.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 1-0 | 100.0 | 25.9 | 74.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 25.9 | 40.7 | +3.34 | 111.3 | -1.53 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 25.9 | 74.1 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-0 | 100.0 | 25.9 | 74.1 | +1.64 | 164.0 | 3.8 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-6 | 45.5 | 48.1 | -2.7 | -1.68 | -15.3 | 1.73 | 72.7 | keep collecting (11/30) |
| consensus_gap+money_moving | spread | 5-1 | 83.3 | 48.1 | 35.2 | +3.32 | 55.3 | 0.83 | 50.0 | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 10-8 | 55.6 | 49.0 | 6.6 | +0.6 | 3.3 | 0.5 | 50.0 | keep collecting (18/30) |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.1 | 8.9 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 49.1 | 13.4 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 10-5 | 66.7 | 48.9 | 17.8 | +4.12 | 27.5 | 0.93 | 66.7 | keep collecting (15/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 49.2 | -6.3 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 51.1 | 8.9 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 51.9 | -51.9 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 51.9 | -51.9 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-11 | 56.0 | 49.3 | 6.7 | +1.62 | 6.5 | 1.0 | 44.0 | keep collecting (25/30) |
| money_moving+sharp_gap | spread | 10-3 | 76.9 | 49.3 | 27.6 | +6.04 | 46.4 | 0.54 | 46.2 | keep collecting (13/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.4 | 17.3 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-11 | 45.0 | 48.7 | -3.7 | -3.2 | -16.0 | 0.85 | 45.0 | keep collecting (20/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 48.1 | 14.4 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 11-9 | 55.0 | 48.9 | 6.1 | +1.04 | 5.2 | 0.7 | 45.0 | keep collecting (20/30) |
| follow_move+pin_value | spread | 12-7 | 63.2 | 49.1 | 14.0 | +3.45 | 18.2 | 0.26 | 31.6 | keep collecting (19/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 48.1 | 51.9 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 48.1 | 51.9 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-2 | 81.8 | 48.5 | 33.3 | +6.22 | 56.6 | 0.36 | 45.5 | keep collecting (11/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 51.9 | 14.8 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | spread | 1-3 | 25.0 | 49.1 | -24.1 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 48.1 | -48.1 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-2 | 33.3 | 48.1 | -14.8 | -1.09 | -36.4 | 0.33 | 33.3 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 51.9 | -51.9 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 24-22 | 52.2 | 49.8 | 2.4 | -0.08 | -0.2 | -0.04 | 37.0 | no edge shown yet |
| money_level+sharp_gap | total | 37-29 | 56.1 | 49.9 | 6.2 | +4.65 | 7.0 | -0.09 | 33.3 | no edge shown yet |
| money_moving+sharp_gap | total | 28-19 | 59.6 | 50.1 | 9.4 | +6.5 | 13.8 | 0.26 | 36.2 | no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 49.4 | -49.4 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 8-5 | 61.5 | 50.2 | 11.3 | +2.23 | 17.2 | 0.23 | 30.8 | keep collecting (13/30) |
| money_moving+pin_value | total | 5-3 | 62.5 | 50.1 | 12.4 | +1.47 | 18.3 | 0.12 | 25.0 | keep collecting (8/30) |
| pin_value+sharp_gap | total | 11-6 | 64.7 | 50.1 | 14.6 | +3.92 | 23.1 | -0.06 | 29.4 | keep collecting (17/30) |
| follow_move+money_level | total | 22-19 | 53.7 | 49.8 | 3.9 | +0.94 | 2.3 | 0.15 | 39.0 | no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.9 | -3.2 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 13-5 | 72.2 | 50.5 | 21.8 | +6.99 | 38.8 | 0.67 | 55.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 29-14 | 67.4 | 50.1 | 17.4 | +12.42 | 28.9 | 0.44 | 44.2 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 5-3 | 62.5 | 50.4 | 12.1 | +1.63 | 20.4 | 1.0 | 62.5 | keep collecting (8/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 50.2 | 16.5 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 13-5 | 72.2 | 50.5 | 21.8 | +6.99 | 38.8 | 0.67 | 55.6 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 16-14 | 53.3 | 50.0 | 3.3 | +0.65 | 2.2 | 0.57 | 50.0 | no edge shown yet |
| consensus_gap+money_level | total | 4-3 | 57.1 | 49.7 | 7.4 | +0.53 | 7.5 | -0.43 | 14.3 | keep collecting (7/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 49.6 | 30.4 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 49.9 | -16.5 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 5-6 | 45.5 | 50.2 | -4.7 | -1.49 | -13.5 | 0.0 | 27.3 | keep collecting (11/30) |
| money_moving+rlm_ratio | total | 6-4 | 60.0 | 50.4 | 9.6 | +1.58 | 15.8 | 0.4 | 50.0 | keep collecting (10/30) |
| consensus_gap+follow_move | total | 11-8 | 57.9 | 49.9 | 8.0 | +1.97 | 10.4 | 1.58 | 68.4 | keep collecting (19/30) |
| consensus_gap+money_delta | total | 2-0 | 100.0 | 49.4 | 50.6 | +1.78 | 88.9 | 0.0 | 0.0 | keep collecting (2/30) |
| follow_move+money_delta | total | 2-2 | 50.0 | 50.3 | -0.3 | -0.22 | -5.5 | 1.25 | 50.0 | keep collecting (4/30) |
| money_delta+money_moving | total | 6-2 | 75.0 | 50.3 | 24.7 | +3.35 | 41.9 | 0.5 | 25.0 | keep collecting (8/30) |
| money_delta+pin_value | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 | -0.5 | 0.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 5-1 | 83.3 | 50.2 | 33.1 | +3.44 | 57.4 | 0.67 | 33.3 | keep collecting (6/30) |
| follow_move+pin_move | total | 2-0 | 100.0 | 50.6 | 49.4 | +1.86 | 93.0 | 1.0 | 100.0 | keep collecting (2/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 50.6 | -50.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 50.6 | -50.6 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 2-1 | 66.7 | 50.2 | 16.5 | +0.82 | 27.3 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+rlm_ratio | total | 2-1 | 66.7 | 50.6 | 16.1 | +0.86 | 28.7 | 0.67 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | total | 0-1 | 0.0 | 49.4 | -49.4 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_value | total | 0-1 | 0.0 | 49.4 | -49.4 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 49.4 | -49.4 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | total | 0-1 | 0.0 | 50.6 | -50.6 | -1.0 | -100.0 | 2.0 | 100.0 | keep collecting (1/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_move | both | 485-484 | 50.1 | 49.9 | 0.1 | -27.25 | -2.8 |  |  | no edge shown yet |
| money_delta | both | 312-414 | 43.0 | 43.9 | -0.9 | -55.34 | -7.6 |  |  | DROP: below break-even |
| pin_rlm | both | 138-155 | 47.1 | 42.1 | 5.0 | +31.16 | 10.6 |  |  | DROP: below break-even |
| follow_move | both | 842-750 | 52.9 | 52.0 | 0.9 | -90.28 | -5.7 |  |  | no edge shown yet |
| rlm_ratio | both | 196-222 | 46.9 | 44.4 | 2.5 | +0.4 | 0.1 |  |  | DROP: below break-even |
| money_level | both | 1069-786 | 57.6 | 55.8 | 1.9 | -59.98 | -3.2 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 828-961 | 46.3 | 47.4 | -1.1 | -121.3 | -6.8 |  |  | DROP: below break-even |
| money_moving | both | 828-962 | 46.3 | 47.7 | -1.5 | -130.86 | -7.3 |  |  | DROP: below break-even |
| pin_value | both | 344-352 | 49.4 | 47.7 | 1.7 | +1.96 | 0.3 |  |  | DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 50.6 | 16.0 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 327-444 | 42.4 | 46.7 | -4.3 | -85.75 | -11.1 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 124-124 | 50.0 | 50.9 | -0.9 | -14.58 | -5.9 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 147-240 | 38.0 | 43.9 | -6.0 | -30.55 | -7.9 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 77-80 | 49.0 | 50.5 | -1.4 | +2.8 | 1.8 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 23-39 | 37.1 | 36.8 | 0.3 | +10.03 | 16.2 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 130-144 | 47.4 | 45.1 | 2.3 | +3.92 | 1.4 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | both | 25-43 | 36.8 | 39.3 | -2.5 | -1.66 | -2.4 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 146-244 | 37.4 | 43.4 | -5.9 | -31.54 | -8.1 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 450-482 | 48.3 | 49.4 | -1.1 | -67.92 | -7.3 |  |  | DROP: below break-even |
| follow_move+pin_move | both | 347-343 | 50.3 | 50.3 | 0.0 | -28.55 | -4.1 |  |  | no edge shown yet |
| follow_move+pin_rlm | both | 107-109 | 49.5 | 44.3 | 5.3 | +8.59 | 4.0 |  |  | no edge shown yet |
| follow_move+pin_value | both | 119-115 | 50.9 | 48.9 | 2.0 | -9.07 | -3.9 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 196-222 | 46.9 | 44.4 | 2.5 | +0.4 | 0.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 455-479 | 48.7 | 49.2 | -0.5 | -57.81 | -6.2 |  |  | DROP: below break-even |
| money_moving+pin_move | both | 293-322 | 47.6 | 48.7 | -1.0 | -24.16 | -3.9 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 132-151 | 46.6 | 42.0 | 4.6 | +29.2 | 10.3 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 152-179 | 45.9 | 46.9 | -1.0 | -12.63 | -3.8 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 188-215 | 46.7 | 44.5 | 2.1 | -0.52 | -0.1 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 793-923 | 46.2 | 47.5 | -1.3 | -113.88 | -6.6 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 128-128 | 50.0 | 44.2 | 5.8 | +26.52 | 10.4 |  |  | no edge shown yet |
| pin_move+pin_value | both | 153-152 | 50.2 | 49.0 | 1.1 | -4.6 | -1.5 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 115-107 | 51.8 | 45.7 | 6.1 | +17.27 | 7.8 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 300-322 | 48.2 | 48.6 | -0.4 | -17.92 | -2.9 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 40-39 | 50.6 | 45.4 | 5.2 | +14.58 | 18.5 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 107-109 | 49.5 | 44.3 | 5.3 | +8.59 | 4.0 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 138-155 | 47.1 | 42.1 | 5.0 | +31.16 | 10.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 37-29 | 56.1 | 48.6 | 7.5 | +4.78 | 7.2 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 154-181 | 46.0 | 46.9 | -0.9 | -12.83 | -3.8 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 196-222 | 46.9 | 44.4 | 2.5 | +0.4 | 0.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 151-173 | 46.6 | 46.0 | 0.6 | -19.47 | -6.0 |  |  | DROP: below break-even |
| money_level+money_moving | both | 588-523 | 52.9 | 52.5 | 0.4 | -44.16 | -4.0 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 579-513 | 53.0 | 52.3 | 0.7 | -35.71 | -3.3 |  |  | no edge shown yet |
| follow_move+money_level | both | 557-394 | 58.6 | 56.8 | 1.7 | -43.94 | -4.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 94-80 | 54.0 | 48.6 | 5.4 | +10.7 | 6.2 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 200-160 | 55.6 | 57.9 | -2.4 | -20.11 | -5.6 |  |  | no edge shown yet |
| money_level+pin_move | both | 284-264 | 51.8 | 53.2 | -1.4 | -31.63 | -5.8 |  |  | no edge shown yet |
| money_level+pin_value | both | 168-156 | 51.9 | 49.8 | 2.1 | -10.11 | -3.1 |  |  | no edge shown yet |
| money_delta+money_moving | both | 222-323 | 40.7 | 42.3 | -1.6 | -47.34 | -8.7 |  |  | DROP: below break-even |
| consensus_gap+money_delta | both | 41-110 | 27.2 | 36.2 | -9.0 | -31.68 | -21.0 |  |  | DROP: below break-even |
| money_delta+money_level | both | 116-106 | 52.3 | 47.1 | 5.2 | +15.57 | 7.0 |  |  | no edge shown yet |
| money_delta+pin_value | both | 68-70 | 49.3 | 46.8 | 2.5 | -4.57 | -3.3 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 219-318 | 40.8 | 42.3 | -1.5 | -45.51 | -8.5 |  |  | DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 50.6 | 16.0 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 118-134 | 46.8 | 46.3 | 0.5 | -4.93 | -2.0 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 62-43 | 59.0 | 46.9 | 12.2 | +18.27 | 17.4 |  |  | no edge shown yet |
| money_delta+pin_rlm | both | 81-93 | 46.6 | 42.1 | 4.4 | +12.29 | 7.1 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | both | 110-114 | 49.1 | 44.9 | 4.2 | +1.9 | 0.8 |  |  | no edge shown yet |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 50.6 | 49.4 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_move | moneyline | 101-98 | 50.8 | 49.2 | 1.6 | +8.43 | 4.2 |  |  | no edge shown yet |
| pin_move | spread | 190-201 | 48.6 | 50.1 | -1.5 | -27.88 | -7.1 |  |  | DROP: below break-even |
| pin_move | total | 194-185 | 51.2 | 50.1 | 1.0 | -7.81 | -2.1 |  |  | no edge shown yet |
| money_delta | moneyline | 45-164 | 21.5 | 27.5 | -6.0 | -49.09 | -23.5 |  |  | DROP: below break-even |
| money_delta | spread | 122-123 | 49.8 | 50.7 | -0.9 | -11.91 | -4.9 |  |  | no edge shown yet |
| money_delta | total | 145-127 | 53.3 | 50.3 | 3.0 | +5.66 | 2.1 |  |  | no edge shown yet |
| pin_rlm | moneyline | 36-72 | 33.3 | 27.7 | 5.6 | +20.85 | 19.3 |  |  | DROP: below break-even |
| pin_rlm | spread | 25-22 | 53.2 | 50.8 | 2.4 | +0.79 | 1.7 |  |  | no edge shown yet |
| pin_rlm | total | 77-61 | 55.8 | 50.4 | 5.4 | +9.52 | 6.9 |  |  | no edge shown yet |
| follow_move | moneyline | 310-198 | 61.0 | 56.6 | 4.4 | -22.59 | -4.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 245-257 | 48.8 | 49.6 | -0.8 | -34.55 | -6.9 |  |  | DROP: below break-even |
| follow_move | total | 287-295 | 49.3 | 50.0 | -0.7 | -33.15 | -5.7 |  |  | no edge shown yet |
| rlm_ratio | moneyline | 36-80 | 31.0 | 29.2 | 1.8 | -3.76 | -3.2 |  |  | DROP: below break-even |
| rlm_ratio | spread | 41-42 | 49.4 | 50.1 | -0.7 | -4.76 | -5.7 |  |  | no edge shown yet |
| rlm_ratio | total | 119-100 | 54.3 | 50.3 | 4.0 | +8.92 | 4.1 |  |  | no edge shown yet |
| money_level | moneyline | 412-150 | 73.3 | 69.9 | 3.4 | -18.81 | -3.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 312-321 | 49.3 | 49.4 | -0.1 | -39.59 | -6.3 |  |  | DROP: below break-even |
| money_level | total | 345-315 | 52.3 | 49.9 | 2.4 | -1.58 | -0.2 |  |  | no edge shown yet |
| sharp_gap | moneyline | 192-324 | 37.2 | 41.3 | -4.1 | -61.56 | -11.9 |  |  | DROP: below break-even |
| sharp_gap | spread | 318-307 | 50.9 | 49.7 | 1.2 | -20.12 | -3.2 |  |  | no edge shown yet |
| sharp_gap | total | 318-330 | 49.1 | 50.1 | -1.1 | -39.61 | -6.1 |  |  | DROP: below break-even |
| money_moving | moneyline | 200-314 | 38.9 | 42.4 | -3.5 | -52.52 | -10.2 |  |  | DROP: below break-even |
| money_moving | spread | 315-310 | 50.4 | 49.6 | 0.8 | -25.99 | -4.2 |  |  | no edge shown yet |
| money_moving | total | 313-338 | 48.1 | 50.1 | -2.0 | -52.35 | -8.0 |  |  | DROP: below break-even |
| pin_value | moneyline | 18-53 | 25.4 | 29.3 | -4.0 | +11.87 | 16.7 |  |  | DROP: below break-even |
| pin_value | spread | 155-145 | 51.7 | 49.7 | 2.0 | -9.79 | -3.3 |  |  | no edge shown yet |
| pin_value | total | 171-154 | 52.6 | 49.9 | 2.7 | -0.12 | -0.0 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 51.9 | 48.1 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 138-269 | 33.9 | 44.3 | -10.4 | -75.55 | -18.6 |  |  | DROP: below break-even |
| consensus_gap | spread | 86-74 | 53.8 | 49.3 | 4.4 | -0.7 | -0.4 |  |  | no edge shown yet |
| consensus_gap | total | 103-101 | 50.5 | 49.7 | 0.8 | -9.51 | -4.7 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 140-80 | 63.6 | 64.0 | -0.4 | -6.8 | -3.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 131-78 | 62.7 | 63.5 | -0.8 | -6.42 | -3.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 178-300 | 37.2 | 41.2 | -4.0 | -48.8 | -10.2 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 51-64 | 44.3 | 52.7 | -8.4 | -18.01 | -15.7 |  |  | DROP: below break-even |
| consensus_gap+money_level | moneyline | 94-61 | 60.6 | 69.4 | -8.8 | -13.35 | -8.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 54-153 | 26.1 | 39.2 | -13.1 | -24.33 | -11.8 |  |  | DROP: below break-even |
| follow_move+money_level | moneyline | 243-74 | 76.7 | 71.3 | 5.3 | -8.6 | -2.7 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 98-108 | 47.6 | 48.1 | -0.6 | -13.59 | -6.6 |  |  | no edge shown yet |
| money_delta+money_moving | moneyline | 42-147 | 22.2 | 27.2 | -5.0 | -35.06 | -18.6 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 40-146 | 21.5 | 27.2 | -5.7 | -36.25 | -19.5 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 52-158 | 24.8 | 38.1 | -13.3 | -27.21 | -13.0 |  |  | DROP: below break-even |
| follow_move+sharp_gap | moneyline | 95-107 | 47.0 | 47.1 | -0.1 | -13.01 | -6.4 |  |  | DROP: below break-even |
| consensus_gap+pin_move | moneyline | 27-32 | 45.8 | 52.0 | -6.3 | +7.35 | 12.5 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 10-28 | 26.3 | 28.5 | -2.1 | +9.65 | 25.4 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 4-30 | 11.8 | 28.8 | -17.0 | -7.04 | -20.7 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 81-64 | 55.9 | 51.2 | 4.7 | +7.79 | 5.4 |  |  | no edge shown yet |
| follow_move+pin_rlm | moneyline | 23-39 | 37.1 | 29.0 | 8.1 | +1.48 | 2.4 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 36-80 | 31.0 | 29.2 | 1.8 | -3.76 | -3.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 44-62 | 41.5 | 42.3 | -0.8 | +9.13 | 8.6 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 35-70 | 33.3 | 27.8 | 5.6 | +21.45 | 20.4 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 35-76 | 31.5 | 29.4 | 2.1 | -1.16 | -1.0 |  |  | DROP: below break-even |
| pin_move+pin_rlm | moneyline | 26-45 | 36.6 | 28.0 | 8.7 | +16.21 | 22.8 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 20-30 | 40.0 | 29.8 | 10.2 | +7.3 | 14.6 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 44-63 | 41.1 | 41.7 | -0.6 | +7.95 | 7.4 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 23-39 | 37.1 | 29.0 | 8.1 | +1.48 | 2.4 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 36-72 | 33.3 | 27.7 | 5.6 | +20.85 | 19.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 36-80 | 31.0 | 29.2 | 1.8 | -3.76 | -3.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 11-82 | 11.8 | 27.5 | -15.6 | -29.62 | -31.8 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 13-44 | 22.8 | 28.5 | -5.6 | +2.38 | 4.2 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 16-35 | 31.4 | 29.7 | 1.7 | +0.84 | 1.6 |  |  | DROP: below break-even |
| money_delta+pin_rlm | moneyline | 21-44 | 32.3 | 28.1 | 4.2 | +6.49 | 10.0 |  |  | DROP: below break-even |
| money_delta+pin_value | moneyline | 2-18 | 10.0 | 25.9 | -15.9 | -11.18 | -55.9 |  |  | keep collecting (20/30) |
| money_moving+pin_value | moneyline | 10-32 | 23.8 | 28.2 | -4.4 | +9.44 | 22.5 |  |  | DROP: below break-even |
| pin_move+pin_value | moneyline | 6-9 | 40.0 | 32.3 | 7.7 | +7.27 | 48.5 |  |  | keep collecting (15/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 25.9 | 5.3 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 10-34 | 22.7 | 28.1 | -5.4 | +7.44 | 16.9 |  |  | DROP: below break-even |
| follow_move+money_delta | moneyline | 23-46 | 33.3 | 30.1 | 3.2 | -9.09 | -13.2 |  |  | DROP: below break-even |
| money_delta+money_level | moneyline | 13-21 | 38.2 | 30.2 | 8.1 | +7.09 | 20.8 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | moneyline | 21-38 | 35.6 | 30.0 | 5.6 | -3.0 | -5.1 |  |  | DROP: below break-even |
| money_level+pin_move | moneyline | 65-39 | 62.5 | 67.6 | -5.1 | -5.33 | -5.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 10-9 | 52.6 | 31.0 | 21.6 | +4.79 | 25.2 |  |  | keep collecting (19/30) |
| money_level+rlm_ratio | moneyline | 12-11 | 52.2 | 38.5 | 13.7 | +5.12 | 22.2 |  |  | keep collecting (23/30) |
| money_level+pin_value | moneyline | 5-1 | 83.3 | 66.1 | 17.3 | +1.68 | 28.0 |  |  | keep collecting (6/30) |
| follow_move+pin_value | moneyline | 2-7 | 22.2 | 31.3 | -9.0 | -4.79 | -53.3 |  |  | keep collecting (9/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 25.9 | -0.9 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 34-27 | 55.7 | 48.8 | 6.9 | +1.9 | 3.1 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 48-41 | 53.9 | 49.1 | 4.8 | -0.14 | -0.2 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 25-27 | 48.1 | 49.3 | -1.2 | -5.73 | -11.0 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | -0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 60-43 | 58.3 | 49.3 | 9.0 | +7.95 | 7.7 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 4-4 | 50.0 | 50.0 | 0.0 | -0.67 | -8.3 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | spread | 47-41 | 53.4 | 49.3 | 4.1 | -1.03 | -1.2 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 156-159 | 49.5 | 49.4 | 0.1 | -18.0 | -5.7 |  |  | no edge shown yet |
| follow_move+pin_move | spread | 120-132 | 47.6 | 49.9 | -2.3 | -22.73 | -9.0 |  |  | DROP: below break-even |
| follow_move+pin_rlm | spread | 19-18 | 51.4 | 50.6 | 0.8 | -0.65 | -1.7 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 56-49 | 53.3 | 49.2 | 4.2 | -0.23 | -0.2 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 41-42 | 49.4 | 50.1 | -0.7 | -4.76 | -5.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 157-158 | 49.8 | 49.4 | 0.4 | -15.87 | -5.0 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 114-123 | 48.1 | 49.8 | -1.7 | -19.67 | -8.3 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 23-22 | 51.1 | 50.7 | 0.4 | -1.04 | -2.3 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 77-78 | 49.7 | 49.3 | 0.3 | -11.61 | -7.5 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 39-41 | 48.8 | 50.0 | -1.3 | -5.69 | -7.1 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 310-302 | 50.7 | 49.6 | 1.0 | -22.5 | -3.7 |  |  | no edge shown yet |
| pin_move+pin_rlm | spread | 25-22 | 53.2 | 50.8 | 2.4 | +0.79 | 1.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 72-78 | 48.0 | 49.8 | -1.8 | -14.57 | -9.7 |  |  | no edge shown yet |
| pin_move+rlm_ratio | spread | 22-24 | 47.8 | 50.4 | -2.6 | -3.94 | -8.6 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 117-123 | 48.8 | 49.8 | -1.1 | -16.94 | -7.1 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 7-10 | 41.2 | 50.5 | -9.4 | -3.88 | -22.8 |  |  | keep collecting (17/30) |
| pin_rlm+rlm_ratio | spread | 19-18 | 51.4 | 50.6 | 0.8 | -0.65 | -1.7 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 25-22 | 53.2 | 50.8 | 2.4 | +0.79 | 1.7 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 7-7 | 50.0 | 49.5 | 0.5 | -1.01 | -7.2 |  |  | keep collecting (14/30) |
| pin_value+sharp_gap | spread | 77-78 | 49.7 | 49.4 | 0.3 | -11.67 | -7.5 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 41-42 | 49.4 | 50.1 | -0.7 | -4.76 | -5.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 151-162 | 48.2 | 49.2 | -1.0 | -25.58 | -8.2 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 21-27 | 43.8 | 49.8 | -6.1 | -8.13 | -16.9 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 245-240 | 50.5 | 49.4 | 1.1 | -19.3 | -4.0 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 57-45 | 55.9 | 49.0 | 6.9 | +3.72 | 3.6 |  |  | no edge shown yet |
| money_level+money_moving | spread | 244-241 | 50.3 | 49.4 | 0.9 | -21.22 | -4.4 |  |  | no edge shown yet |
| money_level+pin_move | spread | 104-124 | 45.6 | 49.6 | -4.0 | -30.16 | -13.2 |  |  | DROP: below break-even |
| money_level+pin_value | spread | 84-85 | 49.7 | 49.2 | 0.5 | -12.59 | -7.4 |  |  | no edge shown yet |
| consensus_gap+money_delta | spread | 14-14 | 50.0 | 50.4 | -0.4 | -2.09 | -7.5 |  |  | keep collecting (28/30) |
| follow_move+money_delta | spread | 38-46 | 45.2 | 50.2 | -4.9 | -11.62 | -13.8 |  |  | no edge shown yet |
| money_delta+money_level | spread | 40-39 | 50.6 | 50.0 | 0.6 | -2.96 | -3.7 |  |  | no edge shown yet |
| money_delta+money_moving | spread | 68-73 | 48.2 | 50.4 | -2.2 | -11.64 | -8.3 |  |  | no edge shown yet |
| money_delta+pin_value | spread | 32-26 | 55.2 | 50.4 | 4.8 | +1.88 | 3.2 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 67-71 | 48.6 | 50.4 | -1.8 | -10.62 | -7.7 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 14-10 | 58.3 | 50.3 | 8.0 | +2.58 | 10.7 |  |  | keep collecting (24/30) |
| money_delta+rlm_ratio | spread | 16-25 | 39.0 | 50.0 | -10.9 | -10.78 | -26.3 |  |  | DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 51.9 | 48.1 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_move | spread | 36-42 | 46.2 | 50.7 | -4.6 | -9.09 | -11.7 |  |  | no edge shown yet |
| money_delta+pin_rlm | spread | 13-15 | 46.4 | 50.5 | -4.1 | -3.31 | -11.8 |  |  | keep collecting (28/30) |
| follow_move+money_delta | total | 90-81 | 52.6 | 50.3 | 2.3 | +1.24 | 0.7 |  |  | no edge shown yet |
| money_level+money_moving | total | 204-202 | 50.2 | 50.0 | 0.3 | -16.14 | -4.0 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 203-195 | 51.0 | 50.0 | 1.0 | -9.98 | -2.5 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 305-321 | 48.7 | 50.1 | -1.4 | -42.59 | -6.8 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 49-54 | 47.6 | 49.6 | -2.0 | -10.48 | -10.2 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 25-21 | 54.3 | 49.7 | 4.6 | +1.18 | 2.6 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 57-57 | 50.0 | 49.7 | 0.3 | -6.41 | -5.6 |  |  | no edge shown yet |
| follow_move+money_moving | total | 196-215 | 47.7 | 50.1 | -2.4 | -36.33 | -8.8 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 203-214 | 48.7 | 50.1 | -1.4 | -28.93 | -6.9 |  |  | DROP: below break-even |
| money_level+pin_move | total | 115-101 | 53.2 | 50.0 | 3.2 | +3.86 | 1.8 |  |  | no edge shown yet |
| money_level+pin_value | total | 79-70 | 53.0 | 49.7 | 3.3 | +0.8 | 0.5 |  |  | no edge shown yet |
| pin_move+pin_value | total | 75-65 | 53.6 | 50.0 | 3.5 | +2.71 | 1.9 |  |  | no edge shown yet |
| money_moving+pin_move | total | 135-137 | 49.6 | 50.2 | -0.6 | -13.62 | -5.0 |  |  | no edge shown yet |
| money_delta+money_moving | total | 112-103 | 52.1 | 50.3 | 1.8 | -0.64 | -0.3 |  |  | no edge shown yet |
| follow_move+money_level | total | 163-158 | 50.8 | 49.9 | 0.9 | -9.75 | -3.0 |  |  | no edge shown yet |
| follow_move+pin_value | total | 61-59 | 50.8 | 50.0 | 0.9 | -4.04 | -3.4 |  |  | no edge shown yet |
| money_moving+pin_value | total | 65-69 | 48.5 | 50.0 | -1.5 | -10.46 | -7.8 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 67-69 | 49.3 | 50.0 | -0.8 | -8.6 | -6.3 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 45-46 | 49.5 | 49.7 | -0.3 | -6.08 | -6.7 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 47-45 | 51.1 | 49.7 | 1.3 | -3.3 | -3.6 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 39-33 | 54.2 | 49.6 | 4.5 | +1.52 | 2.1 |  |  | no edge shown yet |
| consensus_gap+money_delta | total | 16-14 | 53.3 | 49.9 | 3.4 | +0.03 | 0.1 |  |  | no edge shown yet |
| money_delta+sharp_gap | total | 112-101 | 52.6 | 50.3 | 2.2 | +1.36 | 0.6 |  |  | no edge shown yet |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 63-46 | 57.8 | 50.3 | 7.5 | +11.44 | 10.5 |  |  | no edge shown yet |
| money_delta+pin_move | total | 66-57 | 53.7 | 50.4 | 3.3 | +3.32 | 2.7 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 139-136 | 50.5 | 50.2 | 0.3 | -8.93 | -3.2 |  |  | no edge shown yet |
| follow_move+pin_move | total | 146-147 | 49.8 | 50.1 | -0.3 | -13.61 | -4.6 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | total | 10-8 | 55.6 | 49.9 | 5.6 | +0.87 | 4.8 |  |  | keep collecting (18/30) |
| consensus_gap+rlm_ratio | total | 17-9 | 65.4 | 49.8 | 15.6 | +6.04 | 23.2 |  |  | keep collecting (26/30) |
| follow_move+pin_rlm | total | 65-52 | 55.6 | 50.4 | 5.2 | +7.75 | 6.6 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 119-100 | 54.3 | 50.3 | 4.0 | +8.92 | 4.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 38-24 | 61.3 | 50.4 | 10.9 | +10.91 | 17.6 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 61-42 | 59.2 | 50.3 | 9.0 | +13.72 | 13.3 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 74-59 | 55.6 | 50.4 | 5.2 | +8.79 | 6.6 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 114-98 | 53.8 | 50.3 | 3.4 | +6.34 | 3.0 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 77-61 | 55.8 | 50.4 | 5.4 | +9.52 | 6.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 73-53 | 57.9 | 50.4 | 7.6 | +13.92 | 11.0 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 28-18 | 60.9 | 50.3 | 10.6 | +7.4 | 16.1 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 65-52 | 55.6 | 50.4 | 5.2 | +7.75 | 6.6 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 77-61 | 55.8 | 50.4 | 5.4 | +9.52 | 6.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 29-19 | 60.4 | 50.2 | 10.2 | +7.27 | 15.2 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 119-100 | 54.3 | 50.3 | 4.0 | +8.92 | 4.1 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 47-34 | 58.0 | 50.4 | 7.6 | +9.11 | 11.2 |  |  | no edge shown yet |
| money_delta+rlm_ratio | total | 73-51 | 58.9 | 50.4 | 8.5 | +15.68 | 12.6 |  |  | no edge shown yet |
| money_delta+pin_value | total | 34-26 | 56.7 | 50.2 | 6.4 | +4.73 | 7.9 |  |  | no edge shown yet |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 50.6 | 49.4 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_move | close | 1-3k bets | 303-295 | 50.7 | 0.9 | -1.2 |  |
| pin_move | close | 3k+ bets | 115-121 | 48.7 | -1.1 | -5.9 |  |
| pin_move | close | <1k bets | 67-68 | 49.6 | -1.1 | -4.6 |  |
| pin_move | close | pin $1-2k | 230-222 | 50.9 | 0.5 | -0.2 |  |
| pin_move | close | pin $2k+ | 168-178 | 48.6 | -0.8 | -7.5 |  |
| pin_move | close | pin limit <$1k | 87-84 | 50.9 | 1.0 | -0.1 |  |
| money_delta | close | 1-3k bets | 196-247 | 44.2 | -0.5 | -6.6 |  |
| money_delta | close | 3k+ bets | 78-105 | 42.6 | -0.3 | -1.8 |  |
| money_delta | close | <1k bets | 38-62 | 38.0 | -3.9 | -22.9 |  |
| money_delta | close | pin $1-2k | 111-112 | 49.8 | 4.1 | 4.0 |  |
| money_delta | close | pin $2k+ | 79-108 | 42.2 | 1.2 | -10.5 |  |
| money_delta | close | pin limit <$1k | 50-54 | 48.1 | -1.8 | -3.7 |  |
| pin_rlm | close | 1-3k bets | 86-92 | 48.3 | 5.7 | 17.7 |  |
| pin_rlm | close | 3k+ bets | 31-42 | 42.5 | 0.6 | -6.9 |  |
| pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.6 | 11.0 |  |
| pin_rlm | close | pin $1-2k | 61-62 | 49.6 | 6.0 | 14.5 |  |
| pin_rlm | close | pin $2k+ | 36-64 | 36.0 | 0.9 | -4.1 |  |
| pin_rlm | close | pin limit <$1k | 41-29 | 58.6 | 9.2 | 24.9 |  |
| follow_move | close | 1-3k bets | 539-470 | 53.4 | 1.8 | -4.3 |  |
| follow_move | close | 3k+ bets | 183-172 | 51.5 | -0.7 | -6.1 |  |
| follow_move | close | <1k bets | 120-108 | 52.6 | -0.7 | -11.2 |  |
| follow_move | close | pin $1-2k | 253-277 | 47.7 | -3.5 | -11.1 |  |
| follow_move | close | pin $2k+ | 212-172 | 55.2 | 2.9 | -3.1 |  |
| follow_move | close | pin limit <$1k | 104-104 | 50.0 | -0.1 | -4.6 |  |
| rlm_ratio | close | 1-3k bets | 125-154 | 44.8 | 0.1 | -3.6 |  |
| rlm_ratio | close | 3k+ bets | 45-42 | 51.7 | 7.3 | 11.5 |  |
| rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.9 | 0.8 |  |
| rlm_ratio | close | pin $1-2k | 68-69 | 49.6 | 3.3 | 4.2 |  |
| rlm_ratio | close | pin $2k+ | 37-50 | 42.5 | 4.5 | -5.6 |  |
| rlm_ratio | close | pin limit <$1k | 44-34 | 56.4 | 6.6 | 8.9 |  |
| money_level | close | 1-3k bets | 689-480 | 58.9 | 3.1 | -1.2 |  |
| money_level | close | 3k+ bets | 235-187 | 55.7 | 0.2 | -3.6 |  |
| money_level | close | <1k bets | 145-118 | 55.1 | -1.0 | -11.5 |  |
| money_level | close | pin $1-2k | 311-272 | 53.3 | -0.8 | -5.2 |  |
| money_level | close | pin $2k+ | 267-206 | 56.4 | -1.2 | -7.1 |  |
| money_level | close | pin limit <$1k | 124-120 | 50.8 | 0.7 | -3.4 |  |
| sharp_gap | close | 1-3k bets | 512-612 | 45.6 | -1.8 | -8.7 |  |
| sharp_gap | close | 3k+ bets | 202-211 | 48.9 | 1.6 | 3.6 |  |
| sharp_gap | close | <1k bets | 114-137 | 45.4 | -2.5 | -14.6 |  |
| sharp_gap | close | pin $1-2k | 271-296 | 47.8 | -0.9 | -4.6 |  |
| sharp_gap | close | pin $2k+ | 210-246 | 46.1 | -0.1 | -3.7 |  |
| sharp_gap | close | pin limit <$1k | 115-121 | 48.7 | -1.1 | -2.7 |  |
| money_moving | close | 1-3k bets | 515-611 | 45.7 | -2.1 | -9.3 |  |
| money_moving | close | 3k+ bets | 201-213 | 48.6 | 0.9 | 2.0 |  |
| money_moving | close | <1k bets | 112-137 | 45.0 | -2.5 | -13.5 |  |
| money_moving | close | pin $1-2k | 268-300 | 47.2 | -1.8 | -5.6 |  |
| money_moving | close | pin $2k+ | 211-244 | 46.4 | 0.2 | -3.6 |  |
| money_moving | close | pin limit <$1k | 110-127 | 46.4 | -3.3 | -7.2 |  |
| pin_value | close | 1-3k bets | 212-227 | 48.3 | 0.6 | -0.5 |  |
| pin_value | close | 3k+ bets | 78-81 | 49.1 | 0.8 | -3.9 |  |
| pin_value | close | <1k bets | 54-44 | 55.1 | 8.1 | 10.6 |  |
| pin_value | close | pin $1-2k | 159-180 | 46.9 | -1.2 | -4.8 |  |
| pin_value | close | pin $2k+ | 94-109 | 46.3 | 0.8 | -2.3 |  |
| pin_value | close | pin limit <$1k | 91-63 | 59.1 | 9.5 | 14.9 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 48.1 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 48.1 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 206-272 | 43.1 | -4.4 | -12.5 |  |
| consensus_gap | close | 3k+ bets | 81-93 | 46.6 | -0.6 | 6.3 |  |
| consensus_gap | close | <1k bets | 40-78 | 33.9 | -9.6 | -30.7 |  |
| consensus_gap | close | pin $1-2k | 105-119 | 46.9 | -1.9 | -2.4 |  |
| consensus_gap | close | pin $2k+ | 81-98 | 45.3 | -3.1 | -3.8 |  |
| consensus_gap | close | pin limit <$1k | 49-43 | 53.3 | 3.1 | 4.1 |  |
| consensus_gap+follow_move | close | 1-3k bets | 85-77 | 52.5 | 1.1 | -1.0 |  |
| consensus_gap+money_level | close | 1-3k bets | 138-91 | 60.3 | 1.4 | 3.2 |  |
| consensus_gap+money_moving | close | 1-3k bets | 97-150 | 39.3 | -5.5 | -10.1 |  |
| consensus_gap+pin_move | close | 1-3k bets | 50-48 | 51.0 | 0.4 | 5.4 |  |
| consensus_gap+pin_value | close | 1-3k bets | 82-99 | 45.3 | -0.1 | -2.9 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 95-153 | 38.3 | -5.6 | -11.2 |  |
| follow_move+money_level | close | 1-3k bets | 366-246 | 59.8 | 3.4 | -2.4 |  |
| follow_move+money_moving | close | 1-3k bets | 299-316 | 48.6 | -0.8 | -6.9 |  |
| follow_move+pin_move | close | 1-3k bets | 218-214 | 50.5 | 0.4 | -4.1 |  |
| follow_move+pin_value | close | 1-3k bets | 70-73 | 49.0 | 0.5 | -7.2 |  |
| follow_move+sharp_gap | close | 1-3k bets | 300-314 | 48.9 | -0.2 | -5.5 |  |
| money_level+money_moving | close | 1-3k bets | 376-328 | 53.4 | 0.8 | -2.9 |  |
| money_level+pin_move | close | 1-3k bets | 188-168 | 52.8 | 0.1 | -3.6 |  |
| money_level+pin_value | close | 1-3k bets | 107-98 | 52.2 | 2.6 | -2.1 |  |
| money_level+sharp_gap | close | 1-3k bets | 365-321 | 53.2 | 0.9 | -2.4 |  |
| money_moving+pin_move | close | 1-3k bets | 190-203 | 48.3 | -0.7 | -2.4 |  |
| money_moving+pin_value | close | 1-3k bets | 98-119 | 45.2 | -2.0 | -5.9 |  |
| money_moving+sharp_gap | close | 1-3k bets | 489-584 | 45.6 | -1.9 | -8.4 |  |
| pin_move+pin_value | close | 1-3k bets | 96-95 | 50.3 | 1.2 | -0.8 |  |
| pin_move+sharp_gap | close | 1-3k bets | 197-202 | 49.4 | 0.5 | -0.0 |  |
| pin_value+sharp_gap | close | 1-3k bets | 100-123 | 44.8 | -2.2 | -6.8 |  |
| consensus_gap+money_delta | close | 1-3k bets | 25-65 | 27.8 | -9.1 | -24.2 |  |
| follow_move+money_delta | close | 1-3k bets | 95-108 | 46.8 | -0.1 | -7.0 |  |
| money_delta+money_level | close | 1-3k bets | 74-68 | 52.1 | 4.1 | 7.9 |  |
| money_delta+money_moving | close | 1-3k bets | 136-197 | 40.8 | -2.2 | -10.4 |  |
| money_delta+pin_value | close | 1-3k bets | 44-44 | 50.0 | 2.6 | 0.2 |  |
| money_delta+sharp_gap | close | 1-3k bets | 135-195 | 40.9 | -2.2 | -10.2 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 70-77 | 47.6 | 0.1 | 2.1 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 17-26 | 39.5 | 1.9 | 19.2 |  |
| money_level+pin_rlm | close | 1-3k bets | 39-28 | 58.2 | 9.8 | 12.1 |  |
| pin_move+pin_rlm | close | 1-3k bets | 79-76 | 51.0 | 6.2 | 13.7 |  |
| pin_rlm+pin_value | close | 1-3k bets | 29-24 | 54.7 | 8.6 | 30.7 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 86-92 | 48.3 | 5.7 | 17.7 |  |
| money_delta+pin_rlm | close | 1-3k bets | 48-53 | 47.5 | 3.9 | 14.3 |  |
| money_moving+pin_rlm | close | 1-3k bets | 81-89 | 47.6 | 5.0 | 17.4 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 19-30 | 38.8 | -1.3 | 4.1 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 125-154 | 44.8 | 0.1 | -3.6 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 66-76 | 46.5 | 0.5 | -6.2 |  |
| money_level+rlm_ratio | close | 1-3k bets | 59-55 | 51.8 | 2.1 | -0.1 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 119-149 | 44.4 | -0.4 | -4.1 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 125-154 | 44.8 | 0.1 | -3.6 |  |
| follow_move+pin_rlm | close | 1-3k bets | 62-70 | 47.0 | 2.4 | -2.5 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 67-65 | 50.8 | 4.7 | 4.7 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 62-70 | 47.0 | 2.4 | -2.5 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 25-21 | 54.3 | 6.4 | 4.5 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 49.4 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 30-27 | 52.6 | 3.0 | 3.3 |  |
| consensus_gap+money_moving | close | 3k+ bets | 33-50 | 39.8 | -3.6 | 17.3 |  |
| consensus_gap+pin_move | close | 3k+ bets | 21-19 | 52.5 | 2.2 | 6.4 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-6 | 33.3 | -6.0 | 6.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 34-31 | 52.3 | 6.5 | 7.5 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -0.4 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 34-50 | 40.5 | -2.7 | 20.4 |  |
| follow_move+money_moving | close | 3k+ bets | 97-103 | 48.5 | -0.9 | -4.6 |  |
| follow_move+pin_move | close | 3k+ bets | 87-87 | 50.0 | -0.2 | -2.8 |  |
| follow_move+pin_rlm | close | 3k+ bets | 29-28 | 50.9 | 6.7 | 12.6 |  |
| follow_move+pin_value | close | 3k+ bets | 31-30 | 50.8 | 0.9 | -4.7 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 45-42 | 51.7 | 7.3 | 11.5 |  |
| follow_move+sharp_gap | close | 3k+ bets | 99-102 | 49.3 | 0.4 | -2.4 |  |
| money_moving+pin_move | close | 3k+ bets | 67-78 | 46.2 | -2.0 | -7.9 |  |
| money_moving+pin_rlm | close | 3k+ bets | 30-41 | 42.3 | 0.6 | -7.0 |  |
| money_moving+pin_value | close | 3k+ bets | 37-44 | 45.7 | -1.1 | -5.8 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 43-40 | 51.8 | 7.4 | 12.2 |  |
| money_moving+sharp_gap | close | 3k+ bets | 194-203 | 48.9 | 1.5 | 3.4 |  |
| pin_move+pin_rlm | close | 3k+ bets | 30-36 | 45.5 | 1.9 | 0.0 |  |
| pin_move+pin_value | close | 3k+ bets | 32-37 | 46.4 | -3.1 | -12.8 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 32-29 | 52.5 | 7.1 | 14.3 |  |
| pin_move+sharp_gap | close | 3k+ bets | 67-78 | 46.2 | -1.6 | -7.1 |  |
| pin_rlm+pin_value | close | 3k+ bets | 6-12 | 33.3 | -11.9 | -36.5 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 29-28 | 50.9 | 6.7 | 12.6 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 31-42 | 42.5 | 0.6 | -6.9 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 8-7 | 53.3 | 3.0 | 0.9 |  |
| pin_value+sharp_gap | close | 3k+ bets | 37-43 | 46.2 | -0.6 | -4.6 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 45-42 | 51.7 | 7.3 | 11.5 |  |
| follow_move+money_delta | close | 3k+ bets | 38-45 | 45.8 | 0.5 | -4.9 |  |
| money_level+money_moving | close | 3k+ bets | 136-117 | 53.8 | 1.4 | -0.3 |  |
| money_level+sharp_gap | close | 3k+ bets | 135-114 | 54.2 | 2.1 | 1.3 |  |
| follow_move+money_level | close | 3k+ bets | 116-89 | 56.6 | -0.3 | -4.3 |  |
| money_level+rlm_ratio | close | 3k+ bets | 22-12 | 64.7 | 17.3 | 33.4 |  |
| consensus_gap+money_level | close | 3k+ bets | 44-42 | 51.2 | -5.4 | -11.3 |  |
| money_level+pin_move | close | 3k+ bets | 62-61 | 50.4 | -3.5 | -7.6 |  |
| money_level+pin_value | close | 3k+ bets | 43-41 | 51.2 | 1.2 | -5.3 |  |
| money_delta+money_moving | close | 3k+ bets | 59-80 | 42.4 | 0.4 | 2.9 |  |
| consensus_gap+money_delta | close | 3k+ bets | 12-23 | 34.3 | -3.6 | 18.4 |  |
| money_delta+sharp_gap | close | 3k+ bets | 57-77 | 42.5 | 0.7 | 3.6 |  |
| money_delta+money_level | close | 3k+ bets | 30-21 | 58.8 | 12.3 | 19.2 |  |
| money_level+pin_rlm | close | 3k+ bets | 14-9 | 60.9 | 15.6 | 31.8 |  |
| money_delta+pin_value | close | 3k+ bets | 18-18 | 50.0 | 4.4 | -5.8 |  |
| money_delta+pin_move | close | 3k+ bets | 35-40 | 46.7 | 1.7 | -4.5 |  |
| money_delta+pin_rlm | close | 3k+ bets | 21-26 | 44.7 | 3.4 | -4.6 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 28-23 | 54.9 | 10.7 | 17.1 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 48.1 | 87.7 |  |
| money_level+money_moving | close | <1k bets | 76-77 | 49.7 | -2.9 | -14.4 |  |
| money_level+sharp_gap | close | <1k bets | 79-77 | 50.6 | -2.4 | -13.9 |  |
| money_moving+sharp_gap | close | <1k bets | 110-135 | 44.9 | -2.7 | -14.7 |  |
| consensus_gap+money_level | close | <1k bets | 18-27 | 40.0 | -16.1 | -39.4 |  |
| consensus_gap+money_moving | close | <1k bets | 17-40 | 29.8 | -11.5 | -34.9 |  |
| consensus_gap+pin_move | close | <1k bets | 6-13 | 31.6 | -18.3 | -26.5 |  |
| consensus_gap+pin_value | close | <1k bets | 14-14 | 50.0 | 8.3 | 15.4 |  |
| consensus_gap+sharp_gap | close | <1k bets | 17-41 | 29.3 | -11.7 | -36.0 |  |
| money_level+pin_move | close | <1k bets | 34-35 | 49.3 | -5.3 | -13.5 |  |
| money_level+pin_value | close | <1k bets | 18-17 | 51.4 | 1.2 | -4.2 |  |
| money_moving+pin_move | close | <1k bets | 36-41 | 46.8 | -1.2 | -4.2 |  |
| money_moving+pin_value | close | <1k bets | 17-16 | 51.5 | 6.2 | 14.9 |  |
| pin_move+pin_value | close | <1k bets | 25-20 | 55.6 | 7.3 | 12.9 |  |
| pin_move+sharp_gap | close | <1k bets | 36-42 | 46.2 | -2.4 | -9.5 |  |
| pin_value+sharp_gap | close | <1k bets | 17-15 | 53.1 | 7.2 | 18.5 |  |
| follow_move+money_delta | close | <1k bets | 18-20 | 47.4 | 4.9 | -3.2 |  |
| follow_move+money_moving | close | <1k bets | 54-63 | 46.2 | -3.6 | -13.8 |  |
| follow_move+pin_move | close | <1k bets | 42-42 | 50.0 | -1.5 | -7.2 |  |
| follow_move+sharp_gap | close | <1k bets | 56-63 | 47.1 | -3.5 | -16.1 |  |
| money_delta+money_moving | close | <1k bets | 27-46 | 37.0 | -2.8 | -23.1 |  |
| money_delta+pin_move | close | <1k bets | 13-17 | 43.3 | -0.5 | -15.5 |  |
| money_delta+sharp_gap | close | <1k bets | 27-46 | 37.0 | -2.8 | -23.1 |  |
| follow_move+rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.9 | 0.8 |  |
| money_delta+rlm_ratio | close | <1k bets | 16-15 | 51.6 | 10.1 | 6.3 |  |
| money_moving+rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.9 | 0.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 26-26 | 50.0 | 6.9 | 0.8 |  |
| follow_move+money_level | close | <1k bets | 75-59 | 56.0 | -2.6 | -15.1 |  |
| consensus_gap+money_delta | close | <1k bets | 4-22 | 15.4 | -16.0 | -63.0 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -0.7 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 12-14 | 46.2 | 8.1 | -0.2 |  |
| money_moving+pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.6 | 11.0 |  |
| pin_rlm+sharp_gap | close | <1k bets | 21-21 | 50.0 | 9.6 | 11.0 |  |
| money_delta+pin_value | close | <1k bets | 6-8 | 42.9 | -3.0 | -19.4 |  |
| consensus_gap+follow_move | close | <1k bets | 9-20 | 31.0 | -19.2 | -51.4 |  |
| follow_move+pin_rlm | close | <1k bets | 16-11 | 59.3 | 16.2 | 17.3 |  |
| follow_move+pin_value | close | <1k bets | 18-12 | 60.0 | 11.2 | 13.8 |  |
| pin_move+pin_rlm | close | <1k bets | 19-16 | 54.3 | 10.9 | 15.0 |  |
| pin_move+rlm_ratio | close | <1k bets | 16-13 | 55.2 | 10.1 | 7.8 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 21.5 | 60.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 16-11 | 59.3 | 16.2 | 17.3 |  |
| pin_value+rlm_ratio | close | <1k bets | 4-1 | 80.0 | 30.4 | 51.7 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 2-7 | 22.2 | -11.5 | -57.2 |  |
| money_delta+money_level | close | <1k bets | 12-17 | 41.4 | -2.1 | -18.9 |  |
| money_level+rlm_ratio | close | <1k bets | 13-13 | 50.0 | 4.6 | -1.9 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 17.7 | 19.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 39-45 | 46.4 | -5.7 | -10.9 |  |
| consensus_gap+money_moving | close | pin $1-2k | 54-65 | 45.4 | -2.9 | -3.4 |  |
| consensus_gap+pin_move | close | pin $1-2k | 41-42 | 49.4 | -3.0 | 4.8 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-18 | 41.9 | 1.3 | 25.8 |  |
| consensus_gap+pin_value | close | pin $1-2k | 62-70 | 47.0 | 1.3 | -5.6 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-14 | 50.0 | 4.6 | 9.0 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 52-63 | 45.2 | -1.8 | -2.5 |  |
| follow_move+money_moving | close | pin $1-2k | 150-181 | 45.3 | -4.6 | -11.1 |  |
| follow_move+pin_move | close | pin $1-2k | 161-166 | 49.2 | -1.5 | -5.4 |  |
| follow_move+pin_rlm | close | pin $1-2k | 49-46 | 51.6 | 5.7 | 8.8 |  |
| follow_move+pin_value | close | pin $1-2k | 53-63 | 45.7 | -3.7 | -13.9 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 68-69 | 49.6 | 3.3 | 4.2 |  |
| follow_move+sharp_gap | close | pin $1-2k | 153-179 | 46.1 | -3.7 | -10.0 |  |
| money_moving+pin_move | close | pin $1-2k | 145-158 | 47.9 | -1.5 | -2.7 |  |
| money_moving+pin_rlm | close | pin $1-2k | 58-60 | 49.2 | 5.2 | 14.1 |  |
| money_moving+pin_value | close | pin $1-2k | 65-93 | 41.1 | -6.7 | -19.4 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 66-66 | 50.0 | 3.2 | 4.8 |  |
| money_moving+sharp_gap | close | pin $1-2k | 260-288 | 47.4 | -1.3 | -5.0 |  |
| pin_move+pin_rlm | close | pin $1-2k | 58-56 | 50.9 | 5.8 | 14.8 |  |
| pin_move+pin_value | close | pin $1-2k | 69-84 | 45.1 | -4.6 | -12.8 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 57-50 | 53.3 | 6.3 | 10.4 |  |
| pin_move+sharp_gap | close | pin $1-2k | 148-157 | 48.5 | -0.6 | -1.7 |  |
| pin_rlm+pin_value | close | pin $1-2k | 15-22 | 40.5 | -7.7 | -15.3 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 49-46 | 51.6 | 5.7 | 8.8 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 61-62 | 49.6 | 6.0 | 14.5 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 17-18 | 48.6 | -1.3 | -8.5 |  |
| pin_value+sharp_gap | close | pin $1-2k | 65-91 | 41.7 | -6.0 | -18.4 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 68-69 | 49.6 | 3.3 | 4.2 |  |
| follow_move+money_level | close | pin $1-2k | 176-167 | 51.3 | -3.2 | -10.3 |  |
| money_level+rlm_ratio | close | pin $1-2k | 40-32 | 55.6 | 6.9 | 8.4 |  |
| money_level+sharp_gap | close | pin $1-2k | 197-191 | 50.8 | -1.1 | -5.7 |  |
| money_level+money_moving | close | pin $1-2k | 197-195 | 50.3 | -1.8 | -6.7 |  |
| consensus_gap+money_level | close | pin $1-2k | 61-55 | 52.6 | -4.4 | -7.2 |  |
| money_level+pin_value | close | pin $1-2k | 72-77 | 48.3 | -1.6 | -9.6 |  |
| money_level+pin_move | close | pin $1-2k | 140-131 | 51.7 | -1.3 | -5.8 |  |
| money_level+pin_rlm | close | pin $1-2k | 29-22 | 56.9 | 10.4 | 11.8 |  |
| follow_move+money_delta | close | pin $1-2k | 54-54 | 50.0 | 3.9 | 3.2 |  |
| money_delta+money_moving | close | pin $1-2k | 76-89 | 46.1 | 1.8 | -0.1 |  |
| money_delta+pin_move | close | pin $1-2k | 58-60 | 49.2 | 1.9 | 4.4 |  |
| money_delta+pin_rlm | close | pin $1-2k | 37-40 | 48.1 | 4.7 | 11.4 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 42-39 | 51.9 | 5.9 | 9.2 |  |
| money_delta+sharp_gap | close | pin $1-2k | 76-87 | 46.6 | 2.3 | 1.1 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 48.1 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 42-36 | 53.8 | 5.9 | 4.8 |  |
| consensus_gap+money_delta | close | pin $1-2k | 16-26 | 38.1 | -2.2 | -10.1 |  |
| money_delta+pin_value | close | pin $1-2k | 37-41 | 47.4 | -1.0 | -10.3 |  |
| follow_move+money_level | close | pin $2k+ | 135-83 | 61.9 | 2.1 | -1.4 |  |
| follow_move+money_moving | close | pin $2k+ | 103-101 | 50.5 | 2.6 | -3.3 |  |
| follow_move+pin_move | close | pin $2k+ | 127-117 | 52.0 | 2.2 | -2.0 |  |
| follow_move+sharp_gap | close | pin $2k+ | 104-102 | 50.5 | 2.7 | -3.0 |  |
| money_level+money_moving | close | pin $2k+ | 141-127 | 52.6 | -0.3 | -4.4 |  |
| money_level+pin_move | close | pin $2k+ | 95-86 | 52.5 | -2.8 | -7.5 |  |
| money_level+sharp_gap | close | pin $2k+ | 141-128 | 52.4 | -0.5 | -4.4 |  |
| money_moving+pin_move | close | pin $2k+ | 90-103 | 46.6 | -0.4 | -6.5 |  |
| money_moving+sharp_gap | close | pin $2k+ | 205-240 | 46.1 | -0.0 | -3.5 |  |
| pin_move+sharp_gap | close | pin $2k+ | 90-104 | 46.4 | -0.6 | -6.5 |  |
| consensus_gap+money_delta | close | pin $2k+ | 7-25 | 21.9 | -9.4 | -56.9 |  |
| consensus_gap+money_moving | close | pin $2k+ | 29-56 | 34.1 | -7.4 | -5.3 |  |
| consensus_gap+pin_value | close | pin $2k+ | 33-43 | 43.4 | 2.8 | 9.2 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 31-59 | 34.4 | -7.9 | -4.8 |  |
| money_delta+money_moving | close | pin $2k+ | 53-77 | 40.8 | 2.4 | -9.9 |  |
| money_delta+pin_value | close | pin $2k+ | 18-21 | 46.2 | 3.9 | -11.8 |  |
| money_delta+sharp_gap | close | pin $2k+ | 51-76 | 40.2 | 1.7 | -11.1 |  |
| money_moving+pin_value | close | pin $2k+ | 52-61 | 46.0 | 1.6 | 6.4 |  |
| pin_value+sharp_gap | close | pin $2k+ | 52-62 | 45.6 | 1.3 | 5.4 |  |
| consensus_gap+pin_move | close | pin $2k+ | 22-28 | 44.0 | -4.1 | -15.7 |  |
| money_delta+pin_move | close | pin $2k+ | 31-44 | 41.3 | -0.8 | -14.8 |  |
| consensus_gap+follow_move | close | pin $2k+ | 25-24 | 51.0 | 0.8 | -14.0 |  |
| follow_move+pin_value | close | pin $2k+ | 32-29 | 52.5 | 5.3 | -0.7 |  |
| pin_move+pin_value | close | pin $2k+ | 44-43 | 50.6 | 3.0 | -0.4 |  |
| follow_move+money_delta | close | pin $2k+ | 31-36 | 46.3 | 4.4 | -3.9 |  |
| follow_move+pin_rlm | close | pin $2k+ | 26-41 | 38.8 | 1.4 | -10.9 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 37-50 | 42.5 | 4.5 | -5.6 |  |
| money_delta+money_level | close | pin $2k+ | 23-19 | 54.8 | 10.5 | 11.1 |  |
| money_delta+pin_rlm | close | pin $2k+ | 20-36 | 35.7 | 0.5 | -10.5 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 19-22 | 46.3 | 8.0 | 0.7 |  |
| money_level+pin_rlm | close | pin $2k+ | 14-9 | 60.9 | 18.0 | 29.5 |  |
| money_level+pin_value | close | pin $2k+ | 51-47 | 52.0 | 2.3 | -4.0 |  |
| money_level+rlm_ratio | close | pin $2k+ | 13-11 | 54.2 | 7.2 | 14.2 |  |
| money_moving+pin_rlm | close | pin $2k+ | 36-64 | 36.0 | 0.9 | -4.1 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 37-49 | 43.0 | 4.9 | -4.5 |  |
| pin_move+pin_rlm | close | pin $2k+ | 30-43 | 41.1 | 3.3 | -3.3 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 26-35 | 42.6 | 2.9 | -2.2 |  |
| pin_rlm+pin_value | close | pin $2k+ | 6-13 | 31.6 | -3.8 | 13.6 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 26-41 | 38.8 | 1.4 | -10.9 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 36-64 | 36.0 | 0.9 | -4.1 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 4-6 | 40.0 | -0.6 | -19.0 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 37-50 | 42.5 | 4.5 | -5.6 |  |
| consensus_gap+money_level | close | pin $2k+ | 52-40 | 56.5 | -6.3 | -12.1 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-19 | 17.4 | -10.7 | -24.8 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-11 | 0.0 | -28.3 | -100.0 |  |
| follow_move+money_delta | close | pin limit <$1k | 31-37 | 45.6 | -4.4 | -12.5 |  |
| money_level+money_moving | close | pin limit <$1k | 68-76 | 47.2 | -2.6 | -9.4 |  |
| money_level+sharp_gap | close | pin limit <$1k | 67-70 | 48.9 | -1.0 | -6.1 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 103-112 | 47.9 | -1.8 | -3.9 |  |
| consensus_gap+money_level | close | pin limit <$1k | 27-25 | 51.9 | 1.5 | -4.1 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 14-10 | 58.3 | 9.8 | 27.8 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 35-31 | 53.0 | 3.9 | 6.4 |  |
| follow_move+money_moving | close | pin limit <$1k | 64-73 | 46.7 | -3.1 | -10.2 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 69-73 | 48.6 | -1.2 | -6.6 |  |
| money_level+pin_move | close | pin limit <$1k | 49-47 | 51.0 | 1.1 | -2.5 |  |
| money_level+pin_value | close | pin limit <$1k | 45-32 | 58.4 | 8.9 | 10.6 |  |
| pin_move+pin_value | close | pin limit <$1k | 40-25 | 61.5 | 12.1 | 23.8 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 17-10 | 63.0 | 12.8 | 15.4 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 21-17 | 55.3 | 6.3 | 16.0 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 23-18 | 56.1 | 6.9 | 16.7 |  |
| follow_move+money_level | close | pin limit <$1k | 53-54 | 49.5 | -0.7 | -5.7 |  |
| follow_move+pin_move | close | pin limit <$1k | 59-60 | 49.6 | -0.3 | -5.1 |  |
| follow_move+pin_value | close | pin limit <$1k | 34-23 | 59.6 | 10.0 | 13.2 |  |
| money_moving+pin_move | close | pin limit <$1k | 58-61 | 48.7 | -1.1 | -3.0 |  |
| money_moving+pin_value | close | pin limit <$1k | 35-25 | 58.3 | 9.0 | 18.1 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 62-61 | 50.4 | 0.6 | 0.0 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 37-28 | 56.9 | 7.4 | 14.9 |  |
| money_delta+money_moving | close | pin limit <$1k | 43-45 | 48.9 | -1.0 | -1.4 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 7-6 | 53.8 | 5.9 | 35.2 |  |
| money_delta+money_level | close | pin limit <$1k | 25-19 | 56.8 | 6.5 | 8.8 |  |
| money_delta+pin_value | close | pin limit <$1k | 13-8 | 61.9 | 13.1 | 38.5 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 42-43 | 49.4 | -0.4 | -0.3 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 29-30 | 49.2 | -0.5 | 1.6 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 6-2 | 75.0 | 28.2 | 96.7 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 24-17 | 58.5 | 9.3 | 23.0 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 38-27 | 58.5 | 9.2 | 25.7 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 40-29 | 58.0 | 8.3 | 17.5 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-4 | 82.6 | 33.5 | 76.8 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 41-29 | 58.6 | 9.2 | 24.9 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 32-22 | 59.3 | 9.3 | 14.0 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 44-34 | 56.4 | 6.6 | 8.9 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 25-21 | 54.3 | 4.4 | 4.4 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 40-32 | 55.6 | 5.8 | 7.4 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 32-22 | 59.3 | 9.3 | 14.0 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 32-22 | 59.3 | 9.3 | 14.0 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 44-34 | 56.4 | 6.6 | 8.9 |  |
| money_level+pin_rlm | close | pin limit <$1k | 19-12 | 61.3 | 10.8 | 17.6 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 21-14 | 60.0 | 10.3 | 16.8 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 16-5 | 76.2 | 25.9 | 46.1 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 5-3 | 62.5 | 12.6 | 18.4 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 49.4 | 87.7 |  |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -49.4 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 5-8 | 38.5 | -9.6 | -31.5 | 0.32 |
| pin_move | early | pin $1-2k | 0-3 | 0.0 | -34.6 | -100.0 | 0.23 |
| pin_move | early | pin limit <$1k | 5-6 | 45.5 | -6.4 | -19.1 | 0.22 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 16.9 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 8-6 | 57.1 | 17.2 | 26.7 | -0.34 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -38.9 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 4-0 | 100.0 | 50.3 | 88.0 | -0.25 |
| pin_rlm | early | <1k bets | 1-2 | 33.3 | 7.4 | -35.8 | -1.0 |
| pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -25.9 | -100.0 | -1.75 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.2 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -50.6 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 389-323 | 54.6 | 2.2 | -5.3 | 0.23 |
| follow_move | early | pin $1-2k | 27-16 | 62.8 | 8.4 | 11.9 | -0.35 |
| follow_move | early | pin limit <$1k | 47-39 | 54.7 | 4.4 | 1.9 | -0.11 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 24.0 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -51.9 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 23-14 | 62.2 | 25.7 | 37.6 | 0.56 |
| rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.7 | 55.6 | -1.52 |
| rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.4 | 77.5 | 0.29 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 0.7 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 42.4 | 59.7 | 0.33 |
| money_level | early | <1k bets | 140-88 | 61.4 | 1.4 | -4.0 | -0.13 |
| money_level | early | pin $1-2k | 20-8 | 71.4 | 5.3 | 4.1 | 0.01 |
| money_level | early | pin limit <$1k | 24-26 | 48.0 | -5.4 | -11.4 | 0.22 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.6 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 7.8 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 116-97 | 54.5 | 5.9 | 5.0 | 0.32 |
| sharp_gap | early | pin $1-2k | 15-11 | 57.7 | 4.7 | 6.7 | -0.39 |
| sharp_gap | early | pin limit <$1k | 29-18 | 61.7 | 13.2 | 27.9 | 0.12 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.4 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.6 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 78-70 | 52.7 | 0.8 | -8.4 | -0.03 |
| money_moving | early | pin $1-2k | 8-8 | 50.0 | -8.8 | -31.4 | 0.21 |
| money_moving | early | pin limit <$1k | 23-9 | 71.9 | 22.7 | 52.0 | 0.42 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.6 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 51.9 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 36-39 | 48.0 | -0.2 | -9.2 | 0.13 |
| pin_value | early | pin $1-2k | 13-18 | 41.9 | -3.7 | -21.1 | 0.12 |
| pin_value | early | pin limit <$1k | 36-30 | 54.5 | 5.0 | 3.2 | 0.09 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -49.4 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -26.5 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.3 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 13.0 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 175-231 | 43.1 | -4.2 | -14.0 | 0.36 |
| consensus_gap | early | pin $1-2k | 12-20 | 37.5 | -7.8 | -28.2 | 0.51 |
| consensus_gap | early | pin limit <$1k | 18-34 | 34.6 | -15.6 | -28.2 | 0.28 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -51.9 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 16.9 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 16.9 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -0.6 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 16.8 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 4.5 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 4.0 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.7 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.5 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.5 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -49.4 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -1.1 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 3.6 | -6.9 | 0.3 |
| follow_move+pin_value | early | 1-3k bets | 7-6 | 53.8 | 6.5 | 0.8 | -0.31 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.7 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.2 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 2.5 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.5 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 24.0 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.6 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 24.0 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.0 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.8 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 19.3 | 18.8 | -0.24 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -25.9 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 51.9 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 51.9 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 51.9 | 83.3 | 1.0 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -51.9 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -51.9 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.6 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 51.9 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 51.9 | 83.3 | 1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -51.9 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 37.7 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 49.4 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 25-32 | 43.9 | -8.4 | -20.0 | 0.91 |
| consensus_gap+money_level | early | <1k bets | 28-21 | 57.1 | -8.8 | -10.9 | 0.38 |
| consensus_gap+sharp_gap | early | <1k bets | 21-38 | 35.6 | -11.0 | -20.5 | 1.03 |
| follow_move+money_level | early | <1k bets | 75-33 | 69.4 | 7.8 | 2.5 | 0.05 |
| follow_move+sharp_gap | early | <1k bets | 63-28 | 69.2 | 18.8 | 22.2 | 0.47 |
| money_level+sharp_gap | early | <1k bets | 79-46 | 63.2 | 6.3 | 2.8 | 0.16 |
| follow_move+money_moving | early | <1k bets | 41-24 | 63.1 | 9.1 | 8.5 | 0.32 |
| money_level+money_moving | early | <1k bets | 49-35 | 58.3 | -0.8 | -8.2 | -0.27 |
| money_moving+sharp_gap | early | <1k bets | 46-40 | 53.5 | 3.9 | -3.9 | 0.1 |
| consensus_gap+money_moving | early | <1k bets | 10-19 | 34.5 | -13.7 | -44.4 | 0.26 |
| follow_move+pin_value | early | <1k bets | 13-11 | 54.2 | 4.5 | 1.3 | -0.01 |
| follow_move+rlm_ratio | early | <1k bets | 23-14 | 62.2 | 25.7 | 37.6 | 0.56 |
| rlm_ratio+sharp_gap | early | <1k bets | 23-14 | 62.2 | 25.7 | 37.6 | 0.56 |
| pin_move+pin_value | early | <1k bets | 1-4 | 20.0 | -29.1 | -61.8 | 0.2 |
| follow_move+pin_move | early | <1k bets | 5-3 | 62.5 | 10.0 | 11.2 | 0.42 |
| consensus_gap+pin_value | early | <1k bets | 13-23 | 36.1 | -10.3 | -32.5 | 0.4 |
| money_delta+money_moving | early | <1k bets | 7-6 | 53.8 | 14.7 | 21.7 | -0.36 |
| money_delta+sharp_gap | early | <1k bets | 6-4 | 60.0 | 21.9 | 39.1 | -0.47 |
| consensus_gap+pin_move | early | <1k bets | 0-5 | 0.0 | -44.4 | -100.0 | 0.26 |
| money_level+pin_move | early | <1k bets | 2-2 | 50.0 | -5.9 | -21.8 | 0.1 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | <1k bets | 3-3 | 50.0 | 11.7 | 3.0 | 0.87 |
| follow_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 24.1 | -3.7 | -2.15 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 24.1 | -3.7 | -2.15 |
| pin_rlm+sharp_gap | early | <1k bets | 1-2 | 33.3 | 7.4 | -35.8 | -1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 11.7 | -4.5 | -1.9 |
| pin_value+sharp_gap | early | <1k bets | 5-4 | 55.6 | 8.5 | 6.1 | -0.09 |
| money_level+pin_value | early | <1k bets | 4-4 | 50.0 | 0.1 | -4.5 | 0.88 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -51.2 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -50.6 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 1-2 | 33.3 | -17.3 | -36.4 | 1.33 |
| money_level+rlm_ratio | early | <1k bets | 7-6 | 53.8 | 16.6 | 12.9 | 1.69 |
| money_moving+rlm_ratio | early | <1k bets | 9-6 | 60.0 | 19.5 | 38.2 | 0.3 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 50.6 | 90.9 | 0.0 |
| money_delta+money_level | early | <1k bets | 3-1 | 75.0 | 30.9 | 61.5 | 1.2 |
| pin_move+sharp_gap | early | <1k bets | 2-1 | 66.7 | 16.9 | 4.3 | -0.07 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 3-3 | 50.0 | 11.7 | 37.5 | 0.07 |
| money_delta+rlm_ratio | early | <1k bets | 2-1 | 66.7 | 32.5 | 111.3 | 0.87 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 49.4 | 90.9 | -1.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -25.9 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 5-4 | 55.6 | -9.9 | -12.6 | 0.71 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -32.1 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 5-10 | 33.3 | -7.9 | -38.7 | 0.31 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.7 | 55.6 | -1.52 |
| follow_move+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 13.7 | 37.5 | -0.83 |
| money_level+money_moving | early | pin $1-2k | 8-5 | 61.5 | -4.8 | -15.6 | 0.07 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.9 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-3 | 40.0 | 3.7 | 55.6 | -1.52 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -51.9 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -38.9 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -51.9 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -38.9 | -100.0 | 2.5 |
| money_level+sharp_gap | early | pin $1-2k | 12-4 | 75.0 | 9.9 | 12.5 | -0.26 |
| money_moving+sharp_gap | early | pin $1-2k | 4-6 | 40.0 | -17.0 | -45.4 | 0.08 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.6 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 4-6 | 40.0 | -10.0 | -31.3 | 0.34 |
| follow_move+pin_value | early | pin $1-2k | 6-5 | 54.5 | 7.1 | 0.8 | -0.3 |
| follow_move+money_level | early | pin $1-2k | 11-4 | 73.3 | 7.7 | 6.6 | -0.07 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 48.1 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 4-1 | 80.0 | 11.1 | 6.9 | -0.18 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -16.7 | -46.8 | -0.12 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -25.9 | -100.0 | -1.75 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -25.9 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | 1.3 |
| money_level+money_moving | early | pin limit <$1k | 13-7 | 65.0 | 12.6 | 20.2 | 0.48 |
| money_level+sharp_gap | early | pin limit <$1k | 20-16 | 55.6 | 4.9 | 1.6 | 0.14 |
| money_moving+sharp_gap | early | pin limit <$1k | 18-5 | 78.3 | 30.3 | 70.1 | 0.35 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -49.4 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 9-6 | 60.0 | 9.8 | 13.8 | 0.33 |
| money_moving+pin_value | early | pin limit <$1k | 7-4 | 63.6 | 13.7 | 20.1 | 0.18 |
| pin_value+sharp_gap | early | pin limit <$1k | 12-6 | 66.7 | 16.7 | 26.4 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-9 | 40.0 | -12.2 | -25.7 | 0.53 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -26.9 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 14-18 | 43.8 | -5.2 | -17.9 | 0.43 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.2 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 11-11 | 50.0 | -4.1 | -7.4 | -0.04 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 4.4 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 13-7 | 65.0 | 16.4 | 24.2 | -0.07 |
| follow_move+rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.4 | 77.5 | 0.29 |
| money_level+rlm_ratio | early | pin limit <$1k | 6-0 | 100.0 | 53.7 | 92.6 | 0.42 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 16.5 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 7-1 | 87.5 | 43.4 | 77.5 | 0.29 |
| consensus_gap+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 22.8 | 72.3 | 0.54 |
| follow_move+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.2 | 85.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 9-3 | 75.0 | 25.4 | 43.3 | 0.33 |
| money_delta+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 50.6 | 87.1 | -0.33 |
| money_delta+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 50.6 | 87.1 | -0.33 |
| money_moving+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.0 | 45.3 | -0.5 |
| money_delta+sharp_gap | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 | -0.5 |
| pin_move+pin_value | early | pin limit <$1k | 1-4 | 20.0 | -29.1 | -61.8 | 0.2 |
| follow_move+pin_move | early | pin limit <$1k | 5-3 | 62.5 | 10.0 | 11.2 | 0.42 |
| consensus_gap+pin_move | early | pin limit <$1k | 0-3 | 0.0 | -56.8 | -100.0 | 0.53 |
| money_level+pin_move | early | pin limit <$1k | 2-2 | 50.0 | -5.9 | -21.8 | 0.1 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -50.6 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -50.6 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 16.9 | 4.3 | -0.07 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 49.4 | 90.9 | -1.0 |
| pin_move | close | 1-3k bets | 289-288 | 50.1 | 0.3 | -2.6 |  |
| pin_move | close | 3k+ bets | 107-112 | 48.9 | -1.1 | -5.6 |  |
| pin_move | close | <1k bets | 67-68 | 49.6 | -1.2 | -4.6 |  |
| pin_move | close | pin $1-2k | 220-213 | 50.8 | 0.3 | -0.8 |  |
| pin_move | close | pin $2k+ | 159-174 | 47.7 | -1.5 | -9.0 |  |
| pin_move | close | pin limit <$1k | 84-81 | 50.9 | 0.9 | 0.0 |  |
| money_delta | close | 1-3k bets | 187-237 | 44.1 | -0.7 | -7.1 |  |
| money_delta | close | 3k+ bets | 75-96 | 43.9 | 1.2 | 1.7 |  |
| money_delta | close | <1k bets | 38-62 | 38.0 | -3.9 | -22.9 |  |
| money_delta | close | pin $1-2k | 105-106 | 49.8 | 4.1 | 3.3 |  |
| money_delta | close | pin $2k+ | 74-104 | 41.6 | 0.7 | -11.5 |  |
| money_delta | close | pin limit <$1k | 50-51 | 49.5 | -0.6 | -0.8 |  |
| pin_rlm | close | 1-3k bets | 80-91 | 46.8 | 4.3 | 14.4 |  |
| pin_rlm | close | 3k+ bets | 29-36 | 44.6 | 3.1 | -1.5 |  |
| pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| pin_rlm | close | pin $1-2k | 55-57 | 49.1 | 5.6 | 13.3 |  |
| pin_rlm | close | pin $2k+ | 34-64 | 34.7 | -0.3 | -6.1 |  |
| pin_rlm | close | pin limit <$1k | 41-27 | 60.3 | 10.7 | 28.6 |  |
| follow_move | close | 1-3k bets | 522-453 | 53.5 | 2.0 | -3.9 |  |
| follow_move | close | 3k+ bets | 170-163 | 51.1 | -1.5 | -7.3 |  |
| follow_move | close | <1k bets | 120-108 | 52.6 | -0.7 | -11.2 |  |
| follow_move | close | pin $1-2k | 245-265 | 48.0 | -3.2 | -10.4 |  |
| follow_move | close | pin $2k+ | 199-169 | 54.1 | 1.7 | -5.3 |  |
| follow_move | close | pin limit <$1k | 103-102 | 50.2 | 0.1 | -4.1 |  |
| rlm_ratio | close | 1-3k bets | 122-149 | 45.0 | 0.4 | -2.9 |  |
| rlm_ratio | close | 3k+ bets | 42-37 | 53.2 | 8.7 | 14.4 |  |
| rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.8 | 0.8 |  |
| rlm_ratio | close | pin $1-2k | 64-65 | 49.6 | 3.4 | 4.7 |  |
| rlm_ratio | close | pin $2k+ | 35-50 | 41.2 | 3.0 | -8.9 |  |
| rlm_ratio | close | pin limit <$1k | 44-32 | 57.9 | 7.9 | 11.8 |  |
| money_level | close | 1-3k bets | 661-463 | 58.8 | 3.0 | -1.5 |  |
| money_level | close | 3k+ bets | 216-174 | 55.4 | -0.2 | -4.6 |  |
| money_level | close | <1k bets | 144-118 | 55.0 | -1.1 | -11.5 |  |
| money_level | close | pin $1-2k | 296-264 | 52.9 | -1.2 | -6.0 |  |
| money_level | close | pin $2k+ | 257-196 | 56.7 | -1.0 | -6.9 |  |
| money_level | close | pin limit <$1k | 119-118 | 50.2 | 0.1 | -4.5 |  |
| sharp_gap | close | 1-3k bets | 493-588 | 45.6 | -1.8 | -8.5 |  |
| sharp_gap | close | 3k+ bets | 186-196 | 48.7 | 1.5 | 3.9 |  |
| sharp_gap | close | <1k bets | 114-137 | 45.4 | -2.5 | -14.6 |  |
| sharp_gap | close | pin $1-2k | 258-286 | 47.4 | -1.3 | -5.4 |  |
| sharp_gap | close | pin $2k+ | 200-237 | 45.8 | -0.3 | -3.9 |  |
| sharp_gap | close | pin limit <$1k | 112-117 | 48.9 | -1.0 | -2.3 |  |
| money_moving | close | 1-3k bets | 496-587 | 45.8 | -2.1 | -9.1 |  |
| money_moving | close | 3k+ bets | 185-199 | 48.2 | 0.6 | 1.9 |  |
| money_moving | close | <1k bets | 112-137 | 45.0 | -2.5 | -13.5 |  |
| money_moving | close | pin $1-2k | 255-290 | 46.8 | -2.2 | -6.5 |  |
| money_moving | close | pin $2k+ | 201-235 | 46.1 | 0.0 | -3.8 |  |
| money_moving | close | pin limit <$1k | 108-123 | 46.8 | -3.1 | -6.4 |  |
| pin_value | close | 1-3k bets | 204-224 | 47.7 | 0.1 | -1.5 |  |
| pin_value | close | 3k+ bets | 72-77 | 48.3 | 0.4 | -4.9 |  |
| pin_value | close | <1k bets | 54-44 | 55.1 | 8.2 | 10.6 |  |
| pin_value | close | pin $1-2k | 153-177 | 46.4 | -1.7 | -5.7 |  |
| pin_value | close | pin $2k+ | 90-106 | 45.9 | 0.7 | -2.5 |  |
| pin_value | close | pin limit <$1k | 87-62 | 58.4 | 8.9 | 13.7 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 48.1 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 48.1 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 201-270 | 42.7 | -4.7 | -13.0 |  |
| consensus_gap | close | 3k+ bets | 78-89 | 46.7 | -0.2 | 7.3 |  |
| consensus_gap | close | <1k bets | 40-78 | 33.9 | -9.5 | -30.7 |  |
| consensus_gap | close | pin $1-2k | 102-118 | 46.4 | -2.5 | -3.1 |  |
| consensus_gap | close | pin $2k+ | 80-96 | 45.5 | -2.7 | -3.3 |  |
| consensus_gap | close | pin limit <$1k | 47-43 | 52.2 | 2.3 | 2.2 |  |
| consensus_gap+follow_move | close | 1-3k bets | 84-77 | 52.2 | 0.8 | -1.5 |  |
| consensus_gap+money_level | close | 1-3k bets | 133-91 | 59.4 | 0.5 | 1.7 |  |
| consensus_gap+money_moving | close | 1-3k bets | 93-148 | 38.6 | -6.1 | -10.6 |  |
| consensus_gap+pin_move | close | 1-3k bets | 48-48 | 50.0 | -0.7 | 3.7 |  |
| consensus_gap+pin_value | close | 1-3k bets | 78-99 | 44.1 | -1.1 | -5.0 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 91-151 | 37.6 | -6.2 | -11.8 |  |
| follow_move+money_level | close | 1-3k bets | 357-239 | 59.9 | 3.6 | -2.1 |  |
| follow_move+money_moving | close | 1-3k bets | 293-308 | 48.8 | -0.6 | -6.6 |  |
| follow_move+pin_move | close | 1-3k bets | 211-210 | 50.1 | 0.1 | -4.7 |  |
| follow_move+pin_value | close | 1-3k bets | 68-71 | 48.9 | 0.5 | -7.2 |  |
| follow_move+sharp_gap | close | 1-3k bets | 294-305 | 49.1 | 0.0 | -5.0 |  |
| money_level+money_moving | close | 1-3k bets | 361-316 | 53.3 | 0.8 | -3.0 |  |
| money_level+pin_move | close | 1-3k bets | 180-163 | 52.5 | -0.2 | -4.4 |  |
| money_level+pin_value | close | 1-3k bets | 100-96 | 51.0 | 1.5 | -4.3 |  |
| money_level+sharp_gap | close | 1-3k bets | 352-311 | 53.1 | 0.9 | -2.5 |  |
| money_moving+pin_move | close | 1-3k bets | 180-198 | 47.6 | -1.4 | -4.2 |  |
| money_moving+pin_value | close | 1-3k bets | 93-117 | 44.3 | -2.8 | -7.3 |  |
| money_moving+sharp_gap | close | 1-3k bets | 472-562 | 45.6 | -1.9 | -8.2 |  |
| pin_move+pin_value | close | 1-3k bets | 91-94 | 49.2 | 0.2 | -2.7 |  |
| pin_move+sharp_gap | close | 1-3k bets | 186-198 | 48.4 | -0.4 | -2.2 |  |
| pin_value+sharp_gap | close | 1-3k bets | 96-121 | 44.2 | -2.7 | -7.6 |  |
| consensus_gap+money_delta | close | 1-3k bets | 25-63 | 28.4 | -8.7 | -22.4 |  |
| follow_move+money_delta | close | 1-3k bets | 91-106 | 46.2 | -0.7 | -8.1 |  |
| money_delta+money_level | close | 1-3k bets | 70-67 | 51.1 | 2.9 | 6.3 |  |
| money_delta+money_moving | close | 1-3k bets | 130-190 | 40.6 | -2.6 | -11.1 |  |
| money_delta+pin_value | close | 1-3k bets | 43-44 | 49.4 | 2.0 | -0.8 |  |
| money_delta+sharp_gap | close | 1-3k bets | 129-188 | 40.7 | -2.6 | -10.9 |  |
| book_lag+money_delta | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | 1-3k bets | 64-77 | 45.4 | -2.2 | -3.4 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 17-26 | 39.5 | 2.0 | 19.2 |  |
| money_level+pin_rlm | close | 1-3k bets | 36-28 | 56.2 | 7.8 | 8.3 |  |
| pin_move+pin_rlm | close | 1-3k bets | 73-75 | 49.3 | 4.6 | 9.7 |  |
| pin_rlm+pin_value | close | 1-3k bets | 28-24 | 53.8 | 7.7 | 29.6 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 80-91 | 46.8 | 4.3 | 14.4 |  |
| money_delta+pin_rlm | close | 1-3k bets | 43-53 | 44.8 | 1.2 | 7.8 |  |
| money_moving+pin_rlm | close | 1-3k bets | 75-88 | 46.0 | 3.5 | 13.9 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 19-30 | 38.8 | -1.2 | 4.1 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 122-149 | 45.0 | 0.4 | -2.9 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 64-76 | 45.7 | -0.3 | -7.6 |  |
| money_level+rlm_ratio | close | 1-3k bets | 58-55 | 51.3 | 1.6 | -0.9 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 116-145 | 44.4 | -0.3 | -3.7 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 122-149 | 45.0 | 0.4 | -2.9 |  |
| follow_move+pin_rlm | close | 1-3k bets | 59-69 | 46.1 | 1.5 | -3.9 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 64-64 | 50.0 | 4.0 | 3.5 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 59-69 | 46.1 | 1.5 | -3.9 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 25-21 | 54.3 | 6.3 | 4.5 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 49.0 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 29-27 | 51.8 | 1.8 | 1.4 |  |
| consensus_gap+money_moving | close | 3k+ bets | 33-49 | 40.2 | -3.2 | 18.7 |  |
| consensus_gap+pin_move | close | 3k+ bets | 20-18 | 52.6 | 2.5 | 6.4 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-6 | 33.3 | -5.9 | 6.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 33-31 | 51.6 | 6.0 | 6.3 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -0.2 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 34-49 | 41.0 | -2.3 | 21.9 |  |
| follow_move+money_moving | close | 3k+ bets | 90-96 | 48.4 | -1.2 | -4.9 |  |
| follow_move+pin_move | close | 3k+ bets | 80-82 | 49.4 | -1.0 | -3.9 |  |
| follow_move+pin_rlm | close | 3k+ bets | 27-24 | 52.9 | 9.1 | 18.2 |  |
| follow_move+pin_value | close | 3k+ bets | 28-28 | 50.0 | 0.5 | -6.1 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 42-37 | 53.2 | 8.7 | 14.4 |  |
| follow_move+sharp_gap | close | 3k+ bets | 92-95 | 49.2 | 0.1 | -2.6 |  |
| money_moving+pin_move | close | 3k+ bets | 63-72 | 46.7 | -1.4 | -6.5 |  |
| money_moving+pin_rlm | close | 3k+ bets | 28-36 | 43.8 | 2.4 | -3.0 |  |
| money_moving+pin_value | close | 3k+ bets | 34-41 | 45.3 | -0.9 | -5.6 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 40-35 | 53.3 | 8.9 | 15.3 |  |
| money_moving+sharp_gap | close | 3k+ bets | 178-189 | 48.5 | 1.2 | 3.4 |  |
| pin_move+pin_rlm | close | 3k+ bets | 29-30 | 49.2 | 6.0 | 8.6 |  |
| pin_move+pin_value | close | 3k+ bets | 29-34 | 46.0 | -3.0 | -13.2 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 31-25 | 55.4 | 10.5 | 21.1 |  |
| pin_move+sharp_gap | close | 3k+ bets | 63-71 | 47.0 | -0.7 | -5.0 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-10 | 33.3 | -10.8 | -36.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 27-24 | 52.9 | 9.1 | 18.2 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 29-36 | 44.6 | 3.1 | -1.5 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 7-6 | 53.8 | 3.7 | 1.4 |  |
| pin_value+sharp_gap | close | 3k+ bets | 34-39 | 46.6 | 0.4 | -3.0 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 42-37 | 53.2 | 8.7 | 14.4 |  |
| follow_move+money_delta | close | 3k+ bets | 36-40 | 47.4 | 2.2 | -1.4 |  |
| money_level+money_moving | close | 3k+ bets | 126-111 | 53.2 | 0.8 | -1.4 |  |
| money_level+sharp_gap | close | 3k+ bets | 125-108 | 53.6 | 1.5 | 0.3 |  |
| follow_move+money_level | close | 3k+ bets | 109-85 | 56.2 | -0.9 | -5.2 |  |
| money_level+rlm_ratio | close | 3k+ bets | 22-11 | 66.7 | 19.4 | 37.4 |  |
| consensus_gap+money_level | close | 3k+ bets | 42-39 | 51.9 | -4.7 | -10.4 |  |
| money_level+pin_move | close | 3k+ bets | 58-59 | 49.6 | -4.1 | -9.2 |  |
| money_level+pin_value | close | 3k+ bets | 38-39 | 49.4 | -0.3 | -8.6 |  |
| money_delta+money_moving | close | 3k+ bets | 58-73 | 44.3 | 2.6 | 7.6 |  |
| consensus_gap+money_delta | close | 3k+ bets | 12-23 | 34.3 | -3.5 | 18.4 |  |
| money_delta+sharp_gap | close | 3k+ bets | 56-70 | 44.4 | 2.9 | 8.6 |  |
| money_delta+money_level | close | 3k+ bets | 30-20 | 60.0 | 13.6 | 21.5 |  |
| money_level+pin_rlm | close | 3k+ bets | 14-8 | 63.6 | 18.6 | 37.8 |  |
| money_delta+pin_value | close | 3k+ bets | 18-16 | 52.9 | 7.5 | -0.2 |  |
| money_delta+pin_move | close | 3k+ bets | 33-35 | 48.5 | 4.1 | -0.5 |  |
| money_delta+pin_rlm | close | 3k+ bets | 20-22 | 47.6 | 6.9 | 2.1 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 27-18 | 60.0 | 16.1 | 28.3 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 48.1 | 87.7 |  |
| money_level+money_moving | close | <1k bets | 76-77 | 49.7 | -3.0 | -14.4 |  |
| money_level+sharp_gap | close | <1k bets | 79-77 | 50.6 | -2.4 | -13.9 |  |
| money_moving+sharp_gap | close | <1k bets | 110-135 | 44.9 | -2.8 | -14.7 |  |
| consensus_gap+money_level | close | <1k bets | 18-27 | 40.0 | -16.1 | -39.4 |  |
| consensus_gap+money_moving | close | <1k bets | 17-40 | 29.8 | -11.4 | -34.9 |  |
| consensus_gap+pin_move | close | <1k bets | 6-13 | 31.6 | -18.3 | -26.5 |  |
| consensus_gap+pin_value | close | <1k bets | 14-14 | 50.0 | 8.4 | 15.4 |  |
| consensus_gap+sharp_gap | close | <1k bets | 17-41 | 29.3 | -11.7 | -36.0 |  |
| money_level+pin_move | close | <1k bets | 34-35 | 49.3 | -5.4 | -13.5 |  |
| money_level+pin_value | close | <1k bets | 18-17 | 51.4 | 1.3 | -4.2 |  |
| money_moving+pin_move | close | <1k bets | 36-41 | 46.8 | -1.3 | -4.2 |  |
| money_moving+pin_value | close | <1k bets | 17-16 | 51.5 | 6.2 | 14.9 |  |
| pin_move+pin_value | close | <1k bets | 25-20 | 55.6 | 7.3 | 12.9 |  |
| pin_move+sharp_gap | close | <1k bets | 36-42 | 46.2 | -2.6 | -9.5 |  |
| pin_value+sharp_gap | close | <1k bets | 17-15 | 53.1 | 7.2 | 18.5 |  |
| follow_move+money_delta | close | <1k bets | 18-20 | 47.4 | 4.8 | -3.2 |  |
| follow_move+money_moving | close | <1k bets | 54-63 | 46.2 | -3.7 | -13.8 |  |
| follow_move+pin_move | close | <1k bets | 42-42 | 50.0 | -1.6 | -7.2 |  |
| follow_move+sharp_gap | close | <1k bets | 56-63 | 47.1 | -3.6 | -16.1 |  |
| money_delta+money_moving | close | <1k bets | 27-46 | 37.0 | -2.9 | -23.1 |  |
| money_delta+pin_move | close | <1k bets | 13-17 | 43.3 | -0.6 | -15.5 |  |
| money_delta+sharp_gap | close | <1k bets | 27-46 | 37.0 | -2.9 | -23.1 |  |
| follow_move+rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.8 | 0.8 |  |
| money_delta+rlm_ratio | close | <1k bets | 16-15 | 51.6 | 10.0 | 6.3 |  |
| money_moving+rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.8 | 0.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 26-26 | 50.0 | 6.8 | 0.8 |  |
| follow_move+money_level | close | <1k bets | 75-59 | 56.0 | -2.7 | -15.1 |  |
| consensus_gap+money_delta | close | <1k bets | 4-22 | 15.4 | -15.9 | -63.0 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -0.6 | 12.2 |  |
| money_delta+pin_rlm | close | <1k bets | 12-14 | 46.2 | 8.1 | -0.2 |  |
| money_moving+pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| pin_rlm+sharp_gap | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| money_delta+pin_value | close | <1k bets | 6-8 | 42.9 | -2.9 | -19.4 |  |
| consensus_gap+follow_move | close | <1k bets | 9-20 | 31.0 | -19.2 | -51.4 |  |
| follow_move+pin_rlm | close | <1k bets | 16-11 | 59.3 | 16.1 | 17.3 |  |
| follow_move+pin_value | close | <1k bets | 18-12 | 60.0 | 11.2 | 13.8 |  |
| pin_move+pin_rlm | close | <1k bets | 19-16 | 54.3 | 10.8 | 15.0 |  |
| pin_move+rlm_ratio | close | <1k bets | 16-13 | 55.2 | 9.9 | 7.8 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 21.3 | 60.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 16-11 | 59.3 | 16.1 | 17.3 |  |
| pin_value+rlm_ratio | close | <1k bets | 4-1 | 80.0 | 30.1 | 51.7 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 2-7 | 22.2 | -11.4 | -57.2 |  |
| money_delta+money_level | close | <1k bets | 12-17 | 41.4 | -2.2 | -18.9 |  |
| money_level+rlm_ratio | close | <1k bets | 13-13 | 50.0 | 4.4 | -1.9 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 17.5 | 19.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 39-45 | 46.4 | -5.6 | -10.9 |  |
| consensus_gap+money_moving | close | pin $1-2k | 52-64 | 44.8 | -3.6 | -4.1 |  |
| consensus_gap+pin_move | close | pin $1-2k | 40-42 | 48.8 | -3.7 | 3.9 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-18 | 41.9 | 1.4 | 25.8 |  |
| consensus_gap+pin_value | close | pin $1-2k | 59-70 | 45.7 | 0.2 | -7.7 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-14 | 50.0 | 4.7 | 9.0 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 50-62 | 44.6 | -2.4 | -3.2 |  |
| follow_move+money_moving | close | pin $1-2k | 145-175 | 45.3 | -4.6 | -11.0 |  |
| follow_move+pin_move | close | pin $1-2k | 156-160 | 49.4 | -1.5 | -5.2 |  |
| follow_move+pin_rlm | close | pin $1-2k | 45-42 | 51.7 | 6.1 | 10.0 |  |
| follow_move+pin_value | close | pin $1-2k | 52-61 | 46.0 | -3.4 | -13.3 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 64-65 | 49.6 | 3.4 | 4.7 |  |
| follow_move+sharp_gap | close | pin $1-2k | 148-173 | 46.1 | -3.7 | -9.9 |  |
| money_moving+pin_move | close | pin $1-2k | 136-151 | 47.4 | -2.0 | -4.1 |  |
| money_moving+pin_rlm | close | pin $1-2k | 52-55 | 48.6 | 4.8 | 12.8 |  |
| money_moving+pin_value | close | pin $1-2k | 62-91 | 40.5 | -7.2 | -20.5 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 62-62 | 50.0 | 3.4 | 5.4 |  |
| money_moving+sharp_gap | close | pin $1-2k | 247-278 | 47.0 | -1.7 | -5.8 |  |
| pin_move+pin_rlm | close | pin $1-2k | 52-51 | 50.5 | 5.5 | 13.5 |  |
| pin_move+pin_value | close | pin $1-2k | 67-83 | 44.7 | -5.0 | -13.6 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 53-46 | 53.5 | 6.7 | 11.5 |  |
| pin_move+sharp_gap | close | pin $1-2k | 139-150 | 48.1 | -1.1 | -3.1 |  |
| pin_rlm+pin_value | close | pin $1-2k | 14-21 | 40.0 | -8.2 | -16.1 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 45-42 | 51.7 | 6.1 | 10.0 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 55-57 | 49.1 | 5.6 | 13.3 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 16-17 | 48.5 | -1.4 | -8.9 |  |
| pin_value+sharp_gap | close | pin $1-2k | 62-89 | 41.1 | -6.6 | -19.4 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 64-65 | 49.6 | 3.4 | 4.7 |  |
| follow_move+money_level | close | pin $1-2k | 172-163 | 51.3 | -3.1 | -10.0 |  |
| money_level+rlm_ratio | close | pin $1-2k | 39-31 | 55.7 | 7.1 | 8.7 |  |
| money_level+sharp_gap | close | pin $1-2k | 188-187 | 50.1 | -1.6 | -6.8 |  |
| money_level+money_moving | close | pin $1-2k | 188-191 | 49.6 | -2.3 | -7.8 |  |
| consensus_gap+money_level | close | pin $1-2k | 58-55 | 51.3 | -5.8 | -9.7 |  |
| money_level+pin_value | close | pin $1-2k | 67-75 | 47.2 | -2.7 | -11.8 |  |
| money_level+pin_move | close | pin $1-2k | 135-128 | 51.3 | -1.6 | -6.5 |  |
| money_level+pin_rlm | close | pin $1-2k | 27-21 | 56.2 | 9.9 | 10.7 |  |
| follow_move+money_delta | close | pin $1-2k | 52-50 | 51.0 | 5.1 | 5.6 |  |
| money_delta+money_moving | close | pin $1-2k | 71-84 | 45.8 | 1.6 | -1.4 |  |
| money_delta+pin_move | close | pin $1-2k | 53-57 | 48.2 | 0.8 | 1.1 |  |
| money_delta+pin_rlm | close | pin $1-2k | 33-37 | 47.1 | 4.1 | 8.1 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 40-36 | 52.6 | 6.9 | 11.4 |  |
| money_delta+sharp_gap | close | pin $1-2k | 71-82 | 46.4 | 2.2 | -0.1 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 48.1 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 39-35 | 52.7 | 4.9 | 2.7 |  |
| consensus_gap+money_delta | close | pin $1-2k | 16-25 | 39.0 | -1.6 | -7.9 |  |
| money_delta+pin_value | close | pin $1-2k | 37-40 | 48.1 | -0.5 | -9.2 |  |
| follow_move+money_level | close | pin $2k+ | 129-80 | 61.7 | 1.8 | -2.0 |  |
| follow_move+money_moving | close | pin $2k+ | 97-99 | 49.5 | 1.7 | -5.4 |  |
| follow_move+pin_move | close | pin $2k+ | 119-115 | 50.9 | 1.1 | -4.2 |  |
| follow_move+sharp_gap | close | pin $2k+ | 98-100 | 49.5 | 1.8 | -5.1 |  |
| money_level+money_moving | close | pin $2k+ | 134-121 | 52.5 | -0.4 | -4.5 |  |
| money_level+pin_move | close | pin $2k+ | 90-83 | 52.0 | -3.1 | -8.5 |  |
| money_level+sharp_gap | close | pin $2k+ | 134-122 | 52.3 | -0.6 | -4.5 |  |
| money_moving+pin_move | close | pin $2k+ | 86-101 | 46.0 | -0.7 | -7.4 |  |
| money_moving+sharp_gap | close | pin $2k+ | 195-231 | 45.8 | -0.2 | -3.7 |  |
| pin_move+sharp_gap | close | pin $2k+ | 86-102 | 45.7 | -0.9 | -7.4 |  |
| consensus_gap+money_delta | close | pin $2k+ | 7-25 | 21.9 | -9.3 | -56.9 |  |
| consensus_gap+money_moving | close | pin $2k+ | 29-56 | 34.1 | -7.4 | -5.3 |  |
| consensus_gap+pin_value | close | pin $2k+ | 33-43 | 43.4 | 2.9 | 9.2 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 31-59 | 34.4 | -7.8 | -4.8 |  |
| money_delta+money_moving | close | pin $2k+ | 51-75 | 40.5 | 2.2 | -10.1 |  |
| money_delta+pin_value | close | pin $2k+ | 17-20 | 45.9 | 4.2 | -12.2 |  |
| money_delta+sharp_gap | close | pin $2k+ | 49-74 | 39.8 | 1.4 | -11.3 |  |
| money_moving+pin_value | close | pin $2k+ | 49-58 | 45.8 | 1.9 | 7.2 |  |
| pin_value+sharp_gap | close | pin $2k+ | 49-59 | 45.4 | 1.6 | 6.2 |  |
| consensus_gap+pin_move | close | pin $2k+ | 21-27 | 43.8 | -4.3 | -16.7 |  |
| money_delta+pin_move | close | pin $2k+ | 28-43 | 39.4 | -2.2 | -18.2 |  |
| consensus_gap+follow_move | close | pin $2k+ | 24-24 | 50.0 | -0.7 | -16.6 |  |
| follow_move+pin_value | close | pin $2k+ | 29-27 | 51.8 | 5.2 | -1.5 |  |
| pin_move+pin_value | close | pin $2k+ | 40-41 | 49.4 | 2.2 | -2.1 |  |
| follow_move+money_delta | close | pin $2k+ | 28-36 | 43.8 | 1.9 | -8.5 |  |
| follow_move+pin_rlm | close | pin $2k+ | 25-41 | 37.9 | 0.4 | -12.6 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 35-50 | 41.2 | 3.0 | -8.9 |  |
| money_delta+money_level | close | pin $2k+ | 22-18 | 55.0 | 10.5 | 11.8 |  |
| money_delta+pin_rlm | close | pin $2k+ | 18-36 | 33.3 | -1.7 | -14.4 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 18-22 | 45.0 | 6.4 | -1.7 |  |
| money_level+pin_rlm | close | pin $2k+ | 13-9 | 59.1 | 16.6 | 26.7 |  |
| money_level+pin_value | close | pin $2k+ | 48-45 | 51.6 | 2.1 | -4.7 |  |
| money_level+rlm_ratio | close | pin $2k+ | 13-11 | 54.2 | 7.2 | 14.2 |  |
| money_moving+pin_rlm | close | pin $2k+ | 34-64 | 34.7 | -0.3 | -6.1 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 35-49 | 41.7 | 3.3 | -7.8 |  |
| pin_move+pin_rlm | close | pin $2k+ | 29-43 | 40.3 | 2.7 | -4.6 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 26-35 | 42.6 | 3.0 | -2.2 |  |
| pin_rlm+pin_value | close | pin $2k+ | 5-13 | 27.8 | -6.6 | 9.3 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 25-41 | 37.9 | 0.4 | -12.6 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 34-64 | 34.7 | -0.3 | -6.1 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 4-6 | 40.0 | -0.6 | -19.0 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 35-50 | 41.2 | 3.0 | -8.9 |  |
| consensus_gap+money_level | close | pin $2k+ | 52-38 | 57.8 | -4.9 | -10.1 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-19 | 17.4 | -10.6 | -24.8 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-11 | 0.0 | -28.1 | -100.0 |  |
| follow_move+money_delta | close | pin limit <$1k | 31-36 | 46.3 | -4.0 | -11.2 |  |
| money_level+money_moving | close | pin limit <$1k | 66-74 | 47.1 | -2.7 | -9.5 |  |
| money_level+sharp_gap | close | pin limit <$1k | 66-70 | 48.5 | -1.4 | -6.8 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 102-110 | 48.1 | -1.8 | -3.5 |  |
| consensus_gap+money_level | close | pin limit <$1k | 25-25 | 50.0 | -0.3 | -7.8 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 13-10 | 56.5 | 8.3 | 25.1 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 33-31 | 51.6 | 2.6 | 3.9 |  |
| follow_move+money_moving | close | pin limit <$1k | 63-72 | 46.7 | -3.3 | -10.3 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 68-71 | 48.9 | -1.0 | -6.0 |  |
| money_level+pin_move | close | pin limit <$1k | 47-46 | 50.5 | 0.5 | -3.5 |  |
| money_level+pin_value | close | pin limit <$1k | 41-32 | 56.2 | 6.8 | 6.3 |  |
| pin_move+pin_value | close | pin limit <$1k | 38-24 | 61.3 | 12.0 | 23.6 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 16-10 | 61.5 | 11.4 | 12.5 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 20-17 | 54.1 | 5.3 | 14.0 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 22-18 | 55.0 | 6.0 | 14.8 |  |
| follow_move+money_level | close | pin limit <$1k | 52-54 | 49.1 | -1.2 | -6.6 |  |
| follow_move+pin_move | close | pin limit <$1k | 58-59 | 49.6 | -0.5 | -5.1 |  |
| follow_move+pin_value | close | pin limit <$1k | 33-23 | 58.9 | 9.3 | 11.8 |  |
| money_moving+pin_move | close | pin limit <$1k | 57-59 | 49.1 | -0.8 | -2.2 |  |
| money_moving+pin_value | close | pin limit <$1k | 33-25 | 56.9 | 7.7 | 15.6 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 60-59 | 50.4 | 0.4 | 0.2 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 36-27 | 57.1 | 7.7 | 15.5 |  |
| money_delta+money_moving | close | pin limit <$1k | 43-43 | 50.0 | -0.0 | 0.9 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 7-6 | 53.8 | 5.9 | 35.2 |  |
| money_delta+money_level | close | pin limit <$1k | 25-19 | 56.8 | 6.3 | 8.8 |  |
| money_delta+pin_value | close | pin limit <$1k | 13-8 | 61.9 | 13.1 | 38.5 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 42-41 | 50.6 | 0.6 | 2.1 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 29-29 | 50.0 | 0.1 | 3.4 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 6-2 | 75.0 | 28.4 | 96.7 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 24-16 | 60.0 | 10.5 | 26.0 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 38-26 | 59.4 | 9.9 | 27.7 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 40-27 | 59.7 | 9.8 | 21.0 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-3 | 86.4 | 37.2 | 84.9 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 41-27 | 60.3 | 10.7 | 28.6 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 32-21 | 60.4 | 10.1 | 16.1 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 44-32 | 57.9 | 7.9 | 11.8 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 25-20 | 55.6 | 5.3 | 6.8 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 40-31 | 56.3 | 6.3 | 8.9 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 32-21 | 60.4 | 10.1 | 16.1 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 32-21 | 60.4 | 10.1 | 16.1 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 44-32 | 57.9 | 7.9 | 11.8 |  |
| money_level+pin_rlm | close | pin limit <$1k | 19-12 | 61.3 | 10.5 | 17.6 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 21-14 | 60.0 | 10.0 | 16.8 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 16-5 | 76.2 | 25.8 | 46.1 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 5-3 | 62.5 | 12.8 | 18.4 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 49.0 | 87.7 |  |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -49.0 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 5-8 | 38.5 | -9.6 | -31.5 | 0.32 |
| pin_move | early | pin $1-2k | 0-3 | 0.0 | -34.5 | -100.0 | 0.23 |
| pin_move | early | pin limit <$1k | 5-6 | 45.5 | -6.4 | -19.1 | 0.22 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 17.0 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 8-4 | 66.7 | 26.3 | 47.8 | -0.56 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -38.8 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 4-0 | 100.0 | 50.2 | 88.0 | -0.25 |
| pin_rlm | early | <1k bets | 1-2 | 33.3 | 7.6 | -35.8 | -1.0 |
| pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -25.8 | -100.0 | -1.75 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.2 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -50.4 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 380-315 | 54.7 | 2.2 | -5.4 | 0.24 |
| follow_move | early | pin $1-2k | 27-16 | 62.8 | 8.3 | 11.9 | -0.35 |
| follow_move | early | pin limit <$1k | 47-39 | 54.7 | 4.4 | 1.9 | -0.11 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 24.0 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -51.9 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 19-12 | 61.3 | 25.9 | 38.7 | 0.54 |
| rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.8 | 55.6 | -1.52 |
| rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 0.6 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 42.2 | 59.7 | 0.33 |
| money_level | early | <1k bets | 133-80 | 62.4 | 2.4 | -2.7 | -0.11 |
| money_level | early | pin $1-2k | 20-8 | 71.4 | 5.2 | 4.1 | 0.01 |
| money_level | early | pin limit <$1k | 24-26 | 48.0 | -5.4 | -11.4 | 0.22 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.6 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 7.6 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 108-91 | 54.3 | 5.8 | 3.6 | 0.29 |
| sharp_gap | early | pin $1-2k | 15-11 | 57.7 | 4.7 | 6.7 | -0.39 |
| sharp_gap | early | pin limit <$1k | 29-18 | 61.7 | 13.1 | 27.9 | 0.12 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.4 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.4 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 75-60 | 55.6 | 3.3 | -3.5 | 0.04 |
| money_moving | early | pin $1-2k | 8-8 | 50.0 | -8.9 | -31.4 | 0.21 |
| money_moving | early | pin limit <$1k | 23-9 | 71.9 | 22.7 | 52.0 | 0.42 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.6 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 51.9 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 36-39 | 48.0 | -0.2 | -9.2 | 0.13 |
| pin_value | early | pin $1-2k | 13-18 | 41.9 | -3.7 | -21.1 | 0.12 |
| pin_value | early | pin limit <$1k | 36-30 | 54.5 | 5.0 | 3.2 | 0.09 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -49.0 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -26.6 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.3 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 13.0 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 172-228 | 43.0 | -4.1 | -13.9 | 0.35 |
| consensus_gap | early | pin $1-2k | 12-20 | 37.5 | -7.7 | -28.2 | 0.51 |
| consensus_gap | early | pin limit <$1k | 18-34 | 34.6 | -15.5 | -28.2 | 0.28 |
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -51.9 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 17.0 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 17.0 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -0.4 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 16.7 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 4.2 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 3.8 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.6 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.5 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.3 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -49.0 | -100.0 | -1.0 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -1.1 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 3.6 | -6.9 | 0.3 |
| follow_move+pin_value | early | 1-3k bets | 7-6 | 53.8 | 6.4 | 0.8 | -0.31 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.8 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.2 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 2.4 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.5 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 24.0 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.5 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 24.0 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.0 | 25.3 | 0.18 |
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.4 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.8 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.4 | 85.1 | 0.0 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 19.3 | 18.8 | -0.24 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -25.8 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 51.9 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 51.9 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 51.9 | 83.3 | 1.0 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -51.9 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -51.9 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.4 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 51.9 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 51.9 | 83.3 | 1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -51.9 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 37.4 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 49.0 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 24-30 | 44.4 | -7.6 | -18.9 | 0.95 |
| consensus_gap+money_level | early | <1k bets | 26-19 | 57.8 | -8.1 | -9.5 | 0.31 |
| consensus_gap+sharp_gap | early | <1k bets | 20-37 | 35.1 | -10.5 | -20.9 | 1.05 |
| follow_move+money_level | early | <1k bets | 71-30 | 70.3 | 8.6 | 3.0 | 0.1 |
| follow_move+sharp_gap | early | <1k bets | 56-26 | 68.3 | 17.9 | 20.1 | 0.48 |
| money_level+sharp_gap | early | <1k bets | 76-44 | 63.3 | 6.8 | 3.1 | 0.14 |
| follow_move+money_moving | early | <1k bets | 38-20 | 65.5 | 11.1 | 12.2 | 0.45 |
| money_level+money_moving | early | <1k bets | 48-30 | 61.5 | 2.3 | -2.6 | -0.24 |
| money_moving+sharp_gap | early | <1k bets | 44-36 | 55.0 | 5.4 | -0.5 | 0.13 |
| consensus_gap+money_moving | early | <1k bets | 10-18 | 35.7 | -12.4 | -42.4 | 0.2 |
| follow_move+pin_value | early | <1k bets | 13-11 | 54.2 | 4.6 | 1.3 | -0.01 |
| follow_move+rlm_ratio | early | <1k bets | 19-12 | 61.3 | 25.9 | 38.7 | 0.54 |
| rlm_ratio+sharp_gap | early | <1k bets | 19-12 | 61.3 | 25.9 | 38.7 | 0.54 |
| pin_move+pin_value | early | <1k bets | 1-4 | 20.0 | -29.1 | -61.8 | 0.2 |
| follow_move+pin_move | early | <1k bets | 5-3 | 62.5 | 9.9 | 11.2 | 0.42 |
| consensus_gap+pin_value | early | <1k bets | 13-23 | 36.1 | -10.3 | -32.5 | 0.4 |
| money_delta+money_moving | early | <1k bets | 7-4 | 63.6 | 24.3 | 43.8 | -0.61 |
| money_delta+sharp_gap | early | <1k bets | 6-3 | 66.7 | 29.9 | 54.6 | -0.74 |
| consensus_gap+pin_move | early | <1k bets | 0-5 | 0.0 | -44.4 | -100.0 | 0.26 |
| money_level+pin_move | early | <1k bets | 2-2 | 50.0 | -5.8 | -21.8 | 0.1 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | <1k bets | 3-3 | 50.0 | 11.6 | 3.0 | 0.87 |
| follow_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 24.2 | -3.7 | -2.15 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 24.2 | -3.7 | -2.15 |
| pin_rlm+sharp_gap | early | <1k bets | 1-2 | 33.3 | 7.6 | -35.8 | -1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 11.6 | -4.5 | -1.9 |
| pin_value+sharp_gap | early | <1k bets | 5-4 | 55.6 | 8.6 | 6.1 | -0.09 |
| money_level+pin_value | early | <1k bets | 4-4 | 50.0 | 0.3 | -4.5 | 0.88 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -51.4 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -51.0 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 1-2 | 33.3 | -17.3 | -36.4 | 1.33 |
| money_level+rlm_ratio | early | <1k bets | 7-5 | 58.3 | 22.2 | 22.3 | 1.67 |
| money_moving+rlm_ratio | early | <1k bets | 8-4 | 66.7 | 26.6 | 56.4 | 0.34 |
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 51.0 | 90.9 | 0.0 |
| money_delta+money_level | early | <1k bets | 3-0 | 100.0 | 58.1 | 115.3 | 0.93 |
| pin_move+sharp_gap | early | <1k bets | 2-1 | 66.7 | 17.0 | 4.3 | -0.07 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 3-2 | 60.0 | 24.1 | 65.0 | -0.32 |
| money_delta+rlm_ratio | early | <1k bets | 2-0 | 100.0 | 74.2 | 217.0 | 0.3 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 49.0 | 90.9 | -1.0 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -25.8 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 5-4 | 55.6 | -10.0 | -12.6 | 0.71 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -32.2 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 5-10 | 33.3 | -7.8 | -38.7 | 0.31 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.8 | 55.6 | -1.52 |
| follow_move+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 13.6 | 37.5 | -0.83 |
| money_level+money_moving | early | pin $1-2k | 8-5 | 61.5 | -4.9 | -15.6 | 0.07 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.9 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-3 | 40.0 | 3.8 | 55.6 | -1.52 |
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -51.9 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -38.8 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -51.9 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -38.8 | -100.0 | 2.5 |
| money_level+sharp_gap | early | pin $1-2k | 12-4 | 75.0 | 9.9 | 12.5 | -0.26 |
| money_moving+sharp_gap | early | pin $1-2k | 4-6 | 40.0 | -17.1 | -45.4 | 0.08 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.6 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 4-6 | 40.0 | -10.0 | -31.3 | 0.34 |
| follow_move+pin_value | early | pin $1-2k | 6-5 | 54.5 | 7.1 | 0.8 | -0.3 |
| follow_move+money_level | early | pin $1-2k | 11-4 | 73.3 | 7.6 | 6.6 | -0.07 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 48.1 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 4-1 | 80.0 | 11.0 | 6.9 | -0.18 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -16.7 | -46.8 | -0.12 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -25.8 | -100.0 | -1.75 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | -4.8 |
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -25.8 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.8 | -100.0 | 1.3 |
| money_level+money_moving | early | pin limit <$1k | 13-7 | 65.0 | 12.5 | 20.2 | 0.48 |
| money_level+sharp_gap | early | pin limit <$1k | 20-16 | 55.6 | 4.8 | 1.6 | 0.14 |
| money_moving+sharp_gap | early | pin limit <$1k | 18-5 | 78.3 | 30.2 | 70.1 | 0.35 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -49.0 | -100.0 | -1.0 |
| money_level+pin_value | early | pin limit <$1k | 9-6 | 60.0 | 9.7 | 13.8 | 0.33 |
| money_moving+pin_value | early | pin limit <$1k | 7-4 | 63.6 | 13.6 | 20.1 | 0.18 |
| pin_value+sharp_gap | early | pin limit <$1k | 12-6 | 66.7 | 16.6 | 26.4 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-9 | 40.0 | -12.1 | -25.7 | 0.53 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -27.0 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 14-18 | 43.8 | -5.1 | -17.9 | 0.43 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.2 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 11-11 | 50.0 | -4.2 | -7.4 | -0.04 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 4.5 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 13-7 | 65.0 | 16.4 | 24.2 | -0.07 |
| follow_move+rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level+rlm_ratio | early | pin limit <$1k | 6-0 | 100.0 | 53.5 | 92.6 | 0.42 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 16.3 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| consensus_gap+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.4 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 22.9 | 72.3 | 0.54 |
| follow_move+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.4 | 85.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 9-3 | 75.0 | 25.4 | 43.3 | 0.33 |
| money_delta+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 50.6 | 87.1 | -0.33 |
| money_delta+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 50.6 | 87.1 | -0.33 |
| money_moving+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.0 | 45.3 | -0.5 |
| money_delta+sharp_gap | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 | -0.5 |
| pin_move+pin_value | early | pin limit <$1k | 1-4 | 20.0 | -29.1 | -61.8 | 0.2 |
| follow_move+pin_move | early | pin limit <$1k | 5-3 | 62.5 | 9.9 | 11.2 | 0.42 |
| consensus_gap+pin_move | early | pin limit <$1k | 0-3 | 0.0 | -56.8 | -100.0 | 0.53 |
| money_level+pin_move | early | pin limit <$1k | 2-2 | 50.0 | -5.8 | -21.8 | 0.1 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -51.0 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -51.0 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 17.0 | 4.3 | -0.07 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 74.2 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 49.0 | 90.9 | -1.0 |
| pin_move | close | 1-3k bets | 14-7 | 66.7 | 17.3 | 37.7 |  |
| pin_move | close | 3k+ bets | 8-9 | 47.1 | -0.2 | -9.6 |  |
| pin_move | close | pin $1-2k | 10-9 | 52.6 | 8.2 | 13.5 |  |
| pin_move | close | pin $2k+ | 9-4 | 69.2 | 15.6 | 30.5 |  |
| pin_move | close | pin limit <$1k | 3-3 | 50.0 | 0.0 | -3.8 |  |
| money_delta | close | 1-3k bets | 9-10 | 47.4 | 6.2 | 3.8 |  |
| money_delta | close | 3k+ bets | 3-9 | 25.0 | -19.1 | -50.5 |  |
| money_delta | close | pin $1-2k | 6-6 | 50.0 | 7.5 | 16.3 |  |
| money_delta | close | pin $2k+ | 5-4 | 55.6 | 11.7 | 8.1 |  |
| money_delta | close | pin limit <$1k | 0-3 | 0.0 | -40.7 | -100.0 |  |
| pin_rlm | close | 1-3k bets | 6-1 | 85.7 | 45.0 | 98.4 |  |
| pin_rlm | close | 3k+ bets | 2-6 | 25.0 | -14.2 | -50.8 |  |
| pin_rlm | close | pin $1-2k | 6-5 | 54.5 | 14.9 | 26.6 |  |
| pin_rlm | close | pin $2k+ | 2-0 | 100.0 | 59.5 | 94.5 |  |
| pin_rlm | close | pin limit <$1k | 0-2 | 0.0 | -40.7 | -100.0 |  |
| follow_move | close | 1-3k bets | 17-17 | 50.0 | -1.4 | -14.6 |  |
| follow_move | close | 3k+ bets | 13-9 | 59.1 | 11.3 | 12.4 |  |
| follow_move | close | pin $1-2k | 8-12 | 40.0 | -7.2 | -29.0 |  |
| follow_move | close | pin $2k+ | 13-3 | 81.2 | 29.6 | 48.8 |  |
| follow_move | close | pin limit <$1k | 1-2 | 33.3 | -13.6 | -36.4 |  |
| rlm_ratio | close | 1-3k bets | 3-5 | 37.5 | -3.2 | -28.4 |  |
| rlm_ratio | close | 3k+ bets | 3-5 | 37.5 | -1.7 | -17.4 |  |
| rlm_ratio | close | pin $1-2k | 4-4 | 50.0 | 7.9 | -4.0 |  |
| rlm_ratio | close | pin $2k+ | 2-0 | 100.0 | 70.8 | 133.0 |  |
| rlm_ratio | close | pin limit <$1k | 0-2 | 0.0 | -40.7 | -100.0 |  |
| money_level | close | 1-3k bets | 28-17 | 62.2 | 4.9 | 6.0 |  |
| money_level | close | 3k+ bets | 19-13 | 59.4 | 2.9 | 8.3 |  |
| money_level | close | <1k bets | 1-0 | 100.0 | 29.2 | 0.5 |  |
| money_level | close | pin $1-2k | 15-8 | 65.2 | 7.4 | 13.6 |  |
| money_level | close | pin $2k+ | 10-10 | 50.0 | -6.4 | -11.8 |  |
| money_level | close | pin limit <$1k | 5-2 | 71.4 | 12.2 | 35.3 |  |
| sharp_gap | close | 1-3k bets | 19-24 | 44.2 | -1.6 | -13.8 |  |
| sharp_gap | close | 3k+ bets | 16-15 | 51.6 | 6.4 | -0.3 |  |
| sharp_gap | close | pin $1-2k | 13-10 | 56.5 | 9.8 | 15.0 |  |
| sharp_gap | close | pin $2k+ | 10-9 | 52.6 | 4.5 | 0.9 |  |
| sharp_gap | close | pin limit <$1k | 3-4 | 42.9 | -0.5 | -17.0 |  |
| money_moving | close | 1-3k bets | 19-24 | 44.2 | -3.3 | -14.1 |  |
| money_moving | close | 3k+ bets | 16-14 | 53.3 | 7.9 | 3.1 |  |
| money_moving | close | pin $1-2k | 13-10 | 56.5 | 9.8 | 15.0 |  |
| money_moving | close | pin $2k+ | 10-9 | 52.6 | 4.5 | 0.9 |  |
| money_moving | close | pin limit <$1k | 2-4 | 33.3 | -19.8 | -36.9 |  |
| pin_value | close | 1-3k bets | 8-3 | 72.7 | 19.2 | 36.8 |  |
| pin_value | close | 3k+ bets | 6-4 | 60.0 | 7.4 | 11.5 |  |
| pin_value | close | pin $1-2k | 6-3 | 66.7 | 14.0 | 25.9 |  |
| pin_value | close | pin $2k+ | 4-3 | 57.1 | 5.2 | 4.3 |  |
| pin_value | close | pin limit <$1k | 4-1 | 80.0 | 24.4 | 51.3 |  |
| consensus_gap | close | 1-3k bets | 5-2 | 71.4 | 22.3 | 21.9 |  |
| consensus_gap | close | 3k+ bets | 3-4 | 42.9 | -10.1 | -16.6 |  |
| consensus_gap | close | pin $1-2k | 3-1 | 75.0 | 28.8 | 40.3 |  |
| consensus_gap | close | pin $2k+ | 1-2 | 33.3 | -23.6 | -29.3 |  |
| consensus_gap | close | pin limit <$1k | 2-0 | 100.0 | 40.7 | 88.9 |  |
| consensus_gap+money_level | close | 1-3k bets | 5-0 | 100.0 | 42.9 | 70.7 |  |
| consensus_gap+money_moving | close | 1-3k bets | 4-2 | 66.7 | 19.2 | 10.4 |  |
| consensus_gap+pin_value | close | 1-3k bets | 4-0 | 100.0 | 46.3 | 88.0 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 4-2 | 66.7 | 19.2 | 10.4 |  |
| follow_move+money_delta | close | 1-3k bets | 4-2 | 66.7 | 18.5 | 28.4 |  |
| money_level+money_moving | close | 1-3k bets | 15-12 | 55.6 | 1.4 | -0.0 |  |
| money_level+pin_value | close | 1-3k bets | 7-2 | 77.8 | 24.3 | 46.8 |  |
| money_level+sharp_gap | close | 1-3k bets | 13-10 | 56.5 | 3.3 | 0.9 |  |
| money_moving+pin_value | close | 1-3k bets | 5-2 | 71.4 | 19.6 | 34.3 |  |
| money_moving+sharp_gap | close | 1-3k bets | 17-22 | 43.6 | -2.7 | -15.0 |  |
| pin_value+sharp_gap | close | 1-3k bets | 4-2 | 66.7 | 16.0 | 25.4 |  |
| money_delta+money_moving | close | 1-3k bets | 6-7 | 46.2 | 9.0 | 6.8 |  |
| money_delta+sharp_gap | close | 1-3k bets | 6-7 | 46.2 | 9.0 | 6.8 |  |
| money_level+pin_move | close | 1-3k bets | 8-5 | 61.5 | 7.9 | 16.2 |  |
| pin_move+pin_value | close | 1-3k bets | 5-1 | 83.3 | 30.9 | 56.5 |  |
| follow_move+money_level | close | 1-3k bets | 9-7 | 56.2 | -3.0 | -12.7 |  |
| follow_move+money_moving | close | 1-3k bets | 6-8 | 42.9 | -4.8 | -18.7 |  |
| follow_move+pin_move | close | 1-3k bets | 7-4 | 63.6 | 14.8 | 19.6 |  |
| follow_move+pin_value | close | 1-3k bets | 2-2 | 50.0 | -0.9 | -6.5 |  |
| follow_move+sharp_gap | close | 1-3k bets | 6-9 | 40.0 | -7.2 | -24.1 |  |
| money_moving+pin_move | close | 1-3k bets | 10-5 | 66.7 | 17.3 | 42.1 |  |
| pin_move+sharp_gap | close | 1-3k bets | 11-4 | 73.3 | 25.2 | 55.1 |  |
| follow_move+pin_rlm | close | 1-3k bets | 3-1 | 75.0 | 34.3 | 43.2 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 3-5 | 37.5 | -3.2 | -28.4 |  |
| money_delta+money_level | close | 1-3k bets | 4-1 | 80.0 | 37.1 | 53.6 |  |
| money_delta+pin_move | close | 1-3k bets | 6-0 | 100.0 | 57.5 | 131.5 |  |
| money_delta+pin_rlm | close | 1-3k bets | 5-0 | 100.0 | 59.4 | 139.6 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 2-0 | 100.0 | 59.3 | 90.9 |  |
| money_level+pin_rlm | close | 1-3k bets | 3-0 | 100.0 | 55.6 | 92.3 |  |
| money_level+rlm_ratio | close | 1-3k bets | 1-0 | 100.0 | 59.3 | 90.9 |  |
| money_moving+pin_rlm | close | 1-3k bets | 6-1 | 85.7 | 45.0 | 98.4 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 3-4 | 42.9 | 2.1 | -18.2 |  |
| pin_move+pin_rlm | close | 1-3k bets | 6-1 | 85.7 | 45.0 | 98.4 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 3-1 | 75.0 | 34.3 | 43.2 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 3-1 | 75.0 | 34.3 | 43.2 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 6-1 | 85.7 | 45.0 | 98.4 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 3-5 | 37.5 | -3.2 | -28.4 |  |
| consensus_gap+follow_move | close | 1-3k bets | 1-0 | 100.0 | 40.7 | 90.9 |  |
| consensus_gap+pin_move | close | 1-3k bets | 2-0 | 100.0 | 46.3 | 87.1 |  |
| money_delta+pin_value | close | 1-3k bets | 1-0 | 100.0 | 48.1 | 90.9 |  |
| pin_rlm+pin_value | close | 1-3k bets | 1-0 | 100.0 | 48.1 | 90.9 |  |
| consensus_gap+money_delta | close | 1-3k bets | 0-2 | 0.0 | -29.2 | -100.0 |  |
| follow_move+money_level | close | 3k+ bets | 7-4 | 63.6 | 8.3 | 11.0 |  |
| follow_move+money_moving | close | 3k+ bets | 7-7 | 50.0 | 5.6 | -0.1 |  |
| follow_move+pin_value | close | 3k+ bets | 3-2 | 60.0 | 8.1 | 10.3 |  |
| follow_move+sharp_gap | close | 3k+ bets | 7-7 | 50.0 | 5.6 | -0.1 |  |
| money_delta+pin_move | close | 3k+ bets | 2-5 | 28.6 | -18.0 | -43.4 |  |
| money_level+money_moving | close | 3k+ bets | 10-6 | 62.5 | 11.3 | 15.5 |  |
| money_level+pin_value | close | 3k+ bets | 5-2 | 71.4 | 14.7 | 31.4 |  |
| money_level+sharp_gap | close | 3k+ bets | 10-6 | 62.5 | 11.3 | 15.5 |  |
| money_moving+pin_value | close | 3k+ bets | 3-3 | 50.0 | -1.3 | -8.1 |  |
| money_moving+sharp_gap | close | 3k+ bets | 16-14 | 53.3 | 7.9 | 3.1 |  |
| pin_value+sharp_gap | close | 3k+ bets | 3-4 | 42.9 | -6.9 | -21.2 |  |
| pin_move+pin_rlm | close | 3k+ bets | 1-6 | 14.3 | -26.4 | -72.1 |  |
| pin_move+pin_value | close | 3k+ bets | 3-3 | 50.0 | -0.1 | -8.1 |  |
| pin_move+sharp_gap | close | 3k+ bets | 4-7 | 36.4 | -10.1 | -32.5 |  |
| pin_rlm+pin_value | close | 3k+ bets | 1-2 | 33.3 | -11.1 | -34.9 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 2-6 | 25.0 | -14.2 | -50.8 |  |
| money_moving+pin_move | close | 3k+ bets | 4-6 | 40.0 | -7.0 | -25.8 |  |
| money_moving+pin_rlm | close | 3k+ bets | 2-5 | 28.6 | -10.4 | -43.8 |  |
| consensus_gap+money_level | close | 3k+ bets | 2-3 | 40.0 | -17.9 | -25.7 |  |
| consensus_gap+money_moving | close | 3k+ bets | 0-1 | 0.0 | -29.2 | -100.0 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 0-1 | 0.0 | -29.2 | -100.0 |  |
| follow_move+money_delta | close | 3k+ bets | 2-5 | 28.6 | -13.7 | -43.4 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 3-5 | 37.5 | -1.7 | -17.4 |  |
| money_delta+money_moving | close | 3k+ bets | 1-7 | 12.5 | -30.5 | -75.2 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 1-5 | 16.7 | -24.0 | -67.0 |  |
| money_delta+sharp_gap | close | 3k+ bets | 1-7 | 12.5 | -30.5 | -75.2 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 3-5 | 37.5 | -1.7 | -17.4 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 3-5 | 37.5 | -1.7 | -17.4 |  |
| money_delta+pin_value | close | 3k+ bets | 0-2 | 0.0 | -50.0 | -100.0 |  |
| follow_move+pin_move | close | 3k+ bets | 7-5 | 58.3 | 11.5 | 11.6 |  |
| follow_move+pin_rlm | close | 3k+ bets | 2-4 | 33.3 | -7.3 | -34.5 |  |
| money_delta+pin_rlm | close | 3k+ bets | 1-4 | 20.0 | -20.6 | -60.4 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 1-4 | 20.0 | -23.0 | -61.0 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 2-4 | 33.3 | -7.3 | -34.5 |  |
| consensus_gap+pin_move | close | 3k+ bets | 1-1 | 50.0 | 0.0 | 6.0 |  |
| money_level+pin_move | close | 3k+ bets | 4-2 | 66.7 | 6.6 | 22.4 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 1-1 | 50.0 | 3.7 | -2.4 |  |
| consensus_gap+follow_move | close | 3k+ bets | 1-0 | 100.0 | 70.8 | 112.0 |  |
| money_delta+money_level | close | 3k+ bets | 0-1 | 0.0 | -51.9 | -100.0 |  |
| money_level+pin_rlm | close | 3k+ bets | 0-1 | 0.0 | -51.9 | -100.0 |  |
| money_level+rlm_ratio | close | 3k+ bets | 0-1 | 0.0 | -51.9 | -100.0 |  |
| consensus_gap+pin_value | close | 3k+ bets | 1-0 | 100.0 | 40.7 | 87.0 |  |
| consensus_gap+money_level | close | pin $1-2k | 3-0 | 100.0 | 48.1 | 87.1 |  |
| consensus_gap+money_moving | close | pin $1-2k | 2-1 | 66.7 | 24.8 | 23.4 |  |
| consensus_gap+pin_value | close | pin $1-2k | 3-0 | 100.0 | 48.1 | 87.1 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 2-1 | 66.7 | 24.8 | 23.4 |  |
| follow_move+money_delta | close | pin $1-2k | 2-4 | 33.3 | -11.1 | -36.4 |  |
| money_level+money_moving | close | pin $1-2k | 9-4 | 69.2 | 15.3 | 26.0 |  |
| money_level+pin_value | close | pin $1-2k | 5-2 | 71.4 | 18.0 | 33.9 |  |
| money_level+sharp_gap | close | pin $1-2k | 9-4 | 69.2 | 15.3 | 26.0 |  |
| money_moving+pin_value | close | pin $1-2k | 3-2 | 60.0 | 12.6 | 13.1 |  |
| money_moving+sharp_gap | close | pin $1-2k | 13-10 | 56.5 | 9.8 | 15.0 |  |
| pin_value+sharp_gap | close | pin $1-2k | 3-2 | 60.0 | 12.6 | 13.1 |  |
| money_delta+money_moving | close | pin $1-2k | 5-5 | 50.0 | 9.4 | 19.8 |  |
| money_delta+sharp_gap | close | pin $1-2k | 5-5 | 50.0 | 9.4 | 19.8 |  |
| follow_move+money_level | close | pin $1-2k | 4-4 | 50.0 | -7.6 | -24.7 |  |
| follow_move+money_moving | close | pin $1-2k | 5-6 | 45.5 | 0.7 | -12.8 |  |
| follow_move+pin_move | close | pin $1-2k | 5-6 | 45.5 | 2.4 | -12.8 |  |
| follow_move+pin_rlm | close | pin $1-2k | 4-4 | 50.0 | 7.9 | -4.0 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 4-4 | 50.0 | 7.9 | -4.0 |  |
| follow_move+sharp_gap | close | pin $1-2k | 5-6 | 45.5 | 0.7 | -12.8 |  |
| money_delta+money_level | close | pin $1-2k | 3-1 | 75.0 | 28.7 | 44.2 |  |
| money_delta+pin_move | close | pin $1-2k | 5-3 | 62.5 | 20.4 | 50.6 |  |
| money_delta+pin_rlm | close | pin $1-2k | 4-3 | 57.1 | 16.5 | 43.9 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 2-3 | 40.0 | -3.0 | -23.6 |  |
| money_level+pin_move | close | pin $1-2k | 5-3 | 62.5 | 11.1 | 18.9 |  |
| money_level+pin_rlm | close | pin $1-2k | 2-1 | 66.7 | 22.2 | 28.7 |  |
| money_level+rlm_ratio | close | pin $1-2k | 1-1 | 50.0 | 3.7 | -4.5 |  |
| money_moving+pin_move | close | pin $1-2k | 9-7 | 56.2 | 11.6 | 22.4 |  |
| money_moving+pin_rlm | close | pin $1-2k | 6-5 | 54.5 | 14.9 | 26.6 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 4-4 | 50.0 | 7.9 | -4.0 |  |
| pin_move+pin_rlm | close | pin $1-2k | 6-5 | 54.5 | 14.9 | 26.6 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 4-4 | 50.0 | 7.9 | -4.0 |  |
| pin_move+sharp_gap | close | pin $1-2k | 9-7 | 56.2 | 11.6 | 22.4 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 4-4 | 50.0 | 7.9 | -4.0 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 6-5 | 54.5 | 14.9 | 26.6 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 4-4 | 50.0 | 7.9 | -4.0 |  |
| follow_move+pin_value | close | pin $1-2k | 1-2 | 33.3 | -13.6 | -34.9 |  |
| pin_move+pin_value | close | pin $1-2k | 2-1 | 66.7 | 19.8 | 26.2 |  |
| pin_rlm+pin_value | close | pin $1-2k | 1-1 | 50.0 | 3.7 | -2.4 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 1-1 | 50.0 | 3.7 | -2.4 |  |
| money_delta+pin_value | close | pin $1-2k | 0-1 | 0.0 | -51.9 | -100.0 |  |
| consensus_gap+pin_move | close | pin $1-2k | 1-0 | 100.0 | 51.9 | 83.3 |  |
| consensus_gap+money_delta | close | pin $1-2k | 0-1 | 0.0 | -29.2 | -100.0 |  |
| follow_move+money_level | close | pin $2k+ | 6-3 | 66.7 | 9.3 | 13.9 |  |
| follow_move+money_moving | close | pin $2k+ | 6-2 | 75.0 | 25.5 | 48.9 |  |
| follow_move+pin_move | close | pin $2k+ | 8-2 | 80.0 | 27.4 | 50.5 |  |
| follow_move+pin_value | close | pin $2k+ | 3-2 | 60.0 | 7.3 | 7.9 |  |
| follow_move+sharp_gap | close | pin $2k+ | 6-2 | 75.0 | 25.5 | 48.9 |  |
| money_level+money_moving | close | pin $2k+ | 7-6 | 53.8 | 1.1 | -2.6 |  |
| money_level+pin_move | close | pin $2k+ | 5-3 | 62.5 | 4.0 | 14.0 |  |
| money_level+pin_value | close | pin $2k+ | 3-2 | 60.0 | 6.6 | 9.4 |  |
| money_level+sharp_gap | close | pin $2k+ | 7-6 | 53.8 | 1.1 | -2.6 |  |
| money_moving+pin_move | close | pin $2k+ | 4-2 | 66.7 | 10.3 | 20.9 |  |
| money_moving+pin_value | close | pin $2k+ | 3-3 | 50.0 | -2.5 | -8.8 |  |
| money_moving+sharp_gap | close | pin $2k+ | 10-9 | 52.6 | 4.5 | 0.9 |  |
| pin_move+pin_value | close | pin $2k+ | 4-2 | 66.7 | 14.1 | 21.7 |  |
| pin_move+sharp_gap | close | pin $2k+ | 4-2 | 66.7 | 10.3 | 20.9 |  |
| pin_value+sharp_gap | close | pin $2k+ | 3-3 | 50.0 | -2.5 | -8.8 |  |
| money_delta+money_level | close | pin $2k+ | 1-1 | 50.0 | 9.5 | -4.5 |  |
| money_delta+money_moving | close | pin $2k+ | 2-2 | 50.0 | 10.4 | -2.8 |  |
| money_delta+sharp_gap | close | pin $2k+ | 2-2 | 50.0 | 10.4 | -2.8 |  |
| follow_move+money_delta | close | pin $2k+ | 3-0 | 100.0 | 55.7 | 95.6 |  |
| money_delta+pin_move | close | pin $2k+ | 3-1 | 75.0 | 24.1 | 45.0 |  |
| money_delta+pin_value | close | pin $2k+ | 1-1 | 50.0 | 0.0 | -4.5 |  |
| consensus_gap+money_level | close | pin $2k+ | 0-2 | 0.0 | -70.8 | -100.0 |  |
| consensus_gap+pin_move | close | pin $2k+ | 1-1 | 50.0 | 0.0 | 6.0 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 2-0 | 100.0 | 70.8 | 133.0 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 2-0 | 100.0 | 70.8 | 133.0 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 2-0 | 100.0 | 70.8 | 133.0 |  |
| consensus_gap+follow_move | close | pin $2k+ | 1-0 | 100.0 | 70.8 | 112.0 |  |
| follow_move+pin_rlm | close | pin $2k+ | 1-0 | 100.0 | 70.8 | 98.0 |  |
| money_delta+pin_rlm | close | pin $2k+ | 2-0 | 100.0 | 59.5 | 94.5 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 1-0 | 100.0 | 70.8 | 98.0 |  |
| money_moving+pin_rlm | close | pin $2k+ | 2-0 | 100.0 | 59.5 | 94.5 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 1-0 | 100.0 | 70.8 | 98.0 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 2-0 | 100.0 | 59.5 | 94.5 |  |
| money_level+pin_rlm | close | pin $2k+ | 1-0 | 100.0 | 48.1 | 90.9 |  |
| pin_move+pin_rlm | close | pin $2k+ | 1-0 | 100.0 | 48.1 | 90.9 |  |
| pin_rlm+pin_value | close | pin $2k+ | 1-0 | 100.0 | 48.1 | 90.9 |  |
| money_delta+money_moving | close | pin limit <$1k | 0-2 | 0.0 | -40.7 | -100.0 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 0-2 | 0.0 | -40.7 | -100.0 |  |
| money_level+pin_move | close | pin limit <$1k | 2-1 | 66.7 | 7.4 | 27.3 |  |
| money_level+pin_value | close | pin limit <$1k | 4-0 | 100.0 | 40.7 | 89.1 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 1-2 | 33.3 | -13.6 | -36.4 |  |
| pin_move+pin_value | close | pin limit <$1k | 2-1 | 66.7 | 13.6 | 27.3 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 0-2 | 0.0 | -40.7 | -100.0 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 2-2 | 50.0 | 4.6 | -3.5 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 0-1 | 0.0 | -40.7 | -100.0 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 0-2 | 0.0 | -40.7 | -100.0 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 0-2 | 0.0 | -40.7 | -100.0 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 1-2 | 33.3 | -13.6 | -36.4 |  |
| money_level+money_moving | close | pin limit <$1k | 2-2 | 50.0 | -9.3 | -5.3 |  |
| money_moving+pin_value | close | pin limit <$1k | 2-0 | 100.0 | 40.7 | 89.3 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 0-2 | 0.0 | -40.7 | -100.0 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 1-0 | 100.0 | 40.7 | 90.9 |  |
| consensus_gap+money_level | close | pin limit <$1k | 2-0 | 100.0 | 40.7 | 88.9 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 1-0 | 100.0 | 40.7 | 90.9 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 1-0 | 100.0 | 40.7 | 90.9 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 2-0 | 100.0 | 40.7 | 88.9 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 1-0 | 100.0 | 40.7 | 90.9 |  |
| follow_move+money_level | close | pin limit <$1k | 1-0 | 100.0 | 40.7 | 90.9 |  |
| follow_move+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 |  |
| follow_move+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 |  |
| follow_move+pin_value | close | pin limit <$1k | 1-0 | 100.0 | 40.7 | 90.9 |  |
| money_level+sharp_gap | close | pin limit <$1k | 1-0 | 100.0 | 40.7 | 90.9 |  |
| money_moving+pin_move | close | pin limit <$1k | 1-2 | 33.3 | -19.8 | -36.4 |  |
| follow_move+money_delta | close | pin limit <$1k | 0-1 | 0.0 | -40.7 | -100.0 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 0-1 | 0.0 | -40.7 | -100.0 |  |
| money_delta+pin_move | close | pin limit <$1k | 0-1 | 0.0 | -40.7 | -100.0 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 0-1 | 0.0 | -40.7 | -100.0 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 0-1 | 0.0 | -40.7 | -100.0 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 0-1 | 0.0 | -40.7 | -100.0 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 0-1 | 0.0 | -40.7 | -100.0 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 0-1 | 0.0 | -40.7 | -100.0 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 0-1 | 0.0 | -40.7 | -100.0 |  |
| money_delta | early | <1k bets | 0-2 | 0.0 | -35.0 | -100.0 | 1.0 |
| follow_move | early | <1k bets | 9-8 | 52.9 | 4.1 | -0.2 | -0.2 |
| rlm_ratio | early | <1k bets | 4-2 | 66.7 | 29.8 | 31.8 | 0.7 |
| money_level | early | <1k bets | 7-8 | 46.7 | -15.2 | -22.6 | -0.32 |
| sharp_gap | early | <1k bets | 8-6 | 57.1 | 11.1 | 25.4 | 0.81 |
| money_moving | early | <1k bets | 3-10 | 23.1 | -23.0 | -58.4 | -0.71 |
| consensus_gap | early | <1k bets | 3-3 | 50.0 | -9.5 | -20.6 | 0.57 |
| money_moving+sharp_gap | early | <1k bets | 2-4 | 33.3 | -10.5 | -49.3 | -0.35 |
| follow_move+money_level | early | <1k bets | 4-3 | 57.1 | -2.8 | -4.2 | -0.64 |
| follow_move+money_moving | early | <1k bets | 3-4 | 42.9 | -4.2 | -22.8 | -0.74 |
| follow_move+sharp_gap | early | <1k bets | 7-2 | 77.8 | 30.9 | 41.2 | 0.41 |
| money_level+money_moving | early | <1k bets | 1-5 | 16.7 | -41.5 | -81.8 | -0.75 |
| money_level+sharp_gap | early | <1k bets | 3-2 | 60.0 | -2.5 | -4.1 | 0.52 |
| follow_move+money_delta | early | <1k bets | 0-1 | 0.0 | -40.7 | -100.0 | 2.0 |
| follow_move+rlm_ratio | early | <1k bets | 4-2 | 66.7 | 29.8 | 31.8 | 0.7 |
| money_delta+money_level | early | <1k bets | 0-1 | 0.0 | -40.7 | -100.0 | 2.0 |
| money_delta+money_moving | early | <1k bets | 0-2 | 0.0 | -35.0 | -100.0 | 1.0 |
| money_delta+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -40.7 | -100.0 | 2.0 |
| money_delta+sharp_gap | early | <1k bets | 0-1 | 0.0 | -40.7 | -100.0 | 2.0 |
| money_level+rlm_ratio | early | <1k bets | 0-1 | 0.0 | -40.7 | -100.0 | 2.0 |
| money_moving+rlm_ratio | early | <1k bets | 1-2 | 33.3 | -3.5 | -34.9 | 0.13 |
| rlm_ratio+sharp_gap | early | <1k bets | 4-2 | 66.7 | 29.8 | 31.8 | 0.7 |
| consensus_gap+follow_move | early | <1k bets | 1-2 | 33.3 | -22.4 | -38.9 | 0.33 |
| consensus_gap+money_level | early | <1k bets | 2-2 | 50.0 | -15.2 | -26.8 | 1.1 |
| consensus_gap+money_moving | early | <1k bets | 0-1 | 0.0 | -48.1 | -100.0 | 2.0 |
| consensus_gap+sharp_gap | early | <1k bets | 1-1 | 50.0 | -20.8 | -8.4 | 0.55 |
