# NFL board

Generated 2026-11-23 13:33 UTC. Upcoming games with a FanDuel line, grouped by how many signals
agree on each market. Every game is listed; nothing is cut. Each call shows that
signal's graded CLOSE record so far, so you can see which ones are earning.

`Pin` is Pinnacle's number and the size it will take — **Gate A, a price floor and
a guide to which book to use. It is not a veto.** `gap` is FanDuel minus Pinnacle in
points. `public` names the ticket majority when it is over 60% — when the line has
moved the other way, `rlm` fires.

This is analysis, not picks.

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
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | spread | away **SPLIT** | +83.4 | 5-3 | -5.5 (-120) | -4 | 1.5 | -6.5 ($50,000) | +1 |  | 82% / 72% | 37845 | money_delta->home (3-14 fit · 1-0 fwd); follow_move->away (16-21 fit · 5-5 fwd); money_level->away (25-17 fit · 3-7 fwd); sharp_gap->home (17-25 fit · 7-4 fwd); money_moving->home (10-21 fit · 4-7 fwd); consensus_gap->away (5-3 fit · 0-2 fwd); pin_value->away (16-3 fit · 2-3 fwd); pin_move->away (8-10 fit · 3-3 fwd) |

## B  weighted ROI +10% to +20%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | total | over **SPLIT** | +18.5 | 4-2 | 54.5 (-110) | 52.5 | 2 | 55 ($10,000) | -0.5 |  | 66% / 66% | 37845 | money_delta->under (4-7 fit · 1-3 fwd); follow_move->over (10-9 fit · 8-1 fwd); money_level->over (23-19 fit · 6-5 fwd); money_moving->under (15-18 fit · 5-6 fwd); pin_value->over (12-11 fit · 4-1 fwd); pin_move->over (14-13 fit · 10-1 fwd) |

## C  weighted ROI 0 to +10%

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | tt_away | under | +0.3 | 1-0 | 30.5 (-106) | 30.5 |  | 29.5 ($3,000) | -1 |  | 0% / 0% | 37845 | pin_value->under (14-12 fit · 1-6 fwd) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| kickoff (ET) | game | market | lean | wt ROI | raw | FD now | open | move | Pin | gap | public | tix / money (lean) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 20:15 | Cincinnati Bengals @ Washington Commanders | moneyline | home **SPLIT** | -35 | 4-3 | 240 (+240) | 235 | 0.4 | 260 ($20,000) |  |  | 4% / 8% | 37845 | money_delta->home (4-5 fit · 0-1 fwd); follow_move->away (17-18 fit · 5-4 fwd); money_level->away (35-7 fit · 8-3 fwd); sharp_gap->home (21-19 fit · 2-9 fwd); money_moving->home (14-19 fit · 4-6 fwd); consensus_gap->home (13-30 fit · 3-8 fwd); pin_move->away (15-11 fit · 4-4 fwd) |

