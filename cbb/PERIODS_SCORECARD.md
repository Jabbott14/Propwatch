# CBB period scorecard — halves and half team totals

Generated 2026-11-28 17:41 UTC. 2230 graded period markets (218 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 1111 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 47.3% (n=641)
- **total**: default side won 50.3% (n=443)
- **ml**: default side won 65.8% (n=389)
- **tt_home**: default side won 49.6% (n=373)
- **tt_away**: default side won 51.2% (n=367)
- **2h_tt_ot**: default side won 83.3% (n=36)
- **2h_tt_no_ot**: default side won 48.7% (n=704)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 53-48 | 52.5 | 50.4 | 2.1 | -2.29 | -2.3 | 0.14 | no edge shown yet |
| pin_price | 5-18-2 | 21.7 | 40.6 | -18.8 | -12.52 | -50.1 | 0.82 | keep collecting (23/50) |
| follow_move | 127-85-3 | 59.9 | 49.7 | 10.2 | +46.32 | 21.5 | -0.06 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 18-30 | 37.5 | 50.7 | -13.2 | -15.01 | -31.3 | 0.52 | keep collecting (48/50) |
| follow_move+pin_value | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | 1.0 | keep collecting (1/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 122-106 | 53.5 | 49.9 | 3.6 | -0.51 | -0.2 |  | no edge shown yet |
| pin_price | 15-32-2 | 31.9 | 41.0 | -9.1 | +17.27 | 35.2 |  | keep collecting (47/50) |
| follow_move | 424-424-9 | 50.0 | 49.7 | 0.3 | -0.27 | -0.0 |  | no edge shown yet |
| fd_juice | 61-63 | 49.2 | 50.5 | -1.3 | -12.41 | -10.0 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 48.1 | -48.1 | -2.0 | -100.0 |  | keep collecting (2/50) |
| follow_move+pin_price | 7-11 | 38.9 | 40.3 | -1.4 | +21.86 | 121.4 |  | keep collecting (18/50) |
| follow_move+pin_value | 19-13 | 59.4 | 50.5 | 8.9 | +3.47 | 10.8 |  | keep collecting (32/50) |

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
| pin_value | 122-109 | 52.8 | 50.0 | 2.8 | -3.43 | -1.5 | 0.18 | no edge shown yet |
| pin_price | 15-45-2 | 25.0 | 34.7 | -9.7 | +4.64 | 7.5 | 0.68 | DROP: below break-even |
| follow_move | 262-201-6 | 56.6 | 50.3 | 6.3 | +44.27 | 9.4 | -0.05 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 35-59 | 37.2 | 50.0 | -12.8 | -30.08 | -32.0 | 0.34 | DROP: below break-even |
| follow_move+pin_value | 3-4 | 42.9 | 50.4 | -7.5 | -1.29 | -18.4 | 0.29 | keep collecting (7/50) |
| follow_move+pin_price | 2-0 | 100.0 | 34.2 | 65.8 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 265-215 | 55.2 | 49.8 | 5.4 | +14.66 | 3.1 |  | no edge shown yet |
| pin_price | 29-78-3 | 27.1 | 35.0 | -7.9 | +35.01 | 31.8 |  | DROP: below break-even |
| follow_move | 805-858-15 | 48.4 | 49.5 | -1.1 | -48.29 | -2.9 |  | DROP: below break-even |
| fd_juice | 120-138 | 46.5 | 50.2 | -3.7 | -38.56 | -14.9 |  | DROP: below break-even |
| follow_move+pin_price | 14-22-1 | 38.9 | 34.2 | 4.7 | +49.56 | 133.9 |  | keep collecting (36/50) |
| follow_move+pin_value | 32-26 | 55.2 | 50.1 | 5.1 | +1.98 | 3.4 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 48.5 | -48.5 | -2.0 | -100.0 |  | keep collecting (2/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 265-215 | 55.2 | 5.4 | 3.1 |
| pin_value | close | 1h\|spread | 118-107 | 52.4 | 2.9 | -2.4 |
| pin_value | close | 1h\|total | 147-108 | 57.6 | 7.6 | 7.8 |
| pin_price | close | 1h | 29-78-3 | 27.1 | -7.9 | 31.8 |
| pin_price | close | 1h\|ml | 28-75-3 | 27.2 | -7.3 | 34.9 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -13.9 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.7 | -100.0 |
| follow_move | close | 1h | 469-431-15 | 52.1 | 3.1 | 7.7 |
| follow_move | close | 1h\|ml | 176-171-15 | 50.7 | 3.4 | 17.9 |
| follow_move | close | 1h\|spread | 134-102 | 56.8 | 6.4 | 9.0 |
| follow_move | close | 1h\|total | 159-158 | 50.2 | 0.2 | -5.0 |
| follow_move | close | 2h | 336-427 | 44.0 | -6.0 | -15.5 |
| follow_move | close | 2h OT game | 14-16 | 46.7 | -3.3 | -10.3 |
| follow_move | close | 2h no OT | 322-411 | 43.9 | -6.1 | -15.7 |
| follow_move | close | 2h\|spread | 106-125 | 45.9 | -4.2 | -11.8 |
| follow_move | close | 2h\|tt_away | 113-155 | 42.2 | -7.7 | -19.3 |
| follow_move | close | 2h\|tt_home | 117-147 | 44.3 | -5.7 | -14.9 |
| fd_juice | close | 1h | 11-13 | 45.8 | -4.9 | -15.7 |
| fd_juice | close | 1h\|spread | 10-11 | 47.6 | -3.3 | -12.4 |
| fd_juice | close | 1h\|total | 1-2 | 33.3 | -16.3 | -38.9 |
| fd_juice | close | 2h | 109-125 | 46.6 | -3.6 | -14.9 |
| fd_juice | close | 2h OT game | 5-6 | 45.5 | -4.4 | -16.2 |
| fd_juice | close | 2h no OT | 104-119 | 46.6 | -3.5 | -14.8 |
| fd_juice | close | 2h\|spread | 13-13 | 50.0 | -0.2 | -7.7 |
| fd_juice | close | 2h\|tt_away | 52-47 | 52.5 | 2.4 | -4.4 |
| fd_juice | close | 2h\|tt_home | 44-65 | 40.4 | -9.8 | -26.1 |
| follow_move+pin_price | close | 1h | 14-22-1 | 38.9 | 4.7 | 133.9 |
| follow_move+pin_value | close | 1h | 32-26 | 55.2 | 5.1 | 3.4 |
| fd_juice+pin_value | close | 1h | 0-2 | 0.0 | -48.5 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 14-22-1 | 38.9 | 4.7 | 133.9 |
| follow_move+pin_value | close | 1h\|spread | 13-8 | 61.9 | 11.5 | 15.7 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -47.3 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 19-18 | 51.4 | 1.4 | -3.5 |
| fd_juice+pin_value | close | 1h\|total | 0-1 | 0.0 | -49.7 | -100.0 |
| pin_value | early | 1h | 122-109 | 52.8 | 2.8 | -1.5 |
| pin_value | early | 1h\|spread | 56-49 | 53.3 | 3.5 | -0.6 |
| pin_value | early | 1h\|total | 66-60 | 52.4 | 2.3 | -2.2 |
| pin_price | early | 1h | 15-45-2 | 25.0 | -9.7 | 7.5 |
| pin_price | early | 1h\|ml | 14-44-2 | 24.1 | -10.1 | 7.8 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 52.7 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.7 | -100.0 |
| follow_move | early | 1h | 164-119-6 | 58.0 | 7.4 | 12.0 |
| follow_move | early | 1h\|ml | 73-50-6 | 59.3 | 7.9 | 16.1 |
| follow_move | early | 1h\|spread | 48-24 | 66.7 | 16.9 | 28.4 |
| follow_move | early | 1h\|total | 43-45 | 48.9 | -1.0 | -7.3 |
| follow_move | early | 2h | 98-82 | 54.4 | 4.6 | 5.3 |
| follow_move | early | 2h OT game | 6-4 | 60.0 | 9.8 | 15.3 |
| follow_move | early | 2h no OT | 92-78 | 54.1 | 4.3 | 4.7 |
| follow_move | early | 2h\|spread | 29-21 | 58.0 | 8.4 | 11.6 |
| follow_move | early | 2h\|tt_away | 33-28 | 54.1 | 4.2 | 4.8 |
| follow_move | early | 2h\|tt_home | 36-33 | 52.2 | 2.1 | 1.1 |
| fd_juice | early | 1h | 3-3 | 50.0 | 0.8 | -7.9 |
| fd_juice | early | 1h\|spread | 2-2 | 50.0 | 1.4 | -7.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.3 | -8.4 |
| fd_juice | early | 2h | 32-56 | 36.4 | -13.7 | -33.6 |
| fd_juice | early | 2h OT game | 1-0 | 100.0 | 48.8 | 88.5 |
| fd_juice | early | 2h no OT | 31-56 | 35.6 | -14.4 | -35.0 |
| fd_juice | early | 2h\|spread | 1-4 | 20.0 | -31.6 | -63.1 |
| fd_juice | early | 2h\|tt_away | 16-26 | 38.1 | -11.7 | -30.9 |
| fd_juice | early | 2h\|tt_home | 15-26 | 36.6 | -13.5 | -32.9 |
| follow_move+pin_value | early | 1h | 3-4 | 42.9 | -7.5 | -18.4 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 65.8 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 65.8 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 15.8 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-3 | 25.0 | -25.0 | -52.9 |
