# NFL board

Generated 2026-11-17 22:51 UTC. Upcoming games with a FanDuel line, grouped by how many signals
agree on each market. Every game is listed; nothing is cut. Each call shows that
signal's graded CLOSE record so far, so you can see which ones are earning.

`Pin` is Pinnacle's number and the size it will take — **Gate A, a price floor and
a guide to which book to use. It is not a veto.** `gap` is FanDuel minus Pinnacle in
points. `public` names the ticket majority when it is over 60% — when the line has
moved the other way, `rlm` fires.

This is analysis, not picks.

## FLAGGED — reverse line movement with split confirmation

The crowd holds the tickets on the other side, the money on this side is
outsized relative to its ticket count (>= 1.2x), and the number moved
here anyway. Pinnacle tier first: that is the sharp book moving, not a retail
book reacting to its own flow.


`moved` is **that tier's own book** moving — Pinnacle's number for the Pinnacle
tier, FanDuel's for the FanDuel tier. `FD now` is what you would actually be
buying. Those are two different books and this table used to print one next to
the other in a single row.

| tier | game | market | side | book | moved | FD now | tickets | money/tix | record |
|---|---|---|---|---|---|---|---|---|---|
| PINNACLE moved vs public | Baltimore Ravens @ Carolina Panthers | moneyline | away | Pinnacle | 128 -> 124 | 112 | 15% | 2.33 | 5-10 fit · 0-0 fwd |
| PINNACLE moved vs public | Miami Dolphins @ Buffalo Bills | total | under | Pinnacle | 47 -> 45.5 | 45.5 | 19% | 1.21 | 5-10 fit · 0-0 fwd |
| PINNACLE moved vs public | Miami Dolphins @ Buffalo Bills | moneyline | away | Pinnacle | 889 -> 886 | 980 | 2% | 3.5 | 5-10 fit · 0-0 fwd |
| PINNACLE moved vs public | Minnesota Vikings @ San Francisco 49ers | moneyline | away | Pinnacle | 145 -> 145 | 138 | 10% | 4.1 | 5-10 fit · 0-0 fwd |
| FanDuel moved vs public | Arizona Cardinals @ Kansas City Chiefs | moneyline | away | FanDuel | -1500 -> 830 | 830 | 2% | 10.5 | 5-14 fit · 1-0 fwd |
| FanDuel moved vs public | Miami Dolphins @ Buffalo Bills | spread | away | FanDuel | -17 -> 16.5 | 16.5 | 29% | 1.41 | 5-14 fit · 1-0 fwd |
| FanDuel moved vs public | New Orleans Saints @ Chicago Bears | moneyline | away | FanDuel | -670 -> 460 | 460 | 3% | 1.33 | 5-14 fit · 1-0 fwd |

Ranked by **weighted ROI**: each agreeing signal contributes its own return per
unit risked, and contributes nothing until it has 30 decided outcomes. A signal
earns positive weight only if it **both** beats its own base rate and makes
money. Hit-rate edge alone is blind to price — `money_level` on CBB moneylines
beats its base rate by 3.6 points while returning −3.5%, because it lays −880
favourites, and on 2026-11-17 that ranked a −880 chalk first on the board.
Raw agreement count is shown too, but it is the weaker number — a
market can have seven signals agreeing where four of them have losing records.

Each call shows **two** records: `fit` (the games the signal was chosen on —
before 2026-11-17, so a good number there proves nothing) and `fwd` (games
since, which it had no hand in choosing). A `*` means the weight came from the
forward record, which happens once that record reaches 30 decided
outcomes. No asterisk means the lean rests on fitted numbers only.

