# NFL board

Generated 2026-11-13 07:08 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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
| PINNACLE moved vs public | Los Angeles Chargers @ Baltimore Ravens | spread | home | -4.5 | -3.5 | 31% | 2.23 | 3-8 |
| PINNACLE moved vs public | Minnesota Vikings @ Green Bay Packers | moneyline | away | 138 | -221 | 14% | 1.64 | 3-8 |
| PINNACLE moved vs public | Pittsburgh Steelers @ Cincinnati Bengals | moneyline | away | 154 | -190 | 14% | 1.86 | 3-8 |
| FanDuel moved vs public | Buffalo Bills @ New York Jets | spread | home | 7.5 | 8.5 | 8% | 1.88 | 3-6 |
| FanDuel moved vs public | Los Angeles Chargers @ Baltimore Ravens | spread | home | -4.5 | -2.5 | 31% | 2.23 | 3-6 |
| FanDuel moved vs public | New England Patriots @ Detroit Lions | spread | home | -2.5 | -1.5 | 29% | 1.59 | 3-6 |

Ranked by **weighted edge**: each agreeing signal contributes its own
base-rate-corrected edge, and contributes nothing until it has 30 decided
outcomes. Raw agreement count is shown too, but it is the weaker number — a
market can have seven signals agreeing where four of them have losing records.

## B  weighted edge +5 to +10

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Houston Texans @ Cleveland Browns | spread | away | +8.7 | 4-1 | -4.5 (-115) | 3.5 | 1 | 5 ($20,000) | -0.5 |  | 80% / 78% | 9976 | follow_move->away (9-14); money_level->away (16-12); sharp_gap->home (9-18); money_moving->away (7-10); pin_value->away (10-1) |
| Sun 16:25 | San Francisco 49ers @ Dallas Cowboys | spread | home | +6.9 | 4-1 | 4.5 (-120) | 4.5 |  | 4 ($30,000) | +0.5 |  | 22% / 32% | 12015 | money_level->away (16-12); sharp_gap->home (9-18); money_moving->home (7-10); consensus_gap->home (4-3); pin_value->home (10-1) |
| Sun 13:00 | Carolina Panthers @ New Orleans Saints | moneyline | away | +6.3 | 4-1 | 112 (+112) | -108 | 5 | -137 ($10,000) |  |  | 54% / 75% | 10062 | follow_move->home (23-5); money_level->away (24-4); sharp_gap->away (14-12); money_moving->away (7-12); consensus_gap->away (8-20) |

