# NFL board

Generated 2026-11-25 09:02 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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
| PINNACLE moved vs public | Denver Broncos @ Pittsburgh Steelers | total | under | Pinnacle | 38 -> 36 | — | 36.5 | 22% | 1.68 | 5-10 fit · 0-3 fwd |
| PINNACLE moved vs public | Green Bay Packers @ Los Angeles Rams | moneyline | away | Pinnacle | 137 -> 118 | **+1.3** | 120 | 24% | 2.21 | 5-10 fit · 0-3 fwd |
| PINNACLE moved vs public | New York Giants @ Indianapolis Colts | moneyline | home | Pinnacle | 253 -> 248 | — | 275 | 5% | 1.2 | 5-10 fit · 0-3 fwd |
| PINNACLE moved vs public | Seattle Seahawks @ San Francisco 49ers | total | under | Pinnacle | 46.5 -> 45 | — | 45.5 | 18% | 1.22 | 5-10 fit · 0-3 fwd |
| PINNACLE moved vs public | Seattle Seahawks @ San Francisco 49ers | moneyline | away | Pinnacle | 153 -> 150 | — | 136 | 9% | 1.22 | 5-10 fit · 0-3 fwd |
| PINNACLE moved vs public | Washington Commanders @ Arizona Cardinals | moneyline | home | Pinnacle | 294 -> 282 | — | 300 | 4% | 1.25 | 5-10 fit · 0-3 fwd |
| FanDuel moved vs public | Denver Broncos @ Pittsburgh Steelers | total | under | FanDuel | 37.5 -> 36.5 | — | 36.5 | 22% | 1.68 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Kansas City Chiefs @ Buffalo Bills | moneyline | away | FanDuel | 132 -> 128 | **+0.7** | 128 | 22% | 1.77 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Seattle Seahawks @ San Francisco 49ers | total | under | FanDuel | 46.5 -> 45.5 | — | 45.5 | 18% | 1.22 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Seattle Seahawks @ San Francisco 49ers | moneyline | away | FanDuel | 144 -> 136 | — | 136 | 9% | 1.22 | 6-14 fit · 0-2 fwd |
| line moved off the public (no ratio test) | Atlanta Falcons @ Minnesota Vikings | total | under | FanDuel | 42.5 -> 41.5 | — | 41.5 | 35% | 1.17 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | Baltimore Ravens @ Houston Texans | moneyline | away | FanDuel | 265 -> 250 | — | 250 | 6% | 1.17 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | Carolina Panthers @ Tampa Bay Buccaneers | spread | home | FanDuel | -2.5 -> -3 | — | -3 | 35% | 1.06 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | Las Vegas Raiders @ Cleveland Browns | total | under | FanDuel | 41.5 -> 40.5 | — | 40.5 | 22% | 1.05 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New Orleans Saints @ Cincinnati Bengals | spread | away | FanDuel | 10 -> 9.5 | — | 9.5 | 13% | 0.85 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New Orleans Saints @ Cincinnati Bengals | moneyline | away | FanDuel | 430 -> 420 | — | 420 | 2% | 1.0 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New York Giants @ Indianapolis Colts | spread | home | FanDuel | 7 -> 6.5 | — | 6.5 | 14% | 1.07 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New York Jets @ Miami Dolphins | spread | home | FanDuel | 4 -> 3.5 | — | 3.5 | 40% | 1.0 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New York Jets @ Miami Dolphins | total | under | FanDuel | 41.5 -> 40.5 | — | 40.5 | 20% | 1.15 | 9-32 fit · 8-5 fwd |

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
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | spread | home **SPLIT** | +57.7 | 4-3 | -9.5 (-120) | -10 | 0.5 | -10 ($5,000) | +0.5 | home 87% | 87% / 89% | 2696 | follow_move->away (16-21 fit · 5-6 fwd); rlm->away (1-11 fit · 3-2 fwd); rlm_quiet->away (1-9 fit · 3-2 fwd); money_level->home (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->home (10-21 fit · 5-7 fwd); pin_value->home (16-3 fit · 2-3 fwd) |
| Thu 16:30 | Philadelphia Eagles @ Dallas Cowboys | moneyline | home **SPLIT** | +48.8 | 3-3 | -490 (-490) | -460 | 0.9 | -429 ($20,000) |  |  | 80% / 87% | 12152 | follow_move->home (17-18 fit · 5-5 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->home (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd); pin_value->away (2-7 fit · 1-3 fwd) |
| Thu 13:00 | Chicago Bears @ Detroit Lions | spread | home **SPLIT** | +47.3 | 5-2 | 2.5 (-115) | -2.5 | 5 | 1 ($30,000) | +1.5 |  | 44% / 58% | 17816 | follow_move->away (16-21 fit · 5-6 fwd); money_level->home (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd); consensus_gap->home (5-3 fit · 0-2 fwd); pin_value->home (16-3 fit · 2-3 fwd); pin_move->home (8-10 fit · 3-4 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | spread | home **SPLIT** | +38 | 3-2 | -3 (-110) | -2 | 1 | -3 ($10,000) |  |  | 66% / 64% | 4654 | follow_move->home (16-21 fit · 5-6 fwd); money_level->home (25-17 fit · 3-8 fwd); sharp_gap->away (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd); consensus_gap->home (5-3 fit · 0-2 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | moneyline | home **SPLIT** | +26.4 | 4-3 | -154 (-154) | -148 | 1 | -161 ($5,000) |  |  | 70% / 75% | 3372 | money_delta->away (4-5 fit · 1-1 fwd); follow_move->home (17-18 fit · 5-5 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->home (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd); pin_move->home (15-11 fit · 4-5 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | moneyline | home | +22.4 | 2-1 | -330 (-330) | -310 | 1.1 | -319 ($6,000) |  |  | 98% / 98% | 3847 | follow_move->home (17-18 fit · 5-5 fwd); money_level->home (35-7 fit · 8-4 fwd); consensus_gap->away (13-30 fit · 4-8 fwd) |

## B  weighted ROI +10% to +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | total | over **SPLIT** | +15.2 | 4-2 | 48.5 (-110) | 47.5 | 1 | 48.5 ($3,000) |  |  | 73% / 76% | 3569 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->over (10-9 fit · 8-2 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->over (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd); pin_move->over (14-13 fit · 10-2 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | moneyline | home **SPLIT** | +12.5 | 3-2 | -245 (-245) | -240 | 0.4 | -231 ($6,000) |  |  | 77% / 55% | 3175 | follow_move->home (17-18 fit · 5-5 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | spread | away | +16.3 | 4-1 | 1.5 (-115) | 3.5 | 2 | 1 ($5,000) | +0.5 |  | 65% / 61% | 3387 | follow_move->away (16-21 fit · 5-6 fwd); money_level->away (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd); pin_value->away (16-3 fit · 2-3 fwd) |

## C  weighted ROI 0 to +10%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | moneyline | away **SPLIT** | +8.4 | 4-2 | -205 (-205) | -142 | 8.7 | -193 ($5,000) |  |  | 86% / 76% | 10385 | follow_move->away (17-18 fit · 5-5 fwd); money_level->away (35-7 fit · 8-4 fwd); sharp_gap->home (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->home (13-30 fit · 4-8 fwd); pin_move->away (15-11 fit · 4-5 fwd) |
| Thu 16:30 | Philadelphia Eagles @ Dallas Cowboys | spread | away **SPLIT** | +5.4 | 3-2 | 8.5 (-110) | 1.5 | 7 | 8.5 ($30,000) |  |  | 57% / 58% | 12152 | follow_move->home (16-21 fit · 5-6 fwd); rlm_quiet->home (1-9 fit · 3-2 fwd); money_level->away (25-17 fit · 3-8 fwd); sharp_gap->away (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | moneyline | away **SPLIT** | +5.2 | 3-2 | -104 (-104) | -104 |  | -105 ($3,000) |  |  | 59% / 63% | 3387 | money_level->away (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd); book_lag->home (1-1 fit · 0-0 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | total | over **SPLIT** | +1.2 | 2-2 | 42.5 (-100) | 42.5 |  | 42 ($3,000) | +0.5 |  | 81% / 78% | 3311 | money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->over (15-18 fit · 6-6 fwd); pin_value->under (12-11 fit · 4-2 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | spread | home | +8.4 | 1-0 | -6.5 (-115) | -6.5 |  | -6.5 ($10,000) |  |  | 59% / 59% | 3983 | money_level->home (25-17 fit · 3-8 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | total | over | +6.3 | 2-1 | 50.5 (-110) | 50.5 |  | 50.5 ($3,000) |  |  | 60% / 68% | 2696 | money_level->over (23-19 fit · 6-6 fwd); sharp_gap->over (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd) |
| Wed 20:00 | Green Bay Packers @ Los Angeles Rams | tt_home | over | +4.6 | 1-0 | 23.5 (-100) | 23.5 |  | 24.5 ($3,000) | -1 |  | 0% / 0% | 25157 | pin_value->over (17-12 fit · 2-4 fwd) |
| Thu 16:30 | Philadelphia Eagles @ Dallas Cowboys | tt_home | under | +4.6 | 1-0 | 29.5 (-115) | 29.5 |  | 28.5 ($2,000) | -1 |  | 0% / 0% | 12152 | pin_value->under (17-12 fit · 2-4 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | tt_away | over | +2.3 | 1-0 | 20.5 (+102) | 19.5 | 1 | 20.5 ($2,000) |  |  | 0% / 0% | 10385 | follow_move->over (9-7 fit · 5-1 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | tt_away | under | +2.3 | 1-0 | 16.5 (-100) | 17.5 | 1 | 16.5 ($2,000) |  |  | 0% / 0% | 3847 | follow_move->under (9-7 fit · 5-1 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | tt_away | under | +2 | 1-1 | 22.5 (-100) | 23.5 | 1 | 23.5 ($2,000) | +1 |  | 0% / 0% | 16953 | follow_move->under (9-7 fit · 5-1 fwd); pin_value->over (14-12 fit · 2-6 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | tt_away | under | +2 | 1-1 | 22.5 (-111) | 23.5 | 1 | 23.5 ($2,000) | +1 |  | 0% / 0% | 2352 | follow_move->under (9-7 fit · 5-1 fwd); pin_value->over (14-12 fit · 2-6 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | tt_away | under | +2 | 1-1 | 20.5 (-104) | 21.5 | 1 | 21.5 ($2,000) | +1 |  | 0% / 0% | 4654 | follow_move->under (9-7 fit · 5-1 fwd); pin_value->over (14-12 fit · 2-6 fwd) |
| Wed 20:00 | Green Bay Packers @ Los Angeles Rams | tt_away | over | +0.3 | 1-0 | 20.5 (-120) | 20.5 |  | 21.5 ($3,000) | -1 |  | 0% / 0% | 25157 | pin_value->over (14-12 fit · 2-6 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | tt_away | over | +0.3 | 1-0 | 19.5 (-125) | 19.5 |  | 20.5 ($2,000) | -1 |  | 0% / 0% | 2696 | pin_value->over (14-12 fit · 2-6 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | tt_away | under | +0.3 | 1-0 | 16.5 (-100) | 16.5 |  | 15.5 ($2,000) | -1 |  | 0% / 0% | 3569 | pin_value->under (14-12 fit · 2-6 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | spread | away | +0.3 | 5-0 | -7 (-115) | -7 |  | -7.5 ($5,000) | +0.5 |  | 80% / 82% | 2327 | money_level->away (25-17 fit · 3-8 fwd); sharp_gap->away (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd); consensus_gap->away (5-3 fit · 0-2 fwd); pin_value->away (16-3 fit · 2-3 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | total | over | +0.1 | 2-1 | 41.5 (-110) | 41.5 |  | 41.5 ($3,000) |  |  | 81% / 79% | 2327 | money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->over (15-18 fit · 6-6 fwd) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | total | under **SPLIT** | -6.5 | 4-4 | 40.5 (-105) | 41.5 | 1 | 41.5 ($3,000) | +1 | over 78% | 22% / 23% | 3175 | follow_move->under (10-9 fit · 8-2 fwd); rlm->under (4-5 fit · 4-1 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->over (15-18 fit · 6-6 fwd); pin_value->over (12-11 fit · 4-2 fwd); pin_move->over (14-13 fit · 10-2 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | spread | home **SPLIT** | -21.2 | 2-2 | -7 (-105) | -7 |  | -7 ($10,000) |  |  | 86% / 88% | 3847 | money_level->home (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); consensus_gap->away (5-3 fit · 0-2 fwd); book_lag->away (4-0 fit · 0-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | total | under **SPLIT** | -25.7 | 4-2 | 47.5 (-115) | 46.5 | 1 | 46.5 ($3,000) | -1 |  | 28% / 29% | 3983 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->over (10-9 fit · 8-2 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd); pin_value->under (12-11 fit · 4-2 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | total | under **SPLIT** | -31.3 | 6-2 | 40.5 (-110) | 41.5 | 1 | 41 ($3,000) | +0.5 | over 80% | 20% / 23% | 2352 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->under (10-9 fit · 8-2 fwd); rlm->under (4-5 fit · 4-1 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd); pin_value->over (12-11 fit · 4-2 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | moneyline | home **SPLIT** | -57.4 | 4-2 | 176 (+176) | 172 | 0.5 | 167 ($6,000) |  |  | 15% / 16% | 2352 | follow_move->away (17-18 fit · 5-5 fwd); money_level->away (35-7 fit · 8-4 fwd); sharp_gap->home (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->home (13-30 fit · 4-8 fwd); pin_value->home (2-7 fit · 1-3 fwd) |
| Thu 13:00 | Chicago Bears @ Detroit Lions | moneyline | home **SPLIT** | -60.2 | 4-2 | 110 (+110) | 124 | 3 | 105 ($20,000) |  |  | 51% / 38% | 17816 | follow_move->home (17-18 fit · 5-5 fwd); money_level->away (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->home (13-30 fit · 4-8 fwd); pin_move->home (15-11 fit · 4-5 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | moneyline | home **SPLIT** | -64.8 | 5-2 | 275 (+275) | 265 | 0.7 | 248 ($6,000) |  |  | 5% / 6% | 3311 | follow_move->away (17-18 fit · 5-5 fwd); money_level->away (35-7 fit · 8-4 fwd); sharp_gap->home (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->home (13-30 fit · 4-8 fwd); pin_value->home (2-7 fit · 1-3 fwd); pin_rlm->home (2-7 fit · 0-2 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | moneyline | home **SPLIT** | -65.1 | 5-2 | 300 (+300) | 300 |  | 282 ($3,000) |  |  | 4% / 5% | 2327 | pre_move->home (1-3 fit · 0-2 fwd); money_level->away (35-7 fit · 8-4 fwd); sharp_gap->home (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->home (13-30 fit · 4-8 fwd); pin_value->home (2-7 fit · 1-3 fwd); pin_rlm->home (2-7 fit · 0-2 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | moneyline | away **SPLIT** | -83.5 | 4-2 | 420 (+420) | 430 | 0.7 | 417 ($3,000) |  | home 98% | 2% / 2% | 2696 | follow_move->away (17-18 fit · 5-5 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 8-4 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | moneyline | away **SPLIT** | -87.8 | 5-2 | 250 (+250) | 265 | 1.1 | 259 ($6,000) |  | home 94% | 6% / 7% | 3983 | follow_move->away (17-18 fit · 5-5 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | moneyline | away **SPLIT** | -96 | 6-2 | 128 (+128) | 132 | 0.6 | 129 ($20,000) |  | home 78% | 22% / 39% | 16953 | follow_move->away (17-18 fit · 5-5 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | spread | home **SPLIT** | -115.4 | 6-2 | -3 (-100) | -2.5 | 0.5 | -3 ($10,000) |  | away 65% | 35% / 37% | 3372 | follow_move->home (16-21 fit · 5-6 fwd); rlm->home (1-11 fit · 3-2 fwd); rlm_quiet->home (1-9 fit · 3-2 fwd); money_level->away (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->home (10-21 fit · 5-7 fwd); consensus_gap->away (5-3 fit · 0-2 fwd); pin_move->home (8-10 fit · 3-4 fwd) |
| Thu 16:30 | Philadelphia Eagles @ Dallas Cowboys | total | under | -0.9 | 3-0 | 47.5 (-105) | 48.5 | 1 | 47.5 ($5,000) |  |  | 93% / 94% | 12152 | follow_move->under (10-9 fit · 8-2 fwd); money_level->under (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd) |
| Thu 13:00 | Chicago Bears @ Detroit Lions | total | under | -1.2 | 2-0 | 55.5 (-115) | 55.5 |  | 55.5 ($5,000) |  |  | 84% / 88% | 17816 | money_level->under (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | tt_home | under | -1.2 | 2-0 | 16.5 (-128) | 17.5 | 1 | 16.5 ($2,000) |  |  | 0% / 0% | 10385 | follow_move->under (9-10 fit · 3-2 fwd); pin_move->under (1-0 fit · 0-0 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | spread | away | -1.4 | 4-1 | -3.5 (-115) | -1.5 | 2 | -3.5 ($5,000) |  |  | 73% / 77% | 10385 | follow_move->away (16-21 fit · 5-6 fwd); money_level->away (25-17 fit · 3-8 fwd); sharp_gap->away (17-25 fit · 7-5 fwd); money_moving->home (10-21 fit · 5-7 fwd); pin_move->away (8-10 fit · 3-4 fwd) |
| Wed 20:00 | Green Bay Packers @ Los Angeles Rams | total | under | -1.8 | 3-0 | 44.5 (-120) | 44.5 |  | 44.5 ($10,000) |  |  | 92% / 94% | 25157 | money_level->under (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); pin_move->under (14-13 fit · 10-2 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | spread | away | -1.8 | 2-0 | 4.5 (-105) | 5 | 0.5 | 4.5 ($10,000) |  |  | 65% / 65% | 3175 | follow_move->away (16-21 fit · 5-6 fwd); money_level->away (25-17 fit · 3-8 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | total | under | -3.3 | 9-1 | 36.5 (-114) | 37.5 | 1 | 36 ($3,000) | -0.5 | over 78% | 22% / 37% | 10385 | follow_move->under (10-9 fit · 8-2 fwd); rlm->under (4-5 fit · 4-1 fwd); rlm_ratio->under (3-1 fit · 0-0 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd); pin_value->under (12-11 fit · 4-2 fwd); pin_move->under (14-13 fit · 10-2 fwd); pin_rlm->under (3-1 fit · 0-0 fwd) |
| Thu 13:00 | Chicago Bears @ Detroit Lions | tt_home | over | -4.6 | 1-0 | 27.5 (-102) | 26.5 | 1 | 27.5 ($2,000) |  |  | 0% / 0% | 17816 | follow_move->over (9-10 fit · 3-2 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | tt_home | under | -4.6 | 1-0 | 17.5 (-113) | 18.5 | 1 | 17.5 ($2,000) |  |  | 0% / 0% | 2352 | follow_move->under (9-10 fit · 3-2 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | tt_home | over | -4.6 | 1-0 | 27.5 (+102) | 26.5 | 1 | 27.5 ($2,000) |  |  | 0% / 0% | 3983 | follow_move->over (9-10 fit · 3-2 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | tt_home | over | -4.6 | 1-0 | 31.5 (-102) | 30.5 | 1 | 31.5 ($2,000) |  |  | 0% / 0% | 3569 | follow_move->over (9-10 fit · 3-2 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | tt_home | over | -4.6 | 1-0 | 23.5 (-106) | 22.5 | 1 | 23.5 ($2,000) |  |  | 0% / 0% | 3372 | follow_move->over (9-10 fit · 3-2 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | total | under | -9 | 5-0 | 47.5 (-110) | 48.5 | 1 | 47.5 ($5,000) |  |  | 71% / 84% | 16953 | follow_move->under (10-9 fit · 8-2 fwd); money_level->under (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd); pin_move->under (14-13 fit · 10-2 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | tt_home | under | -9.2 | 1-1 | 24.5 (-113) | 25.5 | 1 | 26.5 ($2,000) | +2 |  | 0% / 0% | 16953 | follow_move->under (9-10 fit · 3-2 fwd); pin_value->over (17-12 fit · 2-4 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | tt_home | under | -9.2 | 1-1 | 23.5 (-102) | 24.5 | 1 | 24.5 ($2,000) | +1 |  | 0% / 0% | 4654 | follow_move->under (9-10 fit · 3-2 fwd); pin_value->over (17-12 fit · 2-4 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | total | under | -11.7 | 2-1 | 43.5 (-105) | 43.5 |  | 43.5 ($5,000) |  |  | 17% / 21% | 3372 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | total | under | -12.5 | 10-1 | 45.5 (-115) | 46.5 | 1 | 45 ($3,000) | -0.5 | over 82% | 18% / 22% | 4654 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->under (10-9 fit · 8-2 fwd); rlm->under (4-5 fit · 4-1 fwd); rlm_ratio->under (3-1 fit · 0-0 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd); pin_value->under (12-11 fit · 4-2 fwd); pin_move->under (14-13 fit · 10-2 fwd); pin_rlm->under (3-1 fit · 0-0 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | spread | away | -12.8 | 3-0 | 2.5 (-100) | 2.5 |  | 2.5 ($30,000) |  |  | 58% / 63% | 16953 | money_level->away (25-17 fit · 3-8 fwd); sharp_gap->away (17-25 fit · 7-5 fwd); pin_move->away (8-10 fit · 3-4 fwd) |
| Wed 20:00 | Green Bay Packers @ Los Angeles Rams | moneyline | away | -22.9 | 8-0 | 120 (+120) | 120 |  | 118 ($30,000) **retraced +1.3** |  |  | 24% / 53% | 25157 | money_delta->away (4-5 fit · 1-1 fwd); pre_move->away (1-3 fit · 0-2 fwd); money_level->away (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd); pin_move->away (15-11 fit · 4-5 fwd); pin_rlm->away (2-7 fit · 0-2 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | total | under | -23.2 | 5-1 | 41.5 (-110) | 42.5 | 1 | 41.5 ($3,000) |  | over 65% | 35% / 41% | 3847 | follow_move->under (10-9 fit · 8-2 fwd); rlm->under (4-5 fit · 4-1 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd) |
| Wed 20:00 | Green Bay Packers @ Los Angeles Rams | spread | away | -23.4 | 3-1 | 2.5 (-108) | 3.5 | 1 | 2.5 ($50,000) |  |  | 54% / 50% | 25157 | follow_move->away (16-21 fit · 5-6 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd); pin_move->away (8-10 fit · 3-4 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | spread | home | -23.4 | 3-0 | -14.5 (-105) | -14 | 0.5 | -14.5 ($10,000) |  |  | 89% / 89% | 3569 | follow_move->home (16-21 fit · 5-6 fwd); money_level->home (25-17 fit · 3-8 fwd); money_moving->home (10-21 fit · 5-7 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | total | under | -24.3 | 3-1 | 35.5 (-108) | 35.5 |  | 35.5 ($3,000) |  |  | 16% / 18% | 3387 | money_delta->under (4-7 fit · 2-3 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | moneyline | away | -53.1 | 4-1 | 750 (+750) | 750 |  | 730 ($6,000) |  |  | 2% / 3% | 3569 | pre_move->away (1-3 fit · 0-2 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | moneyline | away | -77.1 | 8-1 | 136 (+136) | 144 | 1.4 | 150 ($6,000) |  | home 91% | 9% / 11% | 4654 | follow_move->away (17-18 fit · 5-5 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd); pin_rlm->away (2-7 fit · 0-2 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | spread | home | -96.1 | 4-1 | 3.5 (-100) | 4 | 0.5 | 3.5 ($10,000) |  | away 60% | 40% / 40% | 2352 | money_delta->home (3-14 fit · 1-0 fwd); follow_move->home (16-21 fit · 5-6 fwd); rlm->home (1-11 fit · 3-2 fwd); rlm_quiet->home (1-9 fit · 3-2 fwd); money_level->away (25-17 fit · 3-8 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | spread | home | -105.6 | 5-1 | 6.5 (-105) | 7 | 0.5 | 6.5 ($10,000) |  | away 86% | 14% / 15% | 3311 | follow_move->home (16-21 fit · 5-6 fwd); rlm->home (1-11 fit · 3-2 fwd); rlm_quiet->home (1-9 fit · 3-2 fwd); money_level->away (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->home (10-21 fit · 5-7 fwd) |

