# NFL prop scorecard

Generated 2026-11-28 15:15 UTC. 1516 graded props (181 had no nflverse result and are not graded).

## Read this first: fit vs forward

**890 props before 2026-11-17 (fit) · 626 on or after it (forward).**

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

Base rate: the over hit **43.7%** of 1516 graded props, but `expected %`
uses **each stat's own rate**, not that pooled one. A yardage over is near a coin
flip; an anytime-TD over 0.5 is a longshot. Scored against one pooled number every
anytime-TD signal would be charged an expectation it could never meet:

- **recv_yds**: over hit 47.7% of 518
- **receptions**: over hit 43.4% of 415
- **rush_yds**: over hit 48.3% of 263
- **anytime_td**: over hit 21.6% of 153
- **pass_yds**: over hit 51.1% of 94
- **pass_tds**: over hit 37.0% of 73

Proposals appear at 50 decided props. Nothing changes automatically.

# FORWARD (out-of-sample — this is the evidence)

Props for games kicking off on or after 2026-11-17. n=626, over rate 41.9% of 626.

## EARLY  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 1-1 | 50.0 | 46.3 | 3.7 | -0.12 | -6.2 | -1.0 | -0.1 | 0.0 | keep collecting (2/50) |
| pin_price | 1-2 | 33.3 | 40.9 | -7.6 | -1.02 | -34.0 | 0.0 | 3.6 | 66.7 | keep collecting (3/50) |
| fd_move | 23-10 | 69.7 | 49.5 | 20.1 | +10.81 | 32.8 | 0.82 | -0.05 | 6.1 | keep collecting (33/50) |
| fd_juice | 11-6 | 64.7 | 51.8 | 12.9 | +3.27 | 19.3 | 0.06 | 1.16 | 52.9 | keep collecting (17/50) |

## CLOSE  (fwd)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 80-72 | 52.6 | 50.6 | 2.1 | -1.51 | -1.0 |  |  |  | no edge shown yet |
| pin_price | 17-64 | 21.0 | 23.9 | -2.9 | -35.97 | -44.4 |  |  |  | DROP: below break-even |
| fd_move | 180-161 | 52.8 | 50.0 | 2.8 | +2.04 | 0.6 |  |  |  | no edge shown yet |
| fd_juice | 102-71 | 59.0 | 51.7 | 7.3 | +9.42 | 5.4 |  |  |  | PROMOTE: beats break-even and its own base rate |
| pin_lead | 21-12 | 63.6 | 50.1 | 13.5 | +6.28 | 19.0 |  |  |  | keep collecting (33/50) |
| td_steam | 4-22 | 15.4 | 14.1 | 1.3 | -12.77 | -49.1 |  |  |  | keep collecting (26/50) |
| fd_move+pin_value | 20-14 | 58.8 | 50.7 | 8.2 | +3.7 | 10.9 |  |  |  | keep collecting (34/50) |
| pin_lead+pin_value | 12-9 | 57.1 | 50.9 | 6.3 | +1.32 | 6.3 |  |  |  | keep collecting (21/50) |
| fd_juice+pin_price | 2-2 | 50.0 | 49.6 | 0.4 | -0.29 | -7.3 |  |  |  | keep collecting (4/50) |
| fd_move+pin_price | 1-2 | 33.3 | 46.5 | -13.2 | -1.11 | -37.2 |  |  |  | keep collecting (3/50) |
| fd_juice+pin_lead | 1-1 | 50.0 | 46.6 | 3.4 | -0.42 | -21.0 |  |  |  | keep collecting (2/50) |
| fd_juice+pin_value | 1-1 | 50.0 | 46.6 | 3.4 | -0.42 | -21.0 |  |  |  | keep collecting (2/50) |

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
| pin_price | 7-5 | 58.3 | 39.1 | 19.2 | +5.07 | 42.3 | 0.0 | 1.27 | 50.0 | keep collecting (12/50) |
| fd_move | 40-17 | 70.2 | 49.6 | 20.6 | +18.65 | 32.7 | 1.86 | -0.11 | 3.5 | PROMOTE: beats break-even and its own base rate |
| fd_juice | 25-10 | 71.4 | 50.8 | 20.6 | +13.07 | 37.3 | 0.0 | 2.55 | 57.1 | keep collecting (35/50) |
| td_steam | 0-1 | 0.0 | 21.6 | -21.6 | -1.0 | -100.0 | 0.0 | 8.3 | 100.0 | keep collecting (1/50) |

