# NFL period scorecard — halves, quarters, team totals

Generated 2026-11-13 17:22 UTC. 211 graded period markets.

Action Network serves no periods, so these lines come from the FanDuel event
feed and Pinnacle's `s;1;*` keys. **There are no tickets/money splits on any
period market**, so every signal here is handicap or price. Pinnacle's `s;3;*`
keys are excluded: tested against realised quarter scores they fit Q1 and Q3
about equally, so quarters are graded off FanDuel alone rather than guessed.
Everything settles from the boxscore linescore.

Base rates on this sample:

- **spread**: default side won 50.0% (n=40)
- **total**: default side won 36.4% (n=55)
- **ml**: default side won 71.4% (n=42)
- **tt**: default side won 49.3% (n=67)

Proposals appear at 40 decided markets. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 10-13 | 43.5 | 52.5 | -9.0 | -4.59 | -19.9 | 0.22 | keep collecting (23/40) |
| pin_price | 2-7 | 22.2 | 44.0 | -21.7 | -3.85 | -42.8 | 0.36 | keep collecting (9/40) |
| follow_move | 6-9 | 40.0 | 43.7 | -3.7 | -3.44 | -23.0 | 0.42 | keep collecting (15/40) |
| fd_juice | 3-2 | 60.0 | 52.9 | 7.1 | +0.48 | 9.6 | 0.4 | keep collecting (5/40) |
| follow_move+pin_price | 0-2 | 0.0 | 28.6 | -28.6 | -2.0 | -100.0 | -0.35 | keep collecting (2/40) |
| fd_juice+pin_value | 1-0 | 100.0 | 50.7 | 49.3 | +0.62 | 61.7 | 1.0 | keep collecting (1/40) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 33-34 | 49.3 | 51.1 | -1.8 | -6.72 | -10.0 |  | no edge shown yet |
| pin_price | 3-10 | 23.1 | 41.3 | -18.3 | -6.67 | -51.3 |  | keep collecting (13/40) |
| pin_lead | 1-0 | 100.0 | 50.0 | 50.0 | +0.8 | 80.0 |  | keep collecting (1/40) |
| follow_move | 52-54-7 | 49.1 | 48.7 | 0.3 | -6.24 | -5.5 |  | no edge shown yet |
| fd_juice | 27-24 | 52.9 | 49.7 | 3.2 | -0.95 | -1.9 |  | no edge shown yet |
| follow_move+pin_price | 0-3 | 0.0 | 28.6 | -28.6 | -3.0 | -100.0 |  | keep collecting (3/40) |
| pin_lead+pin_value | 1-0 | 100.0 | 50.0 | 50.0 | +0.8 | 80.0 |  | redundant -- identical record to pin_lead alone, not independent confirmation |
| follow_move+pin_value | 1-1 | 50.0 | 50.4 | -0.4 | -0.07 | -3.7 |  | keep collecting (2/40) |

