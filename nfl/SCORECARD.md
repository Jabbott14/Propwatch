# NFL scorecard

Generated 2026-11-12 06:03 UTC. 28 graded games (0 finished games had no final score and are not graded).

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before kickoff. Break-even at -110 is 52.4%. CLV = points of
closing-line value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured on
this sample. `edge` is hit% minus that. A signal that is structurally long dogs or
unders will beat 50% in any week dogs or unders run, which is not an edge --
this sample ran **67.9% favourites** (n=28)
**50.0% overs** (n=28) and **82.1% moneyline favourites** (n=28).

Moneyline has no handicap, so its `follow_move` reads price, its CLV is
percentage points of implied probability, and `pin_value` is a pure price
comparison against Pinnacle's no-vig fair -- no half-points involved.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

**Gate B is these signals. Gate A is the Pinnacle columns on the board — a price
floor, never a veto.** EV against Pinnacle can essentially never be positive,
because Pinnacle is the fair-value definition. Using it as a veto rejects every
signal this system exists to find. See fault 4 in propwatch-news-vs-coherence.md.

## EARLY

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| follow_move | both | 1-2 | 33.3 | 50.0 | -16.7 | -1.44 | -47.9 | -1.87 | 33.3 | keep collecting (3/30) |
| rlm | both | 0-1 | 0.0 | 17.9 | -17.9 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| money_level | both | 37-21 | 63.8 | 61.0 | 2.8 | +4.26 | 7.3 | -0.81 | 15.5 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 30-29 | 50.8 | 51.3 | -0.5 | -5.24 | -8.9 | -0.1 | 28.8 | no edge shown yet |
| money_moving | both | 10-6 | 62.5 | 57.4 | 5.1 | +1.61 | 10.1 | -0.23 | 25.0 | keep collecting (16/30) |
| pin_value | both | 12-11 | 52.2 | 46.1 | 6.1 | -0.32 | -1.4 | 0.3 | 30.4 | keep collecting (23/30) |
| follow_move | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.44 | -21.9 | -1.3 | 50.0 | keep collecting (2/30) |
| follow_move | total | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | -3.0 | 0.0 | keep collecting (1/30) |
| rlm | moneyline | 0-1 | 0.0 | 17.9 | -17.9 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| money_level | moneyline | 16-3 | 84.2 | 78.8 | 5.5 | +2.98 | 15.7 | -1.55 | 26.3 | keep collecting (19/30) |
| money_level | spread | 12-7 | 63.2 | 54.7 | 8.5 | +4.08 | 21.5 | -0.24 | 10.5 | keep collecting (19/30) |
| money_level | total | 9-11 | 45.0 | 50.0 | -5.0 | -2.81 | -14.0 | -0.65 | 10.0 | keep collecting (20/30) |
| sharp_gap | moneyline | 10-10 | 50.0 | 46.8 | 3.2 | -4.32 | -21.6 | -0.07 | 40.0 | keep collecting (20/30) |
| sharp_gap | spread | 9-11 | 45.0 | 57.1 | -12.1 | -2.89 | -14.5 | 0.07 | 25.0 | keep collecting (20/30) |
| sharp_gap | total | 11-8 | 57.9 | 50.0 | 7.9 | +1.97 | 10.4 | -0.32 | 21.1 | keep collecting (19/30) |
| money_moving | moneyline | 4-2 | 66.7 | 60.7 | 6.0 | +0.02 | 0.3 | 0.07 | 50.0 | keep collecting (6/30) |
| money_moving | spread | 4-3 | 57.1 | 57.7 | -0.5 | +0.72 | 10.2 | -0.43 | 14.3 | keep collecting (7/30) |
| money_moving | total | 2-1 | 66.7 | 50.0 | 16.7 | +0.88 | 29.3 | -0.33 | 0.0 | keep collecting (3/30) |
| pin_value | moneyline | 0-5 | 0.0 | 17.9 | -17.9 | -5.0 | -100.0 | 2.28 | 100.0 | keep collecting (5/30) |
| pin_value | spread | 9-1 | 90.0 | 57.1 | 32.9 | +6.94 | 69.4 | -0.25 | 10.0 | keep collecting (10/30) |
| pin_value | total | 3-5 | 37.5 | 50.0 | -12.5 | -2.26 | -28.2 | -0.25 | 12.5 | keep collecting (8/30) |

