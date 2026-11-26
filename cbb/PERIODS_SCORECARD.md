# CBB period scorecard — halves and half team totals

Generated 2026-11-26 17:10 UTC. 2059 graded period markets (218 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 940 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 47.0% (n=589)
- **total**: default side won 50.7% (n=410)
- **ml**: default side won 67.1% (n=359)
- **tt_home**: default side won 49.4% (n=344)
- **tt_away**: default side won 51.2% (n=340)
- **2h_tt_ot**: default side won 82.4% (n=34)
- **2h_tt_no_ot**: default side won 48.6% (n=650)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 42-38 | 52.5 | 50.4 | 2.1 | -1.75 | -2.2 | 0.16 | no edge shown yet |
| pin_price | 4-15-2 | 21.1 | 38.9 | -17.8 | -10.74 | -51.1 | 0.74 | keep collecting (19/50) |
| follow_move | 120-78-3 | 60.6 | 49.5 | 11.1 | +46.72 | 23.2 | -0.06 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 15-28 | 34.9 | 50.8 | -15.9 | -15.56 | -36.2 | 0.51 | keep collecting (43/50) |
| follow_move+pin_value | 0-1 | 0.0 | 50.8 | -50.8 | -1.0 | -100.0 | 1.0 | keep collecting (1/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 95-88 | 51.9 | 49.9 | 2.0 | -5.79 | -3.2 |  | no edge shown yet |
| pin_price | 13-26-2 | 33.3 | 38.9 | -5.5 | +20.53 | 50.1 |  | keep collecting (39/50) |
| follow_move | 369-354-9 | 51.0 | 49.7 | 1.4 | +17.8 | 2.4 |  | no edge shown yet |
| fd_juice | 54-56 | 49.1 | 50.7 | -1.7 | -11.14 | -10.1 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 47.3 | -47.3 | -2.0 | -100.0 |  | keep collecting (2/50) |
| follow_move+pin_price | 7-9 | 43.8 | 38.5 | 5.2 | +23.86 | 149.1 |  | keep collecting (16/50) |
| follow_move+pin_value | 17-11 | 60.7 | 50.6 | 10.1 | +3.77 | 13.5 |  | keep collecting (28/50) |

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
| pin_value | 111-99 | 52.9 | 50.0 | 2.9 | -2.89 | -1.4 | 0.2 | no edge shown yet |
| pin_price | 14-42-2 | 25.0 | 33.4 | -8.4 | +6.42 | 11.1 | 0.64 | DROP: below break-even |
| follow_move | 255-194-6 | 56.8 | 50.3 | 6.5 | +44.66 | 9.8 | -0.05 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 32-57 | 36.0 | 50.0 | -14.0 | -30.63 | -34.4 | 0.33 | DROP: below break-even |
| follow_move+pin_value | 3-4 | 42.9 | 50.4 | -7.6 | -1.29 | -18.4 | 0.29 | keep collecting (7/50) |
| follow_move+pin_price | 2-0 | 100.0 | 32.9 | 67.1 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 238-197 | 54.7 | 49.8 | 4.9 | +9.38 | 2.2 |  | no edge shown yet |
| pin_price | 27-72-3 | 27.3 | 33.5 | -6.2 | +38.27 | 37.5 |  | DROP: below break-even |
| follow_move | 750-788-15 | 48.8 | 49.4 | -0.7 | -30.22 | -1.9 |  | DROP: below break-even |
| fd_juice | 113-131 | 46.3 | 50.3 | -4.0 | -37.29 | -15.3 |  | DROP: below break-even |
| follow_move+pin_price | 14-20-1 | 41.2 | 32.9 | 8.3 | +51.56 | 147.3 |  | keep collecting (34/50) |
| follow_move+pin_value | 30-24 | 55.6 | 50.1 | 5.4 | +2.29 | 4.2 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 48.1 | -48.1 | -2.0 | -100.0 |  | keep collecting (2/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 238-197 | 54.7 | 4.9 | 2.2 |
| pin_value | close | 1h\|spread | 108-97 | 52.7 | 3.2 | -1.8 |
| pin_value | close | 1h\|total | 130-100 | 56.5 | 6.4 | 5.7 |
| pin_price | close | 1h | 27-72-3 | 27.3 | -6.2 | 37.5 |
| pin_price | close | 1h\|ml | 26-69-3 | 27.4 | -5.5 | 41.1 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -13.7 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.3 | -100.0 |
| follow_move | close | 1h | 440-398-15 | 52.5 | 3.6 | 8.8 |
| follow_move | close | 1h\|ml | 163-159-15 | 50.6 | 3.6 | 18.7 |
| follow_move | close | 1h\|spread | 126-94 | 57.3 | 6.9 | 9.9 |
| follow_move | close | 1h\|total | 151-145 | 51.0 | 1.2 | -3.4 |
| follow_move | close | 2h | 310-390 | 44.3 | -5.8 | -15.0 |
| follow_move | close | 2h OT game | 13-16 | 44.8 | -5.1 | -14.1 |
| follow_move | close | 2h no OT | 297-374 | 44.3 | -5.8 | -15.1 |
| follow_move | close | 2h\|spread | 98-114 | 46.2 | -4.0 | -11.2 |
| follow_move | close | 2h\|tt_away | 105-141 | 42.7 | -7.2 | -18.3 |
| follow_move | close | 2h\|tt_home | 107-135 | 44.2 | -5.9 | -15.1 |
| fd_juice | close | 1h | 11-13 | 45.8 | -4.9 | -15.7 |
| fd_juice | close | 1h\|spread | 10-11 | 47.6 | -3.4 | -12.4 |
| fd_juice | close | 1h\|total | 1-2 | 33.3 | -15.9 | -38.9 |
| fd_juice | close | 2h | 102-118 | 46.4 | -3.8 | -15.2 |
| fd_juice | close | 2h OT game | 4-6 | 40.0 | -9.8 | -26.3 |
| fd_juice | close | 2h no OT | 98-112 | 46.7 | -3.6 | -14.7 |
| fd_juice | close | 2h\|spread | 13-11 | 54.2 | 3.9 | 0.0 |
| fd_juice | close | 2h\|tt_away | 48-46 | 51.1 | 0.9 | -7.1 |
| fd_juice | close | 2h\|tt_home | 41-61 | 40.2 | -10.0 | -26.4 |
| follow_move+pin_price | close | 1h | 14-20-1 | 41.2 | 8.3 | 147.3 |
| follow_move+pin_value | close | 1h | 30-24 | 55.6 | 5.4 | 4.2 |
| fd_juice+pin_value | close | 1h | 0-2 | 0.0 | -48.1 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 14-20-1 | 41.2 | 8.3 | 147.3 |
| follow_move+pin_value | close | 1h\|spread | 12-8 | 60.0 | 9.4 | 12.3 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -47.0 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 18-16 | 52.9 | 3.1 | -0.5 |
| fd_juice+pin_value | close | 1h\|total | 0-1 | 0.0 | -49.3 | -100.0 |
| pin_value | early | 1h | 111-99 | 52.9 | 2.9 | -1.4 |
| pin_value | early | 1h\|spread | 50-43 | 53.8 | 4.1 | 0.2 |
| pin_value | early | 1h\|total | 61-56 | 52.1 | 1.9 | -2.6 |
| pin_price | early | 1h | 14-42-2 | 25.0 | -8.4 | 11.1 |
| pin_price | early | 1h\|ml | 13-41-2 | 24.1 | -8.8 | 11.5 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 53.0 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.3 | -100.0 |
| follow_move | early | 1h | 162-114-6 | 58.7 | 8.2 | 13.5 |
| follow_move | early | 1h\|ml | 73-48-6 | 60.3 | 8.8 | 17.9 |
| follow_move | early | 1h\|spread | 47-23 | 67.1 | 17.5 | 29.3 |
| follow_move | early | 1h\|total | 42-43 | 49.4 | -0.4 | -6.2 |
| follow_move | early | 2h | 93-80 | 53.8 | 3.9 | 3.9 |
| follow_move | early | 2h OT game | 5-4 | 55.6 | 5.3 | 6.1 |
| follow_move | early | 2h no OT | 88-76 | 53.7 | 3.8 | 3.7 |
| follow_move | early | 2h\|spread | 27-20 | 57.4 | 7.9 | 10.5 |
| follow_move | early | 2h\|tt_away | 31-27 | 53.4 | 3.6 | 3.4 |
| follow_move | early | 2h\|tt_home | 35-33 | 51.5 | 1.4 | -0.3 |
| fd_juice | early | 1h | 3-3 | 50.0 | 0.7 | -7.9 |
| fd_juice | early | 1h\|spread | 2-2 | 50.0 | 1.5 | -7.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.7 | -8.4 |
| fd_juice | early | 2h | 29-54 | 34.9 | -15.1 | -36.3 |
| fd_juice | early | 2h no OT | 29-54 | 34.9 | -15.1 | -36.3 |
| fd_juice | early | 2h\|spread | 1-4 | 20.0 | -31.8 | -63.1 |
| fd_juice | early | 2h\|tt_away | 15-24 | 38.5 | -11.3 | -30.4 |
| fd_juice | early | 2h\|tt_home | 13-26 | 33.3 | -16.8 | -38.8 |
| follow_move+pin_value | early | 1h | 3-4 | 42.9 | -7.6 | -18.4 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 67.1 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 67.1 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 15.7 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-3 | 25.0 | -25.0 | -52.9 |
