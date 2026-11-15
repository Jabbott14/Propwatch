# NFL prop scorecard

Generated 2026-11-15 14:21 UTC. 527 graded props (88 had no nflverse result and are not graded).

**Read this on its own scale, not against the side scorecard.** Pinnacle risks
**$75,000** on an NFL side and **$1,000-$3,000** on a prop at kickoff, $250-$500
earlier in the week. The sharpest book in the world is telling you it is 25-75x
less confident in its own prop number. A prop signal must never be sized like a
side signal, and `pin_value` barely fires here because FanDuel's prop handicaps
sit on Pinnacle's almost every time.

There are no tickets/money splits on any prop, so the only channels are the
handicap and the price. `fd_juice` is the money channel: a static handicap whose
price moves 12+ cents one way. Break-even at -110 is 52.4%.

**CLV pts** is handicap movement and is near-blank here, because most prop
numbers never move. **CLV price** is the real one: percentage points of implied
probability gained on the taken side between the early read and the close.

Base rate: the over hit **47.6%** of 527 graded props. `expected %` is
that rate applied to the sides each signal picked; `edge` is hit% minus it.

Proposals appear at 50 decided props. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 17-12 | 58.6 | 49.6 | 9.0 | +2.8 | 9.7 | -0.55 | -0.03 | 0.0 | keep collecting (29/50) |
| pin_price | 4-1 | 80.0 | 49.5 | 30.5 | +2.79 | 55.9 | 0.0 | 0.86 | 60.0 | keep collecting (5/50) |
| fd_move | 12-5 | 70.6 | 50.1 | 20.4 | +5.53 | 32.5 | 4.29 | -0.19 | 0.0 | keep collecting (17/50) |
| fd_juice | 7-2 | 77.8 | 49.7 | 28.0 | +4.68 | 52.0 | 0.0 | 3.33 | 55.6 | keep collecting (9/50) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 98-90 | 52.1 | 49.6 | 2.5 | -5.46 | -2.9 |  |  |  | no edge shown yet |
| pin_price | 29-21 | 58.0 | 49.8 | 8.2 | +8.64 | 17.3 |  |  |  | no edge shown yet |
| fd_move | 130-149 | 46.6 | 50.2 | -3.6 | -31.92 | -11.4 |  |  |  | DROP: below break-even |
| fd_juice | 79-62 | 56.0 | 50.6 | 5.4 | +3.41 | 2.4 |  |  |  | no edge shown yet |
| pin_lead | 17-8 | 68.0 | 49.3 | 18.7 | +6.61 | 26.5 |  |  |  | keep collecting (25/50) |
| pin_lead+pin_value | 13-7 | 65.0 | 49.5 | 15.5 | +4.07 | 20.4 |  |  |  | keep collecting (20/50) |
| fd_juice+pin_price | 4-1 | 80.0 | 52.4 | 27.6 | +1.96 | 39.3 |  |  |  | keep collecting (5/50) |
| fd_move+pin_value | 10-13 | 43.5 | 49.3 | -5.8 | -4.15 | -18.0 |  |  |  | keep collecting (23/50) |
| fd_move+pin_price | 6-4 | 60.0 | 50.9 | 9.1 | +2.95 | 29.5 |  |  |  | keep collecting (10/50) |
| fd_juice+pin_lead | 0-1 | 0.0 | 52.4 | -52.4 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 52.4 | -52.4 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |

## By Pinnacle limit and by stat

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | pass_tds | 3-1 | 75.0 | 25.0 | 7.8 |
| pin_value | close | pass_yds | 8-10 | 44.4 | -4.0 | -16.2 |
| pin_value | close | pin $1k+ | 63-58 | 52.1 | 2.8 | -3.3 |
| pin_value | close | pin $400-1k | 31-29 | 51.7 | 1.3 | -3.3 |
| pin_value | close | pin limit <$400 | 4-3 | 57.1 | 7.5 | 7.7 |
| pin_value | close | receptions | 4-1 | 80.0 | 29.5 | 31.9 |
| pin_value | close | recv_yds | 60-51 | 54.1 | 4.2 | 1.9 |
| pin_value | close | rush_yds | 23-27 | 46.0 | -3.4 | -13.1 |
| pin_price | close | pass_tds | 4-2 | 66.7 | 15.1 | 53.8 |
| pin_price | close | pass_yds | 2-3 | 40.0 | -9.5 | -24.6 |
| pin_price | close | pin $1k+ | 15-13 | 53.6 | 3.6 | 9.1 |
| pin_price | close | pin $400-1k | 13-6 | 68.4 | 18.5 | 36.5 |
| pin_price | close | pin limit <$400 | 1-2 | 33.3 | -14.3 | -28.0 |
| pin_price | close | receptions | 10-10 | 50.0 | 0.5 | 5.0 |
| pin_price | close | recv_yds | 7-4 | 63.6 | 14.7 | 20.0 |
| pin_price | close | rush_yds | 6-2 | 75.0 | 24.4 | 43.0 |
| fd_move | close | pass_tds | 0-2 | 0.0 | -52.4 | -100.0 |
| fd_move | close | pass_yds | 12-16 | 42.9 | -8.3 | -19.2 |
| fd_move | close | pin $1k+ | 53-53 | 50.0 | -0.8 | -5.9 |
| fd_move | close | pin $400-1k | 60-74 | 44.8 | -5.2 | -14.1 |
| fd_move | close | pin limit <$400 | 5-12 | 29.4 | -18.8 | -42.9 |
| fd_move | close | receptions | 8-14 | 36.4 | -14.3 | -21.7 |
| fd_move | close | recv_yds | 69-83 | 45.4 | -4.5 | -14.4 |
| fd_move | close | rush_yds | 41-34 | 54.7 | 4.4 | 2.9 |
| fd_juice | close | pass_tds | 10-12 | 45.5 | -4.8 | -14.2 |
| fd_juice | close | pin $1k+ | 33-28 | 54.1 | 3.4 | -2.8 |
| fd_juice | close | pin $400-1k | 38-28 | 57.6 | 7.3 | 6.2 |
| fd_juice | close | pin limit <$400 | 2-1 | 66.7 | 17.5 | 9.9 |
| fd_juice | close | receptions | 66-47 | 58.4 | 7.8 | 6.2 |
| fd_juice | close | recv_yds | 2-2 | 50.0 | -2.4 | -11.9 |
| fd_juice | close | rush_yds | 1-1 | 50.0 | 0.0 | -1.0 |
| pin_lead | close | pass_tds | 1-1 | 50.0 | -2.4 | -27.2 |
| pin_lead | close | pass_yds | 2-0 | 100.0 | 52.4 | 88.5 |
| pin_lead | close | pin $1k+ | 12-4 | 75.0 | 26.2 | 38.7 |
| pin_lead | close | pin $400-1k | 5-4 | 55.6 | 5.3 | 4.7 |
| pin_lead | close | recv_yds | 10-4 | 71.4 | 21.8 | 34.6 |
| pin_lead | close | rush_yds | 4-3 | 57.1 | 8.8 | 7.7 |
| pin_lead+pin_value | close | pass_tds | 1-1 | 50.0 | -2.4 | -27.2 |
| fd_juice+pin_lead | close | pass_tds | 0-1 | 0.0 | -52.4 | -100.0 |
| fd_juice+pin_value | close | pass_tds | 0-1 | 0.0 | -52.4 | -100.0 |
| pin_lead+pin_value | close | pass_yds | 2-0 | 100.0 | 52.4 | 88.5 |
| fd_move+pin_price | close | pass_yds | 1-1 | 50.0 | -2.4 | -5.8 |
| fd_move+pin_value | close | pass_yds | 0-2 | 0.0 | -50.0 | -100.0 |
| pin_lead+pin_value | close | pin $1k+ | 10-4 | 71.4 | 22.4 | 31.6 |
| fd_juice+pin_price | close | pin $1k+ | 1-0 | 100.0 | 47.6 | 55.6 |
| fd_move+pin_value | close | pin $1k+ | 6-6 | 50.0 | 0.8 | -5.8 |
| fd_move+pin_price | close | pin $1k+ | 2-2 | 50.0 | -2.4 | -5.8 |
| pin_lead+pin_value | close | pin $400-1k | 3-3 | 50.0 | -0.8 | -5.7 |
| fd_move+pin_price | close | pin $400-1k | 3-0 | 100.0 | 47.6 | 134.0 |
| fd_juice+pin_price | close | pin $400-1k | 3-1 | 75.0 | 22.6 | 35.2 |
| fd_move+pin_value | close | pin $400-1k | 3-6 | 33.3 | -16.4 | -37.2 |
| fd_juice+pin_lead | close | pin $400-1k | 0-1 | 0.0 | -52.4 | -100.0 |
| fd_juice+pin_value | close | pin $400-1k | 0-1 | 0.0 | -52.4 | -100.0 |
| fd_move+pin_price | close | pin limit <$400 | 1-2 | 33.3 | -14.3 | -28.0 |
| fd_move+pin_value | close | pin limit <$400 | 1-1 | 50.0 | 2.4 | -5.8 |
| fd_juice+pin_price | close | receptions | 4-1 | 80.0 | 27.6 | 39.3 |
| fd_move+pin_price | close | receptions | 2-1 | 66.7 | 17.5 | 80.3 |
| pin_lead+pin_value | close | recv_yds | 9-4 | 69.2 | 19.4 | 30.5 |
| fd_move+pin_value | close | recv_yds | 5-7 | 41.7 | -7.1 | -21.5 |
| fd_move+pin_price | close | recv_yds | 1-2 | 33.3 | -17.5 | -37.2 |
| fd_move+pin_value | close | rush_yds | 5-4 | 55.6 | 5.8 | 4.7 |
| pin_lead+pin_value | close | rush_yds | 1-2 | 33.3 | -14.3 | -37.2 |
| fd_move+pin_price | close | rush_yds | 2-0 | 100.0 | 47.6 | 88.5 |
| pin_value | early | pass_yds | 1-1 | 50.0 | 2.4 | -5.8 |
| pin_value | early | pin $1k+ | 16-7 | 69.6 | 20.1 | 30.1 |
| pin_value | early | pin $400-1k | 0-1 | 0.0 | -47.6 | -100.0 |
| pin_value | early | pin limit <$400 | 1-4 | 20.0 | -30.5 | -62.5 |
| pin_value | early | receptions | 1-0 | 100.0 | 47.6 | 64.9 |
| pin_value | early | recv_yds | 8-6 | 57.1 | 7.1 | 7.7 |
| pin_value | early | rush_yds | 7-5 | 58.3 | 9.1 | 9.9 |
| pin_price | early | pin $1k+ | 4-0 | 100.0 | 50.0 | 94.8 |
| pin_price | early | pin $400-1k | 0-1 | 0.0 | -47.6 | -100.0 |
| pin_price | early | receptions | 3-1 | 75.0 | 25.0 | 41.3 |
| pin_price | early | rush_yds | 1-0 | 100.0 | 52.4 | 114.0 |
| fd_move | early | pass_yds | 3-1 | 75.0 | 23.8 | 40.8 |
| fd_move | early | pin limit <$400 | 2-1 | 66.7 | 15.9 | 25.1 |
| fd_move | early | recv_yds | 4-2 | 66.7 | 17.5 | 25.1 |
| fd_move | early | rush_yds | 5-2 | 71.4 | 21.1 | 34.2 |
| fd_juice | early | pass_tds | 2-0 | 100.0 | 47.6 | 79.8 |
| fd_juice | early | receptions | 4-2 | 66.7 | 18.2 | 38.6 |
| fd_juice | early | recv_yds | 1-0 | 100.0 | 47.6 | 76.9 |
