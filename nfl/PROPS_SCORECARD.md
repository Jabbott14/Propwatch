# NFL prop scorecard

Generated 2026-11-12 05:54 UTC. 494 graded props (87 had no nflverse result and are not graded).

**Read this on its own scale, not against the side scorecard.** Pinnacle risks
**$75,000** on an NFL side and **$1,000-$3,000** on a prop at kickoff, $250-$500
earlier in the week. The sharpest book in the world is telling you it is 25-75x
less confident in its own prop number. A prop signal must never be sized like a
side signal, and `pin_value` barely fires here because FanDuel's prop handicaps
sit on Pinnacle's almost every time.

There are no tickets/money splits on any prop, so the only channels are the
handicap and the price. `fd_juice` is the money channel: a static handicap whose
price moves 12+ cents one way. Break-even at -110 is 52.4%.

Base rate: the over hit **46.4%** of 494 graded props. `expected %` is
that rate applied to the sides each signal picked; `edge` is hit% minus it.

Proposals appear at 50 decided props. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 17-12 | 58.6 | 49.4 | 9.2 | +2.8 | 9.7 | -0.55 | keep collecting (29/50) |
| pin_price | 4-1 | 80.0 | 49.3 | 30.7 | +2.79 | 55.9 | 0.0 | keep collecting (5/50) |
| fd_move | 11-5 | 68.8 | 50.5 | 18.3 | +4.65 | 29.0 | 4.0 | keep collecting (16/50) |
| fd_juice | 7-2 | 77.8 | 49.6 | 28.2 | +4.68 | 52.0 | 0.0 | keep collecting (9/50) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 97-84 | 53.6 | 49.5 | 4.1 | -0.35 | -0.2 |  | no edge shown yet |
| pin_price | 29-20 | 59.2 | 49.8 | 9.4 | +9.64 | 19.7 |  | keep collecting (49/50) |
| fd_move | 124-137 | 47.5 | 50.2 | -2.7 | -25.23 | -9.7 |  | DROP: below break-even |
| fd_juice | 73-55 | 57.0 | 50.8 | 6.2 | +5.67 | 4.4 |  | no edge shown yet |
| pin_lead | 15-6 | 71.4 | 49.5 | 21.9 | +6.84 | 32.6 |  | keep collecting (21/50) |

