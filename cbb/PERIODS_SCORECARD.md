# CBB period scorecard — halves and half team totals

Generated 2026-11-15 23:02 UTC. 1074 graded period markets (162 had no unique final matched and are not graded).

Retail lines from the FanDuel event feed, sharp reference from Pinnacle at
period 1. Second-half markets settle **including overtime**, which is how
FanDuel grades them, and the finals file carries `h1a`/`h1h` so the second half
is simply final minus first half.

**There are no tickets/money splits on any period market** — the Action Network
splits feed is full-game only — so every signal here is handicap or price.
Pinnacle covers the first half only, so 2nd-half markets run on FanDuel's own
movement alone.

Base rates on this sample:

- **spread**: default side won 47.7% (n=304)
- **total**: default side won 50.5% (n=218)
- **ml**: default side won 72.1% (n=190)
- **tt_home**: default side won 52.0% (n=179)
- **tt_away**: default side won 51.4% (n=177)
- **2h_tt_ot**: default side won 92.3% (n=13)
- **2h_tt_no_ot**: default side won 50.1% (n=343)

Proposals appear at 50 decided markets. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 68-59 | 53.5 | 49.8 | 3.7 | -0.04 | -0.0 | 0.22 | no edge shown yet |
| pin_price | 9-26 | 25.7 | 28.5 | -2.8 | +14.56 | 41.6 | 0.57 | keep collecting (35/50) |
| follow_move | 131-110-3 | 54.4 | 51.4 | 2.9 | +0.91 | 0.4 | -0.05 | no edge shown yet |
| fd_juice | 17-28 | 37.8 | 49.9 | -12.1 | -14.07 | -31.3 | 0.13 | keep collecting (45/50) |
| follow_move+pin_value | 3-3 | 50.0 | 50.3 | -0.3 | -0.29 | -4.9 | 0.17 | keep collecting (6/50) |
| follow_move+pin_price | 2-0 | 100.0 | 27.9 | 72.1 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 140-106 | 56.9 | 49.8 | 7.1 | +15.57 | 6.3 |  | no edge shown yet |
| pin_price | 13-44-1 | 22.8 | 28.6 | -5.8 | +16.34 | 28.2 |  | DROP: below break-even |
| follow_move | 362-419-6 | 46.4 | 49.3 | -2.9 | -66.44 | -8.4 |  | DROP: below break-even |
| fd_juice | 56-72 | 43.8 | 49.7 | -6.0 | -25.57 | -20.0 |  | DROP: below break-even |
| follow_move+pin_price | 6-11-1 | 35.3 | 27.9 | 7.4 | +24.3 | 135.0 |  | keep collecting (17/50) |
| follow_move+pin_value | 13-13 | 50.0 | 49.9 | 0.1 | -1.48 | -5.7 |  | keep collecting (26/50) |

