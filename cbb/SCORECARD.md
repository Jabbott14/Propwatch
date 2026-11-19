# CBB scorecard

Generated 2026-11-19 17:00 UTC. 642 graded games (17 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**512 games before 2026-11-17 (fit) · 130 on or after it (forward).**

Every signal, threshold and PROMOTE/DROP label here was chosen while looking at
the games before 2026-11-17. `pin_value` went 108-68 in first halves --
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
sample ran **48.0% favourites** (n=641) and **48.9% overs** (n=642) and **74.3% moneyline favourites** (n=544).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-17. Nothing in the engine was chosen using these. n=130 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 0-1 | 0.0 | 25.2 | -25.2 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| follow_move | both | 131-90 | 59.3 | 52.5 | 6.8 | +9.86 | 4.5 | 0.16 | 42.1 | PROMOTE: beats break-even and its own base rate |
| rlm_ratio | both | 8-1 | 88.9 | 35.1 | 53.7 | +8.39 | 93.2 | 1.33 | 66.7 | keep collecting (9/30) |
| money_level | both | 43-24 | 64.2 | 64.2 | -0.0 | +0.93 | 1.4 | -0.93 | 32.8 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 30-34 | 46.9 | 46.7 | 0.2 | -7.43 | -11.6 | -0.14 | 42.2 | no edge shown yet |
| money_moving | both | 29-21 | 58.0 | 52.8 | 5.2 | -1.58 | -3.2 | -0.24 | 44.0 | no edge shown yet |
| pin_value | both | 6-6 | 50.0 | 50.8 | -0.8 | -0.76 | -6.3 | -0.21 | 16.7 | keep collecting (12/30) |
| consensus_gap | both | 56-59 | 48.7 | 47.9 | 0.8 | +7.87 | 6.8 | 0.65 | 44.3 | no edge shown yet |
| money_level+money_moving | both | 18-8 | 69.2 | 65.1 | 4.1 | +1.96 | 7.5 | -0.91 | 42.3 | keep collecting (26/30) |
| money_level+sharp_gap | both | 22-16 | 57.9 | 58.9 | -1.0 | -1.74 | -4.6 | -0.94 | 34.2 | no edge shown yet |
| money_moving+sharp_gap | both | 14-15 | 48.3 | 47.1 | 1.2 | -3.39 | -11.7 | -0.55 | 44.8 | keep collecting (29/30) |
| consensus_gap+money_moving | both | 2-3 | 40.0 | 50.3 | -10.3 | -1.73 | -34.5 | 0.44 | 60.0 | keep collecting (5/30) |
| consensus_gap+sharp_gap | both | 5-11 | 31.2 | 37.0 | -5.7 | -6.3 | -39.3 | 1.82 | 62.5 | keep collecting (16/30) |
| follow_move+money_level | both | 22-5 | 81.5 | 70.0 | 11.5 | +4.8 | 17.8 | -0.81 | 44.4 | keep collecting (27/30) |
| follow_move+money_moving | both | 18-8 | 69.2 | 54.8 | 14.4 | +3.61 | 13.9 | 0.19 | 50.0 | keep collecting (26/30) |
| follow_move+rlm_ratio | both | 8-1 | 88.9 | 35.1 | 53.7 | +8.39 | 93.2 | 1.33 | 66.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 16-7 | 69.6 | 50.5 | 19.1 | +5.44 | 23.6 | 0.07 | 47.8 | keep collecting (23/30) |
| money_moving+rlm_ratio | both | 5-1 | 83.3 | 35.7 | 47.6 | +5.21 | 86.8 | 0.58 | 50.0 | keep collecting (6/30) |
| rlm_ratio+sharp_gap | both | 8-1 | 88.9 | 35.1 | 53.7 | +8.39 | 93.2 | 1.33 | 66.7 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 6-4 | 60.0 | 51.3 | 8.7 | +1.75 | 17.4 | 0.97 | 60.0 | keep collecting (10/30) |
| consensus_gap+pin_value | both | 2-1 | 66.7 | 49.5 | 17.2 | +0.62 | 20.8 | -0.17 | 0.0 | keep collecting (3/30) |
| money_level+pin_value | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -0.5 | 0.0 | keep collecting (2/30) |
| pin_value+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -0.5 | 0.0 | keep collecting (2/30) |
| consensus_gap+money_level | both | 8-4 | 66.7 | 67.6 | -0.9 | +2.07 | 17.3 | 0.45 | 50.0 | keep collecting (12/30) |
| money_moving+pin_value | both | 1-0 | 100.0 | 38.5 | 61.5 | +0.91 | 90.9 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+rlm_ratio | both | 2-0 | 100.0 | 43.4 | 56.6 | +2.59 | 129.6 | 2.4 | 100.0 | keep collecting (2/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 25.2 | -25.2 | -1.0 | -100.0 | 1.3 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 0-1 | 0.0 | 25.2 | -25.2 | -1.0 | -100.0 | 1.3 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+pin_value | both | 2-0 | 100.0 | 63.2 | 36.8 | +1.61 | 80.3 | -0.75 | 0.0 | keep collecting (2/30) |
| consensus_gap+rlm_ratio | both | 2-0 | 100.0 | 31.8 | 68.2 | +2.27 | 113.6 | 2.75 | 100.0 | keep collecting (2/30) |
| pin_rlm | moneyline | 0-1 | 0.0 | 25.2 | -25.2 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| follow_move | moneyline | 53-31 | 63.1 | 57.7 | 5.4 | -2.8 | -3.3 | -0.26 | 41.7 | PROMOTE: beats break-even and its own base rate |
| follow_move | spread | 33-25 | 56.9 | 49.5 | 7.4 | +5.62 | 9.7 | 0.19 | 37.9 | no edge shown yet |
| follow_move | total | 45-34 | 57.0 | 49.3 | 7.7 | +7.05 | 8.9 | 0.59 | 45.6 | no edge shown yet |
| rlm_ratio | moneyline | 3-1 | 75.0 | 25.2 | 49.8 | +3.76 | 94.0 | 1.5 | 50.0 | keep collecting (4/30) |
| rlm_ratio | total | 5-0 | 100.0 | 43.1 | 56.9 | +4.63 | 92.6 | 1.2 | 80.0 | keep collecting (5/30) |
| money_level | moneyline | 29-9 | 76.3 | 69.6 | 6.8 | +3.24 | 8.5 | -0.96 | 44.7 | PROMOTE: beats break-even and its own base rate |
| money_level | spread | 1-0 | 100.0 | 51.5 | 48.5 | +0.91 | 90.9 | 2.0 | 100.0 | keep collecting (1/30) |
| money_level | total | 13-15 | 46.4 | 57.4 | -11.0 | -3.22 | -11.5 | -1.0 | 14.3 | keep collecting (28/30) |
| sharp_gap | moneyline | 14-22 | 38.9 | 43.1 | -4.2 | -10.02 | -27.8 | -0.03 | 47.2 | DROP: below break-even |
| sharp_gap | spread | 1-0 | 100.0 | 51.5 | 48.5 | +0.91 | 90.9 | 2.0 | 100.0 | keep collecting (1/30) |
| sharp_gap | total | 15-12 | 55.6 | 51.3 | 4.3 | +1.68 | 6.2 | -0.37 | 33.3 | keep collecting (27/30) |
| money_moving | moneyline | 16-12 | 57.1 | 55.3 | 1.8 | -4.44 | -15.9 | -0.82 | 39.3 | keep collecting (28/30) |
| money_moving | spread | 1-0 | 100.0 | 51.5 | 48.5 | +0.91 | 90.9 | 2.0 | 100.0 | keep collecting (1/30) |
| money_moving | total | 12-9 | 57.1 | 49.5 | 7.7 | +1.95 | 9.3 | 0.43 | 47.6 | keep collecting (21/30) |
| pin_value | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.29 | -14.3 | -0.25 | 0.0 | keep collecting (2/30) |
| pin_value | spread | 2-3 | 40.0 | 49.7 | -9.7 | -1.2 | -24.0 | 0.0 | 20.0 | keep collecting (5/30) |
| pin_value | total | 3-2 | 60.0 | 52.3 | 7.7 | +0.73 | 14.5 | -0.4 | 20.0 | keep collecting (5/30) |
| consensus_gap | moneyline | 24-40 | 37.5 | 45.4 | -7.9 | -1.56 | -2.4 | 0.58 | 42.2 | DROP: below break-even |
| consensus_gap | spread | 12-8 | 60.0 | 51.1 | 8.9 | +2.6 | 13.0 | -0.35 | 20.0 | keep collecting (20/30) |
| consensus_gap | total | 20-11 | 64.5 | 51.1 | 13.4 | +6.83 | 22.0 | 1.45 | 64.5 | no edge shown yet |
| money_level+money_moving | moneyline | 12-3 | 80.0 | 71.5 | 8.5 | +1.47 | 9.8 | -1.37 | 46.7 | keep collecting (15/30) |
| money_level+sharp_gap | moneyline | 11-6 | 64.7 | 63.1 | 1.6 | -1.74 | -10.2 | -1.16 | 47.1 | keep collecting (17/30) |
| money_moving+sharp_gap | moneyline | 6-11 | 35.3 | 45.6 | -10.3 | -6.7 | -39.4 | -1.24 | 35.3 | keep collecting (17/30) |
| consensus_gap+money_moving | moneyline | 1-3 | 25.0 | 50.0 | -25.0 | -2.64 | -65.9 | 0.05 | 50.0 | keep collecting (4/30) |
| consensus_gap+sharp_gap | moneyline | 3-11 | 21.4 | 35.8 | -14.4 | -8.16 | -58.3 | 1.87 | 57.1 | keep collecting (14/30) |
| follow_move+money_level | moneyline | 18-3 | 85.7 | 72.4 | 13.3 | +3.16 | 15.0 | -0.76 | 52.4 | keep collecting (21/30) |
| follow_move+money_moving | moneyline | 12-6 | 66.7 | 58.3 | 8.4 | +0.11 | 0.6 | -0.11 | 44.4 | keep collecting (18/30) |
| consensus_gap+money_level | moneyline | 6-4 | 60.0 | 69.8 | -9.8 | +0.3 | 3.0 | 0.54 | 50.0 | keep collecting (10/30) |
| follow_move+sharp_gap | moneyline | 8-6 | 57.1 | 50.0 | 7.1 | -0.88 | -6.3 | 0.05 | 50.0 | keep collecting (14/30) |
| follow_move+rlm_ratio | moneyline | 3-1 | 75.0 | 25.2 | 49.8 | +3.76 | 94.0 | 1.5 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_ratio | moneyline | 2-1 | 66.7 | 25.2 | 41.4 | +2.44 | 81.3 | 0.5 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | moneyline | 3-1 | 75.0 | 25.2 | 49.8 | +3.76 | 94.0 | 1.5 | 50.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 25.2 | -25.2 | -1.0 | -100.0 | 1.3 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 0-1 | 0.0 | 25.2 | -25.2 | -1.0 | -100.0 | 1.3 | 100.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 2-3 | 40.0 | 55.0 | -15.0 | -0.97 | -19.3 | -0.26 | 40.0 | keep collecting (5/30) |
| consensus_gap+pin_value | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.29 | -14.3 | -0.25 | 0.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_value | moneyline | 1-0 | 100.0 | 74.8 | 25.2 | +0.71 | 71.4 | -0.5 | 0.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | moneyline | 1-0 | 100.0 | 25.2 | 74.8 | +1.32 | 132.0 | 4.5 | 100.0 | keep collecting (1/30) |
| money_level+rlm_ratio | moneyline | 1-0 | 100.0 | 25.2 | 74.8 | +1.64 | 164.0 | 3.8 | 100.0 | keep collecting (1/30) |
| consensus_gap+follow_move | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.02 | -1.0 | 0.5 | 50.0 | keep collecting (2/30) |
| consensus_gap+pin_value | spread | 1-0 | 100.0 | 48.5 | 51.5 | +0.91 | 90.9 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+pin_value | spread | 1-0 | 100.0 | 51.5 | 48.5 | +0.89 | 89.3 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 1-0 | 100.0 | 51.5 | 48.5 | +0.91 | 90.9 | 2.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| consensus_gap+money_moving | spread | 1-0 | 100.0 | 51.5 | 48.5 | +0.91 | 90.9 | 2.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| consensus_gap+sharp_gap | spread | 1-0 | 100.0 | 51.5 | 48.5 | +0.91 | 90.9 | 2.0 | 100.0 | redundant -- identical record to sharp_gap alone, not independent confirmation |
| money_level+money_moving | spread | 1-0 | 100.0 | 51.5 | 48.5 | +0.91 | 90.9 | 2.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+sharp_gap | spread | 1-0 | 100.0 | 51.5 | 48.5 | +0.91 | 90.9 | 2.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_moving+sharp_gap | spread | 1-0 | 100.0 | 51.5 | 48.5 | +0.91 | 90.9 | 2.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+money_moving | total | 6-2 | 75.0 | 47.1 | 27.9 | +3.5 | 43.7 | 0.88 | 62.5 | keep collecting (8/30) |
| follow_move+rlm_ratio | total | 5-0 | 100.0 | 43.1 | 56.9 | +4.63 | 92.6 | 1.2 | 80.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 8-1 | 88.9 | 51.3 | 37.6 | +6.32 | 70.2 | 0.11 | 44.4 | keep collecting (9/30) |
| money_moving+rlm_ratio | total | 3-0 | 100.0 | 46.2 | 53.8 | +2.77 | 92.3 | 0.67 | 66.7 | keep collecting (3/30) |
| money_moving+sharp_gap | total | 7-4 | 63.6 | 49.0 | 14.7 | +2.41 | 21.9 | 0.27 | 54.5 | keep collecting (11/30) |
| rlm_ratio+sharp_gap | total | 5-0 | 100.0 | 43.1 | 56.9 | +4.63 | 92.6 | 1.2 | 80.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | total | 3-0 | 100.0 | 46.2 | 53.8 | +2.73 | 91.0 | 3.33 | 100.0 | keep collecting (3/30) |
| money_level+pin_value | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -0.5 | 0.0 | keep collecting (2/30) |
| money_level+sharp_gap | total | 10-10 | 50.0 | 55.8 | -5.8 | -0.91 | -4.5 | -0.9 | 20.0 | keep collecting (20/30) |
| pin_value+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.09 | -4.5 | -0.5 | 0.0 | keep collecting (2/30) |
| money_level+money_moving | total | 5-5 | 50.0 | 56.9 | -6.9 | -0.41 | -4.1 | -0.5 | 30.0 | keep collecting (10/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 38.5 | 61.5 | +0.91 | 90.9 | -1.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_level | total | 4-2 | 66.7 | 61.5 | 5.1 | +1.64 | 27.3 | -1.0 | 16.7 | keep collecting (6/30) |
| money_level+rlm_ratio | total | 1-0 | 100.0 | 61.5 | 38.5 | +0.95 | 95.2 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 1-0 | 100.0 | 38.5 | 61.5 | +0.95 | 95.2 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+sharp_gap | total | 1-0 | 100.0 | 38.5 | 61.5 | +0.95 | 95.2 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | total | 1-0 | 100.0 | 61.5 | 38.5 | +0.87 | 87.0 | -2.0 | 0.0 | keep collecting (1/30) |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 25-34 | 42.4 | 38.6 | 3.8 | +4.94 | 8.4 |  |  | DROP: below break-even |
| follow_move | both | 157-144 | 52.2 | 50.5 | 1.6 | -16.38 | -5.4 |  |  | no edge shown yet |
| rlm_ratio | both | 39-49 | 44.3 | 42.0 | 2.3 | -3.11 | -3.5 |  |  | DROP: below break-even |
| money_level | both | 219-148 | 59.7 | 57.3 | 2.4 | +1.89 | 0.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 169-182 | 48.1 | 48.3 | -0.2 | -20.23 | -5.8 |  |  | DROP: below break-even |
| money_moving | both | 173-179 | 49.1 | 49.4 | -0.2 | -17.56 | -5.0 |  |  | no edge shown yet |
| pin_value | both | 57-62 | 47.9 | 48.4 | -0.5 | +7.77 | 6.5 |  |  | no edge shown yet |
| consensus_gap | both | 60-58 | 50.8 | 48.9 | 1.9 | -2.09 | -1.8 |  |  | no edge shown yet |
| money_level+money_moving | both | 126-94 | 57.3 | 54.9 | 2.4 | +2.01 | 0.9 |  |  | no edge shown yet |
| money_level+pin_rlm | both | 8-10 | 44.4 | 42.1 | 2.3 | -0.38 | -2.1 |  |  | keep collecting (18/30) |
| money_level+sharp_gap | both | 119-91 | 56.7 | 54.2 | 2.5 | +2.08 | 1.0 |  |  | no edge shown yet |
| money_moving+pin_rlm | both | 22-32 | 40.7 | 38.7 | 2.0 | +3.71 | 6.9 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 161-170 | 48.6 | 48.8 | -0.2 | -14.01 | -4.2 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 25-34 | 42.4 | 38.6 | 3.8 | +4.94 | 8.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_value | both | 27-27 | 50.0 | 52.2 | -2.2 | -3.67 | -6.8 |  |  | no edge shown yet |
| money_moving+pin_value | both | 26-32 | 44.8 | 49.5 | -4.7 | -3.62 | -6.2 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 27-34 | 44.3 | 48.5 | -4.3 | -4.7 | -7.7 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 36-18 | 66.7 | 64.7 | 2.0 | +2.85 | 5.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | both | 31-31 | 50.0 | 48.0 | 2.0 | -2.05 | -3.3 |  |  | no edge shown yet |
| consensus_gap+pin_value | both | 19-13 | 59.4 | 46.8 | 12.6 | +9.43 | 29.5 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | both | 29-31 | 48.3 | 46.5 | 1.8 | -2.21 | -3.7 |  |  | no edge shown yet |
| follow_move+money_level | both | 104-63 | 62.3 | 57.7 | 4.6 | +4.41 | 2.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+money_moving | both | 90-86 | 51.1 | 49.7 | 1.5 | -4.73 | -2.7 |  |  | no edge shown yet |
| follow_move+sharp_gap | both | 91-87 | 51.1 | 49.0 | 2.1 | -2.24 | -1.3 |  |  | no edge shown yet |
| follow_move+pin_value | both | 13-18 | 41.9 | 47.8 | -5.9 | -6.44 | -20.8 |  |  | no edge shown yet |
| follow_move+pin_rlm | both | 18-23 | 43.9 | 38.9 | 5.1 | +2.42 | 5.9 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 39-49 | 44.3 | 42.0 | 2.3 | -3.11 | -3.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm_ratio | both | 35-47 | 42.7 | 42.3 | 0.4 | -5.29 | -6.5 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | both | 18-23 | 43.9 | 38.9 | 5.1 | +2.42 | 5.9 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | both | 39-49 | 44.3 | 42.0 | 2.3 | -3.11 | -3.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | both | 20-11 | 64.5 | 52.9 | 11.6 | +2.68 | 8.6 |  |  | no edge shown yet |
| money_level+rlm_ratio | both | 15-16 | 48.4 | 47.7 | 0.7 | +0.14 | 0.4 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 5-6 | 45.5 | 36.6 | 8.8 | -1.53 | -13.9 |  |  | keep collecting (11/30) |
| pin_rlm+pin_value | both | 10-8 | 55.6 | 44.0 | 11.6 | +0.98 | 5.5 |  |  | keep collecting (18/30) |
| consensus_gap+rlm_ratio | both | 5-5 | 50.0 | 37.8 | 12.2 | -0.64 | -6.4 |  |  | keep collecting (10/30) |
| pin_value+rlm_ratio | both | 7-5 | 58.3 | 43.4 | 14.9 | +1.26 | 10.5 |  |  | keep collecting (12/30) |
| pin_rlm | moneyline | 6-13 | 31.6 | 25.2 | 6.4 | +8.66 | 45.6 |  |  | keep collecting (19/30) |
| pin_rlm | spread | 4-5 | 44.4 | 49.5 | -5.0 | -1.25 | -13.9 |  |  | keep collecting (9/30) |
| pin_rlm | total | 15-16 | 48.4 | 43.7 | 4.7 | -2.47 | -8.0 |  |  | no edge shown yet |
| follow_move | moneyline | 59-40 | 59.6 | 54.3 | 5.3 | -2.39 | -2.4 |  |  | no edge shown yet |
| follow_move | spread | 45-51 | 46.9 | 49.7 | -2.8 | -9.38 | -9.8 |  |  | no edge shown yet |
| follow_move | total | 53-53 | 50.0 | 47.8 | 2.2 | -4.61 | -4.4 |  |  | no edge shown yet |
| rlm_ratio | moneyline | 8-16 | 33.3 | 31.4 | 1.9 | +1.65 | 6.9 |  |  | keep collecting (24/30) |
| rlm_ratio | spread | 8-6 | 57.1 | 49.8 | 7.4 | +1.21 | 8.6 |  |  | keep collecting (14/30) |
| rlm_ratio | total | 23-27 | 46.0 | 44.9 | 1.1 | -5.97 | -11.9 |  |  | no edge shown yet |
| money_level | moneyline | 84-26 | 76.4 | 71.2 | 5.2 | +1.37 | 1.2 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level | spread | 64-63 | 50.4 | 50.5 | -0.1 | -5.08 | -4.0 |  |  | no edge shown yet |
| money_level | total | 71-59 | 54.6 | 52.1 | 2.5 | +5.6 | 4.3 |  |  | no edge shown yet |
| sharp_gap | moneyline | 43-56 | 43.4 | 45.7 | -2.3 | -8.17 | -8.3 |  |  | DROP: below break-even |
| sharp_gap | spread | 65-62 | 51.2 | 50.4 | 0.8 | -3.53 | -2.8 |  |  | no edge shown yet |
| sharp_gap | total | 61-64 | 48.8 | 48.2 | 0.6 | -8.53 | -6.8 |  |  | no edge shown yet |
| money_moving | moneyline | 47-52 | 47.5 | 48.7 | -1.3 | -4.45 | -4.5 |  |  | no edge shown yet |
| money_moving | spread | 65-62 | 51.2 | 50.4 | 0.8 | -3.53 | -2.8 |  |  | no edge shown yet |
| money_moving | total | 61-65 | 48.4 | 48.9 | -0.5 | -9.59 | -7.6 |  |  | no edge shown yet |
| pin_value | moneyline | 4-7 | 36.4 | 29.7 | 6.6 | +16.09 | 146.2 |  |  | keep collecting (11/30) |
| pin_value | spread | 21-27 | 43.8 | 50.6 | -6.9 | -9.1 | -19.0 |  |  | no edge shown yet |
| pin_value | total | 32-28 | 53.3 | 50.0 | 3.3 | +0.79 | 1.3 |  |  | no edge shown yet |
| consensus_gap | moneyline | 31-40 | 43.7 | 46.9 | -3.2 | -9.31 | -13.1 |  |  | no edge shown yet |
| consensus_gap | spread | 12-8 | 60.0 | 50.6 | 9.4 | +2.06 | 10.3 |  |  | keep collecting (20/30) |
| consensus_gap | total | 17-10 | 63.0 | 53.0 | 10.0 | +5.15 | 19.1 |  |  | keep collecting (27/30) |
| money_moving+sharp_gap | moneyline | 39-48 | 44.8 | 46.9 | -2.0 | -2.26 | -2.6 |  |  | no edge shown yet |
| follow_move+money_level | moneyline | 46-11 | 80.7 | 72.2 | 8.5 | +3.24 | 5.7 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 23-21 | 52.3 | 52.3 | 0.0 | -1.01 | -2.3 |  |  | no edge shown yet |
| follow_move+sharp_gap | moneyline | 21-21 | 50.0 | 50.0 | 0.0 | -0.3 | -0.7 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 39-14 | 73.6 | 68.2 | 5.4 | +3.29 | 6.2 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level+sharp_gap | moneyline | 34-13 | 72.3 | 67.4 | 4.9 | +3.18 | 6.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_level | moneyline | 23-8 | 74.2 | 73.2 | 1.0 | +1.58 | 5.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move+pin_rlm | moneyline | 5-6 | 45.5 | 25.2 | 20.2 | +7.56 | 68.7 |  |  | keep collecting (11/30) |
| follow_move+rlm_ratio | moneyline | 8-16 | 33.3 | 31.4 | 1.9 | +1.65 | 6.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_rlm | moneyline | 5-12 | 29.4 | 25.2 | 4.2 | +8.26 | 48.6 |  |  | keep collecting (17/30) |
| money_moving+rlm_ratio | moneyline | 7-15 | 31.8 | 32.0 | -0.2 | +1.25 | 5.7 |  |  | keep collecting (22/30) |
| pin_rlm+rlm_ratio | moneyline | 5-6 | 45.5 | 25.2 | 20.2 | +7.56 | 68.7 |  |  | keep collecting (11/30) |
| pin_rlm+sharp_gap | moneyline | 6-13 | 31.6 | 25.2 | 6.4 | +8.66 | 45.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 8-16 | 33.3 | 31.4 | 1.9 | +1.65 | 6.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 11-7 | 61.1 | 55.5 | 5.6 | -1.17 | -6.5 |  |  | keep collecting (18/30) |
| money_level+pin_rlm | moneyline | 1-2 | 33.3 | 25.2 | 8.1 | +1.3 | 43.3 |  |  | keep collecting (3/30) |
| money_level+rlm_ratio | moneyline | 2-3 | 40.0 | 45.0 | -5.0 | +1.4 | 28.0 |  |  | keep collecting (5/30) |
| consensus_gap+money_moving | moneyline | 16-22 | 42.1 | 46.1 | -4.0 | -6.06 | -15.9 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | moneyline | 0-4 | 0.0 | 25.2 | -25.2 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| consensus_gap+sharp_gap | moneyline | 13-22 | 37.1 | 43.6 | -6.5 | -7.09 | -20.3 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | moneyline | 0-5 | 0.0 | 25.2 | -25.2 | -5.0 | -100.0 |  |  | keep collecting (5/30) |
| consensus_gap+pin_value | moneyline | 1-5 | 16.7 | 25.2 | -8.6 | +1.8 | 30.0 |  |  | keep collecting (6/30) |
| money_moving+pin_value | moneyline | 2-2 | 50.0 | 37.6 | 12.4 | +5.48 | 137.1 |  |  | keep collecting (4/30) |
| pin_value+sharp_gap | moneyline | 2-4 | 33.3 | 33.5 | -0.2 | +3.48 | 58.1 |  |  | keep collecting (6/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 25.2 | -25.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+pin_value | moneyline | 1-0 | 100.0 | 74.8 | 25.2 | +0.69 | 68.5 |  |  | keep collecting (1/30) |
| money_level+money_moving | spread | 52-50 | 51.0 | 50.5 | 0.4 | -3.13 | -3.1 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 2-3 | 40.0 | 50.3 | -10.3 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| money_level+sharp_gap | spread | 52-50 | 51.0 | 50.5 | 0.4 | -3.13 | -3.1 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 4-5 | 44.4 | 49.5 | -5.0 | -1.25 | -13.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | spread | 65-62 | 51.2 | 50.4 | 0.8 | -3.53 | -2.8 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 4-5 | 44.4 | 49.5 | -5.0 | -1.25 | -13.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+money_level | spread | 7-5 | 58.3 | 51.3 | 7.1 | +0.84 | 7.0 |  |  | keep collecting (12/30) |
| consensus_gap+money_moving | spread | 7-6 | 53.8 | 51.1 | 2.8 | -0.16 | -1.2 |  |  | keep collecting (13/30) |
| consensus_gap+pin_value | spread | 8-3 | 72.7 | 51.0 | 21.7 | +3.73 | 33.9 |  |  | keep collecting (11/30) |
| consensus_gap+sharp_gap | spread | 7-6 | 53.8 | 51.1 | 2.8 | -0.16 | -1.2 |  |  | keep collecting (13/30) |
| money_level+pin_value | spread | 15-16 | 48.4 | 50.8 | -2.5 | -3.28 | -10.6 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 12-16 | 42.9 | 50.8 | -7.9 | -5.9 | -21.1 |  |  | keep collecting (28/30) |
| pin_value+sharp_gap | spread | 12-16 | 42.9 | 50.8 | -7.9 | -5.9 | -21.1 |  |  | keep collecting (28/30) |
| follow_move+money_level | spread | 29-30 | 49.2 | 50.1 | -0.9 | -3.25 | -5.5 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 5-6 | 45.5 | 50.1 | -4.7 | -1.68 | -15.3 |  |  | keep collecting (11/30) |
| consensus_gap+follow_move | spread | 3-3 | 50.0 | 50.5 | -0.5 | -0.5 | -8.3 |  |  | keep collecting (6/30) |
| follow_move+money_moving | spread | 30-28 | 51.7 | 50.1 | 1.7 | -0.39 | -0.7 |  |  | no edge shown yet |
| follow_move+sharp_gap | spread | 30-28 | 51.7 | 50.1 | 1.7 | -0.39 | -0.7 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 8-6 | 57.1 | 49.8 | 7.4 | +1.21 | 8.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+rlm_ratio | spread | 4-6 | 40.0 | 50.0 | -10.0 | -2.42 | -24.2 |  |  | keep collecting (10/30) |
| money_moving+rlm_ratio | spread | 8-6 | 57.1 | 49.8 | 7.4 | +1.21 | 8.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | spread | 8-6 | 57.1 | 49.8 | 7.4 | +1.21 | 8.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+pin_value | spread | 0-2 | 0.0 | 48.5 | -48.5 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| follow_move+pin_rlm | spread | 2-2 | 50.0 | 50.0 | 0.0 | -0.11 | -2.8 |  |  | keep collecting (4/30) |
| pin_rlm+rlm_ratio | spread | 2-2 | 50.0 | 50.0 | 0.0 | -0.11 | -2.8 |  |  | keep collecting (4/30) |
| consensus_gap+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.67 | 83.3 |  |  | keep collecting (2/30) |
| pin_value+rlm_ratio | spread | 1-0 | 100.0 | 51.5 | 48.5 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| money_level+money_moving | total | 35-30 | 53.8 | 50.9 | 3.0 | +1.85 | 2.8 |  |  | no edge shown yet |
| money_level+pin_value | total | 11-11 | 50.0 | 53.1 | -3.1 | -1.08 | -4.9 |  |  | keep collecting (22/30) |
| money_level+sharp_gap | total | 33-28 | 54.1 | 50.2 | 3.9 | +2.03 | 3.3 |  |  | no edge shown yet |
| money_moving+pin_value | total | 12-14 | 46.2 | 50.0 | -3.8 | -3.21 | -12.3 |  |  | keep collecting (26/30) |
| money_moving+sharp_gap | total | 57-60 | 48.7 | 48.5 | 0.2 | -8.22 | -7.0 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 13-14 | 48.1 | 49.6 | -1.4 | -2.29 | -8.5 |  |  | keep collecting (27/30) |
| follow_move+money_level | total | 29-22 | 56.9 | 50.2 | 6.6 | +4.42 | 8.7 |  |  | no edge shown yet |
| follow_move+money_moving | total | 37-37 | 50.0 | 47.8 | 2.2 | -3.33 | -4.5 |  |  | no edge shown yet |
| follow_move+sharp_gap | total | 40-38 | 51.3 | 47.6 | 3.6 | -1.55 | -2.0 |  |  | no edge shown yet |
| consensus_gap+money_level | total | 6-5 | 54.5 | 55.2 | -0.7 | +0.42 | 3.8 |  |  | keep collecting (11/30) |
| consensus_gap+pin_value | total | 10-5 | 66.7 | 52.3 | 14.4 | +3.9 | 26.0 |  |  | keep collecting (15/30) |
| consensus_gap+money_moving | total | 8-3 | 72.7 | 51.0 | 21.7 | +4.16 | 37.8 |  |  | keep collecting (11/30) |
| consensus_gap+pin_rlm | total | 5-1 | 83.3 | 46.2 | 37.2 | +3.47 | 57.9 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | total | 9-3 | 75.0 | 50.0 | 25.0 | +5.04 | 42.0 |  |  | keep collecting (12/30) |
| money_moving+pin_rlm | total | 13-15 | 46.4 | 43.4 | 3.0 | -3.3 | -11.8 |  |  | keep collecting (28/30) |
| pin_rlm+pin_value | total | 10-5 | 66.7 | 44.6 | 22.1 | +3.98 | 26.6 |  |  | keep collecting (15/30) |
| pin_rlm+sharp_gap | total | 15-16 | 48.4 | 43.7 | 4.7 | -2.47 | -8.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+pin_rlm | total | 11-15 | 42.3 | 42.9 | -0.6 | -5.03 | -19.3 |  |  | keep collecting (26/30) |
| follow_move+rlm_ratio | total | 23-27 | 46.0 | 44.9 | 1.1 | -5.97 | -11.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 5-5 | 50.0 | 43.1 | 6.9 | -0.49 | -4.9 |  |  | keep collecting (10/30) |
| money_level+rlm_ratio | total | 9-7 | 56.2 | 47.1 | 9.1 | +1.16 | 7.2 |  |  | keep collecting (16/30) |
| money_moving+rlm_ratio | total | 20-26 | 43.5 | 45.0 | -1.5 | -7.75 | -16.9 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 11-15 | 42.3 | 42.9 | -0.6 | -5.03 | -19.3 |  |  | keep collecting (26/30) |
| rlm_ratio+sharp_gap | total | 23-27 | 46.0 | 44.9 | 1.1 | -5.97 | -11.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+follow_move | total | 6-1 | 85.7 | 48.4 | 37.4 | +4.34 | 62.1 |  |  | keep collecting (7/30) |
| consensus_gap+rlm_ratio | total | 3-1 | 75.0 | 44.2 | 30.8 | +1.7 | 42.4 |  |  | keep collecting (4/30) |
| follow_move+pin_value | total | 8-12 | 40.0 | 46.5 | -6.5 | -4.76 | -23.8 |  |  | keep collecting (20/30) |
| pin_value+rlm_ratio | total | 6-5 | 54.5 | 42.7 | 11.9 | +0.43 | 3.9 |  |  | keep collecting (11/30) |

# FIT (in-sample — this is the hypothesis)

Games before 2026-11-17. The engine was built by looking at these, so a strong record here is expected and proves nothing. n=512 games.

## EARLY  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | both | 325-302 | 51.8 | 52.1 | -0.3 | -58.99 | -9.4 | 0.24 | 42.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | both | 17-15 | 53.1 | 37.6 | 15.5 | +9.23 | 28.9 | 0.08 | 46.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | both | 119-76 | 61.0 | 58.4 | 2.6 | -8.05 | -4.1 | 0.21 | 41.5 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 105-79 | 57.1 | 49.3 | 7.7 | +23.97 | 13.0 | 0.36 | 42.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | both | 70-50 | 58.3 | 50.9 | 7.4 | +9.37 | 7.8 | 0.19 | 42.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | both | 43-42 | 50.6 | 47.8 | 2.8 | -3.68 | -4.3 | 0.14 | 41.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.7 | -31.7 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 158-223 | 41.5 | 46.6 | -5.1 | -65.4 | -17.2 | 0.31 | 45.7 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | both | 23-22 | 51.1 | 63.2 | -12.1 | -10.62 | -23.6 | 0.25 | 46.7 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | both | 15-19 | 44.1 | 45.7 | -1.6 | -3.69 | -10.9 | 0.17 | 38.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_value | both | 17-27 | 38.6 | 45.5 | -6.9 | -12.16 | -27.6 | 0.43 | 52.3 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_ratio | both | 17-15 | 53.1 | 37.6 | 15.5 | +9.23 | 28.9 | 0.08 | 46.9 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 52-29 | 64.2 | 49.9 | 14.3 | +15.17 | 18.7 | 0.44 | 48.1 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 45-27 | 62.5 | 56.7 | 5.8 | +2.08 | 2.9 | 0.16 | 48.6 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | both | 10-8 | 55.6 | 50.7 | 4.8 | +0.9 | 5.0 | 0.5 | 50.0 | keep collecting (18/30) |
| money_moving+pin_value | both | 7-5 | 58.3 | 50.1 | 8.2 | +1.13 | 9.4 | 0.42 | 41.7 | keep collecting (12/30) |
| rlm_ratio+sharp_gap | both | 17-15 | 53.1 | 37.6 | 15.5 | +9.23 | 28.9 | 0.08 | 46.9 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 72-41 | 63.7 | 55.6 | 8.2 | +7.11 | 6.3 | 0.49 | 46.0 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 44-28 | 61.1 | 49.5 | 11.6 | +12.34 | 17.1 | 0.44 | 45.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | both | 12-7 | 63.2 | 49.3 | 13.9 | +3.75 | 19.8 | -0.15 | 36.8 | keep collecting (19/30) |
| consensus_gap+follow_move | both | 24-34 | 41.4 | 50.8 | -9.4 | -15.5 | -26.7 | 0.77 | 56.9 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_value | both | 18-17 | 51.4 | 47.6 | 3.8 | -1.2 | -3.4 | -0.08 | 31.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+sharp_gap | both | 19-33 | 36.5 | 46.5 | -10.0 | -4.74 | -9.1 | 0.64 | 46.2 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | both | 64-36 | 64.0 | 58.2 | 5.8 | -3.53 | -3.5 | 0.33 | 44.0 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 9-6 | 60.0 | 42.6 | 17.4 | +2.84 | 18.9 | 1.01 | 53.3 | keep collecting (15/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 45.0 | 5.0 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 32-17 | 65.3 | 51.8 | 13.5 | +7.79 | 15.9 | 0.49 | 55.1 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+rlm_ratio | both | 6-5 | 54.5 | 42.4 | 12.1 | +2.5 | 22.7 | -0.05 | 45.5 | keep collecting (11/30) |
| consensus_gap+rlm_ratio | both | 1-4 | 20.0 | 37.2 | -17.2 | -3.09 | -61.8 | 0.2 | 60.0 | keep collecting (5/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 53.6 | -53.6 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 25.9 | 74.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| follow_move | moneyline | 133-92 | 59.1 | 57.2 | 1.9 | -24.75 | -11.0 | 0.43 | 48.9 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 94-110 | 46.1 | 49.2 | -3.1 | -23.73 | -11.6 | -0.02 | 33.3 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | total | 98-100 | 49.5 | 49.4 | 0.1 | -10.51 | -5.3 | 0.28 | 44.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | moneyline | 9-9 | 50.0 | 25.9 | 24.1 | +7.81 | 43.4 | 0.14 | 61.1 | keep collecting (18/30) |
| rlm_ratio | spread | 3-2 | 60.0 | 51.7 | 8.3 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 5-4 | 55.6 | 53.3 | 2.2 | +0.59 | 6.5 | 0.33 | 44.4 | keep collecting (9/30) |
| money_level | moneyline | 64-27 | 70.3 | 69.4 | 1.0 | -8.93 | -9.8 | 0.18 | 46.2 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 16-16 | 50.0 | 49.1 | 0.9 | -1.6 | -5.0 | 0.81 | 46.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | total | 39-33 | 54.2 | 48.7 | 5.5 | +2.48 | 3.4 | -0.01 | 33.3 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 43-37 | 53.8 | 47.6 | 6.2 | +9.7 | 12.1 | 0.39 | 50.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | spread | 19-14 | 57.6 | 49.7 | 7.8 | +3.09 | 9.4 | 0.61 | 36.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 43-28 | 60.6 | 51.1 | 9.4 | +11.17 | 15.7 | 0.21 | 38.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | moneyline | 26-26 | 50.0 | 52.8 | -2.8 | -6.41 | -12.3 | 0.23 | 53.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | spread | 17-4 | 81.0 | 49.1 | 31.9 | +11.27 | 53.7 | 0.14 | 38.1 | keep collecting (21/30) |
| money_moving | total | 27-20 | 57.4 | 49.7 | 7.7 | +4.51 | 9.6 | 0.17 | 31.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | moneyline | 1-5 | 16.7 | 25.9 | -9.2 | -4.02 | -67.0 | -0.02 | 66.7 | keep collecting (6/30) |
| pin_value | spread | 22-17 | 56.4 | 49.2 | 7.2 | +2.35 | 6.0 | 0.28 | 41.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 20-20 | 50.0 | 49.8 | 0.2 | -2.01 | -5.0 | 0.03 | 37.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.8 | -19.5 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 63-121 | 34.2 | 43.7 | -9.5 | -47.49 | -25.8 | -0.03 | 42.4 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 51-49 | 51.0 | 49.1 | 1.9 | -4.52 | -4.5 | 0.49 | 45.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap | total | 44-53 | 45.4 | 49.3 | -4.0 | -13.39 | -13.8 | 0.76 | 52.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | moneyline | 33-12 | 73.3 | 64.5 | 8.9 | +0.72 | 1.6 | 0.53 | 57.8 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+follow_move | moneyline | 8-18 | 30.8 | 53.7 | -22.9 | -13.56 | -52.1 | 0.36 | 61.5 | keep collecting (26/30) |
| consensus_gap+pin_value | moneyline | 1-5 | 16.7 | 25.9 | -9.2 | -4.02 | -67.0 | -0.02 | 66.7 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_value | moneyline | 0-2 | 0.0 | 25.9 | -25.9 | -2.0 | -100.0 | -1.9 | 50.0 | keep collecting (2/30) |
| money_level+money_moving | moneyline | 17-9 | 65.4 | 70.4 | -5.0 | -5.47 | -21.0 | -0.07 | 57.7 | keep collecting (26/30) |
| consensus_gap+sharp_gap | moneyline | 11-24 | 31.4 | 45.2 | -13.7 | -2.71 | -7.7 | 0.55 | 48.6 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | moneyline | 37-12 | 75.5 | 68.2 | 7.3 | -4.09 | -8.4 | 0.18 | 46.9 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 14-5 | 73.7 | 56.4 | 17.3 | +3.36 | 17.7 | 0.68 | 73.7 | keep collecting (19/30) |
| consensus_gap+money_level | moneyline | 16-14 | 53.3 | 70.9 | -17.6 | -8.68 | -28.9 | -0.09 | 46.7 | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+sharp_gap | moneyline | 25-11 | 69.4 | 50.0 | 19.4 | +8.63 | 24.0 | 0.36 | 58.3 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 15-13 | 53.6 | 48.3 | 5.3 | +1.07 | 3.8 | 0.67 | 64.3 | keep collecting (28/30) |
| consensus_gap+money_moving | moneyline | 7-18 | 28.0 | 45.2 | -17.2 | -9.63 | -38.5 | 0.27 | 48.0 | keep collecting (25/30) |
| follow_move+rlm_ratio | moneyline | 9-9 | 50.0 | 25.9 | 24.1 | +7.81 | 43.4 | 0.14 | 61.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 9-9 | 50.0 | 25.9 | 24.1 | +7.81 | 43.4 | 0.14 | 61.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 0-3 | 0.0 | 25.9 | -25.9 | -3.0 | -100.0 | 0.0 | 66.7 | keep collecting (3/30) |
| money_moving+rlm_ratio | moneyline | 2-2 | 50.0 | 25.9 | 24.1 | +1.78 | 44.5 | 0.1 | 75.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 1-1 | 50.0 | 25.9 | 24.1 | -0.07 | -3.7 | -2.15 | 50.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 25.9 | -25.9 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| money_level+rlm_ratio | moneyline | 3-3 | 50.0 | 25.9 | 24.1 | +0.23 | 3.8 | 1.7 | 83.3 | keep collecting (6/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 25.9 | 74.1 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 4-5 | 44.4 | 47.2 | -2.7 | -1.59 | -17.7 | 1.67 | 66.7 | keep collecting (9/30) |
| consensus_gap+money_moving | spread | 4-0 | 100.0 | 47.2 | 52.8 | +3.41 | 85.2 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_value | spread | 9-8 | 52.9 | 48.2 | 4.8 | -0.31 | -1.8 | 0.53 | 52.9 | keep collecting (17/30) |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.7 | 8.3 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 48.6 | 13.9 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 9-4 | 69.2 | 48.5 | 20.8 | +4.21 | 32.4 | 0.77 | 61.5 | keep collecting (13/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 48.8 | -5.9 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.4 | 10.6 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 51.7 | 8.3 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 13-11 | 54.2 | 49.1 | 5.1 | +0.71 | 3.0 | 0.96 | 41.7 | keep collecting (24/30) |
| money_moving+sharp_gap | spread | 9-3 | 75.0 | 49.1 | 25.9 | +5.13 | 42.7 | 0.42 | 41.7 | keep collecting (12/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.1 | 17.6 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 8-8 | 50.0 | 47.9 | 2.1 | -1.18 | -7.4 | 0.94 | 43.8 | keep collecting (16/30) |
| consensus_gap+sharp_gap | spread | 4-3 | 57.1 | 47.2 | 10.0 | +0.41 | 5.8 | 2.14 | 71.4 | keep collecting (7/30) |
| follow_move+money_level | spread | 11-8 | 57.9 | 48.4 | 9.5 | +2.04 | 10.7 | 0.63 | 42.1 | keep collecting (19/30) |
| follow_move+pin_value | spread | 11-7 | 61.1 | 48.7 | 12.4 | +2.56 | 14.2 | 0.33 | 33.3 | keep collecting (18/30) |
| follow_move+money_moving | spread | 9-1 | 90.0 | 47.7 | 42.3 | +7.22 | 72.2 | 0.2 | 40.0 | keep collecting (10/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 52.8 | 13.8 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.8 | -52.8 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 19-14 | 57.6 | 49.1 | 8.5 | +3.34 | 10.1 | 0.09 | 36.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | total | 26-18 | 59.1 | 50.0 | 9.1 | +5.68 | 12.9 | 0.18 | 36.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | total | 20-12 | 62.5 | 50.8 | 11.7 | +6.14 | 19.2 | 0.25 | 31.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | total | 7-4 | 63.6 | 52.0 | 11.7 | +2.32 | 21.1 | 0.36 | 36.4 | keep collecting (11/30) |
| money_moving+pin_value | total | 4-3 | 57.1 | 50.6 | 6.5 | +0.56 | 8.0 | 0.29 | 28.6 | keep collecting (7/30) |
| pin_value+sharp_gap | total | 10-5 | 66.7 | 50.9 | 15.8 | +4.01 | 26.7 | 0.0 | 33.3 | keep collecting (15/30) |
| follow_move+money_level | total | 16-16 | 50.0 | 48.7 | 1.3 | -1.47 | -4.6 | 0.38 | 40.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.1 | -2.5 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 5-4 | 55.6 | 53.3 | 2.2 | +0.59 | 6.5 | 0.33 | 44.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 17-12 | 58.6 | 50.4 | 8.2 | +3.46 | 11.9 | 0.45 | 41.4 | keep collecting (29/30) |
| money_level+rlm_ratio | total | 4-2 | 66.7 | 54.3 | 12.4 | +1.68 | 28.0 | 0.83 | 50.0 | keep collecting (6/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 51.4 | 15.2 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 5-4 | 55.6 | 53.3 | 2.2 | +0.59 | 6.5 | 0.33 | 44.4 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 9-11 | 45.0 | 49.6 | -4.6 | -2.8 | -14.0 | 0.45 | 45.0 | keep collecting (20/30) |
| consensus_gap+money_level | total | 3-3 | 50.0 | 48.6 | 1.4 | -0.34 | -5.7 | -0.17 | 16.7 | keep collecting (6/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 47.4 | 32.6 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 49.0 | -15.6 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 4-6 | 40.0 | 50.9 | -10.9 | -2.44 | -24.4 | -0.1 | 20.0 | keep collecting (10/30) |
| money_moving+rlm_ratio | total | 2-3 | 40.0 | 52.6 | -12.6 | -1.14 | -22.8 | 0.2 | 40.0 | keep collecting (5/30) |
| consensus_gap+follow_move | total | 8-8 | 50.0 | 48.9 | 1.1 | -0.76 | -4.8 | 1.25 | 62.5 | keep collecting (16/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 54.3 | -54.3 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 1-1 | 50.0 | 54.3 | -4.3 | -0.09 | -4.5 | 0.5 | 50.0 | keep collecting (2/30) |

## CLOSE  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 100-106 | 48.5 | 42.9 | 5.6 | +26.73 | 13.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | both | 652-576 | 53.1 | 52.0 | 1.1 | -69.75 | -5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | both | 151-161 | 48.4 | 45.0 | 3.4 | +9.17 | 2.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | both | 796-605 | 56.8 | 55.4 | 1.4 | -68.72 | -4.9 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 621-734 | 45.8 | 47.3 | -1.5 | -92.36 | -6.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | both | 617-739 | 45.5 | 47.5 | -2.0 | -105.46 | -7.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | both | 264-275 | 49.0 | 47.2 | 1.8 | -10.88 | -2.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 50.9 | 15.7 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 257-380 | 40.3 | 45.9 | -5.6 | -86.46 | -13.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+follow_move | both | 101-113 | 47.2 | 49.8 | -2.6 | -20.2 | -9.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_moving | both | 110-206 | 34.8 | 42.8 | -8.0 | -30.55 | -9.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_rlm | both | 18-32 | 36.0 | 36.1 | -0.1 | +12.56 | 25.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_value | both | 104-130 | 44.4 | 44.1 | 0.4 | -10.63 | -4.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | both | 20-38 | 34.5 | 38.4 | -4.0 | -1.02 | -1.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | both | 111-210 | 34.6 | 42.4 | -7.8 | -31.38 | -9.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_moving | both | 346-379 | 47.7 | 49.2 | -1.5 | -59.47 | -8.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_rlm | both | 81-77 | 51.3 | 45.3 | 6.0 | +7.88 | 5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | both | 97-91 | 51.6 | 47.9 | 3.7 | -4.48 | -2.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | both | 151-161 | 48.4 | 45.0 | 3.4 | +9.17 | 2.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 350-374 | 48.3 | 49.2 | -0.8 | -50.85 | -7.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_rlm | both | 97-105 | 48.0 | 42.8 | 5.2 | +24.99 | 12.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | both | 113-138 | 45.0 | 46.2 | -1.2 | -11.31 | -4.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | both | 147-157 | 48.4 | 45.0 | 3.3 | +9.43 | 3.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | both | 596-711 | 45.6 | 47.3 | -1.7 | -92.26 | -7.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+pin_value | both | 28-26 | 51.9 | 45.2 | 6.7 | +16.74 | 31.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_ratio | both | 81-77 | 51.3 | 45.3 | 6.0 | +7.88 | 5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | both | 100-106 | 48.5 | 42.9 | 5.6 | +26.73 | 13.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 28-22 | 56.0 | 48.7 | 7.3 | +3.7 | 7.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | both | 115-137 | 45.6 | 46.3 | -0.7 | -8.55 | -3.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio+sharp_gap | both | 151-161 | 48.4 | 45.0 | 3.4 | +9.17 | 2.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+money_moving | both | 435-409 | 51.5 | 52.0 | -0.5 | -48.42 | -5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | both | 435-404 | 51.8 | 51.9 | -0.1 | -40.24 | -4.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | both | 435-318 | 57.8 | 56.3 | 1.5 | -46.7 | -6.2 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 78-62 | 55.7 | 49.4 | 6.3 | +11.66 | 8.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | both | 156-139 | 52.9 | 56.3 | -3.4 | -26.12 | -8.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | both | 123-125 | 49.6 | 48.7 | 0.9 | -18.15 | -7.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | both | 47-31 | 60.3 | 48.5 | 11.8 | +13.99 | 17.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 54.3 | 45.7 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 26-53 | 32.9 | 27.7 | 5.2 | +11.98 | 15.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm | spread | 17-16 | 51.5 | 51.1 | 0.4 | -0.62 | -1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm | total | 57-37 | 60.6 | 52.8 | 7.8 | +15.36 | 16.3 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move | moneyline | 235-152 | 60.7 | 57.3 | 3.4 | -24.57 | -6.3 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 192-193 | 49.9 | 49.1 | 0.8 | -19.46 | -5.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | total | 225-231 | 49.3 | 50.0 | -0.7 | -25.72 | -5.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | moneyline | 26-64 | 28.9 | 28.5 | 0.3 | -8.07 | -9.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio | spread | 33-34 | 49.3 | 50.0 | -0.8 | -3.97 | -5.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | total | 92-63 | 59.4 | 52.4 | 7.0 | +21.21 | 13.7 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level | moneyline | 312-113 | 73.4 | 69.8 | 3.6 | -14.87 | -3.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 231-245 | 48.5 | 49.0 | -0.5 | -36.88 | -7.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level | total | 253-247 | 50.6 | 49.3 | 1.3 | -16.98 | -3.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 138-254 | 35.2 | 40.1 | -4.9 | -51.15 | -13.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| sharp_gap | spread | 239-231 | 50.9 | 49.5 | 1.3 | -15.18 | -3.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 244-249 | 49.5 | 51.0 | -1.5 | -26.04 | -5.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | moneyline | 142-248 | 36.4 | 40.8 | -4.4 | -45.82 | -11.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | spread | 236-234 | 50.2 | 49.4 | 0.8 | -21.05 | -4.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | total | 239-257 | 48.2 | 50.8 | -2.7 | -38.6 | -7.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | moneyline | 13-44 | 22.8 | 28.4 | -5.6 | -2.9 | -5.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | spread | 124-111 | 52.8 | 49.6 | 3.2 | -2.24 | -1.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 127-120 | 51.4 | 49.1 | 2.3 | -5.73 | -2.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.8 | 47.2 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 104-224 | 31.7 | 43.7 | -12.0 | -63.89 | -19.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 72-65 | 52.6 | 49.0 | 3.6 | -3.46 | -2.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap | total | 81-91 | 47.1 | 47.7 | -0.6 | -19.11 | -11.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | moneyline | 95-61 | 60.9 | 63.0 | -2.1 | -8.33 | -5.3 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 91-60 | 60.3 | 62.6 | -2.4 | -7.83 | -5.2 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 128-238 | 35.0 | 39.8 | -4.9 | -44.29 | -12.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+follow_move | moneyline | 39-57 | 40.6 | 52.5 | -11.9 | -17.96 | -18.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | moneyline | 70-50 | 58.3 | 68.9 | -10.6 | -11.95 | -10.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | moneyline | 36-128 | 22.0 | 37.6 | -15.7 | -16.8 | -10.2 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+money_level | moneyline | 188-59 | 76.1 | 71.4 | 4.7 | -11.11 | -4.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move+money_moving | moneyline | 71-86 | 45.2 | 47.1 | -1.9 | -15.71 | -10.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 37-133 | 21.8 | 36.9 | -15.2 | -18.65 | -11.0 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+sharp_gap | moneyline | 70-85 | 45.2 | 46.4 | -1.3 | -15.84 | -10.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_rlm | moneyline | 10-22 | 31.2 | 28.9 | 2.4 | +15.65 | 48.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 4-26 | 13.3 | 29.1 | -15.8 | -3.04 | -10.1 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_rlm | moneyline | 16-31 | 34.0 | 28.9 | 5.1 | -5.85 | -12.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 26-64 | 28.9 | 28.5 | 0.3 | -8.07 | -9.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_rlm | moneyline | 26-52 | 33.3 | 27.7 | 5.6 | +12.98 | 16.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 26-61 | 29.9 | 28.6 | 1.2 | -5.07 | -5.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 16-31 | 34.0 | 28.9 | 5.1 | -5.85 | -12.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 26-53 | 32.9 | 27.7 | 5.2 | +11.98 | 15.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 26-64 | 28.9 | 28.5 | 0.3 | -8.07 | -9.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 12-38 | 24.0 | 28.8 | -4.8 | +1.58 | 3.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_value | moneyline | 7-28 | 20.0 | 25.9 | -5.9 | +5.27 | 15.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+pin_value | moneyline | 5-8 | 38.5 | 25.9 | 12.6 | +14.07 | 108.2 |  |  | keep collecting (13/30) |
| pin_value+sharp_gap | moneyline | 7-28 | 20.0 | 25.9 | -5.9 | +5.27 | 15.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_rlm | moneyline | 8-7 | 53.3 | 32.3 | 21.0 | +2.35 | 15.6 |  |  | keep collecting (15/30) |
| money_level+rlm_ratio | moneyline | 10-8 | 55.6 | 36.6 | 19.0 | +3.72 | 20.6 |  |  | keep collecting (18/30) |
| money_level+pin_value | moneyline | 3-1 | 75.0 | 62.1 | 12.9 | +0.31 | 7.8 |  |  | keep collecting (4/30) |
| follow_move+pin_value | moneyline | 1-7 | 12.5 | 25.9 | -13.4 | -5.48 | -68.5 |  |  | keep collecting (8/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 25.9 | -0.9 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 31-24 | 56.4 | 48.1 | 8.3 | +2.4 | 4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | spread | 39-35 | 52.7 | 48.8 | 3.9 | -1.68 | -2.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 49-40 | 55.1 | 48.9 | 6.1 | +1.7 | 1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_ratio | spread | 2-4 | 33.3 | 50.0 | -16.7 | -2.33 | -38.9 |  |  | keep collecting (6/30) |
| consensus_gap+sharp_gap | spread | 38-35 | 52.1 | 49.1 | 2.9 | -2.58 | -3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | spread | 123-125 | 49.6 | 48.9 | 0.7 | -14.36 | -5.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_rlm | spread | 15-15 | 50.0 | 50.9 | -0.9 | -1.37 | -4.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | spread | 48-39 | 55.2 | 48.7 | 6.5 | +2.87 | 3.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | spread | 33-34 | 49.3 | 50.0 | -0.8 | -3.97 | -5.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 124-124 | 50.0 | 48.9 | 1.1 | -12.23 | -4.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | spread | 15-16 | 48.4 | 51.0 | -2.6 | -2.44 | -7.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | spread | 58-57 | 50.4 | 49.1 | 1.3 | -6.77 | -5.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_ratio | spread | 31-33 | 48.4 | 49.9 | -1.5 | -4.9 | -7.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | spread | 231-226 | 50.5 | 49.5 | 1.1 | -17.55 | -3.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+pin_value | spread | 6-7 | 46.2 | 50.2 | -4.1 | -1.79 | -13.8 |  |  | keep collecting (13/30) |
| pin_rlm+rlm_ratio | spread | 15-15 | 50.0 | 50.9 | -0.9 | -1.37 | -4.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | spread | 17-16 | 51.5 | 51.1 | 0.4 | -0.62 | -1.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 5-6 | 45.5 | 49.2 | -3.8 | -1.72 | -15.6 |  |  | keep collecting (11/30) |
| pin_value+sharp_gap | spread | 58-57 | 50.4 | 49.2 | 1.2 | -6.84 | -5.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | spread | 33-34 | 49.3 | 50.0 | -0.8 | -3.97 | -5.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 118-124 | 48.8 | 48.5 | 0.3 | -17.91 | -7.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+rlm_ratio | spread | 17-19 | 47.2 | 49.5 | -2.3 | -3.71 | -10.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | spread | 180-179 | 50.1 | 49.1 | 1.1 | -16.91 | -4.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | spread | 48-40 | 54.5 | 48.6 | 6.0 | +1.17 | 1.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | spread | 179-180 | 49.9 | 49.0 | 0.8 | -18.83 | -5.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | spread | 62-65 | 48.8 | 48.8 | 0.0 | -11.37 | -9.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_rlm | spread | 8-6 | 57.1 | 50.4 | 6.7 | +1.1 | 7.9 |  |  | keep collecting (14/30) |
| money_level+money_moving | total | 161-168 | 48.9 | 50.1 | -1.2 | -21.27 | -6.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | total | 164-165 | 49.8 | 50.2 | -0.3 | -15.51 | -4.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | total | 237-247 | 49.0 | 50.9 | -2.0 | -30.42 | -6.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | total | 38-49 | 43.7 | 46.7 | -3.0 | -15.34 | -17.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_value | total | 43-52 | 45.3 | 47.5 | -2.2 | -13.91 | -14.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | total | 152-168 | 47.5 | 50.6 | -3.1 | -29.4 | -9.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+sharp_gap | total | 156-165 | 48.6 | 50.7 | -2.1 | -22.78 | -7.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | total | 58-59 | 49.6 | 48.1 | 1.5 | -7.09 | -6.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | total | 129-135 | 48.9 | 49.3 | -0.5 | -17.68 | -6.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 48-45 | 51.6 | 49.1 | 2.5 | -1.87 | -2.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | total | 48-53 | 47.5 | 50.0 | -2.4 | -9.81 | -9.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | total | 50-52 | 49.0 | 50.1 | -1.1 | -6.99 | -6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | total | 35-43 | 44.9 | 47.8 | -2.9 | -12.06 | -15.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+sharp_gap | total | 36-42 | 46.2 | 47.9 | -1.8 | -10.15 | -13.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+follow_move | total | 31-32 | 49.2 | 47.1 | 2.1 | -4.64 | -7.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pin_rlm | total | 5-7 | 41.7 | 48.6 | -6.9 | -2.6 | -21.7 |  |  | keep collecting (12/30) |
| consensus_gap+rlm_ratio | total | 14-8 | 63.6 | 48.0 | 15.6 | +4.35 | 19.8 |  |  | keep collecting (22/30) |
| follow_move+pin_rlm | total | 50-31 | 61.7 | 52.7 | 9.0 | +15.1 | 18.6 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move+rlm_ratio | total | 92-63 | 59.4 | 52.4 | 7.0 | +21.21 | 13.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 31-18 | 63.3 | 52.9 | 10.4 | +10.54 | 21.5 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 51-35 | 59.3 | 52.0 | 7.3 | +11.65 | 13.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | total | 56-37 | 60.2 | 52.8 | 7.4 | +14.45 | 15.5 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+rlm_ratio | total | 90-63 | 58.8 | 52.3 | 6.5 | +19.41 | 12.7 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| pin_rlm+pin_value | total | 17-11 | 60.7 | 51.8 | 8.9 | +4.46 | 15.9 |  |  | keep collecting (28/30) |
| pin_rlm+rlm_ratio | total | 50-31 | 61.7 | 52.7 | 9.0 | +15.1 | 18.6 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| pin_rlm+sharp_gap | total | 57-37 | 60.6 | 52.8 | 7.8 | +15.36 | 16.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 22-13 | 62.9 | 51.1 | 11.8 | +6.89 | 19.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | total | 92-63 | 59.4 | 52.4 | 7.0 | +21.21 | 13.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 54.3 | 45.7 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

# Pooled (fit + forward together)

Kept for continuity. **Contaminated** — it mixes the games the engine was built
on with the games testing it. Use the forward table for any decision.

## EARLY  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 1-2 | 33.3 | 25.7 | 7.6 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | both | 456-392 | 53.8 | 52.6 | 1.2 | -49.13 | -5.8 | 0.22 | 42.5 | no edge shown yet |
| rlm_ratio | both | 25-16 | 61.0 | 37.4 | 23.6 | +17.63 | 43.0 | 0.35 | 51.2 | no edge shown yet |
| money_level | both | 162-100 | 61.8 | 59.3 | 2.5 | -7.12 | -2.7 | -0.08 | 39.3 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 135-113 | 54.4 | 48.3 | 6.2 | +16.54 | 6.7 | 0.23 | 42.7 | no edge shown yet |
| money_moving | both | 99-71 | 58.2 | 51.6 | 6.6 | +7.79 | 4.6 | 0.07 | 42.9 | PROMOTE: beats break-even and its own base rate |
| pin_value | both | 49-48 | 50.5 | 48.3 | 2.3 | -4.43 | -4.6 | 0.1 | 38.1 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.2 | -31.2 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 214-282 | 43.1 | 46.8 | -3.7 | -57.53 | -11.6 | 0.39 | 45.4 | DROP: below break-even |
| consensus_gap+money_level | both | 31-26 | 54.4 | 64.1 | -9.7 | -8.54 | -15.0 | 0.29 | 47.4 | no edge shown yet |
| consensus_gap+money_moving | both | 17-22 | 43.6 | 46.6 | -3.0 | -5.42 | -13.9 | 0.21 | 41.0 | no edge shown yet |
| consensus_gap+pin_value | both | 19-28 | 40.4 | 46.4 | -5.9 | -11.54 | -24.5 | 0.39 | 48.9 | DROP: below break-even |
| follow_move+rlm_ratio | both | 25-16 | 61.0 | 37.4 | 23.6 | +17.63 | 43.0 | 0.35 | 51.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 68-36 | 65.4 | 49.9 | 15.5 | +20.61 | 19.8 | 0.36 | 48.1 | PROMOTE: beats break-even and its own base rate |
| money_level+money_moving | both | 63-35 | 64.3 | 58.4 | 5.9 | +4.04 | 4.1 | -0.13 | 46.9 | PROMOTE: beats break-even and its own base rate |
| money_level+pin_value | both | 11-9 | 55.0 | 50.0 | 5.0 | +0.81 | 4.0 | 0.4 | 45.0 | keep collecting (20/30) |
| money_moving+pin_value | both | 8-5 | 61.5 | 50.0 | 11.5 | +2.04 | 15.7 | 0.31 | 38.5 | keep collecting (13/30) |
| rlm_ratio+sharp_gap | both | 25-16 | 61.0 | 37.4 | 23.6 | +17.63 | 43.0 | 0.35 | 51.2 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 94-57 | 62.3 | 55.6 | 6.7 | +5.37 | 3.6 | 0.13 | 43.0 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | both | 58-43 | 57.4 | 48.8 | 8.6 | +8.96 | 8.9 | 0.16 | 45.5 | no edge shown yet |
| pin_value+sharp_gap | both | 13-8 | 61.9 | 48.9 | 13.0 | +3.66 | 17.4 | -0.18 | 33.3 | keep collecting (21/30) |
| consensus_gap+follow_move | both | 30-38 | 44.1 | 51.4 | -7.3 | -13.76 | -20.2 | 0.8 | 57.4 | no edge shown yet |
| follow_move+pin_value | both | 20-17 | 54.1 | 48.8 | 5.3 | +0.41 | 1.1 | -0.12 | 29.7 | no edge shown yet |
| consensus_gap+sharp_gap | both | 24-44 | 35.3 | 44.5 | -9.2 | -11.04 | -16.2 | 0.92 | 50.0 | DROP: below break-even |
| follow_move+money_level | both | 86-41 | 67.7 | 60.4 | 7.3 | +1.27 | 1.0 | 0.09 | 44.1 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 11-6 | 64.7 | 40.7 | 24.0 | +5.43 | 31.9 | 1.18 | 58.8 | keep collecting (17/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 44.2 | 5.8 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 50-25 | 66.7 | 53.4 | 13.3 | +11.4 | 15.2 | 0.39 | 53.3 | PROMOTE: beats break-even and its own base rate |
| money_moving+rlm_ratio | both | 11-6 | 64.7 | 40.3 | 24.4 | +7.71 | 45.4 | 0.17 | 47.1 | keep collecting (17/30) |
| consensus_gap+rlm_ratio | both | 3-4 | 42.9 | 36.6 | 6.3 | -0.82 | -11.7 | 0.93 | 71.4 | keep collecting (7/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 25.7 | 24.3 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 25.7 | 24.3 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | both | 1-2 | 33.3 | 25.7 | 7.6 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.5 | -51.5 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 25.7 | 74.3 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-2 | 33.3 | 25.7 | 7.6 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | moneyline | 186-123 | 60.2 | 57.3 | 2.9 | -27.55 | -8.9 | 0.24 | 46.9 | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 127-135 | 48.5 | 49.7 | -1.3 | -18.11 | -6.9 | 0.03 | 34.4 | no edge shown yet |
| follow_move | total | 143-134 | 51.6 | 49.9 | 1.7 | -3.46 | -1.2 | 0.37 | 45.1 | no edge shown yet |
| rlm_ratio | moneyline | 12-10 | 54.5 | 25.7 | 28.8 | +11.57 | 52.6 | 0.39 | 59.1 | keep collecting (22/30) |
| rlm_ratio | spread | 3-2 | 60.0 | 51.2 | 8.8 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 10-4 | 71.4 | 50.8 | 20.6 | +5.22 | 37.3 | 0.64 | 57.1 | keep collecting (14/30) |
| money_level | moneyline | 93-36 | 72.1 | 69.4 | 2.7 | -5.69 | -4.4 | -0.16 | 45.7 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-16 | 51.5 | 49.3 | 2.2 | -0.69 | -2.1 | 0.85 | 48.5 | no edge shown yet |
| money_level | total | 52-48 | 52.0 | 49.6 | 2.4 | -0.74 | -0.7 | -0.29 | 28.0 | no edge shown yet |
| sharp_gap | moneyline | 57-59 | 49.1 | 46.2 | 2.9 | -0.32 | -0.3 | 0.26 | 49.1 | no edge shown yet |
| sharp_gap | spread | 20-14 | 58.8 | 49.8 | 9.1 | +4.0 | 11.8 | 0.65 | 38.2 | no edge shown yet |
| sharp_gap | total | 58-40 | 59.2 | 50.2 | 9.0 | +12.86 | 13.1 | 0.05 | 36.7 | no edge shown yet |
| money_moving | moneyline | 42-38 | 52.5 | 53.6 | -1.1 | -10.85 | -13.6 | -0.14 | 48.8 | no edge shown yet |
| money_moving | spread | 18-4 | 81.8 | 49.3 | 32.5 | +12.18 | 55.3 | 0.23 | 40.9 | keep collecting (22/30) |
| money_moving | total | 39-29 | 57.4 | 50.0 | 7.4 | +6.46 | 9.5 | 0.25 | 36.8 | no edge shown yet |
| pin_value | moneyline | 2-6 | 25.0 | 31.8 | -6.8 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| pin_value | spread | 24-20 | 54.5 | 49.6 | 5.0 | +1.16 | 2.6 | 0.25 | 38.6 | no edge shown yet |
| pin_value | total | 23-22 | 51.1 | 49.9 | 1.2 | -1.28 | -2.9 | -0.02 | 35.6 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.0 | -18.6 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 87-161 | 35.1 | 44.1 | -9.0 | -49.06 | -19.8 | 0.13 | 42.3 | DROP: below break-even |
| consensus_gap | spread | 63-57 | 52.5 | 49.3 | 3.2 | -1.92 | -1.6 | 0.35 | 40.8 | no edge shown yet |
| consensus_gap | total | 64-64 | 50.0 | 49.8 | 0.2 | -6.56 | -5.1 | 0.93 | 55.5 | no edge shown yet |
| money_level+sharp_gap | moneyline | 44-18 | 71.0 | 64.1 | 6.9 | -1.02 | -1.6 | 0.07 | 54.8 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+follow_move | moneyline | 10-21 | 32.3 | 53.9 | -21.7 | -14.52 | -46.9 | 0.26 | 58.1 | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 31.8 | -6.8 | -4.31 | -53.8 | -0.08 | 50.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 41.9 | -8.6 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| money_level+money_moving | moneyline | 29-12 | 70.7 | 70.7 | 0.0 | -4.0 | -9.8 | -0.54 | 53.7 | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+sharp_gap | moneyline | 14-35 | 28.6 | 42.6 | -14.0 | -10.86 | -22.2 | 0.93 | 51.0 | DROP: below break-even |
| follow_move+money_level | moneyline | 55-15 | 78.6 | 69.4 | 9.2 | -0.93 | -1.3 | -0.1 | 48.6 | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 26-11 | 70.3 | 57.2 | 13.1 | +3.47 | 9.4 | 0.3 | 59.5 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 22-18 | 55.0 | 70.6 | -15.6 | -8.38 | -21.0 | 0.07 | 47.5 | INVERT candidate: wrong well beyond its base rate |
| follow_move+sharp_gap | moneyline | 33-17 | 66.0 | 50.0 | 16.0 | +7.74 | 15.5 | 0.27 | 56.0 | PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 21-24 | 46.7 | 47.3 | -0.6 | -5.63 | -12.5 | -0.05 | 53.3 | no edge shown yet |
| consensus_gap+money_moving | moneyline | 8-21 | 27.6 | 45.8 | -18.2 | -12.26 | -42.3 | 0.24 | 48.3 | keep collecting (29/30) |
| follow_move+rlm_ratio | moneyline | 12-10 | 54.5 | 25.7 | 28.8 | +11.57 | 52.6 | 0.39 | 59.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 12-10 | 54.5 | 25.7 | 28.8 | +11.57 | 52.6 | 0.39 | 59.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 25.7 | -0.7 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | moneyline | 4-3 | 57.1 | 25.7 | 31.4 | +4.22 | 60.3 | 0.27 | 57.1 | keep collecting (7/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-1 | 50.0 | 25.7 | 24.3 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-1 | 50.0 | 25.7 | 24.3 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | moneyline | 1-2 | 33.3 | 25.7 | 7.6 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| money_level+rlm_ratio | moneyline | 4-3 | 57.1 | 25.7 | 31.4 | +1.87 | 26.7 | 2.0 | 85.7 | keep collecting (7/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 25.7 | 74.3 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-5 | 50.0 | 48.0 | 2.0 | -0.68 | -6.8 | 1.7 | 70.0 | keep collecting (10/30) |
| consensus_gap+money_moving | spread | 5-0 | 100.0 | 48.0 | 52.0 | +4.32 | 86.3 | 0.6 | 40.0 | keep collecting (5/30) |
| consensus_gap+pin_value | spread | 10-8 | 55.6 | 48.9 | 6.6 | +0.6 | 3.3 | 0.5 | 50.0 | keep collecting (18/30) |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.2 | 8.8 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 49.0 | 13.5 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 10-4 | 71.4 | 48.9 | 22.5 | +5.12 | 36.6 | 0.86 | 64.3 | keep collecting (14/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 49.2 | -6.3 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 51.2 | 8.8 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | spread | 14-11 | 56.0 | 49.3 | 6.7 | +1.62 | 6.5 | 1.0 | 44.0 | keep collecting (25/30) |
| money_moving+sharp_gap | spread | 10-3 | 76.9 | 49.2 | 27.7 | +6.04 | 46.4 | 0.54 | 46.2 | keep collecting (13/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.3 | 17.3 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-9 | 50.0 | 48.7 | 1.3 | -1.2 | -6.7 | 0.89 | 44.4 | keep collecting (18/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 48.0 | 14.5 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 11-8 | 57.9 | 48.9 | 9.0 | +2.04 | 10.7 | 0.63 | 42.1 | keep collecting (19/30) |
| follow_move+pin_value | spread | 12-7 | 63.2 | 49.1 | 14.1 | +3.45 | 18.2 | 0.26 | 31.6 | keep collecting (19/30) |
| follow_move+money_moving | spread | 9-1 | 90.0 | 48.4 | 41.6 | +7.22 | 72.2 | 0.2 | 40.0 | keep collecting (10/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 52.0 | 14.7 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.0 | -52.0 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 24-19 | 55.8 | 49.7 | 6.1 | +2.92 | 6.8 | -0.05 | 34.9 | no edge shown yet |
| money_level+sharp_gap | total | 36-28 | 56.2 | 49.8 | 6.4 | +4.78 | 7.5 | -0.16 | 31.2 | no edge shown yet |
| money_moving+sharp_gap | total | 27-16 | 62.8 | 50.2 | 12.6 | +8.55 | 19.9 | 0.26 | 37.2 | no edge shown yet |
| money_level+pin_value | total | 8-5 | 61.5 | 50.4 | 11.1 | +2.23 | 17.2 | 0.23 | 30.8 | keep collecting (13/30) |
| money_moving+pin_value | total | 5-3 | 62.5 | 50.3 | 12.2 | +1.47 | 18.3 | 0.12 | 25.0 | keep collecting (8/30) |
| pin_value+sharp_gap | total | 11-6 | 64.7 | 50.2 | 14.5 | +3.92 | 23.1 | -0.06 | 29.4 | keep collecting (17/30) |
| follow_move+money_level | total | 20-18 | 52.6 | 49.5 | 3.1 | +0.17 | 0.4 | 0.16 | 36.8 | no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.8 | -3.1 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 10-4 | 71.4 | 50.8 | 20.6 | +5.22 | 37.3 | 0.64 | 57.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 25-13 | 65.8 | 50.1 | 15.7 | +9.78 | 25.7 | 0.37 | 42.1 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | total | 5-2 | 71.4 | 50.8 | 20.6 | +2.63 | 37.6 | 0.86 | 57.1 | keep collecting (7/30) |
| pin_value+rlm_ratio | total | 2-1 | 66.7 | 50.4 | 16.3 | +0.82 | 27.3 | -0.67 | 33.3 | keep collecting (3/30) |
| rlm_ratio+sharp_gap | total | 10-4 | 71.4 | 50.8 | 20.6 | +5.22 | 37.3 | 0.64 | 57.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_moving | total | 15-13 | 53.6 | 50.0 | 3.6 | +0.7 | 2.5 | 0.57 | 50.0 | keep collecting (28/30) |
| consensus_gap+money_level | total | 4-3 | 57.1 | 49.5 | 7.6 | +0.53 | 7.5 | -0.43 | 14.3 | keep collecting (7/30) |
| consensus_gap+money_moving | total | 4-1 | 80.0 | 49.3 | 30.7 | +2.53 | 50.5 | -0.4 | 0.0 | keep collecting (5/30) |
| consensus_gap+pin_value | total | 7-14 | 33.3 | 49.7 | -16.4 | -7.83 | -37.3 | 0.48 | 47.6 | keep collecting (21/30) |
| consensus_gap+sharp_gap | total | 5-6 | 45.5 | 50.3 | -4.8 | -1.49 | -13.5 | 0.0 | 27.3 | keep collecting (11/30) |
| money_moving+rlm_ratio | total | 5-3 | 62.5 | 50.5 | 12.0 | +1.63 | 20.4 | 0.38 | 50.0 | keep collecting (8/30) |
| consensus_gap+follow_move | total | 11-8 | 57.9 | 49.8 | 8.1 | +1.97 | 10.4 | 1.58 | 68.4 | keep collecting (19/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm_ratio | total | 2-1 | 66.7 | 51.1 | 15.6 | +0.86 | 28.7 | 0.67 | 66.7 | keep collecting (3/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 125-140 | 47.2 | 42.0 | 5.2 | +31.66 | 11.9 |  |  | DROP: below break-even |
| follow_move | both | 809-720 | 52.9 | 52.0 | 0.9 | -86.12 | -5.6 |  |  | no edge shown yet |
| rlm_ratio | both | 190-210 | 47.5 | 44.4 | 3.1 | +6.06 | 1.5 |  |  | DROP: below break-even |
| money_level | both | 1015-753 | 57.4 | 55.8 | 1.6 | -66.83 | -3.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 790-916 | 46.3 | 47.4 | -1.1 | -112.58 | -6.6 |  |  | DROP: below break-even |
| money_moving | both | 790-918 | 46.3 | 47.8 | -1.5 | -123.03 | -7.2 |  |  | DROP: below break-even |
| pin_value | both | 321-337 | 48.8 | 47.5 | 1.2 | -3.1 | -0.5 |  |  | DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 317-438 | 42.0 | 46.7 | -4.7 | -88.55 | -11.7 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 121-124 | 49.4 | 50.9 | -1.5 | -17.52 | -7.2 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 141-237 | 37.3 | 43.9 | -6.6 | -32.6 | -8.6 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | both | 23-38 | 37.7 | 36.8 | 0.9 | +11.03 | 18.1 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 123-143 | 46.2 | 44.9 | 1.3 | -1.2 | -0.5 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | both | 25-43 | 36.8 | 39.2 | -2.4 | -1.66 | -2.4 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 140-241 | 36.7 | 43.3 | -6.5 | -33.59 | -8.8 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 436-465 | 48.4 | 49.4 | -1.1 | -64.2 | -7.1 |  |  | DROP: below break-even |
| follow_move+pin_rlm | both | 99-100 | 49.7 | 44.1 | 5.6 | +10.3 | 5.2 |  |  | no edge shown yet |
| follow_move+pin_value | both | 110-109 | 50.2 | 48.7 | 1.6 | -10.92 | -5.0 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 190-210 | 47.5 | 44.4 | 3.1 | +6.06 | 1.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 441-461 | 48.9 | 49.3 | -0.4 | -53.09 | -5.9 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 119-137 | 46.5 | 42.0 | 4.5 | +28.7 | 11.2 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 139-170 | 45.0 | 46.8 | -1.8 | -14.93 | -4.8 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 182-204 | 47.2 | 44.4 | 2.7 | +4.15 | 1.1 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 757-881 | 46.2 | 47.5 | -1.3 | -106.26 | -6.5 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 38-34 | 52.8 | 45.7 | 7.1 | +17.72 | 24.6 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 99-100 | 49.7 | 44.1 | 5.6 | +10.3 | 5.2 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 125-140 | 47.2 | 42.0 | 5.2 | +31.66 | 11.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 35-27 | 56.5 | 48.6 | 7.9 | +4.96 | 8.0 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 142-171 | 45.4 | 46.7 | -1.3 | -13.26 | -4.2 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 190-210 | 47.5 | 44.4 | 3.1 | +6.06 | 1.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+money_moving | both | 561-503 | 52.7 | 52.5 | 0.2 | -46.41 | -4.4 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 554-495 | 52.8 | 52.3 | 0.5 | -38.17 | -3.6 |  |  | no edge shown yet |
| follow_move+money_level | both | 539-381 | 58.6 | 56.8 | 1.8 | -42.29 | -4.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 93-78 | 54.4 | 48.7 | 5.7 | +11.79 | 6.9 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 192-157 | 55.0 | 58.0 | -3.0 | -23.27 | -6.7 |  |  | no edge shown yet |
| money_level+pin_value | both | 150-152 | 49.7 | 49.6 | 0.1 | -21.82 | -7.2 |  |  | no edge shown yet |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_level+pin_rlm | both | 55-41 | 57.3 | 46.9 | 10.4 | +13.61 | 14.2 |  |  | no edge shown yet |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 51.1 | 48.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_rlm | moneyline | 32-66 | 32.7 | 27.2 | 5.4 | +20.64 | 21.1 |  |  | DROP: below break-even |
| pin_rlm | spread | 21-21 | 50.0 | 50.7 | -0.7 | -1.87 | -4.4 |  |  | no edge shown yet |
| pin_rlm | total | 72-53 | 57.6 | 50.7 | 6.9 | +12.89 | 10.3 |  |  | no edge shown yet |
| follow_move | moneyline | 294-192 | 60.5 | 56.7 | 3.8 | -26.96 | -5.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 237-244 | 49.3 | 49.6 | -0.3 | -28.83 | -6.0 |  |  | no edge shown yet |
| follow_move | total | 278-284 | 49.5 | 50.0 | -0.6 | -30.33 | -5.4 |  |  | no edge shown yet |
| rlm_ratio | moneyline | 34-80 | 29.8 | 29.1 | 0.7 | -6.42 | -5.6 |  |  | DROP: below break-even |
| rlm_ratio | spread | 41-40 | 50.6 | 50.1 | 0.5 | -2.76 | -3.4 |  |  | no edge shown yet |
| rlm_ratio | total | 115-90 | 56.1 | 50.6 | 5.5 | +15.24 | 7.4 |  |  | no edge shown yet |
| money_level | moneyline | 396-139 | 74.0 | 70.1 | 3.9 | -13.5 | -2.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 295-308 | 48.9 | 49.3 | -0.4 | -41.96 | -7.0 |  |  | DROP: below break-even |
| money_level | total | 324-306 | 51.4 | 49.8 | 1.6 | -11.37 | -1.8 |  |  | no edge shown yet |
| sharp_gap | moneyline | 181-310 | 36.9 | 41.3 | -4.4 | -59.31 | -12.1 |  |  | DROP: below break-even |
| sharp_gap | spread | 304-293 | 50.9 | 49.6 | 1.3 | -18.7 | -3.1 |  |  | no edge shown yet |
| sharp_gap | total | 305-313 | 49.4 | 50.2 | -0.9 | -34.57 | -5.6 |  |  | DROP: below break-even |
| money_moving | moneyline | 189-300 | 38.7 | 42.4 | -3.8 | -50.27 | -10.3 |  |  | DROP: below break-even |
| money_moving | spread | 301-296 | 50.4 | 49.6 | 0.8 | -24.57 | -4.1 |  |  | no edge shown yet |
| money_moving | total | 300-322 | 48.2 | 50.2 | -2.0 | -48.18 | -7.7 |  |  | DROP: below break-even |
| pin_value | moneyline | 17-51 | 25.0 | 28.6 | -3.6 | +13.19 | 19.4 |  |  | DROP: below break-even |
| pin_value | spread | 145-138 | 51.2 | 49.6 | 1.6 | -11.34 | -4.0 |  |  | no edge shown yet |
| pin_value | total | 159-148 | 51.8 | 49.8 | 2.0 | -4.95 | -1.6 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.0 | 48.0 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 135-264 | 33.8 | 44.2 | -10.4 | -73.2 | -18.3 |  |  | DROP: below break-even |
| consensus_gap | spread | 84-73 | 53.5 | 49.3 | 4.2 | -1.4 | -0.9 |  |  | no edge shown yet |
| consensus_gap | total | 98-101 | 49.2 | 49.5 | -0.2 | -13.95 | -7.0 |  |  | no edge shown yet |
| money_level+money_moving | moneyline | 134-75 | 64.1 | 64.3 | -0.2 | -5.04 | -2.4 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 125-73 | 63.1 | 63.7 | -0.6 | -4.65 | -2.3 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 167-286 | 36.9 | 41.2 | -4.3 | -46.55 | -10.3 |  |  | DROP: below break-even |
| consensus_gap+follow_move | moneyline | 50-64 | 43.9 | 53.0 | -9.1 | -19.13 | -16.8 |  |  | DROP: below break-even |
| consensus_gap+money_level | moneyline | 93-58 | 61.6 | 69.8 | -8.2 | -10.37 | -6.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 52-150 | 25.7 | 39.2 | -13.4 | -22.86 | -11.3 |  |  | DROP: below break-even |
| follow_move+money_level | moneyline | 234-70 | 77.0 | 71.6 | 5.4 | -7.87 | -2.6 |  |  | PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 94-107 | 46.8 | 48.2 | -1.4 | -16.72 | -8.3 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 50-155 | 24.4 | 38.0 | -13.7 | -25.74 | -12.6 |  |  | DROP: below break-even |
| follow_move+sharp_gap | moneyline | 91-106 | 46.2 | 47.2 | -1.0 | -16.14 | -8.2 |  |  | DROP: below break-even |
| consensus_gap+pin_rlm | moneyline | 10-27 | 27.0 | 28.4 | -1.3 | +10.65 | 28.8 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 4-30 | 11.8 | 28.6 | -16.8 | -7.04 | -20.7 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_rlm | moneyline | 21-37 | 36.2 | 28.2 | 8.0 | +1.71 | 2.9 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 34-80 | 29.8 | 29.1 | 0.7 | -6.42 | -5.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_rlm | moneyline | 31-64 | 32.6 | 27.3 | 5.4 | +21.24 | 22.4 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 33-76 | 30.3 | 29.3 | 1.0 | -3.82 | -3.5 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 21-37 | 36.2 | 28.2 | 8.0 | +1.71 | 2.9 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 32-66 | 32.7 | 27.2 | 5.4 | +20.64 | 21.1 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 34-80 | 29.8 | 29.1 | 0.7 | -6.42 | -5.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 13-43 | 23.2 | 28.3 | -5.1 | +3.38 | 6.0 |  |  | DROP: below break-even |
| money_moving+pin_value | moneyline | 9-30 | 23.1 | 27.0 | -3.9 | +10.76 | 27.6 |  |  | DROP: below break-even |
| pin_rlm+pin_value | moneyline | 5-9 | 35.7 | 25.7 | 10.0 | +13.07 | 93.4 |  |  | keep collecting (14/30) |
| pin_value+sharp_gap | moneyline | 9-32 | 22.0 | 26.9 | -5.0 | +8.76 | 21.4 |  |  | DROP: below break-even |
| money_level+pin_rlm | moneyline | 9-9 | 50.0 | 31.1 | 18.9 | +3.65 | 20.3 |  |  | keep collecting (18/30) |
| money_level+rlm_ratio | moneyline | 12-11 | 52.2 | 38.4 | 13.8 | +5.12 | 22.2 |  |  | keep collecting (23/30) |
| money_level+pin_value | moneyline | 4-1 | 80.0 | 64.6 | 15.4 | +1.0 | 19.9 |  |  | keep collecting (5/30) |
| follow_move+pin_value | moneyline | 1-7 | 12.5 | 25.7 | -13.2 | -5.48 | -68.5 |  |  | keep collecting (8/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 25.7 | -0.7 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 34-27 | 55.7 | 48.8 | 7.0 | +1.9 | 3.1 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 46-41 | 52.9 | 49.1 | 3.7 | -1.84 | -2.1 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 57-43 | 57.0 | 49.2 | 7.8 | +5.42 | 5.4 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 4-4 | 50.0 | 50.0 | 0.0 | -0.67 | -8.3 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | spread | 45-41 | 52.3 | 49.3 | 3.1 | -2.73 | -3.2 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 153-153 | 50.0 | 49.3 | 0.7 | -14.75 | -4.8 |  |  | no edge shown yet |
| follow_move+pin_rlm | spread | 17-17 | 50.0 | 50.6 | -0.6 | -1.48 | -4.4 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 53-45 | 54.1 | 49.2 | 4.9 | +1.19 | 1.2 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 41-40 | 50.6 | 50.1 | 0.5 | -2.76 | -3.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 154-152 | 50.3 | 49.4 | 0.9 | -12.61 | -4.1 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 19-21 | 47.5 | 50.7 | -3.2 | -3.69 | -9.2 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 70-73 | 49.0 | 49.3 | -0.4 | -12.67 | -8.9 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 39-39 | 50.0 | 50.0 | 0.0 | -3.69 | -4.7 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 296-288 | 50.7 | 49.6 | 1.1 | -21.08 | -3.6 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 6-9 | 40.0 | 50.4 | -10.4 | -3.79 | -25.3 |  |  | keep collecting (15/30) |
| pin_rlm+rlm_ratio | spread | 17-17 | 50.0 | 50.6 | -0.6 | -1.48 | -4.4 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 21-21 | 50.0 | 50.7 | -0.7 | -1.87 | -4.4 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 6-6 | 50.0 | 49.3 | 0.7 | -0.88 | -7.4 |  |  | keep collecting (12/30) |
| pin_value+sharp_gap | spread | 70-73 | 49.0 | 49.4 | -0.4 | -12.73 | -8.9 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 41-40 | 50.6 | 50.1 | 0.5 | -2.76 | -3.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 147-154 | 48.8 | 49.2 | -0.3 | -21.16 | -7.0 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 21-25 | 45.7 | 49.7 | -4.1 | -6.13 | -13.3 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 232-229 | 50.3 | 49.4 | 1.0 | -20.04 | -4.3 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 55-45 | 55.0 | 48.9 | 6.1 | +2.02 | 2.0 |  |  | no edge shown yet |
| money_level+money_moving | spread | 231-230 | 50.1 | 49.3 | 0.8 | -21.96 | -4.8 |  |  | no edge shown yet |
| money_level+pin_value | spread | 77-81 | 48.7 | 49.1 | -0.4 | -14.65 | -9.3 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 10-9 | 52.6 | 50.1 | 2.5 | -0.08 | -0.4 |  |  | keep collecting (19/30) |
| money_level+money_moving | total | 196-198 | 49.7 | 50.0 | -0.3 | -19.42 | -4.9 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 197-193 | 50.5 | 50.0 | 0.5 | -13.48 | -3.5 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 294-307 | 48.9 | 50.2 | -1.3 | -38.64 | -6.4 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 44-54 | 44.9 | 49.2 | -4.3 | -14.92 | -15.2 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 53-57 | 48.2 | 49.4 | -1.2 | -10.0 | -9.1 |  |  | no edge shown yet |
| follow_move+money_moving | total | 189-205 | 48.0 | 50.2 | -2.2 | -32.74 | -8.3 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 196-203 | 49.1 | 50.2 | -1.1 | -24.33 | -6.1 |  |  | no edge shown yet |
| money_level+pin_value | total | 69-70 | 49.6 | 49.5 | 0.1 | -8.16 | -5.9 |  |  | no edge shown yet |
| follow_move+money_level | total | 158-157 | 50.2 | 49.9 | 0.3 | -13.26 | -4.2 |  |  | no edge shown yet |
| follow_move+pin_value | total | 56-57 | 49.6 | 49.9 | -0.3 | -6.63 | -5.9 |  |  | no edge shown yet |
| money_moving+pin_value | total | 60-67 | 47.2 | 50.0 | -2.7 | -13.02 | -10.2 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 63-66 | 48.8 | 50.0 | -1.2 | -9.28 | -7.2 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 43-46 | 48.3 | 49.5 | -1.2 | -7.9 | -8.9 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 45-45 | 50.0 | 49.5 | 0.5 | -5.12 | -5.7 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 37-33 | 52.9 | 49.3 | 3.5 | -0.3 | -0.4 |  |  | no edge shown yet |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pin_rlm | total | 10-8 | 55.6 | 49.9 | 5.7 | +0.87 | 4.8 |  |  | keep collecting (18/30) |
| consensus_gap+rlm_ratio | total | 17-9 | 65.4 | 49.7 | 15.7 | +6.04 | 23.2 |  |  | keep collecting (26/30) |
| follow_move+pin_rlm | total | 61-46 | 57.0 | 50.7 | 6.3 | +10.07 | 9.4 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 115-90 | 56.1 | 50.6 | 5.5 | +15.24 | 7.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 36-23 | 61.0 | 50.7 | 10.3 | +10.04 | 17.0 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 60-42 | 58.8 | 50.5 | 8.4 | +12.81 | 12.6 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 69-52 | 57.0 | 50.7 | 6.3 | +11.15 | 9.2 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 110-89 | 55.3 | 50.6 | 4.7 | +11.66 | 5.9 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 27-16 | 62.8 | 50.5 | 12.3 | +8.44 | 19.6 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 61-46 | 57.0 | 50.7 | 6.3 | +10.07 | 9.4 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 72-53 | 57.6 | 50.7 | 6.9 | +12.89 | 10.3 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 28-18 | 60.9 | 50.4 | 10.5 | +7.32 | 15.9 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 115-90 | 56.1 | 50.6 | 5.5 | +15.24 | 7.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 51.1 | 48.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_rlm | close | 1-3k bets | 79-91 | 46.5 | 3.9 | 13.8 |  |
| pin_rlm | close | 3k+ bets | 25-28 | 47.2 | 5.8 | 6.6 |  |
| pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| pin_rlm | close | pin $1-2k | 54-56 | 49.1 | 5.5 | 13.6 |  |
| pin_rlm | close | pin $2k+ | 30-58 | 34.1 | -0.2 | -4.3 |  |
| pin_rlm | close | pin limit <$1k | 41-26 | 61.2 | 11.6 | 30.5 |  |
| follow_move | close | 1-3k bets | 522-453 | 53.5 | 2.0 | -3.9 |  |
| follow_move | close | 3k+ bets | 167-159 | 51.2 | -1.2 | -6.9 |  |
| follow_move | close | <1k bets | 120-108 | 52.6 | -0.7 | -11.2 |  |
| follow_move | close | pin $1-2k | 238-262 | 47.6 | -3.7 | -11.3 |  |
| follow_move | close | pin $2k+ | 189-155 | 54.9 | 2.7 | -3.5 |  |
| follow_move | close | pin limit <$1k | 103-102 | 50.2 | 0.1 | -4.1 |  |
| rlm_ratio | close | 1-3k bets | 122-149 | 45.0 | 0.4 | -2.9 |  |
| rlm_ratio | close | 3k+ bets | 42-35 | 54.5 | 10.3 | 17.4 |  |
| rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.8 | 0.8 |  |
| rlm_ratio | close | pin $1-2k | 63-64 | 49.6 | 3.3 | 4.9 |  |
| rlm_ratio | close | pin $2k+ | 32-46 | 41.0 | 3.9 | -7.9 |  |
| rlm_ratio | close | pin limit <$1k | 44-32 | 57.9 | 7.8 | 11.8 |  |
| money_level | close | 1-3k bets | 661-463 | 58.8 | 3.0 | -1.5 |  |
| money_level | close | 3k+ bets | 210-171 | 55.1 | -0.4 | -5.1 |  |
| money_level | close | <1k bets | 144-118 | 55.0 | -1.1 | -11.5 |  |
| money_level | close | pin $1-2k | 287-262 | 52.3 | -1.9 | -7.2 |  |
| money_level | close | pin $2k+ | 240-187 | 56.2 | -1.6 | -8.0 |  |
| money_level | close | pin limit <$1k | 119-117 | 50.4 | 0.4 | -4.1 |  |
| sharp_gap | close | 1-3k bets | 493-588 | 45.6 | -1.8 | -8.5 |  |
| sharp_gap | close | 3k+ bets | 183-190 | 49.1 | 1.7 | 4.7 |  |
| sharp_gap | close | <1k bets | 114-137 | 45.4 | -2.5 | -14.6 |  |
| sharp_gap | close | pin $1-2k | 252-281 | 47.3 | -1.4 | -5.6 |  |
| sharp_gap | close | pin $2k+ | 186-226 | 45.1 | -0.9 | -5.0 |  |
| sharp_gap | close | pin limit <$1k | 112-116 | 49.1 | -0.8 | -1.9 |  |
| money_moving | close | 1-3k bets | 496-587 | 45.8 | -2.1 | -9.1 |  |
| money_moving | close | 3k+ bets | 182-193 | 48.5 | 0.8 | 2.6 |  |
| money_moving | close | <1k bets | 112-137 | 45.0 | -2.5 | -13.5 |  |
| money_moving | close | pin $1-2k | 249-285 | 46.6 | -2.3 | -6.7 |  |
| money_moving | close | pin $2k+ | 188-223 | 45.7 | -0.3 | -4.0 |  |
| money_moving | close | pin limit <$1k | 108-122 | 47.0 | -2.9 | -6.0 |  |
| pin_value | close | 1-3k bets | 202-224 | 47.4 | -0.1 | -1.9 |  |
| pin_value | close | 3k+ bets | 65-69 | 48.5 | 0.5 | -4.0 |  |
| pin_value | close | <1k bets | 54-44 | 55.1 | 8.2 | 10.6 |  |
| pin_value | close | pin $1-2k | 149-174 | 46.1 | -1.9 | -6.0 |  |
| pin_value | close | pin $2k+ | 85-101 | 45.7 | 0.5 | -2.2 |  |
| pin_value | close | pin limit <$1k | 87-62 | 58.4 | 9.0 | 13.7 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 48.0 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 48.0 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 201-270 | 42.7 | -4.7 | -13.0 |  |
| consensus_gap | close | 3k+ bets | 76-89 | 46.1 | -1.0 | 5.9 |  |
| consensus_gap | close | <1k bets | 40-78 | 33.9 | -9.5 | -30.7 |  |
| consensus_gap | close | pin $1-2k | 101-118 | 46.1 | -2.7 | -3.6 |  |
| consensus_gap | close | pin $2k+ | 76-95 | 44.4 | -4.2 | -6.4 |  |
| consensus_gap | close | pin limit <$1k | 47-43 | 52.2 | 2.3 | 2.2 |  |
| consensus_gap+follow_move | close | 1-3k bets | 84-77 | 52.2 | 0.9 | -1.5 |  |
| consensus_gap+money_level | close | 1-3k bets | 133-91 | 59.4 | 0.5 | 1.7 |  |
| consensus_gap+money_moving | close | 1-3k bets | 93-148 | 38.6 | -6.1 | -10.6 |  |
| consensus_gap+pin_value | close | 1-3k bets | 78-99 | 44.1 | -1.1 | -5.0 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 91-151 | 37.6 | -6.2 | -11.8 |  |
| follow_move+money_level | close | 1-3k bets | 357-239 | 59.9 | 3.6 | -2.1 |  |
| follow_move+money_moving | close | 1-3k bets | 293-308 | 48.8 | -0.6 | -6.6 |  |
| follow_move+pin_value | close | 1-3k bets | 68-71 | 48.9 | 0.5 | -7.2 |  |
| follow_move+sharp_gap | close | 1-3k bets | 294-305 | 49.1 | 0.0 | -5.0 |  |
| money_level+money_moving | close | 1-3k bets | 361-316 | 53.3 | 0.8 | -3.0 |  |
| money_level+pin_value | close | 1-3k bets | 98-96 | 50.5 | 1.0 | -5.2 |  |
| money_level+sharp_gap | close | 1-3k bets | 352-311 | 53.1 | 0.9 | -2.5 |  |
| money_moving+pin_value | close | 1-3k bets | 92-117 | 44.0 | -3.1 | -7.7 |  |
| money_moving+sharp_gap | close | 1-3k bets | 472-562 | 45.6 | -1.9 | -8.2 |  |
| pin_value+sharp_gap | close | 1-3k bets | 95-121 | 44.0 | -2.9 | -8.1 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 17-26 | 39.5 | 2.0 | 19.2 |  |
| money_level+pin_rlm | close | 1-3k bets | 35-28 | 55.6 | 6.7 | 6.6 |  |
| pin_rlm+pin_value | close | 1-3k bets | 28-24 | 53.8 | 7.7 | 29.6 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 79-91 | 46.5 | 3.9 | 13.8 |  |
| money_moving+pin_rlm | close | 1-3k bets | 74-88 | 45.7 | 3.0 | 13.3 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 19-30 | 38.8 | -1.2 | 4.1 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 122-149 | 45.0 | 0.4 | -2.9 |  |
| money_level+rlm_ratio | close | 1-3k bets | 58-55 | 51.3 | 1.5 | -0.9 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 116-145 | 44.4 | -0.3 | -3.7 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 122-149 | 45.0 | 0.4 | -2.9 |  |
| follow_move+pin_rlm | close | 1-3k bets | 59-69 | 46.1 | 1.5 | -3.9 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 59-69 | 46.1 | 1.5 | -3.9 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 25-21 | 54.3 | 6.3 | 4.5 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 48.9 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 28-27 | 50.9 | 0.9 | -0.2 |  |
| consensus_gap+money_moving | close | 3k+ bets | 31-49 | 38.8 | -4.8 | 16.1 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-5 | 37.5 | -3.4 | 19.3 |  |
| consensus_gap+pin_value | close | 3k+ bets | 31-30 | 50.8 | 5.1 | 5.4 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -0.2 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 32-49 | 39.5 | -3.9 | 19.4 |  |
| follow_move+money_moving | close | 3k+ bets | 89-94 | 48.6 | -0.9 | -4.4 |  |
| follow_move+pin_rlm | close | 3k+ bets | 24-20 | 54.5 | 11.1 | 24.2 |  |
| follow_move+pin_value | close | 3k+ bets | 24-26 | 48.0 | -1.4 | -10.0 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 42-35 | 54.5 | 10.3 | 17.4 |  |
| follow_move+sharp_gap | close | 3k+ bets | 91-93 | 49.5 | 0.4 | -2.0 |  |
| money_moving+pin_rlm | close | 3k+ bets | 24-28 | 46.2 | 5.0 | 4.9 |  |
| money_moving+pin_value | close | 3k+ bets | 30-37 | 44.8 | -1.7 | -5.7 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 40-33 | 54.8 | 10.6 | 18.5 |  |
| money_moving+sharp_gap | close | 3k+ bets | 175-183 | 48.9 | 1.5 | 4.2 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-7 | 41.7 | -4.9 | -21.0 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 24-20 | 54.5 | 11.1 | 24.2 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 25-28 | 47.2 | 5.8 | 6.6 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 6-5 | 54.5 | 4.3 | 2.8 |  |
| pin_value+sharp_gap | close | 3k+ bets | 30-35 | 46.2 | -0.3 | -2.7 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 42-35 | 54.5 | 10.3 | 17.4 |  |
| money_level+money_moving | close | 3k+ bets | 124-109 | 53.2 | 0.8 | -1.3 |  |
| money_level+sharp_gap | close | 3k+ bets | 123-106 | 53.7 | 1.5 | 0.4 |  |
| follow_move+money_level | close | 3k+ bets | 107-83 | 56.3 | -0.6 | -4.9 |  |
| money_level+rlm_ratio | close | 3k+ bets | 22-10 | 68.8 | 21.6 | 41.7 |  |
| consensus_gap+money_level | close | 3k+ bets | 41-39 | 51.2 | -5.4 | -11.7 |  |
| money_level+pin_value | close | 3k+ bets | 34-39 | 46.6 | -3.0 | -13.9 |  |
| money_level+pin_rlm | close | 3k+ bets | 11-7 | 61.1 | 17.3 | 36.5 |  |
| money_level+money_moving | close | <1k bets | 76-77 | 49.7 | -3.0 | -14.4 |  |
| money_level+sharp_gap | close | <1k bets | 79-77 | 50.6 | -2.4 | -13.9 |  |
| money_moving+sharp_gap | close | <1k bets | 110-135 | 44.9 | -2.8 | -14.7 |  |
| consensus_gap+money_level | close | <1k bets | 18-27 | 40.0 | -16.1 | -39.4 |  |
| consensus_gap+money_moving | close | <1k bets | 17-40 | 29.8 | -11.4 | -34.9 |  |
| consensus_gap+pin_value | close | <1k bets | 14-14 | 50.0 | 8.4 | 15.4 |  |
| consensus_gap+sharp_gap | close | <1k bets | 17-41 | 29.3 | -11.7 | -36.0 |  |
| money_level+pin_value | close | <1k bets | 18-17 | 51.4 | 1.3 | -4.2 |  |
| money_moving+pin_value | close | <1k bets | 17-16 | 51.5 | 6.2 | 14.9 |  |
| pin_value+sharp_gap | close | <1k bets | 17-15 | 53.1 | 7.2 | 18.5 |  |
| follow_move+money_moving | close | <1k bets | 54-63 | 46.2 | -3.6 | -13.8 |  |
| follow_move+sharp_gap | close | <1k bets | 56-63 | 47.1 | -3.6 | -16.1 |  |
| follow_move+rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.8 | 0.8 |  |
| money_moving+rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.8 | 0.8 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 26-26 | 50.0 | 6.8 | 0.8 |  |
| follow_move+money_level | close | <1k bets | 75-59 | 56.0 | -2.7 | -15.1 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -0.6 | 12.2 |  |
| money_moving+pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| pin_rlm+sharp_gap | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| consensus_gap+follow_move | close | <1k bets | 9-20 | 31.0 | -19.2 | -51.4 |  |
| follow_move+pin_rlm | close | <1k bets | 16-11 | 59.3 | 16.1 | 17.3 |  |
| follow_move+pin_value | close | <1k bets | 18-12 | 60.0 | 11.2 | 13.8 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 21.3 | 60.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 16-11 | 59.3 | 16.1 | 17.3 |  |
| pin_value+rlm_ratio | close | <1k bets | 4-1 | 80.0 | 30.1 | 51.7 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 2-7 | 22.2 | -11.4 | -57.2 |  |
| money_level+rlm_ratio | close | <1k bets | 13-13 | 50.0 | 4.4 | -1.9 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 17.5 | 19.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 38-45 | 45.8 | -6.2 | -12.2 |  |
| consensus_gap+money_moving | close | pin $1-2k | 52-64 | 44.8 | -3.5 | -4.1 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-18 | 41.9 | 1.4 | 25.8 |  |
| consensus_gap+pin_value | close | pin $1-2k | 58-70 | 45.3 | -0.1 | -8.5 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-14 | 50.0 | 4.8 | 9.0 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 50-62 | 44.6 | -2.4 | -3.2 |  |
| follow_move+money_moving | close | pin $1-2k | 141-174 | 44.8 | -5.2 | -12.0 |  |
| follow_move+pin_rlm | close | pin $1-2k | 44-41 | 51.8 | 6.0 | 10.4 |  |
| follow_move+pin_value | close | pin $1-2k | 49-60 | 45.0 | -4.4 | -15.4 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 63-64 | 49.6 | 3.3 | 4.9 |  |
| follow_move+sharp_gap | close | pin $1-2k | 144-172 | 45.6 | -4.3 | -10.9 |  |
| money_moving+pin_rlm | close | pin $1-2k | 51-54 | 48.6 | 4.6 | 13.1 |  |
| money_moving+pin_value | close | pin $1-2k | 60-90 | 40.0 | -7.7 | -21.4 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 61-61 | 50.0 | 3.3 | 5.6 |  |
| money_moving+sharp_gap | close | pin $1-2k | 241-273 | 46.9 | -1.9 | -6.1 |  |
| pin_rlm+pin_value | close | pin $1-2k | 14-21 | 40.0 | -8.3 | -16.1 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 44-41 | 51.8 | 6.0 | 10.4 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 54-56 | 49.1 | 5.5 | 13.6 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 16-17 | 48.5 | -1.4 | -8.9 |  |
| pin_value+sharp_gap | close | pin $1-2k | 60-88 | 40.5 | -7.0 | -20.4 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 63-64 | 49.6 | 3.3 | 4.9 |  |
| follow_move+money_level | close | pin $1-2k | 167-163 | 50.6 | -3.9 | -11.5 |  |
| money_level+rlm_ratio | close | pin $1-2k | 38-31 | 55.1 | 6.6 | 7.6 |  |
| money_level+sharp_gap | close | pin $1-2k | 182-185 | 49.6 | -2.2 | -7.9 |  |
| money_level+money_moving | close | pin $1-2k | 182-189 | 49.1 | -2.9 | -8.9 |  |
| consensus_gap+money_level | close | pin $1-2k | 58-55 | 51.3 | -5.8 | -9.7 |  |
| money_level+pin_value | close | pin $1-2k | 64-75 | 46.0 | -3.8 | -14.0 |  |
| money_level+pin_rlm | close | pin $1-2k | 26-21 | 55.3 | 9.1 | 9.1 |  |
| follow_move+money_level | close | pin $2k+ | 122-75 | 61.9 | 2.0 | -1.5 |  |
| follow_move+money_moving | close | pin $2k+ | 92-92 | 50.0 | 2.4 | -4.4 |  |
| follow_move+sharp_gap | close | pin $2k+ | 93-94 | 49.7 | 2.1 | -4.6 |  |
| money_level+money_moving | close | pin $2k+ | 124-116 | 51.7 | -1.3 | -6.3 |  |
| money_level+sharp_gap | close | pin $2k+ | 124-118 | 51.2 | -1.8 | -6.6 |  |
| money_moving+sharp_gap | close | pin $2k+ | 182-220 | 45.3 | -0.7 | -4.2 |  |
| consensus_gap+money_moving | close | pin $2k+ | 28-55 | 33.7 | -8.1 | -6.0 |  |
| consensus_gap+pin_value | close | pin $2k+ | 32-42 | 43.2 | 2.7 | 9.7 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 29-58 | 33.3 | -9.5 | -8.8 |  |
| money_moving+pin_value | close | pin $2k+ | 46-55 | 45.5 | 1.6 | 8.1 |  |
| pin_value+sharp_gap | close | pin $2k+ | 46-56 | 45.1 | 1.3 | 7.0 |  |
| consensus_gap+follow_move | close | pin $2k+ | 23-24 | 48.9 | -2.3 | -19.0 |  |
| follow_move+pin_value | close | pin $2k+ | 28-26 | 51.9 | 5.5 | -1.3 |  |
| follow_move+pin_rlm | close | pin $2k+ | 23-38 | 37.7 | 1.3 | -11.5 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 32-46 | 41.0 | 3.9 | -7.9 |  |
| money_level+pin_rlm | close | pin $2k+ | 10-9 | 52.6 | 10.1 | 15.2 |  |
| money_level+pin_value | close | pin $2k+ | 45-45 | 50.0 | 0.6 | -7.7 |  |
| money_level+rlm_ratio | close | pin $2k+ | 11-10 | 52.4 | 5.7 | 12.4 |  |
| money_moving+pin_rlm | close | pin $2k+ | 30-58 | 34.1 | -0.2 | -4.3 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 32-45 | 41.6 | 4.3 | -6.7 |  |
| pin_rlm+pin_value | close | pin $2k+ | 5-10 | 33.3 | -1.1 | 31.2 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 23-38 | 37.7 | 1.3 | -11.5 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 30-58 | 34.1 | -0.2 | -4.3 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 3-5 | 37.5 | -0.9 | -22.1 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 32-46 | 41.0 | 3.9 | -7.9 |  |
| consensus_gap+money_level | close | pin $2k+ | 52-38 | 57.8 | -4.9 | -10.1 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-18 | 18.2 | -9.9 | -21.4 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-11 | 0.0 | -28.1 | -100.0 |  |
| money_level+money_moving | close | pin limit <$1k | 66-73 | 47.5 | -2.4 | -8.8 |  |
| money_level+sharp_gap | close | pin limit <$1k | 66-69 | 48.9 | -1.0 | -6.1 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 102-109 | 48.3 | -1.6 | -3.0 |  |
| consensus_gap+money_level | close | pin limit <$1k | 25-25 | 50.0 | -0.2 | -7.8 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 33-31 | 51.6 | 2.7 | 3.9 |  |
| follow_move+money_moving | close | pin limit <$1k | 63-72 | 46.7 | -3.3 | -10.3 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 68-71 | 48.9 | -1.1 | -6.0 |  |
| money_level+pin_value | close | pin limit <$1k | 41-32 | 56.2 | 6.9 | 6.3 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 16-10 | 61.5 | 11.5 | 12.5 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 20-17 | 54.1 | 5.3 | 14.0 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 22-18 | 55.0 | 6.0 | 14.8 |  |
| follow_move+money_level | close | pin limit <$1k | 52-54 | 49.1 | -1.2 | -6.6 |  |
| follow_move+pin_value | close | pin limit <$1k | 33-23 | 58.9 | 9.4 | 11.8 |  |
| money_moving+pin_value | close | pin limit <$1k | 33-25 | 56.9 | 7.7 | 15.6 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 36-27 | 57.1 | 7.7 | 15.5 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 6-2 | 75.0 | 28.4 | 96.7 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 38-25 | 60.3 | 10.8 | 29.7 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-3 | 86.4 | 37.2 | 84.9 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 41-26 | 61.2 | 11.6 | 30.5 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 32-21 | 60.4 | 10.1 | 16.1 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 44-32 | 57.9 | 7.8 | 11.8 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 40-31 | 56.3 | 6.3 | 8.9 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 32-21 | 60.4 | 10.1 | 16.1 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 44-32 | 57.9 | 7.8 | 11.8 |  |
| money_level+pin_rlm | close | pin limit <$1k | 19-11 | 63.3 | 12.5 | 21.5 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 21-14 | 60.0 | 9.9 | 16.8 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 16-5 | 76.2 | 25.7 | 46.1 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 5-3 | 62.5 | 12.8 | 18.4 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 48.9 | 87.7 |  |
| pin_rlm | early | <1k bets | 1-2 | 33.3 | 7.6 | -35.8 | -1.0 |
| pin_rlm | early | pin $1-2k | 0-2 | 0.0 | -25.7 | -100.0 | -1.75 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.2 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -50.4 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 377-315 | 54.5 | 2.1 | -5.7 | 0.24 |
| follow_move | early | pin $1-2k | 27-16 | 62.8 | 8.3 | 11.9 | -0.35 |
| follow_move | early | pin limit <$1k | 47-39 | 54.7 | 4.5 | 1.9 | -0.11 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 24.0 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.0 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 19-12 | 61.3 | 25.9 | 38.7 | 0.54 |
| rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.8 | 55.6 | -1.52 |
| rlm_ratio | early | pin limit <$1k | 7-1 | 87.5 | 43.3 | 77.5 | 0.29 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 0.5 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 42.2 | 59.7 | 0.33 |
| money_level | early | <1k bets | 133-80 | 62.4 | 2.4 | -2.7 | -0.11 |
| money_level | early | pin $1-2k | 20-8 | 71.4 | 5.2 | 4.1 | 0.01 |
| money_level | early | pin limit <$1k | 24-26 | 48.0 | -5.4 | -11.4 | 0.22 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 7.5 | 20.4 | 0.03 |
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
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 36-39 | 48.0 | -0.2 | -9.2 | 0.13 |
| pin_value | early | pin $1-2k | 13-18 | 41.9 | -3.6 | -21.1 | 0.12 |
| pin_value | early | pin limit <$1k | 36-30 | 54.5 | 5.0 | 3.2 | 0.09 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -48.9 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -26.7 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.2 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 13.1 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 172-228 | 43.0 | -4.1 | -13.9 | 0.35 |
| consensus_gap | early | pin $1-2k | 12-20 | 37.5 | -7.7 | -28.2 | 0.51 |
| consensus_gap | early | pin limit <$1k | 18-34 | 34.6 | -15.5 | -28.2 | 0.28 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 16.6 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 4.2 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 3.8 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.6 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.4 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.3 | 26.0 | -0.25 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -1.0 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 3.7 | -6.9 | 0.3 |
| follow_move+pin_value | early | 1-3k bets | 7-6 | 53.8 | 6.4 | 0.8 | -0.31 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.8 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.2 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 2.4 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.5 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 24.0 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 28.4 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 24.0 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.0 | 25.3 | 0.18 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.9 | 56.1 | 0.15 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 19.3 | 18.8 | -0.24 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -25.7 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.0 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.0 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 50.4 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.0 | 83.3 | 1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.0 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 37.3 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 48.9 | 95.2 | 0.0 |
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
| consensus_gap+pin_value | early | <1k bets | 13-23 | 36.1 | -10.2 | -32.5 | 0.4 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -25.7 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | <1k bets | 3-3 | 50.0 | 11.6 | 3.0 | 0.87 |
| follow_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 24.3 | -3.7 | -2.15 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -25.7 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 24.3 | -3.7 | -2.15 |
| pin_rlm+sharp_gap | early | <1k bets | 1-2 | 33.3 | 7.6 | -35.8 | -1.0 |
| pin_value+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 11.6 | -4.5 | -1.9 |
| pin_value+sharp_gap | early | <1k bets | 5-4 | 55.6 | 8.6 | 6.1 | -0.09 |
| money_level+pin_value | early | <1k bets | 4-4 | 50.0 | 0.3 | -4.5 | 0.88 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -51.5 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -51.1 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 1-2 | 33.3 | -17.3 | -36.4 | 1.33 |
| money_level+rlm_ratio | early | <1k bets | 7-5 | 58.3 | 22.2 | 22.3 | 1.67 |
| money_moving+rlm_ratio | early | <1k bets | 8-4 | 66.7 | 26.6 | 56.4 | 0.34 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -25.7 | -100.0 | 1.3 |
| consensus_gap+money_level | early | pin $1-2k | 5-4 | 55.6 | -10.0 | -12.6 | 0.71 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -32.2 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 5-10 | 33.3 | -7.8 | -38.7 | 0.31 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.8 | 55.6 | -1.52 |
| follow_move+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 13.6 | 37.5 | -0.83 |
| money_level+money_moving | early | pin $1-2k | 8-5 | 61.5 | -5.0 | -15.6 | 0.07 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.8 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-3 | 40.0 | 3.8 | 55.6 | -1.52 |
| money_level+sharp_gap | early | pin $1-2k | 12-4 | 75.0 | 9.8 | 12.5 | -0.26 |
| money_moving+sharp_gap | early | pin $1-2k | 4-6 | 40.0 | -17.1 | -45.4 | 0.08 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.6 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 4-6 | 40.0 | -10.0 | -31.3 | 0.34 |
| follow_move+pin_value | early | pin $1-2k | 6-5 | 54.5 | 7.1 | 0.8 | -0.3 |
| follow_move+money_level | early | pin $1-2k | 11-4 | 73.3 | 7.5 | 6.6 | -0.07 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 48.0 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 4-1 | 80.0 | 11.0 | 6.9 | -0.18 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.7 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.7 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 2-4 | 33.3 | -16.7 | -46.8 | -0.12 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.7 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -25.7 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.7 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -25.7 | -100.0 | -1.75 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.7 | -100.0 | -4.8 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.7 | -100.0 | 1.3 |
| money_level+money_moving | early | pin limit <$1k | 13-7 | 65.0 | 12.5 | 20.2 | 0.48 |
| money_level+sharp_gap | early | pin limit <$1k | 20-16 | 55.6 | 4.8 | 1.6 | 0.14 |
| money_moving+sharp_gap | early | pin limit <$1k | 18-5 | 78.3 | 30.2 | 70.1 | 0.35 |
| money_level+pin_value | early | pin limit <$1k | 9-6 | 60.0 | 9.6 | 13.8 | 0.33 |
| money_moving+pin_value | early | pin limit <$1k | 7-4 | 63.6 | 13.6 | 20.1 | 0.18 |
| pin_value+sharp_gap | early | pin limit <$1k | 12-6 | 66.7 | 16.6 | 26.4 | 0.0 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-9 | 40.0 | -12.0 | -25.7 | 0.53 |
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
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 22.9 | 72.3 | 0.54 |
| follow_move+money_moving | early | pin limit <$1k | 9-3 | 75.0 | 25.4 | 43.3 | 0.33 |
| money_moving+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.0 | 45.3 | -0.5 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -51.1 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -51.1 | -100.0 | 1.0 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| pin_rlm | close | 1-3k bets | 59-64 | 48.0 | 4.3 | 15.1 |  |
| pin_rlm | close | 3k+ bets | 20-22 | 47.6 | 6.4 | 6.1 |  |
| pin_rlm | close | <1k bets | 21-20 | 51.2 | 8.8 | 13.7 |  |
| pin_rlm | close | pin $1-2k | 44-41 | 51.8 | 7.1 | 20.4 |  |
| pin_rlm | close | pin $2k+ | 21-49 | 30.0 | -4.4 | -22.4 |  |
| pin_rlm | close | pin limit <$1k | 35-16 | 68.6 | 16.8 | 49.1 |  |
| follow_move | close | 1-3k bets | 408-344 | 54.3 | 2.7 | -3.2 |  |
| follow_move | close | 3k+ bets | 135-131 | 50.8 | -1.6 | -7.7 |  |
| follow_move | close | <1k bets | 109-101 | 51.9 | -1.4 | -11.9 |  |
| follow_move | close | pin $1-2k | 193-212 | 47.7 | -3.3 | -11.3 |  |
| follow_move | close | pin $2k+ | 150-132 | 53.2 | 1.4 | -7.8 |  |
| follow_move | close | pin limit <$1k | 92-80 | 53.5 | 2.8 | 2.1 |  |
| rlm_ratio | close | 1-3k bets | 94-111 | 45.9 | 0.4 | -1.6 |  |
| rlm_ratio | close | 3k+ bets | 33-28 | 54.1 | 10.2 | 16.3 |  |
| rlm_ratio | close | <1k bets | 24-22 | 52.2 | 8.0 | 5.7 |  |
| rlm_ratio | close | pin $1-2k | 54-49 | 52.4 | 5.4 | 9.3 |  |
| rlm_ratio | close | pin $2k+ | 25-42 | 37.3 | -0.1 | -20.9 |  |
| rlm_ratio | close | pin limit <$1k | 38-20 | 65.5 | 13.1 | 26.7 |  |
| money_level | close | 1-3k bets | 506-348 | 59.3 | 3.8 | -0.6 |  |
| money_level | close | 3k+ bets | 162-143 | 53.1 | -2.2 | -9.3 |  |
| money_level | close | <1k bets | 128-113 | 53.1 | -2.6 | -14.3 |  |
| money_level | close | pin $1-2k | 233-208 | 52.8 | -0.8 | -6.3 |  |
| money_level | close | pin $2k+ | 193-154 | 55.6 | -2.0 | -9.6 |  |
| money_level | close | pin limit <$1k | 96-97 | 49.7 | 0.3 | -5.3 |  |
| sharp_gap | close | 1-3k bets | 369-453 | 44.9 | -2.4 | -9.4 |  |
| sharp_gap | close | 3k+ bets | 146-154 | 48.7 | 1.9 | 5.8 |  |
| sharp_gap | close | <1k bets | 106-126 | 45.7 | -2.8 | -13.7 |  |
| sharp_gap | close | pin $1-2k | 209-221 | 48.6 | -0.2 | -2.5 |  |
| sharp_gap | close | pin $2k+ | 146-189 | 43.6 | -2.1 | -10.8 |  |
| sharp_gap | close | pin limit <$1k | 94-92 | 50.5 | -0.5 | 1.8 |  |
| money_moving | close | 1-3k bets | 368-455 | 44.7 | -2.8 | -10.4 |  |
| money_moving | close | 3k+ bets | 145-157 | 48.0 | 0.9 | 3.2 |  |
| money_moving | close | <1k bets | 104-126 | 45.2 | -2.7 | -12.5 |  |
| money_moving | close | pin $1-2k | 204-227 | 47.3 | -1.2 | -4.2 |  |
| money_moving | close | pin $2k+ | 148-186 | 44.3 | -1.3 | -9.5 |  |
| money_moving | close | pin limit <$1k | 91-97 | 48.4 | -2.3 | -2.3 |  |
| pin_value | close | 1-3k bets | 160-170 | 48.5 | 1.1 | -3.3 |  |
| pin_value | close | 3k+ bets | 55-61 | 47.4 | 0.2 | -5.2 |  |
| pin_value | close | <1k bets | 49-44 | 52.7 | 6.5 | 6.4 |  |
| pin_value | close | pin $1-2k | 124-139 | 47.1 | -0.6 | -7.5 |  |
| pin_value | close | pin $2k+ | 73-81 | 47.4 | 2.2 | -0.3 |  |
| pin_value | close | pin limit <$1k | 67-55 | 54.9 | 6.6 | 7.7 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 47.2 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 47.2 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 158-230 | 40.7 | -5.6 | -15.7 |  |
| consensus_gap | close | 3k+ bets | 62-78 | 44.3 | -2.3 | 4.5 |  |
| consensus_gap | close | <1k bets | 37-71 | 34.3 | -9.3 | -28.7 |  |
| consensus_gap | close | pin $1-2k | 81-104 | 43.8 | -3.8 | -5.0 |  |
| consensus_gap | close | pin $2k+ | 65-82 | 44.2 | -5.2 | -13.2 |  |
| consensus_gap | close | pin limit <$1k | 39-39 | 50.0 | 2.1 | -1.1 |  |
| consensus_gap+follow_move | close | 1-3k bets | 70-70 | 50.0 | 0.2 | -2.7 |  |
| consensus_gap+money_level | close | 1-3k bets | 107-78 | 57.8 | 1.2 | 1.6 |  |
| consensus_gap+money_moving | close | 1-3k bets | 69-126 | 35.4 | -7.7 | -12.8 |  |
| consensus_gap+pin_value | close | 1-3k bets | 64-86 | 42.7 | -1.9 | -9.2 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 69-129 | 34.8 | -7.7 | -13.9 |  |
| follow_move+money_level | close | 1-3k bets | 283-188 | 60.1 | 4.3 | -1.9 |  |
| follow_move+money_moving | close | 1-3k bets | 226-243 | 48.2 | -1.0 | -7.4 |  |
| follow_move+pin_value | close | 1-3k bets | 58-56 | 50.9 | 3.4 | -3.5 |  |
| follow_move+sharp_gap | close | 1-3k bets | 226-239 | 48.6 | -0.4 | -5.9 |  |
| money_level+money_moving | close | 1-3k bets | 271-243 | 52.7 | 0.8 | -2.3 |  |
| money_level+pin_value | close | 1-3k bets | 80-75 | 51.6 | 2.9 | -3.1 |  |
| money_level+sharp_gap | close | 1-3k bets | 269-241 | 52.7 | 1.0 | -1.6 |  |
| money_moving+pin_value | close | 1-3k bets | 72-88 | 45.0 | -1.6 | -6.5 |  |
| money_moving+sharp_gap | close | 1-3k bets | 356-439 | 44.8 | -2.5 | -9.5 |  |
| pin_value+sharp_gap | close | 1-3k bets | 74-90 | 45.1 | -1.6 | -6.5 |  |
| book_lag+money_level | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 12-20 | 37.5 | 0.7 | 30.6 |  |
| money_level+pin_rlm | close | 1-3k bets | 30-19 | 61.2 | 10.2 | 17.7 |  |
| pin_rlm+pin_value | close | 1-3k bets | 18-17 | 51.4 | 6.0 | 38.3 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 59-64 | 48.0 | 4.3 | 15.1 |  |
| money_moving+pin_rlm | close | 1-3k bets | 57-63 | 47.5 | 3.9 | 14.8 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 15-26 | 36.6 | -2.6 | 6.0 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 94-111 | 45.9 | 0.4 | -1.6 |  |
| money_level+rlm_ratio | close | 1-3k bets | 49-41 | 54.4 | 3.8 | 5.1 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 92-109 | 45.8 | 0.2 | -1.6 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 94-111 | 45.9 | 0.4 | -1.6 |  |
| follow_move+pin_rlm | close | 1-3k bets | 46-50 | 47.9 | 1.8 | -4.7 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 46-50 | 47.9 | 1.8 | -4.7 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 19-16 | 54.3 | 6.5 | 4.7 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 45.7 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 23-25 | 47.9 | -1.1 | -5.5 |  |
| consensus_gap+money_moving | close | 3k+ bets | 26-44 | 37.1 | -5.8 | 15.8 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-5 | 37.5 | -2.7 | 19.3 |  |
| consensus_gap+pin_value | close | 3k+ bets | 28-30 | 48.3 | 3.9 | 1.1 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | 0.7 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 27-44 | 38.0 | -4.8 | 19.6 |  |
| follow_move+money_moving | close | 3k+ bets | 71-78 | 47.7 | -1.2 | -6.3 |  |
| follow_move+pin_rlm | close | 3k+ bets | 19-16 | 54.3 | 10.8 | 22.0 |  |
| follow_move+pin_value | close | 3k+ bets | 23-23 | 50.0 | 1.1 | -6.2 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 33-28 | 54.1 | 10.2 | 16.3 |  |
| follow_move+sharp_gap | close | 3k+ bets | 73-77 | 48.7 | 0.4 | -3.3 |  |
| money_moving+pin_rlm | close | 3k+ bets | 19-22 | 46.3 | 5.4 | 3.9 |  |
| money_moving+pin_value | close | 3k+ bets | 26-34 | 43.3 | -2.0 | -6.8 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 31-26 | 54.4 | 10.6 | 17.5 |  |
| money_moving+sharp_gap | close | 3k+ bets | 138-147 | 48.4 | 1.6 | 5.2 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-6 | 45.5 | -0.9 | -13.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 19-16 | 54.3 | 10.8 | 22.0 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 20-22 | 47.6 | 6.4 | 6.1 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 6-5 | 54.5 | 4.4 | 2.8 |  |
| pin_value+sharp_gap | close | 3k+ bets | 26-32 | 44.8 | -0.6 | -3.5 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 33-28 | 54.1 | 10.2 | 16.3 |  |
| money_level+money_moving | close | 3k+ bets | 94-90 | 51.1 | -0.7 | -6.3 |  |
| money_level+sharp_gap | close | 3k+ bets | 93-87 | 51.7 | 0.2 | -4.2 |  |
| follow_move+money_level | close | 3k+ bets | 86-72 | 54.4 | -1.9 | -8.8 |  |
| money_level+rlm_ratio | close | 3k+ bets | 17-9 | 65.4 | 18.1 | 28.5 |  |
| consensus_gap+money_level | close | 3k+ bets | 33-35 | 48.5 | -7.2 | -17.0 |  |
| money_level+pin_value | close | 3k+ bets | 26-33 | 44.1 | -4.2 | -18.7 |  |
| money_level+pin_rlm | close | 3k+ bets | 8-6 | 57.1 | 13.1 | 17.5 |  |
| money_level+money_moving | close | <1k bets | 70-75 | 48.3 | -4.4 | -16.7 |  |
| money_level+sharp_gap | close | <1k bets | 73-75 | 49.3 | -3.9 | -16.1 |  |
| money_moving+sharp_gap | close | <1k bets | 102-124 | 45.1 | -3.0 | -13.7 |  |
| consensus_gap+money_level | close | <1k bets | 16-26 | 38.1 | -17.5 | -41.8 |  |
| consensus_gap+money_moving | close | <1k bets | 15-36 | 29.4 | -11.8 | -32.8 |  |
| consensus_gap+pin_value | close | <1k bets | 12-14 | 46.2 | 5.7 | 9.9 |  |
| consensus_gap+sharp_gap | close | <1k bets | 15-37 | 28.8 | -12.1 | -34.1 |  |
| money_level+pin_value | close | <1k bets | 17-17 | 50.0 | 0.7 | -6.7 |  |
| money_moving+pin_value | close | <1k bets | 15-16 | 48.4 | 2.9 | 10.3 |  |
| pin_value+sharp_gap | close | <1k bets | 15-15 | 50.0 | 3.9 | 13.9 |  |
| follow_move+money_moving | close | <1k bets | 49-58 | 45.8 | -4.4 | -14.4 |  |
| follow_move+sharp_gap | close | <1k bets | 51-58 | 46.8 | -4.3 | -17.0 |  |
| follow_move+rlm_ratio | close | <1k bets | 24-22 | 52.2 | 8.0 | 5.7 |  |
| money_moving+rlm_ratio | close | <1k bets | 24-22 | 52.2 | 8.0 | 5.7 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 24-22 | 52.2 | 8.0 | 5.7 |  |
| follow_move+money_level | close | <1k bets | 66-58 | 53.2 | -5.0 | -19.2 |  |
| consensus_gap+pin_rlm | close | <1k bets | 3-7 | 30.0 | -0.7 | 12.2 |  |
| money_moving+pin_rlm | close | <1k bets | 21-20 | 51.2 | 8.8 | 13.7 |  |
| pin_rlm+sharp_gap | close | <1k bets | 21-20 | 51.2 | 8.8 | 13.7 |  |
| consensus_gap+follow_move | close | <1k bets | 8-18 | 30.8 | -20.2 | -52.8 |  |
| follow_move+pin_rlm | close | <1k bets | 16-11 | 59.3 | 14.6 | 17.3 |  |
| follow_move+pin_value | close | <1k bets | 16-12 | 57.1 | 8.8 | 8.5 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 19.8 | 60.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 16-11 | 59.3 | 14.6 | 17.3 |  |
| pin_value+rlm_ratio | close | <1k bets | 3-1 | 75.0 | 22.5 | 43.9 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 1-6 | 14.3 | -18.5 | -71.1 |  |
| money_level+rlm_ratio | close | <1k bets | 12-12 | 50.0 | 3.2 | -1.3 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 15.8 | 19.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 31-41 | 43.1 | -7.0 | -14.8 |  |
| consensus_gap+money_moving | close | pin $1-2k | 42-57 | 42.4 | -4.5 | -5.4 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 11-16 | 40.7 | 0.8 | 30.3 |  |
| consensus_gap+pin_value | close | pin $1-2k | 48-62 | 43.6 | -0.7 | -10.5 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 12-12 | 50.0 | 5.3 | 11.5 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 42-54 | 43.8 | -2.5 | -2.4 |  |
| follow_move+money_moving | close | pin $1-2k | 115-142 | 44.7 | -4.7 | -12.0 |  |
| follow_move+pin_rlm | close | pin $1-2k | 36-31 | 53.7 | 6.5 | 11.9 |  |
| follow_move+pin_value | close | pin $1-2k | 44-49 | 47.3 | -1.5 | -10.9 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 54-49 | 52.4 | 5.4 | 9.3 |  |
| follow_move+sharp_gap | close | pin $1-2k | 119-139 | 46.1 | -3.6 | -10.4 |  |
| money_moving+pin_rlm | close | pin $1-2k | 42-40 | 51.2 | 6.6 | 20.2 |  |
| money_moving+pin_value | close | pin $1-2k | 49-68 | 41.9 | -5.3 | -16.7 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 53-47 | 53.0 | 5.9 | 10.5 |  |
| money_moving+sharp_gap | close | pin $1-2k | 200-217 | 48.0 | -0.6 | -3.4 |  |
| pin_rlm+pin_value | close | pin $1-2k | 10-16 | 38.5 | -9.7 | -16.2 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 36-31 | 53.7 | 6.5 | 11.9 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 44-41 | 51.8 | 7.1 | 20.4 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 13-13 | 50.0 | 0.0 | -6.0 |  |
| pin_value+sharp_gap | close | pin $1-2k | 49-66 | 42.6 | -4.6 | -15.3 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 54-49 | 52.4 | 5.4 | 9.3 |  |
| follow_move+money_level | close | pin $1-2k | 135-131 | 50.8 | -3.1 | -11.3 |  |
| money_level+rlm_ratio | close | pin $1-2k | 34-23 | 59.6 | 11.2 | 17.0 |  |
| money_level+sharp_gap | close | pin $1-2k | 155-149 | 51.0 | -0.5 | -5.1 |  |
| money_level+money_moving | close | pin $1-2k | 152-152 | 50.0 | -1.3 | -6.6 |  |
| consensus_gap+money_level | close | pin $1-2k | 46-49 | 48.4 | -6.8 | -13.9 |  |
| money_level+pin_value | close | pin $1-2k | 54-59 | 47.8 | -1.3 | -10.5 |  |
| money_level+pin_rlm | close | pin $1-2k | 23-15 | 60.5 | 12.9 | 19.8 |  |
| follow_move+money_level | close | pin $2k+ | 96-64 | 60.0 | 0.5 | -6.0 |  |
| follow_move+money_moving | close | pin $2k+ | 72-82 | 46.8 | -0.1 | -11.8 |  |
| follow_move+sharp_gap | close | pin $2k+ | 73-84 | 46.5 | -0.4 | -12.1 |  |
| money_level+money_moving | close | pin $2k+ | 96-96 | 50.0 | -2.5 | -9.2 |  |
| money_level+sharp_gap | close | pin $2k+ | 96-98 | 49.5 | -3.1 | -9.8 |  |
| money_moving+sharp_gap | close | pin $2k+ | 143-184 | 43.7 | -1.8 | -10.0 |  |
| consensus_gap+money_moving | close | pin $2k+ | 22-48 | 31.4 | -10.4 | -15.2 |  |
| consensus_gap+pin_value | close | pin $2k+ | 29-38 | 43.3 | 2.4 | 4.0 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 23-51 | 31.1 | -11.8 | -17.9 |  |
| money_moving+pin_value | close | pin $2k+ | 37-46 | 44.6 | 1.1 | 4.2 |  |
| pin_value+sharp_gap | close | pin $2k+ | 37-46 | 44.6 | 1.1 | 4.2 |  |
| consensus_gap+follow_move | close | pin $2k+ | 21-23 | 47.7 | -3.9 | -22.1 |  |
| follow_move+pin_value | close | pin $2k+ | 25-23 | 52.1 | 6.5 | -0.8 |  |
| follow_move+pin_rlm | close | pin $2k+ | 17-34 | 33.3 | -3.6 | -27.4 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 25-42 | 37.3 | -0.1 | -20.9 |  |
| money_level+pin_rlm | close | pin $2k+ | 7-8 | 46.7 | 3.9 | -8.2 |  |
| money_level+pin_value | close | pin $2k+ | 35-36 | 49.3 | 0.2 | -9.2 |  |
| money_level+rlm_ratio | close | pin $2k+ | 9-9 | 50.0 | 2.4 | -3.4 |  |
| money_moving+pin_rlm | close | pin $2k+ | 21-49 | 30.0 | -4.4 | -22.4 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 25-41 | 37.9 | 0.3 | -19.7 |  |
| pin_rlm+pin_value | close | pin $2k+ | 5-8 | 38.5 | 4.2 | 51.3 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 17-34 | 33.3 | -3.6 | -27.4 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 21-49 | 30.0 | -4.4 | -22.4 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 3-5 | 37.5 | -1.1 | -22.1 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 25-42 | 37.3 | -0.1 | -20.9 |  |
| consensus_gap+money_level | close | pin $2k+ | 45-34 | 57.0 | -5.1 | -11.8 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-14 | 22.2 | -6.7 | -3.9 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-10 | 0.0 | -28.6 | -100.0 |  |
| money_level+money_moving | close | pin limit <$1k | 54-59 | 47.8 | -2.2 | -8.1 |  |
| money_level+sharp_gap | close | pin limit <$1k | 56-58 | 49.1 | -1.1 | -5.6 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 87-87 | 50.0 | -1.0 | 1.2 |  |
| consensus_gap+money_level | close | pin limit <$1k | 21-22 | 48.8 | 0.9 | -9.8 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 27-30 | 47.4 | 0.2 | -3.2 |  |
| follow_move+money_moving | close | pin limit <$1k | 57-56 | 50.4 | -0.6 | -2.9 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 59-54 | 52.2 | 1.1 | 0.4 |  |
| money_level+pin_value | close | pin limit <$1k | 34-30 | 53.1 | 5.7 | 0.4 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 14-10 | 58.3 | 9.9 | 6.1 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 17-15 | 53.1 | 6.2 | 13.9 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 18-16 | 52.9 | 5.5 | 12.7 |  |
| follow_move+money_level | close | pin limit <$1k | 48-46 | 51.1 | 1.0 | -2.8 |  |
| follow_move+pin_value | close | pin limit <$1k | 28-19 | 59.6 | 11.1 | 12.8 |  |
| money_moving+pin_value | close | pin limit <$1k | 27-24 | 52.9 | 4.5 | 9.2 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 29-25 | 53.7 | 4.8 | 10.1 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 3-2 | 60.0 | 18.3 | 101.6 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 34-16 | 68.0 | 16.2 | 48.3 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 13-2 | 86.7 | 37.1 | 95.2 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 35-16 | 68.6 | 16.8 | 49.1 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 28-12 | 70.0 | 17.2 | 34.7 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 38-20 | 65.5 | 13.1 | 26.7 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 36-20 | 64.3 | 11.9 | 24.5 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 28-12 | 70.0 | 17.2 | 34.7 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 38-20 | 65.5 | 13.1 | 26.7 |  |
| money_level+pin_rlm | close | pin limit <$1k | 17-8 | 68.0 | 14.7 | 30.7 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 19-11 | 63.3 | 11.1 | 23.5 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 12-4 | 75.0 | 23.4 | 43.9 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 3-3 | 50.0 | 2.9 | -5.2 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 45.7 | 87.7 |  |
| pin_rlm | early | <1k bets | 1-1 | 50.0 | 24.1 | -3.7 | -2.15 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| follow_move | early | 1-3k bets | 22-20 | 52.4 | 2.4 | -1.0 | -0.0 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -49.3 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 262-238 | 52.4 | 0.5 | -8.6 | 0.28 |
| follow_move | early | pin $1-2k | 19-15 | 55.9 | 3.7 | 4.8 | -0.25 |
| follow_move | early | pin limit <$1k | 41-35 | 53.9 | 4.5 | 1.2 | -0.22 |
| rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.3 | 73.7 | -0.13 |
| rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.8 | -100.0 | -1.0 |
| rlm_ratio | early | <1k bets | 11-11 | 50.0 | 15.4 | 16.4 | 0.21 |
| rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.3 | 55.6 | -1.52 |
| rlm_ratio | early | pin limit <$1k | 6-1 | 85.7 | 40.8 | 74.9 | 0.19 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | -0.1 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 41.5 | 59.7 | 0.33 |
| money_level | early | <1k bets | 90-56 | 61.6 | 2.7 | -4.6 | 0.26 |
| money_level | early | pin $1-2k | 15-8 | 65.2 | 0.9 | -2.7 | -0.03 |
| money_level | early | pin limit <$1k | 22-24 | 47.8 | -6.2 | -12.1 | 0.31 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 6.9 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 6.2 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 78-57 | 57.8 | 8.0 | 10.8 | 0.49 |
| sharp_gap | early | pin $1-2k | 12-9 | 57.1 | 4.4 | 13.4 | -0.59 |
| sharp_gap | early | pin limit <$1k | 27-16 | 62.8 | 13.9 | 30.8 | 0.2 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.0 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.3 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 46-39 | 54.1 | 2.7 | -3.8 | 0.2 |
| money_moving | early | pin $1-2k | 6-6 | 50.0 | -11.6 | -26.9 | 0.35 |
| money_moving | early | pin limit <$1k | 20-9 | 69.0 | 19.7 | 47.8 | 0.36 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.4 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 30-33 | 47.6 | 0.1 | -9.7 | 0.19 |
| pin_value | early | pin $1-2k | 11-14 | 44.0 | -0.3 | -16.7 | 0.17 |
| pin_value | early | pin limit <$1k | 32-28 | 53.3 | 4.0 | 0.8 | 0.13 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -45.7 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -28.2 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -10.8 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 13.5 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 125-175 | 41.7 | -5.2 | -18.1 | 0.3 |
| consensus_gap | early | pin $1-2k | 10-17 | 37.0 | -8.1 | -27.6 | 0.49 |
| consensus_gap | early | pin limit <$1k | 17-33 | 34.0 | -16.0 | -29.1 | 0.31 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 15.8 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 2.3 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 2.7 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.0 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 18.7 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 15.2 | 26.0 | -0.25 |
| consensus_gap+follow_move | early | 1-3k bets | 5-6 | 45.5 | -0.2 | -23.0 | 0.39 |
| consensus_gap+pin_value | early | 1-3k bets | 5-5 | 50.0 | 4.5 | -6.9 | 0.3 |
| follow_move+pin_value | early | 1-3k bets | 7-6 | 53.8 | 6.4 | 0.8 | -0.31 |
| consensus_gap+money_level | early | 1-3k bets | 4-7 | 36.4 | -21.9 | -46.2 | 0.15 |
| consensus_gap+sharp_gap | early | 1-3k bets | 4-7 | 36.4 | -2.3 | 7.9 | 0.23 |
| follow_move+money_level | early | 1-3k bets | 15-11 | 57.7 | 2.1 | -6.6 | 0.04 |
| follow_move+sharp_gap | early | 1-3k bets | 12-9 | 57.1 | 9.1 | 24.3 | -0.04 |
| follow_move+rlm_ratio | early | 1-3k bets | 6-3 | 66.7 | 23.3 | 73.7 | -0.13 |
| money_level+rlm_ratio | early | 1-3k bets | 4-1 | 80.0 | 26.6 | 55.0 | 0.0 |
| pin_value+rlm_ratio | early | 1-3k bets | 1-1 | 50.0 | 0.0 | -4.5 | -1.5 |
| rlm_ratio+sharp_gap | early | 1-3k bets | 6-3 | 66.7 | 23.3 | 73.7 | -0.13 |
| follow_move+money_moving | early | 1-3k bets | 12-5 | 70.6 | 21.0 | 25.3 | 0.18 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 18.1 | 56.1 | 0.15 |
| money_moving+rlm_ratio | early | 1-3k bets | 3-2 | 60.0 | 19.1 | 18.8 | -0.24 |
| consensus_gap+rlm_ratio | early | 1-3k bets | 0-1 | 0.0 | -25.9 | -100.0 | 1.3 |
| consensus_gap+money_level | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| consensus_gap+money_moving | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| consensus_gap+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| follow_move+rlm_ratio | early | 3k+ bets | 0-1 | 0.0 | -52.8 | -100.0 | -1.0 |
| follow_move+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.8 | -100.0 | -1.0 |
| money_level+money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.3 | 89.2 | 0.5 |
| money_level+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| money_moving+pin_value | early | 3k+ bets | 1-0 | 100.0 | 52.8 | 83.3 | 1.0 |
| rlm_ratio+sharp_gap | early | 3k+ bets | 0-1 | 0.0 | -52.8 | -100.0 | -1.0 |
| money_level+sharp_gap | early | 3k+ bets | 2-0 | 100.0 | 35.8 | 47.9 | 0.0 |
| money_moving+sharp_gap | early | 3k+ bets | 1-0 | 100.0 | 45.7 | 95.2 | 0.0 |
| consensus_gap+follow_move | early | <1k bets | 19-27 | 41.3 | -10.2 | -26.0 | 0.92 |
| consensus_gap+money_level | early | <1k bets | 18-15 | 54.5 | -10.8 | -19.3 | 0.26 |
| consensus_gap+sharp_gap | early | <1k bets | 15-26 | 36.6 | -12.1 | -13.7 | 0.75 |
| follow_move+money_level | early | <1k bets | 49-25 | 66.2 | 7.1 | -2.4 | 0.43 |
| follow_move+sharp_gap | early | <1k bets | 40-19 | 67.8 | 17.3 | 18.8 | 0.64 |
| money_level+sharp_gap | early | <1k bets | 54-28 | 65.9 | 9.4 | 6.7 | 0.64 |
| follow_move+money_moving | early | <1k bets | 20-12 | 62.5 | 9.5 | 10.9 | 0.65 |
| money_level+money_moving | early | <1k bets | 30-22 | 57.7 | 0.7 | -7.6 | 0.1 |
| money_moving+sharp_gap | early | <1k bets | 30-21 | 58.8 | 8.1 | 5.8 | 0.52 |
| consensus_gap+money_moving | early | <1k bets | 8-15 | 34.8 | -12.6 | -44.1 | 0.14 |
| follow_move+pin_value | early | <1k bets | 11-11 | 50.0 | 2.3 | -5.9 | 0.05 |
| follow_move+rlm_ratio | early | <1k bets | 11-11 | 50.0 | 15.4 | 16.4 | 0.21 |
| rlm_ratio+sharp_gap | early | <1k bets | 11-11 | 50.0 | 15.4 | 16.4 | 0.21 |
| consensus_gap+pin_value | early | <1k bets | 11-22 | 33.3 | -12.1 | -37.3 | 0.45 |
| consensus_gap+pin_rlm | early | <1k bets | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | <1k bets | 1-3 | 25.0 | -15.1 | -52.3 | -0.07 |
| follow_move+pin_rlm | early | <1k bets | 1-1 | 50.0 | 24.1 | -3.7 | -2.15 |
| pin_rlm+pin_value | early | <1k bets | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 24.1 | -3.7 | -2.15 |
| pin_rlm+sharp_gap | early | <1k bets | 1-1 | 50.0 | 24.1 | -3.7 | -2.15 |
| pin_value+rlm_ratio | early | <1k bets | 1-1 | 50.0 | 9.9 | -4.5 | -1.9 |
| pin_value+sharp_gap | early | <1k bets | 4-3 | 57.1 | 11.6 | 9.1 | 0.03 |
| money_level+pin_value | early | <1k bets | 3-3 | 50.0 | 1.4 | -4.5 | 1.33 |
| book_lag+consensus_gap | early | <1k bets | 0-2 | 0.0 | -53.6 | -100.0 | -0.5 |
| book_lag+pin_value | early | <1k bets | 0-1 | 0.0 | -54.3 | -100.0 | 1.0 |
| money_moving+pin_value | early | <1k bets | 0-2 | 0.0 | -49.3 | -100.0 | 2.5 |
| money_level+rlm_ratio | early | <1k bets | 5-5 | 50.0 | 12.8 | 0.9 | 1.52 |
| money_moving+rlm_ratio | early | <1k bets | 3-3 | 50.0 | 6.4 | 26.0 | 0.1 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| consensus_gap+money_level | early | pin $1-2k | 4-4 | 50.0 | -14.0 | -22.9 | 0.44 |
| consensus_gap+money_moving | early | pin $1-2k | 1-2 | 33.3 | -31.8 | -38.9 | 1.27 |
| consensus_gap+pin_value | early | pin $1-2k | 4-9 | 30.8 | -8.6 | -42.5 | 0.4 |
| follow_move+rlm_ratio | early | pin $1-2k | 2-3 | 40.0 | 3.3 | 55.6 | -1.52 |
| follow_move+sharp_gap | early | pin $1-2k | 7-4 | 63.6 | 11.4 | 42.5 | -0.87 |
| money_level+money_moving | early | pin $1-2k | 6-5 | 54.5 | -10.3 | -20.3 | 0.02 |
| money_level+pin_value | early | pin $1-2k | 2-3 | 40.0 | -8.3 | -25.2 | 0.6 |
| money_moving+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -8.4 | 1.0 |
| rlm_ratio+sharp_gap | early | pin $1-2k | 2-3 | 40.0 | 3.3 | 55.6 | -1.52 |
| money_level+sharp_gap | early | pin $1-2k | 9-4 | 69.2 | 6.2 | 8.3 | -0.45 |
| money_moving+sharp_gap | early | pin $1-2k | 3-5 | 37.5 | -21.2 | -45.3 | -0.06 |
| pin_value+sharp_gap | early | pin $1-2k | 1-2 | 33.3 | -8.6 | -36.4 | -1.27 |
| consensus_gap+follow_move | early | pin $1-2k | 3-6 | 33.3 | -14.0 | -42.7 | 0.43 |
| follow_move+pin_value | early | pin $1-2k | 4-5 | 44.4 | 0.1 | -16.8 | -0.2 |
| follow_move+money_level | early | pin $1-2k | 7-4 | 63.6 | 1.2 | -0.7 | 0.07 |
| money_level+rlm_ratio | early | pin $1-2k | 1-0 | 100.0 | 47.2 | 98.0 | 0.0 |
| follow_move+money_moving | early | pin $1-2k | 2-1 | 66.7 | 1.5 | 4.7 | -0.53 |
| consensus_gap+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| consensus_gap+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| consensus_gap+sharp_gap | early | pin $1-2k | 1-3 | 25.0 | -25.0 | -62.8 | -0.72 |
| follow_move+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| pin_rlm+pin_value | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| pin_rlm+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| pin_value+rlm_ratio | early | pin $1-2k | 0-1 | 0.0 | -25.9 | -100.0 | -4.8 |
| money_level+money_moving | early | pin limit <$1k | 11-7 | 61.1 | 7.9 | 12.1 | 0.53 |
| money_level+sharp_gap | early | pin limit <$1k | 18-14 | 56.2 | 4.8 | 2.3 | 0.25 |
| money_moving+sharp_gap | early | pin limit <$1k | 16-5 | 76.2 | 27.9 | 68.0 | 0.39 |
| money_level+pin_value | early | pin limit <$1k | 8-5 | 61.5 | 9.9 | 16.6 | 0.46 |
| money_moving+pin_value | early | pin limit <$1k | 6-4 | 60.0 | 9.9 | 13.0 | 0.3 |
| pin_value+sharp_gap | early | pin limit <$1k | 11-5 | 68.8 | 18.1 | 30.3 | 0.06 |
| consensus_gap+follow_move | early | pin limit <$1k | 6-9 | 40.0 | -10.7 | -25.7 | 0.53 |
| consensus_gap+money_level | early | pin limit <$1k | 3-7 | 30.0 | -27.1 | -51.9 | 0.4 |
| consensus_gap+pin_value | early | pin limit <$1k | 13-18 | 41.9 | -6.1 | -21.4 | 0.44 |
| consensus_gap+sharp_gap | early | pin limit <$1k | 6-4 | 60.0 | 15.4 | 53.2 | 0.9 |
| follow_move+money_level | early | pin limit <$1k | 10-11 | 47.6 | -7.1 | -12.3 | -0.09 |
| follow_move+pin_value | early | pin limit <$1k | 14-12 | 53.8 | 5.1 | 1.2 | -0.04 |
| follow_move+sharp_gap | early | pin limit <$1k | 12-7 | 63.2 | 14.2 | 20.4 | -0.13 |
| follow_move+rlm_ratio | early | pin limit <$1k | 6-1 | 85.7 | 40.8 | 74.9 | 0.19 |
| money_level+rlm_ratio | early | pin limit <$1k | 5-0 | 100.0 | 51.4 | 92.1 | 0.3 |
| pin_value+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.2 | 27.3 | -0.67 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 6-1 | 85.7 | 40.8 | 74.9 | 0.19 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 23.4 | 72.3 | 0.54 |
| follow_move+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 20.4 | 33.3 | 0.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 2-1 | 66.7 | 15.2 | 28.7 | -1.0 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -54.3 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -54.3 | -100.0 | 1.0 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 74.1 | 92.6 | 0.5 |
| pin_rlm | close | 1-3k bets | 20-27 | 42.6 | 4.0 | 10.6 |  |
| pin_rlm | close | 3k+ bets | 5-6 | 45.5 | 5.5 | 8.5 |  |
| pin_rlm | close | <1k bets | 0-1 | 0.0 | -25.2 | -100.0 |  |
| pin_rlm | close | pin $1-2k | 10-15 | 40.0 | 0.8 | -9.5 |  |
| pin_rlm | close | pin $2k+ | 9-9 | 50.0 | 15.2 | 66.2 |  |
| pin_rlm | close | pin limit <$1k | 6-10 | 37.5 | -4.5 | -28.8 |  |
| follow_move | close | 1-3k bets | 114-109 | 51.1 | 0.7 | -6.2 |  |
| follow_move | close | 3k+ bets | 32-28 | 53.3 | 2.6 | -3.2 |  |
| follow_move | close | <1k bets | 11-7 | 61.1 | 9.3 | -3.2 |  |
| follow_move | close | pin $1-2k | 45-50 | 47.4 | -4.0 | -11.3 |  |
| follow_move | close | pin $2k+ | 39-23 | 62.9 | 10.8 | 16.3 |  |
| follow_move | close | pin limit <$1k | 11-22 | 33.3 | -12.7 | -36.3 |  |
| rlm_ratio | close | 1-3k bets | 28-38 | 42.4 | 0.9 | -6.6 |  |
| rlm_ratio | close | 3k+ bets | 9-7 | 56.2 | 11.4 | 21.7 |  |
| rlm_ratio | close | <1k bets | 2-4 | 33.3 | -6.8 | -36.9 |  |
| rlm_ratio | close | pin $1-2k | 9-15 | 37.5 | -5.9 | -14.0 |  |
| rlm_ratio | close | pin $2k+ | 7-4 | 63.6 | 27.0 | 71.5 |  |
| rlm_ratio | close | pin limit <$1k | 6-12 | 33.3 | -8.2 | -36.3 |  |
| money_level | close | 1-3k bets | 155-115 | 57.4 | 0.2 | -4.2 |  |
| money_level | close | 3k+ bets | 48-28 | 63.2 | 6.8 | 12.1 |  |
| money_level | close | <1k bets | 16-5 | 76.2 | 15.0 | 19.8 |  |
| money_level | close | pin $1-2k | 54-54 | 50.0 | -5.9 | -10.9 |  |
| money_level | close | pin $2k+ | 47-33 | 58.8 | 0.2 | -1.0 |  |
| money_level | close | pin limit <$1k | 23-20 | 53.5 | 2.6 | 1.3 |  |
| sharp_gap | close | 1-3k bets | 124-135 | 47.9 | -0.1 | -6.0 |  |
| sharp_gap | close | 3k+ bets | 37-36 | 50.7 | 0.8 | 0.3 |  |
| sharp_gap | close | <1k bets | 8-11 | 42.1 | -4.3 | -26.2 |  |
| sharp_gap | close | pin $1-2k | 43-60 | 41.7 | -7.3 | -18.9 |  |
| sharp_gap | close | pin $2k+ | 40-37 | 51.9 | 3.4 | 20.4 |  |
| sharp_gap | close | pin limit <$1k | 18-24 | 42.9 | -2.7 | -18.2 |  |
| money_moving | close | 1-3k bets | 128-132 | 49.2 | -0.3 | -4.9 |  |
| money_moving | close | 3k+ bets | 37-36 | 50.7 | 0.8 | 0.3 |  |
| money_moving | close | <1k bets | 8-11 | 42.1 | -4.3 | -26.2 |  |
| money_moving | close | pin $1-2k | 45-58 | 43.7 | -7.4 | -17.0 |  |
| money_moving | close | pin $2k+ | 40-37 | 51.9 | 3.4 | 19.7 |  |
| money_moving | close | pin limit <$1k | 17-25 | 40.5 | -5.6 | -22.8 |  |
| pin_value | close | 1-3k bets | 42-54 | 43.8 | -3.4 | 2.8 |  |
| pin_value | close | 3k+ bets | 10-8 | 55.6 | 0.6 | 3.6 |  |
| pin_value | close | <1k bets | 5-0 | 100.0 | 51.7 | 89.4 |  |
| pin_value | close | pin $1-2k | 25-35 | 41.7 | -6.0 | 0.8 |  |
| pin_value | close | pin $2k+ | 12-20 | 37.5 | -8.4 | -11.6 |  |
| pin_value | close | pin limit <$1k | 20-7 | 74.1 | 21.1 | 40.7 |  |
| consensus_gap | close | 1-3k bets | 43-40 | 51.8 | 1.5 | -0.3 |  |
| consensus_gap | close | 3k+ bets | 14-11 | 56.0 | 9.0 | 13.8 |  |
| consensus_gap | close | <1k bets | 3-7 | 30.0 | -11.7 | -52.5 |  |
| consensus_gap | close | pin $1-2k | 20-14 | 58.8 | 6.4 | 4.2 |  |
| consensus_gap | close | pin $2k+ | 11-13 | 45.8 | 1.8 | 35.3 |  |
| consensus_gap | close | pin limit <$1k | 8-4 | 66.7 | 11.7 | 23.5 |  |
| money_level+money_moving | close | 1-3k bets | 90-73 | 55.2 | 0.3 | -5.2 |  |
| money_level+pin_rlm | close | 1-3k bets | 5-9 | 35.7 | -8.4 | -32.1 |  |
| money_level+sharp_gap | close | 1-3k bets | 83-70 | 54.2 | 0.3 | -5.5 |  |
| money_moving+pin_rlm | close | 1-3k bets | 17-25 | 40.5 | 1.8 | 9.0 |  |
| money_moving+sharp_gap | close | 1-3k bets | 116-123 | 48.5 | -0.1 | -3.9 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 20-27 | 42.6 | 4.0 | 10.6 |  |
| money_level+pin_value | close | 1-3k bets | 18-21 | 46.2 | -4.6 | -13.7 |  |
| money_moving+pin_value | close | 1-3k bets | 20-29 | 40.8 | -7.4 | -11.5 |  |
| pin_value+sharp_gap | close | 1-3k bets | 21-31 | 40.4 | -6.7 | -12.9 |  |
| follow_move+money_level | close | 1-3k bets | 74-51 | 59.2 | 2.0 | -3.0 |  |
| follow_move+pin_value | close | 1-3k bets | 10-15 | 40.0 | -7.2 | -24.1 |  |
| consensus_gap+money_level | close | 1-3k bets | 26-13 | 66.7 | -0.0 | 2.0 |  |
| follow_move+money_moving | close | 1-3k bets | 67-65 | 50.8 | 1.3 | -4.0 |  |
| follow_move+pin_rlm | close | 1-3k bets | 13-19 | 40.6 | 2.3 | -1.6 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 28-38 | 42.4 | 0.9 | -6.6 |  |
| follow_move+sharp_gap | close | 1-3k bets | 68-66 | 50.7 | 2.2 | -2.1 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 24-36 | 40.0 | -1.9 | -10.9 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 13-19 | 40.6 | 2.3 | -1.6 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 28-38 | 42.4 | 0.9 | -6.6 |  |
| consensus_gap+money_moving | close | 1-3k bets | 24-22 | 52.2 | 3.1 | -1.6 |  |
| consensus_gap+sharp_gap | close | 1-3k bets | 22-22 | 50.0 | 2.9 | -2.1 |  |
| consensus_gap+pin_value | close | 1-3k bets | 14-13 | 51.9 | 6.7 | 18.7 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 5-6 | 45.5 | 8.8 | -13.9 |  |
| pin_rlm+pin_value | close | 1-3k bets | 10-7 | 58.8 | 15.1 | 11.7 |  |
| money_level+rlm_ratio | close | 1-3k bets | 9-14 | 39.1 | -10.4 | -24.6 |  |
| consensus_gap+follow_move | close | 1-3k bets | 14-7 | 66.7 | 11.2 | 6.3 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 4-4 | 50.0 | 12.4 | -5.9 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 6-5 | 54.5 | 11.9 | 3.9 |  |
| consensus_gap+money_level | close | 3k+ bets | 8-4 | 66.7 | 8.2 | 18.5 |  |
| consensus_gap+money_moving | close | 3k+ bets | 5-5 | 50.0 | 3.3 | 18.5 |  |
| consensus_gap+pin_value | close | 3k+ bets | 3-0 | 100.0 | 41.8 | 88.4 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 5-5 | 50.0 | 3.3 | 18.5 |  |
| money_level+money_moving | close | 3k+ bets | 30-19 | 61.2 | 6.8 | 17.1 |  |
| money_level+pin_value | close | 3k+ bets | 8-6 | 57.1 | 0.8 | 5.9 |  |
| money_level+sharp_gap | close | 3k+ bets | 30-19 | 61.2 | 6.8 | 17.1 |  |
| money_moving+pin_value | close | 3k+ bets | 4-3 | 57.1 | 0.3 | 3.7 |  |
| money_moving+sharp_gap | close | 3k+ bets | 37-36 | 50.7 | 0.8 | 0.3 |  |
| pin_value+sharp_gap | close | 3k+ bets | 4-3 | 57.1 | 0.3 | 3.7 |  |
| follow_move+money_level | close | 3k+ bets | 21-11 | 65.6 | 7.8 | 14.5 |  |
| follow_move+money_moving | close | 3k+ bets | 18-16 | 52.9 | 1.8 | 3.8 |  |
| follow_move+sharp_gap | close | 3k+ bets | 18-16 | 52.9 | 1.8 | 3.8 |  |
| consensus_gap+follow_move | close | 3k+ bets | 5-2 | 71.4 | 21.6 | 36.1 |  |
| follow_move+pin_rlm | close | 3k+ bets | 5-4 | 55.6 | 14.9 | 32.6 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 9-7 | 56.2 | 11.4 | 21.7 |  |
| money_level+pin_rlm | close | 3k+ bets | 3-1 | 75.0 | 39.8 | 102.9 |  |
| money_level+rlm_ratio | close | 3k+ bets | 5-1 | 83.3 | 43.2 | 99.2 |  |
| money_moving+pin_rlm | close | 3k+ bets | 5-6 | 45.5 | 5.5 | 8.5 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 9-7 | 56.2 | 11.4 | 21.7 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 5-4 | 55.6 | 14.9 | 32.6 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 5-6 | 45.5 | 5.5 | 8.5 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 9-7 | 56.2 | 11.4 | 21.7 |  |
| follow_move+pin_value | close | 3k+ bets | 1-3 | 25.0 | -28.3 | -54.2 |  |
| pin_rlm+pin_value | close | 3k+ bets | 0-1 | 0.0 | -48.5 | -100.0 |  |
| money_level+money_moving | close | <1k bets | 6-2 | 75.0 | 16.8 | 27.1 |  |
| money_level+sharp_gap | close | <1k bets | 6-2 | 75.0 | 16.8 | 27.1 |  |
| money_moving+sharp_gap | close | <1k bets | 8-11 | 42.1 | -4.3 | -26.2 |  |
| follow_move+money_moving | close | <1k bets | 5-5 | 50.0 | 3.0 | -7.3 |  |
| follow_move+rlm_ratio | close | <1k bets | 2-4 | 33.3 | -6.8 | -36.9 |  |
| follow_move+sharp_gap | close | <1k bets | 5-5 | 50.0 | 3.0 | -7.3 |  |
| money_moving+rlm_ratio | close | <1k bets | 2-4 | 33.3 | -6.8 | -36.9 |  |
| rlm_ratio+sharp_gap | close | <1k bets | 2-4 | 33.3 | -6.8 | -36.9 |  |
| consensus_gap+money_moving | close | <1k bets | 2-4 | 33.3 | -8.9 | -52.6 |  |
| consensus_gap+sharp_gap | close | <1k bets | 2-4 | 33.3 | -8.9 | -52.6 |  |
| follow_move+money_level | close | <1k bets | 9-1 | 90.0 | 27.2 | 35.6 |  |
| consensus_gap+pin_value | close | <1k bets | 2-0 | 100.0 | 48.5 | 87.1 |  |
| money_level+rlm_ratio | close | <1k bets | 1-1 | 50.0 | 0.0 | -8.4 |  |
| follow_move+pin_value | close | <1k bets | 2-0 | 100.0 | 55.0 | 87.1 |  |
| consensus_gap+follow_move | close | <1k bets | 1-2 | 33.3 | -9.4 | -38.9 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 1-1 | 50.0 | 11.6 | -8.4 |  |
| money_moving+pin_rlm | close | <1k bets | 0-1 | 0.0 | -25.2 | -100.0 |  |
| pin_rlm+sharp_gap | close | <1k bets | 0-1 | 0.0 | -25.2 | -100.0 |  |
| consensus_gap+money_level | close | <1k bets | 2-1 | 66.7 | 4.0 | -5.1 |  |
| money_level+pin_value | close | <1k bets | 1-0 | 100.0 | 48.5 | 83.3 |  |
| money_moving+pin_value | close | <1k bets | 2-0 | 100.0 | 43.5 | 87.1 |  |
| pin_value+rlm_ratio | close | <1k bets | 1-0 | 100.0 | 48.5 | 83.3 |  |
| pin_value+sharp_gap | close | <1k bets | 2-0 | 100.0 | 43.5 | 87.1 |  |
| money_level+money_moving | close | pin $1-2k | 30-37 | 44.8 | -10.2 | -19.4 |  |
| money_level+pin_value | close | pin $1-2k | 10-16 | 38.5 | -14.2 | -29.1 |  |
| money_level+sharp_gap | close | pin $1-2k | 27-36 | 42.9 | -10.9 | -21.1 |  |
| money_moving+pin_value | close | pin $1-2k | 11-22 | 33.3 | -15.4 | -38.3 |  |
| money_moving+sharp_gap | close | pin $1-2k | 41-56 | 42.3 | -7.7 | -17.4 |  |
| pin_value+sharp_gap | close | pin $1-2k | 11-22 | 33.3 | -15.0 | -38.3 |  |
| follow_move+money_level | close | pin $1-2k | 32-32 | 50.0 | -6.1 | -12.5 |  |
| follow_move+money_moving | close | pin $1-2k | 26-32 | 44.8 | -7.0 | -12.1 |  |
| follow_move+sharp_gap | close | pin $1-2k | 25-33 | 43.1 | -7.1 | -12.9 |  |
| consensus_gap+money_level | close | pin $1-2k | 12-6 | 66.7 | 3.9 | 12.6 |  |
| consensus_gap+money_moving | close | pin $1-2k | 10-7 | 58.8 | 4.7 | 3.0 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 8-8 | 50.0 | 0.2 | -7.5 |  |
| consensus_gap+pin_value | close | pin $1-2k | 10-8 | 55.6 | 8.0 | 3.7 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 2-2 | 50.0 | 9.1 | -4.5 |  |
| money_moving+pin_rlm | close | pin $1-2k | 9-14 | 39.1 | -1.3 | -12.0 |  |
| pin_rlm+pin_value | close | pin $1-2k | 4-5 | 44.4 | 2.3 | -15.6 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 10-15 | 40.0 | 0.8 | -9.5 |  |
| follow_move+pin_rlm | close | pin $1-2k | 8-10 | 44.4 | 3.8 | 4.5 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 9-15 | 37.5 | -5.9 | -14.0 |  |
| money_level+pin_rlm | close | pin $1-2k | 3-6 | 33.3 | -8.4 | -36.4 |  |
| money_level+rlm_ratio | close | pin $1-2k | 4-8 | 33.3 | -15.6 | -37.0 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 8-14 | 36.4 | -8.7 | -17.1 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 8-10 | 44.4 | 3.8 | 4.5 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 9-15 | 37.5 | -5.9 | -14.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 7-4 | 63.6 | 4.2 | 4.8 |  |
| follow_move+pin_value | close | pin $1-2k | 5-11 | 31.2 | -16.9 | -41.5 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 3-4 | 42.9 | -0.8 | -19.8 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 2-2 | 50.0 | 5.8 | -6.5 |  |
| money_level+money_moving | close | pin $2k+ | 28-20 | 58.3 | 3.2 | 5.2 |  |
| money_level+pin_rlm | close | pin $2k+ | 3-1 | 75.0 | 33.3 | 102.9 |  |
| money_level+sharp_gap | close | pin $2k+ | 28-20 | 58.3 | 3.2 | 6.3 |  |
| money_moving+pin_rlm | close | pin $2k+ | 9-9 | 50.0 | 15.2 | 66.2 |  |
| money_moving+sharp_gap | close | pin $2k+ | 39-36 | 52.0 | 3.5 | 21.4 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 9-9 | 50.0 | 15.2 | 66.2 |  |
| consensus_gap+money_level | close | pin $2k+ | 7-4 | 63.6 | -2.7 | 1.8 |  |
| consensus_gap+money_moving | close | pin $2k+ | 6-7 | 46.2 | 3.4 | 43.1 |  |
| consensus_gap+pin_value | close | pin $2k+ | 3-4 | 42.9 | 6.4 | 63.8 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 6-7 | 46.2 | 3.4 | 43.1 |  |
| money_level+pin_value | close | pin $2k+ | 10-9 | 52.6 | 1.7 | -2.3 |  |
| money_moving+pin_value | close | pin $2k+ | 9-9 | 50.0 | 1.2 | 25.7 |  |
| pin_value+sharp_gap | close | pin $2k+ | 9-10 | 47.4 | -0.2 | 19.1 |  |
| follow_move+money_level | close | pin $2k+ | 26-11 | 70.3 | 10.8 | 17.9 |  |
| follow_move+money_moving | close | pin $2k+ | 20-10 | 66.7 | 17.0 | 33.3 |  |
| follow_move+sharp_gap | close | pin $2k+ | 20-10 | 66.7 | 17.0 | 35.0 |  |
| follow_move+pin_value | close | pin $2k+ | 3-3 | 50.0 | 0.5 | -5.8 |  |
| follow_move+pin_rlm | close | pin $2k+ | 6-4 | 60.0 | 24.9 | 69.6 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 7-4 | 63.6 | 27.0 | 71.5 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 7-4 | 63.6 | 27.0 | 71.5 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 6-4 | 60.0 | 24.9 | 69.6 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 7-4 | 63.6 | 27.0 | 71.5 |  |
| money_level+rlm_ratio | close | pin $2k+ | 2-1 | 66.7 | 28.3 | 107.0 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 0-4 | 0.0 | -25.2 | -100.0 |  |
| pin_rlm+pin_value | close | pin $2k+ | 0-2 | 0.0 | -36.8 | -100.0 |  |
| consensus_gap+follow_move | close | pin $2k+ | 2-1 | 66.7 | 24.9 | 26.8 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-1 | 0.0 | -25.2 | -100.0 |  |
| money_level+money_moving | close | pin limit <$1k | 12-14 | 46.2 | -1.2 | -11.9 |  |
| money_level+sharp_gap | close | pin limit <$1k | 10-11 | 47.6 | 1.5 | -9.1 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 15-22 | 40.5 | -4.7 | -22.7 |  |
| follow_move+money_level | close | pin limit <$1k | 4-8 | 33.3 | -10.9 | -36.4 |  |
| follow_move+money_moving | close | pin limit <$1k | 6-16 | 27.3 | -15.2 | -47.9 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 6-12 | 33.3 | -8.2 | -36.3 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 9-17 | 34.6 | -9.0 | -33.9 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 2-3 | 40.0 | -3.1 | -23.6 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 4-11 | 26.7 | -14.0 | -49.1 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 6-12 | 33.3 | -8.2 | -36.3 |  |
| money_level+pin_rlm | close | pin limit <$1k | 2-3 | 40.0 | -3.1 | -24.4 |  |
| money_level+pin_value | close | pin limit <$1k | 7-2 | 77.8 | 23.9 | 48.0 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 4-9 | 30.8 | -10.2 | -41.9 |  |
| money_moving+pin_value | close | pin limit <$1k | 6-1 | 85.7 | 30.8 | 62.5 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 6-1 | 85.7 | 37.4 | 62.7 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 6-10 | 37.5 | -4.5 | -28.8 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 7-2 | 77.8 | 26.5 | 47.7 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 4-9 | 30.8 | -8.4 | -41.2 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 4-9 | 30.8 | -8.4 | -41.2 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 2-0 | 100.0 | 61.5 | 89.3 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 3-2 | 60.0 | 12.3 | 14.6 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 3-0 | 100.0 | 53.8 | 88.5 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 6-1 | 85.7 | 30.8 | 61.5 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 2-0 | 100.0 | 61.5 | 89.3 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 4-2 | 66.7 | 20.5 | 26.8 |  |
| follow_move+pin_value | close | pin limit <$1k | 5-4 | 55.6 | 9.4 | 6.2 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 4-1 | 80.0 | 36.9 | 52.9 |  |
| consensus_gap+money_level | close | pin limit <$1k | 4-3 | 57.1 | 0.3 | 4.2 |  |
| pin_rlm | early | <1k bets | 0-1 | 0.0 | -25.2 | -100.0 | 1.3 |
| pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.2 | -100.0 | 1.3 |
| follow_move | early | <1k bets | 115-77 | 59.9 | 7.4 | 2.0 | 0.14 |
| follow_move | early | pin $1-2k | 8-1 | 88.9 | 24.8 | 38.7 | -0.7 |
| follow_move | early | pin limit <$1k | 6-4 | 60.0 | 6.4 | 7.2 | 0.7 |
| rlm_ratio | early | <1k bets | 8-1 | 88.9 | 53.7 | 93.2 | 1.33 |
| rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 38.5 | 95.2 | 1.0 |
| money_level | early | <1k bets | 43-24 | 64.2 | -0.0 | 1.4 | -0.93 |
| money_level | early | pin $1-2k | 5-0 | 100.0 | 25.2 | 35.3 | 0.22 |
| money_level | early | pin limit <$1k | 2-2 | 50.0 | -5.8 | -3.5 | -0.75 |
| sharp_gap | early | <1k bets | 30-34 | 46.9 | 0.2 | -11.6 | -0.14 |
| sharp_gap | early | pin $1-2k | 3-2 | 60.0 | 5.0 | -21.8 | 0.46 |
| sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | -5.8 | -3.5 | -0.75 |
| money_moving | early | <1k bets | 29-21 | 58.0 | 5.2 | -3.2 | -0.24 |
| money_moving | early | pin $1-2k | 2-2 | 50.0 | 0.0 | -44.9 | -0.2 |
| money_moving | early | pin limit <$1k | 3-0 | 100.0 | 53.8 | 92.3 | 1.0 |
| pin_value | early | <1k bets | 6-6 | 50.0 | -0.8 | -6.3 | -0.21 |
| pin_value | early | pin $1-2k | 2-4 | 33.3 | -16.7 | -39.9 | -0.08 |
| pin_value | early | pin limit <$1k | 4-2 | 66.7 | 15.0 | 27.3 | -0.33 |
| consensus_gap | early | <1k bets | 47-53 | 47.0 | -0.8 | -1.1 | 0.51 |
| consensus_gap | early | pin $1-2k | 2-3 | 40.0 | -5.0 | -31.6 | 0.6 |
| consensus_gap | early | pin limit <$1k | 1-1 | 50.0 | 13.2 | -4.5 | -0.4 |
| money_level+money_moving | early | <1k bets | 18-8 | 69.2 | 4.1 | 7.5 | -0.91 |
| money_level+sharp_gap | early | <1k bets | 22-16 | 57.9 | -1.0 | -4.6 | -0.94 |
| money_moving+sharp_gap | early | <1k bets | 14-15 | 48.3 | 1.2 | -11.7 | -0.55 |
| consensus_gap+money_moving | early | <1k bets | 2-3 | 40.0 | -10.3 | -34.5 | 0.44 |
| consensus_gap+sharp_gap | early | <1k bets | 5-11 | 31.2 | -5.7 | -39.3 | 1.82 |
| follow_move+money_level | early | <1k bets | 22-5 | 81.5 | 11.5 | 17.8 | -0.81 |
| follow_move+money_moving | early | <1k bets | 18-8 | 69.2 | 14.4 | 13.9 | 0.19 |
| follow_move+rlm_ratio | early | <1k bets | 8-1 | 88.9 | 53.7 | 93.2 | 1.33 |
| follow_move+sharp_gap | early | <1k bets | 16-7 | 69.6 | 19.1 | 23.6 | 0.07 |
| money_moving+rlm_ratio | early | <1k bets | 5-1 | 83.3 | 47.6 | 86.8 | 0.58 |
| rlm_ratio+sharp_gap | early | <1k bets | 8-1 | 88.9 | 53.7 | 93.2 | 1.33 |
| consensus_gap+follow_move | early | <1k bets | 5-3 | 62.5 | 10.8 | 22.1 | 1.09 |
| consensus_gap+pin_value | early | <1k bets | 2-1 | 66.7 | 17.2 | 20.8 | -0.17 |
| money_level+pin_value | early | <1k bets | 1-1 | 50.0 | 0.0 | -4.5 | -0.5 |
| pin_value+sharp_gap | early | <1k bets | 1-1 | 50.0 | 0.0 | -4.5 | -0.5 |
| consensus_gap+money_level | early | <1k bets | 8-4 | 66.7 | -0.9 | 17.3 | 0.45 |
| money_moving+pin_value | early | <1k bets | 1-0 | 100.0 | 61.5 | 90.9 | -1.0 |
| money_level+rlm_ratio | early | <1k bets | 2-0 | 100.0 | 56.6 | 129.6 | 2.4 |
| money_moving+pin_rlm | early | <1k bets | 0-1 | 0.0 | -25.2 | -100.0 | 1.3 |
| pin_rlm+sharp_gap | early | <1k bets | 0-1 | 0.0 | -25.2 | -100.0 | 1.3 |
| follow_move+pin_value | early | <1k bets | 2-0 | 100.0 | 36.8 | 80.3 | -0.75 |
| consensus_gap+rlm_ratio | early | <1k bets | 2-0 | 100.0 | 68.2 | 113.6 | 2.75 |
| consensus_gap+money_level | early | pin $1-2k | 1-0 | 100.0 | 25.2 | 70.4 | 2.9 |
| consensus_gap+sharp_gap | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -14.8 | 1.1 |
| money_level+sharp_gap | early | pin $1-2k | 3-0 | 100.0 | 25.2 | 30.4 | 0.57 |
| follow_move+money_level | early | pin $1-2k | 4-0 | 100.0 | 25.2 | 26.5 | -0.45 |
| follow_move+money_moving | early | pin $1-2k | 2-0 | 100.0 | 25.2 | 10.2 | 0.35 |
| money_level+money_moving | early | pin $1-2k | 2-0 | 100.0 | 25.2 | 10.2 | 0.35 |
| follow_move+sharp_gap | early | pin $1-2k | 2-0 | 100.0 | 25.2 | 10.4 | -0.6 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.2 | -100.0 | 1.3 |
| money_moving+sharp_gap | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -45.9 | 0.65 |
| pin_rlm+sharp_gap | early | pin $1-2k | 0-1 | 0.0 | -25.2 | -100.0 | 1.3 |
| follow_move+pin_value | early | pin $1-2k | 2-0 | 100.0 | 36.8 | 80.3 | -0.75 |
| consensus_gap+follow_move | early | pin $1-2k | 1-0 | 100.0 | 25.2 | 71.4 | -0.5 |
| consensus_gap+pin_value | early | pin $1-2k | 1-1 | 50.0 | 0.0 | -14.3 | -0.25 |
| consensus_gap+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 51.5 | 90.9 | 0.0 |
| money_level+pin_value | early | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 | -0.5 |
| money_level+sharp_gap | early | pin limit <$1k | 2-2 | 50.0 | -5.8 | -3.5 | -0.75 |
| pin_value+sharp_gap | early | pin limit <$1k | 1-1 | 50.0 | 0.0 | -4.5 | -0.5 |
| money_level+money_moving | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 93.0 | 0.0 |
| money_moving+pin_value | early | pin limit <$1k | 1-0 | 100.0 | 61.5 | 90.9 | -1.0 |
| money_moving+sharp_gap | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 93.0 | 0.0 |
| follow_move+money_level | early | pin limit <$1k | 1-0 | 100.0 | 38.5 | 95.2 | 1.0 |
| follow_move+money_moving | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 93.0 | 2.0 |
| follow_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 38.5 | 95.2 | 1.0 |
| follow_move+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 38.5 | 95.2 | 1.0 |
| money_level+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 38.5 | 95.2 | 1.0 |
| money_moving+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 38.5 | 95.2 | 1.0 |
| rlm_ratio+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 38.5 | 95.2 | 1.0 |
