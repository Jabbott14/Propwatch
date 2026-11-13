# CBB period scorecard — halves and half team totals

Generated 2026-11-13 17:18 UTC. 830 graded period markets (84 had no unique final matched and are not graded).

Retail lines from the FanDuel event feed, sharp reference from Pinnacle at
period 1. Second-half markets settle **including overtime**, which is how
FanDuel grades them, and the finals file carries `h1a`/`h1h` so the second half
is simply final minus first half.

**There are no tickets/money splits on any period market** — the Action Network
splits feed is full-game only — so every signal here is handicap or price.
Pinnacle covers the first half only, so 2nd-half markets run on FanDuel's own
movement alone.

Base rates on this sample:

- **spread**: default side won 48.7% (n=230)
- **total**: default side won 50.6% (n=168)
- **ml**: default side won 74.0% (n=146)
- **tt_home**: default side won 57.4% (n=141)
- **tt_away**: default side won 55.4% (n=139)
- **2h_tt_ot**: default side won 90.9% (n=11)
- **2h_tt_no_ot**: default side won 55.0% (n=269)

Proposals appear at 50 decided markets. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 61-50 | 55.0 | 49.9 | 5.1 | +2.99 | 2.7 | 0.24 | no edge shown yet |
| pin_price | 9-21 | 30.0 | 26.8 | 3.2 | +19.56 | 65.2 | 0.5 | keep collecting (30/50) |
| follow_move | 118-93-3 | 55.9 | 52.1 | 3.9 | +6.18 | 2.9 | -0.06 | no edge shown yet |
| fd_juice | 14-25 | 35.9 | 49.1 | -13.2 | -13.55 | -34.7 | 0.03 | keep collecting (39/50) |
| follow_move+pin_value | 2-3 | 40.0 | 49.9 | -9.9 | -1.15 | -23.1 | 0.2 | keep collecting (5/50) |
| follow_move+pin_price | 2-0 | 100.0 | 26.0 | 74.0 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 113-73 | 60.8 | 49.9 | 10.9 | +25.29 | 13.6 |  | PROMOTE: beats break-even and its own base rate |
| pin_price | 12-34-1 | 26.1 | 26.5 | -0.4 | +22.24 | 47.3 |  | keep collecting (46/50) |
| follow_move | 277-321-6 | 46.3 | 49.2 | -2.9 | -64.33 | -10.7 |  | DROP: below break-even |
| fd_juice | 39-63 | 38.2 | 49.1 | -10.9 | -30.91 | -30.3 |  | DROP: below break-even |
| follow_move+pin_price | 5-7-1 | 41.7 | 26.0 | 15.6 | +24.2 | 186.2 |  | keep collecting (12/50) |
| follow_move+pin_value | 12-8 | 60.0 | 49.7 | 10.3 | +2.68 | 13.4 |  | keep collecting (20/50) |

