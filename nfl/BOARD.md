# NFL board

Generated 2026-11-18 12:09 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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
| PINNACLE moved vs public | Miami Dolphins @ Buffalo Bills | total | under | Pinnacle | 47 -> 45.5 | 45.5 | 18% | 1.28 | 5-10 fit · 0-0 fwd |
| PINNACLE moved vs public | Miami Dolphins @ Buffalo Bills | moneyline | away | Pinnacle | 889 -> 886 | 900 | 2% | 3.0 | 5-10 fit · 0-0 fwd |
| PINNACLE moved vs public | Minnesota Vikings @ San Francisco 49ers | moneyline | away | Pinnacle | 145 -> 145 | 138 | 12% | 2.75 | 5-10 fit · 0-0 fwd |
| FanDuel moved vs public | Miami Dolphins @ Buffalo Bills | spread | away | FanDuel | -17 -> 16.5 | 16.5 | 31% | 1.29 | 5-14 fit · 1-0 fwd |
| FanDuel moved vs public | Miami Dolphins @ Buffalo Bills | moneyline | away | FanDuel | -1800 -> 900 | 900 | 2% | 3.0 | 5-14 fit · 1-0 fwd |

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
| Thu 20:15 | Indianapolis Colts @ Houston Texans | spread | home | +59.1 | 3-2 | -12.5 (-110) | -10 | 2.5 | -13 ($20,000) | +0.5 |  | 53% / 52% | 6785 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | spread | home | +54.1 | 5-1 | -9.5 (-120) | -9.5 |  | -10 ($20,000) | +0.5 |  | 59% / 62% | 3826 | money_level->home (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd); book_lag->home (4-0 fit · 0-0 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | spread | home | +35.7 | 2-2 | -11.5 (-110) | -9.5 | 2 | -11.5 ($20,000) |  |  | 84% / 72% | 4740 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | spread | home | +32.7 | 4-2 | -7.5 (-115) | -8 | 0.5 | -8 ($20,000) | +0.5 | home 65% | 65% / 70% | 4927 | follow_move->away (15-20 fit · 0-1 fwd); rlm->away (1-11 fit · 0-0 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | moneyline | home | +23.7 | 3-3 | -590 (-590) | -550 | 0.9 | -535 ($10,000) |  |  | 97% / 92% | 3826 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->home (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_value->away (2-6 fit · 0-0 fwd) |

## B  weighted ROI +10% to +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | spread | home | +18.1 | 5-1 | -15.5 (-115) | -15 | 0.5 | -16 ($20,000) | +0.5 |  | 73% / 67% | 3190 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | moneyline | away | +16.3 | 3-1 | -295 (-295) | -290 | 0.4 | -279 ($5,000) |  |  | 97% / 98% | 3544 | follow_move->away (15-18 fit · 1-0 fwd); money_level->away (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); consensus_gap->home (12-29 fit · 1-0 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | moneyline | away | +15.4 | 3-2 | -210 (-210) | -210 |  | -218 ($10,000) |  |  | 91% / 94% | 2988 | money_level->away (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->home (12-29 fit · 1-0 fwd); book_lag->home (1-1 fit · 0-0 fwd) |

## C  weighted ROI 0 to +10%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 20:15 | Indianapolis Colts @ Houston Texans | moneyline | home | +9.8 | 3-2 | -770 (-770) | -720 | 0.7 | -726 ($10,000) |  |  | 94% / 63% | 6785 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->home (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | moneyline | home | +9.8 | 3-2 | -134 (-134) | -132 | 0.4 | -140 ($10,000) |  |  | 84% / 82% | 2605 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->home (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | spread | away | +5.3 | 4-1 | 3.5 (-115) | 3 | 0.5 | 3 ($10,000) | -0.5 |  | 49% / 75% | 2372 | follow_move->home (15-20 fit · 0-1 fwd); money_level->away (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); pin_value->away (15-3 fit · 0-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | total | over | +3.9 | 2-2 | 40.5 (-110) | 40.5 |  | 40 ($3,000) | +0.5 |  | 79% / 78% | 3826 | money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | total | over | +3.7 | 2-1 | 38.5 (-110) | 38.5 |  | 38.5 ($3,000) |  |  | 82% / 85% | 2988 | money_level->over (22-18 fit · 1-0 fwd); sharp_gap->over (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | total | over | +3.4 | 1-0 | 48.5 (-115) | 48.5 |  | 48.5 ($3,000) |  |  | 63% / 63% | 4740 | money_level->over (22-18 fit · 1-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | total | over | +3.1 | 2-1 | 54.5 (-120) | 54.5 |  | 54.5 ($3,000) |  |  | 75% / 71% | 4927 | money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | total | under | +2.6 | 2-0 | 46.5 (-115) | 46.5 |  | 46 ($3,000) | +0.5 |  | 89% / 89% | 4791 | money_level->under (22-18 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | total | over | +2.6 | 3-2 | 53.5 (-115) | 52.5 | 1 | 53 ($3,000) | +0.5 |  | 58% / 80% | 3544 | follow_move->over (9-9 fit · 1-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->over (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | tt_away | over | +2.3 | 1-0 | 18.5 (-113) | 18.5 |  | 19.5 ($2,000) | -1 |  | 0% / 0% | 4740 | pin_value->over (14-11 fit · 0-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | tt_away | under | +2.3 | 1-0 | 19.5 (-120) | 19.5 |  | 18.5 ($2,000) | +1 |  | 0% / 0% | 2372 | pin_value->under (14-11 fit · 0-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | tt_away | under | +2.3 | 1-0 | 30.5 (-113) | 30.5 |  | 29.5 ($1,000) | +1 |  | 0% / 0% | 3544 | pin_value->under (14-11 fit · 0-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | total | over | +2 | 3-2 | 44.5 (-100) | 43.5 | 1 | 43.5 ($3,000) | +1 |  | 83% / 75% | 2605 | follow_move->over (9-9 fit · 1-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | total | over | +2 | 3-2 | 41.5 (-105) | 40.5 | 1 | 41 ($3,000) | +0.5 |  | 69% / 62% | 2372 | follow_move->over (9-9 fit · 1-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | tt_home | over | +1.4 | 1-0 | 30.5 (-115) | 30.5 |  | 31.5 ($2,000) | -1 |  | 0% / 0% | 3534 | pin_value->over (15-12 fit · 1-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | tt_home | under | +1.4 | 1-0 | 30.5 (-106) | 30.5 |  | 29.5 ($2,000) | +1 |  | 0% / 0% | 4740 | pin_value->under (15-12 fit · 1-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | tt_home | under | +1.4 | 1-0 | 25.5 (-104) | 25.5 |  | 24.5 ($2,000) | +1 |  | 0% / 0% | 3826 | pin_value->under (15-12 fit · 1-0 fwd) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | total | under | -1.7 | 4-1 | 45.5 (-115) | 45.5 |  | 45.5 ($3,000) |  |  | 18% / 23% | 3534 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd); pin_rlm->under (3-1 fit · 0-0 fwd) |
| Thu 20:15 | Indianapolis Colts @ Houston Texans | tt_away | under | -2.3 | 1-1 | 15.5 (-104) | 16.5 | 1 | 16.5 ($2,000) | -1 |  | 0% / 0% | 6785 | follow_move->under (8-7 fit · 0-0 fwd); pin_value->over (14-11 fit · 0-0 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | tt_away | under | -2.3 | 1-1 | 17.5 (-120) | 20.5 | 3 | 20.5 ($2,000) | -3 |  | 0% / 0% | 4442 | follow_move->under (8-7 fit · 0-0 fwd); pin_value->over (14-11 fit · 0-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | tt_away | over | -2.3 | 1-1 | 21.5 (-106) | 20.5 | 1 | 20.5 ($2,000) | +1 |  | 0% / 0% | 2605 | follow_move->over (8-7 fit · 0-0 fwd); pin_value->under (14-11 fit · 0-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | tt_home | under | -4.7 | 1-0 | 19.5 (+102) | 20.5 | 1 | 19.5 ($2,000) |  |  | 0% / 0% | 4175 | follow_move->under (8-9 fit · 1-0 fwd) |
| Thu 20:15 | Indianapolis Colts @ Houston Texans | tt_home | over | -6.1 | 1-1 | 28.5 (-111) | 27.5 | 1 | 27.5 ($2,000) | +1 |  | 0% / 0% | 6785 | follow_move->over (8-9 fit · 1-0 fwd); pin_value->under (15-12 fit · 1-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | tt_home | over | -6.1 | 1-1 | 32.5 (-113) | 31.5 | 1 | 31.5 ($2,000) | +1 |  | 0% / 0% | 4927 | follow_move->over (8-9 fit · 1-0 fwd); pin_value->under (15-12 fit · 1-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | tt_home | over | -6.1 | 1-1 | 23.5 (-100) | 22.5 | 1 | 22.5 ($2,000) | +1 |  | 0% / 0% | 2605 | follow_move->over (8-9 fit · 1-0 fwd); pin_value->under (15-12 fit · 1-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | tt_home | over | -6.1 | 1-1 | 22.5 (-122) | 21.5 | 1 | 21.5 ($2,000) | +1 |  | 0% / 0% | 2372 | follow_move->over (8-9 fit · 1-0 fwd); pin_value->under (15-12 fit · 1-0 fwd) |
| Thu 20:15 | Indianapolis Colts @ Houston Texans | total | under | -8 | 3-2 | 44.5 (-115) | 44.5 |  | 44 ($5,000) | +0.5 |  | 25% / 32% | 6785 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | total | under | -8 | 3-2 | 41.5 (-120) | 41.5 |  | 41 ($3,000) | +0.5 |  | 13% / 19% | 3190 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | total | under | -10.6 | 4-2 | 44.5 (-120) | 46.5 | 2 | 44 ($3,000) | +0.5 | over 81% | 19% / 11% | 4442 | follow_move->under (9-9 fit · 1-0 fwd); rlm->under (4-5 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->over (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | spread | away | -12.1 | 3-2 | 3 (-100) | 3.5 | 0.5 | 3 ($20,000) |  |  | 68% / 52% | 4791 | follow_move->away (15-20 fit · 0-1 fwd); money_level->away (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | spread | away | -12.1 | 6-0 | -5.5 (-120) | -4 | 1.5 | -6.5 ($10,000) | -1 |  | 81% / 86% | 3544 | follow_move->away (15-20 fit · 0-1 fwd); money_level->away (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); consensus_gap->away (5-3 fit · 0-0 fwd); pin_value->away (15-3 fit · 0-0 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | spread | away | -12.3 | 3-2 | 7.5 (-120) | 5.5 | 2 | 7 ($10,000) | -0.5 |  | 22% / 25% | 4442 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); pin_value->away (15-3 fit · 0-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | spread | home | -16.7 | 3-0 | -2.5 (-110) | -2 | 0.5 | -2.5 ($20,000) |  |  | 70% / 74% | 2605 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | total | under | -22.4 | 3-1 | 46.5 (-110) | 46.5 |  | 46.5 ($3,000) |  |  | 10% / 16% | 4175 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | moneyline | away | -25.9 | 3-2 | 870 (+870) | 870 |  | 855 ($10,000) |  |  | 2% / 16% | 3190 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->home (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | moneyline | home | -25.9 | 3-2 | 200 (+200) | 200 |  | 224 ($10,000) |  |  | 3% / 4% | 4175 | pre_move->home (1-3 fit · 0-0 fwd); money_level->away (34-6 fit · 0-1 fwd); sharp_gap->home (20-18 fit · 1-0 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->home (12-29 fit · 1-0 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | spread | home | -46.1 | 2-1 | 4.5 (-110) | 4.5 |  | 4.5 ($20,000) |  |  | 20% / 23% | 2988 | money_level->away (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | moneyline | away | -46.4 | 3-2 | 154 (+154) | 134 | 3.5 | 154 ($10,000) |  |  | 30% / 48% | 2372 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | moneyline | away | -52 | 6-2 | 900 (+900) | 980 | 0.6 | 886 ($10,000) |  | home 98% | 2% / 6% | 3534 | follow_move->away (15-18 fit · 1-0 fwd); rlm->away (3-16 fit · 1-0 fwd); rlm_ratio->away (2-7 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->home (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_rlm->away (2-7 fit · 0-0 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | moneyline | away | -52.3 | 5-1 | 138 (+138) | 138 |  | 145 ($10,000) |  |  | 12% / 33% | 4791 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_rlm->away (2-7 fit · 0-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | moneyline | away | -58.1 | 4-1 | 350 (+350) | 350 |  | 310 ($10,000) |  |  | 3% / 6% | 4927 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_value->away (2-6 fit · 0-0 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | moneyline | away | -60.3 | 4-2 | 280 (+280) | 215 | 5.6 | 261 ($10,000) |  |  | 4% / 9% | 4442 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_value->away (2-6 fit · 0-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | moneyline | away | -60.3 | 4-2 | 520 (+520) | 490 | 0.8 | 439 ($10,000) |  |  | 2% / 4% | 4740 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_value->away (2-6 fit · 0-0 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | spread | away | -82.3 | 4-3 | 16.5 (-110) | 17 | 0.5 | 17 ($20,000) | +0.5 | home 69% | 31% / 40% | 3534 | follow_move->away (15-20 fit · 0-1 fwd); rlm->away (1-11 fit · 0-0 fwd); rlm_ratio->away (0-6 fit · 0-0 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | spread | home | -107.3 | 4-2 | 5.5 (-100) | 6.5 | 1 | 6 ($20,000) | -0.5 | away 86% | 14% / 16% | 4175 | follow_move->home (15-20 fit · 0-1 fwd); rlm->home (1-11 fit · 0-0 fwd); money_level->away (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd); pin_value->away (15-3 fit · 0-0 fwd) |

