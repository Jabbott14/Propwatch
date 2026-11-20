# NFL board

Generated 2026-11-20 20:40 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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
| PINNACLE moved vs public | Miami Dolphins @ Buffalo Bills | moneyline | away | Pinnacle | 889 -> 879 | 900 | 1% | 5.0 | 5-10 fit · 0-0 fwd |
| FanDuel moved vs public | Miami Dolphins @ Buffalo Bills | moneyline | away | FanDuel | 980 -> 900 | 900 | 1% | 5.0 | 5-14 fit · 1-0 fwd |
| FanDuel moved vs public | Tennessee Titans @ Dallas Cowboys | moneyline | away | FanDuel | 350 -> 320 | 320 | 4% | 1.5 | 5-14 fit · 1-0 fwd |
| line moved off the public (no ratio test) | Arizona Cardinals @ Kansas City Chiefs | spread | home | FanDuel | -15 -> -15.5 | -15.5 | 31% | 0.97 | 8-32 fit · 1-0 fwd |
| line moved off the public (no ratio test) | Jacksonville Jaguars @ New York Giants | spread | home | FanDuel | 6.5 -> 5.5 | 5.5 | 28% | 1.04 | 8-32 fit · 1-0 fwd |
| line moved off the public (no ratio test) | Miami Dolphins @ Buffalo Bills | total | under | FanDuel | 45.5 -> 44.5 | 44.5 | 27% | 0.89 | 8-32 fit · 1-0 fwd |
| line moved off the public (no ratio test) | Pittsburgh Steelers @ Philadelphia Eagles | total | under | FanDuel | 38.5 -> 37.5 | 37.5 | 21% | 1.1 | 8-32 fit · 1-0 fwd |
| line moved off the public (no ratio test) | Pittsburgh Steelers @ Philadelphia Eagles | moneyline | home | FanDuel | 176 -> 172 | 172 | 11% | 0.64 | 8-32 fit · 1-0 fwd |
| line moved off the public (no ratio test) | Tampa Bay Buccaneers @ Detroit Lions | moneyline | away | FanDuel | 215 -> 194 | 194 | 4% | 1.0 | 8-32 fit · 1-0 fwd |

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
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | spread | home **SPLIT** | +35.7 | 2-2 | -2.5 (-116) | -2 | 0.5 | -2.5 ($20,000) |  |  | 70% / 69% | 8860 | follow_move->home (15-20 fit · 1-1 fwd); money_level->home (24-16 fit · 1-1 fwd); sharp_gap->away (16-24 fit · 1-1 fwd); money_moving->away (9-20 fit · 1-1 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | spread | away **SPLIT** | +35.7 | 2-2 | -6.5 (-105) | -4 | 2.5 | -6.5 ($10,000) |  |  | 77% / 63% | 8754 | follow_move->away (15-20 fit · 1-1 fwd); money_level->away (24-16 fit · 1-1 fwd); sharp_gap->home (16-24 fit · 1-1 fwd); money_moving->home (9-20 fit · 1-1 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | spread | home **SPLIT** | +29.7 | 3-2 | -3 (-120) | -3.5 | 0.5 | -3 ($20,000) |  |  | 31% / 61% | 12470 | follow_move->away (15-20 fit · 1-1 fwd); money_level->home (24-16 fit · 1-1 fwd); sharp_gap->home (16-24 fit · 1-1 fwd); money_moving->away (9-20 fit · 1-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | moneyline | home **SPLIT** | +23.7 | 3-3 | -1800 (-1800) | -1500 | 1 | -1352 ($5,000) |  |  | 98% / 88% | 10016 | follow_move->home (15-18 fit · 2-0 fwd); money_level->home (34-6 fit · 1-1 fwd); sharp_gap->away (20-18 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->away (12-29 fit · 1-1 fwd); pin_value->away (2-6 fit · 0-1 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | moneyline | home **SPLIT** | +23.7 | 3-3 | -590 (-590) | -550 | 0.9 | -542 ($10,000) |  |  | 97% / 92% | 10647 | follow_move->home (15-18 fit · 2-0 fwd); money_level->home (34-6 fit · 1-1 fwd); sharp_gap->away (20-18 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->away (12-29 fit · 1-1 fwd); pin_value->away (2-6 fit · 0-1 fwd) |

## B  weighted ROI +10% to +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | New Orleans Saints @ Chicago Bears | moneyline | home **SPLIT** | +17.8 | 3-2 | -750 (-750) | -670 | 1.2 | -582 ($10,000) |  |  | 98% / 98% | 14595 | follow_move->home (15-18 fit · 2-0 fwd); money_level->home (34-6 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->away (12-29 fit · 1-1 fwd); pin_value->away (2-6 fit · 0-1 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | total | under **SPLIT** | +17.5 | 2-2 | 46.5 (-105) | 46.5 |  | 46 ($3,000) | -0.5 |  | 89% / 87% | 12470 | money_level->under (22-18 fit · 1-1 fwd); sharp_gap->over (19-22 fit · 2-0 fwd); money_moving->over (14-17 fit · 1-1 fwd); pin_value->under (11-10 fit · 1-1 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | spread | away **SPLIT** | +12.5 | 2-2 | 3 (-115) | 3 |  | 3 ($10,000) |  |  | 67% / 68% | 6724 | money_level->away (24-16 fit · 1-1 fwd); sharp_gap->away (16-24 fit · 1-1 fwd); money_moving->home (9-20 fit · 1-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd) |

## C  weighted ROI 0 to +10%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | moneyline | home **SPLIT** | +9.8 | 3-2 | -168 (-168) | -164 | 0.6 | -174 ($10,000) |  |  | 85% / 74% | 12470 | follow_move->home (15-18 fit · 2-0 fwd); money_level->home (34-6 fit · 1-1 fwd); sharp_gap->away (20-18 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->away (12-29 fit · 1-1 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | total | over **SPLIT** | +4.5 | 2-2 | 46.5 (-104) | 46.5 |  | 45 ($3,000) | +1.5 |  | 82% / 87% | 13581 | money_level->over (22-18 fit · 1-1 fwd); sharp_gap->over (19-22 fit · 2-0 fwd); money_moving->under (14-17 fit · 1-1 fwd); pin_value->under (11-10 fit · 1-1 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | total | over | +3.1 | 2-1 | 43.5 (-110) | 43.5 |  | 43.5 ($3,000) |  |  | 64% / 63% | 8860 | money_level->over (22-18 fit · 1-1 fwd); sharp_gap->under (19-22 fit · 2-0 fwd); money_moving->over (14-17 fit · 1-1 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | tt_away | over | +2.3 | 1-0 | 18.5 (-111) | 18.5 |  | 19.5 ($2,000) | -1 |  | 0% / 0% | 14595 | pin_value->over (14-11 fit · 0-1 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | tt_away | under | +2.3 | 1-0 | 19.5 (+102) | 19.5 |  | 18.5 ($2,000) | -1 |  | 0% / 0% | 6724 | pin_value->under (14-11 fit · 0-1 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | tt_away | under | +2.3 | 1-0 | 30.5 (-113) | 30.5 |  | 29.5 ($1,000) | -1 |  | 0% / 0% | 8754 | pin_value->under (14-11 fit · 0-1 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | tt_home | over | +1.4 | 1-0 | 30.5 (-115) | 30.5 |  | 31.5 ($2,000) | -1 |  | 0% / 0% | 10738 | pin_value->over (15-12 fit · 2-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | tt_home | under | +1.4 | 1-0 | 30.5 (-108) | 30.5 |  | 29.5 ($2,000) | -1 |  | 0% / 0% | 14595 | pin_value->under (15-12 fit · 2-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | total | over | +1.2 | 3-1 | 41.5 (-120) | 40.5 | 1 | 41.5 ($3,000) |  |  | 58% / 57% | 6724 | follow_move->over (9-9 fit · 1-0 fwd); money_level->over (22-18 fit · 1-1 fwd); sharp_gap->under (19-22 fit · 2-0 fwd); money_moving->over (14-17 fit · 1-1 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | total | over | +1 | 4-1 | 53.5 (-115) | 52.5 | 1 | 54 ($3,000) | -0.5 |  | 61% / 66% | 8754 | follow_move->over (9-9 fit · 1-0 fwd); money_level->over (22-18 fit · 1-1 fwd); sharp_gap->over (19-22 fit · 2-0 fwd); money_moving->under (14-17 fit · 1-1 fwd); pin_value->over (11-10 fit · 1-1 fwd) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | total | over **SPLIT** | -5.4 | 3-2 | 44.5 (-115) | 45.5 | 1 | 44.5 ($3,000) |  | over 73% | 73% / 76% | 10738 | follow_move->under (9-9 fit · 1-0 fwd); rlm->under (4-5 fit · 0-0 fwd); money_level->over (22-18 fit · 1-1 fwd); sharp_gap->over (19-22 fit · 2-0 fwd); money_moving->over (14-17 fit · 1-1 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | moneyline | away **SPLIT** | -12 | 3-3 | 134 (+134) | 134 |  | 151 ($10,000) |  |  | 24% / 31% | 6724 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 1-1 fwd); sharp_gap->away (20-18 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->away (12-29 fit · 1-1 fwd); pin_value->home (2-6 fit · 0-1 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | spread | away **SPLIT** | -17.9 | 3-2 | 16.5 (-110) | 17 | 0.5 | 17 ($20,000) | -0.5 |  | 49% / 54% | 10738 | follow_move->away (15-20 fit · 1-1 fwd); money_level->away (24-16 fit · 1-1 fwd); sharp_gap->away (16-24 fit · 1-1 fwd); money_moving->home (9-20 fit · 1-1 fwd); pin_value->home (15-3 fit · 1-0 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | spread | home **SPLIT** | -26.9 | 5-2 | -15.5 (-115) | -15 | 0.5 | -16.5 ($10,000) | +1 | away 69% | 31% / 30% | 10016 | follow_move->home (15-20 fit · 1-1 fwd); rlm->home (1-11 fit · 0-0 fwd); money_level->away (24-16 fit · 1-1 fwd); sharp_gap->away (16-24 fit · 1-1 fwd); money_moving->home (9-20 fit · 1-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd); pin_value->home (15-3 fit · 1-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | moneyline | home **SPLIT** | -46.4 | 3-2 | 240 (+240) | 235 | 0.4 | 242 ($10,000) |  |  | 2% / 3% | 8754 | follow_move->away (15-18 fit · 2-0 fwd); money_level->away (34-6 fit · 1-1 fwd); sharp_gap->home (20-18 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->home (12-29 fit · 1-1 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | moneyline | away **SPLIT** | -52 | 6-2 | 900 (+900) | 980 | 0.6 | 879 ($10,000) |  | home 99% | 1% / 5% | 10738 | follow_move->away (15-18 fit · 2-0 fwd); rlm->away (3-16 fit · 1-0 fwd); rlm_ratio->away (2-7 fit · 1-0 fwd); money_level->home (34-6 fit · 1-1 fwd); sharp_gap->away (20-18 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->away (12-29 fit · 1-1 fwd); pin_rlm->away (2-7 fit · 0-0 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | moneyline | home **SPLIT** | -57.1 | 3-3 | 172 (+172) | 176 | 0.5 | 176 ($10,000) |  | away 89% | 11% / 7% | 8274 | follow_move->home (15-18 fit · 2-0 fwd); rlm->home (3-16 fit · 1-0 fwd); money_level->away (34-6 fit · 1-1 fwd); sharp_gap->away (20-18 fit · 1-1 fwd); money_moving->away (12-19 fit · 2-0 fwd); consensus_gap->home (12-29 fit · 1-1 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | moneyline | away **SPLIT** | -63 | 3-2 | 194 (+194) | 215 | 2.5 | 211 ($10,000) |  | home 96% | 4% / 4% | 13581 | follow_move->away (15-18 fit · 2-0 fwd); rlm->away (3-16 fit · 1-0 fwd); money_level->home (34-6 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->away (12-29 fit · 1-1 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | spread | away **SPLIT** | -65.7 | 4-2 | 7.5 (-105) | 8 | 0.5 | 8 ($20,000) | -0.5 |  | 51% / 52% | 13131 | follow_move->away (15-20 fit · 1-1 fwd); money_level->away (24-16 fit · 1-1 fwd); sharp_gap->away (16-24 fit · 1-1 fwd); money_moving->away (9-20 fit · 1-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd); pin_value->home (15-3 fit · 1-0 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | spread | away **SPLIT** | -65.7 | 4-2 | 4.5 (-105) | 5.5 | 1 | 5.5 ($10,000) | -1 |  | 60% / 61% | 13581 | follow_move->away (15-20 fit · 1-1 fwd); money_level->away (24-16 fit · 1-1 fwd); sharp_gap->away (16-24 fit · 1-1 fwd); money_moving->away (9-20 fit · 1-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd); pin_value->home (15-3 fit · 1-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | spread | away **SPLIT** | -66.7 | 3-3 | 9.5 (-100) | 9.5 |  | 10.5 ($20,000) | -1 |  | 49% / 51% | 10647 | money_level->away (24-16 fit · 1-1 fwd); sharp_gap->away (16-24 fit · 1-1 fwd); money_moving->away (9-20 fit · 1-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd); book_lag->home (4-0 fit · 0-0 fwd); pin_value->home (15-3 fit · 1-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | moneyline | away **SPLIT** | -82.9 | 5-2 | 320 (+320) | 350 | 1.6 | 313 ($10,000) |  | home 96% | 4% / 6% | 13131 | follow_move->away (15-18 fit · 2-0 fwd); rlm->away (3-16 fit · 1-0 fwd); rlm_ratio->away (2-7 fit · 1-0 fwd); money_level->home (34-6 fit · 1-1 fwd); sharp_gap->away (20-18 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->away (12-29 fit · 1-1 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | spread | home **SPLIT** | -107.3 | 4-2 | 5.5 (-100) | 6.5 | 1 | 6 ($20,000) | -0.5 | away 72% | 28% / 29% | 13187 | follow_move->home (15-20 fit · 1-1 fwd); rlm->home (1-11 fit · 0-0 fwd); money_level->away (24-16 fit · 1-1 fwd); sharp_gap->home (16-24 fit · 1-1 fwd); money_moving->home (9-20 fit · 1-1 fwd); pin_value->away (15-3 fit · 1-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | moneyline | home | -2 | 4-1 | -146 (-146) | -132 | 2.5 | -153 ($10,000) |  |  | 82% / 84% | 8860 | follow_move->home (15-18 fit · 2-0 fwd); money_level->home (34-6 fit · 1-1 fwd); sharp_gap->home (20-18 fit · 1-1 fwd); money_moving->home (12-19 fit · 2-0 fwd); consensus_gap->away (12-29 fit · 1-1 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | moneyline | away | -2 | 4-1 | -260 (-260) | -245 | 1.6 | -259 ($10,000) |  |  | 97% / 99% | 13187 | follow_move->away (15-18 fit · 2-0 fwd); money_level->away (34-6 fit · 1-1 fwd); sharp_gap->away (20-18 fit · 1-1 fwd); money_moving->away (12-19 fit · 2-0 fwd); consensus_gap->home (12-29 fit · 1-1 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | tt_away | under | -2.3 | 1-1 | 13.5 (-100) | 14.5 | 1 | 14.5 ($2,000) | +1 |  | 0% / 0% | 10738 | follow_move->under (8-7 fit · 1-0 fwd); pin_value->over (14-11 fit · 0-1 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | tt_away | under | -2.3 | 1-1 | 20.5 (-113) | 21.5 | 1 | 21.5 ($2,000) | +1 |  | 0% / 0% | 8274 | follow_move->under (8-7 fit · 1-0 fwd); pin_value->over (14-11 fit · 0-1 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | total | over | -3.4 | 2-1 | 41.5 (-100) | 41.5 |  | 41 ($3,000) | +0.5 |  | 83% / 83% | 10016 | money_level->over (22-18 fit · 1-1 fwd); money_moving->over (14-17 fit · 1-1 fwd); pin_value->under (11-10 fit · 1-1 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | total | over | -4.2 | 2-0 | 46.5 (-104) | 46.5 |  | 46.5 ($3,000) |  |  | 83% / 83% | 13187 | money_level->over (22-18 fit · 1-1 fwd); money_moving->over (14-17 fit · 1-1 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | tt_home | under | -4.7 | 1-0 | 19.5 (-104) | 20.5 | 1 | 19.5 ($2,000) |  |  | 0% / 0% | 13187 | follow_move->under (8-9 fit · 1-1 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | total | over | -5 | 3-0 | 40.5 (-110) | 40.5 |  | 41 ($3,000) | -0.5 |  | 78% / 78% | 10647 | money_level->over (22-18 fit · 1-1 fwd); money_moving->over (14-17 fit · 1-1 fwd); pin_value->over (11-10 fit · 1-1 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | tt_home | over | -6.1 | 1-1 | 32.5 (-113) | 31.5 | 1 | 31.5 ($2,000) | +1 |  | 0% / 0% | 13131 | follow_move->over (8-9 fit · 1-1 fwd); pin_value->under (15-12 fit · 2-0 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | tt_home | under | -6.1 | 1-1 | 25.5 (-108) | 26.5 | 1 | 26.5 ($2,000) | +1 |  | 0% / 0% | 13581 | follow_move->under (8-9 fit · 1-1 fwd); pin_value->over (15-12 fit · 2-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | tt_home | over | -6.1 | 1-1 | 22.5 (-120) | 21.5 | 1 | 21.5 ($2,000) | +1 |  | 0% / 0% | 6724 | follow_move->over (8-9 fit · 1-1 fwd); pin_value->under (15-12 fit · 2-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | tt_home | over | -6.1 | 1-1 | 26.5 (-104) | 25.5 | 1 | 24.5 ($2,000) | +2 |  | 0% / 0% | 10647 | follow_move->over (8-9 fit · 1-1 fwd); pin_value->under (15-12 fit · 2-0 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | tt_home | over | -6.1 | 1-1 | 25.5 (-111) | 24.5 | 1 | 24.5 ($2,000) | +1 |  | 0% / 0% | 12470 | follow_move->over (8-9 fit · 1-1 fwd); pin_value->under (15-12 fit · 2-0 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | spread | home | -6.3 | 2-0 | 4.5 (-115) | 4.5 |  | 4.5 ($20,000) |  |  | 72% / 73% | 8274 | money_level->home (24-16 fit · 1-1 fwd); sharp_gap->home (16-24 fit · 1-1 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | spread | home | -8.7 | 3-1 | -11.5 (-110) | -9.5 | 2 | -11.5 ($20,000) |  |  | 75% / 74% | 14595 | follow_move->home (15-20 fit · 1-1 fwd); money_level->home (24-16 fit · 1-1 fwd); sharp_gap->away (16-24 fit · 1-1 fwd); money_moving->home (9-20 fit · 1-1 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | total | over | -11.5 | 3-0 | 48.5 (-115) | 48.5 |  | 48.5 ($3,000) |  |  | 74% / 77% | 14595 | money_level->over (22-18 fit · 1-1 fwd); sharp_gap->over (19-22 fit · 2-0 fwd); money_moving->over (14-17 fit · 1-1 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | total | over | -12.3 | 4-0 | 54.5 (-120) | 54.5 |  | 55.5 ($3,000) | -1 |  | 70% / 71% | 13131 | money_level->over (22-18 fit · 1-1 fwd); sharp_gap->over (19-22 fit · 2-0 fwd); money_moving->over (14-17 fit · 1-1 fwd); pin_value->over (11-10 fit · 1-1 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | total | under | -24.4 | 4-1 | 37.5 (-110) | 38.5 | 1 | 37.5 ($3,000) |  | over 79% | 21% / 23% | 8274 | follow_move->under (9-9 fit · 1-0 fwd); rlm->under (4-5 fit · 0-0 fwd); money_level->over (22-18 fit · 1-1 fwd); sharp_gap->under (19-22 fit · 2-0 fwd); money_moving->under (14-17 fit · 1-1 fwd) |