## C  weighted edge 0 to +5

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Houston Texans @ Cleveland Browns | total | over | +4.5 | 2-2 | 40.5 (-105) | 39.5 | 1 | 40.5 ($5,000) |  |  | 49% / 40% | 9976 | follow_move->over (5-4); money_level->under (14-14); sharp_gap->under (13-15); money_moving->over (10-9) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | moneyline | home | +4.1 | 2-2 | -215 (-215) | -110 | 15.9 | -199 ($10,000) |  |  | 84% / 74% | 7860 | follow_move->home (23-5); money_level->home (24-4); sharp_gap->away (14-12); consensus_gap->away (8-20) |
| Sun 09:30 | New England Patriots @ Detroit Lions | moneyline | home | +3.5 | 3-2 | -152 (-152) | -105 | 9.1 | -146 ($20,000) |  |  | 80% / 95% | 12293 | follow_move->home (23-5); money_level->home (24-4); sharp_gap->home (14-12); money_moving->away (7-12); consensus_gap->away (8-20) |
| Sun 13:00 | Houston Texans @ Cleveland Browns | moneyline | away | +3.5 | 3-2 | -235 (-235) | -108 | 17.9 | 190 ($10,000) |  |  | 92% / 93% | 9976 | follow_move->away (23-5); money_level->away (24-4); sharp_gap->away (14-12); money_moving->home (7-12); consensus_gap->home (8-20) |
| Sun 16:05 | Seattle Seahawks @ Las Vegas Raiders | moneyline | away | +3.5 | 3-2 | -290 (-290) | 100 | 20.1 | 237 ($10,000) |  |  | 95% / 96% | 11137 | follow_move->away (23-5); money_level->away (24-4); sharp_gap->away (14-12); money_moving->home (7-12); consensus_gap->home (8-20) |
| Sun 13:00 | Minnesota Vikings @ Green Bay Packers | tt_away | over | +3.1 | 1-1 | 19.5 (-122) | 17.5 | 2 | 16.5 ($1,000) | +3 |  | 0% / 0% | 10622 | follow_move->over (6-4); pin_value->under (8-9) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | tt_away | under | +3.1 | 1-1 | 16.5 (-102) | 19.5 | 3 | 20.5 ($2,000) | -4 |  | 0% / 0% | 7860 | follow_move->under (6-4); pin_value->over (8-9) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | tt_away | over | +3.1 | 1-1 | 23.5 (-102) | 22.5 | 1 | 21.5 ($2,000) | +2 |  | 0% / 0% | 10127 | follow_move->over (6-4); pin_value->under (8-9) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | moneyline | away | +2.3 | 4-1 | -174 (-174) | 100 | 9.3 | 154 ($10,000) |  |  | 97% / 99% | 11480 | follow_move->away (23-5); money_level->away (24-4); sharp_gap->away (14-12); money_moving->away (7-12); consensus_gap->home (8-20) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | tt_away | over | +2.3 | 1-0 | 25.5 (-113) | 24.5 | 1 | 25.5 ($2,000) |  |  | 0% / 0% | 11480 | follow_move->over (6-4) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | total | under | +2.3 | 2-2 | 39.5 (-110) | 40.5 | 1 | 39.5 ($5,000) |  |  | 57% / 56% | 9158 | follow_move->under (5-4); money_level->under (14-14); sharp_gap->over (13-15); money_moving->over (10-9) |
| Sun 16:25 | San Francisco 49ers @ Dallas Cowboys | moneyline | away | +2.3 | 4-1 | -210 (-210) | -108 | 15.7 | 176 ($20,000) |  |  | 95% / 96% | 12015 | follow_move->away (23-5); money_level->away (24-4); sharp_gap->away (14-12); money_moving->away (7-12); consensus_gap->home (8-20) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | total | under | +1.8 | 3-2 | 37.5 (-105) | 40.5 | 3 | 38 ($5,000) | -0.5 |  | 57% / 56% | 7860 | follow_move->under (5-4); money_level->under (14-14); sharp_gap->over (13-15); money_moving->under (10-9); pin_value->over (7-5) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | total | over | +1.1 | 2-0 | 38.5 (-115) | 38.5 |  | 38.5 ($5,000) |  |  | 73% / 73% | 5356 | money_level->over (14-14); money_moving->over (10-9) |
| Sun 13:00 | Houston Texans @ Cleveland Browns | tt_home | under | +0.5 | 1-0 | 17.5 (-125) | 17.5 |  | 16.5 ($2,000) | +1 |  | 0% / 0% | 9976 | pin_value->under (10-9) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | tt_home | over | +0.5 | 1-0 | 14.5 (-102) | 14.5 |  | 19.5 ($2,000) | -5 |  | 0% / 0% | 9158 | pin_value->over (10-9) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | total | under | +0.4 | 3-2 | 49.5 (-110) | 48.5 | 1 | 48.5 ($5,000) | +1 |  | 26% / 29% | 10127 | follow_move->over (5-4); money_level->over (14-14); sharp_gap->under (13-15); money_moving->under (10-9); pin_value->under (7-5) |
| Sun 13:00 | Buffalo Bills @ New York Jets | total | under | +0.3 | 2-2 | 50.5 (-100) | 50.5 |  | 51 ($5,000) | -0.5 |  | 62% / 60% | 11263 | money_level->under (14-14); sharp_gap->over (13-15); money_moving->under (10-9); pin_value->over (7-5) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | tt_home | under | +0.2 | 2-0 | 21.5 (-108) | 22.5 | 1 | 20.5 ($2,000) | +1 |  | 0% / 0% | 5356 | follow_move->under (5-5); pin_value->under (10-9) |

