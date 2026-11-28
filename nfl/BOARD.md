# NFL board

Generated 2026-11-28 08:21 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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
| PINNACLE moved vs public | New Orleans Saints @ Cincinnati Bengals | moneyline | away | Pinnacle | 421 -> 413 | — | 460 | 2% | 1.5 | 5-10 fit · 0-4 fwd |
| PINNACLE moved vs public | Seattle Seahawks @ San Francisco 49ers | moneyline | away | Pinnacle | 153 -> -113 | — | -116 | 12% | 2.25 | 5-10 fit · 0-4 fwd |
| PINNACLE moved vs public | Tennessee Titans @ Jacksonville Jaguars | moneyline | away | Pinnacle | 729 -> 675 | — | 700 | 2% | 1.5 | 5-10 fit · 0-4 fwd |
| PINNACLE moved vs public | Washington Commanders @ Arizona Cardinals | moneyline | home | Pinnacle | 294 -> 266 | — | 285 | 3% | 2.33 | 5-10 fit · 0-4 fwd |
| FanDuel moved vs public | Las Vegas Raiders @ Cleveland Browns | moneyline | away | FanDuel | 198 -> 190 | **+0.6** | 190 | 22% | 1.91 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Seattle Seahawks @ San Francisco 49ers | moneyline | away | FanDuel | 144 -> -116 | — | -116 | 12% | 2.25 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Tennessee Titans @ Jacksonville Jaguars | moneyline | away | FanDuel | 750 -> 700 | — | 700 | 2% | 1.5 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Washington Commanders @ Arizona Cardinals | moneyline | home | FanDuel | 300 -> 285 | — | 285 | 3% | 2.33 | 6-14 fit · 0-2 fwd |
| line moved off the public (no ratio test) | Atlanta Falcons @ Minnesota Vikings | total | under | FanDuel | 42.5 -> 41.5 | — | 41.5 | 34% | 1.03 | 9-32 fit · 10-5-1 fwd |
| line moved off the public (no ratio test) | Baltimore Ravens @ Houston Texans | moneyline | away | FanDuel | 265 -> 240 | **+0.7** | 240 | 7% | 1.0 | 9-32 fit · 10-5-1 fwd |
| line moved off the public (no ratio test) | Carolina Panthers @ Tampa Bay Buccaneers | spread | home | FanDuel | -2.5 -> -3 | — | -3 | 40% | 1.07 | 9-32 fit · 10-5-1 fwd |
| line moved off the public (no ratio test) | Las Vegas Raiders @ Cleveland Browns | total | under | FanDuel | 41.5 -> 39.5 | — | 39.5 | 21% | 1.14 | 9-32 fit · 10-5-1 fwd |
| line moved off the public (no ratio test) | New Orleans Saints @ Cincinnati Bengals | spread | away | FanDuel | 10 -> 9.5 | — | 9.5 | 10% | 1.0 | 9-32 fit · 10-5-1 fwd |
| line moved off the public (no ratio test) | New Orleans Saints @ Cincinnati Bengals | total | under | FanDuel | 50.5 -> 48.5 | — | 48.5 | 40% | 0.93 | 9-32 fit · 10-5-1 fwd |
| line moved off the public (no ratio test) | New York Giants @ Indianapolis Colts | spread | home | FanDuel | 7 -> 5.5 | — | 5.5 | 18% | 0.94 | 9-32 fit · 10-5-1 fwd |
| line moved off the public (no ratio test) | New York Giants @ Indianapolis Colts | moneyline | home | FanDuel | 265 -> 225 | — | 225 | 5% | 0.8 | 9-32 fit · 10-5-1 fwd |
| line moved off the public (no ratio test) | New York Jets @ Miami Dolphins | total | under | FanDuel | 41.5 -> 40.5 | — | 40.5 | 30% | 0.83 | 9-32 fit · 10-5-1 fwd |
| line moved off the public (no ratio test) | Seattle Seahawks @ San Francisco 49ers | spread | away | FanDuel | 2 -> -1.5 | — | -1.5 | 32% | 1.19 | 9-32 fit · 10-5-1 fwd |
| line moved off the public (no ratio test) | Seattle Seahawks @ San Francisco 49ers | total | under | FanDuel | 46.5 -> 42.5 | — | 42.5 | 21% | 1.14 | 9-32 fit · 10-5-1 fwd |

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
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | spread | home **SPLIT** | +66.1 | 4-3 | -9.5 (-120) | -10 | 0.5 | -10.5 ($30,000) | +1 | home 90% | 90% / 90% | 12985 | follow_move->away (16-21 fit · 6-9-1 fwd); rlm->away (1-11 fit · 3-2-1 fwd); rlm_quiet->away (1-9 fit · 3-2-1 fwd); money_level->home (25-17 fit · 3-12-1 fwd); money_moving->home (10-21 fit · 7-9-1 fwd); pin_value->home (16-3 fit · 2-4 fwd); pin_move->home (8-10 fit · 3-7 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | moneyline | away **SPLIT** | +36.8 | 3-3 | -255 (-255) | -205 | 4.5 | -237 ($10,000) |  |  | 88% / 84% | 8189 | follow_move->away (17-18 fit · 6-8 fwd); money_level->away (35-7 fit · 10-7 fwd); sharp_gap->home (21-19 fit · 4-12 fwd); money_moving->home (14-19 fit · 8-8 fwd); consensus_gap->home (13-30 fit · 6-11 fwd); pin_move->away (15-11 fit · 5-8 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | moneyline | home | +22.4 | 2-1 | -330 (-330) | -310 | 1.1 | -319 ($10,000) |  |  | 97% / 97% | 14378 | follow_move->home (17-18 fit · 6-8 fwd); money_level->home (35-7 fit · 10-7 fwd); consensus_gap->away (13-30 fit · 6-11 fwd) |

## B  weighted ROI +10% to +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | spread | home | +13.5 | 3-1 | 7 (-115) | 7 |  | 6.5 ($20,000) | +0.5 |  | 16% / 16% | 10895 | money_level->away (25-17 fit · 3-12-1 fwd); consensus_gap->home (5-3 fit · 0-2-1 fwd); pin_value->home (16-3 fit · 2-4 fwd); pin_move->home (8-10 fit · 3-7 fwd) |

## C  weighted ROI 0 to +10%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | New York Giants @ Indianapolis Colts | total | over **SPLIT** | +1.2 | 2-2 | 42.5 (-100) | 42.5 |  | 42 ($5,000) | +0.5 |  | 75% / 74% | 13182 | money_level->over (23-19 fit · 8-9 fwd); sharp_gap->under (21-22 fit · 8-7 fwd); money_moving->over (15-18 fit · 8-8 fwd); pin_value->under (12-11 fit · 5-4 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | spread | home | +8.4 | 1-0 | -6.5 (-110) | -6.5 |  | -6.5 ($20,000) |  |  | 60% / 60% | 12026 | money_level->home (25-17 fit · 3-12-1 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | total | over | +7.7 | 4-1 | 47.5 (-105) | 46.5 | 1 | 47.5 ($5,000) |  |  | 63% / 68% | 12026 | money_delta->under (4-7 fit · 2-4 fwd); follow_move->over (10-9 fit · 12-2 fwd); money_level->over (23-19 fit · 8-9 fwd); sharp_gap->over (21-22 fit · 8-7 fwd); pin_move->over (14-13 fit · 15-2 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | total | over | +4.9 | 2-1 | 41.5 (-110) | 41.5 |  | 41.5 ($5,000) |  |  | 74% / 74% | 10895 | money_delta->under (4-7 fit · 2-4 fwd); money_level->over (23-19 fit · 8-9 fwd); money_moving->over (15-18 fit · 8-8 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | tt_home | over | +4.6 | 1-0 | 30.5 (-128) | 30.5 |  | 31.5 ($2,000) | -1 |  | 0% / 0% | 12854 | pin_value->over (17-12 fit · 4-6 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | tt_away | under | +2.3 | 1-0 | 16.5 (-102) | 17.5 | 1 | 16.5 ($2,000) |  |  | 0% / 0% | 14378 | follow_move->under (9-7 fit · 6-2 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | tt_away | under | +2 | 1-1 | 22.5 (+102) | 23.5 | 1 | 23.5 ($2,000) | +1 |  | 0% / 0% | 8189 | follow_move->under (9-7 fit · 6-2 fwd); pin_value->over (14-12 fit · 2-8 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | tt_away | over | +2 | 1-1 | 20.5 (-102) | 19.5 | 1 | 19.5 ($2,000) | +1 |  | 0% / 0% | 12026 | follow_move->over (9-7 fit · 6-2 fwd); pin_value->under (14-12 fit · 2-8 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | tt_away | under | +2 | 1-1 | 23.5 (-106) | 24.5 | 1 | 24.5 ($2,000) | +1 |  | 0% / 0% | 13182 | follow_move->under (9-7 fit · 6-2 fwd); pin_value->over (14-12 fit · 2-8 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | tt_away | over | +2 | 1-1 | 19.5 (-106) | 17.5 | 2 | 17.5 ($2,000) | +2 |  | 0% / 0% | 9718 | follow_move->over (9-7 fit · 6-2 fwd); pin_value->under (14-12 fit · 2-8 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | tt_away | under | +2 | 1-1 | 16.5 (-102) | 17.5 | 1 | 17.5 ($2,000) | +1 |  | 0% / 0% | 13030 | follow_move->under (9-7 fit · 6-2 fwd); pin_value->over (14-12 fit · 2-8 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | tt_away | over | +0.3 | 1-0 | 19.5 (-111) | 19.5 |  | 20.5 ($2,000) | -1 |  | 0% / 0% | 12985 | pin_value->over (14-12 fit · 2-8 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | tt_away | under | +0.3 | 1-0 | 16.5 (-102) | 16.5 |  | 15.5 ($2,000) | -1 |  | 0% / 0% | 12854 | pin_value->under (14-12 fit · 2-8 fwd) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | moneyline | away **SPLIT** | -5.6 | 4-3 | -154 (-154) | -104 | 9.4 | -154 ($5,000) |  |  | 72% / 58% | 9718 | money_delta->home (4-5 fit · 1-2 fwd); follow_move->away (17-18 fit · 6-8 fwd); money_level->away (35-7 fit · 10-7 fwd); sharp_gap->home (21-19 fit · 4-12 fwd); money_moving->home (14-19 fit · 8-8 fwd); consensus_gap->away (13-30 fit · 6-11 fwd); pin_move->away (15-11 fit · 5-8 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | total | under **SPLIT** | -8.8 | 5-2 | 39.5 (-110) | 41.5 | 2 | 39.5 ($5,000) |  | over 79% | 21% / 24% | 13030 | follow_move->under (10-9 fit · 12-2 fwd); rlm->under (4-5 fit · 6-1 fwd); rlm_quiet->under (3-4 fit · 6-1 fwd); money_level->over (23-19 fit · 8-9 fwd); sharp_gap->under (21-22 fit · 8-7 fwd); money_moving->over (15-18 fit · 8-8 fwd); pin_move->under (14-13 fit · 15-2 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | total | under **SPLIT** | -10.3 | 6-3 | 40.5 (-120) | 41.5 | 1 | 40 ($5,000) | -0.5 | over 70% | 30% / 25% | 8189 | money_delta->under (4-7 fit · 2-4 fwd); follow_move->under (10-9 fit · 12-2 fwd); rlm->under (4-5 fit · 6-1 fwd); rlm_quiet->under (3-4 fit · 6-1 fwd); money_level->over (23-19 fit · 8-9 fwd); sharp_gap->over (21-22 fit · 8-7 fwd); money_moving->over (15-18 fit · 8-8 fwd); pin_value->under (12-11 fit · 5-4 fwd); pin_move->under (14-13 fit · 15-2 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | total | under **SPLIT** | -23.1 | 6-3 | 48.5 (-108) | 50.5 | 2 | 49 ($5,000) | +0.5 | over 60% | 40% / 37% | 12985 | money_delta->under (4-7 fit · 2-4 fwd); follow_move->under (10-9 fit · 12-2 fwd); rlm->under (4-5 fit · 6-1 fwd); rlm_quiet->under (3-4 fit · 6-1 fwd); money_level->over (23-19 fit · 8-9 fwd); sharp_gap->over (21-22 fit · 8-7 fwd); money_moving->under (15-18 fit · 8-8 fwd); pin_value->over (12-11 fit · 5-4 fwd); pin_move->under (14-13 fit · 15-2 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | total | under **SPLIT** | -24 | 3-3 | 48.5 (-115) | 47.5 | 1 | 48.5 ($5,000) **retraced +1.5** |  |  | 28% / 31% | 12854 | money_delta->under (4-7 fit · 2-4 fwd); follow_move->over (10-9 fit · 12-2 fwd); money_level->over (23-19 fit · 8-9 fwd); sharp_gap->under (21-22 fit · 8-7 fwd); money_moving->under (15-18 fit · 8-8 fwd); pin_move->over (14-13 fit · 15-2 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | spread | away **SPLIT** | -31.2 | 3-2 | 14.5 (-120) | 14 | 0.5 | 14.5 ($10,000) |  |  | 13% / 15% | 12854 | follow_move->home (16-21 fit · 6-9-1 fwd); money_level->home (25-17 fit · 3-12-1 fwd); sharp_gap->away (17-25 fit · 8-8-1 fwd); money_moving->away (10-21 fit · 7-9-1 fwd); consensus_gap->away (5-3 fit · 0-2-1 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | moneyline | away **SPLIT** | -35 | 4-3 | 134 (+134) | 126 | 1.6 | 145 ($20,000) |  |  | 33% / 42% | 9496 | money_delta->away (4-5 fit · 1-2 fwd); follow_move->home (17-18 fit · 6-8 fwd); money_level->home (35-7 fit · 10-7 fwd); sharp_gap->away (21-19 fit · 4-12 fwd); money_moving->away (14-19 fit · 8-8 fwd); consensus_gap->away (13-30 fit · 6-11 fwd); pin_move->home (15-11 fit · 5-8 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | moneyline | away **SPLIT** | -38.8 | 9-2 | -116 (-116) | 144 | 12.7 | -113 ($10,000) |  | home 88% | 12% / 27% | 17094 | money_delta->away (4-5 fit · 1-2 fwd); follow_move->away (17-18 fit · 6-8 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 10-7 fwd); sharp_gap->away (21-19 fit · 4-12 fwd); money_moving->away (14-19 fit · 8-8 fwd); consensus_gap->home (13-30 fit · 6-11 fwd); pin_move->away (15-11 fit · 5-8 fwd); pin_rlm->away (2-7 fit · 0-3 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | spread | home **SPLIT** | -39.2 | 4-3 | 5.5 (-105) | 7 | 1.5 | 5.5 ($30,000) |  | away 82% | 18% / 17% | 13182 | follow_move->home (16-21 fit · 6-9-1 fwd); rlm->home (1-11 fit · 3-2-1 fwd); rlm_quiet->home (1-9 fit · 3-2-1 fwd); money_level->away (25-17 fit · 3-12-1 fwd); sharp_gap->away (17-25 fit · 8-8-1 fwd); money_moving->away (10-21 fit · 7-9-1 fwd); pin_move->home (8-10 fit · 3-7 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | spread | away **SPLIT** | -42.6 | 5-2 | -5.5 (-110) | -4 | 1.5 | -5 ($20,000) | -0.5 |  | 51% / 55% | 8189 | money_delta->home (3-14 fit · 2-0 fwd); follow_move->away (16-21 fit · 6-9-1 fwd); money_level->away (25-17 fit · 3-12-1 fwd); sharp_gap->away (17-25 fit · 8-8-1 fwd); money_moving->away (10-21 fit · 7-9-1 fwd); pin_value->home (16-3 fit · 2-4 fwd); pin_move->away (8-10 fit · 3-7 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | spread | away **SPLIT** | -43.3 | 4-3 | -3 (-105) | 3.5 | 6.5 | -2.5 ($10,000) | -0.5 |  | 59% / 58% | 9718 | follow_move->away (16-21 fit · 6-9-1 fwd); money_level->away (25-17 fit · 3-12-1 fwd); sharp_gap->home (17-25 fit · 8-8-1 fwd); money_moving->away (10-21 fit · 7-9-1 fwd); consensus_gap->home (5-3 fit · 0-2-1 fwd); pin_value->home (16-3 fit · 2-4 fwd); pin_move->away (8-10 fit · 3-7 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | moneyline | away **SPLIT** | -64.8 | 4-3 | 460 (+460) | 430 | 0.6 | 413 ($10,000) |  |  | 2% / 3% | 12985 | follow_move->home (17-18 fit · 6-8 fwd); money_level->home (35-7 fit · 10-7 fwd); sharp_gap->away (21-19 fit · 4-12 fwd); money_moving->home (14-19 fit · 8-8 fwd); consensus_gap->away (13-30 fit · 6-11 fwd); pin_value->away (2-7 fit · 2-4 fwd); pin_rlm->away (2-7 fit · 0-3 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | moneyline | home **SPLIT** | -83.3 | 5-3 | 225 (+225) | 265 | 3.4 | 218 ($10,000) |  | away 95% | 5% / 4% | 13182 | follow_move->home (17-18 fit · 6-8 fwd); rlm->home (4-16 fit · 1-2 fwd); rlm_quiet->home (2-15 fit · 1-2 fwd); money_level->away (35-7 fit · 10-7 fwd); sharp_gap->away (21-19 fit · 4-12 fwd); money_moving->away (14-19 fit · 8-8 fwd); consensus_gap->home (13-30 fit · 6-11 fwd); pin_move->home (15-11 fit · 5-8 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | moneyline | away **SPLIT** | -83.5 | 4-2 | 240 (+240) | 265 | 2.1 | 251 ($10,000) |  | home 93% | 7% / 7% | 12026 | follow_move->away (17-18 fit · 6-8 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 10-7 fwd); money_moving->home (14-19 fit · 8-8 fwd); consensus_gap->away (13-30 fit · 6-11 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | moneyline | away **SPLIT** | -96 | 6-2 | 190 (+190) | 198 | 0.9 | 195 ($10,000) |  | home 78% | 22% / 42% | 13030 | follow_move->away (17-18 fit · 6-8 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 10-7 fwd); sharp_gap->away (21-19 fit · 4-12 fwd); money_moving->home (14-19 fit · 8-8 fwd); consensus_gap->away (13-30 fit · 6-11 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | spread | home **SPLIT** | -115.4 | 6-2 | -3 (-104) | -2.5 | 0.5 | -3 ($30,000) |  | away 60% | 40% / 43% | 9496 | follow_move->home (16-21 fit · 6-9-1 fwd); rlm->home (1-11 fit · 3-2-1 fwd); rlm_quiet->home (1-9 fit · 3-2-1 fwd); money_level->away (25-17 fit · 3-12-1 fwd); sharp_gap->home (17-25 fit · 8-8-1 fwd); money_moving->home (10-21 fit · 7-9-1 fwd); consensus_gap->away (5-3 fit · 0-2-1 fwd); pin_move->home (8-10 fit · 3-7 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | spread | away **SPLIT** | -136.9 | 6-2 | -1.5 (-105) | 2 | 3.5 | -1 ($20,000) | -0.5 | home 68% | 32% / 38% | 17094 | follow_move->away (16-21 fit · 6-9-1 fwd); rlm->away (1-11 fit · 3-2-1 fwd); rlm_quiet->away (1-9 fit · 3-2-1 fwd); money_level->home (25-17 fit · 3-12-1 fwd); sharp_gap->away (17-25 fit · 8-8-1 fwd); money_moving->away (10-21 fit · 7-9-1 fwd); pin_value->home (16-3 fit · 2-4 fwd); pin_move->away (8-10 fit · 3-7 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | tt_home | over | -4.6 | 1-0 | 27.5 (-100) | 26.5 | 1 | 27.5 ($2,000) |  |  | 0% / 0% | 12026 | follow_move->over (9-10 fit · 5-4 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | tt_home | over | -4.6 | 1-0 | 23.5 (-108) | 22.5 | 1 | 23.5 ($2,000) |  |  | 0% / 0% | 9496 | follow_move->over (9-10 fit · 5-4 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | total | over | -8.7 | 3-0 | 43.5 (-115) | 43.5 |  | 43.5 ($10,000) |  |  | 81% / 86% | 9496 | money_level->over (23-19 fit · 8-9 fwd); sharp_gap->over (21-22 fit · 8-7 fwd); money_moving->over (15-18 fit · 8-8 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | tt_home | under | -9.2 | 1-1 | 16.5 (+102) | 18.5 | 2 | 17.5 ($2,000) | +1 |  | 0% / 0% | 8189 | follow_move->under (9-10 fit · 5-4 fwd); pin_value->over (17-12 fit · 4-6 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | tt_home | over | -9.2 | 1-1 | 17.5 (-104) | 16.5 | 1 | 16.5 ($2,000) | +1 |  | 0% / 0% | 13182 | follow_move->over (9-10 fit · 5-4 fwd); pin_value->under (17-12 fit · 4-6 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | tt_home | under | -9.2 | 1-1 | 16.5 (-113) | 17.5 | 1 | 17.5 ($2,000) | +1 |  | 0% / 0% | 9718 | follow_move->under (9-10 fit · 5-4 fwd); pin_value->over (17-12 fit · 4-6 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | tt_home | under | -9.2 | 1-1 | 20.5 (-111) | 24.5 | 4 | 24.5 ($2,000) | +4 |  | 0% / 0% | 17094 | follow_move->under (9-10 fit · 5-4 fwd); pin_value->over (17-12 fit · 4-6 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | tt_home | under | -9.2 | 1-1 | 22.5 (-113) | 23.5 | 1 | 23.5 ($2,000) | +1 |  | 0% / 0% | 13030 | follow_move->under (9-10 fit · 5-4 fwd); pin_value->over (17-12 fit · 4-6 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | total | under | -15.1 | 2-1 | 35.5 (-108) | 35.5 |  | 35.5 ($3,000) |  |  | 15% / 16% | 9718 | money_level->over (23-19 fit · 8-9 fwd); sharp_gap->under (21-22 fit · 8-7 fwd); money_moving->under (15-18 fit · 8-8 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | total | under | -15.7 | 4-1 | 41.5 (-110) | 42.5 | 1 | 41.5 ($5,000) |  | over 66% | 34% / 35% | 14378 | follow_move->under (10-9 fit · 12-2 fwd); rlm->under (4-5 fit · 6-1 fwd); rlm_quiet->under (3-4 fit · 6-1 fwd); money_level->over (23-19 fit · 8-9 fwd); sharp_gap->under (21-22 fit · 8-7 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | total | under | -34.1 | 8-1 | 42.5 (-110) | 46.5 | 4 | 42 ($5,000) | -0.5 | over 79% | 21% / 24% | 17094 | money_delta->under (4-7 fit · 2-4 fwd); follow_move->under (10-9 fit · 12-2 fwd); rlm->under (4-5 fit · 6-1 fwd); rlm_quiet->under (3-4 fit · 6-1 fwd); money_level->over (23-19 fit · 8-9 fwd); sharp_gap->under (21-22 fit · 8-7 fwd); money_moving->under (15-18 fit · 8-8 fwd); pin_value->under (12-11 fit · 5-4 fwd); pin_move->under (14-13 fit · 15-2 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | spread | away | -38.2 | 4-0 | 4.5 (-105) | 5 | 0.5 | 4.5 ($20,000) |  |  | 70% / 71% | 13030 | follow_move->away (16-21 fit · 6-9-1 fwd); money_level->away (25-17 fit · 3-12-1 fwd); sharp_gap->away (17-25 fit · 8-8-1 fwd); money_moving->away (10-21 fit · 7-9-1 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | spread | away | -42.1 | 4-1 | 7 (-115) | 7 |  | 7 ($20,000) |  |  | 20% / 20% | 14378 | money_delta->away (3-14 fit · 2-0 fwd); money_level->home (25-17 fit · 3-12-1 fwd); money_moving->away (10-21 fit · 7-9-1 fwd); consensus_gap->away (5-3 fit · 0-2-1 fwd); book_lag->away (4-0 fit · 0-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | moneyline | away | -77.1 | 8-1 | 700 (+700) | 750 | 0.6 | 675 ($10,000) |  | home 98% | 2% / 3% | 12854 | follow_move->away (17-18 fit · 6-8 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 10-7 fwd); sharp_gap->away (21-19 fit · 4-12 fwd); money_moving->away (14-19 fit · 8-8 fwd); consensus_gap->away (13-30 fit · 6-11 fwd); pin_rlm->away (2-7 fit · 0-3 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | moneyline | home | -97.7 | 9-1 | 285 (+285) | 300 | 1 | 266 ($10,000) |  | away 97% | 3% / 7% | 10895 | follow_move->home (17-18 fit · 6-8 fwd); rlm->home (4-16 fit · 1-2 fwd); rlm_ratio->home (3-7 fit · 0-1 fwd); rlm_quiet->home (2-15 fit · 1-2 fwd); money_level->away (35-7 fit · 10-7 fwd); sharp_gap->home (21-19 fit · 4-12 fwd); consensus_gap->home (13-30 fit · 6-11 fwd); pin_value->home (2-7 fit · 2-4 fwd); pin_move->home (15-11 fit · 5-8 fwd); pin_rlm->home (2-7 fit · 0-3 fwd) |

