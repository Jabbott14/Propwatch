# NFL prop scorecard

Generated 2026-11-12 18:32 UTC. 497 graded props (84 had no nflverse result and are not graded).

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

Base rate: the over hit **46.7%** of 497 graded props. `expected %` is
that rate applied to the sides each signal picked; `edge` is hit% minus it.

Proposals appear at 50 decided props. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 17-12 | 58.6 | 49.4 | 9.2 | +2.8 | 9.7 | -0.55 | -0.03 | 0.0 | keep collecting (29/50) |
| pin_price | 4-1 | 80.0 | 49.3 | 30.7 | +2.79 | 55.9 | 0.0 | 0.86 | 60.0 | keep collecting (5/50) |
| fd_move | 12-5 | 70.6 | 50.2 | 20.4 | +5.53 | 32.5 | 4.29 | -0.19 | 0.0 | keep collecting (17/50) |
| fd_juice | 7-2 | 77.8 | 49.6 | 28.1 | +4.68 | 52.0 | 0.0 | 3.33 | 55.6 | keep collecting (9/50) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 97-85 | 53.3 | 49.5 | 3.8 | -1.35 | -0.7 |  |  |  | no edge shown yet |
| pin_price | 29-20 | 59.2 | 49.8 | 9.4 | +9.64 | 19.7 |  |  |  | keep collecting (49/50) |
| fd_move | 125-137 | 47.7 | 50.2 | -2.5 | -24.35 | -9.3 |  |  |  | DROP: below break-even |
| fd_juice | 73-57 | 56.2 | 50.8 | 5.4 | +3.67 | 2.8 |  |  |  | no edge shown yet |
| pin_lead | 15-6 | 71.4 | 49.5 | 21.9 | +6.84 | 32.6 |  |  |  | keep collecting (21/50) |
| pin_lead+pin_value | 13-5 | 72.2 | 49.6 | 22.6 | +6.07 | 33.7 |  |  |  | keep collecting (18/50) |
| fd_juice+pin_price | 4-1 | 80.0 | 53.3 | 26.7 | +1.96 | 39.3 |  |  |  | keep collecting (5/50) |
| fd_move+pin_value | 9-12 | 42.9 | 48.9 | -6.0 | -4.04 | -19.2 |  |  |  | keep collecting (21/50) |
| fd_move+pin_price | 6-4 | 60.0 | 51.3 | 8.7 | +2.95 | 29.5 |  |  |  | keep collecting (10/50) |
| fd_juice+pin_lead | 0-1 | 0.0 | 53.3 | -53.3 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 53.3 | -53.3 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |

## By Pinnacle limit and by stat

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | pass_tds | 3-1 | 75.0 | 25.0 | 7.8 |
| pin_value | close | pass_yds | 8-10 | 44.4 | -3.3 | -16.2 |
| pin_value | close | pin $1k+ | 62-53 | 53.9 | 4.9 | 0.1 |
| pin_value | close | pin $400-1k | 31-29 | 51.7 | 1.1 | -3.3 |
| pin_value | close | pin limit <$400 | 4-3 | 57.1 | 7.6 | 7.7 |
| pin_value | close | receptions | 4-1 | 80.0 | 29.3 | 31.9 |
| pin_value | close | recv_yds | 60-48 | 55.6 | 5.7 | 4.7 |
| pin_value | close | rush_yds | 22-25 | 46.8 | -2.6 | -11.6 |
| pin_price | close | pass_tds | 4-1 | 80.0 | 26.7 | 84.5 |
| pin_price | close | pass_yds | 2-3 | 40.0 | -9.3 | -24.6 |
| pin_price | close | pin $1k+ | 15-12 | 55.6 | 5.4 | 13.1 |
| pin_price | close | pin $400-1k | 13-6 | 68.4 | 18.6 | 36.5 |
| pin_price | close | pin limit <$400 | 1-2 | 33.3 | -13.3 | -28.0 |
| pin_price | close | receptions | 10-10 | 50.0 | 0.7 | 5.0 |
| pin_price | close | recv_yds | 7-4 | 63.6 | 15.1 | 20.0 |
| pin_price | close | rush_yds | 6-2 | 75.0 | 24.2 | 43.0 |
| fd_move | close | pass_tds | 0-2 | 0.0 | -53.3 | -100.0 |
| fd_move | close | pass_yds | 12-14 | 46.2 | -5.4 | -13.0 |
| fd_move | close | pin $1k+ | 48-41 | 53.9 | 3.0 | 1.5 |
| fd_move | close | pin $400-1k | 60-74 | 44.8 | -5.2 | -14.1 |
| fd_move | close | pin limit <$400 | 5-12 | 29.4 | -18.0 | -42.9 |
| fd_move | close | receptions | 8-12 | 40.0 | -10.7 | -13.9 |
| fd_move | close | recv_yds | 66-78 | 45.8 | -4.0 | -13.6 |
| fd_move | close | rush_yds | 39-31 | 55.7 | 5.4 | 4.9 |
| fd_juice | close | pass_tds | 9-11 | 45.0 | -5.0 | -12.9 |
| fd_juice | close | pin $1k+ | 27-23 | 54.0 | 3.1 | -2.9 |
| fd_juice | close | pin $400-1k | 38-28 | 57.6 | 7.2 | 6.2 |
| fd_juice | close | pin limit <$400 | 2-1 | 66.7 | 17.8 | 9.9 |
| fd_juice | close | receptions | 61-43 | 58.7 | 7.8 | 6.5 |
| fd_juice | close | recv_yds | 2-2 | 50.0 | -3.3 | -11.9 |
| fd_juice | close | rush_yds | 1-1 | 50.0 | 0.0 | -1.0 |
| pin_lead | close | pass_tds | 1-1 | 50.0 | -3.3 | -27.2 |
| pin_lead | close | pass_yds | 2-0 | 100.0 | 53.3 | 88.5 |
| pin_lead | close | pin $1k+ | 10-2 | 83.3 | 34.4 | 53.5 |
| pin_lead | close | pin $400-1k | 5-4 | 55.6 | 5.2 | 4.7 |
| pin_lead | close | recv_yds | 9-3 | 75.0 | 25.0 | 41.4 |
| pin_lead | close | rush_yds | 3-2 | 60.0 | 12.0 | 13.1 |
| pin_lead+pin_value | close | pass_tds | 1-1 | 50.0 | -3.3 | -27.2 |
| fd_juice+pin_lead | close | pass_tds | 0-1 | 0.0 | -53.3 | -100.0 |
| fd_juice+pin_value | close | pass_tds | 0-1 | 0.0 | -53.3 | -100.0 |
| pin_lead+pin_value | close | pass_yds | 2-0 | 100.0 | 53.3 | 88.5 |
| fd_move+pin_price | close | pass_yds | 1-1 | 50.0 | -3.3 | -5.8 |
| fd_move+pin_value | close | pass_yds | 0-2 | 0.0 | -50.0 | -100.0 |
| pin_lead+pin_value | close | pin $1k+ | 10-2 | 83.3 | 34.4 | 53.5 |
| fd_juice+pin_price | close | pin $1k+ | 1-0 | 100.0 | 46.7 | 55.6 |
| fd_move+pin_value | close | pin $1k+ | 5-5 | 50.0 | 1.3 | -5.7 |
| fd_move+pin_price | close | pin $1k+ | 2-2 | 50.0 | -3.3 | -5.8 |
| pin_lead+pin_value | close | pin $400-1k | 3-3 | 50.0 | -1.1 | -5.7 |
| fd_move+pin_price | close | pin $400-1k | 3-0 | 100.0 | 46.7 | 134.0 |
| fd_juice+pin_price | close | pin $400-1k | 3-1 | 75.0 | 21.7 | 35.2 |
| fd_move+pin_value | close | pin $400-1k | 3-6 | 33.3 | -16.3 | -37.2 |
| fd_juice+pin_lead | close | pin $400-1k | 0-1 | 0.0 | -53.3 | -100.0 |
| fd_juice+pin_value | close | pin $400-1k | 0-1 | 0.0 | -53.3 | -100.0 |
| fd_move+pin_price | close | pin limit <$400 | 1-2 | 33.3 | -13.3 | -28.0 |
| fd_move+pin_value | close | pin limit <$400 | 1-1 | 50.0 | 3.3 | -5.8 |
| fd_juice+pin_price | close | receptions | 4-1 | 80.0 | 26.7 | 39.3 |
| fd_move+pin_price | close | receptions | 2-1 | 66.7 | 17.8 | 80.3 |
| pin_lead+pin_value | close | recv_yds | 9-3 | 75.0 | 25.0 | 41.4 |
| fd_move+pin_value | close | recv_yds | 5-6 | 45.5 | -2.4 | -14.3 |
| fd_move+pin_price | close | recv_yds | 1-2 | 33.3 | -17.8 | -37.2 |
| fd_move+pin_value | close | rush_yds | 4-4 | 50.0 | 0.0 | -5.8 |
| pin_lead+pin_value | close | rush_yds | 1-1 | 50.0 | 3.3 | -5.8 |
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
| fd_move | early | pass_yds | 3-1 | 75.0 | 23.3 | 40.8 |
| fd_move | early | pin limit <$400 | 2-1 | 66.7 | 15.6 | 25.1 |
| fd_move | early | recv_yds | 4-2 | 66.7 | 17.8 | 25.1 |
| fd_move | early | rush_yds | 5-2 | 71.4 | 21.0 | 34.2 |
| fd_juice | early | pass_tds | 2-0 | 100.0 | 46.7 | 79.8 |
| fd_juice | early | receptions | 4-2 | 66.7 | 18.9 | 38.6 |
| fd_juice | early | recv_yds | 1-0 | 100.0 | 46.7 | 76.9 |