## D  no weighted edge (agreement is all unproven or negative signals)

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 16:25 | San Francisco 49ers @ Dallas Cowboys | total | over | -0.3 | 3-1 | 55.5 (-115) | 55.5 |  | 56 ($5,000) | -0.5 |  | 72% / 80% | 12015 | money_level->over (14-14); sharp_gap->over (13-15); money_moving->under (10-9); pin_value->over (7-5) |
| Sun 09:30 | New England Patriots @ Detroit Lions | tt_away | under | -0.8 | 1-0 | 24.5 (-125) | 24.5 |  | 23.5 ($2,000) | +1 |  | 0% / 0% | 12293 | pin_value->under (8-9) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | tt_home | under | -0.8 | 1-1 | 16.5 (-102) | 17.5 | 1 | 17.5 ($2,000) | -1 |  | 0% / 0% | 9592 | follow_move->under (5-5); pin_value->over (10-9) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | tt_away | under | -0.8 | 1-0 | 28.5 (-113) | 28.5 |  | 27.5 ($2,000) | +1 |  | 0% / 0% | 9592 | pin_value->under (8-9) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | tt_home | under | -0.8 | 1-1 | 20.5 (-104) | 21.5 | 1 | 21.5 ($2,000) | -1 |  | 0% / 0% | 7860 | follow_move->under (5-5); pin_value->over (10-9) |
| Sun 13:00 | Carolina Panthers @ New Orleans Saints | tt_home | over | -0.8 | 1-1 | 25.5 (-111) | 24.5 | 1 | 23.5 ($2,000) | +2 |  | 0% / 0% | 10062 | follow_move->over (5-5); pin_value->under (10-9) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | tt_home | over | -0.8 | 1-1 | 22.5 (-111) | 20.5 | 2 | 20.5 ($2,000) | +2 |  | 0% / 0% | 11480 | follow_move->over (5-5); pin_value->under (10-9) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | tt_away | over | -0.8 | 1-0 | 24.5 (-113) | 24.5 |  | 27.5 ($2,000) | -3 |  | 0% / 0% | 9158 | pin_value->over (8-9) |
| Sun 16:05 | Seattle Seahawks @ Las Vegas Raiders | tt_home | under | -0.8 | 1-1 | 16.5 (-102) | 19.5 | 3 | 20.5 ($2,000) | -4 |  | 0% / 0% | 11137 | follow_move->under (5-5); pin_value->over (10-9) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | spread | home | -1.1 | 5-0 | -3.5 (-115) | -2.5 | 1 | -4 ($20,000) | +0.5 |  | 54% / 57% | 7860 | follow_move->home (9-14); money_level->home (16-12); sharp_gap->home (9-18); money_moving->home (7-10); pin_value->home (10-1) |
| Sun 16:05 | Seattle Seahawks @ Las Vegas Raiders | total | under | -1.5 | 3-2 | 40.5 (-110) | 43.5 | 3 | 40.5 ($5,000) |  | over 75% | 25% / 29% | 11137 | follow_move->under (5-4); rlm->under (3-3); money_level->over (14-14); sharp_gap->under (13-15); money_moving->over (10-9) |
| Sun 13:00 | Minnesota Vikings @ Green Bay Packers | total | over | -2 | 4-1 | 42.5 (-105) | 40.5 | 2 | 42 ($3,000) | +0.5 |  | 53% / 55% | 10622 | follow_move->over (5-4); money_level->over (14-14); sharp_gap->over (13-15); money_moving->over (10-9); pin_value->under (7-5) |
| Sun 13:00 | Carolina Panthers @ New Orleans Saints | total | under | -2.3 | 3-1 | 48.5 (-105) | 47.5 | 1 | 48.5 ($5,000) |  |  | 49% / 51% | 10062 | follow_move->over (5-4); money_level->under (14-14); sharp_gap->under (13-15); money_moving->under (10-9) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | spread | away | -2.7 | 2-2 | -3.5 (-100) | 3 | 0.5 | 3.5 ($20,000) |  |  | 89% / 80% | 11480 | follow_move->away (9-14); money_level->away (16-12); sharp_gap->home (9-18); money_moving->home (7-10) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | total | over | -3 | 2-1 | 46.5 (-100) | 46.5 |  | 46.5 ($5,000) |  |  | 47% / 54% | 9592 | money_level->over (14-14); sharp_gap->over (13-15); money_moving->under (10-9) |
| Sun 09:30 | New England Patriots @ Detroit Lions | total | under | -3.5 | 3-1 | 50.5 (-105) | 50.5 |  | 51 ($5,000) | -0.5 |  | 89% / 90% | 12293 | money_level->under (14-14); sharp_gap->under (13-15); money_moving->under (10-9); pin_value->over (7-5) |
| Sun 13:00 | Buffalo Bills @ New York Jets | moneyline | home | -3.8 | 3-2 | 370 (+370) | -108 | 30.6 | 336 ($10,000) |  |  | 1% / 1% | 11263 | follow_move->away (23-5); money_level->away (24-4); money_moving->home (7-12); consensus_gap->home (8-20); pin_value->home (2-5) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | total | over | -4.2 | 3-2 | 47.5 (-105) | 45.5 | 2 | 47 ($5,000) | +0.5 |  | 50% / 51% | 11480 | follow_move->over (5-4); money_level->over (14-14); sharp_gap->over (13-15); money_moving->under (10-9); pin_value->under (7-5) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | moneyline | home | -4.4 | 4-2 | 500 (+500) | -110 | 35.7 | 427 ($10,000) |  |  | 1% / 2% | 9592 | follow_move->away (23-5); money_level->away (24-4); sharp_gap->home (14-12); money_moving->home (7-12); consensus_gap->home (8-20); pin_value->home (2-5) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | moneyline | home | -4.4 | 4-2 | 410 (+410) | -108 | 32.3 | 352 ($10,000) |  |  | 2% / 4% | 9158 | follow_move->away (23-5); money_level->away (24-4); sharp_gap->home (14-12); money_moving->home (7-12); consensus_gap->home (8-20); pin_value->home (2-5) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | moneyline | away | -4.7 | 3-2 | 188 (+188) | -112 | 15.9 | -212 ($10,000) |  |  | 17% / 31% | 5356 | follow_move->home (23-5); money_level->home (24-4); sharp_gap->away (14-12); money_moving->away (7-12); consensus_gap->away (8-20) |
| Sun 13:00 | Minnesota Vikings @ Green Bay Packers | spread | home | -5.7 | 2-2 | -3 (-110) | -3 |  | -3 ($10,000) |  |  | 58% / 62% | 10622 | money_level->home (16-12); sharp_gap->home (9-18); money_moving->away (7-10); consensus_gap->away (4-3) |
| Sun 13:00 | Minnesota Vikings @ Green Bay Packers | moneyline | away | -6.5 | 4-2 | 138 (+138) | -108 | 10.2 | -156 ($6,000) |  |  | 14% / 23% | 10622 | follow_move->home (23-5); money_level->home (24-4); sharp_gap->away (14-12); money_moving->away (7-12); consensus_gap->away (8-20); pin_rlm->away (0-5) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | moneyline | away | -6.5 | 4-2 | 154 (+154) | -108 | 12.9 | -180 ($20,000) |  |  | 14% / 26% | 10127 | follow_move->home (23-5); money_level->home (24-4); sharp_gap->away (14-12); money_moving->away (7-12); consensus_gap->away (8-20); pin_rlm->away (0-5) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | spread | home | -10.2 | 7-0 | -4.5 (-110) | -2.5 | 2 | -4.5 ($20,000) |  | away 69% | 31% / 69% | 5356 | follow_move->home (9-14); rlm->home (1-8); rlm_ratio->home (0-4); money_level->home (16-12); sharp_gap->home (9-18); money_moving->home (7-10); pin_rlm->home (0-2) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | spread | away | -12.1 | 4-0 | -10.5 (-110) | 10 | 0.5 | 10.5 ($20,000) |  |  | 92% / 95% | 9592 | follow_move->away (9-14); money_level->away (16-12); sharp_gap->away (9-18); money_moving->away (7-10) |
| Sun 09:30 | New England Patriots @ Detroit Lions | spread | home | -12.4 | 4-2 | -2.5 (-120) | -1.5 | 1 | -2.5 ($30,000) |  | away 71% | 29% / 46% | 12293 | follow_move->home (9-14); rlm->home (1-8); rlm_ratio->home (0-4); money_level->away (16-12); sharp_gap->home (9-18); money_moving->away (7-10) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | spread | away | -12.5 | 3-1 | -9.5 (-110) | 8.5 | 1 | 9.5 ($20,000) |  |  | 77% / 82% | 9158 | follow_move->away (9-14); money_level->away (16-12); sharp_gap->away (9-18); money_moving->home (7-10) |
| Sun 16:05 | Seattle Seahawks @ Las Vegas Raiders | spread | away | -12.5 | 3-1 | -6.5 (-105) | 3 | 3.5 | 6.5 ($20,000) |  |  | 78% / 87% | 11137 | follow_move->away (9-14); money_level->away (16-12); sharp_gap->away (9-18); money_moving->home (7-10) |
| Sun 13:00 | Carolina Panthers @ New Orleans Saints | spread | home | -22.7 | 4-1 | -2.5 (-105) | 1.5 | 4 | -2.5 ($20,000) |  | away 70% | 30% / 31% | 10062 | follow_move->home (9-14); rlm->home (1-8); money_level->away (16-12); sharp_gap->home (9-18); money_moving->home (7-10) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | spread | away | -23.1 | 3-2 | 3.5 (-110) | -4 | 0.5 | -3.5 ($30,000) |  | home 68% | 32% / 34% | 10127 | follow_move->away (9-14); rlm->away (1-8); money_level->home (16-12); sharp_gap->away (9-18); money_moving->home (7-10) |
| Sun 13:00 | Buffalo Bills @ New York Jets | spread | home | -24 | 5-3 | 7.5 (-105) | 8.5 | 1 | 8.5 ($20,000) | -1 | away 92% | 8% / 15% | 11263 | follow_move->home (9-14); rlm->home (1-8); rlm_ratio->home (0-4); money_level->away (16-12); sharp_gap->home (9-18); money_moving->home (7-10); consensus_gap->away (4-3); pin_value->away (10-1) |

