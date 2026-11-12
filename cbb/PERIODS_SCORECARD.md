# CBB period scorecard — halves and half team totals

Generated 2026-11-12 18:33 UTC. 775 graded period markets (72 had no unique final matched and are not graded).

Retail lines from the FanDuel event feed, sharp reference from Pinnacle at
period 1. Second-half markets settle **including overtime**, which is how
FanDuel grades them, and the finals file carries `h1a`/`h1h` so the second half
is simply final minus first half.

**There are no tickets/money splits on any period market** — the Action Network
splits feed is full-game only — so every signal here is handicap or price.
Pinnacle covers the first half only, so 2nd-half markets run on FanDuel's own
movement alone.

Base rates on this sample:

- **spread**: default side won 49.1% (n=214)
- **total**: default side won 50.9% (n=159)
- **ml**: default side won 73.3% (n=135)
- **tt_home**: default side won 59.8% (n=132)
- **tt_away**: default side won 56.9% (n=130)
- **2h_tt_ot**: default side won 90.9% (n=11)
- **2h_tt_no_ot**: default side won 57.0% (n=251)

Proposals appear at 50 decided markets. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 60-47 | 56.1 | 50.0 | 6.0 | +5.08 | 4.7 | 0.23 | no edge shown yet |
| pin_price | 9-21 | 30.0 | 27.4 | 2.6 | +19.56 | 65.2 | 0.5 | keep collecting (30/50) |
| follow_move | 107-85-2 | 55.7 | 51.9 | 3.8 | +5.14 | 2.6 | -0.0 | no edge shown yet |
| fd_juice | 11-20 | 35.5 | 48.1 | -12.7 | -11.0 | -35.5 | 0.1 | keep collecting (31/50) |
| follow_move+pin_value | 2-3 | 40.0 | 49.8 | -9.8 | -1.15 | -23.1 | 0.2 | keep collecting (5/50) |
| follow_move+pin_price | 2-0 | 100.0 | 26.7 | 73.3 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 108-69 | 61.0 | 50.0 | 11.0 | +24.98 | 14.1 |  | PROMOTE: beats break-even and its own base rate |
| pin_price | 11-32-1 | 25.6 | 27.2 | -1.6 | +20.74 | 47.1 |  | keep collecting (43/50) |
| follow_move | 254-295-5 | 46.3 | 49.1 | -2.8 | -56.48 | -10.2 |  | DROP: below break-even |
| fd_juice | 36-62 | 36.7 | 48.9 | -12.1 | -32.34 | -33.0 |  | DROP: below break-even |
| follow_move+pin_price | 5-5-1 | 50.0 | 26.7 | 23.3 | +26.2 | 238.2 |  | keep collecting (10/50) |
| follow_move+pin_value | 11-7 | 61.1 | 49.7 | 11.4 | +2.84 | 15.8 |  | keep collecting (18/50) |

