# NFL period scorecard — halves, quarters, team totals

Generated 2026-11-26 22:26 UTC. 479 graded period markets.

## Read this first: fit vs forward

**328 markets before 2026-11-17 (fit) · 151 on or after it (forward).** Every signal and threshold here was chosen by looking at the
fit markets, so a label there is a **hypothesis**; only the forward table is
**evidence**. Base rates are measured separately in each period.

Action Network serves no periods, so these lines come from the FanDuel event
feed and Pinnacle's `s;1;*` keys. **There are no tickets/money splits on any
period market**, so every signal here is handicap or price. Pinnacle's `s;3;*`
keys are excluded: tested against realised quarter scores they fit Q1 and Q3
about equally, so quarters are graded off FanDuel alone rather than guessed.
Everything settles from the boxscore linescore.

Base rates on this sample:

- **spread**: default side won 51.6% (n=91)
- **total**: default side won 45.5% (n=121)
- **ml**: default side won 70.8% (n=113)
- **tt**: default side won 51.4% (n=142)

Proposals appear at 40 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 12-9 | 57.1 | 49.1 | 8.0 | +1.39 | 6.6 | 0.38 | keep collecting (21/40) |
| pin_price | 2-5 | 28.6 | 47.1 | -18.5 | -3.17 | -45.3 | 0.86 | keep collecting (7/40) |
| pin_lead | 0-1 | 0.0 | 52.9 | -52.9 | -1.0 | -100.0 | 2.0 | keep collecting (1/40) |
| follow_move | 2-0 | 100.0 | 62.2 | 37.8 | +1.8 | 89.8 | -1.55 | keep collecting (2/40) |
| pin_lead+pin_value | 0-1 | 0.0 | 52.9 | -52.9 | -1.0 | -100.0 | 2.0 | redundant -- identical record to pin_lead alone, not independent confirmation |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 17-17 | 50.0 | 48.0 | 2.0 | -2.97 | -8.7 |  | keep collecting (34/40) |
| pin_price | 6-9 | 40.0 | 40.3 | -0.3 | -3.36 | -22.4 |  | keep collecting (15/40) |
| pin_lead | 0-1 | 0.0 | 60.7 | -60.7 | -1.0 | -100.0 |  | keep collecting (1/40) |
| follow_move | 58-42-2 | 58.0 | 50.3 | 7.7 | +7.52 | 7.4 |  | no edge shown yet |
| fd_juice | 23-16 | 59.0 | 50.5 | 8.4 | +3.64 | 9.3 |  | keep collecting (39/40) |
| follow_move+pin_value | 1-2 | 33.3 | 41.7 | -8.4 | -1.2 | -40.0 |  | keep collecting (3/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 47.1 | 52.9 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move+pin_price | 5-1 | 83.3 | 43.3 | 40.1 | +3.88 | 64.6 |  | keep collecting (6/40) |
| fd_juice+pin_price | 1-0 | 100.0 | 53.5 | 46.5 | +0.77 | 76.9 |  | keep collecting (1/40) |

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
| pin_value | 36-31 | 53.7 | 49.8 | 3.9 | -0.14 | -0.2 | 0.13 | no edge shown yet |
| pin_price | 6-13 | 31.6 | 45.4 | -13.8 | -6.04 | -31.8 | 0.47 | keep collecting (19/40) |
| pin_lead | 0-1 | 0.0 | 54.5 | -54.5 | -1.0 | -100.0 | 2.0 | keep collecting (1/40) |
| follow_move | 21-19-1 | 52.5 | 48.2 | 4.3 | +0.28 | 0.7 | -0.31 | no edge shown yet |
| fd_juice | 9-5 | 64.3 | 48.9 | 15.4 | +2.69 | 19.2 | 0.29 | keep collecting (14/40) |
| follow_move+pin_price | 0-2 | 0.0 | 29.2 | -29.2 | -2.0 | -100.0 | -0.35 | keep collecting (2/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 48.6 | 51.4 | +0.62 | 61.7 | 1.0 | keep collecting (1/40) |
| fd_juice+pin_price | 1-0 | 100.0 | 48.6 | 51.4 | +1.0 | 100.0 | 2.0 | keep collecting (1/40) |
| follow_move+pin_value | 0-1 | 0.0 | 51.4 | -51.4 | -1.0 | -100.0 | 1.0 | keep collecting (1/40) |
| pin_lead+pin_value | 0-1 | 0.0 | 54.5 | -54.5 | -1.0 | -100.0 | 2.0 | redundant -- identical record to pin_lead alone, not independent confirmation |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 70-64 | 52.2 | 49.8 | 2.5 | -5.43 | -4.1 |  | no edge shown yet |
| pin_price | 11-21 | 34.4 | 41.5 | -7.1 | -10.23 | -32.0 |  | keep collecting (32/40) |
| pin_lead | 1-1 | 50.0 | 50.0 | 0.0 | -0.2 | -10.0 |  | keep collecting (2/40) |
| follow_move | 149-129-12 | 53.6 | 49.8 | 3.8 | +1.55 | 0.5 |  | no edge shown yet |
| fd_juice | 60-56 | 51.7 | 49.9 | 1.8 | -4.97 | -4.3 |  | no edge shown yet |
| follow_move+pin_price | 5-5 | 50.0 | 37.8 | 12.2 | -0.13 | -1.3 |  | keep collecting (10/40) |
| pin_lead+pin_value | 1-0 | 100.0 | 48.4 | 51.6 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move+pin_value | 2-3 | 40.0 | 48.4 | -8.4 | -1.27 | -25.5 |  | keep collecting (5/40) |
| fd_juice+pin_price | 1-1 | 50.0 | 48.4 | 1.6 | -0.23 | -11.5 |  | keep collecting (2/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 45.5 | 54.5 | +0.8 | 80.0 |  | keep collecting (1/40) |

## By period, market and Pinnacle limit (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 70-64 | 52.2 | 2.5 | -4.1 |
| pin_value | close | 1h\|spread | 18-22 | 45.0 | -4.6 | -19.2 |
| pin_value | close | 1h\|total | 22-20 | 52.4 | 2.6 | -1.5 |
| pin_value | close | 1h\|tt | 30-22 | 57.7 | 7.7 | 5.5 |
| pin_value | close | pin $20k+ | 12-18 | 40.0 | -9.8 | -29.2 |
| pin_value | close | pin $5-20k | 23-20 | 53.5 | 4.0 | -0.3 |
| pin_value | close | pin <$5k | 35-26 | 57.4 | 7.4 | 5.7 |
| pin_price | close | 1h | 11-21 | 34.4 | -7.1 | -32.0 |
| pin_price | close | 1h\|ml | 3-14 | 17.6 | -16.4 | -64.2 |
| pin_price | close | 1h\|spread | 1-1 | 50.0 | -1.6 | -4.5 |
| pin_price | close | 1h\|total | 2-1 | 66.7 | 18.2 | 24.7 |
| pin_price | close | 1h\|tt | 5-5 | 50.0 | 0.0 | 0.4 |
| pin_price | close | pin $20k+ | 3-2 | 60.0 | 13.5 | 10.6 |
| pin_price | close | pin $5-20k | 3-14 | 17.6 | -17.4 | -63.5 |
| pin_price | close | pin <$5k | 5-5 | 50.0 | 0.0 | 0.4 |
| pin_lead | close | 1h | 1-1 | 50.0 | 0.0 | -10.0 |
| pin_lead | close | 1h\|spread | 1-1 | 50.0 | 0.0 | -10.0 |
| pin_lead | close | pin $20k+ | 1-0 | 100.0 | 51.6 | 80.0 |
| pin_lead | close | pin $5-20k | 0-1 | 0.0 | -51.6 | -100.0 |
| follow_move | close | 1h | 57-56-2 | 50.4 | 0.7 | -3.8 |
| follow_move | close | 1h\|ml | 23-16-2 | 59.0 | 10.6 | 6.6 |
| follow_move | close | 1h\|spread | 10-8 | 55.6 | 5.4 | 10.1 |
| follow_move | close | 1h\|total | 7-9 | 43.8 | -9.1 | -21.5 |
| follow_move | close | 1h\|tt | 17-23 | 42.5 | -7.0 | -13.8 |
| follow_move | close | 2h | 67-45-2 | 59.8 | 10.3 | 12.0 |
| follow_move | close | 2h\|ml | 19-22-2 | 46.3 | -2.1 | -20.9 |
| follow_move | close | 2h\|spread | 11-4 | 73.3 | 23.0 | 41.1 |
| follow_move | close | 2h\|total | 17-8 | 68.0 | 17.8 | 31.9 |
| follow_move | close | 2h\|tt | 20-11 | 64.5 | 14.7 | 27.3 |
| follow_move | close | pin $20k+ | 13-7-1 | 65.0 | 11.6 | 16.7 |
| follow_move | close | pin $5-20k | 25-25-1 | 50.0 | 2.0 | -6.6 |
| follow_move | close | pin <$5k | 19-24 | 44.2 | -5.7 | -10.6 |
| follow_move | close | q4 | 25-28-8 | 47.2 | -3.4 | -12.6 |
| follow_move | close | q4\|ml | 13-16-8 | 44.8 | -5.9 | -19.0 |
| follow_move | close | q4\|spread | 1-3 | 25.0 | -25.0 | -54.9 |
| follow_move | close | q4\|total | 11-9 | 55.0 | 4.5 | 7.9 |
| fd_juice | close | 1h | 21-13 | 61.8 | 11.3 | 14.5 |
| fd_juice | close | 1h\|spread | 3-3 | 50.0 | 0.0 | -8.9 |
| fd_juice | close | 1h\|total | 7-6 | 53.8 | 3.5 | 0.5 |
| fd_juice | close | 1h\|tt | 11-4 | 73.3 | 22.7 | 35.9 |
| fd_juice | close | 2h | 28-29 | 49.1 | -0.7 | -9.0 |
| fd_juice | close | 2h\|spread | 6-8 | 42.9 | -7.4 | -19.5 |
| fd_juice | close | 2h\|total | 6-7 | 46.2 | -2.8 | -13.3 |
| fd_juice | close | 2h\|tt | 16-14 | 53.3 | 3.2 | -2.3 |
| fd_juice | close | pin $20k+ | 3-1 | 75.0 | 25.0 | 36.6 |
| fd_juice | close | pin $5-20k | 6-8 | 42.9 | -6.9 | -20.3 |
| fd_juice | close | pin <$5k | 12-4 | 75.0 | 23.9 | 39.4 |
| fd_juice | close | q4 | 11-14 | 44.0 | -5.5 | -19.0 |
| fd_juice | close | q4\|spread | 3-9 | 25.0 | -25.0 | -54.4 |
| fd_juice | close | q4\|total | 8-5 | 61.5 | 12.6 | 13.8 |
| follow_move+pin_price | close | 1h | 5-5 | 50.0 | 12.2 | -1.3 |
| pin_lead+pin_value | close | 1h | 1-0 | 100.0 | 51.6 | 80.0 |
| follow_move+pin_value | close | 1h | 2-3 | 40.0 | -8.4 | -25.5 |
| fd_juice+pin_price | close | 1h | 1-1 | 50.0 | 1.6 | -11.5 |
| fd_juice+pin_value | close | 1h | 1-0 | 100.0 | 54.5 | 80.0 |
| follow_move+pin_price | close | 1h\|ml | 3-5 | 37.5 | 3.1 | -24.0 |
| pin_lead+pin_value | close | 1h\|spread | 1-0 | 100.0 | 51.6 | 80.0 |
| follow_move+pin_value | close | 1h\|spread | 1-2 | 33.3 | -15.0 | -40.0 |
| follow_move+pin_price | close | 1h\|spread | 1-0 | 100.0 | 48.4 | 90.9 |
| fd_juice+pin_price | close | 1h\|total | 0-1 | 0.0 | -45.5 | -100.0 |
| fd_juice+pin_value | close | 1h\|total | 1-0 | 100.0 | 54.5 | 80.0 |
| follow_move+pin_value | close | 1h\|tt | 1-1 | 50.0 | 1.4 | -3.7 |
| follow_move+pin_price | close | 1h\|tt | 1-0 | 100.0 | 48.6 | 88.5 |
| fd_juice+pin_price | close | 1h\|tt | 1-0 | 100.0 | 48.6 | 76.9 |
| pin_lead+pin_value | close | pin $20k+ | 1-0 | 100.0 | 51.6 | 80.0 |
| follow_move+pin_value | close | pin $20k+ | 1-1 | 50.0 | 1.6 | -10.0 |
| follow_move+pin_price | close | pin $20k+ | 3-0 | 100.0 | 49.5 | 84.3 |
| follow_move+pin_price | close | pin $5-20k | 1-5 | 16.7 | -12.5 | -59.0 |
| fd_juice+pin_price | close | pin $5-20k | 0-1 | 0.0 | -45.5 | -100.0 |
| fd_juice+pin_value | close | pin $5-20k | 1-0 | 100.0 | 54.5 | 80.0 |
| follow_move+pin_value | close | pin $5-20k | 0-1 | 0.0 | -48.4 | -100.0 |
| follow_move+pin_value | close | pin <$5k | 1-1 | 50.0 | 1.4 | -3.7 |
| follow_move+pin_price | close | pin <$5k | 1-0 | 100.0 | 48.6 | 88.5 |
| fd_juice+pin_price | close | pin <$5k | 1-0 | 100.0 | 48.6 | 76.9 |
| pin_value | early | 1h | 36-31 | 53.7 | 3.9 | -0.2 |
| pin_value | early | 1h\|spread | 12-9 | 57.1 | 7.4 | 5.5 |
| pin_value | early | 1h\|total | 13-14 | 48.1 | -1.7 | -8.9 |
| pin_value | early | 1h\|tt | 11-8 | 57.9 | 8.0 | 5.8 |
| pin_value | early | pin $20k+ | 0-3 | 0.0 | -50.5 | -100.0 |
| pin_value | early | pin $5-20k | 2-3 | 40.0 | -10.3 | -19.0 |
| pin_value | early | pin <$5k | 34-25 | 57.6 | 7.9 | 6.5 |
| pin_price | early | 1h | 6-13 | 31.6 | -13.8 | -31.8 |
| pin_price | early | 1h\|ml | 2-6 | 25.0 | -14.6 | -39.8 |
| pin_price | early | 1h\|spread | 0-1 | 0.0 | -51.6 | -100.0 |
| pin_price | early | 1h\|total | 1-0 | 100.0 | 54.5 | 110.0 |
| pin_price | early | 1h\|tt | 3-6 | 33.3 | -16.5 | -32.9 |
| pin_price | early | pin $5-20k | 3-0 | 100.0 | 51.5 | 130.6 |
| pin_price | early | pin <$5k | 3-13 | 18.8 | -26.1 | -62.2 |
| pin_lead | early | 1h | 0-1 | 0.0 | -54.5 | -100.0 |
| pin_lead | early | 1h\|total | 0-1 | 0.0 | -54.5 | -100.0 |
| pin_lead | early | pin <$5k | 0-1 | 0.0 | -54.5 | -100.0 |
| follow_move | early | 1h | 8-10 | 44.4 | -3.9 | -17.7 |
| follow_move | early | 1h\|ml | 4-4 | 50.0 | 5.2 | -15.4 |
| follow_move | early | 1h\|total | 2-2 | 50.0 | -2.3 | -1.0 |
| follow_move | early | 1h\|tt | 2-4 | 33.3 | -17.1 | -32.0 |
| follow_move | early | 2h | 10-5 | 66.7 | 16.1 | 31.2 |
| follow_move | early | 2h\|ml | 5-2 | 71.4 | 18.5 | 44.1 |
| follow_move | early | 2h\|total | 3-1 | 75.0 | 29.5 | 45.3 |
| follow_move | early | 2h\|tt | 2-2 | 50.0 | -1.4 | -5.7 |
| follow_move | early | pin <$5k | 8-9 | 47.1 | -2.4 | -12.9 |
| follow_move | early | q4 | 3-4-1 | 42.9 | 0.3 | -15.0 |
| follow_move | early | q4\|ml | 2-2-1 | 50.0 | 10.4 | -4.8 |
| follow_move | early | q4\|spread | 0-1 | 0.0 | -48.4 | -100.0 |
| follow_move | early | q4\|total | 1-1 | 50.0 | 4.5 | 2.0 |
| fd_juice | early | 1h | 4-3 | 57.1 | 7.7 | 5.7 |
| fd_juice | early | 1h\|spread | 2-0 | 100.0 | 50.0 | 89.2 |
| fd_juice | early | 1h\|total | 0-2 | 0.0 | -50.0 | -100.0 |
| fd_juice | early | 1h\|tt | 2-1 | 66.7 | 18.1 | 20.6 |
| fd_juice | early | 2h | 4-2 | 66.7 | 17.7 | 21.8 |
| fd_juice | early | 2h\|spread | 1-1 | 50.0 | 0.0 | -4.5 |
| fd_juice | early | 2h\|total | 2-0 | 100.0 | 54.5 | 81.7 |
| fd_juice | early | 2h\|tt | 1-1 | 50.0 | -1.4 | -11.5 |
| fd_juice | early | pin <$5k | 3-3 | 50.0 | 0.4 | -7.2 |
| fd_juice | early | q4 | 1-0 | 100.0 | 54.5 | 98.0 |
| fd_juice | early | q4\|total | 1-0 | 100.0 | 54.5 | 98.0 |
| follow_move+pin_price | early | 1h | 0-2 | 0.0 | -29.2 | -100.0 |
| fd_juice+pin_value | early | 1h | 1-0 | 100.0 | 51.4 | 61.7 |
| fd_juice+pin_price | early | 1h | 1-0 | 100.0 | 51.4 | 100.0 |
| follow_move+pin_value | early | 1h | 0-1 | 0.0 | -51.4 | -100.0 |
| pin_lead+pin_value | early | 1h | 0-1 | 0.0 | -54.5 | -100.0 |
| follow_move+pin_price | early | 1h\|ml | 0-2 | 0.0 | -29.2 | -100.0 |
| pin_lead+pin_value | early | 1h\|total | 0-1 | 0.0 | -54.5 | -100.0 |
| fd_juice+pin_value | early | 1h\|tt | 1-0 | 100.0 | 51.4 | 61.7 |
| fd_juice+pin_price | early | 1h\|tt | 1-0 | 100.0 | 51.4 | 100.0 |
| follow_move+pin_value | early | 1h\|tt | 0-1 | 0.0 | -51.4 | -100.0 |
| follow_move+pin_price | early | pin <$5k | 0-2 | 0.0 | -29.2 | -100.0 |
| fd_juice+pin_value | early | pin <$5k | 1-0 | 100.0 | 51.4 | 61.7 |
| fd_juice+pin_price | early | pin <$5k | 1-0 | 100.0 | 51.4 | 100.0 |
| follow_move+pin_value | early | pin <$5k | 0-1 | 0.0 | -51.4 | -100.0 |
| pin_lead+pin_value | early | pin <$5k | 0-1 | 0.0 | -54.5 | -100.0 |
