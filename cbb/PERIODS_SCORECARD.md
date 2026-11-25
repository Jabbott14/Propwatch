# CBB period scorecard — halves and half team totals

Generated 2026-11-25 08:56 UTC. 1966 graded period markets (204 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 847 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 46.9% (n=565)
- **total**: default side won 49.6% (n=387)
- **ml**: default side won 68.1% (n=345)
- **tt_home**: default side won 49.1% (n=326)
- **tt_away**: default side won 50.6% (n=328)
- **2h_tt_ot**: default side won 81.2% (n=32)
- **2h_tt_no_ot**: default side won 48.2% (n=622)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 33-33 | 50.0 | 49.8 | 0.2 | -4.34 | -6.6 | 0.2 | no edge shown yet |
| pin_price | 4-14-2 | 22.2 | 37.2 | -15.0 | -9.74 | -48.7 | 0.78 | keep collecting (18/50) |
| follow_move | 103-72-3 | 58.9 | 49.8 | 9.1 | +34.32 | 19.3 | -0.03 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 12-27 | 30.8 | 51.2 | -20.4 | -17.13 | -43.9 | 0.51 | keep collecting (39/50) |
| follow_move+pin_value | 0-1 | 0.0 | 48.2 | -48.2 | -1.0 | -100.0 | 1.0 | keep collecting (1/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 79-81 | 49.4 | 49.5 | -0.2 | -12.47 | -7.8 |  | no edge shown yet |
| pin_price | 12-23-2 | 34.3 | 37.2 | -2.9 | +22.39 | 60.5 |  | keep collecting (35/50) |
| follow_move | 335-327-7 | 50.6 | 49.8 | 0.8 | +9.5 | 1.4 |  | no edge shown yet |
| fd_juice | 48-52 | 48.0 | 50.6 | -2.6 | -12.09 | -12.1 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 48.4 | -48.4 | -2.0 | -100.0 |  | keep collecting (2/50) |
| follow_move+pin_price | 6-9 | 40.0 | 36.7 | 3.3 | +22.72 | 151.5 |  | keep collecting (15/50) |
| follow_move+pin_value | 17-11 | 60.7 | 51.4 | 9.3 | +3.77 | 13.5 |  | keep collecting (28/50) |

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
| pin_value | 102-94 | 52.0 | 49.7 | 2.3 | -5.48 | -2.8 | 0.21 | no edge shown yet |
| pin_price | 14-41-2 | 25.5 | 32.5 | -7.0 | +7.42 | 13.0 | 0.65 | DROP: below break-even |
| follow_move | 238-188-6 | 55.9 | 50.5 | 5.4 | +32.26 | 7.5 | -0.04 | no edge shown yet |
| fd_juice | 29-56 | 34.1 | 50.1 | -16.0 | -32.2 | -37.9 | 0.32 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-4 | 42.9 | 50.4 | -7.6 | -1.29 | -18.4 | 0.29 | keep collecting (7/50) |
| follow_move+pin_price | 2-0 | 100.0 | 31.9 | 68.1 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 222-190 | 53.9 | 49.7 | 4.2 | +2.7 | 0.7 |  | no edge shown yet |
| pin_price | 26-69-3 | 27.4 | 32.6 | -5.2 | +40.13 | 40.9 |  | DROP: below break-even |
| follow_move | 716-761-13 | 48.5 | 49.5 | -1.0 | -38.52 | -2.6 |  | DROP: below break-even |
| fd_juice | 107-127 | 45.7 | 50.3 | -4.6 | -38.24 | -16.3 |  | DROP: below break-even |
| follow_move+pin_price | 13-20-1 | 39.4 | 31.9 | 7.5 | +50.42 | 148.3 |  | keep collecting (33/50) |
| follow_move+pin_value | 30-24 | 55.6 | 50.3 | 5.3 | +2.29 | 4.2 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 48.6 | -48.6 | -2.0 | -100.0 |  | keep collecting (2/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 222-190 | 53.9 | 4.2 | 0.7 |
| pin_value | close | 1h\|spread | 101-93 | 52.1 | 2.7 | -2.9 |
| pin_value | close | 1h\|total | 121-97 | 55.5 | 5.6 | 3.8 |
| pin_price | close | 1h | 26-69-3 | 27.4 | -5.2 | 40.9 |
| pin_price | close | 1h\|ml | 25-66-3 | 27.5 | -4.4 | 44.8 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -13.6 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -50.4 | -100.0 |
| follow_move | close | 1h | 421-383-13 | 52.4 | 3.4 | 8.4 |
| follow_move | close | 1h\|ml | 155-155-13 | 50.0 | 3.0 | 17.3 |
| follow_move | close | 1h\|spread | 121-91 | 57.1 | 6.7 | 9.4 |
| follow_move | close | 1h\|total | 145-137 | 51.4 | 1.3 | -2.6 |
| follow_move | close | 2h | 295-378 | 43.8 | -6.3 | -15.9 |
| follow_move | close | 2h OT game | 11-15 | 42.3 | -7.4 | -18.5 |
| follow_move | close | 2h no OT | 284-363 | 43.9 | -6.2 | -15.8 |
| follow_move | close | 2h\|spread | 96-110 | 46.6 | -3.6 | -10.5 |
| follow_move | close | 2h\|tt_away | 99-137 | 41.9 | -8.0 | -19.7 |
| follow_move | close | 2h\|tt_home | 100-131 | 43.3 | -6.9 | -16.9 |
| fd_juice | close | 1h | 11-12 | 47.8 | -3.0 | -12.1 |
| fd_juice | close | 1h\|spread | 10-10 | 50.0 | -0.9 | -8.1 |
| fd_juice | close | 1h\|total | 1-2 | 33.3 | -17.1 | -38.9 |
| fd_juice | close | 2h | 96-115 | 45.5 | -4.7 | -16.8 |
| fd_juice | close | 2h OT game | 4-6 | 40.0 | -9.9 | -26.3 |
| fd_juice | close | 2h no OT | 92-109 | 45.8 | -4.5 | -16.3 |
| fd_juice | close | 2h\|spread | 13-11 | 54.2 | 3.9 | 0.0 |
| fd_juice | close | 2h\|tt_away | 46-46 | 50.0 | -0.1 | -9.0 |
| fd_juice | close | 2h\|tt_home | 37-58 | 38.9 | -11.4 | -28.6 |
| follow_move+pin_price | close | 1h | 13-20-1 | 39.4 | 7.5 | 148.3 |
| follow_move+pin_value | close | 1h | 30-24 | 55.6 | 5.3 | 4.2 |
| fd_juice+pin_value | close | 1h | 0-2 | 0.0 | -48.6 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 13-20-1 | 39.4 | 7.5 | 148.3 |
| follow_move+pin_value | close | 1h\|spread | 12-8 | 60.0 | 9.4 | 12.3 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -46.9 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 18-16 | 52.9 | 2.8 | -0.5 |
| fd_juice+pin_value | close | 1h\|total | 0-1 | 0.0 | -50.4 | -100.0 |
| pin_value | early | 1h | 102-94 | 52.0 | 2.3 | -2.8 |
| pin_value | early | 1h\|spread | 46-40 | 53.5 | 4.0 | -0.1 |
| pin_value | early | 1h\|total | 56-54 | 50.9 | 1.0 | -4.9 |
| pin_price | early | 1h | 14-41-2 | 25.5 | -7.0 | 13.0 |
| pin_price | early | 1h\|ml | 13-40-2 | 24.5 | -7.4 | 13.5 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 53.1 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -50.4 | -100.0 |
| follow_move | early | 1h | 153-111-6 | 58.0 | 7.0 | 11.1 |
| follow_move | early | 1h\|ml | 68-48-6 | 58.6 | 6.4 | 12.7 |
| follow_move | early | 1h\|spread | 44-22 | 66.7 | 16.9 | 28.2 |
| follow_move | early | 1h\|total | 41-41 | 50.0 | -0.1 | -5.1 |
| follow_move | early | 2h | 85-77 | 52.5 | 2.6 | 1.5 |
| follow_move | early | 2h OT game | 3-3 | 50.0 | 0.5 | -3.1 |
| follow_move | early | 2h no OT | 82-74 | 52.6 | 2.7 | 1.7 |
| follow_move | early | 2h\|spread | 26-19 | 57.8 | 8.4 | 11.3 |
| follow_move | early | 2h\|tt_away | 29-26 | 52.7 | 2.8 | 2.1 |
| follow_move | early | 2h\|tt_home | 30-32 | 48.4 | -1.7 | -6.2 |
| fd_juice | early | 1h | 3-3 | 50.0 | 1.2 | -7.9 |
| fd_juice | early | 1h\|spread | 2-2 | 50.0 | 1.5 | -7.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | 0.4 | -8.4 |
| fd_juice | early | 2h | 26-53 | 32.9 | -17.3 | -40.2 |
| fd_juice | early | 2h no OT | 26-53 | 32.9 | -17.3 | -40.2 |
| fd_juice | early | 2h\|spread | 1-4 | 20.0 | -31.9 | -63.1 |
| fd_juice | early | 2h\|tt_away | 14-24 | 36.8 | -13.0 | -33.5 |
| fd_juice | early | 2h\|tt_home | 11-25 | 30.6 | -19.7 | -44.1 |
| follow_move+pin_value | early | 1h | 3-4 | 42.9 | -7.6 | -18.4 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 68.1 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 68.1 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 15.6 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-3 | 25.0 | -25.0 | -52.9 |
