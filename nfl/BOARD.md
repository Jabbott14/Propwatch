# NFL board

Generated 2026-11-20 12:06 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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

| tier | game | market | side | book | moved | FD now | tickets | money/tix | record |
|---|---|---|---|---|---|---|---|---|---|
| PINNACLE moved vs public | Miami Dolphins @ Buffalo Bills | total | under | Pinnacle | 47 -> 44.5 | 44.5 | 22% | 1.91 | 5-10 fit · 0-0 fwd |
| PINNACLE moved vs public | Miami Dolphins @ Buffalo Bills | moneyline | away | Pinnacle | 889 -> 879 | 900 | 1% | 5.0 | 5-10 fit · 0-0 fwd |
| FanDuel moved vs public | Miami Dolphins @ Buffalo Bills | spread | away | FanDuel | 17 -> 16.5 | 16.5 | 29% | 1.21 | 5-14 fit · 1-0 fwd |
| FanDuel moved vs public | Miami Dolphins @ Buffalo Bills | total | under | FanDuel | 45.5 -> 44.5 | 44.5 | 22% | 1.91 | 5-14 fit · 1-0 fwd |
| FanDuel moved vs public | Miami Dolphins @ Buffalo Bills | moneyline | away | FanDuel | 980 -> 900 | 900 | 1% | 5.0 | 5-14 fit · 1-0 fwd |
| line moved off the public (no ratio test) | Jacksonville Jaguars @ New York Giants | spread | home | FanDuel | 6.5 -> 5.5 | 5.5 | 12% | 1.17 | 8-32 fit · 1-0 fwd |
| line moved off the public (no ratio test) | Tampa Bay Buccaneers @ Detroit Lions | total | under | FanDuel | 46.5 -> 45.5 | 45.5 | 18% | 0.67 | 8-32 fit · 1-0 fwd |
| line moved off the public (no ratio test) | Tennessee Titans @ Dallas Cowboys | spread | away | FanDuel | 8 -> 7.5 | 7.5 | 34% | 0.97 | 8-32 fit · 1-0 fwd |

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
before 2026-11-17, so a good number there proves nothing) and `fwd` (games
since, which it had no hand in choosing). A `*` means the weight came from the
forward record, which happens once that record reaches 30 decided
outcomes. No asterisk means the lean rests on fitted numbers only.

## A  weighted ROI >= +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | spread | home **SPLIT** | +80.5 | 4-3 | -7.5 (-115) | -8 | 0.5 | -8 ($20,000) | +0.5 | home 66% | 66% / 67% | 12015 | follow_move->away (15-20 fit · 1-1 fwd); rlm->away (1-11 fit · 0-0 fwd); money_level->home (24-16 fit · 1-1 fwd); sharp_gap->home (16-24 fit · 1-1 fwd); money_moving->away (9-20 fit · 1-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd); pin_value->home (15-3 fit · 1-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | spread | away **SPLIT** | +35.7 | 2-2 | -6.5 (-105) | -4 | 2.5 | -6.5 ($10,000) |  |  | 83% / 80% | 7966 | follow_move->away (15-20 fit · 1-1 fwd); money_level->away (24-16 fit · 1-1 fwd); sharp_gap->home (16-24 fit · 1-1 fwd); money_moving->home (9-20 fit · 1-1 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | moneyline | home **SPLIT** | +23.7 | 3-3 | -590 (-590) | -550 | 0.9 | -542 ($10,000) |  |  | 97% / 92% | 9940 | follow_move->home (15-18 fit · 2-0 fwd); money_level->home (34-6 fit · 1-1 fwd); sharp_gap->away (20-18 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->away (12-29 fit · 1-1 fwd); pin_value->away (2-6 fit · 0-1 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | spread | home | +54.1 | 5-1 | -9.5 (-120) | -9.5 |  | -10.5 ($20,000) | +1 |  | 68% / 69% | 9940 | money_level->home (24-16 fit · 1-1 fwd); sharp_gap->home (16-24 fit · 1-1 fwd); money_moving->away (9-20 fit · 1-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd); book_lag->home (4-0 fit · 0-0 fwd); pin_value->home (15-3 fit · 1-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | spread | home | +20.6 | 2-1 | -2.5 (-115) | -2 | 0.5 | -2.5 ($20,000) |  |  | 66% / 66% | 8098 | follow_move->home (15-20 fit · 1-1 fwd); money_level->home (24-16 fit · 1-1 fwd); money_moving->away (9-20 fit · 1-1 fwd) |

