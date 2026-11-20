# CBB period scorecard — halves and half team totals

Generated 2026-11-20 11:58 UTC. 1493 graded period markets (126 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 374 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 48.3% (n=435)
- **total**: default side won 50.7% (n=298)
- **ml**: default side won 70.2% (n=262)
- **tt_home**: default side won 51.7% (n=240)
- **tt_away**: default side won 52.8% (n=250)
- **2h_tt_ot**: default side won 88.9% (n=18)
- **2h_tt_no_ot**: default side won 50.8% (n=472)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 7-4 | 63.6 | 49.8 | 13.8 | +2.12 | 19.3 | 0.18 | keep collecting (11/50) |
| pin_price | 2-1-1 | 66.7 | 38.9 | 27.8 | +0.98 | 24.5 | 0.12 | keep collecting (3/50) |
| follow_move | 38-32-1 | 54.3 | 48.7 | 5.6 | +14.46 | 20.4 | 0.08 | no edge shown yet |
| fd_juice | 3-18 | 14.3 | 48.9 | -34.6 | -15.62 | -74.4 | 0.43 | keep collecting (21/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 33-39 | 45.8 | 49.7 | -3.9 | -10.5 | -14.6 |  | no edge shown yet |
| pin_price | 9-7-1 | 56.2 | 36.1 | 20.2 | +34.81 | 204.8 |  | keep collecting (16/50) |
| follow_move | 144-152-1 | 48.6 | 48.5 | 0.1 | +10.5 | 3.5 |  | no edge shown yet |
| fd_juice | 18-27 | 40.0 | 51.2 | -11.2 | -11.97 | -26.6 |  | keep collecting (45/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 47.8 | -47.8 | -1.0 | -100.0 |  | keep collecting (1/50) |
| follow_move+pin_price | 5-3 | 62.5 | 34.4 | 28.1 | +27.58 | 344.8 |  | keep collecting (8/50) |
| follow_move+pin_value | 10-7 | 58.8 | 50.1 | 8.8 | +1.59 | 9.4 |  | keep collecting (17/50) |

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
| pin_price | 12-28-1 | 30.0 | 30.7 | -0.7 | +18.14 | 44.2 | 0.54 | keep collecting (40/50) |
| follow_move | 173-148-4 | 53.9 | 50.7 | 3.2 | +12.41 | 3.8 | -0.02 | no edge shown yet |
| fd_juice | 20-47 | 29.9 | 49.6 | -19.8 | -30.69 | -45.8 | 0.24 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-3 | 50.0 | 50.2 | -0.2 | -0.29 | -4.9 | 0.17 | keep collecting (6/50) |
| follow_move+pin_price | 2-0 | 100.0 | 29.8 | 70.2 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 176-148 | 54.3 | 49.8 | 4.5 | +4.68 | 1.4 |  | no edge shown yet |
| pin_price | 23-53-2 | 30.3 | 30.8 | -0.5 | +52.55 | 67.4 |  | DROP: below break-even |
| follow_move | 525-586-7 | 47.3 | 49.1 | -1.8 | -37.52 | -3.4 |  | DROP: below break-even |
| fd_juice | 77-102 | 43.0 | 49.9 | -6.9 | -38.12 | -21.3 |  | DROP: below break-even |
| follow_move+pin_price | 12-14-1 | 46.2 | 29.8 | 16.4 | +55.28 | 204.7 |  | keep collecting (26/50) |
| follow_move+pin_value | 23-20 | 53.5 | 49.9 | 3.5 | +0.11 | 0.2 |  | keep collecting (43/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 48.3 | -48.3 | -1.0 | -100.0 |  | keep collecting (1/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 176-148 | 54.3 | 4.5 | 1.4 |
| pin_value | close | 1h\|spread | 81-76 | 51.6 | 2.0 | -3.8 |
| pin_value | close | 1h\|total | 95-72 | 56.9 | 6.8 | 6.3 |
| pin_price | close | 1h | 23-53-2 | 30.3 | -0.5 | 67.4 |
| pin_price | close | 1h\|ml | 22-50-2 | 30.6 | 0.8 | 73.7 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -14.9 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.3 | -100.0 |
| follow_move | close | 1h | 309-296-7 | 51.1 | 2.5 | 8.8 |
| follow_move | close | 1h\|ml | 111-123-7 | 47.4 | 1.2 | 20.1 |
| follow_move | close | 1h\|spread | 90-69 | 56.6 | 6.4 | 8.2 |
| follow_move | close | 1h\|total | 108-104 | 50.9 | 1.0 | -3.6 |
| follow_move | close | 2h | 216-290 | 42.7 | -7.0 | -18.1 |
| follow_move | close | 2h OT game | 4-8 | 33.3 | -15.9 | -34.8 |
| follow_move | close | 2h no OT | 212-282 | 42.9 | -6.8 | -17.7 |
| follow_move | close | 2h\|spread | 71-86 | 45.2 | -4.9 | -13.1 |
| follow_move | close | 2h\|tt_away | 72-107 | 40.2 | -9.2 | -23.0 |
| follow_move | close | 2h\|tt_home | 73-97 | 42.9 | -6.7 | -17.6 |
| fd_juice | close | 1h | 8-11 | 42.1 | -8.1 | -22.7 |
| fd_juice | close | 1h\|spread | 7-10 | 41.2 | -9.1 | -24.4 |
| fd_juice | close | 1h\|total | 1-1 | 50.0 | 0.7 | -8.4 |
| fd_juice | close | 2h | 69-91 | 43.1 | -6.8 | -21.1 |
| fd_juice | close | 2h OT game | 2-5 | 28.6 | -21.0 | -48.2 |
| fd_juice | close | 2h no OT | 67-86 | 43.8 | -6.1 | -19.9 |
| fd_juice | close | 2h\|spread | 10-9 | 52.6 | 2.4 | -2.9 |
| fd_juice | close | 2h\|tt_away | 33-38 | 46.5 | -3.9 | -15.3 |
| fd_juice | close | 2h\|tt_home | 26-44 | 37.1 | -12.2 | -32.0 |
| follow_move+pin_price | close | 1h | 12-14-1 | 46.2 | 16.4 | 204.7 |
| follow_move+pin_value | close | 1h | 23-20 | 53.5 | 3.5 | 0.2 |
| fd_juice+pin_value | close | 1h | 0-1 | 0.0 | -48.3 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 12-14-1 | 46.2 | 16.4 | 204.7 |
| follow_move+pin_value | close | 1h\|spread | 9-7 | 56.2 | 6.0 | 5.1 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -48.3 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 14-13 | 51.9 | 2.1 | -2.6 |
| pin_value | early | 1h | 76-65 | 53.9 | 4.0 | 0.7 |
| pin_value | early | 1h\|spread | 36-28 | 56.2 | 6.7 | 5.2 |
| pin_value | early | 1h\|total | 40-37 | 51.9 | 1.8 | -3.0 |
| pin_price | early | 1h | 12-28-1 | 30.0 | -0.7 | 44.2 |
| pin_price | early | 1h\|ml | 11-27-1 | 28.9 | -0.8 | 46.6 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 51.7 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.3 | -100.0 |
| follow_move | early | 1h | 114-85-4 | 57.3 | 5.9 | 10.1 |
| follow_move | early | 1h\|ml | 49-43-4 | 53.3 | 0.2 | 3.7 |
| follow_move | early | 1h\|spread | 33-14 | 70.2 | 20.4 | 34.7 |
| follow_move | early | 1h\|total | 32-28 | 53.3 | 3.4 | 1.0 |
| follow_move | early | 2h | 59-63 | 48.4 | -1.1 | -6.6 |
| follow_move | early | 2h OT game | 1-1 | 50.0 | -2.2 | -3.7 |
| follow_move | early | 2h no OT | 58-62 | 48.3 | -1.1 | -6.6 |
| follow_move | early | 2h\|spread | 18-16 | 52.9 | 3.5 | 1.8 |
| follow_move | early | 2h\|tt_away | 18-25 | 41.9 | -7.4 | -18.9 |
| follow_move | early | 2h\|tt_home | 23-22 | 51.1 | 1.3 | -1.1 |
| fd_juice | early | 1h | 2-3 | 40.0 | -9.9 | -26.4 |
| fd_juice | early | 1h\|spread | 1-2 | 33.3 | -16.1 | -38.4 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.7 | -8.4 |
| fd_juice | early | 2h | 18-44 | 29.0 | -20.6 | -47.4 |
| fd_juice | early | 2h no OT | 18-44 | 29.0 | -20.6 | -47.4 |
| fd_juice | early | 2h\|spread | 0-3 | 0.0 | -50.6 | -100.0 |
| fd_juice | early | 2h\|tt_away | 11-21 | 34.4 | -14.9 | -38.1 |
| fd_juice | early | 2h\|tt_home | 7-20 | 25.9 | -23.9 | -52.5 |
| follow_move+pin_value | early | 1h | 3-3 | 50.0 | -0.2 | -4.9 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 70.2 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 70.2 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 16.1 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-2 | 33.3 | -16.4 | -37.2 |
