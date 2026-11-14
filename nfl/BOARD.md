# NFL board

Generated 2026-11-14 15:59 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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
| PINNACLE moved vs public | Los Angeles Chargers @ Baltimore Ravens | spread | home | -4.5 | -3.5 | 33% | 2.03 | 4-8 |
| PINNACLE moved vs public | Minnesota Vikings @ Green Bay Packers | moneyline | away | 130 | -221 | 16% | 1.5 | 4-8 |
| PINNACLE moved vs public | Pittsburgh Steelers @ Cincinnati Bengals | moneyline | away | 150 | -190 | 15% | 1.33 | 4-8 |
| PINNACLE moved vs public | San Francisco 49ers @ Dallas Cowboys | moneyline | home | 176 | 182 | 5% | 1.2 | 4-8 |
| PINNACLE moved vs public | Seattle Seahawks @ Las Vegas Raiders | total | under | 40.5 | 43.5 | 24% | 1.29 | 4-8 |
| FanDuel moved vs public | Buffalo Bills @ New York Jets | spread | home | 7.5 | 8.5 | 8% | 1.5 | 3-6 |
| FanDuel moved vs public | Los Angeles Chargers @ Baltimore Ravens | spread | home | -4.5 | -2.5 | 33% | 2.03 | 3-6 |
| FanDuel moved vs public | New England Patriots @ Detroit Lions | spread | home | -2.5 | -1.5 | 39% | 1.33 | 3-6 |
| FanDuel moved vs public | Seattle Seahawks @ Las Vegas Raiders | total | under | 40.5 | 43.5 | 24% | 1.29 | 3-6 |

Ranked by **weighted edge**: each agreeing signal contributes its own
base-rate-corrected edge, and contributes nothing until it has 30 decided
outcomes. Raw agreement count is shown too, but it is the weaker number — a
market can have seven signals agreeing where four of them have losing records.

## A  weighted edge >= +10

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Carolina Panthers @ New Orleans Saints | moneyline | away | +11 | 4-1 | 118 (+118) | -108 | 6.1 | -134 ($10,000) |  |  | 51% / 72% | 17710 | follow_move->home (23-6); money_level->away (24-4); sharp_gap->away (15-12); money_moving->away (8-12); consensus_gap->away (9-20) |

## B  weighted edge +5 to +10

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 16:05 | Seattle Seahawks @ Las Vegas Raiders | total | under | +8.2 | 5-2 | 40.5 (-110) | 43.5 | 3 | 40.5 ($5,000) |  | over 76% | 24% / 31% | 19048 | follow_move->under (5-5); rlm->under (3-3); rlm_ratio->under (3-1); money_level->over (14-14); sharp_gap->under (13-16); money_moving->over (10-10); pin_rlm->under (3-1) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | moneyline | away | +6.4 | 4-1 | -172 (-172) | 100 | 9 | 151 ($10,000) |  |  | 97% / 98% | 18150 | follow_move->away (23-6); money_level->away (24-4); sharp_gap->away (15-12); money_moving->away (8-12); consensus_gap->home (9-20) |
| Sun 16:25 | San Francisco 49ers @ Dallas Cowboys | spread | home | +5.5 | 4-1 | 4.5 (-120) | 4.5 |  | 4 ($30,000) | +0.5 |  | 23% / 35% | 19447 | money_level->away (17-12); sharp_gap->home (10-18); money_moving->home (8-10); consensus_gap->home (4-3); pin_value->home (10-2) |
| Sun 16:25 | San Francisco 49ers @ Dallas Cowboys | moneyline | away | +5.2 | 3-3 | -210 (-210) | -108 | 15.7 | 176 ($20,000) |  |  | 95% / 94% | 19447 | follow_move->away (23-6); money_level->away (24-4); sharp_gap->home (15-12); money_moving->away (8-12); consensus_gap->home (9-20); pin_rlm->home (1-5) |