## By period and market

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 108-69 | 61.0 | 11.0 | 14.1 |
| pin_value | close | 1h|spread | 52-31 | 62.7 | 12.9 | 17.2 |
| pin_value | close | 1h|total | 56-38 | 59.6 | 9.4 | 11.4 |
| pin_price | close | 1h | 11-32-1 | 25.6 | -1.6 | 47.1 |
| pin_price | close | 1h|ml | 11-31-1 | 26.2 | -0.5 | 50.6 |
| pin_price | close | 1h|spread | 0-1 | 0.0 | -49.1 | -100.0 |
| follow_move | close | 1h | 148-143-5 | 50.9 | 1.5 | -0.7 |
| follow_move | close | 1h|ml | 54-60-5 | 47.4 | -1.0 | -3.3 |
| follow_move | close | 1h|spread | 40-31 | 56.3 | 6.3 | 7.4 |
| follow_move | close | 1h|total | 54-52 | 50.9 | 1.1 | -3.1 |
| follow_move | close | 2h | 106-152 | 41.1 | -7.7 | -21.1 |
| follow_move | close | 2h OT game | 1-6 | 14.3 | -29.5 | -72.2 |
| follow_move | close | 2h no OT | 105-146 | 41.8 | -7.1 | -19.7 |
| follow_move | close | 2h|spread | 36-43 | 45.6 | -4.5 | -12.4 |
| follow_move | close | 2h|tt_away | 33-56 | 37.1 | -11.8 | -28.8 |
| follow_move | close | 2h|tt_home | 37-53 | 41.1 | -6.5 | -21.1 |
| fd_juice | close | 1h | 1-5 | 16.7 | -33.0 | -69.5 |
| fd_juice | close | 1h|spread | 0-4 | 0.0 | -50.0 | -100.0 |
| fd_juice | close | 1h|total | 1-1 | 50.0 | 0.9 | -8.4 |
| fd_juice | close | 2h | 35-57 | 38.0 | -10.8 | -30.6 |
| fd_juice | close | 2h OT game | 0-4 | 0.0 | -45.8 | -100.0 |
| fd_juice | close | 2h no OT | 35-53 | 39.8 | -9.2 | -27.5 |
| fd_juice | close | 2h|spread | 4-5 | 44.4 | -5.7 | -18.2 |
| fd_juice | close | 2h|tt_away | 20-21 | 48.8 | -2.4 | -11.0 |
| fd_juice | close | 2h|tt_home | 11-31 | 26.2 | -20.1 | -52.5 |
| follow_move+pin_price | close | 1h | 5-5-1 | 50.0 | 23.3 | 238.2 |
| follow_move+pin_value | close | 1h | 11-7 | 61.1 | 11.4 | 15.8 |
| follow_move+pin_price | close | 1h|ml | 5-5-1 | 50.0 | 23.3 | 238.2 |
| follow_move+pin_value | close | 1h|spread | 6-3 | 66.7 | 17.0 | 25.8 |
| follow_move+pin_value | close | 1h|total | 5-4 | 55.6 | 5.9 | 5.7 |
| pin_value | early | 1h | 60-47 | 56.1 | 6.0 | 4.7 |
| pin_value | early | 1h|spread | 25-21 | 54.3 | 4.6 | 1.5 |
| pin_value | early | 1h|total | 35-26 | 57.4 | 7.1 | 7.2 |
| pin_price | early | 1h | 9-21 | 30.0 | 2.6 | 65.2 |
| pin_price | early | 1h|ml | 9-20 | 31.0 | 4.4 | 70.9 |
| pin_price | early | 1h|total | 0-1 | 0.0 | -49.1 | -100.0 |
| follow_move | early | 1h | 71-45-2 | 61.2 | 7.1 | 9.9 |
| follow_move | early | 1h|ml | 34-21-2 | 61.8 | 2.9 | 4.3 |
| follow_move | early | 1h|spread | 20-5 | 80.0 | 30.3 | 52.7 |
| follow_move | early | 1h|total | 17-19 | 47.2 | -2.6 | -10.9 |
| follow_move | early | 2h | 36-40 | 47.4 | -1.2 | -8.6 |
| follow_move | early | 2h no OT | 36-40 | 47.4 | -1.2 | -8.6 |
| follow_move | early | 2h|spread | 11-11 | 50.0 | 0.5 | -4.2 |
| follow_move | early | 2h|tt_away | 11-14 | 44.0 | -4.1 | -15.5 |
| follow_move | early | 2h|tt_home | 14-15 | 48.3 | -0.0 | -6.0 |
| fd_juice | early | 1h | 1-0 | 100.0 | 49.1 | 83.3 |
| fd_juice | early | 1h|total | 1-0 | 100.0 | 49.1 | 83.3 |
| fd_juice | early | 2h | 10-20 | 33.3 | -14.7 | -39.4 |
| fd_juice | early | 2h no OT | 10-20 | 33.3 | -14.7 | -39.4 |
| fd_juice | early | 2h|spread | 0-2 | 0.0 | -50.0 | -100.0 |
| fd_juice | early | 2h|tt_away | 6-7 | 46.2 | -0.1 | -16.8 |
| fd_juice | early | 2h|tt_home | 4-11 | 26.7 | -22.7 | -50.9 |
| follow_move+pin_value | early | 1h | 2-3 | 40.0 | -9.8 | -23.1 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 73.3 | 610.0 |
| follow_move+pin_price | early | 1h|ml | 2-0 | 100.0 | 73.3 | 610.0 |
| follow_move+pin_value | early | 1h|spread | 1-1 | 50.0 | 0.0 | -1.9 |
| follow_move+pin_value | early | 1h|total | 1-2 | 33.3 | -16.4 | -37.2 |