## CLOSE  (pooled)

| signal | record | hit % | expected % | edge | units | ROI % | CLV pts | CLV price | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_value | 221-199 | 52.6 | 49.9 | 2.7 | -5.97 | -1.4 |  |  |  | no edge shown yet |
| pin_price | 68-121 | 36.0 | 35.8 | 0.2 | -27.93 | -14.8 |  |  |  | DROP: below break-even |
| fd_move | 420-392 | 51.7 | 50.1 | 1.6 | -11.94 | -1.5 |  |  |  | no edge shown yet |
| fd_juice | 230-173 | 57.1 | 51.8 | 5.3 | +14.5 | 3.6 |  |  |  | PROMOTE: beats break-even and its own base rate |
| pin_lead | 43-34 | 55.8 | 50.0 | 5.9 | +3.32 | 4.3 |  |  |  | no edge shown yet |
| td_steam | 13-46 | 22.0 | 21.6 | 0.5 | -12.95 | -22.0 |  |  |  | DROP: below break-even |
| pin_lead+pin_value | 30-25 | 54.5 | 50.3 | 4.2 | +0.82 | 1.5 |  |  |  | no edge shown yet |
| fd_juice+pin_price | 7-4 | 63.6 | 52.4 | 11.2 | +1.65 | 15.0 |  |  |  | keep collecting (11/50) |
| fd_move+pin_value | 44-31 | 58.7 | 49.8 | 8.8 | +7.94 | 10.6 |  |  |  | no edge shown yet |
| fd_move+pin_price | 11-9 | 55.0 | 48.5 | 6.5 | +2.37 | 11.9 |  |  |  | keep collecting (20/50) |
| fd_juice+pin_lead | 1-2 | 33.3 | 51.6 | -18.2 | -1.42 | -47.3 |  |  |  | keep collecting (3/50) |
| fd_juice+pin_value | 1-2 | 33.3 | 51.6 | -18.2 | -1.42 | -47.3 |  |  |  | keep collecting (3/50) |

