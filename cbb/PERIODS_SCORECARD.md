# CBB period scorecard — halves and half team totals

Generated 2026-11-23 01:53 UTC. 1696 graded period markets (192 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 577 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 47.4% (n=494)
- **total**: default side won 50.7% (n=339)
- **ml**: default side won 68.9% (n=299)
- **tt_home**: default side won 51.1% (n=272)
- **tt_away**: default side won 52.7% (n=281)
- **2h_tt_ot**: default side won 90.0% (n=20)
- **2h_tt_no_ot**: default side won 50.5% (n=533)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 17-19 | 47.2 | 49.7 | -2.5 | -4.16 | -11.6 | 0.03 | keep collecting (36/50) |
| pin_price | 3-8-1 | 27.3 | 37.4 | -10.2 | -4.9 | -40.8 | 0.62 | keep collecting (11/50) |
| follow_move | 59-46-2 | 56.2 | 49.3 | 6.9 | +20.25 | 18.9 | -0.06 | no edge shown yet |
| fd_juice | 7-23 | 23.3 | 49.3 | -26.0 | -17.27 | -57.6 | 0.43 | keep collecting (30/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 56-59 | 48.7 | 49.5 | -0.8 | -10.39 | -9.0 |  | no edge shown yet |
| pin_price | 10-16-1 | 38.5 | 37.3 | 1.2 | +27.15 | 100.6 |  | keep collecting (26/50) |
| follow_move | 211-234-4 | 47.4 | 49.2 | -1.8 | -8.9 | -2.0 |  | DROP: below break-even |
| fd_juice | 28-41 | 40.6 | 51.1 | -10.5 | -17.56 | -25.4 |  | DROP: below break-even |
| fd_juice+pin_value | 0-2 | 0.0 | 47.3 | -47.3 | -2.0 | -100.0 |  | keep collecting (2/50) |
| follow_move+pin_price | 5-6 | 45.5 | 36.6 | 8.8 | +24.58 | 223.5 |  | keep collecting (11/50) |
| follow_move+pin_value | 14-7 | 66.7 | 50.4 | 16.2 | +5.08 | 24.2 |  | keep collecting (21/50) |

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
| pin_value | 86-80 | 51.8 | 49.8 | 2.0 | -5.3 | -3.2 | 0.17 | no edge shown yet |
| pin_price | 13-35-1 | 27.1 | 31.8 | -4.7 | +12.26 | 25.0 | 0.59 | keep collecting (48/50) |
| follow_move | 194-162-5 | 54.5 | 50.5 | 4.0 | +18.2 | 5.0 | -0.05 | no edge shown yet |
| fd_juice | 24-52 | 31.6 | 49.6 | -18.0 | -32.33 | -42.5 | 0.26 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-3 | 50.0 | 50.3 | -0.3 | -0.29 | -4.9 | 0.17 | keep collecting (6/50) |
| follow_move+pin_price | 2-0 | 100.0 | 31.1 | 68.9 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 199-168 | 54.2 | 49.7 | 4.5 | +4.79 | 1.3 |  | no edge shown yet |
| pin_price | 24-62-2 | 27.9 | 31.9 | -4.0 | +44.89 | 51.0 |  | DROP: below break-even |
| follow_move | 592-668-10 | 47.0 | 49.2 | -2.2 | -56.92 | -4.5 |  | DROP: below break-even |
| fd_juice | 87-116 | 42.9 | 50.0 | -7.2 | -43.71 | -21.5 |  | DROP: below break-even |
| follow_move+pin_price | 12-17-1 | 41.4 | 31.1 | 10.3 | +52.28 | 174.3 |  | keep collecting (29/50) |
| follow_move+pin_value | 27-20 | 57.4 | 50.0 | 7.5 | +3.6 | 7.7 |  | keep collecting (47/50) |
| fd_juice+pin_value | 0-2 | 0.0 | 48.3 | -48.3 | -2.0 | -100.0 |  | keep collecting (2/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 199-168 | 54.2 | 4.5 | 1.3 |
| pin_value | close | 1h\|spread | 91-87 | 51.1 | 1.7 | -4.6 |
| pin_value | close | 1h\|total | 108-81 | 57.1 | 7.1 | 6.9 |
| pin_price | close | 1h | 24-62-2 | 27.9 | -4.0 | 51.0 |
| pin_price | close | 1h\|ml | 23-59-2 | 28.0 | -3.1 | 55.8 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -14.0 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.3 | -100.0 |
| follow_move | close | 1h | 353-338-10 | 51.1 | 2.3 | 7.5 |
| follow_move | close | 1h\|ml | 128-139-10 | 47.9 | 1.3 | 17.7 |
| follow_move | close | 1h\|spread | 101-80 | 55.8 | 5.5 | 6.8 |
| follow_move | close | 1h\|total | 124-119 | 51.0 | 1.2 | -3.4 |
| follow_move | close | 2h | 239-330 | 42.0 | -7.8 | -19.3 |
| follow_move | close | 2h OT game | 4-10 | 28.6 | -20.4 | -44.1 |
| follow_move | close | 2h no OT | 235-320 | 42.3 | -7.5 | -18.7 |
| follow_move | close | 2h\|spread | 78-99 | 44.1 | -6.1 | -15.3 |
| follow_move | close | 2h\|tt_away | 82-117 | 41.2 | -8.3 | -20.9 |
| follow_move | close | 2h\|tt_home | 79-114 | 40.9 | -8.9 | -21.3 |
| fd_juice | close | 1h | 9-12 | 42.9 | -7.5 | -21.2 |
| fd_juice | close | 1h\|spread | 8-10 | 44.4 | -6.1 | -18.3 |
| fd_juice | close | 1h\|total | 1-2 | 33.3 | -15.9 | -38.9 |
| fd_juice | close | 2h | 78-104 | 42.9 | -7.2 | -21.6 |
| fd_juice | close | 2h OT game | 2-6 | 25.0 | -24.3 | -54.6 |
| fd_juice | close | 2h no OT | 76-98 | 43.7 | -6.4 | -20.0 |
| fd_juice | close | 2h\|spread | 10-11 | 47.6 | -2.5 | -12.2 |
| fd_juice | close | 2h\|tt_away | 38-44 | 46.3 | -4.1 | -15.4 |
| fd_juice | close | 2h\|tt_home | 30-49 | 38.0 | -11.5 | -30.4 |
| follow_move+pin_price | close | 1h | 12-17-1 | 41.4 | 10.3 | 174.3 |
| follow_move+pin_value | close | 1h | 27-20 | 57.4 | 7.5 | 7.7 |
| fd_juice+pin_value | close | 1h | 0-2 | 0.0 | -48.3 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 12-17-1 | 41.4 | 10.3 | 174.3 |
| follow_move+pin_value | close | 1h\|spread | 10-7 | 58.8 | 8.4 | 9.8 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -47.4 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 17-13 | 56.7 | 7.0 | 6.4 |
| fd_juice+pin_value | close | 1h\|total | 0-1 | 0.0 | -49.3 | -100.0 |
| pin_value | early | 1h | 86-80 | 51.8 | 2.0 | -3.2 |
| pin_value | early | 1h\|spread | 40-35 | 53.3 | 3.9 | -0.4 |
| pin_value | early | 1h\|total | 46-45 | 50.5 | 0.4 | -5.5 |
| pin_price | early | 1h | 13-35-1 | 27.1 | -4.7 | 25.0 |
| pin_price | early | 1h\|ml | 12-34-1 | 26.1 | -5.0 | 26.1 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 52.6 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.3 | -100.0 |
| follow_move | early | 1h | 128-95-5 | 57.4 | 6.4 | 10.3 |
| follow_move | early | 1h\|ml | 57-46-5 | 55.3 | 3.0 | 7.6 |
| follow_move | early | 1h\|spread | 36-17 | 67.9 | 18.2 | 30.3 |
| follow_move | early | 1h\|total | 35-32 | 52.2 | 2.4 | -1.0 |
| follow_move | early | 2h | 66-67 | 49.6 | 0.1 | -4.1 |
| follow_move | early | 2h OT game | 1-2 | 33.3 | -17.0 | -35.8 |
| follow_move | early | 2h no OT | 65-65 | 50.0 | 0.5 | -3.3 |
| follow_move | early | 2h\|spread | 19-17 | 52.8 | 3.7 | 1.3 |
| follow_move | early | 2h\|tt_away | 23-25 | 47.9 | -1.6 | -7.0 |
| follow_move | early | 2h\|tt_home | 24-25 | 49.0 | -0.9 | -5.2 |
| fd_juice | early | 1h | 3-3 | 50.0 | 0.6 | -7.9 |
| fd_juice | early | 1h\|spread | 2-2 | 50.0 | 1.3 | -7.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.7 | -8.4 |
| fd_juice | early | 2h | 21-49 | 30.0 | -19.6 | -45.5 |
| fd_juice | early | 2h no OT | 21-49 | 30.0 | -19.6 | -45.5 |
| fd_juice | early | 2h\|spread | 0-4 | 0.0 | -51.3 | -100.0 |
| fd_juice | early | 2h\|tt_away | 12-21 | 36.4 | -12.9 | -34.5 |
| fd_juice | early | 2h\|tt_home | 9-24 | 27.3 | -22.5 | -49.9 |
| follow_move+pin_value | early | 1h | 3-3 | 50.0 | -0.3 | -4.9 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 68.9 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 68.9 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 15.8 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-2 | 33.3 | -16.4 | -37.2 |
