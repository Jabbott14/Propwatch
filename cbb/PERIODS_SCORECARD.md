# CBB period scorecard — halves and half team totals

Generated 2026-11-23 13:24 UTC. 1720 graded period markets (162 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 601 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 47.2% (n=500)
- **total**: default side won 50.9% (n=344)
- **ml**: default side won 68.3% (n=303)
- **tt_home**: default side won 51.1% (n=278)
- **tt_away**: default side won 52.5% (n=284)
- **2h_tt_ot**: default side won 82.6% (n=23)
- **2h_tt_no_ot**: default side won 50.5% (n=539)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 21-22 | 48.8 | 49.5 | -0.6 | -3.69 | -8.6 | 0.12 | keep collecting (43/50) |
| pin_price | 3-8-1 | 27.3 | 38.7 | -11.5 | -4.9 | -40.8 | 0.62 | keep collecting (11/50) |
| follow_move | 63-50-2 | 55.8 | 49.2 | 6.5 | +21.87 | 19.0 | -0.03 | no edge shown yet |
| fd_juice | 7-23 | 23.3 | 49.3 | -26.0 | -17.27 | -57.6 | 0.43 | keep collecting (30/50) |
| follow_move+pin_value | 0-1 | 0.0 | 51.2 | -51.2 | -1.0 | -100.0 | 1.0 | keep collecting (1/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 61-61 | 50.0 | 49.4 | 0.6 | -8.04 | -6.6 |  | no edge shown yet |
| pin_price | 10-16-1 | 38.5 | 38.6 | -0.2 | +27.15 | 100.6 |  | keep collecting (26/50) |
| follow_move | 224-242-4 | 48.1 | 49.4 | -1.3 | -4.72 | -1.0 |  | DROP: below break-even |
| fd_juice | 30-41 | 42.3 | 50.9 | -8.7 | -15.96 | -22.5 |  | DROP: below break-even |
| fd_juice+pin_value | 0-2 | 0.0 | 46.9 | -46.9 | -2.0 | -100.0 |  | keep collecting (2/50) |
| follow_move+pin_price | 5-6 | 45.5 | 38.1 | 7.4 | +24.58 | 223.5 |  | keep collecting (11/50) |
| follow_move+pin_value | 15-8 | 65.2 | 50.1 | 15.1 | +4.98 | 21.6 |  | keep collecting (23/50) |

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
| pin_value | 90-83 | 52.0 | 49.8 | 2.2 | -4.83 | -2.8 | 0.19 | no edge shown yet |
| pin_price | 13-35-1 | 27.1 | 32.4 | -5.3 | +12.26 | 25.0 | 0.59 | keep collecting (48/50) |
| follow_move | 198-166-5 | 54.4 | 50.3 | 4.1 | +19.82 | 5.4 | -0.04 | no edge shown yet |
| fd_juice | 24-52 | 31.6 | 49.6 | -18.1 | -32.33 | -42.5 | 0.26 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-4 | 42.9 | 50.4 | -7.5 | -1.29 | -18.4 | 0.29 | keep collecting (7/50) |
| follow_move+pin_price | 2-0 | 100.0 | 31.7 | 68.3 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 204-170 | 54.5 | 49.7 | 4.8 | +7.14 | 1.9 |  | no edge shown yet |
| pin_price | 24-62-2 | 27.9 | 32.4 | -4.5 | +44.89 | 51.0 |  | DROP: below break-even |
| follow_move | 605-676-10 | 47.2 | 49.3 | -2.1 | -52.74 | -4.1 |  | DROP: below break-even |
| fd_juice | 89-116 | 43.4 | 50.0 | -6.6 | -42.1 | -20.5 |  | DROP: below break-even |
| follow_move+pin_price | 12-17-1 | 41.4 | 31.7 | 9.7 | +52.28 | 174.3 |  | keep collecting (29/50) |
| follow_move+pin_value | 28-21 | 57.1 | 49.9 | 7.2 | +3.49 | 7.1 |  | keep collecting (49/50) |
| fd_juice+pin_value | 0-2 | 0.0 | 48.2 | -48.2 | -2.0 | -100.0 |  | keep collecting (2/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 204-170 | 54.5 | 4.8 | 1.9 |
| pin_value | close | 1h\|spread | 93-88 | 51.4 | 2.1 | -4.1 |
| pin_value | close | 1h\|total | 111-82 | 57.5 | 7.4 | 7.6 |
| pin_price | close | 1h | 24-62-2 | 27.9 | -4.5 | 51.0 |
| pin_price | close | 1h\|ml | 23-59-2 | 28.0 | -3.6 | 55.8 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -13.9 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.1 | -100.0 |
| follow_move | close | 1h | 359-344-10 | 51.1 | 2.3 | 7.5 |
| follow_move | close | 1h\|ml | 131-140-10 | 48.3 | 1.5 | 18.3 |
| follow_move | close | 1h\|spread | 104-81 | 56.2 | 5.9 | 7.6 |
| follow_move | close | 1h\|total | 124-123 | 50.2 | 0.4 | -5.0 |
| follow_move | close | 2h | 246-332 | 42.6 | -7.3 | -18.3 |
| follow_move | close | 2h OT game | 5-12 | 29.4 | -20.0 | -42.5 |
| follow_move | close | 2h no OT | 241-320 | 43.0 | -6.9 | -17.6 |
| follow_move | close | 2h\|spread | 80-99 | 44.7 | -5.5 | -14.1 |
| follow_move | close | 2h\|tt_away | 84-118 | 41.6 | -8.0 | -20.3 |
| follow_move | close | 2h\|tt_home | 82-115 | 41.6 | -8.2 | -20.1 |
| fd_juice | close | 1h | 9-12 | 42.9 | -7.6 | -21.2 |
| fd_juice | close | 1h\|spread | 8-10 | 44.4 | -6.2 | -18.3 |
| fd_juice | close | 1h\|total | 1-2 | 33.3 | -15.8 | -38.9 |
| fd_juice | close | 2h | 80-104 | 43.5 | -6.5 | -20.5 |
| fd_juice | close | 2h OT game | 3-6 | 33.3 | -16.0 | -39.5 |
| fd_juice | close | 2h no OT | 77-98 | 44.0 | -6.0 | -19.5 |
| fd_juice | close | 2h\|spread | 10-11 | 47.6 | -2.5 | -12.2 |
| fd_juice | close | 2h\|tt_away | 38-44 | 46.3 | -4.1 | -15.4 |
| fd_juice | close | 2h\|tt_home | 32-49 | 39.5 | -10.0 | -27.7 |
| follow_move+pin_price | close | 1h | 12-17-1 | 41.4 | 9.7 | 174.3 |
| follow_move+pin_value | close | 1h | 28-21 | 57.1 | 7.2 | 7.1 |
| fd_juice+pin_value | close | 1h | 0-2 | 0.0 | -48.2 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 12-17-1 | 41.4 | 9.7 | 174.3 |
| follow_move+pin_value | close | 1h\|spread | 11-7 | 61.1 | 10.8 | 14.2 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -47.2 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 17-14 | 54.8 | 5.1 | 3.0 |
| fd_juice+pin_value | close | 1h\|total | 0-1 | 0.0 | -49.1 | -100.0 |
| pin_value | early | 1h | 90-83 | 52.0 | 2.2 | -2.8 |
| pin_value | early | 1h\|spread | 42-36 | 53.8 | 4.6 | 0.6 |
| pin_value | early | 1h\|total | 48-47 | 50.5 | 0.3 | -5.5 |
| pin_price | early | 1h | 13-35-1 | 27.1 | -5.3 | 25.0 |
| pin_price | early | 1h\|ml | 12-34-1 | 26.1 | -5.6 | 26.1 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 52.8 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.1 | -100.0 |
| follow_move | early | 1h | 131-98-5 | 57.2 | 6.4 | 10.8 |
| follow_move | early | 1h\|ml | 59-46-5 | 56.2 | 4.3 | 10.8 |
| follow_move | early | 1h\|spread | 37-18 | 67.3 | 17.4 | 29.1 |
| follow_move | early | 1h\|total | 35-34 | 50.7 | 0.9 | -3.9 |
| follow_move | early | 2h | 67-68 | 49.6 | 0.1 | -4.0 |
| follow_move | early | 2h OT game | 1-3 | 25.0 | -24.9 | -51.8 |
| follow_move | early | 2h no OT | 66-65 | 50.4 | 0.8 | -2.5 |
| follow_move | early | 2h\|spread | 19-17 | 52.8 | 3.7 | 1.3 |
| follow_move | early | 2h\|tt_away | 23-25 | 47.9 | -1.7 | -7.0 |
| follow_move | early | 2h\|tt_home | 25-26 | 49.0 | -0.8 | -5.0 |
| fd_juice | early | 1h | 3-3 | 50.0 | 0.6 | -7.9 |
| fd_juice | early | 1h\|spread | 2-2 | 50.0 | 1.4 | -7.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.9 | -8.4 |
| fd_juice | early | 2h | 21-49 | 30.0 | -19.7 | -45.5 |
| fd_juice | early | 2h no OT | 21-49 | 30.0 | -19.7 | -45.5 |
| fd_juice | early | 2h\|spread | 0-4 | 0.0 | -51.4 | -100.0 |
| fd_juice | early | 2h\|tt_away | 12-21 | 36.4 | -13.0 | -34.5 |
| fd_juice | early | 2h\|tt_home | 9-24 | 27.3 | -22.5 | -49.9 |
| follow_move+pin_value | early | 1h | 3-4 | 42.9 | -7.5 | -18.4 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 68.3 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 68.3 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 15.7 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-3 | 25.0 | -25.0 | -52.9 |