## B  weighted ROI +10% to +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | New Orleans Saints @ Chicago Bears | moneyline | home **SPLIT** | +17.8 | 3-2 | -770 (-770) | -670 | 1.5 | -582 ($10,000) |  |  | 98% / 98% | 13111 | follow_move->home (15-18 fit · 2-0 fwd); money_level->home (34-6 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->away (12-29 fit · 1-1 fwd); pin_value->away (2-6 fit · 0-1 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | total | under **SPLIT** | +17.5 | 2-2 | 46.5 (-105) | 46.5 |  | 46 ($3,000) | -0.5 |  | 88% / 86% | 11394 | money_level->under (22-18 fit · 1-1 fwd); sharp_gap->over (19-22 fit · 2-0 fwd); money_moving->over (14-17 fit · 1-1 fwd); pin_value->under (11-10 fit · 1-1 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | moneyline | home | +19.7 | 2-1 | -260 (-260) | -260 |  | -256 ($10,000) |  |  | 96% / 96% | 12419 | money_level->home (34-6 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->away (12-29 fit · 1-1 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | spread | home | +18.1 | 5-1 | -15.5 (-115) | -15 | 0.5 | -16.5 ($10,000) | +1 |  | 62% / 58% | 9097 | follow_move->home (15-20 fit · 1-1 fwd); money_level->home (24-16 fit · 1-1 fwd); sharp_gap->away (16-24 fit · 1-1 fwd); money_moving->home (9-20 fit · 1-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd); pin_value->home (15-3 fit · 1-0 fwd) |

