# Picks scorecard — what was actually recommended

Generated 2026-11-20 00:44 UTC. Every pick ever logged, graded at the price and number
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

- **Record: 1-3-1**
- **Net: -1.09 units** (ROI -36.3% on 3u risked)
- **CLV: +0.10 average**, 20% of picks beat the close
- 4 pending, 0 unmatched

## By sport

| | record | units | CLV avg |
|---|---|---|---|
| cbb | 1-3-1 | -1.09 | +0.10 |

## By what drove the pick

| | record | units | CLV avg |
|---|---|---|---|
| rlm_ratio + money ratio | 1-1 | -0.09 | +0.50 |
| pin_rlm + price vs Pinnacle | 0-2-1 | -1.00 | -0.17 |

## By market volume at close (PRE-DECLARED TEST)

| | record | units | CLV avg |
|---|---|---|---|
| 1k-2k | 0-1-1 | -0.50 | -0.25 |
| 2k-4k | 1-2 | -0.59 | +0.33 |

## By what the board said at the time

| | record | units | CLV avg |
|---|---|---|---|
| backfilled; taken at 172 not | 0-0-1 | +0.00 | -0.50 |
| backfilled | 1-3 | -1.09 | +0.25 |

## Every pick

| logged | sport | game | market | side | took | closed | CLV | result | units | driver | board said |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19T17:10 | cbb | UTU@WASH | spread | away | 17.5 (-110) |  |  | **pending** |  | pin_rlm, Pinnacle moved + FanDuel held | D -14.9 (OVERRIDE) |
| 2026-11-19T17:10 | cbb | NE@BUT | total | under | 164.5 (-110) |  |  | **pending** |  | pin_rlm + price vs Pinnacle | D -11.9 (OVERRIDE) |
| 2026-11-19T04:30 | nfl | Las Vegas Raiders @ Denver Broncos | spread | home | -9.5 (-120) |  |  | **pending** |  | price vs Pinnacle only (board top band ignored) | A +69.2 (lean agreed) |
| 2026-11-19T04:30 | nfl | Indianapolis Colts @ Houston Texans | spread | home | -12.5 (-110) |  |  | **pending** |  | price vs Pinnacle, $30k limit | A +50.3 (lean agreed) |
| 2026-11-18T22:45 | cbb | HOW@DUQ | total | under | 139.5 (-110) | 139.5 | 0.0 | **L** | -0.5 | pin_rlm + price vs Pinnacle | backfilled |
| 2026-11-18T22:45 | cbb | UNH@STNH | total | under | 130.5 (-110) | 130.5 | 0.0 | **L** | -0.5 | pin_rlm + price vs Pinnacle | backfilled |
| 2026-11-18T22:45 | cbb | WEB@USU | total | over | 172 (-110) | 171.5 | -0.5 | **P** | 0.0 | pin_rlm + price vs Pinnacle | backfilled; taken at 172 not 171.5 |
| 2026-11-17T21:40 | cbb | KENN@ALA | total | over | 177.5 (-110) | 179.5 | 2.0 | **W** | 0.909 | rlm_ratio + money ratio | backfilled |
| 2026-11-17T21:40 | cbb | ODU@UVA | total | under | 144.5 (-105) | 145.5 | -1.0 | **L** | -1.0 | rlm_ratio + money ratio | backfilled |
