# CBB period scorecard — halves and half team totals

Generated 2026-11-14 22:38 UTC. 960 graded period markets (168 had no unique final matched and are not graded).

Retail lines from the FanDuel event feed, sharp reference from Pinnacle at
period 1. Second-half markets settle **including overtime**, which is how
FanDuel grades them, and the finals file carries `h1a`/`h1h` so the second half
is simply final minus first half.

**There are no tickets/money splits on any period market** — the Action Network
splits feed is full-game only — so every signal here is handicap or price.
Pinnacle covers the first half only, so 2nd-half markets run on FanDuel's own
movement alone.

Base rates on this sample:

- **spread**: default side won 47.8% (n=272)
- **total**: default side won 50.8% (n=193)
- **ml**: default side won 73.1% (n=167)
- **tt_home**: default side won 53.4% (n=161)
- **tt_away**: default side won 54.0% (n=161)
- **2h_tt_ot**: default side won 92.3% (n=13)
- **2h_tt_no_ot**: default side won 52.1% (n=309)

Proposals appear at 50 decided markets. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 61-54 | 53.0 | 49.8 | 3.3 | -1.01 | -0.9 | 0.22 | no edge shown yet |
| pin_price | 9-24 | 27.3 | 27.6 | -0.3 | +16.56 | 50.2 | 0.53 | keep collecting (33/50) |
| follow_move | 122-98-3 | 55.5 | 51.9 | 3.6 | +4.86 | 2.2 | -0.04 | no edge shown yet |
| fd_juice | 14-26 | 35.0 | 49.2 | -14.2 | -14.55 | -36.4 | 0.03 | keep collecting (40/50) |
| follow_move+pin_value | 2-3 | 40.0 | 49.8 | -9.8 | -1.15 | -23.1 | 0.2 | keep collecting (5/50) |
| follow_move+pin_price | 2-0 | 100.0 | 26.9 | 73.1 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 128-91 | 58.4 | 49.8 | 8.7 | +20.18 | 9.2 |  | PROMOTE: beats break-even and its own base rate |
| pin_price | 12-41-1 | 22.6 | 27.3 | -4.7 | +15.24 | 28.2 |  | DROP: below break-even |
| follow_move | 323-374-6 | 46.3 | 49.3 | -3.0 | -64.97 | -9.2 |  | DROP: below break-even |
| fd_juice | 48-68 | 41.4 | 49.7 | -8.4 | -28.01 | -24.2 |  | DROP: below break-even |
| follow_move+pin_price | 5-10-1 | 33.3 | 26.9 | 6.4 | +21.2 | 132.5 |  | keep collecting (15/50) |
| follow_move+pin_value | 13-12 | 52.0 | 49.8 | 2.2 | -0.48 | -1.9 |  | keep collecting (25/50) |

