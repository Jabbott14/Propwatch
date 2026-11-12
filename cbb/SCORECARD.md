# CBB scorecard

Generated 2026-11-12 06:28 UTC. 338 graded games (8 finished games had no final score matched and are not graded).

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before tip. Break-even at -110 is 52.4%. CLV = points of closing-line
value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured
on this sample. `edge` is hit% minus that. A signal that is structurally long
favourites or overs beats 50% whenever those run, which is not an edge -- this
sample ran **49.7% favourites** (n=338) and **49.4% overs** (n=338) and **76.2% moneyline favourites** (n=282).

Moneyline has no handicap: `follow_move` reads price, CLV is percentage points
of implied probability, and `pin_value` is a pure price comparison.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

## EARLY

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| follow_move | both | 143-141 | 50.4 | 49.9 | 0.4 | -10.5 | -3.7 | 0.19 | 39.8 | no edge shown yet |
| money_level | both | 87-50 | 63.5 | 59.5 | 4.0 | +3.49 | 2.5 | 0.39 | 43.8 | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 71-56 | 55.9 | 48.2 | 7.7 | +21.43 | 16.9 | 0.44 | 41.7 | no edge shown yet |
| money_moving | both | 53-33 | 61.6 | 51.5 | 10.1 | +9.53 | 11.1 | 0.1 | 41.9 | PROMOTE: beats break-even and its own base rate |
| pin_value | both | 43-41 | 51.2 | 48.1 | 3.1 | -2.68 | -3.2 | 0.15 | 41.7 | no edge shown yet |
| book_lag | both | 1-4 | 20.0 | 50.2 | -30.2 | -3.09 | -61.8 | -1.0 | 20.0 | keep collecting (5/30) |
| consensus_gap | both | 121-169 | 41.7 | 46.2 | -4.4 | -44.09 | -15.2 | 0.33 | 46.9 | DROP: below break-even |
| follow_move | spread | 68-73 | 48.2 | 49.9 | -1.7 | -11.05 | -7.8 | 0.08 | 36.2 | no edge shown yet |
| follow_move | total | 75-68 | 52.4 | 50.0 | 2.5 | +0.55 | 0.4 | 0.31 | 43.4 | no edge shown yet |
| money_level | moneyline | 41-19 | 68.3 | 71.9 | -3.5 | -7.2 | -12.0 | 0.31 | 50.0 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 15-14 | 51.7 | 49.9 | 1.8 | -0.54 | -1.9 | 0.86 | 44.8 | keep collecting (29/30) |
| money_level | total | 31-17 | 64.6 | 49.8 | 14.8 | +11.22 | 23.4 | 0.21 | 35.4 | PROMOTE: beats break-even and its own base rate |
| sharp_gap | moneyline | 28-23 | 54.9 | 45.4 | 9.5 | +15.41 | 30.2 | 0.5 | 52.9 | no edge shown yet |
| sharp_gap | spread | 16-14 | 53.3 | 50.0 | 3.3 | +0.41 | 1.4 | 0.63 | 33.3 | no edge shown yet |
| sharp_gap | total | 27-19 | 58.7 | 50.1 | 8.6 | +5.61 | 12.2 | 0.24 | 34.8 | no edge shown yet |
| money_moving | moneyline | 20-17 | 54.1 | 53.5 | 0.5 | -4.28 | -11.6 | 0.13 | 56.8 | no edge shown yet |
| money_moving | spread | 15-4 | 78.9 | 49.9 | 29.0 | +9.42 | 49.6 | 0.21 | 36.8 | keep collecting (19/30) |
| money_moving | total | 18-12 | 60.0 | 50.0 | 10.0 | +4.39 | 14.6 | 0.0 | 26.7 | no edge shown yet |
| pin_value | moneyline | 1-5 | 16.7 | 23.8 | -7.1 | -4.02 | -67.0 | -0.02 | 66.7 | keep collecting (6/30) |
| pin_value | spread | 22-17 | 56.4 | 49.9 | 6.5 | +2.35 | 6.0 | 0.28 | 41.0 | no edge shown yet |
| pin_value | total | 20-19 | 51.3 | 50.0 | 1.3 | -1.01 | -2.6 | 0.05 | 38.5 | no edge shown yet |
| book_lag | spread | 1-2 | 33.3 | 50.3 | -17.0 | -1.09 | -36.4 | -1.67 | 0.0 | keep collecting (3/30) |
| book_lag | total | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 | 0.0 | 50.0 | keep collecting (2/30) |
| consensus_gap | moneyline | 45-91 | 33.1 | 41.9 | -8.8 | -33.15 | -24.4 | 0.06 | 43.4 | DROP: below break-even |
| consensus_gap | spread | 42-35 | 54.5 | 49.9 | 4.6 | +1.57 | 2.0 | 0.51 | 48.1 | no edge shown yet |
| consensus_gap | total | 34-43 | 44.2 | 49.9 | -5.8 | -12.5 | -16.2 | 0.62 | 51.9 | no edge shown yet |

