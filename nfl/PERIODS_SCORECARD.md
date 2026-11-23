# NFL period scorecard — halves, quarters, team totals

Generated 2026-11-23 13:36 UTC. 451 graded period markets.

## Read this first: fit vs forward

**328 markets before 2026-11-17 (fit) · 123 on or after it (forward).** Every signal and threshold here was chosen by looking at the
fit markets, so a label there is a **hypothesis**; only the forward table is
**evidence**. Base rates are measured separately in each period.

Action Network serves no periods, so these lines come from the FanDuel event
feed and Pinnacle's `s;1;*` keys. **There are no tickets/money splits on any
period market**, so every signal here is handicap or price. Pinnacle's `s;3;*`
keys are excluded: tested against realised quarter scores they fit Q1 and Q3
about equally, so quarters are graded off FanDuel alone rather than guessed.
Everything settles from the boxscore linescore.

Base rates on this sample:

- **spread**: default side won 52.9% (n=87)
- **total**: default side won 45.6% (n=114)
- **ml**: default side won 71.7% (n=106)
- **tt**: default side won 51.1% (n=133)

Proposals appear at 40 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 11-7 | 61.1 | 49.2 | 11.9 | +2.59 | 14.4 | 0.33 | keep collecting (18/40) |
| pin_price | 2-4 | 33.3 | 46.3 | -13.0 | -2.17 | -36.2 | 0.83 | keep collecting (6/40) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 11-15 | 42.3 | 47.3 | -5.0 | -6.05 | -23.3 |  | keep collecting (26/40) |
| pin_price | 4-8 | 33.3 | 41.3 | -7.9 | -4.11 | -34.2 |  | keep collecting (12/40) |
| pin_lead | 0-1 | 0.0 | 66.7 | -66.7 | -1.0 | -100.0 |  | keep collecting (1/40) |
| follow_move | 53-31-1 | 63.1 | 50.6 | 12.5 | +14.08 | 16.6 |  | PROMOTE: beats break-even and its own base rate |
| fd_juice | 19-11 | 63.3 | 50.6 | 12.7 | +5.44 | 18.1 |  | keep collecting (30/40) |
| follow_move+pin_value | 1-2 | 33.3 | 37.9 | -4.6 | -1.2 | -40.0 |  | keep collecting (3/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 48.1 | 51.9 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move+pin_price | 4-1 | 80.0 | 47.7 | 32.3 | +2.9 | 57.9 |  | keep collecting (5/40) |

# FIT (in-sample — this is the hypothesis)

## EARLY  (fit)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 24-22 | 52.2 | 49.9 | 2.3 | -1.53 | -3.3 | 0.02 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_price | 4-8 | 33.3 | 45.1 | -11.7 | -2.87 | -23.9 | 0.24 | keep collecting (12/40) |
| follow_move | 19-19-1 | 50.0 | 48.0 | 2.0 | -1.51 | -3.9 | -0.25 | keep collecting (38/40) |
| fd_juice | 9-5 | 64.3 | 48.9 | 15.4 | +2.69 | 19.2 | 0.29 | keep collecting (14/40) |
| follow_move+pin_price | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 | -0.35 | keep collecting (2/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 49.5 | 50.5 | +0.62 | 61.7 | 1.0 | keep collecting (1/40) |
| fd_juice+pin_price | 1-0 | 100.0 | 49.5 | 50.5 | +1.0 | 100.0 | 2.0 | keep collecting (1/40) |
| follow_move+pin_value | 0-1 | 0.0 | 50.5 | -50.5 | -1.0 | -100.0 | 1.0 | keep collecting (1/40) |

## CLOSE  (fit)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 53-47 | 53.0 | 50.2 | 2.8 | -2.46 | -2.5 |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_price | 5-12 | 29.4 | 42.6 | -13.2 | -6.88 | -40.4 |  | keep collecting (17/40) |
| pin_lead | 1-0 | 100.0 | 52.4 | 47.6 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move | 91-87-10 | 51.1 | 49.5 | 1.6 | -5.97 | -3.2 |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| fd_juice | 37-40 | 48.1 | 50.0 | -2.0 | -8.61 | -11.2 |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move+pin_price | 0-4 | 0.0 | 33.3 | -33.3 | -4.0 | -100.0 |  | keep collecting (4/40) |
| pin_lead+pin_value | 1-0 | 100.0 | 52.4 | 47.6 | +0.8 | 80.0 |  | redundant -- identical record to pin_lead alone, not independent confirmation |
| follow_move+pin_value | 1-1 | 50.0 | 50.9 | -0.9 | -0.07 | -3.7 |  | keep collecting (2/40) |
| fd_juice+pin_price | 0-1 | 0.0 | 44.8 | -44.8 | -1.0 | -100.0 |  | keep collecting (1/40) |

# Pooled (contaminated — mixes fit and forward)

## EARLY  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 35-29 | 54.7 | 49.8 | 4.9 | +1.06 | 1.7 | 0.11 | no edge shown yet |
| pin_price | 6-12 | 33.3 | 45.1 | -11.8 | -5.04 | -28.0 | 0.44 | keep collecting (18/40) |
| follow_move | 19-19-1 | 50.0 | 47.5 | 2.5 | -1.51 | -3.9 | -0.25 | keep collecting (38/40) |
| fd_juice | 9-5 | 64.3 | 49.0 | 15.3 | +2.69 | 19.2 | 0.29 | keep collecting (14/40) |
| follow_move+pin_price | 0-2 | 0.0 | 28.3 | -28.3 | -2.0 | -100.0 | -0.35 | keep collecting (2/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 48.9 | 51.1 | +0.62 | 61.7 | 1.0 | keep collecting (1/40) |
| fd_juice+pin_price | 1-0 | 100.0 | 48.9 | 51.1 | +1.0 | 100.0 | 2.0 | keep collecting (1/40) |
| follow_move+pin_value | 0-1 | 0.0 | 51.1 | -51.1 | -1.0 | -100.0 | 1.0 | keep collecting (1/40) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 64-62 | 50.8 | 49.8 | 1.0 | -8.51 | -6.8 |  | no edge shown yet |
| pin_price | 9-20 | 31.0 | 41.8 | -10.7 | -10.98 | -37.9 |  | keep collecting (29/40) |
| pin_lead | 1-1 | 50.0 | 50.0 | 0.0 | -0.2 | -10.0 |  | keep collecting (2/40) |
| follow_move | 144-118-11 | 55.0 | 49.9 | 5.1 | +8.11 | 3.0 |  | no edge shown yet |
| fd_juice | 56-51 | 52.3 | 49.9 | 2.4 | -3.17 | -3.0 |  | no edge shown yet |
| follow_move+pin_price | 4-5 | 44.4 | 38.4 | 6.1 | -1.11 | -12.3 |  | keep collecting (9/40) |
| pin_lead+pin_value | 1-0 | 100.0 | 47.1 | 52.9 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move+pin_value | 2-3 | 40.0 | 47.8 | -7.8 | -1.27 | -25.5 |  | keep collecting (5/40) |
| fd_juice+pin_price | 0-1 | 0.0 | 45.6 | -45.6 | -1.0 | -100.0 |  | keep collecting (1/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 45.6 | 54.4 | +0.8 | 80.0 |  | keep collecting (1/40) |

## By period, market and Pinnacle limit (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 64-62 | 50.8 | 1.0 | -6.8 |
| pin_value | close | 1h\|spread | 16-22 | 42.1 | -7.3 | -24.3 |
| pin_value | close | 1h\|total | 21-19 | 52.5 | 2.5 | -1.3 |
| pin_value | close | 1h\|tt | 27-21 | 56.2 | 6.3 | 2.6 |
| pin_value | close | pin $20k+ | 10-18 | 35.7 | -13.9 | -36.8 |
| pin_value | close | pin $5-20k | 21-19 | 52.5 | 2.8 | -2.5 |
| pin_value | close | pin <$5k | 33-25 | 56.9 | 7.0 | 4.8 |
| pin_price | close | 1h | 9-20 | 31.0 | -10.7 | -37.9 |
| pin_price | close | 1h\|ml | 2-13 | 13.3 | -20.8 | -72.7 |
| pin_price | close | 1h\|spread | 1-1 | 50.0 | -2.9 | -4.5 |
| pin_price | close | 1h\|total | 2-1 | 66.7 | 18.1 | 24.7 |
| pin_price | close | 1h\|tt | 4-5 | 44.4 | -5.4 | -8.1 |
| pin_price | close | pin $20k+ | 2-1 | 66.7 | 7.5 | 18.3 |
| pin_price | close | pin $5-20k | 3-14 | 17.6 | -16.8 | -63.5 |
| pin_price | close | pin <$5k | 4-5 | 44.4 | -5.4 | -8.1 |
| pin_lead | close | 1h | 1-1 | 50.0 | 0.0 | -10.0 |
| pin_lead | close | 1h\|spread | 1-1 | 50.0 | 0.0 | -10.0 |
| pin_lead | close | pin $20k+ | 1-0 | 100.0 | 52.9 | 80.0 |
| pin_lead | close | pin $5-20k | 0-1 | 0.0 | -52.9 | -100.0 |
| follow_move | close | 1h | 54-51-1 | 51.4 | 1.8 | -1.8 |
| follow_move | close | 1h\|ml | 21-16-1 | 56.8 | 8.5 | 3.5 |
| follow_move | close | 1h\|spread | 10-7 | 58.8 | 8.7 | 16.6 |
| follow_move | close | 1h\|total | 7-8 | 46.7 | -6.0 | -16.3 |
| follow_move | close | 1h\|tt | 16-20 | 44.4 | -5.2 | -10.1 |
| follow_move | close | 2h | 65-42-2 | 60.7 | 11.0 | 13.5 |
| follow_move | close | 2h\|ml | 19-19-2 | 50.0 | 1.1 | -15.0 |
| follow_move | close | 2h\|spread | 11-4 | 73.3 | 22.8 | 41.1 |
| follow_move | close | 2h\|total | 16-8 | 66.7 | 16.3 | 29.7 |
| follow_move | close | 2h\|tt | 19-11 | 63.3 | 13.5 | 24.6 |
| follow_move | close | pin $20k+ | 11-6 | 64.7 | 10.5 | 18.3 |
| follow_move | close | pin $5-20k | 25-23-1 | 52.1 | 4.4 | -2.8 |
| follow_move | close | pin <$5k | 18-22 | 45.0 | -5.1 | -9.2 |
| follow_move | close | q4 | 25-25-8 | 50.0 | -0.7 | -8.0 |
| follow_move | close | q4\|ml | 13-14-8 | 48.1 | -2.7 | -14.4 |
| follow_move | close | q4\|spread | 1-3 | 25.0 | -25.0 | -54.9 |
| follow_move | close | q4\|total | 11-8 | 57.9 | 7.2 | 13.5 |
| fd_juice | close | 1h | 20-12 | 62.5 | 12.2 | 16.1 |
| fd_juice | close | 1h\|spread | 3-3 | 50.0 | 0.0 | -8.9 |
| fd_juice | close | 1h\|total | 7-6 | 53.8 | 3.5 | 0.5 |
| fd_juice | close | 1h\|tt | 10-3 | 76.9 | 26.5 | 43.2 |
| fd_juice | close | 2h | 26-26 | 50.0 | 0.2 | -7.2 |
| fd_juice | close | 2h\|spread | 6-7 | 46.2 | -4.1 | -13.3 |
| fd_juice | close | 2h\|total | 5-6 | 45.5 | -3.3 | -14.2 |
| fd_juice | close | 2h\|tt | 15-13 | 53.6 | 3.6 | -1.5 |
| fd_juice | close | pin $20k+ | 3-1 | 75.0 | 25.0 | 36.6 |
| fd_juice | close | pin $5-20k | 6-7 | 46.2 | -3.5 | -14.2 |
| fd_juice | close | pin <$5k | 11-4 | 73.3 | 22.4 | 36.9 |
| fd_juice | close | q4 | 10-13 | 43.5 | -6.3 | -20.0 |
| fd_juice | close | q4\|spread | 3-8 | 27.3 | -23.0 | -50.3 |
| fd_juice | close | q4\|total | 7-5 | 58.3 | 9.1 | 7.7 |
| follow_move+pin_price | close | 1h | 4-5 | 44.4 | 6.1 | -12.3 |
| pin_lead+pin_value | close | 1h | 1-0 | 100.0 | 52.9 | 80.0 |
| follow_move+pin_value | close | 1h | 2-3 | 40.0 | -7.8 | -25.5 |
| fd_juice+pin_price | close | 1h | 0-1 | 0.0 | -45.6 | -100.0 |
| fd_juice+pin_value | close | 1h | 1-0 | 100.0 | 54.4 | 80.0 |
| follow_move+pin_price | close | 1h\|ml | 2-5 | 28.6 | -5.9 | -41.4 |
| pin_lead+pin_value | close | 1h\|spread | 1-0 | 100.0 | 52.9 | 80.0 |
| follow_move+pin_value | close | 1h\|spread | 1-2 | 33.3 | -13.8 | -40.0 |
| follow_move+pin_price | close | 1h\|spread | 1-0 | 100.0 | 47.1 | 90.9 |
| fd_juice+pin_price | close | 1h\|total | 0-1 | 0.0 | -45.6 | -100.0 |
| fd_juice+pin_value | close | 1h\|total | 1-0 | 100.0 | 54.4 | 80.0 |
| follow_move+pin_value | close | 1h\|tt | 1-1 | 50.0 | 1.1 | -3.7 |
| follow_move+pin_price | close | 1h\|tt | 1-0 | 100.0 | 48.9 | 88.5 |
| pin_lead+pin_value | close | pin $20k+ | 1-0 | 100.0 | 52.9 | 80.0 |
| follow_move+pin_value | close | pin $20k+ | 1-1 | 50.0 | 2.9 | -10.0 |
| follow_move+pin_price | close | pin $20k+ | 2-0 | 100.0 | 37.7 | 77.5 |
| follow_move+pin_price | close | pin $5-20k | 1-5 | 16.7 | -11.6 | -59.0 |
| fd_juice+pin_price | close | pin $5-20k | 0-1 | 0.0 | -45.6 | -100.0 |
| fd_juice+pin_value | close | pin $5-20k | 1-0 | 100.0 | 54.4 | 80.0 |
| follow_move+pin_value | close | pin $5-20k | 0-1 | 0.0 | -47.1 | -100.0 |
| follow_move+pin_value | close | pin <$5k | 1-1 | 50.0 | 1.1 | -3.7 |
| follow_move+pin_price | close | pin <$5k | 1-0 | 100.0 | 48.9 | 88.5 |
| pin_value | early | 1h | 35-29 | 54.7 | 4.9 | 1.7 |
| pin_value | early | 1h\|spread | 11-9 | 55.0 | 5.3 | 1.8 |
| pin_value | early | 1h\|total | 13-12 | 52.0 | 2.2 | -1.6 |
| pin_value | early | 1h\|tt | 11-8 | 57.9 | 8.0 | 5.8 |
| pin_value | early | pin $20k+ | 0-3 | 0.0 | -51.0 | -100.0 |
| pin_value | early | pin $5-20k | 2-3 | 40.0 | -10.6 | -19.0 |
| pin_value | early | pin <$5k | 33-23 | 58.9 | 9.2 | 9.0 |
| pin_price | early | 1h | 6-12 | 33.3 | -11.8 | -28.0 |
| pin_price | early | 1h\|ml | 2-6 | 25.0 | -14.2 | -39.8 |
| pin_price | early | 1h\|spread | 0-1 | 0.0 | -52.9 | -100.0 |
| pin_price | early | 1h\|total | 1-0 | 100.0 | 54.4 | 110.0 |
| pin_price | early | 1h\|tt | 3-5 | 37.5 | -12.5 | -24.5 |
| pin_price | early | pin $5-20k | 3-0 | 100.0 | 51.5 | 130.6 |
| pin_price | early | pin <$5k | 3-12 | 20.0 | -24.4 | -59.7 |
| follow_move | early | 1h | 7-10 | 41.2 | -7.2 | -25.0 |
| follow_move | early | 1h\|ml | 4-4 | 50.0 | 5.4 | -15.4 |
| follow_move | early | 1h\|total | 1-2 | 33.3 | -21.1 | -36.4 |
| follow_move | early | 1h\|tt | 2-4 | 33.3 | -17.0 | -32.0 |
| follow_move | early | 2h | 9-5 | 64.3 | 15.2 | 28.0 |
| follow_move | early | 2h\|ml | 4-2 | 66.7 | 16.7 | 39.1 |
| follow_move | early | 2h\|total | 3-1 | 75.0 | 29.4 | 45.3 |
| follow_move | early | 2h\|tt | 2-2 | 50.0 | -1.1 | -5.7 |
| follow_move | early | pin <$5k | 7-9 | 43.8 | -5.9 | -20.3 |
| follow_move | early | q4 | 3-4-1 | 42.9 | 0.7 | -15.0 |
| follow_move | early | q4\|ml | 2-2-1 | 50.0 | 10.8 | -4.8 |
| follow_move | early | q4\|spread | 0-1 | 0.0 | -47.1 | -100.0 |
| follow_move | early | q4\|total | 1-1 | 50.0 | 4.4 | 2.0 |
| fd_juice | early | 1h | 4-3 | 57.1 | 7.6 | 5.7 |
| fd_juice | early | 1h\|spread | 2-0 | 100.0 | 50.0 | 89.2 |
| fd_juice | early | 1h\|total | 0-2 | 0.0 | -50.0 | -100.0 |
| fd_juice | early | 1h\|tt | 2-1 | 66.7 | 17.8 | 20.6 |
| fd_juice | early | 2h | 4-2 | 66.7 | 17.8 | 21.8 |
| fd_juice | early | 2h\|spread | 1-1 | 50.0 | 0.0 | -4.5 |
| fd_juice | early | 2h\|total | 2-0 | 100.0 | 54.4 | 81.7 |
| fd_juice | early | 2h\|tt | 1-1 | 50.0 | -1.1 | -11.5 |
| fd_juice | early | pin <$5k | 3-3 | 50.0 | 0.1 | -7.2 |
| fd_juice | early | q4 | 1-0 | 100.0 | 54.4 | 98.0 |
| fd_juice | early | q4\|total | 1-0 | 100.0 | 54.4 | 98.0 |
| follow_move+pin_price | early | 1h | 0-2 | 0.0 | -28.3 | -100.0 |
| fd_juice+pin_value | early | 1h | 1-0 | 100.0 | 51.1 | 61.7 |
| fd_juice+pin_price | early | 1h | 1-0 | 100.0 | 51.1 | 100.0 |
| follow_move+pin_value | early | 1h | 0-1 | 0.0 | -51.1 | -100.0 |
| follow_move+pin_price | early | 1h\|ml | 0-2 | 0.0 | -28.3 | -100.0 |
| fd_juice+pin_value | early | 1h\|tt | 1-0 | 100.0 | 51.1 | 61.7 |
| fd_juice+pin_price | early | 1h\|tt | 1-0 | 100.0 | 51.1 | 100.0 |
| follow_move+pin_value | early | 1h\|tt | 0-1 | 0.0 | -51.1 | -100.0 |
| follow_move+pin_price | early | pin <$5k | 0-2 | 0.0 | -28.3 | -100.0 |
| fd_juice+pin_value | early | pin <$5k | 1-0 | 100.0 | 51.1 | 61.7 |
| fd_juice+pin_price | early | pin <$5k | 1-0 | 100.0 | 51.1 | 100.0 |
| follow_move+pin_value | early | pin <$5k | 0-1 | 0.0 | -51.1 | -100.0 |
