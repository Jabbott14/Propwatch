# CBB board

Generated 2026-11-23 13:42 UTC. Upcoming games with a FanDuel line. Every game is listed;
nothing is cut.

Ranked by **weighted ROI**: each agreeing signal contributes its own return per
unit risked, and contributes nothing until it has 30 decided outcomes. A
signal earns positive weight only if it **both** beats its own base rate and
makes money. Hit-rate edge alone is blind to price — `money_level` on CBB
moneylines beats its base rate by 3.6 points while returning −3.5%, because it
lays −880 favourites, and on 2026-11-17 that ranked a −880 chalk first here.
Raw agreement count is shown too, but it is the weaker number — a
market can have five signals agreeing where four have losing records.

**SPLIT** marks a market where at least two signals point each way. Those average
to a weak score and land in band D looking empty, when our inputs are in
conflict — often the markets worth the most attention. They sort first inside
whatever band they fall in.

Each call shows **two** records: `fit` (games the signal was chosen on, before
2026-11-21 — a good number there proves nothing) and `fwd` (games since,
which it had no hand in choosing). A `*` means the weight came from the forward
record, which happens once that record reaches 30 decided outcomes.

This is analysis, not picks.

## FLAGGED — reverse line movement with split confirmation

The crowd holds the tickets on the other side, the money on this side is
outsized relative to its ticket count (>= 1.2x), and the number moved
here anyway. Pinnacle tier first: that is the sharp book moving, not a retail
book reacting to its own flow.


`moved` is **that tier's own book** moving — Pinnacle's number for the Pinnacle
tier, FanDuel's for the FanDuel tier. `FD now` is what you would be buying.
This table used to print one book's number next to the other's in one row.

`retraced` is how far Pinnacle's number has already come BACK against the move
in the `moved` column. `moved` compares first-seen with current, so a number
that went 136.5 -> 131 -> 135 prints as a drop while it is actually climbing.
A large `retraced` means the move is finished and reversing, and you would be
buying the wrong end of it. This is shown, not gated -- it is not a signal.

| tier | game | market | side | book | moved | retraced | FD now | tickets | money/tix | record |
|---|---|---|---|---|---|---|---|---|---|---|
| PINNACLE moved vs public | GASO@NKU | moneyline | away | Pinnacle | 136 -> 128 | — | 118 | 7% | 2.57 | 140-161 fit · 15-23 fwd |
| PINNACLE moved vs public | ILST@SCU | moneyline | away | Pinnacle | 183 -> 170 | — | 172 | 1% | 2.0 | 140-161 fit · 15-23 fwd |
| PINNACLE moved vs public | LBSU@FIU | moneyline | away | Pinnacle | 375 -> 370 | — | 360 | 4% | 5.0 | 140-161 fit · 15-23 fwd |
| PINNACLE moved vs public | SBON@APP | moneyline | home | Pinnacle | 183 -> 174 | **+1** | 160 | 10% | 4.6 | 140-161 fit · 15-23 fwd |
| PINNACLE moved vs public | TEM@UTM | moneyline | home | Pinnacle | 164 -> 162 | — | 152 | 4% | 2.0 | 140-161 fit · 15-23 fwd |
| PINNACLE moved vs public | TULN@GAST | moneyline | away | Pinnacle | 102 -> 104 | — | 102 | 17% | 2.82 | 140-161 fit · 15-23 fwd |
| PINNACLE moved vs public | UNI@DAV | moneyline | away | Pinnacle | 186 -> 183 | — | 184 | 6% | 3.0 | 140-161 fit · 15-23 fwd |
| FanDuel moved vs public | ALST@CAL | total | under | FanDuel | 146.5 -> 145.5 |  | 145.5 | 1% | 5.0 | 200-225 fit · 26-48 fwd |
| FanDuel moved vs public | CHAR@FGCU | moneyline | home | FanDuel | 260 -> 215 |  | 215 | 7% | 1.57 | 200-225 fit · 26-48 fwd |
| FanDuel moved vs public | CSU@ARIZ | moneyline | away | FanDuel | 1200 -> 1100 |  | 1100 | 2% | 17.0 | 200-225 fit · 26-48 fwd |
| FanDuel moved vs public | GASO@NKU | moneyline | away | FanDuel | 145 -> 118 | — | 118 | 7% | 2.57 | 200-225 fit · 26-48 fwd |
| FanDuel moved vs public | ILST@SCU | moneyline | away | FanDuel | 180 -> 172 | — | 172 | 1% | 2.0 | 200-225 fit · 26-48 fwd |
| FanDuel moved vs public | LBSU@FIU | moneyline | away | FanDuel | 390 -> 360 | — | 360 | 4% | 5.0 | 200-225 fit · 26-48 fwd |
| FanDuel moved vs public | MONM@UNC | moneyline | away | FanDuel | 1400 (other side moved) |  | 1400 | 1% | 7.0 | 200-225 fit · 26-48 fwd |
| FanDuel moved vs public | SBON@APP | moneyline | home | FanDuel | 180 -> 160 | **+1** | 160 | 10% | 4.6 | 200-225 fit · 26-48 fwd |
| FanDuel moved vs public | SFA@UVU | total | under | FanDuel | 152.5 -> 151.5 | — | 151.5 | 12% | 5.0 | 200-225 fit · 26-48 fwd |
| FanDuel moved vs public | TEM@UTM | moneyline | home | FanDuel | 190 -> 152 | — | 152 | 4% | 2.0 | 200-225 fit · 26-48 fwd |
| FanDuel moved vs public | UMES@YSU | total | under | FanDuel | 135.5 -> 133.5 |  | 133.5 | 7% | 3.0 | 200-225 fit · 26-48 fwd |