## CLOSE

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| follow_move | both | 281-281 | 50.0 | 49.9 | 0.1 | -26.9 | -4.8 |  |  | no edge shown yet |
| money_level | both | 525-395 | 57.1 | 56.4 | 0.7 | -43.92 | -4.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 392-498 | 44.0 | 46.5 | -2.4 | -74.6 | -8.4 |  |  | DROP: below break-even |
| money_moving | both | 389-501 | 43.7 | 46.9 | -3.2 | -88.0 | -9.9 |  |  | DROP: below break-even |
| pin_value | both | 188-173 | 52.1 | 47.6 | 4.5 | +12.66 | 3.5 |  |  | no edge shown yet |
| book_lag | both | 2-1 | 66.7 | 50.1 | 16.6 | +0.75 | 25.1 |  |  | keep collecting (3/30) |
| consensus_gap | both | 215-295 | 42.2 | 46.6 | -4.4 | -49.11 | -9.6 |  |  | DROP: below break-even |
| follow_move | spread | 128-134 | 48.9 | 49.9 | -1.0 | -19.04 | -7.3 |  |  | no edge shown yet |
| follow_move | total | 153-147 | 51.0 | 50.0 | 1.0 | -7.86 | -2.6 |  |  | no edge shown yet |
| money_level | moneyline | 209-67 | 75.7 | 71.7 | 4.0 | -0.4 | -0.1 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 157-157 | 50.0 | 49.9 | 0.1 | -16.55 | -5.3 |  |  | no edge shown yet |
| money_level | total | 159-171 | 48.2 | 49.8 | -1.6 | -26.97 | -8.2 |  |  | DROP: below break-even |
| sharp_gap | moneyline | 83-172 | 32.5 | 37.8 | -5.2 | -27.69 | -10.9 |  |  | DROP: below break-even |
| sharp_gap | spread | 158-152 | 51.0 | 49.9 | 1.0 | -10.33 | -3.3 |  |  | no edge shown yet |
| sharp_gap | total | 151-174 | 46.5 | 50.0 | -3.6 | -36.58 | -11.3 |  |  | DROP: below break-even |
| money_moving | moneyline | 87-166 | 34.4 | 39.1 | -4.7 | -25.58 | -10.1 |  |  | DROP: below break-even |
| money_moving | spread | 155-155 | 50.0 | 49.9 | 0.1 | -16.2 | -5.2 |  |  | no edge shown yet |
| money_moving | total | 147-180 | 45.0 | 50.0 | -5.1 | -46.22 | -14.1 |  |  | DROP: below break-even |
| pin_value | moneyline | 9-29 | 23.7 | 27.9 | -4.2 | -1.86 | -4.9 |  |  | DROP: below break-even |
| pin_value | spread | 90-60 | 60.0 | 50.0 | 10.0 | +18.61 | 12.4 |  |  | PROMOTE: beats break-even and its own base rate |
| pin_value | total | 89-84 | 51.4 | 49.9 | 1.6 | -4.09 | -2.4 |  |  | no edge shown yet |
| book_lag | spread | 1-0 | 100.0 | 50.3 | 49.7 | +0.88 | 87.7 |  |  | keep collecting (1/30) |
| book_lag | total | 1-1 | 50.0 | 50.0 | 0.0 | -0.12 | -6.2 |  |  | keep collecting (2/30) |
| consensus_gap | moneyline | 82-170 | 32.5 | 43.3 | -10.8 | -40.07 | -15.9 |  |  | DROP: below break-even |
| consensus_gap | spread | 63-48 | 56.8 | 49.9 | 6.9 | +5.82 | 5.2 |  |  | no edge shown yet |
| consensus_gap | total | 70-77 | 47.6 | 49.7 | -2.1 | -14.85 | -10.1 |  |  | no edge shown yet |

