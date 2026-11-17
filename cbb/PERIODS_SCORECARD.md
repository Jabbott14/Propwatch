# CBB period scorecard — halves and half team totals

Generated 2026-11-17 16:19 UTC. 1179 graded period markets (120 had no unique final matched and are not graded).

Retail lines from the FanDuel event feed, sharp reference from Pinnacle at
period 1. Second-half markets settle **including overtime**, which is how
FanDuel grades them, and the finals file carries `h1a`/`h1h` so the second half
is simply final minus first half.

**There are no tickets/money splits on any period market** — the Action Network
splits feed is full-game only — so every signal here is handicap or price.
Pinnacle covers the first half only, so 2nd-half markets run on FanDuel's own
movement alone.

Base rates on this sample:

- **spread**: default side won 47.9% (n=338)
- **total**: default side won 50.0% (n=234)
- **ml**: default side won 71.3% (n=209)
- **tt_home**: default side won 52.3% (n=195)
- **tt_away**: default side won 49.7% (n=197)
- **2h_tt_ot**: default side won 92.3% (n=13)
- **2h_tt_no_ot**: default side won 49.6% (n=379)

Proposals appear at 50 decided markets. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 69-61 | 53.1 | 49.8 | 3.3 | -1.14 | -0.9 | 0.22 | no edge shown yet |
| pin_price | 10-27 | 27.0 | 29.3 | -2.3 | +17.16 | 46.4 | 0.59 | keep collecting (37/50) |
| follow_move | 140-118-3 | 54.3 | 51.2 | 3.1 | +2.52 | 1.0 | -0.04 | no edge shown yet |
| fd_juice | 17-31 | 35.4 | 50.1 | -14.7 | -17.07 | -35.6 | 0.17 | keep collecting (48/50) |
| follow_move+pin_value | 3-3 | 50.0 | 50.3 | -0.3 | -0.29 | -4.9 | 0.17 | keep collecting (6/50) |
| follow_move+pin_price | 2-0 | 100.0 | 28.7 | 71.3 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 143-120 | 54.4 | 49.7 | 4.6 | +4.18 | 1.6 |  | no edge shown yet |
| pin_price | 15-47-1 | 24.2 | 29.4 | -5.2 | +19.34 | 30.7 |  | DROP: below break-even |
| follow_move | 404-458-6 | 46.9 | 49.1 | -2.2 | -47.59 | -5.5 |  | DROP: below break-even |
| fd_juice | 62-81 | 43.4 | 49.7 | -6.3 | -29.58 | -20.7 |  | DROP: below break-even |
| follow_move+pin_price | 8-12-1 | 40.0 | 28.7 | 11.3 | +29.3 | 139.5 |  | keep collecting (20/50) |
| follow_move+pin_value | 13-14 | 48.1 | 49.9 | -1.8 | -2.48 | -9.2 |  | keep collecting (27/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 47.9 | -47.9 | -1.0 | -100.0 |  | keep collecting (1/50) |

## By period and market

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 143-120 | 54.4 | 4.6 | 1.6 |
| pin_value | close | 1h|spread | 68-61 | 52.7 | 3.2 | -1.7 |
| pin_value | close | 1h|total | 75-59 | 56.0 | 6.0 | 4.7 |
| pin_price | close | 1h | 15-47-1 | 24.2 | -5.2 | 30.7 |
| pin_price | close | 1h|ml | 15-45-1 | 25.0 | -3.7 | 35.0 |
| pin_price | close | 1h|spread | 0-1 | 0.0 | -47.9 | -100.0 |
| pin_price | close | 1h|total | 0-1 | 0.0 | -50.0 | -100.0 |
| follow_move | close | 1h | 225-234-6 | 49.0 | 0.6 | 2.7 |
| follow_move | close | 1h|ml | 87-97-6 | 47.3 | 1.4 | 12.8 |
| follow_move | close | 1h|spread | 67-53 | 55.8 | 5.6 | 6.9 |
| follow_move | close | 1h|total | 71-84 | 45.8 | -4.2 | -13.1 |
| follow_move | close | 2h | 179-224 | 44.4 | -5.5 | -14.9 |
| follow_move | close | 2h OT game | 2-6 | 25.0 | -24.5 | -51.0 |
| follow_move | close | 2h no OT | 177-218 | 44.8 | -5.1 | -14.2 |
| follow_move | close | 2h|spread | 59-67 | 46.8 | -3.3 | -10.1 |
| follow_move | close | 2h|tt_away | 59-79 | 42.8 | -7.3 | -18.3 |
| follow_move | close | 2h|tt_home | 61-78 | 43.9 | -5.6 | -15.9 |
| fd_juice | close | 1h | 6-8 | 42.9 | -7.7 | -21.1 |
| fd_juice | close | 1h|spread | 5-7 | 41.7 | -9.0 | -23.3 |
| fd_juice | close | 1h|total | 1-1 | 50.0 | 0.0 | -8.4 |
| fd_juice | close | 2h | 56-73 | 43.4 | -6.2 | -20.6 |
| fd_juice | close | 2h OT game | 1-4 | 20.0 | -29.5 | -63.1 |
| fd_juice | close | 2h no OT | 55-69 | 44.4 | -5.2 | -18.9 |
| fd_juice | close | 2h|spread | 7-7 | 50.0 | -0.6 | -7.7 |
| fd_juice | close | 2h|tt_away | 30-29 | 50.8 | 0.9 | -7.2 |
| fd_juice | close | 2h|tt_home | 19-37 | 33.9 | -15.0 | -38.0 |
| follow_move+pin_price | close | 1h | 8-12-1 | 40.0 | 11.3 | 139.5 |
| follow_move+pin_value | close | 1h | 13-14 | 48.1 | -1.8 | -9.2 |
| fd_juice+pin_value | close | 1h | 0-1 | 0.0 | -47.9 | -100.0 |
| follow_move+pin_price | close | 1h|ml | 8-12-1 | 40.0 | 11.3 | 139.5 |
| follow_move+pin_value | close | 1h|spread | 8-5 | 61.5 | 11.7 | 15.4 |
| fd_juice+pin_value | close | 1h|spread | 0-1 | 0.0 | -47.9 | -100.0 |
| follow_move+pin_value | close | 1h|total | 5-9 | 35.7 | -14.3 | -32.0 |
| pin_value | early | 1h | 69-61 | 53.1 | 3.3 | -0.9 |
| pin_value | early | 1h|spread | 33-26 | 55.9 | 6.5 | 4.5 |
| pin_value | early | 1h|total | 36-35 | 50.7 | 0.7 | -5.3 |
| pin_price | early | 1h | 10-27 | 27.0 | -2.3 | 46.4 |
| pin_price | early | 1h|ml | 10-26 | 27.8 | -0.9 | 50.4 |
| pin_price | early | 1h|total | 0-1 | 0.0 | -50.0 | -100.0 |
| follow_move | early | 1h | 86-67-3 | 56.2 | 3.9 | 2.1 |
| follow_move | early | 1h|ml | 41-34-3 | 54.7 | -0.2 | -5.7 |
| follow_move | early | 1h|spread | 26-9 | 74.3 | 24.6 | 42.5 |
| follow_move | early | 1h|total | 19-24 | 44.2 | -5.8 | -16.5 |
| follow_move | early | 2h | 54-51 | 51.4 | 1.9 | -0.8 |
| follow_move | early | 2h no OT | 54-51 | 51.4 | 1.9 | -0.8 |
| follow_move | early | 2h|spread | 17-14 | 54.8 | 5.7 | 5.3 |
| follow_move | early | 2h|tt_away | 16-19 | 45.7 | -4.4 | -11.4 |
| follow_move | early | 2h|tt_home | 21-18 | 53.8 | 4.4 | 4.0 |
| fd_juice | early | 1h | 2-1 | 66.7 | 17.4 | 22.7 |
| fd_juice | early | 1h|spread | 1-0 | 100.0 | 52.1 | 84.7 |
| fd_juice | early | 1h|total | 1-1 | 50.0 | 0.0 | -8.4 |
| fd_juice | early | 2h | 15-30 | 33.3 | -16.8 | -39.4 |
| fd_juice | early | 2h no OT | 15-30 | 33.3 | -16.8 | -39.4 |
| fd_juice | early | 2h|spread | 0-3 | 0.0 | -50.7 | -100.0 |
| fd_juice | early | 2h|tt_away | 9-12 | 42.9 | -7.2 | -22.8 |
| fd_juice | early | 2h|tt_home | 6-15 | 28.6 | -21.5 | -47.4 |
| follow_move+pin_value | early | 1h | 3-3 | 50.0 | -0.3 | -4.9 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 71.3 | 610.0 |
| follow_move+pin_price | early | 1h|ml | 2-0 | 100.0 | 71.3 | 610.0 |
| follow_move+pin_value | early | 1h|spread | 2-1 | 66.7 | 16.0 | 27.5 |
| follow_move+pin_value | early | 1h|total | 1-2 | 33.3 | -16.7 | -37.2 |
