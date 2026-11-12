# CBB period scorecard — halves and half team totals

Generated 2026-11-12 06:34 UTC. 722 graded period markets (156 had no unique final matched and are not graded).

Retail lines from the FanDuel event feed, sharp reference from Pinnacle at
period 1. Second-half markets settle **including overtime**, which is how
FanDuel grades them, and the finals file carries `h1a`/`h1h` so the second half
is simply final minus first half.

**There are no tickets/money splits on any period market** — the Action Network
splits feed is full-game only — so every signal here is handicap or price.
Pinnacle covers the first half only, so 2nd-half markets run on FanDuel's own
movement alone.

Base rates on this sample:

- **spread**: default side won 53.2% (n=126)
- **total**: default side won 58.2% (n=91)
- **ml**: default side won 72.9% (n=48)
- **tt_home**: default side won 46.5% (n=43)
- **tt_away**: default side won 48.3% (n=60)

Proposals appear at 50 decided markets. Nothing changes automatically.

## EARLY

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 57-42 | 57.6 | 51.7 | 5.9 | +7.42 | 7.5 | 0.22 | no edge shown yet |
| pin_price | 8-19 | 29.6 | 28.8 | 0.8 | +17.66 | 65.4 | 0.53 | keep collecting (27/50) |
| follow_move | 103-72-2 | 58.9 | 52.4 | 6.4 | +15.74 | 8.9 | 0.01 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 10-20 | 33.3 | 50.7 | -17.4 | -11.8 | -39.3 | 0.1 | keep collecting (30/50) |

## CLOSE

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 99-62 | 61.5 | 51.2 | 10.2 | +26.05 | 16.2 |  | PROMOTE: beats break-even and its own base rate |
| pin_price | 10-29-1 | 25.6 | 28.4 | -2.8 | +19.24 | 48.1 |  | keep collecting (39/50) |
| follow_move | 241-272-5 | 47.0 | 49.4 | -2.4 | -43.57 | -8.4 |  | DROP: below break-even |
| fd_juice | 33-61 | 35.1 | 50.3 | -15.2 | -33.78 | -35.9 |  | INVERT candidate: wrong well beyond its base rate |

## By period and market

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 99-62 | 61.5 | 10.2 | 16.2 |
| pin_value | close | 1h|spread | 46-32 | 59.0 | 8.0 | 11.5 |
| pin_value | close | 1h|total | 53-30 | 63.9 | 12.4 | 20.5 |
| pin_price | close | 1h | 10-29-1 | 25.6 | -2.8 | 48.1 |
| pin_price | close | 1h|ml | 9-28-1 | 24.3 | -2.8 | 50.7 |
| pin_price | close | 1h|spread | 1-1 | 50.0 | -3.2 | -1.0 |
| follow_move | close | 1h | 139-134-5 | 50.9 | 2.3 | 0.2 |
| follow_move | close | 1h|ml | 50-58-5 | 46.3 | -1.2 | -3.4 |
| follow_move | close | 1h|spread | 39-30 | 56.5 | 6.8 | 7.8 |
| follow_move | close | 1h|total | 50-46 | 52.1 | 3.1 | -0.9 |
| follow_move | close | 2h | 102-138 | 42.5 | -7.8 | -18.4 |
| follow_move | close | 2h|spread | 35-38 | 47.9 | -1.9 | -7.8 |
| follow_move | close | 2h|tt_away | 32-52 | 38.1 | -12.1 | -27.0 |
| follow_move | close | 2h|tt_home | 35-48 | 42.2 | -8.7 | -19.1 |
| fd_juice | close | 1h | 1-5 | 16.7 | -30.6 | -69.5 |
| fd_juice | close | 1h|spread | 0-4 | 0.0 | -50.0 | -100.0 |
| fd_juice | close | 1h|total | 1-1 | 50.0 | 8.2 | -8.4 |
| fd_juice | close | 2h | 32-56 | 36.4 | -14.1 | -33.6 |
| fd_juice | close | 2h|spread | 4-5 | 44.4 | -5.2 | -18.2 |
| fd_juice | close | 2h|tt_away | 17-21 | 44.7 | -4.9 | -18.3 |
| fd_juice | close | 2h|tt_home | 11-30 | 26.8 | -24.6 | -51.3 |
| pin_value | early | 1h | 57-42 | 57.6 | 5.9 | 7.5 |
| pin_value | early | 1h|spread | 22-22 | 50.0 | -1.3 | -6.6 |
| pin_value | early | 1h|total | 35-20 | 63.6 | 11.7 | 18.8 |
| pin_price | early | 1h | 8-19 | 29.6 | 0.8 | 65.4 |
| pin_price | early | 1h|ml | 8-17 | 32.0 | 4.9 | 78.6 |
| pin_price | early | 1h|total | 0-2 | 0.0 | -50.0 | -100.0 |
| follow_move | early | 1h | 68-36-2 | 65.4 | 12.0 | 18.2 |
| follow_move | early | 1h|ml | 32-19-2 | 62.7 | 5.1 | 7.3 |
| follow_move | early | 1h|spread | 19-4 | 82.6 | 31.9 | 58.1 |
| follow_move | early | 1h|total | 17-13 | 56.7 | 8.3 | 6.9 |
| follow_move | early | 2h | 35-36 | 49.3 | -1.6 | -5.0 |
| follow_move | early | 2h|spread | 11-10 | 52.4 | 0.7 | 0.4 |
| follow_move | early | 2h|tt_away | 11-13 | 45.8 | -4.6 | -12.0 |
| follow_move | early | 2h|tt_home | 13-13 | 50.0 | -0.8 | -2.8 |
| fd_juice | early | 1h | 1-0 | 100.0 | 41.8 | 83.3 |
| fd_juice | early | 1h|total | 1-0 | 100.0 | 41.8 | 83.3 |
| fd_juice | early | 2h | 9-20 | 31.0 | -19.4 | -43.5 |
| fd_juice | early | 2h|spread | 0-2 | 0.0 | -50.0 | -100.0 |
| fd_juice | early | 2h|tt_away | 5-7 | 41.7 | -9.2 | -24.9 |
| fd_juice | early | 2h|tt_home | 4-11 | 26.7 | -23.6 | -50.9 |
