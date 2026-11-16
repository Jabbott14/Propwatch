# NFL prop scorecard

Generated 2026-11-16 19:53 UTC. 822 graded props (119 had no nflverse result and are not graded).

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

Base rate: the over hit **46.1%** of 822 graded props. `expected %` is
that rate applied to the sides each signal picked; `edge` is hit% minus it.

Proposals appear at 50 decided props. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 17-12 | 58.6 | 49.3 | 9.3 | +2.8 | 9.7 | -0.55 | -0.03 | 0.0 | keep collecting (29/50) |
| pin_price | 4-1 | 80.0 | 49.2 | 30.8 | +2.79 | 55.9 | 0.0 | 0.86 | 60.0 | keep collecting (5/50) |
| fd_move | 17-7 | 70.8 | 50.0 | 20.8 | +7.84 | 32.7 | 3.29 | -0.18 | 0.0 | keep collecting (24/50) |
| fd_juice | 14-4 | 77.8 | 49.6 | 28.2 | +9.79 | 54.4 | -0.06 | 3.86 | 61.1 | keep collecting (18/50) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 141-127 | 52.6 | 49.3 | 3.3 | -4.46 | -1.7 |  |  |  | no edge shown yet |
| pin_price | 39-34 | 53.4 | 49.1 | 4.3 | +4.69 | 6.4 |  |  |  | no edge shown yet |
| fd_move | 240-231 | 51.0 | 50.2 | 0.8 | -13.98 | -3.0 |  |  |  | no edge shown yet |
| fd_juice | 128-102 | 55.7 | 51.0 | 4.7 | +5.08 | 2.2 |  |  |  | no edge shown yet |
| pin_lead | 22-22 | 50.0 | 49.3 | 0.7 | -2.96 | -6.7 |  |  |  | keep collecting (44/50) |
| pin_lead+pin_value | 18-16 | 52.9 | 49.5 | 3.4 | -0.5 | -1.5 |  |  |  | keep collecting (34/50) |
| fd_juice+pin_price | 5-2 | 71.4 | 51.7 | 19.8 | +1.94 | 27.8 |  |  |  | keep collecting (7/50) |
| fd_move+pin_value | 24-17 | 58.5 | 48.8 | 9.8 | +4.24 | 10.3 |  |  |  | keep collecting (41/50) |
| fd_move+pin_price | 10-7 | 58.8 | 49.8 | 9.1 | +3.49 | 20.5 |  |  |  | keep collecting (17/50) |
| fd_juice+pin_lead | 0-1 | 0.0 | 53.9 | -53.9 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 53.9 | -53.9 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |

