# CBB period scorecard — halves and half team totals

Generated 2026-11-27 23:37 UTC. 2170 graded period markets (266 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 1051 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 47.1% (n=628)
- **total**: default side won 50.8% (n=429)
- **ml**: default side won 65.8% (n=377)
- **tt_home**: default side won 50.3% (n=362)
- **tt_away**: default side won 51.5% (n=357)
- **2h_tt_ot**: default side won 83.3% (n=36)
- **2h_tt_no_ot**: default side won 49.2% (n=683)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 47-44 | 51.6 | 50.6 | 1.1 | -3.5 | -3.8 | 0.16 | no edge shown yet |
| pin_price | 5-16-2 | 23.8 | 41.0 | -17.2 | -10.52 | -45.7 | 0.91 | keep collecting (21/50) |
| follow_move | 125-84-3 | 59.8 | 49.7 | 10.1 | +45.42 | 21.4 | -0.07 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 18-29 | 38.3 | 50.2 | -11.9 | -14.01 | -29.8 | 0.51 | keep collecting (47/50) |
| follow_move+pin_value | 0-1 | 0.0 | 51.0 | -51.0 | -1.0 | -100.0 | 1.0 | keep collecting (1/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 110-97 | 53.1 | 50.1 | 3.1 | -1.96 | -0.9 |  | no edge shown yet |
| pin_price | 15-28-2 | 34.9 | 41.4 | -6.6 | +21.27 | 47.3 |  | keep collecting (43/50) |
| follow_move | 403-400-9 | 50.2 | 49.6 | 0.6 | +3.85 | 0.5 |  | no edge shown yet |
| fd_juice | 58-61 | 48.7 | 50.4 | -1.7 | -12.81 | -10.8 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 47.4 | -47.4 | -2.0 | -100.0 |  | keep collecting (2/50) |
| follow_move+pin_price | 7-9 | 43.8 | 40.8 | 3.0 | +23.86 | 149.1 |  | keep collecting (16/50) |
| follow_move+pin_value | 16-12 | 57.1 | 50.6 | 6.6 | +1.9 | 6.8 |  | keep collecting (28/50) |

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
| pin_value | 116-105 | 52.5 | 50.1 | 2.4 | -4.64 | -2.1 | 0.19 | no edge shown yet |
| pin_price | 15-43-2 | 25.9 | 34.7 | -8.8 | +6.64 | 11.1 | 0.71 | DROP: below break-even |
| follow_move | 260-200-6 | 56.5 | 50.3 | 6.3 | +43.36 | 9.3 | -0.06 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 35-58 | 37.6 | 49.9 | -12.2 | -29.08 | -31.3 | 0.33 | DROP: below break-even |
| follow_move+pin_value | 3-4 | 42.9 | 50.4 | -7.6 | -1.29 | -18.4 | 0.29 | keep collecting (7/50) |
| follow_move+pin_price | 2-0 | 100.0 | 34.2 | 65.8 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 253-206 | 55.1 | 49.9 | 5.2 | +13.22 | 2.9 |  | no edge shown yet |
| pin_price | 29-74-3 | 28.2 | 35.0 | -6.9 | +39.01 | 36.8 |  | DROP: below break-even |
| follow_move | 784-834-15 | 48.5 | 49.4 | -0.9 | -44.17 | -2.7 |  | DROP: below break-even |
| fd_juice | 117-136 | 46.2 | 50.1 | -3.9 | -38.96 | -15.4 |  | DROP: below break-even |
| follow_move+pin_price | 14-20-1 | 41.2 | 34.2 | 7.0 | +51.56 | 147.3 |  | keep collecting (34/50) |
| follow_move+pin_value | 29-25 | 53.7 | 50.1 | 3.6 | +0.42 | 0.8 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 48.2 | -48.2 | -2.0 | -100.0 |  | keep collecting (2/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 253-206 | 55.1 | 5.2 | 2.9 |
| pin_value | close | 1h\|spread | 115-101 | 53.2 | 3.7 | -0.8 |
| pin_value | close | 1h\|total | 138-105 | 56.8 | 6.6 | 6.2 |
| pin_price | close | 1h | 29-74-3 | 28.2 | -6.9 | 36.8 |
| pin_price | close | 1h\|ml | 28-71-3 | 28.3 | -6.3 | 40.2 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -13.8 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.2 | -100.0 |
| follow_move | close | 1h | 457-417-15 | 52.3 | 3.3 | 8.1 |
| follow_move | close | 1h\|ml | 170-166-15 | 50.6 | 3.4 | 18.0 |
| follow_move | close | 1h\|spread | 131-100 | 56.7 | 6.4 | 8.8 |
| follow_move | close | 1h\|total | 156-151 | 50.8 | 1.0 | -3.7 |
| follow_move | close | 2h | 327-417 | 44.0 | -6.0 | -15.7 |
| follow_move | close | 2h OT game | 14-16 | 46.7 | -3.4 | -10.3 |
| follow_move | close | 2h no OT | 313-401 | 43.8 | -6.1 | -15.9 |
| follow_move | close | 2h\|spread | 104-124 | 45.6 | -4.5 | -12.3 |
| follow_move | close | 2h\|tt_away | 111-148 | 42.9 | -6.9 | -18.0 |
| follow_move | close | 2h\|tt_home | 112-145 | 43.6 | -6.4 | -16.3 |
| fd_juice | close | 1h | 11-13 | 45.8 | -4.9 | -15.7 |
| fd_juice | close | 1h\|spread | 10-11 | 47.6 | -3.3 | -12.4 |
| fd_juice | close | 1h\|total | 1-2 | 33.3 | -15.9 | -38.9 |
| fd_juice | close | 2h | 106-123 | 46.3 | -3.8 | -15.4 |
| fd_juice | close | 2h OT game | 5-6 | 45.5 | -4.4 | -16.2 |
| fd_juice | close | 2h no OT | 101-117 | 46.3 | -3.7 | -15.3 |
| fd_juice | close | 2h\|spread | 13-13 | 50.0 | -0.2 | -7.7 |
| fd_juice | close | 2h\|tt_away | 51-47 | 52.0 | 1.9 | -5.2 |
| fd_juice | close | 2h\|tt_home | 42-63 | 40.0 | -9.9 | -26.7 |
| follow_move+pin_price | close | 1h | 14-20-1 | 41.2 | 7.0 | 147.3 |
| follow_move+pin_value | close | 1h | 29-25 | 53.7 | 3.6 | 0.8 |
| fd_juice+pin_value | close | 1h | 0-2 | 0.0 | -48.2 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 14-20-1 | 41.2 | 7.0 | 147.3 |
| follow_move+pin_value | close | 1h\|spread | 12-8 | 60.0 | 9.4 | 12.3 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -47.1 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 17-17 | 50.0 | 0.1 | -6.0 |
| fd_juice+pin_value | close | 1h\|total | 0-1 | 0.0 | -49.2 | -100.0 |
| pin_value | early | 1h | 116-105 | 52.5 | 2.4 | -2.1 |
| pin_value | early | 1h\|spread | 53-47 | 53.0 | 3.2 | -1.3 |
| pin_value | early | 1h\|total | 63-58 | 52.1 | 1.8 | -2.8 |
| pin_price | early | 1h | 15-43-2 | 25.9 | -8.8 | 11.1 |
| pin_price | early | 1h\|ml | 14-42-2 | 25.0 | -9.2 | 11.5 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 52.9 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.2 | -100.0 |
| follow_move | early | 1h | 163-118-6 | 58.0 | 7.5 | 12.1 |
| follow_move | early | 1h\|ml | 73-49-6 | 59.8 | 8.3 | 17.0 |
| follow_move | early | 1h\|spread | 47-24 | 66.2 | 16.5 | 27.5 |
| follow_move | early | 1h\|total | 43-45 | 48.9 | -0.9 | -7.3 |
| follow_move | early | 2h | 97-82 | 54.2 | 4.4 | 4.8 |
| follow_move | early | 2h OT game | 6-4 | 60.0 | 9.5 | 15.3 |
| follow_move | early | 2h no OT | 91-78 | 53.8 | 4.1 | 4.1 |
| follow_move | early | 2h\|spread | 28-21 | 57.1 | 7.6 | 9.9 |
| follow_move | early | 2h\|tt_away | 33-28 | 54.1 | 4.3 | 4.8 |
| follow_move | early | 2h\|tt_home | 36-33 | 52.2 | 2.2 | 1.1 |
| fd_juice | early | 1h | 3-3 | 50.0 | 0.7 | -7.9 |
| fd_juice | early | 1h\|spread | 2-2 | 50.0 | 1.4 | -7.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.8 | -8.4 |
| fd_juice | early | 2h | 32-55 | 36.8 | -13.1 | -32.9 |
| fd_juice | early | 2h OT game | 1-0 | 100.0 | 48.5 | 88.5 |
| fd_juice | early | 2h no OT | 31-55 | 36.0 | -13.8 | -34.3 |
| fd_juice | early | 2h\|spread | 1-4 | 20.0 | -31.7 | -63.1 |
| fd_juice | early | 2h\|tt_away | 16-25 | 39.0 | -10.6 | -29.2 |
| fd_juice | early | 2h\|tt_home | 15-26 | 36.6 | -13.3 | -32.9 |
| follow_move+pin_value | early | 1h | 3-4 | 42.9 | -7.6 | -18.4 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 65.8 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 65.8 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 15.7 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-3 | 25.0 | -25.0 | -52.9 |
