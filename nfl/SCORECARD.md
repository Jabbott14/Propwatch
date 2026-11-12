# NFL scorecard

Generated 2026-11-12 05:23 UTC. 28 graded games (0 finished games had no final score and are not graded).

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before kickoff. Break-even at -110 is 52.4%. CLV = points of
closing-line value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured on
this sample. `edge` is hit% minus that. A signal that is structurally long dogs or
unders will beat 50% in any week dogs or unders run, which is not an edge --
this sample ran **67.9% favourites** (n=28)
and **50.0% overs** (n=28).

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

**Gate B is these signals. Gate A is the Pinnacle columns on the board — a price
floor, never a veto.** EV against Pinnacle can essentially never be positive,
because Pinnacle is the fair-value definition. Using it as a veto rejects every
signal this system exists to find. See fault 4 in propwatch-news-vs-coherence.md.

## EARLY

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| follow_move | both | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | -3.0 | 0.0 | keep collecting (1/30) |
| money_level | both | 21-18 | 53.8 | 52.3 | 1.6 | +1.27 | 3.3 | -0.45 | 10.3 | no edge shown yet |
| sharp_gap | both | 20-19 | 51.3 | 53.7 | -2.4 | -0.92 | -2.4 | -0.12 | 23.1 | no edge shown yet |
| money_moving | both | 6-4 | 60.0 | 55.4 | 4.6 | +1.59 | 15.9 | -0.4 | 10.0 | keep collecting (10/30) |
| pin_value | both | 12-6 | 66.7 | 54.0 | 12.7 | +4.68 | 26.0 | -0.25 | 11.1 | keep collecting (18/30) |
| follow_move | total | 0-1 | 0.0 | 50.0 | -50.0 | -1.0 | -100.0 | -3.0 | 0.0 | keep collecting (1/30) |
| money_level | spread | 12-7 | 63.2 | 54.7 | 8.5 | +4.08 | 21.5 | -0.24 | 10.5 | keep collecting (19/30) |
| money_level | total | 9-11 | 45.0 | 50.0 | -5.0 | -2.81 | -14.0 | -0.65 | 10.0 | keep collecting (20/30) |
| sharp_gap | spread | 9-11 | 45.0 | 57.1 | -12.1 | -2.89 | -14.5 | 0.07 | 25.0 | keep collecting (20/30) |
| sharp_gap | total | 11-8 | 57.9 | 50.0 | 7.9 | +1.97 | 10.4 | -0.32 | 21.1 | keep collecting (19/30) |
| money_moving | spread | 4-3 | 57.1 | 57.7 | -0.5 | +0.72 | 10.2 | -0.43 | 14.3 | keep collecting (7/30) |
| money_moving | total | 2-1 | 66.7 | 50.0 | 16.7 | +0.88 | 29.3 | -0.33 | 0.0 | keep collecting (3/30) |
| pin_value | spread | 9-1 | 90.0 | 57.1 | 32.9 | +6.94 | 69.4 | -0.25 | 10.0 | keep collecting (10/30) |
| pin_value | total | 3-5 | 37.5 | 50.0 | -12.5 | -2.26 | -28.2 | -0.25 | 12.5 | keep collecting (8/30) |

## CLOSE

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| follow_move | both | 6-12 | 33.3 | 49.0 | -15.7 | -6.62 | -36.8 |  |  | keep collecting (18/30) |
| rlm | both | 3-10 | 23.1 | 45.9 | -22.8 | -7.31 | -56.2 |  |  | keep collecting (13/30) |
| money_level | both | 30-26 | 53.6 | 53.2 | 0.4 | +1.21 | 2.2 |  |  | no edge shown yet |
| sharp_gap | both | 22-33 | 40.0 | 46.4 | -6.4 | -13.31 | -24.2 |  |  | DROP: below break-even |
| money_moving | both | 17-19 | 47.2 | 45.5 | 1.7 | -3.91 | -10.9 |  |  | no edge shown yet |
| pin_value | both | 17-6 | 73.9 | 52.3 | 21.6 | +8.74 | 38.0 |  |  | keep collecting (23/30) |
| follow_move | spread | 1-8 | 11.1 | 48.0 | -36.9 | -7.09 | -78.8 |  |  | keep collecting (9/30) |
| follow_move | total | 5-4 | 55.6 | 50.0 | 5.6 | +0.47 | 5.2 |  |  | keep collecting (9/30) |
| rlm | spread | 0-7 | 0.0 | 42.3 | -42.3 | -7.0 | -100.0 |  |  | keep collecting (7/30) |
| rlm | total | 3-3 | 50.0 | 50.0 | 0.0 | -0.31 | -5.2 |  |  | keep collecting (6/30) |
| money_level | spread | 16-12 | 57.1 | 56.4 | 0.8 | +2.55 | 9.1 |  |  | keep collecting (28/30) |
| money_level | total | 14-14 | 50.0 | 50.0 | 0.0 | -1.34 | -4.8 |  |  | keep collecting (28/30) |
| sharp_gap | spread | 9-18 | 33.3 | 42.7 | -9.4 | -10.0 | -37.0 |  |  | keep collecting (27/30) |
| sharp_gap | total | 13-15 | 46.4 | 50.0 | -3.6 | -3.31 | -11.8 |  |  | keep collecting (28/30) |
| money_moving | spread | 7-10 | 41.2 | 40.5 | 0.6 | -3.87 | -22.7 |  |  | keep collecting (17/30) |
| money_moving | total | 10-9 | 52.6 | 50.0 | 2.6 | -0.04 | -0.2 |  |  | keep collecting (19/30) |
| pin_value | spread | 10-1 | 90.9 | 54.9 | 36.0 | +7.72 | 70.2 |  |  | keep collecting (11/30) |
| pin_value | total | 7-5 | 58.3 | 50.0 | 8.3 | +1.02 | 8.5 |  |  | keep collecting (12/30) |

