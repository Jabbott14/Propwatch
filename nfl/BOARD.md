# NFL board

Generated 2026-11-16 07:10 UTC. Upcoming games with a FanDuel line, grouped by how many signals
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
| FanDuel moved vs public | Los Angeles Chargers @ Baltimore Ravens | spread | home | -4.5 | -2.5 | 43% | 1.53 | 3-8 |

Ranked by **weighted edge**: each agreeing signal contributes its own
base-rate-corrected edge, and contributes nothing until it has 30 decided
outcomes. Raw agreement count is shown too, but it is the weaker number — a
market can have seven signals agreeing where four of them have losing records.

## C  weighted edge 0 to +5

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | tt_home | under | +2.9 | 1-0 | 22.5 (-118) | 22.5 |  | 20.5 ($5,000) | +2 |  | 0% / 0% | 20947 | pin_value->under (15-12) |

## D  no weighted edge (agreement is all unproven or negative signals)

| kickoff (ET) | game | market | lean | wt edge | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | moneyline | away | -1.5 | 3-2 | 190 (+190) | -112 | 16.9 | -217 ($30,000) |  |  | 18% / 39% | 20947 | follow_move->home (32-8); money_level->home (34-6); sharp_gap->away (20-18); money_moving->away (12-19); consensus_gap->away (12-29) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | total | over | -4.3 | 3-0 | 38.5 (-115) | 38.5 |  | 38.5 ($15,000) |  |  | 71% / 73% | 20947 | money_level->over (22-18); sharp_gap->over (19-22); money_moving->over (14-17) |
| Mon 20:15 | Los Angeles Chargers @ Baltimore Ravens | spread | home | -14.5 | 5-0 | -4.5 (-110) | -2.5 | 2 | -4.5 ($50,000) |  |  | 43% / 66% | 20947 | follow_move->home (15-20); rlm_ratio->home (0-6); money_level->home (24-16); sharp_gap->home (16-24); money_moving->home (9-20) |

