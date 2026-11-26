# CBB board

Generated 2026-11-26 13:14 UTC. Upcoming games with a FanDuel line. Every game is listed;
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
| PINNACLE moved vs public | GTWN@TEX | moneyline | away | Pinnacle | 322 -> 329 | — | 310 | 4% | 1.75 | 140-161 fit · 42-63 fwd |
| PINNACLE moved vs public | OKLA@PUR | moneyline | away | Pinnacle | 167 -> 164 | — | 158 | 14% | 2.0 | 140-161 fit · 42-63 fwd |
| PINNACLE moved vs public | SCAR@ASU | total | under | Pinnacle | 140.5 -> 139.5 | — | 139.5 | 13% | 2.15 | 140-161 fit · 42-63 fwd |
| PINNACLE moved vs public | SDSU@MD | moneyline | away | Pinnacle | 158 -> 155 | **+1.4** | 160 | 12% | 1.83 | 140-161 fit · 42-63 fwd |
| FanDuel moved vs public | ARMY@UTSA | moneyline | away | FanDuel | 760 -> 720 |  | 720 | 5% | 3.8 | 200-225 fit · 71-117 fwd |
| FanDuel moved vs public | CREI@TCU | total | under | FanDuel | 156.5 -> 153.5 |  | 153.5 | 38% | 1.39 | 200-225 fit · 71-117 fwd |
| FanDuel moved vs public | GONZ@BAY | moneyline | home | FanDuel | 185 -> 146 |  | 146 | 13% | 4.54 | 200-225 fit · 71-117 fwd |
| FanDuel moved vs public | ISU@TENN | spread | away | FanDuel | -1.5 -> -2.5 | — | -2.5 | 23% | 2.0 | 200-225 fit · 71-117 fwd |
| FanDuel moved vs public | JVST@UCD | moneyline | home | FanDuel | 105 -> 102 | — | 102 | 29% | 2.69 | 200-225 fit · 71-117 fwd |
| FanDuel moved vs public | MICH@MIA | moneyline | away | FanDuel | 136 -> 114 |  | 114 | 14% | 1.64 | 200-225 fit · 71-117 fwd |
| FanDuel moved vs public | OKLA@PUR | moneyline | away | FanDuel | 185 -> 158 | — | 158 | 14% | 2.0 | 200-225 fit · 71-117 fwd |
| FanDuel moved vs public | SCAR@ASU | total | under | FanDuel | 141.5 -> 139.5 | — | 139.5 | 13% | 2.15 | 200-225 fit · 71-117 fwd |
| FanDuel moved vs public | UGA@CIN | total | under | FanDuel | 155.5 -> 154.5 | — | 154.5 | 30% | 1.47 | 200-225 fit · 71-117 fwd |
| FanDuel moved vs public | USU@USC | spread | away | FanDuel | 3.5 -> 2.5 |  | 2.5 | 30% | 1.47 | 200-225 fit · 71-117 fwd |

## A  weighted ROI >= +20%

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 19:00 | SMU@LSU | moneyline | away **SPLIT** | +31 | 3-3 | 205 (+205) | 240 |  | 6% / 3% | 701 | follow_move->away (313-205 fit · 116-127 fwd*); rlm_quiet->away (52-110 fit · 41-80 fwd*); money_level->home (416-157 fit · 170-94 fwd*); sharp_gap->home (201-326 fit · 98-138 fwd*); money_moving->home (209-316 fit · 107-127 fwd*); consensus_gap->away (140-272 fit · 72-56 fwd*) |

## B  weighted ROI +10% to +20%

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 19:00 | DEP@PITT | spread | away | +12.3 | 2-1 | 1.5 (-122) | -1.5 | 1 ($1,000) | 0% / 0% | 701 | follow_move->home (247-261 fit · 93-100 fwd*); consensus_gap->away (85-75 fit · 29-21 fwd*); pin_value->away (159-148 fit · 74-64 fwd*) |

