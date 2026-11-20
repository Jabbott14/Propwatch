# NFL prop scorecard

Generated 2026-11-20 02:39 UTC. 939 graded props (165 had no nflverse result and are not graded).

## Read this first: fit vs forward

**890 props before 2026-11-17 (fit) · 49 on or after it (forward).**

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

Base rate: the over hit **44.7%** of 939 graded props, but `expected %`
uses **each stat's own rate**, not that pooled one. A yardage over is near a coin
flip; an anytime-TD over 0.5 is a longshot. Scored against one pooled number every
anytime-TD signal would be charged an expectation it could never meet:

- **recv_yds**: over hit 49.4% of 326
- **receptions**: over hit 43.4% of 249
- **rush_yds**: over hit 47.7% of 172
- **anytime_td**: over hit 25.6% of 86
- **pass_yds**: over hit 50.0% of 60
- **pass_tds**: over hit 37.0% of 46

Proposals appear at 50 decided props. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

Props for games kicking off on or after 2026-11-17. n=49, over rate 40.8% of 49.

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| fd_move | 4-1 | 80.0 | 51.8 | 28.2 | +2.51 | 50.2 | 0.4 | -0.2 | 0.0 | keep collecting (5/50) |
| fd_juice | 1-1 | 50.0 | 50.0 | 0.0 | -0.07 | -3.7 | 0.0 | 1.7 | 50.0 | keep collecting (2/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 10-7 | 58.8 | 49.5 | 9.4 | +1.85 | 10.9 |  |  |  | keep collecting (17/50) |
| pin_price | 1-13 | 7.1 | 40.8 | -33.7 | -10.0 | -71.4 |  |  |  | keep collecting (14/50) |
| fd_move | 9-9 | 50.0 | 50.0 | 0.0 | -1.24 | -6.9 |  |  |  | keep collecting (18/50) |
| fd_juice | 6-3 | 66.7 | 51.0 | 15.6 | +2.96 | 32.8 |  |  |  | keep collecting (9/50) |
| pin_lead | 1-3 | 25.0 | 50.0 | -25.0 | -2.12 | -52.9 |  |  |  | keep collecting (4/50) |
| td_steam | 0-4 | 0.0 | 40.8 | -40.8 | -4.0 | -100.0 |  |  |  | keep collecting (4/50) |
| fd_move+pin_value | 1-1 | 50.0 | 40.8 | 9.2 | -0.11 | -5.8 |  |  |  | keep collecting (2/50) |
| pin_lead+pin_value | 1-2 | 33.3 | 46.9 | -13.6 | -1.11 | -37.2 |  |  |  | keep collecting (3/50) |

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
| pin_value | 17-12 | 58.6 | 49.9 | 8.7 | +2.8 | 9.7 | -0.55 | -0.03 | 0.0 | keep collecting (29/50) |
| pin_price | 6-3 | 66.7 | 38.9 | 27.8 | +6.09 | 67.7 | 0.0 | 0.49 | 44.4 | keep collecting (9/50) |
| fd_move | 21-8 | 72.4 | 50.1 | 22.3 | +10.35 | 35.7 | 2.79 | -0.19 | 0.0 | keep collecting (29/50) |
| fd_juice | 15-5 | 75.0 | 49.0 | 26.0 | +9.72 | 48.6 | -0.05 | 3.65 | 60.0 | keep collecting (20/50) |
| td_steam | 0-1 | 0.0 | 25.6 | -25.6 | -1.0 | -100.0 | 0.0 | 8.3 | 100.0 | keep collecting (1/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 151-134 | 53.0 | 49.8 | 3.2 | -2.61 | -0.9 |  |  |  | no edge shown yet |
| pin_price | 52-70 | 42.6 | 40.0 | 2.6 | -1.96 | -1.6 |  |  |  | DROP: below break-even |
| fd_move | 249-240 | 50.9 | 50.2 | 0.7 | -15.22 | -3.1 |  |  |  | no edge shown yet |
| fd_juice | 134-105 | 56.1 | 51.5 | 4.5 | +8.03 | 3.4 |  |  |  | no edge shown yet |
| pin_lead | 23-25 | 47.9 | 50.1 | -2.2 | -5.08 | -10.6 |  |  |  | keep collecting (48/50) |
| td_steam | 9-28 | 24.3 | 25.6 | -1.3 | -4.18 | -11.3 |  |  |  | keep collecting (37/50) |
| pin_lead+pin_value | 19-18 | 51.4 | 50.3 | 1.1 | -1.62 | -4.4 |  |  |  | keep collecting (37/50) |
| fd_juice+pin_price | 5-2 | 71.4 | 52.8 | 18.6 | +1.94 | 27.8 |  |  |  | keep collecting (7/50) |
| fd_move+pin_value | 25-18 | 58.1 | 49.7 | 8.4 | +4.12 | 9.6 |  |  |  | keep collecting (43/50) |
| fd_move+pin_price | 10-7 | 58.8 | 49.4 | 9.4 | +3.49 | 20.5 |  |  |  | keep collecting (17/50) |
| fd_juice+pin_lead | 0-1 | 0.0 | 63.0 | -63.0 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 63.0 | -63.0 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |

## By Pinnacle limit and by stat (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | pass_tds | 3-1 | 75.0 | 25.0 | 7.8 |
| pin_value | close | pass_yds | 15-15 | 50.0 | 0.0 | -5.8 |
| pin_value | close | pin $1k+ | 91-74 | 55.2 | 5.5 | 2.9 |
| pin_value | close | pin $400-1k | 55-52 | 51.4 | 1.4 | -3.5 |
| pin_value | close | pin limit <$400 | 5-8 | 38.5 | -10.7 | -27.9 |
| pin_value | close | receptions | 4-4 | 50.0 | 1.7 | -17.5 |
| pin_value | close | recv_yds | 86-72 | 54.4 | 4.5 | 2.6 |
| pin_value | close | rush_yds | 43-42 | 50.6 | 1.2 | -4.6 |
| pin_price | close | anytime_td | 13-36 | 26.5 | 0.9 | -13.6 |
| pin_price | close | pass_tds | 4-2 | 66.7 | 8.0 | 53.8 |
| pin_price | close | pass_yds | 2-4 | 33.3 | -16.7 | -37.2 |
| pin_price | close | pin $1k+ | 29-40 | 42.0 | 2.7 | 1.8 |
| pin_price | close | pin $400-1k | 21-27 | 43.8 | 2.5 | -5.3 |
| pin_price | close | pin limit <$400 | 2-3 | 40.0 | 2.5 | -13.8 |
| pin_price | close | receptions | 13-16 | 44.8 | -2.7 | -7.4 |
| pin_price | close | recv_yds | 12-8 | 60.0 | 10.4 | 13.1 |
| pin_price | close | rush_yds | 8-4 | 66.7 | 16.3 | 26.7 |
| fd_move | close | pass_tds | 0-3 | 0.0 | -63.0 | -100.0 |
| fd_move | close | pass_yds | 23-25 | 47.9 | -2.1 | -9.7 |
| fd_move | close | pin $1k+ | 92-96 | 48.9 | -1.5 | -7.9 |
| fd_move | close | pin $400-1k | 121-116 | 51.1 | 1.0 | -2.2 |
| fd_move | close | pin limit <$400 | 14-14 | 50.0 | 0.1 | -4.5 |
| fd_move | close | receptions | 20-24 | 45.5 | -5.4 | -3.3 |
| fd_move | close | recv_yds | 132-129 | 50.6 | 0.6 | -4.7 |
| fd_move | close | rush_yds | 74-59 | 55.6 | 5.5 | 4.6 |
| fd_juice | close | pass_tds | 18-19 | 48.6 | -1.0 | -1.4 |
| fd_juice | close | pin $1k+ | 52-40 | 56.5 | 4.3 | 3.0 |
| fd_juice | close | pin $400-1k | 70-55 | 56.0 | 5.2 | 3.5 |
| fd_juice | close | pin limit <$400 | 4-3 | 57.1 | 4.3 | -0.1 |
| fd_juice | close | receptions | 110-83 | 57.0 | 5.0 | 3.6 |
| fd_juice | close | recv_yds | 2-2 | 50.0 | -0.6 | -11.9 |
| fd_juice | close | rush_yds | 4-1 | 80.0 | 30.5 | 41.0 |
| pin_lead | close | pass_tds | 1-1 | 50.0 | -13.0 | -27.2 |
| pin_lead | close | pass_yds | 4-5 | 44.4 | -5.6 | -16.2 |
| pin_lead | close | pin $1k+ | 15-12 | 55.6 | 5.6 | 3.1 |
| pin_lead | close | pin $400-1k | 8-13 | 38.1 | -12.1 | -28.2 |
| pin_lead | close | recv_yds | 12-11 | 52.2 | 2.3 | -1.7 |
| pin_lead | close | rush_yds | 6-8 | 42.9 | -5.8 | -19.2 |
| td_steam | close | anytime_td | 9-28 | 24.3 | -1.3 | -11.3 |
| td_steam | close | pin $1k+ | 1-5 | 16.7 | -8.9 | -71.0 |
| td_steam | close | pin $400-1k | 1-1 | 50.0 | 24.4 | -27.2 |
| td_steam | close | pin limit <$400 | 1-1 | 50.0 | 24.4 | -33.4 |
| pin_lead+pin_value | close | pass_tds | 1-1 | 50.0 | -13.0 | -27.2 |
| fd_juice+pin_lead | close | pass_tds | 0-1 | 0.0 | -63.0 | -100.0 |
| fd_juice+pin_value | close | pass_tds | 0-1 | 0.0 | -63.0 | -100.0 |
| pin_lead+pin_value | close | pass_yds | 4-3 | 57.1 | 7.1 | 7.7 |
| fd_move+pin_price | close | pass_yds | 1-1 | 50.0 | 0.0 | -5.8 |
| fd_move+pin_value | close | pass_yds | 2-2 | 50.0 | 0.0 | -5.8 |
| pin_lead+pin_value | close | pin $1k+ | 13-9 | 59.1 | 9.1 | 9.4 |
| fd_juice+pin_price | close | pin $1k+ | 2-0 | 100.0 | 50.0 | 76.8 |
| fd_move+pin_value | close | pin $1k+ | 11-9 | 55.0 | 5.6 | 3.7 |
| fd_move+pin_price | close | pin $1k+ | 5-4 | 55.6 | 5.4 | 4.7 |
| pin_lead+pin_value | close | pin $400-1k | 6-9 | 40.0 | -10.7 | -24.6 |
| fd_move+pin_price | close | pin $400-1k | 4-1 | 80.0 | 29.5 | 78.1 |
| fd_juice+pin_price | close | pin $400-1k | 3-2 | 60.0 | 6.0 | 8.1 |
| fd_move+pin_value | close | pin $400-1k | 13-8 | 61.9 | 11.9 | 16.7 |
| fd_juice+pin_lead | close | pin $400-1k | 0-1 | 0.0 | -63.0 | -100.0 |
| fd_juice+pin_value | close | pin $400-1k | 0-1 | 0.0 | -63.0 | -100.0 |
| fd_move+pin_price | close | pin limit <$400 | 1-2 | 33.3 | -12.0 | -28.0 |
| fd_move+pin_value | close | pin limit <$400 | 1-1 | 50.0 | 0.6 | -5.8 |
| fd_juice+pin_price | close | receptions | 5-2 | 71.4 | 18.6 | 27.8 |
| fd_move+pin_price | close | receptions | 2-2 | 50.0 | 3.3 | 35.2 |
| pin_lead+pin_value | close | recv_yds | 11-9 | 55.0 | 5.1 | 3.7 |
| fd_move+pin_value | close | recv_yds | 13-9 | 59.1 | 9.4 | 11.4 |
| fd_move+pin_price | close | recv_yds | 5-4 | 55.6 | 5.8 | 4.7 |
| fd_move+pin_value | close | rush_yds | 10-7 | 58.8 | 9.2 | 10.9 |
| pin_lead+pin_value | close | rush_yds | 3-5 | 37.5 | -10.8 | -29.3 |
| fd_move+pin_price | close | rush_yds | 2-0 | 100.0 | 47.7 | 88.5 |
| pin_value | early | pass_yds | 1-1 | 50.0 | 0.0 | -5.8 |
| pin_value | early | pin $1k+ | 16-7 | 69.6 | 19.7 | 30.1 |
| pin_value | early | pin $400-1k | 0-1 | 0.0 | -49.4 | -100.0 |
| pin_value | early | pin limit <$400 | 1-4 | 20.0 | -30.2 | -62.5 |
| pin_value | early | receptions | 1-0 | 100.0 | 43.4 | 64.9 |
| pin_value | early | recv_yds | 8-6 | 57.1 | 7.1 | 7.7 |
| pin_value | early | rush_yds | 7-5 | 58.3 | 9.1 | 9.9 |
| pin_price | early | anytime_td | 2-2 | 50.0 | 24.4 | 82.5 |
| pin_price | early | pin $1k+ | 6-1 | 85.7 | 45.6 | 115.6 |
| pin_price | early | pin $400-1k | 0-2 | 0.0 | -34.5 | -100.0 |
| pin_price | early | receptions | 3-1 | 75.0 | 25.0 | 41.3 |
| pin_price | early | rush_yds | 1-0 | 100.0 | 52.3 | 114.0 |
| fd_move | early | pass_yds | 4-1 | 80.0 | 30.0 | 50.2 |
| fd_move | early | pin limit <$400 | 2-1 | 66.7 | 15.9 | 25.1 |
| fd_move | early | recv_yds | 8-4 | 66.7 | 16.8 | 24.5 |
| fd_move | early | rush_yds | 9-3 | 75.0 | 24.6 | 40.8 |
| fd_juice | early | pass_tds | 4-0 | 100.0 | 50.0 | 102.5 |
| fd_juice | early | receptions | 10-5 | 66.7 | 18.0 | 32.3 |
| fd_juice | early | recv_yds | 1-0 | 100.0 | 49.4 | 76.9 |
| td_steam | early | anytime_td | 0-1 | 0.0 | -25.6 | -100.0 |
