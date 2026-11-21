# NFL prop scorecard

Generated 2026-11-21 11:50 UTC. 969 graded props (129 had no nflverse result and are not graded).

## Read this first: fit vs forward

**890 props before 2026-11-17 (fit) · 79 on or after it (forward).**

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

Base rate: the over hit **44.8%** of 969 graded props, but `expected %`
uses **each stat's own rate**, not that pooled one. A yardage over is near a coin
flip; an anytime-TD over 0.5 is a longshot. Scored against one pooled number every
anytime-TD signal would be charged an expectation it could never meet:

- **recv_yds**: over hit 49.1% of 338
- **receptions**: over hit 42.9% of 259
- **rush_yds**: over hit 48.0% of 177
- **anytime_td**: over hit 27.9% of 86
- **pass_yds**: over hit 48.4% of 62
- **pass_tds**: over hit 38.3% of 47

Proposals appear at 50 decided props. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

Props for games kicking off on or after 2026-11-17. n=79, over rate 43.0% of 79.

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| fd_move | 4-2 | 66.7 | 52.3 | 14.3 | +1.51 | 25.1 | 0.33 | -0.17 | 0.0 | keep collecting (6/50) |
| fd_juice | 1-2 | 33.3 | 52.3 | -19.0 | -1.07 | -35.8 | 0.0 | 1.13 | 33.3 | keep collecting (3/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 18-12 | 60.0 | 50.5 | 9.5 | +3.6 | 12.0 |  |  |  | keep collecting (30/50) |
| pin_price | 3-11 | 21.4 | 43.0 | -21.6 | -2.9 | -20.7 |  |  |  | keep collecting (14/50) |
| fd_move | 19-20 | 48.7 | 50.5 | -1.8 | -2.52 | -6.4 |  |  |  | keep collecting (39/50) |
| fd_juice | 12-5 | 70.6 | 51.2 | 19.4 | +5.53 | 32.5 |  |  |  | keep collecting (17/50) |
| pin_lead | 1-3 | 25.0 | 50.0 | -25.0 | -2.12 | -52.9 |  |  |  | keep collecting (4/50) |
| td_steam | 0-4 | 0.0 | 43.0 | -43.0 | -4.0 | -100.0 |  |  |  | keep collecting (4/50) |
| fd_move+pin_value | 3-3 | 50.0 | 50.0 | 0.0 | -0.34 | -5.8 |  |  |  | keep collecting (6/50) |
| pin_lead+pin_value | 1-2 | 33.3 | 47.7 | -14.3 | -1.11 | -37.2 |  |  |  | keep collecting (3/50) |

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
| pin_value | 17-12 | 58.6 | 49.9 | 8.8 | +2.8 | 9.7 | -0.55 | -0.03 | 0.0 | keep collecting (29/50) |
| pin_price | 6-3 | 66.7 | 40.0 | 26.7 | +6.09 | 67.7 | 0.0 | 0.49 | 44.4 | keep collecting (9/50) |
| fd_move | 21-9 | 70.0 | 50.2 | 19.8 | +9.35 | 31.2 | 2.7 | -0.18 | 0.0 | keep collecting (30/50) |
| fd_juice | 15-6 | 71.4 | 49.4 | 22.1 | +8.72 | 41.5 | -0.05 | 3.47 | 57.1 | keep collecting (21/50) |
| td_steam | 0-1 | 0.0 | 27.9 | -27.9 | -1.0 | -100.0 | 0.0 | 8.3 | 100.0 | keep collecting (1/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 159-139 | 53.4 | 49.8 | 3.6 | -0.86 | -0.3 |  |  |  | no edge shown yet |
| pin_price | 54-68 | 44.3 | 40.8 | 3.5 | +5.14 | 4.2 |  |  |  | DROP: below break-even |
| fd_move | 259-251 | 50.8 | 50.2 | 0.6 | -16.5 | -3.2 |  |  |  | no edge shown yet |
| fd_juice | 140-107 | 56.7 | 51.7 | 5.0 | +10.61 | 4.3 |  |  |  | no edge shown yet |
| pin_lead | 23-25 | 47.9 | 50.2 | -2.2 | -5.08 | -10.6 |  |  |  | keep collecting (48/50) |
| td_steam | 9-28 | 24.3 | 27.9 | -3.6 | -4.18 | -11.3 |  |  |  | keep collecting (37/50) |
| pin_lead+pin_value | 19-18 | 51.4 | 50.3 | 1.0 | -1.62 | -4.4 |  |  |  | keep collecting (37/50) |
| fd_juice+pin_price | 5-2 | 71.4 | 53.1 | 18.4 | +1.94 | 27.8 |  |  |  | keep collecting (7/50) |
| fd_move+pin_value | 27-20 | 57.4 | 49.7 | 7.8 | +3.89 | 8.3 |  |  |  | keep collecting (47/50) |
| fd_move+pin_price | 10-7 | 58.8 | 49.4 | 9.4 | +3.49 | 20.5 |  |  |  | keep collecting (17/50) |
| fd_juice+pin_lead | 0-1 | 0.0 | 61.7 | -61.7 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |
| fd_juice+pin_value | 0-1 | 0.0 | 61.7 | -61.7 | -1.0 | -100.0 |  |  |  | keep collecting (1/50) |

## By Pinnacle limit and by stat (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | pass_tds | 3-2 | 60.0 | 7.7 | -13.7 |
| pin_value | close | pass_yds | 16-15 | 51.6 | 2.2 | -2.7 |
| pin_value | close | pin $1k+ | 98-79 | 55.4 | 5.7 | 3.2 |
| pin_value | close | pin $400-1k | 56-52 | 51.9 | 1.8 | -2.6 |
| pin_value | close | pin limit <$400 | 5-8 | 38.5 | -10.7 | -27.9 |
| pin_value | close | receptions | 5-4 | 55.6 | 6.3 | -9.4 |
| pin_value | close | recv_yds | 90-76 | 54.2 | 4.3 | 2.2 |
| pin_value | close | rush_yds | 45-42 | 51.7 | 2.2 | -2.5 |
| pin_price | close | anytime_td | 15-34 | 30.6 | 2.7 | 0.9 |
| pin_price | close | pass_tds | 4-2 | 66.7 | 8.9 | 53.8 |
| pin_price | close | pass_yds | 2-4 | 33.3 | -16.7 | -37.2 |
| pin_price | close | pin $1k+ | 31-38 | 44.9 | 4.7 | 12.1 |
| pin_price | close | pin $400-1k | 21-27 | 43.8 | 1.8 | -5.3 |
| pin_price | close | pin limit <$400 | 2-3 | 40.0 | 1.9 | -13.8 |
| pin_price | close | receptions | 13-16 | 44.8 | -2.5 | -7.4 |
| pin_price | close | recv_yds | 12-8 | 60.0 | 10.5 | 13.1 |
| pin_price | close | rush_yds | 8-4 | 66.7 | 16.3 | 26.7 |
| fd_move | close | pass_tds | 1-3 | 25.0 | -30.9 | -34.5 |
| fd_move | close | pass_yds | 25-25 | 50.0 | -0.4 | -5.8 |
| fd_move | close | pin $1k+ | 102-105 | 49.3 | -1.1 | -6.8 |
| fd_move | close | pin $400-1k | 121-118 | 50.6 | 0.6 | -3.0 |
| fd_move | close | pin limit <$400 | 14-14 | 50.0 | 0.3 | -4.5 |
| fd_move | close | receptions | 21-25 | 45.7 | -5.3 | -3.1 |
| fd_move | close | recv_yds | 136-137 | 49.8 | -0.2 | -6.1 |
| fd_move | close | rush_yds | 76-61 | 55.5 | 5.4 | 4.3 |
| fd_juice | close | pass_tds | 18-19 | 48.6 | -1.0 | -1.4 |
| fd_juice | close | pin $1k+ | 58-41 | 58.6 | 6.4 | 6.4 |
| fd_juice | close | pin $400-1k | 70-56 | 55.6 | 4.6 | 2.7 |
| fd_juice | close | pin limit <$400 | 4-3 | 57.1 | 4.1 | -0.1 |
| fd_juice | close | receptions | 116-85 | 57.7 | 5.6 | 4.7 |
| fd_juice | close | recv_yds | 2-2 | 50.0 | -0.9 | -11.9 |
| fd_juice | close | rush_yds | 4-1 | 80.0 | 30.4 | 41.0 |
| pin_lead | close | pass_tds | 1-1 | 50.0 | -11.7 | -27.2 |
| pin_lead | close | pass_yds | 4-5 | 44.4 | -6.1 | -16.2 |
| pin_lead | close | pin $1k+ | 15-12 | 55.6 | 5.6 | 3.1 |
| pin_lead | close | pin $400-1k | 8-13 | 38.1 | -12.3 | -28.2 |
| pin_lead | close | recv_yds | 12-11 | 52.2 | 2.4 | -1.7 |
| pin_lead | close | rush_yds | 6-8 | 42.9 | -6.0 | -19.2 |
| td_steam | close | anytime_td | 9-28 | 24.3 | -3.6 | -11.3 |
| td_steam | close | pin $1k+ | 1-5 | 16.7 | -11.2 | -71.0 |
| td_steam | close | pin $400-1k | 1-1 | 50.0 | 22.1 | -27.2 |
| td_steam | close | pin limit <$400 | 1-1 | 50.0 | 22.1 | -33.4 |
| pin_lead+pin_value | close | pass_tds | 1-1 | 50.0 | -11.7 | -27.2 |
| fd_juice+pin_lead | close | pass_tds | 0-1 | 0.0 | -61.7 | -100.0 |
| fd_juice+pin_value | close | pass_tds | 0-1 | 0.0 | -61.7 | -100.0 |
| pin_lead+pin_value | close | pass_yds | 4-3 | 57.1 | 6.9 | 7.7 |
| fd_move+pin_price | close | pass_yds | 1-1 | 50.0 | -1.6 | -5.8 |
| fd_move+pin_value | close | pass_yds | 3-2 | 60.0 | 10.3 | 13.1 |
| pin_lead+pin_value | close | pin $1k+ | 13-9 | 59.1 | 9.2 | 9.4 |
| fd_juice+pin_price | close | pin $1k+ | 2-0 | 100.0 | 50.0 | 76.8 |
| fd_move+pin_value | close | pin $1k+ | 13-11 | 54.2 | 4.7 | 2.1 |
| fd_move+pin_price | close | pin $1k+ | 5-4 | 55.6 | 5.2 | 4.7 |
| pin_lead+pin_value | close | pin $400-1k | 6-9 | 40.0 | -11.0 | -24.6 |
| fd_move+pin_price | close | pin $400-1k | 4-1 | 80.0 | 29.6 | 78.1 |
| fd_juice+pin_price | close | pin $400-1k | 3-2 | 60.0 | 5.7 | 8.1 |
| fd_move+pin_value | close | pin $400-1k | 13-8 | 61.9 | 12.0 | 16.7 |
| fd_juice+pin_lead | close | pin $400-1k | 0-1 | 0.0 | -61.7 | -100.0 |
| fd_juice+pin_value | close | pin $400-1k | 0-1 | 0.0 | -61.7 | -100.0 |
| fd_move+pin_price | close | pin limit <$400 | 1-2 | 33.3 | -11.6 | -28.0 |
| fd_move+pin_value | close | pin limit <$400 | 1-1 | 50.0 | 0.9 | -5.8 |
| fd_juice+pin_price | close | receptions | 5-2 | 71.4 | 18.4 | 27.8 |
| fd_move+pin_price | close | receptions | 2-2 | 50.0 | 3.6 | 35.2 |
| pin_lead+pin_value | close | recv_yds | 11-9 | 55.0 | 5.1 | 3.7 |
| fd_move+pin_value | close | recv_yds | 14-11 | 56.0 | 6.3 | 5.6 |
| fd_move+pin_price | close | recv_yds | 5-4 | 55.6 | 5.9 | 4.7 |
| fd_move+pin_value | close | rush_yds | 10-7 | 58.8 | 9.2 | 10.9 |
| pin_lead+pin_value | close | rush_yds | 3-5 | 37.5 | -11.0 | -29.3 |
| fd_move+pin_price | close | rush_yds | 2-0 | 100.0 | 48.0 | 88.5 |
| pin_value | early | pass_yds | 1-1 | 50.0 | 1.6 | -5.8 |
| pin_value | early | pin $1k+ | 16-7 | 69.6 | 19.7 | 30.1 |
| pin_value | early | pin $400-1k | 0-1 | 0.0 | -49.1 | -100.0 |
| pin_value | early | pin limit <$400 | 1-4 | 20.0 | -30.0 | -62.5 |
| pin_value | early | receptions | 1-0 | 100.0 | 42.9 | 64.9 |
| pin_value | early | recv_yds | 8-6 | 57.1 | 7.1 | 7.7 |
| pin_value | early | rush_yds | 7-5 | 58.3 | 9.0 | 9.9 |
| pin_price | early | anytime_td | 2-2 | 50.0 | 22.1 | 82.5 |
| pin_price | early | pin $1k+ | 6-1 | 85.7 | 44.4 | 115.6 |
| pin_price | early | pin $400-1k | 0-2 | 0.0 | -35.4 | -100.0 |
| pin_price | early | receptions | 3-1 | 75.0 | 25.0 | 41.3 |
| pin_price | early | rush_yds | 1-0 | 100.0 | 52.0 | 114.0 |
| fd_move | early | pass_yds | 4-1 | 80.0 | 29.7 | 50.2 |
| fd_move | early | pin limit <$400 | 2-1 | 66.7 | 16.0 | 25.1 |
| fd_move | early | recv_yds | 8-5 | 61.5 | 11.6 | 14.9 |
| fd_move | early | rush_yds | 9-3 | 75.0 | 24.7 | 40.8 |
| fd_juice | early | pass_tds | 4-0 | 100.0 | 50.0 | 102.5 |
| fd_juice | early | receptions | 10-6 | 62.5 | 13.4 | 24.1 |
| fd_juice | early | recv_yds | 1-0 | 100.0 | 49.1 | 76.9 |
| td_steam | early | anytime_td | 0-1 | 0.0 | -27.9 | -100.0 |