## By period and market

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 140-106 | 56.9 | 7.1 | 6.3 |
| pin_value | close | 1h|spread | 67-53 | 55.8 | 6.4 | 4.2 |
| pin_value | close | 1h|total | 73-53 | 57.9 | 7.8 | 8.4 |
| pin_price | close | 1h | 13-44-1 | 22.8 | -5.8 | 28.2 |
| pin_price | close | 1h|ml | 13-42-1 | 23.6 | -4.3 | 32.7 |
| pin_price | close | 1h|spread | 0-1 | 0.0 | -47.7 | -100.0 |
| pin_price | close | 1h|total | 0-1 | 0.0 | -49.5 | -100.0 |
| follow_move | close | 1h | 203-215-6 | 48.6 | -0.2 | -1.9 |
| follow_move | close | 1h|ml | 77-89-6 | 46.4 | -0.4 | 2.3 |
| follow_move | close | 1h|spread | 62-48 | 56.4 | 6.1 | 7.8 |
| follow_move | close | 1h|total | 64-78 | 45.1 | -4.9 | -14.5 |
| follow_move | close | 2h | 159-204 | 43.8 | -6.0 | -16.1 |
| follow_move | close | 2h OT game | 2-6 | 25.0 | -24.2 | -51.0 |
| follow_move | close | 2h no OT | 157-198 | 44.2 | -5.6 | -15.3 |
| follow_move | close | 2h|spread | 52-61 | 46.0 | -4.0 | -11.6 |
| follow_move | close | 2h|tt_away | 48-75 | 39.0 | -10.7 | -25.5 |
| follow_move | close | 2h|tt_home | 59-68 | 46.5 | -3.2 | -11.0 |
| fd_juice | close | 1h | 4-6 | 40.0 | -10.4 | -26.4 |
| fd_juice | close | 1h|spread | 3-5 | 37.5 | -13.1 | -30.9 |
| fd_juice | close | 1h|total | 1-1 | 50.0 | 0.5 | -8.4 |
| fd_juice | close | 2h | 52-66 | 44.1 | -5.6 | -19.4 |
| fd_juice | close | 2h OT game | 1-4 | 20.0 | -29.6 | -63.1 |
| fd_juice | close | 2h no OT | 51-62 | 45.1 | -4.6 | -17.5 |
| fd_juice | close | 2h|spread | 6-6 | 50.0 | -0.4 | -7.8 |
| fd_juice | close | 2h|tt_away | 28-26 | 51.9 | 1.7 | -5.4 |
| fd_juice | close | 2h|tt_home | 18-34 | 34.6 | -14.5 | -36.7 |
| follow_move+pin_price | close | 1h | 6-11-1 | 35.3 | 7.4 | 135.0 |
| follow_move+pin_value | close | 1h | 13-13 | 50.0 | 0.1 | -5.7 |
| follow_move+pin_price | close | 1h|ml | 6-11-1 | 35.3 | 7.4 | 135.0 |
| follow_move+pin_value | close | 1h|spread | 8-5 | 61.5 | 11.7 | 15.4 |
| follow_move+pin_value | close | 1h|total | 5-8 | 38.5 | -11.5 | -26.8 |
| pin_value | early | 1h | 68-59 | 53.5 | 3.7 | -0.0 |
| pin_value | early | 1h|spread | 32-25 | 56.1 | 6.7 | 4.8 |
| pin_value | early | 1h|total | 36-34 | 51.4 | 1.3 | -4.0 |
| pin_price | early | 1h | 9-26 | 25.7 | -2.8 | 41.6 |
| pin_price | early | 1h|ml | 9-25 | 26.5 | -1.4 | 45.8 |
| pin_price | early | 1h|total | 0-1 | 0.0 | -49.5 | -100.0 |
| follow_move | early | 1h | 80-62-3 | 56.3 | 3.5 | 1.0 |
| follow_move | early | 1h|ml | 38-33-3 | 53.5 | -2.4 | -10.0 |
| follow_move | early | 1h|spread | 24-7 | 77.4 | 27.8 | 48.2 |
| follow_move | early | 1h|total | 18-22 | 45.0 | -5.0 | -15.1 |
| follow_move | early | 2h | 51-48 | 51.5 | 2.1 | -0.6 |
| follow_move | early | 2h no OT | 51-48 | 51.5 | 2.1 | -0.6 |
| follow_move | early | 2h|spread | 16-12 | 57.1 | 8.3 | 9.6 |
| follow_move | early | 2h|tt_away | 15-18 | 45.5 | -4.2 | -12.0 |
| follow_move | early | 2h|tt_home | 20-18 | 52.6 | 3.0 | 1.8 |
| fd_juice | early | 1h | 2-1 | 66.7 | 17.1 | 22.7 |
| fd_juice | early | 1h|spread | 1-0 | 100.0 | 52.3 | 84.7 |
| fd_juice | early | 1h|total | 1-1 | 50.0 | -0.5 | -8.4 |
| fd_juice | early | 2h | 15-27 | 35.7 | -14.2 | -35.1 |
| fd_juice | early | 2h no OT | 15-27 | 35.7 | -14.2 | -35.1 |
| fd_juice | early | 2h|spread | 0-3 | 0.0 | -50.8 | -100.0 |
| fd_juice | early | 2h|tt_away | 9-10 | 47.4 | -2.1 | -14.7 |
| fd_juice | early | 2h|tt_home | 6-14 | 30.0 | -20.2 | -44.8 |
| follow_move+pin_value | early | 1h | 3-3 | 50.0 | -0.3 | -4.9 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 72.1 | 610.0 |
| follow_move+pin_price | early | 1h|ml | 2-0 | 100.0 | 72.1 | 610.0 |
| follow_move+pin_value | early | 1h|spread | 2-1 | 66.7 | 15.9 | 27.5 |
| follow_move+pin_value | early | 1h|total | 1-2 | 33.3 | -16.5 | -37.2 |