## C  weighted edge 0 to +5

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Houston Texans @ Cleveland Browns | spread | away | +4.9 | 4-0 | -4.5 (-115) | 3.5 | 1 | 5 ($20,000) | -0.5 |  | 79% / 79% | 15438 | follow_move->away (9-14); money_level->away (17-12); money_moving->away (8-10); pin_value->away (10-2) |
| Sun 09:30 | New England Patriots @ Detroit Lions | moneyline | home | +4.8 | 3-2 | -152 (-152) | -105 | 9.1 | -147 ($20,000) |  |  | 82% / 96% | 22486 | follow_move->home (23-6); money_level->home (24-4); sharp_gap->home (15-12); money_moving->away (8-12); consensus_gap->away (9-20) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | moneyline | home | +4 | 3-2 | -210 (-210) | -110 | 15.4 | -205 ($10,000) |  |  | 84% / 76% | 12879 | follow_move->home (23-6); money_level->home (24-4); sharp_gap->away (15-12); money_moving->home (8-12); consensus_gap->away (9-20) |
| Sun 13:00 | Houston Texans @ Cleveland Browns | total | over | +3.8 | 2-2 | 40.5 (-105) | 39.5 | 1 | 40.5 ($5,000) |  |  | 49% / 48% | 15438 | follow_move->over (5-5); money_level->under (14-14); sharp_gap->under (13-16); money_moving->over (10-10) |
| Sun 13:00 | Buffalo Bills @ New York Jets | moneyline | away | +3.6 | 2-2 | -450 (-450) | -108 | 29.7 | 337 ($10,000) |  |  | 99% / 99% | 18670 | follow_move->away (23-6); money_level->away (24-4); money_moving->home (8-12); consensus_gap->home (9-20) |
| Sun 16:05 | Seattle Seahawks @ Las Vegas Raiders | moneyline | away | +3.6 | 2-2 | -300 (-300) | 100 | 21 | 238 ($10,000) |  |  | 95% / 95% | 19048 | follow_move->away (23-6); money_level->away (24-4); money_moving->home (8-12); consensus_gap->home (9-20) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | spread | home | +2 | 6-0 | -3.5 (-115) | -2.5 | 1 | -4 ($20,000) | +0.5 |  | 60% / 61% | 12879 | follow_move->home (9-14); money_level->home (17-12); sharp_gap->home (10-18); money_moving->home (8-10); consensus_gap->home (4-3); pin_value->home (10-2) |
| Sun 13:00 | Carolina Panthers @ New Orleans Saints | total | over | +2 | 2-2 | 48.5 (-115) | 47.5 | 1 | 48.5 ($5,000) |  |  | 54% / 52% | 17710 | follow_move->over (5-5); money_level->over (14-14); sharp_gap->under (13-16); money_moving->under (10-10) |
| Sun 09:30 | New England Patriots @ Detroit Lions | total | under | +1.9 | 3-0 | 49.5 (-110) | 50.5 | 1 | 49 ($5,000) | +0.5 |  | 89% / 89% | 22486 | follow_move->under (5-5); money_level->under (14-14); pin_value->under (7-5) |
| Sun 13:00 | Houston Texans @ Cleveland Browns | tt_home | under | +1.9 | 1-0 | 17.5 (-125) | 17.5 |  | 16.5 ($2,000) | +1 |  | 0% / 0% | 15438 | pin_value->under (11-9) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | tt_home | over | +1.9 | 1-0 | 14.5 (-104) | 14.5 |  | 19.5 ($2,000) | -5 |  | 0% / 0% | 15585 | pin_value->over (11-9) |
| Sun 09:30 | New England Patriots @ Detroit Lions | tt_away | under | +0.9 | 1-0 | 23.5 (-108) | 24.5 | 1 | 23.5 ($2,000) |  |  | 0% / 0% | 22486 | follow_move->under (6-5) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | tt_away | over | +0.9 | 1-0 | 25.5 (-113) | 24.5 | 1 | 25.5 ($2,000) |  |  | 0% / 0% | 18150 | follow_move->over (6-5) |
| Sun 13:00 | Minnesota Vikings @ Green Bay Packers | tt_away | over | +0.6 | 1-1 | 19.5 (-125) | 17.5 | 2 | 16.5 ($1,000) | +3 |  | 0% / 0% | 18649 | follow_move->over (6-5); pin_value->under (9-9) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | tt_away | under | +0.6 | 1-1 | 16.5 (-102) | 19.5 | 3 | 20.5 ($2,000) | -4 |  | 0% / 0% | 12879 | follow_move->under (6-5); pin_value->over (9-9) |
| Sun 13:00 | Minnesota Vikings @ Green Bay Packers | spread | away | +0.4 | 2-1 | 3 (-110) | -3 |  | -3 ($10,000) |  |  | 37% / 37% | 18649 | money_level->home (17-12); money_moving->away (8-10); consensus_gap->away (4-3) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | tt_away | under | +0.3 | 1-0 | 28.5 (-115) | 28.5 |  | 27.5 ($2,000) | +1 |  | 0% / 0% | 16322 | pin_value->under (9-9) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | tt_away | over | +0.3 | 1-0 | 24.5 (-111) | 24.5 |  | 27.5 ($2,000) | -3 |  | 0% / 0% | 15585 | pin_value->over (9-9) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | tt_away | under | +0.3 | 1-0 | 22.5 (-100) | 22.5 |  | 21.5 ($2,000) | +1 |  | 0% / 0% | 17140 | pin_value->under (9-9) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | tt_home | under | +0.2 | 2-0 | 21.5 (-108) | 22.5 | 1 | 20.5 ($2,000) | +1 |  | 0% / 0% | 7663 | follow_move->under (5-6); pin_value->under (11-9) |

