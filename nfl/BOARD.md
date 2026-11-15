# NFL board

Generated 2026-11-15 07:04 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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
| PINNACLE moved vs public | Kansas City Chiefs @ Atlanta Falcons | moneyline | home | 144 | 170 | 3% | 4.67 | 4-8 |
| PINNACLE moved vs public | Los Angeles Chargers @ Baltimore Ravens | spread | home | -4.5 | -3.5 | 34% | 1.91 | 4-8 |
| PINNACLE moved vs public | Minnesota Vikings @ Green Bay Packers | moneyline | away | 124 | -221 | 18% | 2.11 | 4-8 |
| PINNACLE moved vs public | San Francisco 49ers @ Dallas Cowboys | moneyline | home | 184 | 182 | 5% | 2.0 | 4-8 |
| PINNACLE moved vs public | Seattle Seahawks @ Las Vegas Raiders | total | under | 40.5 | 43.5 | 24% | 1.25 | 4-8 |
| FanDuel moved vs public | Buffalo Bills @ New York Jets | spread | home | 7.5 | 8.5 | 7% | 1.57 | 3-6 |
| FanDuel moved vs public | Los Angeles Chargers @ Baltimore Ravens | spread | home | -4.5 | -2.5 | 34% | 1.91 | 3-6 |
| FanDuel moved vs public | Miami Dolphins @ Indianapolis Colts | total | under | 37.5 | 40.5 | 42% | 1.48 | 3-6 |
| FanDuel moved vs public | Seattle Seahawks @ Las Vegas Raiders | total | under | 40.5 | 43.5 | 24% | 1.25 | 3-6 |

Ranked by **weighted edge**: each agreeing signal contributes its own
base-rate-corrected edge, and contributes nothing until it has 30 decided
outcomes. Raw agreement count is shown too, but it is the weaker number — a
market can have seven signals agreeing where four of them have losing records.

## B  weighted edge +5 to +10

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Carolina Panthers @ New Orleans Saints | moneyline | away | +9.4 | 3-2 | 114 (+114) | -108 | 5.3 | -124 ($20,000) |  |  | 50% / 61% | 28363 | follow_move->home (23-6); money_level->away (24-4); sharp_gap->away (15-12); money_moving->home (8-12); consensus_gap->away (9-20) |
| Sun 16:05 | Seattle Seahawks @ Las Vegas Raiders | total | under | +8.2 | 5-2 | 40.5 (-110) | 43.5 | 3 | 40.5 ($10,000) |  | over 76% | 24% / 30% | 28328 | follow_move->under (5-5); rlm->under (3-3); rlm_ratio->under (3-1); money_level->over (14-14); sharp_gap->under (13-16); money_moving->over (10-10); pin_rlm->under (3-1) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | moneyline | home | +6.4 | 4-1 | -178 (-178) | -108 | 12.1 | -184 ($30,000) |  |  | 85% / 88% | 25526 | follow_move->home (23-6); money_level->home (24-4); sharp_gap->home (15-12); money_moving->home (8-12); consensus_gap->away (9-20) |