## CLOSE

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| follow_move | both | 12-26 | 31.6 | 46.1 | -14.6 | -17.97 | -47.3 |  |  | DROP: below break-even |
| rlm | both | 3-22 | 12.0 | 32.4 | -20.4 | -19.31 | -77.2 |  |  | keep collecting (25/30) |
| money_level | both | 54-30 | 64.3 | 60.5 | 3.7 | +8.81 | 10.5 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 36-45 | 44.4 | 49.2 | -4.7 | -15.76 | -19.5 |  |  | no edge shown yet |
| money_moving | both | 24-31 | 43.6 | 43.0 | 0.6 | -11.31 | -20.6 |  |  | no edge shown yet |
| pin_value | both | 19-11 | 63.3 | 46.4 | 16.9 | +5.14 | 17.1 |  |  | no edge shown yet |
| follow_move | moneyline | 6-14 | 30.0 | 43.6 | -13.6 | -11.34 | -56.7 |  |  | keep collecting (20/30) |
| follow_move | spread | 1-8 | 11.1 | 48.0 | -36.9 | -7.09 | -78.8 |  |  | keep collecting (9/30) |
| follow_move | total | 5-4 | 55.6 | 50.0 | 5.6 | +0.47 | 5.2 |  |  | keep collecting (9/30) |
| rlm | moneyline | 0-12 | 0.0 | 17.9 | -17.9 | -12.0 | -100.0 |  |  | keep collecting (12/30) |
| rlm | spread | 0-7 | 0.0 | 42.3 | -42.3 | -7.0 | -100.0 |  |  | keep collecting (7/30) |
| rlm | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| money_level | moneyline | 24-4 | 85.7 | 75.3 | 10.5 | +7.6 | 27.1 |  |  | keep collecting (28/30) |
| money_level | spread | 16-12 | 57.1 | 56.4 | 0.8 | +2.55 | 9.1 |  |  | keep collecting (28/30) |
| money_level | total | 14-14 | 50.0 | 50.0 | 0.0 | -1.34 | -4.8 |  |  | keep collecting (28/30) |
| sharp_gap | moneyline | 14-12 | 53.8 | 54.9 | -1.1 | -2.45 | -9.4 |  |  | keep collecting (26/30) |
| sharp_gap | spread | 9-18 | 33.3 | 42.7 | -9.4 | -10.0 | -37.0 |  |  | keep collecting (27/30) |
| sharp_gap | total | 13-15 | 46.4 | 50.0 | -3.6 | -3.31 | -11.8 |  |  | keep collecting (28/30) |
| money_moving | moneyline | 7-12 | 36.8 | 38.2 | -1.3 | -7.4 | -38.9 |  |  | keep collecting (19/30) |
| money_moving | spread | 7-10 | 41.2 | 40.5 | 0.6 | -3.87 | -22.7 |  |  | keep collecting (17/30) |
| money_moving | total | 10-9 | 52.6 | 50.0 | 2.6 | -0.04 | -0.2 |  |  | keep collecting (19/30) |
| pin_value | moneyline | 2-5 | 28.6 | 27.0 | 1.5 | -3.59 | -51.3 |  |  | keep collecting (7/30) |
| pin_value | spread | 10-1 | 90.9 | 54.9 | 36.0 | +7.72 | 70.2 |  |  | keep collecting (11/30) |
| pin_value | total | 7-5 | 58.3 | 50.0 | 8.3 | +1.02 | 8.5 |  |  | keep collecting (12/30) |

