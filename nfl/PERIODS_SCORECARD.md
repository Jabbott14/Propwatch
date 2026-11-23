# NFL period scorecard — halves, quarters, team totals

Generated 2026-11-23 01:57 UTC. 439 graded period markets.

## Read this first: fit vs forward

**328 markets before 2026-11-17 (fit) · 111 on or after it (forward).** Every signal and threshold here was chosen by looking at the
fit markets, so a label there is a **hypothesis**; only the forward table is
**evidence**. Base rates are measured separately in each period.

Action Network serves no periods, so these lines come from the FanDuel event
feed and Pinnacle's `s;1;*` keys. **There are no tickets/money splits on any
period market**, so every signal here is handicap or price. Pinnacle's `s;3;*`
keys are excluded: tested against realised quarter scores they fit Q1 and Q3
about equally, so quarters are graded off FanDuel alone rather than guessed.
Everything settles from the boxscore linescore.

Base rates on this sample:

- **spread**: default side won 51.8% (n=85)
- **total**: default side won 45.9% (n=111)
- **ml**: default side won 70.9% (n=103)
- **tt**: default side won 51.2% (n=129)

Proposals appear at 40 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 8-7 | 53.3 | 48.2 | 5.2 | -0.14 | -1.0 | 0.27 | keep collecting (15/40) |
| pin_price | 1-4 | 20.0 | 40.2 | -20.2 | -2.94 | -58.8 | 0.12 | keep collecting (5/40) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 9-15 | 37.5 | 47.7 | -10.2 | -7.6 | -31.7 |  | keep collecting (24/40) |
| pin_price | 1-8 | 11.1 | 33.7 | -22.5 | -6.54 | -72.7 |  | keep collecting (9/40) |
| pin_lead | 0-1 | 0.0 | 63.6 | -63.6 | -1.0 | -100.0 |  | keep collecting (1/40) |
| follow_move | 45-30-1 | 60.0 | 49.1 | 10.9 | +8.4 | 11.0 |  | no edge shown yet |
| fd_juice | 17-10 | 63.0 | 50.6 | 12.3 | +4.59 | 17.0 |  | keep collecting (27/40) |
| follow_move+pin_value | 1-2 | 33.3 | 39.8 | -6.5 | -1.2 | -40.0 |  | keep collecting (3/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 50.0 | 50.0 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move+pin_price | 1-1 | 50.0 | 20.6 | 29.4 | +0.46 | 23.0 |  | keep collecting (2/40) |

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
| pin_value | 32-29 | 52.5 | 49.9 | 2.6 | -1.67 | -2.7 | 0.08 | no edge shown yet |
| pin_price | 5-12 | 29.4 | 43.7 | -14.3 | -5.81 | -34.2 | 0.21 | keep collecting (17/40) |
| follow_move | 19-19-1 | 50.0 | 47.6 | 2.4 | -1.51 | -3.9 | -0.25 | keep collecting (38/40) |
| fd_juice | 9-5 | 64.3 | 49.0 | 15.2 | +2.69 | 19.2 | 0.29 | keep collecting (14/40) |
| follow_move+pin_price | 0-2 | 0.0 | 29.1 | -29.1 | -2.0 | -100.0 | -0.35 | keep collecting (2/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 48.8 | 51.2 | +0.62 | 61.7 | 1.0 | keep collecting (1/40) |
| fd_juice+pin_price | 1-0 | 100.0 | 48.8 | 51.2 | +1.0 | 100.0 | 2.0 | keep collecting (1/40) |
| follow_move+pin_value | 0-1 | 0.0 | 51.2 | -51.2 | -1.0 | -100.0 | 1.0 | keep collecting (1/40) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 62-62 | 50.0 | 49.9 | 0.1 | -10.06 | -8.1 |  | no edge shown yet |
| pin_price | 6-20 | 23.1 | 40.2 | -17.1 | -13.42 | -51.6 |  | keep collecting (26/40) |
| pin_lead | 1-1 | 50.0 | 50.0 | 0.0 | -0.2 | -10.0 |  | keep collecting (2/40) |
| follow_move | 136-117-11 | 53.8 | 49.6 | 4.2 | +2.43 | 0.9 |  | no edge shown yet |
| fd_juice | 54-50 | 51.9 | 49.9 | 2.0 | -4.02 | -3.9 |  | no edge shown yet |
| follow_move+pin_price | 1-5 | 16.7 | 29.1 | -12.5 | -3.54 | -59.0 |  | keep collecting (6/40) |
| pin_lead+pin_value | 1-0 | 100.0 | 48.2 | 51.8 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move+pin_value | 2-3 | 40.0 | 48.5 | -8.5 | -1.27 | -25.5 |  | keep collecting (5/40) |
| fd_juice+pin_price | 0-1 | 0.0 | 45.9 | -45.9 | -1.0 | -100.0 |  | keep collecting (1/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 45.9 | 54.1 | +0.8 | 80.0 |  | keep collecting (1/40) |

## By period, market and Pinnacle limit (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 62-62 | 50.0 | 0.1 | -8.1 |
| pin_value | close | 1h\|spread | 16-22 | 42.1 | -7.5 | -24.3 |
| pin_value | close | 1h\|total | 20-19 | 51.3 | 1.2 | -3.6 |
| pin_value | close | 1h\|tt | 26-21 | 55.3 | 5.4 | 1.2 |
| pin_value | close | pin $20k+ | 10-18 | 35.7 | -14.1 | -36.8 |
| pin_value | close | pin $5-20k | 20-19 | 51.3 | 1.4 | -4.8 |
| pin_value | close | pin <$5k | 32-25 | 56.1 | 6.2 | 3.7 |
| pin_price | close | 1h | 6-20 | 23.1 | -17.1 | -51.6 |
| pin_price | close | 1h\|ml | 1-13 | 7.1 | -25.0 | -82.4 |
| pin_price | close | 1h\|spread | 0-1 | 0.0 | -51.8 | -100.0 |
| pin_price | close | 1h\|total | 2-1 | 66.7 | 18.0 | 24.7 |
| pin_price | close | 1h\|tt | 3-5 | 37.5 | -12.2 | -20.2 |
| pin_price | close | pin $20k+ | 0-1 | 0.0 | -51.8 | -100.0 |
| pin_price | close | pin $5-20k | 3-14 | 17.6 | -17.4 | -63.5 |
| pin_price | close | pin <$5k | 3-5 | 37.5 | -12.2 | -20.2 |
| pin_lead | close | 1h | 1-1 | 50.0 | 0.0 | -10.0 |
| pin_lead | close | 1h\|spread | 1-1 | 50.0 | 0.0 | -10.0 |
| pin_lead | close | pin $20k+ | 1-0 | 100.0 | 51.8 | 80.0 |
| pin_lead | close | pin $5-20k | 0-1 | 0.0 | -51.8 | -100.0 |
| follow_move | close | 1h | 51-50-1 | 50.5 | 1.1 | -3.3 |
| follow_move | close | 1h\|ml | 20-16-1 | 55.6 | 7.9 | 1.8 |
| follow_move | close | 1h\|spread | 9-7 | 56.2 | 6.2 | 11.9 |
| follow_move | close | 1h\|total | 7-8 | 46.7 | -5.8 | -16.3 |
| follow_move | close | 1h\|tt | 15-19 | 44.1 | -5.5 | -10.3 |
| follow_move | close | 2h | 62-42-2 | 59.6 | 10.2 | 11.5 |
| follow_move | close | 2h\|ml | 18-19-2 | 48.6 | 0.3 | -16.8 |
| follow_move | close | 2h\|spread | 11-4 | 73.3 | 23.0 | 41.1 |
| follow_move | close | 2h\|total | 15-8 | 65.2 | 15.0 | 27.1 |
| follow_move | close | 2h\|tt | 18-11 | 62.1 | 12.2 | 21.8 |
| follow_move | close | pin $20k+ | 9-6 | 60.0 | 7.1 | 10.4 |
| follow_move | close | pin $5-20k | 25-23-1 | 52.1 | 4.3 | -2.8 |
| follow_move | close | pin <$5k | 17-21 | 44.7 | -5.3 | -9.3 |
| follow_move | close | q4 | 23-25-8 | 47.9 | -2.3 | -11.4 |
| follow_move | close | q4\|ml | 12-14-8 | 46.2 | -3.8 | -16.9 |
| follow_move | close | q4\|spread | 1-3 | 25.0 | -25.0 | -54.9 |
| follow_move | close | q4\|total | 10-8 | 55.6 | 5.1 | 8.5 |
| fd_juice | close | 1h | 20-11 | 64.5 | 14.3 | 19.9 |
| fd_juice | close | 1h\|spread | 3-3 | 50.0 | 0.0 | -8.9 |
| fd_juice | close | 1h\|total | 7-5 | 58.3 | 8.3 | 8.9 |
| fd_juice | close | 1h\|tt | 10-3 | 76.9 | 26.5 | 43.2 |
| fd_juice | close | 2h | 24-26 | 48.0 | -1.8 | -11.1 |
| fd_juice | close | 2h\|spread | 5-7 | 41.7 | -8.3 | -21.4 |
| fd_juice | close | 2h\|total | 5-6 | 45.5 | -3.4 | -14.2 |
| fd_juice | close | 2h\|tt | 14-13 | 51.9 | 1.8 | -5.4 |
| fd_juice | close | pin $20k+ | 3-1 | 75.0 | 25.0 | 36.6 |
| fd_juice | close | pin $5-20k | 6-6 | 50.0 | 0.7 | -7.0 |
| fd_juice | close | pin <$5k | 11-4 | 73.3 | 22.4 | 36.9 |
| fd_juice | close | q4 | 10-13 | 43.5 | -6.2 | -20.0 |
| fd_juice | close | q4\|spread | 3-8 | 27.3 | -22.9 | -50.3 |
| fd_juice | close | q4\|total | 7-5 | 58.3 | 9.0 | 7.7 |
| follow_move+pin_price | close | 1h | 1-5 | 16.7 | -12.5 | -59.0 |
| pin_lead+pin_value | close | 1h | 1-0 | 100.0 | 51.8 | 80.0 |
| follow_move+pin_value | close | 1h | 2-3 | 40.0 | -8.5 | -25.5 |
| fd_juice+pin_price | close | 1h | 0-1 | 0.0 | -45.9 | -100.0 |
| fd_juice+pin_value | close | 1h | 1-0 | 100.0 | 54.1 | 80.0 |
| follow_move+pin_price | close | 1h\|ml | 1-5 | 16.7 | -12.5 | -59.0 |
| pin_lead+pin_value | close | 1h\|spread | 1-0 | 100.0 | 51.8 | 80.0 |
| follow_move+pin_value | close | 1h\|spread | 1-2 | 33.3 | -14.9 | -40.0 |
| fd_juice+pin_price | close | 1h\|total | 0-1 | 0.0 | -45.9 | -100.0 |
| fd_juice+pin_value | close | 1h\|total | 1-0 | 100.0 | 54.1 | 80.0 |
| follow_move+pin_value | close | 1h\|tt | 1-1 | 50.0 | 1.2 | -3.7 |
| pin_lead+pin_value | close | pin $20k+ | 1-0 | 100.0 | 51.8 | 80.0 |
| follow_move+pin_value | close | pin $20k+ | 1-1 | 50.0 | 1.8 | -10.0 |
| follow_move+pin_price | close | pin $5-20k | 1-5 | 16.7 | -12.5 | -59.0 |
| fd_juice+pin_price | close | pin $5-20k | 0-1 | 0.0 | -45.9 | -100.0 |
| fd_juice+pin_value | close | pin $5-20k | 1-0 | 100.0 | 54.1 | 80.0 |
| follow_move+pin_value | close | pin $5-20k | 0-1 | 0.0 | -48.2 | -100.0 |
| follow_move+pin_value | close | pin <$5k | 1-1 | 50.0 | 1.2 | -3.7 |
| pin_value | early | 1h | 32-29 | 52.5 | 2.6 | -2.7 |
| pin_value | early | 1h\|spread | 10-9 | 52.6 | 2.9 | -3.7 |
| pin_value | early | 1h\|total | 12-12 | 50.0 | 0.0 | -5.0 |
| pin_value | early | 1h\|tt | 10-8 | 55.6 | 5.7 | 1.2 |
| pin_value | early | pin $20k+ | 0-3 | 0.0 | -50.6 | -100.0 |
| pin_value | early | pin $5-20k | 1-3 | 25.0 | -25.0 | -50.0 |
| pin_value | early | pin <$5k | 31-23 | 57.4 | 7.6 | 6.2 |
| pin_price | early | 1h | 5-12 | 29.4 | -14.3 | -34.2 |
| pin_price | early | 1h\|ml | 1-6 | 14.3 | -20.8 | -56.4 |
| pin_price | early | 1h\|spread | 0-1 | 0.0 | -51.8 | -100.0 |
| pin_price | early | 1h\|total | 1-0 | 100.0 | 54.1 | 110.0 |
| pin_price | early | 1h\|tt | 3-5 | 37.5 | -12.5 | -24.5 |
| pin_price | early | pin $5-20k | 2-0 | 100.0 | 62.5 | 157.5 |
| pin_price | early | pin <$5k | 3-12 | 20.0 | -24.6 | -59.7 |
| follow_move | early | 1h | 7-10 | 41.2 | -7.2 | -25.0 |
| follow_move | early | 1h\|ml | 4-4 | 50.0 | 5.2 | -15.4 |
| follow_move | early | 1h\|total | 1-2 | 33.3 | -20.7 | -36.4 |
| follow_move | early | 1h\|tt | 2-4 | 33.3 | -17.1 | -32.0 |
| follow_move | early | 2h | 9-5 | 64.3 | 15.1 | 28.0 |
| follow_move | early | 2h\|ml | 4-2 | 66.7 | 16.7 | 39.1 |
| follow_move | early | 2h\|total | 3-1 | 75.0 | 29.1 | 45.3 |
| follow_move | early | 2h\|tt | 2-2 | 50.0 | -1.2 | -5.7 |
| follow_move | early | pin <$5k | 7-9 | 43.8 | -5.9 | -20.3 |
| follow_move | early | q4 | 3-4-1 | 42.9 | 0.2 | -15.0 |
| follow_move | early | q4\|ml | 2-2-1 | 50.0 | 10.4 | -4.8 |
| follow_move | early | q4\|spread | 0-1 | 0.0 | -48.2 | -100.0 |
| follow_move | early | q4\|total | 1-1 | 50.0 | 4.1 | 2.0 |
| fd_juice | early | 1h | 4-3 | 57.1 | 7.6 | 5.7 |
| fd_juice | early | 1h\|spread | 2-0 | 100.0 | 50.0 | 89.2 |
| fd_juice | early | 1h\|total | 0-2 | 0.0 | -50.0 | -100.0 |
| fd_juice | early | 1h\|tt | 2-1 | 66.7 | 17.8 | 20.6 |
| fd_juice | early | 2h | 4-2 | 66.7 | 17.6 | 21.8 |
| fd_juice | early | 2h\|spread | 1-1 | 50.0 | 0.0 | -4.5 |
| fd_juice | early | 2h\|total | 2-0 | 100.0 | 54.1 | 81.7 |
| fd_juice | early | 2h\|tt | 1-1 | 50.0 | -1.2 | -11.5 |
| fd_juice | early | pin <$5k | 3-3 | 50.0 | 0.3 | -7.2 |
| fd_juice | early | q4 | 1-0 | 100.0 | 54.1 | 98.0 |
| fd_juice | early | q4\|total | 1-0 | 100.0 | 54.1 | 98.0 |
| follow_move+pin_price | early | 1h | 0-2 | 0.0 | -29.1 | -100.0 |
| fd_juice+pin_value | early | 1h | 1-0 | 100.0 | 51.2 | 61.7 |
| fd_juice+pin_price | early | 1h | 1-0 | 100.0 | 51.2 | 100.0 |
| follow_move+pin_value | early | 1h | 0-1 | 0.0 | -51.2 | -100.0 |
| follow_move+pin_price | early | 1h\|ml | 0-2 | 0.0 | -29.1 | -100.0 |
| fd_juice+pin_value | early | 1h\|tt | 1-0 | 100.0 | 51.2 | 61.7 |
| fd_juice+pin_price | early | 1h\|tt | 1-0 | 100.0 | 51.2 | 100.0 |
| follow_move+pin_value | early | 1h\|tt | 0-1 | 0.0 | -51.2 | -100.0 |
| follow_move+pin_price | early | pin <$5k | 0-2 | 0.0 | -29.1 | -100.0 |
| fd_juice+pin_value | early | pin <$5k | 1-0 | 100.0 | 51.2 | 61.7 |
| fd_juice+pin_price | early | pin <$5k | 1-0 | 100.0 | 51.2 | 100.0 |
| follow_move+pin_value | early | pin <$5k | 0-1 | 0.0 | -51.2 | -100.0 |
