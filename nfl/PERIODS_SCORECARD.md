# NFL period scorecard — halves, quarters, team totals

Generated 2026-11-27 03:45 UTC. 490 graded period markets.

## Read this first: fit vs forward

**328 markets before 2026-11-17 (fit) · 162 on or after it (forward).** Every signal and threshold here was chosen by looking at the
fit markets, so a label there is a **hypothesis**; only the forward table is
**evidence**. Base rates are measured separately in each period.

Action Network serves no periods, so these lines come from the FanDuel event
feed and Pinnacle's `s;1;*` keys. **There are no tickets/money splits on any
period market**, so every signal here is handicap or price. Pinnacle's `s;3;*`
keys are excluded: tested against realised quarter scores they fit Q1 and Q3
about equally, so quarters are graded off FanDuel alone rather than guessed.
Everything settles from the boxscore linescore.

Base rates on this sample:

- **spread**: default side won 51.1% (n=94)
- **total**: default side won 46.8% (n=124)
- **ml**: default side won 69.8% (n=116)
- **tt**: default side won 51.4% (n=144)

Proposals appear at 40 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 12-11 | 52.2 | 49.0 | 3.1 | -0.61 | -2.7 | 0.35 | keep collecting (23/40) |
| pin_price | 2-7 | 22.2 | 44.9 | -22.7 | -5.17 | -57.5 | 0.39 | keep collecting (9/40) |
| pin_lead | 0-1 | 0.0 | 48.6 | -48.6 | -1.0 | -100.0 | 2.0 | keep collecting (1/40) |
| follow_move | 2-0 | 100.0 | 62.9 | 37.1 | +1.8 | 89.8 | -1.55 | keep collecting (2/40) |
| pin_lead+pin_value | 0-1 | 0.0 | 48.6 | -48.6 | -1.0 | -100.0 | 2.0 | redundant -- identical record to pin_lead alone, not independent confirmation |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 17-19 | 47.2 | 48.8 | -1.6 | -4.97 | -13.8 |  | keep collecting (36/40) |
| pin_price | 6-10 | 37.5 | 40.2 | -2.7 | -4.36 | -27.2 |  | keep collecting (16/40) |
| pin_lead | 1-1 | 50.0 | 54.7 | -4.7 | -0.09 | -4.5 |  | keep collecting (2/40) |
| follow_move | 61-45-2 | 57.5 | 50.7 | 6.8 | +6.52 | 6.0 |  | no edge shown yet |
| fd_juice | 25-18 | 58.1 | 51.3 | 6.8 | +3.44 | 8.0 |  | no edge shown yet |
| follow_move+pin_value | 1-2 | 33.3 | 43.5 | -10.2 | -1.2 | -40.0 |  | keep collecting (3/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 51.4 | 48.6 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move+pin_price | 5-1 | 83.3 | 43.7 | 39.6 | +3.88 | 64.6 |  | keep collecting (6/40) |
| fd_juice+pin_price | 1-0 | 100.0 | 53.3 | 46.7 | +0.77 | 76.9 |  | keep collecting (1/40) |
| fd_juice+pin_lead | 1-0 | 100.0 | 51.4 | 48.6 | +0.91 | 90.9 |  | keep collecting (1/40) |

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
| pin_value | 36-33 | 52.2 | 49.9 | 2.3 | -2.14 | -3.1 | 0.13 | no edge shown yet |
| pin_price | 6-15 | 28.6 | 45.0 | -16.5 | -8.04 | -38.3 | 0.3 | keep collecting (21/40) |
| pin_lead | 0-1 | 0.0 | 53.2 | -53.2 | -1.0 | -100.0 | 2.0 | keep collecting (1/40) |
| follow_move | 21-19-1 | 52.5 | 48.4 | 4.1 | +0.28 | 0.7 | -0.31 | no edge shown yet |
| fd_juice | 9-5 | 64.3 | 49.2 | 15.1 | +2.69 | 19.2 | 0.29 | keep collecting (14/40) |
| follow_move+pin_price | 0-2 | 0.0 | 30.2 | -30.2 | -2.0 | -100.0 | -0.35 | keep collecting (2/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 48.6 | 51.4 | +0.62 | 61.7 | 1.0 | keep collecting (1/40) |
| fd_juice+pin_price | 1-0 | 100.0 | 48.6 | 51.4 | +1.0 | 100.0 | 2.0 | keep collecting (1/40) |
| follow_move+pin_value | 0-1 | 0.0 | 51.4 | -51.4 | -1.0 | -100.0 | 1.0 | keep collecting (1/40) |
| pin_lead+pin_value | 0-1 | 0.0 | 53.2 | -53.2 | -1.0 | -100.0 | 2.0 | redundant -- identical record to pin_lead alone, not independent confirmation |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 70-66 | 51.5 | 49.8 | 1.6 | -7.43 | -5.5 |  | no edge shown yet |
| pin_price | 11-22 | 33.3 | 41.6 | -8.2 | -11.23 | -34.0 |  | keep collecting (33/40) |
| pin_lead | 2-1 | 66.7 | 48.9 | 17.7 | +0.71 | 23.6 |  | keep collecting (3/40) |
| follow_move | 152-132-12 | 53.5 | 49.9 | 3.6 | +0.55 | 0.2 |  | no edge shown yet |
| fd_juice | 62-58 | 51.7 | 50.0 | 1.7 | -5.17 | -4.3 |  | no edge shown yet |
| follow_move+pin_price | 5-5 | 50.0 | 38.3 | 11.7 | -0.13 | -1.3 |  | keep collecting (10/40) |
| pin_lead+pin_value | 1-0 | 100.0 | 48.9 | 51.1 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move+pin_value | 2-3 | 40.0 | 48.8 | -8.8 | -1.27 | -25.5 |  | keep collecting (5/40) |
| fd_juice+pin_price | 1-1 | 50.0 | 49.1 | 0.9 | -0.23 | -11.5 |  | keep collecting (2/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 46.8 | 53.2 | +0.8 | 80.0 |  | keep collecting (1/40) |
| fd_juice+pin_lead | 1-0 | 100.0 | 46.8 | 53.2 | +0.91 | 90.9 |  | keep collecting (1/40) |

## By period, market and Pinnacle limit (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 70-66 | 51.5 | 1.6 | -5.5 |
| pin_value | close | 1h\|spread | 18-23 | 43.9 | -5.8 | -21.2 |
| pin_value | close | 1h\|total | 22-20 | 52.4 | 2.5 | -1.5 |
| pin_value | close | 1h\|tt | 30-23 | 56.6 | 6.7 | 3.6 |
| pin_value | close | pin $20k+ | 12-19 | 38.7 | -11.1 | -31.5 |
| pin_value | close | pin $5-20k | 23-20 | 53.5 | 3.8 | -0.3 |
| pin_value | close | pin <$5k | 35-27 | 56.5 | 6.5 | 4.0 |
| pin_price | close | 1h | 11-22 | 33.3 | -8.2 | -34.0 |
| pin_price | close | 1h\|ml | 3-15 | 16.7 | -17.9 | -66.2 |
| pin_price | close | 1h\|spread | 1-1 | 50.0 | -1.1 | -4.5 |
| pin_price | close | 1h\|total | 2-1 | 66.7 | 17.7 | 24.7 |
| pin_price | close | 1h\|tt | 5-5 | 50.0 | 0.0 | 0.4 |
| pin_price | close | pin $20k+ | 3-2 | 60.0 | 13.5 | 10.6 |
| pin_price | close | pin $5-20k | 3-15 | 16.7 | -18.8 | -65.5 |
| pin_price | close | pin <$5k | 5-5 | 50.0 | 0.0 | 0.4 |
| pin_lead | close | 1h | 2-1 | 66.7 | 17.7 | 23.6 |
| pin_lead | close | 1h\|spread | 1-1 | 50.0 | 0.0 | -10.0 |
| pin_lead | close | 1h\|total | 1-0 | 100.0 | 53.2 | 90.9 |
| pin_lead | close | pin $20k+ | 1-0 | 100.0 | 51.1 | 80.0 |
| pin_lead | close | pin $5-20k | 1-1 | 50.0 | 1.1 | -4.5 |
| follow_move | close | 1h | 59-56-2 | 51.3 | 1.5 | -2.8 |
| follow_move | close | 1h\|ml | 24-16-2 | 60.0 | 11.0 | 7.1 |
| follow_move | close | 1h\|spread | 10-8 | 55.6 | 5.4 | 10.1 |
| follow_move | close | 1h\|total | 7-9 | 43.8 | -8.3 | -21.5 |
| follow_move | close | 1h\|tt | 18-23 | 43.9 | -5.7 | -11.3 |
| follow_move | close | 2h | 68-46-2 | 59.6 | 10.0 | 11.6 |
| follow_move | close | 2h\|ml | 19-23-2 | 45.2 | -3.8 | -22.7 |
| follow_move | close | 2h\|spread | 11-4 | 73.3 | 23.1 | 41.1 |
| follow_move | close | 2h\|total | 18-8 | 69.2 | 19.2 | 33.9 |
| follow_move | close | 2h\|tt | 20-11 | 64.5 | 14.7 | 27.3 |
| follow_move | close | pin $20k+ | 13-7-1 | 65.0 | 11.9 | 16.7 |
| follow_move | close | pin $5-20k | 26-25-1 | 51.0 | 2.5 | -6.0 |
| follow_move | close | pin <$5k | 20-24 | 45.5 | -4.4 | -8.3 |
| follow_move | close | q4 | 25-30-8 | 45.5 | -5.4 | -15.3 |
| follow_move | close | q4\|ml | 13-17-8 | 43.3 | -8.0 | -21.2 |
| follow_move | close | q4\|spread | 1-4 | 20.0 | -30.2 | -63.9 |
| follow_move | close | q4\|total | 11-9 | 55.0 | 4.7 | 7.9 |
| fd_juice | close | 1h | 22-13 | 62.9 | 12.6 | 16.7 |
| fd_juice | close | 1h\|spread | 3-3 | 50.0 | 0.0 | -8.9 |
| fd_juice | close | 1h\|total | 8-6 | 57.1 | 7.1 | 7.0 |
| fd_juice | close | 1h\|tt | 11-4 | 73.3 | 22.7 | 35.9 |
| fd_juice | close | 2h | 28-31 | 47.5 | -2.5 | -12.1 |
| fd_juice | close | 2h\|spread | 6-9 | 40.0 | -10.2 | -24.9 |
| fd_juice | close | 2h\|total | 6-7 | 46.2 | -3.1 | -13.3 |
| fd_juice | close | 2h\|tt | 16-15 | 51.6 | 1.5 | -5.5 |
| fd_juice | close | pin $20k+ | 3-1 | 75.0 | 25.0 | 36.6 |
| fd_juice | close | pin $5-20k | 7-8 | 46.7 | -3.0 | -12.9 |
| fd_juice | close | pin <$5k | 12-4 | 75.0 | 24.1 | 39.4 |
| fd_juice | close | q4 | 12-14 | 46.2 | -3.3 | -14.8 |
| fd_juice | close | q4\|spread | 3-9 | 25.0 | -25.0 | -54.4 |
| fd_juice | close | q4\|total | 9-5 | 64.3 | 15.2 | 19.2 |
| follow_move+pin_price | close | 1h | 5-5 | 50.0 | 11.7 | -1.3 |
| pin_lead+pin_value | close | 1h | 1-0 | 100.0 | 51.1 | 80.0 |
| follow_move+pin_value | close | 1h | 2-3 | 40.0 | -8.8 | -25.5 |
| fd_juice+pin_price | close | 1h | 1-1 | 50.0 | 0.9 | -11.5 |
| fd_juice+pin_value | close | 1h | 1-0 | 100.0 | 53.2 | 80.0 |
| fd_juice+pin_lead | close | 1h | 1-0 | 100.0 | 53.2 | 90.9 |
| follow_move+pin_price | close | 1h\|ml | 3-5 | 37.5 | 2.4 | -24.0 |
| pin_lead+pin_value | close | 1h\|spread | 1-0 | 100.0 | 51.1 | 80.0 |
| follow_move+pin_value | close | 1h\|spread | 1-2 | 33.3 | -15.6 | -40.0 |
| follow_move+pin_price | close | 1h\|spread | 1-0 | 100.0 | 48.9 | 90.9 |
| fd_juice+pin_price | close | 1h\|total | 0-1 | 0.0 | -46.8 | -100.0 |
| fd_juice+pin_value | close | 1h\|total | 1-0 | 100.0 | 53.2 | 80.0 |
| fd_juice+pin_lead | close | 1h\|total | 1-0 | 100.0 | 53.2 | 90.9 |
| follow_move+pin_value | close | 1h\|tt | 1-1 | 50.0 | 1.4 | -3.7 |
| follow_move+pin_price | close | 1h\|tt | 1-0 | 100.0 | 48.6 | 88.5 |
| fd_juice+pin_price | close | 1h\|tt | 1-0 | 100.0 | 48.6 | 76.9 |
| pin_lead+pin_value | close | pin $20k+ | 1-0 | 100.0 | 51.1 | 80.0 |
| follow_move+pin_value | close | pin $20k+ | 1-1 | 50.0 | 1.1 | -10.0 |
| follow_move+pin_price | close | pin $20k+ | 3-0 | 100.0 | 49.6 | 84.3 |
| follow_move+pin_price | close | pin $5-20k | 1-5 | 16.7 | -13.5 | -59.0 |
| fd_juice+pin_price | close | pin $5-20k | 0-1 | 0.0 | -46.8 | -100.0 |
| fd_juice+pin_value | close | pin $5-20k | 1-0 | 100.0 | 53.2 | 80.0 |
| follow_move+pin_value | close | pin $5-20k | 0-1 | 0.0 | -48.9 | -100.0 |
| fd_juice+pin_lead | close | pin $5-20k | 1-0 | 100.0 | 53.2 | 90.9 |
| follow_move+pin_value | close | pin <$5k | 1-1 | 50.0 | 1.4 | -3.7 |
| follow_move+pin_price | close | pin <$5k | 1-0 | 100.0 | 48.6 | 88.5 |
| fd_juice+pin_price | close | pin <$5k | 1-0 | 100.0 | 48.6 | 76.9 |
| pin_value | early | 1h | 36-33 | 52.2 | 2.3 | -3.1 |
| pin_value | early | 1h\|spread | 12-10 | 54.5 | 4.7 | 0.7 |
| pin_value | early | 1h\|total | 13-15 | 46.4 | -3.6 | -12.1 |
| pin_value | early | 1h\|tt | 11-8 | 57.9 | 8.0 | 5.8 |
| pin_value | early | pin $20k+ | 0-3 | 0.0 | -50.4 | -100.0 |
| pin_value | early | pin $5-20k | 2-3 | 40.0 | -10.2 | -19.0 |
| pin_value | early | pin <$5k | 34-27 | 55.7 | 5.9 | 3.0 |
| pin_price | early | 1h | 6-15 | 28.6 | -16.5 | -38.3 |
| pin_price | early | 1h\|ml | 2-7 | 22.2 | -16.8 | -46.5 |
| pin_price | early | 1h\|spread | 0-1 | 0.0 | -51.1 | -100.0 |
| pin_price | early | 1h\|total | 1-0 | 100.0 | 53.2 | 110.0 |
| pin_price | early | 1h\|tt | 3-7 | 30.0 | -19.7 | -39.6 |
| pin_price | early | pin $5-20k | 3-0 | 100.0 | 51.1 | 130.6 |
| pin_price | early | pin <$5k | 3-15 | 16.7 | -27.7 | -66.4 |
| pin_lead | early | 1h | 0-1 | 0.0 | -53.2 | -100.0 |
| pin_lead | early | 1h\|total | 0-1 | 0.0 | -53.2 | -100.0 |
| pin_lead | early | pin <$5k | 0-1 | 0.0 | -53.2 | -100.0 |
| follow_move | early | 1h | 8-10 | 44.4 | -3.9 | -17.7 |
| follow_move | early | 1h\|ml | 4-4 | 50.0 | 5.0 | -15.4 |
| follow_move | early | 1h\|total | 2-2 | 50.0 | -1.6 | -1.0 |
| follow_move | early | 1h\|tt | 2-4 | 33.3 | -17.1 | -32.0 |
| follow_move | early | 2h | 10-5 | 66.7 | 15.8 | 31.2 |
| follow_move | early | 2h\|ml | 5-2 | 71.4 | 18.6 | 44.1 |
| follow_move | early | 2h\|total | 3-1 | 75.0 | 28.2 | 45.3 |
| follow_move | early | 2h\|tt | 2-2 | 50.0 | -1.4 | -5.7 |
| follow_move | early | pin <$5k | 8-9 | 47.1 | -2.3 | -12.9 |
| follow_move | early | q4 | 3-4-1 | 42.9 | -0.4 | -15.0 |
| follow_move | early | q4\|ml | 2-2-1 | 50.0 | 9.9 | -4.8 |
| follow_move | early | q4\|spread | 0-1 | 0.0 | -48.9 | -100.0 |
| follow_move | early | q4\|total | 1-1 | 50.0 | 3.2 | 2.0 |
| fd_juice | early | 1h | 4-3 | 57.1 | 7.7 | 5.7 |
| fd_juice | early | 1h\|spread | 2-0 | 100.0 | 50.0 | 89.2 |
| fd_juice | early | 1h\|total | 0-2 | 0.0 | -50.0 | -100.0 |
| fd_juice | early | 1h\|tt | 2-1 | 66.7 | 18.1 | 20.6 |
| fd_juice | early | 2h | 4-2 | 66.7 | 17.3 | 21.8 |
| fd_juice | early | 2h\|spread | 1-1 | 50.0 | 0.0 | -4.5 |
| fd_juice | early | 2h\|total | 2-0 | 100.0 | 53.2 | 81.7 |
| fd_juice | early | 2h\|tt | 1-1 | 50.0 | -1.4 | -11.5 |
| fd_juice | early | pin <$5k | 3-3 | 50.0 | 0.5 | -7.2 |
| fd_juice | early | q4 | 1-0 | 100.0 | 53.2 | 98.0 |
| fd_juice | early | q4\|total | 1-0 | 100.0 | 53.2 | 98.0 |
| follow_move+pin_price | early | 1h | 0-2 | 0.0 | -30.2 | -100.0 |
| fd_juice+pin_value | early | 1h | 1-0 | 100.0 | 51.4 | 61.7 |
| fd_juice+pin_price | early | 1h | 1-0 | 100.0 | 51.4 | 100.0 |
| follow_move+pin_value | early | 1h | 0-1 | 0.0 | -51.4 | -100.0 |
| pin_lead+pin_value | early | 1h | 0-1 | 0.0 | -53.2 | -100.0 |
| follow_move+pin_price | early | 1h\|ml | 0-2 | 0.0 | -30.2 | -100.0 |
| pin_lead+pin_value | early | 1h\|total | 0-1 | 0.0 | -53.2 | -100.0 |
| fd_juice+pin_value | early | 1h\|tt | 1-0 | 100.0 | 51.4 | 61.7 |
| fd_juice+pin_price | early | 1h\|tt | 1-0 | 100.0 | 51.4 | 100.0 |
| follow_move+pin_value | early | 1h\|tt | 0-1 | 0.0 | -51.4 | -100.0 |
| follow_move+pin_price | early | pin <$5k | 0-2 | 0.0 | -30.2 | -100.0 |
| fd_juice+pin_value | early | pin <$5k | 1-0 | 100.0 | 51.4 | 61.7 |
| fd_juice+pin_price | early | pin <$5k | 1-0 | 100.0 | 51.4 | 100.0 |
| follow_move+pin_value | early | pin <$5k | 0-1 | 0.0 | -51.4 | -100.0 |
| pin_lead+pin_value | early | pin <$5k | 0-1 | 0.0 | -53.2 | -100.0 |
