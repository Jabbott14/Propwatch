# NFL prop scorecard

Generated 2026-11-23 01:59 UTC. 1238 graded props (231 had no nflverse result and are not graded).

## Read this first: fit vs forward

**890 props before 2026-11-17 (fit) · 348 on or after it (forward).**

Every signal and threshold here was chosen by looking at the props before
2026-11-17. `pin_lead` read 17-8 on Nov 15 and 22-22 a week later; the only
way to tell a signal from a streak is to score it on props it had no hand in
picking. So every record appears twice:

- **FIT** — in-sample. A label here is a **hypothesis**.
- **FORWARD** — out-of-sample. A label here is **evidence**.

The over base rate is measured separately in each period.

**Read this on its own scale, not against the side scorecard.** Pinnacle risks
**$75,000** on an NFL side and **$1,000-$3,000** on a prop at kickoff, $250-$500
earlier in the week. The sharpest book in the world is telling you it is 25-75x
less confident in its own prop number. A prop signal must never be sized like a
side signal, and `pin_value` barely fires here because FanDuel's prop handicaps
sit on Pinnacle's almost every time.

There are no tickets/money splits on any prop, so the only channels are the
handicap and the price. `fd_juice` is the money channel: a static handicap whose
price moves 12+ cents one way. Break-even at -110 is 52.4%.

**CLV pts** is handicap movement and is near-blank here, because most prop
numbers never move. **CLV price** is the real one: percentage points of implied
probability gained on the taken side between the early read and the close.

Base rate: the over hit **44.8%** of 1238 graded props, but `expected %`
uses **each stat's own rate**, not that pooled one. A yardage over is near a coin
flip; an anytime-TD over 0.5 is a longshot. Scored against one pooled number every
anytime-TD signal would be charged an expectation it could never meet:

- **recv_yds**: over hit 49.1% of 426
- **receptions**: over hit 43.2% of 338
- **rush_yds**: over hit 49.1% of 218
- **anytime_td**: over hit 22.9% of 118
- **pass_yds**: over hit 51.3% of 78
- **pass_tds**: over hit 43.3% of 60

Proposals appear at 50 decided props. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

