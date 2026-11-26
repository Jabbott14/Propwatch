# CBB board

Generated 2026-11-26 03:48 UTC. Upcoming games with a FanDuel line. Every game is listed;
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
| FanDuel moved vs public | GONZ@BAY | moneyline | home | FanDuel | 185 -> 146 |  | 146 | 12% | 3.25 | 200-225 fit · 69-107 fwd |
| FanDuel moved vs public | ISU@TENN | spread | away | FanDuel | -1.5 -> -2.5 |  | -2.5 | 25% | 2.76 | 200-225 fit · 69-107 fwd |
| FanDuel moved vs public | IW@HAW | total | under | FanDuel | 142.5 -> 139.5 | — | 139.5 | 12% | 1.33 | 200-225 fit · 69-107 fwd |
| FanDuel moved vs public | MICH@MIA | moneyline | away | FanDuel | 136 -> 112 |  | 112 | 13% | 1.38 | 200-225 fit · 69-107 fwd |
| FanDuel moved vs public | SLU@STAN | moneyline | home | FanDuel | 172 -> 136 | **+3.2** | 136 | 15% | 2.07 | 200-225 fit · 69-107 fwd |
| FanDuel moved vs public | SMU@LSU | moneyline | away | FanDuel | 240 -> 184 |  | 184 | 1% | 3.0 | 200-225 fit · 69-107 fwd |
| FanDuel moved vs public | USU@USC | moneyline | away | FanDuel | 130 -> 126 |  | 126 | 4% | 1.25 | 200-225 fit · 69-107 fwd |

## A  weighted ROI >= +20%

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 15:30 | ISU@TENN | moneyline | away **SPLIT** | +27.4 | 3-3 | -146 (-146) | -120 |  | 36% / 33% | 681 | follow_move->away (313-205 fit · 112-120 fwd*); rlm_quiet->away (52-110 fit · 39-76 fwd*); money_level->home (416-157 fit · 163-90 fwd*); sharp_gap->home (201-326 fit · 96-129 fwd*); money_moving->home (209-316 fit · 105-118 fwd*); consensus_gap->away (140-272 fit · 68-52 fwd*) |

## B  weighted ROI +10% to +20%

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 00:00 | SLU@STAN | spread | away **SPLIT** | +10.5 | 4-2 | -3.5 (-110) | -4.5 | -3.5 ($3,000) | 45% / 66% | 3205 | follow_move->home (247-261 fit · 88-95 fwd*); money_level->away (315-326 fit · 100-93 fwd*); sharp_gap->away (323-310 fit · 98-95 fwd*); money_moving->away (320-313 fit · 98-95 fwd*); consensus_gap->away (85-75 fit · 27-21 fwd*); pin_move->home (194-208 fit · 65-72 fwd*) |

