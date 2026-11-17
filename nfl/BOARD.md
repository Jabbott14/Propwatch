# NFL board

Generated 2026-11-17 16:25 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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

| tier | game | market | side | line | moved from | tickets | money/tix | record |
|---|---|---|---|---|---|---|---|---|
| PINNACLE moved vs public | Miami Dolphins @ Buffalo Bills | total | under | 45.5 | 47.0 | 19% | 1.21 | 5-10 |
| PINNACLE moved vs public | Miami Dolphins @ Buffalo Bills | moneyline | away | 980 | -1438 | 2% | 3.5 | 5-10 |
| PINNACLE moved vs public | Minnesota Vikings @ San Francisco 49ers | moneyline | away | 138 | -165 | 10% | 2.8 | 5-10 |
| FanDuel moved vs public | Miami Dolphins @ Buffalo Bills | spread | away | 16.5 | -17 | 28% | 1.43 | 3-8 |

Ranked by **weighted edge**: each agreeing signal contributes its own
base-rate-corrected edge, and contributes nothing until it has 30 decided
outcomes. Raw agreement count is shown too, but it is the weaker number — a
market can have seven signals agreeing where four of them have losing records.

## A  weighted edge >= +10

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | spread | home | +26.2 | 5-2 | -7.5 (-115) | -8 | 0.5 | -8 ($10,000) | +0.5 | home 63% | 63% / 67% | 2958 | follow_move->away (15-21); rlm->away (1-11); money_level->home (24-17); sharp_gap->home (16-25); money_moving->home (9-21); consensus_gap->home (5-3); pin_value->home (15-3) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | spread | away | +23.2 | 4-2 | 3.5 (-115) | -3 | 0.5 | -3 ($5,000) | -0.5 | away 67% | 67% / 82% | 1469 | follow_move->home (15-21); rlm->home (1-11); money_level->away (24-17); sharp_gap->away (16-25); money_moving->away (9-21); pin_value->away (15-3) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | spread | home | +16.1 | 3-2 | -3 (-120) | -3.5 | 0.5 | -3 ($20,000) |  |  | 22% / 51% | 2897 | follow_move->away (15-21); money_level->home (24-17); sharp_gap->home (16-25); money_moving->away (9-21); consensus_gap->home (5-3) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | spread | home | +16 | 4-0 | -9.5 (-115) | -9.5 |  | -10 ($10,000) | +0.5 |  | 64% / 68% | 2175 | money_level->home (24-17); sharp_gap->home (16-25); book_lag->home (4-0); pin_value->home (15-3) |
| Thu 20:15 | Indianapolis Colts @ Houston Texans | spread | home | +12.7 | 5-1 | -11.5 (-115) | -10 | 1.5 | -13 ($20,000) | +1.5 |  | 59% / 61% | 3569 | follow_move->home (15-21); money_level->home (24-17); sharp_gap->home (16-25); money_moving->away (9-21); consensus_gap->home (5-3); pin_value->home (15-3) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | spread | home | +12.4 | 4-1 | -15.5 (-115) | -15 | 0.5 | -16 ($10,000) | +0.5 |  | 75% / 66% | 1772 | follow_move->home (15-21); money_level->home (24-17); sharp_gap->away (16-25); consensus_gap->home (5-3); pin_value->home (15-3) |

## B  weighted edge +5 to +10

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | moneyline | away | +6 | 4-1 | -210 (-210) | -110 | 16.1 | 190 ($10,000) |  |  | 91% / 92% | 1888 | follow_move->away (32-9); money_level->away (34-7); sharp_gap->away (21-18); money_moving->away (13-19); consensus_gap->home (13-29) |