## By ticket volume and Pinnacle limit (both markets)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| follow_move | close | 40k+ bets | 6-12 | 33.3 | -15.7 | -36.8 |  |
| follow_move | close | pin $10-50k | 5-4 | 55.6 | 5.6 | 5.2 |  |
| follow_move | close | pin $50k+ | 1-8 | 11.1 | -36.9 | -78.8 |  |
| rlm | close | 40k+ bets | 3-10 | 23.1 | -22.8 | -56.2 |  |
| rlm | close | pin $10-50k | 3-3 | 50.0 | 0.0 | -5.2 |  |
| rlm | close | pin $50k+ | 0-7 | 0.0 | -42.3 | -100.0 |  |
| money_level | close | 40k+ bets | 30-26 | 53.6 | 0.4 | 2.2 |  |
| money_level | close | pin $10-50k | 13-14 | 48.1 | -1.9 | -8.3 |  |
| money_level | close | pin $50k+ | 17-12 | 58.6 | 2.5 | 11.9 |  |
| sharp_gap | close | 40k+ bets | 22-33 | 40.0 | -6.4 | -24.2 |  |
| sharp_gap | close | pin $10-50k | 12-15 | 44.4 | -5.6 | -15.6 |  |
| sharp_gap | close | pin $50k+ | 10-18 | 35.7 | -7.3 | -32.5 |  |
| money_moving | close | 40k+ bets | 17-19 | 47.2 | 1.7 | -10.9 |  |
| money_moving | close | pin $10-50k | 9-9 | 50.0 | 0.0 | -5.3 |  |
| money_moving | close | pin $50k+ | 8-10 | 44.4 | 3.4 | -16.4 |  |
| pin_value | close | 40k+ bets | 17-6 | 73.9 | 21.6 | 38.0 |  |
| pin_value | close | pin $10-50k | 7-5 | 58.3 | 8.3 | 8.5 |  |
| pin_value | close | pin $50k+ | 10-1 | 90.9 | 36.0 | 70.2 |  |
| follow_move | early | <10k bets | 0-1 | 0.0 | -50.0 | -100.0 | -3.0 |
| follow_move | early | pin limit <$10k | 0-1 | 0.0 | -50.0 | -100.0 | -3.0 |
| money_level | early | 10-40k bets | 2-2 | 50.0 | 0.0 | -5.0 | -0.12 |
| money_level | early | 40k+ bets | 2-3 | 40.0 | -17.1 | -24.3 | 0.0 |
| money_level | early | <10k bets | 17-13 | 56.7 | 4.9 | 9.0 | -0.57 |
| money_level | early | pin $10-50k | 10-8 | 55.6 | 3.6 | 7.1 | -0.22 |
| money_level | early | pin $50k+ | 3-1 | 75.0 | 16.1 | 42.3 | -0.12 |
| money_level | early | pin limit <$10k | 8-9 | 47.1 | -4.0 | -10.0 | -0.76 |
| sharp_gap | early | 10-40k bets | 2-2 | 50.0 | -8.9 | -6.8 | 0.12 |
| sharp_gap | early | 40k+ bets | 2-4 | 33.3 | -13.7 | -37.9 | 0.0 |
| sharp_gap | early | <10k bets | 16-13 | 55.2 | 0.9 | 5.6 | -0.17 |
| sharp_gap | early | pin $10-50k | 8-10 | 44.4 | -11.5 | -14.7 | 0.06 |
| sharp_gap | early | pin $50k+ | 2-3 | 40.0 | -13.6 | -26.9 | 0.1 |
| sharp_gap | early | pin limit <$10k | 10-6 | 62.5 | 11.4 | 19.2 | -0.38 |
| money_moving | early | <10k bets | 6-4 | 60.0 | 4.6 | 15.9 | -0.4 |
| money_moving | early | pin $10-50k | 4-2 | 66.7 | 10.7 | 28.6 | -0.5 |
| money_moving | early | pin limit <$10k | 2-2 | 50.0 | -4.5 | -3.0 | -0.25 |
| pin_value | early | 10-40k bets | 1-0 | 100.0 | 32.1 | 82.0 | 0.0 |
| pin_value | early | 40k+ bets | 2-1 | 66.7 | 28.6 | 20.5 | 0.0 |
| pin_value | early | <10k bets | 9-5 | 64.3 | 7.9 | 23.2 | -0.32 |
| pin_value | early | pin $10-50k | 6-2 | 75.0 | 13.8 | 43.8 | -0.31 |
| pin_value | early | pin $50k+ | 3-0 | 100.0 | 56.0 | 81.1 | 0.0 |
| pin_value | early | pin limit <$10k | 3-4 | 42.9 | -7.1 | -17.9 | -0.29 |