## D  no weighted edge (agreement is all unproven or negative signals)

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | total | under | -0.8 | 5-0 | 38.5 (-115) | 40.5 | 2 | 38 ($5,000) | +0.5 |  | 48% / 53% | 12879 | follow_move->under (5-5); money_level->under (14-14); sharp_gap->under (13-16); money_moving->under (10-10); pin_value->under (7-5) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | total | over | -0.8 | 2-1 | 39.5 (-110) | 40.5 | 1 | 39.5 ($5,000) |  |  | 52% / 52% | 15585 | follow_move->under (5-5); money_level->over (14-14); money_moving->over (10-10) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | total | over | -1 | 4-1 | 47.5 (-105) | 45.5 | 2 | 48 ($5,000) | -0.5 |  | 50% / 55% | 18150 | follow_move->over (5-5); money_level->over (14-14); sharp_gap->over (13-16); money_moving->under (10-10); pin_value->over (7-5) |
| Sun 16:25 | San Francisco 49ers @ Dallas Cowboys | total | over | -1.1 | 3-1 | 55.5 (-115) | 55.5 |  | 56 ($5,000) | -0.5 |  | 72% / 80% | 19447 | money_level->over (14-14); sharp_gap->over (13-16); money_moving->under (10-10); pin_value->over (7-5) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | total | under | -1.9 | 2-1 | 38.5 (-105) | 38.5 |  | 38.5 ($5,000) |  |  | 28% / 31% | 7663 | money_level->over (14-14); sharp_gap->under (13-16); money_moving->under (10-10) |
| Sun 13:00 | Houston Texans @ Cleveland Browns | moneyline | home | -2.4 | 3-2 | 194 (+194) | -108 | 17.9 | 195 ($10,000) |  |  | 8% / 9% | 15438 | follow_move->away (23-6); money_level->away (24-4); sharp_gap->home (15-12); money_moving->home (8-12); consensus_gap->home (9-20) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | moneyline | away | -2.4 | 3-2 | 188 (+188) | -112 | 16.4 | -212 ($10,000) |  |  | 18% / 33% | 7663 | follow_move->home (23-6); money_level->home (24-4); sharp_gap->away (15-12); money_moving->away (8-12); consensus_gap->away (9-20) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | moneyline | home | -2.5 | 4-2 | 490 (+490) | -110 | 35.4 | 429 ($10,000) |  |  | 1% / 2% | 16322 | follow_move->away (23-6); money_level->away (24-4); sharp_gap->home (15-12); money_moving->home (8-12); consensus_gap->home (9-20); pin_value->home (2-5) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | moneyline | home | -2.5 | 4-2 | 400 (+400) | -108 | 31.9 | 353 ($10,000) |  |  | 3% / 5% | 15585 | follow_move->away (23-6); money_level->away (24-4); sharp_gap->home (15-12); money_moving->home (8-12); consensus_gap->home (9-20); pin_value->home (2-5) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | spread | away | -2.8 | 2-2 | -10.5 (-110) | 10 | 0.5 | 10.5 ($20,000) |  |  | 92% / 88% | 16322 | follow_move->away (9-14); money_level->away (17-12); sharp_gap->home (10-18); money_moving->home (8-10) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | spread | away | -2.8 | 2-2 | -3.5 (-100) | 3 | 0.5 | 3.5 ($20,000) |  |  | 87% / 84% | 18150 | follow_move->away (9-14); money_level->away (17-12); sharp_gap->home (10-18); money_moving->home (8-10) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | tt_home | under | -3.6 | 1-1 | 16.5 (-104) | 17.5 | 1 | 17.5 ($2,000) | -1 |  | 0% / 0% | 16322 | follow_move->under (5-6); pin_value->over (11-9) |
| Sun 13:00 | Miami Dolphins @ Indianapolis Colts | tt_home | under | -3.6 | 1-1 | 20.5 (-106) | 21.5 | 1 | 21.5 ($2,000) | -1 |  | 0% / 0% | 12879 | follow_move->under (5-6); pin_value->over (11-9) |
| Sun 13:00 | Carolina Panthers @ New Orleans Saints | tt_home | over | -3.6 | 1-1 | 25.5 (-113) | 24.5 | 1 | 23.5 ($2,000) | +2 |  | 0% / 0% | 17710 | follow_move->over (5-6); pin_value->under (11-9) |
| Sun 13:00 | Kansas City Chiefs @ Atlanta Falcons | tt_home | over | -3.6 | 1-1 | 22.5 (-113) | 20.5 | 2 | 20.5 ($2,000) | +2 |  | 0% / 0% | 18150 | follow_move->over (5-6); pin_value->under (11-9) |
| Sun 16:05 | Seattle Seahawks @ Las Vegas Raiders | tt_home | under | -3.6 | 1-1 | 16.5 (-104) | 19.5 | 3 | 20.5 ($2,000) | -4 |  | 0% / 0% | 19048 | follow_move->under (5-6); pin_value->over (11-9) |
| Sun 13:00 | Jacksonville Jaguars @ Tennessee Titans | total | over | -3.7 | 2-1 | 46.5 (-100) | 46.5 |  | 46.5 ($5,000) |  |  | 52% / 60% | 16322 | money_level->over (14-14); sharp_gap->over (13-16); money_moving->under (10-10) |
| Sun 13:00 | Carolina Panthers @ New Orleans Saints | spread | home | -3.8 | 5-2 | -1.5 (-120) | 1.5 | 3 | -2.5 ($20,000) | +1 | away 67% | 33% / 25% | 17710 | follow_move->home (9-14); rlm->home (1-8); money_level->away (17-12); sharp_gap->away (10-18); money_moving->home (8-10); consensus_gap->home (4-3); pin_value->home (10-2) |
| Sun 13:00 | Minnesota Vikings @ Green Bay Packers | moneyline | away | -5.2 | 4-2 | 130 (+130) | -108 | 8.7 | -152 ($6,000) |  |  | 16% / 24% | 18649 | follow_move->home (23-6); money_level->home (24-4); sharp_gap->away (15-12); money_moving->away (8-12); consensus_gap->away (9-20); pin_rlm->away (1-5) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | moneyline | away | -5.2 | 4-2 | 150 (+150) | -108 | 12.1 | -180 ($20,000) |  |  | 15% / 20% | 17140 | follow_move->home (23-6); money_level->home (24-4); sharp_gap->away (15-12); money_moving->away (8-12); consensus_gap->away (9-20); pin_rlm->away (1-5) |
| Sun 13:00 | Minnesota Vikings @ Green Bay Packers | total | over | -6 | 4-1 | 42.5 (-105) | 40.5 | 2 | 42 ($3,000) | +0.5 |  | 54% / 67% | 18649 | follow_move->over (5-5); money_level->over (14-14); sharp_gap->over (13-16); money_moving->over (10-10); pin_value->under (7-5) |
| Sun 13:00 | Buffalo Bills @ New York Jets | total | under | -6.1 | 3-1 | 50.5 (-105) | 50.5 |  | 51 ($5,000) | -0.5 |  | 54% / 57% | 18670 | money_level->under (14-14); sharp_gap->under (13-16); money_moving->under (10-10); pin_value->over (7-5) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | total | over | -6.2 | 3-2 | 49.5 (-105) | 48.5 | 1 | 48.5 ($5,000) | +1 |  | 64% / 69% | 17140 | follow_move->over (5-5); money_level->over (14-14); sharp_gap->over (13-16); money_moving->under (10-10); pin_value->under (7-5) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | spread | home | -8.6 | 7-0 | -4.5 (-110) | -2.5 | 2 | -4.5 ($20,000) |  | away 67% | 33% / 67% | 7663 | follow_move->home (9-14); rlm->home (1-8); rlm_ratio->home (0-4); money_level->home (17-12); sharp_gap->home (10-18); money_moving->home (8-10); pin_rlm->home (0-2) |
| Sun 09:30 | New England Patriots @ Detroit Lions | spread | home | -10.2 | 5-1 | -2.5 (-120) | -1.5 | 1 | -2.5 ($30,000) |  | away 61% | 39% / 52% | 22486 | follow_move->home (9-14); rlm->home (1-8); rlm_ratio->home (0-4); money_level->home (17-12); sharp_gap->home (10-18); money_moving->away (8-10) |
| Sun 16:05 | Los Angeles Rams @ Arizona Cardinals | spread | away | -10.8 | 3-1 | -9.5 (-110) | 8.5 | 1 | 9.5 ($20,000) |  |  | 78% / 80% | 15585 | follow_move->away (9-14); money_level->away (17-12); sharp_gap->away (10-18); money_moving->home (8-10) |
| Sun 16:05 | Seattle Seahawks @ Las Vegas Raiders | spread | away | -10.8 | 3-1 | -6.5 (-110) | 3 | 3.5 | 6.5 ($20,000) |  |  | 81% / 85% | 19048 | follow_move->away (9-14); money_level->away (17-12); sharp_gap->away (10-18); money_moving->home (8-10) |
| Sun 13:00 | Buffalo Bills @ New York Jets | spread | home | -20.7 | 5-2 | 7.5 (-110) | 8.5 | 1 | 8.5 ($20,000) | -1 | away 92% | 8% / 12% | 18670 | follow_move->home (9-14); rlm->home (1-8); rlm_ratio->home (0-4); money_level->away (17-12); sharp_gap->home (10-18); money_moving->home (8-10); pin_value->away (10-2) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | spread | away | -22 | 4-1 | 3.5 (-110) | -4 | 0.5 | -3.5 ($30,000) |  | home 66% | 34% / 39% | 17140 | follow_move->away (9-14); rlm->away (1-8); money_level->home (17-12); sharp_gap->away (10-18); money_moving->away (8-10) |

