# CBB board

Generated 2026-11-21 02:51 UTC. Upcoming games with a FanDuel line. Every game is listed;
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
| PINNACLE moved vs public | ALST@FRES | total | under | Pinnacle | 147 -> 146.5 | **+1** | 146.5 | 6% | 10.17 | 140-157 fit · 1-2 fwd |
| FanDuel moved vs public | ALST@FRES | total | under | FanDuel | 152.5 -> 146.5 | **+1** | 146.5 | 6% | 10.17 | 200-225 fit · 2-7 fwd |
| FanDuel moved vs public | SLU@SMC | total | over | FanDuel | 158.5 -> 162.5 |  | 162.5 | 39% | 2.08 | 200-225 fit · 2-7 fwd |
| FanDuel moved vs public | SLU@SMC | moneyline | away | FanDuel | 112 -> 110 |  | 110 | 17% | 1.47 | 200-225 fit · 2-7 fwd |

## B  weighted ROI +10% to +20%

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Sat 11:00 | SIE@BUCK | moneyline | away | +13.1 | 1-1 | -265 (-265) | -205 |  | 0% / 0% | 95 | follow_move->away (314-205 fit · 7-7 fwd); consensus_gap->home (140-273 fit · 7-7 fwd) |
| Sat 14:00 | NIU@BGSU | moneyline | away | +13.1 | 1-1 | 184 (+184) | 188 |  | 0% / 0% | 85 | follow_move->away (314-205 fit · 7-7 fwd); consensus_gap->home (140-273 fit · 7-7 fwd) |

## D  no weighted edge (agreement is all unproven or money-losing signals)

