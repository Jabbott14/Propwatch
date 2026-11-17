# NFL prop scorecard

Generated 2026-11-17 16:30 UTC. 853 graded props (127 had no nflverse result and are not graded).

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

Base rate: the over hit **46.7%** of 853 graded props. `expected %` is
that rate applied to the sides each signal picked; `edge` is hit% minus it.

Proposals appear at 50 decided props. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 17-12 | 58.6 | 49.4 | 9.2 | +2.8 | 9.7 | -0.55 | -0.03 | 0.0 | keep collecting (29/50) |
| pin_price | 4-1 | 80.0 | 49.3 | 30.7 | +2.79 | 55.9 | 0.0 | 0.86 | 60.0 | keep collecting (5/50) |
| fd_move | 21-8 | 72.4 | 50.1 | 22.3 | +10.35 | 35.7 | 2.79 | -0.19 | 0.0 | keep collecting (29/50) |
| fd_juice | 15-5 | 75.0 | 49.7 | 25.3 | +9.72 | 48.6 | -0.05 | 3.65 | 60.0 | keep collecting (20/50) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 151-134 | 53.0 | 49.4 | 3.5 | -2.61 | -0.9 |  |  |  | no edge shown yet |
| pin_price | 39-34 | 53.4 | 49.2 | 4.2 | +4.69 | 6.4 |  |  |  | no edge shown yet |
| fd_move | 249-240 | 50.9 | 50.1 | 0.8 | -15.22 | -3.1 |  |  |  | no edge shown yet |
| fd_juice | 134-105 | 56.1 | 50.8 | 5.2 | +8.03 | 3.4 |  |  |  | no edge shown yet |
| pin_lead | 23-25 | 47.9 | 49.4 | -1.5 | -5.08 | -10.6 |  |  |  | keep collecting (48/50) |
| pin_lead+pin_value | 19-18 | 51.4 | 49.5 | 1.8 | -1.62 | -4.4 |  |  |  | keep collecting (37/50) |
| fd_juice+pin_price | 5-2 | 71.4 | 51.4 | 20.0 | +1.94 | 27.8 |  |  |  | keep collecting (7/50) |
| fd_move+pin_value | 25-18 | 58.1 | 48.8 | 9.3 | +4.12 | 9.6 |  |  |  | keep collecting (43/50) |
| fd_move+pin_price | 10-7 | 58.8 | 49.8 | 9.0 | +3.49 | 20.5 |  |  |  | keep collecting (17/50) |
| fd_juice+pin_lead | 0-1 | 0.0 | 53.3 | -53.3 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 53.3 | -53.3 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |

## By Pinnacle limit and by stat

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | pass_tds | 3-1 | 75.0 | 25.0 | 7.8 |
| pin_value | close | pass_yds | 15-15 | 50.0 | 1.3 | -5.8 |
| pin_value | close | pin $1k+ | 91-74 | 55.2 | 6.1 | 2.9 |
| pin_value | close | pin $400-1k | 55-52 | 51.4 | 1.2 | -3.5 |
| pin_value | close | pin limit <$400 | 5-8 | 38.5 | -9.7 | -27.9 |
| pin_value | close | receptions | 4-4 | 50.0 | 0.8 | -17.5 |
| pin_value | close | recv_yds | 86-72 | 54.4 | 4.7 | 2.6 |
| pin_value | close | rush_yds | 43-42 | 50.6 | 1.4 | -4.6 |
| pin_price | close | pass_tds | 4-2 | 66.7 | 14.4 | 53.8 |
| pin_price | close | pass_yds | 2-4 | 33.3 | -16.7 | -37.2 |
| pin_price | close | pin $1k+ | 20-19 | 51.3 | 1.9 | 2.7 |
| pin_price | close | pin $400-1k | 18-13 | 58.1 | 8.8 | 14.4 |
| pin_price | close | pin limit <$400 | 1-2 | 33.3 | -13.3 | -28.0 |
| pin_price | close | receptions | 13-16 | 44.8 | -3.9 | -7.4 |
| pin_price | close | recv_yds | 12-8 | 60.0 | 12.0 | 13.1 |
| pin_price | close | rush_yds | 8-4 | 66.7 | 16.1 | 26.7 |
| fd_move | close | pass_tds | 0-3 | 0.0 | -53.3 | -100.0 |
| fd_move | close | pass_yds | 23-25 | 47.9 | -2.8 | -9.7 |
| fd_move | close | pin $1k+ | 92-96 | 48.9 | -1.6 | -7.9 |
| fd_move | close | pin $400-1k | 121-116 | 51.1 | 1.2 | -2.2 |
| fd_move | close | pin limit <$400 | 14-14 | 50.0 | 0.7 | -4.5 |
| fd_move | close | receptions | 20-24 | 45.5 | -5.0 | -3.3 |
| fd_move | close | recv_yds | 132-129 | 50.6 | 0.6 | -4.7 |
| fd_move | close | rush_yds | 74-59 | 55.6 | 5.5 | 4.6 |
| fd_juice | close | pass_tds | 18-19 | 48.6 | -1.3 | -1.4 |
| fd_juice | close | pin $1k+ | 52-40 | 56.5 | 5.5 | 3.0 |
| fd_juice | close | pin $400-1k | 70-55 | 56.0 | 5.5 | 3.5 |
| fd_juice | close | pin limit <$400 | 4-3 | 57.1 | 5.7 | -0.1 |
| fd_juice | close | receptions | 110-83 | 57.0 | 6.0 | 3.6 |
| fd_juice | close | recv_yds | 2-2 | 50.0 | -3.3 | -11.9 |
| fd_juice | close | rush_yds | 4-1 | 80.0 | 30.7 | 41.0 |
| pin_lead | close | pass_tds | 1-1 | 50.0 | -3.3 | -27.2 |
| pin_lead | close | pass_yds | 4-5 | 44.4 | -6.7 | -16.2 |
| pin_lead | close | pin $1k+ | 15-12 | 55.6 | 6.4 | 3.1 |
| pin_lead | close | pin $400-1k | 8-13 | 38.1 | -11.7 | -28.2 |
| pin_lead | close | recv_yds | 12-11 | 52.2 | 2.9 | -1.7 |
| pin_lead | close | rush_yds | 6-8 | 42.9 | -5.2 | -19.2 |
| pin_lead+pin_value | close | pass_tds | 1-1 | 50.0 | -3.3 | -27.2 |
| fd_juice+pin_lead | close | pass_tds | 0-1 | 0.0 | -53.3 | -100.0 |
| fd_juice+pin_value | close | pass_tds | 0-1 | 0.0 | -53.3 | -100.0 |
| pin_lead+pin_value | close | pass_yds | 4-3 | 57.1 | 6.7 | 7.7 |
| fd_move+pin_price | close | pass_yds | 1-1 | 50.0 | -3.3 | -5.8 |
| fd_move+pin_value | close | pass_yds | 2-2 | 50.0 | 1.7 | -5.8 |
| pin_lead+pin_value | close | pin $1k+ | 13-9 | 59.1 | 10.3 | 9.4 |
| fd_juice+pin_price | close | pin $1k+ | 2-0 | 100.0 | 50.0 | 76.8 |
| fd_move+pin_value | close | pin $1k+ | 11-9 | 55.0 | 6.7 | 3.7 |
| fd_move+pin_price | close | pin $1k+ | 5-4 | 55.6 | 5.2 | 4.7 |
| pin_lead+pin_value | close | pin $400-1k | 6-9 | 40.0 | -10.7 | -24.6 |
| fd_move+pin_price | close | pin $400-1k | 4-1 | 80.0 | 29.3 | 78.1 |
| fd_juice+pin_price | close | pin $400-1k | 3-2 | 60.0 | 8.0 | 8.1 |
| fd_move+pin_value | close | pin $400-1k | 13-8 | 61.9 | 12.4 | 16.7 |
| fd_juice+pin_lead | close | pin $400-1k | 0-1 | 0.0 | -53.3 | -100.0 |
| fd_juice+pin_value | close | pin $400-1k | 0-1 | 0.0 | -53.3 | -100.0 |
| fd_move+pin_price | close | pin limit <$400 | 1-2 | 33.3 | -13.3 | -28.0 |
| fd_move+pin_value | close | pin limit <$400 | 1-1 | 50.0 | 3.3 | -5.8 |
| fd_juice+pin_price | close | receptions | 5-2 | 71.4 | 20.0 | 27.8 |
| fd_move+pin_price | close | receptions | 2-2 | 50.0 | 1.7 | 35.2 |
| pin_lead+pin_value | close | recv_yds | 11-9 | 55.0 | 5.3 | 3.7 |
| fd_move+pin_value | close | recv_yds | 13-9 | 59.1 | 10.6 | 11.4 |
| fd_move+pin_price | close | recv_yds | 5-4 | 55.6 | 6.7 | 4.7 |
| fd_move+pin_value | close | rush_yds | 10-7 | 58.8 | 9.4 | 10.9 |
| pin_lead+pin_value | close | rush_yds | 3-5 | 37.5 | -10.0 | -29.3 |
| fd_move+pin_price | close | rush_yds | 2-0 | 100.0 | 46.7 | 88.5 |
| pin_value | early | pass_yds | 1-1 | 50.0 | 3.3 | -5.8 |
| pin_value | early | pin $1k+ | 16-7 | 69.6 | 20.3 | 30.1 |
| pin_value | early | pin $400-1k | 0-1 | 0.0 | -46.7 | -100.0 |
| pin_value | early | pin limit <$400 | 1-4 | 20.0 | -30.7 | -62.5 |
| pin_value | early | receptions | 1-0 | 100.0 | 46.7 | 64.9 |
| pin_value | early | recv_yds | 8-6 | 57.1 | 7.1 | 7.7 |
| pin_value | early | rush_yds | 7-5 | 58.3 | 9.4 | 9.9 |
| pin_price | early | pin $1k+ | 4-0 | 100.0 | 50.0 | 94.8 |
| pin_price | early | pin $400-1k | 0-1 | 0.0 | -46.7 | -100.0 |
| pin_price | early | receptions | 3-1 | 75.0 | 25.0 | 41.3 |
| pin_price | early | rush_yds | 1-0 | 100.0 | 53.3 | 114.0 |
| fd_move | early | pass_yds | 4-1 | 80.0 | 29.3 | 50.2 |
| fd_move | early | pin limit <$400 | 2-1 | 66.7 | 15.6 | 25.1 |
| fd_move | early | recv_yds | 8-4 | 66.7 | 17.2 | 24.5 |
| fd_move | early | rush_yds | 9-3 | 75.0 | 24.4 | 40.8 |
| fd_juice | early | pass_tds | 4-0 | 100.0 | 50.0 | 102.5 |
| fd_juice | early | receptions | 10-5 | 66.7 | 17.3 | 32.3 |
| fd_juice | early | recv_yds | 1-0 | 100.0 | 46.7 | 76.9 |
