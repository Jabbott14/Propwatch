# CBB period scorecard — halves and half team totals

Generated 2026-11-24 23:59 UTC. 1874 graded period markets (243 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 755 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 47.5% (n=541)
- **total**: default side won 49.9% (n=371)
- **ml**: default side won 68.1% (n=329)
- **tt_home**: default side won 50.3% (n=308)
- **tt_away**: default side won 50.6% (n=310)
- **2h_tt_ot**: default side won 80.0% (n=30)
- **2h_tt_no_ot**: default side won 49.0% (n=588)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 24-28 | 46.2 | 49.6 | -3.4 | -7.08 | -13.6 | 0.12 | no edge shown yet |
| pin_price | 3-11-2 | 21.4 | 38.0 | -16.6 | -7.9 | -49.4 | 0.94 | keep collecting (14/50) |
| follow_move | 87-61-3 | 58.8 | 49.6 | 9.2 | +32.54 | 21.5 | -0.01 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 9-26 | 25.7 | 50.4 | -24.7 | -18.55 | -53.0 | 0.51 | keep collecting (35/50) |
| follow_move+pin_value | 0-1 | 0.0 | 48.6 | -48.6 | -1.0 | -100.0 | 1.0 | keep collecting (1/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 69-76 | 47.6 | 49.5 | -1.9 | -16.16 | -11.1 |  | no edge shown yet |
| pin_price | 11-20-2 | 35.5 | 38.0 | -2.5 | +24.25 | 73.5 |  | keep collecting (31/50) |
| follow_move | 293-300-7 | 49.4 | 49.7 | -0.3 | +1.08 | 0.2 |  | no edge shown yet |
| fd_juice | 40-48 | 45.5 | 50.3 | -4.9 | -14.7 | -16.7 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 48.8 | -48.8 | -2.0 | -100.0 |  | keep collecting (2/50) |
| follow_move+pin_price | 5-9 | 35.7 | 37.4 | -1.7 | +21.58 | 154.1 |  | keep collecting (14/50) |
| follow_move+pin_value | 16-11 | 59.3 | 51.1 | 8.1 | +2.87 | 10.6 |  | keep collecting (27/50) |

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
| pin_value | 93-89 | 51.1 | 49.7 | 1.4 | -8.22 | -4.5 | 0.19 | no edge shown yet |
| pin_price | 13-38-2 | 25.5 | 32.6 | -7.1 | +9.26 | 17.5 | 0.69 | DROP: below break-even |
| follow_move | 222-177-6 | 55.6 | 50.4 | 5.2 | +30.48 | 7.5 | -0.03 | no edge shown yet |
| fd_juice | 26-55 | 32.1 | 49.9 | -17.8 | -33.62 | -41.5 | 0.31 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-4 | 42.9 | 50.4 | -7.5 | -1.29 | -18.4 | 0.29 | keep collecting (7/50) |
| follow_move+pin_price | 2-0 | 100.0 | 31.9 | 68.1 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 212-185 | 53.4 | 49.7 | 3.7 | -0.98 | -0.2 |  | no edge shown yet |
| pin_price | 25-66-3 | 27.5 | 32.6 | -5.2 | +41.99 | 44.7 |  | DROP: below break-even |
| follow_move | 674-734-13 | 47.9 | 49.4 | -1.5 | -46.94 | -3.3 |  | DROP: below break-even |
| fd_juice | 99-123 | 44.6 | 50.1 | -5.5 | -40.84 | -18.4 |  | DROP: below break-even |
| follow_move+pin_price | 12-20-1 | 37.5 | 31.9 | 5.6 | +49.28 | 149.3 |  | keep collecting (32/50) |
| follow_move+pin_value | 29-24 | 54.7 | 50.2 | 4.5 | +1.39 | 2.6 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 48.8 | -48.8 | -2.0 | -100.0 |  | keep collecting (2/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 212-185 | 53.4 | 3.7 | -0.2 |
| pin_value | close | 1h\|spread | 97-91 | 51.6 | 2.2 | -3.8 |
| pin_value | close | 1h\|total | 115-94 | 55.0 | 5.0 | 2.9 |
| pin_price | close | 1h | 25-66-3 | 27.5 | -5.2 | 44.7 |
| pin_price | close | 1h\|ml | 24-63-3 | 27.6 | -4.3 | 48.9 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -14.2 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -50.1 | -100.0 |
| follow_move | close | 1h | 402-368-13 | 52.2 | 3.3 | 8.8 |
| follow_move | close | 1h\|ml | 145-151-13 | 49.0 | 2.2 | 17.4 |
| follow_move | close | 1h\|spread | 118-85 | 58.1 | 7.8 | 11.4 |
| follow_move | close | 1h\|total | 139-132 | 51.3 | 1.3 | -2.9 |
| follow_move | close | 2h | 272-366 | 42.6 | -7.4 | -18.2 |
| follow_move | close | 2h OT game | 10-15 | 40.0 | -9.9 | -22.5 |
| follow_move | close | 2h no OT | 262-351 | 42.7 | -7.3 | -18.0 |
| follow_move | close | 2h\|spread | 90-108 | 45.5 | -4.7 | -12.6 |
| follow_move | close | 2h\|tt_away | 90-132 | 40.5 | -9.4 | -22.4 |
| follow_move | close | 2h\|tt_home | 92-126 | 42.2 | -7.7 | -19.1 |
| fd_juice | close | 1h | 11-12 | 47.8 | -2.8 | -12.1 |
| fd_juice | close | 1h\|spread | 10-10 | 50.0 | -0.7 | -8.1 |
| fd_juice | close | 1h\|total | 1-2 | 33.3 | -16.8 | -38.9 |
| fd_juice | close | 2h | 88-111 | 44.2 | -5.8 | -19.1 |
| fd_juice | close | 2h OT game | 3-6 | 33.3 | -16.5 | -39.5 |
| fd_juice | close | 2h no OT | 85-105 | 44.7 | -5.3 | -18.2 |
| fd_juice | close | 2h\|spread | 10-11 | 47.6 | -2.5 | -12.2 |
| fd_juice | close | 2h\|tt_away | 43-45 | 48.9 | -1.2 | -10.9 |
| fd_juice | close | 2h\|tt_home | 35-55 | 38.9 | -11.0 | -28.8 |
| follow_move+pin_price | close | 1h | 12-20-1 | 37.5 | 5.6 | 149.3 |
| follow_move+pin_value | close | 1h | 29-24 | 54.7 | 4.5 | 2.6 |
| fd_juice+pin_value | close | 1h | 0-2 | 0.0 | -48.8 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 12-20-1 | 37.5 | 5.6 | 149.3 |
| follow_move+pin_value | close | 1h\|spread | 12-8 | 60.0 | 9.5 | 12.3 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -47.5 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 17-16 | 51.5 | 1.5 | -3.2 |
| fd_juice+pin_value | close | 1h\|total | 0-1 | 0.0 | -50.1 | -100.0 |
| pin_value | early | 1h | 93-89 | 51.1 | 1.4 | -4.5 |
| pin_value | early | 1h\|spread | 43-39 | 52.4 | 3.0 | -2.0 |
| pin_value | early | 1h\|total | 50-50 | 50.0 | 0.0 | -6.6 |
| pin_price | early | 1h | 13-38-2 | 25.5 | -7.1 | 17.5 |
| pin_price | early | 1h\|ml | 12-37-2 | 24.5 | -7.4 | 18.2 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 52.5 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -50.1 | -100.0 |
| follow_move | early | 1h | 145-105-6 | 58.0 | 7.2 | 11.9 |
| follow_move | early | 1h\|ml | 65-47-6 | 58.0 | 6.1 | 13.4 |
| follow_move | early | 1h\|spread | 41-19 | 68.3 | 18.5 | 31.3 |
| follow_move | early | 1h\|total | 39-39 | 50.0 | -0.0 | -5.2 |
| follow_move | early | 2h | 77-72 | 51.7 | 1.9 | 0.0 |
| follow_move | early | 2h OT game | 3-3 | 50.0 | 0.1 | -3.1 |
| follow_move | early | 2h no OT | 74-69 | 51.7 | 2.0 | 0.1 |
| follow_move | early | 2h\|spread | 23-18 | 56.1 | 6.8 | 8.1 |
| follow_move | early | 2h\|tt_away | 25-26 | 49.0 | -0.9 | -4.8 |
| follow_move | early | 2h\|tt_home | 29-28 | 50.9 | 0.9 | -1.5 |
| fd_juice | early | 1h | 3-3 | 50.0 | 0.9 | -7.9 |
| fd_juice | early | 1h\|spread | 2-2 | 50.0 | 1.2 | -7.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | 0.1 | -8.4 |
| fd_juice | early | 2h | 23-52 | 30.7 | -19.3 | -44.2 |
| fd_juice | early | 2h no OT | 23-52 | 30.7 | -19.3 | -44.2 |
| fd_juice | early | 2h\|spread | 1-4 | 20.0 | -31.5 | -63.1 |
| fd_juice | early | 2h\|tt_away | 13-23 | 36.1 | -13.7 | -34.8 |
| fd_juice | early | 2h\|tt_home | 9-25 | 26.5 | -23.5 | -51.4 |
| follow_move+pin_value | early | 1h | 3-4 | 42.9 | -7.5 | -18.4 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 68.1 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 68.1 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 15.8 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-3 | 25.0 | -25.0 | -52.9 |
