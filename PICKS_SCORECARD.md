# Picks scorecard — what was actually recommended

Generated 2026-11-23 01:51 UTC. Every pick ever logged, graded at the price and number
taken. `picks.json` is append-only: nothing here is edited or removed after
the fact, including the losers.

**Why this exists separately from the signal scorecards.** The picks are not
the board. They are the board filtered by price, Pinnacle's limit, and
judgment — and that filter had no record of its own. A scorecard can say
`rlm_ratio` is 39-49 forward; only this file can say whether overriding the
board helped. `board_rank` on each pick is what the engine said at the time,
so an override is countable rather than remembered selectively.

**Read CLV before the record.** At this sample size W/L is noise. CLV scores
every pick the moment its game closes and converges much faster: if the picks
are finding value, the number we bought beats the close even while the record
is losing.

## Overall

- **Record: 4-5-1**
- **Net: -0.73 units** (ROI -13.3% on 5.5u risked)
- **CLV: -0.05 average**, 20% of picks beat the close
- 0 pending, 1 unmatched

## Real money vs paper

Both are graded. Only the `real` rows are a P&L; `paper` rows are
engine evidence. A pick with no `stake` field counts as paper. 1u = $100.

| | picks | record | units | dollars |
|---|---|---|---|---|
| paper | 10 | 4-5-1 | -0.73u | **-$73** |


No open real-money risk.

## By sport

| | record | units | CLV avg |
|---|---|---|---|
| nfl | 1-0 | +0.46 | +0.00 |
| cbb | 3-5-1 | -1.18 | -0.06 |

## By what drove the pick

| | record | units | CLV avg |
|---|---|---|---|
| price vs Pinnacle, $30k limi | 1-0 | +0.46 | +0.00 |
| pin_rlm, Pinnacle moved + Fa | 1-0 | +0.46 | +0.00 |
| rlm_ratio + money ratio | 1-1 | -0.09 | +0.50 |
| pin_rlm, Pinnacle 149.5->147 | 0-1 | -0.50 | +0.00 |
| pin_rlm, Pinnacle 136.5->132 | 0-1 | -0.50 | -2.00 |
| pin_rlm + price vs Pinnacle | 1-2-1 | -0.54 | +0.12 |

## By market volume at close (PRE-DECLARED TEST)

| | record | units | CLV avg |
|---|---|---|---|
| 1k-2k | 1-1-1 | -0.04 | +0.17 |
| 2k-4k | 2-2 | -0.14 | +0.25 |
| 4k+ | 1-2 | -0.54 | -0.67 |

## By what the board said at the time

| | record | units | CLV avg |
|---|---|---|---|
| A +50.3 (lean agreed) | 1-0 | +0.46 | +0.00 |
| D -14.9 (OVERRIDE) | 1-0 | +0.46 | +0.00 |
| D -11.9 (OVERRIDE) | 1-0 | +0.46 | +1.00 |
| backfilled; taken at 172 not | 0-0-1 | +0.00 | -0.50 |
| C +5.3 (lean agreed) | 0-1 | -0.50 | +0.00 |
| C +3.8 (lean agreed) | 0-1 | -0.50 | -2.00 |
| backfilled | 1-3 | -1.09 | +0.25 |

## Every pick

| logged | sport | game | market | side | took | closed | CLV | result | units | driver | board said |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19T19:30 | cbb | WVU@FLA | total | under | 147.5 (-105) | 147.5 | 0.0 | **L** | -0.5 | pin_rlm, Pinnacle 149.5->147.5 on 13% tickets; 10,395 bets (only 4k+ volume play) | C +5.3 (lean agreed) |
| 2026-11-19T19:30 | cbb | UTEP@NMSU | total | under | 132.5 (-110) | 134.5 | -2.0 | **L** | -0.5 | pin_rlm, Pinnacle 136.5->132 (4.5pts) on 10% tickets, money/tix 6.6; 9-0 agreement | C +3.8 (lean agreed) |
| 2026-11-19T17:10 | cbb | UTU@WASH | spread | away | 17.5 (-110) | 17.5 | 0.0 | **W** | 0.455 | pin_rlm, Pinnacle moved + FanDuel held | D -14.9 (OVERRIDE) |
| 2026-11-19T17:10 | cbb | NE@BUT | total | under | 164.5 (-110) | 163.5 | 1.0 | **W** | 0.455 | pin_rlm + price vs Pinnacle | D -11.9 (OVERRIDE) |
| 2026-11-19T04:30 | nfl | Indianapolis Colts @ Houston Texans | spread | home | -12.5 (-110) | -12.5 | 0.0 | **W** | 0.455 | price vs Pinnacle, $30k limit | A +50.3 (lean agreed) |
| 2026-11-18T22:45 | cbb | HOW@DUQ | total | under | 139.5 (-110) | 139.5 | 0.0 | **L** | -0.5 | pin_rlm + price vs Pinnacle | backfilled |
| 2026-11-18T22:45 | cbb | UNH@STNH | total | under | 130.5 (-110) | 130.5 | 0.0 | **L** | -0.5 | pin_rlm + price vs Pinnacle | backfilled |
| 2026-11-18T22:45 | cbb | WEB@USU | total | over | 172 (-110) | 171.5 | -0.5 | **P** | 0.0 | pin_rlm + price vs Pinnacle | backfilled; taken at 172 not 171.5 |
| 2026-11-17T21:40 | cbb | KENN@ALA | total | over | 177.5 (-110) | 179.5 | 2.0 | **W** | 0.909 | rlm_ratio + money ratio | backfilled |
| 2026-11-17T21:40 | cbb | ODU@UVA | total | under | 144.5 (-105) | 145.5 | -1.0 | **L** | -1.0 | rlm_ratio + money ratio | backfilled |

## Unmatched — FLAGGED, not dropped

These could not be joined to a graded game. They are listed rather than
silently excluded, because a pick that quietly disappears is how a record
flatters itself.

- `2026-11-19T04:30Z` nfl Las Vegas Raiders @ Denver Broncos spread home
