# NFL prop scorecard

Generated 2026-11-27 13:47 UTC. 1476 graded props (173 had no nflverse result and are not graded).

## Read this first: fit vs forward

**890 props before 2026-11-17 (fit) · 586 on or after it (forward).**

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

Base rate: the over hit **43.9%** of 1476 graded props, but `expected %`
uses **each stat's own rate**, not that pooled one. A yardage over is near a coin
flip; an anytime-TD over 0.5 is a longshot. Scored against one pooled number every
anytime-TD signal would be charged an expectation it could never meet:

- **recv_yds**: over hit 47.7% of 505
- **receptions**: over hit 43.2% of 405
- **rush_yds**: over hit 48.8% of 256
- **anytime_td**: over hit 22.4% of 147
- **pass_yds**: over hit 52.2% of 92
- **pass_tds**: over hit 36.6% of 71

Proposals appear at 50 decided props. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

Props for games kicking off on or after 2026-11-17. n=586, over rate 42.3% of 586.

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 1-1 | 50.0 | 46.3 | 3.7 | -0.12 | -6.2 | -1.0 | -0.1 | 0.0 | keep collecting (2/50) |
| pin_price | 1-2 | 33.3 | 41.4 | -8.1 | -1.02 | -34.0 | 0.0 | 3.6 | 66.7 | keep collecting (3/50) |
| fd_move | 23-10 | 69.7 | 49.3 | 20.4 | +10.81 | 32.8 | 0.82 | -0.05 | 6.1 | keep collecting (33/50) |
| fd_juice | 11-6 | 64.7 | 51.9 | 12.8 | +3.27 | 19.3 | 0.06 | 1.16 | 52.9 | keep collecting (17/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 74-67 | 52.5 | 50.7 | 1.8 | -1.82 | -1.3 |  |  |  | no edge shown yet |
| pin_price | 17-58 | 22.7 | 25.0 | -2.4 | -29.97 | -40.0 |  |  |  | DROP: below break-even |
| fd_move | 169-149 | 53.1 | 49.9 | 3.2 | +4.97 | 1.6 |  |  |  | no edge shown yet |
| fd_juice | 96-68 | 58.5 | 51.5 | 7.0 | +7.21 | 4.4 |  |  |  | PROMOTE: beats break-even and its own base rate |
| pin_lead | 19-12 | 61.3 | 50.2 | 11.1 | +4.51 | 14.6 |  |  |  | keep collecting (31/50) |
| td_steam | 4-21 | 16.0 | 15.2 | 0.8 | -11.77 | -47.1 |  |  |  | keep collecting (25/50) |
| fd_move+pin_value | 19-13 | 59.4 | 51.0 | 8.4 | +3.81 | 11.9 |  |  |  | keep collecting (32/50) |
| pin_lead+pin_value | 10-9 | 52.6 | 51.2 | 1.5 | -0.45 | -2.4 |  |  |  | keep collecting (19/50) |
| fd_juice+pin_price | 2-2 | 50.0 | 49.6 | 0.4 | -0.29 | -7.3 |  |  |  | keep collecting (4/50) |
| fd_move+pin_price | 1-2 | 33.3 | 46.9 | -13.6 | -1.11 | -37.2 |  |  |  | keep collecting (3/50) |
| fd_juice+pin_lead | 1-1 | 50.0 | 47.2 | 2.8 | -0.42 | -21.0 |  |  |  | keep collecting (2/50) |
| fd_juice+pin_value | 1-1 | 50.0 | 47.2 | 2.8 | -0.42 | -21.0 |  |  |  | keep collecting (2/50) |

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
| pin_value | 18-13 | 58.1 | 50.1 | 8.0 | +2.68 | 8.6 | -0.58 | -0.03 | 0.0 | keep collecting (31/50) |
| pin_price | 7-5 | 58.3 | 39.6 | 18.8 | +5.07 | 42.3 | 0.0 | 1.27 | 50.0 | keep collecting (12/50) |
| fd_move | 40-17 | 70.2 | 49.5 | 20.7 | +18.65 | 32.7 | 1.86 | -0.11 | 3.5 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 25-10 | 71.4 | 50.8 | 20.6 | +13.07 | 37.3 | 0.0 | 2.55 | 57.1 | keep collecting (35/50) |
| td_steam | 0-1 | 0.0 | 22.4 | -22.4 | -1.0 | -100.0 | 0.0 | 8.3 | 100.0 | keep collecting (1/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 215-194 | 52.6 | 50.0 | 2.6 | -6.28 | -1.5 |  |  |  | no edge shown yet |
| pin_price | 68-115 | 37.2 | 36.5 | 0.7 | -21.93 | -12.0 |  |  |  | DROP: below break-even |
| fd_move | 409-380 | 51.8 | 50.1 | 1.8 | -9.01 | -1.1 |  |  |  | no edge shown yet |
| fd_juice | 224-170 | 56.9 | 51.7 | 5.1 | +12.29 | 3.1 |  |  |  | PROMOTE: beats break-even and its own base rate |
| pin_lead | 41-34 | 54.7 | 50.0 | 4.6 | +1.55 | 2.1 |  |  |  | no edge shown yet |
| td_steam | 13-45 | 22.4 | 22.4 | -0.0 | -11.95 | -20.6 |  |  |  | DROP: below break-even |
| pin_lead+pin_value | 28-25 | 52.8 | 50.4 | 2.4 | -0.95 | -1.8 |  |  |  | no edge shown yet |
| fd_juice+pin_price | 7-4 | 63.6 | 52.5 | 11.1 | +1.65 | 15.0 |  |  |  | keep collecting (11/50) |
| fd_move+pin_value | 43-30 | 58.9 | 49.9 | 9.0 | +8.05 | 11.0 |  |  |  | no edge shown yet |
| fd_move+pin_price | 11-9 | 55.0 | 48.4 | 6.6 | +2.37 | 11.9 |  |  |  | keep collecting (20/50) |
| fd_juice+pin_lead | 1-2 | 33.3 | 51.8 | -18.5 | -1.42 | -47.3 |  |  |  | keep collecting (3/50) |
| fd_juice+pin_value | 1-2 | 33.3 | 51.8 | -18.5 | -1.42 | -47.3 |  |  |  | keep collecting (3/50) |

## By Pinnacle limit and by stat (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | pass_tds | 3-2 | 60.0 | 7.3 | -13.7 |
| pin_value | close | pass_yds | 19-21 | 47.5 | -3.5 | -10.5 |
| pin_value | close | pin $1k+ | 149-130 | 53.4 | 3.4 | -0.1 |
| pin_value | close | pin $400-1k | 60-56 | 51.7 | 1.7 | -2.9 |
| pin_value | close | pin limit <$400 | 6-8 | 42.9 | -6.8 | -19.6 |
| pin_value | close | receptions | 6-5 | 54.5 | 6.4 | -11.5 |
| pin_value | close | recv_yds | 126-108 | 53.8 | 3.9 | 1.6 |
| pin_value | close | rush_yds | 61-58 | 51.3 | 1.4 | -3.3 |
| pin_price | close | anytime_td | 20-69 | 22.5 | 0.0 | -26.0 |
| pin_price | close | pass_tds | 4-6 | 40.0 | -15.4 | -7.7 |
| pin_price | close | pass_yds | 3-4 | 42.9 | -7.5 | -19.2 |
| pin_price | close | pin $1k+ | 44-74 | 37.3 | 1.1 | -8.0 |
| pin_price | close | pin $400-1k | 22-37 | 37.3 | -0.1 | -18.2 |
| pin_price | close | pin limit <$400 | 2-4 | 33.3 | -0.2 | -28.2 |
| pin_price | close | receptions | 19-19 | 50.0 | 1.1 | 1.8 |
| pin_price | close | recv_yds | 13-12 | 52.0 | 3.5 | -2.0 |
| pin_price | close | rush_yds | 9-5 | 64.3 | 14.3 | 22.1 |
| fd_move | close | pass_tds | 1-5 | 16.7 | -37.8 | -56.3 |
| fd_move | close | pass_yds | 42-36 | 53.8 | 4.5 | 1.5 |
| fd_move | close | pin $1k+ | 234-224 | 51.1 | 1.0 | -2.7 |
| fd_move | close | pin $400-1k | 128-123 | 51.0 | 1.0 | -2.4 |
| fd_move | close | pin limit <$400 | 15-14 | 51.7 | 2.3 | -1.3 |
| fd_move | close | receptions | 33-35 | 48.5 | -2.3 | 4.5 |
| fd_move | close | recv_yds | 222-209 | 51.5 | 1.5 | -3.0 |
| fd_move | close | rush_yds | 111-95 | 53.9 | 3.8 | 1.4 |
| fd_juice | close | pass_tds | 33-25 | 56.9 | 6.0 | 9.5 |
| fd_juice | close | pin $1k+ | 134-97 | 58.0 | 6.0 | 3.9 |
| fd_juice | close | pin $400-1k | 73-60 | 54.9 | 3.9 | 1.1 |
| fd_juice | close | pin limit <$400 | 4-3 | 57.1 | 4.2 | -0.1 |
| fd_juice | close | receptions | 183-137 | 57.2 | 5.3 | 2.8 |
| fd_juice | close | recv_yds | 2-3 | 40.0 | -12.3 | -29.5 |
| fd_juice | close | rush_yds | 6-5 | 54.5 | 4.4 | -6.1 |
| pin_lead | close | pass_tds | 1-1 | 50.0 | -13.4 | -27.2 |
| pin_lead | close | pass_yds | 6-6 | 50.0 | 0.4 | -5.8 |
| pin_lead | close | pin $1k+ | 32-20 | 61.5 | 11.5 | 14.6 |
| pin_lead | close | pin $400-1k | 9-14 | 39.1 | -11.0 | -26.2 |
| pin_lead | close | receptions | 1-0 | 100.0 | 56.8 | 58.1 |
| pin_lead | close | recv_yds | 21-15 | 58.3 | 8.5 | 10.0 |
| pin_lead | close | rush_yds | 12-12 | 50.0 | 0.4 | -5.8 |
| td_steam | close | anytime_td | 13-45 | 22.4 | -0.0 | -20.6 |
| td_steam | close | pin $1k+ | 4-8 | 33.3 | 10.9 | -41.9 |
| td_steam | close | pin $400-1k | 1-1 | 50.0 | 27.6 | -27.2 |
| td_steam | close | pin limit <$400 | 1-1 | 50.0 | 27.6 | -33.4 |
| pin_lead+pin_value | close | pass_tds | 1-1 | 50.0 | -13.4 | -27.2 |
| fd_juice+pin_lead | close | pass_tds | 0-1 | 0.0 | -63.4 | -100.0 |
| fd_juice+pin_value | close | pass_tds | 0-1 | 0.0 | -63.4 | -100.0 |
| fd_juice+pin_price | close | pass_tds | 0-1 | 0.0 | -36.6 | -100.0 |
| pin_lead+pin_value | close | pass_yds | 5-3 | 62.5 | 12.5 | 17.8 |
| fd_move+pin_price | close | pass_yds | 1-1 | 50.0 | 2.2 | -5.8 |
| fd_move+pin_value | close | pass_yds | 4-4 | 50.0 | -0.5 | -5.8 |
| pin_lead+pin_value | close | pin $1k+ | 22-15 | 59.5 | 9.1 | 10.1 |
| fd_juice+pin_price | close | pin $1k+ | 4-2 | 66.7 | 15.5 | 20.7 |
| fd_move+pin_value | close | pin $1k+ | 28-21 | 57.1 | 7.0 | 7.7 |
| fd_move+pin_price | close | pin $1k+ | 6-6 | 50.0 | 1.5 | -5.8 |
| fd_juice+pin_lead | close | pin $1k+ | 1-1 | 50.0 | 4.0 | -21.0 |
| fd_juice+pin_value | close | pin $1k+ | 1-1 | 50.0 | 4.0 | -21.0 |
| pin_lead+pin_value | close | pin $400-1k | 6-10 | 37.5 | -13.0 | -29.3 |
| fd_move+pin_price | close | pin $400-1k | 4-1 | 80.0 | 29.8 | 78.1 |
| fd_juice+pin_price | close | pin $400-1k | 3-2 | 60.0 | 5.9 | 8.1 |
| fd_move+pin_value | close | pin $400-1k | 13-8 | 61.9 | 12.3 | 16.7 |
| fd_juice+pin_lead | close | pin $400-1k | 0-1 | 0.0 | -63.4 | -100.0 |
| fd_juice+pin_value | close | pin $400-1k | 0-1 | 0.0 | -63.4 | -100.0 |
| fd_move+pin_price | close | pin limit <$400 | 1-2 | 33.3 | -11.4 | -28.0 |
| fd_move+pin_value | close | pin limit <$400 | 2-1 | 66.7 | 17.4 | 25.7 |
| fd_juice+pin_price | close | receptions | 7-3 | 70.0 | 15.9 | 26.5 |
| fd_move+pin_price | close | receptions | 2-3 | 40.0 | -5.9 | 8.2 |
| fd_juice+pin_lead | close | receptions | 1-0 | 100.0 | 56.8 | 58.1 |
| fd_juice+pin_value | close | receptions | 1-0 | 100.0 | 56.8 | 58.1 |
| pin_lead+pin_value | close | receptions | 1-0 | 100.0 | 56.8 | 58.1 |
| pin_lead+pin_value | close | recv_yds | 15-13 | 53.6 | 3.2 | 1.0 |
| fd_move+pin_value | close | recv_yds | 27-18 | 60.0 | 10.2 | 13.1 |
| fd_move+pin_price | close | recv_yds | 5-5 | 50.0 | 0.9 | -5.7 |
| fd_move+pin_value | close | rush_yds | 12-8 | 60.0 | 10.1 | 13.1 |
| pin_lead+pin_value | close | rush_yds | 6-8 | 42.9 | -6.6 | -19.2 |
| fd_move+pin_price | close | rush_yds | 3-0 | 100.0 | 49.6 | 88.5 |
| fd_juice+pin_lead | close | rush_yds | 0-1 | 0.0 | -48.8 | -100.0 |
| fd_juice+pin_value | close | rush_yds | 0-1 | 0.0 | -48.8 | -100.0 |
| pin_value | early | pass_yds | 1-1 | 50.0 | -2.2 | -5.8 |
| pin_value | early | pin $1k+ | 16-8 | 66.7 | 16.7 | 24.7 |
| pin_value | early | pin $400-1k | 0-1 | 0.0 | -47.7 | -100.0 |
| pin_value | early | pin limit <$400 | 2-4 | 33.3 | -17.4 | -37.4 |
| pin_value | early | receptions | 1-0 | 100.0 | 43.2 | 64.9 |
| pin_value | early | recv_yds | 9-7 | 56.2 | 6.5 | 6.0 |
| pin_value | early | rush_yds | 7-5 | 58.3 | 8.7 | 9.9 |
| pin_price | early | anytime_td | 2-3 | 40.0 | 17.6 | 46.0 |
| pin_price | early | pin $1k+ | 6-1 | 85.7 | 46.7 | 115.6 |
| pin_price | early | pin $400-1k | 0-3 | 0.0 | -29.4 | -100.0 |
| pin_price | early | pin limit <$400 | 1-1 | 50.0 | -6.8 | -1.0 |
| pin_price | early | receptions | 4-2 | 66.7 | 14.4 | 27.2 |
| pin_price | early | rush_yds | 1-0 | 100.0 | 51.2 | 114.0 |
| fd_move | early | pass_yds | 5-2 | 71.4 | 22.4 | 34.1 |
| fd_move | early | pin limit <$400 | 2-1 | 66.7 | 16.3 | 25.1 |
| fd_move | early | receptions | 1-1 | 50.0 | 6.8 | 22.0 |
| fd_move | early | recv_yds | 22-9 | 71.0 | 21.3 | 33.2 |
| fd_move | early | rush_yds | 12-5 | 70.6 | 20.4 | 32.5 |
| fd_juice | early | pass_tds | 4-0 | 100.0 | 50.0 | 102.5 |
| fd_juice | early | receptions | 20-10 | 66.7 | 15.8 | 27.3 |
| fd_juice | early | recv_yds | 1-0 | 100.0 | 47.7 | 76.9 |
| td_steam | early | anytime_td | 0-1 | 0.0 | -22.4 | -100.0 |
