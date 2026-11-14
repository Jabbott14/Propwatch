# CBB period scorecard — halves and half team totals

Generated 2026-11-14 15:55 UTC. 921 graded period markets (108 had no unique final matched and are not graded).

Retail lines from the FanDuel event feed, sharp reference from Pinnacle at
period 1. Second-half markets settle **including overtime**, which is how
FanDuel grades them, and the finals file carries `h1a`/`h1h` so the second half
is simply final minus first half.

**There are no tickets/money splits on any period market** — the Action Network
splits feed is full-game only — so every signal here is handicap or price.
Pinnacle covers the first half only, so 2nd-half markets run on FanDuel's own
movement alone.

Base rates on this sample:

- **spread**: default side won 48.1% (n=258)
- **total**: default side won 51.1% (n=186)
- **ml**: default side won 74.1% (n=162)
- **tt_home**: default side won 54.5% (n=156)
- **tt_away**: default side won 55.6% (n=153)
- **2h_tt_ot**: default side won 92.3% (n=13)
- **2h_tt_no_ot**: default side won 53.4% (n=296)

Proposals appear at 50 decided markets. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 61-54 | 53.0 | 49.9 | 3.2 | -1.01 | -0.9 | 0.22 | no edge shown yet |
| pin_price | 9-24 | 27.3 | 26.6 | 0.6 | +16.56 | 50.2 | 0.53 | keep collecting (33/50) |
| follow_move | 121-97-3 | 55.5 | 51.8 | 3.7 | +4.97 | 2.2 | -0.06 | no edge shown yet |
| fd_juice | 14-26 | 35.0 | 49.0 | -14.0 | -14.55 | -36.4 | 0.03 | keep collecting (40/50) |
| follow_move+pin_value | 2-3 | 40.0 | 49.8 | -9.8 | -1.15 | -23.1 | 0.2 | keep collecting (5/50) |
| follow_move+pin_price | 2-0 | 100.0 | 25.9 | 74.1 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 125-88 | 58.7 | 49.9 | 8.8 | +20.6 | 9.7 |  | PROMOTE: beats break-even and its own base rate |
| pin_price | 12-41-1 | 22.6 | 26.3 | -3.7 | +15.24 | 28.2 |  | DROP: below break-even |
| follow_move | 309-355-6 | 46.5 | 49.3 | -2.7 | -70.6 | -10.5 |  | DROP: below break-even |
| fd_juice | 45-68 | 39.8 | 49.7 | -9.9 | -30.79 | -27.2 |  | DROP: below break-even |
| follow_move+pin_price | 5-10-1 | 33.3 | 25.9 | 7.4 | +21.2 | 132.5 |  | keep collecting (15/50) |
| follow_move+pin_value | 13-11 | 54.2 | 49.8 | 4.4 | +0.52 | 2.1 |  | keep collecting (24/50) |