## By period, market and Pinnacle limit

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 33-34 | 49.3 | -1.8 | -10.0 |
| pin_value | close | 1h|spread | 6-11 | 35.3 | -14.7 | -39.7 |
| pin_value | close | 1h|total | 12-11 | 52.2 | -0.8 | -1.5 |
| pin_value | close | 1h|tt | 15-12 | 55.6 | 5.5 | 1.3 |
| pin_value | close | pin $20k+ | 7-11 | 38.9 | -11.9 | -32.4 |
| pin_value | close | pin $5-20k | 5-7 | 41.7 | -12.9 | -23.0 |
| pin_value | close | pin <$5k | 21-16 | 56.8 | 6.7 | 5.1 |
| pin_price | close | 1h | 3-10 | 23.1 | -18.3 | -51.3 |
| pin_price | close | 1h|ml | 0-6 | 0.0 | -28.6 | -100.0 |
| pin_price | close | 1h|spread | 0-1 | 0.0 | -50.0 | -100.0 |
| pin_price | close | 1h|total | 1-0 | 100.0 | 36.4 | 90.9 |
| pin_price | close | 1h|tt | 2-3 | 40.0 | -10.4 | -11.6 |
| pin_price | close | pin $20k+ | 0-1 | 0.0 | -50.0 | -100.0 |
| pin_price | close | pin $5-20k | 1-6 | 14.3 | -19.3 | -72.7 |
| pin_price | close | pin <$5k | 2-3 | 40.0 | -10.4 | -11.6 |
| pin_lead | close | 1h | 1-0 | 100.0 | 50.0 | 80.0 |
| pin_lead | close | 1h|spread | 1-0 | 100.0 | 50.0 | 80.0 |
| pin_lead | close | pin $20k+ | 1-0 | 100.0 | 50.0 | 80.0 |
| follow_move | close | 1h | 25-23-1 | 52.1 | 0.7 | 0.9 |
| follow_move | close | 1h|ml | 9-6-1 | 60.0 | 11.4 | 14.2 |
| follow_move | close | 1h|spread | 3-3 | 50.0 | 0.0 | -1.5 |
| follow_move | close | 1h|total | 4-4 | 50.0 | -10.2 | -15.1 |
| follow_move | close | 1h|tt | 9-10 | 47.4 | -3.0 | -2.9 |
| follow_move | close | 2h | 19-21-2 | 47.5 | 0.7 | -9.1 |
| follow_move | close | 2h|ml | 5-9-2 | 35.7 | -8.2 | -30.6 |
| follow_move | close | 2h|spread | 3-2 | 60.0 | 10.0 | 16.4 |
| follow_move | close | 2h|total | 6-5 | 54.5 | 8.3 | 5.8 |
| follow_move | close | 2h|tt | 5-5 | 50.0 | 0.3 | -3.9 |
| follow_move | close | pin $20k+ | 4-3 | 57.1 | 4.1 | 4.9 |
| follow_move | close | pin $5-20k | 10-8-1 | 55.6 | 6.4 | 3.5 |
| follow_move | close | pin <$5k | 11-12 | 47.8 | -4.8 | -2.5 |
| follow_move | close | q4 | 8-10-4 | 44.4 | -1.6 | -13.0 |
| follow_move | close | q4|ml | 5-5-4 | 50.0 | 8.6 | -5.3 |
| follow_move | close | q4|spread | 0-1 | 0.0 | -50.0 | -100.0 |
| follow_move | close | q4|total | 3-4 | 42.9 | -9.1 | -15.9 |
| fd_juice | close | 1h | 10-2 | 83.3 | 31.0 | 56.4 |
| fd_juice | close | 1h|spread | 2-1 | 66.7 | 16.7 | 22.2 |
| fd_juice | close | 1h|total | 3-1 | 75.0 | 18.2 | 41.3 |
| fd_juice | close | 1h|tt | 5-0 | 100.0 | 49.9 | 89.0 |
| fd_juice | close | 2h | 12-16 | 42.9 | -6.1 | -20.5 |
| fd_juice | close | 2h|spread | 3-4 | 42.9 | -7.1 | -19.7 |
| fd_juice | close | 2h|total | 2-4 | 33.3 | -12.1 | -35.7 |
| fd_juice | close | 2h|tt | 7-8 | 46.7 | -3.3 | -14.8 |
| fd_juice | close | pin $20k+ | 2-1 | 66.7 | 16.7 | 22.2 |
| fd_juice | close | pin $5-20k | 2-0 | 100.0 | 50.0 | 87.1 |
| fd_juice | close | pin <$5k | 6-1 | 85.7 | 31.7 | 62.3 |
| fd_juice | close | q4 | 5-6 | 45.5 | -3.3 | -17.9 |
| fd_juice | close | q4|spread | 3-3 | 50.0 | 0.0 | -8.8 |
| fd_juice | close | q4|total | 2-3 | 40.0 | -7.3 | -28.8 |
| follow_move+pin_price | close | 1h | 0-3 | 0.0 | -28.6 | -100.0 |
| pin_lead+pin_value | close | 1h | 1-0 | 100.0 | 50.0 | 80.0 |
| follow_move+pin_value | close | 1h | 1-1 | 50.0 | -0.4 | -3.7 |
| follow_move+pin_price | close | 1h|ml | 0-3 | 0.0 | -28.6 | -100.0 |
| pin_lead+pin_value | close | 1h|spread | 1-0 | 100.0 | 50.0 | 80.0 |
| follow_move+pin_value | close | 1h|spread | 0-1 | 0.0 | -50.0 | -100.0 |
| follow_move+pin_value | close | 1h|tt | 1-0 | 100.0 | 49.3 | 92.6 |
| pin_lead+pin_value | close | pin $20k+ | 1-0 | 100.0 | 50.0 | 80.0 |
| follow_move+pin_value | close | pin $20k+ | 0-1 | 0.0 | -50.0 | -100.0 |
| follow_move+pin_price | close | pin $5-20k | 0-3 | 0.0 | -28.6 | -100.0 |
| follow_move+pin_value | close | pin <$5k | 1-0 | 100.0 | 49.3 | 92.6 |
| pin_value | early | 1h | 10-13 | 43.5 | -9.0 | -19.9 |
| pin_value | early | 1h|spread | 2-3 | 40.0 | -10.0 | -28.0 |
| pin_value | early | 1h|total | 4-6 | 40.0 | -15.5 | -22.7 |
| pin_value | early | 1h|tt | 4-4 | 50.0 | -0.4 | -11.4 |
| pin_value | early | pin $20k+ | 0-3 | 0.0 | -50.0 | -100.0 |
| pin_value | early | pin $5-20k | 1-3 | 25.0 | -25.0 | -50.0 |
| pin_value | early | pin <$5k | 9-7 | 56.2 | 2.7 | 2.6 |
| pin_price | early | 1h | 2-7 | 22.2 | -21.7 | -42.8 |
| pin_price | early | 1h|ml | 1-3 | 25.0 | -14.3 | -23.8 |
| pin_price | early | 1h|spread | 0-1 | 0.0 | -50.0 | -100.0 |
| pin_price | early | 1h|total | 1-0 | 100.0 | 63.6 | 110.0 |
| pin_price | early | 1h|tt | 0-3 | 0.0 | -50.7 | -100.0 |
| pin_price | early | pin $5-20k | 2-0 | 100.0 | 67.5 | 157.5 |
| pin_price | early | pin <$5k | 0-7 | 0.0 | -47.3 | -100.0 |
| follow_move | early | 1h | 2-3 | 40.0 | -5.4 | -27.4 |
| follow_move | early | 1h|ml | 1-2 | 33.3 | -9.5 | -43.8 |
| follow_move | early | 1h|tt | 1-1 | 50.0 | 0.7 | -2.9 |
| follow_move | early | 2h | 3-3 | 50.0 | 8.2 | 2.5 |
| follow_move | early | 2h|ml | 2-1 | 66.7 | 23.8 | 39.9 |
| follow_move | early | 2h|total | 1-1 | 50.0 | 13.6 | -2.4 |
| follow_move | early | 2h|tt | 0-1 | 0.0 | -49.3 | -100.0 |
| follow_move | early | pin <$5k | 2-3 | 40.0 | -5.4 | -27.4 |
| follow_move | early | q4 | 1-3 | 25.0 | -19.6 | -55.5 |
| follow_move | early | q4|ml | 1-2 | 33.3 | -9.5 | -40.6 |
| follow_move | early | q4|spread | 0-1 | 0.0 | -50.0 | -100.0 |
| fd_juice | early | 1h | 2-1 | 66.7 | 11.9 | 19.0 |
| fd_juice | early | 1h|spread | 1-0 | 100.0 | 50.0 | 95.2 |
| fd_juice | early | 1h|total | 0-1 | 0.0 | -63.6 | -100.0 |
| fd_juice | early | 1h|tt | 1-0 | 100.0 | 49.3 | 61.7 |
| fd_juice | early | 2h | 1-1 | 50.0 | 0.0 | -4.5 |
| fd_juice | early | 2h|spread | 1-1 | 50.0 | 0.0 | -4.5 |
| fd_juice | early | pin <$5k | 2-1 | 66.7 | 11.9 | 19.0 |
| follow_move+pin_price | early | 1h | 0-2 | 0.0 | -28.6 | -100.0 |
| fd_juice+pin_value | early | 1h | 1-0 | 100.0 | 49.3 | 61.7 |
| follow_move+pin_price | early | 1h|ml | 0-2 | 0.0 | -28.6 | -100.0 |
| fd_juice+pin_value | early | 1h|tt | 1-0 | 100.0 | 49.3 | 61.7 |
| follow_move+pin_price | early | pin <$5k | 0-2 | 0.0 | -28.6 | -100.0 |
| fd_juice+pin_value | early | pin <$5k | 1-0 | 100.0 | 49.3 | 61.7 |
