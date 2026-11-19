# CBB scorecard

Generated 2026-11-19 20:59 UTC. 642 graded games (18 finished games had no final score matched and are not graded).

## Read this first: fit vs forward

**642 games before 2026-11-20 (fit) · 0 on or after it (forward).**

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
sample ran **48.0% favourites** (n=641) and **48.9% overs** (n=642) and **74.3% moneyline favourites** (n=544).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

# FORWARD (out-of-sample — this is the evidence)

Games tipping on or after 2026-11-20. Nothing in the engine was chosen using these. n=0 games.

*No games yet. The forward test starts with the next tip.*

# FIT (in-sample — this is the hypothesis)

Games before 2026-11-20. The engine was built by looking at these, so a strong record here is expected and proves nothing. n=642 games.

## EARLY  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_move | both | 5-9 | 35.7 | 48.1 | -12.4 | -5.1 | -36.4 | 0.22 | 50.0 | keep collecting (14/30) |
| money_delta | both | 10-5 | 66.7 | 42.2 | 24.5 | +6.43 | 42.9 | -0.38 | 26.7 | keep collecting (15/30) |
| pin_rlm | both | 1-2 | 33.3 | 25.7 | 7.6 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | both | 456-392 | 53.8 | 52.6 | 1.2 | -49.13 | -5.8 | 0.22 | 42.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | both | 25-16 | 61.0 | 37.4 | 23.6 | +17.63 | 43.0 | 0.35 | 51.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | both | 162-100 | 61.8 | 59.3 | 2.5 | -7.12 | -2.7 | -0.08 | 39.3 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 135-113 | 54.4 | 48.3 | 6.2 | +16.54 | 6.7 | 0.23 | 42.7 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | both | 99-71 | 58.2 | 51.6 | 6.6 | +7.79 | 4.6 | 0.07 | 42.9 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| pin_value | both | 49-48 | 50.5 | 48.3 | 2.3 | -4.43 | -4.6 | 0.1 | 38.1 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 51.2 | -31.2 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 214-282 | 43.1 | 46.8 | -3.7 | -57.53 | -11.6 | 0.39 | 45.4 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | both | 31-26 | 54.4 | 64.1 | -9.7 | -8.54 | -15.0 | 0.29 | 47.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | both | 17-22 | 43.6 | 46.6 | -3.0 | -5.42 | -13.9 | 0.21 | 41.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_value | both | 19-28 | 40.4 | 46.4 | -5.9 | -11.54 | -24.5 | 0.39 | 48.9 | HYPOTHESIS (in-sample) -- DROP: below break-even |
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
| money_delta+sharp_gap | both | 7-4 | 63.6 | 39.2 | 24.4 | +4.78 | 43.5 | -0.52 | 36.4 | keep collecting (11/30) |
| pin_value+sharp_gap | both | 13-8 | 61.9 | 48.9 | 13.0 | +3.66 | 17.4 | -0.18 | 33.3 | keep collecting (21/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 30-38 | 44.1 | 51.4 | -7.3 | -13.76 | -20.2 | 0.8 | 57.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | both | 20-17 | 54.1 | 48.8 | 5.3 | +0.41 | 1.1 | -0.12 | 29.7 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+sharp_gap | both | 24-44 | 35.3 | 44.5 | -9.2 | -11.04 | -16.2 | 0.92 | 50.0 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | both | 86-41 | 67.7 | 60.4 | 7.3 | +1.27 | 1.0 | 0.09 | 44.1 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 11-6 | 64.7 | 40.7 | 24.0 | +5.43 | 31.9 | 1.18 | 58.8 | keep collecting (17/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 44.2 | 5.8 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 50-25 | 66.7 | 53.4 | 13.3 | +11.4 | 15.2 | 0.39 | 53.3 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 3-0 | 100.0 | 48.6 | 51.4 | +2.61 | 87.1 | 0.0 | 0.0 | keep collecting (3/30) |
| follow_move+money_delta | both | 5-2 | 71.4 | 39.5 | 32.0 | +4.95 | 70.7 | -0.23 | 28.6 | keep collecting (7/30) |
| money_moving+rlm_ratio | both | 11-6 | 64.7 | 40.3 | 24.4 | +7.71 | 45.4 | 0.17 | 47.1 | keep collecting (17/30) |
| consensus_gap+rlm_ratio | both | 3-4 | 42.9 | 36.6 | 6.3 | -0.82 | -11.7 | 0.93 | 71.4 | keep collecting (7/30) |
| pin_move+pin_value | both | 1-4 | 20.0 | 49.0 | -29.0 | -3.09 | -61.8 | 0.2 | 20.0 | keep collecting (5/30) |
| follow_move+pin_move | both | 5-3 | 62.5 | 52.6 | 9.9 | +0.9 | 11.2 | 0.42 | 62.5 | keep collecting (8/30) |
| consensus_gap+pin_move | both | 0-5 | 0.0 | 44.4 | -44.4 | -5.0 | -100.0 | 0.26 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | both | 2-2 | 50.0 | 55.8 | -5.8 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 25.7 | 24.3 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 25.7 | 24.3 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | both | 1-2 | 33.3 | 25.7 | 7.6 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.5 | -51.5 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-1 | 66.7 | 49.6 | 17.0 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 25.7 | 74.3 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 25.7 | 74.3 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 25.7 | 74.3 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 2-0 | 100.0 | 25.7 | 74.3 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| pin_move | moneyline | 2-3 | 40.0 | 45.1 | -5.1 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-4 | 20.0 | 49.6 | -29.6 | -3.09 | -61.8 | 0.4 | 40.0 | keep collecting (5/30) |
| pin_move | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.14 | -3.5 | 0.25 | 50.0 | keep collecting (4/30) |
| money_delta | moneyline | 2-3 | 40.0 | 25.7 | 14.3 | +1.34 | 26.8 | -1.74 | 40.0 | keep collecting (5/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 7-1 | 87.5 | 50.5 | 37.0 | +5.26 | 65.8 | 0.25 | 12.5 | keep collecting (8/30) |
| pin_rlm | moneyline | 1-2 | 33.3 | 25.7 | 7.6 | -1.07 | -35.8 | -1.0 | 66.7 | keep collecting (3/30) |
| follow_move | moneyline | 186-123 | 60.2 | 57.3 | 2.9 | -27.55 | -8.9 | 0.24 | 46.9 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 127-135 | 48.5 | 49.7 | -1.3 | -18.11 | -6.9 | 0.03 | 34.4 | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | total | 143-134 | 51.6 | 49.9 | 1.7 | -3.46 | -1.2 | 0.37 | 45.1 | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | moneyline | 12-10 | 54.5 | 25.7 | 28.8 | +11.57 | 52.6 | 0.39 | 59.1 | keep collecting (22/30) |
| rlm_ratio | spread | 3-2 | 60.0 | 51.2 | 8.8 | +0.84 | 16.8 | -0.6 | 0.0 | keep collecting (5/30) |
| rlm_ratio | total | 10-4 | 71.4 | 50.8 | 20.6 | +5.22 | 37.3 | 0.64 | 57.1 | keep collecting (14/30) |
| money_level | moneyline | 93-36 | 72.1 | 69.4 | 2.7 | -5.69 | -4.4 | -0.16 | 45.7 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 17-16 | 51.5 | 49.3 | 2.2 | -0.69 | -2.1 | 0.85 | 48.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | total | 52-48 | 52.0 | 49.6 | 2.4 | -0.74 | -0.7 | -0.29 | 28.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 57-59 | 49.1 | 46.2 | 2.9 | -0.32 | -0.3 | 0.26 | 49.1 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | spread | 20-14 | 58.8 | 49.8 | 9.1 | +4.0 | 11.8 | 0.65 | 38.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 58-40 | 59.2 | 50.2 | 9.0 | +12.86 | 13.1 | 0.05 | 36.7 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | moneyline | 42-38 | 52.5 | 53.6 | -1.1 | -10.85 | -13.6 | -0.14 | 48.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | spread | 18-4 | 81.8 | 49.3 | 32.5 | +12.18 | 55.3 | 0.23 | 40.9 | keep collecting (22/30) |
| money_moving | total | 39-29 | 57.4 | 50.0 | 7.4 | +6.46 | 9.5 | 0.25 | 36.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | moneyline | 2-6 | 25.0 | 31.8 | -6.8 | -4.31 | -53.8 | -0.08 | 50.0 | keep collecting (8/30) |
| pin_value | spread | 24-20 | 54.5 | 49.6 | 5.0 | +1.16 | 2.6 | 0.25 | 38.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 23-22 | 51.1 | 49.9 | 1.2 | -1.28 | -2.9 | -0.02 | 35.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 52.0 | -18.6 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 87-161 | 35.1 | 44.1 | -9.0 | -49.06 | -19.8 | 0.13 | 42.3 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 63-57 | 52.5 | 49.3 | 3.2 | -1.92 | -1.6 | 0.35 | 40.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap | total | 64-64 | 50.0 | 49.8 | 0.2 | -6.56 | -5.1 | 0.93 | 55.5 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | moneyline | 44-18 | 71.0 | 64.1 | 6.9 | -1.02 | -1.6 | 0.07 | 54.8 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+follow_move | moneyline | 10-21 | 32.3 | 53.9 | -21.7 | -14.52 | -46.9 | 0.26 | 58.1 | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 2-6 | 25.0 | 31.8 | -6.8 | -4.31 | -53.8 | -0.08 | 50.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| follow_move+pin_value | moneyline | 1-2 | 33.3 | 41.9 | -8.6 | -1.29 | -42.9 | -1.43 | 33.3 | keep collecting (3/30) |
| money_level+money_moving | moneyline | 29-12 | 70.7 | 70.7 | 0.0 | -4.0 | -9.8 | -0.54 | 53.7 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+sharp_gap | moneyline | 14-35 | 28.6 | 42.6 | -14.0 | -10.86 | -22.2 | 0.93 | 51.0 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | moneyline | 55-15 | 78.6 | 69.4 | 9.2 | -0.93 | -1.3 | -0.1 | 48.6 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 26-11 | 70.3 | 57.2 | 13.1 | +3.47 | 9.4 | 0.3 | 59.5 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_level | moneyline | 22-18 | 55.0 | 70.6 | -15.6 | -8.38 | -21.0 | 0.07 | 47.5 | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+sharp_gap | moneyline | 33-17 | 66.0 | 50.0 | 16.0 | +7.74 | 15.5 | 0.27 | 56.0 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_moving+sharp_gap | moneyline | 21-24 | 46.7 | 47.3 | -0.6 | -5.63 | -12.5 | -0.05 | 53.3 | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | moneyline | 8-21 | 27.6 | 45.8 | -18.2 | -12.26 | -42.3 | 0.24 | 48.3 | keep collecting (29/30) |
| follow_move+rlm_ratio | moneyline | 12-10 | 54.5 | 25.7 | 28.8 | +11.57 | 52.6 | 0.39 | 59.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 12-10 | 54.5 | 25.7 | 28.8 | +11.57 | 52.6 | 0.39 | 59.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-3 | 25.0 | 25.7 | -0.7 | -1.68 | -42.0 | 1.12 | 75.0 | keep collecting (4/30) |
| money_moving+rlm_ratio | moneyline | 4-3 | 57.1 | 25.7 | 31.4 | +4.22 | 60.3 | 0.27 | 57.1 | keep collecting (7/30) |
| money_delta+money_moving | moneyline | 2-3 | 40.0 | 25.7 | 14.3 | +1.34 | 26.8 | -1.74 | 40.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-3 | 40.0 | 25.7 | 14.3 | +1.34 | 26.8 | -1.74 | 40.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 41.9 | -41.9 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-1 | 66.7 | 58.1 | 8.6 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | moneyline | 2-1 | 66.7 | 58.1 | 8.6 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-1 | 50.0 | 25.7 | 24.3 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-1 | 50.0 | 25.7 | 24.3 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | moneyline | 1-2 | 33.3 | 25.7 | 7.6 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.13 | 56.5 | -0.1 | 50.0 | keep collecting (2/30) |
| money_level+rlm_ratio | moneyline | 4-3 | 57.1 | 25.7 | 31.4 | +1.87 | 26.7 | 2.0 | 85.7 | keep collecting (7/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 25.7 | 74.3 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 1-0 | 100.0 | 25.7 | 74.3 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 1-0 | 100.0 | 25.7 | 74.3 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 25.7 | 40.9 | +3.34 | 111.3 | -1.53 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 25.7 | 74.3 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-0 | 100.0 | 25.7 | 74.3 | +1.64 | 164.0 | 3.8 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-5 | 50.0 | 48.0 | 2.0 | -0.68 | -6.8 | 1.7 | 70.0 | keep collecting (10/30) |
| consensus_gap+money_moving | spread | 5-0 | 100.0 | 48.0 | 52.0 | +4.32 | 86.3 | 0.6 | 40.0 | keep collecting (5/30) |
| consensus_gap+pin_value | spread | 10-8 | 55.6 | 48.9 | 6.6 | +0.6 | 3.3 | 0.5 | 50.0 | keep collecting (18/30) |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.2 | 8.8 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 49.0 | 13.5 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 10-4 | 71.4 | 48.9 | 22.5 | +5.12 | 36.6 | 0.86 | 64.3 | keep collecting (14/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 49.2 | -6.3 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 51.2 | 8.8 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 52.0 | -52.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 52.0 | -52.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-11 | 56.0 | 49.3 | 6.7 | +1.62 | 6.5 | 1.0 | 44.0 | keep collecting (25/30) |
| money_moving+sharp_gap | spread | 10-3 | 76.9 | 49.2 | 27.7 | +6.04 | 46.4 | 0.54 | 46.2 | keep collecting (13/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.3 | 17.3 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-9 | 50.0 | 48.7 | 1.3 | -1.2 | -6.7 | 0.89 | 44.4 | keep collecting (18/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 48.0 | 14.5 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 11-8 | 57.9 | 48.9 | 9.0 | +2.04 | 10.7 | 0.63 | 42.1 | keep collecting (19/30) |
| follow_move+pin_value | spread | 12-7 | 63.2 | 49.1 | 14.1 | +3.45 | 18.2 | 0.26 | 31.6 | keep collecting (19/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 48.0 | 52.0 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 48.0 | 52.0 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-1 | 90.0 | 48.4 | 41.6 | +7.22 | 72.2 | 0.2 | 40.0 | keep collecting (10/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 52.0 | 14.7 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | spread | 1-3 | 25.0 | 49.0 | -24.0 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 48.0 | -48.0 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-2 | 33.3 | 48.0 | -14.7 | -1.09 | -36.4 | 0.33 | 33.3 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.0 | -52.0 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 24-19 | 55.8 | 49.7 | 6.1 | +2.92 | 6.8 | -0.05 | 34.9 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | total | 36-28 | 56.2 | 49.8 | 6.4 | +4.78 | 7.5 | -0.16 | 31.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | total | 27-16 | 62.8 | 50.2 | 12.6 | +8.55 | 19.9 | 0.26 | 37.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level+pin_value | total | 8-5 | 61.5 | 50.4 | 11.1 | +2.23 | 17.2 | 0.23 | 30.8 | keep collecting (13/30) |
| money_moving+pin_value | total | 5-3 | 62.5 | 50.3 | 12.2 | +1.47 | 18.3 | 0.12 | 25.0 | keep collecting (8/30) |
| pin_value+sharp_gap | total | 11-6 | 64.7 | 50.2 | 14.5 | +3.92 | 23.1 | -0.06 | 29.4 | keep collecting (17/30) |
| follow_move+money_level | total | 20-18 | 52.6 | 49.5 | 3.1 | +0.17 | 0.4 | 0.16 | 36.8 | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 7-8 | 46.7 | 49.8 | -3.1 | -1.75 | -11.7 | -0.33 | 26.7 | keep collecting (15/30) |
| follow_move+rlm_ratio | total | 10-4 | 71.4 | 50.8 | 20.6 | +5.22 | 37.3 | 0.64 | 57.1 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 25-13 | 65.8 | 50.1 | 15.7 | +9.78 | 25.7 | 0.37 | 42.1 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
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
| consensus_gap+money_delta | total | 2-0 | 100.0 | 48.9 | 51.1 | +1.78 | 88.9 | 0.0 | 0.0 | keep collecting (2/30) |
| follow_move+money_delta | total | 2-1 | 66.7 | 50.4 | 16.3 | +0.78 | 26.0 | 1.0 | 33.3 | keep collecting (3/30) |
| money_delta+money_moving | total | 6-1 | 85.7 | 50.5 | 35.2 | +4.35 | 62.2 | 0.29 | 14.3 | keep collecting (7/30) |
| money_delta+pin_value | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 | -0.5 | 0.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 5-0 | 100.0 | 50.2 | 49.8 | +4.44 | 88.9 | 0.4 | 20.0 | keep collecting (5/30) |
| follow_move+pin_move | total | 2-0 | 100.0 | 51.1 | 48.9 | +1.86 | 93.0 | 1.0 | 100.0 | keep collecting (2/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.82 | 90.9 | -0.5 | 0.0 | keep collecting (2/30) |
| consensus_gap+rlm_ratio | total | 2-1 | 66.7 | 51.1 | 15.6 | +0.86 | 28.7 | 0.67 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | total | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_value | total | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |

## CLOSE  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_move | both | 462-464 | 49.9 | 50.0 | -0.1 | -30.46 | -3.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta | both | 299-393 | 43.2 | 43.9 | -0.7 | -49.53 | -7.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm | both | 130-146 | 47.1 | 42.0 | 5.1 | +30.34 | 11.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | both | 809-720 | 52.9 | 52.0 | 0.9 | -86.12 | -5.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | both | 190-210 | 47.5 | 44.4 | 3.1 | +6.06 | 1.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level | both | 1015-753 | 57.4 | 55.8 | 1.6 | -66.83 | -3.8 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 790-916 | 46.3 | 47.4 | -1.1 | -112.58 | -6.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | both | 790-918 | 46.3 | 47.8 | -1.5 | -123.03 | -7.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | both | 328-345 | 48.7 | 47.5 | 1.2 | -4.94 | -0.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 317-438 | 42.0 | 46.7 | -4.7 | -88.55 | -11.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+follow_move | both | 121-124 | 49.4 | 50.9 | -1.5 | -17.52 | -7.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | both | 141-237 | 37.3 | 43.9 | -6.6 | -32.6 | -8.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_move | both | 74-79 | 48.4 | 50.4 | -2.0 | +0.94 | 0.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | both | 23-39 | 37.1 | 36.7 | 0.4 | +10.03 | 16.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_value | both | 125-144 | 46.5 | 44.9 | 1.6 | -0.47 | -0.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | both | 25-43 | 36.8 | 39.2 | -2.4 | -1.66 | -2.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | both | 140-241 | 36.7 | 43.3 | -6.5 | -33.59 | -8.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_moving | both | 436-465 | 48.4 | 49.4 | -1.1 | -64.2 | -7.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_move | both | 332-331 | 50.1 | 50.3 | -0.2 | -30.01 | -4.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_rlm | both | 102-103 | 49.8 | 44.2 | 5.6 | +9.93 | 4.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | both | 114-111 | 50.7 | 48.7 | 2.0 | -9.32 | -4.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | both | 190-210 | 47.5 | 44.4 | 3.1 | +6.06 | 1.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 441-461 | 48.9 | 49.3 | -0.4 | -53.09 | -5.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_move | both | 279-308 | 47.5 | 48.7 | -1.1 | -24.9 | -4.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_rlm | both | 124-143 | 46.4 | 42.0 | 4.5 | +27.38 | 10.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_value | both | 143-174 | 45.1 | 46.7 | -1.6 | -15.41 | -4.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | both | 182-204 | 47.2 | 44.4 | 2.7 | +4.15 | 1.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+sharp_gap | both | 757-881 | 46.2 | 47.5 | -1.3 | -106.26 | -6.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_rlm | both | 121-119 | 50.4 | 44.2 | 6.2 | +26.68 | 11.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_value | both | 145-148 | 49.5 | 48.9 | 0.6 | -7.5 | -2.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_ratio | both | 111-100 | 52.6 | 45.6 | 7.0 | +20.59 | 9.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | both | 285-308 | 48.1 | 48.6 | -0.5 | -19.61 | -3.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+pin_value | both | 38-37 | 50.7 | 45.2 | 5.5 | +14.72 | 19.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_ratio | both | 102-103 | 49.8 | 44.2 | 5.6 | +9.93 | 4.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | both | 130-146 | 47.1 | 42.0 | 5.1 | +30.34 | 11.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 36-28 | 56.2 | 48.6 | 7.6 | +4.83 | 7.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | both | 146-175 | 45.5 | 46.6 | -1.2 | -13.74 | -4.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio+sharp_gap | both | 190-210 | 47.5 | 44.4 | 3.1 | +6.06 | 1.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 145-165 | 46.8 | 45.9 | 0.9 | -17.13 | -5.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+money_moving | both | 561-503 | 52.7 | 52.5 | 0.2 | -46.41 | -4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | both | 554-495 | 52.8 | 52.3 | 0.5 | -38.17 | -3.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | both | 539-381 | 58.6 | 56.8 | 1.8 | -42.29 | -4.6 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 93-78 | 54.4 | 48.7 | 5.7 | +11.79 | 6.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | both | 192-157 | 55.0 | 58.0 | -3.0 | -23.27 | -6.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | both | 272-256 | 51.5 | 53.2 | -1.7 | -34.08 | -6.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | both | 155-152 | 50.5 | 49.6 | 0.9 | -17.39 | -5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_moving | both | 214-308 | 41.0 | 42.4 | -1.4 | -42.73 | -8.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_delta | both | 40-108 | 27.0 | 36.3 | -9.3 | -31.2 | -21.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_level | both | 112-104 | 51.9 | 47.2 | 4.7 | +13.89 | 6.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | both | 67-68 | 49.6 | 46.7 | 2.9 | -3.48 | -2.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+sharp_gap | both | 211-303 | 41.1 | 42.4 | -1.3 | -40.9 | -8.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 110-128 | 46.2 | 46.3 | -0.1 | -8.78 | -3.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_rlm | both | 59-42 | 58.4 | 46.9 | 11.5 | +16.5 | 16.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_rlm | both | 75-89 | 45.7 | 42.0 | 3.7 | +8.34 | 5.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+rlm_ratio | both | 107-109 | 49.5 | 44.9 | 4.6 | +4.1 | 1.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 51.1 | 48.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_move | moneyline | 97-93 | 51.1 | 49.2 | 1.8 | +7.55 | 4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move | spread | 182-193 | 48.5 | 50.2 | -1.6 | -27.11 | -7.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move | total | 183-178 | 50.7 | 50.3 | 0.4 | -10.9 | -3.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | moneyline | 42-158 | 21.0 | 27.4 | -6.4 | -48.89 | -24.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta | spread | 115-115 | 50.0 | 50.7 | -0.7 | -10.53 | -4.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta | total | 142-120 | 54.2 | 50.5 | 3.6 | +9.89 | 3.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm | moneyline | 34-70 | 32.7 | 27.6 | 5.1 | +18.57 | 17.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm | spread | 24-21 | 53.3 | 50.7 | 2.6 | +0.88 | 2.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm | total | 72-55 | 56.7 | 50.7 | 6.0 | +10.89 | 8.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | moneyline | 294-192 | 60.5 | 56.7 | 3.8 | -26.96 | -5.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| follow_move | spread | 237-244 | 49.3 | 49.6 | -0.3 | -28.83 | -6.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | total | 278-284 | 49.5 | 50.0 | -0.6 | -30.33 | -5.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | moneyline | 34-80 | 29.8 | 29.1 | 0.7 | -6.42 | -5.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio | spread | 41-40 | 50.6 | 50.1 | 0.5 | -2.76 | -3.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio | total | 115-90 | 56.1 | 50.6 | 5.5 | +15.24 | 7.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | moneyline | 396-139 | 74.0 | 70.1 | 3.9 | -13.5 | -2.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 295-308 | 48.9 | 49.3 | -0.4 | -41.96 | -7.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level | total | 324-306 | 51.4 | 49.8 | 1.6 | -11.37 | -1.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 181-310 | 36.9 | 41.3 | -4.4 | -59.31 | -12.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| sharp_gap | spread | 304-293 | 50.9 | 49.6 | 1.3 | -18.7 | -3.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 305-313 | 49.4 | 50.2 | -0.9 | -34.57 | -5.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | moneyline | 189-300 | 38.7 | 42.4 | -3.8 | -50.27 | -10.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | spread | 301-296 | 50.4 | 49.6 | 0.8 | -24.57 | -4.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | total | 300-322 | 48.2 | 50.2 | -2.0 | -48.18 | -7.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | moneyline | 17-53 | 24.3 | 28.5 | -4.2 | +11.19 | 16.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | spread | 148-140 | 51.4 | 49.7 | 1.7 | -10.82 | -3.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | total | 163-152 | 51.7 | 49.8 | 1.9 | -5.31 | -1.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 52.0 | 48.0 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 135-264 | 33.8 | 44.2 | -10.4 | -73.2 | -18.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 84-73 | 53.5 | 49.3 | 4.2 | -1.4 | -0.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap | total | 98-101 | 49.2 | 49.5 | -0.2 | -13.95 | -7.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | moneyline | 134-75 | 64.1 | 64.3 | -0.2 | -5.04 | -2.4 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+sharp_gap | moneyline | 125-73 | 63.1 | 63.7 | -0.6 | -4.65 | -2.3 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_moving+sharp_gap | moneyline | 167-286 | 36.9 | 41.2 | -4.3 | -46.55 | -10.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+follow_move | moneyline | 50-64 | 43.9 | 53.0 | -9.1 | -19.13 | -16.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | moneyline | 93-58 | 61.6 | 69.8 | -8.2 | -10.37 | -6.9 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| consensus_gap+money_moving | moneyline | 52-150 | 25.7 | 39.2 | -13.4 | -22.86 | -11.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_level | moneyline | 234-70 | 77.0 | 71.6 | 5.4 | -7.87 | -2.6 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| follow_move+money_moving | moneyline | 94-107 | 46.8 | 48.2 | -1.4 | -16.72 | -8.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_moving | moneyline | 39-142 | 21.5 | 27.1 | -5.5 | -35.86 | -19.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+sharp_gap | moneyline | 37-141 | 20.8 | 27.1 | -6.3 | -37.05 | -20.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 50-155 | 24.4 | 38.0 | -13.7 | -25.74 | -12.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+sharp_gap | moneyline | 91-106 | 46.2 | 47.2 | -1.0 | -16.14 | -8.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+pin_move | moneyline | 26-31 | 45.6 | 52.1 | -6.5 | +7.23 | 12.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 10-28 | 26.3 | 28.3 | -2.0 | +9.65 | 25.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 4-30 | 11.8 | 28.6 | -16.8 | -7.04 | -20.7 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 78-63 | 55.3 | 51.2 | 4.1 | +6.21 | 4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_rlm | moneyline | 22-39 | 36.1 | 28.9 | 7.1 | +0.5 | 0.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 34-80 | 29.8 | 29.1 | 0.7 | -6.42 | -5.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 41-59 | 41.0 | 41.8 | -0.8 | +7.36 | 7.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+pin_rlm | moneyline | 33-68 | 32.7 | 27.7 | 5.0 | +19.17 | 19.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 33-76 | 30.3 | 29.3 | 1.0 | -3.82 | -3.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_rlm | moneyline | 25-43 | 36.8 | 27.9 | 8.9 | +14.91 | 21.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 20-30 | 40.0 | 29.6 | 10.4 | +7.3 | 14.6 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+sharp_gap | moneyline | 41-60 | 40.6 | 41.1 | -0.5 | +6.18 | 6.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 22-39 | 36.1 | 28.9 | 7.1 | +0.5 | 0.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 34-70 | 32.7 | 27.6 | 5.1 | +18.57 | 17.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 34-80 | 29.8 | 29.1 | 0.7 | -6.42 | -5.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 10-80 | 11.1 | 27.4 | -16.2 | -29.14 | -32.4 |  |  | HYPOTHESIS (in-sample) -- INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 13-44 | 22.8 | 28.3 | -5.5 | +2.38 | 4.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_move | moneyline | 15-35 | 30.0 | 29.6 | 0.4 | -2.46 | -4.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_rlm | moneyline | 19-44 | 30.2 | 28.0 | 2.1 | +2.21 | 3.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+pin_value | moneyline | 2-18 | 10.0 | 25.7 | -15.7 | -11.18 | -55.9 |  |  | keep collecting (20/30) |
| money_moving+pin_value | moneyline | 9-32 | 22.0 | 26.9 | -5.0 | +8.76 | 21.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_move+pin_value | moneyline | 5-9 | 35.7 | 29.2 | 6.5 | +6.58 | 47.0 |  |  | keep collecting (14/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 25.7 | 5.5 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 9-34 | 20.9 | 26.9 | -5.9 | +6.76 | 15.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_delta | moneyline | 22-46 | 32.4 | 30.0 | 2.3 | -10.07 | -14.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_delta+money_level | moneyline | 13-20 | 39.4 | 30.1 | 9.2 | +8.09 | 24.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+rlm_ratio | moneyline | 20-38 | 34.5 | 29.9 | 4.6 | -3.98 | -6.9 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_move | moneyline | 63-37 | 63.0 | 67.5 | -4.5 | -4.79 | -4.8 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 10-9 | 52.6 | 30.8 | 21.8 | +4.79 | 25.2 |  |  | keep collecting (19/30) |
| money_level+rlm_ratio | moneyline | 12-11 | 52.2 | 38.4 | 13.8 | +5.12 | 22.2 |  |  | keep collecting (23/30) |
| money_level+pin_value | moneyline | 4-1 | 80.0 | 64.6 | 15.4 | +1.0 | 19.9 |  |  | keep collecting (5/30) |
| follow_move+pin_value | moneyline | 1-7 | 12.5 | 25.7 | -13.2 | -5.48 | -68.5 |  |  | keep collecting (8/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 25.7 | -0.7 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 34-27 | 55.7 | 48.8 | 7.0 | +1.9 | 3.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | spread | 46-41 | 52.9 | 49.1 | 3.7 | -1.84 | -2.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_move | spread | 24-27 | 47.1 | 49.3 | -2.2 | -6.56 | -12.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 58-43 | 57.4 | 49.2 | 8.2 | +6.24 | 6.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+rlm_ratio | spread | 4-4 | 50.0 | 50.0 | 0.0 | -0.67 | -8.3 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | spread | 45-41 | 52.3 | 49.3 | 3.1 | -2.73 | -3.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | spread | 153-153 | 50.0 | 49.3 | 0.7 | -14.75 | -4.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_move | spread | 116-126 | 47.9 | 49.9 | -2.0 | -20.33 | -8.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_rlm | spread | 19-17 | 52.8 | 50.5 | 2.2 | +0.35 | 1.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | spread | 54-45 | 54.5 | 49.2 | 5.4 | +2.06 | 2.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | spread | 41-40 | 50.6 | 50.1 | 0.5 | -2.76 | -3.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 154-152 | 50.3 | 49.4 | 0.9 | -12.61 | -4.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_move | spread | 110-118 | 48.2 | 49.8 | -1.6 | -18.2 | -8.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | spread | 22-21 | 51.2 | 50.7 | 0.5 | -0.95 | -2.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | spread | 72-73 | 49.7 | 49.3 | 0.3 | -10.97 | -7.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_ratio | spread | 39-39 | 50.0 | 50.0 | 0.0 | -3.69 | -4.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | spread | 296-288 | 50.7 | 49.6 | 1.1 | -21.08 | -3.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_rlm | spread | 24-21 | 53.3 | 50.7 | 2.6 | +0.88 | 2.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 68-75 | 47.6 | 49.8 | -2.2 | -15.02 | -10.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+rlm_ratio | spread | 22-22 | 50.0 | 50.4 | -0.4 | -1.94 | -4.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | spread | 113-118 | 48.9 | 49.8 | -0.9 | -15.47 | -6.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+pin_value | spread | 6-9 | 40.0 | 50.4 | -10.4 | -3.79 | -25.3 |  |  | keep collecting (15/30) |
| pin_rlm+rlm_ratio | spread | 19-17 | 52.8 | 50.5 | 2.2 | +0.35 | 1.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | spread | 24-21 | 53.3 | 50.7 | 2.6 | +0.88 | 2.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 7-6 | 53.8 | 49.2 | 4.6 | -0.01 | -0.1 |  |  | keep collecting (13/30) |
| pin_value+sharp_gap | spread | 72-73 | 49.7 | 49.4 | 0.3 | -11.03 | -7.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | spread | 41-40 | 50.6 | 50.1 | 0.5 | -2.76 | -3.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 147-154 | 48.8 | 49.2 | -0.3 | -21.16 | -7.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+rlm_ratio | spread | 21-25 | 45.7 | 49.7 | -4.1 | -6.13 | -13.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | spread | 232-229 | 50.3 | 49.4 | 1.0 | -20.04 | -4.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | spread | 55-45 | 55.0 | 48.9 | 6.1 | +2.02 | 2.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | spread | 231-230 | 50.1 | 49.3 | 0.8 | -21.96 | -4.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | spread | 100-119 | 45.7 | 49.6 | -4.0 | -28.69 | -13.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_level+pin_value | spread | 79-81 | 49.4 | 49.1 | 0.2 | -12.95 | -8.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_delta | spread | 14-14 | 50.0 | 50.4 | -0.4 | -2.09 | -7.5 |  |  | keep collecting (28/30) |
| follow_move+money_delta | spread | 35-42 | 45.5 | 50.1 | -4.6 | -10.49 | -13.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_level | spread | 38-38 | 50.0 | 49.9 | 0.1 | -3.77 | -5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_moving | spread | 66-69 | 48.9 | 50.4 | -1.5 | -9.46 | -7.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_value | spread | 31-24 | 56.4 | 50.4 | 6.0 | +2.97 | 5.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+sharp_gap | spread | 65-67 | 49.2 | 50.3 | -1.1 | -8.44 | -6.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_rlm | spread | 13-9 | 59.1 | 50.2 | 8.9 | +2.67 | 12.1 |  |  | keep collecting (22/30) |
| money_delta+rlm_ratio | spread | 16-24 | 40.0 | 49.9 | -9.9 | -9.78 | -24.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 52.0 | 48.0 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_move | spread | 32-39 | 45.1 | 50.7 | -5.7 | -9.87 | -13.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_rlm | spread | 12-14 | 46.2 | 50.5 | -4.3 | -3.22 | -12.4 |  |  | keep collecting (26/30) |
| follow_move+money_delta | total | 88-77 | 53.3 | 50.5 | 2.8 | +3.42 | 2.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+money_moving | total | 196-198 | 49.7 | 50.0 | -0.3 | -19.42 | -4.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+sharp_gap | total | 197-193 | 50.5 | 50.0 | 0.5 | -13.48 | -3.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+sharp_gap | total | 294-307 | 48.9 | 50.2 | -1.3 | -38.64 | -6.4 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap+money_level | total | 44-54 | 44.9 | 49.2 | -4.3 | -14.92 | -15.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_move | total | 24-21 | 53.3 | 49.5 | 3.8 | +0.27 | 0.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_value | total | 54-57 | 48.6 | 49.4 | -0.8 | -9.09 | -8.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_moving | total | 189-205 | 48.0 | 50.2 | -2.2 | -32.74 | -8.3 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+sharp_gap | total | 196-203 | 49.1 | 50.2 | -1.1 | -24.33 | -6.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_move | total | 109-100 | 52.2 | 50.1 | 2.1 | -0.6 | -0.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | total | 72-70 | 50.7 | 49.5 | 1.2 | -5.44 | -3.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_value | total | 72-64 | 52.9 | 50.0 | 2.9 | +0.94 | 0.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_move | total | 128-131 | 49.4 | 50.3 | -0.9 | -14.07 | -5.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+money_moving | total | 109-97 | 52.9 | 50.6 | 2.3 | +2.59 | 1.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+money_level | total | 158-157 | 50.2 | 49.9 | 0.3 | -13.26 | -4.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_value | total | 59-59 | 50.0 | 49.9 | 0.1 | -5.9 | -5.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_value | total | 62-69 | 47.3 | 50.0 | -2.7 | -13.2 | -10.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value+sharp_gap | total | 65-68 | 48.9 | 50.0 | -1.2 | -9.46 | -7.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_moving | total | 43-46 | 48.3 | 49.5 | -1.2 | -7.9 | -8.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+sharp_gap | total | 45-45 | 50.0 | 49.5 | 0.5 | -5.12 | -5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+follow_move | total | 37-33 | 52.9 | 49.3 | 3.5 | -0.3 | -0.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_delta | total | 16-14 | 53.3 | 49.9 | 3.5 | +0.03 | 0.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+sharp_gap | total | 109-95 | 53.4 | 50.6 | 2.8 | +4.59 | 2.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 61-46 | 57.0 | 50.5 | 6.6 | +9.58 | 9.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+pin_move | total | 63-54 | 53.8 | 50.7 | 3.1 | +3.55 | 3.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+sharp_gap | total | 131-130 | 50.2 | 50.4 | -0.2 | -10.33 | -4.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_move | total | 138-142 | 49.3 | 50.2 | -0.9 | -15.89 | -5.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | total | 10-8 | 55.6 | 49.9 | 5.7 | +0.87 | 4.8 |  |  | keep collecting (18/30) |
| consensus_gap+rlm_ratio | total | 17-9 | 65.4 | 49.7 | 15.7 | +6.04 | 23.2 |  |  | keep collecting (26/30) |
| follow_move+pin_rlm | total | 61-47 | 56.5 | 50.7 | 5.8 | +9.07 | 8.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+rlm_ratio | total | 115-90 | 56.1 | 50.6 | 5.5 | +15.24 | 7.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 36-24 | 60.0 | 50.7 | 9.3 | +9.04 | 15.1 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+rlm_ratio | total | 60-42 | 58.8 | 50.5 | 8.4 | +12.81 | 12.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+pin_rlm | total | 69-54 | 56.1 | 50.7 | 5.4 | +9.15 | 7.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving+rlm_ratio | total | 110-89 | 55.3 | 50.6 | 4.7 | +11.66 | 5.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_move+pin_rlm | total | 72-55 | 56.7 | 50.7 | 6.0 | +10.89 | 8.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 69-48 | 59.0 | 50.6 | 8.3 | +15.24 | 13.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+pin_value | total | 27-17 | 61.4 | 50.5 | 10.9 | +7.44 | 16.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+rlm_ratio | total | 61-47 | 56.5 | 50.7 | 5.8 | +9.07 | 8.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_rlm+sharp_gap | total | 72-55 | 56.7 | 50.7 | 6.0 | +10.89 | 8.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 28-19 | 59.6 | 50.4 | 9.2 | +6.32 | 13.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm_ratio+sharp_gap | total | 115-90 | 56.1 | 50.6 | 5.5 | +15.24 | 7.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 44-31 | 58.7 | 50.8 | 7.9 | +9.34 | 12.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_delta+rlm_ratio | total | 71-47 | 60.2 | 50.6 | 9.5 | +17.86 | 15.1 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_delta+pin_value | total | 34-26 | 56.7 | 50.4 | 6.3 | +4.73 | 7.9 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 51.1 | 48.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

# Pooled (fit + forward together)

Kept for continuity. **Contaminated** — it mixes the games the engine was built
on with the games testing it. Use the forward table for any decision.

## EARLY  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_move | both | 5-9 | 35.7 | 48.1 | -12.4 | -5.1 | -36.4 | 0.22 | 50.0 | keep collecting (14/30) |
| money_delta | both | 10-5 | 66.7 | 42.2 | 24.5 | +6.43 | 42.9 | -0.38 | 26.7 | keep collecting (15/30) |
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
| money_delta+money_level | both | 3-1 | 75.0 | 44.4 | 30.6 | +2.46 | 61.5 | 0.95 | 50.0 | keep collecting (4/30) |
| money_delta+money_moving | both | 9-5 | 64.3 | 41.6 | 22.7 | +5.53 | 39.5 | -0.41 | 28.6 | keep collecting (14/30) |
| money_delta+pin_value | both | 3-1 | 75.0 | 50.0 | 25.0 | +1.61 | 40.3 | 0.0 | 25.0 | keep collecting (4/30) |
| money_delta+sharp_gap | both | 7-4 | 63.6 | 39.2 | 24.4 | +4.78 | 43.5 | -0.52 | 36.4 | keep collecting (11/30) |
| pin_value+sharp_gap | both | 13-8 | 61.9 | 48.9 | 13.0 | +3.66 | 17.4 | -0.18 | 33.3 | keep collecting (21/30) |
| book_lag+pin_move | both | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+follow_move | both | 30-38 | 44.1 | 51.4 | -7.3 | -13.76 | -20.2 | 0.8 | 57.4 | no edge shown yet |
| follow_move+pin_value | both | 20-17 | 54.1 | 48.8 | 5.3 | +0.41 | 1.1 | -0.12 | 29.7 | no edge shown yet |
| consensus_gap+sharp_gap | both | 24-44 | 35.3 | 44.5 | -9.2 | -11.04 | -16.2 | 0.92 | 50.0 | DROP: below break-even |
| follow_move+money_level | both | 86-41 | 67.7 | 60.4 | 7.3 | +1.27 | 1.0 | 0.09 | 44.1 | PROMOTE: beats break-even and its own base rate |
| money_level+rlm_ratio | both | 11-6 | 64.7 | 40.7 | 24.0 | +5.43 | 31.9 | 1.18 | 58.8 | keep collecting (17/30) |
| pin_value+rlm_ratio | both | 2-2 | 50.0 | 44.2 | 5.8 | -0.18 | -4.5 | -1.7 | 25.0 | keep collecting (4/30) |
| follow_move+money_moving | both | 50-25 | 66.7 | 53.4 | 13.3 | +11.4 | 15.2 | 0.39 | 53.3 | PROMOTE: beats break-even and its own base rate |
| consensus_gap+money_delta | both | 3-0 | 100.0 | 48.6 | 51.4 | +2.61 | 87.1 | 0.0 | 0.0 | keep collecting (3/30) |
| follow_move+money_delta | both | 5-2 | 71.4 | 39.5 | 32.0 | +4.95 | 70.7 | -0.23 | 28.6 | keep collecting (7/30) |
| money_moving+rlm_ratio | both | 11-6 | 64.7 | 40.3 | 24.4 | +7.71 | 45.4 | 0.17 | 47.1 | keep collecting (17/30) |
| consensus_gap+rlm_ratio | both | 3-4 | 42.9 | 36.6 | 6.3 | -0.82 | -11.7 | 0.93 | 71.4 | keep collecting (7/30) |
| pin_move+pin_value | both | 1-4 | 20.0 | 49.0 | -29.0 | -3.09 | -61.8 | 0.2 | 20.0 | keep collecting (5/30) |
| follow_move+pin_move | both | 5-3 | 62.5 | 52.6 | 9.9 | +0.9 | 11.2 | 0.42 | 62.5 | keep collecting (8/30) |
| consensus_gap+pin_move | both | 0-5 | 0.0 | 44.4 | -44.4 | -5.0 | -100.0 | 0.26 | 60.0 | keep collecting (5/30) |
| money_level+pin_move | both | 2-2 | 50.0 | 55.8 | -5.8 | -0.87 | -21.8 | 0.1 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | both | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | both | 1-1 | 50.0 | 25.7 | 24.3 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | both | 1-1 | 50.0 | 25.7 | 24.3 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | both | 1-2 | 33.3 | 25.7 | 7.6 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+consensus_gap | both | 0-2 | 0.0 | 51.5 | -51.5 | -2.0 | -100.0 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+pin_value | both | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_move+sharp_gap | both | 2-1 | 66.7 | 49.6 | 17.0 | +0.13 | 4.3 | -0.07 | 33.3 | keep collecting (3/30) |
| money_level+pin_rlm | both | 1-0 | 100.0 | 25.7 | 74.3 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | both | 1-0 | 100.0 | 25.7 | 74.3 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | both | 1-0 | 100.0 | 25.7 | 74.3 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| money_delta+rlm_ratio | both | 2-0 | 100.0 | 25.7 | 74.3 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | both | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| pin_move | moneyline | 2-3 | 40.0 | 45.1 | -5.1 | -1.87 | -37.4 | 0.02 | 60.0 | keep collecting (5/30) |
| pin_move | spread | 1-4 | 20.0 | 49.6 | -29.6 | -3.09 | -61.8 | 0.4 | 40.0 | keep collecting (5/30) |
| pin_move | total | 2-2 | 50.0 | 50.0 | 0.0 | -0.14 | -3.5 | 0.25 | 50.0 | keep collecting (4/30) |
| money_delta | moneyline | 2-3 | 40.0 | 25.7 | 14.3 | +1.34 | 26.8 | -1.74 | 40.0 | keep collecting (5/30) |
| money_delta | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | keep collecting (2/30) |
| money_delta | total | 7-1 | 87.5 | 50.5 | 37.0 | +5.26 | 65.8 | 0.25 | 12.5 | keep collecting (8/30) |
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
| money_delta+money_moving | moneyline | 2-3 | 40.0 | 25.7 | 14.3 | +1.34 | 26.8 | -1.74 | 40.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | moneyline | 2-3 | 40.0 | 25.7 | 14.3 | +1.34 | 26.8 | -1.74 | 40.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| consensus_gap+pin_move | moneyline | 0-3 | 0.0 | 41.9 | -41.9 | -3.0 | -100.0 | 0.1 | 66.7 | keep collecting (3/30) |
| follow_move+pin_move | moneyline | 2-1 | 66.7 | 58.1 | 8.6 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | moneyline | 2-1 | 66.7 | 58.1 | 8.6 | +0.13 | 4.3 | 0.13 | 66.7 | keep collecting (3/30) |
| consensus_gap+pin_rlm | moneyline | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| follow_move+pin_rlm | moneyline | 1-1 | 50.0 | 25.7 | 24.3 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_rlm+rlm_ratio | moneyline | 1-1 | 50.0 | 25.7 | 24.3 | -0.07 | -3.7 | -2.15 | 50.0 | keep collecting (2/30) |
| pin_rlm+sharp_gap | moneyline | 1-2 | 33.3 | 25.7 | 7.6 | -1.07 | -35.8 | -1.0 | 66.7 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | moneyline | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | -4.8 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | moneyline | 2-0 | 100.0 | 50.0 | 50.0 | +1.13 | 56.5 | -0.1 | 50.0 | keep collecting (2/30) |
| money_level+rlm_ratio | moneyline | 4-3 | 57.1 | 25.7 | 31.4 | +1.87 | 26.7 | 2.0 | 85.7 | keep collecting (7/30) |
| money_level+pin_rlm | moneyline | 1-0 | 100.0 | 25.7 | 74.3 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+pin_rlm | moneyline | 1-0 | 100.0 | 25.7 | 74.3 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| pin_move+rlm_ratio | moneyline | 1-0 | 100.0 | 25.7 | 74.3 | +0.93 | 92.6 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move+money_delta | moneyline | 2-1 | 66.7 | 25.7 | 40.9 | +3.34 | 111.3 | -1.53 | 33.3 | keep collecting (3/30) |
| money_delta+rlm_ratio | moneyline | 2-0 | 100.0 | 25.7 | 74.3 | +4.34 | 217.0 | 0.3 | 50.0 | keep collecting (2/30) |
| money_moving+pin_rlm | moneyline | 0-1 | 0.0 | 25.7 | -25.7 | -1.0 | -100.0 | 1.3 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | moneyline | 1-0 | 100.0 | 25.7 | 74.3 | +1.64 | 164.0 | 3.8 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 5-5 | 50.0 | 48.0 | 2.0 | -0.68 | -6.8 | 1.7 | 70.0 | keep collecting (10/30) |
| consensus_gap+money_moving | spread | 5-0 | 100.0 | 48.0 | 52.0 | +4.32 | 86.3 | 0.6 | 40.0 | keep collecting (5/30) |
| consensus_gap+pin_value | spread | 10-8 | 55.6 | 48.9 | 6.6 | +0.6 | 3.3 | 0.5 | 50.0 | keep collecting (18/30) |
| follow_move+rlm_ratio | spread | 3-2 | 60.0 | 51.2 | 8.8 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 49.0 | 13.5 | +3.09 | 19.3 | 0.62 | 37.5 | keep collecting (16/30) |
| money_level+money_moving | spread | 10-4 | 71.4 | 48.9 | 22.5 | +5.12 | 36.6 | 0.86 | 64.3 | keep collecting (14/30) |
| money_level+pin_value | spread | 3-4 | 42.9 | 49.2 | -6.3 | -1.43 | -20.4 | 0.71 | 71.4 | keep collecting (7/30) |
| money_moving+pin_value | spread | 3-2 | 60.0 | 49.6 | 10.4 | +0.57 | 11.5 | 0.6 | 60.0 | keep collecting (5/30) |
| rlm_ratio+sharp_gap | spread | 3-2 | 60.0 | 51.2 | 8.8 | +0.84 | 16.8 | -0.6 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+money_level | spread | 0-1 | 0.0 | 52.0 | -52.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_moving | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+pin_value | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.5 | 50.0 | redundant -- identical record to money_delta alone, not independent confirmation |
| money_delta+sharp_gap | spread | 0-1 | 0.0 | 52.0 | -52.0 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | spread | 14-11 | 56.0 | 49.3 | 6.7 | +1.62 | 6.5 | 1.0 | 44.0 | keep collecting (25/30) |
| money_moving+sharp_gap | spread | 10-3 | 76.9 | 49.2 | 27.7 | +6.04 | 46.4 | 0.54 | 46.2 | keep collecting (13/30) |
| pin_value+sharp_gap | spread | 2-1 | 66.7 | 49.3 | 17.3 | +0.74 | 24.7 | 0.67 | 66.7 | keep collecting (3/30) |
| consensus_gap+follow_move | spread | 9-9 | 50.0 | 48.7 | 1.3 | -1.2 | -6.7 | 0.89 | 44.4 | keep collecting (18/30) |
| consensus_gap+sharp_gap | spread | 5-3 | 62.5 | 48.0 | 14.5 | +1.32 | 16.5 | 2.12 | 75.0 | keep collecting (8/30) |
| follow_move+money_level | spread | 11-8 | 57.9 | 48.9 | 9.0 | +2.04 | 10.7 | 0.63 | 42.1 | keep collecting (19/30) |
| follow_move+pin_value | spread | 12-7 | 63.2 | 49.1 | 14.1 | +3.45 | 18.2 | 0.26 | 31.6 | keep collecting (19/30) |
| consensus_gap+money_delta | spread | 1-0 | 100.0 | 48.0 | 52.0 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_delta | spread | 1-0 | 100.0 | 48.0 | 52.0 | +0.83 | 83.3 | 0.0 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | spread | 9-1 | 90.0 | 48.4 | 41.6 | +7.22 | 72.2 | 0.2 | 40.0 | keep collecting (10/30) |
| money_level+rlm_ratio | spread | 2-1 | 66.7 | 52.0 | 14.7 | +0.93 | 31.1 | 0.0 | 0.0 | keep collecting (3/30) |
| money_moving+rlm_ratio | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.86 | 93.0 | -1.0 | 0.0 | keep collecting (2/30) |
| pin_move+pin_value | spread | 1-3 | 25.0 | 49.0 | -24.0 | -2.09 | -52.3 | 0.25 | 25.0 | keep collecting (4/30) |
| consensus_gap+pin_move | spread | 0-2 | 0.0 | 48.0 | -48.0 | -2.0 | -100.0 | 0.5 | 50.0 | keep collecting (2/30) |
| follow_move+pin_move | spread | 1-2 | 33.3 | 48.0 | -14.7 | -1.09 | -36.4 | 0.33 | 33.3 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 0-1 | 0.0 | 52.0 | -52.0 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| money_level+money_moving | total | 24-19 | 55.8 | 49.7 | 6.1 | +2.92 | 6.8 | -0.05 | 34.9 | no edge shown yet |
| money_level+sharp_gap | total | 36-28 | 56.2 | 49.8 | 6.4 | +4.78 | 7.5 | -0.16 | 31.2 | no edge shown yet |
| money_moving+sharp_gap | total | 27-16 | 62.8 | 50.2 | 12.6 | +8.55 | 19.9 | 0.26 | 37.2 | no edge shown yet |
| book_lag+pin_move | total | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
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
| consensus_gap+money_delta | total | 2-0 | 100.0 | 48.9 | 51.1 | +1.78 | 88.9 | 0.0 | 0.0 | keep collecting (2/30) |
| follow_move+money_delta | total | 2-1 | 66.7 | 50.4 | 16.3 | +0.78 | 26.0 | 1.0 | 33.3 | keep collecting (3/30) |
| money_delta+money_moving | total | 6-1 | 85.7 | 50.5 | 35.2 | +4.35 | 62.2 | 0.29 | 14.3 | keep collecting (7/30) |
| money_delta+pin_value | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.78 | 88.9 | -0.5 | 0.0 | keep collecting (2/30) |
| money_delta+sharp_gap | total | 5-0 | 100.0 | 50.2 | 49.8 | +4.44 | 88.9 | 0.4 | 20.0 | keep collecting (5/30) |
| follow_move+pin_move | total | 2-0 | 100.0 | 51.1 | 48.9 | +1.86 | 93.0 | 1.0 | 100.0 | keep collecting (2/30) |
| book_lag+consensus_gap | total | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| book_lag+pin_value | total | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_delta+money_level | total | 2-0 | 100.0 | 50.0 | 50.0 | +1.82 | 90.9 | -0.5 | 0.0 | keep collecting (2/30) |
| consensus_gap+rlm_ratio | total | 2-1 | 66.7 | 51.1 | 15.6 | +0.86 | 28.7 | 0.67 | 66.7 | keep collecting (3/30) |
| money_level+pin_move | total | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+pin_value | total | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| pin_move+sharp_gap | total | 0-1 | 0.0 | 48.9 | -48.9 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_move | both | 462-464 | 49.9 | 50.0 | -0.1 | -30.46 | -3.3 |  |  | DROP: below break-even |
| money_delta | both | 299-393 | 43.2 | 43.9 | -0.7 | -49.53 | -7.2 |  |  | DROP: below break-even |
| pin_rlm | both | 130-146 | 47.1 | 42.0 | 5.1 | +30.34 | 11.0 |  |  | DROP: below break-even |
| follow_move | both | 809-720 | 52.9 | 52.0 | 0.9 | -86.12 | -5.6 |  |  | no edge shown yet |
| rlm_ratio | both | 190-210 | 47.5 | 44.4 | 3.1 | +6.06 | 1.5 |  |  | DROP: below break-even |
| money_level | both | 1015-753 | 57.4 | 55.8 | 1.6 | -66.83 | -3.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 790-916 | 46.3 | 47.4 | -1.1 | -112.58 | -6.6 |  |  | DROP: below break-even |
| money_moving | both | 790-918 | 46.3 | 47.8 | -1.5 | -123.03 | -7.2 |  |  | DROP: below break-even |
| pin_value | both | 328-345 | 48.7 | 47.5 | 1.2 | -4.94 | -0.7 |  |  | DROP: below break-even |
| book_lag | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 317-438 | 42.0 | 46.7 | -4.7 | -88.55 | -11.7 |  |  | DROP: below break-even |
| consensus_gap+follow_move | both | 121-124 | 49.4 | 50.9 | -1.5 | -17.52 | -7.2 |  |  | no edge shown yet |
| consensus_gap+money_moving | both | 141-237 | 37.3 | 43.9 | -6.6 | -32.6 | -8.6 |  |  | DROP: below break-even |
| consensus_gap+pin_move | both | 74-79 | 48.4 | 50.4 | -2.0 | +0.94 | 0.6 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 23-39 | 37.1 | 36.7 | 0.4 | +10.03 | 16.2 |  |  | DROP: below break-even |
| consensus_gap+pin_value | both | 125-144 | 46.5 | 44.9 | 1.6 | -0.47 | -0.2 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | both | 25-43 | 36.8 | 39.2 | -2.4 | -1.66 | -2.4 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | both | 140-241 | 36.7 | 43.3 | -6.5 | -33.59 | -8.8 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 436-465 | 48.4 | 49.4 | -1.1 | -64.2 | -7.1 |  |  | DROP: below break-even |
| follow_move+pin_move | both | 332-331 | 50.1 | 50.3 | -0.2 | -30.01 | -4.5 |  |  | no edge shown yet |
| follow_move+pin_rlm | both | 102-103 | 49.8 | 44.2 | 5.6 | +9.93 | 4.8 |  |  | no edge shown yet |
| follow_move+pin_value | both | 114-111 | 50.7 | 48.7 | 2.0 | -9.32 | -4.1 |  |  | no edge shown yet |
| follow_move+rlm_ratio | both | 190-210 | 47.5 | 44.4 | 3.1 | +6.06 | 1.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 441-461 | 48.9 | 49.3 | -0.4 | -53.09 | -5.9 |  |  | DROP: below break-even |
| money_moving+pin_move | both | 279-308 | 47.5 | 48.7 | -1.1 | -24.9 | -4.2 |  |  | DROP: below break-even |
| money_moving+pin_rlm | both | 124-143 | 46.4 | 42.0 | 4.5 | +27.38 | 10.3 |  |  | DROP: below break-even |
| money_moving+pin_value | both | 143-174 | 45.1 | 46.7 | -1.6 | -15.41 | -4.9 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | both | 182-204 | 47.2 | 44.4 | 2.7 | +4.15 | 1.1 |  |  | DROP: below break-even |
| money_moving+sharp_gap | both | 757-881 | 46.2 | 47.5 | -1.3 | -106.26 | -6.5 |  |  | DROP: below break-even |
| pin_move+pin_rlm | both | 121-119 | 50.4 | 44.2 | 6.2 | +26.68 | 11.1 |  |  | no edge shown yet |
| pin_move+pin_value | both | 145-148 | 49.5 | 48.9 | 0.6 | -7.5 | -2.6 |  |  | no edge shown yet |
| pin_move+rlm_ratio | both | 111-100 | 52.6 | 45.6 | 7.0 | +20.59 | 9.8 |  |  | no edge shown yet |
| pin_move+sharp_gap | both | 285-308 | 48.1 | 48.6 | -0.5 | -19.61 | -3.3 |  |  | DROP: below break-even |
| pin_rlm+pin_value | both | 38-37 | 50.7 | 45.2 | 5.5 | +14.72 | 19.6 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | both | 102-103 | 49.8 | 44.2 | 5.6 | +9.93 | 4.8 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | both | 130-146 | 47.1 | 42.0 | 5.1 | +30.34 | 11.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | both | 36-28 | 56.2 | 48.6 | 7.6 | +4.83 | 7.5 |  |  | no edge shown yet |
| pin_value+sharp_gap | both | 146-175 | 45.5 | 46.6 | -1.2 | -13.74 | -4.3 |  |  | DROP: below break-even |
| rlm_ratio+sharp_gap | both | 190-210 | 47.5 | 44.4 | 3.1 | +6.06 | 1.5 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_delta | both | 145-165 | 46.8 | 45.9 | 0.9 | -17.13 | -5.5 |  |  | DROP: below break-even |
| money_level+money_moving | both | 561-503 | 52.7 | 52.5 | 0.2 | -46.41 | -4.4 |  |  | no edge shown yet |
| money_level+sharp_gap | both | 554-495 | 52.8 | 52.3 | 0.5 | -38.17 | -3.6 |  |  | no edge shown yet |
| follow_move+money_level | both | 539-381 | 58.6 | 56.8 | 1.8 | -42.29 | -4.6 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+rlm_ratio | both | 93-78 | 54.4 | 48.7 | 5.7 | +11.79 | 6.9 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 192-157 | 55.0 | 58.0 | -3.0 | -23.27 | -6.7 |  |  | no edge shown yet |
| money_level+pin_move | both | 272-256 | 51.5 | 53.2 | -1.7 | -34.08 | -6.5 |  |  | no edge shown yet |
| money_level+pin_value | both | 155-152 | 50.5 | 49.6 | 0.9 | -17.39 | -5.7 |  |  | no edge shown yet |
| money_delta+money_moving | both | 214-308 | 41.0 | 42.4 | -1.4 | -42.73 | -8.2 |  |  | DROP: below break-even |
| consensus_gap+money_delta | both | 40-108 | 27.0 | 36.3 | -9.3 | -31.2 | -21.1 |  |  | DROP: below break-even |
| money_delta+money_level | both | 112-104 | 51.9 | 47.2 | 4.7 | +13.89 | 6.4 |  |  | no edge shown yet |
| money_delta+pin_value | both | 67-68 | 49.6 | 46.7 | 2.9 | -3.48 | -2.6 |  |  | no edge shown yet |
| money_delta+sharp_gap | both | 211-303 | 41.1 | 42.4 | -1.3 | -40.9 | -8.0 |  |  | DROP: below break-even |
| book_lag+money_delta | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| book_lag+pin_move | both | 2-1 | 66.7 | 50.7 | 16.0 | +0.75 | 25.1 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| money_delta+pin_move | both | 110-128 | 46.2 | 46.3 | -0.1 | -8.78 | -3.7 |  |  | DROP: below break-even |
| money_level+pin_rlm | both | 59-42 | 58.4 | 46.9 | 11.5 | +16.5 | 16.3 |  |  | no edge shown yet |
| money_delta+pin_rlm | both | 75-89 | 45.7 | 42.0 | 3.7 | +8.34 | 5.1 |  |  | DROP: below break-even |
| money_delta+rlm_ratio | both | 107-109 | 49.5 | 44.9 | 4.6 | +4.1 | 1.9 |  |  | no edge shown yet |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 51.1 | 48.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| pin_move | moneyline | 97-93 | 51.1 | 49.2 | 1.8 | +7.55 | 4.0 |  |  | no edge shown yet |
| pin_move | spread | 182-193 | 48.5 | 50.2 | -1.6 | -27.11 | -7.2 |  |  | no edge shown yet |
| pin_move | total | 183-178 | 50.7 | 50.3 | 0.4 | -10.9 | -3.0 |  |  | no edge shown yet |
| money_delta | moneyline | 42-158 | 21.0 | 27.4 | -6.4 | -48.89 | -24.4 |  |  | DROP: below break-even |
| money_delta | spread | 115-115 | 50.0 | 50.7 | -0.7 | -10.53 | -4.6 |  |  | no edge shown yet |
| money_delta | total | 142-120 | 54.2 | 50.5 | 3.6 | +9.89 | 3.8 |  |  | no edge shown yet |
| pin_rlm | moneyline | 34-70 | 32.7 | 27.6 | 5.1 | +18.57 | 17.9 |  |  | DROP: below break-even |
| pin_rlm | spread | 24-21 | 53.3 | 50.7 | 2.6 | +0.88 | 2.0 |  |  | no edge shown yet |
| pin_rlm | total | 72-55 | 56.7 | 50.7 | 6.0 | +10.89 | 8.6 |  |  | no edge shown yet |
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
| pin_value | moneyline | 17-53 | 24.3 | 28.5 | -4.2 | +11.19 | 16.0 |  |  | DROP: below break-even |
| pin_value | spread | 148-140 | 51.4 | 49.7 | 1.7 | -10.82 | -3.8 |  |  | no edge shown yet |
| pin_value | total | 163-152 | 51.7 | 49.8 | 1.9 | -5.31 | -1.7 |  |  | no edge shown yet |
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
| money_delta+money_moving | moneyline | 39-142 | 21.5 | 27.1 | -5.5 | -35.86 | -19.8 |  |  | DROP: below break-even |
| money_delta+sharp_gap | moneyline | 37-141 | 20.8 | 27.1 | -6.3 | -37.05 | -20.8 |  |  | DROP: below break-even |
| consensus_gap+sharp_gap | moneyline | 50-155 | 24.4 | 38.0 | -13.7 | -25.74 | -12.6 |  |  | DROP: below break-even |
| follow_move+sharp_gap | moneyline | 91-106 | 46.2 | 47.2 | -1.0 | -16.14 | -8.2 |  |  | DROP: below break-even |
| consensus_gap+pin_move | moneyline | 26-31 | 45.6 | 52.1 | -6.5 | +7.23 | 12.7 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | moneyline | 10-28 | 26.3 | 28.3 | -2.0 | +9.65 | 25.4 |  |  | DROP: below break-even |
| consensus_gap+rlm_ratio | moneyline | 4-30 | 11.8 | 28.6 | -16.8 | -7.04 | -20.7 |  |  | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_move | moneyline | 78-63 | 55.3 | 51.2 | 4.1 | +6.21 | 4.4 |  |  | no edge shown yet |
| follow_move+pin_rlm | moneyline | 22-39 | 36.1 | 28.9 | 7.1 | +0.5 | 0.8 |  |  | DROP: below break-even |
| follow_move+rlm_ratio | moneyline | 34-80 | 29.8 | 29.1 | 0.7 | -6.42 | -5.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+pin_move | moneyline | 41-59 | 41.0 | 41.8 | -0.8 | +7.36 | 7.4 |  |  | DROP: below break-even |
| money_moving+pin_rlm | moneyline | 33-68 | 32.7 | 27.7 | 5.0 | +19.17 | 19.0 |  |  | DROP: below break-even |
| money_moving+rlm_ratio | moneyline | 33-76 | 30.3 | 29.3 | 1.0 | -3.82 | -3.5 |  |  | DROP: below break-even |
| pin_move+pin_rlm | moneyline | 25-43 | 36.8 | 27.9 | 8.9 | +14.91 | 21.9 |  |  | DROP: below break-even |
| pin_move+rlm_ratio | moneyline | 20-30 | 40.0 | 29.6 | 10.4 | +7.3 | 14.6 |  |  | DROP: below break-even |
| pin_move+sharp_gap | moneyline | 41-60 | 40.6 | 41.1 | -0.5 | +6.18 | 6.1 |  |  | DROP: below break-even |
| pin_rlm+rlm_ratio | moneyline | 22-39 | 36.1 | 28.9 | 7.1 | +0.5 | 0.8 |  |  | DROP: below break-even |
| pin_rlm+sharp_gap | moneyline | 34-70 | 32.7 | 27.6 | 5.1 | +18.57 | 17.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 34-80 | 29.8 | 29.1 | 0.7 | -6.42 | -5.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+money_delta | moneyline | 10-80 | 11.1 | 27.4 | -16.2 | -29.14 | -32.4 |  |  | INVERT candidate: wrong well beyond its base rate |
| consensus_gap+pin_value | moneyline | 13-44 | 22.8 | 28.3 | -5.5 | +2.38 | 4.2 |  |  | DROP: below break-even |
| money_delta+pin_move | moneyline | 15-35 | 30.0 | 29.6 | 0.4 | -2.46 | -4.9 |  |  | DROP: below break-even |
| money_delta+pin_rlm | moneyline | 19-44 | 30.2 | 28.0 | 2.1 | +2.21 | 3.5 |  |  | DROP: below break-even |
| money_delta+pin_value | moneyline | 2-18 | 10.0 | 25.7 | -15.7 | -11.18 | -55.9 |  |  | keep collecting (20/30) |
| money_moving+pin_value | moneyline | 9-32 | 22.0 | 26.9 | -5.0 | +8.76 | 21.4 |  |  | DROP: below break-even |
| pin_move+pin_value | moneyline | 5-9 | 35.7 | 29.2 | 6.5 | +6.58 | 47.0 |  |  | keep collecting (14/30) |
| pin_rlm+pin_value | moneyline | 5-11 | 31.2 | 25.7 | 5.5 | +11.07 | 69.2 |  |  | keep collecting (16/30) |
| pin_value+sharp_gap | moneyline | 9-34 | 20.9 | 26.9 | -5.9 | +6.76 | 15.7 |  |  | DROP: below break-even |
| follow_move+money_delta | moneyline | 22-46 | 32.4 | 30.0 | 2.3 | -10.07 | -14.8 |  |  | DROP: below break-even |
| money_delta+money_level | moneyline | 13-20 | 39.4 | 30.1 | 9.2 | +8.09 | 24.5 |  |  | no edge shown yet |
| money_delta+rlm_ratio | moneyline | 20-38 | 34.5 | 29.9 | 4.6 | -3.98 | -6.9 |  |  | DROP: below break-even |
| money_level+pin_move | moneyline | 63-37 | 63.0 | 67.5 | -4.5 | -4.79 | -4.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level+pin_rlm | moneyline | 10-9 | 52.6 | 30.8 | 21.8 | +4.79 | 25.2 |  |  | keep collecting (19/30) |
| money_level+rlm_ratio | moneyline | 12-11 | 52.2 | 38.4 | 13.8 | +5.12 | 22.2 |  |  | keep collecting (23/30) |
| money_level+pin_value | moneyline | 4-1 | 80.0 | 64.6 | 15.4 | +1.0 | 19.9 |  |  | keep collecting (5/30) |
| follow_move+pin_value | moneyline | 1-7 | 12.5 | 25.7 | -13.2 | -5.48 | -68.5 |  |  | keep collecting (8/30) |
| pin_value+rlm_ratio | moneyline | 1-3 | 25.0 | 25.7 | -0.7 | -1.48 | -37.0 |  |  | keep collecting (4/30) |
| consensus_gap+follow_move | spread | 34-27 | 55.7 | 48.8 | 7.0 | +1.9 | 3.1 |  |  | no edge shown yet |
| consensus_gap+money_moving | spread | 46-41 | 52.9 | 49.1 | 3.7 | -1.84 | -2.1 |  |  | no edge shown yet |
| consensus_gap+pin_move | spread | 24-27 | 47.1 | 49.3 | -2.2 | -6.56 | -12.9 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | spread | 3-3 | 50.0 | 50.0 | 0.0 | -0.49 | -8.1 |  |  | keep collecting (6/30) |
| consensus_gap+pin_value | spread | 58-43 | 57.4 | 49.2 | 8.2 | +6.24 | 6.2 |  |  | no edge shown yet |
| consensus_gap+rlm_ratio | spread | 4-4 | 50.0 | 50.0 | 0.0 | -0.67 | -8.3 |  |  | keep collecting (8/30) |
| consensus_gap+sharp_gap | spread | 45-41 | 52.3 | 49.3 | 3.1 | -2.73 | -3.2 |  |  | no edge shown yet |
| follow_move+money_moving | spread | 153-153 | 50.0 | 49.3 | 0.7 | -14.75 | -4.8 |  |  | no edge shown yet |
| follow_move+pin_move | spread | 116-126 | 47.9 | 49.9 | -2.0 | -20.33 | -8.4 |  |  | no edge shown yet |
| follow_move+pin_rlm | spread | 19-17 | 52.8 | 50.5 | 2.2 | +0.35 | 1.0 |  |  | no edge shown yet |
| follow_move+pin_value | spread | 54-45 | 54.5 | 49.2 | 5.4 | +2.06 | 2.1 |  |  | no edge shown yet |
| follow_move+rlm_ratio | spread | 41-40 | 50.6 | 50.1 | 0.5 | -2.76 | -3.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 154-152 | 50.3 | 49.4 | 0.9 | -12.61 | -4.1 |  |  | no edge shown yet |
| money_moving+pin_move | spread | 110-118 | 48.2 | 49.8 | -1.6 | -18.2 | -8.0 |  |  | no edge shown yet |
| money_moving+pin_rlm | spread | 22-21 | 51.2 | 50.7 | 0.5 | -0.95 | -2.2 |  |  | no edge shown yet |
| money_moving+pin_value | spread | 72-73 | 49.7 | 49.3 | 0.3 | -10.97 | -7.6 |  |  | no edge shown yet |
| money_moving+rlm_ratio | spread | 39-39 | 50.0 | 50.0 | 0.0 | -3.69 | -4.7 |  |  | no edge shown yet |
| money_moving+sharp_gap | spread | 296-288 | 50.7 | 49.6 | 1.1 | -21.08 | -3.6 |  |  | no edge shown yet |
| pin_move+pin_rlm | spread | 24-21 | 53.3 | 50.7 | 2.6 | +0.88 | 2.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+pin_value | spread | 68-75 | 47.6 | 49.8 | -2.2 | -15.02 | -10.5 |  |  | no edge shown yet |
| pin_move+rlm_ratio | spread | 22-22 | 50.0 | 50.4 | -0.4 | -1.94 | -4.4 |  |  | no edge shown yet |
| pin_move+sharp_gap | spread | 113-118 | 48.9 | 49.8 | -0.9 | -15.47 | -6.7 |  |  | no edge shown yet |
| pin_rlm+pin_value | spread | 6-9 | 40.0 | 50.4 | -10.4 | -3.79 | -25.3 |  |  | keep collecting (15/30) |
| pin_rlm+rlm_ratio | spread | 19-17 | 52.8 | 50.5 | 2.2 | +0.35 | 1.0 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | spread | 24-21 | 53.3 | 50.7 | 2.6 | +0.88 | 2.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | spread | 7-6 | 53.8 | 49.2 | 4.6 | -0.01 | -0.1 |  |  | keep collecting (13/30) |
| pin_value+sharp_gap | spread | 72-73 | 49.7 | 49.4 | 0.3 | -11.03 | -7.6 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | spread | 41-40 | 50.6 | 50.1 | 0.5 | -2.76 | -3.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 147-154 | 48.8 | 49.2 | -0.3 | -21.16 | -7.0 |  |  | no edge shown yet |
| money_level+rlm_ratio | spread | 21-25 | 45.7 | 49.7 | -4.1 | -6.13 | -13.3 |  |  | no edge shown yet |
| money_level+sharp_gap | spread | 232-229 | 50.3 | 49.4 | 1.0 | -20.04 | -4.3 |  |  | no edge shown yet |
| consensus_gap+money_level | spread | 55-45 | 55.0 | 48.9 | 6.1 | +2.02 | 2.0 |  |  | no edge shown yet |
| money_level+money_moving | spread | 231-230 | 50.1 | 49.3 | 0.8 | -21.96 | -4.8 |  |  | no edge shown yet |
| money_level+pin_move | spread | 100-119 | 45.7 | 49.6 | -4.0 | -28.69 | -13.1 |  |  | DROP: below break-even |
| money_level+pin_value | spread | 79-81 | 49.4 | 49.1 | 0.2 | -12.95 | -8.1 |  |  | no edge shown yet |
| consensus_gap+money_delta | spread | 14-14 | 50.0 | 50.4 | -0.4 | -2.09 | -7.5 |  |  | keep collecting (28/30) |
| follow_move+money_delta | spread | 35-42 | 45.5 | 50.1 | -4.6 | -10.49 | -13.6 |  |  | no edge shown yet |
| money_delta+money_level | spread | 38-38 | 50.0 | 49.9 | 0.1 | -3.77 | -5.0 |  |  | no edge shown yet |
| money_delta+money_moving | spread | 66-69 | 48.9 | 50.4 | -1.5 | -9.46 | -7.0 |  |  | no edge shown yet |
| money_delta+pin_value | spread | 31-24 | 56.4 | 50.4 | 6.0 | +2.97 | 5.4 |  |  | no edge shown yet |
| money_delta+sharp_gap | spread | 65-67 | 49.2 | 50.3 | -1.1 | -8.44 | -6.4 |  |  | no edge shown yet |
| money_level+pin_rlm | spread | 13-9 | 59.1 | 50.2 | 8.9 | +2.67 | 12.1 |  |  | keep collecting (22/30) |
| money_delta+rlm_ratio | spread | 16-24 | 40.0 | 49.9 | -9.9 | -9.78 | -24.4 |  |  | DROP: below break-even |
| book_lag+pin_move | spread | 1-0 | 100.0 | 52.0 | 48.0 | +0.88 | 87.7 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+pin_move | spread | 32-39 | 45.1 | 50.7 | -5.7 | -9.87 | -13.9 |  |  | no edge shown yet |
| money_delta+pin_rlm | spread | 12-14 | 46.2 | 50.5 | -4.3 | -3.22 | -12.4 |  |  | keep collecting (26/30) |
| follow_move+money_delta | total | 88-77 | 53.3 | 50.5 | 2.8 | +3.42 | 2.1 |  |  | no edge shown yet |
| money_level+money_moving | total | 196-198 | 49.7 | 50.0 | -0.3 | -19.42 | -4.9 |  |  | no edge shown yet |
| money_level+sharp_gap | total | 197-193 | 50.5 | 50.0 | 0.5 | -13.48 | -3.5 |  |  | no edge shown yet |
| money_moving+sharp_gap | total | 294-307 | 48.9 | 50.2 | -1.3 | -38.64 | -6.4 |  |  | DROP: below break-even |
| consensus_gap+money_level | total | 44-54 | 44.9 | 49.2 | -4.3 | -14.92 | -15.2 |  |  | no edge shown yet |
| consensus_gap+pin_move | total | 24-21 | 53.3 | 49.5 | 3.8 | +0.27 | 0.6 |  |  | no edge shown yet |
| consensus_gap+pin_value | total | 54-57 | 48.6 | 49.4 | -0.8 | -9.09 | -8.2 |  |  | no edge shown yet |
| follow_move+money_moving | total | 189-205 | 48.0 | 50.2 | -2.2 | -32.74 | -8.3 |  |  | DROP: below break-even |
| follow_move+sharp_gap | total | 196-203 | 49.1 | 50.2 | -1.1 | -24.33 | -6.1 |  |  | no edge shown yet |
| money_level+pin_move | total | 109-100 | 52.2 | 50.1 | 2.1 | -0.6 | -0.3 |  |  | no edge shown yet |
| money_level+pin_value | total | 72-70 | 50.7 | 49.5 | 1.2 | -5.44 | -3.8 |  |  | no edge shown yet |
| pin_move+pin_value | total | 72-64 | 52.9 | 50.0 | 2.9 | +0.94 | 0.7 |  |  | no edge shown yet |
| money_moving+pin_move | total | 128-131 | 49.4 | 50.3 | -0.9 | -14.07 | -5.4 |  |  | no edge shown yet |
| money_delta+money_moving | total | 109-97 | 52.9 | 50.6 | 2.3 | +2.59 | 1.3 |  |  | no edge shown yet |
| follow_move+money_level | total | 158-157 | 50.2 | 49.9 | 0.3 | -13.26 | -4.2 |  |  | no edge shown yet |
| follow_move+pin_value | total | 59-59 | 50.0 | 49.9 | 0.1 | -5.9 | -5.0 |  |  | no edge shown yet |
| money_moving+pin_value | total | 62-69 | 47.3 | 50.0 | -2.7 | -13.2 | -10.1 |  |  | no edge shown yet |
| pin_value+sharp_gap | total | 65-68 | 48.9 | 50.0 | -1.2 | -9.46 | -7.1 |  |  | no edge shown yet |
| consensus_gap+money_moving | total | 43-46 | 48.3 | 49.5 | -1.2 | -7.9 | -8.9 |  |  | no edge shown yet |
| consensus_gap+sharp_gap | total | 45-45 | 50.0 | 49.5 | 0.5 | -5.12 | -5.7 |  |  | no edge shown yet |
| consensus_gap+follow_move | total | 37-33 | 52.9 | 49.3 | 3.5 | -0.3 | -0.4 |  |  | no edge shown yet |
| consensus_gap+money_delta | total | 16-14 | 53.3 | 49.9 | 3.5 | +0.03 | 0.1 |  |  | no edge shown yet |
| money_delta+sharp_gap | total | 109-95 | 53.4 | 50.6 | 2.8 | +4.59 | 2.2 |  |  | no edge shown yet |
| book_lag+money_delta | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_level | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+pin_move | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+sharp_gap | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| money_delta+money_level | total | 61-46 | 57.0 | 50.5 | 6.6 | +9.58 | 9.0 |  |  | no edge shown yet |
| money_delta+pin_move | total | 63-54 | 53.8 | 50.7 | 3.1 | +3.55 | 3.0 |  |  | no edge shown yet |
| pin_move+sharp_gap | total | 131-130 | 50.2 | 50.4 | -0.2 | -10.33 | -4.0 |  |  | no edge shown yet |
| follow_move+pin_move | total | 138-142 | 49.3 | 50.2 | -0.9 | -15.89 | -5.7 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | total | 10-8 | 55.6 | 49.9 | 5.7 | +0.87 | 4.8 |  |  | keep collecting (18/30) |
| consensus_gap+rlm_ratio | total | 17-9 | 65.4 | 49.7 | 15.7 | +6.04 | 23.2 |  |  | keep collecting (26/30) |
| follow_move+pin_rlm | total | 61-47 | 56.5 | 50.7 | 5.8 | +9.07 | 8.4 |  |  | no edge shown yet |
| follow_move+rlm_ratio | total | 115-90 | 56.1 | 50.6 | 5.5 | +15.24 | 7.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_rlm | total | 36-24 | 60.0 | 50.7 | 9.3 | +9.04 | 15.1 |  |  | no edge shown yet |
| money_level+rlm_ratio | total | 60-42 | 58.8 | 50.5 | 8.4 | +12.81 | 12.6 |  |  | no edge shown yet |
| money_moving+pin_rlm | total | 69-54 | 56.1 | 50.7 | 5.4 | +9.15 | 7.4 |  |  | no edge shown yet |
| money_moving+rlm_ratio | total | 110-89 | 55.3 | 50.6 | 4.7 | +11.66 | 5.9 |  |  | no edge shown yet |
| pin_move+pin_rlm | total | 72-55 | 56.7 | 50.7 | 6.0 | +10.89 | 8.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_move+rlm_ratio | total | 69-48 | 59.0 | 50.6 | 8.3 | +15.24 | 13.0 |  |  | no edge shown yet |
| pin_rlm+pin_value | total | 27-17 | 61.4 | 50.5 | 10.9 | +7.44 | 16.9 |  |  | no edge shown yet |
| pin_rlm+rlm_ratio | total | 61-47 | 56.5 | 50.7 | 5.8 | +9.07 | 8.4 |  |  | no edge shown yet |
| pin_rlm+sharp_gap | total | 72-55 | 56.7 | 50.7 | 6.0 | +10.89 | 8.6 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm_ratio | total | 28-19 | 59.6 | 50.4 | 9.2 | +6.32 | 13.4 |  |  | no edge shown yet |
| rlm_ratio+sharp_gap | total | 115-90 | 56.1 | 50.6 | 5.5 | +15.24 | 7.4 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_delta+pin_rlm | total | 44-31 | 58.7 | 50.8 | 7.9 | +9.34 | 12.4 |  |  | no edge shown yet |
| money_delta+rlm_ratio | total | 71-47 | 60.2 | 50.6 | 9.5 | +17.86 | 15.1 |  |  | PROMOTE: beats break-even and its own base rate |
| money_delta+pin_value | total | 34-26 | 56.7 | 50.4 | 6.3 | +4.73 | 7.9 |  |  | no edge shown yet |
| book_lag+pin_rlm | total | 1-0 | 100.0 | 51.1 | 48.9 | +0.88 | 87.7 |  |  | keep collecting (1/30) |

## By market depth (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_move | close | 1-3k bets | 289-288 | 50.1 | 0.3 | -2.6 |  |
| pin_move | close | 3k+ bets | 106-108 | 49.5 | -0.5 | -4.3 |  |
| pin_move | close | <1k bets | 67-68 | 49.6 | -1.2 | -4.6 |  |
| pin_move | close | pin $1-2k | 219-213 | 50.7 | 0.1 | -1.0 |  |
| pin_move | close | pin $2k+ | 159-170 | 48.3 | -1.0 | -7.9 |  |
| pin_move | close | pin limit <$1k | 84-81 | 50.9 | 0.9 | 0.0 |  |
| money_delta | close | 1-3k bets | 187-237 | 44.1 | -0.7 | -7.1 |  |
| money_delta | close | 3k+ bets | 74-94 | 44.0 | 1.3 | 2.0 |  |
| money_delta | close | <1k bets | 38-62 | 38.0 | -4.0 | -22.9 |  |
| money_delta | close | pin $1-2k | 105-106 | 49.8 | 4.1 | 3.3 |  |
| money_delta | close | pin $2k+ | 73-103 | 41.5 | 0.6 | -11.9 |  |
| money_delta | close | pin limit <$1k | 50-51 | 49.5 | -0.6 | -0.8 |  |
| pin_rlm | close | 1-3k bets | 80-91 | 46.8 | 4.3 | 14.4 |  |
| pin_rlm | close | 3k+ bets | 29-34 | 46.0 | 4.4 | 1.7 |  |
| pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| pin_rlm | close | pin $1-2k | 55-57 | 49.1 | 5.6 | 13.3 |  |
| pin_rlm | close | pin $2k+ | 34-62 | 35.4 | 0.6 | -4.2 |  |
| pin_rlm | close | pin limit <$1k | 41-27 | 60.3 | 10.7 | 28.6 |  |
| follow_move | close | 1-3k bets | 522-453 | 53.5 | 2.0 | -3.9 |  |
| follow_move | close | 3k+ bets | 167-159 | 51.2 | -1.2 | -6.9 |  |
| follow_move | close | <1k bets | 120-108 | 52.6 | -0.7 | -11.2 |  |
| follow_move | close | pin $1-2k | 244-265 | 47.9 | -3.3 | -10.6 |  |
| follow_move | close | pin $2k+ | 198-165 | 54.5 | 2.3 | -4.4 |  |
| follow_move | close | pin limit <$1k | 103-102 | 50.2 | 0.1 | -4.1 |  |
| rlm_ratio | close | 1-3k bets | 122-149 | 45.0 | 0.4 | -2.9 |  |
| rlm_ratio | close | 3k+ bets | 42-35 | 54.5 | 10.3 | 17.4 |  |
| rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.8 | 0.8 |  |
| rlm_ratio | close | pin $1-2k | 64-65 | 49.6 | 3.4 | 4.7 |  |
| rlm_ratio | close | pin $2k+ | 35-48 | 42.2 | 4.3 | -6.7 |  |
| rlm_ratio | close | pin limit <$1k | 44-32 | 57.9 | 7.8 | 11.8 |  |
| money_level | close | 1-3k bets | 661-463 | 58.8 | 3.0 | -1.5 |  |
| money_level | close | 3k+ bets | 210-171 | 55.1 | -0.4 | -5.1 |  |
| money_level | close | <1k bets | 144-118 | 55.0 | -1.1 | -11.5 |  |
| money_level | close | pin $1-2k | 296-263 | 53.0 | -1.1 | -5.8 |  |
| money_level | close | pin $2k+ | 254-194 | 56.7 | -1.0 | -7.0 |  |
| money_level | close | pin limit <$1k | 119-118 | 50.2 | 0.1 | -4.5 |  |
| sharp_gap | close | 1-3k bets | 493-588 | 45.6 | -1.8 | -8.5 |  |
| sharp_gap | close | 3k+ bets | 183-190 | 49.1 | 1.7 | 4.7 |  |
| sharp_gap | close | <1k bets | 114-137 | 45.4 | -2.5 | -14.6 |  |
| sharp_gap | close | pin $1-2k | 258-285 | 47.5 | -1.2 | -5.3 |  |
| sharp_gap | close | pin $2k+ | 198-234 | 45.8 | -0.3 | -3.8 |  |
| sharp_gap | close | pin limit <$1k | 112-117 | 48.9 | -1.0 | -2.3 |  |
| money_moving | close | 1-3k bets | 496-587 | 45.8 | -2.1 | -9.1 |  |
| money_moving | close | 3k+ bets | 182-193 | 48.5 | 0.8 | 2.6 |  |
| money_moving | close | <1k bets | 112-137 | 45.0 | -2.5 | -13.5 |  |
| money_moving | close | pin $1-2k | 255-289 | 46.9 | -2.1 | -6.3 |  |
| money_moving | close | pin $2k+ | 199-232 | 46.2 | 0.0 | -3.7 |  |
| money_moving | close | pin limit <$1k | 108-123 | 46.8 | -3.1 | -6.4 |  |
| pin_value | close | 1-3k bets | 204-224 | 47.7 | 0.1 | -1.5 |  |
| pin_value | close | 3k+ bets | 70-77 | 47.6 | -0.3 | -6.1 |  |
| pin_value | close | <1k bets | 54-44 | 55.1 | 8.2 | 10.6 |  |
| pin_value | close | pin $1-2k | 153-177 | 46.4 | -1.7 | -5.7 |  |
| pin_value | close | pin $2k+ | 88-106 | 45.4 | 0.2 | -3.4 |  |
| pin_value | close | pin limit <$1k | 87-62 | 58.4 | 9.0 | 13.7 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 48.0 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 48.0 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 201-270 | 42.7 | -4.7 | -13.0 |  |
| consensus_gap | close | 3k+ bets | 76-89 | 46.1 | -1.0 | 5.9 |  |
| consensus_gap | close | <1k bets | 40-78 | 33.9 | -9.5 | -30.7 |  |
| consensus_gap | close | pin $1-2k | 102-118 | 46.4 | -2.5 | -3.1 |  |
| consensus_gap | close | pin $2k+ | 79-96 | 45.1 | -3.2 | -4.2 |  |
| consensus_gap | close | pin limit <$1k | 47-43 | 52.2 | 2.3 | 2.2 |  |
| consensus_gap+follow_move | close | 1-3k bets | 84-77 | 52.2 | 0.9 | -1.5 |  |
| consensus_gap+money_level | close | 1-3k bets | 133-91 | 59.4 | 0.5 | 1.7 |  |
| consensus_gap+money_moving | close | 1-3k bets | 93-148 | 38.6 | -6.1 | -10.6 |  |
| consensus_gap+pin_move | close | 1-3k bets | 48-48 | 50.0 | -0.6 | 3.7 |  |
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
| consensus_gap+money_delta | close | 1-3k bets | 25-63 | 28.4 | -8.6 | -22.4 |  |
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
| money_delta+pin_move | close | 1-3k bets | 64-77 | 45.4 | -2.3 | -3.4 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 17-26 | 39.5 | 2.0 | 19.2 |  |
| money_level+pin_rlm | close | 1-3k bets | 36-28 | 56.2 | 7.7 | 8.3 |  |
| pin_move+pin_rlm | close | 1-3k bets | 73-75 | 49.3 | 4.6 | 9.7 |  |
| pin_rlm+pin_value | close | 1-3k bets | 28-24 | 53.8 | 7.7 | 29.6 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 80-91 | 46.8 | 4.3 | 14.4 |  |
| money_delta+pin_rlm | close | 1-3k bets | 43-53 | 44.8 | 1.2 | 7.8 |  |
| money_moving+pin_rlm | close | 1-3k bets | 75-88 | 46.0 | 3.5 | 13.9 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 19-30 | 38.8 | -1.2 | 4.1 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 122-149 | 45.0 | 0.4 | -2.9 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 64-76 | 45.7 | -0.3 | -7.6 |  |
| money_level+rlm_ratio | close | 1-3k bets | 58-55 | 51.3 | 1.5 | -0.9 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 116-145 | 44.4 | -0.3 | -3.7 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 122-149 | 45.0 | 0.4 | -2.9 |  |
| follow_move+pin_rlm | close | 1-3k bets | 59-69 | 46.1 | 1.5 | -3.9 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 64-64 | 50.0 | 3.9 | 3.5 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 59-69 | 46.1 | 1.5 | -3.9 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 25-21 | 54.3 | 6.3 | 4.5 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 48.9 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 28-27 | 50.9 | 0.9 | -0.2 |  |
| consensus_gap+money_moving | close | 3k+ bets | 31-49 | 38.8 | -4.8 | 16.1 |  |
| consensus_gap+pin_move | close | 3k+ bets | 20-18 | 52.6 | 2.5 | 6.4 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-6 | 33.3 | -5.9 | 6.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 33-31 | 51.6 | 6.0 | 6.3 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -0.2 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 32-49 | 39.5 | -3.9 | 19.4 |  |
| follow_move+money_moving | close | 3k+ bets | 89-94 | 48.6 | -0.9 | -4.4 |  |
| follow_move+pin_move | close | 3k+ bets | 79-79 | 50.0 | -0.4 | -2.7 |  |
| follow_move+pin_rlm | close | 3k+ bets | 27-23 | 54.0 | 10.3 | 20.5 |  |
| follow_move+pin_value | close | 3k+ bets | 28-28 | 50.0 | 0.5 | -6.1 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 42-35 | 54.5 | 10.3 | 17.4 |  |
| follow_move+sharp_gap | close | 3k+ bets | 91-93 | 49.5 | 0.4 | -2.0 |  |
| money_moving+pin_move | close | 3k+ bets | 63-69 | 47.7 | -0.4 | -4.4 |  |
| money_moving+pin_rlm | close | 3k+ bets | 28-34 | 45.2 | 3.7 | 0.1 |  |
| money_moving+pin_value | close | 3k+ bets | 33-41 | 44.6 | -1.5 | -6.9 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 40-33 | 54.8 | 10.6 | 18.5 |  |
| money_moving+sharp_gap | close | 3k+ bets | 175-183 | 48.9 | 1.5 | 4.2 |  |
| pin_move+pin_rlm | close | 3k+ bets | 29-28 | 50.9 | 7.6 | 12.4 |  |
| pin_move+pin_value | close | 3k+ bets | 29-34 | 46.0 | -3.0 | -13.2 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 31-23 | 57.4 | 12.8 | 25.5 |  |
| pin_move+sharp_gap | close | 3k+ bets | 63-68 | 48.1 | 0.3 | -2.9 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-10 | 33.3 | -10.8 | -36.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 27-23 | 54.0 | 10.3 | 20.5 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 29-34 | 46.0 | 4.4 | 1.7 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 7-6 | 53.8 | 3.7 | 1.4 |  |
| pin_value+sharp_gap | close | 3k+ bets | 33-39 | 45.8 | -0.3 | -4.3 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 42-35 | 54.5 | 10.3 | 17.4 |  |
| follow_move+money_delta | close | 3k+ bets | 36-39 | 48.0 | 2.9 | -0.1 |  |
| money_level+money_moving | close | 3k+ bets | 124-109 | 53.2 | 0.8 | -1.3 |  |
| money_level+sharp_gap | close | 3k+ bets | 123-106 | 53.7 | 1.5 | 0.4 |  |
| follow_move+money_level | close | 3k+ bets | 107-83 | 56.3 | -0.6 | -4.9 |  |
| money_level+rlm_ratio | close | 3k+ bets | 22-10 | 68.8 | 21.6 | 41.7 |  |
| consensus_gap+money_level | close | 3k+ bets | 41-39 | 51.2 | -5.4 | -11.7 |  |
| money_level+pin_move | close | 3k+ bets | 58-58 | 50.0 | -3.7 | -8.4 |  |
| money_level+pin_value | close | 3k+ bets | 37-39 | 48.7 | -0.9 | -9.9 |  |
| money_delta+money_moving | close | 3k+ bets | 57-72 | 44.2 | 2.5 | 7.4 |  |
| consensus_gap+money_delta | close | 3k+ bets | 11-23 | 32.4 | -5.7 | 14.5 |  |
| money_delta+sharp_gap | close | 3k+ bets | 55-69 | 44.4 | 2.8 | 8.4 |  |
| money_delta+money_level | close | 3k+ bets | 30-20 | 60.0 | 13.6 | 21.5 |  |
| money_level+pin_rlm | close | 3k+ bets | 14-8 | 63.6 | 18.5 | 37.8 |  |
| money_delta+pin_value | close | 3k+ bets | 18-16 | 52.9 | 7.5 | -0.2 |  |
| money_delta+pin_move | close | 3k+ bets | 33-34 | 49.3 | 4.8 | 1.0 |  |
| money_delta+pin_rlm | close | 3k+ bets | 20-22 | 47.6 | 6.9 | 2.1 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 27-18 | 60.0 | 16.1 | 28.3 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 48.0 | 87.7 |  |
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
| follow_move+money_moving | close | <1k bets | 54-63 | 46.2 | -3.6 | -13.8 |  |
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
| money_delta+pin_value | close | <1k bets | 6-8 | 42.9 | -2.8 | -19.4 |  |
| consensus_gap+follow_move | close | <1k bets | 9-20 | 31.0 | -19.2 | -51.4 |  |
| follow_move+pin_rlm | close | <1k bets | 16-11 | 59.3 | 16.1 | 17.3 |  |
| follow_move+pin_value | close | <1k bets | 18-12 | 60.0 | 11.2 | 13.8 |  |
| pin_move+pin_rlm | close | <1k bets | 19-16 | 54.3 | 10.7 | 15.0 |  |
| pin_move+rlm_ratio | close | <1k bets | 16-13 | 55.2 | 9.9 | 7.8 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 21.3 | 60.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 16-11 | 59.3 | 16.1 | 17.3 |  |
| pin_value+rlm_ratio | close | <1k bets | 4-1 | 80.0 | 30.1 | 51.7 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 2-7 | 22.2 | -11.4 | -57.2 |  |
| money_delta+money_level | close | <1k bets | 12-17 | 41.4 | -2.3 | -18.9 |  |
| money_level+rlm_ratio | close | <1k bets | 13-13 | 50.0 | 4.4 | -1.9 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 17.5 | 19.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 39-45 | 46.4 | -5.6 | -10.9 |  |
| consensus_gap+money_moving | close | pin $1-2k | 52-64 | 44.8 | -3.5 | -4.1 |  |
| consensus_gap+pin_move | close | pin $1-2k | 40-42 | 48.8 | -3.6 | 3.9 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-18 | 41.9 | 1.4 | 25.8 |  |
| consensus_gap+pin_value | close | pin $1-2k | 59-70 | 45.7 | 0.3 | -7.7 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-14 | 50.0 | 4.8 | 9.0 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 50-62 | 44.6 | -2.4 | -3.2 |  |
| follow_move+money_moving | close | pin $1-2k | 145-175 | 45.3 | -4.6 | -11.0 |  |
| follow_move+pin_move | close | pin $1-2k | 155-160 | 49.2 | -1.6 | -5.5 |  |
| follow_move+pin_rlm | close | pin $1-2k | 45-42 | 51.7 | 6.1 | 10.0 |  |
| follow_move+pin_value | close | pin $1-2k | 52-61 | 46.0 | -3.4 | -13.3 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 64-65 | 49.6 | 3.4 | 4.7 |  |
| follow_move+sharp_gap | close | pin $1-2k | 148-173 | 46.1 | -3.7 | -9.9 |  |
| money_moving+pin_move | close | pin $1-2k | 136-151 | 47.4 | -2.0 | -4.1 |  |
| money_moving+pin_rlm | close | pin $1-2k | 52-55 | 48.6 | 4.8 | 12.8 |  |
| money_moving+pin_value | close | pin $1-2k | 62-91 | 40.5 | -7.2 | -20.5 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 62-62 | 50.0 | 3.4 | 5.4 |  |
| money_moving+sharp_gap | close | pin $1-2k | 247-277 | 47.1 | -1.6 | -5.7 |  |
| pin_move+pin_rlm | close | pin $1-2k | 52-51 | 50.5 | 5.4 | 13.5 |  |
| pin_move+pin_value | close | pin $1-2k | 67-83 | 44.7 | -5.0 | -13.6 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 53-46 | 53.5 | 6.7 | 11.5 |  |
| pin_move+sharp_gap | close | pin $1-2k | 139-150 | 48.1 | -1.1 | -3.1 |  |
| pin_rlm+pin_value | close | pin $1-2k | 14-21 | 40.0 | -8.3 | -16.1 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 45-42 | 51.7 | 6.1 | 10.0 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 55-57 | 49.1 | 5.6 | 13.3 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 16-17 | 48.5 | -1.4 | -8.9 |  |
| pin_value+sharp_gap | close | pin $1-2k | 62-89 | 41.1 | -6.5 | -19.4 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 64-65 | 49.6 | 3.4 | 4.7 |  |
| follow_move+money_level | close | pin $1-2k | 172-163 | 51.3 | -3.1 | -10.0 |  |
| money_level+rlm_ratio | close | pin $1-2k | 39-31 | 55.7 | 7.1 | 8.7 |  |
| money_level+sharp_gap | close | pin $1-2k | 188-186 | 50.3 | -1.5 | -6.5 |  |
| money_level+money_moving | close | pin $1-2k | 188-190 | 49.7 | -2.2 | -7.6 |  |
| consensus_gap+money_level | close | pin $1-2k | 58-55 | 51.3 | -5.8 | -9.7 |  |
| money_level+pin_value | close | pin $1-2k | 67-75 | 47.2 | -2.7 | -11.8 |  |
| money_level+pin_move | close | pin $1-2k | 135-128 | 51.3 | -1.6 | -6.5 |  |
| money_level+pin_rlm | close | pin $1-2k | 27-21 | 56.2 | 9.9 | 10.7 |  |
| follow_move+money_delta | close | pin $1-2k | 52-50 | 51.0 | 5.1 | 5.6 |  |
| money_delta+money_moving | close | pin $1-2k | 71-84 | 45.8 | 1.6 | -1.4 |  |
| money_delta+pin_move | close | pin $1-2k | 53-57 | 48.2 | 0.8 | 1.1 |  |
| money_delta+pin_rlm | close | pin $1-2k | 33-37 | 47.1 | 4.0 | 8.1 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 40-36 | 52.6 | 6.9 | 11.4 |  |
| money_delta+sharp_gap | close | pin $1-2k | 71-82 | 46.4 | 2.2 | -0.1 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 48.0 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 39-35 | 52.7 | 4.9 | 2.7 |  |
| consensus_gap+money_delta | close | pin $1-2k | 16-25 | 39.0 | -1.6 | -7.9 |  |
| money_delta+pin_value | close | pin $1-2k | 37-40 | 48.1 | -0.5 | -9.2 |  |
| follow_move+money_level | close | pin $2k+ | 128-78 | 62.1 | 2.3 | -1.2 |  |
| follow_move+money_moving | close | pin $2k+ | 97-97 | 50.0 | 2.2 | -4.4 |  |
| follow_move+pin_move | close | pin $2k+ | 119-112 | 51.5 | 1.8 | -3.0 |  |
| follow_move+sharp_gap | close | pin $2k+ | 98-98 | 50.0 | 2.3 | -4.1 |  |
| money_level+money_moving | close | pin $2k+ | 133-120 | 52.6 | -0.4 | -4.5 |  |
| money_level+pin_move | close | pin $2k+ | 90-82 | 52.3 | -2.9 | -8.0 |  |
| money_level+sharp_gap | close | pin $2k+ | 133-121 | 52.4 | -0.6 | -4.4 |  |
| money_moving+pin_move | close | pin $2k+ | 86-98 | 46.7 | 0.0 | -5.8 |  |
| money_moving+sharp_gap | close | pin $2k+ | 193-228 | 45.8 | -0.1 | -3.6 |  |
| pin_move+sharp_gap | close | pin $2k+ | 86-99 | 46.5 | -0.2 | -5.9 |  |
| consensus_gap+money_delta | close | pin $2k+ | 6-25 | 19.4 | -11.9 | -63.6 |  |
| consensus_gap+money_moving | close | pin $2k+ | 28-56 | 33.3 | -8.3 | -7.2 |  |
| consensus_gap+pin_value | close | pin $2k+ | 33-43 | 43.4 | 2.9 | 9.2 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 30-59 | 33.7 | -8.7 | -6.6 |  |
| money_delta+money_moving | close | pin $2k+ | 50-75 | 40.0 | 1.6 | -11.4 |  |
| money_delta+pin_value | close | pin $2k+ | 17-20 | 45.9 | 4.2 | -12.2 |  |
| money_delta+sharp_gap | close | pin $2k+ | 48-74 | 39.3 | 0.8 | -12.7 |  |
| money_moving+pin_value | close | pin $2k+ | 48-58 | 45.3 | 1.5 | 6.5 |  |
| pin_value+sharp_gap | close | pin $2k+ | 48-59 | 44.9 | 1.2 | 5.5 |  |
| consensus_gap+pin_move | close | pin $2k+ | 21-27 | 43.8 | -4.3 | -16.7 |  |
| money_delta+pin_move | close | pin $2k+ | 28-42 | 40.0 | -1.5 | -17.0 |  |
| consensus_gap+follow_move | close | pin $2k+ | 24-24 | 50.0 | -0.7 | -16.6 |  |
| follow_move+pin_value | close | pin $2k+ | 29-27 | 51.8 | 5.3 | -1.5 |  |
| pin_move+pin_value | close | pin $2k+ | 40-41 | 49.4 | 2.2 | -2.1 |  |
| follow_move+money_delta | close | pin $2k+ | 28-35 | 44.4 | 2.7 | -7.1 |  |
| follow_move+pin_rlm | close | pin $2k+ | 25-40 | 38.5 | 1.2 | -11.2 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 35-48 | 42.2 | 4.3 | -6.7 |  |
| money_delta+money_level | close | pin $2k+ | 22-18 | 55.0 | 10.5 | 11.8 |  |
| money_delta+pin_rlm | close | pin $2k+ | 18-36 | 33.3 | -1.6 | -14.4 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 18-22 | 45.0 | 6.4 | -1.7 |  |
| money_level+pin_rlm | close | pin $2k+ | 13-9 | 59.1 | 16.6 | 26.7 |  |
| money_level+pin_value | close | pin $2k+ | 47-45 | 51.1 | 1.7 | -5.7 |  |
| money_level+rlm_ratio | close | pin $2k+ | 13-10 | 56.5 | 9.7 | 19.2 |  |
| money_moving+pin_rlm | close | pin $2k+ | 34-62 | 35.4 | 0.6 | -4.2 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 35-47 | 42.7 | 4.7 | -5.5 |  |
| pin_move+pin_rlm | close | pin $2k+ | 29-41 | 41.4 | 3.9 | -1.9 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 26-33 | 44.1 | 4.8 | 1.1 |  |
| pin_rlm+pin_value | close | pin $2k+ | 5-13 | 27.8 | -6.6 | 9.3 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 25-40 | 38.5 | 1.2 | -11.2 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 34-62 | 35.4 | 0.6 | -4.2 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 4-6 | 40.0 | -0.6 | -19.0 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 35-48 | 42.2 | 4.3 | -6.7 |  |
| consensus_gap+money_level | close | pin $2k+ | 52-38 | 57.8 | -4.9 | -10.1 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-19 | 17.4 | -10.6 | -24.8 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-11 | 0.0 | -28.1 | -100.0 |  |
| follow_move+money_delta | close | pin limit <$1k | 31-36 | 46.3 | -4.0 | -11.2 |  |
| money_level+money_moving | close | pin limit <$1k | 66-74 | 47.1 | -2.7 | -9.5 |  |
| money_level+sharp_gap | close | pin limit <$1k | 66-70 | 48.5 | -1.4 | -6.8 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 102-110 | 48.1 | -1.8 | -3.5 |  |
| consensus_gap+money_level | close | pin limit <$1k | 25-25 | 50.0 | -0.2 | -7.8 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 13-10 | 56.5 | 8.3 | 25.1 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 33-31 | 51.6 | 2.7 | 3.9 |  |
| follow_move+money_moving | close | pin limit <$1k | 63-72 | 46.7 | -3.3 | -10.3 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 68-71 | 48.9 | -1.1 | -6.0 |  |
| money_level+pin_move | close | pin limit <$1k | 47-46 | 50.5 | 0.5 | -3.5 |  |
| money_level+pin_value | close | pin limit <$1k | 41-32 | 56.2 | 6.9 | 6.3 |  |
| pin_move+pin_value | close | pin limit <$1k | 38-24 | 61.3 | 12.0 | 23.6 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 16-10 | 61.5 | 11.5 | 12.5 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 20-17 | 54.1 | 5.3 | 14.0 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 22-18 | 55.0 | 6.0 | 14.8 |  |
| follow_move+money_level | close | pin limit <$1k | 52-54 | 49.1 | -1.2 | -6.6 |  |
| follow_move+pin_move | close | pin limit <$1k | 58-59 | 49.6 | -0.5 | -5.1 |  |
| follow_move+pin_value | close | pin limit <$1k | 33-23 | 58.9 | 9.4 | 11.8 |  |
| money_moving+pin_move | close | pin limit <$1k | 57-59 | 49.1 | -0.8 | -2.2 |  |
| money_moving+pin_value | close | pin limit <$1k | 33-25 | 56.9 | 7.7 | 15.6 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 60-59 | 50.4 | 0.4 | 0.2 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 36-27 | 57.1 | 7.7 | 15.5 |  |
| money_delta+money_moving | close | pin limit <$1k | 43-43 | 50.0 | -0.1 | 0.9 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 7-6 | 53.8 | 5.9 | 35.2 |  |
| money_delta+money_level | close | pin limit <$1k | 25-19 | 56.8 | 6.3 | 8.8 |  |
| money_delta+pin_value | close | pin limit <$1k | 13-8 | 61.9 | 13.1 | 38.5 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 42-41 | 50.6 | 0.5 | 2.1 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 29-29 | 50.0 | 0.0 | 3.4 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 6-2 | 75.0 | 28.4 | 96.7 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 24-16 | 60.0 | 10.4 | 26.0 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 38-26 | 59.4 | 9.8 | 27.7 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 40-27 | 59.7 | 9.7 | 21.0 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-3 | 86.4 | 37.2 | 84.9 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 41-27 | 60.3 | 10.7 | 28.6 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 32-21 | 60.4 | 10.1 | 16.1 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 44-32 | 57.9 | 7.8 | 11.8 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 25-20 | 55.6 | 5.3 | 6.8 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 40-31 | 56.3 | 6.3 | 8.9 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 32-21 | 60.4 | 10.1 | 16.1 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 32-21 | 60.4 | 10.1 | 16.1 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 44-32 | 57.9 | 7.8 | 11.8 |  |
| money_level+pin_rlm | close | pin limit <$1k | 19-12 | 61.3 | 10.5 | 17.6 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 21-14 | 60.0 | 9.9 | 16.8 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 16-5 | 76.2 | 25.7 | 46.1 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 5-3 | 62.5 | 12.8 | 18.4 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 48.9 | 87.7 |  |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -48.9 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 5-8 | 38.5 | -9.6 | -31.5 | 0.32 |
| pin_move | early | pin $1-2k | 0-3 | 0.0 | -34.5 | -100.0 | 0.23 |
| pin_move | early | pin limit <$1k | 5-6 | 45.5 | -6.4 | -19.1 | 0.22 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 17.0 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 8-4 | 66.7 | 26.3 | 47.8 | -0.56 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -38.8 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 4-0 | 100.0 | 50.2 | 88.0 | -0.25 |
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
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -52.0 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 17.0 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 17.0 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -0.4 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 16.6 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 4.2 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 3.8 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.6 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.4 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.3 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -48.9 | -100.0 | -1.0 |
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
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.5 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.9 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.5 | 85.1 | 0.0 |
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
| pin_move+pin_value | early | <1k bets | 1-4 | 20.0 | -29.0 | -61.8 | 0.2 |
| follow_move+pin_move | early | <1k bets | 5-3 | 62.5 | 9.9 | 11.2 | 0.42 |
| consensus_gap+pin_value | early | <1k bets | 13-23 | 36.1 | -10.2 | -32.5 | 0.4 |
| money_delta+money_moving | early | <1k bets | 7-4 | 63.6 | 24.3 | 43.8 | -0.61 |
| money_delta+sharp_gap | early | <1k bets | 6-3 | 66.7 | 29.9 | 54.6 | -0.74 |
| consensus_gap+pin_move | early | <1k bets | 0-5 | 0.0 | -44.4 | -100.0 | 0.26 |
| money_level+pin_move | early | <1k bets | 2-2 | 50.0 | -5.8 | -21.8 | 0.1 |
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
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 51.1 | 90.9 | 0.0 |
| money_delta+money_level | early | <1k bets | 3-0 | 100.0 | 58.1 | 115.3 | 0.93 |
| pin_move+sharp_gap | early | <1k bets | 2-1 | 66.7 | 17.0 | 4.3 | -0.07 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 3-2 | 60.0 | 24.1 | 65.0 | -0.32 |
| money_delta+rlm_ratio | early | <1k bets | 2-0 | 100.0 | 74.3 | 217.0 | 0.3 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 48.9 | 90.9 | -1.0 |
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
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -52.0 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -38.8 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -52.0 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -38.8 | -100.0 | 2.5 |
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
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -25.7 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.7 | -100.0 | 1.3 |
| money_level+money_moving | early | pin limit <$1k | 13-7 | 65.0 | 12.5 | 20.2 | 0.48 |
| money_level+sharp_gap | early | pin limit <$1k | 20-16 | 55.6 | 4.8 | 1.6 | 0.14 |
| money_moving+sharp_gap | early | pin limit <$1k | 18-5 | 78.3 | 30.2 | 70.1 | 0.35 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -48.9 | -100.0 | -1.0 |
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
| consensus_gap+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.5 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 22.9 | 72.3 | 0.54 |
| follow_move+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.5 | 85.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 9-3 | 75.0 | 25.4 | 43.3 | 0.33 |
| money_delta+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_delta+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_moving+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.0 | 45.3 | -0.5 |
| money_delta+sharp_gap | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 | -0.5 |
| pin_move+pin_value | early | pin limit <$1k | 1-4 | 20.0 | -29.0 | -61.8 | 0.2 |
| follow_move+pin_move | early | pin limit <$1k | 5-3 | 62.5 | 9.9 | 11.2 | 0.42 |
| consensus_gap+pin_move | early | pin limit <$1k | 0-3 | 0.0 | -56.8 | -100.0 | 0.53 |
| money_level+pin_move | early | pin limit <$1k | 2-2 | 50.0 | -5.8 | -21.8 | 0.1 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -51.1 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -51.1 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 17.0 | 4.3 | -0.07 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 48.9 | 90.9 | -1.0 |
| pin_move | close | 1-3k bets | 289-288 | 50.1 | 0.3 | -2.6 |  |
| pin_move | close | 3k+ bets | 106-108 | 49.5 | -0.5 | -4.3 |  |
| pin_move | close | <1k bets | 67-68 | 49.6 | -1.2 | -4.6 |  |
| pin_move | close | pin $1-2k | 219-213 | 50.7 | 0.1 | -1.0 |  |
| pin_move | close | pin $2k+ | 159-170 | 48.3 | -1.0 | -7.9 |  |
| pin_move | close | pin limit <$1k | 84-81 | 50.9 | 0.9 | 0.0 |  |
| money_delta | close | 1-3k bets | 187-237 | 44.1 | -0.7 | -7.1 |  |
| money_delta | close | 3k+ bets | 74-94 | 44.0 | 1.3 | 2.0 |  |
| money_delta | close | <1k bets | 38-62 | 38.0 | -4.0 | -22.9 |  |
| money_delta | close | pin $1-2k | 105-106 | 49.8 | 4.1 | 3.3 |  |
| money_delta | close | pin $2k+ | 73-103 | 41.5 | 0.6 | -11.9 |  |
| money_delta | close | pin limit <$1k | 50-51 | 49.5 | -0.6 | -0.8 |  |
| pin_rlm | close | 1-3k bets | 80-91 | 46.8 | 4.3 | 14.4 |  |
| pin_rlm | close | 3k+ bets | 29-34 | 46.0 | 4.4 | 1.7 |  |
| pin_rlm | close | <1k bets | 21-21 | 50.0 | 9.4 | 11.0 |  |
| pin_rlm | close | pin $1-2k | 55-57 | 49.1 | 5.6 | 13.3 |  |
| pin_rlm | close | pin $2k+ | 34-62 | 35.4 | 0.6 | -4.2 |  |
| pin_rlm | close | pin limit <$1k | 41-27 | 60.3 | 10.7 | 28.6 |  |
| follow_move | close | 1-3k bets | 522-453 | 53.5 | 2.0 | -3.9 |  |
| follow_move | close | 3k+ bets | 167-159 | 51.2 | -1.2 | -6.9 |  |
| follow_move | close | <1k bets | 120-108 | 52.6 | -0.7 | -11.2 |  |
| follow_move | close | pin $1-2k | 244-265 | 47.9 | -3.3 | -10.6 |  |
| follow_move | close | pin $2k+ | 198-165 | 54.5 | 2.3 | -4.4 |  |
| follow_move | close | pin limit <$1k | 103-102 | 50.2 | 0.1 | -4.1 |  |
| rlm_ratio | close | 1-3k bets | 122-149 | 45.0 | 0.4 | -2.9 |  |
| rlm_ratio | close | 3k+ bets | 42-35 | 54.5 | 10.3 | 17.4 |  |
| rlm_ratio | close | <1k bets | 26-26 | 50.0 | 6.8 | 0.8 |  |
| rlm_ratio | close | pin $1-2k | 64-65 | 49.6 | 3.4 | 4.7 |  |
| rlm_ratio | close | pin $2k+ | 35-48 | 42.2 | 4.3 | -6.7 |  |
| rlm_ratio | close | pin limit <$1k | 44-32 | 57.9 | 7.8 | 11.8 |  |
| money_level | close | 1-3k bets | 661-463 | 58.8 | 3.0 | -1.5 |  |
| money_level | close | 3k+ bets | 210-171 | 55.1 | -0.4 | -5.1 |  |
| money_level | close | <1k bets | 144-118 | 55.0 | -1.1 | -11.5 |  |
| money_level | close | pin $1-2k | 296-263 | 53.0 | -1.1 | -5.8 |  |
| money_level | close | pin $2k+ | 254-194 | 56.7 | -1.0 | -7.0 |  |
| money_level | close | pin limit <$1k | 119-118 | 50.2 | 0.1 | -4.5 |  |
| sharp_gap | close | 1-3k bets | 493-588 | 45.6 | -1.8 | -8.5 |  |
| sharp_gap | close | 3k+ bets | 183-190 | 49.1 | 1.7 | 4.7 |  |
| sharp_gap | close | <1k bets | 114-137 | 45.4 | -2.5 | -14.6 |  |
| sharp_gap | close | pin $1-2k | 258-285 | 47.5 | -1.2 | -5.3 |  |
| sharp_gap | close | pin $2k+ | 198-234 | 45.8 | -0.3 | -3.8 |  |
| sharp_gap | close | pin limit <$1k | 112-117 | 48.9 | -1.0 | -2.3 |  |
| money_moving | close | 1-3k bets | 496-587 | 45.8 | -2.1 | -9.1 |  |
| money_moving | close | 3k+ bets | 182-193 | 48.5 | 0.8 | 2.6 |  |
| money_moving | close | <1k bets | 112-137 | 45.0 | -2.5 | -13.5 |  |
| money_moving | close | pin $1-2k | 255-289 | 46.9 | -2.1 | -6.3 |  |
| money_moving | close | pin $2k+ | 199-232 | 46.2 | 0.0 | -3.7 |  |
| money_moving | close | pin limit <$1k | 108-123 | 46.8 | -3.1 | -6.4 |  |
| pin_value | close | 1-3k bets | 204-224 | 47.7 | 0.1 | -1.5 |  |
| pin_value | close | 3k+ bets | 70-77 | 47.6 | -0.3 | -6.1 |  |
| pin_value | close | <1k bets | 54-44 | 55.1 | 8.2 | 10.6 |  |
| pin_value | close | pin $1-2k | 153-177 | 46.4 | -1.7 | -5.7 |  |
| pin_value | close | pin $2k+ | 88-106 | 45.4 | 0.2 | -3.4 |  |
| pin_value | close | pin limit <$1k | 87-62 | 58.4 | 9.0 | 13.7 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 48.0 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 48.0 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 201-270 | 42.7 | -4.7 | -13.0 |  |
| consensus_gap | close | 3k+ bets | 76-89 | 46.1 | -1.0 | 5.9 |  |
| consensus_gap | close | <1k bets | 40-78 | 33.9 | -9.5 | -30.7 |  |
| consensus_gap | close | pin $1-2k | 102-118 | 46.4 | -2.5 | -3.1 |  |
| consensus_gap | close | pin $2k+ | 79-96 | 45.1 | -3.2 | -4.2 |  |
| consensus_gap | close | pin limit <$1k | 47-43 | 52.2 | 2.3 | 2.2 |  |
| consensus_gap+follow_move | close | 1-3k bets | 84-77 | 52.2 | 0.9 | -1.5 |  |
| consensus_gap+money_level | close | 1-3k bets | 133-91 | 59.4 | 0.5 | 1.7 |  |
| consensus_gap+money_moving | close | 1-3k bets | 93-148 | 38.6 | -6.1 | -10.6 |  |
| consensus_gap+pin_move | close | 1-3k bets | 48-48 | 50.0 | -0.6 | 3.7 |  |
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
| consensus_gap+money_delta | close | 1-3k bets | 25-63 | 28.4 | -8.6 | -22.4 |  |
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
| money_delta+pin_move | close | 1-3k bets | 64-77 | 45.4 | -2.3 | -3.4 |  |
| consensus_gap+pin_rlm | close | 1-3k bets | 17-26 | 39.5 | 2.0 | 19.2 |  |
| money_level+pin_rlm | close | 1-3k bets | 36-28 | 56.2 | 7.7 | 8.3 |  |
| pin_move+pin_rlm | close | 1-3k bets | 73-75 | 49.3 | 4.6 | 9.7 |  |
| pin_rlm+pin_value | close | 1-3k bets | 28-24 | 53.8 | 7.7 | 29.6 |  |
| pin_rlm+sharp_gap | close | 1-3k bets | 80-91 | 46.8 | 4.3 | 14.4 |  |
| money_delta+pin_rlm | close | 1-3k bets | 43-53 | 44.8 | 1.2 | 7.8 |  |
| money_moving+pin_rlm | close | 1-3k bets | 75-88 | 46.0 | 3.5 | 13.9 |  |
| consensus_gap+rlm_ratio | close | 1-3k bets | 19-30 | 38.8 | -1.2 | 4.1 |  |
| follow_move+rlm_ratio | close | 1-3k bets | 122-149 | 45.0 | 0.4 | -2.9 |  |
| money_delta+rlm_ratio | close | 1-3k bets | 64-76 | 45.7 | -0.3 | -7.6 |  |
| money_level+rlm_ratio | close | 1-3k bets | 58-55 | 51.3 | 1.5 | -0.9 |  |
| money_moving+rlm_ratio | close | 1-3k bets | 116-145 | 44.4 | -0.3 | -3.7 |  |
| rlm_ratio+sharp_gap | close | 1-3k bets | 122-149 | 45.0 | 0.4 | -2.9 |  |
| follow_move+pin_rlm | close | 1-3k bets | 59-69 | 46.1 | 1.5 | -3.9 |  |
| pin_move+rlm_ratio | close | 1-3k bets | 64-64 | 50.0 | 3.9 | 3.5 |  |
| pin_rlm+rlm_ratio | close | 1-3k bets | 59-69 | 46.1 | 1.5 | -3.9 |  |
| pin_value+rlm_ratio | close | 1-3k bets | 25-21 | 54.3 | 6.3 | 4.5 |  |
| book_lag+pin_rlm | close | 1-3k bets | 1-0 | 100.0 | 48.9 | 87.7 |  |
| consensus_gap+follow_move | close | 3k+ bets | 28-27 | 50.9 | 0.9 | -0.2 |  |
| consensus_gap+money_moving | close | 3k+ bets | 31-49 | 38.8 | -4.8 | 16.1 |  |
| consensus_gap+pin_move | close | 3k+ bets | 20-18 | 52.6 | 2.5 | 6.4 |  |
| consensus_gap+pin_rlm | close | 3k+ bets | 3-6 | 33.3 | -5.9 | 6.1 |  |
| consensus_gap+pin_value | close | 3k+ bets | 33-31 | 51.6 | 6.0 | 6.3 |  |
| consensus_gap+rlm_ratio | close | 3k+ bets | 4-6 | 40.0 | -0.2 | 14.9 |  |
| consensus_gap+sharp_gap | close | 3k+ bets | 32-49 | 39.5 | -3.9 | 19.4 |  |
| follow_move+money_moving | close | 3k+ bets | 89-94 | 48.6 | -0.9 | -4.4 |  |
| follow_move+pin_move | close | 3k+ bets | 79-79 | 50.0 | -0.4 | -2.7 |  |
| follow_move+pin_rlm | close | 3k+ bets | 27-23 | 54.0 | 10.3 | 20.5 |  |
| follow_move+pin_value | close | 3k+ bets | 28-28 | 50.0 | 0.5 | -6.1 |  |
| follow_move+rlm_ratio | close | 3k+ bets | 42-35 | 54.5 | 10.3 | 17.4 |  |
| follow_move+sharp_gap | close | 3k+ bets | 91-93 | 49.5 | 0.4 | -2.0 |  |
| money_moving+pin_move | close | 3k+ bets | 63-69 | 47.7 | -0.4 | -4.4 |  |
| money_moving+pin_rlm | close | 3k+ bets | 28-34 | 45.2 | 3.7 | 0.1 |  |
| money_moving+pin_value | close | 3k+ bets | 33-41 | 44.6 | -1.5 | -6.9 |  |
| money_moving+rlm_ratio | close | 3k+ bets | 40-33 | 54.8 | 10.6 | 18.5 |  |
| money_moving+sharp_gap | close | 3k+ bets | 175-183 | 48.9 | 1.5 | 4.2 |  |
| pin_move+pin_rlm | close | 3k+ bets | 29-28 | 50.9 | 7.6 | 12.4 |  |
| pin_move+pin_value | close | 3k+ bets | 29-34 | 46.0 | -3.0 | -13.2 |  |
| pin_move+rlm_ratio | close | 3k+ bets | 31-23 | 57.4 | 12.8 | 25.5 |  |
| pin_move+sharp_gap | close | 3k+ bets | 63-68 | 48.1 | 0.3 | -2.9 |  |
| pin_rlm+pin_value | close | 3k+ bets | 5-10 | 33.3 | -10.8 | -36.8 |  |
| pin_rlm+rlm_ratio | close | 3k+ bets | 27-23 | 54.0 | 10.3 | 20.5 |  |
| pin_rlm+sharp_gap | close | 3k+ bets | 29-34 | 46.0 | 4.4 | 1.7 |  |
| pin_value+rlm_ratio | close | 3k+ bets | 7-6 | 53.8 | 3.7 | 1.4 |  |
| pin_value+sharp_gap | close | 3k+ bets | 33-39 | 45.8 | -0.3 | -4.3 |  |
| rlm_ratio+sharp_gap | close | 3k+ bets | 42-35 | 54.5 | 10.3 | 17.4 |  |
| follow_move+money_delta | close | 3k+ bets | 36-39 | 48.0 | 2.9 | -0.1 |  |
| money_level+money_moving | close | 3k+ bets | 124-109 | 53.2 | 0.8 | -1.3 |  |
| money_level+sharp_gap | close | 3k+ bets | 123-106 | 53.7 | 1.5 | 0.4 |  |
| follow_move+money_level | close | 3k+ bets | 107-83 | 56.3 | -0.6 | -4.9 |  |
| money_level+rlm_ratio | close | 3k+ bets | 22-10 | 68.8 | 21.6 | 41.7 |  |
| consensus_gap+money_level | close | 3k+ bets | 41-39 | 51.2 | -5.4 | -11.7 |  |
| money_level+pin_move | close | 3k+ bets | 58-58 | 50.0 | -3.7 | -8.4 |  |
| money_level+pin_value | close | 3k+ bets | 37-39 | 48.7 | -0.9 | -9.9 |  |
| money_delta+money_moving | close | 3k+ bets | 57-72 | 44.2 | 2.5 | 7.4 |  |
| consensus_gap+money_delta | close | 3k+ bets | 11-23 | 32.4 | -5.7 | 14.5 |  |
| money_delta+sharp_gap | close | 3k+ bets | 55-69 | 44.4 | 2.8 | 8.4 |  |
| money_delta+money_level | close | 3k+ bets | 30-20 | 60.0 | 13.6 | 21.5 |  |
| money_level+pin_rlm | close | 3k+ bets | 14-8 | 63.6 | 18.5 | 37.8 |  |
| money_delta+pin_value | close | 3k+ bets | 18-16 | 52.9 | 7.5 | -0.2 |  |
| money_delta+pin_move | close | 3k+ bets | 33-34 | 49.3 | 4.8 | 1.0 |  |
| money_delta+pin_rlm | close | 3k+ bets | 20-22 | 47.6 | 6.9 | 2.1 |  |
| money_delta+rlm_ratio | close | 3k+ bets | 27-18 | 60.0 | 16.1 | 28.3 |  |
| book_lag+pin_move | close | 3k+ bets | 1-0 | 100.0 | 48.0 | 87.7 |  |
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
| follow_move+money_moving | close | <1k bets | 54-63 | 46.2 | -3.6 | -13.8 |  |
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
| money_delta+pin_value | close | <1k bets | 6-8 | 42.9 | -2.8 | -19.4 |  |
| consensus_gap+follow_move | close | <1k bets | 9-20 | 31.0 | -19.2 | -51.4 |  |
| follow_move+pin_rlm | close | <1k bets | 16-11 | 59.3 | 16.1 | 17.3 |  |
| follow_move+pin_value | close | <1k bets | 18-12 | 60.0 | 11.2 | 13.8 |  |
| pin_move+pin_rlm | close | <1k bets | 19-16 | 54.3 | 10.7 | 15.0 |  |
| pin_move+rlm_ratio | close | <1k bets | 16-13 | 55.2 | 9.9 | 7.8 |  |
| pin_rlm+pin_value | close | <1k bets | 5-3 | 62.5 | 21.3 | 60.8 |  |
| pin_rlm+rlm_ratio | close | <1k bets | 16-11 | 59.3 | 16.1 | 17.3 |  |
| pin_value+rlm_ratio | close | <1k bets | 4-1 | 80.0 | 30.1 | 51.7 |  |
| consensus_gap+rlm_ratio | close | <1k bets | 2-7 | 22.2 | -11.4 | -57.2 |  |
| money_delta+money_level | close | <1k bets | 12-17 | 41.4 | -2.3 | -18.9 |  |
| money_level+rlm_ratio | close | <1k bets | 13-13 | 50.0 | 4.4 | -1.9 |  |
| money_level+pin_rlm | close | <1k bets | 9-6 | 60.0 | 17.5 | 19.0 |  |
| consensus_gap+follow_move | close | pin $1-2k | 39-45 | 46.4 | -5.6 | -10.9 |  |
| consensus_gap+money_moving | close | pin $1-2k | 52-64 | 44.8 | -3.5 | -4.1 |  |
| consensus_gap+pin_move | close | pin $1-2k | 40-42 | 48.8 | -3.6 | 3.9 |  |
| consensus_gap+pin_rlm | close | pin $1-2k | 13-18 | 41.9 | 1.4 | 25.8 |  |
| consensus_gap+pin_value | close | pin $1-2k | 59-70 | 45.7 | 0.3 | -7.7 |  |
| consensus_gap+rlm_ratio | close | pin $1-2k | 14-14 | 50.0 | 4.8 | 9.0 |  |
| consensus_gap+sharp_gap | close | pin $1-2k | 50-62 | 44.6 | -2.4 | -3.2 |  |
| follow_move+money_moving | close | pin $1-2k | 145-175 | 45.3 | -4.6 | -11.0 |  |
| follow_move+pin_move | close | pin $1-2k | 155-160 | 49.2 | -1.6 | -5.5 |  |
| follow_move+pin_rlm | close | pin $1-2k | 45-42 | 51.7 | 6.1 | 10.0 |  |
| follow_move+pin_value | close | pin $1-2k | 52-61 | 46.0 | -3.4 | -13.3 |  |
| follow_move+rlm_ratio | close | pin $1-2k | 64-65 | 49.6 | 3.4 | 4.7 |  |
| follow_move+sharp_gap | close | pin $1-2k | 148-173 | 46.1 | -3.7 | -9.9 |  |
| money_moving+pin_move | close | pin $1-2k | 136-151 | 47.4 | -2.0 | -4.1 |  |
| money_moving+pin_rlm | close | pin $1-2k | 52-55 | 48.6 | 4.8 | 12.8 |  |
| money_moving+pin_value | close | pin $1-2k | 62-91 | 40.5 | -7.2 | -20.5 |  |
| money_moving+rlm_ratio | close | pin $1-2k | 62-62 | 50.0 | 3.4 | 5.4 |  |
| money_moving+sharp_gap | close | pin $1-2k | 247-277 | 47.1 | -1.6 | -5.7 |  |
| pin_move+pin_rlm | close | pin $1-2k | 52-51 | 50.5 | 5.4 | 13.5 |  |
| pin_move+pin_value | close | pin $1-2k | 67-83 | 44.7 | -5.0 | -13.6 |  |
| pin_move+rlm_ratio | close | pin $1-2k | 53-46 | 53.5 | 6.7 | 11.5 |  |
| pin_move+sharp_gap | close | pin $1-2k | 139-150 | 48.1 | -1.1 | -3.1 |  |
| pin_rlm+pin_value | close | pin $1-2k | 14-21 | 40.0 | -8.3 | -16.1 |  |
| pin_rlm+rlm_ratio | close | pin $1-2k | 45-42 | 51.7 | 6.1 | 10.0 |  |
| pin_rlm+sharp_gap | close | pin $1-2k | 55-57 | 49.1 | 5.6 | 13.3 |  |
| pin_value+rlm_ratio | close | pin $1-2k | 16-17 | 48.5 | -1.4 | -8.9 |  |
| pin_value+sharp_gap | close | pin $1-2k | 62-89 | 41.1 | -6.5 | -19.4 |  |
| rlm_ratio+sharp_gap | close | pin $1-2k | 64-65 | 49.6 | 3.4 | 4.7 |  |
| follow_move+money_level | close | pin $1-2k | 172-163 | 51.3 | -3.1 | -10.0 |  |
| money_level+rlm_ratio | close | pin $1-2k | 39-31 | 55.7 | 7.1 | 8.7 |  |
| money_level+sharp_gap | close | pin $1-2k | 188-186 | 50.3 | -1.5 | -6.5 |  |
| money_level+money_moving | close | pin $1-2k | 188-190 | 49.7 | -2.2 | -7.6 |  |
| consensus_gap+money_level | close | pin $1-2k | 58-55 | 51.3 | -5.8 | -9.7 |  |
| money_level+pin_value | close | pin $1-2k | 67-75 | 47.2 | -2.7 | -11.8 |  |
| money_level+pin_move | close | pin $1-2k | 135-128 | 51.3 | -1.6 | -6.5 |  |
| money_level+pin_rlm | close | pin $1-2k | 27-21 | 56.2 | 9.9 | 10.7 |  |
| follow_move+money_delta | close | pin $1-2k | 52-50 | 51.0 | 5.1 | 5.6 |  |
| money_delta+money_moving | close | pin $1-2k | 71-84 | 45.8 | 1.6 | -1.4 |  |
| money_delta+pin_move | close | pin $1-2k | 53-57 | 48.2 | 0.8 | 1.1 |  |
| money_delta+pin_rlm | close | pin $1-2k | 33-37 | 47.1 | 4.0 | 8.1 |  |
| money_delta+rlm_ratio | close | pin $1-2k | 40-36 | 52.6 | 6.9 | 11.4 |  |
| money_delta+sharp_gap | close | pin $1-2k | 71-82 | 46.4 | 2.2 | -0.1 |  |
| book_lag+pin_move | close | pin $1-2k | 1-0 | 100.0 | 48.0 | 87.7 |  |
| money_delta+money_level | close | pin $1-2k | 39-35 | 52.7 | 4.9 | 2.7 |  |
| consensus_gap+money_delta | close | pin $1-2k | 16-25 | 39.0 | -1.6 | -7.9 |  |
| money_delta+pin_value | close | pin $1-2k | 37-40 | 48.1 | -0.5 | -9.2 |  |
| follow_move+money_level | close | pin $2k+ | 128-78 | 62.1 | 2.3 | -1.2 |  |
| follow_move+money_moving | close | pin $2k+ | 97-97 | 50.0 | 2.2 | -4.4 |  |
| follow_move+pin_move | close | pin $2k+ | 119-112 | 51.5 | 1.8 | -3.0 |  |
| follow_move+sharp_gap | close | pin $2k+ | 98-98 | 50.0 | 2.3 | -4.1 |  |
| money_level+money_moving | close | pin $2k+ | 133-120 | 52.6 | -0.4 | -4.5 |  |
| money_level+pin_move | close | pin $2k+ | 90-82 | 52.3 | -2.9 | -8.0 |  |
| money_level+sharp_gap | close | pin $2k+ | 133-121 | 52.4 | -0.6 | -4.4 |  |
| money_moving+pin_move | close | pin $2k+ | 86-98 | 46.7 | 0.0 | -5.8 |  |
| money_moving+sharp_gap | close | pin $2k+ | 193-228 | 45.8 | -0.1 | -3.6 |  |
| pin_move+sharp_gap | close | pin $2k+ | 86-99 | 46.5 | -0.2 | -5.9 |  |
| consensus_gap+money_delta | close | pin $2k+ | 6-25 | 19.4 | -11.9 | -63.6 |  |
| consensus_gap+money_moving | close | pin $2k+ | 28-56 | 33.3 | -8.3 | -7.2 |  |
| consensus_gap+pin_value | close | pin $2k+ | 33-43 | 43.4 | 2.9 | 9.2 |  |
| consensus_gap+sharp_gap | close | pin $2k+ | 30-59 | 33.7 | -8.7 | -6.6 |  |
| money_delta+money_moving | close | pin $2k+ | 50-75 | 40.0 | 1.6 | -11.4 |  |
| money_delta+pin_value | close | pin $2k+ | 17-20 | 45.9 | 4.2 | -12.2 |  |
| money_delta+sharp_gap | close | pin $2k+ | 48-74 | 39.3 | 0.8 | -12.7 |  |
| money_moving+pin_value | close | pin $2k+ | 48-58 | 45.3 | 1.5 | 6.5 |  |
| pin_value+sharp_gap | close | pin $2k+ | 48-59 | 44.9 | 1.2 | 5.5 |  |
| consensus_gap+pin_move | close | pin $2k+ | 21-27 | 43.8 | -4.3 | -16.7 |  |
| money_delta+pin_move | close | pin $2k+ | 28-42 | 40.0 | -1.5 | -17.0 |  |
| consensus_gap+follow_move | close | pin $2k+ | 24-24 | 50.0 | -0.7 | -16.6 |  |
| follow_move+pin_value | close | pin $2k+ | 29-27 | 51.8 | 5.3 | -1.5 |  |
| pin_move+pin_value | close | pin $2k+ | 40-41 | 49.4 | 2.2 | -2.1 |  |
| follow_move+money_delta | close | pin $2k+ | 28-35 | 44.4 | 2.7 | -7.1 |  |
| follow_move+pin_rlm | close | pin $2k+ | 25-40 | 38.5 | 1.2 | -11.2 |  |
| follow_move+rlm_ratio | close | pin $2k+ | 35-48 | 42.2 | 4.3 | -6.7 |  |
| money_delta+money_level | close | pin $2k+ | 22-18 | 55.0 | 10.5 | 11.8 |  |
| money_delta+pin_rlm | close | pin $2k+ | 18-36 | 33.3 | -1.6 | -14.4 |  |
| money_delta+rlm_ratio | close | pin $2k+ | 18-22 | 45.0 | 6.4 | -1.7 |  |
| money_level+pin_rlm | close | pin $2k+ | 13-9 | 59.1 | 16.6 | 26.7 |  |
| money_level+pin_value | close | pin $2k+ | 47-45 | 51.1 | 1.7 | -5.7 |  |
| money_level+rlm_ratio | close | pin $2k+ | 13-10 | 56.5 | 9.7 | 19.2 |  |
| money_moving+pin_rlm | close | pin $2k+ | 34-62 | 35.4 | 0.6 | -4.2 |  |
| money_moving+rlm_ratio | close | pin $2k+ | 35-47 | 42.7 | 4.7 | -5.5 |  |
| pin_move+pin_rlm | close | pin $2k+ | 29-41 | 41.4 | 3.9 | -1.9 |  |
| pin_move+rlm_ratio | close | pin $2k+ | 26-33 | 44.1 | 4.8 | 1.1 |  |
| pin_rlm+pin_value | close | pin $2k+ | 5-13 | 27.8 | -6.6 | 9.3 |  |
| pin_rlm+rlm_ratio | close | pin $2k+ | 25-40 | 38.5 | 1.2 | -11.2 |  |
| pin_rlm+sharp_gap | close | pin $2k+ | 34-62 | 35.4 | 0.6 | -4.2 |  |
| pin_value+rlm_ratio | close | pin $2k+ | 4-6 | 40.0 | -0.6 | -19.0 |  |
| rlm_ratio+sharp_gap | close | pin $2k+ | 35-48 | 42.2 | 4.3 | -6.7 |  |
| consensus_gap+money_level | close | pin $2k+ | 52-38 | 57.8 | -4.9 | -10.1 |  |
| consensus_gap+pin_rlm | close | pin $2k+ | 4-19 | 17.4 | -10.6 | -24.8 |  |
| consensus_gap+rlm_ratio | close | pin $2k+ | 0-11 | 0.0 | -28.1 | -100.0 |  |
| follow_move+money_delta | close | pin limit <$1k | 31-36 | 46.3 | -4.0 | -11.2 |  |
| money_level+money_moving | close | pin limit <$1k | 66-74 | 47.1 | -2.7 | -9.5 |  |
| money_level+sharp_gap | close | pin limit <$1k | 66-70 | 48.5 | -1.4 | -6.8 |  |
| money_moving+sharp_gap | close | pin limit <$1k | 102-110 | 48.1 | -1.8 | -3.5 |  |
| consensus_gap+money_level | close | pin limit <$1k | 25-25 | 50.0 | -0.2 | -7.8 |  |
| consensus_gap+pin_move | close | pin limit <$1k | 13-10 | 56.5 | 8.3 | 25.1 |  |
| consensus_gap+pin_value | close | pin limit <$1k | 33-31 | 51.6 | 2.7 | 3.9 |  |
| follow_move+money_moving | close | pin limit <$1k | 63-72 | 46.7 | -3.3 | -10.3 |  |
| follow_move+sharp_gap | close | pin limit <$1k | 68-71 | 48.9 | -1.1 | -6.0 |  |
| money_level+pin_move | close | pin limit <$1k | 47-46 | 50.5 | 0.5 | -3.5 |  |
| money_level+pin_value | close | pin limit <$1k | 41-32 | 56.2 | 6.9 | 6.3 |  |
| pin_move+pin_value | close | pin limit <$1k | 38-24 | 61.3 | 12.0 | 23.6 |  |
| consensus_gap+follow_move | close | pin limit <$1k | 16-10 | 61.5 | 11.5 | 12.5 |  |
| consensus_gap+money_moving | close | pin limit <$1k | 20-17 | 54.1 | 5.3 | 14.0 |  |
| consensus_gap+sharp_gap | close | pin limit <$1k | 22-18 | 55.0 | 6.0 | 14.8 |  |
| follow_move+money_level | close | pin limit <$1k | 52-54 | 49.1 | -1.2 | -6.6 |  |
| follow_move+pin_move | close | pin limit <$1k | 58-59 | 49.6 | -0.5 | -5.1 |  |
| follow_move+pin_value | close | pin limit <$1k | 33-23 | 58.9 | 9.4 | 11.8 |  |
| money_moving+pin_move | close | pin limit <$1k | 57-59 | 49.1 | -0.8 | -2.2 |  |
| money_moving+pin_value | close | pin limit <$1k | 33-25 | 56.9 | 7.7 | 15.6 |  |
| pin_move+sharp_gap | close | pin limit <$1k | 60-59 | 50.4 | 0.4 | 0.2 |  |
| pin_value+sharp_gap | close | pin limit <$1k | 36-27 | 57.1 | 7.7 | 15.5 |  |
| money_delta+money_moving | close | pin limit <$1k | 43-43 | 50.0 | -0.1 | 0.9 |  |
| consensus_gap+money_delta | close | pin limit <$1k | 7-6 | 53.8 | 5.9 | 35.2 |  |
| money_delta+money_level | close | pin limit <$1k | 25-19 | 56.8 | 6.3 | 8.8 |  |
| money_delta+pin_value | close | pin limit <$1k | 13-8 | 61.9 | 13.1 | 38.5 |  |
| money_delta+sharp_gap | close | pin limit <$1k | 42-41 | 50.6 | 0.5 | 2.1 |  |
| book_lag+money_delta | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_level | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+money_moving | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+pin_move | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag+sharp_gap | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| money_delta+pin_move | close | pin limit <$1k | 29-29 | 50.0 | 0.0 | 3.4 |  |
| consensus_gap+pin_rlm | close | pin limit <$1k | 6-2 | 75.0 | 28.4 | 96.7 |  |
| money_delta+pin_rlm | close | pin limit <$1k | 24-16 | 60.0 | 10.4 | 26.0 |  |
| money_moving+pin_rlm | close | pin limit <$1k | 38-26 | 59.4 | 9.8 | 27.7 |  |
| pin_move+pin_rlm | close | pin limit <$1k | 40-27 | 59.7 | 9.7 | 21.0 |  |
| pin_rlm+pin_value | close | pin limit <$1k | 19-3 | 86.4 | 37.2 | 84.9 |  |
| pin_rlm+sharp_gap | close | pin limit <$1k | 41-27 | 60.3 | 10.7 | 28.6 |  |
| follow_move+pin_rlm | close | pin limit <$1k | 32-21 | 60.4 | 10.1 | 16.1 |  |
| follow_move+rlm_ratio | close | pin limit <$1k | 44-32 | 57.9 | 7.8 | 11.8 |  |
| money_delta+rlm_ratio | close | pin limit <$1k | 25-20 | 55.6 | 5.3 | 6.8 |  |
| money_moving+rlm_ratio | close | pin limit <$1k | 40-31 | 56.3 | 6.3 | 8.9 |  |
| pin_move+rlm_ratio | close | pin limit <$1k | 32-21 | 60.4 | 10.1 | 16.1 |  |
| pin_rlm+rlm_ratio | close | pin limit <$1k | 32-21 | 60.4 | 10.1 | 16.1 |  |
| rlm_ratio+sharp_gap | close | pin limit <$1k | 44-32 | 57.9 | 7.8 | 11.8 |  |
| money_level+pin_rlm | close | pin limit <$1k | 19-12 | 61.3 | 10.5 | 17.6 |  |
| money_level+rlm_ratio | close | pin limit <$1k | 21-14 | 60.0 | 9.9 | 16.8 |  |
| pin_value+rlm_ratio | close | pin limit <$1k | 16-5 | 76.2 | 25.7 | 46.1 |  |
| consensus_gap+rlm_ratio | close | pin limit <$1k | 5-3 | 62.5 | 12.8 | 18.4 |  |
| book_lag+pin_rlm | close | pin limit <$1k | 1-0 | 100.0 | 48.9 | 87.7 |  |
| pin_move | early | 1-3k bets | 0-1 | 0.0 | -48.9 | -100.0 | -1.0 |
| pin_move | early | <1k bets | 5-8 | 38.5 | -9.6 | -31.5 | 0.32 |
| pin_move | early | pin $1-2k | 0-3 | 0.0 | -34.5 | -100.0 | 0.23 |
| pin_move | early | pin limit <$1k | 5-6 | 45.5 | -6.4 | -19.1 | 0.22 |
| money_delta | early | 1-3k bets | 2-1 | 66.7 | 17.0 | 23.4 | 0.33 |
| money_delta | early | <1k bets | 8-4 | 66.7 | 26.3 | 47.8 | -0.56 |
| money_delta | early | pin $1-2k | 0-2 | 0.0 | -38.8 | -100.0 | 2.5 |
| money_delta | early | pin limit <$1k | 4-0 | 100.0 | 50.2 | 88.0 | -0.25 |
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
| money_delta+money_level | early | 1-3k bets | 0-1 | 0.0 | -52.0 | -100.0 | 1.0 |
| money_delta+money_moving | early | 1-3k bets | 2-1 | 66.7 | 17.0 | 23.4 | 0.33 |
| money_delta+pin_value | early | 1-3k bets | 2-1 | 66.7 | 17.0 | 23.4 | 0.33 |
| money_delta+sharp_gap | early | 1-3k bets | 1-1 | 50.0 | -0.4 | -6.5 | 0.5 |
| money_level+money_moving | early | 1-3k bets | 13-5 | 72.2 | 16.6 | 23.7 | 0.29 |
| money_level+pin_value | early | 1-3k bets | 6-5 | 54.5 | 4.2 | 3.1 | 0.0 |
| money_level+sharp_gap | early | 1-3k bets | 16-13 | 55.2 | 3.8 | 2.3 | 0.08 |
| money_moving+pin_value | early | 1-3k bets | 6-3 | 66.7 | 16.6 | 25.6 | -0.11 |
| money_moving+sharp_gap | early | 1-3k bets | 13-7 | 65.0 | 19.4 | 42.2 | 0.27 |
| pin_value+sharp_gap | early | 1-3k bets | 8-4 | 66.7 | 16.3 | 26.0 | -0.25 |
| book_lag+pin_move | early | 1-3k bets | 0-1 | 0.0 | -48.9 | -100.0 | -1.0 |
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
| consensus_gap+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.5 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | 1-3k bets | 6-4 | 60.0 | 17.9 | 56.1 | 0.15 |
| follow_move+money_delta | early | 1-3k bets | 2-0 | 100.0 | 51.5 | 85.1 | 0.0 |
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
| pin_move+pin_value | early | <1k bets | 1-4 | 20.0 | -29.0 | -61.8 | 0.2 |
| follow_move+pin_move | early | <1k bets | 5-3 | 62.5 | 9.9 | 11.2 | 0.42 |
| consensus_gap+pin_value | early | <1k bets | 13-23 | 36.1 | -10.2 | -32.5 | 0.4 |
| money_delta+money_moving | early | <1k bets | 7-4 | 63.6 | 24.3 | 43.8 | -0.61 |
| money_delta+sharp_gap | early | <1k bets | 6-3 | 66.7 | 29.9 | 54.6 | -0.74 |
| consensus_gap+pin_move | early | <1k bets | 0-5 | 0.0 | -44.4 | -100.0 | 0.26 |
| money_level+pin_move | early | <1k bets | 2-2 | 50.0 | -5.8 | -21.8 | 0.1 |
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
| consensus_gap+money_delta | early | <1k bets | 1-0 | 100.0 | 51.1 | 90.9 | 0.0 |
| money_delta+money_level | early | <1k bets | 3-0 | 100.0 | 58.1 | 115.3 | 0.93 |
| pin_move+sharp_gap | early | <1k bets | 2-1 | 66.7 | 17.0 | 4.3 | -0.07 |
| money_level+pin_rlm | early | <1k bets | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | <1k bets | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | <1k bets | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| follow_move+money_delta | early | <1k bets | 3-2 | 60.0 | 24.1 | 65.0 | -0.32 |
| money_delta+rlm_ratio | early | <1k bets | 2-0 | 100.0 | 74.3 | 217.0 | 0.3 |
| money_delta+pin_value | early | <1k bets | 1-0 | 100.0 | 48.9 | 90.9 | -1.0 |
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
| money_delta+money_level | early | pin $1-2k | 0-1 | 0.0 | -52.0 | -100.0 | 1.0 |
| money_delta+money_moving | early | pin $1-2k | 0-2 | 0.0 | -38.8 | -100.0 | 2.5 |
| money_delta+pin_value | early | pin $1-2k | 0-1 | 0.0 | -52.0 | -100.0 | 1.0 |
| money_delta+sharp_gap | early | pin $1-2k | 0-2 | 0.0 | -38.8 | -100.0 | 2.5 |
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
| consensus_gap+pin_move | early | pin $1-2k | 0-2 | 0.0 | -25.7 | -100.0 | -0.15 |
| money_moving+pin_rlm | early | pin $1-2k | 0-1 | 0.0 | -25.7 | -100.0 | 1.3 |
| money_level+money_moving | early | pin limit <$1k | 13-7 | 65.0 | 12.5 | 20.2 | 0.48 |
| money_level+sharp_gap | early | pin limit <$1k | 20-16 | 55.6 | 4.8 | 1.6 | 0.14 |
| money_moving+sharp_gap | early | pin limit <$1k | 18-5 | 78.3 | 30.2 | 70.1 | 0.35 |
| book_lag+pin_move | early | pin limit <$1k | 0-1 | 0.0 | -48.9 | -100.0 | -1.0 |
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
| consensus_gap+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.5 | 85.1 | 0.0 |
| consensus_gap+money_moving | early | pin limit <$1k | 7-3 | 70.0 | 22.9 | 72.3 | 0.54 |
| follow_move+money_delta | early | pin limit <$1k | 2-0 | 100.0 | 51.5 | 85.1 | 0.0 |
| follow_move+money_moving | early | pin limit <$1k | 9-3 | 75.0 | 25.4 | 43.3 | 0.33 |
| money_delta+money_moving | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_delta+pin_value | early | pin limit <$1k | 3-0 | 100.0 | 50.7 | 87.1 | -0.33 |
| money_moving+rlm_ratio | early | pin limit <$1k | 3-1 | 75.0 | 25.0 | 45.3 | -0.5 |
| money_delta+sharp_gap | early | pin limit <$1k | 2-0 | 100.0 | 50.0 | 88.9 | -0.5 |
| pin_move+pin_value | early | pin limit <$1k | 1-4 | 20.0 | -29.0 | -61.8 | 0.2 |
| follow_move+pin_move | early | pin limit <$1k | 5-3 | 62.5 | 9.9 | 11.2 | 0.42 |
| consensus_gap+pin_move | early | pin limit <$1k | 0-3 | 0.0 | -56.8 | -100.0 | 0.53 |
| money_level+pin_move | early | pin limit <$1k | 2-2 | 50.0 | -5.8 | -21.8 | 0.1 |
| book_lag+consensus_gap | early | pin limit <$1k | 0-1 | 0.0 | -51.1 | -100.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$1k | 0-1 | 0.0 | -51.1 | -100.0 | 1.0 |
| pin_move+sharp_gap | early | pin limit <$1k | 2-1 | 66.7 | 17.0 | 4.3 | -0.07 |
| follow_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| money_level+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| pin_move+pin_rlm | early | pin limit <$1k | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| pin_move+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| pin_rlm+rlm_ratio | early | pin limit <$1k | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| pin_rlm+sharp_gap | early | pin limit <$1k | 1-0 | 100.0 | 74.3 | 92.6 | 0.5 |
| money_delta+money_level | early | pin limit <$1k | 1-0 | 100.0 | 48.9 | 90.9 | -1.0 |
