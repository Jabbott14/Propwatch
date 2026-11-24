# CBB period scorecard — halves and half team totals

Generated 2026-11-24 02:27 UTC. 1783 graded period markets (216 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 664 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 47.5% (n=518)
- **total**: default side won 50.6% (n=354)
- **ml**: default side won 68.3% (n=315)
- **tt_home**: default side won 51.2% (n=289)
- **tt_away**: default side won 51.7% (n=296)
- **2h_tt_ot**: default side won 84.0% (n=25)
- **2h_tt_no_ot**: default side won 50.0% (n=560)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 22-24 | 47.8 | 49.8 | -1.9 | -4.8 | -10.4 | 0.15 | keep collecting (46/50) |
| pin_price | 3-9-1 | 25.0 | 38.3 | -13.3 | -5.9 | -45.4 | 0.92 | keep collecting (12/50) |
| follow_move | 76-56-2 | 57.6 | 49.3 | 8.3 | +27.83 | 20.8 | -0.0 | no edge shown yet |
| fd_juice | 7-25 | 21.9 | 49.6 | -27.7 | -19.27 | -60.2 | 0.47 | keep collecting (32/50) |
| follow_move+pin_value | 0-1 | 0.0 | 50.4 | -50.4 | -1.0 | -100.0 | 1.0 | keep collecting (1/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 63-68 | 48.1 | 49.6 | -1.5 | -13.24 | -10.1 |  | no edge shown yet |
| pin_price | 10-19-1 | 34.5 | 38.2 | -3.7 | +24.15 | 80.5 |  | keep collecting (29/50) |
| follow_move | 251-267-4 | 48.5 | 49.4 | -0.9 | -3.08 | -0.6 |  | DROP: below break-even |
| fd_juice | 37-44 | 45.7 | 50.3 | -4.6 | -13.14 | -16.2 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 47.8 | -47.8 | -2.0 | -100.0 |  | keep collecting (2/50) |
| follow_move+pin_price | 5-9 | 35.7 | 37.6 | -1.9 | +21.58 | 154.1 |  | keep collecting (14/50) |
| follow_move+pin_value | 16-11 | 59.3 | 50.6 | 8.6 | +2.87 | 10.6 |  | keep collecting (27/50) |

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
| pin_value | 91-85 | 51.7 | 49.8 | 1.9 | -5.94 | -3.4 | 0.2 | no edge shown yet |
| pin_price | 13-36-1 | 26.5 | 32.4 | -5.9 | +11.26 | 22.5 | 0.67 | keep collecting (49/50) |
| follow_move | 211-172-5 | 55.1 | 50.3 | 4.7 | +25.77 | 6.6 | -0.03 | no edge shown yet |
| fd_juice | 24-54 | 30.8 | 49.7 | -18.9 | -34.33 | -44.0 | 0.28 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-4 | 42.9 | 50.4 | -7.5 | -1.29 | -18.4 | 0.29 | keep collecting (7/50) |
| follow_move+pin_price | 2-0 | 100.0 | 31.7 | 68.3 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 206-177 | 53.8 | 49.8 | 4.0 | +1.93 | 0.5 |  | no edge shown yet |
| pin_price | 24-65-2 | 27.0 | 32.5 | -5.5 | +41.89 | 46.0 |  | DROP: below break-even |
| follow_move | 632-701-10 | 47.4 | 49.3 | -1.8 | -51.1 | -3.8 |  | DROP: below break-even |
| fd_juice | 96-119 | 44.7 | 49.9 | -5.3 | -39.29 | -18.3 |  | DROP: below break-even |
| follow_move+pin_price | 12-20-1 | 37.5 | 31.7 | 5.8 | +49.28 | 149.3 |  | keep collecting (32/50) |
| follow_move+pin_value | 29-24 | 54.7 | 50.1 | 4.6 | +1.39 | 2.6 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 48.5 | -48.5 | -2.0 | -100.0 |  | keep collecting (2/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 206-177 | 53.8 | 4.0 | 0.5 |
| pin_value | close | 1h\|spread | 94-91 | 50.8 | 1.4 | -5.2 |
| pin_value | close | 1h\|total | 112-86 | 56.6 | 6.5 | 5.8 |
| pin_price | close | 1h | 24-65-2 | 27.0 | -5.5 | 46.0 |
| pin_price | close | 1h\|ml | 23-62-2 | 27.1 | -4.7 | 50.5 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -14.2 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.4 | -100.0 |
| follow_move | close | 1h | 378-355-10 | 51.6 | 2.8 | 8.3 |
| follow_move | close | 1h\|ml | 138-145-10 | 48.8 | 2.2 | 18.7 |
| follow_move | close | 1h\|spread | 111-82 | 57.5 | 7.2 | 10.1 |
| follow_move | close | 1h\|total | 129-128 | 50.2 | 0.3 | -5.0 |
| follow_move | close | 2h | 254-346 | 42.3 | -7.6 | -18.8 |
| follow_move | close | 2h OT game | 7-12 | 36.8 | -12.9 | -28.4 |
| follow_move | close | 2h no OT | 247-334 | 42.5 | -7.4 | -18.5 |
| follow_move | close | 2h\|spread | 84-102 | 45.2 | -5.0 | -13.2 |
| follow_move | close | 2h\|tt_away | 86-125 | 40.8 | -9.0 | -21.9 |
| follow_move | close | 2h\|tt_home | 84-119 | 41.4 | -8.4 | -20.6 |
| fd_juice | close | 1h | 11-12 | 47.8 | -2.8 | -12.1 |
| fd_juice | close | 1h\|spread | 10-10 | 50.0 | -0.8 | -8.1 |
| fd_juice | close | 1h\|total | 1-2 | 33.3 | -16.1 | -38.9 |
| fd_juice | close | 2h | 85-107 | 44.3 | -5.6 | -19.0 |
| fd_juice | close | 2h OT game | 3-6 | 33.3 | -16.2 | -39.5 |
| fd_juice | close | 2h no OT | 82-101 | 44.8 | -5.1 | -18.0 |
| fd_juice | close | 2h\|spread | 10-11 | 47.6 | -2.5 | -12.2 |
| fd_juice | close | 2h\|tt_away | 40-45 | 47.1 | -3.2 | -14.2 |
| fd_juice | close | 2h\|tt_home | 35-51 | 40.7 | -8.8 | -25.4 |
| follow_move+pin_price | close | 1h | 12-20-1 | 37.5 | 5.8 | 149.3 |
| follow_move+pin_value | close | 1h | 29-24 | 54.7 | 4.6 | 2.6 |
| fd_juice+pin_value | close | 1h | 0-2 | 0.0 | -48.5 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 12-20-1 | 37.5 | 5.8 | 149.3 |
| follow_move+pin_value | close | 1h\|spread | 12-8 | 60.0 | 9.5 | 12.3 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -47.5 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 17-16 | 51.5 | 1.7 | -3.2 |
| fd_juice+pin_value | close | 1h\|total | 0-1 | 0.0 | -49.4 | -100.0 |
| pin_value | early | 1h | 91-85 | 51.7 | 1.9 | -3.4 |
| pin_value | early | 1h\|spread | 43-37 | 53.8 | 4.3 | 0.4 |
| pin_value | early | 1h\|total | 48-48 | 50.0 | -0.1 | -6.5 |
| pin_price | early | 1h | 13-36-1 | 26.5 | -5.9 | 22.5 |
| pin_price | early | 1h\|ml | 12-35-1 | 25.5 | -6.2 | 23.5 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 52.5 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.4 | -100.0 |
| follow_move | early | 1h | 140-102-5 | 57.9 | 7.1 | 11.9 |
| follow_move | early | 1h\|ml | 64-47-5 | 57.7 | 5.8 | 13.1 |
| follow_move | early | 1h\|spread | 40-18 | 69.0 | 19.1 | 32.5 |
| follow_move | early | 1h\|total | 36-37 | 49.3 | -0.6 | -6.5 |
| follow_move | early | 2h | 71-70 | 50.4 | 0.7 | -2.5 |
| follow_move | early | 2h OT game | 1-3 | 25.0 | -24.8 | -51.8 |
| follow_move | early | 2h no OT | 70-67 | 51.1 | 1.5 | -1.0 |
| follow_move | early | 2h\|spread | 21-17 | 55.3 | 6.1 | 6.3 |
| follow_move | early | 2h\|tt_away | 24-26 | 48.0 | -1.7 | -6.7 |
| follow_move | early | 2h\|tt_home | 26-27 | 49.1 | -0.8 | -4.8 |
| fd_juice | early | 1h | 3-3 | 50.0 | 0.6 | -7.9 |
| fd_juice | early | 1h\|spread | 2-2 | 50.0 | 1.3 | -7.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.6 | -8.4 |
| fd_juice | early | 2h | 21-51 | 29.2 | -20.6 | -47.0 |
| fd_juice | early | 2h no OT | 21-51 | 29.2 | -20.6 | -47.0 |
| fd_juice | early | 2h\|spread | 0-4 | 0.0 | -51.3 | -100.0 |
| fd_juice | early | 2h\|tt_away | 12-22 | 35.3 | -14.3 | -36.4 |
| fd_juice | early | 2h\|tt_home | 9-25 | 26.5 | -23.2 | -51.4 |
| follow_move+pin_value | early | 1h | 3-4 | 42.9 | -7.5 | -18.4 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 68.3 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 68.3 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 15.8 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-3 | 25.0 | -25.0 | -52.9 |
