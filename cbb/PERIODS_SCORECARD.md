# CBB period scorecard — halves and half team totals

Generated 2026-11-19 11:57 UTC. 1450 graded period markets (126 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 331 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 48.5% (n=423)
- **total**: default side won 50.7% (n=290)
- **ml**: default side won 70.6% (n=255)
- **tt_home**: default side won 52.4% (n=231)
- **tt_away**: default side won 52.3% (n=243)
- **2h_tt_ot**: default side won 93.8% (n=16)
- **2h_tt_no_ot**: default side won 50.9% (n=458)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 2-3 | 40.0 | 49.4 | -9.4 | -1.16 | -23.1 | -0.2 | keep collecting (5/50) |
| pin_price | 1-1-1 | 50.0 | 40.9 | 9.1 | -0.02 | -0.7 | -0.17 | keep collecting (2/50) |
| follow_move | 37-31-1 | 54.4 | 48.6 | 5.8 | +14.54 | 21.1 | 0.08 | no edge shown yet |
| fd_juice | 3-17 | 15.0 | 48.6 | -33.6 | -14.62 | -73.1 | 0.5 | keep collecting (20/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 27-37 | 42.2 | 49.7 | -7.5 | -13.61 | -21.3 |  | DROP: below break-even |
| pin_price | 8-7-1 | 53.3 | 35.4 | 18.0 | +29.91 | 186.9 |  | keep collecting (15/50) |
| follow_move | 126-135-1 | 48.3 | 48.0 | 0.2 | +11.48 | 4.4 |  | no edge shown yet |
| fd_juice | 17-24 | 41.5 | 50.7 | -9.3 | -9.8 | -23.9 |  | keep collecting (41/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 48.5 | -48.5 | -1.0 | -100.0 |  | keep collecting (1/50) |
| follow_move+pin_price | 5-3 | 62.5 | 33.3 | 29.2 | +27.58 | 344.8 |  | keep collecting (8/50) |
| follow_move+pin_value | 8-6 | 57.1 | 49.8 | 7.3 | +0.87 | 6.2 |  | keep collecting (14/50) |

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
| pin_value | 71-64 | 52.6 | 49.9 | 2.7 | -2.3 | -1.7 | 0.2 | no edge shown yet |
| pin_price | 11-28-1 | 28.2 | 30.4 | -2.2 | +17.14 | 42.9 | 0.53 | keep collecting (39/50) |
| follow_move | 172-147-4 | 53.9 | 50.7 | 3.2 | +12.48 | 3.9 | -0.02 | no edge shown yet |
| fd_juice | 20-46 | 30.3 | 49.7 | -19.4 | -29.69 | -45.0 | 0.26 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-3 | 50.0 | 50.1 | -0.1 | -0.29 | -4.9 | 0.17 | keep collecting (6/50) |
| follow_move+pin_price | 2-0 | 100.0 | 29.4 | 70.6 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 170-146 | 53.8 | 49.9 | 3.9 | +1.56 | 0.5 |  | no edge shown yet |
| pin_price | 22-53-2 | 29.3 | 30.4 | -1.1 | +47.65 | 61.9 |  | DROP: below break-even |
| follow_move | 507-569-7 | 47.1 | 49.0 | -1.9 | -36.54 | -3.4 |  | DROP: below break-even |
| fd_juice | 76-99 | 43.4 | 49.8 | -6.3 | -35.95 | -20.5 |  | DROP: below break-even |
| follow_move+pin_price | 12-14-1 | 46.2 | 29.4 | 16.7 | +55.28 | 204.7 |  | keep collecting (26/50) |
| follow_move+pin_value | 21-19 | 52.5 | 49.9 | 2.6 | -0.62 | -1.5 |  | keep collecting (40/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 48.5 | -48.5 | -1.0 | -100.0 |  | keep collecting (1/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 170-146 | 53.8 | 3.9 | 0.5 |
| pin_value | close | 1h\|spread | 79-75 | 51.3 | 1.7 | -4.3 |
| pin_value | close | 1h\|total | 91-71 | 56.2 | 6.1 | 5.0 |
| pin_price | close | 1h | 22-53-2 | 29.3 | -1.1 | 61.9 |
| pin_price | close | 1h\|ml | 21-50-2 | 29.6 | 0.2 | 68.0 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -15.1 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.3 | -100.0 |
| follow_move | close | 1h | 300-289-7 | 50.9 | 2.5 | 8.9 |
| follow_move | close | 1h\|ml | 108-120-7 | 47.4 | 1.3 | 20.9 |
| follow_move | close | 1h\|spread | 88-68 | 56.4 | 6.2 | 7.9 |
| follow_move | close | 1h\|total | 104-101 | 50.7 | 0.8 | -3.9 |
| follow_move | close | 2h | 207-280 | 42.5 | -7.2 | -18.4 |
| follow_move | close | 2h OT game | 3-7 | 30.0 | -18.7 | -41.5 |
| follow_move | close | 2h no OT | 204-273 | 42.8 | -6.9 | -18.0 |
| follow_move | close | 2h\|spread | 69-82 | 45.7 | -4.4 | -12.1 |
| follow_move | close | 2h\|tt_away | 68-106 | 39.1 | -10.4 | -25.2 |
| follow_move | close | 2h\|tt_home | 70-92 | 43.2 | -6.2 | -17.1 |
| fd_juice | close | 1h | 8-11 | 42.1 | -8.1 | -22.7 |
| fd_juice | close | 1h\|spread | 7-10 | 41.2 | -9.1 | -24.4 |
| fd_juice | close | 1h\|total | 1-1 | 50.0 | 0.7 | -8.4 |
| fd_juice | close | 2h | 68-88 | 43.6 | -6.1 | -20.3 |
| fd_juice | close | 2h OT game | 2-5 | 28.6 | -21.1 | -48.2 |
| fd_juice | close | 2h no OT | 66-83 | 44.3 | -5.4 | -19.0 |
| fd_juice | close | 2h\|spread | 9-9 | 50.0 | -0.2 | -7.7 |
| fd_juice | close | 2h\|tt_away | 33-36 | 47.8 | -2.5 | -12.9 |
| fd_juice | close | 2h\|tt_home | 26-43 | 37.7 | -11.3 | -31.0 |
| follow_move+pin_price | close | 1h | 12-14-1 | 46.2 | 16.7 | 204.7 |
| follow_move+pin_value | close | 1h | 21-19 | 52.5 | 2.6 | -1.5 |
| fd_juice+pin_value | close | 1h | 0-1 | 0.0 | -48.5 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 12-14-1 | 46.2 | 16.7 | 204.7 |
| follow_move+pin_value | close | 1h\|spread | 9-7 | 56.2 | 6.1 | 5.1 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -48.5 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 12-12 | 50.0 | 0.3 | -6.0 |
| pin_value | early | 1h | 71-64 | 52.6 | 2.7 | -1.7 |
| pin_value | early | 1h\|spread | 34-28 | 54.8 | 5.2 | 2.6 |
| pin_value | early | 1h\|total | 37-36 | 50.7 | 0.5 | -5.3 |
| pin_price | early | 1h | 11-28-1 | 28.2 | -2.2 | 42.9 |
| pin_price | early | 1h\|ml | 10-27-1 | 27.0 | -2.4 | 45.2 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 51.5 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.3 | -100.0 |
| follow_move | early | 1h | 114-85-4 | 57.3 | 5.9 | 10.1 |
| follow_move | early | 1h\|ml | 49-43-4 | 53.3 | 0.1 | 3.7 |
| follow_move | early | 1h\|spread | 33-14 | 70.2 | 20.4 | 34.7 |
| follow_move | early | 1h\|total | 32-28 | 53.3 | 3.4 | 1.0 |
| follow_move | early | 2h | 58-62 | 48.3 | -1.2 | -6.6 |
| follow_move | early | 2h no OT | 58-62 | 48.3 | -1.2 | -6.6 |
| follow_move | early | 2h\|spread | 18-16 | 52.9 | 3.5 | 1.8 |
| follow_move | early | 2h\|tt_away | 17-25 | 40.5 | -8.9 | -21.5 |
| follow_move | early | 2h\|tt_home | 23-21 | 52.3 | 2.6 | 1.1 |
| fd_juice | early | 1h | 2-3 | 40.0 | -10.0 | -26.4 |
| fd_juice | early | 1h\|spread | 1-2 | 33.3 | -16.2 | -38.4 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.7 | -8.4 |
| fd_juice | early | 2h | 18-43 | 29.5 | -20.1 | -46.5 |
| fd_juice | early | 2h no OT | 18-43 | 29.5 | -20.1 | -46.5 |
| fd_juice | early | 2h\|spread | 0-3 | 0.0 | -50.5 | -100.0 |
| fd_juice | early | 2h\|tt_away | 11-20 | 35.5 | -14.0 | -36.1 |
| fd_juice | early | 2h\|tt_home | 7-20 | 25.9 | -23.8 | -52.5 |
| follow_move+pin_value | early | 1h | 3-3 | 50.0 | -0.1 | -4.9 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 70.6 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 70.6 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 16.2 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-2 | 33.3 | -16.4 | -37.2 |
