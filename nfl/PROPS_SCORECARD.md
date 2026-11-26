# NFL prop scorecard

Generated 2026-11-26 22:26 UTC. 1398 graded props (208 had no nflverse result and are not graded).

## Read this first: fit vs forward

**890 props before 2026-11-17 (fit) · 508 on or after it (forward).**

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

Base rate: the over hit **44.6%** of 1398 graded props, but `expected %`
uses **each stat's own rate**, not that pooled one. A yardage over is near a coin
flip; an anytime-TD over 0.5 is a longshot. Scored against one pooled number every
anytime-TD signal would be charged an expectation it could never meet:

- **recv_yds**: over hit 48.3% of 482
- **receptions**: over hit 44.5% of 382
- **rush_yds**: over hit 48.4% of 244
- **anytime_td**: over hit 23.1% of 134
- **pass_yds**: over hit 52.3% of 88
- **pass_tds**: over hit 38.2% of 68

Proposals appear at 50 decided props. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

Props for games kicking off on or after 2026-11-17. n=508, over rate 44.1% of 508.

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 1-1 | 50.0 | 47.9 | 2.1 | -0.12 | -6.2 | -1.0 | -0.1 | 0.0 | keep collecting (2/50) |
| pin_price | 1-1 | 50.0 | 50.7 | -0.7 | -0.02 | -1.0 | 0.0 | 6.75 | 100.0 | keep collecting (2/50) |
| fd_move | 23-8 | 74.2 | 49.9 | 24.3 | +12.81 | 41.3 | 0.9 | -0.04 | 6.5 | keep collecting (31/50) |
| fd_juice | 10-6 | 62.5 | 50.4 | 12.1 | +2.45 | 15.3 | 0.06 | 1.11 | 50.0 | keep collecting (16/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 65-58 | 52.8 | 50.6 | 2.3 | -0.78 | -0.6 |  |  |  | no edge shown yet |
| pin_price | 15-46 | 24.6 | 24.9 | -0.3 | -22.74 | -37.3 |  |  |  | DROP: below break-even |
| fd_move | 147-132 | 52.7 | 49.7 | 2.9 | +2.06 | 0.7 |  |  |  | no edge shown yet |
| fd_juice | 81-61 | 57.0 | 50.4 | 6.7 | +4.64 | 3.3 |  |  |  | no edge shown yet |
| pin_lead | 17-10 | 63.0 | 49.8 | 13.2 | +4.74 | 17.6 |  |  |  | keep collecting (27/50) |
| td_steam | 3-19 | 13.6 | 15.2 | -1.5 | -10.31 | -46.9 |  |  |  | keep collecting (22/50) |
| fd_move+pin_value | 14-11 | 56.0 | 50.6 | 5.4 | +1.39 | 5.6 |  |  |  | keep collecting (25/50) |
| pin_lead+pin_value | 8-7 | 53.3 | 50.5 | 2.8 | -0.22 | -1.5 |  |  |  | keep collecting (15/50) |
| fd_juice+pin_price | 2-2 | 50.0 | 49.1 | 0.9 | -0.29 | -7.3 |  |  |  | keep collecting (4/50) |
| fd_move+pin_price | 1-1 | 50.0 | 47.7 | 2.3 | -0.11 | -5.8 |  |  |  | keep collecting (2/50) |
| fd_juice+pin_lead | 1-1 | 50.0 | 48.4 | 1.6 | -0.42 | -21.0 |  |  |  | keep collecting (2/50) |
| fd_juice+pin_value | 1-1 | 50.0 | 48.4 | 1.6 | -0.42 | -21.0 |  |  |  | keep collecting (2/50) |

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
| pin_value | 18-13 | 58.1 | 50.0 | 8.1 | +2.68 | 8.6 | -0.58 | -0.03 | 0.0 | keep collecting (31/50) |
| pin_price | 7-4 | 63.6 | 41.1 | 22.6 | +6.07 | 55.2 | 0.0 | 1.63 | 54.5 | keep collecting (11/50) |
| fd_move | 40-15 | 72.7 | 49.7 | 23.1 | +20.65 | 37.5 | 1.95 | -0.1 | 3.6 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 24-10 | 70.6 | 50.9 | 19.7 | +12.25 | 36.0 | 0.0 | 2.57 | 55.9 | keep collecting (34/50) |
| td_steam | 0-1 | 0.0 | 23.1 | -23.1 | -1.0 | -100.0 | 0.0 | 8.3 | 100.0 | keep collecting (1/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 206-185 | 52.7 | 50.0 | 2.7 | -5.24 | -1.3 |  |  |  | no edge shown yet |
| pin_price | 66-103 | 39.1 | 37.5 | 1.6 | -14.7 | -8.7 |  |  |  | DROP: below break-even |
| fd_move | 387-363 | 51.6 | 50.0 | 1.6 | -11.92 | -1.6 |  |  |  | no edge shown yet |
| fd_juice | 209-163 | 56.2 | 51.3 | 4.9 | +9.72 | 2.6 |  |  |  | no edge shown yet |
| pin_lead | 39-32 | 54.9 | 49.9 | 5.0 | +1.78 | 2.5 |  |  |  | no edge shown yet |
| td_steam | 12-43 | 21.8 | 23.1 | -1.3 | -10.49 | -19.1 |  |  |  | DROP: below break-even |
| pin_lead+pin_value | 26-23 | 53.1 | 50.2 | 2.8 | -0.72 | -1.5 |  |  |  | keep collecting (49/50) |
| fd_juice+pin_price | 7-4 | 63.6 | 51.9 | 11.7 | +1.65 | 15.0 |  |  |  | keep collecting (11/50) |
| fd_move+pin_value | 38-28 | 57.6 | 49.9 | 7.7 | +5.63 | 8.5 |  |  |  | no edge shown yet |
| fd_move+pin_price | 11-8 | 57.9 | 48.9 | 9.0 | +3.37 | 17.8 |  |  |  | keep collecting (19/50) |
| fd_juice+pin_lead | 1-2 | 33.3 | 51.5 | -18.2 | -1.42 | -47.3 |  |  |  | keep collecting (3/50) |
| fd_juice+pin_value | 1-2 | 33.3 | 51.5 | -18.2 | -1.42 | -47.3 |  |  |  | keep collecting (3/50) |

## By Pinnacle limit and by stat (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | pass_tds | 3-2 | 60.0 | 7.6 | -13.7 |
| pin_value | close | pass_yds | 18-20 | 47.4 | -3.6 | -10.7 |
| pin_value | close | pin $1k+ | 140-121 | 53.6 | 3.6 | 0.3 |
| pin_value | close | pin $400-1k | 60-56 | 51.7 | 1.8 | -2.9 |
| pin_value | close | pin limit <$400 | 6-8 | 42.9 | -6.7 | -19.6 |
| pin_value | close | receptions | 6-5 | 54.5 | 6.0 | -11.5 |
| pin_value | close | recv_yds | 120-102 | 54.1 | 4.1 | 2.0 |
| pin_value | close | rush_yds | 59-56 | 51.3 | 1.6 | -3.2 |
| pin_price | close | anytime_td | 19-60 | 24.1 | 0.9 | -23.3 |
| pin_price | close | pass_tds | 4-5 | 44.4 | -12.1 | 2.5 |
| pin_price | close | pass_yds | 3-4 | 42.9 | -7.5 | -19.2 |
| pin_price | close | pin $1k+ | 42-62 | 40.4 | 2.9 | -2.2 |
| pin_price | close | pin $400-1k | 22-37 | 37.3 | -0.4 | -18.2 |
| pin_price | close | pin limit <$400 | 2-4 | 33.3 | -1.1 | -28.2 |
| pin_price | close | receptions | 18-18 | 50.0 | 0.9 | 3.4 |
| pin_price | close | recv_yds | 13-12 | 52.0 | 3.1 | -2.0 |
| pin_price | close | rush_yds | 9-4 | 69.2 | 19.1 | 31.5 |
| fd_move | close | pass_tds | 1-5 | 16.7 | -37.3 | -56.3 |
| fd_move | close | pass_yds | 39-36 | 52.0 | 2.6 | -2.0 |
| fd_move | close | pin $1k+ | 213-207 | 50.7 | 0.7 | -3.5 |
| fd_move | close | pin $400-1k | 128-123 | 51.0 | 1.0 | -2.4 |
| fd_move | close | pin limit <$400 | 15-14 | 51.7 | 2.0 | -1.3 |
| fd_move | close | receptions | 31-33 | 48.4 | -2.2 | 4.3 |
| fd_move | close | recv_yds | 209-200 | 51.1 | 1.1 | -3.7 |
| fd_move | close | rush_yds | 107-89 | 54.6 | 4.5 | 2.7 |
| fd_juice | close | pass_tds | 31-24 | 56.4 | 5.7 | 9.9 |
| fd_juice | close | pin $1k+ | 119-90 | 56.9 | 5.4 | 3.1 |
| fd_juice | close | pin $400-1k | 73-60 | 54.9 | 4.1 | 1.1 |
| fd_juice | close | pin limit <$400 | 4-3 | 57.1 | 4.8 | -0.1 |
| fd_juice | close | receptions | 171-131 | 56.6 | 5.1 | 2.3 |
| fd_juice | close | recv_yds | 2-3 | 40.0 | -11.7 | -29.5 |
| fd_juice | close | rush_yds | 5-5 | 50.0 | 0.0 | -13.3 |
| pin_lead | close | pass_tds | 1-1 | 50.0 | -11.8 | -27.2 |
| pin_lead | close | pass_yds | 5-6 | 45.5 | -3.9 | -14.3 |
| pin_lead | close | pin $1k+ | 30-18 | 62.5 | 12.6 | 16.3 |
| pin_lead | close | pin $400-1k | 9-14 | 39.1 | -10.9 | -26.2 |
| pin_lead | close | receptions | 1-0 | 100.0 | 55.5 | 58.1 |
| pin_lead | close | recv_yds | 21-14 | 60.0 | 10.1 | 13.1 |
| pin_lead | close | rush_yds | 11-11 | 50.0 | 0.6 | -5.8 |
| td_steam | close | anytime_td | 12-43 | 21.8 | -1.3 | -19.1 |
| td_steam | close | pin $1k+ | 3-6 | 33.3 | 10.2 | -39.7 |
| td_steam | close | pin $400-1k | 1-1 | 50.0 | 26.9 | -27.2 |
| td_steam | close | pin limit <$400 | 1-1 | 50.0 | 26.9 | -33.4 |
| pin_lead+pin_value | close | pass_tds | 1-1 | 50.0 | -11.8 | -27.2 |
| fd_juice+pin_lead | close | pass_tds | 0-1 | 0.0 | -61.8 | -100.0 |
| fd_juice+pin_value | close | pass_tds | 0-1 | 0.0 | -61.8 | -100.0 |
| fd_juice+pin_price | close | pass_tds | 0-1 | 0.0 | -38.2 | -100.0 |
| pin_lead+pin_value | close | pass_yds | 4-3 | 57.1 | 7.5 | 7.7 |
| fd_move+pin_price | close | pass_yds | 1-1 | 50.0 | 2.3 | -5.8 |
| fd_move+pin_value | close | pass_yds | 4-4 | 50.0 | -0.6 | -5.8 |
| pin_lead+pin_value | close | pin $1k+ | 20-13 | 60.6 | 10.4 | 12.0 |
| fd_juice+pin_price | close | pin $1k+ | 4-2 | 66.7 | 15.9 | 20.7 |
| fd_move+pin_value | close | pin $1k+ | 23-19 | 54.8 | 4.8 | 3.2 |
| fd_move+pin_price | close | pin $1k+ | 6-5 | 54.5 | 5.4 | 2.8 |
| fd_juice+pin_lead | close | pin $1k+ | 1-1 | 50.0 | 3.6 | -21.0 |
| fd_juice+pin_value | close | pin $1k+ | 1-1 | 50.0 | 3.6 | -21.0 |
| pin_lead+pin_value | close | pin $400-1k | 6-10 | 37.5 | -12.8 | -29.3 |
| fd_move+pin_price | close | pin $400-1k | 4-1 | 80.0 | 29.7 | 78.1 |
| fd_juice+pin_price | close | pin $400-1k | 3-2 | 60.0 | 6.7 | 8.1 |
| fd_move+pin_value | close | pin $400-1k | 13-8 | 61.9 | 12.1 | 16.7 |
| fd_juice+pin_lead | close | pin $400-1k | 0-1 | 0.0 | -61.8 | -100.0 |
| fd_juice+pin_value | close | pin $400-1k | 0-1 | 0.0 | -61.8 | -100.0 |
| fd_move+pin_price | close | pin limit <$400 | 1-2 | 33.3 | -12.4 | -28.0 |
| fd_move+pin_value | close | pin limit <$400 | 2-1 | 66.7 | 17.2 | 25.7 |
| fd_juice+pin_price | close | receptions | 7-3 | 70.0 | 16.7 | 26.5 |
| fd_move+pin_price | close | receptions | 2-2 | 50.0 | 2.7 | 35.2 |
| fd_juice+pin_lead | close | receptions | 1-0 | 100.0 | 55.5 | 58.1 |
| fd_juice+pin_value | close | receptions | 1-0 | 100.0 | 55.5 | 58.1 |
| pin_lead+pin_value | close | receptions | 1-0 | 100.0 | 55.5 | 58.1 |
| pin_lead+pin_value | close | recv_yds | 15-12 | 55.6 | 5.4 | 4.7 |
| fd_move+pin_value | close | recv_yds | 22-16 | 57.9 | 8.2 | 9.1 |
| fd_move+pin_price | close | recv_yds | 5-5 | 50.0 | 0.7 | -5.7 |
| fd_move+pin_value | close | rush_yds | 12-8 | 60.0 | 10.2 | 13.1 |
| pin_lead+pin_value | close | rush_yds | 5-7 | 41.7 | -7.5 | -21.5 |
| fd_move+pin_price | close | rush_yds | 3-0 | 100.0 | 49.5 | 88.5 |
| fd_juice+pin_lead | close | rush_yds | 0-1 | 0.0 | -48.4 | -100.0 |
| fd_juice+pin_value | close | rush_yds | 0-1 | 0.0 | -48.4 | -100.0 |
| pin_value | early | pass_yds | 1-1 | 50.0 | -2.3 | -5.8 |
| pin_value | early | pin $1k+ | 16-8 | 66.7 | 16.8 | 24.7 |
| pin_value | early | pin $400-1k | 0-1 | 0.0 | -48.3 | -100.0 |
| pin_value | early | pin limit <$400 | 2-4 | 33.3 | -17.3 | -37.4 |
| pin_value | early | receptions | 1-0 | 100.0 | 44.5 | 64.9 |
| pin_value | early | recv_yds | 9-7 | 56.2 | 6.5 | 6.0 |
| pin_value | early | rush_yds | 7-5 | 58.3 | 8.9 | 9.9 |
| pin_price | early | anytime_td | 2-2 | 50.0 | 26.9 | 82.5 |
| pin_price | early | pin $1k+ | 6-1 | 85.7 | 46.7 | 115.6 |
| pin_price | early | pin $400-1k | 0-2 | 0.0 | -33.8 | -100.0 |
| pin_price | early | pin limit <$400 | 1-1 | 50.0 | -5.5 | -1.0 |
| pin_price | early | receptions | 4-2 | 66.7 | 14.8 | 27.2 |
| pin_price | early | rush_yds | 1-0 | 100.0 | 51.6 | 114.0 |
| fd_move | early | pass_yds | 5-2 | 71.4 | 22.4 | 34.1 |
| fd_move | early | pin limit <$400 | 2-1 | 66.7 | 16.1 | 25.1 |
| fd_move | early | receptions | 1-1 | 50.0 | 5.5 | 22.0 |
| fd_move | early | recv_yds | 22-8 | 73.3 | 23.6 | 37.6 |
| fd_move | early | rush_yds | 12-4 | 75.0 | 24.6 | 40.8 |
| fd_juice | early | pass_tds | 4-0 | 100.0 | 50.0 | 102.5 |
| fd_juice | early | receptions | 19-10 | 65.5 | 14.6 | 25.4 |
| fd_juice | early | recv_yds | 1-0 | 100.0 | 48.3 | 76.9 |
| td_steam | early | anytime_td | 0-1 | 0.0 | -23.1 | -100.0 |
