# NFL board

Generated 2026-11-19 20:55 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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
| PINNACLE moved vs public | Miami Dolphins @ Buffalo Bills | total | under | Pinnacle | 47 -> 44.5 | 45.5 | 22% | 1.5 | 5-10 fit · 0-0 fwd |
| PINNACLE moved vs public | Miami Dolphins @ Buffalo Bills | moneyline | away | Pinnacle | 889 -> 880 | 870 | 1% | 6.0 | 5-10 fit · 0-0 fwd |
| PINNACLE moved vs public | Minnesota Vikings @ San Francisco 49ers | moneyline | away | Pinnacle | 145 -> 143 | 138 | 13% | 2.31 | 5-10 fit · 0-0 fwd |
| FanDuel moved vs public | Miami Dolphins @ Buffalo Bills | spread | away | FanDuel | 17 -> 16.5 | 16.5 | 31% | 1.23 | 5-14 fit · 1-0 fwd |
| FanDuel moved vs public | Miami Dolphins @ Buffalo Bills | moneyline | away | FanDuel | 980 -> 870 | 870 | 1% | 6.0 | 5-14 fit · 1-0 fwd |
| line moved off the public (no ratio test) | Cincinnati Bengals @ Washington Commanders | moneyline | home | FanDuel | 235 -> 220 | 220 | 2% | 0.5 | 8-32 fit · 1-0 fwd |
| line moved off the public (no ratio test) | Indianapolis Colts @ Houston Texans | total | under | FanDuel | 44.5 -> 43.5 | 43.5 | 25% | 0.8 | 8-32 fit · 1-0 fwd |
| line moved off the public (no ratio test) | Jacksonville Jaguars @ New York Giants | spread | home | FanDuel | 6.5 -> 5.5 | 5.5 | 11% | 1.09 | 8-32 fit · 1-0 fwd |
| line moved off the public (no ratio test) | Pittsburgh Steelers @ Philadelphia Eagles | total | under | FanDuel | 38.5 -> 37.5 | 37.5 | 18% | 0.94 | 8-32 fit · 1-0 fwd |
| line moved off the public (no ratio test) | Tampa Bay Buccaneers @ Detroit Lions | total | under | FanDuel | 46.5 -> 45.5 | 45.5 | 19% | 0.68 | 8-32 fit · 1-0 fwd |
| line moved off the public (no ratio test) | Tennessee Titans @ Dallas Cowboys | spread | away | FanDuel | 8 -> 7.5 | 7.5 | 36% | 0.94 | 8-32 fit · 1-0 fwd |

Ranked by **weighted ROI**: each agreeing signal contributes its own return per
unit risked, and contributes nothing until it has 30 decided outcomes. A signal
earns positive weight only if it **both** beats its own base rate and makes
money. Hit-rate edge alone is blind to price — `money_level` on CBB moneylines
beats its base rate by 3.6 points while returning −3.5%, because it lays −880
favourites, and on 2026-11-17 that ranked a −880 chalk first on the board.
Raw agreement count is shown too, but it is the weaker number — a
market can have seven signals agreeing where four of them have losing records.

**SPLIT** marks a market where at least two signals point each way. Those average
to a weak score and land in band D looking empty, when in fact our inputs are
in conflict — usually the markets worth the most attention. They sort first
inside whatever band they fall in.

Each call shows **two** records: `fit` (the games the signal was chosen on —
before 2026-11-17, so a good number there proves nothing) and `fwd` (games
since, which it had no hand in choosing). A `*` means the weight came from the
forward record, which happens once that record reaches 30 decided
outcomes. No asterisk means the lean rests on fitted numbers only.

