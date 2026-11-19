# NFL board

Generated 2026-11-19 12:02 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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
| PINNACLE moved vs public | Miami Dolphins @ Buffalo Bills | total | under | Pinnacle | 47 -> 45.5 | 45.5 | 19% | 1.21 | 5-10 fit · 0-0 fwd |
| PINNACLE moved vs public | Miami Dolphins @ Buffalo Bills | moneyline | away | Pinnacle | 889 -> 882 | 980 | 1% | 6.0 | 5-10 fit · 0-0 fwd |
| PINNACLE moved vs public | Minnesota Vikings @ San Francisco 49ers | moneyline | away | Pinnacle | 145 -> 143 | 142 | 13% | 2.38 | 5-10 fit · 0-0 fwd |
| FanDuel moved vs public | Miami Dolphins @ Buffalo Bills | spread | away | FanDuel | -17 -> 16.5 | 16.5 | 30% | 1.27 | 5-14 fit · 1-0 fwd |
| FanDuel moved vs public | Tennessee Titans @ Dallas Cowboys | moneyline | away | FanDuel | -450 -> 330 | 330 | 3% | 2.0 | 5-14 fit · 1-0 fwd |

Ranked by **weighted ROI**: each agreeing signal contributes its own return per
unit risked, and contributes nothing until it has 30 decided outcomes. A signal
earns positive weight only if it **both** beats its own base rate and makes
money. Hit-rate edge alone is blind to price — `money_level` on CBB moneylines
beats its base rate by 3.6 points while returning −3.5%, because it lays −880
favourites, and on 2026-11-17 that ranked a −880 chalk first on the board.
Raw agreement count is shown too, but it is the weaker number — a
market can have seven signals agreeing where four of them have losing records.

Each call shows **two** records: `fit` (the games the signal was chosen on —
before 2026-11-17, so a good number there proves nothing) and `fwd` (games
since, which it had no hand in choosing). A `*` means the weight came from the
forward record, which happens once that record reaches 30 decided
outcomes. No asterisk means the lean rests on fitted numbers only.

