# NFL board

Generated 2026-11-27 03:45 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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

`retraced` is how far Pinnacle's number has already come BACK against the move
in the `moved` column. `moved` compares first-seen with current, so a number
that went 136.5 -> 131 -> 135 prints as a drop while it is actually climbing.
A large `retraced` means the move is finished and reversing, and you would be
buying the wrong end of it. This is shown, not gated -- it is not a signal.

| tier | game | market | side | book | moved | retraced | FD now | tickets | money/tix | record |
|---|---|---|---|---|---|---|---|---|---|---|
| PINNACLE moved vs public | Seattle Seahawks @ San Francisco 49ers | moneyline | away | Pinnacle | 153 -> 128 | **+1.2** | 124 | 10% | 1.7 | 5-10 fit · 0-4 fwd |
| PINNACLE moved vs public | Tennessee Titans @ Jacksonville Jaguars | moneyline | away | Pinnacle | 729 -> 723 | — | 730 | 2% | 2.5 | 5-10 fit · 0-4 fwd |
| FanDuel moved vs public | Las Vegas Raiders @ Cleveland Browns | moneyline | away | FanDuel | 198 -> 190 | — | 190 | 22% | 1.82 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | New Orleans Saints @ Cincinnati Bengals | moneyline | away | FanDuel | 430 -> 420 | — | 420 | 2% | 1.5 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Seattle Seahawks @ San Francisco 49ers | moneyline | away | FanDuel | 144 -> 124 | **+1.2** | 124 | 10% | 1.7 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Tennessee Titans @ Jacksonville Jaguars | moneyline | away | FanDuel | 750 -> 730 | — | 730 | 2% | 2.5 | 6-14 fit · 0-2 fwd |
| line moved off the public (no ratio test) | Atlanta Falcons @ Minnesota Vikings | total | under | FanDuel | 42.5 -> 41.5 | — | 41.5 | 34% | 0.88 | 9-32 fit · 9-5 fwd |
| line moved off the public (no ratio test) | Baltimore Ravens @ Houston Texans | moneyline | away | FanDuel | 265 -> 240 | **+0.7** | 240 | 6% | 1.0 | 9-32 fit · 9-5 fwd |
| line moved off the public (no ratio test) | Carolina Panthers @ Tampa Bay Buccaneers | spread | home | FanDuel | -2.5 -> -3 | — | -3 | 40% | 1.1 | 9-32 fit · 9-5 fwd |
| line moved off the public (no ratio test) | Denver Broncos @ Pittsburgh Steelers | total | under | FanDuel | 37.5 -> 36.5 | **+0.5** | 36.5 | 26% | 1.0 | 9-32 fit · 9-5 fwd |
| line moved off the public (no ratio test) | Las Vegas Raiders @ Cleveland Browns | total | under | FanDuel | 41.5 -> 39.5 | **+1** | 39.5 | 24% | 1.12 | 9-32 fit · 9-5 fwd |
| line moved off the public (no ratio test) | New Orleans Saints @ Cincinnati Bengals | spread | away | FanDuel | 10 -> 9.5 | — | 9.5 | 9% | 0.89 | 9-32 fit · 9-5 fwd |
| line moved off the public (no ratio test) | New York Giants @ Indianapolis Colts | spread | home | FanDuel | 7 -> 6.5 | — | 6.5 | 19% | 0.79 | 9-32 fit · 9-5 fwd |
| line moved off the public (no ratio test) | New York Giants @ Indianapolis Colts | moneyline | home | FanDuel | 265 -> 240 | — | 240 | 5% | 0.8 | 9-32 fit · 9-5 fwd |
| line moved off the public (no ratio test) | New York Jets @ Miami Dolphins | total | under | FanDuel | 41.5 -> 40.5 | — | 40.5 | 30% | 0.87 | 9-32 fit · 9-5 fwd |
| line moved off the public (no ratio test) | Seattle Seahawks @ San Francisco 49ers | total | under | FanDuel | 46.5 -> 44.5 | — | 44.5 | 22% | 1.09 | 9-32 fit · 9-5 fwd |
| line moved off the public (no ratio test) | Washington Commanders @ Arizona Cardinals | moneyline | home | FanDuel | 300 -> 280 | — | 280 | 3% | 1.0 | 9-32 fit · 9-5 fwd |

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
before 2026-11-21, so a good number there proves nothing) and `fwd` (games
since, which it had no hand in choosing). A `*` means the weight came from the
forward record, which happens once that record reaches 30 decided
outcomes. No asterisk means the lean rests on fitted numbers only.

