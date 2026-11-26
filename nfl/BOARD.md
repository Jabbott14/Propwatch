# NFL board

Generated 2026-11-26 11:35 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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
| PINNACLE moved vs public | Baltimore Ravens @ Houston Texans | moneyline | away | Pinnacle | 253 -> 251 | **+0.7** | 240 | 5% | 1.2 | 5-10 fit · 0-4 fwd |
| PINNACLE moved vs public | Denver Broncos @ Pittsburgh Steelers | total | under | Pinnacle | 38 -> 36.5 | **+0.5** | 36.5 | 23% | 1.52 | 5-10 fit · 0-4 fwd |
| PINNACLE moved vs public | Seattle Seahawks @ San Francisco 49ers | moneyline | away | Pinnacle | 153 -> 122 | — | 122 | 10% | 2.0 | 5-10 fit · 0-4 fwd |
| PINNACLE moved vs public | Tennessee Titans @ Jacksonville Jaguars | moneyline | away | Pinnacle | 729 -> 727 | — | 750 | 2% | 2.5 | 5-10 fit · 0-4 fwd |
| FanDuel moved vs public | Baltimore Ravens @ Houston Texans | moneyline | away | FanDuel | 265 -> 240 | **+0.7** | 240 | 5% | 1.2 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Denver Broncos @ Pittsburgh Steelers | total | under | FanDuel | 37.5 -> 36.5 | **+0.5** | 36.5 | 23% | 1.52 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Kansas City Chiefs @ Buffalo Bills | moneyline | away | FanDuel | 132 -> 128 | — | 128 | 28% | 1.5 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Las Vegas Raiders @ Cleveland Browns | total | under | FanDuel | 41.5 -> 39.5 | **+1** | 39.5 | 25% | 1.2 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Las Vegas Raiders @ Cleveland Browns | moneyline | away | FanDuel | 198 -> 190 | — | 190 | 23% | 1.78 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | New Orleans Saints @ Cincinnati Bengals | moneyline | away | FanDuel | 430 -> 420 | — | 420 | 2% | 1.5 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Seattle Seahawks @ San Francisco 49ers | moneyline | away | FanDuel | 144 -> 122 | — | 122 | 10% | 2.0 | 6-14 fit · 0-2 fwd |
| line moved off the public (no ratio test) | Atlanta Falcons @ Minnesota Vikings | total | under | FanDuel | 42.5 -> 41.5 | — | 41.5 | 31% | 1.03 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New Orleans Saints @ Cincinnati Bengals | spread | away | FanDuel | 10 -> 9.5 | — | 9.5 | 10% | 0.9 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New York Giants @ Indianapolis Colts | spread | home | FanDuel | 7 -> 6.5 | — | 6.5 | 22% | 0.91 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New York Giants @ Indianapolis Colts | moneyline | home | FanDuel | 265 -> 240 | — | 240 | 5% | 1.0 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New York Jets @ Miami Dolphins | total | under | FanDuel | 41.5 -> 40.5 | — | 40.5 | 25% | 1.08 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | Seattle Seahawks @ San Francisco 49ers | total | under | FanDuel | 46.5 -> 44.5 | — | 44.5 | 17% | 1.18 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | Washington Commanders @ Arizona Cardinals | moneyline | home | FanDuel | 300 -> 280 | — | 280 | 3% | 1.0 | 9-32 fit · 8-5 fwd |

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
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | spread | home **SPLIT** | +54.7 | 6-3 | -9.5 (-120) | -10 | 0.5 | -10.5 ($20,000) | +1 | home 90% | 90% / 91% | 5639 | follow_move->away (16-21 fit · 5-7 fwd); rlm->away (1-11 fit · 3-2 fwd); rlm_quiet->away (1-9 fit · 3-2 fwd); money_level->home (25-17 fit · 3-9 fwd); sharp_gap->home (17-25 fit · 7-6 fwd); money_moving->home (10-21 fit · 5-8 fwd); consensus_gap->home (5-3 fit · 0-2 fwd); pin_value->home (16-3 fit · 2-3 fwd); pin_move->home (8-10 fit · 3-5 fwd) |
| Thu 16:30 | Philadelphia Eagles @ Dallas Cowboys | moneyline | home **SPLIT** | +48.8 | 3-3 | -480 (-480) | -460 | 0.6 | -434 ($30,000) |  |  | 85% / 86% | 36941 | follow_move->home (17-18 fit · 5-5 fwd); money_level->home (35-7 fit · 9-4 fwd); sharp_gap->home (21-19 fit · 3-10 fwd); money_moving->away (14-19 fit · 6-6 fwd); consensus_gap->away (13-30 fit · 4-9 fwd); pin_value->away (2-7 fit · 1-3 fwd) |
| Thu 13:00 | Chicago Bears @ Detroit Lions | spread | home **SPLIT** | +43.9 | 4-2 | 1.5 (-105) | -2.5 | 4 | 1 ($50,000) | +0.5 |  | 46% / 54% | 59408 | follow_move->away (16-21 fit · 5-7 fwd); money_level->home (25-17 fit · 3-9 fwd); sharp_gap->home (17-25 fit · 7-6 fwd); money_moving->away (10-21 fit · 5-8 fwd); pin_value->home (16-3 fit · 2-3 fwd); pin_move->home (8-10 fit · 3-5 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | moneyline | away **SPLIT** | +28.2 | 4-2 | -230 (-230) | -205 | 2.3 | -236 ($10,000) |  |  | 88% / 90% | 4351 | follow_move->away (17-18 fit · 5-5 fwd); money_level->away (35-7 fit · 9-4 fwd); sharp_gap->away (21-19 fit · 3-10 fwd); money_moving->home (14-19 fit · 6-6 fwd); consensus_gap->home (13-30 fit · 4-9 fwd); pin_move->away (15-11 fit · 4-6 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | moneyline | home | +22.4 | 2-1 | -330 (-330) | -310 | 1.1 | -319 ($10,000) |  |  | 98% / 98% | 7497 | follow_move->home (17-18 fit · 5-5 fwd); money_level->home (35-7 fit · 9-4 fwd); consensus_gap->away (13-30 fit · 4-9 fwd) |

## B  weighted ROI +10% to +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Baltimore Ravens @ Houston Texans | total | over **SPLIT** | +15.2 | 4-2 | 47.5 (-105) | 46.5 | 1 | 47.5 ($5,000) |  |  | 69% / 72% | 6820 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->over (10-9 fit · 9-2 fwd); money_level->over (23-19 fit · 7-6 fwd); sharp_gap->over (21-22 fit · 6-6 fwd); money_moving->under (15-18 fit · 7-6 fwd); pin_move->over (14-13 fit · 11-2 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | spread | home | +13 | 2-1 | -14.5 (-105) | -14 | 0.5 | -14.5 ($20,000) |  |  | 90% / 89% | 6447 | follow_move->home (16-21 fit · 5-7 fwd); money_level->home (25-17 fit · 3-9 fwd); sharp_gap->away (17-25 fit · 7-6 fwd) |

## C  weighted ROI 0 to +10%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | moneyline | away **SPLIT** | +8.4 | 4-2 | -200 (-200) | -142 | 8.1 | -212 ($10,000) |  |  | 90% / 84% | 21911 | follow_move->away (17-18 fit · 5-5 fwd); money_level->away (35-7 fit · 9-4 fwd); sharp_gap->home (21-19 fit · 3-10 fwd); money_moving->away (14-19 fit · 6-6 fwd); consensus_gap->home (13-30 fit · 4-9 fwd); pin_move->away (15-11 fit · 4-6 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | total | over **SPLIT** | +1.2 | 2-2 | 42.5 (-100) | 42.5 |  | 42 ($5,000) | +0.5 |  | 75% / 73% | 6628 | money_level->over (23-19 fit · 7-6 fwd); sharp_gap->under (21-22 fit · 6-6 fwd); money_moving->over (15-18 fit · 7-6 fwd); pin_value->under (12-11 fit · 4-2 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | spread | away | +8.8 | 3-1 | 2.5 (-100) | 2.5 |  | 2.5 ($50,000) |  |  | 58% / 61% | 45721 | money_level->away (25-17 fit · 3-9 fwd); sharp_gap->away (17-25 fit · 7-6 fwd); money_moving->home (10-21 fit · 5-8 fwd); pin_move->away (8-10 fit · 3-5 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | spread | home | +8.4 | 1-0 | -6.5 (-110) | -6.5 |  | -6.5 ($20,000) |  |  | 57% / 57% | 6820 | money_level->home (25-17 fit · 3-9 fwd) |
| Thu 16:30 | Philadelphia Eagles @ Dallas Cowboys | tt_home | under | +4.6 | 1-0 | 29.5 (-111) | 29.5 |  | 28.5 ($2,000) | -1 |  | 0% / 0% | 36941 | pin_value->under (17-12 fit · 3-4 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | tt_away | over | +2.3 | 1-0 | 20.5 (-102) | 19.5 | 1 | 20.5 ($2,000) |  |  | 0% / 0% | 21911 | follow_move->over (9-7 fit · 5-1 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | tt_away | under | +2.3 | 1-0 | 16.5 (-100) | 17.5 | 1 | 16.5 ($2,000) |  |  | 0% / 0% | 7497 | follow_move->under (9-7 fit · 5-1 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | tt_away | under | +2 | 1-1 | 21.5 (-113) | 23.5 | 2 | 23.5 ($2,000) | +2 |  | 0% / 0% | 45721 | follow_move->under (9-7 fit · 5-1 fwd); pin_value->over (14-12 fit · 2-7 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | tt_away | under | +2 | 1-1 | 22.5 (-100) | 23.5 | 1 | 23.5 ($2,000) | +1 |  | 0% / 0% | 4351 | follow_move->under (9-7 fit · 5-1 fwd); pin_value->over (14-12 fit · 2-7 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | tt_away | over | +2 | 1-1 | 20.5 (-102) | 19.5 | 1 | 19.5 ($2,000) | +1 |  | 0% / 0% | 6820 | follow_move->over (9-7 fit · 5-1 fwd); pin_value->under (14-12 fit · 2-7 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | tt_away | under | +2 | 1-1 | 23.5 (-100) | 24.5 | 1 | 24.5 ($2,000) | +1 |  | 0% / 0% | 6628 | follow_move->under (9-7 fit · 5-1 fwd); pin_value->over (14-12 fit · 2-7 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | tt_away | over | +2 | 1-1 | 17.5 (+104) | 16.5 | 1 | 15.5 ($2,000) | +2 |  | 0% / 0% | 6447 | follow_move->over (9-7 fit · 5-1 fwd); pin_value->under (14-12 fit · 2-7 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | tt_away | under | +2 | 1-1 | 16.5 (-100) | 17.5 | 1 | 17.5 ($2,000) | +1 |  | 0% / 0% | 6280 | follow_move->under (9-7 fit · 5-1 fwd); pin_value->over (14-12 fit · 2-7 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | tt_away | over | +0.3 | 1-0 | 19.5 (-115) | 19.5 |  | 20.5 ($2,000) | -1 |  | 0% / 0% | 5639 | pin_value->over (14-12 fit · 2-7 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | total | over | +0.1 | 2-1 | 43.5 (-115) | 43.5 |  | 43.5 ($10,000) |  |  | 81% / 79% | 5316 | money_level->over (23-19 fit · 7-6 fwd); sharp_gap->under (21-22 fit · 6-6 fwd); money_moving->over (15-18 fit · 7-6 fwd) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 16:30 | Philadelphia Eagles @ Dallas Cowboys | total | over **SPLIT** | -12.7 | 3-2 | 47.5 (-120) | 48.5 | 1 | 48.5 ($5,000) | -1 |  | 7% / 7% | 36941 | follow_move->under (10-9 fit · 9-2 fwd); money_level->under (23-19 fit · 7-6 fwd); money_moving->over (15-18 fit · 7-6 fwd); pin_value->over (12-11 fit · 4-2 fwd); pin_move->over (14-13 fit · 11-2 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | total | under **SPLIT** | -16.3 | 6-2 | 39.5 (-105) | 41.5 | 2 | 40.5 ($5,000) **retraced +1** | +1 | over 75% | 25% / 30% | 6280 | follow_move->under (10-9 fit · 9-2 fwd); rlm->under (4-5 fit · 4-1 fwd); rlm_ratio->under (3-1 fit · 0-0 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 7-6 fwd); sharp_gap->under (21-22 fit · 6-6 fwd); money_moving->under (15-18 fit · 7-6 fwd); pin_value->over (12-11 fit · 4-2 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | spread | away **SPLIT** | -17.1 | 2-2 | 7 (-115) | 7 |  | 7 ($20,000) |  |  | 21% / 19% | 7497 | money_delta->away (3-14 fit · 1-0 fwd); money_level->home (25-17 fit · 3-9 fwd); sharp_gap->home (17-25 fit · 7-6 fwd); consensus_gap->away (5-3 fit · 0-2 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | total | under **SPLIT** | -21.1 | 6-2 | 49.5 (-110) | 50.5 | 1 | 49 ($5,000) | -0.5 |  | 41% / 37% | 5639 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->under (10-9 fit · 9-2 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 7-6 fwd); sharp_gap->over (21-22 fit · 6-6 fwd); money_moving->under (15-18 fit · 7-6 fwd); pin_value->under (12-11 fit · 4-2 fwd); pin_move->under (14-13 fit · 11-2 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | total | under **SPLIT** | -31.3 | 6-2 | 40.5 (-105) | 41.5 | 1 | 41 ($5,000) | +0.5 | over 75% | 25% / 27% | 4351 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->under (10-9 fit · 9-2 fwd); rlm->under (4-5 fit · 4-1 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 7-6 fwd); sharp_gap->under (21-22 fit · 6-6 fwd); money_moving->under (15-18 fit · 7-6 fwd); pin_value->over (12-11 fit · 4-2 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | spread | away **SPLIT** | -33.5 | 3-2 | -1.5 (-105) | 3.5 | 5 | 1 ($5,000) | -2.5 |  | 63% / 62% | 5866 | follow_move->away (16-21 fit · 5-7 fwd); money_level->away (25-17 fit · 3-9 fwd); sharp_gap->home (17-25 fit · 7-6 fwd); money_moving->away (10-21 fit · 5-8 fwd); pin_value->home (16-3 fit · 2-3 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | moneyline | home **SPLIT** | -35 | 4-3 | -102 (-102) | -112 | 2.3 | 102 ($3,000) |  |  | 34% / 49% | 5866 | money_delta->home (4-5 fit · 1-2 fwd); follow_move->away (17-18 fit · 5-5 fwd); money_level->away (35-7 fit · 9-4 fwd); sharp_gap->home (21-19 fit · 3-10 fwd); money_moving->home (14-19 fit · 6-6 fwd); consensus_gap->home (13-30 fit · 4-9 fwd); pin_move->away (15-11 fit · 4-6 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | moneyline | away **SPLIT** | -35 | 4-3 | 136 (+136) | 126 | 2.2 | 142 ($20,000) |  |  | 34% / 47% | 5316 | money_delta->away (4-5 fit · 1-2 fwd); follow_move->home (17-18 fit · 5-5 fwd); money_level->home (35-7 fit · 9-4 fwd); sharp_gap->away (21-19 fit · 3-10 fwd); money_moving->away (14-19 fit · 6-6 fwd); consensus_gap->away (13-30 fit · 4-9 fwd); pin_move->home (15-11 fit · 4-6 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | spread | away **SPLIT** | -41 | 3-2 | 2.5 (-105) | 2 | 0.5 | 2.5 ($5,000) |  |  | 30% / 31% | 8951 | follow_move->home (16-21 fit · 5-7 fwd); money_level->home (25-17 fit · 3-9 fwd); sharp_gap->away (17-25 fit · 7-6 fwd); money_moving->away (10-21 fit · 5-8 fwd); pin_move->away (8-10 fit · 3-5 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | spread | home **SPLIT** | -59.7 | 4-3 | 6.5 (-115) | 7 | 0.5 | 6.5 ($30,000) |  | away 78% | 22% / 20% | 6628 | money_delta->home (3-14 fit · 1-0 fwd); follow_move->home (16-21 fit · 5-7 fwd); rlm->home (1-11 fit · 3-2 fwd); rlm_quiet->home (1-9 fit · 3-2 fwd); money_level->away (25-17 fit · 3-9 fwd); sharp_gap->away (17-25 fit · 7-6 fwd); money_moving->away (10-21 fit · 5-8 fwd) |
| Thu 13:00 | Chicago Bears @ Detroit Lions | moneyline | home **SPLIT** | -76.7 | 5-2 | 112 (+112) | 124 | 2.5 | 100 ($30,000) |  |  | 50% / 47% | 59408 | follow_move->home (17-18 fit · 5-5 fwd); money_level->away (35-7 fit · 9-4 fwd); sharp_gap->away (21-19 fit · 3-10 fwd); money_moving->home (14-19 fit · 6-6 fwd); consensus_gap->home (13-30 fit · 4-9 fwd); pin_value->home (2-7 fit · 1-3 fwd); pin_move->home (15-11 fit · 4-6 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | moneyline | away **SPLIT** | -77.1 | 7-2 | 240 (+240) | 265 | 2.1 | 251 ($10,000) |  | home 95% | 5% / 6% | 6820 | follow_move->away (17-18 fit · 5-5 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 9-4 fwd); sharp_gap->away (21-19 fit · 3-10 fwd); money_moving->home (14-19 fit · 6-6 fwd); consensus_gap->away (13-30 fit · 4-9 fwd); pin_rlm->away (2-7 fit · 0-3 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | moneyline | home **SPLIT** | -87.6 | 5-2 | 280 (+280) | 300 | 1.3 | 273 ($10,000) |  | away 97% | 3% / 3% | 5154 | follow_move->home (17-18 fit · 5-5 fwd); rlm->home (4-16 fit · 1-2 fwd); rlm_quiet->home (2-15 fit · 1-2 fwd); money_level->away (35-7 fit · 9-4 fwd); money_moving->away (14-19 fit · 6-6 fwd); consensus_gap->home (13-30 fit · 4-9 fwd); pin_move->home (15-11 fit · 4-6 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | spread | home **SPLIT** | -91.7 | 5-2 | -3 (-104) | -2.5 | 0.5 | -3 ($30,000) |  |  | 41% / 46% | 5316 | money_delta->home (3-14 fit · 1-0 fwd); follow_move->home (16-21 fit · 5-7 fwd); money_level->away (25-17 fit · 3-9 fwd); sharp_gap->home (17-25 fit · 7-6 fwd); money_moving->home (10-21 fit · 5-8 fwd); consensus_gap->away (5-3 fit · 0-2 fwd); pin_move->home (8-10 fit · 3-5 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | moneyline | away **SPLIT** | -96 | 6-2 | 128 (+128) | 132 | 0.6 | 133 ($30,000) |  | home 72% | 28% / 42% | 45721 | follow_move->away (17-18 fit · 5-5 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 9-4 fwd); sharp_gap->away (21-19 fit · 3-10 fwd); money_moving->home (14-19 fit · 6-6 fwd); consensus_gap->away (13-30 fit · 4-9 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | moneyline | away **SPLIT** | -96 | 6-2 | 420 (+420) | 430 | 0.7 | 434 ($10,000) |  | home 98% | 2% / 3% | 5639 | follow_move->away (17-18 fit · 5-5 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 9-4 fwd); sharp_gap->away (21-19 fit · 3-10 fwd); money_moving->home (14-19 fit · 6-6 fwd); consensus_gap->away (13-30 fit · 4-9 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | moneyline | away **SPLIT** | -96 | 6-2 | 190 (+190) | 198 | 0.9 | 200 ($10,000) |  | home 77% | 23% / 41% | 6280 | follow_move->away (17-18 fit · 5-5 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 9-4 fwd); sharp_gap->away (21-19 fit · 3-10 fwd); money_moving->home (14-19 fit · 6-6 fwd); consensus_gap->away (13-30 fit · 4-9 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | tt_home | under | -1.2 | 2-0 | 16.5 (-115) | 17.5 | 1 | 16.5 ($2,000) |  |  | 0% / 0% | 21911 | follow_move->under (9-10 fit · 3-3 fwd); pin_move->under (1-0 fit · 0-0 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | total | under | -2.2 | 8-1 | 36.5 (-106) | 37.5 | 1 | 36.5 ($5,000) |  | over 77% | 23% / 35% | 21911 | follow_move->under (10-9 fit · 9-2 fwd); rlm->under (4-5 fit · 4-1 fwd); rlm_ratio->under (3-1 fit · 0-0 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 7-6 fwd); sharp_gap->under (21-22 fit · 6-6 fwd); money_moving->under (15-18 fit · 7-6 fwd); pin_move->under (14-13 fit · 11-2 fwd); pin_rlm->under (3-1 fit · 0-0 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | total | under | -2.6 | 5-0 | 45.5 (-110) | 48.5 | 3 | 45 ($5,000) | -0.5 |  | 69% / 81% | 45721 | follow_move->under (10-9 fit · 9-2 fwd); money_level->under (23-19 fit · 7-6 fwd); sharp_gap->under (21-22 fit · 6-6 fwd); pin_value->under (12-11 fit · 4-2 fwd); pin_move->under (14-13 fit · 11-2 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | total | over | -2.6 | 5-0 | 49.5 (-110) | 47.5 | 2 | 50 ($5,000) | -0.5 |  | 75% / 86% | 6447 | follow_move->over (10-9 fit · 9-2 fwd); money_level->over (23-19 fit · 7-6 fwd); sharp_gap->over (21-22 fit · 6-6 fwd); pin_value->over (12-11 fit · 4-2 fwd); pin_move->over (14-13 fit · 11-2 fwd) |
| Thu 13:00 | Chicago Bears @ Detroit Lions | tt_home | over | -4.6 | 1-0 | 27.5 (-108) | 26.5 | 1 | 27.5 ($2,000) |  |  | 0% / 0% | 59408 | follow_move->over (9-10 fit · 3-3 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | tt_home | under | -4.6 | 1-0 | 17.5 (-115) | 18.5 | 1 | 17.5 ($2,000) |  |  | 0% / 0% | 4351 | follow_move->under (9-10 fit · 3-3 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | tt_home | over | -4.6 | 1-0 | 27.5 (-100) | 26.5 | 1 | 27.5 ($2,000) |  |  | 0% / 0% | 6820 | follow_move->over (9-10 fit · 3-3 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | tt_home | over | -4.6 | 1-0 | 31.5 (-111) | 30.5 | 1 | 31.5 ($2,000) |  |  | 0% / 0% | 6447 | follow_move->over (9-10 fit · 3-3 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | tt_home | over | -4.6 | 1-0 | 23.5 (-108) | 22.5 | 1 | 23.5 ($2,000) |  |  | 0% / 0% | 5316 | follow_move->over (9-10 fit · 3-3 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | spread | away | -6.5 | 4-1 | -7 (-105) | -7 |  | -7.5 ($20,000) | +0.5 |  | 82% / 83% | 5154 | money_level->away (25-17 fit · 3-9 fwd); sharp_gap->away (17-25 fit · 7-6 fwd); money_moving->away (10-21 fit · 5-8 fwd); consensus_gap->home (5-3 fit · 0-2 fwd); pin_value->away (16-3 fit · 2-3 fwd) |
| Thu 13:00 | Chicago Bears @ Detroit Lions | total | under | -8.7 | 3-0 | 55.5 (-108) | 55.5 |  | 55.5 ($5,000) |  |  | 83% / 88% | 59408 | money_level->under (23-19 fit · 7-6 fwd); sharp_gap->under (21-22 fit · 6-6 fwd); money_moving->under (15-18 fit · 7-6 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | total | over | -8.7 | 3-0 | 41.5 (-110) | 41.5 |  | 41.5 ($5,000) |  |  | 81% / 83% | 5154 | money_level->over (23-19 fit · 7-6 fwd); sharp_gap->over (21-22 fit · 6-6 fwd); money_moving->over (15-18 fit · 7-6 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | tt_home | under | -9.2 | 1-1 | 23.5 (-102) | 25.5 | 2 | 26.5 ($2,000) | +3 |  | 0% / 0% | 45721 | follow_move->under (9-10 fit · 3-3 fwd); pin_value->over (17-12 fit · 3-4 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | tt_home | over | -9.2 | 1-1 | 17.5 (+102) | 16.5 | 1 | 16.5 ($2,000) | +1 |  | 0% / 0% | 6628 | follow_move->over (9-10 fit · 3-3 fwd); pin_value->under (17-12 fit · 3-4 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | tt_home | under | -9.2 | 1-1 | 23.5 (-113) | 24.5 | 1 | 24.5 ($2,000) | +1 |  | 0% / 0% | 8951 | follow_move->under (9-10 fit · 3-3 fwd); pin_value->over (17-12 fit · 3-4 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | tt_home | under | -9.2 | 1-1 | 22.5 (-104) | 23.5 | 1 | 23.5 ($2,000) | +1 |  | 0% / 0% | 6280 | follow_move->under (9-10 fit · 3-3 fwd); pin_value->over (17-12 fit · 3-4 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | total | under | -15.1 | 2-1 | 35.5 (-108) | 35.5 |  | 35.5 ($3,000) |  |  | 15% / 16% | 5866 | money_level->over (23-19 fit · 7-6 fwd); sharp_gap->under (21-22 fit · 6-6 fwd); money_moving->under (15-18 fit · 7-6 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | total | under | -15.7 | 4-1 | 41.5 (-110) | 42.5 | 1 | 41.5 ($5,000) |  | over 69% | 31% / 32% | 7497 | follow_move->under (10-9 fit · 9-2 fwd); rlm->under (4-5 fit · 4-1 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 7-6 fwd); sharp_gap->under (21-22 fit · 6-6 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | spread | away | -19.7 | 6-0 | -3.5 (-114) | -1.5 | 2 | -4 ($20,000) | +0.5 |  | 79% / 86% | 21911 | follow_move->away (16-21 fit · 5-7 fwd); money_level->away (25-17 fit · 3-9 fwd); sharp_gap->away (17-25 fit · 7-6 fwd); money_moving->away (10-21 fit · 5-8 fwd); pin_value->away (16-3 fit · 2-3 fwd); pin_move->away (8-10 fit · 3-5 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | spread | away | -19.7 | 6-0 | -4.5 (-110) | -4 | 0.5 | -5 ($20,000) | +0.5 |  | 50% / 52% | 4351 | follow_move->away (16-21 fit · 5-7 fwd); money_level->away (25-17 fit · 3-9 fwd); sharp_gap->away (17-25 fit · 7-6 fwd); money_moving->away (10-21 fit · 5-8 fwd); pin_value->away (16-3 fit · 2-3 fwd); pin_move->away (8-10 fit · 3-5 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | total | under | -34.1 | 8-1 | 44.5 (-110) | 46.5 | 2 | 44 ($3,000) | -0.5 | over 83% | 17% / 20% | 8951 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->under (10-9 fit · 9-2 fwd); rlm->under (4-5 fit · 4-1 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 7-6 fwd); sharp_gap->under (21-22 fit · 6-6 fwd); money_moving->under (15-18 fit · 7-6 fwd); pin_value->under (12-11 fit · 4-2 fwd); pin_move->under (14-13 fit · 11-2 fwd) |
| Thu 16:30 | Philadelphia Eagles @ Dallas Cowboys | spread | home | -38.2 | 4-0 | -8.5 (-110) | -1.5 | 7 | -8.5 ($50,000) |  |  | 53% / 54% | 36941 | follow_move->home (16-21 fit · 5-7 fwd); money_level->home (25-17 fit · 3-9 fwd); sharp_gap->home (17-25 fit · 7-6 fwd); money_moving->home (10-21 fit · 5-8 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | spread | away | -38.2 | 4-0 | 4.5 (-105) | 5 | 0.5 | 4.5 ($20,000) |  |  | 67% / 68% | 6280 | follow_move->away (16-21 fit · 5-7 fwd); money_level->away (25-17 fit · 3-9 fwd); sharp_gap->away (17-25 fit · 7-6 fwd); money_moving->away (10-21 fit · 5-8 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | moneyline | away | -48.6 | 5-1 | 750 (+750) | 750 |  | 727 ($10,000) |  |  | 2% / 5% | 6447 | pre_move->away (1-3 fit · 0-3 fwd); money_level->home (35-7 fit · 9-4 fwd); sharp_gap->away (21-19 fit · 3-10 fwd); money_moving->away (14-19 fit · 6-6 fwd); consensus_gap->away (13-30 fit · 4-9 fwd); pin_rlm->away (2-7 fit · 0-3 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | moneyline | away | -79.4 | 10-1 | 122 (+122) | 144 | 4.2 | 122 ($3,000) |  | home 90% | 10% / 20% | 8951 | money_delta->away (4-5 fit · 1-2 fwd); follow_move->away (17-18 fit · 5-5 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 9-4 fwd); sharp_gap->away (21-19 fit · 3-10 fwd); money_moving->away (14-19 fit · 6-6 fwd); consensus_gap->away (13-30 fit · 4-9 fwd); pin_move->away (15-11 fit · 4-6 fwd); pin_rlm->away (2-7 fit · 0-3 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | moneyline | home | -101.8 | 5-1 | 240 (+240) | 265 | 2 | 232 ($10,000) |  | away 95% | 5% / 5% | 6628 | follow_move->home (17-18 fit · 5-5 fwd); rlm->home (4-16 fit · 1-2 fwd); rlm_quiet->home (2-15 fit · 1-2 fwd); money_level->away (35-7 fit · 9-4 fwd); consensus_gap->home (13-30 fit · 4-9 fwd); pin_move->home (15-11 fit · 4-6 fwd) |

