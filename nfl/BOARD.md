# NFL board

Generated 2026-11-15 16:32 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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
| PINNACLE moved vs public | Kansas City Chiefs @ Atlanta Falcons | moneyline | home | 144 | 170 | 4% | 2.25 | 4-8 |
| PINNACLE moved vs public | Los Angeles Chargers @ Baltimore Ravens | spread | home | -4.5 | -3.5 | 35% | 1.8 | 4-8 |
| PINNACLE moved vs public | Minnesota Vikings @ Green Bay Packers | moneyline | away | 124 | -221 | 19% | 1.89 | 4-8 |
| PINNACLE moved vs public | San Francisco 49ers @ Dallas Cowboys | moneyline | home | 198 | 182 | 5% | 2.0 | 4-8 |
| FanDuel moved vs public | Buffalo Bills @ New York Jets | spread | home | 7.5 | 8.5 | 7% | 1.43 | 3-6 |
| FanDuel moved vs public | Los Angeles Chargers @ Baltimore Ravens | spread | home | -4.5 | -2.5 | 35% | 1.8 | 3-6 |

Ranked by **weighted edge**: each agreeing signal contributes its own
base-rate-corrected edge, and contributes nothing until it has 30 decided
outcomes. Raw agreement count is shown too, but it is the weaker number — a
market can have seven signals agreeing where four of them have losing records.

## B  weighted edge +5 to +10

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Houston Texans @ Cleveland Browns | moneyline | away | +6.4 | 4-1 | -230 (-230) | -108 | 17.4 | 194 ($20,000) |  |  | 91% / 94% | 34401 | follow_move->away (23-6); money_level->away (24-4); sharp_gap->away (15-12); money_moving->away (8-12); consensus_gap->home (9-20) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | moneyline | home | +6.4 | 4-1 | -180 (-180) | -108 | 12.4 | -182 ($50,000) |  |  | 85% / 92% | 34699 | follow_move->home (23-6); money_level->home (24-4); sharp_gap->home (15-12); money_moving->home (8-12); consensus_gap->away (9-20) |
| Sun 13:00 | Carolina Panthers @ New Orleans Saints | moneyline | away | +5.2 | 4-1 | -108 (-108) | -108 |  | -110 ($50,000) |  |  | 50% / 66% | 39910 | money_level->away (24-4); sharp_gap->away (15-12); money_moving->away (8-12); consensus_gap->away (9-20); book_lag->home (0-0) |

