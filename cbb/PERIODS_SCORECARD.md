# CBB period scorecard — halves and half team totals

Generated 2026-11-22 11:45 UTC. 1661 graded period markets (150 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 542 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 47.4% (n=483)
- **total**: default side won 50.5% (n=333)
- **ml**: default side won 70.0% (n=293)
- **tt_home**: default side won 51.5% (n=264)
- **tt_away**: default side won 52.2% (n=278)
- **2h_tt_ot**: default side won 90.0% (n=20)
- **2h_tt_no_ot**: default side won 50.4% (n=522)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 13-19 | 40.6 | 49.9 | -9.2 | -7.64 | -23.9 | 0.03 | keep collecting (32/50) |
| pin_price | 3-8-1 | 27.3 | 34.7 | -7.5 | -4.9 | -40.8 | 0.62 | keep collecting (11/50) |
| follow_move | 54-45-2 | 54.5 | 49.0 | 5.5 | +15.17 | 15.0 | -0.04 | no edge shown yet |
| fd_juice | 6-22 | 21.4 | 49.1 | -27.7 | -17.15 | -61.3 | 0.43 | keep collecting (28/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 51-58 | 46.8 | 49.5 | -2.7 | -13.77 | -12.6 |  | no edge shown yet |
| pin_price | 10-16-1 | 38.5 | 34.6 | 3.9 | +27.15 | 100.6 |  | keep collecting (26/50) |
| follow_move | 198-220-3 | 47.4 | 49.2 | -1.8 | -10.51 | -2.5 |  | DROP: below break-even |
| fd_juice | 26-39 | 40.0 | 50.8 | -10.8 | -17.19 | -26.4 |  | DROP: below break-even |
| fd_juice+pin_value | 0-2 | 0.0 | 47.7 | -47.7 | -2.0 | -100.0 |  | keep collecting (2/50) |
| follow_move+pin_price | 5-6 | 45.5 | 33.7 | 11.8 | +24.58 | 223.5 |  | keep collecting (11/50) |
| follow_move+pin_value | 13-7 | 65.0 | 50.9 | 14.1 | +4.2 | 21.0 |  | keep collecting (20/50) |

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
| pin_value | 82-80 | 50.6 | 49.8 | 0.8 | -8.78 | -5.4 | 0.18 | no edge shown yet |
| pin_price | 13-35-1 | 27.1 | 30.8 | -3.7 | +12.26 | 25.0 | 0.59 | keep collecting (48/50) |
| follow_move | 189-161-5 | 54.0 | 50.5 | 3.5 | +13.11 | 3.7 | -0.04 | no edge shown yet |
| fd_juice | 23-51 | 31.1 | 49.6 | -18.6 | -32.22 | -43.5 | 0.26 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-3 | 50.0 | 50.4 | -0.4 | -0.29 | -4.9 | 0.17 | keep collecting (6/50) |
| follow_move+pin_price | 2-0 | 100.0 | 30.0 | 70.0 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 194-167 | 53.7 | 49.7 | 4.0 | +1.41 | 0.4 |  | no edge shown yet |
| pin_price | 24-62-2 | 27.9 | 30.9 | -3.0 | +44.89 | 51.0 |  | DROP: below break-even |
| follow_move | 579-654-9 | 47.0 | 49.2 | -2.3 | -58.53 | -4.7 |  | DROP: below break-even |
| fd_juice | 85-114 | 42.7 | 50.0 | -7.2 | -43.33 | -21.8 |  | DROP: below break-even |
| follow_move+pin_price | 12-17-1 | 41.4 | 30.0 | 11.3 | +52.28 | 174.3 |  | keep collecting (29/50) |
| follow_move+pin_value | 26-20 | 56.5 | 50.1 | 6.5 | +2.72 | 5.9 |  | keep collecting (46/50) |
| fd_juice+pin_value | 0-2 | 0.0 | 48.5 | -48.5 | -2.0 | -100.0 |  | keep collecting (2/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 194-167 | 53.7 | 4.0 | 0.4 |
| pin_value | close | 1h\|spread | 89-86 | 50.9 | 1.5 | -5.1 |
| pin_value | close | 1h\|total | 105-81 | 56.5 | 6.4 | 5.5 |
| pin_price | close | 1h | 24-62-2 | 27.9 | -3.0 | 51.0 |
| pin_price | close | 1h\|ml | 23-59-2 | 28.0 | -2.0 | 55.8 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -14.1 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.5 | -100.0 |
| follow_move | close | 1h | 344-331-9 | 51.0 | 2.2 | 7.0 |
| follow_move | close | 1h\|ml | 123-138-9 | 47.1 | 0.6 | 15.5 |
| follow_move | close | 1h\|spread | 98-78 | 55.7 | 5.4 | 6.5 |
| follow_move | close | 1h\|total | 123-115 | 51.7 | 1.8 | -2.2 |
| follow_move | close | 2h | 235-323 | 42.1 | -7.7 | -19.1 |
| follow_move | close | 2h OT game | 4-10 | 28.6 | -20.5 | -44.1 |
| follow_move | close | 2h no OT | 231-313 | 42.5 | -7.4 | -18.5 |
| follow_move | close | 2h\|spread | 77-96 | 44.5 | -5.7 | -14.4 |
| follow_move | close | 2h\|tt_away | 81-117 | 40.9 | -8.7 | -21.5 |
| follow_move | close | 2h\|tt_home | 77-110 | 41.2 | -8.5 | -20.8 |
| fd_juice | close | 1h | 9-12 | 42.9 | -7.6 | -21.2 |
| fd_juice | close | 1h\|spread | 8-10 | 44.4 | -6.1 | -18.3 |
| fd_juice | close | 1h\|total | 1-2 | 33.3 | -16.2 | -38.9 |
| fd_juice | close | 2h | 76-102 | 42.7 | -7.2 | -21.8 |
| fd_juice | close | 2h OT game | 2-6 | 25.0 | -24.5 | -54.6 |
| fd_juice | close | 2h no OT | 74-96 | 43.5 | -6.4 | -20.3 |
| fd_juice | close | 2h\|spread | 10-11 | 47.6 | -2.5 | -12.2 |
| fd_juice | close | 2h\|tt_away | 37-43 | 46.2 | -4.1 | -15.5 |
| fd_juice | close | 2h\|tt_home | 29-48 | 37.7 | -11.7 | -31.0 |
| follow_move+pin_price | close | 1h | 12-17-1 | 41.4 | 11.3 | 174.3 |
| follow_move+pin_value | close | 1h | 26-20 | 56.5 | 6.5 | 5.9 |
| fd_juice+pin_value | close | 1h | 0-2 | 0.0 | -48.5 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 12-17-1 | 41.4 | 11.3 | 174.3 |
| follow_move+pin_value | close | 1h\|spread | 10-7 | 58.8 | 8.4 | 9.8 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -47.4 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 16-13 | 55.2 | 5.3 | 3.6 |
| fd_juice+pin_value | close | 1h\|total | 0-1 | 0.0 | -49.5 | -100.0 |
| pin_value | early | 1h | 82-80 | 50.6 | 0.8 | -5.4 |
| pin_value | early | 1h\|spread | 39-35 | 52.7 | 3.3 | -1.5 |
| pin_value | early | 1h\|total | 43-45 | 48.9 | -1.2 | -8.7 |
| pin_price | early | 1h | 13-35-1 | 27.1 | -3.7 | 25.0 |
| pin_price | early | 1h\|ml | 12-34-1 | 26.1 | -3.9 | 26.1 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 52.6 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.5 | -100.0 |
| follow_move | early | 1h | 124-95-5 | 56.6 | 5.5 | 8.2 |
| follow_move | early | 1h\|ml | 55-46-5 | 54.5 | 1.9 | 4.6 |
| follow_move | early | 1h\|spread | 34-17 | 66.7 | 16.9 | 27.8 |
| follow_move | early | 1h\|total | 35-32 | 52.2 | 2.3 | -1.0 |
| follow_move | early | 2h | 65-66 | 49.6 | 0.1 | -4.0 |
| follow_move | early | 2h OT game | 1-2 | 33.3 | -17.0 | -35.8 |
| follow_move | early | 2h no OT | 64-64 | 50.0 | 0.5 | -3.3 |
| follow_move | early | 2h\|spread | 19-17 | 52.8 | 3.6 | 1.3 |
| follow_move | early | 2h\|tt_away | 22-25 | 46.8 | -2.8 | -9.0 |
| follow_move | early | 2h\|tt_home | 24-24 | 50.0 | 0.3 | -3.2 |
| fd_juice | early | 1h | 3-3 | 50.0 | 0.7 | -7.9 |
| fd_juice | early | 1h\|spread | 2-2 | 50.0 | 1.3 | -7.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.5 | -8.4 |
| fd_juice | early | 2h | 20-48 | 29.4 | -20.3 | -46.7 |
| fd_juice | early | 2h no OT | 20-48 | 29.4 | -20.3 | -46.7 |
| fd_juice | early | 2h\|spread | 0-4 | 0.0 | -51.3 | -100.0 |
| fd_juice | early | 2h\|tt_away | 12-21 | 36.4 | -13.0 | -34.5 |
| fd_juice | early | 2h\|tt_home | 8-23 | 25.8 | -23.9 | -52.8 |
| follow_move+pin_value | early | 1h | 3-3 | 50.0 | -0.4 | -4.9 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 70.0 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 70.0 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 15.8 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-2 | 33.3 | -16.5 | -37.2 |
