# CBB period scorecard — halves and half team totals

Generated 2026-11-16 06:58 UTC. 1112 graded period markets (120 had no unique final matched and are not graded).

Retail lines from the FanDuel event feed, sharp reference from Pinnacle at
period 1. Second-half markets settle **including overtime**, which is how
FanDuel grades them, and the finals file carries `h1a`/`h1h` so the second half
is simply final minus first half.

**There are no tickets/money splits on any period market** — the Action Network
splits feed is full-game only — so every signal here is handicap or price.
Pinnacle covers the first half only, so 2nd-half markets run on FanDuel's own
movement alone.

Base rates on this sample:

- **spread**: default side won 47.9% (n=317)
- **total**: default side won 50.7% (n=223)
- **ml**: default side won 71.6% (n=197)
- **tt_home**: default side won 51.4% (n=185)
- **tt_away**: default side won 50.0% (n=184)
- **2h_tt_ot**: default side won 92.3% (n=13)
- **2h_tt_no_ot**: default side won 49.2% (n=356)

Proposals appear at 50 decided markets. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 69-61 | 53.1 | 49.9 | 3.2 | -1.14 | -0.9 | 0.22 | no edge shown yet |
| pin_price | 10-27 | 27.0 | 29.0 | -2.0 | +17.16 | 46.4 | 0.59 | keep collecting (37/50) |
| follow_move | 135-115-3 | 54.0 | 51.4 | 2.6 | -1.06 | -0.4 | -0.04 | no edge shown yet |
| fd_juice | 17-28 | 37.8 | 50.1 | -12.3 | -14.07 | -31.3 | 0.13 | keep collecting (45/50) |
| follow_move+pin_value | 3-3 | 50.0 | 50.2 | -0.2 | -0.29 | -4.9 | 0.17 | keep collecting (6/50) |
| follow_move+pin_price | 2-0 | 100.0 | 28.4 | 71.6 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 143-109 | 56.7 | 49.8 | 6.9 | +15.18 | 6.0 |  | no edge shown yet |
| pin_price | 14-46-1 | 23.3 | 29.1 | -5.8 | +17.74 | 29.1 |  | DROP: below break-even |
| follow_move | 378-431-6 | 46.7 | 49.2 | -2.5 | -46.89 | -5.8 |  | DROP: below break-even |
| fd_juice | 59-74 | 44.4 | 49.8 | -5.5 | -25.14 | -18.9 |  | DROP: below break-even |
| follow_move+pin_price | 7-11-1 | 38.9 | 28.4 | 10.5 | +27.7 | 145.8 |  | keep collecting (18/50) |
| follow_move+pin_value | 13-13 | 50.0 | 49.9 | 0.1 | -1.48 | -5.7 |  | keep collecting (26/50) |

