# CBB board

Generated 2026-11-23 01:59 UTC. Upcoming games with a FanDuel line. Every game is listed;
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
| FanDuel moved vs public | UNI@DAV | total | under | FanDuel | 141.5 -> 140.5 |  | 140.5 | 14% | 1.57 | 200-225 fit · 23-45 fwd |

## A  weighted ROI >= +20%

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 00:00 | SJSU@L-IL | total | over **SPLIT** | +24.1 | 3-2 | 146.5 (-110) | 148.5 |  | 75% / 77% | 1580 | follow_move->under (296-297 fit · 42-63 fwd*); rlm_quiet->under (85-102 fit · 16-34 fwd*); money_level->over (351-321 fit · 68-45 fwd*); sharp_gap->over (321-339 fit · 50-52 fwd*); money_moving->over (317-346 fit · 50-56 fwd*) |
| Mon 14:30 | MISS@CLEM | total | over **SPLIT** | +24.1 | 3-2 | 148.5 (-115) | 150.5 |  | 81% / 88% | 186 | follow_move->under (296-297 fit · 42-63 fwd*); rlm_quiet->under (85-102 fit · 16-34 fwd*); money_level->over (351-321 fit · 68-45 fwd*); sharp_gap->over (321-339 fit · 50-52 fwd*); money_moving->over (317-346 fit · 50-56 fwd*) |
| Mon 16:30 | NEV@SF | total | over **SPLIT** | +24.1 | 3-2 | 137.5 (-115) | 138.5 | 137.5 ($250) | 89% / 97% | 116 | follow_move->under (296-297 fit · 42-63 fwd*); rlm_quiet->under (85-102 fit · 16-34 fwd*); money_level->over (351-321 fit · 68-45 fwd*); sharp_gap->over (321-339 fit · 50-52 fwd*); money_moving->over (317-346 fit · 50-56 fwd*) |