## By Pinnacle limit and by stat

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | pass_tds | 3-1 | 75.0 | 25.0 | 7.8 |
| pin_value | close | pass_yds | 14-14 | 50.0 | 1.4 | -5.8 |
| pin_value | close | pin $1k+ | 81-67 | 54.7 | 5.9 | 2.0 |
| pin_value | close | pin $400-1k | 55-52 | 51.4 | 1.2 | -3.5 |
| pin_value | close | pin limit <$400 | 5-8 | 38.5 | -9.4 | -27.9 |
| pin_value | close | receptions | 4-4 | 50.0 | 1.0 | -17.5 |
| pin_value | close | recv_yds | 81-68 | 54.4 | 4.7 | 2.5 |
| pin_value | close | rush_yds | 39-40 | 49.4 | 0.4 | -6.9 |
| pin_price | close | pass_tds | 4-2 | 66.7 | 14.1 | 53.8 |
| pin_price | close | pass_yds | 2-4 | 33.3 | -16.7 | -37.2 |
| pin_price | close | pin $1k+ | 20-19 | 51.3 | 2.0 | 2.7 |
| pin_price | close | pin $400-1k | 18-13 | 58.1 | 8.9 | 14.4 |
| pin_price | close | pin limit <$400 | 1-2 | 33.3 | -12.8 | -28.0 |
| pin_price | close | receptions | 13-16 | 44.8 | -3.7 | -7.4 |
| pin_price | close | recv_yds | 12-8 | 60.0 | 12.3 | 13.1 |
| pin_price | close | rush_yds | 8-4 | 66.7 | 16.0 | 26.7 |
| fd_move | close | pass_tds | 0-3 | 0.0 | -53.9 | -100.0 |
| fd_move | close | pass_yds | 21-25 | 45.7 | -5.2 | -13.9 |
| fd_move | close | pin $1k+ | 83-87 | 48.8 | -1.9 | -8.0 |
| fd_move | close | pin $400-1k | 121-116 | 51.1 | 1.2 | -2.2 |
| fd_move | close | pin limit <$400 | 14-14 | 50.0 | 0.8 | -4.5 |
| fd_move | close | receptions | 20-23 | 46.5 | -3.9 | -1.1 |
| fd_move | close | recv_yds | 128-125 | 50.6 | 0.7 | -4.7 |
| fd_move | close | rush_yds | 71-55 | 56.3 | 6.1 | 6.1 |
| fd_juice | close | pass_tds | 17-19 | 47.2 | -2.6 | -6.5 |
| fd_juice | close | pin $1k+ | 46-38 | 54.8 | 3.5 | -1.4 |
| fd_juice | close | pin $400-1k | 70-54 | 56.5 | 5.9 | 4.4 |
| fd_juice | close | pin limit <$400 | 4-3 | 57.1 | 5.5 | -0.1 |
| fd_juice | close | receptions | 105-80 | 56.8 | 5.6 | 3.2 |
| fd_juice | close | recv_yds | 2-2 | 50.0 | -3.9 | -11.9 |
| fd_juice | close | rush_yds | 4-1 | 80.0 | 30.8 | 41.0 |
| pin_lead | close | pass_tds | 1-1 | 50.0 | -3.9 | -27.2 |
| pin_lead | close | pass_yds | 4-4 | 50.0 | -1.0 | -5.8 |
| pin_lead | close | pin $1k+ | 14-9 | 60.9 | 12.1 | 12.9 |
| pin_lead | close | pin $400-1k | 8-13 | 38.1 | -11.7 | -28.2 |
| pin_lead | close | recv_yds | 11-10 | 52.4 | 3.3 | -1.3 |
| pin_lead | close | rush_yds | 6-7 | 46.2 | -1.7 | -13.0 |
| pin_lead+pin_value | close | pass_tds | 1-1 | 50.0 | -3.9 | -27.2 |
| fd_juice+pin_lead | close | pass_tds | 0-1 | 0.0 | -53.9 | -100.0 |
| fd_juice+pin_value | close | pass_tds | 0-1 | 0.0 | -53.9 | -100.0 |
| pin_lead+pin_value | close | pass_yds | 4-3 | 57.1 | 6.6 | 7.7 |
| fd_move+pin_price | close | pass_yds | 1-1 | 50.0 | -3.9 | -5.8 |
| fd_move+pin_value | close | pass_yds | 1-2 | 33.3 | -15.4 | -37.2 |
| pin_lead+pin_value | close | pin $1k+ | 12-7 | 63.2 | 14.6 | 16.8 |
| fd_juice+pin_price | close | pin $1k+ | 2-0 | 100.0 | 50.0 | 76.8 |
| fd_move+pin_value | close | pin $1k+ | 10-8 | 55.6 | 7.3 | 4.7 |
| fd_move+pin_price | close | pin $1k+ | 5-4 | 55.6 | 5.1 | 4.7 |
| pin_lead+pin_value | close | pin $400-1k | 6-9 | 40.0 | -10.8 | -24.6 |
| fd_move+pin_price | close | pin $400-1k | 4-1 | 80.0 | 29.2 | 78.1 |
| fd_juice+pin_price | close | pin $400-1k | 3-2 | 60.0 | 7.7 | 8.1 |
| fd_move+pin_value | close | pin $400-1k | 13-8 | 61.9 | 12.5 | 16.7 |
| fd_juice+pin_lead | close | pin $400-1k | 0-1 | 0.0 | -53.9 | -100.0 |
| fd_juice+pin_value | close | pin $400-1k | 0-1 | 0.0 | -53.9 | -100.0 |
| fd_move+pin_price | close | pin limit <$400 | 1-2 | 33.3 | -12.8 | -28.0 |
| fd_move+pin_value | close | pin limit <$400 | 1-1 | 50.0 | 3.9 | -5.8 |
| fd_juice+pin_price | close | receptions | 5-2 | 71.4 | 19.8 | 27.8 |
| fd_move+pin_price | close | receptions | 2-2 | 50.0 | 1.9 | 35.2 |
| pin_lead+pin_value | close | recv_yds | 10-8 | 55.6 | 6.0 | 4.7 |
| fd_move+pin_value | close | recv_yds | 13-9 | 59.1 | 10.9 | 11.4 |
| fd_move+pin_price | close | recv_yds | 5-4 | 55.6 | 6.9 | 4.7 |
| fd_move+pin_value | close | rush_yds | 10-6 | 62.5 | 13.0 | 17.8 |
| pin_lead+pin_value | close | rush_yds | 3-4 | 42.9 | -4.4 | -19.2 |
| fd_move+pin_price | close | rush_yds | 2-0 | 100.0 | 46.1 | 88.5 |
| pin_value | early | pass_yds | 1-1 | 50.0 | 3.9 | -5.8 |
| pin_value | early | pin $1k+ | 16-7 | 69.6 | 20.4 | 30.1 |
| pin_value | early | pin $400-1k | 0-1 | 0.0 | -46.1 | -100.0 |
| pin_value | early | pin limit <$400 | 1-4 | 20.0 | -30.8 | -62.5 |
| pin_value | early | receptions | 1-0 | 100.0 | 46.1 | 64.9 |
| pin_value | early | recv_yds | 8-6 | 57.1 | 7.1 | 7.7 |
| pin_value | early | rush_yds | 7-5 | 58.3 | 9.6 | 9.9 |
| pin_price | early | pin $1k+ | 4-0 | 100.0 | 50.0 | 94.8 |
| pin_price | early | pin $400-1k | 0-1 | 0.0 | -46.1 | -100.0 |
| pin_price | early | receptions | 3-1 | 75.0 | 25.0 | 41.3 |
| pin_price | early | rush_yds | 1-0 | 100.0 | 53.9 | 114.0 |
| fd_move | early | pass_yds | 3-1 | 75.0 | 23.1 | 40.8 |
| fd_move | early | pin limit <$400 | 2-1 | 66.7 | 15.4 | 25.1 |
| fd_move | early | recv_yds | 7-3 | 70.0 | 20.8 | 30.6 |
| fd_move | early | rush_yds | 7-3 | 70.0 | 20.0 | 31.5 |
| fd_juice | early | pass_tds | 4-0 | 100.0 | 50.0 | 102.5 |
| fd_juice | early | receptions | 9-4 | 69.2 | 20.1 | 37.9 |
| fd_juice | early | recv_yds | 1-0 | 100.0 | 46.1 | 76.9 |