## By period and market

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 143-109 | 56.7 | 6.9 | 6.0 |
| pin_value | close | 1h|spread | 68-56 | 54.8 | 5.3 | 2.3 |
| pin_value | close | 1h|total | 75-53 | 58.6 | 8.5 | 9.6 |
| pin_price | close | 1h | 14-46-1 | 23.3 | -5.8 | 29.1 |
| pin_price | close | 1h|ml | 14-44-1 | 24.1 | -4.3 | 33.5 |
| pin_price | close | 1h|spread | 0-1 | 0.0 | -47.9 | -100.0 |
| pin_price | close | 1h|total | 0-1 | 0.0 | -49.3 | -100.0 |
| follow_move | close | 1h | 209-222-6 | 48.5 | -0.1 | 1.6 |
| follow_move | close | 1h|ml | 81-91-6 | 47.1 | 0.6 | 12.4 |
| follow_move | close | 1h|spread | 64-50 | 56.1 | 5.9 | 7.5 |
| follow_move | close | 1h|total | 64-81 | 44.1 | -5.8 | -16.2 |
| follow_move | close | 2h | 169-209 | 44.7 | -5.2 | -14.3 |
| follow_move | close | 2h OT game | 2-6 | 25.0 | -24.7 | -51.0 |
| follow_move | close | 2h no OT | 167-203 | 45.1 | -4.8 | -13.5 |
| follow_move | close | 2h|spread | 55-63 | 46.6 | -3.5 | -10.4 |
| follow_move | close | 2h|tt_away | 53-76 | 41.1 | -8.9 | -21.4 |
| follow_move | close | 2h|tt_home | 61-70 | 46.6 | -3.2 | -10.7 |
| fd_juice | close | 1h | 5-6 | 45.5 | -5.0 | -16.3 |
| fd_juice | close | 1h|spread | 4-5 | 44.4 | -6.2 | -18.1 |
| fd_juice | close | 1h|total | 1-1 | 50.0 | 0.7 | -8.4 |
| fd_juice | close | 2h | 54-68 | 44.3 | -5.5 | -19.1 |
| fd_juice | close | 2h OT game | 1-4 | 20.0 | -29.7 | -63.1 |
| fd_juice | close | 2h no OT | 53-64 | 45.3 | -4.5 | -17.3 |
| fd_juice | close | 2h|spread | 6-7 | 46.2 | -4.3 | -14.9 |
| fd_juice | close | 2h|tt_away | 29-26 | 52.7 | 2.7 | -3.9 |
| fd_juice | close | 2h|tt_home | 19-35 | 35.2 | -14.2 | -35.7 |
| follow_move+pin_price | close | 1h | 7-11-1 | 38.9 | 10.5 | 145.8 |
| follow_move+pin_value | close | 1h | 13-13 | 50.0 | 0.1 | -5.7 |
| follow_move+pin_price | close | 1h|ml | 7-11-1 | 38.9 | 10.5 | 145.8 |
| follow_move+pin_value | close | 1h|spread | 8-5 | 61.5 | 11.7 | 15.4 |
| follow_move+pin_value | close | 1h|total | 5-8 | 38.5 | -11.5 | -26.8 |
| pin_value | early | 1h | 69-61 | 53.1 | 3.2 | -0.9 |
| pin_value | early | 1h|spread | 33-26 | 55.9 | 6.5 | 4.5 |
| pin_value | early | 1h|total | 36-35 | 50.7 | 0.5 | -5.3 |
| pin_price | early | 1h | 10-27 | 27.0 | -2.0 | 46.4 |
| pin_price | early | 1h|ml | 10-26 | 27.8 | -0.6 | 50.4 |
| pin_price | early | 1h|total | 0-1 | 0.0 | -49.3 | -100.0 |
| follow_move | early | 1h | 81-66-3 | 55.1 | 2.4 | -1.5 |
| follow_move | early | 1h|ml | 39-34-3 | 53.4 | -2.2 | -10.7 |
| follow_move | early | 1h|spread | 24-9 | 72.7 | 23.0 | 39.2 |
| follow_move | early | 1h|total | 18-23 | 43.9 | -6.0 | -17.2 |
| follow_move | early | 2h | 54-49 | 52.4 | 2.8 | 1.2 |
| follow_move | early | 2h no OT | 54-49 | 52.4 | 2.8 | 1.2 |
| follow_move | early | 2h|spread | 17-12 | 58.6 | 9.5 | 12.6 |
| follow_move | early | 2h|tt_away | 16-19 | 45.7 | -4.3 | -11.4 |
| follow_move | early | 2h|tt_home | 21-18 | 53.8 | 4.2 | 4.0 |
| fd_juice | early | 1h | 2-1 | 66.7 | 16.9 | 22.7 |
| fd_juice | early | 1h|spread | 1-0 | 100.0 | 52.1 | 84.7 |
| fd_juice | early | 1h|total | 1-1 | 50.0 | -0.7 | -8.4 |
| fd_juice | early | 2h | 15-27 | 35.7 | -14.4 | -35.1 |
| fd_juice | early | 2h no OT | 15-27 | 35.7 | -14.4 | -35.1 |
| fd_juice | early | 2h|spread | 0-3 | 0.0 | -50.7 | -100.0 |
| fd_juice | early | 2h|tt_away | 9-10 | 47.4 | -2.6 | -14.7 |
| fd_juice | early | 2h|tt_home | 6-14 | 30.0 | -20.1 | -44.8 |
| follow_move+pin_value | early | 1h | 3-3 | 50.0 | -0.2 | -4.9 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 71.6 | 610.0 |
| follow_move+pin_price | early | 1h|ml | 2-0 | 100.0 | 71.6 | 610.0 |
| follow_move+pin_value | early | 1h|spread | 2-1 | 66.7 | 16.0 | 27.5 |
| follow_move+pin_value | early | 1h|total | 1-2 | 33.3 | -16.4 | -37.2 |