Props for games kicking off on or after 2026-11-17. n=348, over rate 44.5% of 348.

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| fd_move | 20-8 | 71.4 | 50.0 | 21.4 | +10.18 | 36.3 | 0.82 | -0.02 | 7.1 | keep collecting (28/50) |
| fd_juice | 9-5 | 64.3 | 51.3 | 13.0 | +2.85 | 20.4 | 0.07 | 1.14 | 50.0 | keep collecting (14/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 36-32 | 52.9 | 49.9 | 3.1 | -0.32 | -0.5 |  |  |  | no edge shown yet |
| pin_price | 9-32 | 22.0 | 23.5 | -1.6 | -18.15 | -44.3 |  |  |  | keep collecting (41/50) |
| fd_move | 104-90 | 53.6 | 50.2 | 3.4 | +5.86 | 3.0 |  |  |  | no edge shown yet |
| fd_juice | 56-38 | 59.6 | 50.8 | 8.7 | +8.57 | 9.1 |  |  |  | no edge shown yet |
| pin_lead | 11-4 | 73.3 | 50.0 | 23.4 | +5.73 | 38.2 |  |  |  | keep collecting (15/50) |
| td_steam | 2-19 | 9.5 | 12.0 | -2.5 | -11.0 | -52.4 |  |  |  | keep collecting (21/50) |
| fd_move+pin_value | 6-6 | 50.0 | 50.0 | 0.0 | -0.69 | -5.8 |  |  |  | keep collecting (12/50) |
| pin_lead+pin_value | 3-3 | 50.0 | 49.8 | 0.2 | -0.34 | -5.8 |  |  |  | keep collecting (6/50) |
| fd_juice+pin_price | 2-1 | 66.7 | 53.1 | 13.6 | +0.71 | 23.6 |  |  |  | keep collecting (3/50) |
| fd_move+pin_price | 1-1 | 50.0 | 50.2 | -0.2 | -0.11 | -5.8 |  |  |  | keep collecting (2/50) |

# FIT (in-sample — this is the hypothesis)

Props before 2026-11-17, which the signals were chosen on. n=890, over rate 44.9% of 890.

## EARLY  (fit)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 17-12 | 58.6 | 50.1 | 8.5 | +2.8 | 9.7 | -0.55 | -0.03 | 0.0 | keep collecting (29/50) |
| pin_price | 6-3 | 66.7 | 41.4 | 25.3 | +6.09 | 67.7 | 0.0 | 0.49 | 44.4 | keep collecting (9/50) |
| fd_move | 17-7 | 70.8 | 49.9 | 21.0 | +7.84 | 32.7 | 3.29 | -0.18 | 0.0 | keep collecting (24/50) |
| fd_juice | 14-4 | 77.8 | 48.7 | 29.1 | +9.79 | 54.4 | -0.06 | 3.86 | 61.1 | keep collecting (18/50) |
| td_steam | 0-1 | 0.0 | 30.9 | -30.9 | -1.0 | -100.0 | 0.0 | 8.3 | 100.0 | keep collecting (1/50) |

## CLOSE  (fit)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 141-127 | 52.6 | 49.8 | 2.8 | -4.46 | -1.7 |  |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_price | 51-57 | 47.2 | 43.3 | 3.9 | +8.04 | 7.4 |  |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| fd_move | 240-231 | 51.0 | 50.2 | 0.8 | -13.98 | -3.0 |  |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| fd_juice | 128-102 | 55.7 | 52.0 | 3.7 | +5.08 | 2.2 |  |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_lead | 22-22 | 50.0 | 50.2 | -0.2 | -2.96 | -6.7 |  |  |  | keep collecting (44/50) |
| td_steam | 9-24 | 27.3 | 30.9 | -3.6 | -0.18 | -0.6 |  |  |  | keep collecting (33/50) |
| pin_lead+pin_value | 18-16 | 52.9 | 50.5 | 2.5 | -0.5 | -1.5 |  |  |  | keep collecting (34/50) |
| fd_juice+pin_price | 5-2 | 71.4 | 53.6 | 17.9 | +1.94 | 27.8 |  |  |  | keep collecting (7/50) |
| fd_move+pin_value | 24-17 | 58.5 | 49.6 | 8.9 | +4.24 | 10.3 |  |  |  | keep collecting (41/50) |
| fd_move+pin_price | 10-7 | 58.8 | 48.9 | 9.9 | +3.49 | 20.5 |  |  |  | keep collecting (17/50) |
| fd_juice+pin_lead | 0-1 | 0.0 | 62.2 | -62.2 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 62.2 | -62.2 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |

# Pooled (fit + forward together)

Kept for continuity. **Contaminated** — it mixes the props the signals were
chosen on with the props testing them.

## EARLY  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 17-12 | 58.6 | 50.2 | 8.4 | +2.8 | 9.7 | -0.55 | -0.03 | 0.0 | keep collecting (29/50) |
| pin_price | 6-3 | 66.7 | 37.8 | 28.8 | +6.09 | 67.7 | 0.0 | 0.49 | 44.4 | keep collecting (9/50) |
| fd_move | 37-15 | 71.2 | 49.7 | 21.5 | +18.02 | 34.6 | 1.96 | -0.1 | 3.8 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 23-9 | 71.9 | 50.7 | 21.2 | +12.64 | 39.5 | 0.0 | 2.67 | 56.2 | keep collecting (32/50) |
| td_steam | 0-1 | 0.0 | 22.9 | -22.9 | -1.0 | -100.0 | 0.0 | 8.3 | 100.0 | keep collecting (1/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 177-159 | 52.7 | 50.0 | 2.7 | -4.77 | -1.4 |  |  |  | no edge shown yet |
| pin_price | 60-89 | 40.3 | 38.2 | 2.1 | -10.11 | -6.8 |  |  |  | DROP: below break-even |
| fd_move | 344-321 | 51.7 | 50.0 | 1.7 | -8.12 | -1.2 |  |  |  | no edge shown yet |
| fd_juice | 184-140 | 56.8 | 51.7 | 5.1 | +13.65 | 4.2 |  |  |  | PROMOTE: beats break-even and its own base rate |
| pin_lead | 33-26 | 55.9 | 50.0 | 5.9 | +2.77 | 4.7 |  |  |  | no edge shown yet |
| td_steam | 11-43 | 20.4 | 22.9 | -2.5 | -11.18 | -20.7 |  |  |  | DROP: below break-even |
| pin_lead+pin_value | 21-19 | 52.5 | 50.2 | 2.3 | -0.85 | -2.1 |  |  |  | keep collecting (40/50) |
| fd_juice+pin_price | 7-3 | 70.0 | 54.1 | 15.9 | +2.65 | 26.5 |  |  |  | keep collecting (10/50) |
| fd_move+pin_value | 30-23 | 56.6 | 49.8 | 6.8 | +3.55 | 6.7 |  |  |  | no edge shown yet |
| fd_move+pin_price | 11-8 | 57.9 | 49.0 | 8.9 | +3.37 | 17.8 |  |  |  | keep collecting (19/50) |
| fd_juice+pin_lead | 0-1 | 0.0 | 56.7 | -56.7 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 56.7 | -56.7 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |

## By Pinnacle limit and by stat (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | pass_tds | 3-2 | 60.0 | 8.7 | -13.7 |
| pin_value | close | pass_yds | 17-16 | 51.5 | 1.0 | -2.9 |
| pin_value | close | pin $1k+ | 112-98 | 53.3 | 3.3 | -0.4 |
| pin_value | close | pin $400-1k | 60-53 | 53.1 | 3.2 | -0.3 |
| pin_value | close | pin limit <$400 | 5-8 | 38.5 | -11.2 | -27.9 |
| pin_value | close | receptions | 5-4 | 55.6 | 6.3 | -9.4 |
| pin_value | close | recv_yds | 101-89 | 53.2 | 3.2 | 0.2 |
| pin_value | close | rush_yds | 51-48 | 51.5 | 1.7 | -2.8 |
| pin_price | close | anytime_td | 16-48 | 25.0 | 2.1 | -19.1 |
| pin_price | close | pass_tds | 4-4 | 50.0 | -5.0 | 15.3 |
| pin_price | close | pass_yds | 3-4 | 42.9 | -7.3 | -19.2 |
| pin_price | close | pin $1k+ | 37-56 | 39.8 | 2.0 | -4.2 |
| pin_price | close | pin $400-1k | 21-30 | 41.2 | 2.0 | -10.8 |
| pin_price | close | pin limit <$400 | 2-3 | 40.0 | 3.8 | -13.8 |
| pin_price | close | receptions | 16-18 | 47.1 | -1.3 | -4.4 |
| pin_price | close | recv_yds | 12-11 | 52.2 | 2.8 | -1.7 |
| pin_price | close | rush_yds | 9-4 | 69.2 | 19.2 | 31.5 |
| fd_move | close | pass_tds | 1-4 | 20.0 | -34.0 | -47.6 |
| fd_move | close | pass_yds | 33-32 | 50.8 | 1.1 | -4.3 |
| fd_move | close | pin $1k+ | 175-166 | 51.3 | 1.3 | -2.1 |
| fd_move | close | pin $400-1k | 126-123 | 50.6 | 0.6 | -3.1 |
| fd_move | close | pin limit <$400 | 14-14 | 50.0 | 0.3 | -4.5 |
| fd_move | close | receptions | 29-30 | 49.2 | -1.2 | 6.3 |
| fd_move | close | recv_yds | 185-175 | 51.4 | 1.4 | -3.1 |
| fd_move | close | rush_yds | 96-80 | 54.5 | 4.5 | 2.6 |
| fd_juice | close | pass_tds | 26-22 | 54.2 | 4.2 | 8.9 |
| fd_juice | close | pin $1k+ | 95-69 | 57.9 | 6.1 | 5.5 |
| fd_juice | close | pin $400-1k | 73-59 | 55.3 | 4.2 | 1.9 |
| fd_juice | close | pin limit <$400 | 4-3 | 57.1 | 4.2 | -0.1 |
| fd_juice | close | receptions | 152-113 | 57.4 | 5.3 | 3.7 |
| fd_juice | close | recv_yds | 2-3 | 40.0 | -10.9 | -29.5 |
| fd_juice | close | rush_yds | 4-2 | 66.7 | 17.0 | 17.5 |
| pin_lead | close | pass_tds | 1-1 | 50.0 | -6.7 | -27.2 |
| pin_lead | close | pass_yds | 5-5 | 50.0 | 0.3 | -5.7 |
| pin_lead | close | pin $1k+ | 24-13 | 64.9 | 14.8 | 21.1 |
| pin_lead | close | pin $400-1k | 9-13 | 40.9 | -9.1 | -22.9 |
| pin_lead | close | recv_yds | 18-12 | 60.0 | 10.1 | 13.1 |
| pin_lead | close | rush_yds | 9-8 | 52.9 | 3.3 | -0.2 |
| td_steam | close | anytime_td | 11-43 | 20.4 | -2.5 | -20.7 |
| td_steam | close | pin $1k+ | 2-6 | 25.0 | 2.1 | -53.2 |
| td_steam | close | pin $400-1k | 1-1 | 50.0 | 27.1 | -27.2 |
| td_steam | close | pin limit <$400 | 1-1 | 50.0 | 27.1 | -33.4 |
| pin_lead+pin_value | close | pass_tds | 1-1 | 50.0 | -6.7 | -27.2 |
| fd_juice+pin_lead | close | pass_tds | 0-1 | 0.0 | -56.7 | -100.0 |
| fd_juice+pin_value | close | pass_tds | 0-1 | 0.0 | -56.7 | -100.0 |
| pin_lead+pin_value | close | pass_yds | 4-3 | 57.1 | 7.3 | 7.7 |
| fd_move+pin_price | close | pass_yds | 1-1 | 50.0 | 1.3 | -5.8 |
| fd_move+pin_value | close | pass_yds | 3-2 | 60.0 | 9.7 | 13.1 |
| pin_lead+pin_value | close | pin $1k+ | 15-10 | 60.0 | 9.8 | 11.4 |
| fd_juice+pin_price | close | pin $1k+ | 4-1 | 80.0 | 25.9 | 44.9 |
| fd_move+pin_value | close | pin $1k+ | 16-14 | 53.3 | 3.4 | 0.5 |
| fd_move+pin_price | close | pin $1k+ | 6-5 | 54.5 | 5.0 | 2.8 |
| pin_lead+pin_value | close | pin $400-1k | 6-9 | 40.0 | -10.1 | -24.6 |
| fd_move+pin_price | close | pin $400-1k | 4-1 | 80.0 | 29.8 | 78.1 |
| fd_juice+pin_price | close | pin $400-1k | 3-2 | 60.0 | 5.9 | 8.1 |
| fd_move+pin_value | close | pin $400-1k | 13-8 | 61.9 | 12.0 | 16.7 |
| fd_juice+pin_lead | close | pin $400-1k | 0-1 | 0.0 | -56.7 | -100.0 |
| fd_juice+pin_value | close | pin $400-1k | 0-1 | 0.0 | -56.7 | -100.0 |
| fd_move+pin_price | close | pin limit <$400 | 1-2 | 33.3 | -11.8 | -28.0 |
| fd_move+pin_value | close | pin limit <$400 | 1-1 | 50.0 | 0.9 | -5.8 |
| fd_juice+pin_price | close | receptions | 7-3 | 70.0 | 15.9 | 26.5 |
| fd_move+pin_price | close | receptions | 2-2 | 50.0 | 3.4 | 35.2 |
| pin_lead+pin_value | close | recv_yds | 13-10 | 56.5 | 6.5 | 6.5 |
| fd_move+pin_value | close | recv_yds | 16-13 | 55.2 | 5.5 | 4.0 |
| fd_move+pin_price | close | recv_yds | 5-5 | 50.0 | 0.4 | -5.7 |
| fd_move+pin_value | close | rush_yds | 11-8 | 57.9 | 7.9 | 9.1 |
| pin_lead+pin_value | close | rush_yds | 3-5 | 37.5 | -11.8 | -29.3 |
| fd_move+pin_price | close | rush_yds | 3-0 | 100.0 | 49.7 | 88.5 |
| pin_value | early | pass_yds | 1-1 | 50.0 | -1.3 | -5.8 |
| pin_value | early | pin $1k+ | 16-7 | 69.6 | 19.4 | 30.1 |
| pin_value | early | pin $400-1k | 0-1 | 0.0 | -49.1 | -100.0 |
| pin_value | early | pin limit <$400 | 1-4 | 20.0 | -30.6 | -62.5 |
| pin_value | early | receptions | 1-0 | 100.0 | 43.2 | 64.9 |
| pin_value | early | recv_yds | 8-6 | 57.1 | 7.1 | 7.7 |
| pin_value | early | rush_yds | 7-5 | 58.3 | 8.6 | 9.9 |
| pin_price | early | anytime_td | 2-2 | 50.0 | 27.1 | 82.5 |
| pin_price | early | pin $1k+ | 6-1 | 85.7 | 46.5 | 115.6 |
| pin_price | early | pin $400-1k | 0-2 | 0.0 | -33.0 | -100.0 |
| pin_price | early | receptions | 3-1 | 75.0 | 25.0 | 41.3 |
| pin_price | early | rush_yds | 1-0 | 100.0 | 50.9 | 114.0 |
| fd_move | early | pass_yds | 5-2 | 71.4 | 22.0 | 34.1 |
| fd_move | early | pin limit <$400 | 2-1 | 66.7 | 16.4 | 25.1 |
| fd_move | early | receptions | 1-1 | 50.0 | 6.8 | 22.0 |
| fd_move | early | recv_yds | 19-8 | 70.4 | 20.5 | 32.1 |
| fd_move | early | rush_yds | 12-4 | 75.0 | 24.8 | 40.8 |
| fd_juice | early | pass_tds | 4-0 | 100.0 | 50.0 | 102.5 |
| fd_juice | early | receptions | 18-9 | 66.7 | 15.9 | 28.8 |
| fd_juice | early | recv_yds | 1-0 | 100.0 | 49.1 | 76.9 |
| td_steam | early | anytime_td | 0-1 | 0.0 | -22.9 | -100.0 |