## A  weighted ROI >= +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | spread | home **SPLIT** | +54.7 | 6-3 | -9.5 (-120) | -10 | 0.5 | -10.5 ($20,000) | +1 | home 91% | 91% / 92% | 7795 | follow_move->away (16-21 fit · 6-8 fwd); rlm->away (1-11 fit · 3-2 fwd); rlm_quiet->away (1-9 fit · 3-2 fwd); money_level->home (25-17 fit · 3-11 fwd); sharp_gap->home (17-25 fit · 7-8 fwd); money_moving->home (10-21 fit · 6-9 fwd); consensus_gap->home (5-3 fit · 0-2 fwd); pin_value->home (16-3 fit · 2-4 fwd); pin_move->home (8-10 fit · 3-6 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | moneyline | away **SPLIT** | +28.2 | 4-2 | -255 (-255) | -205 | 4.5 | -236 ($10,000) |  |  | 88% / 89% | 5568 | follow_move->away (17-18 fit · 5-7 fwd); money_level->away (35-7 fit · 9-6 fwd); sharp_gap->away (21-19 fit · 3-11 fwd); money_moving->home (14-19 fit · 7-7 fwd); consensus_gap->home (13-30 fit · 5-10 fwd); pin_move->away (15-11 fit · 4-7 fwd) |

## B  weighted ROI +10% to +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | spread | home | +13 | 2-1 | -14.5 (-105) | -14 | 0.5 | -14.5 ($20,000) |  |  | 90% / 89% | 8315 | follow_move->home (16-21 fit · 6-8 fwd); money_level->home (25-17 fit · 3-11 fwd); sharp_gap->away (17-25 fit · 7-8 fwd) |

