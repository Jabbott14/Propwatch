# CBB period scorecard — halves and half team totals

Generated 2026-11-19 02:42 UTC. 1357 graded period markets (282 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 238 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 49.1% (n=395)
- **total**: default side won 50.2% (n=273)
- **ml**: default side won 71.2% (n=240)
- **tt_home**: default side won 53.0% (n=217)
- **tt_away**: default side won 52.0% (n=225)
- **2h_tt_ot**: default side won 92.3% (n=13)
- **2h_tt_no_ot**: default side won 51.3% (n=429)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 2-0 | 100.0 | 50.0 | 50.0 | +1.84 | 92.2 | -0.5 | keep collecting (2/50) |
| pin_price | 0-1 | 0.0 | 31.0 | -31.0 | -1.0 | -100.0 | -0.5 | keep collecting (1/50) |
| follow_move | 24-21-1 | 53.3 | 49.5 | 3.8 | +1.85 | 4.0 | 0.0 | keep collecting (45/50) |
| fd_juice | 2-12 | 14.3 | 46.3 | -32.0 | -10.44 | -74.6 | 0.57 | keep collecting (14/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 20-25 | 44.4 | 50.5 | -6.0 | -7.54 | -16.8 |  | keep collecting (45/50) |
| pin_price | 5-3 | 62.5 | 31.0 | 31.5 | +15.33 | 191.6 |  | keep collecting (8/50) |
| follow_move | 89-103-1 | 46.4 | 47.6 | -1.2 | -7.08 | -3.7 |  | DROP: below break-even |
| fd_juice | 12-17 | 41.4 | 50.3 | -9.0 | -7.0 | -24.1 |  | keep collecting (29/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 52.0 | -52.0 | -1.0 | -100.0 |  | keep collecting (1/50) |
| follow_move+pin_price | 3-1 | 75.0 | 31.0 | 44.0 | +11.98 | 299.5 |  | keep collecting (4/50) |
| follow_move+pin_value | 5-2 | 71.4 | 51.4 | 20.0 | +2.35 | 33.5 |  | keep collecting (7/50) |

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
| pin_value | 71-61 | 53.8 | 49.9 | 3.9 | +0.7 | 0.5 | 0.2 | no edge shown yet |
| pin_price | 10-28 | 26.3 | 29.3 | -3.0 | +16.16 | 42.5 | 0.56 | keep collecting (38/50) |
| follow_move | 159-137-4 | 53.7 | 51.1 | 2.6 | -0.2 | -0.1 | -0.03 | no edge shown yet |
| fd_juice | 19-41 | 31.7 | 49.7 | -18.0 | -25.51 | -42.5 | 0.25 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-3 | 50.0 | 50.1 | -0.1 | -0.29 | -4.9 | 0.17 | keep collecting (6/50) |
| follow_move+pin_price | 2-0 | 100.0 | 28.7 | 71.2 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 163-134 | 54.9 | 49.9 | 5.0 | +7.64 | 2.6 |  | no edge shown yet |
| pin_price | 19-49-1 | 27.9 | 29.4 | -1.4 | +33.07 | 47.9 |  | DROP: below break-even |
| follow_move | 470-537-7 | 46.7 | 49.0 | -2.4 | -55.1 | -5.4 |  | DROP: below break-even |
| fd_juice | 71-92 | 43.6 | 49.6 | -6.0 | -33.15 | -20.3 |  | DROP: below break-even |
| follow_move+pin_price | 10-12-1 | 45.5 | 28.7 | 16.7 | +39.68 | 172.5 |  | keep collecting (22/50) |
| follow_move+pin_value | 18-15 | 54.5 | 49.9 | 4.6 | +0.86 | 2.6 |  | keep collecting (33/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 49.1 | -49.1 | -1.0 | -100.0 |  | keep collecting (1/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 163-134 | 54.9 | 5.0 | 2.6 |
| pin_value | close | 1h\|spread | 76-67 | 53.1 | 3.4 | -0.8 |
| pin_value | close | 1h\|total | 87-67 | 56.5 | 6.5 | 5.7 |
| pin_price | close | 1h | 19-49-1 | 27.9 | -1.4 | 47.9 |
| pin_price | close | 1h\|ml | 19-47-1 | 28.8 | 0.0 | 52.3 |
| pin_price | close | 1h\|spread | 0-1 | 0.0 | -49.1 | -100.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.8 | -100.0 |
| follow_move | close | 1h | 273-274-7 | 49.9 | 1.4 | 4.9 |
| follow_move | close | 1h\|ml | 100-114-7 | 46.7 | 0.5 | 14.0 |
| follow_move | close | 1h\|spread | 79-64 | 55.2 | 5.1 | 5.8 |
| follow_move | close | 1h\|total | 94-96 | 49.5 | -0.5 | -6.3 |
| follow_move | close | 2h | 197-263 | 42.8 | -6.8 | -17.9 |
| follow_move | close | 2h OT game | 2-6 | 25.0 | -23.8 | -51.0 |
| follow_move | close | 2h no OT | 195-257 | 43.1 | -6.5 | -17.3 |
| follow_move | close | 2h\|spread | 64-81 | 44.1 | -5.9 | -15.2 |
| follow_move | close | 2h\|tt_away | 66-95 | 41.0 | -8.5 | -21.5 |
| follow_move | close | 2h\|tt_home | 67-87 | 43.5 | -5.8 | -16.6 |
| fd_juice | close | 1h | 8-11 | 42.1 | -8.0 | -22.7 |
| fd_juice | close | 1h\|spread | 7-10 | 41.2 | -9.0 | -24.4 |
| fd_juice | close | 1h\|total | 1-1 | 50.0 | 0.2 | -8.4 |
| fd_juice | close | 2h | 63-81 | 43.8 | -5.8 | -20.0 |
| fd_juice | close | 2h OT game | 1-4 | 20.0 | -29.4 | -63.1 |
| fd_juice | close | 2h no OT | 62-77 | 44.6 | -4.9 | -18.5 |
| fd_juice | close | 2h\|spread | 9-8 | 52.9 | 2.8 | -2.3 |
| fd_juice | close | 2h\|tt_away | 32-32 | 50.0 | -0.2 | -8.8 |
| fd_juice | close | 2h\|tt_home | 22-41 | 34.9 | -13.7 | -36.2 |
| follow_move+pin_price | close | 1h | 10-12-1 | 45.5 | 16.7 | 172.5 |
| follow_move+pin_value | close | 1h | 18-15 | 54.5 | 4.6 | 2.6 |
| fd_juice+pin_value | close | 1h | 0-1 | 0.0 | -49.1 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 10-12-1 | 45.5 | 16.7 | 172.5 |
| follow_move+pin_value | close | 1h\|spread | 8-5 | 61.5 | 11.6 | 15.4 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -49.1 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 10-10 | 50.0 | 0.1 | -5.7 |
| pin_value | early | 1h | 71-61 | 53.8 | 3.9 | 0.5 |
| pin_value | early | 1h\|spread | 34-26 | 56.7 | 6.9 | 6.0 |
| pin_value | early | 1h\|total | 37-35 | 51.4 | 1.3 | -4.0 |
| pin_price | early | 1h | 10-28 | 26.3 | -3.0 | 42.5 |
| pin_price | early | 1h\|ml | 10-27 | 27.0 | -1.7 | 46.4 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.8 | -100.0 |
| follow_move | early | 1h | 103-79-4 | 56.6 | 4.4 | 3.0 |
| follow_move | early | 1h\|ml | 45-40-4 | 52.9 | -1.8 | -8.7 |
| follow_move | early | 1h\|spread | 29-13 | 69.0 | 19.2 | 32.3 |
| follow_move | early | 1h\|total | 29-26 | 52.7 | 2.7 | -0.2 |
| follow_move | early | 2h | 56-58 | 49.1 | -0.4 | -5.1 |
| follow_move | early | 2h no OT | 56-58 | 49.1 | -0.4 | -5.1 |
| follow_move | early | 2h\|spread | 18-16 | 52.9 | 3.3 | 1.8 |
| follow_move | early | 2h\|tt_away | 16-22 | 42.1 | -7.3 | -18.4 |
| follow_move | early | 2h\|tt_home | 22-20 | 52.4 | 3.0 | 1.2 |
| fd_juice | early | 1h | 2-3 | 40.0 | -9.9 | -26.4 |
| fd_juice | early | 1h\|spread | 1-2 | 33.3 | -16.4 | -38.4 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.2 | -8.4 |
| fd_juice | early | 2h | 17-38 | 30.9 | -18.7 | -44.0 |
| fd_juice | early | 2h no OT | 17-38 | 30.9 | -18.7 | -44.0 |
| fd_juice | early | 2h\|spread | 0-3 | 0.0 | -50.3 | -100.0 |
| fd_juice | early | 2h\|tt_away | 10-17 | 37.0 | -12.3 | -33.4 |
| fd_juice | early | 2h\|tt_home | 7-18 | 28.0 | -21.9 | -48.7 |
| follow_move+pin_value | early | 1h | 3-3 | 50.0 | -0.1 | -4.9 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 71.2 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 71.2 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 16.4 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-2 | 33.3 | -16.6 | -37.2 |
