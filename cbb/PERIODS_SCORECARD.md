# CBB period scorecard — halves and half team totals

Generated 2026-11-21 19:36 UTC. 1590 graded period markets (192 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 471 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 47.4% (n=466)
- **total**: default side won 50.5% (n=317)
- **ml**: default side won 69.6% (n=280)
- **tt_home**: default side won 51.4% (n=253)
- **tt_away**: default side won 52.1% (n=265)
- **2h_tt_ot**: default side won 88.9% (n=18)
- **2h_tt_no_ot**: default side won 50.4% (n=500)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 12-14 | 46.2 | 50.4 | -4.2 | -3.5 | -13.5 | 0.04 | keep collecting (26/50) |
| pin_price | 3-6-1 | 33.3 | 36.5 | -3.1 | -2.9 | -29.0 | 0.76 | keep collecting (9/50) |
| follow_move | 46-37-1 | 55.4 | 49.3 | 6.2 | +15.18 | 18.1 | 0.02 | no edge shown yet |
| fd_juice | 3-20 | 13.0 | 49.7 | -36.6 | -17.62 | -76.6 | 0.43 | keep collecting (23/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 46-48 | 48.9 | 49.7 | -0.8 | -8.24 | -8.8 |  | no edge shown yet |
| pin_price | 10-14-1 | 41.7 | 36.2 | 5.5 | +29.15 | 116.6 |  | keep collecting (24/50) |
| follow_move | 173-196-2 | 46.9 | 49.2 | -2.4 | -8.62 | -2.3 |  | DROP: below break-even |
| fd_juice | 21-33 | 38.9 | 51.0 | -12.1 | -15.4 | -28.5 |  | DROP: below break-even |
| fd_juice+pin_value | 0-1 | 0.0 | 45.2 | -45.2 | -1.0 | -100.0 |  | keep collecting (1/50) |
| follow_move+pin_price | 5-6 | 45.5 | 35.4 | 10.1 | +24.58 | 223.5 |  | keep collecting (11/50) |
| follow_move+pin_value | 13-7 | 65.0 | 51.0 | 14.0 | +4.2 | 21.0 |  | keep collecting (20/50) |

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
| pin_value | 81-75 | 51.9 | 49.9 | 2.1 | -4.64 | -3.0 | 0.19 | no edge shown yet |
| pin_price | 13-33-1 | 28.3 | 31.1 | -2.9 | +14.26 | 30.3 | 0.62 | keep collecting (46/50) |
| follow_move | 181-153-4 | 54.2 | 50.6 | 3.6 | +13.12 | 3.9 | -0.03 | no edge shown yet |
| fd_juice | 20-49 | 29.0 | 49.8 | -20.8 | -32.69 | -47.4 | 0.25 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-3 | 50.0 | 50.4 | -0.4 | -0.29 | -4.9 | 0.17 | keep collecting (6/50) |
| follow_move+pin_price | 2-0 | 100.0 | 30.4 | 69.6 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 189-157 | 54.6 | 49.8 | 4.9 | +6.93 | 2.0 |  | no edge shown yet |
| pin_price | 24-60-2 | 28.6 | 31.2 | -2.6 | +46.89 | 54.5 |  | DROP: below break-even |
| follow_move | 554-630-8 | 46.8 | 49.2 | -2.4 | -56.64 | -4.8 |  | DROP: below break-even |
| fd_juice | 80-108 | 42.6 | 50.0 | -7.4 | -41.55 | -22.1 |  | DROP: below break-even |
| follow_move+pin_price | 12-17-1 | 41.4 | 30.4 | 11.0 | +52.28 | 174.3 |  | keep collecting (29/50) |
| follow_move+pin_value | 26-20 | 56.5 | 50.1 | 6.5 | +2.72 | 5.9 |  | keep collecting (46/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 47.4 | -47.4 | -1.0 | -100.0 |  | keep collecting (1/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 189-157 | 54.6 | 4.9 | 2.0 |
| pin_value | close | 1h\|spread | 86-81 | 51.5 | 2.0 | -4.0 |
| pin_value | close | 1h\|total | 103-76 | 57.5 | 7.5 | 7.6 |
| pin_price | close | 1h | 24-60-2 | 28.6 | -2.6 | 54.5 |
| pin_price | close | 1h\|ml | 23-57-2 | 28.7 | -1.6 | 59.6 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -14.1 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.5 | -100.0 |
| follow_move | close | 1h | 326-319-8 | 50.5 | 1.9 | 6.8 |
| follow_move | close | 1h\|ml | 116-133-8 | 46.6 | 0.1 | 16.0 |
| follow_move | close | 1h\|spread | 96-75 | 56.1 | 5.8 | 7.3 |
| follow_move | close | 1h\|total | 114-111 | 50.7 | 0.7 | -4.1 |
| follow_move | close | 2h | 228-311 | 42.3 | -7.5 | -18.8 |
| follow_move | close | 2h OT game | 4-8 | 33.3 | -16.0 | -34.8 |
| follow_move | close | 2h no OT | 224-303 | 42.5 | -7.3 | -18.4 |
| follow_move | close | 2h\|spread | 75-94 | 44.4 | -5.8 | -14.7 |
| follow_move | close | 2h\|tt_away | 78-112 | 41.1 | -8.6 | -21.3 |
| follow_move | close | 2h\|tt_home | 75-105 | 41.7 | -8.1 | -19.9 |
| fd_juice | close | 1h | 8-11 | 42.1 | -8.3 | -22.7 |
| fd_juice | close | 1h\|spread | 7-10 | 41.2 | -9.3 | -24.4 |
| fd_juice | close | 1h\|total | 1-1 | 50.0 | 0.5 | -8.4 |
| fd_juice | close | 2h | 72-97 | 42.6 | -7.3 | -22.0 |
| fd_juice | close | 2h OT game | 2-5 | 28.6 | -21.1 | -48.2 |
| fd_juice | close | 2h no OT | 70-92 | 43.2 | -6.7 | -20.9 |
| fd_juice | close | 2h\|spread | 10-11 | 47.6 | -2.5 | -12.2 |
| fd_juice | close | 2h\|tt_away | 34-41 | 45.3 | -5.0 | -17.3 |
| fd_juice | close | 2h\|tt_home | 28-45 | 38.4 | -11.1 | -29.8 |
| follow_move+pin_price | close | 1h | 12-17-1 | 41.4 | 11.0 | 174.3 |
| follow_move+pin_value | close | 1h | 26-20 | 56.5 | 6.5 | 5.9 |
| fd_juice+pin_value | close | 1h | 0-1 | 0.0 | -47.4 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 12-17-1 | 41.4 | 11.0 | 174.3 |
| follow_move+pin_value | close | 1h\|spread | 10-7 | 58.8 | 8.4 | 9.8 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -47.4 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 16-13 | 55.2 | 5.4 | 3.6 |
| pin_value | early | 1h | 81-75 | 51.9 | 2.1 | -3.0 |
| pin_value | early | 1h\|spread | 38-33 | 53.5 | 4.0 | 0.1 |
| pin_value | early | 1h\|total | 43-42 | 50.6 | 0.5 | -5.5 |
| pin_price | early | 1h | 13-33-1 | 28.3 | -2.9 | 30.3 |
| pin_price | early | 1h\|ml | 12-32-1 | 27.3 | -3.1 | 31.7 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 52.6 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.5 | -100.0 |
| follow_move | early | 1h | 118-89-4 | 57.0 | 5.8 | 8.7 |
| follow_move | early | 1h\|ml | 52-44-4 | 54.2 | 1.3 | 3.6 |
| follow_move | early | 1h\|spread | 34-16 | 68.0 | 18.3 | 30.4 |
| follow_move | early | 1h\|total | 32-29 | 52.5 | 2.5 | -0.7 |
| follow_move | early | 2h | 63-64 | 49.6 | 0.0 | -4.1 |
| follow_move | early | 2h OT game | 1-1 | 50.0 | -1.7 | -3.7 |
| follow_move | early | 2h no OT | 62-63 | 49.6 | 0.1 | -4.1 |
| follow_move | early | 2h\|spread | 19-16 | 54.3 | 5.1 | 4.2 |
| follow_move | early | 2h\|tt_away | 21-25 | 45.7 | -4.0 | -11.4 |
| follow_move | early | 2h\|tt_home | 23-23 | 50.0 | 0.2 | -3.3 |
| fd_juice | early | 1h | 2-3 | 40.0 | -9.7 | -26.4 |
| fd_juice | early | 1h\|spread | 1-2 | 33.3 | -15.8 | -38.4 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.5 | -8.4 |
| fd_juice | early | 2h | 18-46 | 28.1 | -21.7 | -49.0 |
| fd_juice | early | 2h no OT | 18-46 | 28.1 | -21.7 | -49.0 |
| fd_juice | early | 2h\|spread | 0-4 | 0.0 | -51.3 | -100.0 |
| fd_juice | early | 2h\|tt_away | 11-21 | 34.4 | -15.1 | -38.1 |
| fd_juice | early | 2h\|tt_home | 7-21 | 25.0 | -24.9 | -54.2 |
| follow_move+pin_value | early | 1h | 3-3 | 50.0 | -0.4 | -4.9 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 69.6 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 69.6 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 15.8 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-2 | 33.3 | -16.5 | -37.2 |