## C  weighted edge 0 to +5

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 16:05 | Seattle Seahawks @ Las Vegas Raiders | moneyline | away | +4.9 | 3-3 | -300 (-300) | 100 | 21 | 233 ($20,000) |  |  | 96% / 99% | 37845 | follow_move->away (23-6); money_level->away (24-4); sharp_gap->away (15-12); money_moving->home (8-12); consensus_gap->home (9-20); pin_value->home (2-5) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | moneyline | away | +4.5 | 2-2 | -700 (-700) | -110 | 35.7 | 429 ($20,000) |  |  | 99% / 99% | 41364 | follow_move->away (23-6); money_level->away (24-4); consensus_gap->home (9-20); pin_value->home (2-5) |
| Sun 16:25 | San Francisco 49ers @ Dallas Cowboys | spread | home | +4.4 | 3-1 | 4.5 (-105) | 4.5 |  | 4 ($75,000) | +0.5 |  | 27% / 38% | 41460 | money_level->away (17-12); sharp_gap->home (10-18); money_moving->home (8-10); pin_value->home (10-2) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | moneyline | home | +4 | 3-2 | -210 (-210) | -110 | 15.4 | -206 ($30,000) |  |  | 86% / 84% | 29307 | follow_move->home (23-6); money_level->home (24-4); sharp_gap->away (15-12); money_moving->home (8-12); consensus_gap->away (9-20) |
| Sun 13:00 | Buffalo Bills @ New York Jets | moneyline | away | +3.6 | 2-2 | -450 (-450) | -108 | 29.7 | 382 ($10,000) |  |  | 99% / 99% | 43535 | follow_move->away (23-6); money_level->away (24-4); money_moving->home (8-12); consensus_gap->home (9-20) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | total | under | +3.6 | 3-2 | 38.5 (-110) | 40.5 | 2 | 38 ($15,000) | +0.5 | over 62% | 38% / 38% | 31110 | follow_move->under (5-5); rlm->under (3-3); money_level->over (14-14); money_moving->over (10-10); pin_value->under (7-5) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | total | over | +2 | 1-1 | 38.5 (-115) | 38.5 |  | 38.5 ($5,000) |  |  | 72% / 70% | 11273 | money_level->over (14-14); sharp_gap->under (13-16) |
| Sun 13:00 | Houston Texans @ Cleveland Browns | tt_home | under | +1.9 | 1-0 | 17.5 (-113) | 17.5 |  | 16.5 ($5,000) | +1 |  | 0% / 0% | 34401 | pin_value->under (11-9) |
| Sun 13:00 | Carolina Panthers @ New Orleans Saints | tt_home | under | +1.9 | 1-0 | 24.5 (-122) | 24.5 |  | 23.5 ($5,000) | +1 |  | 0% / 0% | 39910 | pin_value->under (11-9) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | tt_away | over | +0.9 | 1-0 | 25.5 (-115) | 24.5 | 1 | 25.5 ($5,000) |  |  | 0% / 0% | 41242 | follow_move->over (6-5) |
| Sun 13:00 | Houston Texans @ Cleveland Browns | tt_away | over | +0.6 | 1-1 | 23.5 (-102) | 22.5 | 1 | 22.5 ($5,000) | +1 |  | 0% / 0% | 34401 | follow_move->over (6-5); pin_value->under (9-9) |
| Sun 13:00 | Minnesota Vikings @ Green Bay Packers | tt_away | over | +0.6 | 1-1 | 19.5 (-130) | 17.5 | 2 | 16.5 ($5,000) | +3 |  | 0% / 0% | 44686 | follow_move->over (6-5); pin_value->under (9-9) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | tt_away | under | +0.6 | 1-1 | 16.5 (-108) | 19.5 | 3 | 20.5 ($5,000) | -4 |  | 0% / 0% | 29307 | follow_move->under (6-5); pin_value->over (9-9) |
| Sun 13:00 | Carolina Panthers @ New Orleans Saints | tt_away | over | +0.6 | 1-1 | 24.5 (-104) | 23.5 | 1 | 23.5 ($5,000) | +1 |  | 0% / 0% | 39910 | follow_move->over (6-5); pin_value->under (9-9) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | tt_away | under | +0.3 | 1-0 | 28.5 (-113) | 28.5 |  | 27.5 ($5,000) | +1 |  | 0% / 0% | 41364 | pin_value->under (9-9) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | tt_away | over | +0.3 | 1-0 | 24.5 (-102) | 24.5 |  | 27.5 ($5,000) | -3 |  | 0% / 0% | 31110 | pin_value->over (9-9) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | tt_away | under | +0.3 | 1-0 | 22.5 (-100) | 22.5 |  | 21.5 ($5,000) | +1 |  | 0% / 0% | 34699 | pin_value->under (9-9) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | tt_home | under | +0.2 | 2-0 | 21.5 (-111) | 22.5 | 1 | 20.5 ($2,000) | +1 |  | 0% / 0% | 11273 | follow_move->under (5-6); pin_value->under (11-9) |

