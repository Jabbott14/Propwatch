# NFL period scorecard — halves, quarters, team totals

Generated 2026-11-16 07:13 UTC. 328 graded period markets.

Action Network serves no periods, so these lines come from the FanDuel event
feed and Pinnacle's `s;1;*` keys. **There are no tickets/money splits on any
period market**, so every signal here is handicap or price. Pinnacle's `s;3;*`
keys are excluded: tested against realised quarter scores they fit Q1 and Q3
about equally, so quarters are graded off FanDuel alone rather than guessed.
Everything settles from the boxscore linescore.

Base rates on this sample:

- **spread**: default side won 47.6% (n=63)
- **total**: default side won 44.8% (n=87)
- **ml**: default side won 66.7% (n=69)
- **tt**: default side won 50.5% (n=99)

Proposals appear at 40 decided markets. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 24-22 | 52.2 | 49.9 | 2.3 | -1.53 | -3.3 | 0.02 | no edge shown yet |
| pin_price | 4-8 | 33.3 | 45.1 | -11.7 | -2.87 | -23.9 | 0.24 | keep collecting (12/40) |
| follow_move | 19-19-1 | 50.0 | 48.0 | 2.0 | -1.51 | -3.9 | -0.25 | keep collecting (38/40) |
| fd_juice | 9-5 | 64.3 | 48.9 | 15.4 | +2.69 | 19.2 | 0.29 | keep collecting (14/40) |
| follow_move+pin_price | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 | -0.35 | keep collecting (2/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 49.5 | 50.5 | +0.62 | 61.7 | 1.0 | keep collecting (1/40) |
| fd_juice+pin_price | 1-0 | 100.0 | 49.5 | 50.5 | +1.0 | 100.0 | 2.0 | keep collecting (1/40) |
| follow_move+pin_value | 0-1 | 0.0 | 50.5 | -50.5 | -1.0 | -100.0 | 1.0 | keep collecting (1/40) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 53-47 | 53.0 | 50.2 | 2.8 | -2.46 | -2.5 |  | no edge shown yet |
| pin_price | 5-12 | 29.4 | 42.6 | -13.2 | -6.88 | -40.4 |  | keep collecting (17/40) |
| pin_lead | 1-0 | 100.0 | 52.4 | 47.6 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move | 91-87-10 | 51.1 | 49.5 | 1.6 | -5.97 | -3.2 |  | no edge shown yet |
| fd_juice | 37-40 | 48.1 | 50.0 | -2.0 | -8.61 | -11.2 |  | no edge shown yet |
| follow_move+pin_price | 0-4 | 0.0 | 33.3 | -33.3 | -4.0 | -100.0 |  | keep collecting (4/40) |
| pin_lead+pin_value | 1-0 | 100.0 | 52.4 | 47.6 | +0.8 | 80.0 |  | redundant -- identical record to pin_lead alone, not independent confirmation |
| follow_move+pin_value | 1-1 | 50.0 | 50.9 | -0.9 | -0.07 | -3.7 |  | keep collecting (2/40) |
| fd_juice+pin_price | 0-1 | 0.0 | 44.8 | -44.8 | -1.0 | -100.0 |  | keep collecting (1/40) |

## By period, market and Pinnacle limit

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 53-47 | 53.0 | 2.8 | -2.5 |
| pin_value | close | 1h|spread | 12-16 | 42.9 | -7.5 | -23.1 |
| pin_value | close | 1h|total | 17-14 | 54.8 | 4.3 | 3.4 |
| pin_value | close | 1h|tt | 24-17 | 58.5 | 8.6 | 7.2 |
| pin_value | close | pin $20k+ | 9-14 | 39.1 | -11.5 | -30.8 |
| pin_value | close | pin $5-20k | 14-12 | 53.8 | 3.4 | 0.6 |
| pin_value | close | pin <$5k | 30-21 | 58.8 | 8.9 | 8.8 |
| pin_price | close | 1h | 5-12 | 29.4 | -13.2 | -40.4 |
| pin_price | close | 1h|ml | 0-7 | 0.0 | -33.3 | -100.0 |
| pin_price | close | 1h|spread | 0-1 | 0.0 | -47.6 | -100.0 |
| pin_price | close | 1h|total | 2-1 | 66.7 | 18.4 | 24.7 |
| pin_price | close | 1h|tt | 3-3 | 50.0 | 0.2 | 6.4 |
| pin_price | close | pin $20k+ | 0-1 | 0.0 | -47.6 | -100.0 |
| pin_price | close | pin $5-20k | 2-8 | 20.0 | -17.8 | -62.6 |
| pin_price | close | pin <$5k | 3-3 | 50.0 | 0.2 | 6.4 |
| pin_lead | close | 1h | 1-0 | 100.0 | 47.6 | 80.0 |
| pin_lead | close | 1h|spread | 1-0 | 100.0 | 47.6 | 80.0 |
| pin_lead | close | pin $20k+ | 1-0 | 100.0 | 47.6 | 80.0 |
| follow_move | close | 1h | 34-40-1 | 45.9 | -4.0 | -13.4 |
| follow_move | close | 1h|ml | 13-13-1 | 50.0 | 1.3 | -10.3 |
| follow_move | close | 1h|spread | 5-5 | 50.0 | 0.5 | -0.4 |
| follow_move | close | 1h|total | 4-7 | 36.4 | -16.9 | -38.3 |
| follow_move | close | 1h|tt | 12-15 | 44.4 | -5.4 | -11.1 |
| follow_move | close | 2h | 40-32-2 | 55.6 | 6.5 | 5.7 |
| follow_move | close | 2h|ml | 12-13-2 | 48.0 | 0.0 | -11.9 |
| follow_move | close | 2h|spread | 6-3 | 66.7 | 16.9 | 28.9 |
| follow_move | close | 2h|total | 12-7 | 63.2 | 14.0 | 23.7 |
| follow_move | close | 2h|tt | 10-9 | 52.6 | 2.6 | 2.0 |
| follow_move | close | pin $20k+ | 6-6 | 50.0 | -2.4 | -11.5 |
| follow_move | close | pin $5-20k | 14-17-1 | 45.2 | -3.2 | -17.5 |
| follow_move | close | pin <$5k | 14-17 | 45.2 | -5.4 | -9.8 |
| follow_move | close | q4 | 17-15-7 | 53.1 | 3.4 | -0.5 |
| follow_move | close | q4|ml | 8-7-7 | 53.3 | 4.4 | -3.7 |
| follow_move | close | q4|spread | 1-2 | 33.3 | -15.9 | -39.8 |
| follow_move | close | q4|total | 8-6 | 57.1 | 6.4 | 12.9 |
| fd_juice | close | 1h | 12-9 | 57.1 | 6.3 | 7.0 |
| fd_juice | close | 1h|spread | 2-3 | 40.0 | -10.5 | -26.7 |
| fd_juice | close | 1h|total | 5-4 | 55.6 | 3.8 | 4.0 |
| fd_juice | close | 1h|tt | 5-2 | 71.4 | 21.5 | 35.0 |
| fd_juice | close | 2h | 17-22 | 43.6 | -6.3 | -19.4 |
| fd_juice | close | 2h|spread | 5-5 | 50.0 | -0.0 | -5.6 |
| fd_juice | close | 2h|total | 2-5 | 28.6 | -20.7 | -44.8 |
| fd_juice | close | 2h|tt | 10-12 | 45.5 | -4.6 | -17.5 |
| fd_juice | close | pin $20k+ | 2-1 | 66.7 | 15.9 | 22.2 |
| fd_juice | close | pin $5-20k | 4-5 | 44.4 | -6.1 | -17.2 |
| fd_juice | close | pin <$5k | 6-3 | 66.7 | 15.6 | 26.2 |
| fd_juice | close | q4 | 8-9 | 47.1 | -2.4 | -14.9 |
| fd_juice | close | q4|spread | 3-5 | 37.5 | -11.9 | -31.6 |
| fd_juice | close | q4|total | 5-4 | 55.6 | 6.1 | 0.0 |
| follow_move+pin_price | close | 1h | 0-4 | 0.0 | -33.3 | -100.0 |
| pin_lead+pin_value | close | 1h | 1-0 | 100.0 | 47.6 | 80.0 |
| follow_move+pin_value | close | 1h | 1-1 | 50.0 | -0.9 | -3.7 |
| fd_juice+pin_price | close | 1h | 0-1 | 0.0 | -44.8 | -100.0 |
| follow_move+pin_price | close | 1h|ml | 0-4 | 0.0 | -33.3 | -100.0 |
| pin_lead+pin_value | close | 1h|spread | 1-0 | 100.0 | 47.6 | 80.0 |
| follow_move+pin_value | close | 1h|spread | 0-1 | 0.0 | -52.4 | -100.0 |
| fd_juice+pin_price | close | 1h|total | 0-1 | 0.0 | -44.8 | -100.0 |
| follow_move+pin_value | close | 1h|tt | 1-0 | 100.0 | 50.5 | 92.6 |
| pin_lead+pin_value | close | pin $20k+ | 1-0 | 100.0 | 47.6 | 80.0 |
| follow_move+pin_value | close | pin $20k+ | 0-1 | 0.0 | -52.4 | -100.0 |
| follow_move+pin_price | close | pin $5-20k | 0-4 | 0.0 | -33.3 | -100.0 |
| fd_juice+pin_price | close | pin $5-20k | 0-1 | 0.0 | -44.8 | -100.0 |
| follow_move+pin_value | close | pin <$5k | 1-0 | 100.0 | 50.5 | 92.6 |
| pin_value | early | 1h | 24-22 | 52.2 | 2.3 | -3.3 |
| pin_value | early | 1h|spread | 7-6 | 53.8 | 3.7 | -1.3 |
| pin_value | early | 1h|total | 9-8 | 52.9 | 3.2 | 1.1 |
| pin_value | early | 1h|tt | 8-8 | 50.0 | 0.1 | -9.7 |
| pin_value | early | pin $20k+ | 0-3 | 0.0 | -49.2 | -100.0 |
| pin_value | early | pin $5-20k | 1-3 | 25.0 | -25.0 | -50.0 |
| pin_value | early | pin <$5k | 23-16 | 59.0 | 9.0 | 8.9 |
| pin_price | early | 1h | 4-8 | 33.3 | -11.7 | -23.9 |
| pin_price | early | 1h|ml | 1-4 | 20.0 | -20.0 | -39.0 |
| pin_price | early | 1h|spread | 0-1 | 0.0 | -47.6 | -100.0 |
| pin_price | early | 1h|total | 1-0 | 100.0 | 55.2 | 110.0 |
| pin_price | early | 1h|tt | 2-3 | 40.0 | -9.7 | -20.4 |
| pin_price | early | pin $5-20k | 2-0 | 100.0 | 60.9 | 157.5 |
| pin_price | early | pin <$5k | 2-8 | 20.0 | -26.3 | -60.2 |
| follow_move | early | 1h | 7-10 | 41.2 | -7.8 | -25.0 |
| follow_move | early | 1h|ml | 4-4 | 50.0 | 4.2 | -15.4 |
| follow_move | early | 1h|total | 1-2 | 33.3 | -21.8 | -36.4 |
| follow_move | early | 1h|tt | 2-4 | 33.3 | -16.8 | -32.0 |
| follow_move | early | 2h | 9-5 | 64.3 | 15.6 | 28.0 |
| follow_move | early | 2h|ml | 4-2 | 66.7 | 16.7 | 39.1 |
| follow_move | early | 2h|total | 3-1 | 75.0 | 30.2 | 45.3 |
| follow_move | early | 2h|tt | 2-2 | 50.0 | -0.5 | -5.7 |
| follow_move | early | pin <$5k | 7-9 | 43.8 | -6.2 | -20.3 |
| follow_move | early | q4 | 3-4-1 | 42.9 | -1.2 | -15.0 |
| follow_move | early | q4|ml | 2-2-1 | 50.0 | 8.3 | -4.8 |
| follow_move | early | q4|spread | 0-1 | 0.0 | -52.4 | -100.0 |
| follow_move | early | q4|total | 1-1 | 50.0 | 5.2 | 2.0 |
| fd_juice | early | 1h | 4-3 | 57.1 | 7.4 | 5.7 |
| fd_juice | early | 1h|spread | 2-0 | 100.0 | 50.0 | 89.2 |
| fd_juice | early | 1h|total | 0-2 | 0.0 | -50.0 | -100.0 |
| fd_juice | early | 1h|tt | 2-1 | 66.7 | 17.2 | 20.6 |
| fd_juice | early | 2h | 4-2 | 66.7 | 18.2 | 21.8 |
| fd_juice | early | 2h|spread | 1-1 | 50.0 | 0.0 | -4.5 |
| fd_juice | early | 2h|total | 2-0 | 100.0 | 55.2 | 81.7 |
| fd_juice | early | 2h|tt | 1-1 | 50.0 | -0.5 | -11.5 |
| fd_juice | early | pin <$5k | 3-3 | 50.0 | 0.6 | -7.2 |
| fd_juice | early | q4 | 1-0 | 100.0 | 55.2 | 98.0 |
| fd_juice | early | q4|total | 1-0 | 100.0 | 55.2 | 98.0 |
| follow_move+pin_price | early | 1h | 0-2 | 0.0 | -33.3 | -100.0 |
| fd_juice+pin_value | early | 1h | 1-0 | 100.0 | 50.5 | 61.7 |
| fd_juice+pin_price | early | 1h | 1-0 | 100.0 | 50.5 | 100.0 |
| follow_move+pin_value | early | 1h | 0-1 | 0.0 | -50.5 | -100.0 |
| follow_move+pin_price | early | 1h|ml | 0-2 | 0.0 | -33.3 | -100.0 |
| fd_juice+pin_value | early | 1h|tt | 1-0 | 100.0 | 50.5 | 61.7 |
| fd_juice+pin_price | early | 1h|tt | 1-0 | 100.0 | 50.5 | 100.0 |
| follow_move+pin_value | early | 1h|tt | 0-1 | 0.0 | -50.5 | -100.0 |
| follow_move+pin_price | early | pin <$5k | 0-2 | 0.0 | -33.3 | -100.0 |
| fd_juice+pin_value | early | pin <$5k | 1-0 | 100.0 | 50.5 | 61.7 |
| fd_juice+pin_price | early | pin <$5k | 1-0 | 100.0 | 50.5 | 100.0 |
| follow_move+pin_value | early | pin <$5k | 0-1 | 0.0 | -50.5 | -100.0 |
