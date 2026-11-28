# CBB board

Generated 2026-11-28 03:34 UTC. Upcoming games with a FanDuel line. Every game is listed;
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
| PINNACLE moved vs public | TTU@SDSU | total | under | Pinnacle | 143 -> 142 | — | 141.5 | 7% | 4.86 | 140-161 fit · 61-84 fwd |
| FanDuel moved vs public | NIU@EIU | moneyline | home | FanDuel | 520 -> 480 |  | 480 | 6% | 16.33 | 200-225 fit · 100-148 fwd |
| FanDuel moved vs public | TTU@SDSU | total | under | FanDuel | 142.5 -> 141.5 | — | 141.5 | 7% | 4.86 | 200-225 fit · 100-148 fwd |

## C  weighted ROI 0 to +10%

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Fri 23:30 | TTU@SDSU | spread | home **SPLIT** | +9.6 | 3-3 | 8.5 (-110) | 6.5 | 8.5 ($3,000) | 39% / 40% | 4503 | money_delta->home (122-125 fit · 30-30 fwd*); follow_move->away (247-261 fit · 111-121 fwd*); money_level->away (315-326 fit · 138-123 fwd*); sharp_gap->home (323-310 fit · 132-128 fwd*); money_moving->home (320-313 fit · 132-128 fwd*); pin_move->away (194-208 fit · 81-97 fwd*) |
| Sat 12:00 | SIE@HALL | spread | away | +8.7 | 1-0 | 17.5 (-110) | 17.5 |  | 0% / 0% | 116 | consensus_gap->away (85-75 fit · 35-23 fwd*) |
| Sat 13:00 | HAMP@RAD | spread | away | +8.7 | 1-0 | 1.5 (-120) | 1.5 |  | 0% / 0% | 80 | consensus_gap->away (85-75 fit · 35-23 fwd*) |
| Sat 16:00 | DEL@STON | total | under | +5 | 1-0 | 137.5 (-105) | 137.5 |  | 0% / 0% | 90 | consensus_gap->under (105-101 fit · 45-35 fwd*) |
| Sat 16:00 | PEAY@FUR | total | over | +5 | 1-0 | 150.5 (-110) | 150.5 |  | 0% / 0% | 55 | consensus_gap->over (105-101 fit · 45-35 fwd*) |
| Sat 19:00 | UTU@SCU | total | under | +5 | 1-0 | 166.5 (-110) | 166.5 |  | 0% / 0% | 50 | consensus_gap->under (105-101 fit · 45-35 fwd*) |
| Fri 23:00 | GONZ@CREI | spread | away | +2.5 | 5-0 | -5.5 (-118) | -5.5 | -6 ($5,000) | 53% / 60% | 5634 | money_level->away (315-326 fit · 138-123 fwd*); sharp_gap->away (323-310 fit · 132-128 fwd*); money_moving->away (320-313 fit · 132-128 fwd*); consensus_gap->away (85-75 fit · 35-23 fwd*); pin_value->away (159-148 fit · 85-74 fwd*) |
| Sat 16:00 | SJSU@UVU | spread | away | +1.1 | 2-0 | 6.5 (-110) | 7.5 |  | 0% / 0% | 136 | follow_move->away (247-261 fit · 111-121 fwd*); consensus_gap->away (85-75 fit · 35-23 fwd*) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Fri 23:00 | GONZ@CREI | moneyline | away **SPLIT** | -19.1 | 4-3 | -245 (-245) | -250 | -256 ($3,000) | 93% / 94% | 5634 | money_delta->home (49-165 fit · 35-69 fwd*); follow_move->home (313-205 fit · 139-154 fwd*); rlm_quiet->home (52-110 fit · 51-97 fwd*); money_level->away (416-157 fit · 202-114 fwd*); sharp_gap->away (201-326 fit · 117-169 fwd*); money_moving->away (209-316 fit · 126-158 fwd*); pin_move->away (103-103 fit · 68-73 fwd*) |
| Sat 12:00 | SIE@HALL | moneyline | away **SPLIT** | -19.6 | 3-2 | 1160 (+1160) | 1100 |  | 1% / 2% | 116 | follow_move->home (313-205 fit · 139-154 fwd*); money_level->home (416-157 fit · 202-114 fwd*); sharp_gap->away (201-326 fit · 117-169 fwd*); money_moving->away (209-316 fit · 126-158 fwd*); consensus_gap->away (140-272 fit · 88-73 fwd*) |
| Fri 23:30 | TTU@SDSU | total | under **SPLIT** | -29.7 | 8-3 | 141.5 (-110) | 142.5 | 142 ($1,500) | 7% / 34% | 4503 | money_delta->under (145-132 fit · 68-62 fwd*); follow_move->under (296-297 fit · 153-159 fwd*); rlm_ratio->under (122-102 fit · 54-62 fwd*); rlm_quiet->under (85-102 fit · 71-82 fwd*); money_level->over (351-321 fit · 172-168 fwd*); sharp_gap->under (321-339 fit · 153-166 fwd*); money_moving->under (317-346 fit · 158-167 fwd*); consensus_gap->over (105-101 fit · 45-35 fwd*); pin_value->over (178-158 fit · 89-89 fwd*); pin_move->under (199-189 fit · 95-103 fwd*); pin_rlm->under (77-64 fit · 34-32 fwd*) |
| Sat 14:00 | FOR@HARV | total | under | -0.6 | 2-0 | 139.5 (-110) | 141.5 |  | 0% / 0% | 100 | follow_move->under (296-297 fit · 153-159 fwd*); consensus_gap->under (105-101 fit · 45-35 fwd*) |
| Sat 20:00 | CAL@MINN | total | over | -0.6 | 2-0 | 141.5 (-115) | 140.5 |  | 0% / 0% | 106 | follow_move->over (296-297 fit · 153-159 fwd*); consensus_gap->over (105-101 fit · 45-35 fwd*) |
| Sat 13:00 | WOF@PFW | moneyline | home | -1.8 | 1-1 | -138 (-138) | -132 |  | 0% / 0% | 106 | follow_move->home (313-205 fit · 139-154 fwd*); consensus_gap->away (140-272 fit · 88-73 fwd*) |
| Sat 14:00 | TROY@CHAT | moneyline | away | -1.8 | 1-1 | 116 (+116) | 142 |  | 0% / 0% | 90 | follow_move->away (313-205 fit · 139-154 fwd*); consensus_gap->home (140-272 fit · 88-73 fwd*) |
| Sat 15:30 | BUFF@TOWS | moneyline | home | -1.8 | 1-1 | -150 (-150) | -140 |  | 0% / 0% | 70 | follow_move->home (313-205 fit · 139-154 fwd*); consensus_gap->away (140-272 fit · 88-73 fwd*) |
| Sat 16:00 | DEL@STON | moneyline | home | -1.8 | 1-1 | -205 (-205) | -176 |  | 0% / 0% | 90 | follow_move->home (313-205 fit · 139-154 fwd*); consensus_gap->away (140-272 fit · 88-73 fwd*) |
| Sat 17:00 | NAU@CSB | moneyline | home | -1.8 | 1-1 | -250 (-250) | -245 |  | 0% / 0% | 80 | follow_move->home (313-205 fit · 139-154 fwd*); consensus_gap->away (140-272 fit · 88-73 fwd*) |
| Sat 17:00 | WEB@CSF | moneyline | home | -1.8 | 1-1 | -670 (-670) | -650 |  | 0% / 0% | 65 | follow_move->home (313-205 fit · 139-154 fwd*); consensus_gap->away (140-272 fit · 88-73 fwd*) |
| Sat 18:00 | VMI@RICH | moneyline | home | -1.8 | 1-1 | -1700 (-1700) | -1600 |  | 0% / 0% | 55 | follow_move->home (313-205 fit · 139-154 fwd*); consensus_gap->away (140-272 fit · 88-73 fwd*) |
| Sat 19:00 | PRST@SIU | moneyline | away | -1.8 | 1-1 | 240 (+240) | 240 |  | 0% / 0% | 50 | follow_move->away (313-205 fit · 139-154 fwd*); consensus_gap->home (140-272 fit · 88-73 fwd*) |
| Sat 19:00 | UTU@SCU | moneyline | home | -1.8 | 1-1 | -2800 (-2800) | -2642 |  | 0% / 0% | 50 | follow_move->home (313-205 fit · 139-154 fwd*); consensus_gap->away (140-272 fit · 88-73 fwd*) |
| Sat 19:00 | JOES@MONM | moneyline | home | -1.8 | 1-1 | 114 (+114) | 115 |  | 0% / 0% | 90 | follow_move->home (313-205 fit · 139-154 fwd*); consensus_gap->away (140-272 fit · 88-73 fwd*) |
| Sat 12:00 | PRIN@UST | total | under | -5.6 | 1-0 | 144.5 (-110) | 145.5 |  | 0% / 0% | 70 | follow_move->under (296-297 fit · 153-159 fwd*) |
| Sat 13:00 | WOF@PFW | total | under | -5.6 | 1-0 | 155.5 (-110) | 158.5 |  | 0% / 0% | 106 | follow_move->under (296-297 fit · 153-159 fwd*) |
| Sat 13:00 | RMU@UNI | total | under | -5.6 | 1-0 | 148.5 (-110) | 149.5 |  | 0% / 0% | 60 | follow_move->under (296-297 fit · 153-159 fwd*) |
| Sat 13:00 | NCCU@WEBB | total | under | -5.6 | 1-0 | 138.5 (-105) | 140.5 |  | 0% / 0% | 75 | follow_move->under (296-297 fit · 153-159 fwd*) |
| Sat 13:00 | HAMP@RAD | total | under | -5.6 | 1-0 | 135.5 (-110) | 138 |  | 0% / 0% | 80 | follow_move->under (296-297 fit · 153-159 fwd*) |
| Sat 13:00 | COLG@UVM | total | under | -5.6 | 1-0 | 142.5 (-110) | 146.5 |  | 0% / 0% | 95 | follow_move->under (296-297 fit · 153-159 fwd*) |
| Sat 14:00 | TROY@CHAT | total | under | -5.6 | 1-0 | 145.5 (-105) | 147.5 |  | 0% / 0% | 90 | follow_move->under (296-297 fit · 153-159 fwd*) |
| Sat 15:00 | WIU@CCAR | total | over | -5.6 | 1-0 | 140.5 (-115) | 137.5 |  | 0% / 0% | 65 | follow_move->over (296-297 fit · 153-159 fwd*) |
| Sat 15:00 | SEMO@UMKC | total | under | -5.6 | 1-0 | 147.5 (-110) | 148.5 |  | 0% / 0% | 100 | follow_move->under (296-297 fit · 153-159 fwd*) |
| Sat 15:00 | LIB@UNCW | total | under | -5.6 | 1-0 | 150.5 (-105) | 151.5 |  | 0% / 0% | 121 | follow_move->under (296-297 fit · 153-159 fwd*) |
| Sat 15:00 | DEN@NMSU | total | under | -5.6 | 1-0 | 141.5 (-105) | 144.5 |  | 0% / 0% | 106 | follow_move->under (296-297 fit · 153-159 fwd*) |
| Sat 15:30 | MRMK@HOF | total | under | -5.6 | 1-0 | 124.5 (-105) | 125.5 |  | 0% / 0% | 151 | follow_move->under (296-297 fit · 153-159 fwd*) |
| Sat 18:00 | USA@SDST | total | under | -5.6 | 1-0 | 140.5 (-105) | 141.5 |  | 0% / 0% | 65 | follow_move->under (296-297 fit · 153-159 fwd*) |
| Sat 18:00 | VMI@RICH | total | under | -5.6 | 1-0 | 150.5 (-110) | 151.5 |  | 0% / 0% | 55 | follow_move->under (296-297 fit · 153-159 fwd*) |
| Sat 19:00 | PRST@SIU | total | over | -5.6 | 1-0 | 155.5 (-115) | 154.5 |  | 0% / 0% | 50 | follow_move->over (296-297 fit · 153-159 fwd*) |
| Sat 22:00 | LMU@UCSD | total | under | -5.6 | 1-0 | 155.5 (-110) | 156.5 |  | 0% / 0% | 65 | follow_move->under (296-297 fit · 153-159 fwd*) |
| Sat 14:00 | BALL@USI | moneyline | away | -6.5 | 1-0 | -137 (-137) | -137 |  | 0% / 0% | 65 | consensus_gap->away (140-272 fit · 88-73 fwd*) |
| Sat 14:00 | MRST@GMU | moneyline | away | -6.5 | 1-0 | 1400 (+1400) | 1280 |  | 0% / 0% | 60 | consensus_gap->away (140-272 fit · 88-73 fwd*) |
| Sat 15:30 | UNT@BSU | moneyline | away | -6.5 | 1-0 | 168 (+168) | 168 |  | 0% / 0% | 116 | consensus_gap->away (140-272 fit · 88-73 fwd*) |
| Sat 15:30 | MRMK@HOF | moneyline | home | -6.5 | 1-0 | -137 (-137) | -137 |  | 0% / 0% | 151 | consensus_gap->home (140-272 fit · 88-73 fwd*) |
| Sat 16:00 | DREX@MSM | moneyline | away | -6.5 | 1-0 | -215 (-215) | -215 |  | 0% / 0% | 75 | consensus_gap->away (140-272 fit · 88-73 fwd*) |
| Sat 16:00 | UNCO@USD | moneyline | away | -6.5 | 1-0 | 860 (+860) | 810 |  | 0% / 0% | 95 | consensus_gap->away (140-272 fit · 88-73 fwd*) |
| Sat 16:00 | SJSU@UVU | moneyline | away | -6.5 | 1-0 | 225 (+225) | 220 |  | 0% / 0% | 136 | consensus_gap->away (140-272 fit · 88-73 fwd*) |
| Sat 16:00 | TNTC@EKY | moneyline | home | -6.5 | 1-0 | 146 (+146) | 146 |  | 0% / 0% | 126 | consensus_gap->home (140-272 fit · 88-73 fwd*) |
| Sat 18:00 | USA@SDST | moneyline | away | -6.5 | 1-0 | -106 (-106) | -106 |  | 0% / 0% | 65 | consensus_gap->away (140-272 fit · 88-73 fwd*) |
| Sat 18:00 | NDSU@DRKE | moneyline | home | -6.5 | 1-0 | -245 (-245) | -245 |  | 0% / 0% | 106 | consensus_gap->home (140-272 fit · 88-73 fwd*) |
| Sat 20:00 | CAL@MINN | moneyline | home | -6.5 | 1-0 | -335 (-335) | -335 |  | 0% / 0% | 106 | consensus_gap->home (140-272 fit · 88-73 fwd*) |
| Sat 12:00 | ELON@NCST | spread | away | -7.6 | 1-0 | 20.5 (-110) | 22.5 |  | 0% / 0% | 85 | follow_move->away (247-261 fit · 111-121 fwd*) |
| Sat 13:00 | WOF@PFW | spread | home | -7.6 | 1-0 | -2.5 (-110) | -2 |  | 0% / 0% | 106 | follow_move->home (247-261 fit · 111-121 fwd*) |
| Sat 13:00 | RMU@UNI | spread | away | -7.6 | 1-0 | 6.5 (-110) | 7 |  | 0% / 0% | 60 | follow_move->away (247-261 fit · 111-121 fwd*) |
| Sat 13:00 | NCCU@WEBB | spread | home | -7.6 | 1-0 | -2.5 (-110) | -1.5 |  | 0% / 0% | 75 | follow_move->home (247-261 fit · 111-121 fwd*) |
| Sat 14:00 | MRST@GMU | spread | home | -7.6 | 1-0 | -19.5 (-110) | -19 |  | 0% / 0% | 60 | follow_move->home (247-261 fit · 111-121 fwd*) |
| Sat 15:00 | WIU@CCAR | spread | away | -7.6 | 1-0 | 11.5 (-110) | 12.5 |  | 0% / 0% | 65 | follow_move->away (247-261 fit · 111-121 fwd*) |
| Sat 15:00 | TOL@VALP | spread | away | -7.6 | 1-0 | 3.5 (-110) | 4.5 |  | 0% / 0% | 75 | follow_move->away (247-261 fit · 111-121 fwd*) |
| Sat 15:00 | SEMO@UMKC | spread | home | -7.6 | 1-0 | -3.5 (-110) | -2.5 |  | 0% / 0% | 100 | follow_move->home (247-261 fit · 111-121 fwd*) |
| Sat 15:00 | LIB@UNCW | spread | away | -7.6 | 1-0 | 5.5 (-102) | 6.5 |  | 0% / 0% | 121 | follow_move->away (247-261 fit · 111-121 fwd*) |
| Sat 15:00 | DEN@NMSU | spread | away | -7.6 | 1-0 | 3.5 (-110) | 5.5 |  | 0% / 0% | 106 | follow_move->away (247-261 fit · 111-121 fwd*) |
| Sat 15:30 | BUFF@TOWS | spread | away | -7.6 | 1-0 | 2.5 (-102) | 4.5 |  | 0% / 0% | 70 | follow_move->away (247-261 fit · 111-121 fwd*) |
| Sat 15:30 | UNT@BSU | spread | home | -7.6 | 1-0 | -4.5 (-120) | -3.5 |  | 0% / 0% | 116 | follow_move->home (247-261 fit · 111-121 fwd*) |
| Sat 15:30 | MRMK@HOF | spread | away | -7.6 | 1-0 | 2.5 (-110) | 5.5 |  | 0% / 0% | 151 | follow_move->away (247-261 fit · 111-121 fwd*) |
| Sat 16:00 | DREX@MSM | spread | away | -7.6 | 1-0 | -5.5 (-110) | -4.5 |  | 0% / 0% | 75 | follow_move->away (247-261 fit · 111-121 fwd*) |
| Sat 16:00 | UNCO@USD | spread | home | -7.6 | 1-0 | -14.5 (-110) | -13.5 |  | 0% / 0% | 95 | follow_move->home (247-261 fit · 111-121 fwd*) |
| Sat 16:00 | PEAY@FUR | spread | away | -7.6 | 1-0 | 7.5 (-110) | 8.5 |  | 0% / 0% | 55 | follow_move->away (247-261 fit · 111-121 fwd*) |
| Sat 17:00 | WEB@CSF | spread | away | -7.6 | 1-0 | 10.5 (-102) | 12.5 |  | 0% / 0% | 65 | follow_move->away (247-261 fit · 111-121 fwd*) |
| Sat 18:00 | VMI@RICH | spread | away | -7.6 | 1-0 | 15.5 (-110) | 16.5 |  | 0% / 0% | 55 | follow_move->away (247-261 fit · 111-121 fwd*) |
| Sat 19:00 | UTU@SCU | spread | away | -7.6 | 1-0 | 17.5 (-110) | 19.5 |  | 0% / 0% | 50 | follow_move->away (247-261 fit · 111-121 fwd*) |
| Sat 19:00 | JOES@MONM | spread | away | -7.6 | 1-0 | -2.5 (-110) | -1.5 |  | 0% / 0% | 90 | follow_move->away (247-261 fit · 111-121 fwd*) |
| Sat 22:00 | LMU@UCSD | spread | away | -7.6 | 1-0 | 1.5 (-110) | 2.5 |  | 0% / 0% | 65 | follow_move->away (247-261 fit · 111-121 fwd*) |
| Sat 13:00 | HAMP@RAD | moneyline | away | -8.3 | 1-0 | -108 (-108) | 105 |  | 0% / 0% | 80 | follow_move->away (313-205 fit · 139-154 fwd*) |
| Sat 13:00 | COLG@UVM | moneyline | home | -8.3 | 1-0 | -100 (-100) | 102 |  | 0% / 0% | 95 | follow_move->home (313-205 fit · 139-154 fwd*) |
| Sat 15:00 | BRWN@AFA | moneyline | away | -8.3 | 1-0 | 102 (+102) | 110 |  | 0% / 0% | 85 | follow_move->away (313-205 fit · 139-154 fwd*) |
| Sat 15:00 | WIU@CCAR | moneyline | home | -8.3 | 1-0 | -720 (-720) | -670 |  | 0% / 0% | 65 | follow_move->home (313-205 fit · 139-154 fwd*) |
| Sat 15:00 | TOL@VALP | moneyline | home | -8.3 | 1-0 | -162 (-162) | -150 |  | 0% / 0% | 75 | follow_move->home (313-205 fit · 139-154 fwd*) |
| Sat 15:00 | SEMO@UMKC | moneyline | home | -8.3 | 1-0 | -162 (-162) | -160 |  | 0% / 0% | 100 | follow_move->home (313-205 fit · 139-154 fwd*) |
| Sat 17:00 | UCI@SEA | moneyline | home | -8.3 | 1-0 | -210 (-210) | -205 |  | 0% / 0% | 85 | follow_move->home (313-205 fit · 139-154 fwd*) |
| Sat 22:00 | LMU@UCSD | moneyline | home | -8.3 | 1-0 | -122 (-122) | -121 |  | 0% / 0% | 65 | follow_move->home (313-205 fit · 139-154 fwd*) |
| Sat 12:00 | ELON@NCST | total | under | -10.6 | 1-1 | 149.5 (-105) | 152.5 |  | 0% / 0% | 85 | follow_move->under (296-297 fit · 153-159 fwd*); consensus_gap->over (105-101 fit · 45-35 fwd*) |
| Sat 14:00 | BALL@USI | total | under | -10.6 | 1-1 | 138.5 (-105) | 139.5 |  | 0% / 0% | 65 | follow_move->under (296-297 fit · 153-159 fwd*); consensus_gap->over (105-101 fit · 45-35 fwd*) |
| Sat 14:00 | MRST@GMU | total | over | -10.6 | 1-1 | 131.5 (-115) | 131 |  | 0% / 0% | 60 | follow_move->over (296-297 fit · 153-159 fwd*); consensus_gap->under (105-101 fit · 45-35 fwd*) |
| Sat 15:00 | BRWN@AFA | total | under | -10.6 | 1-1 | 157.5 (-105) | 158.5 |  | 0% / 0% | 85 | follow_move->under (296-297 fit · 153-159 fwd*); consensus_gap->over (105-101 fit · 45-35 fwd*) |
| Sat 15:00 | TOL@VALP | total | under | -10.6 | 1-1 | 152.5 (-105) | 153.5 |  | 0% / 0% | 75 | follow_move->under (296-297 fit · 153-159 fwd*); consensus_gap->over (105-101 fit · 45-35 fwd*) |
| Sat 15:00 | NIU@EIU | total | under | -10.6 | 1-1 | 141.5 (-105) | 143.5 |  | 0% / 0% | 80 | follow_move->under (296-297 fit · 153-159 fwd*); consensus_gap->over (105-101 fit · 45-35 fwd*) |
| Sat 15:30 | BUFF@TOWS | total | under | -10.6 | 1-1 | 137.5 (-105) | 139.5 |  | 0% / 0% | 70 | follow_move->under (296-297 fit · 153-159 fwd*); consensus_gap->over (105-101 fit · 45-35 fwd*) |
| Sat 15:30 | UNT@BSU | total | under | -10.6 | 1-1 | 154.5 (-105) | 155.5 |  | 0% / 0% | 116 | follow_move->under (296-297 fit · 153-159 fwd*); consensus_gap->over (105-101 fit · 45-35 fwd*) |
| Sat 16:00 | DREX@MSM | total | over | -10.6 | 1-1 | 138.5 (-115) | 137.5 |  | 0% / 0% | 75 | follow_move->over (296-297 fit · 153-159 fwd*); consensus_gap->under (105-101 fit · 45-35 fwd*) |
| Sat 16:00 | UNCO@USD | total | over | -10.6 | 1-1 | 149.5 (-115) | 146.5 |  | 0% / 0% | 95 | follow_move->over (296-297 fit · 153-159 fwd*); consensus_gap->under (105-101 fit · 45-35 fwd*) |
| Sat 16:00 | SJSU@UVU | total | under | -10.6 | 1-1 | 154.5 (-110) | 155.5 |  | 0% / 0% | 136 | follow_move->under (296-297 fit · 153-159 fwd*); consensus_gap->over (105-101 fit · 45-35 fwd*) |
| Sat 16:00 | TNTC@EKY | total | over | -10.6 | 1-1 | 170.5 (-110) | 169.5 |  | 0% / 0% | 126 | follow_move->over (296-297 fit · 153-159 fwd*); consensus_gap->under (105-101 fit · 45-35 fwd*) |
| Sat 17:00 | NAU@CSB | total | under | -10.6 | 1-1 | 149.5 (-105) | 151 |  | 0% / 0% | 80 | follow_move->under (296-297 fit · 153-159 fwd*); consensus_gap->over (105-101 fit · 45-35 fwd*) |
| Sat 17:00 | WEB@CSF | total | under | -10.6 | 1-1 | 168.5 (-105) | 169.5 |  | 0% / 0% | 65 | follow_move->under (296-297 fit · 153-159 fwd*); consensus_gap->over (105-101 fit · 45-35 fwd*) |
| Sat 19:00 | JOES@MONM | total | over | -10.6 | 1-1 | 147.5 (-110) | 146.5 |  | 0% / 0% | 90 | follow_move->over (296-297 fit · 153-159 fwd*); consensus_gap->under (105-101 fit · 45-35 fwd*) |
| Fri 23:00 | GONZ@CREI | total | over | -12.4 | 3-1 | 160.5 (-110) | 161.5 | 160.5 ($1,500) | 42% / 58% | 5634 | follow_move->under (296-297 fit · 153-159 fwd*); money_level->over (351-321 fit · 172-168 fwd*); sharp_gap->over (321-339 fit · 153-166 fwd*); money_moving->over (317-346 fit · 158-167 fwd*) |
| Sat 12:00 | ELON@NCST | moneyline | home | -14.8 | 2-0 | -4500 (-4500) | -4000 |  | 0% / 0% | 85 | follow_move->home (313-205 fit · 139-154 fwd*); consensus_gap->home (140-272 fit · 88-73 fwd*) |
| Sat 13:00 | RMU@UNI | moneyline | home | -14.8 | 2-0 | -265 (-265) | -265 |  | 98% / 98% | 60 | money_level->home (416-157 fit · 202-114 fwd*); consensus_gap->home (140-272 fit · 88-73 fwd*) |
| Sat 13:00 | NCCU@WEBB | moneyline | home | -14.8 | 2-0 | -138 (-138) | -125 |  | 0% / 0% | 75 | follow_move->home (313-205 fit · 139-154 fwd*); consensus_gap->home (140-272 fit · 88-73 fwd*) |
| Sat 12:00 | PRIN@UST | spread | away | -16.3 | 1-1 | 1.5 (-102) | 2.5 |  | 0% / 0% | 70 | follow_move->away (247-261 fit · 111-121 fwd*); consensus_gap->home (85-75 fit · 35-23 fwd*) |
| Sat 14:00 | BALL@USI | spread | home | -16.3 | 1-1 | 2.5 (-110) | 3 |  | 0% / 0% | 65 | follow_move->home (247-261 fit · 111-121 fwd*); consensus_gap->away (85-75 fit · 35-23 fwd*) |
| Sat 14:00 | TROY@CHAT | spread | away | -16.3 | 1-1 | 2.5 (-110) | 3.5 |  | 0% / 0% | 90 | follow_move->away (247-261 fit · 111-121 fwd*); consensus_gap->home (85-75 fit · 35-23 fwd*) |
| Sat 14:00 | FOR@HARV | spread | away | -16.3 | 1-1 | -3.5 (-110) | -2.5 |  | 0% / 0% | 100 | follow_move->away (247-261 fit · 111-121 fwd*); consensus_gap->home (85-75 fit · 35-23 fwd*) |
| Sat 15:00 | BRWN@AFA | spread | away | -16.3 | 1-1 | 1.5 (-110) | 2.5 |  | 0% / 0% | 85 | follow_move->away (247-261 fit · 111-121 fwd*); consensus_gap->home (85-75 fit · 35-23 fwd*) |
| Sat 15:00 | NIU@EIU | spread | away | -16.3 | 1-1 | -11.5 (-102) | -10.5 |  | 0% / 0% | 80 | follow_move->away (247-261 fit · 111-121 fwd*); consensus_gap->home (85-75 fit · 35-23 fwd*) |
| Sat 16:00 | DEL@STON | spread | away | -16.3 | 1-1 | 4.5 (-102) | 5.5 |  | 0% / 0% | 90 | follow_move->away (247-261 fit · 111-121 fwd*); consensus_gap->home (85-75 fit · 35-23 fwd*) |
| Sat 16:00 | TNTC@EKY | spread | away | -16.3 | 1-1 | -4.5 (-102) | -3.5 |  | 0% / 0% | 126 | follow_move->away (247-261 fit · 111-121 fwd*); consensus_gap->home (85-75 fit · 35-23 fwd*) |
| Sat 19:00 | PRST@SIU | spread | away | -16.3 | 1-1 | 6.5 (-102) | 7.5 |  | 0% / 0% | 50 | follow_move->away (247-261 fit · 111-121 fwd*); consensus_gap->home (85-75 fit · 35-23 fwd*) |
| Sat 20:00 | CAL@MINN | spread | away | -16.3 | 1-1 | 7.5 (-102) | 9.5 |  | 0% / 0% | 106 | follow_move->away (247-261 fit · 111-121 fwd*); consensus_gap->home (85-75 fit · 35-23 fwd*) |
| Fri 23:30 | TTU@SDSU | moneyline | away | -23.7 | 4-0 | -375 (-375) | -265 | -378 ($3,000) | 97% / 97% | 4503 | follow_move->away (313-205 fit · 139-154 fwd*); money_level->away (416-157 fit · 202-114 fwd*); consensus_gap->away (140-272 fit · 88-73 fwd*); pin_move->away (103-103 fit · 68-73 fwd*) |
| Sat 12:00 | PRIN@UST | moneyline | home | -52.8 | 5-0 | -132 (-132) | -128 |  | 91% / 100% | 70 | follow_move->home (313-205 fit · 139-154 fwd*); money_level->home (416-157 fit · 202-114 fwd*); sharp_gap->home (201-326 fit · 117-169 fwd*); money_moving->home (209-316 fit · 126-158 fwd*); consensus_gap->home (140-272 fit · 88-73 fwd*) |
| Sat 15:00 | NIU@EIU | moneyline | home | -55.2 | 6-0 | 480 (+480) | 520 |  | 6% / 98% | 80 | follow_move->home (313-205 fit · 139-154 fwd*); rlm_ratio->home (37-80 fit · 30-72 fwd*); money_level->home (416-157 fit · 202-114 fwd*); sharp_gap->home (201-326 fit · 117-169 fwd*); money_moving->home (209-316 fit · 126-158 fwd*); consensus_gap->home (140-272 fit · 88-73 fwd*) |

