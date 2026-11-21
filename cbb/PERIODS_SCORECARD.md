# CBB period scorecard — halves and half team totals

Generated 2026-11-21 02:38 UTC. 1560 graded period markets (180 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 441 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 47.7% (n=455)
- **total**: default side won 50.8% (n=311)
- **ml**: default side won 69.3% (n=274)
- **tt_home**: default side won 51.2% (n=250)
- **tt_away**: default side won 52.5% (n=261)
- **2h_tt_ot**: default side won 88.9% (n=18)
- **2h_tt_no_ot**: default side won 50.5% (n=493)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 10-10 | 50.0 | 50.4 | -0.4 | -1.28 | -6.4 | 0.0 | keep collecting (20/50) |
| pin_price | 3-3-1 | 50.0 | 38.4 | 11.6 | +0.1 | 1.4 | 0.8 | keep collecting (6/50) |
| follow_move | 46-35-1 | 56.8 | 49.4 | 7.4 | +17.18 | 21.0 | 0.02 | no edge shown yet |
| fd_juice | 3-20 | 13.0 | 49.7 | -36.6 | -17.62 | -76.6 | 0.43 | keep collecting (23/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 41-44 | 48.2 | 49.7 | -1.4 | -8.45 | -9.9 |  | no edge shown yet |
| pin_price | 10-10-1 | 50.0 | 37.8 | 12.2 | +33.15 | 157.9 |  | keep collecting (20/50) |
| follow_move | 167-181-2 | 48.0 | 49.3 | -1.3 | +0.44 | 0.1 |  | DROP: below break-even |
| fd_juice | 21-32 | 39.6 | 51.2 | -11.6 | -14.4 | -27.2 |  | DROP: below break-even |
| fd_juice+pin_value | 0-1 | 0.0 | 45.9 | -45.9 | -1.0 | -100.0 |  | keep collecting (1/50) |
| follow_move+pin_price | 5-4 | 55.6 | 36.8 | 18.7 | +26.58 | 295.3 |  | keep collecting (9/50) |
| follow_move+pin_value | 12-7 | 63.2 | 50.3 | 12.8 | +3.38 | 17.8 |  | keep collecting (19/50) |

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
| pin_value | 79-71 | 52.7 | 49.9 | 2.8 | -2.42 | -1.6 | 0.19 | no edge shown yet |
| pin_price | 13-30-1 | 30.2 | 31.5 | -1.3 | +17.26 | 39.2 | 0.62 | keep collecting (43/50) |
| follow_move | 181-151-4 | 54.5 | 50.7 | 3.9 | +15.12 | 4.5 | -0.03 | no edge shown yet |
| fd_juice | 20-49 | 29.0 | 49.7 | -20.7 | -32.69 | -47.4 | 0.25 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-3 | 50.0 | 50.3 | -0.3 | -0.29 | -4.9 | 0.17 | keep collecting (6/50) |
| follow_move+pin_price | 2-0 | 100.0 | 30.7 | 69.3 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 184-153 | 54.6 | 49.8 | 4.8 | +6.73 | 2.0 |  | no edge shown yet |
| pin_price | 24-56-2 | 30.0 | 31.5 | -1.5 | +50.89 | 62.1 |  | DROP: below break-even |
| follow_move | 548-615-8 | 47.1 | 49.3 | -2.1 | -47.58 | -4.1 |  | DROP: below break-even |
| fd_juice | 80-107 | 42.8 | 50.0 | -7.2 | -40.55 | -21.7 |  | DROP: below break-even |
| follow_move+pin_price | 12-15-1 | 44.4 | 30.7 | 13.8 | +54.28 | 193.9 |  | keep collecting (27/50) |
| follow_move+pin_value | 25-20 | 55.6 | 50.0 | 5.6 | +1.9 | 4.2 |  | keep collecting (45/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 47.7 | -47.7 | -1.0 | -100.0 |  | keep collecting (1/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 184-153 | 54.6 | 4.8 | 2.0 |
| pin_value | close | 1h\|spread | 84-78 | 51.9 | 2.4 | -3.3 |
| pin_value | close | 1h\|total | 100-75 | 57.1 | 7.0 | 6.9 |
| pin_price | close | 1h | 24-56-2 | 30.0 | -1.5 | 62.1 |
| pin_price | close | 1h\|ml | 23-53-2 | 30.3 | -0.4 | 67.8 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -14.4 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.2 | -100.0 |
| follow_move | close | 1h | 322-313-8 | 50.7 | 1.9 | 7.2 |
| follow_move | close | 1h\|ml | 115-130-8 | 46.9 | 0.2 | 16.9 |
| follow_move | close | 1h\|spread | 95-74 | 56.2 | 6.0 | 7.4 |
| follow_move | close | 1h\|total | 112-109 | 50.7 | 0.8 | -4.0 |
| follow_move | close | 2h | 226-302 | 42.8 | -7.0 | -17.8 |
| follow_move | close | 2h OT game | 4-8 | 33.3 | -16.0 | -34.8 |
| follow_move | close | 2h no OT | 222-294 | 43.0 | -6.8 | -17.4 |
| follow_move | close | 2h\|spread | 75-89 | 45.7 | -4.4 | -12.1 |
| follow_move | close | 2h\|tt_away | 77-110 | 41.2 | -8.4 | -21.1 |
| follow_move | close | 2h\|tt_home | 74-103 | 41.8 | -7.9 | -19.7 |
| fd_juice | close | 1h | 8-11 | 42.1 | -8.2 | -22.7 |
| fd_juice | close | 1h\|spread | 7-10 | 41.2 | -9.2 | -24.4 |
| fd_juice | close | 1h\|total | 1-1 | 50.0 | 0.8 | -8.4 |
| fd_juice | close | 2h | 72-96 | 42.9 | -7.1 | -21.6 |
| fd_juice | close | 2h OT game | 2-5 | 28.6 | -21.1 | -48.2 |
| fd_juice | close | 2h no OT | 70-91 | 43.5 | -6.5 | -20.4 |
| fd_juice | close | 2h\|spread | 10-11 | 47.6 | -2.5 | -12.2 |
| fd_juice | close | 2h\|tt_away | 34-40 | 45.9 | -4.5 | -16.2 |
| fd_juice | close | 2h\|tt_home | 28-45 | 38.4 | -11.2 | -29.8 |
| follow_move+pin_price | close | 1h | 12-15-1 | 44.4 | 13.8 | 193.9 |
| follow_move+pin_value | close | 1h | 25-20 | 55.6 | 5.6 | 4.2 |
| fd_juice+pin_value | close | 1h | 0-1 | 0.0 | -47.7 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 12-15-1 | 44.4 | 13.8 | 193.9 |
| follow_move+pin_value | close | 1h\|spread | 10-7 | 58.8 | 8.4 | 9.8 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -47.7 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 15-13 | 53.6 | 3.9 | 0.8 |
| pin_value | early | 1h | 79-71 | 52.7 | 2.8 | -1.6 |
| pin_value | early | 1h\|spread | 37-31 | 54.4 | 4.9 | 1.7 |
| pin_value | early | 1h\|total | 42-40 | 51.2 | 1.0 | -4.3 |
| pin_price | early | 1h | 13-30-1 | 30.2 | -1.3 | 39.2 |
| pin_price | early | 1h\|ml | 12-29-1 | 29.3 | -1.4 | 41.1 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 52.3 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.2 | -100.0 |
| follow_move | early | 1h | 118-87-4 | 57.6 | 6.3 | 9.8 |
| follow_move | early | 1h\|ml | 52-43-4 | 54.7 | 1.7 | 4.6 |
| follow_move | early | 1h\|spread | 34-15 | 69.4 | 19.7 | 33.0 |
| follow_move | early | 1h\|total | 32-29 | 52.5 | 2.6 | -0.7 |
| follow_move | early | 2h | 63-64 | 49.6 | 0.0 | -4.1 |
| follow_move | early | 2h OT game | 1-1 | 50.0 | -1.8 | -3.7 |
| follow_move | early | 2h no OT | 62-63 | 49.6 | 0.0 | -4.1 |
| follow_move | early | 2h\|spread | 19-16 | 54.3 | 5.0 | 4.2 |
| follow_move | early | 2h\|tt_away | 21-25 | 45.7 | -3.9 | -11.4 |
| follow_move | early | 2h\|tt_home | 23-23 | 50.0 | 0.2 | -3.3 |
| fd_juice | early | 1h | 2-3 | 40.0 | -9.9 | -26.4 |
| fd_juice | early | 1h\|spread | 1-2 | 33.3 | -15.9 | -38.4 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.8 | -8.4 |
| fd_juice | early | 2h | 18-46 | 28.1 | -21.6 | -49.0 |
| fd_juice | early | 2h no OT | 18-46 | 28.1 | -21.6 | -49.0 |
| fd_juice | early | 2h\|spread | 0-4 | 0.0 | -51.2 | -100.0 |
| fd_juice | early | 2h\|tt_away | 11-21 | 34.4 | -15.0 | -38.1 |
| fd_juice | early | 2h\|tt_home | 7-21 | 25.0 | -24.9 | -54.2 |
| follow_move+pin_value | early | 1h | 3-3 | 50.0 | -0.3 | -4.9 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 69.3 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 69.3 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 15.9 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-2 | 33.3 | -16.4 | -37.2 |
