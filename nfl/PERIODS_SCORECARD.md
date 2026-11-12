# NFL period scorecard — halves, quarters, team totals

Generated 2026-11-12 21:54 UTC. 201 graded period markets.

Action Network serves no periods, so these lines come from the FanDuel event
feed and Pinnacle's `s;1;*` keys. **There are no tickets/money splits on any
period market**, so every signal here is handicap or price. Pinnacle's `s;3;*`
keys are excluded: tested against realised quarter scores they fit Q1 and Q3
about equally, so quarters are graded off FanDuel alone rather than guessed.
Everything settles from the boxscore linescore.

Base rates on this sample:

- **spread**: default side won 51.3% (n=39)
- **total**: default side won 34.6% (n=52)
- **ml**: default side won 73.2% (n=41)
- **tt**: default side won 47.6% (n=63)

Proposals appear at 40 decided markets. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 8-13 | 38.1 | 52.7 | -14.6 | -6.26 | -29.8 | 0.14 | keep collecting (21/40) |
| pin_price | 2-7 | 22.2 | 44.1 | -21.9 | -3.85 | -42.8 | 0.36 | keep collecting (9/40) |
| follow_move | 6-9 | 40.0 | 42.8 | -2.8 | -3.44 | -23.0 | 0.42 | keep collecting (15/40) |
| fd_juice | 3-2 | 60.0 | 53.8 | 6.2 | +0.48 | 9.6 | 0.4 | keep collecting (5/40) |
| follow_move+pin_price | 0-2 | 0.0 | 26.8 | -26.8 | -2.0 | -100.0 | -0.35 | keep collecting (2/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 52.4 | 47.6 | +0.62 | 61.7 | 1.0 | keep collecting (1/40) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 31-32 | 49.2 | 51.6 | -2.4 | -6.14 | -9.8 |  | no edge shown yet |
| pin_price | 3-10 | 23.1 | 41.1 | -18.1 | -6.67 | -51.3 |  | keep collecting (13/40) |
| pin_lead | 1-0 | 100.0 | 48.7 | 51.3 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move | 49-50-6 | 49.5 | 48.3 | 1.2 | -5.28 | -5.0 |  | no edge shown yet |
| fd_juice | 27-23 | 54.0 | 49.6 | 4.4 | +0.05 | 0.1 |  | no edge shown yet |
| follow_move+pin_price | 0-3 | 0.0 | 26.8 | -26.8 | -3.0 | -100.0 |  | keep collecting (3/40) |
| pin_lead+pin_value | 1-0 | 100.0 | 48.7 | 51.3 | +0.8 | 80.0 |  | redundant -- identical record to pin_lead alone, not independent confirmation |
| follow_move+pin_value | 1-1 | 50.0 | 50.5 | -0.5 | -0.07 | -3.7 |  | keep collecting (2/40) |

## By period, market and Pinnacle limit

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 31-32 | 49.2 | -2.4 | -9.8 |
| pin_value | close | 1h|spread | 5-11 | 31.2 | -18.6 | -46.8 |
| pin_value | close | 1h|total | 12-10 | 54.5 | 0.3 | 3.0 |
| pin_value | close | 1h|tt | 14-11 | 56.0 | 5.5 | 2.7 |
| pin_value | close | pin $20k+ | 6-11 | 35.3 | -15.5 | -38.7 |
| pin_value | close | pin $5-20k | 5-6 | 45.5 | -11.5 | -16.0 |
| pin_value | close | pin <$5k | 20-15 | 57.1 | 6.8 | 6.3 |
| pin_price | close | 1h | 3-10 | 23.1 | -18.1 | -51.3 |
| pin_price | close | 1h|ml | 0-6 | 0.0 | -26.8 | -100.0 |
| pin_price | close | 1h|spread | 0-1 | 0.0 | -51.3 | -100.0 |
| pin_price | close | 1h|total | 1-0 | 100.0 | 34.6 | 90.9 |
| pin_price | close | 1h|tt | 2-3 | 40.0 | -11.4 | -11.6 |
| pin_price | close | pin $20k+ | 0-1 | 0.0 | -51.3 | -100.0 |
| pin_price | close | pin $5-20k | 1-6 | 14.3 | -18.1 | -72.7 |
| pin_price | close | pin <$5k | 2-3 | 40.0 | -11.4 | -11.6 |
| pin_lead | close | 1h | 1-0 | 100.0 | 51.3 | 80.0 |
| pin_lead | close | 1h|spread | 1-0 | 100.0 | 51.3 | 80.0 |
| pin_lead | close | pin $20k+ | 1-0 | 100.0 | 51.3 | 80.0 |
| follow_move | close | 1h | 22-22-1 | 50.0 | -2.1 | -3.6 |
| follow_move | close | 1h|ml | 8-6-1 | 57.1 | 7.1 | 8.8 |
| follow_move | close | 1h|spread | 3-3 | 50.0 | 0.0 | -1.5 |
| follow_move | close | 1h|total | 3-4 | 42.9 | -18.1 | -29.2 |
| follow_move | close | 1h|tt | 8-9 | 47.1 | -3.9 | -4.6 |
| follow_move | close | 2h | 19-19-1 | 50.0 | 4.4 | -4.7 |
| follow_move | close | 2h|ml | 5-9-1 | 35.7 | -7.7 | -32.6 |
| follow_move | close | 2h|spread | 3-2 | 60.0 | 10.3 | 16.4 |
| follow_move | close | 2h|total | 6-4 | 60.0 | 16.2 | 16.4 |
| follow_move | close | 2h|tt | 5-4 | 55.6 | 6.9 | 6.8 |
| follow_move | close | pin $20k+ | 4-3 | 57.1 | 3.8 | 4.9 |
| follow_move | close | pin $5-20k | 8-8-1 | 50.0 | 0.5 | -6.6 |
| follow_move | close | pin <$5k | 10-11 | 47.6 | -6.1 | -3.9 |
| follow_move | close | q4 | 8-9-4 | 47.1 | 2.6 | -8.8 |
| follow_move | close | q4|ml | 5-5-4 | 50.0 | 9.3 | -5.3 |
| follow_move | close | q4|spread | 0-1 | 0.0 | -48.7 | -100.0 |
| follow_move | close | q4|total | 3-3 | 50.0 | 0.0 | -1.9 |
| fd_juice | close | 1h | 10-2 | 83.3 | 30.7 | 56.4 |
| fd_juice | close | 1h|spread | 2-1 | 66.7 | 17.1 | 22.2 |
| fd_juice | close | 1h|total | 3-1 | 75.0 | 17.3 | 41.3 |
| fd_juice | close | 1h|tt | 5-0 | 100.0 | 49.5 | 89.0 |
| fd_juice | close | 2h | 12-15 | 44.4 | -4.2 | -17.6 |
| fd_juice | close | 2h|spread | 3-4 | 42.9 | -7.0 | -19.7 |
| fd_juice | close | 2h|total | 2-4 | 33.3 | -11.5 | -35.7 |
| fd_juice | close | 2h|tt | 7-7 | 50.0 | 0.3 | -8.7 |
| fd_juice | close | pin $20k+ | 2-1 | 66.7 | 17.1 | 22.2 |
| fd_juice | close | pin $5-20k | 2-0 | 100.0 | 50.0 | 87.1 |
| fd_juice | close | pin <$5k | 6-1 | 85.7 | 31.0 | 62.3 |
| fd_juice | close | q4 | 5-6 | 45.5 | -3.1 | -17.9 |
| fd_juice | close | q4|spread | 3-3 | 50.0 | 0.0 | -8.8 |
| fd_juice | close | q4|total | 2-3 | 40.0 | -6.9 | -28.8 |
| follow_move+pin_price | close | 1h | 0-3 | 0.0 | -26.8 | -100.0 |
| pin_lead+pin_value | close | 1h | 1-0 | 100.0 | 51.3 | 80.0 |
| follow_move+pin_value | close | 1h | 1-1 | 50.0 | -0.5 | -3.7 |
| follow_move+pin_price | close | 1h|ml | 0-3 | 0.0 | -26.8 | -100.0 |
| pin_lead+pin_value | close | 1h|spread | 1-0 | 100.0 | 51.3 | 80.0 |
| follow_move+pin_value | close | 1h|spread | 0-1 | 0.0 | -48.7 | -100.0 |
| follow_move+pin_value | close | 1h|tt | 1-0 | 100.0 | 47.6 | 92.6 |
| pin_lead+pin_value | close | pin $20k+ | 1-0 | 100.0 | 51.3 | 80.0 |
| follow_move+pin_value | close | pin $20k+ | 0-1 | 0.0 | -48.7 | -100.0 |
| follow_move+pin_price | close | pin $5-20k | 0-3 | 0.0 | -26.8 | -100.0 |
| follow_move+pin_value | close | pin <$5k | 1-0 | 100.0 | 47.6 | 92.6 |
| pin_value | early | 1h | 8-13 | 38.1 | -14.6 | -29.8 |
| pin_value | early | 1h|spread | 1-3 | 25.0 | -25.0 | -54.2 |
| pin_value | early | 1h|total | 3-6 | 33.3 | -21.8 | -35.4 |
| pin_value | early | 1h|tt | 4-4 | 50.0 | -1.2 | -11.4 |
| pin_value | early | pin $20k+ | 0-3 | 0.0 | -50.4 | -100.0 |
| pin_value | early | pin $5-20k | 1-3 | 25.0 | -25.0 | -50.0 |
| pin_value | early | pin <$5k | 7-7 | 50.0 | -3.9 | -9.0 |
| pin_price | early | 1h | 2-7 | 22.2 | -21.9 | -42.8 |
| pin_price | early | 1h|ml | 1-3 | 25.0 | -13.4 | -23.8 |
| pin_price | early | 1h|spread | 0-1 | 0.0 | -51.3 | -100.0 |
| pin_price | early | 1h|total | 1-0 | 100.0 | 65.4 | 110.0 |
| pin_price | early | 1h|tt | 0-3 | 0.0 | -52.4 | -100.0 |
| pin_price | early | pin $5-20k | 2-0 | 100.0 | 69.3 | 157.5 |
| pin_price | early | pin <$5k | 0-7 | 0.0 | -47.9 | -100.0 |
| follow_move | early | 1h | 2-3 | 40.0 | -4.4 | -27.4 |
| follow_move | early | 1h|ml | 1-2 | 33.3 | -8.9 | -43.8 |
| follow_move | early | 1h|tt | 1-1 | 50.0 | 2.4 | -2.9 |
| follow_move | early | 2h | 3-3 | 50.0 | 9.4 | 2.5 |
| follow_move | early | 2h|ml | 2-1 | 66.7 | 24.4 | 39.9 |
| follow_move | early | 2h|total | 1-1 | 50.0 | 15.4 | -2.4 |
| follow_move | early | 2h|tt | 0-1 | 0.0 | -47.6 | -100.0 |
| follow_move | early | pin <$5k | 2-3 | 40.0 | -4.4 | -27.4 |
| follow_move | early | q4 | 1-3 | 25.0 | -18.9 | -55.5 |
| follow_move | early | q4|ml | 1-2 | 33.3 | -8.9 | -40.6 |
| follow_move | early | q4|spread | 0-1 | 0.0 | -48.7 | -100.0 |
| fd_juice | early | 1h | 2-1 | 66.7 | 10.3 | 19.0 |
| fd_juice | early | 1h|spread | 1-0 | 100.0 | 48.7 | 95.2 |
| fd_juice | early | 1h|total | 0-1 | 0.0 | -65.4 | -100.0 |
| fd_juice | early | 1h|tt | 1-0 | 100.0 | 47.6 | 61.7 |
| fd_juice | early | 2h | 1-1 | 50.0 | 0.0 | -4.5 |
| fd_juice | early | 2h|spread | 1-1 | 50.0 | 0.0 | -4.5 |
| fd_juice | early | pin <$5k | 2-1 | 66.7 | 10.3 | 19.0 |
| follow_move+pin_price | early | 1h | 0-2 | 0.0 | -26.8 | -100.0 |
| fd_juice+pin_value | early | 1h | 1-0 | 100.0 | 47.6 | 61.7 |
| follow_move+pin_price | early | 1h|ml | 0-2 | 0.0 | -26.8 | -100.0 |
| fd_juice+pin_value | early | 1h|tt | 1-0 | 100.0 | 47.6 | 61.7 |
| follow_move+pin_price | early | pin <$5k | 0-2 | 0.0 | -26.8 | -100.0 |
| fd_juice+pin_value | early | pin <$5k | 1-0 | 100.0 | 47.6 | 61.7 |
