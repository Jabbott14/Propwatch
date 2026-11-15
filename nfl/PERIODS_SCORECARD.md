# NFL period scorecard — halves, quarters, team totals

Generated 2026-11-15 23:09 UTC. 289 graded period markets.

Action Network serves no periods, so these lines come from the FanDuel event
feed and Pinnacle's `s;1;*` keys. **There are no tickets/money splits on any
period market**, so every signal here is handicap or price. Pinnacle's `s;3;*`
keys are excluded: tested against realised quarter scores they fit Q1 and Q3
about equally, so quarters are graded off FanDuel alone rather than guessed.
Everything settles from the boxscore linescore.

Base rates on this sample:

- **spread**: default side won 45.5% (n=55)
- **total**: default side won 43.4% (n=76)
- **ml**: default side won 66.7% (n=60)
- **tt**: default side won 50.0% (n=88)

Proposals appear at 40 decided markets. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 20-16 | 55.6 | 50.6 | 4.9 | +1.04 | 2.9 | 0.17 | keep collecting (36/40) |
| pin_price | 3-8 | 27.3 | 44.4 | -17.2 | -3.85 | -35.0 | 0.35 | keep collecting (11/40) |
| follow_move | 19-19-1 | 50.0 | 47.8 | 2.2 | -1.51 | -3.9 | -0.25 | keep collecting (38/40) |
| fd_juice | 9-5 | 64.3 | 48.6 | 15.7 | +2.69 | 19.2 | 0.29 | keep collecting (14/40) |
| follow_move+pin_price | 0-2 | 0.0 | 33.3 | -33.3 | -2.0 | -100.0 | -0.35 | keep collecting (2/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 50.0 | 50.0 | +0.62 | 61.7 | 1.0 | keep collecting (1/40) |
| fd_juice+pin_price | 1-0 | 100.0 | 50.0 | 50.0 | +1.0 | 100.0 | 2.0 | keep collecting (1/40) |
| follow_move+pin_value | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 1.0 | keep collecting (1/40) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 46-42 | 52.3 | 50.7 | 1.6 | -3.48 | -4.0 |  | no edge shown yet |
| pin_price | 3-12 | 20.0 | 41.9 | -21.9 | -8.67 | -57.8 |  | keep collecting (15/40) |
| pin_lead | 1-0 | 100.0 | 54.5 | 45.5 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move | 73-77-10 | 48.7 | 49.2 | -0.5 | -11.21 | -7.0 |  | no edge shown yet |
| fd_juice | 36-37 | 49.3 | 49.9 | -0.6 | -6.41 | -8.8 |  | no edge shown yet |
| follow_move+pin_price | 0-4 | 0.0 | 33.3 | -33.3 | -4.0 | -100.0 |  | keep collecting (4/40) |
| pin_lead+pin_value | 1-0 | 100.0 | 54.5 | 45.5 | +0.8 | 80.0 |  | redundant -- identical record to pin_lead alone, not independent confirmation |
| follow_move+pin_value | 1-1 | 50.0 | 52.3 | -2.3 | -0.07 | -3.7 |  | keep collecting (2/40) |
| fd_juice+pin_price | 0-1 | 0.0 | 43.4 | -43.4 | -1.0 | -100.0 |  | keep collecting (1/40) |

## By period, market and Pinnacle limit

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 46-42 | 52.3 | 1.6 | -4.0 |
| pin_value | close | 1h|spread | 11-14 | 44.0 | -6.9 | -21.4 |
| pin_value | close | 1h|total | 15-13 | 53.6 | 2.2 | 1.0 |
| pin_value | close | 1h|tt | 20-15 | 57.1 | 7.1 | 4.5 |
| pin_value | close | pin $20k+ | 8-12 | 40.0 | -11.5 | -29.8 |
| pin_value | close | pin $5-20k | 12-11 | 52.2 | 0.7 | -2.7 |
| pin_value | close | pin <$5k | 26-19 | 57.8 | 7.8 | 6.9 |
| pin_price | close | 1h | 3-12 | 20.0 | -21.9 | -57.8 |
| pin_price | close | 1h|ml | 0-7 | 0.0 | -33.3 | -100.0 |
| pin_price | close | 1h|spread | 0-1 | 0.0 | -45.5 | -100.0 |
| pin_price | close | 1h|total | 1-1 | 50.0 | 0.0 | -4.5 |
| pin_price | close | 1h|tt | 2-3 | 40.0 | -10.0 | -11.6 |
| pin_price | close | pin $20k+ | 0-1 | 0.0 | -45.5 | -100.0 |
| pin_price | close | pin $5-20k | 1-8 | 11.1 | -25.9 | -78.8 |
| pin_price | close | pin <$5k | 2-3 | 40.0 | -10.0 | -11.6 |
| pin_lead | close | 1h | 1-0 | 100.0 | 45.5 | 80.0 |
| pin_lead | close | 1h|spread | 1-0 | 100.0 | 45.5 | 80.0 |
| pin_lead | close | pin $20k+ | 1-0 | 100.0 | 45.5 | 80.0 |
| follow_move | close | 1h | 31-33-1 | 48.4 | -1.4 | -8.0 |
| follow_move | close | 1h|ml | 12-11-1 | 52.2 | 4.3 | -4.4 |
| follow_move | close | 1h|spread | 4-4 | 50.0 | 0.0 | -0.5 |
| follow_move | close | 1h|total | 4-6 | 40.0 | -13.9 | -32.1 |
| follow_move | close | 1h|tt | 11-12 | 47.8 | -2.2 | -4.0 |
| follow_move | close | 2h | 30-30-2 | 50.0 | 1.2 | -4.2 |
| follow_move | close | 2h|ml | 9-12-2 | 42.9 | -4.8 | -18.6 |
| follow_move | close | 2h|spread | 4-3 | 57.1 | 6.5 | 9.9 |
| follow_move | close | 2h|total | 9-7 | 56.2 | 7.9 | 9.4 |
| follow_move | close | 2h|tt | 8-8 | 50.0 | 0.0 | -3.4 |
| follow_move | close | pin $20k+ | 4-3 | 57.1 | 4.8 | 4.9 |
| follow_move | close | pin $5-20k | 14-16-1 | 46.7 | -1.5 | -14.9 |
| follow_move | close | pin <$5k | 13-14 | 48.1 | -2.8 | -3.5 |
| follow_move | close | q4 | 12-14-7 | 46.2 | -2.2 | -10.2 |
| follow_move | close | q4|ml | 7-6-7 | 53.8 | 7.7 | -1.2 |
| follow_move | close | q4|spread | 0-2 | 0.0 | -50.0 | -100.0 |
| follow_move | close | q4|total | 5-6 | 45.5 | -5.1 | -10.2 |
| fd_juice | close | 1h | 11-9 | 55.0 | 4.1 | 3.4 |
| fd_juice | close | 1h|spread | 2-3 | 40.0 | -10.9 | -26.7 |
| fd_juice | close | 1h|total | 4-4 | 50.0 | -1.6 | -5.5 |
| fd_juice | close | 1h|tt | 5-2 | 71.4 | 21.4 | 35.0 |
| fd_juice | close | 2h | 17-21 | 44.7 | -5.1 | -17.3 |
| fd_juice | close | 2h|spread | 5-5 | 50.0 | 0.0 | -5.6 |
| fd_juice | close | 2h|total | 2-5 | 28.6 | -20.5 | -44.8 |
| fd_juice | close | 2h|tt | 10-11 | 47.6 | -2.4 | -13.6 |
| fd_juice | close | pin $20k+ | 2-1 | 66.7 | 15.2 | 22.2 |
| fd_juice | close | pin $5-20k | 3-5 | 37.5 | -12.5 | -29.4 |
| fd_juice | close | pin <$5k | 6-3 | 66.7 | 15.2 | 26.2 |
| fd_juice | close | q4 | 8-7 | 53.3 | 4.5 | -3.5 |
| fd_juice | close | q4|spread | 3-4 | 42.9 | -6.5 | -21.8 |
| fd_juice | close | q4|total | 5-3 | 62.5 | 14.1 | 12.5 |
| follow_move+pin_price | close | 1h | 0-4 | 0.0 | -33.3 | -100.0 |
| pin_lead+pin_value | close | 1h | 1-0 | 100.0 | 45.5 | 80.0 |
| follow_move+pin_value | close | 1h | 1-1 | 50.0 | -2.3 | -3.7 |
| fd_juice+pin_price | close | 1h | 0-1 | 0.0 | -43.4 | -100.0 |
| follow_move+pin_price | close | 1h|ml | 0-4 | 0.0 | -33.3 | -100.0 |
| pin_lead+pin_value | close | 1h|spread | 1-0 | 100.0 | 45.5 | 80.0 |
| follow_move+pin_value | close | 1h|spread | 0-1 | 0.0 | -54.5 | -100.0 |
| fd_juice+pin_price | close | 1h|total | 0-1 | 0.0 | -43.4 | -100.0 |
| follow_move+pin_value | close | 1h|tt | 1-0 | 100.0 | 50.0 | 92.6 |
| pin_lead+pin_value | close | pin $20k+ | 1-0 | 100.0 | 45.5 | 80.0 |
| follow_move+pin_value | close | pin $20k+ | 0-1 | 0.0 | -54.5 | -100.0 |
| follow_move+pin_price | close | pin $5-20k | 0-4 | 0.0 | -33.3 | -100.0 |
| fd_juice+pin_price | close | pin $5-20k | 0-1 | 0.0 | -43.4 | -100.0 |
| follow_move+pin_value | close | pin <$5k | 1-0 | 100.0 | 50.0 | 92.6 |
| pin_value | early | 1h | 20-16 | 55.6 | 4.9 | 2.9 |
| pin_value | early | 1h|spread | 6-4 | 60.0 | 9.1 | 9.7 |
| pin_value | early | 1h|total | 7-7 | 50.0 | -0.9 | -4.8 |
| pin_value | early | 1h|tt | 7-5 | 58.3 | 8.3 | 6.2 |
| pin_value | early | pin $20k+ | 0-3 | 0.0 | -48.5 | -100.0 |
| pin_value | early | pin $5-20k | 1-3 | 25.0 | -25.0 | -50.0 |
| pin_value | early | pin <$5k | 19-10 | 65.5 | 14.6 | 20.8 |
| pin_price | early | 1h | 3-8 | 27.3 | -17.2 | -35.0 |
| pin_price | early | 1h|ml | 1-4 | 20.0 | -20.0 | -39.0 |
| pin_price | early | 1h|spread | 0-1 | 0.0 | -45.5 | -100.0 |
| pin_price | early | 1h|total | 1-0 | 100.0 | 56.6 | 110.0 |
| pin_price | early | 1h|tt | 1-3 | 25.0 | -25.0 | -50.0 |
| pin_price | early | pin $5-20k | 2-0 | 100.0 | 61.6 | 157.5 |
| pin_price | early | pin <$5k | 1-8 | 11.1 | -34.7 | -77.8 |
| follow_move | early | 1h | 7-10 | 41.2 | -8.0 | -25.0 |
| follow_move | early | 1h|ml | 4-4 | 50.0 | 4.2 | -15.4 |
| follow_move | early | 1h|total | 1-2 | 33.3 | -23.2 | -36.4 |
| follow_move | early | 1h|tt | 2-4 | 33.3 | -16.7 | -32.0 |
| follow_move | early | 2h | 9-5 | 64.3 | 16.2 | 28.0 |
| follow_move | early | 2h|ml | 4-2 | 66.7 | 16.7 | 39.1 |
| follow_move | early | 2h|total | 3-1 | 75.0 | 31.6 | 45.3 |
| follow_move | early | 2h|tt | 2-2 | 50.0 | 0.0 | -5.7 |
| follow_move | early | pin <$5k | 7-9 | 43.8 | -6.4 | -20.3 |
| follow_move | early | q4 | 3-4-1 | 42.9 | -1.2 | -15.0 |
| follow_move | early | q4|ml | 2-2-1 | 50.0 | 8.3 | -4.8 |
| follow_move | early | q4|spread | 0-1 | 0.0 | -54.5 | -100.0 |
| follow_move | early | q4|total | 1-1 | 50.0 | 6.6 | 2.0 |
| fd_juice | early | 1h | 4-3 | 57.1 | 7.1 | 5.7 |
| fd_juice | early | 1h|spread | 2-0 | 100.0 | 50.0 | 89.2 |
| fd_juice | early | 1h|total | 0-2 | 0.0 | -50.0 | -100.0 |
| fd_juice | early | 1h|tt | 2-1 | 66.7 | 16.7 | 20.6 |
| fd_juice | early | 2h | 4-2 | 66.7 | 18.9 | 21.8 |
| fd_juice | early | 2h|spread | 1-1 | 50.0 | 0.0 | -4.5 |
| fd_juice | early | 2h|total | 2-0 | 100.0 | 56.6 | 81.7 |
| fd_juice | early | 2h|tt | 1-1 | 50.0 | 0.0 | -11.5 |
| fd_juice | early | pin <$5k | 3-3 | 50.0 | 0.8 | -7.2 |
| fd_juice | early | q4 | 1-0 | 100.0 | 56.6 | 98.0 |
| fd_juice | early | q4|total | 1-0 | 100.0 | 56.6 | 98.0 |
| follow_move+pin_price | early | 1h | 0-2 | 0.0 | -33.3 | -100.0 |
| fd_juice+pin_value | early | 1h | 1-0 | 100.0 | 50.0 | 61.7 |
| fd_juice+pin_price | early | 1h | 1-0 | 100.0 | 50.0 | 100.0 |
| follow_move+pin_value | early | 1h | 0-1 | 0.0 | -50.0 | -100.0 |
| follow_move+pin_price | early | 1h|ml | 0-2 | 0.0 | -33.3 | -100.0 |
| fd_juice+pin_value | early | 1h|tt | 1-0 | 100.0 | 50.0 | 61.7 |
| fd_juice+pin_price | early | 1h|tt | 1-0 | 100.0 | 50.0 | 100.0 |
| follow_move+pin_value | early | 1h|tt | 0-1 | 0.0 | -50.0 | -100.0 |
| follow_move+pin_price | early | pin <$5k | 0-2 | 0.0 | -33.3 | -100.0 |
| fd_juice+pin_value | early | pin <$5k | 1-0 | 100.0 | 50.0 | 61.7 |
| fd_juice+pin_price | early | pin <$5k | 1-0 | 100.0 | 50.0 | 100.0 |
| follow_move+pin_value | early | pin <$5k | 0-1 | 0.0 | -50.0 | -100.0 |