## C  weighted ROI 0 to +10%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | moneyline | home **SPLIT** | +9.8 | 3-2 | -168 (-168) | -164 | 0.6 | -174 ($10,000) |  |  | 85% / 72% | 11394 | follow_move->home (15-18 fit · 2-0 fwd); money_level->home (34-6 fit · 1-1 fwd); sharp_gap->away (20-18 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->away (12-29 fit · 1-1 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | total | over **SPLIT** | +4.5 | 2-2 | 38.5 (-105) | 38.5 |  | 37.5 ($3,000) | +1 |  | 81% / 82% | 7436 | money_level->over (22-18 fit · 1-1 fwd); sharp_gap->over (19-22 fit · 2-0 fwd); money_moving->under (14-17 fit · 1-1 fwd); pin_value->under (11-10 fit · 1-1 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | total | over | +3.4 | 1-0 | 48.5 (-115) | 48.5 |  | 48.5 ($3,000) |  |  | 63% / 63% | 13111 | money_level->over (22-18 fit · 1-1 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | total | over | +3.1 | 2-1 | 43.5 (-110) | 43.5 |  | 43.5 ($3,000) |  |  | 74% / 69% | 8098 | money_level->over (22-18 fit · 1-1 fwd); sharp_gap->under (19-22 fit · 2-0 fwd); money_moving->over (14-17 fit · 1-1 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | total | under | +2.4 | 6-1 | 44.5 (-105) | 45.5 | 1 | 44.5 ($3,000) |  | over 78% | 22% / 42% | 9582 | follow_move->under (9-9 fit · 1-0 fwd); rlm->under (4-5 fit · 0-0 fwd); rlm_ratio->under (3-1 fit · 0-0 fwd); money_level->over (22-18 fit · 1-1 fwd); sharp_gap->under (19-22 fit · 2-0 fwd); money_moving->under (14-17 fit · 1-1 fwd); pin_rlm->under (3-1 fit · 0-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | tt_away | over | +2.3 | 1-0 | 18.5 (-111) | 18.5 |  | 19.5 ($2,000) | -1 |  | 0% / 0% | 13111 | pin_value->over (14-11 fit · 0-1 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | tt_away | under | +2.3 | 1-0 | 19.5 (+102) | 19.5 |  | 18.5 ($2,000) | -1 |  | 0% / 0% | 6149 | pin_value->under (14-11 fit · 0-1 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | tt_away | under | +2.3 | 1-0 | 30.5 (-113) | 30.5 |  | 29.5 ($1,000) | -1 |  | 0% / 0% | 7966 | pin_value->under (14-11 fit · 0-1 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | tt_home | over | +1.4 | 1-0 | 30.5 (-115) | 30.5 |  | 31.5 ($2,000) | -1 |  | 0% / 0% | 9582 | pin_value->over (15-12 fit · 2-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | tt_home | under | +1.4 | 1-0 | 30.5 (-108) | 30.5 |  | 29.5 ($2,000) | -1 |  | 0% / 0% | 13111 | pin_value->under (15-12 fit · 2-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | total | over | +1.2 | 3-1 | 41.5 (-120) | 40.5 | 1 | 41.5 ($3,000) |  |  | 62% / 57% | 6149 | follow_move->over (9-9 fit · 1-0 fwd); money_level->over (22-18 fit · 1-1 fwd); sharp_gap->under (19-22 fit · 2-0 fwd); money_moving->over (14-17 fit · 1-1 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | total | over | +1 | 4-1 | 53.5 (-115) | 52.5 | 1 | 54 ($3,000) | -0.5 |  | 60% / 73% | 7966 | follow_move->over (9-9 fit · 1-0 fwd); money_level->over (22-18 fit · 1-1 fwd); sharp_gap->over (19-22 fit · 2-0 fwd); money_moving->under (14-17 fit · 1-1 fwd); pin_value->over (11-10 fit · 1-1 fwd) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | total | under **SPLIT** | -10.6 | 4-2 | 45.5 (-105) | 46.5 | 1 | 45 ($3,000) | -0.5 | over 82% | 18% / 12% | 12419 | follow_move->under (9-9 fit · 1-0 fwd); rlm->under (4-5 fit · 0-0 fwd); money_level->over (22-18 fit · 1-1 fwd); sharp_gap->over (19-22 fit · 2-0 fwd); money_moving->under (14-17 fit · 1-1 fwd); pin_value->under (11-10 fit · 1-1 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | spread | away **SPLIT** | -12.1 | 3-2 | 3 (-100) | 3.5 | 0.5 | 3 ($20,000) |  |  | 60% / 54% | 11394 | follow_move->away (15-20 fit · 1-1 fwd); money_level->away (24-16 fit · 1-1 fwd); sharp_gap->home (16-24 fit · 1-1 fwd); money_moving->away (9-20 fit · 1-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | moneyline | away **SPLIT** | -25.9 | 3-2 | 870 (+870) | 870 |  | 862 ($5,000) |  |  | 2% / 13% | 9097 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 1-1 fwd); sharp_gap->away (20-18 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->away (12-29 fit · 1-1 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | moneyline | away **SPLIT** | -30.3 | 3-2 | 134 (+134) | 134 |  | 151 ($10,000) |  |  | 25% / 34% | 6149 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 1-1 fwd); sharp_gap->away (20-18 fit · 1-1 fwd); consensus_gap->away (12-29 fit · 1-1 fwd); pin_value->home (2-6 fit · 0-1 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | spread | away **SPLIT** | -32.3 | 3-2 | 6.5 (-120) | 5.5 | 1 | 6.5 ($10,000) |  |  | 28% / 32% | 12419 | follow_move->home (15-20 fit · 1-1 fwd); money_level->home (24-16 fit · 1-1 fwd); sharp_gap->away (16-24 fit · 1-1 fwd); money_moving->away (9-20 fit · 1-1 fwd); consensus_gap->away (5-3 fit · 0-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | moneyline | away **SPLIT** | -39.8 | 4-2 | 350 (+350) | 350 |  | 313 ($10,000) |  |  | 4% / 6% | 12015 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 1-1 fwd); sharp_gap->away (20-18 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->away (12-29 fit · 1-1 fwd); pin_value->away (2-6 fit · 0-1 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | moneyline | away **SPLIT** | -52 | 6-2 | 900 (+900) | 980 | 0.6 | 879 ($10,000) |  | home 99% | 1% / 5% | 9582 | follow_move->away (15-18 fit · 2-0 fwd); rlm->away (3-16 fit · 1-0 fwd); rlm_ratio->away (2-7 fit · 1-0 fwd); money_level->home (34-6 fit · 1-1 fwd); sharp_gap->away (20-18 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->away (12-29 fit · 1-1 fwd); pin_rlm->away (2-7 fit · 0-0 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | spread | away **SPLIT** | -82.3 | 4-3 | 16.5 (-110) | 17 | 0.5 | 17 ($20,000) | -0.5 | home 71% | 29% / 35% | 9582 | follow_move->away (15-20 fit · 1-1 fwd); rlm->away (1-11 fit · 0-0 fwd); rlm_ratio->away (0-6 fit · 0-0 fwd); money_level->home (24-16 fit · 1-1 fwd); sharp_gap->away (16-24 fit · 1-1 fwd); money_moving->home (9-20 fit · 1-1 fwd); pin_value->home (15-3 fit · 1-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | spread | home **SPLIT** | -107.3 | 4-2 | 5.5 (-100) | 6.5 | 1 | 6 ($20,000) | -0.5 | away 88% | 12% / 14% | 12137 | follow_move->home (15-20 fit · 1-1 fwd); rlm->home (1-11 fit · 0-0 fwd); money_level->away (24-16 fit · 1-1 fwd); sharp_gap->home (16-24 fit · 1-1 fwd); money_moving->home (9-20 fit · 1-1 fwd); pin_value->away (15-3 fit · 1-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | moneyline | home | -2 | 4-1 | -144 (-144) | -132 | 2.1 | -153 ($10,000) |  |  | 82% / 84% | 8098 | follow_move->home (15-18 fit · 2-0 fwd); money_level->home (34-6 fit · 1-1 fwd); sharp_gap->home (20-18 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->away (12-29 fit · 1-1 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | moneyline | away | -2 | 4-1 | -215 (-215) | -210 | 0.5 | -203 ($10,000) |  |  | 88% / 93% | 7436 | follow_move->away (15-18 fit · 2-0 fwd); money_level->away (34-6 fit · 1-1 fwd); sharp_gap->away (20-18 fit · 1-1 fwd); money_moving->away (12-19 fit · 2-0 fwd); consensus_gap->home (12-29 fit · 1-1 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | moneyline | away | -2 | 4-1 | -260 (-260) | -245 | 1.6 | -259 ($10,000) |  |  | 97% / 99% | 12137 | follow_move->away (15-18 fit · 2-0 fwd); money_level->away (34-6 fit · 1-1 fwd); sharp_gap->away (20-18 fit · 1-1 fwd); money_moving->away (12-19 fit · 2-0 fwd); consensus_gap->home (12-29 fit · 1-1 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | tt_away | under | -2.3 | 1-1 | 19.5 (+104) | 20.5 | 1 | 20.5 ($2,000) | +1 |  | 0% / 0% | 12419 | follow_move->under (8-7 fit · 1-0 fwd); pin_value->over (14-11 fit · 0-1 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | tt_away | under | -2.3 | 1-1 | 13.5 (-100) | 14.5 | 1 | 14.5 ($2,000) | +1 |  | 0% / 0% | 9582 | follow_move->under (8-7 fit · 1-0 fwd); pin_value->over (14-11 fit · 0-1 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | tt_home | under | -4.7 | 1-0 | 19.5 (+102) | 20.5 | 1 | 19.5 ($2,000) |  |  | 0% / 0% | 12137 | follow_move->under (8-9 fit · 1-1 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | total | over | -5 | 3-0 | 40.5 (-110) | 40.5 |  | 41 ($3,000) | -0.5 |  | 76% / 76% | 9940 | money_level->over (22-18 fit · 1-1 fwd); money_moving->over (14-17 fit · 1-1 fwd); pin_value->over (11-10 fit · 1-1 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | tt_home | over | -6.1 | 1-1 | 32.5 (-115) | 31.5 | 1 | 31.5 ($2,000) | +1 |  | 0% / 0% | 12015 | follow_move->over (8-9 fit · 1-1 fwd); pin_value->under (15-12 fit · 2-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | tt_home | over | -6.1 | 1-1 | 22.5 (-120) | 21.5 | 1 | 21.5 ($2,000) | +1 |  | 0% / 0% | 6149 | follow_move->over (8-9 fit · 1-1 fwd); pin_value->under (15-12 fit · 2-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | tt_home | over | -6.1 | 1-1 | 26.5 (-104) | 25.5 | 1 | 24.5 ($2,000) | +2 |  | 0% / 0% | 9940 | follow_move->over (8-9 fit · 1-1 fwd); pin_value->under (15-12 fit · 2-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | spread | home | -8.7 | 3-1 | -11.5 (-110) | -9.5 | 2 | -11.5 ($20,000) |  |  | 82% / 77% | 13111 | follow_move->home (15-20 fit · 1-1 fwd); money_level->home (24-16 fit · 1-1 fwd); sharp_gap->away (16-24 fit · 1-1 fwd); money_moving->home (9-20 fit · 1-1 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | total | over | -12.3 | 4-0 | 54.5 (-120) | 54.5 |  | 55.5 ($3,000) | -1 |  | 71% / 72% | 12015 | money_level->over (22-18 fit · 1-1 fwd); sharp_gap->over (19-22 fit · 2-0 fwd); money_moving->over (14-17 fit · 1-1 fwd); pin_value->over (11-10 fit · 1-1 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | spread | away | -13.4 | 2-0 | -4.5 (-105) | -4.5 |  | -4.5 ($20,000) |  |  | 63% / 63% | 7436 | money_level->away (24-16 fit · 1-1 fwd); money_moving->away (9-20 fit · 1-1 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | total | under | -14.8 | 2-1 | 46.5 (-110) | 46.5 |  | 46.5 ($3,000) |  |  | 13% / 18% | 12137 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-1 fwd); sharp_gap->under (19-22 fit · 2-0 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | total | under | -23.2 | 4-1 | 41.5 (-120) | 41.5 |  | 41 ($3,000) | -0.5 |  | 13% / 25% | 9097 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-1 fwd); sharp_gap->under (19-22 fit · 2-0 fwd); money_moving->under (14-17 fit · 1-1 fwd); pin_value->under (11-10 fit · 1-1 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | spread | away | -31.9 | 3-1 | 3 (-115) | 3 |  | 3 ($10,000) |  |  | 50% / 64% | 6149 | money_level->away (24-16 fit · 1-1 fwd); sharp_gap->away (16-24 fit · 1-1 fwd); money_moving->away (9-20 fit · 1-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | moneyline | home | -56.3 | 2-1 | 235 (+235) | 235 |  | 242 ($10,000) |  |  | 2% / 2% | 7966 | money_level->away (34-6 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->home (12-29 fit · 1-1 fwd) |

