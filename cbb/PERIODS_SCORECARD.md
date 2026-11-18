# CBB period scorecard — halves and half team totals

Generated 2026-11-18 12:00 UTC. 1321 graded period markets (120 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 202 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 48.0% (n=383)
- **total**: default side won 49.2% (n=264)
- **ml**: default side won 70.5% (n=234)
- **tt_home**: default side won 52.8% (n=214)
- **tt_away**: default side won 52.1% (n=219)
- **2h_tt_ot**: default side won 92.3% (n=13)
- **2h_tt_no_ot**: default side won 51.2% (n=420)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 2-0 | 100.0 | 56.3 | 43.7 | +1.84 | 92.2 | -0.5 | keep collecting (2/50) |
| pin_price | 0-1 | 0.0 | 36.1 | -36.1 | -1.0 | -100.0 | -0.5 | keep collecting (1/50) |
| follow_move | 17-16-1 | 51.5 | 48.6 | 2.9 | +1.75 | 5.1 | -0.13 | keep collecting (33/50) |
| fd_juice | 2-9 | 18.2 | 44.6 | -26.4 | -7.44 | -67.6 | 0.55 | keep collecting (11/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 17-22 | 43.6 | 49.8 | -6.2 | -7.14 | -18.3 |  | keep collecting (39/50) |
| pin_price | 5-3 | 62.5 | 36.1 | 26.4 | +15.33 | 191.6 |  | keep collecting (8/50) |
| follow_move | 73-89-1 | 45.1 | 48.0 | -3.0 | -5.85 | -3.6 |  | DROP: below break-even |
| fd_juice | 11-16 | 40.7 | 51.4 | -10.7 | -6.82 | -25.3 |  | keep collecting (27/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 46.0 | -46.0 | -1.0 | -100.0 |  | keep collecting (1/50) |
| follow_move+pin_price | 3-1 | 75.0 | 36.1 | 38.9 | +11.98 | 299.5 |  | keep collecting (4/50) |
| follow_move+pin_value | 5-2 | 71.4 | 56.1 | 15.3 | +2.35 | 33.5 |  | keep collecting (7/50) |

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
| pin_value | 71-61 | 53.8 | 49.7 | 4.1 | +0.7 | 0.5 | 0.2 | no edge shown yet |
| pin_price | 10-28 | 26.3 | 30.0 | -3.7 | +16.16 | 42.5 | 0.56 | keep collecting (38/50) |
| follow_move | 152-132-4 | 53.5 | 51.0 | 2.5 | -0.31 | -0.1 | -0.05 | no edge shown yet |
| fd_juice | 19-38 | 33.3 | 49.6 | -16.2 | -22.51 | -39.5 | 0.23 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-3 | 50.0 | 50.5 | -0.5 | -0.29 | -4.9 | 0.17 | keep collecting (6/50) |
| follow_move+pin_price | 2-0 | 100.0 | 29.5 | 70.5 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 160-131 | 55.0 | 49.7 | 5.3 | +8.03 | 2.8 |  | no edge shown yet |
| pin_price | 19-49-1 | 27.9 | 30.1 | -2.1 | +33.07 | 47.9 |  | DROP: below break-even |
| follow_move | 454-523-7 | 46.5 | 49.1 | -2.6 | -53.87 | -5.5 |  | DROP: below break-even |
| fd_juice | 70-91 | 43.5 | 49.7 | -6.2 | -32.97 | -20.5 |  | DROP: below break-even |
| follow_move+pin_price | 10-12-1 | 45.5 | 29.5 | 16.0 | +39.68 | 172.5 |  | keep collecting (22/50) |
| follow_move+pin_value | 18-15 | 54.5 | 50.1 | 4.5 | +0.86 | 2.6 |  | keep collecting (33/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 48.0 | -48.0 | -1.0 | -100.0 |  | keep collecting (1/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 160-131 | 55.0 | 5.3 | 2.8 |
| pin_value | close | 1h\|spread | 73-67 | 52.1 | 2.6 | -2.6 |
| pin_value | close | 1h\|total | 87-64 | 57.6 | 7.7 | 7.8 |
| pin_price | close | 1h | 19-49-1 | 27.9 | -2.1 | 47.9 |
| pin_price | close | 1h\|ml | 19-47-1 | 28.8 | -0.7 | 52.3 |
| pin_price | close | 1h\|spread | 0-1 | 0.0 | -48.0 | -100.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -50.8 | -100.0 |
| follow_move | close | 1h | 263-265-7 | 49.8 | 1.2 | 5.4 |
| follow_move | close | 1h\|ml | 97-111-7 | 46.6 | 0.4 | 15.2 |
| follow_move | close | 1h\|spread | 77-61 | 55.8 | 5.5 | 6.8 |
| follow_move | close | 1h\|total | 89-93 | 48.9 | -1.2 | -7.3 |
| follow_move | close | 2h | 191-258 | 42.5 | -7.1 | -18.4 |
| follow_move | close | 2h OT game | 2-6 | 25.0 | -23.8 | -51.0 |
| follow_move | close | 2h no OT | 189-252 | 42.9 | -6.8 | -17.8 |
| follow_move | close | 2h\|spread | 62-80 | 43.7 | -6.4 | -16.1 |
| follow_move | close | 2h\|tt_away | 65-91 | 41.7 | -7.9 | -20.3 |
| follow_move | close | 2h\|tt_home | 64-87 | 42.4 | -7.0 | -18.7 |
| fd_juice | close | 1h | 7-11 | 38.9 | -11.6 | -28.5 |
| fd_juice | close | 1h\|spread | 6-10 | 37.5 | -13.0 | -31.0 |
| fd_juice | close | 1h\|total | 1-1 | 50.0 | -0.8 | -8.4 |
| fd_juice | close | 2h | 63-80 | 44.1 | -5.5 | -19.5 |
| fd_juice | close | 2h OT game | 1-4 | 20.0 | -29.4 | -63.1 |
| fd_juice | close | 2h no OT | 62-76 | 44.9 | -4.7 | -17.9 |
| fd_juice | close | 2h\|spread | 9-8 | 52.9 | 2.6 | -2.3 |
| fd_juice | close | 2h\|tt_away | 32-31 | 50.8 | 0.5 | -7.4 |
| fd_juice | close | 2h\|tt_home | 22-41 | 34.9 | -13.8 | -36.2 |
| follow_move+pin_price | close | 1h | 10-12-1 | 45.5 | 16.0 | 172.5 |
| follow_move+pin_value | close | 1h | 18-15 | 54.5 | 4.5 | 2.6 |
| fd_juice+pin_value | close | 1h | 0-1 | 0.0 | -48.0 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 10-12-1 | 45.5 | 16.0 | 172.5 |
| follow_move+pin_value | close | 1h\|spread | 8-5 | 61.5 | 11.7 | 15.4 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -48.0 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 10-10 | 50.0 | -0.2 | -5.7 |
| pin_value | early | 1h | 71-61 | 53.8 | 4.1 | 0.5 |
| pin_value | early | 1h\|spread | 34-26 | 56.7 | 7.1 | 6.0 |
| pin_value | early | 1h\|total | 37-35 | 51.4 | 1.6 | -4.0 |
| pin_price | early | 1h | 10-28 | 26.3 | -3.7 | 42.5 |
| pin_price | early | 1h\|ml | 10-27 | 27.0 | -2.5 | 46.4 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -50.8 | -100.0 |
| follow_move | early | 1h | 97-75-4 | 56.4 | 4.3 | 3.1 |
| follow_move | early | 1h\|ml | 43-39-4 | 52.4 | -2.1 | -8.6 |
| follow_move | early | 1h\|spread | 28-11 | 71.8 | 22.1 | 37.8 |
| follow_move | early | 1h\|total | 26-25 | 51.0 | 0.9 | -3.5 |
| follow_move | early | 2h | 55-57 | 49.1 | -0.3 | -5.2 |
| follow_move | early | 2h no OT | 55-57 | 49.1 | -0.3 | -5.2 |
| follow_move | early | 2h\|spread | 18-15 | 54.5 | 5.2 | 4.9 |
| follow_move | early | 2h\|tt_away | 16-22 | 42.1 | -7.2 | -18.4 |
| follow_move | early | 2h\|tt_home | 21-20 | 51.2 | 1.8 | -1.1 |
| fd_juice | early | 1h | 2-2 | 50.0 | 1.4 | -8.0 |
| fd_juice | early | 1h\|spread | 1-1 | 50.0 | 2.0 | -7.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | 0.8 | -8.4 |
| fd_juice | early | 2h | 17-36 | 32.1 | -17.6 | -41.9 |
| fd_juice | early | 2h no OT | 17-36 | 32.1 | -17.6 | -41.9 |
| fd_juice | early | 2h\|spread | 0-3 | 0.0 | -50.7 | -100.0 |
| fd_juice | early | 2h\|tt_away | 10-15 | 40.0 | -9.3 | -28.0 |
| fd_juice | early | 2h\|tt_home | 7-18 | 28.0 | -21.9 | -48.7 |
| follow_move+pin_value | early | 1h | 3-3 | 50.0 | -0.5 | -4.9 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 70.5 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 70.5 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 16.0 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-2 | 33.3 | -16.9 | -37.2 |