## A  weighted ROI >= +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | spread | home | +50.7 | 4-1 | -9.5 (-115) | -9.5 |  | -10 ($20,000) | +0.5 |  | 63% / 65% | 2453 | money_level->home (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); book_lag->home (4-0 fit · 0-0 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | spread | home | +40.3 | 4-1 | -15.5 (-115) | -15 | 0.5 | -16 ($20,000) | +0.5 |  | 74% / 65% | 2054 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | spread | home | +36.1 | 5-2 | -7.5 (-115) | -8 | 0.5 | -8 ($20,000) | +0.5 | home 63% | 63% / 67% | 3306 | follow_move->away (15-20 fit · 0-1 fwd); rlm->away (1-11 fit · 0-0 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | spread | home | +35.7 | 2-2 | -11.5 (-110) | -9.5 | 2 | -11.5 ($20,000) |  |  | 83% / 73% | 3180 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | spread | away | +32.7 | 4-2 | 3.5 (-115) | 3 | 0.5 | 3 ($10,000) | -0.5 | away 60% | 60% / 81% | 1650 | follow_move->home (15-20 fit · 0-1 fwd); rlm->home (1-11 fit · 0-0 fwd); money_level->away (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); pin_value->away (15-3 fit · 0-0 fwd) |
| Thu 20:15 | Indianapolis Colts @ Houston Texans | spread | home | +32.3 | 5-1 | -11.5 (-115) | -10 | 1.5 | -13 ($20,000) | +1.5 |  | 57% / 59% | 4084 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | moneyline | away | +32.1 | 2-1 | -290 (-290) | -290 |  | -283 ($5,000) |  |  | 97% / 98% | 2403 | money_level->away (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); consensus_gap->home (12-29 fit · 1-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | moneyline | away | +28.1 | 2-2 | -255 (-255) | -245 | 1.1 | -264 ($10,000) |  |  | 97% / 95% | 2796 | follow_move->away (15-18 fit · 1-0 fwd); money_level->away (34-6 fit · 0-1 fwd); sharp_gap->home (20-18 fit · 1-0 fwd); consensus_gap->home (12-29 fit · 1-0 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | spread | away | +23.9 | 1-1 | -4.5 (-110) | -4.5 |  | -4.5 ($20,000) |  |  | 78% / 77% | 2140 | money_level->away (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd) |

## B  weighted ROI +10% to +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | moneyline | away | +15.4 | 3-2 | -210 (-210) | -210 |  | -220 ($10,000) |  |  | 91% / 92% | 2140 | money_level->away (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->home (12-29 fit · 1-0 fwd); book_lag->home (1-1 fit · 0-0 fwd) |

## C  weighted ROI 0 to +10%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 20:15 | Indianapolis Colts @ Houston Texans | moneyline | home | +9.8 | 3-2 | -750 (-750) | -720 | 0.4 | -739 ($10,000) |  |  | 94% / 62% | 4084 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->home (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | total | over | +9.6 | 2-2 | 44.5 (-100) | 43.5 | 1 | 43.5 ($3,000) | +1 |  | 84% / 72% | 1726 | follow_move->over (9-9 fit · 1-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | spread | home | +5.5 | 3-1 | -2.5 (-110) | -2 | 0.5 | -2.5 ($20,000) |  |  | 61% / 64% | 1726 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | total | over | +3.7 | 2-1 | 38.5 (-110) | 38.5 |  | 38.5 ($3,000) |  |  | 81% / 86% | 2140 | money_level->over (22-18 fit · 1-0 fwd); sharp_gap->over (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | total | over | +3.4 | 1-0 | 48.5 (-120) | 48.5 |  | 48.5 ($3,000) |  |  | 61% / 61% | 3180 | money_level->over (22-18 fit · 1-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | total | over | +2.9 | 3-1 | 52.5 (-115) | 52.5 |  | 53 ($3,000) | -0.5 |  | 54% / 79% | 2403 | money_level->over (22-18 fit · 1-0 fwd); sharp_gap->over (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd); pin_value->over (11-10 fit · 0-1 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | total | under | +2.6 | 2-0 | 46.5 (-115) | 46.5 |  | 46 ($3,000) | +0.5 |  | 89% / 89% | 3216 | money_level->under (22-18 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | tt_away | over | +2.3 | 1-0 | 18.5 (-113) | 18.5 |  | 19.5 ($2,000) | -1 |  | 0% / 0% | 3180 | pin_value->over (14-11 fit · 0-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | tt_away | under | +2.3 | 1-0 | 19.5 (-120) | 19.5 |  | 18.5 ($2,000) | +1 |  | 0% / 0% | 1650 | pin_value->under (14-11 fit · 0-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | tt_away | under | +2.3 | 1-0 | 30.5 (-125) | 30.5 |  | 29.5 ($1,000) | +1 |  | 0% / 0% | 2403 | pin_value->under (14-11 fit · 0-0 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | tt_home | over | +1.4 | 1-0 | 30.5 (-128) | 30.5 |  | 31.5 ($2,000) | -1 |  | 0% / 0% | 2478 | pin_value->over (15-12 fit · 1-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | tt_home | under | +1.4 | 1-0 | 30.5 (-104) | 30.5 |  | 29.5 ($2,000) | +1 |  | 0% / 0% | 3180 | pin_value->under (15-12 fit · 1-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | tt_home | under | +1.4 | 1-0 | 25.5 (-111) | 25.5 |  | 24.5 ($2,000) | +1 |  | 0% / 0% | 2453 | pin_value->under (15-12 fit · 1-0 fwd) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | total | under | -1.7 | 3-1 | 45.5 (-105) | 45.5 |  | 45.5 ($3,000) |  |  | 19% / 23% | 2478 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); pin_rlm->under (3-1 fit · 0-0 fwd) |
| Thu 20:15 | Indianapolis Colts @ Houston Texans | tt_away | under | -2.3 | 1-1 | 15.5 (-100) | 16.5 | 1 | 16.5 ($2,000) | -1 |  | 0% / 0% | 4084 | follow_move->under (8-7 fit · 0-0 fwd); pin_value->over (14-11 fit · 0-0 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | tt_away | under | -2.3 | 1-1 | 19.5 (-113) | 20.5 | 1 | 20.5 ($2,000) | -1 |  | 0% / 0% | 3059 | follow_move->under (8-7 fit · 0-0 fwd); pin_value->over (14-11 fit · 0-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | tt_away | over | -2.3 | 1-1 | 21.5 (-104) | 20.5 | 1 | 20.5 ($2,000) | +1 |  | 0% / 0% | 1726 | follow_move->over (8-7 fit · 0-0 fwd); pin_value->under (14-11 fit · 0-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | tt_home | under | -4.7 | 1-0 | 19.5 (-100) | 20.5 | 1 | 19.5 ($2,000) |  |  | 0% / 0% | 2796 | follow_move->under (8-9 fit · 1-0 fwd) |
| Thu 20:15 | Indianapolis Colts @ Houston Texans | tt_home | over | -6.1 | 1-1 | 28.5 (-111) | 27.5 | 1 | 27.5 ($2,000) | +1 |  | 0% / 0% | 4084 | follow_move->over (8-9 fit · 1-0 fwd); pin_value->under (15-12 fit · 1-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | tt_home | over | -6.1 | 1-1 | 32.5 (-113) | 31.5 | 1 | 31.5 ($2,000) | +1 |  | 0% / 0% | 3306 | follow_move->over (8-9 fit · 1-0 fwd); pin_value->under (15-12 fit · 1-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | tt_home | over | -6.1 | 1-1 | 23.5 (-100) | 22.5 | 1 | 22.5 ($2,000) | +1 |  | 0% / 0% | 1726 | follow_move->over (8-9 fit · 1-0 fwd); pin_value->under (15-12 fit · 1-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | tt_home | over | -6.1 | 1-1 | 22.5 (-122) | 21.5 | 1 | 21.5 ($2,000) | +1 |  | 0% / 0% | 1650 | follow_move->over (8-9 fit · 1-0 fwd); pin_value->under (15-12 fit · 1-0 fwd) |
| Thu 20:15 | Indianapolis Colts @ Houston Texans | total | under | -8 | 3-2 | 44.5 (-110) | 44.5 |  | 44 ($5,000) | +0.5 |  | 25% / 36% | 4084 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | total | under | -8 | 3-2 | 41.5 (-110) | 41.5 |  | 41 ($3,000) | +0.5 |  | 11% / 19% | 2054 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | total | under | -10.6 | 4-2 | 45.5 (-120) | 46.5 | 1 | 45 ($3,000) | +0.5 | over 75% | 25% / 10% | 3059 | follow_move->under (9-9 fit · 1-0 fwd); rlm->under (4-5 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->over (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | total | under | -11.5 | 2-1 | 40.5 (-115) | 40.5 |  | 40 ($3,000) | +0.5 |  | 22% / 25% | 2453 | money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | spread | away | -12.1 | 6-0 | -5.5 (-120) | -4 | 1.5 | -6.5 ($10,000) | -1 |  | 75% / 82% | 2403 | follow_move->away (15-20 fit · 0-1 fwd); money_level->away (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); consensus_gap->away (5-3 fit · 0-0 fwd); pin_value->away (15-3 fit · 0-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | total | under | -14.8 | 2-1 | 54.5 (-100) | 54.5 |  | 54.5 ($3,000) |  |  | 25% / 30% | 3306 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | spread | home | -16.7 | 3-0 | -6.5 (-110) | -5.5 | 1 | -6.5 ($10,000) |  |  | 76% / 78% | 3059 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | total | under | -17.2 | 3-2 | 41.5 (-115) | 40.5 | 1 | 41 ($3,000) | +0.5 |  | 32% / 43% | 1650 | follow_move->over (9-9 fit · 1-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | spread | away | -20.9 | 2-2 | 3 (-100) | 3.5 | 0.5 | 3 ($20,000) |  |  | 76% / 50% | 3216 | follow_move->away (15-20 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | total | under | -22.4 | 3-1 | 46.5 (-110) | 46.5 |  | 46.5 ($3,000) |  |  | 10% / 16% | 2796 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | moneyline | away | -39.8 | 4-2 | 350 (+350) | 350 |  | 312 ($10,000) |  |  | 3% / 5% | 3306 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->home (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_value->away (2-6 fit · 0-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | moneyline | away | -44.2 | 3-1 | 410 (+410) | 410 |  | 410 ($10,000) |  |  | 3% / 9% | 2453 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | moneyline | away | -46.4 | 3-2 | 220 (+220) | 215 | 0.8 | 231 ($10,000) |  |  | 5% / 10% | 3059 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | moneyline | away | -46.4 | 3-2 | 154 (+154) | 134 | 3.5 | 152 ($10,000) |  |  | 33% / 49% | 1650 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | moneyline | away | -52.3 | 4-2 | 112 (+112) | 112 |  | 124 ($10,000) |  |  | 15% / 35% | 1726 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->home (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_rlm->away (2-7 fit · 0-0 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | moneyline | away | -52.3 | 5-1 | 138 (+138) | 138 |  | 145 ($10,000) |  |  | 10% / 41% | 3216 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_rlm->away (2-7 fit · 0-0 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | moneyline | away | -66.2 | 5-1 | 980 (+980) | 980 |  | 886 ($10,000) |  |  | 2% / 7% | 2478 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_value->away (2-6 fit · 0-0 fwd); pin_rlm->away (2-7 fit · 0-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | spread | home | -70 | 2-2 | 5.5 (-100) | 6.5 | 1 | 6 ($20,000) | -0.5 | away 83% | 17% / 17% | 2796 | follow_move->home (15-20 fit · 0-1 fwd); rlm->home (1-11 fit · 0-0 fwd); money_level->away (24-16 fit · 0-1 fwd); pin_value->away (15-3 fit · 0-0 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | moneyline | away | -82.9 | 5-2 | 830 (+830) | 870 | 0.4 | 855 ($10,000) |  | home 98% | 2% / 21% | 2054 | follow_move->away (15-18 fit · 1-0 fwd); rlm->away (3-16 fit · 1-0 fwd); rlm_ratio->away (2-7 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->home (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | spread | away | -104.5 | 4-2 | 16.5 (-110) | 17 | 0.5 | 17 ($20,000) | +0.5 | home 71% | 29% / 41% | 2478 | follow_move->away (15-20 fit · 0-1 fwd); rlm->away (1-11 fit · 0-0 fwd); rlm_ratio->away (0-6 fit · 0-0 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | moneyline | away | -115.1 | 6-1 | 460 (+460) | 490 | 0.9 | 439 ($10,000) |  | home 97% | 3% / 4% | 3180 | follow_move->away (15-18 fit · 1-0 fwd); rlm->away (3-16 fit · 1-0 fwd); rlm_ratio->away (2-7 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_value->away (2-6 fit · 0-0 fwd) |