## C  weighted ROI 0 to +10%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | moneyline | away **SPLIT** | +8.4 | 4-2 | -235 (-235) | -142 | 11.4 | -216 ($30,000) **retraced +1.3** |  |  | 91% / 89% | 31130 | follow_move->away (17-18 fit · 5-7 fwd); money_level->away (35-7 fit · 9-6 fwd); sharp_gap->home (21-19 fit · 3-11 fwd); money_moving->away (14-19 fit · 7-7 fwd); consensus_gap->home (13-30 fit · 5-10 fwd); pin_move->away (15-11 fit · 4-7 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | total | under **SPLIT** | +0.6 | 3-3 | 41.5 (-110) | 42.5 | 1 | 41.5 ($5,000) |  | over 66% | 34% / 30% | 9875 | follow_move->under (10-9 fit · 10-2 fwd); rlm->under (4-5 fit · 5-1 fwd); rlm_quiet->under (3-4 fit · 5-1 fwd); money_level->over (23-19 fit · 7-8 fwd); sharp_gap->over (21-22 fit · 6-7 fwd); money_moving->over (15-18 fit · 8-6 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | total | over | +4.9 | 5-1 | 49.5 (-110) | 47.5 | 2 | 50 ($5,000) | -0.5 |  | 74% / 81% | 8315 | follow_move->over (10-9 fit · 10-2 fwd); money_level->over (23-19 fit · 7-8 fwd); sharp_gap->over (21-22 fit · 6-7 fwd); money_moving->under (15-18 fit · 8-6 fwd); pin_value->over (12-11 fit · 5-2 fwd); pin_move->over (14-13 fit · 13-2 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | tt_away | over | +2.3 | 1-0 | 20.5 (-111) | 19.5 | 1 | 20.5 ($2,000) |  |  | 0% / 0% | 31130 | follow_move->over (9-7 fit · 5-1 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | tt_away | under | +2.3 | 1-0 | 16.5 (-100) | 17.5 | 1 | 16.5 ($2,000) |  |  | 0% / 0% | 9875 | follow_move->under (9-7 fit · 5-1 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | tt_away | under | +2 | 1-1 | 22.5 (-100) | 23.5 | 1 | 23.5 ($2,000) | +1 |  | 0% / 0% | 5568 | follow_move->under (9-7 fit · 5-1 fwd); pin_value->over (14-12 fit · 2-7 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | tt_away | over | +2 | 1-1 | 20.5 (-102) | 19.5 | 1 | 19.5 ($2,000) | +1 |  | 0% / 0% | 8693 | follow_move->over (9-7 fit · 5-1 fwd); pin_value->under (14-12 fit · 2-7 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | tt_away | under | +2 | 1-1 | 23.5 (-100) | 24.5 | 1 | 24.5 ($2,000) | +1 |  | 0% / 0% | 8820 | follow_move->under (9-7 fit · 5-1 fwd); pin_value->over (14-12 fit · 2-7 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | tt_away | over | +2 | 1-1 | 17.5 (+102) | 16.5 | 1 | 15.5 ($2,000) | +2 |  | 0% / 0% | 8315 | follow_move->over (9-7 fit · 5-1 fwd); pin_value->under (14-12 fit · 2-7 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | tt_away | under | +2 | 1-1 | 20.5 (-113) | 21.5 | 1 | 21.5 ($2,000) | +1 |  | 0% / 0% | 11405 | follow_move->under (9-7 fit · 5-1 fwd); pin_value->over (14-12 fit · 2-7 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | total | over | +0.5 | 3-1 | 41.5 (-110) | 41.5 |  | 41.5 ($5,000) |  |  | 72% / 74% | 7542 | money_delta->under (4-7 fit · 2-3 fwd); money_level->over (23-19 fit · 7-8 fwd); sharp_gap->over (21-22 fit · 6-7 fwd); money_moving->over (15-18 fit · 8-6 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | tt_away | over | +0.3 | 1-0 | 19.5 (-115) | 19.5 |  | 20.5 ($2,000) | -1 |  | 0% / 0% | 7795 | pin_value->over (14-12 fit · 2-7 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | total | over | +0.2 | 5-1 | 47.5 (-105) | 46.5 | 1 | 47.5 ($5,000) |  |  | 62% / 68% | 8693 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->over (10-9 fit · 10-2 fwd); money_level->over (23-19 fit · 7-8 fwd); sharp_gap->over (21-22 fit · 6-7 fwd); money_moving->over (15-18 fit · 8-6 fwd); pin_move->over (14-13 fit · 13-2 fwd) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | total | under **SPLIT** | -4.4 | 4-2 | 36.5 (-106) | 37.5 | 1 | 36.5 ($10,000) |  | over 74% | 26% / 26% | 31130 | follow_move->under (10-9 fit · 10-2 fwd); rlm->under (4-5 fit · 5-1 fwd); rlm_quiet->under (3-4 fit · 5-1 fwd); money_level->over (23-19 fit · 7-8 fwd); money_moving->over (15-18 fit · 8-6 fwd); pin_move->under (14-13 fit · 13-2 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | spread | away **SPLIT** | -5.7 | 3-2 | 7 (-115) | 7 |  | 7 ($20,000) |  |  | 20% / 18% | 9875 | money_delta->away (3-14 fit · 1-0 fwd); money_level->home (25-17 fit · 3-11 fwd); sharp_gap->home (17-25 fit · 7-8 fwd); consensus_gap->away (5-3 fit · 0-2 fwd); book_lag->away (4-0 fit · 0-0 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | total | under **SPLIT** | -7.1 | 4-3 | 39.5 (-104) | 41.5 | 2 | 40.5 ($5,000) **retraced +1** | +1 | over 76% | 24% / 27% | 8113 | follow_move->under (10-9 fit · 10-2 fwd); rlm->under (4-5 fit · 5-1 fwd); rlm_quiet->under (3-4 fit · 5-1 fwd); money_level->over (23-19 fit · 7-8 fwd); sharp_gap->under (21-22 fit · 6-7 fwd); money_moving->over (15-18 fit · 8-6 fwd); pin_value->over (12-11 fit · 5-2 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | total | under **SPLIT** | -10.3 | 6-3 | 40.5 (-120) | 41.5 | 1 | 40 ($5,000) | -0.5 | over 70% | 30% / 26% | 5568 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->under (10-9 fit · 10-2 fwd); rlm->under (4-5 fit · 5-1 fwd); rlm_quiet->under (3-4 fit · 5-1 fwd); money_level->over (23-19 fit · 7-8 fwd); sharp_gap->over (21-22 fit · 6-7 fwd); money_moving->over (15-18 fit · 8-6 fwd); pin_value->under (12-11 fit · 5-2 fwd); pin_move->under (14-13 fit · 13-2 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | total | under **SPLIT** | -10.4 | 3-2 | 42.5 (-120) | 42.5 |  | 42 ($5,000) | -0.5 |  | 25% / 28% | 8820 | money_delta->under (4-7 fit · 2-3 fwd); money_level->over (23-19 fit · 7-8 fwd); sharp_gap->under (21-22 fit · 6-7 fwd); money_moving->over (15-18 fit · 8-6 fwd); pin_value->under (12-11 fit · 5-2 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | moneyline | home **SPLIT** | -18.5 | 4-4 | 102 (+102) | -112 | 3.3 | 117 ($3,000) |  |  | 31% / 45% | 7098 | money_delta->home (4-5 fit · 1-2 fwd); follow_move->away (17-18 fit · 5-7 fwd); money_level->away (35-7 fit · 9-6 fwd); sharp_gap->home (21-19 fit · 3-11 fwd); money_moving->home (14-19 fit · 7-7 fwd); consensus_gap->home (13-30 fit · 5-10 fwd); pin_value->away (2-7 fit · 2-4 fwd); pin_move->away (15-11 fit · 4-7 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | total | under **SPLIT** | -21.1 | 6-2 | 49.5 (-110) | 50.5 | 1 | 49 ($5,000) | -0.5 |  | 43% / 40% | 7795 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->under (10-9 fit · 10-2 fwd); rlm_quiet->under (3-4 fit · 5-1 fwd); money_level->over (23-19 fit · 7-8 fwd); sharp_gap->over (21-22 fit · 6-7 fwd); money_moving->under (15-18 fit · 8-6 fwd); pin_value->under (12-11 fit · 5-2 fwd); pin_move->under (14-13 fit · 13-2 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | spread | home **SPLIT** | -21.8 | 4-2 | 5.5 (-110) | 4 | 1.5 | 5 ($20,000) | +0.5 |  | 49% / 50% | 5568 | money_delta->home (3-14 fit · 1-0 fwd); follow_move->away (16-21 fit · 6-8 fwd); sharp_gap->home (17-25 fit · 7-8 fwd); money_moving->home (10-21 fit · 6-9 fwd); pin_value->home (16-3 fit · 2-4 fwd); pin_move->away (8-10 fit · 3-6 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | spread | home **SPLIT** | -32.8 | 3-3 | 6.5 (-115) | 7 | 0.5 | 6.5 ($30,000) |  | away 81% | 19% / 15% | 8820 | follow_move->home (16-21 fit · 6-8 fwd); rlm->home (1-11 fit · 3-2 fwd); rlm_quiet->home (1-9 fit · 3-2 fwd); money_level->away (25-17 fit · 3-11 fwd); sharp_gap->away (17-25 fit · 7-8 fwd); money_moving->away (10-21 fit · 6-9 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | moneyline | away **SPLIT** | -35 | 4-3 | 136 (+136) | 126 | 2.2 | 142 ($20,000) |  |  | 33% / 43% | 7174 | money_delta->away (4-5 fit · 1-2 fwd); follow_move->home (17-18 fit · 5-7 fwd); money_level->home (35-7 fit · 9-6 fwd); sharp_gap->away (21-19 fit · 3-11 fwd); money_moving->away (14-19 fit · 7-7 fwd); consensus_gap->away (13-30 fit · 5-10 fwd); pin_move->home (15-11 fit · 4-7 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | moneyline | away **SPLIT** | -40.9 | 3-2 | 265 (+265) | 260 | 1.1 | 265 ($10,000) |  |  | 2% / 3% | 9875 | follow_move->home (17-18 fit · 5-7 fwd); money_level->home (35-7 fit · 9-6 fwd); sharp_gap->away (21-19 fit · 3-11 fwd); money_moving->away (14-19 fit · 7-7 fwd); consensus_gap->away (13-30 fit · 5-10 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | spread | away **SPLIT** | -41 | 3-2 | 2.5 (-100) | 2 | 0.5 | 2.5 ($5,000) |  |  | 30% / 32% | 11405 | follow_move->home (16-21 fit · 6-8 fwd); money_level->home (25-17 fit · 3-11 fwd); sharp_gap->away (17-25 fit · 7-8 fwd); money_moving->away (10-21 fit · 6-9 fwd); pin_move->away (8-10 fit · 3-6 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | moneyline | home **SPLIT** | -83.3 | 5-3 | 240 (+240) | 265 | 2 | 232 ($10,000) |  | away 95% | 5% / 4% | 8820 | follow_move->home (17-18 fit · 5-7 fwd); rlm->home (4-16 fit · 1-2 fwd); rlm_quiet->home (2-15 fit · 1-2 fwd); money_level->away (35-7 fit · 9-6 fwd); sharp_gap->away (21-19 fit · 3-11 fwd); money_moving->away (14-19 fit · 7-7 fwd); consensus_gap->home (13-30 fit · 5-10 fwd); pin_move->home (15-11 fit · 4-7 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | moneyline | away **SPLIT** | -83.5 | 4-2 | 240 (+240) | 265 | 2.1 | 251 ($10,000) |  | home 94% | 6% / 6% | 8693 | follow_move->away (17-18 fit · 5-7 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 9-6 fwd); money_moving->home (14-19 fit · 7-7 fwd); consensus_gap->away (13-30 fit · 5-10 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | moneyline | away **SPLIT** | -96 | 6-2 | 420 (+420) | 430 | 0.7 | 434 ($10,000) |  | home 98% | 2% / 3% | 7795 | follow_move->away (17-18 fit · 5-7 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 9-6 fwd); sharp_gap->away (21-19 fit · 3-11 fwd); money_moving->home (14-19 fit · 7-7 fwd); consensus_gap->away (13-30 fit · 5-10 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | moneyline | away **SPLIT** | -96 | 6-2 | 190 (+190) | 198 | 0.9 | 200 ($10,000) |  | home 78% | 22% / 40% | 8113 | follow_move->away (17-18 fit · 5-7 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 9-6 fwd); sharp_gap->away (21-19 fit · 3-11 fwd); money_moving->home (14-19 fit · 7-7 fwd); consensus_gap->away (13-30 fit · 5-10 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | moneyline | home **SPLIT** | -104.1 | 6-2 | 280 (+280) | 300 | 1.3 | 266 ($10,000) |  | away 97% | 3% / 3% | 7542 | follow_move->home (17-18 fit · 5-7 fwd); rlm->home (4-16 fit · 1-2 fwd); rlm_quiet->home (2-15 fit · 1-2 fwd); money_level->away (35-7 fit · 9-6 fwd); money_moving->away (14-19 fit · 7-7 fwd); consensus_gap->home (13-30 fit · 5-10 fwd); pin_value->home (2-7 fit · 2-4 fwd); pin_move->home (15-11 fit · 4-7 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | spread | home **SPLIT** | -142.3 | 7-2 | -3 (-104) | -2.5 | 0.5 | -3 ($30,000) |  | away 60% | 40% / 44% | 7174 | money_delta->home (3-14 fit · 1-0 fwd); follow_move->home (16-21 fit · 6-8 fwd); rlm->home (1-11 fit · 3-2 fwd); rlm_quiet->home (1-9 fit · 3-2 fwd); money_level->away (25-17 fit · 3-11 fwd); sharp_gap->home (17-25 fit · 7-8 fwd); money_moving->home (10-21 fit · 6-9 fwd); consensus_gap->away (5-3 fit · 0-2 fwd); pin_move->home (8-10 fit · 3-6 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | tt_home | under | -1.2 | 2-0 | 16.5 (-128) | 17.5 | 1 | 16.5 ($2,000) |  |  | 0% / 0% | 31130 | follow_move->under (9-10 fit · 4-3 fwd); pin_move->under (1-0 fit · 0-0 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | total | over | -4.3 | 2-0 | 43.5 (-115) | 43.5 |  | 43.5 ($10,000) |  |  | 81% / 81% | 7174 | money_level->over (23-19 fit · 7-8 fwd); money_moving->over (15-18 fit · 8-6 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | tt_home | over | -4.6 | 1-0 | 27.5 (-100) | 26.5 | 1 | 27.5 ($2,000) |  |  | 0% / 0% | 8693 | follow_move->over (9-10 fit · 4-3 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | tt_home | over | -4.6 | 1-0 | 31.5 (-108) | 30.5 | 1 | 31.5 ($2,000) |  |  | 0% / 0% | 8315 | follow_move->over (9-10 fit · 4-3 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | tt_home | over | -4.6 | 1-0 | 23.5 (-108) | 22.5 | 1 | 23.5 ($2,000) |  |  | 0% / 0% | 7174 | follow_move->over (9-10 fit · 4-3 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | tt_home | under | -9.2 | 1-1 | 16.5 (+102) | 18.5 | 2 | 17.5 ($2,000) | +1 |  | 0% / 0% | 5568 | follow_move->under (9-10 fit · 4-3 fwd); pin_value->over (17-12 fit · 3-5 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | tt_home | over | -9.2 | 1-1 | 17.5 (+102) | 16.5 | 1 | 16.5 ($2,000) | +1 |  | 0% / 0% | 8820 | follow_move->over (9-10 fit · 4-3 fwd); pin_value->under (17-12 fit · 3-5 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | tt_home | under | -9.2 | 1-1 | 23.5 (-122) | 24.5 | 1 | 24.5 ($2,000) | +1 |  | 0% / 0% | 11405 | follow_move->under (9-10 fit · 4-3 fwd); pin_value->over (17-12 fit · 3-5 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | tt_home | under | -9.2 | 1-1 | 22.5 (-102) | 23.5 | 1 | 23.5 ($2,000) | +1 |  | 0% / 0% | 8113 | follow_move->under (9-10 fit · 4-3 fwd); pin_value->over (17-12 fit · 3-5 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | spread | away | -15 | 4-1 | -1.5 (-110) | 3.5 | 5 | -1.5 ($5,000) |  |  | 61% / 60% | 7098 | follow_move->away (16-21 fit · 6-8 fwd); money_level->away (25-17 fit · 3-11 fwd); sharp_gap->home (17-25 fit · 7-8 fwd); money_moving->away (10-21 fit · 6-9 fwd); pin_move->away (8-10 fit · 3-6 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | total | under | -15.1 | 2-1 | 35.5 (-108) | 35.5 |  | 35.5 ($3,000) |  |  | 15% / 16% | 7098 | money_level->over (23-19 fit · 7-8 fwd); sharp_gap->under (21-22 fit · 6-7 fwd); money_moving->under (15-18 fit · 8-6 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | spread | home | -22.9 | 5-1 | 7 (-115) | 7 |  | 6.5 ($20,000) | +0.5 |  | 16% / 17% | 7542 | money_level->away (25-17 fit · 3-11 fwd); sharp_gap->home (17-25 fit · 7-8 fwd); money_moving->home (10-21 fit · 6-9 fwd); consensus_gap->home (5-3 fit · 0-2 fwd); pin_value->home (16-3 fit · 2-4 fwd); pin_move->home (8-10 fit · 3-6 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | spread | away | -23 | 4-0 | -4.5 (-110) | -1.5 | 3 | -4.5 ($50,000) |  |  | 83% / 89% | 31130 | follow_move->away (16-21 fit · 6-8 fwd); money_level->away (25-17 fit · 3-11 fwd); sharp_gap->away (17-25 fit · 7-8 fwd); pin_move->away (8-10 fit · 3-6 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | spread | home | -28 | 3-0 | -6.5 (-110) | -6.5 |  | -6.5 ($20,000) |  |  | 60% / 61% | 8693 | money_level->home (25-17 fit · 3-11 fwd); sharp_gap->home (17-25 fit · 7-8 fwd); money_moving->home (10-21 fit · 6-9 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | total | under | -34.1 | 8-1 | 44.5 (-120) | 46.5 | 2 | 44 ($3,000) | -0.5 | over 78% | 22% / 24% | 11405 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->under (10-9 fit · 10-2 fwd); rlm->under (4-5 fit · 5-1 fwd); rlm_quiet->under (3-4 fit · 5-1 fwd); money_level->over (23-19 fit · 7-8 fwd); sharp_gap->under (21-22 fit · 6-7 fwd); money_moving->under (15-18 fit · 8-6 fwd); pin_value->under (12-11 fit · 5-2 fwd); pin_move->under (14-13 fit · 13-2 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | spread | away | -38.2 | 4-0 | 4.5 (-105) | 5 | 0.5 | 4.5 ($20,000) |  |  | 68% / 69% | 8113 | follow_move->away (16-21 fit · 6-8 fwd); money_level->away (25-17 fit · 3-11 fwd); sharp_gap->away (17-25 fit · 7-8 fwd); money_moving->away (10-21 fit · 6-9 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | moneyline | away | -77.1 | 8-1 | 730 (+730) | 750 | 0.3 | 723 ($10,000) |  | home 98% | 2% / 5% | 8315 | follow_move->away (17-18 fit · 5-7 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 9-6 fwd); sharp_gap->away (21-19 fit · 3-11 fwd); money_moving->away (14-19 fit · 7-7 fwd); consensus_gap->away (13-30 fit · 5-10 fwd); pin_rlm->away (2-7 fit · 0-3 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | moneyline | away | -79.4 | 10-1 | 124 (+124) | 144 | 3.9 | 128 ($3,000) **retraced +1.2** |  | home 90% | 10% / 17% | 11405 | money_delta->away (4-5 fit · 1-2 fwd); follow_move->away (17-18 fit · 5-7 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 9-6 fwd); sharp_gap->away (21-19 fit · 3-11 fwd); money_moving->away (14-19 fit · 7-7 fwd); consensus_gap->away (13-30 fit · 5-10 fwd); pin_move->away (15-11 fit · 4-7 fwd); pin_rlm->away (2-7 fit · 0-3 fwd) |

