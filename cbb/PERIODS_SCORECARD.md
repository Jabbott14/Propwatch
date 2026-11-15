# CBB period scorecard — halves and half team totals

Generated 2026-11-15 16:30 UTC. 1035 graded period markets (114 had no unique final matched and are not graded).

Retail lines from the FanDuel event feed, sharp reference from Pinnacle at
period 1. Second-half markets settle **including overtime**, which is how
FanDuel grades them, and the finals file carries `h1a`/`h1h` so the second half
is simply final minus first half.

**There are no tickets/money splits on any period market** — the Action Network
splits feed is full-game only — so every signal here is handicap or price.
Pinnacle covers the first half only, so 2nd-half markets run on FanDuel's own
movement alone.

Base rates on this sample:

- **spread**: default side won 48.3% (n=294)
- **total**: default side won 50.2% (n=211)
- **ml**: default side won 72.0% (n=182)
- **tt_home**: default side won 52.0% (n=171)
- **tt_away**: default side won 52.6% (n=171)
- **2h_tt_ot**: default side won 92.3% (n=13)
- **2h_tt_no_ot**: default side won 50.8% (n=329)

Proposals appear at 50 decided markets. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 67-57 | 54.0 | 49.8 | 4.2 | +1.1 | 0.9 | 0.23 | no edge shown yet |
| pin_price | 9-25 | 26.5 | 28.7 | -2.2 | +15.56 | 45.8 | 0.53 | keep collecting (34/50) |
| follow_move | 129-104-3 | 55.4 | 51.8 | 3.6 | +5.11 | 2.2 | -0.07 | no edge shown yet |
| fd_juice | 17-28 | 37.8 | 49.7 | -11.9 | -14.07 | -31.3 | 0.13 | keep collecting (45/50) |
| follow_move+pin_value | 2-3 | 40.0 | 50.0 | -10.0 | -1.15 | -23.1 | 0.2 | keep collecting (5/50) |
| follow_move+pin_price | 2-0 | 100.0 | 28.0 | 72.0 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 138-101 | 57.7 | 49.8 | 7.9 | +18.83 | 7.9 |  | PROMOTE: beats break-even and its own base rate |
| pin_price | 13-44-1 | 22.8 | 28.8 | -6.0 | +16.34 | 28.2 |  | DROP: below break-even |
| follow_move | 347-403-6 | 46.3 | 49.2 | -2.9 | -63.4 | -8.4 |  | DROP: below break-even |
| fd_juice | 53-70 | 43.1 | 49.8 | -6.7 | -26.04 | -21.2 |  | DROP: below break-even |
| follow_move+pin_price | 6-11-1 | 35.3 | 28.0 | 7.3 | +24.3 | 135.0 |  | keep collecting (17/50) |
| follow_move+pin_value | 13-13 | 50.0 | 49.9 | 0.1 | -1.48 | -5.7 |  | keep collecting (26/50) |