## A  weighted ROI >= +20%

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 22:00 | EWU@UNLV | total | over **SPLIT** | +22.5 | 5-2 | 159.5 (-115) | 161.5 | 160 ($750) | 54% / 60% | 348 | money_delta->under (145-132 fit · 28-28 fwd*); follow_move->under (296-297 fit · 47-66 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*); consensus_gap->over (105-101 fit · 20-9 fwd); pin_value->over (178-158 fit · 36-26 fwd*) |
| Mon 14:30 | MISS@CLEM | total | over **SPLIT** | +22.3 | 3-2 | 149.5 (-115) | 150.5 |  | 89% / 90% | 1236 | follow_move->under (296-297 fit · 47-66 fwd*); rlm_quiet->under (85-102 fit · 19-36 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*) |
| Mon 17:00 | WASH@BYU | total | over **SPLIT** | +22.3 | 3-2 | 165.5 (-110) | 166.5 |  | 66% / 75% | 1045 | follow_move->under (296-297 fit · 47-66 fwd*); rlm_quiet->under (85-102 fit · 19-36 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*) |
| Mon 19:30 | AMCC@WICH | total | over **SPLIT** | +22.3 | 3-2 | 144.5 (-110) | 145.5 |  | 85% / 95% | 217 | follow_move->under (296-297 fit · 47-66 fwd*); rlm_quiet->under (85-102 fit · 19-36 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*) |

