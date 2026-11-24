# CBB period scorecard — halves and half team totals

Generated 2026-11-24 14:04 UTC. 1824 graded period markets (180 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 705 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 47.5% (n=530)
- **total**: default side won 50.4% (n=363)
- **ml**: default side won 68.4% (n=320)
- **tt_home**: default side won 51.0% (n=296)
- **tt_away**: default side won 50.8% (n=301)
- **2h_tt_ot**: default side won 78.6% (n=28)
- **2h_tt_no_ot**: default side won 49.6% (n=569)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 24-28 | 46.2 | 49.8 | -3.6 | -7.08 | -13.6 | 0.12 | no edge shown yet |
| pin_price | 3-10-2 | 23.1 | 37.6 | -14.5 | -6.9 | -46.0 | 0.73 | keep collecting (13/50) |
| follow_move | 79-58-3 | 57.7 | 49.3 | 8.3 | +28.5 | 20.4 | 0.0 | no edge shown yet |
| fd_juice | 8-25 | 24.2 | 49.9 | -25.7 | -18.42 | -55.8 | 0.52 | keep collecting (33/50) |
| follow_move+pin_value | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 1.0 | keep collecting (1/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 67-72 | 48.2 | 49.6 | -1.4 | -13.8 | -9.9 |  | no edge shown yet |
| pin_price | 10-20-2 | 33.3 | 37.5 | -4.2 | +23.15 | 72.3 |  | keep collecting (30/50) |
| follow_move | 268-282-6 | 48.7 | 49.6 | -0.9 | -4.66 | -0.8 |  | DROP: below break-even |
| fd_juice | 38-46 | 45.2 | 50.2 | -4.9 | -14.36 | -17.1 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 48.1 | -48.1 | -2.0 | -100.0 |  | keep collecting (2/50) |
| follow_move+pin_price | 5-9 | 35.7 | 36.9 | -1.2 | +21.58 | 154.1 |  | keep collecting (14/50) |
| follow_move+pin_value | 16-11 | 59.3 | 50.7 | 8.6 | +2.87 | 10.6 |  | keep collecting (27/50) |

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
| pin_value | 93-89 | 51.1 | 49.8 | 1.3 | -8.22 | -4.5 | 0.19 | no edge shown yet |
| pin_price | 13-37-2 | 26.0 | 32.2 | -6.2 | +10.26 | 19.7 | 0.63 | DROP: below break-even |
| follow_move | 214-174-6 | 55.2 | 50.4 | 4.8 | +26.45 | 6.7 | -0.03 | no edge shown yet |
| fd_juice | 25-54 | 31.6 | 49.9 | -18.2 | -33.49 | -42.4 | 0.3 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-4 | 42.9 | 50.4 | -7.5 | -1.29 | -18.4 | 0.29 | keep collecting (7/50) |
| follow_move+pin_price | 2-0 | 100.0 | 31.6 | 68.4 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 210-181 | 53.7 | 49.8 | 4.0 | +1.38 | 0.4 |  | no edge shown yet |
| pin_price | 24-66-3 | 26.7 | 32.3 | -5.6 | +40.89 | 44.0 |  | DROP: below break-even |
| follow_move | 649-716-12 | 47.5 | 49.3 | -1.8 | -52.68 | -3.8 |  | DROP: below break-even |
| fd_juice | 97-121 | 44.5 | 49.9 | -5.4 | -40.51 | -18.6 |  | DROP: below break-even |
| follow_move+pin_price | 12-20-1 | 37.5 | 31.6 | 5.9 | +49.28 | 149.3 |  | keep collecting (32/50) |
| follow_move+pin_value | 29-24 | 54.7 | 50.1 | 4.6 | +1.39 | 2.6 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 48.6 | -48.6 | -2.0 | -100.0 |  | keep collecting (2/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 210-181 | 53.7 | 4.0 | 0.4 |
| pin_value | close | 1h\|spread | 95-91 | 51.1 | 1.7 | -4.7 |
| pin_value | close | 1h\|total | 115-90 | 56.1 | 6.0 | 5.0 |
| pin_price | close | 1h | 24-66-3 | 26.7 | -5.6 | 44.0 |
| pin_price | close | 1h\|ml | 23-63-3 | 26.7 | -4.8 | 48.2 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -14.2 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.6 | -100.0 |
| follow_move | close | 1h | 389-361-12 | 51.9 | 3.0 | 8.4 |
| follow_move | close | 1h\|ml | 141-147-12 | 49.0 | 2.2 | 17.8 |
| follow_move | close | 1h\|spread | 116-83 | 58.3 | 8.0 | 11.7 |
| follow_move | close | 1h\|total | 132-131 | 50.2 | 0.3 | -5.0 |
| follow_move | close | 2h | 260-355 | 42.3 | -7.7 | -18.9 |
| follow_move | close | 2h OT game | 8-15 | 34.8 | -15.0 | -32.7 |
| follow_move | close | 2h no OT | 252-340 | 42.6 | -7.4 | -18.4 |
| follow_move | close | 2h\|spread | 86-106 | 44.8 | -5.4 | -13.9 |
| follow_move | close | 2h\|tt_away | 87-128 | 40.5 | -9.4 | -22.5 |
| follow_move | close | 2h\|tt_home | 87-121 | 41.8 | -8.0 | -19.8 |
| fd_juice | close | 1h | 11-12 | 47.8 | -2.8 | -12.1 |
| fd_juice | close | 1h\|spread | 10-10 | 50.0 | -0.7 | -8.1 |
| fd_juice | close | 1h\|total | 1-2 | 33.3 | -16.3 | -38.9 |
| fd_juice | close | 2h | 86-109 | 44.1 | -5.8 | -19.3 |
| fd_juice | close | 2h OT game | 3-6 | 33.3 | -16.4 | -39.5 |
| fd_juice | close | 2h no OT | 83-103 | 44.6 | -5.2 | -18.4 |
| fd_juice | close | 2h\|spread | 10-11 | 47.6 | -2.5 | -12.2 |
| fd_juice | close | 2h\|tt_away | 41-45 | 47.7 | -2.4 | -13.1 |
| fd_juice | close | 2h\|tt_home | 35-53 | 39.8 | -9.8 | -27.1 |
| follow_move+pin_price | close | 1h | 12-20-1 | 37.5 | 5.9 | 149.3 |
| follow_move+pin_value | close | 1h | 29-24 | 54.7 | 4.6 | 2.6 |
| fd_juice+pin_value | close | 1h | 0-2 | 0.0 | -48.6 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 12-20-1 | 37.5 | 5.9 | 149.3 |
| follow_move+pin_value | close | 1h\|spread | 12-8 | 60.0 | 9.5 | 12.3 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -47.5 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 17-16 | 51.5 | 1.6 | -3.2 |
| fd_juice+pin_value | close | 1h\|total | 0-1 | 0.0 | -49.6 | -100.0 |
| pin_value | early | 1h | 93-89 | 51.1 | 1.3 | -4.5 |
| pin_value | early | 1h\|spread | 43-39 | 52.4 | 3.0 | -2.0 |
| pin_value | early | 1h\|total | 50-50 | 50.0 | -0.1 | -6.6 |
| pin_price | early | 1h | 13-37-2 | 26.0 | -6.2 | 19.7 |
| pin_price | early | 1h\|ml | 12-36-2 | 25.0 | -6.6 | 20.6 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 52.5 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.6 | -100.0 |
| follow_move | early | 1h | 141-104-6 | 57.6 | 6.8 | 11.2 |
| follow_move | early | 1h\|ml | 64-47-6 | 57.7 | 5.8 | 13.0 |
| follow_move | early | 1h\|spread | 41-18 | 69.5 | 19.6 | 33.5 |
| follow_move | early | 1h\|total | 36-39 | 48.0 | -1.9 | -9.0 |
| follow_move | early | 2h | 73-70 | 51.0 | 1.3 | -1.2 |
| follow_move | early | 2h OT game | 1-3 | 25.0 | -24.6 | -51.8 |
| follow_move | early | 2h no OT | 72-67 | 51.8 | 2.1 | 0.3 |
| follow_move | early | 2h\|spread | 22-17 | 56.4 | 7.1 | 8.6 |
| follow_move | early | 2h\|tt_away | 24-26 | 48.0 | -1.9 | -6.7 |
| follow_move | early | 2h\|tt_home | 27-27 | 50.0 | 0.1 | -3.2 |
| fd_juice | early | 1h | 3-3 | 50.0 | 0.7 | -7.9 |
| fd_juice | early | 1h\|spread | 2-2 | 50.0 | 1.2 | -7.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.4 | -8.4 |
| fd_juice | early | 2h | 22-51 | 30.1 | -19.8 | -45.2 |
| fd_juice | early | 2h no OT | 22-51 | 30.1 | -19.8 | -45.2 |
| fd_juice | early | 2h\|spread | 1-4 | 20.0 | -31.5 | -63.1 |
| fd_juice | early | 2h\|tt_away | 12-22 | 35.3 | -14.5 | -36.4 |
| fd_juice | early | 2h\|tt_home | 9-25 | 26.5 | -23.3 | -51.4 |
| follow_move+pin_value | early | 1h | 3-4 | 42.9 | -7.5 | -18.4 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 68.4 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 68.4 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 15.8 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-3 | 25.0 | -25.0 | -52.9 |