| tip (ET) | game | market | lean | wt ROI | raw | FD now | open | Pin | tix / money (lean side) | bets | calls |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Sat 19:00 | MICH@VILL | moneyline | away **SPLIT** | -8.2 | 3-2 | -160 (-160) | -152 |  | 90% / 80% | 116 | follow_move->away (314-205 fit · 7-7 fwd); money_level->away (417-157 fit · 9-5 fwd); sharp_gap->home (201-327 fit · 1-10 fwd); money_moving->home (209-317 fit · 3-8 fwd); consensus_gap->away (140-273 fit · 7-7 fwd) |
| Fri 22:00 | ALST@FRES | spread | home **SPLIT** | -14 | 5-3 | -9.5 (-120) | -10.5 | -10 ($1,000) | 72% / 83% | 2090 | money_delta->away (122-125 fit · 1-2 fwd); follow_move->away (247-262 fit · 4-7 fwd); rlm_quiet->away (45-45 fit · 1-1 fwd); money_level->home (316-326 fit · 6-6 fwd); sharp_gap->home (324-310 fit · 4-8 fwd); money_moving->home (321-313 fit · 4-8 fwd); pin_value->home (158-147 fit · 3-2 fwd); pin_move->home (194-205 fit · 3-5 fwd) |
| Sat 14:00 | FOR@PORT | spread | home | -1 | 1-0 | 6.5 (-114) | 6.5 |  | 0% / 0% | 70 | consensus_gap->home (86-75 fit · 3-1 fwd) |
| Sat 11:00 | SCUS@UNCG | total | over | -3.4 | 1-0 | 145.5 (-110) | 145.5 |  | 0% / 0% | 65 | consensus_gap->over (105-101 fit · 5-3 fwd) |
| Sat 14:00 | FOR@PORT | total | over | -3.4 | 1-0 | 149.5 (-110) | 149.5 |  | 0% / 0% | 70 | consensus_gap->over (105-101 fit · 5-3 fwd) |
| Sat 19:00 | NAU@CP | total | over | -3.4 | 1-0 | 156.5 (-115) | 156.5 |  | 0% / 0% | 75 | consensus_gap->over (105-101 fit · 5-3 fwd) |
| Fri 22:00 | ALST@FRES | moneyline | home | -3.8 | 1-0 | -500 (-500) | -500 | -557 ($1,000) | 99% / 99% | 1999 | money_level->home (417-157 fit · 9-5 fwd) |
| Sat 14:00 | WCU@WAKE | moneyline | home | -4.2 | 3-1 | -1700 (-1700) | -1700 |  | 98% / 99% | 60 | money_level->home (417-157 fit · 9-5 fwd); sharp_gap->home (201-327 fit · 1-10 fwd); money_moving->home (209-317 fit · 3-8 fwd); consensus_gap->away (140-273 fit · 7-7 fwd) |
| Sat 11:00 | SIE@BUCK | total | over | -4.4 | 1-0 | 153.5 (-110) | 152.5 |  | 0% / 0% | 95 | follow_move->over (296-297 fit · 7-7 fwd) |
| Sat 13:00 | KENT@CLEV | total | under | -4.4 | 1-0 | 148.5 (-110) | 149.5 |  | 0% / 0% | 85 | follow_move->under (296-297 fit · 7-7 fwd) |
| Sat 13:00 | DEN@EMU | total | over | -4.4 | 1-0 | 138.5 (-115) | 137.5 |  | 0% / 0% | 95 | follow_move->over (296-297 fit · 7-7 fwd) |
| Sat 14:00 | UNM@WICH | total | under | -4.4 | 1-0 | 159.5 (-105) | 160.5 |  | 0% / 0% | 237 | follow_move->under (296-297 fit · 7-7 fwd) |
| Sat 14:00 | WCU@WAKE | total | under | -4.4 | 1-0 | 147.5 (-114) | 149.5 |  | 0% / 0% | 60 | follow_move->under (296-297 fit · 7-7 fwd) |
| Sat 15:00 | UST@MILW | total | under | -4.4 | 1-0 | 152.5 (-110) | 154.5 |  | 0% / 0% | 60 | follow_move->under (296-297 fit · 7-7 fwd) |
| Sat 16:00 | PENN@LAS | total | under | -4.4 | 1-0 | 160.5 (-110) | 161.5 |  | 0% / 0% | 85 | follow_move->under (296-297 fit · 7-7 fwd) |
| Sat 16:30 | UCI@USD | total | under | -4.4 | 1-0 | 141.5 (-110) | 144.5 |  | 0% / 0% | 75 | follow_move->under (296-297 fit · 7-7 fwd) |
| Sat 19:00 | MICH@VILL | total | under | -4.4 | 1-0 | 159.5 (-105) | 160.5 |  | 0% / 0% | 116 | follow_move->under (296-297 fit · 7-7 fwd) |
| Sat 13:00 | KENT@CLEV | moneyline | away | -4.8 | 1-0 | -160 (-160) | -152 |  | 0% / 0% | 85 | follow_move->away (314-205 fit · 7-7 fwd) |
| Sat 14:00 | FOR@PORT | moneyline | home | -4.8 | 1-0 | 210 (+210) | 225 |  | 0% / 0% | 70 | follow_move->home (314-205 fit · 7-7 fwd) |
| Sat 16:00 | PENN@LAS | moneyline | home | -4.8 | 1-0 | -118 (-118) | -113 |  | 0% / 0% | 85 | follow_move->home (314-205 fit · 7-7 fwd) |
| Sat 16:30 | UCI@USD | moneyline | away | -4.8 | 1-0 | -192 (-192) | -176 |  | 0% / 0% | 75 | follow_move->away (314-205 fit · 7-7 fwd) |
| Fri 23:00 | SLU@SMC | total | over | -5.8 | 6-1 | 162.5 (-110) | 158.5 |  | 39% / 81% | 7053 | money_delta->over (145-132 fit · 4-4 fwd); follow_move->over (296-297 fit · 7-7 fwd); rlm_ratio->over (122-102 fit · 2-1 fwd); money_level->over (351-322 fit · 8-8 fwd); sharp_gap->over (322-339 fit · 6-4 fwd); money_moving->over (317-347 fit · 6-6 fwd); consensus_gap->under (105-101 fit · 5-3 fwd) |
| Fri 22:00 | ALST@FRES | total | under | -6.4 | 8-0 | 146.5 (-112) | 152.5 | 146.5 ($500) **retraced +1** | 6% / 61% | 2090 | money_delta->under (145-132 fit · 4-4 fwd); follow_move->under (296-297 fit · 7-7 fwd); rlm_ratio->under (122-102 fit · 2-1 fwd); money_level->under (351-322 fit · 8-8 fwd); sharp_gap->under (322-339 fit · 6-4 fwd); money_moving->under (317-347 fit · 6-6 fwd); pin_move->under (198-188 fit · 5-3 fwd); pin_rlm->under (77-63 fit · 1-0 fwd) |
| Fri 23:00 | SLU@SMC | spread | away | -7.1 | 1-0 | 1.5 (-102) | 2.5 |  | 0% / 0% | 6775 | follow_move->away (247-262 fit · 4-7 fwd) |
| Sat 11:00 | SIE@BUCK | spread | away | -7.1 | 1-0 | -6.5 (-105) | -4.5 |  | 0% / 0% | 95 | follow_move->away (247-262 fit · 4-7 fwd) |
| Sat 13:00 | KENT@CLEV | spread | home | -7.1 | 1-0 | 3.5 (-106) | 4.5 |  | 0% / 0% | 85 | follow_move->home (247-262 fit · 4-7 fwd) |
| Sat 17:00 | AFA@UTSA | spread | away | -7.1 | 1-0 | 6.5 (-110) | 7.5 |  | 0% / 0% | 111 | follow_move->away (247-262 fit · 4-7 fwd) |
| Sat 22:00 | BRAD@PAC | spread | home | -7.1 | 1-0 | -9.5 (-108) | -8.5 |  | 0% / 0% | 65 | follow_move->home (247-262 fit · 4-7 fwd) |
| Sat 12:00 | DET@MSU | total | under | -7.8 | 2-0 | 150.5 (-110) | 151 |  | 0% / 0% | 70 | follow_move->under (296-297 fit · 7-7 fwd); consensus_gap->under (105-101 fit · 5-3 fwd) |
| Sat 14:00 | STON@SPC | total | under | -7.8 | 2-0 | 126.5 (-110) | 127.5 |  | 0% / 0% | 45 | follow_move->under (296-297 fit · 7-7 fwd); consensus_gap->under (105-101 fit · 5-3 fwd) |
| Sat 17:00 | AFA@UTSA | total | over | -7.8 | 2-0 | 172.5 (-110) | 170.5 |  | 0% / 0% | 111 | follow_move->over (296-297 fit · 7-7 fwd); consensus_gap->over (105-101 fit · 5-3 fwd) |
| Sat 19:00 | CBU@LMU | total | under | -7.8 | 2-0 | 138.5 (-110) | 139.5 |  | 0% / 0% | 55 | follow_move->under (296-297 fit · 7-7 fwd); consensus_gap->under (105-101 fit · 5-3 fwd) |
| Sat 11:00 | SCUS@UNCG | moneyline | away | -17.9 | 1-0 | 265 (+265) | 265 |  | 0% / 0% | 65 | consensus_gap->away (140-273 fit · 7-7 fwd) |
| Sat 15:00 | DRKE@MOSU | moneyline | away | -17.9 | 1-0 | -160 (-160) | -160 |  | 0% / 0% | 60 | consensus_gap->away (140-273 fit · 7-7 fwd) |
| Sat 19:00 | NAU@CP | moneyline | away | -17.9 | 1-0 | 265 (+265) | 265 |  | 0% / 0% | 75 | consensus_gap->away (140-273 fit · 7-7 fwd) |
| Sat 23:00 | WSU@DUKE | moneyline | away | -17.9 | 1-0 | 2500 (+2500) | 2500 |  | 0% / 0% | 95 | consensus_gap->away (140-273 fit · 7-7 fwd) |
| Fri 23:00 | SLU@SMC | moneyline | away | -28.5 | 6-1 | 110 (+110) | 112 |  | 17% / 25% | 7053 | follow_move->away (314-205 fit · 7-7 fwd); rlm_ratio->away (37-80 fit · 0-5 fwd); rlm_quiet->away (52-110 fit · 2-5 fwd); money_level->home (417-157 fit · 9-5 fwd); sharp_gap->away (201-327 fit · 1-10 fwd); money_moving->away (209-317 fit · 3-8 fwd); consensus_gap->away (140-273 fit · 7-7 fwd) |
| Sat 13:00 | DEN@EMU | moneyline | home | -40 | 4-0 | -310 (-310) | -310 |  | 99% / 100% | 95 | money_level->home (417-157 fit · 9-5 fwd); sharp_gap->home (201-327 fit · 1-10 fwd); money_moving->home (209-317 fit · 3-8 fwd); consensus_gap->home (140-273 fit · 7-7 fwd) |

