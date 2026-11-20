# CBB period scorecard — halves and half team totals

Generated 2026-11-20 20:37 UTC. 1499 graded period markets (162 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 380 on or after it (forward).** Every signal and threshold here was chosen by looking at the
fit markets, so a label there is a **hypothesis**; only the forward table is
**evidence**. Base rates are measured separately in each period.

Retail lines from the FanDuel event feed, sharp reference from Pinnacle at
period 1. Second-half markets settle **including overtime**, which is how
FanDuel grades them, and the finals file carries `h1a`/`h1h` so the second half
is simply final minus first half.

**There are no tickets/money splits on any period market** — the Action Network
splits feed is full-game only — so every signal here is handicap or price.
Pinnacle covers the first half only, so 2nd-half markets run on FanDuel's own
movement alone.

Base rates on this sample:

- **spread**: default side won 48.3% (n=437)
- **total**: default side won 50.5% (n=299)
- **ml**: default side won 70.3% (n=263)
- **tt_home**: default side won 51.9% (n=241)
- **tt_away**: default side won 52.6% (n=251)
- **2h_tt_ot**: default side won 88.9% (n=18)
- **2h_tt_no_ot**: default side won 50.8% (n=474)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 7-4 | 63.6 | 49.8 | 13.8 | +2.12 | 19.3 | 0.18 | keep collecting (11/50) |
| pin_price | 2-1-1 | 66.7 | 38.5 | 28.1 | +0.98 | 24.5 | 0.12 | keep collecting (3/50) |
| follow_move | 39-33-1 | 54.2 | 49.0 | 5.2 | +13.5 | 18.5 | 0.08 | no edge shown yet |
| fd_juice | 3-18 | 14.3 | 48.8 | -34.5 | -15.62 | -74.4 | 0.43 | keep collecting (21/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 35-39 | 47.3 | 49.8 | -2.5 | -8.71 | -11.8 |  | no edge shown yet |
| pin_price | 9-8-1 | 52.9 | 35.5 | 17.4 | +33.81 | 187.8 |  | keep collecting (17/50) |
| follow_move | 145-155-1 | 48.3 | 48.6 | -0.3 | +7.53 | 2.5 |  | no edge shown yet |
| fd_juice | 18-28 | 39.1 | 51.2 | -12.1 | -12.97 | -28.2 |  | keep collecting (46/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 47.9 | -47.9 | -1.0 | -100.0 |  | keep collecting (1/50) |
| follow_move+pin_price | 5-3 | 62.5 | 33.8 | 28.7 | +27.58 | 344.8 |  | keep collecting (8/50) |
| follow_move+pin_value | 10-7 | 58.8 | 50.4 | 8.4 | +1.59 | 9.4 |  | keep collecting (17/50) |

# FIT (in-sample — this is the hypothesis)

## EARLY  (fit)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 69-61 | 53.1 | 49.9 | 3.1 | -1.14 | -0.9 | 0.22 | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_price | 10-27 | 27.0 | 28.9 | -1.8 | +17.16 | 46.4 | 0.59 | keep collecting (37/50) |
| follow_move | 135-116-3 | 53.8 | 51.5 | 2.3 | -2.06 | -0.8 | -0.04 | HYPOTHESIS (in-sample) -- no edge shown yet |
| fd_juice | 17-29 | 37.0 | 50.1 | -13.1 | -15.07 | -32.8 | 0.15 | keep collecting (46/50) |
| follow_move+pin_value | 3-3 | 50.0 | 50.1 | -0.1 | -0.29 | -4.9 | 0.17 | keep collecting (6/50) |
| follow_move+pin_price | 2-0 | 100.0 | 28.3 | 71.7 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (fit)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 143-109 | 56.7 | 49.9 | 6.9 | +15.18 | 6.0 |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_price | 14-46-1 | 23.3 | 29.0 | -5.6 | +17.74 | 29.1 |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move | 381-434-6 | 46.7 | 49.3 | -2.5 | -48.02 | -5.8 |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| fd_juice | 59-75 | 44.0 | 49.8 | -5.8 | -26.14 | -19.5 |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+pin_price | 7-11-1 | 38.9 | 28.3 | 10.6 | +27.7 | 145.8 |  | keep collecting (18/50) |
| follow_move+pin_value | 13-13 | 50.0 | 49.9 | 0.1 | -1.48 | -5.7 |  | keep collecting (26/50) |

# Pooled (contaminated — mixes fit and forward)

## EARLY  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 76-65 | 53.9 | 49.9 | 4.0 | +0.98 | 0.7 | 0.21 | no edge shown yet |
| pin_price | 12-28-1 | 30.0 | 30.6 | -0.6 | +18.14 | 44.2 | 0.54 | keep collecting (40/50) |
| follow_move | 174-149-4 | 53.9 | 50.7 | 3.2 | +11.44 | 3.5 | -0.02 | no edge shown yet |
| fd_juice | 20-47 | 29.9 | 49.6 | -19.8 | -30.69 | -45.8 | 0.24 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-3 | 50.0 | 50.2 | -0.2 | -0.29 | -4.9 | 0.17 | keep collecting (6/50) |
| follow_move+pin_price | 2-0 | 100.0 | 29.7 | 70.3 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 178-148 | 54.6 | 49.8 | 4.8 | +6.47 | 2.0 |  | no edge shown yet |
| pin_price | 23-54-2 | 29.9 | 30.6 | -0.8 | +51.55 | 65.3 |  | DROP: below break-even |
| follow_move | 526-589-7 | 47.2 | 49.1 | -1.9 | -40.49 | -3.6 |  | DROP: below break-even |
| fd_juice | 77-103 | 42.8 | 49.9 | -7.1 | -39.12 | -21.7 |  | DROP: below break-even |
| follow_move+pin_price | 12-14-1 | 46.2 | 29.7 | 16.5 | +55.28 | 204.7 |  | keep collecting (26/50) |
| follow_move+pin_value | 23-20 | 53.5 | 50.0 | 3.5 | +0.11 | 0.2 |  | keep collecting (43/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 48.3 | -48.3 | -1.0 | -100.0 |  | keep collecting (1/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 178-148 | 54.6 | 4.8 | 2.0 |
| pin_value | close | 1h\|spread | 82-76 | 51.9 | 2.3 | -3.2 |
| pin_value | close | 1h\|total | 96-72 | 57.1 | 7.1 | 6.9 |
| pin_price | close | 1h | 23-54-2 | 29.9 | -0.8 | 65.3 |
| pin_price | close | 1h\|ml | 22-51-2 | 30.1 | 0.5 | 71.4 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -15.0 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.5 | -100.0 |
| follow_move | close | 1h | 310-297-7 | 51.1 | 2.5 | 8.6 |
| follow_move | close | 1h\|ml | 112-123-7 | 47.7 | 1.4 | 20.0 |
| follow_move | close | 1h\|spread | 90-70 | 56.2 | 6.0 | 7.6 |
| follow_move | close | 1h\|total | 108-104 | 50.9 | 1.0 | -3.6 |
| follow_move | close | 2h | 216-292 | 42.5 | -7.2 | -18.4 |
| follow_move | close | 2h OT game | 4-8 | 33.3 | -15.9 | -34.8 |
| follow_move | close | 2h no OT | 212-284 | 42.7 | -7.0 | -18.0 |
| follow_move | close | 2h\|spread | 71-87 | 44.9 | -5.2 | -13.6 |
| follow_move | close | 2h\|tt_away | 72-107 | 40.2 | -9.2 | -23.0 |
| follow_move | close | 2h\|tt_home | 73-98 | 42.7 | -6.9 | -18.1 |
| fd_juice | close | 1h | 8-11 | 42.1 | -8.1 | -22.7 |
| fd_juice | close | 1h\|spread | 7-10 | 41.2 | -9.1 | -24.4 |
| fd_juice | close | 1h\|total | 1-1 | 50.0 | 0.5 | -8.4 |
| fd_juice | close | 2h | 69-92 | 42.9 | -7.0 | -21.6 |
| fd_juice | close | 2h OT game | 2-5 | 28.6 | -21.1 | -48.2 |
| fd_juice | close | 2h no OT | 67-87 | 43.5 | -6.4 | -20.4 |
| fd_juice | close | 2h\|spread | 10-9 | 52.6 | 2.4 | -2.9 |
| fd_juice | close | 2h\|tt_away | 33-39 | 45.8 | -4.5 | -16.5 |
| fd_juice | close | 2h\|tt_home | 26-44 | 37.1 | -12.1 | -32.0 |
| follow_move+pin_price | close | 1h | 12-14-1 | 46.2 | 16.5 | 204.7 |
| follow_move+pin_value | close | 1h | 23-20 | 53.5 | 3.5 | 0.2 |
| fd_juice+pin_value | close | 1h | 0-1 | 0.0 | -48.3 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 12-14-1 | 46.2 | 16.5 | 204.7 |
| follow_move+pin_value | close | 1h\|spread | 9-7 | 56.2 | 6.0 | 5.1 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -48.3 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 14-13 | 51.9 | 2.0 | -2.6 |
| pin_value | early | 1h | 76-65 | 53.9 | 4.0 | 0.7 |
| pin_value | early | 1h\|spread | 36-28 | 56.2 | 6.7 | 5.2 |
| pin_value | early | 1h\|total | 40-37 | 51.9 | 1.8 | -3.0 |
| pin_price | early | 1h | 12-28-1 | 30.0 | -0.6 | 44.2 |
| pin_price | early | 1h\|ml | 11-27-1 | 28.9 | -0.7 | 46.6 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 51.7 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.5 | -100.0 |
| follow_move | early | 1h | 115-86-4 | 57.2 | 5.8 | 9.5 |
| follow_move | early | 1h\|ml | 50-43-4 | 53.8 | 0.5 | 3.7 |
| follow_move | early | 1h\|spread | 33-15 | 68.8 | 19.0 | 31.9 |
| follow_move | early | 1h\|total | 32-28 | 53.3 | 3.4 | 1.0 |
| follow_move | early | 2h | 59-63 | 48.4 | -1.2 | -6.6 |
| follow_move | early | 2h OT game | 1-1 | 50.0 | -2.2 | -3.7 |
| follow_move | early | 2h no OT | 58-62 | 48.3 | -1.1 | -6.6 |
| follow_move | early | 2h\|spread | 18-16 | 52.9 | 3.5 | 1.8 |
| follow_move | early | 2h\|tt_away | 18-25 | 41.9 | -7.5 | -18.9 |
| follow_move | early | 2h\|tt_home | 23-22 | 51.1 | 1.3 | -1.1 |
| fd_juice | early | 1h | 2-3 | 40.0 | -9.9 | -26.4 |
| fd_juice | early | 1h\|spread | 1-2 | 33.3 | -16.1 | -38.4 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.5 | -8.4 |
| fd_juice | early | 2h | 18-44 | 29.0 | -20.6 | -47.4 |
| fd_juice | early | 2h no OT | 18-44 | 29.0 | -20.6 | -47.4 |
| fd_juice | early | 2h\|spread | 0-3 | 0.0 | -50.6 | -100.0 |
| fd_juice | early | 2h\|tt_away | 11-21 | 34.4 | -15.0 | -38.1 |
| fd_juice | early | 2h\|tt_home | 7-20 | 25.9 | -23.9 | -52.5 |
| follow_move+pin_value | early | 1h | 3-3 | 50.0 | -0.2 | -4.9 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 70.3 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 70.3 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 16.1 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-2 | 33.3 | -16.5 | -37.2 |