## A  weighted ROI >= +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | spread | away **SPLIT** | +62.5 | 4-2 | -5.5 (-115) | -4 | 1.5 | -6.5 ($20,000) | +1 |  | 80% / 77% | 6209 | follow_move->away (15-20 fit · 0-1 fwd); money_level->away (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd); consensus_gap->away (5-3 fit · 0-0 fwd); pin_value->away (15-3 fit · 0-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | moneyline | home **SPLIT** | +23.7 | 3-3 | -620 (-620) | -550 | 1.5 | -542 ($10,000) |  |  | 97% / 93% | 7421 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->home (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_value->away (2-6 fit · 0-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | spread | home | +69.2 | 4-1 | -9.5 (-120) | -9.5 |  | -10.5 ($20,000) | +1 |  | 68% / 68% | 7421 | money_level->home (24-16 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd); book_lag->home (4-0 fit · 0-0 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | spread | home | +20.6 | 2-1 | -6.5 (-100) | -5.5 | 1 | -6.5 ($10,000) |  |  | 73% / 73% | 8850 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | spread | home | +20.6 | 2-1 | -2.5 (-110) | -2 | 0.5 | -2.5 ($20,000) |  |  | 67% / 67% | 5856 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd) |

## B  weighted ROI +10% to +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | spread | home | +14.7 | 4-1 | -15.5 (-115) | -15 | 0.5 | -16 ($20,000) | +0.5 |  | 64% / 60% | 6750 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | spread | home | +13.5 | 2-1 | -11.5 (-110) | -9.5 | 2 | -11.5 ($20,000) |  |  | 81% / 74% | 9466 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd) |