## C  weighted edge 0 to +5

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 09:30 | New England Patriots @ Detroit Lions | moneyline | home | +4.8 | 3-2 | -146 (-146) | -105 | 8.1 | -145 ($30,000) |  |  | 83% / 93% | 42580 | follow_move->home (23-6); money_level->home (24-4); sharp_gap->home (15-12); money_moving->away (8-12); consensus_gap->away (9-20) |
| Sun 16:05 | Seattle Seahawks @ Las Vegas Raiders | moneyline | away | +4.8 | 3-2 | -300 (-300) | 100 | 21 | 235 ($20,000) |  |  | 96% / 99% | 28328 | follow_move->away (23-6); money_level->away (24-4); sharp_gap->away (15-12); money_moving->home (8-12); consensus_gap->home (9-20) |
| Sun 09:30 | New England Patriots @ Detroit Lions | total | under | +4.6 | 3-2 | 49.5 (-105) | 50.5 | 1 | 49 ($10,000) | +0.5 |  | 87% / 85% | 42580 | follow_move->under (5-5); money_level->under (14-14); sharp_gap->over (13-16); money_moving->over (10-10); pin_value->under (7-5) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | moneyline | away | +4.5 | 2-2 | -670 (-670) | -110 | 35.4 | 430 ($20,000) |  |  | 99% / 99% | 28444 | follow_move->away (23-6); money_level->away (24-4); consensus_gap->home (9-20); pin_value->home (2-5) |
| Sun 16:25 | San Francisco 49ers @ Dallas Cowboys | spread | home | +4.4 | 3-1 | 4.5 (-115) | 4.5 |  | 4 ($30,000) | +0.5 |  | 26% / 36% | 29792 | money_level->away (17-12); sharp_gap->home (10-18); money_moving->home (8-10); pin_value->home (10-2) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | moneyline | home | +4 | 3-2 | -210 (-210) | -110 | 15.4 | -203 ($20,000) |  |  | 86% / 83% | 20664 | follow_move->home (23-6); money_level->home (24-4); sharp_gap->away (15-12); money_moving->home (8-12); consensus_gap->away (9-20) |
| Sun 13:00 | Houston Texans @ Cleveland Browns | total | over | +2.2 | 3-1 | 40.5 (-105) | 39.5 | 1 | 40.5 ($10,000) |  |  | 55% / 53% | 24905 | follow_move->over (5-5); money_level->over (14-14); sharp_gap->under (13-16); money_moving->over (10-10) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | spread | home | +2 | 6-0 | -3.5 (-115) | -2.5 | 1 | -4 ($30,000) | +0.5 |  | 59% / 63% | 20664 | follow_move->home (9-14); money_level->home (17-12); sharp_gap->home (10-18); money_moving->home (8-10); consensus_gap->home (4-3); pin_value->home (10-2) |
| Sun 13:00 | Houston Texans @ Cleveland Browns | tt_home | under | +1.9 | 1-0 | 17.5 (-120) | 17.5 |  | 16.5 ($3,000) | +1 |  | 0% / 0% | 24905 | pin_value->under (11-9) |
| Sun 09:30 | New England Patriots @ Detroit Lions | tt_away | under | +0.9 | 1-0 | 23.5 (-100) | 24.5 | 1 | 23.5 ($3,000) |  |  | 0% / 0% | 42580 | follow_move->under (6-5) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | tt_away | over | +0.9 | 1-0 | 25.5 (-113) | 24.5 | 1 | 25.5 ($3,000) |  |  | 0% / 0% | 29161 | follow_move->over (6-5) |
| Sun 13:00 | Minnesota Vikings @ Green Bay Packers | tt_away | over | +0.6 | 1-1 | 19.5 (-130) | 17.5 | 2 | 16.5 ($3,000) | +3 |  | 0% / 0% | 31009 | follow_move->over (6-5); pin_value->under (9-9) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | tt_away | under | +0.6 | 1-1 | 16.5 (-113) | 19.5 | 3 | 20.5 ($3,000) | -4 |  | 0% / 0% | 20664 | follow_move->under (6-5); pin_value->over (9-9) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | tt_away | under | +0.3 | 1-0 | 28.5 (-115) | 28.5 |  | 27.5 ($3,000) | +1 |  | 0% / 0% | 28444 | pin_value->under (9-9) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | tt_away | over | +0.3 | 1-0 | 24.5 (-102) | 24.5 |  | 27.5 ($3,000) | -3 |  | 0% / 0% | 23097 | pin_value->over (9-9) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | tt_away | under | +0.3 | 1-0 | 22.5 (-100) | 22.5 |  | 21.5 ($3,000) | +1 |  | 0% / 0% | 25526 | pin_value->under (9-9) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | tt_home | under | +0.2 | 2-0 | 21.5 (-108) | 22.5 | 1 | 20.5 ($2,000) | +1 |  | 0% / 0% | 9663 | follow_move->under (5-6); pin_value->under (11-9) |