## C  weighted ROI 0 to +10%

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 19:00 | ILST@SCU | total | under | +5.4 | 1-0 | 151.5 (-110) | 151.5 | 151 ($250) | 0% / 0% | 60 | pin_value->under (178-158 fit · 34-26 fwd*) |
| Mon 20:00 | DEN@KU | total | over | +5.4 | 1-0 | 157.5 (-110) | 157.5 | 158 ($250) | 0% / 0% | 40 | pin_value->over (178-158 fit · 34-26 fwd*) |
| Mon 11:00 | UNI@DAV | spread | away | +4.1 | 1-0 | 5.5 (-110) | 5.5 | 5 ($500) | 0% / 0% | 121 | pin_value->away (159-148 fit · 29-22 fwd*) |
| Mon 12:30 | INST@ECU | spread | home | +4.1 | 1-0 | -2.5 (-110) | -2.5 | -3 ($500) | 0% / 0% | 65 | pin_value->home (159-148 fit · 29-22 fwd*) |
| Mon 20:00 | MONM@UNC | spread | home | +4.1 | 1-0 | -20.5 (-118) | -20.5 | -21 ($500) | 0% / 0% | 45 | pin_value->home (159-148 fit · 29-22 fwd*) |
| Mon 11:00 | SBON@APP | total | over | +4 | 4-0 | 133.5 (-110) | 133.5 | 134 ($250) | 92% / 96% | 232 | money_level->over (351-321 fit · 68-45 fwd*); sharp_gap->over (321-339 fit · 50-52 fwd*); money_moving->over (317-346 fit · 50-56 fwd*); pin_value->over (178-158 fit · 34-26 fwd*) |
| Mon 13:30 | AKR@WRST | total | over | +4 | 4-0 | 147.5 (-110) | 147.5 | 148 ($250) | 80% / 83% | 141 | money_level->over (351-321 fit · 68-45 fwd*); sharp_gap->over (321-339 fit · 50-52 fwd*); money_moving->over (317-346 fit · 50-56 fwd*); pin_value->over (178-158 fit · 34-26 fwd*) |
| Mon 11:00 | SBON@APP | spread | home | +2.7 | 2-0 | 5.5 (-110) | 5.5 | 5 ($500) | 0% / 0% | 131 | consensus_gap->home (85-75 fit · 10-7 fwd); pin_value->home (159-148 fit · 29-22 fwd*) |
| Mon 13:30 | AKR@WRST | moneyline | home | +0.7 | 1-0 | -115 (-115) | -115 | -116 ($500) | 0% / 0% | 95 | consensus_gap->home (140-272 fit · 32-22 fwd*) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 17:00 | WASH@BYU | moneyline | away **SPLIT** | -8.5 | 3-3 | 500 (+500) | 400 |  | 3% / 11% | 176 | money_delta->away (49-165 fit · 12-19 fwd*); follow_move->home (313-205 fit · 45-52 fwd*); money_level->home (416-157 fit · 66-38 fwd*); sharp_gap->away (201-326 fit · 42-51 fwd*); money_moving->away (209-316 fit · 46-47 fwd*); consensus_gap->home (140-272 fit · 32-22 fwd*) |
| Mon 12:30 | INST@ECU | moneyline | home **SPLIT** | -24.6 | 4-3 | -137 (-137) | -138 | -147 ($500) | 90% / 91% | 80 | follow_move->away (313-205 fit · 45-52 fwd*); rlm_quiet->away (52-110 fit · 14-33 fwd*); money_level->home (416-157 fit · 66-38 fwd*); sharp_gap->home (201-326 fit · 42-51 fwd*); money_moving->home (209-316 fit · 46-47 fwd*); consensus_gap->home (140-272 fit · 32-22 fwd*); pin_move->away (103-103 fit · 21-17 fwd*) |
| Mon 12:30 | INST@ECU | total | under **SPLIT** | -55.9 | 4-2 | 145.5 (-105) | 146.5 | 146 ($250) | 28% / 33% | 80 | follow_move->under (296-297 fit · 42-63 fwd*); rlm_quiet->under (85-102 fit · 16-34 fwd*); money_level->over (351-321 fit · 68-45 fwd*); sharp_gap->under (321-339 fit · 50-52 fwd*); money_moving->under (317-346 fit · 50-56 fwd*); pin_value->over (178-158 fit · 34-26 fwd*) |
| Mon 11:00 | UNI@DAV | total | under **SPLIT** | -56.2 | 5-3 | 140.5 (-110) | 141.5 | 141.5 ($250) | 14% / 22% | 166 | follow_move->under (296-297 fit · 42-63 fwd*); rlm_ratio->under (122-102 fit · 15-19 fwd*); rlm_quiet->under (85-102 fit · 16-34 fwd*); money_level->over (351-321 fit · 68-45 fwd*); sharp_gap->under (321-339 fit · 50-52 fwd*); money_moving->under (317-346 fit · 50-56 fwd*); consensus_gap->over (105-101 fit · 16-9 fwd); pin_value->over (178-158 fit · 34-26 fwd*) |
| Mon 16:00 | TULN@GAST | moneyline | away | -6.1 | 1-0 | -102 (-102) | 100 | 102 ($500) | 0% / 0% | 60 | follow_move->away (313-205 fit · 45-52 fwd*) |
| Mon 19:00 | GASO@NKU | moneyline | away | -6.1 | 1-0 | 138 (+138) | 145 | 136 ($500) | 0% / 0% | 126 | follow_move->away (313-205 fit · 45-52 fwd*) |
| Mon 19:00 | ILST@SCU | moneyline | away | -6.1 | 1-0 | 172 (+172) | 180 | 182 ($500) | 0% / 0% | 60 | follow_move->away (313-205 fit · 45-52 fwd*) |
| Mon 21:00 | VCU@PROV | moneyline | away | -6.1 | 1-0 | -106 (-106) | -105 |  | 0% / 0% | 116 | follow_move->away (313-205 fit · 45-52 fwd*) |
| Mon 22:00 | EWU@UNLV | moneyline | away | -6.1 | 1-0 | 255 (+255) | 260 |  | 0% / 0% | 50 | follow_move->away (313-205 fit · 45-52 fwd*) |
| Mon 20:00 | MONM@UNC | moneyline | away | -6.8 | 1-1 | 1600 (+1600) | 1400 |  | 0% / 0% | 45 | follow_move->away (313-205 fit · 45-52 fwd*); consensus_gap->home (140-272 fit · 32-22 fwd*) |
| Mon 13:00 | LBSU@FIU | moneyline | away | -10.4 | 3-1 | 390 (+390) | 390 | 375 ($500) | 2% / 5% | 95 | money_level->home (416-157 fit · 66-38 fwd*); sharp_gap->away (201-326 fit · 42-51 fwd*); money_moving->away (209-316 fit · 46-47 fwd*); consensus_gap->away (140-272 fit · 32-22 fwd*) |
| Mon 11:00 | SBON@APP | moneyline | home | -11.1 | 2-1 | 180 (+180) | 180 | 183 ($500) | 11% / 31% | 232 | money_level->away (416-157 fit · 66-38 fwd*); sharp_gap->home (201-326 fit · 42-51 fwd*); money_moving->home (209-316 fit · 46-47 fwd*) |
| Mon 00:00 | SJSU@L-IL | spread | home | -12.8 | 1-0 | -4.5 (-105) | -3.5 |  | 0% / 0% | 1418 | follow_move->home (247-261 fit · 31-41 fwd*) |
| Mon 14:30 | MISS@CLEM | spread | away | -12.8 | 1-0 | -6.5 (-102) | -5.5 |  | 0% / 0% | 131 | follow_move->away (247-261 fit · 31-41 fwd*) |
| Mon 17:00 | WASH@BYU | spread | home | -12.8 | 1-0 | -11.5 (-110) | -10.5 |  | 0% / 0% | 121 | follow_move->home (247-261 fit · 31-41 fwd*) |
| Mon 20:00 | DEN@KU | spread | away | -12.8 | 1-0 | 36.5 (-104) | 37.5 | 36.5 ($500) | 0% / 0% | 50 | follow_move->away (247-261 fit · 31-41 fwd*) |
| Mon 23:30 | CSU@ARIZ | spread | away | -12.8 | 1-0 | 16.5 (-102) | 17.5 |  | 0% / 0% | 227 | follow_move->away (247-261 fit · 31-41 fwd*) |
| Mon 14:30 | MISS@CLEM | moneyline | away | -13.9 | 2-0 | -250 (-250) | -245 |  | 92% / 92% | 186 | follow_move->away (313-205 fit · 45-52 fwd*); money_level->away (416-157 fit · 66-38 fwd*) |
| Mon 19:00 | ILST@SCU | spread | away | -16.9 | 1-1 | 4.5 (-102) | 5.5 | 5 ($500) | 0% / 0% | 60 | follow_move->away (247-261 fit · 31-41 fwd*); pin_value->home (159-148 fit · 29-22 fwd*) |
| Sun 21:30 | SEA@UCSD | spread | away | -18.3 | 4-0 | 1.5 (-128) | 1.5 |  | 48% / 57% | 2155 | money_level->away (315-326 fit · 31-29 fwd*); sharp_gap->away (323-310 fit · 28-32 fwd*); money_moving->away (320-313 fit · 28-32 fwd*); consensus_gap->away (85-75 fit · 10-7 fwd) |
| Mon 14:00 | TLSA@ORST | total | over | -18.8 | 1-0 | 152.5 (-110) | 151.5 | 152.5 ($500) | 0% / 0% | 80 | follow_move->over (296-297 fit · 42-63 fwd*) |
| Mon 17:00 | WASH@BYU | total | under | -18.8 | 1-0 | 165.5 (-105) | 166.5 |  | 0% / 0% | 121 | follow_move->under (296-297 fit · 42-63 fwd*) |
| Mon 19:00 | GASO@NKU | total | over | -18.8 | 1-0 | 166.5 (-110) | 164.5 | 166.5 ($250) | 0% / 0% | 126 | follow_move->over (296-297 fit · 42-63 fwd*) |
| Mon 21:00 | VCU@PROV | total | over | -18.8 | 1-0 | 153.5 (-115) | 152.5 |  | 0% / 0% | 116 | follow_move->over (296-297 fit · 42-63 fwd*) |
| Mon 22:00 | EWU@UNLV | total | under | -18.8 | 1-0 | 159.5 (-105) | 161.5 |  | 0% / 0% | 50 | follow_move->under (296-297 fit · 42-63 fwd*) |
| Sun 21:30 | SEA@UCSD | total | over | -20.2 | 4-0 | 148.5 (-110) | 143.5 |  | 50% / 55% | 2155 | follow_move->over (296-297 fit · 42-63 fwd*); money_level->over (351-321 fit · 68-45 fwd*); sharp_gap->over (321-339 fit · 50-52 fwd*); money_moving->over (317-346 fit · 50-56 fwd*) |
| Mon 23:30 | CSU@ARIZ | moneyline | away | -22.7 | 5-1 | 1100 (+1100) | 1200 |  | 3% / 55% | 252 | money_delta->away (49-165 fit · 12-19 fwd*); follow_move->home (313-205 fit · 45-52 fwd*); money_level->away (416-157 fit · 66-38 fwd*); sharp_gap->away (201-326 fit · 42-51 fwd*); money_moving->away (209-316 fit · 46-47 fwd*); consensus_gap->away (140-272 fit · 32-22 fwd*) |
| Mon 13:00 | LBSU@FIU | total | under | -25 | 2-1 | 160.5 (-110) | 160.5 | 160.5 ($250) | 40% / 47% | 95 | money_level->over (351-321 fit · 68-45 fwd*); sharp_gap->under (321-339 fit · 50-52 fwd*); money_moving->under (317-346 fit · 50-56 fwd*) |
| Mon 11:00 | UNI@DAV | moneyline | home | -26 | 4-0 | -215 (-215) | -215 | -226 ($500) | 96% / 99% | 121 | money_level->home (416-157 fit · 66-38 fwd*); sharp_gap->home (201-326 fit · 42-51 fwd*); money_moving->home (209-316 fit · 46-47 fwd*); consensus_gap->home (140-272 fit · 32-22 fwd*) |
| Mon 00:00 | SJSU@L-IL | moneyline | home | -32.8 | 4-0 | -182 (-182) | -175 |  | 91% / 97% | 1580 | follow_move->home (313-205 fit · 45-52 fwd*); money_level->home (416-157 fit · 66-38 fwd*); sharp_gap->home (201-326 fit · 42-51 fwd*); money_moving->home (209-316 fit · 46-47 fwd*) |
| Mon 14:00 | TLSA@ORST | moneyline | home | -32.8 | 4-0 | -295 (-295) | -275 | -281 ($1,000) | 97% / 99% | 80 | follow_move->home (313-205 fit · 45-52 fwd*); money_level->home (416-157 fit · 66-38 fwd*); sharp_gap->home (201-326 fit · 42-51 fwd*); money_moving->home (209-316 fit · 46-47 fwd*) |
| Mon 16:30 | NEV@SF | moneyline | away | -32.8 | 4-0 | -310 (-310) | -285 | -313 ($500) | 98% / 99% | 116 | follow_move->away (313-205 fit · 45-52 fwd*); money_level->away (416-157 fit · 66-38 fwd*); sharp_gap->away (201-326 fit · 42-51 fwd*); money_moving->away (209-316 fit · 46-47 fwd*) |
| Sun 21:30 | SEA@UCSD | moneyline | away | -36.3 | 5-1 | -111 (-111) | -106 |  | 47% / 61% | 2155 | money_delta->away (49-165 fit · 12-19 fwd*); follow_move->away (313-205 fit · 45-52 fwd*); money_level->away (416-157 fit · 66-38 fwd*); sharp_gap->away (201-326 fit · 42-51 fwd*); money_moving->away (209-316 fit · 46-47 fwd*); consensus_gap->home (140-272 fit · 32-22 fwd*) |
| Mon 16:00 | TULN@GAST | total | under | -48.5 | 6-1 | 148.5 (-110) | 149.5 | 148 ($250) | 19% / 21% | 85 | follow_move->under (296-297 fit · 42-63 fwd*); rlm_quiet->under (85-102 fit · 16-34 fwd*); money_level->over (351-321 fit · 68-45 fwd*); sharp_gap->under (321-339 fit · 50-52 fwd*); money_moving->under (317-346 fit · 50-56 fwd*); consensus_gap->under (105-101 fit · 16-9 fwd); pin_value->under (178-158 fit · 34-26 fwd*) |

