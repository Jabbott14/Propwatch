# NFL board

Generated 2026-11-21 19:42 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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
| PINNACLE moved vs public | Arizona Cardinals @ Kansas City Chiefs | moneyline | away | Pinnacle | 848 -> 832 | — | 900 | 1% | 10.0 | 5-10 fit · 0-0 fwd |
| PINNACLE moved vs public | Miami Dolphins @ Buffalo Bills | moneyline | away | Pinnacle | 889 -> 879 | — | 900 | 1% | 8.0 | 5-10 fit · 0-0 fwd |
| PINNACLE moved vs public | Minnesota Vikings @ San Francisco 49ers | total | over | Pinnacle | 45.5 -> 46 | **+1** | 46.5 | 11% | 1.36 | 5-10 fit · 0-0 fwd |
| PINNACLE moved vs public | Tennessee Titans @ Dallas Cowboys | moneyline | away | Pinnacle | 307 -> 297 | — | 330 | 4% | 1.5 | 5-10 fit · 0-0 fwd |
| FanDuel moved vs public | Miami Dolphins @ Buffalo Bills | moneyline | away | FanDuel | 980 -> 900 | — | 900 | 1% | 8.0 | 6-14 fit · 0-0 fwd |
| FanDuel moved vs public | Tennessee Titans @ Dallas Cowboys | moneyline | away | FanDuel | 350 -> 330 | — | 330 | 4% | 1.5 | 6-14 fit · 0-0 fwd |
| line moved off the public (no ratio test) | Arizona Cardinals @ Kansas City Chiefs | spread | home | FanDuel | -15 -> -16.5 | — | -16.5 | 35% | 0.97 | 9-32 fit · 0-0 fwd |
| line moved off the public (no ratio test) | Arizona Cardinals @ Kansas City Chiefs | total | under | FanDuel | 41.5 -> 40.5 | — | 40.5 | 16% | 1.06 | 9-32 fit · 0-0 fwd |
| line moved off the public (no ratio test) | Jacksonville Jaguars @ New York Giants | spread | home | FanDuel | 6.5 -> 5.5 | — | 5.5 | 17% | 1.06 | 9-32 fit · 0-0 fwd |
| line moved off the public (no ratio test) | Miami Dolphins @ Buffalo Bills | total | under | FanDuel | 45.5 -> 44.5 | — | 44.5 | 29% | 0.97 | 9-32 fit · 0-0 fwd |
| line moved off the public (no ratio test) | Pittsburgh Steelers @ Philadelphia Eagles | total | under | FanDuel | 38.5 -> 37.5 | — | 37.5 | 27% | 1.11 | 9-32 fit · 0-0 fwd |
| line moved off the public (no ratio test) | Pittsburgh Steelers @ Philadelphia Eagles | moneyline | home | FanDuel | 176 -> 156 | **+0.8** | 156 | 11% | 0.64 | 9-32 fit · 0-0 fwd |
| line moved off the public (no ratio test) | Tampa Bay Buccaneers @ Detroit Lions | moneyline | away | FanDuel | 215 -> 190 | — | 190 | 4% | 0.5 | 9-32 fit · 0-0 fwd |

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
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | spread | home **SPLIT** | +90.2 | 5-2 | -9.5 (-120) | -9.5 |  | -10.5 ($30,000) | +1 |  | 61% / 61% | 15216 | money_delta->away (3-14 fit · 0-0 fwd); money_level->home (25-17 fit · 0-0 fwd); money_moving->away (10-21 fit · 0-0 fwd); consensus_gap->home (5-3 fit · 0-0 fwd); book_lag->home (4-0 fit · 0-0 fwd); pin_value->home (16-3 fit · 0-0 fwd); pin_move->home (8-10 fit · 0-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | spread | away **SPLIT** | +83.4 | 5-3 | -5.5 (-120) | -4 | 1.5 | -6.5 ($10,000) | +1 |  | 80% / 67% | 13732 | money_delta->home (3-14 fit · 0-0 fwd); follow_move->away (16-21 fit · 0-0 fwd); money_level->away (25-17 fit · 0-0 fwd); sharp_gap->home (17-25 fit · 0-0 fwd); money_moving->home (10-21 fit · 0-0 fwd); consensus_gap->away (5-3 fit · 0-0 fwd); pin_value->away (16-3 fit · 0-0 fwd); pin_move->away (8-10 fit · 0-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | moneyline | home **SPLIT** | +24.9 | 4-3 | -620 (-620) | -550 | 1.5 | -557 ($7,500) |  |  | 97% / 93% | 15216 | follow_move->home (17-18 fit · 0-0 fwd); money_level->home (35-7 fit · 0-0 fwd); sharp_gap->away (21-19 fit · 0-0 fwd); money_moving->home (14-19 fit · 0-0 fwd); consensus_gap->away (13-30 fit · 0-0 fwd); pin_value->away (2-7 fit · 0-0 fwd); pin_move->home (15-11 fit · 0-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | total | over **SPLIT** | +22.9 | 4-3 | 53.5 (-115) | 52.5 | 1 | 54 ($3,000) | -0.5 |  | 63% / 62% | 13732 | money_delta->under (4-7 fit · 0-0 fwd); follow_move->over (10-9 fit · 0-0 fwd); money_level->over (23-19 fit · 0-0 fwd); sharp_gap->under (21-22 fit · 0-0 fwd); money_moving->under (15-18 fit · 0-0 fwd); pin_value->over (12-11 fit · 0-0 fwd); pin_move->over (14-13 fit · 0-0 fwd) |

## B  weighted ROI +10% to +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | New Orleans Saints @ Chicago Bears | moneyline | home **SPLIT** | +16.3 | 5-2 | -720 (-720) | -670 | 0.8 | -583 ($10,000) |  |  | 98% / 99% | 22370 | follow_move->home (17-18 fit · 0-0 fwd); money_level->home (35-7 fit · 0-0 fwd); sharp_gap->home (21-19 fit · 0-0 fwd); money_moving->home (14-19 fit · 0-0 fwd); consensus_gap->away (13-30 fit · 0-0 fwd); pin_value->away (2-7 fit · 0-0 fwd); pin_move->home (15-11 fit · 0-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | spread | home **SPLIT** | +11.9 | 4-2 | -11.5 (-110) | -9.5 | 2 | -11.5 ($30,000) |  |  | 62% / 56% | 22370 | money_delta->away (3-14 fit · 0-0 fwd); follow_move->home (16-21 fit · 0-0 fwd); money_level->home (25-17 fit · 0-0 fwd); sharp_gap->away (17-25 fit · 0-0 fwd); money_moving->home (10-21 fit · 0-0 fwd); pin_move->home (8-10 fit · 0-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | spread | home | +19.8 | 2-1 | -2.5 (-116) | -2 | 0.5 | -2.5 ($30,000) |  |  | 61% / 61% | 13687 | follow_move->home (16-21 fit · 0-0 fwd); money_level->home (25-17 fit · 0-0 fwd); money_moving->away (10-21 fit · 0-0 fwd) |

## C  weighted ROI 0 to +10%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 16:05 | New York Jets @ Los Angeles Chargers | moneyline | home **SPLIT** | +8.4 | 4-2 | -180 (-180) | -158 | 3 | -171 ($10,000) **retraced +1.4** |  |  | 76% / 71% | 10294 | follow_move->home (17-18 fit · 0-0 fwd); money_level->home (35-7 fit · 0-0 fwd); sharp_gap->away (21-19 fit · 0-0 fwd); money_moving->home (14-19 fit · 0-0 fwd); consensus_gap->away (13-30 fit · 0-0 fwd); pin_move->home (15-11 fit · 0-0 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | moneyline | home **SPLIT** | +8.4 | 4-2 | -168 (-168) | -164 | 0.6 | -176 ($10,000) |  |  | 84% / 74% | 18140 | follow_move->home (17-18 fit · 0-0 fwd); money_level->home (35-7 fit · 0-0 fwd); sharp_gap->away (21-19 fit · 0-0 fwd); money_moving->home (14-19 fit · 0-0 fwd); consensus_gap->away (13-30 fit · 0-0 fwd); pin_move->home (15-11 fit · 0-0 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | tt_home | over | +4.6 | 1-0 | 30.5 (-115) | 30.5 |  | 31.5 ($2,000) | -1 |  | 0% / 0% | 17670 | pin_value->over (17-12 fit · 0-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | tt_home | under | +4.6 | 1-0 | 30.5 (-113) | 30.5 |  | 29.5 ($2,000) | -1 |  | 0% / 0% | 22370 | pin_value->under (17-12 fit · 0-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | moneyline | home | +3.9 | 4-1 | -148 (-148) | -132 | 2.8 | -142 ($10,000) |  |  | 82% / 83% | 13687 | follow_move->home (17-18 fit · 0-0 fwd); money_level->home (35-7 fit · 0-0 fwd); sharp_gap->home (21-19 fit · 0-0 fwd); money_moving->home (14-19 fit · 0-0 fwd); consensus_gap->away (13-30 fit · 0-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | moneyline | away | +3.9 | 4-1 | -255 (-255) | -245 | 1.1 | -259 ($10,000) |  |  | 97% / 99% | 19482 | follow_move->away (17-18 fit · 0-0 fwd); money_level->away (35-7 fit · 0-0 fwd); sharp_gap->away (21-19 fit · 0-0 fwd); money_moving->away (14-19 fit · 0-0 fwd); consensus_gap->home (13-30 fit · 0-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | tt_away | over | +2 | 1-1 | 23.5 (-102) | 22.5 | 1 | 22.5 ($2,000) | +1 |  | 0% / 0% | 20447 | follow_move->over (9-7 fit · 0-0 fwd); pin_value->under (14-12 fit · 0-0 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | tt_away | under | +2 | 1-1 | 13.5 (-100) | 14.5 | 1 | 14.5 ($2,000) | +1 |  | 0% / 0% | 17670 | follow_move->under (9-7 fit · 0-0 fwd); pin_value->over (14-12 fit · 0-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | tt_away | under | +2 | 1-1 | 17.5 (-113) | 18.5 | 1 | 19.5 ($2,000) | +2 |  | 0% / 0% | 22370 | follow_move->under (9-7 fit · 0-0 fwd); pin_value->over (14-12 fit · 0-0 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | tt_away | under | +2 | 1-1 | 20.5 (-122) | 21.5 | 1 | 21.5 ($2,000) | +1 |  | 0% / 0% | 12889 | follow_move->under (9-7 fit · 0-0 fwd); pin_value->over (14-12 fit · 0-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | tt_away | under | +0.3 | 1-0 | 19.5 (-106) | 19.5 |  | 18.5 ($2,000) | -1 |  | 0% / 0% | 10294 | pin_value->under (14-12 fit · 0-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | tt_away | under | +0.3 | 1-0 | 30.5 (-113) | 30.5 |  | 29.5 ($1,000) | -1 |  | 0% / 0% | 13732 | pin_value->under (14-12 fit · 0-0 fwd) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | total | under **SPLIT** | -0 | 4-3 | 44.5 (-105) | 45.5 | 1 | 44.5 ($3,000) |  | over 71% | 29% / 28% | 17670 | follow_move->under (10-9 fit · 0-0 fwd); rlm->under (4-5 fit · 0-0 fwd); rlm_quiet->under (3-4 fit · 0-0 fwd); money_level->over (23-19 fit · 0-0 fwd); sharp_gap->over (21-22 fit · 0-0 fwd); money_moving->over (15-18 fit · 0-0 fwd); pin_move->under (14-13 fit · 0-0 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | total | over **SPLIT** | -1 | 5-2 | 46.5 (-116) | 46.5 |  | 46 ($3,000) **retraced +1** | +0.5 |  | 11% / 15% | 18140 | pre_move->over (1-2 fit · 0-0 fwd); money_level->under (23-19 fit · 0-0 fwd); sharp_gap->over (21-22 fit · 0-0 fwd); money_moving->over (15-18 fit · 0-0 fwd); pin_value->under (12-11 fit · 0-0 fwd); pin_move->over (14-13 fit · 0-0 fwd); pin_rlm->over (3-1 fit · 0-0 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | total | under **SPLIT** | -7.1 | 4-3 | 40.5 (-110) | 41.5 | 1 | 41 ($3,000) | +0.5 | over 84% | 16% / 17% | 16443 | follow_move->under (10-9 fit · 0-0 fwd); rlm->under (4-5 fit · 0-0 fwd); rlm_quiet->under (3-4 fit · 0-0 fwd); money_level->over (23-19 fit · 0-0 fwd); sharp_gap->under (21-22 fit · 0-0 fwd); money_moving->over (15-18 fit · 0-0 fwd); pin_value->over (12-11 fit · 0-0 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | total | under **SPLIT** | -8 | 3-2 | 46.5 (-116) | 46.5 |  | 46 ($3,000) **retraced +2** | -0.5 |  | 19% / 14% | 20740 | money_level->over (23-19 fit · 0-0 fwd); sharp_gap->over (21-22 fit · 0-0 fwd); money_moving->under (15-18 fit · 0-0 fwd); pin_value->under (12-11 fit · 0-0 fwd); pin_move->under (14-13 fit · 0-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | total | under **SPLIT** | -9.3 | 2-2 | 43.5 (-110) | 43.5 |  | 43.5 ($3,000) |  |  | 35% / 36% | 13687 | money_delta->under (4-7 fit · 0-0 fwd); money_level->over (23-19 fit · 0-0 fwd); sharp_gap->under (21-22 fit · 0-0 fwd); money_moving->over (15-18 fit · 0-0 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | spread | away **SPLIT** | -19.9 | 3-2 | 16.5 (-110) | 17 | 0.5 | 17 ($30,000) | -0.5 |  | 50% / 55% | 17670 | follow_move->away (16-21 fit · 0-0 fwd); money_level->away (25-17 fit · 0-0 fwd); sharp_gap->away (17-25 fit · 0-0 fwd); money_moving->home (10-21 fit · 0-0 fwd); pin_value->home (16-3 fit · 0-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | spread | home **SPLIT** | -38.7 | 3-2 | -3 (-116) | -3 |  | -3 ($30,000) |  |  | 43% / 40% | 10294 | money_delta->home (3-14 fit · 0-0 fwd); money_level->away (25-17 fit · 0-0 fwd); sharp_gap->away (17-25 fit · 0-0 fwd); money_moving->home (10-21 fit · 0-0 fwd); consensus_gap->home (5-3 fit · 0-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | moneyline | home **SPLIT** | -49 | 4-2 | 235 (+235) | 235 |  | 240 ($10,000) |  |  | 2% / 3% | 13732 | pre_move->home (1-3 fit · 0-0 fwd); money_level->away (35-7 fit · 0-0 fwd); sharp_gap->home (21-19 fit · 0-0 fwd); money_moving->home (14-19 fit · 0-0 fwd); consensus_gap->home (13-30 fit · 0-0 fwd); pin_move->away (15-11 fit · 0-0 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | moneyline | away **SPLIT** | -64.8 | 4-3 | 900 (+900) | 870 | 0.4 | 832 ($5,000) |  |  | 1% / 10% | 16443 | follow_move->home (17-18 fit · 0-0 fwd); money_level->home (35-7 fit · 0-0 fwd); sharp_gap->away (21-19 fit · 0-0 fwd); money_moving->home (14-19 fit · 0-0 fwd); consensus_gap->away (13-30 fit · 0-0 fwd); pin_value->away (2-7 fit · 0-0 fwd); pin_rlm->away (2-7 fit · 0-0 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | moneyline | home **SPLIT** | -66.8 | 5-4 | 156 (+156) | 176 | 2.8 | 178 ($10,000) |  | away 89% | 11% / 7% | 12889 | follow_move->home (17-18 fit · 0-0 fwd); rlm->home (4-16 fit · 0-0 fwd); rlm_quiet->home (2-15 fit · 0-0 fwd); money_level->away (35-7 fit · 0-0 fwd); sharp_gap->away (21-19 fit · 0-0 fwd); money_moving->away (14-19 fit · 0-0 fwd); consensus_gap->home (13-30 fit · 0-0 fwd); pin_value->away (2-7 fit · 0-0 fwd); pin_move->home (15-11 fit · 0-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | spread | away **SPLIT** | -77.2 | 3-3 | 7.5 (-105) | 8 | 0.5 | 8 ($30,000) | -0.5 |  | 47% / 45% | 20447 | money_delta->away (3-14 fit · 0-0 fwd); follow_move->away (16-21 fit · 0-0 fwd); money_level->home (25-17 fit · 0-0 fwd); sharp_gap->home (17-25 fit · 0-0 fwd); money_moving->away (10-21 fit · 0-0 fwd); pin_value->home (16-3 fit · 0-0 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | moneyline | away **SPLIT** | -83.3 | 5-3 | 190 (+190) | 215 | 2.5 | 193 ($10,000) |  | home 96% | 4% / 2% | 20740 | follow_move->away (17-18 fit · 0-0 fwd); rlm->away (4-16 fit · 0-0 fwd); rlm_quiet->away (2-15 fit · 0-0 fwd); money_level->home (35-7 fit · 0-0 fwd); sharp_gap->home (21-19 fit · 0-0 fwd); money_moving->home (14-19 fit · 0-0 fwd); consensus_gap->away (13-30 fit · 0-0 fwd); pin_move->away (15-11 fit · 0-0 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | spread | home **SPLIT** | -85.8 | 5-3 | -16.5 (-105) | -15 | 1.5 | -16.5 ($30,000) |  | away 65% | 35% / 34% | 16443 | follow_move->home (16-21 fit · 0-0 fwd); rlm->home (1-11 fit · 0-0 fwd); rlm_quiet->home (1-9 fit · 0-0 fwd); money_level->away (25-17 fit · 0-0 fwd); sharp_gap->away (17-25 fit · 0-0 fwd); money_moving->home (10-21 fit · 0-0 fwd); consensus_gap->away (5-3 fit · 0-0 fwd); pin_move->home (8-10 fit · 0-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | moneyline | away **SPLIT** | -93.6 | 8-2 | 330 (+330) | 350 | 1 | 297 ($10,000) |  | home 96% | 4% / 6% | 20447 | follow_move->away (17-18 fit · 0-0 fwd); rlm->away (4-16 fit · 0-0 fwd); rlm_ratio->away (3-7 fit · 0-0 fwd); rlm_quiet->away (2-15 fit · 0-0 fwd); money_level->home (35-7 fit · 0-0 fwd); sharp_gap->away (21-19 fit · 0-0 fwd); money_moving->home (14-19 fit · 0-0 fwd); consensus_gap->away (13-30 fit · 0-0 fwd); pin_value->away (2-7 fit · 0-0 fwd); pin_rlm->away (2-7 fit · 0-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | spread | home **SPLIT** | -130.5 | 5-2 | 5.5 (-100) | 6.5 | 1 | 6 ($30,000) | -0.5 | away 83% | 17% / 18% | 19482 | follow_move->home (16-21 fit · 0-0 fwd); rlm->home (1-11 fit · 0-0 fwd); rlm_quiet->home (1-9 fit · 0-0 fwd); money_level->away (25-17 fit · 0-0 fwd); sharp_gap->home (17-25 fit · 0-0 fwd); money_moving->home (10-21 fit · 0-0 fwd); pin_value->away (16-3 fit · 0-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | total | over | -0.2 | 4-1 | 41.5 (-120) | 40.5 | 1 | 41.5 ($3,000) |  |  | 57% / 56% | 10294 | follow_move->over (10-9 fit · 0-0 fwd); money_level->over (23-19 fit · 0-0 fwd); sharp_gap->under (21-22 fit · 0-0 fwd); money_moving->over (15-18 fit · 0-0 fwd); pin_move->over (14-13 fit · 0-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | total | over | -1.6 | 4-1 | 40.5 (-110) | 40.5 |  | 41 ($3,000) | -0.5 |  | 78% / 77% | 15216 | money_level->over (23-19 fit · 0-0 fwd); sharp_gap->under (21-22 fit · 0-0 fwd); money_moving->over (15-18 fit · 0-0 fwd); pin_value->over (12-11 fit · 0-0 fwd); pin_move->over (14-13 fit · 0-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | total | over | -4.3 | 2-0 | 46.5 (-100) | 46.5 |  | 46.5 ($3,000) |  |  | 83% / 83% | 19482 | money_level->over (23-19 fit · 0-0 fwd); money_moving->over (15-18 fit · 0-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | tt_home | under | -4.6 | 1-0 | 19.5 (-102) | 20.5 | 1 | 19.5 ($2,000) |  |  | 0% / 0% | 19482 | follow_move->under (9-10 fit · 0-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | total | over | -8.7 | 3-0 | 48.5 (-110) | 48.5 |  | 48.5 ($3,000) |  |  | 75% / 77% | 22370 | money_level->over (23-19 fit · 0-0 fwd); sharp_gap->over (21-22 fit · 0-0 fwd); money_moving->over (15-18 fit · 0-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | tt_home | over | -9.2 | 1-1 | 32.5 (-113) | 31.5 | 1 | 31.5 ($2,000) | +1 |  | 0% / 0% | 20447 | follow_move->over (9-10 fit · 0-0 fwd); pin_value->under (17-12 fit · 0-0 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | tt_home | under | -9.2 | 1-1 | 25.5 (-111) | 26.5 | 1 | 26.5 ($2,000) | +1 |  | 0% / 0% | 20740 | follow_move->under (9-10 fit · 0-0 fwd); pin_value->over (17-12 fit · 0-0 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | tt_home | under | -9.2 | 1-1 | 27.5 (-113) | 28.5 | 1 | 28.5 ($2,000) | +1 |  | 0% / 0% | 16443 | follow_move->under (9-10 fit · 0-0 fwd); pin_value->over (17-12 fit · 0-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | tt_home | over | -9.2 | 1-1 | 23.5 (-100) | 22.5 | 1 | 22.5 ($2,000) | +1 |  | 0% / 0% | 13687 | follow_move->over (9-10 fit · 0-0 fwd); pin_value->under (17-12 fit · 0-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | tt_home | over | -9.2 | 1-1 | 23.5 (-100) | 21.5 | 2 | 21.5 ($2,000) | +2 |  | 0% / 0% | 10294 | follow_move->over (9-10 fit · 0-0 fwd); pin_value->under (17-12 fit · 0-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | tt_home | over | -9.2 | 1-1 | 26.5 (-104) | 25.5 | 1 | 24.5 ($2,000) | +2 |  | 0% / 0% | 15216 | follow_move->over (9-10 fit · 0-0 fwd); pin_value->under (17-12 fit · 0-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | total | over | -10.4 | 5-0 | 54.5 (-120) | 54.5 |  | 55.5 ($3,000) | -1 |  | 69% / 70% | 20447 | money_level->over (23-19 fit · 0-0 fwd); sharp_gap->over (21-22 fit · 0-0 fwd); money_moving->over (15-18 fit · 0-0 fwd); pin_value->over (12-11 fit · 0-0 fwd); pin_move->over (14-13 fit · 0-0 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | total | under | -33 | 7-1 | 37.5 (-110) | 38.5 | 1 | 37.5 ($3,000) |  | over 73% | 27% / 30% | 12889 | money_delta->under (4-7 fit · 0-0 fwd); follow_move->under (10-9 fit · 0-0 fwd); rlm->under (4-5 fit · 0-0 fwd); rlm_quiet->under (3-4 fit · 0-0 fwd); money_level->over (23-19 fit · 0-0 fwd); sharp_gap->under (21-22 fit · 0-0 fwd); money_moving->under (15-18 fit · 0-0 fwd); pin_move->under (14-13 fit · 0-0 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | spread | home | -41.5 | 3-1 | 3.5 (-115) | 4.5 | 1 | 4.5 ($30,000) | -1 |  | 71% / 72% | 12889 | follow_move->home (16-21 fit · 0-0 fwd); money_level->home (25-17 fit · 0-0 fwd); sharp_gap->home (17-25 fit · 0-0 fwd); pin_value->away (16-3 fit · 0-0 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | spread | home | -65.5 | 4-1 | -3.5 (-100) | -3.5 |  | -3 ($30,000) | -0.5 |  | 28% / 59% | 18140 | money_delta->home (3-14 fit · 0-0 fwd); pre_move->home (1-3 fit · 0-0 fwd); money_level->home (25-17 fit · 0-0 fwd); sharp_gap->home (17-25 fit · 0-0 fwd); pin_value->away (16-3 fit · 0-0 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | moneyline | away | -77.1 | 8-1 | 900 (+900) | 980 | 0.6 | 879 ($10,000) |  | home 99% | 1% / 8% | 17670 | follow_move->away (17-18 fit · 0-0 fwd); rlm->away (4-16 fit · 0-0 fwd); rlm_ratio->away (3-7 fit · 0-0 fwd); rlm_quiet->away (2-15 fit · 0-0 fwd); money_level->home (35-7 fit · 0-0 fwd); sharp_gap->away (21-19 fit · 0-0 fwd); money_moving->away (14-19 fit · 0-0 fwd); consensus_gap->away (13-30 fit · 0-0 fwd); pin_rlm->away (2-7 fit · 0-0 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | spread | away | -88.3 | 5-1 | 4.5 (-110) | 5.5 | 1 | 4.5 ($30,000) |  |  | 46% / 47% | 20740 | money_delta->away (3-14 fit · 0-0 fwd); follow_move->away (16-21 fit · 0-0 fwd); money_level->home (25-17 fit · 0-0 fwd); sharp_gap->away (17-25 fit · 0-0 fwd); money_moving->away (10-21 fit · 0-0 fwd); pin_move->away (8-10 fit · 0-0 fwd) |