## A  weighted ROI >= +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | spread | home | +54.1 | 5-1 | -9.5 (-120) | -9.5 |  | -10.5 ($20,000) | +1 |  | 62% / 63% | 6169 | money_level->home (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd); book_lag->home (4-0 fit · 0-0 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | spread | home | +35.7 | 2-2 | -11.5 (-110) | -9.5 | 2 | -11.5 ($20,000) |  |  | 82% / 73% | 7825 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | spread | away | +35.7 | 2-2 | -6.5 (-104) | -4 | 2.5 | -6.5 ($20,000) |  |  | 80% / 77% | 5220 | follow_move->away (15-20 fit · 0-1 fwd); money_level->away (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd) |
| Thu 20:15 | Indianapolis Colts @ Houston Texans | moneyline | home | +23.7 | 3-3 | -800 (-800) | -720 | 1.1 | -721 ($10,000) |  |  | 93% / 69% | 17670 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->home (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_value->away (2-6 fit · 0-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | moneyline | home | +23.7 | 3-3 | -620 (-620) | -550 | 1.5 | -535 ($10,000) |  |  | 97% / 94% | 6169 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->home (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_value->away (2-6 fit · 0-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | spread | home | +20.6 | 2-1 | -2.5 (-110) | -2 | 0.5 | -2.5 ($20,000) |  |  | 67% / 67% | 4781 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd) |

## B  weighted ROI +10% to +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | spread | home | +17.2 | 2-2 | -7 (-110) | -5.5 | 1.5 | -7 ($10,000) |  |  | 74% / 74% | 7088 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); consensus_gap->away (5-3 fit · 0-0 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | spread | home | +14.7 | 4-1 | -15.5 (-115) | -15 | 0.5 | -16 ($20,000) | +0.5 |  | 73% / 70% | 5614 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd); pin_value->home (15-3 fit · 0-0 fwd) |

## C  weighted ROI 0 to +10%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | moneyline | away | +3.9 | 3-1 | -260 (-260) | -245 | 1.6 | -266 ($10,000) |  |  | 97% / 97% | 7461 | follow_move->away (15-18 fit · 1-0 fwd); money_level->away (34-6 fit · 0-1 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->home (12-29 fit · 1-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | total | over | +3.9 | 2-2 | 40.5 (-110) | 40.5 |  | 40 ($3,000) | +0.5 |  | 76% / 75% | 6169 | money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | total | under | +2.6 | 2-0 | 46.5 (-115) | 46.5 |  | 46 ($3,000) | +0.5 |  | 89% / 89% | 7280 | money_level->under (22-18 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | total | over | +2.3 | 3-1 | 54.5 (-120) | 54.5 |  | 55.5 ($3,000) | -1 |  | 72% / 69% | 7537 | money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd); pin_value->over (11-10 fit · 0-1 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | tt_away | over | +2.3 | 1-0 | 18.5 (-113) | 18.5 |  | 19.5 ($2,000) | -1 |  | 0% / 0% | 7825 | pin_value->over (14-11 fit · 0-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | tt_away | under | +2.3 | 1-0 | 19.5 (-104) | 19.5 |  | 18.5 ($2,000) | +1 |  | 0% / 0% | 3645 | pin_value->under (14-11 fit · 0-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | tt_away | under | +2.3 | 1-0 | 30.5 (-115) | 30.5 |  | 29.5 ($1,000) | +1 |  | 0% / 0% | 5220 | pin_value->under (14-11 fit · 0-0 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | tt_home | over | +1.4 | 1-0 | 30.5 (-115) | 30.5 |  | 31.5 ($2,000) | -1 |  | 0% / 0% | 5856 | pin_value->over (15-12 fit · 1-0 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | tt_home | under | +1.4 | 1-0 | 30.5 (-106) | 30.5 |  | 29.5 ($2,000) | +1 |  | 0% / 0% | 7825 | pin_value->under (15-12 fit · 1-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | tt_home | under | +1.4 | 1-0 | 20.5 (-130) | 20.5 |  | 19.5 ($2,000) | +1 |  | 0% / 0% | 7461 | pin_value->under (15-12 fit · 1-0 fwd) |
| Sun 16:25 | Las Vegas Raiders @ Denver Broncos | tt_home | under | +1.4 | 1-0 | 25.5 (-104) | 25.5 |  | 24.5 ($2,000) | +1 |  | 0% / 0% | 6169 | pin_value->under (15-12 fit · 1-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | total | over | +1.2 | 3-1 | 41.5 (-110) | 40.5 | 1 | 41.5 ($3,000) |  |  | 66% / 60% | 3645 | follow_move->over (9-9 fit · 1-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | total | over | +1 | 4-1 | 53.5 (-115) | 52.5 | 1 | 54.5 ($3,000) | -1 |  | 58% / 76% | 5220 | follow_move->over (9-9 fit · 1-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->over (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd); pin_value->over (11-10 fit · 0-1 fwd) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | total | under | -1.7 | 3-1 | 45.5 (-115) | 45.5 |  | 45.5 ($3,000) |  |  | 19% / 23% | 5856 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); pin_rlm->under (3-1 fit · 0-0 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | moneyline | home | -2 | 4-1 | -136 (-136) | -132 | 0.7 | -141 ($10,000) |  |  | 82% / 84% | 4781 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->home (20-18 fit · 1-0 fwd); money_moving->home (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | moneyline | away | -2 | 4-1 | -230 (-230) | -210 | 1.7 | -217 ($10,000) |  |  | 86% / 93% | 4705 | follow_move->away (15-18 fit · 1-0 fwd); money_level->away (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->home (12-29 fit · 1-0 fwd) |
| Thu 20:15 | Indianapolis Colts @ Houston Texans | tt_away | under | -2.3 | 1-1 | 15.5 (-111) | 16.5 | 1 | 16.5 ($2,000) | -1 |  | 0% / 0% | 17670 | follow_move->under (8-7 fit · 0-0 fwd); pin_value->over (14-11 fit · 0-0 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | tt_away | under | -2.3 | 1-1 | 17.5 (-120) | 20.5 | 3 | 20.5 ($2,000) | -3 |  | 0% / 0% | 7088 | follow_move->under (8-7 fit · 0-0 fwd); pin_value->over (14-11 fit · 0-0 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | tt_away | under | -2.3 | 1-1 | 13.5 (-100) | 14.5 | 1 | 14.5 ($2,000) | -1 |  | 0% / 0% | 5856 | follow_move->under (8-7 fit · 0-0 fwd); pin_value->over (14-11 fit · 0-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | tt_home | over | -6.1 | 1-1 | 32.5 (-111) | 31.5 | 1 | 31.5 ($2,000) | +1 |  | 0% / 0% | 7537 | follow_move->over (8-9 fit · 1-0 fwd); pin_value->under (15-12 fit · 1-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | tt_home | over | -6.1 | 1-1 | 22.5 (-115) | 21.5 | 1 | 21.5 ($2,000) | +1 |  | 0% / 0% | 3645 | follow_move->over (8-9 fit · 1-0 fwd); pin_value->under (15-12 fit · 1-0 fwd) |
| Thu 20:15 | Indianapolis Colts @ Houston Texans | total | over | -6.2 | 4-2 | 43.5 (-115) | 44.5 | 1 | 44 ($6,000) | -0.5 | over 73% | 73% / 76% | 17670 | follow_move->under (9-9 fit · 1-0 fwd); rlm->under (4-5 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->over (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd); pin_value->over (11-10 fit · 0-1 fwd) |
| Sun 13:00 | Baltimore Ravens @ Carolina Panthers | total | under | -7.2 | 2-2 | 43.5 (-110) | 43.5 |  | 43.5 ($3,000) |  |  | 21% / 27% | 4781 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | total | under | -9 | 3-3 | 37.5 (-105) | 38.5 | 1 | 38.5 ($3,000) | -1 | over 82% | 18% / 17% | 4705 | follow_move->under (9-9 fit · 1-0 fwd); rlm->under (4-5 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->over (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd); pin_value->over (11-10 fit · 0-1 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | total | under | -10.6 | 4-2 | 44.5 (-120) | 46.5 | 2 | 44 ($3,000) | +0.5 | over 81% | 19% / 13% | 7088 | follow_move->under (9-9 fit · 1-0 fwd); rlm->under (4-5 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->over (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | total | over | -11.5 | 3-0 | 48.5 (-115) | 48.5 |  | 48.5 ($3,000) |  |  | 63% / 64% | 7825 | money_level->over (22-18 fit · 1-0 fwd); sharp_gap->over (19-22 fit · 1-0 fwd); money_moving->over (14-17 fit · 1-0 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | spread | away | -12.1 | 3-2 | 3 (-100) | 3.5 | 0.5 | 3 ($20,000) |  |  | 63% / 54% | 7280 | follow_move->away (15-20 fit · 0-1 fwd); money_level->away (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); consensus_gap->home (5-3 fit · 0-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | total | under | -14.8 | 2-1 | 46.5 (-110) | 46.5 |  | 46.5 ($3,000) |  |  | 12% / 17% | 7461 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd) |
| Thu 20:15 | Indianapolis Colts @ Houston Texans | spread | home | -15.5 | 5-0 | -12.5 (-110) | -10 | 2.5 | -13 ($30,000) | +0.5 |  | 54% / 58% | 17670 | follow_move->home (15-20 fit · 0-1 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | total | under | -23.2 | 4-1 | 41.5 (-120) | 41.5 |  | 41 ($3,000) | +0.5 |  | 12% / 24% | 5614 | pre_move->under (1-2 fit · 0-0 fwd); money_level->over (22-18 fit · 1-0 fwd); sharp_gap->under (19-22 fit · 1-0 fwd); money_moving->under (14-17 fit · 1-0 fwd); pin_value->under (11-10 fit · 0-1 fwd) |
| Sun 13:00 | Arizona Cardinals @ Kansas City Chiefs | moneyline | away | -25.9 | 3-2 | 870 (+870) | 870 |  | 850 ($10,000) |  |  | 2% / 12% | 5614 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->home (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | spread | away | -28.5 | 3-0 | 3 (-110) | 3 |  | 3 ($10,000) |  |  | 49% / 73% | 3645 | money_level->away (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd) |
| Sun 13:00 | New Orleans Saints @ Chicago Bears | moneyline | away | -42 | 3-2 | 520 (+520) | 490 | 0.8 | 442 ($10,000) |  |  | 2% / 3% | 7825 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_value->away (2-6 fit · 0-0 fwd) |
| Sun 13:00 | Pittsburgh Steelers @ Philadelphia Eagles | spread | home | -46.1 | 2-1 | 4.5 (-110) | 4.5 |  | 4.5 ($20,000) |  |  | 23% / 25% | 4705 | money_level->away (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd) |
| Sun 16:05 | New York Jets @ Los Angeles Chargers | moneyline | away | -46.4 | 3-2 | 136 (+136) | 134 | 0.6 | 140 ($10,000) |  |  | 29% / 41% | 3645 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd) |
| Sun 20:20 | Minnesota Vikings @ San Francisco 49ers | moneyline | away | -52 | 4-2 | 142 (+142) | 138 | 0.6 | 143 ($10,000) |  |  | 13% / 31% | 7280 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_rlm->away (2-7 fit · 0-0 fwd) |
| Sun 13:00 | Tampa Bay Buccaneers @ Detroit Lions | moneyline | away | -60.3 | 4-2 | 290 (+290) | 215 | 6 | 249 ($10,000) |  |  | 4% / 9% | 7088 | follow_move->home (15-18 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); money_moving->away (12-19 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_value->away (2-6 fit · 0-0 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | moneyline | away | -66.2 | 5-1 | 980 (+980) | 980 |  | 882 ($10,000) |  |  | 1% / 6% | 5856 | pre_move->away (1-3 fit · 0-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_value->away (2-6 fit · 0-0 fwd); pin_rlm->away (2-7 fit · 0-0 fwd) |
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | moneyline | home | -75.4 | 3-2 | 230 (+230) | 235 | 0.5 | 249 ($10,000) |  | away 98% | 2% / 1% | 5220 | follow_move->home (15-18 fit · 1-0 fwd); rlm->home (3-16 fit · 1-0 fwd); money_level->away (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); consensus_gap->home (12-29 fit · 1-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | spread | away | -77.1 | 3-3 | 7.5 (-105) | 8 | 0.5 | 8 ($20,000) | +0.5 | home 65% | 35% / 34% | 7537 | follow_move->away (15-20 fit · 0-1 fwd); rlm->away (1-11 fit · 0-0 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->away (9-20 fit · 0-1 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Sun 13:00 | Miami Dolphins @ Buffalo Bills | spread | away | -82.3 | 4-3 | 16.5 (-110) | 17 | 0.5 | 17 ($20,000) | +0.5 | home 70% | 30% / 38% | 5856 | follow_move->away (15-20 fit · 0-1 fwd); rlm->away (1-11 fit · 0-0 fwd); rlm_ratio->away (0-6 fit · 0-0 fwd); money_level->home (24-16 fit · 0-1 fwd); sharp_gap->away (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd); pin_value->home (15-3 fit · 0-0 fwd) |
| Sun 16:25 | Jacksonville Jaguars @ New York Giants | spread | home | -107.3 | 4-2 | 5.5 (-100) | 6.5 | 1 | 6 ($20,000) | -0.5 | away 88% | 12% / 13% | 7461 | follow_move->home (15-20 fit · 0-1 fwd); rlm->home (1-11 fit · 0-0 fwd); money_level->away (24-16 fit · 0-1 fwd); sharp_gap->home (16-24 fit · 0-1 fwd); money_moving->home (9-20 fit · 0-1 fwd); pin_value->away (15-3 fit · 0-0 fwd) |
| Sun 13:00 | Tennessee Titans @ Dallas Cowboys | moneyline | away | -115.1 | 6-1 | 330 (+330) | 350 | 1 | 312 ($10,000) |  | home 97% | 3% / 6% | 7537 | follow_move->away (15-18 fit · 1-0 fwd); rlm->away (3-16 fit · 1-0 fwd); rlm_ratio->away (2-7 fit · 1-0 fwd); money_level->home (34-6 fit · 0-1 fwd); sharp_gap->away (20-18 fit · 1-0 fwd); consensus_gap->away (12-29 fit · 1-0 fwd); pin_value->away (2-6 fit · 0-0 fwd) |