## By market depth (both markets)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| follow_move | close | 1-3k bets | 188-178 | 51.4 | 1.5 | -2.2 |  |
| follow_move | close | 3k+ bets | 60-70 | 46.2 | -3.8 | -12.1 |  |
| follow_move | close | <1k bets | 33-33 | 50.0 | 0.1 | -4.9 |  |
| follow_move | close | pin $1-2k | 91-113 | 44.6 | -5.3 | -15.1 |  |
| follow_move | close | pin $2k+ | 48-51 | 48.5 | -1.4 | -7.8 |  |
| follow_move | close | pin limit <$1k | 64-53 | 54.7 | 4.6 | 4.6 |  |
| money_level | close | 1-3k bets | 358-227 | 61.2 | 4.6 | 2.5 |  |
| money_level | close | 3k+ bets | 111-105 | 51.4 | -4.4 | -12.4 |  |
| money_level | close | <1k bets | 56-62 | 47.5 | -9.1 | -26.1 |  |
| money_level | close | pin $1-2k | 148-138 | 51.7 | -2.8 | -8.3 |  |
| money_level | close | pin $2k+ | 126-93 | 57.5 | -0.8 | -6.7 |  |
| money_level | close | pin limit <$1k | 64-68 | 48.5 | -1.9 | -8.2 |  |
| sharp_gap | close | 1-3k bets | 247-320 | 43.6 | -3.1 | -11.3 |  |
| sharp_gap | close | 3k+ bets | 96-116 | 45.3 | -0.6 | 2.9 |  |
| sharp_gap | close | <1k bets | 49-61 | 44.5 | -2.6 | -14.4 |  |
| sharp_gap | close | pin $1-2k | 133-146 | 47.7 | -0.4 | -1.4 |  |
| sharp_gap | close | pin $2k+ | 79-131 | 37.6 | -7.4 | -25.5 |  |
| sharp_gap | close | pin limit <$1k | 60-66 | 47.6 | -2.1 | -1.8 |  |
| money_moving | close | 1-3k bets | 245-321 | 43.3 | -3.6 | -12.5 |  |
| money_moving | close | 3k+ bets | 95-119 | 44.4 | -2.3 | -0.7 |  |
| money_moving | close | <1k bets | 49-60 | 45.0 | -2.4 | -13.6 |  |
| money_moving | close | pin $1-2k | 128-151 | 45.9 | -2.4 | -5.0 |  |
| money_moving | close | pin $2k+ | 82-127 | 39.2 | -5.9 | -22.8 |  |
| money_moving | close | pin limit <$1k | 59-68 | 46.5 | -3.2 | -4.0 |  |
| pin_value | close | 1-3k bets | 115-116 | 49.8 | 2.2 | -1.8 |  |
| pin_value | close | 3k+ bets | 40-43 | 48.2 | 0.5 | -1.8 |  |
| pin_value | close | <1k bets | 33-14 | 70.2 | 22.5 | 39.1 |  |
| pin_value | close | pin $1-2k | 90-82 | 52.3 | 4.5 | 3.7 |  |
| pin_value | close | pin $2k+ | 48-50 | 49.0 | 3.6 | -1.8 |  |
| pin_value | close | pin limit <$1k | 50-41 | 54.9 | 5.4 | 9.0 |  |
| book_lag | close | 1-3k bets | 1-1 | 50.0 | 0.0 | -6.2 |  |
| book_lag | close | 3k+ bets | 1-0 | 100.0 | 49.7 | 87.7 |  |
| book_lag | close | pin $1-2k | 1-0 | 100.0 | 49.7 | 87.7 |  |
| book_lag | close | pin limit <$1k | 1-1 | 50.0 | 0.0 | -6.2 |  |
| consensus_gap | close | 1-3k bets | 135-183 | 42.5 | -4.5 | -12.0 |  |
| consensus_gap | close | 3k+ bets | 54-64 | 45.8 | -2.1 | 8.4 |  |
| consensus_gap | close | <1k bets | 26-47 | 35.6 | -7.5 | -27.3 |  |
| consensus_gap | close | pin $1-2k | 70-79 | 47.0 | -1.0 | 3.1 |  |
| consensus_gap | close | pin $2k+ | 52-63 | 45.2 | -6.1 | -20.6 |  |
| consensus_gap | close | pin limit <$1k | 34-31 | 52.3 | 2.7 | 4.3 |  |
| follow_move | early | 1-3k bets | 15-16 | 48.4 | -1.5 | -7.7 | -0.1 |
| follow_move | early | 3k+ bets | 0-2 | 0.0 | -49.9 | -100.0 | -0.5 |
| follow_move | early | <1k bets | 115-109 | 51.3 | 1.4 | -1.8 | 0.25 |
| follow_move | early | pin $1-2k | 10-8 | 55.6 | 5.6 | 5.0 | -0.06 |
| follow_move | early | pin limit <$1k | 33-29 | 53.2 | 3.4 | 1.1 | -0.35 |
| money_level | early | 1-3k bets | 26-20 | 56.5 | 0.1 | -6.8 | 0.05 |
| money_level | early | 3k+ bets | 3-0 | 100.0 | 41.2 | 59.7 | 0.33 |
| money_level | early | <1k bets | 58-30 | 65.9 | 4.8 | 5.5 | 0.57 |
| money_level | early | pin $1-2k | 14-8 | 63.6 | -1.8 | -3.2 | 0.01 |
| money_level | early | pin limit <$1k | 22-24 | 47.8 | -6.2 | -12.1 | 0.31 |
| sharp_gap | early | 1-3k bets | 25-21 | 54.3 | 8.2 | 20.4 | 0.03 |
| sharp_gap | early | 3k+ bets | 2-1 | 66.7 | 7.6 | -1.4 | -0.33 |
| sharp_gap | early | <1k bets | 44-34 | 56.4 | 7.5 | 15.5 | 0.71 |
| sharp_gap | early | pin $1-2k | 11-9 | 55.0 | 3.6 | 13.8 | -0.57 |
| sharp_gap | early | pin limit <$1k | 27-16 | 62.8 | 14.5 | 30.8 | 0.2 |
| money_moving | early | 1-3k bets | 22-11 | 66.7 | 17.4 | 32.6 | 0.16 |
| money_moving | early | 3k+ bets | 2-0 | 100.0 | 49.9 | 89.2 | 0.5 |
| money_moving | early | <1k bets | 29-22 | 56.9 | 3.9 | -5.9 | 0.05 |
| money_moving | early | pin $1-2k | 6-6 | 50.0 | -13.1 | -26.9 | 0.35 |
| money_moving | early | pin limit <$1k | 20-9 | 69.0 | 19.8 | 47.8 | 0.36 |
| pin_value | early | 1-3k bets | 12-9 | 57.1 | 8.4 | 7.7 | -0.05 |
| pin_value | early | 3k+ bets | 1-0 | 100.0 | 50.3 | 83.3 | 1.0 |
| pin_value | early | <1k bets | 30-32 | 48.4 | 0.6 | -8.3 | 0.21 |
| pin_value | early | pin $1-2k | 11-14 | 44.0 | -0.7 | -16.7 | 0.17 |
| pin_value | early | pin limit <$1k | 32-27 | 54.2 | 4.7 | 2.5 | 0.15 |
| book_lag | early | 1-3k bets | 0-1 | 0.0 | -49.4 | -100.0 | -1.0 |
| book_lag | early | <1k bets | 1-3 | 25.0 | -25.4 | -52.3 | -1.0 |
| book_lag | early | pin limit <$1k | 0-2 | 0.0 | -50.0 | -100.0 | 0.0 |
| consensus_gap | early | 1-3k bets | 9-16 | 36.0 | -11.8 | -21.4 | 0.04 |
| consensus_gap | early | 3k+ bets | 1-1 | 50.0 | 13.3 | -8.4 | 0.5 |
| consensus_gap | early | <1k bets | 96-135 | 41.6 | -4.4 | -15.9 | 0.32 |
| consensus_gap | early | pin $1-2k | 10-16 | 38.5 | -7.5 | -24.8 | 0.47 |
| consensus_gap | early | pin limit <$1k | 17-32 | 34.7 | -16.3 | -27.7 | 0.33 |