## By ticket volume and Pinnacle limit (both markets)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| follow_move | close | 40k+ bets | 12-26 | 31.6 | -14.6 | -47.3 |  |
| follow_move | close | pin $10-50k | 7-7 | 50.0 | 2.3 | -13.4 |  |
| follow_move | close | pin $50k+ | 5-19 | 20.8 | -24.4 | -67.0 |  |
| rlm | close | 40k+ bets | 3-22 | 12.0 | -20.4 | -77.2 |  |
| rlm | close | pin $10-50k | 3-6 | 33.3 | -6.0 | -36.8 |  |
| rlm | close | pin $50k+ | 0-16 | 0.0 | -28.6 | -100.0 |  |
| money_level | close | 40k+ bets | 54-30 | 64.3 | 3.7 | 10.5 |  |
| money_level | close | pin $10-50k | 18-14 | 56.2 | 1.2 | -2.8 |  |
| money_level | close | pin $50k+ | 36-16 | 69.2 | 5.3 | 18.7 |  |
| sharp_gap | close | 40k+ bets | 36-45 | 44.4 | -4.7 | -19.5 |  |
| sharp_gap | close | pin $10-50k | 15-16 | 48.4 | -3.7 | -13.8 |  |
| sharp_gap | close | pin $50k+ | 21-29 | 42.0 | -5.4 | -23.0 |  |
| money_moving | close | 40k+ bets | 24-31 | 43.6 | 0.6 | -20.6 |  |
| money_moving | close | pin $10-50k | 11-11 | 50.0 | 0.0 | -9.9 |  |
| money_moving | close | pin $50k+ | 13-20 | 39.4 | 1.1 | -27.6 |  |
| pin_value | close | 40k+ bets | 19-11 | 63.3 | 16.9 | 17.1 |  |
| pin_value | close | pin $10-50k | 7-7 | 50.0 | 4.6 | -7.0 |  |
| pin_value | close | pin $50k+ | 12-4 | 75.0 | 27.7 | 38.3 |  |
| follow_move | early | <10k bets | 1-2 | 33.3 | -16.7 | -47.9 | -1.87 |
| follow_move | early | pin limit <$10k | 1-2 | 33.3 | -16.7 | -47.9 | -1.87 |
| rlm | early | <10k bets | 0-1 | 0.0 | -17.9 | -100.0 | 0.5 |
| rlm | early | pin limit <$10k | 0-1 | 0.0 | -17.9 | -100.0 | 0.5 |
| money_level | early | 10-40k bets | 3-3 | 50.0 | -10.7 | -13.8 | -0.28 |
| money_level | early | 40k+ bets | 4-4 | 50.0 | -16.5 | -19.9 | -0.06 |
| money_level | early | <10k bets | 30-14 | 68.2 | 8.2 | 15.2 | -1.02 |
| money_level | early | pin $10-50k | 11-9 | 55.0 | 0.0 | 2.8 | -0.18 |
| money_level | early | pin $50k+ | 5-2 | 71.4 | 2.6 | 20.1 | -0.36 |
| money_level | early | pin limit <$10k | 21-10 | 67.7 | 4.7 | 7.4 | -1.32 |
| sharp_gap | early | 10-40k bets | 3-3 | 50.0 | 4.8 | 3.1 | 0.27 |
| sharp_gap | early | 40k+ bets | 4-5 | 44.4 | -14.3 | -29.5 | -0.06 |
| sharp_gap | early | <10k bets | 23-21 | 52.3 | 1.6 | -6.3 | -0.16 |
| sharp_gap | early | pin $10-50k | 10-10 | 50.0 | -5.4 | -4.6 | -0.03 |
| sharp_gap | early | pin $50k+ | 3-5 | 37.5 | -18.8 | -37.5 | 0.33 |
| sharp_gap | early | pin limit <$10k | 17-14 | 54.8 | 7.4 | -4.3 | -0.26 |
| money_moving | early | <10k bets | 10-6 | 62.5 | 5.1 | 10.1 | -0.23 |
| money_moving | early | pin $10-50k | 4-2 | 66.7 | 10.7 | 28.6 | -0.5 |
| money_moving | early | pin limit <$10k | 6-4 | 60.0 | 1.8 | -1.1 | -0.06 |
| pin_value | early | 10-40k bets | 1-0 | 100.0 | 32.1 | 82.0 | 0.0 |
| pin_value | early | 40k+ bets | 2-1 | 66.7 | 28.6 | 20.5 | 0.0 |
| pin_value | early | <10k bets | 9-10 | 47.4 | 1.1 | -9.2 | 0.36 |
| pin_value | early | pin $10-50k | 6-2 | 75.0 | 13.8 | 43.8 | -0.31 |
| pin_value | early | pin $50k+ | 3-0 | 100.0 | 56.0 | 81.1 | 0.0 |
| pin_value | early | pin limit <$10k | 3-9 | 25.0 | -11.6 | -52.1 | 0.78 |
