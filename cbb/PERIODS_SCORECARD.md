# CBB period scorecard — halves and half team totals

Generated 2026-11-22 01:28 UTC. 1640 graded period markets (186 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 521 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 47.7% (n=478)
- **total**: default side won 50.0% (n=328)
- **ml**: default side won 70.5% (n=288)
- **tt_home**: default side won 51.7% (n=261)
- **tt_away**: default side won 52.0% (n=275)
- **2h_tt_ot**: default side won 90.0% (n=20)
- **2h_tt_no_ot**: default side won 50.4% (n=516)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 12-14 | 46.2 | 50.2 | -4.0 | -3.5 | -13.5 | 0.04 | keep collecting (26/50) |
| pin_price | 3-6-1 | 33.3 | 33.8 | -0.4 | -2.9 | -29.0 | 0.76 | keep collecting (9/50) |
| follow_move | 51-44-2 | 53.7 | 49.2 | 4.5 | +12.24 | 12.6 | -0.05 | no edge shown yet |
| fd_juice | 6-21 | 22.2 | 49.0 | -26.8 | -16.15 | -59.8 | 0.44 | keep collecting (27/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 49-54 | 47.6 | 49.7 | -2.1 | -11.5 | -11.2 |  | no edge shown yet |
| pin_price | 10-15-1 | 40.0 | 33.3 | 6.7 | +28.15 | 108.3 |  | keep collecting (25/50) |
| follow_move | 192-214-3 | 47.3 | 49.2 | -1.9 | -10.68 | -2.6 |  | DROP: below break-even |
| fd_juice | 23-37 | 38.3 | 50.7 | -12.4 | -17.7 | -29.5 |  | DROP: below break-even |
| fd_juice+pin_value | 0-1 | 0.0 | 46.2 | -46.2 | -1.0 | -100.0 |  | keep collecting (1/50) |
| follow_move+pin_price | 5-6 | 45.5 | 32.2 | 13.2 | +24.58 | 223.5 |  | keep collecting (11/50) |
| follow_move+pin_value | 13-7 | 65.0 | 51.5 | 13.5 | +4.2 | 21.0 |  | keep collecting (20/50) |

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
| pin_value | 81-75 | 51.9 | 49.8 | 2.1 | -4.64 | -3.0 | 0.19 | no edge shown yet |
| pin_price | 13-33-1 | 28.3 | 30.4 | -2.1 | +14.26 | 30.3 | 0.62 | keep collecting (46/50) |
| follow_move | 186-160-5 | 53.8 | 50.6 | 3.1 | +10.18 | 2.9 | -0.04 | no edge shown yet |
| fd_juice | 23-50 | 31.5 | 49.7 | -18.2 | -31.22 | -42.8 | 0.26 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-3 | 50.0 | 50.4 | -0.4 | -0.29 | -4.9 | 0.17 | keep collecting (6/50) |
| follow_move+pin_price | 2-0 | 100.0 | 29.5 | 70.5 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 192-163 | 54.1 | 49.8 | 4.3 | +3.67 | 1.0 |  | no edge shown yet |
| pin_price | 24-61-2 | 28.2 | 30.4 | -2.2 | +45.89 | 52.7 |  | DROP: below break-even |
| follow_move | 573-648-9 | 46.9 | 49.2 | -2.3 | -58.7 | -4.8 |  | DROP: below break-even |
| fd_juice | 82-112 | 42.3 | 49.9 | -7.6 | -43.85 | -22.6 |  | DROP: below break-even |
| follow_move+pin_price | 12-17-1 | 41.4 | 29.5 | 11.9 | +52.28 | 174.3 |  | keep collecting (29/50) |
| follow_move+pin_value | 26-20 | 56.5 | 50.2 | 6.4 | +2.72 | 5.9 |  | keep collecting (46/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 47.7 | -47.7 | -1.0 | -100.0 |  | keep collecting (1/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 192-163 | 54.1 | 4.3 | 1.0 |
| pin_value | close | 1h\|spread | 88-84 | 51.2 | 1.7 | -4.5 |
| pin_value | close | 1h\|total | 104-79 | 56.8 | 6.8 | 6.3 |
| pin_price | close | 1h | 24-61-2 | 28.2 | -2.2 | 52.7 |
| pin_price | close | 1h\|ml | 23-58-2 | 28.4 | -1.1 | 57.7 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -14.4 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -50.0 | -100.0 |
| follow_move | close | 1h | 339-327-9 | 50.9 | 2.2 | 6.9 |
| follow_move | close | 1h\|ml | 120-136-9 | 46.9 | 0.4 | 15.2 |
| follow_move | close | 1h\|spread | 98-77 | 56.0 | 5.7 | 7.1 |
| follow_move | close | 1h\|total | 121-114 | 51.5 | 1.5 | -2.5 |
| follow_move | close | 2h | 234-321 | 42.2 | -7.6 | -19.0 |
| follow_move | close | 2h OT game | 4-10 | 28.6 | -20.5 | -44.1 |
| follow_move | close | 2h no OT | 230-311 | 42.5 | -7.3 | -18.4 |
| follow_move | close | 2h\|spread | 77-96 | 44.5 | -5.7 | -14.4 |
| follow_move | close | 2h\|tt_away | 81-116 | 41.1 | -8.5 | -21.1 |
| follow_move | close | 2h\|tt_home | 76-109 | 41.1 | -8.6 | -21.0 |
| fd_juice | close | 1h | 8-11 | 42.1 | -8.3 | -22.7 |
| fd_juice | close | 1h\|spread | 7-10 | 41.2 | -9.2 | -24.4 |
| fd_juice | close | 1h\|total | 1-1 | 50.0 | 0.0 | -8.4 |
| fd_juice | close | 2h | 74-101 | 42.3 | -7.6 | -22.6 |
| fd_juice | close | 2h OT game | 2-6 | 25.0 | -24.5 | -54.6 |
| fd_juice | close | 2h no OT | 72-95 | 43.1 | -6.8 | -21.1 |
| fd_juice | close | 2h\|spread | 10-11 | 47.6 | -2.5 | -12.2 |
| fd_juice | close | 2h\|tt_away | 35-43 | 44.9 | -5.5 | -18.1 |
| fd_juice | close | 2h\|tt_home | 29-47 | 38.2 | -11.1 | -30.1 |
| follow_move+pin_price | close | 1h | 12-17-1 | 41.4 | 11.9 | 174.3 |
| follow_move+pin_value | close | 1h | 26-20 | 56.5 | 6.4 | 5.9 |
| fd_juice+pin_value | close | 1h | 0-1 | 0.0 | -47.7 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 12-17-1 | 41.4 | 11.9 | 174.3 |
| follow_move+pin_value | close | 1h\|spread | 10-7 | 58.8 | 8.4 | 9.8 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -47.7 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 16-13 | 55.2 | 5.2 | 3.6 |
| pin_value | early | 1h | 81-75 | 51.9 | 2.1 | -3.0 |
| pin_value | early | 1h\|spread | 38-33 | 53.5 | 3.9 | 0.1 |
| pin_value | early | 1h\|total | 43-42 | 50.6 | 0.6 | -5.5 |
| pin_price | early | 1h | 13-33-1 | 28.3 | -2.1 | 30.3 |
| pin_price | early | 1h\|ml | 12-32-1 | 27.3 | -2.2 | 31.7 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 52.3 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -50.0 | -100.0 |
| follow_move | early | 1h | 122-94-5 | 56.5 | 5.2 | 7.4 |
| follow_move | early | 1h\|ml | 54-46-5 | 54.0 | 1.1 | 2.7 |
| follow_move | early | 1h\|spread | 34-17 | 66.7 | 16.9 | 27.8 |
| follow_move | early | 1h\|total | 34-31 | 52.3 | 2.3 | -0.9 |
| follow_move | early | 2h | 64-66 | 49.2 | -0.3 | -4.8 |
| follow_move | early | 2h OT game | 1-2 | 33.3 | -17.1 | -35.8 |
| follow_move | early | 2h no OT | 63-64 | 49.6 | 0.1 | -4.1 |
| follow_move | early | 2h\|spread | 19-17 | 52.8 | 3.5 | 1.3 |
| follow_move | early | 2h\|tt_away | 22-25 | 46.8 | -2.8 | -9.0 |
| follow_move | early | 2h\|tt_home | 23-24 | 48.9 | -0.8 | -5.4 |
| fd_juice | early | 1h | 3-3 | 50.0 | 0.8 | -7.9 |
| fd_juice | early | 1h\|spread | 2-2 | 50.0 | 1.2 | -7.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | 0.0 | -8.4 |
| fd_juice | early | 2h | 20-47 | 29.9 | -19.8 | -45.9 |
| fd_juice | early | 2h no OT | 20-47 | 29.9 | -19.8 | -45.9 |
| fd_juice | early | 2h\|spread | 0-4 | 0.0 | -51.2 | -100.0 |
| fd_juice | early | 2h\|tt_away | 12-21 | 36.4 | -13.1 | -34.5 |
| fd_juice | early | 2h\|tt_home | 8-22 | 26.7 | -23.1 | -51.2 |
| follow_move+pin_value | early | 1h | 3-3 | 50.0 | -0.4 | -4.9 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 70.5 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 70.5 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 15.9 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-2 | 33.3 | -16.7 | -37.2 |