## C  weighted ROI 0 to +10%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | moneyline | away | +3.9 | 3-1 | -260 (-260) | -245 | 1.6 | -269 ($10,000) |  |  | 97% / 97% | 8880 | follow_move->away (15-18 fit · 1-0 fwd); money_level->away (34-6 fit · 0-1 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->home (12-29 fit · 1-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | total | over | +3.4 | 1-0 | 48.5 (-115) | 48.5 |  | 48.5 ($3,000) |  |  | 63% / 63% | 9466 | money_level->over (22-18 fit · 1-0 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | total | under | +2.6 | 2-0 | 46.5 (-105) | 46.5 |  | 46 ($3,000) | -0.5 |  | 88% / 88% | 8572 | money_level->under (22-18 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | total | over | +2.3 | 3-1 | 54.5 (-120) | 54.5 |  | 55.5 ($3,000) | -1 |  | 71% / 68% | 9022 | money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd); pin_value->over (11-10 fit · 0-1 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | tt_away | over | +2.3 | 1-0 | 18.5 (-111) | 18.5 |  | 19.5 ($2,000) | -1 |  | 0% / 0% | 9466 | pin_value->over (14-11 fit · 0-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | tt_away | under | +2.3 | 1-0 | 19.5 (-104) | 19.5 |  | 18.5 ($2,000) | -1 |  | 0% / 0% | 4432 | pin_value->under (14-11 fit · 0-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | tt_away | under | +2.3 | 1-0 | 30.5 (-115) | 30.5 |  | 29.5 ($1,000) | -1 |  | 0% / 0% | 6209 | pin_value->under (14-11 fit · 0-0 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | tt_home | over | +1.4 | 1-0 | 30.5 (-113) | 30.5 |  | 31.5 ($2,000) | -1 |  | 0% / 0% | 7027 | pin_value->over (15-12 fit · 1-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | tt_home | under | +1.4 | 1-0 | 30.5 (-108) | 30.5 |  | 29.5 ($2,000) | -1 |  | 0% / 0% | 9466 | pin_value->under (15-12 fit · 1-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | tt_home | under | +1.4 | 1-0 | 20.5 (-130) | 20.5 |  | 19.5 ($2,000) | -1 |  | 0% / 0% | 8880 | pin_value->under (15-12 fit · 1-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | tt_home | under | +1.4 | 1-0 | 25.5 (-104) | 25.5 |  | 24.5 ($2,000) | -1 |  | 0% / 0% | 7421 | pin_value->under (15-12 fit · 1-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | total | over | +1.2 | 3-1 | 41.5 (-115) | 40.5 | 1 | 41.5 ($3,000) |  |  | 61% / 56% | 4432 | follow_move->over (9-9 fit · 1-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | total | over | +1 | 4-1 | 53.5 (-115) | 52.5 | 1 | 54.5 ($3,000) | -1 |  | 55% / 71% | 6209 | follow_move->over (9-9 fit · 1-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->over (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd); pin_value->over (11-10 fit · 0-1 fwd) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 20:15 | Indianapolis Colts @ Houston Texans | total | over **SPLIT** | -6.2 | 4-2 | 43.5 (-120) | 44.5 | 1 | 44 ($20,000) | -0.5 | over 75% | 75% / 80% | 39682 | follow_move->under (9-9 fit · 1-0 fwd); rlm->under (4-5 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->over (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd); pin_value->over (11-10 fit · 0-1 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | total | under **SPLIT** | -7.2 | 2-2 | 43.5 (-110) | 43.5 |  | 43.5 ($3,000) |  |  | 23% / 29% | 5856 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | total | under **SPLIT** | -9 | 3-3 | 37.5 (-105) | 38.5 | 1 | 38.5 ($3,000) | +1 | over 82% | 18% / 17% | 5513 | follow_move->under (9-9 fit · 1-0 fwd); rlm->under (4-5 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->over (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd); pin_value->over (11-10 fit · 0-1 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | total | under **SPLIT** | -10.6 | 4-2 | 45.5 (-105) | 46.5 | 1 | 45 ($3,000) | -0.5 | over 81% | 19% / 13% | 8850 | follow_move->under (9-9 fit · 1-0 fwd); rlm->under (4-5 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->over (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | spread | away **SPLIT** | -12.1 | 3-2 | 3 (-100) | 3.5 | 0.5 | 3 ($20,000) |  |  | 62% / 54% | 8572 | follow_move->away (15-20 fit · 0-1 fwd); money_level->away (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd) |
| Thu 20:15 | Indianapolis Colts @ Houston Texans | moneyline | away **SPLIT** | -25.9 | 3-2 | 520 (+520) | 520 |  | 540 ($30,000) |  |  | 7% / 23% | 39682 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->home (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | moneyline | away **SPLIT** | -25.9 | 3-2 | 870 (+870) | 870 |  | 849 ($10,000) |  |  | 2% / 12% | 6750 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->home (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | moneyline | away **SPLIT** | -42 | 3-2 | 540 (+540) | 490 | 1.5 | 441 ($10,000) |  |  | 2% / 3% | 9466 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_value->away (2-6 fit · 0-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | moneyline | away **SPLIT** | -46.4 | 3-2 | 136 (+136) | 134 | 0.6 | 144 ($10,000) |  |  | 26% / 39% | 4432 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | moneyline | home **SPLIT** | -75.4 | 3-2 | 220 (+220) | 235 | 1.4 | 247 ($10,000) |  | away 98% | 2% / 1% | 6209 | follow_move->home (15-18 fit · 1-0 fwd); rlm->home (3-16 fit · 1-0 fwd); money_level->away (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); consensus_gap->home (12-29 fit · 1-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | spread | away **SPLIT** | -77.1 | 3-3 | 7.5 (-105) | 8 | 0.5 | 8 ($20,000) | -0.5 | home 64% | 36% / 34% | 9022 | follow_move->away (15-20 fit · 0-1 fwd); rlm->away (1-11 fit · 0-0 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | spread | away **SPLIT** | -82.3 | 4-3 | 16.5 (-110) | 17 | 0.5 | 17 ($20,000) | -0.5 | home 69% | 31% / 38% | 7027 | follow_move->away (15-20 fit · 0-1 fwd); rlm->away (1-11 fit · 0-0 fwd); rlm_ratio->away (0-6 fit · 0-0 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | spread | home **SPLIT** | -107.3 | 4-2 | 5.5 (-100) | 6.5 | 1 | 6 ($20,000) | -0.5 | away 89% | 11% / 12% | 8880 | follow_move->home (15-20 fit · 0-1 fwd); rlm->home (1-11 fit · 0-0 fwd); money_level->away (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd); pin_value->away (15-3 fit · 0-0 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | moneyline | away | -2 | 4-1 | -225 (-225) | -210 | 1.5 | -217 ($10,000) |  |  | 87% / 93% | 5513 | follow_move->away (15-18 fit · 1-0 fwd); money_level->away (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->home (12-29 fit · 1-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | tt_away | over | -2.3 | 1-1 | 23.5 (-104) | 22.5 | 1 | 22.5 ($2,000) | +1 |  | 0% / 0% | 9022 | follow_move->over (8-7 fit · 0-0 fwd); pin_value->under (14-11 fit · 0-0 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | tt_away | under | -2.3 | 1-1 | 19.5 (+102) | 20.5 | 1 | 20.5 ($2,000) | +1 |  | 0% / 0% | 8850 | follow_move->under (8-7 fit · 0-0 fwd); pin_value->over (14-11 fit · 0-0 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | total | under | -2.5 | 5-1 | 45.5 (-115) | 45.5 |  | 44.5 ($3,000) | -1 |  | 22% / 33% | 7027 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd); pin_rlm->under (3-1 fit · 0-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | total | over | -5 | 3-0 | 40.5 (-110) | 40.5 |  | 41 ($3,000) | -0.5 |  | 76% / 76% | 7421 | money_level->over (22-18 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd); pin_value->over (11-10 fit · 0-1 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | tt_home | over | -6.1 | 1-1 | 32.5 (-113) | 31.5 | 1 | 31.5 ($2,000) | +1 |  | 0% / 0% | 9022 | follow_move->over (8-9 fit · 1-0 fwd); pin_value->under (15-12 fit · 1-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | tt_home | over | -6.1 | 1-1 | 22.5 (-115) | 21.5 | 1 | 21.5 ($2,000) | +1 |  | 0% / 0% | 4432 | follow_move->over (8-9 fit · 1-0 fwd); pin_value->under (15-12 fit · 1-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | total | under | -14.8 | 2-1 | 46.5 (-110) | 46.5 |  | 46.5 ($3,000) |  |  | 13% / 18% | 8880 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd) |
| Thu 20:15 | Indianapolis Colts @ Houston Texans | spread | home | -15.5 | 5-0 | -12.5 (-104) | -10 | 2.5 | -13 ($60,000) | +0.5 |  | 55% / 63% | 39682 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | moneyline | home | -15.9 | 5-1 | -136 (-136) | -132 | 0.7 | -153 ($10,000) |  |  | 83% / 84% | 5856 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->home (20-18 fit · 1-0 fwd); money_moving->home (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_value->home (2-6 fit · 0-0 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | total | under | -23.2 | 4-1 | 41.5 (-120) | 41.5 |  | 41 ($3,000) | -0.5 |  | 12% / 26% | 6750 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | spread | away | -31.9 | 3-1 | 3 (-110) | 3 |  | 3 ($10,000) |  |  | 50% / 70% | 4432 | money_level->away (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | spread | home | -46.1 | 2-1 | 4.5 (-110) | 4.5 |  | 4.5 ($20,000) |  |  | 35% / 37% | 5513 | money_level->away (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | moneyline | away | -52 | 6-1 | 870 (+870) | 980 | 1 | 880 ($10,000) |  | home 99% | 1% / 6% | 7027 | follow_move->away (15-18 fit · 1-0 fwd); rlm->away (3-16 fit · 1-0 fwd); rlm_ratio->away (2-7 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_rlm->away (2-7 fit · 0-0 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | moneyline | away | -52.3 | 4-1 | 138 (+138) | 138 |  | 143 ($10,000) |  |  | 13% / 30% | 8572 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_rlm->away (2-7 fit · 0-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | moneyline | away | -58.1 | 4-1 | 350 (+350) | 350 |  | 312 ($10,000) |  |  | 3% / 6% | 9022 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_value->away (2-6 fit · 0-0 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | moneyline | away | -62.5 | 4-1 | 215 (+215) | 215 |  | 236 ($10,000) |  |  | 4% / 8% | 8850 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd) |

