# CBB period scorecard — halves and half team totals

Generated 2026-11-18 01:05 UTC. 1188 graded period markets (240 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 69 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 48.2% (n=340)
- **total**: default side won 50.4% (n=236)
- **ml**: default side won 71.6% (n=211)
- **tt_home**: default side won 52.0% (n=196)
- **tt_away**: default side won 49.7% (n=199)
- **2h_tt_ot**: default side won 92.3% (n=13)
- **2h_tt_no_ot**: default side won 49.5% (n=382)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| follow_move | 5-2 | 71.4 | 43.8 | 27.6 | +4.58 | 65.4 | 0.19 | keep collecting (7/50) |
| fd_juice | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.5 | keep collecting (2/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 1-11 | 8.3 | 47.1 | -38.8 | -10.13 | -84.4 |  | keep collecting (12/50) |
| pin_price | 1-1 | 50.0 | 30.8 | 19.2 | +1.6 | 80.0 |  | keep collecting (2/50) |
| follow_move | 25-28 | 47.2 | 45.8 | 1.4 | -1.78 | -3.4 |  | no edge shown yet |
| fd_juice | 5-7 | 41.7 | 49.4 | -7.8 | -2.72 | -22.6 |  | keep collecting (12/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 45.0 | -45.0 | -1.0 | -100.0 |  | keep collecting (1/50) |
| follow_move+pin_price | 1-1 | 50.0 | 30.8 | 19.2 | +1.6 | 80.0 |  | redundant -- identical record to pin_price alone, not independent confirmation |
| follow_move+pin_value | 0-1 | 0.0 | 53.8 | -53.8 | -1.0 | -100.0 |  | keep collecting (1/50) |

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
| pin_value | 69-61 | 53.1 | 49.9 | 3.2 | -1.14 | -0.9 | 0.22 | no edge shown yet |
| pin_price | 10-27 | 27.0 | 29.0 | -2.0 | +17.16 | 46.4 | 0.59 | keep collecting (37/50) |
| follow_move | 140-118-3 | 54.3 | 51.2 | 3.0 | +2.52 | 1.0 | -0.04 | no edge shown yet |
| fd_juice | 17-31 | 35.4 | 50.1 | -14.7 | -17.07 | -35.6 | 0.17 | keep collecting (48/50) |
| follow_move+pin_value | 3-3 | 50.0 | 50.2 | -0.2 | -0.29 | -4.9 | 0.17 | keep collecting (6/50) |
| follow_move+pin_price | 2-0 | 100.0 | 28.4 | 71.6 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 144-120 | 54.5 | 49.8 | 4.7 | +5.05 | 1.9 |  | no edge shown yet |
| pin_price | 15-47-1 | 24.2 | 29.1 | -4.9 | +19.34 | 30.7 |  | DROP: below break-even |
| follow_move | 406-462-6 | 46.8 | 49.0 | -2.3 | -49.8 | -5.7 |  | DROP: below break-even |
| fd_juice | 64-82 | 43.8 | 49.7 | -5.9 | -28.86 | -19.8 |  | DROP: below break-even |
| follow_move+pin_price | 8-12-1 | 40.0 | 28.4 | 11.6 | +29.3 | 139.5 |  | keep collecting (20/50) |
| follow_move+pin_value | 13-14 | 48.1 | 49.9 | -1.8 | -2.48 | -9.2 |  | keep collecting (27/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 48.2 | -48.2 | -1.0 | -100.0 |  | keep collecting (1/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 144-120 | 54.5 | 4.7 | 1.9 |
| pin_value | close | 1h\|spread | 68-61 | 52.7 | 3.2 | -1.7 |
| pin_value | close | 1h\|total | 76-59 | 56.3 | 6.2 | 5.3 |
| pin_price | close | 1h | 15-47-1 | 24.2 | -4.9 | 30.7 |
| pin_price | close | 1h\|ml | 15-45-1 | 25.0 | -3.4 | 35.0 |
| pin_price | close | 1h\|spread | 0-1 | 0.0 | -48.2 | -100.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.6 | -100.0 |
| follow_move | close | 1h | 226-237-6 | 48.8 | 0.5 | 2.2 |
| follow_move | close | 1h\|ml | 87-99-6 | 46.8 | 1.2 | 11.6 |
| follow_move | close | 1h\|spread | 67-53 | 55.8 | 5.6 | 6.9 |
| follow_move | close | 1h\|total | 72-85 | 45.9 | -4.1 | -13.0 |
| follow_move | close | 2h | 180-225 | 44.4 | -5.5 | -14.8 |
| follow_move | close | 2h OT game | 2-6 | 25.0 | -24.6 | -51.0 |
| follow_move | close | 2h no OT | 178-219 | 44.8 | -5.1 | -14.1 |
| follow_move | close | 2h\|spread | 59-67 | 46.8 | -3.3 | -10.1 |
| follow_move | close | 2h\|tt_away | 60-80 | 42.9 | -7.2 | -18.1 |
| follow_move | close | 2h\|tt_home | 61-78 | 43.9 | -5.7 | -15.9 |
| fd_juice | close | 1h | 6-9 | 40.0 | -10.5 | -26.4 |
| fd_juice | close | 1h\|spread | 5-8 | 38.5 | -12.2 | -29.2 |
| fd_juice | close | 1h\|total | 1-1 | 50.0 | 0.4 | -8.4 |
| fd_juice | close | 2h | 58-73 | 44.3 | -5.3 | -19.0 |
| fd_juice | close | 2h OT game | 1-4 | 20.0 | -29.6 | -63.1 |
| fd_juice | close | 2h no OT | 57-69 | 45.2 | -4.4 | -17.3 |
| fd_juice | close | 2h\|spread | 8-7 | 53.3 | 3.0 | -1.5 |
| fd_juice | close | 2h\|tt_away | 30-29 | 50.8 | 0.9 | -7.2 |
| fd_juice | close | 2h\|tt_home | 20-37 | 35.1 | -13.9 | -35.8 |
| follow_move+pin_price | close | 1h | 8-12-1 | 40.0 | 11.6 | 139.5 |
| follow_move+pin_value | close | 1h | 13-14 | 48.1 | -1.8 | -9.2 |
| fd_juice+pin_value | close | 1h | 0-1 | 0.0 | -48.2 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 8-12-1 | 40.0 | 11.6 | 139.5 |
| follow_move+pin_value | close | 1h\|spread | 8-5 | 61.5 | 11.7 | 15.4 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -48.2 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 5-9 | 35.7 | -14.2 | -32.0 |
| pin_value | early | 1h | 69-61 | 53.1 | 3.2 | -0.9 |
| pin_value | early | 1h\|spread | 33-26 | 55.9 | 6.4 | 4.5 |
| pin_value | early | 1h\|total | 36-35 | 50.7 | 0.6 | -5.3 |
| pin_price | early | 1h | 10-27 | 27.0 | -2.0 | 46.4 |
| pin_price | early | 1h\|ml | 10-26 | 27.8 | -0.7 | 50.4 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.6 | -100.0 |
| follow_move | early | 1h | 86-67-3 | 56.2 | 3.9 | 2.1 |
| follow_move | early | 1h\|ml | 41-34-3 | 54.7 | -0.2 | -5.7 |
| follow_move | early | 1h\|spread | 26-9 | 74.3 | 24.5 | 42.5 |
| follow_move | early | 1h\|total | 19-24 | 44.2 | -5.8 | -16.5 |
| follow_move | early | 2h | 54-51 | 51.4 | 1.8 | -0.8 |
| follow_move | early | 2h no OT | 54-51 | 51.4 | 1.8 | -0.8 |
| follow_move | early | 2h\|spread | 17-14 | 54.8 | 5.6 | 5.3 |
| follow_move | early | 2h\|tt_away | 16-19 | 45.7 | -4.4 | -11.4 |
| follow_move | early | 2h\|tt_home | 21-18 | 53.8 | 4.3 | 4.0 |
| fd_juice | early | 1h | 2-1 | 66.7 | 17.0 | 22.7 |
| fd_juice | early | 1h\|spread | 1-0 | 100.0 | 51.8 | 84.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.4 | -8.4 |
| fd_juice | early | 2h | 15-30 | 33.3 | -16.8 | -39.4 |
| fd_juice | early | 2h no OT | 15-30 | 33.3 | -16.8 | -39.4 |
| fd_juice | early | 2h\|spread | 0-3 | 0.0 | -50.6 | -100.0 |
| fd_juice | early | 2h\|tt_away | 9-12 | 42.9 | -7.2 | -22.8 |
| fd_juice | early | 2h\|tt_home | 6-15 | 28.6 | -21.5 | -47.4 |
| follow_move+pin_value | early | 1h | 3-3 | 50.0 | -0.2 | -4.9 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 71.6 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 71.6 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 16.1 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-2 | 33.3 | -16.5 | -37.2 |