## By period and market

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 128-91 | 58.4 | 8.7 | 9.2 |
| pin_value | close | 1h|spread | 61-45 | 57.5 | 8.1 | 7.5 |
| pin_value | close | 1h|total | 67-46 | 59.3 | 9.2 | 10.9 |
| pin_price | close | 1h | 12-41-1 | 22.6 | -4.7 | 28.2 |
| pin_price | close | 1h|ml | 12-40-1 | 23.1 | -3.9 | 30.6 |
| pin_price | close | 1h|spread | 0-1 | 0.0 | -47.8 | -100.0 |
| follow_move | close | 1h | 182-189-6 | 49.1 | -0.1 | -2.4 |
| follow_move | close | 1h|ml | 67-77-6 | 46.5 | -1.2 | -0.5 |
| follow_move | close | 1h|spread | 54-44 | 55.1 | 4.9 | 5.2 |
| follow_move | close | 1h|total | 61-68 | 47.3 | -2.6 | -10.2 |
| follow_move | close | 2h | 141-185 | 43.3 | -6.3 | -17.2 |
| follow_move | close | 2h OT game | 2-6 | 25.0 | -23.1 | -51.0 |
| follow_move | close | 2h no OT | 139-179 | 43.7 | -5.9 | -16.3 |
| follow_move | close | 2h|spread | 46-54 | 46.0 | -4.1 | -11.8 |
| follow_move | close | 2h|tt_away | 43-69 | 38.4 | -10.9 | -26.7 |
| follow_move | close | 2h|tt_home | 52-62 | 45.6 | -3.7 | -12.6 |
| fd_juice | close | 1h | 4-6 | 40.0 | -10.3 | -26.4 |
| fd_juice | close | 1h|spread | 3-5 | 37.5 | -13.1 | -30.9 |
| fd_juice | close | 1h|total | 1-1 | 50.0 | 0.8 | -8.4 |
| fd_juice | close | 2h | 44-62 | 41.5 | -8.2 | -23.9 |
| fd_juice | close | 2h OT game | 1-4 | 20.0 | -29.3 | -63.1 |
| fd_juice | close | 2h no OT | 43-58 | 42.6 | -7.1 | -22.0 |
| fd_juice | close | 2h|spread | 5-5 | 50.0 | -0.4 | -7.7 |
| fd_juice | close | 2h|tt_away | 25-24 | 51.0 | 0.4 | -6.7 |
| fd_juice | close | 2h|tt_home | 14-33 | 29.8 | -18.8 | -45.4 |
| follow_move+pin_price | close | 1h | 5-10-1 | 33.3 | 6.4 | 132.5 |
| follow_move+pin_value | close | 1h | 13-12 | 52.0 | 2.2 | -1.9 |
| follow_move+pin_price | close | 1h|ml | 5-10-1 | 33.3 | 6.4 | 132.5 |
| follow_move+pin_value | close | 1h|spread | 8-5 | 61.5 | 11.7 | 15.4 |
| follow_move+pin_value | close | 1h|total | 5-7 | 41.7 | -8.2 | -20.7 |
| pin_value | early | 1h | 61-54 | 53.0 | 3.3 | -0.9 |
| pin_value | early | 1h|spread | 26-25 | 51.0 | 1.7 | -4.7 |
| pin_value | early | 1h|total | 35-29 | 54.7 | 4.5 | 2.2 |
| pin_price | early | 1h | 9-24 | 27.3 | -0.3 | 50.2 |
| pin_price | early | 1h|ml | 9-23 | 28.1 | 1.2 | 54.9 |
| pin_price | early | 1h|total | 0-1 | 0.0 | -49.2 | -100.0 |
| follow_move | early | 1h | 76-52-3 | 59.4 | 5.6 | 6.3 |
| follow_move | early | 1h|ml | 36-26-3 | 58.1 | -0.1 | -2.9 |
| follow_move | early | 1h|spread | 22-6 | 78.6 | 29.2 | 50.5 |
| follow_move | early | 1h|total | 18-20 | 47.4 | -2.5 | -10.6 |
| follow_move | early | 2h | 46-46 | 50.0 | 0.8 | -3.6 |
| follow_move | early | 2h no OT | 46-46 | 50.0 | 0.8 | -3.6 |
| follow_move | early | 2h|spread | 15-12 | 55.6 | 6.6 | 6.8 |
| follow_move | early | 2h|tt_away | 12-17 | 41.4 | -7.6 | -20.4 |
| follow_move | early | 2h|tt_home | 19-17 | 52.8 | 3.3 | 2.1 |
| fd_juice | early | 1h | 2-1 | 66.7 | 16.9 | 22.7 |
| fd_juice | early | 1h|spread | 1-0 | 100.0 | 52.2 | 84.7 |
| fd_juice | early | 1h|total | 1-1 | 50.0 | -0.8 | -8.4 |
| fd_juice | early | 2h | 12-25 | 32.4 | -16.8 | -41.2 |
| fd_juice | early | 2h no OT | 12-25 | 32.4 | -16.8 | -41.2 |
| fd_juice | early | 2h|spread | 0-3 | 0.0 | -50.7 | -100.0 |
| fd_juice | early | 2h|tt_away | 8-9 | 47.1 | -1.3 | -15.2 |
| fd_juice | early | 2h|tt_home | 4-13 | 23.5 | -26.3 | -56.7 |
| follow_move+pin_value | early | 1h | 2-3 | 40.0 | -9.8 | -23.1 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 73.1 | 610.0 |
| follow_move+pin_price | early | 1h|ml | 2-0 | 100.0 | 73.1 | 610.0 |
| follow_move+pin_value | early | 1h|spread | 1-1 | 50.0 | 0.0 | -1.9 |
| follow_move+pin_value | early | 1h|total | 1-2 | 33.3 | -16.4 | -37.2 |
