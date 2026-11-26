# NFL period scorecard — halves, quarters, team totals

Generated 2026-11-26 17:17 UTC. 468 graded period markets.

## Read this first: fit vs forward

**328 markets before 2026-11-17 (fit) · 140 on or after it (forward).** Every signal and threshold here was chosen by looking at the
fit markets, so a label there is a **hypothesis**; only the forward table is
**evidence**. Base rates are measured separately in each period.

Action Network serves no periods, so these lines come from the FanDuel event
feed and Pinnacle's `s;1;*` keys. **There are no tickets/money splits on any
period market**, so every signal here is handicap or price. Pinnacle's `s;3;*`
keys are excluded: tested against realised quarter scores they fit Q1 and Q3
about equally, so quarters are graded off FanDuel alone rather than guessed.
Everything settles from the boxscore linescore.

Base rates on this sample:

- **spread**: default side won 51.7% (n=89)
- **total**: default side won 44.5% (n=119)
- **ml**: default side won 70.9% (n=110)
- **tt**: default side won 50.7% (n=138)

Proposals appear at 40 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 11-9 | 55.0 | 49.5 | 5.5 | +0.59 | 3.0 | 0.4 | keep collecting (20/40) |
| pin_price | 2-5 | 28.6 | 46.4 | -17.8 | -3.17 | -45.3 | 0.86 | keep collecting (7/40) |
| pin_lead | 0-1 | 0.0 | 56.2 | -56.2 | -1.0 | -100.0 | 2.0 | keep collecting (1/40) |
| follow_move | 2-0 | 100.0 | 60.9 | 39.1 | +1.8 | 89.8 | -1.55 | keep collecting (2/40) |
| pin_lead+pin_value | 0-1 | 0.0 | 56.2 | -56.2 | -1.0 | -100.0 | 2.0 | redundant -- identical record to pin_lead alone, not independent confirmation |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 16-16 | 50.0 | 47.3 | 2.7 | -2.71 | -8.5 |  | keep collecting (32/40) |
| pin_price | 4-9 | 30.8 | 40.2 | -9.4 | -5.11 | -39.3 |  | keep collecting (13/40) |
| pin_lead | 0-1 | 0.0 | 61.5 | -61.5 | -1.0 | -100.0 |  | keep collecting (1/40) |
| follow_move | 54-40-2 | 57.4 | 51.7 | 5.7 | +5.49 | 5.7 |  | no edge shown yet |
| fd_juice | 20-15 | 57.1 | 50.0 | 7.2 | +2.28 | 6.5 |  | keep collecting (35/40) |
| follow_move+pin_value | 1-2 | 33.3 | 41.9 | -8.5 | -1.2 | -40.0 |  | keep collecting (3/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 43.8 | 56.2 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move+pin_price | 4-1 | 80.0 | 47.0 | 33.0 | +2.9 | 57.9 |  | keep collecting (5/40) |

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
| pin_value | 35-31 | 53.0 | 49.9 | 3.2 | -0.94 | -1.4 | 0.14 | no edge shown yet |
| pin_price | 6-13 | 31.6 | 45.4 | -13.8 | -6.04 | -31.8 | 0.47 | keep collecting (19/40) |
| pin_lead | 0-1 | 0.0 | 55.5 | -55.5 | -1.0 | -100.0 | 2.0 | keep collecting (1/40) |
| follow_move | 21-19-1 | 52.5 | 48.0 | 4.5 | +0.28 | 0.7 | -0.31 | no edge shown yet |
| fd_juice | 9-5 | 64.3 | 48.8 | 15.5 | +2.69 | 19.2 | 0.29 | keep collecting (14/40) |
| follow_move+pin_price | 0-2 | 0.0 | 29.1 | -29.1 | -2.0 | -100.0 | -0.35 | keep collecting (2/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 49.3 | 50.7 | +0.62 | 61.7 | 1.0 | keep collecting (1/40) |
| fd_juice+pin_price | 1-0 | 100.0 | 49.3 | 50.7 | +1.0 | 100.0 | 2.0 | keep collecting (1/40) |
| follow_move+pin_value | 0-1 | 0.0 | 50.7 | -50.7 | -1.0 | -100.0 | 1.0 | keep collecting (1/40) |
| pin_lead+pin_value | 0-1 | 0.0 | 55.5 | -55.5 | -1.0 | -100.0 | 2.0 | redundant -- identical record to pin_lead alone, not independent confirmation |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 69-63 | 52.3 | 49.8 | 2.5 | -5.17 | -3.9 |  | no edge shown yet |
| pin_price | 9-21 | 30.0 | 41.5 | -11.5 | -11.98 | -39.9 |  | keep collecting (30/40) |
| pin_lead | 1-1 | 50.0 | 50.0 | 0.0 | -0.2 | -10.0 |  | keep collecting (2/40) |
| follow_move | 145-127-12 | 53.3 | 50.1 | 3.2 | -0.49 | -0.2 |  | no edge shown yet |
| fd_juice | 57-55 | 50.9 | 49.9 | 1.0 | -6.34 | -5.7 |  | no edge shown yet |
| follow_move+pin_price | 4-5 | 44.4 | 38.7 | 5.8 | -1.11 | -12.3 |  | keep collecting (9/40) |
| pin_lead+pin_value | 1-0 | 100.0 | 48.3 | 51.7 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move+pin_value | 2-3 | 40.0 | 48.7 | -8.7 | -1.27 | -25.5 |  | keep collecting (5/40) |
| fd_juice+pin_price | 0-1 | 0.0 | 44.5 | -44.5 | -1.0 | -100.0 |  | keep collecting (1/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 44.5 | 55.5 | +0.8 | 80.0 |  | keep collecting (1/40) |

## By period, market and Pinnacle limit (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 69-63 | 52.3 | 2.5 | -3.9 |
| pin_value | close | 1h\|spread | 17-22 | 43.6 | -6.0 | -21.6 |
| pin_value | close | 1h\|total | 22-20 | 52.4 | 2.6 | -1.5 |
| pin_value | close | 1h\|tt | 30-21 | 58.8 | 8.9 | 7.6 |
| pin_value | close | pin $20k+ | 11-18 | 37.9 | -11.9 | -32.7 |
| pin_value | close | pin $5-20k | 23-20 | 53.5 | 4.0 | -0.3 |
| pin_value | close | pin <$5k | 35-25 | 58.3 | 8.4 | 7.4 |
| pin_price | close | 1h | 9-21 | 30.0 | -11.5 | -39.9 |
| pin_price | close | 1h\|ml | 2-14 | 12.5 | -21.8 | -74.4 |
| pin_price | close | 1h\|spread | 1-1 | 50.0 | -1.7 | -4.5 |
| pin_price | close | 1h\|total | 2-1 | 66.7 | 18.5 | 24.7 |
| pin_price | close | 1h\|tt | 4-5 | 44.4 | -5.5 | -8.1 |
| pin_price | close | pin $20k+ | 2-2 | 50.0 | -0.8 | -11.2 |
| pin_price | close | pin $5-20k | 3-14 | 17.6 | -17.3 | -63.5 |
| pin_price | close | pin <$5k | 4-5 | 44.4 | -5.5 | -8.1 |
| pin_lead | close | 1h | 1-1 | 50.0 | 0.0 | -10.0 |
| pin_lead | close | 1h\|spread | 1-1 | 50.0 | 0.0 | -10.0 |
| pin_lead | close | pin $20k+ | 1-0 | 100.0 | 51.7 | 80.0 |
| pin_lead | close | pin $5-20k | 0-1 | 0.0 | -51.7 | -100.0 |
| follow_move | close | 1h | 55-56-2 | 49.5 | -0.5 | -5.8 |
| follow_move | close | 1h\|ml | 22-16-2 | 57.9 | 9.0 | 4.3 |
| follow_move | close | 1h\|spread | 10-8 | 55.6 | 5.4 | 10.1 |
| follow_move | close | 1h\|total | 7-9 | 43.8 | -9.7 | -21.5 |
| follow_move | close | 1h\|tt | 16-23 | 41.0 | -8.7 | -17.0 |
| follow_move | close | 2h | 65-44-2 | 59.6 | 9.9 | 11.4 |
| follow_move | close | 2h\|ml | 19-21-2 | 47.5 | -1.5 | -19.0 |
| follow_move | close | 2h\|spread | 11-4 | 73.3 | 23.0 | 41.1 |
| follow_move | close | 2h\|total | 16-8 | 66.7 | 16.2 | 29.7 |
| follow_move | close | 2h\|tt | 19-11 | 63.3 | 13.4 | 24.6 |
| follow_move | close | pin $20k+ | 12-7-1 | 63.2 | 8.5 | 12.6 |
| follow_move | close | pin $5-20k | 25-25-1 | 50.0 | 1.9 | -6.6 |
| follow_move | close | pin <$5k | 18-24 | 42.9 | -7.4 | -13.5 |
| follow_move | close | q4 | 25-27-8 | 48.1 | -2.9 | -11.1 |
| follow_move | close | q4\|ml | 13-15-8 | 46.4 | -5.1 | -16.8 |
| follow_move | close | q4\|spread | 1-3 | 25.0 | -25.0 | -54.9 |
| follow_move | close | q4\|total | 11-9 | 55.0 | 4.5 | 7.9 |
| fd_juice | close | 1h | 20-13 | 60.6 | 10.3 | 12.6 |
| fd_juice | close | 1h\|spread | 3-3 | 50.0 | 0.0 | -8.9 |
| fd_juice | close | 1h\|total | 7-6 | 53.8 | 3.4 | 0.5 |
| fd_juice | close | 1h\|tt | 10-4 | 71.4 | 21.1 | 33.0 |
| fd_juice | close | 2h | 27-29 | 48.2 | -1.6 | -10.5 |
| fd_juice | close | 2h\|spread | 6-8 | 42.9 | -7.4 | -19.5 |
| fd_juice | close | 2h\|total | 6-7 | 46.2 | -2.6 | -13.3 |
| fd_juice | close | 2h\|tt | 15-14 | 51.7 | 1.7 | -4.9 |
| fd_juice | close | pin $20k+ | 3-1 | 75.0 | 25.0 | 36.6 |
| fd_juice | close | pin $5-20k | 6-8 | 42.9 | -6.8 | -20.3 |
| fd_juice | close | pin <$5k | 11-4 | 73.3 | 22.4 | 36.9 |
| fd_juice | close | q4 | 10-13 | 43.5 | -6.1 | -20.0 |
| fd_juice | close | q4\|spread | 3-8 | 27.3 | -22.9 | -50.3 |
| fd_juice | close | q4\|total | 7-5 | 58.3 | 9.2 | 7.7 |
| follow_move+pin_price | close | 1h | 4-5 | 44.4 | 5.8 | -12.3 |
| pin_lead+pin_value | close | 1h | 1-0 | 100.0 | 51.7 | 80.0 |
| follow_move+pin_value | close | 1h | 2-3 | 40.0 | -8.7 | -25.5 |
| fd_juice+pin_price | close | 1h | 0-1 | 0.0 | -44.5 | -100.0 |
| fd_juice+pin_value | close | 1h | 1-0 | 100.0 | 55.5 | 80.0 |
| follow_move+pin_price | close | 1h\|ml | 2-5 | 28.6 | -6.5 | -41.4 |
| pin_lead+pin_value | close | 1h\|spread | 1-0 | 100.0 | 51.7 | 80.0 |
| follow_move+pin_value | close | 1h\|spread | 1-2 | 33.3 | -15.0 | -40.0 |
| follow_move+pin_price | close | 1h\|spread | 1-0 | 100.0 | 48.3 | 90.9 |
| fd_juice+pin_price | close | 1h\|total | 0-1 | 0.0 | -44.5 | -100.0 |
| fd_juice+pin_value | close | 1h\|total | 1-0 | 100.0 | 55.5 | 80.0 |
| follow_move+pin_value | close | 1h\|tt | 1-1 | 50.0 | 0.7 | -3.7 |
| follow_move+pin_price | close | 1h\|tt | 1-0 | 100.0 | 49.3 | 88.5 |
| pin_lead+pin_value | close | pin $20k+ | 1-0 | 100.0 | 51.7 | 80.0 |
| follow_move+pin_value | close | pin $20k+ | 1-1 | 50.0 | 1.7 | -10.0 |
| follow_move+pin_price | close | pin $20k+ | 2-0 | 100.0 | 38.7 | 77.5 |
| follow_move+pin_price | close | pin $5-20k | 1-5 | 16.7 | -12.4 | -59.0 |
| fd_juice+pin_price | close | pin $5-20k | 0-1 | 0.0 | -44.5 | -100.0 |
| fd_juice+pin_value | close | pin $5-20k | 1-0 | 100.0 | 55.5 | 80.0 |
| follow_move+pin_value | close | pin $5-20k | 0-1 | 0.0 | -48.3 | -100.0 |
| follow_move+pin_value | close | pin <$5k | 1-1 | 50.0 | 0.7 | -3.7 |
| follow_move+pin_price | close | pin <$5k | 1-0 | 100.0 | 49.3 | 88.5 |
| pin_value | early | 1h | 35-31 | 53.0 | 3.2 | -1.4 |
| pin_value | early | 1h\|spread | 11-9 | 55.0 | 5.2 | 1.8 |
| pin_value | early | 1h\|total | 13-14 | 48.1 | -1.6 | -8.9 |
| pin_value | early | 1h\|tt | 11-8 | 57.9 | 7.9 | 5.8 |
| pin_value | early | pin $20k+ | 0-3 | 0.0 | -50.6 | -100.0 |
| pin_value | early | pin $5-20k | 2-3 | 40.0 | -10.3 | -19.0 |
| pin_value | early | pin <$5k | 33-25 | 56.9 | 7.1 | 5.2 |
| pin_price | early | 1h | 6-13 | 31.6 | -13.8 | -31.8 |
| pin_price | early | 1h\|ml | 2-6 | 25.0 | -14.5 | -39.8 |
| pin_price | early | 1h\|spread | 0-1 | 0.0 | -51.7 | -100.0 |
| pin_price | early | 1h\|total | 1-0 | 100.0 | 55.5 | 110.0 |
| pin_price | early | 1h\|tt | 3-6 | 33.3 | -16.6 | -32.9 |
| pin_price | early | pin $5-20k | 3-0 | 100.0 | 51.8 | 130.6 |
| pin_price | early | pin <$5k | 3-13 | 18.8 | -26.1 | -62.2 |
| pin_lead | early | 1h | 0-1 | 0.0 | -55.5 | -100.0 |
| pin_lead | early | 1h\|total | 0-1 | 0.0 | -55.5 | -100.0 |
| pin_lead | early | pin <$5k | 0-1 | 0.0 | -55.5 | -100.0 |
| follow_move | early | 1h | 8-10 | 44.4 | -3.9 | -17.7 |
| follow_move | early | 1h\|ml | 4-4 | 50.0 | 5.2 | -15.4 |
| follow_move | early | 1h\|total | 2-2 | 50.0 | -2.7 | -1.0 |
| follow_move | early | 1h\|tt | 2-4 | 33.3 | -16.9 | -32.0 |
| follow_move | early | 2h | 10-5 | 66.7 | 16.5 | 31.2 |
| follow_move | early | 2h\|ml | 5-2 | 71.4 | 18.4 | 44.1 |
| follow_move | early | 2h\|total | 3-1 | 75.0 | 30.5 | 45.3 |
| follow_move | early | 2h\|tt | 2-2 | 50.0 | -0.7 | -5.7 |
| follow_move | early | pin <$5k | 8-9 | 47.1 | -2.4 | -12.9 |
| follow_move | early | q4 | 3-4-1 | 42.9 | 0.6 | -15.0 |
| follow_move | early | q4\|ml | 2-2-1 | 50.0 | 10.5 | -4.8 |
| follow_move | early | q4\|spread | 0-1 | 0.0 | -48.3 | -100.0 |
| follow_move | early | q4\|total | 1-1 | 50.0 | 5.5 | 2.0 |
| fd_juice | early | 1h | 4-3 | 57.1 | 7.5 | 5.7 |
| fd_juice | early | 1h\|spread | 2-0 | 100.0 | 50.0 | 89.2 |
| fd_juice | early | 1h\|total | 0-2 | 0.0 | -50.0 | -100.0 |
| fd_juice | early | 1h\|tt | 2-1 | 66.7 | 17.4 | 20.6 |
| fd_juice | early | 2h | 4-2 | 66.7 | 18.2 | 21.8 |
| fd_juice | early | 2h\|spread | 1-1 | 50.0 | 0.0 | -4.5 |
| fd_juice | early | 2h\|total | 2-0 | 100.0 | 55.5 | 81.7 |
| fd_juice | early | 2h\|tt | 1-1 | 50.0 | -0.7 | -11.5 |
| fd_juice | early | pin <$5k | 3-3 | 50.0 | 0.1 | -7.2 |
| fd_juice | early | q4 | 1-0 | 100.0 | 55.5 | 98.0 |
| fd_juice | early | q4\|total | 1-0 | 100.0 | 55.5 | 98.0 |
| follow_move+pin_price | early | 1h | 0-2 | 0.0 | -29.1 | -100.0 |
| fd_juice+pin_value | early | 1h | 1-0 | 100.0 | 50.7 | 61.7 |
| fd_juice+pin_price | early | 1h | 1-0 | 100.0 | 50.7 | 100.0 |
| follow_move+pin_value | early | 1h | 0-1 | 0.0 | -50.7 | -100.0 |
| pin_lead+pin_value | early | 1h | 0-1 | 0.0 | -55.5 | -100.0 |
| follow_move+pin_price | early | 1h\|ml | 0-2 | 0.0 | -29.1 | -100.0 |
| pin_lead+pin_value | early | 1h\|total | 0-1 | 0.0 | -55.5 | -100.0 |
| fd_juice+pin_value | early | 1h\|tt | 1-0 | 100.0 | 50.7 | 61.7 |
| fd_juice+pin_price | early | 1h\|tt | 1-0 | 100.0 | 50.7 | 100.0 |
| follow_move+pin_value | early | 1h\|tt | 0-1 | 0.0 | -50.7 | -100.0 |
| follow_move+pin_price | early | pin <$5k | 0-2 | 0.0 | -29.1 | -100.0 |
| fd_juice+pin_value | early | pin <$5k | 1-0 | 100.0 | 50.7 | 61.7 |
| fd_juice+pin_price | early | pin <$5k | 1-0 | 100.0 | 50.7 | 100.0 |
| follow_move+pin_value | early | pin <$5k | 0-1 | 0.0 | -50.7 | -100.0 |
| pin_lead+pin_value | early | pin <$5k | 0-1 | 0.0 | -55.5 | -100.0 |
