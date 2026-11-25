# NFL board

Generated 2026-11-25 20:09 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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
| PINNACLE moved vs public | Denver Broncos @ Pittsburgh Steelers | total | under | Pinnacle | 38 -> 36 | — | 36.5 | 20% | 1.5 | 5-10 fit · 0-3 fwd |
| PINNACLE moved vs public | Green Bay Packers @ Los Angeles Rams | moneyline | away | Pinnacle | 137 -> 126 | **+2.6** | 120 | 30% | 1.53 | 5-10 fit · 0-3 fwd |
| PINNACLE moved vs public | Seattle Seahawks @ San Francisco 49ers | total | under | Pinnacle | 46.5 -> 44 | — | 44.5 | 18% | 1.33 | 5-10 fit · 0-3 fwd |
| PINNACLE moved vs public | Seattle Seahawks @ San Francisco 49ers | moneyline | away | Pinnacle | 153 -> 125 | — | 116 | 10% | 1.4 | 5-10 fit · 0-3 fwd |
| PINNACLE moved vs public | Tennessee Titans @ Jacksonville Jaguars | moneyline | away | Pinnacle | 729 -> 728 | — | 750 | 2% | 2.0 | 5-10 fit · 0-3 fwd |
| PINNACLE moved vs public | Washington Commanders @ Arizona Cardinals | moneyline | home | Pinnacle | 294 -> 284 | — | 300 | 3% | 1.33 | 5-10 fit · 0-3 fwd |
| FanDuel moved vs public | Atlanta Falcons @ Minnesota Vikings | total | under | FanDuel | 42.5 -> 41.5 | — | 41.5 | 31% | 1.23 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Denver Broncos @ Pittsburgh Steelers | total | under | FanDuel | 37.5 -> 36.5 | — | 36.5 | 20% | 1.5 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Kansas City Chiefs @ Buffalo Bills | moneyline | away | FanDuel | 132 -> 128 | **+0.7** | 128 | 24% | 1.58 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Las Vegas Raiders @ Cleveland Browns | moneyline | away | FanDuel | 198 -> 194 | — | 194 | 25% | 1.8 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Seattle Seahawks @ San Francisco 49ers | total | under | FanDuel | 46.5 -> 44.5 | — | 44.5 | 18% | 1.33 | 6-14 fit · 0-2 fwd |
| FanDuel moved vs public | Seattle Seahawks @ San Francisco 49ers | moneyline | away | FanDuel | 144 -> 116 | — | 116 | 10% | 1.4 | 6-14 fit · 0-2 fwd |
| line moved off the public (no ratio test) | Baltimore Ravens @ Houston Texans | moneyline | away | FanDuel | 265 -> 250 | — | 250 | 6% | 1.17 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | Carolina Panthers @ Tampa Bay Buccaneers | spread | home | FanDuel | -2.5 -> -3 | — | -3 | 39% | 1.13 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | Las Vegas Raiders @ Cleveland Browns | total | under | FanDuel | 41.5 -> 40.5 | **+1** | 40.5 | 26% | 1.04 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New Orleans Saints @ Cincinnati Bengals | spread | away | FanDuel | 10 -> 9.5 | — | 9.5 | 10% | 0.8 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New Orleans Saints @ Cincinnati Bengals | moneyline | away | FanDuel | 430 -> 420 | — | 420 | 2% | 1.0 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New York Giants @ Indianapolis Colts | spread | home | FanDuel | 7 -> 6.5 | — | 6.5 | 17% | 1.06 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New York Giants @ Indianapolis Colts | moneyline | home | FanDuel | 265 -> 240 | — | 240 | 6% | 0.67 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New York Jets @ Miami Dolphins | total | under | FanDuel | 41.5 -> 40.5 | — | 40.5 | 21% | 1.1 | 9-32 fit · 8-5 fwd |

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
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | spread | home **SPLIT** | +57.7 | 4-3 | -9.5 (-120) | -10 | 0.5 | -10 ($5,000) | +0.5 | home 90% | 90% / 92% | 4069 | follow_move->away (16-21 fit · 5-6 fwd); rlm->away (1-11 fit · 3-2 fwd); rlm_quiet->away (1-9 fit · 3-2 fwd); money_level->home (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->home (10-21 fit · 5-7 fwd); pin_value->home (16-3 fit · 2-3 fwd) |
| Thu 16:30 | Philadelphia Eagles @ Dallas Cowboys | moneyline | home **SPLIT** | +48.8 | 3-3 | -480 (-480) | -460 | 0.6 | -430 ($20,000) |  |  | 82% / 86% | 18483 | follow_move->home (17-18 fit · 5-5 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->home (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd); pin_value->away (2-7 fit · 1-3 fwd) |
| Thu 13:00 | Chicago Bears @ Detroit Lions | spread | home **SPLIT** | +43.9 | 4-2 | 1.5 (-112) | -2.5 | 4 | 1 ($30,000) | +0.5 |  | 46% / 59% | 26960 | follow_move->away (16-21 fit · 5-6 fwd); money_level->home (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd); pin_value->home (16-3 fit · 2-3 fwd); pin_move->home (8-10 fit · 3-4 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | moneyline | home **SPLIT** | +26.4 | 4-3 | -154 (-154) | -148 | 1 | -161 ($5,000) |  |  | 66% / 72% | 4346 | money_delta->away (4-5 fit · 1-1 fwd); follow_move->home (17-18 fit · 5-5 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->home (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd); pin_move->home (15-11 fit · 4-5 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | moneyline | away **SPLIT** | +20.4 | 4-2 | -210 (-210) | -205 | 0.5 | -191 ($6,000) |  |  | 87% / 91% | 3236 | follow_move->away (17-18 fit · 5-5 fwd); money_level->away (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->home (13-30 fit · 4-8 fwd); pin_value->home (2-7 fit · 1-3 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | moneyline | home | +22.4 | 2-1 | -330 (-330) | -310 | 1.1 | -319 ($6,000) |  |  | 98% / 98% | 5437 | follow_move->home (17-18 fit · 5-5 fwd); money_level->home (35-7 fit · 8-4 fwd); consensus_gap->away (13-30 fit · 4-8 fwd) |

## B  weighted ROI +10% to +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Baltimore Ravens @ Houston Texans | total | over **SPLIT** | +15.2 | 4-2 | 47.5 (-105) | 46.5 | 1 | 47.5 ($3,000) |  |  | 72% / 74% | 5124 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->over (10-9 fit · 8-2 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->over (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd); pin_move->over (14-13 fit · 10-2 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | total | over **SPLIT** | +15.2 | 4-2 | 48.5 (-110) | 47.5 | 1 | 48.5 ($3,000) |  |  | 76% / 78% | 4998 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->over (10-9 fit · 8-2 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->over (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd); pin_move->over (14-13 fit · 10-2 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | spread | home **SPLIT** | +11.8 | 2-2 | -7 (-105) | -7 |  | -7 ($10,000) |  |  | 85% / 86% | 5437 | money_level->home (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd); consensus_gap->away (5-3 fit · 0-2 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | spread | away | +16.3 | 4-1 | 1.5 (-115) | 3.5 | 2 | 1 ($5,000) | +0.5 |  | 65% / 59% | 4331 | follow_move->away (16-21 fit · 5-6 fwd); money_level->away (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd); pin_value->away (16-3 fit · 2-3 fwd) |
| Thu 16:30 | Philadelphia Eagles @ Dallas Cowboys | total | under | +11 | 2-1 | 47.5 (-100) | 48.5 | 1 | 47.5 ($5,000) |  |  | 93% / 93% | 18483 | follow_move->under (10-9 fit · 8-2 fwd); money_level->under (23-19 fit · 6-6 fwd); money_moving->over (15-18 fit · 6-6 fwd) |

## C  weighted ROI 0 to +10%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 16:30 | Philadelphia Eagles @ Dallas Cowboys | spread | away **SPLIT** | +9.1 | 3-2 | 8.5 (-110) | 1.5 | 7 | 8.5 ($30,000) |  |  | 54% / 55% | 18483 | money_delta->home (3-14 fit · 1-0 fwd); follow_move->home (16-21 fit · 5-6 fwd); money_level->away (25-17 fit · 3-8 fwd); sharp_gap->away (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | moneyline | away **SPLIT** | +8.4 | 4-2 | -184 (-184) | -142 | 6.1 | -191 ($8,000) |  |  | 88% / 78% | 15322 | follow_move->away (17-18 fit · 5-5 fwd); money_level->away (35-7 fit · 8-4 fwd); sharp_gap->home (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->home (13-30 fit · 4-8 fwd); pin_move->away (15-11 fit · 4-5 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | moneyline | away **SPLIT** | +5.2 | 3-2 | -104 (-104) | -104 |  | -105 ($3,000) |  |  | 62% / 65% | 4331 | money_level->away (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd); book_lag->home (1-1 fit · 0-0 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | total | over **SPLIT** | +1.2 | 2-2 | 42.5 (-100) | 42.5 |  | 42 ($3,000) | +0.5 |  | 77% / 75% | 4705 | money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->over (15-18 fit · 6-6 fwd); pin_value->under (12-11 fit · 4-2 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | spread | away | +8.8 | 3-1 | 2.5 (-100) | 2.5 |  | 2.5 ($30,000) |  |  | 56% / 60% | 24824 | money_level->away (25-17 fit · 3-8 fwd); sharp_gap->away (17-25 fit · 7-5 fwd); money_moving->home (10-21 fit · 5-7 fwd); pin_move->away (8-10 fit · 3-4 fwd) |
| Thu 16:30 | Philadelphia Eagles @ Dallas Cowboys | tt_home | under | +4.6 | 1-0 | 29.5 (-113) | 29.5 |  | 28.5 ($2,000) | -1 |  | 0% / 0% | 18483 | pin_value->under (17-12 fit · 2-4 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | tt_away | under | +2.3 | 1-0 | 16.5 (-100) | 17.5 | 1 | 16.5 ($2,000) |  |  | 0% / 0% | 5437 | follow_move->under (9-7 fit · 5-1 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | tt_away | under | +2 | 1-1 | 22.5 (-115) | 23.5 | 1 | 23.5 ($2,000) | +1 |  | 0% / 0% | 24824 | follow_move->under (9-7 fit · 5-1 fwd); pin_value->over (14-12 fit · 2-6 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | tt_away | under | +2 | 1-1 | 22.5 (-111) | 23.5 | 1 | 23.5 ($2,000) | +1 |  | 0% / 0% | 3236 | follow_move->under (9-7 fit · 5-1 fwd); pin_value->over (14-12 fit · 2-6 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | tt_away | under | +2 | 1-1 | 23.5 (-100) | 24.5 | 1 | 24.5 ($2,000) | +1 |  | 0% / 0% | 4705 | follow_move->under (9-7 fit · 5-1 fwd); pin_value->over (14-12 fit · 2-6 fwd) |
| Wed 20:00 | Green Bay Packers @ Los Angeles Rams | tt_away | over | +0.3 | 1-0 | 20.5 (-111) | 20.5 |  | 21.5 ($3,000) | -1 |  | 0% / 0% | 66011 | pin_value->over (14-12 fit · 2-6 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | tt_away | over | +0.3 | 1-0 | 19.5 (-132) | 19.5 |  | 20.5 ($2,000) | -1 |  | 0% / 0% | 15322 | pin_value->over (14-12 fit · 2-6 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | tt_away | over | +0.3 | 1-0 | 19.5 (-113) | 19.5 |  | 20.5 ($2,000) | -1 |  | 0% / 0% | 4069 | pin_value->over (14-12 fit · 2-6 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | tt_away | under | +0.3 | 1-0 | 16.5 (-100) | 16.5 |  | 15.5 ($2,000) | -1 |  | 0% / 0% | 4998 | pin_value->under (14-12 fit · 2-6 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | spread | away | +0.3 | 5-0 | -7 (-115) | -7 |  | -7.5 ($5,000) | +0.5 |  | 82% / 83% | 3423 | money_level->away (25-17 fit · 3-8 fwd); sharp_gap->away (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd); consensus_gap->away (5-3 fit · 0-2 fwd); pin_value->away (16-3 fit · 2-3 fwd) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | total | under **SPLIT** | -8.2 | 4-2 | 40.5 (-115) | 41.5 | 1 | 40.5 ($3,000) **retraced +1** |  | over 74% | 26% / 27% | 4649 | follow_move->under (10-9 fit · 8-2 fwd); rlm->under (4-5 fit · 4-1 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->over (15-18 fit · 6-6 fwd) |
| Wed 20:00 | Green Bay Packers @ Los Angeles Rams | spread | home **SPLIT** | -11.4 | 3-2 | -2.5 (-115) | -3.5 | 1 | -2.5 ($75,000) |  |  | 51% / 61% | 66011 | follow_move->away (16-21 fit · 5-6 fwd); money_level->home (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->home (10-21 fit · 5-7 fwd); pin_move->away (8-10 fit · 3-4 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | total | under **SPLIT** | -21.1 | 6-2 | 49.5 (-110) | 50.5 | 1 | 49 ($3,000) | -0.5 |  | 41% / 37% | 4069 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->under (10-9 fit · 8-2 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->over (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd); pin_value->under (12-11 fit · 4-2 fwd); pin_move->under (14-13 fit · 10-2 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | total | under **SPLIT** | -31.3 | 6-2 | 40.5 (-110) | 41.5 | 1 | 41 ($3,000) | +0.5 | over 79% | 21% / 23% | 3236 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->under (10-9 fit · 8-2 fwd); rlm->under (4-5 fit · 4-1 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd); pin_value->over (12-11 fit · 4-2 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | spread | away **SPLIT** | -41 | 3-2 | 2.5 (-110) | 2 | 0.5 | 2.5 ($5,000) |  |  | 30% / 31% | 6740 | follow_move->home (16-21 fit · 5-6 fwd); money_level->home (25-17 fit · 3-8 fwd); sharp_gap->away (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd); pin_move->away (8-10 fit · 3-4 fwd) |
| Wed 20:00 | Green Bay Packers @ Los Angeles Rams | moneyline | away **SPLIT** | -50.9 | 6-2 | 120 (+120) | 120 |  | 126 ($50,000) **retraced +2.6** |  |  | 30% / 46% | 66011 | money_delta->away (4-5 fit · 1-1 fwd); pre_move->away (1-3 fit · 0-2 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd); pin_move->away (15-11 fit · 4-5 fwd); pin_rlm->away (2-7 fit · 0-2 fwd) |
| Thu 13:00 | Chicago Bears @ Detroit Lions | moneyline | home **SPLIT** | -60.2 | 4-2 | 104 (+104) | 124 | 4.4 | 103 ($20,000) |  |  | 50% / 41% | 26960 | follow_move->home (17-18 fit · 5-5 fwd); money_level->away (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->home (13-30 fit · 4-8 fwd); pin_move->home (15-11 fit · 4-5 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | moneyline | home **SPLIT** | -65.1 | 5-2 | 300 (+300) | 300 |  | 284 ($3,000) |  |  | 3% / 4% | 3423 | pre_move->home (1-3 fit · 0-2 fwd); money_level->away (35-7 fit · 8-4 fwd); sharp_gap->home (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->home (13-30 fit · 4-8 fwd); pin_value->home (2-7 fit · 1-3 fwd); pin_rlm->home (2-7 fit · 0-2 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | moneyline | away **SPLIT** | -67.2 | 5-2 | 194 (+194) | 198 | 0.4 | 198 ($6,000) |  | home 75% | 25% / 45% | 4649 | follow_move->away (17-18 fit · 5-5 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | moneyline | home **SPLIT** | -83.3 | 5-3 | 240 (+240) | 265 | 2 | 239 ($6,000) |  | away 94% | 6% / 4% | 4705 | follow_move->home (17-18 fit · 5-5 fwd); rlm->home (4-16 fit · 1-2 fwd); rlm_quiet->home (2-15 fit · 1-2 fwd); money_level->away (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->home (13-30 fit · 4-8 fwd); pin_move->home (15-11 fit · 4-5 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | moneyline | away **SPLIT** | -83.5 | 4-2 | 420 (+420) | 430 | 0.7 | 417 ($3,000) |  | home 98% | 2% / 2% | 4069 | follow_move->away (17-18 fit · 5-5 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 8-4 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | moneyline | away **SPLIT** | -87.8 | 5-2 | 250 (+250) | 265 | 1.1 | 260 ($6,000) |  | home 94% | 6% / 7% | 5124 | follow_move->away (17-18 fit · 5-5 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | moneyline | away **SPLIT** | -96 | 6-2 | 128 (+128) | 132 | 0.6 | 129 ($20,000) |  | home 76% | 24% / 38% | 24824 | follow_move->away (17-18 fit · 5-5 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | spread | home **SPLIT** | -142.3 | 7-2 | -3 (-100) | -2.5 | 0.5 | -3 ($10,000) |  | away 61% | 39% / 44% | 4346 | money_delta->home (3-14 fit · 1-0 fwd); follow_move->home (16-21 fit · 5-6 fwd); rlm->home (1-11 fit · 3-2 fwd); rlm_quiet->home (1-9 fit · 3-2 fwd); money_level->away (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->home (10-21 fit · 5-7 fwd); consensus_gap->away (5-3 fit · 0-2 fwd); pin_move->home (8-10 fit · 3-4 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | tt_home | under | -1.2 | 2-0 | 16.5 (-113) | 17.5 | 1 | 16.5 ($2,000) |  |  | 0% / 0% | 15322 | follow_move->under (9-10 fit · 3-2 fwd); pin_move->under (1-0 fit · 0-0 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | spread | away | -1.4 | 4-1 | -3.5 (-100) | -1.5 | 2 | -3.5 ($10,000) |  |  | 76% / 80% | 15322 | follow_move->away (16-21 fit · 5-6 fwd); money_level->away (25-17 fit · 3-8 fwd); sharp_gap->away (17-25 fit · 7-5 fwd); money_moving->home (10-21 fit · 5-7 fwd); pin_move->away (8-10 fit · 3-4 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | total | under | -1.5 | 4-0 | 46.5 (-110) | 48.5 | 2 | 46.5 ($5,000) |  |  | 71% / 83% | 24824 | follow_move->under (10-9 fit · 8-2 fwd); money_level->under (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); pin_move->under (14-13 fit · 10-2 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | spread | away | -1.8 | 2-0 | 4.5 (-105) | 5 | 0.5 | 4.5 ($10,000) |  |  | 65% / 65% | 4649 | follow_move->away (16-21 fit · 5-6 fwd); money_level->away (25-17 fit · 3-8 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | total | under | -3.3 | 9-1 | 36.5 (-110) | 37.5 | 1 | 36 ($3,000) | -0.5 | over 80% | 20% / 30% | 15322 | follow_move->under (10-9 fit · 8-2 fwd); rlm->under (4-5 fit · 4-1 fwd); rlm_ratio->under (3-1 fit · 0-0 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd); pin_value->under (12-11 fit · 4-2 fwd); pin_move->under (14-13 fit · 10-2 fwd); pin_rlm->under (3-1 fit · 0-0 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | total | over | -4.3 | 2-0 | 41.5 (-110) | 41.5 |  | 41.5 ($3,000) |  |  | 83% / 83% | 3423 | money_level->over (23-19 fit · 6-6 fwd); money_moving->over (15-18 fit · 6-6 fwd) |
| Thu 13:00 | Chicago Bears @ Detroit Lions | tt_home | over | -4.6 | 1-0 | 27.5 (-113) | 26.5 | 1 | 27.5 ($2,000) |  |  | 0% / 0% | 26960 | follow_move->over (9-10 fit · 3-2 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | tt_home | under | -4.6 | 1-0 | 17.5 (-113) | 18.5 | 1 | 17.5 ($2,000) |  |  | 0% / 0% | 3236 | follow_move->under (9-10 fit · 3-2 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | tt_home | over | -4.6 | 1-0 | 27.5 (+102) | 26.5 | 1 | 27.5 ($2,000) |  |  | 0% / 0% | 5124 | follow_move->over (9-10 fit · 3-2 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | tt_home | over | -4.6 | 1-0 | 31.5 (-102) | 30.5 | 1 | 31.5 ($2,000) |  |  | 0% / 0% | 4998 | follow_move->over (9-10 fit · 3-2 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | tt_home | over | -4.6 | 1-0 | 23.5 (-106) | 22.5 | 1 | 23.5 ($2,000) |  |  | 0% / 0% | 4346 | follow_move->over (9-10 fit · 3-2 fwd) |
| Thu 13:00 | Chicago Bears @ Detroit Lions | total | under | -8.7 | 3-0 | 55.5 (-108) | 55.5 |  | 55.5 ($5,000) |  |  | 83% / 88% | 26960 | money_level->under (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd) |
| Wed 20:00 | Green Bay Packers @ Los Angeles Rams | total | under | -9 | 5-0 | 43.5 (-115) | 44.5 | 1 | 43.5 ($20,000) |  |  | 92% / 95% | 66011 | follow_move->under (10-9 fit · 8-2 fwd); money_level->under (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd); pin_move->under (14-13 fit · 10-2 fwd) |
| Wed 20:00 | Green Bay Packers @ Los Angeles Rams | tt_home | under | -9.2 | 1-1 | 22.5 (-102) | 23.5 | 1 | 24.5 ($3,000) | +2 |  | 0% / 0% | 66011 | follow_move->under (9-10 fit · 3-2 fwd); pin_value->over (17-12 fit · 2-4 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | tt_home | under | -9.2 | 1-1 | 24.5 (-128) | 25.5 | 1 | 26.5 ($2,000) | +2 |  | 0% / 0% | 24824 | follow_move->under (9-10 fit · 3-2 fwd); pin_value->over (17-12 fit · 2-4 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | tt_home | over | -9.2 | 1-1 | 17.5 (+102) | 16.5 | 1 | 16.5 ($2,000) | +1 |  | 0% / 0% | 4705 | follow_move->over (9-10 fit · 3-2 fwd); pin_value->under (17-12 fit · 2-4 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | tt_home | under | -9.2 | 1-1 | 23.5 (-118) | 24.5 | 1 | 24.5 ($2,000) | +1 |  | 0% / 0% | 6740 | follow_move->under (9-10 fit · 3-2 fwd); pin_value->over (17-12 fit · 2-4 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | tt_home | under | -9.2 | 1-1 | 22.5 (-102) | 23.5 | 1 | 23.5 ($2,000) | +1 |  | 0% / 0% | 4649 | follow_move->under (9-10 fit · 3-2 fwd); pin_value->over (17-12 fit · 2-4 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | total | under | -11.7 | 2-1 | 43.5 (-105) | 43.5 |  | 43.5 ($5,000) |  |  | 17% / 21% | 4346 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | total | under | -12.5 | 10-1 | 44.5 (-110) | 46.5 | 2 | 44 ($3,000) | -0.5 | over 82% | 18% / 24% | 6740 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->under (10-9 fit · 8-2 fwd); rlm->under (4-5 fit · 4-1 fwd); rlm_ratio->under (3-1 fit · 0-0 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd); pin_value->under (12-11 fit · 4-2 fwd); pin_move->under (14-13 fit · 10-2 fwd); pin_rlm->under (3-1 fit · 0-0 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | total | under | -15.1 | 2-1 | 35.5 (-108) | 35.5 |  | 35.5 ($3,000) |  |  | 15% / 16% | 4331 | money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | total | under | -17.4 | 6-1 | 41.5 (-110) | 42.5 | 1 | 41.5 ($3,000) |  | over 69% | 31% / 38% | 5437 | follow_move->under (10-9 fit · 8-2 fwd); rlm->under (4-5 fit · 4-1 fwd); rlm_ratio->under (3-1 fit · 0-0 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | spread | home | -23.4 | 3-0 | -14.5 (-105) | -14 | 0.5 | -14.5 ($10,000) |  |  | 90% / 90% | 4998 | follow_move->home (16-21 fit · 5-6 fwd); money_level->home (25-17 fit · 3-8 fwd); money_moving->home (10-21 fit · 5-7 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | moneyline | away | -48.6 | 5-1 | 750 (+750) | 750 |  | 728 ($6,000) |  |  | 2% / 4% | 4998 | pre_move->away (1-3 fit · 0-2 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd); pin_rlm->away (2-7 fit · 0-2 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | spread | away | -71.7 | 3-1 | 6.5 (-105) | 6.5 |  | 6.5 ($10,000) |  |  | 44% / 45% | 5124 | money_delta->away (3-14 fit · 1-0 fwd); money_level->home (25-17 fit · 3-8 fwd); sharp_gap->away (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | moneyline | away | -79.4 | 10-1 | 116 (+116) | 144 | 5.6 | 125 ($3,000) |  | home 90% | 10% / 14% | 6740 | money_delta->away (4-5 fit · 1-1 fwd); follow_move->away (17-18 fit · 5-5 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd); pin_move->away (15-11 fit · 4-5 fwd); pin_rlm->away (2-7 fit · 0-2 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | spread | home | -81.9 | 4-1 | 3.5 (-100) | 4 | 0.5 | 3.5 ($10,000) |  |  | 44% / 45% | 3236 | money_delta->home (3-14 fit · 1-0 fwd); follow_move->home (16-21 fit · 5-6 fwd); money_level->away (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->home (10-21 fit · 5-7 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | spread | home | -132.5 | 6-1 | 6.5 (-115) | 7 | 0.5 | 6.5 ($10,000) |  | away 83% | 17% / 18% | 4705 | money_delta->home (3-14 fit · 1-0 fwd); follow_move->home (16-21 fit · 5-6 fwd); rlm->home (1-11 fit · 3-2 fwd); rlm_quiet->home (1-9 fit · 3-2 fwd); money_level->away (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->home (10-21 fit · 5-7 fwd) |