## By Pinnacle limit and by stat (pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % |
|---|---|---|---|---|---|---|
| pin_value | close | pass_tds | 3-2 | 60.0 | 7.4 | -13.7 |
| pin_value | close | pass_yds | 19-23 | 45.2 | -5.3 | -14.7 |
| pin_value | close | pin $1k+ | 155-135 | 53.4 | 3.5 | 0.0 |
| pin_value | close | pin $400-1k | 60-56 | 51.7 | 1.7 | -2.9 |
| pin_value | close | pin limit <$400 | 6-8 | 42.9 | -6.6 | -19.6 |
| pin_value | close | receptions | 6-5 | 54.5 | 6.4 | -11.5 |
| pin_value | close | recv_yds | 130-109 | 54.4 | 4.4 | 2.6 |
| pin_value | close | rush_yds | 63-60 | 51.2 | 1.5 | -3.3 |
| pin_price | close | anytime_td | 20-74 | 21.3 | -0.3 | -29.9 |
| pin_price | close | pass_tds | 4-6 | 40.0 | -15.2 | -7.7 |
| pin_price | close | pass_yds | 3-4 | 42.9 | -7.3 | -19.2 |
| pin_price | close | pin $1k+ | 44-80 | 35.5 | 0.2 | -12.5 |
| pin_price | close | pin $400-1k | 22-37 | 37.3 | 0.4 | -18.2 |
| pin_price | close | pin limit <$400 | 2-4 | 33.3 | 0.1 | -28.2 |
| pin_price | close | receptions | 19-20 | 48.7 | -0.4 | -0.8 |
| pin_price | close | recv_yds | 13-12 | 52.0 | 3.6 | -2.0 |
| pin_price | close | rush_yds | 9-5 | 64.3 | 14.3 | 22.1 |
| fd_move | close | pass_tds | 1-5 | 16.7 | -37.7 | -56.3 |
| fd_move | close | pass_yds | 44-36 | 55.0 | 5.3 | 3.7 |
| fd_move | close | pin $1k+ | 243-236 | 50.7 | 0.5 | -3.4 |
| fd_move | close | pin $400-1k | 128-123 | 51.0 | 1.0 | -2.4 |
| fd_move | close | pin limit <$400 | 15-14 | 51.7 | 2.2 | -1.3 |
| fd_move | close | receptions | 34-36 | 48.6 | -2.4 | 4.5 |
| fd_move | close | recv_yds | 227-216 | 51.2 | 1.2 | -3.7 |
| fd_move | close | rush_yds | 114-99 | 53.5 | 3.5 | 0.7 |
| fd_juice | close | pass_tds | 34-26 | 56.7 | 5.4 | 8.2 |
| fd_juice | close | pin $1k+ | 140-100 | 58.3 | 6.2 | 4.7 |
| fd_juice | close | pin $400-1k | 73-60 | 54.9 | 4.0 | 1.1 |
| fd_juice | close | pin limit <$400 | 4-3 | 57.1 | 4.3 | -0.1 |
| fd_juice | close | receptions | 188-139 | 57.5 | 5.6 | 3.6 |
| fd_juice | close | recv_yds | 2-3 | 40.0 | -12.3 | -29.5 |
| fd_juice | close | rush_yds | 6-5 | 54.5 | 4.4 | -6.1 |
| pin_lead | close | pass_tds | 1-1 | 50.0 | -13.0 | -27.2 |
| pin_lead | close | pass_yds | 6-6 | 50.0 | 0.2 | -5.8 |
| pin_lead | close | pin $1k+ | 34-20 | 63.0 | 13.1 | 17.3 |
| pin_lead | close | pin $400-1k | 9-14 | 39.1 | -11.0 | -26.2 |
| pin_lead | close | receptions | 1-0 | 100.0 | 56.6 | 58.1 |
| pin_lead | close | recv_yds | 23-15 | 60.5 | 10.6 | 14.1 |
| pin_lead | close | rush_yds | 12-12 | 50.0 | 0.6 | -5.8 |
| td_steam | close | anytime_td | 13-46 | 22.0 | 0.5 | -22.0 |
| td_steam | close | pin $1k+ | 4-9 | 30.8 | 9.2 | -46.4 |
| td_steam | close | pin $400-1k | 1-1 | 50.0 | 28.4 | -27.2 |
| td_steam | close | pin limit <$400 | 1-1 | 50.0 | 28.4 | -33.4 |
| pin_lead+pin_value | close | pass_tds | 1-1 | 50.0 | -13.0 | -27.2 |
| fd_juice+pin_lead | close | pass_tds | 0-1 | 0.0 | -63.0 | -100.0 |
| fd_juice+pin_value | close | pass_tds | 0-1 | 0.0 | -63.0 | -100.0 |
| fd_juice+pin_price | close | pass_tds | 0-1 | 0.0 | -37.0 | -100.0 |
| pin_lead+pin_value | close | pass_yds | 5-3 | 62.5 | 12.5 | 17.8 |
| fd_move+pin_price | close | pass_yds | 1-1 | 50.0 | 1.1 | -5.8 |
| fd_move+pin_value | close | pass_yds | 4-4 | 50.0 | -0.3 | -5.8 |
| pin_lead+pin_value | close | pin $1k+ | 24-15 | 61.5 | 11.3 | 14.1 |
| fd_juice+pin_price | close | pin $1k+ | 4-2 | 66.7 | 15.5 | 20.7 |
| fd_move+pin_value | close | pin $1k+ | 29-22 | 56.9 | 6.9 | 7.2 |
| fd_move+pin_price | close | pin $1k+ | 6-6 | 50.0 | 1.3 | -5.8 |
| fd_juice+pin_lead | close | pin $1k+ | 1-1 | 50.0 | 4.2 | -21.0 |
| fd_juice+pin_value | close | pin $1k+ | 1-1 | 50.0 | 4.2 | -21.0 |
| pin_lead+pin_value | close | pin $400-1k | 6-10 | 37.5 | -13.2 | -29.3 |
| fd_move+pin_price | close | pin $400-1k | 4-1 | 80.0 | 29.7 | 78.1 |
| fd_juice+pin_price | close | pin $400-1k | 3-2 | 60.0 | 6.0 | 8.1 |
| fd_move+pin_value | close | pin $400-1k | 13-8 | 61.9 | 12.3 | 16.7 |
| fd_juice+pin_lead | close | pin $400-1k | 0-1 | 0.0 | -63.0 | -100.0 |
| fd_juice+pin_value | close | pin $400-1k | 0-1 | 0.0 | -63.0 | -100.0 |
| fd_move+pin_price | close | pin limit <$400 | 1-2 | 33.3 | -11.5 | -28.0 |
| fd_move+pin_value | close | pin limit <$400 | 2-1 | 66.7 | 17.4 | 25.7 |
| fd_juice+pin_price | close | receptions | 7-3 | 70.0 | 16.0 | 26.5 |
| fd_move+pin_price | close | receptions | 2-3 | 40.0 | -6.0 | 8.2 |
| fd_juice+pin_lead | close | receptions | 1-0 | 100.0 | 56.6 | 58.1 |
| fd_juice+pin_value | close | receptions | 1-0 | 100.0 | 56.6 | 58.1 |
| pin_lead+pin_value | close | receptions | 1-0 | 100.0 | 56.6 | 58.1 |
| pin_lead+pin_value | close | recv_yds | 17-13 | 56.7 | 6.4 | 6.8 |
| fd_move+pin_value | close | recv_yds | 28-18 | 60.9 | 11.1 | 14.7 |
| fd_move+pin_price | close | recv_yds | 5-5 | 50.0 | 0.9 | -5.7 |
| fd_move+pin_value | close | rush_yds | 12-9 | 57.1 | 7.4 | 7.7 |
| pin_lead+pin_value | close | rush_yds | 6-8 | 42.9 | -6.4 | -19.2 |
| fd_move+pin_price | close | rush_yds | 3-0 | 100.0 | 49.4 | 88.5 |
| fd_juice+pin_lead | close | rush_yds | 0-1 | 0.0 | -48.3 | -100.0 |
| fd_juice+pin_value | close | rush_yds | 0-1 | 0.0 | -48.3 | -100.0 |
| pin_value | early | pass_yds | 1-1 | 50.0 | -1.1 | -5.8 |
| pin_value | early | pin $1k+ | 16-8 | 66.7 | 16.8 | 24.7 |
| pin_value | early | pin $400-1k | 0-1 | 0.0 | -47.7 | -100.0 |
| pin_value | early | pin limit <$400 | 2-4 | 33.3 | -17.2 | -37.4 |
| pin_value | early | receptions | 1-0 | 100.0 | 43.4 | 64.9 |
| pin_value | early | recv_yds | 9-7 | 56.2 | 6.5 | 6.0 |
| pin_value | early | rush_yds | 7-5 | 58.3 | 8.9 | 9.9 |
| pin_price | early | anytime_td | 2-3 | 40.0 | 18.4 | 46.0 |
| pin_price | early | pin $1k+ | 6-1 | 85.7 | 47.2 | 115.6 |
| pin_price | early | pin $400-1k | 0-3 | 0.0 | -28.8 | -100.0 |
| pin_price | early | pin limit <$400 | 1-1 | 50.0 | -6.6 | -1.0 |
| pin_price | early | receptions | 4-2 | 66.7 | 14.5 | 27.2 |
| pin_price | early | rush_yds | 1-0 | 100.0 | 51.7 | 114.0 |
| fd_move | early | pass_yds | 5-2 | 71.4 | 21.9 | 34.1 |
| fd_move | early | pin limit <$400 | 2-1 | 66.7 | 16.1 | 25.1 |
| fd_move | early | receptions | 1-1 | 50.0 | 6.6 | 22.0 |
| fd_move | early | recv_yds | 22-9 | 71.0 | 21.3 | 33.2 |
| fd_move | early | rush_yds | 12-5 | 70.6 | 20.3 | 32.5 |
| fd_juice | early | pass_tds | 4-0 | 100.0 | 50.0 | 102.5 |
| fd_juice | early | receptions | 20-10 | 66.7 | 15.8 | 27.3 |
| fd_juice | early | recv_yds | 1-0 | 100.0 | 47.7 | 76.9 |
| td_steam | early | anytime_td | 0-1 | 0.0 | -21.6 | -100.0 |
