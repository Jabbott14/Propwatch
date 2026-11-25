# NFL board

Generated 2026-11-25 00:04 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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
| PINNACLE moved vs public | Denver Broncos @ Pittsburgh Steelers | total | under | Pinnacle | 38 -> 37 | — | 37.5 | 23% | 1.35 | 5-10 fit · 0-3 fwd |
| PINNACLE moved vs public | Green Bay Packers @ Los Angeles Rams | moneyline | away | Pinnacle | 137 -> 119 | **+1.5** | 120 | 21% | 2.14 | 5-10 fit · 0-3 fwd |
| PINNACLE moved vs public | Kansas City Chiefs @ Buffalo Bills | moneyline | away | Pinnacle | 128 (other side moved) | **+2.5** | 128 | 20% | 1.85 | 5-10 fit · 0-3 fwd |
| PINNACLE moved vs public | Seattle Seahawks @ San Francisco 49ers | moneyline | away | Pinnacle | 153 (other side moved) | — | 146 | 8% | 1.38 | 5-10 fit · 0-3 fwd |
| PINNACLE moved vs public | Washington Commanders @ Arizona Cardinals | moneyline | home | Pinnacle | 294 -> 288 | — | 300 | 3% | 2.0 | 5-10 fit · 0-3 fwd |
| FanDuel moved vs public | Kansas City Chiefs @ Buffalo Bills | moneyline | away | FanDuel | 132 -> 128 | **+2.5** | 128 | 20% | 1.85 | 6-14 fit · 0-2 fwd |
| line moved off the public (no ratio test) | Carolina Panthers @ Tampa Bay Buccaneers | spread | home | FanDuel | -2.5 -> -3 | — | -3 | 38% | 0.95 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New Orleans Saints @ Cincinnati Bengals | spread | away | FanDuel | 10 -> 9.5 | — | 9.5 | 12% | 1.0 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New York Giants @ Indianapolis Colts | spread | home | FanDuel | 7 -> 6.5 | — | 6.5 | 13% | 1.08 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New York Jets @ Miami Dolphins | spread | home | FanDuel | 4 -> 3.5 | — | 3.5 | 36% | 1.0 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | New York Jets @ Miami Dolphins | total | under | FanDuel | 41.5 -> 40.5 | — | 40.5 | 20% | 0.95 | 9-32 fit · 8-5 fwd |
| line moved off the public (no ratio test) | Seattle Seahawks @ San Francisco 49ers | total | under | FanDuel | 46.5 -> 45.5 | — | 45.5 | 18% | 1.0 | 9-32 fit · 8-5 fwd |

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
| Thu 16:30 | Philadelphia Eagles @ Dallas Cowboys | moneyline | home **SPLIT** | +48.8 | 3-3 | -510 (-510) | -460 | 1.5 | -421 ($10,000) |  |  | 78% / 87% | 8552 | follow_move->home (17-18 fit · 5-5 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->home (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd); pin_value->away (2-7 fit · 1-3 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | spread | home **SPLIT** | +38 | 3-2 | -3 (-115) | -2 | 1 | -3 ($10,000) |  |  | 68% / 66% | 3281 | follow_move->home (16-21 fit · 5-6 fwd); money_level->home (25-17 fit · 3-8 fwd); sharp_gap->away (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd); consensus_gap->home (5-3 fit · 0-2 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | moneyline | away **SPLIT** | +32.3 | 3-2 | -210 (-210) | -205 | 0.5 | -194 ($6,000) |  |  | 85% / 86% | 1751 | follow_move->away (17-18 fit · 5-5 fwd); money_level->away (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->home (13-30 fit · 4-8 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | moneyline | home **SPLIT** | +26.4 | 4-3 | -154 (-154) | -148 | 1 | -161 ($5,000) |  |  | 72% / 76% | 2726 | money_delta->away (4-5 fit · 1-1 fwd); follow_move->home (17-18 fit · 5-5 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->home (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd); pin_move->home (15-11 fit · 4-5 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | moneyline | away **SPLIT** | +20.4 | 4-2 | -340 (-340) | -330 | 0.7 | -300 ($6,000) |  |  | 95% / 96% | 2473 | follow_move->away (17-18 fit · 5-5 fwd); money_level->away (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->home (13-30 fit · 4-8 fwd); pin_value->home (2-7 fit · 1-3 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | moneyline | home | +34.3 | 1-1 | -1200 (-1200) | -1200 |  | -1096 ($6,000) |  |  | 98% / 98% | 2610 | money_level->home (35-7 fit · 8-4 fwd); consensus_gap->away (13-30 fit · 4-8 fwd) |

## B  weighted ROI +10% to +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Baltimore Ravens @ Houston Texans | moneyline | home **SPLIT** | +12.5 | 3-2 | -335 (-335) | -330 | 0.3 | -310 ($6,000) |  |  | 94% / 92% | 2897 | follow_move->home (17-18 fit · 5-5 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | spread | away | +16.3 | 4-1 | 1.5 (-115) | 3.5 | 2 | 1 ($5,000) | +0.5 |  | 65% / 59% | 2413 | follow_move->away (16-21 fit · 5-6 fwd); money_level->away (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd); pin_value->away (16-3 fit · 2-3 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | spread | away | +11.7 | 6-0 | -7 (-115) | -7 |  | -7.5 ($5,000) | +0.5 |  | 82% / 83% | 1544 | money_level->away (25-17 fit · 3-8 fwd); sharp_gap->away (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd); consensus_gap->away (5-3 fit · 0-2 fwd); book_lag->away (4-0 fit · 0-0 fwd); pin_value->away (16-3 fit · 2-3 fwd) |

## C  weighted ROI 0 to +10%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | moneyline | away **SPLIT** | +8.4 | 4-2 | -154 (-154) | -142 | 2 | -151 ($10,000) |  |  | 86% / 73% | 7254 | follow_move->away (17-18 fit · 5-5 fwd); money_level->away (35-7 fit · 8-4 fwd); sharp_gap->home (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->home (13-30 fit · 4-8 fwd); pin_move->away (15-11 fit · 4-5 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | moneyline | away **SPLIT** | +5.2 | 3-2 | -104 (-104) | -104 |  | -104 ($3,000) |  |  | 57% / 64% | 2413 | money_level->away (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd); book_lag->home (1-1 fit · 0-0 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | spread | away | +8.8 | 3-1 | 2.5 (-100) | 2.5 |  | 2.5 ($20,000) |  |  | 58% / 62% | 12621 | money_level->away (25-17 fit · 3-8 fwd); sharp_gap->away (17-25 fit · 7-5 fwd); money_moving->home (10-21 fit · 5-7 fwd); pin_move->away (8-10 fit · 3-4 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | spread | away | +5 | 3-1 | -2.5 (-120) | -1.5 | 1 | -2.5 ($20,000) |  |  | 74% / 79% | 7254 | follow_move->away (16-21 fit · 5-6 fwd); money_level->away (25-17 fit · 3-8 fwd); sharp_gap->away (17-25 fit · 7-5 fwd); money_moving->home (10-21 fit · 5-7 fwd) |
| Wed 20:00 | Green Bay Packers @ Los Angeles Rams | tt_home | over | +4.6 | 1-0 | 23.5 (-100) | 23.5 |  | 24.5 ($3,000) | -1 |  | 0% / 0% | 15348 | pin_value->over (17-12 fit · 2-4 fwd) |
| Thu 13:00 | Chicago Bears @ Detroit Lions | tt_home | over | +4.6 | 1-0 | 26.5 (-125) | 26.5 |  | 27.5 ($2,000) | -1 |  | 0% / 0% | 12586 | pin_value->over (17-12 fit · 2-4 fwd) |
| Thu 16:30 | Philadelphia Eagles @ Dallas Cowboys | tt_home | under | +4.6 | 1-0 | 29.5 (-113) | 29.5 |  | 28.5 ($2,000) | -1 |  | 0% / 0% | 8552 | pin_value->under (17-12 fit · 2-4 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | tt_home | over | +4.6 | 1-0 | 17.5 (-102) | 17.5 |  | 18.5 ($2,000) | -1 |  | 0% / 0% | 7254 | pin_value->over (17-12 fit · 2-4 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | moneyline | home | +3.9 | 4-1 | -335 (-335) | -310 | 1.4 | -317 ($6,000) |  |  | 98% / 99% | 2701 | follow_move->home (17-18 fit · 5-5 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->home (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | tt_away | under | +2 | 1-1 | 22.5 (-100) | 23.5 | 1 | 23.5 ($2,000) | +1 |  | 0% / 0% | 12621 | follow_move->under (9-7 fit · 5-1 fwd); pin_value->over (14-12 fit · 2-6 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | tt_away | under | +2 | 1-1 | 22.5 (-111) | 23.5 | 1 | 23.5 ($2,000) | +1 |  | 0% / 0% | 1751 | follow_move->under (9-7 fit · 5-1 fwd); pin_value->over (14-12 fit · 2-6 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | tt_away | under | +2 | 1-1 | 20.5 (-111) | 21.5 | 1 | 21.5 ($2,000) | +1 |  | 0% / 0% | 3281 | follow_move->under (9-7 fit · 5-1 fwd); pin_value->over (14-12 fit · 2-6 fwd) |
| Wed 20:00 | Green Bay Packers @ Los Angeles Rams | tt_away | over | +0.3 | 1-0 | 20.5 (-120) | 20.5 |  | 21.5 ($3,000) | -1 |  | 0% / 0% | 15348 | pin_value->over (14-12 fit · 2-6 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | tt_away | over | +0.3 | 1-0 | 19.5 (-125) | 19.5 |  | 20.5 ($2,000) | -1 |  | 0% / 0% | 7254 | pin_value->over (14-12 fit · 2-6 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | tt_away | over | +0.3 | 1-0 | 19.5 (-128) | 19.5 |  | 20.5 ($2,000) | -1 |  | 0% / 0% | 1827 | pin_value->over (14-12 fit · 2-6 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | tt_away | under | +0.3 | 1-0 | 17.5 (-130) | 17.5 |  | 16.5 ($2,000) | -1 |  | 0% / 0% | 2701 | pin_value->under (14-12 fit · 2-6 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | tt_away | under | +0.3 | 1-0 | 16.5 (-106) | 16.5 |  | 15.5 ($2,000) | -1 |  | 0% / 0% | 2610 | pin_value->under (14-12 fit · 2-6 fwd) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | New York Jets @ Miami Dolphins | total | over **SPLIT** | -1.7 | 4-3 | 40.5 (-110) | 41.5 | 1 | 41 ($3,000) | -0.5 | over 80% | 80% / 81% | 1751 | follow_move->under (10-9 fit · 8-2 fwd); rlm->under (4-5 fit · 4-1 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->over (21-22 fit · 5-6 fwd); money_moving->over (15-18 fit · 6-6 fwd); pin_value->over (12-11 fit · 4-2 fwd) |
| Fri 15:00 | Denver Broncos @ Pittsburgh Steelers | total | under **SPLIT** | -3.2 | 5-2 | 37.5 (-115) | 37.5 |  | 37 ($5,000) | -0.5 |  | 23% / 31% | 7254 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->over (15-18 fit · 6-6 fwd); pin_value->under (12-11 fit · 4-2 fwd); pin_move->under (14-13 fit · 10-2 fwd); pin_rlm->under (3-1 fit · 0-0 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | total | under **SPLIT** | -5.3 | 3-2 | 42.5 (-120) | 42.5 |  | 42 ($3,000) | -0.5 |  | 18% / 22% | 2473 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->over (15-18 fit · 6-6 fwd); pin_value->under (12-11 fit · 4-2 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | total | under **SPLIT** | -16.9 | 3-3 | 48.5 (-115) | 47.5 | 1 | 47.5 ($3,000) | -1 |  | 27% / 24% | 2610 | money_delta->under (4-7 fit · 2-3 fwd); follow_move->over (10-9 fit · 8-2 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->over (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd); pin_value->under (12-11 fit · 4-2 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | spread | home **SPLIT** | -21.2 | 2-2 | -7 (-105) | -7 |  | -7 ($10,000) |  |  | 87% / 89% | 2701 | money_level->home (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); consensus_gap->away (5-3 fit · 0-2 fwd); book_lag->away (4-0 fit · 0-0 fwd) |
| Thu 13:00 | Chicago Bears @ Detroit Lions | spread | away **SPLIT** | -25.4 | 2-2 | -2.5 (-112) | 2.5 | 5 | -2.5 ($20,000) |  |  | 58% / 43% | 12586 | follow_move->away (16-21 fit · 5-6 fwd); money_level->home (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | moneyline | away **SPLIT** | -48.3 | 4-2 | 146 (+146) | 144 | 0.3 | 153 ($6,000) |  |  | 8% / 11% | 3281 | follow_move->home (17-18 fit · 5-5 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd); pin_rlm->away (2-7 fit · 0-2 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | moneyline | home **SPLIT** | -48.6 | 4-2 | 300 (+300) | 300 |  | 288 ($3,000) |  |  | 3% / 6% | 1544 | pre_move->home (1-3 fit · 0-2 fwd); money_level->away (35-7 fit · 8-4 fwd); sharp_gap->home (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->home (13-30 fit · 4-8 fwd); pin_rlm->home (2-7 fit · 0-2 fwd) |
| Thu 13:00 | Chicago Bears @ Detroit Lions | moneyline | home **SPLIT** | -56.1 | 3-2 | 120 (+120) | 124 | 0.8 | 119 ($10,000) **retraced +1** |  |  | 52% / 37% | 12586 | follow_move->home (17-18 fit · 5-5 fwd); money_level->away (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->home (13-30 fit · 4-8 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | spread | away **SPLIT** | -72.5 | 3-3 | 9.5 (-100) | 10 | 0.5 | 10 ($5,000) | -0.5 | home 88% | 12% / 12% | 1827 | follow_move->away (16-21 fit · 5-6 fwd); rlm->away (1-11 fit · 3-2 fwd); rlm_quiet->away (1-9 fit · 3-2 fwd); money_level->home (25-17 fit · 3-8 fwd); money_moving->home (10-21 fit · 5-7 fwd); pin_value->home (16-3 fit · 2-3 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | moneyline | away **SPLIT** | -77.1 | 7-2 | 128 (+128) | 132 | 0.6 | 128 ($10,000) **retraced +2.5** |  | home 80% | 20% / 37% | 12621 | follow_move->away (17-18 fit · 5-5 fwd); rlm->away (4-16 fit · 1-2 fwd); rlm_ratio->away (3-7 fit · 0-1 fwd); rlm_quiet->away (2-15 fit · 1-2 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->home (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd); pin_rlm->away (2-7 fit · 0-2 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | spread | home **SPLIT** | -85.8 | 5-3 | -3 (-100) | -2.5 | 0.5 | -3 ($10,000) |  | away 62% | 38% / 36% | 2726 | follow_move->home (16-21 fit · 5-6 fwd); rlm->home (1-11 fit · 3-2 fwd); rlm_quiet->home (1-9 fit · 3-2 fwd); money_level->away (25-17 fit · 3-8 fwd); sharp_gap->away (17-25 fit · 7-5 fwd); money_moving->home (10-21 fit · 5-7 fwd); consensus_gap->away (5-3 fit · 0-2 fwd); pin_move->home (8-10 fit · 3-4 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | total | over | -0.5 | 3-1 | 41.5 (-105) | 41.5 |  | 41.5 ($3,000) |  |  | 76% / 74% | 2251 | money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->over (15-18 fit · 6-6 fwd); pin_move->over (14-13 fit · 10-2 fwd) |
| Thu 13:00 | Chicago Bears @ Detroit Lions | total | under | -1.2 | 2-0 | 55.5 (-115) | 55.5 |  | 55.5 ($5,000) |  |  | 84% / 88% | 12586 | money_level->under (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | total | over | -1.2 | 2-0 | 50.5 (-110) | 50.5 |  | 50.5 ($3,000) |  |  | 59% / 70% | 1827 | money_level->over (23-19 fit · 6-6 fwd); sharp_gap->over (21-22 fit · 5-6 fwd) |
| Sun 16:05 | New England Patriots @ Los Angeles Chargers | total | over | -1.2 | 2-0 | 35.5 (-112) | 35.5 |  | 35.5 ($3,000) |  |  | 85% / 87% | 2413 | money_level->over (23-19 fit · 6-6 fwd); sharp_gap->over (21-22 fit · 5-6 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | total | under | -1.5 | 4-0 | 47.5 (-110) | 48.5 | 1 | 47.5 ($5,000) |  |  | 72% / 84% | 12621 | follow_move->under (10-9 fit · 8-2 fwd); money_level->under (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); pin_move->under (14-13 fit · 10-2 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | spread | away | -1.8 | 2-0 | 4.5 (-105) | 5 | 0.5 | 4.5 ($10,000) |  |  | 65% / 65% | 2251 | follow_move->away (16-21 fit · 5-6 fwd); money_level->away (25-17 fit · 3-8 fwd) |
| Thu 16:30 | Philadelphia Eagles @ Dallas Cowboys | total | under | -2.3 | 3-0 | 48.5 (-115) | 48.5 |  | 47.5 ($5,000) | -1 |  | 93% / 94% | 8552 | money_level->under (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); pin_value->under (12-11 fit · 4-2 fwd) |
| Sun 16:25 | Washington Commanders @ Arizona Cardinals | total | over | -4.3 | 2-0 | 41.5 (-110) | 41.5 |  | 41.5 ($3,000) |  |  | 82% / 82% | 1544 | money_level->over (23-19 fit · 6-6 fwd); money_moving->over (15-18 fit · 6-6 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | tt_home | under | -4.6 | 1-0 | 17.5 (-113) | 18.5 | 1 | 17.5 ($2,000) |  |  | 0% / 0% | 1751 | follow_move->under (9-10 fit · 3-2 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | tt_home | over | -4.6 | 1-0 | 27.5 (-100) | 26.5 | 1 | 27.5 ($2,000) |  |  | 0% / 0% | 2897 | follow_move->over (9-10 fit · 3-2 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | tt_home | over | -4.6 | 1-0 | 31.5 (-100) | 30.5 | 1 | 31.5 ($2,000) |  |  | 0% / 0% | 2610 | follow_move->over (9-10 fit · 3-2 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | tt_home | over | -4.6 | 1-0 | 23.5 (-106) | 22.5 | 1 | 23.5 ($2,000) |  |  | 0% / 0% | 2726 | follow_move->over (9-10 fit · 3-2 fwd) |
| Thu 20:20 | Kansas City Chiefs @ Buffalo Bills | tt_home | under | -9.2 | 1-1 | 24.5 (-113) | 25.5 | 1 | 26.5 ($2,000) | +2 |  | 0% / 0% | 12621 | follow_move->under (9-10 fit · 3-2 fwd); pin_value->over (17-12 fit · 2-4 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | tt_home | under | -9.2 | 1-1 | 23.5 (+102) | 24.5 | 1 | 24.5 ($2,000) | +1 |  | 0% / 0% | 3281 | follow_move->under (9-10 fit · 3-2 fwd); pin_value->over (17-12 fit · 2-4 fwd) |
| Wed 20:00 | Green Bay Packers @ Los Angeles Rams | total | under | -9.3 | 4-0 | 44.5 (-120) | 44.5 |  | 44.5 ($5,000) |  |  | 92% / 95% | 15348 | money_level->under (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd); pin_move->under (14-13 fit · 10-2 fwd) |
| Wed 20:00 | Green Bay Packers @ Los Angeles Rams | spread | away | -15 | 4-1 | 2.5 (-108) | 3.5 | 1 | 2.5 ($20,000) |  |  | 56% / 52% | 15348 | follow_move->away (16-21 fit · 5-6 fwd); money_level->away (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->away (10-21 fit · 5-7 fwd); pin_move->away (8-10 fit · 3-4 fwd) |
| Sun 13:00 | Atlanta Falcons @ Minnesota Vikings | total | under | -16.2 | 3-1 | 42.5 (-110) | 42.5 |  | 41.5 ($3,000) | -1 |  | 36% / 40% | 2701 | money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd); pin_value->under (12-11 fit · 4-2 fwd) |
| Mon 20:15 | Carolina Panthers @ Tampa Bay Buccaneers | total | under | -19.2 | 3-1 | 43.5 (-105) | 43.5 |  | 43.5 ($5,000) |  |  | 16% / 21% | 2726 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd) |
| Sun 16:25 | Seattle Seahawks @ San Francisco 49ers | total | under | -20.5 | 6-1 | 45.5 (-115) | 46.5 | 1 | 45 ($3,000) | -0.5 | over 82% | 18% / 18% | 3281 | follow_move->under (10-9 fit · 8-2 fwd); rlm->under (4-5 fit · 4-1 fwd); rlm_quiet->under (3-4 fit · 4-1 fwd); money_level->over (23-19 fit · 6-6 fwd); money_moving->under (15-18 fit · 6-6 fwd); pin_value->under (12-11 fit · 4-2 fwd); pin_move->under (14-13 fit · 10-2 fwd) |
| Sun 13:00 | Tennessee Titans @ Jacksonville Jaguars | spread | home | -23.4 | 3-0 | -14.5 (-105) | -14 | 0.5 | -14.5 ($10,000) |  |  | 87% / 87% | 2610 | follow_move->home (16-21 fit · 5-6 fwd); money_level->home (25-17 fit · 3-8 fwd); money_moving->home (10-21 fit · 5-7 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | total | under | -24.3 | 3-1 | 46.5 (-105) | 46.5 |  | 46.5 ($3,000) |  |  | 26% / 29% | 2897 | money_delta->under (4-7 fit · 2-3 fwd); money_level->over (23-19 fit · 6-6 fwd); sharp_gap->under (21-22 fit · 5-6 fwd); money_moving->under (15-18 fit · 6-6 fwd) |
| Sun 13:00 | Baltimore Ravens @ Houston Texans | spread | home | -28 | 3-0 | -6.5 (-115) | -6.5 |  | -6.5 ($10,000) |  |  | 61% / 62% | 2897 | money_level->home (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->home (10-21 fit · 5-7 fwd) |
| Sun 13:00 | New Orleans Saints @ Cincinnati Bengals | moneyline | away | -38.9 | 3-1 | 440 (+440) | 430 |  | 421 ($3,000) |  |  | 2% / 4% | 1827 | pre_move->away (1-3 fit · 0-2 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); consensus_gap->away (13-30 fit · 4-8 fwd) |
| Thu 16:30 | Philadelphia Eagles @ Dallas Cowboys | spread | home | -41.8 | 2-1 | -8.5 (-110) | -1.5 | 7 | -8.5 ($20,000) |  |  | 41% / 41% | 8552 | follow_move->home (16-21 fit · 5-6 fwd); rlm_quiet->home (1-9 fit · 3-2 fwd); money_level->away (25-17 fit · 3-8 fwd) |
| Wed 20:00 | Green Bay Packers @ Los Angeles Rams | moneyline | away | -52.7 | 6-1 | 120 (+120) | 120 |  | 119 ($10,000) **retraced +1.5** |  |  | 21% / 45% | 15348 | pre_move->away (1-3 fit · 0-2 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd); pin_move->away (15-11 fit · 4-5 fwd); pin_rlm->away (2-7 fit · 0-2 fwd) |
| Sun 20:20 | Las Vegas Raiders @ Cleveland Browns | moneyline | away | -53.1 | 4-1 | 198 (+198) | 198 |  | 195 ($6,000) |  |  | 22% / 47% | 2251 | pre_move->away (1-3 fit · 0-2 fwd); money_level->home (35-7 fit · 8-4 fwd); sharp_gap->away (21-19 fit · 3-9 fwd); money_moving->away (14-19 fit · 5-6 fwd); consensus_gap->away (13-30 fit · 4-8 fwd) |
| Sun 13:00 | New York Jets @ Miami Dolphins | spread | home | -69.2 | 3-1 | 3.5 (-100) | 4 | 0.5 | 3.5 ($10,000) |  | away 64% | 36% / 36% | 1751 | follow_move->home (16-21 fit · 5-6 fwd); rlm->home (1-11 fit · 3-2 fwd); rlm_quiet->home (1-9 fit · 3-2 fwd); money_level->away (25-17 fit · 3-8 fwd) |
| Sun 13:00 | New York Giants @ Indianapolis Colts | spread | home | -105.6 | 5-1 | 6.5 (-105) | 7 | 0.5 | 6.5 ($10,000) |  | away 87% | 13% / 14% | 2473 | follow_move->home (16-21 fit · 5-6 fwd); rlm->home (1-11 fit · 3-2 fwd); rlm_quiet->home (1-9 fit · 3-2 fwd); money_level->away (25-17 fit · 3-8 fwd); sharp_gap->home (17-25 fit · 7-5 fwd); money_moving->home (10-21 fit · 5-7 fwd) |

