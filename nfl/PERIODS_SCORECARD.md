# NFL period scorecard — halves, quarters, team totals

Generated 2026-11-28 05:13 UTC. 514 graded period markets.

## Read this first: fit vs forward

**328 markets before 2026-11-17 (fit) · 186 on or after it (forward).** Every signal and threshold here was chosen by looking at the
fit markets, so a label there is a **hypothesis**; only the forward table is
**evidence**. Base rates are measured separately in each period.

Action Network serves no periods, so these lines come from the FanDuel event
feed and Pinnacle's `s;1;*` keys. **There are no tickets/money splits on any
period market**, so every signal here is handicap or price. Pinnacle's `s;3;*`
keys are excluded: tested against realised quarter scores they fit Q1 and Q3
about equally, so quarters are graded off FanDuel alone rather than guessed.
Everything settles from the boxscore linescore.

Base rates on this sample:

- **spread**: default side won 50.0% (n=98)
- **total**: default side won 45.4% (n=130)
- **ml**: default side won 68.0% (n=122)
- **tt**: default side won 49.3% (n=152)

Proposals appear at 40 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 15-11 | 57.7 | 49.6 | 8.1 | +2.05 | 7.9 | 0.46 | keep collecting (26/40) |
| pin_price | 2-7 | 22.2 | 45.3 | -23.1 | -5.17 | -57.5 | 0.39 | keep collecting (9/40) |
| pin_lead | 0-1 | 0.0 | 53.5 | -53.5 | -1.0 | -100.0 | 2.0 | keep collecting (1/40) |
| follow_move | 2-0 | 100.0 | 58.2 | 41.8 | +1.8 | 89.8 | -1.55 | keep collecting (2/40) |
| pin_lead+pin_value | 0-1 | 0.0 | 53.5 | -53.5 | -1.0 | -100.0 | 2.0 | redundant -- identical record to pin_lead alone, not independent confirmation |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 18-23 | 43.9 | 48.6 | -4.7 | -8.34 | -20.3 |  | no edge shown yet |
| pin_price | 6-10 | 37.5 | 41.2 | -3.7 | -4.36 | -27.2 |  | keep collecting (16/40) |
| pin_lead | 1-1 | 50.0 | 50.4 | -0.4 | -0.09 | -4.5 |  | keep collecting (2/40) |
| follow_move | 74-53-2 | 58.3 | 52.0 | 6.3 | +10.16 | 7.9 |  | no edge shown yet |
| fd_juice | 26-20 | 56.5 | 49.1 | 7.4 | +2.24 | 4.9 |  | no edge shown yet |
| follow_move+pin_value | 1-3 | 25.0 | 49.4 | -24.4 | -2.2 | -55.0 |  | keep collecting (4/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 46.5 | 53.5 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move+pin_price | 5-1 | 83.3 | 43.6 | 39.7 | +3.88 | 64.6 |  | keep collecting (6/40) |
| fd_juice+pin_price | 1-0 | 100.0 | 47.2 | 52.8 | +0.77 | 76.9 |  | keep collecting (1/40) |
| fd_juice+pin_lead | 1-0 | 100.0 | 46.5 | 53.5 | +0.91 | 90.9 |  | keep collecting (1/40) |

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
| pin_value | 39-33 | 54.2 | 50.1 | 4.1 | +0.52 | 0.7 | 0.18 | no edge shown yet |
| pin_price | 6-15 | 28.6 | 45.5 | -17.0 | -8.04 | -38.3 | 0.3 | keep collecting (21/40) |
| pin_lead | 0-1 | 0.0 | 54.6 | -54.6 | -1.0 | -100.0 | 2.0 | keep collecting (1/40) |
| follow_move | 21-19-1 | 52.5 | 48.1 | 4.4 | +0.28 | 0.7 | -0.31 | no edge shown yet |
| fd_juice | 9-5 | 64.3 | 49.1 | 15.2 | +2.69 | 19.2 | 0.29 | keep collecting (14/40) |
| follow_move+pin_price | 0-2 | 0.0 | 32.0 | -32.0 | -2.0 | -100.0 | -0.35 | keep collecting (2/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 50.7 | 49.3 | +0.62 | 61.7 | 1.0 | keep collecting (1/40) |
| fd_juice+pin_price | 1-0 | 100.0 | 50.7 | 49.3 | +1.0 | 100.0 | 2.0 | keep collecting (1/40) |
| follow_move+pin_value | 0-1 | 0.0 | 49.3 | -49.3 | -1.0 | -100.0 | 1.0 | keep collecting (1/40) |
| pin_lead+pin_value | 0-1 | 0.0 | 54.6 | -54.6 | -1.0 | -100.0 | 2.0 | redundant -- identical record to pin_lead alone, not independent confirmation |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 71-70 | 50.4 | 50.0 | 0.4 | -10.8 | -7.7 |  | no edge shown yet |
| pin_price | 11-22 | 33.3 | 42.2 | -8.9 | -11.23 | -34.0 |  | keep collecting (33/40) |
| pin_lead | 2-1 | 66.7 | 48.5 | 18.2 | +0.71 | 23.6 |  | keep collecting (3/40) |
| follow_move | 165-140-12 | 54.1 | 50.4 | 3.7 | +4.18 | 1.3 |  | no edge shown yet |
| fd_juice | 63-60 | 51.2 | 49.7 | 1.5 | -6.37 | -5.2 |  | no edge shown yet |
| follow_move+pin_price | 5-5 | 50.0 | 39.1 | 10.9 | -0.13 | -1.3 |  | keep collecting (10/40) |
| pin_lead+pin_value | 1-0 | 100.0 | 50.0 | 50.0 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move+pin_value | 2-4 | 33.3 | 51.0 | -17.7 | -2.27 | -37.9 |  | keep collecting (6/40) |
| fd_juice+pin_price | 1-1 | 50.0 | 47.4 | 2.6 | -0.23 | -11.5 |  | keep collecting (2/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 45.4 | 54.6 | +0.8 | 80.0 |  | keep collecting (1/40) |
| fd_juice+pin_lead | 1-0 | 100.0 | 45.4 | 54.6 | +0.91 | 90.9 |  | keep collecting (1/40) |

## By period, market and Pinnacle limit (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 71-70 | 50.4 | 0.4 | -7.7 |
| pin_value | close | 1h\|spread | 18-24 | 42.9 | -7.1 | -23.1 |
| pin_value | close | 1h\|total | 22-21 | 51.2 | 1.3 | -3.8 |
| pin_value | close | 1h\|tt | 31-25 | 55.4 | 5.3 | 0.9 |
| pin_value | close | pin $20k+ | 12-20 | 37.5 | -12.6 | -33.6 |
| pin_value | close | pin $5-20k | 23-21 | 52.3 | 2.5 | -2.6 |
| pin_value | close | pin <$5k | 36-29 | 55.4 | 5.4 | 1.7 |
| pin_price | close | 1h | 11-22 | 33.3 | -8.9 | -34.0 |
| pin_price | close | 1h\|ml | 3-15 | 16.7 | -19.3 | -66.2 |
| pin_price | close | 1h\|spread | 1-1 | 50.0 | 0.0 | -4.5 |
| pin_price | close | 1h\|total | 2-1 | 66.7 | 18.2 | 24.7 |
| pin_price | close | 1h\|tt | 5-5 | 50.0 | 0.0 | 0.4 |
| pin_price | close | pin $20k+ | 3-2 | 60.0 | 13.6 | 10.6 |
| pin_price | close | pin $5-20k | 3-15 | 16.7 | -20.1 | -65.5 |
| pin_price | close | pin <$5k | 5-5 | 50.0 | 0.0 | 0.4 |
| pin_lead | close | 1h | 2-1 | 66.7 | 18.2 | 23.6 |
| pin_lead | close | 1h\|spread | 1-1 | 50.0 | 0.0 | -10.0 |
| pin_lead | close | 1h\|total | 1-0 | 100.0 | 54.6 | 90.9 |
| pin_lead | close | pin $20k+ | 1-0 | 100.0 | 50.0 | 80.0 |
| pin_lead | close | pin $5-20k | 1-1 | 50.0 | 2.3 | -4.5 |
| follow_move | close | 1h | 64-61-2 | 51.2 | 0.7 | -3.0 |
| follow_move | close | 1h\|ml | 25-17-2 | 59.5 | 9.5 | 5.8 |
| follow_move | close | 1h\|spread | 11-9 | 55.0 | 5.0 | 8.3 |
| follow_move | close | 1h\|total | 8-10 | 44.4 | -8.6 | -20.2 |
| follow_move | close | 1h\|tt | 20-25 | 44.4 | -5.8 | -9.7 |
| follow_move | close | 2h | 74-48-2 | 60.7 | 10.8 | 13.5 |
| follow_move | close | 2h\|ml | 20-24-2 | 45.5 | -3.7 | -21.8 |
| follow_move | close | 2h\|spread | 11-5 | 68.8 | 18.8 | 32.3 |
| follow_move | close | 2h\|total | 20-8 | 71.4 | 21.1 | 38.3 |
| follow_move | close | 2h\|tt | 23-11 | 67.6 | 17.5 | 32.1 |
| follow_move | close | pin $20k+ | 15-8-1 | 65.2 | 12.1 | 16.2 |
| follow_move | close | pin $5-20k | 27-27-1 | 50.0 | 0.7 | -7.8 |
| follow_move | close | pin <$5k | 22-26 | 45.8 | -4.8 | -7.1 |
| follow_move | close | q4 | 27-31-8 | 46.6 | -4.9 | -13.3 |
| follow_move | close | q4\|ml | 14-18-8 | 43.8 | -8.5 | -20.7 |
| follow_move | close | q4\|spread | 1-4 | 20.0 | -30.0 | -63.9 |
| follow_move | close | q4\|total | 12-9 | 57.1 | 6.5 | 12.7 |
| fd_juice | close | 1h | 22-13 | 62.9 | 13.0 | 16.7 |
| fd_juice | close | 1h\|spread | 3-3 | 50.0 | 0.0 | -8.9 |
| fd_juice | close | 1h\|total | 8-6 | 57.1 | 7.1 | 7.0 |
| fd_juice | close | 1h\|tt | 11-4 | 73.3 | 23.6 | 35.9 |
| fd_juice | close | 2h | 28-32 | 46.7 | -3.1 | -13.6 |
| fd_juice | close | 2h\|spread | 6-9 | 40.0 | -10.0 | -24.9 |
| fd_juice | close | 2h\|total | 6-7 | 46.2 | -2.8 | -13.3 |
| fd_juice | close | 2h\|tt | 16-16 | 50.0 | 0.1 | -8.4 |
| fd_juice | close | pin $20k+ | 3-1 | 75.0 | 25.0 | 36.6 |
| fd_juice | close | pin $5-20k | 7-8 | 46.7 | -2.7 | -12.9 |
| fd_juice | close | pin <$5k | 12-4 | 75.0 | 24.7 | 39.4 |
| fd_juice | close | q4 | 13-15 | 46.4 | -3.1 | -14.5 |
| fd_juice | close | q4\|spread | 3-10 | 23.1 | -26.9 | -57.9 |
| fd_juice | close | q4\|total | 10-5 | 66.7 | 17.6 | 23.2 |
| follow_move+pin_price | close | 1h | 5-5 | 50.0 | 10.9 | -1.3 |
| pin_lead+pin_value | close | 1h | 1-0 | 100.0 | 50.0 | 80.0 |
| follow_move+pin_value | close | 1h | 2-4 | 33.3 | -17.7 | -37.9 |
| fd_juice+pin_price | close | 1h | 1-1 | 50.0 | 2.6 | -11.5 |
| fd_juice+pin_value | close | 1h | 1-0 | 100.0 | 54.6 | 80.0 |
| fd_juice+pin_lead | close | 1h | 1-0 | 100.0 | 54.6 | 90.9 |
| follow_move+pin_price | close | 1h\|ml | 3-5 | 37.5 | 1.0 | -24.0 |
| pin_lead+pin_value | close | 1h\|spread | 1-0 | 100.0 | 50.0 | 80.0 |
| follow_move+pin_value | close | 1h\|spread | 1-2 | 33.3 | -16.7 | -40.0 |
| follow_move+pin_price | close | 1h\|spread | 1-0 | 100.0 | 50.0 | 90.9 |
| fd_juice+pin_price | close | 1h\|total | 0-1 | 0.0 | -45.4 | -100.0 |
| fd_juice+pin_value | close | 1h\|total | 1-0 | 100.0 | 54.6 | 80.0 |
| fd_juice+pin_lead | close | 1h\|total | 1-0 | 100.0 | 54.6 | 90.9 |
| follow_move+pin_value | close | 1h\|total | 0-1 | 0.0 | -54.6 | -100.0 |
| follow_move+pin_value | close | 1h\|tt | 1-1 | 50.0 | -0.7 | -3.7 |
| follow_move+pin_price | close | 1h\|tt | 1-0 | 100.0 | 50.7 | 88.5 |
| fd_juice+pin_price | close | 1h\|tt | 1-0 | 100.0 | 50.7 | 76.9 |
| pin_lead+pin_value | close | pin $20k+ | 1-0 | 100.0 | 50.0 | 80.0 |
| follow_move+pin_value | close | pin $20k+ | 1-1 | 50.0 | 0.0 | -10.0 |
| follow_move+pin_price | close | pin $20k+ | 3-0 | 100.0 | 50.0 | 84.3 |
| follow_move+pin_price | close | pin $5-20k | 1-5 | 16.7 | -15.3 | -59.0 |
| fd_juice+pin_price | close | pin $5-20k | 0-1 | 0.0 | -45.4 | -100.0 |
| fd_juice+pin_value | close | pin $5-20k | 1-0 | 100.0 | 54.6 | 80.0 |
| follow_move+pin_value | close | pin $5-20k | 0-2 | 0.0 | -52.3 | -100.0 |
| fd_juice+pin_lead | close | pin $5-20k | 1-0 | 100.0 | 54.6 | 90.9 |
| follow_move+pin_value | close | pin <$5k | 1-1 | 50.0 | -0.7 | -3.7 |
| follow_move+pin_price | close | pin <$5k | 1-0 | 100.0 | 50.7 | 88.5 |
| fd_juice+pin_price | close | pin <$5k | 1-0 | 100.0 | 50.7 | 76.9 |
| pin_value | early | 1h | 39-33 | 54.2 | 4.1 | 0.7 |
| pin_value | early | 1h\|spread | 13-10 | 56.5 | 6.5 | 4.3 |
| pin_value | early | 1h\|total | 14-15 | 48.3 | -1.9 | -8.4 |
| pin_value | early | 1h\|tt | 12-8 | 60.0 | 9.9 | 9.9 |
| pin_value | early | pin $20k+ | 0-3 | 0.0 | -50.0 | -100.0 |
| pin_value | early | pin $5-20k | 3-3 | 50.0 | 0.0 | -1.9 |
| pin_value | early | pin <$5k | 36-27 | 57.1 | 7.0 | 5.8 |
| pin_price | early | 1h | 6-15 | 28.6 | -17.0 | -38.3 |
| pin_price | early | 1h\|ml | 2-7 | 22.2 | -17.8 | -46.5 |
| pin_price | early | 1h\|spread | 0-1 | 0.0 | -50.0 | -100.0 |
| pin_price | early | 1h\|total | 1-0 | 100.0 | 54.6 | 110.0 |
| pin_price | early | 1h\|tt | 3-7 | 30.0 | -20.1 | -39.6 |
| pin_price | early | pin $5-20k | 3-0 | 100.0 | 51.5 | 130.6 |
| pin_price | early | pin <$5k | 3-15 | 16.7 | -28.4 | -66.4 |
| pin_lead | early | 1h | 0-1 | 0.0 | -54.6 | -100.0 |
| pin_lead | early | 1h\|total | 0-1 | 0.0 | -54.6 | -100.0 |
| pin_lead | early | pin <$5k | 0-1 | 0.0 | -54.6 | -100.0 |
| follow_move | early | 1h | 8-10 | 44.4 | -4.0 | -17.7 |
| follow_move | early | 1h\|ml | 4-4 | 50.0 | 4.5 | -15.4 |
| follow_move | early | 1h\|total | 2-2 | 50.0 | -2.3 | -1.0 |
| follow_move | early | 1h\|tt | 2-4 | 33.3 | -16.4 | -32.0 |
| follow_move | early | 2h | 10-5 | 66.7 | 16.9 | 31.2 |
| follow_move | early | 2h\|ml | 5-2 | 71.4 | 18.9 | 44.1 |
| follow_move | early | 2h\|total | 3-1 | 75.0 | 29.6 | 45.3 |
| follow_move | early | 2h\|tt | 2-2 | 50.0 | 0.7 | -5.7 |
| follow_move | early | pin <$5k | 8-9 | 47.1 | -2.3 | -12.9 |
| follow_move | early | q4 | 3-4-1 | 42.9 | -0.7 | -15.0 |
| follow_move | early | q4\|ml | 2-2-1 | 50.0 | 9.0 | -4.8 |
| follow_move | early | q4\|spread | 0-1 | 0.0 | -50.0 | -100.0 |
| follow_move | early | q4\|total | 1-1 | 50.0 | 4.6 | 2.0 |
| fd_juice | early | 1h | 4-3 | 57.1 | 6.9 | 5.7 |
| fd_juice | early | 1h\|spread | 2-0 | 100.0 | 50.0 | 89.2 |
| fd_juice | early | 1h\|total | 0-2 | 0.0 | -50.0 | -100.0 |
| fd_juice | early | 1h\|tt | 2-1 | 66.7 | 16.0 | 20.6 |
| fd_juice | early | 2h | 4-2 | 66.7 | 18.4 | 21.8 |
| fd_juice | early | 2h\|spread | 1-1 | 50.0 | 0.0 | -4.5 |
| fd_juice | early | 2h\|total | 2-0 | 100.0 | 54.6 | 81.7 |
| fd_juice | early | 2h\|tt | 1-1 | 50.0 | 0.7 | -11.5 |
| fd_juice | early | pin <$5k | 3-3 | 50.0 | -0.3 | -7.2 |
| fd_juice | early | q4 | 1-0 | 100.0 | 54.6 | 98.0 |
| fd_juice | early | q4\|total | 1-0 | 100.0 | 54.6 | 98.0 |
| follow_move+pin_price | early | 1h | 0-2 | 0.0 | -32.0 | -100.0 |
| fd_juice+pin_value | early | 1h | 1-0 | 100.0 | 49.3 | 61.7 |
| fd_juice+pin_price | early | 1h | 1-0 | 100.0 | 49.3 | 100.0 |
| follow_move+pin_value | early | 1h | 0-1 | 0.0 | -49.3 | -100.0 |
| pin_lead+pin_value | early | 1h | 0-1 | 0.0 | -54.6 | -100.0 |
| follow_move+pin_price | early | 1h\|ml | 0-2 | 0.0 | -32.0 | -100.0 |
| pin_lead+pin_value | early | 1h\|total | 0-1 | 0.0 | -54.6 | -100.0 |
| fd_juice+pin_value | early | 1h\|tt | 1-0 | 100.0 | 49.3 | 61.7 |
| fd_juice+pin_price | early | 1h\|tt | 1-0 | 100.0 | 49.3 | 100.0 |
| follow_move+pin_value | early | 1h\|tt | 0-1 | 0.0 | -49.3 | -100.0 |
| follow_move+pin_price | early | pin <$5k | 0-2 | 0.0 | -32.0 | -100.0 |
| fd_juice+pin_value | early | pin <$5k | 1-0 | 100.0 | 49.3 | 61.7 |
| fd_juice+pin_price | early | pin <$5k | 1-0 | 100.0 | 49.3 | 100.0 |
| follow_move+pin_value | early | pin <$5k | 0-1 | 0.0 | -49.3 | -100.0 |
| pin_lead+pin_value | early | pin <$5k | 0-1 | 0.0 | -54.6 | -100.0 |
