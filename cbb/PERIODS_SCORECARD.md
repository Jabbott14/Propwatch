# CBB period scorecard — halves and half team totals

Generated 2026-11-18 20:46 UTC. 1325 graded period markets (120 had no unique final matched and are not graded).

## Read this first: fit vs forward

**1119 markets before 2026-11-17 (fit) · 206 on or after it (forward).** Every signal and threshold here was chosen by looking at the
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

- **spread**: default side won 48.1% (n=385)
- **total**: default side won 49.4% (n=265)
- **ml**: default side won 70.5% (n=234)
- **tt_home**: default side won 52.8% (n=214)
- **tt_away**: default side won 52.3% (n=220)
- **2h_tt_ot**: default side won 92.3% (n=13)
- **2h_tt_no_ot**: default side won 51.3% (n=421)

Proposals appear at 50 decided markets. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 2-0 | 100.0 | 55.5 | 44.5 | +1.84 | 92.2 | -0.5 | keep collecting (2/50) |
| pin_price | 0-1 | 0.0 | 36.1 | -36.1 | -1.0 | -100.0 | -0.5 | keep collecting (1/50) |
| follow_move | 18-18-1 | 50.0 | 48.4 | 1.6 | +0.62 | 1.7 | -0.09 | keep collecting (36/50) |
| fd_juice | 2-10 | 16.7 | 43.6 | -26.9 | -8.44 | -70.3 | 0.5 | keep collecting (12/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 17-22 | 43.6 | 49.8 | -6.2 | -7.14 | -18.3 |  | keep collecting (39/50) |
| pin_price | 5-3 | 62.5 | 36.1 | 26.4 | +15.33 | 191.6 |  | keep collecting (8/50) |
| follow_move | 74-91-1 | 44.8 | 47.8 | -3.0 | -7.02 | -4.2 |  | DROP: below break-even |
| fd_juice | 11-17 | 39.3 | 51.0 | -11.7 | -7.82 | -27.9 |  | keep collecting (28/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 46.2 | -46.2 | -1.0 | -100.0 |  | keep collecting (1/50) |
| follow_move+pin_price | 3-1 | 75.0 | 36.1 | 38.9 | +11.98 | 299.5 |  | keep collecting (4/50) |
| follow_move+pin_value | 5-2 | 71.4 | 55.1 | 16.3 | +2.35 | 33.5 |  | keep collecting (7/50) |

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
| follow_move | 153-134-4 | 53.3 | 51.0 | 2.3 | -1.44 | -0.5 | -0.05 | no edge shown yet |
| fd_juice | 19-39 | 32.8 | 49.5 | -16.7 | -23.51 | -40.5 | 0.22 | INVERT candidate: wrong well beyond its base rate |
| follow_move+pin_value | 3-3 | 50.0 | 50.4 | -0.4 | -0.29 | -4.9 | 0.17 | keep collecting (6/50) |
| follow_move+pin_price | 2-0 | 100.0 | 29.5 | 70.5 | +12.2 | 610.0 | 1.05 | keep collecting (2/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV avg | status |
|---|---|---|---|---|---|---|---|---|
| pin_value | 160-131 | 55.0 | 49.7 | 5.3 | +8.03 | 2.8 |  | no edge shown yet |
| pin_price | 19-49-1 | 27.9 | 30.1 | -2.1 | +33.07 | 47.9 |  | DROP: below break-even |
| follow_move | 455-525-7 | 46.4 | 49.1 | -2.7 | -55.04 | -5.6 |  | DROP: below break-even |
| fd_juice | 70-92 | 43.2 | 49.7 | -6.5 | -33.97 | -21.0 |  | DROP: below break-even |
| follow_move+pin_price | 10-12-1 | 45.5 | 29.5 | 16.0 | +39.68 | 172.5 |  | keep collecting (22/50) |
| follow_move+pin_value | 18-15 | 54.5 | 50.0 | 4.5 | +0.86 | 2.6 |  | keep collecting (33/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 48.1 | -48.1 | -1.0 | -100.0 |  | keep collecting (1/50) |

## By period and market (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | 1h | 160-131 | 55.0 | 5.3 | 2.8 |
| pin_value | close | 1h\|spread | 73-67 | 52.1 | 2.6 | -2.6 |
| pin_value | close | 1h\|total | 87-64 | 57.6 | 7.7 | 7.8 |
| pin_price | close | 1h | 19-49-1 | 27.9 | -2.1 | 47.9 |
| pin_price | close | 1h\|ml | 19-47-1 | 28.8 | -0.7 | 52.3 |
| pin_price | close | 1h\|spread | 0-1 | 0.0 | -48.1 | -100.0 |
| pin_price | close | 1h\|total | 0-1 | 0.0 | -50.6 | -100.0 |
| follow_move | close | 1h | 264-266-7 | 49.8 | 1.2 | 5.3 |
| follow_move | close | 1h\|ml | 97-111-7 | 46.6 | 0.4 | 15.2 |
| follow_move | close | 1h\|spread | 77-62 | 55.4 | 5.1 | 6.0 |
| follow_move | close | 1h\|total | 90-93 | 49.2 | -0.9 | -6.8 |
| follow_move | close | 2h | 191-259 | 42.4 | -7.2 | -18.6 |
| follow_move | close | 2h OT game | 2-6 | 25.0 | -23.7 | -51.0 |
| follow_move | close | 2h no OT | 189-253 | 42.8 | -6.9 | -18.0 |
| follow_move | close | 2h\|spread | 62-81 | 43.4 | -6.7 | -16.7 |
| follow_move | close | 2h\|tt_away | 65-91 | 41.7 | -7.8 | -20.3 |
| follow_move | close | 2h\|tt_home | 64-87 | 42.4 | -7.0 | -18.7 |
| fd_juice | close | 1h | 7-11 | 38.9 | -11.6 | -28.5 |
| fd_juice | close | 1h\|spread | 6-10 | 37.5 | -13.0 | -31.0 |
| fd_juice | close | 1h\|total | 1-1 | 50.0 | -0.6 | -8.4 |
| fd_juice | close | 2h | 63-81 | 43.8 | -5.9 | -20.0 |
| fd_juice | close | 2h OT game | 1-4 | 20.0 | -29.4 | -63.1 |
| fd_juice | close | 2h no OT | 62-77 | 44.6 | -5.0 | -18.5 |
| fd_juice | close | 2h\|spread | 9-8 | 52.9 | 2.6 | -2.3 |
| fd_juice | close | 2h\|tt_away | 32-32 | 50.0 | -0.3 | -8.8 |
| fd_juice | close | 2h\|tt_home | 22-41 | 34.9 | -13.8 | -36.2 |
| follow_move+pin_price | close | 1h | 10-12-1 | 45.5 | 16.0 | 172.5 |
| follow_move+pin_value | close | 1h | 18-15 | 54.5 | 4.5 | 2.6 |
| fd_juice+pin_value | close | 1h | 0-1 | 0.0 | -48.1 | -100.0 |
| follow_move+pin_price | close | 1h\|ml | 10-12-1 | 45.5 | 16.0 | 172.5 |
| follow_move+pin_value | close | 1h\|spread | 8-5 | 61.5 | 11.7 | 15.4 |
| fd_juice+pin_value | close | 1h\|spread | 0-1 | 0.0 | -48.1 | -100.0 |
| follow_move+pin_value | close | 1h\|total | 10-10 | 50.0 | -0.2 | -5.7 |
| pin_value | early | 1h | 71-61 | 53.8 | 4.1 | 0.5 |
| pin_value | early | 1h\|spread | 34-26 | 56.7 | 7.1 | 6.0 |
| pin_value | early | 1h\|total | 37-35 | 51.4 | 1.5 | -4.0 |
| pin_price | early | 1h | 10-28 | 26.3 | -3.7 | 42.5 |
| pin_price | early | 1h\|ml | 10-27 | 27.0 | -2.5 | 46.4 |
| pin_price | early | 1h\|total | 0-1 | 0.0 | -50.6 | -100.0 |
| follow_move | early | 1h | 98-76-4 | 56.3 | 4.2 | 3.0 |
| follow_move | early | 1h\|ml | 43-39-4 | 52.4 | -2.1 | -8.6 |
| follow_move | early | 1h\|spread | 28-12 | 70.0 | 20.3 | 34.3 |
| follow_move | early | 1h\|total | 27-25 | 51.9 | 1.9 | -1.7 |
| follow_move | early | 2h | 55-58 | 48.7 | -0.7 | -6.1 |
| follow_move | early | 2h no OT | 55-58 | 48.7 | -0.7 | -6.1 |
| follow_move | early | 2h\|spread | 18-16 | 52.9 | 3.6 | 1.8 |
| follow_move | early | 2h\|tt_away | 16-22 | 42.1 | -7.2 | -18.4 |
| follow_move | early | 2h\|tt_home | 21-20 | 51.2 | 1.8 | -1.1 |
| fd_juice | early | 1h | 2-2 | 50.0 | 1.3 | -8.0 |
| fd_juice | early | 1h\|spread | 1-1 | 50.0 | 1.9 | -7.7 |
| fd_juice | early | 1h\|total | 1-1 | 50.0 | 0.6 | -8.4 |
| fd_juice | early | 2h | 17-37 | 31.5 | -18.1 | -42.9 |
| fd_juice | early | 2h no OT | 17-37 | 31.5 | -18.1 | -42.9 |
| fd_juice | early | 2h\|spread | 0-3 | 0.0 | -50.6 | -100.0 |
| fd_juice | early | 2h\|tt_away | 10-16 | 38.5 | -10.7 | -30.8 |
| fd_juice | early | 2h\|tt_home | 7-18 | 28.0 | -21.9 | -48.7 |
| follow_move+pin_value | early | 1h | 3-3 | 50.0 | -0.4 | -4.9 |
| follow_move+pin_price | early | 1h | 2-0 | 100.0 | 70.5 | 610.0 |
| follow_move+pin_price | early | 1h\|ml | 2-0 | 100.0 | 70.5 | 610.0 |
| follow_move+pin_value | early | 1h\|spread | 2-1 | 66.7 | 16.0 | 27.5 |
| follow_move+pin_value | early | 1h\|total | 1-2 | 33.3 | -16.9 | -37.2 |
