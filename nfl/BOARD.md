# NFL board

Generated 2026-11-15 23:06 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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

| tier | game | market | side | line | moved from | tickets | money/tix | record |
|---|---|---|---|---|---|---|---|---|
| PINNACLE moved vs public | Los Angeles Chargers @ Baltimore Ravens | spread | home | -4.5 | -3.5 | 37% | 1.59 | 5-9 |
| FanDuel moved vs public | Los Angeles Chargers @ Baltimore Ravens | spread | home | -4.5 | -2.5 | 37% | 1.59 | 3-7 |

Ranked by **weighted edge**: each agreeing signal contributes its own
base-rate-corrected edge, and contributes nothing until it has 30 decided
outcomes. Raw agreement count is shown too, but it is the weaker number — a
market can have seven signals agreeing where four of them have losing records.

## B  weighted edge +5 to +10

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | tt_home | under | +5 | 1-0 | 22.5 (-118) | 22.5 |  | 20.5 ($2,000) | +2 |  | 0% / 0% | 16090 | pin_value->under (15-10) |

## C  weighted edge 0 to +5

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | moneyline | home | +4.4 | 4-1 | -188 (-188) | -108 | 13.4 | -185 ($75,000) |  |  | 85% / 90% | 71479 | follow_move->home (28-8); money_level->home (30-6); sharp_gap->home (18-16); money_moving->home (11-16); consensus_gap->away (12-25) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | tt_away | under | +1.1 | 1-0 | 22.5 (-104) | 22.5 |  | 21.5 ($5,000) | +1 |  | 0% / 0% | 71479 | pin_value->under (12-11) |

## D  no weighted edge (agreement is all unproven or negative signals)

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | moneyline | away | -0.6 | 3-2 | 190 (+190) | -112 | 16.9 | -217 ($10,000) |  |  | 18% / 36% | 16090 | follow_move->home (28-8); money_level->home (30-6); sharp_gap->away (18-16); money_moving->away (11-16); consensus_gap->away (12-25) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | total | over | -6.1 | 4-0 | 49.5 (-105) | 48.5 | 1 | 50 ($20,000) | -0.5 |  | 70% / 76% | 71479 | follow_move->over (7-8); money_level->over (19-17); sharp_gap->over (15-22); pin_value->over (9-9) |
| Sun 20:20 | Pittsburgh Steelers @ Cincinnati Bengals | spread | away | -7.6 | 3-0 | 3.5 (-110) | -4 | 0.5 | -3.5 ($100,000) |  |  | 48% / 52% | 71479 | follow_move->away (13-18); money_level->away (22-15); sharp_gap->away (14-22) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | total | under | -8.6 | 2-1 | 38.5 (-105) | 38.5 |  | 38.5 ($5,000) |  |  | 29% / 32% | 16090 | money_level->over (19-17); sharp_gap->under (15-22); money_moving->under (13-15) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | spread | home | -8.9 | 7-0 | -4.5 (-110) | -2.5 | 2 | -4.5 ($20,000) |  | away 63% | 37% / 59% | 16090 | follow_move->home (13-18); rlm->home (1-10); rlm_ratio->home (0-5); money_level->home (22-15); sharp_gap->home (14-22); money_moving->home (9-17); pin_rlm->home (0-2) |