## By period and market

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 125-88 | 58.7 | 8.8 | 9.7 |
| pin_value | close | 1h|spread | 60-43 | 58.3 | 8.7 | 8.8 |
| pin_value | close | 1h|total | 65-45 | 59.1 | 8.9 | 10.5 |
| pin_price | close | 1h | 12-41-1 | 22.6 | -3.7 | 28.2 |
| pin_price | close | 1h|ml | 12-40-1 | 23.1 | -2.8 | 30.6 |
| pin_price | close | 1h|spread | 0-1 | 0.0 | -48.1 | -100.0 |
| follow_move | close | 1h | 176-179-6 | 49.6 | 0.4 | -4.5 |
| follow_move | close | 1h|ml | 65-74-6 | 46.8 | -1.3 | -8.1 |
| follow_move | close | 1h|spread | 52-40 | 56.5 | 6.4 | 7.8 |
| follow_move | close | 1h|total | 59-65 | 47.6 | -2.2 | -9.6 |
| follow_move | close | 2h | 133-176 | 43.0 | -6.3 | -17.5 |
| follow_move | close | 2h OT game | 2-6 | 25.0 | -22.5 | -51.0 |
| follow_move | close | 2h no OT | 131-170 | 43.5 | -5.9 | -16.6 |
| follow_move | close | 2h|spread | 42-52 | 44.7 | -5.4 | -14.2 |
| follow_move | close | 2h|tt_away | 40-64 | 38.5 | -10.6 | -26.4 |
| follow_move | close | 2h|tt_home | 51-60 | 45.9 | -3.1 | -12.1 |
| fd_juice | close | 1h | 3-6 | 33.3 | -16.6 | -38.7 |
| fd_juice | close | 1h|spread | 2-5 | 28.6 | -21.7 | -47.4 |
| fd_juice | close | 1h|total | 1-1 | 50.0 | 1.1 | -8.4 |
| fd_juice | close | 2h | 42-62 | 40.4 | -9.3 | -26.2 |
| fd_juice | close | 2h OT game | 1-4 | 20.0 | -29.1 | -63.1 |
| fd_juice | close | 2h no OT | 41-58 | 41.4 | -8.3 | -24.4 |
| fd_juice | close | 2h|spread | 5-5 | 50.0 | -0.4 | -7.7 |
| fd_juice | close | 2h|tt_away | 25-24 | 51.0 | 0.2 | -6.7 |
| fd_juice | close | 2h|tt_home | 12-33 | 26.7 | -21.6 | -51.7 |
| follow_move+pin_price | close | 1h | 5-10-1 | 33.3 | 7.4 | 132.5 |
| follow_move+pin_value | close | 1h | 13-11 | 54.2 | 4.4 | 2.1 |
| follow_move+pin_price | close | 1h|ml | 5-10-1 | 33.3 | 7.4 | 132.5 |
| follow_move+pin_value | close | 1h|spread | 8-5 | 61.5 | 11.7 | 15.4 |
| follow_move+pin_value | close | 1h|total | 5-6 | 45.5 | -4.3 | -13.5 |
| pin_value | early | 1h | 61-54 | 53.0 | 3.2 | -0.9 |
| pin_value | early | 1h|spread | 26-25 | 51.0 | 1.6 | -4.7 |
| pin_value | early | 1h|total | 35-29 | 54.7 | 4.4 | 2.2 |
| pin_price | early | 1h | 9-24 | 27.3 | 0.6 | 50.2 |
| pin_price | early | 1h|ml | 9-23 | 28.1 | 2.2 | 54.9 |
| pin_price | early | 1h|total | 0-1 | 0.0 | -48.9 | -100.0 |
| follow_move | early | 1h | 76-51-3 | 59.8 | 6.0 | 7.1 |
| follow_move | early | 1h|ml | 36-25-3 | 59.0 | 0.7 | -1.4 |
| follow_move | early | 1h|spread | 22-6 | 78.6 | 29.1 | 50.5 |
| follow_move | early | 1h|total | 18-20 | 47.4 | -2.5 | -10.6 |
| follow_move | early | 2h | 45-46 | 49.5 | 0.4 | -4.6 |
| follow_move | early | 2h no OT | 45-46 | 49.5 | 0.4 | -4.6 |
| follow_move | early | 2h|spread | 14-12 | 53.8 | 4.7 | 3.6 |
| follow_move | early | 2h|tt_away | 12-17 | 41.4 | -7.3 | -20.4 |
| follow_move | early | 2h|tt_home | 19-17 | 52.8 | 3.5 | 2.1 |
| fd_juice | early | 1h | 2-1 | 66.7 | 16.6 | 22.7 |
| fd_juice | early | 1h|spread | 1-0 | 100.0 | 51.9 | 84.7 |
| fd_juice | early | 1h|total | 1-1 | 50.0 | -1.1 | -8.4 |
| fd_juice | early | 2h | 12-25 | 32.4 | -16.4 | -41.2 |
| fd_juice | early | 2h no OT | 12-25 | 32.4 | -16.4 | -41.2 |
| fd_juice | early | 2h|spread | 0-3 | 0.0 | -50.6 | -100.0 |
| fd_juice | early | 2h|tt_away | 8-9 | 47.1 | -0.7 | -15.2 |
| fd_juice | early | 2h|tt_home | 4-13 | 23.5 | -26.2 | -56.7 |
| follow_move+pin_value | early | 1h | 2-3 | 40.0 | -9.8 | -23.1 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 74.1 | 610.0 |
| follow_move+pin_price | early | 1h|ml | 2-0 | 100.0 | 74.1 | 610.0 |
| follow_move+pin_value | early | 1h|spread | 1-1 | 50.0 | 0.0 | -1.9 |
| follow_move+pin_value | early | 1h|total | 1-2 | 33.3 | -16.3 | -37.2 |