## C  weighted edge 0 to +5

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | New Orleans Saints @ Chicago Bears | spread | home | +4.7 | 2-2 | -11.5 (-110) | -9.5 | 2 | -11.5 ($10,000) |  |  | 82% / 74% | 2832 | follow_move->home (15-21); money_level->home (24-17); sharp_gap->away (16-25); money_moving->away (9-21) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | moneyline | away | +4.3 | 3-1 | -280 (-280) | -110 | 22.1 | 238 ($5,000) |  |  | 97% / 98% | 2155 | follow_move->away (32-9); money_level->away (34-7); sharp_gap->away (21-18); consensus_gap->home (13-29) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | tt_home | over | +3.8 | 1-0 | 30.5 (-128) | 30.5 |  | 31.5 ($1,000) | -1 |  | 0% / 0% | 2140 | pin_value->over (16-12) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | tt_home | under | +3.8 | 1-0 | 30.5 (-100) | 30.5 |  | 29.5 ($1,000) | +1 |  | 0% / 0% | 2832 | pin_value->under (16-12) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | tt_home | under | +3.8 | 1-0 | 20.5 (-130) | 20.5 |  | 19.5 ($1,000) | +1 |  | 0% / 0% | 2539 | pin_value->under (16-12) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | tt_home | under | +3.8 | 1-0 | 25.5 (-111) | 25.5 |  | 24.5 ($1,000) | +1 |  | 0% / 0% | 2175 | pin_value->under (16-12) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | total | over | +3.3 | 1-1 | 43.5 (-110) | 43.5 |  | 43.5 ($3,000) |  |  | 84% / 72% | 1469 | money_level->over (23-18); sharp_gap->under (20-22) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | total | over | +3.3 | 1-1 | 46.5 (-110) | 46.5 |  | 46.5 ($3,000) |  |  | 89% / 84% | 2539 | money_level->over (23-18); sharp_gap->under (20-22) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | tt_away | over | +3 | 1-0 | 18.5 (-111) | 18.5 |  | 19.5 ($1,000) | -1 |  | 0% / 0% | 2832 | pin_value->over (14-11) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | tt_away | under | +3 | 1-0 | 19.5 (-120) | 19.5 |  | 18.5 ($1,000) | +1 |  | 0% / 0% | 1469 | pin_value->under (14-11) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | tt_away | under | +3 | 1-0 | 30.5 (-128) | 30.5 |  | 29.5 ($1,000) | +1 |  | 0% / 0% | 2155 | pin_value->under (14-11) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | total | under | +2.9 | 2-1 | 45.5 (-105) | 45.5 |  | 45.5 ($3,000) |  |  | 19% / 23% | 2140 | money_level->over (23-18); sharp_gap->under (20-22); pin_rlm->under (3-1) |
| Thu 20:15 | Indianapolis Colts @ Houston Texans | total | over | +1.6 | 2-2 | 44.5 (-110) | 44.5 |  | 44 ($5,000) | +0.5 |  | 75% / 63% | 3569 | money_level->over (23-18); sharp_gap->under (20-22); money_moving->over (15-17); pin_value->under (11-11) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | total | over | +1.6 | 2-2 | 40.5 (-105) | 40.5 |  | 40 ($3,000) | +0.5 |  | 77% / 75% | 2175 | money_level->over (23-18); sharp_gap->under (20-22); money_moving->over (15-17); pin_value->under (11-11) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | total | over | +1.4 | 2-1 | 54.5 (-120) | 54.5 |  | 54.5 ($3,000) |  |  | 74% / 70% | 2958 | money_level->over (23-18); sharp_gap->under (20-22); money_moving->over (15-17) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | total | under | +1.4 | 1-1 | 46.5 (-110) | 46.5 |  | 47 ($5,000) | -0.5 |  | 89% / 89% | 2897 | money_level->under (23-18); pin_value->over (11-11) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | moneyline | home | +1.3 | 4-2 | -134 (-134) | -108 | 5.3 | -145 ($5,000) |  |  | 85% / 63% | 1469 | follow_move->home (32-9); money_level->home (34-7); sharp_gap->away (21-18); money_moving->home (13-19); consensus_gap->away (13-29); pin_value->home (2-6) |
| Thu 20:15 | Indianapolis Colts @ Houston Texans | moneyline | away | +1.2 | 3-2 | 530 (+530) | -108 | 36.3 | -717 ($10,000) |  |  | 6% / 40% | 3569 | follow_move->home (32-9); money_level->home (34-7); sharp_gap->away (21-18); money_moving->away (13-19); consensus_gap->away (13-29) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | moneyline | away | +1.2 | 3-2 | 215 (+215) | -112 | 19.4 | -277 ($3,000) |  |  | 5% / 9% | 2781 | follow_move->home (32-9); money_level->home (34-7); sharp_gap->away (21-18); money_moving->away (13-19); consensus_gap->away (13-29) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | total | over | +1.2 | 1-0 | 48.5 (-120) | 48.5 |  | 48.5 ($3,000) |  |  | 60% / 60% | 2832 | money_level->over (23-18) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | moneyline | away | +1.2 | 3-2 | 154 (+154) | -118 | 10.7 | -173 ($3,000) |  |  | 32% / 46% | 1469 | follow_move->home (32-9); money_level->home (34-7); sharp_gap->away (21-18); money_moving->away (13-19); consensus_gap->away (13-29) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | total | over | +1 | 2-1 | 38.5 (-110) | 38.5 |  | 38.5 ($3,000) |  |  | 81% / 86% | 1888 | money_level->over (23-18); sharp_gap->over (20-22); money_moving->under (15-17) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | total | over | +0.8 | 3-1 | 52.5 (-115) | 52.5 |  | 53 ($3,000) | -0.5 |  | 51% / 79% | 2155 | money_level->over (23-18); sharp_gap->over (20-22); money_moving->under (15-17); pin_value->over (11-11) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | moneyline | home | +0.5 | 2-2 | -1400 (-1400) | -110 | 41 | -1363 ($5,000) |  |  | 98% / 78% | 1772 | follow_move->home (32-9); money_level->home (34-7); sharp_gap->away (21-18); consensus_gap->away (13-29) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | moneyline | away | +0.5 | 2-2 | -245 (-245) | -110 | 19 | 224 ($5,000) |  |  | 97% / 95% | 2539 | follow_move->away (32-9); money_level->away (34-7); sharp_gap->home (21-18); consensus_gap->home (13-29) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | moneyline | home | +0.5 | 2-2 | -550 (-550) | -108 | 32.7 | -533 ($5,000) |  |  | 97% / 91% | 2175 | follow_move->home (32-9); money_level->home (34-7); sharp_gap->away (21-18); consensus_gap->away (13-29) |