## By period and market

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 113-73 | 60.8 | 10.9 | 13.6 |
| pin_value | close | 1h|spread | 55-33 | 62.5 | 12.9 | 16.8 |
| pin_value | close | 1h|total | 58-40 | 59.2 | 9.1 | 10.7 |
| pin_price | close | 1h | 12-34-1 | 26.1 | -0.4 | 47.3 |
| pin_price | close | 1h|ml | 12-33-1 | 26.7 | 0.6 | 50.5 |
| pin_price | close | 1h|spread | 0-1 | 0.0 | -48.7 | -100.0 |
| follow_move | close | 1h | 159-159-6 | 50.0 | 0.7 | -3.3 |
| follow_move | close | 1h|ml | 59-66-6 | 47.2 | -1.1 | -6.1 |
| follow_move | close | 1h|spread | 44-35 | 55.7 | 5.6 | 6.2 |
| follow_move | close | 1h|total | 56-58 | 49.1 | -0.8 | -6.6 |
| follow_move | close | 2h | 118-162 | 42.1 | -6.9 | -19.2 |
| follow_move | close | 2h OT game | 1-6 | 14.3 | -31.0 | -72.2 |
| follow_move | close | 2h no OT | 117-156 | 42.9 | -6.3 | -17.8 |
| follow_move | close | 2h|spread | 38-47 | 44.7 | -5.3 | -14.2 |
| follow_move | close | 2h|tt_away | 37-59 | 38.5 | -10.4 | -26.0 |
| follow_move | close | 2h|tt_home | 43-56 | 43.4 | -5.0 | -16.8 |
| fd_juice | close | 1h | 2-6 | 25.0 | -24.9 | -54.2 |
| fd_juice | close | 1h|spread | 1-5 | 16.7 | -33.3 | -69.5 |
| fd_juice | close | 1h|total | 1-1 | 50.0 | 0.6 | -8.4 |
| fd_juice | close | 2h | 37-57 | 39.4 | -9.7 | -28.3 |
| fd_juice | close | 2h OT game | 0-4 | 0.0 | -46.8 | -100.0 |
| fd_juice | close | 2h no OT | 37-53 | 41.1 | -8.0 | -25.1 |
| fd_juice | close | 2h|spread | 4-5 | 44.4 | -5.7 | -18.2 |
| fd_juice | close | 2h|tt_away | 22-21 | 51.2 | 0.5 | -6.7 |
| fd_juice | close | 2h|tt_home | 11-31 | 26.2 | -21.0 | -52.5 |
| follow_move+pin_price | close | 1h | 5-7-1 | 41.7 | 15.6 | 186.2 |
| follow_move+pin_value | close | 1h | 12-8 | 60.0 | 10.3 | 13.4 |
| follow_move+pin_price | close | 1h|ml | 5-7-1 | 41.7 | 15.6 | 186.2 |
| follow_move+pin_value | close | 1h|spread | 7-3 | 70.0 | 20.5 | 31.7 |
| follow_move+pin_value | close | 1h|total | 5-5 | 50.0 | 0.1 | -4.8 |
| pin_value | early | 1h | 61-50 | 55.0 | 5.1 | 2.7 |
| pin_value | early | 1h|spread | 26-22 | 54.2 | 4.6 | 1.3 |
| pin_value | early | 1h|total | 35-28 | 55.6 | 5.4 | 3.8 |
| pin_price | early | 1h | 9-21 | 30.0 | 3.2 | 65.2 |
| pin_price | early | 1h|ml | 9-20 | 31.0 | 5.0 | 70.9 |
| pin_price | early | 1h|total | 0-1 | 0.0 | -49.4 | -100.0 |
| follow_move | early | 1h | 75-49-3 | 60.5 | 6.3 | 8.1 |
| follow_move | early | 1h|ml | 36-24-3 | 60.0 | 1.2 | 0.2 |
| follow_move | early | 1h|spread | 21-6 | 77.8 | 28.1 | 48.8 |
| follow_move | early | 1h|total | 18-19 | 48.6 | -1.3 | -8.2 |
| follow_move | early | 2h | 43-44 | 49.4 | 0.3 | -4.7 |
| follow_move | early | 2h no OT | 43-44 | 49.4 | 0.3 | -4.7 |
| follow_move | early | 2h|spread | 13-12 | 52.0 | 2.7 | 0.1 |
| follow_move | early | 2h|tt_away | 12-16 | 42.9 | -6.0 | -17.6 |
| follow_move | early | 2h|tt_home | 18-16 | 52.9 | 3.8 | 2.5 |
| fd_juice | early | 1h | 2-1 | 66.7 | 16.7 | 22.7 |
| fd_juice | early | 1h|spread | 1-0 | 100.0 | 51.3 | 84.7 |
| fd_juice | early | 1h|total | 1-1 | 50.0 | -0.6 | -8.4 |
| fd_juice | early | 2h | 12-24 | 33.3 | -15.7 | -39.5 |
| fd_juice | early | 2h no OT | 12-24 | 33.3 | -15.7 | -39.5 |
| fd_juice | early | 2h|spread | 0-3 | 0.0 | -50.4 | -100.0 |
| fd_juice | early | 2h|tt_away | 8-9 | 47.1 | -0.7 | -15.2 |
| fd_juice | early | 2h|tt_home | 4-12 | 25.0 | -25.0 | -54.0 |
| follow_move+pin_value | early | 1h | 2-3 | 40.0 | -9.9 | -23.1 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 74.0 | 610.0 |
| follow_move+pin_price | early | 1h|ml | 2-0 | 100.0 | 74.0 | 610.0 |
| follow_move+pin_value | early | 1h|spread | 1-1 | 50.0 | 0.0 | -1.9 |
| follow_move+pin_value | early | 1h|total | 1-2 | 33.3 | -16.5 | -37.2 |