## By period and market

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 138-101 | 57.7 | 7.9 | 7.9 |
| pin_value | close | 1h|spread | 67-50 | 57.3 | 7.7 | 6.8 |
| pin_value | close | 1h|total | 71-51 | 58.2 | 8.2 | 8.9 |
| pin_price | close | 1h | 13-44-1 | 22.8 | -6.0 | 28.2 |
| pin_price | close | 1h|ml | 13-42-1 | 23.6 | -4.4 | 32.7 |
| pin_price | close | 1h|spread | 0-1 | 0.0 | -48.3 | -100.0 |
| pin_price | close | 1h|total | 0-1 | 0.0 | -49.8 | -100.0 |
| follow_move | close | 1h | 195-207-6 | 48.5 | -0.2 | -1.6 |
| follow_move | close | 1h|ml | 75-83-6 | 47.5 | 0.8 | 5.4 |
| follow_move | close | 1h|spread | 58-48 | 54.7 | 4.5 | 4.6 |
| follow_move | close | 1h|total | 62-76 | 44.9 | -5.0 | -14.7 |
| follow_move | close | 2h | 152-196 | 43.7 | -6.1 | -16.3 |
| follow_move | close | 2h OT game | 2-6 | 25.0 | -23.8 | -51.0 |
| follow_move | close | 2h no OT | 150-190 | 44.1 | -5.6 | -15.5 |
| follow_move | close | 2h|spread | 49-59 | 45.4 | -4.7 | -13.0 |
| follow_move | close | 2h|tt_away | 45-72 | 38.5 | -11.1 | -26.5 |
| follow_move | close | 2h|tt_home | 58-65 | 47.2 | -2.4 | -9.7 |
| fd_juice | close | 1h | 4-6 | 40.0 | -10.3 | -26.4 |
| fd_juice | close | 1h|spread | 3-5 | 37.5 | -12.9 | -30.9 |
| fd_juice | close | 1h|total | 1-1 | 50.0 | 0.2 | -8.4 |
| fd_juice | close | 2h | 49-64 | 43.4 | -6.4 | -20.7 |
| fd_juice | close | 2h OT game | 1-4 | 20.0 | -29.6 | -63.1 |
| fd_juice | close | 2h no OT | 48-60 | 44.4 | -5.3 | -18.7 |
| fd_juice | close | 2h|spread | 6-5 | 54.5 | 4.1 | 0.5 |
| fd_juice | close | 2h|tt_away | 28-26 | 51.9 | 1.7 | -5.4 |
| fd_juice | close | 2h|tt_home | 15-33 | 31.2 | -17.9 | -42.8 |
| follow_move+pin_price | close | 1h | 6-11-1 | 35.3 | 7.3 | 135.0 |
| follow_move+pin_value | close | 1h | 13-13 | 50.0 | 0.1 | -5.7 |
| follow_move+pin_price | close | 1h|ml | 6-11-1 | 35.3 | 7.3 | 135.0 |
| follow_move+pin_value | close | 1h|spread | 8-5 | 61.5 | 11.7 | 15.4 |
| follow_move+pin_value | close | 1h|total | 5-8 | 38.5 | -11.5 | -26.8 |
| pin_value | early | 1h | 67-57 | 54.0 | 4.2 | 0.9 |
| pin_value | early | 1h|spread | 31-25 | 55.4 | 5.8 | 3.4 |
| pin_value | early | 1h|total | 36-32 | 52.9 | 2.9 | -1.2 |
| pin_price | early | 1h | 9-25 | 26.5 | -2.2 | 45.8 |
| pin_price | early | 1h|ml | 9-24 | 27.3 | -0.7 | 50.2 |
| pin_price | early | 1h|total | 0-1 | 0.0 | -49.8 | -100.0 |
| follow_move | early | 1h | 78-58-3 | 57.4 | 3.9 | 2.7 |
| follow_move | early | 1h|ml | 38-30-3 | 55.9 | -1.2 | -6.2 |
| follow_move | early | 1h|spread | 22-7 | 75.9 | 26.3 | 45.3 |
| follow_move | early | 1h|total | 18-21 | 46.2 | -3.8 | -12.9 |
| follow_move | early | 2h | 51-46 | 52.6 | 3.2 | 1.4 |
| follow_move | early | 2h no OT | 51-46 | 52.6 | 3.2 | 1.4 |
| follow_move | early | 2h|spread | 16-12 | 57.1 | 8.0 | 9.6 |
| follow_move | early | 2h|tt_away | 15-17 | 46.9 | -2.5 | -9.3 |
| follow_move | early | 2h|tt_home | 20-17 | 54.1 | 4.4 | 4.5 |
| fd_juice | early | 1h | 2-1 | 66.7 | 17.1 | 22.7 |
| fd_juice | early | 1h|spread | 1-0 | 100.0 | 51.7 | 84.7 |
| fd_juice | early | 1h|total | 1-1 | 50.0 | -0.2 | -8.4 |
| fd_juice | early | 2h | 15-27 | 35.7 | -14.0 | -35.1 |
| fd_juice | early | 2h no OT | 15-27 | 35.7 | -14.0 | -35.1 |
| fd_juice | early | 2h|spread | 0-3 | 0.0 | -50.6 | -100.0 |
| fd_juice | early | 2h|tt_away | 9-10 | 47.4 | -1.7 | -14.7 |
| fd_juice | early | 2h|tt_home | 6-14 | 30.0 | -20.2 | -44.8 |
| follow_move+pin_value | early | 1h | 2-3 | 40.0 | -10.0 | -23.1 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 72.0 | 610.0 |
| follow_move+pin_price | early | 1h|ml | 2-0 | 100.0 | 72.0 | 610.0 |
| follow_move+pin_value | early | 1h|spread | 1-1 | 50.0 | 0.0 | -1.9 |
| follow_move+pin_value | early | 1h|total | 1-2 | 33.3 | -16.6 | -37.2 |