## By Pinnacle limit and by stat

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | pass_tds | 3-1 | 75.0 | 25.0 | 7.8 |
| pin_value | close | pass_yds | 8-10 | 44.4 | -3.1 | -16.2 |
| pin_value | close | pin $1k+ | 62-53 | 53.9 | 5.0 | 0.1 |
| pin_value | close | pin $400-1k | 31-28 | 52.5 | 2.0 | -1.7 |
| pin_value | close | pin limit <$400 | 4-3 | 57.1 | 7.7 | 7.7 |
| pin_value | close | receptions | 4-1 | 80.0 | 29.3 | 31.9 |
| pin_value | close | recv_yds | 60-48 | 55.6 | 5.8 | 4.7 |
| pin_value | close | rush_yds | 22-24 | 47.8 | -1.4 | -9.6 |
| pin_price | close | pass_tds | 4-1 | 80.0 | 26.4 | 84.5 |
| pin_price | close | pass_yds | 2-3 | 40.0 | -9.3 | -24.6 |
| pin_price | close | pin $1k+ | 15-12 | 55.6 | 5.4 | 13.1 |
| pin_price | close | pin $400-1k | 13-6 | 68.4 | 18.6 | 36.5 |
| pin_price | close | pin limit <$400 | 1-2 | 33.3 | -13.0 | -28.0 |
| pin_price | close | receptions | 10-10 | 50.0 | 0.7 | 5.0 |
| pin_price | close | recv_yds | 7-4 | 63.6 | 15.3 | 20.0 |
| pin_price | close | rush_yds | 6-2 | 75.0 | 24.1 | 43.0 |
| fd_move | close | pass_tds | 0-2 | 0.0 | -53.6 | -100.0 |
| fd_move | close | pass_yds | 12-14 | 46.2 | -5.5 | -13.0 |
| fd_move | close | pin $1k+ | 48-41 | 53.9 | 2.9 | 1.5 |
| fd_move | close | pin $400-1k | 59-74 | 44.4 | -5.6 | -14.9 |
| fd_move | close | pin limit <$400 | 5-12 | 29.4 | -17.8 | -42.9 |
| fd_move | close | receptions | 8-12 | 40.0 | -10.7 | -13.9 |
| fd_move | close | recv_yds | 66-78 | 45.8 | -4.0 | -13.6 |
| fd_move | close | rush_yds | 38-31 | 55.1 | 4.7 | 3.6 |
| fd_juice | close | pass_tds | 9-11 | 45.0 | -5.0 | -12.9 |
| fd_juice | close | pin $1k+ | 27-23 | 54.0 | 3.0 | -2.9 |
| fd_juice | close | pin $400-1k | 38-26 | 59.4 | 9.0 | 9.6 |
| fd_juice | close | pin limit <$400 | 2-1 | 66.7 | 17.9 | 9.9 |
| fd_juice | close | receptions | 61-42 | 59.2 | 8.3 | 7.5 |
| fd_juice | close | recv_yds | 2-1 | 66.7 | 13.0 | 17.5 |
| fd_juice | close | rush_yds | 1-1 | 50.0 | 0.0 | -1.0 |
| pin_lead | close | pass_tds | 1-1 | 50.0 | -3.6 | -27.2 |
| pin_lead | close | pass_yds | 2-0 | 100.0 | 53.6 | 88.5 |
| pin_lead | close | pin $1k+ | 10-2 | 83.3 | 34.5 | 53.5 |
| pin_lead | close | pin $400-1k | 5-4 | 55.6 | 5.2 | 4.7 |
| pin_lead | close | recv_yds | 9-3 | 75.0 | 25.0 | 41.4 |
| pin_lead | close | rush_yds | 3-2 | 60.0 | 12.2 | 13.1 |
| pin_value | early | pass_yds | 1-1 | 50.0 | 3.6 | -5.8 |
| pin_value | early | pin $1k+ | 16-7 | 69.6 | 20.4 | 30.1 |
| pin_value | early | pin $400-1k | 0-1 | 0.0 | -46.4 | -100.0 |
| pin_value | early | pin limit <$400 | 1-4 | 20.0 | -30.7 | -62.5 |
| pin_value | early | receptions | 1-0 | 100.0 | 46.4 | 64.9 |
| pin_value | early | recv_yds | 8-6 | 57.1 | 7.1 | 7.7 |
| pin_value | early | rush_yds | 7-5 | 58.3 | 9.5 | 9.9 |
| pin_price | early | pin $1k+ | 4-0 | 100.0 | 50.0 | 94.8 |
| pin_price | early | pin $400-1k | 0-1 | 0.0 | -46.4 | -100.0 |
| pin_price | early | receptions | 3-1 | 75.0 | 25.0 | 41.3 |
| pin_price | early | rush_yds | 1-0 | 100.0 | 53.6 | 114.0 |
| fd_move | early | pass_yds | 3-1 | 75.0 | 23.2 | 40.8 |
| fd_move | early | pin limit <$400 | 2-1 | 66.7 | 15.5 | 25.1 |
| fd_move | early | recv_yds | 4-2 | 66.7 | 17.9 | 25.1 |
| fd_move | early | rush_yds | 4-2 | 66.7 | 15.5 | 25.1 |
| fd_juice | early | pass_tds | 2-0 | 100.0 | 46.4 | 79.8 |
| fd_juice | early | receptions | 4-2 | 66.7 | 19.1 | 38.6 |
| fd_juice | early | recv_yds | 1-0 | 100.0 | 46.4 | 76.9 |