## D  no weighted edge (agreement is all unproven or negative signals)

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | moneyline | away | -1.4 | 3-2 | 350 (+350) | -108 | 29.9 | -385 ($5,000) |  |  | 3% / 6% | 2958 | follow_move->home (32-9); money_level->home (34-7); sharp_gap->away (21-18); consensus_gap->away (13-29); pin_value->away (2-6) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | moneyline | away | -1.4 | 3-2 | 490 (+490) | -110 | 34.6 | -578 ($5,000) |  |  | 3% / 4% | 2832 | follow_move->home (32-9); money_level->home (34-7); sharp_gap->away (21-18); consensus_gap->away (13-29); pin_value->away (2-6) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | total | over | -1.6 | 3-2 | 45.5 (-110) | 46.5 | 1 | 46.5 ($2,000) | -1 | over 72% | 72% / 89% | 2781 | follow_move->under (10-9); rlm->under (4-5); money_level->over (23-18); sharp_gap->over (20-22); pin_value->over (11-11) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | tt_away | over | -1.8 | 1-1 | 23.5 (-102) | 22.5 | 1 | 22.5 ($1,000) | +1 |  | 0% / 0% | 2958 | follow_move->over (8-7); pin_value->under (14-11) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | tt_away | under | -1.8 | 1-1 | 19.5 (-104) | 20.5 | 1 | 20.5 ($1,000) | -1 |  | 0% / 0% | 2781 | follow_move->under (8-7); pin_value->over (14-11) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | spread | away | -1.9 | 6-0 | -5.5 (-120) | 4 | 1.5 | 6.5 ($10,000) | -1 |  | 76% / 81% | 2155 | follow_move->away (15-21); money_level->away (24-17); sharp_gap->away (16-25); money_moving->away (9-21); consensus_gap->away (5-3); pin_value->away (15-3) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | moneyline | away | -2.2 | 4-2 | 138 (+138) | -120 | 7.6 | -164 ($10,000) |  |  | 10% / 28% | 2897 | follow_move->home (32-9); money_level->home (34-7); sharp_gap->away (21-18); money_moving->away (13-19); consensus_gap->away (13-29); pin_rlm->away (2-7) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | spread | home | -2.3 | 3-1 | -2.5 (-110) | -2 | 0.5 | -2.5 ($10,000) |  |  | 57% / 60% | 1469 | follow_move->home (15-21); money_level->home (24-17); sharp_gap->home (16-25); money_moving->away (9-21) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | moneyline | away | -3.1 | 4-2 | 980 (+980) | -108 | 42.8 | -1431 ($5,000) |  |  | 2% / 7% | 2140 | follow_move->home (32-9); money_level->home (34-7); sharp_gap->away (21-18); consensus_gap->away (13-29); pin_value->away (2-6); pin_rlm->away (2-7) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | total | under | -3.5 | 2-1 | 41.5 (-120) | 41.5 |  | 41 ($3,000) | +0.5 |  | 10% / 20% | 1772 | money_level->over (23-18); sharp_gap->under (20-22); pin_value->under (11-11) |
| Thu 20:15 | Indianapolis Colts @ Houston Texans | tt_home | over | -3.8 | 1-1 | 28.5 (-111) | 27.5 | 1 | 27.5 ($2,000) | +1 |  | 0% / 0% | 3569 | follow_move->over (9-9); pin_value->under (16-12) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | tt_home | over | -3.8 | 1-1 | 32.5 (-111) | 31.5 | 1 | 31.5 ($1,000) | +1 |  | 0% / 0% | 2958 | follow_move->over (9-9); pin_value->under (16-12) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | tt_home | under | -3.8 | 1-1 | 27.5 (-111) | 28.5 | 1 | 28.5 ($1,000) | -1 |  | 0% / 0% | 1772 | follow_move->under (9-9); pin_value->over (16-12) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | tt_home | over | -3.8 | 1-1 | 23.5 (-100) | 22.5 | 1 | 22.5 ($1,000) | +1 |  | 0% / 0% | 1469 | follow_move->over (9-9); pin_value->under (16-12) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | tt_home | over | -3.8 | 1-1 | 22.5 (-122) | 21.5 | 1 | 21.5 ($1,000) | +1 |  | 0% / 0% | 1469 | follow_move->over (9-9); pin_value->under (16-12) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | spread | away | -5.7 | 2-0 | -4.5 (-110) | 4.5 |  | 4.5 ($10,000) |  |  | 77% / 77% | 1888 | money_level->away (24-17); money_moving->away (9-21) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | total | under | -6.4 | 3-2 | 41.5 (-115) | 40.5 | 1 | 40 ($2,000) | +1.5 |  | 33% / 44% | 1469 | follow_move->over (10-9); money_level->over (23-18); sharp_gap->under (20-22); money_moving->under (15-17); pin_value->under (11-11) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | spread | home | -16.9 | 4-0 | -6.5 (-110) | -5.5 | 1 | -6.5 ($5,000) |  |  | 75% / 78% | 2781 | follow_move->home (15-21); money_level->home (24-17); sharp_gap->home (16-25); money_moving->home (9-21) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | spread | away | -25.8 | 4-2 | 16.5 (-110) | -17 | 0.5 | -17 ($10,000) | +0.5 | home 72% | 28% / 40% | 2140 | follow_move->away (15-21); rlm->away (1-11); rlm_ratio->away (0-6); money_level->home (24-17); sharp_gap->away (16-25); pin_value->home (15-3) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | spread | home | -34 | 2-2 | 5.5 (-100) | 6.5 | 1 | 6 ($10,000) | -0.5 | away 81% | 19% / 19% | 2539 | follow_move->home (15-21); rlm->home (1-11); money_level->away (24-17); pin_value->away (15-3) |

