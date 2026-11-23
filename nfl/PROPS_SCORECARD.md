# NFL prop scorecard

Generated 2026-11-23 13:42 UTC. 1290 graded props (161 had no nflverse result and are not graded).

## Read this first: fit vs forward

**890 props before 2026-11-17 (fit) · 400 on or after it (forward).**

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

Base rate: the over hit **45.2%** of 1290 graded props, but `expected %`
uses **each stat's own rate**, not that pooled one. A yardage over is near a coin
flip; an anytime-TD over 0.5 is a longshot. Scored against one pooled number every
anytime-TD signal would be charged an expectation it could never meet:

- **recv_yds**: over hit 49.3% of 446
- **receptions**: over hit 44.0% of 352
- **rush_yds**: over hit 47.6% of 229
- **anytime_td**: over hit 25.4% of 118
- **pass_yds**: over hit 52.4% of 82
- **pass_tds**: over hit 41.3% of 63

Proposals appear at 50 decided props. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

Props for games kicking off on or after 2026-11-17. n=400, over rate 45.8% of 400.

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| fd_move | 21-8 | 72.4 | 50.9 | 21.5 | +11.05 | 38.1 | 0.79 | -0.03 | 6.9 | keep collecting (29/50) |
| fd_juice | 9-5 | 64.3 | 50.4 | 13.9 | +2.85 | 20.4 | 0.07 | 1.14 | 50.0 | keep collecting (14/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 46-41 | 52.9 | 50.3 | 2.6 | -0.77 | -0.9 |  |  |  | no edge shown yet |
| pin_price | 12-30 | 28.6 | 27.9 | 0.6 | -10.35 | -24.6 |  |  |  | keep collecting (42/50) |
| fd_move | 120-107 | 52.9 | 50.1 | 2.7 | +2.85 | 1.3 |  |  |  | no edge shown yet |
| fd_juice | 63-46 | 57.8 | 50.3 | 7.5 | +5.24 | 4.8 |  |  |  | no edge shown yet |
| pin_lead | 15-7 | 68.2 | 49.9 | 18.3 | +5.97 | 27.1 |  |  |  | keep collecting (22/50) |
| td_steam | 2-19 | 9.5 | 18.0 | -8.5 | -11.0 | -52.4 |  |  |  | keep collecting (21/50) |
| fd_move+pin_value | 8-9 | 47.1 | 50.5 | -3.4 | -1.92 | -11.3 |  |  |  | keep collecting (17/50) |
| pin_lead+pin_value | 7-5 | 58.3 | 49.6 | 8.7 | +0.89 | 7.4 |  |  |  | keep collecting (12/50) |
| fd_juice+pin_price | 2-2 | 50.0 | 49.6 | 0.4 | -0.29 | -7.3 |  |  |  | keep collecting (4/50) |
| fd_move+pin_price | 1-1 | 50.0 | 47.9 | 2.1 | -0.11 | -5.8 |  |  |  | keep collecting (2/50) |
| fd_juice+pin_lead | 1-0 | 100.0 | 49.1 | 50.9 | +0.58 | 58.1 |  |  |  | keep collecting (1/50) |
| fd_juice+pin_value | 1-0 | 100.0 | 49.1 | 50.9 | +0.58 | 58.1 |  |  |  | keep collecting (1/50) |

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
| pin_value | 17-12 | 58.6 | 50.0 | 8.6 | +2.8 | 9.7 | -0.55 | -0.03 | 0.0 | keep collecting (29/50) |
| pin_price | 6-3 | 66.7 | 38.8 | 27.9 | +6.09 | 67.7 | 0.0 | 0.49 | 44.4 | keep collecting (9/50) |
| fd_move | 38-15 | 71.7 | 49.8 | 21.9 | +18.89 | 35.6 | 1.92 | -0.1 | 3.8 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 23-9 | 71.9 | 50.6 | 21.3 | +12.64 | 39.5 | 0.0 | 2.67 | 56.2 | keep collecting (32/50) |
| td_steam | 0-1 | 0.0 | 25.4 | -25.4 | -1.0 | -100.0 | 0.0 | 8.3 | 100.0 | keep collecting (1/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 187-168 | 52.7 | 50.0 | 2.7 | -5.23 | -1.5 |  |  |  | no edge shown yet |
| pin_price | 63-87 | 42.0 | 39.5 | 2.5 | -2.31 | -1.5 |  |  |  | DROP: below break-even |
| fd_move | 360-338 | 51.6 | 50.0 | 1.6 | -11.13 | -1.6 |  |  |  | no edge shown yet |
| fd_juice | 191-148 | 56.3 | 51.4 | 4.9 | +10.32 | 3.0 |  |  |  | no edge shown yet |
| pin_lead | 37-29 | 56.1 | 49.8 | 6.3 | +3.01 | 4.6 |  |  |  | no edge shown yet |
| td_steam | 11-43 | 20.4 | 25.4 | -5.1 | -11.18 | -20.7 |  |  |  | DROP: below break-even |
| pin_lead+pin_value | 25-21 | 54.3 | 50.0 | 4.4 | +0.39 | 0.8 |  |  |  | keep collecting (46/50) |
| fd_juice+pin_price | 7-4 | 63.6 | 52.5 | 11.2 | +1.65 | 15.0 |  |  |  | keep collecting (11/50) |
| fd_move+pin_value | 32-26 | 55.2 | 49.9 | 5.3 | +2.32 | 4.0 |  |  |  | no edge shown yet |
| fd_move+pin_price | 11-8 | 57.9 | 49.1 | 8.8 | +3.37 | 17.8 |  |  |  | keep collecting (19/50) |
| fd_juice+pin_lead | 1-1 | 50.0 | 51.4 | -1.4 | -0.42 | -21.0 |  |  |  | keep collecting (2/50) |
| fd_juice+pin_value | 1-1 | 50.0 | 51.4 | -1.4 | -0.42 | -21.0 |  |  |  | keep collecting (2/50) |

## By Pinnacle limit and by stat (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | pass_tds | 3-2 | 60.0 | 8.3 | -13.7 |
| pin_value | close | pass_yds | 17-17 | 50.0 | -0.9 | -5.8 |
| pin_value | close | pin $1k+ | 121-106 | 53.3 | 3.3 | -0.5 |
| pin_value | close | pin $400-1k | 60-54 | 52.6 | 2.7 | -1.2 |
| pin_value | close | pin limit <$400 | 6-8 | 42.9 | -6.6 | -19.6 |
| pin_value | close | receptions | 6-4 | 60.0 | 11.2 | -2.7 |
| pin_value | close | recv_yds | 106-94 | 53.0 | 3.0 | -0.1 |
| pin_value | close | rush_yds | 55-51 | 51.9 | 2.2 | -2.1 |
| pin_price | close | anytime_td | 19-45 | 29.7 | 4.3 | -5.3 |
| pin_price | close | pass_tds | 4-5 | 44.4 | -10.4 | 2.5 |
| pin_price | close | pass_yds | 3-4 | 42.9 | -7.5 | -19.2 |
| pin_price | close | pin $1k+ | 40-54 | 42.6 | 3.5 | 4.2 |
| pin_price | close | pin $400-1k | 21-30 | 41.2 | 0.9 | -10.8 |
| pin_price | close | pin limit <$400 | 2-3 | 40.0 | 2.4 | -13.8 |
| pin_price | close | receptions | 16-18 | 47.1 | -1.5 | -4.4 |
| pin_price | close | recv_yds | 12-11 | 52.2 | 2.6 | -1.7 |
| pin_price | close | rush_yds | 9-4 | 69.2 | 19.0 | 31.5 |
| fd_move | close | pass_tds | 1-4 | 20.0 | -35.2 | -47.6 |
| fd_move | close | pass_yds | 34-35 | 49.3 | 0.1 | -7.1 |
| fd_move | close | pin $1k+ | 188-183 | 50.7 | 0.7 | -3.5 |
| fd_move | close | pin $400-1k | 127-123 | 50.8 | 0.8 | -2.8 |
| fd_move | close | pin limit <$400 | 15-14 | 51.7 | 1.7 | -1.3 |
| fd_move | close | receptions | 30-31 | 49.2 | -1.3 | 5.7 |
| fd_move | close | recv_yds | 195-183 | 51.6 | 1.6 | -2.8 |
| fd_move | close | rush_yds | 100-85 | 54.1 | 4.0 | 1.7 |
| fd_juice | close | pass_tds | 28-23 | 54.9 | 4.7 | 8.4 |
| fd_juice | close | pin $1k+ | 102-76 | 57.3 | 5.6 | 3.8 |
| fd_juice | close | pin $400-1k | 73-59 | 55.3 | 4.4 | 1.9 |
| fd_juice | close | pin limit <$400 | 4-3 | 57.1 | 4.6 | -0.1 |
| fd_juice | close | receptions | 157-120 | 56.7 | 4.9 | 2.3 |
| fd_juice | close | recv_yds | 2-3 | 40.0 | -10.7 | -29.5 |
| fd_juice | close | rush_yds | 4-2 | 66.7 | 17.5 | 17.5 |
| pin_lead | close | pass_tds | 1-1 | 50.0 | -8.7 | -27.2 |
| pin_lead | close | pass_yds | 5-5 | 50.0 | 0.5 | -5.7 |
| pin_lead | close | pin $1k+ | 28-16 | 63.6 | 13.8 | 18.3 |
| pin_lead | close | pin $400-1k | 9-13 | 40.9 | -8.9 | -22.9 |
| pin_lead | close | receptions | 1-0 | 100.0 | 56.0 | 58.1 |
| pin_lead | close | recv_yds | 19-13 | 59.4 | 9.5 | 11.9 |
| pin_lead | close | rush_yds | 11-10 | 52.4 | 3.2 | -1.3 |
| td_steam | close | anytime_td | 11-43 | 20.4 | -5.1 | -20.7 |
| td_steam | close | pin $1k+ | 2-6 | 25.0 | -0.4 | -53.2 |
| td_steam | close | pin $400-1k | 1-1 | 50.0 | 24.6 | -27.2 |
| td_steam | close | pin limit <$400 | 1-1 | 50.0 | 24.6 | -33.4 |
| pin_lead+pin_value | close | pass_tds | 1-1 | 50.0 | -8.7 | -27.2 |
| fd_juice+pin_lead | close | pass_tds | 0-1 | 0.0 | -58.7 | -100.0 |
| fd_juice+pin_value | close | pass_tds | 0-1 | 0.0 | -58.7 | -100.0 |
| fd_juice+pin_price | close | pass_tds | 0-1 | 0.0 | -41.3 | -100.0 |
| pin_lead+pin_value | close | pass_yds | 4-3 | 57.1 | 7.5 | 7.7 |
| fd_move+pin_price | close | pass_yds | 1-1 | 50.0 | 2.4 | -5.8 |
| fd_move+pin_value | close | pass_yds | 3-3 | 50.0 | 0.0 | -5.8 |
| pin_lead+pin_value | close | pin $1k+ | 19-12 | 61.3 | 11.3 | 13.2 |
| fd_juice+pin_price | close | pin $1k+ | 4-2 | 66.7 | 15.1 | 20.7 |
| fd_move+pin_value | close | pin $1k+ | 17-17 | 50.0 | 0.2 | -5.7 |
| fd_move+pin_price | close | pin $1k+ | 6-5 | 54.5 | 5.2 | 2.8 |
| fd_juice+pin_lead | close | pin $1k+ | 1-0 | 100.0 | 56.0 | 58.1 |
| fd_juice+pin_value | close | pin $1k+ | 1-0 | 100.0 | 56.0 | 58.1 |
| pin_lead+pin_value | close | pin $400-1k | 6-9 | 40.0 | -9.9 | -24.6 |
| fd_move+pin_price | close | pin $400-1k | 4-1 | 80.0 | 29.5 | 78.1 |
| fd_juice+pin_price | close | pin $400-1k | 3-2 | 60.0 | 6.4 | 8.1 |
| fd_move+pin_value | close | pin $400-1k | 13-8 | 61.9 | 11.9 | 16.7 |
| fd_juice+pin_lead | close | pin $400-1k | 0-1 | 0.0 | -58.7 | -100.0 |
| fd_juice+pin_value | close | pin $400-1k | 0-1 | 0.0 | -58.7 | -100.0 |
| fd_move+pin_price | close | pin limit <$400 | 1-2 | 33.3 | -12.5 | -28.0 |
| fd_move+pin_value | close | pin limit <$400 | 2-1 | 66.7 | 16.9 | 25.7 |
| fd_juice+pin_price | close | receptions | 7-3 | 70.0 | 16.4 | 26.5 |
| fd_move+pin_price | close | receptions | 2-2 | 50.0 | 3.0 | 35.2 |
| fd_juice+pin_lead | close | receptions | 1-0 | 100.0 | 56.0 | 58.1 |
| fd_juice+pin_value | close | receptions | 1-0 | 100.0 | 56.0 | 58.1 |
| pin_lead+pin_value | close | receptions | 1-0 | 100.0 | 56.0 | 58.1 |
| pin_lead+pin_value | close | recv_yds | 14-11 | 56.0 | 6.0 | 5.6 |
| fd_move+pin_value | close | recv_yds | 18-15 | 54.5 | 4.7 | 2.8 |
| fd_move+pin_price | close | recv_yds | 5-5 | 50.0 | 0.3 | -5.7 |
| fd_move+pin_value | close | rush_yds | 11-8 | 57.9 | 8.0 | 9.1 |
| pin_lead+pin_value | close | rush_yds | 5-6 | 45.5 | -3.5 | -14.3 |
| fd_move+pin_price | close | rush_yds | 3-0 | 100.0 | 49.2 | 88.5 |
| pin_value | early | pass_yds | 1-1 | 50.0 | -2.4 | -5.8 |
| pin_value | early | pin $1k+ | 16-7 | 69.6 | 19.6 | 30.1 |
| pin_value | early | pin $400-1k | 0-1 | 0.0 | -49.3 | -100.0 |
| pin_value | early | pin limit <$400 | 1-4 | 20.0 | -30.8 | -62.5 |
| pin_value | early | receptions | 1-0 | 100.0 | 44.0 | 64.9 |
| pin_value | early | recv_yds | 8-6 | 57.1 | 7.1 | 7.7 |
| pin_value | early | rush_yds | 7-5 | 58.3 | 9.1 | 9.9 |
| pin_price | early | anytime_td | 2-2 | 50.0 | 24.6 | 82.5 |
| pin_price | early | pin $1k+ | 6-1 | 85.7 | 45.7 | 115.6 |
| pin_price | early | pin $400-1k | 0-2 | 0.0 | -34.7 | -100.0 |
| pin_price | early | receptions | 3-1 | 75.0 | 25.0 | 41.3 |
| pin_price | early | rush_yds | 1-0 | 100.0 | 52.4 | 114.0 |
| fd_move | early | pass_yds | 5-2 | 71.4 | 22.5 | 34.1 |
| fd_move | early | pin limit <$400 | 2-1 | 66.7 | 15.9 | 25.1 |
| fd_move | early | receptions | 1-1 | 50.0 | 6.0 | 22.0 |
| fd_move | early | recv_yds | 20-8 | 71.4 | 21.5 | 34.1 |
| fd_move | early | rush_yds | 12-4 | 75.0 | 24.4 | 40.8 |
| fd_juice | early | pass_tds | 4-0 | 100.0 | 50.0 | 102.5 |
| fd_juice | early | receptions | 18-9 | 66.7 | 16.0 | 28.8 |
| fd_juice | early | recv_yds | 1-0 | 100.0 | 49.3 | 76.9 |
| td_steam | early | anytime_td | 0-1 | 0.0 | -25.4 | -100.0 |