## D  no weighted edge (agreement is all unproven or negative signals)

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Carolina Panthers @ New Orleans Saints | total | over | -0.8 | 2-1 | 48.5 (-115) | 47.5 | 1 | 48.5 ($10,000) |  |  | 58% / 58% | 28363 | follow_move->over (5-5); money_level->over (14-14); money_moving->under (10-10) |
| Sun 13:00 | Buffalo Bills @ New York Jets | total | over | -0.9 | 4-0 | 50.5 (-115) | 50.5 |  | 51 ($10,000) | -0.5 |  | 55% / 66% | 29959 | money_level->over (14-14); sharp_gap->over (13-16); money_moving->over (10-10); pin_value->over (7-5) |
| Sun 16:25 | San Francisco 49ers @ Dallas Cowboys | total | over | -1.1 | 3-1 | 55.5 (-115) | 55.5 |  | 56 ($10,000) | -0.5 |  | 73% / 79% | 29792 | money_level->over (14-14); sharp_gap->over (13-16); money_moving->under (10-10); pin_value->over (7-5) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | total | over | -1.2 | 4-2 | 38.5 (-110) | 40.5 | 2 | 39.5 ($10,000) | -1 | over 61% | 61% / 63% | 23097 | follow_move->under (5-5); rlm->under (3-3); money_level->over (14-14); sharp_gap->over (13-16); money_moving->over (10-10); pin_value->over (7-5) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | total | under | -1.9 | 2-1 | 38.5 (-105) | 38.5 |  | 38.5 ($5,000) |  |  | 27% / 30% | 9663 | money_level->over (14-14); sharp_gap->under (13-16); money_moving->under (10-10) |
| Sun 13:00 | Houston Texans @ Cleveland Browns | moneyline | home | -2.4 | 3-2 | 180 (+180) | -108 | 16.2 | 193 ($20,000) |  |  | 8% / 9% | 24905 | follow_move->away (23-6); money_level->away (24-4); sharp_gap->home (15-12); money_moving->home (8-12); consensus_gap->home (9-20) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | total | under | -2.4 | 5-1 | 37.5 (-115) | 40.5 | 3 | 38 ($10,000) | -0.5 |  | 42% / 62% | 20664 | follow_move->under (5-5); rlm_ratio->under (3-1); money_level->under (14-14); sharp_gap->under (13-16); money_moving->under (10-10); pin_value->over (7-5) |
| Sun 13:00 | Buffalo Bills @ New York Jets | moneyline | home | -2.4 | 3-2 | 360 (+360) | -108 | 30.2 | 360 ($10,000) |  |  | 1% / 2% | 29959 | follow_move->away (23-6); money_level->away (24-4); sharp_gap->home (15-12); money_moving->home (8-12); consensus_gap->home (9-20) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | moneyline | away | -2.4 | 3-2 | 188 (+188) | -112 | 16.4 | -212 ($10,000) |  |  | 19% / 33% | 9663 | follow_move->home (23-6); money_level->home (24-4); sharp_gap->away (15-12); money_moving->away (8-12); consensus_gap->away (9-20) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | moneyline | home | -2.5 | 4-2 | 385 (+385) | -108 | 31.3 | 351 ($20,000) |  |  | 3% / 5% | 23097 | follow_move->away (23-6); money_level->away (24-4); sharp_gap->home (15-12); money_moving->home (8-12); consensus_gap->home (9-20); pin_value->home (2-5) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | spread | away | -2.8 | 2-2 | -10.5 (-110) | 10 | 0.5 | 10.5 ($30,000) |  |  | 90% / 79% | 28444 | follow_move->away (9-14); money_level->away (17-12); sharp_gap->home (10-18); money_moving->home (8-10) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | spread | away | -2.8 | 2-2 | -3.5 (-100) | 3 | 0.5 | 3.5 ($30,000) |  |  | 84% / 63% | 29161 | follow_move->away (9-14); money_level->away (17-12); sharp_gap->home (10-18); money_moving->home (8-10) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | tt_home | under | -3.6 | 1-1 | 16.5 (-104) | 17.5 | 1 | 17.5 ($3,000) | -1 |  | 0% / 0% | 28444 | follow_move->under (5-6); pin_value->over (11-9) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | tt_home | under | -3.6 | 1-1 | 20.5 (-118) | 21.5 | 1 | 21.5 ($3,000) | -1 |  | 0% / 0% | 20664 | follow_move->under (5-6); pin_value->over (11-9) |
| Sun 13:00 | Carolina Panthers @ New Orleans Saints | tt_home | over | -3.6 | 1-1 | 25.5 (-111) | 24.5 | 1 | 23.5 ($3,000) | +2 |  | 0% / 0% | 28363 | follow_move->over (5-6); pin_value->under (11-9) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | tt_home | over | -3.6 | 1-1 | 22.5 (-111) | 20.5 | 2 | 20.5 ($3,000) | +2 |  | 0% / 0% | 29161 | follow_move->over (5-6); pin_value->under (11-9) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | tt_home | under | -3.6 | 1-1 | 13.5 (-108) | 14.5 | 1 | 19.5 ($3,000) | -6 |  | 0% / 0% | 23097 | follow_move->under (5-6); pin_value->over (11-9) |
| Sun 16:05 | Seattle Seahawks @ Las Vegas Raiders | tt_home | under | -3.6 | 1-1 | 16.5 (-104) | 19.5 | 3 | 20.5 ($3,000) | -4 |  | 0% / 0% | 28328 | follow_move->under (5-6); pin_value->over (11-9) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | total | over | -3.7 | 2-1 | 46.5 (-100) | 46.5 |  | 46.5 ($10,000) |  |  | 59% / 67% | 28444 | money_level->over (14-14); sharp_gap->over (13-16); money_moving->under (10-10) |
| Sun 13:00 | Carolina Panthers @ New Orleans Saints | spread | home | -3.8 | 5-2 | -1.5 (-120) | 1.5 | 3 | -2.5 ($30,000) | +1 | away 70% | 30% / 23% | 28363 | follow_move->home (9-14); rlm->home (1-8); money_level->away (17-12); sharp_gap->away (10-18); money_moving->home (8-10); consensus_gap->home (4-3); pin_value->home (10-2) |
| Sun 13:00 | Minnesota Vikings @ Green Bay Packers | moneyline | away | -5.2 | 4-2 | 124 (+124) | -108 | 7.4 | -145 ($20,000) |  |  | 18% / 38% | 31009 | follow_move->home (23-6); money_level->home (24-4); sharp_gap->away (15-12); money_moving->away (8-12); consensus_gap->away (9-20); pin_rlm->away (1-5) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | moneyline | home | -5.2 | 4-2 | 144 (+144) | 100 | 9 | 155 ($20,000) |  |  | 3% / 14% | 29161 | follow_move->away (23-6); money_level->away (24-4); sharp_gap->home (15-12); money_moving->home (8-12); consensus_gap->home (9-20); pin_rlm->home (1-5) |
| Sun 16:25 | San Francisco 49ers @ Dallas Cowboys | moneyline | home | -5.2 | 4-2 | 184 (+184) | -108 | 16.7 | 181 ($20,000) |  |  | 5% / 10% | 29792 | follow_move->away (23-6); money_level->away (24-4); sharp_gap->home (15-12); money_moving->home (8-12); consensus_gap->home (9-20); pin_rlm->home (1-5) |
| Sun 13:00 | Minnesota Vikings @ Green Bay Packers | total | over | -6 | 4-1 | 42.5 (-105) | 40.5 | 2 | 42 ($10,000) | +0.5 |  | 59% / 70% | 31009 | follow_move->over (5-5); money_level->over (14-14); sharp_gap->over (13-16); money_moving->over (10-10); pin_value->under (7-5) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | total | over | -6.1 | 3-1 | 47.5 (-105) | 45.5 | 2 | 47 ($10,000) | +0.5 |  | 56% / 64% | 29161 | follow_move->over (5-5); money_level->over (14-14); sharp_gap->over (13-16); pin_value->under (7-5) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | total | over | -6.1 | 3-1 | 49.5 (-105) | 48.5 | 1 | 48.5 ($10,000) | +1 |  | 67% / 73% | 25526 | follow_move->over (5-5); money_level->over (14-14); sharp_gap->over (13-16); pin_value->under (7-5) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | spread | home | -8.6 | 7-0 | -4.5 (-110) | -2.5 | 2 | -4.5 ($20,000) |  | away 66% | 34% / 65% | 9663 | follow_move->home (9-14); rlm->home (1-8); rlm_ratio->home (0-4); money_level->home (17-12); sharp_gap->home (10-18); money_moving->home (8-10); pin_rlm->home (0-2) |
| Sun 09:30 | New England Patriots @ Detroit Lions | spread | home | -10.8 | 3-1 | -2.5 (-120) | -1.5 | 1 | -2.5 ($50,000) |  |  | 48% / 53% | 42580 | follow_move->home (9-14); money_level->home (17-12); sharp_gap->home (10-18); money_moving->away (8-10) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | spread | away | -10.8 | 3-1 | -9.5 (-110) | 8.5 | 1 | 9.5 ($30,000) |  |  | 77% / 79% | 23097 | follow_move->away (9-14); money_level->away (17-12); sharp_gap->away (10-18); money_moving->home (8-10) |
| Sun 16:05 | Seattle Seahawks @ Las Vegas Raiders | spread | away | -10.8 | 3-1 | -6.5 (-110) | 3 | 3.5 | 6.5 ($30,000) |  |  | 79% / 82% | 28328 | follow_move->away (9-14); money_level->away (17-12); sharp_gap->away (10-18); money_moving->home (8-10) |
| Sun 13:00 | Houston Texans @ Cleveland Browns | spread | away | -13.3 | 3-1 | -4.5 (-110) | 3.5 | 1 | 4 ($30,000) | +0.5 |  | 74% / 74% | 24905 | follow_move->away (9-14); money_level->away (17-12); money_moving->away (8-10); pin_value->home (10-2) |
| Sun 13:00 | Minnesota Vikings @ Green Bay Packers | spread | away | -17.3 | 2-2 | 2.5 (-100) | -3 | 0.5 | -3 ($30,000) | +0.5 |  | 42% / 42% | 31009 | follow_move->away (9-14); money_level->home (17-12); money_moving->away (8-10); pin_value->home (10-2) |
| Sun 13:00 | Buffalo Bills @ New York Jets | spread | home | -20.7 | 5-2 | 7.5 (-110) | 8.5 | 1 | 8.5 ($30,000) | -1 | away 93% | 7% / 11% | 29959 | follow_move->home (9-14); rlm->home (1-8); rlm_ratio->home (0-4); money_level->away (17-12); sharp_gap->home (10-18); money_moving->home (8-10); pin_value->away (10-2) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | spread | away | -24.6 | 3-2 | 3.5 (-110) | -4 | 0.5 | -3.5 ($50,000) |  | home 60% | 40% / 42% | 25526 | follow_move->away (9-14); rlm->away (1-8); money_level->home (17-12); sharp_gap->away (10-18); money_moving->home (8-10) |

