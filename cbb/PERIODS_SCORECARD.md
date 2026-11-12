# CBB period scorecard — halves and half team totals

Generated 2026-11-12 06:44 UTC. 722 graded period markets (156 had no unique final matched and are not graded).

Retail lines from the FanDuel event feed, sharp reference from Pinnacle at
period 1. Second-half markets settle **including overtime**, which is how
FanDuel grades them, and the finals file carries `h1a`/`h1h` so the second half
is simply final minus first half.

**There are no tickets/money splits on any period market** — the Action Network
splits feed is full-game only — so every signal here is handicap or price.
Pinnacle covers the first half only, so 2nd-half markets run on FanDuel's own
movement alone.

Base rates on this sample:

- **spread**: default side won 49.5% (n=202)
- **total**: default side won 51.4% (n=144)
- **ml**: default side won 75.2% (n=125)
- **tt_home**: default side won 60.5% (n=124)
- **tt_away**: default side won 58.2% (n=122)
- **2h_tt_ot**: default side won 90.9% (n=11)
- **2h_tt_no_ot**: default side won 57.9% (n=235)

Proposals appear at 50 decided markets. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 57-42 | 57.6 | 50.1 | 7.5 | +7.42 | 7.5 | 0.22 | no edge shown yet |
| pin_price | 8-19 | 29.6 | 26.7 | 3.0 | +17.66 | 65.4 | 0.53 | keep collecting (27/50) |
| follow_move | 103-72-2 | 58.9 | 51.7 | 7.1 | +15.74 | 8.9 | 0.01 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 10-20 | 33.3 | 48.1 | -14.7 | -11.8 | -39.3 | 0.1 | keep collecting (30/50) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 99-62 | 61.5 | 50.1 | 11.4 | +26.05 | 16.2 |  | PROMOTE: beats break-even and its own base rate |
| pin_price | 10-29-1 | 25.6 | 26.1 | -0.4 | +19.24 | 48.1 |  | keep collecting (39/50) |
| follow_move | 241-272-5 | 47.0 | 48.8 | -1.8 | -43.57 | -8.4 |  | DROP: below break-even |
| fd_juice | 33-61 | 35.1 | 48.8 | -13.7 | -33.78 | -35.9 |  | DROP: below break-even |

## By period and market

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 99-62 | 61.5 | 11.4 | 16.2 |
| pin_value | close | 1h|spread | 46-32 | 59.0 | 9.1 | 11.5 |
| pin_value | close | 1h|total | 53-30 | 63.9 | 13.6 | 20.5 |
| pin_price | close | 1h | 10-29-1 | 25.6 | -0.4 | 48.1 |
| pin_price | close | 1h|ml | 9-28-1 | 24.3 | -0.5 | 50.7 |
| pin_price | close | 1h|spread | 1-1 | 50.0 | 0.5 | -1.0 |
| follow_move | close | 1h | 139-134-5 | 50.9 | 2.1 | 0.2 |
| follow_move | close | 1h|ml | 50-58-5 | 46.3 | -0.9 | -3.4 |
| follow_move | close | 1h|spread | 39-30 | 56.5 | 6.5 | 7.8 |
| follow_move | close | 1h|total | 50-46 | 52.1 | 2.3 | -0.9 |
| follow_move | close | 2h | 102-138 | 42.5 | -6.2 | -18.4 |
| follow_move | close | 2h OT game | 1-6 | 14.3 | -28.9 | -72.2 |
| follow_move | close | 2h no OT | 101-132 | 43.3 | -5.6 | -16.8 |
| follow_move | close | 2h|spread | 35-38 | 47.9 | -2.1 | -7.8 |
| follow_move | close | 2h|tt_away | 32-52 | 38.1 | -10.9 | -27.0 |
| follow_move | close | 2h|tt_home | 35-48 | 42.2 | -5.2 | -19.1 |
| fd_juice | close | 1h | 1-5 | 16.7 | -32.9 | -69.5 |
| fd_juice | close | 1h|spread | 0-4 | 0.0 | -50.0 | -100.0 |
| fd_juice | close | 1h|total | 1-1 | 50.0 | 1.4 | -8.4 |
| fd_juice | close | 2h | 32-56 | 36.4 | -12.4 | -33.6 |
| fd_juice | close | 2h OT game | 0-4 | 0.0 | -45.3 | -100.0 |
| fd_juice | close | 2h no OT | 32-52 | 38.1 | -10.8 | -30.5 |
| fd_juice | close | 2h|spread | 4-5 | 44.4 | -5.6 | -18.2 |
| fd_juice | close | 2h|tt_away | 17-21 | 44.7 | -7.0 | -18.3 |
| fd_juice | close | 2h|tt_home | 11-30 | 26.8 | -18.8 | -51.3 |
| pin_value | early | 1h | 57-42 | 57.6 | 7.5 | 7.5 |
| pin_value | early | 1h|spread | 22-22 | 50.0 | 0.2 | -6.6 |
| pin_value | early | 1h|total | 35-20 | 63.6 | 13.3 | 18.8 |
| pin_price | early | 1h | 8-19 | 29.6 | 3.0 | 65.4 |
| pin_price | early | 1h|ml | 8-17 | 32.0 | 7.2 | 78.6 |
| pin_price | early | 1h|total | 0-2 | 0.0 | -50.0 | -100.0 |
| follow_move | early | 1h | 68-36-2 | 65.4 | 11.4 | 18.2 |
| follow_move | early | 1h|ml | 32-19-2 | 62.7 | 4.3 | 7.3 |
| follow_move | early | 1h|spread | 19-4 | 82.6 | 32.7 | 58.1 |
| follow_move | early | 1h|total | 17-13 | 56.7 | 6.9 | 6.9 |
| follow_move | early | 2h | 35-36 | 49.3 | 1.0 | -5.0 |
| follow_move | early | 2h no OT | 35-36 | 49.3 | 1.0 | -5.0 |
| follow_move | early | 2h|spread | 11-10 | 52.4 | 2.6 | 0.4 |
| follow_move | early | 2h|tt_away | 11-13 | 45.8 | -2.1 | -12.0 |
| follow_move | early | 2h|tt_home | 13-13 | 50.0 | 2.4 | -2.8 |
| fd_juice | early | 1h | 1-0 | 100.0 | 48.6 | 83.3 |
| fd_juice | early | 1h|total | 1-0 | 100.0 | 48.6 | 83.3 |
| fd_juice | early | 2h | 9-20 | 31.0 | -16.9 | -43.5 |
| fd_juice | early | 2h no OT | 9-20 | 31.0 | -16.9 | -43.5 |
| fd_juice | early | 2h|spread | 0-2 | 0.0 | -50.0 | -100.0 |
| fd_juice | early | 2h|tt_away | 5-7 | 41.7 | -4.2 | -24.9 |
| fd_juice | early | 2h|tt_home | 4-11 | 26.7 | -22.6 | -50.9 |