## B  weighted ROI +10% to +20%

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 16:00 | TULN@GAST | moneyline | away **SPLIT** | +15.5 | 3-2 | 102 (+102) | 100 | 104 ($1,500) | 17% / 48% | 474 | follow_move->home (313-205 fit · 48-55 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->away (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*); pin_rlm->away (38-74 fit · 6-11 fwd) |
| Mon 19:00 | ILST@SCU | total | over **SPLIT** | +12.6 | 3-2 | 151.5 (-110) | 151.5 | 152 ($750) **retraced +1** | 98% / 97% | 504 | money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->under (321-339 fit · 54-55 fwd*); money_moving->under (317-346 fit · 54-59 fwd*); pin_value->over (178-158 fit · 36-26 fwd*); pin_move->over (199-189 fit · 29-43 fwd*) |
| Mon 23:30 | CSU@ARIZ | total | under **SPLIT** | +12.4 | 5-2 | 159.5 (-105) | 158.5 | 158.5 ($750) | 57% / 69% | 913 | follow_move->over (296-297 fit · 47-66 fwd*); rlm_quiet->over (85-102 fit · 19-36 fwd*); money_level->under (351-321 fit · 72-49 fwd*); sharp_gap->under (321-339 fit · 54-55 fwd*); money_moving->under (317-346 fit · 54-59 fwd*); pin_value->under (178-158 fit · 36-26 fwd*); pin_move->under (199-189 fit · 29-43 fwd*) |
| Mon 11:00 | UNI@DAV | moneyline | away **SPLIT** | +10.9 | 4-2 | 184 (+184) | 184 | 183 ($3,000) | 6% / 18% | 1277 | money_delta->away (49-165 fit · 13-21 fwd*); follow_move->home (313-205 fit · 48-55 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->away (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*); pin_rlm->away (38-74 fit · 6-11 fwd) |
| Mon 19:00 | ILST@SCU | spread | home | +13 | 2-1 | -4.5 (-120) | -5.5 | -5 ($1,500) | 0% / 0% | 504 | follow_move->away (247-261 fit · 36-43 fwd*); consensus_gap->home (85-75 fit · 13-7 fwd); pin_value->home (159-148 fit · 31-23 fwd*) |

## C  weighted ROI 0 to +10%

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 15:00 | MTU@SIU | total | under **SPLIT** | +5.9 | 2-2 | 149.5 (-110) | 150.5 |  | 61% / 57% | 323 | follow_move->under (296-297 fit · 47-66 fwd*); money_level->under (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*) |
| Mon 21:30 | UNCG@PEPP | total | over **SPLIT** | +5.9 | 2-2 | 155.5 (-115) | 152.5 |  | 93% / 91% | 686 | follow_move->over (296-297 fit · 47-66 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->under (321-339 fit · 54-55 fwd*); money_moving->under (317-346 fit · 54-59 fwd*) |
| Mon 17:00 | WASH@BYU | moneyline | away **SPLIT** | +4.6 | 4-2 | 610 (+610) | 400 |  | 3% / 16% | 1085 | money_delta->away (49-165 fit · 13-21 fwd*); follow_move->home (313-205 fit · 48-55 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->away (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*); consensus_gap->away (140-272 fit · 36-22 fwd*) |
| Mon 18:30 | UMES@YSU | moneyline | away **SPLIT** | +4.6 | 4-2 | 860 (+860) | 750 |  | 1% / 13% | 191 | money_delta->away (49-165 fit · 13-21 fwd*); follow_move->home (313-205 fit · 48-55 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->away (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*); consensus_gap->away (140-272 fit · 36-22 fwd*) |
| Mon 19:00 | CARK@UNF | moneyline | home **SPLIT** | +3.6 | 3-2 | 365 (+365) | 310 |  | 2% / 59% | 277 | follow_move->away (313-205 fit · 48-55 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->home (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*); consensus_gap->home (140-272 fit · 36-22 fwd*) |
| Mon 20:00 | WIN@ILL | spread | away **SPLIT** | +1.5 | 2-2 | 43.5 (-110) | 45.5 |  | 98% / 76% | 292 | follow_move->away (247-261 fit · 36-43 fwd*); money_level->away (315-326 fit · 34-31 fwd*); sharp_gap->home (323-310 fit · 31-33 fwd*); money_moving->home (320-313 fit · 31-33 fwd*) |
| Mon 17:30 | TEM@UTM | total | over **SPLIT** | +0.9 | 2-2 | 145.5 (-110) | 145.5 | 144 ($250) | 99% / 98% | 156 | money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->under (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*); pin_value->under (178-158 fit · 36-26 fwd*) |
| Mon 11:00 | SBON@APP | total | over | +9.3 | 4-1 | 133.5 (-110) | 133.5 | 134 ($1,500) | 81% / 86% | 1736 | money_delta->under (145-132 fit · 28-28 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*); pin_value->over (178-158 fit · 36-26 fwd*) |
| Mon 12:30 | INST@ECU | spread | home | +4.9 | 1-0 | -2.5 (-110) | -2.5 | -3 ($3,000) | 0% / 0% | 590 | pin_value->home (159-148 fit · 31-23 fwd*) |
| Mon 15:30 | SUU@ARST | spread | away | +4.9 | 1-0 | 7.5 (-110) | 7.5 | 7 ($500) | 0% / 0% | 313 | pin_value->away (159-148 fit · 31-23 fwd*) |
| Mon 16:00 | YALE@BEL | spread | home | +4.9 | 1-0 | -2.5 (-115) | -2.5 | -3 ($1,500) | 0% / 0% | 454 | pin_value->home (159-148 fit · 31-23 fwd*) |
| Mon 13:30 | AKR@WRST | spread | home | +4 | 2-0 | -1.5 (-114) | -1.5 | -2 ($1,500) | 0% / 0% | 1135 | pin_value->home (159-148 fit · 31-23 fwd*); pin_move->home (194-208 fit · 29-27 fwd*) |
| Mon 13:30 | CHAR@FGCU | total | over | +2.7 | 3-1 | 145.5 (-110) | 145.5 |  | 81% / 87% | 343 | money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*); consensus_gap->under (105-101 fit · 20-9 fwd) |
| Mon 11:00 | SBON@APP | spread | away | +2.2 | 4-1 | -4.5 (-114) | -5.5 | -5 ($3,000) | 48% / 54% | 1873 | follow_move->home (247-261 fit · 36-43 fwd*); money_level->away (315-326 fit · 34-31 fwd*); sharp_gap->away (323-310 fit · 31-33 fwd*); money_moving->away (320-313 fit · 31-33 fwd*); pin_value->away (159-148 fit · 31-23 fwd*) |
| Mon 15:30 | SUU@ARST | moneyline | home | +0.4 | 4-1 | -320 (-320) | -300 | -304 ($500) | 97% / 95% | 313 | follow_move->home (313-205 fit · 48-55 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->away (201-326 fit · 45-54 fwd*); money_moving->home (209-316 fit · 49-50 fwd*); consensus_gap->home (140-272 fit · 36-22 fwd*) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 15:30 | SUU@ARST | total | over **SPLIT** | -0.1 | 3-2 | 162.5 (-110) | 159.5 | 162.5 ($250) | 65% / 70% | 313 | money_delta->under (145-132 fit · 28-28 fwd*); follow_move->over (296-297 fit · 47-66 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->under (317-346 fit · 54-59 fwd*) |
| Mon 16:00 | YALE@BEL | moneyline | home **SPLIT** | -3.4 | 4-2 | -146 (-146) | -155 | -153 ($1,500) | 90% / 94% | 469 | follow_move->away (313-205 fit · 48-55 fwd*); rlm_quiet->away (52-110 fit · 15-35 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->home (201-326 fit · 45-54 fwd*); money_moving->home (209-316 fit · 49-50 fwd*); consensus_gap->home (140-272 fit · 36-22 fwd*) |
| Mon 12:30 | INST@ECU | total | under **SPLIT** | -4 | 4-3 | 145.5 (-105) | 146.5 | 147 ($1,500) | 52% / 55% | 590 | follow_move->under (296-297 fit · 47-66 fwd*); money_level->under (351-321 fit · 72-49 fwd*); sharp_gap->under (321-339 fit · 54-55 fwd*); money_moving->under (317-346 fit · 54-59 fwd*); consensus_gap->over (105-101 fit · 20-9 fwd); pin_value->over (178-158 fit · 36-26 fwd*); pin_move->over (199-189 fit · 29-43 fwd*) |
| Mon 22:00 | ALST@CAL | moneyline | away **SPLIT** | -4.4 | 3-2 | 1400 (+1400) | 1250 |  | 1% / 10% | 232 | money_delta->away (49-165 fit · 13-21 fwd*); follow_move->home (313-205 fit · 48-55 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->away (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*) |
| Mon 14:00 | TLSA@ORST | moneyline | home **SPLIT** | -9.7 | 4-3 | -265 (-265) | -275 | -269 ($1,500) | 96% / 97% | 1075 | follow_move->away (313-205 fit · 48-55 fwd*); rlm_quiet->away (52-110 fit · 15-35 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->home (201-326 fit · 45-54 fwd*); money_moving->home (209-316 fit · 49-50 fwd*); consensus_gap->home (140-272 fit · 36-22 fwd*); pin_move->away (103-103 fit · 22-19 fwd*) |
| Mon 14:30 | MISS@CLEM | moneyline | away **SPLIT** | -12.4 | 3-2 | -220 (-220) | -245 |  | 89% / 93% | 1236 | follow_move->home (313-205 fit · 48-55 fwd*); rlm_quiet->home (52-110 fit · 15-35 fwd*); money_level->away (416-157 fit · 70-40 fwd*); sharp_gap->away (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*) |
| Mon 16:00 | TULN@GAST | total | under **SPLIT** | -15.1 | 3-3 | 148.5 (-110) | 149.5 | 148 ($750) | 16% / 12% | 474 | follow_move->under (296-297 fit · 47-66 fwd*); rlm_quiet->under (85-102 fit · 19-36 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*); pin_value->under (178-158 fit · 36-26 fwd*) |
| Mon 19:00 | GASO@NKU | moneyline | away **SPLIT** | -15.9 | 7-2 | 118 (+118) | 145 | 128 ($1,500) | 7% / 18% | 504 | follow_move->away (313-205 fit · 48-55 fwd*); rlm_ratio->away (37-80 fit · 9-26 fwd*); rlm_quiet->away (52-110 fit · 15-35 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->away (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*); consensus_gap->home (140-272 fit · 36-22 fwd*); pin_move->away (103-103 fit · 22-19 fwd*); pin_rlm->away (38-74 fit · 6-11 fwd) |
| Mon 19:00 | ILST@SCU | moneyline | away **SPLIT** | -15.9 | 7-2 | 172 (+172) | 180 | 170 ($1,500) | 1% / 2% | 504 | follow_move->away (313-205 fit · 48-55 fwd*); rlm_ratio->away (37-80 fit · 9-26 fwd*); rlm_quiet->away (52-110 fit · 15-35 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->away (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*); consensus_gap->home (140-272 fit · 36-22 fwd*); pin_move->away (103-103 fit · 22-19 fwd*); pin_rlm->away (38-74 fit · 6-11 fwd) |
| Mon 20:00 | SFA@UVU | moneyline | away **SPLIT** | -19.2 | 3-2 | 136 (+136) | 145 | 141 ($500) | 0% / 1% | 171 | follow_move->away (313-205 fit · 48-55 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->away (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*); consensus_gap->home (140-272 fit · 36-22 fwd*) |
| Mon 21:30 | UNCG@PEPP | moneyline | away **SPLIT** | -19.2 | 3-2 | 420 (+420) | 475 |  | 0% / 5% | 691 | follow_move->away (313-205 fit · 48-55 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->away (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*); consensus_gap->home (140-272 fit · 36-22 fwd*) |
| Mon 22:00 | EWU@UNLV | moneyline | away **SPLIT** | -19.2 | 3-2 | 255 (+255) | 260 | 270 ($1,500) | 0% / 5% | 348 | follow_move->away (313-205 fit · 48-55 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->away (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*); consensus_gap->home (140-272 fit · 36-22 fwd*) |
| Mon 15:30 | IUIN@WM | total | over **SPLIT** | -21.1 | 4-2 | 167.5 (-110) | 165.5 | 166.5 ($250) | 56% / 73% | 393 | follow_move->over (296-297 fit · 47-66 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*); consensus_gap->under (105-101 fit · 20-9 fwd); pin_value->under (178-158 fit · 36-26 fwd*) |
| Mon 16:00 | YALE@BEL | total | over **SPLIT** | -35.4 | 5-3 | 145.5 (-110) | 143.5 | 144 ($750) | 56% / 63% | 469 | money_delta->under (145-132 fit · 28-28 fwd*); follow_move->over (296-297 fit · 47-66 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*); consensus_gap->under (105-101 fit · 20-9 fwd); pin_value->under (178-158 fit · 36-26 fwd*); pin_move->over (199-189 fit · 29-43 fwd*) |
| Mon 22:00 | ALST@CAL | total | under **SPLIT** | -35.4 | 4-2 | 145.5 (-110) | 146.5 |  | 1% / 5% | 232 | follow_move->under (296-297 fit · 47-66 fwd*); rlm_ratio->under (122-102 fit · 16-20 fwd*); rlm_quiet->under (85-102 fit · 19-36 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->under (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*) |
| Mon 16:30 | NEV@SF | total | over **SPLIT** | -38.8 | 5-2 | 142.5 (-106) | 138.5 | 142 ($750) | 69% / 80% | 631 | money_delta->under (145-132 fit · 28-28 fwd*); follow_move->over (296-297 fit · 47-66 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*); pin_value->under (178-158 fit · 36-26 fwd*); pin_move->over (199-189 fit · 29-43 fwd*) |
| Mon 20:00 | MONM@UNC | moneyline | away **SPLIT** | -42.1 | 6-2 | 1400 (+1400) | 1400 |  | 1% / 7% | 489 | money_delta->away (49-165 fit · 13-21 fwd*); follow_move->away (313-205 fit · 48-55 fwd*); rlm_ratio->away (37-80 fit · 9-26 fwd*); rlm_quiet->away (52-110 fit · 15-35 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->away (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*); consensus_gap->home (140-272 fit · 36-22 fwd*) |
| Mon 22:00 | EWU@UNLV | spread | home | -0.9 | 1-0 | -7.5 (-110) | -7.5 | -7.5 ($1,500) | 0% / 0% | 348 | pin_move->home (194-208 fit · 29-27 fwd*) |
| Mon 19:00 | CARK@UNF | spread | home | -1.4 | 1-0 | 9.5 (-110) | 9.5 |  | 0% / 0% | 277 | consensus_gap->home (85-75 fit · 13-7 fwd) |
| Mon 19:00 | FDU@IONA | moneyline | home | -4.4 | 2-1 | -465 (-465) | -450 |  | 99% / 97% | 212 | follow_move->home (313-205 fit · 48-55 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->away (201-326 fit · 45-54 fwd*) |
| Mon 19:00 | FDU@IONA | total | over | -6.7 | 3-1 | 137.5 (-106) | 132.5 |  | 98% / 99% | 212 | follow_move->over (296-297 fit · 47-66 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); consensus_gap->under (105-101 fit · 20-9 fwd) |
| Mon 11:00 | UNI@DAV | spread | away | -7.3 | 4-0 | 5.5 (-110) | 5.5 | 5 ($3,000) | 58% / 60% | 1277 | money_level->away (315-326 fit · 34-31 fwd*); sharp_gap->away (323-310 fit · 31-33 fwd*); money_moving->away (320-313 fit · 31-33 fwd*); pin_value->away (159-148 fit · 31-23 fwd*) |
| Mon 19:00 | CARK@UNF | total | over | -8.5 | 3-1 | 164.5 (-110) | 163.5 |  | 63% / 53% | 277 | follow_move->over (296-297 fit · 47-66 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->under (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*) |
| Mon 19:00 | NCAT@SCST | moneyline | away | -8.6 | 3-1 | -142 (-142) | -145 |  | 97% / 74% | 186 | follow_move->away (313-205 fit · 48-55 fwd*); money_level->away (416-157 fit · 70-40 fwd*); sharp_gap->home (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*) |
| Mon 15:00 | MTU@SIU | spread | home | -9.5 | 1-0 | -2.5 (-110) | -1.5 |  | 0% / 0% | 323 | follow_move->home (247-261 fit · 36-43 fwd*) |
| Mon 17:00 | WASH@BYU | spread | home | -9.5 | 1-0 | -12.5 (-110) | -10.5 |  | 0% / 0% | 1045 | follow_move->home (247-261 fit · 36-43 fwd*) |
| Mon 18:30 | UMES@YSU | spread | home | -9.5 | 1-0 | -14.5 (-110) | -13.5 |  | 0% / 0% | 191 | follow_move->home (247-261 fit · 36-43 fwd*) |
| Mon 19:00 | FDU@IONA | spread | home | -9.5 | 1-0 | -9.5 (-110) | -8.5 |  | 0% / 0% | 201 | follow_move->home (247-261 fit · 36-43 fwd*) |
| Mon 11:00 | SBON@APP | moneyline | home | -10.1 | 7-1 | 160 (+160) | 180 | 174 ($3,000) **retraced +1** | 10% / 46% | 1873 | money_delta->home (49-165 fit · 13-21 fwd*); follow_move->home (313-205 fit · 48-55 fwd*); rlm_ratio->home (37-80 fit · 9-26 fwd*); money_level->away (416-157 fit · 70-40 fwd*); sharp_gap->home (201-326 fit · 45-54 fwd*); money_moving->home (209-316 fit · 49-50 fwd*); pin_move->home (103-103 fit · 22-19 fwd*); pin_rlm->home (38-74 fit · 6-11 fwd) |
| Mon 20:00 | MONM@UNC | spread | away | -10.4 | 2-0 | 19.5 (-110) | 20.5 | 19.5 ($1,500) | 0% / 0% | 489 | follow_move->away (247-261 fit · 36-43 fwd*); pin_move->away (194-208 fit · 29-27 fwd*) |
| Mon 23:30 | CSU@ARIZ | spread | away | -10.4 | 2-0 | 16.5 (-110) | 17.5 | 16.5 ($1,500) | 0% / 0% | 928 | follow_move->away (247-261 fit · 36-43 fwd*); pin_move->away (194-208 fit · 29-27 fwd*) |
| Mon 20:00 | DEN@KU | total | under | -10.7 | 4-1 | 157.5 (-110) | 157.5 | 158 ($750) | 40% / 51% | 307 | money_delta->under (145-132 fit · 28-28 fwd*); money_level->under (351-321 fit · 72-49 fwd*); sharp_gap->under (321-339 fit · 54-55 fwd*); money_moving->under (317-346 fit · 54-59 fwd*); pin_value->over (178-158 fit · 36-26 fwd*) |
| Mon 19:30 | AMCC@WICH | spread | home | -11 | 2-1 | -21.5 (-110) | -21.5 |  | 1% / 27% | 217 | money_level->away (315-326 fit · 34-31 fwd*); sharp_gap->home (323-310 fit · 31-33 fwd*); money_moving->home (320-313 fit · 31-33 fwd*) |
| Mon 19:30 | AMCC@WICH | moneyline | home | -11 | 4-0 | -7000 (-7000) | -5000 |  | 99% / 100% | 217 | follow_move->home (313-205 fit · 48-55 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->home (201-326 fit · 45-54 fwd*); consensus_gap->home (140-272 fit · 36-22 fwd*) |
| Mon 13:00 | LBSU@FIU | spread | away | -12.2 | 3-0 | 9.5 (-110) | 9.5 | 9.5 ($3,000) | 50% / 51% | 484 | money_level->away (315-326 fit · 34-31 fwd*); sharp_gap->away (323-310 fit · 31-33 fwd*); money_moving->away (320-313 fit · 31-33 fwd*) |
| Mon 14:00 | TLSA@ORST | spread | home | -12.2 | 3-0 | -6.5 (-110) | -6.5 | -6.5 ($1,500) | 53% / 56% | 1075 | money_level->home (315-326 fit · 34-31 fwd*); sharp_gap->home (323-310 fit · 31-33 fwd*); money_moving->home (320-313 fit · 31-33 fwd*) |
| Mon 14:30 | MISS@CLEM | spread | away | -12.2 | 3-0 | -5.5 (-110) | -5.5 |  | 69% / 70% | 1236 | money_level->away (315-326 fit · 34-31 fwd*); sharp_gap->away (323-310 fit · 31-33 fwd*); money_moving->away (320-313 fit · 31-33 fwd*) |
| Mon 16:30 | NEV@SF | spread | home | -12.2 | 3-0 | 7.5 (-114) | 7.5 | 7.5 ($1,500) | 59% / 68% | 615 | money_level->home (315-326 fit · 34-31 fwd*); sharp_gap->home (323-310 fit · 31-33 fwd*); money_moving->home (320-313 fit · 31-33 fwd*) |
| Mon 20:00 | DEN@KU | spread | away | -14.4 | 1-1 | 35.5 (-104) | 37.5 | 36.5 ($1,500) | 0% / 0% | 307 | follow_move->away (247-261 fit · 36-43 fwd*); pin_value->home (159-148 fit · 31-23 fwd*) |
| Mon 16:30 | NEV@SF | moneyline | away | -15.2 | 5-0 | -310 (-310) | -285 | -311 ($1,500) | 95% / 96% | 615 | follow_move->away (313-205 fit · 48-55 fwd*); money_level->away (416-157 fit · 70-40 fwd*); sharp_gap->away (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*); consensus_gap->away (140-272 fit · 36-22 fwd*) |
| Mon 19:00 | GASO@NKU | spread | away | -15.3 | 2-1 | 2.5 (-108) | 3.5 | 3 ($1,500) | 0% / 0% | 504 | follow_move->away (247-261 fit · 36-43 fwd*); pin_value->home (159-148 fit · 31-23 fwd*); pin_move->away (194-208 fit · 29-27 fwd*) |
| Mon 15:00 | MTU@SIU | moneyline | home | -15.8 | 3-1 | -138 (-138) | -118 |  | 86% / 94% | 323 | follow_move->home (313-205 fit · 48-55 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->home (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*) |
| Mon 19:00 | GASO@NKU | total | over | -17.3 | 4-0 | 166.5 (-110) | 164.5 | 166.5 ($750) | 51% / 59% | 494 | follow_move->over (296-297 fit · 47-66 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*) |
| Mon 20:00 | WIN@ILL | total | over | -17.3 | 4-0 | 180.5 (-110) | 178.5 |  | 62% / 81% | 292 | follow_move->over (296-297 fit · 47-66 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*) |
| Mon 21:00 | VCU@PROV | total | over | -17.3 | 4-0 | 154.5 (-115) | 152.5 |  | 71% / 72% | 1156 | follow_move->over (296-297 fit · 47-66 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*) |
| Mon 13:00 | LBSU@FIU | moneyline | away | -17.8 | 7-1 | 360 (+360) | 390 | 370 ($3,000) | 4% / 20% | 484 | money_delta->away (49-165 fit · 13-21 fwd*); follow_move->away (313-205 fit · 48-55 fwd*); rlm_ratio->away (37-80 fit · 9-26 fwd*); rlm_quiet->away (52-110 fit · 15-35 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->away (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*); pin_rlm->away (38-74 fit · 6-11 fwd) |
| Mon 17:30 | TEM@UTM | moneyline | home | -17.8 | 7-1 | 152 (+152) | 190 | 162 ($500) | 4% / 8% | 176 | money_delta->home (49-165 fit · 13-21 fwd*); follow_move->home (313-205 fit · 48-55 fwd*); rlm_ratio->home (37-80 fit · 9-26 fwd*); rlm_quiet->home (52-110 fit · 15-35 fwd*); money_level->away (416-157 fit · 70-40 fwd*); sharp_gap->home (201-326 fit · 45-54 fwd*); money_moving->home (209-316 fit · 49-50 fwd*); pin_rlm->home (38-74 fit · 6-11 fwd) |
| Mon 13:30 | AKR@WRST | moneyline | home | -17.9 | 5-0 | -122 (-122) | -115 | -131 ($1,500) | 80% / 98% | 1135 | follow_move->home (313-205 fit · 48-55 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->home (201-326 fit · 45-54 fwd*); money_moving->home (209-316 fit · 49-50 fwd*); pin_move->home (103-103 fit · 22-19 fwd*) |
| Mon 20:00 | SFA@UVU | total | under | -21 | 6-1 | 151.5 (-110) | 152.5 | 151.5 ($250) | 12% / 60% | 171 | money_delta->under (145-132 fit · 28-28 fwd*); follow_move->under (296-297 fit · 47-66 fwd*); rlm_ratio->under (122-102 fit · 16-20 fwd*); money_level->under (351-321 fit · 72-49 fwd*); sharp_gap->under (321-339 fit · 54-55 fwd*); money_moving->under (317-346 fit · 54-59 fwd*); consensus_gap->over (105-101 fit · 20-9 fwd) |
| Mon 13:30 | CHAR@FGCU | spread | home | -21.7 | 4-0 | 6.5 (-110) | 7.5 |  | 54% / 55% | 343 | follow_move->home (247-261 fit · 36-43 fwd*); money_level->home (315-326 fit · 34-31 fwd*); sharp_gap->home (323-310 fit · 31-33 fwd*); money_moving->home (320-313 fit · 31-33 fwd*) |
| Mon 20:00 | MONM@UNC | total | under | -22.5 | 2-1 | 153.5 (-110) | 153.5 | 153.5 ($750) | 8% / 12% | 489 | money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->under (321-339 fit · 54-55 fwd*); money_moving->under (317-346 fit · 54-59 fwd*) |
| Mon 12:30 | INST@ECU | moneyline | home | -24.2 | 4-0 | -140 (-140) | -138 | -149 ($3,000) | 87% / 99% | 590 | follow_move->home (313-205 fit · 48-55 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->home (201-326 fit · 45-54 fwd*); money_moving->home (209-316 fit · 49-50 fwd*) |
| Mon 21:00 | VCU@PROV | moneyline | home | -24.2 | 4-0 | -120 (-120) | -115 |  | 76% / 93% | 1156 | follow_move->home (313-205 fit · 48-55 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->home (201-326 fit · 45-54 fwd*); money_moving->home (209-316 fit · 49-50 fwd*) |
| Mon 11:00 | UNI@DAV | total | over | -24.5 | 4-1 | 142.5 (-110) | 141.5 | 141.5 ($1,500) | 88% / 91% | 1358 | follow_move->over (296-297 fit · 47-66 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*); pin_value->under (178-158 fit · 36-26 fwd*) |
| Mon 13:30 | CHAR@FGCU | moneyline | home | -28.5 | 5-1 | 215 (+215) | 260 |  | 7% / 11% | 343 | follow_move->home (313-205 fit · 48-55 fwd*); rlm_ratio->home (37-80 fit · 9-26 fwd*); rlm_quiet->home (52-110 fit · 15-35 fwd*); money_level->away (416-157 fit · 70-40 fwd*); sharp_gap->home (201-326 fit · 45-54 fwd*); money_moving->home (209-316 fit · 49-50 fwd*) |
| Mon 15:30 | IUIN@WM | moneyline | home | -29 | 3-1 | -194 (-194) | -190 | -186 ($500) | 95% / 97% | 393 | follow_move->home (313-205 fit · 48-55 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->home (201-326 fit · 45-54 fwd*); consensus_gap->away (140-272 fit · 36-22 fwd*) |
| Mon 23:30 | CSU@ARIZ | moneyline | away | -33.1 | 7-1 | 1100 (+1100) | 1200 | 1046 ($1,500) | 2% / 34% | 928 | money_delta->away (49-165 fit · 13-21 fwd*); follow_move->away (313-205 fit · 48-55 fwd*); rlm_ratio->away (37-80 fit · 9-26 fwd*); rlm_quiet->away (52-110 fit · 15-35 fwd*); money_level->home (416-157 fit · 70-40 fwd*); sharp_gap->away (201-326 fit · 45-54 fwd*); money_moving->away (209-316 fit · 49-50 fwd*); pin_value->away (18-54 fit · 5-1 fwd) |
| Mon 13:00 | LBSU@FIU | total | under | -34.4 | 5-0 | 159.5 (-110) | 160.5 | 159.5 ($1,500) | 84% / 85% | 459 | follow_move->under (296-297 fit · 47-66 fwd*); money_level->under (351-321 fit · 72-49 fwd*); sharp_gap->under (321-339 fit · 54-55 fwd*); money_moving->under (317-346 fit · 54-59 fwd*); pin_move->under (199-189 fit · 29-43 fwd*) |
| Mon 13:30 | AKR@WRST | total | over | -49 | 5-1 | 148.5 (-110) | 147.5 | 149 ($750) | 43% / 46% | 1135 | follow_move->over (296-297 fit · 47-66 fwd*); money_level->under (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*); pin_value->over (178-158 fit · 36-26 fwd*); pin_move->over (199-189 fit · 29-43 fwd*) |
| Mon 18:30 | UMES@YSU | total | under | -52.6 | 6-1 | 133.5 (-110) | 135.5 |  | 7% / 21% | 191 | money_delta->under (145-132 fit · 28-28 fwd*); follow_move->under (296-297 fit · 47-66 fwd*); rlm_ratio->under (122-102 fit · 16-20 fwd*); rlm_quiet->under (85-102 fit · 19-36 fwd*); money_level->over (351-321 fit · 72-49 fwd*); sharp_gap->under (321-339 fit · 54-55 fwd*); money_moving->under (317-346 fit · 54-59 fwd*) |
| Mon 14:00 | TLSA@ORST | total | over | -55.4 | 6-1 | 153.5 (-115) | 151.5 | 154 ($750) | 42% / 44% | 1075 | follow_move->over (296-297 fit · 47-66 fwd*); rlm_quiet->over (85-102 fit · 19-36 fwd*); money_level->under (351-321 fit · 72-49 fwd*); sharp_gap->over (321-339 fit · 54-55 fwd*); money_moving->over (317-346 fit · 54-59 fwd*); pin_value->over (178-158 fit · 36-26 fwd*); pin_move->over (199-189 fit · 29-43 fwd*) |

