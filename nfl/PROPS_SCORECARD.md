# NFL prop scorecard

Generated 2026-11-15 23:11 UTC. 725 graded props (216 had no nflverse result and are not graded).

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

Base rate: the over hit **46.5%** of 725 graded props. `expected %` is
that rate applied to the sides each signal picked; `edge` is hit% minus it.

Proposals appear at 50 decided props. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 17-12 | 58.6 | 49.4 | 9.2 | +2.8 | 9.7 | -0.55 | -0.03 | 0.0 | keep collecting (29/50) |
| pin_price | 4-1 | 80.0 | 49.3 | 30.7 | +2.79 | 55.9 | 0.0 | 0.86 | 60.0 | keep collecting (5/50) |
| fd_move | 15-5 | 75.0 | 50.7 | 24.3 | +8.09 | 40.4 | 3.7 | -0.18 | 0.0 | keep collecting (20/50) |
| fd_juice | 10-3 | 76.9 | 50.3 | 26.7 | +6.54 | 50.3 | 0.0 | 3.42 | 69.2 | keep collecting (13/50) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 118-116 | 50.4 | 49.5 | 0.9 | -13.81 | -5.9 |  |  |  | no edge shown yet |
| pin_price | 37-29 | 56.1 | 49.4 | 6.7 | +7.92 | 12.0 |  |  |  | no edge shown yet |
| fd_move | 215-199 | 51.9 | 50.2 | 1.7 | -4.72 | -1.1 |  |  |  | no edge shown yet |
| fd_juice | 111-87 | 56.1 | 50.8 | 5.3 | +5.39 | 2.7 |  |  |  | no edge shown yet |
| pin_lead | 17-16 | 51.5 | 49.7 | 1.8 | -1.39 | -4.2 |  |  |  | keep collecting (33/50) |
| pin_lead+pin_value | 13-12 | 52.0 | 50.1 | 1.9 | -0.93 | -3.7 |  |  |  | keep collecting (25/50) |
| fd_juice+pin_price | 5-1 | 83.3 | 52.3 | 31.0 | +2.94 | 49.1 |  |  |  | keep collecting (6/50) |
| fd_move+pin_value | 20-16 | 55.6 | 49.0 | 6.5 | +1.7 | 4.7 |  |  |  | keep collecting (36/50) |
| fd_move+pin_price | 9-7 | 56.2 | 50.0 | 6.2 | +2.6 | 16.3 |  |  |  | keep collecting (16/50) |
| fd_juice+pin_lead | 0-1 | 0.0 | 53.5 | -53.5 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 53.5 | -53.5 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |

## By Pinnacle limit and by stat

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | pass_tds | 3-1 | 75.0 | 25.0 | 7.8 |
| pin_value | close | pass_yds | 10-13 | 43.5 | -5.1 | -18.0 |
| pin_value | close | pin $1k+ | 71-61 | 53.8 | 4.8 | 0.0 |
| pin_value | close | pin $400-1k | 42-47 | 47.2 | -3.2 | -11.5 |
| pin_value | close | pin limit <$400 | 5-8 | 38.5 | -9.6 | -27.9 |
| pin_value | close | receptions | 4-3 | 57.1 | 7.6 | -5.8 |
| pin_value | close | recv_yds | 70-63 | 52.6 | 2.8 | -0.8 |
| pin_value | close | rush_yds | 31-36 | 46.3 | -2.8 | -12.7 |
| pin_price | close | pass_tds | 4-2 | 66.7 | 14.3 | 53.8 |
| pin_price | close | pass_yds | 2-3 | 40.0 | -9.3 | -24.6 |
| pin_price | close | pin $1k+ | 18-17 | 51.4 | 1.9 | 3.7 |
| pin_price | close | pin $400-1k | 18-10 | 64.3 | 14.8 | 26.7 |
| pin_price | close | pin limit <$400 | 1-2 | 33.3 | -13.1 | -28.0 |
| pin_price | close | receptions | 13-14 | 48.1 | -0.7 | -0.5 |
| pin_price | close | recv_yds | 10-7 | 58.8 | 10.7 | 10.9 |
| pin_price | close | rush_yds | 8-3 | 72.7 | 21.8 | 38.3 |
| fd_move | close | pass_tds | 0-2 | 0.0 | -53.5 | -100.0 |
| fd_move | close | pass_yds | 18-22 | 45.0 | -6.1 | -15.2 |
| fd_move | close | pin $1k+ | 73-69 | 51.4 | 0.7 | -3.1 |
| fd_move | close | pin $400-1k | 109-103 | 51.4 | 1.5 | -1.6 |
| fd_move | close | pin limit <$400 | 12-14 | 46.2 | -3.3 | -12.0 |
| fd_move | close | receptions | 18-21 | 46.2 | -4.3 | -2.2 |
| fd_move | close | recv_yds | 117-107 | 52.2 | 2.3 | -1.6 |
| fd_move | close | rush_yds | 62-47 | 56.9 | 6.5 | 7.1 |
| fd_juice | close | pass_tds | 14-18 | 43.8 | -6.0 | -14.0 |
| fd_juice | close | pin $1k+ | 40-32 | 55.6 | 4.4 | -0.1 |
| fd_juice | close | pin $400-1k | 60-47 | 56.1 | 5.8 | 3.0 |
| fd_juice | close | pin limit <$400 | 3-2 | 60.0 | 9.3 | 8.3 |
| fd_juice | close | receptions | 92-66 | 58.2 | 7.2 | 5.6 |
| fd_juice | close | recv_yds | 2-2 | 50.0 | -3.5 | -11.9 |
| fd_juice | close | rush_yds | 3-1 | 75.0 | 26.8 | 38.4 |
| pin_lead | close | pass_tds | 1-1 | 50.0 | -3.5 | -27.2 |
| pin_lead | close | pass_yds | 2-4 | 33.3 | -17.8 | -37.2 |
| pin_lead | close | pin $1k+ | 12-6 | 66.7 | 17.8 | 23.3 |
| pin_lead | close | pin $400-1k | 5-10 | 33.3 | -17.4 | -37.2 |
| pin_lead | close | recv_yds | 10-6 | 62.5 | 12.9 | 17.8 |
| pin_lead | close | rush_yds | 4-5 | 44.4 | -3.6 | -16.2 |
| pin_lead+pin_value | close | pass_tds | 1-1 | 50.0 | -3.5 | -27.2 |
| fd_juice+pin_lead | close | pass_tds | 0-1 | 0.0 | -53.5 | -100.0 |
| fd_juice+pin_value | close | pass_tds | 0-1 | 0.0 | -53.5 | -100.0 |
| pin_lead+pin_value | close | pass_yds | 2-3 | 40.0 | -10.7 | -24.6 |
| fd_move+pin_price | close | pass_yds | 1-1 | 50.0 | -3.5 | -5.8 |
| fd_move+pin_value | close | pass_yds | 0-2 | 0.0 | -50.0 | -100.0 |
| pin_lead+pin_value | close | pin $1k+ | 10-5 | 66.7 | 17.8 | 22.8 |
| fd_juice+pin_price | close | pin $1k+ | 2-0 | 100.0 | 50.0 | 76.8 |
| fd_move+pin_value | close | pin $1k+ | 9-7 | 56.2 | 7.6 | 6.0 |
| fd_move+pin_price | close | pin $1k+ | 4-4 | 50.0 | -0.9 | -5.8 |
| pin_lead+pin_value | close | pin $400-1k | 3-7 | 30.0 | -22.1 | -43.5 |
| fd_move+pin_price | close | pin $400-1k | 4-1 | 80.0 | 29.3 | 78.1 |
| fd_juice+pin_price | close | pin $400-1k | 3-1 | 75.0 | 21.5 | 35.2 |
| fd_move+pin_value | close | pin $400-1k | 10-8 | 55.6 | 5.9 | 4.7 |
| fd_juice+pin_lead | close | pin $400-1k | 0-1 | 0.0 | -53.5 | -100.0 |
| fd_juice+pin_value | close | pin $400-1k | 0-1 | 0.0 | -53.5 | -100.0 |
| fd_move+pin_price | close | pin limit <$400 | 1-2 | 33.3 | -13.1 | -28.0 |
| fd_move+pin_value | close | pin limit <$400 | 1-1 | 50.0 | 3.5 | -5.8 |
| fd_juice+pin_price | close | receptions | 5-1 | 83.3 | 31.0 | 49.1 |
| fd_move+pin_price | close | receptions | 2-2 | 50.0 | 1.8 | 35.2 |
| pin_lead+pin_value | close | recv_yds | 9-5 | 64.3 | 14.3 | 21.2 |
| fd_move+pin_value | close | recv_yds | 12-9 | 57.1 | 8.7 | 7.7 |
| fd_move+pin_price | close | recv_yds | 4-4 | 50.0 | 0.9 | -5.8 |
| fd_move+pin_value | close | rush_yds | 8-5 | 61.5 | 11.8 | 16.0 |
| pin_lead+pin_value | close | rush_yds | 1-3 | 25.0 | -23.2 | -52.9 |
| fd_move+pin_price | close | rush_yds | 2-0 | 100.0 | 46.5 | 88.5 |
| pin_value | early | pass_yds | 1-1 | 50.0 | 3.5 | -5.8 |
| pin_value | early | pin $1k+ | 16-7 | 69.6 | 20.3 | 30.1 |
| pin_value | early | pin $400-1k | 0-1 | 0.0 | -46.5 | -100.0 |
| pin_value | early | pin limit <$400 | 1-4 | 20.0 | -30.7 | -62.5 |
| pin_value | early | receptions | 1-0 | 100.0 | 46.5 | 64.9 |
| pin_value | early | recv_yds | 8-6 | 57.1 | 7.1 | 7.7 |
| pin_value | early | rush_yds | 7-5 | 58.3 | 9.5 | 9.9 |
| pin_price | early | pin $1k+ | 4-0 | 100.0 | 50.0 | 94.8 |
| pin_price | early | pin $400-1k | 0-1 | 0.0 | -46.5 | -100.0 |
| pin_price | early | receptions | 3-1 | 75.0 | 25.0 | 41.3 |
| pin_price | early | rush_yds | 1-0 | 100.0 | 53.5 | 114.0 |
| fd_move | early | pass_yds | 3-1 | 75.0 | 23.2 | 40.8 |
| fd_move | early | pin limit <$400 | 2-1 | 66.7 | 15.5 | 25.1 |
| fd_move | early | recv_yds | 6-2 | 75.0 | 25.0 | 39.8 |
| fd_move | early | rush_yds | 6-2 | 75.0 | 24.1 | 40.9 |
| fd_juice | early | pass_tds | 2-0 | 100.0 | 46.5 | 79.8 |
| fd_juice | early | receptions | 7-3 | 70.0 | 20.7 | 41.7 |
| fd_juice | early | recv_yds | 1-0 | 100.0 | 46.5 | 76.9 |
