# NFL period scorecard — halves, quarters, team totals

Generated 2026-11-20 12:08 UTC. 346 graded period markets.

## Read this first: fit vs forward

**328 markets before 2026-11-17 (fit) · 18 on or after it (forward).** Every signal and threshold here was chosen by looking at the
fit markets, so a label there is a **hypothesis**; only the forward table is
**evidence**. Base rates are measured separately in each period.

Action Network serves no periods, so these lines come from the FanDuel event
feed and Pinnacle's `s;1;*` keys. **There are no tickets/money splits on any
period market**, so every signal here is handicap or price. Pinnacle's `s;3;*`
keys are excluded: tested against realised quarter scores they fit Q1 and Q3
about equally, so quarters are graded off FanDuel alone rather than guessed.
Everything settles from the boxscore linescore.

Base rates on this sample:

- **spread**: default side won 47.8% (n=67)
- **total**: default side won 43.3% (n=90)
- **ml**: default side won 67.6% (n=74)
- **tt**: default side won 50.0% (n=104)

Proposals appear at 40 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 2-0 | 100.0 | 75.0 | 25.0 | +1.6 | 80.0 | 1.0 | keep collecting (2/40) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 0-5 | 0.0 | 40.0 | -40.0 | -5.0 | -100.0 |  | keep collecting (5/40) |
| pin_price | 0-1 | 0.0 | 20.0 | -20.0 | -1.0 | -100.0 |  | keep collecting (1/40) |
| follow_move | 10-2-1 | 83.3 | 52.5 | 30.8 | +6.84 | 52.6 |  | keep collecting (12/40) |
| fd_juice | 2-3 | 40.0 | 38.0 | 2.0 | -1.25 | -25.0 |  | keep collecting (5/40) |

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
| pin_value | 26-22 | 54.2 | 50.1 | 4.1 | +0.07 | 0.2 | 0.06 | no edge shown yet |
| pin_price | 4-8 | 33.3 | 44.9 | -11.5 | -2.87 | -23.9 | 0.24 | keep collecting (12/40) |
| follow_move | 19-19-1 | 50.0 | 47.7 | 2.3 | -1.51 | -3.9 | -0.25 | keep collecting (38/40) |
| fd_juice | 9-5 | 64.3 | 48.6 | 15.7 | +2.69 | 19.2 | 0.29 | keep collecting (14/40) |
| follow_move+pin_price | 0-2 | 0.0 | 32.4 | -32.4 | -2.0 | -100.0 | -0.35 | keep collecting (2/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 50.0 | 50.0 | +0.62 | 61.7 | 1.0 | keep collecting (1/40) |
| fd_juice+pin_price | 1-0 | 100.0 | 50.0 | 50.0 | +1.0 | 100.0 | 2.0 | keep collecting (1/40) |
| follow_move+pin_value | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 1.0 | keep collecting (1/40) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 53-52 | 50.5 | 50.2 | 0.3 | -7.46 | -7.1 |  | no edge shown yet |
| pin_price | 5-13 | 27.8 | 41.7 | -13.9 | -7.88 | -43.8 |  | keep collecting (18/40) |
| pin_lead | 1-0 | 100.0 | 52.2 | 47.8 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move | 101-89-11 | 53.2 | 49.7 | 3.5 | +0.87 | 0.4 |  | no edge shown yet |
| fd_juice | 39-43 | 47.6 | 49.9 | -2.4 | -9.86 | -12.0 |  | no edge shown yet |
| follow_move+pin_price | 0-4 | 0.0 | 32.4 | -32.4 | -4.0 | -100.0 |  | keep collecting (4/40) |
| pin_lead+pin_value | 1-0 | 100.0 | 52.2 | 47.8 | +0.8 | 80.0 |  | redundant -- identical record to pin_lead alone, not independent confirmation |
| follow_move+pin_value | 1-1 | 50.0 | 51.1 | -1.1 | -0.07 | -3.7 |  | keep collecting (2/40) |
| fd_juice+pin_price | 0-1 | 0.0 | 43.3 | -43.3 | -1.0 | -100.0 |  | keep collecting (1/40) |

## By period, market and Pinnacle limit (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 53-52 | 50.5 | 0.3 | -7.1 |
| pin_value | close | 1h\|spread | 12-18 | 40.0 | -10.3 | -28.2 |
| pin_value | close | 1h\|total | 17-15 | 53.1 | 2.7 | 0.2 |
| pin_value | close | 1h\|tt | 24-19 | 55.8 | 5.8 | 2.2 |
| pin_value | close | pin $20k+ | 9-16 | 36.0 | -14.6 | -36.4 |
| pin_value | close | pin $5-20k | 14-13 | 51.9 | 1.6 | -3.1 |
| pin_value | close | pin <$5k | 30-23 | 56.6 | 6.6 | 4.7 |
| pin_price | close | 1h | 5-13 | 27.8 | -13.9 | -43.8 |
| pin_price | close | 1h\|ml | 0-8 | 0.0 | -32.4 | -100.0 |
| pin_price | close | 1h\|spread | 0-1 | 0.0 | -47.8 | -100.0 |
| pin_price | close | 1h\|total | 2-1 | 66.7 | 18.9 | 24.7 |
| pin_price | close | 1h\|tt | 3-3 | 50.0 | 0.0 | 6.4 |
| pin_price | close | pin $20k+ | 0-1 | 0.0 | -47.8 | -100.0 |
| pin_price | close | pin $5-20k | 2-9 | 18.2 | -18.4 | -66.0 |
| pin_price | close | pin <$5k | 3-3 | 50.0 | 0.0 | 6.4 |
| pin_lead | close | 1h | 1-0 | 100.0 | 47.8 | 80.0 |
| pin_lead | close | 1h\|spread | 1-0 | 100.0 | 47.8 | 80.0 |
| pin_lead | close | pin $20k+ | 1-0 | 100.0 | 47.8 | 80.0 |
| follow_move | close | 1h | 41-40-1 | 50.6 | 0.4 | -3.6 |
| follow_move | close | 1h\|ml | 15-13-1 | 53.6 | 4.8 | -3.6 |
| follow_move | close | 1h\|spread | 7-5 | 58.3 | 8.7 | 17.6 |
| follow_move | close | 1h\|total | 5-7 | 41.7 | -12.8 | -27.5 |
| follow_move | close | 1h\|tt | 14-15 | 48.3 | -1.7 | -2.6 |
| follow_move | close | 2h | 42-33-2 | 56.0 | 7.0 | 5.7 |
| follow_move | close | 2h\|ml | 13-14-2 | 48.1 | 0.1 | -13.5 |
| follow_move | close | 2h\|spread | 7-3 | 70.0 | 20.4 | 34.7 |
| follow_move | close | 2h\|total | 12-7 | 63.2 | 14.2 | 23.7 |
| follow_move | close | 2h\|tt | 10-9 | 52.6 | 2.6 | 2.0 |
| follow_move | close | pin $20k+ | 8-6 | 57.1 | 5.0 | 5.5 |
| follow_move | close | pin $5-20k | 17-17-1 | 50.0 | 1.3 | -8.4 |
| follow_move | close | pin <$5k | 16-17 | 48.5 | -2.3 | -2.4 |
| follow_move | close | q4 | 18-16-8 | 52.9 | 2.8 | -1.4 |
| follow_move | close | q4\|ml | 9-7-8 | 56.2 | 6.3 | -0.8 |
| follow_move | close | q4\|spread | 1-2 | 33.3 | -15.9 | -39.8 |
| follow_move | close | q4\|total | 8-7 | 53.3 | 2.9 | 5.4 |
| fd_juice | close | 1h | 13-9 | 59.1 | 8.1 | 11.2 |
| fd_juice | close | 1h\|spread | 2-3 | 40.0 | -10.4 | -26.7 |
| fd_juice | close | 1h\|total | 5-4 | 55.6 | 3.3 | 4.0 |
| fd_juice | close | 1h\|tt | 6-2 | 75.0 | 25.0 | 42.9 |
| fd_juice | close | 2h | 18-24 | 42.9 | -6.8 | -20.9 |
| fd_juice | close | 2h\|spread | 5-5 | 50.0 | 0.0 | -5.6 |
| fd_juice | close | 2h\|total | 2-6 | 25.0 | -23.3 | -51.7 |
| fd_juice | close | 2h\|tt | 11-13 | 45.8 | -4.2 | -17.0 |
| fd_juice | close | pin $20k+ | 2-1 | 66.7 | 15.9 | 22.2 |
| fd_juice | close | pin $5-20k | 4-5 | 44.4 | -6.3 | -17.2 |
| fd_juice | close | pin <$5k | 7-3 | 70.0 | 18.7 | 33.4 |
| fd_juice | close | q4 | 8-10 | 44.4 | -4.8 | -19.6 |
| fd_juice | close | q4\|spread | 3-6 | 33.3 | -15.9 | -39.2 |
| fd_juice | close | q4\|total | 5-4 | 55.6 | 6.3 | 0.0 |
| follow_move+pin_price | close | 1h | 0-4 | 0.0 | -32.4 | -100.0 |
| pin_lead+pin_value | close | 1h | 1-0 | 100.0 | 47.8 | 80.0 |
| follow_move+pin_value | close | 1h | 1-1 | 50.0 | -1.1 | -3.7 |
| fd_juice+pin_price | close | 1h | 0-1 | 0.0 | -43.3 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 0-4 | 0.0 | -32.4 | -100.0 |
| pin_lead+pin_value | close | 1h\|spread | 1-0 | 100.0 | 47.8 | 80.0 |
| follow_move+pin_value | close | 1h\|spread | 0-1 | 0.0 | -52.2 | -100.0 |
| fd_juice+pin_price | close | 1h\|total | 0-1 | 0.0 | -43.3 | -100.0 |
| follow_move+pin_value | close | 1h\|tt | 1-0 | 100.0 | 50.0 | 92.6 |
| pin_lead+pin_value | close | pin $20k+ | 1-0 | 100.0 | 47.8 | 80.0 |
| follow_move+pin_value | close | pin $20k+ | 0-1 | 0.0 | -52.2 | -100.0 |
| follow_move+pin_price | close | pin $5-20k | 0-4 | 0.0 | -32.4 | -100.0 |
| fd_juice+pin_price | close | pin $5-20k | 0-1 | 0.0 | -43.3 | -100.0 |
| follow_move+pin_value | close | pin <$5k | 1-0 | 100.0 | 50.0 | 92.6 |
| pin_value | early | 1h | 26-22 | 54.2 | 4.1 | 0.2 |
| pin_value | early | 1h\|spread | 8-6 | 57.1 | 6.8 | 4.6 |
| pin_value | early | 1h\|total | 10-8 | 55.6 | 5.6 | 5.5 |
| pin_value | early | 1h\|tt | 8-8 | 50.0 | 0.0 | -9.7 |
| pin_value | early | pin $20k+ | 0-3 | 0.0 | -49.3 | -100.0 |
| pin_value | early | pin $5-20k | 1-3 | 25.0 | -25.0 | -50.0 |
| pin_value | early | pin <$5k | 25-16 | 61.0 | 10.8 | 12.4 |
| pin_price | early | 1h | 4-8 | 33.3 | -11.5 | -23.9 |
| pin_price | early | 1h\|ml | 1-4 | 20.0 | -19.5 | -39.0 |
| pin_price | early | 1h\|spread | 0-1 | 0.0 | -47.8 | -100.0 |
| pin_price | early | 1h\|total | 1-0 | 100.0 | 56.7 | 110.0 |
| pin_price | early | 1h\|tt | 2-3 | 40.0 | -10.0 | -20.4 |
| pin_price | early | pin $5-20k | 2-0 | 100.0 | 62.1 | 157.5 |
| pin_price | early | pin <$5k | 2-8 | 20.0 | -26.3 | -60.2 |
| follow_move | early | 1h | 7-10 | 41.2 | -7.9 | -25.0 |
| follow_move | early | 1h\|ml | 4-4 | 50.0 | 4.4 | -15.4 |
| follow_move | early | 1h\|total | 1-2 | 33.3 | -23.3 | -36.4 |
| follow_move | early | 1h\|tt | 2-4 | 33.3 | -16.7 | -32.0 |
| follow_move | early | 2h | 9-5 | 64.3 | 16.2 | 28.0 |
| follow_move | early | 2h\|ml | 4-2 | 66.7 | 16.7 | 39.1 |
| follow_move | early | 2h\|total | 3-1 | 75.0 | 31.7 | 45.3 |
| follow_move | early | 2h\|tt | 2-2 | 50.0 | 0.0 | -5.7 |
| follow_move | early | pin <$5k | 7-9 | 43.8 | -6.4 | -20.3 |
| follow_move | early | q4 | 3-4-1 | 42.9 | -0.5 | -15.0 |
| follow_move | early | q4\|ml | 2-2-1 | 50.0 | 8.8 | -4.8 |
| follow_move | early | q4\|spread | 0-1 | 0.0 | -52.2 | -100.0 |
| follow_move | early | q4\|total | 1-1 | 50.0 | 6.7 | 2.0 |
| fd_juice | early | 1h | 4-3 | 57.1 | 7.1 | 5.7 |
| fd_juice | early | 1h\|spread | 2-0 | 100.0 | 50.0 | 89.2 |
| fd_juice | early | 1h\|total | 0-2 | 0.0 | -50.0 | -100.0 |
| fd_juice | early | 1h\|tt | 2-1 | 66.7 | 16.7 | 20.6 |
| fd_juice | early | 2h | 4-2 | 66.7 | 18.9 | 21.8 |
| fd_juice | early | 2h\|spread | 1-1 | 50.0 | 0.0 | -4.5 |
| fd_juice | early | 2h\|total | 2-0 | 100.0 | 56.7 | 81.7 |
| fd_juice | early | 2h\|tt | 1-1 | 50.0 | 0.0 | -11.5 |
| fd_juice | early | pin <$5k | 3-3 | 50.0 | 0.4 | -7.2 |
| fd_juice | early | q4 | 1-0 | 100.0 | 56.7 | 98.0 |
| fd_juice | early | q4\|total | 1-0 | 100.0 | 56.7 | 98.0 |
| follow_move+pin_price | early | 1h | 0-2 | 0.0 | -32.4 | -100.0 |
| fd_juice+pin_value | early | 1h | 1-0 | 100.0 | 50.0 | 61.7 |
| fd_juice+pin_price | early | 1h | 1-0 | 100.0 | 50.0 | 100.0 |
| follow_move+pin_value | early | 1h | 0-1 | 0.0 | -50.0 | -100.0 |
| follow_move+pin_price | early | 1h\|ml | 0-2 | 0.0 | -32.4 | -100.0 |
| fd_juice+pin_value | early | 1h\|tt | 1-0 | 100.0 | 50.0 | 61.7 |
| fd_juice+pin_price | early | 1h\|tt | 1-0 | 100.0 | 50.0 | 100.0 |
| follow_move+pin_value | early | 1h\|tt | 0-1 | 0.0 | -50.0 | -100.0 |
| follow_move+pin_price | early | pin <$5k | 0-2 | 0.0 | -32.4 | -100.0 |
| fd_juice+pin_value | early | pin <$5k | 1-0 | 100.0 | 50.0 | 61.7 |
| fd_juice+pin_price | early | pin <$5k | 1-0 | 100.0 | 50.0 | 100.0 |
| follow_move+pin_value | early | pin <$5k | 0-1 | 0.0 | -50.0 | -100.0 |
