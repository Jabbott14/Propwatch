# CBB period scorecard — halves and half team totals

Generated 2026-11-26 03:41 UTC. 2038 graded period markets (266 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 919 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 47.1% (n=584)
- **total**: default side won 50.6% (n=403)
- **ml**: default side won 66.9% (n=356)
- **tt_home**: default side won 49.4% (n=340)
- **tt_away**: default side won 51.2% (n=338)
- **2h_tt_ot**: default side won 82.4% (n=34)
- **2h_tt_no_ot**: default side won 48.6% (n=644)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 37-37 | 50.0 | 50.3 | -0.3 | -4.95 | -6.7 | 0.19 | no edge shown yet |
| pin_price | 4-15-2 | 21.1 | 39.6 | -18.5 | -10.74 | -51.1 | 0.74 | keep collecting (19/50) |
| follow_move | 119-78-3 | 60.4 | 49.6 | 10.8 | +45.79 | 22.9 | -0.05 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 13-28 | 31.7 | 50.8 | -19.1 | -17.19 | -41.9 | 0.49 | keep collecting (41/50) |
| follow_move+pin_value | 0-1 | 0.0 | 50.6 | -50.6 | -1.0 | -100.0 | 1.0 | keep collecting (1/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 88-86 | 50.6 | 49.8 | 0.7 | -9.76 | -5.6 |  | no edge shown yet |
| pin_price | 13-24-2 | 35.1 | 39.6 | -4.4 | +22.53 | 57.8 |  | keep collecting (37/50) |
| follow_move | 362-349-9 | 50.9 | 49.7 | 1.2 | +16.81 | 2.3 |  | no edge shown yet |
| fd_juice | 54-55 | 49.5 | 50.7 | -1.2 | -10.14 | -9.3 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 47.4 | -47.4 | -2.0 | -100.0 |  | keep collecting (2/50) |
| follow_move+pin_price | 7-9 | 43.8 | 39.2 | 4.5 | +23.86 | 149.1 |  | keep collecting (16/50) |
| follow_move+pin_value | 17-11 | 60.7 | 50.7 | 10.0 | +3.77 | 13.5 |  | keep collecting (28/50) |

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
| pin_value | 106-98 | 52.0 | 49.9 | 2.0 | -6.09 | -3.0 | 0.21 | no edge shown yet |
| pin_price | 14-42-2 | 25.0 | 33.7 | -8.7 | +6.42 | 11.1 | 0.64 | DROP: below break-even |
| follow_move | 254-194-6 | 56.7 | 50.3 | 6.4 | +43.74 | 9.6 | -0.05 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 30-57 | 34.5 | 50.0 | -15.5 | -32.26 | -37.1 | 0.31 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-4 | 42.9 | 50.4 | -7.6 | -1.29 | -18.4 | 0.29 | keep collecting (7/50) |
| follow_move+pin_price | 2-0 | 100.0 | 33.1 | 66.9 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 231-195 | 54.2 | 49.8 | 4.4 | +5.41 | 1.3 |  | no edge shown yet |
| pin_price | 27-70-3 | 27.8 | 33.7 | -5.9 | +40.27 | 40.3 |  | DROP: below break-even |
| follow_move | 743-783-15 | 48.7 | 49.4 | -0.7 | -31.21 | -2.0 |  | DROP: below break-even |
| fd_juice | 113-130 | 46.5 | 50.3 | -3.8 | -36.29 | -14.9 |  | DROP: below break-even |
| follow_move+pin_price | 14-20-1 | 41.2 | 33.1 | 8.0 | +51.56 | 147.3 |  | keep collecting (34/50) |
| follow_move+pin_value | 30-24 | 55.6 | 50.1 | 5.4 | +2.29 | 4.2 |  | no edge shown yet |
| fd_juice+pin_value | 0-2 | 0.0 | 48.2 | -48.2 | -2.0 | -100.0 |  | keep collecting (2/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 231-195 | 54.2 | 4.4 | 1.3 |
| pin_value | close | 1h\|spread | 105-97 | 52.0 | 2.5 | -3.1 |
| pin_value | close | 1h\|total | 126-98 | 56.2 | 6.1 | 5.2 |
| pin_price | close | 1h | 27-70-3 | 27.8 | -5.9 | 40.3 |
| pin_price | close | 1h\|ml | 26-67-3 | 28.0 | -5.2 | 44.1 |
| pin_price | close | 1h\|spread | 1-2 | 33.3 | -13.8 | -34.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -49.4 | -100.0 |
| follow_move | close | 1h | 437-395-15 | 52.5 | 3.6 | 8.9 |
| follow_move | close | 1h\|ml | 162-158-15 | 50.6 | 3.6 | 19.0 |
| follow_move | close | 1h\|spread | 126-93 | 57.5 | 7.2 | 10.4 |
| follow_move | close | 1h\|total | 149-144 | 50.9 | 1.0 | -3.7 |
| follow_move | close | 2h | 306-388 | 44.1 | -6.0 | -15.4 |
| follow_move | close | 2h OT game | 13-16 | 44.8 | -5.1 | -14.1 |
| follow_move | close | 2h no OT | 293-372 | 44.1 | -6.0 | -15.5 |
| follow_move | close | 2h\|spread | 98-113 | 46.4 | -3.8 | -10.7 |
| follow_move | close | 2h\|tt_away | 104-140 | 42.6 | -7.3 | -18.4 |
| follow_move | close | 2h\|tt_home | 104-135 | 43.5 | -6.6 | -16.5 |
| fd_juice | close | 1h | 11-13 | 45.8 | -4.9 | -15.7 |
| fd_juice | close | 1h\|spread | 10-11 | 47.6 | -3.4 | -12.4 |
| fd_juice | close | 1h\|total | 1-2 | 33.3 | -16.0 | -38.9 |
| fd_juice | close | 2h | 102-117 | 46.6 | -3.6 | -14.8 |
| fd_juice | close | 2h OT game | 4-6 | 40.0 | -9.8 | -26.3 |
| fd_juice | close | 2h no OT | 98-111 | 46.9 | -3.3 | -14.3 |
| fd_juice | close | 2h\|spread | 13-11 | 54.2 | 3.9 | 0.0 |
| fd_juice | close | 2h\|tt_away | 48-46 | 51.1 | 0.9 | -7.1 |
| fd_juice | close | 2h\|tt_home | 41-60 | 40.6 | -9.6 | -25.6 |
| follow_move+pin_price | close | 1h | 14-20-1 | 41.2 | 8.0 | 147.3 |
| follow_move+pin_value | close | 1h | 30-24 | 55.6 | 5.4 | 4.2 |
| fd_juice+pin_value | close | 1h | 0-2 | 0.0 | -48.2 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 14-20-1 | 41.2 | 8.0 | 147.3 |
| follow_move+pin_value | close | 1h\|spread | 12-8 | 60.0 | 9.4 | 12.3 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -47.1 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 18-16 | 52.9 | 3.1 | -0.5 |
| fd_juice+pin_value | close | 1h\|total | 0-1 | 0.0 | -49.4 | -100.0 |
| pin_value | early | 1h | 106-98 | 52.0 | 2.0 | -3.0 |
| pin_value | early | 1h\|spread | 47-43 | 52.2 | 2.6 | -2.5 |
| pin_value | early | 1h\|total | 59-55 | 51.8 | 1.6 | -3.3 |
| pin_price | early | 1h | 14-42-2 | 25.0 | -8.7 | 11.1 |
| pin_price | early | 1h\|ml | 13-41-2 | 24.1 | -9.1 | 11.5 |
| pin_price | early | 1h\|spread | 1-0 | 100.0 | 52.9 | 98.0 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -49.4 | -100.0 |
| follow_move | early | 1h | 162-114-6 | 58.7 | 8.2 | 13.5 |
| follow_move | early | 1h\|ml | 73-48-6 | 60.3 | 8.8 | 17.9 |
| follow_move | early | 1h\|spread | 47-23 | 67.1 | 17.5 | 29.3 |
| follow_move | early | 1h\|total | 42-43 | 49.4 | -0.4 | -6.2 |
| follow_move | early | 2h | 92-80 | 53.5 | 3.6 | 3.4 |
| follow_move | early | 2h OT game | 5-4 | 55.6 | 5.3 | 6.1 |
| follow_move | early | 2h no OT | 87-76 | 53.4 | 3.5 | 3.2 |
| follow_move | early | 2h\|spread | 27-20 | 57.4 | 7.9 | 10.5 |
| follow_move | early | 2h\|tt_away | 31-27 | 53.4 | 3.6 | 3.4 |
| follow_move | early | 2h\|tt_home | 34-33 | 50.7 | 0.7 | -1.7 |
| fd_juice | early | 1h | 3-3 | 50.0 | 0.8 | -7.9 |
| fd_juice | early | 1h\|spread | 2-2 | 50.0 | 1.5 | -7.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | -0.6 | -8.4 |
| fd_juice | early | 2h | 27-54 | 33.3 | -16.7 | -39.2 |
| fd_juice | early | 2h no OT | 27-54 | 33.3 | -16.7 | -39.2 |
| fd_juice | early | 2h\|spread | 1-4 | 20.0 | -31.7 | -63.1 |
| fd_juice | early | 2h\|tt_away | 14-24 | 36.8 | -12.9 | -33.5 |
| fd_juice | early | 2h\|tt_home | 12-26 | 31.6 | -18.6 | -41.9 |
| follow_move+pin_value | early | 1h | 3-4 | 42.9 | -7.6 | -18.4 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 66.9 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 66.9 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 15.7 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-3 | 25.0 | -25.0 | -52.9 |