## C  weighted ROI 0 to +10%

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 17:00 | SMC@UCLA | total | under **SPLIT** | +7 | 3-3 | 153.5 (-110) | 155.5 |  | 32% / 29% | 908 | follow_move->under (296-297 fit · 120-138 fwd*); rlm_quiet->under (85-102 fit · 48-69 fwd*); money_level->over (351-321 fit · 149-135 fwd*); sharp_gap->over (321-339 fit · 122-144 fwd*); money_moving->over (317-346 fit · 126-146 fwd*); consensus_gap->under (105-101 fit · 37-31 fwd*) |
| Thu 11:00 | UGA@CIN | spread | home **SPLIT** | +5.4 | 4-3 | -1.5 (-120) | -1.5 | -2.5 ($1,000) | 35% / 34% | 1630 | money_delta->home (122-125 fit · 19-19 fwd*); money_level->away (315-326 fit · 105-99 fwd*); sharp_gap->away (323-310 fit · 104-101 fwd*); money_moving->away (320-313 fit · 104-101 fwd*); consensus_gap->home (85-75 fit · 29-21 fwd*); pin_value->home (159-148 fit · 74-64 fwd*); pin_move->home (194-208 fit · 69-73 fwd*) |
| Thu 21:00 | SJU@LOU | spread | home **SPLIT** | +4.3 | 3-3 | 2.5 (-114) | 4.5 |  | 40% / 30% | 1519 | follow_move->home (247-261 fit · 93-100 fwd*); rlm_quiet->home (45-44 fit · 22-28 fwd*); money_level->away (315-326 fit · 105-99 fwd*); sharp_gap->away (323-310 fit · 104-101 fwd*); money_moving->away (320-313 fit · 104-101 fwd*); consensus_gap->home (85-75 fit · 29-21 fwd*) |
| Thu 19:00 | SMU@LSU | spread | home **SPLIT** | +1.2 | 3-2 | -5.5 (-118) | -6.5 |  | 74% / 84% | 701 | follow_move->away (247-261 fit · 93-100 fwd*); rlm_quiet->away (45-44 fit · 22-28 fwd*); money_level->home (315-326 fit · 105-99 fwd*); sharp_gap->home (323-310 fit · 104-101 fwd*); money_moving->home (320-313 fit · 104-101 fwd*) |
| Thu 14:30 | GTWN@TEX | total | under **SPLIT** | +0.1 | 3-3 | 154.5 (-110) | 155.5 | 154 ($500) | 25% / 24% | 1181 | follow_move->under (296-297 fit · 120-138 fwd*); rlm_quiet->under (85-102 fit · 48-69 fwd*); money_level->over (351-321 fit · 149-135 fwd*); sharp_gap->over (321-339 fit · 122-144 fwd*); money_moving->over (317-346 fit · 126-146 fwd*); pin_value->under (178-158 fit · 74-75 fwd*) |
| Thu 16:30 | ARK@MSU | total | under **SPLIT** | +0.1 | 3-3 | 150.5 (-110) | 151.5 | 150 ($500) | 23% / 17% | 1171 | follow_move->under (296-297 fit · 120-138 fwd*); rlm_quiet->under (85-102 fit · 48-69 fwd*); money_level->over (351-321 fit · 149-135 fwd*); sharp_gap->over (321-339 fit · 122-144 fwd*); money_moving->over (317-346 fit · 126-146 fwd*); pin_value->under (178-158 fit · 74-75 fwd*) |
| Thu 15:30 | ISU@TENN | total | over | +0.6 | 2-1 | 139.5 (-110) | 139.5 | 139.5 ($500) | 84% / 72% | 2251 | money_level->over (351-321 fit · 149-135 fwd*); sharp_gap->under (321-339 fit · 122-144 fwd*); money_moving->over (317-346 fit · 126-146 fwd*) |
| Thu 20:00 | JVST@UCD | spread | away | +0.1 | 1-0 | -1.5 (-110) | -1.5 | -2 ($1,000) | 0% / 0% | 277 | pin_value->away (159-148 fit · 74-64 fwd*) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 23:30 | ORE@TTU | total | under **SPLIT** | -0.4 | 3-3 | 149.5 (-110) | 153.5 |  | 29% / 18% | 661 | money_delta->under (145-132 fit · 54-57 fwd*); follow_move->under (296-297 fit · 120-138 fwd*); rlm_quiet->under (85-102 fit · 48-69 fwd*); money_level->over (351-321 fit · 149-135 fwd*); sharp_gap->over (321-339 fit · 122-144 fwd*); money_moving->over (317-346 fit · 126-146 fwd*) |
| Thu 13:00 | SDSU@MD | moneyline | home **SPLIT** | -1.3 | 4-2 | -192 (-192) | -120 | -182 ($1,000) **retraced +1.4** | 88% / 78% | 1040 | follow_move->home (313-205 fit · 116-127 fwd*); money_level->home (416-157 fit · 170-94 fwd*); sharp_gap->away (201-326 fit · 98-138 fwd*); money_moving->home (209-316 fit · 107-127 fwd*); consensus_gap->home (140-272 fit · 72-56 fwd*); pin_rlm->away (38-74 fit · 16-33 fwd*) |
| Thu 15:30 | MICH@MIA | total | over **SPLIT** | -2.8 | 4-2 | 158.5 (-110) | 163.5 |  | 56% / 60% | 1474 | follow_move->under (296-297 fit · 120-138 fwd*); rlm_quiet->under (85-102 fit · 48-69 fwd*); money_level->over (351-321 fit · 149-135 fwd*); sharp_gap->over (321-339 fit · 122-144 fwd*); money_moving->over (317-346 fit · 126-146 fwd*); consensus_gap->over (105-101 fit · 37-31 fwd*) |
| Thu 19:00 | DEP@PITT | total | under **SPLIT** | -3.9 | 4-3 | 139.5 (-110) | 138.5 | 139.5 ($500) **retraced +1** | 16% / 21% | 701 | money_delta->under (145-132 fit · 54-57 fwd*); follow_move->over (296-297 fit · 120-138 fwd*); money_level->over (351-321 fit · 149-135 fwd*); sharp_gap->under (321-339 fit · 122-144 fwd*); money_moving->under (317-346 fit · 126-146 fwd*); consensus_gap->under (105-101 fit · 37-31 fwd*); pin_move->over (199-189 fit · 76-91 fwd*) |
| Thu 12:00 | ARMY@UTSA | total | over **SPLIT** | -4.9 | 3-2 | 149.5 (-110) | 151.5 |  | 80% / 81% | 348 | follow_move->under (296-297 fit · 120-138 fwd*); rlm_quiet->under (85-102 fit · 48-69 fwd*); money_level->over (351-321 fit · 149-135 fwd*); sharp_gap->over (321-339 fit · 122-144 fwd*); money_moving->over (317-346 fit · 126-146 fwd*) |
| Thu 22:30 | NEOM@PAC | total | over **SPLIT** | -4.9 | 3-2 | 139.5 (-110) | 143.5 |  | 87% / 90% | 307 | follow_move->under (296-297 fit · 120-138 fwd*); rlm_quiet->under (85-102 fit · 48-69 fwd*); money_level->over (351-321 fit · 149-135 fwd*); sharp_gap->over (321-339 fit · 122-144 fwd*); money_moving->over (317-346 fit · 126-146 fwd*) |
| Thu 16:30 | ARK@MSU | spread | home **SPLIT** | -6.2 | 3-2 | -5.5 (-110) | -5.5 | -5 ($1,000) | 71% / 77% | 1171 | money_delta->away (122-125 fit · 19-19 fwd*); money_level->home (315-326 fit · 105-99 fwd*); sharp_gap->home (323-310 fit · 104-101 fwd*); money_moving->home (320-313 fit · 104-101 fwd*); pin_value->away (159-148 fit · 74-64 fwd*) |
| Thu 13:00 | SDSU@MD | spread | home **SPLIT** | -6.6 | 4-3 | -4.5 (-110) | -1.5 | -4 ($1,000) | 54% / 67% | 1040 | money_delta->away (122-125 fit · 19-19 fwd*); follow_move->home (247-261 fit · 93-100 fwd*); money_level->home (315-326 fit · 105-99 fwd*); sharp_gap->home (323-310 fit · 104-101 fwd*); money_moving->home (320-313 fit · 104-101 fwd*); pin_value->away (159-148 fit · 74-64 fwd*); pin_move->away (194-208 fit · 69-73 fwd*) |
| Thu 19:00 | DEP@PITT | moneyline | away **SPLIT** | -6.6 | 4-2 | -108 (-108) | -120 | -112 ($1,000) | 30% / 35% | 701 | follow_move->home (313-205 fit · 116-127 fwd*); money_level->home (416-157 fit · 170-94 fwd*); sharp_gap->away (201-326 fit · 98-138 fwd*); money_moving->away (209-316 fit · 107-127 fwd*); consensus_gap->away (140-272 fit · 72-56 fwd*); pin_move->away (103-103 fit · 60-53 fwd*) |
| Thu 20:00 | JVST@UCD | total | over **SPLIT** | -21.7 | 4-2 | 140.5 (-110) | 138.5 | 140 ($500) | 88% / 89% | 277 | money_delta->under (145-132 fit · 54-57 fwd*); follow_move->over (296-297 fit · 120-138 fwd*); money_level->over (351-321 fit · 149-135 fwd*); sharp_gap->over (321-339 fit · 122-144 fwd*); money_moving->over (317-346 fit · 126-146 fwd*); pin_value->under (178-158 fit · 74-75 fwd*) |
| Thu 15:30 | ISU@TENN | moneyline | home **SPLIT** | -30 | 3-2 | 120 (+120) | 100 | 128 ($1,000) | 44% / 65% | 2251 | follow_move->away (313-205 fit · 116-127 fwd*); money_level->home (416-157 fit · 170-94 fwd*); sharp_gap->home (201-326 fit · 98-138 fwd*); money_moving->home (209-316 fit · 107-127 fwd*); consensus_gap->away (140-272 fit · 72-56 fwd*) |
| Thu 21:00 | KSU@ALA | moneyline | away **SPLIT** | -31.2 | 4-2 | 860 (+860) | 525 |  | 2% / 11% | 681 | money_delta->away (49-165 fit · 27-53 fwd*); follow_move->home (313-205 fit · 116-127 fwd*); money_level->home (416-157 fit · 170-94 fwd*); sharp_gap->away (201-326 fit · 98-138 fwd*); money_moving->away (209-316 fit · 107-127 fwd*); consensus_gap->away (140-272 fit · 72-56 fwd*) |
| Thu 13:30 | BC@UCF | moneyline | home **SPLIT** | -33.1 | 3-2 | -128 (-128) | -155 |  | 82% / 93% | 671 | follow_move->away (313-205 fit · 116-127 fwd*); rlm_quiet->away (52-110 fit · 41-80 fwd*); money_level->home (416-157 fit · 170-94 fwd*); sharp_gap->home (201-326 fit · 98-138 fwd*); money_moving->home (209-316 fit · 107-127 fwd*) |
| Thu 16:30 | USU@USC | moneyline | home **SPLIT** | -35.2 | 4-2 | -150 (-150) | -155 |  | 90% / 93% | 1070 | follow_move->away (313-205 fit · 116-127 fwd*); rlm_quiet->away (52-110 fit · 41-80 fwd*); money_level->home (416-157 fit · 170-94 fwd*); sharp_gap->home (201-326 fit · 98-138 fwd*); money_moving->home (209-316 fit · 107-127 fwd*); consensus_gap->home (140-272 fit · 72-56 fwd*) |
| Thu 21:00 | SJU@LOU | moneyline | away **SPLIT** | -35.2 | 4-2 | -134 (-134) | -205 |  | 76% / 88% | 1519 | follow_move->home (313-205 fit · 116-127 fwd*); rlm_quiet->home (52-110 fit · 41-80 fwd*); money_level->away (416-157 fit · 170-94 fwd*); sharp_gap->away (201-326 fit · 98-138 fwd*); money_moving->away (209-316 fit · 107-127 fwd*); consensus_gap->away (140-272 fit · 72-56 fwd*) |
| Thu 14:30 | GTWN@TEX | moneyline | away **SPLIT** | -40.7 | 4-3 | 310 (+310) | 295 | 329 ($1,000) | 4% / 7% | 1181 | money_delta->away (49-165 fit · 27-53 fwd*); follow_move->home (313-205 fit · 116-127 fwd*); money_level->home (416-157 fit · 170-94 fwd*); sharp_gap->away (201-326 fit · 98-138 fwd*); money_moving->away (209-316 fit · 107-127 fwd*); consensus_gap->home (140-272 fit · 72-56 fwd*); pin_rlm->away (38-74 fit · 16-33 fwd*) |
| Thu 11:00 | UGA@CIN | total | under **SPLIT** | -44.1 | 6-2 | 154.5 (-106) | 155.5 | 155 ($500) | 30% / 44% | 1630 | money_delta->under (145-132 fit · 54-57 fwd*); follow_move->under (296-297 fit · 120-138 fwd*); rlm_ratio->under (122-102 fit · 35-50 fwd*); rlm_quiet->under (85-102 fit · 48-69 fwd*); money_level->over (351-321 fit · 149-135 fwd*); sharp_gap->under (321-339 fit · 122-144 fwd*); money_moving->under (317-346 fit · 126-146 fwd*); pin_value->over (178-158 fit · 74-75 fwd*) |
| Thu 15:30 | MICH@MIA | moneyline | away **SPLIT** | -47.6 | 6-2 | 114 (+114) | 136 |  | 14% / 23% | 1474 | money_delta->away (49-165 fit · 27-53 fwd*); follow_move->away (313-205 fit · 116-127 fwd*); rlm_ratio->away (37-80 fit · 24-58 fwd*); rlm_quiet->away (52-110 fit · 41-80 fwd*); money_level->home (416-157 fit · 170-94 fwd*); sharp_gap->away (201-326 fit · 98-138 fwd*); money_moving->away (209-316 fit · 107-127 fwd*); consensus_gap->home (140-272 fit · 72-56 fwd*) |
| Thu 12:00 | OKLA@PUR | moneyline | away **SPLIT** | -61.3 | 7-2 | 158 (+158) | 185 | 164 ($1,000) | 14% / 28% | 1004 | money_delta->away (49-165 fit · 27-53 fwd*); follow_move->away (313-205 fit · 116-127 fwd*); rlm_ratio->away (37-80 fit · 24-58 fwd*); rlm_quiet->away (52-110 fit · 41-80 fwd*); money_level->home (416-157 fit · 170-94 fwd*); sharp_gap->away (201-326 fit · 98-138 fwd*); money_moving->away (209-316 fit · 107-127 fwd*); consensus_gap->home (140-272 fit · 72-56 fwd*); pin_rlm->away (38-74 fit · 16-33 fwd*) |
| Thu 21:00 | KSU@ALA | spread | home | -1.2 | 2-0 | -14.5 (-110) | -13.5 |  | 0% / 0% | 681 | follow_move->home (247-261 fit · 93-100 fwd*); consensus_gap->home (85-75 fit · 29-21 fwd*) |
| Thu 13:30 | BC@UCF | spread | home | -1.8 | 3-1 | -1.5 (-120) | -2.5 |  | 50% / 77% | 671 | follow_move->away (247-261 fit · 93-100 fwd*); money_level->home (315-326 fit · 105-99 fwd*); sharp_gap->home (323-310 fit · 104-101 fwd*); money_moving->home (320-313 fit · 104-101 fwd*) |
| Thu 14:00 | SCAR@ASU | spread | away | -1.8 | 3-1 | 3.5 (-110) | 2.5 | 3.5 ($1,000) | 38% / 53% | 711 | follow_move->home (247-261 fit · 93-100 fwd*); money_level->away (315-326 fit · 105-99 fwd*); sharp_gap->away (323-310 fit · 104-101 fwd*); money_moving->away (320-313 fit · 104-101 fwd*) |
| Thu 12:00 | OKLA@PUR | spread | home | -2.1 | 1-0 | -4.5 (-110) | -4.5 | -4.5 ($1,000) | 63% / 63% | 1004 | money_level->home (315-326 fit · 105-99 fwd*) |
| Thu 14:00 | SCAR@ASU | moneyline | home | -5.1 | 3-1 | -160 (-160) | -150 | -168 ($1,000) | 90% / 90% | 711 | money_delta->away (49-165 fit · 27-53 fwd*); follow_move->home (313-205 fit · 116-127 fwd*); money_level->home (416-157 fit · 170-94 fwd*); consensus_gap->home (140-272 fit · 72-56 fwd*) |
| Thu 15:30 | MICH@MIA | spread | home | -6.1 | 3-1 | -2.5 (-106) | -2.5 |  | 65% / 77% | 1474 | money_delta->away (122-125 fit · 19-19 fwd*); money_level->home (315-326 fit · 105-99 fwd*); sharp_gap->home (323-310 fit · 104-101 fwd*); money_moving->home (320-313 fit · 104-101 fwd*) |
| Thu 14:30 | GTWN@TEX | spread | away | -6.7 | 3-1 | 8.5 (-110) | 8.5 | 8.5 ($1,000) | 30% / 36% | 1181 | money_delta->away (122-125 fit · 19-19 fwd*); money_level->home (315-326 fit · 105-99 fwd*); sharp_gap->away (323-310 fit · 104-101 fwd*); money_moving->away (320-313 fit · 104-101 fwd*) |
| Thu 18:00 | CREI@TCU | spread | away | -6.7 | 1-0 | -1.5 (-104) | 1.5 |  | 0% / 0% | 1353 | follow_move->away (247-261 fit · 93-100 fwd*) |
| Thu 12:00 | ARMY@UTSA | spread | home | -8.5 | 3-0 | -13.5 (-106) | -13.5 |  | 58% / 85% | 348 | money_level->home (315-326 fit · 105-99 fwd*); sharp_gap->home (323-310 fit · 104-101 fwd*); money_moving->home (320-313 fit · 104-101 fwd*) |
| Thu 17:00 | SMC@UCLA | spread | home | -8.5 | 3-0 | -7.5 (-110) | -7.5 |  | 79% / 87% | 908 | money_level->home (315-326 fit · 105-99 fwd*); sharp_gap->home (323-310 fit · 104-101 fwd*); money_moving->home (320-313 fit · 104-101 fwd*) |
| Thu 15:30 | ISU@TENN | spread | away | -13 | 5-1 | -2.5 (-114) | -1.5 | -3 ($1,000) | 23% / 46% | 2251 | follow_move->away (247-261 fit · 93-100 fwd*); rlm_ratio->away (41-43 fit · 12-9 fwd); money_level->home (315-326 fit · 105-99 fwd*); sharp_gap->away (323-310 fit · 104-101 fwd*); money_moving->away (320-313 fit · 104-101 fwd*); pin_value->away (159-148 fit · 74-64 fwd*) |
| Thu 23:30 | GONZ@BAY | spread | away | -14 | 3-1 | -4.5 (-102) | -4.5 |  | 60% / 65% | 1544 | money_level->away (315-326 fit · 105-99 fwd*); sharp_gap->away (323-310 fit · 104-101 fwd*); money_moving->away (320-313 fit · 104-101 fwd*); consensus_gap->home (85-75 fit · 29-21 fwd*) |
| Thu 21:00 | SJU@LOU | total | under | -15.2 | 4-1 | 161.5 (-110) | 157.5 |  | 49% / 50% | 1519 | money_delta->under (145-132 fit · 54-57 fwd*); follow_move->over (296-297 fit · 120-138 fwd*); sharp_gap->under (321-339 fit · 122-144 fwd*); money_moving->under (317-346 fit · 126-146 fwd*); consensus_gap->under (105-101 fit · 37-31 fwd*) |
| Thu 23:30 | ORE@TTU | spread | home | -15.2 | 4-0 | -9.5 (-120) | -8.5 |  | 60% / 77% | 661 | follow_move->home (247-261 fit · 93-100 fwd*); money_level->home (315-326 fit · 105-99 fwd*); sharp_gap->home (323-310 fit · 104-101 fwd*); money_moving->home (320-313 fit · 104-101 fwd*) |
| Thu 16:30 | USU@USC | spread | away | -18.5 | 6-1 | 2.5 (-102) | 3.5 |  | 30% / 44% | 1070 | money_delta->away (122-125 fit · 19-19 fwd*); follow_move->away (247-261 fit · 93-100 fwd*); rlm_ratio->away (41-43 fit · 12-9 fwd); rlm_quiet->away (45-44 fit · 22-28 fwd*); money_level->home (315-326 fit · 105-99 fwd*); sharp_gap->away (323-310 fit · 104-101 fwd*); money_moving->away (320-313 fit · 104-101 fwd*) |
| Thu 19:00 | SMU@LSU | total | under | -22 | 3-0 | 160.5 (-110) | 160.5 |  | 48% / 63% | 701 | money_level->under (351-321 fit · 149-135 fwd*); sharp_gap->under (321-339 fit · 122-144 fwd*); money_moving->under (317-346 fit · 126-146 fwd*) |
| Thu 23:30 | GONZ@BAY | total | under | -24.4 | 5-1 | 156.5 (-110) | 160.5 |  | 52% / 61% | 1544 | money_delta->over (145-132 fit · 54-57 fwd*); follow_move->under (296-297 fit · 120-138 fwd*); money_level->under (351-321 fit · 149-135 fwd*); sharp_gap->under (321-339 fit · 122-144 fwd*); money_moving->under (317-346 fit · 126-146 fwd*); consensus_gap->under (105-101 fit · 37-31 fwd*) |
| Thu 12:00 | OKLA@PUR | total | over | -24.7 | 5-0 | 141.5 (-114) | 141.5 | 142.5 ($500) | 80% / 88% | 1004 | money_level->over (351-321 fit · 149-135 fwd*); sharp_gap->over (321-339 fit · 122-144 fwd*); money_moving->over (317-346 fit · 126-146 fwd*); consensus_gap->over (105-101 fit · 37-31 fwd*); pin_value->over (178-158 fit · 74-75 fwd*) |
| Thu 21:00 | KSU@ALA | total | under | -26.5 | 4-1 | 169.5 (-105) | 172.5 |  | 51% / 59% | 681 | money_delta->over (145-132 fit · 54-57 fwd*); follow_move->under (296-297 fit · 120-138 fwd*); money_level->under (351-321 fit · 149-135 fwd*); sharp_gap->under (321-339 fit · 122-144 fwd*); money_moving->under (317-346 fit · 126-146 fwd*) |
| Thu 13:30 | BC@UCF | total | over | -31.8 | 4-0 | 146.5 (-110) | 144.5 |  | 75% / 90% | 671 | follow_move->over (296-297 fit · 120-138 fwd*); money_level->over (351-321 fit · 149-135 fwd*); sharp_gap->over (321-339 fit · 122-144 fwd*); money_moving->over (317-346 fit · 126-146 fwd*) |
| Thu 16:30 | USU@USC | total | over | -31.8 | 4-0 | 164.5 (-110) | 162.5 |  | 48% / 59% | 1070 | follow_move->over (296-297 fit · 120-138 fwd*); money_level->over (351-321 fit · 149-135 fwd*); sharp_gap->over (321-339 fit · 122-144 fwd*); money_moving->over (317-346 fit · 126-146 fwd*) |
| Thu 18:00 | CREI@TCU | moneyline | home | -34.2 | 4-1 | -106 (-106) | -120 |  | 51% / 62% | 1353 | follow_move->away (313-205 fit · 116-127 fwd*); money_level->home (416-157 fit · 170-94 fwd*); sharp_gap->home (201-326 fit · 98-138 fwd*); money_moving->home (209-316 fit · 107-127 fwd*); consensus_gap->home (140-272 fit · 72-56 fwd*) |
| Thu 12:00 | ARMY@UTSA | moneyline | away | -34.7 | 5-1 | 720 (+720) | 760 |  | 5% / 19% | 348 | follow_move->away (313-205 fit · 116-127 fwd*); rlm_ratio->away (37-80 fit · 24-58 fwd*); rlm_quiet->away (52-110 fit · 41-80 fwd*); money_level->home (416-157 fit · 170-94 fwd*); sharp_gap->away (201-326 fit · 98-138 fwd*); money_moving->away (209-316 fit · 107-127 fwd*) |
| Thu 16:30 | ARK@MSU | moneyline | home | -35.1 | 4-1 | -225 (-225) | -218 | -223 ($1,000) | 92% / 94% | 1171 | money_delta->away (49-165 fit · 27-53 fwd*); follow_move->home (313-205 fit · 116-127 fwd*); money_level->home (416-157 fit · 170-94 fwd*); sharp_gap->home (201-326 fit · 98-138 fwd*); money_moving->home (209-316 fit · 107-127 fwd*) |
| Thu 11:00 | UGA@CIN | moneyline | away | -39 | 3-1 | 108 (+108) | 110 | 115 ($1,000) | 25% / 90% | 1630 | money_level->away (416-157 fit · 170-94 fwd*); sharp_gap->away (201-326 fit · 98-138 fwd*); money_moving->away (209-316 fit · 107-127 fwd*); consensus_gap->home (140-272 fit · 72-56 fwd*) |
| Thu 18:00 | CREI@TCU | total | under | -42 | 6-0 | 153.5 (-105) | 156.5 |  | 38% / 53% | 1353 | money_delta->under (145-132 fit · 54-57 fwd*); follow_move->under (296-297 fit · 120-138 fwd*); rlm_ratio->under (122-102 fit · 35-50 fwd*); money_level->under (351-321 fit · 149-135 fwd*); sharp_gap->under (321-339 fit · 122-144 fwd*); money_moving->under (317-346 fit · 126-146 fwd*) |
| Thu 23:30 | ORE@TTU | moneyline | home | -48 | 4-1 | -520 (-520) | -440 |  | 98% / 99% | 661 | follow_move->home (313-205 fit · 116-127 fwd*); money_level->home (416-157 fit · 170-94 fwd*); sharp_gap->home (201-326 fit · 98-138 fwd*); money_moving->home (209-316 fit · 107-127 fwd*); consensus_gap->away (140-272 fit · 72-56 fwd*) |
| Thu 13:00 | SDSU@MD | total | under | -48.6 | 6-1 | 152.5 (-110) | 153.5 | 151.5 ($500) | 39% / 39% | 1040 | money_delta->under (145-132 fit · 54-57 fwd*); follow_move->under (296-297 fit · 120-138 fwd*); rlm_quiet->under (85-102 fit · 48-69 fwd*); money_level->over (351-321 fit · 149-135 fwd*); money_moving->under (317-346 fit · 126-146 fwd*); pin_value->under (178-158 fit · 74-75 fwd*); pin_move->under (199-189 fit · 76-91 fwd*) |
| Thu 17:00 | SMC@UCLA | moneyline | home | -52.2 | 5-0 | -320 (-320) | -305 |  | 98% / 99% | 908 | follow_move->home (313-205 fit · 116-127 fwd*); money_level->home (416-157 fit · 170-94 fwd*); sharp_gap->home (201-326 fit · 98-138 fwd*); money_moving->home (209-316 fit · 107-127 fwd*); consensus_gap->home (140-272 fit · 72-56 fwd*) |
| Thu 20:00 | JVST@UCD | moneyline | home | -66.6 | 6-1 | 102 (+102) | 105 | 109 ($1,000) | 29% / 78% | 277 | money_delta->home (49-165 fit · 27-53 fwd*); follow_move->home (313-205 fit · 116-127 fwd*); rlm_ratio->home (37-80 fit · 24-58 fwd*); money_level->home (416-157 fit · 170-94 fwd*); sharp_gap->home (201-326 fit · 98-138 fwd*); money_moving->home (209-316 fit · 107-127 fwd*); consensus_gap->away (140-272 fit · 72-56 fwd*) |
| Thu 14:00 | SCAR@ASU | total | under | -70.6 | 8-1 | 139.5 (-105) | 141.5 | 139.5 ($500) | 13% / 28% | 711 | money_delta->under (145-132 fit · 54-57 fwd*); follow_move->under (296-297 fit · 120-138 fwd*); rlm_ratio->under (122-102 fit · 35-50 fwd*); rlm_quiet->under (85-102 fit · 48-69 fwd*); money_level->over (351-321 fit · 149-135 fwd*); sharp_gap->under (321-339 fit · 122-144 fwd*); money_moving->under (317-346 fit · 126-146 fwd*); pin_move->under (199-189 fit · 76-91 fwd*); pin_rlm->under (77-64 fit · 21-27 fwd*) |
| Thu 23:30 | GONZ@BAY | moneyline | home | -70.8 | 7-0 | 146 (+146) | 185 |  | 13% / 59% | 1544 | money_delta->home (49-165 fit · 27-53 fwd*); follow_move->home (313-205 fit · 116-127 fwd*); rlm_ratio->home (37-80 fit · 24-58 fwd*); money_level->home (416-157 fit · 170-94 fwd*); sharp_gap->home (201-326 fit · 98-138 fwd*); money_moving->home (209-316 fit · 107-127 fwd*); consensus_gap->home (140-272 fit · 72-56 fwd*) |

