# NFL prop scorecard

Generated 2026-11-26 13:14 UTC. 1361 graded props (169 had no nflverse result and are not graded).

## Read this first: fit vs forward

**890 props before 2026-11-17 (fit) · 471 on or after it (forward).**

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

Base rate: the over hit **44.7%** of 1361 graded props, but `expected %`
uses **each stat's own rate**, not that pooled one. A yardage over is near a coin
flip; an anytime-TD over 0.5 is a longshot. Scored against one pooled number every
anytime-TD signal would be charged an expectation it could never meet:

- **recv_yds**: over hit 48.7% of 470
- **receptions**: over hit 44.4% of 372
- **rush_yds**: over hit 47.9% of 238
- **anytime_td**: over hit 23.4% of 128
- **pass_yds**: over hit 51.2% of 86
- **pass_tds**: over hit 38.8% of 67

Proposals appear at 50 decided props. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

Props for games kicking off on or after 2026-11-17. n=471, over rate 44.2% of 471.

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 1-1 | 50.0 | 49.0 | 1.0 | -0.12 | -6.2 | -1.0 | -0.1 | 0.0 | keep collecting (2/50) |
| pin_price | 1-1 | 50.0 | 50.8 | -0.8 | -0.02 | -1.0 | 0.0 | 6.75 | 100.0 | keep collecting (2/50) |
| fd_move | 23-8 | 74.2 | 50.3 | 23.9 | +12.81 | 41.3 | 0.9 | -0.04 | 6.5 | keep collecting (31/50) |
| fd_juice | 10-6 | 62.5 | 50.4 | 12.1 | +2.45 | 15.3 | 0.06 | 1.11 | 50.0 | keep collecting (16/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 56-57 | 49.6 | 50.4 | -0.9 | -7.86 | -7.0 |  |  |  | no edge shown yet |
| pin_price | 15-41 | 26.8 | 25.7 | 1.1 | -17.74 | -31.7 |  |  |  | DROP: below break-even |
| fd_move | 140-120 | 53.8 | 49.8 | 4.0 | +7.86 | 3.0 |  |  |  | no edge shown yet |
| fd_juice | 76-55 | 58.0 | 50.3 | 7.7 | +7.57 | 5.8 |  |  |  | no edge shown yet |
| pin_lead | 16-10 | 61.5 | 49.8 | 11.7 | +3.86 | 14.8 |  |  |  | keep collecting (26/50) |
| td_steam | 2-19 | 9.5 | 15.0 | -5.5 | -11.0 | -52.4 |  |  |  | keep collecting (21/50) |
| fd_move+pin_value | 11-11 | 50.0 | 50.3 | -0.3 | -1.27 | -5.8 |  |  |  | keep collecting (22/50) |
| pin_lead+pin_value | 8-7 | 53.3 | 50.0 | 3.3 | -0.22 | -1.5 |  |  |  | keep collecting (15/50) |
| fd_juice+pin_price | 2-2 | 50.0 | 49.1 | 0.9 | -0.29 | -7.3 |  |  |  | keep collecting (4/50) |
| fd_move+pin_price | 1-1 | 50.0 | 47.5 | 2.5 | -0.11 | -5.8 |  |  |  | keep collecting (2/50) |
| fd_juice+pin_lead | 1-1 | 50.0 | 47.6 | 2.4 | -0.42 | -21.0 |  |  |  | keep collecting (2/50) |
| fd_juice+pin_value | 1-1 | 50.0 | 47.6 | 2.4 | -0.42 | -21.0 |  |  |  | keep collecting (2/50) |

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
| pin_value | 18-13 | 58.1 | 49.9 | 8.2 | +2.68 | 8.6 | -0.58 | -0.03 | 0.0 | keep collecting (31/50) |
| pin_price | 7-4 | 63.6 | 41.2 | 22.5 | +6.07 | 55.2 | 0.0 | 1.63 | 54.5 | keep collecting (11/50) |
| fd_move | 40-15 | 72.7 | 49.8 | 22.9 | +20.65 | 37.5 | 1.95 | -0.1 | 3.6 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 24-10 | 70.6 | 50.9 | 19.7 | +12.25 | 36.0 | 0.0 | 2.57 | 55.9 | keep collecting (34/50) |
| td_steam | 0-1 | 0.0 | 23.4 | -23.4 | -1.0 | -100.0 | 0.0 | 8.3 | 100.0 | keep collecting (1/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 197-184 | 51.7 | 49.9 | 1.8 | -12.32 | -3.2 |  |  |  | no edge shown yet |
| pin_price | 66-98 | 40.2 | 38.0 | 2.2 | -9.7 | -5.9 |  |  |  | DROP: below break-even |
| fd_move | 380-351 | 52.0 | 50.1 | 1.9 | -6.12 | -0.8 |  |  |  | no edge shown yet |
| fd_juice | 204-157 | 56.5 | 51.4 | 5.1 | +12.64 | 3.5 |  |  |  | PROMOTE: beats break-even and its own base rate |
| pin_lead | 38-32 | 54.3 | 49.9 | 4.4 | +0.9 | 1.3 |  |  |  | no edge shown yet |
| td_steam | 11-43 | 20.4 | 23.4 | -3.1 | -11.18 | -20.7 |  |  |  | DROP: below break-even |
| pin_lead+pin_value | 26-23 | 53.1 | 50.1 | 2.9 | -0.72 | -1.5 |  |  |  | keep collecting (49/50) |
| fd_juice+pin_price | 7-4 | 63.6 | 52.1 | 11.6 | +1.65 | 15.0 |  |  |  | keep collecting (11/50) |
| fd_move+pin_value | 35-28 | 55.6 | 49.8 | 5.7 | +2.97 | 4.7 |  |  |  | no edge shown yet |
| fd_move+pin_price | 11-8 | 57.9 | 49.1 | 8.8 | +3.37 | 17.8 |  |  |  | keep collecting (19/50) |
| fd_juice+pin_lead | 1-2 | 33.3 | 51.1 | -17.8 | -1.42 | -47.3 |  |  |  | keep collecting (3/50) |
| fd_juice+pin_value | 1-2 | 33.3 | 51.1 | -17.8 | -1.42 | -47.3 |  |  |  | keep collecting (3/50) |

## By Pinnacle limit and by stat (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | pass_tds | 3-2 | 60.0 | 7.8 | -13.7 |
| pin_value | close | pass_yds | 17-20 | 45.9 | -4.5 | -13.4 |
| pin_value | close | pin $1k+ | 131-120 | 52.2 | 2.3 | -2.5 |
| pin_value | close | pin $400-1k | 60-56 | 51.7 | 1.7 | -2.9 |
| pin_value | close | pin limit <$400 | 6-8 | 42.9 | -6.5 | -19.6 |
| pin_value | close | receptions | 6-5 | 54.5 | 6.1 | -11.5 |
| pin_value | close | recv_yds | 115-101 | 53.2 | 3.3 | 0.4 |
| pin_value | close | rush_yds | 56-56 | 50.0 | 0.3 | -5.6 |
| pin_price | close | anytime_td | 19-55 | 25.7 | 2.2 | -18.1 |
| pin_price | close | pass_tds | 4-5 | 44.4 | -11.8 | 2.5 |
| pin_price | close | pass_yds | 3-4 | 42.9 | -7.3 | -19.2 |
| pin_price | close | pin $1k+ | 42-58 | 42.0 | 3.8 | 1.7 |
| pin_price | close | pin $400-1k | 22-37 | 37.3 | -0.6 | -18.2 |
| pin_price | close | pin limit <$400 | 2-3 | 40.0 | 3.1 | -13.8 |
| pin_price | close | receptions | 18-18 | 50.0 | 0.9 | 3.4 |
| pin_price | close | recv_yds | 13-12 | 52.0 | 2.9 | -2.0 |
| pin_price | close | rush_yds | 9-4 | 69.2 | 19.1 | 31.5 |
| fd_move | close | pass_tds | 1-4 | 20.0 | -36.7 | -47.6 |
| fd_move | close | pass_yds | 37-36 | 50.7 | 1.1 | -4.5 |
| fd_move | close | pin $1k+ | 207-196 | 51.4 | 1.2 | -2.2 |
| fd_move | close | pin $400-1k | 128-123 | 51.0 | 1.0 | -2.4 |
| fd_move | close | pin limit <$400 | 15-14 | 51.7 | 1.9 | -1.3 |
| fd_move | close | receptions | 31-32 | 49.2 | -1.4 | 5.9 |
| fd_move | close | recv_yds | 206-192 | 51.8 | 1.8 | -2.5 |
| fd_move | close | rush_yds | 105-87 | 54.7 | 4.6 | 2.9 |
| fd_juice | close | pass_tds | 31-24 | 56.4 | 5.8 | 9.9 |
| fd_juice | close | pin $1k+ | 115-84 | 57.8 | 6.1 | 5.0 |
| fd_juice | close | pin $400-1k | 73-60 | 54.9 | 4.1 | 1.1 |
| fd_juice | close | pin limit <$400 | 4-3 | 57.1 | 4.7 | -0.1 |
| fd_juice | close | receptions | 167-126 | 57.0 | 5.4 | 3.3 |
| fd_juice | close | recv_yds | 2-3 | 40.0 | -11.3 | -29.5 |
| fd_juice | close | rush_yds | 4-4 | 50.0 | 0.5 | -11.9 |
| pin_lead | close | pass_tds | 1-1 | 50.0 | -11.2 | -27.2 |
| pin_lead | close | pass_yds | 5-6 | 45.5 | -4.2 | -14.3 |
| pin_lead | close | pin $1k+ | 29-18 | 61.7 | 11.9 | 14.7 |
| pin_lead | close | pin $400-1k | 9-14 | 39.1 | -11.0 | -26.2 |
| pin_lead | close | receptions | 1-0 | 100.0 | 55.6 | 58.1 |
| pin_lead | close | recv_yds | 20-14 | 58.8 | 8.9 | 10.9 |
| pin_lead | close | rush_yds | 11-11 | 50.0 | 0.8 | -5.8 |
| td_steam | close | anytime_td | 11-43 | 20.4 | -3.1 | -20.7 |
| td_steam | close | pin $1k+ | 2-6 | 25.0 | 1.6 | -53.2 |
| td_steam | close | pin $400-1k | 1-1 | 50.0 | 26.6 | -27.2 |
| td_steam | close | pin limit <$400 | 1-1 | 50.0 | 26.6 | -33.4 |
| pin_lead+pin_value | close | pass_tds | 1-1 | 50.0 | -11.2 | -27.2 |
| fd_juice+pin_lead | close | pass_tds | 0-1 | 0.0 | -61.2 | -100.0 |
| fd_juice+pin_value | close | pass_tds | 0-1 | 0.0 | -61.2 | -100.0 |
| fd_juice+pin_price | close | pass_tds | 0-1 | 0.0 | -38.8 | -100.0 |
| pin_lead+pin_value | close | pass_yds | 4-3 | 57.1 | 7.3 | 7.7 |
| fd_move+pin_price | close | pass_yds | 1-1 | 50.0 | 1.2 | -5.8 |
| fd_move+pin_value | close | pass_yds | 3-4 | 42.9 | -7.3 | -19.2 |
| pin_lead+pin_value | close | pin $1k+ | 20-13 | 60.6 | 10.6 | 12.0 |
| fd_juice+pin_price | close | pin $1k+ | 4-2 | 66.7 | 15.7 | 20.7 |
| fd_move+pin_value | close | pin $1k+ | 20-19 | 51.3 | 1.4 | -3.3 |
| fd_move+pin_price | close | pin $1k+ | 6-5 | 54.5 | 5.1 | 2.8 |
| fd_juice+pin_lead | close | pin $1k+ | 1-1 | 50.0 | 3.9 | -21.0 |
| fd_juice+pin_value | close | pin $1k+ | 1-1 | 50.0 | 3.9 | -21.0 |
| pin_lead+pin_value | close | pin $400-1k | 6-10 | 37.5 | -12.9 | -29.3 |
| fd_move+pin_price | close | pin $400-1k | 4-1 | 80.0 | 29.6 | 78.1 |
| fd_juice+pin_price | close | pin $400-1k | 3-2 | 60.0 | 6.6 | 8.1 |
| fd_move+pin_value | close | pin $400-1k | 13-8 | 61.9 | 12.0 | 16.7 |
| fd_juice+pin_lead | close | pin $400-1k | 0-1 | 0.0 | -61.2 | -100.0 |
| fd_juice+pin_value | close | pin $400-1k | 0-1 | 0.0 | -61.2 | -100.0 |
| fd_move+pin_price | close | pin limit <$400 | 1-2 | 33.3 | -12.5 | -28.0 |
| fd_move+pin_value | close | pin limit <$400 | 2-1 | 66.7 | 17.1 | 25.7 |
| fd_juice+pin_price | close | receptions | 7-3 | 70.0 | 16.6 | 26.5 |
| fd_move+pin_price | close | receptions | 2-2 | 50.0 | 2.8 | 35.2 |
| fd_juice+pin_lead | close | receptions | 1-0 | 100.0 | 55.6 | 58.1 |
| fd_juice+pin_value | close | receptions | 1-0 | 100.0 | 55.6 | 58.1 |
| pin_lead+pin_value | close | receptions | 1-0 | 100.0 | 55.6 | 58.1 |
| pin_lead+pin_value | close | recv_yds | 15-12 | 55.6 | 5.4 | 4.7 |
| fd_move+pin_value | close | recv_yds | 21-16 | 56.8 | 7.0 | 7.0 |
| fd_move+pin_price | close | recv_yds | 5-5 | 50.0 | 0.5 | -5.7 |
| fd_move+pin_value | close | rush_yds | 11-8 | 57.9 | 8.0 | 9.1 |
| pin_lead+pin_value | close | rush_yds | 5-7 | 41.7 | -7.3 | -21.5 |
| fd_move+pin_price | close | rush_yds | 3-0 | 100.0 | 49.3 | 88.5 |
| fd_juice+pin_lead | close | rush_yds | 0-1 | 0.0 | -47.9 | -100.0 |
| fd_juice+pin_value | close | rush_yds | 0-1 | 0.0 | -47.9 | -100.0 |
| pin_value | early | pass_yds | 1-1 | 50.0 | -1.2 | -5.8 |
| pin_value | early | pin $1k+ | 16-8 | 66.7 | 16.8 | 24.7 |
| pin_value | early | pin $400-1k | 0-1 | 0.0 | -48.7 | -100.0 |
| pin_value | early | pin limit <$400 | 2-4 | 33.3 | -17.1 | -37.4 |
| pin_value | early | receptions | 1-0 | 100.0 | 44.4 | 64.9 |
| pin_value | early | recv_yds | 9-7 | 56.2 | 6.4 | 6.0 |
| pin_value | early | rush_yds | 7-5 | 58.3 | 9.0 | 9.9 |
| pin_price | early | anytime_td | 2-2 | 50.0 | 26.6 | 82.5 |
| pin_price | early | pin $1k+ | 6-1 | 85.7 | 46.6 | 115.6 |
| pin_price | early | pin $400-1k | 0-2 | 0.0 | -33.9 | -100.0 |
| pin_price | early | pin limit <$400 | 1-1 | 50.0 | -5.6 | -1.0 |
| pin_price | early | receptions | 4-2 | 66.7 | 14.8 | 27.2 |
| pin_price | early | rush_yds | 1-0 | 100.0 | 52.1 | 114.0 |
| fd_move | early | pass_yds | 5-2 | 71.4 | 21.9 | 34.1 |
| fd_move | early | pin limit <$400 | 2-1 | 66.7 | 16.0 | 25.1 |
| fd_move | early | receptions | 1-1 | 50.0 | 5.6 | 22.0 |
| fd_move | early | recv_yds | 22-8 | 73.3 | 23.5 | 37.6 |
| fd_move | early | rush_yds | 12-4 | 75.0 | 24.5 | 40.8 |
| fd_juice | early | pass_tds | 4-0 | 100.0 | 50.0 | 102.5 |
| fd_juice | early | receptions | 19-10 | 65.5 | 14.5 | 25.4 |
| fd_juice | early | recv_yds | 1-0 | 100.0 | 48.7 | 76.9 |
| td_steam | early | anytime_td | 0-1 | 0.0 | -23.4 | -100.0 |
