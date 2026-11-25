# CBB period scorecard — halves and half team totals

Generated 2026-11-25 19:29 UTC. 1985 graded period markets (206 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 866 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 46.8% (n=570)
- **total**: default side won 49.9% (n=389)
- **ml**: default side won 67.6% (n=349)
- **tt_home**: default side won 49.1% (n=330)
- **tt_away**: default side won 51.1% (n=331)
- **2h_tt_ot**: default side won 81.2% (n=32)
- **2h_tt_no_ot**: default side won 48.5% (n=629)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 33-34 | 49.3 | 49.8 | -0.5 | -5.34 | -8.0 | 0.19 | no edge shown yet |
| pin_price | 4-14-2 | 22.2 | 38.1 | -15.9 | -9.74 | -48.7 | 0.78 | keep collecting (18/50) |
| follow_move | 108-75-3 | 59.0 | 49.8 | 9.2 | +35.97 | 19.3 | -0.06 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 13-28 | 31.7 | 51.1 | -19.4 | -17.19 | -41.9 | 0.49 | keep collecting (41/50) |
| follow_move+pin_value | 0-1 | 0.0 | 48.8 | -48.8 | -1.0 | -100.0 | 1.0 | keep collecting (1/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 79-82 | 49.1 | 49.6 | -0.5 | -13.47 | -8.4 |  | no edge shown yet |
| pin_price | 12-23-2 | 34.3 | 38.2 | -3.9 | +22.39 | 60.5 |  | keep collecting (35/50) |
| follow_move | 340-335-8 | 50.4 | 49.8 | 0.5 | +7.48 | 1.1 |  | no edge shown yet |
| fd_juice | 52-52 | 50.0 | 50.7 | -0.7 | -8.8 | -8.5 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 48.0 | -48.0 | -2.0 | -100.0 |  | keep collecting (2/50) |
| follow_move+pin_price | 6-9 | 40.0 | 37.7 | 2.3 | +22.72 | 151.5 |  | keep collecting (15/50) |
| follow_move+pin_value | 17-11 | 60.7 | 51.2 | 9.5 | +3.77 | 13.5 |  | keep collecting (28/50) |

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
| pin_value | 102-95 | 51.8 | 49.7 | 2.0 | -6.48 | -3.3 | 0.21 | no edge shown yet |
| pin_price | 14-41-2 | 25.5 | 33.0 | -7.5 | +7.42 | 13.0 | 0.65 | DROP: below break-even |
| follow_move | 243-191-6 | 56.0 | 50.5 | 5.5 | +33.91 | 7.7 | -0.05 | no edge shown yet |
| fd_juice | 30-57 | 34.5 | 50.0 | -15.6 | -32.26 | -37.1 | 0.31 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-4 | 42.9 | 50.5 | -7.6 | -1.29 | -18.4 | 0.29 | keep collecting (7/50) |
| follow_move+pin_price | 2-0 | 100.0 | 32.4 | 67.6 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 222-191 | 53.8 | 49.7 | 4.1 | +1.7 | 0.4 |  | no edge shown yet |
| pin_price | 26-69-3 | 27.4 | 33.0 | -5.7 | +40.13 | 40.9 |  | DROP: below break-even |
| follow_move | 721-769-14 | 48.4 | 49.5 | -1.1 | -40.55 | -2.7 |  | DROP: below break-even |
| fd_juice | 111-127 | 46.6 | 50.3 | -3.7 | -34.94 | -14.7 |  | DROP: below break-even |
| follow_move+pin_price | 13-20-1 | 39.4 | 32.4 | 7.0 | +50.42 | 148.3 |  | keep collecting (33/50) |
| follow_move+pin_value | 30-24 | 55.6 | 50.3 | 5.3 | +2.29 | 4.2 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 48.5 | -48.5 | -2.0 | -100.0 |  | keep collecting (2/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 222-191 | 53.8 | 4.1 | 0.4 |
| pin_value | close | 1h\|spread | 101-94 | 51.8 | 2.5 | -3.4 |
| pin_value | close | 1h\|total | 121-97 | 55.5 | 5.5 | 3.8 |
| pin_price | close | 1h | 26-69-3 | 27.4 | -5.7 | 40.9 |
| pin_price | close | 1h\|ml | 25-66-3 | 27.5 | -4.9 | 44.8 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -13.5 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -50.1 | -100.0 |
| follow_move | close | 1h | 426-387-14 | 52.4 | 3.4 | 8.5 |
| follow_move | close | 1h\|ml | 158-156-14 | 50.3 | 3.2 | 18.0 |
| follow_move | close | 1h\|spread | 123-92 | 57.2 | 6.8 | 9.7 |
| follow_move | close | 1h\|total | 145-139 | 51.1 | 1.0 | -3.3 |
| follow_move | close | 2h | 295-382 | 43.6 | -6.5 | -16.4 |
| follow_move | close | 2h OT game | 11-15 | 42.3 | -7.4 | -18.5 |
| follow_move | close | 2h no OT | 284-367 | 43.6 | -6.5 | -16.3 |
| follow_move | close | 2h\|spread | 96-111 | 46.4 | -3.9 | -10.9 |
| follow_move | close | 2h\|tt_away | 99-139 | 41.6 | -8.3 | -20.4 |
| follow_move | close | 2h\|tt_home | 100-132 | 43.1 | -7.0 | -17.3 |
| fd_juice | close | 1h | 11-12 | 47.8 | -3.0 | -12.1 |
| fd_juice | close | 1h\|spread | 10-10 | 50.0 | -0.9 | -8.1 |
| fd_juice | close | 1h\|total | 1-2 | 33.3 | -16.8 | -38.9 |
| fd_juice | close | 2h | 100-115 | 46.5 | -3.7 | -15.0 |
| fd_juice | close | 2h OT game | 4-6 | 40.0 | -9.8 | -26.3 |
| fd_juice | close | 2h no OT | 96-109 | 46.8 | -3.4 | -14.4 |
| fd_juice | close | 2h\|spread | 13-11 | 54.2 | 3.9 | 0.0 |
| fd_juice | close | 2h\|tt_away | 47-46 | 50.5 | 0.4 | -8.1 |
| fd_juice | close | 2h\|tt_home | 40-58 | 40.8 | -9.5 | -25.2 |
| follow_move+pin_price | close | 1h | 13-20-1 | 39.4 | 7.0 | 148.3 |
| follow_move+pin_value | close | 1h | 30-24 | 55.6 | 5.3 | 4.2 |
| fd_juice+pin_value | close | 1h | 0-2 | 0.0 | -48.5 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 13-20-1 | 39.4 | 7.0 | 148.3 |
| follow_move+pin_value | close | 1h\|spread | 12-8 | 60.0 | 9.4 | 12.3 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -46.8 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 18-16 | 52.9 | 2.9 | -0.5 |
| fd_juice+pin_value | close | 1h\|total | 0-1 | 0.0 | -50.1 | -100.0 |
| pin_value | early | 1h | 102-95 | 51.8 | 2.0 | -3.3 |
| pin_value | early | 1h\|spread | 46-41 | 52.9 | 3.4 | -1.3 |
| pin_value | early | 1h\|total | 56-54 | 50.9 | 0.9 | -4.9 |
| pin_price | early | 1h | 14-41-2 | 25.5 | -7.5 | 13.0 |
| pin_price | early | 1h\|ml | 13-40-2 | 24.5 | -7.8 | 13.5 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 53.2 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -50.1 | -100.0 |
| follow_move | early | 1h | 157-112-6 | 58.4 | 7.5 | 11.8 |
| follow_move | early | 1h\|ml | 70-48-6 | 59.3 | 7.2 | 13.9 |
| follow_move | early | 1h\|spread | 46-22 | 67.6 | 17.9 | 30.2 |
| follow_move | early | 1h\|total | 41-42 | 49.4 | -0.6 | -6.3 |
| follow_move | early | 2h | 86-79 | 52.1 | 2.3 | 0.8 |
| follow_move | early | 2h OT game | 3-3 | 50.0 | 0.3 | -3.1 |
| follow_move | early | 2h no OT | 83-76 | 52.2 | 2.4 | 1.0 |
| follow_move | early | 2h\|spread | 26-19 | 57.8 | 8.4 | 11.3 |
| follow_move | early | 2h\|tt_away | 30-27 | 52.6 | 2.8 | 2.0 |
| follow_move | early | 2h\|tt_home | 30-33 | 47.6 | -2.5 | -7.7 |
| fd_juice | early | 1h | 3-3 | 50.0 | 1.1 | -7.9 |
| fd_juice | early | 1h\|spread | 2-2 | 50.0 | 1.6 | -7.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | 0.1 | -8.4 |
| fd_juice | early | 2h | 27-54 | 33.3 | -16.8 | -39.2 |
| fd_juice | early | 2h no OT | 27-54 | 33.3 | -16.8 | -39.2 |
| fd_juice | early | 2h\|spread | 1-4 | 20.0 | -31.9 | -63.1 |
| fd_juice | early | 2h\|tt_away | 14-24 | 36.8 | -12.9 | -33.5 |
| fd_juice | early | 2h\|tt_home | 12-26 | 31.6 | -18.7 | -41.9 |
| follow_move+pin_value | early | 1h | 3-4 | 42.9 | -7.6 | -18.4 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 67.6 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 67.6 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 15.6 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-3 | 25.0 | -25.0 | -52.9 |