## C  weighted ROI 0 to +10%

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 12:00 | ARMY@UTSA | moneyline | home **SPLIT** | +9.9 | 2-2 | -1400 (-1400) | -1250 |  | 96% / 84% | 65 | follow_move->home (313-205 fit · 112-120 fwd*); money_level->home (416-157 fit · 163-90 fwd*); sharp_gap->away (201-326 fit · 96-129 fwd*); money_moving->away (209-316 fit · 105-118 fwd*) |
| Thu 11:00 | UGA@CIN | spread | home | +0.3 | 1-0 | -1.5 (-120) | -1.5 | -2 ($1,000) | 0% / 0% | 151 | pin_value->home (159-148 fit · 71-61 fwd*) |
| Thu 16:30 | ARK@MSU | spread | away | +0.3 | 1-0 | 5.5 (-110) | 5.5 | 5 ($1,000) | 0% / 0% | 257 | pin_value->away (159-148 fit · 71-61 fwd*) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 00:00 | SLU@STAN | total | under **SPLIT** | -7.5 | 3-3 | 152.5 (-105) | 154.5 | 152 ($1,500) | 67% / 48% | 3205 | follow_move->under (296-297 fit · 113-133 fwd*); money_level->over (351-321 fit · 141-131 fwd*); sharp_gap->over (321-339 fit · 118-136 fwd*); money_moving->over (317-346 fit · 122-138 fwd*); pin_value->under (178-158 fit · 71-72 fwd*); pin_move->under (199-189 fit · 72-90 fwd*) |
| Thu 13:00 | SDSU@MD | total | under **SPLIT** | -8.8 | 2-2 | 152.5 (-110) | 153.5 |  | 50% / 48% | 227 | follow_move->under (296-297 fit · 113-133 fwd*); money_level->over (351-321 fit · 141-131 fwd*); sharp_gap->over (321-339 fit · 118-136 fwd*); money_moving->under (317-346 fit · 122-138 fwd*) |
| Thu 23:30 | ORE@TTU | moneyline | home **SPLIT** | -10.5 | 3-2 | -520 (-520) | -440 |  | 98% / 97% | 237 | follow_move->home (313-205 fit · 112-120 fwd*); money_level->home (416-157 fit · 163-90 fwd*); sharp_gap->away (201-326 fit · 96-129 fwd*); money_moving->home (209-316 fit · 105-118 fwd*); consensus_gap->away (140-272 fit · 68-52 fwd*) |
| Thu 00:30 | CSU@CLEM | moneyline | away **SPLIT** | -17.6 | 3-3 | 138 (+138) | 150 | 157 ($3,000) | 9% / 9% |  | money_delta->away (49-165 fit · 27-46 fwd*); follow_move->away (313-205 fit · 112-120 fwd*); rlm_quiet->away (52-110 fit · 39-76 fwd*); money_level->home (416-157 fit · 163-90 fwd*); pin_value->home (18-54 fit · 7-13 fwd); pin_move->home (103-103 fit · 58-50 fwd*) |
| Thu 00:00 | IW@HAW | moneyline | away **SPLIT** | -18.8 | 4-2 | 1160 (+1160) | 1000 | 1049 ($1,000) | 3% / 5% | 1045 | money_delta->away (49-165 fit · 27-46 fwd*); follow_move->home (313-205 fit · 112-120 fwd*); money_level->home (416-157 fit · 163-90 fwd*); sharp_gap->away (201-326 fit · 96-129 fwd*); money_moving->away (209-316 fit · 105-118 fwd*); pin_value->away (18-54 fit · 7-13 fwd) |
| Thu 21:00 | KSU@ALA | moneyline | away **SPLIT** | -19.6 | 4-2 | 890 (+890) | 525 |  | 2% / 15% | 272 | money_delta->away (49-165 fit · 27-46 fwd*); follow_move->home (313-205 fit · 112-120 fwd*); money_level->home (416-157 fit · 163-90 fwd*); sharp_gap->away (201-326 fit · 96-129 fwd*); money_moving->away (209-316 fit · 105-118 fwd*); consensus_gap->away (140-272 fit · 68-52 fwd*) |
| Thu 16:30 | USU@USC | moneyline | away **SPLIT** | -25.9 | 5-2 | 126 (+126) | 130 |  | 4% / 5% | 176 | follow_move->away (313-205 fit · 112-120 fwd*); rlm_ratio->away (37-80 fit · 24-52 fwd*); rlm_quiet->away (52-110 fit · 39-76 fwd*); money_level->home (416-157 fit · 163-90 fwd*); sharp_gap->away (201-326 fit · 96-129 fwd*); money_moving->away (209-316 fit · 105-118 fwd*); consensus_gap->home (140-272 fit · 68-52 fwd*) |
| Thu 19:00 | SMU@LSU | moneyline | away **SPLIT** | -25.9 | 5-2 | 184 (+184) | 240 |  | 1% / 3% | 156 | follow_move->away (313-205 fit · 112-120 fwd*); rlm_ratio->away (37-80 fit · 24-52 fwd*); rlm_quiet->away (52-110 fit · 39-76 fwd*); money_level->home (416-157 fit · 163-90 fwd*); sharp_gap->away (201-326 fit · 96-129 fwd*); money_moving->away (209-316 fit · 105-118 fwd*); consensus_gap->home (140-272 fit · 68-52 fwd*) |
| Thu 21:00 | SJU@LOU | moneyline | away **SPLIT** | -28.2 | 3-2 | -142 (-142) | -205 |  | 88% / 91% | 509 | follow_move->home (313-205 fit · 112-120 fwd*); rlm_quiet->home (52-110 fit · 39-76 fwd*); money_level->away (416-157 fit · 163-90 fwd*); sharp_gap->away (201-326 fit · 96-129 fwd*); money_moving->away (209-316 fit · 105-118 fwd*) |
| Thu 12:00 | OKLA@PUR | moneyline | home **SPLIT** | -29 | 4-2 | -210 (-210) | -225 | -194 ($1,000) | 93% / 98% | 191 | follow_move->away (313-205 fit · 112-120 fwd*); rlm_quiet->away (52-110 fit · 39-76 fwd*); money_level->home (416-157 fit · 163-90 fwd*); sharp_gap->home (201-326 fit · 96-129 fwd*); money_moving->home (209-316 fit · 105-118 fwd*); consensus_gap->home (140-272 fit · 68-52 fwd*) |
| Thu 00:00 | SLU@STAN | moneyline | home **SPLIT** | -34.8 | 6-3 | 136 (+136) | 172 | 152 ($3,000) **retraced +3.2** | 15% / 31% | 3205 | money_delta->home (49-165 fit · 27-46 fwd*); follow_move->home (313-205 fit · 112-120 fwd*); rlm_ratio->home (37-80 fit · 24-52 fwd*); rlm_quiet->home (52-110 fit · 39-76 fwd*); money_level->away (416-157 fit · 163-90 fwd*); sharp_gap->home (201-326 fit · 96-129 fwd*); money_moving->home (209-316 fit · 105-118 fwd*); consensus_gap->away (140-272 fit · 68-52 fwd*); pin_value->away (18-54 fit · 7-13 fwd) |
| Thu 13:00 | SDSU@MD | moneyline | home | -0.7 | 2-1 | -188 (-188) | -120 |  | 93% / 74% | 227 | follow_move->home (313-205 fit · 112-120 fwd*); money_level->home (416-157 fit · 163-90 fwd*); sharp_gap->away (201-326 fit · 96-129 fwd*) |
| Thu 13:00 | SDSU@MD | spread | home | -6.8 | 1-0 | -4.5 (-110) | -1.5 |  | 0% / 0% | 227 | follow_move->home (247-261 fit · 88-95 fwd*) |
| Thu 14:00 | SCAR@ASU | spread | home | -6.8 | 1-0 | -3.5 (-110) | -2.5 | -3.5 ($1,000) | 0% / 0% | 116 | follow_move->home (247-261 fit · 88-95 fwd*) |
| Thu 16:30 | USU@USC | spread | away | -6.8 | 1-0 | 2.5 (-102) | 3.5 |  | 0% / 0% | 171 | follow_move->away (247-261 fit · 88-95 fwd*) |
| Thu 19:00 | SMU@LSU | spread | away | -6.8 | 1-0 | 5.5 (-112) | 6.5 |  | 0% / 0% | 156 | follow_move->away (247-261 fit · 88-95 fwd*) |
| Thu 21:00 | SJU@LOU | spread | home | -6.8 | 1-0 | 2.5 (-110) | 4.5 |  | 0% / 0% | 509 | follow_move->home (247-261 fit · 88-95 fwd*) |
| Thu 21:00 | KSU@ALA | spread | home | -6.8 | 1-0 | -14.5 (-120) | -13.5 |  | 0% / 0% | 272 | follow_move->home (247-261 fit · 88-95 fwd*) |
| Thu 23:30 | ORE@TTU | spread | home | -6.8 | 1-0 | -9.5 (-120) | -8.5 |  | 0% / 0% | 237 | follow_move->home (247-261 fit · 88-95 fwd*) |
| Thu 13:30 | BC@UCF | moneyline | away | -7.1 | 1-1 | 116 (+116) | 130 |  | 0% / 0% | 106 | follow_move->away (313-205 fit · 112-120 fwd*); consensus_gap->home (140-272 fit · 68-52 fwd*) |
| Thu 18:00 | CREI@TCU | moneyline | away | -7.1 | 1-1 | -113 (-113) | 100 |  | 0% / 0% | 656 | follow_move->away (313-205 fit · 112-120 fwd*); consensus_gap->home (140-272 fit · 68-52 fwd*) |
| Thu 19:00 | DEP@PITT | spread | home | -7.1 | 1-1 | -1.5 (-100) | 1.5 | -1 ($1,000) | 0% / 0% | 166 | follow_move->home (247-261 fit · 88-95 fwd*); pin_value->away (159-148 fit · 71-61 fwd*) |
| Thu 20:00 | JVST@UCD | moneyline | home | -7.1 | 1-1 | 102 (+102) | 105 |  | 0% / 0% | 55 | follow_move->home (313-205 fit · 112-120 fwd*); consensus_gap->away (140-272 fit · 68-52 fwd*) |
| Thu 00:00 | IW@HAW | spread | home | -7.4 | 4-0 | -16.5 (-120) | -16.5 | -17 ($1,000) | 69% / 78% | 1045 | money_level->home (315-326 fit · 100-93 fwd*); sharp_gap->home (323-310 fit · 98-95 fwd*); money_moving->home (320-313 fit · 98-95 fwd*); pin_value->home (159-148 fit · 71-61 fwd*) |
| Thu 19:00 | DEP@PITT | moneyline | home | -7.9 | 1-0 | -111 (-111) | 100 | -114 ($1,000) | 0% / 0% | 166 | follow_move->home (313-205 fit · 112-120 fwd*) |
| Thu 14:00 | SCAR@ASU | moneyline | home | -8.7 | 2-0 | -160 (-160) | -150 | -165 ($1,000) | 0% / 0% | 116 | follow_move->home (313-205 fit · 112-120 fwd*); consensus_gap->home (140-272 fit · 68-52 fwd*) |
| Thu 18:00 | CREI@TCU | spread | away | -10.1 | 1-1 | -1.5 (-104) | 1.5 |  | 0% / 0% | 656 | follow_move->away (247-261 fit · 88-95 fwd*); consensus_gap->home (85-75 fit · 27-21 fwd*) |
| Thu 12:00 | OKLA@PUR | total | over | -10.8 | 1-0 | 142.5 (-115) | 141.5 | 142.5 ($500) | 0% / 0% | 176 | follow_move->over (296-297 fit · 113-133 fwd*) |
| Thu 12:00 | ARMY@UTSA | total | under | -10.8 | 1-0 | 150.5 (-110) | 151.5 |  | 0% / 0% | 65 | follow_move->under (296-297 fit · 113-133 fwd*) |
| Thu 13:30 | BC@UCF | total | over | -10.8 | 1-0 | 146.5 (-110) | 144.5 |  | 0% / 0% | 106 | follow_move->over (296-297 fit · 113-133 fwd*) |
| Thu 14:00 | SCAR@ASU | total | under | -10.8 | 1-0 | 140.5 (-105) | 141.5 | 140.5 ($500) | 0% / 0% | 116 | follow_move->under (296-297 fit · 113-133 fwd*) |
| Thu 17:00 | SMC@UCLA | total | under | -10.8 | 1-0 | 153.5 (-110) | 155.5 |  | 0% / 0% | 222 | follow_move->under (296-297 fit · 113-133 fwd*) |
| Thu 18:00 | CREI@TCU | total | under | -10.8 | 1-0 | 155.5 (-110) | 156.5 |  | 0% / 0% | 656 | follow_move->under (296-297 fit · 113-133 fwd*) |
| Thu 21:00 | SJU@LOU | total | over | -10.8 | 1-0 | 160.5 (-110) | 157.5 |  | 0% / 0% | 509 | follow_move->over (296-297 fit · 113-133 fwd*) |
| Thu 21:00 | KSU@ALA | total | under | -10.8 | 1-0 | 169.5 (-105) | 172.5 |  | 0% / 0% | 272 | follow_move->under (296-297 fit · 113-133 fwd*) |
| Thu 22:30 | NEOM@PAC | total | under | -10.8 | 1-0 | 140.5 (-105) | 143.5 |  | 0% / 0% | 111 | follow_move->under (296-297 fit · 113-133 fwd*) |
| Thu 23:30 | ORE@TTU | total | under | -10.8 | 1-0 | 149.5 (-110) | 153.5 |  | 0% / 0% | 237 | follow_move->under (296-297 fit · 113-133 fwd*) |
| Thu 23:30 | GONZ@BAY | total | under | -10.8 | 1-0 | 157.5 (-110) | 160.5 |  | 0% / 0% | 666 | follow_move->under (296-297 fit · 113-133 fwd*) |
| Thu 15:30 | MICH@MIA | total | over | -11.3 | 5-1 | 159.5 (-110) | 163.5 |  | 41% / 63% | 550 | money_delta->over (145-132 fit · 53-52 fwd*); follow_move->under (296-297 fit · 113-133 fwd*); money_level->over (351-321 fit · 141-131 fwd*); sharp_gap->over (321-339 fit · 118-136 fwd*); money_moving->over (317-346 fit · 122-138 fwd*); consensus_gap->over (105-101 fit · 35-30 fwd*) |
| Thu 20:00 | JVST@UCD | total | over | -12.1 | 1-1 | 140.5 (-110) | 138.5 |  | 0% / 0% | 55 | follow_move->over (296-297 fit · 113-133 fwd*); consensus_gap->under (105-101 fit · 35-30 fwd*) |
| Thu 11:00 | UGA@CIN | total | over | -13.7 | 5-1 | 154.5 (-110) | 155.5 | 155 ($500) | 55% / 84% | 161 | follow_move->under (296-297 fit · 113-133 fwd*); money_level->over (351-321 fit · 141-131 fwd*); sharp_gap->over (321-339 fit · 118-136 fwd*); money_moving->over (317-346 fit · 122-138 fwd*); consensus_gap->over (105-101 fit · 35-30 fwd*); pin_value->over (178-158 fit · 71-72 fwd*) |
| Thu 16:30 | ARK@MSU | total | under | -15.6 | 2-0 | 150.5 (-110) | 151.5 | 150 ($500) | 0% / 0% | 257 | follow_move->under (296-297 fit · 113-133 fwd*); pin_value->under (178-158 fit · 71-72 fwd*) |
| Thu 15:30 | ISU@TENN | spread | away | -16.7 | 5-0 | -2.5 (-114) | -1.5 |  | 25% / 69% | 681 | follow_move->away (247-261 fit · 88-95 fwd*); rlm_ratio->away (41-43 fit · 11-9 fwd); money_level->away (315-326 fit · 100-93 fwd*); sharp_gap->away (323-310 fit · 98-95 fwd*); money_moving->away (320-313 fit · 98-95 fwd*) |
| Thu 17:00 | SMC@UCLA | moneyline | home | -16.8 | 2-0 | -310 (-310) | -305 |  | 99% / 99% | 247 | follow_move->home (313-205 fit · 112-120 fwd*); money_level->home (416-157 fit · 163-90 fwd*) |
| Thu 15:30 | ISU@TENN | total | under | -20.8 | 3-1 | 139.5 (-110) | 139.5 |  | 15% / 36% | 757 | money_delta->under (145-132 fit · 53-52 fwd*); money_level->over (351-321 fit · 141-131 fwd*); sharp_gap->under (321-339 fit · 118-136 fwd*); money_moving->under (317-346 fit · 122-138 fwd*) |
| Thu 00:30 | CSU@CLEM | spread | home | -22.3 | 6-0 | -3.5 (-115) | -2.5 | -4 ($3,000) | 61% / 70% |  | follow_move->home (247-261 fit · 88-95 fwd*); money_level->home (315-326 fit · 100-93 fwd*); sharp_gap->home (323-310 fit · 98-95 fwd*); money_moving->home (320-313 fit · 98-95 fwd*); pin_value->home (159-148 fit · 71-61 fwd*); pin_move->home (194-208 fit · 65-72 fwd*) |
| Thu 19:00 | DEP@PITT | total | over | -23.7 | 2-0 | 139.5 (-110) | 138.5 | 139.5 ($500) **retraced +1** | 0% / 0% | 217 | follow_move->over (296-297 fit · 113-133 fwd*); pin_move->over (199-189 fit · 72-90 fwd*) |
| Thu 23:30 | GONZ@BAY | moneyline | home | -26.7 | 5-1 | 146 (+146) | 185 |  | 12% / 39% | 666 | follow_move->home (313-205 fit · 112-120 fwd*); rlm_ratio->home (37-80 fit · 24-52 fwd*); rlm_quiet->home (52-110 fit · 39-76 fwd*); money_level->away (416-157 fit · 163-90 fwd*); sharp_gap->home (201-326 fit · 96-129 fwd*); money_moving->home (209-316 fit · 105-118 fwd*) |
| Thu 11:00 | UGA@CIN | moneyline | away | -27.7 | 3-1 | 110 (+110) | 110 | 116 ($1,000) | 30% / 89% | 161 | follow_move->home (313-205 fit · 112-120 fwd*); money_level->away (416-157 fit · 163-90 fwd*); sharp_gap->away (201-326 fit · 96-129 fwd*); money_moving->away (209-316 fit · 105-118 fwd*) |
| Thu 16:30 | USU@USC | total | over | -31.8 | 4-0 | 165.5 (-110) | 162.5 |  | 53% / 84% | 206 | follow_move->over (296-297 fit · 113-133 fwd*); money_level->over (351-321 fit · 141-131 fwd*); sharp_gap->over (321-339 fit · 118-136 fwd*); money_moving->over (317-346 fit · 122-138 fwd*) |
| Thu 15:30 | MICH@MIA | moneyline | away | -35.6 | 6-1 | 112 (+112) | 136 |  | 13% / 18% | 550 | money_delta->away (49-165 fit · 27-46 fwd*); follow_move->away (313-205 fit · 112-120 fwd*); rlm_ratio->away (37-80 fit · 24-52 fwd*); rlm_quiet->away (52-110 fit · 39-76 fwd*); money_level->home (416-157 fit · 163-90 fwd*); sharp_gap->away (201-326 fit · 96-129 fwd*); money_moving->away (209-316 fit · 105-118 fwd*) |
| Thu 14:30 | GTWN@TEX | total | under | -36.6 | 5-0 | 154.5 (-110) | 155.5 | 154 ($500) | 49% / 74% | 313 | follow_move->under (296-297 fit · 113-133 fwd*); money_level->under (351-321 fit · 141-131 fwd*); sharp_gap->under (321-339 fit · 118-136 fwd*); money_moving->under (317-346 fit · 122-138 fwd*); pin_value->under (178-158 fit · 71-72 fwd*) |
| Thu 00:30 | CSU@CLEM | total | under | -39.9 | 5-1 | 147.5 (-105) | 153.5 | 148 ($1,500) | 65% / 74% |  | follow_move->under (296-297 fit · 113-133 fwd*); money_level->under (351-321 fit · 141-131 fwd*); sharp_gap->under (321-339 fit · 118-136 fwd*); money_moving->under (317-346 fit · 122-138 fwd*); pin_value->over (178-158 fit · 71-72 fwd*); pin_move->under (199-189 fit · 72-90 fwd*) |
| Thu 00:00 | IW@HAW | total | under | -40.2 | 6-1 | 139.5 (-110) | 142.5 | 139.5 ($500) | 12% / 16% | 1045 | money_delta->under (145-132 fit · 53-52 fwd*); follow_move->under (296-297 fit · 113-133 fwd*); rlm_ratio->under (122-102 fit · 34-46 fwd*); rlm_quiet->under (85-102 fit · 47-65 fwd*); money_level->over (351-321 fit · 141-131 fwd*); sharp_gap->under (321-339 fit · 118-136 fwd*); money_moving->under (317-346 fit · 122-138 fwd*) |
| Thu 16:30 | ARK@MSU | moneyline | home | -43.5 | 4-0 | -225 (-225) | -218 | -221 ($1,000) | 94% / 96% | 257 | follow_move->home (313-205 fit · 112-120 fwd*); money_level->home (416-157 fit · 163-90 fwd*); sharp_gap->home (201-326 fit · 96-129 fwd*); money_moving->home (209-316 fit · 105-118 fwd*) |
| Thu 14:30 | GTWN@TEX | moneyline | home | -44.3 | 5-0 | -385 (-385) | -375 | -407 ($1,000) | 99% / 100% | 272 | follow_move->home (313-205 fit · 112-120 fwd*); money_level->home (416-157 fit · 163-90 fwd*); sharp_gap->home (201-326 fit · 96-129 fwd*); money_moving->home (209-316 fit · 105-118 fwd*); consensus_gap->home (140-272 fit · 68-52 fwd*) |