## D  no weighted edge (agreement is all unproven or negative signals)

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Buffalo Bills @ New York Jets | total | over | -0.9 | 4-0 | 50.5 (-115) | 50.5 |  | 51 ($15,000) | -0.5 |  | 58% / 69% | 43535 | money_level->over (14-14); sharp_gap->over (13-16); money_moving->over (10-10); pin_value->over (7-5) |
| Sun 16:25 | San Francisco 49ers @ Dallas Cowboys | total | over | -1.1 | 3-1 | 55.5 (-115) | 55.5 |  | 56 ($15,000) | -0.5 |  | 74% / 77% | 41460 | money_level->over (14-14); sharp_gap->over (13-16); money_moving->under (10-10); pin_value->over (7-5) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | spread | away | -1.7 | 4-1 | -9.5 (-110) | 8.5 | 1 | 10.5 ($75,000) | -1 |  | 77% / 80% | 31110 | follow_move->away (9-14); money_level->away (17-12); sharp_gap->away (10-18); money_moving->home (8-10); pin_value->away (10-2) |
| Sun 16:05 | Seattle Seahawks @ Las Vegas Raiders | total | under | -1.8 | 3-2 | 40.5 (-110) | 43.5 | 3 | 40.5 ($15,000) |  | over 74% | 26% / 30% | 37845 | follow_move->under (5-5); rlm->under (3-3); money_level->over (14-14); sharp_gap->under (13-16); money_moving->over (10-10) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | moneyline | home | -2.4 | 3-2 | 385 (+385) | -108 | 31.3 | 373 ($20,000) |  |  | 3% / 7% | 31110 | follow_move->away (23-6); money_level->away (24-4); sharp_gap->home (15-12); money_moving->home (8-12); consensus_gap->home (9-20) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | moneyline | away | -2.4 | 3-2 | 184 (+184) | -112 | 15.9 | -212 ($10,000) |  |  | 18% / 34% | 11273 | follow_move->home (23-6); money_level->home (24-4); sharp_gap->away (15-12); money_moving->away (8-12); consensus_gap->away (9-20) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | spread | away | -2.8 | 2-2 | -10.5 (-110) | 10 | 0.5 | 10.5 ($75,000) |  |  | 90% / 83% | 41364 | follow_move->away (9-14); money_level->away (17-12); sharp_gap->home (10-18); money_moving->home (8-10) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | spread | away | -2.8 | 2-2 | -3.5 (-100) | 3 | 0.5 | 3.5 ($75,000) |  |  | 81% / 62% | 41242 | follow_move->away (9-14); money_level->away (17-12); sharp_gap->home (10-18); money_moving->home (8-10) |
| Sun 13:00 | Houston Texans @ Cleveland Browns | total | over | -3.2 | 3-1 | 41.5 (-100) | 39.5 | 2 | 41 ($15,000) | +0.5 |  | 57% / 57% | 34401 | follow_move->over (5-5); money_level->over (14-14); money_moving->over (10-10); pin_value->under (7-5) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | total | over | -3.4 | 4-0 | 47.5 (-110) | 45.5 | 2 | 47.5 ($15,000) |  |  | 58% / 71% | 41242 | follow_move->over (5-5); money_level->over (14-14); sharp_gap->over (13-16); money_moving->over (10-10) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | tt_home | under | -3.6 | 1-1 | 16.5 (-106) | 17.5 | 1 | 17.5 ($5,000) | -1 |  | 0% / 0% | 41364 | follow_move->under (5-6); pin_value->over (11-9) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | tt_home | under | -3.6 | 1-1 | 20.5 (-111) | 21.5 | 1 | 21.5 ($5,000) | -1 |  | 0% / 0% | 29307 | follow_move->under (5-6); pin_value->over (11-9) |
| Sun 13:00 | Carolina Panthers @ New Orleans Saints | total | over | -3.6 | 3-1 | 48.5 (-115) | 47.5 | 1 | 48.5 ($15,000) |  |  | 60% / 61% | 39910 | follow_move->over (5-5); money_level->over (14-14); sharp_gap->over (13-16); money_moving->under (10-10) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | tt_home | over | -3.6 | 1-1 | 22.5 (-113) | 20.5 | 2 | 20.5 ($5,000) | +2 |  | 0% / 0% | 41242 | follow_move->over (5-6); pin_value->under (11-9) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | tt_home | under | -3.6 | 1-1 | 13.5 (-108) | 14.5 | 1 | 19.5 ($5,000) | -6 |  | 0% / 0% | 31110 | follow_move->under (5-6); pin_value->over (11-9) |
| Sun 16:05 | Seattle Seahawks @ Las Vegas Raiders | tt_home | under | -3.6 | 1-1 | 16.5 (-104) | 19.5 | 3 | 20.5 ($5,000) | -4 |  | 0% / 0% | 37845 | follow_move->under (5-6); pin_value->over (11-9) |
| Sun 16:25 | San Francisco 49ers @ Dallas Cowboys | tt_home | under | -3.6 | 1-1 | 25.5 (-111) | 26.5 | 1 | 26.5 ($5,000) | -1 |  | 0% / 0% | 41460 | follow_move->under (5-6); pin_value->over (11-9) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | total | under | -4.4 | 3-2 | 37.5 (-110) | 40.5 | 3 | 38 ($15,000) | -0.5 |  | 41% / 48% | 29307 | follow_move->under (5-5); money_level->over (14-14); sharp_gap->under (13-16); money_moving->under (10-10); pin_value->over (7-5) |
| Sun 13:00 | Minnesota Vikings @ Green Bay Packers | moneyline | away | -5.2 | 4-2 | 124 (+124) | -108 | 7.4 | -145 ($50,000) |  |  | 19% / 36% | 44686 | follow_move->home (23-6); money_level->home (24-4); sharp_gap->away (15-12); money_moving->away (8-12); consensus_gap->away (9-20); pin_rlm->away (1-5) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | moneyline | home | -5.2 | 4-2 | 144 (+144) | 100 | 9 | 161 ($50,000) |  |  | 4% / 9% | 41242 | follow_move->away (23-6); money_level->away (24-4); sharp_gap->home (15-12); money_moving->home (8-12); consensus_gap->home (9-20); pin_rlm->home (1-5) |
| Sun 16:25 | San Francisco 49ers @ Dallas Cowboys | moneyline | home | -5.3 | 5-2 | 198 (+198) | -108 | 18.4 | 179 ($50,000) |  |  | 5% / 10% | 41460 | follow_move->away (23-6); money_level->away (24-4); sharp_gap->home (15-12); money_moving->home (8-12); consensus_gap->home (9-20); pin_value->home (2-5); pin_rlm->home (1-5) |
| Sun 13:00 | Minnesota Vikings @ Green Bay Packers | total | over | -6 | 4-1 | 42.5 (-105) | 40.5 | 2 | 42 ($10,000) | +0.5 |  | 61% / 71% | 44686 | follow_move->over (5-5); money_level->over (14-14); sharp_gap->over (13-16); money_moving->over (10-10); pin_value->under (7-5) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | total | over | -6.2 | 3-2 | 49.5 (-105) | 48.5 | 1 | 48.5 ($15,000) | +1 |  | 68% / 73% | 34699 | follow_move->over (5-5); money_level->over (14-14); sharp_gap->over (13-16); money_moving->under (10-10); pin_value->under (7-5) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | total | over | -6.3 | 2-2 | 46.5 (-100) | 46.5 |  | 45 ($15,000) | +1.5 |  | 61% / 68% | 41364 | money_level->over (14-14); sharp_gap->over (13-16); money_moving->under (10-10); pin_value->under (7-5) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | spread | home | -8.2 | 4-0 | -4.5 (-105) | -2.5 | 2 | -4.5 ($75,000) |  |  | 58% / 61% | 29307 | follow_move->home (9-14); money_level->home (17-12); sharp_gap->home (10-18); money_moving->home (8-10) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | spread | home | -8.6 | 7-0 | -4.5 (-110) | -2.5 | 2 | -4.5 ($20,000) |  | away 65% | 35% / 63% | 11273 | follow_move->home (9-14); rlm->home (1-8); rlm_ratio->home (0-4); money_level->home (17-12); sharp_gap->home (10-18); money_moving->home (8-10); pin_rlm->home (0-2) |
| Sun 13:00 | Houston Texans @ Cleveland Browns | spread | away | -9.3 | 3-2 | -4.5 (-110) | 3.5 | 1 | 4 ($75,000) | +0.5 |  | 70% / 69% | 34401 | follow_move->away (9-14); money_level->away (17-12); sharp_gap->home (10-18); money_moving->away (8-10); pin_value->home (10-2) |
| Sun 16:05 | Seattle Seahawks @ Las Vegas Raiders | spread | away | -10.8 | 3-1 | -6.5 (-110) | 3 | 3.5 | 6.5 ($75,000) |  |  | 76% / 79% | 37845 | follow_move->away (9-14); money_level->away (17-12); sharp_gap->away (10-18); money_moving->home (8-10) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | spread | away | -14.8 | 2-2 | 3.5 (-110) | -4 | 0.5 | -3.5 ($75,000) |  |  | 43% / 45% | 34699 | follow_move->away (9-14); money_level->home (17-12); sharp_gap->away (10-18); money_moving->home (8-10) |
| Sun 13:00 | Buffalo Bills @ New York Jets | spread | home | -20.7 | 5-2 | 7.5 (-110) | 8.5 | 1 | 8.5 ($75,000) | -1 | away 93% | 7% / 10% | 43535 | follow_move->home (9-14); rlm->home (1-8); rlm_ratio->home (0-4); money_level->away (17-12); sharp_gap->home (10-18); money_moving->home (8-10); pin_value->away (10-2) |
| Sun 13:00 | Minnesota Vikings @ Green Bay Packers | spread | away | -21.3 | 3-2 | 2.5 (-100) | -3 | 0.5 | -3 ($75,000) | +0.5 |  | 43% / 45% | 44686 | follow_move->away (9-14); money_level->home (17-12); sharp_gap->away (10-18); money_moving->away (8-10); pin_value->home (10-2) |
| Sun 13:00 | Carolina Panthers @ New Orleans Saints | spread | home | -23.1 | 3-3 | -1.5 (-100) | 1.5 | 3 | -1 ($75,000) | -0.5 | away 70% | 30% / 21% | 39910 | follow_move->home (9-14); rlm->home (1-8); money_level->away (17-12); sharp_gap->away (10-18); money_moving->home (8-10); pin_value->away (10-2) |

