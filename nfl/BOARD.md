# NFL board

Generated 2026-11-27 19:12 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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
| PINNACLE moved vs public | Seattle Seahawks @ San Francisco 49ers | moneyline | away | Pinnacle | 153 -> 126 | **+0.9** | 126 | 11% | 1.64 | 5-10 fit · 0-4 fwd |
| PINNACLE moved vs public | Washington Commanders @ Arizona Cardinals | moneyline | home | Pinnacle | 294 -> 266 | — | 290 | 3% | 2.67 | 5-10 fit · 0-4 fwd |
| FanDuel moved vs public | Las Vegas Raiders @ Cleveland Browns | moneyline | away | FanDuel | 198 -> 194 | **+0.6** | 194 | 22% | 1.91 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Seattle Seahawks @ San Francisco 49ers | moneyline | away | FanDuel | 144 -> 126 | **+0.9** | 126 | 11% | 1.64 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Washington Commanders @ Arizona Cardinals | moneyline | home | FanDuel | 300 -> 290 | — | 290 | 3% | 2.67 | 6-14 fit · 0-2 fwd |
| line moved off the public (no ratio test) | Atlanta Falcons @ Minnesota Vikings | total | under | FanDuel | 42.5 -> 41.5 | — | 41.5 | 34% | 0.97 | 9-32 fit · 9-5-1 fwd |
| line moved off the public (no ratio test) | Baltimore Ravens @ Houston Texans | moneyline | away | FanDuel | 265 -> 240 | **+0.7** | 240 | 6% | 1.0 | 9-32 fit · 9-5-1 fwd |
| line moved off the public (no ratio test) | Carolina Panthers @ Tampa Bay Buccaneers | spread | home | FanDuel | -2.5 -> -3 | — | -3 | 40% | 1.07 | 9-32 fit · 9-5-1 fwd |
| line moved off the public (no ratio test) | Denver Broncos @ Pittsburgh Steelers | total | under | FanDuel | 37.5 -> 36.5 | **+1** | 36.5 | 27% | 1.15 | 9-32 fit · 9-5-1 fwd |
| line moved off the public (no ratio test) | Las Vegas Raiders @ Cleveland Browns | total | under | FanDuel | 41.5 -> 39.5 | — | 39.5 | 22% | 1.14 | 9-32 fit · 9-5-1 fwd |
| line moved off the public (no ratio test) | New Orleans Saints @ Cincinnati Bengals | spread | away | FanDuel | 10 -> 9.5 | — | 9.5 | 9% | 0.89 | 9-32 fit · 9-5-1 fwd |
| line moved off the public (no ratio test) | New York Giants @ Indianapolis Colts | spread | home | FanDuel | 7 -> 5.5 | — | 5.5 | 18% | 0.83 | 9-32 fit · 9-5-1 fwd |
| line moved off the public (no ratio test) | New York Giants @ Indianapolis Colts | moneyline | home | FanDuel | 265 -> 225 | — | 225 | 5% | 0.8 | 9-32 fit · 9-5-1 fwd |
| line moved off the public (no ratio test) | New York Jets @ Miami Dolphins | total | under | FanDuel | 41.5 -> 40.5 | — | 40.5 | 30% | 0.83 | 9-32 fit · 9-5-1 fwd |
| line moved off the public (no ratio test) | Seattle Seahawks @ San Francisco 49ers | total | under | FanDuel | 46.5 -> 44.5 | — | 44.5 | 22% | 1.09 | 9-32 fit · 9-5-1 fwd |
| line moved off the public (no ratio test) | Tennessee Titans @ Jacksonville Jaguars | moneyline | away | FanDuel | 750 -> 700 | — | 700 | 2% | 1.0 | 9-32 fit · 9-5-1 fwd |

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
| Sun 13:00 | New York Giants @ Indianapolis Colts | spread | away **SPLIT** | +57.7 | 4-3 | -5.5 (-115) | -7 | 1.5 | -6.5 ($30,000) | +1 | away 82% | 82% / 85% | 10925 | follow_move->home (16-21 fit · 6-8-1 fwd); rlm->home (1-11 fit · 3-2-1 fwd); rlm_quiet->home (1-9 fit · 3-2-1 fwd); money_level->away (25-17 fit · 3-11-1 fwd); sharp_gap->away (17-25 fit · 7-8-1 fwd); money_moving->away (10-21 fit · 6-9-1 fwd); pin_value->away (16-3 fit · 2-4 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | spread | home **SPLIT** | +51.3 | 5-3 | -9.5 (-120) | -10 | 0.5 | -10.5 ($20,000) | +1 | home 91% | 91% / 92% | 10112 | follow_move->away (16-21 fit · 6-8-1 fwd); rlm->away (1-11 fit · 3-2-1 fwd); rlm_quiet->away (1-9 fit · 3-2-1 fwd); money_level->home (25-17 fit · 3-11-1 fwd); sharp_gap->home (17-25 fit · 7-8-1 fwd); money_moving->home (10-21 fit · 6-9-1 fwd); pin_value->home (16-3 fit · 2-4 fwd); pin_move->home (8-10 fit · 3-6 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | moneyline | away **SPLIT** | +36.8 | 3-3 | -255 (-255) | -205 | 4.5 | -237 ($10,000) |  |  | 88% / 86% | 6810 | follow_move->away (17-18 fit · 6-7 fwd); money_level->away (35-7 fit · 10-6 fwd); sharp_gap->home (21-19 fit · 3-12 fwd); money_moving->home (14-19 fit · 8-7 fwd); consensus_gap->home (13-30 fit · 5-11 fwd); pin_move->away (15-11 fit · 5-7 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | spread | away **SPLIT** | +28.2 | 3-2 | -4.5 (-115) | -1.5 | 3 | -4.5 ($100,000) |  |  | 82% / 79% | 90639 | follow_move->away (16-21 fit · 6-8-1 fwd); money_level->away (25-17 fit · 3-11-1 fwd); sharp_gap->home (17-25 fit · 7-8-1 fwd); money_moving->home (10-21 fit · 6-9-1 fwd); pin_move->away (8-10 fit · 3-6 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | moneyline | home | +22.4 | 2-1 | -330 (-330) | -310 | 1.1 | -319 ($10,000) |  |  | 97% / 97% | 11914 | follow_move->home (17-18 fit · 6-7 fwd); money_level->home (35-7 fit · 10-6 fwd); consensus_gap->away (13-30 fit · 5-11 fwd) |

## B  weighted ROI +10% to +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Baltimore Ravens @ Houston Texans | total | over **SPLIT** | +15.2 | 4-2 | 47.5 (-105) | 46.5 | 1 | 47.5 ($5,000) |  |  | 62% / 66% | 10294 | money_delta->under (4-7 fit · 2-4 fwd); follow_move->over (10-9 fit · 11-2 fwd); money_level->over (23-19 fit · 8-8 fwd); sharp_gap->over (21-22 fit · 7-7 fwd); money_moving->under (15-18 fit · 8-7 fwd); pin_move->over (14-13 fit · 14-2 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | spread | home | +13.5 | 3-1 | 7 (-115) | 7 |  | 6.5 ($20,000) | +0.5 |  | 16% / 16% | 9203 | money_level->away (25-17 fit · 3-11-1 fwd); consensus_gap->home (5-3 fit · 0-2-1 fwd); pin_value->home (16-3 fit · 2-4 fwd); pin_move->home (8-10 fit · 3-6 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | total | over | +10.7 | 1-1 | 35.5 (-112) | 35.5 |  | 35.5 ($3,000) |  |  | 85% / 85% | 8158 | money_level->over (23-19 fit · 8-8 fwd); money_moving->under (15-18 fit · 8-7 fwd) |

## C  weighted ROI 0 to +10%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | spread | home **SPLIT** | +9.6 | 2-2 | -14.5 (-100) | -14 | 0.5 | -14.5 ($10,000) |  |  | 89% / 88% | 10768 | follow_move->home (16-21 fit · 6-8-1 fwd); money_level->home (25-17 fit · 3-11-1 fwd); sharp_gap->away (17-25 fit · 7-8-1 fwd); consensus_gap->away (5-3 fit · 0-2-1 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | moneyline | away **SPLIT** | +8.4 | 4-2 | -250 (-250) | -142 | 12.7 | -245 ($75,000) |  |  | 88% / 82% | 90639 | follow_move->away (17-18 fit · 6-7 fwd); money_level->away (35-7 fit · 10-6 fwd); sharp_gap->home (21-19 fit · 3-12 fwd); money_moving->away (14-19 fit · 8-7 fwd); consensus_gap->home (13-30 fit · 5-11 fwd); pin_move->away (15-11 fit · 5-7 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | total | over **SPLIT** | +1.2 | 2-2 | 42.5 (-100) | 42.5 |  | 42 ($5,000) | +0.5 |  | 75% / 73% | 10925 | money_level->over (23-19 fit · 8-8 fwd); sharp_gap->under (21-22 fit · 7-7 fwd); money_moving->over (15-18 fit · 8-7 fwd); pin_value->under (12-11 fit · 5-3 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | total | under **SPLIT** | +0.6 | 3-3 | 41.5 (-110) | 42.5 | 1 | 41.5 ($5,000) |  | over 66% | 34% / 33% | 11914 | follow_move->under (10-9 fit · 11-2 fwd); rlm->under (4-5 fit · 5-1 fwd); rlm_quiet->under (3-4 fit · 5-1 fwd); money_level->over (23-19 fit · 8-8 fwd); sharp_gap->over (21-22 fit · 7-7 fwd); money_moving->over (15-18 fit · 8-7 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | spread | home | +8.4 | 1-0 | -6.5 (-110) | -6.5 |  | -6.5 ($20,000) |  |  | 60% / 60% | 10294 | money_level->home (25-17 fit · 3-11-1 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | moneyline | home | +8.2 | 3-1 | -600 (-600) | -590 | 0.2 | -570 ($10,000) |  |  | 98% / 98% | 10112 | follow_move->home (17-18 fit · 6-7 fwd); money_level->home (35-7 fit · 10-6 fwd); money_moving->home (14-19 fit · 8-7 fwd); consensus_gap->away (13-30 fit · 5-11 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | tt_home | over | +4.6 | 1-0 | 30.5 (-128) | 30.5 |  | 31.5 ($2,000) | -1 |  | 0% / 0% | 10768 | pin_value->over (17-12 fit · 3-6 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | tt_away | over | +2.3 | 1-0 | 20.5 (-111) | 19.5 | 1 | 20.5 ($5,000) |  |  | 0% / 0% | 90639 | follow_move->over (9-7 fit · 6-1 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | tt_away | under | +2.3 | 1-0 | 16.5 (-102) | 17.5 | 1 | 16.5 ($2,000) |  |  | 0% / 0% | 11914 | follow_move->under (9-7 fit · 6-1 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | tt_away | under | +2 | 1-1 | 22.5 (+102) | 23.5 | 1 | 23.5 ($2,000) | +1 |  | 0% / 0% | 6810 | follow_move->under (9-7 fit · 6-1 fwd); pin_value->over (14-12 fit · 2-8 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | tt_away | over | +2 | 1-1 | 20.5 (-102) | 19.5 | 1 | 19.5 ($2,000) | +1 |  | 0% / 0% | 10294 | follow_move->over (9-7 fit · 6-1 fwd); pin_value->under (14-12 fit · 2-8 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | tt_away | under | +2 | 1-1 | 23.5 (-106) | 24.5 | 1 | 24.5 ($2,000) | +1 |  | 0% / 0% | 10925 | follow_move->under (9-7 fit · 6-1 fwd); pin_value->over (14-12 fit · 2-8 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | tt_away | over | +2 | 1-1 | 18.5 (-111) | 17.5 | 1 | 17.5 ($2,000) | +1 |  | 0% / 0% | 8158 | follow_move->over (9-7 fit · 6-1 fwd); pin_value->under (14-12 fit · 2-8 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | tt_away | under | +2 | 1-1 | 20.5 (-113) | 21.5 | 1 | 21.5 ($2,000) | +1 |  | 0% / 0% | 13187 | follow_move->under (9-7 fit · 6-1 fwd); pin_value->over (14-12 fit · 2-8 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | tt_away | under | +2 | 1-1 | 16.5 (-104) | 17.5 | 1 | 17.5 ($2,000) | +1 |  | 0% / 0% | 10198 | follow_move->under (9-7 fit · 6-1 fwd); pin_value->over (14-12 fit · 2-8 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | total | over | +0.5 | 3-1 | 41.5 (-110) | 41.5 |  | 41.5 ($5,000) |  |  | 72% / 74% | 9203 | money_delta->under (4-7 fit · 2-4 fwd); money_level->over (23-19 fit · 8-8 fwd); sharp_gap->over (21-22 fit · 7-7 fwd); money_moving->over (15-18 fit · 8-7 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | tt_away | over | +0.3 | 1-0 | 19.5 (-108) | 19.5 |  | 20.5 ($2,000) | -1 |  | 0% / 0% | 10112 | pin_value->over (14-12 fit · 2-8 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | tt_away | under | +0.3 | 1-0 | 16.5 (-104) | 16.5 |  | 15.5 ($2,000) | -1 |  | 0% / 0% | 10768 | pin_value->under (14-12 fit · 2-8 fwd) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | total | under **SPLIT** | -7.7 | 5-3 | 36.5 (-106) | 37.5 | 1 | 37 ($30,000) **retraced +1** | +0.5 | over 73% | 27% / 31% | 90639 | follow_move->under (10-9 fit · 11-2 fwd); rlm->under (4-5 fit · 5-1 fwd); rlm_quiet->under (3-4 fit · 5-1 fwd); money_level->over (23-19 fit · 8-8 fwd); sharp_gap->under (21-22 fit · 7-7 fwd); money_moving->over (15-18 fit · 8-7 fwd); pin_value->over (12-11 fit · 5-3 fwd); pin_move->under (14-13 fit · 14-2 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | total | under **SPLIT** | -8.8 | 5-2 | 39.5 (-110) | 41.5 | 2 | 39.5 ($10,000) |  | over 78% | 22% / 25% | 10198 | follow_move->under (10-9 fit · 11-2 fwd); rlm->under (4-5 fit · 5-1 fwd); rlm_quiet->under (3-4 fit · 5-1 fwd); money_level->over (23-19 fit · 8-8 fwd); sharp_gap->under (21-22 fit · 7-7 fwd); money_moving->over (15-18 fit · 8-7 fwd); pin_move->under (14-13 fit · 14-2 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | total | under **SPLIT** | -10.3 | 6-3 | 40.5 (-120) | 41.5 | 1 | 40 ($5,000) | -0.5 | over 70% | 30% / 25% | 6810 | money_delta->under (4-7 fit · 2-4 fwd); follow_move->under (10-9 fit · 11-2 fwd); rlm->under (4-5 fit · 5-1 fwd); rlm_quiet->under (3-4 fit · 5-1 fwd); money_level->over (23-19 fit · 8-8 fwd); sharp_gap->over (21-22 fit · 7-7 fwd); money_moving->over (15-18 fit · 8-7 fwd); pin_value->under (12-11 fit · 5-3 fwd); pin_move->under (14-13 fit · 14-2 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | total | under **SPLIT** | -21.1 | 6-2 | 49.5 (-120) | 50.5 | 1 | 49 ($5,000) | -0.5 |  | 43% / 42% | 10112 | money_delta->under (4-7 fit · 2-4 fwd); follow_move->under (10-9 fit · 11-2 fwd); rlm_quiet->under (3-4 fit · 5-1 fwd); money_level->over (23-19 fit · 8-8 fwd); sharp_gap->over (21-22 fit · 7-7 fwd); money_moving->under (15-18 fit · 8-7 fwd); pin_value->under (12-11 fit · 5-3 fwd); pin_move->under (14-13 fit · 14-2 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | total | under **SPLIT** | -24 | 3-3 | 48.5 (-115) | 47.5 | 1 | 48.5 ($5,000) **retraced +1.5** |  |  | 27% / 34% | 10768 | money_delta->under (4-7 fit · 2-4 fwd); follow_move->over (10-9 fit · 11-2 fwd); money_level->over (23-19 fit · 8-8 fwd); sharp_gap->under (21-22 fit · 7-7 fwd); money_moving->under (15-18 fit · 8-7 fwd); pin_move->over (14-13 fit · 14-2 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | spread | away **SPLIT** | -27.3 | 4-2 | 7 (-115) | 7 |  | 7 ($20,000) |  |  | 20% / 19% | 11914 | money_delta->away (3-14 fit · 1-0 fwd); money_level->home (25-17 fit · 3-11-1 fwd); sharp_gap->home (17-25 fit · 7-8-1 fwd); money_moving->away (10-21 fit · 6-9-1 fwd); consensus_gap->away (5-3 fit · 0-2-1 fwd); book_lag->away (4-0 fit · 0-0 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | moneyline | home **SPLIT** | -35 | 4-3 | 112 (+112) | -112 | 5.7 | 117 ($3,000) |  |  | 30% / 45% | 8158 | money_delta->home (4-5 fit · 1-2 fwd); follow_move->away (17-18 fit · 6-7 fwd); money_level->away (35-7 fit · 10-6 fwd); sharp_gap->home (21-19 fit · 3-12 fwd); money_moving->home (14-19 fit · 8-7 fwd); consensus_gap->home (13-30 fit · 5-11 fwd); pin_move->away (15-11 fit · 5-7 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | moneyline | away **SPLIT** | -35 | 4-3 | 134 (+134) | 126 | 1.6 | 145 ($20,000) |  |  | 33% / 43% | 8098 | money_delta->away (4-5 fit · 1-2 fwd); follow_move->home (17-18 fit · 6-7 fwd); money_level->home (35-7 fit · 10-6 fwd); sharp_gap->away (21-19 fit · 3-12 fwd); money_moving->away (14-19 fit · 8-7 fwd); consensus_gap->away (13-30 fit · 5-11 fwd); pin_move->home (15-11 fit · 5-7 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | spread | away **SPLIT** | -41 | 3-2 | 2.5 (-100) | 2 | 0.5 | 2.5 ($5,000) |  |  | 30% / 33% | 13187 | follow_move->home (16-21 fit · 6-8-1 fwd); money_level->home (25-17 fit · 3-11-1 fwd); sharp_gap->away (17-25 fit · 7-8-1 fwd); money_moving->away (10-21 fit · 6-9-1 fwd); pin_move->away (8-10 fit · 3-6 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | moneyline | home **SPLIT** | -83.3 | 5-3 | 225 (+225) | 265 | 3.4 | 225 ($10,000) |  | away 95% | 5% / 4% | 10925 | follow_move->home (17-18 fit · 6-7 fwd); rlm->home (4-16 fit · 1-2 fwd); rlm_quiet->home (2-15 fit · 1-2 fwd); money_level->away (35-7 fit · 10-6 fwd); sharp_gap->away (21-19 fit · 3-12 fwd); money_moving->away (14-19 fit · 8-7 fwd); consensus_gap->home (13-30 fit · 5-11 fwd); pin_move->home (15-11 fit · 5-7 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | moneyline | away **SPLIT** | -83.5 | 4-2 | 240 (+240) | 265 | 2.1 | 251 ($10,000) |  | home 94% | 6% / 6% | 10294 | follow_move->away (17-18 fit · 6-7 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 10-6 fwd); money_moving->home (14-19 fit · 8-7 fwd); consensus_gap->away (13-30 fit · 5-11 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | moneyline | away **SPLIT** | -96 | 6-2 | 194 (+194) | 198 | 0.4 | 195 ($20,000) |  | home 78% | 22% / 42% | 10198 | follow_move->away (17-18 fit · 6-7 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 10-6 fwd); sharp_gap->away (21-19 fit · 3-12 fwd); money_moving->home (14-19 fit · 8-7 fwd); consensus_gap->away (13-30 fit · 5-11 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | spread | home **SPLIT** | -115.4 | 6-2 | -3 (-104) | -2.5 | 0.5 | -3 ($30,000) |  | away 60% | 40% / 43% | 8098 | follow_move->home (16-21 fit · 6-8-1 fwd); rlm->home (1-11 fit · 3-2-1 fwd); rlm_quiet->home (1-9 fit · 3-2-1 fwd); money_level->away (25-17 fit · 3-11-1 fwd); sharp_gap->home (17-25 fit · 7-8-1 fwd); money_moving->home (10-21 fit · 6-9-1 fwd); consensus_gap->away (5-3 fit · 0-2-1 fwd); pin_move->home (8-10 fit · 3-6 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | total | over | -4.3 | 2-0 | 43.5 (-115) | 43.5 |  | 43.5 ($10,000) |  |  | 82% / 82% | 8098 | money_level->over (23-19 fit · 8-8 fwd); money_moving->over (15-18 fit · 8-7 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | tt_home | over | -4.6 | 1-0 | 27.5 (-100) | 26.5 | 1 | 27.5 ($2,000) |  |  | 0% / 0% | 10294 | follow_move->over (9-10 fit · 5-3 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | tt_home | over | -4.6 | 1-0 | 23.5 (-108) | 22.5 | 1 | 23.5 ($2,000) |  |  | 0% / 0% | 8098 | follow_move->over (9-10 fit · 5-3 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | tt_home | under | -5.8 | 2-1 | 15.5 (-102) | 17.5 | 2 | 16.5 ($5,000) | +1 |  | 0% / 0% | 90639 | follow_move->under (9-10 fit · 5-3 fwd); pin_value->over (17-12 fit · 3-6 fwd); pin_move->under (1-0 fit · 0-0 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | tt_home | under | -9.2 | 1-1 | 16.5 (+102) | 18.5 | 2 | 17.5 ($2,000) | +1 |  | 0% / 0% | 6810 | follow_move->under (9-10 fit · 5-3 fwd); pin_value->over (17-12 fit · 3-6 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | tt_home | over | -9.2 | 1-1 | 17.5 (-104) | 16.5 | 1 | 16.5 ($2,000) | +1 |  | 0% / 0% | 10925 | follow_move->over (9-10 fit · 5-3 fwd); pin_value->under (17-12 fit · 3-6 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | tt_home | under | -9.2 | 1-1 | 16.5 (-104) | 17.5 | 1 | 17.5 ($2,000) | +1 |  | 0% / 0% | 8158 | follow_move->under (9-10 fit · 5-3 fwd); pin_value->over (17-12 fit · 3-6 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | tt_home | under | -9.2 | 1-1 | 23.5 (-122) | 24.5 | 1 | 24.5 ($2,000) | +1 |  | 0% / 0% | 13187 | follow_move->under (9-10 fit · 5-3 fwd); pin_value->over (17-12 fit · 3-6 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | tt_home | under | -9.2 | 1-1 | 22.5 (-111) | 23.5 | 1 | 23.5 ($2,000) | +1 |  | 0% / 0% | 10198 | follow_move->under (9-10 fit · 5-3 fwd); pin_value->over (17-12 fit · 3-6 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | spread | away | -11.6 | 5-1 | -1.5 (-114) | 3.5 | 5 | -1.5 ($5,000) |  |  | 60% / 59% | 8158 | follow_move->away (16-21 fit · 6-8-1 fwd); money_level->away (25-17 fit · 3-11-1 fwd); sharp_gap->home (17-25 fit · 7-8-1 fwd); money_moving->away (10-21 fit · 6-9-1 fwd); consensus_gap->away (5-3 fit · 0-2-1 fwd); pin_move->away (8-10 fit · 3-6 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | total | under | -34.1 | 8-1 | 44.5 (-120) | 46.5 | 2 | 44 ($3,000) | -0.5 | over 78% | 22% / 24% | 13187 | money_delta->under (4-7 fit · 2-4 fwd); follow_move->under (10-9 fit · 11-2 fwd); rlm->under (4-5 fit · 5-1 fwd); rlm_quiet->under (3-4 fit · 5-1 fwd); money_level->over (23-19 fit · 8-8 fwd); sharp_gap->under (21-22 fit · 7-7 fwd); money_moving->under (15-18 fit · 8-7 fwd); pin_value->under (12-11 fit · 5-3 fwd); pin_move->under (14-13 fit · 14-2 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | spread | away | -38.2 | 4-0 | 4.5 (-105) | 5 | 0.5 | 4.5 ($30,000) |  |  | 70% / 71% | 10198 | follow_move->away (16-21 fit · 6-8-1 fwd); money_level->away (25-17 fit · 3-11-1 fwd); sharp_gap->away (17-25 fit · 7-8-1 fwd); money_moving->away (10-21 fit · 6-9-1 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | spread | away | -69.5 | 5-1 | -5.5 (-110) | -4 | 1.5 | -5 ($20,000) | -0.5 |  | 50% / 52% | 6810 | follow_move->away (16-21 fit · 6-8-1 fwd); money_level->away (25-17 fit · 3-11-1 fwd); sharp_gap->away (17-25 fit · 7-8-1 fwd); money_moving->away (10-21 fit · 6-9-1 fwd); pin_value->home (16-3 fit · 2-4 fwd); pin_move->away (8-10 fit · 3-6 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | moneyline | away | -79.4 | 10-1 | 126 (+126) | 144 | 3.6 | 126 ($3,000) |  | home 89% | 11% / 18% | 13187 | money_delta->away (4-5 fit · 1-2 fwd); follow_move->away (17-18 fit · 6-7 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 10-6 fwd); sharp_gap->away (21-19 fit · 3-12 fwd); money_moving->away (14-19 fit · 8-7 fwd); consensus_gap->away (13-30 fit · 5-11 fwd); pin_move->away (15-11 fit · 5-7 fwd); pin_rlm->away (2-7 fit · 0-3 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | moneyline | away | -97.7 | 4-1 | 700 (+700) | 750 | 0.6 | 675 ($10,000) |  | home 98% | 2% / 2% | 10768 | follow_move->away (17-18 fit · 6-7 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 10-6 fwd); consensus_gap->away (13-30 fit · 5-11 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | moneyline | home | -97.7 | 10-1 | 290 (+290) | 300 | 0.6 | 266 ($10,000) |  | away 97% | 3% / 8% | 9203 | follow_move->home (17-18 fit · 6-7 fwd); rlm->home (4-16 fit · 1-2 fwd); rlm_ratio->home (3-7 fit · 0-1 fwd); rlm_quiet->home (2-15 fit · 1-2 fwd); money_level->away (35-7 fit · 10-6 fwd); sharp_gap->home (21-19 fit · 3-12 fwd); money_moving->home (14-19 fit · 8-7 fwd); consensus_gap->home (13-30 fit · 5-11 fwd); pin_value->home (2-7 fit · 2-4 fwd); pin_move->home (15-11 fit · 5-7 fwd); pin_rlm->home (2-7 fit · 0-3 fwd) |

