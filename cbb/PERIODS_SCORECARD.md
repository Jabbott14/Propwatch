# CBB period scorecard — halves and half team totals

Generated 2026-11-27 12:53 UTC. 2133 graded period markets (206 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 1014 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 46.8% (n=616)
- **total**: default side won 50.9% (n=422)
- **ml**: default side won 65.8% (n=371)
- **tt_home**: default side won 49.7% (n=356)
- **tt_away**: default side won 51.3% (n=351)
- **2h_tt_ot**: default side won 83.3% (n=36)
- **2h_tt_no_ot**: default side won 48.7% (n=671)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 47-44 | 51.6 | 50.7 | 1.0 | -3.5 | -3.8 | 0.16 | no edge shown yet |
| pin_price | 5-16-2 | 23.8 | 41.2 | -17.4 | -10.52 | -45.7 | 0.91 | keep collecting (21/50) |
| follow_move | 125-84-3 | 59.8 | 49.6 | 10.2 | +45.42 | 21.4 | -0.07 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 18-29 | 38.3 | 50.6 | -12.3 | -14.01 | -29.8 | 0.51 | keep collecting (47/50) |
| follow_move+pin_value | 0-1 | 0.0 | 51.3 | -51.3 | -1.0 | -100.0 | 1.0 | keep collecting (1/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 107-96 | 52.7 | 50.1 | 2.6 | -3.59 | -1.8 |  | no edge shown yet |
| pin_price | 15-28-2 | 34.9 | 41.6 | -6.8 | +21.27 | 47.3 |  | keep collecting (43/50) |
| follow_move | 388-380-9 | 50.5 | 49.7 | 0.8 | +10.59 | 1.4 |  | no edge shown yet |
| fd_juice | 58-61 | 48.7 | 50.6 | -1.8 | -12.81 | -10.8 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 46.8 | -46.8 | -2.0 | -100.0 |  | keep collecting (2/50) |
| follow_move+pin_price | 7-9 | 43.8 | 41.0 | 2.7 | +23.86 | 149.1 |  | keep collecting (16/50) |
| follow_move+pin_value | 17-12 | 58.6 | 50.6 | 8.0 | +2.77 | 9.6 |  | keep collecting (29/50) |

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
| follow_move | 260-200-6 | 56.5 | 50.2 | 6.3 | +43.36 | 9.3 | -0.06 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 35-58 | 37.6 | 50.0 | -12.3 | -29.08 | -31.3 | 0.33 | DROP: below break-even |
| follow_move+pin_value | 3-4 | 42.9 | 50.5 | -7.6 | -1.29 | -18.4 | 0.29 | keep collecting (7/50) |
| follow_move+pin_price | 2-0 | 100.0 | 34.2 | 65.8 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 250-205 | 54.9 | 49.9 | 5.1 | +11.59 | 2.5 |  | no edge shown yet |
| pin_price | 29-74-3 | 28.2 | 35.0 | -6.9 | +39.01 | 36.8 |  | DROP: below break-even |
| follow_move | 769-814-15 | 48.6 | 49.5 | -0.9 | -37.43 | -2.3 |  | DROP: below break-even |
| fd_juice | 117-136 | 46.2 | 50.2 | -4.0 | -38.96 | -15.4 |  | DROP: below break-even |
| follow_move+pin_price | 14-20-1 | 41.2 | 34.2 | 6.9 | +51.56 | 147.3 |  | keep collecting (34/50) |
| follow_move+pin_value | 30-25 | 54.5 | 50.1 | 4.4 | +1.29 | 2.3 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 47.9 | -47.9 | -2.0 | -100.0 |  | keep collecting (2/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 250-205 | 54.9 | 5.1 | 2.5 |
| pin_value | close | 1h\|spread | 113-102 | 52.6 | 3.1 | -2.1 |
| pin_value | close | 1h\|total | 137-103 | 57.1 | 6.9 | 6.7 |
| pin_price | close | 1h | 29-74-3 | 28.2 | -6.9 | 36.8 |
| pin_price | close | 1h\|ml | 28-71-3 | 28.3 | -6.3 | 40.2 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -13.4 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.1 | -100.0 |
| follow_move | close | 1h | 448-409-15 | 52.3 | 3.3 | 8.3 |
| follow_move | close | 1h\|ml | 168-162-15 | 50.9 | 3.7 | 19.1 |
| follow_move | close | 1h\|spread | 128-98 | 56.6 | 6.2 | 8.7 |
| follow_move | close | 1h\|total | 152-149 | 50.5 | 0.7 | -4.3 |
| follow_move | close | 2h | 321-405 | 44.2 | -5.8 | -15.1 |
| follow_move | close | 2h OT game | 14-16 | 46.7 | -3.3 | -10.3 |
| follow_move | close | 2h no OT | 307-389 | 44.1 | -5.9 | -15.3 |
| follow_move | close | 2h\|spread | 101-121 | 45.5 | -4.7 | -12.5 |
| follow_move | close | 2h\|tt_away | 109-144 | 43.1 | -6.8 | -17.6 |
| follow_move | close | 2h\|tt_home | 111-140 | 44.2 | -5.8 | -15.0 |
| fd_juice | close | 1h | 11-13 | 45.8 | -5.0 | -15.7 |
| fd_juice | close | 1h\|spread | 10-11 | 47.6 | -3.5 | -12.4 |
| fd_juice | close | 1h\|total | 1-2 | 33.3 | -15.7 | -38.9 |
| fd_juice | close | 2h | 106-123 | 46.3 | -3.9 | -15.4 |
| fd_juice | close | 2h OT game | 5-6 | 45.5 | -4.4 | -16.2 |
| fd_juice | close | 2h no OT | 101-117 | 46.3 | -3.8 | -15.3 |
| fd_juice | close | 2h\|spread | 13-13 | 50.0 | -0.2 | -7.7 |
| fd_juice | close | 2h\|tt_away | 51-47 | 52.0 | 1.9 | -5.2 |
| fd_juice | close | 2h\|tt_home | 42-63 | 40.0 | -10.1 | -26.7 |
| follow_move+pin_price | close | 1h | 14-20-1 | 41.2 | 6.9 | 147.3 |
| follow_move+pin_value | close | 1h | 30-25 | 54.5 | 4.4 | 2.3 |
| fd_juice+pin_value | close | 1h | 0-2 | 0.0 | -47.9 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 14-20-1 | 41.2 | 6.9 | 147.3 |
| follow_move+pin_value | close | 1h\|spread | 12-8 | 60.0 | 9.4 | 12.3 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -46.8 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 18-17 | 51.4 | 1.6 | -3.3 |
| fd_juice+pin_value | close | 1h\|total | 0-1 | 0.0 | -49.1 | -100.0 |
| pin_value | early | 1h | 116-105 | 52.5 | 2.4 | -2.1 |
| pin_value | early | 1h\|spread | 53-47 | 53.0 | 3.3 | -1.3 |
| pin_value | early | 1h\|total | 63-58 | 52.1 | 1.7 | -2.8 |
| pin_price | early | 1h | 15-43-2 | 25.9 | -8.8 | 11.1 |
| pin_price | early | 1h\|ml | 14-42-2 | 25.0 | -9.2 | 11.5 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 53.2 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.1 | -100.0 |
| follow_move | early | 1h | 163-118-6 | 58.0 | 7.5 | 12.1 |
| follow_move | early | 1h\|ml | 73-49-6 | 59.8 | 8.3 | 17.0 |
| follow_move | early | 1h\|spread | 47-24 | 66.2 | 16.5 | 27.5 |
| follow_move | early | 1h\|total | 43-45 | 48.9 | -0.9 | -7.3 |
| follow_move | early | 2h | 97-82 | 54.2 | 4.4 | 4.8 |
| follow_move | early | 2h OT game | 6-4 | 60.0 | 9.7 | 15.3 |
| follow_move | early | 2h no OT | 91-78 | 53.8 | 4.0 | 4.1 |
| follow_move | early | 2h\|spread | 28-21 | 57.1 | 7.6 | 9.9 |
| follow_move | early | 2h\|tt_away | 33-28 | 54.1 | 4.2 | 4.8 |
| follow_move | early | 2h\|tt_home | 36-33 | 52.2 | 2.2 | 1.1 |
| fd_juice | early | 1h | 3-3 | 50.0 | 0.8 | -7.9 |
| fd_juice | early | 1h\|spread | 2-2 | 50.0 | 1.6 | -7.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.9 | -8.4 |
| fd_juice | early | 2h | 32-55 | 36.8 | -13.2 | -32.9 |
| fd_juice | early | 2h OT game | 1-0 | 100.0 | 48.7 | 88.5 |
| fd_juice | early | 2h no OT | 31-55 | 36.0 | -14.0 | -34.3 |
| fd_juice | early | 2h\|spread | 1-4 | 20.0 | -31.9 | -63.1 |
| fd_juice | early | 2h\|tt_away | 16-25 | 39.0 | -10.7 | -29.2 |
| fd_juice | early | 2h\|tt_home | 15-26 | 36.6 | -13.5 | -32.9 |
| follow_move+pin_value | early | 1h | 3-4 | 42.9 | -7.6 | -18.4 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 65.8 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 65.8 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 15.6 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-3 | 25.0 | -25.0 | -52.9 |
