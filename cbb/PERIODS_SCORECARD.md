# CBB period scorecard — halves and half team totals

Generated 2026-11-27 01:50 UTC. 2096 graded period markets (248 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 977 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 46.9% (n=604)
- **total**: default side won 50.5% (n=416)
- **ml**: default side won 66.5% (n=364)
- **tt_home**: default side won 49.4% (n=350)
- **tt_away**: default side won 51.0% (n=345)
- **2h_tt_ot**: default side won 82.4% (n=34)
- **2h_tt_no_ot**: default side won 48.6% (n=661)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 45-42 | 51.7 | 50.5 | 1.2 | -3.15 | -3.6 | 0.17 | no edge shown yet |
| pin_price | 5-15-2 | 25.0 | 40.0 | -15.0 | -9.52 | -43.3 | 0.76 | keep collecting (20/50) |
| follow_move | 122-82-3 | 59.8 | 49.7 | 10.1 | +44.59 | 21.5 | -0.06 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 17-28 | 37.8 | 50.9 | -13.1 | -13.9 | -30.9 | 0.51 | keep collecting (45/50) |
| follow_move+pin_value | 0-1 | 0.0 | 50.3 | -50.3 | -1.0 | -100.0 | 1.0 | keep collecting (1/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 100-94 | 51.5 | 50.0 | 1.6 | -7.57 | -3.9 |  | no edge shown yet |
| pin_price | 14-27-2 | 34.1 | 40.0 | -5.9 | +21.29 | 49.5 |  | keep collecting (41/50) |
| follow_move | 379-367-9 | 50.8 | 49.7 | 1.1 | +14.77 | 2.0 |  | no edge shown yet |
| fd_juice | 56-57 | 49.6 | 50.7 | -1.2 | -10.44 | -9.2 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 47.4 | -47.4 | -2.0 | -100.0 |  | keep collecting (2/50) |
| follow_move+pin_price | 7-9 | 43.8 | 39.8 | 4.0 | +23.86 | 149.1 |  | keep collecting (16/50) |
| follow_move+pin_value | 17-12 | 58.6 | 50.8 | 7.8 | +2.77 | 9.6 |  | keep collecting (29/50) |

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
| pin_value | 114-103 | 52.5 | 50.0 | 2.5 | -4.29 | -2.0 | 0.2 | no edge shown yet |
| pin_price | 15-42-2 | 26.3 | 34.0 | -7.7 | +7.64 | 12.9 | 0.65 | DROP: below break-even |
| follow_move | 257-198-6 | 56.5 | 50.3 | 6.2 | +42.54 | 9.2 | -0.05 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 34-57 | 37.4 | 50.0 | -12.7 | -28.97 | -31.8 | 0.33 | DROP: below break-even |
| follow_move+pin_value | 3-4 | 42.9 | 50.4 | -7.6 | -1.29 | -18.4 | 0.29 | keep collecting (7/50) |
| follow_move+pin_price | 2-0 | 100.0 | 33.5 | 66.5 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 243-203 | 54.5 | 49.8 | 4.7 | +7.61 | 1.7 |  | no edge shown yet |
| pin_price | 28-73-3 | 27.7 | 34.1 | -6.3 | +39.03 | 37.5 |  | DROP: below break-even |
| follow_move | 760-801-15 | 48.7 | 49.5 | -0.8 | -33.25 | -2.1 |  | DROP: below break-even |
| fd_juice | 115-132 | 46.6 | 50.3 | -3.7 | -36.59 | -14.8 |  | DROP: below break-even |
| follow_move+pin_price | 14-20-1 | 41.2 | 33.5 | 7.7 | +51.56 | 147.3 |  | keep collecting (34/50) |
| follow_move+pin_value | 30-25 | 54.5 | 50.2 | 4.4 | +1.29 | 2.3 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 48.2 | -48.2 | -2.0 | -100.0 |  | keep collecting (2/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 243-203 | 54.5 | 4.7 | 1.7 |
| pin_value | close | 1h\|spread | 111-100 | 52.6 | 3.1 | -2.0 |
| pin_value | close | 1h\|total | 132-103 | 56.2 | 6.1 | 5.0 |
| pin_price | close | 1h | 28-73-3 | 27.7 | -6.3 | 37.5 |
| pin_price | close | 1h\|ml | 27-70-3 | 27.8 | -5.7 | 41.0 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -13.5 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.5 | -100.0 |
| follow_move | close | 1h | 444-403-15 | 52.4 | 3.5 | 8.6 |
| follow_move | close | 1h\|ml | 165-160-15 | 50.8 | 3.7 | 19.0 |
| follow_move | close | 1h\|spread | 127-96 | 57.0 | 6.5 | 9.3 |
| follow_move | close | 1h\|total | 152-147 | 50.8 | 0.9 | -3.7 |
| follow_move | close | 2h | 316-398 | 44.3 | -5.8 | -15.1 |
| follow_move | close | 2h OT game | 13-16 | 44.8 | -5.1 | -14.1 |
| follow_move | close | 2h no OT | 303-382 | 44.2 | -5.8 | -15.1 |
| follow_move | close | 2h\|spread | 100-118 | 45.9 | -4.3 | -11.8 |
| follow_move | close | 2h\|tt_away | 107-143 | 42.8 | -7.1 | -18.1 |
| follow_move | close | 2h\|tt_home | 109-137 | 44.3 | -5.8 | -14.9 |
| fd_juice | close | 1h | 11-13 | 45.8 | -5.0 | -15.7 |
| fd_juice | close | 1h\|spread | 10-11 | 47.6 | -3.4 | -12.4 |
| fd_juice | close | 1h\|total | 1-2 | 33.3 | -16.2 | -38.9 |
| fd_juice | close | 2h | 104-119 | 46.6 | -3.6 | -14.7 |
| fd_juice | close | 2h OT game | 4-6 | 40.0 | -9.8 | -26.3 |
| fd_juice | close | 2h no OT | 100-113 | 46.9 | -3.3 | -14.2 |
| fd_juice | close | 2h\|spread | 13-11 | 54.2 | 3.9 | 0.0 |
| fd_juice | close | 2h\|tt_away | 49-46 | 51.6 | 1.4 | -6.1 |
| fd_juice | close | 2h\|tt_home | 42-62 | 40.4 | -9.8 | -26.0 |
| follow_move+pin_price | close | 1h | 14-20-1 | 41.2 | 7.7 | 147.3 |
| follow_move+pin_value | close | 1h | 30-25 | 54.5 | 4.4 | 2.3 |
| fd_juice+pin_value | close | 1h | 0-2 | 0.0 | -48.2 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 14-20-1 | 41.2 | 7.7 | 147.3 |
| follow_move+pin_value | close | 1h\|spread | 12-8 | 60.0 | 9.4 | 12.3 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -46.9 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 18-17 | 51.4 | 1.5 | -3.3 |
| fd_juice+pin_value | close | 1h\|total | 0-1 | 0.0 | -49.5 | -100.0 |
| pin_value | early | 1h | 114-103 | 52.5 | 2.5 | -2.0 |
| pin_value | early | 1h\|spread | 52-45 | 53.6 | 3.8 | -0.1 |
| pin_value | early | 1h\|total | 62-58 | 51.7 | 1.5 | -3.5 |
| pin_price | early | 1h | 15-42-2 | 26.3 | -7.7 | 12.9 |
| pin_price | early | 1h\|ml | 14-41-2 | 25.5 | -8.1 | 13.4 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 53.1 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.5 | -100.0 |
| follow_move | early | 1h | 162-117-6 | 58.1 | 7.5 | 12.3 |
| follow_move | early | 1h\|ml | 73-49-6 | 59.8 | 8.2 | 17.0 |
| follow_move | early | 1h\|spread | 47-24 | 66.2 | 16.5 | 27.5 |
| follow_move | early | 1h\|total | 42-44 | 48.8 | -1.0 | -7.3 |
| follow_move | early | 2h | 95-81 | 54.0 | 4.1 | 4.3 |
| follow_move | early | 2h OT game | 5-4 | 55.6 | 5.3 | 6.1 |
| follow_move | early | 2h no OT | 90-77 | 53.9 | 4.0 | 4.2 |
| follow_move | early | 2h\|spread | 28-20 | 58.3 | 8.7 | 12.2 |
| follow_move | early | 2h\|tt_away | 32-28 | 53.3 | 3.4 | 3.3 |
| follow_move | early | 2h\|tt_home | 35-33 | 51.5 | 1.4 | -0.3 |
| fd_juice | early | 1h | 3-3 | 50.0 | 0.9 | -7.9 |
| fd_juice | early | 1h\|spread | 2-2 | 50.0 | 1.6 | -7.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.5 | -8.4 |
| fd_juice | early | 2h | 31-54 | 36.5 | -13.6 | -33.5 |
| fd_juice | early | 2h no OT | 31-54 | 36.5 | -13.6 | -33.5 |
| fd_juice | early | 2h\|spread | 1-4 | 20.0 | -31.9 | -63.1 |
| fd_juice | early | 2h\|tt_away | 15-24 | 38.5 | -11.3 | -30.4 |
| fd_juice | early | 2h\|tt_home | 15-26 | 36.6 | -13.6 | -32.9 |
| follow_move+pin_value | early | 1h | 3-4 | 42.9 | -7.6 | -18.4 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 66.5 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 66.5 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 15.6 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-3 | 25.0 | -25.0 | -52.9 |
